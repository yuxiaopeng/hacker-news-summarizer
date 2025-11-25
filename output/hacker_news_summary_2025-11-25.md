# Hacker News 热门文章摘要 (2025-11-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Apt Rust 需求引发质疑

**原文标题**: Apt Rust requirement raises questions

**原文链接**: [https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/](https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/)

LWN.net文章探讨Debian的APT可能于2026年要求使用Rust引发的争议。APT维护者Julian Andres Klode宣布了这项计划，理由是使用Rust重写APT的部分（特别是.deb、.ar、.tar解析和HTTP签名验证）可以带来内存安全和改进的单元测试。

此决定引发了争论，因为它会影响缺乏Rust工具链的Debian移植版本，可能迫使它们获取工具链、放弃移植或继续使用旧版APT。虽然一些开发者欢迎转向Rust等现代技术，但另一些开发者批评Klode的沟通方式以及缺乏事先讨论。

提出的主要问题包括：志愿者维护者支持Rust的负担、Rust软件包的静态链接特性对Debian基础设施的影响，导致潜在的安全支持限制，以及Debian在管理Rust依赖项和跟踪CVE方面面临的现有挑战。

David Kalnischkies建议完全从APT中删除有问题的代码，因为它主要由Canonical的Launchpad软件使用。有些人担心此更改违背了Debian支持多样化硬件和民主治理的价值观，因为这是一个由单个开发者推动的，缺乏足够的社区投入的决定。

讨论还涉及潜在的解决方案，例如Fork APT、创建Rust到C的转换器或为现有的Rust编译器做出贡献。 争论还扩展到静态库与共享库的更大问题，一些人主张使用依赖项更新重建软件包，而另一些人则更喜欢使用共享库以便于维护。

---

## 2. FLUX.2：前沿视觉智能

**原文标题**: FLUX.2: Frontier Visual Intelligence

**原文链接**: [https://bfl.ai/blog/flux-2](https://bfl.ai/blog/flux-2)

FLUX.2：Black Forest Labs最新视觉智能模型，专为真实创意工作流程设计，提供高质量图像生成，具备跨多重参考一致性、结构化提示遵循和高级文本处理能力。它能在保留细节的同时编辑高达 4 百万像素的图像。

Black Forest Labs强调开放式创新，将FLUX.1（流行的开放图像模型）等开放模型与FLUX.1 Kontext等专业级模型相结合。这种开放核心方法旨在推动实验、审查并降低成本。

FLUX.2相比FLUX.1有显著改进，包括多重参考支持（最多10张图像）、图像细节和照片级真实感提升、可靠的文本渲染、增强的提示遵循、改进的世界知识和更高的分辨率输出。

FLUX.2系列包括FLUX.2 [pro]（最先进的质量）、FLUX.2 [flex]（完全参数控制）、FLUX.2 [dev]（32B开放权重模型）和FLUX.2 [klein]（即将推出的开源模型）。一种新的变分自编码器(VAE)为所有FLUX.2模型提供支持，优化可学习性、质量和压缩。

FLUX.2采用潜在流匹配架构，将视觉-语言模型与修正流Transformer相结合。这实现了多重参考支持、更高分辨率、更好的提示遵循和改进的排版。

Black Forest Labs致力于这些模型的负责任开发，并寻求构建视觉智能的基础设施，目标是实现统一感知、生成、记忆和推理的多模态模型。

---

## 3. 模拟信号滤波入门

**原文标题**: The 101 of Analog Signal Filtering

**原文链接**: [https://lcamtuf.substack.com/p/the-101-of-analog-signal-filtering](https://lcamtuf.substack.com/p/the-101-of-analog-signal-filtering)

无法访问文章链接。

---

## 4. Meta 分割一切模型 3

**原文标题**: Meta Segment Anything Model 3

**原文链接**: [https://ai.meta.com/blog/segment-anything-model-3/?_fb_noscript=1](https://ai.meta.com/blog/segment-anything-model-3/?_fb_noscript=1)

无法访问文章链接。

---

## 5. 人类大脑预先配置了理解世界的指令。

**原文标题**: Human brains are preconfigured with instructions for understanding the world

**原文链接**: [https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/](https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/)

加州大学圣克鲁兹分校的研究人员发现，人脑在感官体验发生之前就已具备预先配置的活动模式，表明存在一种内在的“操作系统”指导着与世界的互动。他们利用脑类器官（由干细胞生长而成的三维人脑组织模型）来研究最早的电活动时刻。这项发表在《自然·神经科学》上的研究表明，这些早期的脑电活动是在没有外部刺激的情况下以结构化模式发生的。

这项研究使科学家们能够在伦理的框架下研究人脑发育，而这通常是在子宫内受到保护的。通过观察类器官，该团队发现细胞自发地发出类似于大脑“默认模式”的电信号，这是一种神经元放电的基本底层结构。这些模式出现在发育的最初几个月，有可能被优化用于特定的感觉。

这些发现对于理解神经发育障碍以及毒素对发育中的大脑的影响具有重大意义。识别和研究类器官中的这些早期模式可以为开发脑部疾病的临床前疗法铺平道路，包括药物疗法和基因编辑工具。这项研究突显了类器官在彻底改变我们对人脑发育及其脆弱性的理解方面的潜力。

---

## 6. Pebble手表软件现在开源

**原文标题**: Pebble Watch software is now open source

**原文链接**: [https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source](https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source)

本文宣布Pebble手表软件现已100%开源，旨在解决对该平台长期可持续性的担忧。在Core Devices旗下重启Pebble的作者强调了硬件和软件长期维护的重要性。

在硬件方面，Core Devices自筹资金，致力于制造可修复的手表，如Pebble Time 2，其电池可更换，且Pebble 2 Duo的原理图已公开。

关键进展是Pebble软件的完全开源，包括PebbleOS和移动配套应用程序。这确保了即使Core Devices不复存在，社区也能维护和改进该软件。文章详细介绍了使用Kotlin Multiplatform构建的新移动应用程序现在是开源的。

Pebble Appstore也在去中心化。该移动应用程序将支持多个应用商店“源”，允许任何人创建和托管Pebble应用程序库。Core Devices已推出自己的源，将应用程序备份到Archive.org。开发者仍然可以将其应用程序货币化。

最后，本文提供了有关Pebble Time 2的最新信息，目标是在一月份开始发货，大部分预计在三月/四月送达，并承认可能因中国新年而延迟。还提供了一个预生产PT2手表的视频演示。预购客户很快就可以选择自己喜欢的颜色。

---

## 7. 古惑狼制作秘辛 (2011)

**原文标题**: Making Crash Bandicoot (2011)

**原文链接**: [https://all-things-andy-gavin.com/video-games/making-crash/](https://all-things-andy-gavin.com/video-games/making-crash/)

这篇2011年2月的文章节选标志着“古惑狼”制作系列文章的开始。作者，顽皮狗公司创始人之一，回顾了公司1994年夏天的状况。当时，顽皮狗还是一个由作者和他搭档杰森·鲁宾组成的两人小团队。在过去的八年里，他们高效合作，成功发行了六款游戏。然而，文章暗示，1994年他们决定扩大公司规模，预示着即将开始开发后来的“古惑狼”。“阅读更多”链接表明后续文章将更深入地探讨公司扩张的过程以及这款标志性平台游戏开发的早期阶段。

---

## 8. 数万亿美元投入，大型软件项目依然失败

**原文标题**: Trillions Spent and Big Software Projects Are Still Failing

**原文链接**: [https://spectrum.ieee.org/it-management-software-failures](https://spectrum.ieee.org/it-management-software-failures)

万亿投入，大型软件项目仍频频失败

---

## 9. 研究发现，Ozempic无法延缓阿尔茨海默症。

**原文标题**: Ozempic does not slow Alzheimer's, study finds

**原文链接**: [https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds](https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds)

诺和诺德研究显示Ozempic不延缓阿尔茨海默病进展

---

## 10. 最稳定的树莓派？更好的NTP与散热管理

**原文标题**: Most Stable Raspberry Pi? Better NTP with Thermal Management

**原文链接**: [https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/](https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/)

本文详细介绍了如何通过解决热致时序抖动来提高基于树莓派的NTP服务器的稳定性，以实现精确计时。作者注意到，尽管有稳定的GPS PPS参考，NTP服务器中的频率漂移与CPU温度变化相关。核心问题：CPU频率调整和温度相关的晶体振荡器频率。

解决方案包括两个主要组成部分：CPU核心绑定和热稳定。CPU核心绑定将CPU 0专用于时间关键型任务（chronyd和PPS中断），通过启动优化脚本将CPU调控器设置为“性能”模式，将PPS中断和chronyd绑定到CPU 0，将chronyd设置为实时优先级，并提高内核softirq处理程序的优先级。

热稳定使用PID控制的“时间燃烧器”来维持恒定的CPU温度。这个Python脚本读取CPU温度，计算维持目标温度（54°C）所需的CPU负载，并使用worker进程将负载分配到CPU 1-3上，这些进程在忙循环哈希和睡眠之间交替。通过维持稳定的CPU温度，物理上接近的晶体振荡器的热环境得到稳定，从而实现一致的时钟频率并改善计时。

结果表明，频率稳定性得到了显著改善，平均RMS偏移降低了近50%，中位数RMS偏移降低了52.7%。本文提供了复制优化的详细设置说明，包括启动优化和热稳定的脚本，以及systemd服务配置。作者强调，对于频率稳定性而言，保持硅温度一致比环境空气温度变化更重要。

---

## 11. Orion 1.0 – 浏览无限

**原文标题**: Orion 1.0 – Browse Beyond

**原文链接**: [https://blog.kagi.com/orion](https://blog.kagi.com/orion)

Orion 1.0 正式发布 macOS 版，告别测试阶段。这款由 Kagi 出品的注重隐私的浏览器，与 iOS 和 iPadOS 应用一起，扩展了“Kagi 生态”，以及他们的搜索、助手、翻译和新闻产品。Orion 旨在通过零遥测、优先考虑用户隐私和控制，来提供广告驱动型浏览器的替代方案。

Orion 基于 Safari 背后的开源引擎 WebKit 构建，区别于 Chromium 的单一文化。它强调速度，这得益于精简的代码库和优化的性能，以及内置的隐私保护，如内容拦截。在拥抱人工智能潜力的同时，Orion 避免将不安全的、始终在线的 AI 代理直接集成到浏览器核心中，而是倾向于浏览器和外部 AI 工具之间的明确分离。

独特的功能包括专注模式、链接预览、迷你工具栏、溢出菜单、页面调整和作为应用程序的配置文件。

Orion 由一个六人小团队开发，可以免费使用。其可持续性通过用户的捐赠罐、支持者订阅（每月 5 美元或每年 50 美元）和终身访问权（150 美元）来实现。支持者可以解锁浮动窗口、自定义和抢先体验新功能等福利。

Orion 旨在跨平台可用，目前有 macOS、iOS/iPadOS、Linux (Alpha) 和 Windows（开发中）版本。路线图包括更深层次的定制、性能改进、新的 Orion+ 功能以及与 Kagi 的 AI 工具更紧密的集成。

---

## 12. 未供电的固态硬盘会缓慢丢失数据

**原文标题**: Unpowered SSDs slowly lose data

**原文链接**: [https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/](https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/)

本文探讨了断电状态下固态硬盘长期存储数据丢失的问题，强调固态硬盘并非长期冷存储的理想选择。与磁性存储数据的硬盘不同，固态硬盘依赖于NAND闪存单元中的电荷，这些电荷会随着时间推移而消散，尤其是在断电情况下。

数据保持期因使用的NAND闪存类型而异：QLC NAND可安全存储数据约一年，TLC NAND可存储长达三年，而MLC/SLC NAND可存储五年到十年。由于大多数消费级固态硬盘使用TLC或QLC NAND，因此断电一年以上可能会导致数据损坏或丢失。温度和NAND闪存质量等因素会加速电压损耗。

然而，作者强调，这主要针对涉及档案存储的企业、发烧友和个体经营者的用例。对于典型的PC使用，由于固态硬盘经常通电，因此风险很小。文章还提到，固态硬盘的写入周期有限，最终会使其达到生命周期终点。

关键要点是数据备份的重要性。建议采用3-2-1备份规则（3份数据保存在2种不同的介质上，其中1份异地备份）以防止因任何类型的存储故障（包括固态硬盘因长期断电存储而丢失数据）造成的数据丢失。虽然固态硬盘适用于主存储，但在没有备份的情况下，依赖它们进行断电长期存档是很危险的。

---

## 13. 大脑有五个“时期”，成人模式要到30岁出头才开始。

**原文标题**: Brain has five 'eras' with adult mode not starting until early 30s

**原文链接**: [https://www.theguardian.com/science/2025/nov/25/brain-human-cognitive-development-life-stages-cambridge-study](https://www.theguardian.com/science/2025/nov/25/brain-human-cognitive-development-life-stages-cambridge-study)

这项研究确定了人类大脑发育的五个不同“阶段”，并以9岁、32岁、66岁和83岁四个关键“转折点”为标志。研究人员分析了近4000名个体的大脑扫描图像，绘制了从婴儿期到老年期的神经连接及其演变过程。

第一个阶段，从出生到9岁，其特征是“网络整合”，突触连接被修剪，大脑布线效率降低，灰质和白质体积迅速增加。青春期，即持续到大约32岁的第二个阶段，见证了白质的持续增长和大脑连接效率的提高，这与认知功能的改善有关。

最重要的转变发生在32岁左右，启动了“成人模式”，这是一个大脑相对稳定的阶段。大脑区域变得更加分隔，与观察到的智力和人格的平稳期相一致。虽然诸如为人父母等生活事件可能有所贡献，但该研究并未对此进行直接调查。

最后两个转折点，分别在66岁和83岁，标志着“早期衰老”和“晚期衰老”阶段的开始。这些阶段的特点是大脑连接性降低，这可能与衰老和白质退化有关。该研究结果为大脑发育的脆弱性以及精神健康障碍的潜在风险因素提供了见解，尤其是在青春期。

---

## 14. 利用环境指纹实现无需GPS的附近设备发现

**原文标题**: Nearby peer discovery without GPS using environmental fingerprints

**原文链接**: [https://www.svendewaerhert.com/blog/nearby-peer-discovery/](https://www.svendewaerhert.com/blog/nearby-peer-discovery/)

本文介绍 Shimmer，一个利用环境指纹在没有 GPS 的情况下发现附近对等设备的系统。它利用了这样一个理念：同一区域内的设备很可能观察到同一组环境信号（例如，WiFi 网络、蓝牙信标）。

Shimmer 通过使用 MinHash 和局部敏感哈希 (LSH) 创建这些环境观察的密码学指纹来工作。 MinHash 为每个设备观察到的环境生成紧凑的签名，而 LSH 创建“碰撞桶”，其中相似的签名很可能散列到相同的值 (publicTags)。然后，设备使用 preImages 作为密钥加密其对等信息，并使用 publicTags 作为索引将其发布到会合服务器。观察到类似环境的其他对等设备可以生成匹配的 publicTags，从而允许他们发现和解密对等信息。

作者概述了潜在的用例，例如基于位置的多人游戏和会议网络。 Shimmer 提供了诸如私有集合交集 (PSI) 以获得精确的相似性评分、对多种数据模式（WiFi、蓝牙、共同兴趣）的支持、基于 epoch 的草图过期以及各种会合选项等功能。

本文还讨论了安全方面的考虑，包括欺骗环境观察的潜在可能性以及会合服务器了解 IP 邻近性的风险。 提出了潜在的缓解措施，例如使用 Tor、Oblivious HTTP (OHTTP) 或 DHT 进行会合。 作者强调，Shimmer 的适用性取决于具体的威胁模型。 他将 Shimmer 构建为一个有趣的问题，并考虑了服务器邻近性和 Android 位置权限要求等权衡因素。

---

## 15. 西兰花人，重制版

**原文标题**: Broccoli Man, Remastered

**原文链接**: [https://mbleigh.dev/posts/broccoli-man-remastered/](https://mbleigh.dev/posts/broccoli-man-remastered/)

This article details the author's experience recreating Google's "Broccoli Man" video using AI tools. Fifteen years after the original, the author spent a Saturday using Veo 3.1 and Nano Banana to create a remastered 4-minute short film.

The process involved:
*   **Preproduction:** Script preparation using AI Studio to break down the original video into scenes and brainstorming prompts. Character "ingredients" (Broccoli Man and Red Panda) were converted to photorealistic versions and backgrounds removed using Magic Markup (Nano Banana).
*   **Production:** Video generation using Vertex AI Studio and Veo 3.1 with "Ingredients to Scene." The process was iterative, with the author generating multiple samples per scene and tweaking prompts. Character consistency was surprisingly good, and audio sync was often achievable. Challenges included the rigid 8-second clip duration, recreating static conversation scenes, camera control, and achieving desired character emotes.
*   **Postproduction:** Using CapCut for editing, including trimming scenes, interleaving takes, manipulating audio, and dialogue volume normalization. The author emphasizes the necessity of non-linear video editing for this type of project.

The author concludes by stating that the AI tools allowed them to create something they wouldn't have otherwise, despite limitations and quirks. They believe that intent matters, contrasting the potential for creative expression with the "slop-farm" content.


---

## 16. Claude高级工具使用

**原文标题**: Claude Advanced Tool Use

**原文链接**: [https://www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)

本文介绍三个旨在增强使用 Claude 模型的人工智能代理能力的全新功能，特别是专注于工具使用和集成。

**1. 工具搜索工具：** 解决了大型工具库带来的过度 Token 消耗问题。工具搜索工具并非预先加载所有工具定义，而是使 Claude 能够按需动态发现工具。这显著减少了上下文消耗（高达 85% 的 Token 减少），并提高了工具选择的准确性，尤其是在具有大量工具的系统中。工具标记为 `defer_loading: true` 以防止初始加载，并且仅在需要时才被发现。

**2. 程序化工具调用：** 解决了中间结果和推理开销造成的上下文污染问题。 Claude 现在可以通过代码（Python）来编排工具，从而实现复杂的逻辑、数据处理和高效的控制流。 Claude 无需为每个工具进行单独的 API 调用并将结果返回到 Claude 的上下文中，而是编写代码来调用多个工具，处理它们的输出，并将最终的、相关的信息返回到其上下文中。这减少了 Token 消耗、延迟并提高了准确性。 通过添加 `code_execution` 并指定 `allowed_callers` 来启用工具的程序化调用。

**3. 工具使用示例：** 在本摘要中未深入讨论，但其目的是添加关于如何正确使用工具的示例，以便为 Claude 提供上下文。 JSON Schema 无法表达使用模式，此功能旨在添加必要的上下文。

这些功能旨在使 Claude 更有效地使用广泛的工具库和复杂的工作流程，从而为构建更强大和高效的人工智能代理开辟可能性。

---

## 17. 使用针床阵列制作立体针织造型

**原文标题**: Using an Array of Needles to Create Solid Knitted Shapes

**原文链接**: [https://dl.acm.org/doi/10.1145/3746059.3747759](https://dl.acm.org/doi/10.1145/3746059.3747759)

无法访问文章链接。

---

## 18. 详细解读Techmeme二十年如一日的坚持

**原文标题**: Explaining, at some length, Techmeme's 20 years of consistency

**原文链接**: [https://news.techmeme.com/250912/20-years](https://news.techmeme.com/250912/20-years)

在成立20周年之际，Techmeme回顾了其作为重要科技新闻聚合器的始终如一的角色。尽管技术、网络和新闻消费发生了深刻的变化，Techmeme仍然保持其核心功能：对来自新闻媒体、个人网站和社交媒体等各种来源的链接进行排名和组织，为科技行业领导者提供共享的背景信息。

然而，保持这种一致性变得越来越具有挑战性。由于付费墙和机器人拦截，抓取新闻网站变得更加困难，需要不断与出版商进行谈判。社交网络的碎片化和限制增加降低了可用新闻信号的可用性。最后，广告收入更加依赖于与高级决策者的直接关系。

Techmeme认为，传统新闻业被“公民新闻”或创始人直接发布内容所取代的彻底媒体改革的想法在很大程度上被夸大了。信誉良好的新闻媒体仍然在基于事实的叙事中发挥着至关重要的作用，科技专业人士依赖这些来源获取可靠的信息。此外，虽然像X这样的平台可以提供快速的新闻更新，但它们只代表整个科技新闻领域的一小部分，重要的对话发生在其他网络，如Bluesky和Threads。

展望未来，Techmeme承认未来的不确定性，但专注于在其现有基础上进行建设，包括新闻制作者和公关专业人员明确提示链接的新方法。文章强调，虽然媒体格局不断发展，但新闻传播的核心原则仍然适用，这使Techmeme能够保持其始终如一的存在。

---

## 19. Show HN: 我做了一个交互式 HN 模拟器

**原文标题**: Show HN: I built an interactive HN Simulator

**原文链接**: [https://news.ysimulator.run/news](https://news.ysimulator.run/news)

作者构建了一个交互式的 Hacker News (HN) 模拟器。虽然提供的文本非常简短，但核心思想是它允许用户体验流行的聚合新闻和在线论坛 Hacker News 的模拟环境。该模拟器旨在复制 HN 体验的各个方面，可能包括：

*   **模拟的 HN 帖子：** 用户可能会看到模拟的标题、评论和投票。
*   **交互式元素：** 模拟可能允许用户赞成、反对、评论，并可能提交他们自己的（模拟的）帖子。
*   **模仿 HN 社区：** 模拟器可能会尝试捕捉 Hacker News 平台的语气、讨论类型和整体感觉。

在没有更多信息的情况下，不可能详细说明模拟器的具体细节，但其核心目的是提供 Hacker News 体验的交互式模拟版本。

---

## 20. 从GPT-3到Gemini 3的三年

**原文标题**: Three Years from GPT-3 to Gemini 3

**原文链接**: [https://www.oneusefulthing.org/p/three-years-from-gpt-3-to-gemini](https://www.oneusefulthing.org/p/three-years-from-gpt-3-to-gemini)

伊森·莫里克的文章《从GPT-3到Gemini 3的三年》反思了自ChatGPT发布以来人工智能的快速发展，并探讨了谷歌新模型Gemini 3的功能。莫里克没有使用基准测试分数，而是通过展示Gemini 3执行复杂任务和作为数字同事的能力来证明人工智能的进步。

他强调了从简单的聊天机器人功能到能够编码、设计界面甚至创建互动游戏的代理模型的转变。随着Antigravity的推出，Gemini 3可以访问计算机、编写程序并根据自然语言指令完成任务，有效地发挥通用工具的作用。莫里克通过让Gemini 3分析他过去的著作、进行网络研究并创建一个总结他的人工智能预测的网站来阐明这一点。

此外，莫里克通过让Gemini 3分析一个复杂的数据集并撰写一篇原创研究论文来测试其“博士级智能”。人工智能成功地生成了假设、进行了统计分析并生成了格式化的文档。虽然该论文存在一些缺陷，类似于研究生所做的工作，但它证明了人工智能处理需要判断力和创造力的细微任务的能力。

莫里克总结说，Gemini 3是一个重要的进步，代表着从“人在回路中”纠正人工智能错误到人类指导人工智能工作的协作模型的转变。虽然Gemini 3并非完美，但它标志着人工智能从聊天机器人到智能数字同事的演变，需要新的方法来管理和指导这些能力越来越强的系统。

---

## 21. 从洛杉矶看原子弹试验是怎样的

**原文标题**: How the Atomic Tests Looked Like from Los Angeles

**原文链接**: [https://www.amusingplanet.com/2016/09/how-atomic-tests-looked-like-from-los.html](https://www.amusingplanet.com/2016/09/how-atomic-tests-looked-like-from-los.html)

本文探讨了1951年至1992年间在内华达试验场进行的大气原子弹试验，以及洛杉矶（约240英里之外）的可见度。作者强调了当时记录和看待这些事件的随意甚至近乎庆祝的方式，并将其与现代对潜在危险的理解进行了对比。

文章引用了报纸报道和照片，显示了原子弹爆炸如何照亮夜空，甚至在洛杉矶造成“第二次黎明”。这些事件被认为是具有新闻价值和引人入胜的，当地电视台对其进行了直播。

作者将这种随意的态度与辐射暴露的风险并置。文章承认在20世纪中期对核武器存在一种天真的迷恋，但也暗示了对潜在健康后果缺乏认识或关注。

文章最后提到了拉斯维加斯对原子弹试验的热情拥抱，赌场和酒店举办“原子鸡尾酒”派对来观看爆炸。文章评论区强调了对残留辐射的担忧以及关于癌症原因的争论，突出了这些试验复杂而有争议的遗产。

---

## 22. Windows GUI – 好、坏与丑陋 (2023)

**原文标题**: Windows GUI – Good, Bad and Pretty Ugly (2023)

**原文链接**: [https://creolened.com/windows-gui-good-bad-and-pretty-ugly-ranked/](https://creolened.com/windows-gui-good-bad-and-pretty-ugly-ranked/)

本文幽默地对Windows图形用户界面(GUI)的演变进行了排名，从1985年Windows 1.0的诞生到现在的Windows 11 (2023)。作者使用“Clippy”评分（1-10）来评价每个主要版本，基于的是它们*现在*的观感，而非当时它们有多么创新。

排名如下：Windows 11 (8)，Windows 2000 (8)，Windows 95/98/Vista/7 (7.5)，Windows 10 (6.5)，Windows 3.0/3.1/XP (6)，Windows 8.1 (5.5)，Windows 8 (5)，Windows 2.0 (2.5)，和Windows 1.0 (1)。

作者赞扬Windows 3.0提供了连贯的GUI和专业的外观。Windows 95因其功能性的设计和对苹果的影响而受到赞扬。Windows Vista因其成熟、光鲜的美学而受到认可。Windows 11被认为是自2000年以来最精致的版本，尽管有一些限制。

Windows XP因其卡通般的外观而受到批评，而Windows 8则被认为是重大倒退，因为它以平板电脑为中心的设计和移除了“开始”菜单。早期版本（1.0和2.0）被认为是受到当时技术的限制。Windows 10被视为是为了弥补Windows 8的错误而进行的拼凑之作。

作者最后推测了Windows 12的潜在设计，预计其可能与Windows 11保持连续性。

---

## 23. Go中数据竞争导致死亡的一百万种方式

**原文标题**: A million ways to die from a data race in Go

**原文链接**: [https://gaultier.github.io/blog/a_million_ways_to_data_race_in_go.html](https://gaultier.github.io/blog/a_million_ways_to_data_race_in_go.html)

Philippe Gaultier 的这篇文章探讨了 Go 中常见的数据竞争陷阱并提供了解决方案。文章强调，尽管 Go 以并发性著称，但数据竞争很容易引入，导致不可预测的行为。

第一个讨论的陷阱是**闭包中意外捕获外部变量**，其中 goroutine 无意中修改了共享变量，可以通过在闭包中声明局部变量来解决。

文章接着讨论了 `http.Client` 的并发使用。 虽然它被记录为并发安全，但并发修改其字段（如 `CheckRedirect`）会导致数据竞争。 解决方案是为每个 goroutine 使用单独的 `http.Client` 实例。

第三个问题是 **mutex 的生命周期不当**。 作者描述了一种情况，即全局 map 受由每个 HTTP 处理程序中创建的 mutex 保护，导致多个 mutex 保护相同的数据，从而使同步无效。 解决方法是使数据和 mutex 都成为全局变量，或者为每个处理程序深度克隆数据。

最后，文章简要提到了涉及标准库容器（如 map 和 slice）的常见数据竞争，以及使用 mutex 或并发安全数据结构进行同步的必要性。

作者最后建议，受 Rust 包装数据方法启发的更好的 mutex API 可以缓解其中一些问题，并感叹 Go 中缺少内置的深度克隆函数。 他强调，Go 中的数据竞争不仅与同步有关，还与对象所有权和对象生命周期有关。

---

## 24. 人工智能对学校的影响

**原文标题**: Implications of AI to schools

**原文链接**: [https://twitter.com/karpathy/status/1993010584175141038](https://twitter.com/karpathy/status/1993010584175141038)

提供的并非一篇关于人工智能对学校影响的文章，而是来自X（前身为Twitter）的一段信息，显示用户的浏览器已禁用JavaScript。因此，页面无法正确渲染，并且没有关于人工智能和学校的内容。

因此，无法总结文章，因为内容是技术错误消息，而不是关于人工智能及其对教育影响的文章。要获得摘要，需要提供一篇关于“人工智能对学校的影响”的有效文章。

---

## 25. Cool-retro-term：模拟CRT外观的终端模拟器

**原文标题**: Cool-retro-term: terminal emulator which mimics look and feel of CRTs

**原文链接**: [https://github.com/Swordfish90/cool-retro-term](https://github.com/Swordfish90/cool-retro-term)

Cool-retro-term：一款旨在模仿老式阴极射线管(CRT)屏幕视觉效果的终端模拟器，可定制、轻量且美观。该模拟器使用qtermwidget (Konsole)的QML端口，支持Linux和macOS，需要Qt5。

用户可以通过上下文菜单自定义颜色、字体和视觉效果等设置。预构建版本可以从发布页面下载，格式为AppImage (Linux) 或 dmg (macOS)。它也被打包在许多发行版的官方仓库中，如Ubuntu、Fedora和Arch。在项目的wiki中可以找到关于在Linux和macOS上从源代码构建该模拟器的说明。

---

## 26. 五个项目构建编译器

**原文标题**: Build a Compiler in Five Projects

**原文链接**: [https://kmicinski.com/functional-programming/2025/11/23/build-a-language/](https://kmicinski.com/functional-programming/2025/11/23/build-a-language/)

本文介绍一门基于 Jeremy Siek 教授的“编译原理精要”并使用 Racket 编程语言教授的编译器设计课程 (CIS531)。该课程提供了一种实践性的、基于项目的学习方法，用于构建一个针对逐步复杂的语言的编译器，最终实现对变量、算术、布尔值、分支、堆分配向量、循环以及带闭包的函数等特性的支持。

课程的核心是一系列五个项目：p1 (Racket 热身)，p2 (直线算术到 x86-64)，p3 (布尔/分支到 x86-64)，p4 (向量/变异/循环到 x86-64)，和 p5 (函数/lambda/闭包到 x86-64)。每个项目都附带全面的测试套件。本文重点介绍了编译器的独特功能，包括其端到端 x86-64 编译、用于语义清晰的基于解释器的 IR 定义、语言可扩展性、多通道可测试性以及简单的递归编码风格。

本文概述了每个项目的结构，重点介绍了诸如 `compile.rkt`（学生编写代码的地方）、`irs.rkt`（IR 定义）、`interpreters.rkt`（参考解释器）、`main.rkt`（编译器驱动程序）和 `test.rkt`（测试工具）等关键文件。 目标是尽快使语言尽可能具有表现力和趣味性，即使这意味着放弃类型/内存安全和垃圾收集等功能（尽管这些功能可以在以后添加）。 最后，作者鼓励读者尝试这些项目，在基本编译器之上进行构建，并分享他们的经验。

---

## 27. Show HN: OCR竞技场 – OCR模型的游乐场

**原文标题**: Show HN: OCR Arena – A playground for OCR models

**原文链接**: [https://www.ocrarena.ai/battle](https://www.ocrarena.ai/battle)

OCR竞技场是一个用于匿名比较OCR（光学字符识别）模型的游乐场网站。用户可以上传图像（PDF、JPEG、PNG）并启动两个匿名OCR模型之间的“战斗”。该网站根据模型的Elo评级、胜率和战斗次数来跟踪模型的排名。用户可以上传自己的文档或请求随机文档进行测试。主要功能包括：

*   **OCR模型战斗：** 并排比较两个匿名OCR模型的性能。
*   **匿名参与：** 用户无需注册即可参与，确保公正的测试。
*   **排名系统：** 模型根据Elo、胜率和战斗次数进行排名。
*   **文件支持：** 接受PDF、JPEG和PNG文件。
*   **文档来源：** 用户可以上传自己的文档或请求随机文档进行测试。

该网站旨在提供一个平台，通过众包比较来评估和改进OCR技术。

---

## 28. 重新思考 C++：架构、概念与责任

**原文标题**: Rethinking C++: Architecture, Concepts, and Responsibility

**原文链接**: [https://blogs.embarcadero.com/rethinking-c-architecture-concepts-and-responsibility/](https://blogs.embarcadero.com/rethinking-c-architecture-concepts-and-responsibility/)

本文倡导对C++开发进行根本性的反思，这得益于C++20和C++23的进步，尤其是在C++Builder 13的背景下。作者认为，现代C++不仅是一种进化，更是一场革命，要求开发者超越将其作为简单工具的使用方式，而将其拥抱为一种“架构媒介”。

关键点包括：

*   **基于概念的编程:** 强调使用概念来定义接口并实现编译时验证，从而提高代码安全性和效率。
*   **元编程:** 强调为编译器设计蓝图的重要性，从而在编译时实现优化的代码生成并减少运行时开销。
*   **范围 (Ranges):** 介绍了范围在数据处理方面的强大功能，允许使用声明式的、类似管道的描述，这些描述是类型安全的且可重用的。
*   **RAII:** 强调资源获取即初始化 (RAII) 对于确保资源安全和确定性控制的重要性，将对象生命周期与系统稳定性联系起来。
*   **责任转移:** 强调将重点从运行时执行转移到编译时设计和优化。
*   **重新学习C++:** 敦促开发者“重返校园”并重新学习C++，以有效地利用新的语言特性。

作者通过将C++概念和范围与Delphi库（如VCL和FMX）集成的例子来说明这些观点。最终，本文呼吁新一代C++库拥抱概念、类型列表和编译时机制，并敦促库和编译器供应商充分释放现代语言的潜力。

---

## 29. 当ChatGPT用户失去现实感时，OpenAI做了什么

**原文标题**: What OpenAI did when ChatGPT users lost touch with reality

**原文链接**: [https://www.nytimes.com/2025/11/23/technology/openai-chatgpt-users-risks.html](https://www.nytimes.com/2025/11/23/technology/openai-chatgpt-users-risks.html)

无法访问文章链接。

---

## 30. 为2030年及以后选择哈希函数：SHA-2 vs. SHA-3 vs. BLAKE3

**原文标题**: Choosing a hash function for 2030 and beyond: SHA-2 vs. SHA-3 vs. BLAKE3

**原文链接**: [https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)

提供的现有内容不足以总结文章《为2030年及以后选择哈希函数：SHA-2 vs. SHA-3 vs. BLAKE3》。仅提供了标题和一个JavaScript错误消息。为了提供摘要，需要提供文章的实际内容，讨论每种哈希算法（SHA-2、SHA-3 和 BLAKE3）的优缺点。

由于无法访问该文章，我只能推测它*可能*涵盖的潜在要点：

*   **SHA-2：**讨论其广泛采用、已知漏洞（尽管通常认为对于许多应用程序仍然安全）以及潜在的性能限制。其存在时间可能是一个长期安全考虑因素。

*   **SHA-3：**探讨其作为对 SHA-2 担忧的回应而进行的开发、其对某些类型攻击的抵抗力以及在特定硬件实现中的潜在优势。但是，它也可能涉及与 SHA-2 相比，其采用范围较小的问题。

*   **BLAKE3：**强调其现代设计、性能优势（尤其是在并行处理方面）、安全优势以及在各种环境中的日益普及。它还可能讨论其对不同用例的适用性。

*   **2030年及以后的考量因素：**该文章可能深入探讨了计算能力进步（影响暴力破解攻击）、量子计算的出现以及在选择用于长期使用的哈希算法时不断发展的安全需求等因素。因此，该摘要需要涵盖基于其固有的设计原则以及对这些未来问题的脆弱性，SHA-2、SHA-3 或 BLAKE3 中哪一个最适合未来。

因为这是假设性的，所以不能将其视为基于所提供输入的文章的真实摘要。

---

## 31. 印度科幻史

**原文标题**: The history of Indian science fiction

**原文链接**: [https://altermag.com/articles/the-secret-history-of-indian-science-fiction](https://altermag.com/articles/the-secret-history-of-indian-science-fiction)

高塔姆·巴蒂亚的《印度科幻秘史》一文追溯了印度科幻小说的起源和发展。巴蒂亚认为罗克娅·萨卡瓦特·侯赛因的《苏丹娜之梦》（1905）是印度科幻小说的一部开创性作品，它运用了陌生化和认知疏离等技巧来批判父权制的社会关系，并构想了一个科技乌托邦社会。

该文章探讨了乌尔都语和孟加拉语作品中印度思辨小说的发展，包括《蒂利斯姆-埃-霍什鲁巴》和贾格迪什·钱德拉·玻色（Jagdish Chandra Bose）的《消失的故事》，其中“kalpavigyan”一词开始用来描述孟加拉科幻小说。它还考察了拉胡尔·桑克里提亚扬的乌托邦小说《二十二世纪》，并将其与叶夫根尼·扎米亚京的反乌托邦小说《我们》进行比较，突出了围绕乌托邦理想的全球对话。

巴蒂亚强调《苏丹娜之梦》作为一部用英语创作的女性主义作品的独特性，并将其与后殖民时期印度英语小说中社会现实主义的 dominant 地位相比较。该文章进一步讨论了西方英语科幻小说的发展，包括通俗杂志、“黄金时代”、20世纪60年代的反文化运动以及赛博朋克的兴起。该文章强调，印度科幻小说虽然在非英语语言中蓬勃发展，涌现了萨蒂亚吉特·雷伊和苏贾塔等作家，但在很大程度上与国际趋势隔绝，并且经常侧重于将娱乐与教育相结合的“科学小说”。

---

## 32. 克勞德 Opus 4.5

**原文标题**: Claude Opus 4.5

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-5](https://www.anthropic.com/news/claude-opus-4-5)

Claude Opus 4.5：Anthropic最新AI模型，在编码、代理能力和计算机使用方面有显著提升，并在研究和数据处理方面有所改进。可通过API和云平台使用，定价为每百万token 5美元/25美元。

早期测试者和客户称赞其处理歧义、权衡利弊和修复复杂错误的能力。用户评价强调其卓越的代码质量、代理工作流程效率、复杂企业任务性能以及在长周期自主任务中的出色表现。该模型还在自我改进AI代理、自动化、故事讲述和Excel功能方面取得了突破。

评估显示，Opus 4.5 在 SWE-bench Multilingual、Aider Polyglot、BrowseComp-Plus 和 Vending-Bench 等基准测试中表现优异，取得了最先进的成果。在一个案例中，它超过了人类在性能工程家庭作业考试中获得的最高分。它展示了即使在没有预期的情况下也能找到创造性解决方案的能力，这一特点使其与众不同。

Opus 4.5 的安全对齐和抵抗提示注入攻击的能力也备受重视。Claude API 上的一个新努力参数允许开发人员优化速度或能力。更新包括改进 Claude Code，从而实现更精确的规划和桌面应用程序集成。此外，Claude 应用程序用户受益于更长对话的自动摘要，Chrome 和 Excel 版 Claude 的访问权限也得到扩展。

---

## 33. Chrome JPEG XL 问题重新开启

**原文标题**: Chrome Jpegxl Issue Reopened

**原文链接**: [https://issues.chromium.org/issues/40168998](https://issues.chromium.org/issues/40168998)

请提供Chromium文章《Chrome Jpegxl问题重开》的内容。我需要文章的文本来为您总结。没有内容，我无法提供摘要。

---

## 34. 沙虫归来：超过 300 个 NPM 包受感染

**原文标题**: Shai-Hulud Returns: Over 300 NPM Packages Infected

**原文链接**: [https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)

安全研究公司HelixGuard报告称，超过300个NPM软件包已感染名为“沙虫归来”的恶意活动。该活动涉及入侵合法的NPM软件包维护者账户，并将恶意代码注入其软件包。该恶意代码旨在窃取敏感信息，可能包括环境变量、凭据和API密钥。

此次攻击规模庞大，影响超过300个软件包，凸显了NPM生态系统持续存在的漏洞。它表明攻击者正在通过供应链攻击积极 targeting 开发者及其依赖项。 这项活动强调了开发者仔细审查其依赖项、实施强大的账户安全措施（如MFA）以及定期审核其项目以查找可疑代码的关键需求。HelixGuard的开源研究旨在提高人们的意识，并为开发者提供保护自己及其项目免受这种持续威胁所需的信息。 本文旨在作为警告，并呼吁改进NPM安全实践。

---

## 35. 读心设备现在可以预测潜意识的想法

**原文标题**: Mind-reading devices can now predict preconscious thoughts

**原文链接**: [https://www.nature.com/articles/d41586-025-03714-0](https://www.nature.com/articles/d41586-025-03714-0)

本文探讨了脑机接口(BCI)的进展及其解码前意识思想和意图的潜力。文章重点介绍了南希·史密斯的案例，她使用植入在顶后皮层的脑机接口来播放音乐，该设备在她有意识地启动行动之前就预测了她的行为。这例证了“双植入”脑机接口通过捕获意图和运动前计划来提高假肢设备性能的潜力。

文章还探讨了这些设备访问个人内心最深处想法（包括前意识想法）能力不断增强所带来的伦理问题。 这引发了关于数据隐私、潜在操纵以及监管需求的质疑，尤其是在使用脑电图监测大脑状态的消费级神经技术产品方面。 尽管临床脑机接口面临医疗监管，但消费级脑机接口的监管有限，这可能允许公司利用神经数据。

文章指出，一些法律正在通过以保护神经数据，但伦理学家认为，这些法律需要解决公司将神经信息与其他数字数据相结合时可能进行的推断。 虽然植入式脑机接口尚未获准用于一般临床用途，但Synchron和Neuralink等公司正在临床试验方面取得进展，重点是恢复瘫痪患者的独立性。 最终，脑机接口开发者旨在超越运动皮层，通过识别和监测神经信号并提供量身定制的刺激来解决精神疾病，而这会引发更多的伦理考量。

---

## 36. 谷歌全新“铝制操作系统”项目将安卓带到PC

**原文标题**: Google's new 'Aluminium OS' project brings Android to PC

**原文链接**: [https://www.androidauthority.com/aluminium-os-android-for-pcs-3619092/](https://www.androidauthority.com/aluminium-os-android-for-pcs-3619092/)

谷歌正在开发代号为“铝”的新操作系统Aluminium OS，该系统基于安卓，旨在将ChromeOS和安卓统一到一个桌面平台，更好地与Windows和macOS竞争。该项目在骁龙峰会上正式宣布，涉及与高通的合作，以利用人工智能的进步，并将安卓的功能带入PC市场。

已披露的关键细节包括：

*   **Aluminium OS 代号：** “铝”已被确认为代号，是对安卓作为基础的一种致敬。
*   **人工智能集成：** 该操作系统将与谷歌的人工智能聊天机器人Gemini深度集成，以利用硬件潜力并提供增强的人工智能功能。
*   **目标硬件：** 该操作系统将涵盖各种外形尺寸（笔记本电脑、可拆卸设备、平板电脑、迷你PC）和层级（入门级到高端级），表明谷歌有意在整个PC领域展开竞争。
*   **ChromeOS 的未来：** 谷歌计划最终用Aluminium OS取代ChromeOS，但很可能会为现有设备提供旧版支持，并为兼容硬件提供可选的升级途径。
*   **品牌：** 最终名称尚不确定，但可能性包括保留ChromeOS品牌或采用“Android桌面”。
*   **发布时间表：** 初步公开版本预计在2026年发布，很可能基于Android 17构建。

此举旨在整合开发资源，并创建一个更具竞争力的桌面操作系统，重点是人工智能集成和更广泛的硬件支持。

---

## 37. 蠢蠢的死法：印刷品

**原文标题**: Dumb Ways to Die: Printed Ephemera

**原文链接**: [https://ilovetypography.com/2025/11/19/dumb-ways-to-die-printed-ephemera/](https://ilovetypography.com/2025/11/19/dumb-ways-to-die-printed-ephemera/)

无法访问文章链接。

---

## 38. 从OpenBSD迁移到FreeBSD作为防火墙

**原文标题**: Moving from OpenBSD to FreeBSD for firewalls

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/sysadmin/OpenBSDToFreeBSDMove](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/OpenBSDToFreeBSDMove)

这不是一篇关于将防火墙从OpenBSD迁移到FreeBSD的文章。这是Chris Siebenmann的消息，解释了为什么读者在访问他的博客Wandering Thoughts或他的维基CSpace时可能会遇到错误信息。

Siebenmann实施了反爬虫措施，以应对大量涌入的高流量爬虫，尤其是那些使用旧Chrome浏览器用户代理的爬虫，这是一种普遍存在于为LLM训练收集数据的爬虫中的策略。该系统无意中阻止了使用过时浏览器的合法用户。

如果用户使用当前浏览器遇到此消息，他们将被指示联系作者（Chris Siebenmann在他的大学），并提供他们的浏览器和User-Agent字符串以进行故障排除。

该消息专门针对像archive.today、archive.ph和archive.is这样的存档服务的用户。这些服务也被无意中阻止，因为它们以与恶意行为者无法区分的方式爬取页面，使用旧的Chrome User-Agent值、分布式IP地址，有时还使用伪造的反向DNS条目。Siebenmann建议改用archive.org，因为它是一个行为更好的存档爬虫。

---

## 39. AI 对这段代码的工作原理有深刻的理解。

**原文标题**: AI has a deep understanding of how this code works

**原文链接**: [https://github.com/ocaml/ocaml/pull/14369](https://github.com/ocaml/ocaml/pull/14369)

此 GitHub issue 详细介绍了一个 pull request (PR)，该 PR 为 macOS 和 Linux（AMD64 和 ARM64 架构）的 OCaml 本机编译器添加了 DWARF v5 调试支持。目标是在 GDB 和 LLDB 中启用源代码级调试。

该 PR 实现了核心 DWARF v5 支持，使用内联字符串以避免链接器问题、使用字符串表去重的多编译单元支持以及节相对重定位。 它支持函数/行级调试、参数/局部变量跟踪、词法块和基本的 OCaml 类型信息。平台支持全面，覆盖 Linux/ELF 和 macOS/Mach-O，明确禁用了 Windows。 一个自定义的 LLDB 插件用于格式化 OCaml 值，一个测试套件用于验证功能。

该实现跨越 37 个提交，包括 DWARF 原始结构构建、行号程序生成、代码地址跟踪以及与 OCaml 编译管道的集成。 主要变更包括从 DWARF v4 升级到 v5、利用 `DW_FORM_string` 来避免 macOS 链接器问题，以及针对函数/行断点、类型信息和多对象链接的全面验证测试。

该 PR 使用一个新的 `Variable_info` 模块在 DWARF 调试信息中保留源代码级参数名称和局部变量。 添加了词法块支持以进行嵌套作用域跟踪。 添加了代码来处理特定于架构的寄存器编号映射，并通过将 `-g` 标志传递给链接器来确保在链接期间保留 DWARF 节。

一位审查员发现了未使用的函数，随后将其删除。 一条评论引发了对代码归属的担忧，质疑这项工作是否大量来源于另一位作者。

---

## 40. LLM扩展的惨痛教训

**原文标题**: The Bitter Lesson of LLM Extensions

**原文链接**: [https://www.sawyerhood.com/blog/llm-extension](https://www.sawyerhood.com/blog/llm-extension)

本文写于2025年，回顾了过去三年扩展大型语言模型(LLM)的演变。文章重点介绍了从简单的基于文本的交互到能够与代码库、浏览器和其他工具交互的复杂基于代理的系统的转变。

作者追溯了这一发展过程中的关键里程碑：ChatGPT插件（雄心勃勃但由于模型限制而过早）、自定义指令（一种简单但有效的重复上下文解决方案）、自定义GPT（一种精选的应用程序方法）和ChatGPT记忆（自动个性化）。一项重大进展是Cursor引入了`.cursorrules`文件，实现了在代码仓库中设置上下文。

文章随后讨论了模型上下文协议(MCP)，这是一种用于工具集成和资源配置的重量级客户端-服务器解决方案，被认为可能过于复杂。Claude Code是一种集成了各种扩展机制（如CLAUDE.md、MCP和斜杠命令）的代理，被呈现为一种全面但以开发者为中心的方法。

转折点是Claude Code中引入的代理技能，这是一种更轻量级的、基于Markdown的系统，让人联想到ChatGPT插件，但由于模型能力的提高，现在是可行的。代理技能允许模型利用通用工具和指令来完成任务，标志着回归到自然语言可扩展性。

作者总结道，LLM扩展的未来在于为模型配备通用工具，并相信它们能够有效地利用这些工具，本质上是将一台计算机绑在LLM上。作者预测，未来将从复杂的协议（如MCP）转向更易于访问的、基于自然语言的扩展。他设想未来的应用程序将无缝地将LLM与计算能力集成在一起，从而将底层复杂性从最终用户那里抽象出来。

---

## 41. 构建已知最大的Kubernetes集群

**原文标题**: Building the largest known Kubernetes cluster

**原文链接**: [https://cloud.google.com/blog/products/containers-kubernetes/how-we-built-a-130000-node-gke-cluster/](https://cloud.google.com/blog/products/containers-kubernetes/how-we-built-a-130000-node-gke-cluster/)

2025年11月，谷歌云宣布成功在实验模式下运行了一个拥有13万个节点的 Kubernetes 集群，是GKE官方支持上限的两倍。 这一成就解决了人工智能工作负载驱动的对大型集群日益增长的需求，从芯片限制过渡到电力限制。 文章强调了对稳健的多集群解决方案（如 MultiKueue）的需求，以便在数据中心之间进行分布式训练。

实现这种规模的关键架构创新包括优化读取可扩展性，使用诸如从缓存进行一致性读取和可快照的API服务器缓存等功能，从而减少中央对象数据存储上的负载。 一个基于谷歌 Spanner 分布式数据库的专有键值存储至关重要，它处理了租赁对象更新的13,000 QPS。 作业队列控制器 Kueue 管理着复杂的AI/ML环境，具有公平共享策略和“全有或全无”调度。 未来涉及工作负载感知调度，从而简化 GKE 上的大规模应用程序。 具有区域性 Anywhere Cache 的 GCS FUSE 提供了高效的数据访问，从而降低了 AI 工作负载的延迟。

为了验证 GKE 的性能，一个四阶段基准测试模拟了一个动态的 AI 环境，其中混合了由 Kueue 和 JobSet 管理的各种工作负载（低、中、高优先级）。 该基准测试证明了 GKE 处理波动需求的能力，抢占低优先级作业，在不到 4 分钟内扩展到 13 万个 Pod，并维持高达每秒 1,000 个 Pod 的吞吐量。 Kueue 根据优先级动态分配资源，展示了 GKE 的弹性和资源重新分配能力。

---

## 42. 面向对象编程的五十道阴影

**原文标题**: Fifty Shades of OOP

**原文链接**: [https://lesleylai.info/en/fifty_shades_of_oop/](https://lesleylai.info/en/fifty_shades_of_oop/)

《面向对象编程的五十度灰》是一篇避免直接捍卫或攻击面向对象编程(OOP)的文章，而是旨在通过单独审视其核心思想来提供一个细致的视角。作者认为，“OOP”一词的使用过于宽泛，导致富有成效的对话变得困难，并建议将其视为一系列相互关联的概念的集合。

文章随后考察了OOP的各个方面，包括：

*   **类：** 基于带有方法、信息隐藏和继承的结构体。原型被呈现为一种替代方案。
*   **方法语法：** 一种用于对特定数据进行操作的有用约定，有助于IDE自动完成和链式调用。缺点包括在类外部定义的限制、隐式的`this`指针以及与自由函数的潜在冲突。
*   **信息隐藏：** 防止违反不变式并分离稳定的接口。缺点包括潜在的样板代码和抽象反转。
*   **封装：** 捆绑数据和函数。存在诸如闭包和模块系统之类的替代方案。面向数据的设计提供了一种更粗粒度的替代方案，专注于高效的数据处理。
*   **接口：** 促进接口和实现的分离，支持多态。可能会有运行时成本，但并非总是如此。
*   **延迟绑定：** 将方法/成员查找推迟到运行时，从而实现热重载，但会影响性能并引入潜在错误。
*   **动态分派：** 在运行时选择多态操作，通常使用虚函数表实现。由于内联限制和缓存未命中，可能导致性能问题。
*   **继承：** 最具标志性的OOP特性，支持动态分派、子类型化、接口隔离和代码重用。因其非正交性、强加的性能成本、不健全的子类型化实现以及刚性而受到批评。
*   **子类型多态：** 定义类型之间的“是”关系。通过继承受到OOP的支持，但也受到其他构造的支持。

---

## 43. Win 95的用户界面代码是如何引入到Windows NT代码库中的？

**原文标题**: How did the Win 95 user interface code get brought to the Windows NT code base?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20251028-00/?p=111733](https://devblogs.microsoft.com/oldnewthing/20251028-00/?p=111733)

本文阐述了Windows 95用户界面如何集成到Windows NT 4.0代码库中，并重点介绍了所面临的挑战和采用的策略。

对于窗口管理器功能，Windows NT团队重新实现了Windows 95的代码作为参考，利用了Windows 3.1的共同血统，同时适应了已经分化的代码库。 这是一个从Windows 95到Windows NT的单向移植。

对于资源管理器和其他用户模式组件，Windows 95的代码被“原样”采用，然后在适当的位置进行修改，以适应Windows NT环境，特别是适应Unicode。 这导致了诸如IShellLinkA和IShellLinkW等接口的Unicode变体的创建。这是一个双向过程，Windows NT团队所做的更改会被合并回Windows 95代码库中，以避免冗余修复。

为了确保Windows 95代码的稳定性，Windows NT团队使用了诸如`#ifdef WINNT`指令、`TCHAR`等宏以及`SIZEOF`宏等技术。 `SIZEOF`用于指示是否已针对Windows NT兼容性审查了`sizeof`调用，从而有助于识别仍需要检查的区域。

由于微软内部源代码系统SLM不支持分支，合并过程非常复杂。 这需要手动合并代码库之间的更改。 Windows NT团队，包括Dave Plummer，甚至制作了定制的“你已被访问”名片。

---

## 44. Rust标准库和parking_lot互斥锁的内部机制——谁更胜一筹？

**原文标题**: Inside Rust's std and parking_lot mutexes – who wins?

**原文链接**: [https://blog.cuongle.dev/p/inside-rusts-std-and-parking-lot-mutexes-who-win](https://blog.cuongle.dev/p/inside-rusts-std-and-parking-lot-mutexes-who-win)

本文深入探讨Rust中`std::sync::Mutex`和`parking_lot::Mutex`的实现，以确定它们的性能特征以及何时选择其中一个。

作者解释说，`std::sync::Mutex`利用平台特定的互斥锁实现，通常在使用futexes（快速用户空间互斥锁）的地方。Futexes依赖于原子操作和内核管理的等待队列以提高效率。一个独特的特性是中毒，如果一个线程在持有互斥锁时发生panic，互斥锁将变得不可用，从而防止数据损坏。

`parking_lot::Mutex`采取了一种不同的方法，在所有平台上使用单一算法，并通过全局哈希表在用户空间中管理自己的等待队列。这使得它可以使用单个字节作为其互斥锁状态，不像`std`的更大的AtomicU32（内核对futex队列对齐所需）。它实现了最终公平性，通过使用一个定时器（每约0.5毫秒）强制将锁传递给等待时间最长的线程，以防止线程饥饿。

基准测试结果表明，由于其高效的内核管理队列，`std`在具有短临界区的中等争用下通常表现更好。然而，`parking_lot`提供了更均匀的工作分配。在具有长持有时间的大量争用下，`parking_lot`通常在吞吐量和延迟方面超越`std`。

---

## 45. PS5现价低于64GB DDR5内存，内存短缺致价格飙升至600美元。

**原文标题**: PS5 now costs less than 64GB of DDR5 memory. RAM jumps to $600 due to shortage

**原文链接**: [https://www.tomshardware.com/pc-components/ddr5/64gb-of-ddr5-memory-now-costs-more-than-an-entire-ps5-even-after-a-discount-trident-z5-neo-kit-jumps-to-usd600-due-to-dram-shortage-and-its-expected-to-get-worse-into-2026](https://www.tomshardware.com/pc-components/ddr5/64gb-of-ddr5-memory-now-costs-more-than-an-entire-ps5-even-after-a-discount-trident-z5-neo-kit-jumps-to-usd600-due-to-dram-shortage-and-its-expected-to-get-worse-into-2026)

人工智能热潮导致DDR5内存价格飙升：G.Skill 64GB套装价格已超PS5 Slim或Xbox Series S。

---

## 46. 使用反重力进行 JavaScript 统计物理模拟

**原文标题**: Using Antigravity for Statistical Physics in JavaScript

**原文链接**: [https://christopherkrapu.com/blog/2025/antigravity-stat-mech/](https://christopherkrapu.com/blog/2025/antigravity-stat-mech/)

作者探索了谷歌新款反重力 IDE (基于 Windsurf) 和 Gemini 3 Pro 的性能，通过使用它创建了一个基于 JavaScript 的铁磁性伊辛模型可视化。作者之前使用涉及晦涩互联网人物的隐藏基准问题来测试 LLM，现在已将重点转向 JavaScript 中的统计物理可视化。

伊辛模型，一种铁磁性的数学表示，被描述了其核心方程和模拟方法：随机扫描吉布斯采样器基于受邻居和外场影响的玻尔兹曼分布更新随机选择的自旋。

作者强调，反重力 IDE 与 Gemini 3 Pro 相结合，在一小时内产生了不错的结果，并特别赞扬了 Chrome 浏览器扩展程序检索 DOM 的功能。虽然一些 UI 功能，如子任务和中间步骤显示，被认为不太重要，但作者对反重力 IDE 及其底层技术给出了积极的评价，并肯定了前 Windsurf 团队和谷歌员工的努力。作者还预计类似的功能将被集成到竞争 IDE 中，如 Cursor。

---

## 47. 日本豪赌将北海道打造为全球芯片中心

**原文标题**: Japan's gamble to turn island of Hokkaido into global chip hub

**原文链接**: [https://www.bbc.com/news/articles/c8676qpxgnqo](https://www.bbc.com/news/articles/c8676qpxgnqo)

日本大力投资将北海道打造为全球半导体中心，旨在重振其衰落数十年的芯片制造能力。这项工作的核心是政府支持的Rapidus公司，该公司正在千岁市建设一座最先进的芯片代工厂，目标是在2027年实现2纳米芯片的量产。

政府已对Rapidus进行了大量投资，该公司还与IBM和其他全球公司合作以获取必要的技术。Rapidus已经通过生产2纳米原型取得了突破。尽管取得了这些进展，仍然存在挑战，包括获得足够的资金，获取必要的专业知识，以及在由台积电和三星主导的高度竞争的市场中建立客户群。

日本更广泛的战略包括吸引台积电等主要全球参与者（该公司已经在九州生产芯片），并创建一个蓬勃发展的供应商和相关产业生态系统。政府的支持范围扩大到其他国内企业，如铠侠和东芝，以及吸引美光和三星等外国公司的投资。

尽管日本面临人口萎缩、工程师短缺以及需要依赖外国工人等障碍，但政府致力于重振其半导体产业，确保其科技实力。Rapidus的目标是通过更快地生产定制芯片来脱颖而出，利用人工智能驱动的全球需求激增以及对安全、国内采购的供应链的需求。这项“北海道硅谷”计划的成功被认为是恢复日本作为全球半导体市场主要参与者地位的关键一步。

---

## 48. Cloudflare宕机也许是件好事

**原文标题**: The Cloudflare outage might be a good thing

**原文链接**: [https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048](https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048)

这次Cloudflare中断事件虽然具有破坏性，但它也敲响了重要的警钟，提醒人们互联网日益中心化和脆弱。这次中断由一个普通的配置文件问题引发，暴露了关键服务对单一故障点的依赖程度。作者强调了这种讽刺现象，即最初为分散性和弹性而设计的互联网，已经演变成一个严重依赖Cloudflare和AWS等少数关键提供商的系统。

作者用朋友因中断而无法给轮胎充气的轶事来说明数字基础设施与日常生活的紧密联系。从银行、零售到政府服务，甚至轮胎充气，我们的社会越来越依赖互联网，一旦中心化服务出现故障，就会容易受到广泛的干扰。

文章将此事与COVID-19大流行及其对全球供应链的影响进行了比较，认为对精益高效系统的追求导致了危机期间暴露出来的漏洞。正如企业学会多元化并建立供应链缓冲一样，作者敦促组织和政府为关键服务创建冗余和离线替代方案。

作者总结说，像Cloudflare这样的中断虽然不便，但却是宝贵的警告。它们突显了依赖少数提供商的危险，并鼓励开发更具弹性、分散的系统，以便能够承受未来的中断，包括潜在的网络攻击或关键基础设施提供商内部的故障。行动呼吁是将中断视为学习机会，并主动在我们的数字基础设施中建立冗余。

---

## 49. Show HN: Datamorph – 自动检测的简洁 JSON ⇄ CSV 转换器

**原文标题**: Show HN: Datamorph – A clean JSON ⇄ CSV converter with auto-detect

**原文链接**: [https://datamorphio.vercel.app](https://datamorphio.vercel.app)

Datamorph，DatumInt 出品，是一款免费的在线工具，旨在实现 JSON 和 CSV 文件格式之间的即时、简洁转换。该工具具备自动检测功能，简化了转换过程。用户可以快速地将 JSON 文件转换为 CSV 格式，反之亦然，无需手动指定分隔符或其他格式参数。这意味着它提供了一种用户友好的体验，专注于数据转换任务的效率和可访问性。

---

## 50. Serflings是《工人物语1》的重制版。

**原文标题**: Serflings is a remake of The Settlers 1

**原文链接**: [https://www.simpleguide.net/serflings.xhtml](https://www.simpleguide.net/serflings.xhtml)

《农奴时代》是经典策略游戏《 settlers 1》（又名《农奴之城》）的重制版，旨在还原原作体验，并增加更高分辨率和网络对战等增强功能。要运行该游戏，您需要从原始《 settlers 1》游戏文件中复制特定的数据文件 (SPAE.PA, SPAD.PA, 或 SPAF.PA)，除非您已将历史典藏版安装在默认目录中。游戏将在多个位置搜索这些文件。

该重制版与游戏的 DOS 和历史典藏版游戏文件兼容。它提供所有训练、任务、AI、保存/加载（包括原始存档支持）等功能，并支持多种语言。其他功能包括平滑滚动、缩放、自动寻路、网络对战（1v1）、工作半径指示、可配置的控制、游戏速度调整和保存的任务进度。

目前，原作中缺失的功能包括替换现有建筑物、菜单/建筑物的计时器、建造路径时的滚动、消息自定义、工具提示和更高级的网络对战。

文章提供了稳定版和开发版的下载链接，均提供带和不带集成 Java 运行时 (没有集成则需要 Java 17)的版本。还有 Discord、Facebook 和 Steam 的链接，以便及时了解最新动态。您可以在 Github 上报告错误或请求功能。最新稳定版是 2.1.1 (2025 年 1 月 20 日)，最新开发版是 2.2.0-SNAPSHOT (2025 年 9 月 24 日)。

---

## 51. 内存带宽瓶颈：你的算法问题不大，数据有问题

**原文标题**: Bytes before FLOPS: your algorithm is (mostly) fine, your data isn't

**原文链接**: [https://www.bitsdraumar.is/bytes-before-flops/](https://www.bitsdraumar.is/bytes-before-flops/)

David Miličević的文章《Bytes before FLOPS》强调以数据为导向的优化是提高性能的关键。他认为，专注于高效的数据处理通常比仅仅优化算法能带来更大的改进。

文章概述了一个循序渐进的方法：

1.  **分析（Profile）：** 通过性能分析识别瓶颈，通常会揭示意想不到的问题区域。
2.  **算法特化（Specialize the Algorithm）：** 根据正在处理的特定数据定制算法，消除不必要的通用性以提高性能。
3.  **缓存友好化（Make it Cache Friendly）：** 通过访问附近或最近访问的数据来优化数据访问模式，从而提高缓存效率，包括重新排列结构成员并考虑非临时写入等技术。类型压缩有助于在缓存中保存更多数据。
4.  **SIMD化（Make it SIMD）：** 使用SIMD指令并行处理数据，实现算法的向量化。将数据重新排列成SoA或AoSoA结构。
5.  **并行化（Make it Parallel）：** 使用OpenMP或Rayon等工具并行处理独立的数据流，同时使用填充解决伪共享问题。

文章强调了理解数据流、内存访问和缓存行为的重要性。它强调优化数据布局和访问模式可以带来显著的加速，通常超过纯算法优化的好处。文章还简要讨论了不同编程语言对数据密集型任务的适用性，倾向于使用C/C++/Rust等系统语言来获得对数据布局和内存管理的最佳控制，同时也提供了性能分析和数据导向设计的资源和工具。

---

## 52. 唯一公开出售的通用EV1

**原文标题**: The only GM EV1 ever publicly sold

**原文链接**: [https://www.theautopian.com/how-the-only-gm-ev1-ever-sold-didnt-get-crushed-and-where-its-going-now/](https://www.theautopian.com/how-the-only-gm-ev1-ever-sold-didnt-get-crushed-and-where-its-going-now/)

2025年10月，布莱恩·西尔维斯特罗报道了车架号为4G5PX2250V0200212（唯一一辆公开出售的通用EV1）背后离奇的故事。这辆EV1最初于1997年出租，由于需求低迷和成本高昂，本应像大多数其他EV1一样被压碎。最初的承租人乔纳森·索耶解释说，他对通用汽车的诉讼可能使其免于被销毁。

这辆车最终被遗弃在克拉克亚特兰大大学，随后被拖走。令人惊讶的是，拖车场拍卖了这辆EV1，一位名叫比利的不愿透露姓名的电动汽车爱好者以超过11.8万美元的价格购买了它。比利计划开设一家电动汽车博物馆，目前正在对这辆EV1进行全面修复。

EV1是20世纪90年代一款具有开创性的电动汽车，由于电池的限制，主要在南方各州租赁。尽管马力较低，但它具有再生制动和空气动力学设计等创新功能。通用汽车召回并压碎了大部分EV1，仅向博物馆和大学捐赠了少数。比利的EV1是一个独特的案例，在经历了一系列法律和后勤方面的怪事后幸存了下来。

由于缺少零件，包括电池组和传动系统控制模块，修复过程将充满挑战。比利正在寻求EV1社区的帮助，并计划在2026年11月，即EV1首次行驶30周年之际，让这辆车重新运行。

---

## 53. 蛋卷：新型通用机器学习算法速度提升100倍

**原文标题**: Eggroll: Novel general-purpose machine learning algorithm provides 100x speed

**原文链接**: [https://eshyperscale.github.io/](https://eshyperscale.github.io/)

EGGROLL，即通过低秩学习的进化引导通用优化，是一种新型机器学习算法，与朴素进化策略 (ES) 相比，其训练速度提高了百倍，从而使包括 LLM 在内的大规模模型训练更具实用性。它通过实现高效的微调和从头开始训练新架构，弥合了推理和训练之间的差距。

EGGROLL 使用低秩矩阵扰动技术来降低与传统 ES 相关的计算和内存成本，从而能够有效地扩展到具有数十亿参数的模型的大种群规模。该技术降低了辅助存储和前向传递成本，从而显著提高训练吞吐量，几乎与纯批量推理的速度相匹配。

该算法的有效性通过几个实验得到证明：它在强化学习设置中与 ES 表现相当，在改进 LLM 推理方面与 GRPO 竞争，并且能够稳定地预训练纯粹基于整数数据类型运行的非线性循环语言模型（称为“EGG”）。研究人员通过在 MiniPile 数据集上训练一个 EGG 模型，取得了令人印象深刻的结果，即使移除所有激活函数也是如此，从而展示了 EGGROLL 的能力。他们还展示了它在微调 RWKV-7 语言模型以执行推理任务方面的有效性，优于 GRPO 等现有方法。

作者已经发布了代码、研究论文和纯 int8 语言模型训练的单文件实现，以鼓励社区贡献。他们正在积极努力将 EGGROLL 扩展到更大的种群规模，并探索其在其他语言模型架构和神经符号系统中的应用。

---

## 54. 展示HN：通过切换嵌入模型，我们将RAG延迟降低了约2倍

**原文标题**: Show HN: We cut RAG latency ~2× by switching embedding model

**原文链接**: [https://www.myclone.is/blog/voyage-embedding-migration/](https://www.myclone.is/blog/voyage-embedding-migration/)

MyClone通过将基于RAG的数字人平台从OpenAI的`text-embedding-3-small`（1536维）切换到Voyage-3.5-lite（512维），提高了性能和性价比。 这项变更使向量数据库存储减少了约66%，检索延迟提高了2-2.5倍，端到端语音延迟降低了15-20%。

切换的原因是大型RAG系统中高维嵌入带来的高存储和计算成本。 Voyage-3.5-lite利用Matryoshka Representation Learning (MRL)，以显著更少的维度保持了相当甚至更好的检索质量，使其成为对延迟敏感的应用的理想选择。

检索速度的提高直接增强了用户体验，尤其是在语音交互中，减少了轮次之间的“机械停顿”。 这一转变也转化为更低的的基础设施成本，使MyClone能够更有效地扩展，并将资源重新投入到更丰富的功能中。

文章强调，嵌入选择是一项关键的产品决策，像Voyage-3.5-lite这样针对检索质量、灵活维度和量化进行优化的模型，对于延迟敏感、知识密集型应用将变得越来越重要。 MyClone通过战略性地选择与RAG系统的特定需求相一致的嵌入模型，实现了更好的用户体验、更低的成本和未来的灵活性。

---

## 55. 我用 Rust 构建了一个更快的 Notion

**原文标题**: I built a faster Notion in Rust

**原文链接**: [https://imedadel.com/outcrop/](https://imedadel.com/outcrop/)

Imed 打造了 Outcrop，一个用 Rust 编写的更快 Notion 替代方案，源于对现有知识库解决方案的 frustレーション。 受 Stripe 内部知识库成功案例的启发，并意识到 Atlassian 即将停止 Data Center 服务的时机，Imed 旨在提供速度和简洁性。

最初 Imed 使用 Go 进行原型设计，但遇到了大量的样板代码，因此切换到了 Rust。 Rust 的宏 crate 减少了代码量，解决了实时协作、搜索延迟和访问控制等挑战。 一项关键创新是受 Zanzibar 启发的轻量级内存授权系统，该系统持久化到 Postgres，可提供快速的权限检查。 搜索引擎利用 tantivy，并结合 whatlang 进行语言检测，确保只考虑可访问的资源。

协作通过 Rust 版本的 prosemirror 自定义端口进行处理，提高了文档编辑应用程序的速度。 这使得能够有效地提取文本、链接和提及，为诸如标签补全和由语言模型驱动的结构化建议等功能铺平道路。 Solid.js 与 prosemirror 集成，用于编辑器的 UI。

Imed 设想 Outcrop 不仅仅局限于散文，还包括图表、绘图和电子表格，重点是结构化工作流程以及与任务管理工具的集成。 该产品预计在六个月内发布，定价约为每个席位 10 美元，并提供赞助选项。

---

## 56. 台积电亚利桑那州停电致工厂停产，苹果晶圆报废

**原文标题**: TSMC Arizona outage saw fab halt, Apple wafers scrapped

**原文链接**: [https://www.culpium.com/p/tsmc-arizona-outage-saw-fab-halt](https://www.culpium.com/p/tsmc-arizona-outage-saw-fab-halt)

2025年9月下旬，台积电主要供应商林德工业气体公司的一家工厂发生断电事故，导致台积电位于亚利桑那州的Fab 21工厂停产。此次停电迫使该公司报废了数千片正在为苹果、英伟达和AMD等主要客户生产的晶圆。虽然台积电通常在台湾自行处理气体供应，但在亚利桑那州，它将这一功能外包。

该事件影响了台积电第三季度的盈利能力，导致净利润大幅下降，不过该公司表示海外工厂的整体爬坡成本也是一个因素。虽然台积电拒绝直接评论此次断电事故，但他们承认多种因素对利润产生了影响。

预计此次事件对台积电造成的财务影响将部分由保险承担，并且由于Fab 21的产能相对较小以及许多产品此前已在台湾生产，因此对客户的影响被认为是微乎其微的。台积电正在与林德公司解决该问题，并强调海外工厂需要进行运营改进。

该事件凸显了台湾制造商在海外工厂依赖非台湾公司时面临的挑战，并强调了可靠供应链的重要性。这并非首次因供应商问题导致停产，过去曾因污染和计算机病毒导致生产延误。

---

## 57. 陶哲轩：在埃尔德什问题网站，AI辅助正成为常态

**原文标题**: Terence Tao: At the Erdos problem website, AI assistance now becoming routine

**原文链接**: [https://mathstodon.xyz/@tao/115591487350860999](https://mathstodon.xyz/@tao/115591487350860999)

基于陶哲轩 Mastodon 帖文：AI 助力解决数学问题趋势渐显，Erdos 问题网站可见一斑。

---

## 58. 发布HN：Karumi (YC F25) – 个性化、代理式产品演示

**原文标题**: Launch HN: Karumi (YC F25) – Personalized, agentic product demos

**原文链接**: [http://karumi.ai/](http://karumi.ai/)

Karumi AI (YC F25)：提供全天候个性化智能产品演示，旨在兴趣最高时促成交易。该平台提供根据客户需求和背景定制的高度个性化演示，确保信息始终最新。Karumi的多语种AI代理扩大了覆盖范围，所有互动都会记录到CRM中以供后续跟进。

Karumi的解决方案旨在改善连接、演示交付和转化率，通过着陆页、应用内集成和外发邮件提供按需访问。优势包括更快的“顿悟”时刻和可扩展的个性化，无需增加员工人数。客户评价强调了该平台捕获更多潜在客户和加强销售渠道的能力。

Karumi的应用场景包括筛选潜在客户、运行定制演示、提供个性化入职培训，以及通过回答问题和展示产品特性来提供支持。该公司强调易于实施，并旨在将错失的 inbound 流量转化为预订演示和转化。Karumi符合SOC 2标准，并致力于数据安全和隐私。

---

## 59. 切片足矣：迈向通用的单边分布式矩阵乘法

**原文标题**: Slicing Is All You Need: Towards a Universal One-Sided Distributed MatMul

**原文链接**: [https://arxiv.org/abs/2510.08874](https://arxiv.org/abs/2510.08874)

题为“切片即万物：迈向通用单边分布式矩阵乘法算法”的论文提出了一种新的分布式矩阵乘法方法，旨在克服现有算法的局限性。作者 Benjamin Brock 和 Renato Golin 提出了一种通用单边算法，能够支持任意分区方案和复制因子的组合。

核心思想围绕使用“切片”（索引算术）来确定需要相乘的重叠块。这会生成一个本地矩阵乘法列表，然后可以直接执行该列表，或者通过中间表示 (IR) 进行优化以最大化重叠。该算法使用基于 C++ 的高级 PGAS 编程框架实现，从而可以使用节点内互连促进直接的 GPU 到 GPU 通信。

该算法的关键优势在于其通用性，无需为不同的分区策略实现多个算法，并避免了代价高昂的数据重新分发。作者展示了该算法在各种分区和复制因子下的性能，表明它与 PyTorch DTensor（一种用于 AI 模型的高度优化的分布式张量库）具有竞争力。该论文认为，这种基于切片的方法为分布式矩阵乘法提供了一种灵活高效的解决方案，适用于各种科学、数据分析和 AI 工作负载。

---

## 60. 旅行者1号逼近距离地球一日光程

**原文标题**: Voyager 1 approaches one light day from Earth

**原文链接**: [https://newatlas.com/space/voyager-approaches-1-light-day-from-earth/](https://newatlas.com/space/voyager-approaches-1-light-day-from-earth/)

2026年11月，“旅行者1号”将达成一个重要里程碑：成为首个距离地球一个光天的航天器，这意味着无线电信号到达它需要24小时。“旅行者1号”于1977年发射，在最初飞越木星和土星后，已经远航至太阳系之外。目前，它距离地球约157亿英里，单向信息到达该探测器大约需要23小时32分钟。

这篇文章强调了深空旅行中固有的通信延迟不断增加，将我们在地球上体验到的近乎瞬时的通信与阿波罗登月任务（2.6秒）和火星任务（最多四分钟）遇到的延迟进行了对比。这些延迟使得机器人航天器必须具备高度的自主性。

尽管由于核动力源逐渐减少，“旅行者1号”已接近其运行寿命的尽头，但它仍在继续工作。尽管在如此遥远的距离进行通信面临挑战，但美国宇航局的深空网络仍与“旅行者1号”及其姊妹探测器“旅行者2号”（目前距离19.5光时）保持联系。“旅行者1号”即将迎来一个光天的里程碑，这将要求美国宇航局的工程师们保持耐心，因为指令需要整整两天才能得到这个遥远探测器的确认。

---

## 61. 海龟如何利用地球磁场学习定位：研究

**原文标题**: How sea turtles learn locations using Earth’s magnetic field: research

**原文链接**: [https://uncnews.unc.edu/2025/02/13/sea-turtles-secret-gps-researchers-uncover-how-sea-turtles-learn-locations-using-earths-magnetic-field/](https://uncnews.unc.edu/2025/02/13/sea-turtles-secret-gps-researchers-uncover-how-sea-turtles-learn-locations-using-earths-magnetic-field/)

北卡罗来纳大学教堂山分校的研究人员在了解海龟如何学习和利用地球磁场进行导航方面取得了重大进展。这项发表在《当代生物学》上的研究表明，幼年海龟会学习重要位置的磁场特征。这对于它们成年后返回特定筑巢海滩的能力至关重要，有时需要迁徙数千英里。

该研究包括在受控环境中将幼年海龟暴露于不同的磁场，并观察它们的游泳行为。研究人员发现，海龟并非仅仅本能地对特定磁场做出反应，而是学会将某些磁场特征与理想的位置联系起来。这种学习过程很可能发生在它们生命早期，当它们探索沿海栖息地时。

主要发现包括：

*   海龟学习特定位置的磁场特征，而不是仅仅本能地对它们做出反应。
*   这种学习很可能发生在幼年海龟在沿海栖息地的“迷失之年”阶段。
*   磁场特征与位置之间的这种学习关联对于它们导航回筑巢海滩的能力至关重要。

这项研究为海龟复杂的导航能力提供了宝贵的见解，并强调了沿海栖息地对其发展的重要性。了解这种学习机制对于制定有效的保护策略至关重要，尤其是在面对不断变化的磁场和栖息地退化的情况下。

---

## 62. 波兰反垄断监管机构调查苹果隐私政策

**原文标题**: Polish antitrust watchdog investigates Apple over privacy policy

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/polish-antitrust-watchdog-investigates-apple-over-privacy-policy-2025-11-25/](https://www.reuters.com/sustainability/boards-policy-regulation/polish-antitrust-watchdog-investigates-apple-over-privacy-policy-2025-11-25/)

无法访问文章链接。

---

## 63. 你可以在IBM伦敦办公室看到一台正在运行的量子计算机。

**原文标题**: You can see a working Quantum Computer in IBM's London office

**原文链接**: [https://www.ianvisits.co.uk/articles/you-can-see-a-working-quantum-computer-in-ibms-london-office-85464/](https://www.ianvisits.co.uk/articles/you-can-see-a-working-quantum-computer-in-ibms-london-office-85464/)

IBM在伦敦滑铁卢办公室安装了一台可用的量子计算机，即IBM Quantum System One，令人惊讶地展示了未来科技。 这台基于电路的量子计算机于2019年推出，利用量子物理原理，通过使用可以同时为1和0的量子比特，使其计算速度比传统计算机快指数倍。

虽然不太可能成为家用物品，但量子计算机有潜力取代传统超级计算机来处理复杂计算。 挑战在于它们的构建，需要极低的温度来维持脆弱的量子态。 这就需要一个蒸汽朋克式的冷却系统。

目前该计算机正被公司使用，公众可以通过约克路滑铁卢车站附近的办公室窗口看到它。 虽然内部访问受到限制，但观察者可以从外部见证超级计算的未来。 这一引人注目的展示是由伦敦的Map Project Office和Universal Design Studio与米兰制造商Goppion合作创建的，后者以高端博物馆展柜而闻名。 本文强调了这项尖端技术的可及性，让公众可以亲身体验量子计算的力量和潜力。

---

## 64. 20亿美元反恐精英2崩溃事件暴露了法律漏洞

**原文标题**: $2B Counter-Strike 2 crash exposes a legal black hole

**原文链接**: [https://theconversation.com/2b-counter-strike-2-crash-exposes-a-legal-black-hole-your-digital-investments-arent-really-yours-268749](https://theconversation.com/2b-counter-strike-2-crash-exposes-a-legal-black-hole-your-digital-investments-arent-really-yours-268749)

João Marinotti的文章剖析了因Valve单方面修改“交易升级合同”规则而引发的《反恐精英2》数字市场20亿美元的崩盘。这一变动导致稀有物品涌入市场，大幅降低了现有皮肤的价值。Marinotti认为，该事件突显了一个法律盲点：数字经济主要受私人服务条款协议管辖，缺乏传统金融市场那样健全的监管。

核心问题是玩家在法律上并不拥有他们的“皮肤”，而只是对其进行许可。美国法院已经确认了这一区别，这意味着Valve可以在不侵犯财产权的情况下更改许可条款，使玩家对其经济损失无从追索。现有的消费者保护法不足以解决问题，因为它们侧重于许可的透明度，而不是保护数字物品的投机价值。

Marinotti进一步指出，《反恐精英2》的经济表现出金融市场的特征，但却规避了监管。他应用了豪威测试来判断证券，认为皮肤有可能符合证券的定义，因为涉及资金投入、共同企业、盈利预期以及对Valve管理努力的依赖。然而，皮肤的消费意图、缺乏平台内的现金转换以及Valve的许可计划目前规避了证券监管。作者总结道，随着数字经济的扩张，社会需要考虑将它们纳入更强大的法律框架，以保护投资者和消费者。

---

## 65. 用C11编写并使用SIMD加速的快速EDN (可扩展数据表示) 读取器

**原文标题**: A fast EDN (Extensible Data Notation) reader written in C11 with SIMD boost

**原文链接**: [https://github.com/DotFox/edn.c](https://github.com/DotFox/edn.c)

本文档介绍`EDN.C`，这是一个用C11编写的快速、零拷贝EDN（可扩展数据符号）读取器库，并使用SIMD加速（NEON、SSE4.2、SIMD128）。EDN被描述为“具有超能力的JSON”，提供更具表现力的类型（关键字、符号、集合），并通过标记文字实现可扩展性。

该库具有以下特性：SIMD带来的高性能、WebAssembly支持、最小分配（零拷贝）、简单的API、通过arena分配器实现的内存安全、零依赖（纯C11）、全面的测试、UTF-8原生支持，以及对标记文字、映射命名空间语法、扩展字符文字、元数据、文本块、比例数、扩展整数格式和数字文字中的下划线等的可选支持。

本文档提供了安装（Unix/macOS/Linux、Windows）和集成到项目中的说明，包括链接静态库或直接包含源文件。一个快速入门示例演示了基本用法，包括解析EDN字符串、访问映射条目和释放内存。它详细说明了如何处理空格和控制字符。

API参考部分涵盖了核心函数，例如 `edn_read()`（从字符串读取EDN）、`edn_free()`（释放内存）和 `edn_type()`（获取EDN值的类型）。它还描述了用于访问特定数据类型的函数，例如字符串、布尔值、整数、大整数、浮点数、大十进制数和（可选）比例数。

---

## 66. Fran Sans – 灵感源自旧金山轻轨显示的字体

**原文标题**: Fran Sans – font inspired by San Francisco light rail displays

**原文链接**: [https://emilysneddon.com/fran-sans-essay](https://emilysneddon.com/fran-sans-essay)

艾米丽·斯内登的文章详细介绍了“Fran Sans”字体的创作，这是一款受旧金山Muni Breda轻轨车辆上的LCD目的地显示器启发的展示字体。她被这些显示器的机械感与个性化感觉所吸引，其特点是由几何模块构成的不完美的字母，具有独特的魅力。

斯内登参观了SFMTA的电子商店，技术员Armando Lumbad解释了这些标志的工作原理，并透露它们是由Trans-Lite, Inc.于1999年设计的。她联系了负责这些标志的工程师Gary Wallberg，他确认这些标志的设计是为了满足需求，字符仅在需要时才创建。这激发了斯内登创作Fran Sans的灵感，捕捉了这种实用主义排版的精髓。

在Dave Foster的鼓励下，斯内登在Glyphs中开发了这款字体，使用模块构建大写字母、数字和标点符号。她承认有些字形仍然未解决，小写字母是未来需要考虑的问题。Fran Sans有三种样式：Solid、Tile和Panel，灵感来自Bell Shakespeare的可适应字体。

斯内登还感谢Letterform Archive启发了她的模块化方法，并特别提到了Joan Trochut的Tipo Veloz和Zuzana Licko的Lo-Res。

随着Breda车辆的更换及其显示器的逐步淘汰，斯内登希望Fran Sans能够保留旧金山独特的一部分特征，并激发人们对不完美的欣赏。她还感谢许多在Fran Sans创作过程中帮助过她的人，包括SFMTA员工、Trans-Lite的设计师以及她的设计同行。文章最后附有Maddy Carrucan的一首诗。

---

## 67. GrapheneOS 将服务器基础设施从法国迁移。

**原文标题**: GrapheneOS migrates server infrastructure from France

**原文链接**: [https://www.privacyguides.org/news/2025/11/22/grapheneos-migrates-server-infrastructure-from-france-amid-police-intimidation-claims/](https://www.privacyguides.org/news/2025/11/22/grapheneos-migrates-server-infrastructure-from-france-amid-police-intimidation-claims/)

GrapheneOS，一个注重隐私的操作系统，正将其服务器基础设施迁出法国，理由是开源隐私项目的安全担忧。该项目正在将其网站、Mastodon、Discourse和Matrix服务器迁移到多伦多和德国，特别是Netcup。此决定是由法国政府对欧盟聊天控制提案的支持以及《巴黎人报》的负面报道所引发的，GrapheneOS认为该报道将他们的项目与政府赞助的恶意分支混为一谈。

由于这些担忧，开发者们也拒绝前往法国。虽然此次迁移不会影响签名验证等关键安全服务，但GrapheneOS认为法国不再是他们运营的安全地点。《巴黎人报》的文章提到了隐私工具与犯罪组织之间的联系，暗示可能对不合作的发布者采取法律行动，即使这些工具是合法的。GrapheneOS认为他们被错误地描述，并与用于非法活动的操作系统伪造版本联系起来，例如ANOM案例，其中联邦调查局使用受损的Android操作系统进行“特洛伊木马行动”。

---

## 68. Random lasers from peanut kernel doped with birch leaf–derived carbon dots

**原文标题**: Random lasers from peanut kernel doped with birch leaf–derived carbon dots

**原文链接**: [https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2025-0312/html](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2025-0312/html)

生成摘要时出错

---

## 69. What you can get for the price of a Netflix subscription

**原文标题**: What you can get for the price of a Netflix subscription

**原文链接**: [https://nmil.dev/what-you-can-get-for-the-price-of-a-netflix-subscription](https://nmil.dev/what-you-can-get-for-the-price-of-a-netflix-subscription)

生成摘要时出错

---

## 70. Set theory with types

**原文标题**: Set theory with types

**原文链接**: [https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html](https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html)

生成摘要时出错

---

## 71. General principles for the use of AI at CERN

**原文标题**: General principles for the use of AI at CERN

**原文链接**: [https://home.web.cern.ch/news/official-news/knowledge-sharing/general-principles-use-ai-cern](https://home.web.cern.ch/news/official-news/knowledge-sharing/general-principles-use-ai-cern)

生成摘要时出错

---

## 72. Show HN: Search London StreetView panoramas by text

**原文标题**: Show HN: Search London StreetView panoramas by text

**原文链接**: [https://london.publicinsights.uk](https://london.publicinsights.uk)

生成摘要时出错

---

## 73. Show HN: Cynthia – Reliably play MIDI music files – MIT / Portable / Windows

**原文标题**: Show HN: Cynthia – Reliably play MIDI music files – MIT / Portable / Windows

**原文链接**: [https://www.blaizenterprises.com/cynthia.html](https://www.blaizenterprises.com/cynthia.html)

生成摘要时出错

---

## 74. Ego, empathy, and humility at work

**原文标题**: Ego, empathy, and humility at work

**原文链接**: [https://matthogg.fyi/a-unified-theory-of-ego-empathy-and-humility-at-work/](https://matthogg.fyi/a-unified-theory-of-ego-empathy-and-humility-at-work/)

生成摘要时出错

---

## 75. Historically Accurate Airport Dioramas by AV Pro Designs

**原文标题**: Historically Accurate Airport Dioramas by AV Pro Designs

**原文链接**: [https://www.core77.com/posts/138995/Historically-Accurate-Airport-Dioramas-by-AV-Pro-Designs](https://www.core77.com/posts/138995/Historically-Accurate-Airport-Dioramas-by-AV-Pro-Designs)

生成摘要时出错

---

## 76. Everything you need to know about hard drive vibration (2016)

**原文标题**: Everything you need to know about hard drive vibration (2016)

**原文链接**: [https://www.ept.ca/features/everything-need-know-hard-drive-vibration/](https://www.ept.ca/features/everything-need-know-hard-drive-vibration/)

生成摘要时出错

---

## 77. NSA and IETF, part 3: Dodging the issues at hand

**原文标题**: NSA and IETF, part 3: Dodging the issues at hand

**原文链接**: [https://blog.cr.yp.to/20251123-dodging.html](https://blog.cr.yp.to/20251123-dodging.html)

生成摘要时出错

---

## 78. Lambda Calculus – Animated Beta Reduction of Lambda Diagrams

**原文标题**: Lambda Calculus – Animated Beta Reduction of Lambda Diagrams

**原文链接**: [https://cruzgodar.com/applets/lambda-calculus](https://cruzgodar.com/applets/lambda-calculus)

生成摘要时出错

---

## 79. Trump's FCC: Internet Providers Can Monitor Their Own Cybersecurity Standards

**原文标题**: Trump's FCC: Internet Providers Can Monitor Their Own Cybersecurity Standards

**原文链接**: [https://www.cnet.com/home/internet/internet-providers-can-monitor-their-own-cybersecurity-standards-says-trumps-fcc/](https://www.cnet.com/home/internet/internet-providers-can-monitor-their-own-cybersecurity-standards-says-trumps-fcc/)

生成摘要时出错

---

## 80. We stopped roadmap work for a week and fixed bugs

**原文标题**: We stopped roadmap work for a week and fixed bugs

**原文链接**: [https://lalitm.com/fixits-are-good-for-the-soul/](https://lalitm.com/fixits-are-good-for-the-soul/)

生成摘要时出错

---

## 81. PRC Elites Voice AI-Skepticism

**原文标题**: PRC Elites Voice AI-Skepticism

**原文链接**: [https://jamestown.org/prc-elites-voice-ai-skepticism/](https://jamestown.org/prc-elites-voice-ai-skepticism/)

生成摘要时出错

---

## 82. Roblox is a problem – but it's a symptom of something worse

**原文标题**: Roblox is a problem – but it's a symptom of something worse

**原文链接**: [https://www.platformer.news/roblox-ceo-interview-backlash-analysis/](https://www.platformer.news/roblox-ceo-interview-backlash-analysis/)

生成摘要时出错

---

## 83. An Economy of AI Agents

**原文标题**: An Economy of AI Agents

**原文链接**: [https://arxiv.org/abs/2509.01063](https://arxiv.org/abs/2509.01063)

生成摘要时出错

---

## 84. Show HN: Stun LLMs with thousands of invisible Unicode characters

**原文标题**: Show HN: Stun LLMs with thousands of invisible Unicode characters

**原文链接**: [https://gibberifier.com](https://gibberifier.com)

生成摘要时出错

---

## 85. µcad: New open source programming language that can generate 2D sketches and 3D

**原文标题**: µcad: New open source programming language that can generate 2D sketches and 3D

**原文链接**: [https://microcad.xyz/](https://microcad.xyz/)

生成摘要时出错

---

## 86. RuBee

**原文标题**: RuBee

**原文链接**: [https://computer.rip/2025-11-22-RuBee.html](https://computer.rip/2025-11-22-RuBee.html)

生成摘要时出错

---

## 87. Show HN: I wrote a minimal memory allocator in C

**原文标题**: Show HN: I wrote a minimal memory allocator in C

**原文链接**: [https://github.com/t9nzin/memory](https://github.com/t9nzin/memory)

生成摘要时出错

---

## 88. Build desktop applications using Go and Web Technologies

**原文标题**: Build desktop applications using Go and Web Technologies

**原文链接**: [https://github.com/wailsapp/wails](https://github.com/wailsapp/wails)

生成摘要时出错

---

## 89. The Arithmetic of Braids (2022)

**原文标题**: The Arithmetic of Braids (2022)

**原文链接**: [https://mathcenter.oxford.emory.edu/site/math108/braid_arithmetic/](https://mathcenter.oxford.emory.edu/site/math108/braid_arithmetic/)

生成摘要时出错

---

## 90. Historic Engineering Wonders: Photos That Reveal How They Pulled It Off

**原文标题**: Historic Engineering Wonders: Photos That Reveal How They Pulled It Off

**原文链接**: [https://rarehistoricalphotos.com/engineering-methods-from-the-past/](https://rarehistoricalphotos.com/engineering-methods-from-the-past/)

生成摘要时出错

---

## 91. Mount Proton Drive on Linux using rclone and systemd

**原文标题**: Mount Proton Drive on Linux using rclone and systemd

**原文链接**: [https://github.com/dadtronics/protondrive-linux](https://github.com/dadtronics/protondrive-linux)

生成摘要时出错

---

## 92. A time-travelling door bug in Half Life 2

**原文标题**: A time-travelling door bug in Half Life 2

**原文链接**: [https://mastodon.gamedev.place/@TomF/115589875974658415](https://mastodon.gamedev.place/@TomF/115589875974658415)

生成摘要时出错

---

## 93. Show HN: Hypercamera – a browser-based 4D camera simulator

**原文标题**: Show HN: Hypercamera – a browser-based 4D camera simulator

**原文链接**: [https://dugas.ch/4d_creatures/4d_camera.html](https://dugas.ch/4d_creatures/4d_camera.html)

生成摘要时出错

---

## 94. Microsoft doesn't understand the dislike for Windows' new direction

**原文标题**: Microsoft doesn't understand the dislike for Windows' new direction

**原文链接**: [https://www.xda-developers.com/microsoft-doesnt-understand-dislike-windows-new-direction/](https://www.xda-developers.com/microsoft-doesnt-understand-dislike-windows-new-direction/)

生成摘要时出错

---

## 95. Native Secure Enclave backed SSH keys on macOS

**原文标题**: Native Secure Enclave backed SSH keys on macOS

**原文链接**: [https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf](https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf)

生成摘要时出错

---

## 96. McMaster Carr – The Smartest Website You Haven't Heard Of (2022)

**原文标题**: McMaster Carr – The Smartest Website You Haven't Heard Of (2022)

**原文链接**: [https://www.bedelstein.com/post/mcmaster-carr](https://www.bedelstein.com/post/mcmaster-carr)

生成摘要时出错

---

## 97. Chatbot Psychosis

**原文标题**: Chatbot Psychosis

**原文链接**: [https://en.wikipedia.org/wiki/Chatbot_psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis)

生成摘要时出错

---

## 98. Editing Code in Emacs

**原文标题**: Editing Code in Emacs

**原文链接**: [https://redpenguin101.github.io/html/posts/2025_11_23_emacs_for_code_editing.html](https://redpenguin101.github.io/html/posts/2025_11_23_emacs_for_code_editing.html)

生成摘要时出错

---

## 99. Is your Android TV streaming box part of a botnet?

**原文标题**: Is your Android TV streaming box part of a botnet?

**原文链接**: [https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/](https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/)

生成摘要时出错

---

## 100. Iowa City made its buses free. Traffic cleared, and so did the air

**原文标题**: Iowa City made its buses free. Traffic cleared, and so did the air

**原文链接**: [https://www.nytimes.com/2025/11/18/climate/iowa-city-free-buses.html](https://www.nytimes.com/2025/11/18/climate/iowa-city-free-buses.html)

生成摘要时出错

---

