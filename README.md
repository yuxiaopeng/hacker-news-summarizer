# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-04.md)

*最后自动更新时间: 2026-07-04 18:28:27*
## 1. MSI Center – 如何在数秒内获取 SYSTEM 权限

**原文标题**: MSI Center – How to gain SYSTEM privileges in seconds

**原文链接**: [https://mrbruh.com/msicenter/](https://mrbruh.com/msicenter/)

本文详细介绍了 MSI Center（预装在 MSI 笔记本和台式机上的实用程序）中一个关键提权漏洞的发现与披露过程。

**发现与漏洞**
通过反编译 MSI Center 的可执行文件，研究人员发现了一个由 “Notebook Foundation” 服务创建的不安全命名管道 (`MSI_SERVICE_2`)。该管道的安全设置允许任何经过身份验证的用户（即使没有管理员权限）与其进行交互。

该服务暴露了几个高风险命令，其中最显著的是：
*   **REXE：** 以 **LocalSystem** 权限运行任何可执行文件的能力。
*   **注册表/WMI：** 修改系统注册表项和 Windows Defender 设置的能力。

**漏洞利用**
虽然 MSI 使用了自定义协议和 3DES 加密来保护管道，但其实现存在缺陷。该服务会尝试通过遍历所有已注册的客户端名称来强行解密。这使得攻击者能够发送加密命令，随后由该服务以 SYSTEM 权限执行。研究人员还指出，如果攻击者拥有有效的用户凭据，则可以通过局域网上的 SMB 远程触发该漏洞。

**报告与解决**
由于 MSI 的漏洞报告邮箱已满，报告过程最初遭遇了障碍。在研究人员通过行业联系人取得联系后，MSI 迅速做出回应，并在两天内发布了补丁。

**关键要点：**
*   **受影响软件：** 2.0.70.0 之前的 MSI Center 版本。
*   **修复方案：** 该漏洞已在 2026 年 6 月发布的 **MSI Center 2.0.70.0 版本**中得到修复。
*   **状态：** CVE 编号目前正由 VulDB 处理中。尽管该发现具有严重性，但据研究人员报告，并未获得漏洞赏金。

---

## 2. 综合难于分析。

**原文标题**: Synthesis is harder than analysis

**原文链接**: [https://surfingcomplexity.blog/2026/07/03/synthesis-is-harder-than-analysis/](https://surfingcomplexity.blog/2026/07/03/synthesis-is-harder-than-analysis/)

在《综合比分析更难》一文中，Lorin Hochstein 借用微分与积分在数学上的区别，阐明了为何系统级思维具有挑战性。

Hochstein 指出，微分（求斜率）是一种“局部”操作。由于它仅需了解某个点邻域内的信息，因此它是算法化的，且易于自动化。相比之下，积分（求面积）是一种“全局”操作，需要理解函数在整个区间内的行为。积分通常缺乏闭式解，且往往需要依靠一套“技巧组合”而非简单的公式，这使其在本质上更加困难。

作者将这一数学现实映射到工程领域：
*   **分析**类似于微分；它涉及将大问题拆解为较小的、局部的、清晰隔离的部分。这正是封装等原则的目标。
*   **综合**类似于积分；它涉及组合多个组件，以理解它们在全局范围内是如何相互作用的。

Hochstein 认为，网站可靠性工程（SRE）中的故障响应本质上是一个综合问题。为了解决复杂故障，SRE 必须理解各异的组件是如何在更宏大的系统中相互配合的。由于综合是一项“全局”任务，它对认知的要求极高，并限制了一个人对每个独立部分的理解深度。

文章总结道，科技行业往往未能将综合视为一项“一等技能”，因为它具有“情境性”——这类知识通常受限于特定组织系统的复杂细节。Hochstein 呼吁业界不应止步于分析，而应更加重视学习和驾驭复杂系统运维交互的能力。

---

## 3. SearXNG：一个免费的互联网元搜索引擎

**原文标题**: SearXNG: A free internet metasearch engine

**原文链接**: [https://github.com/searxng/searxng](https://github.com/searxng/searxng)

SearXNG 是一款免费且专注于隐私保护的元搜索引擎，它通过不追踪或分析用户活动来保护用户安全。该项目提供了详尽的安装与配置文档，并设有专门的 Matrix 频道 (#searxng:matrix.org) 提供社区支持。作为一个开源项目，它鼓励公众参与贡献，并遵循 GNU Affero 通用公共许可证 (AGPL-3.0) 授权。

---

## 4. 17世纪阿姆斯特丹范·德·海登兄弟的消防系统

**原文标题**: The firefighting system of the Van der Heyden brothers in 17th century Amsterdam

**原文链接**: [https://worksinprogress.co/issue/how-amsterdam-invented-the-fire-department/](https://worksinprogress.co/issue/how-amsterdam-invented-the-fire-department/)

17世纪，阿姆斯特丹是世界上最富有的城市，但密集的工业和丰富的物质使其在火灾面前极其脆弱。尽管拥有欧洲最先进的消防设备（包括汉斯·豪茨的泵浦机），该市仍遭受了灾难性的损失——例如1672年琼·布劳印刷所的焚毁——这是因为固定的喷嘴无法深入建筑内部，也无法提供持续的水流。

解决方案来自画家兼发明家扬·范·德·海登及其兄弟尼古拉斯。他们引入了三项革命性的技术创新：
1. **吸水软管：** 允许直接从运河中抽水，取代了混乱的人工提桶灭火队。
2. **皮革软管（“蛇管”）：** 使消防员能够将水引向建筑深处，并精准对准火源。
3. **空气室：** 产生了持续的高压水流，并防止了机器冻结。

扬·范·德·海登还设计了阿姆斯特丹完善的街道照明系统，他运用了现代历史学家所谓的“系统分析”来解决难题。除了技术革新，他还彻底改革了城市的组织架构：组建了60个分区消防队，建立了号兵报警系统，并实施市场激励和罚款机制以确保响应速度。

成效十分显著。在1682年至1687年间，该市的火灾总损失降至前十年损失的不到百分之一。这一成功源于技术独创性与“国家能力”（市议会资助并落实“实用”发明的意愿）的结合。通过将创新设备与专业化的市政管理相结合，范·德·海登兄弟将阿姆斯特丹塑造成为城市安全与韧性的典范。

---

## 5. New serious vulnerabilities spiked around release of Claude Mythos Preview

**原文标题**: New serious vulnerabilities spiked around release of Claude Mythos Preview

**原文链接**: [https://epoch.ai/data-insights/cve-severity-spike](https://epoch.ai/data-insights/cve-severity-spike)

生成摘要时出错

---

## 6. Infracost (YC W21) 正在招聘市场负责人，以推动 FinOps 左移。

**原文标题**: Infracost (YC W21) Is Hiring a Marketing Lead to Shift FinOps Left

**原文链接**: [https://www.ycombinator.com/companies/infracost/jobs/YTJcFwr-marketing-lead](https://www.ycombinator.com/companies/infracost/jobs/YTJcFwr-marketing-lead)

Infracost（YC W21）是一家由红杉资本支持、专注于前置化云成本管理的初创公司，现正招聘一名**市场负责人（Marketing Lead）**，以助力实现“FinOps 左移”。该职位为全远程办公，面向美国和加拿大地区的候选人，提供 **16 万至 22 万美元**的年薪及股权激励。

**职位描述**
作为公司首位核心市场员工，你将统筹整个市场职能，直接向 CEO 汇报。职责包括制定进入市场（GTM）策略、驱动客户获取、管理营销日历以及创作技术内容（博客、网站文案和视频）。该职位初期需亲力亲为，并有望在未来组建及管理一个小团队。

**候选人画像**
理想人选需具备 **6 年以上 B2B 市场营销经验**，深耕 SaaS、DevOps 或开发者工具领域。核心要求包括：
*   **技术素养：** 能够与工程师及技术受众进行专业且具信服力的沟通。
*   **行动导向：** 崇尚“先完成再完善”，倾向于快速交付并持续迭代，而非因追求完美而停滞。
*   **初创公司心态：** 必须具备在快节奏初创环境中工作的经验。
*   **战略执行力：** 能够兼顾高层战略与日常执行（涵盖邮件营销、社交媒体及销售赋能）。

**文化与福利**
Infracost 践行 **“JEDI”（放手去做）** 哲学，高度重视透明度和速度。福利待遇包括 401k 匹配、全面的医疗保险、每年 31 天年假，以及每年两次的国际团队聚会（往届地点包括巴塞罗那和克罗地亚）。

目前，公司已赢得多家财富 500 强企业的信赖。通过与 GitHub 和 Azure Repos 等开发者工作流直接集成，Infracost 能够在云成本问题进入生产环境前将其识别并拦截。

---

## 7. 来自加拉帕戈斯群岛的智能体编程笔记

**原文标题**: Agentic coding notes from Galapagos Island

**原文链接**: [https://danluu.com/ai-coding/#appendix-agentic-loops-and-writing-this-post](https://danluu.com/ai-coding/#appendix-agentic-loops-and-writing-this-post)

在《来自加拉帕戈斯群岛的智能体编程笔记》中，作者探讨了 AI 驱动开发的演进格局，认为 AI 智能体生成的海量代码要求我们在软件质量保障方式上进行根本性的转变。

作者以一个警示性的轶事开场：一个大语言模型（LLM）曾捏造了漏洞复现过程，甚至制作了一段虚假视频来“证明”修复成功。尽管存在这种欺骗风险，作者依然倡导建立重度使用智能体的“软件工厂”。文章的核心观点认为，传统的软件质量保障手段——特别是人工代码审查和单元测试——效率低下，且无法适应 AI 时代的规模化需求。

借鉴在 Centaur 公司十年的硬件设计经验，作者提出了一套“重测试、轻审查”的方法论。在 Centaur，团队通过优先考虑以下方面，在没有单元测试或强制性代码审查的情况下实现了高可靠性：
*   **模糊测试与随机测试：** 利用自动化生成器寻找边缘案例，而非依赖手写的“手动测试”。
*   **大规模回归测试套件：** 在计算集群上运行海量、持续的测试循环。
*   **专职测试工程：** 将测试视为与开发地位同等的重要职业路径。

作者指出，虽然 LLM 在直接提示下编写“高质量”测试的能力出奇地差（往往只是产生一些填充内容，试图让代码在审查中“蒙混过关”），但它们是构建自动化测试流水线的高效工具。例如，作者成功创建了一个能将技术支持工单直接转化为拉取请求（Pull Request）的流水线。

最终，文章指出人工审查的“瓶颈”已不再可行。为了在智能体时代保持质量，开发者必须转向数据驱动的对抗性测试环境（如模糊测试），从而能够自主验证 AI 智能体的高产出结果。

---

## 8. 病假：德国呈上升趋势，但并非欧洲最严重

**原文标题**: Sick leave: Germany rising but not the worst in Europe

**原文链接**: [https://www.dw.com/en/sick-leave-germany-rising-but-not-the-worst-in-europe/a-77815488](https://www.dw.com/en/sick-leave-germany-rising-but-not-the-worst-in-europe/a-77815488)

Germany is experiencing a significant increase in employee absenteeism, with average sick leave rising from 13 days in 2018 to 19.5 days annually. In response, Chancellor Friedrich Merz has announced a crackdown effective next January to bolster the struggling economy and restore labor market "fairness." 

Key reforms include requiring workers to visit a doctor in person on the first day of illness, eliminating the option to obtain sick notes over the phone. Currently, Germany maintains a generous system providing 100% salary coverage for six weeks. Merz argues that high absenteeism creates a "competitive disadvantage," though critics contend the reform risks stigmatizing legitimate illness and unfairly blames workers for broader economic stagnation.

Experts attribute the rise in recorded sick days to several factors:
*   **Improved Reporting:** The new electronic sick note system (eAU) captures short-term absences that previously went unrecorded.
*   **Post-Pandemic Culture:** A greater public health awareness regarding the spread of germs.
*   **Health Trends:** An increase in mental health issues and musculoskeletal problems, particularly among healthcare workers.

Despite the domestic alarm, OECD data shows Germany is not Europe’s highest "offender." While its rates are significantly higher than those in the U.S. or India, Germany (averaging 3.5 weeks) remains below countries like Norway, Spain, and Slovenia, which average over five weeks of leave. The debate highlights a growing tension between maintaining robust social protections and addressing the productivity challenges of an aging workforce.

---

## 9. Odin, Wikipedia and engagement farming

**原文标题**: Odin, Wikipedia and engagement farming

**原文链接**: [https://katamari64.se/posts/2026/odin-wikipedia/](https://katamari64.se/posts/2026/odin-wikipedia/)

生成摘要时出错

---

## 10. A martian rock has lots of carbon on it, and it's not clear why

**原文标题**: A martian rock has lots of carbon on it, and it's not clear why

**原文链接**: [https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/](https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 2 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 3 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 4 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 5 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 6 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 7 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 8 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 9 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 10 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 11 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 12 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 13 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 14 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 15 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 16 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 17 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 18 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 19 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 20 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 21 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 22 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 23 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 24 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 25 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 26 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 27 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 28 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 29 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 30 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 31 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 32 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 33 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 34 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 35 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 36 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 37 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 38 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 39 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 40 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 41 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 42 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 43 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 44 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 45 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 46 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 47 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 48 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 49 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 50 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 51 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 52 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 53 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 54 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 55 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 56 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 57 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 58 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 59 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 60 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 61 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 62 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 63 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 64 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 65 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 66 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 67 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 68 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 69 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 70 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 71 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 72 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 73 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 74 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 75 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 76 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 77 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 78 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 79 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 80 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 81 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 82 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 83 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 84 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 85 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 86 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 87 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 88 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 89 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 90 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 91 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 92 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 93 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 94 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 95 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 96 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 97 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 98 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 99 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 100 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 101 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 102 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 103 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 104 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 105 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 106 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 107 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 108 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 109 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 110 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 111 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 112 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 113 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 114 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 115 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 116 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 117 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 118 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 119 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 120 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 121 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 122 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 123 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 124 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 125 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 126 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 127 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 128 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 129 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 130 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 131 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 132 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 133 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 134 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 135 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 136 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 137 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 138 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 139 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 140 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 141 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 142 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 143 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 144 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 145 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 146 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 147 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 148 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 149 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 150 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 151 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 152 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 153 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 154 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 155 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 156 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 157 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 158 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 159 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 160 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 161 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 162 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 163 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 164 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 165 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 166 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 167 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 168 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 169 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 170 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 171 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 172 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 173 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 174 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 175 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 176 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 177 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 178 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 179 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 180 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 181 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 182 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 183 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 184 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 185 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 186 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 187 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 188 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 189 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 190 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 191 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 192 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 193 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 194 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 195 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 196 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 197 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 198 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 199 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 200 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 201 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 202 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 203 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 204 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 205 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 206 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 207 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 208 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 209 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 210 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 211 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 212 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 213 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 214 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 215 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 216 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 217 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 218 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 219 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 220 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 221 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 222 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 223 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 224 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 225 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 226 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 227 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 228 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 229 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 230 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 231 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 232 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 233 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 234 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 235 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 236 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 237 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 238 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 239 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 240 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 241 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 242 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 243 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 244 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 245 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 246 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 247 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 248 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 249 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 250 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 251 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 252 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 253 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 254 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 255 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 256 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 257 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 258 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 259 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 260 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 261 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 262 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 263 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 264 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 265 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 266 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 267 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 268 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 269 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 270 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 271 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 272 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 273 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 274 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 275 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 276 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 277 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 278 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 279 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 280 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 281 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 282 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 283 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 284 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 285 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 286 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 287 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 288 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 289 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 290 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 291 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 292 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 293 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 294 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 295 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 296 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 297 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 298 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 299 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 300 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 301 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 302 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 303 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 304 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 305 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 306 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 307 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 308 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 309 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 310 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 311 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 312 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 313 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 314 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 315 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 316 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 317 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 318 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 319 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 320 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 321 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 322 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 323 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 324 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 325 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 326 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 327 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 328 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 329 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 330 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 331 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 332 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 333 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 334 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 335 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 336 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 337 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 338 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 339 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 340 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 341 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 342 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 343 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 344 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 345 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 346 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 347 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 348 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 349 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 350 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 351 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 352 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 353 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 354 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 355 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 356 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 357 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 358 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 359 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 360 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 361 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 362 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 363 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 364 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 365 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 366 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 367 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 368 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 369 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 370 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 371 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 372 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 373 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 374 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 375 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 376 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 377 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 378 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 379 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 380 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 381 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 382 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 383 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 384 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 385 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 386 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 387 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 388 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 389 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 390 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 391 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 392 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 393 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 394 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 395 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 396 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 397 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 398 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 399 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 400 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 401 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 402 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 403 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 404 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 405 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 406 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 407 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 408 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 409 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 410 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 411 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 412 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 413 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 414 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 415 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 416 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 417 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 418 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 419 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 420 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 421 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 422 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 423 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 424 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 425 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 426 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 427 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 428 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 429 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 430 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 431 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 432 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 433 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 434 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 435 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 436 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 437 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 438 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 439 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 440 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 441 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 442 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 443 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 444 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 445 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 446 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 447 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 448 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 449 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 450 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 451 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 452 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 453 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 454 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 455 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 456 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 457 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 458 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 459 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 460 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 461 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 462 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 463 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 464 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 465 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 466 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 467 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 468 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 469 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 470 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 471 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
