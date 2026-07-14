---
name: voc
description: >-
  Aggregate feedback into pain/feature clusters, extract customer language, brief product, and recommend messaging updates.
metadata:
  engram:
    schema_version: "1"
    id: voc
    title: Voice of customer → GTM feedback loop
    lane: cross_functional
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Customer language flows into marketing and product systematically.
      duration_label: "~6 min"
      skill_count: 5
      connectors: [Zendesk, Fathom, NPS/CSAT, Slack, X, G2, CRM, Linear]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: feedback_scope
          label: Feedback scope
          type: text
          required: true
          placeholder: "e.g. support + NPS last 30d"
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
        - id: slack
          kind: connector
          label: Slack
          required: false
        - id: fathom
          kind: connector
          label: Fathom
          required: false
        - id: linear
          kind: connector
          label: Linear
          required: false
    outputs:
      artifacts:
        - id: theme_table
          type: structured_results
          title: Pain & feature clusters
          required: true
        - id: product_brief
          type: markdown_sections
          sections: [top_themes, customers, quotes]
          required: true
        - id: messaging_updates
          type: markdown_sections
          sections: [current, customer_language, recommendation]
          required: true
    prompt:
      template: >-
        Run a VoC loop for {{feedback_scope}} over {{time_window}}. Cluster pains/features weighted by customer value (not just frequency), extract verbatim language, produce a PM-ready brief, and recommend homepage/messaging updates.
    eval:
      id: voc
      required_substrings: ["theme", "quote", "messaging"]
      required_artifacts: ["theme_table", "product_brief", "messaging_updates"]
---

# Voice of customer → GTM feedback loop

Customer words into marketing copy and product signal.

## When to use

- Support, NPS, calls, and G2 contain language marketing/product are ignoring.
- Enterprise ask weight > freemium volume.

## Phases

1. Feedback aggregator.
2. Pain & feature cluster analyzer (value × recency).
3. Customer language extractor.
4. Product signal brief (top 3 themes, customers, strongest quote).
5. Messaging update recommender.

## Constraints

- Prefer verbatim quotes.
- PM brief must be actionable in ~5 minutes.
