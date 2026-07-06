---
name: design-input-builder
description: Build a structured solution-design input package for medical, laboratory, production, or small-scale automation projects. Use when Codex needs to organize evidence, process requirements, constraints, interfaces, step definitions, missing inputs, maturity level, scoring criteria, and gate readiness before solution generation.
---

# Design Input Builder

默认使用中文输出，除非用户明确要求其他语言。AI 负责整理、追问和起草，不作为工程批准人。

## 工作流

1. 检查项目文件夹和输入资料：
   - `inputs/project_brief.md`
   - `inputs/equipment_list.md`
   - `inputs/material_list.md`
   - `inputs/workflow_steps.md`
   - `inputs/photos/`
   - `inputs/videos/`
   - `inputs/manuals/`
   - `inputs/meeting_notes/`
   - `inputs/dimensions.md`
   - `inputs/cad_index.md`
   - `inputs/video_index.md`
   - `inputs/audio_index.md`
   - `inputs/source_log.md`
   - `inputs/safety_and_risk_boundaries.md`
   - `inputs/existing_issues.md`
   - `inputs/interfaces.md`
2. 如果输入包不足，先使用 `$project-intake-guide` 索要资料并分类，不要硬生成方案。
3. 创建或更新 `outputs/design_input.md`，必须区分事实、假设、决策、缺口。
4. 给出当前方案成熟度，并说明为什么停在该等级。

## 方案成熟度

| 等级 | 名称 | 允许输出 | 不允许输出 |
| --- | --- | --- | --- |
| S0 | 资料接收 | 资料分类、缺口清单、下一轮追问 | 流程承诺、方案推荐 |
| S1 | 流程拆解 | 初版步骤表、主体/对象/输入输出、初版流程图 | 方案定型、成本/节拍承诺 |
| S2 | 方案比较 | 多方案、步骤评分、方案级评分、风险初评 | 工程细节冻结 |
| S3 | 展示评审 | 二维 HTML 三视图、客户/内部评审包、待确认清单 | 作为施工图或最终验证结论 |
| S4 | 验证准备 | 验证矩阵、测试设置、接受标准、责任人 | 替代工程批准 |

资料不足时，输出应停在较低等级，并明确需要哪些资料才能进入下一等级。

## 工艺步骤定义

每个步骤必须尽量定义下列字段；缺失字段要列入“待补资料”，不能默认为已知：

| 字段 | 含义 |
| --- | --- |
| Step ID | 步骤编号 |
| 工艺目的 | 这一步为什么存在 |
| 操作主体 | 人、机器人、固定设备、外部机构、软件系统或待定 |
| 操作对象 | 样本、耗材、容器、设备部件、数据记录等 |
| 输入 | 进入该步骤的物料、状态、信息 |
| 输出 | 完成后的物料、状态、信息 |
| 外部机构/系统 | 夹具、开盖器、转运台、扫码器、泵阀、过滤模块、输送线、工具站、LIMS/MES 等 |
| 关键参数 | 尺寸、力、时间、温度、体积、节拍、精度、清洁要求等 |
| 判定/记录 | 成功判定、记录字段、追溯要求 |
| 风险点 | 污染、错拿、泄漏、卡滞、碰撞、误判、样本损失等 |
| 评分 | 可行性、风险等级、资料置信度、自动化优先级 |

## 输出结构

`outputs/design_input.md` 应包含：

```markdown
# 方案设计输入

## 项目背景
## 方案成熟度
## 工艺目标与成功标准
## 当前人工/现有流程
## 工艺步骤表
## 操作主体与对象清单
## 外部机构与系统接口清单
## 场地、设备、耗材与数据接口
## 已知参数与缺失参数
## 约束与不可改变边界
## 安全、污染、样本完整性边界
## 评分口径
## 假设锁定与变更记录
## 事实、假设与决策
## 资料来源摘要
## 待补资料与追问
## Gate 0 准入结论
## Action Packages
```

## 确定性检查

项目文件夹存在时，运行：

```powershell
python scripts\check_inputs.py <project-folder> --level <1|2|3>
```

脚本结果用于辅助判断，不替代方案评审。
