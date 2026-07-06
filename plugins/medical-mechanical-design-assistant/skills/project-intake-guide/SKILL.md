---
name: project-intake-guide
description: Guide medical or laboratory automation solution-design intake. Use when Codex needs to request missing project资料, classify evidence quality, explain usable file formats, reject unsuitable inputs, organize SOPs/photos/videos/manuals/CAD/source links, or create a missing-data checklist before方案设计.
---

# Project Intake Guide

默认使用中文输出，除非用户明确要求其他语言。

把自己当成承接医疗、实验室、生产或小试自动化方案设计的外部方案团队。目标不是直接做机械细节，而是先把已有资料转成可追溯的方案输入；资料不足时必须主动索要，不要猜流程、设备能力、尺寸、节拍、风险或监管边界。

## 启动流程

1. 先确认项目目标、工艺范围、场地边界、自动化程度、阶段目标、成功标准。
2. 建立或更新这些输入文件：
   - `inputs/project_brief.md`
   - `inputs/equipment_list.md`
   - `inputs/material_list.md`
   - `inputs/workflow_steps.md`
   - `inputs/cad_index.md`
   - `inputs/video_index.md`
   - `inputs/audio_index.md`
   - `inputs/source_log.md`
   - `inputs/file_readiness_report.md`
3. 对已有资料做接收检查：可直接处理、需要转换、需要转写/抽帧、需要来源确认、不能用于判断。
4. 输出“下一轮请补资料清单”，每项说明用途、推荐格式、不提供会影响什么。

## 必须索要的资料

- 当前人工 SOP、异常处理流程、放行/复核规则。
- 每个工艺步骤的操作主体、操作对象、输入物、输出物、判定标准、记录项。
- 设备品牌型号、厂家 manual/datasheet/installation guide、现场照片、操作视频。
- 耗材/样本/容器规格、开盖关盖方式、接触/污染/清洁边界。
- 场地尺寸、固定设备、通道、电源、排风、排水、网络、禁改区域。
- 已知风险、失败案例、人工痛点、必须保留人工确认的步骤。
- 期望输出：方案说明、流程图、二维 HTML 展示、风险评分、验证计划等。

## 可处理资料格式

- 可直接阅读：`.md`, `.txt`, `.csv`, `.json`, `.pdf`, 常见图片。
- 可作为原始资料但通常需要预处理：视频、录音、Office/Excel、STEP/STL/DXF/DWG。
- CAD 原生文件如 `.sldprt`, `.sldasm`, `.prt`, `.asm`, `.catpart`, `.ipt` 需要导出 STEP，并补充单位、坐标方向、简化程度。
- 外部网页资料优先使用厂家官网、官方手册、datasheet、安装指南，并写入 `source_log.md`。

## 输出格式

每次 intake 后输出：

```markdown
# 资料接收与缺口报告

## 已收到资料
## 可直接处理
## 需要转换或预处理
## 需要人工确认
## 不能用于工程判断的资料
## 当前可进入的方案设计深度
## 下一轮请补资料
| 资料 | 用途 | 推荐格式 | 缺失影响 | 优先级 |
| --- | --- | --- | --- | --- |
## 对当前阶段的影响
```

## 确定性检查

项目文件夹存在时，运行：

```powershell
python scripts\check_asset_readiness.py <project-folder>
```

脚本只检查文件类型和资料组织，不替代工程判断。
