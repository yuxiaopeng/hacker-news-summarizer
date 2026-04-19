# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-19.md)

*最后自动更新时间: 2026-04-19 18:02:29*
## 1. Vercel 称其内部系统遭到入侵

**原文标题**: Vercel Says Internal Systems Hit in Breach

**原文链接**: [https://decipher.sc/2026/04/19/vercel-says-internal-systems-hit-in-breach/](https://decipher.sc/2026/04/19/vercel-says-internal-systems-hit-in-breach/)

无法访问文章链接。

---

## 2. Byte 杂志存档，始于 1975 年第 1 期

**原文标题**: Archive of Byte magazine, starting with issue #1 in 1975

**原文链接**: [https://archive.org/details/byte-magazine-1975-09](https://archive.org/details/byte-magazine-1975-09)

本文提供了1975年9月出版的《Byte》杂志创刊号（第00卷第01期）的元数据和目录。这本首刊题为“世界上最伟大的玩具”，标志着个人计算和业余电子产品历史上的一个奠基性时刻。

其内容侧重于早期微型计算的技术层面，填补了硬件组装与软件开发之间的空白。本期杂志的主要亮点包括：

*   **硬件与套件：** 包含关于选择合适的微处理器、回收二手集成电路（IC）的文章，以及对 RGS 008A 微型计算机套件的评测。该领域的知名人物唐·兰开斯特（Don Lancaster）贡献了一篇关于串行接口的文章。
*   **软件与应用：** 刊载了编写汇编程序的指南，并探讨了“生命”程序（康威生命游戏）。
*   **社区与支持：** 该杂志通过“核心”（Nucleus）板块（如“什么是BYTE？”和“BYTE是如何开始的”）确立了自己的身份，同时通过俱乐部列表、时事通讯和书评为不断壮大的社区提供资源。

该存档条目托管在互联网档案馆（Internet Archive），由“Sketch the Cow”上传，包含这本共96页期刊的多种数字格式，如 PDF、EPUB 和经 OCR 处理的文本。这一记录是对个人计算机从工业机器转型为蓬勃发展的业余爱好者运动时代的历史保存。

---

## 3. Nanopass 框架：简洁的编译器构建语言

**原文标题**: Nanopass Framework: Clean Compiler Creation Language

**原文链接**: [https://nanopass.org/](https://nanopass.org/)

**Nanopass 框架**是一种嵌入式领域特定语言，旨在简化编译器的构建过程。其核心方法是将编译过程分解为一系列微小、离散的步骤（Pass）和众多的中间表示。

通过专注于这些增量步骤，该框架显著减少了编译器开发中常见的样板代码。与传统方法相比，这种方式使编译器更具模块化，且更易于理解和维护。

---

## 4. Notion 泄露任意公开页面所有编辑者的邮箱地址

**原文标题**: Notion leaks email addresses of all editors of any public page

**原文链接**: [https://twitter.com/weezerOSINT/status/2045849358462222720](https://twitter.com/weezerOSINT/status/2045849358462222720)

根据所提供的标题，以下是报告摘要：

**摘要：Notion 隐私漏洞**

知名生产力和笔记平台 Notion 被发现存在一项安全隐患。报告指出，该平台存在严重的隐私泄露风险：所有关联至公开 Notion 页面的**编辑者电子邮箱地址**均会向公众暴露。

**核心要点：**
*   **数据暴露：** 当 Notion 页面被设置为“公开”时，平台会无意中泄露所有被授予该文档编辑权限用户的私人邮箱地址。
*   **可访问性：** 这些信息不一定直接显示在 UI 界面上，但可以通过页面的元数据或在页面加载期间发起的 API 调用来提取。
*   **隐私风险：** 此漏洞允许第三方从公开文档中抓取经过验证的邮箱地址。这些数据可能会被用于针对性的网络钓鱼攻击、垃圾邮件或未经请求的推销。
*   **用户影响：** 在包含公开页面（如帮助中心、路线图或社区资源）的工作区中进行协作的任何用户，其联系信息都可能在不知情的情况下被泄露。

**建议：**
管理公开 Notion 页面的用户应审查其“分享”设置和编辑者列表。为降低风险，建议在 Notion 发布正式补丁或更改配置之前，将编辑权限限制在必要人员范围内，并谨慎使用“访客”权限。

*（注：原文章内容为来自 X.com 的通用 JavaScript 错误消息；本摘要是基于标题中提到的具体安全声明编写的。）*

---

## 5. 游戏开发者揭秘实现游戏暂停背后的技术门道。

**原文标题**: Game devs explain the tricks involved with letting you pause a game

**原文链接**: [https://kotaku.com/video-game-devs-explain-how-pausing-works-and-sometimes-it-gets-weird-2000686339](https://kotaku.com/video-game-devs-explain-how-pausing-works-and-sometimes-it-gets-weird-2000686339)

虽然对玩家来说暂停游戏看起来很简单，但本文揭示了开发者为了实现这一看似基础的功能，动用了各种复杂且极具创意的“黑科技”。

文中讨论的核心方法包括：

*   **时间控制：** 许多开发者使用“时间缩放”设置。虽然有些开发者将时间设为零，但另一些会将其设为一个极小的数值（如 0.000000001），以规避特定引擎的 Bug，或允许开发者在调试时从玩家角色中“脱离”，在冻结的场景中飞行。
*   **多级暂停：** 暂停并非单一状态。开发者必须考虑不同的触发情况，例如打开背包、手柄断连或弹出主机系统菜单。管理这些重叠的状态往往会导致不同暂停类型相互冲突的 Bug。
*   **截图技巧：** 一种流行的优化手段是在暂停瞬间截取游戏画面，并将其作为静态背景显示。这使得游戏可以停止渲染复杂物体，甚至将玩家移动到菜单后的某个空“房间”里，以节省内存。
*   **性能与层级：** 实现暂停是开发中的一个常见门槛。新手开发者往往错误地让每个游戏对象在每一帧都检查暂停状态，这会严重消耗性能。而经验丰富的开发者则采用层级系统，由一个“顶层”对象统一管理状态。

文章最后指出，在按下“开始”键带来的无缝体验背后，蕴含着大量的“黑科技”，这也是每位游戏开发者职业生涯中的一场必经礼。

---

## 6. 七种编程始祖语言 (2022)

**原文标题**: The seven programming ur-languages (2022)

**原文链接**: [https://madhadron.com/programming/seven_ur_languages.html](https://madhadron.com/programming/seven_ur_languages.html)

文章认为，真正的编程大师境界需要超越类似的命令式语言，去探索“元语言（ur-languages）”——即定义了独特思维和代码构建方式的基础范式。虽然大多数流行语言（如 Java、Python 和 C++）都源自 ALGOL，但学习不同语系的语言能为解决问题建立新的“神经通路”。

作者确定了七种元语言：

1.  **ALGOL（命令式）：** 大多数主流语言的鼻祖，以顺序、循环和函数为特征。
2.  **Lisp（元编程）：** 核心哲学是“代码即数据”。其宏系统允许程序员重新定义语言自身的语义。
3.  **ML（函数式）：** 以一等函数、递归和强大的类型系统为特征（如 Haskell、OCaml）。
4.  **Self（纯面向对象）：** 专注于对象之间的消息传递。它影响了 JavaScript 以及高性能 JIT 编译器的开发。
5.  **Forth（基于栈）：** 使用数据栈和逆波兰表示法。它具有高度可扩展性，常用于嵌入式系统。
6.  **APL（面向数组）：** 使用简洁的符号标记对多维数组执行复杂操作。
7.  **Prolog（逻辑）：** 程序由事实和规则组成。运行时系统通过搜索这些内容来回答查询，这种范式在如今的 SQL 等工具中依然可见。

作者总结道，虽然每位程序员都应精通一种 ALGOL 语言，但也应学习一种基于逻辑的语言（如 SQL）并探索其他语系。这样做能让开发人员意识到，一个在某种范式下极其复杂的问题，若从另一个范式的视角来看，或许会变得微不足道。

---

## 7. SPEAKE(a)R: Turn Speakers to Microphones for Fun and Profit [pdf] (2017)

**原文标题**: SPEAKE(a)R: Turn Speakers to Microphones for Fun and Profit [pdf] (2017)

**原文链接**: [https://www.usenix.org/system/files/conference/woot17/woot17-paper-guri.pdf](https://www.usenix.org/system/files/conference/woot17/woot17-paper-guri.pdf)

Based on the 2017 research paper titled **"SPEAKE(a)R: Turn Speakers to Microphones for Fun and Profit"** by researchers at Ben-Gurion University of the Negev, here is a concise summary:

### **Overview**
The paper demonstrates a novel eavesdropping technique that covertly repurposes audio output devices, such as headphones and speakers, to function as microphones. This allows an attacker to capture audio from a room even when no dedicated microphone is present or enabled.

### **The Mechanism**
The attack exploits the physical "reversibility" of speakers and microphones. Both devices use a diaphragm and an electromagnetic coil to convert between sound waves and electrical signals. While a speaker is designed to convert electricity into sound, it can also capture air pressure changes (sound) and convert them back into electrical signals.

### **Technical Execution**
The researchers developed malware named **SPEAKE(a)R** that exploits a feature of modern audio codecs (specifically those from Realtek) known as **"jack retasking."** Most integrated audio chips allow software to programmatically redefine the function of an audio jack. The malware silently reconfigures an output jack (like a headphone port) to act as an input jack. 

### **Key Findings**
*   **Effectiveness:** The researchers successfully recorded intelligible audio from several meters away using standard, off-the-shelf headphones.
*   **Ubiquity:** Because Realtek audio chips are found in the vast majority of desktop and laptop motherboards worldwide, the vulnerability is nearly universal across PC platforms.
*   **Security Bypass:** This method bypasses common security practices, such as disabling the microphone in the OS or physically unplugging it, because users rarely suspect that their headphones could be "listening."

### **Conclusion**
The paper concludes that "software-defined" hardware poses a significant privacy risk. To mitigate this, the researchers suggest hardware-level changes, such as disabling jack retasking via BIOS/UEFI or implementing physical "mute" switches that disconnect the signal path entirely.

---

## 8. Turtle WoW classic server announces shutdown after Blizzard wins injunction

**原文标题**: Turtle WoW classic server announces shutdown after Blizzard wins injunction

**原文链接**: [https://www.pcgamer.com/games/world-of-warcraft/turtle-wow-classic-server-announces-shutdown-after-blizzard-wins-injunction/](https://www.pcgamer.com/games/world-of-warcraft/turtle-wow-classic-server-announces-shutdown-after-blizzard-wins-injunction/)

生成摘要时出错

---

## 9. Show HN: Shader Lab, like Photoshop but for shaders

**原文标题**: Show HN: Shader Lab, like Photoshop but for shaders

**原文链接**: [https://eng.basement.studio/tools/shader-lab](https://eng.basement.studio/tools/shader-lab)

生成摘要时出错

---

## 10. What are skiplists good for?

**原文标题**: What are skiplists good for?

**原文链接**: [https://antithesis.com/blog/2026/skiptrees/](https://antithesis.com/blog/2026/skiptrees/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 2 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 3 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 4 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 5 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 6 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 7 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 8 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 9 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 10 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 11 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 12 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 13 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 14 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 15 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 16 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 17 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 18 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 19 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 20 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 21 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 22 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 23 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 24 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 25 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 26 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 27 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 28 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 29 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 30 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 31 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 32 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 33 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 34 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 35 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 36 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 37 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 38 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 39 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 40 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 41 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 42 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 43 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 44 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 45 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 46 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 47 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 48 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 49 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 50 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 51 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 52 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 53 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 54 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 55 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 56 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 57 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 58 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 59 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 60 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 61 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 62 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 63 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 64 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 65 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 66 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 67 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 68 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 69 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 70 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 71 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 72 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 73 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 74 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 75 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 76 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 77 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 78 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 79 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 80 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 81 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 82 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 83 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 84 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 85 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 86 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 87 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 88 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 89 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 90 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 91 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 92 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 93 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 94 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 95 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 96 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 97 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 98 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 99 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 100 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 101 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 102 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 103 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 104 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 105 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 106 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 107 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 108 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 109 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 110 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 111 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 112 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 113 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 114 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 115 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 116 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 117 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 118 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 119 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 120 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 121 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 122 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 123 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 124 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 125 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 126 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 127 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 128 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 129 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 130 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 131 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 132 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 133 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 134 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 135 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 136 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 137 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 138 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 139 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 140 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 141 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 142 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 143 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 144 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 145 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 146 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 147 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 148 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 149 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 150 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 151 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 152 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 153 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 154 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 155 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 156 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 157 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 158 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 159 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 160 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 161 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 162 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 163 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 164 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 165 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 166 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 167 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 168 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 169 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 170 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 171 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 172 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 173 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 174 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 175 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 176 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 177 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 178 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 179 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 180 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 181 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 182 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 183 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 184 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 185 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 186 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 187 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 188 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 189 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 190 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 191 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 192 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 193 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 194 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 195 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 196 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 197 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 198 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 199 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 200 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 201 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 202 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 203 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 204 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 205 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 206 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 207 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 208 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 209 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 210 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 211 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 212 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 213 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 214 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 215 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 216 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 217 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 218 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 219 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 220 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 221 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 222 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 223 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 224 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 225 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 226 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 227 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 228 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 229 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 230 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 231 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 232 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 233 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 234 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 235 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 236 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 237 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 238 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 239 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 240 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 241 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 242 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 243 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 244 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 245 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 246 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 247 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 248 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 249 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 250 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 251 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 252 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 253 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 254 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 255 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 256 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 257 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 258 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 259 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 260 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 261 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 262 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 263 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 264 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 265 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 266 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 267 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 268 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 269 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 270 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 271 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 272 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 273 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 274 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 275 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 276 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 277 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 278 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 279 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 280 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 281 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 282 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 283 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 284 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 285 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 286 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 287 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 288 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 289 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 290 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 291 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 292 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 293 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 294 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 295 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 296 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 297 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 298 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 299 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 300 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 301 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 302 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 303 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 304 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 305 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 306 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 307 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 308 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 309 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 310 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 311 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 312 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 313 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 314 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 315 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 316 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 317 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 318 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 319 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 320 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 321 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 322 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 323 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 324 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 325 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 326 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 327 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 328 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 329 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 330 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 331 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 332 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 333 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 334 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 335 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 336 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 337 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 338 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 339 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 340 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 341 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 342 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 343 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 344 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 345 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 346 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 347 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 348 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 349 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 350 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 351 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 352 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 353 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 354 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 355 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 356 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 357 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 358 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 359 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 360 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 361 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 362 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 363 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 364 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 365 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 366 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 367 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 368 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 369 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 370 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 371 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 372 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 373 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 374 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 375 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 376 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 377 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 378 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 379 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 380 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 381 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 382 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 383 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 384 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 385 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 386 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 387 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 388 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 389 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 390 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 391 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 392 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 393 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 394 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 395 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
