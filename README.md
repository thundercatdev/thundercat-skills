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

| ID | Status | Lane | Notes |
|----|--------|------|-------|
| `competitive-intel-content-brief` | live | marketing | Composite of market-signals + content-linkedin (default enabled) |
| `icp-community` | live | marketing | Community / review ICP signals |
| `icp-linkedin` | live | marketing | LinkedIn / hiring ICP signals |
| `icp-developer` | live | marketing | HN / GitHub / PH ICP signals |
| `content-linkedin` | live | marketing | LinkedIn content engine |
| `content-x` | live | marketing | X content engine |
| `positioning` | live | marketing | Positioning + sentiment |
| `market-signals` | live | marketing | Competitor signal intel |
| `outbound` | live | sales | Personalized sequences |
| `pre-call` | live | sales | Pre-call brief |
| `pipeline` | live | sales | Deal scoring |
| `launch` | live | sales | Launch orchestration |
| `voc` | live | cross_functional | VoC → GTM loop |
| `onboarding-bridge` | live | customer_success | Sales → CS handoff |
| `renewal` | live | customer_success | Renewal / expansion intel |

Draft packages may exist in this repo but stay hidden until added to `manifest.json`.

## Backlog

Source catalog from [engram-demos](https://github.com/tryvinci/engram-demos): [`references/gtm-flows-backlog.md`](./references/gtm-flows-backlog.md) (13 atomic workflows + composite). All 13 workflow slugs are now published packages; keep the backlog for atomic-skill decomposition notes.

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
