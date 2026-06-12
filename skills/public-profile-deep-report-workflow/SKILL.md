---
name: public-profile-deep-report-workflow
description: 用公开资料生成公众人物、创始人、开发者、创作者或行业人物的深度报道。Use when the user asks to 写人物深度报道, 公众人物报道, founder profile, builder profile, 人物侧写, 基于公开资料写人物稿, or turn interviews, podcasts, talks, articles, social posts, and public materials into a fact-checked longform profile.
---

# Public Profile Deep Report Workflow

Use this skill to turn public materials about a person into a grounded longform profile or deep report. Do not begin with a polished article. Build the evidence table first.

## Output Modes

Choose one mode before drafting:

- **第三方无采访**: only public materials are available. Mark uncertainty clearly and avoid mind-reading.
- **当事人自述**: the subject provided notes, interview material, or voice memos. Preserve their language without becoming PR copy.
- **三方协作**: there are public sources plus a client, editor, or partner brief. Separate facts, narrative preference, and commercial claims.

## Workflow

1. **Material Map**
   - List every source with title, link/path, date, source type, and reliability.
   - Separate primary sources, third-party reports, social media, interviews, talks, and user comments.
   - Mark missing context and claims that need confirmation.

2. **Person View**
   - Extract timeline, recurring choices, relationships, conflicts, turning points, public positioning, and contradictions.
   - Identify what the person is trying to build, change, defend, or prove.
   - Keep concrete scenes, quotes, and examples before abstract labels.

3. **Reader Lens**
   - Ask the user who this is for: public readers, industry peers, community members, investors, students, or portfolio reviewers.
   - Ask what the piece should help readers understand that a bio page cannot.
   - Propose 2-3 possible angles before drafting.

4. **Structure**
   - Build an outline with evidence attached to each section.
   - Use narrative only where there is source support.
   - Avoid heroic, over-polished, or slogan-like framing unless source material justifies it.

5. **Draft**
   - Write in sections.
   - Keep names, dates, affiliations, titles, quotes, and causal claims traceable to source material.
   - Prefer specific acts and decisions over broad personality judgments.

6. **Two Gates Before Delivery**
   - **Fact gate**: check names, roles, dates, organizations, claims, links, and quote attribution against the material map.
   - **De-AI-tone gate**: remove generic framing, forced contrasts, empty conclusions, and polished claims that no human source actually supports.

## Required Questions

Ask these before writing the full article:

- Who is the person, and what materials are available?
- Which output mode applies: 第三方无采访, 当事人自述, or 三方协作?
- Who will read it, and where will it be published?
- What should not be inferred, dramatized, or made public?
- Is the goal reporting, portfolio sample, partner profile, workshop material, or internal research?

## Starter Prompt

```text
打开公众人物深度报道工作台。

对象：[人物姓名]
模式：[第三方无采访 / 当事人自述 / 三方协作]
已有素材：[链接 / 文件 / 暂无，请帮我搜集]
发布渠道：[公众号 / Substack / 作品集 / 机构投稿 / 不确定]
大致字数：[比如 3000-6000 字 / 先做框架]

请先做人物资料查看台和素材解剖，不要直接写完整长文。
完成资料查看台后，请用短问题问我阅读透镜、读者画像和框架判断。
最终交付前请过去 AI 味门和信息校对 / 防幻觉门。
```
