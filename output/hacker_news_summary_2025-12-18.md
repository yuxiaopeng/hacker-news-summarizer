# Hacker News 热门文章摘要 (2025-12-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Gemini 3 Flash：为速度而生的前沿智能

**原文标题**: Gemini 3 Flash: Frontier intelligence built for speed

**原文链接**: [https://blog.google/products/gemini/gemini-3-flash/](https://blog.google/products/gemini/gemini-3-flash/)

2025年12月17日，谷歌宣布发布 Gemini 3 模型家族的最新成员——**Gemini 3 Flash**。该模型旨在以高速和低成本提供“前沿智能”，在具备专业级推理能力的同时，其延迟较前代产品显著降低。

**核心性能亮点：**
*   **卓越智能：** 该模型在多项基准测试中超越了 Gemini 2.5 Pro，在 GPQA Diamond（博士级推理）上得分 90.4%，在 MMMU Pro 上得分 81.2%。
*   **效率与速度：** 其运行速度比 Gemini 2.5 Pro 快 3 倍，完成任务平均可节省 30% 的 token 使用量。
*   **卓越编程：** 在 SWE-bench Verified 测试中获得 78% 的评分，在智能体编程能力上甚至超越了 Gemini 3 Pro。
*   **高性价比：** 价格设定为每 100 万输入 token 0.50 美元，每 100 万输出 token 3.00 美元。

**对用户与开发者的影响：**
*   **面向开发者：** Gemini 3 Flash 针对智能体工作流、实时多模态分析和高频编程任务进行了优化。开发者可通过 Google AI Studio 中的 Gemini API、Vertex AI 以及全新的智能体开发平台 **Google Antigravity** 调用该模型。
*   **面向普通用户：** 该模型现已成为 Gemini 应用和搜索中 AI 模式的默认模型。用户可以体验增强的多模态功能，例如实时视频分析（如高尔夫挥杆动作指导）、通过语音即时创建应用，以及根据音频录音生成测试题。

Gemini 3 Flash 目前已面向开发者和企业提供预览版，同时正在全球范围内的 Gemini 应用和搜索中逐步推出。它与 Gemini 3 Pro 及 Deep Think 共同构成了目前的下一代模型阵容。

---

## 2. 来自两栖和爬行动物的肠道细菌可消除小鼠体内的肿瘤。

**原文标题**: Gut bacteria from amphibians and reptiles achieve tumor elimination in mice

**原文链接**: [https://www.jaist.ac.jp/english/whatsnew/press/2025/12/17-1.html](https://www.jaist.ac.jp/english/whatsnew/press/2025/12/17-1.html)

日本北陆先端科学技术大学院大学（JAIST）由Eijiro Miyako教授领导的研究团队发现了一种突破性的癌症治疗方法，该方法利用了从两栖动物和爬行动物肠道中分离出的细菌。这项发表在《肠道微生物》（*Gut Microbes*）杂志上的研究指出，源自日本树蛙的美洲尤文氏菌（*Ewingella americana*）是一种极其强效的抗癌剂。

在结直肠癌小鼠模型中，仅需单次静脉注射美洲尤文氏菌，即可实现100%的完全缓解率，其疗效显著优于标准化学疗法（阿霉素）和免疫疗法（抗PD-L1）。该细菌利用独特的双重作用机制发挥药效：
1. **直接细胞毒性：** 作为一种兼性厌氧菌，它能选择性地定植在肿瘤的缺氧及免疫抑制环境中，并在24小时内繁殖3000倍，从而直接摧毁癌细胞。
2. **免疫激活：** 它的存在会引发T细胞、B细胞和中性粒细胞的大规模招募，同时刺激促炎细胞因子（TNF-α和IFN-γ）的产生，以进一步攻击肿瘤。

该疗法的一个核心亮点是其卓越的安全性。基于肿瘤独特的血管和代谢特征，这些细菌仅在癌组织中聚集，而在肝脏或肺部等健康器官中完全没有定植。细菌在24小时内即可从血液中清除，仅引起短暂、轻微的炎症，且无慢性毒性。

这项研究为利用天然、非工程化细菌作为“活体药物”建立了概念验证。未来的研究将致力于将该疗法扩展到其他难治性恶性肿瘤（如胰腺癌和乳腺癌），并优化给药方法。研究结果表明，尚未开发的生物多样性在下一代肿瘤治疗中蕴藏着巨大的潜力。

---

## 3. OBS Studio 迎来全新渲染器

**原文标题**: OBS Studio Gets a New Renderer

**原文链接**: [https://obsproject.com/blog/obs-studio-gets-a-new-renderer](https://obsproject.com/blog/obs-studio-gets-a-new-renderer)

OBS Studio 32.0.0 为 macOS 引入了实验性的 Metal 图形 API 渲染器，旨在最终取代旧有的 OpenGL 后端。此次更新旨在通过利用现代 GPU 架构，解锁更高的性能并降低开销。

向 Metal 的过渡面临着重大的技术挑战，因为 OBS Studio 的核心渲染器最初是仿照 Direct3D 等旧版 API 构建的。旧版 API 会自动处理资源管理和同步，而 Metal 等现代 API 则要求应用程序手动管理这些任务。为了避免彻底重写 OBS 核心，开发人员直接在新的 Metal 后端中实现了这些管理职责。

其中一个主要的障碍涉及**着色器转译 (Shader Transpilation)**。OBS 使用的是一种较旧的 HLSL（高级着色器语言）方言，必须在运行时将其转换为 Metal 着色语言 (MSL)。这一过程非常复杂，原因如下：
*   **更严格的类型定义：** MSL 要求输入和输出使用独立的结构体，而 HLSL 仅使用一个。后端必须扫描并相应地拆分这些结构。
*   **无全局变量：** 与 HLSL 或 OpenGL 不同，MSL 不支持全局“uniform”变量。转译器必须重写每个着色器函数，以显式地将这些数据作为参数传递，这实际上重构了应用程序中每个特效文件的代码。

目前，由于存在已知问题且缺乏大规模测试，Metal 后端被标记为“实验性”。虽然 OpenGL 目前仍是默认选项，但开发人员正邀请用户和有经验的 Metal 开发者测试新系统并提供反馈。本文是详细介绍 OBS 渲染引擎演进系列文章的第一篇。

---

## 4. 我的支付代理名叫 George，而不是 stripe-agent。

**原文标题**: My payment agent is named George, not stripe-agent

**原文链接**: [https://blog.kestrelsnest.social/posts/2025-12-14-why-my-payment-agent-is-named-george-not-stripe-agent/](https://blog.kestrelsnest.social/posts/2025-12-14-why-my-payment-agent-is-named-george-not-stripe-agent/)

在这篇文章中，一位资深开发者反对科技行业过度使用功能化术语来剥离人性的倾向。作者没有将AI子代理命名为“stripe-agent”或“security-checker”等技术化标签，而是以体现特定价值观的历史人物为其命名：负责支付的叫“乔治”（华盛顿·卡弗），负责设计的叫“瑞”（伊姆斯），负责安全审计的叫“阿加莎”（克里斯蒂），负责无障碍化的则叫“海伦”（凯勒）。

这种做法被称为“意图仪式”，旨在对抗将用户简化为“日活（MAU）”或“转化率”等数据指标的非人化趋向。通过援引“乔治”，作者会提醒自己构建可持续且资源丰富的系统；通过召唤“阿加莎”，他会代入侦探思维去挖掘隐藏的漏洞。这些名字充当了心理框架，在工作开始前便塑造了开发者的思考方式，确保软件是为了服务人类需求，而非仅仅追求技术基准。

作者强调，在他四十年的职业生涯中，软件始终是为生物学家、农民等不同群体解决现实问题的媒介。以那些激励人心的人物来命名工具，创造出了一种“价值观的合奏”，让不同的视角相互叠加以完善产品。例如，通过为海伦·凯勒设立专属代理，作者发现了一些通用设计代理所忽略的无障碍缺陷。

文章最终指出，尽管AI工具并不具备人格，但我们赋予它们的名字决定了我们对自身工作的要求标准。通过将工具人格化，作者确保他的代码始终处于为人服务的状态，并以此提醒自己：软件只是手段，而非目的。

---

## 5. Coursera 将与 Udemy 合并

**原文标题**: Coursera to combine with Udemy

**原文链接**: [https://investor.coursera.com/news/news-details/2025/Coursera-to-Combine-with-Udemy-to-Empower-the-Global-Workforce-with-Skills-for-the-AI-Era/default.aspx](https://investor.coursera.com/news/news-details/2025/Coursera-to-Combine-with-Udemy-to-Empower-the-Global-Workforce-with-Skills-for-the-AI-Era/default.aspx)

Coursera 与 Udemy 宣布达成最终协议，将通过全股票交易进行合并，打造在线学习与技能发展领域的全球领导者。此次合并旨在通过整合两大平台的独特优势，应对“AI 时代”下劳动力技能提升的迫切需求。

**合并要点：**

*   **战略目标：** 此次合并旨在通过将 Coursera 的学术及专业证书认证与 Udemy 庞大且灵活的技能市场相结合，为全球劳动力赋能。其目标是为学习者、企业和政府提供“一站式”服务。
*   **规模与影响力：** 合并后的公司将服务超过 2 亿名学习者，以及逾 16,000 家企业、政府和校园客户。它将提供海量的内容库，包含来自 77,000 名专家讲师以及 325 多家领先大学和行业合作伙伴的 220,000 多门课程。
*   **AI 整合：** 新实体计划加速对 AI 驱动工具（如个性化学习助手和自动化课程映射）的投资，以帮助各机构更高效地填补技能缺口。
*   **领导层：** Coursera 现任首席执行官 Jeff Maggioncalda 将领导合并后的公司。Udemy 首席执行官 Greg Brown 预计将加入董事会。
*   **财务协同效应：** 两家公司预计在交易完成后两年内，主要通过优化营销支出和提升企业运营效率，每年实现超过 1.5 亿美元的成本协同效应。
*   **时间表：** 在获得监管批准和双方股东同意的前提下，该交易预计将于 2025 年初完成。

此次合并代表了教育科技（EdTech）行业的重大整合，使合并后的实体成为全球终身学习和职业发展领域的主导力量。

---

## 6. 解释美国中年死亡率日益扩大的差距：是否存在确凿证据？

**原文标题**: Explaining the Widening Divides in US Midlife Mortality: Is There a Smoking Gun?

**原文链接**: [https://www.nber.org/papers/w34553](https://www.nber.org/papers/w34553)

在NBER工作论文《解释美国中年死亡率差距的扩大：是否存在“确凿证据”？》中，Christopher L. Foote及其同事研究了1992年至2019年间美国死亡率不平等的剧增现象。在此期间，大学毕业生与无学位者之间的预期寿命差距增加了一倍以上，从2.6年扩大到6.3年。同时，县域间的死亡率不平等程度上升了30%，且日益严重的农村健康劣势进一步加剧了这一趋势。

作者指出，受教育程度驱动了地理死亡率模式的根本转变。研究结果揭示了“两个美国”的故事：
1.  **大学毕业生：** 该群体的死亡率大幅下降，地理不平等程度降低，这意味着全美范围内的健康结果不仅得到了改善，而且趋于一致。
2.  **非大学毕业生：** 该群体呈现出截然相反的趋势，死亡率上升且空间不平等加剧，这意味着对于没有学位的人来说，居住地对生存率的影响显著增强。

研究确认**吸烟率**是解释这三种趋势的主要“确凿证据”。虽然收入、州政策和其他健康行为起到了次要作用，但烟草使用的差异是导致差距扩大的首要原因。尽管有此发现，作者指出仍有一个谜团待解：目前尚不完全清楚，为什么“地方效应”（即个人局部环境的具体影响）对非大学毕业生的吸烟习惯和死亡率的影响，会比对大学毕业生的影响大得多。

---

## 7. TikTok非法追踪购物习惯和约会软件的使用？

**原文标题**: TikTok unlawfully tracks shopping habits and use of dating apps?

**原文链接**: [https://noyb.eu/en/tiktok-unlawfully-tracks-your-shopping-habits-and-your-use-dating-apps](https://noyb.eu/en/tiktok-unlawfully-tracks-your-shopping-habits-and-your-use-dating-apps)

隐私保护组织 **noyb** 已向奥地利数据保护局 (DSB) 对 **TikTok**、社交应用 **Grindr** 以及追踪公司 **AppsFlyer** 提起两项正式投诉。投诉的核心在于非法的跨应用追踪以及系统性地向用户隐瞒个人数据。

主要指控包括：

*   **非法跨应用追踪：** TikTok 被指控在缺乏有效法律依据的情况下，跨第三方网站和应用追踪用户。具体而言，一名用户通过数据访问请求发现，他在 Grindr 的使用记录通过 AppsFlyer 被分享给了 TikTok。这使得 TikTok 能够推断出涉及其性取向的敏感信息，而此类信息受到 GDPR 第 9 条的严格保护。
*   **未经同意共享数据：** 投诉称，Grindr 和 AppsFlyer 在未经用户同意且缺乏 GDPR 第 6 条规定的有效法律依据的情况下，与 TikTok 共享了这些敏感数据。据报道，AppsFlyer 充当了中间商，协助数据从第三方应用流向 TikTok。
*   **阻碍数据访问权：** TikTok 被指控违反了 GDPR 第 12 条和第 15 条，未能向用户提供其个人数据的完整副本。尽管 TikTok 提供了一个“下载工具”，但 noyb 声称该工具是刻意不完整的，仅提供 TikTok 认为“相关”的内容，而非所有被处理的数据。投诉人在经过反复且持续的查询后，才最终获得了完全的透明度。

**诉求行动：**
noyb 已要求奥地利当局命令相关公司停止非法处理行为并实现完整的数据透明。此外，他们还呼吁根据 GDPR 第 83 条处以“有效、适度且具有威慑力”的罚款，以防止未来的违规行为。

---

## 8. AWS CEO says replacing junior devs with AI is 'one of the dumbest ideas'

**原文标题**: AWS CEO says replacing junior devs with AI is 'one of the dumbest ideas'

**原文链接**: [https://www.finalroundai.com/blog/aws-ceo-ai-cannot-replace-junior-developers](https://www.finalroundai.com/blog/aws-ceo-ai-cannot-replace-junior-developers)

生成摘要时出错

---

## 9. I got hacked: My Hetzner server started mining Monero

**原文标题**: I got hacked: My Hetzner server started mining Monero

**原文链接**: [https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/](https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/)

生成摘要时出错

---

## 10. Show HN: High-Performance Wavelet Matrix for Python, Implemented in Rust

**原文标题**: Show HN: High-Performance Wavelet Matrix for Python, Implemented in Rust

**原文链接**: [https://pypi.org/project/wavelet-matrix/](https://pypi.org/project/wavelet-matrix/)

生成摘要时出错

---

## 11. Inside PostHog: SSRF, ClickHouse SQL Escape and Default Postgres Creds to RCE

**原文标题**: Inside PostHog: SSRF, ClickHouse SQL Escape and Default Postgres Creds to RCE

**原文链接**: [https://mdisec.com/inside-posthog-how-ssrf-a-clickhouse-sql-escaping-0day-and-default-postgresql-credentials-formed-an-rce-chain-zdi-25-099-zdi-25-097-zdi-25-096/](https://mdisec.com/inside-posthog-how-ssrf-a-clickhouse-sql-escaping-0day-and-default-postgresql-credentials-formed-an-rce-chain-zdi-25-099-zdi-25-097-zdi-25-096/)

生成摘要时出错

---

## 12. A Safer Container Ecosystem with Docker: Free Docker Hardened Images

**原文标题**: A Safer Container Ecosystem with Docker: Free Docker Hardened Images

**原文链接**: [https://www.docker.com/blog/docker-hardened-images-for-every-developer/](https://www.docker.com/blog/docker-hardened-images-for-every-developer/)

生成摘要时出错

---

## 13. The Number That Turned Sideways

**原文标题**: The Number That Turned Sideways

**原文链接**: [https://zuriby.github.io/math.github.io/the-number-that-turned-sideways.html](https://zuriby.github.io/math.github.io/the-number-that-turned-sideways.html)

生成摘要时出错

---

## 14. Developers can now submit apps to ChatGPT

**原文标题**: Developers can now submit apps to ChatGPT

**原文链接**: [https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/)

生成摘要时出错

---

## 15. Fast SEQUENCE iteration in Common Lisp

**原文标题**: Fast SEQUENCE iteration in Common Lisp

**原文链接**: [https://world-playground-deceit.net/blog/2025/12/fast-sequence-iteration-in-common-lisp.html](https://world-playground-deceit.net/blog/2025/12/fast-sequence-iteration-in-common-lisp.html)

生成摘要时出错

---

## 16. Cloudflare Radar 2025 Year in Review

**原文标题**: Cloudflare Radar 2025 Year in Review

**原文链接**: [https://radar.cloudflare.com/year-in-review/2025](https://radar.cloudflare.com/year-in-review/2025)

生成摘要时出错

---

## 17. Zmij: Faster floating point double-to-string conversion

**原文标题**: Zmij: Faster floating point double-to-string conversion

**原文链接**: [https://vitaut.net/posts/2025/faster-dtoa/](https://vitaut.net/posts/2025/faster-dtoa/)

生成摘要时出错

---

## 18. Working quickly is more important than it seems (2015)

**原文标题**: Working quickly is more important than it seems (2015)

**原文链接**: [https://jsomers.net/blog/speed-matters](https://jsomers.net/blog/speed-matters)

生成摘要时出错

---

## 19. How SQLite is tested

**原文标题**: How SQLite is tested

**原文链接**: [https://sqlite.org/testing.html](https://sqlite.org/testing.html)

生成摘要时出错

---

## 20. A Cosmic Offense: Elias Canetti's contest against death

**原文标题**: A Cosmic Offense: Elias Canetti's contest against death

**原文链接**: [https://www.commonwealmagazine.org/cosmic-offense](https://www.commonwealmagazine.org/cosmic-offense)

生成摘要时出错

---

## 21. Pornhub extorted after hackers steal Premium member activity data

**原文标题**: Pornhub extorted after hackers steal Premium member activity data

**原文链接**: [https://www.bleepingcomputer.com/news/security/pornhub-extorted-after-hackers-steal-premium-member-activity-data/](https://www.bleepingcomputer.com/news/security/pornhub-extorted-after-hackers-steal-premium-member-activity-data/)

生成摘要时出错

---

## 22. Flick (YC F25) Is Hiring Founding Engineer to Build Figma for AI Filmmaking

**原文标题**: Flick (YC F25) Is Hiring Founding Engineer to Build Figma for AI Filmmaking

**原文链接**: [https://www.ycombinator.com/companies/flick/jobs/Tdu6FH6-founding-frontend-engineer](https://www.ycombinator.com/companies/flick/jobs/Tdu6FH6-founding-frontend-engineer)

生成摘要时出错

---

## 23. A16z-backed Doublespeed hacked, revealing what its AI-generated accounts promote

**原文标题**: A16z-backed Doublespeed hacked, revealing what its AI-generated accounts promote

**原文链接**: [https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/](https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/)

生成摘要时出错

---

## 24. Learning Fortran (2024)

**原文标题**: Learning Fortran (2024)

**原文链接**: [https://uncenter.dev/posts/learning-fortran/](https://uncenter.dev/posts/learning-fortran/)

生成摘要时出错

---

## 25. I created a publishing system for step-by-step coding guides in Typst

**原文标题**: I created a publishing system for step-by-step coding guides in Typst

**原文链接**: [https://press.knowledge.dev/p/new-150-pages-rust-guide-create-a](https://press.knowledge.dev/p/new-150-pages-rust-guide-create-a)

生成摘要时出错

---

## 26. Thin desires are eating life

**原文标题**: Thin desires are eating life

**原文链接**: [https://www.joanwestenberg.com/thin-desires-are-eating-your-life/](https://www.joanwestenberg.com/thin-desires-are-eating-your-life/)

生成摘要时出错

---

## 27. Is Mozilla trying hard to kill itself?

**原文标题**: Is Mozilla trying hard to kill itself?

**原文链接**: [https://infosec.press/brunomiguel/is-mozilla-trying-hard-to-kill-itself](https://infosec.press/brunomiguel/is-mozilla-trying-hard-to-kill-itself)

生成摘要时出错

---

## 28. I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in hours

**原文标题**: I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in hours

**原文链接**: [https://simonwillison.net/2025/Dec/15/porting-justhtml/](https://simonwillison.net/2025/Dec/15/porting-justhtml/)

生成摘要时出错

---

## 29. TLA+ Modeling Tips

**原文标题**: TLA+ Modeling Tips

**原文链接**: [http://muratbuffalo.blogspot.com/2025/12/tla-modeling-tips.html](http://muratbuffalo.blogspot.com/2025/12/tla-modeling-tips.html)

生成摘要时出错

---

## 30. Show HN: GitForms – Zero-cost contact forms using GitHub Issues as database

**原文标题**: Show HN: GitForms – Zero-cost contact forms using GitHub Issues as database

**原文链接**: [https://gitforms-landing.vercel.app/](https://gitforms-landing.vercel.app/)

生成摘要时出错

---

## 31. The State of AI Coding Report 2025

**原文标题**: The State of AI Coding Report 2025

**原文链接**: [https://www.greptile.com/state-of-ai-coding-2025](https://www.greptile.com/state-of-ai-coding-2025)

生成摘要时出错

---

## 32. AI will make formal verification go mainstream

**原文标题**: AI will make formal verification go mainstream

**原文链接**: [https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html](https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html)

生成摘要时出错

---

## 33. A look back: LANPAR, the first spreadsheet

**原文标题**: A look back: LANPAR, the first spreadsheet

**原文链接**: [https://technicallywewrite.com/2025/12/16/lanpar](https://technicallywewrite.com/2025/12/16/lanpar)

生成摘要时出错

---

## 34. I couldn't find a logging library that worked for my library, so I made one

**原文标题**: I couldn't find a logging library that worked for my library, so I made one

**原文链接**: [https://hackers.pub/@hongminhee/2025/logtape-fedify-case-study](https://hackers.pub/@hongminhee/2025/logtape-fedify-case-study)

生成摘要时出错

---

## 35. AI's real superpower: consuming, not creating

**原文标题**: AI's real superpower: consuming, not creating

**原文链接**: [https://msanroman.io/blog/ai-consumption-paradigm](https://msanroman.io/blog/ai-consumption-paradigm)

生成摘要时出错

---

## 36. alpr.watch

**原文标题**: alpr.watch

**原文链接**: [https://alpr.watch/](https://alpr.watch/)

生成摘要时出错

---

## 37. Modern SID chip substitutes [video]

**原文标题**: Modern SID chip substitutes [video]

**原文链接**: [https://www.youtube.com/watch?v=nooPmXxO6K0](https://www.youtube.com/watch?v=nooPmXxO6K0)

生成摘要时出错

---

## 38. Japan to revise romanization rules for first time in 70 years

**原文标题**: Japan to revise romanization rules for first time in 70 years

**原文链接**: [https://www.japantimes.co.jp/news/2025/08/21/japan/panel-hepburn-style-romanization/](https://www.japantimes.co.jp/news/2025/08/21/japan/panel-hepburn-style-romanization/)

生成摘要时出错

---

## 39. Announcing the Beta release of ty

**原文标题**: Announcing the Beta release of ty

**原文链接**: [https://astral.sh/blog/ty](https://astral.sh/blog/ty)

生成摘要时出错

---

## 40. Venezuela's Navy Begins Escorting Ships as U.S. Threatens Blockade

**原文标题**: Venezuela's Navy Begins Escorting Ships as U.S. Threatens Blockade

**原文链接**: [https://www.nytimes.com/live/2025/12/17/us/trump-news](https://www.nytimes.com/live/2025/12/17/us/trump-news)

生成摘要时出错

---

## 41. No Graphics API

**原文标题**: No Graphics API

**原文链接**: [https://www.sebastianaaltonen.com/blog/no-graphics-api](https://www.sebastianaaltonen.com/blog/no-graphics-api)

生成摘要时出错

---

## 42. AI Isn't Just Spying on You. It's Tricking You into Spending More

**原文标题**: AI Isn't Just Spying on You. It's Tricking You into Spending More

**原文链接**: [https://newrepublic.com/article/204525/artificial-intelligence-consumers-data-dynamic-pricing](https://newrepublic.com/article/204525/artificial-intelligence-consumers-data-dynamic-pricing)

生成摘要时出错

---

## 43. The US govt has revoked the non-immigrant visa of Nobel laureate Wole Soyinka [video]

**原文标题**: The US govt has revoked the non-immigrant visa of Nobel laureate Wole Soyinka [video]

**原文链接**: [https://www.youtube.com/watch?v=ple4xophXfM](https://www.youtube.com/watch?v=ple4xophXfM)

生成摘要时出错

---

## 44. VRChat: “There are more Japanese creators than all other countries combined”

**原文标题**: VRChat: “There are more Japanese creators than all other countries combined”

**原文链接**: [https://twitter.com/chyadosensei/status/2001356290531156159](https://twitter.com/chyadosensei/status/2001356290531156159)

生成摘要时出错

---

## 45. US admits liability in helicopter collision with American jet that killed 67

**原文标题**: US admits liability in helicopter collision with American jet that killed 67

**原文链接**: [https://www.cnbc.com/2025/12/17/us-army-helicopter-collision-american-airlines-jet.html](https://www.cnbc.com/2025/12/17/us-army-helicopter-collision-american-airlines-jet.html)

生成摘要时出错

---

## 46. Introduction to Software Development Tooling (2024)

**原文标题**: Introduction to Software Development Tooling (2024)

**原文链接**: [https://bernsteinbear.com/isdt/](https://bernsteinbear.com/isdt/)

生成摘要时出错

---

## 47. UNC System President Peter Hans confirms all syllabuses will be public records

**原文标题**: UNC System President Peter Hans confirms all syllabuses will be public records

**原文链接**: [https://dailytarheel.com/article/university-peter-hans-syllabi-policy-confirmation-breaking-20251211](https://dailytarheel.com/article/university-peter-hans-syllabi-policy-confirmation-breaking-20251211)

生成摘要时出错

---

## 48. The World Happiness Report is beset with methodological problems

**原文标题**: The World Happiness Report is beset with methodological problems

**原文链接**: [https://yaschamounk.substack.com/p/the-world-happiness-report-is-a-sham](https://yaschamounk.substack.com/p/the-world-happiness-report-is-a-sham)

生成摘要时出错

---

## 49. Nvidia Nemotron 3 Family of Models

**原文标题**: Nvidia Nemotron 3 Family of Models

**原文链接**: [https://research.nvidia.com/labs/nemotron/Nemotron-3/](https://research.nvidia.com/labs/nemotron/Nemotron-3/)

生成摘要时出错

---

## 50. Semiquincentennial $1 Coin Candidate Designs

**原文标题**: Semiquincentennial $1 Coin Candidate Designs

**原文链接**: [https://www.usmint.gov/news/media-kit/semiq-dollar-coin](https://www.usmint.gov/news/media-kit/semiq-dollar-coin)

生成摘要时出错

---

## 51. No AI* Here – A Response to Mozilla's Next Chapter

**原文标题**: No AI* Here – A Response to Mozilla's Next Chapter

**原文链接**: [https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/](https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/)

生成摘要时出错

---

## 52. OpenAI Is Maneuvering for a Government Bailout

**原文标题**: OpenAI Is Maneuvering for a Government Bailout

**原文链接**: [https://prospect.org/2025/11/07/openai-maneuvering-for-government-bailout/](https://prospect.org/2025/11/07/openai-maneuvering-for-government-bailout/)

生成摘要时出错

---

## 53. GitHub postponing the announced billing change for self-hosted GitHub Actions

**原文标题**: GitHub postponing the announced billing change for self-hosted GitHub Actions

**原文链接**: [https://twitter.com/jaredpalmer/status/2001373329811181846](https://twitter.com/jaredpalmer/status/2001373329811181846)

生成摘要时出错

---

## 54. Pricing Changes for GitHub Actions

**原文标题**: Pricing Changes for GitHub Actions

**原文链接**: [https://resources.github.com/actions/2026-pricing-changes-for-github-actions/](https://resources.github.com/actions/2026-pricing-changes-for-github-actions/)

生成摘要时出错

---

## 55. AI capability isn't humanness

**原文标题**: AI capability isn't humanness

**原文链接**: [https://research.roundtable.ai/capabilities-humanness/](https://research.roundtable.ai/capabilities-humanness/)

生成摘要时出错

---

## 56. GPT Image 1.5

**原文标题**: GPT Image 1.5

**原文链接**: [https://openai.com/index/new-chatgpt-images-is-here/](https://openai.com/index/new-chatgpt-images-is-here/)

生成摘要时出错

---

## 57. Show HN: Minimal DL library in C – 24 NAIVE CUDA/CPU ops, autodiff, Python API

**原文标题**: Show HN: Minimal DL library in C – 24 NAIVE CUDA/CPU ops, autodiff, Python API

**原文链接**: [https://github.com/IaroslavElistratov/ml-systems-course](https://github.com/IaroslavElistratov/ml-systems-course)

生成摘要时出错

---

## 58. Show HN: Sqlit – A lazygit-style TUI for SQL databases

**原文标题**: Show HN: Sqlit – A lazygit-style TUI for SQL databases

**原文链接**: [https://github.com/Maxteabag/sqlit](https://github.com/Maxteabag/sqlit)

生成摘要时出错

---

## 59. Dafny: Verification-Aware Programming Language

**原文标题**: Dafny: Verification-Aware Programming Language

**原文链接**: [https://dafny.org/](https://dafny.org/)

生成摘要时出错

---

## 60. 30 years of <br> tags

**原文标题**: 30 years of <br> tags

**原文链接**: [https://www.artmann.co/articles/30-years-of-br-tags](https://www.artmann.co/articles/30-years-of-br-tags)

生成摘要时出错

---

## 61. Full Unicode Search at 50× ICU Speed with AVX‑512

**原文标题**: Full Unicode Search at 50× ICU Speed with AVX‑512

**原文链接**: [https://ashvardanian.com/posts/search-utf8/](https://ashvardanian.com/posts/search-utf8/)

生成摘要时出错

---

## 62. Mozilla appoints new CEO Anthony Enzor-Demeo

**原文标题**: Mozilla appoints new CEO Anthony Enzor-Demeo

**原文链接**: [https://blog.mozilla.org/en/mozilla/leadership/mozillas-next-chapter-anthony-enzor-demeo-new-ceo/](https://blog.mozilla.org/en/mozilla/leadership/mozillas-next-chapter-anthony-enzor-demeo-new-ceo/)

生成摘要时出错

---

## 63. Rust GCC backend: Why and how

**原文标题**: Rust GCC backend: Why and how

**原文链接**: [https://blog.guillaume-gomez.fr/articles/2025-12-15+Rust+GCC+backend%3A+Why+and+how](https://blog.guillaume-gomez.fr/articles/2025-12-15+Rust+GCC+backend%3A+Why+and+how)

生成摘要时出错

---

## 64. 40 percent of fMRI signals do not correspond to actual brain activity

**原文标题**: 40 percent of fMRI signals do not correspond to actual brain activity

**原文链接**: [https://www.tum.de/en/news-and-events/all-news/press-releases/details/40-percent-of-mri-signals-do-not-correspond-to-actual-brain-activity](https://www.tum.de/en/news-and-events/all-news/press-releases/details/40-percent-of-mri-signals-do-not-correspond-to-actual-brain-activity)

生成摘要时出错

---

## 65. P: Formal Modeling and Analysis of Distributed (Event-Driven) Systems

**原文标题**: P: Formal Modeling and Analysis of Distributed (Event-Driven) Systems

**原文链接**: [https://github.com/p-org/P](https://github.com/p-org/P)

生成摘要时出错

---

## 66. Living Particle System

**原文标题**: Living Particle System

**原文链接**: [https://creative-art-points.vercel.app/](https://creative-art-points.vercel.app/)

生成摘要时出错

---

## 67. Purrtran – ᓚᘏᗢ – A Programming Language for Cat People

**原文标题**: Purrtran – ᓚᘏᗢ – A Programming Language for Cat People

**原文链接**: [https://github.com/cmontella/purrtran](https://github.com/cmontella/purrtran)

生成摘要时出错

---

## 68. Testing a cheaper laminar flow hood

**原文标题**: Testing a cheaper laminar flow hood

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/testing-a-cheaper-laminar-flow-hood](https://chillphysicsenjoyer.substack.com/p/testing-a-cheaper-laminar-flow-hood)

生成摘要时出错

---

## 69. Bonsai: A Voxel Engine, from scratch

**原文标题**: Bonsai: A Voxel Engine, from scratch

**原文链接**: [https://github.com/scallyw4g/bonsai](https://github.com/scallyw4g/bonsai)

生成摘要时出错

---

## 70. Writing a blatant Telegram clone using Qt, QML and Rust. And C++

**原文标题**: Writing a blatant Telegram clone using Qt, QML and Rust. And C++

**原文链接**: [https://kemble.net/blog/provoke/](https://kemble.net/blog/provoke/)

生成摘要时出错

---

## 71. Pizlix: Memory Safe Linux from Scratch

**原文标题**: Pizlix: Memory Safe Linux from Scratch

**原文链接**: [https://fil-c.org/pizlix](https://fil-c.org/pizlix)

生成摘要时出错

---

## 72. Chat-tails: Throwback terminal chat, built on Tailscale

**原文标题**: Chat-tails: Throwback terminal chat, built on Tailscale

**原文链接**: [https://tailscale.com/blog/chat-tails-terminal-chat](https://tailscale.com/blog/chat-tails-terminal-chat)

生成摘要时出错

---

## 73. Playing Santa changed Bob Rutan profoundly

**原文标题**: Playing Santa changed Bob Rutan profoundly

**原文链接**: [https://www.esquire.com/lifestyle/a69597294/santaland-bob-rutan/](https://www.esquire.com/lifestyle/a69597294/santaland-bob-rutan/)

生成摘要时出错

---

## 74. Nvidia 800 Gbps ConnectX-8 SuperNIC

**原文标题**: Nvidia 800 Gbps ConnectX-8 SuperNIC

**原文链接**: [https://www.servethehome.com/nvidia-connectx-8-dual-400gbe-400g-nic-review/3/](https://www.servethehome.com/nvidia-connectx-8-dual-400gbe-400g-nic-review/3/)

生成摘要时出错

---

## 75. Nvidia plans heavy cuts to GPU supply in early 2026

**原文标题**: Nvidia plans heavy cuts to GPU supply in early 2026

**原文链接**: [https://overclock3d.net/news/gpu-displays/nvidia-plans-heavy-cuts-to-gpu-supply-in-early-2026/](https://overclock3d.net/news/gpu-displays/nvidia-plans-heavy-cuts-to-gpu-supply-in-early-2026/)

生成摘要时出错

---

## 76. Browser 'privacy' extensions have eye on your AI, log all your chats

**原文标题**: Browser 'privacy' extensions have eye on your AI, log all your chats

**原文链接**: [https://www.theregister.com/2025/12/16/chrome_edge_privacy_extensions_quietly/](https://www.theregister.com/2025/12/16/chrome_edge_privacy_extensions_quietly/)

生成摘要时出错

---

## 77. The biggest heat pumps

**原文标题**: The biggest heat pumps

**原文链接**: [https://www.bbc.com/news/articles/c17p44w87rno](https://www.bbc.com/news/articles/c17p44w87rno)

生成摘要时出错

---

## 78. Short-Circuiting Correlated Subqueries in SQLite

**原文标题**: Short-Circuiting Correlated Subqueries in SQLite

**原文链接**: [https://emschwartz.me/short-circuiting-correlated-subqueries-in-sqlite/](https://emschwartz.me/short-circuiting-correlated-subqueries-in-sqlite/)

生成摘要时出错

---

## 79. A2UI: A Protocol for Agent-Driven Interfaces

**原文标题**: A2UI: A Protocol for Agent-Driven Interfaces

**原文链接**: [https://a2ui.org/](https://a2ui.org/)

生成摘要时出错

---

## 80. FVWM-95 (2001)

**原文标题**: FVWM-95 (2001)

**原文链接**: [https://fvwm95.sourceforge.net/](https://fvwm95.sourceforge.net/)

生成摘要时出错

---

## 81. Various locale mismatch scenarios in Windows clipboard text format synthesis

**原文标题**: Various locale mismatch scenarios in Windows clipboard text format synthesis

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20251211-37/?p=111858](https://devblogs.microsoft.com/oldnewthing/20251211-37/?p=111858)

生成摘要时出错

---

## 82. Canada's Carney called out for 'utilizing' British spelling

**原文标题**: Canada's Carney called out for 'utilizing' British spelling

**原文链接**: [https://www.bbc.com/news/articles/cj69d89l8l5o](https://www.bbc.com/news/articles/cj69d89l8l5o)

生成摘要时出错

---

## 83. Overconsumption is a spiritual problem

**原文标题**: Overconsumption is a spiritual problem

**原文链接**: [https://www.sherryning.com/p/youre-overspending-because-you-lack-values](https://www.sherryning.com/p/youre-overspending-because-you-lack-values)

生成摘要时出错

---

## 84. A brief history of Times New Roman

**原文标题**: A brief history of Times New Roman

**原文链接**: [https://typographyforlawyers.com/a-brief-history-of-times-new-roman.html](https://typographyforlawyers.com/a-brief-history-of-times-new-roman.html)

生成摘要时出错

---

## 85. A Guide to Magnetizing N48 Magnets in Ansys Maxwell

**原文标题**: A Guide to Magnetizing N48 Magnets in Ansys Maxwell

**原文链接**: [https://blog.ozeninc.com/resources/from-datasheet-to-demagnetization-a-guide-to-magnetizing-n48-magnets-in-ansys-maxwell](https://blog.ozeninc.com/resources/from-datasheet-to-demagnetization-a-guide-to-magnetizing-n48-magnets-in-ansys-maxwell)

生成摘要时出错

---

## 86. ArkhamMirror: Airgapped investigation platform with CIA-style hypothesis testing

**原文标题**: ArkhamMirror: Airgapped investigation platform with CIA-style hypothesis testing

**原文链接**: [https://github.com/mantisfury/ArkhamMirror](https://github.com/mantisfury/ArkhamMirror)

生成摘要时出错

---

## 87. FCC chair suggests agency isn't independent, word cut from mission statement

**原文标题**: FCC chair suggests agency isn't independent, word cut from mission statement

**原文链接**: [https://www.axios.com/2025/12/17/brendan-carr-fcc-independent-senate-testimony-website](https://www.axios.com/2025/12/17/brendan-carr-fcc-independent-senate-testimony-website)

生成摘要时出错

---

## 88. Creating custom yellow handshake emojis with zero-width joiners

**原文标题**: Creating custom yellow handshake emojis with zero-width joiners

**原文链接**: [https://blog.alexbeals.com/posts/custom-yellow-handshake-emojis-with-zero-width-joiners](https://blog.alexbeals.com/posts/custom-yellow-handshake-emojis-with-zero-width-joiners)

生成摘要时出错

---

## 89. Sega Channel: VGHF Recovers over 100 Sega Channel ROMs (and More)

**原文标题**: Sega Channel: VGHF Recovers over 100 Sega Channel ROMs (and More)

**原文链接**: [https://gamehistory.org/segachannel/](https://gamehistory.org/segachannel/)

生成摘要时出错

---

## 90. Annual Production of 1/72 (22mm) scale plastic soldiers, 1958-2025

**原文标题**: Annual Production of 1/72 (22mm) scale plastic soldiers, 1958-2025

**原文链接**: [https://plasticsoldierreview.com/ShowFeature.aspx?id=27](https://plasticsoldierreview.com/ShowFeature.aspx?id=27)

生成摘要时出错

---

## 91. SHARP, an approach to photorealistic view synthesis from a single image

**原文标题**: SHARP, an approach to photorealistic view synthesis from a single image

**原文链接**: [https://apple.github.io/ml-sharp/](https://apple.github.io/ml-sharp/)

生成摘要时出错

---

## 92. Show HN: Interactive Common Lisp: An Enhanced REPL

**原文标题**: Show HN: Interactive Common Lisp: An Enhanced REPL

**原文链接**: [https://github.com/atgreen/icl](https://github.com/atgreen/icl)

生成摘要时出错

---

## 93. Reverse-engineering the RK3588 NPU: Hacking limits to run vision transformers

**原文标题**: Reverse-engineering the RK3588 NPU: Hacking limits to run vision transformers

**原文链接**: [https://amohan.dev/blog/2025/shard-optimizing-vision-transformers-edge-npu/](https://amohan.dev/blog/2025/shard-optimizing-vision-transformers-edge-npu/)

生成摘要时出错

---

## 94. Economics of Orbital vs. Terrestrial Data Centers

**原文标题**: Economics of Orbital vs. Terrestrial Data Centers

**原文链接**: [https://andrewmccalip.com/space-datacenters](https://andrewmccalip.com/space-datacenters)

生成摘要时出错

---

## 95. US threatens EU digital services market access

**原文标题**: US threatens EU digital services market access

**原文链接**: [https://twitter.com/ustraderep/status/2000990028835508258](https://twitter.com/ustraderep/status/2000990028835508258)

生成摘要时出错

---

## 96. A linear-time alternative for Dimensionality Reduction and fast visualisation

**原文标题**: A linear-time alternative for Dimensionality Reduction and fast visualisation

**原文链接**: [https://medium.com/@roman.f/a-linear-time-alternative-to-t-sne-for-dimensionality-reduction-and-fast-visualisation-5cd1a7219d6f](https://medium.com/@roman.f/a-linear-time-alternative-to-t-sne-for-dimensionality-reduction-and-fast-visualisation-5cd1a7219d6f)

生成摘要时出错

---

## 97. The appropriate amount of effort is zero

**原文标题**: The appropriate amount of effort is zero

**原文链接**: [https://expandingawareness.org/blog/the-appropriate-amount-of-effort-is-zero/](https://expandingawareness.org/blog/the-appropriate-amount-of-effort-is-zero/)

生成摘要时出错

---

## 98. NOAA deploys new generation of AI-driven global weather models

**原文标题**: NOAA deploys new generation of AI-driven global weather models

**原文链接**: [https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models)

生成摘要时出错

---

## 99. Chafa: Terminal Graphics for the 21st Century

**原文标题**: Chafa: Terminal Graphics for the 21st Century

**原文链接**: [https://hpjansson.org/chafa/](https://hpjansson.org/chafa/)

生成摘要时出错

---

## 100. Show HN: TheAuditor v2.0 – A “Flight Computer” for AI Coding Agents

**原文标题**: Show HN: TheAuditor v2.0 – A “Flight Computer” for AI Coding Agents

**原文链接**: [https://github.com/TheAuditorTool/Auditor](https://github.com/TheAuditorTool/Auditor)

生成摘要时出错

---

