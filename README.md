# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-28.md)

*最后自动更新时间: 2026-11-28 00:47:03*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-28](output/hacker_news_summary_2026-11-28.md) |
| 2 | [2026-11-25](output/hacker_news_summary_2026-11-25.md) |
| 3 | [2026-11-26](output/hacker_news_summary_2026-11-26.md) |
| 4 | [2026-11-27](output/hacker_news_summary_2026-11-27.md) |
| 5 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 6 | [2026-11-24](output/hacker_news_summary_2026-11-24.md) |
| 7 | [2026-11-22](output/hacker_news_summary_2026-11-22.md) |
| 8 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 9 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 10 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 11 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 12 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 13 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 14 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 15 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 16 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 17 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 18 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 19 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 20 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 21 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 22 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 23 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 24 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 25 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 26 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 27 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 28 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 29 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 30 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 31 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 32 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 33 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 34 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 35 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 36 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 37 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 38 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 39 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 40 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 41 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 42 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 43 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 44 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 45 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 46 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 47 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 48 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 49 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 50 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 51 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 52 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 53 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 54 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 55 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 56 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 57 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 58 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 59 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 60 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 61 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 62 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 63 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 64 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 65 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 66 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 67 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 68 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 69 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 70 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 71 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 72 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 73 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 74 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 75 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 76 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 77 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 78 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 79 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 80 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 81 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 82 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 83 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 84 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 85 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 86 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 87 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 88 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 89 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 90 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 91 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 92 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 93 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 94 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 95 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 96 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 97 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 98 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 99 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 100 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 101 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 102 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 103 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 104 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 105 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 106 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 107 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 108 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 109 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 110 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 111 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 112 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 113 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 114 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 115 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 116 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 117 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 118 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 119 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 120 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 121 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 122 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 123 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 124 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 125 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 126 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 127 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 128 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 129 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 130 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 131 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 132 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 133 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 134 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 135 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 136 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 137 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 138 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 139 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 140 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 141 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 142 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 143 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 144 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 145 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 146 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 147 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 148 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 149 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 150 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 151 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 152 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 153 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 154 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 155 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 156 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 157 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 158 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 159 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 160 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 161 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 162 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 163 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 164 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 165 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 166 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 167 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 168 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 169 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 170 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 171 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 172 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 173 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 174 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 175 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 176 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 177 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 178 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 179 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 180 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 181 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 182 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 183 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 184 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 185 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 186 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 187 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 188 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 189 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 190 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 191 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 192 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 193 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 194 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 195 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 196 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 197 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 198 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 199 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 200 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 201 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 202 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 203 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 204 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 205 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 206 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 207 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 208 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 209 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 210 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 211 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 212 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 213 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 214 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 215 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 216 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 217 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 218 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 219 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 220 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 221 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 222 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 223 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 224 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 225 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 226 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 227 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 228 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 229 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 230 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 231 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 232 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 233 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 234 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 235 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 236 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 237 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 238 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 239 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 240 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 241 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 242 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 243 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 244 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 245 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 246 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 247 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 248 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 249 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 250 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 251 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 252 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 253 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 254 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 255 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 256 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 257 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 258 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 259 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 260 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 261 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 262 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 263 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 264 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 265 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 266 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 267 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 268 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 269 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 270 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 271 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 272 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 273 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 274 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 275 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 276 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 277 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 278 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 279 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 280 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 281 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 282 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 283 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 284 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 285 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 286 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 287 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 288 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 289 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 290 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 291 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 292 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 293 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 294 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 295 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 296 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 297 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 298 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 299 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 300 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 301 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 302 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 303 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 304 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 305 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 306 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 307 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 308 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 309 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 310 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 311 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 312 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 313 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 314 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 315 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 316 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 317 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 318 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 319 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 320 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 321 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 322 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 323 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 324 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 325 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 326 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 327 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 328 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 329 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 330 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 331 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 332 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 333 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 334 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 335 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 336 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 337 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 338 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 339 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 340 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 341 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 342 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 343 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 344 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 345 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 346 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 347 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 348 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 349 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 350 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 351 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 352 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 353 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 354 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 355 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 356 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 357 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 358 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 359 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 360 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 361 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 362 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 363 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 364 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 365 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 366 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 367 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 368 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 369 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 370 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 371 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 372 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 373 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 374 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 375 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 376 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 377 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 378 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 379 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 380 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 381 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 382 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 383 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 384 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 385 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 386 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 387 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 388 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 389 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 390 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 391 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 392 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 393 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 394 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 395 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 396 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 397 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 398 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 399 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 400 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 401 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 402 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 403 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 404 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 405 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 406 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 407 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 408 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 409 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 410 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 411 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 412 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 413 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 414 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 415 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 416 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 417 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 418 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 419 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 420 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 421 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 422 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 423 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 424 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 425 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 426 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 427 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 428 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 429 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 430 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 431 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 432 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 433 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 434 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 435 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 436 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 437 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 438 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 439 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 440 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 441 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 442 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 443 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 444 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 445 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 446 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 447 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 448 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 449 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 450 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 451 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 452 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 453 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 454 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 455 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 456 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 457 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 458 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 459 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 460 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 461 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 462 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 463 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 464 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 465 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 466 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 467 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 468 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 469 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 470 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 471 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 472 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 473 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 474 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 475 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 476 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 477 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 478 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 479 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 480 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 481 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 482 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 483 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 484 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 485 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 486 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 487 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 488 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 489 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 490 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 491 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 492 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 493 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 494 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 495 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 496 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 497 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 498 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 499 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 500 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 501 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 502 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 503 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 504 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 505 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 506 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 507 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 508 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 509 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 510 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 511 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 512 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 513 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 514 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 515 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 516 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 517 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 518 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 519 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 520 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 521 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 522 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 523 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 524 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 525 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 526 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 527 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 528 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 529 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 530 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 531 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 532 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 533 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 534 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 535 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 536 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 537 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 538 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 539 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 540 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 541 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 542 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 543 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 544 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 545 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 546 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 547 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 548 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 549 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 550 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 551 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 552 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 553 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 554 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 555 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 556 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 557 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 558 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 559 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 560 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 561 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 562 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 563 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 564 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 565 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 566 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 567 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 568 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 569 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 570 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 571 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 572 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 573 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 574 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 575 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 576 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 577 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 578 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 579 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 580 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 581 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 582 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 583 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 584 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 585 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 586 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 587 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 588 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 589 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 590 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 591 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 592 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 593 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 594 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 595 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 596 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 597 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 598 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 599 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 600 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 601 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 602 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 603 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 604 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 605 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 606 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 607 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 608 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 609 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 610 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 611 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 612 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
