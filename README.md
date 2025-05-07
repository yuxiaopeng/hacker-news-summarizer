# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-07.md)

*最后自动更新时间: 2025-05-07 17:49:33*
## 1. 等待Postgres 18：使用异步I/O加速磁盘读取

**原文标题**: Waiting for Postgres 18: Accelerating Disk Reads with Asynchronous I/O

**原文链接**: [https://pganalyze.com/blog/postgres-18-async-io](https://pganalyze.com/blog/postgres-18-async-io)

本文预览Postgres 18中即将推出的异步I/O (AIO) 功能，这标志着一个重要的架构转变，有望带来显著的性能提升，尤其是在云环境中。 历史上，Postgres 使用同步 I/O，数据库会暂停并等待每个读取请求完成。 AIO 消除了这个瓶颈，允许 Postgres 同时发出多个读取请求。

Postgres 17 引入了读取流，为 AIO 铺平了道路。 Postgres 18 引入了 `io_method` 配置参数，具有三个设置：`sync`（传统同步 I/O）、`worker`（专用 I/O 工作进程）和 `io_uring`（一种高性能的 Linux 特有接口）。 AWS 上的基准测试表明，在冷缓存场景中，`worker` 和 `io_uring` 可以提供比 `sync` 高 2-3 倍的读取性能提升。 虽然 worker 在热缓存场景中显示出一些优势，但 io_uring 在冷缓存中始终表现更好。 `effective_io_concurrency` 设置现在直接控制异步预读请求的数量。

使用 AIO 监控 I/O 更改。 本文介绍了用于调试 I/O 请求的 `pg_aios` 视图。 由于异步执行，标准的 `EXPLAIN ANALYZE` 输出可能无法准确反映 I/O 时间。

---

## 2. Show HN: 优化电纸书阅读的漫画，搭配Kindle Comic Converter (+Kobo/ReMarkable)

**原文标题**: Show HN: eInk optimized manga with Kindle Comic Converter (+Kobo/ReMarkable)

**原文链接**: [https://github.com/ciromattia/kcc](https://github.com/ciromattia/kcc)

Kindle漫画转换器 (KCC) 是一款用于优化漫画和漫画书在Kindle、Kobo和Remarkable等电子墨水设备上的显示的工具。它将各种输入格式（文件夹、CBZ、CBR、PDF）转换为专为电子墨水屏优化的MOBI/AZW3、EPUB、KEPUB或CBZ格式。KCC提供图像处理选项，以增强电子墨水屏幕上的视觉质量，并通过缩小到设备特定的分辨率来减小文件大小。

该工具支持漫画式阅读（从右到左），并提供诸如分格浏览、伽马校正、裁剪和双页分割等功能。用户可以自定义输出设置，包括文件格式、标题和作者。其中包含针对众多Kindle和Kobo型号的设备配置文件，并可以选择自定义分辨率。

KCC需要可选的先决条件，例如KindleGen（通过Kindle Previewer）和7-Zip才能实现某些功能。该项目是开源的，欢迎通过拉取请求进行贡献，并接受捐款以支持持续开发。该帖子还提供了针对不同操作系统（Windows、macOS）的安装说明，以及指向YouTube教程和项目GitHub存储库的链接，用于下载、问题报告和详细文档。

---

## 3. 变老并非你想的那样

**原文标题**: Getting Older Isn't What You Think

**原文链接**: [https://www.katycowan.co.uk/blog/getting-old](https://www.katycowan.co.uk/blog/getting-old)

凯蒂·考恩的《变老并非你想象的那样》是一篇关于衰老的反思文章，着重探讨了夹在X世代和千禧一代之间的“Xennials”世代的体验。作者挑战了“变老意味着活力下降”的刻板印象，认为这反而是一个自我发现和喜好不断演变的过程。

她幽默地叙述了自己从享受夜生活到更喜欢安静的夜晚的转变，并质疑这种改变是源于年龄还是源于对真实自我的认知。考恩批判了青年文化的表演性，尤其是在社交媒体上，并表达了对随着年龄增长而来的简单和真实的满足感。

文章还赞扬了Xennials世代独特的地位，他们既经历了模拟世界也经历了数字世界。他们拥有“双重智慧”，在日益数字化的时代理解隐私和现实生活连接的价值。考恩感叹社交媒体的负面影响，并欣赏人们回归线下活动的趋势。

最终，考恩倡导拥抱好奇心，挑战自己的观点，并倾听他人，无论年龄大小。她总结说，变老不是一种负面体验，而是一个自我接纳、摆脱伪装以及更深入地了解自己的时代。最重要的是要保持好奇心。

---

## 4. 说谎：1996年鲍威与在线音乐发行

**原文标题**: Telling Lies: Bowie and Online Music Distribution in 1996

**原文链接**: [https://cybercultural.com/p/online-music-distribution-1996/](https://cybercultural.com/p/online-music-distribution-1996/)

1996年9月，大卫·鲍威在他的N2K制作的网站上免费下载了他的单曲“Telling Lies”，标志着在线音乐发行的早期实验。当时在线音乐零售（通过购买CD）已经存在，但由于带宽低，数字发行面临挑战。

鲍威与N2K合作，N2K的首席执行官拉里·罗森设想了一个艺术家直接在线发行音乐，绕过唱片公司的未来。虽然像Music Boulevard和CDnow这样的网站在线销售实体CD，但由于网速慢，下载文件并不实际。

“Telling Lies”提供了多种格式，包括低质量的流媒体选项和通过Liquid Audio提供的更大的CD质量文件，需要很长时间的下载（使用28.8 Kbps调制解调器需要45分钟）和特定的软件。尽管存在技术障碍（服务器错误、下载速度慢），但此次发布被认为是营销上的成功，据报道，前两天下载量达15万次，到周末达到45万次。

鲍威将这次发布视为一次实验，承认这不是他的主意，而是维珍唱片公司的。他承认流媒体质量差和下载速度慢，但预计会有所改善。然而，罗森认为这是一个未来即将到来的迹象，预示着一个直接面向消费者的数字音乐发行的未来，尽管电子商务方面还需要一年才能实现。这篇文章强调了早期数字音乐发行的开创性但具有挑战性的性质，以及像N2K这样的公司彻底改变音乐产业的雄心壮志。

---

## 5. 血流成河

**原文标题**: So Much Blood

**原文链接**: [https://dynomight.net/blood/](https://dynomight.net/blood/)

本文题为《血流成河》，深入探讨了美国的血液制品出口情况，起因是作者惊讶于血液制品占美国出口额的 2% 的说法。作者通过仔细剖析官方贸易数据，得出了一个更准确的数字。

他们发现《经济学人》广泛引用的 1.8% 的数据存在缺陷。通过查阅美国贸易委员会的详细数据，特别是血液相关产品的 HTS 编码，作者将出口产品分为“含血”、“不含血”和“可能含血”三类。“含血”包括人血浆、血清和其他血液成分，约占美国商品出口的 0.53%。“不含血”包括兽用疫苗、细胞培养物和发酵剂，占 0.14%。

“可能含血”类别最为复杂，包括免疫学产品、人用疫苗和细胞治疗产品。由于这些项目可能涉及也可能不涉及人血，作者咨询了行业专家，以估计其中确实使用人血的比例。他们估计大约有 0.16% 的商品出口使用了血液。

作者得出结论，美国血液制品出口额占商品出口总额的更准确估计约为 0.69%。他们承认其方法的局限性，特别是对专家估计的依赖，并希望发表他们的研究结果能够鼓励对数据进行进一步的审查和完善。

---

## 6. Unity开源的双重标准：VLC的禁令

**原文标题**: Unity’s Open-Source Double Standard: the ban of VLC

**原文链接**: [https://mfkl.github.io/2024/01/10/unity-double-oss-standards.html](https://mfkl.github.io/2024/01/10/unity-double-oss-standards.html)

本文详细介绍了VideoLAN在使用Unity应用商店的经验，以及随后推出自家Videolabs商店的经过。VideoLAN之前曾在Unity商店提供VLC for Unity集成资源，使开发者能够将VLC多媒体引擎整合到Unity项目中。然而，由于VLC插件中包含LGPL依赖项，Unity封禁了VideoLAN的发布者帐户。

VideoLAN认为这是一种双重标准，并指出Unity商店中许多其他资源也包含LGPL依赖项，如FFmpeg，并且Unity本身也在其编辑器和运行时中依赖LGPL库。被封禁后，并且在对Unity资源持续需求的情况下，VideoLAN在其网站上推出了Videolabs商店。这使得现有和新客户能够购买VLC Unity插件二进制文件，同时仍然允许用户自行构建VLC for Unity，因为它是开源的。

Videolabs商店还提供灵活的LibVLC和FFmpeg多媒体咨询服务，为商业用户提供专家支持、定制构建和SDK集成。除了VLC Unity插件外，该商店还提供LibVLCSharp商业许可、LibVLC电子书以及即将推出的产品，如Kyber流媒体SDK。

---

## 7. Motion (YC W20) 正在招聘高级工程师

**原文标题**: Motion (YC W20) Is Hiring a Senior Engineers

**原文链接**: [https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn](https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn)

Motion (YC W20) 正在招聘各级别软件工程师，包括高级工程师。招聘信息表明，需要使用 JavaScript 才能运行该应用程序。内容未提供有关职位、职责、资格或福利等更多具体信息。

---

## 8. CLion 现在可供非商业用途免费使用

**原文标题**: CLion Is Now Free for Non-Commercial Use

**原文链接**: [https://blog.jetbrains.com/clion/2025/05/clion-is-now-free-for-non-commercial-use/](https://blog.jetbrains.com/clion/2025/05/clion-is-now-free-for-non-commercial-use/)

JetBrains宣布CLion对非商业用途免费，此举使其与RustRover、Rider和WebStorm保持一致，这些产品已经提供免费的非商业许可证。

此免费许可证适用于学生、开源贡献者、内容创作者、业余爱好者以及任何将CLion用于学习或个人项目的人，只要他们没有从中获得商业利益。对于商业用途，现有的许可模式保持不变。

目标是提高CLion的可用性，降低开发人员的入门门槛，鼓励学习和实验。免费许可证提供功能齐全的IDE体验，与付费版本相同，但“Code With Me”功能除外，该功能仅限于社区版。

非商业用途定义为不带来直接或间接商业优势或金钱补偿的开发，明确排除学习、无商业收益的开源贡献、内容创作和业余爱好开发等活动。

免费许可证用户同意收集匿名使用统计数据，以帮助JetBrains改进产品，类似于他们的Early Access Program (EAP)。此数据侧重于IDE功能的使用，不包含个人信息。

非商业许可证的有效期为一年，如果在之前的六个月内至少使用过一次，则会自动续订。现有付费用户应查看退款政策，以确定他们是否符合仅从事非商业开发情况下的退款资格。文章还提供了如何在CLion IDE中切换到非商业许可证的说明。

---

## 9. 我让摩托车骑行更安全一点的探索

**原文标题**: My quest to make motorcycle riding that tad bit safer

**原文链接**: [https://gill.net.in/posts/my-quest-to-make-motorcycle-riding-safer/](https://gill.net.in/posts/my-quest-to-make-motorcycle-riding-safer/)

作者讲述了他们创造BrakeBright的历程，这是一个旨在提高安全性的摩托车智能刹车灯系统。受到CBT教练关于在发动机制动期间使用刹车来提醒驾驶员的建议启发，身为工程师的作者认为，依赖习惯的现有安全措施是不够的。BrakeBright在发动机制动期间会自动激活刹车灯，并在急刹车期间使其闪烁频率与制动强度成正比。

作者详细描述了现有售后解决方案的缺点，强调了对更精密和可靠系统的需求。他们描述了开发过程，从面包板开始，最终形成了一个可用于生产的设备。关键挑战包括传感器精度、抗振性和同步问题，所有这些都通过严格的测试和改进得到解决。

一位朋友提供了一辆摩托车用于早期测试，随后作者在获得驾照后使用了自己的摩托车。测试包括在苏格兰具有挑战性的NC500路线。作者还通过开发用于固件更新和自定义的软件实用程序来增强用户自主权。

第一批产品的到来是一个无比自豪和满足的时刻。作者强调这仅仅是一个开始，其动力来自于改善所有摩托车骑手的安全。作者邀请大家提出反馈意见，提供BrakeBright购买，并提供联系方式。

---

## 10. Zed：高性能AI代码编辑器

**原文标题**: Zed: High-performance AI Code Editor

**原文链接**: [https://zed.dev/blog/fastest-ai-code-editor](https://zed.dev/blog/fastest-ai-code-editor)

Zed，一款用Rust构建并以GPL协议开源的高性能代码编辑器，引入了通过“Agent Panel”访问的全新AI功能。该面板允许用户与AI代理交互，执行代码修改、回答关于代码库的问题以及生成新代码等任务。

主要功能包括：

*   **代理编辑：** AI代理可以被指示进行更改、编写代码并追踪代码库中的特定位置。
*   **隐私与安全：** 默认情况下，用户与代理的对话是私密的，并且在未经明确同意的情况下，Zed不会使用这些数据进行训练。在执行潜在的不可逆操作（如运行终端命令）之前，会请求确认。
*   **定制：** 用户可以选择不同的语言模型（包括通过Ollama使用的自定义模型），并通过配置文件配置代理对各种工具的访问权限，例如语言服务器、代码检查器和终端命令。
*   **模型上下文协议：** 允许使用针对特定用例（例如数据库交互或拉取请求创建）量身定制的工具来扩展代理的功能。
*   **定价：** Zed的核心编辑器功能仍然免费。AI功能通过付费计划提供，具有每月提示限制（免费计划50个提示，$20 Pro计划500个提示），或者可以使用您自己的API密钥，无需Zed额外收费。Ollama也可用于在本地运行代理。

文章强调了Zed致力于为开发者提供可访问的AI工具，并旨在通过增强免费基础体验的可选付费功能来改善编码体验。调试器版本计划在本月晚些时候发布，未来还将推出改进的AI协作和Windows支持。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 2 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 3 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 4 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 5 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 6 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 7 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 8 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 9 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 10 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 11 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 12 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 13 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 14 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 15 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 16 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 17 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 18 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 19 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 20 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 21 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 22 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 23 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 24 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 25 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 26 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 27 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 28 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 29 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 30 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 31 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 32 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 33 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 34 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 35 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 36 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 37 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 38 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 39 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 40 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 41 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 42 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 43 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 44 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 45 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 46 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 47 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 48 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 49 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
