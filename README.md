# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-15.md)

*最后自动更新时间: 2026-03-15 17:57:25*
## 1. 英特尔傲腾为何脱颖而出 (2023)

**原文标题**: What makes Intel Optane stand out (2023)

**原文链接**: [https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/](https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/)

英特尔傲腾（Intel Optane）搭载 3D XPoint 技术，是连接 DRAM（内存）与传统 NAND 闪存之间的高性能桥梁。尽管英特尔在 IDM 2.0 战略下于 2022 年决定停止该技术的创新，但傲腾固态硬盘（如 P4800X 和 P5800X）以及持久内存（PMEM）仍是专业企业级环境中的顶级组件。

**核心优势：**
*   **极高耐用性：** 傲腾的寿命处于行业领先地位。专业级 NAND 硬盘的每日全盘写入次数（DWPD）通常在 1 到 10 之间，而傲腾 P5800X 达到了前所未有的 100 DWPD，是高写入负载环境的理想选择。
*   **超低延迟：** 傲腾的读取延迟约为 25 微秒，比专业级 NAND 硬盘快约 300%。这确保了数据能更快到达 CPU，显著减少了处理等待时间。
*   **写入一致性：** 基于 NAND 的固态硬盘需要“垃圾回收”机制，且在缓存填满时会出现性能掉速，而傲腾支持字节级寻址。这使得数据可以直接覆盖写入，即使在持续的高负载下也能保持最高性能。
*   **数据完整性：** 这些专业级驱动器具备硬件级掉电保护（PLP）功能，可保护缓存中的数据，并防止在意外断电时发生映射表损坏。

**现状与应用场景：**
傲腾非常适合延迟敏感型工作负载，包括 vSAN/ZFS 缓存、高性能数据库和 VDI（虚拟桌面基础架构）环境。尽管英特尔正逐步退出闪存存储业务，但傲腾产品目前仍有供应。值得注意的是，英特尔近期发布了傲腾持久内存 300 系列，以支持第四代至强可扩展处理器（Sapphire Rapids），确保该技术在可预见的未来仍能在高端硬件中发挥重要作用。

---

## 2. 机器学习图解入门 (2015)

**原文标题**: A Visual Introduction to Machine Learning (2015)

**原文链接**: [https://r2d3.us/visual-intro-to-machine-learning-part-1/](https://r2d3.us/visual-intro-to-machine-learning-part-1/)

R2D3 的《机器学习图解入门》通过对纽约或旧金山房屋进行分类这一实际任务，为机器学习（ML）提供了一个通俗易懂的概述。该文章利用称为**特征**的数据维度（如海拔高度和每平方英尺价格），展示了机器学习如何通过识别模式来做出预测。

作者重点介绍了**决策树**方法，该方法使用一系列“如果-那么”语句（即**分叉**）在数据中创建边界。构建该模型的过程被称为**训练**。在训练过程中，算法使用**递归**，根据最优**切分点**将数据反复拆分为分支，直到到达做出最终分类的**叶节点**。每次切分的目标是实现最大程度的同质性，确保分组尽可能“纯净”。

一个核心启示是**训练数据**与**测试数据**之间的区别。虽然模型可以不断生长，从而在已知数据上达到 100% 的准确率，但其真正的成功取决于它在未见过的信息上的表现。当模型捕捉到训练集中的无关噪声或过多细节时，就会导致**过拟合**。过拟合的模型在现实世界中表现不佳，因为它们缺乏泛化能力。归根结底，文章将机器学习描述为一种在寻找边界与确保边界对新的未知数据保持有效性之间寻求平衡的过程。

---

## 3. Glassworm 回归：新一波不可见 Unicode 攻击席卷代码库

**原文标题**: Glassworm Is Back: A New Wave of Invisible Unicode Attacks Hits Repositories

**原文链接**: [https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode)

威胁攻击者 **Glassworm** 发起了一波新的大规模“不可见 Unicode”攻击。截至 2026 年 3 月，该攻击已针对 GitHub、npm 和 VS Code Marketplace 上的数百个仓库。

**攻击机制**
该技术利用了在代码编辑器、终端或代码审查界面中无法渲染的隐藏 Unicode 字符。恶意负载被编码在看似为空的字符串（例如反引号 ` `` `）中。执行时，一段微小的 JavaScript 解码程序会提取这些隐藏字节并将其传递给 `eval()` 函数。过往的负载曾被用于窃取凭据、令牌和机密信息，且通常利用 Solana 作为传输通道。

**规模与复杂程度**
这场自 2026 年 3 月初开始活跃的最新行动已导致至少 151 个 GitHub 仓库沦陷，其中包括 **Wasmer**、**Reworm** 和 **anomalyco** 等知名项目。据报道，攻击者正利用**大语言模型 (LLM)** 炮制逼真的“掩护提交”——如文档更新和细微的漏洞修复——使恶意代码能够无缝融入目标代码库。这种 AI 辅助的伪装使得通过标准的视觉代码审查或基础的代码检查（linting）几乎无法检测到注入。

**检测与防护**
文章强调，由于该威胁在视觉上不可见，开发者必须依赖自动化的恶意软件扫描和主动防御措施。安全公司 Aikido 建议使用 **Safe Chain** 等专用工具来实时拦截并阻断这些供应链风险。这一波攻击标志着 Glassworm 活动的一次重大升级，其行为已从 2025 年的孤立事件演变为 2026 年跨多个生态系统的协同推进。

---

## 4. Show HN: GDSL – 800 行内核：500 行实现 Lisp 子集，1300 行实现 C 子集

**原文标题**: Show HN: GDSL – 800 line kernel: Lisp subset in 500, C subset in 1300

**原文链接**: [https://firthemouse.github.io/](https://firthemouse.github.io/)

**GDSL** 是一个极简主义编程项目，旨在挑战现代编译器动辄数百万行代码的巨大复杂性。作者证明，通过优先考虑简洁性和清晰的架构，只需极小的代码规模即可构建出功能完备且高效的语言工具。

该项目基于一个 **800 行的内核**。在此未经修改的基础上，作者开发了：
*   一个仅用 500 行实现的 **Lisp 子集**。
*   一个约 1,300 行实现的 **C 子集**。

与“小型编译器必然脆弱或功能残缺（仅是‘玩具’）”的假设相反，作者断言这些实现不仅运行迅速、性能稳健，而且具有实用价值。该项目源于一种重构语言“意义”的渴望，旨在摆脱传统的臃肿开销。

本文是对现代软件工业的一次批判，质疑为何标准编译器需要如此庞大的代码量。作者将当代系统的臃肿归咎于“接缝、景观和补丁（kludges）”——即不必要的复杂层级和技术债。

经过 16 个月的基础工作，作者将 GDSL 呈现为一块“净土”，旨在作为软件开发的一个全新的、精简的起点，彻底摆脱定义现代工具链的数百万行代码的束缚。

---

## 5. Show HN：Signet —— 基于卫星和天气数据的自主山火追踪

**原文标题**: Show HN: Signet – Autonomous wildfire tracking from satellite and weather data

**原文链接**: [https://signet.watch](https://signet.watch)

生成摘要时出错

---

## 6. 分离 Wayland 合成器与窗口管理器

**原文标题**: Separating the Wayland Compositor and Window Manager

**原文链接**: [https://isaacfreund.com/blog/river-window-management/](https://isaacfreund.com/blog/river-window-management/)

在《分离 Wayland 合成器与窗口管理器》一文中，Isaac Freund 详细阐述了 **river 0.4.0** 引入的一项重大架构变革。

传统上，Wayland 合成器采用单体式架构，将显示服务器、合成器和窗口管理器整合在同一个进程中。虽然这种架构解决了 X11 的性能和输入路由问题，但它迫使开发者仅为了创建一个新的窗口管理器（WM），就必须实现一个复杂的、完整的合成器。

River 0.4.0 通过使用 **`river-window-management-v1`** 协议将窗口管理器拆分为一个独立的程序，从而打破了这一模式。该设计通过区分**窗口管理状态**（尺寸、焦点）和**渲染状态**（位置、修饰），保持了 Wayland 的“完美帧率”和低延迟。通过利用将更新批量处理为原子序列的状态机，river 避免了不必要的每帧往返通讯，确保高层级的窗口管理策略不会干扰底层的渲染性能。

**这种分离带来的主要优势包括：**
*   **降低准入门槛：** 开发者无需处理底层细节，只需一个周末即可编写出功能完备的窗口管理器。
*   **提高稳定性：** 窗口管理器崩溃不再导致整个 Wayland 会话崩溃；WM 可以直接重启。
*   **语言灵活性：** 可以使用带有垃圾回收机制的高级语言编写 WM，而不会引起合成器中的输入延迟峰值。
*   **增加多样性：** 生态系统已拥有超过 15 个兼容的窗口管理器，包括层叠式、平铺式以及基于 Emacs 的选项。

虽然该协议目前尚不支持 VR 和复杂的着色器，但它已被视为是稳定的。Freund 强调，river 已准备好投入日常使用，下一个主要目标是 1.0.0 版本，重点将放在改进切换窗口管理器的用户体验上。

---

## 7. Show HN：如果你的合成器是由 APL（或一个简陋的 K 克隆版）驱动的会怎样？

**原文标题**: Show HN: What if your synthesizer was powered by APL (or a dumb K clone)?

**原文链接**: [https://octetta.github.io/k-synth/](https://octetta.github.io/k-synth/)

**ksynth** 是一款基于浏览器的合成器项目，它利用数组导向编程语言——具体来说是一个“K 克隆版”（APL 的衍生物）——来生成和处理音频。

该工具利用 **WebAssembly (WASM)** 提供高性能环境，用户可以使用数组语言特有的简洁数学语法通过编程定义声音。通过将音频数据视为数组，该合成器能够实现高效的数字信号处理和算法作曲。

**核心功能包括：**
*   **实时编码界面：** 一个指令驱动的工作区，用于运行代码、管理执行历史记录并清空控制台。
*   **补丁管理：** 用于保存、加载和组织“补丁”（音色预设）的系统，包含针对旋律和鼓声合成的专用模块。
*   **交互式控制：** 用于调节音高、设置基础速率并通过打击垫界面触发声音的 UI 元素。
*   **音频导出：** 支持实时播放序列并将生成的音频下载为 WAV 文件。

该项目是函数式数组编程与音乐技术的实验性交叉产物，为对非常规代码驱动合成感兴趣的开发者和声音设计师提供了独特的工作流。

---

## 8. Rack-mount hydroponics

**原文标题**: Rack-mount hydroponics

**原文链接**: [https://sa.lj.am/rack-mount-hydroponics/](https://sa.lj.am/rack-mount-hydroponics/)

生成摘要时出错

---

## 9. UMD Scientists Create 'Smart Underwear' to Measure Human Flatulence

**原文标题**: UMD Scientists Create 'Smart Underwear' to Measure Human Flatulence

**原文链接**: [https://cbmg.umd.edu/news-events/news/brantley-hall-umd-scientists-create-smart-underwear-measure-human-flatulence](https://cbmg.umd.edu/news-events/news/brantley-hall-umd-scientists-create-smart-underwear-measure-human-flatulence)

生成摘要时出错

---

## 10. Hollywood Enters Oscars Weekend in Existential Crisis

**原文标题**: Hollywood Enters Oscars Weekend in Existential Crisis

**原文链接**: [https://www.theculturenewspaper.com/hollywood-enters-oscars-weekend-in-existential-crisis/](https://www.theculturenewspaper.com/hollywood-enters-oscars-weekend-in-existential-crisis/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 2 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 3 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 4 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 5 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 6 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 7 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 8 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 9 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 10 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 11 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 12 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 13 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 14 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 15 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 16 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 17 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 18 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 19 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 20 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 21 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 22 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 23 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 24 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 25 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 26 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 27 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 28 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 29 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 30 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 31 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 32 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 33 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 34 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 35 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 36 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 37 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 38 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 39 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 40 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 41 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 42 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 43 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 44 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 45 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 46 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 47 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 48 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 49 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 50 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 51 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 52 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 53 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 54 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 55 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 56 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 57 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 58 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 59 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 60 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 61 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 62 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 63 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 64 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 65 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 66 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 67 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 68 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 69 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 70 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 71 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 72 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 73 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 74 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 75 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 76 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 77 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 78 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 79 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 80 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 81 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 82 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 83 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 84 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 85 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 86 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 87 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 88 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 89 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 90 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 91 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 92 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 93 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 94 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 95 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 96 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 97 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 98 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 99 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 100 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 101 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 102 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 103 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 104 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 105 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 106 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 107 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 108 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 109 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 110 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 111 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 112 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 113 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 114 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 115 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 116 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 117 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 118 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 119 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 120 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 121 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 122 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 123 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 124 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 125 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 126 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 127 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 128 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 129 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 130 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 131 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 132 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 133 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 134 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 135 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 136 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 137 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 138 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 139 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 140 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 141 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 142 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 143 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 144 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 145 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 146 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 147 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 148 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 149 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 150 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 151 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 152 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 153 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 154 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 155 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 156 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 157 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 158 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 159 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 160 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 161 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 162 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 163 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 164 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 165 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 166 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 167 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 168 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 169 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 170 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 171 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 172 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 173 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 174 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 175 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 176 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 177 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 178 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 179 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 180 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 181 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 182 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 183 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 184 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 185 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 186 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 187 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 188 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 189 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 190 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 191 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 192 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 193 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 194 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 195 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 196 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 197 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 198 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 199 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 200 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 201 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 202 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 203 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 204 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 205 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 206 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 207 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 208 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 209 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 210 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 211 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 212 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 213 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 214 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 215 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 216 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 217 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 218 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 219 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 220 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 221 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 222 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 223 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 224 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 225 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 226 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 227 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 228 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 229 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 230 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 231 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 232 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 233 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 234 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 235 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 236 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 237 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 238 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 239 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 240 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 241 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 242 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 243 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 244 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 245 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 246 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 247 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 248 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 249 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 250 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 251 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 252 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 253 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 254 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 255 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 256 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 257 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 258 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 259 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 260 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 261 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 262 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 263 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 264 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 265 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 266 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 267 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 268 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 269 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 270 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 271 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 272 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 273 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 274 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 275 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 276 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 277 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 278 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 279 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 280 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 281 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 282 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 283 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 284 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 285 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 286 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 287 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 288 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 289 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 290 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 291 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 292 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 293 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 294 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 295 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 296 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 297 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 298 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 299 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 300 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 301 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 302 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 303 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 304 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 305 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 306 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 307 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 308 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 309 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 310 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 311 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 312 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 313 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 314 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 315 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 316 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 317 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 318 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 319 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 320 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 321 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 322 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 323 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 324 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 325 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 326 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 327 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 328 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 329 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 330 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 331 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 332 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 333 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 334 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 335 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 336 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 337 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 338 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 339 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 340 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 341 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 342 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 343 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 344 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 345 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 346 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 347 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 348 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 349 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 350 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 351 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 352 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 353 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 354 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 355 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 356 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 357 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 358 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 359 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 360 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
