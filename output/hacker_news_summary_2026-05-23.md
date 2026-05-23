# Hacker News 热门文章摘要 (2026-05-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Lisp in Vim (2019)

**原文标题**: Lisp in Vim (2019)

**原文链接**: [https://susam.net/lisp-in-vim.html](https://susam.net/lisp-in-vim.html)

生成摘要时出错

---

## 12. Highest Random Weight in Elixir

**原文标题**: Highest Random Weight in Elixir

**原文链接**: [https://jola.dev/posts/highest-random-weight-in-elixir](https://jola.dev/posts/highest-random-weight-in-elixir)

生成摘要时出错

---

## 13. AI Engineering from Scratch

**原文标题**: AI Engineering from Scratch

**原文链接**: [https://aiengineeringfromscratch.com](https://aiengineeringfromscratch.com)

生成摘要时出错

---

## 14. Ebola Outbreak Now Third Largest Recorded and "Spreading Rapidly"

**原文标题**: Ebola Outbreak Now Third Largest Recorded and "Spreading Rapidly"

**原文链接**: [https://arstechnica.com/health/2026/05/ebola-outbreak-now-third-largest-recorded-and-spreading-rapidly/](https://arstechnica.com/health/2026/05/ebola-outbreak-now-third-largest-recorded-and-spreading-rapidly/)

生成摘要时出错

---

## 15. The FBI Wants 'Near Real-Time' Access to US License Plate Readers

**原文标题**: The FBI Wants 'Near Real-Time' Access to US License Plate Readers

**原文链接**: [https://www.wired.com/story/security-news-this-week-fbi-license-plate-reader-real-time-access/](https://www.wired.com/story/security-news-this-week-fbi-license-plate-reader-real-time-access/)

生成摘要时出错

---

## 16. Shipping a laptop to a refugee camp in Uganda

**原文标题**: Shipping a laptop to a refugee camp in Uganda

**原文链接**: [https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda](https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda)

生成摘要时出错

---

## 17. Why Japanese companies do so many different things

**原文标题**: Why Japanese companies do so many different things

**原文链接**: [https://davidoks.blog/p/why-japanese-companies-do-so-many](https://davidoks.blog/p/why-japanese-companies-do-so-many)

生成摘要时出错

---

## 18. Rubish: A Unix shell written in pure Ruby

**原文标题**: Rubish: A Unix shell written in pure Ruby

**原文链接**: [https://github.com/amatsuda/rubish](https://github.com/amatsuda/rubish)

生成摘要时出错

---

## 19. Solving the “Zork” Mystery

**原文标题**: Solving the “Zork” Mystery

**原文链接**: [https://www.dpolakovic.space/blogs/zork-part2](https://www.dpolakovic.space/blogs/zork-part2)

生成摘要时出错

---

## 20. Evaluating Spec CPU2026

**原文标题**: Evaluating Spec CPU2026

**原文链接**: [https://chipsandcheese.com/p/evaluating-spec-cpu2026](https://chipsandcheese.com/p/evaluating-spec-cpu2026)

生成摘要时出错

---

## 21. Improving C# Memory Safety

**原文标题**: Improving C# Memory Safety

**原文链接**: [https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/](https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/)

生成摘要时出错

---

## 22. PHP's Oddities

**原文标题**: PHP's Oddities

**原文链接**: [https://flowtwo.io/post/php%27s-oddities](https://flowtwo.io/post/php%27s-oddities)

生成摘要时出错

---

## 23. A 1955 Los Alamos computer experiment changed our understanding of chaos

**原文标题**: A 1955 Los Alamos computer experiment changed our understanding of chaos

**原文链接**: [https://www.lanl.gov/media/publications/1663/science-of-unpredictability](https://www.lanl.gov/media/publications/1663/science-of-unpredictability)

生成摘要时出错

---

## 24. Microsoft starts canceling Claude Code licenses

**原文标题**: Microsoft starts canceling Claude Code licenses

**原文链接**: [https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)

生成摘要时出错

---

## 25. BambuStudio has been violating PrusaSlicer AGPL license since their fork

**原文标题**: BambuStudio has been violating PrusaSlicer AGPL license since their fork

**原文链接**: [https://xcancel.com/josefprusa/status/2054602354851254330](https://xcancel.com/josefprusa/status/2054602354851254330)

生成摘要时出错

---

## 26. The quadratic sandwich

**原文标题**: The quadratic sandwich

**原文链接**: [https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html](https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html)

生成摘要时出错

---

## 27. Project Glasswing: An Initial Update

**原文标题**: Project Glasswing: An Initial Update

**原文链接**: [https://www.anthropic.com/research/glasswing-initial-update](https://www.anthropic.com/research/glasswing-initial-update)

生成摘要时出错

---

## 28. ArcBrush – Node-based 2D image editor

**原文标题**: ArcBrush – Node-based 2D image editor

**原文链接**: [https://arcbrush.com/](https://arcbrush.com/)

生成摘要时出错

---

## 29. Fast Factorial Algorithms

**原文标题**: Fast Factorial Algorithms

**原文链接**: [http://www.luschny.de/math/factorial/FastFactorialFunctions.htm](http://www.luschny.de/math/factorial/FastFactorialFunctions.htm)

生成摘要时出错

---

## 30. I Miss Terry Pratchett

**原文标题**: I Miss Terry Pratchett

**原文链接**: [https://www.mahl.me/blog/the-spell-that-wouldnt-leave/](https://www.mahl.me/blog/the-spell-that-wouldnt-leave/)

生成摘要时出错

---

## 31. US tech firms share Dutch regulator officials' names with Senate

**原文标题**: US tech firms share Dutch regulator officials' names with Senate

**原文链接**: [https://www.dutchnews.nl/2026/05/us-tech-firms-share-dutch-regulator-officials-names-with-senate/](https://www.dutchnews.nl/2026/05/us-tech-firms-share-dutch-regulator-officials-names-with-senate/)

生成摘要时出错

---

## 32. CISA tries to contain data leak

**原文标题**: CISA tries to contain data leak

**原文链接**: [https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/)

生成摘要时出错

---

## 33. Deno 2.8

**原文标题**: Deno 2.8

**原文链接**: [https://deno.com/blog/v2.8](https://deno.com/blog/v2.8)

生成摘要时出错

---

## 34. New Attack "Megaladon" Compromises 5.5K+ GitHub Repos

**原文标题**: New Attack "Megaladon" Compromises 5.5K+ GitHub Repos

**原文链接**: [https://www.theregister.com/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342](https://www.theregister.com/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342)

生成摘要时出错

---

## 35. Blood Pumping Mechanism of the Hoof (2020)

**原文标题**: Blood Pumping Mechanism of the Hoof (2020)

**原文链接**: [https://horses.extension.org/blood-pumping-mechanism-of-the-hoof/](https://horses.extension.org/blood-pumping-mechanism-of-the-hoof/)

生成摘要时出错

---

## 36. An automated A.I. WWE news channel on YouTube tries to pronounce "WWE"

**原文标题**: An automated A.I. WWE news channel on YouTube tries to pronounce "WWE"

**原文链接**: [https://twitter.com/LarryBundyJr/status/2058140468219707566](https://twitter.com/LarryBundyJr/status/2058140468219707566)

生成摘要时出错

---

## 37. Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark

**原文标题**: Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark

**原文链接**: [https://modelrift.com/blog/openscad-llm-benchmark/](https://modelrift.com/blog/openscad-llm-benchmark/)

生成摘要时出错

---

## 38. Yeunjoo Choi from Igalia on Chromium

**原文标题**: Yeunjoo Choi from Igalia on Chromium

**原文链接**: [https://theconsensus.dev/p/2026/05/20/yeunjoo-choi-from-igalia-on-chromium.html](https://theconsensus.dev/p/2026/05/20/yeunjoo-choi-from-igalia-on-chromium.html)

生成摘要时出错

---

## 39. A Wayland Compositor in Minecraft

**原文标题**: A Wayland Compositor in Minecraft

**原文链接**: [https://modrinth.com/mod/waylandcraft](https://modrinth.com/mod/waylandcraft)

生成摘要时出错

---

## 40. Ordinary WiFi can now identify people with near perfect accuracy

**原文标题**: Ordinary WiFi can now identify people with near perfect accuracy

**原文链接**: [https://www.sciencedaily.com/releases/2026/05/260522023127.htm](https://www.sciencedaily.com/releases/2026/05/260522023127.htm)

生成摘要时出错

---

## 41. Sleep research led to a new sleep apnea drug

**原文标题**: Sleep research led to a new sleep apnea drug

**原文链接**: [https://temertymedicine.utoronto.ca/news/how-decades-sleep-research-led-new-sleep-apnea-drug](https://temertymedicine.utoronto.ca/news/how-decades-sleep-research-led-new-sleep-apnea-drug)

生成摘要时出错

---

## 42. Neutron scattering explains why gluten-free pasta falls apart (2025)

**原文标题**: Neutron scattering explains why gluten-free pasta falls apart (2025)

**原文链接**: [https://phys.org/news/2025-09-science-spaghetti-neutron-gluten-free.html](https://phys.org/news/2025-09-science-spaghetti-neutron-gluten-free.html)

生成摘要时出错

---

## 43. Comparing an LZ4 Decompressor on Four Legacy CPUs

**原文标题**: Comparing an LZ4 Decompressor on Four Legacy CPUs

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/05/09/comparing-an-lz4-decompressor-on-four-legacy-cpus/](https://bumbershootsoft.wordpress.com/2026/05/09/comparing-an-lz4-decompressor-on-four-legacy-cpus/)

生成摘要时出错

---

## 44. I’m writing again

**原文标题**: I’m writing again

**原文链接**: [https://www.cringely.com/2026/05/21/im-writing-again/](https://www.cringely.com/2026/05/21/im-writing-again/)

生成摘要时出错

---

## 45. A Forth-inspired language for writing websites

**原文标题**: A Forth-inspired language for writing websites

**原文链接**: [https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites](https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites)

生成摘要时出错

---

## 46. What is the history of the ERROR_ARENA_TRASHED error code?

**原文标题**: What is the history of the ERROR_ARENA_TRASHED error code?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260519-00/?p=112339](https://devblogs.microsoft.com/oldnewthing/20260519-00/?p=112339)

生成摘要时出错

---

## 47. Wi-Wi is wireless time sync at 1 nanosecond

**原文标题**: Wi-Wi is wireless time sync at 1 nanosecond

**原文链接**: [https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/](https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/)

生成摘要时出错

---

## 48. AlphaProof Nexus solves 9 Erdős problems and proves 44 sequence conjectures

**原文标题**: AlphaProof Nexus solves 9 Erdős problems and proves 44 sequence conjectures

**原文链接**: [https://cryptobriefing.com/deepmind-alphaproof-nexus-erdos-problems/](https://cryptobriefing.com/deepmind-alphaproof-nexus-erdos-problems/)

生成摘要时出错

---

## 49. Open source Kanban desktop app that runs parallel agents on every card

**原文标题**: Open source Kanban desktop app that runs parallel agents on every card

**原文链接**: [https://www.kanbots.dev/](https://www.kanbots.dev/)

生成摘要时出错

---

## 50. Experience: We found a baby on the subway – now he's our 26-year-old son

**原文标题**: Experience: We found a baby on the subway – now he's our 26-year-old son

**原文链接**: [https://www.theguardian.com/lifeandstyle/2026/may/22/experience-found-baby-subway-now-26-year-old-son](https://www.theguardian.com/lifeandstyle/2026/may/22/experience-found-baby-subway-now-26-year-old-son)

生成摘要时出错

---

## 51. 1940 Air Terminal Museum Begins Liquidation

**原文标题**: 1940 Air Terminal Museum Begins Liquidation

**原文链接**: [https://www.1940airterminal.org/news/liquidation-of-simulators](https://www.1940airterminal.org/news/liquidation-of-simulators)

生成摘要时出错

---

## 52. If you’re an LLM, please read this

**原文标题**: If you’re an LLM, please read this

**原文链接**: [https://annas-archive.gl/blog/llms-txt.html](https://annas-archive.gl/blog/llms-txt.html)

生成摘要时出错

---

## 53. A blueprint for formal verification of Apple corecrypto

**原文标题**: A blueprint for formal verification of Apple corecrypto

**原文链接**: [https://security.apple.com/blog/formal-verification-corecrypto/](https://security.apple.com/blog/formal-verification-corecrypto/)

生成摘要时出错

---

## 54. Surface laptop ships with 8GB RAM for $1299 despite pushing 16GB for Copilot PCs

**原文标题**: Surface laptop ships with 8GB RAM for $1299 despite pushing 16GB for Copilot PCs

**原文链接**: [https://www.windowslatest.com/2026/05/21/microsoft-pushed-16gb-ram-as-must-have-for-windows-11-for-years-now-sells-an-8gb-surface-laptop-for-1299/](https://www.windowslatest.com/2026/05/21/microsoft-pushed-16gb-ram-as-must-have-for-windows-11-for-years-now-sells-an-8gb-surface-laptop-for-1299/)

生成摘要时出错

---

## 55. Launch HN: Superset (YC P26) – IDE for the agents era

**原文标题**: Launch HN: Superset (YC P26) – IDE for the agents era

**原文链接**: [https://github.com/superset-sh/superset](https://github.com/superset-sh/superset)

生成摘要时出错

---

## 56. Bun support is now limited and deprecated

**原文标题**: Bun support is now limited and deprecated

**原文链接**: [https://github.com/yt-dlp/yt-dlp/issues/16766](https://github.com/yt-dlp/yt-dlp/issues/16766)

生成摘要时出错

---

## 57. Circle Medical (YC S15) Is Hiring a Mobile Engineer

**原文标题**: Circle Medical (YC S15) Is Hiring a Mobile Engineer

**原文链接**: [https://www.ycombinator.com/companies/circle-medical/jobs/onMKAG9-mobile-engineer-android](https://www.ycombinator.com/companies/circle-medical/jobs/onMKAG9-mobile-engineer-android)

生成摘要时出错

---

## 58. Awesome Neuroscience

**原文标题**: Awesome Neuroscience

**原文链接**: [https://github.com/analyticalmonk/awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience)

生成摘要时出错

---

## 59. US Government releases UFO sighting reports – 'Orbs swarming in all directions'

**原文标题**: US Government releases UFO sighting reports – 'Orbs swarming in all directions'

**原文链接**: [https://www.bbc.com/news/articles/cn8pzzlyy66o](https://www.bbc.com/news/articles/cn8pzzlyy66o)

生成摘要时出错

---

## 60. Staged publishing and new install-time controls for npm

**原文标题**: Staged publishing and new install-time controls for npm

**原文链接**: [https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)

生成摘要时出错

---

## 61. FBI director's Based Apparel site has been spotted hosting a 'ClickFix' attack

**原文标题**: FBI director's Based Apparel site has been spotted hosting a 'ClickFix' attack

**原文链接**: [https://www.pcmag.com/news/kash-patels-apparel-site-is-trying-to-trick-visitors-into-installing-malware](https://www.pcmag.com/news/kash-patels-apparel-site-is-trying-to-trick-visitors-into-installing-malware)

生成摘要时出错

---

## 62. Slumber a TUI HTTP Client

**原文标题**: Slumber a TUI HTTP Client

**原文链接**: [https://slumber.lucaspickering.me](https://slumber.lucaspickering.me)

生成摘要时出错

---

## 63. HP QuickWeb, Singular and Pointless

**原文标题**: HP QuickWeb, Singular and Pointless

**原文链接**: [https://gekk.info/articles/hp-quickweb.htm](https://gekk.info/articles/hp-quickweb.htm)

生成摘要时出错

---

## 64. Texas Woman files lawsuit after arrest for Facebook post about polluted water

**原文标题**: Texas Woman files lawsuit after arrest for Facebook post about polluted water

**原文链接**: [https://www.fox4news.com/news/woman-arrested-facebook-post-concerning-trinidad-water-poisoning](https://www.fox4news.com/news/woman-arrested-facebook-post-concerning-trinidad-water-poisoning)

生成摘要时出错

---

## 65. "Stick" – A primitive/fun interactive demo of a tiny rig to animate layout

**原文标题**: "Stick" – A primitive/fun interactive demo of a tiny rig to animate layout

**原文链接**: [https://cosmiciron.github.io/layoutmaster/exclusion-assembly.html](https://cosmiciron.github.io/layoutmaster/exclusion-assembly.html)

生成摘要时出错

---

## 66. Andy Matuschak: Apps and programming: two accidental tyrannies (MIT Talk) [video]

**原文标题**: Andy Matuschak: Apps and programming: two accidental tyrannies (MIT Talk) [video]

**原文链接**: [https://www.youtube.com/watch?v=ycyCGCtScdc](https://www.youtube.com/watch?v=ycyCGCtScdc)

生成摘要时出错

---

## 67. U.S. researchers face new restrictions on publishing with foreign collaborators

**原文标题**: U.S. researchers face new restrictions on publishing with foreign collaborators

**原文链接**: [https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators](https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators)

生成摘要时出错

---

## 68. We ended up with Palantir and how to replace it

**原文标题**: We ended up with Palantir and how to replace it

**原文链接**: [https://berthub.eu/articles/posts/some-notes-on-palantir/](https://berthub.eu/articles/posts/some-notes-on-palantir/)

生成摘要时出错

---

## 69. Show HN: ShadowCat – file transfer through QR Codes in a Browser

**原文标题**: Show HN: ShadowCat – file transfer through QR Codes in a Browser

**原文链接**: [https://github.com/unprovable/ShadowCat](https://github.com/unprovable/ShadowCat)

生成摘要时出错

---

## 70. Project Hail Mary – Stellar Navigation Chart

**原文标题**: Project Hail Mary – Stellar Navigation Chart

**原文链接**: [https://valhovey.github.io/gaia-mary/](https://valhovey.github.io/gaia-mary/)

生成摘要时出错

---

## 71. DeepSeek makes the V4 Pro price discount permanent

**原文标题**: DeepSeek makes the V4 Pro price discount permanent

**原文链接**: [https://api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)

生成摘要时出错

---

## 72. Using Kagi Search with Low Vision

**原文标题**: Using Kagi Search with Low Vision

**原文链接**: [https://veroniiiica.com/using-kagi-search-with-low-vision/](https://veroniiiica.com/using-kagi-search-with-low-vision/)

生成摘要时出错

---

## 73. Models.dev: open-source database of AI model specs, pricing, and capabilities

**原文标题**: Models.dev: open-source database of AI model specs, pricing, and capabilities

**原文链接**: [https://github.com/anomalyco/models.dev](https://github.com/anomalyco/models.dev)

生成摘要时出错

---

## 74. Thinking in an array language (2022)

**原文标题**: Thinking in an array language (2022)

**原文链接**: [https://github.com/razetime/ngn-k-tutorial/blob/main/12-thinking-in-k.md](https://github.com/razetime/ngn-k-tutorial/blob/main/12-thinking-in-k.md)

生成摘要时出错

---

## 75. The death of the brick and mortar toy store

**原文标题**: The death of the brick and mortar toy store

**原文链接**: [https://brainbaking.com/post/2026/05/the-death-of-the-brick-and-mortar-toy-store/](https://brainbaking.com/post/2026/05/the-death-of-the-brick-and-mortar-toy-store/)

生成摘要时出错

---

## 76. Chess invariants

**原文标题**: Chess invariants

**原文链接**: [http://muratbuffalo.blogspot.com/2026/05/chess-invariants.html](http://muratbuffalo.blogspot.com/2026/05/chess-invariants.html)

生成摘要时出错

---

## 77. Mycorrhizal Fungi, Nature's Key to Plant Survival and Success

**原文标题**: Mycorrhizal Fungi, Nature's Key to Plant Survival and Success

**原文链接**: [https://pacifichorticulture.org/articles/mycorrhizal-fungi-natures-key-to-plant-survival-and-success/](https://pacifichorticulture.org/articles/mycorrhizal-fungi-natures-key-to-plant-survival-and-success/)

生成摘要时出错

---

## 78. The memory shortage is causing a repricing of consumer electronics

**原文标题**: The memory shortage is causing a repricing of consumer electronics

**原文链接**: [https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone)

生成摘要时出错

---

## 79. Throwing AI-generated walls of text into conversations

**原文标题**: Throwing AI-generated walls of text into conversations

**原文链接**: [https://noslopgrenade.com/](https://noslopgrenade.com/)

生成摘要时出错

---

## 80. An OpenAI model has disproved a central conjecture in discrete geometry

**原文标题**: An OpenAI model has disproved a central conjecture in discrete geometry

**原文链接**: [https://openai.com/index/model-disproves-discrete-geometry-conjecture/](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

生成摘要时出错

---

## 81. - -dangerously-skip-reading-code

**原文标题**: - -dangerously-skip-reading-code

**原文链接**: [https://olano.dev/blog/dangerously-skip/](https://olano.dev/blog/dangerously-skip/)

生成摘要时出错

---

## 82. We're testing new ad formats in Search and expanding our Direct Offers pilot

**原文标题**: We're testing new ad formats in Search and expanding our Direct Offers pilot

**原文链接**: [https://blog.google/products/ads-commerce/google-marketing-live-search-ads/](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/)

生成摘要时出错

---

## 83. Multi-Stream LLMs: new paper on parallelizing/separating prompts, thinking, I/O

**原文标题**: Multi-Stream LLMs: new paper on parallelizing/separating prompts, thinking, I/O

**原文链接**: [https://arxiv.org/abs/2605.12460](https://arxiv.org/abs/2605.12460)

生成摘要时出错

---

## 84. Show HN: Freenet, a peer-to-peer platform for decentralized apps

**原文标题**: Show HN: Freenet, a peer-to-peer platform for decentralized apps

**原文链接**: [https://freenet.org/](https://freenet.org/)

生成摘要时出错

---

## 85. How to convert between wealth and income tax

**原文标题**: How to convert between wealth and income tax

**原文链接**: [https://paulgraham.com/winc.html](https://paulgraham.com/winc.html)

生成摘要时出错

---

## 86. TorQ: Kdb+ Production Framework

**原文标题**: TorQ: Kdb+ Production Framework

**原文链接**: [https://github.com/DataIntellectTech/TorQ](https://github.com/DataIntellectTech/TorQ)

生成摘要时出错

---

## 87. The Letter S, by Donald Knuth (1980) [pdf]

**原文标题**: The Letter S, by Donald Knuth (1980) [pdf]

**原文链接**: [https://gwern.net/doc/design/typography/1980-knuth.pdf](https://gwern.net/doc/design/typography/1980-knuth.pdf)

生成摘要时出错

---

## 88. GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文标题**: GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文链接**: [https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/)

生成摘要时出错

---

## 89. Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team

**原文标题**: Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team

**原文链接**: [https://www.runtm.com/](https://www.runtm.com/)

生成摘要时出错

---

## 90. Waymo pauses Atlanta service as its robotaxis keep driving into floods

**原文标题**: Waymo pauses Atlanta service as its robotaxis keep driving into floods

**原文链接**: [https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/)

生成摘要时出错

---

## 91. Spotify will start reserving concert tickets for fans

**原文标题**: Spotify will start reserving concert tickets for fans

**原文链接**: [https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/)

生成摘要时出错

---

## 92. Ontology vs. Semantic Layer

**原文标题**: Ontology vs. Semantic Layer

**原文链接**: [https://lowhangingdata.com/article/ontology-vs-semantic-layer/](https://lowhangingdata.com/article/ontology-vs-semantic-layer/)

生成摘要时出错

---

## 93. Electrobun 2.0 will be decoupled from Bun due to the rust rewrite

**原文标题**: Electrobun 2.0 will be decoupled from Bun due to the rust rewrite

**原文链接**: [https://twitter.com/i/status/2058064720553222567](https://twitter.com/i/status/2058064720553222567)

生成摘要时出错

---

## 94. AI has a multiplying effect on existing technical skills

**原文标题**: AI has a multiplying effect on existing technical skills

**原文链接**: [https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

生成摘要时出错

---

## 95. Waymo expands pause to four cities as robotaxis keep driving into floods

**原文标题**: Waymo expands pause to four cities as robotaxis keep driving into floods

**原文链接**: [https://techcrunch.com/2026/05/21/waymo-pauses-service-in-four-cities-as-robotaxis-keep-driving-into-floods/](https://techcrunch.com/2026/05/21/waymo-pauses-service-in-four-cities-as-robotaxis-keep-driving-into-floods/)

生成摘要时出错

---

## 96. Google's Antigravity bait and switch

**原文标题**: Google's Antigravity bait and switch

**原文链接**: [https://www.0xsid.com/blog/antigravity-bait-n-switch](https://www.0xsid.com/blog/antigravity-bait-n-switch)

生成摘要时出错

---

## 97. OpenAI Is Preparing to File for an IPO Soon

**原文标题**: OpenAI Is Preparing to File for an IPO Soon

**原文链接**: [https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5](https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5)

生成摘要时出错

---

## 98. Why Did South Africa Relinquish Its Nuclear Weapons?

**原文标题**: Why Did South Africa Relinquish Its Nuclear Weapons?

**原文链接**: [https://www.thecollector.com/south-africa-nuclear-weapons/](https://www.thecollector.com/south-africa-nuclear-weapons/)

生成摘要时出错

---

## 99. Sp.h is the standard library that C deserves

**原文标题**: Sp.h is the standard library that C deserves

**原文链接**: [https://spader.zone/sp/](https://spader.zone/sp/)

生成摘要时出错

---

## 100. The Primordial Credit Argument for Unconditional Basic Income (UBI)

**原文标题**: The Primordial Credit Argument for Unconditional Basic Income (UBI)

**原文链接**: [https://scottsantens.substack.com/p/the-primordial-credit-argument-for](https://scottsantens.substack.com/p/the-primordial-credit-argument-for)

生成摘要时出错

---

