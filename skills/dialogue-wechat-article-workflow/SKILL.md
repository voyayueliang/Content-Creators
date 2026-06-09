---
name: dialogue-wechat-article-workflow
description: 将播客、直播、视频号回放、圆桌、访谈、连麦对谈、活动回放逐字稿，转化为适合公众号发布的对谈稿、对谈摘要、观察文或内容资产包。Use when the user asks to 把对谈转公众号, 直播对谈整理成文章, 播客转推文, 嘉宾连麦整理, 活动回放整理, 访谈内容变公众号, or build a reusable human-AI workflow for conversation-to-WeChat publishing with voice calibration, speaker mapping, title iteration, visible length checks, image placeholders, and fact/ethics review.
---

# Dialogue WeChat Article Workflow

Use this skill for turning spoken conversations into WeChat Official Account-ready content across different accounts, hosts, and guest combinations.

It can support:

- 机构账号、社群账号或项目账号的直播、沙龙、访谈
- 个人账号的对谈、播客、活动回放
- 嘉宾、主持人、创始人、创作者或教育者之间的直播对谈
- 双人访谈、三人圆桌、多人活动复盘
- later reuse as 素材卡, 视频号脚本, 小红书案例帖, 朋友圈短记, newsletter seed

## Core Stance

- Treat spoken material as source material, not as an article draft.
- Start with a compact content view when the material is complex. Do not default to a long draft before deciding form, platform, audience, and boundaries.
- Build a fresh speaker map for every episode. Never copy names, roles, or bios from a previous episode.
- Decide the publishing voice before writing: institutional account, personal account, co-branded account, or editor's note.
- Preserve dialogue when the exchange itself has value. Do not force every conversation into a polished thesis essay.
- Use human-AI iteration as part of the method: first map, then structure, then draft, then respond to human critique.
- Respect human-AI collaboration boundaries: AI may propose, structure, draft, and check; humans decide voice, relationship risk, factual confidence, publication readiness, and consent.
- Protect privacy, consent, minors, guests, commercial details, and relationship boundaries.
- Make every public claim traceable to transcript, poster, user note, or marked editorial inference.

## Start With A Source Map

Before drafting, identify:

- source type: livestream, podcast, interview, roundtable, replay, spoken note, mixed material
- publication account: whose account will publish, and in what voice
- event scene: date, location, platform, live-room texture, poster, screenshots
- speaker map: display name, role, dialogue label, bio source, confidence, pending confirmations
- target readers: parents, practitioners, founders, creators, community members, industry peers, general readers
- output goal: WeChat dialogue, summary, essay, video script, asset cards, or a package
- public boundaries: private stories, minors, client cases, student work, commercial products, organization names, images

If information is unclear, mark `待确认`. Do not invent.

## Choose The Output Form

- `编辑版对谈稿`: speaker turns and live thinking are the main value.
- `对谈摘要`: the transcript is long; curate 4-6 sections.
- `观点观察文`: there is one strong public argument and enough evidence.
- `人物 / 故事文`: one person's arc is the center.
- `活动复盘文`: the event itself matters.
- `方法提炼文`: the conversation contains repeatable practice.
- `视频号口播稿`: one strong question, scene, or quote is enough.
- `素材卡`: valuable but not ready for public release.
- `暂不外发`: consent, privacy, or relationship risk is high.

When unsure, start with a `内容判断卡` instead of drafting.

## Human-AI Collaboration Loop

For complex dialogue articles, do not aim for one-shot perfection.

1. **AI first pass: map**
   - source map, strongest article direction, reader tension, risks, missing confirmations
2. **Human calibration**
   - account voice, audience, preferred form, examples to keep/remove, length range
3. **AI second pass: skeleton**
   - title groups, section arc, must-keep quotes/scenes, image placeholders
4. **Human selection**
   - choose title direction, section titles, tone, what feels wrong
5. **AI draft**
   - publishable draft with editor notes and boundary checks
6. **Human critique**
   - natural feedback like `太 AI`, `太短`, `标题不对`, `不要写成观点文`, `保留对谈`, `前轻后重`
7. **AI revision**
   - translate feedback into editing actions, recount visible body, check logic and ethics
8. **Final packaging**
   - article, image list, publishing checklist, reusable content assets, next questions

Read `references/human-ai-collaboration-loop.md` for the full interaction protocol.

## Drafting Rules

- Open from a real scene or reader tension, not a generic trend paragraph.
- Use 4-5 sections for standard WeChat dialogue posts; 3 sections is often too compressed.
- Each section needs one clear job in the article's logic.
- Preserve speaker labels and direct exchange when possible.
- Remove filler, repeated self-correction, greetings, platform reminders, and transcript noise.
- Keep productive hesitation only when it reveals thinking-in-progress.
- Do not end every section with a neat takeaway; that creates AI味.
- Put image placeholders where visuals help understanding, with permission reminders.
- Count reader-visible正文 only when checking length.

## Quality Defaults

- Standard dialogue article: `4000-6000` reader-visible Chinese characters.
- Short recap: `2500-3500`.
- Deep feature: `6000-8000`, only when the user explicitly accepts longer reading.
- Titles: provide groups by audience and tone, not one generic list.
- Opening: account-specific voice; institution and personal accounts require different posture.
- Final check: fact, logic, voice, length, section balance, privacy, images, unresolved confirmations.

## Reference Files

- `references/operator-workflow.md`: full human operator workflow.
- `references/human-ai-collaboration-loop.md`: how the human and AI should iterate.
- `references/human-ai-boundaries.md`: what AI may do, what must remain human judgment, and how to handle critique.
- `references/content-method-principles.md`: reusable principles distilled from earlier content workflows.
- `references/voice-account-map.md`: how to choose voice for different publishing accounts.
- `references/output-template.md`: reusable article and asset package template.
- `references/quality-check.md`: final fact, logic, ethics, length, and anti-AI-tone checks.

## Final Response

When done, report:

- files created or updated
- where the shareable Skill package lives
- what workflow modules it contains
- any unresolved decisions if this skill was also used to draft a real article
