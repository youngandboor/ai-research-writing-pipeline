# AI Research Writing Pipeline

[English README](README.md)

面向完整学术论文写作流程的 Codex skill。它把论文写作视为一个
`证据 -> 论断 -> 图表 -> 正文 -> 审稿 -> 修订 -> 投稿检查` 的受控集成流程，
而不是单纯的润色或生成文本。

这个 skill 不绑定具体学科、会议、期刊或项目。当前项目需要自己提供研究领域、
目标 venue、方法事实、证据标准、写作风格和本地规则。

## 能做什么

- 扫描并整理混乱的科研项目目录。
- 将任务拆成想法评估、文献核验、论文阅读、baseline 选择、实验证据审计、
  正文写作、语言润色、科研绘图、独立审稿、rebuttal、数据/代码可用性、
  投稿材料和展示/专利等通道。
- 要求核心论断、数字、引用、图表和未知事实先登记，再进入正文。
- 保留负结果、适用边界、post-hoc 解释和证据不足的 gap。
- 避免把 mock/proxy 证据写成真实系统、真实后端或现实世界结论。
- 提供一个轻量目录 inventory 脚本，帮助先建立项目地图，再决定是否移动文件。

## 仓库结构

```text
ai-research-writing-pipeline/
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
`-- skills/
    `-- ai-research-writing-pipeline/
        |-- SKILL.md
        |-- agents/
        |   `-- openai.yaml
        |-- references/
        |   |-- artifact-contracts.md
        |   |-- capability-playbooks.md
        |   `-- framework-patterns.md
        `-- scripts/
            `-- workspace_inventory.py
```

## 安装

使用 Codex 的 skill installer 从 GitHub 安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo youngandboor/ai-research-writing-pipeline \
  --path skills/ai-research-writing-pipeline
```

安装后重启 Codex，让新 skill 被发现。

## 使用方式

显式调用：

```text
Use $ai-research-writing-pipeline to inspect this research project, build claim
and evidence ledgers, and turn the current draft into a traceable manuscript
workflow.
```

如果项目目录已经很乱，可以先运行：

```bash
python3 ~/.codex/skills/ai-research-writing-pipeline/scripts/workspace_inventory.py .
```

## 核心原则

1. 先建立项目地图，再写正文。
2. 先分类任务通道，再分配工作。
3. 先冻结方法事实、证据边界和 non-goals。
4. 先建立文献、实验、数字、图表和未知事实 ledger。
5. 只有登记过、可追溯的论断才能进入正文。
6. 图表必须来自 source data，并保留生成脚本和 QA 记录。
7. 最终论文只由一个 controller/editor 集成。
8. 审稿必须基于当前稿件和当前证据 fresh review。
9. 修订优先处理高影响、低证据风险的问题。
10. 投稿就绪必须由 validator/compile/checklist 证明，而不是口头宣称。

## 集成的能力

本 skill 已将常用科研写作技能压缩为内置 playbooks：

- idea evaluator：想法可行性、新颖性、生命周期和致命缺陷检查。
- literature/citation workflow：文献检索、元数据核验、claim-to-citation 映射。
- paper reader：PDF/论文逐源分析和引用用途判断。
- baseline selector：经典、SOTA、强简单 baseline 和可复现性筛选。
- writing/polishing：证据约束写作、结构重组和语言润色。
- story/template/intro workflow：论文主线、技术论文骨架和引言漏斗。
- evidence auditor：代码、配置、实验结果、统计和 source data 审计。
- figure workflow：图型选择、绘图、导出、最终尺寸 QA 和 manifest。
- reviewer/red-team：独立审稿、严重性排序、修订路线。
- rebuttal workflow：外部评审意见分类和逐点回应。
- data/release workflow：数据可用性、代码发布、license、PID、未知事实门控。
- side outputs：PPT、报告、专利草稿等辅助输出，但不反向制造论文事实。

## 适用场景

- 你有代码、实验结果和论文草稿，但目录很乱。
- 你担心 AI 写作把没有证据的内容写进论文。
- 你需要把多个 agent 的输出合并成一个可审计 manuscript workflow。
- 你需要在投稿前检查引用、数字、图表、claim strength 和行政材料。
- 你想把科研写作流程从一次性对话变成可复用的项目机制。

## 许可证

MIT License.
