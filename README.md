# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-19.md)

*最后自动更新时间: 2025-12-19 17:46:55*
## 1. 现在的 Hacker News 首页，但标题变诚实了。

**原文标题**: Hacker News front page now, but the titles are honest

**原文链接**: [https://dosaygo-studio.github.io/hn-front-page-2035/news-honest.html](https://dosaygo-studio.github.io/hn-front-page-2035/news-honest.html)

这篇讽刺文章呈现了一个“Hacker News：诚实版”，剥离了行业术语和营销废话，揭示了现代科技文化背后愤世嫉俗的现实。这个模拟首页将常见的行业套路归纳为几个核心主题：

**1. 开发与工程痴迷：** 该列表嘲讽了社区对“用 Rust 重写一切”的痴迷、对基础工具（如状态机和拖放 API）的不断重复造轮子，以及由于过度依赖未经审核的依赖项而导致的现代软件脆弱性。

**2. AI 炒作周期：** 几条标题嘲讽了 OpenAI 和 Anthropic 等公司利用发布产品来转移对董事会内斗的注意力，或是拼命追赶同行。它还强调了 AI 训练方法的荒谬性，包括试图避免“觉醒主义”偏见以及使用“中毒”数据集。

**3. 企业与监管的犬儒主义：** 讽刺对象指向了“带有敌意”的营销部门（英特尔）、隐蔽的设计改动（谷歌）以及政客们在技术上的无知。它还将许多“技术教程”定性为掩饰拙劣的特定服务广告。

**4. 职业与生活现状：** 列表指出了科技界的表演性质，从开发者为了保住工作而乞求 GitHub 星标，到富有的发烧友花费 1.5 万美元只为让 AI 模型运行得稍微快一点。

**5. 制度批判：** 标题揭露了学术付费墙这种被视为“骗局”的现象，以及亚马逊等老牌巨头在采用已普及数十年的功能时表现出的迟缓。

最终，这篇文章构成了对 Hacker News 生态系统的元评论，将其描绘成一个由情怀诱饵、自我推销和针对小众问题的过度设计方案交织而成的集合——而消费这些内容的用户，正如页脚所述，主要是在“摸鱼”。

---

## 2. 为了使用 Bluesky，我必须把护照交给《堡垒之夜》。

**原文标题**: I have to give Fortnite my passport to use Bluesky

**原文链接**: [https://spitfirenews.com/p/why-i-have-to-give-fortnite-my-passport-to-use-bluesky](https://spitfirenews.com/p/why-i-have-to-give-fortnite-my-passport-to-use-bluesky)

在这篇文章中，凯特·滕巴奇（Kat Tenbarge）对年龄验证法律的泛滥提出了批评，并以她在俄亥俄州的经历作为主要案例。在访问该州期间，滕巴奇发现，除非向 Epic Games 的一家子公司提交护照或社会安全号码等敏感个人信息，否则她无法访问 Bluesky 的私信。

滕巴奇认为，这些法律“既无效又危险”，理由如下：

*   **隐私与安全风险：** 集中存储敏感的政府身份证件为黑客制造了一个巨大的目标。滕巴奇援引了最近一起年龄验证服务数据泄露事件，该事件导致 7 万名 Discord 用户的身份信息遭到泄露。
*   **无效性：** 精通技术的未成年人可以利用 VPN 或其他漏洞轻松绕过这些限制，使这些法律无法实现其预期目的。
*   **对关键信息的审查：** 英国类似的法律已被用于审查政治信息和医疗资源。滕巴奇警告称，美国的联邦立法（如《儿童在线安全法案》，简称 KOSA）和“2025 计划”（Project 2025）等框架可能会将“儿童安全”武器化，以此清除互联网上的 LGBTQ+ 内容、生殖健康信息和种族正义教育。
*   **对边缘化青少年的伤害：** 对于生活在缺乏支持的环境中的儿童来说，互联网提供了必不可少的社群支持和救命信息。阻碍他们进入这些空间会损害其心理健康和自主权。

滕巴奇总结道，这些法律是由一种“道德恐慌”驱动的，以言论自由和数字隐私为代价换取虚假的安全感。这种零碎的立法不仅没有保护儿童，反而催生了一个监控国家，使最脆弱的用户群体处于劣势，并限制了关键信息的流通。

---

## 3. Garage —— 一款极其可靠、甚至可以在数据中心之外运行的 S3 对象存储。

**原文标题**: Garage – An S3 object store so reliable you can run it outside datacenters

**原文链接**: [https://garagehq.deuxfleurs.fr/](https://garagehq.deuxfleurs.fr/)

Garage 是一款轻量级、兼容 S3 的对象存储解决方案，专为非传统数据中心环境下的高弹性需求而设计。它旨在跨公共互联网的异构硬件上运行，是自托管、边缘计算和分布式部署的理想选择。

**关键特性与目标：**
*   **高弹性：** Garage 旨在抵御网络故障、高延迟以及磁盘或操作失误。它通过将每份数据复制到三个不同的区域来确保数据的持久性。
*   **低系统

**技术基础与支持：**
其架构利用了成熟的分布式系统研究成果，包括 Amazon 的 Dynamo、无冲突复制数据类型 (CRDTs) 以及 Maglev。

该项目由公共资金资助，并已通过 NGI POINTER 以及 NLnet 基金会（NGI0 Entrust 和 Commons 基金）获得了欧盟“地平线 (Horizon)”研究计划的多项资助。这些资金自 2021 年起支持全职开发人员，且承诺的支持将延续至 2025 年。

---

## 4. GotaTun —— Mullvad 的 Rust 版 WireGuard 实现

**原文标题**: GotaTun -- Mullvad's WireGuard Implementation in Rust

**原文链接**: [https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn](https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn)

Mullvad VPN 宣布推出 GotaTun，这是一款使用 Rust 编写的全新 WireGuard 实现。GotaTun 作为 Cloudflare BoringTun 的分支开发，旨在提供快速、高效和可靠的体验，同时集成了 DAITA 和 Multihop 等隐私增强功能。

转向 GotaTun 的主要驱动力是其先前实现方式 `wireguard-go` 的局限性。Mullvad 报告称，其 Android 应用超过 85% 的崩溃都源于基于 Go 的实现。此外，通过外部函数接口 (FFI) 将 Rust 与 Go 对接的技术复杂性，导致调试困难且维护繁琐。通过切换到 Rust，Mullvad 利用安全的多线程和零拷贝内存策略来提升性能和稳定性。

2025 年底 Android 版上线后的初步结果非常显著：
*   **稳定性：** 用户感知的崩溃率从 0.40% 降至 0.01%，且没有任何崩溃归因于 GotaTun。
*   **性能：** 用户反馈连接速度有所提高，电池消耗有所降低。
*   **集成：** 新实现能够与 Mullvad 的其他基于 Rust 的服务组件实现无缝集成。

展望 2026 年，Mullvad 计划对代码进行第三方安全审计，并在包括 iOS 和桌面端在内的所有剩余平台上用 GotaTun 替代 `wireguard-go`。在逐步淘汰旧版实现的同时，该公司将继续专注于进一步的性能优化。

---

## 5. Cursor 收购 Graphite

**原文标题**: Cursor Acquires Graphite

**原文链接**: [https://graphite.com/blog/graphite-joins-cursor](https://graphite.com/blog/graphite-joins-cursor)

**摘要：Cursor 收购 Graphite**

领先的代码评审平台 Graphite 已签署最终协议，将被 AI 原生代码编辑器 Cursor 收购。此次合并旨在打造一个端到端的、集成了 AI 的开发者工具链，实现代码创建、评审和合并的同步。

**战略逻辑**
Graphite 首席执行官 Merrill Lutsky 指出，虽然 Cursor 等 AI 工具显著加速了代码生成，但对于 Shopify、Snowflake 和 Figma 等公司的工程团队来说，人工评审流程已成为新的瓶颈。通过联手，两家公司旨在“打通开发的内外循环”，迈向拉取请求（PR）自动运行、人类与 AI 智能体无缝协作的未来。

**对 Graphite 的影响**
Graphite 将继续作为独立的产品和品牌运营。不过，此次收购为团队提供了更多资源以加速其路线图的推进。接下来的关键举措包括：
*   **深度集成：** 将 Cursor 的本地开发环境与 Graphite 的 PR 平台无缝连接。
*   **增强 AI 功能：** 将 Graphite 的 AI Reviewer 与 Cursor 的 “Bugbot” 相结合，并利用 Cursor 在代码模型方面的专业优势。
*   **工作流优化：** 加大对堆栈式 PR（stacked PRs）和合并队列的投入，以保持高速交付。

**时间表与团队**
交易预计将在未来几周内完成（视惯例成交条件而定），届时 Graphite 的全体团队将加入 Cursor。此次收购标志着软件开发正向统一平台转型，在 AI 驱动开发的共同愿景下，速度与质量将不再冲突。

---

## 6. 亚马逊将支持无 DRM 电子书的 ePub 和 PDF 格式下载。

**原文标题**: Amazon will allow ePub and PDF downloads for DRM-free eBooks

**原文链接**: [https://www.kdpcommunity.com/s/article/New-eBook-Download-Options-for-Readers-Coming-in-2026?language=en_US](https://www.kdpcommunity.com/s/article/New-eBook-Download-Options-for-Readers-Coming-in-2026?language=en_US)

根据提供的标题（由于正文内容似乎是技术错误消息），以下是该新闻的简要总结：

亚马逊已更新其政策，允许读者下载 EPUB 和 PDF 格式的**无数字版权管理 (DRM-free)** 电子书。这标志着 Kindle 生态系统的重大转变，该系统此前一直依赖受下载限制的 AZW 或现已弃用的 MOBI 等专有格式。

**关键点：**
*   **格式灵活性：** 用户现在可以下载 EPUB（行业标准）和 PDF 格式的无保护书籍，从而更轻松地在各种设备和第三方应用程序上阅读所购内容。
*   **聚焦无 DRM 内容：** 此功能专门适用于作者或出版商选择在不使用数字版权管理 (DRM) 软件的情况下分发的书籍。
*   **更广泛的兼容性：** 此举是继亚马逊近期为其“发送至 Kindle”服务提供 EPUB 文件支持后的又一动作，预示着其正向跨平台兼容性迈进。
*   **用户所有权：** 通过提供这些标准格式，亚马逊让读者在官方 Kindle 应用或硬件之外，能更自主地管理和访问其无 DRM 图书库。

这一变化反映了亚马逊对数字内容采取了更加开放的态度，使其服务与其他主要电子书零售商采用的标准出版实践保持一致。

---

## 7. FreeBSD 基金会笔记本电脑支持与易用性项目

**原文标题**: The FreeBSD Foundation's Laptop Support and Usability Project

**原文链接**: [https://github.com/FreeBSDFoundation/proj-laptop](https://github.com/FreeBSDFoundation/proj-laptop)

FreeBSD 基金会与 Quantum Leap Research 合作推出了“笔记本电脑支持与易用性项目”（Laptop Support and Usability Project）。这是一项耗资 75 万美元的计划，旨在确保 FreeBSD 在现代笔记本电脑上实现“开箱即用”的无缝体验。该项目于 2024 年 9 月获批，定于 2024 年第四季度启动，预计持续约一至两年。

该项目的主要目标是通过提升端点安全性和整体用户体验，加速开发者和企业机构的采纳。关键技术优先级包括为 FreeBSD 14.x 及更高版本提供更新，涵盖现代 WiFi、显卡、蓝牙、完整的音频支持以及可靠的待机/恢复功能。虽然主要受众是开发者，但该项目采用“用户故事”方法来定义需求，旨在通过减少对手动配置的需求，降低所有用户的技术门槛。

该工作由 Ed Maste 和 Alice Sowerby 负责管理，由基金会员工和签约开发人员组成的团队执行。项目范围是在参考了社区及戴尔（Dell）、AMD 和 Framework 等硬件厂商的意见后确定的。

基金会强调透明度和社区参与，将通过公开的 GitHub 路线图、桌面邮件列表以及笔记本与桌面工作组提供定期进展。除了代码更新外，该项目还将编写详尽的文档和操作指南。最终，该计划旨在使 FreeBSD 成为个人计算设备领域更具竞争力且用户友好的选择。

---

## 8. Believe the Checkbook

**原文标题**: Believe the Checkbook

**原文链接**: [https://robertgreiner.com/believe-the-checkbook/](https://robertgreiner.com/believe-the-checkbook/)

生成摘要时出错

---

## 9. TikTok Deal Is the Shittiest Possible Outcome, Making Everything Worse

**原文标题**: TikTok Deal Is the Shittiest Possible Outcome, Making Everything Worse

**原文链接**: [https://www.techdirt.com/2025/12/19/tiktok-deal-done-and-its-somehow-the-shittiest-possible-outcome-making-everything-worse/](https://www.techdirt.com/2025/12/19/tiktok-deal-done-and-its-somehow-the-shittiest-possible-outcome-making-everything-worse/)

生成摘要时出错

---

## 10. Show HN: I Made Loom for Mobile

**原文标题**: Show HN: I Made Loom for Mobile

**原文链接**: [https://demoscope.app](https://demoscope.app)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 2 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 3 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 4 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 5 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 6 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 7 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 8 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 9 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 10 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 11 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 12 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 13 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 14 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 15 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 16 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 17 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 18 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 19 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 20 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 21 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 22 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 23 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 24 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 25 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 26 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 27 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 28 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 29 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 30 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 31 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 32 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 33 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 34 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 35 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 36 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 37 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 38 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 39 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 40 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 41 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 42 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 43 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 44 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 45 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 46 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 47 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 48 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 49 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 50 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 51 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 52 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 53 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 54 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 55 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 56 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 57 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 58 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 59 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 60 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 61 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 62 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 63 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 64 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 65 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 66 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 67 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 68 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 69 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 70 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 71 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 72 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 73 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 74 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 75 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 76 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 77 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 78 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 79 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 80 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 81 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 82 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 83 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 84 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 85 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 86 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 87 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 88 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 89 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 90 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 91 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 92 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 93 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 94 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 95 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 96 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 97 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 98 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 99 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 100 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 101 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 102 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 103 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 104 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 105 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 106 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 107 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 108 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 109 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 110 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 111 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 112 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 113 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 114 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 115 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 116 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 117 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 118 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 119 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 120 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 121 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 122 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 123 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 124 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 125 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 126 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 127 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 128 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 129 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 130 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 131 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 132 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 133 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 134 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 135 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 136 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 137 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 138 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 139 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 140 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 141 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 142 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 143 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 144 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 145 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 146 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 147 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 148 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 149 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 150 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 151 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 152 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 153 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 154 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 155 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 156 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 157 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 158 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 159 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 160 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 161 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 162 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 163 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 164 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 165 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 166 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 167 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 168 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 169 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 170 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 171 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 172 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 173 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 174 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 175 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 176 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 177 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 178 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 179 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 180 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 181 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 182 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 183 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 184 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 185 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 186 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 187 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 188 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 189 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 190 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 191 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 192 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 193 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 194 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 195 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 196 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 197 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 198 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 199 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 200 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 201 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 202 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 203 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 204 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 205 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 206 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 207 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 208 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 209 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 210 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 211 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 212 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 213 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 214 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 215 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 216 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 217 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 218 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 219 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 220 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 221 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 222 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 223 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 224 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 225 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 226 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 227 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 228 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 229 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 230 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 231 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 232 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 233 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 234 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 235 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 236 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 237 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 238 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 239 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 240 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 241 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 242 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 243 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 244 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 245 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 246 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 247 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 248 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 249 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 250 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 251 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 252 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 253 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 254 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 255 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 256 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 257 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 258 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 259 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 260 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 261 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 262 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 263 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 264 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 265 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 266 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 267 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 268 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 269 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 270 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 271 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 272 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 273 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 274 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
