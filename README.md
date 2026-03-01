# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-01.md)

*最后自动更新时间: 2026-03-01 17:52:09*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 2 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 3 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 4 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 5 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 6 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 7 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 8 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 9 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 10 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 11 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 12 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 13 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 14 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 15 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 16 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 17 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 18 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 19 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 20 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 21 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 22 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 23 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 24 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 25 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 26 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 27 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 28 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 29 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 30 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 31 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 32 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 33 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 34 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 35 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 36 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 37 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 38 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 39 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 40 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 41 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 42 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 43 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 44 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 45 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 46 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 47 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 48 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 49 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 50 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 51 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 52 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 53 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 54 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 55 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 56 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 57 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 58 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 59 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 60 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 61 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 62 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 63 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 64 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 65 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 66 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 67 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 68 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 69 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 70 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 71 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 72 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 73 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 74 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 75 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 76 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 77 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 78 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 79 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 80 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 81 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 82 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 83 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 84 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 85 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 86 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 87 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 88 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 89 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 90 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 91 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 92 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 93 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 94 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 95 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 96 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 97 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 98 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 99 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 100 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 101 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 102 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 103 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 104 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 105 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 106 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 107 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 108 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 109 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 110 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 111 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 112 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 113 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 114 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 115 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 116 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 117 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 118 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 119 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 120 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 121 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 122 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 123 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 124 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 125 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 126 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 127 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 128 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 129 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 130 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 131 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 132 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 133 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 134 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 135 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 136 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 137 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 138 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 139 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 140 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 141 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 142 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 143 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 144 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 145 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 146 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 147 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 148 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 149 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 150 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 151 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 152 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 153 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 154 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 155 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 156 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 157 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 158 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 159 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 160 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 161 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 162 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 163 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 164 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 165 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 166 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 167 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 168 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 169 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 170 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 171 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 172 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 173 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 174 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 175 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 176 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 177 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 178 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 179 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 180 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 181 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 182 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 183 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 184 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 185 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 186 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 187 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 188 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 189 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 190 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 191 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 192 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 193 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 194 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 195 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 196 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 197 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 198 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 199 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 200 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 201 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 202 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 203 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 204 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 205 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 206 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 207 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 208 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 209 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 210 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 211 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 212 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 213 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 214 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 215 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 216 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 217 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 218 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 219 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 220 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 221 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 222 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 223 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 224 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 225 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 226 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 227 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 228 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 229 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 230 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 231 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 232 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 233 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 234 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 235 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 236 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 237 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 238 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 239 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 240 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 241 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 242 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 243 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 244 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 245 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 246 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 247 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 248 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 249 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 250 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 251 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 252 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 253 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 254 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 255 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 256 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 257 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 258 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 259 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 260 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 261 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 262 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 263 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 264 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 265 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 266 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 267 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 268 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 269 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 270 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 271 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 272 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 273 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 274 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 275 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 276 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 277 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 278 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 279 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 280 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 281 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 282 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 283 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 284 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 285 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 286 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 287 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 288 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 289 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 290 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 291 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 292 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 293 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 294 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 295 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 296 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 297 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 298 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 299 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 300 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 301 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 302 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 303 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 304 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 305 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 306 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 307 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 308 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 309 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 310 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 311 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 312 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 313 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 314 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 315 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 316 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 317 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 318 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 319 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 320 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 321 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 322 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 323 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 324 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 325 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 326 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 327 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 328 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 329 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 330 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 331 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 332 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 333 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 334 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 335 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 336 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 337 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 338 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 339 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 340 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 341 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 342 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 343 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 344 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 345 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 346 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
