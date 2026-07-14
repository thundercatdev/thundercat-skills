---
name: launch
description: >-
  Coordinate launch narrative across channels, draft voice-calibrated assets, battle-card reframes, and post-launch success metrics.
metadata:
  engram:
    schema_version: "1"
    id: launch
    title: Product launch GTM orchestration
    lane: sales
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Coordinated launches; post-launch tracking closes the loop on what worked.
      duration_label: "~8 min"
      skill_count: 4
      connectors: [Slack, Notion, GitHub, Linear, CMS, Resend, CRM, Intercom, Mixpanel]
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
          required: true
        - id: battle_card
          type: markdown_sections
          sections: [claim_ground, competitor_reframe]
          required: false
    prompt:
      template: >-
        Orchestrate GTM for launch "{{launch_name}}" (target: {{launch_date}}). Align narrative across functions, draft {{primary_channel}} assets in brand voice, refresh competitive reframe, and define post-launch success (sales mentions + usage — not vanity views).
    eval:
      id: launch
      required_substrings: ["narrative", "launch", "channel"]
      required_artifacts: ["launch_plan", "launch_drafts", "battle_card"]
---

# Product launch GTM orchestration

Narrative consistency under pressure — then prove the launch worked.

## When to use

- Multi-function launches needing one narrative and channel-specific drafts.
- Post-launch: sales mentions + customer usage beat blog views.

## Phases

1. Launch coordinator — owners, narrative, channel plan.
2. Voice-calibrated drafter (launch mode) — channel-native assets.
3. Battle card (launch mode) — claim ground vs competitor narratives.
4. Performance tracker — sales language + adoption signals.

## Constraints

- Blog post ≠ tweet with different length; rewrite per channel.
