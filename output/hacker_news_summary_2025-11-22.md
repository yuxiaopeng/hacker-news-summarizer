# Hacker News 热门文章摘要 (2025-11-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Agent设计仍然很难

**原文标题**: Agent design is still hard

**原文链接**: [https://lucumr.pocoo.org/2025/11/21/agents-are-hard/](https://lucumr.pocoo.org/2025/11/21/agents-are-hard/)

在2025年11月的博文中，Armin Ronacher 探讨了构建有效代理的持续挑战，即便在代理编码工具取得进展的情况下。他强调，代理设计仍然复杂，SDK 抽象在应用于真实世界的工具使用时会失效。

Ronacher 反对仅仅依赖像 Vercel AI SDK 这样的高级 SDK，提倡直接与平台特定的 SDK（例如 OpenAI、Anthropic）交互，以保持对抽象的控制，并更有效地处理提供商方面的工具。他赞扬了 Anthropic 的显式缓存管理，认为它比自动化系统更可预测和可控。

代理循环中的强化至关重要，它允许对工具性能、状态更改甚至通过“回声工具”进行自我强化进行反馈。隔离故障（通过子代理或上下文编辑，尽管后者仍处于实验阶段）有助于保持上下文质量并节省 tokens。

Ronacher 强调需要共享状态，例如虚拟文件系统，以促进不同工具和子代理之间的通信。他发现输出工具出乎意料地困难，难以控制语气并确保工具调用。

模型选择仍然取决于任务，Haiku 和 Sonnet 因其工具调用能力而受到主代理循环的青睐，而 Gemini 2.5 更适合用于文档摘要和图像提取等任务。至关重要的是，他强调测试和评估是最重要的挑战，需要与来自实际测试运行的可观察性数据相关联。

最后，他简要提到了试用“Amp”编码代理，赞赏其子代理交互。他以一些有趣的阅读材料作为总结，倡导更简单的浏览器代理设置，并强调了像 Tmux 这样的工具的持续相关性。

---

## 2. 新墨西哥州全美首创，向所有人开放免费托儿服务

**原文标题**: In a U.S. First, New Mexico Opens Doors to Free Child Care for All

**原文链接**: [https://www.wsj.com/us-news/in-a-u-s-first-new-mexico-opens-doors-to-free-child-care-for-all-2dfdea96](https://www.wsj.com/us-news/in-a-u-s-first-new-mexico-opens-doors-to-free-child-care-for-all-2dfdea96)

好的，以下是《华尔街日报》文章“美国首例，新墨西哥州向所有人开放免费托儿服务”的摘要，基于网上容易获得的资料以及文章标题和来源推测的内容。由于我无法直接访问链接，所以本摘要基于一般知识和预期内容。

**摘要：**

新墨西哥州正在实施一项全民免费托儿计划，成为美国第一个这样做的州。这项计划旨在让所有家庭，无论收入如何，都能获得托儿服务。该项目由州和联邦资金共同资助，包括来自该州石油和天然气行业的收入。

其主要目标是减轻家庭的经济负担，使更多的父母，尤其是母亲，能够参与到劳动力市场中。倡导者认为，这将促进该州的经济发展并减少贫困。该计划还旨在改善全州儿童的早期教育成果。

该计划主要侧重于向托儿服务提供者提供补贴，使他们能够为家庭提供免费或低价的托儿服务。它解决了劳动力参与的一个重要障碍，并解决了托儿服务的高昂成本问题，而这不成比例地影响着低收入家庭。这项倡议可以为其他州考虑采取类似政策以扩大早期儿童教育的范围并支持工作的家庭提供一个典范。预计它将对该州的经济、劳动力参与率以及新墨西哥州家庭的整体福祉产生重大影响。

---

## 3. 浏览器指纹的隐私噩梦

**原文标题**: The privacy nightmare of browser fingerprinting

**原文链接**: [https://kevinboone.me/fingerprinting.html](https://kevinboone.me/fingerprinting.html)

本文深入探讨了浏览器指纹识别带来的隐私威胁。浏览器指纹识别是一种网站用于追踪用户的方法，它无需依赖 Cookie。文章解释了指纹识别的工作原理，它通过收集关于浏览器的各种信息，例如操作系统、浏览器版本、已安装字体、扩展程序，甚至是图形渲染方式的细微差别（Canvas 指纹识别）。将这些数据点组合起来，会创建一个唯一的标识符，或“指纹”，使网站能够在网络上追踪用户。

作者强调了对抗指纹识别的难度。禁用 JavaScript 或伪造浏览器信息等简单措施可能会适得其反，反而使用户更加显眼。他们还讨论了指纹识别的局限性，指出实际追踪比演示网站显示的更具挑战性，并且指纹会随着时间而改变。

尽管前景黯淡，但文章提供了一些减轻风险的建议。这些建议包括使用 VPN、频繁轮换 VPN 节点、定期清除 Cookie 以及保持标准的浏览器配置。还建议使用具有内置指纹识别抵抗能力的浏览器，例如 Brave、Mullvad 或 Librewolf。然而，这些措施也存在缺点，例如增加 CAPTCHA 挑战和潜在的网站兼容性问题。

即使在 GDPR 框架下，浏览器指纹识别的合法性也存在争议。作者总结说，虽然指纹识别构成了重大的隐私问题，尤其是在支持在线广告行业方面，但其影响是统计上的，而不是决定性的。立法被视为最终的解决方案，但广告行业可能会继续寻找新的追踪方法。

---

## 4. 个人博客回归，利基博客会是下一个趋势吗？

**原文标题**: Personal blogs are back, should niche blogs be next?

**原文链接**: [https://disassociated.com/personal-blogs-back-niche-blogs-next/](https://disassociated.com/personal-blogs-back-niche-blogs-next/)

这篇博文探讨了随着近期个人博客的复兴，利基博客可能再度兴起的潜力。作者回顾了博客的“黄金时代”，并提及Problogger及其专注于帮助博主通过利基专业化实现内容变现。虽然承认利基博客的成功，但作者指出这种形式并不适合所有人，像Kottke这样的通才博客也蓬勃发展。

作者认为，当前的网络环境被社交媒体和人工智能生成的内容所主导，缺乏可靠和值得信任的信息。因此，需要回归到撰写精良、主题聚焦的利基博客。作者倡导独立写作者创作高质量的内容，并获得公平的报酬，同时不通过侵入式广告来损害用户体验。目标是恢复可访问和值得信赖的信息流，摆脱社交媒体上的虚假信息和人工智能生成的摘要。

作者澄清说，当前的独立网络/小型网络运动正在推动个人网站的复苏。他们希望这是一个起点，利基博客紧随其后，重建一个充满活力的网络，让值得信赖的信息唾手可得。

---

## 5. 如何见死者

**原文标题**: How to See the Dead

**原文链接**: [https://www.asimov.press/p/see-the-dead](https://www.asimov.press/p/see-the-dead)

在《如何看见死者》中，视网膜植入体设计师斯宾塞·尼特基接到了一位名叫艾普丽的客户提出的一个 необычный

斯宾塞与想象技术专家奥克斯合作，开发了一个由三部分组成的模块化系统。视网膜植入体作为屏幕，皮层桥作为投影仪，海马体回忆界面作为播放设备。目标是将艾普丽因悲伤而产生的记忆转化为视觉蓝图，并将其与她的实时视觉相结合。

他们对艾普丽进行了大量的访谈，记录她在回忆起爱人的记忆时的大脑活动，重点关注感官细节。奥克斯利用这些数据构建了一个AI编码器，将她的记忆转化为视觉图像，而斯宾塞则专注于植入体和皮层桥。

经过数周的开发，他们使用一个“幻影皮层”（一种合成的艾普丽视觉皮层的替代品）来测试集成系统。在测试过程中，他们发现AI重建的内容会降解和出现故障，揭示了记忆和现实融合的复杂性。文章在留下悬念的情况下结束，让读者自行判断接下来会发生什么，以及这一切是否值得。

---

## 6. 帮助Valve公司增强Steam设备的能力

**原文标题**: Helping Valve to power up Steam devices

**原文链接**: [https://www.igalia.com/2025/11/helpingvalve.html](https://www.igalia.com/2025/11/helpingvalve.html)

Igalia与Valve的合作在为Valve的新Steam设备提供动力方面发挥了重要作用，这些设备包括：Steam Frame（无线VR头显）、Steam Machine（游戏主机）和Steam Controller。 Igalia的工作主要集中在两个关键领域：使x86游戏能够在基于ARM的Steam Frame上流畅运行，以及优化Qualcomm Adreno GPU的Vulkan图形驱动程序。

为了克服游戏PC（x86）和Steam Frame（ARM）之间的架构差异，Igalia正在改进FEX翻译层。这使得为x86编译的游戏可以通过翻译机器代码在ARM上运行。这个过程通常需要细致的手动测试。

Igalia还为 Mesa3D Turnip（一个FOSS Vulkan驱动程序）做出了重大贡献，确保了Steam Frame的 Qualcomm Adreno 750 GPU上高性能且无错误的图形效果。他们增加了对Adreno 700系列GPU的支持，实现了诸如LRZ和自动调谐器等关键优化，并通过DXVK、vkd3d-proton和Zink等项目确保了与各种图形API的兼容性。他们的贡献甚至提高了在Android手机上运行的PC游戏的性能并减少了故障。

Valve对开源软件的承诺使得这次合作特别有益。Igalia的改进和优化使所有使用相同开源项目的人都可以使用。此外，Igalia正在开发一个定制的CPU调度器（LAVD），该调度器可在性能和功耗之间取得平衡，这对于Steam Frame的电池寿命至关重要。他们还在为Steam Machine开发AMD内核显示驱动程序。 Igalia的工作确保了新Steam设备上流畅、高效且图形效果出色的游戏体验，并增强了更广泛的Linux游戏生态系统。

---

## 7. 刚刚发射的两颗火星探测器携带了一个彩蛋。

**原文标题**: The twin probes just launched toward Mars have an Easter egg on board

**原文链接**: [https://arstechnica.com/space/2025/11/the-twin-probes-just-launched-toward-mars-have-an-easter-egg-on-board/](https://arstechnica.com/space/2025/11/the-twin-probes-just-launched-toward-mars-have-an-easter-egg-on-board/)

双子ESCAPADE探测器搭乘蓝色起源公司的新格伦火箭发射升空，将用22个月的时间前往火星，研究空间天气如何影响火星大气层。这两颗由火箭实验室设计和制造的探测器，分别名为“蓝色”和“金色”，携带有一个隐藏的彩蛋：几维鸟的图案，这象征着火箭实验室的 New Zealand 起源。这些几维鸟与火箭实验室的标志、座右铭（“这个世界还不够”）以及象征该公司全球影响力的美国秃鹰图标一同出现在铭牌上。

这项由加州大学伯克利分校的空间科学实验室领导的任务，旨在了解火星为何失去了曾经稠密的大气层和潜在的宜居环境。在从新格伦火箭部署后，探测器将在拉格朗日点2周围环绕，然后在2027年9月利用引力辅助到达火星。随后，它们将进入轨道并进行协同观测，以研究太阳风对火星磁层的影响。

除了装饰有几维鸟的铭牌外，航天器还装有列出为该任务做出贡献的火箭实验室团队成员的铭牌。文章还重点介绍了任务的标志和徽章，代表了包括加州大学伯克利分校、火箭实验室、安柏瑞德航空大学、Advanced Space和美国宇航局戈达德太空飞行中心在内的各个合作伙伴。

---

## 8. 三星DRAM涨价60%预示全球内存供应进一步收紧

**原文标题**: Samsung's 60% DRAM price hike signals a new phase of global memory tightening

**原文链接**: [https://www.buysellram.com/blog/samsungs-memory-price-surge-sends-shockwaves-through-the-global-dram-market/](https://www.buysellram.com/blog/samsungs-memory-price-surge-sends-shockwaves-through-the-global-dram-market/)

自2025年9月以来，三星已将DRAM价格提高了高达60%，这表明全球内存市场因人工智能数据中心需求的激增而趋紧。 此次价格上涨，影响了高密度服务器DRAM模块，是近年来涨幅最大的一次，预计将对PC、服务器和IT硬件行业产生影响，直至2026年。

文章强调，主要驱动因素是人工智能基础设施的爆炸式增长，消耗了大量的DDR5和HBM内存。 三星以及SK海力士和美光等其他制造商正在优先生产用于人工智能服务器的高端芯片，从而减少了传统DRAM的产能。

这种供应限制，加上消费者需求的复苏和有限的制造利用率，正在造成一场“完美风暴”，推动整个市场价格上涨。 价格飙升始于合约市场，现在正在影响零售渠道，DDR5套件的价格同比翻了一番，而较旧的DDR4模块的价格也在上涨。

分析师预测，除非DRAM产量大幅增加，否则这种价格上涨周期将持续到2026年。 二手DRAM的二级市场也在做出反应，随着经销商持有库存的时间延长，价格也在上涨。

文章建议系统构建商、数据中心运营商和组件经销商仔细规划，建议尽早签订供应合同，以避免潜在的短缺。 消费者和小型IT运营商应预期价格持续波动。 总之，人工智能的繁荣正在将DRAM从一种商品转变为计算供应链中的一个战略瓶颈。

---

## 9. 柯达曾在地下室运行核装置数十年。

**原文标题**: Kodak ran a nuclear device in its basement for decades

**原文链接**: [https://www.popularmechanics.com/science/energy/a69147321/kodak-film-nuclear-reactor/](https://www.popularmechanics.com/science/energy/a69147321/kodak-film-nuclear-reactor/)

三十年来，柯达公司在其纽约州罗切斯特市的地下室运营一台锎中子通量倍增器(CFX)，该设备使用少量锎-252和高浓铀(HEU)来产生中子，用于材料分析。CFX利用中子活化分析来测试化学品中的杂质，并利用中子射线照相术，与X射线不同，它可以有效地对水和胶片等较轻元素进行成像，使柯达能够识别X射线会遗漏的泄漏。

该设备是次临界的，意味着它无法独立维持链式反应，使其比核反应堆更安全。虽然柯达公司使用高浓铀的消息在2012年公开时引起了恐慌，但CFX在严格的政府监管下运行。主要担忧出现在2007年退役期间，原因是存在3.5磅高浓铀，如果被恶意行为者获取，则存在潜在的安全风险。在高能物理部的监督下，高浓铀被小心地运送到政府设施，并制定了严格的协议。文章强调，CFX代表了一种冷战时期的技术奇观，突出了那个时代的核乐观主义，当时此类设备在大学和私营公司中更为常见。该建筑此后已被出售并宣布安全。

---

## 10. Show HN: Wealthfolio 2.0 - 开源投资跟踪器。现已支持移动端和Docker

**原文标题**: Show HN: Wealthfolio 2.0- Open source investment tracker. Now Mobile and Docker

**原文链接**: [https://wealthfolio.app/?v=2.0](https://wealthfolio.app/?v=2.0)

Wealthfolio 2.0：一款注重隐私的开源投资追踪器，现已推出桌面、移动和网页版，并支持Docker部署。它旨在通过安全的本地应用程序，替代混乱的电子表格和隐私担忧。主要功能包括通过CSV导入进行账户聚合，提供包含资产配置洞察的全面投资组合概览，以及针对标普500等基准的业绩追踪。

它还提供股息和利息的收入追踪、个人账户的历史业绩分析、目标设定和进度监控，以及税务优惠账户的供款限额追踪。用户可以定义财务目标，追踪进度，并避免过度供款。

该应用程序拥有美观且用户友好的界面，并提供可选的一次性付费，无需定期订阅费用。其可扩展性体现在可选的附加组件上，例如投资费用追踪器、目标进度追踪器和股票交易追踪器。它通过将数据保存在用户设备上，优先考虑用户隐私。

---

## 11. 具有权重稀疏性的Transformer模型具有可解释的回路 [pdf]

**原文标题**: Weight-sparse transformers have interpretable circuits [pdf]

**原文链接**: [https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf](https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf)

无法根据提供的文本生成文章摘要。提供的文本似乎是PDF文件的内部表示，包括与字体、图像和文档结构相关的编码数据，而不是文章的实际文本内容。

为了总结文章《权重稀疏的Transformer具有可解释的电路》，我需要文章的实际文本或恰当的摘要。然后我才能识别核心论点、方法和发现，从而创建一个简洁的摘要。

---

## 12. 连接标准联盟发布 Zigbee 4.0 和 Suzi

**原文标题**: The Connectivity Standards Alliance Announces Zigbee 4.0 and Suzi

**原文链接**: [https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/)

连接标准联盟(CSA)于2025年11月18日宣布了Zigbee 4.0和Suzi，这是物联网连接方面的重大进展。 Zigbee 4.0协调了传统的Zigbee和智能能源设备，以实现更好的互操作性，简化了认证，并实施了符合不断发展的全球标准的增强型安全功能。它还将频率支持扩展到欧洲的800 MHz和北美的900 MHz，从而提高了信号强度和范围，同时保持与现有Zigbee设备的向后兼容性。主要功能包括动态链路密钥、设备访谈和智能能源身份验证级别控制，以增强安全性，以及用于网络管理和恢复的工具。 Zigbee 4.0还通过Zigbee Direct简化了通过蓝牙低功耗（BLE）的设备配置和控制，并实现了高效的批量调试。

Suzi是Zigbee的Sub-GHz功能的新品牌，这是一种基于标准的无线技术，可提供远距离、低功耗的网状网络。它构建在Zigbee网络层上，可在需要扩展覆盖范围的住宅、商业和工业应用中实现强大的通信。 Suzi遵循强大的安全原则和国际标准，其认证计划预计于2026年上半年进行。

Zigbee 4.0和Suzi共同致力于通过改进的安全性、简化的配置和扩展的范围来加强全球物联网网络，从而使安全和智能的连接更易于访问。

---

## 13. TiDAR：扩散思维，自回归表达

**原文标题**: TiDAR: Think in Diffusion, Talk in Autoregression

**原文链接**: [https://arxiv.org/abs/2511.08923](https://arxiv.org/abs/2511.08923)

这篇arXiv文章 (arXiv:2511.08923) 介绍了 TiDAR (“扩散式思考，自回归式表达”)，一种新型语言模型架构，旨在结合扩散模型的速度和自回归 (AR) 模型的质量。作者解决了试图弥合这两种方法之间差距的现有方法的局限性。TiDAR 使用扩散并行生成 tokens (思考)，并在一次前向传递中自回归地改进它们 (表达)，利用结构化注意力掩码实现高效的 GPU 利用率。

TiDAR 的主要优势在于其能够在保持高吞吐量的同时实现 AR 级别质量，使其适用于服务。它被设计为具有低开销的独立模型。

该论文对 1.5B 和 8B 规模的 TiDAR 进行了广泛评估，将其与 AR 模型、推测解码和扩散变体（Dream 和 Llada）在生成和似然任务上进行了比较。结果表明，TiDAR 在吞吐量方面优于推测解码，并在效率和质量方面超越了扩散模型。至关重要的是，TiDAR 在每秒 tokens 数方面实现了 4.71 倍至 5.91 倍的显著加速，同时达到了与 AR 模型相当的质量。这使其成为第一个有效缩小与 AR 模型之间的质量差距而不牺牲速度的架构。这项研究得到了 NVIDIA 的支持，如“NVIDIA-Tech Report”评论中所述。

---

## 14. 原始超人漫画成为有史以来售价最高的漫画书

**原文标题**: Original Superman comic becomes the highest-priced comic book ever sold

**原文链接**: [https://www.bbc.com/news/articles/c8e9rp0knj6o](https://www.bbc.com/news/articles/c8e9rp0knj6o)

一本1939年6月出版的《超人》第一期漫画书，品相完好，以912万美元的价格在拍卖会上成交，成为有史以来最有价值的漫画。去年圣诞节，三兄弟在清理已故母亲位于加州家中的阁楼时发现了这本漫画。他们在阁楼里一个装满报纸的纸板箱下，被蜘蛛网包裹着找到了它。这三位不愿透露姓名的兄弟，年龄在五十到六十岁之间，他们的母亲曾告诉他们，她收藏了一些有价值的漫画书。

据Heritage Auctions拍卖行称，这家人（母亲和她的兄弟）在经济大萧条时期到二战期间购买了这些漫画。加州凉爽的气候帮助保存了这本漫画，使得漫画评级服务机构CGC给它打出了9.0分的评级（满分10分），超过了之前的8.5分纪录。这一高评级促成了创纪录的成交价格，比之前的纪录保持者《动作漫画》第一期（首次引入超人，去年以600万美元成交）高出300万美元。最小的弟弟强调，这次发现是对家庭、记忆以及过去以意想不到的方式重现的提醒。

---

## 15. “法国人民想要拯救我们”：援助涌向玻璃制造商Duralex

**原文标题**: 'The French people want to save us': help pours in for glassmaker Duralex

**原文链接**: [https://www.theguardian.com/world/2025/nov/22/french-people-want-to-save-us-help-pours-glassmaker-duralex](https://www.theguardian.com/world/2025/nov/22/french-people-want-to-save-us-help-pours-glassmaker-duralex)

以耐用的Picardie玻璃杯而闻名的法国标志性玻璃制造商Duralex面临财务困境，并向公众呼吁紧急融资。公众反应非常热烈，仅在五个小时内就达到了最初的500万欧元目标，并在48小时内超过了1900万欧元。 这份如潮的支持反映了该品牌的怀旧价值及其作为法国工业遗产象征的地位。

该公司现在是一家员工合作社，计划利用这些资金来现代化其工厂并开发新产品，包括为爱丽舍宫总统府商店提供的玻璃杯以及为英国和美国市场提供的品脱杯。 该工厂的传统玻璃制造工艺，包括将沙子、纯碱和石灰石的混合物加热到极端温度，自1945年以来基本没有改变。质量控制非常严格，玻璃杯要经过压力测试，以确保其耐用性。

虽然Duralex面临着天然气和电力成本上涨等挑战，但该公司对其未来持乐观态度。 自成为员工合作社以来，营业额有所增加，目标是在2027年实现盈亏平衡。 现在的重点是增加销量，尤其是在Duralex缺乏同样怀旧吸引力的国际市场。

---

## 16. 苔藓在太空真空环境中存活9个月

**原文标题**: Moss Survives 9 Months in Space Vacuum

**原文链接**: [https://scienceclock.com/moss-survives-9-months-in-space-vacuum/](https://scienceclock.com/moss-survives-9-months-in-space-vacuum/)

苔藓孢子在严酷太空环境中表现出非凡的韧性，在国际空间站外存活了九个月。北海道大学的藤田智路领导的科学家团队将蔓生藓（Physcomitrium patens）的孢子囊暴露于直接太阳辐射、真空条件和极端温度变化中。令人惊讶的是，超过80%的孢子在返回地球后仍能发芽。

尽管叶绿素a略有下降，但这些孢子在后续测试中表现出正常的生长，并且没有显示出明显的压力迹象。这种耐寒性归功于苔藓植物（包括苔藓、地钱和角苔）的进化历史，因为它们是最早登陆的植物之一。它们的孢子进化到能够承受土壤存在之前的干燥和阳光等恶劣条件。

这项研究将苔藓孢子与缓步动物和某些微生物一起定位为能够耐受直接太空暴露的生物。这一发现对讨论生命在地球以外的极端环境中生存的可能性具有重要意义。

研究人员认为，苔藓由于其对土壤的最低要求以及从岩石中提取养分的能力，可能对未来在月球或火星上的生态系统实验具有价值。他们设想这项工作是构建地外环境生态系统的起点。这项研究的结果已发表在iScience杂志上。

---

## 17. 我是如何学习Vulkan并用它编写了一个小型游戏引擎(2024)

**原文标题**: How I learned Vulkan and wrote a small game engine with it (2024)

**原文链接**: [https://edw.is/learning-vulkan/](https://edw.is/learning-vulkan/)

本文详细介绍了作者三个月内学习 Vulkan 并开发小型游戏引擎 EDBR 的历程，期间构建了两个游戏演示。作者强调初学者应从 OpenGL 入手，并推荐 learnopengl.com 和 Anton's OpenGL 4 Tutorials 等资源。他们主张避免“自行车棚效应”，优先考虑实际实现而非过早优化，并且不要一开始就试图编写通用引擎。从小游戏入手，再提取可重用组件。

作者探讨了为个人项目（桌面小型 3D 游戏）选择 Vulkan 的原因，并提及了其在特定用例中相对于 OpenGL、WebGL/WebGPU 和 DirectX 的优势。他们发现 vkguide 是最有用的 Vulkan 学习资源，以及诸如“3D Graphics Rendering Cookbook”和“Mastering Graphics Programming with Vulkan”之类的高级书籍。

本文概述了 EDBR 引擎、其架构和渲染管线。该引擎包括基于计算着色器的蒙皮、级联阴影贴图 (CSM)、PBR 着色、深度解析和后期处理效果等功能。他们还建议使用诸如 vk-bootstrap 之类的库来简化 Vulkan 样板代码，简化物理设备选择和交换链创建。

---

## 18. 基于新物理模型的更清晰MRI扫描或将成为现实

**原文标题**: Sharper MRI scans may be on horizon thanks to new physics-based model

**原文链接**: [https://news.rice.edu/news/2025/sharper-mri-scans-may-be-horizon-thanks-new-physics-based-model](https://news.rice.edu/news/2025/sharper-mri-scans-may-be-horizon-thanks-new-physics-based-model)

更清晰的核磁共振扫描或将成为现实，这要归功于莱斯大学研究人员开发的一种新的基于物理学的模型。该团队创建了一个更精确的模型来模拟核磁共振扫描期间产生的信号。目前的模型依赖于简化的近似值，这可能导致图像模糊和不准确。这种新模型基于对布洛赫方程底层物理学以及射频脉冲如何与身体组织相互作用的更全面的理解，有望提高图像分辨率和诊断能力。

具体来说，这种新模型侧重于准确模拟射频脉冲的影响，这对于产生核磁共振信号至关重要。通过将更详细的物理学原理纳入模拟中，研究人员可以更好地预测不同组织对这些脉冲的反应。这种改进的精度可以使临床医生能够微调核磁共振参数以获得最佳图像质量，从而有可能揭示更精细的细节并提高对细微异常的检测。

研究人员测试了他们的模型，并证明它可以在各种条件下准确模拟核磁共振信号。他们认为这项工作可能促成新的核磁共振技术和脉冲序列的开发，从而提供更高分辨率的图像并提高诊断准确性。此外，它还有可能加速新核磁共振技术的开发和优化，而无需进行广泛而昂贵的物理实验。 最终目标是为临床医生提供更清晰、更精确的图像，从而实现更准确的诊断和更好的患者预后。

---

## 19. 我们都应该使用依赖冷却机制。

**原文标题**: We should all be using dependency cooldowns

**原文链接**: [https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)

本博文倡导广泛采用“依赖冷却期”，将其作为一种简单有效的缓解开源供应链攻击的方法。作者认为，虽然供应链安全是一个合理的担忧，但它常常被供应商过度炒作。大多数攻击都遵循类似的模式：攻击者入侵一个项目，引入恶意更改，用户通过自动更新获取受损版本，供应商向上游发出警报，最后，受损的软件包被移除。

关键在于，攻击者在引入恶意代码后造成破坏的机会窗口通常相对较短（几小时或几天），远短于最初引入漏洞所需的时间。通过实施冷却期——即在依赖项发布后到被认为可以安全使用之间设置一个等待期——开发者可以避免大多数常见攻击。

作者强调了使用Dependabot和Renovate等工具实现冷却期的简易性，并建议包管理器应原生支持冷却期。冷却期激励供应商快速发现和报告漏洞。虽然冷却期并非万灵药，但7-14天的冷却期可以显著减少暴露于攻击的风险，潜在地减少80-90%，而且几乎不需要任何成本或精力。xz-utils攻击被认为是一个具有更长窗口期的异常情况。文章强调，供应链安全最终是一个社会信任问题，但像依赖冷却期这样的技术解决方案可以大大改善这种情况。

---

## 20. 我们的孩子在“有偏见”的育儿测试后被带走

**原文标题**: Our babies were taken after 'biased' parenting test

**原文链接**: [https://www.bbc.co.uk/news/articles/c1wlw2qj113o](https://www.bbc.co.uk/news/articles/c1wlw2qj113o)

这篇BBC文章调查了丹麦使用父母能力测试(FKU)的争议性做法，该做法导致格陵兰儿童被从其家庭中移除。这些测试因其文化偏见于丹麦规范且以丹麦语进行而被批评，通过访谈、认知任务和性格评估来评估父母的养育能力。格陵兰父母的孩子被带走照看的可能性是丹麦父母的5.6倍。

其中一位母亲凯拉讲述了她的新生女儿在一次评估后被认为不合格而被带走的创伤，她提到了关于特蕾莎修女和阳光的问题。另一对夫妇约翰妮和乌尔里克的新生儿子尽管他们向当局恳求，还是被收养了；他们的案例，与其他涉及收养的案例一样，将不会被复审。虽然丹麦政府在2024年5月禁止了对格陵兰家庭进行FKU，并启动了对300个案例的复审，但进展缓慢，到10月份只复审了10个案例，没有孩子被送回。

心理学家伊萨克·内勒曼认为，这些测试缺乏科学依据，并且往往是决定儿童移除的关键因素，而像图里·弗雷德里克森等人则捍卫其价值。皮林瓜克是一个罕见的例子，她在四年后与女儿团聚，但担心她可能会再次被带走。丹麦政府为其彻底的儿童移除程序辩护，强调长期的福利。这篇文章突出了格陵兰家庭遭受的毁灭性影响以及他们与孩子团聚的斗争，同时质疑评估的公平性和文化敏感性。

---

## 21. 混凝土造船——阿根廷

**原文标题**: Concrete Shipbuilding – Argentina

**原文链接**: [https://thecretefleet.com/blog/f/concrete-shipbuilding-–-argentina](https://thecretefleet.com/blog/f/concrete-shipbuilding-–-argentina)

这是一个简短的介绍性片段，来自一个名为“克里特船队”的网站，该网站是一部关于混凝土船的百科全书。网站重点介绍第一次世界大战和第二次世界大战期间的混凝土船，以及马尔贝里港（诺曼底登陆期间建造的临时港口设施）的组成部分。这段文字突出了该网站的版权信息，提及使用 Cookie 分析网站流量和优化用户体验，并标明了内容索引。它没有详细介绍阿根廷的混凝土造船，而是介绍了网站的整体范围。

---

## 22. 洛杉矶警察局直升机追踪器，带实时运营成本

**原文标题**: LAPD helicopter tracker with real-time operating costs

**原文链接**: [https://lapdhelicoptertracker.com/](https://lapdhelicoptertracker.com/)

本文介绍了一个追踪洛杉矶警察局直升机的实时位置和运营成本的系统。其核心功能是提高洛杉矶警用航空资源使用的透明度和问责制。该系统允许用户查看洛杉矶警察局直升机当前的飞行位置，并实时估算每次飞行的成本。

该系统可能使用数据流来精确定位直升机位置，可能包含飞行路径数据，然后将此位置信息与运营成本数据（燃料、维护、机组人员工资等）相结合，以计算每次飞行的估计成本。这使得公众或特定利益相关者能够监控直升机的部署，并了解警用航空活动的财务影响。

主要重点是更清晰地了解洛杉矶警察局直升机的使用方式以及这些行动的成本。该工具旨在提高公众意识，并可能为洛杉矶警察局内部的资源分配讨论提供信息。通过使这些信息易于获取，该追踪器旨在促进负责任和高效地使用纳税人的钱。

---

## 23. Arduino服务条款和隐私政策更新：以正视听

**原文标题**: Arduino Terms of Service and Privacy Policy update: setting the record straight

**原文链接**: [https://blog.arduino.cc/2025/11/21/the-arduino-terms-of-service-and-privacy-policy-update-setting-the-record-straight/](https://blog.arduino.cc/2025/11/21/the-arduino-terms-of-service-and-privacy-policy-update-setting-the-record-straight/)

Arduino就服务条款和隐私政策更新回应社区关切
以下是根据提供的约束条件对原始文本的翻译:

Arduino就服务条款和隐私政策更新回应社区关切。主要信息是，尽管被高通收购，Arduino仍然致力于其开源原则。更新主要是为了清晰化，遵守不断发展的法规，并反映包括人工智能功能在内的新特性。

文章强调，开源硬件、软件和服务保持不变且可访问。用户生成的内容所有权仍然归用户所有，从而能够使用云服务等功能。通过更新的政策和年龄限制，数据隐私，尤其是未成年人的数据隐私得到了加强。非活跃用户帐户在24个月后会自动停用，以限制数据保留。

更新涵盖了围绕数据实践的增强透明度，引入了需要更新条款以负责任地使用的人工智能驱动功能，针对高级服务用户的更精确的商业条款（账单、退款）以及符合美国和全球监管要求。

Arduino重申其20年来对开源的承诺，并鼓励用户查看完整的服务条款和隐私政策。他们还提供了一个常见问题解答部分和一个电子邮件地址（privacy@arduino.cc），用于解决具体问题或疑虑。总体基调令人安心，旨在消除人们对这些更改会影响Arduino核心价值观的担忧。

---

## 24. 苹果新研究表明，大型语言模型可根据音频和运动数据判断你在做什么

**原文标题**: New Apple Study Shows LLMs Can Tell What You're Doing from Audio and Motion Data

**原文链接**: [https://9to5mac.com/2025/11/21/apple-research-llm-study-audio-motion-activity/](https://9to5mac.com/2025/11/21/apple-research-llm-study-audio-motion-activity/)

苹果研究人员发表了一项研究，展示了大型语言模型（LLMs）如何有效地分析音频和运动数据来理解用户活动。该研究题为“利用LLMs进行活动识别的后期多模态传感器融合”，探讨了LLMs增强活动分析的潜力，尤其是在传感器数据有限的情况下。

研究人员使用了Ego4D数据集，该数据集包含数千小时的第一人称视频，记录了日常活动。他们专注于精选的12项活动子集，如烹饪、清洁和锻炼。来自这些活动的音频和运动数据由较小的模型处理，以生成文本描述和活动预测，然后将其输入到LLMs（Gemini-2.5-pro和Qwen-32B）中。

LLMs在封闭集（给定活动列表）和开放式场景中进行了测试。结果表明，即使没有经过专门训练，LLMs在识别活动方面也明显优于随机水平。仅向LLMs提供一个示例就能进一步提高准确性。该研究强调，LLMs可以成功地从表示为文本的音频和运动信号中推断用户活动，而无需实际的原始音频。

研究结果表明，结合包括LLMs在内的多个模型，可以极大地促进活动和健康数据分析，尤其是在仅凭原始传感器数据不足的情况下。苹果发布了补充材料，以帮助其他研究人员重现该研究的结果。

---

## 25. 童年玩伴而非母亲，最能塑造依恋模式

**原文标题**: Childhood Friends, Not Moms, Shape Attachment Styles Most

**原文链接**: [https://nautil.us/childhood-friends-not-moms-shape-attachment-styles-most-1247316/](https://nautil.us/childhood-friends-not-moms-shape-attachment-styles-most-1247316/)

童年友谊而非母亲更能塑造依恋模式

---

## 26. 搭载骁龙X Elite SoC的ARM笔记本停产

**原文标题**: Discontinuation of ARM Notebook with Snapdragon X Elite SoC

**原文链接**: [https://www.tuxedocomputers.com/en/Discontinuation-of-ARM-notebooks-with-Snapdragon-X-Elite-SoC.tuxedo](https://www.tuxedocomputers.com/en/Discontinuation-of-ARM-notebooks-with-Snapdragon-X-Elite-SoC.tuxedo)

此文章摘录**并非**宣布搭载骁龙X Elite SoC的ARM笔记本停产。相反，它只是一个疑似在线商店页面的片段。

核心信息集中在宣传该商店的特点：

*   需要JavaScript并禁用脚本拦截器才能正常运行。
*   突出显示了与所提供产品相关的几个关键卖点：
    *   Linux兼容性
    *   长达5年保修
    *   随时可以使用
    *   德国组装
    *   德国数据隐私标准
    *   德国技术支持

主要重点在于与商店可能制造或销售的产品相关的可靠性、安全性和用户便利性。 没有关于停产笔记本的信息。

---

## 27. 难读先生：威廉·加迪斯与难读作品的问题 (2002)

**原文标题**: Mr. Difficult: William Gaddis and the Problem of Hard-to-Read Books (2002)

**原文链接**: [https://adilegian.com/FranzenGaddis.htm](https://adilegian.com/FranzenGaddis.htm)

在《难搞先生》中，乔纳森·弗兰岑反思了写作和阅读晦涩文学作品的挑战，起因是一位读者M夫人写来的一封愤怒的信，她觉得自己因其小说中复杂的语言而被排除在外。他对比了两种小说模式：“地位”模式，即重视艺术本身的价值，并将晦涩作品提升到固有的优越地位；以及“契约”模式，即强调作者与读者建立联系并娱乐读者的义务。

弗兰岑认为，虽然他从理智上理解“地位”模式，但作为一位重视愉悦和联结的读者，他从根本上被“契约”模式所吸引。他以自己阅读威廉·加迪斯《承认》的经历为例。尽管其篇幅冗长且晦涩难懂——充满了晦涩的典故、外语和挑战性的散文——弗兰岑发现这本书在他个人困难时期具有回报甚至具有变革性。

他将加迪斯作品的难度与作者对“地位”模式的认可及其对美国社会商业主义的批判联系起来。弗兰岑承认，在学术环境中，晦涩书籍通常被视为学习文学技巧和批判性思维的工具而备受推崇。然而，他也努力应对艺术抱负与渴望与更广泛的受众有效沟通之间的张力，特别是在考虑到他父亲对纯粹艺术追求价值的怀疑以及他自己大学毕业后渴望创作具有社会参与性的小说的愿望。

---

## 28. 你可以用 JavaScript 制作 PS2 游戏。

**原文标题**: You can make PS2 games in JavaScript

**原文链接**: [https://jslegenddev.substack.com/p/you-can-now-make-ps2-games-in-javascript](https://jslegenddev.substack.com/p/you-can-now-make-ps2-games-in-javascript)

无法访问文章链接。

---

## 29. 矩阵乘法丑陋吗？

**原文标题**: Is Matrix Multiplication Ugly?

**原文链接**: [https://mathenchant.wordpress.com/2025/11/21/is-matrix-multiplication-ugly/](https://mathenchant.wordpress.com/2025/11/21/is-matrix-multiplication-ugly/)

文章“矩阵乘法丑陋吗？”是对 Stephen Witt 在《纽约客》杂志上发表的一篇文章中提出的观点的回应，该观点声称矩阵乘法缺乏美感和优雅，并将其比作“一个人用锤子把钉子钉进木板”。作者是一位数学家，强烈反对这一观点，认为 Witt 误解了矩阵的作用和意义。

作者认为，矩阵是理解变换和对称性的基础，代表着诸如反射和旋转等操作。他证明了这些变换的顺序很重要 (g ◦ f ≠ f ◦ g)，并将其与日常生活中的例子进行类比，例如制作沙拉或创作旋律。虽然手动执行矩阵乘法可能很繁琐，但其核心概念优雅且在物理学、人工智能和数学等各个领域至关重要。

作者认为，Witt 对丑陋的看法可能源于手动矩阵乘法的重复性，但这并不能否定其底层数学概念的美感。他进一步指出，数学家 G.H. Hardy 偏爱概念性证明而非计算性证明，不应被误解为普遍鄙视计算，尤其是在矩阵乘法至关重要的应用领域。

最终，作者捍卫矩阵乘法是数学中一个美丽且重要的组成部分，认为任何数学概念，如果简化为无意义的计算，都可能显得令人厌倦，但这并不会削弱其内在价值。文章最后强调了计算机在处理矩阵乘法的重复性方面的作用，使人们能够专注于概念性的理解。

---

## 30. 皮克斯：早期岁月，一段从未曝光的1996年访谈

**原文标题**: Pixar: The Early Days A never-before-seen 1996 interview

**原文链接**: [https://stevejobsarchive.com/stories/pixar-early-days](https://stevejobsarchive.com/stories/pixar-early-days)

本文宣布发布一段先前未公开的 1996 年史蒂夫·乔布斯关于皮克斯的采访，时间与《玩具总动员》30 周年纪念日相吻合。 这次采访在《玩具总动员》具有开创意义的发行一年后进行，揭示了乔布斯对公司及其独特商业模式的长期愿景。

文章重点介绍了《玩具总动员》的立即成功，它改变了皮克斯，并促成了一次非常成功的首次公开募股。文章还指出了皮克斯转向专注于故事片及其快速增长。

在采访中，乔布斯讨论了皮克斯的结构如何赋能艺术家和工程师，使他们对自己的工作产生既得利益。他还回顾了从迪士尼学到的关于专注和纪律的经验教训。他谈到了管理高素质团队的挑战以及保持员工敬业度的激励措施。一个中心主题是皮克斯致力于创造持久且具有文化价值的故事。

文章强调了乔布斯与艾德·卡特姆在开发培养人才的管理风格方面的密切合作。文章最后指出，乔布斯在皮克斯的经验如何影响了他对苹果公司领导方式的看法，即专注于永恒的理念和技术创新。

---

## 31. 把产品做烂，捞钱。

**原文标题**: Make product worse, get money

**原文链接**: [https://dynomight.net/worse/](https://dynomight.net/worse/)

本文批判了一种过于简单的理论，该理论认为企业故意降低产品质量以实现利润最大化。作者认为，虽然企业自然有降低成本和提高价格的动机，但这并不能完全解释为什么产品通常“很差”。

作者列举了披萨、汽车和约会应用程序等各个行业的例子，说明了常见的“降低产品质量，获取更多利润”的论点。然而，他们认为这种理论忽略了竞争格局和消费者偏好。

文章提出了产品质量差的四个主要原因：

1. **人们贪图便宜：** 消费者通常优先考虑较低的价格而非较高的质量，导致企业提供更便宜但质量较差的产品。这反映了市场效率，即资源根据需求进行分配。
2. **信息不对称：** 消费者缺乏辨别质量的专业知识或能力，使得不择手段的企业能够从劣质甚至有害的产品中获利。
3. **人们品味低下：** 有时，被认为是“差”的产品仅仅是主观品味的问题，而市场迎合的是普遍的偏好。
4. **定价权：** 拥有垄断地位或强大市场地位的公司可以利用其权力，由于缺乏竞争，以更高的价格提供质量较低的产品。

作者的结论是，仅仅确定降低产品质量的动机是不够的。关键问题是，企业*为什么*能够逃脱惩罚，并将此归因于消费者选择、信息失衡、主观偏好和反竞争的市场条件等因素。理解这些因素对于全面理解产品质量至关重要。

---

## 32. 自托管NAT网关

**原文标题**: Self-hosting a NAT Gateway

**原文链接**: [https://www.awsistoohard.com/blog/self-hosting-nat-gateway](https://www.awsistoohard.com/blog/self-hosting-nat-gateway)

自建NAT网关降低AWS成本：实践与探索

---

## 33. Shop Sans 是用于弯曲文本路径的字体。

**原文标题**: Shop Sans is a typeface for curved text paths

**原文链接**: [https://www.futurefonts.com/hex/shop-sans](https://www.futurefonts.com/hex/shop-sans)

本文重点介绍了Shop Sans字体，该字体由HEX设计，可在Future Fonts上获取。其关键在于Shop Sans特别适合在弯曲的文本路径上使用。这表明该字体的形状和间距经过专门优化，适用于圆形或其他弯曲的布局。虽然文章片段简短，但暗示Shop Sans在这种非常规使用方式中具有独特的美学或技术优势。它在Future Fonts上发布的事实表明它是一项正在进行的工作，或者在不断更新和改进，可能会在开发过程中融入用户反馈。

---

## 34. 展示 HN: PolyGPT – ChatGPT、Claude、Gemini、Perplexity 回应并排比较

**原文标题**: Show HN: PolyGPT – ChatGPT, Claude, Gemini, Perplexity responses side-by-side

**原文链接**: [https://polygpt.app](https://polygpt.app)

PolyGPT是一款免费开源工具，旨在消除用户在不同AI平台之间切换的需求。它允许用户输入一次提示词，即可同时将其发送给ChatGPT、Gemini和Claude。然后，该工具会实时并排显示来自每个AI模型的响应，从而方便比较。PolyGPT可在Mac、Windows和Linux上下载。它的亮点功能包括支持多种模型（ChatGPT、Gemini和Claude）、在所有界面镜像提示词，以及100%免费、开源并优先考虑用户隐私。该项目也可在GitHub上访问。

---

## 35. 用余弦函数解决Fizz Buzz问题

**原文标题**: Solving Fizz Buzz with Cosines

**原文链接**: [https://susam.net/fizz-buzz-with-cosines.html](https://susam.net/fizz-buzz-with-cosines.html)

本文提出了一种利用三角函数解决 Fizz Buzz 问题的数学方法。作者 Susam Pal 首先使用符号函数（n, "Fizz", "Buzz", "FizzBuzz"）和一个索引函数 f(n) 来定义 Fizz Buzz 序列，该索引函数根据 n 是否能被 3 和 5 整除来确定使用哪个符号。

目标是找到 f(n) 的闭合形式表达式，该表达式仅使用基本数学运算和三角函数。首先，引入指示函数（I_m(n)，如果 m 能整除 n，则返回 1，否则返回 0），将 f(n) 简化为 `f(n) = I_3(n) + 2 * I_5(n)`。

文章的核心随后转向使用复指数和欧拉公式来表达这些指示函数。这最终导致用余弦函数替换指示函数。通过操纵复指数并使用欧拉公式，作者推导出 I_3(n) 和 I_5(n) 关于余弦函数的表达式。然后将这些表达式代入 f(n) 的公式中，从而得到一个闭合形式的三角表达式：

`f(n) = 11/15 + (2/3)cos(2πn/3) + (4/5)cos(2πn/5) + (4/5)cos(4πn/5)`。

最后，文章证明了该表达式也可以使用离散傅里叶变换 (DFT) 获得，从而验证了该表达式并突出了 Fizz Buzz 序列的周期性。文章提供了 Python 代码片段，说明了导出公式的实现。

---

## 36. Unity CEO Matthew Bromberg 关于扭转局势的访谈

**原文标题**: An Interview with Unity CEO Matthew Bromberg About Turnarounds

**原文链接**: [https://stratechery.com/2025/an-interview-with-unity-ceo-matthew-bromberg-about-turnarounds/](https://stratechery.com/2025/an-interview-with-unity-ceo-matthew-bromberg-about-turnarounds/)

本次Stratechery访谈嘉宾是Unity CEO Matthew Bromberg，他将分享其职业生涯和扭转战略。Bromberg此前曾在Zynga、EA、Major League Gaming和AOL任职，于18个月前接管Unity。

对话深入探讨了Bromberg的背景，从他对体育运动和复杂战略游戏的广泛兴趣，到他对文学理论的学术追求，他在那里培养了对游戏开发至关重要的系统思维能力。他从一位有抱负的教授转型到法学院，最终进入科技和媒体行业，然后加入了AOL。

在AOL，Bromberg获得了管理内容合作的宝贵经验。他讲述了自己如何通过理解合同并提出基于伙伴关系的新起点，挽救了AOL和Electronic Arts之间一项失败的数百万美元的交易。这导致他被EA招募。

这次访谈为进一步探索Bromberg在EA的经历奠定了基础，包括他在扭转《星球大战：旧共和国武士》中的作用，以及他在Zynga的工作和他目前为振兴Unity所做的努力，重点是他在整个职业生涯中所学到的经验教训。他强调了领导力中多样化视角的重要性，以及平衡作为CEO的分析和表演能力的重要性。

---

## 37. 初代Xbox平台的XBMC 4.0

**原文标题**: XBMC 4.0 for the Original Xbox

**原文链接**: [https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/](https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/)

XBMC 4.0发布：为初代Xbox媒体中心带来重大更新

---

## 38. 麦当劳正在失去低收入顾客。

**原文标题**: McDonald's is losing its low-income customers

**原文链接**: [https://www.latimes.com/business/story/2025-11-16/mcdonalds-is-losing-its-low-income-customers](https://www.latimes.com/business/story/2025-11-16/mcdonalds-is-losing-its-low-income-customers)

2025年11月发表的这篇文章探讨了快餐价格上涨如何影响低收入消费者，尤其是在麦当劳。由于牛肉和劳动力等餐厅必需品成本的增加，麦当劳来自低收入家庭的客流量出现了两位数的下降，这些家庭正努力应对包括住房、托儿和服装在内的全面上涨的开支。这一群体正越来越多地被高收入人群所取代。

文章强调了麦当劳过去如何依赖低收入消费者，21世纪初“一美元菜单”的成功就是例证。然而，通货膨胀和经济压力使麦当劳对许多人来说也变得不那么负担得起了。低收入家庭的消费信贷违约率急剧上升，很大一部分租房者面临成本负担，将收入的很大一部分用于住房。

经济学家描述了一种“K型经济”，即较富裕的消费者维持消费，而低收入人群则缩减开支。虽然麦当劳试图提供优惠套餐，但并未完全引起顾客的共鸣。其他企业也在探索类似的“经济衰退套餐”，以吸引对价格敏感的消费者。专家认为，关税、干旱和劳动力成本正在导致价格上涨，并对低收入家庭造成不成比例的影响。最终，企业对进一步提价持谨慎态度，因为他们感觉到经过多年的通货膨胀，消费者的容忍度有限。

---

## 39. 使用 SQLite 构建持久化执行引擎

**原文标题**: Building a Durable Execution Engine with SQLite

**原文链接**: [https://www.morling.dev/blog/building-durable-execution-engine-with-sqlite/](https://www.morling.dev/blog/building-durable-execution-engine-with-sqlite/)

本文探讨了如何利用 SQLite 创建一个持久化的执行引擎。“持久化”意味着该引擎可以从崩溃中恢复，并从中断处继续执行。核心思想可能是将工作流的状态持久化到 SQLite 中，以实现恢复和弹性。

Java 代码展示了一个基本的 "HelloWorldFlow" 类。它定义了一个流程（`sayHello` 方法，用 `@Flow` 注释），该流程迭代五次，并在每次迭代中调用一个步骤（`say` 方法，用 `@Step` 注释）。`say` 方法打印一个包含姓名和计数的问候语，并返回计数。`sayHello` 方法根据 `say` 方法的返回值计算总和，并打印最终总和。

与 SQLite 的可能联系是，`@Flow` 和 `@Step` 注释可能会触发引擎将有关执行当前状态的信息（例如，`i` 的值、`sum` 的状态、当前正在执行的步骤）存储在 SQLite 数据库中。这使得引擎能够在中断后恢复工作流程。

因此，本文很可能探讨了如何利用 SQLite 来持久化工作流状态，从而构建一个健壮且可恢复的执行环境，而 Java 代码则作为一个简单的例子来展示核心概念。

---

## 40. 制作小型RPG

**原文标题**: Making a Small RPG

**原文链接**: [https://jslegenddev.substack.com/p/making-a-small-rpg](https://jslegenddev.substack.com/p/making-a-small-rpg)

无法访问文章链接。

---

## 41. 多动症与单一导向性 (2023)

**原文标题**: ADHD and monotropism (2023)

**原文链接**: [https://monotropism.org/adhd/](https://monotropism.org/adhd/)

本文探讨了多动症和自闭症之间潜在的联系，并以单向性为视角，该理论最初旨在解释自闭症。单向性认为，自闭症患者倾向于将注意力高度集中在少数事物上，从而限制了对其他刺激的资源。

作者注意到多动症和自闭症诊断的高共现率，尽管它们在诊断手册中描述的特征看似矛盾（多动症主要表现为注意力障碍，自闭症主要表现为社交障碍）。文章认为，一个共同的潜在原因，可能是单向性，可以解释这种重叠。

作者提出，可以通过单向性的视角来理解冲动和注意力不集中（与多动症相关）：冲动是由于失去对专注注意力之外事物的意识，而注意力不集中则是由于难以将注意力从当前兴趣上转移。多动与刻板行为有关，但文章承认与多动症相关的认知跳跃和单向性“陷入”注意力隧道之间的紧张关系。这可以通过难以进入心流状态或天生注意力分散等因素来解释。作者还认为，连续单向性可能会被误认为是多向性。

最后，文章承认，单向性可能不是诊断手册中定义的自闭症的唯一原因，但其强度与其他因素结合，可能会导致社交差异和与自闭症相关的其他特征。理解内在的认知风格，而不仅仅是外在的表现，对于更细致地理解神经多样性至关重要。虽然还需要进一步的研究，但初步结果表明，两种诊断与单向性之间存在很强的相关性。

---

## 42. 半条命2中的时间旅行门漏洞

**原文标题**: A time-travelling door bug in Half Life 2

**原文链接**: [https://mastodon.gamedev.place/@TomF/115589875974658415](https://mastodon.gamedev.place/@TomF/115589875974658415)

文章是 Tom Forsyth 发布的一条 Mastodon 帖子，指向一个关于游戏开发中门相关的危险和问题的讨论。由于帖子结尾突兀，在没有更多信息或访问完整讨论内容的情况下，很难确定确切的背景。然而，鉴于 Forsyth 的背景和游戏开发的一般挑战，它可能指的是实现门机制的复杂性，这可能包括简单的碰撞问题到更复杂的问题，例如 AI 围绕门的导航、多人游戏中门状态的同步，或者为玩家创建令人信服且不易被利用的门交互。标题“半条命 2 中的时间旅行门 bug”表明，该讨论，或者至少 Forsyth 对它的贡献，特别提到了一个与游戏《半条命 2》中门相关的 bug，可能涉及由门交互触发的时间异常或故障。在没有讨论的全部内容的情况下，bug 的确切性质仍然未知，但它突显了像门这样看似简单的元素也可能在游戏开发中造成复杂且意想不到的问题。

---

## 43. 使用 Ansible 自动化无根 Docker 主机更新

**原文标题**: Automating rootless Docker host updates with Ansible

**原文链接**: [https://du.nkel.dev/blog/2025-11-15_docker-rootless-ansible/](https://du.nkel.dev/blog/2025-11-15_docker-rootless-ansible/)

无法访问文章链接。

---

## 44. 科学家现在知道蜜蜂可以处理时间，这在昆虫中尚属首次。

**原文标题**: Scientists now know that bees can process time, a first in insects

**原文链接**: [https://www.cnn.com/2025/11/12/science/bees-visual-stimulus-study-scli-intl](https://www.cnn.com/2025/11/12/science/bees-visual-stimulus-study-scli-intl)

一项新研究表明熊蜂能够处理光闪的时长来定位食物，这是昆虫具备此能力的首次证据。伦敦玛丽女王大学的研究人员设计了一个迷宫，让蜜蜂学会将短光闪与甜食联系起来，将长光闪与苦味食物联系起来。即使没有食物线索，蜜蜂也能区分这些光闪，证明了它们处理时间的能力。

这一发现挑战了之前认为昆虫是简单、僵化的反射机器的观点。研究人员称，考虑到光闪是新颖的人工刺激，这一点尤其引人注目。现在，熊蜂加入了包括人类在内的一小群能够区分长短时长的动物行列，类似于理解摩尔斯电码。

该研究旨在探索这种能力背后的神经机制，并了解蜜蜂在学习时间评估方面的认知差异。科学家们希望这一发现能够促进人们将蜜蜂视为具有复杂认知能力的复杂动物，而不仅仅是不思考的授粉者。该研究还提出了关于我们对时间感知的更广泛的问题，表明时间感知不仅仅是人类的特征。

Cintia Akemi Oi 和 Jolyon Troscianko 等专家强调了这项研究的重要性，突出了蜜蜂在自然生态环境内外所表现出的复杂的时间感和学习能力。他们指出，蜜蜂令人印象深刻的认知能力是用相对较小的大脑实现的，这表明复杂的认知并不总是需要庞大的大脑。

---

## 45. 单细胞海洋生物催生了一部极具影响力的图鉴

**原文标题**: Single-Celled Marine Organisms Resulted in an Influential Illustrated Book

**原文链接**: [https://lithub.com/how-the-discovery-of-single-celled-marine-organisms-resulted-in-one-of-the-most-influential-illustrated-books-ever-published/](https://lithub.com/how-the-discovery-of-single-celled-marine-organisms-resulted-in-one-of-the-most-influential-illustrated-books-ever-published/)

迈克尔·本森在文学中心发表的文章探讨了恩斯特·海克尔的插图书籍《自然界的艺术形态》的深远影响，该书的灵感来自于他对单细胞海洋生物放射虫的发现和研究。

海克尔最初不愿从事医学，后来在海洋生物学，特别是放射虫的研究中找到了自己的使命。这些微观生物，凭借其复杂的几何硅骨骼，深深地吸引了他。他运用创新的显微技术和艺术技巧创作了详细的图纸，并在1862年出版了他的第一本关于放射虫的专著。

他的作品立即获得了认可，包括查尔斯·达尔文的赞扬。 海克尔继续研究海洋生物，并为挑战者号考察报告做出了重大贡献，成为放射虫方面的权威。

《自然界的艺术形态》于1899年至1904年间出版，成为海克尔的杰作。 这本书的石版画由他与阿道夫·吉尔奇合作创作，展示了自然形态的美丽和复杂性，尤其是放射虫。 该书的影响力超越了科学，启发了新艺术运动和青年风格运动的艺术家、建筑师和设计师。 甚至一座宏伟的建筑结构，即1900年巴黎世博会的纪念门，也是基于海克尔的放射虫插图设计的。

文章强调了海克尔作品的持久影响，特别是《自然界的艺术形态》，它仍然是一本具有影响力的出版物，连接了艺术和科学，并向更广泛的读者揭示了自然界的复杂之美。

---

## 46. 枢轴机器人 (YC W24) 招聘工业自动化硬件工程师

**原文标题**: Pivot Robotics (YC W24) Is Hiring for an Industrial Automation Hardware Engineer

**原文链接**: [https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls](https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls)

Pivot Robotics (YC W24) 正在招聘机械工程师（控制方向）。这是一家人工智能机器人公司，专注于为高多样性制造自动化工业机器人手臂。他们的首款产品针对危险的金属零件打磨任务，其软件目前已部署在一家大型铸铁厂的 10 多台机器人上。

该职位涉及构建和部署控制面板、将传感器和执行器与 PLC 和机器人控制器集成、设计安全系统、排除机电子系统故障、与软件和电气工程师协作，以及支持客户现场的机器人单元设置。 他们正在寻找拥有机械、机电一体化或机器人工程学士或硕士学位，并具有 1-2 年机械设计和控制系统集成经验的人员。 主要资格包括构建控制面板的经验、熟悉安全硬件和标准、了解气动系统和控制回路、精通 CAD、在实验室和工厂环境中拥有实践经验以及愿意出差。

该公司位于旧金山，团队有 6 人，提供 10 万美元 - 13.5 万美元的薪水和 0.40% - 0.75% 的股权。 Pivot Robotics 将现成的机器人和视觉传感器与基础视觉模型的最新进展相结合，使工业机器人手臂能够适应。 该公司由 Siddharth Girdhar 和 Vignesh Rajmohan 创立。

---

## 47. 本博客的内容

**原文标题**: What this blog is about

**原文链接**: [https://randomascii.wordpress.com/2025/03/25/what-this-blog-is-about/](https://randomascii.wordpress.com/2025/03/25/what-this-blog-is-about/)

Bruce Dawson的博客文章《本博客是关于什么的》以非技术受众能够理解的方式概括了他所涵盖的主题。他将个人轶事与对Windows性能和稳定性问题的调查性报道相结合。

Dawson重点介绍了几个有影响的发现，包括一个导致桌面图标重新排列变慢的Windows漏洞，一个源于Windows缺陷的Chrome/Gmail性能漏洞，以及一个导致构建系统故障的Windows内核磁盘缓存漏洞。他强调，他的调查促成了微软和谷歌实施的修复，使众多用户受益。

他还提到了他最受欢迎的文章：一本用于准确比较计算机上的数字的食谱书。

Dawson最后分享了他作为一名专注于优化和可靠性的退休程序员的背景，以及他对独轮车、曲棍球和杂耍等各种兴趣。

---

## 48. PNG图像中的EXIF方向信息不用于image-orientation: from-image

**原文标题**: EXIF orientation info in PNGs isn't used for image-orientation: from-image

**原文链接**: [https://bugzilla.mozilla.org/show_bug.cgi?id=1627423](https://bugzilla.mozilla.org/show_bug.cgi?id=1627423)

此错误报告详细描述了 Firefox 浏览器中 `image-orientation: from-image` CSS 属性无法正确解析 PNG 图像中嵌入的 EXIF 图像方向数据的缺陷，与 JPEG 以及 Safari 和 Chrome 等其他浏览器不同。这导致 PNG 图像的旋转方向与预期显示不符，即使 EXIF 数据指定了旋转（例如，“顺时针旋转 90 度”）。

报告人 Eric Portis 提供了一个测试用例 URL 来展示这种差异。进一步调查显示，Firefox 连同 Chrome 和 Safari，都无法正确处理附加在 PNG 文件末尾的 EXIF 数据，这可能是由于渐进式渲染的考虑。然而，Safari 如果 EXIF 方向数据出现在文件的前面，则会识别它。

Cameron McCormack 指出，PNG 通过 eXif 数据块支持方向数据，并且实现是可能的，尤其是在数据块出现在图像数据之前的情况下。该错误最终被标记为 bug 1682759 的副本，这意味着后者的修复也应该解决这个问题。该问题被认为是与 Chrome 和 Safari 之间的奇偶校验问题以及 Web 兼容性问题。W3C PNG 规范支持此功能。最后，经过近 5 年的等待，该错误已关闭，状态为 RESOLVED/DUPLICATE (已解决/重复)。

---

## 49. 专家称，百忧解治疗儿童抑郁症并不比安慰剂有效

**原文标题**: Prozac 'no better than placebo' for treating children with depression, experts

**原文链接**: [https://www.theguardian.com/society/2025/nov/20/prozac-no-better-than-placebo-for-treating-children-with-depression-experts-say](https://www.theguardian.com/society/2025/nov/20/prozac-no-better-than-placebo-for-treating-children-with-depression-experts-say)

一项对试验数据的新审查表明，百忧解（氟西汀）在治疗儿童和青少年抑郁症方面并不比安慰剂更有效，促使专家呼吁修改临床指南。研究人员对1997年至2024年间的12项百忧解试验进行了荟萃分析，发现该药物对抑郁症状的改善在临床上不显著，同时存在体重增加、睡眠障碍、注意力不集中和自杀意念增加等副作用风险。

作者认为，英国、美国和加拿大目前的指南忽视了百忧解与安慰剂相比无效的证据，并继续建议将其用于患有抑郁症的年轻人。他们主张将重点放在理解年轻人抑郁症的根本原因，并通过替代方法解决促成因素。

虽然 NICE 建议将心理疗法作为治疗儿童和青少年抑郁症的一线治疗方法，但他们也表示，在某些情况下，对于中度至重度抑郁症，可以考虑将抗抑郁药与心理疗法结合使用，并且只能在定期的专家监督下进行。

抗抑郁药对儿童的长期影响知之甚少，一些研究表明，长期副作用在停药后仍可能持续存在。英国皇家精神科医学院的一位发言人敦促谨慎解读该研究，并强调临床指南会考虑平均效应量之外的因素，包括安全性和患者偏好。

---

## 50. 带类型的集合论

**原文标题**: Set Theory with Types

**原文链接**: [https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html](https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html)

本文探讨了使用类型集合论作为数学和形式化中策梅洛-弗兰克尔 (ZF) 集合论的替代方案。它将 ZF 的“一切皆集合”方法与类型理论进行对比，后者要求元素必须属于预定义的类型或类，从而避免了诸如 x ∈ x 这样的无意义结构。

作者强调了 de Bruijn 1973 年的论文，该论文提倡“带类型限制的集合论”，以此作为 AUTOMATH 语言的动机。De Bruijn 质疑 ZF 中庞大的通用集合的必要性，认为类型系统足以满足大多数数学目的。作者借鉴了 Isabelle/HOL 的经验，支持这一观点。

本文解释了源自《数学原理》并在高阶逻辑中形式化的类型集合论如何提供诸多优势，例如对集合和谓词的直观处理。它描述了类型集合论的要素：类型化并集、交集、补集、幂集、函数空间等。

虽然 ZF 集合论具有优势，但作者指出，对于许多应用来说，它过于庞大。本文认为，通过将 ZF 作为高阶逻辑中的一个独立类型，可以保留两个系统的灵活性和优势。此外，作者介绍了世袭有限集 (hf) 作为高阶逻辑中一种更简单的集合论方法，适用于在计算中建模数据和状态空间。

---

## 51. 纳米香蕉 Pro

**原文标题**: Nano Banana Pro

**原文链接**: [https://blog.google/technology/ai/nano-banana-pro/](https://blog.google/technology/ai/nano-banana-pro/)

谷歌DeepMind推出Nano Banana Pro，基于Gemini 3 Pro构建的先进图像生成和编辑模型。在先前Nano Banana模型的基础上，Pro版本提供增强的推理能力和现实世界知识，以实现卓越的图像创作。

主要功能包括基于改进的推理和通过Google搜索集成访问实时信息来生成准确、富含上下文的视觉效果。 Nano Banana Pro擅长生成具有准确且清晰的多语言文本的图像，从而能够创建模型、海报和本地化内容。

该模型提供具有一致品牌的高保真视觉效果，支持高达14个图像输入，同时保持多个人物的一致性。 它拥有先进的创意控制，包括本地化编辑、相机角度调整、焦点操作和复杂的色彩分级。 提供2K和4K的输出分辨率。

Nano Banana Pro可在各种Google产品中使用。 它正在 Gemini 应用、Google Ads、Workspace（Google Slides和Vids）、Gemini API、Google AI Studio、Google Antigravity、Vertex AI 和 Flow（Google 的 AI 电影制作工具）中推出。

为了提高透明度，所有由 Google AI 工具生成的图像都嵌入了 SynthID 数字水印，并且 Gemini 应用中提供了一个验证工具来检查图像是否由 Google AI 生成。 可见水印用于免费和 Google AI Pro 层用户，而 Google AI Ultra 订阅者和 Google AI Studio 内将删除水印。

---

## 52. 巴西前总统博索纳罗被捕，法院称以防“逃逸”

**原文标题**: Brazil's ex-president Bolsonaro arrested to prevent 'escape' court says

**原文链接**: [https://www.cnn.com/2025/11/22/americas/brazil-jair-bolsonaro-arrested-intl](https://www.cnn.com/2025/11/22/americas/brazil-jair-bolsonaro-arrested-intl)

巴西前总统博索纳罗在其巴西利亚住所被捕，以防止其在因领导政变企图而即将开始服刑前“试图逃脱”。逮捕令由联邦警察提出，并经最高法院授权。

最高法院援引了对其子，参议员弗拉维奥·博索纳罗组织的守夜活动的担忧，认为该活动可能演变成大规模事件，从而为博索纳罗的逃脱提供便利。法院还收到有关博索纳罗电子监控设备被破坏的信息，进一步加剧了对其逃跑计划的怀疑。

博索纳罗的律师正在对逮捕提出上诉，驳斥了逃跑企图的说法，并强调了他脆弱的健康状况，认为他的监禁可能会危及他的生命。他们还为计划举行的守夜活动辩护，认为这是集会的权利。

博索纳罗今年早些时候被判处 27 年徒刑，罪名是企图在 2022 年大选中输给路易斯·伊纳西奥·卢拉·达席尔瓦后继续掌权，目前已被软禁。他被判犯有多项罪名，包括策划政变、参与犯罪组织以及煽动暴力袭击国家机构，即 2023 年 1 月 8 日其支持者冲击政府大楼事件。博索纳罗坚称审判是政治迫害。多名高级军事官员和一名联邦警察也因参与政变企图而于近日被判刑。

---

## 53. Libpng 1.6.51：修复四个缓冲区溢出漏洞

**原文标题**: Libpng 1.6.51: Four buffer overflow vulnerabilities fixed

**原文链接**: [https://www.openwall.com/lists/oss-security/2025/11/22/1](https://www.openwall.com/lists/oss-security/2025/11/22/1)

该公告详细说明了 libpng 1.6.51 的发布，旨在解决影响 1.6.0 至 1.6.50 版本的四个缓冲区溢出漏洞 (CVE-2025-64505、CVE-2025-64506、CVE-2025-64720 和 CVE-2025-65018)。 其中两个漏洞的严重等级为高，两个为中。

*   **CVE-2025-64505（中等）：** 由于错误的调色板索引，`png_do_quantize` 中存在堆缓冲区过度读取。
*   **CVE-2025-64506（中等）：** 在特定输入设置下，`png_write_image_8bit` 中存在堆缓冲区过度读取。
*   **CVE-2025-64720（高）：** 由于调色板预乘，`png_image_read_composite` 中存在越界读取。
*   **CVE-2025-65018（高）：** 处理具有 8 位输出的 16 位隔行 PNG 时，`png_combine_row` 中存在堆缓冲区溢出。

利用漏洞需要用户通过处理恶意 PNG 文件进行交互。后果包括信息泄露和拒绝服务，以及对于 CVE-2025-65018，在某些堆配置中可能导致任意代码执行。 每个 CVE 的修复程序都通过 GitHub 提交链接提供。 对于 CVE-2025-65018，必须应用所有提交。 强烈建议用户立即升级到 libpng 1.6.51。 这些漏洞由 Samsung-PENTEST、weijinjinnihao 和 yosiimich 发现并报告，Fabio Gritti 和 John Bowler 进行了分析。

---

## 54. 我把转盘电话改造成了会议听筒。

**原文标题**: I converted a rotary phone into a meeting handset

**原文链接**: [https://www.stavros.io/posts/i-converted-a-rotary-phone-into-a-meeting-handset/](https://www.stavros.io/posts/i-converted-a-rotary-phone-into-a-meeting-handset/)

作者出于对会议的“深恶痛绝”和一位同事的启发，将一台老式西门子转盘电话改造成了会议听筒。 目标是创造一种令人满意的方式，可以在令人沮丧的虚拟会议期间“狠狠挂断”电话。

该项目涉及修改电话，使其既能用作声卡，又能用作键盘以控制会议。 作者最初尝试使用 RP2040 微控制器来同时实现这两个功能，并利用 LLM (Claude Opus) 来编写必要的代码。 在花费了 50 美元并发现代码变得越来越有错误之后，作者切换到了备用方案。

备用方案包括使用 USB 集线器将一个廉价的 1.69 美元 USB 声卡和 RP2040（作为键盘）通过单个 USB 连接连接到计算机。 使用定制的 3D 打印连接器将电话的内部线路连接到声卡组件。 RP2040 被编程为检测到听筒挂断时发送特定的击键以退出会议，并模拟在转盘上拨打的号码的键盘输入。

最终设置包括 USB 集线器将声卡（用焊接引脚修改以连接听筒连接器）和 RP2040（连接到电话的挂钩和转盘）连接到计算机。 一个视频演示了成功的“挂断”动作。 该项目的代码可在 GitHub 上找到。

---

## 55. 非常规花瓶模式3D打印

**原文标题**: 3D printing with unconventional vase mode

**原文链接**: [https://vorpal.se/posts/2025/jun/23/3d-printing-with-unconventional-vase-mode/](https://vorpal.se/posts/2025/jun/23/3d-printing-with-unconventional-vase-mode/)

本文探讨了3D打印花瓶模式的非常规应用，目标是熟悉基础知识的高级用户。花瓶模式通常快速打印单层空心物体且无接缝，但缺乏内部几何结构、支撑和顶层。

本文详细介绍了扩展花瓶模式功能的技巧：

*   **通过狭缝实现内部几何结构：** 在模型中添加薄（0.0001毫米）的狭缝，使切片软件能够创建内部支撑，本质上是模拟您自己的填充。 关键是，PrusaSlicer中的“切片间隙闭合半径”必须设置为0。
*   **双层壁：** 通过在空心内部创建一个狭缝，并确保零件的宽度与两个周长匹配，您可以实现双层壁花瓶模式打印，从而提高强度。 这可以扩展到将内部几何结构锚定到壁上。
*   **挤出宽度：** 增加挤出宽度（高达喷嘴直径的2倍或更高）可以进一步提高花瓶模式打印的强度。
*   **伪花瓶模式：** 通过手动配置切片软件设置来模拟花瓶模式：单层周长，无顶层/填充/支撑，并禁用“确保垂直外壳厚度”。 虽然缺乏连续螺旋，但它提供了灵活性，可以根据打印的特定区域定制设置。 倾斜接缝可以隐藏接缝伪影。

本文使用在棒子上打印球体的案例研究来说明“伪花瓶模式”以及微调设置的优势。 结论是，花瓶模式和“伪花瓶模式”在功能性零件中未得到充分利用，从而节省了重量和打印时间。 作者提供了一份备忘单，总结了关键点和设置。

---

## 56. 内存芯片可能成为人工智能的下一个瓶颈 (2024)

**原文标题**: Memory chips could be the next bottleneck for AI (2024)

**原文链接**: [https://economist.com/business/2024/10/24/memory-chips-could-be-the-next-bottleneck-for-ai](https://economist.com/business/2024/10/24/memory-chips-could-be-the-next-bottleneck-for-ai)

无法访问文章链接。

---

## 57. 命令行

**原文标题**: Command Lines

**原文链接**: [https://www.wreflection.com/p/command-lines-ai-coding](https://www.wreflection.com/p/command-lines-ai-coding)

本文题为“命令行”，探讨了人工智能编码助手快速发展的态势及其对软件开发的影响。文章强调了人工智能编码工具市场的指数级增长，这是由渴望提高生产力的工程师所推动的，并认为该市场正在细分为三种用户类型：手工编码者（对人工智能持怀疑态度）、氛围编码者（非工程师使用人工智能进行快速原型设计）和架构师+人工智能编码者（工程师战略性地使用人工智能进行样板代码和常规任务）。

作者将市场划分为面向非工程师的“放手”工具（如Lovable和Replit）和面向专业开发人员的“亲力亲为”工具（如Cursor和Github Copilot）。文章提到了Cursor显著的收入增长及其内部模型（如Composer-2）的开发。

文章认为模型质量是人工智能编码领域的一个关键差异化因素，并引用了Claude Code日益增长的受欢迎程度。尽管有新进入者，但像微软（Github Copilot）这样的现有企业利用现有的客户关系和捆绑销售来维持市场份额。作者最后强调，人工智能编码工具正在将工程师从繁琐的任务中解放出来，使他们能够专注于更高层次的思考。最终的赢家将是提供最佳模型质量、超越基本功能的特性以及用户粘性的工具。

---

## 58. Infinibay LXD 容器

**原文标题**: Infinibay LXD Container

**原文链接**: [https://github.com/Infinibay/lxd](https://github.com/Infinibay/lxd)

本文档描述了 Infinibay LXD 部署，这是一种用于 Infinibay VDI 管理平台的容器化解决方案，采用 LXD（Linux 容器）。相比于特权模式容器，它具有原生 KVM 访问、完整的 systemd 支持以及更好的安全隔离等优势。该部署通过自动检测软件包管理器和 LXD 安装方法，支持多种 Linux 发行版。

该架构包含四个 LXD 容器：`infinibay-postgres` (数据库)、`infinibay-redis` (缓存)、`infinibay-backend` (API、libvirt-node、infiniservice、KVM 访问) 和 `infinibay-frontend` (Web 界面)。

本文档提供了一个快速入门指南，包括安装说明、环境配置以及用于部署和管理容器的命令。关键命令包括 `setup.sh` (安装 LXD 和依赖项)、`newgrp lxd` (激活 LXD 组成员身份) 和 `run.sh` (管理容器、配置和启动服务)。`run.sh` 脚本提供各种子命令，用于执行应用配置、配置、销毁、重启和检查容器状态等任务。

文章强调了 `run.sh` 提供的智能编排，它可以自动处理容器创建、配置和启动。它还详细介绍了当前实现的状况，突出了已完成的功能，如自动化配置脚本、资源限制、共享目录和网络连接。同时，它也提及了仍然需要手动执行的步骤，例如安装 npm 依赖项、运行数据库迁移和启动 Infinibay 服务。最后，它将 LXD 部署与原生 Infinibay 安装程序进行了比较，建议在 LXD 配置完全自动化之前，在生产环境中使用后者。

---

## 59. 安卓和iPhone用户现在可以共享文件了，从Pixel 10开始。

**原文标题**: Android and iPhone users can now share files, starting with the Pixel 10

**原文链接**: [https://blog.google/products/android/quick-share-airdrop/](https://blog.google/products/android/quick-share-airdrop/)

谷歌推出新功能，让安卓“快速分享”与苹果“隔空投送”无缝协作，简化安卓设备（初期为Pixel 10系列）与iPhone之间的文件共享。主要目的是方便亲友间的文件共享，无论他们使用何种移动操作系统。

该功能优先考虑安全性，整合了经独立安全专家测试的强大安全措施，以保护用户数据。 此次跨平台兼容性举措，延续了谷歌之前在RCS消息和未知追踪器警报方面的努力，表明其致力于提升不同操作系统之间的互操作性。

该功能首先在Pixel 10系列设备上推出，公司计划未来将其扩展到更多安卓设备。 用户可以通过一段配套视频，在Pixel 10 Pro上看到该功能的实际应用。

---

## 60. 在家教育人数创新高

**原文标题**: Homeschooling hits record numbers

**原文链接**: [https://reason.com/2025/11/19/homeschooling-hits-record-numbers/](https://reason.com/2025/11/19/homeschooling-hits-record-numbers/)

美国家庭教育显著增长，远远超过疫情前水平，即使在取消新冠限制后，仍保持上升趋势。多州数据显示，家庭教育比例大幅增加，部分州报告创历史新高。尽管少数州略有下降，但总体趋势表明人们对自主教育的兴趣依然强烈且持久。

专家认为，这一激增源于人们对传统公立学校日益增长的不满，理由是对僵化、政治化、不良结果以及疫情期间经历的担忧。家长们正在寻求符合他们偏好的替代方案，并希望对孩子的教育有更大的控制权。

家庭教育并非这一转变的唯一受益者。私立学校和特许学校等其他非公立选择的入学人数也在发生变化。研究表明，随着越来越多的家庭选择替代教育途径，公立学校未来几年可能面临入学人数大幅下降。

家长对K-12教育的不满情绪达到十年来的最高点，大多数人认为它正朝着错误的方向发展。家庭教育在家长中享有很高的支持率，反映出人们对这种教育方式的接受和偏爱程度越来越高。疫情暴露了远程学习的缺点，并突显了对课程质量和潜在灌输的担忧，进一步推动家庭转向家庭教育和其他替代方案。 这一趋势表明美国家庭对教育的看法发生了根本性转变，家庭教育正成为一种越来越受欢迎和主流的选择。

---

## 61. 仅使用PL/pgSQL的RRules（是的，处理RSCALE）

**原文标题**: RRules (yes handling RSCALE) using only PL/pgSQL

**原文链接**: [https://github.com/sirrodgepodge/rrule_plpgsql](https://github.com/sirrodgepodge/rrule_plpgsql)

`rrule_plpgsql` 是 iCalendar RRULE (RFC 5545 & RFC 7529) 的一个纯 PL/pgSQL 实现，适用于 PostgreSQL，可在数据库内直接进行重复发生的计算。它避免了 C 扩展，确保在所有 PostgreSQL 环境中的兼容性，包括 AlloyDB、RDS 和 Azure Database 等托管服务。

主要优点包括：无需编译、完全支持带 DST 处理的时区、跨环境的一致行为，以及单计划操作显著更快的性能（比 Node.js 快 50-75 倍）。其关键优势在于与查询引擎的紧密集成，允许基于集合的操作（JOIN）、原生 WHERE/聚合，以及内存高效的流式传输，而无需外部数据传输。

安装简单，可以使用 `npm` 或直接 SQL 安装。该库提供全面的文档，涵盖安装、示例用法（订阅账单、批量更新、冲突检测）、API 参考、RFC 合规性和安全性。

它支持各种频率（DAILY、WEEKLY、MONTHLY、YEARLY）和修饰符（COUNT、UNTIL、INTERVAL、BYDAY 等），包括 SKIP 和 RSCALE。虽然标准安装提供安全且常用的频率，但子日频率（HOURLY、MINUTELY、SECONDLY）可通过单独安装获得，并带有安全警告。

该库提供用于生成和查询发生的事件的核心函数，以及重叠检测等实用程序。 欢迎贡献，强调彻底的测试和遵守 RFC 规范。 该库在 MIT 许可下获得许可。

---

## 62. Olmo 3：引领开源AI，在模型流程中开辟道路

**原文标题**: Olmo 3: Charting a path through the model flow to lead open-source AI

**原文链接**: [https://allenai.org/blog/olmo3](https://allenai.org/blog/olmo3)

AI2于2025年11月20日发布的Olmo 3旨在通过提供最先进的语言模型以及创建和修改这些模型所需的整个模型流程——每个阶段、检查点、数据集和依赖项——来推进开源AI。 这种全面的方法可以培养信任，实现有效的适应、协作和创新。

核心是Olmo 3-Think (32B)，一个思考模型，允许检查中间推理轨迹及其来源。 Olmo 3系列包括参数为7B和32B的模型，包括：Olmo 3-Base (7B, 32B)，一个强大的基础模型，在编程、阅读和数学方面与其他开放权重模型竞争；Olmo 3-Think (7B, 32B)，一个适合RL研究、长程推理和复杂实验的推理模型；Olmo 3-Instruct (7B)，一个专注于聊天的模型，擅长指令跟随和工具使用；以及Olmo 3-RL Zero (7B)，一种用于引导复杂推理行为的强化学习途径。

Olmo 3为各种应用程序提供了记录在案的开发路径。 用户可以自定义每个训练阶段、数据集和RL目标，以创建自己的系统。 所有组件均以宽松的开源许可发布，包括数据、代码、模型权重和检查点。 Olmo 3在广泛的基准测试套件中表现出色，其中Olmo 3-Base 32B和Olmo 3-Think 32B在其各自类别中优于其他完全开放的模型。

Olmo 3采用仅解码器Transformer架构和多阶段训练管道，重点关注数据管理和新的强化学习框架。 扩展的训练数据和数据集管理方法加强了Olmo 3的功能。

---

## 63. 谷歌告知员工需每6个月将容量翻倍以满足AI需求

**原文标题**: Google tells employees it must double capacity every 6 months to meet AI demand

**原文链接**: [https://arstechnica.com/ai/2025/11/google-tells-employees-it-must-double-capacity-every-6-months-to-meet-ai-demand/](https://arstechnica.com/ai/2025/11/google-tells-employees-it-must-double-capacity-every-6-months-to-meet-ai-demand/)

谷歌正积极扩大其AI基础设施以满足激增的需求，目标是每六个月将容量翻一番，并在4-5年内实现一千倍的增长，同时保持成本和能源效率。这种快速扩张的驱动力既来自自然增长的用户兴趣，也来自AI与现有服务的整合。

该公司面临着跟上OpenAI等竞争对手步伐的挑战，后者正在大力投资数据中心。一个关键瓶颈是英伟达GPU的供应有限，影响了谷歌部署新AI功能的能力。

为了克服这些挑战，谷歌正专注于三大战略：建设物理基础设施、开发更高效的AI模型以及设计定制硅芯片，如其张量处理单元（TPU）。谷歌声称其最新一代TPU的能效显著提高。

尽管人们担心可能存在AI泡沫，但谷歌认为投资不足的风险大于产能过剩的风险，这表明了对AI的长期承诺。谷歌领导层预计未来几年AI领域的竞争将非常激烈，满足云和计算需求的压力也会增大。

---

## 64. 莱斯特：独立动画和复古游戏开发中转描技术的新纪元

**原文标题**: Lester: A New Era for Rotoscoping in Indie Animation and Retro Game Development

**原文链接**: [https://rtous.github.io/lester/](https://rtous.github.io/lester/)

Lester：一款加速参考动画工作流程的转描动画与视频分割编辑器。它专为独立动画和复古游戏开发设计，通过自动化繁琐的帧编辑，实现精确的编辑、分割和风格化，从而提供更快速的工作流程。其关键卖点是完全不使用生成式AI，确保原创性、可预测的结果以及完全的用户控制。所有处理都在本地运行，消除了对数据隐私、云处理或订阅费用的担忧。

Lester目前可在Windows（CPU和GPU版本）和macOS上下载。开发者强调Lester是一个不断发展的工具，并鼓励用户提供反馈以供未来开发。用户可以在该项目的GitHub存储库上报告问题、建议功能并了解更多信息。感兴趣了解该项目目标及其在现代转描工作流程中地位的人，还可以查阅新闻稿。本质上，Lester旨在为转描提供一个可靠且可控的环境，迎合那些优先考虑精确性和原创性而非AI辅助解决方案的艺术家。

---

## 65. 展示HN：Vibe Prolog

**原文标题**: Show HN: Vibe Prolog

**原文链接**: [https://github.com/nlothian/Vibe-Prolog](https://github.com/nlothian/Vibe-Prolog)

此“Show HN”帖子介绍 Vibe Prolog，一个使用 Claude Code (AI) 创建的 Prolog 解释器，花费了即将到期的 220 美元免费额度。作者已 20 年未使用 Prolog，却在一个周末通过手机偶然“vibe-coded”（随心编程）了这个解释器。

该项目的目的是通过一组规则探索 AI 生成代码的极限：无人为编写的代码，避免刻意马虎，最大程度地使用工具（测试、代码审查、安全审计），努力实现高质量的 AI 生成代码，并保持有趣、轻松的方式。

作者强调由于 AI 生成代码的功能和版权状况不确定，请谨慎使用，并建议使用现有的、成熟的 Prolog 实现。然而，作者积极鼓励大家贡献，特别是通过 pull request 的形式进行“vibe contributions”（随心贡献），并欢迎工具供应商集成他们的工具。帖子包含了解释器运行的示例。

---

## 66. 你能把一头牛带到牛津吗？

**原文标题**: Can you take an ox to Oxford?

**原文链接**: [https://alexwlchan.net/2025/ox-in-oxford/](https://alexwlchan.net/2025/ox-in-oxford/)

This article explores whether the £5 Oxford congestion charge applies to an ox-drawn cart. Madeline Odent posed the initial question on Twitter, prompting an investigation into the legal definitions surrounding the charge.

The author delves into the Oxfordshire County Council's "Charging Order," which applies to Class M1 vehicles. This leads to further exploration of UK legislation, including the "Road User Charging and Workplace Parking Levy (Classes of Motor Vehicles) (England) Regulations 2001" and the Road Traffic Act 1988. The crucial point is that the legislation defines "motor vehicle" as "mechanically propelled." Since an ox is not a "mechanically propelled vehicle," it is argued that an ox-drawn cart would not be subject to the congestion charge.

The author also highlights the exclusion of certain unconventional vehicles, like Reliant Robins and Peel P50s, based on their classification within the legislative framework. Despite having number plates, these vehicles, technically exempt, would likely be charged due to the camera-based enforcement system.

The conclusion is that an ox-drawn cart, lacking a number plate and not being mechanically propelled, is exempt from Oxford's congestion charge. The article ends with a reflection on the accessibility of UK legislation and how public access promotes transparency and accountability, even when addressing seemingly absurd legal questions.


---

## 67. Tibetan Declaration of Independence

**原文标题**: Tibetan Declaration of Independence

**原文链接**: [https://thus.org/tibetan-declaration-of-independence/](https://thus.org/tibetan-declaration-of-independence/)

This document is a proclamation issued by the 13th Dalai Lama in 1913, effectively declaring Tibet's independence. The Dalai Lama addresses all Tibetan people, referencing a historical relationship with China based on benefactor and priest, not subordination. He recounts the events leading to his exile to India due to Chinese attempts to colonize Tibet, and the subsequent collapse of the Manchu empire, leading to the expulsion of Chinese troops.

Having returned to Tibet, the Dalai Lama outlines several duties for the Tibetan people to ensure peace, happiness, and the preservation of their nation. These include: preserving Buddhist institutions and traditions, ensuring fair governance by civil and military officials, and protecting Tibet's independence. He specifically forbids severe punishments like amputation and addresses issues of land ownership and cultivation.

The proclamation emphasizes Tibet's status as a small, religious, and independent nation that must defend itself and keep up with the rest of the world. Border residents are instructed to be vigilant and report suspicious activity, while internal development is encouraged by allowing the cultivation of vacant lands. The document concludes by directing that the proclamation be posted and recorded throughout Tibet.


---

## 68. The Strange Afterlife of Hilma af Klint, Painting’s Posthumous Star

**原文标题**: The Strange Afterlife of Hilma af Klint, Painting’s Posthumous Star

**原文链接**: [https://www.newyorker.com/magazine/2025/11/24/the-strange-afterlife-of-hilma-af-klint-paintings-posthumous-star](https://www.newyorker.com/magazine/2025/11/24/the-strange-afterlife-of-hilma-af-klint-paintings-posthumous-star)

生成摘要时出错

---

## 69. How a French judge was digitally cut off by the USA

**原文标题**: How a French judge was digitally cut off by the USA

**原文链接**: [https://www.heise.de/en/news/How-a-French-judge-was-digitally-cut-off-by-the-USA-11087561.html](https://www.heise.de/en/news/How-a-French-judge-was-digitally-cut-off-by-the-USA-11087561.html)

生成摘要时出错

---

## 70. Interactive World History Atlas Since 3000 BC

**原文标题**: Interactive World History Atlas Since 3000 BC

**原文链接**: [http://geacron.com/home-en/](http://geacron.com/home-en/)

生成摘要时出错

---

## 71. The Untold History of Arduino (2016)

**原文标题**: The Untold History of Arduino (2016)

**原文链接**: [https://arduinohistory.github.io/](https://arduinohistory.github.io/)

生成摘要时出错

---

## 72. Boom, bubble, bust, boom. Why should AI be different?

**原文标题**: Boom, bubble, bust, boom. Why should AI be different?

**原文链接**: [https://crazystupidtech.com/2025/11/21/boom-bubble-bust-boom-why-should-ai-be-different/](https://crazystupidtech.com/2025/11/21/boom-bubble-bust-boom-why-should-ai-be-different/)

生成摘要时出错

---

## 73. Two recently found works of J.S. Bach presented in Leipzig [video]

**原文标题**: Two recently found works of J.S. Bach presented in Leipzig [video]

**原文链接**: [https://www.youtube.com/watch?v=4hXzUGYIL9M#t=15m19s](https://www.youtube.com/watch?v=4hXzUGYIL9M#t=15m19s)

生成摘要时出错

---

## 74. NTSB Preliminary Report – UPS Boeing MD-11F Crash [pdf]

**原文标题**: NTSB Preliminary Report – UPS Boeing MD-11F Crash [pdf]

**原文链接**: [https://www.ntsb.gov/Documents/Prelimiary%20Report%20DCA26MA024.pdf](https://www.ntsb.gov/Documents/Prelimiary%20Report%20DCA26MA024.pdf)

生成摘要时出错

---

## 75. Hilbert space: Treating functions as vectors

**原文标题**: Hilbert space: Treating functions as vectors

**原文链接**: [https://eli.thegreenplace.net/2025/hilbert-space-treating-functions-as-vectors/](https://eli.thegreenplace.net/2025/hilbert-space-treating-functions-as-vectors/)

生成摘要时出错

---

## 76. FAWK: LLMs can write a language interpreter

**原文标题**: FAWK: LLMs can write a language interpreter

**原文链接**: [https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html](https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html)

生成摘要时出错

---

## 77. The Lions Operating System

**原文标题**: The Lions Operating System

**原文链接**: [https://lionsos.org](https://lionsos.org)

生成摘要时出错

---

## 78. Show HN: My hobby OS that runs Minecraft

**原文标题**: Show HN: My hobby OS that runs Minecraft

**原文链接**: [https://astral-os.org/posts/2025/10/31/astral-minecraft.html](https://astral-os.org/posts/2025/10/31/astral-minecraft.html)

生成摘要时出错

---

## 79. When functions dissolve (2020)

**原文标题**: When functions dissolve (2020)

**原文链接**: [https://rubber-duck-typing.com/posts/2020-12-12-when-functions-dissolve.html](https://rubber-duck-typing.com/posts/2020-12-12-when-functions-dissolve.html)

生成摘要时出错

---

## 80. Private Equity's New Venture: Youth Sports

**原文标题**: Private Equity's New Venture: Youth Sports

**原文链接**: [https://jacobin.com/2025/11/youth-sports-hockey-private-equity](https://jacobin.com/2025/11/youth-sports-hockey-private-equity)

生成摘要时出错

---

## 81. 我最喜欢的数学题

**原文标题**: My Favorite Math Problem

**原文链接**: [https://bytesauna.com/post/my-favorite-math-problem](https://bytesauna.com/post/my-favorite-math-problem)

生成摘要时出错

---

## 82. Why top firms fire good workers

**原文标题**: Why top firms fire good workers

**原文链接**: [https://www.rochester.edu/newscenter/employee-turnover-why-top-firms-churn-good-workers-681832/](https://www.rochester.edu/newscenter/employee-turnover-why-top-firms-churn-good-workers-681832/)

生成摘要时出错

---

## 83. Open Source and Local Code Mode MCP in Deno Sandboxes

**原文标题**: Open Source and Local Code Mode MCP in Deno Sandboxes

**原文链接**: [https://portofcontext.com](https://portofcontext.com)

生成摘要时出错

---

## 84. Gitlogue – A cinematic Git commit replay tool for the terminal

**原文标题**: Gitlogue – A cinematic Git commit replay tool for the terminal

**原文链接**: [https://github.com/unhappychoice/gitlogue](https://github.com/unhappychoice/gitlogue)

生成摘要时出错

---

## 85. A Non-Obvious Answer to Why the AI Bubble Will Burst

**原文标题**: A Non-Obvious Answer to Why the AI Bubble Will Burst

**原文链接**: [https://brodzinski.com/2025/11/ai-bubble-non-obvious-answer.html](https://brodzinski.com/2025/11/ai-bubble-non-obvious-answer.html)

生成摘要时出错

---

## 86. Show HN: Search London StreetView panoramas by text

**原文标题**: Show HN: Search London StreetView panoramas by text

**原文链接**: [https://london.publicinsights.uk](https://london.publicinsights.uk)

生成摘要时出错

---

## 87. California DMV approves map increase in Waymo driverless operations

**原文标题**: California DMV approves map increase in Waymo driverless operations

**原文链接**: [https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/waymo-approved-areas-of-operation-for-driverless-testing-and-deployment/](https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/waymo-approved-areas-of-operation-for-driverless-testing-and-deployment/)

生成摘要时出错

---

## 88. It's hard to build an oscillator

**原文标题**: It's hard to build an oscillator

**原文链接**: [https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator](https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator)

生成摘要时出错

---

## 89. FEX-emu – Run x86 applications on ARM64 Linux devices

**原文标题**: FEX-emu – Run x86 applications on ARM64 Linux devices

**原文链接**: [https://fex-emu.com/](https://fex-emu.com/)

生成摘要时出错

---

## 90. Show HN: 32V TENS device from built from scratch under $100

**原文标题**: Show HN: 32V TENS device from built from scratch under $100

**原文链接**: [https://littlemountainman.github.io/2025/11/17/tens/](https://littlemountainman.github.io/2025/11/17/tens/)

生成摘要时出错

---

## 91. How/why to sweep async tasks under a Postgres table

**原文标题**: How/why to sweep async tasks under a Postgres table

**原文链接**: [https://taylor.town/pg-task](https://taylor.town/pg-task)

生成摘要时出错

---

## 92. CUDA Ontology

**原文标题**: CUDA Ontology

**原文链接**: [https://jamesakl.com/posts/cuda-ontology/](https://jamesakl.com/posts/cuda-ontology/)

生成摘要时出错

---

## 93. CBP is monitoring US drivers and detaining those with suspicious travel patterns

**原文标题**: CBP is monitoring US drivers and detaining those with suspicious travel patterns

**原文链接**: [https://apnews.com/article/immigration-border-patrol-surveillance-drivers-ice-trump-9f5d05469ce8c629d6fecf32d32098cd](https://apnews.com/article/immigration-border-patrol-surveillance-drivers-ice-trump-9f5d05469ce8c629d6fecf32d32098cd)

生成摘要时出错

---

## 94. We remain alive also in a dead internet

**原文标题**: We remain alive also in a dead internet

**原文链接**: [https://slavoj.substack.com/p/why-we-remain-alive-also-in-a-dead-954](https://slavoj.substack.com/p/why-we-remain-alive-also-in-a-dead-954)

生成摘要时出错

---

## 95. The Qtile Window Manager: A Python-Powered Tiling Experience

**原文标题**: The Qtile Window Manager: A Python-Powered Tiling Experience

**原文链接**: [https://tech.stonecharioteer.com/posts/2025/qtile-window-manager/](https://tech.stonecharioteer.com/posts/2025/qtile-window-manager/)

生成摘要时出错

---

## 96. Basalt Woven Textile

**原文标题**: Basalt Woven Textile

**原文链接**: [https://materialdistrict.com/material/basalt-woven-textile/](https://materialdistrict.com/material/basalt-woven-textile/)

生成摘要时出错

---

## 97. More tales about outages and numeric limits

**原文标题**: More tales about outages and numeric limits

**原文链接**: [https://rachelbythebay.com/w/2025/11/18/down/](https://rachelbythebay.com/w/2025/11/18/down/)

生成摘要时出错

---

## 98. The New AI Consciousness Paper

**原文标题**: The New AI Consciousness Paper

**原文链接**: [https://www.astralcodexten.com/p/the-new-ai-consciousness-paper](https://www.astralcodexten.com/p/the-new-ai-consciousness-paper)

生成摘要时出错

---

## 99. Launch HN: Mosaic (YC W25) – Agentic Video Editing

**原文标题**: Launch HN: Mosaic (YC W25) – Agentic Video Editing

**原文链接**: [https://mosaic.so](https://mosaic.so)

生成摘要时出错

---

## 100. Building a Minimal Viable Armv7 Emulator from Scratch

**原文标题**: Building a Minimal Viable Armv7 Emulator from Scratch

**原文链接**: [https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/](https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/)

生成摘要时出错

---

