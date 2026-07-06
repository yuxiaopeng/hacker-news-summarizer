# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-06.md)

*最后自动更新时间: 2026-07-06 19:28:46*
## 1. OpenWrt One – 开源硬件路由器

**原文标题**: OpenWrt One – Open Hardware Router

**原文链接**: [https://openwrt.org/toh/openwrt/one](https://openwrt.org/toh/openwrt/one)

所提供的文本并非文章本身，而是一个名为 **Anubis** 的**安全验证页面**，旨在防止 AI 机器人抓取网站内容。

该文本的核心要点如下：

*   **目的：** 网站使用 Anubis 保护其服务器免受攻击性 AI 抓取的侵害，此类抓取会导致网站崩溃并阻碍合法用户访问资源。
*   **机制：** 它利用基于 Hashcash 模型的**工作量证明 (PoW)** 系统。这需要用户设备提供少量的计算能力——对于个人而言成本微不足道，但对于大规模爬虫来说则是巨大的经济和技术负担。
*   **现状：** 这是一个暂时的“占位”解决方案。开发人员正在研究更先进的浏览器指纹技术（如分析字体渲染）以及一种无需 JavaScript 即可识别无头浏览器的替代方案。
*   **技术

总之，该内容解释了用户面临验证挑战的原因，以及网站实施反机器人措施的技术必要性。

---

## 2. AMD 锐龙 AI Halo – 4000 美元 AI 开发套件

**原文标题**: AMD Ryzen AI Halo – $4k AI Dev Kit

**原文链接**: [https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

AMD Ryzen AI Halo 是一款专为 AI 开发者设计的高性能迷你 PC，售价 3,999.99 美元。它搭载了 Zen 5 架构的 Ryzen AI Max+ 395 处理器（16 核/32 线程），并集成了 Radeon 8060S 显卡（40 个 RDNA 3.5 计算单元）和 XDNA 2 NPU。该系统采用单一硬件配置，配备 128 GB LPDDR5x-8000 统一内存（带宽为 256 GB/s）和 2 TB M.2 SSD。

Halo 的机身尺寸仅为 15 厘米见方、5 厘米高，虽然外形紧凑，但需要一个 240W 的电源适配器。连接性方面，它支持 10 GbE 网口、HDMI 2.1、Wi-Fi 7 以及 USB-C 供电。其散热系统由双涡轮风扇组成，能够稳定维持 120W 的 TDP（峰值可达 140W），但在高负载下噪音较大。

在使用 `llama.cpp` 的性能基准测试中，Halo 证明了其运行 Qwen 35B 和 Gemma 31B 等大语言模型的能力。虽然在受计算量限制的提示词处理（prompt processing）方面，它与苹果的 M2/M3 Ultra 芯片旗鼓相当，但在 Token 生成速度上却显著落后（通常慢 2-3 倍），这归因于 Mac Studio 拥有更优越的内存带宽（高达 819 GB/s，而 Halo 为 256 GB/s）。

Halo 的核心价值在于其“开箱即用”的软件生态系统。它预装了定制的 AMD Linux 发行版（基于 Debian）或 Windows 11 专业版，通过 AMD Ryzen AI 开发者中心提供精选配置和第一方支持。这使其区别于其他使用同款芯片的迷你 PC，将其定位为一款精简的开发套件，专为那些针对 ROCm 或 AMD 硬件优化 AI 模型的开发者打造。

---

## 3. Kani：一款 Rust 模型检查器

**原文标题**: Kani: A Model Checker for Rust

**原文链接**: [https://arxiv.org/abs/2607.01504](https://arxiv.org/abs/2607.01504)

**Kani：面向 Rust 的模型检测器** 介绍了一款旨在验证 Rust 程序安全性和正确性的开源工具。虽然 Rust 的所有权系统确保了“安全”代码中的内存安全，但它无法原生保证 `unsafe` 操作的可靠性、消除运行时恐慌（panics）或确保通用的功能正确性。Kani 通过采用有界模型检测（bounded model checking）填补了这些空白。

该工具通过将 Rust 的中级中间表示（MIR）编译为 CBMC 所使用的位级精确验证引擎来运行。Kani 的一个核心优势是它能够自动检查全面的安全属性，而无需用户进行手动注解。为了从有界缺陷查找迈向完全的形式化验证，Kani 引入了一套强大的规范语言。该语言包含以下特性：
*   **函数和循环合约**
*   **量词**
*   **函数桩（Stubbing）**

论文通过对主流 Rust 项目的案例研究证明了 Kani 的工业可行性。通过利用 Kani 的合约系统，研究人员得以将验证级别从简单的“无恐慌”提升至完全的功能正确性，并由此发现了 6 个此前未知的漏洞。

Kani 专为大规模生产环境构建。目前，它已集成到持续集成（CI）工作流中，尤其是在 Rust 标准库的验证工作中，它在每次代码变更时都能成功处理超过 16,000 个证明桩（proof harnesses）。该工作已被 2026 年 IEEE/ACM 自动化软件工程国际会议（ASE）的工业展示赛道（Industry Showcase Track）接收。

---

## 4. 铝箔 (2021)

**原文标题**: Aluminum foil (2021)

**原文链接**: [https://dernocua.github.io/notes/aluminum-foil.html](https://dernocua.github.io/notes/aluminum-foil.html)

在《铝箔（2021）》一文中，Kragen Javier Sitaker 探讨了标准厨房铝箔的工程特性及其尚未开发的制造潜力。铝箔的厚度通常在 10–30 微米之间，具有极高的长宽比、高反射率和优异的导电性，且成本极低（低于 0.50 美元/平方米）。它在极低温下仍能保持延展性，并可被氧化成无定形蓝宝石，用作绝缘体或耐火材料。

文章的一个核心主题是该材料的加工硬化能力。Sitaker 证明，通过对铝箔进行折叠和分层，可以制造出硬度足以在其他退火铝箔上进行穿孔、压筋或冲压图案的工具。这种“单点渐进成形”（SPIF）技术能够创造出结构超材料和加强几何结构。作者指出，虽然铝箔因其极薄而难以用手指操作，但这些特性使其成为“物质编译器引导自举”（matter compiler bootstrapping）的理想材料。

Sitaker 假设，理论上一平方厘米的铝箔就可以被加工成一台包含 10 万个微型运动部件的机器。虽然铝箔因其电势统一而无法单独构建复杂的电路系统，但通过将其与其他材料层压，或将其作为电解加工（ECM）等先进工艺的基材，可以进一步扩展其用途。文章最后指出，铝箔在微米尺度上结合了低成本与高性能的独特优势，使其在自我复制制造系统和精密工程（如制造太阳能浓缩器或白光全息图）领域具有广阔的应用前景。

---

## 5. 重置 Xbox

**原文标题**: Resetting Xbox

**原文链接**: [https://news.xbox.com/en-us/2026/07/06/resetting-xbox/](https://news.xbox.com/en-us/2026/07/06/resetting-xbox/)

In an internal memo titled "Resetting Xbox," leadership announced the most significant restructure in the brand's history, citing a "hardware crisis" and profit margins significantly lower than industry competitors. To address these challenges, Xbox will reduce its workforce by approximately 3,200 roles through FY27, with 1,600 eliminations occurring immediately.

Key strategic shifts include:

*   **Content Portfolio Reset:** Xbox is divesting several studios to focus on core priorities. Compulsion Games and Double Fine Productions will become independent again, while Ninja Theory and Undead Labs are transitioning to new ownership. Arkane France is also under strategic review. Moving forward, Mojang and King will report directly to leadership.
*   **Platform Simplification:** To increase efficiency, Xbox is flattening its organizational structure, reducing management from 14 layers to a maximum of five. The focus will shift toward "makers" and "player-coaches," alongside a 50% reduction in vendor spending and a streamlined code base.
*   **Operational Unification:** For the first time, Xbox has established a Chief Operating Officer with end-to-end P&L responsibility. Helen Chiang has been promoted to this role to align content, hardware, and services under one operating model. Additionally, long-time executive Dave McCarthy is retiring.

The memo concludes that while the core business has weakened despite investments in Game Pass and multi-platform strategies, these "painful" changes are designed to return Xbox to growth by 2027. The ultimate goal remains to reach over a billion daily players through greater financial discipline and a more focused portfolio.

---

## 6. Road to Elm 1.0

**原文标题**: Road to Elm 1.0

**原文链接**: [https://elm-lang.org/news/faster-builds](https://elm-lang.org/news/faster-builds)

生成摘要时出错

---

## 7. Egypt Is Building a New Nile

**原文标题**: Egypt Is Building a New Nile

**原文链接**: [https://www.theb1m.com/video/egypt-is-building-a-new-nile](https://www.theb1m.com/video/egypt-is-building-a-new-nile)

生成摘要时出错

---

## 8. Real-time map of Great Britain's rail network

**原文标题**: Real-time map of Great Britain's rail network

**原文链接**: [https://www.map.signalbox.io](https://www.map.signalbox.io)

生成摘要时出错

---

## 9. Pros and Cons of Solo Development

**原文标题**: Pros and Cons of Solo Development

**原文链接**: [https://johnjeffers.com/pros-and-cons-of-solo-development/](https://johnjeffers.com/pros-and-cons-of-solo-development/)

生成摘要时出错

---

## 10. I Like Small Keyboards

**原文标题**: I Like Small Keyboards

**原文链接**: [https://samsm.ch/small-keyboards/](https://samsm.ch/small-keyboards/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 2 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 3 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 4 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 5 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 6 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 7 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 8 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 9 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 10 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 11 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 12 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 13 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 14 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 15 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 16 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 17 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 18 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 19 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 20 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 21 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 22 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 23 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 24 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 25 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 26 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 27 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 28 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 29 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 30 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 31 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 32 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 33 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 34 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 35 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 36 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 37 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 38 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 39 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 40 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 41 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 42 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 43 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 44 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 45 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 46 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 47 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 48 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 49 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 50 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 51 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 52 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 53 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 54 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 55 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 56 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 57 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 58 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 59 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 60 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 61 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 62 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 63 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 64 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 65 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 66 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 67 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 68 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 69 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 70 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 71 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 72 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 73 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 74 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 75 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 76 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 77 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 78 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 79 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 80 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 81 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 82 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 83 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 84 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 85 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 86 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 87 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 88 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 89 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 90 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 91 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 92 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 93 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 94 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 95 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 96 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 97 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 98 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 99 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 100 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 101 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 102 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 103 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 104 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 105 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 106 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 107 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 108 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 109 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 110 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 111 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 112 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 113 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 114 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 115 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 116 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 117 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 118 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 119 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 120 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 121 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 122 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 123 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 124 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 125 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 126 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 127 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 128 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 129 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 130 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 131 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 132 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 133 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 134 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 135 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 136 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 137 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 138 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 139 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 140 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 141 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 142 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 143 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 144 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 145 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 146 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 147 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 148 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 149 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 150 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 151 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 152 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 153 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 154 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 155 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 156 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 157 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 158 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 159 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 160 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 161 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 162 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 163 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 164 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 165 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 166 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 167 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 168 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 169 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 170 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 171 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 172 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 173 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 174 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 175 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 176 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 177 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 178 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 179 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 180 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 181 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 182 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 183 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 184 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 185 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 186 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 187 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 188 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 189 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 190 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 191 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 192 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 193 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 194 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 195 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 196 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 197 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 198 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 199 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 200 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 201 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 202 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 203 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 204 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 205 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 206 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 207 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 208 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 209 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 210 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 211 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 212 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 213 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 214 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 215 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 216 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 217 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 218 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 219 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 220 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 221 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 222 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 223 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 224 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 225 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 226 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 227 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 228 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 229 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 230 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 231 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 232 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 233 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 234 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 235 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 236 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 237 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 238 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 239 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 240 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 241 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 242 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 243 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 244 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 245 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 246 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 247 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 248 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 249 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 250 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 251 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 252 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 253 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 254 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 255 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 256 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 257 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 258 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 259 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 260 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 261 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 262 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 263 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 264 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 265 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 266 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 267 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 268 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 269 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 270 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 271 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 272 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 273 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 274 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 275 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 276 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 277 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 278 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 279 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 280 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 281 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 282 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 283 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 284 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 285 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 286 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 287 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 288 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 289 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 290 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 291 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 292 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 293 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 294 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 295 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 296 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 297 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 298 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 299 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 300 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 301 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 302 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 303 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 304 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 305 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 306 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 307 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 308 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 309 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 310 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 311 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 312 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 313 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 314 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 315 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 316 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 317 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 318 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 319 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 320 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 321 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 322 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 323 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 324 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 325 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 326 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 327 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 328 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 329 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 330 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 331 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 332 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 333 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 334 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 335 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 336 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 337 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 338 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 339 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 340 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 341 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 342 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 343 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 344 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 345 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 346 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 347 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 348 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 349 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 350 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 351 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 352 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 353 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 354 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 355 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 356 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 357 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 358 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 359 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 360 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 361 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 362 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 363 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 364 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 365 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 366 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 367 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 368 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 369 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 370 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 371 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 372 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 373 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 374 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 375 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 376 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 377 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 378 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 379 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 380 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 381 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 382 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 383 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 384 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 385 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 386 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 387 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 388 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 389 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 390 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 391 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 392 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 393 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 394 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 395 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 396 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 397 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 398 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 399 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 400 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 401 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 402 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 403 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 404 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 405 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 406 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 407 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 408 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 409 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 410 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 411 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 412 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 413 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 414 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 415 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 416 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 417 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 418 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 419 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 420 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 421 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 422 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 423 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 424 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 425 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 426 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 427 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 428 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 429 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 430 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 431 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 432 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 433 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 434 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 435 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 436 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 437 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 438 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 439 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 440 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 441 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 442 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 443 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 444 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 445 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 446 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 447 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 448 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 449 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 450 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 451 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 452 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 453 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 454 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 455 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 456 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 457 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 458 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 459 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 460 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 461 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 462 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 463 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 464 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 465 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 466 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 467 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 468 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 469 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 470 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 471 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 472 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 473 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
