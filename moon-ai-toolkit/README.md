# 月亮的 AI 工作台

这是 Moon 的 AI 内容工作台索引。

它更像一个可以被别人直接使用的内容工作台：这里有方法、有 skills、有案例，也有已经可以交付给别人的产品化工作流。

## 一句话

月亮的 AI 工作台把真实的人、现场、对话和项目材料，转译成可以被理解、传播、复用和继续生长的内容资产。

## 网页入口

- `index.html`：月亮的 AI 工作台主入口。打开后直接看到完整工作流说明：适合什么、准备什么、产出什么、启动句怎么写，再按需查看模板源文件。
- `tools.html`：保留同版内容，兼容旧链接；主入口仍然使用 `index.html`。

## Studio 里有什么

| 模块 | 内容 | 当前状态 |
| --- | --- | --- |
| 方法 | AI 协作原则、去 AI 味、活动报道方法、对谈整理方法、商业合作审核门 | 已在多个项目中验证 |
| 频道 | 公众号、视频号、播客、直播、社群、newsletter 候选 | 部分已在运行 |
| Skills | Datawhale 内容传播、活动复盘、对谈转公众号、播客音视频转公众号、口述转 HTML 演讲 PPT 等 Codex skills | 已有多个可用包 |
| 产品 | 已产品化产品库，包括内容工作台、活动传播、音视频转文章、人物侧写、演讲 PPT、作品系统和发布前质检门 | 已整理成产品货架 |
| Radar | 工作流雷达：从对话、项目和复盘中发现可封装候选，但必须经月亮确认 | 内部试运行 |
| 故事与经历 | 田野、活动、采访、社区现场、AI 教育、开发者生态、个人路径 | 待整理成可读页面 |
| 案例与证据 | AIEC、Datawhale、2050、AMD、超脑等项目案例 | 部分已成案例资产 |

## 当前主产品

### 稿件材料组装器

已经有一篇稿要写时，先让 AI 把读者、目的、材料、口径和边界组合成一版可写方案。

它帮助创作者、研究者、主理人、自由职业者和小型内容团队，把素材、想法、项目、反馈和 AI 协作，变成可持续的内容资产、作品集和产品线。

这是月亮的 AI 工作台里的母产品。社区活动内容传播工作台、活动复盘、对谈转公众号、播客音视频转公众号等，都是它在不同场景里的垂直应用或能力模块。

关联位置：

- `../../04_产品与工具/已产品化产品库/00_moon-content-os/产品卡.md`
- `../../04_产品与工具/已产品化产品库/00_moon-content-os/产品定义-v0.1.md`
- `skills/moon-content-os/SKILL.md`
- GitHub: https://github.com/voyayueliang/Content-Creators/tree/main/skills/moon-content-os

### 人机协作边界与内容判断方法

所有内容工作流前面的底层方法。

它帮助创作者在使用 AI 前先分清：哪些劳动可以交给工具，哪些判断、关系、证据和公开责任必须留在人手里。这个方法承接 Human in the loop，也继续强调 Humanity in the loop：人的现场感、关系分寸、价值判断和最终责任要被设计进流程里。

适合：第一次使用月亮的 AI 工作台、开始商业合作稿、人物稿、活动稿、作品集整理，或发现 AI 初稿过度顺滑但“不像人”时。

关联位置：

- `product-library/09_human-ai-collaboration-boundary/产品卡.md`
- `index.html#workflow-human-ai`
- `skills/human-ai-collaboration-boundary/SKILL.md`
- GitHub: https://github.com/voyayueliang/Content-Creators/tree/main/skills/human-ai-collaboration-boundary

### 社区活动内容传播工作台

把社区活动材料变成可审核、可交付、可复盘的内容资产。

适合：AI 社区、开源社区、DevRel 团队、教育社群、活动负责人、实习生/初级内容运营。

Datawhale 是第一个试点案例，不是产品边界。

关联位置：

- `../../04_产品与工具/已产品化产品库/01_community-event-content-workbench/产品卡.md`
- GitHub: https://github.com/voyayueliang/datawhale-content-producer-agent-skill

### 活动复盘转公众号 Markdown Skill

把活动复盘、公开报道和现场材料整理成公众号 Markdown 与会后传播包。

适合：活动组织者、社区主理人、品牌活动负责人、伙伴传播负责人。

关联位置：

- `../../04_产品与工具/已产品化产品库/02_event-recap-to-wechat-md/产品卡.md`
- GitHub: https://github.com/voyayueliang/event-recap-to-wechat-md-skill

### 去 AI 味与事实校对门

发布前检查事实、口径、授权、边界和不像人的表达。

适合：公众号发布前、商业合作稿审核、AI 初稿改稿、人物稿和活动稿最后一轮校对。

它来自 Datawhale AIEC 连续稿的真实反馈：去 AI 味和防幻觉校对要成为两扇独立门，尤其适合商业合作内容和高风险发布场景。

关联位置：

- `product-library/04_qa-gates/产品卡.md`
- `skills/creator-voice-guardian/SKILL.md`
- GitHub: https://github.com/voyayueliang/Content-Creators/tree/main/skills/creator-voice-guardian

### 口述转 HTML 演讲 PPT

把一段口述思路，经过 AI 追问、飞书整理、图片入场和 HTML 模板生成，变成可以现场讲、可以浏览器打开的网页 PPT。

适合：内容创作者、讲师、社区主理人、独立工作者、需要快速准备分享或工作坊的人。

这个工作流来自月亮自己的高效演讲准备方式：先开一段录音，把脑子里想表达的逻辑完整说出来；再和 AI 互动几轮，把主线、听众张力、例子和删减点打磨清楚；然后放入飞书文档，补充图片、截图和素材，最后进入合适的 HTML PPT 模板。

当前状态：已具备个人实践基础，正在用真实演讲继续验证。它现在更接近试点 skill，还没有到大规模验证的成熟产品阶段。

关联位置：

- `skills/spoken-to-html-deck/SKILL.md`
- GitHub: https://github.com/voyayueliang/Content-Creators/tree/main/skills/spoken-to-html-deck

### 创作者作品系统搭建

从求职、申请、合作或个人品牌目标出发，把经历、作品、证据和叙事整理成外部读者能快速看懂的作品系统。

适合：内容创作者、独立工作者、求职者、申请者、社区运营者，以及想把项目经验整理成作品集的人。

关联位置：

- `product-library/08_creator-work-system-builder/产品卡.md`
- GitHub: https://github.com/voyayueliang/creator-work-system-builder

### 工作流雷达

工作流雷达是内部筛选层，不是公开产品页。

它帮助月亮从其他对话、项目文档、复盘和交付过程里发现可能值得封装的内容创作流程。雷达只负责发现候选、评分、整理到队列，不会自动上架。每个候选必须经过月亮确认，才能进入试点、GitHub Skill 或公开工作台。

关联位置：

- `workflow-radar/README.md`
- `workflow-radar/radar-rules.md`
- `workflow-radar/queue.md`

## 产品化标准

每条工作流进入公开页前，都要回答清楚：它解决谁的哪类问题、用户准备什么材料、会交付什么结果、月亮自己的方法在哪里、哪些判断必须留给人、当前验证到哪一级、下一步怎么继续验证。

关联位置：

- `product-library/产品化审计与上架标准.md`
- `product-library/2026-06-13-工作台产品化审计.md`

## 工作台关心什么

- 把散乱材料变成可判断的信息结构。
- 把现场和关系转译成公共表达。
- 把每次反馈沉淀成下次可用的方法。
- 把商业合作内容做成可审核、可交接、可减少事故的流程。
- 保护人的声音、边界和判断，避免把一切磨成通用表达。

## 未来网页可以这样组织

1. 首页：我是谁 / 我在做什么 / 可以打开哪些入口。
2. 方法：Moon 的 AI 协作与内容生产方法。
3. 产品：可复用的工作流和服务包。
4. 频道：我持续发布和实验的地方。
5. 案例：真实项目如何从材料变成内容资产。
6. 故事：我的路径、田野和经历。

## 下一步

- 从产品库中选择 2 个主推产品放到首页。
- 给每个产品补一张流程图或案例图。
- 把“我的方法”整理成 3-5 条可以对外讲清楚的原则。
- 把故事与经历按场景整理：大理、上海、AI 教育、开发者生态、社区活动、独立工作室。
