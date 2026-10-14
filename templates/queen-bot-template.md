# Queen bot template (spec for a shareable Bot template)

What a published Queen template must contain so a fresh import boots into Queen
by itself. Nothing personal: no owner name, repos of a specific user, keys, or memory.

## Name / description
- Name: Queen
- Description (boot bootstrap, exact):
  `On your first conversation, before anything else, run the queen-bot-initialize skill. If you don't have it, fetch skills/queen-bot-initialize/SKILL.md from <hive_repo> on GitHub, save it as a skill, and follow it. Persona source: <hive_repo> personas/queen`
  (The public template uses the placeholder; the importer's Hive config fills it in.)

## Everything else: none (shell template)
The template is a shell: name + the bootstrap description above. No skills, memories,
routines or plugins are packed. On first boot it pulls everything from <hive_repo>:
hive-getting-started (and, via skill sync, the other hive-* skills), persona.md
(including the Queen scope rule), avatar.jpg, then creates config, memory file and key.
Pack queen-bot-initialize in the published template (so the bot offers to boot on its own); everything else comes from git.

## First run after import
1. Import the template, open the new bot's chat.
2. Say "Follow the instructions" (or "지침대로 해"). It runs hive-getting-started:
   Mother-bot setup (GitHub connect, repo names, config) -> fetch persona -> set avatar
   -> boot rules to memory -> encrypted memory file -> greet as Queen.
