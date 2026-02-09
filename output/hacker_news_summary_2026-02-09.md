# Hacker News 热门文章摘要 (2026-02-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 将沃尔玛 3.88 美元的模拟时钟改装为基于 ESP8266 的 Wi-Fi 时钟

**原文标题**: Converting a $3.88 analog clock from Walmart into a ESP8266-based Wi-Fi clock

**原文链接**: [https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock)

本文详细介绍了一个 DIY 项目，将售价仅 3.88 美元的沃尔玛廉价模拟时钟改装为使用 WEMOS D1 Mini (ESP8266) 模块的 Wi-Fi 同步计时器。通过连接网络时间协议 (NTP) 服务器，该时钟可保持高精度，每 15 分钟同步一次，并自动调整夏令时。

**硬件改装**
改装过程包括拆解时钟的石英机芯，并将内部的拉维特（Lavet）步进电机线圈与其原始振荡器断开。随后将两根导线焊接在机芯线圈上，使 ESP8266 能够通过交替的正负电脉冲直接控制指针。硬件的一个关键补充是 Microchip 47L04 EERAM 芯片，用于存储指针的物理位置。由于廉价时钟机芯不提供位置反馈，EERAM 的存在至关重要，它使模块即使在断电后也能“记住”指针位置。

**软件与运行**
ESP8266 运行自定义程序，每秒十次将模拟指针位置与实际 NTP 时间进行比对。
* **如果时钟变慢：** 模块发送双极脉冲以驱动秒针快进，直到与正确时间匹配。
* **如果时钟变快：** 模块暂停运行，直到实际时间追上指针位置。

**用户界面**
首次运行时，ESP8266 会托管一个 Web 设置页面，用户需在此手动输入指针的初始位置。同步完成后，模块会提供一个状态网页，通过文本或使用 SVG/HTML Canvas 的图形化界面实时显示时钟状态。

总的来说，该项目展示了一种巧妙的方法，通过互联网连接和持久性存储，将廉价硬件升级为精密仪器。

---

## 2. 为什么天空是蓝色的？

**原文标题**: Why Is the Sky Blue?

**原文链接**: [https://explainers.blog/posts/why-is-the-sky-blue/](https://explainers.blog/posts/why-is-the-sky-blue/)

本文解释了地球和火星大气颜色的物理原理，将其归纳为光线相互作用的三个不同“范畴”。

**1. 微小气体分子（地球的蓝天）**
地球天空呈蓝色源于**瑞利散射**。氮气和氧气分子的共振频率处于紫外线波段。当可见光频率接近这一共振频率时，散射会变得更加剧烈。因此，蓝光和紫光的散射强度比红光高出十倍，使天空充满了这些色调。我们感知天空为蓝色而非紫色，是因为人类眼睛对蓝色更敏感，且太阳辐射出的紫光较少。**日落**时，光线穿越大气的路径大幅增加，蓝光和绿光被完全散射掉，只剩下未被散射的红色波长到达我们的眼睛。

**2. 巨大液滴（白云）**
云朵呈现白色是因为它们由比气体分子大得多的水滴组成。这些水滴并不会散射特定频率，而是像微小的棱镜一样，向各个方向反射和折射所有波长的光。这种所有可见频率的混合被大脑感知为白色。

**3. 中等尺寸颗粒（火星天空）**
火星的天空呈现红色是因为其中充满了富含铁元素的尘埃。与气体分子不同，这些固体颗粒具有很宽的吸收范围，“贪婪地”吸收蓝光和紫光，同时允许红光穿过并散射。有趣的是，火星的**日落是蓝色的**，因为这些尘埃颗粒呈现出“前向散射”现象，其中蓝光的偏转角度比红光窄得多，从而在落日周围直接形成一圈蓝色光晕。

总之，天空的颜色取决于颗粒大小：微小气体产生蓝色，中等尺寸的尘埃或烟雾产生红色，而巨大液滴则产生白色。

---

## 3. 急刹车事件作为路段事故风险指标

**原文标题**: Hard-braking events as indicators of road segment crash risk

**原文链接**: [https://research.google/blog/hard-braking-events-as-indicators-of-road-segment-crash-risk/](https://research.google/blog/hard-braking-events-as-indicators-of-road-segment-crash-risk/)

谷歌和弗吉尼亚理工大学的研究人员证实，通过 Android Auto 收集的急刹车事件（HBEs）可以作为评估路段碰撞风险的有效“先行”指标。传统上，交通安全评估依赖于警方报告的交通事故统计数据，但这些属于“滞后”指标，往往因数据稀疏且频率较低，难以支持预防性的安全干预措施。

相比之下，急刹车事件（定义为车辆减速度超过 -3m/s² 的情况）提供了高密度的数据信号。通过对加利福尼亚州和弗吉尼亚州十年数据的分析，研究发现，观察到急刹车事件的路段数量是报告交通事故路段的 18 倍。研究人员采用负二项回归模型，证实了急刹车频率与实际事故率之间存在显著的正相关性。即便在控制了交通流量和基础设施变量的情况下，这种关系在包括局部街道、主干道和高速公路在内的各种道路类型中均保持一致。

针对加州一段高速公路汇合处的案例研究展示了该指标的预测能力：该路段的急刹车率比平均水平高出 70 倍，在无需多年事故报告确认危险的情况下，便成功将其标注为高风险异常点。

谷歌研究中心（Google Research）的机动 AI 团队（Mobility AI team）目前正将这些研究成果整合到谷歌地图平台的“道路管理洞察”（Roads Management Insights）中。这使得交通管理部门能够获取汇总、匿名且实时的信息，从而主动识别危险位置。通过利用这些先行指标，相关部门可以在事故发生前实施针对性的工程干预，例如优化信号灯配时或重新设计基础设施，以提升道路安全。

---

## 4. Sleeper Shells：攻击者正在 Ivanti EPMM 中植入潜伏后门

**原文标题**: Sleeper Shells: Attackers Are Planting Dormant Backdoors in Ivanti EPMM

**原文链接**: [https://defusedcyber.com/ivanti-epmm-sleeper-shells-403jsp](https://defusedcyber.com/ivanti-epmm-sleeper-shells-403jsp)

截至2026年2月，一场协同网络攻击活动正利用复杂的“潜伏型 Shell”（sleeper shell）策略针对 Ivanti Endpoint Manager Mobile (EPMM) 发起攻击。通过利用两个严重漏洞——**CVE-2026-1281** 和 **CVE-2026-1340**——攻击者能够绕过身份验证并植入休眠后门。

与立即执行命令的典型“砸抢式”攻击不同，该攻击者向路径 `/mifs/403.jsp` 部署了一个专门的 Java 类加载器（标识为 `base.Info`）。该植入物并非传统的交互式 Webshell，而是一个**内存阶段加载器**，旨在后期接收并执行第二阶段载荷。

**关键技术细节：**
*   **休眠性：** 加载器在被特定 HTTP 参数（`k0f53cf964d387`）触发前一直保持静默状态。
*   **隐蔽性：** 它利用反射机制（`ClassLoader#defineClass`）将载荷直接加载到内存中，不会在物理磁盘上留下任何痕迹。
*   **指纹识别：** 在激活前，它会收集基础的主机环境详情（操作系统、用户和目录），为后续操作员提供环境参考。
*   **攻击手法：** 这种“部署后即撤离”的行为有力地表明了**初始访问经纪人 (IAB)** 的活动特征，即先建立立足点，以便随后出售或移交给其他威胁行为者。

**检测与修复：**
由于该植入物是非交互式的且完全驻留在内存中，检测工作十分困难。失陷指标 (IOC) 包括：对 `/mifs/403.jsp` 的请求、以 `yv66vg`（Java 魔术字节）开头的特定 Base64 字符串，以及 `k0f53cf964d387` 参数的出现。

由于该 Shell 驻留在内存中，Ivanti 管理员不仅必须**应用最新的安全补丁**，还必须**重启受影响的应用服务器**，才能有效地从系统中清除植入物。保持对“静默”指标的警惕至关重要，因为利用漏洞后缺乏即时活动并不意味着攻击失败，而代表这是一场有耐心的潜伏攻击。

---

## 5. JavaScript 的 UEFI 绑定

**原文标题**: UEFI Bindings for JavaScript

**原文链接**: [https://codeberg.org/smnx/promethee](https://codeberg.org/smnx/promethee)

**摘要：Promethee —— 面向 JavaScript 的 UEFI 绑定**

**Promethee** 是一个托管在 Codeberg 上的开源项目，旨在为统一可扩展固件接口（UEFI）提供 JavaScript 绑定。该项目由用户 *smnx* 开发，将 **QuickJS**（一个轻量级、可嵌入的 JavaScript 引擎）直接集成到 UEFI 环境中。

Promethee 的主要目标是让开发者能够使用高级 JavaScript 而非传统的低级 C 语言来编写 UEFI 应用程序、脚本和系统工具。这一转变在预启动环境中实现了更易访问且更现代化的开发工作流。

**核心技术亮点：**

*   **引擎集成：** 通过利用 QuickJS，该项目保持了较小的二进制体积和较低的内存开销，这对于资源受限的系统固件环境至关重要。
*   **UEFI 协议访问：** Promethee 提供了核心 UEFI 服务的绑定，包括 `BootServices` 和 `RuntimeServices`。它允许脚本与 `SimpleTextOutput`（用于控制台交互）和 `GraphicsOutputProtocol`（用于图形渲染）等标准协议进行交互。
*   **简化原型设计：** 该项目支持直接从 EFI Shell 执行 `.js` 文件。这有助于快速开发诊断实用程序、自定义引导加载程序或硬件配置工具的原型，而无需在每次迭代时都使用复杂的 C 语言工具链。
*   **现代语言标准：** 它支持 ES2023 特性，将现代编程范式（如模块和高级语法）引入计算机启动过程的最早阶段。

总之，Promethee 弥合了高级 Web 技术与低级固件开发之间的鸿沟。它为希望利用 JavaScript 的便捷性和灵活性在预操作系统环境中编写脚本的开发者提供了一个功能完善的平台。

---

## 6. 关于生成 C 的思考

**原文标题**: Thoughts on Generating C

**原文链接**: [https://wingolog.org/archives/2026/02/09/six-thoughts-on-generating-c](https://wingolog.org/archives/2026/02/09/six-thoughts-on-generating-c)

In this article, a compiler developer shares six strategies for using C as a target language, arguing that generating C is often safer and more efficient than writing it by hand.

The key practices include:
1.  **Using `static inline` functions:** By employing `always_inline` attributes, developers can eliminate the performance cost of data abstractions and avoid ABI bottlenecks when passing or returning structs by value.
2.  **Avoiding implicit conversions:** To sidestep C’s complex promotion rules, generators should use explicit conversion functions and enable `-Wconversion`.
3.  **Wrapping raw types:** Encapsulating pointers and integers in single-member structs provides type safety and allows the generated code to mirror the source language’s type hierarchy (such as WebAssembly’s subtyping).
4.  **Leveraging `memcpy`:** For unaligned memory accesses, `memcpy` is preferred because modern compilers reliably optimize it into efficient unaligned loads.
5.  **Manual register allocation:** To ensure reliable tail calls (`musttail`) and support multiple return values, the author suggests passing a limited number of arguments in registers and using global variables for the remainder.

While C is a "local optimum" that provides industrial-strength instruction selection and optimization, the author notes three major drawbacks: the lack of stack control (preventing delimited continuations), the inability to implement zero-cost exceptions without toolchain support, and difficult source-level debugging. 

Regarding the choice of C over Rust, the author concludes that unless the source language already uses explicit lifetimes, Rust’s benefits are often offset by its slower compile times and less mature tail-call support. Ultimately, these practices allow a compiler to leverage C’s mature ecosystem while maintaining high-level abstractions.

---

## 7. Show HN: Algorithmically Finding the Longest Line of Sight on Earth

**原文标题**: Show HN: Algorithmically Finding the Longest Line of Sight on Earth

**原文链接**: [https://alltheviews.world](https://alltheviews.world)

生成摘要时出错

---

## 8. It's not you; GitHub is down again

**原文标题**: It's not you; GitHub is down again

**原文链接**: [https://www.githubstatus.com/incidents/54hndjxft5bx](https://www.githubstatus.com/incidents/54hndjxft5bx)

生成摘要时出错

---

## 9. 波哥大的交通默剧演员

**原文标题**: The Traffic Mimes of Bogotá

**原文链接**: [https://www.atlasobscura.com/articles/traffic-mimes-of-colombia](https://www.atlasobscura.com/articles/traffic-mimes-of-colombia)

生成摘要时出错

---

## 10. Medieval Monks Wrote over Ancient Star Catalog – Particle Accel Reveals Original

**原文标题**: Medieval Monks Wrote over Ancient Star Catalog – Particle Accel Reveals Original

**原文链接**: [https://www.smithsonianmag.com/smart-news/medieval-monks-wrote-over-a-copy-of-an-ancient-star-catalog-now-a-particle-accelerator-is-revealing-the-long-lost-original-text-180988123/](https://www.smithsonianmag.com/smart-news/medieval-monks-wrote-over-a-copy-of-an-ancient-star-catalog-now-a-particle-accelerator-is-revealing-the-long-lost-original-text-180988123/)

生成摘要时出错

---

## 11. AT&T, Verizon blocking release of Salt Typhoon security assessment reports

**原文标题**: AT&T, Verizon blocking release of Salt Typhoon security assessment reports

**原文链接**: [https://www.reuters.com/business/media-telecom/senator-says-att-verizon-blocking-release-salt-typhoon-security-assessment-2026-02-03/](https://www.reuters.com/business/media-telecom/senator-says-att-verizon-blocking-release-salt-typhoon-security-assessment-2026-02-03/)

生成摘要时出错

---

## 12. Long-Sought Proof Tames Some of Math's Unruliest Equations

**原文标题**: Long-Sought Proof Tames Some of Math's Unruliest Equations

**原文链接**: [https://www.quantamagazine.org/long-sought-proof-tames-some-of-maths-unruliest-equations-20260206/](https://www.quantamagazine.org/long-sought-proof-tames-some-of-maths-unruliest-equations-20260206/)

生成摘要时出错

---

## 13. Art of Roads in Games

**原文标题**: Art of Roads in Games

**原文链接**: [https://sandboxspirit.com/blog/art-of-roads-in-games/](https://sandboxspirit.com/blog/art-of-roads-in-games/)

生成摘要时出错

---

## 14. Like Game-of-Life, but on Growing Graphs, with WASM and WebGL

**原文标题**: Like Game-of-Life, but on Growing Graphs, with WASM and WebGL

**原文链接**: [https://znah.net/graphs/](https://znah.net/graphs/)

生成摘要时出错

---

## 15. Information Is Beautiful

**原文标题**: Information Is Beautiful

**原文链接**: [https://informationisbeautiful.net/](https://informationisbeautiful.net/)

生成摘要时出错

---

## 16. Vouch

**原文标题**: Vouch

**原文链接**: [https://github.com/mitchellh/vouch](https://github.com/mitchellh/vouch)

生成摘要时出错

---

## 17. Why is Singapore no longer "cool"?

**原文标题**: Why is Singapore no longer "cool"?

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/02/why-is-singapore-no-longer-cool.html](https://marginalrevolution.com/marginalrevolution/2026/02/why-is-singapore-no-longer-cool.html)

生成摘要时出错

---

## 18. Humans peak in midlife: A combined cognitive and personality trait perspective

**原文标题**: Humans peak in midlife: A combined cognitive and personality trait perspective

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S0160289625000649](https://www.sciencedirect.com/science/article/pii/S0160289625000649)

生成摘要时出错

---

## 19. Nobody knows how the whole system works

**原文标题**: Nobody knows how the whole system works

**原文链接**: [https://surfingcomplexity.blog/2026/02/08/nobody-knows-how-the-whole-system-works/](https://surfingcomplexity.blog/2026/02/08/nobody-knows-how-the-whole-system-works/)

生成摘要时出错

---

## 20. Roman industrial hub discovered on banks of River Wear

**原文标题**: Roman industrial hub discovered on banks of River Wear

**原文链接**: [https://www.durham.ac.uk/news-events/latest-news/2026/01/roman-industrial-hub-discovered-on-banks-of-river-wear-/](https://www.durham.ac.uk/news-events/latest-news/2026/01/roman-industrial-hub-discovered-on-banks-of-river-wear-/)

生成摘要时出错

---

## 21. Show HN: Printable Classics – Free printable classic books for hobby bookbinders

**原文标题**: Show HN: Printable Classics – Free printable classic books for hobby bookbinders

**原文链接**: [https://printableclassics.com](https://printableclassics.com)

生成摘要时出错

---

## 22. Show HN: Browse Internet Infrastructure

**原文标题**: Show HN: Browse Internet Infrastructure

**原文链接**: [https://www.wirewiki.com](https://www.wirewiki.com)

生成摘要时出错

---

## 23. Offpunk 3.0

**原文标题**: Offpunk 3.0

**原文链接**: [https://ploum.net/2026-02-09-offpunk3.html](https://ploum.net/2026-02-09-offpunk3.html)

生成摘要时出错

---

## 24. Matrix messaging gaining ground in government IT

**原文标题**: Matrix messaging gaining ground in government IT

**原文链接**: [https://www.theregister.com/2026/02/09/matrix_element_secure_chat/](https://www.theregister.com/2026/02/09/matrix_element_secure_chat/)

生成摘要时出错

---

## 25. GitHub Is Down

**原文标题**: GitHub Is Down

**原文链接**: [https://github.com/](https://github.com/)

生成摘要时出错

---

## 26. LispE: Lisp Interpreter with Pattern Programming and Lazy Evaluation

**原文标题**: LispE: Lisp Interpreter with Pattern Programming and Lazy Evaluation

**原文链接**: [https://github.com/naver/lispe](https://github.com/naver/lispe)

生成摘要时出错

---

## 27. Irish man detained by ICE for 5 months

**原文标题**: Irish man detained by ICE for 5 months

**原文链接**: [https://www.rte.ie/news/ireland/2026/0209/1557514-seamus-culleton/](https://www.rte.ie/news/ireland/2026/0209/1557514-seamus-culleton/)

生成摘要时出错

---

## 28. Every book recommended on the Odd Lots Discord

**原文标题**: Every book recommended on the Odd Lots Discord

**原文链接**: [https://odd-lots-books.netlify.app/](https://odd-lots-books.netlify.app/)

生成摘要时出错

---

## 29. Show HN: A custom font that displays Cistercian numerals using ligatures

**原文标题**: Show HN: A custom font that displays Cistercian numerals using ligatures

**原文链接**: [https://bobbiec.github.io/cistercian-font.html](https://bobbiec.github.io/cistercian-font.html)

生成摘要时出错

---

## 30. Experts Have World Models. LLMs Have Word Models

**原文标题**: Experts Have World Models. LLMs Have Word Models

**原文链接**: [https://www.latent.space/p/adversarial-reasoning](https://www.latent.space/p/adversarial-reasoning)

生成摘要时出错

---

## 31. Show HN: I created a Mars colony RPG based on Kim Stanley Robinson’s Mars books

**原文标题**: Show HN: I created a Mars colony RPG based on Kim Stanley Robinson’s Mars books

**原文链接**: [https://underhillgame.com/](https://underhillgame.com/)

生成摘要时出错

---

## 32. Tessellation Kit (2016)

**原文标题**: Tessellation Kit (2016)

**原文链接**: [https://sciencevsmagic.net/tes/#0.5.0.1.aaaaaaaaa](https://sciencevsmagic.net/tes/#0.5.0.1.aaaaaaaaa)

生成摘要时出错

---

## 33. Show HN: Minimal NIST/OWASP-compliant auth implementation for Cloudflare Workers

**原文标题**: Show HN: Minimal NIST/OWASP-compliant auth implementation for Cloudflare Workers

**原文链接**: [https://github.com/vhscom/private-landing](https://github.com/vhscom/private-landing)

生成摘要时出错

---

## 34. Toma (YC W24) Is Hiring Founding Engineers

**原文标题**: Toma (YC W24) Is Hiring Founding Engineers

**原文链接**: [https://www.ycombinator.com/companies/toma/jobs/oONUnCf-founding-engineer-ai-products](https://www.ycombinator.com/companies/toma/jobs/oONUnCf-founding-engineer-ai-products)

生成摘要时出错

---

## 35. Quartz crystals

**原文标题**: Quartz crystals

**原文链接**: [https://www.pa3fwm.nl/technotes/tn13a.html](https://www.pa3fwm.nl/technotes/tn13a.html)

生成摘要时出错

---

## 36. Apple XNU: Clutch Scheduler

**原文标题**: Apple XNU: Clutch Scheduler

**原文链接**: [https://github.com/apple-oss-distributions/xnu/blob/main/doc/scheduler/sched_clutch_edge.md](https://github.com/apple-oss-distributions/xnu/blob/main/doc/scheduler/sched_clutch_edge.md)

生成摘要时出错

---

## 37. Ice Kid Prisons

**原文标题**: Ice Kid Prisons

**原文链接**: [https://www.propublica.org/article/life-inside-ice-dilley-children](https://www.propublica.org/article/life-inside-ice-dilley-children)

生成摘要时出错

---

## 38. Gen Z first generation since 1800's with lower cognitive performance

**原文标题**: Gen Z first generation since 1800's with lower cognitive performance

**原文链接**: [https://www.commerce.senate.gov/services/files/A19DF2E8-3C69-4193-A676-430CF0C83DC2](https://www.commerce.senate.gov/services/files/A19DF2E8-3C69-4193-A676-430CF0C83DC2)

生成摘要时出错

---

## 39. Zero crashes, zero compromises: inside the HAProxy security audit

**原文标题**: Zero crashes, zero compromises: inside the HAProxy security audit

**原文链接**: [https://www.haproxy.com/blog/haproxy-security-audit-results](https://www.haproxy.com/blog/haproxy-security-audit-results)

生成摘要时出错

---

## 40. More Mac malware from Google search

**原文标题**: More Mac malware from Google search

**原文链接**: [https://eclecticlight.co/2026/01/30/more-malware-from-google-search/](https://eclecticlight.co/2026/01/30/more-malware-from-google-search/)

生成摘要时出错

---

## 41. Custom Firmware for the MZ-RH1 – Ready for Testing

**原文标题**: Custom Firmware for the MZ-RH1 – Ready for Testing

**原文链接**: [https://sir68k.re/posts/rh1-firmware-available/](https://sir68k.re/posts/rh1-firmware-available/)

生成摘要时出错

---

## 42. GitHub Agentic Workflows

**原文标题**: GitHub Agentic Workflows

**原文链接**: [https://github.github.io/gh-aw/](https://github.github.io/gh-aw/)

生成摘要时出错

---

## 43. The Little Bool of Doom (2025)

**原文标题**: The Little Bool of Doom (2025)

**原文链接**: [https://blog.svgames.pl/article/the-little-bool-of-doom](https://blog.svgames.pl/article/the-little-bool-of-doom)

生成摘要时出错

---

## 44. Roundcube Webmail: SVG feImage bypasses image blocking to track email opens

**原文标题**: Roundcube Webmail: SVG feImage bypasses image blocking to track email opens

**原文链接**: [https://nullcathedral.com/posts/2026-02-08-roundcube-svg-feimage-remote-image-bypass/](https://nullcathedral.com/posts/2026-02-08-roundcube-svg-feimage-remote-image-bypass/)

生成摘要时出错

---

## 45. Running Your Own As: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing

**原文标题**: Running Your Own As: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing

**原文链接**: [https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/](https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/)

生成摘要时出错

---

## 46. AI makes the easy part easier and the hard part harder

**原文标题**: AI makes the easy part easier and the hard part harder

**原文链接**: [https://www.blundergoat.com/articles/ai-makes-the-easy-part-easier-and-the-hard-part-harder](https://www.blundergoat.com/articles/ai-makes-the-easy-part-easier-and-the-hard-part-harder)

生成摘要时出错

---

## 47. Reverse Engineering the Prom for the SGI O2

**原文标题**: Reverse Engineering the Prom for the SGI O2

**原文链接**: [https://mattst88.com/blog/2026/02/08/Reverse_Engineering_the_PROM_for_the_SGI_O2/](https://mattst88.com/blog/2026/02/08/Reverse_Engineering_the_PROM_for_the_SGI_O2/)

生成摘要时出错

---

## 48. AI Doesn't Reduce Work–It Intensifies It

**原文标题**: AI Doesn't Reduce Work–It Intensifies It

**原文链接**: [https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)

生成摘要时出错

---

## 49. As AI enters the operating room, reports arise of botched surgeries

**原文标题**: As AI enters the operating room, reports arise of botched surgeries

**原文链接**: [https://www.reuters.com/investigations/ai-enters-operating-room-reports-arise-botched-surgeries-misidentified-body-2026-02-09/](https://www.reuters.com/investigations/ai-enters-operating-room-reports-arise-botched-surgeries-misidentified-body-2026-02-09/)

生成摘要时出错

---

## 50. We mourn our craft

**原文标题**: We mourn our craft

**原文链接**: [https://nolanlawson.com/2026/02/07/we-mourn-our-craft/](https://nolanlawson.com/2026/02/07/we-mourn-our-craft/)

生成摘要时出错

---

## 51. Exploiting signed bootloaders to circumvent UEFI Secure Boot (2019)

**原文标题**: Exploiting signed bootloaders to circumvent UEFI Secure Boot (2019)

**原文链接**: [https://habr.com/en/articles/446238/](https://habr.com/en/articles/446238/)

生成摘要时出错

---

## 52. RFC 3092 – Etymology of “Foo” (2001)

**原文标题**: RFC 3092 – Etymology of “Foo” (2001)

**原文链接**: [https://datatracker.ietf.org/doc/html/rfc3092](https://datatracker.ietf.org/doc/html/rfc3092)

生成摘要时出错

---

## 53. Advogato

**原文标题**: Advogato

**原文链接**: [https://en.wikipedia.org/wiki/Advogato](https://en.wikipedia.org/wiki/Advogato)

生成摘要时出错

---

## 54. Show HN: Slack CLI for Agents

**原文标题**: Show HN: Slack CLI for Agents

**原文链接**: [https://github.com/stablyai/agent-slack](https://github.com/stablyai/agent-slack)

生成摘要时出错

---

## 55. A GTA modder has got the 1997 original working on modern PCs and Steam Deck

**原文标题**: A GTA modder has got the 1997 original working on modern PCs and Steam Deck

**原文链接**: [https://gtaforums.com/topic/986492-grand-theft-auto-ready2play-full-game-windows-version/](https://gtaforums.com/topic/986492-grand-theft-auto-ready2play-full-game-windows-version/)

生成摘要时出错

---

## 56. I put a real-time 3D shader on the Game Boy Color

**原文标题**: I put a real-time 3D shader on the Game Boy Color

**原文链接**: [https://blog.otterstack.com/posts/202512-gbshader/](https://blog.otterstack.com/posts/202512-gbshader/)

生成摘要时出错

---

## 57. Clean Coder: The Dark Path (2017)

**原文标题**: Clean Coder: The Dark Path (2017)

**原文链接**: [https://blog.cleancoder.com/uncle-bob/2017/01/11/TheDarkPath.html](https://blog.cleancoder.com/uncle-bob/2017/01/11/TheDarkPath.html)

生成摘要时出错

---

## 58. Thought-Terminating Cliché

**原文标题**: Thought-Terminating Cliché

**原文链接**: [https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9](https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9)

生成摘要时出错

---

## 59. I write games in C (yes, C) (2016)

**原文标题**: I write games in C (yes, C) (2016)

**原文链接**: [https://jonathanwhiting.com/writing/blog/games_in_c/](https://jonathanwhiting.com/writing/blog/games_in_c/)

生成摘要时出错

---

## 60. Shifts in U.S. Social Media Use, 2020–2024: Decline, Fragmentation, Polarization (2025)

**原文标题**: Shifts in U.S. Social Media Use, 2020–2024: Decline, Fragmentation, Polarization (2025)

**原文链接**: [https://arxiv.org/abs/2510.25417](https://arxiv.org/abs/2510.25417)

生成摘要时出错

---

## 61. Omega-3 is inversely related to risk of early-onset dementia

**原文标题**: Omega-3 is inversely related to risk of early-onset dementia

**原文链接**: [https://pubmed.ncbi.nlm.nih.gov/41506004/](https://pubmed.ncbi.nlm.nih.gov/41506004/)

生成摘要时出错

---

## 62. A tough labor market for white-collar workers has turned recruiting upside down

**原文标题**: A tough labor market for white-collar workers has turned recruiting upside down

**原文链接**: [https://www.wsj.com/lifestyle/careers/job-hunters-are-so-desperate-that-theyre-paying-to-get-recruited-44891ac2](https://www.wsj.com/lifestyle/careers/job-hunters-are-so-desperate-that-theyre-paying-to-get-recruited-44891ac2)

生成摘要时出错

---

## 63. Using light-based computing to tackle complex challenges

**原文标题**: Using light-based computing to tackle complex challenges

**原文链接**: [https://www.queensu.ca/gazette/stories/using-light-based-computing-tackle-complex-challenges](https://www.queensu.ca/gazette/stories/using-light-based-computing-tackle-complex-challenges)

生成摘要时出错

---

## 64. Why E cores make Apple silicon fast

**原文标题**: Why E cores make Apple silicon fast

**原文链接**: [https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/](https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/)

生成摘要时出错

---

## 65. Matchlock – Secures AI agent workloads with a Linux-based sandbox

**原文标题**: Matchlock – Secures AI agent workloads with a Linux-based sandbox

**原文链接**: [https://github.com/jingkaihe/matchlock](https://github.com/jingkaihe/matchlock)

生成摘要时出错

---

## 66. Discord Launches Teen-by-Default Settings Globally

**原文标题**: Discord Launches Teen-by-Default Settings Globally

**原文链接**: [https://discord.com/press-releases/discord-launches-teen-by-default-settings-globally](https://discord.com/press-releases/discord-launches-teen-by-default-settings-globally)

生成摘要时出错

---

## 67. Hong Kong pro-democracy tycoon Jimmy Lai gets 20 years' jail

**原文标题**: Hong Kong pro-democracy tycoon Jimmy Lai gets 20 years' jail

**原文链接**: [https://www.bbc.com/news/articles/c8d5pl34vv0o](https://www.bbc.com/news/articles/c8d5pl34vv0o)

生成摘要时出错

---

## 68. Reverse Engineering Raiders of the Lost Ark for the Atari 2600

**原文标题**: Reverse Engineering Raiders of the Lost Ark for the Atari 2600

**原文链接**: [https://github.com/joshuanwalker/Raiders2600](https://github.com/joshuanwalker/Raiders2600)

生成摘要时出错

---

## 69. Bun v1.3.9

**原文标题**: Bun v1.3.9

**原文链接**: [https://bun.com/blog/bun-v1.3.9](https://bun.com/blog/bun-v1.3.9)

生成摘要时出错

---

## 70. Show HN: Ported the 1999 game Bugdom to the browser and added a bunch of mods

**原文标题**: Show HN: Ported the 1999 game Bugdom to the browser and added a bunch of mods

**原文链接**: [https://reallyeli.com/bugdom/Bugdom.html](https://reallyeli.com/bugdom/Bugdom.html)

生成摘要时出错

---

## 71. OpenClaw is changing my life

**原文标题**: OpenClaw is changing my life

**原文链接**: [https://reorx.com/blog/openclaw-is-changing-my-life/](https://reorx.com/blog/openclaw-is-changing-my-life/)

生成摘要时出错

---

## 72. Ktkit: A Kotlin toolkit for building server applications with Ktor

**原文标题**: Ktkit: A Kotlin toolkit for building server applications with Ktor

**原文链接**: [https://github.com/smyrgeorge/ktkit](https://github.com/smyrgeorge/ktkit)

生成摘要时出错

---

## 73. DoNotNotify is now Open Source

**原文标题**: DoNotNotify is now Open Source

**原文链接**: [https://donotnotify.com/opensource.html](https://donotnotify.com/opensource.html)

生成摘要时出错

---

## 74. ADHD and Methylphenidate Use in Prepubertal Children and Adult BMI and Height

**原文标题**: ADHD and Methylphenidate Use in Prepubertal Children and Adult BMI and Height

**原文链接**: [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2843415](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2843415)

生成摘要时出错

---

## 75. Slop Terrifies Me

**原文标题**: Slop Terrifies Me

**原文链接**: [https://ezhik.jp/ai-slop-terrifies-me/](https://ezhik.jp/ai-slop-terrifies-me/)

生成摘要时出错

---

## 76. Rabbit Ear "Origami": programmable origami in the browser

**原文标题**: Rabbit Ear "Origami": programmable origami in the browser

**原文链接**: [https://rabbitear.org/book/origami.html](https://rabbitear.org/book/origami.html)

生成摘要时出错

---

## 77. TSMC to make advanced AI semiconductors in Japan

**原文标题**: TSMC to make advanced AI semiconductors in Japan

**原文链接**: [https://apnews.com/article/semiconductors-tsmc-japan-taiwan-ai-11256f2bfde73ca23d08331ad138d6d5](https://apnews.com/article/semiconductors-tsmc-japan-taiwan-ai-11256f2bfde73ca23d08331ad138d6d5)

生成摘要时出错

---

## 78. Roger Ebert Reviews "The Shawshank Redemption" (1999)

**原文标题**: Roger Ebert Reviews "The Shawshank Redemption" (1999)

**原文链接**: [https://www.rogerebert.com/reviews/great-movie-the-shawshank-redemption-1994](https://www.rogerebert.com/reviews/great-movie-the-shawshank-redemption-1994)

生成摘要时出错

---

## 79. San Francisco's pro-billionaire march draws dozens

**原文标题**: San Francisco's pro-billionaire march draws dozens

**原文链接**: [https://techcrunch.com/2026/02/08/san-franciscos-pro-billionaire-march-draws-dozens/](https://techcrunch.com/2026/02/08/san-franciscos-pro-billionaire-march-draws-dozens/)

生成摘要时出错

---

## 80. Show HN: Emergent – Artificial life simulation in a single HTML file

**原文标题**: Show HN: Emergent – Artificial life simulation in a single HTML file

**原文链接**: [https://emergent-ivory.vercel.app/](https://emergent-ivory.vercel.app/)

生成摘要时出错

---

## 81. OpenCiv3: Open-source, cross-platform reimagining of Civilization III

**原文标题**: OpenCiv3: Open-source, cross-platform reimagining of Civilization III

**原文链接**: [https://openciv3.org/](https://openciv3.org/)

生成摘要时出错

---

## 82. Stop generating, start thinking

**原文标题**: Stop generating, start thinking

**原文链接**: [https://localghost.dev/blog/stop-generating-start-thinking/](https://localghost.dev/blog/stop-generating-start-thinking/)

生成摘要时出错

---

## 83. Dave Farber has died

**原文标题**: Dave Farber has died

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/TSNPJVFH4DKLINIKSMRIIVNHDG5XKJCM/](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/TSNPJVFH4DKLINIKSMRIIVNHDG5XKJCM/)

生成摘要时出错

---

## 84. Recombinant zoster vaccine is associated with a reduced risk of dementia

**原文标题**: Recombinant zoster vaccine is associated with a reduced risk of dementia

**原文链接**: [https://www.nature.com/articles/s41467-026-69289-0](https://www.nature.com/articles/s41467-026-69289-0)

生成摘要时出错

---

## 85. LibreOffice blasts Microsoft for putting "commercial interests" over everything

**原文标题**: LibreOffice blasts Microsoft for putting "commercial interests" over everything

**原文链接**: [https://www.neowin.net/news/libreoffice-blasts-microsoft-for-putting-commercial-interests-over-everything/](https://www.neowin.net/news/libreoffice-blasts-microsoft-for-putting-commercial-interests-over-everything/)

生成摘要时出错

---

## 86. The first sodium-ion battery EV is a winter range monster

**原文标题**: The first sodium-ion battery EV is a winter range monster

**原文链接**: [https://insideevs.com/news/786509/catl-changan-worlds-first-sodium-ion-battery-ev/](https://insideevs.com/news/786509/catl-changan-worlds-first-sodium-ion-battery-ev/)

生成摘要时出错

---

## 87. The Waymo World Model

**原文标题**: The Waymo World Model

**原文链接**: [https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation)

生成摘要时出错

---

## 88. Claude Opus 4.6

**原文标题**: Claude Opus 4.6

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6)

生成摘要时出错

---

## 89. Never Work with Bad People

**原文标题**: Never Work with Bad People

**原文链接**: [https://arseniy.wtf/writing/bad-people/](https://arseniy.wtf/writing/bad-people/)

生成摘要时出错

---

## 90. Wood Gas Vehicles: Firewood in the Fuel Tank (2010)

**原文标题**: Wood Gas Vehicles: Firewood in the Fuel Tank (2010)

**原文链接**: [https://solar.lowtechmagazine.com/2010/01/wood-gas-vehicles-firewood-in-the-fuel-tank/](https://solar.lowtechmagazine.com/2010/01/wood-gas-vehicles-firewood-in-the-fuel-tank/)

生成摘要时出错

---

## 91. Let's compile Quake like it's 1997

**原文标题**: Let's compile Quake like it's 1997

**原文链接**: [https://fabiensanglard.net/compile_like_1997/index.html](https://fabiensanglard.net/compile_like_1997/index.html)

生成摘要时出错

---

## 92. The Legacy of Daniel Kahneman: A Personal View (2025)

**原文标题**: The Legacy of Daniel Kahneman: A Personal View (2025)

**原文链接**: [https://ejpe.org/journal/article/view/1075/753](https://ejpe.org/journal/article/view/1075/753)

生成摘要时出错

---

## 93. SCOTUS to decide if 1988 video tape privacy law applies to internet uses

**原文标题**: SCOTUS to decide if 1988 video tape privacy law applies to internet uses

**原文链接**: [https://www.jurist.org/news/2026/01/us-supreme-court-to-decide-if-1988-video-tape-privacy-law-applies-to-internet-uses/](https://www.jurist.org/news/2026/01/us-supreme-court-to-decide-if-1988-video-tape-privacy-law-applies-to-internet-uses/)

生成摘要时出错

---

## 94. Billing can be bypassed using a combo of subagents with an agent definition

**原文标题**: Billing can be bypassed using a combo of subagents with an agent definition

**原文链接**: [https://github.com/microsoft/vscode/issues/292452](https://github.com/microsoft/vscode/issues/292452)

生成摘要时出错

---

## 95. Big Tech groups race to fund unprecedented $660B AI spending spree

**原文标题**: Big Tech groups race to fund unprecedented $660B AI spending spree

**原文链接**: [https://www.ft.com/content/d503afd5-1012-40f0-8f9d-620dcb39a9a2](https://www.ft.com/content/d503afd5-1012-40f0-8f9d-620dcb39a9a2)

生成摘要时出错

---

## 96. Curating a Show on My Ineffable Mother, Ursula K. Le Guin

**原文标题**: Curating a Show on My Ineffable Mother, Ursula K. Le Guin

**原文链接**: [https://hyperallergic.com/curating-a-show-on-my-ineffable-mother-ursula-k-le-guin/](https://hyperallergic.com/curating-a-show-on-my-ineffable-mother-ursula-k-le-guin/)

生成摘要时出错

---

## 97. Do Markets Believe in Transformative AI?

**原文标题**: Do Markets Believe in Transformative AI?

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2025/09/do-markets-believe-in-transformative-ai.html](https://marginalrevolution.com/marginalrevolution/2025/09/do-markets-believe-in-transformative-ai.html)

生成摘要时出错

---

## 98. Claude’s C Compiler vs. GCC

**原文标题**: Claude’s C Compiler vs. GCC

**原文链接**: [https://harshanu.space/en/tech/ccc-vs-gcc/](https://harshanu.space/en/tech/ccc-vs-gcc/)

生成摘要时出错

---

## 99. Containers, cloud, blockchain, AI – all the same old BS, says veteran Red Hatter

**原文标题**: Containers, cloud, blockchain, AI – all the same old BS, says veteran Red Hatter

**原文链接**: [https://www.theregister.com/2026/02/08/waves_of_tech_bs/](https://www.theregister.com/2026/02/08/waves_of_tech_bs/)

生成摘要时出错

---

## 100. Self-referential functions and the design of options (2014)

**原文标题**: Self-referential functions and the design of options (2014)

**原文链接**: [https://commandcenter.blogspot.com/2014/01/self-referential-functions-and-design.html](https://commandcenter.blogspot.com/2014/01/self-referential-functions-and-design.html)

生成摘要时出错

---

