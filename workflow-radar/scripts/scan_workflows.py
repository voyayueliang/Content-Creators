#!/usr/bin/env python3
"""Lightweight radar for Moon AI Workbench workflow candidates.

It scans markdown / text files for reusable-workflow signals and prints a
candidate report. The report is only a first pass; Moon still decides what
enters the public workbench.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
from typing import Iterable


TRIGGER_TERMS = [
    "工作流",
    "skill",
    "Skill",
    "沉淀",
    "产品化",
    "复用",
    "模板",
    "方法",
    "可上架",
    "工作台",
    "雷达",
    "去 AI 味",
    "校对",
    "质量门",
]

MATURITY_TERMS = {
    "场景": ["场景", "适合", "什么时候用", "用户", "受众"],
    "输入": ["输入", "材料", "准备", "文件", "逐字稿", "策划案"],
    "输出": ["输出", "产出", "得到", "交付", "文章", "报告", "卡片"],
    "步骤": ["步骤", "流程", "先", "再", "最后", "清单"],
    "边界": ["边界", "确认", "人工", "人判断", "不能公开", "脱敏"],
    "质量门": ["校对", "事实", "去 AI 味", "审核", "风险", "检查"],
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".playwright-cli",
    "dist",
    "workflow-radar",
    "__pycache__",
}

TEXT_EXTENSIONS = {".md", ".txt", ".csv"}


def iter_files(root: Path) -> Iterable[Path]:
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = Path(current) / name
            if path.suffix.lower() in TEXT_EXTENSIONS:
                yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def score_text(text: str) -> tuple[int, list[str]]:
    matched = []
    score = 0
    for dimension, terms in MATURITY_TERMS.items():
        if any(term in text for term in terms):
            matched.append(dimension)
            score += 1
    return score, matched


def excerpt(text: str, term: str, width: int = 80) -> str:
    index = text.find(term)
    if index < 0:
        return ""
    start = max(index - width, 0)
    end = min(index + len(term) + width, len(text))
    snippet = text[start:end].replace("\n", " ")
    return " ".join(snippet.split())


def classify(score: int, trigger_count: int) -> str:
    if score >= 5 and trigger_count >= 3:
        return "candidate"
    if score >= 3 and trigger_count >= 2:
        return "hold"
    return "raw"


def build_report(root: Path) -> str:
    rows = []
    for path in iter_files(root):
        text = read_text(path)
        triggers = [term for term in TRIGGER_TERMS if term in text]
        if not triggers:
            continue
        score, matched = score_text(text)
        state = classify(score, len(triggers))
        first_trigger = triggers[0]
        rows.append(
            {
                "path": path,
                "score": score,
                "state": state,
                "triggers": triggers,
                "matched": matched,
                "excerpt": excerpt(text, first_trigger),
            }
        )

    rows.sort(key=lambda item: (item["state"] != "candidate", -item["score"], str(item["path"])))

    today = dt.date.today().isoformat()
    lines = [
        "# 工作流雷达扫描报告",
        "",
        f"- 扫描日期：{today}",
        f"- 扫描目录：`{root}`",
        f"- 命中数量：{len(rows)}",
        "",
        "说明：这是机器初筛，不代表可以上架。进入公开工作台前，需要月亮确认。",
        "",
    ]

    if not rows:
        lines.append("没有发现明显候选。")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| 建议状态 | 分数 | 文件 | 命中维度 | 触发词 | 摘要 |",
            "| --- | ---: | --- | --- | --- | --- |",
        ]
    )
    for item in rows:
        rel = item["path"].relative_to(root)
        trigger_text = ", ".join(item["triggers"][:6])
        matched_text = ", ".join(item["matched"]) or "待判断"
        summary = item["excerpt"].replace("|", "/")
        lines.append(
            f"| {item['state']} | {item['score']} | `{rel}` | {matched_text} | {trigger_text} | {summary} |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            "1. 先看 `candidate`，判断是否真的解决一类人的问题。",
            "2. 把值得继续看的条目复制到 `workflow-radar/candidates/`，使用候选卡模板整理。",
            "3. 月亮确认后，才进入 `pilot` 或 `live`。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan for workflow candidates.")
    parser.add_argument("root", help="Folder to scan")
    parser.add_argument("--out", help="Optional markdown report path")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    report = build_report(root)

    if args.out:
        out = Path(args.out).expanduser().resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
