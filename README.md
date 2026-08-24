# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-24.md)

*最后自动更新时间: 2026-08-24 17:58:58*
## 1. 小米：新处理器单线程性能媲美苹果，多线程表现大幅领先

**原文标题**: Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded

**原文链接**: [https://twitter.com/lemire/status/2091894299289874926](https://twitter.com/lemire/status/2091894299289874926)

小米推出了 Xring O3，这是一款向当前行业领导者发起挑战的高性能 CPU。基准测试显示，该芯片的 Geekbench 单核得分达到 3,945 分——基本与苹果当前的性能水平持平——并实现了前所未有的 15,221 分多核得分。

Xring O3 的核心技术特性包括：

*   **海量缓存：** 该芯片拥有 44 MB 的总缓存，超过了许多现代英特尔和 AMD 笔记本电脑处理器。
*   **先进的核心架构：** 它采用了 C1-Ultra 核心，其“宽度”惊人，拥有 21 个执行端口。这超过了大多数桌面 CPU，可实现极高程度的指令并行执行。
*   **专用加速：** 该架构支持用于矩阵和 AI 加速的 SME2，以及用于数据并行的 SVE2。它包含 6 个 128 位 SIMD 单元，代表了当前 ARM 芯片设计的顶尖水平。
*   **性能趋势：** 尽管 AMD 的 Zen 5 在 SIMD 宽度（512 位）上仍保持优势，但 Xring O3 在算术和执行单元的数量上处于领先地位。

文章总结道，这款处理器反映了更广泛的行业趋势，即利用不断增加的晶体管数量来驱动大规模并行处理和更大的缓存。虽然苹果可能会通过下次发布重新夺回领先地位，但 Xring O3 标志着移动处理能力的一个重要里程碑，其性能已足以媲美甚至在某些情况下超越桌面级硬件。

---

## 2. MS Paint 和照片应用甚至会为本地生成的输出添加包含 GUID 的不可见水印。

**原文标题**: MS Paint and Photos inivisibly watermark even locally generated output with GUID

**原文链接**: [https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/)

对微软画图（Paint）和照片（Photos）应用的逆向工程揭示，即使图像是在设备本地生成的，这些应用也会在 AI 生成的图像中嵌入不可见的、由服务器颁发的 GUID（全局唯一标识符）。

研究强调了 Copilot+ PC 上“共同创作者”（Cocreator）等 AI 功能的混合工作流。虽然实际的图像推理（Stable Diffusion）是在本地 NPU 上进行的，但该过程并非完全离线。在生成开始前，应用会将用户的提示词发送到微软服务器进行审核。服务器会返回“修订后的提示词”以及一个唯一的 `watermarkId`（16 字节的 GUID）。

随后，一个名为 `Watermarker.dll` 的本地组件会利用一种块域、SVD 风格的隐性水印技术，将该 GUID 嵌入到图像像素中。此过程是强制性的；如果水印嵌入失败，应用会触发生成错误，而不会提供无水印的图像。

该系统与 **C2PA 内容凭据（Content Credentials）** 深度集成。嵌入在像素中的同一个 GUID 也会作为“软绑定”记录在文件的 C2PA 元数据中。这使得图像即使在文件级元数据被剥离的情况下，由于标识符仍隐藏在像素数据内，依然可以链接回其来源记录。

为了维持这一溯源链，画图应用限制 AI 生成的图像仅能保存为兼容 C2PA 的格式（PNG、JPEG、GIF 和 .paint），明确排除了 BMP 等传统格式。归根结底，这种架构确保了“本地”AI 生成仍与微软云端挂钩，以便进行审核、追踪以及负责任 AI 标准的执行。

---

## 3. IPFS 维护者正在逐步收尾

**原文标题**: IPFS Maintainers Winding Down

**原文链接**: [https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/)

在 Shipyard 发布的一份更新中，作者 Cameron Wood 和 Adin Schmahmann 概述了 IPFS 生态系统的重大战略转型：向**“后网关时代”**（Post Gateway World）过渡。

多年来，公共 HTTP 网关（如 `ipfs.io`）一直是 Web 用户访问 IPFS 内容的主要桥梁。然而，维护者认为，这些网关已成为中心化的单点故障，带来了隐私风险和性能瓶颈，这与去中心化网络的核心使命背道而驰。

**此次转型的关键点包括：**

*   **转向直接检索：** 重心正从通过网关代理数据转向“直接检索”，即由浏览器直接从 IPFS 网络获取内容。
*   **Web 原生 IPFS：** Shipyard 正在优先推动 IPFS 在标准 Web 环境中的无缝运行，利用 **Helia**（一个 JavaScript 版本的 IPFS 实现）等工具，使 Web 应用程序能够作为轻节点运行。
*   **缩减中心化基础设施：** 通过摆脱“网关优先”模式，维护者旨在降低与托管公共基础设施相关的巨额运营成本和中心化风险。
*   **提升韧性：** 直接检索使用户成为点对点网络的积极参与者，而非中心化服务的被动消费者，从而使生态系统更具抗审查能力。

总之，这种“缩减”是指逐步淡化对传统中心化 HTTP 网关的依赖。这一演进标志着在实现 IPFS 原始愿景方面迈出了关键一步：打造一个真正的点对点互联网，直接从网络中检索数据，确保协议具有更高的隐私性、去中心化程度和长期可持续性。

---

## 4. 黑石旗下一家房地产公司泄露了社保号、出生日期、地址等信息。

**原文标题**: A Blackstone real estate company exposed SSN digits, DOBs, addresses and more

**原文链接**: [https://alexschapiro.com/security/vulnerability/2026/07/16/beam-living-graphql-data-exposure](https://alexschapiro.com/security/vulnerability/2026/07/16/beam-living-graphql-data-exposure)

在通过黑石集团（Blackstone）旗下的房地产公司 Beam Living 申请公寓时，一名安全研究人员在其租赁门户网站中发现了一个严重的敏感数据漏洞。

该漏洞涉及一个 GraphQL 查询，该查询使用用户的电子邮件地址作为查找变量，而非安全的会话 Cookie。研究人员只需在查询中输入其他用户的电子邮件地址，即可访问系统中任何申请人或担保人的敏感个人身份信息（PII）。泄露的数据包括：
* 社会安全号码的后四位
* 出生日期和家庭住址
* 电话号码和 IP 地址
* 信用评分和收入核实状态

该漏洞影响了由 Beam Living 管理的纽约市多个主要住宅社区，包括 StuyTown、Peter Cooper Village、8 Spruce、Kips Bay Court 和 Parker Towers。

研究人员记录了始于 6 月 14 日的坎坷披露过程。尽管多次向 Beam Living 的通用邮箱和安全邮箱发送邮件，该公司在数周内始终未予置评。直到 7 月初研究人员联系了一名租赁代理并最终与住户体验团队取得联系后，问题才得到处理。

尽管 Beam Living 的代表最初声称“完全没有任何问题”，但研究人员确认该漏洞已于 7 月 9 日被悄悄修复。作者在文末批评了该公司缺乏透明度以及对严重安全漏洞处理不当的行为，并指出即使是像黑石集团这样的大型公司，往往也未能提供适当的责任披露渠道。

---

## 5. 公共服务正因大语言模型生成的福利申诉而日益承压。

**原文标题**: Public services are increasingly strained by LLM-written appeals for benefits

**原文链接**: [https://arxiv.org/abs/2608.16603](https://arxiv.org/abs/2608.16603)

由 Chris Schmitz、Lewis Hammond 和 Alan Chan（2026年）撰写的论文《政府服务智能体泛滥的特征分析》（Characterizing Agentic Flooding of Government Services），探讨了 AI 智能体和大语言模型（LLMs）如何导致公共服务需求出现前所未有的激增。

作者识别出一种被称为**“智能体泛滥”（agentic flooding）**的现象：由于利用 AI 生成福利申请、政策咨询和法律申诉的门槛极低且成本低廉，政府基础设施正面临过载。虽然这些工具能提高公众获取服务的便捷性，但同时也让尚未做好准备的政府系统承受巨大压力。

该研究的主要贡献包括：

*   **广泛影响的证据：** 基于涉及 11 个司法管辖区的 84 个潜在案例数据集，作者得出结论，智能体泛滥已成为现实，这主要源于大语言模型能够以极低成本大规模生成复杂文本。
*   **风险评估：** 研究人员开发了一个风险矩阵来识别最脆弱的服务。他们发现，**经济收益高但行政程序复杂的服务**在短期内面临最高的泛滥风险。
*   **政府应对策略：** 论文评估了政府可能的应对方式。虽然“增加摩擦”的措施（如提高费用或复杂的身份验证）可以遏制泛滥，但这些措施往往会为服务本应帮助的人群设置障碍。

作者在结论中建议，政府应采取前瞻性的短期缓解策略，在管理需求的同时，不损害获取基本公共服务的公平性。

---

## 6. 欧洲是如何扼杀创客与小微创业者的

**原文标题**: How Europe is killing makers and micro-entrepreneurs

**原文链接**: [https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs)

文章指出，欧盟定于2026年8月全面实施的新《包装和包装废弃物法规》（PPWR）威胁着微型企业家、创客和艺术家的生存。虽然“生产者责任延伸制度”（EPR）——即要求企业为其包装回收提供资金——的初衷是好的，但其针对小规模卖家的实施方式存在严重缺陷。

核心问题在于碎片化。由于缺乏统一的欧盟系统，卖家必须在发货的每一个成员国分别注册并履行申报义务。对于一个仅销售少量商品的微型企业来说，仅在少数几个国家的年度行政费和“授权代表”成本就可能超过1000欧元。这种财务和行政负担与实际产生的废弃物量极不成比例，往往导致欧洲创客向美国发货比向欧盟邻国发货更具经济可行性。

硬件爱好者平台 Lectronz 警告称，这些规则会扼杀初创企业的实验阶段，从而阻碍创新。如果小型创作者负担不起进入市场的成本，整个创新生态系统都将面临风险。

为了挽救微型企业的单一市场，作者提出了三项解决方案：
1. **设立微量豁免阈值：** 豁免小业务量和低营业额卖家的跨境义务。
2. **建立欧盟一站式服务平台：** 创建类似于增值税一站式服务（VAT OSS）系统的中央注册和申报门户。
3. **平台集体管理：** 允许像 Lectronz 这样的平台作为单一实体代表其所有卖家处理合规事宜。

文章最后呼吁读者签署请愿书并向欧盟委员会提供反馈，以防止欧洲最小型企业遭受意外的毁灭。

---

## 7. 整个旧金山市化身电子游戏

**原文标题**: The entire city of San Francisco as a video game

**原文链接**: [https://sf.thijs.gg/](https://sf.thijs.gg/)

This text appears to be the interface or landing page for a 2026 Apple Inc. project titled **"San Francisco -- The Game."** It describes an ambitious digital recreation of the city designed as an interactive, online "GameCity."

Key features and information include:

*   **Exploration and Movement:** The simulation allows users to explore San Francisco using standard video game controls (WASD). Players can navigate the city on foot, in vehicles, or via a "glider." It also includes a "Click to Teleport" feature for instant travel and adjustable camera distances for a third-person perspective.
*   **Gameplay Mechanics:** The UI displays resource counters for **wood, stone, and metal**, suggesting that the game may involve crafting, building, or survival elements. There are also toggles for "World Safe" and "Life Off" modes, implying customizable environmental settings or the ability to remove NPCs/traffic.
*   **Technical Specifications:** The system uses "tile streaming" to load the city’s neighborhoods dynamically. The interface tracks "Z-levels" (zoom or elevation layers) and provides technical debug logs, indicating a high-fidelity "digital twin" of the city that renders based on the player’s location.
*   **Status and Detail:** The simulation features a "Detail Mode" and neighborhood readiness indicators (e.g., "Neighborhood Ready 100%").

In summary, the document outlines a sophisticated urban simulation of San Francisco that blends open-world exploration with resource management and high-end map streaming technology.

---

## 8. OpenAI: GPT 5.6 Sol price reduction (until at least Nov 21)

**原文标题**: OpenAI: GPT 5.6 Sol price reduction (until at least Nov 21)

**原文链接**: [https://developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)

生成摘要时出错

---

## 9. Hot Chips 2026: CUDA Targets RISC-V – By Chester Lam

**原文标题**: Hot Chips 2026: CUDA Targets RISC-V – By Chester Lam

**原文链接**: [https://chipsandcheese.com/p/hot-chips-2026-cuda-targets-risc](https://chipsandcheese.com/p/hot-chips-2026-cuda-targets-risc)

生成摘要时出错

---

## 10. Jabber/XMPP: 25 Years of Digital Independence

**原文标题**: Jabber/XMPP: 25 Years of Digital Independence

**原文链接**: [https://gultsch.de/posts/25-years-of-digital-independence/](https://gultsch.de/posts/25-years-of-digital-independence/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 2 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 3 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 4 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 5 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 6 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 7 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 8 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 9 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 10 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 11 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 12 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 13 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 14 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 15 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 16 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 17 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 18 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 19 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 20 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 21 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 22 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 23 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 24 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 25 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 26 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 27 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 28 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 29 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 30 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 31 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 32 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 33 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 34 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 35 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 36 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 37 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 38 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 39 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 40 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 41 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 42 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 43 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 44 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 45 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 46 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 47 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 48 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 49 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 50 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 51 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 52 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 53 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 54 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 55 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 56 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 57 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 58 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 59 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 60 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 61 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 62 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 63 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 64 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 65 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 66 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 67 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 68 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 69 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 70 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 71 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 72 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 73 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 74 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 75 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 76 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 77 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 78 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 79 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 80 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 81 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 82 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 83 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 84 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 85 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 86 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 87 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 88 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 89 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 90 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 91 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 92 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 93 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 94 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 95 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 96 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 97 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 98 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 99 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 100 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 101 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 102 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 103 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 104 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 105 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 106 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 107 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 108 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 109 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 110 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 111 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 112 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 113 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 114 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 115 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 116 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 117 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 118 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 119 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 120 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 121 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 122 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 123 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 124 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 125 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 126 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 127 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 128 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 129 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 130 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 131 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 132 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 133 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 134 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 135 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 136 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 137 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 138 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 139 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 140 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 141 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 142 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 143 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 144 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 145 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 146 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 147 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 148 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 149 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 150 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 151 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 152 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 153 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 154 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 155 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 156 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 157 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 158 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 159 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 160 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 161 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 162 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 163 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 164 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 165 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 166 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 167 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 168 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 169 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 170 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 171 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 172 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 173 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 174 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 175 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 176 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 177 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 178 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 179 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 180 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 181 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 182 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 183 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 184 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 185 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 186 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 187 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 188 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 189 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 190 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 191 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 192 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 193 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 194 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 195 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 196 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 197 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 198 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 199 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 200 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 201 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 202 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 203 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 204 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 205 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 206 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 207 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 208 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 209 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 210 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 211 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 212 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 213 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 214 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 215 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 216 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 217 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 218 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 219 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 220 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 221 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 222 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 223 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 224 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 225 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 226 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 227 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 228 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 229 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 230 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 231 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 232 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 233 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 234 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 235 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 236 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 237 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 238 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 239 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 240 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 241 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 242 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 243 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 244 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 245 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 246 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 247 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 248 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 249 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 250 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 251 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 252 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 253 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 254 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 255 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 256 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 257 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 258 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 259 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 260 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 261 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 262 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 263 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 264 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 265 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 266 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 267 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 268 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 269 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 270 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 271 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 272 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 273 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 274 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 275 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 276 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 277 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 278 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 279 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 280 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 281 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 282 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 283 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 284 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 285 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 286 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 287 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 288 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 289 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 290 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 291 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 292 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 293 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 294 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 295 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 296 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 297 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 298 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 299 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 300 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 301 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 302 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 303 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 304 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 305 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 306 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 307 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 308 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 309 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 310 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 311 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 312 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 313 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 314 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 315 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 316 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 317 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 318 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 319 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 320 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 321 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 322 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 323 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 324 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 325 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 326 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 327 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 328 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 329 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 330 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 331 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 332 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 333 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 334 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 335 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 336 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 337 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 338 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 339 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 340 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 341 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 342 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 343 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 344 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 345 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 346 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 347 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 348 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 349 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 350 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 351 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 352 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 353 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 354 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 355 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 356 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 357 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 358 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 359 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 360 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 361 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 362 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 363 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 364 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 365 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 366 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 367 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 368 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 369 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 370 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 371 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 372 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 373 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 374 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 375 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 376 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 377 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 378 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 379 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 380 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 381 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 382 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 383 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 384 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 385 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 386 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 387 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 388 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 389 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 390 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 391 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 392 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 393 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 394 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 395 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 396 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 397 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 398 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 399 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 400 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 401 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 402 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 403 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 404 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 405 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 406 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 407 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 408 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 409 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 410 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 411 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 412 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 413 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 414 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 415 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 416 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 417 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 418 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 419 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 420 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 421 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 422 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 423 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 424 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 425 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 426 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 427 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 428 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 429 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 430 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 431 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 432 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 433 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 434 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 435 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 436 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 437 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 438 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 439 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 440 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 441 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 442 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 443 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 444 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 445 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 446 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 447 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 448 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 449 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 450 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 451 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 452 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 453 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 454 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 455 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 456 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 457 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 458 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 459 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 460 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 461 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 462 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 463 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 464 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 465 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 466 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 467 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 468 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 469 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 470 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 471 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 472 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 473 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 474 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 475 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 476 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 477 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 478 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 479 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 480 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 481 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 482 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 483 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 484 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 485 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 486 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 487 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 488 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 489 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 490 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 491 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 492 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 493 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 494 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 495 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 496 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 497 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 498 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 499 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 500 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 501 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 502 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 503 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 504 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 505 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 506 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 507 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 508 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 509 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 510 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 511 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 512 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 513 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 514 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 515 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 516 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 517 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 518 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 519 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 520 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 521 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
