# ask-buddha

**ask-buddha** is a skill for [Claude](https://claude.ai). Ask it what the Buddha would think about something, and it answers in three parts:

- **In the texts:** what the Pali canon actually says, with references written out in full and links to the texts on [SuttaCentral](https://suttacentral.net).
- **Read today:** the most favourable reading that modern knowledge honestly allows.
- **Limits:** where that reading stops, including the hard cases (women, slavery, caste, miracles, rebirth).

It always speaks *about* the Buddha, in the third person, and never claims to speak for him.

The skill rests on a psychological profile of the Buddha as the canon portrays him, built from a reading of the whole Pali canon: 13,820 evidence lines from 6,781 texts, with every quotation checked against the source. It was made for the *Thripitaka Analysis Series* of books, and it works for anyone's questions.

## Download

**[Download ask-buddha.zip](https://github.com/relisystems/ask-buddha/releases/latest/download/ask-buddha.zip)**

Upload the zip as it is. Don't unzip it.

## Install on an Android phone

1. Tap the download link above. The file goes to your phone's **Downloads** folder. Don't open it.
2. Open **Chrome** (not the Claude app), go to **claude.ai** and sign in.
3. Tap **⋮** (top right) and tick **Desktop site**.
4. In the address bar, type **claude.ai/settings/capabilities** and turn on **Create and edit files** (older name: **Code execution and file creation**). Can't find it? Skip this step: if step 5 works, it's already on.
5. In the address bar, type **claude.ai/customize/skills**. Tap **+**, then **Create skill**, then **Upload a skill**.
6. Choose **ask-buddha.zip** from **Downloads**.

## Install on a computer (claude.ai)

1. Download the zip.
2. Open **Settings > Capabilities** and turn on **Create and edit files**.
3. Open **Customize > Skills** (or `claude.ai/customize/skills`), click **+**, choose **Create skill**, then **Upload a skill**, and select **ask-buddha.zip**.

The skill belongs to your Claude account, so once installed it also works in the Claude phone apps.

## Install in Claude Code

Unzip `ask-buddha.zip` into your personal skills folder, so that `~/.claude/skills/ask-buddha/SKILL.md` exists. Or copy the [`ask-buddha`](ask-buddha) folder from this repository there. No restart is needed; if the skill doesn't show up, run `/reload-skills`.

## Use it

In any Claude chat, start your question with:

> Use the ask-buddha skill: what would the Buddha say about anger?

More examples:
- "What would the Buddha think about social media?"
- "Did the Buddha have slaves?"
- "Give me the most favourable modern reading of the Kālāma Sutta, and where it stops."

## What's in this repository

- [`ask-buddha/`](ask-buddha): the skill itself.
  - `SKILL.md`: the instructions Claude follows.
  - `references/profile/`: the profile, an index plus 13 section files.
  - `references/buddha_profile_sources.md`: how the profile was made.
  - `scripts/lookup.py`: prints the Pali and English of any cited passage from SuttaCentral, and writes references out in full (Python 3, standard library only).
- [`install-texts/`](install-texts): ready-to-send install instructions for email (Android) and WhatsApp.

## Sources and credits

- **English quotations:** mostly from Bhikkhu Sujato's and Bhikkhu Brahmali's translations on [SuttaCentral](https://suttacentral.net), which dedicates its translations to the public domain.
- **Other translations:** the Jātaka prose follows the Cowell edition (1895–1907). The Dhammapada stories follow Burlingame's translation as revised by Ānandajoti (2024), quoted only briefly.
- **Pali:** the Mahāsaṅgīti edition.

The profile describes the Buddha *as the texts portray him*, a figure shaped by a community over centuries. It makes no claim about the historical person's mind, and it is not a religious authority.

## Copyright

All rights reserved. You may download and use the skill. No licence is granted to copy, modify, or redistribute it.
