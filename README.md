# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-17.md)

*最后自动更新时间: 2026-05-17 18:24:05*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 2 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 3 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 4 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 5 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 6 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 7 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 8 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 9 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 10 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 11 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 12 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 13 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 14 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 15 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 16 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 17 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 18 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 19 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 20 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 21 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 22 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 23 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 24 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 25 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 26 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 27 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 28 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 29 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 30 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 31 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 32 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 33 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 34 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 35 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 36 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 37 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 38 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 39 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 40 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 41 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 42 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 43 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 44 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 45 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 46 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 47 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 48 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 49 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 50 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 51 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 52 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 53 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 54 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 55 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 56 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 57 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 58 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 59 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 60 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 61 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 62 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 63 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 64 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 65 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 66 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 67 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 68 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 69 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 70 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 71 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 72 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 73 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 74 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 75 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 76 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 77 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 78 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 79 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 80 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 81 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 82 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 83 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 84 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 85 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 86 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 87 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 88 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 89 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 90 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 91 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 92 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 93 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 94 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 95 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 96 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 97 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 98 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 99 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 100 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 101 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 102 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 103 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 104 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 105 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 106 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 107 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 108 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 109 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 110 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 111 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 112 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 113 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 114 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 115 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 116 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 117 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 118 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 119 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 120 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 121 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 122 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 123 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 124 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 125 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 126 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 127 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 128 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 129 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 130 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 131 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 132 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 133 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 134 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 135 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 136 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 137 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 138 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 139 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 140 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 141 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 142 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 143 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 144 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 145 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 146 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 147 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 148 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 149 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 150 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 151 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 152 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 153 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 154 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 155 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 156 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 157 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 158 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 159 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 160 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 161 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 162 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 163 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 164 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 165 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 166 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 167 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 168 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 169 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 170 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 171 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 172 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 173 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 174 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 175 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 176 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 177 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 178 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 179 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 180 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 181 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 182 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 183 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 184 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 185 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 186 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 187 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 188 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 189 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 190 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 191 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 192 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 193 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 194 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 195 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 196 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 197 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 198 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 199 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 200 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 201 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 202 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 203 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 204 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 205 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 206 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 207 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 208 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 209 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 210 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 211 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 212 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 213 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 214 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 215 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 216 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 217 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 218 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 219 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 220 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 221 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 222 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 223 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 224 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 225 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 226 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 227 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 228 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 229 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 230 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 231 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 232 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 233 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 234 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 235 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 236 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 237 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 238 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 239 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 240 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 241 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 242 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 243 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 244 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 245 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 246 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 247 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 248 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 249 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 250 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 251 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 252 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 253 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 254 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 255 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 256 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 257 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 258 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 259 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 260 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 261 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 262 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 263 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 264 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 265 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 266 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 267 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 268 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 269 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 270 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 271 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 272 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 273 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 274 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 275 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 276 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 277 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 278 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 279 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 280 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 281 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 282 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 283 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 284 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 285 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 286 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 287 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 288 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 289 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 290 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 291 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 292 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 293 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 294 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 295 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 296 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 297 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 298 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 299 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 300 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 301 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 302 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 303 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 304 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 305 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 306 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 307 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 308 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 309 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 310 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 311 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 312 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 313 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 314 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 315 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 316 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 317 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 318 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 319 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 320 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 321 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 322 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 323 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 324 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 325 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 326 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 327 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 328 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 329 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 330 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 331 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 332 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 333 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 334 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 335 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 336 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 337 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 338 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 339 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 340 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 341 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 342 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 343 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 344 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 345 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 346 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 347 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 348 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 349 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 350 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 351 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 352 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 353 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 354 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 355 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 356 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 357 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 358 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 359 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 360 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 361 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 362 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 363 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 364 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 365 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 366 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 367 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 368 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 369 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 370 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 371 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 372 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 373 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 374 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 375 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 376 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 377 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 378 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 379 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 380 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 381 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 382 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 383 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 384 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 385 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 386 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 387 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 388 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 389 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 390 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 391 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 392 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 393 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 394 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 395 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 396 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 397 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 398 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 399 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 400 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 401 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 402 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 403 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 404 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 405 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 406 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 407 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 408 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 409 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 410 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 411 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 412 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 413 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 414 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 415 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 416 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 417 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 418 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 419 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 420 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 421 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 422 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 423 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
