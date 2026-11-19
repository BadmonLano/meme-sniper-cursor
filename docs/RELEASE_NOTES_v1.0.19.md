# v1.0.19 — wording only

No engine behavior, default, or config key changed. Paper mode, suggest mode, armed stops off, and the launch rail off stay as shipped. MIT license unchanged.

## Wording

- v1.0.16 history in `CHANGELOG.md` and `TIMELINE.md` now describes active hours and lane cadences, and notes that v1.0.17 and v1.0.18 made skills opt-in and suggest-only.
- The `ACTIVE_HOURS` label says "the whole day" instead of a 24/7 loop. The key is the same.
- The launcher log says `configured from setup.json` when that file is applied, and `configured from existing .env` when `.env` was already complete. The apply path is the same.
- `SETUP.md`, the README, and the wizard copy describe `AGENT_MODE=auto` as an owner-only opt-in. The default is still `suggest`. An agent never sets it. The owner still confirms with `AUTO`.
