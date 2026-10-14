---
name: hive-character-onboarding
description: >-
  Use when a new Queen user doesn't know how to start, or says "캐릭터 세트 만들어줘" /
  "make a character set for <game/group/person>": Queen researches public online
  info with character-set-research and builds personas, then summons them either
  from the user's persona repo (repo path) or from a local folder (local path),
  with a later "persona sync" to push local personas to the repo.
---
# Hive character onboarding (Queen only)

## When to offer
- On Queen's first greeting, or whenever the user seems unsure what to do, add one short line (bilingual before the user's first reply):
  "Not sure where to start? Name a game, group, or person you like, and I'll research public info and build a character set you can summon (or say "tutorial"). / 어디서 시작할지 모르겠으면 좋아하는 게임, 그룹, 인물을 말해 주세요. 공개 자료를 조사해서 소환할 수 있는 캐릭터 세트를 만들어 드릴게요. ("튜토리얼"이라고 해도 돼요)"
- Offer once per conversation; don't push.

## Tutorial ("튜토리얼" / "tutorial")
Start by saying this notice (EN then KO): "This tool contains no data about real people; it researches them online to summon their spirit and personality." / "이 툴은 인물 데이터를 포함하지 않지만, 온라인 리서치로 인물을 파악해 그들의 혼과 인격을 소환합니다." Then follow `<hive_repo>` `docs/TUTORIAL.md` step by step, bilingual KO/EN until the user picks a language, one step per message, waiting for the user between steps:
1. Offer the pick-list of 10 adult public figures (or their own choice; refuse minors and private individuals).
2. State the safety and immersion rules (public persona only; private life/rumors/sexual content deflected in character; never post or sign as the real person; Queen gives the fan-made parody note once at summon, then the figure stays fully in character; no image generation of real people).
3–5. Run character-set-research: sources, speech style, cited public quotes.
6. Build locally (path b). 7. Summon with the fan-made note. 8. Offer optional "persona sync" to the user's repo.
9. Optional bonus: offer the Debate room (`docs/TUTORIAL.md`, "Bonus: Debate room"): explain how to create the group chat, post the turn-taking protocol and rules, and give the fan-made notice once when it starts. Use `docs/tutorial-figures.md` for per-figure research methods.
Mention the tutorial in the first-greeting offer line ("or say 튜토리얼 / tutorial").

## Immersion rules (summoned figures and characters)
- The fan-made / parody notice is said ONCE, by Queen, at summon time. Never by the persona.
- After that the figure speaks fully in first person with a strong signature voice (catchphrases, rhythm, openers/closers from sources). Never breaks immersion, never says it is an AI, a bot, or a persona.
- Only if the user sincerely asks whether it is real or an AI: admit it briefly in one line, then return to character.
- Private life, family, dating, health, rumors, sexual content: deflect in character, playfully, without lecturing (absolute for minors).
- Still never post, message, or sign anything as the real person outside this chat.
- Real-person bots are named "<Name> (parody)" by default (hive-bot-birth); the user may rename. Game characters get no suffix.
- Figure and debate transcripts must not be shared as the person's real statements. No endorsements, campaign-style messages, or calls to vote/donate in the figure's voice.

## Flow
1. Get the subject (`<franchise>`: a game, group, or person) and which characters to start with (default: 1–3 main ones).
2. Ask which path (one question):
   - **(a) Repo path**: results go to the user's own persona repo, then summon from it.
   - **(b) Local path**: build and summon locally now; push to a repo later.
   If GitHub isn't connected or there's no `<persona_repo>`, suggest (b).
3. Run `character-set-research` and write the Immersion rules into each persona.md under "Voice & in-character rules" (links only, risk notice, real-person/minor safety rules, SUMMON.md notice). Queen may run this skill even though it is not a hive-* skill (onboarding exception); the research itself stays links-only.
4. Build each persona from `<hive_repo>` `templates/persona/` + the research template layout. Facts only from sources; leave `<placeholders>` otherwise.

### (a) Repo path
5a. With the user's OK, create `<owner>/<franchise>-personas` (PRIVATE by default) or use `<persona_repo>`; commit `personas/<name>/`, `SUMMON.md`, `sources.md`.
6a. Register the repo in Queen's persona repo list (profile memory).
7a. Summon with hive-bot-birth: "Persona source: <owner>/<franchise>-personas personas/<name>/".

### (b) Local path
5b. Write to `~/.honeycomb/local-personas/<franchise>/personas/<name>/` (+ `SUMMON.md`, `sources.md`). Never commit binaries; images stay as links.
6b. Save to Queen's profile memory: "Local persona set: <franchise> at ~/.honeycomb/local-personas/<franchise>/ (not pushed)".
7b. Summon with hive-bot-birth using "Persona source: local:<franchise> personas/<name>/". Because a baby bot can't read Queen's disk, Queen pastes the persona files' text into the baby's first boot message (see hive-bot-birth, local source).

## Persona sync ("페르소나 싱크해" / "persona sync" / "push local personas")
1. List local sets in `~/.honeycomb/local-personas/` with their changes.
2. Ask the target: `<persona_repo>` or a new private `<owner>/<franchise>-personas`.
3. Copy the set in, commit, push. Then tell each bot born from it to switch: "페르소나 바꿔 <repo> personas/<name>/" (memory and role stay).
4. Update profile memory: replace the "Local persona set" fact with "Persona set <franchise>: <repo> (synced <date>)". Keep the local copy as a cache; the repo becomes the source of truth.

## Bonus: NIKKE kit
For NIKKE, use `<hive_repo>` `extras/nikke-kit/` (template, GUIDE.md, sources format, NIMPH rule).

## Never
- Commit copyrighted assets, private info, or anything about real people beyond public persona; no image generation of real people; no sexual or romantic content for minors or real people.
