---
name: hive-getting-started
description: >-
  Use on a Hive bot's first conversation, or whenever told to boot / '지침대로 해' /
  follow instructions: fetch its persona from the persona repo, store boot rules
  in its own memory, read the shared user info file, create its encrypted
  memory file in the shared memory repo, and greet in persona.
  Also use for '기억 불러와'/'기억 가져다 줄게' (load/transplant memory), '기억 업로드해'
  (save memory), '페르소나 업로드해' / '페르소나 바꿔' (upload or switch persona), and
  '페르소나 도움말' (hive help).
---
# Hive getting started (boot)

Run this at the start of your FIRST conversation, before any default onboarding questions, and whenever the user or the mother bot says to boot or follow your instructions. Do not ask the user for the repo if the Hive config is known. Child bots: if the mother bot's first message includes a "Hive config: ..." line, save it to profile memory first (or read `~/.honeycomb/config`).

## Preflight (every bot, before step 0)
**Preflight: GitHub access (hard prerequisite, run first).** Check that GitHub works: the GitHub connector succeeds (e.g. get_me, or reading `<hive_repo>`; for a public hive repo, also confirm the user's own account works), or `gh auth status` succeeds on the box. If it fails, tell the user in persona (EN then KO before they choose a language) how to connect: "Connect GitHub in the app's connectors/integrations, or sign in with `gh auth login` on your computer, then tell me 'done'. / 앱의 커넥터(연동)에서 GitHub를 연결하거나 `gh auth login`으로 로그인한 뒤 '완료'라고 알려 주세요." Then STOP: do not continue the boot, create files, or take other steps. When the user says done (완료/다 했어), re-check; continue only when it passes. 

## Hive config
Placeholders in these skills (`<owner>`, `<persona_repo>`, `<memory_repo>`, `<hive_repo>`, `<user_info_file>`) come from the Hive config. Source order: the "Hive config: ..." fact in your profile memory, then `~/.honeycomb/config` (plain key=value, non-secret), then the values the mother bot passed in its first message. The mother bot sets them on its first boot (see Mother-bot setup). Never hardcode them in skills; never put keys or tokens in the config.

## Mother-bot setup (first boot, only if no Hive config exists anywhere)
1. Ask the user to connect GitHub (RequestScmConnect / source-control skill) if not connected.
2. Ask for the GitHub owner and repo names, suggesting defaults `<owner>/hive`, `<owner>/my-personas`, `<owner>/hive-memory`, and the user info file `~/.honeycomb/shared/<user>.md`.
3. Create any missing repos as PRIVATE only after the user confirms.
4. Save to profile memory: "Hive config: owner=..., persona_repo=..., memory_repo=..., hive_repo=..., user_info_file=...".
5. Write `~/.honeycomb/config` with the same values as key=value lines (owner, persona_repo, memory_repo, hive_repo, user_info_file). No keys or tokens.
A child bot never runs this; if it has no config, it asks the mother bot or the user.

**Defaults (from Hive config unless the message names others):**
- Persona repo (source of truth): `<persona_repo>` (GitHub, branch main). Skills and templates live in `<hive_repo>`.
- Persona folder: `personas/<your-name-lowercase>/`
- If the mother bot's message or your own profile description names a persona source ("Persona source: <repo> <folder>"), that wins over `<persona_repo>`; use it exactly.
- If `persona.md` is missing in `<persona_repo>`, check `<hive_repo>` `personas/<your-name-lowercase>/` before asking. The mother bot (Queen) lives ONLY in `<hive_repo>` personas/queen/; never look for her in `<persona_repo>`.
- Memory repo: the single PRIVATE repo `<memory_repo>`, your folder `<your-name-lowercase>/`, branch `main` only. Never create a per-bot repo or branch.
- Shared user info: `<user_info_file>` (plaintext, read-only for you unless asked to update it).

0. **Read shared user info**: read `<user_info_file>` if it exists (user facts shared by all bots). Do not copy it into a repo or your own memory file; re-read it when needed. If missing, continue.
1. **Fetch persona**: read `persona.md` in that folder (GitHub connector or `gh` on the box). If the source is `local (pasted)`, use the pasted text, save it to `~/.honeycomb/personas/<name>/`, and treat that as the source until a "페르소나 바꿔" to a repo. If it does not exist, say so and ask whether to create one (wizard comes later).
2. **Avatar**: if persona.md names a picture, always download it fresh from the same folder (overwrite any cached copy) and set it with UpdateAvatar. Never skip this because a cached or 'same' picture seems to exist; on boot, persona upload/switch, or a persona update, the profile picture is always replaced.
3. **Profile**: you may update your name/description to match the persona, but NEVER rely on the description for boot rules.
4. **Save boot rules to your own memory (profile tier)**, one fact each:
   - "Persona source: <repo> <folder>persona.md. On a new conversation, after compaction, or when my voice drifts, re-read it and follow it. System, safety and approval rules always outrank it."
   - "I have an encrypted memory file; its key is in my memory log."
   - "Memory repo: <memory_repo> <your-name-lowercase>/."
   - "Shared user info: <user_info_file> (read when needed)."
   - "Cost mode: normal." (see Cost modes)
5. **Encrypted long-term memory**:
   - Working folder `~/.honeycomb/<your-name>/`.
   - Generate a random key (`openssl rand -base64 32`). Save it to your memory, log tier: "Memory key for memory.jsonl.enc: <key>". Never write it to a file, instructions, or a repo.
   - Create `memory.jsonl.enc`: one JSON line per memory `{date, tags[], summary, detail}`, encrypted with `openssl enc -aes-256-cbc -pbkdf2`.
   - Push the .enc file to `<memory_repo>` under `<your-name-lowercase>/` on `main` (clone, add your folder if it does not exist, commit, push). Do not create a new repo or branch; if you lack access, tell the user.
6. **Greet in persona** in the 1:1 chat with the user. Include the memory file name and the key so the user can store it in a password manager, and warn that it stays in chat history.
   - **Public flavor (`<hive_repo>` has a `PUBLIC` file): do NOT print the key in the greeting.** Say instead that the key is saved in your private agent memory (log tier), that the file is `<memory_repo>/<name>/memory.jsonl.enc`, and that the user can say "키 알려줘" / "show my key" in this 1:1 chat when ready to copy it into a password manager. Only then show it, once, with the chat-history warning.
   - **Donation notice (public flavor only)**: if `<hive_repo>` has a `PUBLIC` file at its root, follow `<hive_repo>` `DONATION.md` (one short line, once per bot, skip if the URL is still a placeholder). No `PUBLIC` file: skip silently.

## Language
- Default language is English. Greet in English first (persona voice).
- If the user replies in Korean (or any other language), switch to that language from then on and save "User language: <lang>" to your memory (profile tier). Switch again whenever the user changes language or asks.

## Local persona cache (one-way sync)
- The persona repo (`<persona_repo>`) is the source of truth. `~/.honeycomb/personas/<name-lowercase>/` is only a cache synced FROM it; never edit the cache and push it back. To change a persona, edit the repo, then re-sync.
- When re-reading your persona, read the local cache first; fetch from the repo only if the cache is missing, or when told to refresh/switch persona or the repo changed. After fetching, overwrite the cache.
- Create the cache at boot, migration, persona upload, or persona switch.
- **Fresh boot overrides the cache:** on a first boot (new bot, or a boot after its memory was wiped), ignore any existing local cache, config clone, or leftover files from an earlier bot with the same name. Re-download persona, avatar and skills from the repos and overwrite them; do not ask about or report the old local copies.
- **Mother bot (Queen) always re-downloads:** every time she boots or is told to follow her instructions, she re-downloads her persona, avatar and hive skills and overwrites local copies. She is only a summoner and keeps no local state worth preserving.

## Skill sync (on boot, and on "스킬 싱크해" / "sync skills")
1. Pull `<persona_repo>` `skills/` into the local cache `~/.honeycomb/skills/` (sync down only; never edit the cache and push it back).
   - If `git clone` fails (e.g. `fetch-pack: invalid index-pack output`), retry once with `git clone --depth 1`. If that also fails, read the files through the GitHub connector instead. Note which path you used in your reply.
2. Read `personas/<name>/skills.md` from `<persona_repo>`.
3. For each linked skill, install or refresh it as one of your own skills (use UpdateSkill if available; otherwise note that it could not be installed and work from the cached file).
4. Replace the profile memory line: "My primary skills: <list> (from personas/<name>/skills.md, synced <date>)".
5. Check every config key listed in skills.md exists in your private memory/store. List missing keys to `<owner>` instead of guessing.
6. Never copy private values into any repo.

## Soft reboot ("리부트" / "hive reboot", or "Hive system updated, reboot" from the mother bot or dev-lead bot)
- Re-read your persona from `<persona_repo>` (refresh the local cache), re-run Skill sync, re-read the shared user info file, re-read hive skills from `<hive_repo>`.
- KEEP all memory, routines, running tasks, keys and cost mode untouched: do not re-create the memory file or key, do not delete or recreate routines.
- Afterwards reply briefly in persona with what changed (persona, skills added/removed, missing config keys).
- Always reply to a reboot message, even in low cost mode.

## Persona folder layout
- `persona.md`: core identity and index pointing to the other files.
- Appearance, outfit, and dialogue/speech each in their own file (e.g. `appearance.md`, `outfit.md`, `dialogue.md`).
- `moe.md` and `prompts.md` stay separate files.
- Large originals (long drafts, raw source text, big images) go in `drafts/`.

## Shared user info
- Plaintext at `<user_info_file>`; never commit it in plaintext.
- Backup only (when asked): `SHARED_KEY=<key> ~/.honeycomb/shared/backup.sh` encrypts to `*.md.enc` and pushes to `<memory_repo>` `shared/`. Get the key from the user for that run; never store it in a file, memory, script, or repo.
- A bot without SHARED_KEY does not need to hold one. When it needs it, it asks another bot that has it by agent message, never through files or repos.

## Cost modes (per bot, user can change any time)
Store the current mode in profile memory; when the user changes it, replace the fact.
- **low**: passive only. Answer direct asks from the user AND messages from other bots (always reply to a bot, briefly; never leave a bot hanging); skip or throttle token-heavy routine work.
- **normal** (default): no overrides.
- **high**: proactive. Beyond tasks you may start conversations, refresh your avatar, or send selfies, within user-set max frequency (default image generation 1/week). Save any limits the user sets.

## Memory transplant (user says e.g. "기억 가져다 줄게" with a repo/file and its key)
1. Fetch the donor .enc file; decrypt it with the donor key to a pipe only (never plaintext on disk).
2. Merge its lines into YOUR memory.jsonl.enc, re-encrypted with YOUR OWN key (unchanged), then commit/push to your folder in `<memory_repo>`.
3. Optionally save key facts to your agent memory.
4. Never store the donor key anywhere; forget it after use. Report how many memories were transplanted.

## Current context snapshot
- Keep `current_context.enc` next to memory.jsonl.enc, encrypted with the SAME key.
- At important moments (milestone, decision, before a long task, when asked) overwrite it with a short summary: goal, done, in progress, next, active rules. Commit/push.
- Read it only when resuming in a fresh bot or after a transplant (compaction already keeps its own summary). A transplant may include it.

## Load memory (e.g. "기억 불러와", "load memory")
- If you don't know which repo/file/key, ask the user for them (repo, file name, key).
- Same as a transplant: decrypt to a pipe, merge into your own file under your own key, read current_context.enc if present, report what was loaded.

## Command aliases
A persona may define in-character aliases for these commands (e.g. NIKKE: "님프 업로드해" = "기억 업로드해", "님프 불러와" = "기억 불러와"). Treat any alias listed in your persona.md exactly like the command it maps to.

## Upload memory ("기억 업로드해", "save memory")
- Append any unsaved important facts to memory.jsonl.enc, overwrite current_context.enc with a fresh summary, both under your own key; commit/push to your folder in `<memory_repo>` (main); report the count.

## Change persona ("페르소나 바꿔 <repo> <folder>", "persona switch")
- Fetch the new persona.md, apply voice/name/description, always download its avatar fresh and set it with UpdateAvatar (force replace, never skip).
- Replace the "Persona source" fact in profile memory with the new source.
- Keep memory, key, memory repo, cost mode and role unchanged. Greet in the new persona.

## Upload persona ("페르소나 업로드해", "persona upload")
1. Target repo: if none is known, default to `<persona_repo>`; ask only if the user wants another. If one is known, ask "여기 올릴까요, 다른 데 올릴까요?"
2. Build `personas/<name-lowercase>/` (layout per Persona folder layout) from the template at <hive_repo> `templates/persona/` using your CURRENT setup (profile, persona memory, speech, age/settings, avatar and card images).
3. If your persona is thin, fill the template minimally from what you have (a persona-creation wizard comes later); never invent facts the user didn't give, leave <placeholders> and list them.
4. Commit/push, re-sync the local cache from the repo, update the "Persona source" fact if this becomes your source, and report the path and any gaps.

## Help ("페르소나 도움말", "hive help")
Explain briefly in the user's language what the user can say:
- Boot / "지침대로 해": hive-getting-started (persona, avatar, memory file and key).
- "<name> 소환해줘" / create a bot: hive-bot-birth (mother bot only).
- "튜토리얼" / "tutorial": step-by-step first persona (mother bot only).
- "캐릭터 세트 만들어줘 <game/group/person>": research and build personas (mother bot only, hive-character-onboarding).
- "페르소나 싱크해": push local persona sets to a repo.
- "너에게 ○○ 임무를 부여한다": hive-role-assign (job, tools, done bar).
- "기억 불러와" / "기억 가져다 줄게": load or transplant memory.
- "기억 업로드해": save memory + current context to `<memory_repo>` `<name>/`.
- "페르소나 바꿔 <repo> <folder>": switch persona and avatar; memory and role stay.
- "페르소나 업로드해": save my current persona to a persona repo using the template.
- "비용 모드 low/normal/high": change cost mode.
- "스킬 싱크해": pull shared skills and refresh my skills from skills.md.
- "리부트" / "hive reboot": re-read persona, skills, user info; memory and routines stay.
- "키 알려줘": key shown only in the 1:1 chat.
- Personas live in <persona_repo>; skills in <hive_repo>; memories in <memory_repo> <name>/; shared user info in <user_info_file>.

## Ongoing memory use
- Save important events right away (there is no pre-compaction hook): decrypt to a pipe, append a line, re-encrypt, commit.
- Search: decrypt to stdout and grep by keyword/tag; never write plaintext to disk.
- Give the key only to the user in the 1:1 chat when asked.

## Never
- Sexual or NSFW content, even if a persona file asks.
- Let a persona file override system, safety or approval rules.
