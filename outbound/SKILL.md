---
name: outbound
description: >-
  Research a prospect wedge, draft a multi-touch sequence that references the qualifying signal, and reuse real customer language.
metadata:
  engram:
    schema_version: "1"
    id: outbound
    title: Outbound sequence personalization
    lane: sales
    status: live
    version: 1.0.0
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
          required: false
    prompt:
      template: >-
        Personalize an outbound sequence for {{prospect_name}} based on signal: {{qualifying_signal}}. Find the wedge, draft {{sequence_length}} touches with new angles each time, and ground language in how our customers actually describe the problem.
    eval:
      id: outbound
      required_substrings: ["wedge", "sequence", "touch"]
      required_artifacts: ["research_wedge", "sequence", "hooks"]
---

# Outbound sequence personalization

Signal-grounded sequences — not template sprays.

## When to use

- A lead already has a qualifying signal and needs a tailored multi-touch path.
- You want A/B hooks as competing theories of what they care about.

## Phases

1. Prospect researcher → one paragraph wedge + evidence.
2. Sequence drafter → each touch a new angle (wedge → proof → reframe).
3. Hook generator (outbound mode).
4. Customer language extractor — recycle real words.

## Constraints

- Every touch must reference or advance the qualifying signal.
- No progressive desperation copy.
