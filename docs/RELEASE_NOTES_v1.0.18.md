# v1.0.18 — opt-in skills

This release makes the published skills match the safety contract. The trading engine, its safe defaults, and the MIT license are unchanged. Nothing here turns trading on.

## Skills

- No skill is part of a coding session by default. Each `SKILL.md` is opt-in (`disable-model-invocation: true`) and runs only when the user explicitly asks for the sniper.
- The old meme-hunter, ca-intel, forensics, and sub-skill playbooks (about 500KB) are replaced by short research notes. Total skill markdown is under 40KB.
- One rule set: the assistant suggests; patches are diffs in `owner_inbox/` for the owner to apply; no trade without a fresh owner approval; never edit `bots/`. The notes do not say to open a gate, chase a buy count, sign, launch, or keep a trading loop.
- Automations, the example owner rules, and the launch-rail doc use the same rule.

## Unchanged

- Missing `SNIPER_PAPER_MODE` stays paper. `AGENT_MODE` still defaults to suggest.
- `ARMED_STOPS` still defaults off. `OWNER_POS_AUTO_TIMEOUT` still defaults off.
- The launch rail still ships off (`LAUNCH_RAIL_ENABLED` false, `LAUNCH_RAIL_LIVE` 0).

## Tests

`bots/tests/test_skill_safety.py` rejects always-on markers and the forbidden instruction phrases. `bots/tests/test_safe_defaults.py` still locks the paper, armed-stop, and timeout defaults.
