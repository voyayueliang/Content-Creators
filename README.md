# 月亮的 AI 工作台 / Content-Creators

这里不是一组万能 prompt，而是一套从真实内容项目里拆出来的工作流。

它适合已经有材料、任务或初稿的人：你可以把策划案、录音转写、会议纪要、旧稿、网页链接、图片说明和合作方要求放进来，让 AI 先帮你理清材料、读者、目的、边界和下一步。

月亮把自己的内容判断力拆成了可以复用的流程：AI 负责整理、追问、生成备选方案，人负责事实、口径、关系分寸、公开边界和最终发布判断。

公开页面：

https://voyayueliang.github.io/Content-Creators/

## 先从你手上的任务开始

| 你现在的情况 | 推荐入口 | 当前状态 |
| --- | --- | --- |
| 有一篇稿要写，但材料很散 | [`skills/moon-content-os`](skills/moon-content-os) | 已验证，适合先做材料和稿件方案 |
| 有一版 AI 初稿，要改到能发 | [`skills/creator-voice-guardian`](skills/creator-voice-guardian) | 已验证，适合发布前 final gate |
| 有播客、访谈、直播或视频回放 | [`skills/audio-to-wechat-article`](skills/audio-to-wechat-article) | 可试跑，适合先用一条真实素材验证 |
| 有对谈或圆桌逐字稿 | [`skills/dialogue-wechat-article-workflow`](skills/dialogue-wechat-article-workflow) | 已封装，适合保留对话现场感 |
| 要写公开人物或公司人物深度报道 | [`skills/public-profile-deep-report-workflow`](skills/public-profile-deep-report-workflow) | 已封装，适合公开资料研究和事实校对 |
| 要把口述思路变成演讲 PPT | [`skills/spoken-to-html-deck`](skills/spoken-to-html-deck) | 试点中，适合先用于个人演讲准备 |
| 想先建立人机协作边界 | [`skills/human-ai-collaboration-boundary`](skills/human-ai-collaboration-boundary) | 方法层，适合所有内容工作前置检查 |

还有 3 个已经独立发布的工作流仓库：

- 社区活动内容传播：[`voyayueliang/datawhale-content-producer-agent-skill`](https://github.com/voyayueliang/datawhale-content-producer-agent-skill)
- 活动复盘转公众号 Markdown：[`voyayueliang/event-recap-to-wechat-md-skill`](https://github.com/voyayueliang/event-recap-to-wechat-md-skill)
- 创作者作品系统搭建：[`voyayueliang/creator-work-system-builder`](https://github.com/voyayueliang/creator-work-system-builder)

## 状态说明

- **已验证**：已经在真实内容项目或完整交付中跑过，适合直接拿一条真实任务试用。
- **可试跑**：场景、输入和输出已经清楚，但还需要更多外部样本验证效果。
- **方法层**：不是单独帮你写一篇稿，而是帮你在使用 AI 前确认判断、边界和风险。
- **试点中**：月亮自己已经跑通过，方法清楚，但还没有足够多的公开案例，先不要当成熟产品使用。

## 怎么使用一个工作流

1. 打开对应的 `skills/<skill-name>/SKILL.md`。
2. 把里面的工作流说明复制到 Claude Code 或 Codex。
3. 放入你的真实材料：文档、转写、旧稿、链接、图片说明或项目背景。
4. 第一轮先要“材料地图 / 稿件方案 / 风险清单”，不要急着要正文。
5. 确认方向后，再让 AI 写初稿、改稿或进入发布前检查。

## 它适合解决什么问题

- 内容素材太散，不知道如何组合成一篇稿。
- AI 写出来很顺，但不像人，也不敢直接发。
- 活动、合作、播客、访谈和公开人物材料需要整理成可交付内容。
- 小团队或实习生需要一套可复用的内容生产流程。
- 创作者想把一次内容交付沉淀成下一次还能用的方法。

## 不适合什么

- 不适合把未经确认的事实直接写成公开稿。
- 不适合替代编辑、当事人或合作方的最终判断。
- 不适合处理没有授权的隐私材料、原始聊天记录或敏感信息公开发布。
- 不适合只想要一句万能 prompt 的场景。

## 这个仓库里有什么

```text
skills/
  audio-to-wechat-article/
  creator-voice-guardian/
  dialogue-wechat-article-workflow/
  human-ai-collaboration-boundary/
  moon-content-os/
  public-profile-deep-report-workflow/
  spoken-to-html-deck/

moon-ai-toolkit/
  index.html
  tools.html
  product-library/
  workflow-radar/
```

## 核心原则

- 先理清材料，再写正文。
- 先明确读者、任务和边界，再让 AI 生成。
- Human in the loop 不是最后检查一下，而是从一开始就设定人的判断位置。
- Humanity in the loop 指的是：人的现场感、关系分寸、价值判断和公开责任要被设计进流程里。
- 每次交付之后，都要把反馈、问题和可复用方法沉淀回来。

## License

No license has been selected yet. Please do not reuse commercially without permission.
