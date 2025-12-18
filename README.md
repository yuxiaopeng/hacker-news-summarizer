# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-18.md)

*最后自动更新时间: 2025-12-18 02:18:31*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 2 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 3 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 4 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 5 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 6 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 7 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 8 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 9 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 10 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 11 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 12 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 13 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 14 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 15 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 16 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 17 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 18 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 19 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 20 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 21 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 22 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 23 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 24 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 25 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 26 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 27 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 28 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 29 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 30 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 31 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 32 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 33 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 34 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 35 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 36 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 37 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 38 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 39 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 40 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 41 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 42 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 43 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 44 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 45 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 46 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 47 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 48 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 49 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 50 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 51 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 52 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 53 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 54 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 55 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 56 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 57 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 58 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 59 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 60 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 61 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 62 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 63 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 64 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 65 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 66 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 67 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 68 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 69 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 70 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 71 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 72 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 73 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 74 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 75 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 76 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 77 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 78 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 79 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 80 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 81 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 82 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 83 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 84 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 85 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 86 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 87 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 88 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 89 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 90 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 91 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 92 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 93 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 94 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 95 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 96 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 97 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 98 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 99 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 100 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 101 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 102 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 103 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 104 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 105 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 106 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 107 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 108 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 109 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 110 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 111 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 112 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 113 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 114 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 115 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 116 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 117 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 118 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 119 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 120 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 121 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 122 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 123 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 124 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 125 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 126 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 127 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 128 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 129 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 130 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 131 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 132 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 133 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 134 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 135 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 136 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 137 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 138 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 139 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 140 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 141 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 142 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 143 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 144 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 145 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 146 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 147 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 148 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 149 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 150 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 151 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 152 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 153 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 154 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 155 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 156 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 157 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 158 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 159 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 160 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 161 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 162 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 163 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 164 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 165 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 166 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 167 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 168 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 169 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 170 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 171 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 172 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 173 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 174 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 175 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 176 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 177 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 178 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 179 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 180 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 181 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 182 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 183 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 184 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 185 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 186 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 187 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 188 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 189 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 190 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 191 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 192 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 193 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 194 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 195 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 196 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 197 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 198 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 199 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 200 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 201 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 202 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 203 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 204 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 205 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 206 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 207 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 208 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 209 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 210 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 211 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 212 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 213 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 214 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 215 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 216 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 217 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 218 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 219 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 220 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 221 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 222 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 223 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 224 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 225 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 226 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 227 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 228 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 229 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 230 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 231 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 232 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 233 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 234 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 235 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 236 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 237 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 238 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 239 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 240 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 241 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 242 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 243 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 244 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 245 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 246 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 247 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 248 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 249 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 250 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 251 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 252 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 253 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 254 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 255 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 256 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 257 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 258 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 259 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 260 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 261 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 262 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 263 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 264 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 265 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 266 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 267 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 268 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 269 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 270 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 271 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 272 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 273 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
