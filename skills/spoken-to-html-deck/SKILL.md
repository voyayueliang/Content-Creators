---
name: spoken-to-html-deck
description: 将演讲录音、口述思路、飞书文档、图片素材、AI 对话整理成可演讲的 HTML 网页 PPT。Use when the user asks to 口述生成 PPT, 演讲 PPT, HTML PPT, 网页 PPT, 录音转演示文稿, 飞书文档转 slides, 讲稿转 HTML deck, presentation from spoken notes, or wants to turn a talk idea into a speaker-led browser presentation.
---

# Spoken To HTML Deck

Use this skill when Moon or another creator wants to turn spoken thinking into a speaker-led HTML presentation.

The value is not only slide generation. The workflow captures the creator's live logic, helps AI ask clarifying questions, turns the result into a structured document, selects images, then generates a fixed-stage HTML deck that can be rehearsed, revised, shared, or exported.

## Core Stance

- Treat the speaker as the author of the argument, not a person filling a slide template.
- Preserve the live spoken logic before polishing.
- Use AI to clarify structure, tension, pacing, examples, and slide rhythm.
- Do not turn a talk into a dense article pasted onto slides.
- Prefer speaker-led decks: one idea per slide, strong hierarchy, generous breathing room, and enough visual anchors for memory.
- If the deck will be shared asynchronously as a reading file, explicitly switch to a higher-density mode.

## Workflow

### 1. Intake The Spoken Material

Ask for or locate:

- recording transcript, rough notes, or spoken outline
- target audience
- talk occasion and time limit
- desired outcome: inspire, teach, persuade, pitch, report, or facilitate discussion
- existing Feishu / document draft if any
- available images, screenshots, diagrams, logos, or references
- preferred density: speaker-led or reading-first

If the user only has a recording or messy transcript, first create a `talk logic map` instead of slide content.

### 2. Build A Talk Logic Map

Extract:

- central question
- audience tension or pain
- speaker's main judgment
- 3-5 movement beats
- examples, scenes, stories, data, or images that can carry each beat
- parts that are still unclear and need the speaker's judgment

Do not write full slides until the user confirms this map.

### 3. Run The AI Interaction Loop

Help the user iterate through questions such as:

- What do you most want the audience to remember?
- Which part should be felt in the room, not merely understood?
- What examples or images make this concrete?
- Where will the audience resist, get lost, or need a bridge?
- What can be cut because it belongs in speaker notes, not on the slide?

After each loop, update the structure. Keep a section called `待月亮判断` or `待演讲者判断` for decisions AI should not make.

### 4. Turn Into A Document-Ready Outline

Create a Feishu / doc-friendly outline:

```markdown
# 演讲标题

## 演讲目标

## 听众

## 核心判断

## 结构

### 01 开场
- 屏幕上出现:
- 我口头讲:
- 图片 / 视觉:

### 02 ...
```

Each slide candidate should include:

- on-screen text
- speaker note
- visual idea
- source material / quote / image if applicable
- risk or fact to verify

### 5. Design The HTML Deck

When generating the final HTML deck, use the installed `frontend-slides` skill if available. Follow these invariants:

- one self-contained HTML file unless assets must stay in a folder
- fixed 1920 x 1080 stage scaled to viewport
- 16:9 slides on desktop and mobile
- no text overflow, no overlapping panels
- speaker-led density by default
- real images when they help memory, not decorative filler
- CSS/JS inline when feasible
- keyboard navigation
- optional presenter notes or comments

If using `frontend-slides`, follow its fixed-stage rules and visual QA requirements.

### 6. Verify Before Delivery

Before handing off:

- open the HTML locally
- check desktop and mobile viewport screenshots
- click through or keyboard through all slides
- confirm referenced images load
- check that slide text fits and does not overlap
- verify title, names, dates, sources, logos, and sensitive information
- mark any claims that need the speaker's final confirmation

## Output Modes

### Talk Logic Map

Use when the user is still thinking aloud.

```markdown
## 演讲主线

## 听众为什么需要听

## 结构节奏
1.
2.
3.

## 可以放进 PPT 的材料

## 不适合放到屏幕上的内容

## 待演讲者判断
```

### Slide Outline

Use when the user is ready to move into a document or Feishu draft.

```markdown
| 页码 | 屏幕内容 | 口头讲述 | 视觉素材 | 需要确认 |
| --- | --- | --- | --- | --- |
```

### HTML Deck Build Brief

Use before generating the HTML presentation.

```markdown
## Deck Brief
- 标题:
- 场合:
- 听众:
- 时长:
- 密度:
- 视觉方向:
- 图片素材:
- 输出路径:

## Slide Plan
```

## Quality Gates

- `逻辑门`: audience, tension, main judgment, and slide sequence are clear.
- `演讲门`: slide text supports speech instead of replacing it.
- `素材门`: images and examples have source and permission.
- `事实门`: names, dates, claims, citations, and logos are checked.
- `视觉门`: each slide is readable at 1920 x 1080 and scaled viewport.
- `去 AI 味门`: no generic slogans, over-neat conclusions, or empty framework language.

## References

Read `references/pipeline.md` when the task involves turning raw spoken notes into a full deck workflow, productizing this workflow, or creating a reusable brief for another person to use.

