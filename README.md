# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-26.md)

*最后自动更新时间: 2025-09-26 17:49:12*
## 1. 用 Rust 实现 Firefox 的快速 UDP I/O

**原文标题**: Fast UDP I/O for Firefox in Rust

**原文链接**: [https://max-inden.de/post/fast-udp-io-in-firefox/](https://max-inden.de/post/fast-udp-io-in-firefox/)

本文详细介绍了改进 Firefox UDP I/O 堆栈的项目，旨在提高 HTTP/3 QUIC 的性能和安全性，利用了基于 Rust 的 `quinn-udp` 库。最初的实现依赖于过时的 NSPR API，阻碍了利用现代操作系统特性（如多消息 API (sendmmsg/recvmmsg) 和分段卸载 (GSO/GRO)）带来的潜在性能提升。

该项目成功地在 Windows、MacOS、Linux 和 Android 上用现代的、特定于操作系统的系统调用替换了 `sendto/recvfrom`。Linux 从 GSO/GRO 中获得了显著收益，GSO/GRO 将 UDP 分段卸载到内核或 NIC，在 CPU 密集型场景中实现了高达 4 Gbit/s 的吞吐量。每个平台都带来了独特的挑战。由于不稳定和存在 bug，Windows USO/URO 被回滚。MacOS 缺乏原生分段卸载，且未公开的批处理调用被认为部署风险过高。Android 需要对其旧版本和 socketcall 系统进行专门处理。

除了性能之外，此次迁移还通过使用内存安全的 Rust 语言进行 UDP I/O，提高了安全性。升级还启用了 QUIC ECN (显式拥塞通知) 支持，从而改善了网络拥塞管理。虽然某些特定于平台的优化需要进一步完善，但该项目代表了优化 Firefox UDP I/O 的重要一步，有助于实现更快、更安全的 HTTP/3 体验。

---

## 2. 开放社交

**原文标题**: Open Social

**原文链接**: [https://overreacted.io/open-social/](https://overreacted.io/open-social/)

本文介绍了“开放社交”的概念，将其视为当前社交媒体状态的潜在替代者，并将其与开源软件的兴起相提并论。作者认为，当前的社交媒体平台将用户数据困在其专有数据库中，造成权力失衡并阻碍用户自由。

开放社交旨在分散社交数据，让用户掌控自己的个人资料、帖子、点赞和关注。该模型采用了Bluesky开发的AT协议，用户如“Alice”和“Bob”拥有自己的互联网句柄（例如，@alice.com），其数据以签名JSON形式存储在网络上的个人存储库中，并使用“at://”URI进行链接。

这些存储库充当Web服务器，存储可通过AT协议访问的用户数据，本质上创建了一个超链接JSON记录网络，而不是社交媒体公司数据库中的行。虽然技术上很复杂，但其目标是让普通用户对此过程不可见，就像用户与Web交互而无需了解服务器技术一样。

其好处包括用户能够在不丢失其数据或社交连接的情况下切换社交应用程序，从而促进竞争并鼓励平台尊重用户权利。本文认为，这种转变可能会带来更加开放、以用户为中心的社交媒体格局，类似于开源软件的民主化效应。作者预计采用需要时间，但相信开放社交是不可避免的演变。

---

## 3. 如何理清任何混乱局面

**原文标题**: How to make sense of any mess

**原文链接**: [https://www.howtomakesenseofanymess.com](https://www.howtomakesenseofanymess.com)

如何理清任何混乱：Abby Covert通过信息架构的视角，指导读者理解和解决复杂的信息问题。本书引导读者完成一个结构化的过程，强调理解信息和与之互动的人群的重要性。

核心步骤包括：**识别混乱**，认识信息、用户和利益相关者的复杂性；**明确意图**，定义清晰的目标，并选择精确的语言来阐述它们；**面对现实**，承认所有相关的因素、渠道、背景和参与者，并使用图表来可视化情况；**选择方向**，通过定义正在制作的“内容”，理解不同级别的影响，并通过列出将被说和不被说的词语来控制词汇；**衡量距离**，设定目标，跟踪进度，并建立基线和指标，以确保项目走在正确的轨道上；**玩转结构**，探索各种分类法（层级式、异构式、顺序式）和方面，以有效地组织信息；最后，**准备调整**，预测变化，解决冲突，并适应现实情况。

本书强调信息架构的迭代性，鼓励读者拥抱模糊性，优先考虑清晰度，并根据反馈和不断变化的情况不断调整其方法。它使用相关的案例研究（“认识[姓名]”）来说明这些概念，并提供实用工具，如图表和工作表，以帮助读者将这些原则应用于他们自己的混乱情况。

---

## 4. Traefik十年征程：从零到标准

**原文标题**: Traefik's 10-Year Journey from Zero to Standard

**原文链接**: [https://traefik.io/blog/celebrating-10-years-of-traefik](https://traefik.io/blog/celebrating-10-years-of-traefik)

本文庆祝 Traefik 十周年，回顾了这款现代反向代理和负载均衡器从小型个人项目发展成为广泛采用的云原生标准的历程。作者回顾了最初的动机：通过基于容器和服务发现自动配置反向代理来简化微服务管理。

文章重点介绍了几个关键里程碑：Traefik v1 的自动服务发现和 Let's Encrypt 集成；Traefik v2 的架构重新设计，包括路由器、中间件、TCP/UDP 支持和 Kubernetes CRDs；以及 Traefik v3 专注于 Gateway API 和 OpenTelemetry 等现代标准。文章强调了云原生领域从实验到生产就绪的转变，以及 Traefik 如何适应这种演变。

展望未来，文章详细介绍了即将推出的功能：Traefik 3.5 的 NGINX 兼容层，以简化从 ingress-nginx 的迁移，以及 Traefik 3.6 的多层路由和 KNative 集成。作者还介绍了 Traefik v4 的新发布策略，其中功能将在 v3.x 版本中逐步推出，以确保更流畅的升级体验。

最后，作者强调了开源社区的关键作用，突出了他们通过代码、文档、测试和反馈做出的贡献，并宣布了一项周年纪念竞赛，为贡献者提供限量版 T 恤。文章最后对社区表示感谢，并承诺继续在不断发展的云原生生态系统中进行创新。

---

## 5. 思考机器 - 模块化流形

**原文标题**: Thinking Machines – Modular Manifolds

**原文链接**: [https://thinkingmachines.ai/blog/modular-manifolds/](https://thinkingmachines.ai/blog/modular-manifolds/)

本文探讨了在大规模神经网络中规范化张量（特别是权重矩阵）的益处，以在训练期间保持稳定性和可预测性。文章认为，将权重矩阵约束到子流形提供了一种有前景的方法，能够实现优化算法与这些约束的协同设计。

文章介绍了流形优化的概念，从一个约束到超球面的向量的简单例子开始。它强调了在切线空间中选择适当距离度量的重要性，因为它会影响最佳优化步骤的方向。

文章的核心介绍了“流形 Muon”，这是一种基于将权重矩阵约束到Stiefel流形的算法，在该流形中所有奇异值都为一。这确保了对输入向量的一致拉伸效果，防止产生过小或过大的输出。文章提出了流形 Muon 优化问题，并强调了其与原始 Muon 优化器的联系，后者约束了权重更新的谱范数。它参考了 Jianlin Su 和 Franz Louis Cesista 的工作，他们帮助开发了一种数值解。

文章最后强调这是一个活跃的研究领域。作者鼓励进一步探索流形约束、距离函数和可组合流形，用于大规模训练，旨在提高神经网络的稳定性和性能。

---

## 6. 近期国际象棋争议

**原文标题**: A recent chess controversy

**原文链接**: [https://www.chicagobooth.edu/review/did-us-chess-champion-cheat](https://www.chicagobooth.edu/review/did-us-chess-champion-cheat)

芝加哥大学布斯商学院评论的这篇文章调查了弗拉基米尔·克拉姆尼克对国际象棋特级大师中村光涉嫌作弊的指控，该指控基于中村在一次在线闪电战比赛中不太可能出现的连胜纪录。研究人员希瓦·马哈拉杰、尼古拉斯·波尔森和瓦迪姆·索科洛夫对中村在chess.com上的3500多场比赛的表现数据进行了统计分析，并得出结论：中村没有作弊的可能性为99.6%。

研究人员强调了统计分析中初始假设的重要性，特别是关于在线国际象棋作弊的普遍程度。他们使用维斯瓦纳坦·阿南德估计的作弊率，发现中村无罪的可能性很高。他们还使用更高的作弊估计值重新计算了概率，证明了这些初始假设对最终结果的影响。

该研究还强调了潜在的统计谬误。克拉姆尼克的指控被认定为“检察官谬误”，即将在无罪情况下出现证据的概率与在出现证据情况下无罪的概率混淆。中村提出的“选择性取样”的反驳也受到了质疑，因为它通过考虑观察到的连胜之外的数据而违反了似然原则。

研究人员最终强调需要对信息和数据框架进行批判性评估，警告不要赋予绝对概率（克伦威尔规则），并敦促在得出结论之前考虑基本假设，以避免基于统计上倾斜的解释损害声誉。

---

## 7. Gauntlet AI (YC S17) 正在寻找想要精通人工智能的工程师。

**原文标题**: Gauntlet AI (YC S17) is looking for engineers who want to master AI

**原文链接**: [https://apply.gauntletai.com/](https://apply.gauntletai.com/)

Gauntlet AI (YC S17) 正在积极招聘对掌握人工智能充满热情的工程师。公司旨在打造精英网络，寻求顶尖人才，为雄心勃勃、渴望在人工智能领域有所建树的工程师提供精进技艺的平台。

---

## 8. 如何阻止人工智能的“致命三连击”

**原文标题**: How to stop AI's "lethal trifecta"

**原文链接**: [https://www.economist.com/leaders/2025/09/25/how-to-stop-ais-lethal-trifecta](https://www.economist.com/leaders/2025/09/25/how-to-stop-ais-lethal-trifecta)

无法访问文章链接。

---

## 9. DeepFabric – 大规模生成高质量合成数据集

**原文标题**: DeepFabric – Generate High-Quality Synthetic Datasets at Scale

**原文链接**: [https://lukehinds.github.io/deepfabric/](https://lukehinds.github.io/deepfabric/)

DeepFabric 是一款旨在为语言模型训练、评估和研究生成高质量合成数据集的工具。其核心优势在于其主题驱动的数据生成方法，利用分层主题树和实验性的基于图的主题建模来创建多样且上下文丰富的训练示例。

该工具适用于需要高质量合成数据的研究人员、工程师和从业者，用于模型蒸馏、代理评估或统计研究等任务。它提供了一个三阶段流程：主题生成（创建代表领域的主题树或图）、数据集生成（生成上下文适当的训练示例）和打包成标准格式。

DeepFabric 通过构建领域的概念图脱颖而出，确保比简单的基于提示的生成更广泛的覆盖范围和更一致的质量。它支持具有清晰层次结构的领域的传统主题树，以及用于互连领域的主题图。

入门包括安装、配置和数据集生成。用户可以利用 YAML 配置进行详细控制，或使用 Python API 进行程序化集成。DeepFabric 与 OpenAI、Anthropic、Ollama 和 Hugging Face Hub 等平台集成，允许导出具有自动元数据的数据集。CLI 提供了用于验证、可视化和数据集上传的实用程序。

---

## 10. SpaceX – 发展多用户航天港

**原文标题**: SpaceX – Evolving the Multi-User Spaceport

**原文链接**: [https://www.spacex.com/updates#multiuser-spaceport](https://www.spacex.com/updates#multiuser-spaceport)

文章题为《SpaceX：多用户太空发射场的演进》，可能重点介绍SpaceX将其发射设施转变为多用户太空发射场的努力。这意味着从独家使用转变为其他公司和组织可以利用SpaceX的基础设施进行其自身太空相关活动的模式。

文章可能涵盖的关键方面包括：

*   **增加发射能力：** 通过创建多用户太空发射场，SpaceX可以显著增加整体发射次数，从而推动整个航天工业的发展。
*   **收入多样化：** 向其他公司提供发射服务和基础设施为SpaceX提供了除自身任务之外的额外收入来源。
*   **竞争与合作：** 多用户模式可以促进发射服务提供商之间的竞争，同时也可能促成合作和创新。
*   **基础设施改进：** 为了容纳多个用户，SpaceX可能需要投资升级和扩展其发射设施，包括发射台、有效载荷处理设施和地面支持设备。
*   **监管和安全考量：** 运营多用户太空发射场需要应对复杂的监管要求，并确保所有用户和周围环境的安全。
*   **太空发射场的未来：** 文章可能讨论SpaceX的努力如何塑造太空发射场和更广泛的航天工业的未来。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 2 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 3 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 4 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 5 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 6 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 7 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 8 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 9 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 10 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 11 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 12 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 13 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 14 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 15 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 16 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 17 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 18 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 19 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 20 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 21 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 22 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 23 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 24 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 25 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 26 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 27 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 28 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 29 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 30 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 31 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 32 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 33 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 34 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 35 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 36 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 37 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 38 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 39 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 40 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 41 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 42 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 43 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 44 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 45 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 46 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 47 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 48 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 49 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 50 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 51 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 52 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 53 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 54 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 55 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 56 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 57 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 58 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 59 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 60 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 61 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 62 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 63 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 64 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 65 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 66 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 67 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 68 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 69 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 70 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 71 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 72 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 73 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 74 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 75 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 76 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 77 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 78 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 79 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 80 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 81 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 82 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 83 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 84 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 85 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 86 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 87 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 88 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 89 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 90 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 91 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 92 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 93 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 94 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 95 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 96 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 97 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 98 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 99 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 100 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 101 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 102 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 103 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 104 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 105 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 106 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 107 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 108 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 109 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 110 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 111 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 112 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 113 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 114 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 115 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 116 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 117 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 118 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 119 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 120 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 121 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 122 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 123 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 124 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 125 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 126 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 127 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 128 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 129 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 130 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 131 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 132 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 133 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 134 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 135 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 136 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 137 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 138 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 139 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 140 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 141 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 142 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 143 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 144 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 145 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 146 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 147 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 148 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 149 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 150 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 151 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 152 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 153 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 154 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 155 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 156 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 157 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 158 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 159 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 160 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 161 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 162 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 163 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 164 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 165 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 166 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 167 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 168 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 169 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 170 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 171 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 172 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 173 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 174 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 175 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 176 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 177 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 178 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 179 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 180 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 181 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 182 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 183 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 184 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 185 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 186 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 187 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 188 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 189 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 190 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 191 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
