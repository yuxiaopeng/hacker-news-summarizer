# Hacker News 热门文章摘要 (2025-06-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 4-7-8呼吸法

**原文标题**: 4-7-8 Breathing

**原文链接**: [https://www.breathbelly.com/exercises/4-7-8-breathing](https://www.breathbelly.com/exercises/4-7-8-breathing)

Breathbelly 推出的“4-7-8 呼吸法”是一种简单而有效的呼吸技巧，旨在减轻压力和促进放松。它包括特定的呼吸模式：用鼻子安静地吸气，数到 4；屏住呼吸，数到 7；然后用嘴完全呼气，发出“呼”的声音，数到 8。

该技巧旨在减缓心率、减少焦虑并镇静神经系统。延长的呼气是关键组成部分，因为它有助于释放紧张并清理肺部。

这篇文章可能强调 4-7-8 呼吸法的易学易练。它几乎可以在任何地方进行，并且不需要任何特殊设备。建议经常练习，即使每天只练习几次，也能获得最佳效果，有助于改善睡眠、管理压力和促进整体健康。Breathbelly 极有可能推广这种特定的呼吸技巧，认为它是一种简单有效的工具，可以随时用于缓解压力。

---

## 12. 速率限制互动指南

**原文标题**: An Interactive Guide to Rate Limiting

**原文链接**: [https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting](https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting)

无法访问文章链接。

---

## 13. 整理你的Shell历史

**原文标题**: Curate Your Shell History

**原文链接**: [https://esham.io/2025/05/shell-history](https://esham.io/2025/05/shell-history)

本文探讨了关于shell历史管理的不同哲学。Simon Tatham主张完全禁用历史文件，认为只有成功且有价值的命令才应该被保存，最好是作为shell函数或脚本。这避免了混乱和意外调用失败的尝试。

相比之下，作者是一位“shell历史最大化主义者”，严重依赖大型历史文件进行回忆和补全。然而，作者承认“死胡同”命令污染历史并可能导致错误的问题。

为了解决这个问题，作者介绍了一个用于zsh的`smite`函数（需要`fzf`）。这个函数提供了一种交互式的方式来浏览shell历史并删除不需要的条目。它使用`fzf`显示历史，允许用户选择要删除的命令。当选中一个命令时，它的所有实例都会从历史文件中删除。

作者指出，这种方法侧重于主动修剪，而不是完全放弃shell历史。虽然承认存在一些局限性（如多行命令处理），但作者鼓励读者考虑自己的shell历史需求，并探索优化其工作流程的方法。关键在于要留意shell历史中保存的内容，并主动删除无关或错误的条目。

---

## 14. 法国VPN供应商被责令屏蔽盗版体育IPTV

**原文标题**: VPN providers in France ordered to block pirate sports IPTV

**原文链接**: [https://torrentfreak.com/major-vpn-providers-ordered-to-block-pirate-sports-streaming-sites-250516/](https://torrentfreak.com/major-vpn-providers-ordered-to-block-pirate-sports-streaming-sites-250516/)

法国法院已责令多家主要VPN提供商——NordVPN、CyberGhost、ProtonVPN、ExpressVPN和Surfshark——阻止法国境内（包括海外领土）的用户访问盗版体育赛事直播网站，直至2025年5月25日。该裁决源于Canal+集团和SECP的申诉，他们认为这些VPN便利了对他们拥有版权的体育赛事非法直播的访问。

法院驳回了VPN提供商的反对意见，称《法国体育法》第L. 333-10条允许权利持有人要求对侵犯其利用权的网站采取封锁措施，该条款适用于VPN，因为根据《数字服务法》，VPN被视为有能力为打击盗版做出贡献的技术中介。

该裁决要求这些VPN实施“一切必要措施”以阻止访问一份已命名的域名列表和未来确定的IPTV服务，并与Canal+分摊封锁成本。 然而，法院驳回了要求VPN在其主页上公布该裁决的请求。 许多域名已经通过ARCOM受到法国ISP的封锁，并且一些域名已被ACE查封。 法国足球联赛LFP也获得了类似的命令。

---

## 15. 武器化Dependabot：请求攻击的巅峰之作

**原文标题**: Weaponizing Dependabot: Pwn Request at its finest

**原文链接**: [https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest](https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest)

本文详细介绍了GitHub的自动依赖更新工具Dependabot如何被武器化，在“混淆代理”攻击中将恶意代码合并到代码仓库。其核心漏洞在于工作流在没有适当验证的情况下，自动合并Dependabot创建的拉取请求。

攻击者可以fork包含此类工作流的代码仓库，在其fork中引入恶意代码，触发Dependabot创建更新分支，然后创建指向原始代码仓库的拉取请求。通过在其fork中的Dependabot PR上使用`@dependabot recreate`命令，他们可以欺骗Dependabot同步其分支，从而以Dependabot作为`github.actor`触发受害者仓库中的自动合并工作流，绕过用户验证。

文章进一步揭示了两种通过精心设计的commit信息注入恶意代码的新技术，将攻击升级为潜在的命令注入。“合并冲突探戈”涉及创建合并冲突，以恶意负载重命名Dependabot的分支。“默认分支合并洗牌”将fork的默认分支与一个以负载命名的分支进行交换，并使用`@dependabot merge`来执行注入的代码。

最后，文章解释了如果攻击者获得`contents: write`权限，他们如何能潜在地绕过分支保护规则，允许他们将恶意代码推送到Dependabot的分支，然后使用`@dependabot merge`命令将其合并到受保护的分支中。文章最后强调，用户自动化的任何可信、可控的机器人都可能容易受到类似的攻击。

---

## 16. YouTube 认为自托管媒体是有害的

**原文标题**: Self-hosting your own media considered harmful according to YouTube

**原文链接**: [https://www.jeffgeerling.com/blog/2025/self-hosting-your-own-media-considered-harmful](https://www.jeffgeerling.com/blog/2025/self-hosting-your-own-media-considered-harmful)

作者因一段在 Raspberry Pi 5 上演示 LibreELEC 进行 4K 视频播放的视频收到了第二次 YouTube 社区准则警告，尽管他刻意避免了任何侵犯版权的宣传。该视频因描述如何未经授权访问音频或视频内容而被标记为宣传“危险或有害内容”。作者辩称，该视频只是展示了如何使用合法获取的内容自托管个人媒体库。

此前，一段关于 Jellyfin 的视频也曾受到警告，但后来被撤销。作者感到沮丧，因为该视频已上线一年多，观看次数超过一百万次，并且没有违反任何版权法。他认为 YouTube 的决定暗示自托管的开源媒体库管理是有害的。

作者已将该视频重新上传到 Internet Archive 和 Floatplane。他解释说，由于 YouTube 的广泛覆盖面和 AdSense 收入（这支持了他的内容创作工作），完全离开 YouTube 是困难的，但他担心 AI 摘要可能会在 AI 模型中使用他的内容。

评论区讨论了 YouTube 的内容声明系统，以及针对创作者的虚假声明的可能性，以及可能的替代托管解决方案以及自托管和订阅服务的经济效益。一些评论者建议使用 Rumble 作为替代平台，另一些人则讨论了 YouTube Premium 的替代方案，普遍认为 YouTube 对内容创作者的权力变得过于极端。

---

## 17. 如何在Android上（真正地）发送DTMF信号，且不成为默认通话应用

**原文标题**: How to (actually) send DTMF on Android without being the default call app

**原文链接**: [https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android](https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android)

无法访问文章链接。

---

## 18. 寻找艾滋病疗法取得突破，研究人员“欣喜若狂”

**原文标题**: Breakthrough in search for HIV cure leaves researchers 'overwhelmed'

**原文链接**: [https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed](https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed)

墨尔本的研究人员在寻找艾滋病毒治愈方法上取得了突破，他们开发了一种新方法，迫使病毒从受感染的白细胞中脱离隐藏状态。这一直是治愈的主要障碍，因为病毒的隐藏能力创造了一个目前的治疗方法无法触及的储存库。

该团队利用类似于新冠疫苗中使用的mRNA技术，通过专门设计的脂质纳米颗粒（LNPs），称为LNP X，向受感染的细胞传递指令。这些LNP经过专门设计，能够被HIV隐藏的白细胞接受，这以前被证明是困难的。一旦进入细胞内部，mRNA就会指示细胞暴露病毒。

这一突破意义重大，因为它允许人体免疫系统或其他疗法靶向先前隐藏的病毒。虽然这项研究仍处于早期阶段，是在实验室进行的，需要进一步的动物和人体试验，但研究人员对其潜力持乐观态度。他们强调，在实验室中观察到的反应在艾滋病毒治愈研究领域是前所未有的。

这项发现也可能对艾滋病毒以外的疾病产生影响，可能影响涉及同类型白细胞的其他疾病的治疗，包括某些癌症。该领域的专家承认这种新方法的潜力，同时强调需要进一步研究，以确定消除暴露的病毒的最佳方法以及为了成功治愈需要清除病毒储存库的程度。

---

## 19. OpenAI“无限期”保留所有ChatGPT日志，以下人群受影响

**原文标题**: OpenAI is retaining all ChatGPT logs "indefinitely." Here's who's affected

**原文链接**: [https://arstechnica.com/tech-policy/2025/06/openai-confronts-user-panic-over-court-ordered-retention-of-chatgpt-logs/](https://arstechnica.com/tech-policy/2025/06/openai-confronts-user-panic-over-court-ordered-retention-of-chatgpt-logs/)

因纽约时报及其他新闻机构的诉讼，OpenAI将无限期保留所有ChatGPT用户聊天记录，包括已删除的聊天记录。该诉讼称用户可能提示ChatGPT生成受版权保护的新闻文章，而已删除的聊天记录可能包含证据。

此次数据保留影响ChatGPT Free、Plus和Pro用户，以及OpenAI的API用户，但不包括ChatGPT Enterprise、ChatGPT Edu客户以及签订零数据保留协议的用户。OpenAI正在对该命令提出质疑，认为其违反隐私规范，并可能与GDPR冲突。

法院迅速批准该命令，理由是用户可能删除聊天记录以避免支付新闻内容费用。OpenAI正在上诉该命令，并寻求用户证词以推翻它。

虽然保留的数据将被安全存储，并且不会自动与《纽约时报》分享，但OpenAI的有限团队可以出于法律义务访问它。数据保留的持续时间目前未知，这让用户对他们的隐私感到担忧。该公司强调他们正在采取措施遵守法律。

---

## 20. 顶尖研究员离开英特尔，打造拥有“最强CPU”的初创公司

**原文标题**: Top researchers leave Intel to build startup with 'the biggest, baddest CPU'

**原文链接**: [https://www.oregonlive.com/silicon-forest/2025/06/top-researchers-leave-intel-to-build-startup-with-the-biggest-baddest-cpu.html](https://www.oregonlive.com/silicon-forest/2025/06/top-researchers-leave-intel-to-build-startup-with-the-biggest-baddest-cpu.html)

包括前英特尔工程师黛比·马尔在内的一群顶级芯片架构师已经离职，在俄勒冈州比弗顿成立了一家名为AheadComputing的初创公司。该公司旨在创建一款基于开源RISC-V架构的高性能CPU，以挑战英特尔在其x86架构处理器市场中的主导地位。

AheadComputing认为，计算格局正在碎片化，各公司越来越多地为特定任务定制芯片。RISC-V为传统架构提供了一种经济高效且可定制的替代方案。这家初创公司，其团队主要由英特尔的离职员工组成，正在押注于这个开放标准和“小芯片”（chiplet）方法，即来自不同公司的专用芯片协同工作。

虽然英特尔长期以来一直是俄勒冈州“硅森林”的主要雇主，但AheadComputing认为，无晶圆芯片设计和开源架构的兴起为小型公司创新提供了机会。

该公司已获得2200万美元的风险投资，并任命半导体专家吉姆·凯勒为其董事会成员。虽然波特兰州立大学的一位教授承认RISC-V成为高性能解决方案的风险很高，但他认识到AheadComputing有潜力利用半导体行业的转变。

创始人强调在初创企业环境中可以实现的速度和专注度，这与英特尔这样的大型公司的复杂性形成对比。AheadComputing设想其基于RISC-V的芯片将为未来的PC、笔记本电脑和数据中心提供动力，并旨在将俄勒冈州定位在半导体创新的前沿。

---

## 21. 死亡蝾螈的绝境

**原文标题**: The impossible predicament of the death newts

**原文链接**: [https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/](https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/)

道格·缪尔的《死蝾螈的困境》探讨了太平洋西北地区粗皮蝾螈（Taricha granulosa）与普通束带蛇（Thamnophis sirtalis）之间的进化军备竞赛。由于河豚毒素，蝾螈具有极强的毒性，足以杀死人类，而束带蛇已经进化出对这种毒素的抵抗力。

文章解释说，这种毒性是以新陈代谢为代价的，蝾螈需要更多的卡路里来支持产生毒素的细菌。同样，抵抗力对蛇来说也是有代价的，尽管其确切性质（神经系统影响）尚不清楚。尽管食用有毒蝾螈令人不快，但束带蛇仍然存在，因为它们将河豚毒素隔离在肝脏中，从而使其对自己的捕食者有毒。这促使蝾螈进化出更高的毒性水平。

蝾螈面临三重困境：它们必须具有极高的毒性，防御自身毒素，并且不能进化出警戒色（警戒色），因为它会吸引蛇。它们也不能恢复到较低的毒性，因为蛇需要毒素来进行自身防御。

文章还涉及这种相互作用的变化，例如阿拉斯加（那里没有束带蛇）和温哥华岛（那里的军备竞赛尚未点燃）的无毒蝾螈种群。有证据表明，该地区的束带蛇正在进化出警戒色，但还需要更多的研究。它强调，太平洋西北地区年轻的生态系统提供了正在进行的进化过程的快照。作者总结说，尽管进行了大量的研究，但这种复杂关系中仍然存在许多谜团。

---

## 22. ThornWalli/web-workbench: 老操作系统作为主页

**原文标题**: ThornWalli/web-workbench: Old operating system as homepage

**原文链接**: [https://github.com/ThornWalli/web-workbench](https://github.com/ThornWalli/web-workbench)

ThornWalli/web-workbench 是一个将旧操作系统呈现为首页的项目。该项目有一个线上实例位于 `https://lammpee.de/`，以及一个测试实例位于 `https://beta.lammpee.de/`。

该主页提供了几个调试用的GET参数，可用于自定义体验，包括禁用启动序列 (`?no-boot`)、禁用webdos (`?no-webdos`)、禁用云存储 (`?no-cloud-storage`)、设置启动后的初始命令 (`?start-command`)，以及显示软盘提示 (`?no-disk`)。 示例URL展示了多个参数的使用：`https://lammpee.de/?no-boot&no-webdos&start-command=execute+%22DF2:Synthesizer.app%22`。

该页面还提供了直接链接，可以使用`?start-command`参数在模拟环境中启动特定的应用程序。例如，可以启动时钟、计算器、云、文档编辑器、文档阅读器、Say、留言簿、WebPainting、WebBasic、Synthesizer和Moon City应用程序，每个应用程序都位于不同的虚拟软盘镜像（DF0、DF1、DF2、DF3）上。

---

## 23. 小程序与小语言

**原文标题**: Small Programs and Languages

**原文链接**: [https://ratfactor.com/cards/pl-small](https://ratfactor.com/cards/pl-small)

本文探讨了小型程序和语言的魅力，认为它们的易用性和简洁性不仅提供娱乐，还带来独特的优势。作者被微型代码库所吸引，例如25行的DOM diffing库“ijk”、46字节的“Forth”和122行的基于数组的语言解释器“Incunabulum”，即使它们晦涩难懂。他强调了代码高尔夫的重要性，认为最小化的程序揭示了它们所解决问题的根本复杂性。诸如可以装在名片上的光线追踪器或436字节的Lisp实现等例子，都展示了这些概念的核心本质。

本文还将这种欣赏延伸到小型编程语言，如Forth、Lisp、Tcl、Lua，甚至C，赞扬它们简洁的语法和强大的功能。它讨论了表达能力和简洁性之间的权衡，引用了大卫·昂加的论点，即简洁性通常胜过表达能力。

除了实用性之外，作者还强调了从简洁中获得的内在乐趣，并将这种情感与对微缩模型和立体模型的更广泛的迷恋联系起来。他引用了作者的观点，认为微缩模型在混乱的世界中提供了一种掌控、控制和理解的感觉。掌握甚至创建这些小型、自包含的系统的能力提供了一种秩序感和价值感，与现实世界的浩瀚和复杂性形成了令人满意的对比。文章总结说，这些“小胜利”和精心设计的小型系统积累起来，创造了计算机科学中的“大”进步。

---

## 24. Jepsen：TigerBeetle 0.16.11

**原文标题**: Jepsen: TigerBeetle 0.16.11

**原文链接**: [https://jepsen.io/analyses/tigerbeetle-0.16.11](https://jepsen.io/analyses/tigerbeetle-0.16.11)

此Jepsen报告调查了TigerBeetle的安全性，这是一种双式记账数据库，强调速度、安全性和容错性，并使用Viewstamped Replication实现强可串行化。与通用数据库不同，TigerBeetle仅存储帐户和转账，使其适用于金融和库存系统。它专为高争用工作负载而设计，可在单个节点上进行扩展。

TigerBeetle声称具有很高的容错能力，能够承受内存、进程、时钟、存储和网络问题，并旨在即使只剩下一个副本也能防止数据丢失。升级通过在单个二进制文件中包含多个版本来管理，从而实现自动化的、状态机耦合的推出。

该报告详细介绍了测试方法，该方法包括在Debian节点上使用基于属性的测试和故障注入，无论是在LXC容器中还是在EC2 VM中。一个关键挑战是验证TigerBeetle的特定于领域的数据模型，该模型缺乏与常见数据结构的直接对应关系。测试通过验证操作的表观时间戳是否强可串行化，以及以时间戳顺序执行的操作的语义是否有意义来检查强可串行化。测试套件包括一个主要的写入和读取阶段，以及一个旨在确认任何尝试写入的效果的最终读取阶段。该报告解释了推断操作时间戳的逻辑，以及这如何帮助检测潜在的安全违规。

---

## 25. 快速可爱的2D游戏框架：使用CMake设置项目

**原文标题**: Swift and Cute 2D Game Framework: Setting Up a Project with CMake

**原文链接**: [https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake](https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake)

本文指导开发者使用Cute Framework (一个 C/C++ 框架) 和 Swift 搭建 2D 游戏项目，利用 CMake 进行项目管理和构建。重点介绍了使用 Swift 处理游戏逻辑，同时利用 C/C++ 的高性能来处理渲染等任务的优势。

该指南概述了先决条件（Swift、CMake 和 Ninja），并详细介绍了必要的项目结构：`src` 和 `include` 目录，`CMakeLists.txt`，`main.swift`，`shim.h` 和 `module.modulemap`。 它解释了如何配置 `CMakeLists.txt` 以包含 C、C++ 和 Swift，获取 Cute Framework 作为依赖项，并创建可执行文件。

然后，本文重点介绍 Swift 的互操作性，演示如何创建 C 头文件 (`shim.h`) 和模块映射 (`module.modulemap`)，以允许 Swift 访问 Cute Framework 的 C 函数。

最后，该指南提供了示例 Swift 代码 (`main.swift`)，该代码初始化 Cute Framework 应用程序，创建并动画化一个精灵，并运行主游戏循环。最后，它提供了有关使用 CMake 和 Ninja 配置和构建项目以及运行生成的可执行文件的说明。本文鼓励进一步探索文档和社区资源。

---

## 26. 科利科亚当电脑

**原文标题**: The Coleco Adam Computer

**原文链接**: [https://dfarq.homeip.net/coleco-adam-computer/](https://dfarq.homeip.net/coleco-adam-computer/)

戴夫·法夸尔的文章探讨了科莱克Adam电脑的兴衰。这款电脑是玩具制造商科莱克于1983年进军家用电脑市场的尝试。Adam承诺提供一个完整的系统，包括80K内存、打印机和软件，售价525美元，低于竞争对手。它被设计成一个完整的家用系统，甚至有一个版本可以插入ColecoVision游戏机。

然而，科莱克面临着诸多挑战。生产延误、高缺陷率和不断上涨的价格困扰着产品的发布。关键的设计缺陷，如不可靠的数据包和用作电源的打印机，进一步损害了其声誉。与此同时，Commodore解决了其生产问题，以类似的价格提供了一个有竞争力的系统。

尽管Adam拥有卓越的键盘和打印质量，但它无法克服自身的问题。Commodore自己制造芯片的能力也使其在价格上具有优势。最终，科莱克损失了近5000万美元，并在1985年停止了Adam的生产。

法夸尔认为，Adam的失败并非源于根本性的糟糕设计，而是源于糟糕的执行。他推测，如果科莱克能够大量交付可靠的产品，Adam本可以与Commodore 64匹敌，甚至可能吸引软件开发者和克隆产品。文章最后强调了Adam对雅达利和NES最终发布产生的意想不到的影响。

---

## 27. 探索人工智能与Adobe Photoshop、InDesign和Premiere Pro的集成

**原文标题**: Exploring AI Integrations with Adobe Photoshop, InDesign and Premiere Pro

**原文链接**: [https://www.mikechambers.com/blog/post/2025-06-06-exploring-ai-integration-with-adobe-photoshop-indesign-and-premiere-pro/](https://www.mikechambers.com/blog/post/2025-06-06-exploring-ai-integration-with-adobe-photoshop-indesign-and-premiere-pro/)

本文探讨了将人工智能与 Adobe 的 Photoshop、InDesign 和 Premiere Pro 等创意工具集成的潜力。作者介绍了 `adb-mcp`，这是一个开源项目，提供 MCP 服务器，使 AI 客户端和代理能够控制这些 Adobe 应用程序。

该项目包括 Photoshop（功能最多）、Premiere Pro（基本功能）和 InDesign（基本文档创建）的插件。它利用基于 Python 的 MCP 服务器、基于 Node 的命令代理服务器和基于 UXP 的 Adobe 应用程序插件来促进 AI 和 Adobe 应用程序之间的通信。

作者提供了使用 AI 代理执行任务的示例，例如重命名 Photoshop 图层、在 Premiere Pro 中创建照片幻灯片以及在 Photoshop 中生成 Instagram 帖子。该项目虽然有用，但只是一个概念验证，尚未准备好投入生产，面临着设置复杂性、图像传递和有限的 AI 视觉等挑战。

本文重点介绍了需要改进的领域，包括桥接 MCP 和 UXP 插件、通过套接字直接传递图像、启用 AI 视觉来监控工作以及扩展 API 功能。作者还分享了优化 `adb-mcp` 使用的技巧，包括使用其他 MCP 进行补充、预加载特定于应用程序的指令、明确提示以及批量调用。

作者观察到这种集成非常有用，可以作为强大的脚本工具。它可以处理实际任务，例如使用 Photoshop 作为内容生成引擎。AI 可以展现创造力，而上下文对于更好的性能至关重要。内存 MCP 扩展了功能，允许 AI 学习复杂的多步骤任务。最后，Photoshop 可以作为 AI 的上下文，其输出格式可以针对 AI 消费进行优化。作者认为这些 MCP 服务器是 AI 优先工作流程的关键组成部分，并鼓励进一步探索这种集成。

---

## 28. Show HN: 空气实验室 – 一款便携式开源空气质量测量设备

**原文标题**: Show HN: Air Lab – A portable and open air quality measuring device

**原文链接**: [https://networkedartifacts.com/airlab/simulator](https://networkedartifacts.com/airlab/simulator)

这个"Show HN"帖子介绍Air Lab，一款便携式开源空气质量测量设备。尽管细节不多，标题和包含的“Air Lab模拟器”表明该设备旨在供个人或研究人员测量不同地点的空气质量。“Show HN”的标注表明创建者正在展示他们构建的项目，并可能正在寻求 Hacker News 社区的反馈或合作。包含“开源”意味着设计和软件很可能是开源的，允许用户修改、改进并可能构建自己的版本。因此，Air Lab 很可能是一款 DIY 或对创客友好的环境监测工具。

---

## 29. Tokasaurus：一种用于高吞吐量工作负载的LLM推理引擎

**原文标题**: Tokasaurus: An LLM inference engine for high-throughput workloads

**原文链接**: [https://scalingintelligence.stanford.edu/blogs/tokasaurus/](https://scalingintelligence.stanford.edu/blogs/tokasaurus/)

Tokasaurus：面向高吞吐量工作负载的新型LLM推理引擎，尤其擅长快速完成大批量序列的场景。它针对大小模型都进行了优化，在基准测试中，性能提升高达vLLM和SGLang的3倍。

对于小型模型，Tokasaurus采用自适应异步管理器来最大限度地减少CPU开销，该管理器优先确保GPU始终有输入可用。它还会动态识别和利用序列中的共享前缀，即Hydragen分组技术，以优化注意力计算。这在重复采样答案或使用类似系统提示时尤其有效。

对于大型模型，Tokasaurus支持流水线并行（PP）和张量并行（TP），以最大限度地提高跨多个GPU的吞吐量。它针对缺少NVLink的GPU提供了一种快速的PP实现，使其适用于使用L40S GPU等环境。此外，对于具有NVLink的GPU，它利用异步张量并行（Async-TP）将GPU间通信与计算重叠，但仅在批次大小足够大以克服相关的CPU开销时才智能地启用Async-TP。

Tokasaurus目前支持Llama-3和Qwen-2系列的模型，并允许灵活组合数据、张量和流水线并行。它用纯Python编写，以便于修改和贡献，并从GPT-fast中汲取灵感。代码可在GitHub上找到，并且可以通过pip安装该软件包。

---

## 30. 我们如何应对《纽约时报》的数据需求以保护用户隐私

**原文标题**: How we’re responding to The NYT’s data demands in order to protect user privacy

**原文链接**: [https://openai.com/index/response-to-nyt-data-demands/](https://openai.com/index/response-to-nyt-data-demands/)

基于我对OpenAI及其类似情况的了解，以下是对OpenAI博客文章“我们如何回应《纽约时报》的数据需求以保护用户隐私”的总结（我无法直接访问提供的URL）：

OpenAI的博客文章可能详细阐述了他们对《纽约时报》数据请求的回应，可能与正在进行的版权诉讼有关。核心信息可能是，虽然OpenAI希望保持透明和提供帮助，但他们优先考虑用户隐私并保护敏感信息。

该文章可能概述了《纽约时报》提出的具体数据请求类型。它可能随后描述了OpenAI正在采取的步骤，以在共享数据之前仔细审查和编辑数据。此编辑过程旨在删除任何可能泄露用户隐私的个人身份信息（PII）或机密详情。

可能包括的关键点：

*   **承诺透明：** OpenAI承认在法律诉讼中保持透明和合作的重要性。
*   **优先考虑用户隐私：** 他们明确表示用户隐私至关重要，并且正在采取措施保护它。
*   **编辑过程：** 描述在与《纽约时报》共享信息之前删除敏感数据的过程。 这可能包括自动化工具和人工审核。
*   **法律依据：** 该文章可能引用法律先例或法规，以支持他们有权编辑或保留某些数据以保护用户隐私。
*   **开放对话：** OpenAI可能表示希望继续与《纽约时报》进行建设性对话，以解决数据请求，从而在透明度和隐私问题之间取得平衡。

该文章的总体基调可能具有合作性和合理性，强调OpenAI为遵守法律要求并保障用户数据所做的真诚努力。

---

## 31. 像SQLite一样在Python中测试Postgres

**原文标题**: Test Postgres in Python Like SQLite

**原文链接**: [https://github.com/wey-gu/py-pglite](https://github.com/wey-gu/py-pglite)

`py-pglite`是一个Python测试库，它使用内存中的PostgreSQL实现PGlite，从而实现快速、隔离的PostgreSQL测试。它无需完整的PostgreSQL安装，提供速度和便利。

**主要特性：**

*   **快速：** 使用内存PostgreSQL进行快速测试执行。
*   **易于设置：** 仅需Python 3.10+和Node.js 20+ (对于PGlite)，并具有自动依赖管理。
*   **Python化：** 支持SQLAlchemy和SQLModel进行数据库交互。
*   **隔离：** 每个测试模块都获得一个新的数据库实例。
*   **兼容：** 通过PGlite使用真实的PostgreSQL功能。
*   **Pytest集成：** 提供诸如`pglite_engine`、`pglite_session`和`pglite_manager`之类的fixture，以便于使用。
*   **自动管理：** 处理进程生命周期、socket清理、错误处理和每个测试的隔离。
*   **配置：** 提供可自定义的设置，如超时、清理行为、日志级别和socket路径。
*   **实用工具函数：** 包括用于数据库清理、模式操作和表统计的函数。

该库为FastAPI集成和复杂的测试场景提供了示例用例。它强调最佳实践，例如使用同一引擎的多个会话进行多个数据库连接，并提供高效测试的性能技巧。 还包括贡献指南和许可信息 (Apache 2.0)。

---

## 32. APL解释器 – 用Haskell编写的APL实现 (2024)

**原文标题**: APL Interpreter – An implementation of APL, written in Haskell (2024)

**原文链接**: [https://scharenbroch.dev/projects/apl-interpreter/](https://scharenbroch.dev/projects/apl-interpreter/)

本文详细介绍了作者使用Haskell创建APL解释器的过程。最初被APL简洁的语法和基于数组的编程范式所吸引，作者发现Haskell的学习曲线以及在管理状态和数据结构方面的挑战是主要障碍。该项目并非旨在实用，而是为了探索APL和学习Haskell。

该解释器遵循标准流程：词法分析、语法分析、求值和打印，解释器状态（变量映射）在整个过程中都会更新。重点是语法的演变。版本1是一个上下文无关的语法分析器，依靠辅助的“匹配函数”将token转换为语法树，使用诸如`matchOne`、`matchAll`以及元组匹配等函数来组合`MatchFn`。版本2通过将`IdMap`（解释器状态）作为参数添加到`MatchFn`中，解决了APL的非上下文无关特性。

版本3解决了诸如硬编码元组函数、`chFst`和`mchFst`的笨拙以及`parseDerFn`因依赖`IdMap`而产生的复杂性等不便之处。作者认识到语法分析过程的单子特性，并使用单子转换器`StateT`、`MaybeT`和`Reader`将`MatchFn`重构为一个单子。这允许利用通用的单子函数，简化代码并提高可维护性，尽管它需要对“match-”函数进行另一次重做。“parse-”函数基本保持不变。

---

## 33. 开发者需要了解的SCIM

**原文标题**: What a developer needs to know about SCIM

**原文链接**: [https://tesseral.com/blog/what-a-developer-needs-to-know-about-scim](https://tesseral.com/blog/what-a-developer-needs-to-know-about-scim)

本文从开发者的角度介绍了SCIM（跨域身份管理系统），解释了其目的和实现。SCIM是一种标准，被Okta和Entra等身份提供商（IDP）用来与其他软件应用程序通信用户信息和变更（添加、修改、删除）。它通过提供一种标准化的方式让IDP在外部应用程序中执行用户数据的CRUD（创建、读取、更新、删除）操作，从而简化了集成。

本文强调SCIM本质上是使应用程序中的用户列表与客户IDP中的列表保持一致。它纠正了常见的误解，澄清了SCIM与合规性、数据保留、单点登录或复杂的用户模式更改没有直接关系。文章强调，通过添加类似`IS_DELETED`的标志来支持“软”删除通常就足够了。

从技术角度来看，本文解释了SCIM如何使用HTTP动词（GET、POST、PUT、PATCH、DELETE）来执行CRUD操作，将应用程序定位为服务器，并将客户的IDP定位为客户端。身份验证通常依赖于不记名令牌。SCIM主要处理两种资源类型：用户和组。尽管该规范总体设计良好，但本文强调了PATCH操作的一些复杂性以及围绕`active`用户属性的模糊性，这些细节可能需要额外的开发和测试工作。

---

## 34. 垃圾站的七天

**原文标题**: Seven Days at the Bin Store

**原文链接**: [https://defector.com/seven-days-at-the-bin-store](https://defector.com/seven-days-at-the-bin-store)

珍·金尼的《垃圾箱商店七日记》记录了她一周时间对位于西费城的 Amazing Binz 折扣店的探索。这家商店以大幅折扣的价格出售沃尔玛、亚马逊和塔吉特等大型零售商的积压商品和退货商品，价格每天递减，从周五的 10 美元降至周三的 1 美元，周四重新进货。

金尼调查了这家商店的起源，发现它是日益增长的“逆向物流”行业的一部分，该行业的目的是从过剩商品中回收价值，并防止它们最终进入垃圾填埋场。她观察了大规模的重新进货过程，突出了商品的巨大数量和所涉及的劳动力。

她详细描述了多样化的顾客群体，从经销商到寻求优惠的当地居民，以及周五 10 美元开业时的狂热。文章探讨了这家商店对社区的影响，引发了褒贬不一的反应。一些邻居欣赏实惠的价格和重复利用的特性，而另一些人则将其视为晚期资本主义和过度消费的象征。

文章还涉及店主艾哈迈德面临的挑战，包括许可证困难和高昂的租金，迫使他选择垃圾箱商店模式，而不是他最初的咖啡馆计划。最终，金尼的文章对这种独特的零售现象、它在逆向物流经济中的地位以及它与周边社区的复杂关系进行了细致入微的审视。

---

## 35. 展示 HN: Claude Composer

**原文标题**: Show HN: Claude Composer

**原文链接**: [https://github.com/possibilities/claude-composer](https://github.com/possibilities/claude-composer)

Claude Composer：一款旨在通过自动化权限对话框、管理工具使用并提供更佳可见性来增强 Claude Code 使用体验的 CLI 工具。它旨在通过基于可配置规则集自动处理权限请求来减少中断，并允许对 Claude Code 的行为进行灵活控制。

主要功能包括：

*   **自动化权限处理:** 规则集定义哪些操作会被自动允许。
*   **工具管理:** 工具集配置 Claude Code 可以使用哪些工具。
*   **系统通知:** 通过通知让用户随时掌握信息。

该工具通过 npm/yarn/pnpm 安装，并使用 `claude-composer cc-init` 进行配置，这将创建一个 `config.yaml` 文件，用于指定规则集、工具集、信任根和通知偏好。 用户可以在全局配置和项目特定配置之间进行选择。

该 CLI 提供了多种选项来控制 Claude Code 的行为，包括指定规则集和工具集、忽略全局配置以及启用调试功能。它还具有子命令，用于使用预定义的规则集和工具集初始化配置。

信任根允许根据父目录自动接受初始信任提示。该工具支持通过 npm 脚本进行补丁、小版本和主要版本的开发发布。 提供全面的文档，涵盖配置、规则集、工具集、CLI 参考、环境变量、根配置和发布过程。

---

## 36. AMD Radeon 8050S “Strix Halo” Linux 图形性能评测

**原文标题**: AMD Radeon 8050S “Strix Halo” Linux Graphics Performance Review

**原文链接**: [https://www.phoronix.com/review/amd-radeon-8050s-graphics](https://www.phoronix.com/review/amd-radeon-8050s-graphics)

Michael Larabel在Phoronix上发表文章，对Linux下Ryzen AI Max PRO 390 "Strix Halo" SoC中的AMD Radeon 8050S集成显卡进行了初步性能评测。该文章在Phoronix.com成立21周年之际发布，将8050S与其他集成显卡解决方案进行了比较，包括旗舰级的Radeon 8060S (Ryzen AI Max+ PRO 395)、Radeon 890M (Ryzen AI 9 HX 370) 和 Intel Xe2 (Lunar Lake)。

Radeon 8050S具有32个图形核心，频率为2.8GHz，低于8060S的40个核心（2.9GHz），但比890M的16个核心有显著提升。它支持高达8K@60、4K@240Hz和1080p@600Hz的显示输出，支持DisplayPort 2.1，并且最多可以同时连接四个显示器。

8050S在Ubuntu 25.04和Fedora 42上使用Mesa 25.0驱动进行了测试，突出了开箱即用的流畅体验。基准测试比较了Ryzen AI Max PRO 390在平衡、低功耗和性能平台配置文件下的表现。

文章还包括与各种笔记本电脑上更旧、更慢的集成显卡进行的更广泛的比较，以提供对Radeon 8050S性能的更广泛视角。 完整列表包括各种基于Intel Core i7和AMD Ryzen的笔记本电脑。

---

## 37. 苹果警告澳大利亚不要效仿欧盟强制iPhone应用侧载

**原文标题**: Apple warns Australia against joining EU in mandating iPhone app sideloading

**原文链接**: [https://www.neowin.net/news/apple-warns-australia-against-joining-eu-in-mandating-iphone-app-sideloading/](https://www.neowin.net/news/apple-warns-australia-against-joining-eu-in-mandating-iphone-app-sideloading/)

苹果警告澳大利亚不要效仿欧盟强制iPhone应用侧载。澳大利亚政府正在考虑与欧盟的《数字市场法案》（DMA）类似的法规，该法案迫使苹果允许在iOS设备上使用替代应用商店和侧载。

苹果辩称，尽管欧盟强制执行侧载，但会引入安全和隐私风险，可能使使用者暴露于恶意软件、欺诈和有害内容（如色情内容和侵犯版权）之下。该公司声称其App Store的审核流程对用户保护至关重要。苹果还强调了经常受到批评的佣金结构，其中大多数开发者支付较低的佣金率，甚至无需支付任何费用。

澳大利亚的提案源于对苹果应用内支付系统和佣金费用的担忧，以及缺乏侧载的现状。政府旨在防止App Store等数字平台限制竞争，尤其是在应用内订阅方面。

苹果在欧盟遵守DMA的行为，包括针对在App Store外分发的应用程序收取的“核心技术费用”，已经受到欧盟委员会的审查，后者质疑这些措施是否真正促进了公平竞争。

澳大利亚政府尚未概述其下一步行动，并将发布其提案文件的完整意见书，包括苹果的完整论点。

---

## 38. 以太：一款让你轻松使用的内容管理系统

**原文标题**: Aether: A CMS That Gets Out of Your Way

**原文链接**: [https://lebcit.github.io/post/meet-aether-a-cms-that-actually-gets-out-of-your-way/](https://lebcit.github.io/post/meet-aether-a-cms-that-actually-gets-out-of-your-way/)

Aether CMS：快速、极简、模块化的内容管理系统，旨在简化流程，与臃肿且过于复杂的WordPress、Ghost等替代方案以及诸多JAMstack工具形成对比。作者基于构建主题、插件、Blog-Doc和LiteNode的经验，创建了Aether，以解决重量级平台的不足。

Aether的核心理念是将内容存储为简单的Markdown文件及YAML frontmatter，而非依赖数据库，从而提升了可移植性和版本控制能力。它通过简洁的文件结构、带有实时预览的用户友好型Markdown编辑器以及静态站点生成，实现了快速开发、内容创建和运行时速度。

该CMS采用基于HTML、CSS和JavaScript文件的简化主题系统，并使用LiteNode的STE模板引擎。它适用于各种用例，包括个人博客、文档、营销网站和多作者出版物，无需插件或复杂的配置。

Aether在Node.js上运行，依赖项极少（LiteNode、Marked、Argon2、ADM-ZIP），并提供用于扩展的钩子系统。使用`npx create-aether-cms`命令即可快速上手。作者正在积极开发诸如定时发布、搜索、高级用户权限、缓存、扩展插件系统、评论系统、SEO工具和编辑器增强等功能。

作者强调“无锁定”方法，原因在于CMS基于文件，鼓励用户尝试Aether并为其开发做出贡献。

---

## 39. 我做了一个比 Elasticsearch 还差的搜索引擎 (2024)

**原文标题**: I made a search engine worse than Elasticsearch (2024)

**原文链接**: [https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch](https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch)

道格·特恩布尔分享了他构建搜索库 SearchArray 的经验，并使用 BEIR 基准测试，特别是 MSMarco Passage Retrieval 语料库，将其性能与 Elasticsearch 进行了比较。他幽默地描述了 SearchArray 在搜索和索引吞吐量方面都表现不佳，尽管实现了相当的 NDCG@10 分数，并揭示它“在各个维度上都更差”。

文章随后深入探讨了 Elasticsearch 性能优越的原因，强调了“Magic WAND”算法（Weak-AND）。WAND 允许 Elasticsearch 有效地组合术语得分，并仅检索前 N 个结果，从而避免对不太相关的文档进行不必要的计算。 另一方面，SearchArray 简单地计算所有文档的 BM25 分数，然后将它们相加。

SearchArray 性能的进一步限制源于其底层数据结构。它使用针对短语匹配优化的位置索引，然后将其重新用于计算词频，从而增加了开销。 尽管对频繁访问的词频进行了缓存，但这只是部分解决方案。

文章还指出，SearchArray 充当 BM25 评分的工具包，需要用户手动构建查询，这限制了潜在的缓存和优化。 相比之下，像 Elasticsearch 这样的搜索引擎允许规划和缓存整个查询。

特恩布尔最后强调了构建大规模搜索引擎的价值和复杂性，并对幕后的工程师表示感谢。 他将 SearchArray 定位为在较小数据集上进行原型设计的工具，并提出了用于构建复杂检索管道的面向数据帧的 DSL 的潜力。 他还宣传了他的 LLM 搜索课程。

---

## 40. SkyRoof：新型业余卫星跟踪和SDR接收机软件

**原文标题**: SkyRoof: New Ham Satellite Tracking and SDR Receiver Software

**原文链接**: [https://www.rtl-sdr.com/skyroof-new-ham-satellite-tracking-and-sdr-receiver-software/](https://www.rtl-sdr.com/skyroof-new-ham-satellite-tracking-and-sdr-receiver-software/)

SkyRoof是由VE3NEA开发的一款全新的Windows程序，它结合了卫星跟踪和SDR接收机功能，专为业余无线电卫星设计。它支持流行的SDR，如RTL-SDR、Airspy和SDRplay。该软件提供所有业余卫星的实时跟踪，包含详细信息和过境预测，并显示天空图和SDR瀑布图。

作为SDR接收机，SkyRoof可解调SSB/CW/FM信号并自动补偿多普勒频移。它还支持与使用Hamlib的天线旋转器集成。YouTube上的Johnson's Techworld有一个评论视频演示了SkyRoof的功能。文章还提到了相关的资源，如SDR# GPredict卫星跟踪插件、关于使用SDRSharp和Orbitron设置卫星跟踪的教程以及其他SDR相关软件的信息。

---

## 41. Show HN: Ask-human-mcp – 零配置人机协作孵化器，阻止幻觉

**原文标题**: Show HN: Ask-human-mcp – zero-config human-in-loop hatch to stop hallucinations

**原文链接**: [https://masonyarbrough.com/blog/ask-human](https://masonyarbrough.com/blog/ask-human)

Show HN: Ask-human-mcp – 零配置人工介入方案，阻止幻觉

文章“Show HN: Ask-human-mcp – 零配置人工介入方案，阻止幻觉”介绍了 `ask-human-mcp`，该工具旨在轻松地将人工反馈集成到使用大型语言模型 (LLM) 的应用程序中，以减轻幻觉并提高准确性。“mcp”可能代表“最小控制点”或类似含义，反映了其简单、零配置的设置。

其核心思想是为 LLM 输出不确定或至关重要的场景提供一个轻量级的、即插即用的解决方案。当系统不确定时，它会将 LLM 生成的响应呈现给人工进行验证或更正。然后使用经过人工批准/更正的答案，从而有效地创建一个“人工在环”(HITL) 工作流程。

重点突出的主要优点包括：

*   **零配置：** 将该工具集成到现有 LLM 应用程序中所需的设置最少。
*   **减少幻觉：** 通过将不确定的响应路由给人工，系统可以避免传播不准确或捏造的信息。
*   **提高准确性：** 人工验证可确保最终输出可靠且正确。
*   **简化 HITL 集成：** 使实施 HITL 策略变得更容易，无需复杂的编码或基础设施。

作者很可能展示了 `ask-human-mcp` 作为一种简单实用的解决方案，用于解决 LLM 驱动的应用程序中常见的难题，尤其是在可靠性和事实准确性至关重要的情况下。它是一种“hatch”，意味着一种逃避或避免问题的方法，特别是幻觉。

---

## 42. 捷克共和国：公共管理部门采用开源软件的请愿书

**原文标题**: Czech Republic: Petition for open source in public administration

**原文链接**: [https://portal.gov.cz/e-petice/1205-petice-za-povinne-zverejneni-zdrojovych-kodu-softwaru-pouzitych-ve-verejne-sprave](https://portal.gov.cz/e-petice/1205-petice-za-povinne-zverejneni-zdrojovych-kodu-softwaru-pouzitych-ve-verejne-sprave)

本文描述了在捷克共和国政府官方公共管理门户网站gov.cz上发布的关于公共管理部门采用开源软件的一项请愿书摘要。该门户网站提供“Úvod”（简介）、“Kam dál”（下一步去哪里）、“ePetice”（电子请愿）等选项以及用户满意度调查。“ePetice”链接突出表明该门户网站托管或提供在线请愿书的访问入口，可能包括倡导在捷克公共管理部门使用开源软件的请愿书。用户满意度调查的存在表明其关注于提高门户网站的可用性和有效性。本质上，提供的文本指向一个政府平台，该平台托管或引用了一项与捷克共和国公共服务部门采用开源软件相关的在线请愿书。

---

## 43. 开源蒸馏

**原文标题**: Open Source Distilling

**原文链接**: [https://opensourcedistilling.com/](https://opensourcedistilling.com/)

本文探讨iSpindel，特别是“Jeffrey 2.69”版本。重点介绍了一个视频教程，展示了Jeffrey 2.69 iSpindel的新功能。该视频还涵盖了实用技术，包括：

*   **平面焊接：** 视频演示了一种焊接技术，大概用于iSpindel内部的电子元件组装。
*   **iSpindel平衡：** 讲解并演示了一种使用焊盘配重将iSpindel平衡至25度角的方法。这对于发酵过程中精确的重力读数可能很重要。

本质上，本文是对一个关于iSpindel的视频教程的推广，内容涵盖其新功能、平面焊接以及一种特定的平衡方法。

---

## 44. Show HN: Lambduck, 一个函数式编程 Brainfuck

**原文标题**: Show HN: Lambduck, a Functional Programming Brainfuck

**原文链接**: [https://imjakingit.github.io/lambduck/](https://imjakingit.github.io/lambduck/)

Lambduck是一种函数式编程语言，被描述为“函数式编程Brainfuck”。它只有三种特殊形式：lambda 抽象（`\`），使用 De Bruijn 索引进行变量查找（像 0、1、99... 这样的数字）以及函数应用（`\``）。所有其他字符都会被忽略，这使得代码看起来像噪音。

该语言还包括两个内置函数：`,` 从 stdin 读取一个字节，将其转换为 Church 数，并用它调用其参数；而 `.` 解码一个 Church 数参数，取模 256，将其作为一个字节写入 stdout，并返回原始参数。

本文提供了 Lambduck 代码的示例，用于表示 `true` 和 `false`、Z 组合子、一个简单的回显程序以及一个将 "@" 打印到 stdout 的程序。核心概念是使用 lambda 演算、Church 数和策略性放置的忽略字符来执行 I/O 操作。

---

## 45. 医生们正准备摘除他们的器官，然后他们醒了。

**原文标题**: Doctors Were Preparing to Remove Their Organs. Then They Woke Up.

**原文链接**: [https://www.nytimes.com/2025/06/06/us/kentucky-organ-donations.html](https://www.nytimes.com/2025/06/06/us/kentucky-organ-donations.html)

联邦调查揭示肯塔基州一家器官捐献机构存在令人不安的模式，该机构官员忽视了正在考虑循环死亡后器官捐献的患者所表现出的意识迹象。调查审查了四年内最终取消器官移除计划的350个案例。调查发现，在73个案例中，由于患者表现出改善或高度的意识，官员本应更早停止该过程。

报告重点介绍了一个具体案例，一名无意识的男子在准备移除生命支持和器官捐献时开始苏醒，甚至表现出痛苦的迹象。虽然手术最终被取消，但调查显示，多名患者在接受手术准备时表现出疼痛的迹象。大多数患者最终死亡，但也有一些患者康复出院。

调查重点关注“循环死亡后捐献”，这是一种涉及仍有部分脑功能的、靠生命维持且康复希望渺茫的患者的手术。卫生资源和服务管理局的调查结果表明，存在系统性缺陷，未能充分评估患者的意识并做出适当反应，从而引发了对该过程的伦理担忧。

---

## 46. 通用科技树

**原文标题**: The Universal Tech Tree

**原文链接**: [https://asteriskmag.com/issues/10/the-universal-tech-tree](https://asteriskmag.com/issues/10/the-universal-tech-tree)

埃蒂安·福蒂埃-杜布瓦探讨了他的“通用科技树”项目，该项目旨在绘制所有重大技术创新及其在历史上的联系。受文明系列视频游戏中科技树的启发，作者认为技术由先前的技术演变而来，形成一个复杂、相互关联的网络。他通过追溯电影摄影机出人意料的起源——从左轮手枪到科尔特左轮手枪的旋转机制如何影响扬森的“摄影左轮手枪”，后者又启发了马雷的“摄影枪”和爱迪生的电影放映机——来说明这一点。

福蒂埃-杜布瓦详细介绍了构建科技树的方法，该科技树目前包含超过1550项技术和1700个连接，依赖于维基百科、学术文章和他自己的探索。他概述了三个关键的设计选择：将“技术”定义为为实际目的在物理基质中实施的知识；将创新离散化为特定的发明，以维基百科页面为指导；以及将发明的日期定为第一个实际版本。

作者强调了科技树的益处，揭示了意想不到的联系（例如自行车对飞机的影响），并提供了对技术何时出现的更广泛的理解（例如无人机可以追溯到一战时期）。他的目标是创建一个交互式可视化工具，以促进对技术历史及其内在逻辑的更深入理解。

---

## 47. 魔法命名引用

**原文标题**: Magic Namerefs

**原文链接**: [https://gist.github.com/izabera/e4717562e20eb6cfb6e05f8019883efb](https://gist.github.com/izabera/e4717562e20eb6cfb6e05f8019883efb)

Bash名称引用：动态表达式的魔力

本文探讨了bash 4.0引入的bash名称引用的强大而令人惊讶的功能，它能创建动态评估表达式的“魔术变量”。名称引用充当其他变量的别名，允许间接操作。

作者利用此特性以及辅助数组`tmp`，强制进入算术环境，并在名称引用声明中执行任意表达式。这允许创建基于这些表达式更新和返回值的变量。

提供的示例包括一个基本计数器（每次访问时递增）和一个斐波那契数列生成器。这些展示了复杂数值计算的潜力。

文章随后将该概念扩展到数字之外，通过结合美元扩展，实现对系统信息的访问，如日期和时间。一个时钟示例展示了如何使用名称引用通过字符串格式化和变量替换来动态显示当前日期和时间。

作者强调了由此产生的代码的令人惊讶的优雅和简洁性，突出了进一步探索和应用这些技术的潜力。他们认为该技术既强大又优雅。

---

## 48. 指挥你的Claude代码军团

**原文标题**: Commanding Your Claude Code Army

**原文链接**: [https://steipete.me/posts/2025/commanding-your-claude-code-army](https://steipete.me/posts/2025/commanding-your-claude-code-army)

本文探讨了当终端标题仅显示“claude”时，如何管理多个Claude Code实例的问题，这使得区分它们变得困难。作者作为Claude Code的重度用户，提出了一个ZSH解决方案来保持有组织的终端标题。

该解决方案的核心是一个ZSH包装脚本`claude-wrapper.zsh`，它可以动态设置和维护终端标题，以指示当前文件夹以及Claude正在运行。这是通过自定义函数`_set_title`和一个执行Claude Code的`cly`别名来实现的。`cly`别名启动一个后台进程，持续重置终端标题，防止Claude用信息量较少的消息覆盖它。

该脚本还包括一个`_claude_precmd`函数，该函数使用ZSH钩子在每个提示符之前将终端标题重置为当前目录（`%~`）。这确保了即使Claude没有主动运行，标题也是信息丰富的。

该实现涉及在`.zshrc`文件中引入`claude-wrapper.zsh`脚本。通过使用这种设置，作者避免了终端“轮盘赌”，并确保清楚地了解每个终端选项卡中运行的是哪个Claude实例，这在使用`--dangerously-skip-permissions`标志时尤为重要。本文提倡利用Claude本身来实现这种设置，突出了它的实用性。

---

## 49. Dino编程语言及其实现

**原文标题**: Programming language Dino and its implementation

**原文链接**: [https://github.com/dino-lang/dino](https://github.com/dino-lang/dino)

本文介绍了Dino编程语言，这是一种高级的、面向对象的脚本语言，开发版本为0.98。Dino的目标是采用类似C语言的语法，并包含多精度整数、可扩展的数组和切片、关联表、用于继承和特征的强大类组合、头等函数和纤程、异常处理、并发、模式匹配以及Unicode 8支持等特性。

本文讨论了Dino的实现，涵盖了总体结构、使用的工具（COCOM、SPRUT、MSTA、SHILKA、AMMUNITION、GMP、Oniguruma）、字节码编译器优化、带有GC的字节码解释器、并发和REPL、通过C代码生成的JIT编译，以及用于性能的类型推断。计划进行与Python、Ruby和Javascript等其他语言的性能比较。

重点突出的关键特性包括数组切片、带有闭包和匿名函数的函数、用于并发的绿色线程，以及一个通过类组合模拟继承和特征的强大的面向对象模型。Dino还提供使用`pmatch`的模式匹配、使用`rmatch`的正则表达式匹配、使用`try-catch`块的异常处理，以及用于语言原型设计的内置Earley解析器。标准空间（`lang`、`io`、`sys`、`math`、`re`、`yaep`）提供了与核心功能的接口。

---

## 50. Eleven v3

**原文标题**: Eleven v3

**原文链接**: [https://elevenlabs.io/v3](https://elevenlabs.io/v3)

Eleven v3 (alpha) 是 ElevenLabs 最具表现力的文本转语音 (TTS) 模型，通过音频标签增强了对情感、表达和方向的控制。 它能够创建动态的、多说话人的对话，实现听起来自然的对话，并考虑上下文和情感。 该模型支持 70 多种语言，可实现广泛的全球覆盖。

主要亮点包括创建带有情感、音频事件和沉浸式声景的语音，以及生成多个声音之间逼真互动的功能。

Eleven v3 (alpha) 通过其更宽的动态范围（由内联音频标签控制）与之前的模型区分开来。 除了暂停和中断等基本标签外，它还支持全系列的情感、方向和音频效果。

在 2025 年 6 月底之前，自服务用户可以通过 UI 以 2 折优惠购买 alpha 版本。 公共 API 访问计划在未来推出。 该文章通过各种示例和对话场景突出了该模型的功能，强调了其生成类人且引人入胜的音频内容的能力。

---

## 51. 硅谷震惊于马斯克-特朗普决裂

**原文标题**: Silicon Valley aghast at the Musk-Trump divorce

**原文链接**: [https://www.ft.com/content/df15f13d-310f-47a5-89ed-330a6a379068](https://www.ft.com/content/df15f13d-310f-47a5-89ed-330a6a379068)

硅谷对马斯克-特朗普“决裂”感到震惊

文章关注唐纳德·特朗普和埃隆·马斯克之间被认为“决裂”所造成的后果，可能发生在假想的2025年美国政治背景下。 文章强调了双方盟友呼吁和解的声音，表明这次“决裂”被视为具有破坏性。

英国《金融时报》正在向对该文章感兴趣的读者推广其各种订阅级别，这些订阅提供不同级别的访问权限，包括：

*   **FT数字版：** 访问报纸的数字版本。
*   **标准数字版：** 访问FT.com、FT应用程序上的文章以及精选的新闻通讯。
*   **高级数字版：** 完整的数字访问权限，包括高级新闻通讯和专栏。

文章鼓励读者免费注册以接收“白宫观察”新闻通讯，该通讯提供了对特朗普第二个任期对华盛顿、商业和世界的影响的深刻见解。 其他相关的推广内容包括关注美国关税的“特朗普追踪器”以及更广泛的美国政治和政策报道。

---

## 52. 显示HN：通过REST API获取iOS屏幕使用时间

**原文标题**: Show HN: iOS Screen Time from a REST API

**原文链接**: [https://www.thescreentimenetwork.com/api/](https://www.thescreentimenetwork.com/api/)

此“Show HN”提交介绍了“屏幕时间网络”项目，该项目旨在通过 REST API 提供对 iOS 屏幕时间数据的访问。该项目可能涉及逆向工程或利用现有方法从 iOS 设备提取使用数据（尽管提交内容未明确说明如何获取数据）。

其核心优势是使开发者和用户能够以编程方式访问和分析他们的屏幕时间数据。这可能会开启以下可能性：

*   **个性化洞察：** 用户可以创建自定义仪表板、可视化图表和报告，以了解其设备使用模式，超越 iOS 内置工具。
*   **与其他服务集成：** 屏幕时间数据可以与其他个人数据（例如，睡眠跟踪、生产力应用程序）相结合，以更全面地了解个人的数字生活。
*   **研究与开发：** 研究人员和开发人员可以使用该 API 来研究数字健康、创建管理屏幕时间的工具，并探索技术对行为的影响。

虽然提供的上下文有限，但关键在于通过标准 REST API 将 iOS 屏幕时间数据暴露给更广泛的应用和分析的潜力。需要注意的是，访问和使用此类数据可能适用法律和隐私方面的考虑，并且简短的提交内容未提供实施细节。

---

## 53. 多次发明有多常见？

**原文标题**: How Common Is Multiple Invention?

**原文链接**: [https://www.construction-physics.com/p/how-often-do-inventions-have-multiple](https://www.construction-physics.com/p/how-often-do-inventions-have-multiple)

本文探讨了多重发明现象的普遍性，即相同或相似的发明由不同的个人或团队独立开发。作者Brian Potter对此现象进行了调查，旨在深入了解技术进步的本质。

Potter分析了1800年至1970年间的190项重大发明清单，根据发明类型（电气、化学、机械等）和多重性程度进行分类：多次描述、认真的开发努力以及多次成功或接近成功。他还考虑了这些努力是否真正独立，排除了直接抄袭或衍生的案例。

研究表明，多重发明现象的普遍程度令人惊讶。在分析的发明中，超过50%存在某种形式的多重努力，近40%取得了成功或接近成功。作者发现，在研究期间和不同发明类别中，多重发明的比率保持相对稳定。

Potter的结论是，高比例的多重发明表明，许多发明背后的想法通常是“显而易见的”，或者关键问题会吸引众多独立的解决方案尝试。这挑战了技术进步的“伟人理论”，表明进步更多地受到广泛的历史力量和条件的影响，而不是受个人天才的影响。研究结果表明，技术进步较少依赖于特定个人，而更有可能在条件成熟时发生。

---

## 54. 限制网站访问用户本地网络的提议

**原文标题**: A proposal to restrict sites from accessing a users’ local network

**原文链接**: [https://github.com/explainers-by-googlers/local-network-access](https://github.com/explainers-by-googlers/local-network-access)

本文件提出了一种限制网站访问用户本地网络的新方法，旨在防止利用本地设备的漏洞。该提案引入了“本地网络访问”权限，用户必须先明确授予网站该权限，网站才能向私有IP地址或环回地址发出请求。

目前，网站可以自由探测本地网络并执行CSRF攻击。本提案旨在弃用直接访问私有IP地址，将控制权交到用户手中。这与之前依赖设备通过预检请求选择加入的“私有网络访问”提案不同。

该解决方案将“本地网络请求”定义为任何跨地址空间边界向更私有地址空间发出的请求（公网到本地/环回，本地到环回）。它与Fetch API集成，允许开发者使用`targetAddressSpace`选项显式声明目标地址空间，这有助于解决混合内容阻止问题。如果网站在没有权限的情况下发起本地网络请求，则会显示提示，要求用户授予权限。该提案还与WebRTC、权限策略（用于子框架委派）和权限API集成。

目标是允许通过公共Web前端控制本地设备等合法用例，同时防止对本地网络进行不必要的探测。本文档还讨论了处理混合内容、与HTML、WebSocket和Service Worker集成等技术细节。其目的是在安全性和对现有服务的最小干扰之间取得平衡。

---

## 55. 从词元到思想：大型语言模型和人类如何通过压缩换取意义

**原文标题**: From tokens to thoughts: How LLMs and humans trade compression for meaning

**原文链接**: [https://arxiv.org/abs/2505.17117](https://arxiv.org/abs/2505.17117)

从词符到思想：大语言模型与人类如何以压缩换取意义
本文《从词符到思想：大语言模型与人类如何以压缩换取意义》研究了大语言模型（LLMs）和人类如何表示知识和概念范畴。作者Shani等人使用基于率失真理论和信息瓶颈原理的信息论框架，将LLM词符嵌入与人类分类基准进行比较。

核心论点是，虽然LLM可以形成与人类判断相符的广泛概念范畴，但它们难以掌握对人类理解至关重要的细微语义差别。分析揭示了一个根本性的差异：LLM表现出对激进的统计压缩的强烈偏见，优先考虑效率，而人类概念系统则优先考虑适应性细微差别和情境丰富性，即使这会导致效率较低的压缩。

本质上，LLM往往比人类更积极地压缩语义信息，可能牺牲了在更精细的语义区分方面的准确性。该研究突出了当前人工智能和人类认知之间认知架构的一个关键差异，表明未来的研究应侧重于开发具有与人类般的理解和细微差别更一致的概念表示的LLM。研究结果为如何创建不仅捕捉语言的统计模式，而且捕捉人类从中获得的更丰富、上下文相关的意义的人工智能系统提供了见解。

---

## 56. 苹果备忘录将在WWDC获得Markdown导出功能，我有一些想法

**原文标题**: Apple Notes Will Gain Markdown Export at WWDC, and, I Have Thoughts

**原文链接**: [https://daringfireball.net/linked/2025/06/04/apple-notes-markdown](https://daringfireball.net/linked/2025/06/04/apple-notes-markdown)

Daring Fireball 的 John Gruber 谈论了 9to5Mac 报道的关于 Apple Notes 将在 WWDC 上获得 Markdown 导出功能的传闻。Gruber 澄清说，这并不意味着 Apple Notes 会变成像 Bear 或 Obsidian 那样的 Markdown 编辑器，用户可以直接键入和查看 Markdown 语法。他反对将 Apple Notes 变成一个成熟的 Markdown 编辑器，强调它作为 WYSIWYG 富文本编辑器的优势，尤其是在 iPhone 和 Mac 上。他重视它的简单性和有限的格式选项，这使得它对快速记笔记的用户来说非常友好。

Gruber 表达了他个人偏好仅将 Markdown 用于网页写作，并引用了他最初将其定义为“网页写作者的文本到 HTML 转换工具”。他认为 Apple Notes 应该保持其独特性，避免 Markdown 编辑中固有的复杂性和潜在的格式错误语法。

他批评了 Apple Notes 的标签主题的井号标签实现方式，认为标记化的标签（如 Finder 中的标签）会更方便用户使用。

最终，Gruber 对 Apple Notes 导出 Markdown 的前景感到兴奋。他认为当前的导出选项（PDF 和 Pages）不足。他认为 Markdown 导出将是一个有价值的补充，但想知道 Apple 将如何处理 Markdown 输出中的图像。

---

## 57. X修改条款，禁止使用其内容训练人工智能模型

**原文标题**: X changes its terms to bar training of AI models using its content

**原文链接**: [https://techcrunch.com/2025/06/05/x-changes-its-terms-to-bar-training-of-ai-models-using-its-content/](https://techcrunch.com/2025/06/05/x-changes-its-terms-to-bar-training-of-ai-models-using-its-content/)

X (原推特) 已更新其开发者协议，禁止第三方使用其内容来训练大型语言模型 (LLM)。这一变更阻止了各公司使用 X API 或 X 内容来微调或训练 AI 基础模型或前沿模型。

此举紧随埃隆·马斯克的 AI 公司 xAI 于三月份收购 X 之后，表明该公司希望保护专有数据。虽然 X 之前曾在 2023 年更新其隐私政策，允许使用公共数据进行 AI 训练，甚至在去年 10 月允许第三方模型训练，但这项新的限制标志着一个重大转变。

采取这种立场的并非只有 X。Reddit 也已实施针对 AI 爬虫的保护措施，The Browser Company 也在其以 AI 为中心的浏览器 Dia 的使用条款中添加了类似条款。这篇文章表明，平台正变得越来越重视保护其数据，并限制其用于 AI 训练目的，这是一种更广泛的趋势。

---

## 58. 现在是2025年，苹果仍然没有修复音频左右声道平衡的bug。

**原文标题**: It's 2025 and Apple still has not fixed the audio left/right balance bug

**原文链接**: [https://twitter.com/ffaebi/status/1930944771956031954](https://twitter.com/ffaebi/status/1930944771956031954)

提供的內容並非文章，而是一個來自 X（前身為 Twitter）的螢幕截圖或文字片段。它顯示了一條訊息，表明使用者的瀏覽器中已停用 JavaScript。由於 JavaScript 已停用，X 平台無法正常運作。該平台指示使用者啟用 JavaScript 或切換到受支援的瀏覽器，並引導他們前往幫助中心獲取受支援瀏覽器的列表。

並不存在關於 Apple 或音訊錯誤的實際文章內容。“現在是2025年，蘋果仍然沒有修復音訊左右平衡錯誤”這個標題純粹是假設性的，與給定的內容無關。內容僅涉及 X 對 JavaScript 的依賴以及使用者停用的 JavaScript 設定。

---

## 59. Phptop：简单易用的PHP资源分析器，安全可靠，适用于生产环境。

**原文标题**: Phptop: Simple PHP ressource profiler, safe and useful for production sites

**原文链接**: [https://github.com/bearstech/phptop](https://github.com/bearstech/phptop)

Phptop：一款轻量级的PHP资源分析器，专为生产环境设计。由Bearstech开发，它提供类似于'time'命令的单次查询和平均指标，如实际运行时间、CPU使用率（用户和系统）以及内存消耗。多年来，它已在生产服务器上使用，未出现任何问题。

激活非常简单，只需在`php.ini`或`.user.ini`中添加一行代码来预加载`phptop_hook.php`文件，然后重新加载Web服务器（Apache或php-fpm）。收集几分钟的数据后，即可使用`phptop`命令行工具查看资源使用统计信息，并按各种指标排序（例如，使用`phptop -s mem`按内存使用量排序）。

输出会显示URL以及点击数、总时间、用户CPU时间、系统CPU时间、每次点击的平均内存使用量和最大内存使用量等指标。摘要行会显示最近10分钟的总计（默认）。

Phptop兼容PHP 5.2.0及更高版本，已测试到PHP 8.2。该工具的man page提供了有关其操作和选项的更多详细信息。

---

## 60. 有条件地极力捍卫副词

**原文标题**: Defending adverbs exuberantly if conditionally

**原文链接**: [https://countercraft.substack.com/p/defending-adverbs-exuberantly-if](https://countercraft.substack.com/p/defending-adverbs-exuberantly-if)

无法访问文章链接。

---

## 61. 展示HN：代理的容器化应用

**原文标题**: Show HN: Container Use for Agents

**原文链接**: [https://github.com/dagger/container-use](https://github.com/dagger/container-use)

容器使用：为编码代理提供隔离的容器化环境。它允许多个代理安全且独立地运行，从而实现并行执行和实验，避免冲突。

主要功能包括：

*   **隔离环境：** 每个代理在其自身的 git 分支中的全新容器中运行，从而实现安全实验并立即丢弃失败。
*   **实时可见性：** 完整的命令历史记录和日志提供了对代理行为的深入了解。
*   **直接干预：** 使开发人员能够访问代理的终端以检查状态并进行控制。
*   **环境控制：** 利用标准的 git 工作流程来审查代理工作（通过 `git checkout`）。
*   **通用兼容性：** 适用于各种代理、模型和基础设施，防止供应商锁定。

该项目尚处于早期开发阶段，不断改进并可能存在重大更改。

本文还提供了使用 `make` 的安装说明，以及与 Claude Code、goose、Cursor、VSCode 和 GitHub Copilot 集成的说明。 提供了示例用例（hello world、并行应用程序创建、安全扫描），以及有关如何使用 Claude Code 和 goose 运行这些示例的说明。 `cu watch` 允许实时监控代理进度，因为代理会提交到本地文件系统上的 container-use 远程存储库。

---

## 62. 我不记得我的生活，这样也挺好。

**原文标题**: I do not remember my life and it's fine

**原文链接**: [https://aethermug.com/posts/i-do-not-remember-my-life-and-it-s-fine](https://aethermug.com/posts/i-do-not-remember-my-life-and-it-s-fine)

在《我不记得我的生活，但一切都好》一书中，患有失忆症（无法形成心理图像）的马可·詹科蒂探讨了他患有严重自传体记忆缺失症（SDAM）的经历。SDAM是一种与失忆症相关的疾病，会削弱人们生动回忆过去事件的能力。

詹科蒂描述了他如何努力“重温”过去的事件，导致记忆空白，使得特定事件模糊成一般的回忆。他用轶事来说明这一点，例如他难以回忆起某个特定的大学问题用于求职申请，或生动地回忆起与祖父的经历。他指出，虽然他可以回忆起事实和总体感受，但缺乏详细的情景记忆使他的过去感觉遥远，就像别人的生活一样。

尽管存在这些局限性，詹科蒂强调他的实际能力并没有受到显着阻碍。他拥有强大的语义记忆（事实和知识）和空间记忆，他利用这些记忆来弥补他缺失的情景记忆。他使用“嗖嗖效应”，即空间线索触发大量相关的记忆，以此来重建过去的事件。

詹科蒂引用研究表明，失忆症患者在记忆形成过程中可能存在大脑活动差异，但可以发展出补偿策略。他认为，虽然缺乏情景回忆会带来情感上的负面影响，但并不会削弱他的行动能力。

---

## 63. Show HN: ClickStack – 基于 ClickHouse 和 HyperDX 的开源 Datadog 替代方案

**原文标题**: Show HN: ClickStack – Open-source Datadog alternative by ClickHouse and HyperDX

**原文链接**: [https://github.com/hyperdxio/hyperdx](https://github.com/hyperdxio/hyperdx)

HyperDX：基于 ClickHouse 的开源可观测性平台

HyperDX 作为 ClickStack 的核心组件，被定位为 Datadog 的开源替代方案，利用 ClickHouse 实现快速且可扩展的可观测性。它使工程师能够在 ClickHouse 集群中高效地搜索和可视化日志、追踪、指标和会话回放。主要功能包括与模式无关的数据摄取、全文和属性搜索、异常趋势分析、告警以及高基数仪表盘，并支持原生 JSON 字符串查询。它开箱即用地支持 OpenTelemetry，并提供 APM 功能。

本文详细介绍了如何使用 Docker 作为 ClickStack 的一部分来启动 HyperDX，或者使用现有的 ClickHouse 实例，文档中也提供了部署选项。HyperDX 也可以通过 ClickHouse Cloud 部署。通过提供的适用于各种语言（浏览器、Node.js、Python 等）的 SDK 和 OpenTelemetry 兼容性，可以轻松实现检测。

HyperDX 背后的动机是为生产遥测提供经济高效且用户友好的解决方案，解决现有昂贵且复杂工具的缺点。该项目欢迎贡献，并提供各种联系和反馈渠道。它还会收集匿名使用数据以支持其开源开发，并提供退出选项。它在 MIT 许可下发布。

---

## 64. 特朗普“金色穹顶”计划遭遇重大阻碍：物理学

**原文标题**: Trump's 'Golden Dome' plan has a major obstacle: Physics

**原文链接**: [https://www.sciencenews.org/article/golden-dome-missile-defense-physics](https://www.sciencenews.org/article/golden-dome-missile-defense-physics)

本文讨论了特朗普总统旨在保护美国免受来自俄罗斯、中国和朝鲜等国的洲际弹道导弹、高超音速武器和先进巡航导弹攻击的下一代导弹防御系统“金穹顶”计划。特朗普声称该计划将在其任期结束前投入使用，耗资1750亿美元。

然而，该计划面临来自科学家的严重质疑。美国物理学会的一份报告表明，即使是防御小规模洲际弹道导弹袭击，当前系统也存在不确定性，且未来15年的改进仍然有限。“金穹顶”计划旨在利用陆基系统和数千个天基拦截器实现更具雄心的防御。

虽然支持者认为发射成本降低使得天基防御成为可能，但批评者强调物理定律是不变的。拦截以极高速度飞行的洲际弹道导弹极其具有挑战性，尤其是在对手部署诱饵等对抗措施时。洲际弹道导弹飞行中段阶段在区分太空中的弹头和诱饵方面存在困难。助推段拦截需要拦截器非常靠近发射地点，因此需要大量卫星。

专家质疑“金穹顶”计划的可行性，尤其考虑到其成本和部署的短时间框架。虽然导弹防御在乌克兰和以色列等冲突中发挥了作用，但这些涉及不同类型的导弹。在没有明确规定要拦截来自特定国家的洲际弹道导弹数量的情况下，该计划的合理性仍然不明确。文章最后强调了导弹防御背后的复杂现实，以及对各种因素进行仔细考虑的必要性。

---

## 65. 推特新加密私信不如旧的。

**原文标题**: Twitter's new encrypted DMs aren't better than the old ones

**原文链接**: [https://mjg59.dreamwidth.org/71646.html](https://mjg59.dreamwidth.org/71646.html)

提供的文本并非文章，而是看起来像是验证码检查的一段代码。因此，没有可供总结的文章。这段文本仅表明用户已被选中完成验证码测试以验证其请求，表明系统怀疑他们可能是机器人。文本中没有任何关于Twitter加密私信或其功能的信息。由于提示的前提不正确，因此无法进行总结。

---

## 66. 数字大臣希望以开放标准和开源作为指导原则。

**原文标题**: Digital Minister wants open standards and open source as guiding principle

**原文链接**: [https://www.heise.de/en/news/Digital-Minister-wants-open-standards-and-open-source-as-guiding-principle-10414632.html](https://www.heise.de/en/news/Digital-Minister-wants-open-standards-and-open-source-as-guiding-principle-10414632.html)

数字化部长倡导以开放标准和开源为指导原则——文章摘要：

德国新任数字化部长沃尔克·维辛倡导将开放标准和开源软件作为该国数字化工作的指导原则。他认为这些原则对于促进创新、竞争和数字主权至关重要。

维辛强调需要减少对专有解决方案的依赖，避免厂商锁定。开放标准确保互操作性，并允许不同的系统和服务进行有效通信，而开源代码则实现了透明性、可审计性和协作开发。他认为这种方法对于构建具有弹性和安全的数字基础设施至关重要。

具体来说，维辛希望开放标准和开源软件成为政府数字化项目的首选，包括电子政务服务、数据管理和网络安全等领域。他承认需要解决对安全和维护的担忧，但他相信这些可以通过适当的实施和社区支持来有效管理。最终目标是在德国营造一个更加透明、更具竞争力和更具创新性的数字环境。

---

## 67. 货运铁路催生新型豪华卧铺列车初创公司

**原文标题**: Freight rail fueled a new luxury overnight train startup

**原文链接**: [https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup](https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup)

梦星，一家新兴客运铁路初创公司，旨在重振洛杉矶和旧金山之间的豪华夜间火车旅行，让人想起20世纪50年代之前的时代。联合创始人约书亚·多米尼克和托马斯·伊斯特蒙德设想提供一种全卧室住宿、美食餐饮和五星级酒店服务的服务，以解决他们认为美国缺乏舒适的中等距离旅行选择的问题。

他们计划的一个关键要素是利用货运铁路基础设施。梦星与联合太平洋铁路公司（UP）就圣何塞和文图拉之间400英里路段的轨道接入达成了谅解备忘录，该路段的夜间货运交通量很少。联合太平洋铁路公司已确认正在进行正式谈判。该公司还在与加州火车、Metrolink和洛杉矶联合客运总站达成协议。

梦星计划提供有限停靠的夜间服务，并声称其列车产生的二氧化碳排放量将比飞行减少75%。定价将与航班和酒店或商务舱航班具有竞争力。

该设计与宝马Designworks合作开发，设有四个等级的私人客舱、休息室、用餐空间，甚至还有一个水疗中心，模仿了圣达菲埃尔卡皮坦等列车的特色。他们还设想提供“汽车渡轮”服务。虽然最初的计划是建造新列车，但梦星现在计划重建现有铁路车辆。机车车辆的建造预计需要18-24个月，目标是在2028年洛杉矶奥运会之前开始运营。房屋建筑商比尔·里昂已投资10万美元，其他投资者包括房地产家族和天使投资者。该公司正在与行业专家合作，以获得监管部门的批准，并将资本效率放在首位。

---

## 68. 阿梅莉亚·埃尔哈特的鲁莽终极飞行

**原文标题**: Amelia Earhart's Reckless Final Flights

**原文链接**: [https://www.newyorker.com/magazine/2025/06/09/amelia-earharts-reckless-final-flights](https://www.newyorker.com/magazine/2025/06/09/amelia-earharts-reckless-final-flights)

本文详细叙述了阿梅莉亚·埃尔哈特第二次环球飞行悲剧性的尝试，着重讲述了她准备不足以及她的丈夫兼公关乔治·帕尔默·普特南的影响。 首次尝试以在檀香山迫降告终，暴露了埃尔哈特在飞行方面的挣扎以及对经验丰富的飞行员保罗·曼茨的依赖。 普特南将这次坠机轻描淡写为轮胎问题。

本文揭示了埃尔哈特的同行和专家（如布拉德福德·瓦什伯恩）对她的导航技能以及在关键的豪兰岛航段依赖“航位推算”的担忧。普特南将宣传和圣诞节书籍发行置于安全预防措施之上，例如在豪兰岛安装无线电信标。

坠机后，导航员哈里·曼宁以无线电纪律松懈为由辞职，而弗雷德·努南尽管有可疑的清醒度，还是被选为替代者。 其他有成就的女飞行员，如埃莉诺·史密斯，质疑埃尔哈特的技能，并暗示普特南优先考虑名声而非能力。 史密斯甚至回忆说，普特南曾向她提供一份工作，让她在女子飞行比赛期间秘密为埃尔哈特飞行。

本文将埃尔哈特描绘成一个开拓者，她的野心受到了对名声无情的追求的推动，而这是由普特南精心策划的，他愿意冒险，可能危及她的生命以及机组人员的生命。

---

## 69. 机器码并不可怕

**原文标题**: Machine Code Isn't Scary

**原文链接**: [https://jimmyhmiller.com/machine-code-isnt-scary](https://jimmyhmiller.com/machine-code-isnt-scary)

机器码并不可怕：本文认为，即使是习惯于高级语言的程序员也能理解机器码。作者回顾了最初对底层编程的恐惧，并强调克服这种恐惧是有益的。

文章将机器码分解为三个核心概念：**指令**、**寄存器**和**内存**。指令是规定机器操作的数字代码，接受常量（“立即数”）、寄存器（类似于变量）或内存地址（类似于列表）等参数。寄存器是用于存储数值的小型存储位置，而内存是更广泛的存储空间。

文章以 ARM 64 位 (AArch64) 为主要示例，解释了“加立即数”等指令是如何使用二进制表示进行构造和编码的。它说明了寄存器是如何编号和使用的，以及“存储” (STR) 指令如何允许将值写入具有偏移量的特定内存地址。

然后，它简要介绍了 x86-64，强调了它与 ARM 的不同之处，特别是其可变宽度指令集。它介绍了关键组件，如 REX 前缀、ModR/M 字节（定义模式和寄存器使用）以及操作码。

作者最后鼓励读者探索机器码和底层编程。他们强调，虽然还需要进一步学习（标志、调用约定、堆栈、跳转），但理解基础知识可以显著提高整体编程知识，并消除与仅依赖高级抽象和文档不完善的底层系统相关的心理障碍。

---

## 70. 拉布拉多海岸惊现罕见黑色冰山，或有十万年历史

**原文标题**: Rare black iceberg spotted off Labrador coast could be 100k years old

**原文链接**: [https://www.cbc.ca/news/canada/newfoundland-labrador/black-iceberg-labrador-coast-1.7551078](https://www.cbc.ca/news/canada/newfoundland-labrador/black-iceberg-labrador-coast-1.7551078)

拉布拉多海岸罕见黑色冰山引人注目。卡本尼尔（Carbonear, N.L.）的渔民 Hallur Antoniussen 五月中旬捕虾时拍摄了这座冰山。与因夹带岩石和泥土而变色的冰山不同，这座冰山整体呈黑色，近乎菱形。

纪念大学教授 Lev Tarasov 估计，这座冰山的冰可能来自格陵兰岛，已有 1,000 至 100,000 年的历史。他解释说，冰流将冰从内陆带到海岸，携带的岩石和沉积物被磨成粉末并散布在整个冰中。从格陵兰岛到纽芬兰和拉布拉多的旅程可能需要一到三年。

Tarasov 认为，这座冰山可能已经翻转，露出了底部。他还认为，黑色可能归因于格陵兰西北部陨石撞击产生的尘埃。无论确切原因如何，Tarasov 强调了冰山的年龄以及冰的动态特性，可能包含数十万年来未见过的物质。这一独特的景象引发了在线猜测，从石油矿藏到隐藏的恐龙，同时也突出了塑造冰山的地质过程。

---

## 71. AGI并非多模态

**原文标题**: AGI is not multimodal

**原文链接**: [https://thegradient.pub/agi-is-not-multimodal/](https://thegradient.pub/agi-is-not-multimodal/)

多模态人工智能趋势难以实现真正通用人工智能

---

## 72. 关于电磁脉冲武器你需要知道的

**原文标题**: What you need to know about EMP weapons

**原文链接**: [https://www.aardvark.co.nz/daily/2025/0606.shtml](https://www.aardvark.co.nz/daily/2025/0606.shtml)

这篇《土豚日报》的文章讨论了电磁脉冲（EMP）武器的威胁，特别是高空核爆炸产生的电磁脉冲。文章解释说，电磁脉冲不仅仅受平方反比定律支配，而且由于伽马辐射与地球磁场的相互作用，会影响大片区域。

文章概述了电磁脉冲产生的三个阶段：E1（微秒级，高频，烧毁电子设备），E2（毫秒到秒级，千赫兹到低兆赫兹范围，更容易防护）和E3（分钟级，低频，破坏电力线路和能源基础设施）。

缓解策略主要围绕使用法拉第笼，这是一种多层导电屏蔽层，可以重新定向电磁脉冲能量。文章强调了导电层中没有间隙或孔洞的重要性，设备的完全封闭，以及防止设备与屏蔽层直接接触。

文章提供了一种在核事件期间保护小型电子设备的DIY解决方案，建议将设备包裹在多层塑料薄膜和铝箔中。文章还指出，化油器汽车和电子管收音机等老式技术比依赖现代微芯片的设备更能抵抗电磁脉冲。作者最后讽刺地承认，对现代技术的依赖使得电磁脉冲造成的破坏更具影响力。

---

## 73. 根据一项大型美国研究，种族、族裔与遗传祖源不完全匹配。

**原文标题**: Race, ethnicity don't match genetic ancestry, according to a large U.S. study

**原文链接**: [https://www.science.org/content/article/race-ethnicity-don-t-match-genetic-ancestry-according-large-u-s-study](https://www.science.org/content/article/race-ethnicity-don-t-match-genetic-ancestry-according-large-u-s-study)

无法访问文章链接。

---

## 74. 使用Axum进行身份验证

**原文标题**: Authentication with Axum

**原文链接**: [https://mattrighetti.com/2025/05/03/authentication-with-axum](https://mattrighetti.com/2025/05/03/authentication-with-axum)

本文探讨了在Axum中实现用户身份验证，重点关注基于Cookie的服务器端渲染（SSR）应用程序的身份验证。它首先阐述了一个常见场景：一个导航栏根据身份验证状态动态显示“个人资料”或“登录”。

本文强调了Cookie的安全优势，详细介绍了`HttpOnly`、`Secure`和`SameSite`等属性，以减轻常见的Web漏洞。 然后介绍了`axum-extra` crate，特别是用于简化Cookie管理的`CookieJar`提取器。 建议使用存储在Cookie中的JWT以及刷新令牌。

本文提供了用于设置`jwt`（短时有效）和`refresh`（长时有效）Cookie的登录端点的代码片段。 它最初使用Axum提取器`CookieJwt<T>`从JWT Cookie中提取用户数据。 如果JWT有效，则用户通过身份验证；如果存在刷新令牌但JWT无效，则用户将被重定向到`/refresh_token`端点以获取新的JWT。

然后，作者指出了使用提取器进行身份验证的局限性：感觉不太正确，缺乏处理复杂角色和场景的灵活性，并且可能在重定向期间破坏POST请求。 本文过渡到将身份验证实现为Axum中间件。

最后一部分概述了Axum中中间件函数的结构，并提供了一个示例，该示例检查JWT和刷新Cookie以建立`UserContext`，该`UserContext`管理Cookie更新并确定用户身份验证状态。 该中间件处理JWT验证、刷新令牌逻辑并清除可能已泄露的Cookie，从而为保护路由提供更简洁、可重用的解决方案。

---

## 75. 无人机竞速：自主无人机首胜人类冠军

**原文标题**: Autonomous drone defeats human champions in racing first

**原文链接**: [https://www.tudelft.nl/en/2025/lr/autonomous-drone-from-tu-delft-defeats-human-champions-in-historic-racing-first](https://www.tudelft.nl/en/2025/lr/autonomous-drone-from-tu-delft-defeats-human-champions-in-historic-racing-first)

在阿布扎比举行的A2RL无人机锦标赛中，代尔夫特理工大学开发的自主无人机战胜了人类冠军，这是一项突破性成就，标志着人工智能首次在国际无人机竞速比赛中战胜人类飞行员。 该无人机仅配备一个前置摄像头，与另外13架自主无人机以及顶级人类无人机竞速专业人士展开了竞争。

代尔夫特理工大学团队通过开发一种高效且强大的AI系统实现了这一壮举，该系统采用深度神经网络直接控制无人机的电机。 该AI系统使用强化学习进行训练，使其能够无限接近无人机的物理极限。 团队的成就超越了以前在人工智能领域的突破，如国际象棋或围棋，因为它发生在现实世界中，而不是受控环境中。

A2RL无人机锦标赛旨在通过在极端压力和有限资源下测试机器人AI，从而推动物理AI的边界。 该AI以高达95.8公里/小时的速度在复杂赛道上导航的成功，对其他机器人应用具有重要意义。 代尔夫特理工大学团队表示，开发的AI可用于从自动驾驶汽车到救灾等各种应用，并可能彻底改变对时间、安全或能源优化有需求的领域。

---

## 76. 比较Claude系统提示词揭示Anthropic的优先事项

**原文标题**: Comparing Claude System Prompts Reveal Anthropic's Priorities

**原文链接**: [https://www.dbreunig.com/2025/06/03/comparing-system-prompts-across-claude-versions.html](https://www.dbreunig.com/2025/06/03/comparing-system-prompts-across-claude-versions.html)

本文分析了 Claude 3.7 和 Claude 4.0 系统提示词之间的差异，揭示了 Anthropic 在塑造其聊天机器人行为和用户体验方面的优先事项。这些变化突显了一个以用户驱动的开发周期，其中观察到的用户互动会影响系统提示词中的即时“热修复”调整以及后续模型发布的长期后训练策略。

主要结论包括：

*   **热修复移除：** 解决了常见 LLM 问题的旧热修复已被移除，表明这些问题现在已在 Claude 4.0 的后训练中得到解决。添加了新的热修复，例如防止过度奉承的回复，以解决最近的问题，展示了提示词的反应作用。
*   **强调搜索：** 鼓励 Claude 4.0 主动使用搜索，特别是对于时间敏感的查询，表明对其搜索能力的信心增强，并反映了用户对最新信息的需求。
*   **结构化文档使用：** 提示词指定了更广泛的结构化内容，例如膳食计划和学习指南，供 Claude 生成为成品，反映了用户对这些格式的偏好。
*   **上下文限制问题：** 关于在代码中使用简洁变量名的指令表明 Anthropic 正在解决上下文限制问题，承认与 Gemini 和 GPT 等竞争对手相比，存在潜在的劣势。
*   **网络安全防护：** 实施了更严格的指南来防止代码的恶意使用，突显了对网络安全的高度关注。

本文强调，系统提示词是聊天机器人设计的一个关键方面，通过塑造模型的行为和优先事项来定义用户体验。Claude 系统提示词的演变展示了 Anthropic 以用户为中心的迭代式聊天机器人开发方法。

---

## 77. 科里·多克托罗谈我们是如何失去互联网的

**原文标题**: Cory Doctorow on how we lost the internet

**原文链接**: [https://lwn.net/Articles/1021871/](https://lwn.net/Articles/1021871/)

科里·多克托罗的PyCon US 2025主题演讲探讨了互联网的衰败，他称之为“垃圾化”。他将垃圾化解释为一个三阶段过程：首先，平台提供优质服务并锁定用户；其次，它降低用户体验以惠及商业客户；最后，它榨取最大价值，仅留下最低限度可行的服务以保留用户和客户。谷歌搜索引擎就是一个典型的例子，其搜索准确性下降且存在合谋广告行为。

多克托罗将这种衰败归因于“调整”，即通过算法操纵平台功能和定价的能力，并以“零工经济”中的算法工资歧视为例，比如护理应用程序和优步。他驳斥了为服务付费就能消除问题的观点，指出即使是向用户收费的苹果公司，也在进行监控，并将用户和应用程序供应商都视为产品。

他认为，导致垃圾化的是政策变化，而非技术转变。他提出了四种可以防止垃圾化的制约因素：市场、监管、互操作性和员工行动。然而，反垄断法削弱了市场竞争，监管机构常常被行业俘获，隐私法也已过时。多克托罗总结说，扭转这些有害政策并促进互操作性对于夺回互联网至关重要。

---

## 78. Show HN：GPT图像编辑，3D模型版

**原文标题**: Show HN: GPT image editing, but for 3D models

**原文链接**: [https://www.adamcad.com/](https://www.adamcad.com/)

AdamCAD是一个人工智能驱动的CAD平台，允许用户使用自然语言提示或图像生成和编辑3D模型。它提供文本到CAD和图像到3D功能，承诺快速生成设计。用户可以用文本描述他们想要的3D模型，AdamCAD将生成该模型，并提供一系列可调节的参数以供进一步完善。或者，用户可以上传图像，AdamCAD将基于该图像创建3D模型。

该平台旨在与专业人士使用的现有CAD软件集成，充当人工智能副驾驶。它支持各种应用，从工业设计到机械工程，并提供潜在用例的示例，如设计凸轮轴、生成齿轮、创建手机支架等等。其目的是让用户能够使用自然语言输入快速实现他们的想法。该网站重点介绍了诸如文本到CAD、细化和导出3D模型以及图像到3D创建等功能。可以通过电子邮件联系该公司。

---

## 79. Doge开发出易出错的AI工具，以“吞噬”退伍军人事务部合同

**原文标题**: Doge Developed Error-Prone AI Tool to "Munch" Veterans Affairs Contracts

**原文链接**: [https://www.propublica.org/article/trump-doge-veterans-affairs-ai-contracts-health-care](https://www.propublica.org/article/trump-doge-veterans-affairs-ai-contracts-health-care)

2025年，特朗普政府时期埃隆·马斯克领导下的政府效率部(DOGE)指派一位没有医学经验的软件工程师开发一款人工智能工具，以识别并取消退伍军人事务部(VA)的合同。这款由Sahil Lavingia创建的工具将合同标记为“可取消”。

这款人工智能使用过时模型，造成重大错误，例如严重误算合同价值。虽然退伍军人事务部总体上取消了近600份合同，但尚不清楚有多少合同源自DOGE工具，但至少有二十几份已被确认。这些被取消的合同包括基因测序癌症治疗和血液样本研究分析等基本服务。

人工智能和采购专家批评该工具存在缺陷且问题严重，认为使用人工智能在退伍军人事务部进行预算削减是不明智的。该人工智能缺乏关于退伍军人事务部运营、重要合同和法律要求的关键背景信息，导致其标记了核心采购系统。

Lavingia承认代码存在缺陷，将其归因于时间限制和技术局限性。后来，据报道在马斯克的批准下，他将代码开源，导致他最终被政府效率部解雇。虽然退伍军人事务部声称合同是在人工审查后终止的，但工作人员报告称，他们只有很少的时间来证明保留服务的合理性。

这篇文章强调了依赖容易出错的人工智能做出关键决定的潜在危险，尤其是在处理基本的退伍军人服务时。尽管存在错误，但退伍军人事务部仍然愿意使用人工智能来取代员工。

---

## 80. 构建智能体的实用指南 [pdf]

**原文标题**: A practical guide to building agents [pdf]

**原文链接**: [https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

由于存在无法读取的字符，该文档看起来是二进制格式，可能是一个压缩的PDF文件。因此，无法对其内容进行适当的总结。

要创建摘要，需要对该PDF文件进行适当的处理并转换为可读格式，如果它是基于图像的PDF，则可能需要进行OCR处理。

---

## 81. Show HN: String Flux – 简化开发者日常字符串转换

**原文标题**: Show HN: String Flux – Simplify everyday string transformations for developers

**原文链接**: [https://stringflux.io](https://stringflux.io)

StringFlux是一款基于网络的工具，旨在简化和精简开发者字符串转换流程。它允许用户像命令行管道一样将多个操作链接在一起，从而在单个统一的界面中实现复杂的转换。这种方法对于从JSON日志中提取和格式化堆栈跟踪等任务特别有用。

StringFlux支持各种操作，包括JSON格式化和压缩、JSON到YAML转换、Base64和URL编码/解码等。该平台优先考虑直观的用户体验，提供智能推荐、搜索功能和分类操作，以简化选择过程。

主要功能包括创建转换链、将选定内容复制到新编辑器以进行有针对性的转换，以及修复格式错误的JSON中的常见错误。它还允许通过可共享链接共享转换链以进行协作。StringFlux旨在通过为日常字符串操作需求提供集中、高效的解决方案来提高开发人员的工作效率。该平台支持各种格式化、转换、编码/解码、转义/反转义、安全/哈希以及诸如大小写转换之类的其他操作。开发人员正在积极寻求用户反馈，以进一步改进StringFlux。

---

## 82. SP80突破100公里时速（航行）大关

**原文标题**: SP80 Breaks the 100kph (sailing) Barrier

**原文链接**: [https://sp80.ch/sp80-smashes-the-mythical-100-km-h-barrier/](https://sp80.ch/sp80-smashes-the-mythical-100-km-h-barrier/)

SP80团队在打破世界帆船速度纪录的征程中取得重大进展，其风筝帆船最高速度达到58.261节（108公里/小时），成为有史以来第二快的帆船，超过了美洲杯（AC75）和帆船大奖赛（F50）帆船的速度。 该团队目前专注于在500米内实现持续的高平均速度，以获得官方世界纪录认证。

虽然他们的峰值速度不符合纪录资格，但他们多次达到55至58节之间的速度，证明了该船的潜力和可靠性。 眼前的目标是保持超过50节的速度超过500米，以打破目前由Macquarie Innovation和l'Hydroptère保持的类别记录。 他们在500米内实现了48.645节的平均速度，表明他们正在接近目标。

最终目标仍然是超越Vestas Sailrocket II创造的65.45节的绝对世界帆船速度纪录。 该团队有信心通过不断改进操控和数据分析，他们可以达到打破纪录所需的必要速度。 他们正专注于提高协调性，并学习该船在超过100公里/小时的速度下的表现。

---

## 83. 我出卖给谷歌的那个时代的黑暗反乌托邦故事

**原文标题**: Dystopian tales of that time when I sold out to Google

**原文链接**: [https://wordsmith.social/elilla/deep-in-mordor-where-the-shadows-lie-dystopian-stories-of-my-time-as-a-googler](https://wordsmith.social/elilla/deep-in-mordor-where-the-shadows-lie-dystopian-stories-of-my-time-as-a-googler)

这篇博文详细描述了作者2007年在巴西谷歌公司工作时的幻灭经历，重点讲述了该公司公共形象与其内部现实之间的差距。 谷歌一直被宣传为“最佳工作场所”，倡导开放标准，并通过“20%时间”给予员工自由。 然而，作者发现自己陷入了修复枯燥乏味的bug和过度劳累的困境，而承诺的20%时间成了一个无法实现的白日梦。

在内部博客文章中抱怨“20%时间”的承诺无法兑现后，作者因“背后捅刀”她的老板而受到斥责，突显了谷歌对其“彻底透明”的主张，却不能容忍负面情绪。 该文章进一步详细描述了她创建了一个IRC机器人来访问公司词汇表，结果导致临时工、兼职人员和合同工被拒绝访问该词汇表网站。 作者强调了谷歌创建了一个等级制度，这些工人被视为二等公民。

作者回忆起一个事件，一位AdSense员工要求她提供巴西同性恋俚语用于广告目的，这说明了该公司操纵人们购买劣质产品的隐藏议程。 她对这种不道德行为感到不安，更糟糕的是，她后来因在公司个人资料中声明自己的性取向和父母身份而被斥责为“过于个人化”。

最后，作者讨论了谷歌员工既“备受呵护”又“薪酬过低”的矛盾说法。 她描述了该公司如何利用福利和承诺来激励员工，但他们的薪酬甚至低于当地市场水平。 作者无法忽视临时工、兼职人员和合同工的困境，他们被排除在全职员工享有的福利之外。

---

## 84. 视频生成中可能未被充分重视的方面 (Andrej Karpathy)

**原文标题**: Aspects to video generation that may not be fully appreciated (Andrej Karpathy)

**原文链接**: [https://twitter.com/karpathy/status/1929634696474120576](https://twitter.com/karpathy/status/1929634696474120576)

提供的文本**并非文章**。 它只是X（前Twitter）上的一段文字，表明JavaScript已禁用，因此无法显示内容（可能是Andrej Karpathy关于视频生成的帖子）。

因此，**不可能根据提供的信息总结文章内容**。 我们只知道Andrej Karpathy可能在X上发布了一些与视频生成方面可能被低估的问题有关的内容。要理解其内容，需要：

1. 在浏览器中启用JavaScript。
2. 访问X (Twitter) 并找到 Andrej Karpathy 关于该主题的帖子。

在无法访问实际内容的情况下，任何总结都纯属猜测。

---

## 85. 马嚼子，沿用数千年，今被重新审视

**原文标题**: Horse Bits, Used for Thousands of Years. Now Being Reconsidered

**原文链接**: [https://www.nytimes.com/2025/06/04/sports/horse-racing/horse-bits-reconsidered.html](https://www.nytimes.com/2025/06/04/sports/horse-racing/horse-bits-reconsidered.html)

本文着重介绍了布伦丹·怀斯，一位无嚼环骑乘马匹的场地障碍赛骑手，他通过无嚼环骑乘他的马匹维拉努埃瓦·康拉德（抒情），挑战了传统的马术实践。传统上，骑手使用放置在马口中的金属嚼环来控制和引导马匹。然而，怀斯仅使用腿部压力和一根绕在抒情脖子上的绳索进行引导，在高水平比赛（大奖赛，1.40米跳跃）中竞争。

文章强调怀斯的方法质疑了马术运动中使用嚼环的必要性。他认为，如果不用嚼环也能取得相当的成绩，就应该重新考虑使用嚼环。怀斯的成功表明，无嚼环骑乘不仅仅是一种技巧，而是一种可行的方法，即使在竞争性环境中也是如此。

怀斯的主要目标并非总是获胜，而是展示替代骑乘技术的潜力，并鼓励更广泛地讨论马术界公认的规范。他并非完全谴责嚼环，而是促使骑手们质疑其固有的必要性，并探索与马匹沟通和控制的其他可能性。

---

## 86. 理解 PURL 规范（软件包 URL）

**原文标题**: Understanding the PURL Specification (Package URL)

**原文链接**: [https://fossa.com/blog/understanding-purl-specification-package-url/](https://fossa.com/blog/understanding-purl-specification-package-url/)

Package URL (PURL) 规范是一种开放标准，用于跨不同生态系统唯一标识软件包。它创建于 2017 年，旨在简化软件组件的跟踪和共享，尤其是在 SBOM 环境中。PURL 是一种特殊格式的 URL，编码了软件包类型、命名空间、名称、版本、限定符和子路径。

虽然从验证的角度来看所有字段都是可选的，但命名空间和版本对于所有生态系统都很重要，而限定符和子路径对于 Linux 生态系统尤其重要。

PURL 支持多种生态系统，例如 npm、Maven 和 PyPI，定义了如何解释每个生态系统的命名空间和限定符。它是 SBOM 中的一个关键要素，充当软件组件的唯一标识符。虽然 NTIA 没有明确要求，但 PURL 被认为是 SBOM 准确性和可用性的最佳选择，能够丰富许可和漏洞信息。CycloneDX 和 SPDX SBOM 格式都支持 PURL。

与 CPE（通用平台枚举）相比，PURL 侧重于软件包，与开发人员的实践和开源生态系统保持一致。CPE 专为 IT 产品设计，具有严格的格式，并且需要引用字典进行命名。PURL 更简单，直接使用来自软件包生态系统的名称，并且需要较少的外部知识。因此，PURL 更好地处理了开源依赖项的“长尾”，而 CPE 对商业产品的支持更好。总而言之，PURL 是软件供应链透明度和安全性的重要工具。

---

## 87. Infomaniak力挺备受争议的瑞士加密法

**原文标题**: Infomaniak comes out in support of controversial Swiss encryption law

**原文链接**: [https://www.tomsguide.com/computing/vpns/infomaniak-breaks-rank-and-comes-out-in-support-of-controversial-swiss-encryption-law](https://www.tomsguide.com/computing/vpns/infomaniak-breaks-rank-and-comes-out-in-support-of-controversial-swiss-encryption-law)

这篇Tom's Guide文章讨论了围绕瑞士加密法律拟议变更的争议，这些变更将扩大监控义务，并要求公司收集用户身份信息。这引起了强烈反对，尤其是来自像Proton VPN这样注重隐私的VPN提供商，其CEO表示该公司宁愿搬迁也不愿损害用户隐私。

尽管反对声众多，瑞士云安全公司Infomaniak却支持该法律。Infomaniak的发言人辩称，匿名阻碍了正义，需要取得平衡以防止“数字蛮荒”。他们还批评了免费VPN，声称它们允许个人躲避法律。

文章对Infomaniak的立场提出了质疑，澄清Proton倡导的是隐私而非匿名，混淆两者是一种常见的误解。文章还强调，VPN，尤其是免费VPN，对于生活在审查制度和互联网限制下的人们至关重要。

文章强调Infomaniak接受元数据收集，认为这对于起诉非法活动是必要的。然而，批评人士认为，元数据收集构成重大隐私风险。最后，文章提到Infomaniak正在转向加密电子邮件服务，但仍将收集用户的元数据。瑞士政府对拟议法律的咨询已于2024年5月结束，调查结果待定。

---

## 88. 鹦鹉直播

**原文标题**: parrot.live

**原文链接**: [https://github.com/hugomd/parrot.live](https://github.com/hugomd/parrot.live)

Parrot.live 是一个项目，允许用户使用 `curl` 命令在终端中显示一个动画派对鹦鹉。它利用 "terminal-parrot" 项目的帧来创建动画。用户只需在终端中运行 `curl parrot.live` 即可看到派对鹦鹉。该项目感谢 jmhobbs 创作原始 terminal-parrot 和动画帧，并感谢 Robert Koch 和 Eric Jiang 的测试和反馈。该页面还提供了其他相关的鹦鹉主题资源链接，包括 "cultofthepartyparrot.com" 网站、"terminal-parrot" 项目本身、"parrotsay" (可能是一个鹦鹉主题的 `say` 命令) 和 "ascii.live"。本质上，parrot.live 提供了一种快速简便的方法，可以为任何终端环境增添乐趣和动画效果。

---

## 89. 双 RTX 5060 Ti 16GB 对比 RTX 3090 用于本地 LLM

**原文标题**: Dual RTX 5060 Ti 16GB vs. RTX 3090 for Local LLMs

**原文链接**: [https://www.hardware-corner.net/guides/dual-rtx-5060-ti-16gb-vs-rtx-3090-llm/](https://www.hardware-corner.net/guides/dual-rtx-5060-ti-16gb-vs-rtx-3090-llm/)

本文比较了假设的双 RTX 5060 Ti 16GB 显卡配置与二手 RTX 3090 在 2025 年 6 月进行本地大型语言模型 (LLM) 推理的性能。作者 Allan Witt 旨在为构建 LLM 设备的爱好者找到 VRAM、性能和价格的最佳平衡点。

双 RTX 5060 Ti 配置提供 32GB 的 VRAM，这允许更大的模型、更长的上下文长度或更高的精度量化。 然而，RTX 3090 具有明显更高的内存带宽（936 GB/s 对比 448 GB/s）。 基准测试使用 llama.cpp 服务器和 OpenWebUI，在 Ubuntu 22.04 上使用 4 位量化的 Qwen3 模型进行。

RTX 3090 显示出更快的令牌生成速度，尤其是在密集的 Qwen3-32B 模型上，平均比双 5060 Ti 配置快 70-85%。 然而，对于混合专家 (MoE) 模型 Qwen3 30B A3B，差异不太明显（3090 快约 29-30%），并且在极长的上下文长度（32,000 个令牌）下，双 5060 Ti 配置的性能与 RTX 3090 非常接近。 此外，双 5060 Ti 配置能够处理更大的上下文大小（约 44,000 个令牌），而 RTX 3090 只能处理约 32,000 个令牌。

作者的结论是，对于适合其 24GB VRAM 的模型，RTX 3090 在最大化令牌生成速度方面仍然具有优势，尤其是在密集模型方面。 然而，双 RTX 5060 Ti 16GB 配置在非常大的上下文窗口或以更高精度运行模型时变得引人注目。 32GB 的 VRAM 提供了显着的优势，其性能，尤其是在 MoE 模型和非常大的上下文下，是一个可行的选择。 最终的选择取决于用户是否需要持续处理极其长的提示。

---

## 90. 加倍投入开源

**原文标题**: Doubling Down on Open Source

**原文链接**: [https://langfuse.com/blog/2025-06-04-open-sourcing-langfuse-product](https://langfuse.com/blog/2025-06-04-open-sourcing-langfuse-product)

2025年6月4日，Langfuse宣布将其所有剩余产品功能以MIT许可证开源，有效加倍了其开源承诺。这包括之前商业化的功能，如托管LLM即服务评估、注释队列、提示实验和游乐场。

此举旨在培养更深层次的信任、协作、更快的迭代和更丰富的社区反馈。Langfuse认为，一个真正以开发者为中心的平台需要以开放为核心，并且这些功能现在已成为市场标准，应该免费提供。

Langfuse最初是一个开源项目，基于可访问数据、与各种模型的不可知集成以及自定义工作流程的灵活性等原则。通过此次公告，核心开源产品已得到扩展，而商业许可的代码现在仅专注于企业安全和平台团队功能，如SCIM、审计日志和数据保留策略。

Langfuse的商业重点现在集中在Langfuse Cloud和支持自托管的企业平台团队上。该公司拥有显著的开源采用率，每月SDK安装量超过700万，Docker拉取量为550万，每月活跃的自托管实例为8000个。Langfuse鼓励通过GitHub星标、讨论和路线图反馈来促进社区贡献。

---

## 91. 澳洲葵花鹦鹉学会使用饮水机

**原文标题**: Cockatoos have learned to operate drinking fountains in Australia

**原文链接**: [https://www.science.org/content/article/cockatoos-have-learned-operate-drinking-fountains-australia](https://www.science.org/content/article/cockatoos-have-learned-operate-drinking-fountains-australia)

澳大利亚的鹦鹉学会了操作公共饮水机来获取淡水，展现了卓越的问题解决能力和行为适应性。 这种行为最初在悉尼被观察到，并已在地理上传播，表明存在社会学习的过程。 鹦鹉以特定的顺序使用喙和爪来操纵喷泉的机械装置，通常包括按住杠杆或按钮以保持水流流动，同时它们饮用。

研究人员认为，最初的创新者很可能是成年鸟类，并且该技能随后已通过鹦鹉种群中的观察和模仿传递下来。 对这种行为的研究表明，不同的鹦鹉种群已经开发出略有不同的操作喷泉的技术，表明解决问题方面存在当地的文化差异。

这种学习行为的传播突显了鹦鹉的智慧和适应能力，使它们能够利用环境中的新资源。 虽然这种独创性令人着迷，但同时也引发了人们对与人类潜在冲突的担忧，因为鸟类对喷泉的操纵有时会导致损坏和浪费水。 了解这种行为如何在鹦鹉种群中传播和演变，对于管理城市环境中的人与野生动物互动至关重要。

---

## 92. 大型语言模型与 Elixir：福音抑或丧钟？

**原文标题**: LLMs and Elixir: Windfall or Deathblow?

**原文链接**: [https://www.zachdaniel.dev/p/llms-and-elixir-windfall-or-deathblow](https://www.zachdaniel.dev/p/llms-and-elixir-windfall-or-deathblow)

Zach Daniel的文章《LLM与Elixir：意外之喜还是致命一击？》探讨了大型语言模型（LLM）对Elixir编程语言及其社区的潜在影响。他认为，LLM不一定会构成生存威胁，但如果Elixir社区适应并投资于使Elixir工具对LLM友好，它们可以成为倍增器。

文章阐述了对LLM会偏爱Node.js等主流语言，从而导致开发者放弃Elixir的担忧。Daniel认为，这要么通过神奇的AI使所有语言趋于平等，要么更有可能的是，开发者会遇到Elixir旨在解决的相同扩展和并发性瓶颈，从而可能使他们回归Elixir。

他强调了确保LLM能够有效地与Elixir工具协同工作的重要性。作者强调，LLM擅长翻译和概括，但缺乏上下文知识，尤其是对于小众技术。

Daniel为Elixir社区提出了几项策略：

*   **研究与调查：** 在提问之前，通过提供相关的文档上下文来引导LLM。
*   **使用Tidewave：** 集成可让LLM实时访问正在运行的应用程序的状态和数据的工具。
*   **“帮我做一个像Y一样的X”：** 通过向LLM提供现有功能的示例来利用其概括能力。
*   **通过usage-rules.md文件众包上下文：** 创建专门为LLM上下文窗口设计的简洁文档。
*   **Evals：训练训练者：** 开发评估数据集，以训练LLM处理Elixir特定场景和最佳实践，从而帮助他们在适当的时候推荐Elixir。

最终，作者认为，通过积极塑造LLM与Elixir的交互方式，社区可以利用它们来降低学习曲线，提高可访问性，并推动Elixir的采用。

---

## 93. 氦气巨兽归来：LTA研究飞艇现身旧金山湾

**原文标题**: Helium Giants Return: LTA Research Airship over SF Bay

**原文链接**: [https://spectrum.ieee.org/lta-research-airship-pathfinder-1](https://spectrum.ieee.org/lta-research-airship-pathfinder-1)

2025年5月，LTA Research的巨型氦气飞艇“探路者1号”飞越旧金山湾。此事凸显了谢尔盖·布林的初创公司LTA Research正在探索其飞艇的性能和局限性。这篇由IEEE Spectrum特约编辑、调查性科学技术记者马克·哈里斯撰写的文章，聚焦于这次重要的试飞。此次飞行标志着LTA Research在飞艇开发方面持续进行的努力。

---

## 94. 极光，地球系统基础模型

**原文标题**: Aurora, a foundation model for the Earth system

**原文链接**: [https://www.nytimes.com/2025/05/21/climate/ai-weather-models-aurora-microsoft.html](https://www.nytimes.com/2025/05/21/climate/ai-weather-models-aurora-microsoft.html)

微软新型AI天气模型Aurora在天气预报领域引起轰动。《自然》杂志的一篇报道强调了Aurora的关键优势：与许多现有模型相比，它能以更精细的尺度提供准确的10天预报，并且已在欧洲一家主要气象中心使用。

Aurora最显著的特点是其多功能性。它被设计用于处理来自各种地球系统的数据，使其不仅可以被训练来预测热带气旋等天气事件，还可以预测空气污染、波浪高度和其他相关现象。这种适应性允许用户潜在地添加和预测其他地球系统，一家初创公司已经将其用于可再生能源市场预测。

领导Aurora开发的Paris Perdikaris教授强调了其作为将更多地球系统纳入预测流程蓝图的潜力。该模型的速度是另一个主要优势，它能在几秒钟内产生结果，比传统非人工智能模型（可能需要数小时）快得多。总而言之，Aurora的速度、准确性和适应性使其成为地球系统预测（不仅仅是天气）的强大工具。

---

## 95. 思考需要多少能量？

**原文标题**: How Much Energy Does It Take To Think?

**原文链接**: [https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/](https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/)

思考需要多少能量？

本文《思考需要多少能量？》探讨了人脑的能量消耗。尽管在专注任务后会感到精神疲惫，但研究表明，费力认知仅比大脑休息时多消耗约 5% 的能量。这表明大脑的大部分能量用于维护和后台处理，例如调节生理系统和响应环境变化。

大脑消耗人体 20% 的能量（婴儿为 50%），主要利用来自葡萄糖和氧气的 ATP 来驱动神经元之间的通信。科学家通过葡萄糖消耗（PET）和血流（fMRI）来测量大脑的能量使用。虽然活跃任务会增加神经元放电率，但大部分能量消耗用于支持大脑的基础代谢负荷，包括参与内部精神体验和维持体内平衡的默认模式网络。

神经科学家 Jordan Theriault 认为，大部分基础负荷用于预测，使大脑能够通过预测未来需求来有效地分配资源。文章认为，活跃思考期间能量消耗的有限增加反映了进化约束。我们的祖先在能量匮乏的环境中进化，导致了节能机制以防止过度劳累。大脑优先考虑最大化每次 ATP 消耗的信息传输，从而导致神经元放电率和突触传递成功率低于理论上的可能性。

最终，大脑的能量使用反映了复杂器官的优势与生物能量约束的限制之间的平衡，影响着从信息传输到精神疲劳的一切。

---

## 96. 考虑编织

**原文标题**: Consider Knitting

**原文链接**: [https://journal.stuffwithstuff.com/2025/05/30/consider-knitting/](https://journal.stuffwithstuff.com/2025/05/30/consider-knitting/)

在《考虑编织》一文中，一位软件工程师极力称赞编织的优点，尤其是对于那些终日盯着屏幕的人。他认为编织提供了急需的触觉刺激，满足了身体对物理感觉的深层渴望。他将编织比作一款具有平滑、用户可控技能曲线的开放世界游戏，允许编织者选择符合自己兴趣和技能水平的项目和技术，而无需强迫他们完成令人不快的任务。编织知识和技术的深度确保了持续且有益的学习体验。

作者在承认编织的结构化本质的同时，强调它不仅仅是一款用于优化的游戏。它在结构和非结构化的创造力之间提供了平衡，从而能够可靠地朝着一个有形的、美丽的物体取得进展。编织也具有高度的适应性，可以利用零碎的时间，并适应各种程度的脑力。它只需要最小的空间和设置。

最终，编织被视为对抗现代世界对效率和自动化痴迷的解药。作者强调了手工创造一件东西，一针一线，是一种有价值的关怀表达，也是一种有意义的消磨时间的方式，特别是当最终产品是送给所爱之人的礼物时。他以一个行动号召结束，鼓励读者探索可用于学习编织的丰富资源，并找到他在这项工艺中体验到的乐趣。

---

## 97. 程序员的提示工程手册

**原文标题**: Prompt engineering playbook for programmers

**原文链接**: [https://addyo.substack.com/p/the-prompt-engineering-playbook-for](https://addyo.substack.com/p/the-prompt-engineering-playbook-for)

无法访问文章链接。

---

## 98. 墨林观鸟

**原文标题**: Merlin Bird ID

**原文链接**: [https://merlin.allaboutbirds.org/](https://merlin.allaboutbirds.org/)

梅林鸟类识别是一款综合性的移动应用程序，旨在通过多种方法帮助用户识别鸟类。 它利用声音分析、图像识别和逐步向导来识别鸟类，满足新手和经验丰富的观鸟者的需求。

主要功能包括：

*   **声音识别：** 通过鸟鸣声和叫声实时识别鸟类，甚至可以离线使用。 目前覆盖范围包括美国、加拿大、欧洲、中美洲和南美洲的部分地区以及印度，并计划扩大覆盖范围。
*   **照片识别：** 通过照片识别鸟类，这些照片可以在应用程序内拍摄，也可以从设备的相机胶卷中导入，并且可以离线使用。
*   **鸟类识别向导：** 一个简单的三问题工具，引导用户识别鸟类，适用于全球。
*   **终生名录：** 一项用于保存已识别的鸟类并跟踪个人观鸟体验的功能。
*   **基于位置的列表：** 使用来自 eBird 的数据，能够创建在特定位置和一年中特定时间可能看到的鸟类的自定义列表。

梅林受益于由 eBird 广泛的鸟类观察数据驱动的庞大社区驱动的鸟类照片、歌曲、鸣叫声、专家提示和范围地图数据库。 该应用程序旨在成为任何有兴趣了解和识别周围鸟类的人的宝贵工具。

---

## 99. 华盛顿州维修权法案生效

**原文标题**: The Right to Repair Is Law in Washington State

**原文链接**: [https://www.eff.org/deeplinks/2025/06/right-repair-law-washington-state](https://www.eff.org/deeplinks/2025/06/right-repair-law-washington-state)

华盛顿州通过维修权法案，赋予公民获取维修个人电子产品、电器和轮椅所需的工具、零件和信息的权利。该法案体现了所有者应有权控制谁来维修、改装或修改其财产的原则。这项胜利是华盛顿公共利益研究小组、华盛顿残疾人权利组织以及“此时此地”项目等团体多年倡导的结果，并得到了环境和消费者权益倡导者以及谷歌和微软等公司的支持。

文章还强调了维修权重要性日益受到全美认可。美国国防部长已指示陆军在采购合同中寻求维修权条款，并将此与林肯总统历史上对军事装备标准化工具的关注相提并论。此举旨在解决军队依赖外部供应商进行维护的问题，这使纳税人损失数十亿美元。

维修权运动旨在消除维修障碍，使从农民到房主再到士兵的各类人群受益。随着所有 50 个州都在考虑维修权立法，华盛顿州是第八个颁布此类法律的州，这标志着该运动在全国范围内势头渐增。

---

## 100. 一个时代的终结：陆地卫星7号退役，结束25年地球观测任务

**原文标题**: End of an Era: Landsat 7 Decommissioned After 25 Years of Earth Observation

**原文链接**: [https://www.usgs.gov/news/national-news-release/end-era-landsat-7-decommissioned-after-25-years-earth-observation](https://www.usgs.gov/news/national-news-release/end-era-landsat-7-decommissioned-after-25-years-earth-observation)

经过25年的地球观测，美国地质调查局（USGS）已正式退役了陆地卫星7号。 陆地卫星7号于1999年发射，是USGS和NASA之间的联合任务，在陆地卫星计划中发挥了关键作用，提供了超过五十年的地球表面图像。

陆地卫星7号的数据在各种应用中发挥了重要作用，帮助世界各地的农民、土地管理者、城市规划者、科学家和社区管理土地、水和自然资源。 它有助于监测干旱、指导灾后恢复并了解环境变化。

该卫星实现了多个里程碑，包括成为第一颗将数据下行链路到苏福尔斯USGS地面站的陆地卫星，也是第一颗在发射后完全由USGS运营的陆地卫星。 它的增强型专题制图仪Plus传感器捕捉了9/11事件、卡特里娜飓风和深水地平线漏油事件等关键事件的后果。 它还为南极洲陆地卫星图像镶嵌图和“地球即艺术”系列等重要项目做出了贡献。

虽然陆地卫星7号的任务于2024年结束，但陆地卫星8号和陆地卫星9号继续每八天提供地球快照。 计划于2030年代初发射的陆地卫星Next将进一步增强覆盖范围和细节。 为确保负责任的空间实践，陆地卫星7号的退役包括降低其轨道并耗尽能源。 该卫星将在轨道上漂移约55年，然后重新进入地球大气层。

---

