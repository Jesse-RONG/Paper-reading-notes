# 📚 每日论文阅读笔记

每天读一点论文，用 Jupyter Notebook 记录：**理解总结 + 公式推导 + 小型数值实验**。

## 📁 目录结构

```
每日论文阅读/
├── README.md                  # 本文件（含阅读索引）
├── templates/
│   └── paper_note_template.ipynb   # 笔记模板
├── new_note.py                # 一键生成当天笔记
├── requirements.txt
└── 7.18SGD C+H/               # 每天一个文件夹：日期 + 主题
    ├── xxx.pdf                # 当天读的论文
    └── note.ipynb             # 当天的笔记
```

## 🚀 使用方法

新建一天的笔记（自动建文件夹并复制模板）：

```bash
py new_note.py "SGD噪声协方差"
# 生成 7.18SGD噪声协方差/note.ipynb
```

也可以手动把 `templates/paper_note_template.ipynb` 复制到当天文件夹里改名。

## 📝 笔记模板包含

- **元信息**：标题 / 作者 / 链接 / 标签 / 推荐指数
- **TL;DR**：一句话总结
- **三个问题**：WHY（动机）/ HOW（方法）/ WHAT（结论）
- **核心思想与主要结论**：关键定理 + 直觉
- **公式推导**：比论文更细的推导，写给未来的自己
- **数值实验**：小实验验证论文结论（固定随机种子可复现）
- **疑问与思考** & **延伸阅读**

## 📖 阅读索引

| 日期 | 主题 | 论文 | 笔记 |
| --- | --- | --- | --- |
| 2026-07-18 | SGD 噪声 / 损失景观 | SGD Noise Covariance; WSD Learning Rates; Saddle Point Problem | [7.18SGD C+H](./7.18SGD%20C+H/) |
| 2026-07-15 | 优化 / Barron 空间 / 高维概率 | Barron Space and Flow-Induced Functions; Functional Scaling Laws in Kernel Regression | [7.15](./7.15优化一篇barron一篇高维概率一章/) |

> 每天读完后在上表加一行，最新的放最上面。
