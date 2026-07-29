# Hacker News 热门文章摘要 (2026-07-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in

**原文标题**: Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in

**原文链接**: [https://federalistreader.org/](https://federalistreader.org/)

生成摘要时出错

---

## 12. After the AI Crash

**原文标题**: After the AI Crash

**原文链接**: [https://potsandpansbyccg.com/2026/07/29/after-the-ai-crash/](https://potsandpansbyccg.com/2026/07/29/after-the-ai-crash/)

生成摘要时出错

---

## 13. Small Portable Weather Radar

**原文标题**: Small Portable Weather Radar

**原文链接**: [https://github.com/Koakno/Small-portable-weather-radar-Dome](https://github.com/Koakno/Small-portable-weather-radar-Dome)

生成摘要时出错

---

## 14. ALP: Adaptive lossless floating-point compression

**原文标题**: ALP: Adaptive lossless floating-point compression

**原文链接**: [https://github.com/cwida/ALP](https://github.com/cwida/ALP)

生成摘要时出错

---

## 15. Teacher arrested for clapping in opposition at an AI data center meeting

**原文标题**: Teacher arrested for clapping in opposition at an AI data center meeting

**原文链接**: [https://www.tomshardware.com/tech-industry/data-centers/teacher-arrested-for-clapping-in-support-of-opposition-at-an-ai-data-center-meeting-gigawatt-scale-project-gets-approved-anyway-despite-community-resistance](https://www.tomshardware.com/tech-industry/data-centers/teacher-arrested-for-clapping-in-support-of-opposition-at-an-ai-data-center-meeting-gigawatt-scale-project-gets-approved-anyway-despite-community-resistance)

生成摘要时出错

---

## 16. French musician Kavinsky found dead

**原文标题**: French musician Kavinsky found dead

**原文链接**: [https://www.euronews.com/culture/2026/07/29/dj-kavinsky-known-for-his-track-nightcall-found-dead-at-his-paris-home](https://www.euronews.com/culture/2026/07/29/dj-kavinsky-known-for-his-track-nightcall-found-dead-at-his-paris-home)

生成摘要时出错

---

## 17. Valve Sponsors Work Bringing Open-Source RADV Driver to Windows

**原文标题**: Valve Sponsors Work Bringing Open-Source RADV Driver to Windows

**原文链接**: [https://www.phoronix.com/news/Valve-Sponsors-RADV-Windows](https://www.phoronix.com/news/Valve-Sponsors-RADV-Windows)

生成摘要时出错

---

## 18. Graph Engineering Needs a Compiler

**原文标题**: Graph Engineering Needs a Compiler

**原文链接**: [https://fluxtion-playground.dev/blog/2026-07-29-graph-engineering-needs-a-compiler](https://fluxtion-playground.dev/blog/2026-07-29-graph-engineering-needs-a-compiler)

生成摘要时出错

---

## 19. ReFrame – The EPaper Camera

**原文标题**: ReFrame – The EPaper Camera

**原文链接**: [https://reframe.camera/](https://reframe.camera/)

生成摘要时出错

---

## 20. Show HN: Echologue – the private AI voice journal I built for myself

**原文标题**: Show HN: Echologue – the private AI voice journal I built for myself

**原文链接**: [https://echologue.com/](https://echologue.com/)

生成摘要时出错

---

## 21. The only road in London where you have to drive on the right

**原文标题**: The only road in London where you have to drive on the right

**原文链接**: [https://www.mylondon.news/news/transport/only-road-london-you-drive-30499294](https://www.mylondon.news/news/transport/only-road-london-you-drive-30499294)

生成摘要时出错

---

## 22. Show HN: Bullshit Detector – agent skills that fact-check videos and articles

**原文标题**: Show HN: Bullshit Detector – agent skills that fact-check videos and articles

**原文链接**: [https://github.com/SerhiiKorniienko/bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector)

生成摘要时出错

---

## 23. Steel Bank Common Lisp version 2.6.7

**原文标题**: Steel Bank Common Lisp version 2.6.7

**原文链接**: [https://sbcl.org/all-news.html?2.6.7](https://sbcl.org/all-news.html?2.6.7)

生成摘要时出错

---

## 24. Cooking for Engineers

**原文标题**: Cooking for Engineers

**原文链接**: [https://www.cookingforengineers.com/](https://www.cookingforengineers.com/)

生成摘要时出错

---

## 25. LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences

**原文标题**: LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences

**原文链接**: [https://learnvector.ai/](https://learnvector.ai/)

生成摘要时出错

---

## 26. Cracking Windows Open: Porting RADV to Win32

**原文标题**: Cracking Windows Open: Porting RADV to Win32

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/cracking-windows-open-porting-radv-to-win32.html](https://www.collabora.com/news-and-blog/news-and-events/cracking-windows-open-porting-radv-to-win32.html)

生成摘要时出错

---

## 27. Big Companies Are Starting to Hire Again, Defying Predictions of AI Wipeout

**原文标题**: Big Companies Are Starting to Hire Again, Defying Predictions of AI Wipeout

**原文链接**: [https://www.wsj.com/business/big-companies-are-starting-to-hire-again-defying-predictions-of-ai-wipeout-f4974e99](https://www.wsj.com/business/big-companies-are-starting-to-hire-again-defying-predictions-of-ai-wipeout-f4974e99)

生成摘要时出错

---

## 28. Kalshi attacks a Wisconsin law banning election bets as 'voter suppression'

**原文标题**: Kalshi attacks a Wisconsin law banning election bets as 'voter suppression'

**原文链接**: [https://www.npr.org/2026/07/27/nx-s1-5905360/kalshi-wisconsin-election-betting-prediction-markets](https://www.npr.org/2026/07/27/nx-s1-5905360/kalshi-wisconsin-election-betting-prediction-markets)

生成摘要时出错

---

## 29. TokenTown: A visual way to understand how LLMs work

**原文标题**: TokenTown: A visual way to understand how LLMs work

**原文链接**: [https://laurentiugabriel.github.io/token-town/](https://laurentiugabriel.github.io/token-town/)

生成摘要时出错

---

## 30. Windows 11 is quietly installing OneDrive Photos

**原文标题**: Windows 11 is quietly installing OneDrive Photos

**原文链接**: [https://www.windowslatest.com/2026/07/29/windows-11-is-quietly-installing-onedrive-photos-another-image-viewer-that-nobody-asked-for/](https://www.windowslatest.com/2026/07/29/windows-11-is-quietly-installing-onedrive-photos-another-image-viewer-that-nobody-asked-for/)

生成摘要时出错

---

## 31. We built an MCP server for your SRE agent

**原文标题**: We built an MCP server for your SRE agent

**原文链接**: [https://clickhouse.com/blog/benchmarking-the-clickstack-mcp-server-with-hdx-evals](https://clickhouse.com/blog/benchmarking-the-clickstack-mcp-server-with-hdx-evals)

生成摘要时出错

---

## 32. Codex Security

**原文标题**: Codex Security

**原文链接**: [https://github.com/openai/codex-security](https://github.com/openai/codex-security)

生成摘要时出错

---

## 33. AI Doomsday Bullshit Is Getting Tired

**原文标题**: AI Doomsday Bullshit Is Getting Tired

**原文链接**: [https://karlbode.com/ai-doomsday-bullshit-is-getting-tired/](https://karlbode.com/ai-doomsday-bullshit-is-getting-tired/)

生成摘要时出错

---

## 34. Astronomers find strongest evidence yet that Betelgeuse has a companion

**原文标题**: Astronomers find strongest evidence yet that Betelgeuse has a companion

**原文链接**: [https://phys.org/news/2026-07-astronomers-strongest-evidence-betelgeuse-companion.html](https://phys.org/news/2026-07-astronomers-strongest-evidence-betelgeuse-companion.html)

生成摘要时出错

---

## 35. The Strain in Your Brain

**原文标题**: The Strain in Your Brain

**原文链接**: [https://anirudh.fi/strain](https://anirudh.fi/strain)

生成摘要时出错

---

## 36. Hubble: Open-source notetaking app for you and your agents

**原文标题**: Hubble: Open-source notetaking app for you and your agents

**原文链接**: [https://www.hubble.md/](https://www.hubble.md/)

生成摘要时出错

---

## 37. Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-Design

**原文标题**: Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-Design

**原文链接**: [https://transformer-transformer.github.io/](https://transformer-transformer.github.io/)

生成摘要时出错

---

## 38. I Want to Leave the Internet

**原文标题**: I Want to Leave the Internet

**原文链接**: [https://chupacabra.bearblog.dev/i-want-to-leave-the-internet/](https://chupacabra.bearblog.dev/i-want-to-leave-the-internet/)

生成摘要时出错

---

## 39. Show HN: A free curl API for IP data (we scan the IPv4 space in <24h)

**原文标题**: Show HN: A free curl API for IP data (we scan the IPv4 space in <24h)

**原文链接**: [https://worldip.io/news/keyless-ip-api-no-key-required](https://worldip.io/news/keyless-ip-api-no-key-required)

生成摘要时出错

---

## 40. Substack writers, you need a website

**原文标题**: Substack writers, you need a website

**原文链接**: [https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/](https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/)

生成摘要时出错

---

## 41. 60 Years Ago, a Submerged Submarine Circled the Globe for the First Time (2020)

**原文标题**: 60 Years Ago, a Submerged Submarine Circled the Globe for the First Time (2020)

**原文链接**: [https://www.popularmechanics.com/military/weapons/a32009109/operation-sandblast-sumbarine-circumnavigation/](https://www.popularmechanics.com/military/weapons/a32009109/operation-sandblast-sumbarine-circumnavigation/)

生成摘要时出错

---

## 42. Show HN: I was tired of opening 2 tabs for every HN link, so I made a userscript

**原文标题**: Show HN: I was tired of opening 2 tabs for every HN link, so I made a userscript

**原文链接**: [https://github.com/twalichiewicz/HNewhere](https://github.com/twalichiewicz/HNewhere)

生成摘要时出错

---

## 43. Interview with Boris Cherny [video]

**原文标题**: Interview with Boris Cherny [video]

**原文链接**: [https://www.youtube.com/watch?v=qyPCVqFUyDo](https://www.youtube.com/watch?v=qyPCVqFUyDo)

生成摘要时出错

---

## 44. Building an Affiliation Network for Blog Posts and Tags in Hugo

**原文标题**: Building an Affiliation Network for Blog Posts and Tags in Hugo

**原文链接**: [https://ohaodha.ie/blog/building-an-affiliation-network-for-blog-posts--tags-in-hugo/](https://ohaodha.ie/blog/building-an-affiliation-network-for-blog-posts--tags-in-hugo/)

生成摘要时出错

---

## 45. Using AI to Strengthen Learning, Not Replace It

**原文标题**: Using AI to Strengthen Learning, Not Replace It

**原文链接**: [https://studywisdom.co.uk/ai-study-strategies-choosing-tools-that-strengthen-learning/](https://studywisdom.co.uk/ai-study-strategies-choosing-tools-that-strengthen-learning/)

生成摘要时出错

---

## 46. Why We're Dropping Basecamp (2023)

**原文标题**: Why We're Dropping Basecamp (2023)

**原文链接**: [https://blogs.library.duke.edu/blog/2023/11/30/why-were-dropping-basecamp/](https://blogs.library.duke.edu/blog/2023/11/30/why-were-dropping-basecamp/)

生成摘要时出错

---

## 47. Shai-Hulud and the risks of external dependencies

**原文标题**: Shai-Hulud and the risks of external dependencies

**原文链接**: [https://scotto.me/blog/2026-07-29-shai-hulud-code-review/](https://scotto.me/blog/2026-07-29-shai-hulud-code-review/)

生成摘要时出错

---

## 48. Hooray for the Sockets Interface

**原文标题**: Hooray for the Sockets Interface

**原文链接**: [https://blog.apnic.net/2026/07/28/hooray-for-the-sockets-interface/](https://blog.apnic.net/2026/07/28/hooray-for-the-sockets-interface/)

生成摘要时出错

---

## 49. I'd not buy a LG monitor

**原文标题**: I'd not buy a LG monitor

**原文链接**: [https://beko.famkos.net/2026/07/27/id-not-buy-a-lg-monitor/](https://beko.famkos.net/2026/07/27/id-not-buy-a-lg-monitor/)

生成摘要时出错

---

## 50. Discovering Cryptographic Weaknesses with Claude

**原文标题**: Discovering Cryptographic Weaknesses with Claude

**原文链接**: [https://www.anthropic.com/research/discovering-cryptographic-weaknesses](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

生成摘要时出错

---

## 51. Simple sorting tool (CLI) in C++

**原文标题**: Simple sorting tool (CLI) in C++

**原文链接**: [https://github.com/metw0/qsort](https://github.com/metw0/qsort)

生成摘要时出错

---

## 52. Show HN: Tessera – tmux/Zellij ergonomics for macOS windows

**原文标题**: Show HN: Tessera – tmux/Zellij ergonomics for macOS windows

**原文链接**: [https://github.com/pa/tessera](https://github.com/pa/tessera)

生成摘要时出错

---

## 53. Show HN: A Persistent AI RPG Engine Built with React SPA and Supabase

**原文标题**: Show HN: A Persistent AI RPG Engine Built with React SPA and Supabase

**原文链接**: [https://vampirolife.com/en](https://vampirolife.com/en)

生成摘要时出错

---

## 54. An Android and iOS app from 7 Claude Code commands, every prompt and timing

**原文标题**: An Android and iOS app from 7 Claude Code commands, every prompt and timing

**原文链接**: [https://proandroiddev.com/seven-claude-code-commands-one-kotlin-multiplatform-app-on-android-and-ios-cb01e920a3e6](https://proandroiddev.com/seven-claude-code-commands-one-kotlin-multiplatform-app-on-android-and-ios-cb01e920a3e6)

生成摘要时出错

---

## 55. 7.1 Earthquake in Japan

**原文标题**: 7.1 Earthquake in Japan

**原文链接**: [https://www.data.jma.go.jp/multi/quake/quake_detail.html?eventID=20260728163528&lang=en](https://www.data.jma.go.jp/multi/quake/quake_detail.html?eventID=20260728163528&lang=en)

生成摘要时出错

---

## 56. What's That Burning Smell?

**原文标题**: What's That Burning Smell?

**原文链接**: [http://inthewilderness.net/2026/02/16/whats-that-burning-smell/](http://inthewilderness.net/2026/02/16/whats-that-burning-smell/)

生成摘要时出错

---

## 57. Half-Life ported to Mac OS 9

**原文标题**: Half-Life ported to Mac OS 9

**原文链接**: [https://mac-classic.com/news/half-life-ported-to-mac-os-9/](https://mac-classic.com/news/half-life-ported-to-mac-os-9/)

生成摘要时出错

---

## 58. Notes from a Burning Paris

**原文标题**: Notes from a Burning Paris

**原文链接**: [https://sarahwilson.substack.com/p/notes-from-a-burning-paris](https://sarahwilson.substack.com/p/notes-from-a-burning-paris)

生成摘要时出错

---

## 59. Teaching agents to predict and pre-execute their next tool call

**原文标题**: Teaching agents to predict and pre-execute their next tool call

**原文链接**: [https://arxiv.org/abs/2607.25816](https://arxiv.org/abs/2607.25816)

生成摘要时出错

---

## 60. Anthropeum – Where in the world, and when, does this human artifact belong?

**原文标题**: Anthropeum – Where in the world, and when, does this human artifact belong?

**原文链接**: [https://anthropeum.com/](https://anthropeum.com/)

生成摘要时出错

---

## 61. AI in Linux

**原文标题**: AI in Linux

**原文链接**: [https://drewdevault.com/blog/AI-in-Linux/](https://drewdevault.com/blog/AI-in-Linux/)

生成摘要时出错

---

## 62. A $500 RL fine-tune of a 9B open model beat frontier models on catalog review

**原文标题**: A $500 RL fine-tune of a 9B open model beat frontier models on catalog review

**原文链接**: [https://fermisense.com/when-machines-take-the-wheel/](https://fermisense.com/when-machines-take-the-wheel/)

生成摘要时出错

---

## 63. Kimi K3 Architecture Overview and Notes

**原文标题**: Kimi K3 Architecture Overview and Notes

**原文链接**: [https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html)

生成摘要时出错

---

## 64. DMARC has been public since 2012 but most company domains still don't enforce it

**原文标题**: DMARC has been public since 2012 but most company domains still don't enforce it

**原文链接**: [https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026](https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026)

生成摘要时出错

---

## 65. MCP 2026-07-28 Specification: transport going stateless

**原文标题**: MCP 2026-07-28 Specification: transport going stateless

**原文链接**: [https://blog.modelcontextprotocol.io/posts/2026-07-28/](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

生成摘要时出错

---

## 66. How Do I Profile eBPF Code?

**原文标题**: How Do I Profile eBPF Code?

**原文链接**: [https://naveensrinivasan.com/posts/2026-07-22-how-do-i-profile-ebpf-code/](https://naveensrinivasan.com/posts/2026-07-22-how-do-i-profile-ebpf-code/)

生成摘要时出错

---

## 67. Show HN: XY – A Fast, composable, GPU-accelerated interactive plotting library

**原文标题**: Show HN: XY – A Fast, composable, GPU-accelerated interactive plotting library

**原文链接**: [https://github.com/reflex-dev/xy](https://github.com/reflex-dev/xy)

生成摘要时出错

---

## 68. The Fabled Flatbreads of Uzbekistan (2015)

**原文标题**: The Fabled Flatbreads of Uzbekistan (2015)

**原文链接**: [https://www.aramcoworld.com/articles/2015/the-fabled-flatbreads-of-uzbekistan](https://www.aramcoworld.com/articles/2015/the-fabled-flatbreads-of-uzbekistan)

生成摘要时出错

---

## 69. Multiple Mouse Cursors in Wayland

**原文标题**: Multiple Mouse Cursors in Wayland

**原文链接**: [https://blinry.org/multi-seat-wayland/](https://blinry.org/multi-seat-wayland/)

生成摘要时出错

---

## 70. Beyond Greece and Rome

**原文标题**: Beyond Greece and Rome

**原文链接**: [https://aeon.co/essays/uncovering-a-global-ancient-history-beyond-greece-and-rome](https://aeon.co/essays/uncovering-a-global-ancient-history-beyond-greece-and-rome)

生成摘要时出错

---

## 71. Teach yourself programming in ten years (1998)

**原文标题**: Teach yourself programming in ten years (1998)

**原文链接**: [https://www.norvig.com/21-days.html](https://www.norvig.com/21-days.html)

生成摘要时出错

---

## 72. Google DeepMind dismantles AlphaFold team

**原文标题**: Google DeepMind dismantles AlphaFold team

**原文链接**: [https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33)

生成摘要时出错

---

## 73. Stop Killing the Internet: No Digital ID and No Age Verification

**原文标题**: Stop Killing the Internet: No Digital ID and No Age Verification

**原文链接**: [https://citizens-initiative.europa.eu/initiatives/details/2026/000011_en](https://citizens-initiative.europa.eu/initiatives/details/2026/000011_en)

生成摘要时出错

---

## 74. Mag Computer: A Mag History of RAM (1960–2025)

**原文标题**: Mag Computer: A Mag History of RAM (1960–2025)

**原文链接**: [https://magworld.pw/episodes/computer/](https://magworld.pw/episodes/computer/)

生成摘要时出错

---

## 75. About the security content of macOS Tahoe 26.6

**原文标题**: About the security content of macOS Tahoe 26.6

**原文链接**: [https://support.apple.com/en-us/128067](https://support.apple.com/en-us/128067)

生成摘要时出错

---

## 76. Show HN: PriEco (open source, 400M index, EU search engine) integrated Goggles

**原文标题**: Show HN: PriEco (open source, 400M index, EU search engine) integrated Goggles

**原文链接**: [https://prieco.net/](https://prieco.net/)

生成摘要时出错

---

## 77. Notes on Mythos Breaking AES

**原文标题**: Notes on Mythos Breaking AES

**原文链接**: [https://mkagenius.substack.com/p/notes-on-mythos-breaking-aes](https://mkagenius.substack.com/p/notes-on-mythos-breaking-aes)

生成摘要时出错

---

## 78. Google's Beyond Zero: Enterprise Security for the AI Era

**原文标题**: Google's Beyond Zero: Enterprise Security for the AI Era

**原文链接**: [https://spawn-queue.acm.org/doi/10.1145/3819083](https://spawn-queue.acm.org/doi/10.1145/3819083)

生成摘要时出错

---

## 79. Show HN: Vimgolf.ai – Learn Vim by playing through a map of levels

**原文标题**: Show HN: Vimgolf.ai – Learn Vim by playing through a map of levels

**原文链接**: [https://vimgolf.ai](https://vimgolf.ai)

生成摘要时出错

---

## 80. We identify visitors with no cookies, and the midnight UTC flaw

**原文标题**: We identify visitors with no cookies, and the midnight UTC flaw

**原文链接**: [https://zenovay.com/en/blog/cookieless-identity-midnight-utc/](https://zenovay.com/en/blog/cookieless-identity-midnight-utc/)

生成摘要时出错

---

## 81. Show HN: How far do I have to go to run into 100k people?

**原文标题**: Show HN: How far do I have to go to run into 100k people?

**原文链接**: [https://imjasonh.github.io/playground/population-rays/](https://imjasonh.github.io/playground/population-rays/)

生成摘要时出错

---

## 82. Chip stocks slide in US and Asia as AI jitters rattle investors

**原文标题**: Chip stocks slide in US and Asia as AI jitters rattle investors

**原文链接**: [https://www.bbc.com/news/articles/cly8zng43npo](https://www.bbc.com/news/articles/cly8zng43npo)

生成摘要时出错

---

## 83. These European airports now allow up to 2 litres of liquids in hand luggage

**原文标题**: These European airports now allow up to 2 litres of liquids in hand luggage

**原文链接**: [https://www.fly4free.com/flight-deals/europe/these-european-airports-now-allow-up-to-2-litres-of-liquids-in-hand-luggage/](https://www.fly4free.com/flight-deals/europe/these-european-airports-now-allow-up-to-2-litres-of-liquids-in-hand-luggage/)

生成摘要时出错

---

## 84. Pacing the frontier

**原文标题**: Pacing the frontier

**原文链接**: [https://www.pacingthefrontier.com/](https://www.pacingthefrontier.com/)

生成摘要时出错

---

## 85. Delayed Gratification – Proud to Be 'Last to Breaking News'

**原文标题**: Delayed Gratification – Proud to Be 'Last to Breaking News'

**原文链接**: [https://www.slow-journalism.com/](https://www.slow-journalism.com/)

生成摘要时出错

---

## 86. PwC published reports on AI marred by AI hallucinations

**原文标题**: PwC published reports on AI marred by AI hallucinations

**原文链接**: [https://www.ft.com/content/7e149ac8-2ce2-4266-8940-192f9821b33c](https://www.ft.com/content/7e149ac8-2ce2-4266-8940-192f9821b33c)

生成摘要时出错

---

## 87. Our position on open-weights models

**原文标题**: Our position on open-weights models

**原文链接**: [https://www.anthropic.com/news/position-open-weights-models](https://www.anthropic.com/news/position-open-weights-models)

生成摘要时出错

---

## 88. Does Your Home or Classroom Need an Air Purifier? Make a Corsi-Rosenthal Box

**原文标题**: Does Your Home or Classroom Need an Air Purifier? Make a Corsi-Rosenthal Box

**原文链接**: [https://www.npr.org/sections/back-to-school-live-updates/2021/08/26/1031018250/does-your-kids-classroom-need-an-air-purifier-heres-how-you-can-make-one-yoursel](https://www.npr.org/sections/back-to-school-live-updates/2021/08/26/1031018250/does-your-kids-classroom-need-an-air-purifier-heres-how-you-can-make-one-yoursel)

生成摘要时出错

---

## 89. Lightweight Spring Boot Monitoring Without Prometheus and Grafana

**原文标题**: Lightweight Spring Boot Monitoring Without Prometheus and Grafana

**原文链接**: [https://pvrlabs.xyz/articles/lightweight-spring-boot-monitoring.html](https://pvrlabs.xyz/articles/lightweight-spring-boot-monitoring.html)

生成摘要时出错

---

