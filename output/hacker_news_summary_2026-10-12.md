# Hacker News 热门文章摘要 (2026-10-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GLM-法律

**原文标题**: GLM-Legal

**原文链接**: [https://z.ai/blog/glm-legal](https://z.ai/blog/glm-legal)

**GLM-Legal** 是一款专为应对法律行业的特定复杂性和专业需求而开发的专业大语言模型（LLM）。它基于 **GLM-4** 架构构建，代表了从通用人工智能向专为高精度环境设计的领域特定“垂直”模型的重大转变。

GLM-Legal 的开发涉及在海量、高质量的法律语料库上进行训练。该数据集涵盖了法律法规、司法判例和法律学术文献。通过整合这些专业知识，该模型克服了通用大模型的局限性，后者往往难以处理法律推理所需的精确术语和复杂逻辑。

**其核心特性与能力包括：**

*   **法律专业知识：** 该模型经过微调，能够理解并应用法律原则，使其精通法律咨询、案件分析和文书起草等任务。
*   **减少幻觉：** GLM-Legal 的一个主要重点是提高事实准确性。在法律领域，“幻觉”或编造的信息可能会导致严重后果；该模型经过优化，可提供可靠且基于证据的回答。
*   **性能基准：** 在包括专业法律考试和司法任务模拟在内的各项评估中，据报道，GLM-Legal 在中国法律背景下的表现优于 GPT-4 等通用模型。
*   **为专业人士增效：** 该工具旨在通过自动执行法律研究、总结冗长的案件卷宗以及识别相关判例来辅助律师和法官，从而显著提高工作流效率。

总之，GLM-Legal 弥补了通用人工智能与司法专业需求之间的差距，为法律领域提供了一个更准确、可靠且专业的工具。

---

## 2. Who Is Vfmaddrnd231pd?

**原文标题**: Who Is Vfmaddrnd231pd?

**原文链接**: [https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/](https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/)

In the blog post "Who Is Vfmaddrnd231pd?", the author investigates a mysterious "phantom" x86 instruction discovered in the Intel Software Development Manual (SDM). 

**The Instruction**
`vfmaddrnd231pd` was documented as a Fused Multiply-Add (FMA) instruction that allowed for per-instruction rounding control via an immediate byte. This feature would theoretically allow developers to perform high-performance arithmetic with specific rounding modes without the overhead of changing the CPU's global rounding state.

**The Discrepancies**
Despite its detailed documentation—including unique tables and pseudocode—the author found that the instruction does not actually function:
*   **Missing Support:** Neither the GNU assembler nor compilers like Clang or ICC recognize the instruction or its associated intrinsics.
*   **Technical Red Flags:** The opcode uses a prefix ("DDS") that is otherwise undocumented or deprecated in modern SDMs.
*   **Execution Failure:** Attempting to run the instruction on hardware that supports the FMA set (such as Haswell) results in an "Undefined Instruction" (#UD) error.
*   **Documentation Removal:** While the instruction appeared in the 2024 version of the SDM, it was completely scrubbed from the 2026 edition.

**Conclusion**
The author hypothesizes that `vfmaddrnd231pd` was a planned feature that Intel cancelled late in the hardware development cycle. Due to a documentation error, the technical specifications were accidentally published in the SDM before being removed in later revisions. Ultimately, the instruction is a "ghost" that exists in manuals but never made it into physical silicon.

---

## 3. A Modern Web App in C

**原文标题**: A Modern Web App in C

**原文链接**: [https://prophitt.me/writing/a-modern-web-app-in-c](https://prophitt.me/writing/a-modern-web-app-in-c)

生成摘要时出错

---

## 4. Phreak.ing – 网络电话交换机

**原文标题**: Phreak.ing – Internet Phone Switch

**原文链接**: [https://phreak.ing/](https://phreak.ing/)

**Phreak.ing – 互联网电话交换机**是一款功能强大的 VoIP 平台，通过一系列拨号代码和键盘指令实现通信管理与系统设置。该服务提供了一套涵盖通话功能、管理维护及社交互动的综合工具集。

核心功能包括标准电信服务，如回声测试、末次来电回拨（*69）和匿名拨号（*67）。管理工具允许用户处理个人或通用语音信箱、“驻留”通话以待后续接听，以及代接响铃中的分机。此外，系统支持强大的对讲与广播功能，可在桌面电话间实现单向或双向扩音通信。

用户可以直接通过键盘切换“勿扰模式”或配置呼叫转移，从而管理自己的状态。除基础通话外，Phreak.ing 还整合了独特的社交与媒体功能，包括：

*   **会议室：** 访问众多公共会议室（*801-*899）及特定的社区语音频道。
*   **媒体：** “acid-radio”实时音频流。
*   **消息传递：** 支持从电话向专用频道（#phreak）发送短信。
*   **附加功能：** 用于开启“派对模式”的特殊指令，以及快速访问系统帮助目录。

该平台提供了一个灵活的界面，使用户能够通过简单的数字快捷键全面掌控其互联网电话环境。

---

## 5. 黑客开启欧洲各地超市冷柜自动除霜功能

**原文标题**: Hackers activate automatic defrosting in supermarket fridges across Europe

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident)

一场重大的网络攻击袭击了欧洲多家知名连锁超市，包括 Intermarché、Leclerc 和 Albert Heijn。此次攻击专门针对丹佛斯（Danfoss）制造的制冷控制系统，迫使设备进入设定为 50 摄氏度（122 华氏度）的持续除霜循环。

此次入侵的影响是多方面的：
*   **食品变质：** 制冷设备的强制加热导致了巨大的库存损失。初步估计损失为 30 万欧元，但专家警告称，随着生鲜产品变质，全国范围内的总损失可能达到数百万欧元。
*   **运营中断：** 除制冷系统外，攻击还影响了电子价签，导致店内价格出错。在荷兰和比利时，Albert Heijn 和 Delhaize 等超市报告了网站故障，导致配送服务和会员计划陷入瘫痪。
*   **安全响应：** 零售商已动员制冷专家和 IT 团队以重夺控制权。一些连锁机构已预防性地关闭了系统，以保护其整体 IT 环境。

法国 Coopérative U 集团主席多米尼克·谢尔彻（Dominique Schelcher）形容此次事件“极其严重”且“前所未有”，并指出攻击关键食品供应基础设施是“不可接受的”。虽然攻击的完整规模仍在确定中，但相关调查正在进行，以确认法国、荷兰和比利时发生的干扰是否出自同一组织之手。此次事件引发了关于将关键工业设备连接至互联网所带来的安全风险的更广泛讨论。

---

## 6. 在 Firefox 中实现大文件断点续传

**原文标题**: Making big downloads resumable in Firefox

**原文链接**: [https://lunarwatcher.codeberg.page/til/firefox/resumable-big-downloads.html](https://lunarwatcher.codeberg.page/til/firefox/resumable-big-downloads.html)

在本文中，Olivia 概述了提高 Firefox 大文件下载稳定性和续传能力的解决方案。自第 28 版起，该浏览器的 `network.http.response.timeout` 设置默认为 300 秒，作者认为这是导致下载失败或无法续传的主要原因。

**核心要点：**
*   **解决方案：** 用户可以访问 `about:config` 并将 `network.http.response.timeout` 更改为 **0**（或一个明显更大的值）。实验测试表明，这能让 Firefox 成功续传原本会失败的下载。
*   **作用机制：** 作者指出，当发生连接错误时，Firefox 经常会忽略现有的 `.part` 文件。浏览器的续传能力似乎取决于连接超时设置；通过取消超时限制，浏览器更有可能维持或正确重启下载进程。
*   **局限性：** 只有在托管文件的服务器支持断点续传时，此修复才有效。作者还观察到，Firefox 的内部下载管理长期以来一直不稳定，相关问题可追溯至 2005 年。
*   **替代方案：** 对于在浏览器之外寻求更强大解决方案的用户，作者建议使用带有 `-c` 参数的命令行工具 `wget`（例如 `wget -c -O "$filename" "$url"`），该工具以其卓越的稳定性著称。

---

## 7. 为 ZX Spectrum 编写 Demoscene Intro

**原文标题**: Writing a Demoscene Intro for the ZX Spectrum

**原文链接**: [https://www.markround.com/blog/2026/zx-spectrum-intro](https://www.markround.com/blog/2026/zx-spectrum-intro)

本文记录了作者为128Kb ZX Spectrum创作Demo演示（intro）的历程，该项目的灵感源于其童年时期对20世纪80年代Amiga“破解片头”（cracktros）的痴迷。最终的作品集成了视差星空、平滑滚动文本、自定义字体及三通道AY音轨，是对Z80汇编语言和8位硬件限制的一次深度技术探究。

作者介绍了一套结合了Pasmo汇编器、FUSE模拟器和实机Spectrum +3的现代开发工作流。从高级语言编程转向汇编语言需要一种“回归基础”的方法，涉及手动位掩码、寄存器跟踪，以及利用在线Z80编辑器来可视化指令集。

文中探讨的关键技术里程碑包括：
*   **硬件交互：** 使用`out`指令与ULA（用于控制边框颜色）及AY-3-8912音频芯片进行通信。
*   **内存管理：** 利用`ldir`指令进行块内存复制，并深入理解Spectrum的内存映射。
*   **ROM例程：** 探索了用于打印文本的内置“系统调用”，但作者最终选择编写自定义例程，以实现更具“Demo感”的精美字体。
*   **“诡异”的屏幕布局：** 作者强调了Spectrum臭名昭著的非线性显示内存。与现代位图显示不同，Spectrum的内存被分为三个区域且行间交错，这使得手动像素操作和滚动处理成为了极具挑战的逻辑难题。

最终，该项目实现了作者数十年来从Sinclair BASIC转型到专业级机器码的夙愿，彰显了Demoscene作为“代码艺术”与技术巧思结合体的独特魅力。

---

## 8. Turn a WiFi 7 Router into a 320Msps Software Defined Radio Receiver

**原文标题**: Turn a WiFi 7 Router into a 320Msps Software Defined Radio Receiver

**原文链接**: [https://github.com/h0m3us3r/w1700k-sdr](https://github.com/h0m3us3r/w1700k-sdr)

The **W1700K SDR** project converts a Gemtek W1700K WiFi 7 router into a high-performance, wideband software-defined radio receiver. By leveraging the router's MediaTek MT7996 radio and Airoha AN7581 SoC, the system captures 14-bit IQ data at sample rates up to 320 Msps across the 2.4, 5, and 6 GHz bands.

**Key Technical Features:**
*   **Performance:** It supports sample rates of 40, 80, 160, or 320 Msps. On the 2.4 GHz band, it can even achieve 640/2 Msps.
*   **Tuning and Filtering:** The system offers precise tuning (sub-15 Hz steps) across wide frequency ranges and features an adjustable analog filter (20–320 MHz).
*   **Custom Firmware:** The project utilizes entirely original firmware, including a custom ROM patch and radio management code developed without any proprietary MediaTek code.
*   **Data Transport:** Raw IQ data is streamed via a 10 GbE link using zero-copy UDP datagrams. This allows a Linux host to process massive bandwidth in real-time.
*   **Visualization:** A browser-based interface provides a live spectrum and waterfall display, performing a 262,144-point FFT at 100 frames per second with built-in digital roll-off correction.

**Requirements and Safety:**
Installation requires a 3.3V USB serial adapter for console access and replaces the router's stock operating system. Notably, the firmware is **receive-only**; it disables all transmit paths to prevent accidental interference. The project is open-source, primarily under the MIT license, with specific kernel components under GPL. 

This transformation turns consumer networking hardware into a powerful tool for wideband RF analysis, capable of visualizing entire WiFi bands simultaneously with high precision.

---

## 9. Codex CLI installs a persistent, self-updating background daemon by default

**原文标题**: Codex CLI installs a persistent, self-updating background daemon by default

**原文链接**: [https://github.com/openai/codex/issues/48195](https://github.com/openai/codex/issues/48195)

生成摘要时出错

---

## 10. Citroen revives the 2CV for an electric age

**原文标题**: Citroen revives the 2CV for an electric age

**原文链接**: [https://www.bbc.com/news/articles/c620r33plgppo](https://www.bbc.com/news/articles/c620r33plgppo)

生成摘要时出错

---

## 11. AI is a tool and using it well takes skill

**原文标题**: AI is a tool and using it well takes skill

**原文链接**: [https://yyhh.org/blog/2026/10/ai-is-a-tool/](https://yyhh.org/blog/2026/10/ai-is-a-tool/)

生成摘要时出错

---

## 12. The Making Of Super Mario 64 – full Giles Goddard interview (2001)

**原文标题**: The Making Of Super Mario 64 – full Giles Goddard interview (2001)

**原文链接**: [https://pixelatron.com/blog/the-making-of-super-mario-64-full-giles-goddard-interview-ngc/](https://pixelatron.com/blog/the-making-of-super-mario-64-full-giles-goddard-interview-ngc/)

生成摘要时出错

---

## 13. Muse Wonder

**原文标题**: Muse Wonder

**原文链接**: [https://research.meta.ai/blog/muse-wonder](https://research.meta.ai/blog/muse-wonder)

生成摘要时出错

---

## 14. Breaking Bad star RJ Mitte dies aged 34

**原文标题**: Breaking Bad star RJ Mitte dies aged 34

**原文链接**: [https://news.sky.com/story/breaking-bad-star-rj-mitte-dies-aged-34-13598332](https://news.sky.com/story/breaking-bad-star-rj-mitte-dies-aged-34-13598332)

生成摘要时出错

---

## 15. Secret of Orange Cats Revealed After 60-Year Search

**原文标题**: Secret of Orange Cats Revealed After 60-Year Search

**原文链接**: [https://www.sciencealert.com/secret-of-orange-cats-finally-revealed-after-60-year-search](https://www.sciencealert.com/secret-of-orange-cats-finally-revealed-after-60-year-search)

生成摘要时出错

---

## 16. Kevin Kelly's 2016 AI Predictions, 10 Years Later

**原文标题**: Kevin Kelly's 2016 AI Predictions, 10 Years Later

**原文链接**: [https://taylor.town/kk-ai-2026](https://taylor.town/kk-ai-2026)

生成摘要时出错

---

## 17. Solar panels that plug into your wall

**原文标题**: Solar panels that plug into your wall

**原文链接**: [https://www.nationalgeographic.com/environment/article/balcony-plug-in-solar-panels-renewable-energy](https://www.nationalgeographic.com/environment/article/balcony-plug-in-solar-panels-renewable-energy)

生成摘要时出错

---

## 18. Show HN: PS2 games statically recompiled to WebAssembly

**原文标题**: Show HN: PS2 games statically recompiled to WebAssembly

**原文链接**: [https://github.com/snuri00/ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp)

生成摘要时出错

---

## 19. Show HN: Brickbrag – A multiplayer brick-building world in the browser

**原文标题**: Show HN: Brickbrag – A multiplayer brick-building world in the browser

**原文链接**: [https://brickbrag.com/](https://brickbrag.com/)

生成摘要时出错

---

## 20. 'AI' Is Not a Tool by Rich Hickey

**原文标题**: 'AI' Is Not a Tool by Rich Hickey

**原文链接**: [https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e](https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e)

生成摘要时出错

---

## 21. Thinking will become a hobby

**原文标题**: Thinking will become a hobby

**原文链接**: [https://www.spinellis.gr/blog/20261008/?li261008](https://www.spinellis.gr/blog/20261008/?li261008)

生成摘要时出错

---

## 22. AI coding agents generate more code, but not more software

**原文标题**: AI coding agents generate more code, but not more software

**原文链接**: [https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/](https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/)

生成摘要时出错

---

## 23. Show HN: Atticus – Hold-to-talk voice assistant for macOS that runs on Claude -p

**原文标题**: Show HN: Atticus – Hold-to-talk voice assistant for macOS that runs on Claude -p

**原文链接**: [https://github.com/SaarthurR/atticus-mac](https://github.com/SaarthurR/atticus-mac)

生成摘要时出错

---

## 24. Publishers Killed the Paperback, Then Blamed Readers

**原文标题**: Publishers Killed the Paperback, Then Blamed Readers

**原文链接**: [https://jacobin.com/2026/10/books-publishing-reading-mass-market-paperback](https://jacobin.com/2026/10/books-publishing-reading-mass-market-paperback)

生成摘要时出错

---

## 25. Type-safe HTML templating in Zig

**原文标题**: Type-safe HTML templating in Zig

**原文链接**: [https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html](https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html)

生成摘要时出错

---

## 26. America's Longest Highway Tunnel (2025)

**原文标题**: America's Longest Highway Tunnel (2025)

**原文链接**: [https://www.thetravel.com/americas-longest-highway-tunnel-not-for-faint-of-heart/](https://www.thetravel.com/americas-longest-highway-tunnel-not-for-faint-of-heart/)

生成摘要时出错

---

## 27. No portable way to detect string-to-float conversion errors in standard C

**原文标题**: No portable way to detect string-to-float conversion errors in standard C

**原文链接**: [https://sebsite.pw/w/20261009-strtod.html](https://sebsite.pw/w/20261009-strtod.html)

生成摘要时出错

---

## 28. My Reddit AMA on the Law of Web Scraping

**原文标题**: My Reddit AMA on the Law of Web Scraping

**原文链接**: [https://blog.ericgoldman.org/archives/2026/10/my-reddit-ama-on-the-law-of-web-scraping.htm](https://blog.ericgoldman.org/archives/2026/10/my-reddit-ama-on-the-law-of-web-scraping.htm)

生成摘要时出错

---

## 29. QGIS enacts moratorium on AI contributions

**原文标题**: QGIS enacts moratorium on AI contributions

**原文链接**: [https://github.com/qgis/QGIS-Enhancement-Proposals/pull/387](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/387)

生成摘要时出错

---

## 30. I Found a $90k Remote Code Execution Vulnerability in Google

**原文标题**: I Found a $90k Remote Code Execution Vulnerability in Google

**原文链接**: [https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce)

生成摘要时出错

---

## 31. (Post-Quantum) Cryptographic Right Answers

**原文标题**: (Post-Quantum) Cryptographic Right Answers

**原文链接**: [https://words.filippo.io/right-answers/](https://words.filippo.io/right-answers/)

生成摘要时出错

---

## 32. Calculus with Julia

**原文标题**: Calculus with Julia

**原文链接**: [https://jverzani.github.io/CalculusWithJuliaNotes.jl/](https://jverzani.github.io/CalculusWithJuliaNotes.jl/)

生成摘要时出错

---

## 33. OpenFatigue™ – Open is the new closed

**原文标题**: OpenFatigue™ – Open is the new closed

**原文链接**: [https://openfatigue.ai/](https://openfatigue.ai/)

生成摘要时出错

---

## 34. Terence Tao: Math 2.0 [pdf]

**原文标题**: Terence Tao: Math 2.0 [pdf]

**原文链接**: [https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf)

生成摘要时出错

---

## 35. Reverse engineer anything with agents, from app behavior down to native binaries

**原文标题**: Reverse engineer anything with agents, from app behavior down to native binaries

**原文链接**: [https://github.com/morluto/rea](https://github.com/morluto/rea)

生成摘要时出错

---

## 36. Fingerprints are the new cookies

**原文标题**: Fingerprints are the new cookies

**原文链接**: [https://royfish.dev/fingerprints-are-the-new-cookies](https://royfish.dev/fingerprints-are-the-new-cookies)

生成摘要时出错

---

## 37. The CEO's of Broadcom and Intel Say the Quiet Part Out Loud about AI and ROI

**原文标题**: The CEO's of Broadcom and Intel Say the Quiet Part Out Loud about AI and ROI

**原文链接**: [https://wolfstreet.com/2026/10/12/ceos-of-broadcom-intel-say-the-quiet-part-out-loud-about-ai-and-roi/](https://wolfstreet.com/2026/10/12/ceos-of-broadcom-intel-say-the-quiet-part-out-loud-about-ai-and-roi/)

生成摘要时出错

---

## 38. Running the unmodified Linux amdgpu driver on an iPad

**原文标题**: Running the unmodified Linux amdgpu driver on an iPad

**原文链接**: [https://github.com/Geramy/LemonSeed-Studio](https://github.com/Geramy/LemonSeed-Studio)

生成摘要时出错

---

## 39. Cartographers of North Korea (2019)

**原文标题**: Cartographers of North Korea (2019)

**原文链接**: [https://cartographers-nk.wonyoung.so/](https://cartographers-nk.wonyoung.so/)

生成摘要时出错

---

## 40. Feds got warrants to use fake cell towers to hunt down Don Lemon's producer

**原文标题**: Feds got warrants to use fake cell towers to hunt down Don Lemon's producer

**原文链接**: [https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/](https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/)

生成摘要时出错

---

## 41. Living in the Weimar Era of Ruby

**原文标题**: Living in the Weimar Era of Ruby

**原文链接**: [https://blog.julik.nl/2026/10/the-weimar-of-ruby](https://blog.julik.nl/2026/10/the-weimar-of-ruby)

生成摘要时出错

---

## 42. Doory – Open-Source Canva

**原文标题**: Doory – Open-Source Canva

**原文链接**: [https://github.com/shaongitbd/doory](https://github.com/shaongitbd/doory)

生成摘要时出错

---

## 43. EXT4 Introducing IOmap Buffered I/O Path with Some Performance Gains

**原文标题**: EXT4 Introducing IOmap Buffered I/O Path with Some Performance Gains

**原文链接**: [https://www.phoronix.com/news/EXT4-iomap-Buffered-IO](https://www.phoronix.com/news/EXT4-iomap-Buffered-IO)

生成摘要时出错

---

## 44. Incident with Actions, Pull Requests and Issues

**原文标题**: Incident with Actions, Pull Requests and Issues

**原文链接**: [https://www.githubstatus.com/incidents/93njd414rpbx](https://www.githubstatus.com/incidents/93njd414rpbx)

生成摘要时出错

---

## 45. The gap in shared understanding of LLM capability is widening

**原文标题**: The gap in shared understanding of LLM capability is widening

**原文链接**: [https://twitter.com/karpathy/status/2109361546505966046](https://twitter.com/karpathy/status/2109361546505966046)

生成摘要时出错

---

## 46. Bag of Decisions Reranker

**原文标题**: Bag of Decisions Reranker

**原文链接**: [https://softwaredoug.com/blog/2026/10/08/bag-of-decisions.html](https://softwaredoug.com/blog/2026/10/08/bag-of-decisions.html)

生成摘要时出错

---

## 47. Epic Games tells employees to use AI to get Disney game done

**原文标题**: Epic Games tells employees to use AI to get Disney game done

**原文链接**: [https://www.avclub.com/epic-games-disney-ai-delay](https://www.avclub.com/epic-games-disney-ai-delay)

生成摘要时出错

---

## 48. Passkeys are a trap

**原文标题**: Passkeys are a trap

**原文链接**: [https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them](https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them)

生成摘要时出错

---

## 49. Total Annihilation, rebuilt for modern computers

**原文标题**: Total Annihilation, rebuilt for modern computers

**原文链接**: [https://nanolathe.gg](https://nanolathe.gg)

生成摘要时出错

---

## 50. Martin Odersky – Keynote: The End of Programming? [video]

**原文标题**: Martin Odersky – Keynote: The End of Programming? [video]

**原文链接**: [https://www.youtube.com/watch?v=jlJyuJhDnlc](https://www.youtube.com/watch?v=jlJyuJhDnlc)

生成摘要时出错

---

## 51. EC users should be afraid of a US kill switch – not some new software

**原文标题**: EC users should be afraid of a US kill switch – not some new software

**原文链接**: [https://www.theregister.com/columnists/2026/10/10/ec-users-should-be-afraid-of-a-us-kill-switch-not-some-new-software/5301875](https://www.theregister.com/columnists/2026/10/10/ec-users-should-be-afraid-of-a-us-kill-switch-not-some-new-software/5301875)

生成摘要时出错

---

## 52. Firefox 158 Now Available with JPEG-XL Support by Default

**原文标题**: Firefox 158 Now Available with JPEG-XL Support by Default

**原文链接**: [https://www.phoronix.com/news/Firefox-158-Released](https://www.phoronix.com/news/Firefox-158-Released)

生成摘要时出错

---

## 53. Chapter 1 of "Ways of Seeing" by John Berger (1972)

**原文标题**: Chapter 1 of "Ways of Seeing" by John Berger (1972)

**原文链接**: [https://www.ways-of-seeing.com/ch1](https://www.ways-of-seeing.com/ch1)

生成摘要时出错

---

## 54. Ukraine strikes didn't blow up Russian disinformation on social

**原文标题**: Ukraine strikes didn't blow up Russian disinformation on social

**原文链接**: [https://www.machinesociety.ai/p/no-ukraine-strikes-didnt-blow-up](https://www.machinesociety.ai/p/no-ukraine-strikes-didnt-blow-up)

生成摘要时出错

---

## 55. Local Indexing to reduce tool calling and token usage

**原文标题**: Local Indexing to reduce tool calling and token usage

**原文链接**: [https://tedhaley.ca/pensieve/](https://tedhaley.ca/pensieve/)

生成摘要时出错

---

## 56. An Unmade Film Shaped Hayao Miyazaki

**原文标题**: An Unmade Film Shaped Hayao Miyazaki

**原文链接**: [https://animationobsessive.substack.com/p/an-unmade-film-shaped-hayao-miyazaki](https://animationobsessive.substack.com/p/an-unmade-film-shaped-hayao-miyazaki)

生成摘要时出错

---

## 57. Weave (YC W25) is hiring ML, AI, product, & design engineers

**原文标题**: Weave (YC W25) is hiring ML, AI, product, & design engineers

**原文链接**: [https://jobs.ashbyhq.com/weave-os](https://jobs.ashbyhq.com/weave-os)

生成摘要时出错

---

## 58. Obituary: Robert X. Cringley

**原文标题**: Obituary: Robert X. Cringley

**原文链接**: [https://www.facebook.com/story.php?story_fbid=pfbid0YbCLrAJfBirAWuPBy4a7pauaQ6gHkAPUwtbzyg2wAjeMcruFC7dWUZKQJKkNChP9l&id=536506060&_rdr](https://www.facebook.com/story.php?story_fbid=pfbid0YbCLrAJfBirAWuPBy4a7pauaQ6gHkAPUwtbzyg2wAjeMcruFC7dWUZKQJKkNChP9l&id=536506060&_rdr)

生成摘要时出错

---

## 59. Illustration Beyond Proof

**原文标题**: Illustration Beyond Proof

**原文链接**: [https://terrytao.wordpress.com/2026/10/11/illustration-beyond-proof/](https://terrytao.wordpress.com/2026/10/11/illustration-beyond-proof/)

生成摘要时出错

---

## 60. NYC's "Click to Cancel" rule is now in effect

**原文标题**: NYC's "Click to Cancel" rule is now in effect

**原文链接**: [https://www.nyc.gov/main/click-to-cancel](https://www.nyc.gov/main/click-to-cancel)

生成摘要时出错

---

## 61. I guess I'm using WebP now?

**原文标题**: I guess I'm using WebP now?

**原文链接**: [https://anderegg.ca/2026/10/08/i-guess-im-using-webp-now](https://anderegg.ca/2026/10/08/i-guess-im-using-webp-now)

生成摘要时出错

---

## 62. So, you’d like to sell your print issues of The Onion?

**原文标题**: So, you’d like to sell your print issues of The Onion?

**原文链接**: [https://theonion.com/archivehunt/](https://theonion.com/archivehunt/)

生成摘要时出错

---

## 63. Empty shelves likely at Nederlands Albert Heijn due to "Cyber incident"

**原文标题**: Empty shelves likely at Nederlands Albert Heijn due to "Cyber incident"

**原文链接**: [https://nltimes.nl/2026/10/12/empty-shelves-likely-albert-heijn-cyber-incident-extends-parents-us-business](https://nltimes.nl/2026/10/12/empty-shelves-likely-albert-heijn-cyber-incident-extends-parents-us-business)

生成摘要时出错

---

## 64. Google Data Centers around the world

**原文标题**: Google Data Centers around the world

**原文链接**: [https://datacenters.google/locations/](https://datacenters.google/locations/)

生成摘要时出错

---

## 65. Valen's Memory Safety: A New Kind of Borrow Checking

**原文标题**: Valen's Memory Safety: A New Kind of Borrow Checking

**原文链接**: [https://verdagon.dev/blog/valen-group-borrowing](https://verdagon.dev/blog/valen-group-borrowing)

生成摘要时出错

---

## 66. Programmable pigments: Photochromic nanoparticle inks for rewritable tattoos

**原文标题**: Programmable pigments: Photochromic nanoparticle inks for rewritable tattoos

**原文链接**: [https://www.cell.com/matter-light/fulltext/S3117-5848(26)00119-5](https://www.cell.com/matter-light/fulltext/S3117-5848(26)00119-5)

生成摘要时出错

---

## 67. Using AI for just 10 minutes erodes your ability to persist at hard things

**原文标题**: Using AI for just 10 minutes erodes your ability to persist at hard things

**原文链接**: [https://vcresearch.berkeley.edu/news/using-ai-just-10-minutes-erodes-your-ability-persist-hard-things](https://vcresearch.berkeley.edu/news/using-ai-just-10-minutes-erodes-your-ability-persist-hard-things)

生成摘要时出错

---

## 68. Deloitte falsified documents to evade tax on Abramovich's wealth

**原文标题**: Deloitte falsified documents to evade tax on Abramovich's wealth

**原文链接**: [https://www.bbc.com/news/articles/c64g1l5389kvo](https://www.bbc.com/news/articles/c64g1l5389kvo)

生成摘要时出错

---

## 69. Ricky Mondello responds to "Passkeys are a trap. Do not use them."

**原文标题**: Ricky Mondello responds to "Passkeys are a trap. Do not use them."

**原文链接**: [https://hachyderm.io/@rmondello/117428258722253709](https://hachyderm.io/@rmondello/117428258722253709)

生成摘要时出错

---

## 70. Vectorized CLZ and CTZ

**原文标题**: Vectorized CLZ and CTZ

**原文链接**: [https://purplesyringa.moe/blog/vectorized-clz-and-ctz/](https://purplesyringa.moe/blog/vectorized-clz-and-ctz/)

生成摘要时出错

---

## 71. IRCv3

**原文标题**: IRCv3

**原文链接**: [https://ircv3.net/](https://ircv3.net/)

生成摘要时出错

---

## 72. "Today we're laying off a large part of the Airtable team "

**原文标题**: "Today we're laying off a large part of the Airtable team "

**原文链接**: [https://twitter.com/fedesimio/status/2109713695165329511](https://twitter.com/fedesimio/status/2109713695165329511)

生成摘要时出错

---

## 73. Phishing emails are now baiting your AI assistant

**原文标题**: Phishing emails are now baiting your AI assistant

**原文链接**: [https://www.malwarebytes.com/blog/ai/2026/10/phishing-emails-are-baiting-your-ai-assistant](https://www.malwarebytes.com/blog/ai/2026/10/phishing-emails-are-baiting-your-ai-assistant)

生成摘要时出错

---

## 74. Choreographic Programming in Rust

**原文标题**: Choreographic Programming in Rust

**原文链接**: [https://github.com/hibanaworks/hibana](https://github.com/hibanaworks/hibana)

生成摘要时出错

---

## 75. apsw: Another Python SQLite Wrapper

**原文标题**: apsw: Another Python SQLite Wrapper

**原文链接**: [https://github.com/rogerbinns/apsw](https://github.com/rogerbinns/apsw)

生成摘要时出错

---

## 76. 3rd Yandex Cloud Data Center Was Hit

**原文标题**: 3rd Yandex Cloud Data Center Was Hit

**原文链接**: [https://status.yandex.cloud/en/incidents/2136](https://status.yandex.cloud/en/incidents/2136)

生成摘要时出错

---

## 77. A Cray-1 supercomputer replica from 30 "obsolete" Mac Minis

**原文标题**: A Cray-1 supercomputer replica from 30 "obsolete" Mac Minis

**原文链接**: [https://arstechnica.com/gadgets/2026/10/a-cray-1-supercomputer-replica-from-30-obsolete-mac-minis/](https://arstechnica.com/gadgets/2026/10/a-cray-1-supercomputer-replica-from-30-obsolete-mac-minis/)

生成摘要时出错

---

## 78. Scandinavia's first farmers slaughtered hunter-gatherer population, DNA suggests

**原文标题**: Scandinavia's first farmers slaughtered hunter-gatherer population, DNA suggests

**原文链接**: [https://phys.org/news/2024-02-scandinavia-farmers-slaughtered-hunter-population.html](https://phys.org/news/2024-02-scandinavia-farmers-slaughtered-hunter-population.html)

生成摘要时出错

---

## 79. ClickHouse C – Talk to ClickHouse using its native binary protocol

**原文标题**: ClickHouse C – Talk to ClickHouse using its native binary protocol

**原文链接**: [https://github.com/ClickHouse/clickhouse-c](https://github.com/ClickHouse/clickhouse-c)

生成摘要时出错

---

## 80. Recursive self-improvement through collective intelligence

**原文标题**: Recursive self-improvement through collective intelligence

**原文链接**: [https://pub.sakana.ai/mass/](https://pub.sakana.ai/mass/)

生成摘要时出错

---

## 81. Whatever became of holography? (2011)

**原文标题**: Whatever became of holography? (2011)

**原文链接**: [https://www.americanscientist.org/article/whatever-became-of-holography](https://www.americanscientist.org/article/whatever-became-of-holography)

生成摘要时出错

---

## 82. Deep dive into Azure Maia 300 architecture

**原文标题**: Deep dive into Azure Maia 300 architecture

**原文链接**: [https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/](https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/)

生成摘要时出错

---

## 83. Tesla Factory Plan Increase of Toxic Heavy Metal Emissions Near School

**原文标题**: Tesla Factory Plan Increase of Toxic Heavy Metal Emissions Near School

**原文链接**: [https://anonymous94538.substack.com/p/tesla-fremont-is-applying-to-spew](https://anonymous94538.substack.com/p/tesla-fremont-is-applying-to-spew)

生成摘要时出错

---

## 84. LineageOS 24

**原文标题**: LineageOS 24

**原文链接**: [https://lineageos.org/Changelog-32/](https://lineageos.org/Changelog-32/)

生成摘要时出错

---

## 85. I paid people to try and follow my README

**原文标题**: I paid people to try and follow my README

**原文链接**: [https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/](https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/)

生成摘要时出错

---

## 86. Will Linux phones become a viable alternative to the Android/iOS duopoly?

**原文标题**: Will Linux phones become a viable alternative to the Android/iOS duopoly?

**原文链接**: [https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/](https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/)

生成摘要时出错

---

## 87. Rice husk is being repurposed as a sturdy and resilient construction material

**原文标题**: Rice husk is being repurposed as a sturdy and resilient construction material

**原文链接**: [https://www.bbc.com/future/article/20261009-the-houses-made-from-rice-husks](https://www.bbc.com/future/article/20261009-the-houses-made-from-rice-husks)

生成摘要时出错

---

## 88. Cbirds: A flock of birds in your terminal

**原文标题**: Cbirds: A flock of birds in your terminal

**原文链接**: [https://github.com/clainstone/cbirds](https://github.com/clainstone/cbirds)

生成摘要时出错

---

## 89. A Critical Look at Lean4

**原文标题**: A Critical Look at Lean4

**原文链接**: [https://www.lesswrong.com/posts/zHhGa3iQBQcdSifFL/a-critical-look-at-lean4-1](https://www.lesswrong.com/posts/zHhGa3iQBQcdSifFL/a-critical-look-at-lean4-1)

生成摘要时出错

---

## 90. How I reverse engineered a commercial spatial audio effect

**原文标题**: How I reverse engineered a commercial spatial audio effect

**原文链接**: [http://epestr.com/blog/reverse-engineering-a-commercial-spatial-audio-effect/](http://epestr.com/blog/reverse-engineering-a-commercial-spatial-audio-effect/)

生成摘要时出错

---

## 91. 500B tokens later: Letting AI agents decompile a first-person shooter

**原文标题**: 500B tokens later: Letting AI agents decompile a first-person shooter

**原文链接**: [https://momo5502.com/posts/2026-10-09-game-decompilation/](https://momo5502.com/posts/2026-10-09-game-decompilation/)

生成摘要时出错

---

## 92. Safe SIMD in Rust, even on the inside

**原文标题**: Safe SIMD in Rust, even on the inside

**原文链接**: [https://shnatsel.github.io/safe-simd-in-rust-even-on-the-inside/](https://shnatsel.github.io/safe-simd-in-rust-even-on-the-inside/)

生成摘要时出错

---

## 93. I'm sorry, but you still have to think

**原文标题**: I'm sorry, but you still have to think

**原文链接**: [https://itsallaboutthebit.com/i-am-sorry-but-you-still-have-to-think/](https://itsallaboutthebit.com/i-am-sorry-but-you-still-have-to-think/)

生成摘要时出错

---

## 94. Zod 4.6.6 compromised by malware?

**原文标题**: Zod 4.6.6 compromised by malware?

**原文链接**: [https://github.com/colinhacks/zod/commit/d821685ea6732436fcdf786a81d076958471e467](https://github.com/colinhacks/zod/commit/d821685ea6732436fcdf786a81d076958471e467)

生成摘要时出错

---

## 95. 2D Vehicles

**原文标题**: 2D Vehicles

**原文链接**: [https://patkerr.co.uk/2d-vehicles/](https://patkerr.co.uk/2d-vehicles/)

生成摘要时出错

---

## 96. Postgres isn't slow, your storage is

**原文标题**: Postgres isn't slow, your storage is

**原文链接**: [https://clickhouse.com/blog/posette-talk-recap-postgres-isnt-slow-your-storage-is](https://clickhouse.com/blog/posette-talk-recap-postgres-isnt-slow-your-storage-is)

生成摘要时出错

---

## 97. A Remote Employee Refused 160 Webcam Photos a Day. Her Employer Fired Her

**原文标题**: A Remote Employee Refused 160 Webcam Photos a Day. Her Employer Fired Her

**原文链接**: [https://www.inc.com/chloe-rosenberg/a-remote-employee-refused-160-webcam-photos-a-day-her-employer-fired-her/91415963](https://www.inc.com/chloe-rosenberg/a-remote-employee-refused-160-webcam-photos-a-day-her-employer-fired-her/91415963)

生成摘要时出错

---

## 98. Kamino: GPU-Based Simulation of Rigid Multi-Body Physics with Kinematic Loops [video]

**原文标题**: Kamino: GPU-Based Simulation of Rigid Multi-Body Physics with Kinematic Loops [video]

**原文链接**: [https://www.youtube.com/watch?v=_eYarcC8D9Y](https://www.youtube.com/watch?v=_eYarcC8D9Y)

生成摘要时出错

---

## 99. FlowCE: Calculus on your TI-84 Plus CE

**原文标题**: FlowCE: Calculus on your TI-84 Plus CE

**原文链接**: [https://tommyb3ll.github.io/FlowCE/](https://tommyb3ll.github.io/FlowCE/)

生成摘要时出错

---

## 100. Draw by Pinging IPv6 Addresses

**原文标题**: Draw by Pinging IPv6 Addresses

**原文链接**: [https://pings.utwente.io/](https://pings.utwente.io/)

生成摘要时出错

---

