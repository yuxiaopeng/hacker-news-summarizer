# Hacker News 热门文章摘要 (2026-05-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Reflex (YC W23) Is Hiring SWEs, Growth, and GTM Roles

**原文标题**: Reflex (YC W23) Is Hiring SWEs, Growth, and GTM Roles

**原文链接**: [https://www.ycombinator.com/companies/reflex/jobs](https://www.ycombinator.com/companies/reflex/jobs)

生成摘要时出错

---

## 12. Training our own AI models

**原文标题**: Training our own AI models

**原文链接**: [https://posthog.com/blog/training-ai-models](https://posthog.com/blog/training-ai-models)

生成摘要时出错

---

## 13. Stress disrupts hippocampal integration of overlapping events, memory inference

**原文标题**: Stress disrupts hippocampal integration of overlapping events, memory inference

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.aea5496?user_id=66c4bf745d78644b3aa57b08](https://www.science.org/doi/10.1126/sciadv.aea5496?user_id=66c4bf745d78644b3aa57b08)

生成摘要时出错

---

## 14. Matrix Multiplications on GPUs Run Faster When Given "Predictable" Data (2024)

**原文标题**: Matrix Multiplications on GPUs Run Faster When Given "Predictable" Data (2024)

**原文链接**: [https://www.thonking.ai/p/strangely-matrix-multiplications](https://www.thonking.ai/p/strangely-matrix-multiplications)

生成摘要时出错

---

## 15. Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction

**原文标题**: Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction

**原文链接**: [https://arxiv.org/abs/2605.21779](https://arxiv.org/abs/2605.21779)

生成摘要时出错

---

## 16. All of human cooking compressed into 2 megabytes

**原文标题**: All of human cooking compressed into 2 megabytes

**原文链接**: [https://arxiv.org/abs/2605.22391](https://arxiv.org/abs/2605.22391)

生成摘要时出错

---

## 17. Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS

**原文标题**: Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS

**原文链接**: [https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/](https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/)

生成摘要时出错

---

## 18. A Comma and a Question Mark, Redux: Quick Terminal Helpers Using Pi

**原文标题**: A Comma and a Question Mark, Redux: Quick Terminal Helpers Using Pi

**原文链接**: [https://z3ugma.github.io/2026/05/25/a-comma-and-a-question-mark/](https://z3ugma.github.io/2026/05/25/a-comma-and-a-question-mark/)

生成摘要时出错

---

## 19. Show HN: I made an emergency page for my family

**原文标题**: Show HN: I made an emergency page for my family

**原文链接**: [https://help.delduca.org](https://help.delduca.org)

生成摘要时出错

---

## 20. My new obsession: A horse-racing board game of pure luck

**原文标题**: My new obsession: A horse-racing board game of pure luck

**原文链接**: [https://alexanderbjoy.com/horse-race-board-game/](https://alexanderbjoy.com/horse-race-board-game/)

生成摘要时出错

---

## 21. Theseus: Translating Win32 to WASM

**原文标题**: Theseus: Translating Win32 to WASM

**原文链接**: [https://neugierig.org/software/blog/2026/05/theseus-wasm.html](https://neugierig.org/software/blog/2026/05/theseus-wasm.html)

生成摘要时出错

---

## 22. XLIDE: VBA without excel

**原文标题**: XLIDE: VBA without excel

**原文链接**: [https://github.com/WilliamSmithEdward/xlide_vscode](https://github.com/WilliamSmithEdward/xlide_vscode)

生成摘要时出错

---

## 23. Show HN: Open-source Workspace (mail,docs,spreadsheet,drive) web/iOS

**原文标题**: Show HN: Open-source Workspace (mail,docs,spreadsheet,drive) web/iOS

**原文链接**: [https://tinycld.org/](https://tinycld.org/)

生成摘要时出错

---

## 24. Cloudflare Flagship

**原文标题**: Cloudflare Flagship

**原文链接**: [https://developers.cloudflare.com/flagship/](https://developers.cloudflare.com/flagship/)

生成摘要时出错

---

## 25. Human Bottlenecks

**原文标题**: Human Bottlenecks

**原文链接**: [https://borretti.me/article/human-bottlenecks](https://borretti.me/article/human-bottlenecks)

生成摘要时出错

---

## 26. Atomically precise mechanosynthesis of carbon structures on hydrogenated Silicon

**原文标题**: Atomically precise mechanosynthesis of carbon structures on hydrogenated Silicon

**原文链接**: [https://arxiv.org/abs/2605.27250](https://arxiv.org/abs/2605.27250)

生成摘要时出错

---

## 27. Corporations can vote in some Delaware elections, judge says

**原文标题**: Corporations can vote in some Delaware elections, judge says

**原文链接**: [https://news.bloomberglaw.com/esg/corporations-have-the-right-to-vote-in-delaware-town-judge-says](https://news.bloomberglaw.com/esg/corporations-have-the-right-to-vote-in-delaware-town-judge-says)

生成摘要时出错

---

## 28. The Melancholy of Slaying Monsters

**原文标题**: The Melancholy of Slaying Monsters

**原文链接**: [https://thereader.mitpress.mit.edu/the-strange-melancholy-of-slaying-monsters/](https://thereader.mitpress.mit.edu/the-strange-melancholy-of-slaying-monsters/)

生成摘要时出错

---

## 29. Incident with Pull Requests, Issues, Git Operations and API Requests

**原文标题**: Incident with Pull Requests, Issues, Git Operations and API Requests

**原文链接**: [https://www.githubstatus.com/incidents/xy1tt3hs572m](https://www.githubstatus.com/incidents/xy1tt3hs572m)

生成摘要时出错

---

## 30. Raft Consensus with a Minority of Nodes

**原文标题**: Raft Consensus with a Minority of Nodes

**原文链接**: [https://padhye.org/raft-minority/](https://padhye.org/raft-minority/)

生成摘要时出错

---

## 31. Phloto for My Photo Flow

**原文标题**: Phloto for My Photo Flow

**原文链接**: [https://cceckman.com/writing/phloto/](https://cceckman.com/writing/phloto/)

生成摘要时出错

---

## 32. Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs

**原文标题**: Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs

**原文链接**: [https://arps18.github.io/posts/claude-code-mastery/](https://arps18.github.io/posts/claude-code-mastery/)

生成摘要时出错

---

## 33. I'm Tired of Talking to AI

**原文标题**: I'm Tired of Talking to AI

**原文链接**: [https://orchidfiles.com/im-tired-of-ai-generated-answers/](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

生成摘要时出错

---

## 34. The worst job interview I ever had

**原文标题**: The worst job interview I ever had

**原文链接**: [https://www.oliverio.dev/blog/the-worst-job-interview-i-had](https://www.oliverio.dev/blog/the-worst-job-interview-i-had)

生成摘要时出错

---

## 35. How the ZX80 Works

**原文标题**: How the ZX80 Works

**原文链接**: [http://blog.tynemouthsoftware.co.uk/2019/10/how-the-zx80-works.html](http://blog.tynemouthsoftware.co.uk/2019/10/how-the-zx80-works.html)

生成摘要时出错

---

## 36. That Methyl Methacrylate Tank

**原文标题**: That Methyl Methacrylate Tank

**原文链接**: [https://www.science.org/content/blog-post/methyl-methacrylate-tank](https://www.science.org/content/blog-post/methyl-methacrylate-tank)

生成摘要时出错

---

## 37. BadHost – CVE-2026-48710: Starlette Host-Header Auth Bypass

**原文标题**: BadHost – CVE-2026-48710: Starlette Host-Header Auth Bypass

**原文链接**: [https://badhost.org/](https://badhost.org/)

生成摘要时出错

---

## 38. Private Equity Bought America's Essential Services

**原文标题**: Private Equity Bought America's Essential Services

**原文链接**: [https://rubbishtalk.com/economy/how-private-equity-bought-americas-essential-services/](https://rubbishtalk.com/economy/how-private-equity-bought-americas-essential-services/)

生成摘要时出错

---

## 39. Declassified CIA Cartography Maps from the 1980s

**原文标题**: Declassified CIA Cartography Maps from the 1980s

**原文链接**: [https://brilliantmaps.com/cia-maps-1980s/](https://brilliantmaps.com/cia-maps-1980s/)

生成摘要时出错

---

## 40. The Structural Barriers to AI Lawyers

**原文标题**: The Structural Barriers to AI Lawyers

**原文链接**: [https://www.diffuseai.pub/p/the-structural-barriers-to-ai-lawyers](https://www.diffuseai.pub/p/the-structural-barriers-to-ai-lawyers)

生成摘要时出错

---

## 41. The AI tech job slaughter gets real

**原文标题**: The AI tech job slaughter gets real

**原文链接**: [https://www.computerworld.com/article/4175956/the-ai-tech-job-slaughter-gets-real.html](https://www.computerworld.com/article/4175956/the-ai-tech-job-slaughter-gets-real.html)

生成摘要时出错

---

## 42. A few interesting modern pixel fonts

**原文标题**: A few interesting modern pixel fonts

**原文链接**: [https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/)

生成摘要时出错

---

## 43. The VibeSec Reckoning

**原文标题**: The VibeSec Reckoning

**原文链接**: [https://martinfowler.com/articles/vibesec-reckoning.html](https://martinfowler.com/articles/vibesec-reckoning.html)

生成摘要时出错

---

## 44. Objective metrics that change the most as we age

**原文标题**: Objective metrics that change the most as we age

**原文链接**: [https://www.empirical.health/blog/biomarkers-that-change-with-age/](https://www.empirical.health/blog/biomarkers-that-change-with-age/)

生成摘要时出错

---

## 45. I built a Git-tracked book production pipeline

**原文标题**: I built a Git-tracked book production pipeline

**原文链接**: [https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/](https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/)

生成摘要时出错

---

## 46. An Update on Composer and Packagist Supply Chain Security

**原文标题**: An Update on Composer and Packagist Supply Chain Security

**原文链接**: [https://blog.packagist.com/an-update-on-composer-packagist-supply-chain-security/](https://blog.packagist.com/an-update-on-composer-packagist-supply-chain-security/)

生成摘要时出错

---

## 47. Apple reportedly preps native support for Google Cast in iOS 27

**原文标题**: Apple reportedly preps native support for Google Cast in iOS 27

**原文链接**: [https://macdailynews.com/2026/05/27/apple-reportedly-preps-native-support-for-google-cast-in-ios-27/](https://macdailynews.com/2026/05/27/apple-reportedly-preps-native-support-for-google-cast-in-ios-27/)

生成摘要时出错

---

## 48. TSDuck: Open-source toolkit for MPEG-TS analysis and manipulation

**原文标题**: TSDuck: Open-source toolkit for MPEG-TS analysis and manipulation

**原文链接**: [https://tsduck.io/](https://tsduck.io/)

生成摘要时出错

---

## 49. OpenAI and Anthropic dig in against each other on AI jobs apocalypse

**原文标题**: OpenAI and Anthropic dig in against each other on AI jobs apocalypse

**原文链接**: [https://www.axios.com/2026/05/27/ai-hype-doom-openai-anthropic](https://www.axios.com/2026/05/27/ai-hype-doom-openai-anthropic)

生成摘要时出错

---

## 50. Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文标题**: Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文链接**: [https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/)

生成摘要时出错

---

## 51. Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文标题**: Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文链接**: [https://www.minicor.com/](https://www.minicor.com/)

生成摘要时出错

---

## 52. What Gets Kept

**原文标题**: What Gets Kept

**原文链接**: [https://www.newyorker.com/culture/the-weekend-essay/what-jack-kerouac-left-behind](https://www.newyorker.com/culture/the-weekend-essay/what-jack-kerouac-left-behind)

生成摘要时出错

---

## 53. What Is a Direct Attach Copper (DAC) Cable

**原文标题**: What Is a Direct Attach Copper (DAC) Cable

**原文链接**: [https://www.servethehome.com/what-is-a-direct-attach-copper-dac-cable/](https://www.servethehome.com/what-is-a-direct-attach-copper-dac-cable/)

生成摘要时出错

---

## 54. C array types are weird

**原文标题**: C array types are weird

**原文链接**: [https://anselmschueler.com/blogposts/2025-c-pointers/](https://anselmschueler.com/blogposts/2025-c-pointers/)

生成摘要时出错

---

## 55. Lombardy increases tax on data centers built in green and agricultural areas

**原文标题**: Lombardy increases tax on data centers built in green and agricultural areas

**原文链接**: [https://en.ilsole24ore.com/art/lombardy-introduces-increased-charges-of-up-to-200-per-cent-for-data-centre-construction-in-green-and-agricultural-areas-AI6Jp4ID](https://en.ilsole24ore.com/art/lombardy-introduces-increased-charges-of-up-to-200-per-cent-for-data-centre-construction-in-green-and-agricultural-areas-AI6Jp4ID)

生成摘要时出错

---

## 56. We are Poles, so, of course, we print in Latin

**原文标题**: We are Poles, so, of course, we print in Latin

**原文链接**: [https://www.ustc.ac.uk/news/we-are-poles-so-of-course-we-print-in-latin](https://www.ustc.ac.uk/news/we-are-poles-so-of-course-we-print-in-latin)

生成摘要时出错

---

## 57. Show HN: Posthorn, self-hosted mail gateway

**原文标题**: Show HN: Posthorn, self-hosted mail gateway

**原文链接**: [https://github.com/craigmccaskill/posthorn](https://github.com/craigmccaskill/posthorn)

生成摘要时出错

---

## 58. Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文标题**: Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文链接**: [https://github.com/logannye/rosalind](https://github.com/logannye/rosalind)

生成摘要时出错

---

## 59. A portentous reunion

**原文标题**: A portentous reunion

**原文链接**: [https://bcantrill.dtrace.org/2026/05/25/a-portentous-reunion/](https://bcantrill.dtrace.org/2026/05/25/a-portentous-reunion/)

生成摘要时出错

---

## 60. Steam Deck OLED is back in stock, with a price increase for both models

**原文标题**: Steam Deck OLED is back in stock, with a price increase for both models

**原文链接**: [https://store.steampowered.com/news/group/45479024/view/672869045073085538](https://store.steampowered.com/news/group/45479024/view/672869045073085538)

生成摘要时出错

---

