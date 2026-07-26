---
name: launch
description: >-
  Coordinate a product/feature launch narrative across channels, draft
  voice-calibrated primary-channel assets, refresh competitive reframe, and
  define post-launch success beyond vanity views. Use for multi-function
  launches. Do not use for steady-state LinkedIn/X posting (content-*), sole
  competitor monitoring (market-signals), or VoC clustering (voc).
metadata:
  engram:
    schema_version: "1"
    id: launch
    title: Product launch GTM orchestration
    lane: sales
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Coordinated launches; post-launch tracking closes the loop on what worked.
      duration_label: "~8 min"
      skill_count: 4
      connectors: [Slack, Notion, Linear]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: launch_name
          label: Launch / feature name
          type: text
          required: true
        - key: launch_date
          label: Launch date
          type: text
          required: false
          default: "TBD"
        - key: primary_channel
          label: Primary channel
          type: select
          default: linkedin
          options:
            - value: linkedin
              label: LinkedIn
            - value: x
              label: X
            - value: blog
              label: Blog
            - value: email
              label: Email
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
        - id: notion
          kind: connector
          label: Notion
          required: false
        - id: linear
          kind: connector
          label: Linear
          required: false
    outputs:
      artifacts:
        - id: launch_plan
          type: markdown_sections
          sections: [narrative, channel_plan, owners]
          required: true
        - id: launch_drafts
          type: engram_content
          content_type: social_media_posts
          required: false
          required_when:
            config_key: primary_channel
            in: [linkedin, x]
        - id: launch_longform
          type: markdown_sections
          sections: [title, body]
          required: false
          required_when:
            config_key: primary_channel
            in: [blog, email]
        - id: battle_card
          type: markdown_sections
          sections: [claim_ground, competitor_reframe]
          required: true
      exactly_one_of: [[launch_drafts, launch_longform]]
    prompt:
      template: >-
        Orchestrate GTM for launch "{{launch_name}}" (target: {{launch_date}}).
        Align one narrative across functions with owners; draft {{primary_channel}}
        assets in brand voice (rewrite per channel — blog ≠ tweet). For linkedin/x
        emit launch_drafts as social_media_posts; for blog/email emit launch_longform
        as markdown_sections. Refresh claim ground vs competitor narratives; define
        post-launch success as sales mentions + customer usage, not vanity views.
    eval:
      id: launch
      required_substrings: [Workspace memory sync, narrative, channel]
      required_artifacts: [launch_plan, battle_card]
      channel_required_artifacts:
        linkedin: [launch_drafts]
        x: [launch_drafts]
        blog: [launch_longform]
        email: [launch_longform]
---

# Product launch GTM orchestration

Narrative consistency under pressure — then prove the launch worked.

## When to use

- Multi-function launches needing one narrative and channel-specific drafts.
- Post-launch: sales mentions + customer usage beat blog views.

## When not to use

- Ongoing LinkedIn/X content engine → `content-linkedin` / `content-x`.
- Competitor signal triage without a launch → `market-signals`.

## Phase 1 — Coordinate

1. Lock narrative, channel plan, and owners.
2. Emit **launch_plan**.

## Phase 2 — Assets & reframe

1. Voice-calibrated primary-channel drafts (channel-native rewrite):
   - `linkedin` / `x` → emit **launch_drafts** via `<engram_content type="social_media_posts" />`.
   - `blog` / `email` → emit **launch_longform** (title + body markdown); do not force social_media_posts.
2. Battle card: claim ground + competitor reframe.
3. Define success metrics (sales language + adoption).
4. Emit the channel-matched draft artifact + **battle_card**.

## Constraints

- Blog post ≠ tweet with different length; rewrite per channel.
- Match artifact type to `primary_channel` — social keeps LinkedIn/X export cards; longform stays markdown.
- Emit exactly one channel draft artifact: `launch_drafts` (linkedin/x) or `launch_longform` (blog/email) — never both, never neither.
