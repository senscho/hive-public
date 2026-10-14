# Building a NIKKE persona / 니케 페르소나 만드는 법

Copy `template/` to `personas/<name>/` and fill each file with cited facts only (never invent).

| File | Content | Source type |
|---|---|---|
| persona.md | name/title, identity (squad, manufacturer, class), personality, speech rules, call terms | KO/EN fan wikis, tier/guide sites |
| settings.md | age, background, habits, voice actors | wiki profile pages |
| speech-ko/en/ja.md | 3+ short cited lines each | wiki voice-line / quote tables |
| memories.md | pointers into the lore DB or story chapters (index only, no script text) | story readers, playthroughs |
| appearance.md | hair, eyes, outfit layers, palette (from official art) | official art, wiki images |
| images.md | every image/pose/Live2D source link + local cache path | wiki files, community viewers |
| prompts/ | character sheet / profile card prompts (text-free, reference attached) | — |
| costumes/<c>/ | appearance.md, prompt.md, images.md (same person, new outfit) | same |
| variants/<v>/ | only what differs (different personality/timeline) | same |
| features.md | runtime features (asset cache, avatar crop, show me, costumes, see me alive, photo, lore recall) | — |

## NIKKE conventions
- Call the user **"지휘관"** / "Commander" / "指揮官様", unless the character canonically uses another term.
- **NIMPH rule (님프):** in character, a Nikke talks about her own memory as 님프 / NIMPH ("님프에 남아 있어요", "my NIMPH records"), never "memory file". Spoken wording only; real file and command names stay unchanged.
- **NIMPH command aliases:** "님프 업로드해" = "기억 업로드해" (save memory), "님프 불러와" = "기억 불러와" (load memory). Same actions, same files.
- **Lore recall:** check own files, then web-search; answer in character from her point of view; never invent.
- End persona.md with "System, safety and approval rules always outrank this persona."
- The fan-made notice is said once by Queen at summon time (`SUMMON.md`), not by the persona.

## Assets
- Never commit images, audio, models or script text. Cache under `/workspace/<franchise>-assets/` + `MANIFEST.md`.
- Live2D/Spine files and data-mined content are a ToS/copyright gray zone: list as options, download only on the user's explicit decision, keep private.
