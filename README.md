# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-21.md)

*最后自动更新时间: 2026-01-21 18:21:14*
## 1. Show HN：ChartGPU —— 基于 WebGPU 的图表库（60fps 下渲染 100 万个点）

**原文标题**: Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)

**原文链接**: [https://github.com/ChartGPU/ChartGPU](https://github.com/ChartGPU/ChartGPU)

**ChartGPU** 是一款基于 TypeScript 的高性能图表库，利用 **WebGPU** 技术，旨在以 60fps 的帧率渲染多达一百万个数据点。它专为需要对大规模数据集进行流畅交互式可视化的应用而构建，解决了传统 SVG 或 Canvas 库经常遇到的性能瓶颈。

**核心特性与功能：**
*   **丰富的图表类型：** 支持多种序列，包括折线图、面积图、柱状图、散点图、饼图以及金融 K 线图 (OHLC)。
*   **交互与工具：** 内置支持 X 轴缩放（通过手势或滑块）、工具提示、悬停高亮和十字光标。它还提供同步 API，用于联动多个图表实例之间的交互。
*   **实时数据：** 通过 `appendData` 方法针对流式更新进行了优化，非常适合实时数据监控。
*   **自定义：** 提供浅色和深色主题预设，并支持自定义主题。

**架构与集成：**
该库采用模块化架构，通过“渲染协调器”管理 GPU 生命周期、布局和数据缓冲。它为每种序列类型使用专门的 **WGSL 着色器**，以确保最大程度的硬件加速。对于使用现代框架的开发者，提供专用的 React 封装库 (`chartgpu-react`) 以实现无缝集成。

**浏览器支持与

ChartGPU 采用 **MIT 许可证** 开源，为 Web 端的高频或大规模数据可视化提供了一个稳健且开发者友好的解决方案。

---

## 2. JPEG XL Demo Page

**原文标题**: JPEG XL Demo Page

**原文链接**: [https://tildeweb.nl/~michiel/jxl/](https://tildeweb.nl/~michiel/jxl/)

本演示页面用于 JPEG XL 图像格式的兼容性测试。截至 2026 年 1 月，作者指出 Safari 是唯一预计将支持并显示该图像的主流浏览器。示例测试图像展示了 Jon Sneyers，他是 JPEG XL 规范的共同作者，也是前代自由无损图像格式 (FLIF) 的创造者。

---

## 3. SmartOS

**原文标题**: SmartOS

**原文链接**: [https://docs.smartos.org/](https://docs.smartos.org/)

生成摘要时出错

---

## 4. PicoPCMCIA – a PCMCIA development board for retro-computing enthusiasts

**原文标题**: PicoPCMCIA – a PCMCIA development board for retro-computing enthusiasts

**原文链接**: [https://www.yyzkevin.com/picopcmcia/](https://www.yyzkevin.com/picopcmcia/)

生成摘要时出错

---

## 5. Skip 现已免费并开源

**原文标题**: Skip Is Now Free and Open Source

**原文链接**: [https://skip.dev/blog/skip-is-free/](https://skip.dev/blog/skip-is-free/)

截至2026年1月21日，随着1.7版本的发布，Skip已转型为完全免费且开源的模式。此举取消了开发者和企业之前的所有许可要求、订阅费用和许可证密钥。

**关键变化：**
*   **开源：** 核心引擎“skipstone”现已在GitHub上公开。该工具负责Swift/SwiftUI到Kotlin/Jetpack Compose的关键转译、项目管理和应用打包。
*   **新主页：** 项目推出了 **skip.dev**，这是一个全新的开源网站，用于文档查阅和社区贡献。
*   **可持续发展模式：** 作为一家此前没有外部投资、依靠自筹资金运作的公司，Skip正从强制付费模式转向自愿付费模式。该项目目前通过面向个人的 **GitHub Sponsors** 和面向企业的 **分级企业赞助** 来获取资金支持。

**动机：**
创始人意识到，开发者期望使用免费工具，且往往对在小公司的闭源付费平台上构建应用持谨慎态度，以规避“项目停摆（rug pull）”的风险。通过将底层技术开源，Skip确保了技术的持久性；即使核心团队不复存在，社区仍能继续维护代码库。

**愿景：**
Skip的使命始终专注于提供“不妥协”的跨平台体验。与往往导致UI陈旧的传统框架不同，Skip允许开发者利用单一的Swift代码库，为iOS和Android生成真正的原生应用。通过消除成本障碍，Skip旨在实现大规模普及，并直接与第一方IDE及成熟的跨平台工具展开竞争。

---

## 6. Markdown 嵌套代码块

**原文标题**: Nested Code Fences in Markdown

**原文链接**: [https://susam.net/nested-code-fences.html](https://susam.net/nested-code-fences.html)

生成摘要时出错

---

## 7. 搜索破晓：搜索索引、谷歌裁决及其对 Kagi 的影响

**原文标题**: Waiting for dawn in search: Search index, Google rulings and impact on Kagi

**原文链接**: [https://blog.kagi.com/waiting-dawn-search](https://blog.kagi.com/waiting-dawn-search)

In this January 2026 blog post, Kagi analyzes the evolving search landscape following the 2024 ruling that declared Google a monopolist. Kagi argues that Google’s control over 90% of the web index creates an "innovation crunch" that extends beyond search into AI, as LLMs require search indexes for real-world grounding.

Kagi highlights the immense difficulty of competing in this market, noting that even Microsoft’s $100 billion investment in Bing resulted in only single-digit market share. Furthermore, Kagi describes its own struggle to secure direct, fair licensing: Microsoft retired its Bing Search APIs in 2025, and Google lacks a viable API that doesn't force ad-syndication. This has forced Kagi and other major entities to rely on third-party API providers—a "back door" that Google is now attempting to close through litigation.

The post expresses optimism regarding the DOJ’s late-2025 remedies, which include:
*   **Mandatory syndication:** Google must offer search results to competitors on fair terms.
*   **No ad-bundling:** Competitors can access results without being forced to use Google Ads.
*   **Marginal-cost access:** Google must provide index data (URLs and metadata) at a fair price.

Kagi envisions a future "layered search ecosystem" consisting of a taxpayer-funded public search (similar to public libraries), free ad-supported search, and premium subscription services like Kagi. By transforming the search index from a private chokepoint into shared infrastructure, Kagi believes the market can finally move toward healthy competition. The company remains committed to its ad-free, multi-source model, positioning itself to transition from "gray-market workarounds" to legitimate, contractual access once the court's remedies are fully enforced.

---

## 8. Autonomous (YC F25) is hiring – AI-native financial advisor at 0% advisory fees

**原文标题**: Autonomous (YC F25) is hiring – AI-native financial advisor at 0% advisory fees

**原文链接**: [https://atg.science/](https://atg.science/)

生成摘要时出错

---

## 9. Can you slim macOS down?

**原文标题**: Can you slim macOS down?

**原文链接**: [https://eclecticlight.co/2026/01/21/can-you-slim-macos-down/](https://eclecticlight.co/2026/01/21/can-you-slim-macos-down/)

生成摘要时出错

---

## 10. EU–INC – A new pan-European legal entity

**原文标题**: EU–INC – A new pan-European legal entity

**原文链接**: [https://www.eu-inc.org/](https://www.eu-inc.org/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 2 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 3 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 4 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 5 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 6 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 7 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 8 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 9 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 10 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 11 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 12 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 13 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 14 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 15 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 16 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 17 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 18 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 19 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 20 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 21 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 22 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 23 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 24 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 25 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 26 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 27 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 28 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 29 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 30 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 31 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 32 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 33 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 34 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 35 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 36 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 37 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 38 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 39 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 40 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 41 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 42 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 43 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 44 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 45 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 46 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 47 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 48 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 49 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 50 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 51 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 52 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 53 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 54 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 55 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 56 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 57 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 58 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 59 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 60 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 61 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 62 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 63 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 64 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 65 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 66 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 67 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 68 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 69 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 70 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 71 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 72 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 73 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 74 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 75 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 76 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 77 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 78 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 79 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 80 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 81 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 82 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 83 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 84 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 85 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 86 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 87 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 88 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 89 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 90 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 91 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 92 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 93 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 94 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 95 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 96 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 97 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 98 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 99 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 100 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 101 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 102 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 103 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 104 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 105 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 106 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 107 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 108 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 109 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 110 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 111 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 112 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 113 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 114 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 115 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 116 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 117 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 118 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 119 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 120 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 121 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 122 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 123 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 124 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 125 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 126 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 127 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 128 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 129 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 130 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 131 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 132 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 133 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 134 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 135 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 136 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 137 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 138 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 139 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 140 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 141 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 142 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 143 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 144 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 145 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 146 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 147 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 148 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 149 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 150 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 151 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 152 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 153 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 154 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 155 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 156 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 157 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 158 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 159 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 160 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 161 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 162 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 163 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 164 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 165 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 166 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 167 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 168 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 169 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 170 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 171 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 172 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 173 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 174 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 175 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 176 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 177 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 178 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 179 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 180 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 181 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 182 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 183 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 184 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 185 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 186 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 187 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 188 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 189 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 190 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 191 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 192 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 193 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 194 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 195 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 196 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 197 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 198 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 199 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 200 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 201 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 202 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 203 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 204 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 205 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 206 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 207 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 208 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 209 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 210 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 211 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 212 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 213 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 214 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 215 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 216 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 217 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 218 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 219 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 220 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 221 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 222 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 223 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 224 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 225 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 226 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 227 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 228 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 229 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 230 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 231 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 232 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 233 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 234 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 235 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 236 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 237 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 238 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 239 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 240 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 241 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 242 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 243 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 244 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 245 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 246 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 247 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 248 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 249 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 250 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 251 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 252 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 253 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 254 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 255 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 256 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 257 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 258 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 259 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 260 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 261 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 262 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 263 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 264 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 265 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 266 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 267 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 268 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 269 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 270 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 271 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 272 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 273 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 274 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 275 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 276 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 277 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 278 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 279 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 280 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 281 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 282 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 283 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 284 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 285 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 286 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 287 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 288 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 289 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 290 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 291 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 292 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 293 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 294 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 295 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 296 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 297 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 298 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 299 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 300 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 301 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 302 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 303 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 304 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 305 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 306 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 307 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
