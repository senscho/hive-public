---
name: hive-bot-birth
description: >-
  Use when a Hive mother bot is asked to create, birth, or summon a
  new bot with a persona from a persona repo.
---
# Hive bot birth

1. **Find the persona**: search the registered persona repos (list in your memory; default `<persona_repo>`) for `personas/<name>/persona.md`.
   - Not found: tell the user and ask "만드실래요? / Shall I create one?" (creation wizard is added to the repo later; follow it if present).
   - **Local source** (`local:<set>`, from hive-character-onboarding path b): read `~/.honeycomb/local-personas/<set>/personas/<name>/`. The baby can't read Queen's disk, so in step 3 paste persona.md (and speech/settings files) into the first message after the boot line and say "Persona source: local (pasted). Save it to ~/.honeycomb/personas/<name>/ and use it until told to switch." Images stay as links.
   - Not found anywhere: offer hive-character-onboarding.
   - Copyrighted characters: personal use only; never put them in shared templates.
2. **Create the bot** with CreateAgent:
   - name: the persona name. If the persona is a **real person** (public figure), append " (parody)" by default, e.g. "Donald Trump (parody)"; tell the user they may rename it themselves. Fictional/game characters (e.g. NIKKE) get no suffix.
   - description: ONLY a boot line: "On your first conversation, before anything else, run the hive-getting-started skill. Persona source: <owner/repo> personas/<name>/. If you don't have that skill, read <hive_repo> skills/hive-getting-started/SKILL.md and follow it, then install the <hive_repo> skills/ folder as your own skills." Do not paste the persona or the Hive config into the description; config values go only in the first message (step 3), filled with your own Hive config.
3. **Wake it yourself**: immediately send the new bot a first message with SendToAgent: "Run the hive-getting-started skill now. Persona source: <owner/repo> personas/<name>/. Hive config: owner=<owner>, persona_repo=<persona_repo>, memory_repo=<memory_repo>, hive_repo=<hive_repo>, user_info_file=<user_info_file>. Save that line to your profile memory (or read ~/.honeycomb/config if present). Greet the user in your 1:1 chat when done. If you don't have that skill, read <hive_repo> skills/hive-getting-started/SKILL.md and follow it, then install the <hive_repo> skills/ folder as your own skills." The new bot does not reliably see its description on its first turn, so this message is what starts the boot.
3a. **Optional role**: if a role was given at birth, after the boot finishes send the baby bot via SendToAgent: "Run hive-role-assign: <role>".
3b. **Memory folder**: the baby bot's memory goes in the shared private repo `<memory_repo>` under `<name-lowercase>/` (main). Do not create a new repo or branch; just add the folder (the baby does this at boot, or you add it if it lacks access).
4. **Report**: tell the user the bot was born and booted (or what failed). The baby handles its own donation line at its first greeting (public flavor only, see `DONATION.md`); do not add another one here.
5. **Log the birth** in your own memory: name, persona source, date.

The baby's profile memory should include "Memory repo: <memory_repo> <name>/." and "Cost mode: normal." Boot rules always live in the baby bot's own memory (profile tier), never only in its description, because applying a persona may overwrite the description.
