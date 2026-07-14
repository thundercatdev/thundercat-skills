---
name: icp-community
description: >-
  Surface qualified leads from community and review channels (Facebook Groups,
  Reddit, Google Business, Yelp) with hooks that cite the exact post or review.
  Use when competitors ignore non-LinkedIn intent. Do not use for LinkedIn/hiring
  signals (icp-linkedin), developer communities (icp-developer), or writing
  outbound sequences (outbound).
metadata:
  engram:
    schema_version: "1"
    id: icp-community
    title: ICP signal discovery — community & social
    lane: marketing
    status: live
    version: 1.1.0
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
        Find qualified "{{icp_description}}" leads in community/social channels
        ({{channels}}) over {{time_window}}. Prefer purchase-intent language over
        chatter; verify businesses; dedupe against known pipeline; write a hook that
        references the exact post or review that surfaced each lead.
    eval:
      id: icp_community
      required_substrings: [mid-market ops, hook, intent]
      required_artifacts: [lead_table, hooks]
---

# ICP signal discovery — community & social

Scan community and review channels for purchase-intent language your ICP actually uses.

## When to use

- Leads from Facebook Groups, Reddit, Google Business, or Yelp before they hit LinkedIn.
- Hooks must cite the exact post, review, or complaint.

## When not to use

- Professional network / hiring spikes → `icp-linkedin`.
- HN / GitHub / Product Hunt → `icp-developer`.
- Multi-touch sequence from an already-qualified signal → `outbound`.

## Phase 1 — Scan & detect intent

1. Scan configured channels; separate chatter from purchase-intent language.
2. Weight intent by recency × specificity × urgency.
3. Business-verify with growth proxies when useful (e.g. review count/rating bands).

## Phase 2 — Qualify & hook

1. Suppress known CRM contacts; escalate multi-channel reappearances.
2. Draft hooks per `references/hook-quality.md`.
3. Emit **lead_table** + **hooks**.

## Constraints

- Prefer specific pain language over generic "anyone know a tool" noise.
- Deliver exportable artifacts — not a step recap.
