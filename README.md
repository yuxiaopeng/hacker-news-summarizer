# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-10.md)

*最后自动更新时间: 2026-05-10 18:18:29*
## 1. Tracesofhumanity.org，作者：Joanna Rutkowska

**原文标题**: Tracesofhumanity.org by Joanna Rutkowska

**原文链接**: [https://tracesofhumanity.org/hello-world/](https://tracesofhumanity.org/hello-world/)

在为 *Tracesofhumanity.org* 撰写的开篇博文中，著名安全研究员、Qubes OS 创始人 Joanna Rutkowska 宣布在沉寂七年后重返博客圈。Rutkowska 在 2006 年至 2018 年间因其在操作系统和虚拟化安全领域的深厚造诣而闻名，她反思了自己早期的职业生涯如何几乎完全将“真理”与“自由”视为至高无上的价值，且往往以牺牲生活的其他人文维度为代价。

现年四十多岁的 Rutkowska 描述了一个更趋成熟且更为复杂的价值观体系。她的新博客旨在记录她在平衡相互矛盾的理想时所经历的个人挣扎：理性与人文、务实与美感，以及个人主义与社区。尽管她早期的工作优先考虑形式逻辑和隐私，但她目前的思考则试图融入直觉、爱与平等主义。

Rutkowska 明确表示，她并不声称已找到了人类幸福的终极答案。相反，她认为人文主义的本质可能正隐藏在这种挣扎本身的不确定性和不完整性之中。通过分享这些感悟，她希望能提供一些令她年轻时那个纯粹理性的自我也会感到充实的见解。最后，她邀请读者参与对话，欢迎大家提出个人观点以及对她推论的理性批判。

---

## 2. 走路变慢了？问题可能出在耳朵，而非膝盖

**原文标题**: Walking Slower? Why Your Ears, Not Your Knees, Might Be the Problem

**原文链接**: [https://www.wsj.com/health/wellness/hearing-loss-walking-speed-iphone-study-c53c482a](https://www.wsj.com/health/wellness/hearing-loss-walking-speed-iphone-study-c53c482a)

一项发表在《JAMA Network Open》上的研究利用“Apple心脏与运动研究”的数据揭示，听力损失与步行速度减慢之间存在显著相关性。来自密歇根大学和布莱根妇女医院的研究人员分析了约4万名参与者的数据，这些参与者通过iPhone和Apple Watch追踪了自己的步态和听力健康状况。

研究结果显示，听力灵敏度每下降10分贝，个体的步速就会减慢约0.02米/秒。即便在研究人员对年龄、性别及其他健康因素进行调整后，这种关联依然存在。

专家指出，产生这种联系的原因主要有几点：
*   **认知负荷：** 当大脑需要消耗更多精力处理声音时，用于控制平衡和维持稳定行动的认知资源就会减少。
*   **空间意识：** 声音提供了关键的环境线索，协助个体辨别方向并保持稳定。
*   **前庭系统：** 由于内耳同时包含耳蜗（负责听觉）和前庭系统（负责平衡），其中一方受损往往会影响另一方。

医学专家常将步速称为“第六大生命体征”，因为它是预测寿命、认知健康以及跌倒风险的重要指标。该研究表明，听力损失可能是导致身体机能下降的一个容易被忽视的因素。因此，通过早期筛查和佩戴助听器来关注听力健康，或许是维持老年人行动能力与独立生活能力的重要干预手段。

---

## 3. 重返 AWS，我想起了当初离开的原因

**原文标题**: I returned to AWS, and was reminded why I left

**原文链接**: [http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html](http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html)

在这篇文章中，亚马逊云服务（AWS）的早期拥护者和曾经的“铁杆粉丝”安德鲁·斯图尔特（Andrew Stuart）记录了他从一名忠实用户转变为批评者，并最终彻底弃用该平台的历程。

斯图尔特概述了长达十年的积怨，这些问题侵蚀了他对 AWS 的信任。他的主要抱怨包括：
* **高昂的成本：** 特别是“离谱”的数据流出费用（egress fees）以及针对内部数据传输“隐蔽”且复杂的计费方式。
* **技术挫败感：** IAM（身份与访问管理）极其复杂，AWS Lambda 导致的供应商锁定，以及平台向 Python 3 等现代标准迁移缓慢。
* **伦理问题：** 他将 AWS 定性为“掠夺者”，因其有克隆 Elasticsearch 和 Redis 等开源项目并从中获利的黑历史。

虽然他在几年前就迁移了大部分基础设施，但斯图尔特最近重返 AWS，旨在对高性能的 192 核 EC2 实例进行基准测试，并在 Bedrock 上测试 Claude。这个休眠账号的突然活跃触发了系统的自动安全停用。结果，斯图尔特的主要业务邮箱（AWS WorkMail）被禁用，导致其业务运营陷入瘫痪。

斯图尔特愤怒的核心在于后续处理：尽管他遵守了安全协议并尝试联系支持部门，但他面临的是长达四天的毫无回应，以及“请耐心等待”这类格式化的回复。他总结道，这次经历成为了他离开的最后通牒，并誓言将其剩余服务（Workmail 和 Route53）永久迁出该平台，以避开定义了现代 AWS 体验的“复杂性陷阱”和糟糕的技术支持。

---

## 4. 数学家该何去何从？

**原文标题**: What's a Mathematician to Do?

**原文链接**: [https://mathoverflow.net/questions/43690/whats-a-mathematician-to-do](https://mathoverflow.net/questions/43690/whats-a-mathematician-to-do)

本文记录了 MathOverflow 上一段触动人心的讨论，起因是一名本科生对高斯、欧拉等数学“天才”感到畏惧。该学生质疑，没有非凡天赋的人是否能为该领域做出任何原创性贡献，还是只能沦为重大突破的“炮灰”。

数学界的回复提供了一个深刻的视角转变：

*   **人性与清晰度：** 著名数学家比尔·瑟斯顿（Bill Thurston）认为，数学的真正目标是提升人类的洞察力和理解力，而非仅仅产出定理。他强调数学是一项社会性事业；如果没有一个充满活力的社区来消化、重构和交流思想，数学知识实际上会逐渐凋零。
*   **阐释的价值：** 讨论者强调，“原创性”并非衡量成功的唯一标准。教学和写作是该领域至关重要的组成部分。将复杂的思想转化为易于理解的形式，本身就是一种创造性的、不可或缺的行为，它为后代传承了这门学科。
*   **坚持胜过天才：** 社区指出，许多“顶级”数学家也会产生“冒充者综合征”。文中引用了理查德·费曼的建议：只要持续学习，你终将抵达已知知识的边界，并发现新的领域。
*   **乔丹类比：** 文中提出了一个简单而有力的观点：“你不必成为迈克尔·乔丹也可以打篮球。” 无论是否能达到传奇地位，一个人都可以通过热爱与参与，在数学中找到成就感并做出有意义的贡献。

总之，这些建议的核心在于：数学是一项人类协作的追求。贡献不仅源于革命性的突破，也源于对理解、分享和维护数学思想这一“生命体”的倾心奉献。

---

## 5. 调度场动画

**原文标题**: Shunting-Yard Animation

**原文链接**: [https://somethingorotherwhatever.com/shunting-yard-animation/](https://somethingorotherwhatever.com/shunting-yard-animation/)

这段文字是名为“调度场算法动画”的交互式应用程序的占位符和备用信息。其内容告知访问者，该程序若非成功加载，便是初始化失败，而在后一种情况下，这段文字将保持显示。作者以幽默和自嘲的口吻，直言不讳地表示自己并未努力确保该程序能在所有平台或为所有用户正常运行。本质上，这是为一个可能无法运行或具有平台局限性的网页工具所做的坦诚免责声明。

---

## 6. Linux 上的太空军校生弹球

**原文标题**: Space Cadet Pinball on Linux

**原文链接**: [https://brennan.io/2026/05/09/pinball-and-escrow/](https://brennan.io/2026/05/09/pinball-and-escrow/)

在这篇文章中，Stephen Brennan 解释了 Linux 用户如何体验经典的 Windows XP 游戏——**三维弹球：太空军校生 (Space Cadet Pinball)**。得益于一位开发者对原版游戏进行了逆向工程，并编写了可跨平台（包括 Linux、Mac、Android 和 Nintendo Switch）移植的源代码，这一项目才得以实现。

**安装与增强**
在 Linux 上最简单的游玩方式是通过 **Flatpak**，执行以下命令：  
`flatpak install com.github.k4zmu2a.spacecadetpinball`

虽然标准版运行在 480p 分辨率下，但 Brennan 指出，玩家可以使用该游戏的商业版本 *Full Tilt! Pinball*（可在 archive.org 获取）的数据文件，实现 **1024x768 分辨率**。他为这一升级提供了技术操作流程：
1. 将 *Full Tilt!* 的数据提取到 Flatpak 的数据目录中。
2. 删除原有的捆绑数据文件，强制游戏识别新的高分辨率资源。
3. 注意这些文件还会略微改变游戏机制，例如使重新进入通道的灯光更容易点亮。

**软件保护与伦理**
除了技术指南，Brennan 还讨论了“弃置软件 (abandonware)”的伦理问题。虽然他主张向创作者付费并尊重版权，但他承认要对已停售的软件做到这一点非常困难。他提出了一个**源代码托管 (source code escrow)** 系统：当所有者停止商业支持时，专有软件应转换为 FOSS（自由及开源软件）许可。这种方法旨在平衡创作者的权益与软件保护的文化价值。

---

## 7. Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

**原文标题**: Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

**原文链接**: [https://twitter.com/jarredsumner/status/2053047748191232310](https://twitter.com/jarredsumner/status/2053047748191232310)

Based on the title provided, here is a concise summary of the news:

**Summary: Bun’s Rust Rewrite Achievement**

Bun, the high-performance JavaScript runtime and toolkit originally developed primarily in Zig, has reached a significant milestone in its **experimental Rust-based rewrite**. The project has officially hit **99.8% test compatibility** on Linux x64 systems using the glibc library.

This achievement indicates that the Rust implementation is nearing functional parity with the original version on core Linux platforms. By maintaining nearly 100% compatibility with its existing test suite, the Bun team demonstrates that the transition to Rust can preserve the runtime's speed and features while potentially benefiting from Rust’s memory safety and broader ecosystem. This shift marks a major evolution in Bun's underlying architecture as it moves toward greater stability for mainstream server environments.

---

## 8. Idempotency Is Easy Until the Second Request Is Different

**原文标题**: Idempotency Is Easy Until the Second Request Is Different

**原文链接**: [https://blog.dochia.dev/blog/idempotency/](https://blog.dochia.dev/blog/idempotency/)

In the article "Idempotency Is Easy Until the Second Request Is Different," the author explores the technical nuances of implementing idempotency, arguing that it is more complex than simply deduplicating requests based on a unique key.

The core challenge arises when a client sends a second request using a previously used `Idempotency-Key` but provides a **different request body** (e.g., a different payment amount or recipient). If the server only checks for the existence of the key and returns the cached successful result, it creates a silent failure where the user believes their second, different intent was processed, when in fact it was ignored.

To build a robust idempotency layer, the author highlights several key strategies:

*   **Payload Validation:** Servers should store a hash of the original request body alongside the idempotency key. If a subsequent request arrives with the same key but a different hash, the server should return an error (such as `422 Unprocessable Entity` or `409 Conflict`) rather than a cached success.
*   **Request Fingerprinting:** To prevent collisions between different users, idempotency keys should be scoped to a specific user or resource, effectively creating a composite key.
*   **Handling Concurrency:** Systems must account for race conditions where two identical requests arrive simultaneously. This is typically managed by using an "In-Progress" state or atomic locks to ensure only one process executes the business logic.
*   **Lifecycle Management:** Idempotency records should have a Time-To-Live (TTL). Since the mechanism is intended to handle network retries, the results do not need to be stored indefinitely.

The article concludes that true idempotency is about ensuring a retry matches the **original intent**. By validating the request body and managing concurrent states, developers can prevent data corruption and ensure system consistency.

---

## 9. 一美元伪钞犯

**原文标题**: The One Dollar Counterfeiter

**原文链接**: [https://www.amusingplanet.com/2026/05/emerich-juettner-one-dollar.html](https://www.amusingplanet.com/2026/05/emerich-juettner-one-dollar.html)

埃默里奇·朱特纳（Emerich Juettner）是一位居住在纽约市的奥地利移民，他成为了美国历史上最令人意想不到且最成功的伪钞制造者之一。被特勤局称为“880先生”的朱特纳在1938年，即他60岁时，开始印制一美元面值的伪钞，以补贴他作为废品收集者的微薄收入。

与追求高精度和大面值的专业造假者不同，朱特纳的作品制作极其粗糙。他印制的伪钞油墨拙劣、细节模糊，甚至存在拼写错误。然而，他利用了一个简单的心理现实，成功逃避追捕长达十年之久：人们很少会去检查一美元的钞票。通过仅进行小额流通，且从不在同一地点花费超过一张伪钞，他避开了通常针对大额货币的严格审查。

美国特勤局在“880号案件”上耗费了十年时间，使其成为了该机构历史上耗资最巨的伪钞调查案。直到1948年，朱特纳才因纯粹的巧合落网。在他的公寓发生火灾后，消防员将他的财物（包括锌制雕刻版）扔进了一处空地，随后这些物品被当地的孩子们发现。

被捕后，这位老人表现出的不贪婪，以及他关于“从未让任何人的损失超过一美元”的申辩，博得了公众和媒体的好感。法官意识到他的行为是出于生存而非恶意，因此对他从轻发落，判处一年零一天的监禁，并处以一美元的象征性罚款。朱特纳的故事后来被载入1950年的好莱坞电影《880先生》，这部电影最终为他带来的收益超过了他十年来制造伪钞的总和。此后，他在长岛过着平静的生活，直到1955年去世。

---

## 10. Think Linear Algebra (2023)

**原文标题**: Think Linear Algebra (2023)

**原文链接**: [https://allendowney.github.io/ThinkLinearAlgebra/index.html](https://allendowney.github.io/ThinkLinearAlgebra/index.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 2 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 3 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 4 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 5 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 6 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 7 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 8 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 9 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 10 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 11 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 12 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 13 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 14 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 15 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 16 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 17 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 18 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 19 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 20 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 21 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 22 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 23 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 24 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 25 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 26 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 27 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 28 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 29 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 30 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 31 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 32 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 33 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 34 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 35 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 36 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 37 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 38 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 39 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 40 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 41 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 42 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 43 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 44 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 45 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 46 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 47 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 48 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 49 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 50 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 51 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 52 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 53 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 54 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 55 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 56 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 57 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 58 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 59 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 60 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 61 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 62 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 63 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 64 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 65 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 66 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 67 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 68 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 69 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 70 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 71 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 72 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 73 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 74 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 75 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 76 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 77 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 78 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 79 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 80 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 81 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 82 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 83 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 84 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 85 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 86 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 87 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 88 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 89 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 90 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 91 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 92 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 93 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 94 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 95 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 96 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 97 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 98 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 99 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 100 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 101 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 102 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 103 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 104 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 105 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 106 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 107 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 108 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 109 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 110 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 111 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 112 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 113 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 114 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 115 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 116 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 117 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 118 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 119 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 120 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 121 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 122 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 123 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 124 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 125 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 126 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 127 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 128 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 129 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 130 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 131 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 132 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 133 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 134 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 135 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 136 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 137 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 138 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 139 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 140 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 141 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 142 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 143 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 144 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 145 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 146 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 147 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 150 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 151 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 152 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 153 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 154 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 155 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 156 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 157 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 158 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 159 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 160 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 161 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 162 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 163 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 164 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 165 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 166 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 167 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 168 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 169 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 170 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 171 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 172 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 173 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 174 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 175 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 176 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 177 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 178 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 179 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 180 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 181 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 182 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 183 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 184 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 185 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 186 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 187 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 188 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 189 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 190 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 191 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 192 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 193 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 194 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 195 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 196 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 197 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 198 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 199 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 200 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 201 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 202 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 203 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 204 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 205 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 206 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 207 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 208 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 209 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 210 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 211 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 212 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 213 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 214 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 215 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 216 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 217 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 218 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 219 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 220 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 221 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 222 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 223 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 224 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 225 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 226 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 227 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 228 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 229 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 230 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 231 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 232 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 233 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 234 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 235 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 236 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 237 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 238 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 239 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 240 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 241 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 242 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 243 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 244 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 245 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 246 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 247 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 248 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 249 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 250 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 251 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 252 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 253 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 254 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 255 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 256 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 257 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 258 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 259 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 260 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 261 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 262 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 263 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 264 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 265 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 266 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 267 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 268 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 269 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 270 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 271 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 272 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 273 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 274 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 275 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 276 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 277 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 278 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 279 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 280 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 281 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 282 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 283 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 284 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 285 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 286 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 287 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 288 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 289 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 290 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 291 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 292 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 293 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 294 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 295 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 296 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 297 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 298 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 299 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 300 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 301 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 302 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 303 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 304 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 305 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 306 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 307 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 308 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 309 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 310 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 311 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 312 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 313 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 314 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 315 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 316 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 317 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 318 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 319 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 320 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 321 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 322 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 323 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 324 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 325 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 326 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 327 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 328 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 329 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 330 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 331 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 332 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 333 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 334 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 335 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 336 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 337 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 338 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 339 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 340 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 341 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 342 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 343 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 344 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 345 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 346 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 347 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 348 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 349 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 350 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 351 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 352 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 353 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 354 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 355 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 356 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 357 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 358 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 359 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 360 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 361 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 362 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 363 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 364 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 365 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 366 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 367 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 368 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 369 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 370 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 371 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 372 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 373 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 374 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 375 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 376 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 377 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 378 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 379 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 380 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 381 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 382 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 383 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 384 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 385 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 386 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 387 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 388 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 389 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 390 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 391 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 392 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 393 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 394 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 395 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 396 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 397 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 398 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 399 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 400 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 401 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 402 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 403 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 404 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 405 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 406 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 407 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 408 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 409 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 410 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 411 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 412 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 413 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 414 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 415 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 416 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
