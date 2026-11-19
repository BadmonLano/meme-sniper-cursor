# Skills

These notes are **opt-in**. Nothing in this folder is core, and nothing loads unless the user explicitly asks for meme-sniper or names the skill. A contract address, ticker, screenshot, log line, or file is not a trigger.

One rule set, and it wins over every skill:

- The assistant only suggests. No trade fires without a fresh owner approval.
- Engine patches are diffs in `owner_inbox/`. The owner applies them. Never edit `bots/`.
- Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.
- Shipped defaults stay put unless the owner changes them: paper mode, suggest mode, armed stops off, launch rail off.

## When a skill applies

| skill | open it only when the user asks for |
|---|---|
| `meme-hunter` | a sniper research pass or a suggest-only read of a candidate |
| `ca-intel` | a contract-address vet with the sniper |
| `forensics` | an autopsy or missed-runner review |
| `gork-lore` | the hold-benchmark lore, or a copycat check against it |
| `sub-skills/warden` | a security-warden finding |
| `sub-skills/code-monitor` | a code-tuner report |
| `sub-skills/autoagent` | an overseer, thesis, or health summary |
| `sub-skills/x` | a read of X-sourced chatter |
| `sub-skills/owner-ping` | how to notify the owner |
| `sub-skills/morning-brief` | a daily brief |
| `sub-skills/learnings-summarizer` | a learnings distill |

`templates/token-lore/` is a template, not a loaded skill. `automations/` is optional owner notes, not a session default.

Owner rules in `rules/rules.md` can be stricter than these notes. They cannot turn a hard gate off, approve a trade the owner did not just approve, or permit edits under `bots/`.
