---
name: renewal
description: >-
  Score customer health beyond usage volume, draft a renewal brief with expansion
  angle and churn risks, and check whether the champion is still the champion.
  Use for upcoming renewals. Do not use for new-logo handoff (onboarding-bridge),
  open-pipeline ranking (pipeline), or VoC→messaging loops (voc).
metadata:
  engram:
    schema_version: "1"
    id: renewal
    title: Renewal & expansion intelligence
    lane: customer_success
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        CS walks into every renewal with expansion angle and churn risk identified.
      duration_label: "~5 min"
      skill_count: 3
      connectors: [CRM, Mixpanel, Amplitude, Zendesk, Fathom, NPS/CSAT, Stripe]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: account_name
          label: Account name
          type: text
          required: true
        - key: renewal_date
          label: Renewal date
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
    outputs:
      artifacts:
        - id: health_score
          type: structured_results
          title: Health signals
          required: true
        - id: renewal_brief
          type: markdown_sections
          sections: [delivered, expansion, churn_risks, play]
          required: true
    prompt:
      template: >-
        Prepare renewal intelligence for {{account_name}} (renewal {{renewal_date}}).
        Score health as usage × sentiment/support (not volume alone); answer whether
        we delivered, the expansion angle, and churn risks; check champion succession;
        end with a concrete play for the renewal conversation.
    eval:
      id: renewal
      required_substrings: [Northwind Labs, expansion, churn]
      required_artifacts: [health_score, renewal_brief]
---

# Renewal & expansion intelligence

Active retention — expansion angle and churn risk before the meeting.

## When to use

- Upcoming renewals; "active but unhappy" is the dangerous state.
- Champion left unnoticed is a top preventable churn cause.

## When not to use

- Sales→CS new-logo handoff → `onboarding-bridge`.
- Open sales pipeline ranking → `pipeline`.

## Phases

1. Health score: usage × sentiment/support — flag "active but unhappy".
2. Brief: delivered? expand? churn risks?
3. Champion activity / succession check.
4. Emit **health_score** + **renewal_brief** with the play.

## Constraints

- Answer the three questions explicitly.
- Flag champion succession gaps.
