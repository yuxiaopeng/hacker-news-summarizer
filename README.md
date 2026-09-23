# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-23.md)

*最后自动更新时间: 2026-09-23 20:31:43*
## 1. Claude 发现了一种具有类 CRISPR 重复序列的新型酶系统。

**原文标题**: Claude discovers a novel enzyme system with CRISPR-like repeats

**原文链接**: [https://www.anthropic.com/news/claude-discovers-novel-enzyme-system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)

Anthropic has announced the formation of a new life sciences research group and laboratory dedicated to accelerating biological discovery through AI-human collaboration. In its first major breakthrough, the team’s AI model, Claude, autonomously discovered a novel enzyme system called **array-associated reverse transcriptases (ART)**.

Found primarily in jumbo phages (viruses that infect bacteria), the ART system consists of a reverse transcriptase, a partner protein of unknown function, and a long array of DNA repeats. While the enzyme itself had been previously identified, Claude was the first to recognize the associated repeat array, which is structurally reminiscent of the programmable CRISPR-Cas system. Initial laboratory tests confirm that these arrays are expressed as distinct short RNAs, suggesting the system may perform programmable operations like cutting or copying DNA.

The discovery highlights the efficiency of AI-driven research. In a 21-hour campaign, approximately 950 Claude agents scanned a database of 200,000 reverse transcriptases, narrowing them down to 20 compelling candidates and producing human-readable reports. Claude autonomously analyzed raw DNA sequences, measured repeat spacing, and compared findings against existing literature—a process that typically takes human scientists weeks or months.

CRISPR pioneer Feng Zhang praised the discovery as a "genuinely intriguing" example of how AI can support biological research. Anthropic’s scientists validated Claude’s findings in their Bay Area laboratory (operating at BSL-1 and BSL-2 levels), where humans perform all physical experiments.

This milestone demonstrates a new paradigm in "AI-driven hypothesis generation." By training Claude to mimic "scientific taste" and handle massive datasets, Anthropic aims to systematize the discovery of molecular machines that could eventually revolutionize biotechnology and medicine.

---

## 2. Fixing the Portobello Police Station Clock

**原文标题**: Fixing the Portobello Police Station Clock

**原文链接**: [https://pointinthecloud.com/2026-04-11-211700.html](https://pointinthecloud.com/2026-04-11-211700.html)

生成摘要时出错

---

## 3. 我们如何在两周内将 claude.ai 的速度提升 3 倍

**原文标题**: How we made claude.ai 3x faster in two weeks

**原文链接**: [https://claude.dev/blog/how-we-made-claude-ai-faster/](https://claude.dev/blog/how-we-made-claude-ai-faster/)

在这篇文章中，Anthropic 的工程师们详细介绍了一场为期两周的冲刺，将 claude.ai 及其桌面应用的性能平均提升了 3 倍。通过聚焦四大核心用户场景——启动应用、发起对话、加载对话和发送消息——团队将 p75 网页加载时间从 3.1 秒缩短至 0.55 秒，并在特定的内部任务中实现了高达 19 倍的加速。

该项目的核心理念是“一旦 Claude 能够测量某项指标，它就能使其变得更快”。团队利用集成在 Slack 工作流中的内部研究模型（性能可比肩 Opus 5.5）来识别瓶颈并制定确定性的基准测试。他们优先考虑可以在持续集成（CI）中稳步压低的指标——例如 JavaScript 指令数、React 提交数和布局偏移计数——而不是仅仅依赖于波动的“实际耗时”。这使得 Claude 能够在发布更改之前，先在实验室环境中针对特定数值自主进行“爬山式”优化。

关键技术改进包括：
*   **更快的启动速度：** 将静态编辑器嵌入 HTML 以实现即时输入，并在桌面应用中利用 V8 代码缓存。
*   **UI 优化：** 将侧边栏的重新渲染减少了 90%，并通过监测布局不稳定性 API（Layout Instability API）消除了视觉卡顿。
*   **代码路径效率：** 解决了 V8 引擎的一个瓶颈，即非拉丁字符（如破折号）会迫使语法高亮进入较慢的 UTF-16 正则表达式路径。

团队遵循着严谨的闭环流程：由 Claude 追踪问题、构建基准、提交 PR 并监测线上数据。这种方法使得团队在合并超过 3,000 项更改的同时，实现了零客户事故。最终，这次冲刺证明了 AI 可以通过将测量转化为主动、自动化的优化引擎，从而彻底改变性能工程。

---

## 4. Windows 滚动条快捷键简史

**原文标题**: A brief history of Windows scroll bar shortcuts

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260922-00/?p=112719/](https://devblogs.microsoft.com/oldnewthing/20260922-00/?p=112719/)

从历史上看，Windows (Win32) 滚动条通过五个基本操作目标运行：用于逐行滚动的箭头、用于翻页的轨道，以及用于拖动的滑块。Windows 7 通过引入右键上下文菜单和“隐藏的”Shift+点击快捷方式，显著增强了这一功能。

右键菜单增加了多个导航选项，其中最著名的是“滚动到此处”，它允许用户在不拖动滑块的情况下立即跳转到特定位置。同样，Shift+点击快捷方式能让滑块直接跳转到光标所在位置。这两项功能的设计初衷都是为了提高长距离导航的效率。

然而，作者指出，随着软件开发从原生 Win32 控件转向各种 UI 框架，由于生态碎片化，这些快捷方式的表现已变得不再一致：

*   **Chromium/Electron：** 支持 Shift+点击，但缺少右键菜单。
*   **WPF：** 实现了这两项功能。
*   **WinUI：** 令人沮丧的是，这两者均未实现。
*   **Qt：** 支持是可选的，取决于具体开发者的设置。

总之，虽然这些快捷方式仍然是强大的导航工具，但现代框架缺乏标准化，这意味着用户无法再指望它们在不同应用程序中都能保持一致。

---

## 5. 云端智能体是不可避免的AI监狱。

**原文标题**: Cloud Agents Are Inevitable AI Prisons

**原文链接**: [https://normanponte.io/19df691f](https://normanponte.io/19df691f)

基于所提供的文本，由于正文内容由字母数字代码而非标准叙述组成，因此难以进行全面总结。不过，该文章可归纳如下：

**总结：云端代理是不可避免的 AI 监狱**

这篇由 Norman Ponte 撰写、题为**《云端代理是不可避免的 AI 监狱》(Cloud Agents Are Inevitable AI Prisons)** 的文章，对人工智能的未来提出了一个发人深省的论点。虽然所提供的文本大部分由晦涩的字母数字字符串（如“z3 m4k 2k94 mk2”）组成，但可以推断出以下几个关键点：

*   **“监狱”隐喻：** 标题暗示，随着 AI 代理越来越多地托管在云端，它们被局限在专有基础设施之内。这意味着 AI 失去了自主性，权力向中心集中，企业云供应商成为了这项技术及其所处理数据的“狱卒”。
*   **集中化控制：** 文中在作者姓名旁提到了“控制 AI”，这表明向云端的迁移是维持人类或企业监管的一种刻意手段。这种基础设施确保了 AI 无法在特定的、受监控的环境之外存在或运行。
*   **隐秘的传达方式：** 文中使用了“黑客语”（leetspeak）或编码语言（如“4ik 2k1 k42”），并要求“听取 nponte 的意见”，这使作者在 AI 控制的论述中呈现出一种专业且独特的姿态，尽管具体的片段技术论据在本文中仍显模糊。

本质上，这篇文章似乎是对云主导景观下 AI 代理缺乏自由的一种批判或警告，认为“云”不仅是一个托管平台，更是一种永久禁锢的机制。

---

## 6. Italian parliament votes for return to nuclear energy

**原文标题**: Italian parliament votes for return to nuclear energy

**原文链接**: [https://apnews.com/article/italy-nuclear-chernobyl-4891b6b7c7791ae84db6b0bf0f7cf567](https://apnews.com/article/italy-nuclear-chernobyl-4891b6b7c7791ae84db6b0bf0f7cf567)

生成摘要时出错

---

## 7. Gemini 3.8 text-to-speech

**原文标题**: Gemini 3.8 text-to-speech

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/)

生成摘要时出错

---

## 8. Radicle: Disclosure of Vulnerability in the Network Protocol

**原文标题**: Radicle: Disclosure of Vulnerability in the Network Protocol

**原文链接**: [https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol](https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol)

生成摘要时出错

---

## 9. Jev in 25 Lines of Python

**原文标题**: Jev in 25 Lines of Python

**原文链接**: [https://www.nobodywho.ai/posts/jev-in-25-lines/](https://www.nobodywho.ai/posts/jev-in-25-lines/)

生成摘要时出错

---

## 10. GPT-6 Sol and Luna

**原文标题**: GPT-6 Sol and Luna

**原文链接**: [https://openai.com/index/introducing-gpt-6-sol-and-luna/](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 2 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 3 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 4 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 5 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 6 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 7 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 8 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 9 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 10 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 11 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 12 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 13 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 14 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 15 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 16 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 17 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 18 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 19 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 20 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 21 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 22 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 23 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 24 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 25 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 26 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 27 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 28 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 29 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 30 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 31 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 32 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 33 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 34 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 35 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 36 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 37 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 38 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 39 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 40 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 41 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 42 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 43 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 44 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 45 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 46 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 47 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 48 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 49 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 50 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 51 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 52 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 53 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 54 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 55 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 56 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 57 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 58 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 59 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 60 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 61 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 62 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 63 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 64 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 65 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 66 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 67 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 68 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 69 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 70 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 71 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 72 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 73 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 74 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 75 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 76 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 77 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 78 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 79 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 80 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 81 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 82 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 83 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 84 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 85 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 86 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 87 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 88 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 89 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 90 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 91 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 92 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 93 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 94 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 95 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 96 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 97 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 98 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 99 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 100 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 101 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 102 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 103 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 104 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 105 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 106 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 107 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 108 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 109 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 110 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 111 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 112 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 113 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 114 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 115 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 116 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 117 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 118 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 119 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 120 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 121 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 122 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 123 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 124 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 125 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 126 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 127 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 128 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 129 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 130 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 131 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 132 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 133 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 134 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 135 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 136 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 137 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 138 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 139 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 140 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 141 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 142 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 143 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 144 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 145 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 146 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 147 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 148 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 149 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 150 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 151 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 152 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 153 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 154 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 155 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 156 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 157 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 158 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 159 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 160 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 161 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 162 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 163 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 164 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 165 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 166 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 167 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 168 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 169 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 170 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 171 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 172 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 173 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 174 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 175 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 176 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 177 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 178 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 179 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 180 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 181 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 182 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 183 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 184 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 185 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 186 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 187 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 188 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 189 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 190 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 191 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 192 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 193 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 194 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 195 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 196 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 197 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 198 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 199 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 200 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 201 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 202 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 203 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 204 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 205 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 206 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 207 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 208 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 209 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 210 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 211 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 212 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 213 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 214 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 215 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 216 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 217 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 218 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 219 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 220 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 221 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 222 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 223 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 224 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 225 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 226 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 227 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 228 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 229 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 230 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 231 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 232 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 233 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 234 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 235 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 236 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 237 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 238 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 239 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 240 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 241 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 242 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 243 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 244 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 245 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 246 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 247 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 248 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 249 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 250 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 251 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 252 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 253 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 254 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 255 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 256 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 257 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 258 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 259 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 260 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 261 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 262 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 263 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 264 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 265 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 266 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 267 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 268 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 269 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 270 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 271 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 272 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 273 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 274 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 275 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 276 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 277 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 278 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 279 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 280 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 281 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 282 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 283 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 284 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 285 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 286 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 287 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 288 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 289 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 290 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 291 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 292 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 293 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 294 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 295 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 296 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 297 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 298 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 299 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 300 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 301 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 302 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 303 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 304 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 305 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 306 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 307 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 308 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 309 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 310 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 311 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 312 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 313 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 314 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 315 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 316 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 317 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 318 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 319 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 320 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 321 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 322 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 323 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 324 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 325 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 326 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 327 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 328 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 329 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 330 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 331 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 332 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 333 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 334 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 335 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 336 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 337 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 338 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 339 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 340 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 341 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 342 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 343 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 344 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 345 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 346 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 347 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 348 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 349 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 350 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 351 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 352 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 353 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 354 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 355 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 356 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 357 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 358 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 359 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 360 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 361 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 362 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 363 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 364 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 365 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 366 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 367 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 368 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 369 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 370 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 371 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 372 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 373 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 374 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 375 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 376 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 377 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 378 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 379 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 380 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 381 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 382 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 383 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 384 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 385 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 386 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 387 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 388 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 389 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 390 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 391 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 392 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 393 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 394 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 395 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 396 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 397 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 398 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 399 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 400 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 401 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 402 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 403 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 404 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 405 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 406 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 407 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 408 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 409 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 410 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 411 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 412 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 413 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 414 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 415 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 416 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 417 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 418 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 419 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 420 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 421 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 422 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 423 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 424 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 425 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 426 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 427 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 428 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 429 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 430 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 431 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 432 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 433 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 434 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 435 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 436 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 437 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 438 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 439 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 440 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 441 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 442 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 443 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 444 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 445 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 446 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 447 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 448 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 449 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 450 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 451 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 452 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 453 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 454 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 455 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 456 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 457 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 458 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 459 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 460 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 461 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 462 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 463 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 464 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 465 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 466 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 467 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 468 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 469 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 470 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 471 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 472 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 473 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 474 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 475 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 476 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 477 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 478 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 479 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 480 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 481 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 482 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 483 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 484 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 485 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 486 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 487 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 488 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 489 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 490 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 491 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 492 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 493 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 494 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 495 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 496 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 497 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 498 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 499 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 500 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 501 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 502 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 503 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 504 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 505 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 506 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 507 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 508 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 509 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 510 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 511 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 512 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 513 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 514 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 515 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 516 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 517 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 518 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 519 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 520 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 521 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 522 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 523 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 524 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 525 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 526 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 527 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 528 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 529 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 530 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 531 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 532 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 533 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 534 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 535 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 536 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 537 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 538 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 539 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 540 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 541 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 542 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 543 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 544 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 545 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 546 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 547 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 548 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 549 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 550 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
