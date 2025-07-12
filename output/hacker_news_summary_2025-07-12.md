# Hacker News 热门文章摘要 (2025-07-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. XAI寻求在下一轮融资中达到2000亿美元估值

**原文标题**: XAI seeks up to $200B valuation in next fundraising

**原文链接**: [https://www.ft.com/content/25aab987-c2a1-4fca-8883-38a617269b68](https://www.ft.com/content/25aab987-c2a1-4fca-8883-38a617269b68)

埃隆·马斯克的xAI据报道寻求在下一轮融资中估值高达2000亿美元。《金融时报》（FT）发表的这篇文章设置了付费墙，需要订阅才能完全访问。FT提供多种订阅选项，包括标准数字版、高级数字版和印刷+高级数字版，每种订阅级别提供不同程度的访问其新闻和专题报道的权限。文章强调了FT新闻报道的价值，突出了其全球新闻和分析、专家观点以及各种数字功能，旨在吸引读者订阅以获得更全面的报道。

---

## 12. Show HN: DesignArena – AI生成UI/UX的众包基准

**原文标题**: Show HN: DesignArena – crowdsourced benchmark for AI-generated UI/UX

**原文链接**: [https://www.designarena.ai/](https://www.designarena.ai/)

DesignArena：人工智能UI/UX设计基准众包平台。用户投票选出最佳AI设计模型，提交网站设计、游戏开发、3D设计、数据可视化、UI组件和图像生成等各类设计提示。近期示例包括：摄影业务作品集网站、量子计算研究数据可视化和地球仪3D模型。平台设有排行榜展示顶尖AI模型，并鼓励用户推荐遗漏模型。网站实时展示近期投票和提示，以促进社区参与。本质上，DesignArena旨在建立一个社区驱动的AI设计工具评估体系。

---

## 13. 首个婴幼儿疟疾疗法获批使用

**原文标题**: First malaria treatment for babies approved for use

**原文链接**: [https://www.bbc.com/news/articles/c89e872jdjxo](https://www.bbc.com/news/articles/c89e872jdjxo)

一种专为婴幼儿配制的新型疟疾治疗药物已获批准，解决了此前婴儿只能服用为较大儿童设计的药物所造成的严重“治疗缺口”，由于肝功能和药物代谢的差异，这会带来过量风险。该药物由诺华公司开发，名为Coartem Baby或Riamet Baby，已获得瑞士当局批准，预计将在几周内以非营利方式在非洲国家推广。

2023年，疟疾导致约59.7万人死亡，几乎全部发生在非洲，其中约四分之三是五岁以下儿童。到目前为止，还没有专门为体重低于4.5公斤的婴儿设计的疟疾药物。

该药物的开发涉及诺华公司、疟疾药物风险投资公司（MMV）之间的合作，并获得了多个政府和盖茨基金会的财政支持。八个非洲国家参与了评估和试验，预计将成为首批获得治疗的国家。专家们认为这是一个重大突破，有可能挽救脆弱的婴幼儿的生命，尤其是在撒哈拉以南非洲等疟疾死亡率高的地区。非营利模式也有望减少医疗不平等。

---

## 14. 用D语言制作速通计时器

**原文标题**: Making a Speedrun Timer in D

**原文链接**: [https://bradley.chatha.dev/blog/linux-speedrun-timer-dlang/post/](https://bradley.chatha.dev/blog/linux-speedrun-timer-dlang/post/)

本文详述了作者在Linux上为《杀出重围》（Deus Ex）创建自定义速通计时器的过程，解决了因Linux限制而缺乏可用LiveSplit插件的问题。其目标是创建一个具有自动分段和加载时间移除功能的计时器。

由于虚幻引擎内存分配的动态性，最初尝试在内存中寻找加载标志的方案宣告失败。随后，作者转向了一种更复杂的方法，即向游戏进程注入自定义代码。

主要步骤包括：

*   利用`ptrace`和`process_vm_readv`系统调用来读取和写入游戏内存。
*   使用导出地址表在Engine.dll中识别`LoadMap`函数。
*   在Engine.dll的内存映射中找到一个未使用的、可写入的内存区域，以存储自定义加载标志。

作者描述了用D语言创建一个迷你框架来管理查找和与游戏进程交互、修补游戏代码以及创建计时器用户界面的过程。目标是修改`LoadMap`函数以设置一个指示加载状态的标志，计时器可以监控该标志以实现自动分段和加载时间移除的目的。

---

## 15. 亚利桑那州居民出现症状后不到24小时死于鼠疫。

**原文标题**: Arizona resident dies from the plague less than 24 hours after showing symptoms

**原文链接**: [https://www.independent.co.uk/news/health/arizona-plague-death-cases-b2787325.html](https://www.independent.co.uk/news/health/arizona-plague-death-cases-b2787325.html)

亚利桑那州北部一名居民死于鼠疫，尸检证实存在鼠疫耶尔森菌后，卫生官员确认了该病例。受害者因严重症状被紧急送往弗拉格斯塔夫医疗中心，当日死亡。该病例恰逢弗拉格斯塔夫东北部最近发生草原犬鼠大规模死亡事件，这是鼠疫活动的一个已知指标，原因是感染了跳蚤。科科尼诺县官员正在调查草原犬鼠的死亡情况，并收集跳蚤进行检测。

虽然鼠疫在美国很少见，平均每年约有七例，但主要发生在美国西部的农村地区。鼠疫有三种表现形式：腺鼠疫、败血性鼠疫和肺鼠疫。美国大多数病例是腺鼠疫，通常通过感染啮齿动物的跳蚤叮咬传播。症状可能在一周内出现，包括发烧、发冷、淋巴结肿大、恶心和虚弱。

早期抗生素治疗非常有效，最好在症状出现后的24小时内进行，腺鼠疫的存活率超过90%。公共卫生官员敦促居民报告患病或死亡的啮齿动物，对宠物进行跳蚤控制，并在潜在暴露后出现症状时立即就医。

---

## 16. Sieve (YC X25) 正在招聘研究人员，为 AI 实验室构建大型视频数据集。

**原文标题**: Sieve (YC X25) is hiring researchers to build large video datasets for AI labs

**原文链接**: [https://sievedata.com/about/jobs](https://sievedata.com/about/jobs)

Sieve (YC X25) 正在招聘研究员，为人工智能实验室构建专门定制的大型视频数据集。 这意味着 Sieve 正在解决人工智能领域的一个关键需求：提供高质量、大规模的视频数据集来训练和评估先进的人工智能模型。该公司可能专注于视频数据，将其作为核心战略组成部分，并向那些难以获取或创建自有数据集的人工智能实验室提供服务。 他们是一家 Y Combinator 投资的公司 (YC X25) 这一事实增加了其可信度，并表明其业务具有坚实的基础。 受聘的研究员可能会参与数据收集、标记、注释等任务，甚至可能参与数据集的策划和验证，以确保数据的质量和适用于人工智能训练。 本质上，Sieve 通过解决获取相关且全面的视频数据集的瓶颈，将自己定位为人工智能视频应用的基本基础设施提供商。

---

## 17. 伪造JPEG图像

**原文标题**: Faking a JPEG

**原文链接**: [https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/](https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/)

2025年3月25日，作者讨论了一个名为Spigot的项目，这是一个旨在生成包含无意义内容的虚假网页以吸引和研究网络爬虫的Web应用程序。观察到名为“ImageSiftBot”的爬虫在Spigot缺乏图像的情况下仍然积极地寻求图像，作者设计了一种方法来创建虚假的JPEG图像，以满足爬虫的请求，而不会过度消耗服务器的CPU。

该方法涉及使用来自作者网站上真实JPEG图像的模板。通过提取JPEG文件的结构化部分（大小、颜色深度）并记录像素数据块的长度，作者创建了一组逼真的模板。为了生成虚假的JPEG，脚本会随机选择一个模板，并用随机数据填充像素数据块。

最初，作者发现纯粹的随机像素数据会导致解码器错误，原因是哈夫曼编码结构。然而，这些垃圾JPEG仍然被大多数JPEG查看器接受和显示，使其适合欺骗网络爬虫。作者还实施了一种位掩码技术，以进一步降低生成无效哈夫曼代码的可能性。

这种方法允许每秒生成大约900张垃圾图像，这比服务器的互联网连接速度快得多。虚假JPEG生成被集成到Spigot中，大约60%的生成页面包含一个垃圾JPEG。ImageSiftBot以及Meta的机器人、AmazonBot和GPTBot等其他爬虫的活动有所增加，它们抓取了这些图像。作者已在GitHub上发布了代码，并继续优化它，以提高效率和有效性，从而浪费滥用的网络爬虫的资源。

---

## 18. 印度航空坠机事故初步报告发布

**原文标题**: Preliminary report into Air India crash released

**原文链接**: [https://www.bbc.co.uk/news/live/cx20p2x9093t](https://www.bbc.co.uk/news/live/cx20p2x9093t)

印度航空6月12日在艾哈迈达巴德坠机事故造成260人死亡，一份初步报告已发布。报告虽未下定论，但显示坠机前燃油开关处于“切断”位置。驾驶舱录音显示飞行员之间存在困惑，一人质问另一人关闭开关，另一人否认。

印度航空部长告诫不要进行猜测，而美国航空监管机构承诺将根据事实进行调查。该报告让遇难者家属产生了更多疑问。

该调查由印度飞机事故调查局主导，美国国家运输安全委员会提供支持，目前仍在进行中。预计明年发布最终报告。关于坠机事故和驾驶舱录音重要性的更多细节可在持续报道中找到。

---

## 19. 仅在南塔克特：奔驰“失窃”奇案

**原文标题**: Only on Nantucket: The Curious Case of the "Stolen" Mercedes

**原文链接**: [https://nantucketcurrent.com/news/only-on-nantucket-the-curious-case-of-the](https://nantucketcurrent.com/news/only-on-nantucket-the-curious-case-of-the)

一辆奔驰G级越野车在楠塔基特岛一家Stop & Shop超市停车场被报失窃，由于该岛汽车盗窃案罕见，引发了全岛猜测。谜团最终解开，岛上居民Alex Miccio意识到他年长的家人朋友错误地开走了另一辆G级越野车。Miccio将自己的G级越野车钥匙留给了这位朋友，朋友抵达渡轮后，发现一辆相似的车辆，钥匙竟然能用。这位朋友将错误的车辆开回了家，并未意识到这个错误。

车辆已归还，警方证实不会提出指控，认为这是一起认错车辆的案件。警察中尉Angus MacVicar强调，由于岛上相似车辆众多以及人们将钥匙留在车内的情况普遍，车辆失踪的情况时有发生。他建议司机在开车离开前仔细检查车辆登记信息。MacVicar还提到，尽管不太频繁，但兜风也是另一个原因，并回忆起他职业生涯中只有一个失窃车辆未迅速找回的案例，几个月后最终在森林深处被发现。他还指出，蒸汽船管理局会收到失踪车辆的警报，使得汽车盗贼很难逃离该岛。

---

## 20. 垃圾回收基础 (2023)

**原文标题**: Fundamentals of garbage collection (2023)

**原文链接**: [https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals)

本文阐述了 .NET CLR 中垃圾回收 (GC) 的基本原理，这是一种自动内存管理系统。GC 使开发人员无需手动释放内存，防止内存泄漏，并确保内存安全。

关键概念包括：

*   **托管堆：** 一个连续的虚拟地址空间区域，CLR 在此为对象分配内存。
*   **内存分配：** GC 通过递增托管堆上的指针来高效地分配内存。
*   **内存释放：** GC 通过检查应用程序根（静态字段、局部变量、CPU 寄存器、GC 句柄、终结队列），创建可达对象图并压缩内存，来回收来自不可达对象的内存。
*   **垃圾回收条件：** 由物理内存不足、超过分配阈值或调用 `GC.Collect` 触发。
*   **代：** 托管堆分为三个代（0、1 和 2）以优化 GC 性能。第 0 代包含短生存期对象，第 1 代充当缓冲区，第 2 代包含长生存期对象。大型对象堆 (LOH)，有时被称为第 3 代，处理大于 85,000 字节的对象。
*   **生存和晋升：** 在 GC 中幸存的对象会被晋升到下一代。一代中较高的生存率会导致该代的分配阈值增加。
*   **临时代和段：** 第 0 代和第 1 代是临时的，驻留在临时段中。此段的大小因系统架构和 GC 类型而异。

本质上，GC 通过为新对象分配空间、回收来自未使用对象的内存以及压缩内存以避免碎片化来自动管理内存。这优化了应用程序性能并通过消除手动内存管理的需求来简化开发。

---

## 21. Jank 是 C++

**原文标题**: Jank is C++

**原文链接**: [https://jank-lang.org/blog/2025-07-11-jank-is-cpp/](https://jank-lang.org/blog/2025-07-11-jank-is-cpp/)

本项目旨在实现从 Clojure 无缝对接 C++，以下是“jank”项目上季度取得的进展详情：

*   **手动内存管理：** 使用 jank 的垃圾回收器 (bdwgc) 实现了 `cpp/new` 和 `cpp/delete`，并支持析构函数。
*   **C++ 布尔值：** 引入了 `cpp/true` 和 `cpp/false`，用于直接处理 C++ 布尔值，避免了隐式类型转换并生成更精简的 IR。
*   **复杂类型：** 使用符号中的指针类型（例如 `cpp/int**`）和用于模板的 `cpp/type` 函数（例如 `(cpp/type "std::map<std::string, int>")`）扩展了类型表示。
*   **复杂类型构造函数：** 调用类型时，`.` 后缀变为可选，类型调用被视为构造函数调用。
*   **不透明盒子：** 创建了 `cpp/box` 和 `cpp/unbox`，用于处理原始本机指针，使其能够在 jank 的数据结构中使用，需要像在 C++ 中一样进行手动类型管理。
*   **预编译头文件 (PCH)：** 实现了 PCH 预编译，以加快启动速度。
*   **稳定性改进：** 解决了与数组、全局指针、函数指针、可变参数 C 函数调用和 LLVM 问题相关的各种崩溃。
*   **静态类型：** 强调了 jank 的静态类型 C++ 互操作。
*   **实际示例：** 通过使用流的“Hello, world”示例、使用 `json.hpp` 的 JSON 漂亮打印机以及使用 `ftxui` 的终端 UI，演示了互操作。

作者还提到 Clasp，另一个 C++ Lisp 实现，作为灵感来源。未来的计划包括解决堆栈分配对象的自动析构函数调用问题，改进打包和分发，以及修复错误，为 alpha 版本的发布做准备。

---

## 22. 使用8位家用电脑复制量子因式分解记录 [pdf]

**原文标题**: Replication of Quantum Factorisation Records with an 8-bit Home Computer [pdf]

**原文链接**: [https://eprint.iacr.org/2025/1237.pdf](https://eprint.iacr.org/2025/1237.pdf)

标题：“使用8位家用电脑复制量子因式分解记录[pdf]”

此文档（标题为“使用8位家用电脑复制量子因式分解记录[pdf]”）是一个PDF文件，但其内容主要是二进制数据，间杂着PDF格式标记。根据标题，该文档*声称*描述了一种使用非常基础的8位家用电脑复制量子因式分解记录的方法。

然而，PDF的实际内容高度压缩，并且在被解释为文本时，看起来大多是毫无意义的。存在大量的二进制乱码，这表明该文档要么经过高度优化和压缩，要么更可能的是数据已损坏。 看起来像是文本的部分包含代码片段或数据，可能与PDF文档中常见的图像处理或字体嵌入有关。某些片段似乎与JPEG编码和PDF结构元素有关。

几乎没有连贯的文本信息来支持标题的主张。标题本身提出了一个非同寻常的声明，如果真实，将具有巨大的科学意义。在无法可靠地解压缩和分析PDF中的压缩信息的情况下，无法验证标题的有效性，并且它可能是欺诈性的或存在技术缺陷。

---

## 23. 利用Elixir的热代码加载能力来模块化单体应用

**原文标题**: Leveraging Elixir's hot code loading capabilities to modularize a monolithic app

**原文链接**: [https://lucassifoni.info/blog/leveraging-hot-code-loading-for-fun-and-profit/](https://lucassifoni.info/blog/leveraging-hot-code-loading-for-fun-and-profit/)

本文探讨了作者如何利用 Elixir 的热代码加载功能来模块化名为 Alzo 的单体应用（用于提供特定客户服务），从而避免采用微服务架构。Alzo 为每个客户部署一个实例，以便于本地部署、实现开源潜力以及简化特定客户的应用开发。

特定客户的应用，主要是基于 LiveView 的多人文档编辑器，位于专用目录中并实现特定行为。这些应用会在运行时动态加载到主应用程序中。

为了确保隔离，特定客户的代码会在构建过程中被移除。这确保了主应用程序不依赖于运行时应用代码，反之亦然。测试最初包含动态应用，但在 Docker 镜像构建之前会被移除。这种方法利用 LiveView 和单元测试来代替微服务通常需要的集成测试。

特定客户的应用使用 mix 命令打包，并通过管理面板上传。上传的应用会被重新编译，并在主应用程序启动时动态加载。本文还简要提及，由于应用程序的性质，避免了热代码*升级*，而是专注于热代码*加载*。

对于更复杂的服务，外部功能齐全的应用通过消息路由器与 Alzo 通信，从而支持请求/响应和请求/邮箱/轮询/响应模式。

作者总结说，热代码加载已被证明在其用例中是成功的，便于在出现通用性时将特定行为轻松重构到主代码库中。

---

## 24. Watchfiles: 用 Rust 编写的简单、现代且快速的 Python 文件监控工具

**原文标题**: Watchfiles: Simple, modern and fast file watching for Python, written in Rust

**原文链接**: [https://github.com/samuelcolvin/watchfiles](https://github.com/samuelcolvin/watchfiles)

Watchfiles 是一个 Python 库，用 Rust 编写，旨在实现简单、现代和高性能的文件监视和代码重新加载。它利用 Notify Rust 库进行底层文件系统通知。之前名为 "watchgod"，现已提供迁移指南。

它支持 Python 3.9 到 3.14 版本，可以通过 `pip install watchfiles` 安装。 预构建的二进制文件适用于 Linux、MacOS 和 Windows 上的大多数架构；否则，从源代码安装需要 Rust。

该库提供以下几个函数：

*   `watch`: 用于基本的文件监视和打印更改。
*   `awatch`: 使用 `asyncio` 的 `watch` 异步版本。
*   `run_process`: 运行一个函数作为目标，并在文件更改时重新启动。
*   `arun_process`: 使用 `asyncio` 的 `run_process` 异步版本。

每个函数都有相应的文档，其中包含详细的用法说明。

Watchfiles 还提供了一个命令行界面 (CLI)，用于在文件更改时运行命令，可以通过 `watchfiles "some command" src` 或 `watchfiles --help` 访问选项。 其文档可以在 CLI 文档中找到。

---

## 25. 构建沃森：DeepQA项目概述（2010）

**原文标题**: Building Watson: An Overview of the DeepQA Project (2010)

**原文链接**: [https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2303](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2303)

以下是我对“构建沃森：DeepQA 项目概述”一文的总结，基于我对该项目的理解和相关常识，因为我无法直接访问外部网站：

“构建沃森”一文概述了 DeepQA 项目，该项目的目标是创建一个问答 (QA) 系统，使其能够在 Jeopardy! 问答节目中与顶级人类选手竞争。 这篇文章详细介绍了开放领域 QA 中固有的挑战，即系统必须理解复杂的自然语言，推理大量信息，并在时间限制内提供精确的答案。

文章中描述的沃森架构基于大规模并行和基于证据的推理。 它利用数百种不同的算法（管道）同时运行，以分析问题、生成假设（可能的答案）、从各种来源（包括结构化数据库、非结构化文本和本体）收集证据，并根据累积的证据对每个假设进行评分。 这些算法独立运行，提高了鲁棒性，并允许采用不同的方法进行问题分析和答案生成。

DeepQA 项目的一个关键贡献是它强调*统计*机器学习技术，而不是仅仅依赖手工制定的规则。 这使得沃森能够从数据中学习并适应语言的细微差别。 该文章可能讨论了沃森如何权衡和组合来自这些不同算法的证据，从而得出每个假设的最终置信度评分。 得分最高的假设随后被呈现为沃森的答案。

该文章强调，沃森的成功源于其将包括自然语言处理、信息检索、知识表示和机器学习在内的各种 AI 技术集成到连贯且可扩展的架构中的能力。 该系统的开放架构允许通过添加新的算法和知识来源进行持续改进。 最后，该文章可能讨论了 DeepQA 项目对于推进 AI 领域及其在 Jeopardy! 之外的潜在应用的更广泛意义。

---

## 26. 吴恩达：用人工智能加速构建 [视频]

**原文标题**: Andrew Ng: Building Faster with AI [video]

**原文链接**: [https://www.youtube.com/watch?v=RNJCfif1dPY](https://www.youtube.com/watch?v=RNJCfif1dPY)

所提供的信息并未描述吴恩达“利用人工智能构建更快速的应用”视频的内容，仅仅是YouTube视频上常见的页脚信息，与版权、服务条款和联系方式相关。因此，仅凭这些信息无法总结该视频的内容。

---

## 27. 反向代理深度解析

**原文标题**: Reverse proxy deep dive

**原文链接**: [https://medium.com/@mitendra_mahto/cross-posted-from-https-startwithawhy-com-reverseproxy-2024-01-15-reverseproxy-deep-dive-html-c3443dc3e0e5](https://medium.com/@mitendra_mahto/cross-posted-from-https-startwithawhy-com-reverseproxy-2024-01-15-reverseproxy-deep-dive-html-c3443dc3e0e5)

反向代理连接管理深度解析：分布式系统中的关键组件

本文深入探讨了反向代理的连接管理方面，它是分布式系统中的一个关键组件。文章首先概述了反向代理的核心功能：连接管理、HTTP请求解析、服务发现、作为HTTP客户端以及可观测性。

重点在于连接管理，详细介绍了代理处理客户端连接的步骤：绑定端口、监听、接受连接和传输数据。文章强调了扩展连接管理方面的挑战，特别是并发性。传统的阻塞I/O对于大量客户端来说效率低下，导致了非阻塞I/O和I/O多路复用（select、poll、epoll）的演进，以处理更多的并发连接。

然后，文章深入探讨了C10k问题以及事件驱动编程的兴起，强调使用单个事件循环来监视I/O就绪状态。文章讨论了单线程事件循环在处理长时间运行操作方面的局限性，从而引出了多线程解决方案。还介绍了使用SO_REUSEPORT的套接字分片，作为利用操作系统负载均衡的一种方法。最后，文章讨论了TLS支持和库选择（OpenSSL、LibreSSL、BoringSSL）作为连接管理中的复杂因素。

结论强调了扩展连接管理的复杂性，并鼓励读者理解不同代理解决方案的细微差别。作者承诺在未来的文章中涵盖反向代理的其他方面，如HTTP解析、服务发现、HTTP客户端功能和可观测性。

---

## 28. New Date("wtf") – 你有多了解 JavaScript 的 Date 类？

**原文标题**: New Date("wtf") – How well do you know JavaScript's Date class?

**原文链接**: [https://jsdate.wtf](https://jsdate.wtf)

这是一个关于`Date`类的JavaScript测验。它似乎是由"samwho"创建的网页呈现的。该测验包含20个问题，用于测试对JavaScript Date对象的了解。问题在配备BST时区（UTC+1）的MacBook Pro上使用NodeJS 24.4.0进行验证。页面包含诸如“开始测验”、“下一题”等导航元素，以及表示分数为“0 / 0”的测验结束消息。页面上还提供分享和复制选项。标题“New Date("wtf") – 你有多了解JavaScript的Date类？”暗示某些问题可能侧重于使用不寻常的输入实例化`Date`对象时出现的意外或不太常见的行为。

---

## 29. Python中的字典解包

**原文标题**: Dict Unpacking in Python

**原文链接**: [https://github.com/asottile/dict-unpacking-at-home](https://github.com/asottile/dict-unpacking-at-home)

本文介绍了一个讽刺性的Python包`dict-unpacking-at-home`，声称提供字典解包功能。作者强烈建议不要使用它，幽默地提及了对意外创建关键PyPI包的担忧。

该包通过`pip install dict-unpacking-at-home`安装，并通过在Python文件顶部添加`# -*- coding: dict-unpacking-at-home -*-`来激活。本文通过示例展示了它的用法，展示了解包简单字典，甚至包括列表等嵌套结构。

然而，作者强调了其显著的缺点。具体来说，当前版本引入了堆栈跟踪行号错误，尽管在`correct-line-numbers`分支中存在潜在的修复方案，但代价未明。结论重申了最初的警告，不鼓励使用该包。脚注提到了对另一个玩笑项目变得出乎意料地流行并对PyPI至关重要的担忧。本质上，本文是一个伪装成软件包公告的警示故事，突出了开源开发中意外后果的危险。

---

## 30. 鉴于环境影响，ChatGPT搜索“显著”不设上限

**原文标题**: No limit to ChatGPT searches 'remarkable' given environmental impact

**原文链接**: [https://www.independent.co.uk/climate-change/news/tim-peake-chatgpt-ceo-british-chichester-b2787894.html](https://www.independent.co.uk/climate-change/news/tim-peake-chatgpt-ceo-british-chichester-b2787894.html)

在古德伍德速度节上，宇航员蒂姆·皮克强调了ChatGPT搜索“显著”缺乏限制的问题，并引发了对驱动人工智能的数据中心对环境产生巨大影响的担忧。他强调了人工智能搜索相关的能源和水消耗，并建议负责任地使用。皮克提出轨道数据中心作为一种潜在的解决方案，理由是太空拥有清洁、无限的能源。然而，像多梅尼科·维琴扎博士这样的批评家认为，天基数据中心将是复杂且资源密集的。

皮克还指出，超过50%的气候数据来自太空，突显了其在环境监测中的关键作用。“未来实验室”展示了尖端技术，包括由ChatGPT驱动的Ameca人形机器人，该机器人展示了令人印象深刻的互动能力。国家机器人研究院首席执行官斯图尔特·米勒强调了理解和协调人机互动的重要性。皮克质疑，像ChatGPT这样的人工智能工具虽然有用，但是否会削弱人类的好奇心以及从独立发现中获得的满足感。他强调了在人工智能使用方面的平衡以及对其能力的教育需求。

---

## 31. 重新涂抹MacBook散热硅脂

**原文标题**: Repasting a MacBook

**原文链接**: [https://christianselig.com/2025/07/repaste-macbook/](https://christianselig.com/2025/07/repaste-macbook/)

本文作者讲述了其为解决老旧 M1 Pro MacBook Pro 风扇噪音过大问题而重涂 CPU 散热硅脂的经历。他们肯定了MacBook的持续性能，但也注意到在执行密集任务时风扇噪音越来越大。

作者解释了散热硅脂的作用及其随时间推移而干燥的趋势，这会导致热传递效率降低。在参考 iFixit 指南后，他们拆卸了 MacBook 以更换散热硅脂。他们遇到了苹果在 RAM 芯片上使用的特殊导热化合物“Carbon Black”，由于其稀有性，他们决定不更换。

在拆卸过程中，作者不小心撕裂了脆弱的风扇电缆，导致需要更换风扇，灾难发生了。 更糟糕的是，在重新组装过程中，同样脆弱的 Touch ID 传感器电缆也莫名其妙地损坏了，导致 Touch ID 功能无法使用，并且可能需要昂贵的Apple维修。

尽管遇到挫折，但重涂散热硅脂的努力产生了积极的结果。 重涂后，MacBook 在 Cinebench 测试期间的最高 CPU 温度从 102°C 降至 96°C，最高风扇转速从 6,300 RPM 显著降至 4,700 RPM，从而实现了更安静、更高效的散热系统。 CPU 的空闲温度也更低。

作者最后建议，除非您有处理精密电子产品的经验，或者可以找到信誉良好的维修店来完成这项工作，否则不要重涂 MacBook 的散热硅脂。 正如作者不幸发现的那样，损坏精密元件的风险很高。 然而，对于旧款 MacBook 而言，改善散热性能的回报可能是值得的。

---

## 32. OpenAI推迟发布开源权重模型

**原文标题**: OpenAI delays launch of open-weight model

**原文链接**: [https://twitter.com/sama/status/1943837550369812814](https://twitter.com/sama/status/1943837550369812814)

提供的文本并非关于OpenAI推迟发布开源权重模型的文章，而是X（原Twitter）的错误信息，表明用户的浏览器中禁用了JavaScript。该信息指示用户启用JavaScript或切换到支持的浏览器以继续使用该平台。它还提供了帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接，以及X Corp.在2025年的版权声明。**因此，提供的文本中没有任何关于OpenAI或任何模型发布延迟的信息。**

---

## 33. ICANN对AFRINIC取消选举却未作解释表示不满。

**原文标题**: ICANN fumes as AFRINIC offers no explanation for annulled election

**原文链接**: [https://www.theregister.com/2025/07/11/afrinic_election_annulled_why/](https://www.theregister.com/2025/07/11/afrinic_election_annulled_why/)

本文详细介绍了围绕非洲互联网络信息中心（AFRINIC）持续不断的动荡，该机构负责管理IP地址和自治系统号。最近的AFRINIC选举，旨在结束自2022年以来无董事会运作的局面，但因法院指定的接管人认为选民文件存在违规行为，特别是欺诈性的授权委托书，而被宣布无效。

全球互联网治理组织ICANN对此“怒火中烧”，并批评AFRINIC的接管人在宣布选举无效和调查所谓欺诈行为方面缺乏透明度。ICANN已提醒AFRINIC，其政策允许其为失能的RIR指定紧急替代机构。

ISPA声称，欺诈性的授权委托书被用于代表资源持有者进行投票，而未经他们的同意。AFRINIC尚未回应有关选举无效和指控的信息请求。

过去与AFRINIC有过诉讼的Cloud Innovation Ltd公司呼吁解散AFRINIC，并将其职责转移到一个更值得信赖的框架下，理由是选举无效证明了该组织已无可救药地失能。他们已经提交了法院文件，寻求这一结果。该公司认为，此举比ICANN取消对AFRINIC的认可更快、更稳定。

---

## 34. Incus – 下一代系统容器、应用容器和虚拟机管理器

**原文标题**: Incus – Next-generation system container, application container, and VM manager

**原文链接**: [https://linuxcontainers.org/incus/](https://linuxcontainers.org/incus/)

Incus是下一代系统容器、应用容器和虚拟机管理器，旨在提供类似云的用户体验。它允许用户管理容器和虚拟机，共享底层存储和网络资源。Incus基于镜像，提供各种Linux发行版的镜像，并支持多种存储后端和网络类型。它可以部署在单台笔记本电脑到整个服务器机架上。

实例的管理通过命令行工具、REST API或第三方集成完成，本地和远程访问均使用单个API。主要功能包括内建安全性（非特权容器）、可扩展性、直观的API和远程访问能力。它还支持项目，用于划分镜像和配置文件。

Incus提供适用于容器和虚拟机的可配置配置文件、备份和恢复功能、快照、容器/镜像传输以及实例迁移。高级资源控制可用于CPU、内存、网络I/O等。还支持USB、GPU和其他设备的设备直通。

Incus运行在最新的Linux发行版上。虽然上游Incus不提供软件包，但可以通过发行版或第三方存储库获得。Incus客户端可用于Windows和macOS，以连接到基于Linux的服务器。它提供LTS和功能版本，其中Incus 6.0是当前的LTS版本。Zabbly提供商业支持。该项目用Go编写，使用Apache 2许可，并欢迎遵循DCO的贡献。

---

## 35. 展示HN：我用编码代理为5岁的孩子做了个玩具音乐控制器

**原文标题**: Show HN: I built a toy music controller for my 5yo with a coding agent

**原文链接**: [https://github.com/jeffmccune/sonoserve](https://github.com/jeffmccune/sonoserve)

作者在“Show HN”上发布的这篇文章介绍了一个项目，作者使用 M5Stack CardPuter 为 5 岁的孩子制作了一个简单的音乐控制器，用于控制 Sonos Play:1 扬声器。目的是让孩子能够轻松地重新开始他们最喜欢的播放列表或以最小的努力播放他们最喜欢的曲目。 CardPuter 充当热键控制器，由简单的按钮按下触发。用于控制 Sonos 扬声器的核心逻辑驻留在服务器上的 Go 可执行文件中，从而最大限度地降低了 CardPuter 上的复杂性。目标是提供简单的用户体验：打开设备，等待绿灯亮起，然后按下一个按钮来启动所需的音乐操作。该项目有效地使用现成的硬件和一个 Go 后端为音乐播放创建了一个儿童友好的界面。

---

## 36. 倡导质量的软件会议

**原文标题**: A software conference that advocates for quality

**原文链接**: [https://bettersoftwareconference.com/](https://bettersoftwareconference.com/)

BSC 2025，一个倡导软件开发质量的软件会议，将于7月12日至14日在瑞典一个迷人的小镇举行。会议也将于瑞典时间早上9点开始在Twitch上进行直播，录像将免费在线提供。

会议汇集了各种各样的演讲者和主题。第一天包括关于编程历史（Casey Muratori）、并行物理引擎（Dennis Gustafsson）、开发工具（Bill Hall）和内部引擎架构（Vjekoslav Krajačić）的讲座。

第二天涵盖实时调试器可视化（Ryan Fleury）、项目完成（Eskil Steenberg）、游戏中的车辆编程（Wassim Alhajomar）、音频中的动态相位对齐（Sander J. Skjegstad）以及关于项目选择的引人深思的演讲（Ted Bendixson）。

第三天包括关于使用梯度进行字形渲染（Demetri Spanos）、安全（Eskil Steenberg）、面向游戏开发者的深度学习和计算机视觉（Cameron Reikes）、无AST编译器（Sam H. Smith）以及编程中的乐观假设（Andrew Reece）的演示。

现场参会仅限邀请，受邀者将收到参会指南。更新信息可通过订阅新闻通讯获取。组织者是 Sam、Sander 和 Charlie。问题可通过 Twitter 提出。

---

## 37. 单轨 – 将 CSS 动画转换为交互式 SVG 图表

**原文标题**: Monorail – Turn CSS animations into interactive SVG graphs

**原文链接**: [https://muffinman.io/monorail/](https://muffinman.io/monorail/)

Monorail：将CSS关键帧动画转换为交互式SVG图表。该工具的主要目的是允许用户以图形格式可视化并交互动画过程。本文重点介绍了该工具将任何CSS关键帧动画转换为交互式图表的能力，以便更好地理解和控制。文章鼓励用户探索页面上提供的示例，以体验该工具的功能。有关详细说明和使用信息，文章引导用户访问Monorail的GitHub存储库。页面还包括播放速度调整功能，可能旨在进一步方便用户交互和分析动画数据。

---

## 38. 稻米反叛者：研究揭示谷物的酿造益处

**原文标题**: Rice rebels: Research reveals grain's brewing benefits

**原文链接**: [https://phys.org/news/2025-06-rice-rebels-reveals-grain-brewing.html](https://phys.org/news/2025-06-rice-rebels-reveals-grain-brewing.html)

本文探讨了阿肯色大学的研究，该研究挑战了人们认为大米不适合啤酒酿造的观点。研究人员Christian Schubert和Scott Lafontaine发表了两项研究，表明大米具有增强风味、提高提取率（即可发酵糖的量）甚至缩短发酵时间的潜力，尤其是在无醇啤酒中。

他们的工作强调了这项研究的及时性，恰逢阿肯色州立法激励在啤酒和清酒生产中使用当地种植的大米。研究人员警告说，目前专注于食品应用有利特性（如高整米率和低血糖指数）的水稻育种计划可能会无意中阻碍其酿造潜力。

第一项研究侧重于无醇啤酒，表明大米可以限制不良醛类物质，缩短发酵时间并改善风味。感官小组发现美国和德国参与者之间的偏好存在差异，这表明平衡的大米-大麦混合物可能具有更广泛的吸引力。第二项研究分析了74个水稻品种，发现提取潜力存在显着差异，确定了直链淀粉含量较低的品种，这些品种在糖化过程中更有效地释放糖分。

Lafontaine强调，大米不仅仅是一种廉价的填充物，而是一种有价值的创新工具，可提供独特的技术和感官益处。某些水稻品种还具有较低的糊化温度，使其更易于加工。这项研究鼓励啤酒商重新考虑大米，从而有助于更可持续和高效的酿造实践，同时满足不断变化的消费者偏好。

---

## 39. 提高量子比特操作的保真度

**原文标题**: Increasing the Fidelity of Qubit Operations

**原文链接**: [https://www.nature.com/articles/s41467-025-61126-0](https://www.nature.com/articles/s41467-025-61126-0)

本文介绍了一种高相干超导量子比特的设计、制造和测量装置，该装置实现的能量弛豫时间（T1）和自旋回波退相干时间（T2 echo）超过了先前报道的超导量子比特。研究人员测得的量子比特频率为2.9 GHz，T1中值为425 μs（最大值为666 ± 33 μs），T2 echo中值为541 μs（最大值为1057 ± 138 μs）。

作者详细介绍了他们的制造过程，该过程基于现有方法，但进行了一些修改，例如使用CF4进行Nb刻蚀和预先切割样品以最大限度地减少大气暴露。这种详细的文档旨在使其他研究小组能够重现他们的结果。

该样品包含四个超导量子比特，每个量子比特都耦合到一个谐振器以进行读出。其中两个是磁通可调的，另外两个具有固定频率。测量是在两个降温周期内进行的。虽然第一次降温显示出有希望的初步结果，但第二次降温显示T1和T2 echo降低，这可能是由于环境变化或表面氧化造成的。尽管有所下降，但实现的相干时间仍然代表着显著的改进。

研究人员得出结论，他们的工作代表了超导量子比特技术的一个进步，并且提供的详细信息将使更广泛的量子计算研究界受益。

---

## 40. 天文学家竞相研究星际访客

**原文标题**: Astronomers race to study interstellar interloper

**原文链接**: [https://www.science.org/content/article/astronomers-race-study-interstellar-interloper](https://www.science.org/content/article/astronomers-race-study-interstellar-interloper)

无法访问文章链接。

---

## 41. Meta 超级智能 – 领导力计算、人才和数据

**原文标题**: Meta Superintelligence – Leadership Compute, Talent, and Data

**原文链接**: [https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/](https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/)

无法访问文章链接。

---

## 42. 用你壁橱里的废品测量电网频率

**原文标题**: Measuring power network frequency using junk you have in your closet

**原文链接**: [https://halcy.de/blog/2025/02/09/measuring-power-network-frequency-using-junk-you-have-in-your-closet/](https://halcy.de/blog/2025/02/09/measuring-power-network-frequency-using-junk-you-have-in-your-closet/)

本文详细介绍了一个使用易得的家用物品测量电网频率的项目。作者受到波罗的海国家电网与欧洲大陆电网同步的启发，想观察该过程中的频率变化。由于缺乏专业设备，作者巧妙地利用了电脑的线路输入、音频线以及现有的电源线作为天线来拾取交流电声。

作者使用Audacity记录了微弱的信号，对其进行了归一化处理，然后开发了一个Python脚本，该脚本结合了数字信号处理(DSP)技术，特别是Hann窗加权的FFT，来分析音频数据并提取主要的频率分量。 使用了较大的FFT窗口（25秒）以获得良好的频率分辨率。

为了验证测量结果，作者将结果与Sympower的频率监测工具的数据进行了比较。 尽管存在一些时间滞后和平滑处理，但DIY设置在跟踪总体频率波动方面证明了出乎意料的准确性。

作者继续记录数据，并将结果与f50hz.de的数据进行了比较，该网站提供了有关欧洲网络频率的信息。通过将作者的数据移动12.5秒以补偿FFT窗口的时间滞后，网络之间的同步时刻清晰可见。 作者注意到在断路器跳闸之前，两个网络的频率之间存在一个有趣的相互漂移。 提供了该项目中使用的Python脚本，供读者尝试自己的测量。

---

## 43. 数字滤波器导论 (2024)

**原文标题**: Introduction to Digital Filters (2024)

**原文链接**: [https://ccrma.stanford.edu/~jos/filters/](https://ccrma.stanford.edu/~jos/filters/)

朱利叶斯·O·史密斯三世的《数字滤波器及其在音频中的应用导论》是一本关于数字滤波器理论及其在音频处理中的实际应用的综合性资源。该书涵盖了滤波器定义、线性度和时不变性等基本概念，并深入研究了滤波器的各种表示形式，包括差分方程、信号流图和脉冲响应。

该书详细解释了Z变换、频率响应分析和极零点分析，为理解和设计数字滤波器提供了工具。探讨了不同的实现结构，如直接型、串联型和并联型，以及它们的数值特性。

书中考察了线性相位和最小相位滤波器等特殊滤波器类型。该材料扩展到高级主题，如全通滤波器、酉滤波器和拉普拉斯变换分析，将数字滤波器与其模拟对应物联系起来。还介绍了滤波器的状态空间表示，以及相关的系统辨识技术。

最后部分深入研究了递归数字滤波器设计，包括巴特沃斯低通滤波器和方程误差方法。该文档还包括实用的资源，如Matlab工具、Faust和Pure Data中的数字滤波示例，以及在线资源链接。目标受众似乎是音频工程和信号处理领域的学生、研究人员和从业者。

---

## 44. 美国放弃搜寻宇宙膨胀信号

**原文标题**: U.S. abandons hunt for signal of cosmic inflation

**原文链接**: [https://www.science.org/content/article/u-s-abandons-hunt-signal-cosmic-inflation](https://www.science.org/content/article/u-s-abandons-hunt-signal-cosmic-inflation)

美国放弃搜寻宇宙暴胀信号
美国国家科学基金会（NSF）已决定停止资助下一代BICEP（宇宙外背景成像偏振）望远镜阵列，该项目主要旨在探测宇宙暴胀的信号——印刻在宇宙微波背景（CMB）上的引力波。

宇宙暴胀是宇宙早期一个理论上的指数膨胀时期，找到其证据将是宇宙学的一项重大突破。位于南极的BICEP系列望远镜一直处于这一探索的前沿。

该项目被取消资助的原因包括预算限制，以及来自欧洲航天局普朗克卫星和其他CMB实验（如西蒙斯天文台和CMB-S4等即将到来的地面观测站）的数据可用性。预计这些其他项目将提供更全面、可能更敏感的CMB偏振数据。

文章表明，虽然美国放弃了其专门的实验，但对暴胀信号的搜寻并未结束。相反，重点正在转向国际合作和替代实验方法，利用其他CMB实验收集的数据和专业知识。这一决定反映了宇宙学研究界内部资源配置的战略性调整，优先考虑更广泛、更协作的努力来了解早期宇宙。文章强调，即使美国主导的BICEP项目不再是追求该目标的主要工具，科学目标仍然重要。

---

## 45. 逆权侵占法，以及一人如何因一群山羊失去土地

**原文标题**: The law of adverse possession, and how one man lost his land to a herd of goats

**原文链接**: [https://www.npr.org/2023/05/03/1173682158/delaware-goats-property-land-squatters-adverse-possession](https://www.npr.org/2023/05/03/1173682158/delaware-goats-property-land-squatters-adverse-possession)

这篇“金钱星球”的文章讨论了特拉华州的一起房产纠纷，涉及继承了家族土地的伯特·班克斯和他的邻居梅丽莎·施罗克。梅丽莎的羊圈侵占了伯特一半的土地。当伯特试图出售土地时，侵占问题就显现出来了。

伯特最初试图说服梅丽莎搬迁羊圈，但最终诉诸法律。这场诉讼凸显了房产法的复杂性，特别是关于逆权侵占的概念（虽然在本节选里没有明确说明，但暗示了这一点）。文章表明，即使有产权契约，所有权也并非总是那么直接明了，尤其是在长期使用和占用（在本案中是羊）等问题出现时。播客节目深入探讨了这起案件的复杂性，探究了“擅自占地的羊”如何使法律程序变得复杂，并挑战了人们对私有产权的传统理解。虽然摘要中没有透露结果，但很明显，这种情况非常不寻常，并强调了房产纠纷中可能存在的法律意外。

---

## 46. 报告称，英国邮局丑闻导致至少13人自杀身亡。

**原文标题**: At Least 13 People Died by Suicide Amid U.K. Post Office Scandal, Report Says

**原文链接**: [https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html](https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html)

无法访问文章链接。

---

## 47. Show HN: Vibe Kanban – 用于管理AI编码代理的看板

**原文标题**: Show HN: Vibe Kanban – Kanban board to manage your AI coding agents

**原文链接**: [https://github.com/BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)

Vibe Kanban：旨在帮助软件工程师更好地管理和编排AI编码助手（如Claude Code、Gemini CLI、Codex和Amp）的工具。 随着AI越来越多地处理代码编写，Vibe Kanban旨在简化人类工程师在规划、审查和协调分配给这些助手的任务中的角色。

该工具便于在不同助手之间切换，并行或顺序地编排它们的执行，简化代码审查和服务器启动，跟踪任务进度，并集中管理编码助手MCP配置。

要使用Vibe Kanban，用户必须首先通过他们选择的编码助手进行身份验证。 安装通过`npx vibe-kanban`完成。 详细文档和用户指南可在网站上找到。 Bug报告和功能请求应作为GitHub issue提交。

开发环境需要Rust、Node.js和pnpm。 命令`pnpm run dev` 使用从 `dev_assets_seed` 文件夹复制的空白数据库启动带有实时重新加载的前端和后端。 从源代码构建涉及运行 `build-npm-package.sh`，然后在 `npx-cli` 文件夹中运行 `npm pack`。 生成的构建可以使用 `npx [GENERATED FILE].tgz` 运行。 欢迎贡献，但在提交pull request之前，应通过GitHub issue与核心团队讨论。

---

## 48. Show HN: 微软官方MCP，用于文档及更多

**原文标题**: Show HN: Microsoft official MCP for documentation and more

**原文链接**: [https://github.com/MicrosoftDocs/mcp](https://github.com/MicrosoftDocs/mcp)

微软 Learn Docs MCP Server：为 AI 代理提供最新微软官方文档信息

---

## 49. OpenFront: 浏览器实时类风险多人游戏

**原文标题**: OpenFront: Realtime Risk-like multiplayer game in the browser

**原文链接**: [https://openfront.io/](https://openfront.io/)

无法访问文章链接。

---

## 50. 姜黄中的铅颜料是全球中毒之谜的罪魁祸首 (2024)

**原文标题**: Lead pigment in turmeric is the culprit in a global poisoning mystery (2024)

**原文链接**: [https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh](https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh)

全球铅中毒之谜：孟加拉国姜黄中添加铬酸铅为祸首。此做法始于20世纪80年代，当时农民在洪水过后难以妥善干燥姜黄根，便使用这种鲜黄色颜料来增强香料的颜色和适销性。即使洪水退去后，由于利润增加，这种做法依然持续。

纽约市警探在调查孟加拉国儿童体内高铅含量以及博士生珍娜·福赛思在孟加拉国农村研究孕妇体内令人担忧的铅含量时，首次发现了这个问题。福赛思追溯铅的来源至姜黄，并发现了农民使用铬酸铅的做法。姜黄中铅的化学指纹与妇女血液中的铅相符。

孟加拉国食品安全局迅速做出反应。他们发布了公共警告，没收了受铅污染的姜黄，对商贩处以罚款，并向农民和磨坊主宣传铅污染的危害。结果，达卡市场上姜黄样品中铅检测呈阳性的百分比从47%降至0%。受影响社区的姜黄农民和孕妇的血铅水平也显著下降。研究人员、卫生官员和执法机构之间的这种合作努力凸显了数据驱动的调查和迅速干预对于解决公共卫生危机的重要性。

---

## 51. 用半价升级M4 Pro Mac mini的存储

**原文标题**: Upgrading an M4 Pro Mac mini's storage for half the price

**原文链接**: [https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price](https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price)

本文详细介绍了使用M4-SSD升级套件将M4 Pro Mac mini的内置存储从512GB升级到4TB的过程。作者逐步讲解了升级过程，强调了拆卸后盖塑料盖的棘手之处以及安装后需要进行DFU恢复。M4 Mac mini存储的独特之处在于，存储控制器集成在M4 SoC中，因此需要进行DFU恢复。

文章提到一个常见的误解，即只有Apple Silicon Mac才能执行DFU恢复，但配备T2芯片的Intel Mac甚至Hackintosh也能做到。

作者还将升级后的内置SSD与外部Thunderbolt 5 NVMe硬盘盒的性能进行了比较。内部存储表现出更优异的写入性能，这归因于其拥有更多的闪存芯片。虽然外部驱动器速度很快，但在持续传输大型文件时会出现速度减慢，这可能是由于其DRAM缓存的限制。

最终，作者得出结论，与标准NVMe SSD相比，M4-SSD升级虽然价格昂贵，但比Apple自己的存储升级选项便宜得多。文章还提供了相关内容的链接。

---

## 52. 基于硬盘指示灯活动，HDD Clicker生成硬盘咔哒声。

**原文标题**: HDD Clicker generates HDD clicking sounds, based on HDD Led activity

**原文链接**: [https://www.serdashop.com/HDDClicker](https://www.serdashop.com/HDDClicker)

此网页宣传由Serdashop销售的名为“HDD Clicker”的产品。HDD Clicker根据硬盘指示灯活动生成硬盘咔哒声。

Serdashop是一家在线商店，提供各种类别的产品，包括：

*   复古声卡
*   MIDI
*   小工具和玩具
*   视频PCB
*   操纵杆产品
*   焊接套件
*   零件
*   其他产品
*   即将推出

该网页提供购物车功能、登录/注册选项以及指向诸如首页、博物馆、通用条款、联系方式和链接等页面的链接。

当用户将“HDD Clicker”添加到其“报价单”时，他们将被重定向到报价页面以完成报价请求，Serdashop将与他们联系。所有列出的价格均包含增值税。该网站由CCV Shop提供支持。

---

## 53. 裸盖菇素展现抗衰老疗法的潜力

**原文标题**: Psilocybin shows promise as anti-aging therapy

**原文链接**: [https://neurosciencenews.com/psilocybin-longevity-aging-29425/](https://neurosciencenews.com/psilocybin-longevity-aging-29425/)

本文重点介绍埃默里大学近期发表在《npj Aging》上的一项研究，该研究表明，裸盖菇素具有作为抗衰老疗法的潜力。研究人员发现，裸盖菇素的代谢产物裸盖菇碱在*体外*实验中，将人类皮肤和肺细胞的寿命延长了50%以上。对老年小鼠（相当于人类60-65岁）进行的平行*体内*实验表明，与对照组相比，接受裸盖菇素治疗的小鼠存活率提高了30%。接受治疗的小鼠还表现出改善的身体特征，如更好的毛发质量和毛发再生。

该研究表明，裸盖菇素的益处与其对衰老关键标志的影响有关，包括减少氧化应激、改善DNA修复机制和保持端粒长度。这些机制影响人类衰老和与年龄相关疾病的发生。

研究人员强调，这些发现为理解裸盖菇素的全身性影响开辟了一条新途径，因为之前的大部分研究都集中在其对大脑的影响上。他们认为，即使在小鼠的生命后期进行裸盖菇素干预，也能提高其存活率，这表明其对健康衰老具有临床意义。该研究强调，鉴于美国与其他发达国家相比令人担忧的预期寿命趋势，有必要对老年人进行进一步研究，以探索裸盖菇素在提高寿命和生活质量方面的潜力。

---

## 54. 展示HN: RULER – 轻松将强化学习应用于任何智能体

**原文标题**: Show HN: RULER – Easily apply RL to any agent

**原文链接**: [https://openpipe.ai/blog/ruler](https://openpipe.ai/blog/ruler)

展示HN：RULER – 轻松将强化学习应用于任何智能体

“展示HN：RULER – 轻松将强化学习应用于任何智能体”一文介绍了OpenPipe的工具RULER，旨在简化将强化学习 (RL) 应用于智能体开发的过程。 关键要点是，RULER旨在通过抽象化训练和部署的复杂性，使强化学习更容易用于构建和改进智能体。

RULER无需深入的强化学习专业知识或大量的代码修改，而是允许开发人员定义他们的智能体和奖励函数，然后利用强化学习自动优化智能体的行为。 这意味着您可以通过简单地定义适当的奖励，而无需重写智能体的核心逻辑，就有可能提高现有智能体的性能。

这篇文章很可能强调了以下功能：

*   **易于集成：** 将RULER集成到现有智能体架构中所需的最小代码更改。
*   **简化训练：** 自动化强化学习训练过程，处理算法选择、超参数调整和基础设施管理的复杂性。
*   **清晰的奖励定义：** 侧重于允许开发人员轻松定义适当的奖励函数来指导智能体的学习。
*   **OpenPipe集成：** 很可能利用 OpenPipe 平台来管理实验、跟踪性能和部署训练有素的智能体。

本质上，RULER承诺普及强化学习在智能体开发中的应用，使所有技能水平的开发人员都能更轻松地利用强化学习的力量来构建更智能、更高效的智能体。

---

## 55. GeoArrow 和 GeoParquet，以及地理空间数据分析的未来

**原文标题**: GeoArrow and GeoParquet, and the Future of Geospatial Data Analysis

**原文链接**: [https://cloudnativegeo.org/blog/2024/12/interview-with-kyle-barron-on-geoarrow-and-geoparquet-and-the-future-of-geospatial-data-analysis/](https://cloudnativegeo.org/blog/2024/12/interview-with-kyle-barron-on-geoarrow-and-geoparquet-and-the-future-of-geospatial-data-analysis/)

凯尔·巴伦，Development Seed 的云工程师，探讨了他进入地理空间数据分析领域的历程以及 GeoParquet 和 GeoArrow 的重要性。他的兴趣源于在网络浏览器中可视化大型地理空间数据集，旨在使更多人能够访问地理空间数据。

GeoParquet 和 GeoArrow 被强调为加速处理大型地理空间数据集的工具。 GeoParquet 是一种用于存储地理空间矢量数据的文件格式，构建于 Parquet 格式之上，可实现云原生数据访问、高效压缩以及与 GeoArrow 等技术的集成。 GeoParquet 中的空间分区允许基于空间过滤器获取特定的数据行，从而在索引效率和索引大小之间进行权衡。

另一方面，GeoArrow 是一种在内存中表示地理空间矢量数据的方法，有助于实现高效操作和程序之间快速数据共享。它与 GeoParquet 无缝集成，提高了读写速度。文章强调了 GeoParquet 的云原生功能如何增强用户能力并释放超越传统地理空间分析的可能性。

展望未来，巴伦设想了一个通过混合系统访问和处理地理空间数据的未来，利用本地和基于云的资源。他正在开发基于浏览器的系统，该系统可以智能地决定要下载哪些数据源，旨在在交互式地图上实现高效渲染。

巴伦强调了学习新技能时动机的重要性以及明确最终目标的重要性。他还强调了注重细节和超越自我价值的重要性，即使在额外努力可能不会立即显现的任务中也是如此。他将自己徒步太平洋山脊步道的经历以及地理空间社区中各种人士的影响归功于塑造其职业生涯的重要因素。

---

## 56. 百万乘百万

**原文标题**: Million Times Million

**原文链接**: [https://susam.net/million-times-million.html](https://susam.net/million-times-million.html)

苏山·帕尔的《百万次的百万》探讨了命名大数时采用的长短尺度之间的差异，重点关注了他童年所学与现代科技世界所用惯例之间的差异。帕尔在成长过程中使用长尺度，其中“十亿”、“万亿”和“百京”等名称分别直接对应于一百万自乘两次、三次和五次。他觉得这个系统直观且合乎逻辑。

然而，进入大学并接触计算机和互联网后，他发现短尺度占据主导地位。在这个系统中，一百万次的一百万是万亿，一百万自乘三次变成百京，这与他已建立的理解产生了不协调的差异。

帕尔详细描述了他如何适应短尺度，通过将前缀解释为附加在1000上的千的个数，表示为\(1000 \times 1000^n\)或\(10^{3(n + 1)}\)，从而找到了一种使其合理化的方法。他提供了一个表格，比较了长短尺度，突出了相同名称所代表的量级之间日益扩大的差异。

尽管由于短尺度在技术、金融和英语语境中的流行，现在完全使用短尺度，但帕尔仍然表达了对长尺度的优雅及其在童年记忆中的地位的依恋。

---

## 57. 比尔·阿特金森的迷幻用户界面

**原文标题**: Bill Atkinson's psychedelic user interface

**原文链接**: [https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill](https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill)

无法访问文章链接。

---

## 58. 不良行为者正在训练大型语言模型来产生虚假信息

**原文标题**: Bad Actors Are Grooming LLMs to Produce Falsehoods

**原文链接**: [https://americansunlight.substack.com/cp/168074209](https://americansunlight.substack.com/cp/168074209)

无法访问文章链接。

---

## 59. 宾州众议院通过“一键取消”订阅法案

**原文标题**: Pa. House passes 'click-to-cancel' subscription bills

**原文链接**: [https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html](https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html)

宾夕法尼亚州众议院通过两项旨在简化订阅取消的法案，与联邦“点击取消”规则类似，但该规则最近因程序问题被联邦上诉法院推翻。其中一项法案针对“否定性选择”协议，要求企业在订阅自动续订前通知消费者，并允许他们使用与注册时相同的方式选择退出。第二项法案规定，在线订阅必须可以在线取消。

众议员乔·西雷西是其中一项法案的发起人，他强调，鉴于联邦政府的挫折，州一级的行动至关重要。他说，该立法源于选民在取消订阅过程中遇到的困难。众议员丽莎·博罗夫斯基是另一项法案的发起人，她说该法案旨在确保企业提供价值，而不是依赖消费者忘记取消不需要的订阅。

这些法案获得了两党支持，但排除受州公共事业委员会或联邦通信委员会监管的服务，以及健身房（尽管这可能会被修改）。如果获得参议院通过并由州长乔什·夏皮罗签署，宾夕法尼亚州将加入纽约、加利福尼亚和弗吉尼亚等州，制定类似的关于订阅服务的消费者保护法。

---

## 60. 苹果大战法律

**原文标题**: Apple vs the Law

**原文链接**: [https://formularsumo.co.uk/blog/2025/apple-vs-the-law/](https://formularsumo.co.uk/blog/2025/apple-vs-the-law/)

本文详细介绍了作者在布鲁塞尔参加苹果和谷歌数字市场法案（DMA）合规研讨会的经历。 DMA是一项欧盟法律，旨在防止指定“守门人”的反竞争行为，要求他们与竞争对手互操作。

作者认为苹果公司的态度具有对抗性和不尊重性，侧重于该法律对他们的不公平，并使用暗示他们是唯一目标的措辞。 苹果公司的代表经常提到他们对法律的解释，暗示它过于极端，并承诺“积极捍卫”他们的权利。 谷歌的态度较为缓和，但他们也对该法律的难度以及对消费者可能造成的损害表示担忧。

作者批评了苹果公司阻挠监管的历史，以及他们拖延或挑战调查的倾向。 他指出，与欧盟委员会相比，苹果和谷歌拥有巨大的资源，这意味着他们有能力浪费时间并支付罚款，同时维持垄断利润。

研讨会上提出的具体问题包括：苹果公司繁琐的追踪系统、他们坚持对所有应用程序进行人工审核、缺乏显眼的诈骗举报按钮、对第三方浏览器引擎的限制（要求重新获取用户）、迫使某些用户使用Safari的年龄限制，以及非欧盟开发者无法在iOS上测试第三方浏览器引擎。

作者还指出，苹果公司一方面抱怨竞争对手在场，另一方面却有未公开的、由苹果资助的与会者在场，这显然是虚伪的。 最后，作者认为应取消苹果公司对第三方浏览器和应用商店的地域限制，以允许全球访问，并促进DMA原则的更广泛采用。 他们认为，要使此类监管取得成功，相同的条款需要在所有司法管辖区适用。

---

## 61. 某人创造1840亿枚比特币之日 (2020)

**原文标题**: The day someone created 184 billion Bitcoin (2020)

**原文链接**: [https://decrypt.co/39750/184-billion-bitcoin-anonymous-creator](https://decrypt.co/39750/184-billion-bitcoin-anonymous-creator)

提供的文本并非文章，而是一份加密货币价格快照。它列出了各种加密货币，包括比特币（BTC）、以太坊（ETH）、瑞波币（XRP）、币安币（BNB）、索拉纳币（SOL）、狗狗币（DOGE）以及许多其他币种。

对于每种加密货币，列表显示其当前价格以及在特定时间段内（大概是24小时）的百分比变化。价格会有波动，一些加密货币显示上涨（正百分比变化），而另一些则经历下跌（负百分比变化）。

需要注意的是，标题“某人在一天内创造了 1840 亿枚比特币（2020 年）”与内容完全无关。内容是当前价格列表，没有提及比特币的创建或 2020 年的任何特定事件。

---

## 62. 出狱第一年 (2020)

**原文标题**: The First Year Out of Prison (2020)

**原文链接**: [https://www.marieclaire.com/politics/a32630854/prison-release-recidivism/](https://www.marieclaire.com/politics/a32630854/prison-release-recidivism/)

本文讲述了梅克达·戴维斯的故事，她最近因袭击罪在贝德福德山惩教所服刑七年半后获释，记录了她重返社会的第一年所面临的挑战。文章重点介绍了她与母亲乔治亚和女儿梅尔汉达重逢时的激动之情，以及梅克达最初对世界快速变化的震惊。

文章详细描述了梅克达面临的诸多障碍，包括经济困难、破碎的家庭关系、缺乏稳定的住房，以及因犯罪记录和过时技能而难以找到工作。她还努力应对监禁带来的心理影响，感到不知所措和力不从心。

文章探讨了阻碍前囚犯成功重返社会的系统性问题，例如监狱内接受教育和职业培训的机会有限、贫困和监禁的恶性循环，以及缺乏足够的支援服务。梅克达向财富协会寻求帮助，该协会是一家非营利组织，提供诸如就业安置、法律援助和获得公共援助等资源。

尽管面临这些挑战，梅克达仍然决心重建她的生活，重拾她的事业，并成为她女儿的支持性母亲。文章描绘了她的韧性以及她在出狱后努力应对复杂现实的挣扎，强调了全面重返社会计划和社会支持对于确保前囚犯成功融入社会的必要性。

---

## 63. 我不用社交媒体了——或者：为什么我现在有了博客

**原文标题**: I'm done with social media – Or: why I have a blog now

**原文链接**: [https://www.carolinecrampton.com/im-done-with-social-media/](https://www.carolinecrampton.com/im-done-with-social-media/)

作者详细描述了其2024年利用社交媒体推广其书籍《玻璃之躯》的失败尝试。由于对销售一本融合多种类型且具个人色彩的书籍感到焦虑，他们大量投资于社交媒体策略，参加培训课程，创建内容日历，并为Instagram和TikTok拍摄视频。

然而，他们很快就感到幻灭。他们发现持续的拍摄和内容创作既不真实，也扰乱了他们的个人生活。更重要的是，这些努力收效甚微；算法忽略了他们的内容，受众参与度仍然很低。尽管出版专业人士提供了建议，但他们的社交媒体影响力并未转化为书籍销量的增长。

他们意识到社交媒体的成功需要与写作截然不同的技能，并怀疑行业推动作者积极参与社交媒体是一种转移图书推广责任的方式。作者批评“创作者经济”是一种有利于大型企业的金字塔骗局，并质疑向这些平台提供免费内容的价值。

最终，作者得出结论，社交媒体对他们而言不是一个可行的推广工具。他们反思了自己长期以来对社交媒体的矛盾心理，并重申了退出这些平台的决定，认为直接与读者互动（通过活动和电子邮件通讯）更为有效。作者正准备开始写博客。

---

## 64. “123456”密码泄露6400万麦当劳求职者聊天记录

**原文标题**: '123456' password exposed chats for 64M McDonald's job applicants

**原文链接**: [https://www.bleepingcomputer.com/news/security/123456-password-exposed-chats-for-64-million-mcdonalds-job-applicants/](https://www.bleepingcomputer.com/news/security/123456-password-exposed-chats-for-64-million-mcdonalds-job-applicants/)

安全研究人员发现麦当劳McHire聊天机器人招聘平台存在漏洞，导致美国超过6400万份求职申请的聊天记录泄露。该漏洞源于平台管理面板使用弱默认凭据（“123456”：“123456”）以及API端点中的不安全直接对象引用（IDOR）。通过操纵API请求中的“lead_id”参数，研究人员能够访问敏感数据，包括聊天记录、会话令牌以及求职者的个人信息。

该漏洞于2025年6月30日报告给Paradox.ai（平台提供商）和麦当劳。麦当劳确认了该问题，并将其归因于Paradox.ai。弱凭据很快被禁用，Paradox当天部署了修复程序以解决IDOR漏洞。Paradox.ai正在审查其系统，以防止将来发生类似事件。泄露的数据包括任何聊天机器人互动，例如按钮点击，无论是否输入个人信息。此安全问题突显了Web应用程序中弱凭据和IDOR漏洞的风险，以及发现后及时补救的重要性。

---

## 65. Show HN: Pangolin - Cloudflare Tunnels 的开源替代方案

**原文标题**: Show HN: Pangolin – Open source alternative to Cloudflare Tunnels

**原文链接**: [https://github.com/fosrl/pangolin](https://github.com/fosrl/pangolin)

Pangolin：一款开源自托管的Cloudflare Tunnels替代方案，提供一种安全的方式，无需开放端口即可在分布式网络上暴露私有资源。它使用WireGuard隧道进行连接，从而能够访问防火墙后的远程服务。主要功能包括反向代理、通过Let's Encrypt自动生成SSL证书、负载均衡以及对HTTP/HTTPS和TCP/UDP服务的支持。

Pangolin拥有一个集中式认证系统，支持平台SSO、TOTP、电子邮件白名单、临时共享链接、资源专用PIN码/密码以及与Authentik和Okta等外部身份提供商 (IdP) 的集成。它提供基于角色的访问控制和来自IdP的用户/角色自动配置，并通过具有亮/暗模式的用户友好型仪表板进行管理。

使用Docker Compose和一个设置脚本简化了部署，从而可以轻松地与现有基础设施集成。用户可以使用任何WireGuard客户端或Pangolin的自定义客户端Newt进行连接。该系统提供一个具有细粒度访问控制和Swagger文档的API。

Pangolin强调模块化设计，可以通过CrowdSec等Traefik插件进行扩展。它突出了诸如绕过家庭实验室中的端口限制、部署商业服务和管理物联网网络等用例。它的灵感来自Cloudflare Tunnels和Authelia。

该项目正在大力开发中，路线图可能会发生变化，并采用AGPL-3和Fossorial商业许可双重许可。鼓励通过GitHub存储库进行贡献和反馈。

---

## 66. 上月太阳能首次成为欧洲最大电力来源

**原文标题**: In a First, Solar Was Europe's Biggest Source of Power Last Month

**原文链接**: [https://e360.yale.edu/digest/solar-biggest-power-source-europe-june-2025](https://e360.yale.edu/digest/solar-biggest-power-source-europe-june-2025)

六月份，太阳能首次成为欧盟最大的电力来源，提供了创纪录的22%的电力。至少有13个国家/地区的太阳能发电量创下月度新高。太阳能的崛起帮助欧洲应对了严重的酷暑，因为在空调需求最高时，太阳能供应充足，缓解了电网的压力。

核能是第二大电力来源，其次是风能、天然气和水力发电。煤炭发电量降至月度新低，仅占发电量的6%。目前已有15个欧盟国家不使用煤炭。

分析师强调了太阳能在缓解气候变化加剧的酷暑影响方面的重要性。一项研究发现，化石燃料的燃烧使与酷暑相关的死亡人数增加了两倍。

---

## 67. Bootstrapping a side project into a profitable seven-figure business

**原文标题**: Bootstrapping a side project into a profitable seven-figure business

**原文链接**: [https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding](https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding)

凯尔·诺兰在四年内将财务规划工具ProjectionLab从一个副业发展成为年收入100万美元的企业。受到财务自由运动的启发，他最初是为自己的需求构建了这个工具。关键里程碑包括在Hacker News上获得早期关注，获得Mr. Money Mustache的认可，并最终辞去公司工作全身心投入ProjectionLab。

这段旅程并非一帆风顺；诺兰将其描述为一场充满高潮、低谷和自我怀疑的情感过山车。他强调坚持不懈("不放弃")是一种超能力，并强调了与你喜欢的人一起工作的价值。

最初是一名独立开发者，诺兰意识到需要一个增长伙伴。他引进了Jon Kuipers来负责营销和运营，后者已经证明了自己的价值。他们还从ProjectionLab用户社区中增加了承包商来处理客户成功，优先考虑强大的用户体验而非削减成本。

诺兰认为一致性是他们成功的关键因素，他敦促有抱负的创业者“坚持下去”，即使增长缓慢或令人沮丧。他最后强调了构建优质产品、保持精简和以客户为中心，以及构建可持续性而非追逐潮流的重要性。他和团队现在专注于加倍实践这些价值观，以继续ProjectionLab的增长。

---

## 68. 戴森球计划 – 开发者日志 – 全新多线程框架

**原文标题**: Dyson Sphere Program – Dev Log – The New Multithreading Framework

**原文链接**: [https://store.steampowered.com/news/app/1366540/view/543361383085900510](https://store.steampowered.com/news/app/1366540/view/543361383085900510)

This "Dyson Sphere Program – Dev Log – The New Multithreading Framework" isn't really an article, but rather a partial listing of interface elements within the Steam platform. It's a context menu offering language options. Therefore, there isn't a main point or key information about a "new multithreading framework" to summarize. The title is misleading in the context of the presented content. The content lists a variety of languages available for the Steam client and indicates standard navigation elements like store, home, news, community, and account management links.


---

## 69. 有史以来最大的数码相机是这位宇宙学家的杰作

**原文标题**: The Biggest-Ever Digital Camera Is This Cosmologist's Magnum Opus

**原文链接**: [https://www.quantamagazine.org/the-biggest-ever-digital-camera-is-this-cosmologists-magnum-opus-20250711/](https://www.quantamagazine.org/the-biggest-ever-digital-camera-is-this-cosmologists-magnum-opus-20250711/)

生成摘要时出错

---

## 70. "high level" languages are easier to optimize

**原文标题**: "high level" languages are easier to optimize

**原文链接**: [https://jyn.dev/high-level-languages-are-easier-to-optimize/](https://jyn.dev/high-level-languages-are-easier-to-optimize/)

生成摘要时出错

---

## 71. Overtourism in Japan, and how it hurts small businesses

**原文标题**: Overtourism in Japan, and how it hurts small businesses

**原文链接**: [https://craigmod.com/ridgeline/210/](https://craigmod.com/ridgeline/210/)

生成摘要时出错

---

## 72. America's largest power grid is struggling to meet demand from AI

**原文标题**: America's largest power grid is struggling to meet demand from AI

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/americas-largest-power-grid-is-struggling-meet-demand-ai-2025-07-09/](https://www.reuters.com/sustainability/boards-policy-regulation/americas-largest-power-grid-is-struggling-meet-demand-ai-2025-07-09/)

生成摘要时出错

---

## 73. The death of partying in the USA

**原文标题**: The death of partying in the USA

**原文链接**: [https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand](https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand)

生成摘要时出错

---

## 74. AMD's Magny Cours and HyperTransport Interconnect

**原文标题**: AMD's Magny Cours and HyperTransport Interconnect

**原文链接**: [https://chipsandcheese.com/p/amds-magny-cours-and-hypertransport](https://chipsandcheese.com/p/amds-magny-cours-and-hypertransport)

生成摘要时出错

---

## 75. Before Tragedy, Texas Repeatedly Rejected Pleas for Flood Alarm Funding

**原文标题**: Before Tragedy, Texas Repeatedly Rejected Pleas for Flood Alarm Funding

**原文链接**: [https://www.nytimes.com/2025/07/10/us/politics/texas-flood-alarm-system.html](https://www.nytimes.com/2025/07/10/us/politics/texas-flood-alarm-system.html)

生成摘要时出错

---

## 76. LLM Inference Handbook

**原文标题**: LLM Inference Handbook

**原文链接**: [https://bentoml.com/llm/](https://bentoml.com/llm/)

生成摘要时出错

---

## 77. The ChompSaw: A benchtop power tool that's safe for kids to use

**原文标题**: The ChompSaw: A benchtop power tool that's safe for kids to use

**原文链接**: [https://www.core77.com/posts/137602/The-ChompSaw-A-Benchtop-Power-Tool-Thats-Safe-for-Kids-to-Use](https://www.core77.com/posts/137602/The-ChompSaw-A-Benchtop-Power-Tool-Thats-Safe-for-Kids-to-Use)

生成摘要时出错

---

## 78. Xenharmlib: A music theory library that supports non-western harmonic systems

**原文标题**: Xenharmlib: A music theory library that supports non-western harmonic systems

**原文链接**: [https://xenharmlib.readthedocs.io/en/latest/](https://xenharmlib.readthedocs.io/en/latest/)

生成摘要时出错

---

## 79. Recovering from AI addiction

**原文标题**: Recovering from AI addiction

**原文链接**: [https://internetaddictsanonymous.org/internet-and-technology-addiction/signs-of-an-addiction-to-ai/](https://internetaddictsanonymous.org/internet-and-technology-addiction/signs-of-an-addiction-to-ai/)

生成摘要时出错

---

## 80. Series of posts on HTTP status codes (2018)

**原文标题**: Series of posts on HTTP status codes (2018)

**原文链接**: [https://evertpot.com/http/](https://evertpot.com/http/)

生成摘要时出错

---

## 81. Grok: Searching X for "From:Elonmusk (Israel or Palestine or Hamas or Gaza)"

**原文标题**: Grok: Searching X for "From:Elonmusk (Israel or Palestine or Hamas or Gaza)"

**原文链接**: [https://simonwillison.net/2025/Jul/11/grok-musk/](https://simonwillison.net/2025/Jul/11/grok-musk/)

生成摘要时出错

---

## 82. Btrfs Allocator Hints

**原文标题**: Btrfs Allocator Hints

**原文链接**: [https://lwn.net/ml/all/cover.1747070147.git.anand.jain@oracle.com/](https://lwn.net/ml/all/cover.1747070147.git.anand.jain@oracle.com/)

生成摘要时出错

---

## 83. Threads is nearing X's daily app users, new data shows

**原文标题**: Threads is nearing X's daily app users, new data shows

**原文链接**: [https://techcrunch.com/2025/07/07/threads-is-nearing-xs-daily-app-users-new-data-shows/](https://techcrunch.com/2025/07/07/threads-is-nearing-xs-daily-app-users-new-data-shows/)

生成摘要时出错

---

## 84. Orwell Diaries 1938-1942

**原文标题**: Orwell Diaries 1938-1942

**原文链接**: [https://orwelldiaries.wordpress.com/page/2/](https://orwelldiaries.wordpress.com/page/2/)

生成摘要时出错

---

## 85. Measuring the impact of AI on experienced open-source developer productivity

**原文标题**: Measuring the impact of AI on experienced open-source developer productivity

**原文链接**: [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

生成摘要时出错

---

## 86. The Ghost of Muriel Spark

**原文标题**: The Ghost of Muriel Spark

**原文链接**: [https://www.newstatesman.com/culture/books/2025/06/the-ghost-of-muriel-spark](https://www.newstatesman.com/culture/books/2025/06/the-ghost-of-muriel-spark)

生成摘要时出错

---

## 87. FP8 is ~100 tflops faster when the kernel name has "cutlass" in it

**原文标题**: FP8 is ~100 tflops faster when the kernel name has "cutlass" in it

**原文链接**: [https://twitter.com/cis_female/status/1943069934332055912](https://twitter.com/cis_female/status/1943069934332055912)

生成摘要时出错

---

## 88. I'm more proud of these 128 kilobytes than anything I've built since

**原文标题**: I'm more proud of these 128 kilobytes than anything I've built since

**原文链接**: [https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18](https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18)

生成摘要时出错

---

## 89. AI agent benchmarks are broken

**原文标题**: AI agent benchmarks are broken

**原文链接**: [https://ddkang.substack.com/p/ai-agent-benchmarks-are-broken](https://ddkang.substack.com/p/ai-agent-benchmarks-are-broken)

生成摘要时出错

---

## 90. Underwater turbine spinning for 6 years off Scotland's coast is a breakthrough

**原文标题**: Underwater turbine spinning for 6 years off Scotland's coast is a breakthrough

**原文链接**: [https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6](https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6)

生成摘要时出错

---

## 91. eBPF: Connecting with Container Runtimes

**原文标题**: eBPF: Connecting with Container Runtimes

**原文链接**: [https://h0x0er.github.io/blog/2025/06/29/ebpf-connecting-with-container-runtimes/](https://h0x0er.github.io/blog/2025/06/29/ebpf-connecting-with-container-runtimes/)

生成摘要时出错

---

## 92. Infinite Mac Construction Set

**原文标题**: Infinite Mac Construction Set

**原文链接**: [https://blog.persistent.info/2025/07/infinite-mac-embedding.html](https://blog.persistent.info/2025/07/infinite-mac-embedding.html)

生成摘要时出错

---

## 93. The price of software freedom is eternal politics

**原文标题**: The price of software freedom is eternal politics

**原文链接**: [https://www.theregister.com/2025/07/12/the_price_of_software_freedom/](https://www.theregister.com/2025/07/12/the_price_of_software_freedom/)

生成摘要时出错

---

## 94. DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Gen

**原文标题**: DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Gen

**原文链接**: [https://arxiv.org/abs/2506.20639](https://arxiv.org/abs/2506.20639)

生成摘要时出错

---

## 95. Epstein's Unredacted Black Book

**原文标题**: Epstein's Unredacted Black Book

**原文链接**: [https://archive.org/details/jeffrey-epstein-39s-little-black-book-unredacted](https://archive.org/details/jeffrey-epstein-39s-little-black-book-unredacted)

生成摘要时出错

---

## 96. Gut microbes could protect us from toxic 'forever chemicals'

**原文标题**: Gut microbes could protect us from toxic 'forever chemicals'

**原文链接**: [https://www.cam.ac.uk/research/news/gut-microbes-could-protect-us-from-toxic-forever-chemicals](https://www.cam.ac.uk/research/news/gut-microbes-could-protect-us-from-toxic-forever-chemicals)

生成摘要时出错

---

## 97. Postgres LISTEN/NOTIFY does not scale

**原文标题**: Postgres LISTEN/NOTIFY does not scale

**原文链接**: [https://www.recall.ai/blog/postgres-listen-notify-does-not-scale](https://www.recall.ai/blog/postgres-listen-notify-does-not-scale)

生成摘要时出错

---

## 98. Operational Apple-1 Computer for sale [video]

**原文标题**: Operational Apple-1 Computer for sale [video]

**原文链接**: [https://www.youtube.com/watch?v=XdBKuBhdZwg](https://www.youtube.com/watch?v=XdBKuBhdZwg)

生成摘要时出错

---

## 99. Batch Mode in the Gemini API: Process More for Less

**原文标题**: Batch Mode in the Gemini API: Process More for Less

**原文链接**: [https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/)

生成摘要时出错

---

## 100. Diving into Plasma Bigscreen

**原文标题**: Diving into Plasma Bigscreen

**原文链接**: [https://espi.dev/posts/2025/07/plasma-bigscreen/](https://espi.dev/posts/2025/07/plasma-bigscreen/)

生成摘要时出错

---

