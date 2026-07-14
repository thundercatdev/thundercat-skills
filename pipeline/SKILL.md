---
name: pipeline
description: >-
  Rank deals by close likelihood using behavioral and champion signals, with a specific next action per deal.
metadata:
  engram:
    schema_version: "1"
    id: pipeline
    title: Pipeline scoring & prioritization
    lane: sales
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Pipeline ranked by likelihood to close; clear next action per deal.
      duration_label: "~5 min"
      skill_count: 4
      connectors: [CRM, Email, Web analytics, LinkedIn, Outreach]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: pipeline_scope
          label: Pipeline scope
          type: text
          required: true
          placeholder: "e.g. late-stage ARR > $20k"
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
    outputs:
      artifacts:
        - id: ranked_pipeline
          type: structured_results
          title: Ranked deals
          required: true
        - id: next_actions
          type: markdown_sections
          sections: [actions]
          required: true
    prompt:
      template: >-
        Score and prioritize {{pipeline_scope}} over {{time_window}}. Weight behavioral signals and champion activity (including silence), explain velocity stalls, and recommend a concrete next action per deal — not "follow up".
    eval:
      id: pipeline
      required_substrings: ["rank", "action", "champion"]
      required_artifacts: ["ranked_pipeline", "next_actions"]
---

# Pipeline scoring & prioritization

Likelihood ranking with social/leading indicators and specific next actions.

## When to use

- Weekly pipeline review needs focus, not a flat stage list.
- Champion silence is a first-class risk signal.

## Phases

1. Behavioral signal scorer (pricing visits ≫ opens).
2. Champion activity tracker — silence matters.
3. Deal velocity analyzer — slow + likely reason.
4. Next action recommender — specific artifact/angle, not "follow up".

## Constraints

- Each deal gets one ranked priority and one concrete action.
