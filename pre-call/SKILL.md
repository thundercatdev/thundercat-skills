---
name: pre-call
description: >-
  Build a pre-call brief with relationship narrative, last-48h context,
  stakeholder map, and a concrete play — so nobody walks in cold. Use before
  discovery, demos, or exec joins. Do not use for multi-touch outbound
  (outbound), full pipeline ranking (pipeline), or sales→CS handoff
  (onboarding-bridge).
metadata:
  engram:
    schema_version: "1"
    id: pre-call
    title: Pre-call intelligence brief
    lane: sales
    status: live
    version: 1.1.1
    author: engram
    catalog:
      outcome: >-
        Structured brief with relationship history, recent context, and the play.
      duration_label: "~3 min"
      skill_count: 3
      connectors: [Fathom, Gmail]
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
          default: "discovery"
        - key: account_notes
          label: Account notes (optional fallback)
          type: text
          required: false
          default: ""
          placeholder: "Paste CRM history when CRM is not connected"
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
        Build a pre-call brief for {{account_or_contact}} (purpose: {{call_purpose}}).
        Use enabled tools plus account notes: "{{account_notes}}". Synthesize
        relationship narrative (not a CRM dump), last-48h news/activity, stakeholder
        map for the internal sell path, and a concrete play with risks if the champion
        cannot sell internally. Fail closed: when Fathom, Gmail, memory, web, and
        account_notes yield no evidence for a section (relationship, recent activity,
        stakeholders, champion/play), mark that section "unknown/not found" — do not
        invent CRM history or stakeholder maps.
    eval:
      id: pre_call
      required_substrings: [Northwind Labs, relationship, recent, stakeholder, play, champion]
      required_artifacts: [pre_call_brief]
---

# Pre-call intelligence brief

Nobody walks in cold — narrative, not a data dump.

## When to use

- Discovery, demos, or executive joins where recent context wins trust.
- You need the internal sell path, not just champion enthusiasm.

## When not to use

- Multi-touch email/LinkedIn sequence → `outbound`.
- Weekly deal ranking → `pipeline`.
- Post-close sales→CS handoff → `onboarding-bridge`.

## Phases

1. Synthesize relationship narrative from memory / Fathom / Gmail / `account_notes` (and web research).
   If sources are empty, mark relationship as unknown/not found — do not invent CRM history.
2. Scan last-48h news and activity (prefer freshness); mark unknown when nothing found.
3. Map stakeholders who must be sold internally; mark unknown when evidence is missing.
4. Emit **pre_call_brief** with the play and landmines (or unknown/not found per section).

## Constraints

- Narrative + play over bullet CRM dumps.
- Fail closed: never fabricate relationship, recent activity, stakeholders, or champion play.
- Flag risk if champion cannot sell internally.
