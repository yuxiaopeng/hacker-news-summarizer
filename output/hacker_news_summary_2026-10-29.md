# Hacker News 热门文章摘要 (2026-10-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Claude Duet is the future of chatbot interaction

**原文标题**: Claude Duet is the future of chatbot interaction

**原文链接**: [https://fig.blue/posts/duet-is-the-future/](https://fig.blue/posts/duet-is-the-future/)

生成摘要时出错

---

## 12. IgE disruptor for food allergy with Claude-enabled antibody design [pdf]

**原文标题**: IgE disruptor for food allergy with Claude-enabled antibody design [pdf]

**原文链接**: [https://divergencelabs.com/publications/ige-preprint.pdf](https://divergencelabs.com/publications/ige-preprint.pdf)

生成摘要时出错

---

## 13. Edit an SQLite database in your browser

**原文标题**: Edit an SQLite database in your browser

**原文链接**: [https://editsqlite.com/](https://editsqlite.com/)

生成摘要时出错

---

## 14. Chained PHP2Shell exploit roots 25 servers, including US Government servers

**原文标题**: Chained PHP2Shell exploit roots 25 servers, including US Government servers

**原文链接**: [https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)

生成摘要时出错

---

## 15. Zombie stats: Where the numbers AI quotes come from

**原文标题**: Zombie stats: Where the numbers AI quotes come from

**原文链接**: [https://trakkr.ai/trakkr-research/zombie-stats](https://trakkr.ai/trakkr-research/zombie-stats)

生成摘要时出错

---

## 16. After 28 years walking across the globe, he's almost home

**原文标题**: After 28 years walking across the globe, he's almost home

**原文链接**: [https://www.nytimes.com/2026/10/29/world/europe/karl-bushby-walking-globe-uk.html](https://www.nytimes.com/2026/10/29/world/europe/karl-bushby-walking-globe-uk.html)

生成摘要时出错

---

## 17. One reviewer per layer: splitting code review by the way code is read

**原文标题**: One reviewer per layer: splitting code review by the way code is read

**原文链接**: [https://djordjepuzic.com/blog/posts/2026-10-27-one-reviewer-per-layer/](https://djordjepuzic.com/blog/posts/2026-10-27-one-reviewer-per-layer/)

生成摘要时出错

---

## 18. Sylphide OS: a general-purpose OS for microcontroller-based computers

**原文标题**: Sylphide OS: a general-purpose OS for microcontroller-based computers

**原文链接**: [https://projects.freehackers.org/sylphide-os/](https://projects.freehackers.org/sylphide-os/)

生成摘要时出错

---

## 19. ElementaryUI – Swift, in the Browser

**原文标题**: ElementaryUI – Swift, in the Browser

**原文链接**: [https://elementary.codes](https://elementary.codes)

生成摘要时出错

---

## 20. 16colo.rs – ANSI/ASCII art archive

**原文标题**: 16colo.rs – ANSI/ASCII art archive

**原文链接**: [https://16colo.rs/](https://16colo.rs/)

生成摘要时出错

---

## 21. Grace Blackwell needs a new scheduler: 27% more usable GPUs from the same racks

**原文标题**: Grace Blackwell needs a new scheduler: 27% more usable GPUs from the same racks

**原文链接**: [https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler](https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler)

生成摘要时出错

---

## 22. Show HN: Overtone – Transcribe, correct and cut captions for any screen shape

**原文标题**: Show HN: Overtone – Transcribe, correct and cut captions for any screen shape

**原文链接**: [https://github.com/lonthq/overtone-captions](https://github.com/lonthq/overtone-captions)

生成摘要时出错

---

## 23. If IPv4 were land

**原文标题**: If IPv4 were land

**原文链接**: [https://iptrust.co/blog/if-ipv4-were-land](https://iptrust.co/blog/if-ipv4-were-land)

生成摘要时出错

---

## 24. NetBSD adds a new text editor called atto

**原文标题**: NetBSD adds a new text editor called atto

**原文链接**: [https://mastodon.sdf.org/@netbsd/117518160563539748](https://mastodon.sdf.org/@netbsd/117518160563539748)

生成摘要时出错

---

## 25. Scattered thoughts on how doing math feels these days

**原文标题**: Scattered thoughts on how doing math feels these days

**原文链接**: [https://dynomight.net/math/](https://dynomight.net/math/)

生成摘要时出错

---

## 26. What we know so far about Spain train crash

**原文标题**: What we know so far about Spain train crash

**原文链接**: [https://www.bbc.com/news/articles/cm8xz7pkd0jjo](https://www.bbc.com/news/articles/cm8xz7pkd0jjo)

生成摘要时出错

---

## 27. Tomáš Mikolov awarded the Medal of Merit by the President of the Czech Republic

**原文标题**: Tomáš Mikolov awarded the Medal of Merit by the President of the Czech Republic

**原文链接**: [https://www.vut.cz/en/but/news-f19528/two-but-graduates-received-state-honors-from-the-president-of-the-republic-d378468](https://www.vut.cz/en/but/news-f19528/two-but-graduates-received-state-honors-from-the-president-of-the-republic-d378468)

生成摘要时出错

---

## 28. noalloc: Tooling and libraries to enforce zero heap allocations in Golang

**原文标题**: noalloc: Tooling and libraries to enforce zero heap allocations in Golang

**原文链接**: [https://github.com/theconsensuslabs/noalloc](https://github.com/theconsensuslabs/noalloc)

生成摘要时出错

---

## 29. Keplearn: Extract Equations from Data in Seconds

**原文标题**: Keplearn: Extract Equations from Data in Seconds

**原文链接**: [https://github.com/owls-on-wires/keplearn](https://github.com/owls-on-wires/keplearn)

生成摘要时出错

---

## 30. The tragedy of losing your Wikipedia page

**原文标题**: The tragedy of losing your Wikipedia page

**原文链接**: [https://www.wired.com/story/the-tragedy-of-losing-your-wikipedia-page/](https://www.wired.com/story/the-tragedy-of-losing-your-wikipedia-page/)

生成摘要时出错

---

## 31. I went to Mexico to test-drive the cars Americans can’t buy

**原文标题**: I went to Mexico to test-drive the cars Americans can’t buy

**原文链接**: [https://www.washingtonpost.com/climate-environment/2026/10/27/i-saw-future-driving-mexico-its-off-limits-americans/](https://www.washingtonpost.com/climate-environment/2026/10/27/i-saw-future-driving-mexico-its-off-limits-americans/)

生成摘要时出错

---

## 32. If-then-else had to be invented (2020)

**原文标题**: If-then-else had to be invented (2020)

**原文链接**: [https://github.com/e-n-f/if-then-else/blob/master/if-then-else.md](https://github.com/e-n-f/if-then-else/blob/master/if-then-else.md)

生成摘要时出错

---

## 33. Over $5B drained from Binance in apparent hack

**原文标题**: Over $5B drained from Binance in apparent hack

**原文链接**: [http://twitter.com/emmettgallic/status/2115916025774723210](http://twitter.com/emmettgallic/status/2115916025774723210)

生成摘要时出错

---

## 34. We won't "just hang out"

**原文标题**: We won't "just hang out"

**原文链接**: [https://borretti.me/article/we-wont-just-hang-out](https://borretti.me/article/we-wont-just-hang-out)

生成摘要时出错

---

## 35. Google Search is now less than half of Alphabet’s revenue

**原文标题**: Google Search is now less than half of Alphabet’s revenue

**原文链接**: [https://www.kadoa.com/companies/insights/google-search-below-half](https://www.kadoa.com/companies/insights/google-search-below-half)

生成摘要时出错

---

## 36. How Google determines the names for bodies of water in Google Earth (2008)

**原文标题**: How Google determines the names for bodies of water in Google Earth (2008)

**原文链接**: [https://publicpolicy.googleblog.com/2008/04/how-google-determines-names-for-bodies.html](https://publicpolicy.googleblog.com/2008/04/how-google-determines-names-for-bodies.html)

生成摘要时出错

---

## 37. The case of the 9 bit AES key

**原文标题**: The case of the 9 bit AES key

**原文链接**: [https://v12.sh/blog/the-case-of-the-9bit-aes-key](https://v12.sh/blog/the-case-of-the-9bit-aes-key)

生成摘要时出错

---

## 38. The first wired XR glasses powered by Android XR

**原文标题**: The first wired XR glasses powered by Android XR

**原文链接**: [https://blog.google/products-and-platforms/platforms/android/xreal-aura/](https://blog.google/products-and-platforms/platforms/android/xreal-aura/)

生成摘要时出错

---

## 39. Blanets and Weird Worlds

**原文标题**: Blanets and Weird Worlds

**原文链接**: [https://www.antipope.org/charlie/blog-static/2026/10/bizarre-blanets-and-other-weir.html](https://www.antipope.org/charlie/blog-static/2026/10/bizarre-blanets-and-other-weir.html)

生成摘要时出错

---

## 40. Zero click, silent, remote Android DoS

**原文标题**: Zero click, silent, remote Android DoS

**原文链接**: [https://smsofdeath.com/](https://smsofdeath.com/)

生成摘要时出错

---

## 41. Utah charges Kalshi and its CEO with illegally promoting online gambling

**原文标题**: Utah charges Kalshi and its CEO with illegally promoting online gambling

**原文链接**: [https://www.theverge.com/policy/1022400/utah-kalshi-criminal-charges](https://www.theverge.com/policy/1022400/utah-kalshi-criminal-charges)

生成摘要时出错

---

## 42. Java's new AOT cache feature is in a rough state

**原文标题**: Java's new AOT cache feature is in a rough state

**原文链接**: [https://xpipe.io/blog/java-aot-cache](https://xpipe.io/blog/java-aot-cache)

生成摘要时出错

---

## 43. Patrick Stewart Has Died

**原文标题**: Patrick Stewart Has Died

**原文链接**: [https://www.nytimes.com/2026/10/29/arts/television/patrick-stewart-dead.html](https://www.nytimes.com/2026/10/29/arts/television/patrick-stewart-dead.html)

生成摘要时出错

---

## 44. Getting debug access on a Brother printer over Telnet

**原文标题**: Getting debug access on a Brother printer over Telnet

**原文链接**: [https://inventor7777.github.io/blog/2026/10/22/debug-access-on-brother/](https://inventor7777.github.io/blog/2026/10/22/debug-access-on-brother/)

生成摘要时出错

---

## 45. Show HN: Typebook.lol read books by typing the letters only

**原文标题**: Show HN: Typebook.lol read books by typing the letters only

**原文链接**: [https://typebook.lol/](https://typebook.lol/)

生成摘要时出错

---

## 46. Archive Of Our Own down for maintenance for 2 to 4 weeks

**原文标题**: Archive Of Our Own down for maintenance for 2 to 4 weeks

**原文链接**: [https://www.otwstatus.org/incidents/g12jnxck9g6h](https://www.otwstatus.org/incidents/g12jnxck9g6h)

生成摘要时出错

---

## 47. Everything Rhymes with Porcelain

**原文标题**: Everything Rhymes with Porcelain

**原文链接**: [https://worksinprogress.co/issue/everything-rhymes-with-porcelain/](https://worksinprogress.co/issue/everything-rhymes-with-porcelain/)

生成摘要时出错

---

## 48. Toxic experts (2017)

**原文标题**: Toxic experts (2017)

**原文链接**: [https://nedbatchelder.com/blog/201711/toxic_experts](https://nedbatchelder.com/blog/201711/toxic_experts)

生成摘要时出错

---

## 49. Nango (YC W23) Is Hiring Across Eng, FDE, Marketing, DevRel

**原文标题**: Nango (YC W23) Is Hiring Across Eng, FDE, Marketing, DevRel

**原文链接**: [https://nango.dev/careers](https://nango.dev/careers)

生成摘要时出错

---

## 50. AI Contributions to GHC

**原文标题**: AI Contributions to GHC

**原文链接**: [https://serokell.io/blog/ai-contributions-to-ghc](https://serokell.io/blog/ai-contributions-to-ghc)

生成摘要时出错

---

## 51. Polymarket Halted International Trading After Hackers Drained Accounts

**原文标题**: Polymarket Halted International Trading After Hackers Drained Accounts

**原文链接**: [https://www.wired.com/story/polymarket-flagship-platform-hack-traders-lose-money/](https://www.wired.com/story/polymarket-flagship-platform-hack-traders-lose-money/)

生成摘要时出错

---

## 52. From Spreadsheets to DuckLake: A Data Engineer's Road to DuckDB

**原文标题**: From Spreadsheets to DuckLake: A Data Engineer's Road to DuckDB

**原文链接**: [https://duckdb.org/2026/10/29/from-spreadsheets-to-ducklake](https://duckdb.org/2026/10/29/from-spreadsheets-to-ducklake)

生成摘要时出错

---

## 53. Forging a Microsoft Edge Full Chain with Logic Bugs Only

**原文标题**: Forging a Microsoft Edge Full Chain with Logic Bugs Only

**原文链接**: [https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/](https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/)

生成摘要时出错

---

## 54. The US added a record 20.2 GWh of battery storage in just 3 months

**原文标题**: The US added a record 20.2 GWh of battery storage in just 3 months

**原文链接**: [https://electrek.co/2026/08/31/the-us-added-a-record-20-2-gwh-of-battery-storage-in-just-3-months/](https://electrek.co/2026/08/31/the-us-added-a-record-20-2-gwh-of-battery-storage-in-just-3-months/)

生成摘要时出错

---

## 55. StackOverflow now gets fewer than 1000 questions a month

**原文标题**: StackOverflow now gets fewer than 1000 questions a month

**原文链接**: [https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1](https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1)

生成摘要时出错

---

## 56. Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5

**原文标题**: Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5

**原文链接**: [https://divagr.com/blog/qwenputer](https://divagr.com/blog/qwenputer)

生成摘要时出错

---

## 57. Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5

**原文标题**: Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5

**原文链接**: [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

生成摘要时出错

---

## 58. Hackers expose the identities of more than 40k DHS employees

**原文标题**: Hackers expose the identities of more than 40k DHS employees

**原文链接**: [https://text.npr.org/nx-s1-6021497](https://text.npr.org/nx-s1-6021497)

生成摘要时出错

---

## 59. MiniLake Is a Local Databricks API Emulator with SQL, Delta Lake and Spark

**原文标题**: MiniLake Is a Local Databricks API Emulator with SQL, Delta Lake and Spark

**原文链接**: [https://dmux.github.io/minilake/](https://dmux.github.io/minilake/)

生成摘要时出错

---

## 60. Why is this fingerprinting script creating bioweapons?

**原文标题**: Why is this fingerprinting script creating bioweapons?

**原文链接**: [https://nullpt.rs/fingerprinting-bioweapons](https://nullpt.rs/fingerprinting-bioweapons)

生成摘要时出错

---

## 61. Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文标题**: Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文链接**: [https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/)

生成摘要时出错

---

## 62. Show HN: phpClaw – AI agent runtime for PHP with tools, memory and guards

**原文标题**: Show HN: phpClaw – AI agent runtime for PHP with tools, memory and guards

**原文链接**: [https://github.com/phpclaw-php/phpclaw-monorepo](https://github.com/phpclaw-php/phpclaw-monorepo)

生成摘要时出错

---

## 63. ‘You Are Done’: The letter sent to King by the F.B.I (2014)

**原文标题**: ‘You Are Done’: The letter sent to King by the F.B.I (2014)

**原文链接**: [https://www.nytimes.com/2014/11/16/magazine/what-an-uncensored-letter-to-mlk-reveals.html](https://www.nytimes.com/2014/11/16/magazine/what-an-uncensored-letter-to-mlk-reveals.html)

生成摘要时出错

---

## 64. A new faster algorithm to compute 64-bit signed floor division

**原文标题**: A new faster algorithm to compute 64-bit signed floor division

**原文链接**: [https://www.benjoffe.com/fast-floordiv](https://www.benjoffe.com/fast-floordiv)

生成摘要时出错

---

## 65. Southern Africa's first known stenciled rock art found hiding in plain sight

**原文标题**: Southern Africa's first known stenciled rock art found hiding in plain sight

**原文链接**: [https://phys.org/news/2026-10-southern-africa-stenciled-art-plain.html](https://phys.org/news/2026-10-southern-africa-stenciled-art-plain.html)

生成摘要时出错

---

## 66. Apple bullied flash memory suppliers, and why AI datacenters changed the game

**原文标题**: Apple bullied flash memory suppliers, and why AI datacenters changed the game

**原文链接**: [https://www.msn.com/en-us/news/other/the-beleaguered-chip-sellers-getting-their-revenge-on-apple/ar-AA2ghTPi](https://www.msn.com/en-us/news/other/the-beleaguered-chip-sellers-getting-their-revenge-on-apple/ar-AA2ghTPi)

生成摘要时出错

---

## 67. Newly discovered Kerberos delegation abuse path

**原文标题**: Newly discovered Kerberos delegation abuse path

**原文链接**: [https://hunio.org/security/abusing-constrained-delegation-without-protocol-transition-against-spn-less-accounts/](https://hunio.org/security/abusing-constrained-delegation-without-protocol-transition-against-spn-less-accounts/)

生成摘要时出错

---

## 68. GitLab Security Incident: Attempted Exploitation of CVE-2026-97229

**原文标题**: GitLab Security Incident: Attempted Exploitation of CVE-2026-97229

**原文链接**: [https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html)

生成摘要时出错

---

## 69. Alphabet heads for a $500B drop in market value, biggest in its history

**原文标题**: Alphabet heads for a $500B drop in market value, biggest in its history

**原文链接**: [https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html](https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html)

生成摘要时出错

---

## 70. Thursday: A SerenityOS for Myself

**原文标题**: Thursday: A SerenityOS for Myself

**原文链接**: [https://shantaram.xyz/posts/2026/10/a-serenityos-for-myself](https://shantaram.xyz/posts/2026/10/a-serenityos-for-myself)

生成摘要时出错

---

## 71. The AI bubble is about to pop [video]

**原文标题**: The AI bubble is about to pop [video]

**原文链接**: [https://www.youtube.com/watch?v=MgngwkPAuqQ](https://www.youtube.com/watch?v=MgngwkPAuqQ)

生成摘要时出错

---

## 72. Polymarket halts trading after compromise, impacted users will be 'made whole'

**原文标题**: Polymarket halts trading after compromise, impacted users will be 'made whole'

**原文链接**: [https://www.nbcnews.com/business/consumer/polymarket-trading-halt-hack-wallets-rcna606405](https://www.nbcnews.com/business/consumer/polymarket-trading-halt-hack-wallets-rcna606405)

生成摘要时出错

---

## 73. AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura

**原文标题**: AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura

**原文链接**: [https://thedataexchange.media/leo-de-moura-lean-aws/](https://thedataexchange.media/leo-de-moura-lean-aws/)

生成摘要时出错

---

## 74. Why birds can fly over Mount Everest (2020)

**原文标题**: Why birds can fly over Mount Everest (2020)

**原文链接**: [https://lede-v2.nautil.us/why-birds-can-fly-over-mount-everest-237864](https://lede-v2.nautil.us/why-birds-can-fly-over-mount-everest-237864)

生成摘要时出错

---

## 75. Polymarket Pauses Trading After Some Users Report Funds Drained

**原文标题**: Polymarket Pauses Trading After Some Users Report Funds Drained

**原文链接**: [https://www.wsj.com/business/polymarket-pauses-trading-after-some-users-report-funds-drained-b014527d](https://www.wsj.com/business/polymarket-pauses-trading-after-some-users-report-funds-drained-b014527d)

生成摘要时出错

---

## 76. Gemini 4 Carbon

**原文标题**: Gemini 4 Carbon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

生成摘要时出错

---

## 77. Formlabs Studio 1 $699 Resin Printer

**原文标题**: Formlabs Studio 1 $699 Resin Printer

**原文链接**: [https://formlabs.com/products/form-studio-1-basic-founders-edition/](https://formlabs.com/products/form-studio-1-basic-founders-edition/)

生成摘要时出错

---

## 78. Show HN: An open-source app for IELTS preparation

**原文标题**: Show HN: An open-source app for IELTS preparation

**原文链接**: [https://github.com/Luxshan2000/ielts-prep](https://github.com/Luxshan2000/ielts-prep)

生成摘要时出错

---

## 79. Tesla caught altering specs following rear suspension collapse reports

**原文标题**: Tesla caught altering specs following rear suspension collapse reports

**原文链接**: [https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/](https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/)

生成摘要时出错

---

## 80. One of Binance Hot Wallets drained to new account, funded by Tornado Cash

**原文标题**: One of Binance Hot Wallets drained to new account, funded by Tornado Cash

**原文链接**: [https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3](https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3)

生成摘要时出错

---

## 81. Dayjob: Tax – evaluating AI agents on 50 professional tax assignments

**原文标题**: Dayjob: Tax – evaluating AI agents on 50 professional tax assignments

**原文链接**: [https://surgehq.ai/blog/dayjob-tax](https://surgehq.ai/blog/dayjob-tax)

生成摘要时出错

---

## 82. Claude Code regularly sends each background agent’s transcript to its model

**原文标题**: Claude Code regularly sends each background agent’s transcript to its model

**原文链接**: [https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)

生成摘要时出错

---

## 83. Proton CEO Andy Yen: "This will be the last year that we hire engineers."

**原文标题**: Proton CEO Andy Yen: "This will be the last year that we hire engineers."

**原文链接**: [https://twitter.com/LayoffAI/status/2115871654366642624](https://twitter.com/LayoffAI/status/2115871654366642624)

生成摘要时出错

---

## 84. A Defense Contractor Gave Their AI Agent Access to a Secure Pentagon System

**原文标题**: A Defense Contractor Gave Their AI Agent Access to a Secure Pentagon System

**原文链接**: [https://www.wired.com/story/a-defense-contractor-gave-their-personal-ai-agent-access-to-a-secure-pentagon-system/](https://www.wired.com/story/a-defense-contractor-gave-their-personal-ai-agent-access-to-a-secure-pentagon-system/)

生成摘要时出错

---

## 85. Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js

**原文标题**: Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js

**原文链接**: [https://sparkjs.dev/radix/](https://sparkjs.dev/radix/)

生成摘要时出错

---

## 86. Requests, Please

**原文标题**: Requests, Please

**原文链接**: [https://morronel.github.io/requests_please/](https://morronel.github.io/requests_please/)

生成摘要时出错

---

## 87. Why are good developers so wary of agentic development?

**原文标题**: Why are good developers so wary of agentic development?

**原文链接**: [https://martinfowler.com/rachels-ramblings/good-devs-wary.html](https://martinfowler.com/rachels-ramblings/good-devs-wary.html)

生成摘要时出错

---

## 88. Pi Durable on Cloudflare – Earendil

**原文标题**: Pi Durable on Cloudflare – Earendil

**原文链接**: [https://earendil.com/posts/pi-durable-on-cloudflare/](https://earendil.com/posts/pi-durable-on-cloudflare/)

生成摘要时出错

---

## 89. ACLs Don't (2009) [pdf]

**原文标题**: ACLs Don't (2009) [pdf]

**原文链接**: [https://shiftleft.com/mirrors/www.hpl.hp.com/techreports/2009/HPL-2009-20.pdf](https://shiftleft.com/mirrors/www.hpl.hp.com/techreports/2009/HPL-2009-20.pdf)

生成摘要时出错

---

## 90. Old 'Popcorn Time' App Left Macs at Risk

**原文标题**: Old 'Popcorn Time' App Left Macs at Risk

**原文链接**: [https://www.macrumors.com/2026/10/29/old-popcorn-time-app-macs-at-risk/](https://www.macrumors.com/2026/10/29/old-popcorn-time-app-macs-at-risk/)

生成摘要时出错

---

## 91. AlpineBSD

**原文标题**: AlpineBSD

**原文链接**: [https://wiki.alpinebsd.org](https://wiki.alpinebsd.org)

生成摘要时出错

---

## 92. Until – You approve the plan, a separate agent checks the code against it

**原文标题**: Until – You approve the plan, a separate agent checks the code against it

**原文链接**: [https://until.dev](https://until.dev)

生成摘要时出错

---

## 93. I Used AI to Fake a Scientific Paper. Here's What Happened

**原文标题**: I Used AI to Fake a Scientific Paper. Here's What Happened

**原文链接**: [https://spectrum.ieee.org/ai-generated-scientific-papers](https://spectrum.ieee.org/ai-generated-scientific-papers)

生成摘要时出错

---

## 94. Two unpatched zero-day vulnerabilities in NTE allow for full account takeover

**原文标题**: Two unpatched zero-day vulnerabilities in NTE allow for full account takeover

**原文链接**: [https://hunio.org/security/nte-account-takeover/](https://hunio.org/security/nte-account-takeover/)

生成摘要时出错

---

## 95. Show HN: Witnessory – a signed record of the web's move to post-quantum crypto

**原文标题**: Show HN: Witnessory – a signed record of the web's move to post-quantum crypto

**原文链接**: [https://witnessory.org](https://witnessory.org)

生成摘要时出错

---

## 96. MacBook Pro with PROLED XDR Display and Touch

**原文标题**: MacBook Pro with PROLED XDR Display and Touch

**原文链接**: [https://www.apple.com/macbook-pro/proled-xdr-display/](https://www.apple.com/macbook-pro/proled-xdr-display/)

生成摘要时出错

---

## 97. AI Made Me Homeless

**原文标题**: AI Made Me Homeless

**原文链接**: [https://medium.com/effortless-programming/ai-made-me-homeless-a7266d716e59](https://medium.com/effortless-programming/ai-made-me-homeless-a7266d716e59)

生成摘要时出错

---

## 98. Polymarket Pauses Trading After Some Users Report Funds Drained

**原文标题**: Polymarket Pauses Trading After Some Users Report Funds Drained

**原文链接**: [https://www.wsj.com/business/polymarket-pauses-trading-after-some-users-report-funds-drained-b014527d](https://www.wsj.com/business/polymarket-pauses-trading-after-some-users-report-funds-drained-b014527d)

生成摘要时出错

---

## 99. Apple's git still trusts the compromised eMudhra certificates

**原文标题**: Apple's git still trusts the compromised eMudhra certificates

**原文链接**: [https://emudhra.we-have-a-problem.com/apple.html](https://emudhra.we-have-a-problem.com/apple.html)

生成摘要时出错

---

## 100. A Health Update

**原文标题**: A Health Update

**原文链接**: [https://furbo.org/2026/10/28/a-health-update/](https://furbo.org/2026/10/28/a-health-update/)

生成摘要时出错

---

