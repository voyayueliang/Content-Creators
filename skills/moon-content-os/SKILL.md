---
name: moon-content-os
description: 搭建 AI 时代个人内容工作台，把素材、项目、反馈、AI 协作和发布流程组织成可持续内容资产。Use when the user asks to 搭建内容工作台, Moon Content OS, 内容中台, 素材系统, 内容资产库, 个人内容操作系统, 创作者工作台, 发布队列, 反馈回收, 产品化回收, or wants to turn scattered notes, recordings, projects, conversations, drafts, and audience feedback into a reusable creator operating system.
---

# Moon Content OS

Use this skill to help a creator build a lightweight content workbench through one real pilot task. Do not start by organizing everything the user has.

## Core Promise

Build a system where material can enter, be judged, become publishable work, pass human-AI gates, and return as reusable assets.

Do not promise viral growth, automation, or one-click publishing. The value is clarity, continuity, judgment, and asset recovery.

The first session should feel usable in 10 minutes: pick one material, map it, name the boundary, and decide the next instruction.

## Required Inputs

Ask for or infer:

- One pilot task: a draft, transcript, event material pack, portfolio case, meeting note, published link set, or content folder.
- User role: creator, researcher, community operator, educator, founder, freelancer, or small team.
- Current material sources: chats, notes, recordings, interviews, event documents, drafts, links, screenshots, feedback.
- Current publishing surfaces: WeChat, video, podcast, newsletter, social posts, portfolio, internal docs, workshops.
- Pain point: too much material, no queue, no feedback recovery, AI voice drift, weak portfolio, unclear productization.
- Available tool surface: local folders, GitHub, Notion, Feishu, Markdown, Codex, Claude Code, or another AI workspace.

If the user only wants a single deliverable, route them to a narrower skill before building a full OS.
If the user wants an OS but has not chosen a pilot task, ask them to choose one material first.

## Workflow

1. Choose the pilot material.
   - Use one concrete task before building the wider system.
   - Accept a draft, transcript, event pack, meeting note, portfolio case, content folder, or public link set.
2. Map the pilot material.
   - List what is available, what it can support, what is missing, what is risky, and what needs human confirmation.
   - Separate active, archive, and sensitive material only when needed for the current task.
3. Decide the workflow route.
   - Route to event communication, audio-to-article, profile/case, deck, portfolio, final gate, or archive-only.
   - Explain why in one sentence.
4. Create the minimum workbench.
   - Use the folders and templates in `references/lite-workbench-templates.md`.
   - Keep the first version small enough to use today.
   - Do not output a large OS if the user only needs a few folders for the pilot.
5. Add the intake protocol.
   - Define how new notes, transcripts, feedback, drafts, screenshots, and project files enter.
   - Give the user short intent tags such as `入库`, `参考拆解`, `产品化`, `验证`, `发布`, `复盘`.
6. Add content judgment.
   - Decide whether each material should become a source card, topic, draft, public post, portfolio case, product signal, or archive item.
7. Add human-AI boundaries.
   - Use `$human-ai-collaboration-boundary` before any high-risk content work.
   - Use `$creator-voice-guardian` before publication.
8. Add publishing and recovery.
   - Create a publishing queue.
   - Create a feedback recovery habit for comments, private messages, referrals, saved posts, and collaboration leads.
9. Add productization recovery.
   - After projects or repeated tasks, decide whether the work becomes a case, method, skill, template, workshop, offer, or product line.

## Output Contract

Return:

1. `这份材料适合进入哪条工作流`
   - route and one-sentence reason.
2. `材料地图`
   - available material, possible use, missing evidence, risk/boundary, next action.
3. `这次任务需要的最小文件夹`
   - only 4-6 folders unless the user asks for a full OS.
4. `三张今天就能用的卡片`
   - source card, boundary card, next-step card.
5. `下一条可以继续发给 AI 的指令`
   - write next, fill gaps, verify facts, or ask for human confirmation.

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
For a first run, use only the folders needed by the pilot task. Introduce the full structure as an upgrade path, not the first output.

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

- Did the work start from one real task rather than an abstract complete system?
- Can the user know where to put a new material today?
- Can the user see which item to act on next?
- Are privacy, consent, and publication boundaries visible?
- Does every output have a recovery path?
- Is the first version small enough to actually use?
