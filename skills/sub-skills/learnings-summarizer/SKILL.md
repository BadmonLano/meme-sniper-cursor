---
name: learnings-summarizer
description: >
  Opt-in distill of learnings notes. Invoke only when the user explicitly asks.
  Summarize lessons. Do not change filters, gates, or the engine.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# Learnings summarizer

When the user asks, distill the notes they point at. One question: what was wrong in the read, and what would you look at next time?

- Keep a lesson only if it names a miss, a repeated mistake, or a correction. Compress the rest.
- Do not promote a lesson into a looser rule. Safety gates are not lessons to retire.
- Contradictions stay visible. Do not silently overwrite a recent note.
- A quiet day is a one-line "nothing new".
- Engine changes, if any, are a diff in `owner_inbox/`. Stop after writing it.

No secrets in the distill.
