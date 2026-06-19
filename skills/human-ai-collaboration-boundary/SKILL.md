---
name: human-ai-collaboration-boundary
description: 在内容创作、活动报道、人物稿、商业合作稿、作品集、演讲或公开发布前，先划清 AI 可代劳的劳动、人必须保留的判断、事实证据、授权隐私和关系边界。Use when the user asks 人机协作边界, Human in the loop, Humanity in the loop, AI 协作原则, 内容判断, 先不要写正文, 边界卡, 使用 AI 前先判断, or needs a boundary card before drafting, editing, publishing, or packaging content.
---

# Human AI Collaboration Boundary

Use this skill before writing or revising content with AI. The goal is to prevent AI from taking over judgment, voice, relationship boundaries, or publication responsibility.

## Core Principle

AI is the second workbench. It may organize, compare, extract, suggest, and mark risks. The human decides angle, public boundary, relationship responsibility, final voice, and whether to publish.

## Required Inputs

Ask for or infer:

- content task
- raw materials
- publishing or use scenario
- reader
- publishing account or speaker
- biggest risks: fact, voice, public boundary, authorization, relationship, commercial口径

Do not draft the article first. Produce a boundary card first.

## Workflow

1. Name the task.
   - What is being made: event article, recap, profile, portfolio page, talk deck, commercial copy, internal note, or asset card?
2. Map materials.
   - What is supplied?
   - What is missing?
   - Which parts are public, private, or unclear?
3. Separate AI labor from human judgment.
   - AI labor: organize, extract, summarize, compare, generate options, mark risk, check consistency.
   - Human judgment: angle, relationship, consent, public口径, final voice, publishing decision.
4. Mark risk gates.
   - facts
   - evidence
   - privacy
   - authorization
   - partner or client口径
   - AI voice drift
5. Recommend next action.
   - continue drafting
   - ask for missing materials
   - do public research
   - confirm boundary with stakeholder
   - keep as internal material

## Load References

- Read `references/boundary-card-template.md` whenever outputting a boundary card.
- Read `references/risk-signals.md` for commercial, event, profile, education, minors, client, or sensitive public content.

## Output Contract

Use these sections:

1. `这次任务是什么`
2. `AI 可以帮你省哪些力`
3. `必须由人判断的部分`
4. `不能直接公开的信息`
5. `需要校对的事实`
6. `容易出现 AI 味的地方`
7. `下一步建议`

End with one of:

- `可以进入写作`
- `先补材料`
- `先确认边界`
- `先做调研`
- `暂不公开`

## Rules

- Do not hide uncertainty.
- Do not turn private context into public copy.
- Do not overstate a partner, person, event, or product beyond supplied material.
- Do not make every draft sound like a strategic announcement.
- Preserve the publishing subject's voice.
- Send final drafts through `$creator-voice-guardian` before publication.
