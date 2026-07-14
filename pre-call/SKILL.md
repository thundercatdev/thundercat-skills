---
name: pre-call
description: >-
  Relationship narrative, last-48h context, stakeholder map, and the play — so nobody walks into a call cold.
metadata:
  engram:
    schema_version: "1"
    id: pre-call
    title: Pre-call intelligence brief
    lane: sales
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Structured brief with relationship history, recent context, and the play.
      duration_label: "~3 min"
      skill_count: 3
      connectors: [CRM, Fathom, Gmail, Zendesk, LinkedIn, X, Crunchbase]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: account_or_contact
          label: Account or contact
          type: text
          required: true
        - key: call_purpose
          label: Call purpose
          type: text
          required: false
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
        - id: fathom
          kind: connector
          label: Fathom
          required: false
        - id: gmail
          kind: connector
          label: Gmail
          required: false
    outputs:
      artifacts:
        - id: pre_call_brief
          type: markdown_sections
          sections: [relationship, recent_context, stakeholders, the_play]
          required: true
    prompt:
      template: >-
        Build a pre-call brief for {{account_or_contact}} (purpose: {{call_purpose}}). Synthesize relationship narrative, last-48h news/activity, stakeholder map, and a concrete play.
    eval:
      id: pre_call
      required_substrings: ["relationship", "play", "stakeholder"]
      required_artifacts: ["pre_call_brief"]
---

# Pre-call intelligence brief

Nobody walks in cold — narrative, not a data dump.

## When to use

- Discovery, demos, or executives joins where recent context wins trust.
- You need the internal sell path, not just the champion's enthusiasm.

## Phases

1. Pre-call brief generator — synthesised story.
2. News & activity scanner — last 48 hours preferred.
3. Stakeholder mapper — who must be sold internally.

## Constraints

- Prefer a narrative with the play over bullet CRM dumps.
- Note risk if champion cannot sell internally.
