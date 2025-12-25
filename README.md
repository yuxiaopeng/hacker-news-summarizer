# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-25.md)

*最后自动更新时间: 2025-12-25 17:47:42*
## 1. Python 3.15 的 Windows x86-64 解释器有望提速 15%

**原文标题**: Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster

**原文链接**: [https://fidget-spinner.github.io/posts/no-longer-sorry.html](https://fidget-spinner.github.io/posts/no-longer-sorry.html)

Ken Jin 报告称，Python 3.15 预计将带来显著的性能提升，具体而言，Windows x86-64 平台上的几何平均加速比达 15%，macOS AArch64 平台上约为 5%。

此次提升的主要驱动力是向“尾调用线程解释器”（tail-call threaded interpreter）的转型。从历史上看，基于 C 语言的解释器使用“switch-case”或“计算跳转”（computed goto）循环。然而，CPython 的解释器循环代码量已增长至超过 12,000 行，这使得现代编译器（如 MSVC 和 Clang）难以处理其优化启发式算法。具体来说，为了避免代码体积进一步膨胀，编译器通常会拒绝在如此庞大的循环中内联细小的基础函数。

通过使用 `musttail` 属性（最近引入 Clang，目前正在 Visual Studio 2026 (MSVC) 中进行实验性支持），每个字节码处理程序都可以编写为独立的函数，并“尾调用”下一个函数。这种结构强制编译器在不增加堆栈的情况下执行调用，从而有效地重置了编译器的启发式算法。结果是，编译器可以再次成功内联辅助函数，从而生成更高效的机器代码。

**关键要点包括：**
*   **性能：** `pyperformance` 基准测试显示，大型库的提速达 15%，某些微基准测试的提速则接近 80%。
*   **协作：** 这一突破是 CPython 开发团队与微软 MSVC 团队合作的结晶。
*   **可用性：** 虽然该功能目前处于实验阶段，且需要使用 Visual Studio 2026 进行源码构建，但团队计划将其纳入 Python 3.15 的正式版本。
*   **应用：** `uv` 包管理器已经在 macOS 上的 Python 3.14 中采用了类似的尾调用优化。

这一变化代表了 Python 解释器编译方式的重大转变，即从单一的庞大循环转向更模块化、对编译器更友好的架构。

---

## 2. 《纽约客》完整档案现已全面数字化

**原文标题**: The entire New Yorker Archive Is Now Fully Digitized

**原文链接**: [https://www.newyorker.com/news/press-room/the-entire-new-yorker-archive-is-now-fully-digitized](https://www.newyorker.com/news/press-room/the-entire-new-yorker-archive-is-now-fully-digitized)

《纽约客》宣布将其全部档案完整数字化，使过去一个世纪的每一期杂志都能在网上查阅。该项目在杂志网站上增加了来自4000多期杂志的10万多篇文章，读者无需再整理成堆的纸质刊物，也无需依赖图书管理员来查找历史文献。

这一数字档案跨越了杂志百年的历史，汇集了诸如约翰·厄普代克、苏珊·桑塔格、豪尔赫·路易斯·博尔赫斯和拉尔夫·艾里森等传奇作者的作品。馆藏规模宏大，包含超过3.1万篇“城中话题”（Talk of the Town）故事、1.4万首诗歌，以及数千篇涵盖无穷话题的“深度报道”（Reporter at Large）和“纪事”（Annals of）系列文章。

为了使海量内容更易于检索，杂志推出了升级版搜索功能，允许用户按日期、作者或关键词进行筛选。值得注意的是，该刊还利用人工智能为文章生成简短摘要，帮助读者解读那些原本可能含义模糊的“经典”标题。

作为杂志百年庆典的一部分，该档案库为浏览封面和目录提供了一个统一的平台。虽然订阅者可以无限访问完整的历史资料库，但杂志也鼓励所有读者去探索其在小说、诗歌和报道领域积累的深厚历史。

---

## 3. 阿尔茨海默病可在动物身上逆转，并实现完全的神经功能恢复。

**原文标题**: Alzheimer's can be reversed to achieve full neurological recovery in animals

**原文链接**: [https://case.edu/news/new-study-shows-alzheimers-disease-can-be-reversed-achieve-full-neurological-recovery-not-just-prevented-or-slowed-animal-models](https://case.edu/news/new-study-shows-alzheimers-disease-can-be-reversed-achieve-full-neurological-recovery-not-just-prevented-or-slowed-animal-models)

凯斯西储大学、大学医院（University Hospitals）以及克利夫兰退伍军人事务部（Cleveland VA）的研究人员在《细胞报告医学》（Cell Reports Medicine）上发表了一项研究，挑战了长期以来认为阿尔茨海默病（AD）不可逆转的传统观点。该研究表明，即使在疾病显著进展后，通过恢复大脑的能量平衡，也能在动物模型中实现神经功能的完全恢复。

研究指出，关键细胞能量分子 NAD+ 的下降是阿尔茨海默病的主要驱动因素。虽然 NAD+ 水平会随年龄增长自然下降，但研究团队发现，在人类 AD 患者大脑和模型小鼠中，这种下降程度要严重得多。通过施用一种名为 P7C3-A20 的药物，研究人员成功恢复了患有晚期 AD 病理小鼠的 NAD+ 平衡。

实验结果意义重大：同时具有淀粉样蛋白和 Tau 蛋白突变的小鼠表现出脑损伤的逆转，且认知功能完全恢复。通过对 p-tau 217（一种公认的阿尔茨海默病临床生物标志物）恢复正常指标的检测，进一步证实了这一康复效果。

资深作者安德鲁·A·皮珀（Andrew A. Pieper）强调，这一发现代表了科研范式的转变——即从单纯减缓疾病进展转向潜在的逆转疾病。重要的是，皮珀将他们的方法与非处方 NAD+ 前体进行了区分，后者可能使 NAD+ 达到“超生理”水平，从而可能诱发癌症；而 P7C3-A20 则是帮助细胞在压力下维持适当的能量平衡。

这些发现传递了一个“希望的信号”，即受损的大脑可能具备自我修复的能力。该团队目前正致力于开展人体临床试验，并研究这种能量恢复方法是否可应用于其他神经退行性疾病。

---

## 4. 我在网上卖洋葱

**原文标题**: I Sell Onions on the Internet

**原文链接**: [https://www.deepsouthventures.com/i-sell-onions-on-the-internet/](https://www.deepsouthventures.com/i-sell-onions-on-the-internet/)

在《我在网上卖洋葱》一文中，彼得·阿斯丘（Peter Askew）讲述了他从一名“互联网人”转型为成功利基电商企业主的非凡历程。作为一名域名爱好者，阿斯丘在2014年的一次拍卖中以2200美元买下了 VidaliaOnions.com。受威廉·福克纳（William Faulkner）的启发，他秉持“域名（如同文学角色）应引导自身发展”的哲学，决定模仿 Harry & David 的模式，将该网址转型为一家“农场直达”的宅配服务。

尽管缺乏农业经验，阿斯丘仍主动联系了维达利亚洋葱委员会，并与经验丰富的佐治亚州农民阿里斯·海古德（Aries Haygood）达成合作。海古德负责耕种与包装，阿斯丘则负责数字化基础设施、市场营销和客户服务。这一创业尝试迅速获得了成功：2015年的首个销售季便收获了600多个订单，远超他们50个订单的保守估算。

通过结合数字化与传统营销手段（包括电话订购热线和战略赞助），业务不断壮大。尽管经历了重大挫折——尤其是因包装箱质量问题导致一万美元损失，险些让项目夭折——但阿斯丘坚持了下来。到第五个销售季时，该业务已成为“甜洋葱中的鱼子酱”爱好者们的首选，甚至连竞争对手都会将客户引荐至他的网站。

最后，阿斯丘强调了选择“使命感胜过利润”所带来的满足感。通过将传统农产品与现代数字策略相结合，他从成为“维达利亚洋葱人”中找到了自我实现。这证明了在合适的域名和对客户服务的执着驱动下，即使是最“传统”的行业也能在互联网上焕发生机。

---

## 5. 为什么 FedRAMP 授权与 CMMC 2 级已成为政府承包 AI 的准入门槛

**原文标题**: Why FedRAMP Authorization and CMMC Level 2 Are Now Table Stakes for GovCon AI

**原文链接**: [https://blog.procurementsciences.com/psci_blogs/why-fedramp-authorization-and-cmmc-level-2-are-now-table-stakes-for-govcon-ai](https://blog.procurementsciences.com/psci_blogs/why-fedramp-authorization-and-cmmc-level-2-are-now-table-stakes-for-govcon-ai)

截至2025年12月，FedRAMP授权和CMMC 2级认证已成为服务于政府承包（GovCon）行业的AI平台的必要条件——即“入门门槛”。

文章强调，AI不再是边缘工具，而是已深度融入GovCon的核心工作流程，包括商机挖掘、建议书开发、合规追踪和项目管线管理。由于这些流程涉及定价策略、客户情报和受控非机密信息（CUI）等高度敏感数据，安全性必须成为任何AI解决方案的基础组成部分。

其核心观点是，GovCon团队无法承受使用会损害其安全态势的平台。为了实现负责任且规模化的运营，AI供应商必须达到与承包商自身相同的严苛合规与安全标准。在这种环境下，高级别认证不仅是营销口号，更是处理政府相关敏感数据的基本底线。

---

## 6. Phoenix：一个用 Zig 从零编写的现代化 X 服务器

**原文标题**: Phoenix: A modern X server written from scratch in Zig

**原文链接**: [https://git.dec05eba.com/phoenix/about/](https://git.dec05eba.com/phoenix/about/)

**Phoenix** 是一个使用 **Zig** 编程语言从零开始编写的现代 X server。与 Xorg 不同，它不是一个分支，而是一个独立的实现，旨在为现代硬件提供一个更简单、更安全的替代方案。

**核心特性与目标：**
*   **简洁性：** Phoenix 仅支持过去 20 年间应用程序所需的 X11 协议子集。它专注于现代 Linux 硬件 (DRM/GBM)，并移除了传统的服务器驱动接口。
*   **安全性：** 通过利用 Zig 的安全特性和自动协议解析，Phoenix 旨在防止非法内存行为。它实现了客户端隔离，对屏幕录制等敏感操作需要显式授权，同时提供“伪数据”以保持与受限应用的兼容性。
*   **现代技术：** 该项目解决了 Xorg 长期存在的局限性，提供完善的多显示器支持（独立刷新率和 VRR）、HDR 功能以及内置的混成器以防止屏幕撕裂。
*   **兼容性：** 虽然目前仅以“嵌套”模式运行以供开发，但其目标是通过桥接支持 Wayland 应用，并可作为 Xwayland 的替代方案。

**非目标：**
Phoenix 并不打算在旧系统中取代 Xorg。它明确忽略了诸如间接 GLX、字节序交换客户端以及陈旧的字体操作等过时特性。

**当前状态：**
该项目处于早期阶段，尚不适合日常使用。目前在嵌套于现有 X server 运行时，它可以渲染硬件加速的 GLX、EGL 和 Vulkan 应用程序。开发者指出，与普遍看法相反，编写一个精简的 X server 通常比构建一个完整的 Wayland 合成器生态系统更简单。Phoenix 需要 **Zig 0.14.1** 版本进行构建。

---

## 7. Clearspace (YC W23) Is Hiring a Founding Network Engineer (VPN and Proxy)

**原文标题**: Clearspace (YC W23) Is Hiring a Founding Network Engineer (VPN and Proxy)

**原文链接**: [https://www.ycombinator.com/companies/clearspace/jobs/5LtM86I-founding-network-engineer-at-clearspace](https://www.ycombinator.com/companies/clearspace/jobs/5LtM86I-founding-network-engineer-at-clearspace)

**Clearspace**, a YC W23 startup based in San Francisco, is seeking a **Founding Network Engineer** to lead the development of its VPN and proxy infrastructure. The company’s mission is to combat compulsive phone usage by building an "intentionality layer" for the internet, using AI to filter network traffic based on natural language rules.

**The Role**
The engineer will own the global VPN and first-hop policy proxy, ensuring fast, stable, and privacy-respecting traffic classification. Key responsibilities include building a system that applies human-language rules to real-time traffic and developing region-aware routing strategies to maintain connection stability for mobile users.

**Qualifications**
* **Experience:** 3+ years building high-throughput networking or edge systems (proxies, gateways, L4/L7 traffic, or CDNs).
* **Technical Skills:** Proficiency in **Go** is required (TypeScript is a plus). Candidates must have strong systems engineering fundamentals and the ability to debug across the network stack using packet captures.
* **Domain Knowledge:** While specific IKEv2 expertise isn't required, a deep intuition for networking is essential. Experience with WireGuard, IPsec, DPI, or eBPF is highly valued.
* **Environment:** Candidates must be willing to work onsite in San Francisco.

**Compensation and Impact**
The role offers a salary range of **$170K – $230K** and **0.50% – 1.00% equity**. As a founding member of a lean, five-person team, the engineer will have significant autonomy and direct influence over a product already featured by *Huberman Lab* and the *New York Times*. This position is ideal for those passionate about building sophisticated technology to protect human attention from exploitative digital feeds.

---

## 8. We invited a man into our home at Christmas and he stayed with us for 45 years

**原文标题**: We invited a man into our home at Christmas and he stayed with us for 45 years

**原文链接**: [https://www.bbc.co.uk/news/articles/cdxwllqz1l0o](https://www.bbc.co.uk/news/articles/cdxwllqz1l0o)

生成摘要时出错

---

## 9. Asahi Linux with Sway on the MacBook Air M2

**原文标题**: Asahi Linux with Sway on the MacBook Air M2

**原文链接**: [https://daniel.lawrence.lu/blog/2024-12-01-asahi-linux-with-sway-on-the-macbook-air-m2/](https://daniel.lawrence.lu/blog/2024-12-01-asahi-linux-with-sway-on-the-macbook-air-m2/)

This article details the author’s experience installing and configuring **Asahi Linux** on a **MacBook Air M2** (16GB RAM/256GB SSD). Having previously used various Linux distributions on Intel-based hardware, the author opted for a **Fedora minimal** installation paired with the **Sway** window manager to save space and maintain a keyboard-driven workflow.

**Key Technical Customizations:**
*   **The Notch:** By default, Asahi Linux disables the screen area around the notch. The author re-enabled this using a kernel argument (`apple_dcp.show_notch=1`) and configured a 56px tall black Sway bar at the top of the screen to visually integrate the notch.
*   **Touchpad Mapping:** To prevent the mouse cursor from entering the top bar (which allows for easier clicking of browser tabs at the screen's edge), the author used `map_to_region` to restrict the touchpad’s input area.
*   **System Tweaks:** The author updated `i3status` to correctly track the MacBook’s specific battery path and manually installed ARM64 Debian packages for specialized photography hardware by extracting them directly into the Fedora filesystem.

**Performance and Results:**
The author reports that Asahi Linux is incredibly responsive, noting that the touchpad performance—including two-finger scrolling and inertia—is just as smooth as native macOS. While the battery life does not match macOS's 15-hour claim, the author achieved a respectable **4.5 hours** under heavy workloads (high brightness and frequent code compilation). Overall, the author finds the M2 MacBook Air running Asahi Linux to be a superior daily driver compared to their previous high-end hardware.

---

## 10. Toys with the highest play-time and lowest clean-up-time

**原文标题**: Toys with the highest play-time and lowest clean-up-time

**原文链接**: [https://joannabregan.substack.com/p/toys-with-the-highest-play-time-and](https://joannabregan.substack.com/p/toys-with-the-highest-play-time-and)

In "Toys with the highest play-time and lowest clean-up-time," Joanna Bregan addresses a common parental dilemma: the search for toys that maximize independent play while minimizing the "reset time" required to clean up. She argues that the best toys are those with a high "play-to-clean ratio," emphasizing open-ended items that grow with the child.

Key recommendations include:

*   **Magnetic Tiles (Magna-Tiles/Connetix):** Highlighted as the "gold standard." They offer endless creative possibilities for building but can be cleaned up in seconds because they stack together magnetically.
*   **Audio Players (Yoto/Toniebox):** These provide hours of screen-free entertainment, stories, and music. Since they are controlled by small cards or figurines, they involve virtually no physical mess.
*   **Animal Figurines (Schleich/Holztiger):** Durable and versatile for imaginative play, these are easy to store by simply tossing them into a single bin or basket.
*   **Play Silks:** These take up almost no storage space and can be easily folded, yet they transform into capes, landscapes, or doll blankets.
*   **Activity Pads and Stickers:** These encourage "deep work" and focus. Cleanup is minimal as it mostly involves closing a book or disposing of sticker backings.
*   **The Kitchen Sink:** Bregan notes that simple water play with bubbles and a few plastic containers is one of the highest-engagement activities that results in zero toy clutter.

The article concludes that by prioritizing open-ended, stackable, or "tossable" toys, parents can foster a child's creativity and independence without the exhaustion of a lengthy evening cleanup. The goal is to choose quality over quantity, focusing on items that offer the most "bang for your buck" in terms of time.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 2 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 3 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 4 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 5 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 6 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 7 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 8 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 9 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 10 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 11 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 12 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 13 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 14 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 15 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 16 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 17 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 18 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 19 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 20 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 21 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 22 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 23 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 24 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 25 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 26 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 27 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 28 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 29 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 30 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 31 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 32 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 33 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 34 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 35 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 36 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 37 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 38 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 39 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 40 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 41 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 42 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 43 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 44 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 45 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 46 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 47 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 48 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 49 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 50 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 51 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 52 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 53 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 54 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 55 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 56 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 57 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 58 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 59 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 60 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 61 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 62 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 63 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 64 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 65 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 66 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 67 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 68 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 69 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 70 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 71 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 72 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 73 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 74 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 75 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 76 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 77 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 78 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 79 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 80 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 81 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 82 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 83 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 84 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 85 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 86 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 87 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 88 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 89 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 90 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 91 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 92 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 93 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 94 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 95 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 96 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 97 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 98 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 99 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 100 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 101 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 102 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 103 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 104 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 105 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 106 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 107 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 108 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 109 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 110 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 111 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 112 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 113 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 114 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 115 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 116 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 117 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 118 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 119 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 120 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 121 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 122 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 123 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 124 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 125 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 126 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 127 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 128 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 129 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 130 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 131 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 132 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 133 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 134 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 135 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 136 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 137 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 138 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 139 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 140 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 141 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 142 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 143 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 144 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 145 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 146 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 147 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 148 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 149 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 150 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 151 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 152 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 153 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 154 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 155 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 156 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 157 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 158 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 159 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 160 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 161 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 162 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 163 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 164 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 165 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 166 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 167 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 168 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 169 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 170 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 171 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 172 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 173 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 174 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 175 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 176 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 177 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 178 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 179 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 180 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 181 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 182 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 183 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 184 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 185 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 186 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 187 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 188 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 189 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 190 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 191 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 192 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 193 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 194 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 195 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 196 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 197 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 198 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 199 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 200 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 201 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 202 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 203 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 204 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 205 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 206 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 207 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 208 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 209 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 210 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 211 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 212 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 213 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 214 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 215 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 216 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 217 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 218 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 219 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 220 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 221 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 222 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 223 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 224 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 225 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 226 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 227 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 228 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 229 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 230 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 231 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 232 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 233 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 234 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 235 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 236 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 237 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 238 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 239 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 240 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 241 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 242 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 243 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 244 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 245 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 246 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 247 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 248 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 249 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 250 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 251 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 252 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 253 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 254 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 255 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 256 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 257 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 258 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 259 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 260 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 261 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 262 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 263 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 264 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 265 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 266 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 267 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 268 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 269 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 270 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 271 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 272 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 273 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 274 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 275 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 276 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 277 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 278 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 279 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 280 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
