---
name: content-linkedin
description: >-
  Strategy brief, voice-calibrated LinkedIn draft, conversation targets, and performance notes for consistent team posting.
metadata:
  engram:
    schema_version: "1"
    id: content-linkedin
    title: Content engine — LinkedIn
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Each GTM teammate posting in their own voice; content grounded in what the market is discussing.
      duration_label: "~5 min"
      skill_count: 5
      connectors: [LinkedIn, Slack, Fathom, Granola, Shield]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: topic_or_angle
          label: Topic or angle
          type: text
          required: true
        - key: author_role
          label: Author role
          type: text
          required: false
          placeholder: "e.g. Founder / AE"
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
        - id: fathom
          kind: connector
          label: Fathom
          required: false
    outputs:
      artifacts:
        - id: content_brief
          type: markdown_sections
          sections: [market_conversation, angle, proof_points, cta]
          required: true
        - id: social_draft
          type: engram_content
          content_type: social_media_posts
          required: true
        - id: conversation_targets
          type: structured_results
          title: Threads to join
          required: false
    prompt:
      template: >-
        Build a LinkedIn content brief for {{topic_or_angle}} (author: {{author_role}}) using {{time_window}} market talk. Draft in my voice, suggest high-signal threads to join early, and note what to measure besides impressions.
    eval:
      id: content_linkedin
      required_substrings: ["brief", "draft", "voice"]
      required_artifacts: ["content_brief", "social_draft", "conversation_targets"]
---

# Content engine — LinkedIn

Voice-calibrated LinkedIn content grounded in live market conversation.

## When to use

- Weekly posting with attributable inbound — not a content calendar.
- You need a decision brief: what the market is talking about that you have a right to speak on.

## Phases

1. Strategy brief generator.
2. Voice-calibrated drafter (LinkedIn) using brand memory / past edits.
3. Thread & conversation finder — early on high-quality ICP posts.
4. Performance notes: profile-view→DM and inbound-attributed calls, not impressions.
5. Optional voice recalibrator from edit patterns.

## Constraints

- Reader should guess the author without seeing the name.
- Use `<engram_content type="social_media_posts" />` for the draft when applicable.
