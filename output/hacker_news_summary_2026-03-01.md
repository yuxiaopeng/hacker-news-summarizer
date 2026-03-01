# Hacker News 热门文章摘要 (2026-03-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Ghostty – 终端模拟器

**原文标题**: Ghostty – Terminal Emulator

**原文链接**: [https://ghostty.org/docs](https://ghostty.org/docs)

Ghostty 是一款快速、跨平台的终端模拟器，旨在提供高性能和原生用户体验。通过利用 GPU 加速和平台原生 UI 组件，它提供了一个流畅的界面，无需任何配置即可上手使用。

主要特性和信息包括：

*   **平台支持：** Ghostty 为 macOS 提供开箱即用的二进制文件，并为 Linux 提供多种软件包或支持源码编译。
*   **自定义：** 该模拟器非常灵活，提供数百个配置选项和可自定义的快捷键绑定，以适应个人的工作流。
*   **视觉效果：** 它内置了数百种配色方案，并原生支持在明亮和暗黑模式之间切换。
*   **开发者资源：** 对于终端应用开发者，Ghostty 提供了全面的 API 参考，涵盖了终端概念和支持的 VT 控制序列。

总的来说，Ghostty 专注于将速度和性能与“开箱即用”的理念相结合，使其在易于初学者上手的同时，依然能满足高级用户深度配置的需求。

---

## 2. 微GPT

**原文标题**: Microgpt

**原文链接**: [http://karpathy.github.io/2026/02/12/microgpt/](http://karpathy.github.io/2026/02/12/microgpt/)

“Microgpt” 是 Andrej Karpathy 发起的一个极简主义艺术项目，它将一个功能齐全的大语言模型（LLM）浓缩成了仅 200 行且没有任何依赖的纯 Python 代码。它代表了 GPT-4 等模型背后技术的最核心要素，涵盖了从数据处理到推理的完整流水线。

该项目包含几个核心组件：
*   **数据集与分词器（Tokenizer）：** 它使用了一个包含 32,000 个名字的数据集，以及一个简单的字符级分词器（26 个字母加上一个“序列开始”标记），将文本转换为整数 ID。
*   **自动求导引擎（Autograd Engine）：** 其核心是一个自定义的 `Value` 类，实现了一个标量级的自动求导引擎。它通过链式法则手动处理反向传播，使模型能够计算优化所需的梯度。
*   **架构：** 该模型采用了简化的 GPT-2 设计，具有 RMSNorm、线性变换、多头注意力机制和 MLP 模块。它包含约 4,192 个随机初始化的参数。
*   **训练与推理：** 脚本包含一个 Adam 优化器和一个训练循环，通过迭代微调参数来降低损失。训练完成后，模型通过预测序列中的下一个字符，生成听起来真实的新名字。

该项目证明了 LLM 本质上是“统计学文档补全器”。通过在特定模式（名字）上进行训练，模型学会了“幻觉”出符合输入统计分布的新条目。Karpathy 将此视为其此前作品（如 micrograd 和 nanogpt）在教学意义上的集大成之作，旨在展示：在剥离了追求效率的复杂性后，AI 的底层算法在数学上是优雅且出奇简单的。

---

## 3. AI Made Writing Code Easier. It Made Being an Engineer Harder

**原文标题**: AI Made Writing Code Easier. It Made Being an Engineer Harder

**原文链接**: [https://www.ivanturkovic.com/2026/02/25/ai-made-writing-code-easier-engineering-harder/](https://www.ivanturkovic.com/2026/02/25/ai-made-writing-code-easier-engineering-harder/)

生成摘要时出错

---

## 4. 约旦河西岸的罪恶——戴维·舒尔曼

**原文标题**: Evil in the West Bank – David Shulman

**原文链接**: [https://www.nybooks.com/articles/2026/03/12/evil-in-the-west-bank-david-shulman/](https://www.nybooks.com/articles/2026/03/12/evil-in-the-west-bank-david-shulman/)

在《约旦河西岸之恶》（Evil in the West Bank）一书中，大卫·舒尔曼记录了贝都因村庄拉斯阿因（Ras al-‘Ain）的毁灭，并将其视为C区系统性种族清洗运动的一个缩影。通过定居者的暴力行为——包括盗窃牲畜、身体攻击和非法强占土地——巴勒斯坦居民在以色列军方以及现由极端主义部长伊塔马尔·本-格维尔监管的警方的默许下被迫流离失所。舒尔曼报告称，拉斯阿因是近年来第86个被摧毁的村庄，他将这一过程描述为一场“重大的道德灾难”。

舒尔曼认为，这种局部暴力与本雅明·内塔尼亚胡政府领导下对以色列民主更广泛的冲击密不可分。他详细列举了拆除法治的种种行径，包括：
* 试图通过取消阿拉伯政党资格来操纵选举的立法企图。
* 司法机构对右翼政客的从属化。
* 旨在追溯性保护总理免受腐败指控的法律。

作者指出了当前驱动以色列政策的四大有毒意识形态支柱：坚信土地排他性地属于犹太人、将国家提升为形而上学的实体、对犹太至上主义/种族隔离的痴迷，以及对武力而非国际合法性的依赖。他警告说，这种追求永久战争的“超级斯巴达”式手段是自我毁灭的药方。

尽管舒尔曼承认“巴勒斯坦甘地”的存在，以及以色列社会中仍有一部分人致力于普世价值与和平，但他得出结论称，该国正处于一段“任性的熵增”时期。他断言，只有承认巴勒斯坦人的尊严并结束目前正“侵蚀”国家核心的残酷占领，以色列在道德和制度上的瓦解才能被遏制。

---

## 5. 长续航电动自行车

**原文标题**: Long Range E-Bike

**原文链接**: [https://jacquesmattheij.com/long-range-ebike/](https://jacquesmattheij.com/long-range-ebike/)

本文详细介绍了作者为 S-Pedelec 电动自行车打造定制高容量电池，从而克服“里程焦虑”的历程。尽管电动自行车非常适合通勤，但作者发现标准 500 Wh 电池的续航里程不足，尤其是对于耗电量更大的高速车型（时速 45 公里）。

主要障碍在于博世（Bosch）电动自行车系统的专有“DRM”设置，该设置禁止使用第三方电池。为了绕过这一限制，作者拆解并利用了一套博世电池管理系统（BMS），并搭配外部蓝牙均衡器来监控电池组。最终成品使用了 170 节三星 E35 电芯，采用 10S17P 配置，容量达 2150 Wh，是标准容量的四倍以上。

作者强调了该项目中的技术与安全挑战，包括：
*   **安全：** 处理高能量锂电池组被比作拆解“定时炸弹”。
*   **构造：** 使用绝缘的 Trespa 外壳，并将电池组安装在车架内以保持低重心。
*   **制造：** 克服家用电源限制对电芯进行点焊。

实验结果非常成功。该自行车目前在全功率下续航里程可达 180 公里，在节能（Eco）模式下最高可达 500 公里，使其成为长途通勤中替代汽车的可行选择。此外，由于电芯承受的压力更小且极端放电循环更少，大容量电池组还延长了使用寿命。作者在最后倡导将电动自行车作为可持续交通工具，并批评制造商使用封闭系统阻碍用户的创新与维修。

---

## 6. 决策树 —— 嵌套决策规则的非凡威力

**原文标题**: Decision trees – the unreasonable power of nested decision rules

**原文链接**: [https://mlu-explain.github.io/decision-tree/](https://mlu-explain.github.io/decision-tree/)

本文通过对树种（苹果树、樱桃树或橡树）根据树干直径和高度这两个特征进行分类的实际类比，解释了**决策树**的基本机制。

构建决策树的过程包含以下关键步骤：

*   **迭代划分：** 模型从**根节点**开始，基于一个特征（如：直径 ≥ 0.45）做出初始决策。这将数据划分为不同的区域。
*   **嵌套规则：** 这一过程通过额外的**决策节点**继续进行，利用水平或垂直边界进一步划分数据。这些嵌套规则为分类构建了路线图。
*   **叶节点：** 这是树的末梢，用于分配特定的分类。当新数据点的属性通过各节点后，最终会落入一个叶节点（即预测类别）。

本文的一个核心观点是警惕**过拟合**的风险。虽然不断划分直到每个数据点都被完美分类非常诱人，但这样做会使决策树变得“过深”。过于复杂的树捕捉的是噪声而非可泛化的模式，这一概念根植于**偏差-方差权衡**。为了构建有效的模型，必须在规则对训练集变得过于特殊之前停止划分。

总之，一个平衡良好的决策树通过遵循一系列嵌套且通用的规则，为分类新数据提供了一种强大、直观且符合逻辑的方法。

---

## 7. 我做了一个演示，展示了当AI聊天“免费”且靠广告支持时会是什么样子。

**原文标题**: I built a demo of what AI chat will look like when it's "free" and ad-supported

**原文链接**: [https://99helpers.com/tools/ad-supported-chat](https://99helpers.com/tools/ad-supported-chat)

本文介绍了一个具有讽刺意味但功能完备的广告支持型 AI 聊天机器人演示，旨在展示各公司在应对高昂计算成本时，可能会如何通过 AI 服务实现变现。尽管其中涉及的品牌（如“BrainBoost Pro”）均为虚构，但该演示切实探讨了维持 AI “免费”使用所必须做出的权衡。

该工具展示了一系列激进的变现模式，包括：
*   **会话前插屏广告：** 在对话开始前出现的带有倒计时的全屏广告。
*   **赞助式回答：** 一种原生广告形式，AI 会自然地将产品推荐融入其回答中。
*   **免费模式限制：** 限制发送五条消息，之后用户必须“观看广告”或升级服务才能继续。
*   **上下文及意图驱动广告：** 根据对话中讨论的具体话题触发的横幅广告和产品卡片。

创作者将其定位为面向产品经理、市场营销人员和开发者的教育资源，旨在帮助他们理解 AI 用户体验（UX）与伦理的未来趋势。通过将广告支持模式与传统订阅模式进行对比，该演示突显了在隐私、回答质量和用户体验方面的重大转变。

最终，这篇文章既是对未来充斥广告的 AI 环境的“预警”，同时也推介了作者的服务 **99helpers** —— 为希望部署自家聊天机器人的企业提供一种纯净、无广告的替代方案。

---

## 8. 为什么 XML 标签对 Claude 如此重要

**原文标题**: Why XML Tags Are So Fundamental to Claude

**原文链接**: [https://glthr.com/XML-fundamental-to-Claude](https://glthr.com/XML-fundamental-to-Claude)

In the article **"Why XML Tags Are So Fundamental to Claude,"** the author explains why XML formatting is the most effective way to prompt Anthropic’s Claude models. While many LLMs use Markdown or plain text, Claude is uniquely optimized for XML due to its specific training and architectural design.

The article highlights several key reasons why XML is superior for Claude:

*   **Structural Clarity and Hierarchy:** XML tags (e.g., `<instructions>`, `<context>`, `<example>`) provide clear boundaries between different parts of a prompt. This prevents "prompt leakage" or confusion, where the model might mistake user-provided data for new instructions.
*   **Purposeful Training:** Claude was fine-tuned on vast amounts of data structured with XML. Consequently, the model is "native" to this syntax, making it highly sensitive to the hierarchy and meaning established by tags.
*   **Handling Complexity:** Unlike Markdown or simple delimiters, XML handles nested structures with ease. This allows users to build complex, multi-layered prompts without the model losing track of the organizational logic.
*   **Machine-Readable Outputs:** By instructing Claude to wrap its responses in specific tags (like `<answer>` or `<json>`), developers can easily parse the model's output programmatically, making Claude more reliable for integration into software applications.
*   **Improved Reasoning:** Using tags like `<thought>` or `<thinking>` encourages "Chain of Thought" reasoning. By separating its internal processing from the final output, Claude typically produces more accurate and logically sound results.

In summary, XML is not merely a stylistic preference for Claude; it is a fundamental tool that leverages the model's training to ensure high precision, better organization, and more reliable performance in complex tasks.

---

## 9. Ape Coding

**原文标题**: Ape Coding

**原文链接**: [https://rsaksida.com/blog/ape-coding/](https://rsaksida.com/blog/ape-coding/)

生成摘要时出错

---

## 10. We do not think Anthropic should be designated as a supply chain risk

**原文标题**: We do not think Anthropic should be designated as a supply chain risk

**原文链接**: [https://twitter.com/OpenAI/status/2027846016423321831](https://twitter.com/OpenAI/status/2027846016423321831)

生成摘要时出错

---

## 11. Interview with Øyvind Kolås, GIMP developer (2017)

**原文标题**: Interview with Øyvind Kolås, GIMP developer (2017)

**原文链接**: [https://www.gimp.org/news/2026/02/22/%C3%B8yvind-kol%C3%A5s-interview-ww2017/](https://www.gimp.org/news/2026/02/22/%C3%B8yvind-kol%C3%A5s-interview-ww2017/)

生成摘要时出错

---

## 12. Flightradar24 for Ships

**原文标题**: Flightradar24 for Ships

**原文链接**: [https://atlas.flexport.com/](https://atlas.flexport.com/)

生成摘要时出错

---

## 13. 10-202: Introduction to Modern AI (CMU)

**原文标题**: 10-202: Introduction to Modern AI (CMU)

**原文链接**: [https://modernaicourse.org](https://modernaicourse.org)

生成摘要时出错

---

## 14. New iron nanomaterial wipes out cancer cells without harming healthy tissue

**原文标题**: New iron nanomaterial wipes out cancer cells without harming healthy tissue

**原文链接**: [https://www.sciencedaily.com/releases/2026/02/260228093456.htm](https://www.sciencedaily.com/releases/2026/02/260228093456.htm)

生成摘要时出错

---

## 15. Lil' Fun Langs' Guts

**原文标题**: Lil' Fun Langs' Guts

**原文链接**: [https://taylor.town/scrapscript-001](https://taylor.town/scrapscript-001)

生成摘要时出错

---

## 16. Aromatic 5-silicon rings synthesized at last

**原文标题**: Aromatic 5-silicon rings synthesized at last

**原文链接**: [https://cen.acs.org/materials/inorganic-chemistry/Aromatic-5-silicon-rings-synthesized/104/web/2026/02](https://cen.acs.org/materials/inorganic-chemistry/Aromatic-5-silicon-rings-synthesized/104/web/2026/02)

生成摘要时出错

---

## 17. The real cost of random I/O

**原文标题**: The real cost of random I/O

**原文链接**: [https://vondra.me/posts/the-real-cost-of-random-io/](https://vondra.me/posts/the-real-cost-of-random-io/)

生成摘要时出错

---

## 18. Why is the first C++ (m)allocation always 72 KB?

**原文标题**: Why is the first C++ (m)allocation always 72 KB?

**原文链接**: [https://joelsiks.com/posts/cpp-emergency-pool-72kb-allocation/](https://joelsiks.com/posts/cpp-emergency-pool-72kb-allocation/)

生成摘要时出错

---

## 19. Switch to Claude without starting over

**原文标题**: Switch to Claude without starting over

**原文链接**: [https://claude.com/import-memory](https://claude.com/import-memory)

生成摘要时出错

---

## 20. An ode to houseplant programming (2025)

**原文标题**: An ode to houseplant programming (2025)

**原文链接**: [https://hannahilea.com/blog/houseplant-programming/](https://hannahilea.com/blog/houseplant-programming/)

生成摘要时出错

---

## 21. Obsidian Sync now has a headless client

**原文标题**: Obsidian Sync now has a headless client

**原文链接**: [https://help.obsidian.md/sync/headless](https://help.obsidian.md/sync/headless)

生成摘要时出错

---

## 22. Robust and efficient quantum-safe HTTPS

**原文标题**: Robust and efficient quantum-safe HTTPS

**原文链接**: [https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html)

生成摘要时出错

---

## 23. Show HN: Vertex.js – A 1kloc SPA Framework

**原文标题**: Show HN: Vertex.js – A 1kloc SPA Framework

**原文链接**: [https://lukeb42.github.io/vertex-manual.html](https://lukeb42.github.io/vertex-manual.html)

生成摘要时出错

---

## 24. The happiest I've ever been

**原文标题**: The happiest I've ever been

**原文链接**: [https://ben-mini.com/2026/the-happiest-ive-ever-been](https://ben-mini.com/2026/the-happiest-ive-ever-been)

生成摘要时出错

---

## 25. Rydberg atoms detect clear signals from a handheld radio

**原文标题**: Rydberg atoms detect clear signals from a handheld radio

**原文链接**: [https://phys.org/news/2026-02-rydberg-atoms-handheld-radio.html](https://phys.org/news/2026-02-rydberg-atoms-handheld-radio.html)

生成摘要时出错

---

## 26. MCP server that reduces Claude Code context consumption by 98%

**原文标题**: MCP server that reduces Claude Code context consumption by 98%

**原文链接**: [https://mksg.lu/blog/context-mode](https://mksg.lu/blog/context-mode)

生成摘要时出错

---

## 27. I Built a Scheme Compiler with AI in 4 Days

**原文标题**: I Built a Scheme Compiler with AI in 4 Days

**原文链接**: [https://matthewphillips.info/programming/posts/i-built-a-scheme-compiler-with-ai/](https://matthewphillips.info/programming/posts/i-built-a-scheme-compiler-with-ai/)

生成摘要时出错

---

## 28. Pigeons and Planes Has a Website Again

**原文标题**: Pigeons and Planes Has a Website Again

**原文链接**: [https://www.pigeonsandplanes.com/read/pigeons-and-planes-has-a-website-again](https://www.pigeonsandplanes.com/read/pigeons-and-planes-has-a-website-again)

生成摘要时出错

---

## 29. Hardwood: A New Parser for Apache Parquet

**原文标题**: Hardwood: A New Parser for Apache Parquet

**原文链接**: [https://www.morling.dev/blog/hardwood-new-parser-for-apache-parquet/](https://www.morling.dev/blog/hardwood-new-parser-for-apache-parquet/)

生成摘要时出错

---

## 30. The Windows 95 user interface: A case study in usability engineering (1996)

**原文标题**: The Windows 95 user interface: A case study in usability engineering (1996)

**原文链接**: [https://dl.acm.org/doi/fullHtml/10.1145/238386.238611](https://dl.acm.org/doi/fullHtml/10.1145/238386.238611)

生成摘要时出错

---

## 31. H-Bomb: A Frank Lloyd Wright typographic mystery

**原文标题**: H-Bomb: A Frank Lloyd Wright typographic mystery

**原文链接**: [https://www.inconspicuous.info/p/h-bomb-a-frank-lloyd-wright-typographic](https://www.inconspicuous.info/p/h-bomb-a-frank-lloyd-wright-typographic)

生成摘要时出错

---

## 32. Woxi: Wolfram Mathematica Reimplementation in Rust

**原文标题**: Woxi: Wolfram Mathematica Reimplementation in Rust

**原文链接**: [https://github.com/ad-si/Woxi](https://github.com/ad-si/Woxi)

生成摘要时出错

---

## 33. Sub-second volumetric 3D printing by synthesis of holographic light fields

**原文标题**: Sub-second volumetric 3D printing by synthesis of holographic light fields

**原文链接**: [https://www.nature.com/articles/s41586-026-10114-5](https://www.nature.com/articles/s41586-026-10114-5)

生成摘要时出错

---

## 34. Show HN: Now I Get It – Translate scientific papers into interactive webpages

**原文标题**: Show HN: Now I Get It – Translate scientific papers into interactive webpages

**原文链接**: [https://nowigetit.us](https://nowigetit.us)

生成摘要时出错

---

## 35. Addressing Antigravity Bans and Reinstating Access

**原文标题**: Addressing Antigravity Bans and Reinstating Access

**原文链接**: [https://github.com/google-gemini/gemini-cli/discussions/20632](https://github.com/google-gemini/gemini-cli/discussions/20632)

生成摘要时出错

---

## 36. Block the “Upgrade to Tahoe” Alerts

**原文标题**: Block the “Upgrade to Tahoe” Alerts

**原文链接**: [https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/](https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/)

生成摘要时出错

---

## 37. Our Agreement with the Department of War

**原文标题**: Our Agreement with the Department of War

**原文链接**: [https://openai.com/index/our-agreement-with-the-department-of-war](https://openai.com/index/our-agreement-with-the-department-of-war)

生成摘要时出错

---

## 38. Verified Spec-Driven Development (VSDD)

**原文标题**: Verified Spec-Driven Development (VSDD)

**原文链接**: [https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00](https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00)

生成摘要时出错

---

## 39. The Eternal Promise: A History of Attempts to Eliminate Programmers

**原文标题**: The Eternal Promise: A History of Attempts to Eliminate Programmers

**原文链接**: [https://www.ivanturkovic.com/2026/01/22/history-software-simplification-cobol-ai-hype/](https://www.ivanturkovic.com/2026/01/22/history-software-simplification-cobol-ai-hype/)

生成摘要时出错

---

## 40. Setting up phones is a nightmare

**原文标题**: Setting up phones is a nightmare

**原文链接**: [https://joelchrono.xyz/blog/setting-up-phones-is-a-nightmare/](https://joelchrono.xyz/blog/setting-up-phones-is-a-nightmare/)

生成摘要时出错

---

## 41. Foods destroying rainforests, in one simple chart

**原文标题**: Foods destroying rainforests, in one simple chart

**原文链接**: [https://www.vox.com/climate/480083/beef-agriculture-deforestation-amazon-rainforest](https://www.vox.com/climate/480083/beef-agriculture-deforestation-amazon-rainforest)

生成摘要时出错

---

## 42. Iran's Ayatollah Ali Khamenei is killed in Israeli strike, ending 36-year rule

**原文标题**: Iran's Ayatollah Ali Khamenei is killed in Israeli strike, ending 36-year rule

**原文链接**: [https://www.npr.org/2026/02/28/1123499337/iran-israel-ayatollah-ali-khamenei-killed](https://www.npr.org/2026/02/28/1123499337/iran-israel-ayatollah-ali-khamenei-killed)

生成摘要时出错

---

## 43. New evidence that Cantor plagiarized Dedekind?

**原文标题**: New evidence that Cantor plagiarized Dedekind?

**原文链接**: [https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/](https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/)

生成摘要时出错

---

## 44. Qwen3.5 122B and 35B models offer Sonnet 4.5 performance on local computers

**原文标题**: Qwen3.5 122B and 35B models offer Sonnet 4.5 performance on local computers

**原文链接**: [https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance](https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance)

生成摘要时出错

---

## 45. The whole thing was a scam

**原文标题**: The whole thing was a scam

**原文链接**: [https://garymarcus.substack.com/p/the-whole-thing-was-scam](https://garymarcus.substack.com/p/the-whole-thing-was-scam)

生成摘要时出错

---

## 46. SpacetimeDB ThreeJS Support

**原文标题**: SpacetimeDB ThreeJS Support

**原文链接**: [https://discourse.threejs.org/t/spacetimedb-threejs-support-and-free-tier/90052](https://discourse.threejs.org/t/spacetimedb-threejs-support-and-free-tier/90052)

生成摘要时出错

---

## 47. The Science of Detecting LLM-Generated Text (2024)

**原文标题**: The Science of Detecting LLM-Generated Text (2024)

**原文链接**: [https://dl.acm.org/doi/10.1145/3624725](https://dl.acm.org/doi/10.1145/3624725)

生成摘要时出错

---

## 48. 747s and coding agents

**原文标题**: 747s and coding agents

**原文链接**: [https://carlkolon.com/2026/02/27/engineering-747-coding-agents/](https://carlkolon.com/2026/02/27/engineering-747-coding-agents/)

生成摘要时出错

---

## 49. Unsloth Dynamic 2.0 GGUFs

**原文标题**: Unsloth Dynamic 2.0 GGUFs

**原文链接**: [https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs)

生成摘要时出错

---

## 50. The archivist preserving decaying floppy disks

**原文标题**: The archivist preserving decaying floppy disks

**原文链接**: [https://www.popsci.com/technology/floppy-disk-archivist-project/](https://www.popsci.com/technology/floppy-disk-archivist-project/)

生成摘要时出错

---

## 51. Werner Herzog Between Fact and Fiction

**原文标题**: Werner Herzog Between Fact and Fiction

**原文链接**: [https://www.thenation.com/article/culture/werner-herzog-future-truth/](https://www.thenation.com/article/culture/werner-herzog-future-truth/)

生成摘要时出错

---

## 52. The United States and Israel have launched a major attack on Iran

**原文标题**: The United States and Israel have launched a major attack on Iran

**原文链接**: [https://www.cnn.com/2026/02/28/middleeast/israel-attack-iran-intl-hnk](https://www.cnn.com/2026/02/28/middleeast/israel-attack-iran-intl-hnk)

生成摘要时出错

---

## 53. Deterministic Programming with LLMs

**原文标题**: Deterministic Programming with LLMs

**原文链接**: [https://www.mcherm.com/deterministic-programming-with-llms.html](https://www.mcherm.com/deterministic-programming-with-llms.html)

生成摘要时出错

---

## 54. AI is making junior devs useless

**原文标题**: AI is making junior devs useless

**原文链接**: [https://beabetterdev.com/2026/03/01/ai-is-making-junior-devs-useless/](https://beabetterdev.com/2026/03/01/ai-is-making-junior-devs-useless/)

生成摘要时出错

---

## 55. OpenAI agrees with Dept. of War to deploy models in their classified network

**原文标题**: OpenAI agrees with Dept. of War to deploy models in their classified network

**原文链接**: [https://twitter.com/sama/status/2027578652477821175](https://twitter.com/sama/status/2027578652477821175)

生成摘要时出错

---

## 56. Building a Minimal Transformer for 10-digit Addition

**原文标题**: Building a Minimal Transformer for 10-digit Addition

**原文链接**: [https://alexlitzenberger.com/blog/post.html?post=/building_a_minimal_transformer_for_10_digit_addition](https://alexlitzenberger.com/blog/post.html?post=/building_a_minimal_transformer_for_10_digit_addition)

生成摘要时出错

---

## 57. Don't use passkeys for encrypting user data

**原文标题**: Don't use passkeys for encrypting user data

**原文链接**: [https://blog.timcappalli.me/p/passkeys-prf-warning/](https://blog.timcappalli.me/p/passkeys-prf-warning/)

生成摘要时出错

---

## 58. The Future of AI

**原文标题**: The Future of AI

**原文链接**: [https://lucijagregov.com/2026/02/26/the-future-of-ai/](https://lucijagregov.com/2026/02/26/the-future-of-ai/)

生成摘要时出错

---

## 59. 4,500 Physicians Agree (About Bacon)

**原文标题**: 4,500 Physicians Agree (About Bacon)

**原文链接**: [https://machielreyneke.com/blog/persuasion/](https://machielreyneke.com/blog/persuasion/)

生成摘要时出错

---

## 60. Smallest transformer that can add two 10-digit numbers

**原文标题**: Smallest transformer that can add two 10-digit numbers

**原文链接**: [https://github.com/anadim/AdderBoard](https://github.com/anadim/AdderBoard)

生成摘要时出错

---

## 61. Dutch Tax Authority hands US software company control over VAT system

**原文标题**: Dutch Tax Authority hands US software company control over VAT system

**原文链接**: [https://www.techzine.eu/news/infrastructure/139152/dutch-tax-authority-hands-us-software-company-control-over-vat-system/](https://www.techzine.eu/news/infrastructure/139152/dutch-tax-authority-hands-us-software-company-control-over-vat-system/)

生成摘要时出错

---

## 62. From Noise to Image – interactive guide to diffusion

**原文标题**: From Noise to Image – interactive guide to diffusion

**原文链接**: [https://lighthousesoftware.co.uk/projects/from-noise-to-image/](https://lighthousesoftware.co.uk/projects/from-noise-to-image/)

生成摘要时出错

---

## 63. Don't go to the shoe shop to buy plates

**原文标题**: Don't go to the shoe shop to buy plates

**原文链接**: [https://naomialderman.substack.com/p/dont-go-to-the-shoe-shop-to-buy-plates](https://naomialderman.substack.com/p/dont-go-to-the-shoe-shop-to-buy-plates)

生成摘要时出错

---

## 64. Samsung Galaxy update removes Android recovery menu tools, including sideloading

**原文标题**: Samsung Galaxy update removes Android recovery menu tools, including sideloading

**原文链接**: [https://9to5google.com/2026/02/27/samsung-galaxy-update-android-recovery-menu-removed/](https://9to5google.com/2026/02/27/samsung-galaxy-update-android-recovery-menu-removed/)

生成摘要时出错

---

## 65. Ghosts'n Goblins – “Worse danger is ahead”

**原文标题**: Ghosts'n Goblins – “Worse danger is ahead”

**原文链接**: [https://superchartisland.com/ghostsn-goblins/](https://superchartisland.com/ghostsn-goblins/)

生成摘要时出错

---

## 66. Kyber (YC W23) Is Hiring an Enterprise Account Executive

**原文标题**: Kyber (YC W23) Is Hiring an Enterprise Account Executive

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/59yPaCs-enterprise-account-executive-ae](https://www.ycombinator.com/companies/kyber/jobs/59yPaCs-enterprise-account-executive-ae)

生成摘要时出错

---

## 67. A new California law says all operating systems need to have age verification

**原文标题**: A new California law says all operating systems need to have age verification

**原文链接**: [https://www.pcgamer.com/software/operating-systems/a-new-california-law-says-all-operating-systems-including-linux-need-to-have-some-form-of-age-verification-at-account-setup/](https://www.pcgamer.com/software/operating-systems/a-new-california-law-says-all-operating-systems-including-linux-need-to-have-some-form-of-age-verification-at-account-setup/)

生成摘要时出错

---

## 68. We Will Not Be Divided

**原文标题**: We Will Not Be Divided

**原文链接**: [https://notdivided.org](https://notdivided.org)

生成摘要时出错

---

## 69. AI Safety Farce

**原文标题**: AI Safety Farce

**原文链接**: [https://seanpedersen.github.io/posts/ai-safety-farce/](https://seanpedersen.github.io/posts/ai-safety-farce/)

生成摘要时出错

---

## 70. Rust is just a tool

**原文标题**: Rust is just a tool

**原文链接**: [https://lewiscampbell.tech/blog/260204.html](https://lewiscampbell.tech/blog/260204.html)

生成摘要时出错

---

## 71. Croatia declared free of landmines after 31 years

**原文标题**: Croatia declared free of landmines after 31 years

**原文链接**: [https://glashrvatske.hrt.hr/en/domestic/croatia-declared-free-of-landmines-after-31-years-12593533](https://glashrvatske.hrt.hr/en/domestic/croatia-declared-free-of-landmines-after-31-years-12593533)

生成摘要时出错

---

## 72. Bootc and OSTree: Modernizing Linux System Deployment

**原文标题**: Bootc and OSTree: Modernizing Linux System Deployment

**原文链接**: [https://a-cup-of.coffee/blog/ostree-bootc/](https://a-cup-of.coffee/blog/ostree-bootc/)

生成摘要时出错

---

## 73. The mission to stop the next global backdoor before it starts

**原文标题**: The mission to stop the next global backdoor before it starts

**原文链接**: [https://thenewstack.io/commonhaus-open-source-governance/](https://thenewstack.io/commonhaus-open-source-governance/)

生成摘要时出错

---

## 74. Show HN: Terminal-Style Portfolio on the Internet

**原文标题**: Show HN: Terminal-Style Portfolio on the Internet

**原文链接**: [https://kuber.studio/](https://kuber.studio/)

生成摘要时出错

---

## 75. Qt45: A small polymerase ribozyme that can synthesize itself

**原文标题**: Qt45: A small polymerase ribozyme that can synthesize itself

**原文链接**: [https://www.science.org/doi/10.1126/science.adt2760](https://www.science.org/doi/10.1126/science.adt2760)

生成摘要时出错

---

## 76. We gave terabytes of CI logs to an LLM

**原文标题**: We gave terabytes of CI logs to an LLM

**原文链接**: [https://www.mendral.com/blog/llms-are-good-at-sql](https://www.mendral.com/blog/llms-are-good-at-sql)

生成摘要时出错

---

## 77. OpenAI fires an employee for prediction market insider trading

**原文标题**: OpenAI fires an employee for prediction market insider trading

**原文链接**: [https://www.wired.com/story/openai-fires-employee-insider-trading-polymarket-kalshi/](https://www.wired.com/story/openai-fires-employee-insider-trading-polymarket-kalshi/)

生成摘要时出错

---

## 78. Cash issuing terminals

**原文标题**: Cash issuing terminals

**原文链接**: [https://computer.rip/2026-02-27-ibm-atm.html](https://computer.rip/2026-02-27-ibm-atm.html)

生成摘要时出错

---

## 79. Statement on the comments from Secretary of War Pete Hegseth

**原文标题**: Statement on the comments from Secretary of War Pete Hegseth

**原文链接**: [https://www.anthropic.com/news/statement-comments-secretary-war](https://www.anthropic.com/news/statement-comments-secretary-war)

生成摘要时出错

---

## 80. A Chinese official’s use of ChatGPT revealed an intimidation operation

**原文标题**: A Chinese official’s use of ChatGPT revealed an intimidation operation

**原文链接**: [https://www.cnn.com/2026/02/25/politics/chatgpt-china-intimidation-operation](https://www.cnn.com/2026/02/25/politics/chatgpt-china-intimidation-operation)

生成摘要时出错

---

## 81. Libre Solar – Open Hardware for Renewable Energy

**原文标题**: Libre Solar – Open Hardware for Renewable Energy

**原文链接**: [https://libre.solar](https://libre.solar)

生成摘要时出错

---

## 82. Why consumer choice is stripped away and how the tech industry profits from it

**原文标题**: Why consumer choice is stripped away and how the tech industry profits from it

**原文链接**: [https://fireborn.mataroa.blog/blog/because-fuck-you-why-consumer-choice-is-being-stripped-away-and-how-the-tech-industry-profits-from-it/](https://fireborn.mataroa.blog/blog/because-fuck-you-why-consumer-choice-is-being-stripped-away-and-how-the-tech-industry-profits-from-it/)

生成摘要时出错

---

## 83. Intelligence is a commodity. Context is the real AI Moat

**原文标题**: Intelligence is a commodity. Context is the real AI Moat

**原文链接**: [https://adlrocha.substack.com/p/adlrocha-intelligence-is-a-commodity](https://adlrocha.substack.com/p/adlrocha-intelligence-is-a-commodity)

生成摘要时出错

---

## 84. OpenAI raises $110B on $730B pre-money valuation

**原文标题**: OpenAI raises $110B on $730B pre-money valuation

**原文链接**: [https://techcrunch.com/2026/02/27/openai-raises-110b-in-one-of-the-largest-private-funding-rounds-in-history/](https://techcrunch.com/2026/02/27/openai-raises-110b-in-one-of-the-largest-private-funding-rounds-in-history/)

生成摘要时出错

---

## 85. Monitor the Situation

**原文标题**: Monitor the Situation

**原文链接**: [https://monitor-the-situation.com/middle-east](https://monitor-the-situation.com/middle-east)

生成摘要时出错

---

## 86. 'Can't sell house' searches are higher now than during the 2008 housing crisis

**原文标题**: 'Can't sell house' searches are higher now than during the 2008 housing crisis

**原文链接**: [https://www.morningstar.com/news/marketwatch/20260228147/cant-sell-house-searches-are-higher-now-than-during-the-2008-housing-crisis](https://www.morningstar.com/news/marketwatch/20260228147/cant-sell-house-searches-are-higher-now-than-during-the-2008-housing-crisis)

生成摘要时出错

---

## 87. Running a One Trillion-Parameter LLM Locally on AMD Ryzen AI Max+ Cluster

**原文标题**: Running a One Trillion-Parameter LLM Locally on AMD Ryzen AI Max+ Cluster

**原文链接**: [https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html](https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html)

生成摘要时出错

---

## 88. 'Play like a dog biting God's feet': Steven Isserlis on György Kurtág at 100

**原文标题**: 'Play like a dog biting God's feet': Steven Isserlis on György Kurtág at 100

**原文链接**: [https://www.theguardian.com/music/2026/feb/26/steven-isserlis-on-the-formidable-gyorgy-kurtag-at-100](https://www.theguardian.com/music/2026/feb/26/steven-isserlis-on-the-formidable-gyorgy-kurtag-at-100)

生成摘要时出错

---

## 89. Smartphone market forecast to decline this year due to memory shortage

**原文标题**: Smartphone market forecast to decline this year due to memory shortage

**原文链接**: [https://www.idc.com/resource-center/press-releases/wwsmartphoneforecast4q25/](https://www.idc.com/resource-center/press-releases/wwsmartphoneforecast4q25/)

生成摘要时出错

---

## 90. Just two days of oatmeal cut bad cholesterol by 10%

**原文标题**: Just two days of oatmeal cut bad cholesterol by 10%

**原文链接**: [https://www.sciencedaily.com/releases/2026/02/260225081217.htm](https://www.sciencedaily.com/releases/2026/02/260225081217.htm)

生成摘要时出错

---

## 91. Don't trust AI agents

**原文标题**: Don't trust AI agents

**原文链接**: [https://nanoclaw.dev/blog/nanoclaw-security-model](https://nanoclaw.dev/blog/nanoclaw-security-model)

The article argues that AI agents should be treated as inherently untrusted and potentially malicious. Relying on application-level security, such as allowlists or confirmation prompts, is insufficient because a compromised or determined agent can bypass these checks. Instead, security must be enforced through architecture that assumes the agent will misbehave.

The author introduces **NanoClaw**, a project designed around three core principles of distrust:

*   **Process Isolation:** Unlike frameworks that run on the host machine, NanoClaw runs every agent in an ephemeral, OS-enforced container. Agents operate as unprivileged users with read-only access to specific directories, ensuring they cannot escape to the host or persist after a task is completed.
*   **Inter-Agent Security:** To prevent data leakage, every agent (e.g., a personal assistant vs. a work assistant) is isolated in its own container with its own filesystem and session history. This prevents one agent from accessing the credentials or data of another.
*   **Auditable Simplicity:** The author critiques "monolithic" AI frameworks like OpenClaw, which contain hundreds of thousands of lines of unaudited code. NanoClaw remains intentionally small and auditable, relying on a "skills" model. Users only add specific, reviewed integrations as needed, keeping the attack surface minimal and the codebase transparent.

Ultimately, the article concludes that while AI agents are high-risk, that risk can be managed by building "walls" around them. Security should reside outside the agent’s control so that hallucinations or prompt injections are contained within a narrow, verifiable "blast radius."

---

## 92. Let's discuss sandbox isolation

**原文标题**: Let's discuss sandbox isolation

**原文链接**: [https://www.shayon.dev/post/2026/52/lets-discuss-sandbox-isolation/](https://www.shayon.dev/post/2026/52/lets-discuss-sandbox-isolation/)

生成摘要时出错

---

## 93. Court finds Fourth Amendment doesn’t support broad search of protesters’ devices

**原文标题**: Court finds Fourth Amendment doesn’t support broad search of protesters’ devices

**原文链接**: [https://www.eff.org/deeplinks/2026/02/victory-tenth-circuit-finds-fourth-amendment-doesnt-support-broad-search-0](https://www.eff.org/deeplinks/2026/02/victory-tenth-circuit-finds-fourth-amendment-doesnt-support-broad-search-0)

生成摘要时出错

---

## 94. Writing a Guide to SDF Fonts

**原文标题**: Writing a Guide to SDF Fonts

**原文链接**: [https://www.redblobgames.com/blog/2026-02-26-writing-a-guide-to-sdf-fonts/](https://www.redblobgames.com/blog/2026-02-26-writing-a-guide-to-sdf-fonts/)

生成摘要时出错

---

## 95. Allocating on the Stack

**原文标题**: Allocating on the Stack

**原文链接**: [https://go.dev/blog/allocation-optimizations](https://go.dev/blog/allocation-optimizations)

生成摘要时出错

---

## 96. Show HN: Unfucked - version all changes (by any tool) - local-first/source avail

**原文标题**: Show HN: Unfucked - version all changes (by any tool) - local-first/source avail

**原文链接**: [https://www.unfudged.io/](https://www.unfudged.io/)

生成摘要时出错

---

## 97. 390TB video game archive being taken offline due to skyrocketing RAM, SSD

**原文标题**: 390TB video game archive being taken offline due to skyrocketing RAM, SSD

**原文链接**: [https://www.tomshardware.com/video-games/390tb-video-game-archive-being-taken-offline-due-to-skyrocketing-ram-ssd-and-hard-drive-prices-ai-driven-supply-squeeze-results-in-closure-of-one-of-the-largest-online-video-game-archives](https://www.tomshardware.com/video-games/390tb-video-game-archive-being-taken-offline-due-to-skyrocketing-ram-ssd-and-hard-drive-prices-ai-driven-supply-squeeze-results-in-closure-of-one-of-the-largest-online-video-game-archives)

生成摘要时出错

---

## 98. Show HN: SplatHash – A lightweight alternative to BlurHash and ThumbHash

**原文标题**: Show HN: SplatHash – A lightweight alternative to BlurHash and ThumbHash

**原文链接**: [https://github.com/junevm/splathash](https://github.com/junevm/splathash)

生成摘要时出错

---

## 99. Show HN: RetroTick – Run classic Windows EXEs in the browser

**原文标题**: Show HN: RetroTick – Run classic Windows EXEs in the browser

**原文链接**: [https://retrotick.com/](https://retrotick.com/)

生成摘要时出错

---

## 100. The normalization of corruption in organizations (2003) [pdf]

**原文标题**: The normalization of corruption in organizations (2003) [pdf]

**原文链接**: [https://gwern.net/doc/sociology/2003-ashforth.pdf](https://gwern.net/doc/sociology/2003-ashforth.pdf)

生成摘要时出错

---

