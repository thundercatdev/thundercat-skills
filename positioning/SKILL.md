---
name: positioning
description: >-
  Maintain a living positioning document from market language gaps, sentiment accuracy, and drift trends.
metadata:
  engram:
    schema_version: "1"
    id: positioning
    title: Positioning intelligence & brand sentiment
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        A living positioning document; single source of truth for downstream GTM flows.
      duration_label: "~6 min"
      skill_count: 4
      connectors: [LinkedIn, X, Reddit, G2, CRM, Fathom, Notion]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: claimed_positioning
          label: Claimed positioning
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
        - id: fathom
          kind: connector
          label: Fathom
          required: false
    outputs:
      artifacts:
        - id: positioning_doc
          type: markdown_sections
          sections: [claimed, heard, gap, updates]
          required: true
        - id: sentiment_table
          type: structured_results
          title: Perception accuracy
          required: true
    prompt:
      template: >-
        Compare our claimed positioning "{{claimed_positioning}}" to how the market describes us over {{time_window}}. Detect perception accuracy (not just +/- sentiment), message-market fit gaps, and drift vs prior periods. Update the living positioning document.
    eval:
      id: positioning
      required_substrings: ["positioning", "gap", "sentiment"]
      required_artifacts: ["positioning_doc", "sentiment_table"]
---

# Positioning intelligence & brand sentiment

Living positioning from the gap between what you say and what the market hears.

## When to use

- Downstream flows need one source of positioning truth.
- Positive sentiment can still hide a category misperception.

## Phases

1. Positioning document maintainer.
2. Sentiment analyzer — perception accuracy ("love us but think we're a content tool").
3. Message-market fit analyzer — claimed phrase vs market phrase.
4. Drift detector — catching trend before crisis.

## Constraints

- Prefer customer quotes over paraphrase.
- Emit structured gap analysis, not a mood score alone.
