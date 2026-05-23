# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-23.md)

*最后自动更新时间: 2026-05-23 18:25:40*
## 1. Oura称收到政府索取用户数据的要求。

**原文标题**: Oura says it gets government demands for user data

**原文链接**: [https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/](https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/)

估值110亿美元、拥有超过550万用户的健康科技巨头Oura，因其数据隐私惯例以及在政府调取信息方面缺乏透明度而面临审查。

调查性报道显示，Oura的健康数据并未采用端到端加密。这种安全设计意味着包括心率、睡眠模式、月经周期和地理位置在内的敏感信息可被Oura员工访问；因此，这些信息也可能被政府机构通过搜查令获取，或面临被黑客窃取的风险。

虽然Oura承认曾“偶尔”收到政府调取用户数据的要求，但拒绝披露其配合调取的数量、范围或频率。八个月前，一名发言人曾表示公司正“积极评估”发布透明度报告，以分享此类请求的汇总数据。然而，该公司此后未能落实此项工作，也未回应后续质询。

作者认为，作为拥有雄厚财力的市场领导者，Oura有责任升级其安全架构，并提供与其他主流科技公司同等水平的透明度。若缺乏透明度报告，用户将无法知晓其私密健康数据被移交给当局的频率，这将使公司难以维持长期的客户信任。

---

## 2. 论 <dl>

**原文标题**: On The <dl>

**原文链接**: [https://benmyers.dev/blog/on-the-dl/](https://benmyers.dev/blog/on-the-dl/)

《关于 `<dl>` 标签》一文探讨了 HTML 描述列表元素的多功能性及其在语义上的重要性。`<dl>` 元素主要用于表示“名称-值”对，由三个核心组件构成：`<dl>`（列表容器）、`<dt>`（描述术语）和 `<dd>`（描述详情）。

关键技术点包括：
*   **结构：** 一个 `<dt>` 后面可以跟随多个 `<dd>` 元素，用以表示一个术语的多个对应值。
*   **样式：** 现代 HTML 规范允许开发者将 `<dt>` 和 `<dd>` 组合包裹在 `<div>` 中，以便于布局和样式设置。
*   **演变：** 该标签此前被称为“定义列表”，主要用于术语表；HTML5 将其更名为“描述列表”，以体现其在表示元数据方面更广泛的用途，例如产品详情、住宿设施或类似《龙与地下城》属性面板的复杂数据。

作者强调，虽然通用的 `<div>` 结构在视觉上可以模拟这些列表，但语义化元素提供了至关重要的无障碍优势。屏幕阅读器可以通过程序识别这种模式，让用户能够获知项目总数、追踪在列表中的位置，或者在内容不相关时跳过整个区块。

归根结底，文章认为，相比使用通用容器，使用 `<dl>` 元素能为辅助技术提供“理论上的提升”，确保信息以结构化的方式呈现，从而让设备能够有效地解析并将其传达给所有用户。

---

## 3. 对1980年太空实验室计算机电路的逆向工程

**原文标题**: Reverse engineering circuitry in a Spacelab computer from 1980

**原文链接**: [https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html](https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html)

生成摘要时出错

---

## 4. z386：基于原始微代码构建的开源 80386

**原文标题**: z386: An Open-Source 80386 Built Around Original Microcode

**原文链接**: [https://nand2mario.github.io/posts/2026/z386/](https://nand2mario.github.io/posts/2026/z386/)

**z386** 是一款开源的、基于 FPGA 的 80386 级 CPU，旨在利用提取的原始 Intel 微代码运行。基于作者之前的 z8086 项目，z386 专注于“微架构考古”，通过重建原始机器的内部逻辑结构（包括 32 项 TLB、保护 PLA 和 2,560 项微代码 ROM）而非依赖现代 RTL 仿真来实现。

该 CPU 性能足以引导 DOS 6/7，运行 DOS/4GW 等保护模式软件，并流畅运行《毁灭战士》(Doom) 等要求较高的游戏。在性能方面，z386 的运行频率为 85MHz，表现接近高速 386 或低端 486。虽然其时钟频率高于历史硬件，但其每指令周期数 (CPI) 稍低。与流行的 ao486 FPGA 内核相比，z386 更加精简，仅需 8,000 行代码，占用的 FPGA 资源（ALUT 和 BRAM）也更少。

其架构镜像了原始 Intel 设计，分为八个单元，例如 16 字节预取器、复杂译码器和微代码定序器。译码器利用 PLA 风格的查找表来处理复杂的 x86 指令，而定序器则管理 37 位宽的微代码字。由于 386 的微代码高度密集，并依赖延迟槽进行寄存器回写等操作，即便是简单的指令也至少需要两个时钟周期。

尽管 z386 加入了针对 FPGA 的优化（如用于乘法运算的 DSP 模块和 16KB 一级缓存），但它依然忠实重构了 386 的特定行为，包括分页、保护检查和精确故障。该项目既是研究 32 位 x86 历史的教育资源，也是现代 FPGA 复古计算平台的功能核心。

---

## 5. 80386微代码反汇编

**原文标题**: 80386 Microcode Disassembled

**原文链接**: [https://www.reenigne.org/blog/80386-microcode-disassembled/](https://www.reenigne.org/blog/80386-microcode-disassembled/)

本文详细介绍了英特尔 80386 微代码的协作逆向工程与反汇编过程。由于该芯片极其复杂，这项任务此前被认为几乎不可能完成。团队（包括 GloriousCow 和 Smartest Blob）利用 Ken Shirriff 提供的高分辨率晶圆图像，通过图像处理和神经网络技术提取出了一个 94,720 位的二进制大对象（binary blob），随后将其手动解码为可理解的微操作。

**核心发现：**
*   **架构：** 80386 拥有 215 个微代码入口点，较 8086 的 60 个显著增加。与现代 CPU 不同，80386 的每一条指令都由微代码处理。
*   **硬件加速器：** 8086 的大多数算法直接在微代码中实现，而 80386 的微代码主要用于协调乘法、除法和桶形移位器等专用硬件加速器。
*   **潜在安全漏洞：** 反汇编揭示了一个可能存在了 40 年的 I/O 权限位图处理漏洞。在进行 4 字节端口访问时，微代码似乎只检查前三个地址，这可能导致对最后一个字节的越权访问。
*   **未使用的代码：** 发现了一段神秘的例程（0x849–0x856），其类似于缺页异常处理程序，但缺乏入口点，且与分页单元的交互方式十分奇特。

**历史背景：**
XBTS 和 IBTS 指令的缺失表明该微代码源自 80386 的后期步进版本（B1 之后）。评论者指出，确定具体的“步进”版本至关重要，因为它揭示了在运行期微代码更新时代到来之前，英特尔在历史上是如何处理漏洞和勘误的。

该项目包含对 386 保护模式和内存系统的深度剖析，目前已在 GitHub 上公开供大众研究。

---

## 6. 我的两部分桌面布置

**原文标题**: My two-part desk setup

**原文链接**: [https://arslan.io/2025/11/18/my-two-part-desk-setup/](https://arslan.io/2025/11/18/my-two-part-desk-setup/)

在本文中，作者详细介绍了一次重大的办公空间改造：从传统的、面壁式且以技术为中心的办公桌，转向更开放且具备双重用途的布局。受一次汉堡之旅的启发，作者首先将办公桌旋转为面向房间，从而获得了更好的深度感和开阔的门口视野。

新方案的核心是一张 200x75 厘米的 USM Haller 办公桌，它被划分为两个截然不同的区域：

*   **数字区：** 该区域刻意保持极简风格以促进专注。配备了 Studio Display、Mac 和定制分体式键盘，专门用于编码、写作和通话等需要高度集中的任务。
*   **模拟区：** 该空间专注于脱离屏幕的活动，如写日记、阅读和素描。与数字区不同，这里拥抱一种功能性的“极繁主义”美学，项目可以长期摆放在桌面上。它还可以作为家庭活动的共享空间，例如一起搭建乐高。

作者总结道，这种物理上的划分建立了一道至关重要的心理边界。只需将椅子从一侧滑向另一侧，他们就能切换工作状态，而不会受到电脑的干扰。经过近一年的使用，作者发现这种数字极简主义与模拟创造力之间的平衡，让办公室变得更具吸引力、更安全且功能更多样。

---

## 7. 赚钱的艺术

**原文标题**: The Art of Money Getting

**原文链接**: [https://kk.org/cooltools/book-freak-210-the-art-of-money-getting/](https://kk.org/cooltools/book-freak-210-the-art-of-money-getting/)

Written by legendary showman P.T. Barnum at age 70, *The Art of Money Getting* (1880) distills a lifetime of entrepreneurial highs and lows into twenty practical rules for financial success. Drawing from his experience building museums, circuses, and recovering from bankruptcy, Barnum emphasizes that wealth is a result of character and discipline rather than just luck.

The article highlights four core principles from the book:

1.  **Select the Right Vocation:** Barnum advises individuals to choose work that aligns with their natural talents. Success is difficult when "fighting upstream" in a job that doesn't match one's "knack."
2.  **Avoid Debt:** Described as a "plague" that destroys self-respect and freedom, Barnum insists on keeping expenses below income to maintain independence.
3.  **Commit Fully:** Half-hearted effort is a recipe for poverty. True success requires doing work "with all your might" and leaving no stone unturned.
4.  **Preserve Integrity:** Reputation is a business’s most valuable asset. While dishonesty may provide temporary gains, long-term success is impossible without the trust of others.

The summary concludes with actionable steps, urging readers to audit their career alignment, create a concrete debt-elimination plan, and approach their current tasks with total dedication. Ultimately, Barnum views money as a "terrible master" but an "excellent servant" when managed with wisdom and integrity.

---

## 8. Making Deep Learning Go Brrrr from First Principles

**原文标题**: Making Deep Learning Go Brrrr from First Principles

**原文链接**: [https://horace.io/brrr_intro.html](https://horace.io/brrr_intro.html)

深度学习性能优化常被视为“炼金术”，但本文认为可以通过识别模型所属的三种范畴——**计算 (Compute)**、**内存带宽 (Memory Bandwidth)** 或 **开销 (Overhead)**，以科学的方法进行优化。

**1. 计算 (FLOPS)：**
计算是指 GPU 执行的实际浮点运算。现代加速器专为矩阵乘法 (matmuls) 进行了优化；虽然非矩阵乘法操作（如激活函数或 LayerNorm）仅占总 FLOPs 的极小部分，但其耗时往往不成比例。优化的目标是最大化模型处于“计算受限 (compute-bound)”状态的时间，以充分发挥硬件的算力峰值 (TFLOPS)。

**2. 内存带宽：**
这是在 GPU 内存 (DRAM) 与计算单元之间移动数据所花费的时间。许多操作（如一元函数 `torch.cos`）属于“内存受限 (memory-bound)”，因为移动数据所需的时间超过了实际计算时间。此处主要的优化手段是**算子融合 (operator fusion)**，即将多个操作合并为一个算子内核 (kernel)。这能减少全局内存访问，显著加速逐元素 (pointwise) 操作序列。作者指出，由于这些操作受内存带宽限制，复杂激活函数（如 GELU）的开销通常与简单激活函数（如 ReLU）相当。

**3. 开销 (Overhead)：**
开销包括除此之外的所有内容，例如 Python 解释器执行时间、框架调度（PyTorch 逻辑）和内核启动耗时。由于 GPU 的速度比 Python 快几个数量级，开销可能成为主要瓶颈，尤其是在处理小张量或科学计算工作负载时。

**结论：**
通过第一性原理进行推导，工程师可以避免无效的“技巧”。如果模型受内存带宽限制，增加 GPU 算力 (FLOPS) 并无帮助；反之，如果模型是计算受限的，减少 Python 开销则毫无意义。有效的优化需要识别特定的瓶颈，并利用融合编译器 (NVFuser, XLA) 或自定义内核 (Triton) 等工具来解决。

---

## 9. Hengefinder: Finding When the Sun Aligns with Your Street

**原文标题**: Hengefinder: Finding When the Sun Aligns with Your Street

**原文链接**: [https://victoriaritvo.com/blog/hengefinder/](https://victoriaritvo.com/blog/hengefinder/)

生成摘要时出错

---

## 10. Italy Cancels Boeing Pegasus Order, Shifting to Airbus A330 MRTT

**原文标题**: Italy Cancels Boeing Pegasus Order, Shifting to Airbus A330 MRTT

**原文链接**: [https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

Italy has officially signed a €1.39 billion contract for six Airbus A330 Multi Role Tanker Transport (MRTT) aircraft, marking a significant geopolitical shift in its air defense strategy. The deal, finalized in April 2026, includes long-term logistical support and signals Italy’s definitive abandonment of the American-made Boeing KC-46 Pegasus.

The procurement process was complex, beginning in 2022 with an initial selection of the Boeing platform. However, that program was canceled in 2024, followed by a series of unsuccessful tenders. By late 2025, Airbus emerged as the sole provider meeting Italy’s technical requirements. 

This move is viewed as a strategic decision to bolster the "European pillar" within the NATO framework. While the Airbus aircraft remain fully NATO-compatible, the shift moves the logistical and industrial "center of gravity" away from a US-centric model toward a European ecosystem of maintenance, training, and supply chains. Italy becomes the 19th global operator of the A330 MRTT, a platform that has increasingly outperformed Boeing in international markets due to the latter's technical delays and performance issues.

The new fleet will significantly enhance the Italian Air Force’s power-projection capabilities, providing essential air-to-air refueling for F-35 and Eurofighter Typhoon jets, as well as strategic transport and humanitarian support. Although the contract is signed, specific technical details—such as whether Italy will receive the standard version or the more efficient MRTT+ (based on the A330neo)—and the extent of Italian industrial involvement are still being finalized. Overall, the decision reflects a broader trend of European nations favoring regional industrial solutions to strengthen strategic autonomy.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 2 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 3 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 4 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 5 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 6 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 7 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 8 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 9 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 10 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 11 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 12 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 13 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 14 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 15 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 16 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 17 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 18 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 19 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 20 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 21 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 22 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 23 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 24 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 25 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 26 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 27 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 28 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 29 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 30 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 31 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 32 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 33 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 34 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 35 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 36 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 37 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 38 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 39 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 40 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 41 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 42 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 43 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 44 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 45 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 46 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 47 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 48 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 49 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 50 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 51 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 52 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 53 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 54 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 55 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 56 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 57 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 58 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 59 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 60 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 61 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 62 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 63 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 64 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 65 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 66 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 67 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 68 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 69 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 70 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 71 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 72 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 73 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 74 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 75 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 76 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 77 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 78 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 79 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 80 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 81 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 82 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 83 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 84 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 85 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 86 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 87 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 88 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 89 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 90 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 91 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 92 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 93 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 94 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 95 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 96 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 97 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 98 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 99 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 100 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 101 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 102 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 103 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 104 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 105 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 106 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 107 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 108 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 109 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 110 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 111 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 112 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 113 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 114 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 115 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 116 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 117 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 118 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 119 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 120 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 121 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 122 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 123 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 124 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 125 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 126 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 127 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 128 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 129 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 130 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 131 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 132 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 133 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 134 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 135 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 136 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 137 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 138 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 139 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 140 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 141 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 142 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 143 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 144 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 145 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 146 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 147 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 148 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 149 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 150 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 151 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 152 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 153 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 154 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 155 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 156 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 157 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 158 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 159 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 160 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 161 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 162 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 163 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 164 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 165 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 166 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 167 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 168 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 169 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 170 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 171 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 172 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 173 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 174 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 175 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 176 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 177 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 178 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 179 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 180 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 181 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 182 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 183 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 184 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 185 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 186 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 187 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 188 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 189 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 190 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 191 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 192 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 193 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 194 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 195 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 196 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 197 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 198 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 199 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 200 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 201 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 202 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 203 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 204 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 205 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 206 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 207 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 208 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 209 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 210 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 211 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 212 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 213 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 214 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 215 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 216 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 217 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 218 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 219 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 220 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 221 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 222 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 223 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 224 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 225 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 226 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 227 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 228 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 229 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 230 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 231 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 232 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 233 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 234 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 235 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 236 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 237 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 238 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 239 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 240 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 241 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 242 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 243 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 244 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 245 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 246 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 247 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 248 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 249 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 250 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 251 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 252 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 253 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 254 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 255 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 256 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 257 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 258 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 259 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 260 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 261 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 262 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 263 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 264 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 265 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 266 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 267 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 268 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 269 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 270 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 271 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 272 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 273 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 274 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 275 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 276 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 277 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 278 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 279 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 280 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 281 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 282 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 283 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 284 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 285 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 286 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 287 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 288 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 289 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 290 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 291 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 292 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 293 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 294 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 295 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 296 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 297 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 298 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 299 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 300 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 301 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 302 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 303 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 304 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 305 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 306 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 307 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 308 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 309 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 310 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 311 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 312 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 313 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 314 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 315 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 316 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 317 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 318 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 319 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 320 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 321 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 322 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 323 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 324 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 325 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 326 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 327 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 328 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 329 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 330 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 331 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 332 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 333 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 334 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 335 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 336 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 337 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 338 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 339 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 340 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 341 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 342 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 343 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 344 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 345 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 346 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 347 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 348 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 349 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 350 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 351 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 352 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 353 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 354 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 355 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 356 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 357 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 358 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 359 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 360 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 361 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 362 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 363 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 364 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 365 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 366 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 367 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 368 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 369 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 370 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 371 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 372 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 373 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 374 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 375 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 376 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 377 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 378 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 379 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 380 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 381 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 382 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 383 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 384 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 385 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 386 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 387 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 388 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 389 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 390 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 391 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 392 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 393 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 394 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 395 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 396 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 397 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 398 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 399 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 400 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 401 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 402 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 403 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 404 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 405 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 406 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 407 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 408 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 409 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 410 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 411 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 412 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 413 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 414 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 415 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 416 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 417 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 418 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 419 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 420 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 421 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 422 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 423 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 424 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 425 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 426 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 427 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 428 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 429 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
