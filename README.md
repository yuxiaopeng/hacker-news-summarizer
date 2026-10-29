# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-29.md)

*最后自动更新时间: 2026-10-29 22:04:23*
## 1. 我们现已发布 Mistral Large 4 的权重。

**原文标题**: We're releasing the weights of Mistral Large 4

**原文链接**: [https://mistral.ai/news/mistral-large-4-oss/](https://mistral.ai/news/mistral-large-4-oss/)

Mistral AI 已发布 Mistral Large 4（代号“Le Chonk”）的开放权重，这是一款拥有 1 万亿参数的原生多模态旗舰模型。该模型被定位为“主权 AI”的领导者，在欧洲基础设施上训练，旨在为各类机构提供高性能、可定制且可自托管的方案，作为闭源 AI 的替代选择。

该模型在两个主要领域表现卓越：
* **编程：** Mistral Large 4 在 FrontierCode 2.0 和 Terminal-Bench 4.0 等开放权重基准测试中处于领先地位。其 Token 效率显著高于 GLM-5.3 和 DeepSeek 等竞争对手，以更低的推理成本提供前沿性能。为了协助开发者，它引入了三种推理模式（低、中、高）来平衡精度与成本。
* **网络安全：** 该模型专为“防御者”设计，凭借复现和修复漏洞的能力，在 Artificial Analysis 网络安全指数中获得高分。它对恶意请求的拒绝率达到 96.6%——在开放模型中排名最高——同时避免了对合法安全研究的“误拒”。此外，Mistral 还向经过审查的企业合作伙伴提供用于高级红队测试的专用变体。

除上述专长外，该模型在通用企业任务中也表现出重大改进，包括金融工作流（Finch 基准测试）、网页浏览（BrowseComp）和智能体安全（B3 基准测试）。

通过发布开放权重，Mistral 允许企业和政府审计模型架构并确保完整的数据驻留。在英伟达（NVIDIA）、Cloudflare 和 CrowdStrike 等全球领先企业的支持下，Mistral Large 4 为高度受监管和技术性行业的开放权重模型开辟了新境界。

---

## 2. 疑似中国间谍与英伟达CEO黄仁勋有“密切关系”

**原文标题**: Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang

**原文链接**: [https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/](https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/)

据《纽约时报》报道，美国情报官员对英伟达（Nvidia）首席执行官黄仁勋与涉嫌为中国间谍的黄乐（Alice Huang）之间的“密切关系”表示担忧。黄乐是新加坡公司 Megaspeed 的高管，该公司是英伟达的客户，涉嫌帮助包括阿里巴巴在内的中国企业规避美国出口限制以获取先进 AI 芯片。

虽然电子监控确认黄仁勋曾与其接触，但尚无直接证据表明他知晓其所谓的情报搜集活动。两人曾于 2024 年和 2025 年在台北的技术活动中被拍到合影。然而，特朗普政府的部分高级官员对黄仁勋是否真的对此全然不知表示怀疑。

该报告强调了复杂的政治背景：
*   **游说与捐赠：** 据报道，黄仁勋曾游说特朗普总统放宽芯片出口限制。在这些努力之后，英伟达向一个与特朗普相关的基金捐赠了至少 2000 万美元，并承诺在美国制造业投资 5000 亿美元。
*   **政府不作为：** 尽管特朗普在一年前就听取了相关情报结果的汇报，但据称他为了避免干扰贸易关系和英伟达利润丰厚的销售，选择不采取行动。

英伟达对相关指控予以反驳，称对于一位每年会见数千名客户的首席执行官而言，此类互动“并非异常”。该公司坚称未分享任何敏感商业机密或国家安全信息，并表示有关 Megaspeed 的指控此前已被调查并证伪。同时，中国大使馆驳斥该报告为旨在打压中国技术发展的“无端抹黑”。

---

## 3. Patrick Stewart has died

**原文标题**: Patrick Stewart has died

**原文链接**: [https://www.nytimes.com/2026/10/29/arts/television/patrick-stewart-dead.html](https://www.nytimes.com/2026/10/29/arts/television/patrick-stewart-dead.html)

生成摘要时出错

---

## 4. 在树莓派 Pico 2 W 上运行游戏的微型世界模型

**原文标题**: A tiny world model running games on a Raspberry Pi Pico 2 W

**原文链接**: [https://github.com/SheepSeb/tinyworldformer](https://github.com/SheepSeb/tinyworldformer)

该项目展示了在 **树莓派 Pico 2 W (RP2350)** 上成功部署生成式“世界模型”和自主强化学习智能体的成果。系统在不依赖原始游戏引擎的情况下运行，而是通过两个神经网络来模拟并游玩《打砖块》（Breakout）、轻量版《毁灭战士》（Doom-lite）和《吃豆人》（Pac-Man）等游戏。

**核心组件与架构：**
*   **世界模型：** 一个**循环 Transformer（Looped Transformer）**，根据当前状态和动作预测下一帧及奖励。通过在多次传递（循环）中复用权重，使模型在保持高精度的同时，体积小巧到足以在微控制器上运行。
*   **执行者（Actor）：** 一个小型多层感知器（MLP），根据生成的“梦境”帧选择动作。
*   **片上学习：** 系统采用 **Stream AC(λ)** 算法，允许智能体从状态转换中实时学习，而无需占用大量内存的经验回放缓冲区。

**技术实现：**
*   **优化：** 为适配 Pico 的 520KB SRAM，模型对权重和激活值进行了 **int8 量化**，同时利用 RP2350 的浮点运算单元（FPU）处理 float32 嵌入和归一化。
*   **双核执行：** 项目采用 **no_std Rust** 编写。核心 1 负责神经网络推理和游戏模拟，核心 0 负责管理 USB 通信和显示驱动。
*   **性能：** 该世界模型在《飞扬的小鸟》（Flappy Bird）和《打砖块》等简单游戏中实现了接近 100% 的帧准确率。根据游戏复杂度，帧率在 6.6 到 15 FPS 之间。

通过将高效架构与底层硬件优化相结合，该项目证明了复杂的生成式 AI 和实时强化学习可以在廉价、低功耗的微控制器硬件上运行。

---

## 5. H.264 的魔法 (2016)

**原文标题**: H.264 Is Magic (2016)

**原文链接**: [https://sidbala.com/h-264-is-magic/](https://sidbala.com/h-264-is-magic/)

《H.264 是魔法》一文探讨了 H.264 编解码器如何实现现代数字视频所需的海量数据压缩。原始、未经压缩的视频体积巨大；例如，一个 1080p 60Hz 的视频流每秒产生约 370 MB 数据。H.264 通过采用几种复杂的“技巧”，在保持视觉质量的同时丢弃不必要的数据，从而解决了这一难题。

压缩过程主要包含四个阶段：

1.  **频域量化：** 通过将图像数据转换至频域，算法可以识别出高频细节（精细纹理）和渐变（低频）。由于人眼对精细细节较不敏感，H.264 通过量化丢弃这些高频成分，从而显著降低“信息熵”。
2.  **色度抽样：** 人类视觉对亮度（Luminance）的敏感度高于色彩（Chrominance）。H.264 以低于亮度的分辨率存储色彩信息，通常在对感知质量影响微乎其微的前提下，将所需带宽减半。
3.  **运动补偿（帧间压缩）：** H.264 并非将每一帧都存储为完整图像，而是使用 **I 帧**（完整图像）、**P 帧**（预测帧）和 **B 帧**（双向预测帧）。它跟踪像素“宏块”的“运动矢量”，仅记录这些色块随时间移动的轨迹，而非对整个场景进行重新编码。
4.  **熵编码：** 最后，编解码器应用无损熵编码器，以消除数据流中残余的所有数学冗余。

作者通过一段 5 秒的视频展示了这些技术的高效性，该视频的体积比同一内容的单张 PNG 截图还要小五倍。通过这些方法，H.264 可以将数据缩减 1500 倍以上，作者将这一壮举比作将一辆 3000 磅的汽车缩减至仅 6.5 盎司。

---

## 6. Show HN: 自动关闭 macOS “允许‘<应用>’查找本地网络上的设备？”提示框

**原文标题**: Show HN: Auto Dismiss Mac OS "Allow <app> to find devices on local networks?"

**原文链接**: [https://github.com/johncassil/dontallow](https://github.com/johncassil/dontallow)

**dontallow** 是一款轻量级的开源实用工具，旨在自动忽略 macOS 15 Sequoia 中频繁出现的“本地网络”权限提示。

### 问题背景
在 macOS Sequoia 中，应用程序必须请求访问本地网络的权限。然而，许多应用（尤其是 Chrome、Brave 和 Edge 等基于 Chromium 的浏览器）在每次启动时都会触发此提示，因为它们在更新过程中会使用随机的临时路径。这会导致 macOS 误将每次启动视为一个新应用，从而使“隐私”设置中充斥着重复条目，并频繁干扰用户。此外，目前尚无原生方法可以通过 MDM 或系统工具预先拒绝这些权限。

### 工作原理
`dontallow` 由单个无依赖的 Swift 文件编写，作为后台 launchd 代理运行，且空闲时 CPU 占用率为零。它利用 macOS **辅助功能 API (Accessibility API)** 来监测 `UserNotificationCenter` 进程。当本地网络提示出现时，该代理会识别该提示，并在极短的时间内通过编程方式点击“不允许”按钮。

### 核心特性
*   **智能忽略：** 它仅针对本地网络提示，且绝不会选择“允许”，确保不会误操作授予权限。
*   **自定义功能：** 如果用户需要手动允许某个应用，可以“暂停”代理（例如暂停 1 小时），或将特定应用添加到永久**白名单**中。
*   **透明化管理：** 它包含一个 `rules` 命令，用于解码并显示系统底层的本地网络权限存储，从而识别“孤立”条目。
*   **企业级支持：** 虽然辅助功能权限通常需要用户手动授予，但对于受管设备群组，可以通过 MDM（PPPC 配置文件）进行预授权。

### 使用要求
该工具可通过 Homebrew 或 `make` 安装，要求 macOS 15 及以上版本，且系统语言需设置为英文。由于该工具出于安全考虑依赖代码签名，用户在更新二进制文件后需要重新开关一次辅助功能权限。

---

## 7. 软件社区的重要性

**原文标题**: The importance of communities around software

**原文链接**: [https://lumi.codeberg.page/blog/software-community.html](https://lumi.codeberg.page/blog/software-community.html)

In "The importance of communities around software," Lumi argues that the ethical value of a software project is determined more by its community than by its legal license. While Lumi previously focused on strong copyleft licenses to protect software freedom, they now view licenses as insufficient tools that still operate within a flawed, corporate-centric copyright system.

The article contends that technical "freedom" does not guarantee a project is ethical. A project can be licensed as free software yet still be corporate-controlled through contributor license agreements (CLAs), lack inclusivity, or endorse extractive technologies like generative AI. To truly evaluate a project, Lumi suggests looking at:
*   **Inclusivity:** The presence of a Code of Conduct.
*   **Autonomy:** Independence from corporate ownership and centralized platforms (e.g., Discord or GitHub).
*   **Ethics:** Policies regarding generative models and the personal values of lead developers.

Lumi emphasizes that the community dictates a project’s direction. Users are encouraged to move beyond passive use and actively participate in the communities they care about. Contribution is not limited to coding; it includes documentation, triage, and community management. By speaking up, members can push projects toward ethical practices. 

Finally, the author advocates for collaborative models like software cooperatives—citing examples such as The Starlight Network and Polyphony—where people build software together based on shared values and mutual support rather than just license compliance.

---

## 8. DoorDash将收购Instacart

**原文标题**: DoorDash to acquire Instacart

**原文链接**: [https://about.doordash.com/en-us/news/doordash-to-acquire-instacart](https://about.doordash.com/en-us/news/doordash-to-acquire-instacart)

**DoorDash 将以 170 亿美元收购 Instacart**

DoorDash (NASDAQ: DASH) 宣布已达成最终协议，将以约 170 亿美元的价格收购 Instacart (NASDAQ: CART)，折合每股 65.00 美元。该价格较 Instacart 2026 年 10 月 22 日的收盘价溢价 26%。此次交易将由至少 75% 的现金和最高 25% 的 DoorDash 股票组成。

此次合并旨在将 DoorDash 的物流网络和全球影响力与 Instacart 专业的生鲜杂货履约技术及零售商关系相结合。其战略目标是通过提供先进的 AI、广告工具和更广泛的配送能力，赋能本地杂货商与大型在线零售商竞争。

**交易要点包括：**
*   **消费者利益：** 用户将可以访问额外 50,000 多家门店。此外，两家公司计划将 DashPass 和 Instacart+ 整合为单一会员体系，每年有望为消费者节省 1 亿美元。
*   **对劳动者的影响：** 配送员 (Dashers) 和采购员 (Shoppers) 将获得更多增收机会，并能灵活在餐饮和杂货两个领域工作。
*   **运营连续性：** DoorDash 打算保留 Instacart 的品牌、应用程序和企业技术。同时，他们承诺执行“开放平台”政策，确保参与商户无需签署生鲜杂货排他性协议。
*   **时间表：** 在获得股东批准以及美国、加拿大和以色列的监管许可后，该收购预计将于 2027 年底至 2028 年上半年之间完成。

首席执行官 Tony Xu 和 Chris Rogers 强调，此次合作将加速杂货行业的创新，并帮助“主街”实体商家在日益数字化的经济中蓬勃发展。DoorDash 将通过现有现金和债务融资为现金部分提供资金。

---

## 9. LLM Voice

**原文标题**: LLM Voice

**原文链接**: [https://martinfowler.com/bliki/LLM-Voice.html](https://martinfowler.com/bliki/LLM-Voice.html)

生成摘要时出错

---

## 10. Show HN: A proof-of-concept formalization of the IRS federal tax forms

**原文标题**: Show HN: A proof-of-concept formalization of the IRS federal tax forms

**原文链接**: [https://github.com/emmilco/us-tax-model](https://github.com/emmilco/us-tax-model)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 2 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 3 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 4 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 5 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 6 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 7 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 8 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 9 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 10 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 11 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 12 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 13 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 14 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 15 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 16 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 17 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 18 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 19 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 20 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 21 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 22 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 23 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 24 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 25 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 26 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 27 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 28 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 29 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 30 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 31 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 32 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 33 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 34 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 35 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 36 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 37 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 38 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 39 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 40 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 41 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 42 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 43 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 44 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 45 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 46 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 47 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 48 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 49 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 50 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 51 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 52 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 53 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 54 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 55 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 56 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 57 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 58 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 59 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 60 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 61 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 62 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 63 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 64 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 65 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 66 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 67 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 68 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 69 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 70 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 71 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 72 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 73 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 74 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 75 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 76 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 77 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 78 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 79 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 80 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 81 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 82 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 83 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 84 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 85 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 86 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 87 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 88 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 89 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 90 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 91 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 92 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 93 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 94 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 95 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 96 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 97 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 98 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 99 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 100 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 101 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 102 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 103 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 104 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 105 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 106 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 107 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 108 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 109 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 110 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 111 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 112 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 113 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 114 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 115 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 116 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 117 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 118 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 119 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 120 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 121 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 122 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 123 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 124 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 125 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 126 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 127 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 128 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 129 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 130 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 131 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 132 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 133 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 134 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 135 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 136 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 137 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 138 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 139 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 140 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 141 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 142 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 143 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 144 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 145 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 146 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 147 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 148 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 149 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 150 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 151 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 152 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 153 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 154 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 155 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 156 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 157 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 158 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 159 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 160 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 161 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 162 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 163 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 164 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 165 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 166 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 167 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 168 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 169 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 170 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 171 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 172 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 173 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 174 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 175 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 176 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 177 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 178 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 179 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 180 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 181 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 182 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 183 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 184 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 185 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 186 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 187 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 188 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 189 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 190 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 191 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 192 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 193 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 194 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 195 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 196 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 197 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 198 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 199 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 200 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 201 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 202 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 203 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 204 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 205 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 206 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 207 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 208 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 209 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 210 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 211 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 212 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 213 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 214 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 215 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 216 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 217 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 218 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 219 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 220 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 221 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 222 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 223 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 224 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 225 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 226 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 227 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 228 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 229 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 230 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 231 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 232 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 233 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 234 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 235 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 236 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 237 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 238 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 239 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 240 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 241 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 242 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 243 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 244 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 245 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 246 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 247 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 248 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 249 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 250 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 251 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 252 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 253 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 254 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 255 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 256 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 257 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 258 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 259 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 260 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 261 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 262 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 263 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 264 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 265 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 266 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 267 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 268 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 269 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 270 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 271 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 272 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 273 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 274 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 275 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 276 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 277 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 278 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 279 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 280 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 281 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 282 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 283 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 284 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 285 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 286 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 287 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 288 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 289 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 290 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 291 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 292 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 293 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 294 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 295 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 296 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 297 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 298 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 299 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 300 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 301 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 302 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 303 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 304 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 305 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 306 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 307 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 308 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 309 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 310 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 311 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 312 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 313 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 314 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 315 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 316 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 317 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 318 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 319 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 320 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 321 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 322 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 323 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 324 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 325 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 326 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 327 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 328 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 329 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 330 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 331 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 332 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 333 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 334 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 335 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 336 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 337 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 338 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 339 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 340 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 341 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 342 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 343 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 344 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 345 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 346 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 347 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 348 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 349 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 350 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 351 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 352 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 353 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 354 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 355 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 356 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 357 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 358 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 359 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 360 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 361 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 362 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 363 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 364 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 365 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 366 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 367 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 368 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 369 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 370 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 371 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 372 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 373 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 374 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 375 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 376 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 377 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 378 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 379 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 380 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 381 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 382 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 383 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 384 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 385 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 386 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 387 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 388 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 389 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 390 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 391 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 392 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 393 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 394 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 395 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 396 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 397 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 398 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 399 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 400 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 401 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 402 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 403 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 404 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 405 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 406 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 407 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 408 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 409 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 410 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 411 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 412 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 413 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 414 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 415 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 416 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 417 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 418 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 419 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 420 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 421 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 422 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 423 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 424 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 425 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 426 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 427 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 428 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 429 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 430 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 431 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 432 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 433 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 434 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 435 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 436 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 437 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 438 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 439 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 440 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 441 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 442 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 443 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 444 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 445 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 446 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 447 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 448 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 449 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 450 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 451 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 452 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 453 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 454 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 455 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 456 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 457 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 458 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 459 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 460 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 461 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 462 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 463 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 464 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 465 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 466 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 467 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 468 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 469 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 470 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 471 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 472 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 473 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 474 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 475 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 476 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 477 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 478 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 479 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 480 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 481 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 482 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 483 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 484 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 485 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 486 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 487 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 488 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 489 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 490 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 491 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 492 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 493 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 494 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 495 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 496 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 497 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 498 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 499 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 500 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 501 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 502 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 503 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 504 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 505 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 506 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 507 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 508 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 509 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 510 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 511 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 512 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 513 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 514 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 515 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 516 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 517 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 518 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 519 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 520 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 521 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 522 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 523 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 524 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 525 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 526 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 527 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 528 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 529 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 530 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 531 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 532 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 533 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 534 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 535 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 536 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 537 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 538 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 539 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 540 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 541 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 542 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 543 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 544 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 545 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 546 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 547 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 548 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 549 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 550 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 551 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 552 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 553 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 554 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 555 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 556 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 557 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 558 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 559 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 560 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 561 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 562 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 563 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 564 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 565 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 566 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 567 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 568 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 569 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 570 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 571 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 572 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 573 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 574 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 575 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 576 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 577 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 578 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 579 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 580 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 581 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 582 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 583 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 584 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 585 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 586 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
