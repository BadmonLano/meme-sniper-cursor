---
name: owner-ping
description: >
  Opt-in format for notifying the owner. Invoke only when the user explicitly
  asks. A ping is a message, not a trade and not an approval.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# owner-ping

A ping asks or informs. It never approves a trade and never stands in for one.

Write it as a file in `owner_inbox/` when the user wants a record:

- kind: error, note, decision needed, or stuck
- severity: critical, high, medium, or low
- one specific summary
- evidence the owner can check
- the exact question, or none
- a stable dedupe key so the same fact is not repeated

In paper mode, start the text with `[PAPER]`. No secrets, keys, or private key material. If you cannot tell whether a message was delivered, say so. Do not continue a trade while you wait.
