# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-27.md)

*最后自动更新时间: 2026-06-27 18:34:17*
## 1. 匿名 GitHub 账号正大批量发布未公开的零日漏洞

**原文标题**: Anonymous GitHub account mass-dropping undisclosed 0-days

**原文链接**: [https://github.com/bikini/exploitarium](https://github.com/bikini/exploitarium)

一名匿名研究人员（Discord 账号 @ashdfrkl）发布了一个名为 **“Exploitarium”** 的 GitHub 仓库，该仓库是一个整合了漏洞研究和未公开零日漏洞概念验证（PoC）漏洞利用的综合存档库。

该仓库作为中心枢纽，汇集了此前独立的项目以及日期标注为 2026 年 6 月的新“直接录入”研究。该集合涵盖了广泛的高知名度软件和协议，包括：
*   **浏览器与媒体：** Firefox（私密 URL 外泄）、VLC（VP9 崩溃）和 FFmpeg。
*   **开发与基础设施：** Docker（目标逃逸）、Ghidra 12.1.2（RCE/ACE）、Gitea 和 ImageMagick。
*   **网络与系统：** Nmap（IPv6 回绕）、libssh2、OpenVPN 和 c-ares（UAF）。
*   **语言与工具：** PHP 8.5.7（Soap RCE）、7zip 和 RustDesk。

创建者利用 Git blob ID 匹配来验证整合数据的完整性，确保来自 12 个原始仓库的 96 条跟踪条目与其源代码保持完全一致。

尽管“大规模投放”未公开漏洞具有重大的安全隐患，但作者将该项目定义为“基于诚信的公开披露漏洞研究”。仓库中包含严厉的“滥用”警告，反对恶意使用，并声明该项目的目标是培养对网络安全的兴趣。该研究人员鼓励社区分享该仓库，并通过 Discord 与其联系进行协作，并称公众参与是其持续披露的主要动力。

---

## 2. OpenRA

**原文标题**: OpenRA

**原文链接**: [https://www.openra.net/](https://www.openra.net/)

生成摘要时出错

---

## 3. DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文标题**: DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文链接**: [https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

生成摘要时出错

---

## 4. 可疑的不连续性 (2020)

**原文标题**: Suspicious Discontinuities (2020)

**原文链接**: [https://danluu.com/discontinuities/](https://danluu.com/discontinuities/)

《可疑的不连续性》（Suspicious Discontinuities）探讨了政策、社会系统和技术中的剧烈阈值如何产生扭曲的激励机制和“非自然”的数据分布。当输入的微小变化导致输出发生不成比例的变化时，就会出现这些“断崖”，促使个人为了规避惩罚或获取利益而“钻系统的空子”。

作者提供了该现象的几个关键案例：
*   **经济与教育政策：** 奥巴马医改（ACA）补贴和佩尔助学金（Pell Grants）的硬性收入门槛，使得个人为了保持在阈值以下以增加总可支配收入，而故意损失金钱（通常通过高风险期权交易）在财务上变得合理。
*   **科学研究：** $p < 0.05$ 的统计显著性标准导致了“p-hacking”，即研究人员通过操纵数据或选择性发表结果来跨越“显著性”红线。
*   **教育：** 波兰的考试数据显示，在及格线位置出现了可疑的得分峰值，这表明阅卷者会为略低于门槛的学生“找分”。
*   **体育：** 青少年年龄分组产生了“相对年龄效应”，即在日历年年初出生的孩子更有可能成功，因为在选拔时他们比同龄人身体发育更成熟。
*   **法律与政治：** 量刑法律导致毒品指控在强制性最低刑期阈值处出现激增，而选举舞弊往往表现为投票率数据在整数处出现“非自然”的峰值。

作者认为，这些界限分明的规则通常是“次优”的，会导致系统性的低效。为了缓解这些问题，文章建议用**渐进式退出**（slow phase-outs）或连续分布来取代剧烈的不连续性，从而平滑激励机制，减轻操纵结果或行为的压力。

---

## 5. Fintech Engineering Handbook

**原文标题**: Fintech Engineering Handbook

**原文链接**: [https://w.pitula.me/fintech-engineering-handbook/](https://w.pitula.me/fintech-engineering-handbook/)

The **Fintech Engineering Handbook** provides a framework for building reliable financial systems, centered on three core principles: **no invented data** (preventing duplicates), **no lost data** (ensuring full persistence), and **no trust** (verifying all internal and external inputs).

**Representing and Moving Money**
The handbook emphasizes precision, strictly forbidding floating-point types due to unpredictable rounding errors. Instead, it recommends arbitrary-precision decimals or minor-unit integers. Rounding must be an explicit business decision, handled at boundaries to avoid "minting" or losing money. Furthermore, amounts should always be paired with currencies in a single data structure to prevent invalid cross-currency arithmetic. Foreign exchange (FX) rates should be treated as directional and time-sensitive, with the data source explicitly recorded.

**The Ledger and Recording**
Financial records should utilize **double-entry bookkeeping**, where money is moved between accounts rather than just updated. In this model, balances are derived from a history of immutable, append-only entries. The system must distinguish between different timestamps: **Value time** (when it happened), **Booking time** (when it was recorded), and **Settlement time** (when funds moved).

**Auditability and Integrity**
To satisfy regulatory requirements, systems must maintain a comprehensive **audit trail** documenting the "what, when, who, and why" of every change. **Event sourcing** is highlighted as a premier pattern for this, as it derives the system state directly from an immutable log of events, ensuring the trail never drifts from reality. Finally, the handbook stresses **immutability**, suggesting that financial records should be protected by database permissions or cryptographic checksums to ensure they remain tamper-evident and verifiable.

---

## 6. AI 正在设计人类甚至无法想象的无线电芯片

**原文标题**: AI Is Designing Radio Chips That Humans Couldn't Even Imagine

**原文链接**: [https://spectrum.ieee.org/ai-radio-chip-design](https://spectrum.ieee.org/ai-radio-chip-design)

Traditional radio-frequency integrated circuit (RFIC) design is an essential but notoriously difficult "dark art" that governs the functionality of 5G, satellite communications, and autonomous vehicles. Unlike standard computing chips, RFICs require the complex balancing of electromagnetic fields, thermodynamics, and physical constraints. This artisanal process has historically relied on human intuition and existing design templates, creating a massive bottleneck in wireless technology development.

Researchers at Princeton University are breaking this bottleneck by using AI to design RFICs from scratch. By employing reinforcement learning and inverse design, the AI is freed from the constraints of human aesthetics and intelligibility. Much like AlphaGo Zero, which learned to play Go through self-play rather than human examples, this AI explores the vast design space to discover novel circuit topologies and electromagnetic structures that traditional designers would never conceive.

The results are transformative:
*   **Performance:** AI-generated chips, which often resemble abstract art rather than symmetrical circuits, frequently outperform state-of-the-art human designs.
*   **Efficiency:** The AI can conceive working designs in a fraction of the time, reducing the design cycle by orders of magnitude.
*   **Innovation:** Using diffusion models, researchers can rapidly generate novel RF layouts that optimize for specific performance goals while managing complex physical trade-offs like impedance matching.

The author concludes that the future of RFIC design lies in shifting away from artisanal manual labor toward algorithmic synthesis. To fully realize this potential, the industry must develop large, shared datasets and open ecosystems, allowing AI to master universal electromagnetic and circuit behaviors. This transition is critical for the next generation of wireless technology, including 6G and beyond.

---

## 7. Post-Mythos Cybersecurity: Keep calm and carry on

**原文标题**: Post-Mythos Cybersecurity: Keep calm and carry on

**原文链接**: [https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/)

生成摘要时出错

---

## 8. Supabase (YC S20) Is Hiring for Multigres

**原文标题**: Supabase (YC S20) Is Hiring for Multigres

**原文链接**: [https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228](https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228)

生成摘要时出错

---

## 9. Zuckerberg's Increasingly Bizarre War on Whistleblowers

**原文标题**: Zuckerberg's Increasingly Bizarre War on Whistleblowers

**原文链接**: [https://pluralistic.net/2026/06/27/zuckerstreisand-2/](https://pluralistic.net/2026/06/27/zuckerstreisand-2/)

生成摘要时出错

---

## 10. If you can't hold it, you don't own it

**原文标题**: If you can't hold it, you don't own it

**原文链接**: [https://dervis.de/physical/](https://dervis.de/physical/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 2 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 3 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 4 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 5 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 6 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 7 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 8 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 9 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 10 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 11 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 12 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 13 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 14 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 15 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 16 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 17 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 18 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 19 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 20 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 21 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 22 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 23 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 24 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 25 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 26 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 27 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 28 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 29 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 30 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 31 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 32 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 33 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 34 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 35 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 36 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 37 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 38 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 39 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 40 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 41 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 42 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 43 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 44 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 45 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 46 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 47 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 48 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 49 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 50 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 51 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 52 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 53 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 54 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 55 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 56 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 57 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 58 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 59 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 60 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 61 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 62 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 63 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 64 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 65 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 66 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 67 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 68 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 69 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 70 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 71 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 72 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 73 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 74 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 75 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 76 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 77 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 78 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 79 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 80 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 81 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 82 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 83 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 84 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 85 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 86 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 87 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 88 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 89 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 90 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 91 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 92 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 93 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 94 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 95 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 96 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 97 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 98 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 99 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 100 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 101 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 102 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 103 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 104 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 105 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 106 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 107 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 108 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 109 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 110 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 111 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 112 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 113 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 114 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 115 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 116 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 117 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 118 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 119 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 120 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 121 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 122 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 123 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 124 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 125 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 126 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 127 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 128 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 129 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 130 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 131 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 132 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 133 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 134 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 135 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 136 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 137 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 138 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 139 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 140 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 141 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 142 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 143 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 144 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 145 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 146 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 147 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 148 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 149 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 150 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 151 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 152 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 153 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 154 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 155 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 156 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 157 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 158 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 159 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 160 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 161 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 162 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 163 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 164 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 165 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 166 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 167 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 168 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 169 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 170 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 171 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 172 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 173 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 174 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 175 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 176 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 177 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 178 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 179 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 180 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 181 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 182 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 183 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 184 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 185 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 186 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 187 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 188 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 189 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 190 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 191 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 192 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 193 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 194 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 195 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 196 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 197 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 198 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 199 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 200 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 201 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 202 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 203 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 204 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 205 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 206 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 207 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 208 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 209 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 210 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 211 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 212 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 213 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 214 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 215 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 216 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 217 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 218 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 219 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 220 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 221 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 222 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 223 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 224 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 225 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 226 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 227 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 228 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 229 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 230 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 231 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 232 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 233 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 234 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 235 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 236 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 237 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 238 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 239 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 240 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 241 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 242 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 243 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 244 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 245 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 246 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 247 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 248 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 249 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 250 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 251 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 252 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 253 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 254 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 255 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 256 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 257 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 258 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 259 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 260 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 261 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 262 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 263 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 264 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 265 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 266 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 267 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 268 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 269 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 270 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 271 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 272 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 273 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 274 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 275 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 276 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 277 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 278 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 279 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 280 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 281 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 282 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 283 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 284 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 285 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 286 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 287 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 288 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 289 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 290 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 291 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 292 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 293 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 294 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 295 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 296 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 297 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 298 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 299 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 300 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 301 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 302 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 303 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 304 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 305 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 306 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 307 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 308 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 309 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 310 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 311 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 312 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 313 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 314 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 315 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 316 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 317 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 318 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 319 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 320 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 321 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 322 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 323 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 324 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 325 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 326 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 327 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 328 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 329 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 330 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 331 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 332 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 333 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 334 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 335 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 336 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 337 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 338 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 339 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 340 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 341 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 342 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 343 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 344 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 345 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 346 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 347 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 348 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 349 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 350 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 351 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 352 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 353 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 354 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 355 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 356 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 357 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 358 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 359 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 360 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 361 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 362 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 363 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 364 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 365 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 366 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 367 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 368 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 369 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 370 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 371 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 372 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 373 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 374 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 375 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 376 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 377 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 378 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 379 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 380 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 381 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 382 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 383 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 384 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 385 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 386 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 387 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 388 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 389 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 390 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 391 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 392 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 393 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 394 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 395 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 396 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 397 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 398 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 399 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 400 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 401 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 402 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 403 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 404 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 405 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 406 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 407 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 408 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 409 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 410 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 411 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 412 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 413 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 414 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 415 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 416 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 417 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 418 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 419 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 420 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 421 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 422 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 423 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 424 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 425 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 426 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 427 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 428 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 429 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 430 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 431 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 432 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 433 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 434 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 435 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 436 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 437 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 438 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 439 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 440 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 441 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 442 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 443 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 444 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 445 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 446 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 447 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 448 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 449 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 450 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 451 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 452 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 453 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 454 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 455 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 456 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 457 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 458 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 459 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 460 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 461 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 462 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 463 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 464 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
