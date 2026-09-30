# Usage patterns / 使用方式

Submit an idea plus the constraints that matter. You do not need to know the internal English status names.

## Start a review

```text
用 dialectic 评审这个想法：[想法]
目标：[想得到什么]
限制：[时间、预算、能力或不可改变的条件]
优先判断：[例如能不能在两周内做出演示]
```

Missing details become explicit assumptions unless they would materially change the recommendation. The assistant should not ask a questionnaire before helping.

## Short review

```text
只做一轮，最多两个关键问题，最后给一个最小行动。
```

A round is critique, adjudication, revision, and verification. Three rounds is a default maximum, not a minimum and not three guaranteed API calls.

## Resume

```text
继续使用 dialectic。下面是上一版方案和问题记录：
[粘贴记录]
这是新方案及修改依据：[内容]
先核查旧问题，再检查这次修改引入的问题。
```

Without the earlier record the assistant cannot reliably know what was closed. It should request the missing relevant context.

## Change a constraint

```text
我明确把预算从 100 调整到 200，其他要求不变。
请更新目标记录，只重查受这个变化影响的问题。
```

User-approved changes version the brief. A reviewer suggestion does not have the same authority.

## Request an audit

```text
给我完整问题记录：编号、依据、裁决、验收条件、当前状态、变化原因。
```

This exposes decision summaries and evidence, not a hidden reasoning transcript.

## Interpreting the result

| Label | Meaning / 下一步 |
| --- | --- |
| ready-for-next-step | 当前范围内已完成相关检查；按建议进入下一步，不等于保证成功 |
| needs-evidence | 补资料、运行实验或核算；还不能确认关键结论 |
| needs-user-decision | 要你选择真实权衡，不能替你放松硬约束 |
| stalled | 继续讨论没有实质进展，换成具体实验或缩小问题 |
| budget-reached | 本次轮数已用完，仍然列出未解决事项 |

For a factual question with a direct answer, ask it directly. For a decision already made and ready to execute, this Skill need not start another debate.
