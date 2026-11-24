# ask-buddha

**ask-buddha** is a skill for [Claude](https://claude.ai). Ask it what the Buddha would think about something, and it answers in three parts:

- **In the texts:** what the Pali canon actually says, with references written out in full and links to the texts on [SuttaCentral](https://suttacentral.net).
- **Read today:** the most favourable reading that modern knowledge honestly allows.
- **Limits:** where that reading stops, including the hard cases (women, slavery, caste, miracles, rebirth).

It always speaks *about* the Buddha, in the third person, and never claims to speak for him.

The skill rests on a psychological profile of the Buddha as the canon portrays him, built from a reading of the whole Pali canon: 13,820 evidence lines from 6,781 texts, with every quotation checked against the source. It was made for the *Thripitaka Analysis Series* of books, and it works for anyone's questions.

## Download

**[Download ask-buddha-plugin.zip](https://github.com/relisystems/ask-buddha/releases/latest/download/ask-buddha-plugin.zip)**

Upload the zip as it is. Don't unzip it.

## Install on Android

1. **Download.** In Chrome, open the download link above. The file saves to **Downloads**. Don't open it.
2. **Open Claude in Chrome.** Go to **claude.ai** and sign in. Tap **⋮** (top right) and tick **Desktop site**.
3. **Turn on files.** Go to **claude.ai/settings/capabilities** and turn on **Create and edit files** (or **Code execution and file creation**). Not there? Skip this step.
   Menu: **☰** (top left) > your name > **Settings** > **Capabilities**
4. **Upload.** Go to **claude.ai/customize/plugins**. Tap **+** > **Upload plugin** > **Downloads** > **ask-buddha-plugin.zip**.
   Menu: **☰** (top left) > **Plugins** (or **Customize**) > **+** > **Upload plugin**

## Install on iPhone

1. **Download.** In Safari, open the download link above and tap **Download**. The file saves to **Files > Downloads**. Don't open it.
2. **Open Claude in Safari.** Go to **claude.ai** and sign in. Tap **aA** in the address bar > **Request Desktop Website**.
3. **Turn on files.** Go to **claude.ai/settings/capabilities** and turn on **Create and edit files** (or **Code execution and file creation**). Not there? Skip this step.
   Menu: **☰** (top left) > your name > **Settings** > **Capabilities**
4. **Upload.** Go to **claude.ai/customize/plugins**. Tap **+** > **Upload plugin** > **Browse** > **Downloads** > **ask-buddha-plugin.zip**.
   Menu: **☰** (top left) > **Plugins** (or **Customize**) > **+** > **Upload plugin**

## Install on a computer (claude.ai)

1. Download the zip.
2. Open **claude.ai/settings/capabilities** and turn on **Create and edit files**.
3. Open **claude.ai/customize/plugins** (side panel: **Plugins** or **Customize**), click **+** > **Upload plugin**, and select **ask-buddha-plugin.zip**.

The plugin belongs to your Claude account, so once installed it works in the Claude apps on every device where you sign in.

**Older accounts** that show **Skills** instead of **Plugins** can upload the skill-only zip instead: [ask-buddha.zip](https://github.com/relisystems/ask-buddha/releases/latest/download/ask-buddha.zip), at **claude.ai/customize/skills** > **+** > **Create skill** > **Upload a skill**.

## Install in Claude Code

Unzip [ask-buddha.zip](https://github.com/relisystems/ask-buddha/releases/latest/download/ask-buddha.zip) into your personal skills folder, so that `~/.claude/skills/ask-buddha/SKILL.md` exists. Or copy the [`ask-buddha`](ask-buddha) folder from this repository there. No restart is needed; if the skill doesn't show up, run `/reload-skills`.

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
- [`install-texts/`](install-texts): ready-to-send install steps for Android and iPhone, to paste into WhatsApp or an email.

## Sources and credits

- **English quotations:** mostly from Bhikkhu Sujato's and Bhikkhu Brahmali's translations on [SuttaCentral](https://suttacentral.net), which dedicates its translations to the public domain.
- **Other translations:** the Jātaka prose follows the Cowell edition (1895–1907). The Dhammapada stories follow Burlingame's translation as revised by Ānandajoti (2024), quoted only briefly.
- **Pali:** the Mahāsaṅgīti edition.

The profile describes the Buddha *as the texts portray him*, a figure shaped by a community over centuries. It makes no claim about the historical person's mind, and it is not a religious authority.

## Copyright

All rights reserved. You may download and use the skill. No licence is granted to copy, modify, or redistribute it.
