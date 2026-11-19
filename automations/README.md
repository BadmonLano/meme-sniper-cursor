# Automations

Optional notes for the owner. They are not loaded with the plugin, and they are not a session default. Nothing here starts a trade, signs, launches, or edits `bots/`.

Run a note only when you explicitly ask. One pass, then stop. The assistant suggests. A trade still needs your fresh approval. Patches are diffs in `owner_inbox/` for you to apply.

The Python engine has its own cadence settings (`LANE_CADENCE_*` and the clock settings in `bots/.env`). Those are engine settings. They do not instruct the IDE assistant to keep a trading loop.

| note | what a single pass may do |
|---|---|
| `sniper_lane.automation.md` | Read sniper packets the owner points at and write a suggestion |
| `warden_lane.automation.md` | Read security findings and report them |
| `misc_lane.automation.md` | Route other notes to the matching opt-in skill |
| `morning_brief.automation.md` | Write the brief the owner asked for |
| `../learnings/nightly_self_eval.automation.md` | Distill learnings the owner asked for |
