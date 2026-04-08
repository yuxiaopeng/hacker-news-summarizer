# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-08.md)

*最后自动更新时间: 2026-04-08 18:34:34*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 2 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 3 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 4 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 5 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 6 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 7 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 8 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 9 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 10 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 11 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 12 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 13 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 14 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 15 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 16 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 17 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 18 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 19 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 20 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 21 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 22 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 23 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 24 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 25 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 26 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 27 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 28 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 29 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 30 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 31 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 32 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 33 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 34 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 35 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 36 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 37 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 38 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 39 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 40 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 41 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 42 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 43 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 44 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 45 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 46 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 47 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 48 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 49 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 50 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 51 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 52 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 53 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 54 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 55 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 56 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 57 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 58 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 61 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 62 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 63 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 64 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 65 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 66 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 67 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 68 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 69 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 70 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 71 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 72 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 73 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 74 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 75 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 76 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 77 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 78 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 79 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 80 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 81 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 82 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 83 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 84 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 85 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 86 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 87 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 88 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 89 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 90 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 91 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 92 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 93 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 94 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 95 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 96 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 97 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 98 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 99 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 100 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 101 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 102 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 103 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 104 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 105 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 106 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 107 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 108 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 109 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 110 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 111 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 112 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 113 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 114 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 115 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 116 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 117 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 118 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 119 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 120 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 121 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 122 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 123 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 124 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 125 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 126 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 127 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 128 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 129 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 130 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 131 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 132 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 133 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 134 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 135 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 136 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 137 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 138 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 139 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 140 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 141 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 142 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 143 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 144 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 145 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 146 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 147 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 148 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 149 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 150 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 151 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 152 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 153 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 154 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 155 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 156 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 157 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 158 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 159 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 160 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 161 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 162 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 163 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 164 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 165 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 166 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 167 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 168 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 169 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 170 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 171 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 172 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 173 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 174 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 175 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 176 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 177 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 178 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 179 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 180 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 181 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 182 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 183 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 184 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 185 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 186 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 187 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 188 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 189 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 190 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 191 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 192 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 193 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 194 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 195 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 196 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 197 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 198 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 199 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 200 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 201 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 202 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 203 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 204 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 205 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 206 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 207 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 208 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 209 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 210 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 211 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 212 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 213 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 214 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 215 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 216 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 217 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 218 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 219 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 220 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 221 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 222 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 223 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 224 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 225 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 226 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 227 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 228 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 229 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 230 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 231 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 232 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 233 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 234 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 235 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 236 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 237 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 238 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 239 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 240 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 241 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 242 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 243 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 244 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 245 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 246 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 247 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 248 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 249 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 250 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 251 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 252 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 253 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 254 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 255 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 256 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 257 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 258 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 259 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 260 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 261 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 262 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 263 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 264 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 265 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 266 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 267 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 268 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 269 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 270 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 271 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 272 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 273 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 274 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 275 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 276 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 277 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 278 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 279 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 280 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 281 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 282 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 283 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 284 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 285 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 286 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 287 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 288 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 289 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 290 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 291 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 292 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 293 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 294 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 295 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 296 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 297 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 298 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 299 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 300 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 301 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 302 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 303 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 304 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 305 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 306 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 307 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 308 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 309 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 310 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 311 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 312 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 313 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 314 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 315 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 316 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 317 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 318 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 319 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 320 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 321 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 322 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 323 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 324 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 325 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 326 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 327 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 328 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 329 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 330 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 331 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 332 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 333 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 334 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 335 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 336 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 337 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 338 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 339 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 340 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 341 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 342 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 343 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 344 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 345 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 346 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 347 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 348 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 349 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 350 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 351 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 352 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 353 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 354 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 355 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 356 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 357 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 358 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 359 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 360 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 361 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 362 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 363 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 364 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 365 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 366 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 367 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 368 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 369 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 370 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 371 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 372 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 373 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 374 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 375 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 376 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 377 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 378 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 379 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 380 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 381 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 382 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 383 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 384 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
