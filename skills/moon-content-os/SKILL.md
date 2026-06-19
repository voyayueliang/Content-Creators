---
name: moon-content-os
description: 搭建 AI 时代个人内容工作台，把素材、项目、反馈、AI 协作和发布流程组织成可持续内容资产。Use when the user asks to 搭建内容工作台, Moon Content OS, 内容中台, 素材系统, 内容资产库, 个人内容操作系统, 创作者工作台, 发布队列, 反馈回收, 产品化回收, or wants to turn scattered notes, recordings, projects, conversations, drafts, and audience feedback into a reusable creator operating system.
---

# Moon Content OS

Use this skill to help a creator build a lightweight content workbench, not to write a single isolated article.

## Core Promise

Build a system where material can enter, be judged, become publishable work, pass human-AI gates, and return as reusable assets.

Do not promise viral growth, automation, or one-click publishing. The value is clarity, continuity, judgment, and asset recovery.

## Required Inputs

Ask for or infer:

- User role: creator, researcher, community operator, educator, founder, freelancer, or small team.
- Current material sources: chats, notes, recordings, interviews, event documents, drafts, links, screenshots, feedback.
- Current publishing surfaces: WeChat, video, podcast, newsletter, social posts, portfolio, internal docs, workshops.
- Pain point: too much material, no queue, no feedback recovery, AI voice drift, weak portfolio, unclear productization.
- Available tool surface: local folders, GitHub, Notion, Feishu, Markdown, Codex, Claude Code, or another AI workspace.

If the user only wants a single deliverable, route them to a narrower skill before building a full OS.

## Workflow

1. Map material sources.
   - List where raw material currently lives.
   - Separate active material, archive material, and sensitive material.
2. Create the minimum workbench.
   - Use the folders and templates in `references/lite-workbench-templates.md`.
   - Keep the first version small enough to use this week.
3. Add the intake protocol.
   - Define how new notes, transcripts, feedback, drafts, screenshots, and project files enter.
   - Give the user short intent tags such as `入库`, `参考拆解`, `产品化`, `验证`, `发布`, `复盘`.
4. Add content judgment.
   - Decide whether each material should become a source card, topic, draft, public post, portfolio case, product signal, or archive item.
5. Add human-AI boundaries.
   - Use `$human-ai-collaboration-boundary` before any high-risk content work.
   - Use `$creator-voice-guardian` before publication.
6. Add publishing and recovery.
   - Create a publishing queue.
   - Create a feedback recovery habit for comments, private messages, referrals, saved posts, and collaboration leads.
7. Add productization recovery.
   - After projects or repeated tasks, decide whether the work becomes a case, method, skill, template, workshop, offer, or product line.

## Output Contract

Return:

1. `最小工作台结构`
   - folder/page structure with names and purpose.
2. `素材进入规则`
   - what the user should drop in, with intent tags.
3. `内容判断规则`
   - how to decide whether to write, archive, publish, or productize.
4. `AI 协作边界`
   - what AI may do, what humans must decide, and what needs final gates.
5. `7 天启动动作`
   - small actions the user can complete without redesigning their whole life.

## Load References

- Read `references/lite-workbench-templates.md` when creating folder structures, template pages, or a first usable workbench.
- Read `references/content-asset-loop.md` when designing publishing, feedback recovery, portfolio recovery, or productization loops.

## Default Shape

Prefer this minimum structure:

```text
00_使用说明
01_素材收件箱
02_内容查看台
03_素材卡
04_选题池
05_发布队列
06_AI协作原则
07_去AI味检查清单
08_事实与边界校对清单
09_发布后反馈回收
10_产品化回收
```

Keep names understandable. The workbench should invite use, not admiration.

## Boundaries

AI can:

- organize material
- build maps and queues
- draft templates
- suggest content forms
- run checks
- recover signals

The human must decide:

- what deserves attention
- what may be public
- whose relationship or privacy is involved
- what voice is acceptable
- which feedback matters
- what becomes a paid offer, case, or public asset

## Quality Gate

Before presenting a workbench, check:

- Can the user know where to put a new material today?
- Can the user see which item to act on next?
- Are privacy, consent, and publication boundaries visible?
- Does every output have a recovery path?
- Is the first version small enough to actually use?
