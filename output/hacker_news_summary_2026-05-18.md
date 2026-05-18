# Hacker News 热门文章摘要 (2026-05-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The Fil-C Optimized Calling Convention

**原文标题**: The Fil-C Optimized Calling Convention

**原文链接**: [https://fil-c.org/calling_convention](https://fil-c.org/calling_convention)

生成摘要时出错

---

## 12. Two computers, one monitor, zero fiddling (2025)

**原文标题**: Two computers, one monitor, zero fiddling (2025)

**原文链接**: [https://alexplescan.com/posts/2025/08/16/kvm/](https://alexplescan.com/posts/2025/08/16/kvm/)

生成摘要时出错

---

## 13. Project Glasswing: what Mythos showed us

**原文标题**: Project Glasswing: what Mythos showed us

**原文链接**: [https://blog.cloudflare.com/cyber-frontier-models/](https://blog.cloudflare.com/cyber-frontier-models/)

生成摘要时出错

---

## 14. 语音人工智能系统易受隐藏音频攻击

**原文标题**: Voice AI Systems Are Vulnerable to Hidden Audio Attacks

**原文链接**: [https://spectrum.ieee.org/voice-ai-audio-attacks](https://spectrum.ieee.org/voice-ai-audio-attacks)

In the article "Voice AI Systems Are Vulnerable to Hidden Audio Attacks," Edd Gent reports on research exposing a critical security flaw in voice-activated artificial intelligence. The study reveals that AI models can be manipulated by audio signals that are completely inaudible to the human ear.

These "hidden audio attacks" function by utilizing ultrasonic frequencies or subtle noise patterns that humans cannot detect but that AI systems interpret as valid commands. By embedding these signals into music, white noise, or broadcast media, attackers can hijack a device's behavior without the user's knowledge. This vulnerability could allow malicious actors to trigger unauthorized actions, such as opening smart locks, accessing sensitive personal data, or making unauthorized purchases.

As voice AI becomes increasingly integrated into smart homes and critical infrastructure, the implications of these findings are significant. The research highlights that while AI models have become highly sensitive to speech, they lack the necessary filters to distinguish between intentional human voices and adversarial inaudible signals. The article concludes that developers must prioritize the creation of more robust defense mechanisms and signal-filtering technologies to protect users from these invisible threats.

---

## 15. Qwen 3.7 Preview

**原文标题**: Qwen 3.7 Preview

**原文链接**: [https://twitter.com/Alibaba_Qwen/status/2056403591464984753](https://twitter.com/Alibaba_Qwen/status/2056403591464984753)

生成摘要时出错

---

## 16. The Aperiodic Table

**原文标题**: The Aperiodic Table

**原文链接**: [https://blog.jgc.org/2026/05/the-aperiodic-table.html](https://blog.jgc.org/2026/05/the-aperiodic-table.html)

生成摘要时出错

---

## 17. Learn Harness Engineering

**原文标题**: Learn Harness Engineering

**原文链接**: [https://walkinglabs.github.io/learn-harness-engineering/en/](https://walkinglabs.github.io/learn-harness-engineering/en/)

生成摘要时出错

---

## 18. Show HN: InsForge – Open-source Heroku for coding agents

**原文标题**: Show HN: InsForge – Open-source Heroku for coding agents

**原文链接**: [https://github.com/InsForge/InsForge](https://github.com/InsForge/InsForge)

生成摘要时出错

---

## 19. Garry Tan, the CEO of YC, accused me of unethical reporting

**原文标题**: Garry Tan, the CEO of YC, accused me of unethical reporting

**原文链接**: [https://radleybalko.substack.com/p/truth-power-and-honest-journalism](https://radleybalko.substack.com/p/truth-power-and-honest-journalism)

生成摘要时出错

---

## 20. 'We mould trees to grow into the shape of chairs'

**原文标题**: 'We mould trees to grow into the shape of chairs'

**原文链接**: [https://www.bbc.co.uk/news/articles/cvg0yy3gp71o](https://www.bbc.co.uk/news/articles/cvg0yy3gp71o)

生成摘要时出错

---

## 21. It is time to give up the dualism introduced by the debate on consciousness

**原文标题**: It is time to give up the dualism introduced by the debate on consciousness

**原文链接**: [https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/](https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/)

生成摘要时出错

---

## 22. 1024000^2 Blocks, 2B2T Minecraft Server World Download Project, and Discoveries

**原文标题**: 1024000^2 Blocks, 2B2T Minecraft Server World Download Project, and Discoveries

**原文链接**: [https://github.com/2b2tplace/1m_release](https://github.com/2b2tplace/1m_release)

生成摘要时出错

---

## 23. Linux security mailing list 'almost unmanageable'

**原文标题**: Linux security mailing list 'almost unmanageable'

**原文链接**: [https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633](https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633)

生成摘要时出错

---

## 24. Actually, democracy dies in H.R.

**原文标题**: Actually, democracy dies in H.R.

**原文链接**: [https://www.nytimes.com/2026/05/18/world/americas/actually-democracy-dies-in-hr.html](https://www.nytimes.com/2026/05/18/world/americas/actually-democracy-dies-in-hr.html)

生成摘要时出错

---

## 25. Porting my 3D points renderer on a ZX Spectrum 48K

**原文标题**: Porting my 3D points renderer on a ZX Spectrum 48K

**原文链接**: [https://github.com/ttsiodras/3D-on-a-ZX-Spectrum-48K/](https://github.com/ttsiodras/3D-on-a-ZX-Spectrum-48K/)

生成摘要时出错

---

## 26. When Kierkegaard Got Cancelled

**原文标题**: When Kierkegaard Got Cancelled

**原文链接**: [https://www.plough.com/en/topics/faith/discipleship/when-kierkegaard-got-cancelled](https://www.plough.com/en/topics/faith/discipleship/when-kierkegaard-got-cancelled)

生成摘要时出错

---

## 27. Strange crystals found inside wreckage from the first nuclear bomb test

**原文标题**: Strange crystals found inside wreckage from the first nuclear bomb test

**原文链接**: [https://www.scientificamerican.com/article/strange-crystals-found-inside-wreckage-from-the-first-nuclear-bomb-test/](https://www.scientificamerican.com/article/strange-crystals-found-inside-wreckage-from-the-first-nuclear-bomb-test/)

生成摘要时出错

---

## 28. Haiku OS runs on M1 Macs now

**原文标题**: Haiku OS runs on M1 Macs now

**原文链接**: [https://www.osnews.com/story/144985/haiku-os-runs-on-m1-macs-now/](https://www.osnews.com/story/144985/haiku-os-runs-on-m1-macs-now/)

生成摘要时出错

---

## 29. Enough with the AI FOMO, go slow-mo, says Domo CDO

**原文标题**: Enough with the AI FOMO, go slow-mo, says Domo CDO

**原文链接**: [https://www.theregister.com/ai-ml/2026/05/17/enough-with-the-ai-fomo-go-slow-mo-says-domo-cdo/5240840](https://www.theregister.com/ai-ml/2026/05/17/enough-with-the-ai-fomo-go-slow-mo-says-domo-cdo/5240840)

生成摘要时出错

---

## 30. Don't answer the first question

**原文标题**: Don't answer the first question

**原文链接**: [https://lalitm.com/post/dont-answer-the-first-question/](https://lalitm.com/post/dont-answer-the-first-question/)

生成摘要时出错

---

## 31. Cursor Introduces Composer 2.5

**原文标题**: Cursor Introduces Composer 2.5

**原文链接**: [https://twitter.com/cursor_ai/status/2056415413077233983](https://twitter.com/cursor_ai/status/2056415413077233983)

生成摘要时出错

---

## 32. Anduril and Meta's quest to make smart glasses for warfare

**原文标题**: Anduril and Meta's quest to make smart glasses for warfare

**原文链接**: [https://www.technologyreview.com/2026/05/18/1137412/inside-anduril-and-metas-quest-to-make-smart-glasses-for-warfare/](https://www.technologyreview.com/2026/05/18/1137412/inside-anduril-and-metas-quest-to-make-smart-glasses-for-warfare/)

生成摘要时出错

---

## 33. Iran starts Bitcoin-backed ship insurance for Hormuz strait

**原文标题**: Iran starts Bitcoin-backed ship insurance for Hormuz strait

**原文链接**: [https://www.bloomberg.com/news/articles/2026-05-18/iran-starts-bitcoin-backed-shipping-insurance-for-hormuz-strait](https://www.bloomberg.com/news/articles/2026-05-18/iran-starts-bitcoin-backed-shipping-insurance-for-hormuz-strait)

生成摘要时出错

---

## 34. Researchers Wanted Preschool Teachers to Wear Cameras to Train AI

**原文标题**: Researchers Wanted Preschool Teachers to Wear Cameras to Train AI

**原文链接**: [https://www.404media.co/researchers-wanted-preschool-teachers-to-wear-cameras-to-train-ai/](https://www.404media.co/researchers-wanted-preschool-teachers-to-wear-cameras-to-train-ai/)

生成摘要时出错

---

## 35. Show HN: Auto-identity-remove – Automated data broker opt-out runner for macOS

**原文标题**: Show HN: Auto-identity-remove – Automated data broker opt-out runner for macOS

**原文链接**: [https://github.com/stephenlthorn/auto-identity-remove](https://github.com/stephenlthorn/auto-identity-remove)

生成摘要时出错

---

## 36. The foundations of a provably secure operating system (PSOS) (1979) [pdf]

**原文标题**: The foundations of a provably secure operating system (PSOS) (1979) [pdf]

**原文链接**: [http://www.csl.sri.com/users/neumann/psos.pdf](http://www.csl.sri.com/users/neumann/psos.pdf)

生成摘要时出错

---

## 37. Ask an Astronaut: 333 hours of Q&A footage with astronauts

**原文标题**: Ask an Astronaut: 333 hours of Q&A footage with astronauts

**原文链接**: [https://askanastronaut.issinrealtime.org/](https://askanastronaut.issinrealtime.org/)

生成摘要时出错

---

## 38. Build a Radio Wave Detector with Balls of Aluminum Foil

**原文标题**: Build a Radio Wave Detector with Balls of Aluminum Foil

**原文链接**: [https://www.wired.com/story/build-a-radio-wave-detector-with-balls-of-aluminum-foil/](https://www.wired.com/story/build-a-radio-wave-detector-with-balls-of-aluminum-foil/)

生成摘要时出错

---

## 39. Jank now has its own custom IR

**原文标题**: Jank now has its own custom IR

**原文链接**: [https://jank-lang.org/blog/2026-05-08-optimization/](https://jank-lang.org/blog/2026-05-08-optimization/)

生成摘要时出错

---

## 40. NASA still maintains some of the Voyager spacecraft code from the 70s era

**原文标题**: NASA still maintains some of the Voyager spacecraft code from the 70s era

**原文链接**: [https://spacedaily.com/nasa-still-maintains-some-of-the-voyager-spacecraft-code-in-a-1970s-era-programming-language-that-almost-nobody-on-earth-fully-understands-anymore-and-the-handful-of-engineers-who-do-are-now-in-their/](https://spacedaily.com/nasa-still-maintains-some-of-the-voyager-spacecraft-code-in-a-1970s-era-programming-language-that-almost-nobody-on-earth-fully-understands-anymore-and-the-handful-of-engineers-who-do-are-now-in-their/)

生成摘要时出错

---

## 41. GenCAD

**原文标题**: GenCAD

**原文链接**: [https://gencad.github.io/](https://gencad.github.io/)

生成摘要时出错

---

## 42. WriteUp: 16 Bytes of x86 that turn Matrix rain into sound

**原文标题**: WriteUp: 16 Bytes of x86 that turn Matrix rain into sound

**原文链接**: [https://hellmood.111mb.de//wake_up_16b_writeup.html](https://hellmood.111mb.de//wake_up_16b_writeup.html)

生成摘要时出错

---

## 43. Prolog Coding Horror

**原文标题**: Prolog Coding Horror

**原文链接**: [https://www.metalevel.at/prolog/horror](https://www.metalevel.at/prolog/horror)

生成摘要时出错

---

## 44. Linux 6.6 LTS To Linux 7.1 Bechmarks: Performance Up 13% Threadripper Over 3 yrs

**原文标题**: Linux 6.6 LTS To Linux 7.1 Bechmarks: Performance Up 13% Threadripper Over 3 yrs

**原文链接**: [https://www.phoronix.com/review/linux-66-linux-71](https://www.phoronix.com/review/linux-66-linux-71)

生成摘要时出错

---

## 45. AI eats the world (Spring 26) [pdf]

**原文标题**: AI eats the world (Spring 26) [pdf]

**原文链接**: [https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

生成摘要时出错

---

## 46. Magical Realism: “Northern Exposure” 25 Years Later (2015)

**原文标题**: Magical Realism: “Northern Exposure” 25 Years Later (2015)

**原文链接**: [https://www.rogerebert.com/streaming/magical-realism-nothern-exposure-25-years-later](https://www.rogerebert.com/streaming/magical-realism-nothern-exposure-25-years-later)

生成摘要时出错

---

## 47. A Master's Degree Isn't the Job Guarantee It Used to Be

**原文标题**: A Master's Degree Isn't the Job Guarantee It Used to Be

**原文链接**: [https://www.wsj.com/lifestyle/careers/a-masters-degree-isnt-the-job-guarantee-it-used-to-be-53e237aa](https://www.wsj.com/lifestyle/careers/a-masters-degree-isnt-the-job-guarantee-it-used-to-be-53e237aa)

生成摘要时出错

---

## 48. I turned a $80 RK3562 Android tablet into a Debian Linux workstation

**原文标题**: I turned a $80 RK3562 Android tablet into a Debian Linux workstation

**原文链接**: [https://github.com/tech4bot/rk3562deb](https://github.com/tech4bot/rk3562deb)

生成摘要时出错

---

## 49. I'm a Normie. Can Normies Vibe Code?

**原文标题**: I'm a Normie. Can Normies Vibe Code?

**原文链接**: [https://www.wired.com/story/normie-vibe-code/](https://www.wired.com/story/normie-vibe-code/)

生成摘要时出错

---

## 50. How to deal with your kid leaving

**原文标题**: How to deal with your kid leaving

**原文链接**: [https://buttondown.com/monteiro/archive/how-to-deal-with-your-kid-leaving/](https://buttondown.com/monteiro/archive/how-to-deal-with-your-kid-leaving/)

生成摘要时出错

---

## 51. Why is Google Maps back to showing old satellite images of Altadena?

**原文标题**: Why is Google Maps back to showing old satellite images of Altadena?

**原文链接**: [https://www.reddit.com/r/pasadena/s/94BHlkE84r](https://www.reddit.com/r/pasadena/s/94BHlkE84r)

生成摘要时出错

---

## 52. A Good Lemma Is Worth a Thousand Theorems (2007)

**原文标题**: A Good Lemma Is Worth a Thousand Theorems (2007)

**原文链接**: [https://sites.math.rutgers.edu/~zeilberg/Opinion82.html](https://sites.math.rutgers.edu/~zeilberg/Opinion82.html)

生成摘要时出错

---

## 53. Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely

**原文标题**: Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely

**原文链接**: [https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base](https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base)

生成摘要时出错

---

## 54. Graphing Scientific Calculator Based on the ESP32

**原文标题**: Graphing Scientific Calculator Based on the ESP32

**原文链接**: [https://github.com/El-EnderJ/NeoCalculator](https://github.com/El-EnderJ/NeoCalculator)

生成摘要时出错

---

## 55. Show HN: Mezz, a curl-able WiFi sandbox for IoT pentesting

**原文标题**: Show HN: Mezz, a curl-able WiFi sandbox for IoT pentesting

**原文链接**: [https://github.com/ABGEO/mezz](https://github.com/ABGEO/mezz)

生成摘要时出错

---

## 56. Ksharp – k version 3 Language Interpreter in C#

**原文标题**: Ksharp – k version 3 Language Interpreter in C#

**原文链接**: [https://github.com/ERufian/ksharp](https://github.com/ERufian/ksharp)

生成摘要时出错

---

## 57. Cannibalistic attacks between gray seals leave telltale “corkscrew” injuries

**原文标题**: Cannibalistic attacks between gray seals leave telltale “corkscrew” injuries

**原文链接**: [https://www.science.org/content/article/scientists-id-corkscrew-killer-behind-gruesome-seal-deaths](https://www.science.org/content/article/scientists-id-corkscrew-killer-behind-gruesome-seal-deaths)

生成摘要时出错

---

## 58. Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

**原文标题**: Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

**原文链接**: [https://github.com/MinishLab/semble](https://github.com/MinishLab/semble)

生成摘要时出错

---

## 59. C++26 Shipped a SIMD Library Nobody Asked For

**原文标题**: C++26 Shipped a SIMD Library Nobody Asked For

**原文链接**: [https://lucisqr.substack.com/p/c26-shipped-a-simd-library-nobody](https://lucisqr.substack.com/p/c26-shipped-a-simd-library-nobody)

生成摘要时出错

---

## 60. Profunctor Equipment in Haskell

**原文标题**: Profunctor Equipment in Haskell

**原文链接**: [https://bartoszmilewski.com/2026/05/16/profunctor-equipment-in-haskell/](https://bartoszmilewski.com/2026/05/16/profunctor-equipment-in-haskell/)

生成摘要时出错

---

## 61. Jury Sides with OpenAI, Sam Altman in Case Brought by Elon Musk

**原文标题**: Jury Sides with OpenAI, Sam Altman in Case Brought by Elon Musk

**原文链接**: [https://www.wsj.com/tech/ai/jury-sides-with-openai-sam-altman-in-case-brought-by-elon-musk-933240ff](https://www.wsj.com/tech/ai/jury-sides-with-openai-sam-altman-in-case-brought-by-elon-musk-933240ff)

生成摘要时出错

---

## 62. America Needs to Build More Housing

**原文标题**: America Needs to Build More Housing

**原文链接**: [https://www.nytimes.com/interactive/2026/05/18/opinion/affordable-housing-america.html](https://www.nytimes.com/interactive/2026/05/18/opinion/affordable-housing-america.html)

生成摘要时出错

---

## 63. Kyber (YC W23) Is Hiring a Founding Marketer

**原文标题**: Kyber (YC W23) Is Hiring a Founding Marketer

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community](https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community)

生成摘要时出错

---

## 64. Demo in 16 Bytes [video]

**原文标题**: Demo in 16 Bytes [video]

**原文链接**: [https://www.youtube.com/watch?v=MvycyU-kLjg](https://www.youtube.com/watch?v=MvycyU-kLjg)

生成摘要时出错

---

## 65. Tesla Solar Roof is on life support as it pivot to panels

**原文标题**: Tesla Solar Roof is on life support as it pivot to panels

**原文链接**: [https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/](https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/)

生成摘要时出错

---

## 66. The US is betting on AI to catch insider trading in prediction markets

**原文标题**: The US is betting on AI to catch insider trading in prediction markets

**原文链接**: [https://www.wired.com/story/polymarket-insider-trading-cftc-michael-selig-interview/](https://www.wired.com/story/polymarket-insider-trading-cftc-michael-selig-interview/)

生成摘要时出错

---

## 67. AI is a technology not a product

**原文标题**: AI is a technology not a product

**原文链接**: [https://daringfireball.net/2026/05/ai_is_technology_not_a_product](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

生成摘要时出错

---

## 68. The SGI Buyer's Guide (2003)

**原文标题**: The SGI Buyer's Guide (2003)

**原文链接**: [https://hardware.majix.org/computers/sgi/buyers-guide.shtml](https://hardware.majix.org/computers/sgi/buyers-guide.shtml)

生成摘要时出错

---

## 69. Don’t Outsource the Learning

**原文标题**: Don’t Outsource the Learning

**原文链接**: [https://addyosmani.com/blog/dont-outsource-learning/](https://addyosmani.com/blog/dont-outsource-learning/)

生成摘要时出错

---

## 70. How diamonds are made

**原文标题**: How diamonds are made

**原文链接**: [https://diamond.jaydip.me/](https://diamond.jaydip.me/)

生成摘要时出错

---

## 71. Zerostack – A Unix-inspired coding agent written in pure Rust

**原文标题**: Zerostack – A Unix-inspired coding agent written in pure Rust

**原文链接**: [https://crates.io/crates/zerostack/1.0.0](https://crates.io/crates/zerostack/1.0.0)

生成摘要时出错

---

## 72. VoIP brings back old-fashioned pay phones to rural Vermont (2025)

**原文标题**: VoIP brings back old-fashioned pay phones to rural Vermont (2025)

**原文链接**: [https://spectrum.ieee.org/payphone-voip](https://spectrum.ieee.org/payphone-voip)

生成摘要时出错

---

## 73. Native all the way, until you need text

**原文标题**: Native all the way, until you need text

**原文链接**: [https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/](https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/)

生成摘要时出错

---

## 74. Justice Department announces a $1.7B fund to compensate Trump allies

**原文标题**: Justice Department announces a $1.7B fund to compensate Trump allies

**原文链接**: [https://apnews.com/article/trump-lawsuit-irs-leak-3729de38770b558be01712a143437bf8](https://apnews.com/article/trump-lawsuit-irs-leak-3729de38770b558be01712a143437bf8)

生成摘要时出错

---

## 75. The Third Hard Problem

**原文标题**: The Third Hard Problem

**原文链接**: [https://mmapped.blog/posts/48-the-third-hard-problem](https://mmapped.blog/posts/48-the-third-hard-problem)

生成摘要时出错

---

## 76. The Four Horsemen of the LLM Apocalypse

**原文标题**: The Four Horsemen of the LLM Apocalypse

**原文链接**: [https://anarc.at/blog/2026-05-16-four-horsemen/](https://anarc.at/blog/2026-05-16-four-horsemen/)

生成摘要时出错

---

## 77. Where Are the Vibecoded Photoshops?

**原文标题**: Where Are the Vibecoded Photoshops?

**原文链接**: [https://indiepixel.de/blog/posts/where-are-the-vibecoded-photoshops/](https://indiepixel.de/blog/posts/where-are-the-vibecoded-photoshops/)

生成摘要时出错

---

## 78. Apple Silicon costs more than OpenRouter

**原文标题**: Apple Silicon costs more than OpenRouter

**原文链接**: [https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html](https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html)

生成摘要时出错

---

## 79. Mado: Fast Markdown linter written in Rust

**原文标题**: Mado: Fast Markdown linter written in Rust

**原文链接**: [https://github.com/akiomik/mado](https://github.com/akiomik/mado)

生成摘要时出错

---

## 80. Mercurial, 20 years and counting: how are we still alive and kicking? [video]

**原文标题**: Mercurial, 20 years and counting: how are we still alive and kicking? [video]

**原文链接**: [https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/](https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/)

生成摘要时出错

---

## 81. Illusions of understanding in the sciences

**原文标题**: Illusions of understanding in the sciences

**原文链接**: [https://link.springer.com/article/10.1007/s42113-026-00271-1](https://link.springer.com/article/10.1007/s42113-026-00271-1)

生成摘要时出错

---

## 82. CUDA Books

**原文标题**: CUDA Books

**原文链接**: [https://github.com/alternbits/awesome-cuda-books](https://github.com/alternbits/awesome-cuda-books)

生成摘要时出错

---

## 83. Where OpenClaw Security Is Heading

**原文标题**: Where OpenClaw Security Is Heading

**原文链接**: [https://openclaw.ai/blog/where-openclaw-security-is-heading](https://openclaw.ai/blog/where-openclaw-security-is-heading)

生成摘要时出错

---

## 84. Ebola outbreak with uncommon strain erupts in Congo and Uganda; 65 deaths

**原文标题**: Ebola outbreak with uncommon strain erupts in Congo and Uganda; 65 deaths

**原文链接**: [https://arstechnica.com/health/2026/05/ebola-outbreak-confirmed-in-congo-and-uganda-246-suspected-cases-65-deaths/](https://arstechnica.com/health/2026/05/ebola-outbreak-confirmed-in-congo-and-uganda-246-suspected-cases-65-deaths/)

生成摘要时出错

---

## 85. Moving away from Tailwind, and learning to structure my CSS

**原文标题**: Moving away from Tailwind, and learning to structure my CSS

**原文链接**: [https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

生成摘要时出错

---

## 86. The Rage of the Billionaires Is Coming

**原文标题**: The Rage of the Billionaires Is Coming

**原文链接**: [https://www.thebignewsletter.com/p/monopoly-round-up-the-rage-of-the](https://www.thebignewsletter.com/p/monopoly-round-up-the-rage-of-the)

生成摘要时出错

---

## 87. Supercharging Immune Cells May Help Control HIV Long-Term

**原文标题**: Supercharging Immune Cells May Help Control HIV Long-Term

**原文链接**: [https://www.wired.com/story/car-t-therapy-may-help-control-hiv-long-term/](https://www.wired.com/story/car-t-therapy-may-help-control-hiv-long-term/)

生成摘要时出错

---

## 88. RISC-V and Floating Point

**原文标题**: RISC-V and Floating Point

**原文链接**: [https://fprox.substack.com/p/risc-v-and-floating-point](https://fprox.substack.com/p/risc-v-and-floating-point)

生成摘要时出错

---

## 89. Prolog Basics Explained with Pokémon

**原文标题**: Prolog Basics Explained with Pokémon

**原文链接**: [https://unplannedobsolescence.com/blog/prolog-basics-pokemon/](https://unplannedobsolescence.com/blog/prolog-basics-pokemon/)

生成摘要时出错

---

## 90. Project Gutenberg – keeps getting better

**原文标题**: Project Gutenberg – keeps getting better

**原文链接**: [https://www.gutenberg.org/](https://www.gutenberg.org/)

生成摘要时出错

---

## 91. Fabricked: Misconfiguring Infinity Fabric to Break AMD SEV-SNP

**原文标题**: Fabricked: Misconfiguring Infinity Fabric to Break AMD SEV-SNP

**原文链接**: [https://xca-attacks.github.io/fabricked/](https://xca-attacks.github.io/fabricked/)

生成摘要时出错

---

## 92. Hindenburg’s Smoking Room

**原文标题**: Hindenburg’s Smoking Room

**原文链接**: [https://www.airships.net/hindenburg-smoking-room/](https://www.airships.net/hindenburg-smoking-room/)

生成摘要时出错

---

## 93. This ultra-lightweight Linux OS saved my Windows 10 laptop from the scrapheap

**原文标题**: This ultra-lightweight Linux OS saved my Windows 10 laptop from the scrapheap

**原文链接**: [https://www.neowin.net/editorials/this-ultra-lightweight-linux-os-just-saved-my-windows-10-laptop-from-the-scrapheap/](https://www.neowin.net/editorials/this-ultra-lightweight-linux-os-just-saved-my-windows-10-laptop-from-the-scrapheap/)

生成摘要时出错

---

## 94. Jury hands victory to Sam Altman in battle with Elon Musk over OpenAI's mission

**原文标题**: Jury hands victory to Sam Altman in battle with Elon Musk over OpenAI's mission

**原文链接**: [https://www.theguardian.com/technology/2026/may/18/sam-altman-trial-victory-elon-musk-openai](https://www.theguardian.com/technology/2026/may/18/sam-altman-trial-victory-elon-musk-openai)

生成摘要时出错

---

## 95. Most Americans don't trust AI – or the people in charge of it (2025)

**原文标题**: Most Americans don't trust AI – or the people in charge of it (2025)

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/644853/pew-gallup-data-americans-dont-trust-ai](https://www.theverge.com/ai-artificial-intelligence/644853/pew-gallup-data-americans-dont-trust-ai)

生成摘要时出错

---

## 96. I don't think AI will make your processes go faster

**原文标题**: I don't think AI will make your processes go faster

**原文链接**: [https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

生成摘要时出错

---

## 97. Reverse engineering Android malware from popular Chinese projectors

**原文标题**: Reverse engineering Android malware from popular Chinese projectors

**原文链接**: [https://zanestjohn.com/blog/reing-with-claude-code](https://zanestjohn.com/blog/reing-with-claude-code)

生成摘要时出错

---

## 98. The era of free money may have ended

**原文标题**: The era of free money may have ended

**原文链接**: [https://www.reuters.com/commentary/reuters-open-interest/g7-long-bond-stress-intensifies-2026-05-13/](https://www.reuters.com/commentary/reuters-open-interest/g7-long-bond-stress-intensifies-2026-05-13/)

生成摘要时出错

---

## 99. Roman Letters

**原文标题**: Roman Letters

**原文链接**: [https://romanletters.org/](https://romanletters.org/)

生成摘要时出错

---

## 100. The History of ThinkPad: From IBM’s Bento Box to Lenovo’s AI Workstations

**原文标题**: The History of ThinkPad: From IBM’s Bento Box to Lenovo’s AI Workstations

**原文链接**: [https://www.jdhodges.com/blog/thinkpad-history/](https://www.jdhodges.com/blog/thinkpad-history/)

生成摘要时出错

---

