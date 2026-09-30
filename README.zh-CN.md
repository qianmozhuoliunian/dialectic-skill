# Dialectic：有记录、有边界的反驳优化 Skill

保留你的原始目标，通过“理解 → 反驳 → 裁决 → 最小修改 → 核验 → 停止”，把想法整理成可执行建议。

[English](README.md) · [安装](docs/installation.md) · [完整示例](examples/README.md) · [发布到 GitHub](docs/publishing.zh-CN.md)

当前版本：实验性 v0.1.0。这是一个 Agent Skill 项目；使用时由宿主 AI 执行规则，不需要部署服务、配置额外 API key 或先学框架。

## 它解决什么问题？

普通的反复批评容易出现三种情况：同一个问题换着说、错误批评也照单全收、改了措辞就认为问题已解决。

Dialectic 把每条关键批评变成可以追踪的问题：说明依据、裁决是否成立、定义如何验收，然后检查修改是否真的满足要求。

这些是设计目标，不是已经证明的优势。已有普通提示对照也能做好关键判断；当前不能宣称优于 Self-Refine 或普通反思提示。详细记录在[评估结果](evals/results.md)。

## 怎么用？

安装到 Codex 后：

```text
用 $dialectic 反驳并优化我的想法：
我想做一个 AI 学习规划助手。
限制：一个人，两周，不使用付费基础设施。
保留值得做的部分，允许驳回不成立的批评。
最后告诉我下一步做什么，做到什么程度算通过。
```

Claude Code 使用 `/dialectic`。也可以把 Skill 核心和协议文件一起交给其他助手，让它按规则评审；这属于手动使用，不能叫自动安装成功。

## 重要规则

- 默认最多三轮，每轮最多三个新问题，允许零问题。
- 先固定目标与约束，不把你的项目悄悄改成另一个项目。
- 批评可以接受、部分接受、驳回或等待证据。
- 已解决问题没有新证据就不重开；未解决问题必须复查。
- 修改方案不等于已经验证性能、实际成本或市场需求。
- 不为满足批评者而堆功能，不替你接受风险。
- 明确停止原因；剩余不确定性可以转成下一步验证任务。

## 最后会得到什么？

1. 优化后的建议或方案。
2. 重要修改及原因。
3. 还没解决的问题。
4. 下一步最小行动与验收标准。
5. 本次轮数与停止原因。

默认不输出长篇角色辩论。需要时可以说“给我完整问题记录”，再用它续接下一次评审。

## 项目内容

| 内容 | 入口 |
| --- | --- |
| Skill 核心 | [SKILL.md](skills/dialectic/SKILL.md) |
| 详细状态和停止规则 | [protocol.md](skills/dialectic/references/protocol.md) |
| Windows / macOS / Linux 安装 | [installation.md](docs/installation.md) |
| 产品、技术、学习计划三个完整示例 | [examples](examples/README.md) |
| 测试案例、评分标准、原始试用记录 | [evals](evals/README.md) |
| 已有项目与定位边界 | [related-work.md](docs/related-work.md) |
| GitHub 发布步骤 | [publishing.zh-CN.md](docs/publishing.zh-CN.md) |

## 检查项目

Python 3.10+，无需额外依赖：

```bash
python tools/check_repo.py
python -m unittest discover -s tests -v
```

检查通过只说明文件结构、引用、评估记录完整性等通过；不代表模型效果优于其他方法。

## 已知限制

它依赖模型遵守规则，不能保证绝不重复、绝不误判。单模型分步骤评审不等于多个独立专家。跨会话记录需要显式提供；默认轮数是提示规则，不是程序强制限制。

适合先从低风险的想法与方案评审开始，用实际案例继续打磨。

MIT 开源许可，见 [LICENSE](LICENSE)。欢迎按[贡献指南](CONTRIBUTING.md)提交失败案例。
