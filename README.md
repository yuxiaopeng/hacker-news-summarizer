# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-11.md)

*最后自动更新时间: 2025-07-11 17:49:29*
## 1. 每天在 Quad9 递归解析器阵列上发现的热门 DNS 域名

**原文标题**: Top DNS domains seen on the Quad9 recursive resolver array each day

**原文链接**: [https://github.com/Quad9DNS/quad9-domains-top500](https://github.com/Quad9DNS/quad9-domains-top500)

本文档描述了 "quad9-domains-top500" 数据，这是一个每日更新的列表，列出了 Quad9 递归解析器中最常查询的 500 个域名。它反映了 Quad9 基础设施内观察到的 DNS 活动快照。

主要要点包括：

*   **目的：** 该列表反映了 Quad9 解析器上最常请求的域名。
*   **排除项：** 顶级域名 (TLD) 被排除在外。
*   **注意事项：** 该列表并非简单的受欢迎程度竞赛。排名靠前可能源于 CDN 使用、激进型应用程序、反病毒校验和或糟糕的 DNS TTL 管理等因素。Quad9 尝试阻止 DNS 隧道，但可能无法检测到所有方法。TTL 也未纳入考量，因此缓存的域名可能不会出现。
*   **数据收集：** 该列表源自 Quad9 服务器子集上查询响应的统计样本。
*   **解读：** 排名靠前并不一定等同于受欢迎程度；它可能表明存在诸如低效 DNS 管理之类的问题。
*   **联系方式：** 有关数据的疑问，请发送至 support@quad9.net。

---

## 2. 展示 HN：Vibe Kanban – 用于管理你的 AI 编码代理的看板

**原文标题**: Show HN: Vibe Kanban – Kanban board to manage your AI coding agents

**原文链接**: [https://github.com/BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)

Vibe Kanban：旨在简化 Claude Code、Gemini CLI、Codex 和 Amp 等 AI 编码代理管理的看板。它旨在通过提供用于规划、审查和编排任务的中心化平台，帮助那些花费越来越多时间来编排 AI 代码生成的工程师。

主要功能包括：

*   **代理切换：** 轻松切换不同的编码代理。
*   **任务编排：** 并行或顺序执行多个编码代理。
*   **审查和执行：** 快速审查工作并启动开发服务器。
*   **任务跟踪：** 跟踪分配给编码代理的任务状态。
*   **配置管理：** 集中管理编码代理 MCP 配置。

验证所需的编码代理后，可以使用 `npx vibe-kanban` 安装此工具。 文档和支持分别可在网站和 GitHub issues 上找到。 欢迎贡献，但在提交 pull request 之前应与核心团队讨论。

开发环境需要 Rust、Node.js 和 pnpm。运行 `pnpm run dev` 会启动带有实时重新加载的前端和后端。可以通过运行 `build-npm-package.sh` 然后在 `npx-cli` 文件夹中运行 `npm pack` 来创建构建。 可以使用 `npx [GENERATED FILE].tgz` 运行构建的包。

---

## 3. 比尔·阿特金森的迷幻用户界面

**原文标题**: Bill Atkinson's psychedelic user interface

**原文链接**: [https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill](https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill)

无法访问文章链接。

---

## 4. 天文学家竞相研究星际闯入者

**原文标题**: Astronomers race to study interstellar interloper

**原文链接**: [https://www.science.org/content/article/astronomers-race-study-interstellar-interloper](https://www.science.org/content/article/astronomers-race-study-interstellar-interloper)

无法访问文章链接。

---

## 5. 重新贴膜你的MacBook

**原文标题**: Repaste Your MacBook

**原文链接**: [https://christianselig.com/2025/07/repaste-macbook/](https://christianselig.com/2025/07/repaste-macbook/)

2025年7月，作者详述了自己为解决日益严重的风扇噪音问题，而重新为老化的M1 Pro MacBook Pro涂抹散热硅脂的经历。风扇噪音的常见原因是散热硅脂干涸。虽然笔记本性能依旧良好，但在编译代码和视频编辑等高强度任务期间，风扇噪音变得令人难以忍受。

作者参考iFixit指南，用Noctua NT-H2替换了CPU散热硅脂。他们发现苹果公司为RAM芯片使用了特殊的“碳黑”化合物，由于其独特的性能和难以采购，因此决定不更换。

过程并非一帆风顺。作者不幸撕裂了脆弱的风扇电缆，需要更换。更换风扇重新组装后，Touch ID传感器电缆也被撕裂，导致Touch ID功能无法使用，而且很可能在Apple Store维修费用高昂。

尽管遭遇这些挫折，重新涂抹硅脂仍然奏效。 Cinebench测试表明，最高CPU温度降低（102°C降至96°C），最大风扇转速显著降低（6,300 RPM降至4,700 RPM），同时保持了相似的性能得分。笔记本电脑的空闲温度也降低了。

作者总结说，虽然拆卸过程可以控制，但电缆的脆弱性使其具有风险。他们建议没有小型电子设备维修经验的人不要尝试，但建议有经验的用户或通过维修店进行维修，如果MacBook使用了几年。散热性能和噪音的改善是有益的，但Touch ID功能的潜在损失是一个重要的考虑因素。

---

## 6. 姜黄是全球铅中毒谜案的罪魁祸首 (2024)

**原文标题**: Turmeric is the culprit in a global lead poisoning mystery (2024)

**原文链接**: [https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh](https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh)

20世纪80年代，为了使姜黄根更具吸引力，孟加拉国的一些农民开始添加铬酸铅，一种通常用于工业涂料的有毒黄色颜料。这种做法最初是为了解决洪水造成的变色问题，后来由于颜色鲜艳的姜黄更容易销售而变得普遍。这种广泛的污染导致了一场全球健康危机，影响了孟加拉国的孕妇和儿童，甚至纽约市的孟加拉社区。

由纽约市卫生侦探和一位名叫Jenna Forsyth的加州博士生牵头的铅中毒调查显示，姜黄是罪魁祸首。 Forsyth的研究源于孟加拉国农村孕妇体内惊人的高铅水平，并将源头追溯到掺铅姜黄。

2019年，孟加拉国食品安全局迅速做出回应。他们发布了公共警告，分发了信息传单，与农民和磨坊主举办了研讨会，甚至设立了“流动法庭”没收受污染的姜黄并对供应商处以罚款。 结果，姜黄样品中的铅污染率从47%骤降至0%，当地农民和孕妇的血铅水平也显着降低。 该案例突显了铅中毒的破坏性影响以及在解决此类危机时迅速、果断行动的有效性。

---

## 7. 报告称，英国邮局丑闻致至少13人自杀身亡。

**原文标题**: At Least 13 People Died by Suicide Amid U.K. Post Office Scandal, Report Says

**原文链接**: [https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html](https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html)

无法访问文章链接。

---

## 8. 以半价升级 M4 Pro Mac mini 的存储

**原文标题**: Upgrading an M4 Pro Mac mini's storage for half the price

**原文链接**: [https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price](https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price)

本文详细介绍了使用 M4-SSD 的 DIY 套件升级 M4 Pro Mac mini 内部存储的过程。作者将一台 Mac mini 从 512GB 升级到 4TB，并在视频中记录了整个过程。虽然物理升级相对简单，只需要基本的笔记本电脑硬件技能，但拆卸后部塑料盖可能比较棘手。

一个关键方面是升级后需要进行 DFU (设备固件更新) 恢复。作者明确指出，DFU 恢复不仅可以用 Apple Silicon Mac 进行，也可以用许多配备 T2 芯片的 Intel Mac 进行。 这涉及到连接到 Mac mini 的 Thunderbolt 端口并在开机时按住电源按钮。

性能测试比较了升级后的内部 SSD 与外部 Thunderbolt 5 NVMe 硬盘盒。升级后的 4TB 内部模块显示出明显更好的写入速度，因为其具有更多的闪存芯片。 外部驱动器虽然速度很快，但偶尔会出现速度下降的情况，这可能是由于 DRAM 缓存的限制。

文章最后总结说，虽然 699 美元的 M4 Pro 4TB SSD 升级套件与标准 NVMe SSD 相比价格昂贵，但它比苹果公司提供的相同容量的 1200 美元的升级便宜得多。作者强调了内部存储的稳定速度和可靠性。

---

## 9. 吴恩达：用人工智能加速构建 [视频]

**原文标题**: Andrew Ng: Building Faster with AI [video]

**原文链接**: [https://www.youtube.com/watch?v=RNJCfif1dPY](https://www.youtube.com/watch?v=RNJCfif1dPY)

这似乎是吴恩达在YouTube上发布的视频列表，标题为“利用人工智能加速构建”。然而，提供的“内容”部分只是YouTube通用的页脚信息（版权、条款、隐私等），不包含关于视频实际内容的任何信息。

因此，无法给出恰当的总结。根据标题推测，该视频可能讨论如何利用人工智能来加速或改进构建过程，可能是在软件开发、机器学习模型，甚至物理建造的背景下。在没有更多来自视频本身的细节的情况下，总结只能局限于这种猜测。

---

## 10. 宾州众议院通过“一键取消”订阅法案

**原文标题**: Pa. House passes 'click-to-cancel' subscription bills

**原文链接**: [https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html](https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html)

宾夕法尼亚州众议院通过两项法案，旨在打击欺骗性订阅行为，与近期被联邦上诉法院驳回的联邦法规类似。第一项法案打击“否定选择”协议，即消费者在未主动选择退出服务的情况下被自动注册。该法案由众议员丽莎·博罗夫斯基发起，规定续订前必须发出通知，并要求消费者能够以与订阅相同的方式取消订阅。第二项法案由众议员乔·奇雷西发起，规定在线订阅必须可以在线取消，并明确显示续订和取消信息。

该州立法旨在解决消费者在取消订阅时遇到的困难，奇雷西众议员表示他的选民和家人都经历过这个问题。虽然一些企业最初抵制，但奇雷西强调，其目标是帮助消费者，而不是损害企业。

这些法案不包括受公共事业委员会、联邦通信委员会和健身房监管的服务（尽管这可能会被修改）。尽管联邦层面遭遇挫折，宾夕法尼亚州希望加入纽约、加利福尼亚、明尼苏达、田纳西和弗吉尼亚等其他州，制定类似的消费者保护政策。这些法案以两党支持获得通过，目前正等待州参议院的审议以及州长乔什·夏皮罗的签署。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 2 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 3 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 4 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 5 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 6 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 7 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 8 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 9 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 10 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 11 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 12 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 13 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 14 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 15 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 16 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 17 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 18 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 19 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 20 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 21 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 22 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 23 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 24 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 25 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 26 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 27 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 28 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 29 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 30 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 31 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 32 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 33 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 34 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 35 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 36 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 37 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 38 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 39 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 40 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 41 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 42 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 43 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 44 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 45 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 46 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 47 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 48 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 49 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 50 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 51 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 52 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 53 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 54 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 55 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 56 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 57 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 58 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 59 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 60 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 61 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 62 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 63 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 64 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 65 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 66 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 67 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 68 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 69 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 70 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 71 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 72 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 73 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 74 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 75 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 76 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 77 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 78 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 79 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 80 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 81 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 82 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 83 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 84 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 85 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 86 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 87 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 88 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 89 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 90 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 91 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 92 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 93 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 94 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 95 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 96 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 97 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 98 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 99 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 100 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 101 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 102 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 103 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 104 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 105 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 106 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 107 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 108 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 109 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 110 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 111 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 112 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 113 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 114 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
