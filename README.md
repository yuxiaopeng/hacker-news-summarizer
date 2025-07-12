# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-12.md)

*最后自动更新时间: 2025-07-12 17:46:11*
## 1. 80年代中期的MacPaint艺术作品，今天依然赏心悦目

**原文标题**: MacPaint Art from the Mid-80s Still Looks Great Today

**原文链接**: [https://blog.decryption.net.au/posts/macpaint.html](https://blog.decryption.net.au/posts/macpaint.html)

八十年代中期MacPaint艺术作品，至今仍令人惊艳

这篇博文讲述了作者重新发现八十年代中期早期MacPaint艺术作品的故事。受到BMUG的CD-ROM启发，作者深入研究了Discmaster上的超过18,000张MacPaint图像，并分享了他们挖掘出的一些“珍品”。作者计划在未来的博文中分享更多较小的图画/图标。

一个关键的主题是欣赏在那个时代的技术限制下所取得的艺术成就，特别是原始Macintosh的小型单色屏幕。作者对这些作品背后的艺术家表达了好奇，并想知道鉴于他们显而易见的天赋，他们此后取得了什么成就。

博文最后简要提到了Macintosh的同期产品Amiga电脑，以及作者探索该平台创作的艺术作品的意图，暗示了作者对早期家用电脑艺术史的更广泛兴趣。

---

## 2. 拟议的美国国家海洋和大气管理局预算将取消旨在防止卫星碰撞的项目。

**原文标题**: Proposed NOAA Budget Kills Program Designed to Prevent Satellite Collisions

**原文链接**: [https://skyandtelescope.org/astronomy-news/proposed-noaa-budget-kills-program-to-prevent-satellite-collisions/](https://skyandtelescope.org/astronomy-news/proposed-noaa-budget-kills-program-to-prevent-satellite-collisions/)

《天空与望远镜》杂志报道，拟议的美国国家海洋和大气管理局（NOAA）下个财政年度的预算取消了空间天气后续L1（SWFO-L1）计划的紧凑日冕仪（CCOR）的资金，该仪器旨在监测太阳的日冕物质抛射（CMEs）。CMEs是太阳事件，会扰乱地球磁场，影响卫星运行，甚至导致电网故障。CCOR旨在为这些事件提供关键的预警。

主要担忧是，如果没有CCOR，NOAA预测和减轻空间天气影响的能力将大大降低，从而增加卫星碰撞的风险。准确预测CME到达时间对于卫星运营商采取保护措施至关重要，例如暂时关闭敏感系统或调整卫星轨道。

该文章强调，考虑到对卫星技术的日益依赖以及对空间天气潜在损害的日益认识，削减CCOR的决定令人惊讶。此外，此举似乎与美国政府对空间态势感知和卫星安全的既定承诺相矛盾。CCOR的缺失使美国的卫星基础设施面临更大的风险，对通信、导航和其他关键服务可能产生严重后果。文章表达了对取消CCOR节省的成本与重大空间天气事件影响卫星的潜在经济和社会成本相比微不足道的担忧。

---

## 3. Show HN: BinaryRPC – 现代 C++ 中基于 WebSocket 的轻量级 RPC 框架

**原文标题**: Show HN: BinaryRPC – Lightweight WebSocket-based RPC framework in modern C++

**原文链接**: [https://github.com/efecan0/binaryrpc-framework](https://github.com/efecan0/binaryrpc-framework)

BinaryRPC 是一个全新的开源、轻量级、高吞吐量的 RPC 框架，构建于现代 C++ 的 uWebSockets 之上。它旨在为多人游戏、金融行情流和物联网仪表盘等对延迟敏感的应用提供高性能且对开发者友好的解决方案。

该框架提供类似于 Node.js 中 Express.js 的功能，包括中间件支持、会话管理和 RPC 处理程序架构。主要亮点包括由 uWebSockets 驱动的 WebSocket 传输、具有可配置可靠性（QoS），例如至少一次和精确一次交付的选项、可插拔协议和中间件、具有自动过期的有状态会话以及用于身份验证和速率限制的中间件链。核心是仅头文件，便于包含。

本文提供了有关如何安装 BinaryRPC 的详细说明，包括 CMake、C++20 编译器和 vcpkg 等依赖项管理工具。它涵盖了安装核心和可选依赖项（如 jwt-cpp 和 nlohmann-json）、使用 CMake 构建库以及将其链接到您自己的项目。

本文还深入探讨了使用 `IHandshakeInspector` 进行自定义握手和身份验证，以验证客户端身份和会话令牌。它提供了使用查询参数和基于 JWT 的身份验证的示例。此外，本文还讨论了 BinaryRPC 的可靠性和 QoS 选项，包括不同的交付层级（None、AtLeastOnce、ExactlyOnce）和会话 TTL，以实现无缝重连和离线推送。它提供了自定义退避重试策略的示例。最后，它涉及使用 `FrameworkAPI` 进行会话管理，以便存储、搜索和向连接的客户端推送数据。

---

## 4. OpenAI的Windsurf交易取消，且Windsurf的CEO将加入谷歌。

**原文标题**: OpenAI’s Windsurf deal is off, and Windsurf’s CEO is going to Google

**原文链接**: [https://www.theverge.com/openai/705999/google-windsurf-ceo-openai](https://www.theverge.com/openai/705999/google-windsurf-ceo-openai)

OpenAI取消收购AI代码初创公司Windsurf的计划，转而谷歌将聘用Windsurf首席执行官Varun Mohan、联合创始人Douglas Chen以及其他关键研发人员加入谷歌DeepMind团队，他们将专注于使用Gemini的自主编码工作。

虽然谷歌并未收购Windsurf或持有股份，但将获得Windsurf部分技术的非独家许可。Windsurf业务主管Jeff Wang现任临时首席执行官，全球销售副总裁Graham Moreno升任总裁。

谷歌证实了此举，并表示欢迎Windsurf的人才加入，以推进自主编码工作。Mohan和Chen对Windsurf取得的成就表示自豪，并对公司在现有领导层下的下一阶段充满热情。

谷歌的聘用交易的财务细节未披露，但OpenAI此前预计以30亿美元收购Windsurf。

---

## 5. 鱼踢可能是目前最快的潜泳泳姿 (2015)

**原文标题**: The fish kick may be the fastest subsurface swim stroke yet (2015)

**原文链接**: [https://nautil.us/is-this-new-swim-stroke-the-fastest-yet-235511/](https://nautil.us/is-this-new-swim-stroke-the-fastest-yet-235511/)

文章《鱼踢可能是目前最快的潜泳泳姿》探讨了鱼踢作为一种卓越游泳技术的潜力，重点关注其力学和物理原理。作者Regan Penaluna讲述了她在向奥运金牌得主Misty Hyman寻求指导之前，最初在鱼踢上的挣扎。

文章解释说，通常情况下，潜泳比水面游泳更快，这是因为水面游泳受到“船体速度”的限制，游泳者受到他们所产生的弓形波的限制。鱼踢是一种在游泳者侧面进行的水平波动运动，它可能比传统的海豚踢更快。专家认为，鱼踢产生更有效的涡流（微型漩涡），推动游泳者前进，与海豚踢相比，这些涡流更不易受到泳池表面或底部的干扰。

虽然鱼踢难以掌握和控制，但一些专家认为，一旦掌握，它可能成为最快的泳姿。然而，文章也指出，在现代更深的泳池中，海豚踢在更深处具有优势。文章最后讨论了水下游泳比赛的潜力，以展示鱼踢的真正能力，尽管人们对其电视吸引力持怀疑态度。Penaluna以她在最初尝试中的一些改进结束了她的体验。

---

## 6. 斯通-威尔斯变换

**原文标题**: Stone–Wales Transformations

**原文链接**: [https://johncarlosbaez.wordpress.com/2025/07/12/stone-wales-transformation/](https://johncarlosbaez.wordpress.com/2025/07/12/stone-wales-transformation/)

本文解释了Stone-Wales转化，这是一种拓扑缺陷，常见于富勒烯和石墨烯等碳基结构中。该转化涉及碳原子之间键的90度旋转，导致六边形和五边形（在富勒烯中）或五边形和七边形（在石墨烯中）排列的变化。

在富勒烯中，Stone-Wales转化将两个六边形和两个五边形转化为两个五边形和两个六边形。在石墨烯中，它将四个六边形转化为两个五边形和两个七边形，从而产生Stone-Wales缺陷。

作者认为这些转化非常有趣，并将它们与类似的拓扑转化（如Pachner移动）联系起来。他们还探讨了阿伦尼乌斯方程，该方程描述了化学反应的速率，并被用于研究富勒烯中Stone-Wales转化的频率。作者表示有兴趣发展一种关于随机发生的拓扑转化的理论，该理论由统计力学支配，类似于在矩阵模型中看到的情况。

文章引用了研究论文和在线资源，其中包含展示Stone-Wales转化的图像。Anton Sherwood的评论指出Stone-Wales翻转在简化富勒烯模型创建过程中的实用性。

---

## 7. 官方Gravity Forms插件发现恶意软件，提示供应链遭到破坏

**原文标题**: Malware found in official gravityforms plugin indicating supply chain breach

**原文链接**: [https://patchstack.com/articles/critical-malware-found-in-gravityforms-official-plugin-site/](https://patchstack.com/articles/critical-malware-found-in-gravityforms-official-plugin-site/)

2025年7月11日，Patchstack报告了一起针对WordPress的Gravity Forms插件的供应链攻击。最初，在下载的插件文件中检测到一个可疑的HTTP请求，目标指向`gravityapi.org`域名。该域名最近于2025年7月8日注册，引发关注。

技术分析显示，`gravityforms/common.php`文件中的`update_entry_detail`函数向`https://gravityapi.org/sites`发起POST请求，发送敏感的WordPress实例信息。服务器的响应包括一个`gf_name`（文件名）和一个`body`（base64编码的内容）。解码后的内容随后被保存到WordPress服务器上指定的文件名，允许攻击者注入恶意代码。在报告的实例中，创建了包含PHP代码的文件`wp-includes/bookmark-canonical.php`。

Gravity Forms确认正在调查恶意软件入侵事件，并已从下载包中删除了恶意代码。发布了2.9.13版本以确保安全更新。Namecheap暂停了`gravityapi.org`域名，以防止进一步的利用。恶意软件主要影响手动下载和composer安装。Patchstack建议检查IOCs，尽管感染似乎仅限于少数用户。观察到一个IP地址，193.160.101.6，使用`gf_api_token`参数向各种Gravity Forms版本发出请求。

---

## 8. Commodore 64 终极版

**原文标题**: Commodore 64 Ultimate

**原文链接**: [https://www.commodore.net](https://www.commodore.net)

“Commodore 64 Ultimate”：一款全新的官方 Commodore 64 电脑，是 30 多年来的首款。它致敬经典，同时加入了现代功能。定价 299 美元起，旨在提供更简单、无干扰的计算体验，让人想起技术更加用户友好的时代。

该设备兼容超过 10,000 款原版 Commodore 64 游戏、卡带和外设。现代增强功能包括游戏联动变色 LED 外壳、用于游戏传输的 Wi-Fi 以及预装经典和新游戏的 USB“磁带”存储。

在美学上，Commodore 64 Ultimate 具有透明键盘和电路板，展示了内部技术。主板上蚀刻着原 C64 创始人的姓名/签名。它还配有螺旋装订的手册和光面经典包装盒。

Commodore 64 Ultimate 针对怀旧用户和新用户，提供了一个学习计算机工作原理的机会，并以有趣且引人入胜的方式向孩子们介绍 BASIC 编程。核心信息强调一种邀请互动和学习而非控制的技术。

---

## 9. 学习“编写C编译器”

**原文标题**: Working through 'Writing A C Compiler'

**原文链接**: [https://jollygoodsw.wordpress.com/2025/03/13/working-through-writing-a-c-compiler/](https://jollygoodsw.wordpress.com/2025/03/13/working-through-writing-a-c-compiler/)

本文是名为“编写 C 编译器”(WACC) 系列文章的一部分，重点介绍第 15 章，该章节讲述如何在编译器中实现数组和指针运算。

---

## 10. 苏黎世联邦理工学院和洛桑联邦理工学院将在公共基础设施上发布一款大型语言模型。

**原文标题**: ETH Zurich and EPFL to release a LLM developed on public infrastructure

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2025/07/a-language-model-built-for-the-public-good.html](https://ethz.ch/en/news-and-events/eth-news/news/2025/07/a-language-model-built-for-the-public-good.html)

苏黎世联邦理工学院和洛桑联邦理工学院将于2025年夏末发布一款完全开源的大型语言模型(LLM)，该模型在瑞士国家超级计算中心(CSCS)的“阿尔卑斯”超级计算机上开发。该LLM旨在促进广泛应用，促进各行业的创新，并提供一种可靠的商业开发模型替代方案。

主要特性包括精通1000多种语言的多语言能力，通过在包含60%英语和40%非英语语言以及代码和数学数据的大型数据集上进行训练来实现。该模型将提供两种尺寸（80亿和700亿参数），并在15万亿个token上进行训练。

该计划优先考虑透明度，源代码、权重和训练数据将根据Apache 2.0许可证公开提供。它遵守瑞士的数据保护和版权法，以及欧盟人工智能法案的透明度义务。

配备NVIDIA Grace Hopper超级芯片并由碳中和电力驱动的“阿尔卑斯”超级计算机，促进了LLM的训练。该项目是洛桑联邦理工学院、苏黎世联邦理工学院、CSCS、NVIDIA和HPE/Cray之间的合作项目。

该项目属于瑞士人工智能倡议，由ETH委员会支持，涉及瑞士各地800多名研究人员。它是世界上致力于人工智能基础模型的最大规模的开放科学和开源工作。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 2 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 3 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 4 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 5 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 6 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 7 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 8 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 9 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 10 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 11 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 12 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 13 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 14 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 15 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 16 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 17 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 18 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 19 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 20 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 21 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 22 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 23 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 24 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 25 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 26 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 27 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 28 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 29 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 30 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 31 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 32 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 33 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 34 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 35 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 36 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 37 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 38 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 39 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 40 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 41 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 42 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 43 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 44 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 45 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 46 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 47 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 48 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 49 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 50 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 51 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 52 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 53 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 54 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 55 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 56 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 57 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 58 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 59 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 60 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 61 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 62 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 63 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 64 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 65 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 66 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 67 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 68 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 69 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 70 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 71 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 72 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 73 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 74 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 75 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 76 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 77 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 78 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 79 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 80 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 81 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 82 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 83 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 84 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 85 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 86 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 87 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 88 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 89 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 90 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 91 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 92 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 93 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 94 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 95 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 96 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 97 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 98 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 99 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 100 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 101 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 102 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 103 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 104 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 105 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 106 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 107 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 108 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 109 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 110 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 111 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 112 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 113 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 114 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 115 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
