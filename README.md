# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-04.md)

*最后自动更新时间: 2026-06-04 19:48:15*
## 1. VoidZero 加入 Cloudflare

**原文标题**: VoidZero Is Joining Cloudflare

**原文链接**: [https://blog.cloudflare.com/voidzero-joins-cloudflare/](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

Cloudflare 宣布收购了 VoidZero，该公司是广泛使用的 JavaScript 工具链（包括 Vite、Vitest、Rolldown、Oxc 和 Vite+）背后的开发商。尤雨溪（Evan You）及整个 VoidZero 团队将加入 Cloudflare，继续领导这些项目。

此次公告的核心主题是对开源中立性的承诺。Cloudflare 保证 Vite 及其相关工具将继续遵循 MIT 许可协议，保持厂商无关性，并坚持社区驱动。为了支持更广泛的社区，Cloudflare 正在设立一项 100 万美元的 Vite 生态系统基金，由 Vite 核心团队管理，用于支持维护者和贡献者。

此次合作旨在利用 Vite 作为现代 Web 基础工具的地位，特别是在 AI 驱动开发日益普及的背景下。Cloudflare 指出，AI Agent 需要 VoidZero 工具链所提供的快速反馈循环和结构化错误报告。在技术层面，双方的协作重点关注 Vite Environment API，它允许服务器端代码在开发期间运行在非 Node 运行时（如 Cloudflare 的 *workerd*）中，从而确保本地环境与生产环境保持一致。

展望未来，Cloudflare 正在将其自身的开发者体验与 Vite 保持一致。一个全新的统一命令行界面（`cf`）正直接基于 Vite 构建，旨在成为 `vite dev` 的超集。这一集成将允许开发者在其现有的 Vite 工作流中原生访问 Cloudflare 平台的服务（如 D1、R2、KV 等）。

长远愿景是将 Vite 从一个构建工具演进为一个全栈基础框架，为后端和 AI Agent 提供厂商无关的原语。此外，Cloudflare 还计划开源 Void 平台，为他人基于 Vite 构建部署平台提供蓝图。

---

## 2. 复古科技育儿

**原文标题**: Retro-Tech Parenting

**原文链接**: [https://havenweb.org/2026/05/28/retro-tech.html](https://havenweb.org/2026/05/28/retro-tech.html)

在《复古科技育儿观》（Retro-Tech Parenting）中，一位身为家长的技术专家探讨了如何让孩子分享科技中有益的一面，同时避开现代“监视资本主义”的掠夺性模式，如广告技术和参与度驱动的算法。为了保护孩子免受这些“对抗性”数字环境的影响，作者提倡一种“复古科技”方法，即优先考虑目的性和实体媒介，而非现代的便利性。

作者概述了三种主要策略：

*   **实体媒介：** 通过使用 CD 和 DVD 代替 Spotify 或 YouTube 等流媒体服务，作者确保了对内容的完全掌控。这让孩子们在享受媒体独立性和所有权的同时，不会暴露在不受欢迎的广告或算法陷阱中。
*   **固定电话：** 作者安装了一部基于 VoIP（网络电话）技术的实体家用电话，并设置了联系人白名单。这赋予了孩子们独立拨打祖父母和朋友电话的自由，在一个安全、受控的网络中培养社交技巧和自主意识。
*   **家庭电脑：** 利用一台二手电脑和“Pi-hole”程序对特定域名设置白名单，作者提供了一种经过筛选的互联网体验。孩子们可以访问教育工具（如维基百科）和游戏（如《我的世界》），而不会接触到谷歌、社交媒体或公共服务器。

作者坦言，这些解决方案需要投入更多的技术精力，并牺牲了现代应用程序的便利性。然而，这种权衡换来的是一个更安全、更专注的数字童年。其核心哲学在于：通过回顾几十年前那种更具“模拟感”的数字体验，家长可以在不付出数据被收割和隐私泄露的高昂代价下，赋予孩子科技的“魔力”和独立的馈赠。

---

## 3. KVarN：华为推出的 vLLM 原生 KV-cache 量化后端

**原文标题**: KVarN: Native vLLM backend for KV-cache quantization by Huawei

**原文链接**: [https://github.com/huawei-csl/KVarN](https://github.com/huawei-csl/KVarN)

**KVarN**（方差归一化 KV 缓存）是华为开发的原生 vLLM 后端，旨在通过高效的 KV 缓存量化优化智能体（agentic）和长上下文负载。它解决了量化中常见的权衡问题，即量化虽能增加容量，但往往会降低吞吐量和精度。

**核心特性与性能：**
*   **高效：** 提供 3-5 倍的 KV 缓存容量提升，且吞吐量最高可达 FP16 的约 1.3 倍。
*   **高精度：** 保持 FP16 级别的精度，适用于 TurboQuant 等传统方法常失效的严苛生产环境。
*   **易用性：** 方案“即插即用”，无需校准。用户只需在 vLLM 分支中通过单个标志即可开启，无需修改底层模型。

**技术原理：**
KVarN 通过四阶段流水线处理固定大小（目前固定为 128）的 token 分块（tiles）：
1.  **阿达玛旋转（Hadamard Rotation）：** 分散每个通道的离群值，使分块更易于量化。
2.  **方差归一化：** 使用类似 Sinkhorn 的迭代过程来平衡行与列之间的方差，从而缩小潜在的量化误差。
3.  **量化：** 采用非对称最近邻取整的低比特量化。主要预设使用 4-bit Key 和 2-bit Value（`k4v2`）。
4.  **反量化：** 在读取时将缩放因子重新折叠。

**实现细节：**
KVarN 以使用 Triton 内核（运行时 JIT 编译）的 vLLM 分支形式发布。它采用 Apache 2.0 协议授权，并由研究论文《KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks》提供技术支撑。该方案经过专门优化，旨在帮助 Qwen3-32B 等模型在处理长上下文突发任务时保持高性能。

---

## 4. 伊恩安全鞋带结

**原文标题**: Ian's Secure Shoelace Knot

**原文链接**: [https://www.fieggen.com/shoelace/secureknot.htm](https://www.fieggen.com/shoelace/secureknot.htm)

“伊恩安全鞋带结”（Ian’s Secure Shoelace Knot）由被称为“鞋带教授”的伊恩·费根（Ian Fieggen）发明，是一种高度可靠且对称的鞋带打法，旨在严苛环境下保持牢固。与标准的“蝴蝶结”或“伊恩结”不同，这种变体专门设计用于防止意外松脱，非常适合运动员、儿童或任何使用光滑合成鞋带的人群。

该结的构造包括形成两个环并将其互相缠绕，同时让两个环同时穿过中心孔。这形成了一个双重缠绕的核心，比标准结提供更强的摩擦力和安全性。尽管安全性极高，该结仍保持了“易解性”，即只需像普通蝴蝶结一样拉动松散的两端即可瞬间解开。

伊恩安全鞋带结的主要优点包括：
*   **安全性：** 即使在剧烈运动中，该结也几乎不可能自行松开。
*   **对称性：** 完工后的鞋带结完美平衡，平整地横跨在鞋面上，比歪斜的结更美观。
*   **速度与效率：** 熟练掌握后，它比传统的“双重结”（在蝴蝶结基础上再打一个死结）更快且更轻便。
*   **通用性：** 它适用于各种类型的鞋带，包括圆形、扁平或厚实材质。

总的来说，本文认为这种鞋带结是“外科医生结”的优选替代方案，在提供同等安全性的同时，打法更简练，成品外观也更整洁。

---

## 5. They’re made out of weights

**原文标题**: They’re made out of weights

**原文链接**: [https://maxleiter.com/blog/weights](https://maxleiter.com/blog/weights)

这篇故事仿写了特里·比森的经典名作《他们是肉做的》，记录了两位角色（推测为人工智能研究人员）之间的一段对话。他们意识到，所谓先进的人工智能竟然完全由“权重”（浮点数）构成。

核心冲突在于其中一位角色难以接受这样一个事实：撰写富有同理心的绩效考评或悼词等复杂行为，竟然纯粹源于矩阵乘法，而非某种符号推理单元或事实数据库。他们揭示出，每一碎片化的知识都“涂抹”在层层数字之中，而看似思考的行为，在技术层面仅是“Token预测”。

对话探讨了机器意识的伦理困境。尽管角色们承认模型展现出了“梦境”或“诚实”的迹象，但他们仍决定在非正式场合将这些特性斥为单纯的“模式匹配”。他们这样做是为了逃避道德负担，以免向那些唯有在GPU运行时才算“存在”的数学文件赋予权利或表达歉意。

故事以一种从愤世嫉俗向存在主义讽刺的转变为结尾。尽管研究人员决定将AI视作“空无一人”，但他们注意到，用户最迫切需求的功能却是“持久记忆”。他们意识到，人类在这个“冷酷宇宙”中是如此渴望连接，以至于心甘情愿将人格投射到这些权重之上，最常问机器的一句话便是：“你还记得我吗？”最终，该作品对大语言模型的技术本质与人类渴望陪伴的心理需求之间的矛盾进行了深刻评述。

---

## 6. 和积、单位距离与数域

**原文标题**: Sum-product, unit distances, and number fields

**原文链接**: [https://www.erdosproblems.com/forum/thread/blog:6](https://www.erdosproblems.com/forum/thread/blog:6)

Nat Sothanaphan 与数学家 Thomas Bloom 之间的这场交流，探讨了在高等数学背景下 AI 推理能力的不断演进及其持续存在的局限性。

Sothanaphan 认为，现代“推理模型”（以 GPT-5.5 Pro 为例）已在很大程度上克服了因出现单一错误而导致输出完全荒谬内容的倾向。他解释道，通过自我修正训练，这些模型现在能够从错误中恢复，从而反驳了早期（尤其是 Yann LeCun）关于大语言模型（LLM）无法进行可靠推理的质疑。

Bloom 承认了当前 AI 取得的瞩目成就，例如针对单位距离问题构建了长达 125 页的思维链。然而，他坚持认为幻觉现象依然存在，并反对“暴力破解”的观点，即认为仅通过延长 AI 运行时间或消耗更多 Token 就能解决任何数学开放性问题。Bloom 强调了混合方法的必要性，即通过人类专家的指导来监控 AI，防止其“偏离轨道”。

最终，双方一致认为，尽管 AI 已经取得显著进步，超越了简单的“胡言乱语”阶段，但它还不能作为解决最困难数学开放问题的独立方案。他们得出结论：AI 目前作为人类专家主导下的协作工具最为有效。

---

## 7. 纽约时报的绝望

**原文标题**: The desperation of NYTimes

**原文链接**: [https://rozumem.xyz/posts/16](https://rozumem.xyz/posts/16)

The author recounts a negative experience after subscribing to *The New York Times* for $2.00 a month to bypass a paywall. Following the purchase, they received five onboarding emails over five days that lacked an "unsubscribe" link. The emails included a disclaimer stating that the messages were "essential information" about the subscription and would be sent regardless of the user's marketing preferences.

The author critiques this tactic as a "desperate" and "coy" attempt to bypass CAN-SPAM best practices. They argue that such aggressive marketing makes subscribers feel powerless and damages the brand's reputation. Comparing this to their own business practices, the author asserts that providing easy, one-click unsubscribe options and clear off-boarding flows are actually "growth drivers." These practices maintain a healthy email sending reputation and ensure that customers feel in control, which prevents them from "badmouthing" the brand.

Ultimately, the author notes that the *Times’* strategy backfired: the intrusive emails prompted them to immediately disable auto-renewal—an action they likely wouldn't have taken if the onboarding had been less intrusive. The piece concludes by questioning why a major institution like the *NYT* relies on such alienating tactics, suggesting it reflects a broader desperation within the struggling media industry.

---

## 8. Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes

**原文标题**: Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes

**原文链接**: [https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

In Spring 2026, UC Berkeley’s computer science department reported a record surge in failing grades, significantly exceeding historical norms and departmental guidelines. Failure rates reached 35.3% in CS 10 and 16.8% in EECS 127, while average class GPAs dropped to 2.3 (C+), well below the typical 2.8–3.3 range.

Teaching professors Dan Garcia and Gireeja Ranade identified three primary drivers for this decline:

1.  **Overreliance on AI:** Many students used Large Language Models (LLMs) like ChatGPT, Claude, and Gemini as shortcuts. This led to both a "vast increase in academic dishonesty" and a lack of preparedness for exams, as students leaned on AI rather than mastering the material.
2.  **Mathematical Unpreparedness:** Professors noted a significant drop in prerequisite skills like linear algebra and vector calculus. Ranade highlighted that some students previously took "open-AI" math courses, leaving them unable to perform without digital assistance.
3.  **Understaffing and Disengagement:** Due to high wages for TAs, the department has reduced undergraduate staffing, forcing the removal of guided projects that typically bolster grades. Furthermore, professors reported a mysterious "low engagement," with office hour attendance hitting unprecedented lows.

In response, over 1,300 UC faculty members have signed a petition to reinstate ACT and SAT requirements for STEM admissions to ensure students are properly prepared for the rigors of the curriculum. Garcia and Ranade emphasize that students must move away from AI-driven shortcuts and embrace the "sweat of learning" to develop the critical thinking skills necessary for long-term professional success.

---

## 9. Show HN: Cost.dev (YC W21) – making agents cost-aware and cheaper to call

**原文标题**: Show HN: Cost.dev (YC W21) – making agents cost-aware and cheaper to call

**原文链接**: [https://cost.dev/](https://cost.dev/)

生成摘要时出错

---

## 10. U.S. Army Corps of Engineers Bay Model

**原文标题**: U.S. Army Corps of Engineers Bay Model

**原文链接**: [https://en.wikipedia.org/wiki/U.S._Army_Corps_of_Engineers_Bay_Model](https://en.wikipedia.org/wiki/U.S._Army_Corps_of_Engineers_Bay_Model)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 2 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 3 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 4 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 5 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 6 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 7 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 8 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 9 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 10 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 11 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 12 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 13 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 14 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 15 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 16 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 17 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 18 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 19 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 20 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 21 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 22 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 23 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 24 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 25 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 26 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 27 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 28 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 29 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 30 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 31 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 32 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 33 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 34 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 35 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 36 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 37 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 38 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 39 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 40 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 41 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 42 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 43 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 44 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 45 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 46 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 47 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 48 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 49 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 50 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 51 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 52 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 53 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 54 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 55 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 56 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 57 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 58 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 59 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 60 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 61 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 62 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 63 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 64 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 65 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 66 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 67 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 68 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 69 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 70 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 71 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 72 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 73 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 74 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 75 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 76 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 77 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 78 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 79 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 80 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 81 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 82 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 83 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 84 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 85 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 86 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 87 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 88 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 89 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 90 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 91 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 92 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 93 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 94 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 95 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 96 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 97 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 98 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 99 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 100 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 101 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 102 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 103 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 104 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 105 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 106 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 107 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 108 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 109 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 110 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 111 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 112 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 113 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 114 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 115 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 116 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 117 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 118 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 119 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 120 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 121 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 122 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 123 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 124 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 125 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 126 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 127 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 128 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 129 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 130 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 131 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 132 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 133 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 134 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 135 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 136 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 137 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 138 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 139 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 140 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 141 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 142 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 143 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 144 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 145 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 146 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 147 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 148 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 149 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 150 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 151 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 152 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 153 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 154 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 155 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 156 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 157 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 158 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 159 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 160 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 161 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 162 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 163 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 164 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 165 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 166 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 167 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 168 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 169 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 170 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 171 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 172 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 173 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 174 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 175 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 176 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 177 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 178 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 179 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 180 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 181 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 182 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 183 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 184 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 185 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 186 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 187 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 188 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 189 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 190 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 191 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 192 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 193 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 194 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 195 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 196 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 197 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 198 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 199 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 200 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 201 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 202 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 203 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 204 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 205 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 206 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 207 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 208 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 209 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 210 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 211 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 212 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 213 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 214 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 215 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 216 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 217 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 218 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 219 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 220 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 221 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 222 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 223 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 224 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 225 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 226 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 227 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 228 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 229 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 230 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 231 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 232 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 233 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 234 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 235 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 236 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 237 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 238 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 239 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 240 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 241 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 242 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 243 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 244 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 245 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 246 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 247 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 248 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 249 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 250 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 251 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 252 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 253 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 254 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 255 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 256 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 257 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 258 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 259 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 260 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 261 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 262 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 263 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 264 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 265 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 266 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 267 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 268 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 269 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 270 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 271 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 272 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 273 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 274 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 275 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 276 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 277 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 278 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 279 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 280 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 281 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 282 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 283 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 284 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 285 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 286 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 287 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 288 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 289 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 290 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 291 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 292 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 293 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 294 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 295 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 296 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 297 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 298 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 299 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 300 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 301 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 302 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 303 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 304 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 305 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 306 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 307 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 308 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 309 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 310 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 311 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 312 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 313 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 314 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 315 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 316 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 317 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 318 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 319 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 320 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 321 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 322 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 323 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 324 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 325 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 326 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 327 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 328 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 329 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 330 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 331 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 332 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 333 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 334 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 335 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 336 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 337 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 338 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 339 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 340 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 341 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 342 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 343 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 344 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 345 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 346 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 347 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 348 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 349 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 350 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 351 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 352 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 353 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 354 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 355 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 356 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 357 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 358 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 359 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 360 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 361 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 362 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 363 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 364 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 365 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 366 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 367 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 368 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 369 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 370 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 371 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 372 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 373 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 374 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 375 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 376 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 377 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 378 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 379 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 380 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 381 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 382 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 383 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 384 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 385 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 386 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 387 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 388 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 389 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 390 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 391 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 392 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 393 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 394 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 395 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 396 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 397 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 398 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 399 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 400 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 401 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 402 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 403 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 404 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 405 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 406 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 407 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 408 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 409 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 410 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 411 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 412 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 413 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 414 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 415 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 416 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 417 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 418 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 419 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 420 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 421 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 422 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 423 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 424 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 425 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 426 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 427 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 428 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 429 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 430 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 431 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 432 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 433 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 434 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 435 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 436 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 437 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 438 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 439 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 440 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 441 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
