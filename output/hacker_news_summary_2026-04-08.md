# Hacker News 热门文章摘要 (2026-04-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我把 Mac OS X 移植到了任天堂 Wii

**原文标题**: I Ported Mac OS X to the Nintendo Wii

**原文链接**: [https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)

本文详细介绍了将 Mac OS X 10.0 (Cheetah) 移植到 Nintendo Wii 的技术过程。尽管社区对此持怀疑态度，但作者判定 Wii 的 PowerPC 750CL 处理器（旧款 Mac 所用 G3 芯片的演进版本）在架构上是兼容的。虽然 Wii 仅有 88 MB 内存，但测试证实 Cheetah 能够在有限的内存下启动。

该项目涉及几个关键阶段：

*   **自定义引导加载程序：** 作者没有移植苹果的 Open Firmware，而是编写了一个自定义引导加载程序来初始化硬件，将 Mach-O 格式的 XNU 内核加载到内存中，并构建传递给操作系统的设备树。
*   **创意调试：** 由于内核执行早期会禁用标准的视频和串口输出，作者采用了“LED 闪烁”调试法——通过对内核二进制文件打补丁来切换 Wii 前面板指示灯的状态，从而跟踪执行进度。
*   **内核补丁：** 为了适配 Wii 独特的内存布局（MEM1 和 MEM2），作者修改了 XNU 内核的块地址转换 (BAT) 代码。这需要使用 QEMU 搭建一个旧版开发环境，以便编译已有 25 年历史的 XNU 源代码。
*   **驱动开发：** 该项目已成功实现内核、IOKit 和 BSD 子系统的初始化。然而，由于内核需要自定义 IOKit 驱动才能从 Wii 的 SD 卡中读取操作系统的其余部分，系统目前会停在“Still waiting for root device”错误处。

该项目证明了通过底层内核修改和自定义引导加载程序，在任天堂硬件上运行 Mac OS X 在技术上是可行的。详细说明和引导加载程序仓库可在作者的“wiiMac”项目中找到。

---

## 2. 阅读代码前我运行的 Git 命令

**原文标题**: Git commands I run before reading any code

**原文链接**: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)

本文概述了一种利用 Git 元数据而非初次代码审查来评估新代码库的诊断方法。作者认为，与手动阅读代码相比，提交历史能更高效地提供关于项目健康状况、团队动态和技术债务的“诊断图景”。

作者重点介绍了从 Git 命令中提取的五个关键指标：

1.  **高变更率 (High Churn)：** 识别更改最频繁的文件。高变更率通常与较高的缺陷率和“代码库阻力”相关，尤其是当开发人员害怕触碰这些特定文件时。
2.  **作者身份与公交系数 (Bus Factor)：** 使用 `shortlog` 确定系统的构建者。工作高度集中在某个人身上（特别是当此人不再活跃时）意味着重大的组织风险。
3.  **Bug 热点：** 筛选包含 “fix” 或 “bug” 等关键词的提交信息，以查看错误聚集的位置。同时出现在“高变更率”和“Bug 热点”列表中的文件被视为项目风险最高的区域。
4.  **提交速率：** 绘制随时间变化的提交频率图，以直观展现团队动力。曲线下滑或突然暴跌通常预示着关键人员的流失或团队正陷入难以维持开发进度的困境。
5.  **救火频率：** 监控团队在提交记录中使用 “revert”、“hotfix” 或 “emergency” 等词汇的频率。频繁的回滚表明团队对发布流程缺乏信心，且自动化测试不可靠。

通过在第一小时运行这些命令，审计员可以避免在代码中“漫游”，从而优先处理系统中问题最多、影响最大的区域，进行有针对性的调查。

---

## 3. Muse Spark：迈向个人超智能

**原文标题**: Muse Spark: Scaling Towards Personal Superintelligence

**原文链接**: [https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1](https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1)

无法访问文章链接。

---

## 4. 他们是肉做的 (1991)

**原文标题**: They're Made Out of Meat (1991)

**原文链接**: [http://www.terrybisson.com/theyre-made-out-of-meat-2/](http://www.terrybisson.com/theyre-made-out-of-meat-2/)

特里·比森（Terry Bisson）的短篇小说《他们是肉做的》（They’re Made Out of Meat）是两名刚刚探索完地球的外星生物之间的一段讽刺性对话。对话的核心在于，当他们发现地球上唯一的智慧生命——人类——完全由有机组织（即“肉”）组成时，所表现出的难以置信和厌恶感。

观察者们对人类进行了彻底的探测，并确认即使是大脑也“彻头彻尾都是肉”。他们认为“会思考的肉”这一概念从根本上是荒谬的，难以理解生物有机体如何能够产生意识、做梦或建造复杂的机器。他们将人类的交流贬低为通过“拍打肉体”或从中“喷射空气”所发出的“肉声”。

尽管官方协议要求他们联系并欢迎所有智慧生命，但这两个实体决定隐瞒他们的发现。他们得出结论，认为与“肉”互动的想法太令人反感，且人类受其生物本性限制太大——被困在“C空间”（光速）内且寿命短暂。他们决定删除访问记录，将该星区标记为“无人居住”，并将任何可能记得这次遭遇的人类视为“疯子”。

故事以一种深刻的讽刺收尾：当外星人准备联系一个“氢核星团”智慧体时，他们感叹如果宇宙中只有孤独的一方，那将是多么“言语无法形容的寒冷”。出于对生物生命的偏见，他们故意抛弃了一个正拼命发出接触信号以逃避这种孤独的物种。

---

## 5. Veracrypt project update

**原文标题**: Veracrypt project update

**原文链接**: [https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/](https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/)

In this project update posted on SourceForge, lead developer Mounir Idrassi provides an overview of the current status and future roadmap for VeraCrypt, the open-source disk encryption software.

The primary focus of the update is the completion of a comprehensive security audit conducted by **Quarkslab** and sponsored by the Open Source Technology Improvement Fund (OSTIF). The results were highly positive, with the auditors finding **no critical or high-severity vulnerabilities**. While some medium and low-severity issues were identified, Idrassi confirmed that most of these have already been resolved in the development code.

Key points regarding the upcoming **version 1.26.7** include:
*   **Security Fixes:** Integration of all fixes resulting from the Quarkslab audit.
*   **Hardware Support:** Improved compatibility and performance for modern hardware, specifically targeting ARM64 and Apple Silicon (M1/M2/M3) architectures.
*   **General Maintenance:** Various bug fixes, performance optimizations, and code cleanups to improve stability.

Idrassi also touched upon long-term goals, such as a potential modernization of the user interface, though he emphasized that security and reliability remain the project's top priorities. He acknowledged the slow pace of recent updates but reassured the community that the project is active and committed to maintaining its status as a robust encryption tool. The update concludes with a call for continued community support through donations to sustain development efforts.

---

## 6. MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

**原文标题**: MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

**原文链接**: [https://arxiv.org/abs/2604.05091](https://arxiv.org/abs/2604.05091)

生成摘要时出错

---

## 7. Muse Spark – Meta Superintelligence Labs

**原文标题**: Muse Spark – Meta Superintelligence Labs

**原文链接**: [https://meta.ai/](https://meta.ai/)

生成摘要时出错

---

## 8. Škoda DuoBell: A bicycle bell that penetrates noise-cancelling headphones

**原文标题**: Škoda DuoBell: A bicycle bell that penetrates noise-cancelling headphones

**原文链接**: [https://www.skoda-storyboard.com/en/skoda-world/skoda-duobell-a-bicycle-bell-that-outsmarts-even-smart-headphones/](https://www.skoda-storyboard.com/en/skoda-world/skoda-duobell-a-bicycle-bell-that-outsmarts-even-smart-headphones/)

生成摘要时出错

---

## 9. Microsoft Abruptly Terminates VeraCrypt Account, Halting Windows Updates

**原文标题**: Microsoft Abruptly Terminates VeraCrypt Account, Halting Windows Updates

**原文链接**: [https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/](https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/)

生成摘要时出错

---

## 10. US cities are axing Flock Safety surveillance technology

**原文标题**: US cities are axing Flock Safety surveillance technology

**原文链接**: [https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/](https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/)

生成摘要时出错

---

## 11. Understanding the Kalman Filter with a Simple Radar Example

**原文标题**: Understanding the Kalman Filter with a Simple Radar Example

**原文链接**: [https://kalmanfilter.net](https://kalmanfilter.net)

生成摘要时出错

---

## 12. Audio Reactive LED Strips Are Diabolically Hard

**原文标题**: Audio Reactive LED Strips Are Diabolically Hard

**原文链接**: [https://scottlawsonbc.com/post/audio-led](https://scottlawsonbc.com/post/audio-led)

生成摘要时出错

---

## 13. Show HN: Go-Bt: Minimalist Behavior Trees for Go

**原文标题**: Show HN: Go-Bt: Minimalist Behavior Trees for Go

**原文链接**: [https://github.com/rvitorper/go-bt](https://github.com/rvitorper/go-bt)

生成摘要时出错

---

## 14. Teardown of unreleased LG Rollable shows why rollable phones aren't a thing

**原文标题**: Teardown of unreleased LG Rollable shows why rollable phones aren't a thing

**原文链接**: [https://arstechnica.com/gadgets/2026/04/teardown-of-unreleased-lg-rollable-shows-why-rollable-phones-arent-a-thing/](https://arstechnica.com/gadgets/2026/04/teardown-of-unreleased-lg-rollable-shows-why-rollable-phones-arent-a-thing/)

生成摘要时出错

---

## 15. Revision Demoparty 2026: Razor1911 [video]

**原文标题**: Revision Demoparty 2026: Razor1911 [video]

**原文链接**: [https://www.youtube.com/watch?v=Lw4W9V57SKs&t=5716s](https://www.youtube.com/watch?v=Lw4W9V57SKs&t=5716s)

生成摘要时出错

---

## 16. We moved Railway's frontend off Next.js. Builds went from 10+ mins to under 2

**原文标题**: We moved Railway's frontend off Next.js. Builds went from 10+ mins to under 2

**原文链接**: [https://blog.railway.com/p/moving-railways-frontend-off-nextjs](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

生成摘要时出错

---

## 17. Show HN: TUI-use: Let AI agents control interactive terminal programs

**原文标题**: Show HN: TUI-use: Let AI agents control interactive terminal programs

**原文链接**: [https://github.com/onesuper/tui-use](https://github.com/onesuper/tui-use)

生成摘要时出错

---

## 18. Virtual Mars Traverse: Every inch of Curiosity rover's path since 2012 landing

**原文标题**: Virtual Mars Traverse: Every inch of Curiosity rover's path since 2012 landing

**原文链接**: [https://www.rovers.land/](https://www.rovers.land/)

生成摘要时出错

---

## 19. Show HN: Explore the Silk Roads through an interactive map

**原文标题**: Show HN: Explore the Silk Roads through an interactive map

**原文链接**: [https://www.intofarlands.com/silk-roads-map](https://www.intofarlands.com/silk-roads-map)

生成摘要时出错

---

## 20. Show HN: BAREmail ʕ·ᴥ·ʔ – minimalist Gmail client for bad WiFi

**原文标题**: Show HN: BAREmail ʕ·ᴥ·ʔ – minimalist Gmail client for bad WiFi

**原文链接**: [https://github.com/matt-virgo/baremail](https://github.com/matt-virgo/baremail)

生成摘要时出错

---

## 21. Your File System Is Already A Graph Database

**原文标题**: Your File System Is Already A Graph Database

**原文链接**: [https://rumproarious.com/2026/04/04/your-file-system-is-already-a-graph-database/](https://rumproarious.com/2026/04/04/your-file-system-is-already-a-graph-database/)

生成摘要时出错

---

## 22. Union types in C# 15

**原文标题**: Union types in C# 15

**原文链接**: [https://devblogs.microsoft.com/dotnet/csharp-15-union-types/](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/)

生成摘要时出错

---

## 23. Claude Managed Agents

**原文标题**: Claude Managed Agents

**原文链接**: [https://claude.com/blog/claude-managed-agents](https://claude.com/blog/claude-managed-agents)

生成摘要时出错

---

## 24. Show HN: I pipe free sports streams into Jellyfin – no ads, just HLS

**原文标题**: Show HN: I pipe free sports streams into Jellyfin – no ads, just HLS

**原文链接**: [https://github.com/pcruz1905/hls-restream-proxy](https://github.com/pcruz1905/hls-restream-proxy)

生成摘要时出错

---

## 25. Show HN: I built a navigation app that displays weather along the route

**原文标题**: Show HN: I built a navigation app that displays weather along the route

**原文链接**: [https://navimodo.com/](https://navimodo.com/)

生成摘要时出错

---

## 26. The Future of Everything Is Lies, I Guess

**原文标题**: The Future of Everything Is Lies, I Guess

**原文链接**: [https://aphyr.com/posts/411-the-future-of-everything-is-lies-i-guess](https://aphyr.com/posts/411-the-future-of-everything-is-lies-i-guess)

生成摘要时出错

---

## 27. Protect your shed

**原文标题**: Protect your shed

**原文链接**: [https://dylanbutler.dev/blog/protect-your-shed/](https://dylanbutler.dev/blog/protect-your-shed/)

生成摘要时出错

---

## 28. A Digital Compute-in-Memory Architecture for NFA Evaluation

**原文标题**: A Digital Compute-in-Memory Architecture for NFA Evaluation

**原文链接**: [https://dl.acm.org/doi/10.1145/3716368.3735157](https://dl.acm.org/doi/10.1145/3716368.3735157)

生成摘要时出错

---

## 29. System Card: Claude Mythos Preview [pdf]

**原文标题**: System Card: Claude Mythos Preview [pdf]

**原文链接**: [https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf](https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf)

生成摘要时出错

---

## 30. Show HN: We built a camera only robot vacuum for less than 300$ (Well almost)

**原文标题**: Show HN: We built a camera only robot vacuum for less than 300$ (Well almost)

**原文链接**: [https://indraneelpatil.github.io/blog/2026/robot-vacuum/](https://indraneelpatil.github.io/blog/2026/robot-vacuum/)

生成摘要时出错

---

## 31. Iran demands Bitcoin fees for ships passing Hormuz during ceasefire

**原文标题**: Iran demands Bitcoin fees for ships passing Hormuz during ceasefire

**原文链接**: [https://www.ft.com/content/02aefac4-ea62-48db-9326-c0da373b11b8](https://www.ft.com/content/02aefac4-ea62-48db-9326-c0da373b11b8)

生成摘要时出错

---

## 32. Mario and Earendil

**原文标题**: Mario and Earendil

**原文链接**: [https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/](https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/)

生成摘要时出错

---

## 33. Native Americans had dice 12k years ago

**原文标题**: Native Americans had dice 12k years ago

**原文链接**: [https://www.nbcnews.com/science/science-news/native-americans-dice-games-probability-study-rcna266426](https://www.nbcnews.com/science/science-news/native-americans-dice-games-probability-study-rcna266426)

生成摘要时出错

---

## 34. How to get better at guitar

**原文标题**: How to get better at guitar

**原文链接**: [https://www.jakeworth.com/posts/how-to-get-better-at-guitar/](https://www.jakeworth.com/posts/how-to-get-better-at-guitar/)

生成摘要时出错

---

## 35. Slightly safer vibecoding by adopting old hacker habits

**原文标题**: Slightly safer vibecoding by adopting old hacker habits

**原文链接**: [http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html](http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html)

生成摘要时出错

---

## 36. Project Glasswing: Securing critical software for the AI era

**原文标题**: Project Glasswing: Securing critical software for the AI era

**原文链接**: [https://www.anthropic.com/glasswing](https://www.anthropic.com/glasswing)

生成摘要时出错

---

## 37. S3 Files

**原文标题**: S3 Files

**原文链接**: [https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html](https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html)

生成摘要时出错

---

## 38. Show HN: We fingerprinted 178 AI models' writing styles and similarity clusters

**原文标题**: Show HN: We fingerprinted 178 AI models' writing styles and similarity clusters

**原文链接**: [https://rival.tips/research/model-similarity](https://rival.tips/research/model-similarity)

生成摘要时出错

---

## 39. Show HN: An interactive map of Tolkien's Middle-earth

**原文标题**: Show HN: An interactive map of Tolkien's Middle-earth

**原文链接**: [https://middle-earth-interactive-map.web.app/](https://middle-earth-interactive-map.web.app/)

生成摘要时出错

---

## 40. Lunar Flyby

**原文标题**: Lunar Flyby

**原文链接**: [https://www.nasa.gov/gallery/lunar-flyby/](https://www.nasa.gov/gallery/lunar-flyby/)

生成摘要时出错

---

## 41. The Harvard Library Passport

**原文标题**: The Harvard Library Passport

**原文链接**: [https://fi-le.net/stamps/](https://fi-le.net/stamps/)

生成摘要时出错

---

## 42. LLM plays an 8-bit Commander X16 game using structured "smart senses"

**原文标题**: LLM plays an 8-bit Commander X16 game using structured "smart senses"

**原文链接**: [https://pvp-ai.russell-harper.com](https://pvp-ai.russell-harper.com)

生成摘要时出错

---

## 43. Middle East ceasefire in serious doubt as Israel assaults Lebanon

**原文标题**: Middle East ceasefire in serious doubt as Israel assaults Lebanon

**原文链接**: [https://www.theguardian.com/world/2026/apr/08/middle-east-ceasefire-doubt-israel-lebanon-iran-oil-tankers](https://www.theguardian.com/world/2026/apr/08/middle-east-ceasefire-doubt-israel-lebanon-iran-oil-tankers)

生成摘要时出错

---

## 44. Show HN: Gemma 4 Multimodal Fine-Tuner for Apple Silicon

**原文标题**: Show HN: Gemma 4 Multimodal Fine-Tuner for Apple Silicon

**原文链接**: [https://github.com/mattmireles/gemma-tuner-multimodal](https://github.com/mattmireles/gemma-tuner-multimodal)

生成摘要时出错

---

## 45. A database of analog cameras that can be 3D printed

**原文标题**: A database of analog cameras that can be 3D printed

**原文链接**: [https://printed.analogcamera.space/](https://printed.analogcamera.space/)

生成摘要时出错

---

## 46. US and Iran agree to provisional ceasefire

**原文标题**: US and Iran agree to provisional ceasefire

**原文链接**: [https://www.theguardian.com/us-news/2026/apr/07/trump-iran-war-ceasefire](https://www.theguardian.com/us-news/2026/apr/07/trump-iran-war-ceasefire)

生成摘要时出错

---

## 47. Xilem – An experimental Rust native UI framework

**原文标题**: Xilem – An experimental Rust native UI framework

**原文链接**: [https://github.com/linebender/xilem](https://github.com/linebender/xilem)

生成摘要时出错

---

## 48. Sam Altman may control our future – can he be trusted?

**原文标题**: Sam Altman may control our future – can he be trusted?

**原文链接**: [https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)

生成摘要时出错

---

## 49. The Clock

**原文标题**: The Clock

**原文链接**: [https://blog.senko.net/the-clock](https://blog.senko.net/the-clock)

生成摘要时出错

---

## 50. Binary obfuscation used in AAA Games

**原文标题**: Binary obfuscation used in AAA Games

**原文链接**: [https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html](https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html)

生成摘要时出错

---

## 51. 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文标题**: 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文链接**: [https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q](https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q)

生成摘要时出错

---

## 52. Hobby CNC machining and resin casting (2015)

**原文标题**: Hobby CNC machining and resin casting (2015)

**原文链接**: [https://lcamtuf.coredump.cx/gcnc/](https://lcamtuf.coredump.cx/gcnc/)

生成摘要时出错

---

## 53. JSIR: A High-Level IR for JavaScript

**原文标题**: JSIR: A High-Level IR for JavaScript

**原文链接**: [https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

生成摘要时出错

---

## 54. A whole boss fight in 256 bytes

**原文标题**: A whole boss fight in 256 bytes

**原文链接**: [https://hellmood.111mb.de//A_whole_boss_fight_in_256_bytes.html](https://hellmood.111mb.de//A_whole_boss_fight_in_256_bytes.html)

生成摘要时出错

---

## 55. Brit says he is not elusive Bitcoin creator named by New York Times

**原文标题**: Brit says he is not elusive Bitcoin creator named by New York Times

**原文链接**: [https://www.bbc.com/news/articles/cgrl4l1y9yxo](https://www.bbc.com/news/articles/cgrl4l1y9yxo)

生成摘要时出错

---

## 56. The Image Boards of Hayao Miyazaki

**原文标题**: The Image Boards of Hayao Miyazaki

**原文链接**: [https://animationobsessive.substack.com/p/the-image-boards-of-hayao-miyazaki](https://animationobsessive.substack.com/p/the-image-boards-of-hayao-miyazaki)

生成摘要时出错

---

## 57. GLM-5.1: Towards Long-Horizon Tasks

**原文标题**: GLM-5.1: Towards Long-Horizon Tasks

**原文链接**: [https://z.ai/blog/glm-5.1](https://z.ai/blog/glm-5.1)

生成摘要时出错

---

## 58. Has electricity decoupled from natural gas prices in Germany?

**原文标题**: Has electricity decoupled from natural gas prices in Germany?

**原文链接**: [https://has-electricity-decoupled-yet.strommarktberatung.de](https://has-electricity-decoupled-yet.strommarktberatung.de)

生成摘要时出错

---

## 59. Cambodia unveils statue to honour famous landmine-sniffing rat

**原文标题**: Cambodia unveils statue to honour famous landmine-sniffing rat

**原文链接**: [https://www.bbc.com/news/articles/c0rx7xzd10xo](https://www.bbc.com/news/articles/c0rx7xzd10xo)

生成摘要时出错

---

## 60. Wildlife Conservation Police Are Searching Flock Cameras for ICE

**原文标题**: Wildlife Conservation Police Are Searching Flock Cameras for ICE

**原文链接**: [https://www.404media.co/floridas-wildlife-cops-are-searching-thousands-of-flock-cameras-for-ice/](https://www.404media.co/floridas-wildlife-cops-are-searching-thousands-of-flock-cameras-for-ice/)

生成摘要时出错

---

## 61. Digital Hopes, Real Power: How the Arab Spring Fueled a Global Surveillance Boom

**原文标题**: Digital Hopes, Real Power: How the Arab Spring Fueled a Global Surveillance Boom

**原文链接**: [https://www.eff.org/deeplinks/2026/04/digital-hopes-real-power-how-arab-spring-fueled-global-surveillance-boom](https://www.eff.org/deeplinks/2026/04/digital-hopes-real-power-how-arab-spring-fueled-global-surveillance-boom)

生成摘要时出错

---

## 62. Struggle Against the Gods

**原文标题**: Struggle Against the Gods

**原文链接**: [https://firstthings.com/struggle-against-the-gods/](https://firstthings.com/struggle-against-the-gods/)

生成摘要时出错

---

## 63. A blind man made it possible for others with low vision to build Lego sets

**原文标题**: A blind man made it possible for others with low vision to build Lego sets

**原文链接**: [https://apnews.com/article/lego-bricks-for-blind-audio-braille-instructions-5a2a27de4354a0b1443171c3f24f29e4](https://apnews.com/article/lego-bricks-for-blind-audio-braille-instructions-5a2a27de4354a0b1443171c3f24f29e4)

生成摘要时出错

---

## 64. Every GPU That Mattered

**原文标题**: Every GPU That Mattered

**原文链接**: [https://sheets.works/data-viz/every-gpu](https://sheets.works/data-viz/every-gpu)

生成摘要时出错

---

## 65. Show HN: Brutalist Concrete Laptop Stand (2024)

**原文标题**: Show HN: Brutalist Concrete Laptop Stand (2024)

**原文链接**: [https://sam-burns.com/posts/concrete-laptop-stand/](https://sam-burns.com/posts/concrete-laptop-stand/)

生成摘要时出错

---

## 66. Greece to ban social media for under-15s from next year

**原文标题**: Greece to ban social media for under-15s from next year

**原文链接**: [https://www.bbc.com/news/articles/ckgx1x742x5o](https://www.bbc.com/news/articles/ckgx1x742x5o)

生成摘要时出错

---

## 67. A truck driver spent 20 years making a scale model of every building in NYC

**原文标题**: A truck driver spent 20 years making a scale model of every building in NYC

**原文链接**: [https://www.smithsonianmag.com/smart-news/a-truck-drive-spent-20-years-making-this-astonishing-scale-model-of-every-single-building-in-new-york-city-180988443/](https://www.smithsonianmag.com/smart-news/a-truck-drive-spent-20-years-making-this-astonishing-scale-model-of-every-single-building-in-new-york-city-180988443/)

生成摘要时出错

---

## 68. Acoustic Eavesdropping with Telecom Fiber Optic Cables

**原文标题**: Acoustic Eavesdropping with Telecom Fiber Optic Cables

**原文链接**: [https://www.ndss-symposium.org/ndss-paper/hiding-an-ear-in-plain-sight-on-the-practicality-and-implications-of-acoustic-eavesdropping-with-telecom-fiber-optic-cables/](https://www.ndss-symposium.org/ndss-paper/hiding-an-ear-in-plain-sight-on-the-practicality-and-implications-of-acoustic-eavesdropping-with-telecom-fiber-optic-cables/)

生成摘要时出错

---

## 69. Bitcoin and quantum computing

**原文标题**: Bitcoin and quantum computing

**原文链接**: [https://nehanarula.org/2026/04/03/bitcoin-and-quantum-computing.html](https://nehanarula.org/2026/04/03/bitcoin-and-quantum-computing.html)

生成摘要时出错

---

## 70. IPv6 is the only way forward

**原文标题**: IPv6 is the only way forward

**原文链接**: [https://ankshilp.in/posts/for-the-love-of-internet/](https://ankshilp.in/posts/for-the-love-of-internet/)

生成摘要时出错

---

## 71. AI helps add 10k more photos to OldNYC

**原文标题**: AI helps add 10k more photos to OldNYC

**原文链接**: [https://www.danvk.org/2026/03/08/oldnyc-updates.html](https://www.danvk.org/2026/03/08/oldnyc-updates.html)

生成摘要时出错

---

## 72. You can't cancel a JavaScript promise (except sometimes you can)

**原文标题**: You can't cancel a JavaScript promise (except sometimes you can)

**原文链接**: [https://www.inngest.com/blog/hanging-promises-for-control-flow](https://www.inngest.com/blog/hanging-promises-for-control-flow)

生成摘要时出错

---

## 73. Launch HN: Freestyle – Sandboxes for Coding Agents

**原文标题**: Launch HN: Freestyle – Sandboxes for Coding Agents

**原文链接**: [https://www.freestyle.sh/](https://www.freestyle.sh/)

生成摘要时出错

---

## 74. Cloudflare targets 2029 for full post-quantum security

**原文标题**: Cloudflare targets 2029 for full post-quantum security

**原文链接**: [https://blog.cloudflare.com/post-quantum-roadmap/](https://blog.cloudflare.com/post-quantum-roadmap/)

生成摘要时出错

---

## 75. John Coltrane illustrates the mathematics of jazz

**原文标题**: John Coltrane illustrates the mathematics of jazz

**原文链接**: [https://www.americanjazzmusicsociety.com/blog/john-coltrane-draws](https://www.americanjazzmusicsociety.com/blog/john-coltrane-draws)

生成摘要时出错

---

## 76. An Arctic Road Trip Brings Vital Underground Networks into View

**原文标题**: An Arctic Road Trip Brings Vital Underground Networks into View

**原文链接**: [https://www.quantamagazine.org/an-arctic-road-trip-brings-vital-underground-networks-into-view-20260406/](https://www.quantamagazine.org/an-arctic-road-trip-brings-vital-underground-networks-into-view-20260406/)

生成摘要时出错

---

## 77. US fired 1k JASSM cruise missiles in 37 days. Lockheed makes 396 per year

**原文标题**: US fired 1k JASSM cruise missiles in 37 days. Lockheed makes 396 per year

**原文链接**: [https://www.shatterbelt.co/articles/jassm-stockpile-crisis](https://www.shatterbelt.co/articles/jassm-stockpile-crisis)

生成摘要时出错

---

## 78. Reproducibility and robustness of economics and political science research

**原文标题**: Reproducibility and robustness of economics and political science research

**原文链接**: [https://www.nature.com/articles/s41586-026-10251-x](https://www.nature.com/articles/s41586-026-10251-x)

生成摘要时出错

---

## 79. Greece to ban under-15s from social media from next year

**原文标题**: Greece to ban under-15s from social media from next year

**原文链接**: [https://news.sky.com/story/greece-to-ban-under-15s-from-social-media-from-next-year-13529181](https://news.sky.com/story/greece-to-ban-under-15s-from-social-media-from-next-year-13529181)

生成摘要时出错

---

## 80. A New Jersey Teen Finds Treasure, and More, in Abandoned Storage Units

**原文标题**: A New Jersey Teen Finds Treasure, and More, in Abandoned Storage Units

**原文链接**: [https://www.nytimes.com/2026/03/31/style/new-jersey-teen-storage-units.html](https://www.nytimes.com/2026/03/31/style/new-jersey-teen-storage-units.html)

生成摘要时出错

---

## 81. Moving fast in hardware: lessons from lab to $100M ARR

**原文标题**: Moving fast in hardware: lessons from lab to $100M ARR

**原文链接**: [https://blog.zacka.io/p/simplify-then-add-lightness-bc4](https://blog.zacka.io/p/simplify-then-add-lightness-bc4)

生成摘要时出错

---

## 82. Teen Basketball Is for Pros

**原文标题**: Teen Basketball Is for Pros

**原文链接**: [https://www.cnn.com/2026/04/08/sport/high-school-basketball-nil-king-bacot-cec](https://www.cnn.com/2026/04/08/sport/high-school-basketball-nil-king-bacot-cec)

生成摘要时出错

---

## 83. Hacking Google Support: Leaking call logs and deanonymising agents

**原文标题**: Hacking Google Support: Leaking call logs and deanonymising agents

**原文链接**: [https://michaeldalton.au/posts/hacking-google-support](https://michaeldalton.au/posts/hacking-google-support)

生成摘要时出错

---

## 84. Amazon rewards loyal Kindle devotees by closing the book on old e-readers

**原文标题**: Amazon rewards loyal Kindle devotees by closing the book on old e-readers

**原文链接**: [https://www.theregister.com/2026/04/08/amazon_kindle_support_discontinued/](https://www.theregister.com/2026/04/08/amazon_kindle_support_discontinued/)

生成摘要时出错

---

## 85. Identify a London Underground Line just by listening to it

**原文标题**: Identify a London Underground Line just by listening to it

**原文链接**: [https://tubesoundquiz.com/](https://tubesoundquiz.com/)

生成摘要时出错

---

## 86. Assessing Claude Mythos Preview's cybersecurity capabilities

**原文标题**: Assessing Claude Mythos Preview's cybersecurity capabilities

**原文链接**: [https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/)

生成摘要时出错

---

## 87. Taste in the age of AI and LLMs

**原文标题**: Taste in the age of AI and LLMs

**原文链接**: [https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/](https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/)

生成摘要时出错

---

## 88. Rescuing old printers with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文标题**: Rescuing old printers with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文链接**: [https://printervention.app/details](https://printervention.app/details)

生成摘要时出错

---

## 89. SQLite in Production: Lessons from Running a Store on a Single File

**原文标题**: SQLite in Production: Lessons from Running a Store on a Single File

**原文链接**: [https://ultrathink.art/blog/sqlite-in-production-lessons](https://ultrathink.art/blog/sqlite-in-production-lessons)

生成摘要时出错

---

## 90. Peptides: where to begin?

**原文标题**: Peptides: where to begin?

**原文链接**: [https://www.science.org/content/blog-post/ah-peptides-where-begin](https://www.science.org/content/blog-post/ah-peptides-where-begin)

生成摘要时出错

---

## 91. I've sold out

**原文标题**: I've sold out

**原文链接**: [https://mariozechner.at/posts/2026-04-08-ive-sold-out/](https://mariozechner.at/posts/2026-04-08-ive-sold-out/)

生成摘要时出错

---

## 92. Dropping Cloudflare for Bunny.net

**原文标题**: Dropping Cloudflare for Bunny.net

**原文链接**: [https://jola.dev/posts/dropping-cloudflare](https://jola.dev/posts/dropping-cloudflare)

生成摘要时出错

---

## 93. Move Detroit

**原文标题**: Move Detroit

**原文链接**: [https://www.movedetroit.com/program](https://www.movedetroit.com/program)

生成摘要时出错

---

## 94. Running out of disk space in production

**原文标题**: Running out of disk space in production

**原文链接**: [https://alt-romes.github.io/posts/2026-04-01-running-out-of-disk-space-on-launch.html](https://alt-romes.github.io/posts/2026-04-01-running-out-of-disk-space-on-launch.html)

生成摘要时出错

---

## 95. Open Models have crossed a threshold

**原文标题**: Open Models have crossed a threshold

**原文链接**: [https://blog.langchain.com/open-models-have-crossed-a-threshold/](https://blog.langchain.com/open-models-have-crossed-a-threshold/)

生成摘要时出错

---

## 96. Blackholing My Email

**原文标题**: Blackholing My Email

**原文链接**: [https://www.johnsto.co.uk/blog/blackholing-my-email/](https://www.johnsto.co.uk/blog/blackholing-my-email/)

生成摘要时出错

---

## 97. Show HN: Voxcode: local speech to text and ripgrep = transcript and code context

**原文标题**: Show HN: Voxcode: local speech to text and ripgrep = transcript and code context

**原文链接**: [https://github.com/jensneuse/voxcode](https://github.com/jensneuse/voxcode)

生成摘要时出错

---

## 98. We found an undocumented bug in the Apollo 11 guidance computer code

**原文标题**: We found an undocumented bug in the Apollo 11 guidance computer code

**原文链接**: [https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/](https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/)

生成摘要时出错

---

## 99. 12k Tons of Dumped Orange Peel Grew into a Landscape Nobody Expected (2017)

**原文标题**: 12k Tons of Dumped Orange Peel Grew into a Landscape Nobody Expected (2017)

**原文链接**: [https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined](https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined)

生成摘要时出错

---

## 100. Solod – A subset of Go that translates to C

**原文标题**: Solod – A subset of Go that translates to C

**原文链接**: [https://github.com/solod-dev/solod](https://github.com/solod-dev/solod)

生成摘要时出错

---

