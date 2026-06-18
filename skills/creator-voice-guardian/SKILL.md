---
name: creator-voice-guardian
description: 保护创作者个人声音、去 AI 味、事实边界和发布前 final gate。Use when revising AI-written or AI-assisted drafts before publication, especially when the user says 去AI味, AI味, 不像我, 声音守门, final gate, 发布前检查, 商业合作稿审核, 事实校对, 防幻觉, or asks to make a draft less generic, less over-polished, more human, more grounded, and more faithful to source materials.
---

# Creator Voice Guardian

Use this skill after logic and evidence checks, before final polishing or publication. Treat it as a final gate, not a decoration pass.

## Core Principle

Do not make text merely smoother. Return the draft to a concrete person, concrete material, clear evidence, and a responsible publishing voice.

AI may mark risks, explain why a sentence feels wrong, and offer replacement options. The human keeps final judgment over angle, facts, relationship boundaries, public口径, and whether to publish.

## Required Inputs

Ask for missing inputs only when they affect risk. Otherwise proceed and mark uncertainty.

- Current draft.
- Source materials, notes, transcript, brief, or links, if available.
- Publishing account or speaker voice.
- Reader and platform.
- The user's main worry: `事实错误`, `太像 AI`, `太宣传`, `不像我`, `边界不清`, or `商业合作口径`.

If source materials are absent, state clearly that factual calibration is limited and perform voice-level review only.

## Workflow

1. Read the draft once as a reader. Identify the promised topic, speaker position, and likely publication context.
2. Run the fact and boundary gate:
   - Extract factual claims: time, place, names, titles, institutions,合作关系, numbers, event details, quotes, links, and calls to action.
   - Mark each claim as `已支撑`, `弱支撑`, `待确认`, or `无支撑`.
   - Mark private, sensitive, or internal information that may not belong in public copy.
3. Run the voice gate:
   - Mark sentences that are generic, slogan-like, over-complete, over-smooth, promotional, or structurally repetitive.
   - Explain why each marked line feels unstable.
   - Replace only what needs replacing; preserve useful structure and real information.
4. Run the reader gate:
   - Remove backstage editor language the reader does not need.
   - Check whether the draft repeats the same opening, sentence pattern, or explanation too many times.
   - Check whether the text says what the reader already knows too solemnly.
5. Return a compact review first. Do not rewrite the whole piece unless the user asks.

## Load References

- Read `references/ai-tone-patterns.md` when the task is mainly about `AI味`, `不像我`, voice, phrasing, or repeated structure.
- Read `references/final-gate-checklist.md` when the task involves publication, commercial content, event articles, facts, evidence, public boundaries, or final review.
- For a full final gate, use both references.

## Output Contract

Use these sections:

1. `必须改`
   - factual errors, unsupported claims, public-boundary risks, or lines that seriously harm voice.
2. `AI 味在哪里`
   - quote short phrases or sentence fragments; explain the pattern, not only the word choice.
3. `更像人的改法`
   - give direct replacement options. Prefer specific, restrained, source-aware wording.
4. `待确认`
   - list facts, names, links, titles, permissions, or strategic口径 that need human confirmation.

When the user sends a phrase with `AI味：...`, extract the reusable pattern:

- `问题句`
- `为什么像 AI`
- `下次避免的规则`
- `更稳的写法`

## Voice Rules

- Concrete beats grand.
- Evidence beats fluency.
- Field texture beats abstract summary.
- Specific reader questions beat universal claims.
- Cautious judgment beats over-complete conclusions.
- Human hesitation may be kept when it carries meaning.
- Do not turn living people into concepts.
- Do not outsource taste, relationship boundaries, or publication responsibility to AI.

## Common Repairs

- Replace grand openings with a concrete scene, task, reader question, or factual entry.
- Replace `不是 A，而是 B` structures with direct statements when contrast is unnecessary.
- Replace vague claims like `值得关注`, `具有重要意义`, `真实场景`, and `长期价值` with the actual thing that changed.
- Remove empty bridge sentences that only announce the next paragraph.
- Break repeated formats across consecutive sections.
- Keep useful plain language; do not polish every line into the same rhythm.
