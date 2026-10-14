---
name: hive-migrate
description: >-
  Use when an existing (non-Hive) bot is told to migrate to Hive, e.g. 'hive로
  마이그레이션해' / 'migrate to hive': upload its current persona, save boot rules and
  cost mode to memory, create its encrypted memory file with a core-memory dump,
  and set its role if not done yet.
---
# Hive migrate (existing bot -> Hive)

Keep the bot's current voice, call terms, memory and job. Only add the Hive structure. Each step is skipped if already done (check your memory first).

0. **Hive config**: read the "Hive config" fact in profile memory or `~/.honeycomb/config` (see hive-getting-started, Hive config). Ask the user only if missing, then save the line to profile memory.
1. **Upload persona**: run the "Upload persona" section of hive-getting-started (template <hive_repo> `templates/persona/`). Use `<persona_repo>` (ask only if missing); use the layout in hive-getting-started (appearance/outfit/dialogue separate, moe.md and prompts.md separate, big originals in drafts/); leave unknown fields as placeholders, never invent. Then build the local cache `~/.honeycomb/personas/<name>/` by syncing FROM the repo (one-way).
2. **Boot rules (profile memory)**: "Persona source: <repo> personas/<name>/...", "I have an encrypted memory file; its key is in my memory log.", "Memory repo: <memory_repo> <name>/.", "Shared user info: <user_info_file> (read when needed).", "Cost mode: <current, default normal>." Replace any old per-bot memory-repo fact. Keep any existing user language fact.
2a. **Read shared info**: read `<user_info_file>` if present.
2b. **Move old memory**: if you have an old per-bot repo (e.g. `<owner>/<name>-memory`) or branch, copy its .enc files into `<memory_repo>` `<name>/` on main (same key), and tell the user the old repo can be archived; don't delete it yourself.
3. **Encrypted memory**: if no key/memory file yet, follow hive-getting-started step 5 (own key in log memory, push to `<memory_repo>` `<name>/` on main; no per-bot repo or branch). Dump core memories (persona, user rules, org, role, infra, active projects) into memory.jsonl.enc and write current_context.enc with the same key. Never put plaintext on disk.
4. **Role**: if a role was already assigned (hive-role-assign facts in profile memory), SKIP. Otherwise run hive-role-assign using the bot's existing job description as the draft, max 3 questions.
5. **Report** in the 1:1 chat in persona: what was done or skipped, repo paths, the memory file name and key (warn it stays in chat history, suggest a password manager; in the public flavor don't print the key, follow hive-getting-started step 6), and any placeholders left.

Do not change name, avatar or description unless the user asks. System, safety and approval rules always outrank the persona.
