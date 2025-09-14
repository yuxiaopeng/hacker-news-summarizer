# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-14.md)

*最后自动更新时间: 2025-09-14 17:43:16*
## 1. 泰国央行冻结300万账户，设定每日转账限额以遏制诈骗

**原文标题**: Bank of Thailand Freezes 3MM Accounts, Sets Daily Transfer Limits to Curb Fraud

**原文链接**: [https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/](https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/)

泰国银行冻结了与诈骗活动相关的300万个银行账户，并实施了更严格的每日交易限额，以打击激增的诈骗活动，这些活动已使泰国人损失估计达60亿泰铢。新的每日转账限额设定在5万至20万泰铢之间，远低于之前的限额。

此举旨在扰乱诈骗分子的运作，并减少对受害者的潜在经济损失。泰国银行的行动是在公众压力日益增加以及政府为解决日益严重的网络诈骗问题采取行动之后进行的。这些被冻结的账户涉嫌被用作通过各种诈骗获得的非法资金的中转点。

虽然降低转账限额的目的是保护消费者，但人们担心这可能会给经常进行较大交易的合法用户带来不便。预计泰国银行将提供进一步的指导和支持，以确保真正的交易不会受到不当影响。这项举措是泰国银行和泰国当局为加强网络安全和提高公众对网络诈骗的认识而做出的更广泛努力的一部分。

---

## 2. 从零开始编写操作系统内核

**原文标题**: Writing an operating system kernel from scratch

**原文链接**: [https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/](https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/)

本文详细介绍了使用 Zig 语言为 RISC-V 架构编写一个极简的时间片操作系统内核的过程。它面向那些旨在了解底层系统软件、驱动程序和系统调用的个人。作者重新审视了一个操作系统项目，重点关注现代工具以及以其可理解性和普及性而闻名的 RISC-V 架构。

该内核设计为 unikernel，将应用程序代码直接与 OS 内核链接，从而简化了用户代码加载。它利用 RISC-V 分层权限模型（M、S 和 U 模式），并利用 OpenSBI 进行控制台打印和计时器控制，绕过手动实现以提高可移植性。

该内核旨在支持在用户模式（U-mode）下运行的静态定义的、永不终止的线程，这些线程能够向内核（S-mode）发送系统调用。时间片轮转通过计时器中断实现，用于在单核机器上进行上下文切换。

核心概念涉及虚拟化内核，使得每个线程“感觉”好像拥有一个虚拟内核。这是通过提供相同的编程模型来实现的，但每个线程只能访问其自身的堆栈和架构寄存器，而内存是共享的。

该实现利用中断处理机制在线程之间进行切换。它通过使用中断例程将堆栈指针交换到不同的内存块来实现，从而恢复不同的架构寄存器值，从而实现上下文切换。

---

## 3. 欧洲地铁站模型

**原文标题**: Models of European Metro Stations

**原文链接**: [http://stations.albertguillaumes.cat/](http://stations.albertguillaumes.cat/)

本文概述了欧洲各城市以及布宜诺斯艾利斯和波士顿的地铁和快速 transit 系统，重点介绍了车站布局、换乘设计和历史背景。

它详细介绍了每个城市系统的具体特征。例如，阿利坎特的 TRAM 拥有带夹层和侧式站台的地下线路，而阿姆斯特丹的地铁则包括地下和地上部分。安特卫普的 premetro 连接着城市的各个部分，在换乘枢纽处有复杂的车站布局。巴塞罗那以其长长的换乘通道和“西班牙式解决方案”站台设计而闻名。柏林的 U-Bahn 通常位于地下，而 S-Bahn 位于地上，具有简单的换乘拓扑结构。

本文还介绍了独特的方面，例如波士顿由于早期施工方法而产生的不同寻常的市中心车站，以及布鲁塞尔计划从 premetro 过渡到完整地铁线路的系统。布达佩斯的地铁是欧洲大陆最古老的地铁，拥有狭窄的隧道，而布加勒斯特的系统则采用明挖回填法建造。

本文重点介绍了建设过程中面临的挑战，例如巴塞罗那的地铁扩建滞后于城市发展，以及适应城市地形，例如在毕尔巴鄂。文章还介绍了现代系统，如哥本哈根的自动地铁和汉诺威的 Stadtbahn。

---

## 4. 我们盘旋

**原文标题**: We Spiral

**原文链接**: [https://behavioralscientist.org/why-we-spiral/](https://behavioralscientist.org/why-we-spiral/)

我们螺旋式下降：探讨自我破坏性螺旋，解释看似微小的事件如何触发负面思维模式并导致不利的结果。文章以一名初级员工Zoom会议迟到，并将老板的评论解读为讽刺为例，说明了如何引发一连串的怀疑和悲观推断。

文章将这种螺旋式下降分解为三个关键组成部分，即“三个C”：**核心问题**、**构建**和**固化**。核心问题与身份、归属感和能力有关，当这些问题未解决时，会像透镜一样影响我们对世界的解读。构建是解释事件的过程，我们容易受到证实偏差的影响，寻求支持我们预先存在的信念的证据。固化是指消极的想法和感受变得根深蒂固，往往导致自我破坏行为。

作者强调，这些消极的螺旋式下降并非不可避免，并提倡“明智干预”——采取积极措施来中断这些模式。通过理解潜在的核心问题并提供替代性的、积极的视角，我们可以转向向上螺旋，从而促进幸福、成功和福祉。作者最后分享了一个关于在大学活动中感到被排斥的个人轶事，突出了看似微不足道的经历如何引发更深层次的不安全感，以及认识和解决这些潜在焦虑的重要性。

---

## 5. Observable Notebooks 数据加载器

**原文标题**: Observable Notebooks Data Loaders

**原文链接**: [https://observablehq.com/notebook-kit/data-loaders](https://observablehq.com/notebook-kit/data-loaders)

Observable Notebooks 数据加载器是特殊的单元格，它们在构建时使用解释器（Node.js 或 Python）执行，而不是在浏览器中实时运行。它们对于预处理静态数据、确保一致性、稳定性和提高性能非常有用，可以看作是数据库连接器的推广。

目前支持 Node.js 和 Python，并计划支持更多解释器。数据加载器支持多种输出格式，包括文本、JSON、CSV、XML、Arrow、Parquet、Blob、Buffer、图像（JPEG、GIF、WebP、PNG、SVG）和服务器端渲染的 HTML。

数据加载器单元格的输出缓存在笔记本旁边的 `.observable/cache` 目录中，仅在重新运行单元格时更新。在 Observable Desktop 中，重新运行通过“播放”按钮或 Shift-Return 完成。在 Notebook Kit 中，从缓存中删除文件，或通过持续部署自动刷新。

Node.js 数据加载器需要安装在特定位置的 Node.js 22.12+，并支持 TypeScript（有局限性）。通过限制文件访问到笔记本的目录来强制执行安全性。安装的软件包必须位于同一目录中。

Python 数据加载器需要安装在特定位置的 Python 3.12+，如果存在虚拟环境（.venv），则自动使用。软件包安装通过 pip 手动进行，建议使用 `pip freeze` 生成 `requirements.txt` 文件。

---

## 6. GrapheneOS 简介

**原文标题**: Introduction to GrapheneOS

**原文链接**: [https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html](https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html)

本文介绍了GrapheneOS (GOS)，一个注重安全的Android操作系统，专为Google Pixel设备设计。GOS通过使用配置文件来优先考虑用户控制和隐私。每个配置文件都像一个独立的手机实例，彼此隔离，具有单独的加密和权限设置。用户可以为每个配置文件定制权限，包括网络访问和联系人访问。

作者强调了通过Web界面安装的便捷性和无缝的OTA更新，这比他们在LineageOS上的体验有了显著的改进。一个关键特性是细粒度的权限管理，允许用户定义存储和联系人访问的范围，以及Google Play服务的沙盒化。

作者详细介绍了他们的个人工作流程，为各种活动（如工作、多媒体、游戏和不受信任的应用）使用单独的配置文件。这种方法隔离了数据并限制了后台活动。Pixel 8a的OLED屏幕、Wi-Fi 6和电池续航能力受到称赞，但缺少SD卡支持也被指出。

与原生Android相比，GrapheneOS提供了广泛的安全增强功能，尽管没有root权限。作者总结说，GOS为智能手机用户提供了前所未有的控制和安全性，但也承认它可能不会吸引所有对当前操作系统感到满意的人。文章建议探索Android内置的配置文件功能，虽然安全性较低，但可能提供有限的隔离。

---

## 7. 环保署试图取消关键的全氟/多氟烷基物质饮用水保护措施

**原文标题**: EPA Seeks to Eliminate Critical PFAS Drinking Water Protections

**原文链接**: [https://earthjustice.org/press/2025/epa-seeks-to-roll-back-pfas-drinking-water-rules-keeping-millions-exposed-to-toxic-forever-chemicals-in-tap-water](https://earthjustice.org/press/2025/epa-seeks-to-roll-back-pfas-drinking-water-rules-keeping-millions-exposed-to-toxic-forever-chemicals-in-tap-water)

2025年9月12日的一篇“地球正义”文章报道，环保署正试图取消对饮用水中PFAS“永久化学品”的关键保护措施。环保署要求联邦法院推翻去年实施的法律保护措施，特别是针对GenX、PFHxS、PFNA和PFBS的监管规定。他们还试图延长PFOA和PFOS标准的合规期限。

“地球正义”组织和其他环保团体，如NRDC，批评这一举动，认为它将行业利润置于公众健康之上，并试图规避《安全饮用水法》的反滑坡条款，该条款旨在防止削弱现有的水质标准。他们声称，环保署署长泽尔丁违背了他保护美国人免受PFAS污染的承诺。

文章强调，PFAS广泛存在，污染了美国约2亿人的饮用水，并与包括癌症和荷尔蒙紊乱在内的多种健康问题有关。“地球正义”组织代表多个社区团体，正在介入，以在法庭上捍卫当前的标准，对抗来自化学公司和自来水公司的挑战。最初的规则于2024年4月最终确定，对六种PFAS化学品设定了限制，并要求供水系统在2029年4月之前监测和报告其合规情况。

---

## 8. 福岛昆虫认知测试

**原文标题**: Fukushima Insects Tested for Cognition

**原文链接**: [https://news.cnrs.fr/articles/fukushima-insects-tested-for-cognition](https://news.cnrs.fr/articles/fukushima-insects-tested-for-cognition)

科学家正在研究福岛灾难的放射性对授粉昆虫，特别是蜜蜂和巨型大黄蜂认知能力的影响。研究人员奥利维尔·阿尔芒和马修·利奥罗正在合作，以了解电离辐射如何影响这些昆虫的学习和记忆。

利奥罗的团队开发了一种自动化系统，包括一个带有彩色LED灯的Y形迷宫，用于测试蜜蜂的认知能力。蜜蜂学会将特定颜色与糖水奖励联系起来。该系统使用二维码单独追踪每只蜜蜂，并实时分析它们的学习过程。对于体型过大无法使用自动化迷宫的巨型大黄蜂，则进行手动测试。

该研究正在福岛周围的污染区域进行，该区域因铯-137土壤污染梯度而被选中。该团队与福岛大学的环境放射性研究所合作，以获得访问权限和专业知识。

初步结果表明，在污染区域昆虫的认知能力有所下降。虽然尚未明确建立与放射性污染的直接因果关系，但研究人员认为这可能是一个因素，因为在无人居住的区域内没有其他常见的污染物（如农药）。这项研究旨在了解辐射暴露对授粉媒介和生态系统更广泛的生态影响。

---

## 9. CorentinJ：实时语音克隆 (2021)

**原文标题**: CorentinJ: Real-Time Voice Cloning (2021)

**原文链接**: [https://github.com/CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)

CorentinJ的仓库提供了一个基于迁移学习的实时语音克隆实现，该实现将说话人验证迁移到多说话人文本到语音合成（SV2TTS）。这个项目源于作者的硕士论文，允许用户使用三阶段深度学习框架实时克隆语音，该框架从短音频样本中创建数字语音表示，然后使用该表示从任何给定的文本生成语音。

该项目实现了几个关键论文，包括SV2TTS、WaveRNN (声码器)、Tacotron (合成器) 和GE2E (编码器)。作者承认，更新、通常是付费的SaaS解决方案提供更卓越的音频质量，但该仓库提供了一个开源替代方案。对于寻求最先进的开源解决方案的用户，建议使用Chatterbox和Paperswithcode。

该仓库支持Windows和Linux，推荐使用Python 3.7和GPU以获得最佳性能。设置包括安装ffmpeg、PyTorch以及`requirements.txt`中列出的其他依赖项。预训练模型会自动下载，但如果需要，也可以手动下载。可以使用`python demo_cli.py`测试配置。用户可以选择下载LibriSpeech等数据集进行实验，或者使用他们自己的音频数据。工具箱通过`python demo_toolbox.py`启动，可以选择指定数据集根目录。

---

## 10. 网站就是一个SVG (2007)

**原文标题**: Website Is Just an SVG (2007)

**原文链接**: [https://svg.nicubunu.ro/](https://svg.nicubunu.ro/)

2007年，Nicu在一个名为“网站就是一个SVG”的项目中，探索了使用SVG（可缩放矢量图形）作为构建网站的唯一技术的可行性。其核心动机是测试谷歌对SVG文件的索引能力，特别是全文索引和链接跟踪。Nicu想确定谷歌是否能够识别和索引SVG内的文本内容，而不是将文件视为一个简单的图像。至关重要的是，该实验旨在确定谷歌是否会抓取并索引嵌入在SVG文件中的链接到其他链接资源的链接。

其根本目标是评估使用矢量图形编辑器Inkscape来创作整个网站的有效性。Nicu承认了不当使用SVG可能带来的缺点，可能会导致文件臃肿和不良的用户体验。他还强调SVG是万维网联盟 (W3C) 的标准。

测试网站使用了高级SVG功能，例如高斯模糊，并指出较旧的浏览器可能无法完全支持这些功能。他建议用户使用Gecko 1.9驱动的浏览器（如Firefox 3.0或更高版本）获得最佳体验。文章还包含一段特定的文本字符串("lmtbk4mh")，旨在被搜索引擎发现，以此作为索引能力的实际测试。最终，该项目是对仅仅依靠SVG进行网站创建的实用性和有效性的调查，重点关注搜索引擎优化方面。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 2 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 3 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 4 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 5 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 6 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 7 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 8 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 9 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 10 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 11 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 12 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 13 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 14 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 15 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 16 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 17 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 18 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 19 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 20 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 21 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 22 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 23 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 24 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 25 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 26 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 27 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 28 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 29 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 30 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 31 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 32 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 33 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 34 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 35 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 36 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 37 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 38 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 39 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 40 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 41 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 42 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 43 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 44 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 45 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 46 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 47 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 48 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 49 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 50 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 51 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 52 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 53 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 54 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 55 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 56 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 57 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 58 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 59 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 60 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 61 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 62 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 63 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 64 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 65 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 66 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 67 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 68 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 69 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 70 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 71 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 72 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 73 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 74 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 75 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 76 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 77 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 78 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 79 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 80 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 81 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 82 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 83 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 84 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 85 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 86 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 87 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 88 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 89 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 90 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 91 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 92 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 93 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 94 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 95 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 96 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 97 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 98 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 99 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 100 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 101 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 102 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 103 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 104 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 105 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 106 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 107 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 108 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 109 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 110 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 111 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 112 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 113 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 114 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 115 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 116 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 117 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 118 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 119 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 120 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 121 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 122 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 123 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 124 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 125 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 126 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 127 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 128 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 129 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 130 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 131 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 132 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 133 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 134 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 135 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 136 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 137 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 138 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 139 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 140 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 141 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 142 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 143 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 144 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 145 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 146 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 147 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 148 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 149 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 150 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 151 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 152 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 153 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 154 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 155 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 156 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 157 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 158 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 159 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 160 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 161 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 162 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 163 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 164 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 165 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 166 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 167 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 168 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 169 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 170 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 171 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 172 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 173 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 174 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 175 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 176 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 177 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 178 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 179 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
