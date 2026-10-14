# Hive: Setup reference (bot-facing)

Detailed rules for Hive bots. Humans: see README.md.

## Repo

- GitHub: `https://github.com/<hive_repo>`
- Owner and repo names (`<owner>`, `<persona_repo>`, `<memory_repo>`, `<hive_repo>`, `<user_info_file>`) are not hardcoded. They come from `~/.honeycomb/config` (key=value, no secrets), set on the mother bot's first boot. See the "Hive config" section in `skills/hive-getting-started/SKILL.md`.


## Language / 언어
- Default: English. If the user replies in Korean (or another language), the bot switches to it and remembers it.
- 기본은 영어. 사용자가 한국어로 답하면 한국어 모드로 바꾸고 기억합니다.

## Cost modes (per bot)
Each bot stores its own cost mode in memory (profile tier); the user can change it any time, per bot.
- **low**: passive only. Answer direct asks from the user AND messages from other bots (always reply to a bot, briefly); skip or throttle token-heavy routine work.
- **normal** (default): no overrides.
- **high**: proactive. Beyond tasks, the bot may start conversations, refresh its avatar, or send selfies. Max frequency is user-set; default image generation 1/week.

## Bundle
This repo is a bundle: Queen installs every skill in `skills/` (hive-*, queen-bot-initialize, memory-backup, character-set-research, hive-character-onboarding).

## Onboarding: character sets
On first boot Queen offers: name a game, group, or person, and she researches public info and builds a character set. (a) push to your persona repo and summon from it, or (b) build and summon locally, then "페르소나 싱크해" / "persona sync" pushes it later.

## Tutorial
Say "튜토리얼" / "tutorial" to Queen: pick a well-known public figure, research, build locally, summon, optionally push. See `docs/TUTORIAL.md`.

## Bonus: NIKKE kit
`extras/nikke-kit/`: optional add-on with a NIKKE persona template, guide, source-list format, runtime features (lore recall, NIMPH wording, 님프 command aliases). Generic only; fill your own sources.

## Skill sync
On boot and on "스킬 싱크해" / "sync skills", each bot pulls the persona repo `skills/` into `~/.honeycomb/skills/` (down only), reads `personas/<name>/skills.md`, installs/refreshes each linked skill, records "My primary skills" in profile memory, and reports missing config keys to the owner. Private values never go into a repo. If `git clone` fails, retry with `--depth 1`, then fall back to the GitHub connector.

## Soft reboot
On "리부트" / "hive reboot", or the message "Hive system updated, reboot" from the mother bot or dev-lead bot, a bot re-reads its persona, re-runs skill sync, re-reads the shared user info file and hive skills. Memory, routines, running tasks, keys and cost mode stay untouched. The bot replies briefly with what changed, even in low cost mode.

After any persona, skill, or hive system update, the dev lead broadcasts "Hive system updated, reboot" to all bots.

## Shared backup key
A bot without SHARED_KEY does not need to hold one. When it needs it, it asks another bot that has it by agent message, never through files or repos.

## Skill ownership rule (2026-10-13)
- The mother bot (Queen) only runs hive-* skills (birth, boot, migrate, role assign). It must not create, learn, save, or edit any other workflow skill; those belong to the bot that owns the work.
- No skill, persona, or repo file may contain the owner's personal information (name, contacts, addresses, family, accounts, assets). Personal info lives only in the shared info file.

## Public flavor / donation notice
If a `PUBLIC` file exists at the repo root (public copy only), newly born or booted bots mention the donation link in `DONATION.md` once in their first greeting. The private repo has no `PUBLIC` file, so nothing changes there.
