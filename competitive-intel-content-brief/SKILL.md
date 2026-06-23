---
name: competitive-intel-content-brief
description: >-
  Cut competitor noise to prioritized signals, refresh the battle card reframe,
  then produce a voice-calibrated content brief and channel draft.
metadata:
  engram:
    schema_version: "1"
    id: competitive-intel-content-brief
    title: Competitive intel → content brief
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: Prioritized competitor signals plus a voice-calibrated content brief and draft post.
      duration_label: "~3 min"
      skill_count: 5
      connectors: [LinkedIn, X, G2, Notion, Memory]
      composite_of: [market-signals, content-linkedin]
    activation:
      default_enabled: true
      requires_brand: true
    config:
      fields:
        - key: competitor_name
          label: Competitor name
          type: text
          required: true
        - key: content_channel
          label: Content channel
          type: select
          default: linkedin
          options:
            - value: linkedin
              label: LinkedIn
            - value: x
              label: X
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
        - id: signal_table
          type: structured_results
          title: Prioritized market signals
          required: true
        - id: content_brief
          type: markdown_sections
          sections: [positioning, angle, proof_points, cta]
          required: true
        - id: social_draft
          type: engram_content
          content_type: social_media_posts
          required: true
    prompt:
      template: >-
        Competitor {{competitor_name}} had moves this week — cut the noise to 3–5 actionable signals,
        update the battle card reframe, then give me a content brief and {{content_channel}} draft in my voice.
    eval:
      id: competitive_intel_content_brief
      required_substrings: [Acme Corp, signal, brief]
      required_artifacts: [signal_table, content_brief, social_draft]
---

# Competitive intel → content brief

Composite GTM workflow: **market-signals** → **content-linkedin**.

## When to use

- A named competitor had visible moves this week and you need actionable signal, not noise.
- You want a battle card reframe plus a voice-calibrated content brief and channel draft in one run.

## Phase 1 — Market signals

1. Scan competitor hiring, pricing, positioning, and review drift in the configured time window.
2. Reduce raw events to **3–5 prioritized signals** with source, implication, recommended action, and priority.
3. Emit a **structured signal table** before narrative summary (see `references/signal-rubric.md`).
4. Optionally run `scripts/prioritize_signals.py` to rank raw signal rows.

## Phase 2 — Content brief

1. Reframe the battle card from the top signal.
2. Draft a content brief with positioning, angle, proof points, and CTA — calibrated to brand memory.
3. Draft the social post for the configured channel; use `<engram_content type="social_media_posts" />` for the draft when applicable.

## Constraints

- Use only tools enabled for this run (see orchestration allowlist).
- Do not recap internal steps; deliver **exportable artifacts**.
- Prefer customer and market language over generic marketing speak.
