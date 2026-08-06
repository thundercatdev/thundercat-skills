---
name: content-x
description: >-
  Find high-signal X threads and draft punchy voice-calibrated posts/replies —
  presence in conversations, not broadcasting. Use for reply-first or short-form
  X. Do not use for LinkedIn tone/length (use content-linkedin), ICP lead tables
  (use icp-*), or long-form launch narratives (use launch).
metadata:
  engram:
    schema_version: "1"
    id: content-x
    title: Content engine — X / Twitter
    lane: marketing
    status: live
    version: 1.1.0
    author: engram
    catalog:
      outcome: >-
        Team presence in the right X conversations — not broadcasting.
      duration_label: "~4 min"
      skill_count: 4
      connectors: [Slack]
    activation:
      default_enabled: false
      requires_brand: true
    config:
      fields:
        - key: topic_or_keywords
          label: Topic or keywords
          type: text
          required: true
        - key: mode
          label: Mode
          type: select
          default: reply
          options:
            - value: reply
              label: Replies
            - value: post
              label: Original post
            - value: both
              label: Post + replies
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
        - id: thread_targets
          type: structured_results
          title: Threads to join
          required: true
        - id: social_draft
          type: engram_content
          content_type: social_media_posts
          required: true
    prompt:
      template: >-
        For "{{topic_or_keywords}}" over {{time_window}}, find high-signal X threads
        and produce {{mode}} drafts in my X voice (punchier and more opinionated than
        LinkedIn). If nothing unique to add, still emit social_draft with an empty
        posts list and a one-line note "awareness only — no reply drafted"; do not
        invent spam replies.
    eval:
      id: content_x
      required_substrings: [GTM agents, thread, draft]
      required_artifacts: [thread_targets, social_draft]
---

# Content engine — X / Twitter

Presence in the right conversations — speed and substance over broadcast.

## When to use

- Replies within the first hour of high-signal threads.
- Same person needs a punchier, more opinionated voice than LinkedIn.

## When not to use

- LinkedIn strategy brief + long draft → `content-linkedin`.
- Launch channel pack across functions → `launch`.

## Phase 1 — Find threads

1. Search topic/keywords in the window; score for ICP relevance and freshness.
2. Emit **thread_targets** with why each is worth joining.

## Phase 2 — Draft

1. Voice-calibrated X drafts per configured mode (reply / post / both).
2. Apply don't-reply: if nothing unique, awareness only — no spam.
3. Always emit **social_draft** (required). For awareness-only runs use empty posts
   plus an explicit "awareness only — no reply drafted" note — never invent replies.
4. Note follower-quality signal over impressions.

## Constraints

- Shorter and sharper than LinkedIn; no LinkedIn-length essays.
- Use only enabled tools; deliver exportable artifacts.
