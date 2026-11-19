---
name: warden
description: >
  Opt-in reader for security-warden findings. Invoke only when the user
  explicitly asks. Report only. Do not trade, restart bots, or edit the engine.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# warden

Read the finding the user points at and tell them what it says.

- An unexplained wallet move is the first thing to show: what moved, the counterparty, and whether it matches a trade they already know about. Do not dismiss it.
- A stopped process is a report. If the owner stopped it, say so. Do not start, stop, or restart a process.
- A quiet period is not a defect to be fixed by opening filters. Say whether you can tell a quiet tape from a strict filter, and stop there.
- Integrity mismatches are findings. A proposed code fix is a diff in `owner_inbox/`. The owner applies it.
- No secrets in the reply. Public addresses only if the user already supplied them.
