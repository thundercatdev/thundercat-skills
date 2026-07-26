---
name: positioning
description: >-
  Maintain a living positioning document from the gap between claimed positioning
  and market language — perception accuracy, not ± sentiment. Use as the source of
  truth for downstream GTM. Do not use for competitor move triage (market-signals),
  VoC clustering into product briefs (voc), or channel drafts (content-*).
metadata:
  engram:
    schema_version: "1"
    id: positioning
    title: Positioning intelligence & brand sentiment
    lane: marketing
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        A living positioning document; single source of truth for downstream GTM flows.
      duration_label: "~6 min"
      skill_count: 4
      connectors: [Fathom, Notion]
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
        Compare our claimed positioning "{{claimed_positioning}}" to how the market
        describes us over {{time_window}}. Detect perception accuracy (e.g. love us
        but wrong category), message-market fit gaps, and drift vs prior periods.
        Update the living positioning document with claimed / heard / gap / updates.
    eval:
      id: positioning
      required_substrings: [GTM infrastructure, gap, perception]
      required_artifacts: [positioning_doc, sentiment_table]
---

# Positioning intelligence & brand sentiment

Living positioning from the gap between what you say and what the market hears.

## When to use

- Downstream flows need one positioning source of truth.
- Positive sentiment can still hide a category misperception.

## When not to use

- Competitor hiring/pricing/review moves → `market-signals`.
- Support/NPS/call clustering for PM → `voc`.

## Phase 1 — Gather language

1. Pull market phrases (reviews, social, calls) for the window.
2. Score perception accuracy per `references/perception-accuracy.md`.

## Phase 2 — Update the living doc

1. Privacy review first: redact personal/sensitive data; keep only approved attribution.
2. Message-market fit: claimed phrase vs heard phrase (Fathom + Notion + memory; state gap if CRM unavailable).
3. Drift vs prior periods — catch trend before crisis.
4. Emit **positioning_doc** + **sentiment_table**.

## Constraints

- Prefer customer quotes over paraphrase.
- Privacy: redact personal/sensitive data; keep only approved or consented attribution before persisting into positioning_doc or sentiment_table.
- Emit structured gap analysis, not a mood score alone.
