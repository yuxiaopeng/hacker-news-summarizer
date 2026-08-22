# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-22.md)

*最后自动更新时间: 2026-08-22 17:49:02*
## 1. 十一实验室、十二实验室、十三实验室

**原文标题**: ElevenLabs, TwelveLabs, ThirteenLabs

**原文链接**: [https://quantumi.sh/public/labs.html](https://quantumi.sh/public/labs.html)

这篇文章《ElevenLabs, TwelveLabs, ThirteenLabs》探讨了当前主导 AI 初创领域的那种重复且序列化的命名趋势。作者指出，采用“[数字] Labs”格式的公司正在激增，并重点关注了 ElevenLabs（语音合成）和 Twelve Labs（视频理解）的崛起。

文章的核心观点包括：

*   **数字序列化：** 作者注意到，虽然 ElevenLabs 和 Twelve Labs 最为知名，但这一模式已渐趋拥挤。这种趋势已扩展到 Thirteen Labs 以及占据 1 到 10 各个数字的各类初创公司。
*   **品牌原创性的匮乏：** 文章批评这种命名惯例是“低熵”且缺乏灵感的。它表明 AI 公司正背离具有创意的品牌身份，转而采用一种感觉像占位符般通用且公式化的名称。
*   **“Labs”的声望：** 作者讨论了“Labs”一词的历史分量，它最初与贝尔实验室等享誉盛名的工业研究中心相联系。在现代 AI 时代，这个后缀被用来暗示科学的严谨与创新，即便对于尚未发布产品的早期软件公司也是如此。
*   **市场饱和与混淆：** 这种遵循数字序列的做法，使这些公司面临产生无意关联的风险。作者暗示，在日益饱和的市场中，这种趋势让初创公司越来越难以实现差异化。

归根结底，这篇文章是对“通用 AI 审美”的一种评论——即技术飞速进步的讽刺之处在于，品牌命名的创意和独特的品牌叙事能力反而有所下降。

---

## 2. 对贾斯汀·比伯《Sorry》的康德式批判

**原文标题**: A Kantian Critique of "Sorry" by Justin Bieber

**原文链接**: [https://decodingvibes.com/blog/a-kantian-critique-of-sorry-by-justin-bieber/](https://decodingvibes.com/blog/a-kantian-critique-of-sorry-by-justin-bieber/)

《对贾斯汀·比伯〈Sorry〉的康德主义批判》一文将伊曼纽尔·康德的义务论伦理学应用于这首2015年热门金曲的歌词，以判定这位歌手道歉的道德有效性。作者认为，从康德的视角来看，比伯的道歉在伦理上是有缺陷的，因为它根源于自私自利而非道德义务。

核心批判基于康德的**绝对命令**，即个人行动所依据的准则应能成为普遍法则。作者指出，比伯反复询问“现在说抱歉是否为时已晚？”，这暗示道歉取决于其时机和成功的可能性。用康德的话说，这使道歉成为了一个“假言命令”——即为了实现特定结果（和解）而采取的行为，而非仅仅因为它是正确的事而履行的“绝对命令”。

此外，文章探讨了**人性公式**，该公式规定绝不应将他人仅仅视为实现目的的手段。作者认为，比伯将他的伴侣视为实现其情感救赎或缓解自身愧疚的手段。由于他的悔意似乎是由“挽回她”或平复自身情绪的欲望所驱动的，他未能尊重受害者作为人的自主权和内在价值。

最终，文章得出结论：比伯的《Sorry》代表了一种“功利主义”或“投机式”的道歉。从康德的角度来看，真正的道歉必须是无条件的，且由义务感驱动。通过将歉意建立在结果之上，比伯未能达到一个真正道德主体的标准。

---

## 3. A Friendly Introduction to Racket

**原文标题**: A Friendly Introduction to Racket

**原文链接**: [https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/)

生成摘要时出错

---

## 4. Munder Difflin – 运行克隆人办公室的智能体框架

**原文标题**: Munder Difflin – Agent harness to run an office of your clones

**原文链接**: [https://munderdiffl.in/](https://munderdiffl.in/)

**Munder Difflin** 是一个开源（MIT 许可）的代理框架，旨在创建个人的 AI “数字分身”以实现专业工作流的自动化。通过封装现有的 AI CLI 代理（如 Claude Code、Codex 和 Grok），该平台允许用户将任务委派给自己的数字版本，实现全天候运行。

**核心功能与特性：**
*   **工作流集成：** 该框架可捕捉用户的特定工具链、记忆和编码标准。这些上下文信息在分身之间共享，使它们能够利用用户的现有知识启动新任务。
*   **自主协作：** 分身之间可以使用端到端（E2E）加密进行通信。它们可以移交工作、回答技术问题并为队友扫清障碍——即使人类主人处于离线状态。
*   **本地优先的安全性：** 默认情况下，所有代码、密钥和个人上下文都保留在用户的本地机器（127.0.0.1）上。分身之间的通信经过加密，包括 Munder Difflin 在内的任何第三方都无法读取消息。
*   **多功能性：** 虽然设计初衷是服务于开发者（如 PR 审查、Bug 修复），但该系统可驱动任何支持 CLI 的工具，因此也适用于设计师、产品经理和销售团队。

**定价方案：**
*   **个人版 (Solo)：** 供单机本地使用，完全免费。
*   **云端版 (Cloud)：** 付费服务，提供专用沙箱虚拟机，确保分身在用户关闭电脑时仍能 24/7 运行。
*   **网络版 (Network)：** 面向团队的付费方案，支持端到端加密的分身间通讯和共享的企业知识库。
*   **创始支持者 (Founding Supporter)：** 一次性支付 20 美元，将用户名刻在数字“创始人墙”上。

最终，Munder Difflin 旨在将团队的集体知识转化为一个 24/7 全天候运行的“蜂群思维”，由 AI 代理处理常规的协调与执行工作，仅将最关键的决策提交给人类处理。

---

## 5. 新版 MCP 路线图

**原文标题**: The New MCP Roadmap

**原文链接**: [https://blog.modelcontextprotocol.io/posts/mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)

The Model Context Protocol (MCP) has released an updated roadmap focused on evolving the protocol for sophisticated agentic workloads. The roadmap identifies five key priority areas:

*   **Agentic Messaging Primitives:** Moving beyond simple request-response patterns, MCP is introducing support for long-running loops, server-initiated events (webhooks/channels), and streaming. This includes maturing the "Tasks" extension to allow better control over mid-flight work.
*   **HTTP-Native Transport Unification:** To simplify development, the protocol aims to unify all deployment modes—including local servers—on HTTP-native transport. This makes MCP servers easier to host and operate using standard API infrastructure.
*   **Agent Identity and Enterprise Security:** Shifting away from manual browser-based approvals, the roadmap prioritizes standardized agent-to-agent identity. This involves implementing Demonstrating Proof of Possession (DPoP), Workload Identity Federation, and OAuth standards to allow agents to securely act on behalf of users or other services.
*   **Improved Primitives:** The roadmap addresses challenges in tool calling by standardizing how results are returned. It also introduces "progressive discovery," allowing servers to reveal tools incrementally so that models aren't overwhelmed by large catalogs.
*   **SDK Developer Experience:** Recognizing that many developers now use AI agents to write MCP code, there is a renewed focus on API ergonomics, conformance, and high-quality documentation across all supported languages.

Finally, the roadmap outlines a prioritized process for Specification Enhancement Proposals (SEPs). Proposals aligned with these five areas will receive expedited review. Developers and organizations are encouraged to get involved by joining Working Groups, contributing to SDKs, or participating in the community Discord.

---

## 6. Z80：依然活跃的 70 年代微处理器 (2021)

**原文标题**: Z80 – The 1970s Microprocessor Still Alive (2021)

**原文链接**: [https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi](https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi)

Zilog公司于1976年发布的Z80微处理器，至今仍是计算机历史上最经久不衰且最具影响力的硬件之一。该处理器由Federico Faggin（Intel 4004和8080的架构师）领导的团队设计，旨在成为Intel 8080更强大、更高效且更易用的继任者。

其早期成功的关键因素在于对8080软件的向下兼容性，以及显著的硬件改进。与前代产品不同，Z80内置了DRAM刷新控制器，且仅需单一的5V电源供电，这极大地降低了制造商在系统设计上的复杂性和成本。

在20世纪70年代末和80年代，Z80成为了家用电脑革命的引擎。它驱动了诸如Radio Shack TRS-80和Sinclair ZX Spectrum等标志性机器，并作为CP/M操作系统的标准处理器。除了个人电脑，它在游戏行业也取得了巨大成功，为ColecoVision、世嘉Master System以及任天堂初代Game Boy（采用其修改版本）提供了动力。

截至2021年，Z80的传奇仍在延续。虽然它在PC市场最终被16位和32位架构所取代，但它从未真正停产。凭借低功耗、简单性以及庞大的软件库，Z80已成为嵌入式系统市场的支柱，广泛应用于从TI-83计算器到工业控制器和打印机的各类设备中。如今，Z80不仅被复古计算爱好者视为历史的象征，更被视为一种在问世数十年后依然具有商业价值的实用、活态的架构。

---

## 7. 消息人士称，Anthropic的IPO文件将把AI抵制列为风险因素。

**原文标题**: Anthropic IPO filing will show AI backlash as a risk factor, sources say

**原文链接**: [https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html](https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html)

Anthropic 正在筹备一场具有历史意义的 IPO，其估值可能达到约 2 万亿美元。据知情人士透露，该公司的招股书将把公众和政治层面针对人工智能及数据中心扩张日益增长的反弹列为主要风险因素。

尽管 Anthropic 目前在私募市场的估值已接近 1 万亿美元，且近期实现了 650 亿美元的年化营收，但其增长与算力规模的扩大密不可分。然而，公众情绪正在发生转变；盖洛普（Gallup）的一项调查显示，出于对失业和基础设施影响的担忧，70% 的美国人反对在当地建设数据中心。

在即将到来的中期选举前夕，这种反对声音已蔓延至政治领域。两党政客已开始回应选民的愤怒；例如，佛罗里达州共和党人拜伦·唐纳兹（Byron Donalds）提议对数据中心实施限制，而宾夕法尼亚州民主党州长乔什·夏皮罗（Josh Shapiro）近期签署了一项行政命令，对数据中心的开发设定了严苛的标准。

据悉，在与投资者的“试水”会议期间，Anthropic 管理层面临了关于这些基础设施障碍、开源模型竞争以及利润率压力的质疑。尽管存在这些风险，Anthropic 的募资规模预计仍将创下历史纪录，甚至可能超过埃隆·马斯克旗下 SpaceX 近期筹集的 857 亿美元。尽管法律、社会和政治阻力不断增加，该公司仍继续推动基础设施合作伙伴以“曲速”进行建设，以满足其 Claude 模型的需求。

---

## 8. 学习《Unix 分时系统》

**原文标题**: Learning about "The Unix Time-Sharing System"

**原文链接**: [https://playtechnique.io/long/the-unix-time-sharing-system.html](https://playtechnique.io/long/the-unix-time-sharing-system.html)

本文探讨了 Unix 操作系统的早期历史和设计哲学，重点围绕丹尼斯·里奇（Dennis Ritchie）和肯·汤普森（Ken Thompson）发表的里程碑式论文《Unix 分时系统》（The Unix Time-Sharing System）。

叙述中强调了 Unix 最初是如何作为肯·汤普森在贝尔实验室的一个个人项目开始的。在 AT&T 退出 Multics 项目后，汤普森利用一台“少有人用”的 PDP-7 计算机继续他关于磁盘吞吐量的研究。令人惊叹的是，趁家人外出之际，他在短短三周内便编写完成了包括编译器、编辑器、汇编器和加载器在内的核心组件。

文章很大一部分篇幅聚焦于 Unix 在技术上对 Multics 的摒弃。与 Multics 将所有数据和程序视为统一虚拟内存的“单级存储”不同，汤普森引入了 `open` 系统调用。这一创新将数据与程序分离，从而实现了更高效的顺序读取和更好的缓存管理。此外，作者还追溯了“shell 脚本”的词源，将其关联到 “comfiles” 和 “runcoms”，并解释说现代的 `/etc/rc` 规范其实是麻省理工学院（MIT）CTSS 系统中 “runcom” 文件的遗迹。

作者格温多林·詹姆斯（Gwendolyn James）在结尾强调，Unix 的成功并非一蹴而就，而是经过了六年的严谨打磨，才增长到 600 台的安装规模。她利用这段体现毅力与技术清晰度的历史，推介其针对 Linux 和基础设施工具的一对一导师服务，并鼓励读者研读 1974 年的原始论文，将其视为一封献给计算机社区的奠基性“情书”。

---

## 9. Show HN: Rotation via Double Reflection

**原文标题**: Show HN: Rotation via Double Reflection

**原文链接**: [https://static.laszlokorte.de/rotor-reflect/](https://static.laszlokorte.de/rotor-reflect/)

生成摘要时出错

---

## 10. Rust Glancer: Rust LSP using 100x less RAM

**原文标题**: Rust Glancer: Rust LSP using 100x less RAM

**原文链接**: [https://rust-glancer.github.io/blog/hello-world/](https://rust-glancer.github.io/blog/hello-world/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 2 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 3 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 4 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 5 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 6 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 7 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 8 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 9 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 10 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 11 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 12 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 13 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 14 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 15 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 16 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 17 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 18 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 19 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 20 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 21 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 22 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 23 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 24 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 25 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 26 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 27 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 28 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 29 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 30 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 31 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 32 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 33 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 34 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 35 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 36 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 37 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 38 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 39 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 40 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 41 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 42 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 43 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 44 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 45 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 46 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 47 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 48 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 49 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 50 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 51 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 52 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 53 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 54 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 55 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 56 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 57 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 58 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 59 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 60 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 61 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 62 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 63 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 64 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 65 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 66 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 67 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 68 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 69 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 70 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 71 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 72 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 73 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 74 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 75 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 76 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 77 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 78 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 79 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 80 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 81 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 82 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 83 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 84 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 85 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 86 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 87 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 88 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 89 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 90 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 91 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 92 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 93 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 94 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 95 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 96 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 97 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 98 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 99 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 100 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 101 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 102 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 103 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 104 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 105 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 106 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 107 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 108 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 109 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 110 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 111 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 112 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 113 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 114 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 115 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 116 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 117 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 118 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 119 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 120 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 121 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 122 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 123 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 124 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 125 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 126 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 127 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 128 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 129 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 130 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 131 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 132 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 133 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 134 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 135 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 136 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 137 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 138 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 139 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 140 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 141 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 142 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 143 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 144 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 145 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 146 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 147 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 148 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 149 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 150 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 151 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 152 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 153 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 154 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 155 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 156 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 157 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 158 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 159 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 160 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 161 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 162 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 163 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 164 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 165 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 166 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 167 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 168 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 169 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 170 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 171 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 172 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 173 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 174 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 175 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 176 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 177 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 178 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 179 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 180 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 181 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 182 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 183 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 184 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 185 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 186 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 187 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 188 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 189 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 190 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 191 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 192 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 193 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 194 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 195 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 196 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 197 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 198 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 199 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 200 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 201 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 202 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 203 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 204 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 205 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 206 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 207 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 208 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 209 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 210 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 211 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 212 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 213 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 214 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 215 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 216 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 217 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 218 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 219 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 220 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 221 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 222 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 223 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 224 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 225 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 226 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 227 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 228 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 229 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 230 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 231 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 232 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 233 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 234 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 235 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 236 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 237 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 238 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 239 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 240 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 241 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 242 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 243 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 244 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 245 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 246 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 247 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 248 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 249 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 250 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 251 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 252 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 253 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 254 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 255 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 256 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 257 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 258 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 259 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 260 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 261 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 262 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 263 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 264 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 265 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 266 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 267 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 268 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 269 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 270 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 271 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 272 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 273 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 274 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 275 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 276 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 277 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 278 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 279 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 280 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 281 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 282 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 283 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 284 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 285 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 286 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 287 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 288 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 289 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 290 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 291 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 292 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 293 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 294 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 295 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 296 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 297 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 298 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 299 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 300 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 301 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 302 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 303 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 304 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 305 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 306 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 307 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 308 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 309 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 310 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 311 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 312 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 313 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 314 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 315 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 316 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 317 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 318 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 319 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 320 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 321 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 322 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 323 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 324 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 325 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 326 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 327 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 328 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 329 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 330 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 331 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 332 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 333 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 334 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 335 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 336 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 337 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 338 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 339 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 340 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 341 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 342 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 343 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 344 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 345 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 346 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 347 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 348 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 349 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 350 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 351 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 352 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 353 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 354 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 355 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 356 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 357 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 358 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 359 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 360 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 361 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 362 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 363 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 364 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 365 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 366 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 367 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 368 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 369 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 370 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 371 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 372 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 373 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 374 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 375 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 376 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 377 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 378 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 379 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 380 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 381 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 382 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 383 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 384 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 385 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 386 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 387 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 388 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 389 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 390 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 391 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 392 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 393 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 394 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 395 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 396 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 397 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 398 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 399 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 400 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 401 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 402 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 403 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 404 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 405 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 406 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 407 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 408 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 409 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 410 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 411 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 412 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 413 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 414 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 415 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 416 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 417 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 418 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 419 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 420 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 421 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 422 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 423 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 424 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 425 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 426 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 427 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 428 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 429 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 430 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 431 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 432 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 433 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 434 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 435 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 436 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 437 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 438 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 439 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 440 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 441 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 442 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 443 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 444 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 445 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 446 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 447 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 448 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 449 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 450 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 451 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 452 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 453 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 454 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 455 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 456 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 457 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 458 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 459 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 460 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 461 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 462 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 463 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 464 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 465 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 466 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 467 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 468 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 469 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 470 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 471 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 472 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 473 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 474 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 475 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 476 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 477 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 478 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 479 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 480 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 481 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 482 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 483 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 484 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 485 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 486 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 487 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 488 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 489 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 490 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 491 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 492 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 493 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 494 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 495 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 496 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 497 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 498 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 499 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 500 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 501 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 502 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 503 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 504 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 505 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 506 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 507 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 508 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 509 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 510 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 511 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 512 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 513 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 514 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 515 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 516 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 517 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 518 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 519 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
