# Hacker News 热门文章摘要 (2026-11-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Java4Shell：OpenJDK 处理 Base64 时存在的远程代码执行漏洞

**原文标题**: Java4Shell: RCE in OpenJDK when processing Base64

**原文链接**: [https://calif.io/java4shell/](https://calif.io/java4shell/)

本文披露了 **Java4Shell** (CVE-2026-114938)，这是 OpenJDK Base64 解码器中一个严重的内存损坏漏洞，其 CVSS 评分高达 9.2。

**技术细节**
该缺陷存在于为了通过 x86-64 AVX-512 VBMI 指令优化 Base64 解码而使用的手写汇编代码中。在处理特定的恶意输入时（例如 64 个“A”字符后跟一个等号），解码器会计算出负的输出长度。这会导致越界写入并覆盖邻近内存，进而可能导致敏感数据泄露或远程代码执行 (RCE)。

**影响与范围**
由于 Base64 是身份验证和数据传输的基础，该漏洞影响了极其广泛的 Java 基础设施。研究人员已在 Jenkins、Atlassian Jira/Confluence、Keycloak 和 Elasticsearch 等广泛使用的应用程序中成功演示了 RCE。服务端和客户端（通过恶意的 TLS 连接）攻击均可行。

**核心主题**
*   **“半人马黑客”：** 该漏洞在短短三小时内通过 AI 代理与人类研究员的协作（即“半人马式黑客攻击”）被发现并武器化，凸显了 AI 如何加速漏洞利用程序的开发。
*   **优化的风险：** 尽管 Java 通常是内存安全的，但其底层性能优化（由 C++ 或汇编编写）绕过了这些保护机制，从而将“传统”内存损坏风险引入了现代技术栈。
*   **Vibe-Uncoding：** 作者主张利用 AI 识别并删除不必要的、臃肿的或“死”代码，以减少攻击面，并称这一过程为 “Vibe-Uncoding”。他们认为，许多系统从其并不真正需要的复杂优化或过时协议（如 FTP）中继承了安全风险。

---

## 2. GPT-6.2 阿斯特拉与索尔

**原文标题**: GPT‑6.2 Astra and Sol

**原文链接**: [https://openai.com/index/introducing-gpt-6-2-astra-sol/](https://openai.com/index/introducing-gpt-6-2-astra-sol/)

无法访问文章链接。

---

## 3. Quad9 撤出法国：煤矿里的金丝雀

**原文标题**: Quad9's withdrawal from France: A canary in the coal mine

**原文链接**: [https://blog.cloudflare.com/quad9-withdrawal-from-france/](https://blog.cloudflare.com/quad9-withdrawal-from-france/)

**摘要：Quad9 撤出法国**

瑞士非营利组织 Quad9 正将其公共 DNS 解析服务撤出法国。此前，法院因该组织拒绝屏蔽涉及侵权的域名而对其处以罚款。Quad9 认为，该裁决使其陷入了两难境地：要么面临毁灭性的诉讼，要么从根本上牺牲其服务的隐私和安全性。

文章强调了此次撤出的几项关键后果：

*   **基础设施立即中断：** 由于 Quad9 不追踪用户，因此无法通知他们服务关停。结果，包括医院、大学和政府机构在内的许多个人和组织可能会在不明原因的情况下突然遭遇断网。
*   **DNS 屏蔽的无效性：** Cloudflare 认为 DNS 屏蔽是一种容易被绕过的“笨拙工具”。它屏蔽的是整个域名而非特定的侵权文件，且无法从互联网上移除实际内容。
*   **日益增长的趋势：** Quad9 并非孤例。此前，思科（Cisco）在类似压力下已将其 OpenDNS 服务撤出多个欧洲国家；目前，Cloudflare、谷歌和思科还面临比利时法院的裁决，要求在 2027 年前开始屏蔽相关网站。
*   **附带损害：** 针对声誉良好且透明的解析服务，会将用户推向信誉较低的匿名服务，而这些服务可能会利用数据牟利，或缺乏恶意软件防护等安全功能。

Cloudflare 及其他行业领导者主张，版权持有者应将反盗版工作的重点放在托管服务商（即内容实际存放地）上，而非基础架构层。他们警告称，对 DNS 解析器持续施加法律压力会威胁开放互联网的稳定性，并开创一个危险的先例，即个别国家可以主宰全球内容的访问权限。目前，Cloudflare 及其同行正就类似裁决提起上诉，以防止互联网服务的进一步碎片化。

---

## 4. jQuery 4.1.0

**原文标题**: jQuery 4.1.0

**原文链接**: [https://github.com/jquery/jquery/releases/tag/4.1.0](https://github.com/jquery/jquery/releases/tag/4.1.0)

2026年11月17日，jQuery 4.1.0 版本与 3.8.0 版本同步发布。此次更新重点在于代码库的现代化、安全性提升，以及对现代 Web 标准兼容性的扩展。

**核心技术更新：**
*   **核心现代化：** 库架构发生了重大转变，放弃了传统的 `getElementsByTagName` 和 `getElementsByClassName` 方法，转而采用更现代的 `querySelectorAll`。同时重构了核心循环以防止数组越界错误。
*   **安全与选择器：** 该版本修复了标识符匹配中的 ReDoS（正则表达式拒绝服务）漏洞。此外，它还包含针对 Safari 27 中正则表达式解释器错误的临时解决方案，并优化了 `jQuery.uniqueSort` 以提升性能。
*   **Ajax 与序列化：** `jqXHR` 对象现在包含 `responseURL` 字段。此外，序列化模块现已支持表单关联的自定义元素，并为传输层（transports）添加了新的回调 API。
*   **XML 与 CSS：** 通过 `createElementNS` 增强了对 XML 文档的支持，并修复了表格样式探测的相关问题。

**文档与社区：**
发布说明中引入了多项组织更新，包括：
*   管理**机器生成（AI）贡献**的指南。
*   新增 **TuxCare** 为商业支持供应商。
*   更新了通过 HeroDevs 获取 jQuery NES（永无止境支持）的链接。

**测试：**
该版本包含了全面的测试套件更新，特别加强了对 SVG 数据、动画和 AJAX 二进制数据的覆盖，并针对 Chrome 和 Internet Explorer 中的特定浏览器行为调整了测试预期。

总体而言，jQuery 4.1.0 展现了在保持其跨浏览器可靠性传统的同时，致力于让该库在现代环境中保持高效与安全的持续努力。

---

## 5. Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文标题**: Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文链接**: [https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf)

在其最新的年度监管文件中，英伟达（Nvidia）已停止单独披露来自新加坡的收入，该市场此前在该公司销售额中占据了极高的份额。这一变化发生在该公司年度总营收飙升126%至609亿美元之际，而近期的季度数据表明其年化营收规模已突破1000亿美元。

历史上，新加坡一直被列为英伟达的主要市场，在2023年底约占其总营收的15%。该国之所以地位显著，主要是因其作为全球数据中心和云服务提供商枢纽的地位。然而，对新加坡的高额销售引发了外界对美国出口管制执行情况的审视。分析师质疑该地区是否被用作向中国运送先进制程AI芯片的“中转站”，而中国目前正面临严厉的美国贸易限制。

英伟达将地理营收归因于客户的“账单地址”而非产品的最终目的地。通过将新加坡重新分类至“其他国家”类别，在半导体技术地缘政治紧张局势加剧的背景下，该公司降低了特定地区销售数据的透明度。

尽管报告方式有所改变，但在AI硬件巨大需求的推动下，英伟达的整体增长势头依然是前所未有的。在应对复杂的贸易法规和不断变化的披露标准的同时，该公司继续主导着全球AI基础设施市场。

---

## 6. MAI Code 2 和 Code 2 Flash

**原文标题**: MAI Code 2 and Code 2 Flash

**原文链接**: [https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)

根据提供的文本，以下是简明摘要：

2026年11月17日，MAI Code 2 系列的衍生版本 MAI Cyber 2 Flash 的相关信息正式发布。公告强调了该新品的两大核心价值主张：领先的安全性和更低的成本。该产品被定位为一种高性能安全解决方案，旨在比以往版本更具价格优势且更易普及。

---

## 7. 

**原文标题**: 350 years ago, Ole Rømer discovered that light has a finite speed

**原文链接**: [https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969)

1676年，丹麦天文学家奥勒·罗默（Ole Rømer）证明了光以有限的速度传播，推翻了长期以来认为光是瞬时传播的观念，从而彻底改变了科学界。在巴黎天文台工作期间，罗默花了数年时间观测木星的卫星之一——木卫一。他发现了一个规律：当地球远离木星时，木卫一从木星阴影中出现的时间比预期的要晚；而当地球靠近木星时，出现的时间则比预期的要早。

罗默正确地推断出，这种差异的出现是因为光到达地球时所经过的距离不同。1676年9月，他成功做出公开预言，称11月9日木卫一的出现将比预期晚10分钟。根据他的观测，他估计光穿越地球轨道直径大约需要22分钟。这得出光速约为22.5万公里/秒——虽然比30万公里/秒的实际速度低了约25%，但在17世纪这已是一项了不起的成就。

尽管最初受到了一些质疑，但罗默的发现最终得到了克里斯蒂安·惠更斯和艾萨克·牛顿等著名科学家的支持。50年后，詹姆斯·布拉德利对恒星光行差的观测充分证实了他的结论。

罗默的研究成果至今仍是现代天文学的基石。通过证明光的传播需要时间，他开启了这样一种认知：观测深空等同于回望过去。这一概念对于我们今天研究宇宙的历史和演化至关重要。

---

## 8. Phrack 73 发布

**原文标题**: Phrack 73 Released

**原文链接**: [https://phrack.org/issues/73/introduction_md](https://phrack.org/issues/73/introduction_md)

生成摘要时出错

---

## 9. Highly classified US national security communications network goes down

**原文标题**: Highly classified US national security communications network goes down

**原文链接**: [https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down)

生成摘要时出错

---

## 10. Java4Shell：Java 17 中的预身份验证 RCE 漏洞使服务器面临风险 (CVE-2026-114938)

**原文标题**: Java4Shell: pre-auth RCE flaw in Java 17 puts servers at risk (CVE-2026-114938)

**原文链接**: [https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938](https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938)

**Java4Shell (CVE-2026-114938)** is a critical unauthenticated remote code execution (RCE) vulnerability affecting Java 17, 21, 25, and 27. Rated with a high severity score of **9.2 (CVSS 4.0)**, the flaw allows attackers to execute code remotely without authentication. While the vulnerability specifically targets the Java 17 line and newer releases, Oracle Java SE 8 and 11 are confirmed to be unaffected by this specific CVE.

Oracle released emergency patches on November 17, 2026. Organizations are urged to update their Java environments to the following fixed versions (or newer):
*   **Java 17:** 17.0.21.1
*   **Java 21:** 21.0.13.1
*   **Java 25:** 25.0.5.1
*   **Java 27:** 27.0.1.1

The scope of the vulnerability includes various distributions such as Amazon Corretto, Eclipse Temurin, Azul Zulu, and Microsoft Build of OpenJDK, as well as JDKs bundled inside containers and applications. While Amazon Corretto has released fixed builds, other vendors may be on different release schedules.

As of the report date, there have been no confirmed instances of exploitation in the wild. however, technical details are expected to be made public soon, which often leads to a surge in attack attempts. Security experts recommend prioritizing updates for internet-facing services. Currently, no workarounds exist; the only effective mitigation is upgrading to a patched runtime.

---

## 11. Microsoft's ONNX Runtime has disappeared from GitHub

**原文标题**: Microsoft's ONNX Runtime has disappeared from GitHub

**原文链接**: [https://github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)

生成摘要时出错

---

## 12. Solid 2.0

**原文标题**: Solid 2.0

**原文链接**: [https://www.solidjs.com/blog/solid-2-0-the-long-hold/](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

生成摘要时出错

---

## 13. Web Browser Engineering (2021)

**原文标题**: Web Browser Engineering (2021)

**原文链接**: [https://browser.engineering/](https://browser.engineering/)

**Web Browser Engineering (2021)** is a comprehensive guide designed to explain the inner workings of web browsers by teaching readers how to build a functional browser from scratch. Using approximately 2,000 lines of Python, the book covers the entire process—from initial networking to complex JavaScript execution.

Published by Oxford University Press, the book’s curriculum is divided into four main parts:

1.  **Loading Pages:** Focuses on the basics of networking, including URLs, HTTP requests, and rendering text to a screen.
2.  **Viewing Documents:** Explores the mechanics of parsing HTML and CSS, as well as managing inline and block layouts.
3.  **Running Applications:** Details the interactive side of the web, covering form submissions, JavaScript integration, and security protocols like cookies and XSS protection.
4.  **Modern Browsers:** Addresses advanced features such as the rendering pipeline, GPU-accelerated animations, task scheduling, accessibility, and performance optimization.

In addition to the technical chapters, the book includes a glossary, bibliography, and a list of academic courses that utilize the text. It is available in English, Korean, and Japanese. The authors also maintain a supporting community through a blog, GitHub discussion forum, and social media channels to provide updates and facilitate reader engagement.

---

## 14. What is the best harness for each model?

**原文标题**: What is the best harness for each model?

**原文链接**: [https://runta.com/blog/introducing-frontierharness-eval-v1-1/](https://runta.com/blog/introducing-frontierharness-eval-v1-1/)

生成摘要时出错

---

## 15. Apple Services Down

**原文标题**: Apple Services Down

**原文链接**: [https://developer.apple.com/system-status/](https://developer.apple.com/system-status/)

生成摘要时出错

---

## 16. Effects of a Nuclear Detonation in Low Earth Orbit

**原文标题**: Effects of a Nuclear Detonation in Low Earth Orbit

**原文链接**: [https://arxiv.org/abs/2611.09827](https://arxiv.org/abs/2611.09827)

生成摘要时出错

---

## 17. 谁在制造“制造机器的机器”？

**原文标题**: Who Builds the Machines That Build the Machines?

**原文链接**: [https://read.corematter.com/p/section-232-us-machine-tools](https://read.corematter.com/p/section-232-us-machine-tools)

生成摘要时出错

---

## 18. Archive Team is archiving the Apple Support Community (closes November 20, 2026)

**原文标题**: Archive Team is archiving the Apple Support Community (closes November 20, 2026)

**原文链接**: [https://wiki.archiveteam.org/index.php/Apple_Discussions](https://wiki.archiveteam.org/index.php/Apple_Discussions)

生成摘要时出错

---

## 19. Mouse Party

**原文标题**: Mouse Party

**原文链接**: [https://aboard.com/lets-have-a-mouse-party/](https://aboard.com/lets-have-a-mouse-party/)

In the article "Mouse Party," tech thinker Paul Ford introduces a free, open-source macOS application designed to help friends watch videos and interact online without the need for a dedicated web server. 

Created as a response to the "male loneliness epidemic," Mouse Party aims to simplify digital social gatherings. The app’s primary innovation is its use of Cloudflare’s "quick tunnel" technology, which allows a user to host a secure, temporary web server directly from their desktop. The process is intentionally simple: a host drags a video or file (such as an MP3, PDF, or ePub) into the app, which generates a disposable link to share with friends. Once the app is closed, the link, the server, and the chat history vanish forever.

Ford highlights several key features and philosophies behind the tool:
*   **Simplicity and Ephemerality:** It avoids the complexity of traditional server setups, offering a "no-login" experience that prioritizes privacy through its temporary nature.
*   **Collaborative Tools:** Beyond video, the app includes mini-apps for sketching, word games, and document sharing.
*   **Content Sourcing:** It is optimized for files and Archive.org links, encouraging a "digital campfire" atmosphere where friends can "talk trash" over retro commercials or niche documentaries.
*   **Social Trust:** Designed for friends rather than the general public, it lacks moderation tools; if a guest is disruptive, the host simply ends the session.

Ultimately, Mouse Party serves as a proof of concept for a more decentralized web, proving that users can create rich, collaborative experiences without relying on massive enterprise platforms or complex systems administration.

---

## 20. Not Everything Needs an LLM

**原文标题**: Not Everything Needs an LLM

**原文链接**: [https://newsletter.posthog.com/p/decision-models](https://newsletter.posthog.com/p/decision-models)

生成摘要时出错

---

## 21. Tencent Hy4 Flash

**原文标题**: Tencent Hy4 Flash

**原文链接**: [https://hy.tencent.ai/research/hy4-flash](https://hy.tencent.ai/research/hy4-flash)

生成摘要时出错

---

## 22. Latent Lattice Language Models

**原文标题**: Latent Lattice Language Models

**原文链接**: [https://shivamduggal4.github.io/latent-lattice-language-models/](https://shivamduggal4.github.io/latent-lattice-language-models/)

生成摘要时出错

---

## 23. Launch HN: StarSling (YC P25) – Self-improving CI for agent-volume repos

**原文标题**: Launch HN: StarSling (YC P25) – Self-improving CI for agent-volume repos

**原文链接**: [https://starsling.dev](https://starsling.dev)

生成摘要时出错

---

## 24. Zoltraak and the Dynamics of Military Innovation

**原文标题**: Zoltraak and the Dynamics of Military Innovation

**原文链接**: [https://jgeekstudies.org/2026/11/15/zoltraak-military-innovation-in-frieren/](https://jgeekstudies.org/2026/11/15/zoltraak-military-innovation-in-frieren/)

生成摘要时出错

---

## 25. New Evidence Shows School Phone Bans Are Gradually Improving Test Scores

**原文标题**: New Evidence Shows School Phone Bans Are Gradually Improving Test Scores

**原文链接**: [https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html](https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html)

生成摘要时出错

---

## 26. Show HN: Alloy CSS, dialogs, menus and tabs that work with JavaScript off

**原文标题**: Show HN: Alloy CSS, dialogs, menus and tabs that work with JavaScript off

**原文链接**: [https://alloyhtml.com/example.html](https://alloyhtml.com/example.html)

生成摘要时出错

---

## 27. Claude Code 团队如何看待验证

**原文标题**: How the Claude Code team thinks about verification

**原文链接**: [https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/)

生成摘要时出错

---

## 28. Show HN: TrnRT – An open-source LLM inference engine for AWS Trainium

**原文标题**: Show HN: TrnRT – An open-source LLM inference engine for AWS Trainium

**原文链接**: [https://github.com/RunanywhereAI/trnrt](https://github.com/RunanywhereAI/trnrt)

生成摘要时出错

---

## 29. Advancing computer-use agents for healthcare teams

**原文标题**: Advancing computer-use agents for healthcare teams

**原文链接**: [https://openai.com/index/advancing-computer-use-for-healthcare-teams/](https://openai.com/index/advancing-computer-use-for-healthcare-teams/)

生成摘要时出错

---

## 30. Fixing a WebKit bug to see if promises are made of train tracks

**原文标题**: Fixing a WebKit bug to see if promises are made of train tracks

**原文链接**: [https://alistair.sh/thenables](https://alistair.sh/thenables)

生成摘要时出错

---

## 31. First Photos of the Poles of a Rod-Shaped Bacterium

**原文标题**: First Photos of the Poles of a Rod-Shaped Bacterium

**原文链接**: [https://nautil.us/check-out-the-first-photos-of-the-poles-of-a-rod-shaped-bacterium-1286664](https://nautil.us/check-out-the-first-photos-of-the-poles-of-a-rod-shaped-bacterium-1286664)

生成摘要时出错

---

## 32. Elephant-Goldfish Model

**原文标题**: Elephant-Goldfish Model

**原文链接**: [https://egm.dev/](https://egm.dev/)

生成摘要时出错

---

## 33. New Species of Giant Fungus Discovered in China Grows Up to 20 Inches Tall

**原文标题**: New Species of Giant Fungus Discovered in China Grows Up to 20 Inches Tall

**原文链接**: [https://www.wired.com/story/new-species-of-giant-fungus-discovered-in-china-grows-up-to-20-inches-tall/](https://www.wired.com/story/new-species-of-giant-fungus-discovered-in-china-grows-up-to-20-inches-tall/)

生成摘要时出错

---

## 34. Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO

**原文标题**: Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO

**原文链接**: [https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html](https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html)

生成摘要时出错

---

## 35. Carnegie Mellon is putting computer science courses on YouTube for free

**原文标题**: Carnegie Mellon is putting computer science courses on YouTube for free

**原文链接**: [https://www.cs.cmu.edu/learn/](https://www.cs.cmu.edu/learn/)

生成摘要时出错

---

## 36. VisualBasic.World: A gallery of Planet Source Code programs from 1997 to 2012

**原文标题**: VisualBasic.World: A gallery of Planet Source Code programs from 1997 to 2012

**原文链接**: [https://visualbasic.world/](https://visualbasic.world/)

生成摘要时出错

---

## 37. Rows vs. Columns: How different are they, really?

**原文标题**: Rows vs. Columns: How different are they, really?

**原文链接**: [https://spiraldb.com/blog/rows-vs-columns](https://spiraldb.com/blog/rows-vs-columns)

生成摘要时出错

---

## 38. Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs

**原文标题**: Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs

**原文链接**: [https://arxiv.org/abs/2611.18126](https://arxiv.org/abs/2611.18126)

生成摘要时出错

---

## 39. California bans Waymo autonomous vehicles from state freeways

**原文标题**: California bans Waymo autonomous vehicles from state freeways

**原文链接**: [https://apnews.com/article/waymo-driverless-vehicle-california-freeway-ban-37bcd5371a4699a1850b7666b271946b](https://apnews.com/article/waymo-driverless-vehicle-california-freeway-ban-37bcd5371a4699a1850b7666b271946b)

生成摘要时出错

---

## 40. Turbo Pascal Compiler Written in Turbo Pascal

**原文标题**: Turbo Pascal Compiler Written in Turbo Pascal

**原文链接**: [https://turbo51.com/compiler-design/tpc16-turbo-pascal-compiler-written-in-turbo-pascal](https://turbo51.com/compiler-design/tpc16-turbo-pascal-compiler-written-in-turbo-pascal)

生成摘要时出错

---

## 41. Purism Launches Librem 5 v2, a RISC-V Phone to Empower People

**原文标题**: Purism Launches Librem 5 v2, a RISC-V Phone to Empower People

**原文链接**: [https://puri.sm/posts/purism-launches-librem-5-v2-a-risc-v-phone-to-empower-people/](https://puri.sm/posts/purism-launches-librem-5-v2-a-risc-v-phone-to-empower-people/)

生成摘要时出错

---

## 42. Antfly learned to stop worrying and love Apache 2.0

**原文标题**: Antfly learned to stop worrying and love Apache 2.0

**原文链接**: [https://antfly.io/thoughts/how-antfly-learned-to-stop-worrying-and-love-apache-2](https://antfly.io/thoughts/how-antfly-learned-to-stop-worrying-and-love-apache-2)

生成摘要时出错

---

## 43. Nimony: A New Compiler for Nim

**原文标题**: Nimony: A New Compiler for Nim

**原文链接**: [https://nimony.org/](https://nimony.org/)

生成摘要时出错

---

## 44. Computer Graphics from Scratch

**原文标题**: Computer Graphics from Scratch

**原文链接**: [https://www.gabrielgambetta.com/computer-graphics-from-scratch/index.html](https://www.gabrielgambetta.com/computer-graphics-from-scratch/index.html)

生成摘要时出错

---

## 45. Harvard researchers find AI coding agents shifted the bottleneck to code review

**原文标题**: Harvard researchers find AI coding agents shifted the bottleneck to code review

**原文链接**: [https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)

生成摘要时出错

---

## 46. Japan's Hometown Tax (2018)

**原文标题**: Japan's Hometown Tax (2018)

**原文链接**: [https://www.kalzumeus.com/2018/10/19/japanese-hometown-tax/](https://www.kalzumeus.com/2018/10/19/japanese-hometown-tax/)

生成摘要时出错

---

## 47. Apple faces French trial over alleged planned obsolescence of iPhones

**原文标题**: Apple faces French trial over alleged planned obsolescence of iPhones

**原文链接**: [https://us.afpnews.com/article/?apple-faces-french-trial-over-alleged-planned-obsolescence-of-iphones-source,D7NH6NW](https://us.afpnews.com/article/?apple-faces-french-trial-over-alleged-planned-obsolescence-of-iphones-source,D7NH6NW)

生成摘要时出错

---

## 48. Anthropic Paid Rubio's Ex-Chief of Staff's Firm $740k.it Lobbied His NSC

**原文标题**: Anthropic Paid Rubio's Ex-Chief of Staff's Firm $740k.it Lobbied His NSC

**原文链接**: [https://www.zerohedge.com/political/anthropic-paid-rubios-ex-chief-staffs-firm-740000-after-jensen-memo-it-lobbied-his-nsc](https://www.zerohedge.com/political/anthropic-paid-rubios-ex-chief-staffs-firm-740000-after-jensen-memo-it-lobbied-his-nsc)

生成摘要时出错

---

## 49. iCloud, App Store, and other Apple services hit by ongoing outage

**原文标题**: iCloud, App Store, and other Apple services hit by ongoing outage

**原文链接**: [https://9to5mac.com/2026/11/17/icloud-app-store-and-other-apple-services-hit-by-ongoing-outage/](https://9to5mac.com/2026/11/17/icloud-app-store-and-other-apple-services-hit-by-ongoing-outage/)

生成摘要时出错

---

## 50. What is w2rt6byl5nf1opmc-a.com?

**原文标题**: What is w2rt6byl5nf1opmc-a.com?

**原文链接**: [https://jack.cab/blog/siterate](https://jack.cab/blog/siterate)

生成摘要时出错

---

## 51. Nvidia Beats Estimates, Raises Guidance After Huang's Ouster

**原文标题**: Nvidia Beats Estimates, Raises Guidance After Huang's Ouster

**原文链接**: [https://www.wsj.com/tech/ai/nvidia-nvda-3q-2027-earnings-report-stock-6e642303](https://www.wsj.com/tech/ai/nvidia-nvda-3q-2027-earnings-report-stock-6e642303)

生成摘要时出错

---

## 52. Nvidia says it does not intend to reinstate Jensen Huang as CEO

**原文标题**: Nvidia says it does not intend to reinstate Jensen Huang as CEO

**原文链接**: [https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo](https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo)

生成摘要时出错

---

## 53. Show HN: Zigzag, a native Mac browser for people leaving Arc

**原文标题**: Show HN: Zigzag, a native Mac browser for people leaving Arc

**原文链接**: [https://github.com/ZigaoWang/zigzag](https://github.com/ZigaoWang/zigzag)

生成摘要时出错

---

## 54. Too Many Stadiums with Roofs

**原文标题**: Too Many Stadiums with Roofs

**原文链接**: [https://sharptext.net/2026/too-many-stadiums-with-roofs/](https://sharptext.net/2026/too-many-stadiums-with-roofs/)

生成摘要时出错

---

## 55. We don't need more apps, we need better open source

**原文标题**: We don't need more apps, we need better open source

**原文链接**: [https://jordankrueger.com/blog/better-open-source-not-more-apps/](https://jordankrueger.com/blog/better-open-source-not-more-apps/)

生成摘要时出错

---

## 56. Optimizely compromised, served malware on Zoom, GitLab

**原文标题**: Optimizely compromised, served malware on Zoom, GitLab

**原文链接**: [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

生成摘要时出错

---

## 57. My Empire of Dirt

**原文标题**: My Empire of Dirt

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/11/17/my-empire-of-dirt.html](https://geohot.github.io//blog/jekyll/update/2026/11/17/my-empire-of-dirt.html)

生成摘要时出错

---

## 58. Uncontacted Awá people approach government post in Brazil, ask for food

**原文标题**: Uncontacted Awá people approach government post in Brazil, ask for food

**原文链接**: [https://www.popsci.com/environment/uncontacted-indigenous-tribe-asks-help-brazil/](https://www.popsci.com/environment/uncontacted-indigenous-tribe-asks-help-brazil/)

生成摘要时出错

---

## 59. CA DMV bans Waymos from operating on state freeways after Bay Area incidents

**原文标题**: CA DMV bans Waymos from operating on state freeways after Bay Area incidents

**原文链接**: [https://abc7news.com/story/california-dmv-bans-waymos-operating-state-freeways-bay-area-traffic-incidents/20046974/](https://abc7news.com/story/california-dmv-bans-waymos-operating-state-freeways-bay-area-traffic-incidents/20046974/)

生成摘要时出错

---

## 60. Witches, vampires, ancient aliens–you'll find them all in Malta

**原文标题**: Witches, vampires, ancient aliens–you'll find them all in Malta

**原文链接**: [https://www.nationalgeographic.com/travel/article/explore-folklore-in-malta-witches-vampires-ancient-aliens](https://www.nationalgeographic.com/travel/article/explore-folklore-in-malta-witches-vampires-ancient-aliens)

生成摘要时出错

---

## 61. BugMeNot has closed

**原文标题**: BugMeNot has closed

**原文链接**: [https://www.bugmenot.com/](https://www.bugmenot.com/)

生成摘要时出错

---

## 62. Do Repeat Yourself

**原文标题**: Do Repeat Yourself

**原文链接**: [https://arcentry.com/blog/do-repeat-yourself/](https://arcentry.com/blog/do-repeat-yourself/)

生成摘要时出错

---

## 63. Stop Filming in Log?

**原文标题**: Stop Filming in Log?

**原文链接**: [https://digitalfilms.wordpress.com/2026/11/15/stop-filming-in-log/](https://digitalfilms.wordpress.com/2026/11/15/stop-filming-in-log/)

生成摘要时出错

---

## 64. Show HN: VennDB: append-only in-memory Rust DB for rows queried using bit flags

**原文标题**: Show HN: VennDB: append-only in-memory Rust DB for rows queried using bit flags

**原文链接**: [https://github.com/plabayo/venndb](https://github.com/plabayo/venndb)

生成摘要时出错

---

## 65. Human.md

**原文标题**: Human.md

**原文链接**: [https://www.human-md.ai/](https://www.human-md.ai/)

生成摘要时出错

---

## 66. Formal Verification Is Not Verifiable

**原文标题**: Formal Verification Is Not Verifiable

**原文链接**: [https://alperenkeles.com/posts/formal-verification-is-not-verifiable/](https://alperenkeles.com/posts/formal-verification-is-not-verifiable/)

生成摘要时出错

---

## 67. Leak of 15M Deutsche Bank files exposes systemic failures

**原文标题**: Leak of 15M Deutsche Bank files exposes systemic failures

**原文链接**: [https://www.ft.com/content/df518845-ed97-4a38-8a38-7fa9d4d24003](https://www.ft.com/content/df518845-ed97-4a38-8a38-7fa9d4d24003)

生成摘要时出错

---

## 68. GPT-6.2 Astra scores 100% on ARC-AGI-3

**原文标题**: GPT-6.2 Astra scores 100% on ARC-AGI-3

**原文链接**: [https://twitter.com/arcprize/status/2122751233442156678](https://twitter.com/arcprize/status/2122751233442156678)

生成摘要时出错

---

## 69. OpenCode Browse

**原文标题**: OpenCode Browse

**原文链接**: [https://opencode.ai/product/browse](https://opencode.ai/product/browse)

生成摘要时出错

---

## 70. Technical issue at JPMorgan Chase triggers online banking delays for US banks

**原文标题**: Technical issue at JPMorgan Chase triggers online banking delays for US banks

**原文链接**: [https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda)

生成摘要时出错

---

## 71. Show HN: SSH into DOS: I wrote an x86 (IBM PC) emulator

**原文标题**: Show HN: SSH into DOS: I wrote an x86 (IBM PC) emulator

**原文链接**: [https://www.dialup.net/farcall/](https://www.dialup.net/farcall/)

生成摘要时出错

---

## 72. Squircles

**原文标题**: Squircles

**原文链接**: [https://linebender.org/wiki/curves/squircle/](https://linebender.org/wiki/curves/squircle/)

生成摘要时出错

---

## 73. As Voyager 1 reaches one light-day from Earth, scientists reflect on its past

**原文标题**: As Voyager 1 reaches one light-day from Earth, scientists reflect on its past

**原文链接**: [https://www.livescience.com/space/space-exploration/out-there-moving-into-the-unknown-as-voyager-1-reaches-one-light-day-from-earth-scientists-reflect-on-its-past-and-its-future](https://www.livescience.com/space/space-exploration/out-there-moving-into-the-unknown-as-voyager-1-reaches-one-light-day-from-earth-scientists-reflect-on-its-past-and-its-future)

生成摘要时出错

---

## 74. Isomorphic Labs $5B Series C

**原文标题**: Isomorphic Labs $5B Series C

**原文链接**: [https://www.cnbc.com/2026/11/17/isomorphic-labs-series-c-ai-drug-discovery-.html](https://www.cnbc.com/2026/11/17/isomorphic-labs-series-c-ai-drug-discovery-.html)

生成摘要时出错

---

## 75. Test/verification technique effectiveness with Astra

**原文标题**: Test/verification technique effectiveness with Astra

**原文链接**: [https://danluu.com/astra-testing/](https://danluu.com/astra-testing/)

生成摘要时出错

---

## 76. If an App Asks for Full Disk Access or System and App Protection Override

**原文标题**: If an App Asks for Full Disk Access or System and App Protection Override

**原文链接**: [https://support.apple.com/en-us/149699](https://support.apple.com/en-us/149699)

生成摘要时出错

---

## 77. Spamhaus new email sender requirements in November

**原文标题**: Spamhaus new email sender requirements in November

**原文链接**: [https://www.spamhaus.org/sender-guidelines/](https://www.spamhaus.org/sender-guidelines/)

生成摘要时出错

---

## 78. The Fossils That Haunted Lovecraft

**原文标题**: The Fossils That Haunted Lovecraft

**原文链接**: [https://paleonerdish.wordpress.com/2026/10/30/halloween-special-xiv-the-fossils-that-haunted-lovecraft/](https://paleonerdish.wordpress.com/2026/10/30/halloween-special-xiv-the-fossils-that-haunted-lovecraft/)

生成摘要时出错

---

## 79. Why 3dfx 1 cards had such a washed out color output?

**原文标题**: Why 3dfx 1 cards had such a washed out color output?

**原文链接**: [https://twitter.com/id_aa_carmack/status/2122478083319992513](https://twitter.com/id_aa_carmack/status/2122478083319992513)

生成摘要时出错

---

## 80. Why did modems have speakers? (2019)

**原文标题**: Why did modems have speakers? (2019)

**原文链接**: [https://retrocomputing.stackexchange.com/questions/11765](https://retrocomputing.stackexchange.com/questions/11765)

生成摘要时出错

---

## 81. Texas Attorney General composed songs for Dragon Ball Z

**原文标题**: Texas Attorney General composed songs for Dragon Ball Z

**原文链接**: [https://www.reddit.com/r/interestingasfuck/comments/1xo0eyv/the_composer_of_this_dragon_ball_z_scene_has_just/](https://www.reddit.com/r/interestingasfuck/comments/1xo0eyv/the_composer_of_this_dragon_ball_z_scene_has_just/)

生成摘要时出错

---

## 82. How to Break into Security, Ptacek Edition (2012)

**原文标题**: How to Break into Security, Ptacek Edition (2012)

**原文链接**: [https://krebsonsecurity.com/2012/06/how-to-break-into-security-ptacek-edition/](https://krebsonsecurity.com/2012/06/how-to-break-into-security-ptacek-edition/)

生成摘要时出错

---

## 83. My Quest to push native Three.js quality match AAA Game Engines

**原文标题**: My Quest to push native Three.js quality match AAA Game Engines

**原文链接**: [https://ben3d.ca/blog/building-the-aaa-lighting-pipeline-in-threejs](https://ben3d.ca/blog/building-the-aaa-lighting-pipeline-in-threejs)

生成摘要时出错

---

## 84. Qwen3.8-Flash-Next 180B running in real time on a 16G MacBook Pro

**原文标题**: Qwen3.8-Flash-Next 180B running in real time on a 16G MacBook Pro

**原文链接**: [https://twitter.com/jalenluorion/status/2122758656668184633](https://twitter.com/jalenluorion/status/2122758656668184633)

生成摘要时出错

---

## 85. Chemistry is Actually Geometry

**原文标题**: Chemistry is Actually Geometry

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry](https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry)

生成摘要时出错

---

## 86. Frame – 31.5" color ePaper display

**原文标题**: Frame – 31.5" color ePaper display

**原文链接**: [https://trmnl.com/blog/introducing-frame](https://trmnl.com/blog/introducing-frame)

生成摘要时出错

---

## 87. Comcast's "fiber-powered Wi-Fi" is cable, AT&T says in false advertising case

**原文标题**: Comcast's "fiber-powered Wi-Fi" is cable, AT&T says in false advertising case

**原文链接**: [https://arstechnica.com/tech-policy/2026/11/comcast-falsely-advertises-cable-internet-as-fiber-powered-att-lawsuit-says/](https://arstechnica.com/tech-policy/2026/11/comcast-falsely-advertises-cable-internet-as-fiber-powered-att-lawsuit-says/)

生成摘要时出错

---

## 88. Interpreting claims that a theorem is correct because it was checked in Lean

**原文标题**: Interpreting claims that a theorem is correct because it was checked in Lean

**原文链接**: [https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)

生成摘要时出错

---

## 89. Windows 11 is collecting data on which coding agents and developer tools you use

**原文标题**: Windows 11 is collecting data on which coding agents and developer tools you use

**原文链接**: [https://xusheng.dev/posts/windows-coding-agent-telemetry/](https://xusheng.dev/posts/windows-coding-agent-telemetry/)

生成摘要时出错

---

## 90. Running coding agents without handing them my credentials

**原文标题**: Running coding agents without handing them my credentials

**原文链接**: [https://blog.antonio.cx/running-agents-with-lend](https://blog.antonio.cx/running-agents-with-lend)

生成摘要时出错

---

## 91. Microsoft blames monster email outage on software defect introduced in July fix

**原文标题**: Microsoft blames monster email outage on software defect introduced in July fix

**原文链接**: [https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026)

生成摘要时出错

---

## 92. Nvidia Announces Financial Results for Third Quarter and Fiscal 2027

**原文标题**: Nvidia Announces Financial Results for Third Quarter and Fiscal 2027

**原文链接**: [https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027)

生成摘要时出错

---

## 93. Many of Amazon’s Black Friday and Cyber Monday “deals” offered no savings

**原文标题**: Many of Amazon’s Black Friday and Cyber Monday “deals” offered no savings

**原文链接**: [http://groundworkcollaborative.org/news/amazons-decoy-deals-groundwork-investigation-reveals-nearly-1-in-3-black-friday-and-cyber-monday-deals-advertised-by-amazon-offered-no-savings-to-shoppers-nearly-1-in-10-w/](http://groundworkcollaborative.org/news/amazons-decoy-deals-groundwork-investigation-reveals-nearly-1-in-3-black-friday-and-cyber-monday-deals-advertised-by-amazon-offered-no-savings-to-shoppers-nearly-1-in-10-w/)

生成摘要时出错

---

## 94. Jiff 1.0: A datetime library for Rust

**原文标题**: Jiff 1.0: A datetime library for Rust

**原文链接**: [https://burntsushi.net/jiff/](https://burntsushi.net/jiff/)

生成摘要时出错

---

## 95. Stripe Press

**原文标题**: Stripe Press

**原文链接**: [https://stripe.press/](https://stripe.press/)

生成摘要时出错

---

## 96. AI tool has been used to automate cyber intrusions

**原文标题**: AI tool has been used to automate cyber intrusions

**原文链接**: [https://abcnews.com/amp/Politics/open-source-ai-tool-automate-cyber-intrusions-fbi/story](https://abcnews.com/amp/Politics/open-source-ai-tool-automate-cyber-intrusions-fbi/story)

生成摘要时出错

---

## 97. Flipper One – Open Linux Multi-Tool

**原文标题**: Flipper One – Open Linux Multi-Tool

**原文链接**: [https://www.kickstarter.com/projects/flipper-devices/flipper-one](https://www.kickstarter.com/projects/flipper-devices/flipper-one)

生成摘要时出错

---

## 98. Researchers track whole body movement with just a smartwatch

**原文标题**: Researchers track whole body movement with just a smartwatch

**原文链接**: [https://news.cornell.edu/stories/2026/11/researchers-track-whole-body-movement-just-smartwatch](https://news.cornell.edu/stories/2026/11/researchers-track-whole-body-movement-just-smartwatch)

生成摘要时出错

---

## 99. Aristotle Expands into Rust

**原文标题**: Aristotle Expands into Rust

**原文链接**: [https://www.harmonic.fun/news/aristotle-rust-verification/](https://www.harmonic.fun/news/aristotle-rust-verification/)

生成摘要时出错

---

## 100. Grazing sheep in fields with solar arrays

**原文标题**: Grazing sheep in fields with solar arrays

**原文链接**: [https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains](https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains)

生成摘要时出错

---

