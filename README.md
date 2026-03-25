# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-25.md)

*最后自动更新时间: 2026-03-25 18:24:58*
## 1. 我在电影《挽救计划》中的天文摄影

**原文标题**: My Astrophotography in the Movie Project Hail Mary

**原文链接**: [https://rpastro.square.site/s/stories/phm](https://rpastro.square.site/s/stories/phm)

根据提供的内容，简要总结如下：

**Rod Prazeres** 宣布，他的天文摄影作品将出现在电影版《挽救计划》（Project Hail Mary）中。具体而言，他的天文影像已被选中用于该片的**片尾字幕序列**。此次合作凸显了专业真实的天文摄影在增强这部根据安迪·威尔小说改编的重磅科幻电影视觉呈现方面的应用。

---

## 2. Ente 的本地 LLM 应用

**原文标题**: Local LLM App by Ente

**原文链接**: [https://ente.com/blog/ensu/](https://ente.com/blog/ensu/)

Ente 宣布推出 Ensu，这是一款全新的离线、开源大语言模型 (LLM) 应用。该项目源于一种信念，即人工智能技术至关重要，不应仅由“科技巨头”掌控，并对隐私泄露、监控风险以及中心化依赖的风险表示了担忧。

Ensu 的功能类似于 ChatGPT，但完全在设备本地运行，从而确保了绝对隐私和零成本使用。虽然 Ente 承认本地模型目前在原始性能上仍落后于前沿模型，但他们认为这些模型正跨越一个“能力阈值”，足以胜任大多数任务——例如私人反思、文学讨论，或在没有网络连接的旅途中使用。

**核心技术细节：**
*   **跨平台：** 支持 iOS、Android、macOS、Linux、Windows 及网页端。
*   **架构：** 核心逻辑采用 Rust 编写，移动端利用原生包装器，桌面端则使用 Tauri。
*   **开源：** 代码已公开，履行了 Ente 对透明度的承诺。
*   **安全性：** 虽然端到端加密 (E2EE) 同步和备份功能已开发完成，但为了根据初始用户反馈灵活调整架构，这些功能在首个版本中暂时禁用。

**未来方向：**
Ensu 目前属于 “Ente Labs” 项目。开发者正在探索多个方向，包括将该应用发展为记录笔记的“第二大脑”、实用型 Android 启动器，或是具备长期记忆的个人智能体。团队正积极寻求社区反馈，以规划产品路线图。

---

## 3. 关于慢他妈下来的思考

**原文标题**: Thoughts on Slowing the Fuck Down

**原文链接**: [https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/)

《关于“彻底慢下来”的思考》一文批判了当前业界对高速度、代理式（agentic）AI 编程的痴迷。在反思了一整年的“进展”后，作者认为，将完整项目委托给自主代理已导致软件质量下降，具体表现为代码脆弱、UI 故障以及无法挽回的技术债。

作者强调了人类开发者与 AI 开发者之间的本质区别：人类充当了天然的“瓶颈”。因为人类能感受到错误带来的“痛苦”，且产出能力有限，所以最终会选择学习和重构。相比之下，代理缺乏这种学习闭环，能瞬间“倾泻出”数千行代码。这导致微小的错误（即“小瑕疵”）以不可持续的速度累积，在开发者意识到之前，就已经制造出了一个“代码库怪兽”。

此外，作者指出，“代理式搜索”存在**低召回率**的问题。代理通常只做局部决策，缺乏对系统的全局理解，导致大量的代码重复和“习得性复杂”。过去大型人类组织需要数年才能搞砸的事情，现在一个小团队利用代理在短短几周内就能将其摧毁。

为了防止这场“狂热之梦”演变成噩梦，作者提出了一套更严谨的方法：
*   **在限定任务中使用代理：** 将“乏味的琐事”或非关键工具交给代理，但人类必须作为最终的质量把关者。
*   **人工架构设计：** 亲手编写核心 API 和架构，以保持系统的“整体感”并确保深刻理解。
*   **慢下来：** 为 AI 生成的代码量设置限制，使其与你彻底审查代码的能力相匹配。
*   **拥抱摩擦：** 意识到编写代码时的阻力，正是让开发者能够学习并保持自主性的关键。

最终，作者认为，保持人类的自主性和纪律是构建“激发喜悦而非产出垃圾”的软件的唯一途径。

---

## 4. 陪审团认定 Meta 为牟利蓄意伤害儿童，做出里程碑式裁决。

**原文标题**: Jury says Meta knowingly harmed children for profit, awarding landmark verdict

**原文链接**: [https://www.latimes.com/business/story/2026-03-25/jury-says-meta-knowingly-harmed-children-for-profit-awarding-landmark-verdict](https://www.latimes.com/business/story/2026-03-25/jury-says-meta-knowingly-harmed-children-for-profit-awarding-landmark-verdict)

新墨西哥州的一个陪审团对 Meta 作出了一项具有里程碑意义的裁决，认定该公司明知其平台（包括 Instagram 和 Facebook）损害儿童心理健康并隐瞒儿童性剥削证据，应承担法律责任。

陪审团认定，Meta 将利润置于安全之上，并通过利用未成年人弱点的“违背良知”的贸易行为违反了该州的《不公平行为法》。因此，Meta 被勒令支付 3.75 亿美元的罚金——即针对所认定的数千项违规行为，按每项 5000 美元的最高标准处罚。

这场为期七周的审判依据了内部通信、举报人证词以及一项卧底调查，调查中特工伪装成儿童并记录了性诱导行为。检察官成功辩称，Meta 的算法旨在以牺牲儿童安全为代价来最大化用户参与度，同时在平台风险方面误导了公众。

虽然这一裁决标志着 Meta 在法律上的重大挫败，但该公司股价在消息传出后有所上涨。一名发言人确认了上诉计划，并坚称公司正努力保护青少年。

此案是日益高涨的诉讼浪潮中的“分水岭时刻”，目前已有 40 多个州的州总检察长提起类似诉讼，指控社交媒体功能具有刻意诱导成瘾的特性。新墨西哥州审判的第二阶段将于 5 月进行，届时法官将裁定 Meta 的平台是否构成“公共滋扰”，以及该公司是否必须资助公共项目以治理所造成的危害。

---

## 5. Meta和YouTube在具有里程碑意义的社交媒体成瘾案中被判定有过失

**原文标题**: Meta and YouTube Found Negligent in Landmark Social Media Addiction Case

**原文链接**: [https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html](https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html)

无法访问文章链接。

---

## 6. TurboQuant：以极致压缩重新定义 AI 效率

**原文标题**: TurboQuant: Redefining AI efficiency with extreme compression

**原文链接**: [https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

Google Research 推出了 TurboQuant，这是一套具有理论支撑的量化算法，旨在大幅压缩大语言模型 (LLM) 和向量搜索引擎中使用的高维向量。

TurboQuant 的主要目标是消除传统量化中的“内存开销”——传统方法通常需要存储额外的常数，这往往会抵消压缩带来的收益。它通过以下两项核心创新实现了这一目标：

*   **PolarQuant：** 该方法将笛卡尔坐标转换为极坐标系（半径和角度）。由于这些角度的几何结构是可预测的，该模型避免了传统“方形”网格量化所需的昂贵数据归一化和常数存储。
*   **量化 Johnson-Lindenstrauss (QJL)：** 这种“1 比特技巧”利用数学变换在缩小数据规模的同时保留关键关系。它充当纠错阶段，仅使用一个符号位来消除偏差，并保持注意力评分的高准确性。

**关键结果与影响：**
*   **效率：** 在使用 Gemma 和 Mistral 等模型的测试中，TurboQuant 将键值 (KV) 缓存内存减少了 6 倍，并在 H100 GPU 上实现了高达 8 倍的注意力逻辑值 (attention logits) 计算加速。
*   **准确性：** 该系统在实现这些提升的同时保持了零精度损失和接近最优的失真率，性能优于 PQ 和 RabbiQ 等现有基准。
*   **通用性：** TurboQuant 具有“数据无关性” (data-oblivious)，这意味着它无需特定数据集调优或模型微调即可高效工作。

通过解决 KV 缓存瓶颈，TurboQuant 使大语言模型能够更高效地处理更长的上下文。除大语言模型外，该技术预计将变革 Google 的大规模语义搜索，从而以极低的内存需求在数十亿个向量中实现更快速、更准确的检索。

---

## 7. Antimatter has been transported for the first time

**原文标题**: Antimatter has been transported for the first time

**原文链接**: [https://www.nature.com/articles/d41586-026-00950-w](https://www.nature.com/articles/d41586-026-00950-w)

欧洲核子研究中心（CERN）的科学家们首次成功运输反物质，实现了历史性的里程碑。3月24日，一支研究团队将92个反质子装载于卡车后部的特制“瓶子”中进行移动。该车辆在日内瓦附近的CERN场区行驶了超过8公里，最高时速达到42公里。

反物质因其在与普通物质接触时会瞬间湮灭并完全转化为能量，而极其难以存储和移动。为了克服这一难题，研究团队利用一种特殊的陷阱，通过磁场使粒子悬浮，从而防止它们触碰容器壁。

此次实验的主要目标是将反质子从其诞生的“反物质工厂”转移到不受实验噪声干扰、更安静的环境中。移动这些粒子使物理学家能够进行比目前在生产现场更高精度的测量。

该项目由杜塞尔多夫海因里希·海涅大学的研究人员领导，实现了科学界数十年来的夙愿。CERN目前是世界上唯一能够生产可用数量反质子的机构。这一技术突破为探究宇宙的基本奥秘（如大爆炸后物质与反物质之间不明原因的差异）提供了新方法。参与该项目的物理学家称此次成功运输为“技术奇迹”，为粒子物理研究开启了新的大门。

---

## 8. Show HN: I built a site that maps the web from a bounty hunter's perspective

**原文标题**: Show HN: I built a site that maps the web from a bounty hunter's perspective

**原文链接**: [https://www.neobotnet.com/](https://www.neobotnet.com/)

**Neobotnet** is a specialized web reconnaissance platform designed specifically for bug bounty hunters and cybersecurity researchers. Launched as a "Show HN" project, the site aims to map the internet from an adversarial perspective, providing a comprehensive view of an organization's digital footprint.

The core purpose of Neobotnet is to streamline the reconnaissance phase of security testing. It functions as a powerful search engine and discovery tool that aggregates data on subdomains, IP addresses, open ports, and underlying technologies. By continuously scanning and indexing the web, the platform allows users to visualize a target's attack surface and identify potential vulnerabilities that might be missed by standard search engines.

**Key features include:**
*   **Subdomain Discovery:** Identifying hidden or forgotten subdomains belonging to a target organization.
*   **Technology Profiling:** Mapping the specific software, frameworks, and services running on various servers.
*   **Asset Tracking:** Monitoring changes in an organization’s infrastructure over time to spot newly exposed risks.
*   **Advanced Filtering:** Allowing researchers to narrow down results by specific criteria, such as geographic location, hosting provider, or port status.

The project emphasizes scale and automation, seeking to provide security professionals with the data necessary to find "low-hanging fruit" and complex misconfigurations. By centralizing infrastructure data, Neobotnet helps bounty hunters more efficiently map out perimeters and uncover security gaps before they can be exploited by malicious actors.

---

## 9. Goodbye to Sora

**原文标题**: Goodbye to Sora

**原文链接**: [https://twitter.com/soraofficialapp/status/2036532795984715896](https://twitter.com/soraofficialapp/status/2036532795984715896)

The provided text does not contain the content of an article titled "Goodbye to Sora." Instead, it is a **technical error message from the social media platform X (formerly Twitter)**.

The main points of the provided text are:
*   **Access Issue:** The website detected that JavaScript is disabled in the user's browser.
*   **Requirement:** To view the content on x.com, the user must enable JavaScript or switch to a supported browser.
*   **Support Links:** The page provides links to the Help Center, Terms of Service, Privacy Policy, and Cookie Policy for further assistance.

Because the actual article content was blocked by these browser settings, it is impossible to summarize the "Goodbye to Sora" story based on this text. To get a summary, please provide the full text of the article itself.

---

## 10. VitruvianOS – Desktop Linux Inspired by the BeOS

**原文标题**: VitruvianOS – Desktop Linux Inspired by the BeOS

**原文链接**: [https://v-os.dev](https://v-os.dev)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 2 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 3 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 4 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 5 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 6 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 7 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 8 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 9 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 10 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 11 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 12 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 13 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 14 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 15 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 16 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 17 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 18 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 19 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 20 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 21 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 22 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 23 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 24 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 25 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 26 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 27 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 28 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 29 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 30 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 31 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 32 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 33 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 34 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 35 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 36 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 37 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 38 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 39 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 40 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 41 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 42 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 43 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 44 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 45 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 46 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 47 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 48 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 49 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 50 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 51 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 52 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 53 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 54 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 55 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 56 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 57 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 58 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 59 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 60 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 61 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 62 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 63 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 64 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 65 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 66 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 67 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 68 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 69 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 70 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 71 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 72 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 73 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 74 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 75 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 76 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 77 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 78 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 79 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 80 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 81 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 82 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 83 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 84 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 85 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 86 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 87 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 88 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 89 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 90 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 91 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 92 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 93 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 94 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 95 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 96 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 97 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 98 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 99 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 100 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 101 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 102 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 103 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 104 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 105 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 106 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 107 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 108 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 109 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 110 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 111 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 112 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 113 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 114 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 115 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 116 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 117 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 118 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 119 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 120 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 121 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 122 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 123 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 124 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 125 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 126 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 127 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 128 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 129 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 130 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 131 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 132 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 133 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 134 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 135 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 136 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 137 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 138 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 139 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 140 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 141 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 142 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 143 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 144 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 145 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 146 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 147 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 148 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 149 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 150 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 151 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 152 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 153 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 154 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 155 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 156 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 157 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 158 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 159 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 160 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 161 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 162 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 163 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 164 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 165 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 166 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 167 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 168 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 169 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 170 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 171 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 172 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 173 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 174 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 175 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 176 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 177 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 178 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 179 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 180 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 181 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 182 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 183 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 184 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 185 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 186 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 187 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 188 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 189 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 190 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 191 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 192 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 193 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 194 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 195 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 196 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 197 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 198 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 199 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 200 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 201 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 202 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 203 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 204 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 205 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 206 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 207 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 208 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 209 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 210 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 211 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 212 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 213 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 214 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 215 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 216 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 217 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 218 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 219 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 220 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 221 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 222 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 223 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 224 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 225 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 226 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 227 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 228 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 229 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 230 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 231 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 232 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 233 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 234 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 235 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 236 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 237 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 238 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 239 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 240 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 241 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 242 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 243 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 244 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 245 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 246 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 247 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 248 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 249 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 250 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 251 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 252 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 253 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 254 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 255 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 256 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 257 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 258 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 259 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 260 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 261 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 262 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 263 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 264 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 265 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 266 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 267 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 268 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 269 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 270 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 271 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 272 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 273 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 274 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 275 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 276 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 277 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 278 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 279 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 280 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 281 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 282 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 283 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 284 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 285 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 286 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 287 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 288 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 289 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 290 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 291 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 292 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 293 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 294 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 295 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 296 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 297 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 298 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 299 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 300 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 301 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 302 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 303 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 304 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 305 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 306 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 307 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 308 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 309 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 310 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 311 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 312 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 313 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 314 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 315 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 316 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 317 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 318 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 319 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 320 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 321 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 322 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 323 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 324 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 325 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 326 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 327 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 328 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 329 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 330 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 331 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 332 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 333 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 334 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 335 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 336 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 337 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 338 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 339 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 340 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 341 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 342 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 343 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 344 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 345 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 346 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 347 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 348 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 349 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 350 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 351 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 352 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 353 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 354 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 355 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 356 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 357 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 358 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 359 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 360 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 361 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 362 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 363 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 364 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 365 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 366 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 367 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 368 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 369 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 370 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
