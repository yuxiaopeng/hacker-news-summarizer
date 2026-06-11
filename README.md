# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-11.md)

*最后自动更新时间: 2026-06-11 20:04:19*
## 1. 以“受制裁”代码污染 Linux 内核

**原文标题**: Spoiling Linux Kernel with "sanctioned" code

**原文链接**: [https://printserver.ink/blog/spoiling-the-kernel/](https://printserver.ink/blog/spoiling-the-kernel/)

文章《以“受制裁”代码破坏 Linux 内核》探讨了国际地缘政治制裁如何在开源社区内部制造法律障碍。

作者是一位使用 .ru（俄罗斯）域名的开发者，他编写了一个补丁，旨在修复 Linux 内核 OHCI (USB 1.1) 协议栈中一个长期存在的延迟漏洞。尽管该修复方案在技术上是完善的，但却遭到了包括 Greg Kroah-Hartman 在内的核心维护者的冷遇。作者认为，这是由于法律建议警告维护者不要与来自受制裁地区（如俄罗斯、伊朗和朝鲜）的贡献者进行交流，除非这些人能证明自己不隶属于受制裁实体。

作者指出，这种动态以类似于专利侵权的方式“破坏”了 Linux 内核。一旦受制裁国家的贡献者提交了高质量的漏洞修复程序，该特定实现方案就在法律上被“投毒”了。由于社区无法接受来自受制裁来源的代码，而其他开发者也被禁止简单地以自己的名义重新提交或重复使用该特定代码，这导致内核实际上无法采用最直接的问题解决方案。

因此，为了规避法律责任，社区被迫寻找其他效率可能较低的替代方案来修复同样的漏洞。作者总结道，这营造了一种“有罪推定”的环境，即贡献者的来源背景超过了其技术价值，最终阻碍了 Linux 内核的发展。

---

## 2. 游戏机上的网页浏览器

**原文标题**: Web Browsers on Video Game Consoles

**原文链接**: [https://vale.rocks/posts/game-console-browsers](https://vale.rocks/posts/game-console-browsers)

本文探讨了视频游戏机官方网络浏览器的演变，强调了它们早期作为非技术用户经济型互联网入口的作用。

这段历程始于1995年的飞利浦（Philips）CD-i，它提供了一种初步的“简化版互联网”体验。然而，由于内存有限，浏览网页往往会覆盖系统内存，甚至包括游戏存档。1996年，世嘉土星（Sega Saturn）推出了配有PlanetWeb浏览器的Net Link。这是一个重大进步，因为它专门针对电视屏幕进行了优化，支持抗锯齿字体，并具有通过电子邮件发送游戏存档和参与IRC聊天等独特功能。

其他早期尝试还包括苹果万代（Apple Bandai）的Pippin，它运行的是经过“Pippin化”处理的桌面浏览器版本（如Netscape和Internet Explorer）。尽管具备技术实力，但Pippin因成本过高而在商业上宣告失败。任天堂（Nintendo）早期的尝试则更为受限：仅在日本发行的64DD提供了Randnet服务，而Game Boy Color提供的浏览器功能极其有限，只能以黑白形式访问任天堂官方网站。

世嘉Dreamcast标志着早期游戏机浏览器的巅峰，它拥有三个独特的地区版本：Dream Passport（日本）、PlanetWeb（美国）和Dreamkey（欧洲）。通过多次迭代，这些浏览器最终支持了Flash、JavaScript和Java小程序等现代标准。世嘉甚至尝试过小众营销，例如Hello Kitty主题浏览器和“家庭主妇上网”套装。

最后，文章总结道，这些浏览器的发展为我们提供了一个独特的窗口，以此窥见万维网的“稚嫩”时代以及游戏机用户界面的成熟过程。

---

## 3. 变革电源的不是苹果，而是新型晶体管。

**原文标题**: Apple didn't revolutionize power supplies; new transistors did

**原文链接**: [https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html](https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html)

史蒂夫·乔布斯在其传记中声称，罗德·霍尔特（Rod Holt）为 Apple II 设计的开关电源是一项革命性的发明，现代计算机至今仍在“抄袭”这一设计。本文反驳了这一说法，认为电源领域的真正革命是由半导体技术的进步驱动的，而非苹果的设计。

虽然开关电源（SMPS）比传统的线性电源更高效、更小巧、更轻便，但它们并非苹果的发明。这项技术早在 20 世纪 30 年代就已出现，并在 60 年代和 70 年代初期被美国航天局（NASA）、IBM、惠普（HP）和数字设备公司（DEC）广泛使用。到 1977 年 Apple II 发布时，开关电源在小型机、彩色电视以及 Boschert Inc. 等公司的商业产品中已经非常普遍。

作者指出，行业转型的真正催化剂是高压高速开关晶体管的改进，以及 1976 年集成电路（IC）控制器的问世。这些组件简化了开关电源的设计，并使其更具成本效益。

尽管罗德·霍尔特为苹果设计的电源因其创新性（具有交流启动机制和特定的钳位绕组）而获得了专利，但这些特性并未成为行业标准。事实上，行业转向了脉冲宽度调制（PWM）控制器 IC，而苹果在采用这一技术方面实际上动作迟缓，直到 20 世纪 90 年代仍在使用分立元件。最终，现代电源是基于不同的原理和 IC 驱动架构，而非霍尔特的特定电路。Apple II 的电源是对现有趋势的一次成功应用，但它并没有发明支撑当今计算机运行的技术。

---

## 4. OpenAI 拟大幅降价以与 Anthropic 争夺用户

**原文标题**: OpenAI mulls slashing prices as it competes with Anthropic for users

**原文链接**: [https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html)

据报道，OpenAI 正考虑大幅下调其人工智能模型的价格，以更好地与竞争对手 Anthropic 竞争。据《华尔街日报》报道，OpenAI 计划降低“token”（用于 AI 使用计费的单位）的成本，以应对 Anthropic 预期的降价举措。

此举正值两家公司竞争加剧之际，双方近期均已提交了首次公开募股（IPO）申请。尽管 OpenAI 长期以来一直是市场领导者，但 Anthropic 的估值近期达到了 9650 亿美元，略高于 OpenAI 在 3 月份 8520 亿美元的估值。目前，OpenAI 对其 GPT-5.5 模型的阶梯订阅费用从每月 8 美元到 100 多美元不等，而 Anthropic 提供的 Claude Pro 服务每月为 17 美元（按年订阅），并设有高端的 Claude Max 档位。

尽管面临定价压力，OpenAI 仍展现出巨大的规模优势。今年 5 月，ChatGPT 成为首个达到 10 亿月活跃用户的应用，仅用三年时间就达成了这一里程碑，增长速度超越了谷歌地图等此前的纪录保持者。这场潜在的价格战标志着 AI 行业进入了一个新阶段，市场份额的争夺不仅取决于技术创新，也取决于激进的定价策略。

---

## 5. 从零构建基础 AI 智能体：长任务规划

**原文标题**: Build a Basic AI Agent from Scratch: Long Task Planning

**原文链接**: [https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d](https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d)

在《从零开始构建基础 AI 智能体：长任务规划》中，Roger Oriol 探讨了对话式 AI 智能体在处理复杂、多步骤项目时的局限性。由于大语言模型（LLM）通常针对短文本交互进行了优化，它们往往难以持续关注长期目标。为了解决这一问题，Oriol 引入了一个以两个新工具为核心的自主规划框架：**草稿垫（Scratchpad）**和**待办事项列表（To-do list）**。

**草稿垫**作为一个私有的内存工作区，智能体可以在其中重申目标、梳理现有知识、评估多种方案并预判潜在的失败模式。这种“思维链”过程确保智能体在执行任何行动之前，先对其策略进行逻辑推理。**待办事项列表**则使智能体能够将项目分解为具体步骤并跟踪其状态（如：待处理、进行中、已失败）。该工具强制执行结构化的工作流，包括针对失败任务的重试限制，以及同一时间只能激活一个任务的规则。

该系统的核心组成部分是**经过优化的系统提示词**，它要求智能体：
1. **规划与跟踪：** 分解任务并在每一步之后更新待办事项列表。
2. **重新规划：** 在草稿垫中诊断错误，并在结果偏离预期时调整方向或重试。
3. **验证完成情况：** 使用由三部分组成的“完成检测”流程——验证结构性完成情况、根据原始目标检查输出（如运行测试），以及对未验证的假设进行“不确定性检查”。

通过整合这些规划工具和严谨的系统提示词，智能体从一个简单的聊天机器人演变成了一个能够执行代码库迁移等复杂自主项目的得力助手。

---

## 6. 热力学主宰未来轨道数据中心

**原文标题**: Thermodynamics rules future orbital data centers

**原文链接**: [https://spectrum.ieee.org/orbital-data-centers-heat](https://spectrum.ieee.org/orbital-data-centers-heat)

While tech giants like Nvidia, SpaceX, and Google are racing to establish orbital data centers, a report from ABI Research suggests that the harsh reality of thermodynamics makes space-based computing significantly more difficult and expensive than terrestrial alternatives.

The primary obstacle is **cooling**. In the vacuum of space, conduction and convection are impossible; heat can only be dissipated through radiation. Governed by the Stefan-Boltzmann Law, this creates a "physics tax" where high-power AI chips require massive radiator surface areas. For example, a single 40-kilowatt server rack would require a radiator the size of a pickleball court. Furthermore, exposure to UV light and atomic oxygen degrades these radiators, requiring a 40% increase in launch mass to ensure end-of-life functionality.

Beyond cooling, **ionizing radiation** poses a threat to the "soft" commercial chips (like Nvidia H100s) necessary for AI. To survive, satellites must use heavy shielding or expensive redundancy, driving the total cost of ownership at least ten times higher than Earth-based data centers. Additionally, while solar energy is abundant, every watt of power generated requires a corresponding watt of heat rejection, doubling the structural burden.

Despite these challenges, space-based computing has "killer apps" in niche markets. Processing data directly on Earth-observation satellites can bypass downlink bottlenecks, and onboard AI is becoming essential for real-time collision avoidance in increasingly crowded orbits. To make larger-scale deployment feasible, the industry is exploring innovative designs like origami-inspired folding radiators and liquid-droplet cooling. Ultimately, while the "physics tax" remains high, the need for immediate, localized insight in orbit ensures that space computing remains a critical, albeit difficult, frontier.

---

## 7. CSS: Unavoidable Bad Parts

**原文标题**: CSS: Unavoidable Bad Parts

**原文链接**: [https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html](https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html)

生成摘要时出错

---

## 8. US House rejects FISA Section 702 extension, warrantless surveillance expires

**原文标题**: US House rejects FISA Section 702 extension, warrantless surveillance expires

**原文链接**: [https://www.axios.com/2026/06/11/fisa-section-702-expiration-pulte-trump-johnson](https://www.axios.com/2026/06/11/fisa-section-702-expiration-pulte-trump-johnson)

生成摘要时出错

---

## 9. Google is finally killing uBlock Origin in Chrome for good

**原文标题**: Google is finally killing uBlock Origin in Chrome for good

**原文链接**: [https://protonprivacy.substack.com/p/google-is-finally-killing-ublock](https://protonprivacy.substack.com/p/google-is-finally-killing-ublock)

生成摘要时出错

---

## 10. Oh good, screwworms are back (2025)

**原文标题**: Oh good, screwworms are back (2025)

**原文链接**: [https://www.marginallycompelling.com/p/oh-good-screwworms-are-back](https://www.marginallycompelling.com/p/oh-good-screwworms-are-back)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 2 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 3 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 4 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 5 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 6 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 7 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 8 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 9 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 10 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 11 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 12 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 13 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 14 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 15 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 16 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 17 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 18 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 19 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 20 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 21 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 22 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 23 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 24 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 25 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 26 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 27 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 28 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 29 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 30 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 31 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 32 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 33 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 34 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 35 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 36 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 37 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 38 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 39 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 40 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 41 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 42 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 43 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 44 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 45 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 46 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 47 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 48 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 49 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 50 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 51 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 52 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 53 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 54 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 55 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 56 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 57 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 58 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 59 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 60 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 61 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 62 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 63 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 64 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 65 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 66 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 67 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 68 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 69 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 70 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 71 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 72 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 73 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 74 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 75 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 76 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 77 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 78 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 79 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 80 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 81 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 82 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 83 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 84 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 85 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 86 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 87 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 88 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 89 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 90 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 91 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 92 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 93 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 94 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 95 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 96 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 97 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 98 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 99 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 100 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 101 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 102 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 103 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 104 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 105 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 106 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 107 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 108 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 109 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 110 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 111 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 112 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 113 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 114 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 115 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 116 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 117 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 118 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 119 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 120 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 121 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 122 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 123 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 124 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 125 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 126 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 127 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 128 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 129 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 130 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 131 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 132 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 133 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 134 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 135 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 136 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 137 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 138 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 139 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 140 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 141 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 142 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 143 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 144 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 145 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 146 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 147 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 148 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 149 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 150 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 151 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 152 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 153 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 154 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 155 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 156 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 157 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 158 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 159 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 160 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 161 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 162 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 163 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 164 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 165 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 166 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 167 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 168 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 169 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 170 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 171 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 172 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 173 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 174 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 175 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 176 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 177 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 178 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 179 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 180 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 181 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 182 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 183 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 184 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 185 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 186 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 187 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 188 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 189 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 190 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 191 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 192 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 193 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 194 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 195 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 196 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 197 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 198 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 199 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 200 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 201 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 202 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 203 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 204 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 205 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 206 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 207 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 208 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 209 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 210 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 211 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 212 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 213 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 214 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 215 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 216 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 217 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 218 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 219 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 220 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 221 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 222 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 223 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 224 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 225 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 226 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 227 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 228 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 229 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 230 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 231 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 232 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 233 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 234 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 235 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 236 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 237 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 238 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 239 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 240 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 241 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 242 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 243 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 244 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 245 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 246 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 247 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 248 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 249 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 250 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 251 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 252 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 253 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 254 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 255 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 256 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 257 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 258 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 259 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 260 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 261 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 262 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 263 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 264 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 265 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 266 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 267 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 268 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 269 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 270 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 271 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 272 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 273 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 274 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 275 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 276 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 277 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 278 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 279 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 280 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 281 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 282 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 283 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 284 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 285 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 286 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 287 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 288 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 289 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 290 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 291 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 292 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 293 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 294 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 295 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 296 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 297 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 298 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 299 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 300 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 301 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 302 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 303 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 304 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 305 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 306 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 307 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 308 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 309 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 310 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 311 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 312 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 313 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 314 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 315 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 316 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 317 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 318 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 319 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 320 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 321 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 322 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 323 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 324 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 325 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 326 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 327 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 328 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 329 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 330 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 331 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 332 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 333 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 334 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 335 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 336 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 337 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 338 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 339 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 340 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 341 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 342 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 343 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 344 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 345 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 346 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 347 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 348 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 349 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 350 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 351 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 352 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 353 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 354 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 355 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 356 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 357 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 358 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 359 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 360 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 361 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 362 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 363 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 364 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 365 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 366 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 367 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 368 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 369 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 370 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 371 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 372 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 373 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 374 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 375 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 376 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 377 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 378 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 379 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 380 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 381 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 382 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 383 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 384 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 385 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 386 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 387 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 388 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 389 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 390 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 391 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 392 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 393 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 394 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 395 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 396 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 397 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 398 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 399 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 400 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 401 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 402 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 403 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 404 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 405 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 406 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 407 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 408 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 409 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 410 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 411 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 412 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 413 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 414 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 415 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 416 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 417 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 418 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 419 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 420 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 421 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 422 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 423 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 424 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 425 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 426 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 427 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 428 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 429 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 430 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 431 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 432 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 433 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 434 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 435 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 436 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 437 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 438 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 439 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 440 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 441 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 442 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 443 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 444 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 445 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 446 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 447 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 448 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
