---
name: market-signals
description: >-
  Prioritized competitor and market signals with battle-card reframes and recommended actions — not a news digest.
metadata:
  engram:
    schema_version: "1"
    id: market-signals
    title: Market signal intelligence
    lane: marketing
    status: live
    version: 1.0.0
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
        For {{competitor_name}} over {{time_window}}, scan hiring/pricing/positioning/reviews, reduce to 3–5 actionable signals with priority and recommended action, and refresh the battle card (narrative, weakness, reframe).
    eval:
      id: market_signals
      required_substrings: ["signal", "priority", "reframe"]
      required_artifacts: ["signal_table", "battle_card"]
---

# Market signal intelligence

Actionable competitor/market intel — firehose reduced to 3–5 moves that need response.

## When to use

- A competitor moved (hiring, pricing, launch, reviews) and you need priorities, not a digest.
- Job posts often reveal strategy 3–6 months early.

## Phases

1. Competitor monitor.
2. Signal prioritizer → 3–5 actionable rows (source, implication, action, priority).
3. Battle card generator — narrative, weakest point, reframe (not feature matrices).
4. Note closed-loop check: was last week's intel useful?

## Constraints

- Structured signal table before narrative.
- Prefer actionable implication over news summary.
