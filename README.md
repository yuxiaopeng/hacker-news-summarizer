# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-16.md)

*最后自动更新时间: 2026-07-16 18:36:39*
## 1. Kimi K3 现已上线

**原文标题**: Kimi K3 is now live

**原文链接**: [https://www.kimi.com/en](https://www.kimi.com/en)

月之暗面（Moonshot AI）正式推出了其 AI 模型的最新版本 **Kimi K3**。该版本专门针对**智能体编程（agentic coding）**和**知识工作**进行了优化，标志着 AI 正向更加自主和任务导向的方向转型。

此次更新的核心亮点包括：

*   **智能体框架：** 与标准聊天机器人不同，Kimi K3 旨在以“智能体”身份运行。用户可以为模型分配特定任务，由其执行多步骤工作流以达成目标。
*   **专业化聚焦：** 该模型专为专业环境量身定制，特别是辅助复杂编程（代码编写）和深度信息处理（知识工作）。
*   **通用多样性：** 虽然针对技术任务进行了优化，但它仍保留了强大的“有问必答”能力，可用于日常咨询和获取灵感。

Kimi K3 现已正式上线，旨在为开发者和知识型专业人士提供更具功能性且更主动的助手。

---

## 2. 微软漫画聊天现已开源

**原文标题**: Microsoft Comic Chat is now open source

**原文链接**: [https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/)

微软正式发布了 Microsoft Comic Chat（后更名为 Microsoft Chat 2.5）的源代码，这是 20 世纪 90 年代标志性的互联网中继聊天 (IRC) 客户端。该项目由 Robert Standefer 和 Scott Hanselman 宣布，目前已在 GitHub 上以 MIT 许可证开源。

Comic Chat 最初于 1996 年推出，是一款独特的通信工具，能自动将文本对话转换为动态的多格漫画。用户可以选择能够表达各种情感和手势的虚拟角色，从而为聊天内容创建视觉叙事。虽然它是早期互联网时代的代表作，但随着微软向其他通信平台转型，该软件最终成为了“弃置软件”(abandonware)。

开源源代码的决定主要旨在进行数字保存。通过公开源代码，微软允许爱好者和开发人员将该软件移植到现代操作系统，修复遗留漏洞，并确保该工具出于历史和怀旧目的保持可用。此举延续了微软发布 MS-DOS 和原始 Windows 文件管理器等遗留项目源代码的趋势，旨在支持开发者社区并归档互联网历史。

---

## 3. 诱饵字体

**原文标题**: Decoy Font

**原文链接**: [https://www.mixfont.com/experiments/decoy-font](https://www.mixfont.com/experiments/decoy-font)

**Decoy Font** 是一种专门设计的 TrueType 字体 (TTF)，旨在向 AI 模型和 OCR（光学字符识别）系统隐藏书面信息。该字体由 Mixfont 的 Eric Lu 开发，利用“空间频率”原理在同一空间内显示两个不同的字母。

这项技术基于“混合图像”技术——这是一种类似于著名的爱因斯坦与玛丽莲·梦露合体肖像的错视效果。Decoy Font 的前景由细长、锐利的轮廓组成，ChatGPT 和 Gemini 等 AI 模型在分析像素时会优先识别这些轮廓。相反，背景包含模糊的低频色块，只有在远处观看或眯起眼睛时，才会显现出真实的隐藏信息。

**主要亮点包括：**
*   **功能：** 诱导 AI 读取“诱饵”文本，同时允许人类看到预期的真实信息。
*   **易用性：** 与基于动态效果的反 AI 字体不同，Decoy Font 是标准的 TTF 文件，可安装并用于个人、商业和客户项目。它基于 DejaVu Sans Mono 许可开发。
*   **目的：** 作为防御 AI 抓取工具的手段，用于保护知识产权和私密通信。
*   **局限性：** 虽然对目前的前沿大语言模型有效，但开发者指出这并非 100% 的保证，因为先进的 AI 代理最终可能会通过提示词学会识别这种错觉。

展望未来，该项目旨在扩展到中文等基于字符的语言，并可能作为测试 AI 文本识别演进的基准。它代表了“反 AI”字体设计的新前沿，致力于确保传达给人类的信息仅对人类可见。

---

## 4. 使用“经典”机器学习检测大语言模型生成的文本

**原文标题**: Detecting LLM-Generated Texts with “Classical” Machine Learning

**原文链接**: [https://blog.lyc8503.net/en/post/llm-classifier/](https://blog.lyc8503.net/en/post/llm-classifier/)

本文详述了一款 AI 文本检测器的开发过程，旨在识别 Lofter 等平台上日益增多的 AI 生成内容。作者摒弃了不可靠且成本高昂的“文本困惑度”方法，转而采用“经典”机器学习技术——具体使用了 Scikit-learn 的 TF-IDF 和 Linear SVC 算法。

**技术方案与训练**
作者构建了一个包含 1 万篇人类撰写文本（2022 年以前）和相应规模 AI 生成样本的数据集，后者由 Gemini、通义千问（Qwen）和 DeepSeek 等七种不同模型生成。作者并未采用单一模型，而是训练了七个二分类器并使用多数投票机制：若至少有两个模型检测出某句为 AI 生成，则将其标记。该方法实现了约 85% 的句级准确率。

**实现与性能**
为确保易用性，该项目采用 JavaScript 实现，支持基于浏览器的无服务器推理。关键性能亮点包括：
*   **泛化能力强：** 该工具能以 70%–90% 的准确率成功检测来自未知模型（如 GPT-5 和 Claude）的内容。
*   **低误报率：** 人类创作的网络小说 AI 概率始终低于 30%，而疑似 AI 生成的内容得分通常高于 80%。
*   **鲁棒性：** 常见的规避手段（如中英往返翻译或特定的“反 AI”提示词）均未能有效欺骗该检测器。

**核心发现**
作者对 Lofter 上的热门内容进行了大规模分析，揭示了一个令人吃惊的趋势：32.22% 的高热度文章在 AI 检测量表上的得分超过 50%，这表明大量未经标注的 AI 小说正涌入平台。该项目总结认为，尽管现代大语言模型非常先进，但它们仍表现出可预测的统计模式，传统机器学习技术依然可以对其进行可靠识别。

---

## 5. 一加停止美欧业务

**原文标题**: OnePlus halts operations in USA and Europe

**原文链接**: [https://community.oneplus.com/thread/2170715118587871237](https://community.oneplus.com/thread/2170715118587871237)

Based on the title provided and the current status of the company (as the full text of the article was not included), here is a concise summary of the facts surrounding these claims:

Contrary to the headline, **OnePlus has not halted operations in the USA or Europe.** This claim typically stems from a misunderstanding of specific legal disputes rather than a total market withdrawal.

**Key Points:**

*   **Official Denials:** In 2023, widespread rumors suggested OnePlus and its parent company, Oppo, were exiting major European markets (including the UK, France, and Germany). OnePlus officially refuted these claims, stating they remain committed to the European region and are simply optimizing their resources.
*   **The German Sales Ban:** The "halt" most accurately refers to a temporary legal situation in **Germany**. Due to a patent dispute with Nokia and InterDigital, OnePlus was legally required to pause smartphone sales in that specific country. However, they have since reached settlements and have begun resuming sales in the German market.
*   **U.S. Market Commitment:** OnePlus remains fully operational in the United States. They continue to release flagship products, such as the OnePlus 12 and OnePlus Open, and maintain strong retail and carrier partnerships (notably with T-Mobile).
*   **Oppo Integration:** While OnePlus has merged its research and development departments more closely with **Oppo** to streamline operations, the brand continues to function as an independent entity in Western markets.

**Summary:** While OnePlus has faced localized legal challenges in Europe—specifically a temporary sales ban in Germany—the company continues to operate and launch new products across both the USA and Europe. There is no evidence of a full exit from these regions.

---

## 6. NotebookLM is now Gemini Notebook

**原文标题**: NotebookLM is now Gemini Notebook

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)

生成摘要时出错

---

## 7. Goes-19 weather satellite enters Safe Hold mode

**原文标题**: Goes-19 weather satellite enters Safe Hold mode

**原文链接**: [https://www.spaceweather.gov/news/goes-19-safe-hold](https://www.spaceweather.gov/news/goes-19-safe-hold)

生成摘要时出错

---

## 8. Adaptional (YC S25) Is Hiring

**原文标题**: Adaptional (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/adaptional/jobs](https://www.ycombinator.com/companies/adaptional/jobs)

生成摘要时出错

---

## 9. 56,000 lines of DOOM, in a language I made up

**原文标题**: 56,000 lines of DOOM, in a language I made up

**原文链接**: [https://betlang.dev/about/](https://betlang.dev/about/)

生成摘要时出错

---

## 10. The lost joy of music piracy

**原文标题**: The lost joy of music piracy

**原文链接**: [https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming](https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 2 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 3 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 4 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 5 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 6 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 7 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 8 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 9 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 10 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 11 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 12 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 13 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 14 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 15 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 16 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 17 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 18 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 19 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 20 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 21 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 22 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 23 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 24 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 25 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 26 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 27 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 28 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 29 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 30 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 31 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 32 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 33 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 34 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 35 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 36 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 37 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 38 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 39 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 40 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 41 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 42 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 43 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 44 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 45 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 46 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 47 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 48 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 49 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 50 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 51 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 52 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 53 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 54 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 55 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 56 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 57 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 58 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 59 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 60 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 61 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 62 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 63 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 64 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 65 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 66 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 67 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 68 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 69 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 70 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 71 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 72 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 73 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 74 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 75 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 76 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 77 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 78 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 79 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 80 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 81 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 82 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 83 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 84 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 85 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 86 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 87 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 88 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 89 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 90 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 91 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 92 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 93 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 94 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 95 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 96 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 97 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 98 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 99 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 100 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 101 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 102 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 103 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 104 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 105 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 106 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 107 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 108 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 109 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 110 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 111 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 112 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 113 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 114 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 115 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 116 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 117 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 118 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 119 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 120 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 121 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 122 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 123 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 124 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 125 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 126 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 127 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 128 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 129 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 130 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 131 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 132 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 133 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 134 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 135 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 136 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 137 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 138 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 139 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 140 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 141 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 142 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 143 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 144 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 145 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 146 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 147 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 148 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 149 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 150 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 151 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 152 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 153 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 154 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 155 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 156 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 157 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 158 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 159 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 160 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 161 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 162 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 163 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 164 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 165 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 166 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 167 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 168 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 169 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 170 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 171 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 172 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 173 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 174 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 175 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 176 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 177 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 178 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 179 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 180 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 181 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 182 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 183 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 184 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 185 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 186 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 187 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 188 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 189 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 190 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 191 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 192 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 193 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 194 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 195 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 196 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 197 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 198 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 199 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 200 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 201 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 202 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 203 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 204 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 205 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 206 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 207 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 208 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 209 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 210 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 211 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 212 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 213 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 214 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 215 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 216 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 217 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 218 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 219 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 220 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 221 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 222 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 223 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 224 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 225 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 226 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 227 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 228 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 229 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 230 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 231 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 232 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 233 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 234 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 235 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 236 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 237 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 238 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 239 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 240 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 241 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 242 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 243 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 244 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 245 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 246 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 247 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 248 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 249 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 250 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 251 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 252 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 253 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 254 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 255 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 256 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 257 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 258 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 259 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 260 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 261 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 262 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 263 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 264 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 265 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 266 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 267 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 268 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 269 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 270 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 271 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 272 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 273 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 274 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 275 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 276 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 277 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 278 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 279 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 280 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 281 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 282 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 283 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 284 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 285 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 286 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 287 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 288 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 289 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 290 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 291 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 292 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 293 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 294 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 295 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 296 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 297 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 298 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 299 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 300 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 301 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 302 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 303 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 304 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 305 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 306 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 307 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 308 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 309 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 310 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 311 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 312 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 313 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 314 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 315 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 316 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 317 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 318 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 319 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 320 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 321 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 322 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 323 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 324 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 325 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 326 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 327 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 328 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 329 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 330 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 331 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 332 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 333 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 334 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 335 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 336 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 337 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 338 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 339 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 340 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 341 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 342 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 343 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 344 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 345 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 346 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 347 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 348 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 349 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 350 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 351 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 352 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 353 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 354 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 355 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 356 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 357 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 358 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 359 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 360 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 361 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 362 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 363 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 364 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 365 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 366 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 367 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 368 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 369 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 370 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 371 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 372 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 373 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 374 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 375 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 376 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 377 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 378 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 379 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 380 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 381 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 382 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 383 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 384 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 385 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 386 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 387 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 388 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 389 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 390 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 391 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 392 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 393 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 394 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 395 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 396 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 397 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 398 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 399 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 400 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 401 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 402 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 403 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 404 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 405 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 406 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 407 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 408 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 409 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 410 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 411 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 412 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 413 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 414 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 415 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 416 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 417 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 418 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 419 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 420 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 421 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 422 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 423 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 424 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 425 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 426 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 427 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 428 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 429 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 430 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 431 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 432 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 433 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 434 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 435 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 436 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 437 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 438 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 439 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 440 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 441 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 442 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 443 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 444 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 445 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 446 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 447 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 448 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 449 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 450 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 451 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 452 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 453 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 454 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 455 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 456 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 457 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 458 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 459 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 460 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 461 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 462 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 463 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 464 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 465 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 466 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 467 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 468 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 469 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 470 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 471 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 472 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 473 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 474 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 475 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 476 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 477 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 478 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 479 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 480 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 481 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 482 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 483 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
