# Owner trading rules (example)

Copy this file to `rules/rules.md` (or let the setup wizard write it) and edit it yourself. These are your limits. They can make suggestions stricter. They cannot turn off a hard safety gate, approve a trade you did not just approve, or allow edits under `bots/`.

The assistant only suggests. Patches are diffs in `owner_inbox/` for you to apply. No trade fires without your fresh approval.

## Max size
<!-- Largest buy in SOL, or % of wallet per trade (e.g. 0.25 SOL / 10%) -->
Suggest at most 0.1 SOL per buy, and never more than 10% of the wallet in one token.

## No-trade hours
<!-- Local hours or days you never want new suggestions to lean toward entry -->
No new entry suggestions 01:00-07:00 local time.

## Banned tokens / categories
<!-- CAs, tickers or categories never to suggest buying -->
No political tokens.

## Loss limits
<!-- Daily / weekly loss that stops new entry suggestions -->
Stop new entry suggestions for the day after -0.5 SOL realized.

## Exits
<!-- How you want exits described on a suggestion card -->
Suggest peeling half at 2x. Do not treat that sentence as a sell.

## Other
<!-- Anything else the assistant must always or never do -->
Ask before describing a bag as a hold. Do not sign, launch, or edit the engine.
