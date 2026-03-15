# Hacker News 热门文章摘要 (2026-03-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Kniterate Notes

**原文标题**: Kniterate Notes

**原文链接**: [https://soup.agnescameron.info//2026/03/07/kniterate-notes.html](https://soup.agnescameron.info//2026/03/07/kniterate-notes.html)

生成摘要时出错

---

## 12. Zipp 2001 Restoration

**原文标题**: Zipp 2001 Restoration

**原文链接**: [https://robot-daycare.com/posts/zipp-2001-restoration-part-1/](https://robot-daycare.com/posts/zipp-2001-restoration-part-1/)

生成摘要时出错

---

## 13. IBM, sonic delay lines, and the history of the 80×24 display (2019)

**原文标题**: IBM, sonic delay lines, and the history of the 80×24 display (2019)

**原文链接**: [https://www.righto.com/2019/11/ibm-sonic-delay-lines-and-history-of.html](https://www.righto.com/2019/11/ibm-sonic-delay-lines-and-history-of.html)

This article explores the historical reasons behind the ubiquity of 80x24 and 80x25 terminal displays. The author argues that these dimensions were not dictated by technological necessity—such as memory limits or television scan rates—but were instead established through **IBM’s market dominance.**

While the 80-column width was a direct legacy of **punch cards**, the number of lines evolved through specific IBM hardware. In 1965, the IBM 2260 introduced CRT terminals to the masses, utilizing "sonic delay lines" (coiled nickel wires) for inexpensive character storage. In 1971, IBM released the **3270 terminal**, which established the **80x24** format. This specific size was a result of using four 480-character MOS shift register blocks for memory. Because IBM held 50% of the market, competitors were forced to adopt 80x24 for compatibility, a trend cemented by the later success of the DEC VT100.

The author debunks theories that 80x24 was an inevitable consequence of hardware limits by pointing out the massive variety of terminal sizes available in the 1970s (ranging from 32x8 to 133x64). If technology were the bottleneck, such diversity would not have existed; instead, market standardization drove the industry toward IBM’s specifications.

The shift to **80x25** occurred with the 1981 IBM PC (and its predecessor, the DataMaster), which added a 25th line to provide a dedicated "status line" for operators. Today, these dimensions persist in modern terminal emulators as a direct legacy of IBM’s influence on mainframe and personal computing history.

---

## 14. $96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor

**原文标题**: $96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor

**原文链接**: [https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

生成摘要时出错

---

## 15. Generating All 32-Bit Primes (Part I)

**原文标题**: Generating All 32-Bit Primes (Part I)

**原文链接**: [https://hnlyman.github.io/pages/prime32_I.html](https://hnlyman.github.io/pages/prime32_I.html)

生成摘要时出错

---

## 16. The 100 hour gap between a vibecoded prototype and a working product

**原文标题**: The 100 hour gap between a vibecoded prototype and a working product

**原文链接**: [https://kanfa.macbudkowski.com/vibecoding-cryptosaurus](https://kanfa.macbudkowski.com/vibecoding-cryptosaurus)

生成摘要时出错

---

## 17. The Webpage Has Instructions. The Agent Has Your Credentials

**原文标题**: The Webpage Has Instructions. The Agent Has Your Credentials

**原文链接**: [https://openguard.sh/blog/prompt-injections/](https://openguard.sh/blog/prompt-injections/)

生成摘要时出错

---

## 18. How kernel anti-cheats work

**原文标题**: How kernel anti-cheats work

**原文链接**: [https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/](https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/)

生成摘要时出错

---

## 19. A most elegant TCP hole punching algorithm

**原文标题**: A most elegant TCP hole punching algorithm

**原文链接**: [https://robertsdotpm.github.io/cryptography/tcp_hole_punching.html](https://robertsdotpm.github.io/cryptography/tcp_hole_punching.html)

生成摘要时出错

---

## 20. Examples for the tcpdump and dig man pages

**原文标题**: Examples for the tcpdump and dig man pages

**原文链接**: [https://jvns.ca/blog/2026/03/10/examples-for-the-tcpdump-and-dig-man-pages/](https://jvns.ca/blog/2026/03/10/examples-for-the-tcpdump-and-dig-man-pages/)

生成摘要时出错

---

## 21. Why Mathematica does not simplify sinh(arccosh(x))

**原文标题**: Why Mathematica does not simplify sinh(arccosh(x))

**原文链接**: [https://www.johndcook.com/blog/2026/03/10/sinh-arccosh/](https://www.johndcook.com/blog/2026/03/10/sinh-arccosh/)

生成摘要时出错

---

## 22. Treasure hunter freed from jail after refusing to turn over shipwreck gold

**原文标题**: Treasure hunter freed from jail after refusing to turn over shipwreck gold

**原文链接**: [https://www.bbc.com/news/articles/cg4g7kn99q3o](https://www.bbc.com/news/articles/cg4g7kn99q3o)

生成摘要时出错

---

## 23. Allow me to get to know you, mistakes and all

**原文标题**: Allow me to get to know you, mistakes and all

**原文链接**: [https://sebi.io/posts/2026-03-14-allow-me-to-get-to-know-you-mistakes-and-all/](https://sebi.io/posts/2026-03-14-allow-me-to-get-to-know-you-mistakes-and-all/)

生成摘要时出错

---

## 24. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adz2240](https://www.science.org/doi/10.1126/sciadv.adz2240)

生成摘要时出错

---

## 25. Codegen is not productivity

**原文标题**: Codegen is not productivity

**原文链接**: [https://www.antifound.com/posts/codegen-is-not-productivity/](https://www.antifound.com/posts/codegen-is-not-productivity/)

生成摘要时出错

---

## 26. Pentagon expands oversight of Stars and Stripes, limits content

**原文标题**: Pentagon expands oversight of Stars and Stripes, limits content

**原文链接**: [https://www.stripes.com/theaters/us/2026-03-13/pentagon-modernization-plan-stars-and-stripes-21051529.html](https://www.stripes.com/theaters/us/2026-03-13/pentagon-modernization-plan-stars-and-stripes-21051529.html)

生成摘要时出错

---

## 27. Learning athletic humanoid tennis skills from imperfect human motion data

**原文标题**: Learning athletic humanoid tennis skills from imperfect human motion data

**原文链接**: [https://zzk273.github.io/LATENT/](https://zzk273.github.io/LATENT/)

生成摘要时出错

---

## 28. Show HN: Han – A Korean programming language written in Rust

**原文标题**: Show HN: Han – A Korean programming language written in Rust

**原文链接**: [https://github.com/xodn348/han](https://github.com/xodn348/han)

生成摘要时出错

---

## 29. Centuries of selective breeding turned wild cabbage into different vegetables

**原文标题**: Centuries of selective breeding turned wild cabbage into different vegetables

**原文链接**: [https://www.worksinprogress.news/p/many-of-the-tastiest-vegetables-are](https://www.worksinprogress.news/p/many-of-the-tastiest-vegetables-are)

生成摘要时出错

---

## 30. SBCL Fibers – Lightweight Cooperative Threads

**原文标题**: SBCL Fibers – Lightweight Cooperative Threads

**原文链接**: [https://atgreen.github.io/repl-yell/posts/sbcl-fibers/](https://atgreen.github.io/repl-yell/posts/sbcl-fibers/)

生成摘要时出错

---

## 31. The Official DR DOS Website

**原文标题**: The Official DR DOS Website

**原文链接**: [https://www.dr-dos.com/](https://www.dr-dos.com/)

生成摘要时出错

---

## 32. Bumblebee queens breathe underwater to survive drowning

**原文标题**: Bumblebee queens breathe underwater to survive drowning

**原文链接**: [https://www.smithsonianmag.com/science-nature/bumblebee-queens-breathe-underwater-to-survive-drowning-revealing-how-they-can-live-submerged-for-a-week-180988330/](https://www.smithsonianmag.com/science-nature/bumblebee-queens-breathe-underwater-to-survive-drowning-revealing-how-they-can-live-submerged-for-a-week-180988330/)

生成摘要时出错

---

## 33. A preview of Coalton 0.2, a statically-typed Lisp

**原文标题**: A preview of Coalton 0.2, a statically-typed Lisp

**原文链接**: [https://coalton-lang.github.io/20260312-coalton0p2/](https://coalton-lang.github.io/20260312-coalton0p2/)

生成摘要时出错

---

## 34. The Appalling Stupidity of Spotify's AI DJ

**原文标题**: The Appalling Stupidity of Spotify's AI DJ

**原文链接**: [https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)

生成摘要时出错

---

## 35. Ageless Linux – Software for humans of indeterminate age

**原文标题**: Ageless Linux – Software for humans of indeterminate age

**原文链接**: [https://agelesslinux.org/](https://agelesslinux.org/)

生成摘要时出错

---

## 36. MCP is dead; long live MCP

**原文标题**: MCP is dead; long live MCP

**原文链接**: [https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/](https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/)

生成摘要时出错

---

## 37. Slicing Bezier Surfaces

**原文标题**: Slicing Bezier Surfaces

**原文链接**: [https://fatih-erikli-potato.github.io/blog/slicing-bezier-surfaces.html](https://fatih-erikli-potato.github.io/blog/slicing-bezier-surfaces.html)

生成摘要时出错

---

## 38. Trust no one: are one-way trusts one way?

**原文标题**: Trust no one: are one-way trusts one way?

**原文链接**: [https://offsec.almond.consulting/trust-no-one_are-one-way-trusts-really-one-way.html](https://offsec.almond.consulting/trust-no-one_are-one-way-trusts-really-one-way.html)

生成摘要时出错

---

## 39. Mathematics Distillation Challenge – Equational Theories

**原文标题**: Mathematics Distillation Challenge – Equational Theories

**原文链接**: [https://terrytao.wordpress.com/2026/03/13/mathematics-distillation-challenge-equational-theories/](https://terrytao.wordpress.com/2026/03/13/mathematics-distillation-challenge-equational-theories/)

生成摘要时出错

---

## 40. Small U.S. town, big company. Can it weather the tariff Blizzard? (Digi-Key) (2025)

**原文标题**: Small U.S. town, big company. Can it weather the tariff Blizzard? (Digi-Key) (2025)

**原文链接**: [https://www.npr.org/2025/04/24/nx-s1-5332209/digikey-tariff-small-minnesota-town-big-company](https://www.npr.org/2025/04/24/nx-s1-5332209/digikey-tariff-small-minnesota-town-big-company)

生成摘要时出错

---

## 41. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://human-organ-atlas.esrf.fr/](https://human-organ-atlas.esrf.fr/)

生成摘要时出错

---

## 42. Reverse Engineering Apple's GPU Energy Model on the M4 Max

**原文标题**: Reverse Engineering Apple's GPU Energy Model on the M4 Max

**原文链接**: [https://www.youtube.com/watch?v=HKxIGgyeISM](https://www.youtube.com/watch?v=HKxIGgyeISM)

生成摘要时出错

---

## 43. An ode to bzip

**原文标题**: An ode to bzip

**原文链接**: [https://purplesyringa.moe/blog/an-ode-to-bzip/](https://purplesyringa.moe/blog/an-ode-to-bzip/)

生成摘要时出错

---

## 44. Tree Search Distillation for Language Models Using PPO

**原文标题**: Tree Search Distillation for Language Models Using PPO

**原文链接**: [https://ayushtambde.com/blog/tree-search-distillation-for-language-models-using-ppo/](https://ayushtambde.com/blog/tree-search-distillation-for-language-models-using-ppo/)

生成摘要时出错

---

## 45. A look inside Dialector, filmmaker Chris Marker's chatbot from 1988

**原文标题**: A look inside Dialector, filmmaker Chris Marker's chatbot from 1988

**原文链接**: [https://kubicki.org/letters/the-festival-of-the-machines/](https://kubicki.org/letters/the-festival-of-the-machines/)

生成摘要时出错

---

## 46. Marketing for Founders

**原文标题**: Marketing for Founders

**原文链接**: [https://github.com/EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders)

生成摘要时出错

---

## 47. Baochip-1x: What it is, why I'm doing it now and how it came about

**原文标题**: Baochip-1x: What it is, why I'm doing it now and how it came about

**原文链接**: [https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about](https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about)

生成摘要时出错

---

## 48. A Recursive Algorithm to Render Signed Distance Fields

**原文标题**: A Recursive Algorithm to Render Signed Distance Fields

**原文链接**: [https://pointersgonewild.com/2026-03-06-a-recursive-algorithm-to-render-signed-distance-fields/](https://pointersgonewild.com/2026-03-06-a-recursive-algorithm-to-render-signed-distance-fields/)

生成摘要时出错

---

## 49. 9 Mothers Defense (YC P26) Is Hiring in Austin

**原文标题**: 9 Mothers Defense (YC P26) Is Hiring in Austin

**原文链接**: [https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q](https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q)

生成摘要时出错

---

## 50. Honda is killing its EVs – and any chance of competing in the future

**原文标题**: Honda is killing its EVs – and any chance of competing in the future

**原文链接**: [https://techcrunch.com/2026/03/14/honda-is-killing-its-evs-and-any-chance-of-competing-in-the-future/](https://techcrunch.com/2026/03/14/honda-is-killing-its-evs-and-any-chance-of-competing-in-the-future/)

生成摘要时出错

---

## 51. Hostile Volume – A game about adjusting volume with intentionally bad UI

**原文标题**: Hostile Volume – A game about adjusting volume with intentionally bad UI

**原文链接**: [https://hostilevolume.com/](https://hostilevolume.com/)

生成摘要时出错

---

## 52. SpaceX IPO Scandal

**原文标题**: SpaceX IPO Scandal

**原文链接**: [https://www.youtube.com/watch?v=8rS3fTbC7TE](https://www.youtube.com/watch?v=8rS3fTbC7TE)

生成摘要时出错

---

## 53. Library of Short Stories

**原文标题**: Library of Short Stories

**原文链接**: [https://www.libraryofshortstories.com/](https://www.libraryofshortstories.com/)

生成摘要时出错

---

## 54. How North Korean IT Workers Infiltrated Western Tech Companies

**原文标题**: How North Korean IT Workers Infiltrated Western Tech Companies

**原文链接**: [https://www.nbcnews.com/investigations/north-korea-it-worker-scheme-nisos-fbi-rcna245025](https://www.nbcnews.com/investigations/north-korea-it-worker-scheme-nisos-fbi-rcna245025)

生成摘要时出错

---

## 55. Fedora 44 on the Raspberry Pi 5

**原文标题**: Fedora 44 on the Raspberry Pi 5

**原文链接**: [https://nullr0ute.com/2026/03/fedora-44-on-the-raspberry-pi-5/](https://nullr0ute.com/2026/03/fedora-44-on-the-raspberry-pi-5/)

生成摘要时出错

---

## 56. Airbus is preparing two uncrewed combat aircraft

**原文标题**: Airbus is preparing two uncrewed combat aircraft

**原文链接**: [https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european](https://www.airbus.com/en/newsroom/press-releases/2026-03-airbus-is-preparing-two-uncrewed-combat-aircraft-from-kratos-for-first-flight-with-a-european)

生成摘要时出错

---

## 57. 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文标题**: 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文链接**: [https://claude.com/blog/1m-context-ga](https://claude.com/blog/1m-context-ga)

生成摘要时出错

---

## 58. UK to Allow "Plug in" Solar

**原文标题**: UK to Allow "Plug in" Solar

**原文链接**: [https://www.gov.uk/government/news/government-to-go-further-and-faster-in-becoming-energy-secure](https://www.gov.uk/government/news/government-to-go-further-and-faster-in-becoming-energy-secure)

生成摘要时出错

---

## 59. Starlink militarization and its impact on global strategic stability (2023)

**原文标题**: Starlink militarization and its impact on global strategic stability (2023)

**原文链接**: [https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/](https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/)

生成摘要时出错

---

## 60. Starlink militarization and its impact on global strategic stability (2023)

**原文标题**: Starlink militarization and its impact on global strategic stability (2023)

**原文链接**: [https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/](https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/)

生成摘要时出错

---

## 61. Postgres with Builtin File Systems

**原文标题**: Postgres with Builtin File Systems

**原文链接**: [https://db9.ai/](https://db9.ai/)

生成摘要时出错

---

## 62. Montana passes Right to Compute act (2025)

**原文标题**: Montana passes Right to Compute act (2025)

**原文链接**: [https://www.westernmt.news/2025/04/21/montana-leads-the-nation-with-groundbreaking-right-to-compute-act/](https://www.westernmt.news/2025/04/21/montana-leads-the-nation-with-groundbreaking-right-to-compute-act/)

生成摘要时出错

---

## 63. Megadev: A Development Kit for the Sega Mega Drive and Mega CD Hardware

**原文标题**: Megadev: A Development Kit for the Sega Mega Drive and Mega CD Hardware

**原文链接**: [https://github.com/drojaazu/megadev](https://github.com/drojaazu/megadev)

生成摘要时出错

---

## 64. Meta and Google trial: are infinite scroll and autoplay creating addicts?

**原文标题**: Meta and Google trial: are infinite scroll and autoplay creating addicts?

**原文链接**: [https://www.theguardian.com/technology/2026/mar/14/meta-and-google-trial-are-infinite-scroll-and-autoplay-creating-addicts](https://www.theguardian.com/technology/2026/mar/14/meta-and-google-trial-are-infinite-scroll-and-autoplay-creating-addicts)

生成摘要时出错

---

## 65. Can I run AI locally?

**原文标题**: Can I run AI locally?

**原文链接**: [https://www.canirun.ai/](https://www.canirun.ai/)

生成摘要时出错

---

## 66. PSA: Top Google Result for Claude Code Is Malicious

**原文标题**: PSA: Top Google Result for Claude Code Is Malicious

**原文链接**: [https://onemillionwords.substack.com/p/top-google-result-for-claude-code](https://onemillionwords.substack.com/p/top-google-result-for-claude-code)

生成摘要时出错

---

## 67. XML is a cheap DSL

**原文标题**: XML is a cheap DSL

**原文链接**: [https://unplannedobsolescence.com/blog/xml-cheap-dsl/](https://unplannedobsolescence.com/blog/xml-cheap-dsl/)

生成摘要时出错

---

## 68. The Enterprise Context Layer

**原文标题**: The Enterprise Context Layer

**原文链接**: [https://andychen32.substack.com/p/the-enterprise-context-layer](https://andychen32.substack.com/p/the-enterprise-context-layer)

生成摘要时出错

---

## 69. Open Source PLFM Radar. Up to 20Km Range

**原文标题**: Open Source PLFM Radar. Up to 20Km Range

**原文链接**: [https://hackaday.io/project/205190-open-source-plfm-radar-up-to-20km-range/details](https://hackaday.io/project/205190-open-source-plfm-radar-up-to-20km-range/details)

生成摘要时出错

---

## 70. Show HN: GitAgent – An open standard that turns any Git repo into an AI agent

**原文标题**: Show HN: GitAgent – An open standard that turns any Git repo into an AI agent

**原文链接**: [https://www.gitagent.sh/](https://www.gitagent.sh/)

生成摘要时出错

---

## 71. Coding after coders: The end of computer programming as we know it?

**原文标题**: Coding after coders: The end of computer programming as we know it?

**原文链接**: [https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=url-share](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=url-share)

生成摘要时出错

---

## 72. Learning Creative Coding

**原文标题**: Learning Creative Coding

**原文链接**: [https://stigmollerhansen.dk/resume/learning-creative-coding/](https://stigmollerhansen.dk/resume/learning-creative-coding/)

生成摘要时出错

---

## 73. Z80-MBC2: a 4 ICs homebrew Z80 computer

**原文标题**: Z80-MBC2: a 4 ICs homebrew Z80 computer

**原文链接**: [https://hackaday.io/project/159973-z80-mbc2-a-4-ics-homebrew-z80-computer](https://hackaday.io/project/159973-z80-mbc2-a-4-ics-homebrew-z80-computer)

生成摘要时出错

---

## 74. Discovering Little Worlds (2020)

**原文标题**: Discovering Little Worlds (2020)

**原文链接**: [https://dmitrybrant.com/2020/08/01/discovering-little-worlds](https://dmitrybrant.com/2020/08/01/discovering-little-worlds)

生成摘要时出错

---

## 75. Changes to OpenTTD Distribution on Steam

**原文标题**: Changes to OpenTTD Distribution on Steam

**原文链接**: [https://www.openttd.org/news/2026/03/14/steam-changes](https://www.openttd.org/news/2026/03/14/steam-changes)

生成摘要时出错

---

## 76. Qatar helium shutdown puts chip supply chain on a two-week clock

**原文标题**: Qatar helium shutdown puts chip supply chain on a two-week clock

**原文链接**: [https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock](https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock)

生成摘要时出错

---

## 77. The Isolation Trap: Erlang

**原文标题**: The Isolation Trap: Erlang

**原文链接**: [https://causality.blog/essays/the-isolation-trap/](https://causality.blog/essays/the-isolation-trap/)

生成摘要时出错

---

## 78. Generalizing Knuth's Pseudocode Architecture From Algorithms to Knowledge

**原文标题**: Generalizing Knuth's Pseudocode Architecture From Algorithms to Knowledge

**原文链接**: [https://www.researchgate.net/publication/401189185_Towards_a_Generalization_of_Knuth%27s_Pseudocode_Architecture_From_Algorithms_to_Knowledge](https://www.researchgate.net/publication/401189185_Towards_a_Generalization_of_Knuth%27s_Pseudocode_Architecture_From_Algorithms_to_Knowledge)

生成摘要时出错

---

## 79. Launching the Claude Partner Network

**原文标题**: Launching the Claude Partner Network

**原文链接**: [https://www.anthropic.com/news/claude-partner-network](https://www.anthropic.com/news/claude-partner-network)

生成摘要时出错

---

## 80. Wired headphone sales are exploding

**原文标题**: Wired headphone sales are exploding

**原文链接**: [https://www.bbc.com/future/article/20260310-wired-headphones-are-better-than-bluetooth](https://www.bbc.com/future/article/20260310-wired-headphones-are-better-than-bluetooth)

生成摘要时出错

---

## 81. I beg you to follow Crocker's Rules, even if you will be rude to me

**原文标题**: I beg you to follow Crocker's Rules, even if you will be rude to me

**原文链接**: [https://lr0.org/blog/p/crocker/](https://lr0.org/blog/p/crocker/)

生成摘要时出错

---

## 82. The mechanics of autonomous software translation

**原文标题**: The mechanics of autonomous software translation

**原文链接**: [https://alperenkeles.com/posts/autonomous-translations/](https://alperenkeles.com/posts/autonomous-translations/)

生成摘要时出错

---

## 83. Show HN: GrobPaint: Somewhere Between MS Paint and Paint.net

**原文标题**: Show HN: GrobPaint: Somewhere Between MS Paint and Paint.net

**原文链接**: [https://github.com/groverburger/grobpaint](https://github.com/groverburger/grobpaint)

生成摘要时出错

---

## 84. Linux 7.0 Lands Improvements to Deal with Rust Changes, Build Reproducibility

**原文标题**: Linux 7.0 Lands Improvements to Deal with Rust Changes, Build Reproducibility

**原文链接**: [https://www.phoronix.com/news/Linux-7.0-rc4-More-Rust](https://www.phoronix.com/news/Linux-7.0-rc4-More-Rust)

生成摘要时出错

---

## 85. Life as an OnlyFans 'chatter'

**原文标题**: Life as an OnlyFans 'chatter'

**原文链接**: [https://www.bbc.com/news/articles/cq571g9gd4lo](https://www.bbc.com/news/articles/cq571g9gd4lo)

生成摘要时出错

---

## 86. An interactive presentation about the Grammar of Graphic

**原文标题**: An interactive presentation about the Grammar of Graphic

**原文链接**: [https://timeplus-io.github.io/gg-vistral-introduction/](https://timeplus-io.github.io/gg-vistral-introduction/)

生成摘要时出错

---

## 87. Python: The Optimization Ladder

**原文标题**: Python: The Optimization Ladder

**原文链接**: [https://cemrehancavdar.com/2026/03/10/optimization-ladder/](https://cemrehancavdar.com/2026/03/10/optimization-ladder/)

生成摘要时出错

---

## 88. Everything you never wanted to know about visually-hidden

**原文标题**: Everything you never wanted to know about visually-hidden

**原文链接**: [https://dbushell.com/2026/02/20/visually-hidden/](https://dbushell.com/2026/02/20/visually-hidden/)

生成摘要时出错

---

## 89. Games with loot boxes to get minimum 16 age rating across Europe

**原文标题**: Games with loot boxes to get minimum 16 age rating across Europe

**原文链接**: [https://www.bbc.com/news/articles/cge84xqjg5lo](https://www.bbc.com/news/articles/cge84xqjg5lo)

生成摘要时出错

---

## 90. Sunsetting Jazzband

**原文标题**: Sunsetting Jazzband

**原文链接**: [https://jazzband.co/news/2026/03/14/sunsetting-jazzband](https://jazzband.co/news/2026/03/14/sunsetting-jazzband)

生成摘要时出错

---

## 91. Nmap in the movies (2008)

**原文标题**: Nmap in the movies (2008)

**原文链接**: [https://nmap.org/movies/](https://nmap.org/movies/)

生成摘要时出错

---

## 92. An old photo of a large BBS (2022)

**原文标题**: An old photo of a large BBS (2022)

**原文链接**: [https://rachelbythebay.com/w/2022/01/26/swcbbs/](https://rachelbythebay.com/w/2022/01/26/swcbbs/)

生成摘要时出错

---

## 93. Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas

**原文标题**: Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas

**原文链接**: [https://www.getspine.ai/](https://www.getspine.ai/)

生成摘要时出错

---

## 94. Malus – Clean Room as a Service

**原文标题**: Malus – Clean Room as a Service

**原文链接**: [https://malus.sh](https://malus.sh)

生成摘要时出错

---

## 95. Elon Musk pushes out more xAI founders as AI coding effort falters

**原文标题**: Elon Musk pushes out more xAI founders as AI coding effort falters

**原文链接**: [https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

生成摘要时出错

---

## 96. It's time to move your docs in the repo

**原文标题**: It's time to move your docs in the repo

**原文链接**: [https://www.dein.fr/posts/2026-03-13-its-time-to-move-your-docs-in-the-repo](https://www.dein.fr/posts/2026-03-13-its-time-to-move-your-docs-in-the-repo)

生成摘要时出错

---

## 97. Show HN: Channel Surfer – Watch YouTube like it’s cable TV

**原文标题**: Show HN: Channel Surfer – Watch YouTube like it’s cable TV

**原文链接**: [https://channelsurfer.tv](https://channelsurfer.tv)

生成摘要时出错

---

## 98. We turned plastic waste into vinegar: A sunlight-powered breakthrough

**原文标题**: We turned plastic waste into vinegar: A sunlight-powered breakthrough

**原文链接**: [https://phys.org/news/2026-03-plastic-vinegar-sunlightpowered-breakthrough.html](https://phys.org/news/2026-03-plastic-vinegar-sunlightpowered-breakthrough.html)

生成摘要时出错

---

## 99. ArXiv is establishing itself as an independent nonprofit organization

**原文标题**: ArXiv is establishing itself as an independent nonprofit organization

**原文链接**: [https://jobs.chronicle.com/job/37961678/chief-executive-officer](https://jobs.chronicle.com/job/37961678/chief-executive-officer)

生成摘要时出错

---

## 100. New 'negative light' technology hides data transfers in plain sight

**原文标题**: New 'negative light' technology hides data transfers in plain sight

**原文链接**: [https://www.unsw.edu.au/newsroom/news/2026/03/New-negative-light-technology-hides-data-transfers-in-plain-sight](https://www.unsw.edu.au/newsroom/news/2026/03/New-negative-light-technology-hides-data-transfers-in-plain-sight)

生成摘要时出错

---

