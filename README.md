# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-29.md)

*最后自动更新时间: 2026-09-29 21:40:48*
## 1. 美国邮政调查员关停销售伪造邮资标签的网站。

**原文标题**: U.S. postal inspectors shut down website selling counterfeit postage labels

**原文链接**: [https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/)

美国邮政检验局（USPIS）及联邦合作伙伴机构已查封域名 LabelsBank.com，并起诉了该网站运营商——33岁的巴基斯坦男子法希姆·阿克拉姆（Faheem Akram），指控其策划了一场大规模的伪造邮资计划。

根据法庭记录，阿克拉姆利用该非法网站向5000多名客户销售了超过510万张伪造的美国邮政署（USPS）运输标签。据称，该网站对每张标签收取约2美元的统一费用，且不限包裹的目的地、尺寸或重量。这一欺诈行为导致美国邮政署估计损失了超过1.26亿美元的收入。

阿克拉姆被控串谋欺诈美国、制造并销售伪造邮资以及电信欺诈。在起诉之后，法院下令授权立即查封并关闭该网站。

美国检察官杰森·A·雷丁·基诺内斯（Jason A. Reding Quiñones）和迈阿密分局首席邮政检验员布拉迪斯米尔·罗霍（Bladismir Rojo）强调了该欺诈行为的规模，并表示联邦政府将追捕针对美国消费者和邮政系统的国际犯罪者。尽管该网站已被关停且相关起诉已经提起，但官员们提醒公众，在法庭证明其有罪之前，被告应被推定为无罪。

---

## 2. Tcl/Tk 9.1 发布

**原文标题**: Tcl/Tk 9.1 Released

**原文链接**: [https://www.tcl-lang.org/software/tcltk/9.1.html](https://www.tcl-lang.org/software/tcltk/9.1.html)

Tcl/Tk 9.1.0 计划于 2026 年 9 月下旬发布，是继 Tcl/Tk 9.0 之后的下一个开发阶段。此次更新为核心语言和图形工具包引入了重大新特性、命令增强以及性能优化。

**Tcl 9.1 亮点：**
核心 Tcl 语言新增了多个命令，包括用于规范化的 `unicode`、用于高分辨率单调时钟功能的 `timer`，以及用于列表项选择的 `lfilter`。它还为 `subst` 和 `switch` 命令引入了新选项，并将许多 C99 数学例程整合为标准 `expr` 函数。开发者将受益于用于 Unicode 处理和列表操作的新 C API 例程，以及针对大型列表的内存效率提升和扩展的 64 位支持。值得注意的是，应用程序现在需要通过 `Tcl_FindExecutable` 或 `TclZipfs_AppHook` 进行特定初始化。特定平台的更新包括 macOS 上不区分大小写的文件系统路径，以及 Windows 上修订后的搜索机制。

**Tk 9.1 亮点：**
Tk 工具包专注于现代化和无障碍化，引入了屏幕阅读器支持和初步的双向/从右至左（RTL）文本处理能力。新特性包括 `ttk::toggleswitch` 组件、`tk attribtable` 命令以及标签（label）上的旋转文本支持。UI 改进包括优化的列表框选择颜色、更好的负向屏幕距离处理，以及针对 Aqua 平台的 `send` 命令修订。为了精简工具包，已移除对 Windows XP 外观的过时支持。

总体而言，Tcl/Tk 9.1 旨在为开发者提供一个更稳健、更易用且更高效的基础，同时扩展该框架在现代硬件和国际化方面的能力。

---

## 3. GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文标题**: GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文链接**: [https://openai.com/index/introducing-gpt-6-1-sol/](https://openai.com/index/introducing-gpt-6-1-sol/)

生成摘要时出错

---

## 4. 德里如何将电力损耗从50%降至5%

**原文标题**: How Delhi cut electricity loss from 50 to 5 percent

**原文链接**: [https://spectrum.ieee.org/delhi-electricity-loss](https://spectrum.ieee.org/delhi-electricity-loss)

生成摘要时出错

---

## 5. PS5 Relapse 漏洞利用

**原文标题**: PS5 Relapse Exploit

**原文链接**: [https://github.com/ntfargo/Relapse-Exploit](https://github.com/ntfargo/Relapse-Exploit)

**PS5 Relapse Exploit** 是一款专为固件版本在 **7.00 至 13.60** 之间的 PlayStation 5 主机设计的安全研究工具。该漏洞利用程序由包括 ntfargo 和 TheFlow 在内的贡献者团队开发，可实现内核读/写访问并执行自定义载荷。

**技术细节**
该漏洞利用采用两阶段链条：
1.  **浏览器阶段：** 利用 JavaScriptCore (JSC) 信息泄露和结构化克隆对象池不匹配来损坏类型化数组。
2.  **内核阶段：** 结合地址泄露与 `aio_multi_wait` 释放后重用 (UAF) 竞态条件，以建立内核读/写权限。

**使用与稳定性**
用户可以通过将主机的首选 DNS 设置为 `45.56.67.85` 或在本地托管相关文件来执行该漏洞利用程序。成功触发后，一个 ELF 加载器将在 **9021** 端口激活。文档指出该漏洞利用具有不稳定性：Webkit 阶段可能需要多次刷新浏览器，而内核阶段可能导致系统挂起或“内核恐慌 (kernel panic)”，届时需要完整重启主机。

**风险与免责声明**
本项目严格仅用于教育和安全研究目的。使用该漏洞利用程序存在重大风险，包括系统不稳定、潜在的数据丢失以及被索尼封禁账号的风险。本软件按“原样”提供而不作任何担保，维护者不支持盗版或未经授权访问商业设备的行为。

---

## 6. 尼古拉斯·波尔森（Nicholas Polson）在2026年（截至目前）已发表了258篇学术论文。

**原文标题**: Nicholas Polson has authored 258 academic papers in 2026 (so far)

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/08/27/258/](https://statmodeling.stat.columbia.edu/2026/08/27/258/)

无法访问文章链接。

---

## 7. DraftKings正利用人工智能针对嗜赌成瘾者进行行为定向。

**原文标题**: DraftKings Is Using AI to Behaviorally Target Chronic Gamblers

**原文链接**: [https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising)

电子前哨基金会（EFF）报告称，DraftKings 正利用人工智能和机器学习来识别并锁定“处于亏损状态的”赌客。通过分析内部投注记录，DraftKings 训练模型以寻找最有可能输钱的客户，并向其发送个性化的促销信息，诱导其重返平台。这种做法专门剥削“问题赌客”，将公司利润置于弱势个体的福祉之上。

EFF 强调了这种做法存在的几个关键问题：

*   **人工智能驱动的剥削：** 人工智能通过高速处理海量数据集，放大了行为广告的危害。由于人工智能运作如同“黑箱”，它会促使公司收集尽可能多的数据，以优化其模型。
*   **监控风险：** 为行为广告收集的数据经常流入“监控产业”。最初为广告收集的信息通常被出售给保险公司、银行以及美国移民及海关执法局（ICE）和美国海关及边境保护局（CBP）等政府机构，用于调查目的。
*   **第一方数据漏洞：** DraftKings 主要使用直接从用户处收集的“第一方数据”。EFF 认为，仅针对第三方数据共享的政策方案是不够的；要制止这种掠夺性的定向投放，必须禁止所有的行为广告。

最终，EFF 主张，禁止行为广告是消除大规模数据收集动机的唯一途径。他们鼓励用户利用隐私资源（例如其“监控自卫”项目）来保护自己免受这些不断演变的数字威胁。

---

## 8. NAND-16: a computer built from 277,248 NAND gates

**原文标题**: NAND-16: a computer built from 277,248 NAND gates

**原文链接**: [https://somethingbig.ai/computer](https://somethingbig.ai/computer)

**NAND-16** is a project that demonstrates the power of universal logic by constructing a fully functional 16-bit computer using only a single type of component: the **NAND gate**. Comprising exactly **277,248 gates**, the project serves as a massive-scale implementation of the "Nand to Tetris" philosophy, showing how complex computational systems emerge from the simplest possible building blocks.

**Key Features and Technical Details:**

*   **16-bit Architecture:** The computer operates on 16-bit data and addresses, allowing it to handle a level of complexity far beyond simple logic demonstrations.
*   **Universal Logic:** The project proves the principle of functional completeness, where every necessary component—including the Arithmetic Logic Unit (ALU), registers, program counter, and memory management—is synthesized entirely from NAND gates.
*   **Scale and Complexity:** With over a quarter-million gates, the design represents a significant engineering feat, bridging the gap between theoretical computer science and practical hardware architecture.
*   **Educational Value:** The project demystifies the layers of abstraction in modern computing. It provides a transparent view of how binary signals are transformed into executable instructions, showing the direct lineage from electricity to high-level logic.

In summary, NAND-16 is a comprehensive exercise in digital logic design. It illustrates that with enough scale and proper organization, the most basic unit of digital electronics can be used to build a machine capable of general-purpose computing, providing a profound look at the foundational mechanics of the digital age.

---

## 9. Web与移动端对话式AI智能体的隐私分析 [pdf]

**原文标题**: A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]

**原文链接**: [https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)

This article provides a comprehensive evaluation of the privacy landscapes surrounding popular Large Language Model (LLM) platforms, specifically comparing their web-based interfaces with their mobile application counterparts. As conversational AI becomes integrated into daily life, the study investigates the extent to which these agents respect user data and adhere to privacy standards.

**Key Findings:**

*   **Platform Disparities:** The research highlights a significant "privacy gap" between web and mobile versions of the same AI agent. Mobile applications are generally more intrusive, frequently requesting extensive device permissions—such as precise location, microphone access, and contact lists—that are often unnecessary for the agent’s core functionality.
*   **Data Collection Practices:** Most agents collect a vast array of information, including chat histories, account metadata, and device identifiers. A primary concern identified is the use of "training data"; many providers are ambiguous about how they scrub Personally Identifiable Information (PII) before using user conversations to retrain future models.
*   **Third-Party Tracking:** The analysis reveals that mobile AI apps often integrate numerous third-party Software Development Kits (SDKs). These are used for analytics and advertising, leading to the silent transmission of user telemetry data to external domains, a practice less prevalent on "cleaner" web interfaces.
*   **Regulatory & Policy Lacunae:** The study finds that privacy policies are often written in vague, legalistic language that fails to provide users with clear "opt-out" mechanisms regarding data retention or model training.

**Conclusion:**
The authors conclude that the rapid deployment of conversational AI has outpaced current privacy protections. They advocate for "Privacy by Design," urging developers to implement stricter data minimization and providing users with more granular control over how their conversational data is stored and utilized. There is a call for regulators to establish standardized transparency requirements specifically tailored to generative AI.

---

## 10. Show HN: TurboGPT: train 22KiB transformer in 13s

**原文标题**: Show HN: TurboGPT: train 22KiB transformer in 13s

**原文链接**: [https://github.com/lostmsu/TurboGPT](https://github.com/lostmsu/TurboGPT)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 2 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 3 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 4 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 5 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 6 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 7 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 8 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 9 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 10 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 11 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 12 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 13 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 14 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 15 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 16 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 17 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 18 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 19 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 20 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 21 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 22 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 23 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 24 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 25 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 26 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 27 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 28 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 29 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 30 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 31 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 32 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 33 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 34 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 35 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 36 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 37 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 38 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 39 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 40 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 41 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 42 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 43 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 44 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 45 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 46 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 47 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 48 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 49 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 50 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 51 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 52 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 53 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 54 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 55 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 56 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 57 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 58 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 59 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 60 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 61 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 62 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 63 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 64 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 65 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 66 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 67 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 68 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 69 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 70 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 71 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 72 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 73 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 74 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 75 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 76 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 77 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 78 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 79 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 80 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 81 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 82 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 83 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 84 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 85 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 86 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 87 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 88 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 89 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 90 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 91 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 92 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 93 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 94 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 95 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 96 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 97 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 98 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 99 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 100 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 101 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 102 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 103 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 104 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 105 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 106 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 107 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 108 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 109 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 110 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 111 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 112 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 113 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 114 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 115 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 116 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 117 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 118 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 119 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 120 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 121 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 122 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 123 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 124 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 125 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 126 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 127 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 128 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 129 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 130 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 131 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 132 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 133 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 134 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 135 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 136 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 137 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 138 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 139 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 140 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 141 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 142 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 143 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 144 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 145 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 146 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 147 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 148 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 149 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 150 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 151 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 152 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 153 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 154 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 155 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 156 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 157 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 158 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 159 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 160 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 161 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 162 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 163 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 164 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 165 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 166 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 167 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 168 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 169 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 170 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 171 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 172 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 173 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 174 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 175 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 176 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 177 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 178 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 179 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 180 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 181 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 182 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 183 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 184 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 185 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 186 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 187 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 188 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 189 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 190 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 191 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 192 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 193 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 194 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 195 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 196 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 197 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 198 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 199 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 200 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 201 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 202 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 203 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 204 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 205 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 206 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 207 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 208 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 209 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 210 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 211 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 212 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 213 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 214 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 215 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 216 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 217 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 218 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 219 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 220 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 221 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 222 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 223 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 224 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 225 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 226 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 227 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 228 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 229 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 230 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 231 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 232 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 233 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 234 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 235 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 236 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 237 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 238 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 239 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 240 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 241 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 242 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 243 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 244 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 245 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 246 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 247 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 248 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 249 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 250 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 251 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 252 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 253 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 254 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 255 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 256 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 257 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 258 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 259 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 260 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 261 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 262 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 263 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 264 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 265 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 266 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 267 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 268 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 269 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 270 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 271 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 272 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 273 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 274 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 275 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 276 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 277 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 278 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 279 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 280 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 281 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 282 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 283 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 284 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 285 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 286 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 287 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 288 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 289 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 290 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 291 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 292 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 293 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 294 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 295 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 296 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 297 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 298 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 299 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 300 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 301 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 302 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 303 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 304 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 305 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 306 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 307 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 308 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 309 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 310 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 311 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 312 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 313 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 314 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 315 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 316 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 317 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 318 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 319 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 320 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 321 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 322 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 323 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 324 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 325 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 326 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 327 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 328 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 329 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 330 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 331 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 332 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 333 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 334 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 335 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 336 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 337 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 338 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 339 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 340 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 341 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 342 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 343 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 344 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 345 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 346 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 347 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 348 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 349 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 350 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 351 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 352 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 353 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 354 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 355 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 356 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 357 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 358 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 359 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 360 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 361 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 362 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 363 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 364 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 365 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 366 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 367 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 368 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 369 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 370 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 371 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 372 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 373 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 374 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 375 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 376 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 377 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 378 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 379 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 380 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 381 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 382 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 383 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 384 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 385 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 386 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 387 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 388 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 389 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 390 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 391 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 392 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 393 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 394 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 395 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 396 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 397 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 398 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 399 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 400 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 401 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 402 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 403 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 404 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 405 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 406 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 407 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 408 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 409 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 410 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 411 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 412 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 413 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 414 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 415 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 416 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 417 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 418 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 419 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 420 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 421 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 422 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 423 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 424 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 425 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 426 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 427 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 428 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 429 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 430 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 431 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 432 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 433 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 434 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 435 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 436 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 437 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 438 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 439 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 440 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 441 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 442 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 443 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 444 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 445 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 446 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 447 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 448 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 449 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 450 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 451 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 452 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 453 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 454 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 455 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 456 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 457 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 458 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 459 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 460 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 461 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 462 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 463 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 464 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 465 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 466 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 467 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 468 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 469 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 470 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 471 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 472 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 473 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 474 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 475 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 476 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 477 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 478 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 479 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 480 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 481 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 482 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 483 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 484 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 485 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 486 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 487 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 488 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 489 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 490 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 491 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 492 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 493 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 494 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 495 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 496 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 497 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 498 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 499 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 500 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 501 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 502 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 503 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 504 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 505 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 506 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 507 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 508 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 509 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 510 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 511 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 512 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 513 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 514 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 515 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 516 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 517 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 518 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 519 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 520 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 521 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 522 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 523 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 524 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 525 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 526 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 527 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 528 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 529 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 530 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 531 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 532 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 533 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 534 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 535 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 536 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 537 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 538 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 539 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 540 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 541 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 542 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 543 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 544 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 545 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 546 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 547 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 548 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 549 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 550 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 551 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 552 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 553 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 554 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 555 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 556 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
