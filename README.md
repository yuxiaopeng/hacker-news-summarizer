# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-01.md)

*最后自动更新时间: 2025-07-01 17:50:48*
## 1. 美联储称这是一个价值一百万美元的立方体，他们算错了，差了五十万。

**原文标题**: The Fed says this is a cube of $1M. They're off by half a million

**原文链接**: [https://calvin.sh/blog/fed-lie/](https://calvin.sh/blog/fed-lie/)

作者幽默地讲述了其调查芝加哥联邦储备银行货币博物馆中“百万美元”立方体展示的经历。作者怀疑标牌上声称该立方体包含整整1,000,000美元的说法，试图清点钞票堆，但发现极具挑战性。由于缺乏现成的图像对象计数工具，作者创建了一个名为“Dot Counter”的简单Web应用程序。

利用Dot Counter，作者仔细数了立方体照片中可见的钞票堆，并根据每捆100张钞票的假设计算了其价值。结果令人惊讶，为1,550,400美元，比声称的数额高出惊人的550,400美元。

文章风趣地探讨了造成差异的各种解释，考虑了立方体是空心的，或是经过策略性填充以显得更有价值等情况。然后，文章深入探讨了由于钞票的尺寸，使用美国货币创建一个真正的立方体的难度，并提出了另一种配置方案。

最终，作者得出结论，该立方体要么包含100万美元，要么包含155万美元，要么就是一个幻觉。主要的收获是以幽默的方式展示了质疑声明和验证信息的重要性，即使这些信息是由官方机构提供的，并且使用了作者新开发的Dot Counter。作者鼓励读者使用该工具来满足他们自己的计数需求。

---

## 2. 探访赛德娜任务可行性研究 - 核动力推进与太阳帆

**原文标题**: Feasibility study of a mission to Sedna - Nuclear propulsion and solar sailing

**原文链接**: [https://arxiv.org/abs/2506.17732](https://arxiv.org/abs/2506.17732)

2025年arXiv论文《前往赛德娜的任务可行性研究——核动力推进与先进太阳帆概念》探讨了使用先进推进方法抵达赛德娜的可行性。作者Elena Ancona、Roman Ya. Kezerashvili和Savino Longo对比了直接聚变驱动（DFD）火箭发动机和利用热脱附的太阳帆。

该研究提出了一项单向地球到赛德娜的任务，其中DFD用于轨道插入，太阳帆则设想用于飞掠。它评估了有效载荷能力、旅行时间和两种推进系统的潜在科学回报等关键参数。DFD被建模为具有恒定推力的1.6兆瓦系统，而太阳帆则结合了热脱附和木星引力辅助。

任务分析分为四个阶段：出发、行星际加速、行星际滑行和交会。由于赛德娜在2075-2076年接近近日点，因此时间安排至关重要。结果表明，DFD可以在大约10年内到达赛德娜，其中推进时间为1.5年。借助木星的辅助，太阳帆可以在7年内完成旅程。

该论文还探讨了容纳科学载荷、电力可用性和通信约束的可行性。该研究提供了一项比较分析，以帮助未来的深空任务规划。

---

## 3. Show HN: Spegel，一款使用LLM重写网页的终端浏览器

**原文标题**: Show HN: Spegel, a Terminal Browser That Uses LLMs to Rewrite Webpages

**原文链接**: [https://simedw.com/2025/06/23/introducing-spegel/](https://simedw.com/2025/06/23/introducing-spegel/)

Spegel：一个使用LLM重写网页并在终端中以Markdown渲染的概念验证终端Web浏览器。作为一个周末项目开发，并受到谷歌更快的Gemini 2.5 Pro Lite发布的推动，Spegel旨在通过自定义提示将其适配到个人需求，从而提供个性化的网页内容视图。

其核心思想是解决在终端中查看现代网站时存在的混乱和干扰。 Spegel获取HTML，通过LLM使用用户在配置文件中定义的提示对其进行处理，并通过Textual库输出渲染的Markdown。 用户可以创建单个页面的多个“视图”，例如简化内容 (ELI5) 或突出显示关键操作，并且可以在浏览会话期间调整提示。

作者分享了一个提取食谱基本部分的示例配置，展示了转换内容以适应特定需求的能力。 该浏览器目前仅支持GET请求，但未来的计划包括处理表单和POST请求。 虽然承认存在其他终端浏览器，如Lynx和Browsh，但Spegel通过利用LLM更紧密地根据用户需求定制内容而脱颖而出。

Spegel可通过pip安装 (`pip install spegel`)，并且需要一个配置文件。 源代码可在GitHub上获取，欢迎贡献。

---

## 4. 将数学软件包转换为C++20模块的经验 [PDF]

**原文标题**: Experience converting a mathematical software package to C++20 modules [PDF]

**原文链接**: [https://arxiv.org/abs/2506.21654](https://arxiv.org/abs/2506.21654)

将大型C++数学软件包转换为C++20模块的经验
        
这篇arXiv论文，题为“将大型C++数学软件包转换为C++20模块的经验”，探讨了将一个重要的C++数学软件库，特别是deal.II（约80万行代码），迁移到C++20模块系统的过程。作者Wolfgang Bangerth详细介绍了一种同时支持传统基于头文件的接口和新的基于模块的方法。

该论文讨论了转换过程中遇到的挑战，并深入了解了C++20模块在实际场景中的运作方式。作者基于编译时间和易用性等人为因素等技术指标评估了该模块系统。

该研究的结论是，将大型C++代码库转换为模块是可行的，但需要付出相当大的努力。虽然转换后的库本身的编译时间有所改善，但下游项目在编译时间变化方面没有显示出一致的趋势。该论文最后提出了长期战略，以便在未来几年内将数学软件生态系统更广泛地过渡到C++20模块。这项工作为考虑在大型项目中采用C++20模块的开发人员贡献了实践经验和见解。

---

## 5. 我做了个东西，改变了我们朋友圈的社交结构。

**原文标题**: I built something that changed my friend group's social fabric

**原文链接**: [https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/](https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/)

2022年，作者的朋友们分散在世界各地，他们使用混乱的Signal群聊努力保持联系和组织游戏。为了解决这个问题，作者构建了一个Discord机器人，每当有人加入Discord服务器中的语音频道时，该机器人就会向指定的文本频道发送通知。这个简单的解决方案就像一个“蝙蝠信号”，提醒所有人何时有人可以聊天或玩游戏。

最初，该机器人褒贬不一，但很快就改变了群体的社交动态。它减少了群聊中不断协调的需求，并鼓励了自发的社交互动，许多成员仅仅为了快速聊天而加入Discord，让人想起过去的电话。作者多年来追踪Discord的使用情况，发现活动量持续增加，即使是那些现在30多岁并有家庭责任的朋友也是如此。该机器人促进了快速的问候，并在忙碌的生活中提供了一种连接感。

作者现在为他们的年度圣诞派对制作一个“Discord年度回顾”，分享个性化的统计数据和排行榜，以回顾一年的在线活动。未来的计划包括添加成就、跟踪在Discord中花费的时间，并可能创建一个带有颜色编码灯的物联网设备，以指示特定朋友何时加入Discord语音频道。作者正在考虑将该设备变成真正的产品。

---

## 6. Cua (YC X25) 招聘创始工程师

**原文标题**: Cua (YC X25) Is Hiring a Founding Engineer

**原文链接**: [https://www.ycombinator.com/companies/cua/jobs/dIskIB1-founding-engineer-cua-yc-x25](https://www.ycombinator.com/companies/cua/jobs/dIskIB1-founding-engineer-cua-yc-x25)

Cua (YC X25) 招聘创始工程师，该公司致力于构建人工智能代理安全且可扩展地使用计算机和应用程序的基础设施。他们提供开源框架、用于代理执行的云容器平台以及生产级代理系统的蓝图。

创始工程师将负责交付驱动代理工作负载的基础设施、塑造开源社区、贡献于产品战略并推广该平台。

理想的候选人应具有扎实的系统背景、扩展基础设施和保护容器的经验，以及对设计简单API的热情。要求包括计算机科学学士学位（或同等学历），以及2年以上后端系统经验（Python、Go、TypeScript或Rust）、熟悉LLM生成的代码以及应对不确定性的能力。Docker/KVM/OS虚拟化经验、多云经验、PostgreSQL优化经验以及开源贡献将是加分项。

该职位位于旧金山（混合办公优先，支持远程办公），基本工资为 10 万美元至 15 万美元，股权为 0.5% 至 0.75%。Cua 获得了 Y Combinator 和顶级投资者的支持。申请人应提供他们的 GitHub 个人资料，并附注他们解决的具有挑战性的基础设施问题，为 Cua 开源项目做出贡献者优先。

---

## 7. Show HN：人脉求职：在领英人脉中找工作

**原文标题**: Show HN: Jobs by Referral: Find jobs in your LinkedIn network

**原文链接**: [https://jobsbyreferral.com/](https://jobsbyreferral.com/)

JobsByReferral是一个工具，帮助用户在LinkedIn等平台上，通过职业人脉网络寻找职位空缺。它分析用户的联系人数据，识别出用户拥有人脉的公司，从而增加他们获得内推和面试的机会。

该过程包括三个步骤：首先，用户必须提供他们的联系人数据，可以通过上传数据存档（例如LinkedIn的ZIP文件）或符合特定格式的CSV文件（需要包括名字、姓氏、公司、职位）来实现。其次，该工具会分析人脉网络，找出拥有最多联系人的公司。第三，用户可以搜索相关职位并查看结果，利用他们的人脉进行内推。

该平台提供了一个演示CSV文件，供希望在上传自己的数据之前测试服务的用户使用，让他们体验该功能并了解其工作原理。

---

## 8. Show HN: HackerNewt - iOS 平台的广度优先 HN 探索客户端

**原文标题**: Show HN: HackerNewt - Breadth-first exploring HN client for iOS

**原文链接**: [https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970](https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970)

HackerNewt：一款旨在改善 Hacker News 阅读体验的 iOS 应用。它以广度优先的方式呈现评论，避免了传统界面中评论宽度逐渐变窄的问题。用户可以通过滑动和滚动轻松浏览讨论，保持上下文，并跳过不感兴趣的子树。

主要功能包括自定义版块、搜索（包括线程内搜索）、锚点、阅读列表和最近项目。该应用免费，但提供应用内购买，用于打赏和购买高级版本。

用户评价大多为正面，平均评分为 4.6 星（满分 5 星）。最近一条负面评论指出该应用无法加载，开发者迅速解决了该问题，并且还积极回应了一位不确定如何在帖子中发表评论的用户。

开发者声称该应用不收集任何数据。它需要 iOS 15.0 或更高版本，并且与 iPhone 和 iPod Touch 兼容。该应用被归类为新闻类，并且由于可能接触到成人主题、亵渎性语言以及毒品/酒精内容，因此评级为 17+。

---

## 9. 大自然何时焕发绚丽色彩？

**原文标题**: When Did Nature Burst into Vivid Color?

**原文链接**: [https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/](https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/)

《量子杂志》文章“自然界何时迸发出鲜艳的色彩？”探讨了自然界中色彩视觉和鲜艳色彩信号的进化时间线。进化生物学家 Zachary Emberts 和 John Wiens 重建了 5 亿年的进化历史，结合化石记录和系统发育树，以研究色彩视觉是在鲜艳色彩信号（例如，鲜亮的水果、花朵、求偶色）之前还是之后进化而来。

他们的研究表明，色彩视觉的进化早于鲜艳色彩信号，可能在 4 亿到 5 亿年前，发生在节肢动物和脊椎动物中。鲜艳色彩信号的出现紧随其后：大约在 3 亿年前，水果和种子中出现了独特的颜色，随后是色彩鲜艳的花朵、警戒色（大约在 1.3 亿年前），最后是动物的性信号（大约在 1 亿年前）。

文章承认了重建如此久远的进化历史所固有的不确定性，指出颜色不易形成化石，且进化树本质上具有推测性。尽管存在这些局限性，该研究仍为色彩视觉和依赖于它的信号之间的进化关系提供了宝贵的见解，表明色彩视觉最初可能具有不同的用途，之后才在检测这些信号中发挥作用。科学家们提出，早期的用途可能包括识别物体、导航，甚至改善在弱光水生环境中的视觉。

---

## 10. OpenFLOW – 在本地快速制作精美的基础设施图表

**原文标题**: OpenFLOW – Quickly make beautiful infrastructure diagrams local to your machine

**原文链接**: [https://github.com/stan-smith/OpenFLOW](https://github.com/stan-smith/OpenFLOW)

OpenFLOW是一款开源的渐进式Web应用(PWA)，使用React和Isoflow库构建，允许用户直接在Web浏览器中快速创建美观的等距基础设施图。它优先考虑用户隐私，将所有数据存储在本地，并提供离线支持以保证工作不中断。

主要功能包括等距图绘制、自动保存功能（每5秒一次）、将图表导入/导出为JSON文件以及全面的离线支持。用户可以通过拖放添加和连接组件，自定义其外观，并轻松导航画布。

图表会自动保存到浏览器的本地存储中。该应用程序还提供快速保存、保存副本、加载现有图表和管理存储空间等选项。

要在本地运行OpenFLOW，用户需要克隆GitHub存储库，使用npm安装依赖项，然后启动开发服务器。可以创建生产版本，以便部署到静态托管服务，例如GitHub Pages、Netlify和AWS S3。 PWA功能需要HTTPS。

该应用依赖于React来实现UI，TypeScript来实现类型安全，以及Isoflow库来实现等距图绘制。 欢迎贡献，该项目根据Unlicense许可发布。 Isoflow库本身根据MIT许可证发布。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 2 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 3 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 4 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 5 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 6 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 7 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 8 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 9 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 10 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 11 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 12 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 13 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 14 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 15 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 16 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 17 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 18 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 19 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 20 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 21 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 22 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 23 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 24 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 25 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 26 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 27 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 28 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 29 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 30 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 31 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 32 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 33 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 34 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 35 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 36 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 37 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 38 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 39 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 40 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 41 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 42 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 43 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 44 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 45 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 46 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 47 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 48 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 49 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 50 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 51 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 52 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 53 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 54 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 55 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 56 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 57 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 58 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 59 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 60 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 61 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 62 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 63 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 64 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 65 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 66 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 67 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 68 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 69 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 70 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 71 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 72 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 73 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 74 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 75 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 76 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 77 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 78 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 79 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 80 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 81 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 82 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 83 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 84 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 85 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 86 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 87 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 88 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 89 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 90 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 91 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 92 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 93 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 94 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 95 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 96 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 97 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 98 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 99 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 100 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 101 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 102 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 103 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 104 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
