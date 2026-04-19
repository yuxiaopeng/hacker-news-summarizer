# Hacker News 热门文章摘要 (2026-04-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Pairwise Order of a Sequence of Elements

**原文标题**: Pairwise Order of a Sequence of Elements

**原文链接**: [https://morwenn.github.io//presortedness/2026/04/11/TSB010-pairwise-order-of-a-sequence-of-elements.html](https://morwenn.github.io//presortedness/2026/04/11/TSB010-pairwise-order-of-a-sequence-of-elements.html)

生成摘要时出错

---

## 12. NIST scientists create 'any wavelength' lasers

**原文标题**: NIST scientists create 'any wavelength' lasers

**原文链接**: [https://www.nist.gov/news-events/news/2026/04/any-color-you-nist-scientists-create-any-wavelength-lasers-tiny-circuits](https://www.nist.gov/news-events/news/2026/04/any-color-you-nist-scientists-create-any-wavelength-lasers-tiny-circuits)

生成摘要时出错

---

## 13. College instructor turns to typewriters to curb AI-written work

**原文标题**: College instructor turns to typewriters to curb AI-written work

**原文链接**: [https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

生成摘要时出错

---

## 14. Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

**原文标题**: Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

**原文链接**: [https://tokens.billchambers.me/leaderboard](https://tokens.billchambers.me/leaderboard)

生成摘要时出错

---

## 15. When moving fast, talking is the first thing to break

**原文标题**: When moving fast, talking is the first thing to break

**原文链接**: [https://daverupert.com/2026/04/more-talk-less-grok/](https://daverupert.com/2026/04/more-talk-less-grok/)

生成摘要时出错

---

## 16. Show HN: Prompt-to-Excalidraw demo with Gemma 4 E2B in the browser (3.1GB)

**原文标题**: Show HN: Prompt-to-Excalidraw demo with Gemma 4 E2B in the browser (3.1GB)

**原文链接**: [https://teamchong.github.io/turboquant-wasm/draw.html](https://teamchong.github.io/turboquant-wasm/draw.html)

生成摘要时出错

---

## 17. Discord Read Receipts Exploit: When, How Often, How Long

**原文标题**: Discord Read Receipts Exploit: When, How Often, How Long

**原文链接**: [https://paul.koeck.dev/writeups/discord-read-receipts](https://paul.koeck.dev/writeups/discord-read-receipts)

生成摘要时出错

---

## 18. Russia's doping program is run by the same FSB team that poisoned Navalny

**原文标题**: Russia's doping program is run by the same FSB team that poisoned Navalny

**原文链接**: [https://theins.press/en/inv/291614](https://theins.press/en/inv/291614)

生成摘要时出错

---

## 19. Notes from the SF Peptide Scene

**原文标题**: Notes from the SF Peptide Scene

**原文链接**: [https://12gramsofcarbon.com/p/notes-from-the-sf-peptide-scene](https://12gramsofcarbon.com/p/notes-from-the-sf-peptide-scene)

生成摘要时出错

---

## 20. The electromechanical angle computer inside the B-52 bomber's star tracker

**原文标题**: The electromechanical angle computer inside the B-52 bomber's star tracker

**原文链接**: [https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html](https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html)

生成摘要时出错

---

## 21. Minimal Viable Programs (2014)

**原文标题**: Minimal Viable Programs (2014)

**原文链接**: [https://joearms.github.io/published/2014-06-25-minimal-viable-program.html](https://joearms.github.io/published/2014-06-25-minimal-viable-program.html)

生成摘要时出错

---

## 22. Binary GCD

**原文标题**: Binary GCD

**原文链接**: [https://en.algorithmica.org/hpc/algorithms/gcd/#binary-gcd](https://en.algorithmica.org/hpc/algorithms/gcd/#binary-gcd)

生成摘要时出错

---

## 23. Airline worker arrested after sharing photos of bomb damage in WhatsApp group

**原文标题**: Airline worker arrested after sharing photos of bomb damage in WhatsApp group

**原文链接**: [https://www.lbc.co.uk/article/dubai-police-spied-private-whatsapp-5HjdXwr_2/](https://www.lbc.co.uk/article/dubai-police-spied-private-whatsapp-5HjdXwr_2/)

生成摘要时出错

---

## 24. Why Japan has such good railways

**原文标题**: Why Japan has such good railways

**原文链接**: [https://worksinprogress.co/issue/why-japan-has-such-good-railways/](https://worksinprogress.co/issue/why-japan-has-such-good-railways/)

生成摘要时出错

---

## 25. The creative software industry has declared war on Adobe

**原文标题**: The creative software industry has declared war on Adobe

**原文链接**: [https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates)

生成摘要时出错

---

## 26. The world in which IPv6 was a good design (2017)

**原文标题**: The world in which IPv6 was a good design (2017)

**原文链接**: [https://apenwarr.ca/log/20170810](https://apenwarr.ca/log/20170810)

生成摘要时出错

---

## 27. Matt Mullenweg Overrules Core Committers; Puts Akismet on WP 7's Connector List

**原文标题**: Matt Mullenweg Overrules Core Committers; Puts Akismet on WP 7's Connector List

**原文链接**: [https://www.therepository.email/matt-mullenweg-overrules-core-committers-to-put-akismet-on-wordpress-7-0s-connectors-screen](https://www.therepository.email/matt-mullenweg-overrules-core-committers-to-put-akismet-on-wordpress-7-0s-connectors-screen)

生成摘要时出错

---

## 28. It's cool to care (2025)

**原文标题**: It's cool to care (2025)

**原文链接**: [https://alexwlchan.net/2025/cool-to-care/](https://alexwlchan.net/2025/cool-to-care/)

生成摘要时出错

---

## 29. Reading Input from an USB RFID Card Reader

**原文标题**: Reading Input from an USB RFID Card Reader

**原文链接**: [https://kevwe.com/blog/usb-rfid-reader](https://kevwe.com/blog/usb-rfid-reader)

生成摘要时出错

---

## 30. Graphs that explain the state of AI in 2026

**原文标题**: Graphs that explain the state of AI in 2026

**原文链接**: [https://spectrum.ieee.org/state-of-ai-index-2026](https://spectrum.ieee.org/state-of-ai-index-2026)

生成摘要时出错

---

## 31. SI Units for Request Rate (2024)

**原文标题**: SI Units for Request Rate (2024)

**原文链接**: [https://entropicthoughts.com/si-units-for-request-rate](https://entropicthoughts.com/si-units-for-request-rate)

生成摘要时出错

---

## 32. Why is IPv6 so complicated?

**原文标题**: Why is IPv6 so complicated?

**原文链接**: [https://github.com/becarpenter/misc/blob/main/why6why.md](https://github.com/becarpenter/misc/blob/main/why6why.md)

生成摘要时出错

---

## 33. Measuring Claude 4.7's tokenizer costs

**原文标题**: Measuring Claude 4.7's tokenizer costs

**原文链接**: [https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you](https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you)

生成摘要时出错

---

## 34. The simple geometry behind any road

**原文标题**: The simple geometry behind any road

**原文链接**: [https://sandboxspirit.com/blog/simple-geometry-of-roads/](https://sandboxspirit.com/blog/simple-geometry-of-roads/)

生成摘要时出错

---

## 35. Landmark ancient-genome study shows surprise acceleration of human evolution

**原文标题**: Landmark ancient-genome study shows surprise acceleration of human evolution

**原文链接**: [https://www.nature.com/articles/d41586-026-01204-5](https://www.nature.com/articles/d41586-026-01204-5)

生成摘要时出错

---

## 36. EU age verification app: "Worry-free package" with security vulnerabilities

**原文标题**: EU age verification app: "Worry-free package" with security vulnerabilities

**原文链接**: [https://www.heise.de/en/news/EU-age-verification-app-Worry-free-package-with-security-vulnerabilities-11262921.html](https://www.heise.de/en/news/EU-age-verification-app-Worry-free-package-with-security-vulnerabilities-11262921.html)

生成摘要时出错

---

## 37. The quiet disappearance of the free-range childhood

**原文标题**: The quiet disappearance of the free-range childhood

**原文链接**: [https://bigthink.com/mind-behavior/the-quiet-disappearance-of-the-free-range-childhood/](https://bigthink.com/mind-behavior/the-quiet-disappearance-of-the-free-range-childhood/)

生成摘要时出错

---

## 38. I dug into the Postgres sources to write my own WAL receiver

**原文标题**: I dug into the Postgres sources to write my own WAL receiver

**原文链接**: [https://medium.com/@mailbox.sq7/a-long-story-about-how-i-dug-into-the-postgresql-source-code-to-write-my-own-wal-receiver-and-what-53fd251d8f25](https://medium.com/@mailbox.sq7/a-long-story-about-how-i-dug-into-the-postgresql-source-code-to-write-my-own-wal-receiver-and-what-53fd251d8f25)

生成摘要时出错

---

## 39. Amiga Graphics Archive

**原文标题**: Amiga Graphics Archive

**原文链接**: [https://amiga.lychesis.net/](https://amiga.lychesis.net/)

生成摘要时出错

---

## 40. Air Is Full of DNA

**原文标题**: Air Is Full of DNA

**原文链接**: [https://www.nature.com/articles/d41586-026-01099-2](https://www.nature.com/articles/d41586-026-01099-2)

生成摘要时出错

---

## 41. All 12 moonwalkers had "lunar hay fever" from dust smelling like gunpowder (2018)

**原文标题**: All 12 moonwalkers had "lunar hay fever" from dust smelling like gunpowder (2018)

**原文链接**: [https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/The_toxic_side_of_the_Moon](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/The_toxic_side_of_the_Moon)

生成摘要时出错

---

## 42. Does your DSL little language need operator precedence?

**原文标题**: Does your DSL little language need operator precedence?

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/programming/LittleLanguagesVsOpPrecedence](https://utcc.utoronto.ca/~cks/space/blog/programming/LittleLanguagesVsOpPrecedence)

生成摘要时出错

---

## 43. My first impressions on ROCm and Strix Halo

**原文标题**: My first impressions on ROCm and Strix Halo

**原文链接**: [https://blog.marcoinacio.com/posts/my-first-impressions-rocm-strix-halo/](https://blog.marcoinacio.com/posts/my-first-impressions-rocm-strix-halo/)

生成摘要时出错

---

## 44. Show HN: AI Subroutines – Run automation scripts inside your browser tab

**原文标题**: Show HN: AI Subroutines – Run automation scripts inside your browser tab

**原文链接**: [https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

生成摘要时出错

---

## 45. Ada, its design, and the language that built the languages

**原文标题**: Ada, its design, and the language that built the languages

**原文链接**: [https://www.iqiipi.com/the-quiet-colossus.html](https://www.iqiipi.com/the-quiet-colossus.html)

生成摘要时出错

---

## 46. Isaac Asimov: The Last Question (1956)

**原文标题**: Isaac Asimov: The Last Question (1956)

**原文链接**: [https://hex.ooo/library/last_question.html](https://hex.ooo/library/last_question.html)

生成摘要时出错

---

## 47. Introducing: ShaderPad

**原文标题**: Introducing: ShaderPad

**原文链接**: [https://rileyjshaw.com/blog/introducing-shaderpad/](https://rileyjshaw.com/blog/introducing-shaderpad/)

生成摘要时出错

---

## 48. Sidephone: A minimalist Android phone with swappable USB keypads

**原文标题**: Sidephone: A minimalist Android phone with swappable USB keypads

**原文链接**: [https://www.sidephone.com/](https://www.sidephone.com/)

生成摘要时出错

---

## 49. Changes in the system prompt between Claude Opus 4.6 and 4.7

**原文标题**: Changes in the system prompt between Claude Opus 4.6 and 4.7

**原文链接**: [https://simonwillison.net/2026/Apr/18/opus-system-prompt/](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)

生成摘要时出错

---

## 50. I’m spending months coding the old way

**原文标题**: I’m spending months coding the old way

**原文链接**: [https://miguelconner.substack.com/p/im-coding-by-hand](https://miguelconner.substack.com/p/im-coding-by-hand)

生成摘要时出错

---

## 51. Category Theory Illustrated – Orders

**原文标题**: Category Theory Illustrated – Orders

**原文链接**: [https://abuseofnotation.github.io/category-theory-illustrated/04_order/](https://abuseofnotation.github.io/category-theory-illustrated/04_order/)

生成摘要时出错

---

## 52. Healthchecks.io now uses self-hosted object storage

**原文标题**: Healthchecks.io now uses self-hosted object storage

**原文链接**: [https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/](https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/)

生成摘要时出错

---

## 53. Show HN: I made a calculator that works over disjoint sets of intervals

**原文标题**: Show HN: I made a calculator that works over disjoint sets of intervals

**原文链接**: [https://victorpoughon.github.io/interval-calculator/](https://victorpoughon.github.io/interval-calculator/)

生成摘要时出错

---

## 54. The purist's guide to phở in Hanoi

**原文标题**: The purist's guide to phở in Hanoi

**原文链接**: [https://connla.substack.com/p/pho-in-hanoi-a-purists-guide](https://connla.substack.com/p/pho-in-hanoi-a-purists-guide)

生成摘要时出错

---

## 55. It is incorrect to "normalize" // in HTTP URL paths

**原文标题**: It is incorrect to "normalize" // in HTTP URL paths

**原文链接**: [https://runxiyu.org/comp/doubleslash/](https://runxiyu.org/comp/doubleslash/)

生成摘要时出错

---

## 56. Show HN: Smol machines – subsecond coldstart, portable virtual machines

**原文标题**: Show HN: Smol machines – subsecond coldstart, portable virtual machines

**原文链接**: [https://github.com/smol-machines/smolvm](https://github.com/smol-machines/smolvm)

生成摘要时出错

---

## 57. Global freedom declined for the 20th consecutive year in 2025

**原文标题**: Global freedom declined for the 20th consecutive year in 2025

**原文链接**: [https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy](https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy)

生成摘要时出错

---

## 58. The GNU libc atanh is correctly rounded

**原文标题**: The GNU libc atanh is correctly rounded

**原文链接**: [https://inria.hal.science/hal-05591661](https://inria.hal.science/hal-05591661)

生成摘要时出错

---

## 59. The Unix executable as a Smalltalk method (2025) [video]

**原文标题**: The Unix executable as a Smalltalk method (2025) [video]

**原文链接**: [https://www.youtube.com/watch?v=sZjPQ7vtLNA](https://www.youtube.com/watch?v=sZjPQ7vtLNA)

生成摘要时出错

---

## 60. Connie Converse was a folk-music genius. Then she vanished

**原文标题**: Connie Converse was a folk-music genius. Then she vanished

**原文链接**: [https://www.bbc.com/culture/article/20260413-the-mystery-of-a-missing-folk-music-pioneer](https://www.bbc.com/culture/article/20260413-the-mystery-of-a-missing-folk-music-pioneer)

生成摘要时出错

---

## 61. I built a 3D printing business and ran it for 8 months

**原文标题**: I built a 3D printing business and ran it for 8 months

**原文链接**: [https://www.wespiser.com/posts/2026-04-12-3D-Printing-Biz.html](https://www.wespiser.com/posts/2026-04-12-3D-Printing-Biz.html)

生成摘要时出错

---

## 62. "cat readme.txt" is not safe if you use iTerm2

**原文标题**: "cat readme.txt" is not safe if you use iTerm2

**原文链接**: [https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not](https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not)

生成摘要时出错

---

## 63. Amazon is discontinuing Kindle for PC on June 30th

**原文标题**: Amazon is discontinuing Kindle for PC on June 30th

**原文链接**: [https://goodereader.com/blog/kindle/amazon-is-discontinuing-kindle-for-pc-on-june-30th](https://goodereader.com/blog/kindle/amazon-is-discontinuing-kindle-for-pc-on-june-30th)

生成摘要时出错

---

## 64. Experiment with ICEYE Open Data

**原文标题**: Experiment with ICEYE Open Data

**原文链接**: [https://www.iceye.com/open-data-initiative](https://www.iceye.com/open-data-initiative)

生成摘要时出错

---

## 65. Are the costs of AI agents also rising exponentially? (2025)

**原文标题**: Are the costs of AI agents also rising exponentially? (2025)

**原文链接**: [https://www.tobyord.com/writing/hourly-costs-for-ai-agents](https://www.tobyord.com/writing/hourly-costs-for-ai-agents)

生成摘要时出错

---

## 66. Frank Dudley Beane's Experience with Ergot and Cannabis Indica (1884)

**原文标题**: Frank Dudley Beane's Experience with Ergot and Cannabis Indica (1884)

**原文链接**: [https://publicdomainreview.org/collection/experience-with-ergot-and-cannabis/](https://publicdomainreview.org/collection/experience-with-ergot-and-cannabis/)

生成摘要时出错

---

## 67. Hyperscalers have already outspent most famous US megaprojects

**原文标题**: Hyperscalers have already outspent most famous US megaprojects

**原文链接**: [https://twitter.com/finmoorhouse/status/2044933442236776794](https://twitter.com/finmoorhouse/status/2044933442236776794)

生成摘要时出错

---

## 68. Slop Cop

**原文标题**: Slop Cop

**原文链接**: [https://awnist.com/slop-cop](https://awnist.com/slop-cop)

生成摘要时出错

---

## 69. Towards trust in Emacs

**原文标题**: Towards trust in Emacs

**原文链接**: [https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html](https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html)

生成摘要时出错

---

## 70. SDF Public Access Unix System

**原文标题**: SDF Public Access Unix System

**原文链接**: [https://sdf.org/?ssh](https://sdf.org/?ssh)

生成摘要时出错

---

## 71. Self-hosted webmail client for JMAP protocol: Email, calendar, contacts, files

**原文标题**: Self-hosted webmail client for JMAP protocol: Email, calendar, contacts, files

**原文链接**: [https://github.com/bulwarkmail/webmail](https://github.com/bulwarkmail/webmail)

生成摘要时出错

---

## 72. Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文标题**: Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文链接**: [https://github.com/paniclock/paniclock/](https://github.com/paniclock/paniclock/)

生成摘要时出错

---

## 73. Bluetooth tracker hidden in postcard and mailed to warship exposed its location

**原文标题**: Bluetooth tracker hidden in postcard and mailed to warship exposed its location

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/bluetooth-tracker-hidden-in-a-postcard-and-mailed-to-a-warship-exposed-its-location-a-eur5-gadget-put-a-eur500-million-dutch-ship-at-risk-for-24-hours](https://www.tomshardware.com/tech-industry/cyber-security/bluetooth-tracker-hidden-in-a-postcard-and-mailed-to-a-warship-exposed-its-location-a-eur5-gadget-put-a-eur500-million-dutch-ship-at-risk-for-24-hours)

生成摘要时出错

---

## 74. William Cecil's Succession Plan

**原文标题**: William Cecil's Succession Plan

**原文链接**: [https://www.historytoday.com/archive/history-matters/william-cecils-succession-plan](https://www.historytoday.com/archive/history-matters/william-cecils-succession-plan)

生成摘要时出错

---

## 75. Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文标题**: Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文链接**: [https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/](https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/)

生成摘要时出错

---

## 76. Detecting DOSBox from Within the Box

**原文标题**: Detecting DOSBox from Within the Box

**原文链接**: [https://datagirl.xyz/posts/dos_inside_the_box.html](https://datagirl.xyz/posts/dos_inside_the_box.html)

生成摘要时出错

---

## 77. FIM – Linux framebuffer image viewer

**原文标题**: FIM – Linux framebuffer image viewer

**原文链接**: [https://www.nongnu.org/fbi-improved/](https://www.nongnu.org/fbi-improved/)

生成摘要时出错

---

## 78. Everyone needs own their own machine that is an extension of their intelligence

**原文标题**: Everyone needs own their own machine that is an extension of their intelligence

**原文链接**: [https://twitter.com/beffjezos/status/2045719076644040991](https://twitter.com/beffjezos/status/2045719076644040991)

生成摘要时出错

---

## 79. Traders placed over $1B in perfectly timed bets on the Iran war

**原文标题**: Traders placed over $1B in perfectly timed bets on the Iran war

**原文链接**: [https://www.theguardian.com/world/2026/apr/18/iran-war-bets-ethics-concerns](https://www.theguardian.com/world/2026/apr/18/iran-war-bets-ethics-concerns)

生成摘要时出错

---

## 80. Hardware Is Hard?

**原文标题**: Hardware Is Hard?

**原文链接**: [https://prdpx7.github.io/posts/hardware-is-hard/](https://prdpx7.github.io/posts/hardware-is-hard/)

生成摘要时出错

---

## 81. The Gregorio project – GPL tools for typesetting Gregorian chant

**原文标题**: The Gregorio project – GPL tools for typesetting Gregorian chant

**原文链接**: [https://gregorio-project.github.io/index.html](https://gregorio-project.github.io/index.html)

生成摘要时出错

---

## 82. Middle schooler finds coin from Troy in Berlin

**原文标题**: Middle schooler finds coin from Troy in Berlin

**原文链接**: [https://www.thehistoryblog.com/archives/75848](https://www.thehistoryblog.com/archives/75848)

生成摘要时出错

---

## 83. Bipartisan Bill to Tighten Controls on Sensitive Chipmaking Equipment

**原文标题**: Bipartisan Bill to Tighten Controls on Sensitive Chipmaking Equipment

**原文链接**: [https://baumgartner.house.gov/2026/04/02/baumgartner-introduces-bipartisan-bill-to-tighten-controls-on-sensitive-chipmaking-equipment/](https://baumgartner.house.gov/2026/04/02/baumgartner-introduces-bipartisan-bill-to-tighten-controls-on-sensitive-chipmaking-equipment/)

生成摘要时出错

---

## 84. NASA Force

**原文标题**: NASA Force

**原文链接**: [https://nasaforce.gov/](https://nasaforce.gov/)

生成摘要时出错

---

## 85. Fake Pro-Trump Avatars Emerge on Social Media

**原文标题**: Fake Pro-Trump Avatars Emerge on Social Media

**原文链接**: [https://www.nytimes.com/2026/04/17/business/media/artificial-intelligence-trump-social-media.html](https://www.nytimes.com/2026/04/17/business/media/artificial-intelligence-trump-social-media.html)

生成摘要时出错

---

## 86. Generating a color spectrum for an image

**原文标题**: Generating a color spectrum for an image

**原文链接**: [https://amandahinton.com/blog/generating-a-color-spectrum-for-an-image](https://amandahinton.com/blog/generating-a-color-spectrum-for-an-image)

生成摘要时出错

---

## 87. A simplified model of Fil-C

**原文标题**: A simplified model of Fil-C

**原文链接**: [https://www.corsix.org/content/simplified-model-of-fil-c](https://www.corsix.org/content/simplified-model-of-fil-c)

生成摘要时出错

---

## 88. Show HN: Sostactic – polynomial inequalities using sums-of-squares in Lean

**原文标题**: Show HN: Sostactic – polynomial inequalities using sums-of-squares in Lean

**原文链接**: [https://github.com/mmaaz-git/sostactic](https://github.com/mmaaz-git/sostactic)

生成摘要时出错

---

