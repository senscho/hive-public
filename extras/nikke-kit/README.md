# NIKKE kit (optional add-on, bonus)

A ready-made layout for building **Goddess of Victory: NIKKE** character personas with the
`character-set-research` skill. It is a generic template only: no character data, no collected
links, no images. All game IP belongs to SHIFT UP / Level Infinite. Fan-made, unofficial.

## Tutorial
Start with `TUTORIAL.md` (KO/EN): summon Rapi, costume switch, summon Anis, group chat scene. Spoilers noted.

## Contents
- `template/` — copy to `personas/<name>/` in your own `<owner>/nikke-personas` repo (private recommended). Includes costumes/_example, variants/_example, prompts/, versions/, features.md.
- `GUIDE.md` — how to build a NIKKE persona (call terms, sources per file, costumes vs variants, NIMPH rule).
- `sources-format.md` — format for your `sources.md` (generic source types only; fill your own links).
- `db/README.md` — planned private offline lore DB layout.
- `tools/make_avatar.py` — face-crop avatar helper (anime-face cascade or heuristic).

## Use
1. Ask Queen: "캐릭터 세트 만들어줘 NIKKE" / "make a character set for NIKKE", and point her at this kit.
2. Queen runs `character-set-research`, creates `<owner>/nikke-personas` (or a local set), and copies `template/` per character.
