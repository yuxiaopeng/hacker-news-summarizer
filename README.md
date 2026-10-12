# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-12.md)

*最后自动更新时间: 2026-10-12 23:55:33*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 2 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 3 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 4 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 5 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 6 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 7 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 8 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 9 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 10 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 11 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 12 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 13 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 14 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 15 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 16 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 17 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 18 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 19 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 20 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 21 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 22 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 23 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 24 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 25 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 26 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 27 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 28 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 29 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 30 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 31 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 32 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 33 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 34 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 35 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 36 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 37 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 38 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 39 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 40 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 41 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 42 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 43 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 44 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 45 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 46 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 47 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 48 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 49 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 50 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 51 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 52 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 53 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 54 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 55 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 56 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 57 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 58 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 59 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 60 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 61 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 62 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 63 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 64 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 65 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 66 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 67 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 68 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 69 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 70 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 71 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 72 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 73 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 74 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 75 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 76 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 77 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 78 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 79 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 80 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 81 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 82 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 83 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 84 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 85 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 86 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 87 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 88 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 89 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 90 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 91 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 92 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 93 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 94 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 95 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 96 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 97 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 98 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 99 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 100 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 101 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 102 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 103 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 104 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 105 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 106 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 107 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 108 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 109 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 110 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 111 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 112 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 113 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 114 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 115 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 116 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 117 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 118 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 119 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 120 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 121 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 122 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 123 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 124 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 125 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 126 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 127 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 128 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 129 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 130 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 131 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 132 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 133 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 134 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 135 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 136 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 137 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 138 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 139 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 140 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 141 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 142 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 143 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 144 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 145 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 146 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 147 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 148 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 149 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 150 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 151 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 152 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 153 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 154 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 155 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 156 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 157 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 158 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 159 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 160 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 161 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 162 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 163 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 164 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 165 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 166 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 167 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 168 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 169 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 170 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 171 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 172 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 173 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 174 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 175 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 176 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 177 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 178 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 179 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 180 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 181 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 182 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 183 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 184 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 185 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 186 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 187 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 188 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 189 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 190 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 191 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 192 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 193 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 194 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 195 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 196 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 197 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 198 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 199 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 200 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 201 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 202 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 203 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 204 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 205 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 206 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 207 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 208 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 209 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 210 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 211 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 212 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 213 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 214 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 215 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 216 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 217 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 218 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 219 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 220 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 221 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 222 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 223 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 224 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 225 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 226 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 227 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 228 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 229 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 230 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 231 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 232 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 233 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 234 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 235 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 236 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 237 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 238 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 239 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 240 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 241 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 242 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 243 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 244 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 245 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 246 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 247 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 248 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 249 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 250 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 251 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 252 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 253 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 254 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 255 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 256 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 257 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 258 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 259 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 260 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 261 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 262 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 263 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 264 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 265 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 266 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 267 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 268 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 269 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 270 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 271 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 272 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 273 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 274 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 275 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 276 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 277 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 278 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 279 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 280 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 281 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 282 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 283 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 284 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 285 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 286 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 287 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 288 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 289 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 290 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 291 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 292 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 293 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 294 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 295 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 296 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 297 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 298 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 299 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 300 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 301 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 302 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 303 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 304 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 305 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 306 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 307 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 308 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 309 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 310 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 311 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 312 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 313 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 314 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 315 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 316 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 317 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 318 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 319 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 320 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 321 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 322 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 323 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 324 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 325 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 326 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 327 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 328 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 329 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 330 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 331 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 332 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 333 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 334 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 335 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 336 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 337 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 338 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 339 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 340 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 341 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 342 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 343 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 344 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 345 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 346 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 347 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 348 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 349 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 350 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 351 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 352 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 353 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 354 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 355 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 356 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 357 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 358 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 359 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 360 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 361 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 362 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 363 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 364 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 365 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 366 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 367 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 368 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 369 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 370 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 371 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 372 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 373 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 374 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 375 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 376 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 377 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 378 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 379 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 380 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 381 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 382 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 383 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 384 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 385 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 386 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 387 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 388 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 389 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 390 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 391 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 392 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 393 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 394 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 395 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 396 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 397 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 398 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 399 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 400 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 401 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 402 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 403 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 404 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 405 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 406 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 407 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 408 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 409 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 410 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 411 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 412 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 413 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 414 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 415 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 416 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 417 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 418 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 419 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 420 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 421 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 422 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 423 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 424 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 425 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 426 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 427 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 428 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 429 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 430 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 431 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 432 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 433 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 434 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 435 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 436 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 437 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 438 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 439 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 440 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 441 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 442 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 443 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 444 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 445 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 446 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 447 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 448 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 449 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 450 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 451 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 452 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 453 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 454 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 455 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 456 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 457 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 458 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 459 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 460 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 461 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 462 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 463 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 464 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 465 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 466 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 467 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 468 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 469 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 470 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 471 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 472 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 473 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 474 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 475 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 476 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 477 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 478 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 479 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 480 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 481 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 482 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 483 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 484 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 485 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 486 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 487 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 488 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 489 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 490 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 491 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 492 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 493 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 494 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 495 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 496 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 497 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 498 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 499 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 500 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 501 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 502 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 503 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 504 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 505 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 506 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 507 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 508 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 509 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 510 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 511 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 512 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 513 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 514 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 515 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 516 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 517 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 518 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 519 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 520 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 521 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 522 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 523 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 524 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 525 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 526 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 527 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 528 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 529 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 530 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 531 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 532 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 533 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 534 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 535 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 536 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 537 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 538 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 539 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 540 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 541 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 542 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 543 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 544 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 545 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 546 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 547 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 548 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 549 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 550 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 551 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 552 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 553 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 554 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 555 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 556 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 557 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 558 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 559 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 560 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 561 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 562 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 563 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 564 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 565 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 566 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 567 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 568 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 569 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
