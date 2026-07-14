---
name: icp-linkedin
description: >-
  Qualified LinkedIn leads with firmographic fit scores and peer-style hooks; treat hiring spikes as leading indicators.
metadata:
  engram:
    schema_version: "1"
    id: icp-linkedin
    title: ICP signal discovery — professional networks
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Qualified LinkedIn leads with context-rich hooks; hiring patterns surfaced as a leading indicator.
      duration_label: "~5 min"
      skill_count: 4
      connectors: [LinkedIn, Sales Navigator, CRM, Apollo]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: icp_description
          label: ICP description
          type: text
          required: true
        - key: signal_focus
          label: Signal focus
          type: select
          default: hiring
          options:
            - value: hiring
              label: Hiring patterns
            - value: posts
              label: Buyer posts
            - value: mixed
              label: Hiring + posts
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
        - id: lead_table
          type: structured_results
          title: Qualified LinkedIn leads
          required: true
        - id: hooks
          type: markdown_sections
          sections: [hooks, fit_rationale]
          required: true
    prompt:
      template: >-
        Find {{icp_description}} accounts on LinkedIn over {{time_window}} focusing on {{signal_focus}}. Score firmographic fit with a reason, dedupe against CRM, and draft peer-style hooks that map the signal to the likely internal problem.
    eval:
      id: icp_linkedin
      required_substrings: ["lead", "fit", "hook"]
      required_artifacts: ["lead_table", "hooks"]
---

# ICP signal discovery — professional networks

LinkedIn and Sales Nav signals with hiring as a leading indicator.

## When to use

- You need B2B leads before they start vendor evaluation.
- Job postings (e.g. 3 marketing roles in 2 weeks) signal expensive context-transfer pain.

## Phase 1 — Scan & score

1. Platform scanner (LinkedIn mode): job posts, buyer language, org moves.
2. Firmographic fit scorer: composite score **plus** the specific reason.

## Phase 2 — Dedupe & hook

1. CRM deduplicator: suppress vs escalate.
2. Hook generator (professional mode): peer observation, not a pitch.
3. Emit lead table + hooks.

## Constraints

- Output reasons, not just scores.
- Hooks must feel like a peer observation.
