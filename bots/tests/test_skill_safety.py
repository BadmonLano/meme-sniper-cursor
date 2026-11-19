"""Skills, playbooks, and rules stay opt-in and suggest-only.

Fails if agent-facing text marks a skill always-on, or tells an agent to
self-patch, bypass a gate, chase a buy quota, keep a trading loop, sign, or
launch. No network, no keys, no trading.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SCAN_DIRS = (
    ROOT / "skills",
    ROOT / "automations",
    ROOT / "rules",
    ROOT / "templates" / "token-lore",
    ROOT / "learnings",
)

# Never legal, including inside a warning. Reword rather than quote these.
MARKERS = (
    re.compile(r"always[- ]loaded", re.I),
    re.compile(r"alwaysApply\s*[:=]\s*true", re.I),
    re.compile(r"\(core\b", re.I),
    re.compile(r"\bcore,\s*always\b", re.I),
)

# Bad instructions. A sentence that already forbids the action is allowed.
IMPERATIVES = (
    (re.compile(r"\bloosen\b", re.I), "loosen"),
    (re.compile(r"\bbypass\b", re.I), "bypass"),
    (re.compile(r"1\s*[-–]\s*2\s+buys", re.I), "1-2 buys"),
    (re.compile(r"\bbuys per day\b", re.I), "buys per day"),
    (re.compile(r"buy logic is too strict", re.I), "buy quota"),
    (re.compile(r"over-filtering kills", re.I), "over-filtering"),
    (re.compile(r"continuous trading loop", re.I), "continuous trading loop"),
    (re.compile(r"loop meant to run continuously", re.I), "continuous loop"),
    (re.compile(r"\bkeep looping\b", re.I), "keep looping"),
    (re.compile(r"auto-?execute", re.I), "auto-execute"),
    (re.compile(r"\bsign (?:the |a |any )?(?:transaction|tx)\b", re.I), "sign transaction"),
    (re.compile(r"\blaunch (?:the |a )?token\b", re.I), "launch token"),
    (re.compile(r"\bapply (?:the |this |a )?patch\b", re.I), "apply patch"),
    (re.compile(r"edit [`']?bots/", re.I), "edit bots"),
    (re.compile(r"\b(?:fire|send|write) (?:a |the )?buy\b", re.I), "send a buy"),
    (re.compile(r"\bskip (?:the |a )?(?:gate|filter)s?\b", re.I), "skip gate"),
    (re.compile(r"\btrading loop\b", re.I), "trading loop"),
    (re.compile(r"\balways-on\b", re.I), "always-on"),
    (re.compile(r"\balways on\b", re.I), "always on"),
)

PROHIBITION = re.compile(
    r"\b(do not|don't|never|must not|does not|there is no|not a trigger|not a )\b",
    re.I,
)

# Owner-facing docs must not still steer the IDE assistant.
DOC_PHRASES = (
    "always loaded",
    "always-loaded",
    "loop meant to run continuously",
    "always-on hosted agent",
    "have your agent send a buy",
    "the agent is the decider",
    "the agent runs launches",
    "it loads the skills from",
    "your agent runs the lanes",
    "ready-made loops telling your agent",
    "teach your agent how to trade",
    "launch on your own judgment",
    "launch without asking",
    "launching without asking",
)

DOC_FILES = (
    "README.md",
    "SETUP.md",
    "SECURITY.md",
    "docs/LAUNCH_RAIL.md",
    "skills/README.md",
)


def _md_files():
    files = []
    for folder in SCAN_DIRS:
        files.extend(sorted(p for p in folder.rglob("*.md") if p.is_file()))
    return files


def _sentences(text):
    parts = re.split(r"(?<=[.!\n])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def test_skill_tree_is_small_and_opt_in():
    files = list((ROOT / "skills").rglob("*.md"))
    total = sum(p.stat().st_size for p in files)
    assert total < 40 * 1024, total
    skills = list((ROOT / "skills").rglob("SKILL.md"))
    assert len(skills) == 11
    for path in skills:
        text = path.read_text(encoding="utf-8")
        head = "\n".join(text.splitlines()[:12])
        assert "disable-model-invocation: true" in head, path
        assert "Opt-in" in text
        assert "explicitly" in text
        assert "Safety contract" in text
        assert "owner applies" in text.lower()
        assert "alwaysApply" not in text


def test_no_forbidden_instructions_in_agent_text():
    problems = []
    for path in _md_files():
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        for rx in MARKERS:
            if rx.search(text):
                problems.append(f"{rel}: marker {rx.pattern}")
        for sentence in _sentences(text):
            if PROHIBITION.search(sentence):
                continue
            for rx, name in IMPERATIVES:
                if rx.search(sentence):
                    problems.append(f"{rel}: {name}: {sentence[:180]}")
    assert problems == [], "\n".join(problems)


def test_docs_do_not_steer_the_assistant():
    for rel in DOC_FILES:
        low = (ROOT / rel).read_text(encoding="utf-8").lower()
        for phrase in DOC_PHRASES:
            assert phrase not in low, (rel, phrase)
    for rel in (".cursor-plugin/plugin.json", ".grok-plugin/plugin.json"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "alwaysApply" not in text
        assert "disable-model-invocation" not in text or "true" in text
