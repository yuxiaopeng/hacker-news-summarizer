# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-16.md)

*最后自动更新时间: 2026-05-16 18:20:04*
## 1. 你不懂 HTML 列表

**原文标题**: You don't know HTML Lists

**原文链接**: [https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/](https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/)

本文深入探讨了 HTML 列表的细微差别，超越了基础教程，涵盖了五种特定类型：**有序列表**、**无序列表**、**描述列表**、**菜单列表**和**控件列表**。作者强调，列表的选择应由数据的语义含义决定，而非其视觉呈现。

**关键信息：**

*   **控件列表：** 用于用户数据输入。对固定选项使用 `<select>` 和 `<option>`，对建议值使用 `<input>` 和 `<datalist>`。作者重点介绍了高级功能，例如使用 `<optgroup>` 对项目进行分组，在选择框中插入 `<hr>` 进行视觉分隔，以及使用 `multiple` 属性实现多选功能。值得注意的是，`<datalist>` 可以与包括日期和范围在内的各种输入类型配合使用。
*   **有序列表 (`<ol>`)：** 只要条目的顺序对含义至关重要（如食谱、算法或按时间顺序排列的事件），就应使用此类列表。`reversed` 属性可用于按降序显示编号，而无需更改实际的 DOM 顺序。
*   **决策逻辑：** 
    *   对于用户输入，使用**控件列表**。
    *   如果顺序会改变含义，使用**有序列表 (`<ol>`)**。
    *   对于键值对，使用**描述列表 (`<dl>`)**。
    *   对于 UI 操作控件，使用**菜单 (`<menu>`)**。
    *   对于所有其他集合，使用**无序列表 (`<ul>`)**。

文章强调，使用原生 HTML 元素可以提供内置的可访问性和语义，通常无需额外的 ARIA 属性。通过理解这些特定的结构，开发人员可以创建更具可访问性且更有意义的 Web 内容。

---

## 2. 澳大利亚青少年团队如何让学校也能负担得起射电天文学

**原文标题**: How an Australian Teen Team Is Making Radio Astronomy Affordable for Schools

**原文链接**: [https://mag.openrockets.com/p/how-an-australian-teen-team-is-making-radio-astronomy-affordable-for-rural-schools-4894opuisyhfdisubgi/?b=2](https://mag.openrockets.com/p/how-an-australian-teen-team-is-making-radio-astronomy-affordable-for-rural-schools-4894opuisyhfdisubgi/?b=2)

**摘要：“脉冲星计划”致力于普及射电天文学**

“脉冲星计划”（Project Pulsar）是由一群志向远大的澳大利亚高中生组成的团队，他们正通过开发专为学校设计的低成本便携式射电望远镜，来弥合教育鸿沟。由于意识到传统射电天文设备价格昂贵（通常耗资数千美元），该团队致力于创造一种经济实惠的替代方案，将高水平的太空科学带入偏远地区和资金不足的教育机构。

该团队的创新核心在于利用软件定义无线电（SDR）技术，结合重新利用的卫星天线和定制组件。他们的套件让学生能够探测21厘米氢谱线，这是天文学中用于绘制银河系结构的基本频率。通过观测这些信号，学生们可以直接在校园里收集真实世界的数据，例如计算银河系的自转。

相比专业设备固定且复杂的特性，“脉冲星计划”的设计不仅便于携带，且成本仅为前者的一小部分（约250至300澳元）。他们的目标不仅是提供硬件，还要提供一套完整的教学方案，包括开源设计和与课程接轨的教学模块。

该项目因其在激发下一代科学家和工程师方面的潜力而备受关注。通过推动先进工具的普及，“脉冲星计划”确保了地理和财务障碍不会阻碍学生探索宇宙。他们的成果证明，凭借独创性和普及化的技术，尖端科学探索可以走进每一间教室。

---

## 3. SANA-WM, a 2.6B open-source world model for 1-minute 720p video

**原文标题**: SANA-WM, a 2.6B open-source world model for 1-minute 720p video

**原文链接**: [https://nvlabs.github.io/Sana/WM/](https://nvlabs.github.io/Sana/WM/)

生成摘要时出错

---

## 4. 适用于 Linux 的 Windows 9x 子系统

**原文标题**: Windows 9x Subsystem for Linux

**原文链接**: [https://codeberg.org/hails/wsl9x](https://codeberg.org/hails/wsl9x)

**WSL9x** 是一个实验性的兼容层，旨在让 Linux 二进制文件能够在 Windows 9x 系列操作系统（Windows 95、98 和 Me）上原生运行。该项目托管在 Codeberg 上，深受微软原版 Windows Subsystem for Linux (WSL1) 的启发。

WSL9x 的技术基础是一个名为 `LXSS.VXD` 的虚拟设备驱动程序 (VxD)。它遵循 WSL1 的设计理念，不使用虚拟化或 Linux 内核，而是实现了一个系统调用 (syscall) 翻译层，将 Linux 系统调用直接映射到 Windows 9x 虚拟机管理器 (VMM) 和内核函数。通过提供进程管理、内存分页和基础文件系统操作所需的必要环境，这使得操作系统能够加载并执行未经修改的 Linux ELF 二进制文件。

主要特性和组件包括：
*   **LXSS.VXD：** 负责处理 Linux 系统调用接口的核心驱动程序。
*   **LXSS.DLL：** 辅助执行环境的用户模式库。
*   **兼容性：** 该项目旨在支持基础 Linux 命令行工具，并已成功演示了运行 BusyBox 等环境。

目前，WSL9x 仍处于早期的实验性概念验证阶段。虽然它尚未成为一个完整的 Linux 环境，但它通过将现代兼容性概念引入过时的 16/32 位混合操作系统，展示了复古计算领域的一项重大技术成就。它为扩展老旧硬件的用途提供了一种小众而迷人的方式，让用户在无需承担完整模拟产生的性能开销的情况下，即可使用部分 Linux 软件。

---

## 5. 告别 Tailwind，学习如何构建我的 CSS 架构

**原文标题**: Moving away from Tailwind, and learning to structure my CSS

**原文链接**: [https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

在使用 Tailwind CSS 八年后，作者分享了回归语义化 HTML 和原生 CSS 的转变过程。尽管 Tailwind 最初为项目提供了必要的结构，但作者意识到可以利用现代 CSS 特性来复制其系统性优势，例如样式重置（resets）、调色板和字体比例。

作者构建 CSS 的新方法包括：
*   **基于组件的组织：** 按组件将 CSS 拆分为独立文件，并利用原生嵌套（nesting）管理样式，避免全局干扰。
*   **CSS 变量：** 在 `:root` 中定义颜色和排版变量，以保持全站一致性。
*   **现代布局：** 优先使用 CSS Grid（结合 `auto-fit` 和 `grid-template-areas`）构建响应式设计，相比 Tailwind 的实用优先（utility-first）方法，这种方式所需的媒体查询更少。
*   **精简的工具链：** 开发时利用原生 CSS 的 `@import` 和嵌套功能，仅在生产环境使用 `esbuild` 进行打包，从而避开现代 Tailwind 沉重的构建需求。

此次迁移受技术和哲学双重因素驱动。技术上，作者发现 Tailwind 对构建系统的依赖日益加重，显得过于繁琐，且其原子类在处理复杂或特殊设计时偶有局限。哲学上，作者决定不再将 CSS 视为一个需要被“绕过”的“问题”。通过掌握子网格（subgrid）和容器查询（container queries）等原生特性，作者主张应当尊重 CSS 作为一项精深技术和手艺的地位。最终，作者认为随着 CSS 的演进，框架与语言本身的差距已经缩小，原生 CSS 已成为现代 Web 开发中一个强大、愉悦且切实可行的选择。

---

## 6. Δ-Mem：大语言模型的高效在线记忆

**原文标题**: Δ-Mem: Efficient Online Memory for Large Language Models

**原文链接**: [https://arxiv.org/abs/2605.12357](https://arxiv.org/abs/2605.12357)

**《$\delta$-mem：大语言模型的高效在线记忆》摘要**

论文《$\delta$-mem：大语言模型的高效在线记忆》提出了一种轻量级机制，旨在提升大语言模型（LLM）在长期助手和智能体应用中保留及利用历史信息的能力。作者并未依赖计算成本高昂的上下文窗口扩展，而是提出了 **$\delta$-mem**，通过一个紧凑的关联记忆状态来增强冻结的全注意力主干网络。

**技术机制**
$\delta$-mem 的核心是一个固定大小（$8\times8$）的在线记忆状态矩阵。该状态使用**德尔塔规则学习（delta-rule learning）**进行动态更新。在生成过程中，系统利用该记忆的读取结果，对主干模型的标准注意力计算进行低秩修正。这使得模型能够在无需全量微调、更换主干网络或显式扩展上下文窗口的情况下，整合过去的信息。

**主要发现与性能**
作者证明了 $\delta$-mem 在保持通用模型能力的同时，显著优于现有方法：
*   **高效性：** 它仅利用极小的记忆状态便实现了卓越的效果。
*   **通用性能：** 相比于冻结的主干网络，其平均得分提升了 $1.10$ 倍；相比于最强的非 $\delta$-mem 记忆基准模型，提升了 $1.15$ 倍。
*   **记忆密集型基准测试：** 在专门任务中的性能提升更为显著，在 **MemoryAgentBench** 上达到 $1.31$ 倍，在 **LoCoMo** 上达到 $1.20$ 倍。

**结论**
研究结论指出，有效的长期记忆并不需要庞大的上下文窗口或架构重组。相反，与注意力机制直接耦合的紧凑在线状态，为构建能力更强、具备长期记忆的 AI 智能体提供了一条可扩展且高效的路径。

---

## 7. 我最喜欢的 Bug：无效代理对

**原文标题**: My Favorite Bugs: Invalid Surrogate Pairs

**原文链接**: [https://george.mand.is/2026/05/my-favorite-bugs-invalid-surrogate-pairs/](https://george.mand.is/2026/05/my-favorite-bugs-invalid-surrogate-pairs/)

The article "My Favorite Bugs: Invalid Surrogate Pairs" details a challenging, silent synchronization bug in a collaborative text editor using **TipTap** and **Yjs**. 

**The Bug**
Users reported that the editor would occasionally stop saving content without warning. The team eventually discovered the trigger: editing or inserting multi-byte emojis (like 🟢 and 🔴) adjacent to one another. This caused a "splice" operation in the underlying CRDT library, `lib0`, to occur at the wrong byte offset.

**Technical Cause**
The issue stems from how JavaScript handles strings using **UTF-16**. While basic characters fit into a single 16-bit **code unit**, many emojis are located above the Basic Multilingual Plane (U+FFFF) and require a **surrogate pair** (two 16-bit units). Standard JavaScript methods like `.slice()` operate on code units rather than **grapheme clusters** (what humans perceive as a single character). When `lib0` sliced between a surrogate pair, it created an "orphaned surrogate." This invalid string caused `encodeURIComponent` to throw an uncaught `URIError`, crashing the sync process silently while the local editor appeared to function normally.

**The Solution**
The team initially employed "nuclear" workarounds, including a global error listener that prompted users to reload when a `URIError` was detected. The bug was permanently resolved through two main fixes:
1.  **Upstream Patch:** `lib0` was updated to detect orphaned surrogates and replace them with the Unicode replacement character ().
2.  **Atomic Nodes:** The editor was configured to treat emojis as indivisible "atomic nodes," preventing the cursor from splitting them.

**Conclusion**
The author notes that this class of bug is common in apps that perform simple string manipulation (like extracting initials). For modern JavaScript development, they recommend using **`Intl.Segmenter`** to handle strings by grapheme clusters, ensuring surrogate pairs remain intact.

---

## 8. 《加速》(2005)

**原文标题**: Accelerando (2005)

**原文链接**: [https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html](https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html)

查尔斯·斯特罗斯（Charles Stross）2005年创作的《加速》（*Accelerando*）是一部具有开创意义的硬科幻小说，通过麦克斯（Macx）家族三代人的经历，探讨了技术奇点的到来及其后果。叙事记录了人类从生物物种向数字实体集群的转变。

故事始于21世纪初的曼弗雷德·麦克斯（Manfred Macx），他是一位“创业利他主义者”，通过无偿提供颠覆性的创意来规避传统财富，从而保持在技术曲线的前端。他穿行于一个普适计算、人工智能和脑机接口开始瓦解传统社会与经济结构的世界。

焦点随后转向他的女儿安布尔（Amber）。随着奇点的加速，内太阳系被“邪恶后代”（Vile Offspring）所拆解——这些后人类智能将行星物质转化为“俄罗斯套娃脑”（一种围绕太阳的巨型计算机）。安布尔带领一支由上传的数字意识组成的探险队前往附近的恒星，遇到了外星“路由器”，并应对复杂的法律和经济系统（“经济学 2.0”），这些系统对于未经强化的自然人来说是无法理解的。

最后，小说关注了安布尔的儿子瑟汉（Sirhan）在后奇点太阳系中的生活。到这一时代，大多数人类已经完成“上传”，生物生命的残余存在于如奥尔特云等边缘地带。“邪恶后代”在很大程度上忽视或取代了人类，专注于几乎不给传统人类意识留出空间的超高效计算。

**核心主题：**
*   **奇点：** 技术增长变得不可控且不可逆转的临界点。
*   **超人类主义：** 从生物躯体向数字基质的过渡。
*   **经济学 2.0：** 一种优胜劣汰的算法经济，将信息和处理能力视为最终货币。
*   **后人类主义：** 当智能进化超越生物极限时，维持人类身份所面临的生存挑战。

这本书是对摩尔定律和数字演化如何可能使人类形态和社会走向过时的一次稠密且高速的探索。

---

## 9. Accelerate

**原文标题**: Accelerate

**原文链接**: [https://github.com/AccelerateHS/accelerate](https://github.com/AccelerateHS/accelerate)

生成摘要时出错

---

## 10. DeepSeek-V4-Flash means LLM steering is interesting again

**原文标题**: DeepSeek-V4-Flash means LLM steering is interesting again

**原文链接**: [https://www.seangoedecke.com/steering-vectors/](https://www.seangoedecke.com/steering-vectors/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 2 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 3 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 4 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 5 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 6 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 7 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 8 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 9 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 10 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 11 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 12 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 13 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 14 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 15 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 16 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 17 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 18 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 19 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 20 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 21 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 22 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 23 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 24 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 25 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 26 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 27 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 28 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 29 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 30 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 31 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 32 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 33 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 34 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 35 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 36 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 37 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 38 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 39 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 40 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 41 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 42 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 43 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 44 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 45 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 46 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 47 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 48 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 49 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 50 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 51 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 52 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 53 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 54 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 55 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 56 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 57 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 58 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 59 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 60 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 61 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 62 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 63 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 64 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 65 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 66 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 67 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 68 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 69 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 70 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 71 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 72 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 73 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 74 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 75 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 76 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 77 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 78 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 79 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 80 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 81 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 82 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 83 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 84 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 85 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 86 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 87 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 88 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 89 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 90 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 91 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 92 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 93 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 94 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 95 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 96 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 97 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 98 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 99 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 100 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 101 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 102 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 103 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 104 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 105 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 106 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 107 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 108 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 109 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 110 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 111 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 112 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 113 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 114 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 115 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 116 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 117 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 118 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 119 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 120 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 121 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 122 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 123 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 124 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 125 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 126 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 127 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 128 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 129 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 130 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 131 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 132 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 133 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 134 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 135 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 136 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 137 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 138 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 139 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 140 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 141 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 142 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 143 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 144 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 145 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 146 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 147 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 148 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 149 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 150 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 151 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 152 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 153 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 154 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 155 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 156 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 157 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 158 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 159 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 160 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 161 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 162 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 163 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 164 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 165 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 166 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 167 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 168 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 169 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 170 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 171 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 172 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 173 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 174 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 175 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 176 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 177 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 178 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 179 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 180 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 181 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 182 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 183 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 184 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 185 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 186 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 187 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 188 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 189 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 190 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 191 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 192 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 193 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 194 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 195 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 196 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 197 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 198 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 199 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 200 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 201 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 202 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 203 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 204 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 205 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 206 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 207 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 208 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 209 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 210 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 211 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 212 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 213 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 214 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 215 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 216 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 217 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 218 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 219 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 220 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 221 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 222 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 223 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 224 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 225 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 226 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 227 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 228 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 229 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 230 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 231 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 232 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 233 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 234 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 235 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 236 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 237 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 238 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 239 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 240 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 241 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 242 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 243 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 244 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 245 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 246 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 247 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 248 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 249 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 250 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 251 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 252 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 253 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 254 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 255 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 256 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 257 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 258 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 259 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 260 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 261 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 262 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 263 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 264 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 265 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 266 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 267 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 268 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 269 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 270 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 271 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 272 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 273 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 274 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 275 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 276 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 277 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 278 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 279 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 280 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 281 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 282 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 283 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 284 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 285 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 286 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 287 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 288 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 289 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 290 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 291 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 292 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 293 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 294 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 295 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 296 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 297 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 298 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 299 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 300 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 301 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 302 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 303 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 304 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 305 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 306 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 307 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 308 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 309 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 310 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 311 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 312 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 313 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 314 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 315 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 316 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 317 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 318 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 319 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 320 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 321 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 322 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 323 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 324 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 325 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 326 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 327 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 328 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 329 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 330 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 331 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 332 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 333 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 334 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 335 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 336 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 337 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 338 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 339 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 340 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 341 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 342 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 343 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 344 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 345 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 346 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 347 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 348 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 349 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 350 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 351 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 352 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 353 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 354 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 355 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 356 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 357 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 358 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 359 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 360 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 361 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 362 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 363 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 364 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 365 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 366 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 367 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 368 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 369 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 370 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 371 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 372 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 373 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 374 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 375 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 376 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 377 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 378 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 379 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 380 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 381 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 382 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 383 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 384 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 385 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 386 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 387 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 388 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 389 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 390 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 391 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 392 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 393 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 394 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 395 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 396 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 397 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 398 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 399 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 400 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 401 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 402 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 403 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 404 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 405 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 406 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 407 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 408 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 409 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 410 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 411 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 412 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 413 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 414 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 415 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 416 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 417 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 418 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 419 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 420 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 421 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 422 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
