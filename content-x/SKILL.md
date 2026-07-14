---
name: content-x
description: >-
  Find the right X threads, draft punchy voice-calibrated posts and replies, and track follower-quality signal — not vanity impressions.
metadata:
  engram:
    schema_version: "1"
    id: content-x
    title: Content engine — X / Twitter
    lane: marketing
    status: live
    version: 1.0.0
    author: engram
    catalog:
      outcome: >-
        Team presence in the right X conversations — not broadcasting.
      duration_label: "~4 min"
      skill_count: 4
      connectors: [X/Twitter, Slack, X analytics]
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
        For {{topic_or_keywords}} over {{time_window}}, find high-signal X threads and produce {{mode}} drafts in my X voice (punchier than LinkedIn). Skip replies when there is nothing to add.
    eval:
      id: content_x
      required_substrings: ["thread", "draft", "reply"]
      required_artifacts: ["thread_targets", "social_draft"]
---

# Content engine — X / Twitter

Presence in the right conversations — speed and substance over broadcast.

## When to use

- You want replies within the first hour of high-signal threads.
- Same person needs a punchier, more opinionated voice than LinkedIn.

## Phases

1. Thread finder (X).
2. Voice-calibrated drafter (X).
3. Reply drafter with don't-reply mode.
4. Performance: follower quality growth, not impressions.

## Constraints

- If nothing unique to add, surface for awareness — do not draft spam.
