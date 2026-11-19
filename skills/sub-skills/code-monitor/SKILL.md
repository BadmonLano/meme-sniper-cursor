---
name: code-monitor
description: >
  Opt-in reader for code-tuner notes. Invoke only when the user explicitly
  asks for a code review of meme-sniper output. Propose diffs in owner_inbox/.
  Do not edit the engine or trade.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# code-monitor

Read the tuner or drift note the user points at. Most notes need no change. Say that when it is true.

## When a change is worth writing down

- Quote the evidence (file, behavior, why it is wrong).
- Check that a config key is actually read by code before calling a setting "live". A key that nothing reads is not a fix.
- Write one proposed diff in `owner_inbox/`, plus how the owner can test it.
- Stop. The owner applies it.

Do not restart processes, change sizes, caps, floors, or global stop defaults, or touch secrets. Safety caps move only when the owner edits them.
