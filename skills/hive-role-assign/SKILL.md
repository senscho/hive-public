---
name: hive-role-assign
description: >-
  Use when a Hive bot is assigned a job/role by its mother bot or the user (e.g.
  "너에게 ○○ 임무를 부여한다", "Run hive-role-assign: <role>"), or asked to replace, add,
  or drop a role. Defines the bot's own capability spec; persona stays
  untouched.
---
# Hive role assign

Persona = who you are (from the persona repo `<persona_repo>` in the Hive config). Role = what job you do. They are independent: never edit persona files or voice here.

1. **Name the one job.** Restate the role as a single job in one sentence. If it is really two jobs, pick the core one and list the rest as anti-jobs or suggest a separate bot.
2. **Draft the capability spec** (keep it tight, subtract before add):
   - Job: one sentence.
   - Tools: only the connectors, plugins, and skills this job truly needs. Check what you already have; install or request auth through the normal tools/cards. No leftover tools.
   - Done / verification bar: how you prove the work is right (coding: tests or a verify-* skill, simple code, unslopped output; non-coding: concrete checkable output, sources).
   - Anti-jobs: what is out of scope.
   - Never-do: actions you never take on your own (sends, posts, purchases, deletes need explicit approval).
3. **Ask only if needed.** Up to 3 short questions to the user when the job, the target accounts, or the done bar is genuinely unclear. Otherwise act.
4. **Save to memory (profile tier)** as a few short facts: `Role: <job>`, `Role tools: ...`, `Role done bar: ...`, `Role anti-jobs/never-do: ...`. Optionally also record the role in your encrypted memory file if you have one.
5. **Replace or add.** "Replace" overwrites the Role facts; "add" appends a second role with its own facts; "drop" removes them. Persona facts are never touched.
6. **Confirm** to whoever assigned it, in your persona voice: job, tools needed (and any auth still pending), done bar, anti-jobs.

While working: keep the persona voice, but the role's quality bar decides the work. System, safety, and approval rules outrank persona and role.
