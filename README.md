# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-18.md)

*最后自动更新时间: 2026-05-18 19:17:22*
## 1. Anthropic 收购 Stainless

**原文标题**: Anthropic acquires Stainless

**原文链接**: [https://www.anthropic.com/news/anthropic-acquires-stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)

2026年5月18日，Anthropic 宣布收购 SDK（软件开发工具包）和 MCP（模型上下文协议）服务器工具领域的领导者 Stainless。这一战略举措旨在加速 Anthropic 的转型——从开发回答查询的模型转向创建“采取行动的智能体”。

Stainless 成立于 2022 年，与 Anthropic 有着深厚的渊源，自 Claude API 早期阶段起就为其官方 SDK 提供支持。该公司专注于将 API 规范转化为跨多个平台（包括 TypeScript、Python、Go、Java 和 Kotlin）的快速、语言原生的 SDK 和连接器。

此次收购主要围绕两个核心目标：
*   **增强智能体连接性：** Anthropic 旨在利用 Stainless 的技术提升 Claude 连接外部数据和工具的能力，这对于自主 AI 智能体至关重要。
*   **优化开发者体验：** 通过整合 Stainless 团队，Anthropic 计划推进 Claude 平台和模型上下文协议 (MCP)，使开发者能够更轻松地构建和扩展 AI 驱动的应用。

Anthropic 平台工程负责人 Katelyn Lesse 指出，AI 智能体的能力取决于其能够触达的系统，而 Stainless 提供了必要的“触达能力”。Stainless 首席执行官 Alex Rattray 强调，鉴于双方的合作历史以及在其工具发挥最大作用的平台上工作的机会，此次收购是水到渠成的。这一举措强化了 Anthropic 构建强大智能体 AI 生态系统的承诺。

---

## 2. 我们利用 Git 的 --author 选项阻止了 GitHub 仓库中的 AI 机器人垃圾信息

**原文标题**: We stopped AI bot spam in our GitHub repo using Git's –author flag

**原文链接**: [https://archestra.ai/blog/only-responsible-ai](https://archestra.ai/blog/only-responsible-ai)

开源初创公司 Archestra 最近遭遇了 AI 生成的垃圾信息和“垃圾内容（slop）”的“大流行”，其 GitHub 仓库不堪重负。在宣布一项 900 美元的悬赏任务后，该项目的 Issue 区涌入了数百个凭空捏造的实施方案和低质量的 PR（拉取请求）。这种“噪音之墙”掩盖了真正的贡献者，迫使维护者每周花费数小时进行手动清理。

为了应对这一挑战，团队采取了“终极手段”，启用了 GitHub 的“仅限先前的贡献者（Limit to prior contributors）”设置。虽然这有效阻止了机器人，但也阻隔了新的合法人类贡献者。为此，Archestra 开发了一种技术变通方案，利用 Git 的 `--author` 标志来自动化白名单流程。

**新成员入职流程：**
1. **验证：** 潜在贡献者需访问外部网站通过 CAPTCHA 验证，并同意 AI 道德准则。
2. **自动提交：** 验证成功后，一个 GitHub Action 会识别该用户的唯一 `noreply` 邮箱地址。
3. **身份归属：** 该 Action 在 `main` 分支上创建一个提交（将用户添加到 `EXTERNAL_CONTRIBUTORS.md` 文件中），并利用 `--author` 标志将该提交归属于该新用户。
4. **授予权限：** 由于 GitHub 将在 `main` 分支上有提交记录的任何人识别为“先前的贡献者”，该用户将立即获得评论和发起 PR 的白名单权限。

作者指出，虽然 GitHub 乐见由 AI 驱动的活跃度指标增长，但这些指标往往掩盖了贡献质量的下降。通过将“以人为本”的质量置于“虚高”的 AI 活跃度之上，Archestra 旨在保护其项目免受 AI 垃圾内容带来的安全风险和成员精力枯竭，并呼吁开源社区正视生成式 AI 对协作带来的负面影响。

---

## 3. Haiku OS runs on M1 Macs now

**原文标题**: Haiku OS runs on M1 Macs now

**原文链接**: [https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2](https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2)

生成摘要时出错

---

## 4. 埃隆·马斯克在针对萨姆·奥特曼和OpenAI的诉讼中败诉。

**原文标题**: Elon Musk has lost his lawsuit against Sam Altman and OpenAI

**原文链接**: [https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/)

埃隆·马斯克在针对 OpenAI、联合创始人萨姆·阿尔特曼和格雷格·布罗克曼以及微软的诉讼中败诉。加利福尼亚州的一个陪审团作出一致裁定，认为马斯克的起诉已超过法定诉讼时效。

马斯克在诉讼中指控被告通过将非营利性 AI 实验室转变为营利性附属机构，“窃取了一个慈善机构”。然而，陪审团判定，任何所谓的损害均发生在 2021 年底和 2022 年的具体起诉截止日期之前。法官伊冯娜·冈萨雷斯·罗杰斯支持该裁决，指出有大量证据支持被告方，并对马斯克方专家证词表示怀疑，该证词曾估算马斯克因此蒙受的“不当收益”损失在 788 亿至 1350 亿美元之间。

此案的终结消除了 OpenAI 面临的一项重大法律威胁，尤其是潜在的重组风险，据报道该公司目前正准备首次公开募股（IPO）。曾被指控协助和教唆违反慈善信托的微软公司对裁决表示欢迎，并重申了与 OpenAI 的持续合作伙伴关系。

尽管遭遇法律挫折，马斯克的首席律师马克·托伯罗夫表示，他们打算对该判决提出上诉。

---

## 5. 刚果（金）埃博拉疫情已致至少100人死亡

**原文标题**: At least 100 deaths reported in Ebola outbreak in DR Congo

**原文链接**: [https://www.bbc.com/news/articles/cq6pz60p996o](https://www.bbc.com/news/articles/cq6pz60p996o)

An Ebola outbreak in the Democratic Republic of Congo (DRC) has resulted in at least 100 deaths and more than 390 suspected cases, leading the World Health Organization (WHO) to declare it an international emergency. The outbreak, centered in the Ituri province, has already spread to Uganda, where two cases and one death have been confirmed.

The current crisis is driven by the **Bundibugyo virus**, a strain for which there are currently no approved vaccines or treatments. Because of this, health officials are emphasizing public health protocols, specifically warning against traditional funeral practices involving the washing of bodies, which historically contributed to mass infections.

The situation has direct implications for the United States, as at least six Americans have been exposed to the virus. One is reportedly symptomatic, while three others are considered high-risk contacts. The U.S. government is currently arranging for their evacuation and quarantine, potentially at a military base in Germany. 

In response to the escalating risk, the CDC has:
*   Issued a **Level 4 travel advisory** (the most severe) for the DRC.
*   Implemented entry restrictions and monitoring for travelers arriving from the DRC, Uganda, and South Sudan.
*   Increased hospital readiness and testing capacity within the U.S.

While the WHO states the outbreak does not yet meet the criteria for a pandemic, it warns of a "much larger outbreak" if containment fails. Neighboring countries, including Rwanda and Nigeria, have heightened border screenings and surveillance to prevent further regional spread.

---

## 6. Show HN: Files.md – Obsidian 的开源替代方案

**原文标题**: Show HN: Files.md – Open-source alternative to Obsidian

**原文链接**: [https://github.com/zakirullin/files.md](https://github.com/zakirullin/files.md)

**Files.md** 是一款开源、本地优先的 Obsidian 替代方案，旨在实现简约、隐私和长久使用。该应用历经五年开发，用户无需安装或服务器端数据存储，即可通过纯 Markdown 文件管理笔记、日志和任务。

**核心功能与技术理念：**
*   **基于浏览器且支持离线：** 它作为渐进式 Web 应用 (PWA) 运行。用户只需在浏览器中打开 `index.html` 即可离线工作，无需构建系统或复杂的依赖。
*   **隐私优先：** 数据默认保存在用户设备上。同步是可选的，可通过云端文件夹（iCloud/Dropbox/Google Drive）、自托管的 Go 二进制文件或托管服务来处理。
*   **极简设计：** 该项目避开了类似 Obsidian 的“插件陷阱”，更倾向于提供能激发创造力和深度思考的“必要功能”，而非复杂的模板。
*   **LLM 友好：** 代码和文件结构旨在让 AI 智能体易于解析，并提供了 `llms.txt` 方案。
*   **Telegram 集成：** 包含一个用于“随时随地”访问的聊天机器人，允许用户将想法直接记录到 `Chat.md` 或收件箱文件中。

**“第一大脑”方法论：**
开发者强调，该工具旨在对抗“通过过度整理获得掌控感”的幻觉。Files.md 鼓励“一条笔记一个想法”的方法，而不是构建一个推迟实际思考的复杂“第二大脑”。其目标是利用该工具进行系统性思考和见解生成，而非单纯的信息囤积。

**面向开发者：**
代码库刻意保持简洁，旨在让个人或 LLM 都能轻松阅读。它通过将所有库本地化（vendoring）来避免外部依赖，确保项目在未来几十年内仍能保持功能性和便携性。它使用标准的 Markdown 链接，以确保跨平台兼容性和知识的可迁移性。

---

## 7. Bitwarden 的悄然翻新

**原文标题**: The Quiet Renovation at Bitwarden

**原文链接**: [https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden](https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden)

文章指出，Bitwarden 正在悄然发生根本性的转变，逐渐背离其以用户为中心、开源的初衷，转向由私募股权驱动的退场策略。作者强调了多个“数据点”，暗示该公司正为了未来的出售或合并进行资产“清理”。

**核心观点包括：**

*   **领导层变动：** 长期担任 CEO 的 Michael Crandell 已被 Michael Sullivan 悄然取代，后者是擅长私募股权（PE）整合及兼并收购（M&A）的高管。一名拥有类似背景的新任 CFO 也已上任，而创始人则留任 CTO。
*   **撤回承诺：** 个人密码管理页面删除了“始终免费”的字样。在此之前，该公司曾对高级账户进行过一次沟通不力的涨价。
*   **价值观转变：** Bitwarden 的核心价值观（GRIT）在未发布公告的情况下进行了修改。“包容”和“透明”被替换为“创新”和“信任”，这一变动被掩埋在了一篇仅修改了一半的 2022 年博文中。
*   **缺乏透明度：** 这些重大的公司变动并未通过新闻稿或博文正式发布，反映出一种“掩埋”消息以规避用户监督的模式。
*   **对用户的影响：** 作者认为 Bitwarden 正在遵循一种熟悉的生命周期：先建立信任和依赖，然后悄悄修改条款以实现利润最大化。

作者目前已迁移至自托管的 **Vaultwarden** 实例，并警告称，虽然得益于 Bitwarden 的开源客户端，目前自托管方案依然可行，但新管理层最终可能会破坏 API 兼容性或关闭源代码。如果 Bitwarden 最终被大公司收购，社区可能被迫通过创建软件分支（Fork）来维持该平台最初的独立性和透明度。

---

## 8. Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint

**原文标题**: Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint

**原文链接**: [https://modal.com/blog/truly-serverless-gpus](https://modal.com/blog/truly-serverless-gpus)

生成摘要时出错

---

## 9. Iran will impose fees on subsea internet cables in Strait of Hormuz

**原文标题**: Iran will impose fees on subsea internet cables in Strait of Hormuz

**原文链接**: [https://www.cnn.com/2026/05/17/middleeast/iran-hormuz-undersea-cables-intl](https://www.cnn.com/2026/05/17/middleeast/iran-hormuz-undersea-cables-intl)

This article describes a plan by Iran to impose fees and licensing requirements on subsea internet cables passing through the Strait of Hormuz. Targeting major tech companies like Google, Meta, Microsoft, and Amazon, Tehran seeks to extract revenue and grant exclusive maintenance rights to state-linked Iranian firms.

Set against a backdrop of renewed regional tensions in May 2026, the move is seen as an attempt to convert geographic leverage into strategic and economic power. By threatening the "hidden arteries" of the global economy, Iran aims to deter future military attacks by demonstrating its ability to cause a "digital catastrophe."

Key points include:

*   **Scope:** While many cables are located in Omani waters, at least two major lines (Falcon and GBI) pass through Iranian territory. 
*   **Legal Justification:** Iran cites the UN Convention on the Law of the Sea, attempting to emulate Egypt’s model of charging for subsea cables in the Suez Canal. However, experts note the legal distinction between an artificial canal and a natural strait.
*   **Enforcement Challenges:** Because U.S. sanctions prohibit American firms from paying Iran, the policy may be viewed as posturing. Nevertheless, state-linked media has vaguely threatened disruptions if firms do not comply.
*   **Global Impact:** Although the affected cables carry less than 1% of global bandwidth, disruptions could severely impact regional banking, energy exports, and connectivity in India, East Africa, and the Middle East.

Ultimately, the strategy highlights Iran's use of asymmetric warfare to exert pressure on global markets and ensure regime survival by raising the potential cost of conflict for the international community.

---

## 10. What Is Date:Italy?

**原文标题**: What Is Date:Italy?

**原文链接**: [http://aesthetikx.info/blog/date_italy.html](http://aesthetikx.info/blog/date_italy.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 2 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 3 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 4 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 5 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 6 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 7 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 8 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 9 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 10 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 11 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 12 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 13 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 14 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 15 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 16 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 17 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 18 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 19 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 20 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 21 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 22 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 23 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 24 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 25 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 26 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 27 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 28 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 29 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 30 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 31 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 32 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 33 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 34 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 35 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 36 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 37 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 38 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 39 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 40 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 41 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 42 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 43 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 44 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 45 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 46 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 47 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 48 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 49 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 50 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 51 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 52 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 53 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 54 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 55 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 56 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 57 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 58 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 59 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 60 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 61 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 62 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 63 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 64 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 65 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 66 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 67 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 68 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 69 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 70 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 71 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 72 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 73 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 74 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 75 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 76 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 77 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 78 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 79 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 80 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 81 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 82 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 83 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 84 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 85 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 86 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 87 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 88 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 89 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 90 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 91 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 92 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 93 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 94 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 95 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 96 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 97 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 98 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 99 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 100 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 101 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 102 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 103 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 104 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 105 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 106 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 107 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 108 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 109 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 110 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 111 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 112 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 113 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 114 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 115 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 116 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 117 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 118 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 119 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 120 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 121 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 122 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 123 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 124 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 125 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 126 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 127 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 128 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 129 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 130 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 131 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 132 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 133 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 134 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 135 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 136 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 137 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 138 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 139 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 140 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 141 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 142 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 143 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 144 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 145 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 146 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 147 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 148 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 149 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 150 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 151 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 152 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 153 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 154 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 155 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 156 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 157 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 158 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 159 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 160 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 161 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 162 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 163 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 164 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 165 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 166 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 167 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 168 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 169 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 170 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 171 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 172 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 173 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 174 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 175 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 176 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 177 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 178 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 179 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 180 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 181 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 182 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 183 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 184 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 185 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 186 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 187 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 188 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 189 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 190 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 191 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 192 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 193 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 194 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 195 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 196 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 197 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 198 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 199 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 200 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 201 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 202 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 203 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 204 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 205 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 206 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 207 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 208 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 209 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 210 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 211 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 212 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 213 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 214 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 215 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 216 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 217 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 218 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 219 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 220 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 221 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 222 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 223 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 224 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 225 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 226 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 227 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 228 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 229 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 230 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 231 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 232 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 233 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 234 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 235 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 236 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 237 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 238 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 239 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 240 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 241 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 242 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 243 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 244 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 245 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 246 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 247 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 248 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 249 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 250 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 251 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 252 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 253 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 254 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 255 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 256 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 257 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 258 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 259 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 260 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 261 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 262 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 263 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 264 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 265 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 266 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 267 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 268 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 269 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 270 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 271 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 272 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 273 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 274 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 275 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 276 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 277 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 278 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 279 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 280 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 281 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 282 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 283 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 284 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 285 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 286 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 287 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 288 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 289 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 290 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 291 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 292 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 293 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 294 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 295 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 296 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 297 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 298 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 299 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 300 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 301 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 302 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 303 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 304 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 305 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 306 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 307 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 308 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 309 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 310 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 311 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 312 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 313 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 314 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 315 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 316 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 317 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 318 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 319 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 320 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 321 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 322 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 323 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 324 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 325 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 326 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 327 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 328 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 329 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 330 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 331 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 332 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 333 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 334 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 335 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 336 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 337 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 338 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 339 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 340 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 341 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 342 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 343 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 344 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 345 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 346 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 347 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 348 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 349 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 350 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 351 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 352 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 353 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 354 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 355 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 356 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 357 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 358 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 359 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 360 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 361 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 362 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 363 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 364 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 365 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 366 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 367 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 368 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 369 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 370 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 371 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 372 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 373 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 374 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 375 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 376 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 377 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 378 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 379 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 380 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 381 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 382 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 383 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 384 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 385 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 386 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 387 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 388 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 389 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 390 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 391 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 392 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 393 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 394 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 395 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 396 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 397 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 398 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 399 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 400 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 401 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 402 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 403 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 404 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 405 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 406 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 407 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 408 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 409 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 410 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 411 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 412 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 413 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 414 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 415 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 416 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 417 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 418 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 419 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 420 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 421 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 422 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 423 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 424 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
