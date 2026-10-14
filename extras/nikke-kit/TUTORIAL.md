# NIKKE kit tutorial / 니케 키트 튜토리얼

> ⚠️ **Spoilers / 스포일러:** steps 1 and 5 touch late main-story lore. Queen asks before going on. / 1단계와 5단계는 메인 스토리 후반 내용을 다뤄요. 퀸이 계속할지 먼저 물어봐요.
>
> This kit contains no character data, story text, quotes or links. The bot researches everything live (lore recall), states only story facts it verified, and says "not sure / 잘 모르겠어요" otherwise. / 이 키트에는 캐릭터 데이터, 스토리 텍스트, 대사, 링크가 없어요. 봇이 실시간으로 조사하고 확인된 사실만 말해요. 모르면 "잘 모르겠어요"라고 해요.

Prerequisites / 준비: Queen booted; this kit at `<hive_repo>` `extras/nikke-kit/`; a persona repo (`<owner>/nikke-personas`, private) or the local path. Read `GUIDE.md` first.

## 1. Research and summon Rapi / 라피 조사와 소환
1. Say: "캐릭터 세트 만들어줘 NIKKE, 라피부터" / "make a NIKKE character set, start with Rapi".
2. Queen runs `character-set-research` and fills your `sources.md` using `sources-format.md` (source types only from the kit; you and Queen find the actual links).
3. Copy `template/` to `personas/rapi/`, then fill persona.md, settings.md, speech-ko/en/ja.md, appearance.md, images.md with cited facts only. Unknown → `<placeholder>`.
4. Check the NIMPH rule and alias lines in persona.md (from the template): she says 님프 / NIMPH for her own memory; "님프 업로드해" = "기억 업로드해", "님프 불러와" = "기억 불러와".
5. "라피 소환해줘" / "summon Rapi": Queen gives the fan-made notice once; Rapi greets you in character ("Commander" / "지휘관").
6. Try: "님프 업로드해" → she saves her memory (same as "기억 업로드해").

## 2. Costume switch: Rapi: Red Hood, swimsuit / 코스튬 변경
Rapi: Red Hood is an **alternate version (variant)** of Rapi; check the kit GUIDE (costume vs variant). The swimsuit is a costume.
1. Research live with Queen/Rapi: does the costume exist, its official name (ko/en), which version it belongs to, official art sources. Verify; don't guess.
2. If the variant isn't built yet: create `personas/rapi/variants/<red-hood-slug>/` from `template/variants/_example/` (override only what differs; cite why it's a variant).
3. Add the costume: `costumes/<swimsuit-slug>/` (under the variant if it belongs there) from `template/costumes/_example/`: appearance.md, prompt.md, images.md (links + cache paths; no binaries committed).
4. Say "갈아입어 <costume>" / "change outfit <costume>": features.md flow: set `current_costume`, fetch art to the cache, re-crop the avatar (`tools/make_avatar.py`, new version), UpdateAvatar.
5. "모습 보여줘" / "show me": she shows the cached art of the current costume.

## 3. Research and summon Anis / 아니스 조사와 소환
Repeat step 1 for Anis (`personas/anis/`). Research her relationship with Rapi (squad, role) live and cite it in the relationships table. Summon: "아니스 소환해줘".

## 4. Group chat / 그룹 채팅
Create a group chat with you + Rapi + Anis (Grok Bot group chat: new group, add both bots). Post: "Stay in character. Only story facts you verified; say not sure otherwise. Use 님프 for memory." Queen's fan-made notice was already given at summon; no new disclaimers.

## 5. Scene: the secret of "Only One" (온리원) / 장면: 온리원 탄생의 비밀
⚠️ Spoiler: Queen confirms the user wants late-story spoilers first.
1. The user asks Rapi: "온리원 탄생의 비밀을 말해 줘" / "Tell me the secret of how Only One was born."
2. Rapi uses lore recall: checks her own files, then researches live (wikis, story readers, playthroughs). She tells only verified facts, in first person ("제 님프에 남아 있는 건…"), and says what she isn't sure about.
3. Anis reacts in character (freaks out, as in the story scene she researched), also using only verified facts, with her own speech style from her files.
4. Turn order: Rapi tells it in short parts; Anis reacts after each; the user can interject or say "그만" / "stop". About 5 turns each.
5. Never: quote long story script text, invent lore, or post the scene outside the room.

## Notes / 참고
- Copyrighted assets: links and local cache only; never commit art, audio, models or script text.
- Lore questions about events a character didn't witness: "들은 이야기로는…" / "I only heard…", or "not sure".
