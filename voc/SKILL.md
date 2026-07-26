---
name: voc
description: >-
  Aggregate customer feedback into pain/feature clusters weighted by
  value×recency×severity, extract anonymized verbatim language, brief product, and
  recommend messaging updates. Use when support/NPS/calls/G2 language is not flowing
  into marketing or PM. Do not use for living positioning docs (positioning),
  competitor moves (market-signals), or renewal health (renewal).
metadata:
  engram:
    schema_version: "1"
    id: voc
    title: Voice of customer → GTM feedback loop
    lane: cross_functional
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Clusters weighted by value×recency×severity; customer language flows into marketing and product.
      duration_label: "~6 min"
      skill_count: 5
      connectors: [Slack, Fathom, Linear]
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
        - key: supplied_feedback
          label: Pasted feedback (optional fallback)
          type: text
          required: false
          default: ""
          placeholder: "Paste tickets/NPS/quotes when Zendesk/NPS/G2/CRM are not connected"
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
        Run a VoC loop for "{{feedback_scope}}" over {{time_window}}. Use enabled
        tools plus any pasted notes: "{{supplied_feedback}}". Cluster pains/features
        by value × recency × severity (not raw frequency). Anonymize customer
        identities by default; keep verbatim quotes only after consent/visibility
        check. Produce a PM-ready brief (top 3 themes, named-or-anonymized customers,
        strongest quote); recommend homepage/messaging updates as current →
        customer language → replace — never publish unapproved confidential quotes.
    eval:
      id: voc
      required_substrings: [NPS, value, recency, severity, theme, quote, customer language, replace]
      required_artifacts: [theme_table, product_brief, messaging_updates]
---

# Voice of customer → GTM feedback loop

Customer words into marketing copy and product signal.

## When to use

- Support, NPS, calls, and G2 contain language marketing/product are ignoring.
- Enterprise ask weight should beat freemium volume.

## When not to use

- Claimed-vs-heard positioning document → `positioning`.
- Renewal expansion/churn play → `renewal`.

## Phases

1. Aggregate feedback from the configured scope via enabled tools (Slack/Fathom/Linear + web/memory).
   State gaps when Zendesk/NPS/G2/CRM are not connected — do not invent private tickets.
2. Cluster per `references/cluster-weighting.md`.
3. Extract verbatim customer language.
4. PM brief: top 3 themes, named customers, strongest quote.
5. Messaging update recommender.
6. Emit **theme_table**, **product_brief**, **messaging_updates**.

## Constraints

- Prefer verbatim quotes after anonymization / consent check; exclude unapproved PII.
- When Zendesk/NPS/G2/CRM are not connected, use `supplied_feedback` or state the gap — do not invent tickets.
- PM brief must be actionable in ~5 minutes.
