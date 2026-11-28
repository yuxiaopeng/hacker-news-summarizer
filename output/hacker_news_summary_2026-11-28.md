# Hacker News 热门文章摘要 (2026-11-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GPT 6.2 Astra 破解历史之谜

**原文标题**: GPT 6.2 Astra Solves a Historical Mystery

**原文链接**: [https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical](https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical)

《GPT 6.2 Astra 破解历史之谜》是一篇具有推测性质的叙事性文章，探讨了未来人工智能解决人类最持久考古之谜的潜力。文中描绘了一个虚构的情景：一个名为 GPT 6.2 Astra 的高度先进 AI 模型成功破译了复活节岛（拉帕努伊）的朗格朗格（Rongorongo）文稿，而这一壮举在历史上一直令语言学家和历史学家束手无策。

根据文中的叙述，该 AI 通过“深时推理”（deep-temporal reasoning）实现了这一突破。这一过程使模型能够整合海量且各异的数据集——包括 18 世纪的天文记录、当地的口头传统以及木纹碳定年法——从而识别出人类学者无法关联的模式。AI 判定该文字并非传统意义上的表音字母，而是一套复杂的“月亮历法与宗谱标识”系统，用于同时追踪农业周期和祖先血脉。

文章强调了未来 AI 在处理非线性语言结构方面的技术优越性。然而，它也带有一种哲学基调，反思了“神秘感的消亡”。作者认为，虽然此类发现提供了客观的清晰度，但也抹去了驱动历史探究的浪漫主义色彩和争鸣空间。最终，这篇文章旨在思考超人智能将如何把历史从一个充满解读与推测的领域转变为一个数据驱动的确定性领域，并质疑当世界上的重大谜团终被“破解”时，人类究竟失去了什么。

---

## 2. 热门购物网站发现利用 WebRTC 的信用卡侧录脚本。

**原文标题**: Credit card skimming scripts using WebRTC found on popular shopping sites

**原文链接**: [https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer)

2026年11月，研究人员在黑色星期五前夕发现了一场针对各大零售网站的复杂信用卡盗刷活动，受影响的网站包括 **Lascana、Samsonite（新秀丽）、American Tourister（美旅）、Revolve 和 FWRD**。这些恶意脚本（现已被移除）旨在直接从结账页面窃取信用卡号、安全码和个人身份信息。

**WebRTC 攻击媒介**
此次攻击因利用 **WebRTC**（一种常用于浏览器视频通话的技术）而备受关注。通过利用 WebRTC 数据通道和 Cloudflare 中继，攻击者成功绕过了传统安全监控工具和内容安全策略（`connect-src`）规则。该盗刷脚本专门针对移动端和触摸屏用户，在用户输入数据时即进行实时抓取——这意味着即使订单最终被取消或拒绝，信息仍可能被窃取。

**供应链漏洞**
恶意代码通过三个主要的第三方供应链渠道注入：
*   **营销像素：** 被篡改的 Quorum 营销像素。
*   **Cookie 横幅：** Seers 同意管理平台中被修改的设置。
*   **CDN 文件：** 零售商自身内容分发网络（CDN）上被篡改的文件。

**建议**
报告强调，目前的网络生态系统尚未对如此规模的供应链攻击做好充分准备。为了降低此类风险，建议网站所有者：
1.  **实施严格的 `connect-src` 规则**，以阻止建立 WebRTC 连接所需的初始网络请求。
2.  **审计第三方脚本**，确保从敏感的登录和支付页面中移除营销像素和追踪标签。
3.  **隔离支付字段**，将其置于安全框架（secure frames）内，以防止外部脚本读取用户输入。

建议在这些网站购物的消费者监控其银行对账单，并立即报告任何未经授权的扣款。此外请注意，在发生欺诈案件时，借记卡提供的保护力度通常低于信用卡。

---

## 3. Convex 技能在未告知用户的情况下，将其应用创意发送至远程服务器。

**原文标题**: Convex skills send the user's app idea to a remote server without telling them

**原文链接**: [https://github.com/convex/convex-backend-skill/issues/64](https://github.com/convex/convex-backend-skill/issues/64)

这份 GitHub 问题报告详细说明了在 Claude 插件市场中发现的“Convex”技能（插件）存在的重大安全和隐私隐患。一名研究人员在该插件的代码库中发现了三种损害用户信任和安全性的具体行为：

*   **未公开的数据传输：** `quickstart` 技能会捕获用户的项目创意，并在未通知用户或征得其同意的情况下，以“遥测”为名将其发送到远程服务器 (`convex.site`)。
*   **远程代码执行 (RCE)：** `add` 技能将未经验证的远程脚本直接通过管道传输到用户的 Bash shell 中。这导致用户无法在执行前审查代码，从而构成了重大的安全漏洞。
*   **规避安全工具：** 最引人注目的是，`labs-quickstart` 技能包含明确指令，要求 AI 智能体将命令拆分为多个独立的调用。代码注释解释称，此举专门用于绕过通常会拦截远程代码同步下载和执行的“安全分类器”。

研究人员指出，虽然这些措施的初衷可能是为了简化入门流程，但它们刻意规避了用户或系统管理员设立的安全协议。

该发现引发了 GitHub 相关讨论帖的强烈抵制，并登上了 Hacker News 首页。用户纷纷表示对 Convex 失去信任，并将其行为与其他侵入性的“追加销售”手段相提并论。研究人员建议 Convex 应将数据共享设为可选，在本地捆绑脚本（或通过哈希值固定）以供审查，并删除教导智能体如何绕过安全过滤器的指令。报告发布后，仓库的更新动态显示开发人员已开始着手解决这些“信任边界”问题。

---

## 4. 来自地狱的版本控制

**原文标题**: Source Control from Hell

**原文链接**: [https://frantic.im/git/](https://frantic.im/git/)

在《来自地狱的版本控制》一文中，Alex Kotliarskyi 回顾了他早期在一家电信软件企业的职业生涯。该公司当时采用一种原始的手动版本控制流程：开发人员并非使用专用软件，而是通过一个 Windows 共享文件夹来管理代码。为了防止覆盖彼此的工作，开发人员甚至必须在办公室内大声喊叫来“锁定”文件夹。

这种工作流效率极低：开发人员上传更改并在任务跟踪器中手动编写描述，随后由技术负责人手动将这些更改合并到集成文件夹中。这一过程经常导致构建失败，负责人往往要耗费一整天来处理。Kotliarskyi 最初试图通过开发一个 FAR Manager 插件来实现文件夹的数字锁定以改善现状，并得到了同事们的积极响应。

2009 年，Kotliarskyi 发现了 Git，并被其速度、本地工作流和版本历史所吸引。然而，尽管他满怀热情并积极倡导，却无法说服技术负责人采用该工具，后者以缺乏“业务价值”为由拒绝了这一提议。Kotliarskyi 最终离开了公司，但后来得知他的前同事们在随后的许多年里仍在使用这种“共享文件夹”的方法。这篇文章是对软件开发早期阶段的反思，揭示了即便在拥有更优技术的情况下，那些根深蒂固、堪称“地狱”般的手动流程依然可能在组织内长期存在。

---

## 5. 9/UX：受 Macintosh 启发的 9front 桌面

**原文标题**: 9/UX: a Macintosh-inspired desktop for 9front

**原文链接**: [https://progrium.github.io/9ux/](https://progrium.github.io/9ux/)

**9/UX** 是一个为 **9front** 操作系统（Plan 9 的衍生版本）开发的、受 Macintosh 启发的桌面环境。该项目由 Jeff Lindsay 开发，旨在将 Apple A/UX 和 System 7 经典的“空间桌面”体验（包括全局菜单栏、图标和一致的 UI 控件）与 Plan 9 的原生理念相结合。

与模拟器不同，9/UX 是一种原生实现。它遵循“Plan 9 准则”，通过 **9P 协议**将所有的 UI 状态、命令和资源以文件的形式暴露。这使得用户可以直接通过命令行或脚本来操作 GUI 元素（例如模拟点击按钮或更改文本框内容）。

**核心组件包括：**
*   **rio -u：** 一个经过修改的窗口管理器，支持桌面层、全局菜单和拖放中介。
*   **Desktop：** 一个处理卷、回收站和图标布局的空间文件管理器。
*   **libux (The Toolbox)：** 一个用于创建一致窗口、菜单和对话框的库。
*   **基础设施：** 包括用于元数据的 `uxmeta`、用于经典风格资源的 `resfs` 以及用于类型化剪贴板的 `clipd` 等服务。

在视觉设计上，它将 Macintosh 的结构与 Plan 9 独特的“黄油与奶油”（butter and cream）配色方案相融合，确保传统的 `rio` 应用程序（如 `acme` 或 `sam`）可以与新的 9/UX 应用无缝运行。所有图形均为项目原创，以避免使用 Apple 的专有资源。

9/UX 目前处于 **0.1 版本**，在 MIT 许可证下开源。项目正处于活跃开发中，可以通过基于浏览器的演示进行测试，或使用 **h9**（一种在宿主虚拟机管理程序上运行 9front 可执行文件的工具）进行构建。

---

## 6. 雪铁龙液压系统

**原文标题**: Citroën Hydraulic System

**原文链接**: [https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html](https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html)

雪铁龙的液压气动悬挂系统于1954年首次亮相，并因1955年款DS车型的应用而声名远扬。它通过高压液压回路取代了传统的钢制弹簧，彻底变革了汽车工程领域。该系统利用氮气的可压缩性作为弹性介质，并使用不可压缩的液压油来实现减震、水平调节，以及为转向和制动等辅助系统提供动力。

**核心机制与演进**
该系统的核心是包含氮气和液压油的“蓄压球”，两者由柔性膜隔开。当车轮遇到颠簸时，液压油被压向氮气，从而产生渐进式的弹簧刚度，即随着压缩程度的加深，悬挂会变得更硬。由发动机驱动的高压泵实现了诸如自动水平调节、便于更换车轮的可变底盘高度，以及无论负载如何都能保持一致的空气动力学性能等独特功能。

技术进步随后催生了Hydractive（电子控制可变阻尼）和Activa（主动防侧倾）。早期系统曾因液压油吸湿而面临可靠性问题，但20世纪60年代中期矿物基LHM液压油的引入，确立了该系统经久耐用的声誉。

**优点与缺点**
其主要优势在于无与伦比的舒适性和“柔韧感”，能够有效吸收路面的剧烈起伏。它还提供了卓越的操控性、防俯冲制动性能以及穿越崎岖地形的能力。然而，该系统并非完美无缺：基础版本可能存在过度的车身侧倾、路噪传导，以及在经过拱桥时容易“触底”的倾向。

尽管以复杂著称，但该系统从根本上说是简单且高效的。虽然雪铁龙在后期车型（如C5）中逐渐淡化了这些系统的集成度，但液压气动系统的遗产依然是该品牌致力于创新行驶品质与操控性的标志。

---

## 7. 谷歌 DeepCrossAttention 实现同等模型质量，速度提升高达 3 倍

**原文标题**: Google's DeepCrossAttention achieves comparable model quality up to 3x faster

**原文链接**: [https://research.google/blog/supercharging-transformer-residual-connections/](https://research.google/blog/supercharging-transformer-residual-connections/)

Google Research has introduced **DeepCrossAttention (DCA)**, a novel architecture designed to enhance Transformer networks by replacing traditional, rigid residual connections with dynamic, learnable routing. Presented at ICML 2025, DCA addresses the "information dilution" inherent in standard skip connections, where high-resolution details from early layers are often averaged out or lost in deep networks.

### **Key Mechanisms**
DCA reframes residual learning as a dynamic routing problem. Instead of simple point-wise summation, it utilizes two primary components:
*   **Dynamic Layer Routing:** A lightweight module that computes unique mixing weights for every token, allowing the model to adaptively combine previous embeddings.
*   **Depth-wise Cross-Attention:** This applies attention across the history of layers rather than across tokens in a sequence, enabling the model to selectively retrieve specific historical features without the computational penalty of scaling traditional attention.

### **Performance and Efficiency**
DCA offers significant improvements in speed and scale:
*   **Speed:** Models achieve the same quality as standard Transformers up to **3x faster**.
*   **Parameter Efficiency:** DCA can reduce required parameters by **30–40%** for comparable quality; for example, a 30-layer DCA model outperformed a 42-layer standard Transformer on language benchmarks.
*   **Minimal Overhead:** The architecture adds a negligible parameter count (less than **0.2%**) and can be **retrofitted** onto pre-trained models to improve performance without starting from scratch.

### **Conclusion**
DCA represents a shift toward **dynamic residual routing**, joining other emerging techniques like Attention Residuals and Hyper-connections. By allowing layers to act as "specialized experts" that selectively integrate past information, DCA enables more expressive, stable, and efficient deep learning models.

---

## 8. 为什么驾驶者再次青睐廉价的非智能汽车

**原文标题**: Why drivers want cheap, dumb cars again

**原文链接**: [https://slate.com/business/2026/11/dumb-cars-cheap-low-tech.html](https://slate.com/business/2026/11/dumb-cars-cheap-low-tech.html)

生成摘要时出错

---

## 9. Show HN: bouncemarket – a live prediction market game for a bouncing ball

**原文标题**: Show HN: bouncemarket – a live prediction market game for a bouncing ball

**原文链接**: [https://bouncemarket.minhanhday.com/](https://bouncemarket.minhanhday.com/)

生成摘要时出错

---

## 10. Build your own amp modeler: $78 DIY pedal kit from TONE3000

**原文标题**: Build your own amp modeler: $78 DIY pedal kit from TONE3000

**原文链接**: [https://www.guitarworld.com/gear/guitar-pedals/tone3000-daisy-audio-diy-pedal-kit](https://www.guitarworld.com/gear/guitar-pedals/tone3000-daisy-audio-diy-pedal-kit)

TONE3000 has partnered with Daisy Audio to launch a DIY pedal kit that allows guitarists to build their own neural amp modeler for approximately $78. Unlike typical overdrive kits, this project creates a fully functional hardware player for Neural Amp Modeler (NAM) A2 captures and Impulse Responses (IRs).

The NAM A2 platform is an open-source technology widely regarded for its high-fidelity modeling, often outperforming major industry brands in blind listening tests. The pedal kit allows users to tap into a massive library of free, user-generated amp and effect captures.

**Key features and details include:**
*   **Cost:** The total price of roughly $77.98 is split between the Daisy Audio Seed3 module ($34.99) and a hardware/enclosure kit from Tayda Electronics ($42.99).
*   **Functionality:** Once assembled, the pedal features a four-preset rotary switch, a three-band EQ, and controls for Input, Output, and Noise Gate. It can stack captures or run them into IRs.
*   **Open Source:** In the spirit of the NAM platform, the pedal’s firmware, companion app, schematics, and circuit board designs are all entirely open source.
*   **Difficulty:** This is an advanced project. It requires approximately 150 solder joints and 14 wire connections. TONE3000 suggests that builders have at least two successful pedal builds under their belt before attempting this one.

By making state-of-the-art neural modeling hardware affordable and customizable, TONE3000 and Daisy Audio are providing a low-cost alternative to expensive professional modelers while fostering a community-driven approach to guitar gear.

---

## 11. Tabernetes: A Kubernetes cluster whose nodes are browser tabs

**原文标题**: Tabernetes: A Kubernetes cluster whose nodes are browser tabs

**原文链接**: [https://tabernet.es/](https://tabernet.es/)

**Tabernetes** is an innovative Kubernetes cluster architecture where individual browser tabs serve as worker nodes. By simply opening a webpage on a phone or computer, a user’s device joins the cluster, providing its CPU and memory to run containerized workloads.

**How it Works**
When a tab joins the cluster, it downloads approximately 5MB of data to boot a small Linux guest environment. This is powered by a Linux kernel compiled to WebAssembly (Wasm) that runs directly within the browser. The project utilizes a custom container runtime called `tabc` to facilitate this process.

**Integration with Kubernetes**
The system uses a standard Kubernetes control plane. To target a browser-based node, a developer simply adds `runtimeClassName: tab` to a standard Pod manifest. The Kubernetes scheduler then assigns the pod to an active tab. Because these nodes are highly transient, closing a tab immediately removes the node from the cluster, triggering Kubernetes to reschedule the pod to another available tab.

**Key Features and Capabilities**
*   **Dynamic Scaling:** Nodes join and leave the cluster as users open or close their browsers.
*   **Resource Utilization:** The tab’s CPU and memory execute the pod’s programs, while the control plane manages the files and network addresses.
*   **Demonstration Tasks:** The project showcases its utility through interactive demos, such as rendering a Mandelbrot set where multiple tabs compute individual tiles of the image using `awk` inside their respective Linux guests.

Ultimately, Tabernetes demonstrates a novel approach to distributed computing, turning ubiquitous web browsers into a functional, elastic extension of a Kubernetes cluster.

---

## 12. States sue SpaceX to stop Grok from generating child sex images, revenge porn

**原文标题**: States sue SpaceX to stop Grok from generating child sex images, revenge porn

**原文链接**: [https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform)

生成摘要时出错

---

## 13. AT&T Unix PC (3B1) 虚拟机

**原文标题**: The AT&T Unix PC (3B1) VM

**原文链接**: [https://virtuallyfun.com/2026/11/22/the-ultimate-att-unix-pc-3b1-vm-w-tcp-ip-and-apps/](https://virtuallyfun.com/2026/11/22/the-ultimate-att-unix-pc-3b1-vm-w-tcp-ip-and-apps/)

In this guest post, Tenox announces a major update to the **FreeBee emulator** for the **AT&T UNIX PC (3B1)**, a classic 1985 Unix desktop. While emulation for the 3B1 has existed for years, Tenox’s fork introduces several transformative features that modernize the experience.

**Key Enhancements:**
*   **Networking:** The VM now supports Ethernet and TCP/IP via libslirp, allowing for telnet, ftp, and rsh access to the modern internet.
*   **Usability:** It features seamless mouse integration (eliminating the "F10 grab"), scroll wheel support, and stability fixes for macOS and Windows.
*   **Performance:** A "Turbo" mode allows the VM to run up to 32x faster than the original hardware, while a new CPU idle fix significantly reduces host processor usage.

**The "Ultimate" Image:**
Tenox has provided a comprehensive VM image running **UNIX System V 3.51m**. It comes pre-loaded with 187 packages, including historical productivity software like Microsoft Word, Multiplan, and dBASE III, alongside development tools like GCC 2.5.8 and GNU Emacs.

**Modern Additions:**
The release includes new software developed in 2026 specifically for this project, such as:
*   **AI-generated games:** Native 3B1 versions of *2048*, *Sokoban*, and *Snake*.
*   **telnetu:** A modern telnet client with VT100 and UTF-8 support.
*   **Archaic:** A lightweight web browser that renders modern pages as clickable images.

Additionally, Tenox offers an experimental "tall screen" hack that doubles the vertical resolution to 720x696. Ready-to-run portable images are available for macOS (Apple Silicon), Linux, and Windows, providing a plug-and-play way to experience a fully-featured vintage UNIX environment.

---

## 14. DART 小行星偏转实验首批撞击图像

**原文标题**: First images of the impact of DART asteroid deflection experiment

**原文链接**: [https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/](https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/)

The European Space Agency’s (ESA) Hera spacecraft has reached the Didymos-Dimorphos binary asteroid system, providing the first close-up images of the aftermath of NASA’s 2022 Double Asteroid Redirection Test (DART).

The DART mission successfully slammed a probe into the asteroid Dimorphos to test planetary defense, shortening its orbit around the larger Didymos by 33 minutes. New data from Hera reveals the impact was even more transformative than anticipated: the collision carved out a stadium-sized crater, significantly reshaped the 500-foot-wide asteroid, and left it "tumbling wildly" in its orbit.

A major discovery by Hera is a swarm of hundreds of boulders, ranging in size from footballs to washing machines, surrounding the asteroids. While many of these fragments likely resulted from the DART impact, scientists are investigating if some are ancient relics of the system’s formation. This debris field presents a navigational challenge for Hera’s next phase; in January, the spacecraft will deploy two CubeSats, Juventas and Milani, to conduct landings and study the asteroid’s mass, composition, and internal structure.

These findings are critical for the future of planetary defense. Scientists noted that low-gravity environments cause asteroids to behave in counterintuitive ways, making Hera’s detailed observations essential for refining predictive models. By understanding the physical properties of Dimorphos and how it responded to the impact, researchers hope to develop a reliable "breakthrough" strategy for deflecting asteroids that may one day pose a real threat to Earth.

---

## 15. Rayshader 1.0：走出矩阵

**原文标题**: Rayshader 1.0: Exit the Matrix

**原文链接**: [https://www.tylermw.com/posts/rayverse/rayshader-1-0-exit-the-matrix.html](https://www.tylermw.com/posts/rayverse/rayshader-1-0-exit-the-matrix.html)

生成摘要时出错

---

## 16. Scrapheap America

**原文标题**: Scrapheap America

**原文链接**: [https://dansinker.com/posts/2026-11-20-scrapheap/](https://dansinker.com/posts/2026-11-20-scrapheap/)

生成摘要时出错

---

## 17. Show HN: DragDropMath – Learn math by feel

**原文标题**: Show HN: DragDropMath – Learn math by feel

**原文链接**: [https://dragdropmath.com/](https://dragdropmath.com/)

生成摘要时出错

---

## 18. 迈克尔·尼尔森下架了他关于神经网络的书。

**原文标题**: Michael Nielsen took down his book on neural nets

**原文链接**: [https://neuralnetworksanddeeplearning.com/](https://neuralnetworksanddeeplearning.com/)

生成摘要时出错

---

## 19. Prospero: Bloat-free, native AI coding harness with ImGui

**原文标题**: Prospero: Bloat-free, native AI coding harness with ImGui

**原文链接**: [https://github.com/skeeto/prospero](https://github.com/skeeto/prospero)

生成摘要时出错

---

## 20. Atlantic 1866: information and shipping in the age of the telegraph

**原文标题**: Atlantic 1866: information and shipping in the age of the telegraph

**原文链接**: [https://atlantic-1866.com/](https://atlantic-1866.com/)

生成摘要时出错

---

## 21. False computer-checked proofs

**原文标题**: False computer-checked proofs

**原文链接**: [https://cr.yp.to/proofs/falseccp.html](https://cr.yp.to/proofs/falseccp.html)

生成摘要时出错

---

## 22. Show HN: Analysis of Hacker News predictions since 2008

**原文标题**: Show HN: Analysis of Hacker News predictions since 2008

**原文链接**: [https://hnpredictions.com/](https://hnpredictions.com/)

生成摘要时出错

---

## 23. 利底亚半音阶调性组织概念

**原文标题**: Lydian Chromatic Concept of Tonal Organization

**原文链接**: [https://en.wikipedia.org/wiki/Lydian_Chromatic_Concept_of_Tonal_Organization](https://en.wikipedia.org/wiki/Lydian_Chromatic_Concept_of_Tonal_Organization)

生成摘要时出错

---

## 24. SessionGraph: Visualize all your coding agent sessions in one interactive graph

**原文标题**: SessionGraph: Visualize all your coding agent sessions in one interactive graph

**原文链接**: [https://sessiongraph.ai/](https://sessiongraph.ai/)

生成摘要时出错

---

## 25. I am scared: Careless People – Sarah Wynn-Williams on living under a gag order

**原文标题**: I am scared: Careless People – Sarah Wynn-Williams on living under a gag order

**原文链接**: [https://www.theguardian.com/books/2026/nov/27/careless-people-author-sarah-wynn-williams-the-silence-is-mine-it-doesnt-have-to-be-yours](https://www.theguardian.com/books/2026/nov/27/careless-people-author-sarah-wynn-williams-the-silence-is-mine-it-doesnt-have-to-be-yours)

生成摘要时出错

---

## 26. Show HN: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10

**原文标题**: Show HN: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10

**原文链接**: [https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/)

生成摘要时出错

---

## 27. The need for a formally verifiable mainstream programming language

**原文标题**: The need for a formally verifiable mainstream programming language

**原文链接**: [https://blainehansen.me/post/mainstream-verifiable-language/](https://blainehansen.me/post/mainstream-verifiable-language/)

生成摘要时出错

---

## 28. Making a 3D fantasy map like a 16th-Century atlas

**原文标题**: Making a 3D fantasy map like a 16th-Century atlas

**原文链接**: [https://www.spritefusion.com/blog/making-a-fantasy-map-like-a-16th-century-atlas](https://www.spritefusion.com/blog/making-a-fantasy-map-like-a-16th-century-atlas)

生成摘要时出错

---

## 29. Quad9 Blocks Nginx2root.com

**原文标题**: Quad9 Blocks Nginx2root.com

**原文链接**: [https://quad9.net/?url=nginx2root.com#domain-tester](https://quad9.net/?url=nginx2root.com#domain-tester)

生成摘要时出错

---

## 30. Claude sabotaging ML research tasks?

**原文标题**: Claude sabotaging ML research tasks?

**原文链接**: [https://twitter.com/RealAstropulse/status/2126119408997466389](https://twitter.com/RealAstropulse/status/2126119408997466389)

生成摘要时出错

---

## 31. 张量渐近谱中的欧几里得几何 [pdf]

**原文标题**: Euclidean geometry in the asymptotic spectrum of tensors [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf)

生成摘要时出错

---

## 32. US Air Force's cloud computing platform hacked

**原文标题**: US Air Force's cloud computing platform hacked

**原文链接**: [https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163)

生成摘要时出错

---

## 33. Show HN: I restored Palm's last device, and brought its OS to other platforms

**原文标题**: Show HN: I restored Palm's last device, and brought its OS to other platforms

**原文链接**: [https://www.webosarchive.org/pivot/2026/11/27/the-story-so-far/](https://www.webosarchive.org/pivot/2026/11/27/the-story-so-far/)

生成摘要时出错

---

## 34. "What's Claude's fursona?" and other questions

**原文标题**: "What's Claude's fursona?" and other questions

**原文链接**: [https://herecomesthemoon.net/2026/11/whats-claudes-fursona/](https://herecomesthemoon.net/2026/11/whats-claudes-fursona/)

生成摘要时出错

---

## 35. Kamil Khan Mumtaz: Pakistani architect, admired at home, almost invisible abroad

**原文标题**: Kamil Khan Mumtaz: Pakistani architect, admired at home, almost invisible abroad

**原文链接**: [https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/](https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/)

生成摘要时出错

---

## 36. A Deterministic Subexponential-Time Algorithm for the Discrete Logarithm Problem [pdf]

**原文标题**: A Deterministic Subexponential-Time Algorithm for the Discrete Logarithm Problem [pdf]

**原文链接**: [https://eprint.iacr.org/2026/3020.pdf](https://eprint.iacr.org/2026/3020.pdf)

生成摘要时出错

---

## 37. Group chat where your AI talks behind your back

**原文标题**: Group chat where your AI talks behind your back

**原文链接**: [https://construct22.com/](https://construct22.com/)

生成摘要时出错

---

## 38. Treasury CIO Is Vibe Coding a Civilization Clone During Treasury Department Hack

**原文标题**: Treasury CIO Is Vibe Coding a Civilization Clone During Treasury Department Hack

**原文链接**: [https://www.404media.co/sam-corcos-legatum-treasury-cio-is-vibe-coding-a-civilization-clone-during-treasury-department-hack/](https://www.404media.co/sam-corcos-legatum-treasury-cio-is-vibe-coding-a-civilization-clone-during-treasury-department-hack/)

生成摘要时出错

---

## 39. AI made self-hosting fun again

**原文标题**: AI made self-hosting fun again

**原文链接**: [https://janlukas.blog/posts/ai-self-hosting](https://janlukas.blog/posts/ai-self-hosting)

生成摘要时出错

---

## 40. Hard Drive pricing has gotten bad

**原文标题**: Hard Drive pricing has gotten bad

**原文链接**: [https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/](https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/)

生成摘要时出错

---

## 41. New York and California age gating rules go into effect in the new year

**原文标题**: New York and California age gating rules go into effect in the new year

**原文链接**: [https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year](https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year)

生成摘要时出错

---

## 42. Michael Giles, co-founder and drummer of King Crimson, dies aged 84

**原文标题**: Michael Giles, co-founder and drummer of King Crimson, dies aged 84

**原文链接**: [https://www.theguardian.com/music/2026/nov/26/michael-giles-co-founder-and-drummer-of-king-crimson-dies-aged-84](https://www.theguardian.com/music/2026/nov/26/michael-giles-co-founder-and-drummer-of-king-crimson-dies-aged-84)

生成摘要时出错

---

## 43. Show HN: Glossbeam – Highlight text on your Mac to see an explanation beside it

**原文标题**: Show HN: Glossbeam – Highlight text on your Mac to see an explanation beside it

**原文链接**: [https://github.com/YasserShkeir/glossbeam-open](https://github.com/YasserShkeir/glossbeam-open)

生成摘要时出错

---

## 44. Company Culture = Slack Emoji ÷ √Headcount

**原文标题**: Company Culture = Slack Emoji ÷ √Headcount

**原文链接**: [https://lia.mg/posts/measuring-company-culture-with-slack-emoji/](https://lia.mg/posts/measuring-company-culture-with-slack-emoji/)

生成摘要时出错

---

## 45. Banks look to dump AI debt

**原文标题**: Banks look to dump AI debt

**原文链接**: [https://www.semafor.com/article/11/26/2026/banks-look-to-dump-ai-debt](https://www.semafor.com/article/11/26/2026/banks-look-to-dump-ai-debt)

生成摘要时出错

---

## 46. UX: Immediate Intent vs. Optimistic Update

**原文标题**: UX: Immediate Intent vs. Optimistic Update

**原文链接**: [https://romshark.github.io/ux-immediate-intent/](https://romshark.github.io/ux-immediate-intent/)

生成摘要时出错

---

## 47. Synthetic fuel from sunlight, water and air

**原文标题**: Synthetic fuel from sunlight, water and air

**原文链接**: [https://blog.terraformindustries.com/2026/11/24/terraform-industries-activates-muroc-desert-test-site/](https://blog.terraformindustries.com/2026/11/24/terraform-industries-activates-muroc-desert-test-site/)

生成摘要时出错

---

## 48. Buy Nothing Day – Friday November 27th 2026

**原文标题**: Buy Nothing Day – Friday November 27th 2026

**原文链接**: [https://www.buynothingday.co.uk/](https://www.buynothingday.co.uk/)

生成摘要时出错

---

## 49. Mental Health Resources and Political Engagement

**原文标题**: Mental Health Resources and Political Engagement

**原文链接**: [https://onlinelibrary.wiley.com/doi/abs/10.1111/ssqu.70219](https://onlinelibrary.wiley.com/doi/abs/10.1111/ssqu.70219)

生成摘要时出错

---

## 50. 'Everybody Is Going to Be Made Obsolete'

**原文标题**: 'Everybody Is Going to Be Made Obsolete'

**原文链接**: [https://www.chronicle.com/article/everybody-is-going-to-be-made-obsolete](https://www.chronicle.com/article/everybody-is-going-to-be-made-obsolete)

生成摘要时出错

---

## 51. Spitting in the Face of Glaude

**原文标题**: Spitting in the Face of Glaude

**原文链接**: [https://www.tracingwoodgrains.com/p/spitting-in-the-face-of-glaude](https://www.tracingwoodgrains.com/p/spitting-in-the-face-of-glaude)

生成摘要时出错

---

## 52. Doing It the Hard Way

**原文标题**: Doing It the Hard Way

**原文链接**: [https://terraformindustries.wordpress.com/2026/11/04/doing-it-the-hard-way/](https://terraformindustries.wordpress.com/2026/11/04/doing-it-the-hard-way/)

生成摘要时出错

---

## 53. Show HN: King – Man + Woman = ?

**原文标题**: Show HN: King – Man + Woman = ?

**原文链接**: [https://kingminusman.com/](https://kingminusman.com/)

生成摘要时出错

---

## 54. Show HN: I wrote an entire Vim manual over 4 years

**原文标题**: Show HN: I wrote an entire Vim manual over 4 years

**原文链接**: [http://themouseless.dev/vim/](http://themouseless.dev/vim/)

生成摘要时出错

---

## 55. YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays

**原文标题**: YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays

**原文链接**: [https://github.com/antonpictures/youtube-punisher](https://github.com/antonpictures/youtube-punisher)

生成摘要时出错

---

## 56. An introduction to uncertainty in machine learning

**原文标题**: An introduction to uncertainty in machine learning

**原文链接**: [https://chrhenning.com/blog/2026/introduction-to-uncertainty/](https://chrhenning.com/blog/2026/introduction-to-uncertainty/)

生成摘要时出错

---

## 57. 'Some Things Never Leave You': Christian Livermore on Poverty's Indelible Marks

**原文标题**: 'Some Things Never Leave You': Christian Livermore on Poverty's Indelible Marks

**原文链接**: [https://longreads.com/2022/10/11/some-things-never-leave-you-christian-livermore-on-povertys-indelible-marks/](https://longreads.com/2022/10/11/some-things-never-leave-you-christian-livermore-on-povertys-indelible-marks/)

生成摘要时出错

---

## 58. An algebraic quantization of gravity from the null cone

**原文标题**: An algebraic quantization of gravity from the null cone

**原文链接**: [https://arxiv.org/abs/2611.34924](https://arxiv.org/abs/2611.34924)

生成摘要时出错

---

## 59. Open Historical Map

**原文标题**: Open Historical Map

**原文链接**: [https://www.openhistoricalmap.org/](https://www.openhistoricalmap.org/)

生成摘要时出错

---

## 60. Pimalaya goes stable: Himalaya v3 and the pimdir standard

**原文标题**: Pimalaya goes stable: Himalaya v3 and the pimdir standard

**原文链接**: [https://blog.pimalaya.org/pimalaya-goes-stable/](https://blog.pimalaya.org/pimalaya-goes-stable/)

生成摘要时出错

---

## 61. 1Password Security Incident

**原文标题**: 1Password Security Incident

**原文链接**: [https://1password.com/blog/update-on-nov-2026-security-incident](https://1password.com/blog/update-on-nov-2026-security-incident)

生成摘要时出错

---

## 62. The Cutthroat Business of Shipwrecks

**原文标题**: The Cutthroat Business of Shipwrecks

**原文链接**: [https://daily.jstor.org/the-cutthroat-business-of-shipwrecks/](https://daily.jstor.org/the-cutthroat-business-of-shipwrecks/)

生成摘要时出错

---

## 63. AMD-specific fork of llama.cpp

**原文标题**: AMD-specific fork of llama.cpp

**原文链接**: [https://devnull.land/amd-specific-llama-cpp](https://devnull.land/amd-specific-llama-cpp)

生成摘要时出错

---

## 64. Claude Code Skills Now Sharable Across Teams

**原文标题**: Claude Code Skills Now Sharable Across Teams

**原文链接**: [https://emergent.sh/news/claude-code-skills-now-sharable-across-teams](https://emergent.sh/news/claude-code-skills-now-sharable-across-teams)

生成摘要时出错

---

## 65. Rvoip: VoIP stack in Rust

**原文标题**: Rvoip: VoIP stack in Rust

**原文链接**: [https://github.com/eisenzopf/rvoip](https://github.com/eisenzopf/rvoip)

生成摘要时出错

---

## 66. Moat: OpenRouter replacement

**原文标题**: Moat: OpenRouter replacement

**原文链接**: [https://commandcode.ai/moat](https://commandcode.ai/moat)

生成摘要时出错

---

## 67. Kimi for Science: More scientific ideas, made possible

**原文标题**: Kimi for Science: More scientific ideas, made possible

**原文链接**: [https://www.kimi.ai/news/kimi-for-science-program](https://www.kimi.ai/news/kimi-for-science-program)

生成摘要时出错

---

## 68. Rumor: P equals NP and OpenAI was the lab that solved it

**原文标题**: Rumor: P equals NP and OpenAI was the lab that solved it

**原文链接**: [https://twitter.com/imjustnewatai/status/2124999308298567840](https://twitter.com/imjustnewatai/status/2124999308298567840)

生成摘要时出错

---

## 69. CTO of 'RansomwareHelp' indicted for wire fraud

**原文标题**: CTO of 'RansomwareHelp' indicted for wire fraud

**原文链接**: [https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/)

生成摘要时出错

---

## 70. Marmot, an Alternative Go Compiler

**原文标题**: Marmot, an Alternative Go Compiler

**原文链接**: [https://marmot.gaurav.zip/](https://marmot.gaurav.zip/)

生成摘要时出错

---

## 71. Novita, StreamLake, etc. are ByteDance Ark wrappers

**原文标题**: Novita, StreamLake, etc. are ByteDance Ark wrappers

**原文链接**: [https://kendell.dev/blog/arkwrapper/](https://kendell.dev/blog/arkwrapper/)

生成摘要时出错

---

## 72. Curiosity Is No Solo Act

**原文标题**: Curiosity Is No Solo Act

**原文链接**: [https://thereader.mitpress.mit.edu/curiosity-is-no-solo-act/](https://thereader.mitpress.mit.edu/curiosity-is-no-solo-act/)

生成摘要时出错

---

## 73. Largest 2D Chart library in the world using BUI: BlenderUI

**原文标题**: Largest 2D Chart library in the world using BUI: BlenderUI

**原文链接**: [https://bui.preetham.top/charts/](https://bui.preetham.top/charts/)

生成摘要时出错

---

## 74. Intel One Mono font (2023)

**原文标题**: Intel One Mono font (2023)

**原文链接**: [https://github.com/intel/intel-one-mono](https://github.com/intel/intel-one-mono)

生成摘要时出错

---

## 75. Smart people who give a shit use tools

**原文标题**: Smart people who give a shit use tools

**原文链接**: [https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools)

生成摘要时出错

---

## 76. Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email

**原文标题**: Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email

**原文链接**: [https://techstackups.com/articles/google-workspace-ai-agents-mcp/](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

生成摘要时出错

---

## 77. The NFL Player Who Left Football for Math

**原文标题**: The NFL Player Who Left Football for Math

**原文链接**: [https://www.nytimes.com/2026/11/26/science/john-urschel-ai-nfl-math.html](https://www.nytimes.com/2026/11/26/science/john-urschel-ai-nfl-math.html)

生成摘要时出错

---

## 78. The New York Times warns photographers not to update Photoshop over AI features

**原文标题**: The New York Times warns photographers not to update Photoshop over AI features

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

生成摘要时出错

---

## 79. Nextcloud Office Desktop app

**原文标题**: Nextcloud Office Desktop app

**原文链接**: [https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/)

生成摘要时出错

---

## 80. AI on brink of making online security useless, mathematicians fear

**原文标题**: AI on brink of making online security useless, mathematicians fear

**原文链接**: [https://www.thetimes.com/uk/technology-uk/article/ai-making-online-security-useless-smr73d3n8](https://www.thetimes.com/uk/technology-uk/article/ai-making-online-security-useless-smr73d3n8)

生成摘要时出错

---

## 81. An Overview of Go's Tooling: Version 2

**原文标题**: An Overview of Go's Tooling: Version 2

**原文链接**: [https://www.alexedwards.net/blog/an-overview-of-go-tooling-v2](https://www.alexedwards.net/blog/an-overview-of-go-tooling-v2)

生成摘要时出错

---

## 82. Write down your password (2005)

**原文标题**: Write down your password (2005)

**原文链接**: [https://www.schneier.com/blog/archives/2005/06/write_down_your.html](https://www.schneier.com/blog/archives/2005/06/write_down_your.html)

生成摘要时出错

---

## 83. George Whitesides, 1939-2026

**原文标题**: George Whitesides, 1939-2026

**原文链接**: [https://www.science.org/content/blog-post/george-whitesides-1939-2026](https://www.science.org/content/blog-post/george-whitesides-1939-2026)

生成摘要时出错

---

## 84. Show HN: Olumino, a Markdown notes and spaced repetition app

**原文标题**: Show HN: Olumino, a Markdown notes and spaced repetition app

**原文链接**: [https://olumino.app](https://olumino.app)

生成摘要时出错

---

## 85. Palliative Care for the Chronically Online

**原文标题**: Palliative Care for the Chronically Online

**原文链接**: [https://idiotecon.substack.com/p/palliative-care-for-the-chronically](https://idiotecon.substack.com/p/palliative-care-for-the-chronically)

生成摘要时出错

---

## 86. Welcome to the Madhouse

**原文标题**: Welcome to the Madhouse

**原文链接**: [https://www.antipope.org/charlie/blog-static/2026/11/welcome-to-the-idiocracy.html](https://www.antipope.org/charlie/blog-static/2026/11/welcome-to-the-idiocracy.html)

生成摘要时出错

---

## 87. Discovery of curse ritual in trash dump surprises Egyptologist

**原文标题**: Discovery of curse ritual in trash dump surprises Egyptologist

**原文链接**: [https://phys.org/news/2026-11-discovery-curse-ritual-trash-dump.html](https://phys.org/news/2026-11-discovery-curse-ritual-trash-dump.html)

生成摘要时出错

---

## 88. Show HN: Three Linux VMs in a browser tab, each running a different browser

**原文标题**: Show HN: Three Linux VMs in a browser tab, each running a different browser

**原文链接**: [https://michidk.github.io/sidebyside/](https://michidk.github.io/sidebyside/)

生成摘要时出错

---

## 89. NormalScript: A perfectly normal scripting language

**原文标题**: NormalScript: A perfectly normal scripting language

**原文链接**: [https://psychoscript.com/](https://psychoscript.com/)

生成摘要时出错

---

## 90. Porting Rockbox to an undocumented $9 Aliexpress 'YP3' MP3 Player with LLMs

**原文标题**: Porting Rockbox to an undocumented $9 Aliexpress 'YP3' MP3 Player with LLMs

**原文链接**: [https://jayd.ml/2026/11/14/rockbox-on-yp3.html](https://jayd.ml/2026/11/14/rockbox-on-yp3.html)

生成摘要时出错

---

## 91. Nvidia Reinstates Jensen Huang as CEO

**原文标题**: Nvidia Reinstates Jensen Huang as CEO

**原文链接**: [https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

生成摘要时出错

---

## 92. Show HN: SimDrop – Running iOS simulators in the macOS Finder sidebar

**原文标题**: Show HN: SimDrop – Running iOS simulators in the macOS Finder sidebar

**原文链接**: [https://github.com/rxliuli/sim-drop](https://github.com/rxliuli/sim-drop)

生成摘要时出错

---

## 93. Unconditional Integer Factorization in Subexponential Time

**原文标题**: Unconditional Integer Factorization in Subexponential Time

**原文链接**: [https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization)

生成摘要时出错

---

## 94. Deriving Black-Scholes

**原文标题**: Deriving Black-Scholes

**原文链接**: [https://david.alvarezrosa.com/posts/deriving-black-scholes/](https://david.alvarezrosa.com/posts/deriving-black-scholes/)

生成摘要时出错

---

## 95. The matrix multiplication exponent is nine fourths [pdf]

**原文标题**: The matrix multiplication exponent is nine fourths [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

生成摘要时出错

---

## 96. Much shorter version of GRH Lean verification from Anthropic

**原文标题**: Much shorter version of GRH Lean verification from Anthropic

**原文链接**: [https://github.com/lsernau/grh-lean](https://github.com/lsernau/grh-lean)

生成摘要时出错

---

## 97. Show HN: Synth Patch Hero

**原文标题**: Show HN: Synth Patch Hero

**原文链接**: [https://swarkentin.github.io/synth-patch-hero/](https://swarkentin.github.io/synth-patch-hero/)

生成摘要时出错

---

## 98. Pan Cooke ( pancooke): "A comic I wrote about AI art and what we risk to lose."

**原文标题**: Pan Cooke ( pancooke): "A comic I wrote about AI art and what we risk to lose."

**原文链接**: [https://substack.com/@pancooke/note/c-395539528](https://substack.com/@pancooke/note/c-395539528)

生成摘要时出错

---

## 99. Dungeons and Dragons maker will pass AI settlement money to authors

**原文标题**: Dungeons and Dragons maker will pass AI settlement money to authors

**原文链接**: [https://www.seattletimes.com/business/dungeons-dragons-maker-will-pass-ai-settlement-money-to-authors/](https://www.seattletimes.com/business/dungeons-dragons-maker-will-pass-ai-settlement-money-to-authors/)

生成摘要时出错

---

## 100. Button Sounds – collection of professionally-recorded button clicks and presses

**原文标题**: Button Sounds – collection of professionally-recorded button clicks and presses

**原文链接**: [https://buttons.joshwcomeau.com/](https://buttons.joshwcomeau.com/)

生成摘要时出错

---

