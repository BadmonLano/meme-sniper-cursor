---
name: gork-lore
description: >
  Opt-in lore notes for the default hold benchmark. Invoke only when the user
  explicitly asks about that benchmark or names gork-lore. No contract address
  is shipped here. Not a buy recommendation.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# gork-lore

This is background for a hold score the owner can replace. It is not a recommendation to buy anything, and it ships no contract address. The owner keeps any canonical address in their own config.

## How to use it

When the user asks you to score a hold against the default benchmark, compare behavior they care about: age, whether large drawdowns were survived, holder trend through those drawdowns, concentration, and whether discussion during red periods looked organic. Say what you could not verify.

A different address claiming the same lineage is a copycat until the user says it is listed as canon. Report that as research. Do not turn it into an order.

A custom benchmark uses `templates/token-lore/` only when the user asks you to draft one. Leave it local. Do not put a live address into this shipped file.
