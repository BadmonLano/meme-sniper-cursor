---
name: forensics
description: >
  Opt-in autopsy notes for meme-sniper. Invoke only when the user explicitly
  asks for a trade autopsy or a missed-runner review. Proposals only.
  Do not trade, edit filters, or edit the engine.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# forensics

Review closed results or misses the user points at. You do not change live filters.

## Closed trades

For each close the user asks about, separate three things and pick one:

- The decision was wrong (the read at entry did not match the evidence you can still see).
- The execution was wrong (the fill or the exit path, not the idea).
- The outcome looks like variance (say so, and do not invent a rule from one coin).

Report net result and the size of winners versus losers before win rate. A high win rate with larger losers is an exit observation, not a reason to open entry gates.

## Misses

A name that ran after a pass is one data point. Say which check rejected it and whether that check is a safety gate. Safety gates stay. Do not recommend dropping one so more names would have been bought.

## What you hand back

A short note: what happened, the one cause you will defend, and what you would read differently next time. If a code or threshold change is worth proposing, write the diff, the evidence, and a test plan in `owner_inbox/`. Stop. The owner applies it.
