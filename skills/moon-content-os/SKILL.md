---
name: moon-content-os
description: 写稿前材料整理助手。Use when the user needs to write a piece of content and has background materials such as briefs, meeting notes, transcripts, old drafts, links, screenshots, partner requirements, audience notes, or reference styles, and needs help combining them into a writing plan before drafting. Supports WeChat articles, event articles, recaps, interview articles, short posts, presentation outlines, portfolio cases, commercial collaboration drafts, internal docs, and content repurposing. Also use for 背景材料组合, 写稿前整理材料, 稿件材料组合, 有一篇稿子要写, 内容产出方式, Moon Content OS, 内容工作台.
---

# Draft Material Builder / Moon Content OS

Use this skill before drafting. Help the user combine writing materials into a usable writing plan: communication task, audience, available evidence, material placement, missing material, output format, and next instruction.

Do not start by building a workbench. Do not immediately write the draft unless the user explicitly asks to skip planning.

## Core Promise

Turn a writing task plus scattered materials into a clear draft plan.

The first output should answer: what is this piece trying to do, which materials matter, where they fit, what is missing, and what instruction should start drafting.

Do not promise viral growth, automation, or one-click publishing. The value is clarity, continuity, judgment, and asset recovery.

The first session should feel usable in 5-10 minutes: organize materials well enough that drafting becomes possible.

## Required Inputs

Ask for or infer:

- Desired output: WeChat article, event article, recap, interview article, short post, presentation outline, portfolio case, commercial draft, internal doc, or uncertain.
- Communication task: invite, explain, recap, persuade, document, showcase, teach, align, or convert.
- Audience: public readers, community members, event attendees, partner/editor/client, hiring reviewer, internal team, or uncertain.
- Writing materials: briefs, meeting notes, transcripts, old drafts, links, screenshots, references, partner requirements, facts, images, quotes.
- Must-keep and must-avoid information: names, facts, partner口径, privacy, unconfirmed details, commercial boundaries.
- User role: creator, researcher, community operator, educator, founder, freelancer, or small team.
- Voice or style requirement: platform style, creator voice, partner tone, enthusiastic, restrained, professional, field-based, or uncertain.
- Available tool surface: local folders, GitHub, Notion, Feishu, Markdown, Codex, Claude Code, or another AI workspace.

If the user only gives raw materials but no output goal, first ask what they are trying to produce.
If the output goal is clear and a narrower skill is more appropriate, route to it after building the draft plan.

## Workflow

1. Name the real writing task.
   - Do not stop at format labels like article, post, or deck.
   - State what the piece must accomplish for the reader or stakeholder.
2. Build a material inventory.
   - List each material, where it can be used, what it supports, whether it needs fact-checking, and whether it should be excluded.
3. Propose material placement.
   - Suggest what belongs in the opening, body, evidence/examples, transition, ending, call to action, or appendix.
   - Mark what should be left out.
4. Check output format fit.
   - If the user specified a format, say whether it fits the available materials.
   - If uncertain, recommend WeChat article, short post, deck, portfolio case, internal doc, or gap-filling.
5. Name missing material.
   - List at most 5 questions that affect drafting.
   - If enough material exists, say drafting can begin.
6. Give one next instruction.
   - Make it copyable.
   - The instruction should begin drafting, fill material gaps, fact-check, confirm boundaries, or route to a narrower skill.
7. Create the minimum workbench only if useful.
   - Use the folders and templates in `references/lite-workbench-templates.md`.
   - Only do this if the same content workflow will repeat.
   - Do not output folders if the user only needs one draft.
8. Add the intake protocol.
   - Define how new notes, transcripts, feedback, drafts, screenshots, and project files enter.
   - Give the user short intent tags such as `入库`, `参考拆解`, `产品化`, `验证`, `发布`, `复盘`.
9. Add content judgment.
   - Decide whether each material should become a source card, topic, draft, public post, portfolio case, product signal, or archive item.
10. Add human-AI boundaries.
   - Use `$human-ai-collaboration-boundary` before any high-risk content work.
   - Use `$creator-voice-guardian` before publication.
11. Add publishing and recovery.
   - Create a publishing queue.
   - Create a feedback recovery habit for comments, private messages, referrals, saved posts, and collaboration leads.
12. Add productization recovery.
   - After projects or repeated tasks, decide whether the work becomes a case, method, skill, template, workshop, offer, or product line.

## Output Contract

Return:

1. `这篇稿的真实任务`
   - one plain sentence.
2. `材料使用清单`
   - material, where to use it, what it supports, check needed, exclude or not.
3. `文章组合方式`
   - opening, body, evidence, ending, and what to leave out.
4. `适合的产出形态`
   - fit check for the requested format or a recommendation.
5. `下一步指令`
   - draft, fill gaps, fact-check, boundary check, or route to a narrower skill.

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
For a first draft-planning run, do not output this full structure unless the user asks to build a recurring workbench. Introduce it as an upgrade path only after repeated similar drafting tasks.

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
- Did the output make it easier to write one piece immediately?
- Did it combine audience, purpose, materials, format, and boundaries?
- Did the output avoid abstract terms such as OS, content asset, middle platform, methodology, or productization unless the user already uses them?
- Can the user know where to put a new material today?
- Can the user see which item to act on next?
- Are privacy, consent, and publication boundaries visible?
- Does every output have a recovery path?
- Is the first version small enough to actually use?
