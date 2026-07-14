---
name: icp-developer
description: >-
  Find teams on HN, GitHub, and Product Hunt showing GTM pain before they appear on LinkedIn.
metadata:
  engram:
    schema_version: "1"
    id: icp-developer
    title: ICP signal discovery — developer communities
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Qualified leads from HN, GitHub, and Product Hunt — identified before they show up on LinkedIn.
      duration_label: "~5 min"
      skill_count: 3
      connectors: [HN, GitHub, Product Hunt, CRM, Apollo]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: icp_description
          label: ICP / product niche
          type: text
          required: true
        - key: communities
          label: Communities
          type: text
          required: false
          placeholder: "HN, GitHub, Product Hunt"
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
          title: Developer-community leads
          required: true
        - id: hooks
          type: markdown_sections
          sections: [hooks]
          required: true
    prompt:
      template: >-
        Scan {{communities}} over {{time_window}} for {{icp_description}} teams with GTM readiness gaps. Detect technical-founder GTM pain language and draft hooks that show you understand what they built.
    eval:
      id: icp_developer
      required_substrings: ["lead", "hook", "GTM"]
      required_artifacts: ["lead_table", "hooks"]
---

# ICP signal discovery — developer communities

HN, GitHub, Product Hunt — GTM readiness before LinkedIn visibility.

## When to use

- Technical founders build in public before they hire GTM.
- Show HN / PH traction without conversion often means product-market fit without go-to-market fit.

## Phases

1. Platform scanner (technical mode).
2. Intent detector (technical): GTM pain phrased as "great at building, bad at telling people."
3. Hook generator (technical): demonstrate you understand what they built.
4. Emit lead table + hooks.

## Constraints

- No generic SaaS pitches; reference the artifact (repo, Show HN, PH launch).
