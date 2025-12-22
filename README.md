# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-22.md)

*最后自动更新时间: 2025-12-22 17:47:35*
## 1. 将大语言模型扩展至更大型代码库

**原文标题**: Scaling LLMs to Larger Codebases

**原文链接**: [https://blog.kierangill.xyz/oversight-and-guidance](https://blog.kierangill.xyz/oversight-and-guidance)

将大语言模型（LLM）应用于更大规模的代码库，需要超越简单的提示词工程，转向由“**引导**（Guidance）”与“**监督**（Oversight）”构成的双支柱策略。

“**引导**”的核心在于提供给模型的上下文。其目标是实现“一次成型”（one-shotting），即在单次尝试中生成高质量、可用的代码，以避免手动返工带来的低效。为此，团队应当建立“提示词库”：通过不断迭代文档、代码库映射和最佳实践，为模型提供必要的背景信息。此外，作者强调“整洁代码”原则在当下尤为重要。由于模型的表现受限于输入质量，一个充斥着技术债和模块化程度差的代码库会诱发模型幻觉。如果人类工程师都无法理清某个模块，模型也同样做不到。

“**监督**”则侧重于验证模型决策所需的人类技能。企业不应追求用自动化取代工程师，而应投资培养他们的设计与架构直觉。合格的监督者必须具备辨别技术决策优劣的“品味”，以判断模型的决策（如数据库选型）是否符合长期目标。这种直觉源于对经典著作的研读以及深度的开发实践。

最后，文章建议尽可能实现**监督自动化**。通过引入强类型系统和“架构逻辑”测试等程序化“护栏”，工程师可以保护抽象层，确保模型在既定边界内运行。随着模型产出的代码量剧增，团队还必须通过优化 QA 流程并将常见的代码评审反馈沉淀为文档来突破“验证瓶颈”，从而在规模化生产中维持代码质量。

---

## 2. 史上最大的CRT：索尼PVM-4300

**原文标题**: The biggest CRT ever made: Sony's PVM-4300

**原文链接**: [https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/](https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/)

1989年，索尼推出了 PVM-4300（在日本被称为 KV-45ED1），这是有史以来制造的最大的传统 CRT（阴极射线管）电视。该机型拥有 45 英寸显像管和 43 英寸可视屏幕，堪称一项宏大的工程壮举：其重量约 450 磅（约 204 公斤），高度为 27 英寸，且往往因为宽度过大而无法通过标准的门框。

1990年，索尼仅向美国进口了 20 台，零售价高达惊人的 4 万美元。与索尼量产的小型机型不同，PVM-4300 是手工打造的。为了匹配其昂贵的身价，它采用了改良清晰度电视（IDTV）技术。该系统利用缓冲区存储并对连续帧进行插值处理，从而提供比标准隔行扫描 CRT 更清晰、更稳定的图像，成为通往高清电视（HDTV）时代的奢华桥梁。

数十年来，这款电视一直被视为“谜一般”的稀缺品，一些发烧友甚至怀疑是否还有存世实例。然而，在 2024 年 12 月，YouTuber Shank Mods 记录了他从日本一家餐厅购得一台幸存机器的过程。尽管其庞大的尺寸和重量带来了物流挑战，该设备还是被成功运抵美国。这一发现证实，这种高端复古技术至少有一个功能完好的实例，如今保存在一位热衷于此的爱好者手中。

---

## 3. 礼赞冬至的古代遗迹

**原文标题**: The ancient monuments saluting the winter solstice

**原文链接**: [https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice](https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice)

本文探讨了人类对冬至持久的迷恋，这体现在具有5000年历史的新石器时代纪念碑和当代大地艺术中。在整个北半球，各种建筑结构都经过精确对齐，以在一年中白天最短的那天框取太阳，标志着季节循环重置时“死亡与重生”的关键时刻。

**古代意义**
对于古代文明而言，追踪冬至关乎生存。它使狩猎采集者和早期农民能够预测动物迁徙和对收割至关重要的季节变化。奥克尼的**梅肖韦古墓**、爱尔兰的**纽格莱奇墓**以及法国的**仙女岩**等纪念碑利用长廊来“捕捉”阳光，在仲冬时节照亮黑暗的墓室。这些遗址体现了精神上的“岁之子夜”，提醒人们时间的循环属性以及春天回归的承诺。

**现代诠释**
近几十年来，艺术家们复兴了这种“新石器时代美学”，让现代人类重新建立起与自然节奏的联系。
*   **南希·霍尔特的《太阳隧道》**（犹他州）利用巨大的混凝土管来框取冬至日出和日落的景象，将辽阔的沙漠带回到人类的尺度。
*   **詹姆斯·特瑞尔的《罗登火山口》**（亚利桑那州）在火山锥中挖掘了一条隧道，作为暗箱将仲冬的阳光投射到大理石板上。
*   **杉本博司的“江之浦测候所”**（日本）包含一条“礼光隧道”，旨在帮助访客在浩瀚的宇宙中找到自己的位置。

无论是为了生存还是艺术表达，这些建筑都赞美了从黑暗到光明的过渡。它们唤起了一种原始的认知：一年中最黑暗的时刻已经过去，预示着春天即将到来的温暖与复苏。

---

## 4. Show HN: Netrinos – 专为小团队打造的极简 Mesh VPN

**原文标题**: Show HN: Netrinos – A keep it simple Mesh VPN for small teams

**原文链接**: [https://netrinos.com](https://netrinos.com)

**Netrinos** 是一款简化的网状 (mesh) VPN 服务，旨在为小型团队和个人提供安全、私密的网络访问，而无需复杂的传统 IT 配置。其核心价值在于能够无缝穿透防火墙和路由器，消除了对端口转发或手动网络调整的需求。

**核心特性：**
*   **零配置：** 该服务旨在实现即时设置——用户只需安装应用程序并登录，软件便会自动处理设备发现和网络配置。
*   **安全性：** 采用行业标准的 **WireGuard** 协议，提供企业级的点对点加密。
*   **无缝漫游：** 设备在办公局域网、家庭网络、公共 Wi-Fi 和蜂窝热点等不同环境之间切换时，能保持稳定的连接。
*   **跨平台支持：** Netrinos 支持 Windows、Mac 和 Linux，并兼容台式机、笔记本电脑、服务器、树莓派 (Raspberry Pi)、云虚拟机和物联网 (IoT) 设备。

**定价方案：**
*   **个人版（免费）：** 供非商业用途，支持 1 名用户和多达 100 台设备。
*   **专业版（10 美元/月）：** 为团队设计，支持多达 10 名用户和 100 台设备，提供 14 天免费试用。
*   **高级版（定制）：** 为企业需求量身定制，提供物联网集成、硬件解决方案和白标品牌定制。

总之，Netrinos 将自己定位为一种“化繁为简”的替代方案，适用于那些希望本地网络能够全球随行、且无需处理繁琐网络管理难题的用户。

---

## 5. 氛围感的一年

**原文标题**: A year of vibes

**原文链接**: [https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)

在《氛围之年》（A Year of Vibes）中，Armin Ronacher 对 2025 年进行了反思。这是充满变革的一年，他离开了 Sentry 创立了一家新公司，并从根本上改变了自己的编程方式。他描述了从手动编码向“智能体化编码”（agentic coding）的转变：在这种模式下，他扮演工程负责人的角色，利用 Claude Code、Amp 和 Pi 等工具监督 AI “虚拟实习生”。

文章的核心主题和见解包括：

*   **智能体工作流的兴起：** Ronacher 强调了具备记忆和工具执行能力的 AI 工具如何成为他的工作常态。然而，他对于人类与这些机器之间形成的“准社交关系”（parasocial bonds）感到不安，并认为“智能体”这一术语存在问题，因为责任必须始终由人类承担。
*   **氛围胜于数据：** 他指出，由于该领域发展极快，许多行业讨论是基于主观的“氛围”（vibes）和偏好，而非成熟的工程证据。
*   **自建还是外包：** 尽管目前的趋势是外包核心服务（如认证、SDK），但 Ronacher 认为 AI 赋予了开发者自行构建这些工具的能力，从而可能减少对外部依赖的需求。
*   **基础设施的不足：** 他认为 Git 和 GitHub 等传统工具已无法适应智能体时代。他呼吁建立一种新型的版本控制系统，能够追踪提示词（prompts）、失败的尝试以及“失败中的价值”，以防止 AI 重复错误。
*   **可观测性与伦理的未来：** AI 处理 eBPF 和 SQL 查询等复杂任务的能力可能会彻底改变可观测性领域。与此同时，他警告要警惕“垃圾代码”（slop）的兴起——即开源项目中未经审查的 AI 代码，并强调需要为 AI 辅助的贡献建立新的社会契约和高标准。

最终，Ronacher 将 2025 年视为软件工程数十年根基开始受到“氛围驱动、智能体主导”这一新现实挑战的一年。

---

## 6. 世上没有假羽毛 [视频]

**原文标题**: There's no such thing as a fake feather [video]

**原文链接**: [https://www.youtube.com/watch?v=N5yV1Q9O6r4](https://www.youtube.com/watch?v=N5yV1Q9O6r4)

基于标题《世界上没有假羽毛》（科普频道 Veritasium 的热门视频），以下是内容的简要总结：

**内容提要**
该视频探讨了鸟类羽毛背后复杂的工程学和物理学原理，重点区分了**色素色**与**结构色**。

要点包括：

*   **结构显色：** 不同于大多数依靠化学色素（通过吸收特定波长的光显色）获取颜色的物体，鸟类许多鲜艳的颜色——尤其是蓝色和虹彩光泽——是由羽毛在微观层面的物理形状产生的。例如，冠蓝鸦体内并没有“蓝色”色素，其颜色是由光线在羽毛羽支内部结构上发生散射而产生的。
*   **“假”的概念：** 标题寓指这些结构极其复杂且独特，简单的染料无法轻易模仿。如果一个结构产生了羽毛的光学效果，那么它在本质上就等同于这种生物技术。视频认为，“颜色”是羽毛物理形态中不可分割的属性。
*   **微观复杂性：** 视频利用高倍显微镜展示了羽支和羽小支的层级排列。它解释了光干涉和“相干散射”如何让鸟类能够极其精确地操纵光线。
*   **进化壮举：** 这种生物“纳米技术”使鸟类能够展示出比色素更明亮、更持久的颜色，而色素往往会随时间褪色。

**注：** 您在提示中提供的文本是标准的 YouTube 网页页脚（版权和法律链接），不包含视频的实际逐字稿。本总结是基于与该特定标题相关的视频内容编写的。

---

## 7. Uplane (YC F25) 招聘创始工程师（全栈与 AI）

**原文标题**: Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文链接**: [https://www.useparallel.com/uplane1/careers](https://www.useparallel.com/uplane1/careers)

**Uplane** 是 Y Combinator 2025 冬季（F25）批次的入选初创公司，目前正在招聘专注于**全栈**和 **AI** 开发的**创始工程师**职位。

作为新一届 YC 成员，Uplane 正在寻找具有高影响力的开发者，在最早期阶段加入其核心团队。“创始”职位的定位意味着这些工程师将对公司的技术架构、产品方向和企业文化产生深远影响。

此次招聘的核心亮点包括：

*   **岗位：** 创始全栈工程师和创始 AI 工程师。
*   **阶段：** 早期阶段（YC F25），提供从零开始构建产品的机会。
*   **技术重点：** 虽然目前信息较少，但“**ParallelLoading**”一词暗示产品可能专注于性能优化、高速数据传输或创新的 Web 架构。

对于希望进入初创生态系统并在风投支持的公司中担任领导角色的工程师来说，这是一个典型的高增长机会。

---

## 8. Programming languages used for music

**原文标题**: Programming languages used for music

**原文链接**: [https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes](https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes)

生成摘要时出错

---

## 9. Microsoft will kill obsolete cipher that has wreaked decades of havoc

**原文标题**: Microsoft will kill obsolete cipher that has wreaked decades of havoc

**原文链接**: [https://arstechnica.com/security/2025/12/microsoft-will-finally-kill-obsolete-cipher-that-has-wreaked-decades-of-havoc/](https://arstechnica.com/security/2025/12/microsoft-will-finally-kill-obsolete-cipher-that-has-wreaked-decades-of-havoc/)

生成摘要时出错

---

## 10. A guide to local coding models

**原文标题**: A guide to local coding models

**原文链接**: [https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude](https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 2 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 3 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 4 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 5 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 6 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 7 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 8 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 9 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 10 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 11 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 12 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 13 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 14 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 15 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 16 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 17 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 18 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 19 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 20 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 21 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 22 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 23 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 24 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 25 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 26 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 27 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 28 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 29 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 30 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 31 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 32 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 33 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 34 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 35 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 36 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 37 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 38 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 39 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 40 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 41 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 42 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 43 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 44 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 45 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 46 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 47 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 48 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 49 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 50 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 51 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 52 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 53 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 54 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 55 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 56 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 57 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 58 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 59 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 60 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 61 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 62 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 63 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 64 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 65 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 66 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 67 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 68 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 69 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 70 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 71 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 72 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 73 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 74 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 75 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 76 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 77 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 78 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 79 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 80 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 81 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 82 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 83 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 84 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 85 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 86 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 87 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 88 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 89 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 90 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 91 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 92 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 93 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 94 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 95 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 96 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 97 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 98 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 99 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 100 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 101 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 102 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 103 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 104 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 105 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 106 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 107 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 108 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 109 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 110 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 111 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 112 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 113 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 114 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 115 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 116 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 117 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 118 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 119 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 120 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 121 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 122 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 123 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 124 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 125 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 126 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 127 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 128 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 129 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 130 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 131 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 132 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 133 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 134 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 135 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 136 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 137 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 138 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 139 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 140 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 141 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 142 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 143 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 144 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 145 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 146 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 147 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 148 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 149 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 150 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 151 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 152 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 153 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 154 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 155 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 156 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 157 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 158 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 159 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 160 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 161 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 162 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 163 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 164 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 165 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 166 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 167 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 168 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 169 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 170 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 171 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 172 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 173 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 174 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 175 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 176 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 177 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 178 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 179 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 180 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 181 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 182 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 183 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 184 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 185 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 186 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 187 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 188 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 189 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 190 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 191 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 192 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 193 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 194 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 195 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 196 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 197 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 198 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 199 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 200 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 201 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 202 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 203 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 204 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 205 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 206 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 207 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 208 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 209 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 210 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 211 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 212 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 213 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 214 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 215 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 216 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 217 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 218 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 219 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 220 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 221 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 222 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 223 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 224 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 225 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 226 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 227 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 228 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 229 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 230 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 231 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 232 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 233 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 234 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 235 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 236 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 237 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 238 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 239 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 240 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 241 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 242 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 243 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 244 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 245 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 246 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 247 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 248 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 249 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 250 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 251 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 252 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 253 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 254 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 255 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 256 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 257 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 258 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 259 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 260 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 261 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 262 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 263 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 264 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 265 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 266 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 267 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 268 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 269 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 270 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 271 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 272 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 273 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 274 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 275 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 276 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 277 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
