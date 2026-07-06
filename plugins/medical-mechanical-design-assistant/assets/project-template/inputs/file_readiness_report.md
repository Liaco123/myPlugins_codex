# 文件可处理性报告

运行以下命令生成或更新：

```powershell
python scripts\check_asset_readiness.py <项目文件夹>
```

## 分类说明

- 可直接读取：文本、Markdown、CSV、JSON 等。
- 可处理但需提取：PDF、Office、Excel 等。
- 可视觉分析：图片。
- 需预处理：视频和录音。
- CAD 优先格式：STEP/STP/STL。
- CAD 可参考：DXF/DWG/OBJ/IGES/Parasolid，需补单位和用途。
- 需要转换：SolidWorks、Creo、CATIA、Inventor 等原生格式。
- 未知或不推荐：需要说明来源、用途和打开方式。
