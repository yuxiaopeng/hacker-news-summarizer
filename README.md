# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-27.md)

*最后自动更新时间: 2026-05-27 19:42:54*
## 1. 我认为 Anthropic 和 OpenAI 已经找到了产品市场契合点。

**原文标题**: I think Anthropic and OpenAI have found product-market fit

**原文链接**: [https://simonwillison.net/2026/May/27/product-market-fit/](https://simonwillison.net/2026/May/27/product-market-fit/)

本文认为，到2026年5月，Anthropic和OpenAI已成功从追求大众普及转向高收益的企业级变现，从而实现了真正的产品市场匹配（PMF）。

这种转变的核心在于编程智能体（如 Claude Code 和 OpenAI Codex）的兴起。通用聊天机器人曾难以盈利，而这些智能体已成为高价值专业人士不可或缺的日常工具。由于智能体消耗的 Token 远多于标准对话，这些实验室激进地重组了企业定价策略。截至2026年4月，两家公司都已摒弃“全包式”固定收费，转而采用按席位费加直接 API 使用成本的模式。

这一转型的关键证据包括：
*   **财务增长：** 传闻 Anthropic 2026年第二季度的收入将达到109亿美元，这可能标志着其首个盈利季度。
*   **变现策略：** 实验室正剔除中间商（如 Cursor）直接向企业销售，以获取高 Token 使用量的全部价值，单名重度用户的月消费可能超过1000美元。
*   **招聘趋势：** 两家公司都将近30%的招聘岗位转向了企业销售和支持。
*   **基础设施支出：** Anthropic 与 SpaceX 签署的每月12.5亿美元算力协议预示着推理需求的巨量且持续。

作者将近期所谓的“AI失败”案例——如 Uber 超出 AI 预算或微软取消内部授权——重新定义为“令人肉疼”的实用性证据。这些并非失败的迹象，而是因为工具变得如此不可或缺，以至于其成本超出了传统的企业预算。作者总结道，2026年4月是一个重大的收入拐点，为两家前沿实验室即将到来的 IPO 奠定了基础。

---

## 2. 4K下的《模拟城市 3000》(2025)

**原文标题**: SimCity 3k in 4k (2025)

**原文链接**: [https://www.thran.uk/writ/hdid/2025/12/simcity-3k-in-4k.html](https://www.thran.uk/writ/hdid/2025/12/simcity-3k-in-4k.html)

这篇文章由 Thran 于 2025 年 12 月发表，为在现代 Windows 10 系统上以 4K 分辨率运行《模拟城市 3000》提供了一份全面的技术指南。作者认为，由于该作在复杂性与高质量等轴测像素艺术之间取得了平衡，它仍然是该系列的巅峰之作。

由于原版游戏受限于过时的分辨率（如 800x600），且在现代硬件上存在滚动卡顿和图形错误，作者概述了六步修复流程：

1. **GOG 补丁版 EXE：** 用 GOG 提供的版本替换原始可执行文件，以启用宽屏支持并免除 CD 运行要求。
2. **导航调整：** 手动编辑 `SC3U.ini` 文件中的 `ScrollMarginFactor` 参数，以修复异常的鼠标加速问题。
3. **D3D 包装器：** 安装 DirectX 包装器对于实现原生 3840x2160 支持和修复图形花屏至关重要。作者建议进行特定的 `.ini` 修改，以确保游戏以真正的全屏模式而非无边框模式运行。
4. **4GB 补丁：** 使用 NTCore 的工具允许游戏使用更多系统内存，有助于在滚动时更平滑地加载资源。
5. **禁用自动更新：** 替换 `UpdateSettings.ini` 文件，防止游戏在启动时因尝试连接已失效的 Maxis 服务器而卡死。
6. **音乐修复：** 作者提供了一种还原缺失曲目的方法，并介绍了如何直接将原版光盘中的高质量音频文件复制到硬盘。

该指南总结道，遵循这些步骤可以获得稳定且“华丽的 4K”体验。虽然该方法在 Windows 10 上进行了测试，但作者推测这些修复程序在 Windows 11 上同样有效，尽管他表示个人更偏好旧版操作系统。

---

## 3. 德国法律将强制算法推广国家批准的新闻

**原文标题**: Germany Law to Force Algorithm Boost for State-Approved News

**原文链接**: [https://nonogra.ph/germany-considers-law-to-force-social-media-algorithm-boost-for-state-approved-news-05-27-2026](https://nonogra.ph/germany-considers-law-to-force-social-media-algorithm-boost-for-state-approved-news-05-27-2026)

根据《阿波罗新闻》（Apollo News）获取的一份泄露文件，德国各州媒体监管机构正在制定一项《数字媒体国家条约》。该条约将从法律上要求X、Meta和TikTok等社交媒体平台在其算法中优先推送“经国家批准”的新闻。

该提案的核心是“公共价值”认定制度。许可与监督委员会（ZAK）——一个通过州议会产生的监管机构——将决定哪些媒体机构是“可靠”的。一旦某家媒体被认定具有“公共价值”，平台将被强制提高其可见度，提案甚至建议在用户推送中为该类内容设定“法定配额”。

文章强调了针对这一监管转变的几个关键担忧：

*   **政治影响：** 批评人士指出，由于监管人员是由与州议会挂钩的机构选出的，因此民选政客与决定新闻推广的官员之间存在直接联系。
*   **现有规则的扩张：** 该计划扩展了2025年的法规，这些法规已经赋予了德国公共广播联盟（ARD）和德国电视二台（ZDF）等“公共价值”媒体在应用商店和智能电视上的优先地位。
*   **针对异见：** 监管机构有制裁独立和右翼媒体（如*Nius*）的历史。自2020年以来，当局已发出近100次正式警告，主要针对小型独立出版物。
*   **自我审查：** 报告指出，如果算法可见度取决于政府的批准，媒体为了满足监管机构对“可靠”信息的标准，其编辑独立性可能会受到损害。

总之，拟议的法律将强制社交媒体公司优先推送经政府审核的来源，而非独立内容，从而使政治任命的监管机构对信息格局拥有重大的控制权。

---

## 4. 谷歌称人们喜爱AI模式后，DuckDuckGo搜索访问量增长了28%

**原文标题**: DuckDuckGo search saw 28% more visits after Google said people love AI mode

**原文链接**: [https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/](https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/)

由于用户正寻求谷歌（Google）日益繁重的AI搜索体验的替代方案，DuckDuckGo 的流量和应用安装量大幅激增。2026年5月下旬，DuckDuckGo 专门的无AI搜索页面访问量周环比平均增长了 22.7%，而 iOS 应用安装量平均飙升了 33%。

这一转变源于科技领袖对搜索未来走向的公开分歧。谷歌首席执行官桑达尔·皮查伊（Sundar Pichai）最近声称用户“喜爱”新的AI模式和概览功能，这助力谷歌 2026 年第一季度的搜索收入增长了 19%。相反，DuckDuckGo 首席执行官加布里埃尔·温伯格（Gabriel Weinberg）批评谷歌在没有提供退出选项的情况下向用户“强推”AI，并认为这种做法正在降低搜索质量。

虽然与谷歌 85% 的市场份额相比，DuckDuckGo 仅占据美国约 2% 的份额，仍是一个较小的参与者，但它将自己定位为“隐私优先”的替代选择。尽管 DuckDuckGo 也提供自己的 AI 工具（如 duck.ai），但它通过三大核心支柱实现了差异化：
1. **隐私：** 不收集搜索历史或聊天记录。
2. **数据完整性：** 用户数据不用于 AI 训练。
3. **选择权：** 用户可以轻松退出 AI 功能或过滤掉 AI 生成的内容。

文章最后指出，尽管 AI 对谷歌而言是利润丰厚的商业举措，但 DuckDuckGo 正成功吸引越来越多的用户群体，这些用户更看重更简洁、更传统、且无需强制 AI 干预的搜索环境。

---

## 5. Last.fm 现已独立

**原文标题**: Last.fm is now independent

**原文链接**: [https://support.last.fm/t/last-fm-is-now-independent/118591](https://support.last.fm/t/last-fm-is-now-independent/118591)

Last.fm 宣布，在所有权变更后，现已作为一家独立公司运营。尽管经历了这一转型，该平台强调，其核心服务、用户体验以及产品背后的团队均保持不变。

公告要点包括：
*   **数据连续性：** 用户账户、听歌记录 (scrobbles)、数据和隐私设置均不受影响，将完整保留。
*   **订阅服务：** Pro 订阅和计费流程将继续运行，不作任何更改。
*   **运营：** 原班团队将继续负责产品开发，各项服务将正常运行。

虽然公司计划在未来几周内分享更多关于未来发展方向的细节，但目前的重点是确保无缝过渡，不中断任何服务。

---

## 6. Valve 将 Steam Deck 售价上调了 200 多美元。

**原文标题**: Valve raises Steam Deck prices by more than $200

**原文链接**: [https://www.theverge.com/games/938340/valve-steam-deck-price-increase](https://www.theverge.com/games/938340/valve-steam-deck-price-increase)

Valve大幅上调了Steam Deck OLED系列机型的价格，理由是内存与存储成本上涨以及全球物流挑战。在新的价格体系下，512GB OLED版的价格从549美元涨至789美元，而1TB版则从649美元涨至949美元。

尽管涨幅显著，这些掌机目前仍有现货，预计送达时间为三至五个工作日。翻新机也以更高的价格销售，512GB和1TB OLED翻新机型的标价分别为629美元和759美元。

此次价格调整是被称为“RAMageddon”（内存末日）的行业大趋势的一部分。全球内存组件的短缺不仅影响了Valve，还迫使联想、索尼和任天堂等竞争对手提高了各自游戏硬件的价格。

组件短缺也影响了Valve的硬件路线图。虽然该公司已于5月4日成功推出了新款Steam控制器，但Steam Machine和Steam Frame的发布时间已从2026年初推迟至今年晚些时候。Valve表示，他们将继续关注形势，若组件成本发生变化，将及时向客户更新信息。

---

## 7. Mini Micro Fantasy Computer

**原文标题**: Mini Micro Fantasy Computer

**原文链接**: [https://miniscript.org/MiniMicro/index.html#about](https://miniscript.org/MiniMicro/index.html#about)

生成摘要时出错

---

## 8. 浏览器内容器构建

**原文标题**: In-Browser Container Builds

**原文链接**: [https://ochagavia.nl/blog/fully-in-browser-container-builds/](https://ochagavia.nl/blog/fully-in-browser-container-builds/)

本文介绍了一个 Web 应用的研究原型，它能够完全在 Web 浏览器中仅通过客户端代码构建容器镜像。通过该演示，用户可以选择基础镜像，定义启动 Shell 脚本，并将最终生成的产物导出为与 Docker 兼容的 tar 文件。

该项目的技术基础在于，容器镜像本质上是文件的集合。由于浏览器可以在沙箱环境中下载、解压、修改并重新打包这些文件，因此它们无需传统的后端基础设施即可实现容器构建器的核心功能。

虽然作者承认浏览器内构建在很大程度上是一个“噱头”，但该项目为自定义容器工具的强大能力提供了一个更广泛的概念验证。文章认为，尽管开发者经常依赖 `docker build` 等标准工具，但这些工具存在固有的局限性。通过深入理解容器的基本原理（如规范和文件结构），开发者可以构建满足特定需求的定制化工具。

作者以一个咨询项目为例，说明了通过优化的架构和缓存机制，定制化工具如何将数 GB 镜像的构建时间缩短至仅几秒钟。最后，文章鼓励开发者探索容器的内部机制，以解锁显著的性能提升，并获得超越行业标准工具限制的自由。

---

## 9. Tech CEOs are apparently suffering from AI psychosis

**原文标题**: Tech CEOs are apparently suffering from AI psychosis

**原文链接**: [https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/](https://techcrunch.com/2026/05/27/tech-ceos-are-apparently-suffering-from-ai-psychosis/)

生成摘要时出错

---

## 10. Canada to order military plane fleet from Sweden in shift from US suppliers

**原文标题**: Canada to order military plane fleet from Sweden in shift from US suppliers

**原文链接**: [https://www.theguardian.com/world/2026/may/27/canada-sweden-saab-globaleye-aircraft](https://www.theguardian.com/world/2026/may/27/canada-sweden-saab-globaleye-aircraft)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 2 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 3 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 4 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 5 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 6 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 7 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 8 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 9 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 10 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 11 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 12 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 13 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 14 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 15 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 16 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 17 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 18 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 19 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 20 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 21 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 22 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 23 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 24 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 25 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 26 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 27 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 28 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 29 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 30 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 31 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 32 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 33 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 34 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 35 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 36 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 37 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 38 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 39 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 40 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 41 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 42 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 43 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 44 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 45 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 46 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 47 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 48 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 49 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 50 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 51 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 52 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 53 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 54 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 55 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 56 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 57 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 58 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 59 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 60 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 61 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 62 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 63 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 64 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 65 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 66 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 67 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 68 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 69 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 70 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 71 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 72 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 73 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 74 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 75 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 76 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 77 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 78 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 79 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 80 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 81 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 82 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 83 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 84 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 85 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 86 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 87 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 88 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 89 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 90 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 91 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 92 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 93 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 94 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 95 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 96 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 97 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 98 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 99 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 100 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 101 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 102 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 103 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 104 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 105 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 106 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 107 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 108 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 109 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 110 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 111 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 112 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 113 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 114 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 115 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 116 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 117 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 118 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 119 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 120 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 121 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 122 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 123 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 124 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 125 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 126 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 127 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 128 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 129 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 130 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 131 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 132 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 133 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 134 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 135 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 136 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 137 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 138 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 139 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 140 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 141 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 142 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 143 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 144 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 145 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 146 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 147 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 148 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 149 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 150 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 151 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 152 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 153 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 154 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 155 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 156 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 157 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 158 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 159 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 160 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 161 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 162 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 163 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 164 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 165 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 166 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 167 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 168 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 169 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 170 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 171 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 172 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 173 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 174 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 175 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 176 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 177 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 178 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 179 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 180 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 181 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 182 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 183 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 184 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 185 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 186 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 187 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 188 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 189 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 190 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 191 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 192 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 193 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 194 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 195 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 196 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 197 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 198 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 199 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 200 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 201 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 202 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 203 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 204 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 205 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 206 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 207 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 208 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 209 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 210 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 211 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 212 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 213 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 214 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 215 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 216 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 217 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 218 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 219 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 220 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 221 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 222 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 223 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 224 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 225 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 226 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 227 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 228 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 229 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 230 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 231 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 232 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 233 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 234 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 235 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 236 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 237 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 238 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 239 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 240 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 241 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 242 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 243 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 244 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 245 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 246 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 247 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 248 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 249 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 250 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 251 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 252 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 253 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 254 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 255 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 256 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 257 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 258 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 259 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 260 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 261 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 262 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 263 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 264 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 265 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 266 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 267 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 268 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 269 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 270 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 271 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 272 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 273 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 274 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 275 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 276 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 277 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 278 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 279 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 280 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 281 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 282 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 283 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 284 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 285 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 286 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 287 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 288 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 289 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 290 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 291 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 292 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 293 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 294 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 295 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 296 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 297 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 298 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 299 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 300 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 301 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 302 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 303 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 304 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 305 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 306 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 307 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 308 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 309 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 310 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 311 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 312 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 313 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 314 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 315 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 316 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 317 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 318 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 319 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 320 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 321 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 322 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 323 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 324 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 325 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 326 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 327 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 328 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 329 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 330 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 331 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 332 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 333 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 334 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 335 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 336 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 337 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 338 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 339 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 340 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 341 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 342 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 343 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 344 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 345 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 346 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 347 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 348 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 349 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 350 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 351 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 352 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 353 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 354 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 355 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 356 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 357 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 358 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 359 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 360 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 361 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 362 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 363 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 364 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 365 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 366 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 367 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 368 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 369 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 370 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 371 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 372 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 373 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 374 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 375 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 376 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 377 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 378 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 379 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 380 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 381 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 382 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 383 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 384 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 385 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 386 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 387 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 388 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 389 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 390 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 391 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 392 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 393 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 394 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 395 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 396 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 397 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 398 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 399 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 400 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 401 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 402 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 403 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 404 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 405 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 406 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 407 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 408 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 409 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 410 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 411 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 412 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 413 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 414 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 415 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 416 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 417 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 418 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 419 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 420 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 421 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 422 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 423 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 424 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 425 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 426 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 427 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 428 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 429 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 430 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 431 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 432 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 433 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
