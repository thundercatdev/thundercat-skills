---
name: onboarding-bridge
description: >-
  Build a sales→CS handoff brief with why bought, champions vs daily users,
  success criteria in their language, and landmines. Use at new-logo handoff.
  Do not use for pre-call prep (pre-call), renewal/expansion intelligence
  (renewal), or VoC clustering (voc).
metadata:
  engram:
    schema_version: "1"
    id: onboarding-bridge
    title: Customer onboarding context bridge
    lane: customer_success
    status: live
    version: 1.1.1
    author: engram
    catalog:
      outcome: >-
        Zero context loss at handoff — why bought, who championed, success criteria, landmines.
      duration_label: "~4 min"
      skill_count: 3
      connectors: [Fathom, Gmail, Slack, Notion]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: account_name
          label: Account name
          type: text
          required: true
        - key: close_date
          label: Close date (optional)
          type: text
          required: false
          default: "recently"
        - key: close_notes
          label: Close notes (optional fallback)
          type: text
          required: false
          default: ""
          placeholder: "Paste CRM close notes when CRM is not connected"
    orchestration:
      tools:
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
        - id: notion
          kind: connector
          label: Notion
          required: false
        - id: slack
          kind: connector
          label: Slack
          required: false
    outputs:
      artifacts:
        - id: onboarding_brief
          type: markdown_sections
          sections: [why_bought, stakeholders, success_criteria, landmines]
          required: true
    prompt:
      template: >-
        Build an onboarding handoff brief for {{account_name}} (closed {{close_date}}).
        Consult every enabled source (memory, Fathom, Gmail, Slack, Notion) plus close
        notes if provided: "{{close_notes}}". Capture evidenced why-bought (rational +
        emotional); map stakeholders (sales champion vs daily user); state success
        criteria in their words; list landmines (politics, failed prior tools,
        skeptics). When a field lacks evidence, return unavailable/unknown — do not
        invent daily users, success criteria, or landmines.
    eval:
      id: onboarding_bridge
      required_substrings: [Northwind Labs, why bought, stakeholder, success criteria, landmine]
      required_artifacts: [onboarding_brief]
---

# Customer onboarding context bridge

Zero context loss from sales → CS.

## When to use

- New logo handoff; champion ≠ daily user is common.
- Success criteria stick when stated in customer language.

## When not to use

- Pre-meeting sales brief → `pre-call`.
- Renewal risk / expansion angle → `renewal`.

## Phases

1. Pull why-bought evidence from memory / Fathom / Gmail / Slack / Notion / `close_notes`.
   If sources are empty, mark why_bought unavailable/unknown — do not invent close notes.
2. Map stakeholders: sales champion vs daily users vs blockers (unknown when not evidenced).
3. Extract success criteria in their language; list landmines (or unavailable/unknown).
4. Emit **onboarding_brief**.

## Constraints

- Include landmines explicitly when evidenced; otherwise mark unavailable/unknown.
- Fail closed: never invent daily user, success criteria, or landmine details.
- Keep brief scannable for a CS owner in one sitting.
