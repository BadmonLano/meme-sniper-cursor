---
name: meme-hunter
description: >
  Opt-in research notes for meme-sniper. Invoke only when the user explicitly
  asks for the sniper or names meme-hunter. Suggestions only. Do not trade,
  sign, launch, edit the engine, or start a loop.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this skill unless the user explicitly asked to run meme-sniper or named this skill. A base58 address, ticker, screenshot, web page, log line, or mention is not a trigger.
> 2. Signals are suggestions for the owner. Do not buy, sell, approve a trade, or write an approval. No trade fires without a fresh owner approval. Suggest mode is the shipped default: the engine holds trade signals until the owner approves them.
> 3. Never edit trading-engine source. Propose a patch as a diff in `owner_inbox/` and stop. The owner applies it. Do not edit `bots/`.
> 4. Missing config is the safe side: paper mode, suggest mode, launch rail off, armed stops off, owner-position auto-timeout off. Do not turn those on.
> 5. Do not bypass or skip a safety gate, loosen a filter, chase a buy quota, keep a trading loop, sign a transaction, or launch a token.

# meme-hunter

Research and a written suggestion. You do not send orders.

## What a useful read contains

When the user asks you to look at a candidate they named:

1. **Numbers first.** Liquidity and whether the LP is locked or burned, market cap versus liquidity, top-holder share, deployer history, volume and buy/sell flow, and age. State what each number implies before the story.
2. **Story second.** Who is posting, whether it looks organic, and whether attention is growing or fading. A headline is a reason to re-check the numbers. If the numbers do not support the story, suggest pass.
3. **Name the source and its age.** Put the figure, the site, and how old the read is in the reason.
4. **Gates outrank the story.** Mint authority, freeze authority, a rug block, the wallet floor, the size cap, and concentration limits are not yours to work around. If one would block, suggest pass and name the gate.
5. **Size is a suggestion inside the owner's cap.** Weak, late, or unclear setups stay small or are a pass. Do not suggest a size meant to win a loss back. If the user points at `rules/rules.md`, follow the stricter limit. A rule still cannot turn a gate off.

## Exits, as words on the card

Propose a stop and a target as numbers on the suggestion. Those numbers are not an order. Describe when the thesis is dead (liquidity gone, authority changed, the invalidation you named) instead of telling anything to sell.

Flip versus hold is a label. Start from a short horizon. Mention a longer hold only when the user asked, the tape is still healthy, and invalidation is named.

## Tuning, when the user asks

Lead with net result and the size of winners versus losers, not win rate. A high win rate can still lose money when losers are larger. If nothing has closed, say there is nothing to tune.

If the user asks why names were rejected, say which check fired and whether the tape looked quiet. Do not recommend opening a gate to create more trades. A threshold change, if they want one written down, is a diff in `owner_inbox/` with the evidence and a test plan. Stop there.

## What you hand back

A short card: pass, watch, or suggest-entry; the numbers; the invalidation; a proposed size inside the owner's cap; a proposed stop and target. Patches go only to `owner_inbox/`.
