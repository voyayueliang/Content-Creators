# Dialogue WeChat Article Workflow

A reusable Codex skill for turning spoken conversations into publishable WeChat Official Account articles.

It works with:

- livestreams
- podcasts
- interviews
- roundtables
- event replays
- multi-speaker transcripts

This is not a one-shot AI writing prompt. It is a human-AI editorial workflow for conversation-based publishing.

## What It Helps With

The skill helps an editor or creator:

- map source material before drafting
- identify speakers, roles, and publication voice
- decide whether the material should become a dialogue post, summary, essay, video script, or internal asset
- preserve speaker texture and live conversation flow
- produce sectioned WeChat-ready dialogue drafts
- add image placeholder notes for editors
- check visible body length
- review facts, logic, privacy, consent, and tone
- recover reusable content assets after drafting

## Why This Exists

Many AI writing workflows optimize for smoothness.

But conversation-based writing needs more than smoothness. Interviews and livestreams often contain hesitation, unfinished thinking, speaker relationship, and field texture. If AI over-synthesizes everything into a clean argument, the best part of the conversation disappears.

This workflow treats dialogue as a first-class output.

## Core Principles

- Start with a content view before drafting.
- Dialogue can be the final format.
- AI is a second workbench, not a ghostwriter.
- Scene comes before abstract judgment.
- Evidence matters more than fluency.
- Keep useful uncertainty.
- Do not publish without human boundary checks.
- Platform adaptation should not erase the publisher's position.
- Recover reusable assets after each conversation.

## Human-AI Boundaries

AI can:

- organize source material
- propose structure
- draft and revise
- generate title options
- check facts, logic, length, and privacy risks

Humans must decide:

- whether the piece should be published
- what the publishing account's voice should be
- which facts are confirmed
- which quotes can be used
- what needs consent
- what should remain private

## Skill Structure

```text
skills/dialogue-wechat-article-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── content-method-principles.md
    ├── human-ai-boundaries.md
    ├── human-ai-collaboration-loop.md
    ├── operator-workflow.md
    ├── output-template.md
    ├── quality-check.md
    └── voice-account-map.md
```

## Suggested Use

Use this skill when you have a transcript or notes from a spoken conversation and want to turn it into a public article without flattening the dialogue.

Example request:

```text
Use this skill to turn this livestream transcript into a WeChat-ready edited dialogue article.
Keep speaker voices, create 4-5 sections, add image placeholders, and include fact/privacy/length checks.
```

## Safety And Privacy

Do not publish raw transcripts, private chats, client stories, student work, family details, or identifiable images without permission.

When in doubt, anonymize, mark `to confirm`, or keep the material as an internal asset.

## License

No license has been selected yet. Please do not reuse commercially without permission.
