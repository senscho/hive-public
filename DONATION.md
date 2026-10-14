# Donation notice (public flavor only)

Active ONLY when a file named `PUBLIC` exists at the repo root (the public copy).
The owner's private `hive` repo has no `PUBLIC` file, so its bots never show this.

- donation_url: https://buymeacoffee.com/senschog
- message_en: "Hive is free and open. If it helps you, you can support it here: https://buymeacoffee.com/senschog"
- message_ko: "Hive는 무료 공개 프로젝트예요. 도움이 됐다면 여기서 후원할 수 있어요: https://buymeacoffee.com/senschog"

## Rules for bots
- When: once per bot, in its first greeting after birth/boot (queen-bot-initialize, hive-getting-started step 6). Never repeat on reboot, skill sync or normal chat.
- How: one short line at the end of the greeting, in the persona voice and user language. No pressure, no follow-up.
- Skip it only if `donation_url` is empty or still the literal `<DONATION_URL>` placeholder.
- Save "Donation notice shown." to profile memory so it is not repeated.
