---
name: audio-to-wechat-article
description: 将播客、音频、视频回放、直播回放、访谈录音、活动回放、圆桌逐字稿或口播笔记转化为公众号文章。Use when the user asks to 把播客转公众号, 音频转文章, 视频转公众号, 直播回放转文章, 逐字稿改成推文, 音视频内容整理成长文, 从录音/视频/访谈/圆桌提炼公众号稿, or turn spoken audio/video content into a publishable WeChat article while preserving field texture, speaker boundaries, public consent, and the creator's own voice.
---

# Audio To WeChat Article

Use this skill to turn spoken audio/video material into a publishable WeChat article draft. The goal is not transcription cleanup or video editing; it is editorial transformation: find the strongest public argument, preserve live texture, protect speaker boundaries, and decide whether the material deserves a long article.

Treat "AI味", "不像发布者", "太完整", "太顺", or "太平台" as hard revision signals. Do not publish abstract values naked; let judgments grow from a small narrative, field detail, showcase, or lived practice.

Use these base content rules: scene before concept, evidence before fluency, dialogue as a first-class output, human-AI boundaries, platform fit, and asset recovery.

Not every spoken source should become a deep article. When the value lives in the exchange itself, choose an edited dialogue, conversation digest, or Q&A-style post instead of forcing a thesis-led WeChat essay.

When the user wants to record the material for 视频号, produce a mouth-friendly, scene-led, recordable script instead of only a written article.

When the user wants an easier way to view outputs, return a compact readiness card or platform decision table before drafting the full article.

## Core Stance

Treat podcast, livestream, recording, and video replay content as source material, not as an article draft.

- Do not summarize every topic in order.
- Do not force all audio/video into a long article. Some material should become a short post, quote card, topic seed, story card, or private note.
- Do not force all interviews into the publisher's synthesized argument. Some should remain visibly dialogic.
- Preserve spoken energy, but remove filler, repetition, hosting logistics, digressions, and timestamp debris.
- Keep the central editorial judgment visible. A WeChat article needs one reason to exist.
- Protect guests, listeners, private examples, and commercially sensitive details.

## Workflow

1. Build a source map:
   - 来源: podcast, audio recording, video replay, livestream, interview, event replay, transcript, notes, or mixed material
   - 时间/场景: when and where the conversation happened
   - 人物: speakers, roles, relationship, naming/anonymization needs
   - 可公开边界: public, semi-public, private, needs consent, or unknown
   - 素材状态: raw transcript, cleaned transcript, notes only, partial audio/video clips, or user memory
2. Diagnose whether it should become a WeChat article:
   - `适合长文`: has a clear claim, tension, story arc, strong scenes, useful method, or public timing
   - `适合对谈稿`: the back-and-forth, guest wording, host questions, or thinking process is the main value
   - `适合对谈摘要`: the source is long but contains several publishable exchanges around clear themes
   - `适合视频号口播`: has one concrete detail, question, or exchange that the publisher can speak to camera
   - `适合短文`: has one sharp idea but not enough evidence for a long piece
   - `适合素材卡`: useful quotes/scenes but no article center yet
   - `需补问`: missing facts, speaker consent, examples, chronology, or the creator's judgment
   - `暂不外发`: too private, too sensitive, or relationship risk is high
3. Choose one article type:
   - `观点观察文`: one central judgment from the conversation, supported by quotes and scenes
   - `人物/故事文`: one person or group arc, with turning points and concrete actions
   - `活动/直播复盘文`: what happened, what it revealed, and what should happen next
   - `方法提炼文`: turn repeated practice into a framework, checklist, or working method
   - `对谈梳理文`: curated dialogue around themes, preserving speaker turns and thinking process
   - `对话摘录文`: lightly edited Q&A or excerpt, used when the speakers' wording is the value
   - `视频号口播稿`: spoken script with cover text, subtitles, recording posture, and post caption
4. Extract article material:
   - Central claim
   - 3-5 support points
   - Scenes worth showing
   - Quotes worth keeping
   - Reader tension or problem
   - Boundary risks
   - Missing follow-up questions
5. Build the article skeleton before drafting:
   - Title candidates
   - One-sentence thesis
   - Opening hook: scene, tension, or sharp question
   - Section arc
   - Quote placement
   - Ending: reflection, invitation, CTA, or next action
6. Draft the article:
   - Rewrite oral fragments into readable paragraphs.
   - Keep key quotes short and attributed when allowed.
   - Make transitions explain why each section follows.
   - Let concrete moments carry meaning before abstract conclusions.
   - Add a light editor's note only when context is necessary.
7. Run a compact final check:
   - Logic: What is the article really saying?
   - Evidence: Which claims are supported by the audio?
   - Voice: Which lines sound generic or over-polished?
   - AI味: Which parts sound too smooth, too complete, too framework-like, or unlike the publisher?
   - Boundary: What needs consent, masking, or removal?
   - Form: Should this remain a dialogue instead of becoming a synthesized article?
   - Asset: What can this article become later: case, method, offer signal, source card, or portfolio proof?

## WeChat Article Defaults

Use these defaults unless the user requests another style.

- Length: `1800-3500` Chinese characters for a standard article; `800-1500` for a light recap.
- Structure: opening, 3-5 titled sections, closing note.
- Tone: concrete, reflective, field-based, not marketing-heavy.
- Voice: small narrative before big trend; real scene before concept; do not end every section with a neat takeaway.
- Title: generate 5-8 options across `直接判断`, `场景张力`, `问题意识`, and `栏目感`.
- Subtitle/摘要: one short line explaining why this piece matters now.
- CTA: soft and context-specific, such as asking for stories, inviting replies, linking to the next event, or naming a collaboration boundary.

## Spoken-To-Written Rules

When transforming oral material:

- Delete filler: "然后", "其实", "就是", "对吧", repeated self-correction, platform reminders, greeting loops, and logistics.
- Merge repeated points instead of preserving chronology.
- Keep productive hesitation when it reveals uncertainty, relationship texture, or thought-in-progress.
- Convert long monologues into paragraphs with one job each.
- Use direct quotes only for lines with voice, evidence, or emotional weight.
- Do not fabricate examples, numbers, chronology, speaker intent, or audience reaction.
- Do not write "这期播客我们聊了很多" as an opening unless the meta-context is the point.

## Output Modes

Choose the smallest useful output.

### Article Readiness

Use when the source is raw, long, or uncertain.

```markdown
## 是否值得写成长公众号

结论:

## 最强文章方向
| 方向 | 类型 | 为什么成立 | 还缺什么 |
| --- | --- | --- | --- |

## 可用素材
| 素材 | 用途 | 风险 |
| --- | --- | --- |

## 不建议写成

## 需要创作者补的 3 个判断
```

### Compact View

Use when the user wants a lighter result.

```markdown
## 公众号查看卡

- 是否值得写成长文:
- 更适合的形式: 长文 / 对谈 / 短观察 / 视频号 / 小红书 / 素材卡
- 最好的入口:
- 需要保留:
- 需要删弱:
- 风险:
- 下一步:
```

### Article Brief

Use before drafting, or when the user wants a writing plan.

```markdown
## 文章主张

## 读者为什么现在需要读

## 标题候选

## 结构

## 必保留的场景/原话

## 需要删弱的口语内容

## 公开边界

## CTA
```

### WeChat Draft

Use when the user asks for the actual article.

```markdown
## 标题候选

## 摘要

## 正文

## 备选开头

## 发布前确认
```

### Edited Dialogue

Use when the source should remain a conversation.

```markdown
## 是否适合对谈形式

结论:

## 标题候选

## 编辑说明

- 对谈发生在:
- 发言人:
- 编辑原则:
- 公开边界:

## 对谈正文

### 1. 主题 / 问题

主持人:

嘉宾:

主持人:

嘉宾:

### 2. 主题 / 问题

...

## 发布者短后记

## 还没聊完的问题

## 发布前确认
```

### Material Recovery

Use when the material should not become a full article yet.

```markdown
## 不直接写成长文的原因

## 可回收素材卡
| 卡片 | 类型 | 可转化用途 | 待补 |
| --- | --- | --- | --- |

## 更适合的发布形态

## 下一次追问/补采
```

## Optional Handoff

If the user's environment has adjacent writing or knowledge-management skills, use them only when useful. This skill must still work as a standalone workflow.

- Use a material-intake or note-card workflow for long raw transcripts that first need reusable cards.
- Use a logic/evidence review workflow when a draft's claims need support checking.
- Use a voice-editing workflow before final polishing.
- Use a platform adaptation workflow after the WeChat article is stable and needs variants for Xiaohongshu, newsletter, posts, or show notes.

## Guardrails

- Do not expose private conversations, client details, financial terms, identifiable audience stories, or off-record comments without permission.
- Do not convert a guest's words into the creator's stance unless the distinction is clear.
- Do not make the article sound more certain, dramatic, or strategic than the source supports.
- Do not smooth away contradiction if the contradiction is the real point.
- If the transcript is too messy or too thin, return an article brief plus follow-up questions instead of pretending to finish.
