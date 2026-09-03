# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-03.md)

*最后自动更新时间: 2026-09-03 20:06:59*
## 1. Qwen 3.8 27B 现已上线 Cerebras，速度达 1500 tokens/s

**原文标题**: Qwen 3.8 27B available on Cerebras at 1500 tokens/s

**原文链接**: [https://inference-docs.cerebras.ai/models/overview](https://inference-docs.cerebras.ai/models/overview)

Cerebras 宣布在其公共 API 端点上推出 **Qwen 3.8 27B** 模型，可实现约每秒 **1,500 个 token** 的高速推理。该模型拥有 270 亿个参数，为免费用户提供 64k 的上下文窗口，为按需付费层级提供 128k 的窗口。

公告的关键细节包括：

*   **模型完整性：** Cerebras 强调其公共端点上的所有模型均为原始、未剪枝的版本。尽管公司在进行剪枝研究（例如其 REAP —— 路由器加权专家激活剪枝技术），但这些修改后的模型仅发布在 Hugging Face 上用于研究，并未应用于生产环境 API。
*   **选择性量化：** 为保持高质量，Cerebras 仅针对存储使用权重量化（4 位、8 位或 16 位）。在推理过程中，权重会进行实时反量化，以确保激活、注意力和 KV 缓存始终保持全精度。
*   **服务层级：** 用户可通过免费试用和按需付费层级访问该模型，并受速率限制。对于需要更高吞吐量、预留容量或生产级服务等级协议（SLA）的用户，Cerebras 提供专用端点。
*   **透明度：** Cerebras 保证在未提前通知的情况下不会更改模型架构。未来任何压缩或剪枝版本都将托管在独立且标识清晰的端点上，以确保开发者能够完全控制其使用的模型版本。

此次更新扩展了 Cerebras 的产品组合，其中还包括运行速度约为每秒 3,000 个 token 的 120B 参数 GPT OSS 等更大型号的模型。

---

## 2. GPT-6 Astra

**原文标题**: GPT-6 Astra

**原文链接**: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)

无法访问文章链接。

---

## 3. 名称 终止

**原文标题**: .name Termination

**原文链接**: [https://neil.fraser.name/news/2026/09/03/](https://neil.fraser.name/news/2026/09/03/)

在这篇文章中，尼尔·弗雷泽（Neil Fraser）讨论了“.name”注册局即将终止三级域名服务的问题。他解释说，在运营了近二十五年后，威瑞信（Verisign）提议移除这些域名以简化其管理流程，这一提议近期已获得 ICANN 的批准。

作者强调了该决定带来的几个严重后果，受影响的用户约有 22,000 名。由于这些域名是长期运营的网站、电子邮件地址和物联网（IoT）设备配置的基础，其突然移除将导致重大的数字混乱。除了个人网络存在的丧失外，弗雷泽还强调了一个重大的安全风险：一旦这些三级域名被注销，底层的二级域名可能会开放给他人注册。这可能允许新所有者重建旧地址，从而劫持敏感账户或拦截私人通信。

弗雷泽对威瑞信表示了深度的不信任，指责该公司向 ICANN 提供误导性信息以确保提案获得通过。尽管他已经预付了直至 2040 年的域名注册费用，但他仍面临数字身份彻底消失的局面。文章最后，作者表示他打算寻求法律咨询，以对这一决定发起挑战。

---

## 4. K2 Horizon：由六个开放模型组成的互联系列

**原文标题**: K2 Horizon: A connected fleet of six open models

**原文链接**: [https://ifm.ai/blog/k2/](https://ifm.ai/blog/k2/)

IFM 发布了 K2 Horizon，这是一个包含六款开源 AI 模型的模型族，参数规模从 0.9B 到 375B 不等。此次发布的独特之处在于其“完全开源”的方式：不仅开源了模型权重，还根据 Apache 2.0 协议公开了整个训练生命周期，包括中间检查点、训练数据配方、代码和细粒度日志。

该系列模型在多个规模上都表现出了顶尖性能：
*   **小规模：** 0.9B、3.7B 和 7B 模型在同尺寸级别中树立了新的性能标杆（SOTA），尤其是在推理和数学领域。
*   **架构创新：** 36B-A4B 模型引入了值注意力混合（MoVA）架构，这种稀疏架构使其能以仅 4B 的激活参数实现接近 32B 模型的性能。
*   **企业级实力：** 375B-A23B 模型是该系列中能力最强的模型，专为高难度的推理和软件工程任务而设计。

K2 Horizon 的核心支柱是其**对智能体化（Agentic）的关注**。它是首个公开了智能体化后训练完整开发过程的开源模型族，让研究人员能够深入研究工具调用和规划能力是如何生成的。这些模型在高达 22 万亿 token 的数据上进行了训练，其中近 17% 的预训练语料由显式推理轨迹组成。

为了提升部署体验，IFM 还推出了 **Uno Diffusion** 技术，通过更高效的 token 生成方式提供无损推理加速，且不会降低质量。凭借统一的架构和词表，K2 Horizon 为开发者提供了一个一致的框架，支持从智能手表等边缘设备到企业级工作站的应用扩展。

---

## 5. 任何曾活过的人——从古往今来所有人中随机抽取的一个生命

**原文标题**: Any Human Ever – One life, drawn at random from all who have ever lived

**原文链接**: [https://anyhumanever.com/](https://anyhumanever.com/)

**《曾活在世上的每一个人》**（Any Human Ever）是一个交互式数据驱动项目，允许用户从估计曾活在世上的 1000 亿人中随机抽取一个生命。通过利用历史数据和统计概率，该工具为跨越时空的人类体验提供了一个具有代表性的缩影。

选择过程分为三个不同的步骤：

1. **时间：** 用户抽取一个出生年份。该项目指出，由于人口的指数级增长，真正的随机抽取落在近现代的可能性远高于古代。
2. **地点：** 用户抽取一个地理位置。其概率根据人口密度进行加权，这意味着抽取结果更有可能落在历史上人口更稠密的“明亮集群”中。
3. **生命：** 最后，该工具会根据所选的时代和地点，生成一个具体的生命轨迹和故事。

该项目是一项旨在理解人口统计数据的统计练习，将关注点从著名的历史人物转向了构成人类历史绝大多数的“普通”个体。它强调了人类的规模，并利用真实数据将每一个随机生成的“故事”植根于历史现实之中。

---

## 6. 将我 1993 年的 Amiga 游戏移植到 Godot，利用大模型解读 68000 汇编代码

**原文标题**: Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

**原文链接**: [https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/)

本文详细记录了作者利用大语言模型（Claude）将其1993年的Amiga游戏《巴比伦孪生子》（Babylonian Twins）移植到 Godot 引擎的经历。这款游戏最初在遭受严厉制裁的巴格达开发，由超过 7.2 万行纯 68000 汇编语言编写，通过绕过操作系统直接驱动 Amiga 硬件运行。

作者为 LLM 设定了三个主要目标：移植 2010 年的 C++ 版本、重构 1993 年的原始汇编代码，并将两者整合。LLM 的表现具有变革意义：它仅用一个晚上就将 3.4 万行的 C++ 引擎移植到了 Godot 中的可运行状态，并成功破解了无注释的汇编代码，重新生成了与 1993 年原始发布版逐字节一致的二进制文件。

技术亮点包括：
*   **解析陈旧格式：** LLM 通过分析汇编程序读取和屏蔽数据位的方式，逆向工程了私有关卡格式和“隐形物理”（碰撞标志）。
*   **保留游戏“手感”：** 为了维持原汁原味的游戏体验，作者保留了不同的刻率（Amiga 版为 50Hz，现代版为 60Hz），并使用了原始的自定义碰撞逻辑，而非 Godot 内置的物理引擎。
*   **验证：** LLM 实现了工具链的自动化，利用现代汇编器和模拟器，结合原始代码和像素级精确的关卡截图来验证移植的准确性。

最后，作者指出，LLM 理清三十年前针对特定硬件的复杂代码的速度和准确度都超过了人类，不仅解决了关于游戏逻辑的历史疑问，还以极高的精度保存了一段伊拉克的游戏历史。

---

## 7. 风投不再是风投了

**原文标题**: VC isn't VC anymore

**原文链接**: [https://www.anildash.com/2026/09/02/cancer-capital/](https://www.anildash.com/2026/09/02/cancer-capital/)

In "VC isn’t VC anymore," tech executive Anil Dash argues that traditional venture capital has been supplanted by "Cancer Capital"—an unaccountable oligarchy driven by billionaire extremists. Dash contends that the industry has shifted from a high-risk funding model for innovation into a predatory system that prioritizes political power and wealth concentration over market success.

Dash highlights several key shifts:

*   **Insulation from Risk:** Large "do-everything" firms manage tens of billions of dollars. By collecting massive management fees (e.g., 2% of a $50 billion fund), these firms profit immensely regardless of whether their portfolio companies succeed or fail.
*   **Regulatory Evasion and Self-Dealing:** These firms have restructured to bypass traditional VC regulations. This allows them to engage in self-dealing—such as selling assets between their own funds—and cashing out long before a company becomes profitable or goes public.
*   **Shifted Power Dynamics:** The relationship between founders and investors has flipped. Dash asserts that many VCs now prioritize extremist political manifestos, selecting founders as mere agents to carry out those agendas rather than supporting independent innovation.
*   **Public Burden:** Modern VC funds increasingly draw from pension funds and retail retirement accounts, meaning the general public bears the financial risk while the "Cancer Capitalists" reap the rewards.
*   **Political Infiltration:** Dash points to firms like Andreessen Horowitz (a16z) as prime examples of this shift, noting their status as some of the largest political donors in the U.S. He argues they use their wealth to aggressively influence AI and crypto policy across both political parties.

Dash concludes that modern venture capital is no longer a financial engine for startups, but a social and political machine focused on dismantling democracy and civil society.

---

## 8. Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%

**原文标题**: Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%

**原文链接**: [https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california)

生成摘要时出错

---

## 9. Gloria Steinem has died

**原文标题**: Gloria Steinem has died

**原文链接**: [https://www.theguardian.com/books/2026/sep/03/gloria-steinem-groundbreaking-feminist-campaigner-dies-aged-92](https://www.theguardian.com/books/2026/sep/03/gloria-steinem-groundbreaking-feminist-campaigner-dies-aged-92)

美国先驱女权主义者、记者兼活动家格洛丽亚·斯泰纳姆（Gloria Steinem）逝世，享年92岁。她在亲友的陪伴下，于纽约市的家中安详离世。

斯泰纳姆在20世纪60和70年代声名鹊起，成为妇女解放运动的领军人物。她的职业生涯致力于通过严谨的新闻报道和公众演讲，将女权主义视角带入主流社会。其职业生涯的亮点包括：对“花花公子兔女郎”待遇著名的卧底揭露、共同创办《女士》（Ms.）杂志，以及创造了“生育自由”一词。

她的社会活动超出了性别平等的范畴：她曾参与反对越战和海湾战争，支持“黑人权力”和“黑人的命也是命”运动，并倡导LGBTQ+权利。她经常强调性别与种族的交织性，认为这两种形式的压迫密不可分。

尽管被许多人奉为英雄，斯泰纳姆也是一个极具争议的人物。批评者有时认为，由于她的种族和外貌，媒体给予了其领导地位优先关注。她还曾因1998年撰文为面临性骚扰指控的比尔·克林顿辩护，以及早期被认为敌视跨性别权利的言论而遭到抵制——她后来对这些立场进行了回应或澄清。

晚年的斯泰纳姆依然是唐纳德·特朗普的著名批评者，并担任了2017年女性大游行的共同主席。她致力于平等事业直至生命尽头，留下了九部著作和近一个世纪的社会活动遗产。她的亲属包括继子、演员克里斯蒂安·贝尔。来自希拉里·克林顿等人士的哀悼高度评价了她的乐观精神，以及她让他人感到被关注与倾听的独特能力。

---

## 10. Gooseworks (YC W23) 招聘：创始创意工程师

**原文标题**: Gooseworks (YC W23) Is Hiring – Founding Creative Engineer

**原文链接**: [https://www.ycombinator.com/companies/gooseworks/jobs/rfgY8La-founding-creative-engineer](https://www.ycombinator.com/companies/gooseworks/jobs/rfgY8La-founding-creative-engineer)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 2 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 3 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 4 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 5 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 6 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 7 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 8 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 9 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 10 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 11 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 12 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 13 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 14 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 15 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 16 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 17 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 18 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 19 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 20 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 21 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 22 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 23 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 24 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 25 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 26 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 27 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 28 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 29 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 30 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 31 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 32 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 33 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 34 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 35 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 36 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 37 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 38 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 39 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 40 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 41 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 42 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 43 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 44 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 45 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 46 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 47 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 48 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 49 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 50 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 51 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 52 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 53 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 54 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 55 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 56 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 57 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 58 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 59 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 60 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 61 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 62 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 63 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 64 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 65 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 66 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 67 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 68 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 69 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 70 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 71 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 72 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 73 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 74 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 75 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 76 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 77 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 78 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 79 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 80 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 81 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 82 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 83 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 84 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 85 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 86 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 87 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 88 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 89 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 90 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 91 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 92 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 93 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 94 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 95 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 96 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 97 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 98 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 99 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 100 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 101 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 102 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 103 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 104 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 105 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 106 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 107 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 108 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 109 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 110 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 111 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 112 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 113 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 114 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 115 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 116 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 117 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 118 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 119 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 120 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 121 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 122 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 123 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 124 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 125 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 126 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 127 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 128 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 129 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 130 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 131 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 132 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 133 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 134 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 135 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 136 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 137 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 138 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 139 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 140 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 141 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 142 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 143 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 144 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 145 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 146 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 147 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 148 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 149 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 150 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 151 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 152 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 153 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 154 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 155 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 156 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 157 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 158 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 159 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 160 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 161 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 162 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 163 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 164 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 165 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 166 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 167 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 168 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 169 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 170 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 171 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 172 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 173 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 174 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 175 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 176 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 177 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 178 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 179 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 180 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 181 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 182 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 183 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 184 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 185 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 186 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 187 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 188 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 189 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 190 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 191 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 192 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 193 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 194 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 195 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 196 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 197 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 198 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 199 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 200 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 201 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 202 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 203 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 204 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 205 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 206 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 207 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 208 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 209 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 210 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 211 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 212 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 213 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 214 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 215 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 216 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 217 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 218 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 219 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 220 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 221 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 222 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 223 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 224 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 225 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 226 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 227 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 228 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 229 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 230 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 231 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 232 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 233 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 234 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 235 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 236 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 237 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 238 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 239 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 240 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 241 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 242 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 243 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 244 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 245 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 246 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 247 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 248 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 249 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 250 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 251 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 252 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 253 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 254 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 255 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 256 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 257 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 258 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 259 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 260 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 261 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 262 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 263 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 264 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 265 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 266 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 267 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 268 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 269 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 270 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 271 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 272 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 273 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 274 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 275 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 276 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 277 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 278 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 279 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 280 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 281 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 282 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 283 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 284 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 285 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 286 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 287 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 288 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 289 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 290 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 291 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 292 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 293 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 294 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 295 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 296 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 297 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 298 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 299 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 300 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 301 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 302 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 303 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 304 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 305 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 306 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 307 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 308 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 309 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 310 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 311 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 312 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 313 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 314 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 315 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 316 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 317 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 318 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 319 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 320 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 321 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 322 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 323 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 324 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 325 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 326 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 327 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 328 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 329 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 330 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 331 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 332 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 333 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 334 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 335 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 336 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 337 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 338 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 339 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 340 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 341 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 342 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 343 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 344 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 345 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 346 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 347 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 348 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 349 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 350 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 351 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 352 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 353 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 354 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 355 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 356 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 357 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 358 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 359 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 360 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 361 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 362 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 363 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 364 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 365 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 366 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 367 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 368 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 369 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 370 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 371 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 372 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 373 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 374 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 375 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 376 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 377 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 378 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 379 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 380 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 381 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 382 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 383 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 384 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 385 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 386 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 387 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 388 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 389 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 390 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 391 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 392 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 393 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 394 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 395 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 396 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 397 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 398 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 399 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 400 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 401 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 402 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 403 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 404 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 405 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 406 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 407 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 408 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 409 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 410 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 411 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 412 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 413 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 414 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 415 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 416 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 417 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 418 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 419 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 420 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 421 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 422 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 423 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 424 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 425 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 426 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 427 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 428 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 429 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 430 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 431 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 432 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 433 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 434 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 435 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 436 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 437 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 438 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 439 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 440 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 441 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 442 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 443 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 444 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 445 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 446 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 447 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 448 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 449 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 450 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 451 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 452 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 453 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 454 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 455 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 456 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 457 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 458 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 459 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 460 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 461 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 462 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 463 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 464 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 465 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 466 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 467 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 468 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 469 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 470 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 471 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 472 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 473 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 474 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 475 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 476 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 477 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 478 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 479 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 480 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 481 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 482 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 483 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 484 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 485 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 486 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 487 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 488 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 489 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 490 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 491 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 492 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 493 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 494 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 495 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 496 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 497 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 498 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 499 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 500 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 501 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 502 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 503 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 504 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 505 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 506 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 507 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 508 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 509 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 510 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 511 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 512 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 513 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 514 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 515 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 516 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 517 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 518 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 519 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 520 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 521 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 522 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 523 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 524 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 525 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 526 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 527 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 528 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 529 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 530 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
