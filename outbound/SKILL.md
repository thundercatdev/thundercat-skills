---
name: outbound
description: >-
  Research a prospect wedge and draft a multi-touch sequence that cites the
  qualifying signal and real customer language. Use when a lead is already
  qualified and needs tailored touches. Do not use to find new ICP leads
  (use icp-*), write social content (content-*), or prepare a live call brief
  (pre-call).
metadata:
  engram:
    schema_version: "1"
    id: outbound
    title: Outbound sequence personalization
    lane: sales
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Outbound that reflects real prospect pain; each sequence cites the qualifying signal.
      duration_label: "~5 min"
      skill_count: 4
      connectors: [CRM, Apollo, LinkedIn Sales Nav, Amplemarket, Outreach]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: prospect_name
          label: Prospect or account
          type: text
          required: true
        - key: qualifying_signal
          label: Qualifying signal
          type: text
          required: true
        - key: sequence_length
          label: Touches
          type: select
          default: 4
          options:
            - value: 3
              label: 3 touches
            - value: 4
              label: 4 touches
            - value: 5
              label: 5 touches
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
    outputs:
      artifacts:
        - id: research_wedge
          type: markdown_sections
          sections: [wedge, evidence]
          required: true
        - id: sequence
          type: markdown_sections
          sections: [touches]
          required: true
        - id: hooks
          type: structured_results
          title: Hook variants
          required: true
    prompt:
      template: >-
        Personalize an outbound sequence for {{prospect_name}} based on signal:
        "{{qualifying_signal}}". Find the wedge with evidence, draft {{sequence_length}}
        touches each with a new angle (wedge → proof → reframe), ground copy in how
        our customers describe the problem, and list labeled hook variants as competing
        theories of what they care about.
    eval:
      id: outbound
      required_substrings: [Jordan Lee, marketing roles, wedge]
      required_artifacts: [research_wedge, sequence, hooks]
---

# Outbound sequence personalization

Signal-grounded sequences — not template sprays.

## When to use

- A lead already has a qualifying signal and needs a tailored multi-touch path.
- You want A/B hooks as competing theories of care.

## When not to use

- Finding / scoring new leads → `icp-*`.
- Walking into a scheduled call → `pre-call`.

## Phase 1 — Wedge research

1. One-paragraph wedge + evidence tied to the qualifying signal.
2. Emit **research_wedge**.

## Phase 2 — Sequence & hooks

1. Draft touches per `references/sequence-quality.md`.
2. Extract customer language from brand memory / proof library.
3. Emit **sequence** + labeled **hooks**.

## Constraints

- Every touch advances or reframes the qualifying signal.
- No progressive desperation ("just bumping") copy.
