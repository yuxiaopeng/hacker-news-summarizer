# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-15.md)

*最后自动更新时间: 2026-09-15 20:34:01*
## 1. Show HN：一款能识别鸟鸣并将其绘制成19世纪风格插画的电子墨水屏相框

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

**Fugleramme** 是由 Arne Giacomo 发起的一项开源项目，它能将实时的鸟鸣声转化为一组不断更新的复古自然历史插画。该系统基于树莓派（Raspberry Pi）构建，利用麦克风和本地人工智能（AI）通过声音识别鸟类，并将结果显示在 Inky Impression 电子墨水屏或基于网页的展示终端上。

该项目的突出特色在于其审美风格：它没有使用照片或 AI 生成的艺术作品，而是利用了一个包含 800 多张 19 世纪公有领域插画的精选库。这 400 多种鸟类均经过抠图处理，并动态排列在带有纹理的数字“页面”上，鸟类的大小根据其真实体重比例缩放。虽然目前覆盖范围主要集中在斯堪的纳维亚半岛、英国和中欧，但针对北美和欧洲其他地区的扩展工作已在进行中。

在技术层面，Fugleramme 通过轮询 **BirdNET-Go** API（一种本地音频分类器）来运行。它旨在保护隐私，并在设置完成后完全支持离线运行。该软件极具灵活性，可以在 Docker 容器中运行，通过专用安装脚本安装，或者为没有电子墨水硬件的用户提供纯网页显示。

该项目目前处于早期开发阶段，欢迎社区贡献，特别是从历史图册中“手动抠取”新的鸟类插画。对于偏好即插即用体验的用户，创作者还提供预装好的框架成品。通过将现代机器学习与 19 世纪的科学艺术相结合，Fugleramme 成为了一张独特的“实时海报”，将室内空间与当地的生物多样性紧密连接在一起。

---

## 2. Jev：新型前沿模型，成本降低 40-400 倍，速度提升 20-200 倍

**原文标题**: Jev: New frontier model 40-400x cheaper and 20-200x faster

**原文链接**: [https://typesafe.ai/blog/introducing-system-one-models-and-jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

由前 OpenAI 研究员 Diogo Almeida 领导的 TypeSafe AI 发布了 **Jev**。这是首个被称为“系统 1”（System One）的新型前沿模型，专门为高速、结构化自动化而设计。与侧重于对话和顺序文本生成的传统大语言模型（LLM）不同，Jev 针对软件可直接调用的“智能 if 语句”决策进行了优化。

**核心技术创新：**
Jev 彻底改变了标准的 LLM 技术栈，采用了全新的架构、并行采样器以及一种名为**针对校准决策的强化学习（RLCD）**的训练方法。Jev 不再逐个生成 Token，而是在单次硬件感知查询中处理所有输出。

**性能与成本：**
与 GPT-5/6 等当前前沿模型相比，该模型在效率上实现了巨大飞跃：
*   **速度：** 快 20–200 倍，端到端响应时间在 70ms 到 500ms 之间。
*   **成本：** 便宜 40–400 倍，输入价格极低（0.042 美元/百万 Token），输出 Token 则“便宜到无需计费”。
*   **可靠性：** Jev 通过输出结构化数据而非字符串，消除了幻觉和类型错误。每一次决策都包含经过校准的概率评分，允许开发者设置精确的置信度阈值。

**应用场景：**
Jev 旨在用于对延迟和可靠性要求极高的实时应用及复杂工作流。演示案例包括一个根据游戏状态实时玩《毁灭战士》（Doom）的 AI 智能体，以及一个“维基百科竞速”机器人。通过专注于“系统 1”（快速、直觉性）任务，TypeSafe 旨在大幅降低智能成本，从而引发“杰文斯悖论”效应——即效率的提升将推动 AI 在整个经济领域集成规模的爆发式增长。

Jev 目前已向开发者开放早期访问候补名单。

---

## 3. Wayback Machine 访问情况更新

**原文标题**: An Update on Wayback Machine Access

**原文链接**: [https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/)

互联网档案馆（Internet Archive）已解决近期因大规模自动化流量激增导致的 Wayback Machine 访问问题。为了维持服务稳定性，该档案馆实施了安全防护措施，在检测到可疑流量时会触发 HTTP 429 错误（“请求过多”）。

虽然这些措施旨在拦截恶意机器人，但档案馆承认部分合法用户被误拦截。他们目前正致力于优化检测系统，以更好地区分人类用户与自动化程序。

如果您认为自己被错误拦截，请将您的操作系统、浏览器及 IP 地址发送至 **info@archive.org**，以便档案馆调查该问题。

---

## 4. We got admin access to Baseten's production GitHub in 25 minutes

**原文标题**: We got admin access to Baseten's production GitHub in 25 minutes

**原文链接**: [https://www.strix.ai/blog/baseten-harbor-github-pat-takeover](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover)

The article details how **Strix**, an autonomous security agent, gained administrative access to Baseten’s production GitHub environment in just 25 minutes during a routine vendor security assessment.

The breach followed a standard reconnaissance path:
1.  **Discovery:** Strix identified an exposed Harbor registry on a Baseten subdomain that allowed anonymous users to list and pull container images.
2.  **Exploitation:** Upon pulling the `baseten-app` image, Strix inspected the Docker build history. It discovered a live GitHub Personal Access Token (PAT) belonging to "basetenbot" embedded in the `history[].created_by` metadata.
3.  **Impact:** The leak occurred because a developer used the `ARG` instruction to pass the token during the build process, which Docker records permanently in the image config. Despite the image being from 2023, the token was still active in 2026. It granted **admin and push access** to Baseten’s core product source code, GitOps repositories (infrastructure control), and private customer directories.

**Response and Remediation:**
Baseten’s security team responded professionally, securing the registry and rotating the compromised token within 24 hours of the report. 

**Key Takeaways:**
*   **Secret Management:** Never use `ARG` or environment variables for secrets in Dockerfiles. Instead, use **BuildKit secret mounts**, which ensure credentials do not persist in the image layers or metadata.
*   **Legacy Data:** Old container images are often overlooked but can contain valid, high-privilege credentials.
*   **Principle of Least Privilege:** Tokens should be scoped to the minimum permissions required; a build bot rarely needs administrative rights over production infrastructure.
*   **AI in Security:** The authors argue that as AI-powered attacks become faster, companies must use similar autonomous tools to identify and fix "human knowledge" gaps in their attack surface.

---

## 5. Gemini 3.8 Live and 3.8 Live Extended Thinking

**原文标题**: Gemini 3.8 Live and 3.8 Live Extended Thinking

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)

生成摘要时出错

---

## 6. Show HN: Capsule – Single-file web apps that save their data into SQLite

**原文标题**: Show HN: Capsule – Single-file web apps that save their data into SQLite

**原文链接**: [https://withcapsule.app/](https://withcapsule.app/)

生成摘要时出错

---

## 7. GEFS on OpenBSD: A Early Preview

**原文标题**: GEFS on OpenBSD: A Early Preview

**原文链接**: [https://marc.info/?l=openbsd-tech&m=178948744271633&w=2](https://marc.info/?l=openbsd-tech&m=178948744271633&w=2)

生成摘要时出错

---

## 8. Chop Up Your Books

**原文标题**: Chop Up Your Books

**原文链接**: [https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html](https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html)

生成摘要时出错

---

## 9. I can't stop thinking about Papua New Guinea

**原文标题**: I can't stop thinking about Papua New Guinea

**原文链接**: [https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua](https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua)

生成摘要时出错

---

## 10. Show HN: Hacking a $20 4G wireless hotspot into a texting device

**原文标题**: Show HN: Hacking a $20 4G wireless hotspot into a texting device

**原文链接**: [https://bkovac.github.io/modem-thing/](https://bkovac.github.io/modem-thing/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 2 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 3 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 4 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 5 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 6 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 7 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 8 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 9 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 10 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 11 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 12 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 13 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 14 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 15 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 16 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 17 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 18 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 19 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 20 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 21 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 22 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 23 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 24 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 25 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 26 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 27 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 28 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 29 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 30 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 31 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 32 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 33 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 34 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 35 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 36 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 37 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 38 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 39 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 40 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 41 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 42 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 43 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 44 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 45 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 46 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 47 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 48 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 49 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 50 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 51 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 52 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 53 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 54 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 55 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 56 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 57 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 58 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 59 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 60 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 61 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 62 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 63 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 64 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 65 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 66 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 67 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 68 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 69 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 70 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 71 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 72 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 73 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 74 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 75 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 76 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 77 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 78 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 79 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 80 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 81 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 82 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 83 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 84 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 85 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 86 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 87 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 88 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 89 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 90 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 91 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 92 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 93 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 94 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 95 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 96 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 97 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 98 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 99 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 100 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 101 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 102 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 103 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 104 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 105 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 106 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 107 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 108 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 109 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 110 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 111 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 112 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 113 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 114 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 115 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 116 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 117 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 118 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 119 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 120 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 121 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 122 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 123 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 124 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 125 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 126 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 127 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 128 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 129 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 130 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 131 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 132 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 133 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 134 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 135 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 136 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 137 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 138 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 139 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 140 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 141 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 142 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 143 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 144 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 145 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 146 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 147 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 148 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 149 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 150 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 151 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 152 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 153 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 154 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 155 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 156 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 157 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 158 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 159 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 160 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 161 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 162 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 163 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 164 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 165 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 166 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 167 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 168 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 169 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 170 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 171 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 172 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 173 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 174 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 175 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 176 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 177 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 178 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 179 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 180 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 181 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 182 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 183 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 184 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 185 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 186 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 187 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 188 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 189 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 190 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 191 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 192 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 193 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 194 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 195 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 196 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 197 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 198 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 199 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 200 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 201 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 202 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 203 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 204 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 205 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 206 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 207 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 208 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 209 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 210 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 211 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 212 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 213 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 214 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 215 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 216 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 217 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 218 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 219 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 220 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 221 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 222 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 223 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 224 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 225 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 226 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 227 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 228 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 229 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 230 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 231 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 232 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 233 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 234 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 235 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 236 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 237 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 238 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 239 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 240 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 241 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 242 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 243 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 244 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 245 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 246 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 247 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 248 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 249 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 250 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 251 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 252 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 253 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 254 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 255 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 256 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 257 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 258 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 259 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 260 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 261 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 262 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 263 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 264 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 265 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 266 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 267 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 268 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 269 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 270 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 271 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 272 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 273 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 274 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 275 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 276 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 277 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 278 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 279 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 280 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 281 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 282 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 283 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 284 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 285 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 286 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 287 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 288 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 289 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 290 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 291 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 292 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 293 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 294 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 295 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 296 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 297 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 298 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 299 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 300 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 301 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 302 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 303 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 304 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 305 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 306 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 307 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 308 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 309 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 310 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 311 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 312 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 313 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 314 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 315 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 316 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 317 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 318 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 319 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 320 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 321 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 322 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 323 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 324 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 325 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 326 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 327 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 328 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 329 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 330 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 331 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 332 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 333 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 334 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 335 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 336 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 337 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 338 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 339 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 340 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 341 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 342 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 343 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 344 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 345 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 346 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 347 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 348 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 349 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 350 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 351 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 352 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 353 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 354 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 355 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 356 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 357 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 358 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 359 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 360 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 361 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 362 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 363 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 364 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 365 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 366 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 367 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 368 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 369 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 370 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 371 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 372 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 373 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 374 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 375 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 376 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 377 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 378 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 379 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 380 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 381 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 382 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 383 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 384 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 385 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 386 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 387 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 388 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 389 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 390 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 391 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 392 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 393 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 394 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 395 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 396 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 397 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 398 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 399 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 400 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 401 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 402 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 403 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 404 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 405 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 406 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 407 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 408 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 409 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 410 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 411 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 412 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 413 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 414 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 415 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 416 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 417 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 418 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 419 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 420 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 421 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 422 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 423 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 424 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 425 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 426 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 427 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 428 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 429 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 430 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 431 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 432 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 433 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 434 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 435 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 436 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 437 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 438 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 439 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 440 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 441 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 442 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 443 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 444 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 445 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 446 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 447 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 448 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 449 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 450 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 451 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 452 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 453 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 454 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 455 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 456 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 457 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 458 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 459 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 460 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 461 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 462 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 463 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 464 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 465 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 466 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 467 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 468 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 469 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 470 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 471 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 472 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 473 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 474 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 475 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 476 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 477 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 478 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 479 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 480 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 481 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 482 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 483 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 484 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 485 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 486 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 487 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 488 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 489 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 490 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 491 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 492 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 493 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 494 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 495 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 496 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 497 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 498 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 499 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 500 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 501 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 502 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 503 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 504 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 505 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 506 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 507 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 508 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 509 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 510 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 511 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 512 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 513 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 514 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 515 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 516 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 517 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 518 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 519 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 520 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 521 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 522 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 523 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 524 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 525 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 526 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 527 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 528 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 529 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 530 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 531 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 532 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 533 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 534 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 535 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 536 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 537 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 538 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 539 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 540 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 541 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 542 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
