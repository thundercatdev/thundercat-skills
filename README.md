# Engram Skills

GTM skill packages for [Skill Hub](../../docs/skill-hub-v1.md). Each published skill is a portable **AgentSkills / OpenClaw** package:

```text
{skill-id}/
├── SKILL.md       # name, description, metadata.engram, procedure
├── scripts/       # optional helpers
├── references/    # optional docs
└── evals/         # optional golden cases
```

**Format spec:** [docs/engram-skill-format.md](../../docs/engram-skill-format.md) (monorepo)  
**Split repo:** `engramdev/engram-skills` (synced from `apps/engram-skills/`; branch mirrors monorepo — `main` on merge, feature branches keep their name)

## Published skills (manifest lock)

Only skills listed in [`manifest.json`](./manifest.json) are published to Skill Hub and synced into engram-chat.

| ID | Status | Notes |
|----|--------|-------|
| `competitive-intel-content-brief` | live | Composite of market-signals + content-linkedin |

Draft packages may exist in this repo but stay hidden until added to `manifest.json`.

## Backlog

Forward-looking migration catalog from [engram-demos](https://github.com/tryvinci/engram-demos): [`references/gtm-flows-backlog.md`](./references/gtm-flows-backlog.md) (13 workflows, ~55 atomic skills).

## Validate

```bash
cd apps/engram-skills
python -m pip install -r requirements.txt
python scripts/validate.py
# or: npm run validate
```

CI runs the same check on push/PR (`.github/workflows/ci.yml`).

## Sync into engram-chat (Docker)

```bash
python apps/engram-chat/scripts/sync_skill_packages.py
```

Copies `manifest.json` + published skill dirs → `apps/engram-chat/skill_packages/` before `docker build`.

## Adding a skill

1. Create `{skill-id}/SKILL.md` (+ optional folders).
2. Run `python scripts/validate.py` (without manifest entry = draft only).
3. Add to `manifest.json` → `published` when ready to ship.
4. Re-run validate + sync script; dogfood via `/dashboard/skills`.
