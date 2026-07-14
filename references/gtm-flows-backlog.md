# GTM flows backlog (from engram-demos)

**Source:** [tryvinci/engram-demos](https://github.com/tryvinci/engram-demos) · `lib/skill-demos/gtm-flows.ts`  
**Purpose:** Forward-looking catalog for Skill Hub package migration. Not published to the hub until each flow becomes a locked `SKILL.md` package in `manifest.json`.

**Live today:** All 13 workflow slugs below are published as Skill Hub packages (plus composite `competitive-intel-content-brief` = `market-signals` + `content-linkedin`). This file remains the atomic-skill decomposition reference.

**Authoring bar (v1.1):** trigger-rich `description` with when-not-to-use routing; procedure bodies with phases/constraints (not atom-name lists); fixture-tied `evals/golden.json`; lean `references/` for rubrics that would bloat the body.

---

## Summary

| ID | Slug | Lane | Atomic skills | Connectors |
|----|------|------|---------------|------------|
| 1A | icp-community | Marketing | 5 | Facebook Groups, Reddit, Google Business, Yelp, CRM, Apollo |
| 1B | icp-linkedin | Marketing | 4 | LinkedIn, Sales Navigator, CRM, Apollo |
| 1C | icp-developer | Marketing | 3 | HN, GitHub, Product Hunt, CRM, Apollo |
| 2A | content-linkedin | Marketing | 5 | LinkedIn, Slack, Fathom, Granola, Shield |
| 2B | content-x | Marketing | 4 | X/Twitter, Slack, X analytics |
| 3A | positioning | Marketing | 4 | LinkedIn, X, Reddit, G2, CRM, Fathom, Notion |
| 3B | market-signals | Marketing | 4 | LinkedIn, X, Crunchbase, Product Hunt, HN, G2, Press |
| 4 | outbound | Sales | 4 | CRM, Apollo, LinkedIn Sales Nav, Amplemarket, Outreach |
| 5A | pre-call | Sales | 3 | CRM, Fathom, Gmail, Zendesk, LinkedIn, X, Crunchbase |
| 5B | pipeline | Sales | 4 | CRM, Email, Web analytics, LinkedIn, Outreach |
| 6 | launch | Sales | 4 | Slack, Notion, GitHub, Linear, CMS, Resend, CRM, Intercom, Mixpanel |
| 7 | voc | Cross-functional | 5 | Zendesk, Fathom, NPS/CSAT, Slack, X, G2, CRM, Linear |
| 8 | onboarding-bridge | Customer success | 3 | CRM, Fathom, Gmail, Slack, Notion |
| 9 | renewal | Customer success | 3 | CRM, Mixpanel, Amplitude, Zendesk, Fathom, NPS/CSAT, Stripe |

**Total:** 13 workflows · ~55 atomic skills

---

## Marketing

### 1A — ICP signal discovery (community & social) `icp-community`

**Outcome:** Qualified leads from channels competitors aren't watching — daily delivery with custom hooks.

**Atomic skills:** Platform scanner (community mode), Intent signal detector, Business verifier, CRM deduplicator, Hook generator.

**Key insight:** Hooks must reference the exact context that surfaced the lead (Facebook post, Yelp review, specific complaint). Generic hooks are invisible.

### 1B — ICP signal discovery (professional networks) `icp-linkedin`

**Outcome:** Qualified LinkedIn leads with context-rich hooks; hiring patterns as leading indicator.

**Atomic skills:** Platform scanner (LinkedIn mode), Firmographic fit scorer, CRM deduplicator, Hook generator (professional mode).

**Key insight:** Job postings are the most underused leading indicator — 3 marketing roles in 2 weeks = context transfer problem about to get expensive.

### 1C — ICP signal discovery (developer communities) `icp-developer`

**Outcome:** Leads from HN, GitHub, Product Hunt before they show up on LinkedIn.

**Atomic skills:** Platform scanner (technical mode), Intent signal detector (technical), Hook generator (technical mode).

### 2A — Content engine (LinkedIn) `content-linkedin`

**Outcome:** Each GTM team member posting consistently in their own voice; inbound attributable to LinkedIn.

**Atomic skills:** Strategy brief generator, Voice-calibrated drafter (LinkedIn), Thread & conversation finder, Performance tracker (LinkedIn), Voice recalibrator.

**Partially shipped:** voice-calibrated drafting in `competitive-intel-content-brief`.

### 2B — Content engine (X) `content-x`

**Outcome:** Team presence in the right X conversations — not broadcasting.

**Atomic skills:** Thread finder (X), Voice-calibrated drafter (X), Reply drafter, Performance tracker (X).

### 3A — Positioning intelligence & brand sentiment `positioning`

**Outcome:** Living positioning document; single source of truth for downstream flows.

**Atomic skills:** Positioning document maintainer, Sentiment analyzer, Message-market fit analyzer, Positioning drift detector.

**Key insight:** Sentiment isn't positive/negative — detect perception accuracy ("They love us but think we're a content tool").

### 3B — Market signal intelligence `market-signals`

**Outcome:** Prioritized feed with recommended actions — not a news digest.

**Atomic skills:** Competitor monitor, Battle card generator, Signal prioritizer, Signal performance tracker.

**Partially shipped:** signal prioritization + battle card reframe in `competitive-intel-content-brief`.

---

## Sales

### 4 — Outbound sequence personalization `outbound`

**Outcome:** Outbound reflecting real prospect pain; each sequence references the qualifying signal.

**Atomic skills:** Prospect researcher, Sequence drafter, Hook generator (outbound mode), Customer language extractor.

### 5A — Pre-call intelligence brief `pre-call`

**Outcome:** Nobody walks into a call cold — relationship narrative, recent context, the play.

**Atomic skills:** Pre-call brief generator, News & activity scanner, Stakeholder mapper.

### 5B — Pipeline scoring & prioritization `pipeline`

**Outcome:** Pipeline ranked by likelihood to close; social as leading indicator; clear next action per deal.

**Atomic skills:** Behavioral signal scorer, Champion activity tracker, Deal velocity analyzer, Next action recommender.

### 6 — Product launch GTM orchestration `launch`

**Outcome:** Coordinated launches; post-launch tracking closes the loop.

**Atomic skills:** Launch coordinator, Voice-calibrated drafter (launch mode), Battle card generator (launch mode), Performance tracker (launch mode).

---

## Cross-functional & customer success

### 7 — Voice of customer → GTM feedback loop `voc`

**Outcome:** Customer language flows into marketing and product systematically.

**Atomic skills:** Feedback aggregator, Pain & feature cluster analyzer, Customer language extractor, Product signal brief generator, Messaging update recommender.

### 8 — Customer onboarding context bridge `onboarding-bridge`

**Outcome:** Zero context loss at handoff — why they bought, who championed, success criteria, landmines.

**Atomic skills:** Onboarding brief generator, Stakeholder mapper (onboarding mode), Customer language extractor (onboarding mode).

### 9 — Renewal & expansion intelligence `renewal`

**Outcome:** CS walks into every renewal with expansion angle and churn risk identified.

**Atomic skills:** Customer health scorer, Renewal brief generator, Champion activity tracker (renewal mode).

---

## Legacy demo slug map

| Legacy slug | Resolves to |
|-------------|-------------|
| `icp-discovery` | `icp-community` |
| `content-generation` | `content-linkedin` |

---

## Migration checklist (per flow)

1. Author `{slug}/SKILL.md` with `metadata.engram` (lane, tools, config, outputs, eval).
2. Add scripts/references/evals as needed.
3. Run `python scripts/validate.py`.
4. Add entry to `manifest.json` → `published`.
5. Sync to engram-chat: `python apps/engram-chat/scripts/sync_skill_packages.py`.
6. Dogfood via `/dashboard/skills`.
