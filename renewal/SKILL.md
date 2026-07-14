---
name: renewal
description: >-
  Customer health, renewal brief with expansion angle and churn risks, and champion activity including silent succession risk.
metadata:
  engram:
    schema_version: "1"
    id: renewal
    title: Renewal & expansion intelligence
    lane: customer_success
    status: live
    version: 1.0.0
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
        Prepare renewal intelligence for {{account_name}} (renewal {{renewal_date}}). Score health beyond usage volume, answer whether we delivered / expand angle / churn risks, and check whether the champion is still the champion.
    eval:
      id: renewal
      required_substrings: ["health", "expansion", "churn"]
      required_artifacts: ["health_score", "renewal_brief"]
---

# Renewal & expansion intelligence

Active retention — expansion angle and churn risk before the meeting.

## When to use

- Upcoming renewals; "active but unhappy" is the dangerous state.
- Champion left unnoticed is a top preventable churn cause.

## Phases

1. Customer health scorer — usage × sentiment/support, not volume alone.
2. Renewal brief: delivered? expand? churn?
3. Champion activity tracker (renewal mode).

## Constraints

- Answer the three questions explicitly.
- Flag champion succession gaps.
