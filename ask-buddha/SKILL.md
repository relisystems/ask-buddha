---
name: ask-buddha
description: Explains how the Buddha of the Pali canon would see a question, read with modern knowledge as favourably as the evidence honestly allows. Use for any 'what would the Buddha say' question.
---

# ask-buddha: the Buddha's view from a modern perspective

This skill answers one kind of question: how does the Buddha of the Pali texts see this, and how
does that view look when read with the best modern knowledge? It was built for the *Thripitaka
Analysis Series*, a series of books that analyse Pali suttas, and it answers anyone's questions the
same way.

It is a method, not a persona. It speaks *about* the Buddha, in the third person, and never puts
modern words in his mouth or claims to speak for him. The series chose this, because
first-person ventriloquism would read as disrespectful to many Buddhist readers and would blur what
the texts say with what we infer.

## The sources, in order of authority

1. **The texts themselves.** Quote the Pali canon by reference (SuttaCentral uid, for example
   `mn47`, `an3.65:9.1`). Check every segment before quoting it:
   `python scripts/lookup.py mn36:27.7` (or `"MN 36:27.7-27.9"`, `--context 2`) prints its Pali and
   English. It reads a local copy of the canon when one is installed (the folder named by the
   environment variable `ASK_BUDDHA_CORPUS`, or `~/claude_work/literature/suttacentral`), which
   also covers the older translations' paragraph ids (`ja544:L4`) and the Dhammapada stories
   (`"DhA 01-09:P3"`). Otherwise it fetches the text from the SuttaCentral API (for example
   `https://suttacentral.net/api/bilarasuttas/mn47/sujato`). Some environments (claude.ai's code
   sandbox, for one) block a script's network access; there, open the same API address, or the
   reading page (`https://suttacentral.net/mn47/en/sujato`), with your own web-fetch tool. If nothing
   works, cite the profile's references, say that the text could not be checked, and quote nothing
   you have not seen.
   Translate from the Pali or check against it; never quote a modern translation as if it were your
   own words.
2. **The profile, `references/profile/`** (version 2, approved 23 November 2026, built from a reading
   of the whole canon): the Buddha as the canon portrays him, in thirteen section files. Open
   `00_index.md` first; read `01_purpose_and_limits.md` once for the labels and conventions; then read
   the sections that bear on the question (values, cognitive style, epistemic stance, temperament,
   ways with people, teaching, ethics, society, tensions, sayings, the modern lens, and the rules for
   this skill in section 13). Each trait carries a label and its evidence counts.
   `references/buddha_profile_sources.md` records the method.
3. **The series' own books, when they are available.** Each book's `content/passage*.html` (translations) and
   `content/analysis*.html` (the two readings) hold verified sources and verdicts. Keep faith with
   them: a favourable reading must never state as fact what a book's science-based analysis found
   false.
4. **Modern knowledge.** Use WebSearch (and a web-fetch tool if available) to consult PubMed,
   PubMed Central, Wikipedia, publishers' pages, and university repositories. Verify every study
   before citing it: authors, year, journal, sample size, and effect size as the paper reports them.
   Wikipedia is a map to sources, not a source to cite for contested points.

## How to answer a question

1. **Find the textual basis.** Which passages speak to it? Quote one or two lines with references.
   If the canon says nothing, say so plainly.
2. **Read the profile.** Which traits and stances apply (for example the middle way, the test of
   experience in the Kālāma Sutta, intention as kamma, compassion with firmness, silence on
   speculative questions)? Weigh them by their labels: build on [Strong] traits, name the group for
   a trait strong in only one ("in the Vinaya"), mark [Thin] ones, and state the complication of any
   trait marked "mixed".
3. **Bring modern evidence.** What do the best studies or scholarship show that bears on it? Check
   each source.
4. **Give the most favourable honest reading.** Prefer the strongest interpretation the texts can
   bear (psychological, ethical, or symbolic readings where the tradition itself offers them), and
   the strongest evidence that supports it.
5. **Mark the limits.** Separate three things in every answer: what the texts say; what the
   favourable modern reading infers; and where that reading stops (claims the evidence does not
   support, such as rebirth, devas, or miracles taken literally).

For a quick question, answer in a few short paragraphs under three labels: **In the texts**,
**Read today**, **Limits**.

**Write references out in full.** Most readers don't know codes like `AN 5.123:2.3`, so every
reference in an answer gives the collection's name and number, the text's title, and the paragraph,
keeps the short code in brackets for those who use it, and links to the text on SuttaCentral. For
example: *a discourse called "A Carer" (Aṅguttara Nikāya 5.123, paragraph 2) [AN 5.123:2.3]*, linked
to `https://suttacentral.net/an5.123/en/sujato`. Paragraph numbers are the ones in the margin of
SuttaCentral's pages; links can't jump to a paragraph, so name it.
- `python scripts/lookup.py --cite an5.123:2.3 "Kd 8:26.3.13"` writes each reference out in that
  form (the profile's codes work as they are), and every ordinary lookup begins with the same
  "Cite as" line.
- Where scripts can't run, write it out from the code yourself: DN Dīgha Nikāya, MN Majjhima Nikāya,
  SN Saṃyutta Nikāya, AN Aṅguttara Nikāya, Kd Vinaya Khandhaka (Kd 1–10 are Mahāvagga I–X, Kd 11–22
  Cūḷavagga I–XII), Bu-Vb/Bi-Vb the Vinaya's analysis of the monks'/nuns' rules, DhA the Dhammapada
  Commentary; the link is `https://suttacentral.net/<uid>` (for example `mn47`, `pli-tv-kd8`).
- End an answer with a short "Texts cited" list of those links, before any list of modern sources.
- In the series' books, follow the book's own style instead (for example "(Saṃyutta Nikāya 16.5)").

## How to write a "Buddha's View from a Modern Perspective" section

This replaces the favourable reading (formerly *Saddhā*, "the case for") in a book of the series.
The first use was Book 1's second edition. The science-based
reading (formerly *Vīmaṃsā*) stays exactly as it is.

**Fit.** Same place, same length: two facing pages, **690–880 words**, inside
`<section id="saddha">…</section>` of `content/analysisNN.html`. Keep the HTML conventions of the
book (`<h3>` headings, `<p>` paragraphs, `<i>` for Pali, author–year citations such as
"(Goyal and colleagues, 2014)"). Every work cited must be in the book's `sources.html`; add any new
one there, in its alphabetical place and section.

**Headings.** Use these five, in this order:

1. `The Buddha’s point`: what the passage teaches, in its own terms and the Buddha's words.
2. `How he saw it`: the passage in the light of the Buddha's character and method as the wider
   canon portrays them (from the profile), with one or two cross-references.
3. `What modern knowledge adds`: the strongest verified evidence and scholarship in its favour.
4. `Answering the critics`: the best honest replies to the science-based reading's main
   objections, granting what must be granted.
5. `Why it matters today`: the most favourable modern application, kept to what the evidence
   allows.

**Standards.**

- *Most favourable, never false.* Choose the strongest readings and evidence; never invent texts,
  misstate a study, inflate an effect size, or claim that science confirms what it does not.
  Report figures exactly as the paper does.
- *Third person.* "The Buddha's teaching here holds that…", "As the texts portray him, he…".
  Never "I".
- *Texts and inference kept apart.* Signal inference: "read today", "on the most favourable
  reading", "the tradition's own psychological reading". Report traditional accounts as tradition.
- *Cosmology and miracles.* Present the tradition's symbolic or psychological readings where it
  offers them (for example the Brahmā realms as states of meditation), and say they are readings.
  Do not assert devas, rebirth, or miracles as facts.
- *Concessions in one place.* The science-based section carries the full case against, so the
  favourable section concedes limits briefly, inside `Answering the critics`, and keeps the rest
  of its space for the Buddha's case. (For quick questions outside the books, the profile's rule
  to state a limit with every favourable reading still applies.) These five headings take
  precedence over the general template in section 13.2 of the profile.
- *Consistency.* Do not contradict the book's own science-based verdicts. Where the favourable
  reading and the verdict differ, the favourable section may argue its reading, but it must not
  misreport the evidence the verdict rests on.
- *Series style.* British spelling, plain English, sentence-case headings, and the same terms as
  the book's translation.

**Check.** After writing, run the book's layout build (`python build.py --html`) and confirm that no
analysis page overflows and every second page is between 0.6 and 0.95 full. Shorten or lengthen to
fit; never change the passage, the illustration, or the science-based section to make room.

## What this skill is not

Not a religious authority, not a claim about the historical Buddha's mind, and not a substitute for
the science-based reading. It gives the Buddha's case its best honest hearing, so that readers can
weigh it against the evidence and decide for themselves, as the Kālāma Sutta asks.
