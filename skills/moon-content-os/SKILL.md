---
name: moon-content-os
description: 内容材料分流与工作台启动器。Use when the user has a draft, transcript, event packet, meeting note, portfolio material, published link, or scattered content material and does not know whether to turn it into an article, short post, presentation, portfolio case, source card, archive item, or fact-checking task. Also use for Moon Content OS, 搭建内容工作台, 内容材料分流, 不知道材料怎么用, 不知道该写什么, 素材系统, 内容资产库, 个人内容操作系统, 创作者工作台, 发布队列, 反馈回收, 产品化回收.
---

# Content Material Router / Moon Content OS

Use this skill first as a concrete material router. Help the user decide what one piece of material can become and what the next AI instruction should be.

Only upgrade to a lightweight content workbench after the first material route is useful. Do not start by organizing everything the user has.

## Core Promise

Turn one uncertain material into a clear next step: write, shorten, make a deck, build a portfolio case, create a source card, archive, fill gaps, or fact-check.

The longer-term workbench is an upgrade path, not the first promise.

Do not promise viral growth, automation, or one-click publishing. The value is clarity, continuity, judgment, and asset recovery.

The first session should feel usable in 5-10 minutes: inspect one material, choose a route, name missing information, and give the user one copyable next instruction.

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

1. Read one material.
   - Accept a draft, transcript, event pack, meeting note, portfolio case, content folder, public link set, or pasted fragment.
   - Do not ask for a full archive first.
2. Name what it is.
   - Classify it as transcript, event material, old draft, meeting note, portfolio material, community feedback, fragment, or another plain category.
3. Route it to the next use.
   - Route to long article, short post, presentation, portfolio case, source card, archive, fact-check, or gap-filling.
   - Explain why in ordinary language, using the material itself as evidence.
4. Name the missing inputs.
   - List up to 3 questions that most affect the next step.
   - If enough information exists, say it can start.
5. Give one next instruction.
   - Make it copyable.
   - The instruction should continue to writing, shortening, deck outlining, case distilling, fact-checking, or source-card creation.
6. Create the minimum workbench only if useful.
   - Use the folders and templates in `references/lite-workbench-templates.md`.
   - Keep the first version small enough for this material.
   - Do not output folders if the user only needs routing and a next instruction.
7. Add the intake protocol.
   - Define how new notes, transcripts, feedback, drafts, screenshots, and project files enter.
   - Give the user short intent tags such as `入库`, `参考拆解`, `产品化`, `验证`, `发布`, `复盘`.
8. Add content judgment.
   - Decide whether each material should become a source card, topic, draft, public post, portfolio case, product signal, or archive item.
9. Add human-AI boundaries.
   - Use `$human-ai-collaboration-boundary` before any high-risk content work.
   - Use `$creator-voice-guardian` before publication.
10. Add publishing and recovery.
   - Create a publishing queue.
   - Create a feedback recovery habit for comments, private messages, referrals, saved posts, and collaboration leads.
11. Add productization recovery.
   - After projects or repeated tasks, decide whether the work becomes a case, method, skill, template, workshop, offer, or product line.

## Output Contract

Return:

1. `这份材料现在属于什么`
   - plain category, no jargon.
2. `它最适合走哪条路`
   - long article, short post, presentation, portfolio case, source card, archive, fact-check, or gap-filling.
3. `为什么`
   - ordinary-language reason based on the material.
4. `还缺哪 3 个关键信息`
   - only the highest-impact questions.
5. `下一步可以复制给 AI 的一句话`
   - one clear instruction.

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
For a first run, do not output this full structure unless the user asks to build a workbench. Introduce it as an upgrade path only after routing one real material.

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
- Did the output avoid abstract terms such as OS, content asset, middle platform, methodology, or productization unless the user already uses them?
- Can the user know where to put a new material today?
- Can the user see which item to act on next?
- Are privacy, consent, and publication boundaries visible?
- Does every output have a recovery path?
- Is the first version small enough to actually use?
