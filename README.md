# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-29.md)

*最后自动更新时间: 2026-07-29 18:31:31*
## 1. Lisp 走向 Forth，Forth 走向 Lisp

**原文标题**: Lisp moving Forth moving Lisp

**原文链接**: [https://letoverlambda.com/textmode.cl/guest/chap8.html](https://letoverlambda.com/textmode.cl/guest/chap8.html)

在《Let Over Lambda》的这段摘录中，Doug Hoyte 探讨了如何利用 Lisp 宏来实现一个“Lisp 风格”的 Forth 版本。他指出，如果说 Lisp 是由“列表”定义的，那么 Forth 就是由“堆栈”和“线索化代码”（threaded code）定义的。这两种语言有着共同的哲学，即提供“元原语”（meta-primitives），使程序员能够担任语言实现者的角色，而不仅仅是使用者。

Hoyte 概述了在 Lisp 内部构建 Forth 系统的技术基础：

*   **寄存器与堆栈：** 该系统使用抽象寄存器（如 `pstack`、`rstack` 和 `pc`）。与大多数语言不同，Forth 使用两个独立的堆栈：用于传递数据的参数栈和用于跟踪执行路径的返回栈。在本次实现中，这些堆栈通过 Lisp 的 `push` 和 `pop` 宏在 cons 单元链表上进行管理。
*   **字典：** Forth 的“单词”（即过程）存储在一个按时间顺序排列的 Lisp 结构单向链表中。这实现了高效的查找和元编程能力，例如功能类似于 Lisp 宏的“立即词”（immediate words）。
*   **线索化代码：** Forth 的核心区别在于它使用了线索化代码——即“内部解释器”所遵循的代码单元指针。Hoyte 讨论了各种线索化类型（间接、直接、令牌和子程序线索化），并指出这些方法允许开发者在程序体积和执行速度的权衡之间进行精细控制。

最后，Hoyte 引入了 **“Flub”** 的概念：指代那些仅提供不透明子程序线索化代码的语言（如 C 或大多数现代 Lisp）。他认为，此类语言限制了程序员操纵汇编过程的能力。相比之下，通过在 Lisp 中实现 Forth，Hoyte 展示了“语法的二元性”和宏抽象如何重新实现对底层执行的高层控制。

---

## 2. CipherX通过可溶解微针贴片实现无痛永久纹身。

**原文标题**: CipherX applies painless permanent tattoos with dissolving microneedle patches

**原文链接**: [https://www.designboom.com/technology/cipherx-painless-permanent-tattoos-dissolving-microneedle-patches/](https://www.designboom.com/technology/cipherx-painless-permanent-tattoos-dissolving-microneedle-patches/)

CipherX 推出了一种革命性的永久纹身方法，利用可溶解微针贴片为传统纹身提供了一种无痛、无血的替代方案。该系统由材料科学家费迪南德·科勒（Ferdinand Kohle）为解决自身的针头恐惧症而开发，它采用包含数百个填充颜料、可生物降解微点的一次性贴片，取代了标准纹身机的振动针头。

操作过程涉及一个专用的手持工具，通过单一动作即可将贴片对齐并压在皮肤上。在 10 到 15 分钟内，微针会溶解并将墨水以精确的数字图案沉积在皮肤中。虽然移除贴片后图像最初可能显得较淡，但颜料会逐渐加深，微点也将在接下来的 48 小时内视觉上融合成连续的形态。后期护理非常简单，主要包括涂抹凡士林以及在两天内避免接触水。

通过将数字艺术作品转化为“像素化”的微点阵列，CipherX 将纹身过程从手工技艺转变为软件驱动的制造模式。这一创新使该系统的涂抹器荣获了 2026 年红点奖的“最佳设计奖”（Best of the Best）。

除了人体艺术，CipherX 的定位是更广泛的皮肤技术平台，其创始人科勒和卡尔-安东·哈姆斯（Karl-Anton Harms）正在探索其在美容治疗、医疗标记和药物输送领域的应用。尽管目前该技术仅通过授权的快闪店和受训从业者提供，但公司的规划蓝图包括未来的家用套件，这可能将纹身推向零售和现场活动领域。

---

## 3. 基荷是一个神话 (2024)

**原文标题**: Baseload Is a Myth (2024)

**原文链接**: [https://cleanenergyreview.io/p/baseload-is-a-myth](https://cleanenergyreview.io/p/baseload-is-a-myth)

生成摘要时出错

---

## 4. 古罗马版谷歌地图：去海边要多久

**原文标题**: Ancient Rome's version of Google Maps: how long to reach the beach

**原文链接**: [https://www.euronews.com/culture/2026/07/02/ancient-romes-version-of-google-maps-how-long-to-reach-the-beach](https://www.euronews.com/culture/2026/07/02/ancient-romes-version-of-google-maps-how-long-to-reach-the-beach)

本文介绍了一个名为 **ORBIS** 的数字项目，即由斯坦福大学开发的“古代世界的谷歌地图”。这是一个交互式地理空间网络模型，允许用户模拟在公元200年左右的罗马帝国境内的旅行。

该项目的主要特点包括：

*   **全面的地图覆盖：** ORBIS 覆盖了约1000万平方公里的面积，整合了632个地点（包括主要城市、港口和山口），以及19.2万公里的道路和通航河流网络。
*   **动态变量：** 与静态地图不同，该工具考虑了季节性变化。它能根据月份计算旅行时间和成本，并兼顾了历史上决定航行速度和安全性的洋流、风向及天气条件。
*   **交通方式：** 用户可以选择古代使用的各种交通方式，如牛车、驮畜、私人马车或快速帆船。这使研究人员能够直观对比军事进军与商业贸易路线的差异。
*   **经济洞察：** 除了时间，ORBIS 还以“第纳里”（古罗马货币）和维持旅途所需的粮食数量来计算旅行“成本”。这有助于历史学家理解罗马贸易与扩张中的物流挑战和经济约束。

该工具为古代世界的互联互通提供了生动的视角，阐明了在古罗马，“距离”的衡量标准与其说是英里，不如说是穿越地中海区域所需的时间和费用。例如，它揭示了从罗马到亚历山大的航行在夏季可能非常快捷，但在冬季则几乎无法成行。

---

## 5. 警惕厂商 C++ 工具链中遗漏的警告

**原文标题**: Watch out for missed warnings on vendor C++ toolchains

**原文链接**: [https://blog.poly.nomial.co.uk/2026-03-31-watch-out-for-missed-warnings-on-vendor-cpp-toolchains.html](https://blog.poly.nomial.co.uk/2026-03-31-watch-out-for-missed-warnings-on-vendor-cpp-toolchains.html)

本文强调了在嵌入式开发中仅依赖特定供应商提供的 C++ 工具链所面临的严重安全风险。作者描述了一个项目的安全审查过程，该项目使用了供应商的 SDK 和编译器，并启用了严格的警告标志（包括 `-Werror` 和 `-Wconversion`）以防止出现漏洞。

作者在一个专为 32 位数据设计的恒定时间内存比较函数（`memcmp_ct_32`）中发现了一个重大缺陷。该函数使用 `uint8_t` 类型的累加器来存储 32 位指针异或（XOR）操作的结果。这导致了**隐式窄化转换**，每个比较结果中有 24 位被截断并丢弃。结果是，该函数实际上每四个字节才进行一次有效的比较，留下了巨大的安全漏洞。

至关重要的一点是，虽然最新版本的 **GCC** 正确地将其标记为警告（在 `-Werror` 模式下会终止构建），但**供应商的工具链**尽管启用了相关标志，却悄无声息地忽略了这一错误。这种差异导致一个重大漏洞在“生产环境”代码中长期存在。

**核心教训：**
*   **供应商工具链并非万无一失：** 即使明确启用了警告，它们对标准编译器警告的实现也可能存在缺陷或不完整。
*   **通过交叉编译确保安全：** 在审查安全敏感的代码时，开发者应尝试使用最新版本的 GCC 或 Clang，并将警告级别调至最高（“turned up to 11”）来构建项目。
*   **警告标志的细微差别：** 注意在 GCC 中，需要专门使用 `-Wconversion`（而非 `-Wnarrowing`）才能捕获 C++ 中的这类隐式窄化转换。

作者总结道，将现代主流编译器作为辅助检查手段，是识别专用工具或旧版供应商工具可能忽略的漏洞的关键步骤。

---

## 6. 一种基于纹理查找的GPU贝塞尔曲线求值方法 (JCGT)

**原文标题**: A Texture Lookup Approach to Bézier Curve Evaluation on the GPU (JCGT)

**原文链接**: [https://jcgt.org/published/0015/02/01/](https://jcgt.org/published/0015/02/01/)

本文提出了一种在 GPU 上加速 Bézier 曲线求值的高效方法，通过将传统的算术密集型计算替换为预计算纹理查表来提升性能。

虽然 De Casteljau 算法和 Horner 算法等标准技术具有数值稳定性，但在渲染高阶曲线或大规模矢量图形时，由于指令数量较多，往往会成为性能瓶颈。作者提出将这一计算负担转移到 GPU 的专用纹理映射单元。

**关键点：**
*   **机制：** 该方法涉及预计算 Bernstein 基函数（Bézier 曲线的多项式分量），并将其存储在 1D 或 2D 纹理中。在运行时，着色器利用曲线参数（$t$）和基函数索引直接从纹理中获取权重。
*   **硬件利用：** 通过纹理查表，该方法充分利用了 GPU 的硬件加速线性插值和高速纹理缓存。这减轻了算术逻辑单元（ALU）的工作负载，并降低了着色器内部的寄存器压力。
*   **性能：** 作者证明，对于高阶曲线（通常为 4 阶及以上），纹理查表法的表现显著优于传统的迭代方法。随着几何复杂度的增加，该方案展现出更好的可扩展性。
*   **通用性：** 该技术不仅限于简单曲线，还可以扩展到 Bézier 曲面和其他基于多项式的样条曲线，使其在字体渲染、CAD 软件和实时矢量图形领域具有高度的应用价值。

最后，论文总结指出，随着现代 GPU 纹理采样吞吐量的持续提升，将基函数求值卸载至内存查表，可以在不牺牲视觉精度的前提下，大幅加速参数曲线的求值过程。

---

## 7. 谷歌关闭获诺贝尔奖的AlphaFold

**原文标题**: Google shuts down Nobel Prize winning AlphaFold

**原文链接**: [https://www.engadget.com/2225849/google-shuts-down-alphafold/](https://www.engadget.com/2225849/google-shuts-down-alphafold/)

无法访问文章链接。

---

## 8. San Francisco: Don't Fall for Industry Defense of Surveillance Pricing

**原文标题**: San Francisco: Don't Fall for Industry Defense of Surveillance Pricing

**原文链接**: [https://www.eff.org/deeplinks/2026/07/san-francisco-dont-fall-industry-defense-surveillance-pricing](https://www.eff.org/deeplinks/2026/07/san-francisco-dont-fall-industry-defense-surveillance-pricing)

The Electronic Frontier Foundation (EFF) is urging the San Francisco Board of Supervisors to pass a resolution supporting California Assembly Bill 2654, which would ban the practice of "surveillance pricing." This practice involves corporations using harvested personal data—such as location, purchase history, and demographics—to charge different prices to different consumers for the same product.

The EFF argues that surveillance pricing is an invasive "pay-for-privacy" scheme that treats personal data as a currency. Citing FTC findings, the article notes that companies may exploit vulnerable consumers, such as charging higher prices for baby thermometers based on a parent's zip code or the time of night they are shopping. While industry defenders suggest the practice could lower prices, the EFF contends it primarily incentivizes mass data harvesting and creates "winners and losers" based on often-inaccurate personal dossiers.

The push for the resolution stalled after the San Francisco Chamber of Commerce raised concerns regarding business compliance and the future of loyalty programs. However, the EFF refutes these claims, stating that A.B. 2654 provides clear definitions and explicit carve-outs. The bill protects legitimate discounts, including those based on production costs, customer retention offers, and transparent, uniformly available loyalty programs (such as senior discounts or mailing list benefits).

Ultimately, the EFF views surveillance pricing as a harmful extension of online behavioral advertising that manipulates economic choices. They call on San Francisco leadership to reject industry pressure and protect privacy as a fundamental human right, ensuring that the cost of everyday goods does not depend on a consumer's willingness to surrender their personal information.

---

## 9. Apple's hostile App Store rating system

**原文标题**: Apple's hostile App Store rating system

**原文链接**: [https://lapcatsoftware.com/articles/2026/7/14.html](https://lapcatsoftware.com/articles/2026/7/14.html)

生成摘要时出错

---

## 10. Show HN: Write, simulate and synthesize VHDL/Verilog in the browser

**原文标题**: Show HN: Write, simulate and synthesize VHDL/Verilog in the browser

**原文链接**: [https://risingedge.pro](https://risingedge.pro)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 2 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 3 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 4 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 5 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 6 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 7 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 8 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 9 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 10 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 11 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 12 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 13 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 14 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 15 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 16 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 17 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 18 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 19 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 20 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 21 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 22 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 23 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 24 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 25 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 26 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 27 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 28 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 29 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 30 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 31 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 32 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 33 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 34 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 35 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 36 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 37 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 38 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 39 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 40 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 41 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 42 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 43 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 44 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 45 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 46 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 47 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 48 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 49 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 50 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 51 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 52 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 53 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 54 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 55 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 56 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 57 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 58 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 59 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 60 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 61 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 62 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 63 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 64 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 65 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 66 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 67 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 68 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 69 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 70 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 71 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 72 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 73 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 74 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 75 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 76 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 77 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 78 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 79 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 80 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 81 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 82 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 83 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 84 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 85 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 86 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 87 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 88 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 89 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 90 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 91 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 92 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 93 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 94 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 95 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 96 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 97 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 98 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 99 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 100 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 101 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 102 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 103 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 104 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 105 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 106 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 107 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 108 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 109 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 110 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 111 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 112 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 113 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 114 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 115 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 116 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 117 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 118 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 119 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 120 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 121 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 122 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 123 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 124 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 125 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 126 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 127 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 128 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 129 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 130 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 131 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 132 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 133 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 134 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 135 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 136 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 137 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 138 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 139 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 140 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 141 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 142 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 143 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 144 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 145 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 146 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 147 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 148 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 149 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 150 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 151 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 152 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 153 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 154 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 155 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 156 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 157 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 158 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 159 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 160 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 161 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 162 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 163 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 164 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 165 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 166 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 167 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 168 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 169 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 170 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 171 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 172 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 173 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 174 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 175 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 176 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 177 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 178 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 179 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 180 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 181 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 182 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 183 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 184 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 185 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 186 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 187 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 188 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 189 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 190 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 191 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 192 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 193 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 194 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 195 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 196 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 197 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 198 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 199 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 200 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 201 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 202 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 203 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 204 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 205 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 206 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 207 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 208 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 209 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 210 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 211 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 212 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 213 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 214 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 215 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 216 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 217 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 218 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 219 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 220 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 221 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 222 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 223 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 224 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 225 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 226 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 227 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 228 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 229 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 230 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 231 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 232 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 233 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 234 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 235 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 236 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 237 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 238 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 239 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 240 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 241 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 242 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 243 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 244 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 245 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 246 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 247 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 248 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 249 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 250 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 251 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 252 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 253 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 254 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 255 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 256 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 257 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 258 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 259 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 260 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 261 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 262 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 263 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 264 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 265 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 266 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 267 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 268 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 269 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 270 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 271 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 272 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 273 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 274 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 275 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 276 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 277 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 278 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 279 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 280 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 281 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 282 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 283 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 284 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 285 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 286 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 287 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 288 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 289 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 290 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 291 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 292 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 293 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 294 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 295 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 296 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 297 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 298 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 299 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 300 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 301 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 302 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 303 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 304 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 305 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 306 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 307 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 308 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 309 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 310 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 311 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 312 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 313 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 314 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 315 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 316 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 317 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 318 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 319 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 320 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 321 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 322 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 323 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 324 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 325 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 326 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 327 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 328 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 329 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 330 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 331 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 332 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 333 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 334 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 335 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 336 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 337 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 338 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 339 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 340 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 341 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 342 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 343 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 344 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 345 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 346 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 347 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 348 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 349 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 350 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 351 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 352 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 353 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 354 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 355 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 356 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 357 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 358 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 359 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 360 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 361 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 362 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 363 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 364 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 365 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 366 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 367 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 368 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 369 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 370 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 371 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 372 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 373 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 374 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 375 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 376 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 377 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 378 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 379 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 380 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 381 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 382 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 383 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 384 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 385 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 386 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 387 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 388 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 389 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 390 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 391 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 392 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 393 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 394 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 395 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 396 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 397 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 398 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 399 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 400 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 401 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 402 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 403 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 404 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 405 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 406 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 407 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 408 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 409 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 410 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 411 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 412 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 413 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 414 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 415 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 416 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 417 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 418 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 419 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 420 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 421 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 422 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 423 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 424 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 425 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 426 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 427 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 428 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 429 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 430 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 431 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 432 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 433 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 434 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 435 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 436 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 437 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 438 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 439 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 440 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 441 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 442 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 443 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 444 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 445 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 446 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 447 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 448 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 449 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 450 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 451 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 452 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 453 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 454 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 455 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 456 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 457 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 458 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 459 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 460 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 461 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 462 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 463 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 464 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 465 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 466 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 467 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 468 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 469 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 470 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 471 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 472 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 473 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 474 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 475 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 476 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 477 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 478 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 479 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 480 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 481 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 482 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 483 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 484 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 485 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 486 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 487 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 488 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 489 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 490 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 491 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 492 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 493 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 494 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 495 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 496 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
