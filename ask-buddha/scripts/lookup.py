"""Print the Pali and English of a canon segment (or a range) from the local corpus.

Usage:
  python lookup.py mn36:27.7
  python lookup.py "MN 36:27.7-27.9"        (display names work too: DN, MN, SN, AN, Ja, Kd 17, Bu-Vb-Pj1, DhA 01-09, ...)
  python lookup.py ja544:L4 dhp-a01-09:P3   (older translations' paragraphs, Dhammapada stories)
  python lookup.py an3.65:4.1-4.3 --context 2
  python lookup.py sn56.11                  (the whole text, first 60 segments; --all for every segment)
  python lookup.py --cite an5.123:2.3 "Kd 8:26.3.13"   (only the full reference for readers, no text)

Each result begins with a "Cite as" line: the reference written out for a reader who doesn't know the
short codes (collection name, number, title, paragraph, and a link to the text on SuttaCentral).

A local copy of the canon is optional. When present (the folder given by --corpus PATH, the environment
variable ASK_BUDDHA_CORPUS, or ~/claude_work/literature/suttacentral), it reads work/segments.jsonl there,
which holds every segment id the profile cites, including the L (older translations' paragraphs) and P
(Dhammapada story paragraphs) ids. Without it, or when it lacks the text, it fetches the text from the
SuttaCentral API (segmented texts only: the suttas, the Vinaya, and the Abhidhamma). Python 3 standard library only.
"""
import argparse
import csv
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

DEFAULT = Path.home() / "claude_work" / "literature" / "suttacentral"
COLL = {"DN": "dn", "MN": "mn", "SN": "sn", "AN": "an", "Kp": "kp", "Dhp": "dhp", "Ud": "ud", "Iti": "iti",
        "Snp": "snp", "Vv": "vv", "Pv": "pv", "Thag": "thag", "Thig": "thig", "Ja": "ja", "Bv": "bv", "Cp": "cp",
        "Tha-ap": "tha-ap", "Thi-ap": "thi-ap", "Mnd": "mnd", "Cnd": "cnd", "Ps": "ps", "Ne": "ne", "Pe": "pe",
        "Mil": "mil", "Ds": "ds", "Vb": "vb", "Dt": "dt", "Pp": "pp", "Kv": "kv", "Ya": "ya", "Paṭṭhāna": "patthana",
        "Kd": "pli-tv-kd", "Pvr": "pli-tv-pvr", "DhA": "dhp-a"}

# uid prefix -> (short code, full name). The longest matching prefix wins; the number must follow it.
NAMES = {
    "dn": ("DN", "Dīgha Nikāya"), "mn": ("MN", "Majjhima Nikāya"), "sn": ("SN", "Saṃyutta Nikāya"),
    "an": ("AN", "Aṅguttara Nikāya"), "kp": ("Kp", "Khuddakapāṭha"), "dhp": ("Dhp", "Dhammapada"),
    "ud": ("Ud", "Udāna"), "iti": ("Iti", "Itivuttaka"), "snp": ("Snp", "Sutta Nipāta"),
    "vv": ("Vv", "Vimānavatthu"), "pv": ("Pv", "Petavatthu"), "thag": ("Thag", "Theragāthā"),
    "thig": ("Thig", "Therīgāthā"), "ja": ("Ja", "Jātaka"), "bv": ("Bv", "Buddhavaṃsa"),
    "cp": ("Cp", "Cariyāpiṭaka"), "tha-ap": ("Tha-ap", "Therāpadāna"), "thi-ap": ("Thi-ap", "Therī-apadāna"),
    "mnd": ("Mnd", "Mahāniddesa"), "cnd": ("Cnd", "Cūḷaniddesa"), "ps": ("Ps", "Paṭisambhidāmagga"),
    "ne": ("Ne", "Nettippakaraṇa"), "pe": ("Pe", "Peṭakopadesa"), "mil": ("Mil", "Milindapañha"),
    "ds": ("Ds", "Dhammasaṅgaṇī"), "vb": ("Vb", "Vibhaṅga"), "dt": ("Dt", "Dhātukathā"),
    "pp": ("Pp", "Puggalapaññatti"), "kv": ("Kv", "Kathāvatthu"), "ya": ("Ya", "Yamaka"),
    "patthana": ("Paṭṭhāna", "Paṭṭhāna"), "pli-tv-kd": ("Kd", "Vinaya, Khandhaka"),
    "pli-tv-pvr": ("Pvr", "Vinaya, Parivāra"), "dhp-a": ("DhA", "Dhammapada Commentary, story"),
}
NIKAYA_EN = {"dn": "Long Discourses", "mn": "Middle Discourses", "sn": "Linked Discourses",
             "an": "Numbered Discourses"}
RULES = {"pj": "Pārājika", "ss": "Saṅghādisesa", "ay": "Aniyata", "np": "Nissaggiya Pācittiya",
         "pc": "Pācittiya", "pd": "Pāṭidesanīya", "sk": "Sekhiya", "as": "Adhikaraṇasamatha"}
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
_manifest = None


def parse(ref):
    """'MN 36:27.7–27.9' -> ('mn36', '27.7', '27.9')."""
    ref = ref.strip().replace("–", "-")
    text, _, segs = ref.partition(":")
    m = re.match(r"^(B[ui]-(?:Vb-[A-Za-z]+\d*(?:-\d+)?|Pm))$", text, re.I)
    if m:
        uid = "pli-tv-" + m.group(1).lower()
    else:
        m = re.match(r"^([A-Za-zṭ\-]+?)\s+(\S+)$", text)
        uid = (COLL.get(m.group(1), m.group(1).lower()) + m.group(2)) if m else text.lower()
    a, _, b = segs.partition("-")
    if b and "." in a and "." not in b and b[:1] not in "LP":
        b = a.rsplit(".", 1)[0] + "." + b                     # 27.7-9 means 27.7 to 27.9
    if b and a[:1] in "LP" and b[:1] not in "LP":
        b = a[0] + b                                           # L4-6 means L4 to L6
    return uid, a, b


def from_corpus(corpus, uid):
    path = corpus / "work" / "segments.jsonl"
    if not path.exists():
        return None
    key, rows = f'"uid": "{uid}"', []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("{" + key + ","):
                r = json.loads(line)
                rows.append((r["seg"], r["pali"].strip(), r["en"].strip()))
            elif rows:
                break                                          # a text's segments are contiguous
    return rows or None


def get_json(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "sutta-reader/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except Exception:
        return None


def from_api(uid):
    for author in ("sujato", "brahmali"):
        d = get_json(f"https://suttacentral.net/api/bilarasuttas/{uid}/{author}") or {}
        keys, root, tr = d.get("keys_order") or [], d.get("root_text") or {}, d.get("translation_text") or {}
        if keys:
            return [(k.split(":", 1)[1], root.get(k, "").strip(), tr.get(k, "").strip()) for k in keys]
    return None


def titles(corpus, uid):
    """(Pali title, English title, English translator) from the local manifest, else SuttaCentral."""
    global _manifest
    if _manifest is None:
        _manifest = {}
        path = corpus / "manifest.csv"
        if path.exists():
            with open(path, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f):
                    _manifest[r["uid"]] = (r["title_pali"], r["title_en"], r["en_author"])
    if uid in _manifest:
        return _manifest[uid]
    d = get_json(f"https://suttacentral.net/api/suttaplex/{uid}")
    d = (d[0] if isinstance(d, list) and d else d) or {}
    en = [t for t in d.get("translations") or [] if t.get("lang") == "en"]
    en.sort(key=lambda t: (not t.get("segmented"), t.get("author_uid") not in ("sujato", "brahmali")))
    return ((d.get("original_title") or "").strip(), (d.get("translated_title") or "").strip(),
            en[0].get("author_uid", "") if en else "")


def cite(corpus, uid, a, b, rows=None):
    """The reference written out for a reader: name and number, title, paragraph, short code, link."""
    m = re.match(r"^pli-tv-(bu|bi)-vb-([a-z]+)(\d+(?:-\d+)?)$", uid)
    if m:
        code = f"{m.group(1).capitalize()}-Vb-{m.group(2).capitalize()}{m.group(3)}"
        name = (f"Vinaya, {'Monks' if m.group(1) == 'bu' else 'Nuns'}’ Analysis "
                f"({'Bhikkhu' if m.group(1) == 'bu' else 'Bhikkhunī'} Vibhaṅga), "
                f"{RULES.get(m.group(2), m.group(2))} {m.group(3).replace('-', '–')}")
    elif re.match(r"^pli-tv-(bu|bi)-pm$", uid):
        code = uid[7:9].capitalize() + "-Pm"
        name = f"Vinaya, {'Monks' if 'bu' in uid else 'Nuns'}’ Pātimokkha"
    else:
        prefix = max((p for p in NAMES if uid.startswith(p) and uid[len(p):][:1].isdigit()), key=len, default=None)
        if not prefix:
            return f"{uid} (https://suttacentral.net/{uid})"
        num = uid[len(prefix):]
        short, full = NAMES[prefix]
        code = f"{short} {num}"
        if prefix == "dhp-a":
            num = ".".join(str(int(n)) for n in num.split("-"))
        name = f"{full} {num.replace('-', '–')}"
        if prefix == "pli-tv-kd" and num.isdigit() and 1 <= int(num) <= 22:
            n = int(num)
            name += f" ({'Mahāvagga ' + ROMAN[n] if n <= 10 else 'Cūḷavagga ' + ROMAN[n - 10]})"
        elif prefix in NIKAYA_EN:
            name += f" ({NIKAYA_EN[prefix]})"
    pali, en, author = titles(corpus, uid)
    if uid.startswith("dhp-a") and rows:
        heads = [e for k, _, e in rows if k == "P1" and e]
        en = re.sub(r"^\d+\.\d+\s+", "", heads[0]) if heads else en
    title = f", “{en}”" + (f" ({pali})" if pali and pali != en else "") if en or pali else ""
    if en == "" and pali:
        title = f", {pali}"
    para = ""
    if a:
        p = lambda s: s if s[:1] in "LP" or "." not in s else s.rsplit(".", 1)[0]
        pa, pb = p(a), p(b) if b else p(a)
        para = f", paragraph {pa[1:] if pa[:1] in 'LP' else pa}" if pa == pb else \
            f", paragraphs {pa[1:] if pa[:1] in 'LP' else pa}–{pb[1:] if pb[:1] in 'LP' else pb}"
    short = code + (f":{a}" + (f"–{b}" if b else "") if a else "")
    if uid.startswith("dhp-a"):
        where = "Burlingame’s translation, revised by Ānandajoti (not on SuttaCentral)"
    else:
        where = f"https://suttacentral.net/{uid}" + (f"/en/{author}" if author else "")
    return f"{name}{title}{para} [{short}] {where}"


def matches(seg, a):
    return seg == a or seg.startswith(a + ".")


def main():
    ap = argparse.ArgumentParser(description="Print canon segments from the local corpus.")
    ap.add_argument("refs", nargs="+")
    ap.add_argument("--context", type=int, default=0, help="segments of context before and after")
    ap.add_argument("--all", action="store_true", help="print a whole text without the 60-segment cap")
    ap.add_argument("--cite", action="store_true", help="print only each reference written out in full")
    ap.add_argument("--corpus", default=os.environ.get("ASK_BUDDHA_CORPUS")
                    or os.environ.get("MODERN_BUDDHA_CORPUS") or str(DEFAULT))   # the old name still works
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    corpus = Path(args.corpus)
    status = 0
    for ref in args.refs:
        uid, a, b = parse(ref)
        if args.cite:
            print(cite(corpus, uid, a, b, from_corpus(corpus, uid) if uid.startswith("dhp-a") else None))
            continue
        rows, source = from_corpus(corpus, uid), "local corpus"
        if rows is None:
            rows, source = from_api(uid), "SuttaCentral API"
        if not rows:
            print(f"== {ref}: text {uid} not found (local corpus and API)\n")
            status = 1
            continue
        keys = [k for k, _, _ in rows]
        if a:
            starts = [i for i, k in enumerate(keys) if matches(k, a)]
            if not starts:
                hint = (" (L and P paragraph ids come from the local corpus; on SuttaCentral, open "
                        f"https://suttacentral.net/{uid} and find the passage by its words)"
                        if source == "SuttaCentral API" and a[:1] in "LP" else "")
                print(f"== {ref}: segment {a} not in {uid}{hint}\n")
                status = 1
                continue
            i = starts[0]
            # the first match at or after the start, then on while ids still match (range texts such as
            # an1.51-60 repeat segment ids for each sutta, so never jump to a later repeat)
            j = next((n for n in range(i, len(keys)) if matches(keys[n], b or a)), i)
            while j + 1 < len(keys) and matches(keys[j + 1], b or a):
                j += 1
            lo, hi = max(0, i - args.context), min(len(rows), j + 1 + args.context)
        else:
            lo, hi = 0, len(rows) if args.all else min(len(rows), 60)
        print(f"== {uid}:{a}{'-' + b if b else ''} ({source})")
        print(f"Cite as: {cite(corpus, uid, a, b, rows)}")
        for k, pali, en in rows[lo:hi]:
            if pali:
                print(f"{uid}:{k}  {pali}")
            if en:
                print(f"{' ' * len(uid + ':' + k)}  {en}")
        if not a and hi < len(rows):
            print(f"... {len(rows) - hi} more segments (use --all)")
        print()
    sys.exit(status)


if __name__ == "__main__":
    main()
