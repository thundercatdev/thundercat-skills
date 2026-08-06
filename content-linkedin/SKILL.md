---
name: content-linkedin
description: >-
  Produce a LinkedIn strategy brief, voice-calibrated draft, and threads to join
  early — grounded in live market conversation and brand memory. Use for weekly
  attributable posting. Do not use for X/Twitter voice (use content-x), ICP lead
  hunting (use icp-*), or competitor signal triage alone (use market-signals).
metadata:
  engram:
    schema_version: "1"
    id: content-linkedin
    title: Content engine — LinkedIn
    lane: marketing
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Each GTM teammate posting in their own voice; content grounded in what the market is discussing.
      duration_label: "~5 min"
      skill_count: 5
      connectors: [Slack, Fathom]
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
          default: "Founder / AE"
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
        # Always required on every run — never skip / never "when applicable".
        - id: social_draft
          type: engram_content
          content_type: social_media_posts
          required: true
        - id: conversation_targets
          type: structured_results
          title: Threads to join
          required: true
    prompt:
      template: >-
        Build a LinkedIn brief for "{{topic_or_angle}}" (author role: {{author_role}})
        using {{time_window}} market talk. Include positioning angle, proof points, CTA;
        draft in my LinkedIn voice and always emit social_draft; list high-signal threads
        to join early; note metrics beyond impressions (profile-view→DM, inbound-attributed calls).
    eval:
      id: content_linkedin
      required_substrings: [context loss, brief, draft]
      required_artifacts: [content_brief, social_draft, conversation_targets]
---

# Content engine — LinkedIn

Voice-calibrated LinkedIn content grounded in live market conversation.

## When to use

- Weekly posting with attributable inbound — not filling a content calendar.
- You need a decision brief: what the market is talking about that you have a right to speak on.

## When not to use

- Punchier reply-first X presence → `content-x`.
- Competitor noise → prioritized signals → `market-signals` (or the composite).
- Lead/hook generation from communities → `icp-*`.

## Phase 1 — Brief

1. Summarize the market conversation on the topic in the time window.
2. Choose an angle with proof points and CTA the author role can own.
3. Emit **content_brief** (market_conversation, angle, proof_points, cta).

## Phase 2 — Draft & conversations

1. Draft in brand voice from memory / past edits — reader should guess the author.
2. Find early, high-quality ICP threads; emit **conversation_targets**.
3. Always emit **social_draft** via `<engram_content type="social_media_posts" />` (required export).
4. Note performance cues: profile-view→DM and inbound-attributed calls, not impressions.

## Constraints

- No generic LinkedIn-bro cadence; prefer customer/market language.
- Deliver exportable artifacts — not a step recap.
