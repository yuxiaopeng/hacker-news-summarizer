# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-23.md)

*最后自动更新时间: 2026-06-23 19:40:47*
## 1. 杰瑞的地图

**原文标题**: Jerry's Map

**原文链接**: [http://www.jerrysmap.com/the-map](http://www.jerrysmap.com/the-map)

《杰里的地图》（Jerry’s Map）是由杰里·格雷辛格（Jerry Gretzinger）于1963年启动的一项宏大且不断演进的艺术项目。最初只是对一座虚构城市的涂鸦，如今已演变成一个庞大的“虚拟世界”，由4,000多块8×10英寸的独立画板组成。这些画板按坐标排列，组装后构成一个近似的圆。在1983年至2003年经历了20年的中断后，该项目得以重启，目前作为一个复杂的、基于规则的系统运行。

其创作过程由一套约100张定制的指令卡主导。这些卡片规定了地图演变的方方面面，包括工作量（以“工作单位”衡量）、进展方向（顺时针或逆时针），以及绘画、拼贴或生成新画板等具体任务。地图永远没有“终点”，而是以连续的图层形式存在。画板会经历不同的阶段，从基础的上色和城市密度演变为更抽象的维度，如“虚空”、“红色维度”和“洪水”。

该项目分为两个截然不同的阶段。第一阶段（1963–1983年）的特点是写实的手绘地形特征和手工记录。第二阶段（2003年至今）引入了数字工具、电子表格和更抽象的美学风格。在当前的阶段，格雷辛格往往将自己视为观察者而非主导者，遵循着卡组的“意志”。在负责扫描和存档的“助手”的协助下，该地图已从个人爱好转型为在博物馆展出的著名艺术装置，并得到了专门在线社区的支持。它始终是一个充满生命力的、自我延续的系统，在不断的修订中持续生长。

---

## 2. Swift Package Index 加入苹果

**原文标题**: Swift Package Index joins Apple

**原文链接**: [https://swiftpackageindex.com/blog/swift-package-index-joins-apple](https://swiftpackageindex.com/blog/swift-package-index-joins-apple)

Swift Package Index (SPI) 是一个用于发现和评估 Swift 软件包的关键社区驱动资源，现已正式加入 Apple。

该平台由 Dave Verwer 和 Sven A. Schmidt 创立，最初是一个旨在帮助开发者探索日益壮大的 Swift 库生态系统的业余项目。此次并入 Apple 旨在通过提供 Swift 语言背后公司的正式支持和资源，确保该服务的长期可持续性与发展。

公告的关键点包括：

*   **团队过渡：** 两位创始人 Verwer 和 Schmidt 都将作为全职员工加入 Apple，继续负责该索引的开发工作。
*   **使命延续：** 核心目标保持不变，即为 Swift 软件包提供全面、高质量的搜索和元数据引擎，帮助开发者做出明智的决策。
*   **开源承诺：** 该项目将保持开源，团队计划继续与开发者社区保持透明且协作的工作模式。
*   **稳定性：** 此举保障了这一许多开发者日常工作所依赖的工具的未来，使其从社区资助模式转变为 Apple 开发者工具基础设施的永久组成部分。

创始人表示，加入 Apple 是扩展该平台并随着 Swift 生态系统在不同平台持续扩张而更好地服务于该生态系统的最佳途径。

---

## 3. 三级方程式

**原文标题**: F3

**原文链接**: [https://github.com/future-file-format/f3](https://github.com/future-file-format/f3)

**F3 (面向未来的文件格式)** 是一种下一代开源列式存储格式，旨在通过解决 Parquet 和 ORC 等陈旧格式的局限性，推动数据分析的现代化。F3 由包括 Wes McKinney 和 Andrew Pavlo 在内的行业领袖所组成的科研团队创建，旨在为现代硬件和工作负载提供一个更高效、互操作性更强且更具扩展性的替代方案。

F3 的核心创新在于直接在数据文件中嵌入 **WebAssembly (Wasm) 解码器**。这种“用户定义编码”（UDE）方法允许开发人员轻松引入新的编码方案。由于解码数据的逻辑与数据本身封装在一起，F3 确保了通用的兼容性，并使其格式具有“面向未来”的特性；即使在没有原生解码器的情况下，任何系统都可以通过内置的 Wasm 二进制文件读取文件。

关键特性和细节包括：
*   **效率与布局：** 纠正了上一代格式的结构性缺陷，以优化在现代硬件上的性能。
*   **自描述特性：** 每个文件都包含数据、元数据以及解码所需的 Wasm 二进制文件，仅增加极小的存储开销（以 KB 计）。
*   **研究状态：** 目前仍处于研究原型阶段，尚未用于生产环境。该项目使用 Rust 语言实现，并采用 FlatBuffers 进行格式定义。
*   **学术验证：** 详见 2025 年发表在《ACM 数据管理学会会刊》（Proceedings of the ACM on Management of Data）上的一篇论文。研究表明，F3 在存储布局效率和解码灵活性方面均优于传统格式。

该项目采用 MIT 许可证，目前仍是数据互操作性未来发展的一个活跃研究领域。

---

## 4. Show HN: TikZ Editor – LaTeX 绘图所见即所得编辑器

**原文标题**: Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

**原文链接**: [https://tikz.dev/editor/](https://tikz.dev/editor/)

生成摘要时出错

---

## 5. Unlimited OCR: One-shot long-horizon parsing

**原文标题**: Unlimited OCR: One-shot long-horizon parsing

**原文链接**: [https://github.com/baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

生成摘要时出错

---

## 6. San Diego photologs from the 1970s

**原文标题**: San Diego photologs from the 1970s

**原文链接**: [https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/](https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/)

生成摘要时出错

---

## 7. The truth about being a manager

**原文标题**: The truth about being a manager

**原文链接**: [https://sofiakodar.github.io/posts/becomingmanager/](https://sofiakodar.github.io/posts/becomingmanager/)

生成摘要时出错

---

## 8. Five monitors on a Commodore 128 [video]

**原文标题**: Five monitors on a Commodore 128 [video]

**原文链接**: [https://www.youtube.com/watch?v=ul5hC3PY1Yg](https://www.youtube.com/watch?v=ul5hC3PY1Yg)

生成摘要时出错

---

## 9. Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文标题**: Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文链接**: [https://lift4d.github.io/](https://lift4d.github.io/)

生成摘要时出错

---

## 10. The Coming Loop

**原文标题**: The Coming Loop

**原文链接**: [https://lucumr.pocoo.org/2026/6/23/the-coming-loop/](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 2 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 3 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 4 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 5 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 6 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 7 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 8 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 9 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 10 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 11 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 12 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 13 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 14 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 15 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 16 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 17 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 18 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 19 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 20 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 21 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 22 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 23 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 24 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 25 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 26 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 27 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 28 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 29 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 30 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 31 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 32 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 33 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 34 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 35 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 36 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 37 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 38 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 39 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 40 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 41 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 42 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 43 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 44 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 45 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 46 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 47 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 48 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 49 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 50 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 51 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 52 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 53 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 54 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 55 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 56 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 57 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 58 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 59 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 60 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 61 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 62 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 63 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 64 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 65 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 66 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 67 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 68 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 69 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 70 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 71 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 72 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 73 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 74 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 75 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 76 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 77 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 78 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 79 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 80 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 81 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 82 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 83 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 84 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 85 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 86 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 87 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 88 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 89 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 90 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 91 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 92 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 93 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 94 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 95 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 96 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 97 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 98 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 99 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 100 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 101 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 102 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 103 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 104 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 105 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 106 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 107 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 108 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 109 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 110 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 111 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 112 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 113 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 114 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 115 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 116 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 117 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 118 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 119 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 120 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 121 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 122 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 123 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 124 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 125 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 126 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 127 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 128 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 129 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 130 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 131 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 132 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 133 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 134 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 135 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 136 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 137 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 138 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 139 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 140 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 141 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 142 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 143 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 144 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 145 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 146 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 147 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 148 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 149 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 150 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 151 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 152 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 153 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 154 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 155 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 156 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 157 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 158 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 159 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 160 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 161 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 162 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 163 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 164 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 165 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 166 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 167 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 168 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 169 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 170 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 171 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 172 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 173 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 174 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 175 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 176 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 177 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 178 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 179 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 180 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 181 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 182 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 183 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 184 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 185 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 186 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 187 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 188 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 189 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 190 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 191 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 192 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 193 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 194 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 195 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 196 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 197 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 198 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 199 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 200 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 201 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 202 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 203 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 204 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 205 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 206 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 207 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 208 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 209 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 210 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 211 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 212 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 213 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 214 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 215 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 216 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 217 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 218 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 219 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 220 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 221 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 222 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 223 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 224 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 225 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 226 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 227 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 228 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 229 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 230 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 231 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 232 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 233 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 234 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 235 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 236 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 237 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 238 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 239 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 240 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 241 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 242 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 243 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 244 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 245 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 246 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 247 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 248 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 249 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 250 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 251 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 252 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 253 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 254 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 255 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 256 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 257 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 258 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 259 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 260 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 261 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 262 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 263 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 264 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 265 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 266 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 267 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 268 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 269 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 270 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 271 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 272 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 273 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 274 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 275 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 276 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 277 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 278 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 279 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 280 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 281 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 282 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 283 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 284 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 285 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 286 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 287 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 288 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 289 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 290 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 291 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 292 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 293 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 294 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 295 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 296 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 297 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 298 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 299 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 300 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 301 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 302 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 303 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 304 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 305 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 306 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 307 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 308 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 309 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 310 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 311 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 312 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 313 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 314 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 315 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 316 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 317 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 318 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 319 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 320 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 321 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 322 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 323 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 324 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 325 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 326 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 327 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 328 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 329 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 330 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 331 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 332 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 333 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 334 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 335 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 336 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 337 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 338 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 339 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 340 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 341 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 342 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 343 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 344 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 345 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 346 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 347 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 348 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 349 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 350 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 351 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 352 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 353 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 354 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 355 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 356 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 357 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 358 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 359 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 360 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 361 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 362 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 363 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 364 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 365 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 366 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 367 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 368 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 369 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 370 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 371 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 372 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 373 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 374 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 375 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 376 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 377 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 378 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 379 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 380 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 381 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 382 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 383 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 384 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 385 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 386 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 387 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 388 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 389 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 390 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 391 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 392 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 393 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 394 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 395 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 396 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 397 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 398 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 399 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 400 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 401 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 402 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 403 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 404 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 405 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 406 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 407 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 408 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 409 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 410 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 411 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 412 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 413 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 414 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 415 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 416 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 417 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 418 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 419 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 420 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 421 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 422 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 423 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 424 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 425 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 426 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 427 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 428 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 429 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 430 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 431 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 432 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 433 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 434 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 435 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 436 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 437 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 438 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 439 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 440 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 441 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 442 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 443 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 444 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 445 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 446 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 447 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 448 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 449 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 450 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 451 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 452 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 453 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 454 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 455 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 456 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 457 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 458 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 459 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 460 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
