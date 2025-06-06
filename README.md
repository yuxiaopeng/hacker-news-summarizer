# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-06.md)

*最后自动更新时间: 2025-06-06 17:51:02*
## 1. Meta: 停止你侵入式的AI发现推送。现在。

**原文标题**: Meta: Shut Down Your Invasive AI Discover Feed. Now

**原文链接**: [https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/](https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/)

由于担心侵犯隐私，Mozilla社区呼吁Meta关闭其AI“发现”信息流。他们声称Meta正在悄悄地将私人AI聊天转化为公共内容，而未经用户的明确同意或知情。这模糊了私人和公共交流之间的界限，并使用户隐私面临风险。

Mozilla要求Meta采取以下行动：

*   立即关闭“发现”信息流，直到隐私保护措施得到实施。
*   默认情况下将所有AI互动设为私密，需要明确知情同意才能公开分享。
*   充分透明地披露有多少用户在不知情的情况下分享了私人信息。
*   在所有Meta平台上创建一个通用的、易于使用的退出系统，以防止用户数据被用于AI训练。
*   通知那些对话可能已被公开的用户，并允许他们永久删除其内容。

核心问题是，用户可能认为他们正在进行私人对话，而Meta可能在未经明确同意的情况下将这些互动公开。 Mozilla强调用户需要知道何时在公开场合发言，尤其是在他们期望隐私时。他们鼓励读者签署请愿书，要求Meta解决这些问题，并确保在公开私人对话之前获得明确的自愿同意。

---

## 2. 将 Gitlab 仓库备份时间从 48 小时缩短至 41 分钟

**原文标题**: Decreasing Gitlab repo backup times from 48 hours to 41 minutes

**原文链接**: [https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/](https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/)

GitLab通过解决`git bundle create`命令中低效算法导致的Git扩展性问题，将仓库备份时间从48小时大幅缩短至41分钟。该命令对于创建完整的仓库快照至关重要，但由于`object_array_remove_duplicates()`函数存在O(N²)的复杂度，导致随着引用数量的增长，处理时间呈指数级增长。

GitLab通过火焰图分析确定了瓶颈，并向上游Git贡献了一个修复方案，用更高效的map数据结构替换了嵌套循环。 这种算法的改变极大地提高了性能，在具有大量引用的仓库上进行的基准测试中，速度提高了6倍。

GitLab客户的受益包括大幅缩短备份时间，从而提高了备份频率，通过降低RPO增强了业务连续性，减少了运营开销，并实现了可随不断增长的代码库无缝扩展的面向未来的基础设施。 所有GitLab客户，无论许可证级别如何，都可以从18.0版本开始使用此改进。 这一突破体现了GitLab对可扩展Git基础设施的承诺，并突出了其通过向更广泛的Git社区贡献修复方案的协作方法。

---

## 3. 贝尔实验室成功之道

**原文标题**: Why Bell Labs Worked

**原文链接**: [https://links.fabiomanganiello.com/share/683ee70d0409e6.66273547](https://links.fabiomanganiello.com/share/683ee70d0409e6.66273547)

贝尔实验室为何成功及其魔力难以复制
        
本文探讨了贝尔实验室如此成功的原因以及复制其魔力为何如此困难。文章认为，贝尔实验室的成功源于其开明的管理风格，该风格由亚历山大·格拉汉姆·贝尔创立，并由默文·凯利达到顶峰。这种风格的关键在于吸引有才华的人，为他们提供极大的自由、自主权和支持性环境，然后信任他们的判断和动力。凯利专注于识别具有内在好奇心和动力的人，而不是对他们进行微观管理。

文章将这种方法与当前的学术和企业环境进行了对比，后者的特点是痴迷于指标、文书工作过多以及年轻科学家缺乏自由。这种环境受到MBA文化的驱动，该文化专注于狭隘地定义的生产力和责任制，扼杀了创造力，并阻碍了贝尔实验室所培养的那种长期探索性研究。

作者强调，仅仅靠庞大的资金储备不足以复制贝尔实验室。像谷歌、苹果和微软这样的当代巨头已经在研究上投入了大量资金，但尚未达到同样程度的突破性创新。这是因为贝尔实验室独特的公式包括寻找伟大而有雄心的人，让他们被志同道合的人包围，鼓励交叉融合，并在必要时给予他们思考数年的自由。

最后，作者对像1517这样的组织表示希望，这些组织试图通过投资个人并允许他们进行探索而不要求立即取得成果来提供贝尔实验室环境的模拟，暗示了未来重塑这种魔力的可能性。

---

## 4. 桑迪亚启动类脑无存储超级计算机 - Blocks and Files

**原文标题**: Sandia turns on brain-like storage-free supercomputer – Blocks and Files

**原文链接**: [https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/](https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/)

桑迪亚国家实验室启用SpiNNaker 2超级计算机：一种无需GPU和内部存储的“大脑启发”系统。该系统由SpiNNcloud提供，可模拟1.5亿至1.8亿个神经元，接近同类平台前五名。该架构源自Arm先驱Steve Furber，采用高度并行设计，每块服务器板包含48个SpiNNaker 2芯片，每个芯片包含152个内核和专用加速器。桑迪亚使用的24板系统包含175,000个内核。

SpiNNaker 2通过消除集中式存储来实现速度和效率，而是依赖于SRAM和DRAM（每个芯片具有20MB SRAM，每块板具有96GB LPDDR4内存）。这种设计促进了高速芯片间通信，避免了对传统存储系统的需求。

桑迪亚的系统与现有HPC系统集成，并且在没有操作系统或磁盘的情况下运行，通过将数据保存在SRAM和DRAM中来保持速度。SpiNNcloud声称其最大的系统超过1050万个内核，能够进行生物实时模拟。SpiNNcloud首席执行官Hector A. Gonzalez预计该系统将被用于“下一代国防及其他领域”，利用其效率用于国家安全应用。

---

## 5. Odyc.js – 用于叙事游戏的微型JavaScript库

**原文标题**: Odyc.js – A tiny JavaScript library for narrative games

**原文链接**: [https://odyc.dev](https://odyc.dev)

Odyc.js 是一个轻量级的 JavaScript 库，专为创建叙事性视频游戏而设计。其主要目标是赋能用户，即使是没有编程经验的人也能开发自己的视频游戏。该库旨在简化游戏开发过程，使其更容易被广大受众所接受。内容还邀请用户了解更多关于 Odyc.js 的信息，在图库中探索使用该库创建的游戏，并普遍参与该工具的生态系统。本质上，Odyc.js 被定位为一款易于使用的 JavaScript 工具，用于构建叙事游戏。

---

## 6. 受虐狂的网页开发指南

**原文标题**: A masochist's guide to web development

**原文链接**: [https://sebastiano.tronto.net/blog/2025-06-06-webdev/](https://sebastiano.tronto.net/blog/2025-06-06-webdev/)

WebAssembly开发中的“受虐指南”：C/C++开发者移植指南

---

## 7. Exa (YC S21) 正在招聘创始物理设计工程师，构建用于人工智能的芯片

**原文标题**: Exa (YC S21) Is Hiring a Founding Physical Design Engineer to Build Chips for AI

**原文链接**: [https://www.ycombinator.com/companies/exa-laboratories/jobs/9TXvyqt-founding-engineer-physical-design-vlsi-rtl](https://www.ycombinator.com/companies/exa-laboratories/jobs/9TXvyqt-founding-engineer-physical-design-vlsi-rtl)

Exa Laboratories (YC S24) 招聘创始物理设计工程师，助力打造用于人工智能的下一代节能型“XPU”芯片。这些多态芯片通过重新配置自身以优化每个模型的数据流，在人工智能训练和推理方面超越现有 GPU，从而显著节省能源并提高性能。

理想的候选人应具有扎实的电气/计算机工程背景，并具备半导体物理设计、超大规模集成电路 (VLSI)、数字/混合信号 IC 设计和 RTL 方面的经验。熟悉 (科)ML 框架和系统编程者优先。

该职位提供成为早期员工的机会，可直接与旧金山的创始团队合作。工程师将主导塑造 AI 计算未来的关键决策，并成长为技术领导职位。Exa 承诺提供具有竞争力的薪酬和可观的股权。

Exa 的目标是通过创建无需大规模电力基础设施即可支持 AGI 和 ASI 的 XPU，从而打造“下一个英伟达”，最终影响科学发现和知识创造。他们正在寻找一位充满激情、有干劲且核心的工程师，准备好迎接近乎不可能的技术挑战并创造持久的事物。

---

## 8. 动态场景重建的随时随地免费高斯图元

**原文标题**: Free Gaussian Primitives at Anytime Anywhere for Dynamic Scene Reconstruction

**原文链接**: [https://zju3dv.github.io/freetimegs/](https://zju3dv.github.io/freetimegs/)

FreeTimeGS：随时随地自由高斯基元用于动态场景重建

---

## 9. 过去94年一美元的增值情况 [pdf]

**原文标题**: See how a dollar would have grown over the past 94 years [pdf]

**原文链接**: [https://www.newyorklifeinvestments.com/assets/documents/education/investing-essentials-growthofadollar.pdf](https://www.newyorklifeinvestments.com/assets/documents/education/investing-essentials-growthofadollar.pdf)

无法根据提供的内容总结文章。 该文本似乎是 PDF 文件的二进制数据，并非人类可读的文本。 为了总结文章，需要可读的文本内容。 标题表明该文章将讲述一美元在过去 94 年里的增长情况，暗示它将涵盖投资回报和通货膨胀。

---

## 10. 打开文件过多

**原文标题**: Too Many Open Files

**原文链接**: [https://mattrighetti.com/2025/06/04/too-many-files-open](https://mattrighetti.com/2025/06/04/too-many-files-open)

解决 Rust 测试中 "Too many open files" 错误的实战记录

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 2 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 3 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 4 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 5 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 6 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 7 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 8 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 9 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 10 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 11 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 12 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 13 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 14 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 15 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 16 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 17 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 18 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 19 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 20 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 21 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 22 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 23 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 24 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 25 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 26 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 27 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 28 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 29 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 30 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 31 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 32 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 33 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 34 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 35 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 36 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 37 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 38 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 39 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 40 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 41 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 42 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 43 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 44 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 45 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 46 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 47 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 48 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 49 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 50 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 51 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 52 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 53 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 54 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 55 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 56 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 57 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 58 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 59 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 60 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 61 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 62 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 63 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 64 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 65 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 66 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 67 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 68 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 69 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 70 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 71 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 72 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 73 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 74 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 75 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 76 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 77 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 78 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 79 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
