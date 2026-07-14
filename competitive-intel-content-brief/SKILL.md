---
name: competitive-intel-content-brief
description: >-
  Cut competitor noise to prioritized signals, refresh the battle-card reframe,
  then produce a voice-calibrated content brief and channel draft. Use when a
  named competitor moved and you need signal + draft in one run. Do not use for
  ICP lead hunting (icp-*), standalone positioning docs (positioning), or X-only
  reply workflows (content-x) without a competitor signal.
metadata:
  engram:
    schema_version: "1"
    id: competitive-intel-content-brief
    title: Competitive intel → content brief
    lane: marketing
    status: live
    version: 1.1.0
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
        Competitor {{competitor_name}} had moves this week — cut the noise to 3–5
        actionable signals (source, implication, action, P1–P3), update the battle
        card reframe, then give me a content brief and {{content_channel}} draft in
        my voice.
    eval:
      id: competitive_intel_content_brief
      required_substrings: [Acme Corp, P1, brief]
      required_artifacts: [signal_table, content_brief, social_draft]
---

# Competitive intel → content brief

Composite GTM workflow: **market-signals** → **content-linkedin**.

## When to use

- A named competitor had visible moves and you need actionable signal plus a draft.
- You want battle-card reframe and a voice-calibrated brief in one run.

## When not to use

- Signals only (no draft) → `market-signals`.
- Draft only (no competitor triage) → `content-linkedin` / `content-x`.
- ICP leads / hooks → `icp-*`.

## Phase 1 — Market signals

1. Scan competitor hiring, pricing, positioning, and review drift in the time window.
2. Reduce to **3–5 prioritized signals** with source, implication, action, priority.
3. Emit **signal_table** before narrative (see `references/signal-rubric.md`).
4. Optionally run `scripts/prioritize_signals.py` to rank raw signal rows.

## Phase 2 — Content brief

1. Reframe the battle card from the top signal.
2. Draft brief: positioning, angle, proof points, CTA — calibrated to brand memory.
3. Draft the social post for the configured channel; use `<engram_content type="social_media_posts" />` when applicable.

## Constraints

- Use only tools enabled for this run.
- Do not recap internal steps; deliver **exportable artifacts**.
- Prefer customer and market language over generic marketing speak.
