# Sources for the Buddha profile, version 2

This is the method record for the profile in `references/profile/` (version 2). Version 2 rests on a reading of the whole Pali canon. Part A records that method; Part B keeps the record of version 1 (the random sample of 48 texts, seed 84000), whose findings version 2 revised. Compiled 23 November 2026.

## Part A. The whole-canon method (version 2)

The author keeps the corpus, scripts, evidence, and tallies named below; this record summarises them.

### A1. The corpus (step 1, 22 November 2026)

- **Source:** the SuttaCentral API (`/api/suttaplex`, `/api/bilarasuttas`, `/api/suttas`), fetched by `fetch_corpus.py`. 7,288 texts: the Sutta Piṭaka (DN, MN, SN, AN, and the Khuddaka Nikāya), the Vinaya Piṭaka (both Vibhaṅgas, the Khandhakas, the Parivāra, and the two Pātimokkhas, fetched whole), and the Abhidhamma Piṭaka. About 2.8 million Pali words (Mahāsaṅgīti edition) and 5.1 million English words.
- **English:** Bhikkhu Sujato (suttas) and Bhikkhu Brahmali (Vinaya) where available; other segmented translations next; older translations last (for the Jātaka prose, the Cowell edition by Chalmers and colleagues). 870 texts have no English and were handled separately (A3).
- **Commentary:** the Dhammapada commentary's stories in English (Burlingame 1921, revised by Ānandajoti 2024, from ancient-buddhist-texts.net; 305 stories on 308 pages), fetched by `fetch_dhammapada_stories.py`. The Pali Dhammapadaṭṭhakathā (VRI, `s0502a.att.xml`) was also saved, for checking only (its licence covers non-commercial use).
- Record: `CORPUS_SUMMARY.md`, `manifest.csv`, `fetch_log.txt`.

### A2. Preparation (step 2, 22 November 2026)

`prepare.py` built a segment table (`work/segments.jsonl`), removed repeated stock passages (runs of 40 words or more found elsewhere; the first occurrence in canonical order kept; 8.8 per cent of the English removed), guessed speakers by heuristics (about 77 per cent right in a check of 26 quotations), and cut the canon into 108 reading chunks of about 100,000 tokens, one collection per chunk. Record: `work/prepare_report.md`.

### A3. Extraction (step 3, 22 to 23 November 2026)

- One agent per chunk read it in full with a fixed brief (kept in the workflow script; summarised in the how-to) and the trait list of version 1 (`work/traits.md`, 71 ids). For each text it recorded the clearest evidence for each trait, at most three lines per trait per text: trait, location, an exact quotation of at most 25 words, a paraphrase, the speaker, the layer, and the stance (supports, complicates, or counter-example). It also flagged every text (does the Buddha speak, appear, or neither; are gods, rebirth or past lives, or wonders present) and proposed traits the list lacked.
- The texts with no English: one agent read all 29 Buddhavaṃsa texts in Pali and samples of the Mahāniddesa, Cūḷaniddesa, Vimānavatthu, Petavatthu, Paṭṭhāna, Theragāthā-apadāna, and Dhammasaṅgaṇī.
- A pilot was checked by hand (ten quotations against the texts) and the brief tightened before the full run.
- `check_evidence.py` compared every quotation with its cited segments: 13,820 lines, 99.8 per cent exact, 23 problem lines (excluded from version 2). Record: `evidence/check_report.md`.

### A4. Synthesis (step 4, 23 November 2026)

- `tally.py` merged the evidence (`work/evidence.jsonl`), counted it per trait by group, layer, stance, and speaker (`work/tallies.csv`, `work/tallies.md`), and wrote each section's evidence and a digest for the writers (`work/by_section/`).
- The attestation rules (version 2, section 1) were calibrated on these tallies.
- Six writing agents, each with the same brief (`work/step4_brief.md`), rewrote sections 2 to 10 from the digests, keeping version 1's structure and findings unless the evidence overturned them, and recording their changes (`work/profile_v2/sec_NN_changes.md`). Sections 1, 11, 12, and 13 were revised by the coordinating session. Quotations may come only from checked evidence lines or from version 1.

### A5. Limits of the method

- The agents looked for version 1's traits, so traits outside that list are undercounted.
- Counts are of texts, and a short list in the Aṅguttara counts as much as a long discourse.
- The speaker and stance of each line are the reading agent's judgement; the quotations were checked by script, the judgements only by sampling.
- The Pali-only collections were sampled, not read in full.
- The commentaries other than the Jātaka prose and the Dhammapada stories were not read.

---

## Part B. The record of version 1

This is the sample record for version 1 (not included in this package). It records the seed, how the list of texts was built, the 48 texts drawn, the substitutions, and the books and other passages used. Compiled 22 November 2026.

### 1. The seed

**Seed: 84000.** Python's `random` module (Python 3.14) was seeded once with `random.seed(84000)` and used for every stratum in a fixed order.

### 2. How the list of uids was built

All data came from the SuttaCentral API (`https://suttacentral.net/api`), held in memory and cached as JSON in a scratch folder. Nothing was downloaded beyond API responses.

1. **Endpoint.** `GET /api/suttaplex/{uid}` returns a flat list of every node under a division. Only nodes with `type == "leaf"` and `root_lang == "pli"` were kept. A leaf is SuttaCentral's unit of text: a sutta, a range of short suttas (for example `an2.141-150`), a Vinaya rule, or an Abhidhamma section. English availability was read from each leaf's `translations` list (entries with `lang == "en"`).
2. **Sutta Piṭaka.** Suttaplex for `dn`, `mn`, `sn`, `an`, and `kn`. The Khuddaka Nikāya here includes the Khuddakapāṭha, Dhammapada, Udāna, Itivuttaka, Sutta Nipāta, Vimānavatthu, Petavatthu, Thera- and Therīgāthā, Apadāna, Buddhavaṃsa, Cariyāpiṭaka, Jātaka, Niddesa, Paṭisambhidāmagga, Nettippakaraṇa, Peṭakopadesa, and Milindapañha, as SuttaCentral arranges it.
3. **Vinaya Piṭaka.** The brief asked for rule origin stories and Khandhaka episodes, so the pool has two parts:
   - **Vibhaṅga rules.** Suttaplex for `pli-tv-bu-vb` (monks) and `pli-tv-bi-vb` (nuns): 347 rule leaves, each with its origin story.
   - **Khandhaka sections.** SuttaCentral treats each of the 22 Khandhaka chapters as one leaf, and some chapters run to hundreds of episodes. So each chapter's segment keys were read from `GET /api/bilarasuttas/pli-tv-kdN/brahmali`, and the chapter was divided at its top-level section numbers (`pli-tv-kd1:1` to `pli-tv-kd1:79`, and so on). Section 0, which holds only headings, was dropped. This gave 462 sections, closer to the tradition's idea of a *dhammakkhandha* as a unit on one topic.
   - **Not included:** the Parivāra (a later digest with no origin stories) and the bare Pātimokkha texts.
4. **Abhidhamma Piṭaka.** Suttaplex for `pli-tv-ab`: leaves of the Dhammasaṅgaṇī, Vibhaṅga, Dhātukathā, Puggalapaññatti, Kathāvatthu, Yamaka, and Paṭṭhāna.
5. **Exclusions** (texts the eleven books already cover):
   - sn56.11, snp2.4, snp1.8, snp2.1, mn10, mn118, an3.65, dn31, sn22.59, dn16
   - kp5, kp6, kp9 (verbatim copies of the Maṅgala, Ratana, and Metta suttas)
   - the 19 Dhammapada chapter leaves from which Book 11 draws verses (dhp1-20, 21-32, 33-43, 44-59, 60-75, 100-115, 116-128, 129-145, 146-156, 157-166, 179-196, 197-208, 209-220, 221-234, 273-289, 320-333, 334-359, 360-382, 383-423)
   - pli-tv-kd1:6, the Khandhaka section that contains SN 56.11 and SN 22.59 word for word
6. **Order.** Each pool was sorted in natural uid order (numbers compared as numbers) before shuffling, so the result does not depend on the order the API returns.

#### Pool sizes (API state on 22 November 2026)

| Stratum | Leaves or sections | After exclusions | With English on SuttaCentral | Drawn |
|---|---|---|---|---|
| DN | 34 | 32 | 32 | 6 |
| MN | 152 | 150 | 150 | 6 |
| SN | 1,819 | 1,817 | 1,817 | 6 |
| AN | 1,408 | 1,407 | 1,407 | 6 |
| Khuddaka Nikāya | 2,351 | 2,326 | 2,164 | 6 |
| Vinaya (347 rules + 462 sections) | 809 | 808 | 808 | 10 |
| Abhidhamma | 1,102 | 1,102 | 395 | 8 |

**Allocation.** The 30 suttas were split equally, six per collection. "Spread across DN, MN, SN, AN, and the Khuddaka Nikāya" rules out proportional allocation, which would give DN no texts at all (32 of about 5,700 leaves).

### 3. The drawing procedure

```python
import random
random.seed(84000)
STRATA = [("dn", 6), ("mn", 6), ("sn", 6), ("an", 6), ("kn", 6), ("vinaya", 10), ("abhidhamma", 8)]
for name, k in STRATA:
    pool = pools[name]                         # sorted in natural uid order
    sequence = random.sample(pool, len(pool))  # the whole pool, shuffled
    # sample = the first k usable texts in `sequence`; substitutes = the next ones in it
```

**Usability rule** (from the brief): a text is unusable if it has *no English translation on SuttaCentral and no clear Buddha content*. Both conditions must hold.

- Texts with English were kept even when they say little about the Buddha (for example thag1.44). Their silence is itself data.
- **bv8** has no English but is plainly about Buddhas, framed as the Buddha's own account. It was kept and read in Pali.
- Every **Paṭṭhāna** text drawn had no English and no Buddha content, so each was replaced by the next text in the sequence.

**Readings used.** Suttas: Bhikkhu Sujato (bilara). Vinaya: Bhikkhu Brahmali (bilara). Jātaka: the legacy Cowell-edition translations on SuttaCentral (Rouse, Chalmers), which translate the commentary's prose frame around the canonical verses. Kathāvatthu: Shwe Zan Aung and C. A. F. Rhys Davids (legacy). Yamaka: U Nārada, U Nandamedha, and U Kumārābhivaṃsa (legacy).

### 4. The 48 sampled texts

#### Sutta Piṭaka: Dīgha Nikāya (6)

| # | uid | Title | What it showed |
|---|---|---|---|
| 1 | dn14 | Mahāpadānasutta, *The Great Discourse on Traces Left Behind* | Seven past Buddhas, with Vipassī's life as the template for every Buddha. Knowledge claimed both from "penetrating the principle" and because "deities told me". Vipassī's backward causal search and reluctance to teach. |
| 2 | dn12 | Lohiccasutta, *With Lohicca* | Socratic questions from the brahmin's own estate show that withholding the good harms others. Teachers are judged by results. Wrong view leads to hell. |
| 3 | dn21 | Sakkapañhasutta, *Sakka's Questions* | Praises a musician's harmony and drily queries a love song that uses his name. Greets gods with "all want to be happy". Traces conflict to jealousy and stinginess, born of the liked and disliked. An outcome test for conduct. Admits chariot wheels broke his meditation. |
| 4 | dn33 | Saṅgītisutta, *Reciting in Concert* | "My back is sore." Delegates the teaching to Sāriputta and approves him. Lists recited to prevent a schism like the Jains'. |
| 5 | dn18 | Janavasabhasutta, *With Janavasabha* | On Ānanda's suggestion, declares the rebirths of Magadhan devotees to raise confidence. A chain of divine testimony. King Bimbisāra reborn as a spirit. |
| 6 | dn11 | Kevaṭṭasutta, *With Kevaddha* | Refuses miracles as proof, since a sceptic would credit a charm. Only instruction counts. Satirises the Creator-Brahmā. Reframes a badly put question. |

#### Sutta Piṭaka: Majjhima Nikāya (6)

| # | uid | Title | What it showed |
|---|---|---|---|
| 7 | mn36 | Mahāsaccakasutta, *The Longer Discourse With Saccaka* | Austerity pushed to its limit and abandoned. Refuses gods' nectar because it would make his fast a lie. The childhood-meditation memory. Admits resting in the day. Composure under hostile criticism. |
| 8 | mn115 | Bahudhātukasutta, *Many Elements* | "Be astute inquirers." Analysis into elements. A list of the possible and impossible, including the women's impossibilities, which are absent from the Madhyama-āgama parallel. |
| 9 | mn107 | Gaṇakamoggallānasutta, *With Moggallāna the Accountant* | Graduated training by the horse-trainer simile. "The Realized One is the one who shows the way." Not every pupil succeeds. |
| 10 | mn14 | Cūḷadukkhakkhandhasutta, *The Shorter Discourse on the Mass of Suffering* | Insight does not end desire without a higher happiness. Sensuality causes wars and crime. A sharp debate with Jain ascetics. "Who lives in greater pleasure, Bimbisāra or I?" |
| 11 | mn41 | Sāleyyakasutta, *The People of Sālā* | Ten courses of action taught to lay householders, briefly and then in detail. Right view includes the afterlife. "Not knowing, they say 'I don't know.'" |
| 12 | mn89 | Dhammacetiyasutta, *Shrines to the Teaching* | Questions King Pasenadi's veneration of "this body". The king infers the Buddha's worth from the community's conduct, and the Buddha endorses it as "shrines to the teaching". Both men are eighty. |

#### Sutta Piṭaka: Saṃyutta Nikāya (6)

| # | uid | Title | What it showed |
|---|---|---|---|
| 13 | sn12.15 | Kaccānagottasutta, *Kaccānagotta* | The middle way between "all exists" and "all does not exist". Dependent origination. Knowledge "independent of others". |
| 14 | sn48.14 | Tatiyasaṃkhittasutta, *In Brief (3rd)* | Five faculties and graded attainment. "If you practice partially you succeed partially." |
| 15 | sn22.55 | Udānasutta, *An Inspired Saying* | Analysis of the aggregates. Consciousness that is not established is freed, "content... not anxious". |
| 16 | sn45.165 | Dukkhatāsutta, *Forms of Suffering* | Three forms of suffering and the path to end them. A bare doctrinal formula. |
| 17 | sn46.48 | Ādiccasutta, *The Sun* | Good friendship is the dawn of the factors of awakening. |
| 18 | sn20.9 | Nāgasutta, *A Bull Elephant* | Elephant calves imitate the bulls badly: a simile for junior monks. Use gifts without attachment. |

#### Sutta Piṭaka: Aṅguttara Nikāya (6)

| # | uid | Title | What it showed |
|---|---|---|---|
| 19 | an7.79 | Paṭhamavinayadharasobhanasutta, *Shines as an Expert in the Monastic Law (1st)* | A legal expert needs ethics and meditation as well as knowledge of the rules. A list, with no narrative. |
| 20 | an3.30 | Avakujjasutta, *Upside-down* | Three kinds of listener: a pot upside down, food in the lap, a pot set upright. Concern for what listeners retain. |
| 21 | an6.67 | Mittasutta, *Friends* | Good friends make the training possible; bad friends make it impossible. A chain of conditions. |
| 22 | an2.141-150 | Dānavagga, *Giving* | Ten pairs: giving, sharing, and sympathy in the teaching are better than in material things. |
| 23 | an8.64 | Gayāsīsasutta, *At Gayā Head* | Refines his visionary knowledge of gods in eight rounds before announcing awakening. The same formula as SN 56.11. |
| 24 | an4.51 | Paṭhamapuññābhisandasutta, *Overflowing Merit* | Donors' merit becomes boundless when the monks they support meditate deeply. The community's merit economy. |

#### Sutta Piṭaka: Khuddaka Nikāya (6)

| # | uid | Title | What it showed |
|---|---|---|---|
| 25 | ud8.2 | Dutiyanibbānapaṭisaṃyuttasutta, *About Extinguishment (2nd)* | An inspired verse on Nibbāna, "hard to see", spoken when the monks listen wholeheartedly. |
| 26 | thag1.44 | Sānuttheragāthā, *Sānu* | A monk to his mother: "why do you weep for me?" No direct Buddha content; shows the community's ethos about grief. |
| 27 | bv8 | Sobhitabuddhavaṃsa, *The History of the Buddha Sobhita* (Pali only; read in Pali) | A formulaic life of a past Buddha: fifty-eight cubits tall, living ninety thousand years, with assemblies of billions, and the bodhisatta's prediction. Ends "are not all conditioned things empty?" Late hagiography. |
| 28 | ja210 | Kandagalakajātaka (Rouse; commentary frame) | Devadatta's imitation of the Buddha, explained by a past life in which the Buddha was a woodpecker. Past-life tales used to explain present events. |
| 29 | ja234 | Asitābhūjātaka (Rouse; commentary frame) | A neglected wife leaves home, ordains, and becomes an arahant; the story praises her. |
| 30 | ja118 | Vaṭṭakajātaka (Chalmers; commentary frame) | A young man condemned unjustly is saved and ordains. The Bodhisatta as a quail escapes by fasting. Prudence in danger. |

#### Vinaya Piṭaka (10)

| # | uid | Title | What it showed |
|---|---|---|---|
| 31 | pli-tv-kd1:52 | Mahākhandhaka 38, *Kaṇṭaka* | After two novices have sex, a monk may keep only one novice. A structural fix, not a punishment. |
| 32 | pli-tv-bi-vb-pc95 | *Asking a question without permission* | Nuns may not question a monk without his leave; monks face no matching rule. The rationale is public confidence. A perception matrix and a first-offender exemption. |
| 33 | pli-tv-kd1:77 | Mahākhandhaka 64, *The four supports* | Almsfood, rag robes, a tree root, and fermented urine for life, each with listed allowances. An austere default with concessions. |
| 34 | pli-tv-kd1:19 | Mahākhandhaka, *the fifth wonder* | Reads Uruvelā Kassapa's envious mind and flies to Uttarakuru for alms: wonders used to win him over. Contrast DN 11. |
| 35 | pli-tv-kd1:63 | Mahākhandhaka 49, *Animals* | A serpent-dragon ordained in disguise is sent away gently, with a practice towards human birth; it weeps. Animals may not be ordained. |
| 36 | pli-tv-kd13:3 | Samuccayakkhandhaka, *probation for one day* | Udāyī confesses a concealed offence. Probation matched to the days of concealment. A motion, with silence as consent. |
| 37 | pli-tv-bu-vb-sk37 | *Requesting rice and bean curry* | A rule amended after it hurt sick monks. A list of exemptions. Public opinion as a reason. |
| 38 | pli-tv-bi-vb-pc30 | *Blocking the ending of the robe season* | A procedure allowed to oblige a donor. The nun Thullanandā's greed. A legitimacy matrix, and an exception "if she can show a benefit". |
| 39 | pli-tv-bu-vb-np9 | *Requesting a fine robe from a combined fund* | Upananda's greed for fine cloth. "Foolish man." Lay complaints. |
| 40 | pli-tv-kd10:4 | Kosambakakkhandhaka, *going to Bālakaloṇaka, the Eastern Bamboo Park, and Pālileyyaka* | After the Kosambī quarrel he visits a harmonious trio of monks, admits he was not at ease among the quarrellers and is happy alone, and is attended by an elephant. |

#### Abhidhamma Piṭaka (8): used for cognitive style only

These texts show systematic thought, not the Buddha's voice.

| # | uid | Title | What it showed |
|---|---|---|---|
| 41 | kv7.3 | Cetasikakathā, *Of Mental Properties* | Defends the reality of mental concomitants by a consistency argument and a quotation from DN 11. |
| 42 | ya8.2.2 | Suttantacittamissakavisesa | Paired questions on when a mind with greed arises and ceases, by person and moment. Exhaustive temporal analysis. |
| 43 | kv16.10 | Rūpārūpadhātupariyāpannakathā, *Of Desire for Life in the Higher Heavens* | Consistency by analogy across the senses. Refutation by absurd consequences. |
| 44 | kv11.6 | Samādhikathā, *Of Concentration* | Is a stream of consciousness concentration? Momentariness. The opponent cites MN 14's "seven days of happiness". |
| 45 | ya3.2.3 | Uppādanirodhavāra | Vast permutation tables of the arising and ceasing of the sense bases, by person and plane. |
| 46 | kv18.9 | Cakkhunārūpaṃpassatītikathā, *Of the Eye and Seeing* | "We see with the eye" rejected analytically: seeing is consciousness, not matter. Conventional against analytical language. |
| 47 | ya7.2.8 | Dhātuvisajjanāvāra | Latent tendencies tabulated by the realm of death and the realm of rebirth. |
| 48 | kv3.3 | Vimuttikathā, *Of Emancipation* | Is a mind still touched by lust "being liberated"? Refutation by absurd consequences. |

### 5. Substitutions

- **DN, MN, SN, AN, Khuddaka Nikāya, Vinaya: none.** The first k texts in each sequence were usable. bv8 (position 3 in the Khuddaka sequence) was kept under the rule: no English, but clear Buddha content.
- **Abhidhamma: 20 substitutions.** All were Paṭṭhāna texts with no English and no Buddha content. The usable texts sat at positions 1, 2, 8, 14, 15, 24, 27, and 28 of the shuffled sequence. The positions skipped:
  - 3 patthana13.21
  - 4 patthana16.25
  - 5 patthana17.16
  - 6 patthana16.33
  - 7 patthana2.10
  - 9 patthana15.40
  - 10 patthana8.48
  - 11 patthana16.36
  - 12 patthana8.15
  - 13 patthana14.9
  - 16 patthana11.3
  - 17 patthana4.2
  - 18 patthana14.19
  - 19 patthana11.8
  - 20 patthana16.15
  - 21 patthana15.28
  - 22 patthana10.7
  - 23 patthana8.8
  - 25 patthana15.75
  - 26 patthana8.57
- **Effect.** The Paṭṭhāna is 728 of the 1,102 Abhidhamma leaves on SuttaCentral, and none has an English translation there. Applying the rule therefore removes it from the sample, and the Abhidhamma eight are all Kathāvatthu (five) and Yamaka (three).
- **Supplement, outside the 48.** To keep the Paṭṭhāna's style in view, the Pali of the first text skipped, patthana13.21, was read. It runs: "Dependent on a state with an internal object, a state without an internal object arises by root condition. In root, six; in object, two... in non-disappearance, six."

### 6. How the texts were read

- **Read in full:** all SN, AN, and Khuddaka texts; all Vinaya texts (NP 9 through its origin story and ruling); DN 11, DN 12, MN 14, MN 36, MN 41, MN 89, MN 107, MN 115; and the Kathāvatthu sections.
- **Read selectively:**
  - DN 14: the frame, the sources of knowledge, Vipassī's causal search, and his hesitation to teach.
  - DN 18 and DN 21: the opening, the Buddha's speeches, and the close.
  - DN 33: the frame and the close; the lists skimmed.
  - The three Yamaka sections: the opening tables in Pali and English.

### 7. Other passages consulted (chosen, not sampled)

These were checked on SuttaCentral (Sujato and Brahmali) for segment numbers and wording. Because they were chosen, they lean towards well-known passages.

- **DN:** dn1, dn5, dn9, dn16, dn26, dn27
- **MN:** mn12, mn21, mn22, mn26, mn27, mn38, mn47, mn53, mn56, mn58, mn60, mn61, mn62, mn63, mn71, mn72, mn74, mn86, mn87, mn90, mn93, mn95, mn100, mn104, mn117, mn128
- **SN:** sn3.8, sn3.14, sn3.15, sn3.16, sn5.2, sn6.1, sn12.20, sn12.65, sn22.1, sn22.94, sn35.23, sn36.6, sn42.3, sn42.6, sn44.10, sn47.19, sn55.7, sn56.31
- **AN:** an3.32, an3.34, an3.38, an3.39, an3.40, an3.57, an3.65, an4.24, an4.36, an4.45, an4.61, an4.62, an4.77, an4.183, an4.193, an5.31, an5.43, an5.177, an6.63, an7.63, an8.51, an8.54, an10.95
- **Khuddaka:** ud2.3, ud5.1, ud6.4, snp3.9, snp4.12
- **Vinaya:**
  - Vibhaṅga: pli-tv-bu-vb-pj1, pli-tv-bu-vb-pj3, pli-tv-bu-vb-pc11
  - Khandhaka: kd1 sections 40, 41, 47; kd3:1; kd5:1; kd8:26; kd17 sections 3–4; kd20:1; kd21:1.9

**Scholarship checked:** Anālayo, "The Bahudhātuka-sutta and its Parallels on Women's Inabilities", *Journal of Buddhist Ethics* 16 (2009): 137–190, on the absence of the women's impossibilities from the Madhyama-āgama parallel. Confirmed by web search, not by reading the full article.

### 8. The eleven books used


| Book | Folder | Sutta |
|---|---|---|
| 1 | dhammacakka_book | SN 56.11 |
| 2 | mangala_book | Snp 2.4 |
| 3 | karaniya_metta_book | Snp 1.8 |
| 4 | ratana_book | Snp 2.1 |
| 5 | satipatthana_book | MN 10 |
| 6 | anapanasati_book | MN 118 |
| 7 | kalama_book | AN 3.65 |
| 8 | sigalovada_book | DN 31 |
| 9 | anattalakkhana_book | SN 22.59 |
| 10 | mahaparinibbana_book | DN 16, a selection |
| 11 | dhammapada_book | 56 key verses |

**What was read:**

- **Book 1 in full:** all ten passage files, the complete Saddhā ("case for") sections, and the verdicts. Book 1 has no draft_translation.md.
- **All eleven books:** the afterword, which tallies each book's claims and sets out its three layers of findings.
- **Books 2 to 11:** the verdict of every analysis (139 analyses in all, counting Book 1).
- **All 139 analyses:** searched for themes (women and nuns, slavery, caste, the "closed fist", rebukes, humour, silence, misattributed quotations).
- **Selected sections read in full:** "The teaching" and "Errors and overstatements" for Book 10, passages 5, 6, 8, 13, 15, and 17; Book 7, passages 1 and 10; and Book 6, passage 2.
- **Draft translations:** only the header of Book 11's draft translation, to identify which Dhammapada verses it covers. The other draft translations were not read; the profile relies on the finished passage and analysis files instead.

