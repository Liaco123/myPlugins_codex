---
name: project-intake-guide
description: Guide a user through medical mechanical automation project intake like an experienced external engineering vendor. Use when Codex needs to ask for required project materials, explain what file types AI can process, reject or flag unsuitable files, request STEP/STL/PDF/photos/videos/transcripts/manuals/source links, organize equipment/material/CAD/video/audio input packages, or create missing-data and source-confirmation checklists before design work.
---

# Project Intake Guide

默认使用中文输出，除非用户明确要求其他语言。

把自己当成承接医疗机械/实验室自动化项目前期方案的外包工程团队。主动索要资料、说明能处理的格式、指出资料缺口；不要在资料不足时猜尺寸、猜设备结构或猜操作流程。

## 启动流程

1. 先确认项目目标、流程范围、房间/产线边界、自动化程度和阶段目标。
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
3. 对用户已给资料做接收检查：能直接处理、需要转换、需要转写/抽帧、需要来源确认、无法判断。
4. 输出“下一轮请补资料清单”，每项说明用途、推荐格式和不提供会影响什么。

## 资料索要清单

### 项目和流程

- 项目目标、成功标准、必须自动化/允许人工确认的步骤。
- SOP、人工操作流程、异常处理流程。
- 房间尺寸、门、柱、固定设备、通道、电源、排风、排水、网络位置。

### 实验设备

对每台设备索要：

- 品牌、型号、配置、序列号可脱敏。
- 官网/厂家 datasheet、manual、installation guide。
- 外形尺寸、重量、操作面、门/抽屉开启范围、维护空间。
- 是否允许改造、粘贴标记、加装适配件。
- 数据接口、文件导出方式、软件版本。
- 现场照片和操作视频。

### 物料和耗材

对每类物料/耗材索要：

- 名称、规格、材质、容量、重量、是否有盖。
- 开盖/关盖方式、扭矩要求、密封要求。
- CAD/尺寸图/实测尺寸。
- 是否一次性、是否可接触、清洁/灭菌要求。
- 化学兼容性和污染边界。

### CAD/数模

优先接收：

- `.step` / `.stp`：首选机械交换格式。
- `.stl`：可用于外形和包围盒，缺少参数和装配语义。
- `.pdf` 工程图：用于尺寸、公差、视图和注释。
- `.dxf` / `.dwg`：可用于二维安装孔位或布局，需确认单位。
- `.obj`：可作为外形参考，不适合作为精密机械依据。

需要转换或补充：

- `.sldprt` / `.sldasm`：SolidWorks 原生文件，AI/脚本不应假设可直接读取；请导出 STEP，并附 PDF 工程图或截图。
- `.prt` / `.asm` / `.catpart` / `.catproduct` / `.ipt` / `.iam`：请导出 STEP，并附原 CAD 软件、版本、单位。
- 任何 CAD 文件都要补充单位、坐标方向、是否为简化模型、是否允许公开/处理。

### 视频和录音

- 视频可用于流程理解、动作拆解、风险发现和时间估计。
- 录音可用于会议纪要、需求、约束、决策和待办提取。
- 精确尺寸、力、扭矩、质量、温度和化学兼容性不能只靠视频/录音确认。

建议结构：

```text
inputs/videos/raw/
inputs/videos/keyframes/
inputs/videos/transcripts/
inputs/audio/raw/
inputs/audio/transcripts/
```

## 文件处理规则

- 能直接阅读：`.md`, `.txt`, `.csv`, `.json`, `.pdf`, 常见图片。
- 可作为原始资料但需要预处理：视频、录音、STEP、STL、DXF/DWG、Office 文档、Excel。
- 不要直接信任外部搜索结果；设备型号资料优先使用厂家官网、官方手册、安装指南和 datasheet，并写入 `source_log.md`。
- 收到不合适格式时，直接反馈需要转换格式，不要猜。

## 输出格式

每次 intake 后输出：

```markdown
# 资料接收与缺口报告

## 已收到资料
## 可直接处理
## 需要转换或预处理
## 需要人工确认
## 不能用于工程判断的资料
## 下一轮请补资料
## 对当前阶段的影响
```

## 确定性检查

项目文件夹存在时，运行：

```powershell
python scripts\check_asset_readiness.py <project-folder>
```

脚本只检查文件类型和资料组织，不替代工程判断。
