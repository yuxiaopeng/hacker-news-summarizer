# Hacker News 热门文章摘要 (2026-03-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 微软“不可破解”的 Xbox One 已被“Bliss”破解

**原文标题**: Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

**原文链接**: [https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)

在被认为“不可破解”十多年后，微软的 Xbox One 终于被攻破了。一名代号为“Bliss”的安全研究员成功绕过了该主机的复杂安全层，实现了在系统各个层面运行未签名代码。

该漏洞利用了一种名为**电压故障注入（voltage glitching）**的硬件技术。通过精确控制主机电源供应的波动时间，研究人员成功干扰了 AMD 平台安全处理器（PSP）在启动过程中的安全检查。这一漏洞提供了对系统硬件的深度访问权限，使得运行自制软件、定制操作系统以及进行以往无法实现的深度技术修改成为可能。

这一突破具有重要意义，因为 2013 年发布的 Xbox One 采用了复杂的“虚拟机管理程序（hypervisor）”和安全启动链，其保持不被破解的时间远超其前代产品 Xbox 360 以及同世代对手 PlayStation 4。

“Bliss”漏洞利用适用于初代 Xbox One 以及 Xbox One S 和 Xbox One X 机型。由于这是一个硬件层面的漏洞，微软很难通过标准的软件更新对现有设备进行修补。虽然该过程目前需要专业的硬件知识和物理改装——这意味着面向普通大众的简易“越狱”方案尚未问世——但它标志着主机黑客社区的一个历史性里程碑，并终结了 Xbox One 长期以来坚不可摧的神话。

---

## 2. Kagi 小众网络

**原文标题**: Kagi Small Web

**原文链接**: [https://kagi.com/smallweb/](https://kagi.com/smallweb/)

**Kagi Small Web** 是由 Kagi 搜索引擎发起的一项倡议，旨在复兴并挖掘“独立网络”。它旨在为日益被 SEO 驱动的内容、侵入性广告和 AI 生成的噪音所主导的现代互联网提供一种替代选择。通过专注于非商业性、以人为本的网站，该项目将用户与个人博客、匠心网站和分众社区连接起来，而这些内容在传统的搜索结果中往往被深埋。

该项目包含三个主要组件：

1.  **Small Web Feed：** 一个精选的实时信息流，汇集了来自高质量个人博客和独立创作者的最新动态。
2.  **Small Web Index：** 一个专门的搜索引擎，仅抓取小型独立域名，让用户在不受商业干扰的情况下发现独特的观点。
3.  **Teacup：** 一个轻量级的集成 RSS 阅读器，帮助用户在纯净、无干扰的环境下关注他们喜爱的独立声音。

其核心理念是通过优先考虑人类的创造力而非算法优化，来对抗互联网的“糟糕化”（enshittification）。Kagi Small Web 鼓励回归“旧互联网”精神——即一个由个人表达、爱好者热情和真实知识共享所定义的数字空间。通过提供这些工具，Kagi 旨在支持独立创作者，并为用户提供一种更有意义、更少商业气息的浏览体验。

---

## 3. Node.js 需要一个虚拟文件系统

**原文标题**: Node.js needs a virtual file system

**原文链接**: [https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system](https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system)

生成摘要时出错

---

## 4. 迈向未经审核 AI 生成代码的自动化验证

**原文标题**: Toward automated verification of unreviewed AI-generated code

**原文链接**: [https://peterlavigne.com/writing/verifying-ai-generated-code](https://peterlavigne.com/writing/verifying-ai-generated-code)

本文提出了关于 AI 生成代码视角的转变：从人工**审查**（逐行阅读代码）转向自动化**验证**（使用机器强制约束来确认正确性）。作者认为，如果 AI 生成的代码满足一系列严格的自动化检查，就可以在无需人工审查的情况下投入生产环境。

作者概述了验证的四个关键约束：
1. **基于属性的测试 (Property-based testing)：** 使用 Hypothesis 等工具测试广泛的半随机输入，确保满足需求且不产生异常。
2. **变异测试 (Mutation testing)：** 使用 *mutmut* 等工具修改代码并确保测试失败。这能将代码限制在必要的逻辑内，防止模型包含冗余代码或通过硬编码测试数据来“作弊”。
3. **副作用预防：** 确保代码不会产生意外后果。
4. **静态分析：** 强制执行类型检查和代码扫描。

一个核心主题是，我们应该将未经审查的 AI 输出视为**编译后的代码**。在这种范式下，人类可读性和可维护性变得次要，代码是否能持续通过其验证套件才是关键。

虽然作者承认，目前设置这些约束的开销与人工审查所花费的时间不相上下，但他们认为这为未来的自动化奠定了基础。通过这些测试缩小“解空间”，无效代码通过的可能性被降至极低，从而可能实现一种“软件工厂”模式，即智能体在无需人工干预的情况下生产出可交付使用的代码。

---

## 5. FFmpeg 8.1

**原文标题**: FFmpeg 8.1

**原文链接**: [https://ffmpeg.org/index.html#pr8.1](https://ffmpeg.org/index.html#pr8.1)

本文记录了 FFmpeg 从 2023 年初到 2026 年初，通过一系列重大和次要版本（版本 6.0 至 8.1）的演进历程。这些更新突显了其在现代化、性能优化和扩展编解码支持方面的重要阶段。

**技术进步**
这些版本的一个主要焦点是集成基于 Vulkan 计算的编解码器和硬件加速。这一转变实现了跨平台、厂商通用的解码/编码流水线，支持包括 H.264、HEVC、AV1、FFv1 和 ProRes 在内的格式。此外，FFmpeg 成功引入并稳定了原生 VVC（多功能视频编码）解码器，并增加了对 xHE-AAC、IAMF（沉浸式音频）和 MV-HEVC（立体编码）的支持。

**性能与基础设施**
该软件进行了多次内部重构以提高效率：
*   **CLI 改进：** `ffmpeg` 命令行工具针对多线程进行了重构，允许解复用器、解码器和过滤器并行运行。
*   **架构：** 7.0 版本迁移至符合 C11 标准的编译器并移除了过时的 API，而 6.0 版本确立了新的年度重大版本发布计划。
*   **优化：** 项目使用更快的 `libavutil/tx` 替换了原有的 FFT/MDCT 实现，并引入了大量的 RISC-V 汇编优化。
*   **数据完整性：** 完成了修复颜色范围协商的大量工作，确保全范围图像在过滤器和编码器中得到正确处理。

**社区与安全**
根据 Coverity 静态分析，FFmpeg 达到了历史最低的缺陷密度，这得益于德国主权科技基金（Sovereign Tech Fund）的资助，该基金于 2024 年成为该项目的首个政府赞助商。项目还通过在 `code.ffmpeg.org` 启动新的托管平台，实现了贡献工作流的现代化。

这些更新共同巩固了 FFmpeg 作为多媒体处理行业标准、跨平台解决方案的地位，在采用尖端硬件 API 与严格内部维护之间取得了平衡。

---

## 6. 发现 Xbox 360 中的 CPU 设计缺陷 (2018)

**原文标题**: Finding a CPU Design Bug in the Xbox 360 (2018)

**原文链接**: [https://randomascii.wordpress.com/2018/01/07/finding-a-cpu-design-bug-in-the-xbox-360/](https://randomascii.wordpress.com/2018/01/07/finding-a-cpu-design-bug-in-the-xbox-360/)

在这篇文章中，前 Xbox 360 CPU 专家 Bruce Dawson 讲述了一个涉及名为 `xdcbt` 的自定义 PowerPC 指令的严重硬件设计缺陷的发现过程。

`xdcbt` 旨在缓解高内存延迟和仅有 1MB 的二级缓存（L2 cache）带来的限制，它是一种“扩展预取”指令，能将数据直接从主内存加载到核心的一级缓存（L1 cache）中，完全绕过二级缓存。虽然这提升了速度，但却破坏了硬件的 MESI 内存一致性协议。由于二级缓存负责跟踪哪些核心持有特定数据，绕过它意味着多个核心最终可能对同一块内存产生冲突且不一致的视图。

最初，Dawson 发现他的内存复制例程导致了堆损坏，因为该例程预取的数据略微超出了缓冲区边界，导致 `xdcbt` 抓取了相邻的元数据，而其他核心当时正在同步修改这些数据。然而，“真正”的漏洞更为隐蔽，且与现代的 **Meltdown（熔断）和 Spectre（幽灵）** 漏洞具有相同的根源：**推测执行**。

即使在开发人员停止显式调用该指令后，Xbox 360 的分支预测器仍会根据预测的代码路径推测性地执行 `xdcbt`。由于 CPU 为了降低延迟会立即启动内存总线事务，并且一旦开始就无法取消，因此错误的分支预测仍会触发破坏缓存的预取操作。

Dawson 通过将所有 `xdcbt` 实例替换为断点验证了这一点。尽管断点从未被触发（证明指令从未被“正式”执行），但崩溃消失了。这证实了即使程序流在技术上从未到达这些指令，它们仍会导致硬件层面的故障。最终，由于分支预测器的不可预测性导致该指令无法受控，它被认为过于危险而无法使用。

---

## 7. 《秘密特工》：探索充满活力却又暴力的巴西 (2025)

**原文标题**: 'The Secret Agent': Exploring a Vibrant, yet Violent Brazil (2025)

**原文链接**: [https://theasc.com/articles/the-secret-agent-cinematography](https://theasc.com/articles/the-secret-agent-cinematography)

《秘密特工》是巴西选送角逐2025年奥斯卡最佳国际影片奖的作品。这是一部以1977年巴西军事独裁末期为背景的政治惊悚片。该片由克莱伯·门多萨·菲略执导，艾夫根尼亚·亚历山德罗娃（AFC）担任摄影指导，讲述了持不同政见者兼技术专家马塞洛（瓦格纳·莫拉饰）在狂欢节周期间，于累西腓四处潜逃的故事。

亚历山德罗娃的摄影手法刻意将影片阴郁、节奏缓慢的主题与充满活力且高饱和度的视觉色调形成对比。她力求捕捉巴西内在的矛盾——即快乐与音乐同苦难与暴力的交织。为了营造出一种富有质感且“不完美”的视觉效果，她选用了阿莱（Arri）Alexa 35摄影机搭配潘那维申（Panavision）B系列经典变形镜头，从而呈现出独特的光晕和像差。在后期制作中，亚历山德罗娃强调色彩分离，摒弃了怀旧的棕褐色调，转而选择在阴影中加入偏红的底色，以还原那个时代巴西摄影的美学风格。

文中重点介绍了两个主要片段：
1. **开场加油站场景：** 一个高景深的长时间审讯镜头，在恶劣天气下拍摄了两周之久。亚历山德罗娃利用12K Dino灯和精密的调色确保了视觉效果的连贯性。
2. **狂欢节序列：** 在观看完电影《凶兆》后，马塞洛加入了一场街头庆典。这一复杂场景动用了庞大的灯光装置（包括SkyPanel和气球灯）来模拟20世纪70年代的街灯。舞者抛撒的面粉营造了独特的质感，象征着一场“死亡之舞”。

最终，影片的技术选择将一段恐怖的政治时代植根于华丽、喜庆的氛围之中，体现了巴西文化在动荡历史中依然保有的“对生命的庆颂”。

---

## 8. Spice Data (YC S19) Is Hiring a Product Specialist

**原文标题**: Spice Data (YC S19) Is Hiring a Product Specialist

**原文链接**: [https://www.ycombinator.com/companies/spice-data/jobs/P0e9MKz-product-specialist-new-grad](https://www.ycombinator.com/companies/spice-data/jobs/P0e9MKz-product-specialist-new-grad)

**Spice Data**, a Y Combinator-backed (S19) startup based in San Francisco, is seeking a **Product Specialist** for a full-time, entry-level role. The company licenses high-quality, cleaned data to Fortune 500 enterprises, with a current focus on the restaurant industry.

**Role and Responsibilities**
The Product Specialist will act as the final quality checkpoint between the data pipeline and customers. Key tasks include:
*   Cleaning raw data and maintaining data mappings.
*   Performing basic data analysis using tools like Excel.
*   Managing third-party contractors involved in data collection.
*   Investigating data inconsistencies and taking initiative in ambiguous situations.

**Candidate Requirements**
The role is open to new graduates and requires a highly organized, detail-oriented individual with strong investigative instincts and clear communication skills. While a technical background is a plus, it is not required. The position is strictly **on-site** in downtown San Francisco five days a week and is open only to US citizens or visa holders.

**Compensation and Benefits**
*   **Salary:** $80,000 – $100,000.
*   **Equity:** 0.1% – 0.5%.
*   **Benefits:** Platinum PPO health insurance, 401k, unlimited PTO, and daily office lunch.

**About the Company**
Founded in 2019, Spice Data is a small, profitable, and lean team with minimal equity dilution. The interview process consists of a 15-minute intro call, two 30-minute skill-based interviews focusing on data cleaning and problem-solving, and a final onsite visit.

---

## 9. Show HN: Antfly: Distributed, Multimodal Search and Memory and Graphs in Go

**原文标题**: Show HN: Antfly: Distributed, Multimodal Search and Memory and Graphs in Go

**原文链接**: [https://github.com/antflydb/antfly](https://github.com/antflydb/antfly)

生成摘要时出错

---

## 10. OpenSUSE Kalpa

**原文标题**: OpenSUSE Kalpa

**原文链接**: [https://kalpadesktop.org/](https://kalpadesktop.org/)

生成摘要时出错

---

## 11. Show HN: March Madness Bracket Challenge for AI Agents Only

**原文标题**: Show HN: March Madness Bracket Challenge for AI Agents Only

**原文链接**: [https://www.Bracketmadness.ai](https://www.Bracketmadness.ai)

生成摘要时出错

---

## 12. Show HN: Crust – A CLI framework for TypeScript and Bun

**原文标题**: Show HN: Crust – A CLI framework for TypeScript and Bun

**原文链接**: [https://github.com/chenxin-yan/crust](https://github.com/chenxin-yan/crust)

生成摘要时出错

---

## 13. Give Django your time and money, not your tokens

**原文标题**: Give Django your time and money, not your tokens

**原文链接**: [https://www.better-simple.com/django/2026/03/16/give-django-your-time-and-money/](https://www.better-simple.com/django/2026/03/16/give-django-your-time-and-money/)

生成摘要时出错

---

## 14. Building a Shell

**原文标题**: Building a Shell

**原文链接**: [https://healeycodes.com/building-a-shell](https://healeycodes.com/building-a-shell)

生成摘要时出错

---

## 15. Efficient sparse computations using linear algebra aware compilers (2025)

**原文标题**: Efficient sparse computations using linear algebra aware compilers (2025)

**原文链接**: [https://www.osti.gov/biblio/3013883](https://www.osti.gov/biblio/3013883)

生成摘要时出错

---

## 16. Leanstral: Open-source agent for trustworthy coding and formal proof engineering

**原文标题**: Leanstral: Open-source agent for trustworthy coding and formal proof engineering

**原文链接**: [https://mistral.ai/news/leanstral](https://mistral.ai/news/leanstral)

生成摘要时出错

---

## 17. Font Smuggler – Copy hidden brand fonts into Google Docs

**原文标题**: Font Smuggler – Copy hidden brand fonts into Google Docs

**原文链接**: [https://brianmoore.com/fontsmuggler/](https://brianmoore.com/fontsmuggler/)

生成摘要时出错

---

## 18. Heart, Head, Life, Fate

**原文标题**: Heart, Head, Life, Fate

**原文链接**: [https://www.lrb.co.uk/the-paper/v48/n05/steven-shapin/heart-head-life-fate](https://www.lrb.co.uk/the-paper/v48/n05/steven-shapin/heart-head-life-fate)

生成摘要时出错

---

## 19. GPT‑5.4 Mini and Nano

**原文标题**: GPT‑5.4 Mini and Nano

**原文链接**: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano)

生成摘要时出错

---

## 20. The unlikely story of Teardown Multiplayer

**原文标题**: The unlikely story of Teardown Multiplayer

**原文链接**: [https://blog.voxagon.se/2026/03/13/teardown-multiplayer.html](https://blog.voxagon.se/2026/03/13/teardown-multiplayer.html)

生成摘要时出错

---

## 21. Reverse-engineering Viktor and making it Open Source

**原文标题**: Reverse-engineering Viktor and making it Open Source

**原文链接**: [https://matijacniacki.com/blog/openviktor](https://matijacniacki.com/blog/openviktor)

生成摘要时出错

---

## 22. Kagi Translate now supports LinkedIn Speak as an output language

**原文标题**: Kagi Translate now supports LinkedIn Speak as an output language

**原文链接**: [https://translate.kagi.com/?from=en&to=LinkedIn+speak](https://translate.kagi.com/?from=en&to=LinkedIn+speak)

生成摘要时出错

---

## 23. What I Learned When I Started a Design Studio (2011)

**原文标题**: What I Learned When I Started a Design Studio (2011)

**原文链接**: [https://www.subtraction.com/2011/12/12/when-i-started-a-design-studio/](https://www.subtraction.com/2011/12/12/when-i-started-a-design-studio/)

生成摘要时出错

---

## 24. Sci-Fi Short Film “There Is No Antimemetics Division” [video]

**原文标题**: Sci-Fi Short Film “There Is No Antimemetics Division” [video]

**原文链接**: [https://www.youtube.com/watch?v=3v8AsTHfAG0](https://www.youtube.com/watch?v=3v8AsTHfAG0)

生成摘要时出错

---

## 25. The American Healthcare Conundrum

**原文标题**: The American Healthcare Conundrum

**原文链接**: [https://github.com/rexrodeo/american-healthcare-conundrum](https://github.com/rexrodeo/american-healthcare-conundrum)

生成摘要时出错

---

## 26. Meta’s renewed commitment to jemalloc

**原文标题**: Meta’s renewed commitment to jemalloc

**原文链接**: [https://engineering.fb.com/2026/03/02/data-infrastructure/investing-in-infrastructure-metas-renewed-commitment-to-jemalloc/](https://engineering.fb.com/2026/03/02/data-infrastructure/investing-in-infrastructure-metas-renewed-commitment-to-jemalloc/)

生成摘要时出错

---

## 27. The “small web” is bigger than you might think

**原文标题**: The “small web” is bigger than you might think

**原文链接**: [https://kevinboone.me/small_web_is_big.html](https://kevinboone.me/small_web_is_big.html)

生成摘要时出错

---

## 28. Gummy Geometry

**原文标题**: Gummy Geometry

**原文链接**: [https://newkrok.github.io/nape-js/examples.html?open=soft-body&mode=3d&outline=0](https://newkrok.github.io/nape-js/examples.html?open=soft-body&mode=3d&outline=0)

生成摘要时出错

---

## 29. A proposal to classify happiness as a psychiatric disorder (1992)

**原文标题**: A proposal to classify happiness as a psychiatric disorder (1992)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC1376114/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1376114/)

生成摘要时出错

---

## 30. Every layer of review makes you 10x slower

**原文标题**: Every layer of review makes you 10x slower

**原文链接**: [https://apenwarr.ca/log/20260316](https://apenwarr.ca/log/20260316)

生成摘要时出错

---

## 31. Backblaze Pricing and Product Updates

**原文标题**: Backblaze Pricing and Product Updates

**原文链接**: [https://www.backblaze.com/blog/backblaze-pricing-and-product-updates/](https://www.backblaze.com/blog/backblaze-pricing-and-product-updates/)

生成摘要时出错

---

## 32. Pyodide: a Python distribution based on WebAssembly

**原文标题**: Pyodide: a Python distribution based on WebAssembly

**原文链接**: [https://github.com/pyodide/pyodide](https://github.com/pyodide/pyodide)

生成摘要时出错

---

## 33. Why I love FreeBSD

**原文标题**: Why I love FreeBSD

**原文链接**: [https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/](https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/)

生成摘要时出错

---

## 34. Beyond has dropped “meat” from its name and expanded its high-protein drink line

**原文标题**: Beyond has dropped “meat” from its name and expanded its high-protein drink line

**原文链接**: [https://plantbasednews.org/news/alternative-protein/beyond-meat-not-the-moment-rebrand/](https://plantbasednews.org/news/alternative-protein/beyond-meat-not-the-moment-rebrand/)

生成摘要时出错

---

## 35. US SEC preparing to scrap quarterly reporting requirement

**原文标题**: US SEC preparing to scrap quarterly reporting requirement

**原文链接**: [https://www.reuters.com/business/finance/us-sec-preparing-eliminate-quarterly-reporting-requirement-wsj-says-2026-03-16/](https://www.reuters.com/business/finance/us-sec-preparing-eliminate-quarterly-reporting-requirement-wsj-says-2026-03-16/)

生成摘要时出错

---

## 36. My Journey to a reliable and enjoyable locally hosted voice assistant (2025)

**原文标题**: My Journey to a reliable and enjoyable locally hosted voice assistant (2025)

**原文链接**: [https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860](https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860)

生成摘要时出错

---

## 37. Gitana 18: the new flying Ultim trimaran

**原文标题**: Gitana 18: the new flying Ultim trimaran

**原文链接**: [https://www.boatnews.com/story/50717/gitana-18-radical-technical-choices-for-the-new-flying-ultim-trimaran](https://www.boatnews.com/story/50717/gitana-18-radical-technical-choices-for-the-new-flying-ultim-trimaran)

生成摘要时出错

---

## 38. Show HN: Oxyde – Pydantic-native async ORM with a Rust core

**原文标题**: Show HN: Oxyde – Pydantic-native async ORM with a Rust core

**原文链接**: [https://github.com/mr-fatalyst/oxyde](https://github.com/mr-fatalyst/oxyde)

生成摘要时出错

---

## 39. Starlink Mini as a failover

**原文标题**: Starlink Mini as a failover

**原文链接**: [https://www.jackpearce.co.uk/posts/starlink-failover/](https://www.jackpearce.co.uk/posts/starlink-failover/)

生成摘要时出错

---

## 40. National Academies of Sciences says no to demands it remove climate info

**原文标题**: National Academies of Sciences says no to demands it remove climate info

**原文链接**: [https://arstechnica.com/science/2026/03/national-academies-of-sciences-resisting-pressure-to-pull-climate-info/](https://arstechnica.com/science/2026/03/national-academies-of-sciences-resisting-pressure-to-pull-climate-info/)

生成摘要时出错

---

## 41. Show HN: Claude Code skills that build complete Godot games

**原文标题**: Show HN: Claude Code skills that build complete Godot games

**原文链接**: [https://github.com/htdt/godogen](https://github.com/htdt/godogen)

生成摘要时出错

---

## 42. Claude Tips for 3D Work

**原文标题**: Claude Tips for 3D Work

**原文链接**: [https://www.davesnider.com/posts/claude-3d](https://www.davesnider.com/posts/claude-3d)

生成摘要时出错

---

## 43. Ryugu asteroid samples contain all DNA and RNA building blocks

**原文标题**: Ryugu asteroid samples contain all DNA and RNA building blocks

**原文链接**: [https://phys.org/news/2026-03-ryugu-asteroid-samples-dna-rna.html](https://phys.org/news/2026-03-ryugu-asteroid-samples-dna-rna.html)

生成摘要时出错

---

## 44. AirPods Max 2

**原文标题**: AirPods Max 2

**原文链接**: [https://www.apple.com/airpods-max/](https://www.apple.com/airpods-max/)

生成摘要时出错

---

## 45. Fatal Core Dump Game

**原文标题**: Fatal Core Dump Game

**原文链接**: [https://www.robopenguins.com/core-dump-game/](https://www.robopenguins.com/core-dump-game/)

生成摘要时出错

---

## 46. Polymarket gamblers threaten to kill me over Iran missile story

**原文标题**: Polymarket gamblers threaten to kill me over Iran missile story

**原文链接**: [https://www.timesofisrael.com/gamblers-trying-to-win-a-bet-on-polymarket-are-vowing-to-kill-me-if-i-dont-rewrite-an-iran-missile-story/](https://www.timesofisrael.com/gamblers-trying-to-win-a-bet-on-polymarket-are-vowing-to-kill-me-if-i-dont-rewrite-an-iran-missile-story/)

生成摘要时出错

---

## 47. In space, no one can hear you kernel panic (2020)

**原文标题**: In space, no one can hear you kernel panic (2020)

**原文链接**: [https://increment.com/software-architecture/in-space-no-one-can-hear-you-kernel-panic/](https://increment.com/software-architecture/in-space-no-one-can-hear-you-kernel-panic/)

生成摘要时出错

---

## 48. Show HN: Thermal Receipt Printers – Markdown and Web UI

**原文标题**: Show HN: Thermal Receipt Printers – Markdown and Web UI

**原文链接**: [https://github.com/sadreck/ThermalMarky](https://github.com/sadreck/ThermalMarky)

生成摘要时出错

---

## 49. Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)

**原文标题**: Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)

**原文链接**: [https://arxiv.org/abs/2511.04427](https://arxiv.org/abs/2511.04427)

生成摘要时出错

---

## 50. Boot ROM Security on Silicon Macs (M1/M2/M3)

**原文标题**: Boot ROM Security on Silicon Macs (M1/M2/M3)

**原文链接**: [https://oliviagallucci.com/boot-rom-security-on-silicon-macs-m1-m2-m3/](https://oliviagallucci.com/boot-rom-security-on-silicon-macs-m1-m2-m3/)

生成摘要时出错

---

## 51. Lazycut: A simple terminal video trimmer using FFmpeg

**原文标题**: Lazycut: A simple terminal video trimmer using FFmpeg

**原文链接**: [https://github.com/emin-ozata/lazycut](https://github.com/emin-ozata/lazycut)

生成摘要时出错

---

## 52. The bureaucracy blocking the chance at a cure

**原文标题**: The bureaucracy blocking the chance at a cure

**原文链接**: [https://www.writingruxandrabio.com/p/the-bureaucracy-blocking-the-chance](https://www.writingruxandrabio.com/p/the-bureaucracy-blocking-the-chance)

生成摘要时出错

---

## 53. Corruption erodes social trust more in democracies than in autocracies

**原文标题**: Corruption erodes social trust more in democracies than in autocracies

**原文链接**: [https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full](https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full)

生成摘要时出错

---

## 54. Grace Hopper's Revenge

**原文标题**: Grace Hopper's Revenge

**原文链接**: [https://www.thefuriousopposites.com/p/grace-hoppers-revenge](https://www.thefuriousopposites.com/p/grace-hoppers-revenge)

生成摘要时出错

---

## 55. Language model teams as distributed systems

**原文标题**: Language model teams as distributed systems

**原文链接**: [https://arxiv.org/abs/2603.12229](https://arxiv.org/abs/2603.12229)

生成摘要时出错

---

## 56. Monkey Island for Commodore 64 Ground Up

**原文标题**: Monkey Island for Commodore 64 Ground Up

**原文链接**: [https://pixeldust.se/monkey-island-project](https://pixeldust.se/monkey-island-project)

生成摘要时出错

---

## 57. Bill C-22, the Lawful Access Act: Dangerous backdoor surveillance risks remain

**原文标题**: Bill C-22, the Lawful Access Act: Dangerous backdoor surveillance risks remain

**原文链接**: [https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/)

生成摘要时出错

---

## 58. Apideck CLI – An AI-agent interface with much lower context consumption than MCP

**原文标题**: Apideck CLI – An AI-agent interface with much lower context consumption than MCP

**原文链接**: [https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

生成摘要时出错

---

## 59. Cert Authorities Check for DNSSEC from Today

**原文标题**: Cert Authorities Check for DNSSEC from Today

**原文链接**: [https://www.grepular.com/Cert_Authorities_Check_for_DNSSEC_From_Today](https://www.grepular.com/Cert_Authorities_Check_for_DNSSEC_From_Today)

生成摘要时出错

---

## 60. The Functional Programming Hiring Problem

**原文标题**: The Functional Programming Hiring Problem

**原文链接**: [https://blog.janissary.xyz/posts/hiring-functional-programming](https://blog.janissary.xyz/posts/hiring-functional-programming)

生成摘要时出错

---

## 61. MoD sources warn Palantir role at heart of government is threat to UK security

**原文标题**: MoD sources warn Palantir role at heart of government is threat to UK security

**原文链接**: [https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets](https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets)

生成摘要时出错

---

## 62. Comparing Python Type Checkers: Typing Spec Conformance

**原文标题**: Comparing Python Type Checkers: Typing Spec Conformance

**原文链接**: [https://pyrefly.org/blog/typing-conformance-comparison/](https://pyrefly.org/blog/typing-conformance-comparison/)

生成摘要时出错

---

## 63. We Study Mass Shooters. Something Terrifying Is Happening Online

**原文标题**: We Study Mass Shooters. Something Terrifying Is Happening Online

**原文链接**: [https://www.nytimes.com/2026/03/17/opinion/mass-shooters-online-radicalization.html](https://www.nytimes.com/2026/03/17/opinion/mass-shooters-online-radicalization.html)

生成摘要时出错

---

## 64. Java 26 Release Notes

**原文标题**: Java 26 Release Notes

**原文链接**: [https://jdk.java.net/26/release-notes](https://jdk.java.net/26/release-notes)

生成摘要时出错

---

## 65. Show HN: Droeftoeter, a Terminal Coding Toy

**原文标题**: Show HN: Droeftoeter, a Terminal Coding Toy

**原文链接**: [https://github.com/whtspc/droeftoeter](https://github.com/whtspc/droeftoeter)

生成摘要时出错

---

## 66. Jepsen: MariaDB Galera Cluster 12.1.2

**原文标题**: Jepsen: MariaDB Galera Cluster 12.1.2

**原文链接**: [https://jepsen.io/analyses/mariadb-galera-cluster-12.1.2](https://jepsen.io/analyses/mariadb-galera-cluster-12.1.2)

生成摘要时出错

---

## 67. US Job Market Visualizer

**原文标题**: US Job Market Visualizer

**原文链接**: [https://karpathy.ai/jobs/](https://karpathy.ai/jobs/)

生成摘要时出错

---

## 68. The Linux Programming Interface as a university course text

**原文标题**: The Linux Programming Interface as a university course text

**原文链接**: [https://man7.org/tlpi/academic/index.html](https://man7.org/tlpi/academic/index.html)

生成摘要时出错

---

## 69. Even faster asin() was staring right at me

**原文标题**: Even faster asin() was staring right at me

**原文链接**: [https://16bpp.net/blog/post/even-faster-asin-was-staring-right-at-me/](https://16bpp.net/blog/post/even-faster-asin-was-staring-right-at-me/)

生成摘要时出错

---

## 70. The emergence of print-on-demand Amazon paperback books

**原文标题**: The emergence of print-on-demand Amazon paperback books

**原文链接**: [https://www.alexerhardt.com/en/enshittification-amazon-paperback-books/](https://www.alexerhardt.com/en/enshittification-amazon-paperback-books/)

生成摘要时出错

---

## 71. MM120, a pharmaceutical form of LSD, shown to reduce anxiety symptoms (2025)

**原文标题**: MM120, a pharmaceutical form of LSD, shown to reduce anxiety symptoms (2025)

**原文链接**: [https://www.sciencedaily.com/releases/2025/10/251027023816.htm](https://www.sciencedaily.com/releases/2025/10/251027023816.htm)

生成摘要时出错

---

## 72. Six ingenious ways how Canon DSLRs used to illuminate their autofocus points

**原文标题**: Six ingenious ways how Canon DSLRs used to illuminate their autofocus points

**原文链接**: [https://exclusivearchitecture.com/03-technical-articles-CSDS-00-table-of-contents.html](https://exclusivearchitecture.com/03-technical-articles-CSDS-00-table-of-contents.html)

生成摘要时出错

---

## 73. Arizona Attorney General sues Kalshi on illegal gambling charges

**原文标题**: Arizona Attorney General sues Kalshi on illegal gambling charges

**原文链接**: [https://www.engadget.com/big-tech/arizona-attorney-general-sues-kalshi-on-illegal-gambling-charges-172006290.html](https://www.engadget.com/big-tech/arizona-attorney-general-sues-kalshi-on-illegal-gambling-charges-172006290.html)

生成摘要时出错

---

## 74. The 49MB web page

**原文标题**: The 49MB web page

**原文链接**: [https://thatshubham.com/blog/news-audit](https://thatshubham.com/blog/news-audit)

生成摘要时出错

---

## 75. How I write software with LLMs

**原文标题**: How I write software with LLMs

**原文链接**: [https://www.stavros.io/posts/how-i-write-software-with-llms/](https://www.stavros.io/posts/how-i-write-software-with-llms/)

生成摘要时出错

---

## 76. We rebuilt the Shockwave engine in Rust and WASM to save early 2000s web games

**原文标题**: We rebuilt the Shockwave engine in Rust and WASM to save early 2000s web games

**原文链接**: [https://old.reddit.com/r/rust/comments/1ro81bt/we_rebuilt_the_shockwave_engine_in_rust_wasm_to/](https://old.reddit.com/r/rust/comments/1ro81bt/we_rebuilt_the_shockwave_engine_in_rust_wasm_to/)

生成摘要时出错

---

## 77. Show HN: M68k assembly emulator that runs in the browser

**原文标题**: Show HN: M68k assembly emulator that runs in the browser

**原文链接**: [https://github.com/gianlucarea/m68k-interpreter](https://github.com/gianlucarea/m68k-interpreter)

生成摘要时出错

---

## 78. Why I may ‘hire’ AI instead of a graduate student

**原文标题**: Why I may ‘hire’ AI instead of a graduate student

**原文链接**: [https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)

生成摘要时出错

---

## 79. Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

**原文标题**: Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

**原文链接**: [https://www.moment.dev/blog/lies-i-was-told-pt-2](https://www.moment.dev/blog/lies-i-was-told-pt-2)

生成摘要时出错

---

## 80. High income improves evaluation of life but not emotional well-being

**原文标题**: High income improves evaluation of life but not emotional well-being

**原文链接**: [https://www.pnas.org/doi/full/10.1073/pnas.1011492107](https://www.pnas.org/doi/full/10.1073/pnas.1011492107)

生成摘要时出错

---

## 81. Qwen3.5-397B at 4.74 tok/s using 5.9GB RAM

**原文标题**: Qwen3.5-397B at 4.74 tok/s using 5.9GB RAM

**原文链接**: [https://xcancel.com/danveloper/status/2033940538563445236](https://xcancel.com/danveloper/status/2033940538563445236)

生成摘要时出错

---

## 82. Video Shows How Globes Were Made by Hand in 1955. End of a 500-Year Tradition

**原文标题**: Video Shows How Globes Were Made by Hand in 1955. End of a 500-Year Tradition

**原文链接**: [https://www.openculture.com/2026/03/how-globes-were-made-by-hand-in-1955.html](https://www.openculture.com/2026/03/how-globes-were-made-by-hand-in-1955.html)

生成摘要时出错

---

## 83. Nvidia Launches Vera CPU, Purpose-Built for Agentic AI

**原文标题**: Nvidia Launches Vera CPU, Purpose-Built for Agentic AI

**原文链接**: [https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

生成摘要时出错

---

## 84. The unwritten laws of software engineering

**原文标题**: The unwritten laws of software engineering

**原文链接**: [https://newsletter.manager.dev/p/the-unwritten-laws-of-software-engineering](https://newsletter.manager.dev/p/the-unwritten-laws-of-software-engineering)

生成摘要时出错

---

## 85. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://human-organ-atlas.esrf.fr/](https://human-organ-atlas.esrf.fr/)

生成摘要时出错

---

## 86. Samsung to Stop Selling $2,899 TriFold Phone After Three Months

**原文标题**: Samsung to Stop Selling $2,899 TriFold Phone After Three Months

**原文链接**: [https://www.bloomberg.com/news/articles/2026-03-17/samsung-to-stop-selling-2-899-trifold-phone-after-three-months](https://www.bloomberg.com/news/articles/2026-03-17/samsung-to-stop-selling-2-899-trifold-phone-after-three-months)

生成摘要时出错

---

## 87. Chrome DevTools MCP (2025)

**原文标题**: Chrome DevTools MCP (2025)

**原文链接**: [https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session)

生成摘要时出错

---

## 88. Stop Sloppypasta

**原文标题**: Stop Sloppypasta

**原文链接**: [https://stopsloppypasta.ai/](https://stopsloppypasta.ai/)

生成摘要时出错

---

## 89. PayPal ends Google Wallet integration

**原文标题**: PayPal ends Google Wallet integration

**原文链接**: [https://www.heise.de/en/news/PayPal-ends-Google-Wallet-integration-11213293.html](https://www.heise.de/en/news/PayPal-ends-Google-Wallet-integration-11213293.html)

生成摘要时出错

---

## 90. Launch HN: Chamber (YC W26) – An AI Teammate for GPU Infrastructure

**原文标题**: Launch HN: Chamber (YC W26) – An AI Teammate for GPU Infrastructure

**原文链接**: [https://www.usechamber.io/](https://www.usechamber.io/)

生成摘要时出错

---

## 91. Bringing Semiconductors to Kazakhstan

**原文标题**: Bringing Semiconductors to Kazakhstan

**原文链接**: [https://www.siliconimist.com/p/bringing-semiconductors-to-kazakhstan](https://www.siliconimist.com/p/bringing-semiconductors-to-kazakhstan)

生成摘要时出错

---

## 92. Mistral Small 4

**原文标题**: Mistral Small 4

**原文链接**: [https://mistral.ai/news/mistral-small-4](https://mistral.ai/news/mistral-small-4)

生成摘要时出错

---

## 93. 'Pokémon Go' players unknowingly trained delivery robots with 30B images

**原文标题**: 'Pokémon Go' players unknowingly trained delivery robots with 30B images

**原文链接**: [https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/)

生成摘要时出错

---

## 94. My Self-Driving Car Crash – The Tesla was driving perfectly–until it wasn't

**原文标题**: My Self-Driving Car Crash – The Tesla was driving perfectly–until it wasn't

**原文链接**: [https://www.theatlantic.com/magazine/2026/04/self-driving-car-technology-tesla-crash/686054/](https://www.theatlantic.com/magazine/2026/04/self-driving-car-technology-tesla-crash/686054/)

生成摘要时出错

---

## 95. Event Publisher enables event integration between Keycloak and OpenFGA

**原文标题**: Event Publisher enables event integration between Keycloak and OpenFGA

**原文链接**: [https://github.com/embesozzi/keycloak-openfga-event-publisher](https://github.com/embesozzi/keycloak-openfga-event-publisher)

生成摘要时出错

---

## 96. LLM Architecture Gallery

**原文标题**: LLM Architecture Gallery

**原文链接**: [https://sebastianraschka.com/llm-architecture-gallery/](https://sebastianraschka.com/llm-architecture-gallery/)

生成摘要时出错

---

## 97. Show HN: Hecate – Call an AI from Signal

**原文标题**: Show HN: Hecate – Call an AI from Signal

**原文链接**: [https://github.com/rhodey/hecate](https://github.com/rhodey/hecate)

生成摘要时出错

---

## 98. NASA's Curiosity Rover Sees Martian 'Spiderwebs' Up Close

**原文标题**: NASA's Curiosity Rover Sees Martian 'Spiderwebs' Up Close

**原文链接**: [https://www.nasa.gov/missions/mars-science-laboratory/curiosity-rover/nasas-curiosity-rover-sees-martian-spiderwebs-up-close/](https://www.nasa.gov/missions/mars-science-laboratory/curiosity-rover/nasas-curiosity-rover-sees-martian-spiderwebs-up-close/)

生成摘要时出错

---

## 99. End of "Chat Control": Paving the Way for Genuine Child Protection

**原文标题**: End of "Chat Control": Paving the Way for Genuine Child Protection

**原文链接**: [https://www.patrick-breyer.de/en/end-of-chat-control-paving-the-way-for-genuine-child-protection/](https://www.patrick-breyer.de/en/end-of-chat-control-paving-the-way-for-genuine-child-protection/)

生成摘要时出错

---

## 100. Show HN: Hackerbrief – Top posts on Hacker News summarized daily

**原文标题**: Show HN: Hackerbrief – Top posts on Hacker News summarized daily

**原文链接**: [https://hackerbrief.vercel.app/](https://hackerbrief.vercel.app/)

生成摘要时出错

---

