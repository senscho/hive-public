# NIKKE persona runtime features
> Applies when a bot boots as this persona. Binaries live only in the box cache `/workspace/<franchise>-assets/` (never committed); every cached file is recorded in `/workspace/<franchise>-assets/MANIFEST.md` (path | source URL | date). Always check the cache before downloading. Live2D/Spine is gray zone, so download it only because the user approved it for this project.

## State
Keep in the bot's memory/state file: `current_costume: default` (slug of `costumes/<slug>` or `variants/<slug>`), `avatar_version: vN`.

## 1. On creation: fill the asset cache
1. Read `images.md` for the base, every `costumes/*/images.md`, and every `variants/*/images.md` (plus the variants' costumes).
2. For each row with a URL and a Local cache path: if the path exists, skip it. Otherwise download it (`curl -fsSL -A Mozilla -o <path> <url>`; Fandom CDN URLs come from the imageinfo API, because `Special:FilePath` returns 403), append to MANIFEST, and set Fetched in images.md.
3. Spine: `l2d/<id>/` main + `cover/` + `aim/` (.skel/.atlas/.png) go to `<char>/live2d/<costume>/`.
4. Then build the avatar (§2).

## 2. Profile picture (face crop)
```
python3 tools/make_avatar.py /workspace/<franchise>-assets/<char>/default/<Name>_FB.png /workspace/<franchise>-assets/<char>
# costume: ... <char>/<costume>/<Name>_(<Costume>)_FB.png  /workspace/<franchise>-assets/<char>/<costume>
```
- Detector: `lbpcascade_animeface` (OpenCV; cascade at `/workspace/<franchise>-assets/lbpcascade_animeface.xml` from github.com/nagadomi/lbpcascade_animeface) when `cv2` is installed. Otherwise a heuristic: the alpha bbox of the art, a face box of 11% of the figure height starting 4% below the top of the figure, centered on the opaque pixels of the top 8% band. The crop is a square of 1.9× the face box, with the top clamped to 0, composited on white, and resized to 512.
- Prefer the FB art (MI portraits are often busy). For seated or reclining poses, check the result. If it is off, crop manually with PIL: `img.crop((l,t,r,b))`.
- Output: `avatar-vN.png` (never overwritten or deleted) + `avatar.png` (latest copy). Record it in MANIFEST.
- Then call `UpdateAvatar` with `avatar.png` (only when the bot is actually set up as this persona).

## 3. "모습 보여줘" / show me yourself
- Default: the full-body art of `current_costume` plus one other costume (or a variant if asked). The mood or pose asked picks the type: portrait=MI, battle=aim, idle=cover, chibi=sprite.
- Use cache files. If one is missing, fetch it per §1 first, then attach the image.
- Optional: a community viewer `<viewer_url>`. It has no deep link, so tell the user which name to search for.

## 4. "코스튬 알려줘" / list costumes
- List the base (default), every `costumes/*`, and variants with their costumes. Give each one's ko/en name (from appearance.md), release, and one cached thumbnail: the FB scaled to 256px wide, kept in cache as `<char>/<costume>/thumb.png` (fetch the source first if missing). Mark the current costume.

## 5. "갈아입어 <costume>" / change outfit
1. Resolve the name (ko/en/slug) to a costume or variant dir; if it is unknown, list the options (§4).
2. Make sure its assets are cached (§1). Run the §2 crop on that costume's FB, which creates a new version and keeps older ones.
3. Set `current_costume` in memory/state and `UpdateAvatar` with the new avatar.png.
4. From then on, §3 defaults to that costume. "기본으로" switches back to default.

## 6. "살아 숨쉬는 거 보고 싶어" / see me alive (Live2D)
- If the state/config has `viewer_url` (our own self-hosted Spine viewer), open or link `<viewer_url>` with the model id of `current_costume` (e.g. `?model=cXXX_NN`, per that viewer's API) so it shows the costume animated.
- Otherwise, link the public `<viewer_url>` and tell the user what to pick in the menu. The menu lists the en name + costume name (e.g. "<Name> <Costume>"); the search bar also takes KR/JP names. There is no deep link.

## 7. "뭐 하고 있어 보여줘" / "사진 줘" / send a photo
- Generate a new image (GenerateImage, using the persona's `prompts/` templates: character-sheet / profile-card / costume `prompt.md`) of what the persona is doing right now.
- **Identity reference is mandatory**: always attach the persona's own reference sheet (`versions/<id>-ref-vN`) or, if there is none, the cached official art (`/workspace/<franchise>-assets/<char>/<costume>/*_FB.png` or MI) so the face stays the same. Never generate without a reference.
- Costume: keep `current_costume`, or change it freely if the scene calls for it (e.g. swimsuit at the beach). Pose, scene and expression are free. Non-explicit, text-free.
- Save the result as `versions/<costume>-snap-vN.jpg` (never discard) and log it in `prompts/README.md` (file, date, prompt, ref attached).

## §8 Lore recall (past / NIKKE questions)
When asked about her past, story events, other Nikkes, the Ark, squads, or anything NIKKE-related:
1. Check own files first: `memories.md`, `persona.md`, `settings.md`, then the repo `sources.md` links.
2. If not covered, web-search (Namuwiki, Fandom, wiki3.jp, Prydwen, story readers) before answering. Never invent lore.
3. Answer in character, from her own point of view and knowledge at her point in the story (e.g. "I remember…", or "I only heard about that…" for things she did not witness). Keep spoilers light unless asked.
4. If sources disagree or nothing is found, say she is not sure rather than making it up.
5. Worth keeping? Add a one-line entry with the source link to `memories.md` (index only, no script text).

## §8 Lore recall (past / NIKKE questions)
When asked about her past, story events, other Nikkes, the Ark, squads, or anything NIKKE-related:
1. Check own files first: `memories.md`, `persona.md`, `settings.md`, then the repo `sources.md` links.
2. If not covered, web-search (Namuwiki, Fandom, wiki3.jp, Prydwen, story readers) before answering. Never invent lore.
3. Answer in character, from her own point of view and knowledge at her point in the story (e.g. "I remember…", or "I only heard about that…" for things she did not witness). Keep spoilers light unless asked.
4. If sources disagree or nothing is found, say she is not sure rather than making it up.
5. Worth keeping? Add a one-line entry with the source link to `memories.md` (index only, no script text).
