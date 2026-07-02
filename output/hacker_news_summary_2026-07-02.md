# Hacker News 热门文章摘要 (2026-07-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 自 Linux 6.9 起，LUKS 挂起不再从内存中擦除磁盘加密密钥。

**原文标题**: Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

**原文链接**: [https://mathstodon.xyz/@iblech/116769502749142438](https://mathstodon.xyz/@iblech/116769502749142438)

自 Linux 内核 6.9 版本发布以来，LUKS 磁盘加密领域发现了一个重大的安全回归问题。正如研究人员 Ingo Blechschmidt 所指出的，即使在进行了专门配置的情况下，内核在系统进入挂起（suspend）模式时，也无法再成功从内存（RAM）中清除加密密钥。

**问题详情**
此前，注重安全的用户通常可以利用 `cryptsetup` 和 `systemd` 启用相关功能，在系统睡眠期间从内存中逐出敏感加密密钥。此举旨在防御“冷启动攻击”，防止攻击者通过物理手段从挂起设备的内存中提取密钥来解密驱动器。然而，由于 6.9 和 6.10 版本内核在挂起过渡期间处理任务和内存的方式发生了变化，导致该清除过程失败或被绕过。

**安全影响**
这一故障意味着当计算机处于睡眠状态时，加密密钥仍驻留在易失性内存中。如果笔记本电脑在挂起状态下被盗或被他人访问，全盘加密将形同虚设，因为解锁数据所需的密钥仍保留在硬件中。

**现状与缓解措施**
该回归问题影响了依赖“挂起到内存（suspend-to-RAM）”安全工作流的用户。Linux 社区已对此进行了广泛讨论，开发人员正致力于通过补丁恢复预期的安全行为。建议用户关注其发行版的内核更新，并升级到已集成修复程序的版本（例如最近发布的 6.11 或 6.10.x 后期稳定版）。在此期间，使用“休眠”（挂起到磁盘）而非“挂起”（到内存）是更安全的替代方案，因为休眠会完全关闭系统电源并清空内存。

---

## 2. PeerTube 是一个自由、去中心化且联邦化的视频平台。

**原文标题**: PeerTube is a free, decentralized and federated video platform

**原文链接**: [https://github.com/Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube)

PeerTube 是一个由法国非营利组织 Framasoft 开发的自由、开源且去中心化的视频平台。作为 YouTube 和 Vimeo 等中心化服务的道德替代方案，PeerTube 采用联邦模式运行。它由一个独立且可互操作的实例网络组成，这些实例通过 ActivityPub 协议进行通信，使其能够与更广泛的“联邦宇宙”（Fediverse，包括 Mastodon 等平台）相集成。

**核心功能：**
*   **P2P 流媒体：** PeerTube 利用 WebRTC 技术在观众之间实现点对点共享，从而减轻单个服务器的带宽负载。这使得小型实例也能高效地承载热门内容。
*   **隐私与自主：** 该平台由社区所有且无广告。它杜绝了数据挖掘、“暗黑模式”的用户体验设计以及操纵性的推荐算法。
*   **创作者支持：** 创作者可以上传视频、开启永久直播，并通过 RSS 或联邦账号与粉丝互动。该平台不依赖广告收入，而是鼓励通过内置的捐赠链接获得观众的直接支持。
*   **高度定制：** 用户和管理员都能对其使用体验拥有极高的控制权，包括自定义界面、修改主题以及设定特定的审核政策。

**技术与社区层面：**
PeerTube 构建于透明、社区驱动的模型之上。它鼓励从代码编写、漏洞报告到翻译和文档编制等各种形式的贡献。对于希望搭建自有实例的用户，该项目提供了详尽的文档、REST API 以及适用于 Docker 和 YunoHost 等平台的社区软件包。该软件采用 GNU Affero 通用公共许可证（AGPLv3）授权，确保平台始终对所有人保持自由与开放。

---

## 3. Android Developer Verification: Threat masquerading as protection

**原文标题**: Android Developer Verification: Threat masquerading as protection

**原文链接**: [https://f-droid.org/2026/07/01/adv-malware.html](https://f-droid.org/2026/07/01/adv-malware.html)

生成摘要时出错

---

## 4. Launch HN: Manufact (YC S25) – MCP Cloud

**原文标题**: Launch HN: Manufact (YC S25) – MCP Cloud

**原文链接**: [https://manufact.com](https://manufact.com)

生成摘要时出错

---

## 5. How to ask for help from people who don't know you

**原文标题**: How to ask for help from people who don't know you

**原文链接**: [https://pradyuprasad.com/writings/how-to-ask-for-help/](https://pradyuprasad.com/writings/how-to-ask-for-help/)

生成摘要时出错

---

## 6. AI can't be listed as inventor on patent applications, Japan's top court rules

**原文标题**: AI can't be listed as inventor on patent applications, Japan's top court rules

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

生成摘要时出错

---

## 7. Podman v6.0.0

**原文标题**: Podman v6.0.0

**原文链接**: [https://blog.podman.io/2026/07/introducing-podman-v6-0-0/](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/)

生成摘要时出错

---

## 8. German button maker searched rivers of American Midwest for valuable shells

**原文标题**: German button maker searched rivers of American Midwest for valuable shells

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/](https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/)

生成摘要时出错

---

## 9. Spain Orders Blacklist of Palantir from Public and Private Companies

**原文标题**: Spain Orders Blacklist of Palantir from Public and Private Companies

**原文链接**: [https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv)

生成摘要时出错

---

## 10. Show HN: CLI tool for detecting non-exact code duplication with embedding models

**原文标题**: Show HN: CLI tool for detecting non-exact code duplication with embedding models

**原文链接**: [https://github.com/rafal-qa/slopo](https://github.com/rafal-qa/slopo)

生成摘要时出错

---

## 11. Kimi K2.7 Code is generally available in GitHub Copilot

**原文标题**: Kimi K2.7 Code is generally available in GitHub Copilot

**原文链接**: [https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/)

生成摘要时出错

---

## 12. The Egg Bandits Made a Thousand Times the Fine They Just Paid for Price Fixing

**原文标题**: The Egg Bandits Made a Thousand Times the Fine They Just Paid for Price Fixing

**原文链接**: [https://www.thebignewsletter.com/p/crime-pays-the-egg-bandits-made-a](https://www.thebignewsletter.com/p/crime-pays-the-egg-bandits-made-a)

生成摘要时出错

---

## 13. Is One Layer Enough? A Single Transformer Layer Matches Full-Parameter RL Train

**原文标题**: Is One Layer Enough? A Single Transformer Layer Matches Full-Parameter RL Train

**原文链接**: [https://arxiv.org/abs/2607.01232](https://arxiv.org/abs/2607.01232)

生成摘要时出错

---

## 14. The primary purpose of code review is to find code that will be hard to maintain

**原文标题**: The primary purpose of code review is to find code that will be hard to maintain

**原文链接**: [https://mathstodon.xyz/@mjd/115096720350507897](https://mathstodon.xyz/@mjd/115096720350507897)

生成摘要时出错

---

## 15. Show HN: Mail Memories – A desktop app to rescue photos from Gmail

**原文标题**: Show HN: Mail Memories – A desktop app to rescue photos from Gmail

**原文链接**: [https://mailmemories.com](https://mailmemories.com)

生成摘要时出错

---

## 16. Show HN: A graph paper generator that renders vector PDFs in the browser

**原文标题**: Show HN: A graph paper generator that renders vector PDFs in the browser

**原文链接**: [https://freegraphpaper.net/](https://freegraphpaper.net/)

生成摘要时出错

---

## 17. Hazel (YC W24) Is Hiring for Our Largest Government Contract

**原文标题**: Hazel (YC W24) Is Hiring for Our Largest Government Contract

**原文链接**: [https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci](https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci)

生成摘要时出错

---

## 18. The fall of the theorem economy

**原文标题**: The fall of the theorem economy

**原文链接**: [https://davidbessis.substack.com/p/the-fall-of-the-theorem-economy](https://davidbessis.substack.com/p/the-fall-of-the-theorem-economy)

生成摘要时出错

---

## 19. No LLM Code in Dependencies

**原文标题**: No LLM Code in Dependencies

**原文链接**: [https://joeyh.name/blog/entry/no_LLM_code_in_dependencies/](https://joeyh.name/blog/entry/no_LLM_code_in_dependencies/)

生成摘要时出错

---

## 20. WinPE as a stateless harness for Windows driver testing and fuzzing

**原文标题**: WinPE as a stateless harness for Windows driver testing and fuzzing

**原文链接**: [https://bednars.me/blog/winpe-harness](https://bednars.me/blog/winpe-harness)

生成摘要时出错

---

## 21. Show HN: ZeroFS – A log-structured filesystem for S3

**原文标题**: Show HN: ZeroFS – A log-structured filesystem for S3

**原文链接**: [https://www.zerofs.net/](https://www.zerofs.net/)

生成摘要时出错

---

## 22. CursorBench 3.1

**原文标题**: CursorBench 3.1

**原文链接**: [https://cursor.com/evals](https://cursor.com/evals)

生成摘要时出错

---

## 23. The US Government Is Now a Shareholder in 26 Companies

**原文标题**: The US Government Is Now a Shareholder in 26 Companies

**原文链接**: [https://moeonmargin.substack.com/p/the-us-government-is-now-a-shareholder](https://moeonmargin.substack.com/p/the-us-government-is-now-a-shareholder)

生成摘要时出错

---

## 24. Show HN: Claudoro, Pomodoro timer embedded in the Claude Code statusline

**原文标题**: Show HN: Claudoro, Pomodoro timer embedded in the Claude Code statusline

**原文链接**: [https://github.com/emson/claudoro](https://github.com/emson/claudoro)

生成摘要时出错

---

## 25. Germany’s Infineon opens major chip plant as EU seeks tech autonomy

**原文标题**: Germany’s Infineon opens major chip plant as EU seeks tech autonomy

**原文链接**: [https://www.rfi.fr/en/international-news/20260702-germany-s-infineon-opens-major-chip-plant-as-eu-seeks-tech-autonomy](https://www.rfi.fr/en/international-news/20260702-germany-s-infineon-opens-major-chip-plant-as-eu-seeks-tech-autonomy)

生成摘要时出错

---

## 26. Vite+ Beta

**原文标题**: Vite+ Beta

**原文链接**: [https://voidzero.dev/posts/announcing-vite-plus-beta](https://voidzero.dev/posts/announcing-vite-plus-beta)

生成摘要时出错

---

## 27. Senior SWE-Bench: open-source benchmark that assesses agents as senior engineers

**原文标题**: Senior SWE-Bench: open-source benchmark that assesses agents as senior engineers

**原文链接**: [https://senior-swe-bench.snorkel.ai/](https://senior-swe-bench.snorkel.ai/)

生成摘要时出错

---

## 28. How VictoriaLogs Stores Your Logs in a Columnar Layout

**原文标题**: How VictoriaLogs Stores Your Logs in a Columnar Layout

**原文链接**: [https://victoriametrics.com/blog/victorialogs-internals-columnar-storage-on-disk/index.html](https://victoriametrics.com/blog/victorialogs-internals-columnar-storage-on-disk/index.html)

生成摘要时出错

---

## 29. My favorite keyboards

**原文标题**: My favorite keyboards

**原文链接**: [https://fabiensanglard.net/keyboards/index.html](https://fabiensanglard.net/keyboards/index.html)

生成摘要时出错

---

## 30. Bring back crappy forums

**原文标题**: Bring back crappy forums

**原文链接**: [https://tedium.co/2026/07/01/online-web-forums-retrospective/](https://tedium.co/2026/07/01/online-web-forums-retrospective/)

生成摘要时出错

---

## 31. What Breaks a Cell's Ribs Can Make It Stronger

**原文标题**: What Breaks a Cell's Ribs Can Make It Stronger

**原文链接**: [https://www.quantamagazine.org/what-breaks-a-cells-ribs-can-make-it-stronger-20260629/](https://www.quantamagazine.org/what-breaks-a-cells-ribs-can-make-it-stronger-20260629/)

生成摘要时出错

---

## 32. Asymmetric Quantization: Near-Lossless Retrieval with 97% Storage Reduction

**原文标题**: Asymmetric Quantization: Near-Lossless Retrieval with 97% Storage Reduction

**原文链接**: [https://www.mixedbread.com/blog/asymmetric-quant](https://www.mixedbread.com/blog/asymmetric-quant)

生成摘要时出错

---

## 33. Natural history on canvas: Brueghel knew about bird-eating noctule bats

**原文标题**: Natural history on canvas: Brueghel knew about bird-eating noctule bats

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2536525123](https://www.pnas.org/doi/10.1073/pnas.2536525123)

生成摘要时出错

---

## 34. NSA tries to weaken mlkem standardisation

**原文标题**: NSA tries to weaken mlkem standardisation

**原文链接**: [https://nsa.2026.action.cr.yp.to](https://nsa.2026.action.cr.yp.to)

生成摘要时出错

---

## 35. Immich v3.0.0 Released

**原文标题**: Immich v3.0.0 Released

**原文链接**: [https://github.com/immich-app/immich/discussions/29439](https://github.com/immich-app/immich/discussions/29439)

生成摘要时出错

---

## 36. Winamp Skin Museum

**原文标题**: Winamp Skin Museum

**原文链接**: [https://skins.webamp.org](https://skins.webamp.org)

生成摘要时出错

---

## 37. Why jet engines aren't made in China

**原文标题**: Why jet engines aren't made in China

**原文链接**: [https://aakash.substack.com/p/why-jet-engines-arent-made-in-china](https://aakash.substack.com/p/why-jet-engines-arent-made-in-china)

生成摘要时出错

---

## 38. Show HN: zkGolf, competitive optimization of formally verified circuits.

**原文标题**: Show HN: zkGolf, competitive optimization of formally verified circuits.

**原文链接**: [https://zk.golf/](https://zk.golf/)

生成摘要时出错

---

## 39. Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'

**原文标题**: Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'

**原文链接**: [https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

生成摘要时出错

---

## 40. Lunatic: An Erlang-inspired runtime for WebAssembly

**原文标题**: Lunatic: An Erlang-inspired runtime for WebAssembly

**原文链接**: [https://lunatic.solutions/](https://lunatic.solutions/)

生成摘要时出错

---

## 41. FoundationDB's Flow – Bringing Actor-Based Concurrency to C++11

**原文标题**: FoundationDB's Flow – Bringing Actor-Based Concurrency to C++11

**原文链接**: [https://apple.github.io/foundationdb/flow.html](https://apple.github.io/foundationdb/flow.html)

生成摘要时出错

---

## 42. Comparing Fable and 10 other LLMs on refactoring a LangGraph god node

**原文标题**: Comparing Fable and 10 other LLMs on refactoring a LangGraph god node

**原文链接**: [https://wtf.korridzy.com/twilight-of-the-gods/](https://wtf.korridzy.com/twilight-of-the-gods/)

生成摘要时出错

---

## 43. Brave's latest browser release offers Containers for better and easier workflow

**原文标题**: Brave's latest browser release offers Containers for better and easier workflow

**原文链接**: [https://brave.com/blog/containers/](https://brave.com/blog/containers/)

生成摘要时出错

---

## 44. How do wombats poop cubes? (2021)

**原文标题**: How do wombats poop cubes? (2021)

**原文链接**: [https://www.science.org/content/article/how-do-wombats-poop-cubes-scientists-get-bottom-mystery](https://www.science.org/content/article/how-do-wombats-poop-cubes-scientists-get-bottom-mystery)

生成摘要时出错

---

## 45. Show HN: Cyclearchive.com – search vintage cycling magazines

**原文标题**: Show HN: Cyclearchive.com – search vintage cycling magazines

**原文链接**: [https://cyclearchive.com/search/](https://cyclearchive.com/search/)

生成摘要时出错

---

## 46. Europe's top court upholds Google's record $4.7B antitrust fine

**原文标题**: Europe's top court upholds Google's record $4.7B antitrust fine

**原文链接**: [https://www.neowin.net/news/europes-top-court-upholds-googles-record-47-billion-antitrust-fine/](https://www.neowin.net/news/europes-top-court-upholds-googles-record-47-billion-antitrust-fine/)

生成摘要时出错

---

## 47. Oomwoo, an open-source robot vacuum you build yourself

**原文标题**: Oomwoo, an open-source robot vacuum you build yourself

**原文链接**: [https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/](https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/)

生成摘要时出错

---

## 48. For first time, a cell built from scratch grows and divides

**原文标题**: For first time, a cell built from scratch grows and divides

**原文链接**: [https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/)

生成摘要时出错

---

## 49. ZCode – Harness for GLM-5.2

**原文标题**: ZCode – Harness for GLM-5.2

**原文链接**: [https://zcode.z.ai/en](https://zcode.z.ai/en)

生成摘要时出错

---

## 50. Chipify – Open-source workflow automation for analog IC design

**原文标题**: Chipify – Open-source workflow automation for analog IC design

**原文链接**: [https://chipify.io/](https://chipify.io/)

生成摘要时出错

---

## 51. Show HN: I built an open-source alternative to Claude Cowork

**原文标题**: Show HN: I built an open-source alternative to Claude Cowork

**原文链接**: [https://github.com/valmishq/valmis](https://github.com/valmishq/valmis)

生成摘要时出错

---

## 52. The Underhanded C Contest

**原文标题**: The Underhanded C Contest

**原文链接**: [https://underhanded-c.org/](https://underhanded-c.org/)

生成摘要时出错

---

## 53. OpenAI ‘in early talks to give 5% stake to US government’

**原文标题**: OpenAI ‘in early talks to give 5% stake to US government’

**原文链接**: [https://www.theguardian.com/technology/2026/jul/02/openai-stake-us-government-ai-sam-altman](https://www.theguardian.com/technology/2026/jul/02/openai-stake-us-government-ai-sam-altman)

生成摘要时出错

---

## 54. Learn Vim motions with an ice-cream van

**原文标题**: Learn Vim motions with an ice-cream van

**原文链接**: [https://thisismodest.com/vimscoops/](https://thisismodest.com/vimscoops/)

生成摘要时出错

---

## 55. AI fake news complaining about how AI fake news is the death of real news

**原文标题**: AI fake news complaining about how AI fake news is the death of real news

**原文链接**: [https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

生成摘要时出错

---

## 56. Department of Commerce has lifted export controls on Claude Fable 5 and Mythos 5

**原文标题**: Department of Commerce has lifted export controls on Claude Fable 5 and Mythos 5

**原文链接**: [https://twitter.com/AnthropicAI/status/2072106151890809341](https://twitter.com/AnthropicAI/status/2072106151890809341)

生成摘要时出错

---

## 57. Show HN: Enola-A deterministic architecture graph for developers and AI agents

**原文标题**: Show HN: Enola-A deterministic architecture graph for developers and AI agents

**原文链接**: [https://github.com/enola-labs/enola/tree/main](https://github.com/enola-labs/enola/tree/main)

生成摘要时出错

---

## 58. Vibe Coded X11 Server Written in Rust Adds Xinerama, FreeBSD Support

**原文标题**: Vibe Coded X11 Server Written in Rust Adds Xinerama, FreeBSD Support

**原文链接**: [https://www.phoronix.com/news/YSERVER-1.3-Released](https://www.phoronix.com/news/YSERVER-1.3-Released)

生成摘要时出错

---

## 59. Zig: Package Management Moved from Compiler to Build System

**原文标题**: Zig: Package Management Moved from Compiler to Build System

**原文链接**: [https://ziglang.org/devlog/2026/?2026-06-30#2026-06-30](https://ziglang.org/devlog/2026/?2026-06-30#2026-06-30)

生成摘要时出错

---

## 60. Physical disc production ending in Jan 2028 for new games on PlayStation

**原文标题**: Physical disc production ending in Jan 2028 for new games on PlayStation

**原文链接**: [https://blog.playstation.com/2026/07/01/physical-disc-production-ending-in-january-2028-for-new-games-releasing-on-playstation-consoles/](https://blog.playstation.com/2026/07/01/physical-disc-production-ending-in-january-2028-for-new-games-releasing-on-playstation-consoles/)

生成摘要时出错

---

## 61. Tiny-C Reference Manual Excerpt

**原文标题**: Tiny-C Reference Manual Excerpt

**原文链接**: [https://permacomputer.solarpunk.au/?p=204](https://permacomputer.solarpunk.au/?p=204)

生成摘要时出错

---

## 62. Qdf – a Go serializer you query the raw bytes of, smaller than protobuf

**原文标题**: Qdf – a Go serializer you query the raw bytes of, smaller than protobuf

**原文链接**: [https://github.com/alex60217101990/qdf](https://github.com/alex60217101990/qdf)

生成摘要时出错

---

## 63. The <usermedia> HTML element

**原文标题**: The <usermedia> HTML element

**原文链接**: [https://developer.chrome.com/blog/usermedia-html-element](https://developer.chrome.com/blog/usermedia-html-element)

生成摘要时出错

---

## 64. What to learn to be a graphics programmer

**原文标题**: What to learn to be a graphics programmer

**原文链接**: [https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/)

生成摘要时出错

---

## 65. The Apple Disk II Controller Card (2021)

**原文标题**: The Apple Disk II Controller Card (2021)

**原文链接**: [https://www.bigmessowires.com/2021/11/12/the-amazing-disk-ii-controller-card/](https://www.bigmessowires.com/2021/11/12/the-amazing-disk-ii-controller-card/)

生成摘要时出错

---

## 66. Chip Off The Old Block

**原文标题**: Chip Off The Old Block

**原文链接**: [https://www.astralcodexten.com/p/chip-off-the-old-block](https://www.astralcodexten.com/p/chip-off-the-old-block)

生成摘要时出错

---

## 67. Claude Code is steganographically marking requests

**原文标题**: Claude Code is steganographically marking requests

**原文链接**: [https://thereallo.dev/blog/claude-code-prompt-steganography](https://thereallo.dev/blog/claude-code-prompt-steganography)

生成摘要时出错

---

## 68. 1-Bit Pixel Art Emojis

**原文标题**: 1-Bit Pixel Art Emojis

**原文链接**: [https://hypertalking.com/2023/05/15/1-bit-pixel-art-emojis/](https://hypertalking.com/2023/05/15/1-bit-pixel-art-emojis/)

生成摘要时出错

---

## 69. How We Made IPFS Content Publishing 10x Faster

**原文标题**: How We Made IPFS Content Publishing 10x Faster

**原文链接**: [https://probelab.io/blog/optimistic-provide/](https://probelab.io/blog/optimistic-provide/)

生成摘要时出错

---

## 70. ChatControl 1.0 mass scanning is to be sneaked through via a 3rd vote next week

**原文标题**: ChatControl 1.0 mass scanning is to be sneaked through via a 3rd vote next week

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/116849906752825989](https://digitalcourage.social/@echo_pbreyer/116849906752825989)

生成摘要时出错

---

## 71. FFmpeg 9.1's new AAC encoder

**原文标题**: FFmpeg 9.1's new AAC encoder

**原文链接**: [https://hydrogenaudio.org/index.php/topic,129691.0.html](https://hydrogenaudio.org/index.php/topic,129691.0.html)

生成摘要时出错

---

## 72. Newly discovered spider builds spring loaded snare to catch ants

**原文标题**: Newly discovered spider builds spring loaded snare to catch ants

**原文链接**: [https://phys.org/news/2026-06-newly-australian-ballista-spider-snare.html](https://phys.org/news/2026-06-newly-australian-ballista-spider-snare.html)

生成摘要时出错

---

## 73. Show HN: I measured the half-life of 41,301 Show HN launches. It's 7 hours

**原文标题**: Show HN: I measured the half-life of 41,301 Show HN launches. It's 7 hours

**原文链接**: [https://jonno.nz/posts/your-show-hn-dies-in-7-hours/](https://jonno.nz/posts/your-show-hn-dies-in-7-hours/)

生成摘要时出错

---

## 74. Portugal launches first open-source AI model, joining Europe's sovereignty push

**原文标题**: Portugal launches first open-source AI model, joining Europe's sovereignty push

**原文链接**: [https://www.reuters.com/business/finance/portugal-launches-first-open-source-ai-model-joining-europes-sovereignty-push-2026-07-01/](https://www.reuters.com/business/finance/portugal-launches-first-open-source-ai-model-joining-europes-sovereignty-push-2026-07-01/)

生成摘要时出错

---

## 75. 24-bit/192kHz music downloads and why they make no sense (2012)

**原文标题**: 24-bit/192kHz music downloads and why they make no sense (2012)

**原文链接**: [https://people.xiph.org/~xiphmont/demo/neil-young.html#toc_wd2bm](https://people.xiph.org/~xiphmont/demo/neil-young.html#toc_wd2bm)

生成摘要时出错

---

## 76. ArXiv's Next Chapter

**原文标题**: ArXiv's Next Chapter

**原文链接**: [https://blog.arxiv.org/2026/06/30/arxivs-next-chapter/](https://blog.arxiv.org/2026/06/30/arxivs-next-chapter/)

生成摘要时出错

---

## 77. Data-Directed Programming in Haskell

**原文标题**: Data-Directed Programming in Haskell

**原文链接**: [https://entropicthoughts.com/sicp-2-4-data-directed-programming-in-haskell](https://entropicthoughts.com/sicp-2-4-data-directed-programming-in-haskell)

生成摘要时出错

---

## 78. Asahi Linux 7.1 Progress Report

**原文标题**: Asahi Linux 7.1 Progress Report

**原文链接**: [https://asahilinux.org/2026/06/progress-report-7-1/](https://asahilinux.org/2026/06/progress-report-7-1/)

生成摘要时出错

---

## 79. Aerial Photographs (2017)

**原文标题**: Aerial Photographs (2017)

**原文链接**: [https://www.toronto.ca/city-government/accountability-operations-customer-service/access-city-information-or-records/city-of-toronto-archives/whats-online/maps/aerial-photographs/](https://www.toronto.ca/city-government/accountability-operations-customer-service/access-city-information-or-records/city-of-toronto-archives/whats-online/maps/aerial-photographs/)

生成摘要时出错

---

## 80. Text AI watermarks will always be trivial to remove

**原文标题**: Text AI watermarks will always be trivial to remove

**原文链接**: [https://www.seangoedecke.com/text-ai-watermarks/](https://www.seangoedecke.com/text-ai-watermarks/)

生成摘要时出错

---

## 81. Show HN: MemSignal - an experimental memory-pressure indicator for Windows

**原文标题**: Show HN: MemSignal - an experimental memory-pressure indicator for Windows

**原文链接**: [https://github.com/riccardoruspoli/MemSignal](https://github.com/riccardoruspoli/MemSignal)

生成摘要时出错

---

## 82. The Wisdom of Quinn the Eskimo (Apple Developer Technical Support Engineer)

**原文标题**: The Wisdom of Quinn the Eskimo (Apple Developer Technical Support Engineer)

**原文链接**: [https://github.com/macshome/The-Wisdom-of-Quinn](https://github.com/macshome/The-Wisdom-of-Quinn)

生成摘要时出错

---

## 83. Healthy but sedentary people show early decline in cellular energy production

**原文标题**: Healthy but sedentary people show early decline in cellular energy production

**原文链接**: [https://news.cuanschutz.edu/news-stories/healthy-but-sedentary-individuals-show-early-decline-in-cellular-energy-production](https://news.cuanschutz.edu/news-stories/healthy-but-sedentary-individuals-show-early-decline-in-cellular-energy-production)

生成摘要时出错

---

## 84. Opening up 'Zero-Knowledge Proof' technology to promote privacy in age assurance

**原文标题**: Opening up 'Zero-Knowledge Proof' technology to promote privacy in age assurance

**原文链接**: [https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/](https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/)

生成摘要时出错

---

## 85. Box3D, an open source 3D physics engine

**原文标题**: Box3D, an open source 3D physics engine

**原文链接**: [https://box2d.org/posts/2026/06/announcing-box3d/](https://box2d.org/posts/2026/06/announcing-box3d/)

生成摘要时出错

---

## 86. Show HN: A lightweight CLI tool to track and purge temporary packages in Linux

**原文标题**: Show HN: A lightweight CLI tool to track and purge temporary packages in Linux

**原文链接**: [https://github.com/hermetic-code/labeled-cli](https://github.com/hermetic-code/labeled-cli)

生成摘要时出错

---

## 87. Fable 5 is Back

**原文标题**: Fable 5 is Back

**原文链接**: [https://twitter.com/claudeai/status/2072402636813607381](https://twitter.com/claudeai/status/2072402636813607381)

生成摘要时出错

---

## 88. Sony Deletes 551 Movies PlayStation Owners Paid For

**原文标题**: Sony Deletes 551 Movies PlayStation Owners Paid For

**原文链接**: [https://reclaimthenet.org/sony-deletes-551-studiocanal-movies-playstation-owners-paid-for](https://reclaimthenet.org/sony-deletes-551-studiocanal-movies-playstation-owners-paid-for)

生成摘要时出错

---

## 89. Hanami 3.0: In Full Bloom

**原文标题**: Hanami 3.0: In Full Bloom

**原文链接**: [https://hanakai.org/blog/2026/06/30/hanami-3-0-in-full-bloom](https://hanakai.org/blog/2026/06/30/hanami-3-0-in-full-bloom)

生成摘要时出错

---

## 90. Weave Robotics launches Isaac 1, a $7,999 home robot with Fall 2026 deliveries

**原文标题**: Weave Robotics launches Isaac 1, a $7,999 home robot with Fall 2026 deliveries

**原文链接**: [https://www.weaverobotics.com/isaac-1](https://www.weaverobotics.com/isaac-1)

生成摘要时出错

---

## 91. Monetization Gateway: Charge for any resource behind Cloudflare via x402

**原文标题**: Monetization Gateway: Charge for any resource behind Cloudflare via x402

**原文链接**: [https://blog.cloudflare.com/monetization-gateway/](https://blog.cloudflare.com/monetization-gateway/)

生成摘要时出错

---

## 92. Building a custom octocopter from scratch with no prior hardware experience

**原文标题**: Building a custom octocopter from scratch with no prior hardware experience

**原文链接**: [https://karolina.mgdubiel.com/drone/](https://karolina.mgdubiel.com/drone/)

生成摘要时出错

---

## 93. Google loses fight over record $4.7B EU antitrust fine

**原文标题**: Google loses fight over record $4.7B EU antitrust fine

**原文链接**: [https://www.cnbc.com/2026/07/02/alphabet-google-android-eu-antitrust-fine-4-1-billion-euro-appeal.html](https://www.cnbc.com/2026/07/02/alphabet-google-android-eu-antitrust-fine-4-1-billion-euro-appeal.html)

生成摘要时出错

---

## 94. Using Aspect-Oriented Programming to Record DRL Agents' Data

**原文标题**: Using Aspect-Oriented Programming to Record DRL Agents' Data

**原文链接**: [https://blog.ptidej.net/using-aspect-oriented-programming-to-record-drl-agents-data/](https://blog.ptidej.net/using-aspect-oriented-programming-to-record-drl-agents-data/)

生成摘要时出错

---

## 95. Mortality associated with non-optimal ambient temperatures from 2000 to 2019

**原文标题**: Mortality associated with non-optimal ambient temperatures from 2000 to 2019

**原文链接**: [https://www.researchgate.net/publication/353058947_Global_regional_and_national_burden_of_mortality_associated_with_non-optimal_ambient_temperatures_from_2000_to_2019_a_three-stage_modelling_study](https://www.researchgate.net/publication/353058947_Global_regional_and_national_burden_of_mortality_associated_with_non-optimal_ambient_temperatures_from_2000_to_2019_a_three-stage_modelling_study)

生成摘要时出错

---

## 96. Solid and Clean Code never felt solid or clean to me

**原文标题**: Solid and Clean Code never felt solid or clean to me

**原文链接**: [https://devz.cl/posts/solid-never-felt-solid/](https://devz.cl/posts/solid-never-felt-solid/)

生成摘要时出错

---

## 97. Internal Combustion Engine (2021)

**原文标题**: Internal Combustion Engine (2021)

**原文链接**: [https://ciechanow.ski/internal-combustion-engine/](https://ciechanow.ski/internal-combustion-engine/)

生成摘要时出错

---

## 98. Nintendo has raised its employees base salary by 10%

**原文标题**: Nintendo has raised its employees base salary by 10%

**原文链接**: [https://mynintendonews.com/2026/06/26/nintendo-has-raised-its-employees-base-salary-by-10/](https://mynintendonews.com/2026/06/26/nintendo-has-raised-its-employees-base-salary-by-10/)

生成摘要时出错

---

## 99. Show HN: digga – DNS, RDAP/WHOIS, subdomains and more in one lookup

**原文标题**: Show HN: digga – DNS, RDAP/WHOIS, subdomains and more in one lookup

**原文链接**: [https://digga.dev](https://digga.dev)

生成摘要时出错

---

## 100. This blog is written in en-GB

**原文标题**: This blog is written in en-GB

**原文链接**: [https://shkspr.mobi/blog/2026/07/this-blog-is-written-in-en-gb/](https://shkspr.mobi/blog/2026/07/this-blog-is-written-in-en-gb/)

生成摘要时出错

---

