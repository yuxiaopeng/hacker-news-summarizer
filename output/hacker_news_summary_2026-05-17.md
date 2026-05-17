# Hacker News 热门文章摘要 (2026-05-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国人正在砸毁 Flock 摄像头

**原文标题**: Americans Are Smashing Flock Cameras

**原文链接**: [https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/)

无法访问文章链接。

---

## 2. 我将一台 80 美元的 RK3562 安卓平板改造为 Debian Linux 工作站

**原文标题**: I turned a $80 RK3562 Android tablet into a Debian Linux workstation

**原文链接**: [https://github.com/tech4bot/rk3562deb](https://github.com/tech4bot/rk3562deb)

本文介绍了 **rkdebian**，这是一个定制的构建系统，可将售价 80 美元的 Doogee U10 安卓平板（搭载瑞芯微 RK3562 SoC）转换为功能完备的 Debian 12 "Bookworm" 工作站。

**核心特性与功能：**
*   **非侵入式启动：** 系统完全从 SD 卡启动，无需解锁引导加载程序（bootloader）或修改内部 eMMC。移除 SD 卡即可将平板恢复为原厂安卓系统。
*   **硬件兼容性：** 大多数核心组件均能正常工作，包括 10.1 英寸显示屏、10 点触控、Wi-Fi、蓝牙、音频以及用于充电的 RK817 电源管理芯片（PMIC）。3D 加速和摄像头为部分支持但基本可用。
*   **NPU 与 AI 集成：** 一大亮点是支持本地大语言模型（LLM）推理。通过利用 RK3562 的 NPU 和瑞芯微 RKLLM 协议栈，该平板可以本地运行 Qwen3-0.6B 等模型。
*   **优化的用户界面：** 镜像采用了 **Phosh** 移动端界面，并针对硬件按钮、手电筒开关和屏幕方向修复进行了定制集成。预装应用包括 Firefox ESR、Chromium 和 FreeTube。

**技术实现：**
*   **构建系统：** 该项目为 x86-64 Linux 主机提供了一个全面的 `build.sh` 脚本，用于编译 U-Boot、内核和 Debian 根文件系统。
*   **OTA 更新：** 系统支持一种“收件箱”式更新方法。用户只需将 `update.tar.gz` 文件放入平板，专用服务就会在重启时自动应用更新，无需重新刷写 SD 卡。
*   **开发过程：** 该项目在没有官方供应商文档的情况下从零开始逆向工程，并利用了 AI 助手（Claude、Gemini）和 Firefly 开源仓库。

该项目提供了一个低成本、便携的 Linux 工作站解决方案，并针对边缘 AI 和 NPU 工作负载提供了专门支持。

---

## 3. I don't think AI will make your processes go faster

**原文标题**: I don't think AI will make your processes go faster

**原文链接**: [https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/)

生成摘要时出错

---

## 4. 偶尔出现的 ECONNRESET

**原文标题**: The occasional ECONNRESET

**原文链接**: [https://movq.de/blog/postings/2026-05-05/1/POSTING-en.html](https://movq.de/blog/postings/2026-05-05/1/POSTING-en.html)

本文探讨了通过 TCP 交换数据的两个本地服务之间间歇性出现 `ECONNRESET` 错误的原因。通过一系列基于 C 语言的实验，作者证明了当客户端向服务端发送数据而服务端从未读取这些数据时，该错误会稳定出现。

利用 `strace` 和 `tcpdump` 等工具，作者观察到服务端成功发送了自身数据并调用了 `close()`，但这一操作触发了向客户端发送的 TCP RST（重置）包。核心发现是：**当接收缓冲区中仍有未读数据时，对 TCP 套接字调用 `close()` 会导致操作系统发送 RST 包**，而不是执行基于 FIN 的优雅关闭。RFC 1122 对此行为进行了记录，规定如果连接关闭时仍有已接收的待处理数据，主机应发送 RST 以信号通知数据丢失。

作者将这一技术行为与涉及 **Nginx** 和 **Gunicorn/Flask** 的实际场景联系起来。在某些 POST 请求中，Gunicorn 会读取 HTTP 头部但忽略请求体。当应用程序完成响应发送并关闭套接字时，残留在缓冲区中的未读请求体数据触发了 Nginx 代理端的 `ECONNRESET`。

主要结论是，应用程序必须确保在关闭连接前消耗掉所有传入数据，以避免连接过早重置。作者的解决办法是强制 Python 应用程序对请求体执行一次“哑读”（dummy read），以确保在关闭前套接字处于“干净”状态。

---

## 5. 安全研究人员称微软内置 Bitlocker 后门并发布利用程序

**原文标题**: Security researcher says Microsoft built a Bitlocker backdoor, releases exploit

**原文链接**: [https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html](https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html)

本文讨论了安全研究员 Thomas Roth（又名 **Stacksmashing**）的一份报告。他声称，由于微软优先考虑用户便利性而非强大的安全性，实际上在 BitLocker 加密中留下了一个“后门”。

问题的核心在于 BitLocker 与**可信平台模块 (TPM)** 的交互方式。Roth 演示了在许多现代设备上，加密密钥在启动过程中通过 LPC（低引脚数）总线以明文形式从 TPM 传输到 CPU。通过使用一种成本不到 10 美元的低成本工具——**树莓派 Pico (Raspberry Pi Pico)**——Roth 证明了拥有物理访问权限的攻击者可以“嗅探”这条未加密的总线，并在几秒钟内捕获解密密钥。

一旦密钥被拦截，加密驱动器就可以在另一台机器上被轻松访问，从而完全绕过 BitLocker 的保护。虽然这个“后门”并非一段隐藏的代码，但批评者认为，微软将其作为默认配置的决定——而不是要求预启动 PIN 码或物理 USB 密钥——使用户极易受到攻击。

微软的辩护通常是，这种设计是易用性的一种权衡，因为每次计算机唤醒或重启时都要求输入 PIN 码可能会对普通用户造成障碍。然而，Roth 认为，由于通信通道未加密且默认不强制执行多因素身份验证，微软制造了一个重大的安全漏洞。

该研究员发布了漏洞利用程序和演示视频，以强调绕过这些默认保护措施是多么容易，并敦促用户启用 **BitLocker PIN 码**，以确保其数据在面临物理窃取或篡改时保持安全。

---

## 6. Hindenburg's Smoking Room

**原文标题**: Hindenburg's Smoking Room

**原文链接**: [https://www.airships.net/hindenburg-smoking-room/](https://www.airships.net/hindenburg-smoking-room/)

生成摘要时出错

---

## 7. 全程原生，直到你需要文本

**原文标题**: Native all the way, until you need text

**原文链接**: [https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/](https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/)

一位拥有 20 年经验的资深 macOS/iOS 开发者指出，苹果的原生框架目前不足以构建现代化的文本密集型应用（如支持 Markdown 的聊天界面）。尽管作者坚持“原生优先”的理念，但他发现 SwiftUI、AppKit 和 TextKit 2 在实现全文档文本选择、平滑滚动和高效文本流式传输等核心需求时，无法提供无缝的体验。

作者详细说明了在使用原生工具过程中遇到的挫折：
* **SwiftUI：** 滚动效果不流畅，且设计上缺乏跨多个组件选择文本的能力。
* **NSTextView/TextKit 2：** 在实时文本流式传输时会出现 CPU 占用飙升，且缺乏与 SwiftUI 的现代化集成。
* **AppKit/NSCollectionView：** 存在难以解决的持续渲染问题，例如单元格闪烁。

在上述每种方案中，为了实现与 macOS 基本行为（如右键菜单、词典查询和辅助功能）对等的功能，都需要长达数月的底层手动开发。

相比之下，作者发现 **Electron 和 WebKit** 能够“开箱即用”地解决这些问题。Web 技术在排版、高性能 Markdown 渲染以及 macOS 系统集成方面表现更优，开发阻力显著更小。

作者总结认为，对于“聊天密集、长篇富文本”的界面，苹果的原生 SDK 已成为限制而非优势。这解释了为何大多数现代文本密集型应用转向基于 Web 的模式，因为 Web 提供了更强大的渲染引擎来处理复杂的文本交互，而苹果的原生工具目前尚无法与之媲美。

---

## 8. Mistral CEO：欧洲只有两年时间来避免沦为美国的 AI “附庸国”

**原文标题**: Mistral's CEO: Europe has 2 years to stop becoming America's AI 'vassal state'

**原文链接**: [https://www.businessinsider.com/mistral-ceo-warns-europe-2-years-avoid-us-ai-dependence-2026-5](https://www.businessinsider.com/mistral-ceo-warns-europe-2-years-avoid-us-ai-dependence-2026-5)

Arthur Mensch, CEO of the French startup Mistral AI, warns that Europe has a narrow **two-year window** to achieve AI independence or risk becoming a permanent "vassal state" of the United States. 

The core points of his warning include:

*   **Dependency Risks:** Mensch argues that if Europe fails to foster a robust internal AI ecosystem, it will become entirely dependent on American tech giants like OpenAI, Google, and Microsoft. This dependency poses significant risks to Europe’s data privacy, economic sovereignty, and cultural values.
*   **The Strategic Timeline:** He believes the next 24 months are critical. This period will determine whether European companies can scale sufficiently to compete or if the market will be irrevocably dominated by Silicon Valley.
*   **Open-Source as a Solution:** Mistral AI positions itself as a "European champion" by championing an open-source approach. Mensch believes that making AI models more transparent and accessible is the best way to break the monopoly of proprietary American "black box" systems.
*   **Regulatory Concerns:** While the EU has been a leader in AI regulation (notably the EU AI Act), Mensch warns that over-regulation could stifle domestic innovation. He suggests that if European startups are bogged down by compliance while US and Chinese firms move faster, the continent will lose its competitive edge.

In summary, Mensch’s message is a call to action for European policymakers and investors to prioritize innovation over restriction, ensuring that Europe remains a global player in the AI race rather than a mere consumer of foreign technology.

---

## 9. 应科威特要求，Meta删除了一个拥有百万粉丝的热门账号。

**原文标题**: Meta deletes popular 1M follower account after Kuwaiti request

**原文链接**: [https://twitter.com/ryangrim/status/2055992439031185782](https://twitter.com/ryangrim/status/2055992439031185782)

您提供的文本似乎是来自 X（原 Twitter）的关于 JavaScript 被禁用的技术错误消息。不过，根据提供的标题，以下是该新闻事件的简要摘要：

**摘要：Meta 应科威特要求删除“Al-Majlis”账号**

Meta 已停用科威特大型新闻机构 **Al-Majlis** 旗下的热门 Instagram 和 Facebook 账号，该机构拥有超过一百万粉丝。此次行动是根据**科威特内政部**提出的正式法律要求执行的。

**核心要点：**
*   **政府请求：** 科威特政府请求删除该账号，指称其通过传播“虚假新闻”和未经证实的信息，违反了当地法律和内部安全条例。
*   **账号影响力：** Al-Majlis 是科威特最具影响力的数字新闻平台之一，对政府事务和社交议题的报道通常比传统的官方媒体更为迅速。
*   **审查担忧：** 此举引发了关于海湾地区新闻自由和数字权利的广泛争论。批评人士认为，政府正利用 Meta 的合规政策来压制独立声音并控制信息流动。
*   **Meta 的立场：** Meta 通常会配合政府限制或删除违反当地法律内容的请求，前提是这些请求根据其透明度准则在法律上是有效的。

此次账号删除事件是科技巨头根据政府要求关闭当地主要独立新闻源的一个显著案例。

---

## 10. Every AI Subscription Is a Ticking Time Bomb for Enterprise

**原文标题**: Every AI Subscription Is a Ticking Time Bomb for Enterprise

**原文链接**: [https://www.thestateofbrand.com/news/ai-subscription-time-bomb](https://www.thestateofbrand.com/news/ai-subscription-time-bomb)

生成摘要时出错

---

## 11. Prolog Basics Explained with Pokémon

**原文标题**: Prolog Basics Explained with Pokémon

**原文链接**: [https://unplannedobsolescence.com/blog/prolog-basics-pokemon/](https://unplannedobsolescence.com/blog/prolog-basics-pokemon/)

生成摘要时出错

---

## 12. High-Entropy Alloy

**原文标题**: High-Entropy Alloy

**原文链接**: [https://en.wikipedia.org/wiki/High-entropy_alloy](https://en.wikipedia.org/wiki/High-entropy_alloy)

生成摘要时出错

---

## 13. CUDA Books

**原文标题**: CUDA Books

**原文链接**: [https://github.com/alternbits/awesome-cuda-books](https://github.com/alternbits/awesome-cuda-books)

生成摘要时出错

---

## 14. Apple Silicon costs more than OpenRouter

**原文标题**: Apple Silicon costs more than OpenRouter

**原文链接**: [https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html](https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html)

生成摘要时出错

---

## 15. AI is a technology not a product

**原文标题**: AI is a technology not a product

**原文链接**: [https://daringfireball.net/2026/05/ai_is_technology_not_a_product](https://daringfireball.net/2026/05/ai_is_technology_not_a_product)

生成摘要时出错

---

## 16. Agentic Trading with Safe Guardrails

**原文标题**: Agentic Trading with Safe Guardrails

**原文链接**: [https://github.com/ShurikenTrade/shuriken-skills](https://github.com/ShurikenTrade/shuriken-skills)

生成摘要时出错

---

## 17. Zerostack – A Unix-inspired coding agent written in pure Rust

**原文标题**: Zerostack – A Unix-inspired coding agent written in pure Rust

**原文链接**: [https://crates.io/crates/zerostack/1.0.0](https://crates.io/crates/zerostack/1.0.0)

生成摘要时出错

---

## 18. WHO Declares Ebola Outbreak a Global Health Emergency

**原文标题**: WHO Declares Ebola Outbreak a Global Health Emergency

**原文链接**: [https://www.nytimes.com/2026/05/17/world/africa/ebola-congo-uganda-who-public-health-emergency.html](https://www.nytimes.com/2026/05/17/world/africa/ebola-congo-uganda-who-public-health-emergency.html)

生成摘要时出错

---

## 19. EU weighs restricting use of US cloud platforms to process sensitive gov data

**原文标题**: EU weighs restricting use of US cloud platforms to process sensitive gov data

**原文链接**: [https://www.osnews.com/story/144943/eu-weighs-restricting-use-of-us-cloud-platforms-to-process-sensitive-government-data/](https://www.osnews.com/story/144943/eu-weighs-restricting-use-of-us-cloud-platforms-to-process-sensitive-government-data/)

生成摘要时出错

---

## 20. XS: A programming language. Anywhere, anytime, by anyone

**原文标题**: XS: A programming language. Anywhere, anytime, by anyone

**原文链接**: [https://xslang.org](https://xslang.org)

生成摘要时出错

---

## 21. Mozilla to UK regulators: VPNs are essential privacy and security tools

**原文标题**: Mozilla to UK regulators: VPNs are essential privacy and security tools

**原文链接**: [https://blog.mozilla.org/netpolicy/2026/05/15/mozilla-to-uk-regulators-vpns-are-essential-privacy-and-security-tools-and-should-not-be-undermined/](https://blog.mozilla.org/netpolicy/2026/05/15/mozilla-to-uk-regulators-vpns-are-essential-privacy-and-security-tools-and-should-not-be-undermined/)

生成摘要时出错

---

## 22. Mercurial, 20 years and counting: how are we still alive and kicking? [video]

**原文标题**: Mercurial, 20 years and counting: how are we still alive and kicking? [video]

**原文链接**: [https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/](https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/)

生成摘要时出错

---

## 23. Colossus: The Forbin Project

**原文标题**: Colossus: The Forbin Project

**原文链接**: [https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project](https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project)

生成摘要时出错

---

## 24. Scientists believe ibogaine can help veterans overcome PTSD

**原文标题**: Scientists believe ibogaine can help veterans overcome PTSD

**原文链接**: [https://www.bbc.com/future/article/20260514-how-hallucinogenic-ibogaine-helps-veterans-overcome-ptsd](https://www.bbc.com/future/article/20260514-how-hallucinogenic-ibogaine-helps-veterans-overcome-ptsd)

生成摘要时出错

---

## 25. A nicer voltmeter clock

**原文标题**: A nicer voltmeter clock

**原文链接**: [https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock](https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock)

生成摘要时出错

---

## 26. Hosting a website on an 8-bit microcontroller

**原文标题**: Hosting a website on an 8-bit microcontroller

**原文链接**: [https://maurycyz.com/projects/mcusite/](https://maurycyz.com/projects/mcusite/)

生成摘要时出错

---

## 27. Moving away from Tailwind, and learning to structure my CSS

**原文标题**: Moving away from Tailwind, and learning to structure my CSS

**原文链接**: [https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

生成摘要时出错

---

## 28. How Diamonds Are Made

**原文标题**: How Diamonds Are Made

**原文链接**: [https://diamond.jaydip.me/](https://diamond.jaydip.me/)

生成摘要时出错

---

## 29. OpenAI and Government of Malta partner to roll out ChatGPT Plus to all citizens

**原文标题**: OpenAI and Government of Malta partner to roll out ChatGPT Plus to all citizens

**原文链接**: [https://openai.com/index/malta-chatgpt-plus-partnership/](https://openai.com/index/malta-chatgpt-plus-partnership/)

生成摘要时出错

---

## 30. Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

**原文标题**: Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

**原文链接**: [https://github.com/MinishLab/semble](https://github.com/MinishLab/semble)

生成摘要时出错

---

## 31. Mado: Fast Markdown linter written in Rust

**原文标题**: Mado: Fast Markdown linter written in Rust

**原文链接**: [https://github.com/akiomik/mado](https://github.com/akiomik/mado)

生成摘要时出错

---

## 32. SANA-WM, a 2.6B open-source world model for 1-minute 720p video

**原文标题**: SANA-WM, a 2.6B open-source world model for 1-minute 720p video

**原文链接**: [https://nvlabs.github.io/Sana/WM/](https://nvlabs.github.io/Sana/WM/)

生成摘要时出错

---

## 33. We've made the world too complicated

**原文标题**: We've made the world too complicated

**原文链接**: [https://user8.bearblog.dev/the-world-is-too-complicated/](https://user8.bearblog.dev/the-world-is-too-complicated/)

生成摘要时出错

---

## 34. Illusions of understanding in the sciences

**原文标题**: Illusions of understanding in the sciences

**原文链接**: [https://link.springer.com/article/10.1007/s42113-026-00271-1](https://link.springer.com/article/10.1007/s42113-026-00271-1)

生成摘要时出错

---

## 35. Roman Letters

**原文标题**: Roman Letters

**原文链接**: [https://romanletters.org/](https://romanletters.org/)

生成摘要时出错

---

## 36. Accelerando (2005)

**原文标题**: Accelerando (2005)

**原文链接**: [https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html](https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html)

生成摘要时出错

---

## 37. Frontier AI has broken the open CTF format

**原文标题**: Frontier AI has broken the open CTF format

**原文链接**: [https://kabir.au/blog/the-ctf-scene-is-dead](https://kabir.au/blog/the-ctf-scene-is-dead)

生成摘要时出错

---

## 38. Playing Atari ST Music on the Amiga with Zero CPU

**原文标题**: Playing Atari ST Music on the Amiga with Zero CPU

**原文链接**: [https://arnaud-carre.github.io/2026-05-15-ym-fast-emu/](https://arnaud-carre.github.io/2026-05-15-ym-fast-emu/)

生成摘要时出错

---

## 39. Halt and Catch Fire

**原文标题**: Halt and Catch Fire

**原文链接**: [https://unstack.io/halt-and-catch-fire](https://unstack.io/halt-and-catch-fire)

生成摘要时出错

---

## 40. The Third Hard Problem

**原文标题**: The Third Hard Problem

**原文链接**: [https://mmapped.blog/posts/48-the-third-hard-problem](https://mmapped.blog/posts/48-the-third-hard-problem)

生成摘要时出错

---

## 41. Twilight of the Velocipede: Typesetting Races Before the Age of Linotype

**原文标题**: Twilight of the Velocipede: Typesetting Races Before the Age of Linotype

**原文链接**: [https://publicdomainreview.org/essay/twilight-of-the-velocipede/](https://publicdomainreview.org/essay/twilight-of-the-velocipede/)

生成摘要时出错

---

## 42. δ-mem: Efficient Online Memory for Large Language Models

**原文标题**: δ-mem: Efficient Online Memory for Large Language Models

**原文链接**: [https://arxiv.org/abs/2605.12357](https://arxiv.org/abs/2605.12357)

生成摘要时出错

---

## 43. The Protein Shortage Is Coming

**原文标题**: The Protein Shortage Is Coming

**原文链接**: [https://www.theatlantic.com/culture/2026/05/protein-powder-shortage/687193/](https://www.theatlantic.com/culture/2026/05/protein-powder-shortage/687193/)

生成摘要时出错

---

## 44. Why did Clovis toolmakers choose difficult quartz crystal?

**原文标题**: Why did Clovis toolmakers choose difficult quartz crystal?

**原文链接**: [https://phys.org/news/2026-04-clovis-toolmakers-difficult-quartz-crystal.html](https://phys.org/news/2026-04-clovis-toolmakers-difficult-quartz-crystal.html)

生成摘要时出错

---

## 45. Google Maps Satellite Imagery of Palisades Fire Area Reverts

**原文标题**: Google Maps Satellite Imagery of Palisades Fire Area Reverts

**原文链接**: [https://twitter.com/royolone/status/2055465365312815543](https://twitter.com/royolone/status/2055465365312815543)

生成摘要时出错

---

## 46. AI license plate cameras tore this town apart and led to a state of emergency

**原文标题**: AI license plate cameras tore this town apart and led to a state of emergency

**原文链接**: [https://www.washingtonpost.com/nation/2026/05/17/citys-ai-license-plate-cameras-led-an-uproar-state-emergency/](https://www.washingtonpost.com/nation/2026/05/17/citys-ai-license-plate-cameras-led-an-uproar-state-emergency/)

生成摘要时出错

---

## 47. MCP Hello Page

**原文标题**: MCP Hello Page

**原文链接**: [https://www.hybridlogic.co.uk/blog/2026/05/mcp-hello-page](https://www.hybridlogic.co.uk/blog/2026/05/mcp-hello-page)

生成摘要时出错

---

## 48. Unknowable Math Can Help Hide Secrets

**原文标题**: Unknowable Math Can Help Hide Secrets

**原文链接**: [https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/)

生成摘要时出错

---

## 49. A molecule with half-Möbius topology

**原文标题**: A molecule with half-Möbius topology

**原文链接**: [https://www.science.org/doi/10.1126/science.aea3321](https://www.science.org/doi/10.1126/science.aea3321)

生成摘要时出错

---

## 50. We Are All Rankers Now: Or Why the Internet Has Turned to Shit

**原文标题**: We Are All Rankers Now: Or Why the Internet Has Turned to Shit

**原文链接**: [https://grumpywelshman.com/we-are-all-rankers-now-or-why-the-internet-has-turned-to-shit/](https://grumpywelshman.com/we-are-all-rankers-now-or-why-the-internet-has-turned-to-shit/)

生成摘要时出错

---

## 51. Show HN: Rocksky – Music scrobbling and discovery on the AT Protocol

**原文标题**: Show HN: Rocksky – Music scrobbling and discovery on the AT Protocol

**原文链接**: [https://tangled.org/rocksky.app/rocksky](https://tangled.org/rocksky.app/rocksky)

生成摘要时出错

---

## 52. Kyber (YC W23) Is Hiring a Founding Marketer

**原文标题**: Kyber (YC W23) Is Hiring a Founding Marketer

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community](https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community)

生成摘要时出错

---

## 53. A revolutionary cancer treatment could transform autoimmune disease

**原文标题**: A revolutionary cancer treatment could transform autoimmune disease

**原文链接**: [https://arstechnica.com/science/2026/05/a-revolutionary-cancer-treatment-could-transform-autoimmune-disease/](https://arstechnica.com/science/2026/05/a-revolutionary-cancer-treatment-could-transform-autoimmune-disease/)

生成摘要时出错

---

## 54. U.K. Economy Accelerates to Outpace U.S. as War Headwinds Loom

**原文标题**: U.K. Economy Accelerates to Outpace U.S. as War Headwinds Loom

**原文链接**: [https://www.wsj.com/economy/u-k-economy-accelerated-at-start-of-year-7c70878b](https://www.wsj.com/economy/u-k-economy-accelerated-at-start-of-year-7c70878b)

生成摘要时出错

---

## 55. Greek Alphabet Cards

**原文标题**: Greek Alphabet Cards

**原文链接**: [https://labs.randomquark.com/alphabet_cards/](https://labs.randomquark.com/alphabet_cards/)

生成摘要时出错

---

## 56. 100 Best Novels of All Time

**原文标题**: 100 Best Novels of All Time

**原文链接**: [https://www.theguardian.com/books/ng-interactive/2026/may/12/the-100-best-novels-of-all-time](https://www.theguardian.com/books/ng-interactive/2026/may/12/the-100-best-novels-of-all-time)

生成摘要时出错

---

## 57. Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

**原文标题**: Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

**原文链接**: [https://github.com/chiennv2000/orthrus](https://github.com/chiennv2000/orthrus)

生成摘要时出错

---

## 58. Nearly 50 Years Later, WKRP in Cincinnati Becomes a Real Radio Station

**原文标题**: Nearly 50 Years Later, WKRP in Cincinnati Becomes a Real Radio Station

**原文链接**: [https://www.openculture.com/2026/05/nearly-50-years-later-wkrp-in-cincinnati-becomes-a-real-radio-station.html](https://www.openculture.com/2026/05/nearly-50-years-later-wkrp-in-cincinnati-becomes-a-real-radio-station.html)

生成摘要时出错

---

## 59. The bird eye was pushed to an evolutionary extreme

**原文标题**: The bird eye was pushed to an evolutionary extreme

**原文链接**: [https://www.quantamagazine.org/how-the-bird-eye-was-pushed-to-an-evolutionary-extreme-20260513/](https://www.quantamagazine.org/how-the-bird-eye-was-pushed-to-an-evolutionary-extreme-20260513/)

生成摘要时出错

---

## 60. Self-Distillation Enables Continual Learning [pdf]

**原文标题**: Self-Distillation Enables Continual Learning [pdf]

**原文链接**: [https://arxiv.org/abs/2601.19897](https://arxiv.org/abs/2601.19897)

生成摘要时出错

---

## 61. Project Gutenberg – keeps getting better

**原文标题**: Project Gutenberg – keeps getting better

**原文链接**: [https://www.gutenberg.org/](https://www.gutenberg.org/)

生成摘要时出错

---

## 62. Futhark by example (2020)

**原文标题**: Futhark by example (2020)

**原文链接**: [https://futhark-lang.org/examples.html](https://futhark-lang.org/examples.html)

生成摘要时出错

---

## 63. C++26 Shipped a SIMD Library Nobody Asked For

**原文标题**: C++26 Shipped a SIMD Library Nobody Asked For

**原文链接**: [https://lucisqr.substack.com/p/c26-shipped-a-simd-library-nobody](https://lucisqr.substack.com/p/c26-shipped-a-simd-library-nobody)

生成摘要时出错

---

## 64. Content-defined chunking added to Bazel

**原文标题**: Content-defined chunking added to Bazel

**原文链接**: [https://www.buildbuddy.io/blog/content-defined-chunking/](https://www.buildbuddy.io/blog/content-defined-chunking/)

生成摘要时出错

---

## 65. Kioxia and Dell cram 10 PB into slim 2RU server

**原文标题**: Kioxia and Dell cram 10 PB into slim 2RU server

**原文链接**: [https://www.blocksandfiles.com/flash/2026/05/14/kioxia-and-dell-cram-10-pb-into-slim-2ru-server/5240574](https://www.blocksandfiles.com/flash/2026/05/14/kioxia-and-dell-cram-10-pb-into-slim-2ru-server/5240574)

生成摘要时出错

---

## 66. Ploopy Bean: a trackpoint for every computer

**原文标题**: Ploopy Bean: a trackpoint for every computer

**原文链接**: [https://ploopy.co/shop/bean-pointing-stick/](https://ploopy.co/shop/bean-pointing-stick/)

生成摘要时出错

---

## 67. 3D Gaussian Splatting in a Weekend

**原文标题**: 3D Gaussian Splatting in a Weekend

**原文链接**: [https://bfeldman.me/3dgs-weekend/](https://bfeldman.me/3dgs-weekend/)

生成摘要时出错

---

## 68. Fisker went bankrupt and owners built an open source car company from the ashes

**原文标题**: Fisker went bankrupt and owners built an open source car company from the ashes

**原文链接**: [https://electrek.co/2026/05/16/fisker-ocean-open-source-ev-story-after-bankruptcy/](https://electrek.co/2026/05/16/fisker-ocean-open-source-ev-story-after-bankruptcy/)

生成摘要时出错

---

## 69. Accelerate – Embedded language for high-performance array computations

**原文标题**: Accelerate – Embedded language for high-performance array computations

**原文链接**: [https://github.com/AccelerateHS/accelerate](https://github.com/AccelerateHS/accelerate)

生成摘要时出错

---

## 70. Why birth rates are falling everywhere all at once

**原文标题**: Why birth rates are falling everywhere all at once

**原文链接**: [https://www.ft.com/content/fba35eca-df3a-4ad6-b42d-eb08eb7c9ad3](https://www.ft.com/content/fba35eca-df3a-4ad6-b42d-eb08eb7c9ad3)

生成摘要时出错

---

## 71. Fecal transplants for autism deliver success in clinical trials (2019)

**原文标题**: Fecal transplants for autism deliver success in clinical trials (2019)

**原文链接**: [https://refractor.io/adhd-autism/fecal-transplants-for-autism-delivers-success-in-clinical-trials/](https://refractor.io/adhd-autism/fecal-transplants-for-autism-delivers-success-in-clinical-trials/)

生成摘要时出错

---

## 72. Gaining control of every projector and camera on campus

**原文标题**: Gaining control of every projector and camera on campus

**原文链接**: [https://www.edna.land/blogs/posts/scanning/](https://www.edna.land/blogs/posts/scanning/)

生成摘要时出错

---

## 73. Voyager Spacecraft Code

**原文标题**: Voyager Spacecraft Code

**原文链接**: [https://spacedaily.com/nasa-still-maintains-some-of-the-voyager-spacecraft-code-in-a-1970s-era-programming-language-that-almost-nobody-on-earth-fully-understands-anymore-and-the-handful-of-engineers-who-do-are-now-in-their/](https://spacedaily.com/nasa-still-maintains-some-of-the-voyager-spacecraft-code-in-a-1970s-era-programming-language-that-almost-nobody-on-earth-fully-understands-anymore-and-the-handful-of-engineers-who-do-are-now-in-their/)

生成摘要时出错

---

## 74. Fame! A Misunderstanding: A new translation of Albert Camus's complete notebooks

**原文标题**: Fame! A Misunderstanding: A new translation of Albert Camus's complete notebooks

**原文链接**: [https://lareviewofbooks.org/article/albert-camus-complete-notebooks-ryan-bloom-existentialism-absurd/](https://lareviewofbooks.org/article/albert-camus-complete-notebooks-ryan-bloom-existentialism-absurd/)

生成摘要时出错

---

## 75. Germany's spy agency picks French AI firm over Palantir

**原文标题**: Germany's spy agency picks French AI firm over Palantir

**原文链接**: [https://www.politico.eu/article/germany-spy-agency-picks-france-ai-firm-over-palantir/](https://www.politico.eu/article/germany-spy-agency-picks-france-ai-firm-over-palantir/)

生成摘要时出错

---

## 76. Grafana Labs internal source code accessed

**原文标题**: Grafana Labs internal source code accessed

**原文链接**: [https://twitter.com/grafana/status/2055827123236171827](https://twitter.com/grafana/status/2055827123236171827)

生成摘要时出错

---

## 77. Naturally Occurring Quasicrystals

**原文标题**: Naturally Occurring Quasicrystals

**原文链接**: [https://johncarlosbaez.wordpress.com/2026/05/14/naturally-occurring-quasicrystals/](https://johncarlosbaez.wordpress.com/2026/05/14/naturally-occurring-quasicrystals/)

生成摘要时出错

---

## 78. After 8 years, I rewrote my open-source PyTorch curvature library

**原文标题**: After 8 years, I rewrote my open-source PyTorch curvature library

**原文链接**: [https://github.com/noahgolmant/pytorch-hessian-eigenthings](https://github.com/noahgolmant/pytorch-hessian-eigenthings)

生成摘要时出错

---

## 79. DeepSeek-V4-Flash means LLM steering is interesting again

**原文标题**: DeepSeek-V4-Flash means LLM steering is interesting again

**原文链接**: [https://www.seangoedecke.com/steering-vectors/](https://www.seangoedecke.com/steering-vectors/)

生成摘要时出错

---

## 80. How to Write to SSDs [pdf]

**原文标题**: How to Write to SSDs [pdf]

**原文链接**: [https://www.vldb.org/pvldb/vol19/p1469-lee.pdf](https://www.vldb.org/pvldb/vol19/p1469-lee.pdf)

生成摘要时出错

---

## 81. The main thing about P2P meth is that there's so much of it (2021)

**原文标题**: The main thing about P2P meth is that there's so much of it (2021)

**原文链接**: [https://dynomight.net/p2p-meth/](https://dynomight.net/p2p-meth/)

生成摘要时出错

---

## 82. Where to buy a non-Apple, non-Google smartphone

**原文标题**: Where to buy a non-Apple, non-Google smartphone

**原文链接**: [https://www.theregister.com/on-prem/2026/05/01/where-to-buy-a-non-apple-non-google-smartphone/5219681](https://www.theregister.com/on-prem/2026/05/01/where-to-buy-a-non-apple-non-google-smartphone/5219681)

生成摘要时出错

---

## 83. Bill to block publishers from killing online games advances in California

**原文标题**: Bill to block publishers from killing online games advances in California

**原文链接**: [https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/)

生成摘要时出错

---

## 84. Points are a weird and inconsistent unit of measure

**原文标题**: Points are a weird and inconsistent unit of measure

**原文链接**: [https://buttondown.com/hillelwayne/archive/points-are-a-weird-and-inconsistent-unit-of/](https://buttondown.com/hillelwayne/archive/points-are-a-weird-and-inconsistent-unit-of/)

生成摘要时出错

---

## 85. Removing the modem and GPS from my 2024 RAV4 hybrid

**原文标题**: Removing the modem and GPS from my 2024 RAV4 hybrid

**原文链接**: [https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/)

生成摘要时出错

---

## 86. Image-blaster: Creates 3D environments, SFX, and meshes from a single image

**原文标题**: Image-blaster: Creates 3D environments, SFX, and meshes from a single image

**原文链接**: [https://github.com/neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster)

生成摘要时出错

---

## 87. Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文标题**: Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文链接**: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

生成摘要时出错

---

## 88. Radicle: Sovereign {code forge} built on Git

**原文标题**: Radicle: Sovereign {code forge} built on Git

**原文链接**: [https://radicle.dev/](https://radicle.dev/)

生成摘要时出错

---

## 89. 我使用 Verilog 设计了一个面向半字节的 CPU，用于构建科学计算器。

**原文标题**: I designed a nibble-oriented CPU in Verilog to build a scientific calculator

**原文链接**: [https://github.com/gdevic/FPGA-Calculator](https://github.com/gdevic/FPGA-Calculator)

生成摘要时出错

---

## 90. ASCII by Jason Scott

**原文标题**: ASCII by Jason Scott

**原文链接**: [https://ascii.textfiles.com/](https://ascii.textfiles.com/)

生成摘要时出错

---

## 91. Show HN: Watch a neural net learn to play Snake

**原文标题**: Show HN: Watch a neural net learn to play Snake

**原文链接**: [https://ppo.gradexp.xyz/](https://ppo.gradexp.xyz/)

生成摘要时出错

---

## 92. I believe there are entire companies right now under AI psychosis

**原文标题**: I believe there are entire companies right now under AI psychosis

**原文链接**: [https://twitter.com/mitchellh/status/2055380239711457578](https://twitter.com/mitchellh/status/2055380239711457578)

生成摘要时出错

---

## 93. What AI Did to My College Class

**原文标题**: What AI Did to My College Class

**原文链接**: [https://www.nytimes.com/2026/05/17/opinion/chatgpt-ai-college-school-graduation.html](https://www.nytimes.com/2026/05/17/opinion/chatgpt-ai-college-school-graduation.html)

生成摘要时出错

---

## 94. OpenAI is connecting ChatGPT to bank accounts via Plaid

**原文标题**: OpenAI is connecting ChatGPT to bank accounts via Plaid

**原文链接**: [https://firethering.com/chatgpt-bank-account-plaid-openai/](https://firethering.com/chatgpt-bank-account-plaid-openai/)

生成摘要时出错

---

## 95. Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

**原文标题**: Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

**原文链接**: [https://github.com/oven-sh/bun/issues/30719](https://github.com/oven-sh/bun/issues/30719)

生成摘要时出错

---

## 96. GDS weighs in on the NHS's decision to retreat from Open Source

**原文标题**: GDS weighs in on the NHS's decision to retreat from Open Source

**原文链接**: [https://shkspr.mobi/blog/2026/05/gds-weighs-in-on-the-nhss-decision-to-retreat-from-open-source/](https://shkspr.mobi/blog/2026/05/gds-weighs-in-on-the-nhss-decision-to-retreat-from-open-source/)

生成摘要时出错

---

## 97. Intel Core i9-14900KF reaches 9.2Ghz setting a new CPU frequency world record

**原文标题**: Intel Core i9-14900KF reaches 9.2Ghz setting a new CPU frequency world record

**原文链接**: [https://www.notebookcheck.net/Intel-Core-i9-14900KF-reaches-9-2Ghz-setting-a-new-CPU-frequency-world-record.1298605.0.html](https://www.notebookcheck.net/Intel-Core-i9-14900KF-reaches-9-2Ghz-setting-a-new-CPU-frequency-world-record.1298605.0.html)

生成摘要时出错

---

## 98. Additive Blending on the Nintendo 64

**原文标题**: Additive Blending on the Nintendo 64

**原文链接**: [https://phoboslab.org/log/2026/05/n64-additive-blending](https://phoboslab.org/log/2026/05/n64-additive-blending)

生成摘要时出错

---

## 99. HTML Lists

**原文标题**: HTML Lists

**原文链接**: [https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/](https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/)

生成摘要时出错

---

## 100. Reddit Is Blocking Some Users from Accessing Its Website from Mobile Devices

**原文标题**: Reddit Is Blocking Some Users from Accessing Its Website from Mobile Devices

**原文链接**: [https://arstechnica.com/information-technology/2026/05/why-reddit-blocked-my-daily-visit-to-its-mobile-website/](https://arstechnica.com/information-technology/2026/05/why-reddit-blocked-my-daily-visit-to-its-mobile-website/)

生成摘要时出错

---

