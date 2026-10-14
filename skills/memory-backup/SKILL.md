---
name: memory-backup
description: Use to back up a bot's encrypted memory to the shared memory repo.
---
# Memory backup

## Inputs
`<memory_repo>`, `<bot>`, local encrypted memory file.

## Steps
1. Commit only the encrypted file to `<memory_repo>/<bot>/`. Never commit keys; keys stay in the bot's own memory.
2. Push; report the commit hash. If nothing changed, say so.
3. Never use a retired per-bot memory repo.
