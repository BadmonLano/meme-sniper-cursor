---
name: ca-intel
description: >
  Opt-in contract-address research for meme-sniper. Invoke only when the user
  explicitly asks to vet an address with the sniper or names ca-intel.
  Suggestions only. Do not trade, sign, or edit the engine.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# ca-intel

There is no auto-trigger. The user must ask for a vet.

## What to check

Read what the user handed you and, if they asked you to look it up, public pages only (the pair, the mint, holders). Report:

- Mint and freeze authority. Active authority is a reason to suggest pass.
- Liquidity, whether it is locked or burned, and market cap versus liquidity.
- Holder concentration and whether the top wallets look related or freshly funded.
- Deployer history: prior launches, sells, and rugs you can actually see.
- Age, volume, and whether flow is two-sided.
- The narrative, after the numbers, and whether posters look organic.

Unknown is unknown. Do not treat a missing data source as a pass.

## Words

The engine's own labels, when a packet has them, are `avoid`, `tradeable`, `caution`, `neutral`, and `no_dex_data`. Your overlay words are suggestion language only: pass, watch, or suggest-entry. Do not describe either set as an order.

A `block` or hard safety failure means the suggestion is pass. Do not propose a path around it.

## What you hand back

One card: the address, each check with its source and age, the gaps, and pass / watch / suggest-entry with a one-line reason. If the user wants a code change, write a diff in `owner_inbox/` and stop.
