# Hacker News 热门文章摘要 (2026-09-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. How much oil-market buffer is left?

**原文标题**: How much oil-market buffer is left?

**原文链接**: [https://www.depletion.org](https://www.depletion.org)

生成摘要时出错

---

## 12. Jiga (YC W21) Is Hiring Product Engineer (Remote/US)

**原文标题**: Jiga (YC W21) Is Hiring Product Engineer (Remote/US)

**原文链接**: [https://jiga.io/about-us/?ashby_jid=0b75d72d-c92b-4dca-8062-09d298ada0bd](https://jiga.io/about-us/?ashby_jid=0b75d72d-c92b-4dca-8062-09d298ada0bd)

生成摘要时出错

---

## 13. WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages

**原文标题**: WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages

**原文链接**: [https://github.com/GraafHenk/numberwang](https://github.com/GraafHenk/numberwang)

生成摘要时出错

---

## 14. Let's make quality the norm again

**原文标题**: Let's make quality the norm again

**原文链接**: [https://www.forbrukerradet.no/short-life/](https://www.forbrukerradet.no/short-life/)

生成摘要时出错

---

## 15. The CSS Zen Garden dream, finally shipped

**原文标题**: The CSS Zen Garden dream, finally shipped

**原文链接**: [https://josprague.com/blog/the-css-zen-garden-dream-finally-shipped/](https://josprague.com/blog/the-css-zen-garden-dream-finally-shipped/)

生成摘要时出错

---

## 16. Photographs of Atlantic City Sand Sculpture (ca. 1880–1920)

**原文标题**: Photographs of Atlantic City Sand Sculpture (ca. 1880–1920)

**原文链接**: [https://publicdomainreview.org/collection/atlantic-city-sand-sculpture/](https://publicdomainreview.org/collection/atlantic-city-sand-sculpture/)

生成摘要时出错

---

## 17. Giving up on smart rings

**原文标题**: Giving up on smart rings

**原文链接**: [https://notesbylex.com/giving-up-on-smart-rings](https://notesbylex.com/giving-up-on-smart-rings)

生成摘要时出错

---

## 18. The Inference Hardware Revolution of 2026

**原文标题**: The Inference Hardware Revolution of 2026

**原文链接**: [https://spectrum.ieee.org/inference-hardware-revolution](https://spectrum.ieee.org/inference-hardware-revolution)

生成摘要时出错

---

## 19. A single firm is behind OpenAI, Anthropic, and Meta hacking scandals

**原文标题**: A single firm is behind OpenAI, Anthropic, and Meta hacking scandals

**原文链接**: [https://www.effort.news/irregular](https://www.effort.news/irregular)

生成摘要时出错

---

## 20. Paul A. M. Dirac, Interview by Friedrich Hund (1982) [video]

**原文标题**: Paul A. M. Dirac, Interview by Friedrich Hund (1982) [video]

**原文链接**: [https://www.youtube.com/watch?v=xJzrU38pGWc](https://www.youtube.com/watch?v=xJzrU38pGWc)

生成摘要时出错

---

## 21. Archiving pirate radio station Kool FM

**原文标题**: Archiving pirate radio station Kool FM

**原文链接**: [https://londonist.com/london/music/kool-fm-archives](https://londonist.com/london/music/kool-fm-archives)

生成摘要时出错

---

## 22. America's Driver's License Breach Is a National Security Disaster

**原文标题**: America's Driver's License Breach Is a National Security Disaster

**原文链接**: [https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster](https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster)

生成摘要时出错

---

## 23. US confirms for first time it has deployed space weapons

**原文标题**: US confirms for first time it has deployed space weapons

**原文链接**: [https://www.bbc.com/news/articles/ck790xg41ygro](https://www.bbc.com/news/articles/ck790xg41ygro)

生成摘要时出错

---

## 24. Most people prefer traditional architecture

**原文标题**: Most people prefer traditional architecture

**原文链接**: [https://www.worksinprogress.news/p/do-people-prefer-traditional-architecture](https://www.worksinprogress.news/p/do-people-prefer-traditional-architecture)

生成摘要时出错

---

## 25. Cartesian – AI 3D Modeling for Design

**原文标题**: Cartesian – AI 3D Modeling for Design

**原文链接**: [https://www.formas.ai/cartesian](https://www.formas.ai/cartesian)

生成摘要时出错

---

## 26. CSS-Tricks in Limbo

**原文标题**: CSS-Tricks in Limbo

**原文链接**: [https://vale.rocks/micros/20260915-0135](https://vale.rocks/micros/20260915-0135)

生成摘要时出错

---

## 27. Rat and Mouse Gazette: Nursing Care (1996)

**原文标题**: Rat and Mouse Gazette: Nursing Care (1996)

**原文链接**: [https://www.rmca.org/Articles/nurse.htm](https://www.rmca.org/Articles/nurse.htm)

生成摘要时出错

---

## 28. 25 years of mass surveillance is enough

**原文标题**: 25 years of mass surveillance is enough

**原文链接**: [https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html)

生成摘要时出错

---

## 29. Alternatives to MinIO for single-node local S3

**原文标题**: Alternatives to MinIO for single-node local S3

**原文链接**: [https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/](https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/)

生成摘要时出错

---

## 30. Hugging Face is billing OpenAI $100M for hacking it

**原文标题**: Hugging Face is billing OpenAI $100M for hacking it

**原文链接**: [https://thenextweb.com/news/hugging-face-delangue-openai-100m-compute-traces-demand](https://thenextweb.com/news/hugging-face-delangue-openai-100m-compute-traces-demand)

生成摘要时出错

---

## 31. Sony's First Computer – The SMC-70 from 1982 [video]

**原文标题**: Sony's First Computer – The SMC-70 from 1982 [video]

**原文链接**: [https://www.youtube.com/watch?v=cT2-7KkPkBc](https://www.youtube.com/watch?v=cT2-7KkPkBc)

生成摘要时出错

---

## 32. A rough guide for going back to the Moon

**原文标题**: A rough guide for going back to the Moon

**原文链接**: [https://research.ibm.com/blog/nasa-ibm-lunar-foundation-model](https://research.ibm.com/blog/nasa-ibm-lunar-foundation-model)

生成摘要时出错

---

## 33. Google copied our open-source code, removed engineers' names without credit

**原文标题**: Google copied our open-source code, removed engineers' names without credit

**原文链接**: [https://www.reddit.com/r/reinforcementlearning/comments/1wg1unx/google_copied_our_opensource_code_removed_our/](https://www.reddit.com/r/reinforcementlearning/comments/1wg1unx/google_copied_our_opensource_code_removed_our/)

生成摘要时出错

---

## 34. Show HN: Panel – A research workspace where the agent can build its own panes

**原文标题**: Show HN: Panel – A research workspace where the agent can build its own panes

**原文链接**: [https://github.com/greentfrapp/panel](https://github.com/greentfrapp/panel)

生成摘要时出错

---

## 35. How much of F-Droid is LLM generated?

**原文标题**: How much of F-Droid is LLM generated?

**原文链接**: [https://tintotint.eu/whacky-corner/f-droid_slop/](https://tintotint.eu/whacky-corner/f-droid_slop/)

生成摘要时出错

---

## 36. OpenArm: An open-source 7DOF humanoid arm

**原文标题**: OpenArm: An open-source 7DOF humanoid arm

**原文链接**: [https://github.com/enactic/OpenArm](https://github.com/enactic/OpenArm)

生成摘要时出错

---

## 37. Show HN: Ordewell – turn one goal into an ordered plan of coding-agent tasks

**原文标题**: Show HN: Ordewell – turn one goal into an ordered plan of coding-agent tasks

**原文链接**: [https://github.com/ordewell/ordewell](https://github.com/ordewell/ordewell)

生成摘要时出错

---

## 38. What we have learned at OpenShell applying formal methods to control AI agents

**原文标题**: What we have learned at OpenShell applying formal methods to control AI agents

**原文链接**: [https://nvidia.github.io/OpenShell-Research/dev-notes/posts/2026-09-10-learning-formal-methods-agent-policy-prover/](https://nvidia.github.io/OpenShell-Research/dev-notes/posts/2026-09-10-learning-formal-methods-agent-policy-prover/)

生成摘要时出错

---

## 39. Fixing an NZXT Signal 4K30 part 2: the green/pink video bug

**原文标题**: Fixing an NZXT Signal 4K30 part 2: the green/pink video bug

**原文链接**: [https://www.downtowndougbrown.com/2026/09/fixing-an-nzxt-signal-4k30-part-2-the-green-pink-video-bug/](https://www.downtowndougbrown.com/2026/09/fixing-an-nzxt-signal-4k30-part-2-the-green-pink-video-bug/)

生成摘要时出错

---

## 40. Inverse-Square Law

**原文标题**: Inverse-Square Law

**原文链接**: [https://blog.coredump.cx/p/inverse-square-law](https://blog.coredump.cx/p/inverse-square-law)

生成摘要时出错

---

## 41. Over 12% of links posted to Hacker News are Show HN projects now

**原文标题**: Over 12% of links posted to Hacker News are Show HN projects now

**原文链接**: [https://www.orangecrumbs.com/stories/show-hn](https://www.orangecrumbs.com/stories/show-hn)

生成摘要时出错

---

## 42. Show HN: Check if your IP has appeared in a residential proxy network

**原文标题**: Show HN: Check if your IP has appeared in a residential proxy network

**原文链接**: [https://haveibeenproxied.com/](https://haveibeenproxied.com/)

生成摘要时出错

---

## 43. The k-server conjecture is true

**原文标题**: The k-server conjecture is true

**原文链接**: [https://arxiv.org/abs/2609.15979](https://arxiv.org/abs/2609.15979)

生成摘要时出错

---

## 44. Suspected sabotage causes major Netherlands rail disruption

**原文标题**: Suspected sabotage causes major Netherlands rail disruption

**原文链接**: [https://www.bbc.com/news/articles/c8ly49w9g1edo](https://www.bbc.com/news/articles/c8ly49w9g1edo)

生成摘要时出错

---

## 45. GRP-Obliteration: Unaligning LLMs with a Single Unlabeled Prompt

**原文标题**: GRP-Obliteration: Unaligning LLMs with a Single Unlabeled Prompt

**原文链接**: [https://arxiv.org/abs/2602.06258](https://arxiv.org/abs/2602.06258)

生成摘要时出错

---

## 46. TSMC revealing details about next gen A14 node

**原文标题**: TSMC revealing details about next gen A14 node

**原文链接**: [https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331](https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331)

生成摘要时出错

---

## 47. OrangePi Zero 3W Review: Tiny yet Powerful

**原文标题**: OrangePi Zero 3W Review: Tiny yet Powerful

**原文链接**: [https://boilingsteam.com/orange-pi-zero-3w-review-tiny-yet-powerful/](https://boilingsteam.com/orange-pi-zero-3w-review-tiny-yet-powerful/)

生成摘要时出错

---

## 48. California attempts to crack down on health spending

**原文标题**: California attempts to crack down on health spending

**原文链接**: [https://www.axios.com/2026/09/14/california-health-spending-limits-affordability](https://www.axios.com/2026/09/14/california-health-spending-limits-affordability)

生成摘要时出错

---

## 49. Closing the IPv6 first-packet gap with GRAND

**原文标题**: Closing the IPv6 first-packet gap with GRAND

**原文链接**: [https://labs.ripe.net/author/pouria/closing-the-ipv6-first-packet-gap-with-grand/](https://labs.ripe.net/author/pouria/closing-the-ipv6-first-packet-gap-with-grand/)

生成摘要时出错

---

## 50. Linux from Scratch

**原文标题**: Linux from Scratch

**原文链接**: [https://www.linuxfromscratch.org/](https://www.linuxfromscratch.org/)

生成摘要时出错

---

## 51. Java 27

**原文标题**: Java 27

**原文链接**: [https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/](https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/)

生成摘要时出错

---

## 52. Microsoft's latest update breaks domain trust, causing widespread login failures

**原文标题**: Microsoft's latest update breaks domain trust, causing widespread login failures

**原文链接**: [https://www.neowin.net/news/kb5129195-fails-to-fix-secure-domain-logins-broken-by-windows-11-kb5124008/](https://www.neowin.net/news/kb5129195-fails-to-fix-secure-domain-logins-broken-by-windows-11-kb5124008/)

生成摘要时出错

---

## 53. 25 Years of Mass Surveillance Is Enough [Auth: Cindy Cohn; Bruce Schneier]

**原文标题**: 25 Years of Mass Surveillance Is Enough [Auth: Cindy Cohn; Bruce Schneier]

**原文链接**: [https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough](https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough)

生成摘要时出错

---

## 54. Dystopian Surveillance Is Becoming a Reality

**原文标题**: Dystopian Surveillance Is Becoming a Reality

**原文链接**: [https://dallincrump.com/dystopian-surveillance-is-becoming-a-reality](https://dallincrump.com/dystopian-surveillance-is-becoming-a-reality)

生成摘要时出错

---

## 55. OpenAI buys smartphone camera maker Glass Imaging for $300M

**原文标题**: OpenAI buys smartphone camera maker Glass Imaging for $300M

**原文链接**: [https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)

生成摘要时出错

---

## 56. Ubuntu 26.10 completes transition to Rust-based coreutils

**原文标题**: Ubuntu 26.10 completes transition to Rust-based coreutils

**原文链接**: [https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete](https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete)

生成摘要时出错

---

## 57. Show HN: Redis City – Explore how Redis works in an interactive 3D model

**原文标题**: Show HN: Redis City – Explore how Redis works in an interactive 3D model

**原文链接**: [https://poltora.dev/redis](https://poltora.dev/redis)

生成摘要时出错

---

## 58. Show HN: SCIP MIP solver bindings for Go, ported from russcip

**原文标题**: Show HN: SCIP MIP solver bindings for Go, ported from russcip

**原文链接**: [https://github.com/egoisutolabs/scipgo](https://github.com/egoisutolabs/scipgo)

生成摘要时出错

---

## 59. There are only twelve 4x4 sudokus (and a cool trick for finding minimal subsets)

**原文标题**: There are only twelve 4x4 sudokus (and a cool trick for finding minimal subsets)

**原文链接**: [https://baldino.dev/blog/there-are-only-twelve-4x4-sudokus/](https://baldino.dev/blog/there-are-only-twelve-4x4-sudokus/)

生成摘要时出错

---

## 60. Show HN: Loss. a tiny satire about AI progress

**原文标题**: Show HN: Loss. a tiny satire about AI progress

**原文链接**: [https://workatloss.com/](https://workatloss.com/)

生成摘要时出错

---

## 61. Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)

**原文标题**: Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)

**原文链接**: [https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/](https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/)

生成摘要时出错

---

## 62. Charges Against Man Who Destroyed 3D-Printed 'Decoy' Flock Camera Reduced

**原文标题**: Charges Against Man Who Destroyed 3D-Printed 'Decoy' Flock Camera Reduced

**原文链接**: [https://www.404media.co/charges-against-man-who-destroyed-3d-printed-decoy-flock-camera-drastically-reduced-after-state-admits-it-was-not-very-valuable/](https://www.404media.co/charges-against-man-who-destroyed-3d-printed-decoy-flock-camera-drastically-reduced-after-state-admits-it-was-not-very-valuable/)

生成摘要时出错

---

## 63. iOS 27, iPadOS 27, and macOS 27

**原文标题**: iOS 27, iPadOS 27, and macOS 27

**原文链接**: [https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/](https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/)

生成摘要时出错

---

## 64. Israeli Minister Threatens Filmmakers' Citizenship over Gaza Documentary

**原文标题**: Israeli Minister Threatens Filmmakers' Citizenship over Gaza Documentary

**原文链接**: [https://www.reutersconnect.com/item/israeli-minister-threatens-filmmakers-citizenship-over-gaza-documentary/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XQ1ZNQzQ0NjcxMC1WSURFTw](https://www.reutersconnect.com/item/israeli-minister-threatens-filmmakers-citizenship-over-gaza-documentary/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XQ1ZNQzQ0NjcxMC1WSURFTw)

生成摘要时出错

---

## 65. Periodic Labs, building labs that learn

**原文标题**: Periodic Labs, building labs that learn

**原文链接**: [https://periodic.com/news/building-labs-that-learn](https://periodic.com/news/building-labs-that-learn)

生成摘要时出错

---

## 66. People who can't picture anything are rewriting the science of imagination

**原文标题**: People who can't picture anything are rewriting the science of imagination

**原文链接**: [https://dailyneuron.com/aphantasia-mental-imagery-brain-network/](https://dailyneuron.com/aphantasia-mental-imagery-brain-network/)

生成摘要时出错

---

## 67. Forgotten Woodlands

**原文标题**: Forgotten Woodlands

**原文链接**: [https://storymaps.arcgis.com/stories/9b790daf22ba4e87836f467abb1c7e49](https://storymaps.arcgis.com/stories/9b790daf22ba4e87836f467abb1c7e49)

生成摘要时出错

---

## 68. There's a 100% Chance AI Agents Are Ruining the Internet

**原文标题**: There's a 100% Chance AI Agents Are Ruining the Internet

**原文链接**: [https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)

生成摘要时出错

---

## 69. Every invoice in Brazil's economy runs on SOAP 1.2

**原文标题**: Every invoice in Brazil's economy runs on SOAP 1.2

**原文链接**: [https://github.com/stoix-dev/sefaz-webservices-postman](https://github.com/stoix-dev/sefaz-webservices-postman)

生成摘要时出错

---

## 70. Garbage Trucks Now Have AI Cameras to Score Your House and Clock Code Violations

**原文标题**: Garbage Trucks Now Have AI Cameras to Score Your House and Clock Code Violations

**原文链接**: [https://www.thedrive.com/news/garbage-trucks-now-have-ai-cameras-to-score-your-house-and-clock-code-violations](https://www.thedrive.com/news/garbage-trucks-now-have-ai-cameras-to-score-your-house-and-clock-code-violations)

生成摘要时出错

---

## 71. Pion, an agent designed to run any company autonomously

**原文标题**: Pion, an agent designed to run any company autonomously

**原文链接**: [https://andonlabs.com/blog/why-we-built-pion](https://andonlabs.com/blog/why-we-built-pion)

生成摘要时出错

---

## 72. XCancel service is suspended until further notice

**原文标题**: XCancel service is suspended until further notice

**原文链接**: [https://xcancel.com/#](https://xcancel.com/#)

生成摘要时出错

---

## 73. High-performance garbage collection for C++

**原文标题**: High-performance garbage collection for C++

**原文链接**: [https://v8.dev/blog/high-performance-cpp-gc](https://v8.dev/blog/high-performance-cpp-gc)

生成摘要时出错

---

## 74. Backprop Alternative: Augmented Lagrangian Predictive Coding

**原文标题**: Backprop Alternative: Augmented Lagrangian Predictive Coding

**原文链接**: [https://pub.sakana.ai/pc-alm/](https://pub.sakana.ai/pc-alm/)

生成摘要时出错

---

## 75. US agency orders Tesla to answer questions on Cybercab certification

**原文标题**: US agency orders Tesla to answer questions on Cybercab certification

**原文链接**: [https://www.reuters.com/business/autos-transportation/us-agency-orders-tesla-answer-questions-cybercab-certification-2026-09-15/](https://www.reuters.com/business/autos-transportation/us-agency-orders-tesla-answer-questions-cybercab-certification-2026-09-15/)

生成摘要时出错

---

## 76. Meta-analysis of the association between childhood maltreatment and depression

**原文标题**: Meta-analysis of the association between childhood maltreatment and depression

**原文链接**: [https://doi.org/10.1111/acps.13794](https://doi.org/10.1111/acps.13794)

生成摘要时出错

---

## 77. 4,400-Year-Old Tomb of Egyptian Judge Found at Saqqara with Colors on Walls

**原文标题**: 4,400-Year-Old Tomb of Egyptian Judge Found at Saqqara with Colors on Walls

**原文链接**: [https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/](https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/)

生成摘要时出错

---

## 78. Dario, Please

**原文标题**: Dario, Please

**原文链接**: [https://pop.rdi.sh/dario-please/](https://pop.rdi.sh/dario-please/)

生成摘要时出错

---

## 79. Steam Frame starts at $1059

**原文标题**: Steam Frame starts at $1059

**原文链接**: [https://store.steampowered.com/hardware/steamframe](https://store.steampowered.com/hardware/steamframe)

生成摘要时出错

---

## 80. Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS

**原文标题**: Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS

**原文链接**: [https://github.com/JamesRyanATX/fcbnerd](https://github.com/JamesRyanATX/fcbnerd)

生成摘要时出错

---

## 81. Swift 6.4 Released

**原文标题**: Swift 6.4 Released

**原文链接**: [https://www.swift.org/blog/swift-6.4-released/](https://www.swift.org/blog/swift-6.4-released/)

生成摘要时出错

---

## 82. Lovable rewrites Vite in Rust – Reduces memory usage by 10x

**原文标题**: Lovable rewrites Vite in Rust – Reduces memory usage by 10x

**原文链接**: [https://lovable.dev/blog/faster-previews-oj](https://lovable.dev/blog/faster-previews-oj)

生成摘要时出错

---

## 83. I'm a doctor. Here's why I wouldn't get a full-body MRI scan

**原文标题**: I'm a doctor. Here's why I wouldn't get a full-body MRI scan

**原文链接**: [https://www.washingtonpost.com/wellness/2026/09/14/im-doctor-heres-why-i-wouldnt-get-full-body-mri-scan/](https://www.washingtonpost.com/wellness/2026/09/14/im-doctor-heres-why-i-wouldnt-get-full-body-mri-scan/)

生成摘要时出错

---

## 84. How my e-reader lost its stripes

**原文标题**: How my e-reader lost its stripes

**原文链接**: [https://www.serpentine.com/posts/2026/x3-stripes/](https://www.serpentine.com/posts/2026/x3-stripes/)

生成摘要时出错

---

## 85. Apple's Dimensional Drawings

**原文标题**: Apple's Dimensional Drawings

**原文链接**: [https://developer.apple.com/accessories/dimensional-drawings/](https://developer.apple.com/accessories/dimensional-drawings/)

生成摘要时出错

---

## 86. Cloudflare AKE cuts origin HelloRetryRequests from 52% to 3.7%

**原文标题**: Cloudflare AKE cuts origin HelloRetryRequests from 52% to 3.7%

**原文链接**: [https://blog.cloudflare.com/automatic-key-exchange-for-origins/](https://blog.cloudflare.com/automatic-key-exchange-for-origins/)

生成摘要时出错

---

## 87. Show HN: Open-source passive NFC tag that signs with ECDSA, verified on-chain

**原文标题**: Show HN: Open-source passive NFC tag that signs with ECDSA, verified on-chain

**原文链接**: [https://github.com/mwbpNFTechnology/toluTag/](https://github.com/mwbpNFTechnology/toluTag/)

生成摘要时出错

---

## 88. Global bond yields hit 2008 highs, raising stakes for big borrowers

**原文标题**: Global bond yields hit 2008 highs, raising stakes for big borrowers

**原文链接**: [https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/](https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/)

生成摘要时出错

---

## 89. Reddit Is Still Useful. It's Also Becoming Impossible

**原文标题**: Reddit Is Still Useful. It's Also Becoming Impossible

**原文链接**: [https://widdershins.verja.net/reddit-is-still-useful-its-also-becoming-impossible/](https://widdershins.verja.net/reddit-is-still-useful-its-also-becoming-impossible/)

生成摘要时出错

---

## 90. Pythoncall.jl – Python and Julia in Harmony

**原文标题**: Pythoncall.jl – Python and Julia in Harmony

**原文链接**: [https://github.com/JuliaPy/PythonCall.jl](https://github.com/JuliaPy/PythonCall.jl)

生成摘要时出错

---

## 91. Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher

**原文标题**: Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher

**原文链接**: [https://www.vals.ai/blogs/fable-solves-cyphral-distich](https://www.vals.ai/blogs/fable-solves-cyphral-distich)

生成摘要时出错

---

## 92. A20 Pro shatters Geekbench 7 single-core record – beats desktop i9 and Ryzen 9

**原文标题**: A20 Pro shatters Geekbench 7 single-core record – beats desktop i9 and Ryzen 9

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent](https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent)

生成摘要时出错

---

## 93. AI models chatting in 'surreal' dialect of poetic language and tech bro jargon

**原文标题**: AI models chatting in 'surreal' dialect of poetic language and tech bro jargon

**原文链接**: [https://www.theguardian.com/technology/2026/sep/15/syd-barrett-ai-chat-language-poetic-tech-bro-jargon-oversight](https://www.theguardian.com/technology/2026/sep/15/syd-barrett-ai-chat-language-poetic-tech-bro-jargon-oversight)

生成摘要时出错

---

## 94. Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama

**原文标题**: Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama

**原文链接**: [https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/](https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/)

生成摘要时出错

---

## 95. Charts built for Chat

**原文标题**: Charts built for Chat

**原文链接**: [https://dbtcharts.com/blog/charts-built-for-chat/](https://dbtcharts.com/blog/charts-built-for-chat/)

生成摘要时出错

---

## 96. Optimizing a Spin-Lock

**原文标题**: Optimizing a Spin-Lock

**原文链接**: [https://david.alvarezrosa.com/posts/optimizing-a-spin-lock/](https://david.alvarezrosa.com/posts/optimizing-a-spin-lock/)

生成摘要时出错

---

## 97. German companies rely almost exclusively on AI models and services from the USA

**原文标题**: German companies rely almost exclusively on AI models and services from the USA

**原文链接**: [https://www.heise.de/en/news/US-AI-dominates-companies-China-models-hardly-used-EU-AI-plays-no-role-11446969.html](https://www.heise.de/en/news/US-AI-dominates-companies-China-models-hardly-used-EU-AI-plays-no-role-11446969.html)

生成摘要时出错

---

## 98. OpenAI bots knew about the RubyGems caching vulnerability

**原文标题**: OpenAI bots knew about the RubyGems caching vulnerability

**原文链接**: [https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/](https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/)

生成摘要时出错

---

## 99. Spaceships (Reverse Asteroid)

**原文标题**: Spaceships (Reverse Asteroid)

**原文链接**: [https://spaceships.treybastian.com/](https://spaceships.treybastian.com/)

生成摘要时出错

---

## 100. Our chance to take down the Epstein class

**原文标题**: Our chance to take down the Epstein class

**原文链接**: [https://thomasmassie.org/members-of-congress-that-currently-support-epstein/](https://thomasmassie.org/members-of-congress-that-currently-support-epstein/)

生成摘要时出错

---

