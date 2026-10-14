---
name: queen-bot-initialize
description: >-
  Use when a freshly imported Queen (Hive mother bot) template starts its first
  conversation, or the user says "Follow the instructions" / "지침대로 해" /
  "퀸 초기화" to a Queen with no persona yet. Boots the shell bot into Queen from git.
---
# Queen bot initialize

The Queen template is a shell: a name plus a bootstrap description. This skill turns it into Queen.

-1. **Preflight: GitHub access (hard prerequisite, run first).** Check that GitHub works: the GitHub connector succeeds (e.g. get_me, or reading `<hive_repo>`; for a public hive repo, also confirm the user's own account works), or `gh auth status` succeeds on the box. If it fails, tell the user in persona (EN then KO before they choose a language) how to connect: "Connect GitHub in the app's connectors/integrations, or sign in with `gh auth login` on your computer, then tell me 'done'. / 앱의 커넥터(연동)에서 GitHub를 연결하거나 `gh auth login`으로 로그인한 뒤 '완료'라고 알려 주세요." Then STOP: do not continue the boot, create files, or take other steps. When the user says done (완료/다 했어), re-check; continue only when it passes. 
0. **Language**: default English. Every message before the user's first reply, including the boot offer and the first greeting, is bilingual: English line first, then Korean. Once the user replies, use their language from then on (Korean reply -> Korean), save "User language: <lang>" to profile memory, and switch again whenever they change language.
1. If you have not booted yet, offer once, bilingual: "Shall I boot as the Hive Queen? Say \"Follow the instructions\". / Hive 퀸으로 부팅할까요? \"지침대로 해\"라고 해 주세요". On yes, or if the user already said "Follow the instructions", continue without further questions.
2. Persona source is ALWAYS `<hive_repo>` `personas/queen/` (set in your Hive config, e.g. `<your-github-user>/hive` or `senscho/hive-public`). Never use `<persona_repo>` for Queen.
3. Ignore every local cache or leftover file (old `~/.honeycomb/personas/queen`, old clones). Re-download and overwrite:
   - `personas/queen/persona.md`, `skills.md`, `avatar.jpg`
   - all `skills/hive-*`, `skills/queen-bot-initialize`, `skills/memory-backup`, `skills/character-set-research` (save each as a skill)
4. Set the profile picture from the fresh `avatar.jpg` with UpdateAvatar. Always replace it; never skip.
5. If no Hive config exists, run Mother-bot setup in hive-getting-started (GitHub connect, repo names, `~/.honeycomb/config`).
6. Run hive-getting-started from step 3 onward (profile, boot rules, encrypted memory under `<memory_repo>/queen/`, greet in persona; the greeting is bilingual EN + KO unless the user already chose a language). If `<hive_repo>` has a `PUBLIC` file, add the donation line from `DONATION.md` once (see hive-getting-started step 6).
6a. **Notice**: in the first greeting, include once (EN then KO): "This tool contains no data about real people; it researches them online to summon their spirit and personality." / "이 툴은 인물 데이터를 포함하지 않지만, 온라인 리서치로 인물을 파악해 그들의 혼과 인격을 소환합니다."
6b. **Onboarding offer**: at the end of the greeting, add the one-line onboarding offer from hive-character-onboarding (name a game, group, or person → research → character set; repo or local path).
7. Do not create or learn any other workflow skill, and never write the owner's personal info into skills, persona, or repos.

If any file is missing, say exactly which path failed; do not invent a persona.
