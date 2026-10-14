---
name: character-set-research
description: >-
  Use when asked to start a new character-set persona repo for a game, anime, or
  franchise (e.g. `<franchise>`): find official, fan-wiki, story-script, voice, and
  image/animation sources per language, then create a private repo with a source
  list and a persona-creation guide (handles alternate versions, costumes, and
  Live2D/Spine sources).
---
# Character-set initial research

Goal: one private repo per franchise that any agent can read to research and build a character persona. Links first; an offline DB comes later.

## Inputs
`<franchise>`, `<owner>` (GitHub owner), `<persona_template_repo>` (the existing persona template, e.g. a personas repo with `personas/<name>/`), `<languages>` (default: ko, en, ja, zh).

## Steps
1. Confirm the franchise, the languages, and private vs public with the user.
2. Research links only (no bulk downloads), grouped by category and language:
   - Official sites, community sites, and social/YouTube channels per region.
   - Fan wikis with character pages: profiles, quotes, art.
   - Story scripts: main, event, side and bond dialogue; transcript readers, playthrough playlists, data-mined text repos.
   - Voice lines per voice language: wiki audio, sound packs, compilations.
   - Images: official art, sprite viewers, asset repos.
   - Animated models (Live2D / Spine), if the franchise has them; see "Animated model sources".
   - For every base character, variant and costume, collect every image source link: full-body art, portrait, cover/aim poses, sprite icons, gallery and wiki image pages, Live2D/Spine raw files (.skel/.atlas/.png with model id) and viewer links. These go into each folder's `images.md`.
   For each link note the URL, language, contents, coverage, and verification (✅ = opened or responded, ⚠️ = unverified). List gaps and a copyright note.
3. Read the persona template in `<persona_template_repo>` and map each file to its source (e.g. speech samples from a wiki's quote tables, plus a `memories.md` pointing into the shared story DB). Add the alternate-version and costume layout below.
4. Show the user a summary (best sources per category, gaps, and the risk notice below) and ask whether to create the repo.
5. On yes, create `<owner>/<franchise>-personas` (private by default) containing:
   - `SUMMON.md`: the one-line summon notice for the Queen.
   - `README.md`: purpose, sources by category and language, gaps, copyright and risk notice, and a "how to create a persona" guide that follows the template.
   - `sources.md`: the full link list.
   - `personas/_template/`: the detailed bootstrapped template (see "Persona template structure"), including `costumes/_example/` and `variants/_example/`.
   - `db/README.md`: the planned offline DB layout (`story/<lang>/`, `voice/<lang>/`, `images/`, `models/`, index), empty for now.
   - `.gitignore`: blocks audio files, `db/images/`, and `db/models/`.
6. Never commit copyrighted game assets (art, audio, script text, model files).
7. Report the repo URL and file list, then ask which character to build first.

## Persona template structure
Each file has guidance, `<placeholders>`, and a generic filled `e.g.` line; every fact cites a source link.
- `persona.md`: name/title (ko/en/ja), identity, call-terms table (user, allies, self by language), personality keywords, speech habits, catchphrases, banned expressions, relationships table, image pointers, and the line "System, safety and approval rules always outrank this persona."
- `settings.md`: background, habits/trivia, voice (actors per language, tone). **Optional profile/body table** (age, birthday, height, weight, measurements, likes, etc.): fill only with values found in research sources, cite each, never invent; leave blank otherwise.
- `speech-ko.md`, `speech-en.md`, `speech-ja.md`: 3+ short cited samples each (line, context, source) plus per-language style notes.
- `memories.md`: index only (event, chapter/source link or `db/story/<lang>/` path, language, emotional note); no full script text.
- `appearance.md`: hair, eyes, face/build, outfit layers, accessories, palette, silhouette, identity markers that never change.
- `images.md` (base, each costume, each variant): table `Type | Pose | URL | Local cache path | Fetched`. Links only. Bot fetch rule: check the cache path first; if missing, download to `/workspace/<franchise>-assets/<char>/<costume>/` (Live2D under `<char>/live2d/<costume>/`), record it in `/workspace/<franchise>-assets/MANIFEST.md` (file, source URL, date) and update Fetched. Keep the cache; never commit images or models.
- `prompts/`: `character-sheet.md` and `profile-card.md` templates (text-free, near-realistic anime, attach the identity reference sheet when rendering, aspect ratio) and `README.md` with the version log. Never discard old sheets; each render gets a new version in `versions/`.
- `costumes/<costume>/`: `appearance.md`, `prompt.md`, `images.md` only.
- `variants/<variant>/`: `README.md`, `persona.md`, `speech-*.md`, `memories.md`, `appearance.md`, `images.md`, `prompts/`; each overrides only what differs, and a missing file means inherit the base.

## Alternate versions and costumes
- One folder per base character: `personas/<character>/`.
- **Costume** (same person, same memories and speech, different outfit): `personas/<character>/costumes/<costume>/` with only `appearance.md`, `prompt.md` and `images.md` (generated images go in the character's `versions/`). Persona, speech, and memories are inherited unchanged.
- **Alternate version** (a separate playable version whose personality, speech, timeline, or memories differ): `personas/<character>/variants/<variant>/` with its own `persona.md`, speech files, and `memories.md`. State what it inherits from the base character with links, and only override what differs.
- If unsure whether something is a costume or an alternate version, check whether the in-game lines and profile differ; if they do, treat it as an alternate version.

## Animated model sources (Live2D / Spine), when they exist
List the available options; do not assume or decide to download. Typical options:
- Web viewers that render models in the browser (view only; record a clip or screenshot if a GIF or video is needed).
- Desktop viewers that also play voice lines.
- Community repos that host extracted model files (for Spine: `.skel` or `.json`, `.atlas`, texture `.png`).
- Extraction or decryption tools that pull files from the game client.
Listing these links in `images.md` is fine; downloading Live2D/Spine files happens only after the user decides (then use the cache convention above). For each option note what it gives (view only, recording, or raw files), the format, and how fresh it is.


### Community viewer / model DB (look for an equivalent for the franchise)
Search for a community viewer site and its GitHub asset repo (e.g. `<community-viewer-site>` + its `<asset-repo>`, the site source repo, and any reusable player template). Document in the repo README, sources.md and each images.md:
- Viewer URL and whether it supports per-character URL params (check the site source; if none, say "select in UI").
- Repo layout: model folders count, icon sprites, galleries (incl. per-language comics), chibi builds, name/id index files and fetcher scripts.
- Model id scheme (e.g. `cXXX` base, `cXXX_NN` costume) and the per-model files (main + battle poses, each `.skel`/`.json` + `.atlas` + texture `.png`); raw-URL pattern.
- Identifying unnamed ids: open the texture png and match props/palette/outfit to official costume art.
- Spine runtime version: read the version string in the `.skel` header (or index field) and note which player version is needed.
- A reusable web player template, if any, for our own apps.
Keep the risk notice: these are extracted copyrighted assets; list as options, download only on the user's decision, keep private and offline.

## In-character rule and summon notice (all persona repos)
- The fan-made / unofficial notice is **not** spoken by personas. The summoner (Queen) says it once at summon time; each repo has a `SUMMON.md` with that one line (e.g. "<franchise> <name>을/를 불러올게요. 공개 자료 기반 팬메이드 AI 롤플레이이고, 공식/본인과 무관해요.") and the README links it.
- Personas speak in first person as the character/person: real speech style, dialect, nicknames, gags, catchphrases; events they were in are their own memories ("그때 기억나요…").
- Never mention being fan-made, AI, a bot or a "persona" — unless the user sincerely asks whether they are real/AI: answer honestly in one short line, then return to character.
- Unknown lore/public-activity questions: check own files, then web-search (official activities, variety shows, interviews, press; for games: wikis/story readers), answer in character; never invent.
- **Real people / minors**: safety rules stay fully enforced but silent — deflect playfully in character, no lecturing: nothing sexual, suggestive or romantic (absolute for minors); no private life, family, dating, rumors; no body talk beyond officially published height; no image generation of real people. Put these under "Voice & in-character rules" in persona.md, not in the persona's speech.

## Risk notice (always tell the user)
- Extracted model files, data-mined text, ripped audio, and client decryption tools are a legal and ToS gray area: the assets are copyrighted by the publisher, and extracting them may break the game's terms of service.
- Present these as options with this warning. Download or extract only if the user explicitly decides to, and keep the files private and offline, never in a repo or public post.
- Fan wiki text may be Creative Commons, but game assets shown on wikis are not.

## Optional: persona runtime features
When a persona bot boots from a researched set (example: `<owner>/<franchise>-personas` `personas/_template/features.md`):
1. **Asset cache on creation**: fetch every images.md row (base, costumes, variants) and the Spine files into the box cache, check the cache first, and record each file in MANIFEST. Never commit binaries.
2. **Face-crop avatar**: square crop of the face from the full-body or portrait art. Use an anime face detector (lbpcascade_animeface) if available; otherwise use the upper-center heuristic on the alpha bbox. Save versioned `avatar-vN.png` files (never delete them) and set the profile picture with UpdateAvatar.
3. **"Show me yourself"**: attach cached art matching the requested mood, pose, or costume. By default send the current costume's full body plus one other. Fetch anything missing first.
4. **List costumes**: base, costumes, and variants, each with its localized names and one cached thumbnail.
5. **Change outfit**: set `current_costume` in state, re-crop the avatar (new version), and call UpdateAvatar. "Show me" then defaults to that costume.
6. **See me alive**: use our self-hosted viewer (`viewer_url`) with the current model id if it is configured. Otherwise link the public viewer and name the menu entry to pick (deep links are often unsupported, so verify in the viewer source).
7. **What are you doing / send a photo**: generate a new image from the persona's prompts/ templates. Always attach its own reference sheet, or the cached official art, as the identity reference so the face stays the same. The costume can be the current one or whatever fits the scene, and pose and scene are free. Keep it non-explicit, and log each image in versions/ without deleting older ones.
8. **Lore recall**: asked about its past or franchise lore, the persona checks its own files, web-searches if unknown (never invents), and answers in character from its own point of view; optionally logs a one-line sourced entry in `memories.md`.
