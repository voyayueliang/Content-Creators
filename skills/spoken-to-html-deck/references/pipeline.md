# Spoken To HTML Deck Pipeline

## Product Shape

This workflow can become a content product because it solves a repeated creator problem:

> I can think and speak quickly, but turning the live logic into a good deck usually becomes slow, visual, and fragmented.

The productized method is not "AI makes slides." It is a creator preparation system:

- voice captures thinking before it is flattened into document language
- AI asks questions and exposes missing judgments
- Feishu / document staging keeps the outline editable and shareable
- images and screenshots become memory anchors
- HTML turns the deck into a browser-native artifact that can be rehearsed, shared, deployed, or exported

The product is a guided production line:

1. speak the talk idea
2. transcribe or paste rough notes
3. use AI to ask clarifying questions
4. turn the result into a Feishu / document outline
5. add images and examples
6. choose an HTML deck style
7. generate and verify a browser presentation
8. rehearse and revise

## Recommended Agent Roles

Use these roles as an internal review committee. They can be simulated in-thread unless the user explicitly asks for real subagents.

| Agent | Job |
| --- | --- |
| Talk Editor | Finds the central argument and talk rhythm. |
| Ordinary Listener | Flags where a first-time audience gets lost. |
| Slide Director | Splits ideas into slide beats and visual moments. |
| Visual Curator | Maps images, screenshots, diagrams, and references to slides. |
| Evidence Checker | Checks names, dates, claims, and sources. |
| Voice Guardian | Removes generic AI phrasing and keeps the speaker's live voice. |
| HTML Deck Builder | Generates and verifies the final fixed-stage HTML deck. |

## Moon Method: From Spoken Logic To Stage Rhythm

Use this sequence when the user wants Moon's actual workflow, not a generic deck generator:

1. `先说完`: ask the speaker to record the whole idea before organizing it. Do not interrupt the first pass.
2. `找主线`: extract the question, tension, judgment, and emotional temperature of the talk.
3. `追问缺口`: ask only the questions that change the structure, examples, or public boundary.
4. `文档中转`: create a Feishu-friendly outline with screen text, oral explanation, visual material, and risk notes.
5. `图片入场`: add images after the argument is clear, but before the final HTML deck. Images should help memory, proof, rhythm, or emotion.
6. `模板匹配`: choose a visual system that fits the occasion and speaker, not a pretty template in isolation.
7. `浏览器排练`: open the HTML deck, speak through it, and revise around live pacing.

## Validation Ladder

Mark each use case with one of these levels:

| Level | Meaning | Evidence Needed |
| --- | --- | --- |
| `L0 方法假设` | The flow makes sense but has not run end to end. | Workflow card only |
| `L1 月亮自用` | Moon has used the flow on her own talk preparation. | Notes, rough outline, timing |
| `L2 完整交付` | One full talk has gone from recording to HTML deck. | Final deck, before/after outline, QA notes |
| `L3 他人复用` | Another creator can use the workflow with light guidance. | User feedback, friction points |
| `L4 产品化` | The workflow has repeatable intake, examples, QA, and support boundary. | Public sample, template, usage guide |

Current status should be treated as `L1` until a full recording-to-HTML case is archived.

## Intake Questions

Ask only what is needed:

1. What is the talk occasion and audience?
2. How long is the talk?
3. Is this a live talk or a deck people will read later?
4. Do you have transcript, notes, or Feishu doc?
5. Do you have images, screenshots, logos, or examples?
6. What should the audience remember or do afterwards?

## Better Intake Prompt

Use this when another person wants to run the workflow:

```markdown
我想用“口述转 HTML 演讲 PPT”工作流准备一次演讲。

这次演讲的场景是：
听众是：
时长是：
我希望他们听完后记住 / 愿意行动的是：

我现在的材料：
- 录音或转写：
- 飞书 / 文档：
- 图片、截图、logo、案例：
- 参考风格：

请先不要生成 PPT。
先帮我做：
1. 演讲主线地图
2. 听众可能会卡住的地方
3. 需要我本人判断的问题
4. 哪些内容适合上屏幕，哪些适合放讲稿
5. 下一轮整理成飞书 slide outline 的结构
```

## Slide Rhythm Heuristics

For speaker-led talks:

- 1 idea per slide
- 1-3 visible lines when possible
- use section breaks for pacing
- put nuance in speaker notes
- use images to anchor memory
- make the first 3 slides clarify why the talk matters

For reading-first decks:

- each slide can carry more context
- use structured layouts, captions, and comparison tables
- still split when text becomes cramped
- make the argument understandable without the speaker

## Screen Vs Voice Rule

Every slide must answer:

| Layer | What It Does |
| --- | --- |
| Screen | Gives the audience a phrase, image, contrast, diagram, or number they can hold. |
| Voice | Carries context, nuance, story, and judgment. |
| Notes | Keeps the speaker's bridge, examples, and timing reminders. |

If the screen contains the whole paragraph, move nuance into notes.
If the voice has to explain the slide for too long, split or redesign the slide.

## Feishu / Document Outline

Use a document as the staging area before HTML generation:

```markdown
# Title

## Talk Goal

## Audience

## Core Judgment

## Slide Outline

### Slide 01
- On screen:
- Speaker says:
- Visual:
- Source / risk:
```

## HTML Deck Build Requirements

- Fixed 1920 x 1080 slide canvas.
- Whole stage scales to viewport.
- No responsive reflow inside slides.
- Use real images or generated assets only when they help the message.
- Keep CSS and JS inline unless a folder deployment is necessary.
- Include keyboard navigation.
- Verify in browser with at least one desktop and one phone viewport.

## When Not To Productize

Do not turn a deck into a public product if:

- the workflow only worked because of one private client context
- the images, examples, or case materials cannot be shared or abstracted
- the speaker's personal judgment is the entire value and cannot be generalized
- there is no repeatable intake, structure, output, or quality gate

## Productization Notes

This workflow becomes stronger after each real talk if the following assets are saved:

- raw prompt / spoken transcript
- talk logic map
- Feishu slide outline
- image list and why each image was used
- first HTML deck
- final HTML deck after rehearsal
- QA checklist and known friction
- anonymized before / after screenshots

Without these artifacts, it remains a useful personal workflow but not yet a strong public product.
