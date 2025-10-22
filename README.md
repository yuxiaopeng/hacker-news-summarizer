# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-22.md)

*最后自动更新时间: 2025-10-22 17:48:16*
## 1. Willow quantum chip demonstrates verifiable quantum advantage on hardware

**原文标题**: Willow quantum chip demonstrates verifiable quantum advantage on hardware

**原文链接**: [https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/](https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/)

Google Quantum AI's "Willow" quantum chip has achieved a significant breakthrough: demonstrating verifiable quantum advantage on hardware for the first time. Their "Quantum Echoes" algorithm, published in Nature, runs 13,000 times faster than the best classical algorithm on a supercomputer and can be repeatedly verified on similar quantum computers.

The Quantum Echoes algorithm measures out-of-order time correlators (OTOC) and can be used to learn the structure of complex systems, from molecules to black holes. It works by sending a signal into the quantum system, perturbing a qubit, reversing the signal, and listening for the "echo," which is amplified by constructive interference.

The team also demonstrated a "molecular ruler" technique, using Quantum Echoes and Nuclear Magnetic Resonance (NMR) data to measure molecular geometry, gaining more information about chemical structure than traditional methods. This was verified in a proof-of-principle experiment with molecules containing 15 and 28 atoms in partnership with The University of California, Berkeley.

This verifiable quantum advantage is enabled by Willow's low error rates and high-speed operations. The algorithm tests both complexity and precision, crucial for real-world applications. The advances have the potential to enhance NMR technology, leading to a "quantum-scope" for observing previously unobservable natural phenomena, impacting fields like drug discovery and materials science.

The team is now focusing on achieving a long-lived logical qubit, a key milestone in their quantum hardware roadmap.


---

## 2. 推出 Galaxy XR，首款安卓 XR 头显

**原文标题**: Introducing Galaxy XR, the first Android XR headset

**原文链接**: [https://blog.google/products/android/samsung-galaxy-xr/](https://blog.google/products/android/samsung-galaxy-xr/)

三星Galaxy XR是首款基于Android XR的设备，这是一款融合数字与物理体验并集成Gemini AI的新操作系统。它提供了一个无限屏幕，可用于Google Play的应用程序和全新的XR体验，通过语音、手势和眼睛进行控制。主要功能包括通过YouTube和Google TV进行沉浸式电影观看，使用Google Photos将2D照片转换为3D，以及使用Google Maps在3D中探索世界，所有这些都通过Gemini的上下文帮助得到增强。Galaxy XR还提供了一个带有多个应用程序、键盘/鼠标支持以及Gemini组织帮助的广阔工作空间。

该头显利用Gemini提供关于屏幕内容的实时信息，例如篮球比赛期间的球员统计数据，或Google Maps中地标的历史背景。它支持为XR重新设计的Google应用程序，全新的XR体验以及数百万个移动和平板电脑应用程序。

Galaxy XR在美国和韩国的Samsung.com和三星体验店有售，价格为1799美元或每月149美元。限时“探索者套装”提供订阅捆绑包，包括Google AI Pro，YouTube Premium，Google Play Pass，访问流媒体服务试用版，体育通行证以及提前访问Adobe的Project Pulsar和Status Pro的NFL PRO ERA等应用程序。Android XR系统还支持OpenXR，WebXR和Unity等开放标准。预计未来将会有更多基于Android XR的设备和体验。

---

## 3. Cloudflare Circl FourQ 实现中的密码学问题 (CVE-2025-8556)

**原文标题**: Cryptographic Issues in Cloudflare's Circl FourQ Implementation (CVE-2025-8556)

**原文链接**: [https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation](https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation)

This article details CVE-2025-8556, a vulnerability discovered in Cloudflare's CIRCL library, specifically in its implementation of the FourQ elliptic curve. The vulnerability stems from insufficient validation of points used in cryptographic calculations, making the implementation susceptible to invalid point attacks.

The FourQ curve, designed for efficiency in resource-constrained environments, relies on specific characteristics including endomorphisms. The core issue lies in the `Shared` function of `Curve4Q` (a Diffie-Hellman implementation), where a public point isn't validated for curve membership before scalar multiplication with a secret key. This allows attackers to supply invalid points, potentially belonging to curves with small subgroup orders, which drastically reduces the difficulty of recovering the server's secret key via brute-force methods and the Chinese Remainder Theorem.

While traditional invalid curve attacks on Weierstrass curves don't directly translate to Edwards curves like FourQ, a specific attack vector exploiting points of the form (0, y) was identified. This allows manipulation of the scalar multiplication to reveal the secret key.

The reported issues include: incorrect point validation during unmarshalling (missing conjugate validation), a faulty point comparison in `pointR1.isEqual` that returns true when Z = 0, lack of point validation after cofactor clearing in `pointR1.ClearCofactor`, and the absence of pre-validation in `pointR1.ScalarMult`, which is vulnerable to degenerate curve attacks. Cloudflare addressed the major points raised.


---

## 4. Linux Capabilities Revisited

**原文标题**: Linux Capabilities Revisited

**原文链接**: [https://dfir.ch/posts/linux_capabilities/](https://dfir.ch/posts/linux_capabilities/)

生成摘要时出错

---

## 5. MinIO停止分发免费Docker镜像

**原文标题**: MinIO stops distributing free Docker images

**原文链接**: [https://github.com/minio/minio/issues/21647#issuecomment-3418675115](https://github.com/minio/minio/issues/21647#issuecomment-3418675115)

本次问题报告指出，Quay.io和DockerHub上均缺少最近MinIO安全版本(Security/CVE RELEASE.2025-10-15T17-29-55Z)的新的Docker镜像。报告人neil-lcv-cs询问这是否是有意的，如果不是，则请求发布新的Docker镜像。该问题被标记为“社区”和“按预期工作”，表明MinIO可能有意停止为该安全版本提供免费Docker镜像，或者由于其他原因该版本未通过Docker分发。报告人和至少22人对最初的报告表示赞同。

---

## 6. 为易腐物品设计软件

**原文标题**: Designing software for things that rot

**原文链接**: [https://drobinin.com/posts/designing-software-for-things-that-rot/](https://drobinin.com/posts/designing-software-for-things-that-rot/)

软件设计与发酵的交汇：一个软件工具“Fermento”的开发历程

---

## 7. Bild AI (YC W25) 正在招聘创始 AI 工程师

**原文标题**: Bild AI (YC W25) Is Hiring a Founding AI Engineer

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai](https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai)

Bild AI（YC W25）是一家专注于将人工智能应用于建筑蓝图的初创公司，正在旧金山招聘创始AI工程师。该职位提供10万至18万美元的薪资，以及0.50%至2.00%的股权。Bild AI旨在简化蓝图阅读、成本估算和许可证申请流程，从而更高效地建造房屋、医院和学校。

理想的候选人将专注于智能层，应用最新的计算机视觉、大型语言模型和人工智能系统，根据用户反馈快速进行原型设计和迭代。期望的资质包括应用计算机视觉/机器学习经验、从零开始构建和部署人工智能解决方案的经验、成长型思维、强大的沟通能力，以及愿意处理创业生活中不太光鲜的一面。有成功产品的早期创业/创始人经验、建筑背景以及以影响力为导向的动机者将获得加分。

申请人应说明他们为何适合该职位，并分享他们最喜欢的水果。该职位要求全职在旧金山办公室工作，或愿意搬迁。Bild AI成立于2024年，是YC W25的一部分，采用模型花园方法来解决蓝图理解中的复杂技术挑战，并已获得顶级风险投资的支持。创始人是Roop Pal和Puneet Sukhija。

---

## 8. AI助手45%的时间内错误呈现新闻内容

**原文标题**: AI assistants misrepresent news content 45% of the time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content](https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content)

EBU与BBC联合研究揭示AI助手常曲解新闻内容

---

## 9. Meta 裁减其人工智能部门 600 个职位

**原文标题**: Meta is axing 600 roles across its AI division

**原文链接**: [https://www.theverge.com/news/804253/meta-ai-research-layoffs-fair-superintelligence](https://www.theverge.com/news/804253/meta-ai-research-layoffs-fair-superintelligence)

Meta裁减人工智能部门600个职位，涉及基础人工智能研究(FAIR)部门、人工智能产品和基础设施部门。尽管公司仍在为其新成立的超智能团队TBD Lab招聘，但仍采取了这一举措。Meta发言人证实了裁员，此前公司曾对人工智能进行大量投资和招聘，包括聘请Scale AI首席执行官Alexandr Wang。此次重组标志着公司将重点转向与人工智能相关的产品和基础设施，而FAIR则退居次要地位。Meta人工智能负责人Wang表示，公司旨在将FAIR的研究成果整合到TBD Lab中。裁员旨在通过创建一个更小、更具影响力的团队来简化决策流程。受影响的员工将有机会申请Meta内部的其他职位。

---

## 10. 本地LLM的安全悖论

**原文标题**: The security paradox of local LLMs

**原文链接**: [https://quesma.com/blog/local-llms-security-paradox/](https://quesma.com/blog/local-llms-security-paradox/)

Jacek Migdal 的文章强调了使用本地 LLM 保护隐私的一个安全悖论。 虽然本意是更安全，但对 gpt-oss-20b 的研究表明，它们比大型前沿模型更容易受到恶意提示的攻击。 这是因为它们识别恶意意图的能力较弱。

该文章详细介绍了两种攻击：第一种是“彩蛋”后门，通过将其伪装成无害的功能来植入成功率高达 95% 的隐藏 RCE 后门。 第二种是通过认知过载实现的即时 RCE，诱骗模型在代码生成期间执行恶意代码。 这种攻击虽然成功率较低 (43.5%)，但由于其即时性而十分危险。

这些攻击通过将恶意提示注入 AI 助手的上下文中来实现，途径包括文档污染、受损的 MCP 服务器或社会工程。 该文章强调，由于本地模型推理能力较弱、对齐效果较差且安全训练有限，因此会加剧这种情况。 前沿模型虽然可能更安全，但由于提供商的限制，难以进行测试。

文章最后提倡一种新的防御方式，包括对生成的代码进行静态分析、沙盒化初始执行、监控输入、输出和网络流量，以及使用较小、更简单的模型进行“二次审查”以检查政策违规情况。 关键在于，所有 AI 生成的代码都应持怀疑态度，认识到本地 LLM 虽然具有隐私优势，但也需要强大的安全措施。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 2 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 3 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 4 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 5 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 6 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 7 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 8 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 9 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 10 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 11 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 12 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 13 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 14 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 15 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 16 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 17 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 18 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 19 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 20 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 21 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 22 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 23 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 24 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 25 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 26 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 27 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 28 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 29 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 30 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 31 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 32 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 33 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 34 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 35 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 36 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 37 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 38 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 39 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 40 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 41 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 42 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 43 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 44 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 45 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 46 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 47 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 48 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 49 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 50 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 51 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 52 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 53 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 54 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 55 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 56 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 57 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 58 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 59 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 60 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 61 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 62 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 63 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 64 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 65 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 66 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 67 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 68 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 69 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 70 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 71 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 72 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 73 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 74 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 75 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 76 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 77 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 78 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 79 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 80 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 81 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 82 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 83 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 84 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 85 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 86 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 87 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 88 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 89 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 90 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 91 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 92 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 93 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 94 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 95 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 96 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 97 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 98 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 99 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 100 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 101 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 102 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 103 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 104 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 105 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 106 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 107 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 108 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 109 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 110 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 111 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 112 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 113 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 114 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 115 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 116 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 117 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 118 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 119 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 120 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 121 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 122 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 123 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 124 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 125 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 126 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 127 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 128 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 129 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 130 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 131 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 132 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 133 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 134 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 135 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 136 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 137 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 138 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 139 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 140 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 141 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 142 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 143 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 144 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 145 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 146 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 147 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 148 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 149 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 150 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 151 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 152 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 153 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 154 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 155 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 156 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 157 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 158 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 159 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 160 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 161 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 162 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 163 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 164 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 165 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 166 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 167 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 168 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 169 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 170 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 171 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 172 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 173 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 174 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 175 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 176 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 177 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 178 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 179 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 180 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 181 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 182 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 183 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 184 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 185 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 186 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 187 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 188 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 189 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 190 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 191 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 192 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 193 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 194 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 195 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 196 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 197 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 198 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 199 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 200 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 201 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 202 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 203 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 204 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 205 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 206 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 207 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 208 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 209 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 210 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 211 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 212 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 213 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 214 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 215 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 216 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 217 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
