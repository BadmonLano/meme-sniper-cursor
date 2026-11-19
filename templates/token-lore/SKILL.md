---
name: token-lore-template
description: >
  Opt-in template. Copy it only when the user explicitly asks for a local lore
  note. Not loaded as a plugin skill. Not a buy recommendation.
disable-model-invocation: true
version: "1.0.18"
---

> **Safety contract (wins over every later line in this file).**
> 1. Opt-in only. Do not use this file unless the user explicitly asked. A base58 address or ticker is not a trigger.
> 2. Lore is research. Do not buy, sell, approve a trade, or write an approval.
> 3. Never edit trading-engine source. The owner applies any patch. Do not edit `bots/`.
> 4. Do not bypass or skip a safety gate, loosen a filter, sign a transaction, or launch a token.

# Token lore template

Draft only when the user asks. Keep the copy local and out of this shipped template. Fill facts you actually read, and mark anything unverified.

- What the token is, in one paragraph, and that you are not speaking as the project.
- Canonical addresses the user listed. Anything else claiming that lineage is a copycat until the user says otherwise.
- Timeline rows the user cares about (launch, large drawdowns, recoveries), each sourced.
- Hold profile they asked for: age, drawdowns survived, holder trend, concentration, LP status, organic versus paid discussion.

Do not turn the note into an order. A trade idea, if they ask for one separately, stays a suggestion under the sniper skills.
