# Hacker News 热门文章摘要 (2026-05-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 实现持久化工作流，SQLite 就够了

**原文标题**: SQLite is all you need for durable workflows

**原文链接**: [https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/)

在博客文章《SQLite 是实现持久化工作流的全部所需》中，作者指出，现代工作流编排（通常由 Temporal 或 Cadence 等复杂的分布式系统处理）可以有效地利用 SQLite 进行管理。持久化工作流是必须在硬件或软件故障中保持存续的长期运行过程。虽然此类工作流传统上与沉重的基础设施相关联，但作者认为 SQLite 的 ACID 特性使其成为执行此任务的理想引擎。

文章介绍了 **Obelisk**，这是一个基于 SQLite 构建的持久化执行引擎。其核心思想是将 SQLite 作为集中的事件存储，用以追踪工作流的状态和历史。通过以事务方式记录过程中的每一步，系统可以在崩溃或重启后可靠地从上次中断的地方恢复。

**该方法的主要优势包括：**
*   **运维简单性：** 它取代了对外部数据库、消息队列和复杂网络管理的需求。
*   **性能：** 通过使用 SQLite 的预写日志（WAL）模式，系统实现了高吞吐量和低延迟，在许多用例中往往优于分布式替代方案。
*   **成本效益：** 在单台服务器或小型实例上运行可显著降低基础设施开销。

为了解决单点故障风险，作者建议利用 **Litestream** 或 **LiteFS** 等工具将数据实时复制到云存储或其他节点。

文章的核心论点是对“默认分布式”思维模式的批判。对于绝大多数企业而言，大规模分布式集群的可扩展性并非必需。相反，作者倡导使用“乏味”但稳健的技术，证明了 SQLite 能够为可靠的工作流执行提供必要的持久性和顺序，而无需承担沉重的运维“复杂度税”。

---

## 2. Mistral AI Now 巴黎峰会笔记

**原文标题**: Notes from the Mistral AI Now Summit in Paris

**原文链接**: [https://koenvangilst.nl/lab/mistral-ai-now-summit](https://koenvangilst.nl/lab/mistral-ai-now-summit)

在巴黎举行的 Mistral AI Now 峰会上，Mistral AI 宣布其已从模型开发商向**全栈 AI 提供商**转型，业务涵盖算力、平台及咨询服务。作为美国科技巨头的欧洲替代方案，Mistral 的核心优势在于**数据主权**、高效的开源模型，以及支持企业**本地部署** (on-premise) 运行 AI 的能力。

峰会核心要点包括：

*   **基础设施与独立性：** Mistral 正在法国和瑞典建立自有的数据中心。这一基础设施支持其“主权 AI”战略，使银行（如法巴银行、Abanca）等受监管行业能够在本地处理敏感数据。
*   **专业化小模型：** Mistral 并非盲目追求通用人工智能 (AGI)，而是优先开发快速且针对特定任务的模型。典型案例包括 **Document AI** (OCR)、**Voxtral**（为亚马逊 Alexa+ 提供的多语言语音模型）以及 **Robostral**（为 ASML 提供的工业机器人模型）。
*   **智能体 AI (Agentic AI)：** 公司推出了“智能体框架”(agentic harness) 的概念，旨在增强模型的上下文理解、推理和持久性。此外，他们还发布了面向企业的办公生产力工具 **Vibe for Work**。
*   **人文与伦理：** 在一个亮眼的案例中，奥地利科学院利用 **Codestral** 转录了 18 万份古代莎草纸碎片，这项任务若按传统方式完成将耗时数千年。

**结论：**
Mistral 的愿景是成为寻求实际投资回报的欧洲机构不可或缺的合作伙伴。通过专注于透明度、效率和本地控制，他们旨在结束欧洲市场对美国超大规模云厂商的盲目依赖，并提供一套稳健、企业级的 AI 技术栈。

---

## 3. 死亡经济理论

**原文标题**: The dead economy theory

**原文链接**: [https://www.owenmcgrann.com/p/the-dead-economy-theory](https://www.owenmcgrann.com/p/the-dead-economy-theory)

在《死亡经济理论》中，欧文·麦格雷恩（Owen McGrann）指出，人工智能公司目前高达数万亿美元的巨额估值，迫使它们必须从“辅助”劳动力转向系统性地“取代”劳动力。他断言，AI产业正将全球专业劳动力市场视为主要收入来源，从而形成了一种威胁资本主义根基的寄生式循环。

麦格雷恩概述了一个“三部曲”经济陷阱：
1. **自动化：** 企业用AI取代工人以提高利润率和股价。
2. **需求毁灭：** 被取代的工人失去购买力，导致消费需求萎缩。
3. **市场崩溃：** 推进自动化的企业最终会倒闭，因为其客户（即工人）再也买不起它们的产品。

这形成了一个“囚徒困境”：单个企业为了保持竞争力会理性地选择自动化，尽管其总体结果是集体的毁灭。麦格雷恩指出，与历史上农业或制造业的转型不同，AI是通用型的，且进化速度极快，使劳动力市场无法适应。他引用了诺贝尔奖得主达隆·阿西莫格鲁（Daron Acemoglu）关于“过度自动化”的警告，即AI被用于消灭工作岗位，却未能带来显著的生产力增长。

此外，麦格雷恩还指出了一场深刻的政治危机：民主依赖于一种契约，即被统治者提供劳动力和税收以换取制衡力。如果AI使人类劳动力变得多余，精英阶层将不再需要大众，从而切断了资本与人类贡献之间的联系。这促使科技领袖形成的“兄弟寡头政治”（broligarchy）更倾向于专制，而非被他们视为阻碍的民主监督。

最终，麦格雷恩驳斥了AI乐观主义者所承诺的“休闲经济”乌托邦。他提到了制造业空心化地区的“绝望之死”，并警告称，剥夺经济目标会导致社会崩溃。文章总结道，我们正在资助一场旨在消灭人类客户群的革命，这不仅威胁到经济，也威胁到民主治理。

---

## 4. Bijou64：一种变长整数编码

**原文标题**: Bijou64: A variable-length integer encoding

**原文链接**: [https://www.inkandswitch.com/tangents/bijou64/](https://www.inkandswitch.com/tangents/bijou64/)

**Bijou64** is a novel variable-length integer (varint) encoding developed for the Subduction CRDT protocol. It was designed to solve a critical security flaw in traditional encodings like LEB128: the lack of structural **canonicality**.

### The Problem
In standard encodings like LEB128, a single integer can be represented by multiple different byte sequences (e.g., by adding redundant "continuation" bytes). This ambiguity is a major vulnerability for signed data and content-addressed systems, as an attacker can alter the byte string without changing the decoded value, thereby breaking digital signatures.

### The Solution: Canonical by Construction
Bijou64 ensures that every integer has exactly one valid representation through two primary mechanisms:
1.  **First-Byte Tagging:** The first byte handles values 0–247 directly. Values 248–255 serve as tags indicating the number of following data bytes. This allows the decoder to know the payload length immediately (O(1)) rather than scanning for continuation bits (O(n)).
2.  **Tiered Offsets:** Each length "tier" is offset by the maximum value of the preceding tier. This mathematical approach prevents the redundancy found in LEB128, ensuring no overlap between representations.

### Performance Gains
Despite being designed for security, Bijou64 significantly outperforms LEB128. Benchmarks on ARM and x86 architectures show it decodes **2–10 times faster** than LEB128. This efficiency is due to:
*   **Predictable Branching:** CPUs can easily predict the fixed-length reads.
*   **Native Instructions:** It uses contiguous big-endian payloads, allowing compilers to utilize high-speed CPU `bswap` (byte-swap) instructions.
*   **Zero-Cost Validation:** Because the format is structurally canonical, no additional runtime checks are required to reject "overlong" encodings.

While the encoded size is comparable to LEB128, Bijou64 offers a safer, faster alternative for modern binary protocols, especially those requiring cryptographic signatures or high-performance data syncing. The library is currently available as a Rust crate.

---

## 5. On Rendering Diffs

**原文标题**: On Rendering Diffs

**原文链接**: [https://pierre.computer/writing/on-rendering-diffs](https://pierre.computer/writing/on-rendering-diffs)

生成摘要时出错

---

## 6. Rothko for your current weather conditions

**原文标题**: Rothko for your current weather conditions

**原文链接**: [https://rothko.joonas.wtf/](https://rothko.joonas.wtf/)

生成摘要时出错

---

## 7. It's hard to justify buying a Framework 12

**原文标题**: It's hard to justify buying a Framework 12

**原文链接**: [https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/](https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/)

生成摘要时出错

---

## 8. GTA 6 Developers Unionize

**原文标题**: GTA 6 Developers Unionize

**原文链接**: [https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/)

生成摘要时出错

---

## 9. Liquid AI reveals 8B-A1B MoE trained on 38T

**原文标题**: Liquid AI reveals 8B-A1B MoE trained on 38T

**原文链接**: [https://www.liquid.ai/blog/lfm2-5-8b-a1b](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

生成摘要时出错

---

## 10. CAPTCHAs can still detect AI agents

**原文标题**: CAPTCHAs can still detect AI agents

**原文链接**: [https://research.roundtable.ai/captchas-detect-ai/](https://research.roundtable.ai/captchas-detect-ai/)

生成摘要时出错

---

## 11. Show HN: TV Explorer. Adding advanced UI to free online TV

**原文标题**: Show HN: TV Explorer. Adding advanced UI to free online TV

**原文链接**: [https://tvexplorer.live](https://tvexplorer.live)

生成摘要时出错

---

## 12. High Density Living, 2000 Years Ago: Inside the Roman Apartment Building

**原文标题**: High Density Living, 2000 Years Ago: Inside the Roman Apartment Building

**原文链接**: [https://commonedge.org/high-density-living-2000-years-ago-inside-the-roman-apartment-building/](https://commonedge.org/high-density-living-2000-years-ago-inside-the-roman-apartment-building/)

生成摘要时出错

---

## 13. We should be more tired than the model

**原文标题**: We should be more tired than the model

**原文链接**: [https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/)

生成摘要时出错

---

## 14. I am retiring from tech to live offline

**原文标题**: I am retiring from tech to live offline

**原文链接**: [https://openpath.quest/2026/i-am-retiring-from-tech-to-live-offline/](https://openpath.quest/2026/i-am-retiring-from-tech-to-live-offline/)

生成摘要时出错

---

## 15. A letter from the Duke of Wellington to the British Foreign Office (1809)

**原文标题**: A letter from the Duke of Wellington to the British Foreign Office (1809)

**原文链接**: [https://wellsoc.org/society-member-pages/anecdotes-of-wellington/](https://wellsoc.org/society-member-pages/anecdotes-of-wellington/)

生成摘要时出错

---

## 16. Someone used my open source project to phish people

**原文标题**: Someone used my open source project to phish people

**原文链接**: [https://andrej.sh/posts/phishing-through-my-open-source-project](https://andrej.sh/posts/phishing-through-my-open-source-project)

生成摘要时出错

---

## 17. Expertise in the age of AI

**原文标题**: Expertise in the age of AI

**原文链接**: [https://www.moderndescartes.com/essays/ai_and_expertise/](https://www.moderndescartes.com/essays/ai_and_expertise/)

生成摘要时出错

---

## 18. Real-time LLM Inference on Standard GPUs: 3k tokens/s per request

**原文标题**: Real-time LLM Inference on Standard GPUs: 3k tokens/s per request

**原文链接**: [https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/)

生成摘要时出错

---

## 19. ATLAS: Autoformalized Textbook Library At Scale

**原文标题**: ATLAS: Autoformalized Textbook Library At Scale

**原文链接**: [https://github.com/facebookresearch/atlas-lean](https://github.com/facebookresearch/atlas-lean)

生成摘要时出错

---

## 20. Cedana (YC S23) Is Hiring

**原文标题**: Cedana (YC S23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/cedana/jobs/d1vYocG-forward-deployed-engineer-ai-hpc](https://www.ycombinator.com/companies/cedana/jobs/d1vYocG-forward-deployed-engineer-ai-hpc)

生成摘要时出错

---

## 21. AI will be used to estimate age of asylum seekers from next year

**原文标题**: AI will be used to estimate age of asylum seekers from next year

**原文链接**: [https://www.bbc.co.uk/news/articles/ce3pe36qe7ro](https://www.bbc.co.uk/news/articles/ce3pe36qe7ro)

生成摘要时出错

---

## 22. Durable execution, the hard way

**原文标题**: Durable execution, the hard way

**原文链接**: [https://github.com/hatchet-dev/durable-execution-the-hard-way](https://github.com/hatchet-dev/durable-execution-the-hard-way)

生成摘要时出错

---

## 23. The Secret Garden of Rock-Paper-Scissors

**原文标题**: The Secret Garden of Rock-Paper-Scissors

**原文链接**: [https://theshamblog.com/the-secret-garden-of-rock-paper-scissors/](https://theshamblog.com/the-secret-garden-of-rock-paper-scissors/)

生成摘要时出错

---

## 24. The Science of Weather and the Nature of Science

**原文标题**: The Science of Weather and the Nature of Science

**原文链接**: [https://www.the-hinternet.com/p/the-science-of-weather-and-the-nature](https://www.the-hinternet.com/p/the-science-of-weather-and-the-nature)

生成摘要时出错

---

## 25. Tulip mania: when a single flower was worth more than a house (2025)

**原文标题**: Tulip mania: when a single flower was worth more than a house (2025)

**原文链接**: [https://dutchreview.com/culture/tulip-mania-netherlands/](https://dutchreview.com/culture/tulip-mania-netherlands/)

生成摘要时出错

---

## 26. Orchestrating AI code review at scale

**原文标题**: Orchestrating AI code review at scale

**原文链接**: [https://blog.cloudflare.com/ai-code-review/](https://blog.cloudflare.com/ai-code-review/)

生成摘要时出错

---

## 27. Let's compile Quake like it's 1997

**原文标题**: Let's compile Quake like it's 1997

**原文链接**: [https://fabiensanglard.net/compile_like_1997/](https://fabiensanglard.net/compile_like_1997/)

生成摘要时出错

---

## 28. Claude Opus 4.8

**原文标题**: Claude Opus 4.8

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)

生成摘要时出错

---

## 29. Bricks and Minifigs Stole a Man's $200k Lego Collection

**原文标题**: Bricks and Minifigs Stole a Man's $200k Lego Collection

**原文链接**: [https://mybricklog.com/blog/bricks-minifigs-corporate-stole-old-mans-200000-lego-collection](https://mybricklog.com/blog/bricks-minifigs-corporate-stole-old-mans-200000-lego-collection)

生成摘要时出错

---

## 30. Dynamic Workflows in Claude Code

**原文标题**: Dynamic Workflows in Claude Code

**原文链接**: [https://claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

生成摘要时出错

---

## 31. Headway Therapy Patients Forced to Scan Their Faces to Keep Getting Care

**原文标题**: Headway Therapy Patients Forced to Scan Their Faces to Keep Getting Care

**原文链接**: [https://www.404media.co/headway-therapy-facial-scan-biometric-data-identity-verification/](https://www.404media.co/headway-therapy-facial-scan-biometric-data-identity-verification/)

生成摘要时出错

---

## 32. Why German trains are never on time anymore

**原文标题**: Why German trains are never on time anymore

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/05/29/why-german-trains-are-never-on-time-anymore_6753927_4.html](https://www.lemonde.fr/en/international/article/2026/05/29/why-german-trains-are-never-on-time-anymore_6753927_4.html)

生成摘要时出错

---

## 33. An Obsessive Focus on UX: Pilot's Pressure-Regulating Kire-Na Highlighter

**原文标题**: An Obsessive Focus on UX: Pilot's Pressure-Regulating Kire-Na Highlighter

**原文链接**: [https://www.core77.com/posts/143832/An-Obsessive-Focus-on-UX-Pilots-Pressure-Regulating-Kire-Na-Highlighter](https://www.core77.com/posts/143832/An-Obsessive-Focus-on-UX-Pilots-Pressure-Regulating-Kire-Na-Highlighter)

生成摘要时出错

---

## 34. Americans Are Falling Behind on Their $1.25T Credit-Card Bill

**原文标题**: Americans Are Falling Behind on Their $1.25T Credit-Card Bill

**原文链接**: [https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77](https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77)

生成摘要时出错

---

## 35. Wterm – A terminal emulator for the web

**原文标题**: Wterm – A terminal emulator for the web

**原文链接**: [https://wterm.dev/](https://wterm.dev/)

生成摘要时出错

---

## 36. Even (very) noisy LLM evaluators are useful for improving AI agents

**原文标题**: Even (very) noisy LLM evaluators are useful for improving AI agents

**原文链接**: [https://www.tensorzero.com/blog/even-very-noisy-llm-evaluators-are-useful-for-improving-ai-agents/](https://www.tensorzero.com/blog/even-very-noisy-llm-evaluators-are-useful-for-improving-ai-agents/)

生成摘要时出错

---

## 37. Volkswagen blocks Home Assistant by requiring client assertion

**原文标题**: Volkswagen blocks Home Assistant by requiring client assertion

**原文链接**: [https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967](https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967)

生成摘要时出错

---

## 38. Blue Origin's New Glenn blows up during static fire test

**原文标题**: Blue Origin's New Glenn blows up during static fire test

**原文链接**: [https://twitter.com/nasaspaceflight/status/2060164928472854821](https://twitter.com/nasaspaceflight/status/2060164928472854821)

生成摘要时出错

---

## 39. Ronny Chieng's 'Fuck AI' Speech Met with Cheers from Harvard Graduates

**原文标题**: Ronny Chieng's 'Fuck AI' Speech Met with Cheers from Harvard Graduates

**原文链接**: [https://www.complex.com/pop-culture/a/tracewilliamcowen/ronny-chieng-ai-speech-harvard](https://www.complex.com/pop-culture/a/tracewilliamcowen/ronny-chieng-ai-speech-harvard)

生成摘要时出错

---

## 40. Step 3.7 Flash

**原文标题**: Step 3.7 Flash

**原文链接**: [https://static.stepfun.com/blog/step-3.7-flash/](https://static.stepfun.com/blog/step-3.7-flash/)

生成摘要时出错

---

## 41. Italians and Dutch share the same gestural instinct for teaching

**原文标题**: Italians and Dutch share the same gestural instinct for teaching

**原文链接**: [https://www.mpi.nl/news/italians-and-dutch-share-same-gestural-instinct-teaching](https://www.mpi.nl/news/italians-and-dutch-share-same-gestural-instinct-teaching)

生成摘要时出错

---

## 42. We suggest using living spiders as cooling devices for data centers (2020)

**原文标题**: We suggest using living spiders as cooling devices for data centers (2020)

**原文链接**: [https://marksilberstein.ece.technion.ac.il/wp-content/uploads/2020/05/Putting_Bugs_in_Your_DC_Might_Actually_be_a_Good_Idea_WACI.pdf](https://marksilberstein.ece.technion.ac.il/wp-content/uploads/2020/05/Putting_Bugs_in_Your_DC_Might_Actually_be_a_Good_Idea_WACI.pdf)

生成摘要时出错

---

## 43. Show HN: AISlop, a CLI for catching AI generated code smells

**原文标题**: Show HN: AISlop, a CLI for catching AI generated code smells

**原文链接**: [https://github.com/scanaislop/aislop](https://github.com/scanaislop/aislop)

生成摘要时出错

---

## 44. Nondeterminism's Not the Problem

**原文标题**: Nondeterminism's Not the Problem

**原文链接**: [https://isaacvando.com/nondeterminisms-not-the-problem](https://isaacvando.com/nondeterminisms-not-the-problem)

生成摘要时出错

---

## 45. Don't Build Your Own Lisp

**原文标题**: Don't Build Your Own Lisp

**原文链接**: [https://gist.github.com/no-defun-allowed/7e3e238c959e27d4919bb4272487d7ad](https://gist.github.com/no-defun-allowed/7e3e238c959e27d4919bb4272487d7ad)

生成摘要时出错

---

## 46. The UK government's Low Value Purchase System is a waste of time

**原文标题**: The UK government's Low Value Purchase System is a waste of time

**原文链接**: [https://shkspr.mobi/blog/2026/05/the-uk-governments-low-value-purchase-system-is-a-waste-of-time/](https://shkspr.mobi/blog/2026/05/the-uk-governments-low-value-purchase-system-is-a-waste-of-time/)

生成摘要时出错

---

## 47. Robinhood now lets your AI agents trade stocks

**原文标题**: Robinhood now lets your AI agents trade stocks

**原文链接**: [https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/)

生成摘要时出错

---

## 48. HeidiSQL – Lightweight MariaDB, MySQL, SQL Server, PostgreSQL and SQLite Manager

**原文标题**: HeidiSQL – Lightweight MariaDB, MySQL, SQL Server, PostgreSQL and SQLite Manager

**原文链接**: [https://github.com/HeidiSQL/HeidiSQL](https://github.com/HeidiSQL/HeidiSQL)

生成摘要时出错

---

## 49. Is AI causing a repeat of Front end's Lost Decade?

**原文标题**: Is AI causing a repeat of Front end's Lost Decade?

**原文链接**: [https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

生成摘要时出错

---

## 50. Show HN: Promptloop – create, run, and improve prompt evals from the terminal

**原文标题**: Show HN: Promptloop – create, run, and improve prompt evals from the terminal

**原文链接**: [https://github.com/Bella3202019/promptloop](https://github.com/Bella3202019/promptloop)

生成摘要时出错

---

## 51. Cars collect a startling amount of data about you

**原文标题**: Cars collect a startling amount of data about you

**原文链接**: [https://www.bbc.com/future/article/20260513-your-car-is-spying-on-you-its-about-to-get-worse](https://www.bbc.com/future/article/20260513-your-car-is-spying-on-you-its-about-to-get-worse)

生成摘要时出错

---

## 52. Deadly fungal storms are sweeping US and spreading disease few doctors recognize

**原文标题**: Deadly fungal storms are sweeping US and spreading disease few doctors recognize

**原文链接**: [https://www.sciencefocus.com/planet-earth/dust-storms-us-blood-rain](https://www.sciencefocus.com/planet-earth/dust-storms-us-blood-rain)

生成摘要时出错

---

## 53. Show HN: Context-aware Japanese furigana using Sudachi and ModernBERT

**原文标题**: Show HN: Context-aware Japanese furigana using Sudachi and ModernBERT

**原文链接**: [https://www.ezfurigana.com/](https://www.ezfurigana.com/)

生成摘要时出错

---

## 54. The literary world is sleepwalking into an AI disaster

**原文标题**: The literary world is sleepwalking into an AI disaster

**原文链接**: [https://www.theargumentmag.com/p/the-literary-world-is-sleepwalking](https://www.theargumentmag.com/p/the-literary-world-is-sleepwalking)

生成摘要时出错

---

## 55. Where are the economies of scale in homebuilding?

**原文标题**: Where are the economies of scale in homebuilding?

**原文链接**: [https://www.construction-physics.com/p/where-are-the-economies-of-scale](https://www.construction-physics.com/p/where-are-the-economies-of-scale)

生成摘要时出错

---

## 56. We See the Beautiful, Violent Sun

**原文标题**: We See the Beautiful, Violent Sun

**原文链接**: [https://www.quantamagazine.org/how-we-see-the-beautiful-violent-sun-20260528/](https://www.quantamagazine.org/how-we-see-the-beautiful-violent-sun-20260528/)

生成摘要时出错

---

## 57. Local Git Remotes

**原文标题**: Local Git Remotes

**原文链接**: [https://cblgh.org/posts/local-git-remotes/](https://cblgh.org/posts/local-git-remotes/)

生成摘要时出错

---

## 58. Social media bans for teenagers lack evidence and pose risks, scientists say

**原文标题**: Social media bans for teenagers lack evidence and pose risks, scientists say

**原文链接**: [https://www.frontiersin.org/news/2026/05/29/we-cannot-ban-our-way-out-of-a-youth-mental-health-crisis-social-media-bans-for-teenagers-lack-evidence-and-pose-risks-scientists-say](https://www.frontiersin.org/news/2026/05/29/we-cannot-ban-our-way-out-of-a-youth-mental-health-crisis-social-media-bans-for-teenagers-lack-evidence-and-pose-risks-scientists-say)

生成摘要时出错

---

## 59. I made a million dollar product from my dorm room (2025)

**原文标题**: I made a million dollar product from my dorm room (2025)

**原文链接**: [https://nick.winans.io/blog/nice-nano/](https://nick.winans.io/blog/nice-nano/)

生成摘要时出错

---

## 60. New Study Reveals the Manipulative 'Dark Patterns' of AI Chatbots

**原文标题**: New Study Reveals the Manipulative 'Dark Patterns' of AI Chatbots

**原文链接**: [https://www.404media.co/new-study-reveals-the-manipulative-dark-patterns-of-ai-chatbots/](https://www.404media.co/new-study-reveals-the-manipulative-dark-patterns-of-ai-chatbots/)

生成摘要时出错

---

## 61. It Will Never Be the Year of the Linux Desktop

**原文标题**: It Will Never Be the Year of the Linux Desktop

**原文链接**: [https://unix.foo/posts/it-will-never-be-the-year-of-the-linux-desktop/](https://unix.foo/posts/it-will-never-be-the-year-of-the-linux-desktop/)

生成摘要时出错

---

## 62. GitHub bans security researcher who posted zero-day Windows exploits

**原文标题**: GitHub bans security researcher who posted zero-day Windows exploits

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation)

生成摘要时出错

---

## 63. Flathub prohibits AI-generated code

**原文标题**: Flathub prohibits AI-generated code

**原文链接**: [https://github.com/flathub-infra/documentation/commit/992f57b30de98ddbd5e80959e9672998c83c8c97](https://github.com/flathub-infra/documentation/commit/992f57b30de98ddbd5e80959e9672998c83c8c97)

生成摘要时出错

---

## 64. Endive: A JVM native WebAssembly runtime

**原文标题**: Endive: A JVM native WebAssembly runtime

**原文链接**: [https://github.com/bytecodealliance/endive](https://github.com/bytecodealliance/endive)

生成摘要时出错

---

## 65. Building durable workflows on Postgres

**原文标题**: Building durable workflows on Postgres

**原文链接**: [https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution)

生成摘要时出错

---

## 66. YouTube to automatically label AI-generated videos

**原文标题**: YouTube to automatically label AI-generated videos

**原文链接**: [https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

生成摘要时出错

---

## 67. Social Animus

**原文标题**: Social Animus

**原文链接**: [https://justine.lol/animus/](https://justine.lol/animus/)

生成摘要时出错

---

## 68. Garnix (A Nix CI) is shutting down

**原文标题**: Garnix (A Nix CI) is shutting down

**原文链接**: [https://discourse.nixos.org/t/garnix-is-shutting-down-not-oc/77895](https://discourse.nixos.org/t/garnix-is-shutting-down-not-oc/77895)

生成摘要时出错

---

## 69. Danish Pension Blacklists SpaceX over 'Catastrophic Governance'

**原文标题**: Danish Pension Blacklists SpaceX over 'Catastrophic Governance'

**原文链接**: [https://www.bloomberg.com/news/articles/2026-05-29/danish-pension-fund-blacklists-spacex-citing-governance-issues](https://www.bloomberg.com/news/articles/2026-05-29/danish-pension-fund-blacklists-spacex-citing-governance-issues)

生成摘要时出错

---

## 70. EU-Backed Appeals Center Accidentally Confirms DSA Censorship Regime Is Broken

**原文标题**: EU-Backed Appeals Center Accidentally Confirms DSA Censorship Regime Is Broken

**原文链接**: [https://reclaimthenet.org/eu-dsa-appeals-centre-report-exposes-content-censorship-failures](https://reclaimthenet.org/eu-dsa-appeals-centre-report-exposes-content-censorship-failures)

生成摘要时出错

---

## 71. Show HN: Ktx – Open-source executable context layer for data agents

**原文标题**: Show HN: Ktx – Open-source executable context layer for data agents

**原文链接**: [https://github.com/Kaelio/ktx](https://github.com/Kaelio/ktx)

生成摘要时出错

---

## 72. Barthelme, the Houstonian

**原文标题**: Barthelme, the Houstonian

**原文链接**: [https://www.theparisreview.org/blog/2026/05/22/barthelme-the-houstonian/](https://www.theparisreview.org/blog/2026/05/22/barthelme-the-houstonian/)

生成摘要时出错

---

## 73. Prolific Wikipedia editors are threatening to go on strike

**原文标题**: Prolific Wikipedia editors are threatening to go on strike

**原文链接**: [https://www.theverge.com/report/939442/wikipedia-editors-protest-wikimedia-layoffs-strike](https://www.theverge.com/report/939442/wikipedia-editors-protest-wikimedia-layoffs-strike)

生成摘要时出错

---

## 74. Bttf is a command line datetime Swiss army knife

**原文标题**: Bttf is a command line datetime Swiss army knife

**原文链接**: [https://github.com/BurntSushi/bttf](https://github.com/BurntSushi/bttf)

生成摘要时出错

---

## 75. Claude Code – Everything you can configure that the docs don't tell you

**原文标题**: Claude Code – Everything you can configure that the docs don't tell you

**原文链接**: [https://buildingbetter.tech/p/i-read-the-claude-code-source-code](https://buildingbetter.tech/p/i-read-the-claude-code-source-code)

生成摘要时出错

---

## 76. Various LLM Smells

**原文标题**: Various LLM Smells

**原文链接**: [https://shvbsle.in/various-llm-smells/](https://shvbsle.in/various-llm-smells/)

生成摘要时出错

---

## 77. Digital Identity Management in Norway Is a Catastrophe

**原文标题**: Digital Identity Management in Norway Is a Catastrophe

**原文链接**: [https://www.uio.no/english/research/research-news/articles/2026/digital-id-management-is-a-catastrophe.html](https://www.uio.no/english/research/research-news/articles/2026/digital-id-management-is-a-catastrophe.html)

生成摘要时出错

---

## 78. Is This Sustainable?

**原文标题**: Is This Sustainable?

**原文链接**: [https://jamiehurst.co.uk/2026-05-24_ai-sustainable](https://jamiehurst.co.uk/2026-05-24_ai-sustainable)

生成摘要时出错

---

## 79. Tesla's AI trainers don't trust its self-driving tech – or its safety stats

**原文标题**: Tesla's AI trainers don't trust its self-driving tech – or its safety stats

**原文链接**: [https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/](https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/)

生成摘要时出错

---

## 80. Bill C-22 Is a Mess of the Government's Own Making

**原文标题**: Bill C-22 Is a Mess of the Government's Own Making

**原文链接**: [https://ethanplant.ca/writing/bill-c22-is-a-mess/](https://ethanplant.ca/writing/bill-c22-is-a-mess/)

生成摘要时出错

---

## 81. Bitburner, programming-based incremental game

**原文标题**: Bitburner, programming-based incremental game

**原文链接**: [https://bitburner-official.github.io/](https://bitburner-official.github.io/)

生成摘要时出错

---

## 82. SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims

**原文标题**: SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims

**原文链接**: [https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

生成摘要时出错

---

## 83. Euro-Office: General availability set for June 9

**原文标题**: Euro-Office: General availability set for June 9

**原文链接**: [https://nextcloud.com/blog/euro-office-general-availability-set-for-june-9/](https://nextcloud.com/blog/euro-office-general-availability-set-for-june-9/)

生成摘要时出错

---

## 84. Anthropic raises $65B in Series H funding at $965B post-money valuation

**原文标题**: Anthropic raises $65B in Series H funding at $965B post-money valuation

**原文链接**: [https://www.anthropic.com/news/series-h](https://www.anthropic.com/news/series-h)

生成摘要时出错

---

## 85. Nitpicking the shell history scene in 'Tron: Legacy'

**原文标题**: Nitpicking the shell history scene in 'Tron: Legacy'

**原文链接**: [https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/)

生成摘要时出错

---

## 86. Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue

**原文标题**: Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue

**原文链接**: [https://llmgame.scalex.dev](https://llmgame.scalex.dev)

生成摘要时出错

---

## 87. Avoid Using "< [Cdata[ ]]>" in RSS

**原文标题**: Avoid Using "< [Cdata[ ]]>" in RSS

**原文链接**: [https://waspdev.com/articles/2026-05-11/avoid-using-cdata-in-rss](https://waspdev.com/articles/2026-05-11/avoid-using-cdata-in-rss)

生成摘要时出错

---

## 88. The Nvidia Tax

**原文标题**: The Nvidia Tax

**原文链接**: [https://www.cringely.com/2026/05/29/the-nvidia-tax/](https://www.cringely.com/2026/05/29/the-nvidia-tax/)

生成摘要时出错

---

## 89. But It Happened [video]

**原文标题**: But It Happened [video]

**原文链接**: [https://www.youtube.com/watch?v=tlQ7EoJDTQY](https://www.youtube.com/watch?v=tlQ7EoJDTQY)

生成摘要时出错

---

## 90. Why the failure of Blue Origin's New Glenn rocket is so catastrophic

**原文标题**: Why the failure of Blue Origin's New Glenn rocket is so catastrophic

**原文链接**: [https://arstechnica.com/space/2026/05/heres-why-the-failure-of-blue-origins-new-glenn-rocket-is-so-catastrophic/](https://arstechnica.com/space/2026/05/heres-why-the-failure-of-blue-origins-new-glenn-rocket-is-so-catastrophic/)

生成摘要时出错

---

## 91. The most unlikely school bag

**原文标题**: The most unlikely school bag

**原文链接**: [https://www.carryology.com/insights/carry-culture/the-tale-of-the-worlds-most-unlikely-school-bag/](https://www.carryology.com/insights/carry-culture/the-tale-of-the-worlds-most-unlikely-school-bag/)

生成摘要时出错

---

## 92. Unix in East Germany (GDR) (1990)

**原文标题**: Unix in East Germany (GDR) (1990)

**原文链接**: [https://groups.google.com/g/comp.unix.wizards/c/QX_dxElrVNs](https://groups.google.com/g/comp.unix.wizards/c/QX_dxElrVNs)

生成摘要时出错

---

## 93. News about Raspberry Pi 6 and Microcontroller Development

**原文标题**: News about Raspberry Pi 6 and Microcontroller Development

**原文链接**: [https://www.jeffgeerling.com/blog/2026/news-about-raspberry-pi-6-and-microcontroller-development/](https://www.jeffgeerling.com/blog/2026/news-about-raspberry-pi-6-and-microcontroller-development/)

生成摘要时出错

---

## 94. The Current Crisis: What's Happening to Science in America

**原文标题**: The Current Crisis: What's Happening to Science in America

**原文链接**: [https://www.science.org/content/blog-post/current-crisis-what-s-happening-science-america](https://www.science.org/content/blog-post/current-crisis-what-s-happening-science-america)

生成摘要时出错

---

## 95. I hated writing until I learned there’s a science to it (2024)

**原文标题**: I hated writing until I learned there’s a science to it (2024)

**原文链接**: [https://www.science.org/content/article/i-hated-writing-until-i-learned-there-s-science-it](https://www.science.org/content/article/i-hated-writing-until-i-learned-there-s-science-it)

生成摘要时出错

---

## 96. The Lone Lisp Heap

**原文标题**: The Lone Lisp Heap

**原文链接**: [https://www.matheusmoreira.com/articles/lone-lisp-heap](https://www.matheusmoreira.com/articles/lone-lisp-heap)

生成摘要时出错

---

## 97. Trial by Fire

**原文标题**: Trial by Fire

**原文链接**: [https://yusufaytas.com/trial-by-fire](https://yusufaytas.com/trial-by-fire)

生成摘要时出错

---

## 98. Using Tailscale with an OrbStack VM on macOS

**原文标题**: Using Tailscale with an OrbStack VM on macOS

**原文链接**: [https://github.com/highpost/tailscale-macos-vm](https://github.com/highpost/tailscale-macos-vm)

生成摘要时出错

---

## 99. Coalton is an efficient, statically typed Lisp with ideas from Haskell and OCaml

**原文标题**: Coalton is an efficient, statically typed Lisp with ideas from Haskell and OCaml

**原文链接**: [https://coalton-lang.github.io/](https://coalton-lang.github.io/)

生成摘要时出错

---

## 100. EU fines Temu €200M for allowing sale of illegal products

**原文标题**: EU fines Temu €200M for allowing sale of illegal products

**原文链接**: [https://www.bbc.co.uk/news/articles/c1k2ydn1rz8o](https://www.bbc.co.uk/news/articles/c1k2ydn1rz8o)

生成摘要时出错

---

