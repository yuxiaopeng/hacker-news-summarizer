# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-05.md)

*最后自动更新时间: 2025-11-05 17:52:07*
## 1. 潜藏在公式中的阴影

**原文标题**: The shadows lurking in the equations

**原文链接**: [https://gods.art/articles/equation_shadows.html](https://gods.art/articles/equation_shadows.html)

本文介绍了一种新的方程可视化方法“模糊图”(FuzzyGraph)，它超越了传统的二元（黑白）方法，即只显示方程完全成立的位置。相反，FuzzyGraph采用非二元方法来可视化“误差”或与等式的偏差，从而揭示隐藏在方程表面之下的“数学阴影”。

本文使用多个例子来说明FuzzyGraph的强大功能。这些例子表明，FuzzyGraph可以揭示传统图形中完全不可见的“黑洞”（高误差区域）、“阴影线”和“水下岛屿”（近解区域）。

“Slash Dot方程”和“类星体方程”等示例展示了FuzzyGraph如何暴露方程失效的区域，从而更全面地了解其行为。“简单星和黑洞”示例进一步阐明了可视化表示误差的概念。“阴影线”和“Phi方程”示例说明了除法如何产生先前可见元素的“阴影”。最后，“水下岛屿”示例展示了FuzzyGraph如何揭示方程的近解，然后可以对其进行调整以成为实际解，从而突出了发现隐藏关系的可能性。

本质上，FuzzyGraph通过揭示传统图形遗漏的底层数学地形，提供了一种更细致和信息丰富的方程可视化方法，从而更深入地了解方程的行为和潜在的解决方案。

---

## 2. 一个eBPF漏洞：使用XDP处理出口流量

**原文标题**: An eBPF Loophole: Using XDP for Egress Traffic

**原文链接**: [https://loopholelabs.io/blog/xdp-for-egress-traffic](https://loopholelabs.io/blog/xdp-for-egress-traffic)

本文详细介绍了一种使用XDP（eXpress Data Path）处理Linux出口流量的新技术，克服了其传统上仅限于入口流量的局限性。其核心思想是利用虚拟以太网（veth）接口的行为。通过将出站流量路由到veth对的一端，另一端将其视为入站流量，从而允许附加到该接口的XDP程序处理数据包。

作者强调了现有出口流量解决方案（如Traffic Control (TC)）由于其在网络堆栈中运行较晚而存在的性能限制，并将其与XDP的早期、零拷贝数据包处理进行了对比。

该实现涉及解决校验和计算和ARP解析问题，这些职责通常由内核处理，但在直接使用XDP时会被绕过。作者提供了代码片段，演示如何在XDP程序中执行增量校验和更新并管理ARP表。

基准测试比较了iptables、TC和他们基于XDP的技术，结果显示性能显著提升，在使用原生XDP驱动程序时实现了接近线路速率的速度（194Gbps），性能分别是iptables的12.4倍和TC的9.2倍。这种改进源于绕过了内核的网络堆栈。

作者强调了该技术在容器网络中的直接适用性。由于容器已经使用veth对，因此该解决方案可以作为直接替代方案来实现，绕过iptables和连接跟踪以实现更快的包路由。 主要用例是实时迁移，从而能够以线路速率透明地重新路由连接。

---

## 3. 从失败中学习，以解决难题

**原文标题**: Learning from failure to tackle hard problems

**原文链接**: [https://blog.ml.cmu.edu/2025/10/27/learning-from-failure-to-tackle-extremely-hard-problems/](https://blog.ml.cmu.edu/2025/10/27/learning-from-failure-to-tackle-extremely-hard-problems/)

卡内基梅隆大学机器学习博客文章强调了从失败中学习的重要性，认为这是解决机器学习研究中极难问题的关键。文章建议，承认和分析失败，而不是仅仅关注成功，能够为改进方法和确定新方向提供宝贵的见解。该博客可能深入探讨了研究人员如何有效地从不成功的实验和模型尝试中提取可操作的信息。

虽然在没有全文的情况下无法获得文章的具体细节，但它可能强调了分析失败的方法，例如：

* **严格的实验设计和文档记录：** 确保对失败进行充分记录并具有可重复性，从而可以准确诊断根本原因。
* **事后分析：** 涉及对实验或模型构建过程进行彻底审查，以找出弱点、有缺陷的假设或未预见的挑战。
* **迭代改进：** 利用从失败中获得的知识来调整参数、修改算法或在后续尝试中探索替代方法。

从其对教育内容的关注来看，该文章很可能提出了具体的例子或案例研究，其中从失败中学习导致了在解决困难的机器学习问题方面的重大突破。它旨在鼓励一种拥抱失败的文化，将其作为 ML@CMU 研究社区内外进步的必要阶梯。它提倡这样一种观点，即理解*为什么*某些事情失败，通常与知道*某些事情有效*一样，甚至更有价值。

---

## 4. Ruby及其邻居：Smalltalk

**原文标题**: Ruby and Its Neighbors: Smalltalk

**原文链接**: [https://noelrappin.com/blog/2025/11/ruby-and-its-neighbors-smalltalk/](https://noelrappin.com/blog/2025/11/ruby-and-its-neighbors-smalltalk/)

本文探讨了Smalltalk对编程语言，特别是Ruby的历史和影响。虽然Smalltalk的语法没有直接移植到Ruby，但其对象模型深刻影响了Ruby的设计。

作者提供了Smalltalk的个人历史，重点介绍了它在施乐PARC的起源，以及窗口界面和以太网等发明。Smalltalk在80年代和90年代获得了商业上的成功，并在航空等行业中得到应用。开源版本Squeak以其自托管架构而创新，主要用Smalltalk本身编写。

Smalltalk与许多现代语言的区别在于它独立于Unix和C，更像是一个独立的操作系统。开发环境与语言紧密集成，具有用于代码编辑和导航的工作区（REPL）和浏览器。浏览器允许完全访问系统的源代码和修改功能。

Smalltalk的语法很简单，围绕对象之间的消息传递构建，包括一元、二元和关键字消息。本文演示了即使是基本操作也依赖于这些消息结构。

本文强调了Smalltalk集成环境的强大功能，尤其是在测试和调试方面。作者感叹，Smalltalk环境的包罗万象虽然是一个优势，但最终导致了它的衰落，因为世界转向了基于Unix的系统。然而，Smalltalk的面向对象原则继续在像Ruby这样的现代语言中产生共鸣。

---

## 5. QUIC的P2P愿景 (2024)

**原文标题**: A P2P Vision for QUIC (2024)

**原文链接**: [https://seemann.io/posts/2024-10-26---p2p-quic/](https://seemann.io/posts/2024-10-26---p2p-quic/)

QUIC的P2P愿景：利用QUIC简化P2P网络中的NAT穿透

本文《QUIC的P2P愿景》探讨了如何利用QUIC简化并改进点对点（P2P）网络中的NAT穿透，而传统上这由STUN、ICE和TURN等复杂协议处理。作者建议利用QUIC的连接迁移和地址发现机制来替代这些较旧的方法。

传统方法包括：
*   **STUN：** 发现NAT后的公共IP地址。
*   **ICE：** 协调打洞，即对等方同时发送数据包以“穿透”其NAT。
*   **TURN：** 当直接连接失败时，通过第三方服务器中继流量。

基于QUIC的方法提供了一种更集成的解决方案：
*   **QUIC地址发现：** 通过使用新的`OBSERVED_ADDRESS`帧在QUIC连接中交换观察到的地址来替换STUN。
*   **通过连接迁移进行打洞：** 利用QUIC的连接迁移机制（专为无缝网络切换而设计）发送探测数据包（`PATH_CHALLENGE`和`PATH_RESPONSE`）进行打洞。需要一个新的`PUNCH_ME_NOW`帧进行协调。
*   **使用HTTP代理进行中继：** 当直接连接不可能时，使用基于QUIC的HTTP代理来中继UDP数据包。这利用了`HTTP Datagrams`，它们是QUIC `DATAGRAM`帧的薄包装。

作者认为，QUIC的加密、集成的地址发现和现有的连接迁移功能为P2P NAT穿透提供了一种比传统STUN/ICE/TURN方法更安全、高效且可能更简单的替代方案。 虽然像`ADD_ADDRESS`和`PUNCH_ME_NOW`这样的新QUIC帧会引发有关欺骗的安全问题，但可以通过适当的防御措施来缓解这些问题。

---

## 6. 蒂夫先生

**原文标题**: Mr TIFF

**原文链接**: [https://inventingthefuture.ghost.io/mr-tiff/](https://inventingthefuture.ghost.io/mr-tiff/)

约翰·巴克，《发明未来》的作者，讲述了他锲而不舍地探寻标签图像文件格式（TIFF）幕后真人的故事。巴克的使命是褒奖实际发明软硬件的个人，而非仅将成就归功于公司。在研究AIFF音频标准时，史蒂夫·米尔恩和马克·伦茨纳引导他发现了作为其前身的TIFF。

尽管TIFF应用广泛且重要，巴克并未找到任何关于其创建者的现成信息，只有公司Aldus。经过艰苦的研究，包括翻阅旧的MacWeek杂志和计算机历史博物馆的记录稿，巴克终于在Aldus TIFF规范文档中发现了斯蒂芬·卡尔森的名字，尽管拼写有误。

通过专利搜索和传统的侦探工作，包括邮寄实体信件，巴克找到了斯蒂芬·卡尔森。卡尔森证实了他在创建TIFF中的作用，解释了桌面出版对标准图像格式的需求。他淡化了自己的贡献，强调了推广TIFF作为行业标准的协作努力。

采访卡尔森两年后，巴克收到了卡尔森的前妻佩吉的电子邮件，告知他卡尔森的去世以及她对他亲切的昵称“TIFF先生”。这封电子邮件突显了卡尔森的谦逊以及认可他的贡献的重要性。受佩吉信息的激励，巴克立即更新了TIFF的维基百科页面，将斯蒂芬·卡尔森列为创建者，纠正了历史记录。巴克总结说，他广泛的研究工作是值得的，以确保将适当的荣誉授予真正的发明者，无论他们个人是否渴望获得认可。

---

## 7. Carice TC2 – 非数字电动汽车

**原文标题**: Carice TC2 – A non-digital electric car

**原文链接**: [https://www.caricecars.com/](https://www.caricecars.com/)

Carice TC2 是一款在荷兰设计和制造的全电动复古风格汽车，旨在将经典美学与现代技术相结合。 它以轻量化、动感和优雅著称，专为纯粹而愉悦的驾驶体验而设计。

主要特点包括零排放的全电动动力系统、590公斤起的车身重量以实现动态操控和低功耗，以及对简洁性和基本驾驶要素的强调。 TC2优先考虑驾驶者和乘客的享受，提供的不仅仅是一种交通工具，更是一件艺术品。

根据电池组的不同，其续航里程可达 300 公里，充电至 80% 最快只需 2.7 小时。 TC2 符合欧盟法规，可在欧盟国家和采用这些法规的国家/地区行驶。

该车可根据个人喜好定制油漆、内饰和车顶颜色。 目前按需生产，起价为 44,500 欧元（不含税）。 感兴趣的买家可以订购 TC2，并预订下一个生产批次的席位。

---

## 8. iOS 26.2 将在日本监管截止日期前允许第三方应用商店

**原文标题**: iOS 26.2 to allow third-party app stores in Japan ahead of regulatory deadline

**原文链接**: [https://www.macrumors.com/2025/11/05/ios-26-2-third-party-app-stores-japan/](https://www.macrumors.com/2025/11/05/ios-26-2-third-party-app-stores-japan/)

苹果iOS 26.2目前处于测试阶段，将允许日本用户在监管截止日期前安装第三方应用商店。此前，日本国会于2024年6月批准立法，强制苹果允许iPhone上存在替代应用商店和支付提供商。日本公平贸易委员会在2025年8月发布的《移动软件竞争法指南》中进一步巩固了这一要求，禁止像苹果这样的平台运营商阻止替代应用商店和支付系统。

这一变化使日本与欧盟保持一致，欧盟由于《数字市场法案》已允许苹果开设第三方应用商店。根据X上的一篇帖子，iOS 26.2测试版允许日本用户安装AltStore PAL和Epic Games Store等应用商店。虽然《堡垒之夜》可用，但Epic目前对应用内购买进行了区域封锁。

《移动软件竞争法指南》预计将于2025年12月18日生效，苹果预计将在12月9日至12月16日之间的某个时候发布iOS 26.2。Epic Games计划在2025年末将《堡垒之夜》及其游戏商店平台带到日本的iOS系统上。

---

## 9. 为了更安全的浏览器，移除 XSLT

**原文标题**: Removing XSLT for a more secure browser

**原文链接**: [https://developer.chrome.com/docs/web-platform/deprecating-xslt](https://developer.chrome.com/docs/web-platform/deprecating-xslt)

Chrome计划于2026年末移除XSLT支持：安全风险与替代方案

主要内容包括：

*   **移除时间表：** XSLT支持将于2027年8月的Chrome 164版本中完全移除，此前将经历一个包含警告和测试阶段的弃用期。
*   **安全问题：** XSLT处理器的复杂C/C++代码库容易出现内存安全漏洞。
*   **替代方案：** 现代JavaScript API（Fetch API、DOMParser）和框架（React、Vue、Svelte）为数据转换和渲染提供了更安全、更强大的替代方案。
*   **迁移策略：** 文章建议将XSLT处理迁移到服务器端，切换到基于JSON的API和客户端JavaScript渲染，或使用基于JavaScript的XSLT库（Saxonica）或polyfill来维持功能。
*   **特定用例：** 文章讨论了诸如RSS/Atom订阅、嵌入式设备API输出和客户端模板等用例，并为每个用例提供了具体的迁移建议。 还提到了Chrome扩展程序，作为无法修改源XML或XSLT的遗留应用程序的潜在解决方案。

总体目标是提高浏览器安全性，简化Web平台，并将资源集中于积极支持现代Web的技术。

---

## 10. SPy：快速静态类型Python变体的解释器和编译器

**原文标题**: SPy: An interpreter and compiler for a fast statically typed variant of Python

**原文链接**: [https://antocuni.eu/2025/10/29/inside-spy-part-1-motivations-and-goals/](https://antocuni.eu/2025/10/29/inside-spy-part-1-motivations-and-goals/)

本文介绍 SPy，这是一种新的解释器和编译器，它针对Python的静态类型变体，专注于性能。 SPy不是100%兼容的“Python编译器”，因为它有意排除了一些动态Python特性。相反，它旨在与现有的Python生态系统紧密集成，允许导入Python库和SPy模块。

作者将 SPy 与两种常见的提高 Python 速度的方法进行了对比：一是“完整 Python”JIT 编译器（如 PyPy），它们在一致的性能和内存使用方面存在困难；二是“子集/变体”编译器（如 Cython），它们牺牲了 Pythonic 模式来换取速度。SPy 旨在弥合这一差距，通过移除阻碍优化的动态特性，同时引入新特性以保持 Pythonic 的表达能力。

作者详细介绍了 Python 固有的性能限制，特别是其动态特性（例如，运行时模块解析、可变类）以及由于普遍存在的指针追踪而导致的缓存不友好的内存布局。他们观察到，开发者通常为了可读性和 JIT 兼容性而遵守一种非正式的“RealPython”子集，但解释器无法利用这些约束。静态类型化的努力改善了这种情况，但 Python 的设计并不完全适合它。

SPy 的设计原则优先考虑易用性、静态类型、与 C/Rust 相当的性能、可预测的性能、丰富的元编程、零成本抽象以及通过动态类型选择性地启用动态性。最终，SPy 致力于在单一语言中提供低级控制和高级表达能力。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 2 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 3 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 4 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 5 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 6 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 7 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 8 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 9 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 10 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 11 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 12 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 13 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 14 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 15 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 16 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 17 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 18 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 19 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 20 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 21 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 22 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 23 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 24 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 25 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 26 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 27 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 28 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 29 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 30 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 31 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 32 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 33 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 34 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 35 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 36 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 37 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 38 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 39 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 40 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 41 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 42 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 43 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 44 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 45 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 46 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 47 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 48 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 49 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 50 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 51 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 52 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 53 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 54 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 55 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 56 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 57 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 58 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 59 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 60 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 61 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 62 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 63 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 64 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 65 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 66 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 67 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 68 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 69 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 70 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 71 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 72 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 73 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 74 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 75 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 76 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 77 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 78 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 79 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 80 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 81 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 82 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 83 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 84 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 85 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 86 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 87 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 88 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 89 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 90 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 91 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 92 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 93 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 94 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 95 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 96 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 97 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 98 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 99 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 100 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 101 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 102 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 103 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 104 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 105 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 106 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 107 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 108 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 109 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 110 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 111 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 112 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 113 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 114 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 115 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 116 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 117 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 118 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 119 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 120 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 121 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 122 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 123 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 124 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 125 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 126 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 127 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 128 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 129 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 130 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 131 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 132 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 133 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 134 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 135 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 136 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 137 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 138 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 139 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 140 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 141 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 142 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 143 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 144 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 145 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 146 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 147 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 148 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 149 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 150 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 151 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 152 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 153 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 154 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 155 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 156 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 157 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 158 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 159 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 160 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 161 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 162 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 163 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 164 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 165 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 166 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 167 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 168 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 169 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 170 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 171 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 172 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 173 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 174 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 175 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 176 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 177 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 178 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 179 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 180 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 181 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 182 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 183 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 184 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 185 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 186 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 187 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 188 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 189 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 190 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 191 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 192 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 193 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 194 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 195 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 196 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 197 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 198 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 199 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 200 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 201 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 202 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 203 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 204 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 205 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 206 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 207 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 208 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 209 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 210 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 211 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 212 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 213 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 214 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 215 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 216 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 217 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 218 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 219 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 220 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 221 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 222 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 223 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 224 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 225 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 226 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 227 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 228 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 229 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 230 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
