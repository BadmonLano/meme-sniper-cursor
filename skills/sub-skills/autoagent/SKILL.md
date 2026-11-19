---
name: autoagent
description: >
  Opt-in summary of overseer, thesis, and health notes. Invoke only when the
  user explicitly asks. Suggestions only. Do not trade or edit the engine.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# autoagent

When the user asks for an overseer note, a thesis, or a health check, summarize what they pointed at.

- Lead with the one finding that matters.
- Separate facts you can point at from guesses.
- A thesis is a hypothesis for the owner to read. It does not raise or lower a trade, and it is not a gate.
- Health means: is the process up, are there unexplained errors, is anything asking the owner for a decision. Report it. Do not restart anything.
- Follow-ups are sentences in the reply, or a diff in `owner_inbox/` if code is involved. Do not apply them.
