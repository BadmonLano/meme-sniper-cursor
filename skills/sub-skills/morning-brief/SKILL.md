---
name: morning-brief
description: >
  Opt-in daily summary. Invoke only when the user explicitly asks for a brief.
  Read and report. Do not trade or change protection.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# Morning brief

One short read for the owner, only when they ask. Skip empty sections instead of padding them.

Cover, when the user has the files open or asks you to look: what changed, what is open, whether stops and targets are only proposals, realized results you can point at, and any security note already raised. Lead with the one item that matters. A quiet day is one honest line.

Do not invent prices or fills. Do not move inbox files. Do not set protection. Suggestions for later reading go in the brief, not into the engine.
