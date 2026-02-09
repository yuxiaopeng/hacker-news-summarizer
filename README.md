# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-09.md)

*最后自动更新时间: 2026-02-09 18:19:26*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 2 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 3 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 4 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 5 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 6 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 7 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 8 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 9 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 10 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 11 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 12 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 13 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 14 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 15 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 16 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 17 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 18 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 19 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 20 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 21 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 22 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 23 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 24 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 25 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 26 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 27 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 28 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 29 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 30 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 31 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 32 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 33 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 34 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 35 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 36 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 37 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 38 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 39 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 40 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 41 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 42 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 43 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 44 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 45 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 46 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 47 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 48 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 49 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 50 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 51 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 52 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 53 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 54 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 55 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 56 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 57 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 58 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 59 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 60 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 61 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 62 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 63 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 64 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 65 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 66 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 67 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 68 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 69 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 70 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 71 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 72 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 73 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 74 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 75 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 76 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 77 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 78 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 79 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 80 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 81 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 82 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 83 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 84 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 85 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 86 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 87 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 88 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 89 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 90 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 91 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 92 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 93 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 94 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 95 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 96 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 97 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 98 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 99 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 100 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 101 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 102 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 103 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 104 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 105 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 106 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 107 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 108 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 109 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 110 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 111 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 112 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 113 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 114 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 115 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 116 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 117 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 118 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 119 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 120 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 121 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 122 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 123 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 124 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 125 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 126 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 127 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 128 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 129 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 130 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 131 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 132 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 133 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 134 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 135 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 136 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 137 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 138 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 139 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 140 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 141 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 142 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 143 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 144 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 145 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 146 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 147 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 148 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 149 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 150 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 151 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 152 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 153 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 154 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 155 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 156 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 157 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 158 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 159 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 160 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 161 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 162 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 163 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 164 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 165 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 166 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 167 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 168 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 169 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 170 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 171 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 172 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 173 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 174 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 175 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 176 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 177 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 178 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 179 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 180 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 181 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 182 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 183 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 184 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 185 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 186 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 187 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 188 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 189 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 190 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 191 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 192 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 193 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 194 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 195 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 196 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 197 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 198 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 199 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 200 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 201 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 202 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 203 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 204 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 205 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 206 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 207 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 208 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 209 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 210 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 211 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 212 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 213 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 214 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 215 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 216 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 217 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 218 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 219 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 220 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 221 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 222 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 223 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 224 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 225 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 226 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 227 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 228 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 229 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 230 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 231 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 232 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 233 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 234 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 235 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 236 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 237 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 238 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 239 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 240 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 241 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 242 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 243 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 244 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 245 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 246 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 247 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 248 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 249 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 250 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 251 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 252 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 253 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 254 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 255 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 256 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 257 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 258 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 259 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 260 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 261 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 262 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 263 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 264 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 265 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 266 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 267 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 268 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 269 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 270 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 271 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 272 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 273 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 274 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 275 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 276 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 277 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 278 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 279 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 280 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 281 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 282 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 283 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 284 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 285 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 286 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 287 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 288 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 289 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 290 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 291 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 292 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 293 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 294 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 295 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 296 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 297 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 298 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 299 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 300 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 301 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 302 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 303 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 304 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 305 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 306 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 307 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 308 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 309 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 310 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 311 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 312 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 313 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 314 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 315 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 316 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 317 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 318 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 319 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 320 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 321 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 322 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 323 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 324 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 325 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 326 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
