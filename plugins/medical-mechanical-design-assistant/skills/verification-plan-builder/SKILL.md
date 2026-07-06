---
name: verification-plan-builder
description: Build measurable verification plans for medical or laboratory automation方案, process steps, external mechanisms, workflow records, risk controls, and 2D/flowchart assumptions. Use when Codex needs to turn方案, step tables, risks, or tests into verifiable items with methods, data, pass criteria, owners, and gate status.
---

# Verification Plan Builder

默认使用中文输出，除非用户明确要求其他语言。验证计划必须能由工程师、工艺人员或测试人员执行。

## 必要输入

优先读取：

- `outputs/design_input.md`
- `outputs/concept_options.md`
- `outputs/risk_review.md`
- `outputs/process_view.html`
- `inputs/workflow_steps.md`
- `inputs/dimensions.md`
- `inputs/safety_and_risk_boundaries.md`
- `inputs/source_log.md`
- `inputs/cad_index.md`
- `inputs/video_index.md`
- `inputs/audio_index.md`

资料不足时，输出待补资料和验证阻塞项，不要虚构通过标准。

## 验证对象

每个验证项必须至少关联以下之一：

- 工艺步骤。
- 操作主体。
- 操作对象。
- 外部机构或系统接口。
- 风险点或控制措施。
- 数据记录/追溯点。
- 流程图或二维 HTML 展示中的关键假设。

## 验证项字段

每个验证项必须包含：

- Requirement or risk link。
- Step ID。
- 操作主体、操作对象、外部机构。
- 需要测量或观察什么。
- 方法和测试设置。
- 所需工具、夹具、样本或资料。
- 样本量或重复次数。
- 记录数据。
- 可量化接受标准。
- 失败处理。
- Owner。
- Status。
- 资料来源和证据等级。

避免“运行稳定”“效果良好”等模糊标准。转成时间、体积、位置误差、成功率、重复次数、缺陷判定、污染标准、记录完整率或人工确认标准。

## 输出

创建或更新 `outputs/verification_plan.md`：

```markdown
# 验证计划

## 范围
## 假设与资料缺口
## 验证矩阵
## 步骤级验证覆盖
## 外部机构与接口验证
## 数据记录与追溯验证
## 测试设置
## 所需工具、样本与夹具
## 数据记录模板
## Gate 5 准入结论
## Action Packages
```

验证矩阵字段：ID, Step ID, requirement/risk link, 操作主体, 操作对象, 外部机构, method, setup, tool, repetitions, data record, acceptance criteria, evidence source, owner, status。

## Gate 5 通过标准

Gate 5 只有在所有高优先级风险都有验证项、每个关键工艺步骤都有可量化接受标准、外部机构/接口有验证方法、资料缺口被解决或被工程负责人明确接受为风险后，才能通过。

## 确定性检查

项目文件夹存在时，运行：

```powershell
python scripts\check_gate.py <project-folder> --gate 5
```

脚本只检查结构覆盖，不替代工程评审。
