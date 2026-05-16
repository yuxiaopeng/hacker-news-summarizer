# Hacker News 热门文章摘要 (2026-05-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Project Gutenberg – keeps getting better

**原文标题**: Project Gutenberg – keeps getting better

**原文链接**: [https://www.gutenberg.org/](https://www.gutenberg.org/)

生成摘要时出错

---

## 12. Greek Alphabet Cards

**原文标题**: Greek Alphabet Cards

**原文链接**: [https://labs.randomquark.com/alphabet_cards/](https://labs.randomquark.com/alphabet_cards/)

生成摘要时出错

---

## 13. Futhark by Example

**原文标题**: Futhark by Example

**原文链接**: [https://futhark-lang.org/examples.html](https://futhark-lang.org/examples.html)

生成摘要时出错

---

## 14. Nearly 50 Years Later, WKRP in Cincinnati Becomes a Real Radio Station

**原文标题**: Nearly 50 Years Later, WKRP in Cincinnati Becomes a Real Radio Station

**原文链接**: [https://www.openculture.com/2026/05/nearly-50-years-later-wkrp-in-cincinnati-becomes-a-real-radio-station.html](https://www.openculture.com/2026/05/nearly-50-years-later-wkrp-in-cincinnati-becomes-a-real-radio-station.html)

生成摘要时出错

---

## 15. After 8 years, I rewrote my open-source PyTorch curvature library

**原文标题**: After 8 years, I rewrote my open-source PyTorch curvature library

**原文链接**: [https://github.com/noahgolmant/pytorch-hessian-eigenthings](https://github.com/noahgolmant/pytorch-hessian-eigenthings)

生成摘要时出错

---

## 16. Clusters become personal (like PCs did)

**原文标题**: Clusters become personal (like PCs did)

**原文链接**: [https://aranya.tech/blog/arrival-of-the-personal-cluster](https://aranya.tech/blog/arrival-of-the-personal-cluster)

生成摘要时出错

---

## 17. Kyber (YC W23) Is Hiring a Founding Marketer

**原文标题**: Kyber (YC W23) Is Hiring a Founding Marketer

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community](https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community)

生成摘要时出错

---

## 18. I believe there are entire companies right now under AI psychosis

**原文标题**: I believe there are entire companies right now under AI psychosis

**原文链接**: [https://twitter.com/mitchellh/status/2055380239711457578](https://twitter.com/mitchellh/status/2055380239711457578)

生成摘要时出错

---

## 19. Ploopy Bean: a trackpoint for every computer

**原文标题**: Ploopy Bean: a trackpoint for every computer

**原文链接**: [https://ploopy.co/shop/bean-pointing-stick/](https://ploopy.co/shop/bean-pointing-stick/)

生成摘要时出错

---

## 20. Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

**原文标题**: Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

**原文链接**: [https://github.com/chiennv2000/orthrus](https://github.com/chiennv2000/orthrus)

生成摘要时出错

---

## 21. The bird eye was pushed to an evolutionary extreme

**原文标题**: The bird eye was pushed to an evolutionary extreme

**原文链接**: [https://www.quantamagazine.org/how-the-bird-eye-was-pushed-to-an-evolutionary-extreme-20260513/](https://www.quantamagazine.org/how-the-bird-eye-was-pushed-to-an-evolutionary-extreme-20260513/)

生成摘要时出错

---

## 22. What Were Ancient Greco-Roman Curse Tablets?

**原文标题**: What Were Ancient Greco-Roman Curse Tablets?

**原文链接**: [https://www.history.com/articles/what-were-ancient-roman-curse-tablets](https://www.history.com/articles/what-were-ancient-roman-curse-tablets)

生成摘要时出错

---

## 23. Gaining control of every projector and camera on campus

**原文标题**: Gaining control of every projector and camera on campus

**原文链接**: [https://www.edna.land/blogs/posts/scanning/](https://www.edna.land/blogs/posts/scanning/)

生成摘要时出错

---

## 24. A 0-click exploit chain for the Pixel 10

**原文标题**: A 0-click exploit chain for the Pixel 10

**原文链接**: [https://projectzero.google/2026/05/pixel-10-exploit.html](https://projectzero.google/2026/05/pixel-10-exploit.html)

生成摘要时出错

---

## 25. Fecal transplants for autism deliver success in clinical trials

**原文标题**: Fecal transplants for autism deliver success in clinical trials

**原文链接**: [https://refractor.io/adhd-autism/fecal-transplants-for-autism-delivers-success-in-clinical-trials/](https://refractor.io/adhd-autism/fecal-transplants-for-autism-delivers-success-in-clinical-trials/)

生成摘要时出错

---

## 26. The sigmoids won't save you

**原文标题**: The sigmoids won't save you

**原文链接**: [https://www.astralcodexten.com/p/the-sigmoids-wont-save-you](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you)

生成摘要时出错

---

## 27. Frontier AI has broken the open CTF format

**原文标题**: Frontier AI has broken the open CTF format

**原文链接**: [https://kabir.au/blog/the-ctf-scene-is-dead](https://kabir.au/blog/the-ctf-scene-is-dead)

生成摘要时出错

---

## 28. The main thing about P2P meth is that there's so much of it (2021)

**原文标题**: The main thing about P2P meth is that there's so much of it (2021)

**原文链接**: [https://dynomight.net/p2p-meth/](https://dynomight.net/p2p-meth/)

生成摘要时出错

---

## 29. The Physics–and Physicality–Of Extreme Juggling (2018)

**原文标题**: The Physics–and Physicality–Of Extreme Juggling (2018)

**原文链接**: [https://www.wired.com/story/the-physicsand-physicalityof-extreme-juggling/](https://www.wired.com/story/the-physicsand-physicalityof-extreme-juggling/)

生成摘要时出错

---

## 30. Naturally Occurring Quasicrystals

**原文标题**: Naturally Occurring Quasicrystals

**原文链接**: [https://johncarlosbaez.wordpress.com/2026/05/14/naturally-occurring-quasicrystals/](https://johncarlosbaez.wordpress.com/2026/05/14/naturally-occurring-quasicrystals/)

生成摘要时出错

---

## 31. Impeaching Every Federal Judge and Justice Who Endorsed Unitary Executive Theory

**原文标题**: Impeaching Every Federal Judge and Justice Who Endorsed Unitary Executive Theory

**原文链接**: [https://cmarmitage.substack.com/p/the-case-for-impeaching-and-removing](https://cmarmitage.substack.com/p/the-case-for-impeaching-and-removing)

生成摘要时出错

---

## 32. England Runestones

**原文标题**: England Runestones

**原文链接**: [https://en.wikipedia.org/wiki/England_runestones](https://en.wikipedia.org/wiki/England_runestones)

生成摘要时出错

---

## 33. Additive Blending on the Nintendo 64

**原文标题**: Additive Blending on the Nintendo 64

**原文链接**: [https://phoboslab.org/log/2026/05/n64-additive-blending](https://phoboslab.org/log/2026/05/n64-additive-blending)

生成摘要时出错

---

## 34. How to Write to SSDs [pdf]

**原文标题**: How to Write to SSDs [pdf]

**原文链接**: [https://www.vldb.org/pvldb/vol19/p1469-lee.pdf](https://www.vldb.org/pvldb/vol19/p1469-lee.pdf)

生成摘要时出错

---

## 35. Bill to block publishers from killing online games advances in California

**原文标题**: Bill to block publishers from killing online games advances in California

**原文链接**: [https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/)

生成摘要时出错

---

## 36. Charity – Categorical programming language (1998)

**原文标题**: Charity – Categorical programming language (1998)

**原文链接**: [https://github.com/mietek/charity-lang/blob/master/doc/README.md](https://github.com/mietek/charity-lang/blob/master/doc/README.md)

生成摘要时出错

---

## 37. Where to buy a non-Apple, non-Google smartphone

**原文标题**: Where to buy a non-Apple, non-Google smartphone

**原文链接**: [https://www.theregister.com/on-prem/2026/05/01/where-to-buy-a-non-apple-non-google-smartphone/5219681](https://www.theregister.com/on-prem/2026/05/01/where-to-buy-a-non-apple-non-google-smartphone/5219681)

生成摘要时出错

---

## 38. Image-blaster: Creates 3D environments, SFX, and meshes from a single image

**原文标题**: Image-blaster: Creates 3D environments, SFX, and meshes from a single image

**原文链接**: [https://github.com/neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster)

生成摘要时出错

---

## 39. I designed a nibble-oriented CPU in Verilog to build a scientific calculator

**原文标题**: I designed a nibble-oriented CPU in Verilog to build a scientific calculator

**原文链接**: [https://github.com/gdevic/FPGA-Calculator](https://github.com/gdevic/FPGA-Calculator)

生成摘要时出错

---

## 40. Show HN: Watch a neural net learn to play Snake

**原文标题**: Show HN: Watch a neural net learn to play Snake

**原文链接**: [https://ppo.gradexp.xyz/](https://ppo.gradexp.xyz/)

生成摘要时出错

---

## 41. ESP-EEG is an affordable 8-channel biosensing board

**原文标题**: ESP-EEG is an affordable 8-channel biosensing board

**原文链接**: [https://www.autodidacts.io/cerelog-esp-eeg-affordable-openbci-like-board/](https://www.autodidacts.io/cerelog-esp-eeg-affordable-openbci-like-board/)

生成摘要时出错

---

## 42. Mode collapse has a name, and he's selling cancer treatment advice on Amazon

**原文标题**: Mode collapse has a name, and he's selling cancer treatment advice on Amazon

**原文链接**: [https://danielmay.co.uk/posts/cheap-agents-alumni-shirts-and-elias-thorne/](https://danielmay.co.uk/posts/cheap-agents-alumni-shirts-and-elias-thorne/)

生成摘要时出错

---

## 43. ASCII by Jason Scott

**原文标题**: ASCII by Jason Scott

**原文链接**: [https://ascii.textfiles.com/](https://ascii.textfiles.com/)

生成摘要时出错

---

## 44. Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

**原文标题**: Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

**原文链接**: [https://github.com/oven-sh/bun/issues/30719](https://github.com/oven-sh/bun/issues/30719)

生成摘要时出错

---

## 45. The Zulip Foundation

**原文标题**: The Zulip Foundation

**原文链接**: [https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/)

生成摘要时出错

---

## 46. A Tiny E Reader

**原文标题**: A Tiny E Reader

**原文链接**: [https://nthp.me/blog/2026/a-tiny-e-reader/](https://nthp.me/blog/2026/a-tiny-e-reader/)

生成摘要时出错

---

## 47. Radicle: Sovereign {code forge} built on Git

**原文标题**: Radicle: Sovereign {code forge} built on Git

**原文链接**: [https://radicle.dev/](https://radicle.dev/)

生成摘要时出错

---

## 48. OpenAI is connecting ChatGPT to bank accounts via Plaid

**原文标题**: OpenAI is connecting ChatGPT to bank accounts via Plaid

**原文链接**: [https://firethering.com/chatgpt-bank-account-plaid-openai/](https://firethering.com/chatgpt-bank-account-plaid-openai/)

生成摘要时出错

---

## 49. Research on mildew contamination affecting the sound quality of analog tapes

**原文标题**: Research on mildew contamination affecting the sound quality of analog tapes

**原文链接**: [https://www.nature.com/articles/s40494-026-02592-7](https://www.nature.com/articles/s40494-026-02592-7)

生成摘要时出错

---

## 50. EMiX: Emulating Beyond Single-FPGA Limits

**原文标题**: EMiX: Emulating Beyond Single-FPGA Limits

**原文链接**: [https://arxiv.org/abs/2604.27012](https://arxiv.org/abs/2604.27012)

生成摘要时出错

---

## 51. Erlang/OTP 29.0

**原文标题**: Erlang/OTP 29.0

**原文链接**: [https://www.erlang.org/news/188](https://www.erlang.org/news/188)

生成摘要时出错

---

## 52. Microsoft Exchange, Windows 11 hacked on second day of Pwn2Own

**原文标题**: Microsoft Exchange, Windows 11 hacked on second day of Pwn2Own

**原文链接**: [https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)

生成摘要时出错

---

## 53. I love Linux, but I can't quit Windows

**原文标题**: I love Linux, but I can't quit Windows

**原文链接**: [https://jpain.io/i-love-linux-but-i-cant-quit-windows/](https://jpain.io/i-love-linux-but-i-cant-quit-windows/)

生成摘要时出错

---

## 54. SQL patterns I use to catch transaction fraud

**原文标题**: SQL patterns I use to catch transaction fraud

**原文链接**: [https://analytics.fixelsmith.com/posts/sql-fraud-patterns/](https://analytics.fixelsmith.com/posts/sql-fraud-patterns/)

生成摘要时出错

---

## 55. Removing the modem and GPS from my 2024 RAV4 hybrid

**原文标题**: Removing the modem and GPS from my 2024 RAV4 hybrid

**原文链接**: [https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/)

生成摘要时出错

---

## 56. High dimensional geometry is transforming the MRI industry (2017) [pdf]

**原文标题**: High dimensional geometry is transforming the MRI industry (2017) [pdf]

**原文链接**: [https://www.ams.org/government/DonohoPresentation06-28-17Final.pdf](https://www.ams.org/government/DonohoPresentation06-28-17Final.pdf)

生成摘要时出错

---

## 57. Welcome to the Strip Mining Era of OSS Security

**原文标题**: Welcome to the Strip Mining Era of OSS Security

**原文链接**: [https://www.metabase.com/blog/strip-mining-era-of-open-source-security](https://www.metabase.com/blog/strip-mining-era-of-open-source-security)

生成摘要时出错

---

## 58. Waymo updates 3,800 robotaxis after they 'drive into standing water'

**原文标题**: Waymo updates 3,800 robotaxis after they 'drive into standing water'

**原文链接**: [https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html)

生成摘要时出错

---

## 59. U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app

**原文标题**: U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app

**原文链接**: [https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/)

生成摘要时出错

---

## 60. The nuclear-physics infrastructure behind PET scans

**原文标题**: The nuclear-physics infrastructure behind PET scans

**原文链接**: [https://www.lanl.gov/media/publications/1663/proton-power-for-public-health](https://www.lanl.gov/media/publications/1663/proton-power-for-public-health)

生成摘要时出错

---

## 61. ABC News has taken all FiveThirtyEight articles offline

**原文标题**: ABC News has taken all FiveThirtyEight articles offline

**原文链接**: [https://twitter.com/baseballot/status/2055309076209492208](https://twitter.com/baseballot/status/2055309076209492208)

生成摘要时出错

---

## 62. Tesla reveals two Robotaxi crashes involving teleoperators

**原文标题**: Tesla reveals two Robotaxi crashes involving teleoperators

**原文链接**: [https://techcrunch.com/2026/05/15/tesla-reveals-two-robotaxi-crashes-involving-teleoperators/](https://techcrunch.com/2026/05/15/tesla-reveals-two-robotaxi-crashes-involving-teleoperators/)

生成摘要时出错

---

## 63. Show HN: Epiq – Distributed Git based issue tracker TUI

**原文标题**: Show HN: Epiq – Distributed Git based issue tracker TUI

**原文链接**: [https://ljtn.github.io/epiq/](https://ljtn.github.io/epiq/)

生成摘要时出错

---

## 64. Building a UMatrix Replacement

**原文标题**: Building a UMatrix Replacement

**原文链接**: [https://lock.cmpxchg8b.com/umatrix.html](https://lock.cmpxchg8b.com/umatrix.html)

生成摘要时出错

---

## 65. Feedr v0.8.0 – a TUI RSS reader, now read the full article from your terminal

**原文标题**: Feedr v0.8.0 – a TUI RSS reader, now read the full article from your terminal

**原文链接**: [https://github.com/bahdotsh/feedr](https://github.com/bahdotsh/feedr)

生成摘要时出错

---

## 66. Gyroflow: Video stabilization using gyroscope data

**原文标题**: Gyroflow: Video stabilization using gyroscope data

**原文链接**: [https://github.com/gyroflow/gyroflow](https://github.com/gyroflow/gyroflow)

生成摘要时出错

---

## 67. Microscale Thermite Reaction

**原文标题**: Microscale Thermite Reaction

**原文链接**: [https://sciencedemonstrations.fas.harvard.edu/presentations/microscale-thermite-reaction](https://sciencedemonstrations.fas.harvard.edu/presentations/microscale-thermite-reaction)

生成摘要时出错

---

## 68. Amazon workers under pressure to up their AI usage are making up tasks

**原文标题**: Amazon workers under pressure to up their AI usage are making up tasks

**原文链接**: [https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks](https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks)

生成摘要时出错

---

## 69. Explore Wikipedia Like a Windows XP Desktop

**原文标题**: Explore Wikipedia Like a Windows XP Desktop

**原文链接**: [https://explorer.samismith.com/](https://explorer.samismith.com/)

生成摘要时出错

---

## 70. Meta to cut 8000 employees despite $26B Q1 net income

**原文标题**: Meta to cut 8000 employees despite $26B Q1 net income

**原文链接**: [https://moneywise.com/news/top-stories/meta-layoffs-8000-workers-zuckerberg-ai-spending](https://moneywise.com/news/top-stories/meta-layoffs-8000-workers-zuckerberg-ai-spending)

生成摘要时出错

---

## 71. Git Is Not Fine

**原文标题**: Git Is Not Fine

**原文链接**: [https://www.billjings.com/posts/title/git-is-not-fine/](https://www.billjings.com/posts/title/git-is-not-fine/)

生成摘要时出错

---

## 72. Solar-based sleep patterns compared to modern norms

**原文标题**: Solar-based sleep patterns compared to modern norms

**原文链接**: [https://dylan.gr/1775146616](https://dylan.gr/1775146616)

生成摘要时出错

---

## 73. Claude for Legal

**原文标题**: Claude for Legal

**原文链接**: [https://github.com/anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal)

生成摘要时出错

---

## 74. A SQL-Inspired Query Language Designed for Event Sourcing (2025)

**原文标题**: A SQL-Inspired Query Language Designed for Event Sourcing (2025)

**原文链接**: [https://yoeight.github.io/blog/2025/12/21/EventQL_A_SQL_Inspired_Query_Language_Designed_For_Event_Sourcing.html](https://yoeight.github.io/blog/2025/12/21/EventQL_A_SQL_Inspired_Query_Language_Designed_For_Event_Sourcing.html)

生成摘要时出错

---

## 75. Zenith: a live local-first fixed viewport planetarium

**原文标题**: Zenith: a live local-first fixed viewport planetarium

**原文链接**: [https://smorgasb.org/zenith-tech/](https://smorgasb.org/zenith-tech/)

生成摘要时出错

---

## 76. Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文标题**: Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文链接**: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

生成摘要时出错

---

## 77. 'No way to prevent this,' says only package manager where this regularly happens

**原文标题**: 'No way to prevent this,' says only package manager where this regularly happens

**原文链接**: [https://kevinpatel.xyz/posts/no-way-to-prevent-this/](https://kevinpatel.xyz/posts/no-way-to-prevent-this/)

生成摘要时出错

---

## 78. Show HN: Burn, baby, burn (those tokens)

**原文标题**: Show HN: Burn, baby, burn (those tokens)

**原文链接**: [https://github.com/dtnewman/burn-baby-burn](https://github.com/dtnewman/burn-baby-burn)

生成摘要时出错

---

## 79. Prepare for an AI Jobs Apocalypse

**原文标题**: Prepare for an AI Jobs Apocalypse

**原文链接**: [https://www.economist.com/leaders/2026/05/14/prepare-for-an-ai-jobs-apocalypse](https://www.economist.com/leaders/2026/05/14/prepare-for-an-ai-jobs-apocalypse)

生成摘要时出错

---

## 80. Why 'Smart' Products Have Started to Look Like the Dumb Choice

**原文标题**: Why 'Smart' Products Have Started to Look Like the Dumb Choice

**原文链接**: [https://www.nytimes.com/2026/05/14/magazine/dumb-phones-tvs-retronym-smart-tech.html](https://www.nytimes.com/2026/05/14/magazine/dumb-phones-tvs-retronym-smart-tech.html)

生成摘要时出错

---

## 81. Tesla Wall Connector bootloader bypasses the firmware downgrade ratchet

**原文标题**: Tesla Wall Connector bootloader bypasses the firmware downgrade ratchet

**原文链接**: [https://www.synacktiv.com/en/publications/exploiting-the-tesla-wall-connector-from-its-charge-port-connector-part-2-bypassing](https://www.synacktiv.com/en/publications/exploiting-the-tesla-wall-connector-from-its-charge-port-connector-part-2-bypassing)

生成摘要时出错

---

## 82. Building ML framework with Rust and Category Theory

**原文标题**: Building ML framework with Rust and Category Theory

**原文链接**: [https://hghalebi.github.io/category_theory_transformer_rs/](https://hghalebi.github.io/category_theory_transformer_rs/)

生成摘要时出错

---

## 83. What's in a GGUF, besides the weights – and what's still missing?

**原文标题**: What's in a GGUF, besides the weights – and what's still missing?

**原文链接**: [https://nobodywho.ooo/posts/whats-in-a-gguf/](https://nobodywho.ooo/posts/whats-in-a-gguf/)

生成摘要时出错

---

## 84. DeepSeek V4: The Open-Source Model Frontier Labs Feared

**原文标题**: DeepSeek V4: The Open-Source Model Frontier Labs Feared

**原文链接**: [https://helloai.com/articles/deepseek-v4-open-source-frontier-parity](https://helloai.com/articles/deepseek-v4-open-source-frontier-parity)

生成摘要时出错

---

## 85. OpenClaw Creator Spent $1.3M on OpenAI Tokens in 30 Days

**原文标题**: OpenClaw Creator Spent $1.3M on OpenAI Tokens in 30 Days

**原文链接**: [https://twitter.com/steipete/status/2055346265869721905](https://twitter.com/steipete/status/2055346265869721905)

生成摘要时出错

---

## 86. RTX 5090 and M4 MacBook Air: Can It Game?

**原文标题**: RTX 5090 and M4 MacBook Air: Can It Game?

**原文链接**: [https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

生成摘要时出错

---

## 87. The Emacsification of Software

**原文标题**: The Emacsification of Software

**原文链接**: [https://sockpuppet.org/blog/2026/05/12/emacsification/](https://sockpuppet.org/blog/2026/05/12/emacsification/)

生成摘要时出错

---

## 88. NanoTDB – Golang Append-Only Time Series DB

**原文标题**: NanoTDB – Golang Append-Only Time Series DB

**原文链接**: [https://github.com/aymanhs/nanotdb](https://github.com/aymanhs/nanotdb)

生成摘要时出错

---

## 89. A few words on DS4

**原文标题**: A few words on DS4

**原文链接**: [https://antirez.com/news/165](https://antirez.com/news/165)

生成摘要时出错

---

## 90. O(x)Caml in Space

**原文标题**: O(x)Caml in Space

**原文链接**: [https://gazagnaire.org/blog/2026-05-14-borealis.html](https://gazagnaire.org/blog/2026-05-14-borealis.html)

生成摘要时出错

---

## 91. I Bought a “Junk” PSP From Japan

**原文标题**: I Bought a “Junk” PSP From Japan

**原文链接**: [https://gardinerbryant.com/i-bought-a-junk-psp-from-japan-heres-how-it-went/](https://gardinerbryant.com/i-bought-a-junk-psp-from-japan-heres-how-it-went/)

生成摘要时出错

---

## 92. Why Spain has the greatest cities

**原文标题**: Why Spain has the greatest cities

**原文链接**: [https://worksinprogress.co/issue/why-spain-has-the-worlds-greatest-cities/](https://worksinprogress.co/issue/why-spain-has-the-worlds-greatest-cities/)

生成摘要时出错

---

## 93. Steve Jobs in Exile – New book on his years at NeXT Computer

**原文标题**: Steve Jobs in Exile – New book on his years at NeXT Computer

**原文链接**: [https://spectrum.ieee.org/steve-jobs-next-computer](https://spectrum.ieee.org/steve-jobs-next-computer)

生成摘要时出错

---

## 94. The day the Pintupi Nine entered the modern world (2014)

**原文标题**: The day the Pintupi Nine entered the modern world (2014)

**原文链接**: [https://www.bbc.com/news/magazine-30500591](https://www.bbc.com/news/magazine-30500591)

生成摘要时出错

---

## 95. Mullvad exit IPs are surprisingly identifying

**原文标题**: Mullvad exit IPs are surprisingly identifying

**原文链接**: [https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/)

生成摘要时出错

---

## 96. First public macOS kernel memory corruption exploit on Apple M5

**原文标题**: First public macOS kernel memory corruption exploit on Apple M5

**原文链接**: [https://blog.calif.io/p/first-public-kernel-memory-corruption](https://blog.calif.io/p/first-public-kernel-memory-corruption)

生成摘要时出错

---

## 97. Echoes (Live at Pompeii) (1972)

**原文标题**: Echoes (Live at Pompeii) (1972)

**原文链接**: [https://genius.com/Pink-floyd-echoes-live-at-pompeii-lyrics](https://genius.com/Pink-floyd-echoes-live-at-pompeii-lyrics)

生成摘要时出错

---

## 98. Porting 3D Movie Maker to Linux

**原文标题**: Porting 3D Movie Maker to Linux

**原文链接**: [https://benstoneonline.com/posts/porting-3d-movie-maker-to-linux/](https://benstoneonline.com/posts/porting-3d-movie-maker-to-linux/)

生成摘要时出错

---

## 99. UK government replaces Palantir software with internally-built refugee system

**原文标题**: UK government replaces Palantir software with internally-built refugee system

**原文链接**: [https://www.bbc.com/news/articles/c2l2j1lxdk5o](https://www.bbc.com/news/articles/c2l2j1lxdk5o)

生成摘要时出错

---

## 100. Codex is now in the ChatGPT mobile app

**原文标题**: Codex is now in the ChatGPT mobile app

**原文链接**: [https://openai.com/index/work-with-codex-from-anywhere/](https://openai.com/index/work-with-codex-from-anywhere/)

生成摘要时出错

---

