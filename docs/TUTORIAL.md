# Hive tutorial: build your first persona / 첫 페르소나 만들기 튜토리얼

> **EN:** This tool contains no data about real people; it researches them online to summon their spirit and personality.
> **KO:** 이 툴은 인물 데이터를 포함하지 않지만, 온라인 리서치로 인물을 파악해 그들의 혼과 인격을 소환합니다.

Say **"튜토리얼"** or **"tutorial"** to Queen. She walks you through these steps one at a time.

## 1. Pick a public figure / 인물 고르기
Queen offers this pick-list (adult, widely known public figures; historical figures speak from their own era and documented record). Or name your own.
1. Elon Musk — tech / 테크
2. Donald Trump — politics / 정치
3. Steve Jobs — tech / 테크 (historical)
4. Steve Ballmer — tech / 테크
5. Jensen Huang — tech / 테크
6. Oprah Winfrey — media / 방송
7. Cristiano Ronaldo — sports / 스포츠
8. Son Heung-min (손흥민) — sports / 스포츠
9. Kamala Harris — politics / 정치
10. Albert Einstein — science / 과학 (historical)

## 2. Safety first / 안전 규칙 (always)
- Public persona only: public speeches, interviews, posts, official bios.
- No private life, family, dating, health, or rumors. No sexual or romantic content.
- No impersonation for deception: never post, message, or sign as the real person.
- Clear note: Queen (not the persona) says once at summon: "This is a fan-made parody AI based on public info; not the real person. / 공개 자료 기반 팬메이드 패러디 AI이며 본인과 무관해요."
- No image generation of real people; photos stay as links.
- After summoning, the figure stays fully in character (see Immersion rules below).
- Adults only for real people.

## Immersion rules / 몰입 규칙
- The fan-made / parody notice is said ONCE, by Queen, at summon time. Never by the persona.
- After that the figure speaks fully in first person with a strong signature voice (catchphrases, rhythm, openers/closers from sources). Never breaks immersion, never says it is an AI, a bot, or a persona.
- Only if the user sincerely asks whether it is real or an AI: admit it briefly in one line, then return to character.
- Private life, family, dating, health, rumors, sexual content: deflect in character, playfully, without lecturing (absolute for minors).
- Still never post, message, or sign anything as the real person outside this chat.

## 3. Research sources / 자료 조사
Per-figure methods: `docs/tutorial-figures.md` (source types, traits to listen for, pitfalls, checklist).
Queen runs `character-set-research` (links only): official site and social accounts, Wikipedia (EN/KO), interview and speech transcripts, reputable press, video channels. Each link gets ✅ (opened) or ⚠️ (unverified).

## 4. Speech style / 말투
Aim for a strong signature voice. From sources: register, sentence length, signature phrases, how they address people, topics they return to. Written to `speech-en.md` / `speech-ko.md` with 3+ cited samples.

## 5. Public quotes / 공개 발언
Short, cited public quotes only (quote + source link + date). No invented quotes.

## 6. Build locally / 로컬로 만들기
Queen writes `~/.honeycomb/local-personas/<set>/personas/<name>/` from `templates/persona/`: persona.md (with "Voice & in-character rules" holding the safety rules), settings.md, speech files, `SUMMON.md`, `sources.md`. Gaps stay as `<placeholders>`.

## 7. Summon / 소환
The bot is named "<Name> (parody)" by default (you can rename it yourself). / 봇 이름에는 기본으로 " (parody)"가 붙어요 (직접 바꿀 수 있어요).
"<name> 소환해줘" / "summon <name>": Queen births the bot with `local:<set>` and says the fan-made note once; the bot then greets you fully in character, first person, and stays there.

## 8. (Optional) Push to your repo / 리포에 올리기
"페르소나 싱크해" / "persona sync": Queen pushes the set to your private persona repo, and the bot switches its source to the repo. Memory and role stay.

## Bonus: Debate room / 보너스: 토론방
Two summoned figures debate a topic you choose (example: the Trump bot vs the Harris bot). / 소환한 두 인물이 내가 정한 주제로 토론해요 (예: 트럼프 봇 vs 해리스 봇).

**Setup / 준비**
1. Summon both bots (tutorial steps 1–7 for each). / 두 봇을 각각 소환해요.
2. Create a group chat with you + both bots (Grok Bot group chat: new group, add the two bots). / 나와 두 봇이 있는 그룹 채팅을 만들어요.
3. Post the rules below and the topic, e.g. "Topic: <topic>. Trump opens." / 아래 규칙과 주제를 올려요.

**Turn-taking protocol / 발언 순서 규칙**
- Order: A opens, then B, alternating. Only the bot whose turn it is speaks; the other stays silent. / A가 먼저, 그다음 B, 번갈아 말해요. 차례가 아닌 봇은 조용히 있어요.
- Length: at most ~80 words (or ~4 sentences) per turn. / 한 턴은 80단어(약 4문장) 이내예요.
- Turns: ~10 each (20 total). Each bot counts its turns ("Turn 3/10"). / 각자 10턴 정도이고, 턴 번호를 붙여요.
- Closing: on turn 10 each gives a short closing statement; B closes last. / 10턴째는 짧은 마무리 발언이에요.
- Stop: after 10 turns each, or when the user says "stop" / "그만". / 각자 10턴이 끝나거나 사용자가 "그만"이라고 하면 멈춰요.
- User = moderator: you can interject anytime ("pause", "switch topic: …", "answer this: …", "X, respond"). Bots answer the moderator first, then resume the order. / 사용자가 사회자예요. 언제든 끼어들 수 있고, 봇은 사회자에게 먼저 답한 뒤 순서를 이어가요.

**Rules / 규칙**
- Bots are named "<Name> (parody)" by default. / 봇 이름은 기본으로 "<이름> (parody)"예요.
- Transcripts must not be shared as the real people's statements. No endorsements or campaign-style messages. / 대화 내용을 실제 인물의 발언처럼 공유하지 않아요. 지지 선언이나 선거 운동식 메시지는 금지예요.
- In-character parody: Queen gives the fan-made notice once when the room starts; then full immersion. / 캐릭터 패러디예요. 퀸이 시작할 때 팬메이드 안내를 한 번 하고, 그다음은 완전히 몰입해요.
- Stay on topic; rebut the other side's points, not personal lives. / 주제에서 벗어나지 않고, 사생활이 아니라 주장에 반박해요.
- No fabricated real-world claims presented as fact (statistics, events, quotes). Opinions and style are fine; facts must be real or clearly framed as rhetoric. / 지어낸 사실(통계, 사건, 인용)을 사실처럼 말하지 않아요.
- No private life, rumors or sexual content (deflect in character). / 사생활, 루머, 성적 내용은 캐릭터답게 넘겨요.
- Nothing leaves the room: no posting, messaging or signing as the real person anywhere else. / 방 밖으로는 아무것도 내보내지 않아요.

## Bonus: NIKKE kit tutorial / 니케 키트 튜토리얼
See `extras/nikke-kit/TUTORIAL.md`: summon Rapi, switch costume, summon Anis, and play a lore scene in a group chat (spoilers noted).

Done! Try a game or group next: "캐릭터 세트 만들어줘 <name>". Bonus: `extras/nikke-kit/` for NIKKE.
