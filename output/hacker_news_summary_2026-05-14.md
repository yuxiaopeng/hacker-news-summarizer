# Hacker News 热门文章摘要 (2026-05-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 拆除我的2024款RAV4混动版上的调制解调器和GPS

**原文标题**: Removing the modem and GPS from my 2024 rav4 hybrid

**原文链接**: [https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/)

本文提供了针对 2024 款丰田 RAV4 混动版物理禁用追踪与遥测功能的全面指南。作者认为，现代车辆已成为侵入性的监控工具，收集大量个人数据——包括驾驶习惯、位置历史甚至生物识别信息——并将其出售给数据经纪商和保险公司。

为从源头上停止此类数据收集，作者详细介绍了如何拆除数据通信模块（DCM，即调制解调器）和内置 GPS 天线。

**关键信息与技术考量：**
*   **功能权衡：** 移除 DCM 将禁用 OTA 远程更新、云服务和紧急救援（SOS）功能。
*   **麦克风修复：** 由于车内麦克风线路经过 DCM，作者使用“DCM 绕过套件”来维持免提通话功能。
*   **断开 GPS：** 物理断开 GPS 是为了防止一个常见故障，即在使用 CarPlay 时，车辆内部位置数据会与手机导航发生冲突并将其覆盖。
*   **蓝牙隐私泄露：** 作者警告说，即使没有调制解调器，车辆也可能尝试通过蓝牙连接驾驶员的手机来“回传数据”。为防止这种情况，建议使用 USB 有线连接或专门的蓝牙转 USB 适配器。
*   **保修：** 虽然特定的车载信息系统保修可能会失效，但作者指出，《马格努森-莫斯保修法》保护车主，防止整车保修因不相关的机械问题而被取消。

作者总结道，尽管此过程需要大规模拆卸仪表盘，但对于在“车轮上的计算机”时代寻求绝对隐私的人来说，这是必要的一步。

---

## 2. RTX 5090 与 M4 MacBook Air：能玩游戏吗？

**原文标题**: RTX 5090 and M4 MacBook Air: Can It Game?

**原文链接**: [https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

本文详细介绍了一项技术实验：通过 Thunderbolt eGPU 显卡坞将 NVIDIA RTX 5090 桌面显卡连接到 M4 MacBook Air。由于 macOS 缺乏针对 Apple Silicon 的原生 NVIDIA 驱动程序，作者通过在 macOS 主机上运行 ARM64 Linux 虚拟机（VM）并实现 PCI 直通（PCI passthrough）绕过了这一限制。

该项目解决了几个重大的工程难题：

*   **PCI BAR 映射：** 最初尝试映射显卡的内存寄存器（BAR）时导致了主机内核崩溃（kernel panic）。作者发现，在 QEMU 中将该内存映射为“可执行”状态触发了崩溃；解决方案是应用代码补丁，确保设备内存仅保持读/写属性。
*   **DMA 与 DART：** 苹果的 IOMMU（即 DART）存在严格限制，包括 1.5GB 的映射上限且无法控制内存对齐。为了绕过这一限制，作者开发了一个名为 `apple-dma-pci` 的自定义 Linux 内核模块，用于处理虚拟机与主机硬件之间的内存转换以及 NVIDIA 特有的对齐问题。
*   **性能瓶颈：** 受限于 macOS 处理设备内存的方式，该配置无法利用“写合并”（write-combining）。这导致 BAR 写入速度比原生性能慢约 10 倍，但仍明显快于拦截（trapping）每次访问的方案。

尽管存在这些限制，该方案依然可行。作者成功运行了《赛博朋克 2077》、《古墓丽影：暗影》和《地平线：零之曙光》等高负载游戏，以及 Qwen 和 Gemma 等 AI 推理模型。该项目作为一个精妙的概念验证，证明了虽然 Apple Silicon 并非为外接 NVIDIA 硬件而设计，但通过创新的虚拟化技术和自定义驱动工程，可以弥合两者间的鸿沟，以支持高端游戏和 AI 工作负载。

---

## 3. Nginx 最新漏洞利用

**原文标题**: New Nginx Exploit

**原文链接**: [https://github.com/DepthFirstDisclosures/Nginx-Rift](https://github.com/DepthFirstDisclosures/Nginx-Rift)

生成摘要时出错

---

## 4. 该死的 AI 让我变笨了。

**原文标题**: God Damn AI is making me dumb

**原文链接**: [https://jpain.io/god-damn-ai-is-making-me-dumb/](https://jpain.io/god-damn-ai-is-making-me-dumb/)

在《该死的 AI 正在让我变笨》一文中，作者反思了过度依赖人工智能如何侵蚀其专业技能和自信。尽管身为一名软件开发人员，作者坦言在连续两年完全依赖 AI 提示词工作后，自己已基本忘记了如何手动编写代码。这种技能的丧失导致了一种沮丧感，促使作者下定决心重新学习手动编程。

文章重点描述了一场心理层面的挣扎，指出 AI 利用了用户的自我怀疑和“冒名顶替综合征”。虽然 AI 工具带来了便利，但作者认为 AI 生成的内容往往缺乏灵魂，无法体现其独特的个人风格，且经常偏离原意。甚至在不借助辅助撰写本文时，作者依然感到一种强烈的、条件反射般的冲动，想要通过 AI 验证来确保文字“通顺合理”。

从宏观角度，作者探讨了 AI 对软件行业的影响。文中引用了罗伯特·马丁（Uncle Bob）的观点，认为 AI 虽然可能减少对开发者的整体需求，但也有潜力让“专业精神”重回该领域。通过将编程这项技艺重新交还给一小部分专家——正如当年开创该领域的物理学家和数学家那样——AI 或许能扭转过去几十年因需求激增而导致的质量下滑趋势。

归根结底，这篇文章是一份个人行动宣言，号召人们抵制自动化捷径的诱惑，重新夺回个人的自主权、工匠精神和智力独立。

---

## 5. 硬盘固件破解

**原文标题**: HDD Firmware Hacking

**原文链接**: [https://icode4.coffee/?p=1465](https://icode4.coffee/?p=1465)

Ryan Miceli 的文章《HDD 固件破解 第一部分》详细介绍了作者在修改硬盘驱动器 (HDD) 和固态驱动器 (SSD) 固件方面的研究。该项目源于利用 Xbox 360 竞态条件的需要；作者意图修改驱动器固件，在特定扇区读取期间引入时间延迟，从而为触发漏洞提供更大的窗口。

作者概述了针对 Western Digital (WD) 和三星驱动器等多个测试对象的系统化方法：
1. **获取固件：** 通过专业修复工具 (PC-3000)、HDD Guru 等专业论坛，以及从制造商网站上的 OEM 固件更新程序中提取镜像来收集数据。
2. **逆向工程与分析：**
    * **Western Digital：** 作者发现其固件使用了 LZHUF 压缩算法的修改版本。通过在 IDA Pro 中逆向加载程序存根，他们调整了压缩常量，成功解压并分析了完整的固件镜像。
    * **三星 PM871a SSD：** 利用联想的固件更新程序，作者逆向了一种用于保护固件的位操作混淆算法。他们通过将内存地址与 ARM Cortex-M3 内存映射对齐，进一步识别了段头。
    * **三星 HM020GI：** 该驱动器带来了更大的挑战，其似乎使用了字反转数据和未知的指令集架构 (ISA)，作者将其推迟到后续文章中讨论。

最终，尽管作者找到了在不需要修改固件的情况下利用 Xbox 360 的替代方法，但该研究展示了如何利用 OEM 更新程序和逆向工程来绕过固件保护，并为自定义补丁准备驱动器。文章最后将 Western Digital 驱动器作为深度分析的主要成功案例进行了总结。

---

## 6. 加拿大计算机爱好者运动

**原文标题**: Computer Hobby Movement in Canada

**原文链接**: [https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada](https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada)

“加拿大计算机爱好者运动”记录了计算机从专业工业工具向家用必需品转变的十年历程（1976–1985年）。这一转型的核心是由哈罗德·梅兰森（Harold Melanson）于1976年1月创立的**多伦多地区计算机爱好者协会（TRACE）**。

这场运动根植于长达一个世纪的无线电和电子爱好者传统，并受到20世纪70年代微处理器问世的催化。虽然受到美国里程碑事件（如家用电脑俱乐部和Altair 8800）的影响，但加拿大的这场运动保持了独特的身份特征。TRACE成员最初关注本地硬件，特别是国际微系统有限公司（MIL）生产的 **MOD-8 和 MOD-80** 微型计算机。此外，TRACE 的独特之处还在于其对 **APL** 语言的深度参与，这是一种由加拿大人肯尼斯·艾弗森（Kenneth Iverson）构思的编程语言。

随着时间的推移，该运动的参与群体发生了变化，从最初的计算机专业人士扩大到包括新手和学生。这些爱好者通过加拿大科技公司的“后门”渠道获取“规格外”零件，以此应对组件昂贵等挑战。文中提到的重要里程碑包括霍华德·富兰克林（Howard Franklin）于1974年自制的计算机，以及总部位于多伦多的 **MCM/70**——这被认为是第一台专为个人使用而设计的、由微处理器驱动的便携式计算机。

尽管随着个人电脑市场的标准化和商业化，正式的爱好者运动到20世纪80年代末已难以维持其影响力，但其遗产影响深远。它成功弥合了专业电子技术与社会之间的鸿沟，培养了包容性文化，并使个人计算成为了加拿大人的现实。

---

## 7. MIT: 20% drop in incoming graduate students

**原文标题**: MIT: 20% drop in incoming graduate students

**原文链接**: [https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline](https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline)

In a May 2026 address, MIT President Sally Kornbluth detailed a significant crisis facing the Institute regarding funding and its talent pipeline. 

**Financial Challenges**
MIT is grappling with a heavy 8% tax on endowment returns and a sharp decline in federal support. Despite some restored Congressional appropriations, federal research activity at MIT has dropped by more than 20%, and new federal awards have seen a similar decline. Total sponsored research is down 10%. This is attributed to a slow flow of federal funds and a shift in government policy that may prioritize geography over scientific merit when allocating grants.

**The Talent Pipeline**
These financial uncertainties, combined with restrictive policy changes affecting international scholars, have forced departments to be cautious with admissions. Consequently, incoming graduate student enrollment (excluding the Sloan School and EECS MEng) has dropped by nearly 20%—representing roughly 500 fewer students. President Kornbluth warned that this decline threatens MIT’s research momentum, reduces mentorship for undergraduates, and ultimately "chokes off" the nation’s supply of future scientific solutions.

**Response and Mitigation**
To navigate these challenges, MIT is implementing several strategies:
*   **Aggressive Grant Pursuit:** Faculty recently submitted 176 proposals for the Department of Energy’s Genesis Mission.
*   **Industry Partnerships:** Strengthening ties with the private sector, such as the newly launched MIT-IBM Computing Research Lab.
*   **New Revenue Streams:** Exploring masters-only programs and revitalizing philanthropic efforts through Resource Development.
*   **Advocacy:** Working with policymakers in Washington to oppose the endowment tax and emphasize the importance of curiosity-driven research.

While describing the outlook as "chilly," Kornbluth expressed confidence in the community’s resilience and creativity in sustaining MIT’s mission during this difficult period.

---

## 8. Fossils show millipede and centipede ancestors evolved legs underwater

**原文标题**: Fossils show millipede and centipede ancestors evolved legs underwater

**原文链接**: [https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html](https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html)

生成摘要时出错

---

## 9. Understanding the Linux Kernel: The Linux Kernel Startup

**原文标题**: Understanding the Linux Kernel: The Linux Kernel Startup

**原文链接**: [https://internals-for-interns.com/posts/linux-kernel-startup/](https://internals-for-interns.com/posts/linux-kernel-startup/)

生成摘要时出错

---

## 10. Terranox AI (YC W26) Is Hiring a Founding AI/ML Engineer and Summer AI/ML Intern

**原文标题**: Terranox AI (YC W26) Is Hiring a Founding AI/ML Engineer and Summer AI/ML Intern

**原文链接**: [https://www.workatastartup.com/companies/terranox-ai](https://www.workatastartup.com/companies/terranox-ai)

生成摘要时出错

---

## 11. Int a = 5; a = a++ + ++a; a =? (2011)

**原文标题**: Int a = 5; a = a++ + ++a; a =? (2011)

**原文链接**: [https://gynvael.coldwind.pl/?id=372](https://gynvael.coldwind.pl/?id=372)

生成摘要时出错

---

## 12. First public macOS kernel memory corruption exploit on Apple M5

**原文标题**: First public macOS kernel memory corruption exploit on Apple M5

**原文链接**: [https://blog.calif.io/p/first-public-kernel-memory-corruption](https://blog.calif.io/p/first-public-kernel-memory-corruption)

生成摘要时出错

---

## 13. On The Conflation of Money and Things

**原文标题**: On The Conflation of Money and Things

**原文链接**: [https://lithub.com/is-it-even-real-on-the-conflation-of-money-and-things/](https://lithub.com/is-it-even-real-on-the-conflation-of-money-and-things/)

生成摘要时出错

---

## 14. Claude AI recovers an 11 yrs old BTC wallet holding 400k USD

**原文标题**: Claude AI recovers an 11 yrs old BTC wallet holding 400k USD

**原文链接**: [https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup](https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup)

生成摘要时出错

---

## 15. The Power of a Free Popsicle (2018)

**原文标题**: The Power of a Free Popsicle (2018)

**原文链接**: [https://www.gsb.stanford.edu/insights/power-free-popsicle](https://www.gsb.stanford.edu/insights/power-free-popsicle)

生成摘要时出错

---

## 16. Claude for Small Business

**原文标题**: Claude for Small Business

**原文链接**: [https://www.anthropic.com/news/claude-for-small-business](https://www.anthropic.com/news/claude-for-small-business)

生成摘要时出错

---

## 17. EditLens: Quantifying the extent of AI editing in text (2025)

**原文标题**: EditLens: Quantifying the extent of AI editing in text (2025)

**原文链接**: [https://arxiv.org/abs/2510.03154](https://arxiv.org/abs/2510.03154)

生成摘要时出错

---

## 18. 60fps Video on a CGA? – The GlyphBlaster

**原文标题**: 60fps Video on a CGA? – The GlyphBlaster

**原文链接**: [https://martypc.blogspot.com/2026/05/60fps-video-on-cga-glyphblaster.html](https://martypc.blogspot.com/2026/05/60fps-video-on-cga-glyphblaster.html)

生成摘要时出错

---

## 19. You Don't Align an AI, You Align with It

**原文标题**: You Don't Align an AI, You Align with It

**原文链接**: [https://danieltan.weblog.lol/2026/05/you-dont-align-an-ai-you-align-with-it](https://danieltan.weblog.lol/2026/05/you-dont-align-an-ai-you-align-with-it)

生成摘要时出错

---

## 20. Show HN: Running the second public ODoH relay

**原文标题**: Show HN: Running the second public ODoH relay

**原文链接**: [https://numa.rs/blog/posts/odoh-anonymous-dns-without-an-account.html](https://numa.rs/blog/posts/odoh-anonymous-dns-without-an-account.html)

生成摘要时出错

---

## 21. Andreessen Horowitz Is Spending on Politics Like No Other

**原文标题**: Andreessen Horowitz Is Spending on Politics Like No Other

**原文链接**: [https://www.nytimes.com/2026/05/13/technology/andreessen-horowitz-politics.html](https://www.nytimes.com/2026/05/13/technology/andreessen-horowitz-politics.html)

生成摘要时出错

---

## 22. What's in a GGUF, besides the weights – and what's still missing?

**原文标题**: What's in a GGUF, besides the weights – and what's still missing?

**原文链接**: [https://nobodywho.ooo/posts/whats-in-a-gguf/](https://nobodywho.ooo/posts/whats-in-a-gguf/)

生成摘要时出错

---

## 23. Anthropic forms $200M partnership with the Gates Foundation

**原文标题**: Anthropic forms $200M partnership with the Gates Foundation

**原文链接**: [https://www.anthropic.com/news/gates-foundation-partnership](https://www.anthropic.com/news/gates-foundation-partnership)

生成摘要时出错

---

## 24. Scorched Earth 2000 – Web

**原文标题**: Scorched Earth 2000 – Web

**原文链接**: [http://www.scorch2000.com/web/](http://www.scorch2000.com/web/)

生成摘要时出错

---

## 25. Myths about /dev/urandom (2014)

**原文标题**: Myths about /dev/urandom (2014)

**原文链接**: [https://www.2uo.de/myths-about-urandom/](https://www.2uo.de/myths-about-urandom/)

生成摘要时出错

---

## 26. Apple-OpenAI Relationship Frays, Setting Up Possible Legal Fight

**原文标题**: Apple-OpenAI Relationship Frays, Setting Up Possible Legal Fight

**原文链接**: [https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight](https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight)

生成摘要时出错

---

## 27. The Tree House: A voyage to the source of a backyard dream

**原文标题**: The Tree House: A voyage to the source of a backyard dream

**原文链接**: [https://www.laphamsquarterly.org/roundtable/tree-house](https://www.laphamsquarterly.org/roundtable/tree-house)

生成摘要时出错

---

## 28. Leaving the Physical World

**原文标题**: Leaving the Physical World

**原文链接**: [https://www.eff.org/pages/leaving-physical-world](https://www.eff.org/pages/leaving-physical-world)

生成摘要时出错

---

## 29. Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO

**原文标题**: Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO

**原文链接**: [https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d](https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d)

生成摘要时出错

---

## 30. USDA Projects Smallest US Wheat Harvest Since 1972 Due to Plains Drought

**原文标题**: USDA Projects Smallest US Wheat Harvest Since 1972 Due to Plains Drought

**原文链接**: [https://www.agweb.com/news/usda-projects-smallest-us-wheat-harvest-1972-due-plains-drought](https://www.agweb.com/news/usda-projects-smallest-us-wheat-harvest-1972-due-plains-drought)

生成摘要时出错

---

## 31. A Claude Code and Codex Skill for Deliberate Skill Development

**原文标题**: A Claude Code and Codex Skill for Deliberate Skill Development

**原文链接**: [https://github.com/DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)

生成摘要时出错

---

## 32. Grok Build

**原文标题**: Grok Build

**原文链接**: [https://x.ai/news/grok-build-cli](https://x.ai/news/grok-build-cli)

生成摘要时出错

---

## 33. Bun's Rust rewrite has been merged

**原文标题**: Bun's Rust rewrite has been merged

**原文链接**: [https://old.reddit.com/r/rust/comments/1tcrmjs/rewrite_bun_in_rust_has_been_merged/](https://old.reddit.com/r/rust/comments/1tcrmjs/rewrite_bun_in_rust_has_been_merged/)

生成摘要时出错

---

## 34. Saying Goodbye to one line of APL

**原文标题**: Saying Goodbye to one line of APL

**原文链接**: [https://homewithinnowhere.com/posts/2026-05-10-one-line.html#fnref1](https://homewithinnowhere.com/posts/2026-05-10-one-line.html#fnref1)

生成摘要时出错

---

## 35. Deal reached with hackers to delete data stolen from the Canvas platform

**原文标题**: Deal reached with hackers to delete data stolen from the Canvas platform

**原文链接**: [https://www.nbcnews.com/tech/tech-news/deal-reached-hackers-delete-data-stolen-canvas-educational-platform-rcna344693](https://www.nbcnews.com/tech/tech-news/deal-reached-hackers-delete-data-stolen-canvas-educational-platform-rcna344693)

生成摘要时出错

---

## 36. The Emacsification of Software

**原文标题**: The Emacsification of Software

**原文链接**: [https://sockpuppet.org/blog/2026/05/12/emacsification/](https://sockpuppet.org/blog/2026/05/12/emacsification/)

生成摘要时出错

---

## 37. MacBook Neo Deep Dive: Benchmarks, Wafer Economics, and the 8GB Gamble

**原文标题**: MacBook Neo Deep Dive: Benchmarks, Wafer Economics, and the 8GB Gamble

**原文链接**: [https://www.jdhodges.com/blog/macbook-neo-benchmarks-analysis/](https://www.jdhodges.com/blog/macbook-neo-benchmarks-analysis/)

生成摘要时出错

---

## 38. Pipes, Forks, and Zombies

**原文标题**: Pipes, Forks, and Zombies

**原文链接**: [https://cs61.seas.harvard.edu/wiki/2017/Shell3/](https://cs61.seas.harvard.edu/wiki/2017/Shell3/)

生成摘要时出错

---

## 39. Linux gaming is faster because Windows APIs are becoming Linux kernel features

**原文标题**: Linux gaming is faster because Windows APIs are becoming Linux kernel features

**原文链接**: [https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/](https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/)

生成摘要时出错

---

## 40. Swift bricks to be installed on all new buildings in Scotland

**原文标题**: Swift bricks to be installed on all new buildings in Scotland

**原文链接**: [https://www.theguardian.com/environment/2026/jan/28/swift-bricks-to-be-installed-in-all-new-buildings-in-scotland-after-holyrood-backs-ruling](https://www.theguardian.com/environment/2026/jan/28/swift-bricks-to-be-installed-in-all-new-buildings-in-scotland-after-holyrood-backs-ruling)

生成摘要时出错

---

## 41. Chess puzzle I found in my dad's old book

**原文标题**: Chess puzzle I found in my dad's old book

**原文链接**: [https://ardoedo.it/kempelen/](https://ardoedo.it/kempelen/)

生成摘要时出错

---

## 42. Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文标题**: Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文链接**: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

生成摘要时出错

---

## 43. A field manual for Deutsche Bahn

**原文标题**: A field manual for Deutsche Bahn

**原文链接**: [https://blog.hofstede.it/a-field-manual-for-three-years-on-deutsche-bahn/](https://blog.hofstede.it/a-field-manual-for-three-years-on-deutsche-bahn/)

生成摘要时出错

---

## 44. Avoiding and reducing microplastic false positives from dry glove contact

**原文标题**: Avoiding and reducing microplastic false positives from dry glove contact

**原文链接**: [https://pubs.rsc.org/en/content/articlelanding/2026/ay/d5ay01801c](https://pubs.rsc.org/en/content/articlelanding/2026/ay/d5ay01801c)

生成摘要时出错

---

## 45. Observation: Communication changes when both sides use AI

**原文标题**: Observation: Communication changes when both sides use AI

**原文链接**: [https://ownyourwords.co/](https://ownyourwords.co/)

生成摘要时出错

---

## 46. Show HN: Nibble

**原文标题**: Show HN: Nibble

**原文链接**: [https://github.com/glouw/nibble](https://github.com/glouw/nibble)

生成摘要时出错

---

## 47. Texas county pauses data center construction in rural areas

**原文标题**: Texas county pauses data center construction in rural areas

**原文链接**: [https://www.texastribune.org/2026/05/12/texas-hill-county-approves-data-center-construction-pause-ai/](https://www.texastribune.org/2026/05/12/texas-hill-county-approves-data-center-construction-pause-ai/)

生成摘要时出错

---

## 48. Technical Dimensions of Live Feedback in Programming Systems

**原文标题**: Technical Dimensions of Live Feedback in Programming Systems

**原文链接**: [https://joshuahhh.com/dims-of-feedback/](https://joshuahhh.com/dims-of-feedback/)

生成摘要时出错

---

## 49. Show HN: Browse 61 3D Printable Robots

**原文标题**: Show HN: Browse 61 3D Printable Robots

**原文链接**: [https://orobot.io/](https://orobot.io/)

生成摘要时出错

---

## 50. How can Apple deal with the memory shortage?

**原文标题**: How can Apple deal with the memory shortage?

**原文链接**: [https://asymco.com/2026/05/11/the-great-memory-panic-of-2026/](https://asymco.com/2026/05/11/the-great-memory-panic-of-2026/)

生成摘要时出错

---

## 51. Heritability of human life span is ~50% when heritability is redefined

**原文标题**: Heritability of human life span is ~50% when heritability is redefined

**原文链接**: [https://dynomight.net/lifespan/](https://dynomight.net/lifespan/)

生成摘要时出错

---

## 52. Parents don't want their kids to use tech at school., districts pushing back

**原文标题**: Parents don't want their kids to use tech at school., districts pushing back

**原文链接**: [https://apnews.com/article/edtech-philly-classroom-technology-computer-phone-screens-6aab2bac1d66df1863509b5d5c74fe12](https://apnews.com/article/edtech-philly-classroom-technology-computer-phone-screens-6aab2bac1d66df1863509b5d5c74fe12)

生成摘要时出错

---

## 53. Healthcare software company owner convicted of $1B Medicare fraud conspiracy

**原文标题**: Healthcare software company owner convicted of $1B Medicare fraud conspiracy

**原文链接**: [https://www.justice.gov/opa/pr/owner-health-care-software-company-convicted-1-billion-dollar-medicare-fraud-conspiracy](https://www.justice.gov/opa/pr/owner-health-care-software-company-convicted-1-billion-dollar-medicare-fraud-conspiracy)

生成摘要时出错

---

## 54. ChatGPT Gave Me Chilling Advice–As I Simulated Planning a Mass Shooting

**原文标题**: ChatGPT Gave Me Chilling Advice–As I Simulated Planning a Mass Shooting

**原文链接**: [https://www.motherjones.com/media/2026/05/openai-chatgpt-mass-shooting-guardrails-fail/](https://www.motherjones.com/media/2026/05/openai-chatgpt-mass-shooting-guardrails-fail/)

生成摘要时出错

---

## 55. Launch HN: Ardent (YC P26) – Postgres sandboxes in seconds with zero migration

**原文标题**: Launch HN: Ardent (YC P26) – Postgres sandboxes in seconds with zero migration

**原文链接**: [https://www.tryardent.com/](https://www.tryardent.com/)

生成摘要时出错

---

## 56. Cisco workforce reductions

**原文标题**: Cisco workforce reductions

**原文链接**: [https://blogs.cisco.com/news/our-path-forward](https://blogs.cisco.com/news/our-path-forward)

生成摘要时出错

---

## 57. Setting up a free *.city.state.us locality domain (2025)

**原文标题**: Setting up a free *.city.state.us locality domain (2025)

**原文链接**: [https://fredchan.org/blog/locality-domains-guide/](https://fredchan.org/blog/locality-domains-guide/)

生成摘要时出错

---

## 58. Extraordinary Ordinals

**原文标题**: Extraordinary Ordinals

**原文链接**: [https://text.marvinborner.de/2026-04-09-17.html](https://text.marvinborner.de/2026-04-09-17.html)

生成摘要时出错

---

## 59. Princeton mandates proctoring for in-person exams, upending 133 year precedent

**原文标题**: Princeton mandates proctoring for in-person exams, upending 133 year precedent

**原文链接**: [https://www.dailyprincetonian.com/article/2026/05/princeton-news-adpol-proctoring-in-person-examinations-passed-faculty-133-years-precedent](https://www.dailyprincetonian.com/article/2026/05/princeton-news-adpol-proctoring-in-person-examinations-passed-faculty-133-years-precedent)

生成摘要时出错

---

## 60. Employment Ice Age

**原文标题**: Employment Ice Age

**原文链接**: [https://en.wikipedia.org/wiki/Employment_Ice_Age](https://en.wikipedia.org/wiki/Employment_Ice_Age)

生成摘要时出错

---

## 61. Golden Testing a CAD Library

**原文标题**: Golden Testing a CAD Library

**原文链接**: [https://doscienceto.it/blog/posts/2026-04-27-golden-testing-cad.html](https://doscienceto.it/blog/posts/2026-04-27-golden-testing-cad.html)

生成摘要时出错

---

## 62. Meta won't let you block its AI account on Threads

**原文标题**: Meta won't let you block its AI account on Threads

**原文链接**: [https://www.theverge.com/tech/929091/meta-ai-threads-account-block](https://www.theverge.com/tech/929091/meta-ai-threads-account-block)

生成摘要时出错

---

## 63. AI-aided code migration: Google got 6x faster migration from TensorFlow to Jax

**原文标题**: AI-aided code migration: Google got 6x faster migration from TensorFlow to Jax

**原文链接**: [https://cloud.google.com/blog/topics/developers-practitioners/6x-faster-migration-from-tensorflow-to-jax](https://cloud.google.com/blog/topics/developers-practitioners/6x-faster-migration-from-tensorflow-to-jax)

生成摘要时出错

---

## 64. New stainless steel can survive conditions for hydrogen production in seawater

**原文标题**: New stainless steel can survive conditions for hydrogen production in seawater

**原文链接**: [https://www.sciencedaily.com/releases/2026/05/260510030950.htm](https://www.sciencedaily.com/releases/2026/05/260510030950.htm)

生成摘要时出错

---

## 65. The Tarot Card Deck Created by Salvador Dalí

**原文标题**: The Tarot Card Deck Created by Salvador Dalí

**原文链接**: [https://www.openculture.com/2026/05/salvador-dali-tarot-card-deck.html](https://www.openculture.com/2026/05/salvador-dali-tarot-card-deck.html)

生成摘要时出错

---

## 66. Web Server on a Nintendo Wii

**原文标题**: Web Server on a Nintendo Wii

**原文链接**: [http://wii.sjmulder.nl/](http://wii.sjmulder.nl/)

生成摘要时出错

---

## 67. Browsers Treat Big Sites Differently

**原文标题**: Browsers Treat Big Sites Differently

**原文链接**: [https://denodell.com/blog/browsers-treat-big-sites-differently](https://denodell.com/blog/browsers-treat-big-sites-differently)

生成摘要时出错

---

## 68. Traceway: MIT-licensed observability stack you can self-host in ~90s

**原文标题**: Traceway: MIT-licensed observability stack you can self-host in ~90s

**原文链接**: [https://github.com/tracewayapp/traceway](https://github.com/tracewayapp/traceway)

生成摘要时出错

---

## 69. Xs of Y – roguelike that names itself every run. Written in 4kLoC

**原文标题**: Xs of Y – roguelike that names itself every run. Written in 4kLoC

**原文链接**: [https://github.com/nooga/xsofy](https://github.com/nooga/xsofy)

生成摘要时出错

---

## 70. Reverting the incremental GC in Python 3.14 and 3.15

**原文标题**: Reverting the incremental GC in Python 3.14 and 3.15

**原文链接**: [https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014](https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014)

生成摘要时出错

---

## 71. Exploring 8 Shaft Weaving

**原文标题**: Exploring 8 Shaft Weaving

**原文链接**: [https://algorithmicpattern.org/2026/03/11/exploring-8-shaft-weaving/](https://algorithmicpattern.org/2026/03/11/exploring-8-shaft-weaving/)

生成摘要时出错

---

## 72. Twin brothers wipe 96 government databases minutes after being fired

**原文标题**: Twin brothers wipe 96 government databases minutes after being fired

**原文链接**: [https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/)

生成摘要时出错

---

## 73. Why senior developers fail to communicate their expertise

**原文标题**: Why senior developers fail to communicate their expertise

**原文链接**: [https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise)

生成摘要时出错

---

## 74. Mystery Microsoft bug leaker keeps the zero-days coming

**原文标题**: Mystery Microsoft bug leaker keeps the zero-days coming

**原文链接**: [https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)

生成摘要时出错

---

## 75. My graduation cap runs Rust

**原文标题**: My graduation cap runs Rust

**原文链接**: [https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/](https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/)

生成摘要时出错

---

## 76. Using OR-Tools CP-SAT for Scheduling Problems

**原文标题**: Using OR-Tools CP-SAT for Scheduling Problems

**原文链接**: [https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html](https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html)

生成摘要时出错

---

## 77. The Original 1965 Gatorade Recipe

**原文标题**: The Original 1965 Gatorade Recipe

**原文链接**: [https://eatshistory.com/the-original-1965-gatorade-recipe-we-made-the-drink-that-started-a-billion-dollar-industry/](https://eatshistory.com/the-original-1965-gatorade-recipe-we-made-the-drink-that-started-a-billion-dollar-industry/)

生成摘要时出错

---

## 78. Remove .zig Files from Bun

**原文标题**: Remove .zig Files from Bun

**原文链接**: [https://github.com/oven-sh/bun/pull/30680](https://github.com/oven-sh/bun/pull/30680)

生成摘要时出错

---

## 79. Israel's AI targeting system: how data from a phone become a death sentence

**原文标题**: Israel's AI targeting system: how data from a phone become a death sentence

**原文链接**: [https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence](https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence)

生成摘要时出错

---

## 80. Fc, a lossless compressor for floating-point streams

**原文标题**: Fc, a lossless compressor for floating-point streams

**原文链接**: [https://github.com/xtellect/fc](https://github.com/xtellect/fc)

生成摘要时出错

---

## 81. Making the news available at no cost is a victory

**原文标题**: Making the news available at no cost is a victory

**原文链接**: [https://www.sltrib.com/opinion/commentary/2026/05/12/just-days-tribune-reporting/](https://www.sltrib.com/opinion/commentary/2026/05/12/just-days-tribune-reporting/)

生成摘要时出错

---

## 82. Arena AI Model ELO History

**原文标题**: Arena AI Model ELO History

**原文链接**: [https://mayerwin.github.io/AI-Arena-History/](https://mayerwin.github.io/AI-Arena-History/)

生成摘要时出错

---

## 83. Self-report fraud and walk free, New York prosecutors tell Wall Street

**原文标题**: Self-report fraud and walk free, New York prosecutors tell Wall Street

**原文链接**: [https://www.ft.com/content/6344b5be-e48c-48b8-8fea-d86e6c4c4aec](https://www.ft.com/content/6344b5be-e48c-48b8-8fea-d86e6c4c4aec)

生成摘要时出错

---

## 84. Open Source Resistance: keep OSS alive on company time

**原文标题**: Open Source Resistance: keep OSS alive on company time

**原文链接**: [https://ossresistance.com/](https://ossresistance.com/)

生成摘要时出错

---

## 85. Preserving Fisher-Price Pixter

**原文标题**: Preserving Fisher-Price Pixter

**原文链接**: [https://dmitry.gr/?r=05.Projects&proj=37.%20Pixter](https://dmitry.gr/?r=05.Projects&proj=37.%20Pixter)

生成摘要时出错

---

## 86. Comparing a 1980s memory map to the Raspi Pico

**原文标题**: Comparing a 1980s memory map to the Raspi Pico

**原文链接**: [https://medium.com/@noborutakahashi/a-40-year-old-memory-map-comparable-to-todays-raspberry-pi-pico-932c4309260d](https://medium.com/@noborutakahashi/a-40-year-old-memory-map-comparable-to-todays-raspberry-pi-pico-932c4309260d)

生成摘要时出错

---

## 87. Hardware Attestation as Monopoly Enabler

**原文标题**: Hardware Attestation as Monopoly Enabler

**原文链接**: [https://grapheneos.social/@GrapheneOS/116550899908879585](https://grapheneos.social/@GrapheneOS/116550899908879585)

生成摘要时出错

---

