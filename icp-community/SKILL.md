---
name: icp-community
description: >-
  Surface qualified leads from community and review channels with context-specific hooks competitors are not watching.
metadata:
  engram:
    schema_version: "1"
    id: icp-community
    title: ICP signal discovery — community & social
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Qualified leads from channels competitors are not watching — delivered with a custom hook per lead.
      duration_label: "~5 min"
      skill_count: 5
      connectors: [Facebook Groups, Reddit, Google Business, Yelp, CRM, Apollo]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: icp_description
          label: ICP description
          type: text
          required: true
        - key: channels
          label: Channels focus
          type: text
          required: false
          placeholder: "e.g. Facebook groups, Reddit, Yelp"
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
        - id: slack
          kind: connector
          label: Slack
          required: false
    outputs:
      artifacts:
        - id: lead_table
          type: structured_results
          title: Qualified community leads
          required: true
        - id: hooks
          type: markdown_sections
          sections: [hooks, rationale]
          required: true
    prompt:
      template: >-
        Find qualified {{icp_description}} leads in community/social channels ({{channels}}) over {{time_window}}. Deduplicate against known pipeline, verify businesses, and write a hook that references the exact post or review that surfaced each lead.
    eval:
      id: icp_community
      required_substrings: ["lead", "hook", "intent"]
      required_artifacts: ["lead_table", "hooks"]
---

# ICP signal discovery — community & social

Scan community and review channels for purchase-intent language your ICP actually uses.

## When to use

- You want leads from Facebook Groups, Reddit, Google Business, or Yelp before they hit LinkedIn.
- Hooks must cite the exact post, review, or complaint that surfaced the lead.

## Phase 1 — Scan & detect intent

1. Platform scanner (community mode): distinguish chatter from purchase-intent language.
2. Intent signal detector: weight recency × specificity × urgency.
3. Business verifier: use review count/rating as growth proxies (e.g. 50–1500 reviews, 4.2+).

## Phase 2 — Qualify & hook

1. CRM deduplicator: suppress known contacts; escalate multi-channel reappearances.
2. Hook generator: every hook references the exact context (post, review, complaint).
3. Emit a **lead table** plus short hook drafts.

## Constraints

- Prefer specific pain language over generic "anyone know a tool" noise.
- Deliver exportable artifacts — not a step recap.
- Use only enabled tools for this run.
