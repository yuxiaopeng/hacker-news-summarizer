# Hacker News 热门文章摘要 (2026-06-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Iroh 1.0

**原文标题**: Iroh 1.0

**原文链接**: [https://www.iroh.computer/blog/v1](https://www.iroh.computer/blog/v1)

Iroh 正式发布 1.0 版本，标志着其网络库的首个稳定版问世。该库旨在将互联网的抽象层从 IP 地址转向公钥。通过“拨号密钥而非 IP”，Iroh 确保设备无论网络环境、防火墙或物理位置如何变化，都能保持安全的寻址与连接。

1.0 版本的核心特性与技术里程碑包括：

*   **基于密钥的寻址：** 公钥作为稳定的标识符，简化了身份验证、权限管理和归属识别，同时允许设备在不同网络间切换而不会中断连接。
*   **高效性与 NAT 穿透：** Iroh 利用自定义的 QUIC 多路径和 NAT 穿透技术建立直接的点对点连接。这使得约 95% 的数据在设备间直接传输，从而降低了延迟和出站流量成本。
*   **广泛的兼容性：** 该库支持本地优先配置（无互联网连接亦可工作），可编译为 WASM 供浏览器使用，并支持蓝牙、LoRa 和 Tor 等自定义传输协议。
*   **扩展的语言支持：** 除了核心的 Rust 实现，Iroh 1.0 还新增了对 Python、Node.js、Swift 和 Kotlin 的官方支持，实现在移动端和桌面端应用的无缝集成。
*   **稳定性保证：** 1.0 版本承诺传输协议和 API 的稳定性。团队还建立了正式的支持周期，维护公共中继服务器，并为旧版本（特别是 v0.35x）用户提供迁移路径。

Iroh 已在数百万台设备上运行，应用场景涵盖大语言模型（LLM）训练到安全聊天等。对于希望构建去中心化、安全且高效的网络应用程序的开发者，Iroh 1.0 提供了一个成熟且生产就绪的技术栈。

---

## 2. TinyWind：具备真实风力物理系统的像素海盗航海游戏（累计航行里程超38万公里）

**原文标题**: TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文链接**: [https://tinywind.io](https://tinywind.io)

**TinyWind** 是一款像素风格的海盗航海游戏，其独特之处在于采用了**真实的物理风力系统**。与传统的街机风格游戏不同，该游戏的核心玩法侧重于通过掌握真实的受风机制，来应对海上航行的技术性挑战。

该游戏获得了极高的社区参与度，玩家在游戏中的累计航行里程已超过 **38 万公里**。TinyWind 将复古美学与物理仿真相结合，为热衷于海洋探索和航海精妙技巧的玩家提供了独特的体验。

---

## 3. 领英职位邀约中的后门

**原文标题**: A backdoor in a LinkedIn job offer

**原文链接**: [https://roman.pt/posts/linkedin-backdoor/](https://roman.pt/posts/linkedin-backdoor/)

本文详细介绍了一场伪装成 LinkedIn 招聘邀约的针对性社会工程学攻击。作者曾接到一家加密货币初创公司“招聘人员”的联系，对方要求其审查一个 GitHub 仓库，以协助解决“过时的 Node 模块”问题。

**攻击机制**
由于怀疑其中有诈，作者在沙盒环境中分析了代码。他们发现 `app/test/index.js` 中隐藏了一个伪装成粗糙测试套件的后门。为了规避简单的字符串搜索，恶意代码通过碎片拼接成一个远程 URL（`https://rest-icon-handler.store/icons/77`）。

该陷阱利用了 `package.json` 文件中的 `prepare` 脚本。在 Node.js 中，当用户执行 `npm install` 时，该脚本会自动运行。通过诱导开发人员安装依赖，攻击者可以强制受害者机器从其服务器获取并执行任意恶意载荷。

**身份盗用**
攻击者使用了复杂的冒充手段：
*   **GitHub：** 仓库的提交历史伪造了一名真实且无关的全栈工程师的姓名和邮箱。
*   **LinkedIn：** 招聘者的个人资料属于一名真实的艺术记者。当作者假称遇到安装问题时，“招聘人员”立即从非技术人设切换到提供专家级的 Node.js 故障排除指导，以此向作者施压并诱导其运行代码。

**核心总结**
作者强调，这类攻击极具迷惑性，往往利用真实专业人士的声誉进行背书。作者建议保持高度的安全防范意识，例如在审查不明来源的代码时，应使用一次性 VPS 环境和只读分析工具（如受限模式下的 AI 工具），因为即使是经验丰富的开发人员，在“疲惫或匆忙”时也可能中招。

---

## 4. 我的家庭实验室 AI 开发平台

**原文标题**: My Homelab AI Dev Platform

**原文链接**: [https://rsgm.dev/post/ai-dev-platform/](https://rsgm.dev/post/ai-dev-platform/)

作者描述了其构建的一个 AI 驱动开发平台，旨在简化家庭实验室（Homelab）中各种 Docker 服务的管理。通过将 OpenCode（一款与厂商无关的 Web IDE）与 GitOps 工作流相结合，作者将耗时的手动维护流程转变为高效的自动化流程。

**关键组件与配置：**
*   **基础设施：** 该方案在 TrueNAS 主机的专用虚拟机上将 OpenCode 作为 systemd 单元运行。这提供了一个持久且适配移动端的 Web UI，用于编写代码和访问终端。
*   **GitOps 集成：** 约有 12 个 Docker Compose 堆栈被迁移至 Arcane 以实现基于 Git 的管理。一旦更改合并，部署将自动执行。
*   **安全与防护措施：** 为最小化“爆炸半径”（潜在风险范围），AI 拥有专属的 Git 用户，且仅限推送至功能分支。它无法直接推送至部署分支或访问运行中的服务。通过“人工干预”机制，确保所有 AI 生成的代码在合并前都经过拉取请求（PR）的审核。

**优势：**
*   **高效：** 以前需要数小时的任务（如研究版本说明中的重大变更，或追踪跨堆栈的网络连通性），现在利用 AI 摘要和自动更新，仅需几分钟即可完成。
*   **提升可靠性：** 作者利用 AI 系统地为容器添加了健康检查，使识别问题变得更加容易。
*   **灵活性：** OpenCode 基于 Web 的特性允许作者在电脑上发起更改，并通过手机审查或合并 PR。

**挑战：**
主要的局限在于缺乏 CI 反馈。由于 Forgejo 不通过公开 API 提供 Action 日志，AI 目前还无法自动诊断测试失败或 Linter 错误，而作者认为这一功能在 GitHub 等其他环境中非常实用。

**总结：**
总体而言，该平台提供了一种可扩展且安全的方式，在利用 AI 管理复杂家庭基础设施的同时，保持了严格的管理控制。

---

## 5. Game Engine White Papers Commander Keen

**原文标题**: Game Engine White Papers Commander Keen

**原文链接**: [https://forgottenbytes.net/commander_keen.html](https://forgottenbytes.net/commander_keen.html)

生成摘要时出错

---

## 6. How TimescaleDB compresses time-series data

**原文标题**: How TimescaleDB compresses time-series data

**原文链接**: [https://roszigit.com/en/blog/timescaledb-compression-hypercore](https://roszigit.com/en/blog/timescaledb-compression-hypercore)

生成摘要时出错

---

## 7. Factoring "short-sleeve" RSA keys with polynomials

**原文标题**: Factoring "short-sleeve" RSA keys with polynomials

**原文链接**: [https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/](https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/)

生成摘要时出错

---

## 8. Hetzner Price Adjustment

**原文标题**: Hetzner Price Adjustment

**原文链接**: [https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers)

生成摘要时出错

---

## 9. Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文标题**: Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文链接**: [https://fata.dev](https://fata.dev)

生成摘要时出错

---

## 10. Making glass-to-metal seals for home­made vacuum tubes

**原文标题**: Making glass-to-metal seals for home­made vacuum tubes

**原文链接**: [https://maurycyz.com/projects/glass/1/](https://maurycyz.com/projects/glass/1/)

生成摘要时出错

---

## 11. Fox to buy Roku

**原文标题**: Fox to buy Roku

**原文链接**: [https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9)

生成摘要时出错

---

## 12. How memory safety CVEs differ between Rust and C/C++

**原文标题**: How memory safety CVEs differ between Rust and C/C++

**原文链接**: [https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html)

生成摘要时出错

---

## 13. Copper transport drug restores memory and clears toxic Alzheimer's proteins

**原文标题**: Copper transport drug restores memory and clears toxic Alzheimer's proteins

**原文链接**: [https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins)

生成摘要时出错

---

## 14. I Love the Computer

**原文标题**: I Love the Computer

**原文链接**: [https://michaelenger.com/blog/i-love-the-computer/](https://michaelenger.com/blog/i-love-the-computer/)

生成摘要时出错

---

## 15. Boot Naked Linux

**原文标题**: Boot Naked Linux

**原文链接**: [https://nick.zoic.org/art/boot-naked-linux/](https://nick.zoic.org/art/boot-naked-linux/)

生成摘要时出错

---

## 16. Typst 0.15.0

**原文标题**: Typst 0.15.0

**原文链接**: [https://typst.app/docs/changelog/0.15.0/](https://typst.app/docs/changelog/0.15.0/)

生成摘要时出错

---

## 17. Apple Foundation Models

**原文标题**: Apple Foundation Models

**原文链接**: [https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)

生成摘要时出错

---

## 18. What every coder should know about Gamma Correction

**原文标题**: What every coder should know about Gamma Correction

**原文链接**: [https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/](https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/)

生成摘要时出错

---

## 19. Can Europe train a frontier AI model on the compute it owns?

**原文标题**: Can Europe train a frontier AI model on the compute it owns?

**原文链接**: [https://github.com/sammysltd/euromesh](https://github.com/sammysltd/euromesh)

生成摘要时出错

---

## 20. Show HN: machine0 – Persistent NixOS VMs You Control from the CLI

**原文标题**: Show HN: machine0 – Persistent NixOS VMs You Control from the CLI

**原文链接**: [https://machine0.io](https://machine0.io)

生成摘要时出错

---

## 21. CrankGPT

**原文标题**: CrankGPT

**原文链接**: [https://crankgpt.com](https://crankgpt.com)

生成摘要时出错

---

## 22. The Alaska Server

**原文标题**: The Alaska Server

**原文链接**: [https://serialport.org/blog/the-alaska-server/](https://serialport.org/blog/the-alaska-server/)

生成摘要时出错

---

## 23. US Government Reportedly Allowing Federal Data Center Rules to Expire

**原文标题**: US Government Reportedly Allowing Federal Data Center Rules to Expire

**原文链接**: [https://gizmodo.com/us-government-reportedly-allowing-federal-data-center-rules-to-expire-2000772083](https://gizmodo.com/us-government-reportedly-allowing-federal-data-center-rules-to-expire-2000772083)

生成摘要时出错

---

## 24. US Air Force B-52 bomber crashes after takeoff, Edwards Air Force Base says

**原文标题**: US Air Force B-52 bomber crashes after takeoff, Edwards Air Force Base says

**原文链接**: [https://www.reuters.com/business/aerospace-defense/us-air-force-b-52-bomber-crashes-after-takeoff-edwards-air-force-base-says-2026-06-15/](https://www.reuters.com/business/aerospace-defense/us-air-force-b-52-bomber-crashes-after-takeoff-edwards-air-force-base-says-2026-06-15/)

生成摘要时出错

---

## 25. Teenagers Stayed Overnight at Their School and Found Hidden Ancient Roman Ruins

**原文标题**: Teenagers Stayed Overnight at Their School and Found Hidden Ancient Roman Ruins

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-italian-teenagers-stayed-overnight-at-their-school-they-found-ancient-roman-ruins-hidden-in-the-basement-180988917/](https://www.smithsonianmag.com/smart-news/these-italian-teenagers-stayed-overnight-at-their-school-they-found-ancient-roman-ruins-hidden-in-the-basement-180988917/)

生成摘要时出错

---

## 26. Openrouter Fusion API

**原文标题**: Openrouter Fusion API

**原文链接**: [https://openrouter.ai/openrouter/fusion](https://openrouter.ai/openrouter/fusion)

生成摘要时出错

---

## 27. Even more batteries included with Emacs

**原文标题**: Even more batteries included with Emacs

**原文链接**: [https://karthinks.com/software/even-more-batteries-included-with-emacs/](https://karthinks.com/software/even-more-batteries-included-with-emacs/)

生成摘要时出错

---

## 28. Improvement in advanced Alzheimer’s disease following high-dose psilocybin

**原文标题**: Improvement in advanced Alzheimer’s disease following high-dose psilocybin

**原文链接**: [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1813281/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1813281/full)

生成摘要时出错

---

## 29. Show HN: Exploiting Slack's video embeds to achieve E2EE communication

**原文标题**: Show HN: Exploiting Slack's video embeds to achieve E2EE communication

**原文链接**: [https://v1c.rocks/log/exploiting-slack-video/](https://v1c.rocks/log/exploiting-slack-video/)

生成摘要时出错

---

## 30. Ported my C game to WASM, here's every bug that I hit

**原文标题**: Ported my C game to WASM, here's every bug that I hit

**原文链接**: [http://ernesernesto.github.io/writes/portingmatchmorphosistowasm/](http://ernesernesto.github.io/writes/portingmatchmorphosistowasm/)

生成摘要时出错

---

## 31. Dalus (YC W25) Is Hiring a Senior Software Engineer in Germany

**原文标题**: Dalus (YC W25) Is Hiring a Senior Software Engineer in Germany

**原文链接**: [https://www.ycombinator.com/companies/dalus/jobs/5IDmKJt-senior-software-frontend-engineer-germany-office](https://www.ycombinator.com/companies/dalus/jobs/5IDmKJt-senior-software-frontend-engineer-germany-office)

生成摘要时出错

---

## 32. Salesforce to Acquire Fin (formerly Intercom) for $3.6B

**原文标题**: Salesforce to Acquire Fin (formerly Intercom) for $3.6B

**原文链接**: [https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL)

生成摘要时出错

---

## 33. Around 200 Stanford students walk out as Google CEO takes stage

**原文标题**: Around 200 Stanford students walk out as Google CEO takes stage

**原文链接**: [https://www.sfgate.com/tech/article/sundar-pichai-stanford-commencement-22304888.php](https://www.sfgate.com/tech/article/sundar-pichai-stanford-commencement-22304888.php)

生成摘要时出错

---

## 34. What happened to nerds?

**原文标题**: What happened to nerds?

**原文链接**: [https://mrmarket.lol/what-the-fuck-happened-to-nerds/](https://mrmarket.lol/what-the-fuck-happened-to-nerds/)

生成摘要时出错

---

## 35. Claude Corps

**原文标题**: Claude Corps

**原文链接**: [https://www.anthropic.com/news/claude-corps](https://www.anthropic.com/news/claude-corps)

生成摘要时出错

---

## 36. Asciline – real-time ASCII video rendering engine

**原文标题**: Asciline – real-time ASCII video rendering engine

**原文链接**: [https://github.com/YusufB5/ASCILINE](https://github.com/YusufB5/ASCILINE)

生成摘要时出错

---

## 37. Your ePub Is fine

**原文标题**: Your ePub Is fine

**原文链接**: [https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/](https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/)

生成摘要时出错

---

## 38. How to build a virtual cell and biology scaling laws

**原文标题**: How to build a virtual cell and biology scaling laws

**原文链接**: [https://letter.nikomc.com/p/virtual-cells](https://letter.nikomc.com/p/virtual-cells)

生成摘要时出错

---

## 39. Today's Frontier AI companies will never exceed the AI capability frontier again

**原文标题**: Today's Frontier AI companies will never exceed the AI capability frontier again

**原文链接**: [https://andrewtrask.substack.com/p/breaking-todays-frontier-ai-companies](https://andrewtrask.substack.com/p/breaking-todays-frontier-ai-companies)

生成摘要时出错

---

## 40. Anthropic's Safety Superpower

**原文标题**: Anthropic's Safety Superpower

**原文链接**: [https://stratechery.com/2026/anthropics-safety-superpower/](https://stratechery.com/2026/anthropics-safety-superpower/)

生成摘要时出错

---

## 41. Bitsy

**原文标题**: Bitsy

**原文链接**: [https://bitsy.org/](https://bitsy.org/)

生成摘要时出错

---

## 42. Google Flight Simulator

**原文标题**: Google Flight Simulator

**原文链接**: [https://developers.google.com/maps/documentation/earth/flight-simulator](https://developers.google.com/maps/documentation/earth/flight-simulator)

生成摘要时出错

---

## 43. 21 years and counting of 'eight fallacies of distributed computing' (2025)

**原文标题**: 21 years and counting of 'eight fallacies of distributed computing' (2025)

**原文链接**: [https://blog.apnic.net/2025/12/08/21-years-and-counting-of-eight-fallacies-of-distributed-computing/](https://blog.apnic.net/2025/12/08/21-years-and-counting-of-eight-fallacies-of-distributed-computing/)

生成摘要时出错

---

## 44. Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model

**原文标题**: Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model

**原文链接**: [https://github.com/nex-agi/Nex-N2/issues/4](https://github.com/nex-agi/Nex-N2/issues/4)

生成摘要时出错

---

## 45. Emacs, how it all started (for me)

**原文标题**: Emacs, how it all started (for me)

**原文链接**: [https://xvw.lol/en/articles/emacs-start.html](https://xvw.lol/en/articles/emacs-start.html)

生成摘要时出错

---

## 46. Curl will not accept vulnerability reports during July 2026

**原文标题**: Curl will not accept vulnerability reports during July 2026

**原文链接**: [https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)

生成摘要时出错

---

## 47. Building a plugin system without runtime, storage, or shared JavaScript context

**原文标题**: Building a plugin system without runtime, storage, or shared JavaScript context

**原文链接**: [https://tolgee.io/blog/building-a-plugin-system-for-tolgee-without-a-runtime-storage-or-shared-js-context](https://tolgee.io/blog/building-a-plugin-system-for-tolgee-without-a-runtime-storage-or-shared-js-context)

生成摘要时出错

---

## 48. There Is(Ǝ) – Such That (∋)

**原文标题**: There Is(Ǝ) – Such That (∋)

**原文链接**: [https://www.fractalkitty.com/there-is-3-such-that/](https://www.fractalkitty.com/there-is-3-such-that/)

生成摘要时出错

---

## 49. Show HN: I wrote a C++ ray tracer from scratch without AI

**原文标题**: Show HN: I wrote a C++ ray tracer from scratch without AI

**原文链接**: [https://github.com/themartiano/luz](https://github.com/themartiano/luz)

生成摘要时出错

---

## 50. Exploring building a tiny FUSE filesystem

**原文标题**: Exploring building a tiny FUSE filesystem

**原文链接**: [https://www.shayon.dev/post/2026/161/building-a-tiny-fuse-filesystem/](https://www.shayon.dev/post/2026/161/building-a-tiny-fuse-filesystem/)

生成摘要时出错

---

## 51. PRC-linked spies hid inside medical and military networks for more than a year

**原文标题**: PRC-linked spies hid inside medical and military networks for more than a year

**原文链接**: [https://www.theregister.com/research/2026/06/15/google-says-prc-linked-spies-hid-in-medical-research-networks-for-more-than-a-year/5254547](https://www.theregister.com/research/2026/06/15/google-says-prc-linked-spies-hid-in-medical-research-networks-for-more-than-a-year/5254547)

生成摘要时出错

---

## 52. Why does paper fold so well?

**原文标题**: Why does paper fold so well?

**原文链接**: [https://www.bbc.co.uk/programmes/w3ct8k70](https://www.bbc.co.uk/programmes/w3ct8k70)

生成摘要时出错

---

## 53. EU Air travellers to enjoy free cabin luggage and keep delay compensation

**原文标题**: EU Air travellers to enjoy free cabin luggage and keep delay compensation

**原文链接**: [https://www.euronews.com/my-europe/2026/06/15/air-travellers-to-enjoy-free-cabin-luggage-and-keep-delay-compensation-after-decade-long-t](https://www.euronews.com/my-europe/2026/06/15/air-travellers-to-enjoy-free-cabin-luggage-and-keep-delay-compensation-after-decade-long-t)

生成摘要时出错

---

## 54. Formal methods and the future of programming

**原文标题**: Formal methods and the future of programming

**原文链接**: [https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1)

生成摘要时出错

---

## 55. Air Force bomber crashed on takoff at California base

**原文标题**: Air Force bomber crashed on takoff at California base

**原文链接**: [https://www.nbcnews.com/news/us-news/air-force-bomber-crashed-takoff-california-base-rcna350183](https://www.nbcnews.com/news/us-news/air-force-bomber-crashed-takoff-california-base-rcna350183)

生成摘要时出错

---

## 56. Show HN: Kage – Shadow any website to a single binary for offline viewing

**原文标题**: Show HN: Kage – Shadow any website to a single binary for offline viewing

**原文链接**: [https://github.com/tamnd/kage](https://github.com/tamnd/kage)

生成摘要时出错

---

## 57. Balkan Sworn Virgins

**原文标题**: Balkan Sworn Virgins

**原文链接**: [https://en.wikipedia.org/wiki/Balkan_sworn_virgins](https://en.wikipedia.org/wiki/Balkan_sworn_virgins)

生成摘要时出错

---

## 58. Firewood Splitting Simulator

**原文标题**: Firewood Splitting Simulator

**原文链接**: [https://screen.toys/firewood/](https://screen.toys/firewood/)

生成摘要时出错

---

## 59. Council of Europe hacked in ShinyHunters' PeopleSoft heist

**原文标题**: Council of Europe hacked in ShinyHunters' PeopleSoft heist

**原文链接**: [https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757)

生成摘要时出错

---

## 60. The AI Price War Is Here, Piling Pressure on OpenAI and Anthropic

**原文标题**: The AI Price War Is Here, Piling Pressure on OpenAI and Anthropic

**原文链接**: [https://www.wsj.com/tech/ai/the-ai-price-war-is-here-piling-pressure-on-openai-and-anthropic-86e1d21b](https://www.wsj.com/tech/ai/the-ai-price-war-is-here-piling-pressure-on-openai-and-anthropic-86e1d21b)

生成摘要时出错

---

## 61. Show HN: Trace – Offline Mac meeting transcripts you can flag mid-call

**原文标题**: Show HN: Trace – Offline Mac meeting transcripts you can flag mid-call

**原文链接**: [https://traceapp.info](https://traceapp.info)

生成摘要时出错

---

## 62. Flock Misappropriates MythBusters

**原文标题**: Flock Misappropriates MythBusters

**原文链接**: [https://ipvm.com/reports/flock-mythbusters](https://ipvm.com/reports/flock-mythbusters)

生成摘要时出错

---

## 63. Show HN: Nxui – Copy-paste animated UI components for Vue

**原文标题**: Show HN: Nxui – Copy-paste animated UI components for Vue

**原文链接**: [https://nxui.geoql.in/docs/](https://nxui.geoql.in/docs/)

生成摘要时出错

---

## 64. The only scalable delete in Postgres is DROP TABLE

**原文标题**: The only scalable delete in Postgres is DROP TABLE

**原文链接**: [https://planetscale.com/blog/the-only-scalable-delete](https://planetscale.com/blog/the-only-scalable-delete)

生成摘要时出错

---

## 65. Fruit Is Too Sweet

**原文标题**: Fruit Is Too Sweet

**原文链接**: [https://www.theatlantic.com/culture/2026/06/fruit-sweet-sumo-cotton-candy-grape/687507/](https://www.theatlantic.com/culture/2026/06/fruit-sweet-sumo-cotton-candy-grape/687507/)

生成摘要时出错

---

## 66. Caddy compatibility for zeroserve: 3x throughput and 70% lower latency

**原文标题**: Caddy compatibility for zeroserve: 3x throughput and 70% lower latency

**原文链接**: [https://su3.io/posts/zeroserve-caddy-compat](https://su3.io/posts/zeroserve-caddy-compat)

生成摘要时出错

---

## 67. ShinyHunters hacked 100 orgs by exploiting an Oracle PeopleSoft 0-day

**原文标题**: ShinyHunters hacked 100 orgs by exploiting an Oracle PeopleSoft 0-day

**原文链接**: [https://www.theregister.com/cyber-crime/2026/06/11/shinyhunters-claims-oracle-peoplesoft-0-day-hit-100-orgs/5254443](https://www.theregister.com/cyber-crime/2026/06/11/shinyhunters-claims-oracle-peoplesoft-0-day-hit-100-orgs/5254443)

生成摘要时出错

---

## 68. Perlisisms (1982)

**原文标题**: Perlisisms (1982)

**原文链接**: [https://www.cs.yale.edu/homes/perlis-alan/quotes.html](https://www.cs.yale.edu/homes/perlis-alan/quotes.html)

生成摘要时出错

---

## 69. Chaosnet (1981)

**原文标题**: Chaosnet (1981)

**原文链接**: [https://tumbleweed.nu/r/lm-3/uv/amber.html](https://tumbleweed.nu/r/lm-3/uv/amber.html)

生成摘要时出错

---

## 70. Windows 11 users are tired of MS account requirements creeping into everything

**原文标题**: Windows 11 users are tired of MS account requirements creeping into everything

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-11-users-are-tired-of-microsoft-account-requirements-and-workarounds](https://www.windowscentral.com/microsoft/windows-11/windows-11-users-are-tired-of-microsoft-account-requirements-and-workarounds)

生成摘要时出错

---

## 71. How to earn a billion dollars

**原文标题**: How to earn a billion dollars

**原文链接**: [https://paulgraham.com/earn.html](https://paulgraham.com/earn.html)

生成摘要时出错

---

## 72. TorchCodec 0.14: HDR Video Decoding for CPU and CUDA, and Fast Wav Decoder

**原文标题**: TorchCodec 0.14: HDR Video Decoding for CPU and CUDA, and Fast Wav Decoder

**原文链接**: [https://github.com/meta-pytorch/torchcodec/releases/tag/v0.14.0](https://github.com/meta-pytorch/torchcodec/releases/tag/v0.14.0)

生成摘要时出错

---

## 73. Did a medieval flying monk spot Halley's comet, twice? It's complicated

**原文标题**: Did a medieval flying monk spot Halley's comet, twice? It's complicated

**原文链接**: [https://arstechnica.com/science/2026/06/did-a-medieval-flying-monk-spot-halleys-comet-twice-its-complicated/](https://arstechnica.com/science/2026/06/did-a-medieval-flying-monk-spot-halleys-comet-twice-its-complicated/)

生成摘要时出错

---

## 74. The Birth and Death of JavaScript (2014)

**原文标题**: The Birth and Death of JavaScript (2014)

**原文链接**: [https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

生成摘要时出错

---

## 75. Lisp's Influence on Ruby

**原文标题**: Lisp's Influence on Ruby

**原文链接**: [https://blog.tacoda.dev/lisps-influence-on-ruby-6a54f1a7740e](https://blog.tacoda.dev/lisps-influence-on-ruby-6a54f1a7740e)

生成摘要时出错

---

## 76. Show HN: Discover Wikipedia articles popular on Hacker News

**原文标题**: Show HN: Discover Wikipedia articles popular on Hacker News

**原文链接**: [https://www.orangecrumbs.com/](https://www.orangecrumbs.com/)

生成摘要时出错

---

## 77. FarOutCompany

**原文标题**: FarOutCompany

**原文链接**: [https://faroutcompany.com/](https://faroutcompany.com/)

生成摘要时出错

---

## 78. Segmented type appreciation corner (2018)

**原文标题**: Segmented type appreciation corner (2018)

**原文链接**: [https://aresluna.org/segmented-type/](https://aresluna.org/segmented-type/)

生成摘要时出错

---

## 79. A man with ALS is "the first power user" of a brain implant that lets him sp

**原文标题**: A man with ALS is "the first power user" of a brain implant that lets him sp

**原文链接**: [https://www.technologyreview.com/2026/06/15/1138953/man-als-first-power-user-brain-implant-speak-bci/](https://www.technologyreview.com/2026/06/15/1138953/man-als-first-power-user-brain-implant-speak-bci/)

生成摘要时出错

---

## 80. USB Power Delivery: Plugging into the Benefits

**原文标题**: USB Power Delivery: Plugging into the Benefits

**原文链接**: [https://www.aptiv.com/en/insights/article/usb-power-delivery-plugging-into-the-benefits](https://www.aptiv.com/en/insights/article/usb-power-delivery-plugging-into-the-benefits)

生成摘要时出错

---

## 81. A short history of Cerro Torre, the most controversial mountain (2012)

**原文标题**: A short history of Cerro Torre, the most controversial mountain (2012)

**原文链接**: [https://www.markhorrell.com/blog/2012/a-short-history-of-cerro-torre/](https://www.markhorrell.com/blog/2012/a-short-history-of-cerro-torre/)

生成摘要时出错

---

## 82. Being an old school web-based sports sim dev in the era of vibe coded games

**原文标题**: Being an old school web-based sports sim dev in the era of vibe coded games

**原文链接**: [https://zengm.com/blog/2026/06/vibecoded-games/](https://zengm.com/blog/2026/06/vibecoded-games/)

生成摘要时出错

---

## 83. Programming the ZX Spectrum's Bitmap Display

**原文标题**: Programming the ZX Spectrum's Bitmap Display

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/06/13/programming-the-zx-spectrums-bitmap-display/](https://bumbershootsoft.wordpress.com/2026/06/13/programming-the-zx-spectrums-bitmap-display/)

生成摘要时出错

---

## 84. Write for One Person

**原文标题**: Write for One Person

**原文链接**: [https://wizardzines.com/comics/write-for-one-person/](https://wizardzines.com/comics/write-for-one-person/)

生成摘要时出错

---

## 85. India, UAE partner on AI sovereignty to bypass Google, Microsoft

**原文标题**: India, UAE partner on AI sovereignty to bypass Google, Microsoft

**原文链接**: [https://restofworld.org/2026/india-uae-g42-cerebras-ai-sovereignty/](https://restofworld.org/2026/india-uae-g42-cerebras-ai-sovereignty/)

生成摘要时出错

---

## 86. GLM 5.2 Is Out

**原文标题**: GLM 5.2 Is Out

**原文链接**: [https://twitter.com/jietang/status/2065784751345287314](https://twitter.com/jietang/status/2065784751345287314)

生成摘要时出错

---

## 87. Every Frame Perfect

**原文标题**: Every Frame Perfect

**原文链接**: [https://tonsky.me/blog/every-frame-perfect/](https://tonsky.me/blog/every-frame-perfect/)

生成摘要时出错

---

## 88. Quivers: A year of linear algebra by drawing arrows

**原文标题**: Quivers: A year of linear algebra by drawing arrows

**原文链接**: [https://lisyarus.github.io/blog/posts/quivers-a-year-of-linear-algebra-by-drawing-arrows.html](https://lisyarus.github.io/blog/posts/quivers-a-year-of-linear-algebra-by-drawing-arrows.html)

生成摘要时出错

---

## 89. How did Atari apply side art to Arcade Cabinets?

**原文标题**: How did Atari apply side art to Arcade Cabinets?

**原文链接**: [https://arcadeblogger.com/2026/06/14/how-did-atari-apply-side-art-to-arcade-cabinets/](https://arcadeblogger.com/2026/06/14/how-did-atari-apply-side-art-to-arcade-cabinets/)

生成摘要时出错

---

## 90. Linux 7.1

**原文标题**: Linux 7.1

**原文链接**: [https://lore.kernel.org/lkml/CAHk-=wi4BF4bMhZNZ1tqs+FFV4OuZRe3ZqdWB+LxRLmRweUzQw@mail.gmail.com/T/#u](https://lore.kernel.org/lkml/CAHk-=wi4BF4bMhZNZ1tqs+FFV4OuZRe3ZqdWB+LxRLmRweUzQw@mail.gmail.com/T/#u)

生成摘要时出错

---

## 91. Show HN: 3D print Z reinforcement via injected loops

**原文标题**: Show HN: 3D print Z reinforcement via injected loops

**原文链接**: [https://mgunlogson.github.io/magma/](https://mgunlogson.github.io/magma/)

生成摘要时出错

---

## 92. Pac-Man, but you're the ghost

**原文标题**: Pac-Man, but you're the ghost

**原文链接**: [https://garrit.xyz/posts/2026-06-13-pac-man-but-you-re-the-ghost](https://garrit.xyz/posts/2026-06-13-pac-man-but-you-re-the-ghost)

生成摘要时出错

---

## 93. Israeli firm BlackCore suspected of meddling in New York and Scotland votes

**原文标题**: Israeli firm BlackCore suspected of meddling in New York and Scotland votes

**原文链接**: [https://www.reuters.com/world/israeli-firm-blackcore-also-suspected-meddling-nyc-scotland-votes-french-2026-06-11/](https://www.reuters.com/world/israeli-firm-blackcore-also-suspected-meddling-nyc-scotland-votes-french-2026-06-11/)

生成摘要时出错

---

## 94. Chopped, Stored, Secured – The Story of the Hash Function

**原文标题**: Chopped, Stored, Secured – The Story of the Hash Function

**原文链接**: [https://0xkrt26.github.io/math_behind_security/2026/06/09/the-story-of-the-hash-function.html](https://0xkrt26.github.io/math_behind_security/2026/06/09/the-story-of-the-hash-function.html)

生成摘要时出错

---

## 95. Noise infusion banned from statistical products published by Census Bureau

**原文标题**: Noise infusion banned from statistical products published by Census Bureau

**原文链接**: [https://desfontain.es/blog/banning-noise.html](https://desfontain.es/blog/banning-noise.html)

生成摘要时出错

---

## 96. Global density and biomass of arbuscular mycorrhizal fungal networks

**原文标题**: Global density and biomass of arbuscular mycorrhizal fungal networks

**原文链接**: [https://www.science.org/doi/10.1126/science.adu4373](https://www.science.org/doi/10.1126/science.adu4373)

生成摘要时出错

---

## 97. Smashed Toilet Phone Web Server

**原文标题**: Smashed Toilet Phone Web Server

**原文链接**: [https://www.offthebricks.com/articles/smashed-toilet-phone-web-server](https://www.offthebricks.com/articles/smashed-toilet-phone-web-server)

生成摘要时出错

---

## 98. Triple Shockwave from Sun Crossing Rocket

**原文标题**: Triple Shockwave from Sun Crossing Rocket

**原文链接**: [https://apod.nasa.gov/apod/ap260615.html](https://apod.nasa.gov/apod/ap260615.html)

生成摘要时出错

---

## 99. If you are asking for human attention, demonstrate human effort

**原文标题**: If you are asking for human attention, demonstrate human effort

**原文链接**: [https://tombedor.dev/human-attention-and-human-effort/](https://tombedor.dev/human-attention-and-human-effort/)

生成摘要时出错

---

## 100. CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文标题**: CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文链接**: [https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/)

生成摘要时出错

---

