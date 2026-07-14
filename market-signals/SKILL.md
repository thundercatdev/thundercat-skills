---
name: market-signals
description: >-
  Prioritize competitor/market moves into 3–5 actionable signals with battle-card
  reframe (hiring, pricing, positioning, reviews). Use when you need a response
  plan, not a news digest. Do not use for drafting social posts (use content-linkedin
  or the competitive-intel-content-brief composite) or for living brand positioning
  (use positioning).
metadata:
  engram:
    schema_version: "1"
    id: market-signals
    title: Market signal intelligence
    lane: marketing
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Prioritized feed with recommended actions and accountability — not a digest.
      duration_label: "~4 min"
      skill_count: 4
      connectors: [LinkedIn, X, Crunchbase, Product Hunt, HN, G2, Press]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: competitor_name
          label: Competitor or topic
          type: text
          required: true
        - key: time_window
          label: Time window
          type: select
          default: 7d
          options:
            - value: 7d
              label: Last 7 days
            - value: 30d
              label: Last 30 days
    orchestration:
      tools:
        - id: web_research
          kind: system
          label: Public web research
          required: true
        - id: memory
          kind: system
          label: Brand memory
          required: true
        - id: notion
          kind: connector
          label: Notion
          required: false
    outputs:
      artifacts:
        - id: signal_table
          type: structured_results
          title: Prioritized market signals
          required: true
        - id: battle_card
          type: markdown_sections
          sections: [narrative, weakness, reframe]
          required: true
    prompt:
      template: >-
        For {{competitor_name}} over {{time_window}}, scan hiring/pricing/positioning/reviews.
        Reduce to 3–5 P1–P3 signals (source, implication, recommended action, priority), then
        refresh the battle card with narrative, weakness, and reframe — not a feature matrix.
    eval:
      id: market_signals
      required_substrings: [Acme Corp, P1, reframe]
      required_artifacts: [signal_table, battle_card]
---

# Market signal intelligence

Actionable competitor/market intel — firehose cut to moves that need a response.

## When to use

- A named competitor moved (hiring, pricing, launch, reviews) and you need priorities.
- Job posts often reveal strategy 3–6 months early.

## When not to use

- You already have the signal and need a LinkedIn/X draft → `content-linkedin` / `content-x`.
- You need claimed-vs-heard brand positioning → `positioning`.
- You want signals **and** a channel draft in one run → `competitive-intel-content-brief`.

## Phase 1 — Monitor & prioritize

1. Scan hiring, pricing, positioning, and review drift for the configured window.
2. Reduce to **3–5** rows using `references/signal-rubric.md`.
3. Emit **signal_table** before any narrative summary.

## Phase 2 — Battle card

1. Write narrative (what they claim), weakness, reframe (how we win the conversation).
2. Optionally note closed-loop check: was last week's intel useful?

## Constraints

- Structured table before prose.
- Prefer actionable implication over news summary.
- Use only tools enabled for this run; deliver exportable artifacts.
