# Hacker News 热门文章摘要 (2025-11-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 吹笛人背后的残酷真相 (2020)

**原文标题**: The grim truth behind the Pied Piper (2020)

**原文链接**: [https://www.bbc.com/travel/article/20200902-the-grim-truth-behind-the-pied-piper](https://www.bbc.com/travel/article/20200902-the-grim-truth-behind-the-pied-piper)

花衣魔笛手传说的历史渊源与不解之谜

本文探讨了花衣魔笛手传说背后的历史基础和历久弥新的谜团。这个故事经格林兄弟和罗伯特·勃朗宁的普及，讲述了一个魔笛手因未收到清除哈默尔恩鼠患的报酬而引诱孩子们离开的故事，但有证据表明，一个真实事件启发了这个故事。

哈默尔恩的城镇记录、铭文和历史记载表明，1284年6月26日，有130名儿童被一位身穿彩衣的魔笛手带领消失。这一事件被视为一个深刻的历史谜团，激发了许多理论。

一种突出的理论认为，“花衣魔笛手”是一位招募人员，在德国向东欧移民期间带领年轻人向东前进。另一种理论将失踪事件与“舞蹈狂热症”的爆发联系起来，这是一种集体癔症。更恐怖的理论则暗示异教仲夏节期间的大屠杀，或者被秘密带到修道院。

尽管存在种种可怕的可能性，花衣魔笛手传说已成为一种文化试金石，在众多国家和语言中广为人知，并激发了艺术、文学和音乐创作。在某种程度上，这种共同的遗产将不同文化背景的人们团结起来，超越了最初的悲剧。哈默尔恩继续利用这个传说，餐厅和商店提供以老鼠为主题的食物和纪念品，而哈默尔恩博物馆则探索这个故事的全球影响力。

---

## 12. Radiant Computer

**原文标题**: Radiant Computer

**原文链接**: [https://radiant.computer](https://radiant.computer)

生成摘要出错

---

## 13. UPS飞机在路易斯维尔机场附近坠毁

**原文标题**: UPS plane crashes near Louisville airport

**原文链接**: [https://avherald.com/h?article=52f5748f&opt=0](https://avherald.com/h?article=52f5748f&opt=0)

生成摘要时出错

---

## 14. 微软无法保护欧盟数据免受美国当局侵害

**原文标题**: Microsoft Can't Keep EU Data Safe from US Authorities

**原文链接**: [https://www.forbes.com/sites/emmawoollacott/2025/07/22/microsoft-cant-keep-eu-data-safe-from-us-authorities/](https://www.forbes.com/sites/emmawoollacott/2025/07/22/microsoft-cant-keep-eu-data-safe-from-us-authorities/)

This Forbes article reports that Microsoft has admitted it cannot guarantee EU data will be protected from U.S. authorities, due to laws like the U.S. Cloud Act. Anton Carniaux, a Microsoft France executive, stated this during testimony before a French Senate inquiry focused on digital sovereignty and public procurement.

The admission raises concerns about European data sovereignty, with experts pointing out that the location of data storage (even within the EU) is irrelevant when U.S. jurisdiction applies to the provider. This impacts national security, privacy, and business competitiveness.

The inquiry specifically questioned the separation of data on Project Bleu, a Microsoft partnership, from the Health Data Hub medical research platform hosted on Azure, fearing that sensitive health data could be accessed by US authorities.

The article highlights the EU's reliance on U.S. cloud providers, despite calls for more homegrown solutions. While a recent report shows that US firms possess a significant portion of Europe's cloud infrastructure market share, it urges the EU and UK to follow France's lead in demanding answers and fostering true data sovereignty.


---

## 15. RISC-V迈出国际ISO/IEC标准化第一步

**原文标题**: RISC-V takes first step toward international ISO/IEC standardization

**原文链接**: [https://riscv.org/blog/risc-v-jtc1-pas-submitter/](https://riscv.org/blog/risc-v-jtc1-pas-submitter/)

RISC-V获得ISO/IEC认可，可提交国际标准草案

---

## 16. 挪威审查网络安全，因中国巴士发现远程访问功能。

**原文标题**: Norway reviews cybersecurity after remote-access feature found in Chinese buses

**原文链接**: [https://scandasia.com/norway-reviews-cybersecurity-after-hidden-remote-access-feature-found-in-chinese-buses/](https://scandasia.com/norway-reviews-cybersecurity-after-hidden-remote-access-feature-found-in-chinese-buses/)

挪威在公共交通运营商Ruter于中国宇通电动巴士中发现隐藏的罗马尼亚SIM卡（可能允许远程访问）后，启动了一项网络安全审查。这些SIM卡理论上允许宇通关闭车辆或通过软件更新进行干预。虽然Ruter首席执行官Bernt Reitan Jenssen认为滥用不太可能，但这一发现引发了人们对外国技术供应商带来的网络安全风险的担忧。

Ruter已移除这些SIM卡，并正在加强其网络安全措施，包括采购规则、防火墙和云安全，以维持本地控制。挪威交通部长Jon-Ivar Nygård表示，政府正在评估来自挪威安全联盟以外国家的供应商风险，以保护关键基础设施。

挪威1300辆电动巴士中约有850辆来自宇通，其中300辆在奥斯陆和阿克斯胡斯地区运营。该事件凸显了更广泛的网络安全挑战，因为中国的电动巴士在全球范围内日益普及，引发了人们对公共交通系统中数字安全和战略依赖性的质疑。文章包含一篇关于宇通向丹麦交付电动巴士的相关文章，进一步强调了该公司日益增长的全球影响力。

---

## 17. 假设：Python 的基于属性的测试

**原文标题**: Hypothesis: Property-Based Testing for Python

**原文链接**: [https://hypothesis.readthedocs.io/en/latest/](https://hypothesis.readthedocs.io/en/latest/)

Hypothesis是一个用于基于属性测试的Python库。用户无需编写特定的测试用例，而是定义应该对一系列输入都成立的属性。然后，Hypothesis会自动生成该范围内的随机输入，包括边缘情况，以测试代码。这种方法有助于发现意想不到的错误并确保代码的健壮性。

给出的例子展示了一个排序函数的测试，其中Hypothesis生成各种整数和浮点数列表，以验证`my_sort`是否产生与标准`sorted`函数相同的结果。

该文档的结构旨在引导用户从初学者到高级水平。它包括一个针对新手的教程，一个用于更快入门的快速入门指南，用于实际应用的实践指南，用于更深入理解的解释，以及一个全面的API参考。 基本上，它提供了学习如何使用Python中的Hypothesis并有效实施基于属性的测试所需的一切。

---

## 18. 解析化学

**原文标题**: Parsing Chemistry

**原文链接**: [https://re.factorcode.org/2025/10/parsing-chemistry.html](https://re.factorcode.org/2025/10/parsing-chemistry.html)

本文探讨了在Factor中构建化学式解析器的方法，灵感来源于Python的`chemparse`项目。目标是创建能够将化学式解析为元素与其计数映射的字典的功能，支持诸如分数化学计量、基团、嵌套基团和括号式等特性。

作者利用Factor的EBNF语法支持来定义解析表达式语法。该语法将解析过程分解为更小的步骤：解析符号（一个或两个字母）、数字（整数或浮点数）和对（带有可选数字前缀和后缀的符号，可能位于括号内）。

最初的EBNF定义`split-formula`成功地将公式解析为嵌套向量，但需要进一步处理才能实现所需的元素到计数的映射。本文介绍了`flatten-formula`这个词，以递归方式将嵌套结构扁平化为关联数组（assoc）。该词将元素符号与其计数结合起来，并递归地处理分组公式。

最后，`parse-formula`这个词结合了`split-formula`和`flatten-formula`，提供了一个完整的解析解决方案。一些单元测试演示了解析器的功能，确认其能够处理简单的公式、分数化学计量、分组公式（嵌套的和括号式的），并准确地将每个元素映射到其正确的计数。代码可在作者的GitHub上找到。

---

## 19. 华硕宣布ProArt Display 8K PA32KCX将于十月上市

**原文标题**: Asus Announces October Availability of ProArt Display 8K PA32KCX

**原文链接**: [https://press.asus.com/news/press-releases/asus-proart-display-8k-pa32kcx-availability/](https://press.asus.com/news/press-releases/asus-proart-display-8k-pa32kcx-availability/)

华硕宣布ProArt Display 8K PA32KCX专业显示器将于2025年10月上市，这是全球首款8K HDR mini LED专业显示器。这款显示器配备32英寸8K HDR面板，具有4032区局部调光、1200尼特峰值亮度和1000尼特持续亮度，非常适合需要高细节和色彩准确度的内容创作者。

主要功能包括95% Adobe RGB、97% DCI-P3色域覆盖、真正的10位色彩深度，以及出厂预校准至Delta E < 1的色彩准确度。它还支持杜比视界、HDR10和HLG格式。内置的电动色度计可实现自校准和自动校准，并且该显示器与ProArt校准软件、Calman和Light Illusion ColourSpace CMS兼容。

PA32KCX提供便捷的连接性，具有两个雷雳4端口、DisplayPort 2.1和两个HDMI 2.1端口。内置的自动KVM切换器可在两台计算机之间无缝切换。此外，特定地区的购买者将获得免费的三个月Adobe Creative Cloud订阅。

该显示器具有环境光传感器、接近传感器和符合人体工程学的支架，可进行倾斜、旋转、枢轴和高度调节。随附环绕式遮光罩，以最大限度地减少反射。该显示器采用mini LED技术，可减少视觉伪影和闪烁，同时提供高持续亮度。

---

## 20. 栈回溯：空间与时间的权衡

**原文标题**: Stack walking: space and time trade-offs

**原文链接**: [https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs](https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs)

本文分析了x86-64 Linux上不同堆栈回溯机制的空间开销权衡，重点关注帧指针（FP）、DWARF .eh_frame和SFrame。

作者发现，启用帧指针虽然会保留一个寄存器，但自相矛盾的是，在频繁访问堆栈对象的情况下，可以减少二进制文件的大小。这是因为相对于RSP相关的寻址方式，RBP相关的寻址方式可以产生更紧凑的机器码。这种影响在不同的程序和编译器实现之间差异很大。

SFrame是一种较新的面向性能分析的格式，本文将其与.eh_frame进行比较。分析表明，SFrame元数据的大小比.eh_frame和.eh_frame_hdr的总和大约大10%。作者对SFrame的可行性表示怀疑，因为它具有这种大小开销，并且相对于现有方法缺乏明显的优势。作者建议使用紧凑的展开描述符。

使用Clang和GCC对FP和SFrame方法进行比较，揭示了编译器特定的差异。Clang构建的二进制文件显示FP导致更小的可执行文件，而GCC构建的二进制文件显示相反的趋势，暗示GCC中帧指针代码生成优化程度较低。

文章最后得出结论，SFrame会导致VM大小显著增加。

最后，作者恳请LLVM社区支持他对SFrame RFC提出的技术异议。

运行时性能分析计划在未来的更新中进行。

---

## 21. Bluetui – Linux 蓝牙管理器

**原文标题**: Bluetui – A TUI for managing Bluetooth on Linux

**原文链接**: [https://github.com/pythops/bluetui](https://github.com/pythops/bluetui)

Bluetui 是一个在 Linux 系统上管理蓝牙设备的终端用户界面（TUI）应用程序。它需要安装 bluez，并可选择安装 nerdfonts 以正确显示图标。 安装方法包括从发布页面获取预构建的二进制文件、使用 `cargo install bluetui` 从 crates.io 安装、Arch Linux 的 extra 仓库 (`pacman -S bluetui`)、Gentoo 的 lamdness overlay、X-CMD (`x install bluetui`)，或使用 `git clone` 和 `cargo build` 从源代码构建。

TUI 允许用户使用键盘快捷键在不同部分之间切换、滚动、启动/停止扫描以及退出应用程序。 启用/禁用适配器的配对/发现/电源，取消配对/连接/断开/信任/重命名已配对的设备以及配对新设备等特定操作也通过快捷键控制。

快捷键可以通过 `$HOME/.config/bluetui/` 中的 `config.toml` 文件或使用 `-c` 标志指定的自定义路径进行配置。 配置选项包括布局和窗口宽度。 该应用程序在 GPLv3 许可下发布，并感谢 Marco Bulgarelli 设计了 Bluetui 标志。

---

## 22. 苹果的Persona技术使用高斯泼溅创建3D面部扫描

**原文标题**: Apple’s Persona technology uses Gaussian splatting to create 3D facial scans

**原文链接**: [https://www.cnet.com/tech/computing/apple-talks-to-me-about-vision-pro-personas-where-is-our-virtual-presence-headed/](https://www.cnet.com/tech/computing/apple-talks-to-me-about-vision-pro-personas-where-is-our-virtual-presence-headed/)

本文探讨了苹果Vision Pro头显中的“人物角色”(Personas)功能，该功能可创建逼真的用户3D虚拟化身，用于实时虚拟互动。作者强调了该技术与以往的虚拟化身系统相比所具有的先进能力，并强调其在革新远程呈现和协作方面的潜力。

这些“人物角色”是使用高斯溅射技术创建的，这是一种将2D图像编织成3D模型的机器学习技术。这使得能够进行详细的面部扫描，捕捉到诸如表情、珠宝甚至睫毛等细微之处。苹果强调该技术专注于创建真实的个人实时呈现，而不是生成深度伪造。

作者讨论了“人物角色”超越Vision Pro的潜力，并暗示该技术最终可能会集成到iPhone和其他设备中。虽然苹果承认这一想法的吸引力，但他们坚持认为Vision Pro独特的传感器和显示功能组合对于获得最佳的人物角色体验至关重要。

文章最后强调了“人物角色”在各种应用中的变革潜力，包括商业协作和远程医疗培训，并展望了该技术的入门成本降低，从而实现更广泛的可访问性和采用的未来。

---

## 23. 灰骷髅：一个用于嵌入式系统等的微型C语言计算机视觉库。

**原文标题**: Grayskull: A tiny computer vision library in C for embedded systems, etc.

**原文链接**: [https://github.com/zserge/grayskull](https://github.com/zserge/grayskull)

Grayskull是一个轻量级、无依赖的C语言库，专为资源受限设备（如微控制器）上的计算机视觉任务而设计。它专注于灰度图像，并在小型代码库（小于1KLOC）内提供一系列用于图像处理和特征提取的算法。

主要功能包括图像操作（如复制、裁剪、调整大小和降采样）；滤波选项（如模糊、Sobel边缘检测和阈值处理（全局、Otsu、自适应））；形态学操作（腐蚀、膨胀）；几何功能（如连通分量分析和透视变换）；以及使用FAST/ORB关键点的特征检测。它还集成了局部二值模式（LBP）用于目标检测。

该库提供用于PGM图像读/写的实用程序，并采用单头文件设计，易于集成。它避免了动态内存分配和C++依赖。

API包括用于操作`gs_image`结构（宽度、高度、像素数据）的函数，以及裁剪、调整大小、阈值处理、模糊、边缘检测、连通分量分析、特征提取（FAST/ORB）和基于LBP级联的目标检测等操作。还提供了用于分配和释放图像内存（`gs_alloc`，`gs_free`）以及PGM I/O（`gs_read_pgm`，`gs_write_pgm`）的可选辅助函数。

Grayskull在MIT许可下授权，允许在各种项目中灵活使用。在线演示和示例代码可用于快速实验。

---

## 24. 使用 Rust 后端的区间树

**原文标题**: Intervaltree with Rust Back End

**原文链接**: [https://github.com/Athe-kunal/intervaltree_rs](https://github.com/Athe-kunal/intervaltree_rs)

本文介绍了`intervaltree_rs`，一个由Rust支持的Python区间树实现，通过PyO3访问。它允许Python开发者直接在他们的Python代码中利用Rust的性能进行区间树操作。

该crate提供了从表示区间的元组列表（左边界，右边界，有效载荷）构建区间树、插入新区间、搜索重叠区间以及基于它们的（左边界，右边界）删除区间的能力。

主要特性包括：

*   **性能：** 利用Rust的高效性进行区间树操作。
*   **易于集成：** 使用PyO3提供无缝的Python接口。
*   **核心功能：** 支持构建、插入、搜索和删除区间。
*   **包含/排除搜索：** 提供一个带有`inclusive`标志的`search`函数来控制查询行为。

要使用该库，用户需要一个Rust工具链，Python 3.8+，以及用于构建和安装包的`maturin`。本文提供了一个使用虚拟环境和`maturin develop`进行本地开发的快速入门指南。它还解释了如何使用`maturin build --release`构建可分发的wheel包。

该包通过Rust单元测试进行测试，确保其可靠性。这些测试可以使用`cargo test`运行。本文全面概述了`intervaltree_rs`、其功能，以及如何在Python环境中设置和使用它。

---

## 25. 在PostgreSQL实例间迁移表

**原文标题**: Moving tables across PostgreSQL instances

**原文链接**: [https://ananthakumaran.in/2025/11/02/moving-tables-across-postgres-instances.html](https://ananthakumaran.in/2025/11/02/moving-tables-across-postgres-instances.html)

本文详细介绍了一种使用原生逻辑复制在PostgreSQL实例之间迁移特定表的方法，这是一种比谷歌数据库迁移服务（DMS）更灵活的替代方案，DMS迁移的是整个数据库。

该过程涉及几个关键步骤：

1.  **授予复制权限：** 确保源和目标实例上的用户帐户都具有复制权限。
2.  **复制模式：** 使用`pg_dump`传输表模式。最初创建表时*不带*约束和索引，以加快初始数据转储速度。
3.  **初始转储和CDC：** 逻辑复制首先执行初始数据转储，然后切换到变更数据捕获（CDC）以进行实时更新。在复制模式时创建主键。
4.  **发布和订阅：** 在源实例上为要迁移的表创建发布，并在目标实例上创建相应的订阅。
5.  **监控复制：** 使用PostgreSQL系统表（如`pg_replication_slots`和`pg_stat_subscription`）跟踪复制进度。
6.  **添加索引和外键：** 在复制切换到CDC模式后，在目标实例上重建索引和外键约束。
7.  **分析和清理：** 运行`analyze`以更新查询统计信息，确保高效的查询计划。`vacuum`也可能是有益的。
8.  **切换：** 手动同步实例之间的序列值。然后，禁用对源的写入并切换到目标。PgBouncer可以通过暂停连接、重新加载配置以指向新实例以及恢复连接，来促进此过程中的近零停机时间。
9.  **清理：** 验证迁移后，删除发布和订阅。

本文强调了约束处理、序列同步的细微之处，以及适当监控和统计信息更新对于迁移后获得最佳性能的重要性。

---

## 26. 科斯莫斯：用于自主发现的AI科学家

**原文标题**: Kosmos: An AI Scientist for Autonomous Discovery

**原文链接**: [https://arxiv.org/abs/2511.02824](https://arxiv.org/abs/2511.02824)

此 arXiv 文章介绍了 Kosmos，一种专为自主科学发现而设计的人工智能科学家。 Kosmos 能够自动进行数据驱动研究的迭代循环，包括文献检索、假设生成和数据分析。 与以往的人工智能代理不同，Kosmos 利用结构化的世界模型来促进数据分析代理和文献检索代理之间的信息共享，从而能够在较长时间内（长达 12 小时和 200 次代理部署）连贯地追求目标。

Kosmos 通过平均每次运行执行 42,000 行代码并分析 1,500 篇论文来展示其能力。 该系统生成具有可追溯推理的科学报告，引用所有带有支持代码或文献的声明。 独立科学家验证了 Kosmos 报告中所述声明的高准确率（79.4%）。 合作者表示，单次 Kosmos 运行（仅限于 20 个周期）可以完成相当于 6 个月的研究工作。 有价值的发现数量也随着 Kosmos 周期的增加呈线性增长。

该论文重点介绍了 Kosmos 在代谢组学、材料科学、神经科学和统计遗传学等不同领域取得的七项发现。 值得注意的是，Kosmos 独立地重现了来自未发表手稿的发现，并为科学文献做出了新的贡献。 该文章强调了 Kosmos 通过自动化和增强研究过程来加速科学发现的潜力。

---

## 27. 蓝王子 (1989)

**原文标题**: Blue Prince (1989)

**原文链接**: [https://novalis.org/blog/2025-10-27-blue-prince-1989.html](https://novalis.org/blog/2025-10-27-blue-prince-1989.html)

本文回顾性地评测了 1989 年 Apple //e 游戏《蓝王子》，并对比了 2025 年的重制版。作者回忆起童年对原作的热爱，决定重玩更新后的版本，但最终认为原作更具吸引力。

作者强调了 1989 年游戏中他更喜欢的几个方面。其中最主要的是一个独特的、需要玩家物理反转软盘的横向思维谜题。这个巧妙的解决方案在重制版中无法复制，被认为是游戏的亮点。他还欣赏原作直接的文字描述，使得重制版的物品栏追踪功能显得不那么重要。

此外，作者批评了 2025 年重制版对 3D 技术的运用，认为与原作高效的文字探索相比，这不必要地拖慢了游戏节奏。他更喜欢原作灵敏的键盘操作，并将其与现代版本的迟缓感形成对比。

总而言之，作者建议那些因重制版节奏缓慢而失去兴趣的玩家尝试 1989 年的版本，并认为其极简主义的美学和更快的游戏节奏可能会带来更愉悦的体验。他鼓励读者找到游戏的软盘镜像，并使用 Apple 模拟器进行游戏。

---

## 28. Apple II 的 Microsoft SoftCard：让两个处理器共享内存

**原文标题**: The Microsoft SoftCard for the Apple II: Getting two processors to share memory

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20251104-00/?p=111758](https://devblogs.microsoft.com/oldnewthing/20251104-00/?p=111758)

微软的SoftCard通过增加Zilog Z80处理器，使Apple II计算机能够运行CP/M软件。由于Apple II已经拥有6502处理器，本文解释了这两个处理器如何共存并共享内存。

SoftCard利用6502进行I/O和其他适合它的任务，同时在Z80上运行CP/M程序。为了避免6502崩溃，SoftCard利用Z80的REFRESH线，允许6502执行短暂的自旋循环并刷新其寄存器，防止数据丢失。当Z80需要6502执行任务时，它会更新内存以通知6502执行特定代码并返回结果。

内存映射是一个关键问题。6502和Z80都希望将内存的前256字节用于不同的目的，并且CP/M期望在6502已经使用的特定地址加载程序。为了解决这个问题，SoftCard包含了地址转换电路，重新映射了Z80的内存空间。Apple II的特殊保留地址被移动到Z80内存映射的末尾，Apple II的普通RAM在Z80的内存映射中变得连续，从地址$0000开始。SoftCard手册为程序员提供了详细的说明，包括如何从Z80调用6502子程序以及内存重映射图。

---

## 29. 我担心他们把Copilot放到Excel里。

**原文标题**: I’m worried that they put co-pilot in Excel

**原文链接**: [https://simonwillison.net/2025/Nov/5/brenda/](https://simonwillison.net/2025/Nov/5/brenda/)

Ada James (@belligerentbarbies) 的TikTok帖子表达了对Copilot AI集成到Excel中的担忧，特别是关注其对现有工作流程的潜在破坏以及像“Brenda”这样的熟练Excel用户所扮演的重要角色。

作者担心Copilot，尽管它做出了承诺，但会给关键的财务报告带来错误。核心论点是，经验丰富的Excel用户Brenda了解这些报告的复杂性并确保其准确性。然而，不熟悉Excel复杂性的高层管理者可能会依赖Copilot进行更改，由于AI倾向于“幻觉”（生成不正确或无意义的信息），这可能导致重大错误。

帖子认为，Brenda的专业知识，源于多年的经验和对Excel的深刻理解，对于准确的财务报告是不可或缺的。作者将Brenda描绘成商业界的重要人物，她对Excel的掌握对于资本主义本身的运作至关重要。核心担忧是Copilot将取代或削弱Brenda的角色，最终导致不准确和不可靠的财务数据。本质上，在Excel中执行的复杂和至关重要的任务方面，作者更信任人类的专业知识而不是AI。

---

## 30. 我把所有项目都从云端撤了下来，省下了数千美元。

**原文标题**: I took all my projects off the cloud, saving thousands of dollars

**原文链接**: [https://rameerez.com/send-this-article-to-your-friend-who-still-thinks-the-cloud-is-a-good-idea/](https://rameerez.com/send-this-article-to-your-friend-who-still-thinks-the-cloud-is-a-good-idea/)

无法访问文章链接。

---

## 31. Gnome Mutter 彻底放弃整个 X11 后端

**原文标题**: Gnome Mutter Now "Completely Drops the Whole X11 Back End"

**原文链接**: [https://www.phoronix.com/news/GNOME-Mutter-Drops-X11](https://www.phoronix.com/news/GNOME-Mutter-Drops-X11)

GNOME的Mutter窗口管理器已正式放弃其X11后端，完全致力于Wayland作为其唯一的显示服务器协议。

---

## 32. 纽约智能手机禁令让午餐再次喧闹起来

**原文标题**: NY smartphone ban has made lunch loud again

**原文链接**: [https://gothamist.com/news/ny-smartphone-ban-has-made-lunch-loud-again](https://gothamist.com/news/ny-smartphone-ban-has-made-lunch-loud-again)

纽约学校（包括皇后区本杰明·N·卡多佐高中）的智能手机禁令导致午餐时间噪音和社交互动明显增加。学生们现在玩棋盘游戏和交谈，而不是沉迷于手机。教师报告称，目前在 31 个州加上华盛顿特区生效的禁令改善了课堂环境，提高了学生的参与度，并提高了整体效率。

虽然大多数学校工作人员认为这项禁令是积极的，但一些学生怀念使用手机。有些人使用“一次性”手机规避规则。另一些人则传递纸条、玩纸牌和拍摄宝丽来照片。尽管感受不一，但许多学生承认禁令的好处，例如阅读量增加和课堂讨论更加活跃。

文章重点介绍了一项来自州教师工会的调查，该调查显示，89% 的学校工作人员表示新政策改善了学校环境，76% 的人表示孩子们更投入到课堂中。教师普遍对这些变化感到满意，并报告说专注力更好，学生互动和讨论更多。一位助理校长甚至指出，学生们需要重新学习如何读取模拟时钟。

---

## 33. 修补68K软件 - 简易文本

**原文标题**: Patching 68K Software – SimpleText

**原文链接**: [https://tinkerdifferent.com/threads/patching-68k-software-simpletext.4793/](https://tinkerdifferent.com/threads/patching-68k-software-simpletext.4793/)

David Cook的文章详细描述了他修改SimpleText以使其在启动时打开一个较小的文本窗口的充满挑战的经历。最初，他期望一个简单的常量覆盖，但后来发现需要注入更复杂的代码来处理各种窗口类型（文本、图片、视频、关于框）。

他无法直接插入代码而不扰乱现有的跳转指令，因此他采用了一种跳出再跳回的方法。他用一个跳转到追加在'CODE'资源末尾的自定义例程的指令覆盖了现有代码，然后返回到原始的SimpleText代码流程。他的例程检查是否为文本窗口，并在需要时替换新的尺寸。之后，他不得不再次修补代码，因为SimpleText再次调整了窗口大小，所以他需要存储窗口是否已被他的代码先前调整过大小。

关键挑战包括：需要保留被覆盖代码的功能（例如检索`MBarHeight`），找到一个地方来存储第一个代码补丁的结果以供后续使用（通过将变量存储在代码本身中解决），以及处理CodeWarrior的限制（没有BSR指令，需要JSR和特定的例程位置）。

他使用了诸如直接调用`GetHandleSize`来避免库开销，将暂存寄存器传递给C函数，以及在资源中定义窗口大小以便于未来修改等技巧。他还提到了潜在的ResEdit损坏问题，并包含了一个破解版的SimpleText和资源。

---

## 34. 福斯蒂诺·奥罗 (12岁) 将维迪特·古杰拉蒂 (#27) 逼入国际象棋加赛

**原文标题**: Faustino Oro (12 years-old) takes Vidit Gujrathi (#27) to the tiebreaks in chess

**原文链接**: [https://twitter.com/FIDE_chess/status/1986051222512554279](https://twitter.com/FIDE_chess/status/1986051222512554279)

“法斯蒂诺·奥罗 (12岁) 国际象棋战平世界第27位维迪特·古杰拉蒂，进入加赛” 这篇文章描述了一场国际象棋比赛，12 岁的法斯蒂诺·奥罗表现出色，与排名很高的国际象棋棋手（世界排名第 27 位）维迪特·古杰拉蒂战成平手。关键在于奥罗能够将古杰拉蒂逼入加赛，凸显了这位年轻棋手令人印象深刻的技能和竞争能力。

---

## 35. 开发者正在选择较旧的AI模型

**原文标题**: Developers are choosing older AI models

**原文链接**: [https://www.augmentcode.com/blog/developers-are-choosing-older-ai-models-and-16b-tokens-of-data-explain-why](https://www.augmentcode.com/blog/developers-are-choosing-older-ai-models-and-16b-tokens-of-data-explain-why)

2025年10月，Augment Code观察到，开发者越来越多地选择旧款AI模型与新款模型并用，这表明AI模型的使用趋势正在从简单的升级换代转向专业化。来自数百万次实时互动的数据显示，Sonnet 4.5 的使用量下降，而 Sonnet 4.0 的使用量增加，这表明模型的选择是基于特定的任务需求。

文章重点介绍了 Sonnet 4.5、Sonnet 4.0 和 GPT-5 之间的行为差异。Sonnet 4.5 表现出更深层次的推理能力和较低的工具调用频率，从而导致更高的 token 输出和缓存利用率。Sonnet 4.0 优先考虑快速的任务执行，工具调用更频繁，从而实现更快、更具确定性的补全。GPT-5 平衡了推理和自然语言能力，擅长解释和混合编码任务。

数据显示，Sonnet 4.5 更适用于重构和调试等复杂任务，而 Sonnet 4.0 更受自动化和基于规则的编码任务青睐。GPT-5 最适合代码演练和文档编写。这种涌现出的专业化趋势与社区情绪相呼应，用户认识到每个模型独特的优势和劣势。

主要结论是，AI模型的使用正在多样化，不同模型之间存在可衡量的行为差异，并且系统成本正在向推理强度和缓存利用率转移。重点正在从寻找单一的“最佳”模型转向为每个任务选择最合适的认知风格。

---

## 36. 黑客宣言 (1986)

**原文标题**: The Hacker’s Manifesto (1986)

**原文链接**: [https://phrack.org/issues/7/3](https://phrack.org/issues/7/3)

《黑客宣言》由The Mentor于1986年撰写，是对黑客身份的热情辩护以及对社会认知的批判。 这份宣言在他被捕后不久写成，认为黑客是由好奇心、智慧和对知识的渴望所驱动，而这些都被僵化且缺乏灵感的教育体系所扼杀。

The Mentor将黑客描绘成因传统教育而感到厌倦和缺乏挑战的人，他们在计算机世界中找到了慰藉和智力刺激。 该文本强调了黑客因被误解和被贴上麻烦制造者的标签而产生的挫败感。 它突出了在线社区中的归属感，在这个社区中，人们的评判标准是他们的想法和能力，而不是种族或国籍等肤浅的特征。

该宣言挑战了黑客是罪犯的观念，认为他们只是在探索系统和寻求知识。 它指责公司从技术中牟取暴利，并指责政府虚伪，指出黑客经常受到不公正的妖魔化，而掌权者却犯下更大的罪行。

最终，《黑客宣言》是对理解和接受的呼吁，认为黑客是被学习和探索的愿望所驱动的，他们的行为应该在这种背景下看待。它以一种挑衅性的断言结束，即黑客精神无法被熄灭，因为“我们都一样”。

---

## 37. 美国国税局告知各州，直接报税系统2026年不会实现。

**原文标题**: Direct File won't happen in 2026, IRS tells states

**原文链接**: [https://www.nextgov.com/digital-government/2025/11/direct-file-wont-happen-2026-irs-tells-states/409309/](https://www.nextgov.com/digital-government/2025/11/direct-file-wont-happen-2026-irs-tells-states/409309/)

文章概要：

美国国税局通知各州，免费的政府运营在线报税服务Direct File项目将于2026年停止提供。此前，该项目在2024年和2025年成功进行了试点，受到数十万用户的好评。这一决定是在共和党人和税务准备公司游说反对该项目之后做出的。

特朗普政府的税收和支出政策法案指示国税局探索公私合作模式，以取代Direct File。现有的公私合作模式Free File使用率不高，并因误导用户付费服务而受到批评。

Direct File的支持者批评这一决定，声称这有利于TurboTax等税务准备垄断企业，损害了纳税人的利益，他们现在将不得不花费更多的金钱和时间来报税。参议员伊丽莎白·沃伦表示，为纳税人提供便捷报税渠道的斗争尚未结束。美国国税局尚未对此事发表评论。

---

## 38. 人工智能热门股下跌，投资者称尚无需恐慌

**原文标题**: Don't panic yet, investors say as high-flying AI stocks tumble

**原文链接**: [https://www.reuters.com/world/asia-pacific/global-markets-ai-selloff-pix-2025-11-05/](https://www.reuters.com/world/asia-pacific/global-markets-ai-selloff-pix-2025-11-05/)

无法访问文章链接。

---

## 39. 1988年的本周，罗伯特·莫里斯放出了以他名字命名的蠕虫病毒

**原文标题**: This week in 1988, Robert Morris unleashed his eponymous worm

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/on-this-day-in-1988-the-morris-worm-slithered-out-and-sparked-a-new-era-in-cybersecurity-10-percent-of-the-internet-was-infected-within-24-hours](https://www.tomshardware.com/tech-industry/cyber-security/on-this-day-in-1988-the-morris-worm-slithered-out-and-sparked-a-new-era-in-cybersecurity-10-percent-of-the-internet-was-infected-within-24-hours)

1988年，康奈尔大学研究生罗伯特·塔潘·莫里斯无意中在互联网上释放了“莫里斯蠕虫”。该蠕虫旨在评估互联网规模，利用BSD UNIX系统（特别是电子邮件和“finger”程序）中的漏洞，在24小时内感染了10%的互联网。

与病毒不同，莫里斯蠕虫能够自我复制和自主传播，导致系统运行缓慢、消息延迟和崩溃。伯克利、哈佛和美国宇航局等机构受到了严重影响，一些机构需要擦除整个系统才能根除该蠕虫。

联邦调查局对此事进行了调查，并将莫里斯确认为罪魁祸首。他因违反《计算机欺诈和滥用法案》而被起诉，但避免了牢狱之灾，而是被处以罚款、缓刑和社区服务。

该事件凸显了当时互联网的脆弱性，那时互联网主要还是NSFNET，万维网尚未出现。虽然该蠕虫没有损坏文件，但其影响造成的损失估计在10万美元到数百万美元之间，影响了当时连接的6万台系统中的大约6000台。该事件还促使人们改进了安全程序，并摆脱了对互联网天真的信任感。正如最近的人工智能蠕虫所见，现代蠕虫仍然是一种威胁。

---

## 40. 山姆大叔想扫描你的虹膜并收集你的DNA，无论你是不是公民。

**原文标题**: Uncle Sam wants to scan your iris and collect your DNA, citizen or not

**原文链接**: [https://www.theregister.com/2025/11/04/dhs_wants_to_collect_biometric_data/](https://www.theregister.com/2025/11/04/dhs_wants_to_collect_biometric_data/)

国土安全部拟大幅扩大移民申请生物识别数据收集范围，不仅可能影响移民，还可能影响与他们案件相关的美国公民。拟议规则将扩大必须提交生物识别数据的人员范围，包括任何申请人、请愿人、担保人、支持者、衍生物、家属、受益人或与移民请求相关的个人，无论其年龄或公民身份。 该规则还包括任何被国土安全部逮捕或拘留的外国人。

“生物识别数据”的定义也将扩大到包括“可测量的生物……或行为特征”，为收集眼部图像、声纹和 DNA 等数据打开了大门。 国土安全部明确寻求收集原始 DNA 或 DNA 测试结果的权力，用于验证生物性别或家庭关系等目的。

国土安全部表示，这些数据将用于身份验证、国家安全检查、安全文件制作和行政职能。

批评人士对政府权力过度扩张表示担忧，将该提案与专制国家相提并论，并指出可能侵犯宪法权利。 他们还对生物识别数据的准确性和潜在滥用表示担忧，尤其是面部识别技术。 公众可在 1 月 2 日之前就该提案提交意见。 国土安全部至今未回应有关公众负面反应的置评请求。

---

## 41. 冻结字符串字面量：过去、现在与未来？

**原文标题**: Frozen String Literals: Past, Present, Future?

**原文链接**: [https://byroot.github.io/ruby/performance/2025/10/28/string-literals.html](https://byroot.github.io/ruby/performance/2025/10/28/string-literals.html)

本文深入探讨了 Ruby 中冻结字符串字面量的历史、目的和未来。与许多流行的字符串不可变的语言不同，Ruby 字符串默认是可变的，这提供了灵活性，但也可能由于不必要的字符串复制和内存分配而导致性能问题。

作者解释说，Ruby 实际上同时具有可变和不可变的字符串，利用冻结来优化某些操作。例如，Ruby 会自动冻结哈希中的字符串键，以防止与可变性相关的问题。

文章随后追溯了冻结字符串字面量的演变历程。最初的动机是通过冻结用作常量的字符串字面量来减少开销。这导致了对新语法的提议，并最终采用了编译器优化。Ruby 2.1 引入了 `opt_str_freeze` 指令，该指令避免了在冻结字符串字面量之前复制它们。诸如 `opt_aref_with` 和 `opt_aset_with` 之类的进一步优化通过避免不必要的字符串复制来提高了哈希访问性能。

然而，`opt_aref_with` 最近已从 Ruby 主干中删除，因为大多数对性能敏感的代码现在都使用了魔法注释 `# frozen_string_literal: true`，从而降低了它的好处。文章最后强调了可变字符串的灵活性与与之相关的性能开销之间持续存在的权衡，以及在 Ruby 中不断优化字符串处理的努力。

---

## 42. 发布HN: Plexe (YC X25) – 从提示构建生产级机器学习模型

**原文标题**: Launch HN: Plexe (YC X25) – Build production-grade ML models from prompts

**原文链接**: [https://www.plexe.ai/](https://www.plexe.ai/)

Plexe AI是一家YC X25创业公司，提供一个平台，使用户能够通过自然语言提示构建和部署生产级机器学习模型。它将自身定位为一个“智能体ML工程团队”，从而为各种业务需求普及AI模型创建。

该平台简化了机器学习开发流程，允许用户连接数据，接收即时洞察（包括数据质量检查和模式识别），并用通俗易懂的语言定义所需模型的用途。然后，Plexe会自动构建一个针对特定挑战（如欺诈检测或客户流失预测）量身定制的、可用于生产的模型。

Plexe强调透明度，为用户提供清晰的性能指标、训练细节以及对每个预测的解释，从而培养信任和理解。该平台支持各种功能，包括自定义机器学习模型、数据仪表板、API端点、批量作业、文件上传和数据库连接器。

Plexe服务于不同的行业，包括金融和银行、电子商务、物流和网络安全，提供量身定制的解决方案，如欺诈预防、信用承销和客户流失减少。该平台强调其快速部署机器学习模型的能力，可以在几小时内（而不是几个月）从想法变成可用的AI。最后，Plexe提供博客、文档以及GitHub和Discord上的社区等资源。

---

## 43. 谷歌从其搜索结果中移除了7.49亿个安娜的档案链接。

**原文标题**: Google Removed 749M Anna's Archive URLs from Its Search Results

**原文链接**: [https://torrentfreak.com/google-removed-749-million-annas-archive-urls-from-its-search-results/](https://torrentfreak.com/google-removed-749-million-annas-archive-urls-from-its-search-results/)

安娜文库：盗版图书和文章的元搜索引擎，成版权方主要打击目标。自2022年上线以来，谷歌已应《数字千年版权法案》(DMCA) 下架请求，从搜索结果中删除了与安娜文库相关的7.49亿个网址，占谷歌自2012年发布透明度报告以来收到的所有下架请求的5%。

包括企鹅兰登书屋和约翰威立父子出版公司在内的出版社，以及1000多名作者和出版商，正积极发送DMCA通知，目前平均每周报告1000万个新网址。他们的目标是使用户难以通过谷歌搜索找到安娜文库的盗版内容。

虽然许多网址已被取消或降级，但通过直接搜索该网站名称，仍可访问安娜文库的主要域名，这表明尚未完全从搜索结果中清除该网站。尽管面临法律压力和下架努力，安娜文库仍在运营，对寻求保护其版权的出版商构成了持续的挑战。

---

## 44. 联邦调查局警告：有罪犯冒充移民局，敦促探员表明身份

**原文标题**: FBI Warns of Criminals Posing as ICE, Urges Agents to ID Themselves

**原文链接**: [https://www.wired.com/story/fbi-warns-of-criminals-posing-as-ice-urges-agents-to-id-themselves/](https://www.wired.com/story/fbi-warns-of-criminals-posing-as-ice-urges-agents-to-id-themselves/)

联邦调查局警告：罪犯冒充移民局特工，导致抢劫、绑架和性侵案件发生。公告敦促执法部门明确表明身份，并配合民众核实身份，以应对冒充犯罪的抬头。

这些犯罪行为利用了移民局的高度关注，针对脆弱社区，并削弱了对执法的信任。引用的例子包括发生在纽约、佛罗里达、布鲁克林和北卡罗来纳州的事件，其中假冒移民局特工犯下了从抢劫到企图强奸等罪行。

联邦调查局建议各机构协调核实合法的移民局行动，并强调了冒充的迹象，例如伪造的证件或过时的装备。他们还建议开展外展计划，以识别假冒特工，并消除冒充者造成的不信任感。

文章探讨了移民局自身掩盖行为的根本问题，批评人士认为这模糊了合法逮捕和军事式武力之间的界限，进一步削弱了公众的信心。一些司法管辖区，如加利福尼亚州和西雅图，正在考虑或已经颁布禁令，禁止执法部门在非高风险情况下进行遮面。

文章还详细介绍了一个发生在华盛顿州法夫市的案例，其中一名男子制作了一个视频，打扮成移民局特工，在他开车经过一家乌克兰杂货店时鸣喇叭，作为YouTube恶作剧的一部分。该案例强调了冒充行为的可能性及其对社区安全和信任的影响。

---

## 45. 泡泡的益处

**原文标题**: The Benefits of Bubbles

**原文链接**: [https://stratechery.com/2025/the-benefits-of-bubbles/](https://stratechery.com/2025/the-benefits-of-bubbles/)

本文认为，经济泡沫虽然最终不可持续，但能带来显著的长期效益，并借鉴了卡洛塔·佩雷斯关于技术革命以及伯恩·霍巴特和托拜厄斯·胡伯关于“拐点泡沫”的研究。

作者指出，目前由OpenAI等公司巨额投资推动的人工智能繁荣，类似于过去的互联网泡沫时代。虽然崩盘很可能发生，但认识到其积极后果至关重要。

佩雷斯的研究强调了泡沫如何驱动技术革命的“安装阶段”，从而导致基础设施建设，即使在泡沫破裂后，也能为未来的增长奠定基础。互联网泡沫尽管遭遇失败，但却促成了光纤基础设施的广泛普及和具备数字素养的劳动力。

霍巴特和胡伯补充了“认知能力”的概念，即在泡沫期间，对变革性未来的共同信念导致协同创新。例如，互联网泡沫刺激了XMLHttpRequest等创新，将Web浏览器从消费工具转变为生产力工具。泡沫也推动了后端创新，特别是随着Linux和商品硬件的兴起，以应对可扩展性挑战。

文章随后探讨了人工智能泡沫是否会有益，并解决了对GPU短寿命的担忧。然而，文章指出，对芯片制造厂（fabs）以及至关重要的发电基础设施的投资提供了更持久的价值。作者对该行业已经触及电力瓶颈感到鼓舞，因为这为建设更多电力提供了经济和政府激励，从而导致基础设施繁荣，这可能会极大地造福人类，特别是如果它能带来低边际成本的可再生能源。

---

## 46. 贝莱德的拉里·芬克：“代币化”、数字身份与社会信用

**原文标题**: BlackRock's Larry Fink: "Tokenization", Digital IDs, & Social Credit

**原文链接**: [https://thewinepress.substack.com/p/tokenization-blackrocks-larry-fink](https://thewinepress.substack.com/p/tokenization-blackrocks-larry-fink)

无法访问文章链接。

---

## 47. Isotemp OCXO107-10 恒温晶振内部

**原文标题**: Inside an Isotemp OCXO107-10 Oven Controlled Crystal Oscillator

**原文链接**: [https://tomverbeure.github.io/2025/10/26/Inside-an-Isotemp-OCXO107-10.html](https://tomverbeure.github.io/2025/10/26/Inside-an-Isotemp-OCXO107-10.html)

本文详细介绍了作者获取和探索Isotemp OCXO107-10恒温晶体振荡器 (OCXO) 的过程。它以 5 美元的价格购得，是一个 5 MHz 的振荡器，与现代设备中更常见的 10 MHz 型号不同，但与惠普铯钟和时间间隔计数器等较旧的设备兼容。

作者整理了来自“time-nuts”邮件列表的信息，强调这些振荡器曾经非常昂贵（1000 美元以上），被朗讯使用，并且有 OCXO107-16 等变体。他还从另一位爱好者 Ed Palmer 那里获得了宝贵的内部照片。

文章随后描述了如何使 OCXO 运行，详细介绍了用于电源和控制的 DE-9 引脚排列（包括用于 TTL 输出的 5V、用于恒温器的 12V、EFC 和 VREF）。台式测试表明，该装置最初会消耗大量电力来加热恒温器，稳定后功耗会降低。测量了输出功率和二次谐波失真。作者注意到该装置的标签上有 EFC 电压设置，并将测量的 Vref 输出与预期值进行了比较。

根据 Ed Palmer 提供的照片，其内部设计采用杜瓦瓶进行热隔离，使其能够抵抗温度变化，但也较为脆弱。文章推测了该振荡器的温度稳定性与其他 OCXO 相比如何，得出的结论是，虽然较旧的 OCXO 可能具有卓越的温度稳定性，但它们可能不如更小、更坚固的现代双恒温器 OCXO，但相位噪声、电压稳定性和尺寸等其他参数也很重要。文章还识别了关键组件，例如用作加热元件的摩托罗拉达林顿晶体管和可能的 TL431 电压基准。

最后，作者概述了构建定制线性电源的计划，用于长期的 OCXO 比较测量，旨在避免当前台式电源的噪声和功耗。

---

## 48. 西苏门答腊的歌唱巴士喇叭

**原文标题**: Singing bus horns in West Sumatra

**原文链接**: [https://www.auralarchipelago.com/auralarchipelago/kalason](https://www.auralarchipelago.com/auralarchipelago/kalason)

本文探寻了印度尼西亚西苏门答腊岛“卡拉松奥托”或称歌唱巴士喇叭的独特历史，并向传奇演奏家巴克·布达哈尔致敬。卡拉松产生于20世纪50年代，当时机械师开始将备用汽车喇叭调音并排列成音阶，为巴士司机创造了演奏旋律的键盘。

当米南加保地区的人们为了工作而穿越苏门答腊岛时，这些喇叭提供了慰藉和与家乡的联系，演奏着传统的民谣和流行歌曲。技术娴熟的演奏者，被称为“tukang kalason”，变得炙手可热，乘客们专门寻找有他们喜爱音乐家的巴士。卡拉松的声音成为西苏门答腊景观不可或缺的一部分。

在20世纪70年代和80年代，卡拉松的流行促使了音乐专辑的制作。然而，20世纪80年代现代柴油巴士的兴起，与卡拉松技术不兼容，导致了它的衰落。

本文重点介绍了作者与巴克·布达哈尔的会面以及当地汽车爱好者对卡拉松的复兴。作者曾希望通过旅行和录制巴克·布达哈尔来记录这一传统，但巴克·布达哈尔于2023年去世。本文是对这一传统和巴克·布达哈尔的深情致敬，颂扬其文化意义，并表达了对它以某种形式继续生存下去的希望。

---

## 49. NoLongerEvil-Thermostat – Nest 第一代和第二代固件

**原文标题**: NoLongerEvil-Thermostat – Nest Generation 1 and 2 Firmware

**原文链接**: [https://github.com/codykociemba/NoLongerEvil-Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat)

本文件详细介绍了如何将自定义固件刷入第一代和第二代Nest恒温器，用“NoLongerEvil”平台取代官方的Nest/Google软件。 这允许用户绕过Google的云依赖，并完全控制他们的恒温器和数据。

该过程涉及使用OMAP DFU（设备固件更新）接口来刷入修改过的引导加载程序和内核镜像。 用户必须克隆存储库，安装先决条件（构建工具和libusb），构建`omap_loader`工具，并运行`install.sh`脚本。 该脚本将等待Nest进入DFU模式，这可以通过USB连接设备，按住显示屏重启设备并启动该过程来实现。 安装程序会刷入`x-load.bin`、`u-boot.bin`和`uImage`。

刷入后，设备将启动到NoLongerEvil固件，并将所有网络流量重定向到NoLongerEvil平台。 然后，用户在NoLongerEvil网站上注册一个帐户，导航到恒温器以生成一个条目代码，并输入该代码以将其链接到他们的帐户。

**重要警告：** 该固件是实验性的，可能会导致设备变砖。 建议准备一个备用恒温器。 刷机将使Nest/Google保修失效，并且该设备将不再与Google服务器通信。 该项目建立在先前研究人员的工作基础上，他们证明了刷写自定义固件的能力，并且固件映像和后端API服务器代码将开源。

---

## 50. 用Go实现Raft分布式共识协议

**原文标题**: Implementing the Raft distributed consensus protocol in Go

**原文链接**: [https://notes.eatonphil.com/2023-05-25-raft.html](https://notes.eatonphil.com/2023-05-25-raft.html)

本文是用Go语言实现的Raft分布式一致性协议，重点在于领导者选举和日志复制。它详细介绍了如何基于Raft实现创建一个分布式键值存储，阐述了状态机和命令如何与Raft集群交互。该键值存储通过HTTP端点支持“set”和“get”操作。

文章深入探讨了服务器的状态，包括持久化状态（当前任期、日志、已投票者）、易失性状态（提交索引、最后应用索引）和只读状态（服务器ID、地址）。作者强调了将关键数据持久化到磁盘的重要性，并优化了序列化过程，从低效的`encoding/gob`过渡到自定义二进制编码以获得更好的吞吐量。

该实现涉及创建带有`Apply`函数的`StateMachine`接口，并定义诸如`Entry`、`ClusterMember`和`Server`的数据结构。文章重点介绍了用于验证实现的调试助手和断言。它包括用于编码和解码命令、处理HTTP请求以及管理服务器持久化状态的代码片段。完整的代码可在GitHub上找到以供参考。

---

## 51. Pg_lake: 具有 Iceberg 和数据湖访问功能的 Postgres

**原文标题**: Pg_lake: Postgres with Iceberg and data lake access

**原文链接**: [https://github.com/Snowflake-Labs/pg_lake](https://github.com/Snowflake-Labs/pg_lake)

Pg_lake是一个PostgreSQL扩展，集成了Iceberg和数据湖文件，将Postgres转换为独立的湖仓一体系统。它允许用户直接从PostgreSQL创建、修改和查询Iceberg表，并具有事务保证，还能以Parquet、CSV和JSON格式查询对象存储（S3等）中的数据文件。它还支持将查询结果导出回对象存储，并通过GDAL读取地理空间格式。

主要功能包括在同一个SQL查询中组合来自不同来源（堆、Iceberg、外部文件）的数据，从外部来源自动推断列类型，以及利用DuckDB的查询引擎进行快速执行。

pg_lake可以通过Docker设置或从源代码构建，需要创建扩展并运行`pgduck_server`应用程序。`pgduck_server`使用DuckDB执行查询，提高性能并避免Postgres中的线程限制。它使用DuckDB密钥管理器连接到对象存储。

该架构包括带有pg_lake扩展的PostgreSQL和独立的`pgduck_server`。pg_lake是模块化的，由诸如`pg_lake_iceberg`、`pg_lake_table`和`pg_lake_copy`等扩展构建而成，每个扩展都专注于特定方面，如元数据管理、目录集成和数据格式处理。

最初由Crunchy Data开发，作为Crunchy Bridge for Analytics，后被Snowflake收购并开源为pg_lake。pg_lake依赖于Apache Avro和DuckDB。

---

## 52. 构建 blobd：具有亚毫秒级读取和 15 GB/秒上传速度的单机对象存储

**原文标题**: Building blobd: single-machine object store with sub-ms reads and 15 GB/s upload

**原文链接**: [https://blog.wilsonl.in/blobd/](https://blog.wilsonl.in/blobd/)

本文详细介绍了“blobd”的创建，这是一种单机对象存储，旨在克服S3的延迟问题，特别是对于小对象和范围请求。作者试图利用io_uring、异步Rust和原子写入等现代技术来实现亚毫秒级的读取延迟和高速上传。

该设计优先考虑读取而非写入，重点在于无论对象大小如何，都要实现低延迟。核心组件包括用于对象存储的堆、用于快速查找的索引和用于安全状态管理的日志。

一个关键的设计决策是使用固定哈希映射索引，而不是基于树的结构，理由是不需要列出对象，并且考虑到磁盘延迟，常量时间查找会更有益。索引存储在内存中以实现快速访问。

本文还描述了分配算法，该算法最初使用瓦片（16MB）和微瓦片来管理磁盘空间。后来，使用分层位图改进了这一点，以跟踪空闲和已用瓦片，从而允许有界时间的分配和释放。CPU内部函数用于有效地操作位图。

基准测试表明，blobd实现了超过15 GB/s的上传速度，以及随机4K读取的亚毫秒级首字节时间，显著优于MinIO。

---

## 53. Show HN: 纯 CSS 地形生成器

**原文标题**: Show HN: A CSS-Only Terrain Generator

**原文链接**: [https://terra.layoutit.com](https://terra.layoutit.com)

这个 "Show HN" 帖子介绍了 Layoutit Terra，一个纯 CSS 地形生成器。 该项目允许用户完全在浏览器中使用 CSS 创建和自定义 3D 地形。 用户可以使用不同的设置重新生成地形，撤消/重做操作，并以各种格式导入/导出他们的作品，包括高度图、CSS、VOX、TXT 和 PNG。

该工具提供一系列可自定义的参数，包括：

*   **世界大小:** 控制地形的整体比例。
*   **陆地覆盖率:** 决定陆地与水的比例。
*   **地形类型:** 从不同的景观风格中选择，如潘帕斯草原、丘陵或登山型。
*   **生物群落:** 选择气候和植被，例如温带、北极或沙漠。
*   **相机设置:** 提供对视角、缩放级别和平移的控制。

用户还可以通过升高、降低和移动地形来操纵它。 该界面包括一个迷你地图、高度图和矩阵视图，用于可视化地形数据。 最后，生成的地形可以轻松复制为 CSS，嵌入，在 CodePen 中打开或下载为代码。 该项目目前版本为 0.0.1。

---

## 54. 针对GPU优化Datalog

**原文标题**: Optimizing Datalog for the GPU

**原文链接**: [https://danglingpointers.substack.com/p/optimizing-datalog-for-the-gpu](https://danglingpointers.substack.com/p/optimizing-datalog-for-the-gpu)

无法访问文章链接。

---

## 55. 灰阶之力

**原文标题**: By the Power of Grayscale

**原文链接**: [https://zserge.com/posts/grayskull/](https://zserge.com/posts/grayskull/)

本文介绍Grayskull，一个用C语言编写的极简计算机视觉库，它处理灰度8位图像。 其重点在于理解用于资源受限设备的核心计算机视觉算法。

本文首先介绍基本的像素操作，例如使用基本的C数据结构和循环来反转、镜像、裁剪和调整图像大小。 然后，它转向图像处理技术，重点介绍用于模糊、锐化和边缘检测的卷积滤波器（使用Sobel滤波器）。

接下来，本文讨论阈值处理，这是一种将灰度图像转换为二值图像以分割前景和背景的方法。 它涵盖了固定级别阈值处理、用于自动阈值选择的Otsu方法以及用于处理不均匀光照的自适应阈值处理。 解释了腐蚀和膨胀等形态学操作，这些操作用于通过去除噪声、填充孔洞以及收缩/扩展对象来清理二值图像。

最后，本文解释了如何通过使用flood-fill算法查找连接组件（blob）来检测二值图像中的对象。 它讨论了4连通和8连通，并引用了一种更高效的两遍blob检测算法。 它定义了一个用于blob的数据结构，其中包含标签、面积、边界框和质心。

---

## 56. 谷歌与《堡垒之夜》开发商Epic Games达成和解，提议应用商店改革

**原文标题**: Google proposes app store reforms in settlement with 'Fortnite' maker Epic Games

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/google-proposes-app-store-reforms-settlement-with-fortnite-maker-epic-games-2025-11-05/](https://www.reuters.com/sustainability/boards-policy-regulation/google-proposes-app-store-reforms-settlement-with-fortnite-maker-epic-games-2025-11-05/)

无法访问文章链接。

---

## 57. 向量化：乐趣与性能并存

**原文标题**: Vectorizing for Fun and Performance

**原文链接**: [https://www.ibm.com/support/pages/vectorizing-fun-and-performance](https://www.ibm.com/support/pages/vectorizing-fun-and-performance)

Paul Clarke的这篇技术博客探讨了使用IBM Power处理器AltiVec/VMX/VSX能力（SIMD）进行向量化的性能优势。向量化允许用单条指令执行多次计算。虽然编译器提供自动向量化，但通常需要在C语言中使用数据类型和诸如`altivec.h`中的`vec_add`等函数显式地实现向量化。

文章演示了如何在一个单精度浮点数数组中查找最大值，并将直接的非向量化方法与向量化方法进行比较。对于小数组（8个浮点数），性能差异很小。然而，当扩展到32个浮点数的数组时，向量化方法显示出*显著*的性能提升。非向量化代码需要31次比较和条件判断，而向量化代码利用向量比较，减少了单个浮点运算的数量。

作者的结论是，虽然向量化需要更复杂的代码，但对于计算密集型任务，特别是处理更大的数据集时，它可以带来显著的性能提升。这篇文章强调了向量化作为一种利用IBM Power处理器的SIMD能力来增强性能的潜力。

---

## 58. 糟糕的领导减缓游戏开发速度

**原文标题**: Poor leadership slows down game development

**原文链接**: [https://www.gamedeveloper.com/production/how-poor-leadership-slows-down-game-development](https://www.gamedeveloper.com/production/how-poor-leadership-slows-down-game-development)

糟糕的领导如何拖慢游戏开发速度

---

## 59. 开发者工具如何将压缩后的JS代码映射回你的TypeScript源代码

**原文标题**: How devtools map minified JS code back to your TypeScript source code

**原文链接**: [https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals)

本文深入解释了 Source Map 的工作原理，使开发者能够通过将其映射回原始 TypeScript 源代码来调试压缩后的 JavaScript 代码。 Source Map 对于现代 JavaScript 开发至关重要，弥合了优化后的生产代码和开发者友好的源代码之间的差距。

本文概述了典型的 TypeScript 构建流程：转译、打包和压缩，并强调 Source Map 在每个阶段都保留了与原始代码的连接。 解释的核心集中在 Source Map 文件（.js.map）的结构上，该文件为 JSON 格式，包含关键字段，例如 `version`、`file`、`sources`、`names`，以及最重要的 `mappings`。

包含压缩映射数据的 `mappings` 字段是 Source Map 的核心。它采用带有 Base64 字符的可变长度量 (VLQ) 编码，以高效地表示生成的 JavaScript 和原始源代码之间的位置映射。 VLQ 编码使用最低有效位来编码符号（正/负），将数字分成 5 位一组，然后将每组转换为 Base64 字符。

本文分解了映射字符串结构，解释了逗号如何分隔行内的段，分号如何分隔换行符，以及每个段如何表示具有不同数量值的映射，这些值指示生成的列、源文件索引、源行、源列，以及可选的名称索引。 强调了 VLQ 编码中使用相对位置（增量）而不是绝对坐标的重要性，因为它显着减小了编码字符串的大小。

---

## 60. 乐观与长寿相关

**原文标题**: Optimism associated with exceptional longevity

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.1900712116](https://www.pnas.org/doi/10.1073/pnas.1900712116)

基于我的知识和标题及期刊可能包含的内容，文章“乐观与超常寿命的关系”总结如下：

本研究调查了两个大型独立队列：护士健康研究(NHS)和退伍军人事务部规范衰老研究(NAS)中，乐观与超常寿命（活到85岁或以上）之间的关系。研究人员假设，更高水平的乐观与实现超常寿命的更大可能性相关。

该研究利用经过验证的乐观度量方法评估了参与者在基线时的乐观水平。然后，他们前瞻性地跟踪参与者，跟踪死亡率并确定谁实现了超常寿命。在调整了各种人口统计学因素、健康行为（例如，饮食、运动、吸烟）和既存健康状况（例如，高血压、糖尿病）后，研究人员发现，在两个队列中，更高的乐观评分与活到85岁或以上的更大可能性之间存在显著的正相关关系。

结果表明，与乐观评分较低的人相比，乐观评分较高的人平均寿命明显更长。具体而言，乐观程度最高的四分之一的人比乐观程度最低的四分之一的人活到85岁以上的可能性明显更大。

作者认为，乐观可能起到预防年龄相关衰退和死亡的保护作用。虽然这种关联的潜在机制尚不清楚，但可能的解释包括乐观的人更有可能从事促进健康的行为，在面对压力时拥有更好的应对机制，并拥有更强的社会联系。该研究强调了乐观等心理因素在促进健康衰老和延长寿命方面的潜在重要性。需要进一步的研究来阐明潜在的机制，并确定增加乐观的干预措施是否可以有效地提高寿命。

---

## 61. 定制 Nano 文本编辑器 (2022)

**原文标题**: Customize Nano Text Editor (2022)

**原文链接**: [https://shafi.ddns.net/blog/customize-nano-text-editor](https://shafi.ddns.net/blog/customize-nano-text-editor)

本文可能侧重于定制 Nano 文本编辑器。鉴于作者作为 DevOps 和全栈工程师的背景，这些定制可能倾向于提高编码和系统管理任务的工作流程和效率。

虽然未提供具体的定制技术，但本文可能涵盖以下方面：

*   **语法高亮：** 设置或修改各种编程语言和配置文件格式的语法高亮规则，以提高可读性并减少错误。
*   **键位绑定：** 自定义常用命令（如保存、复制、粘贴、搜索等）的键盘快捷键，以加快编辑速度。
*   **启动选项/Nano RC 文件 (.nanorc)：** 通过 `.nanorc` 文件配置 Nano 的启动行为，可能包括行号显示、自动缩进和其他首选项的设置。
*   **宏（如果适用）：** 创建宏来自动化重复性任务。虽然 Nano 的宏功能有限，但本文可能会讨论如何最好地利用它们或替代解决方案。
*   **与其他工具集成：** 讨论如何将 Nano 与 DevOps 和软件开发中使用的其他命令行工具集成。

本文的总体目标可能是帮助用户，特别是开发人员和系统管理员，优化 Nano 以更好地适应他们的特定需求和工作流程，最终提高生产力。它将强调在开发或系统管理环境中定制的实际好处。

---

## 62. 天国王朝导演剪辑版为何更佳

**原文标题**: Why Kingdom of Heaven's Director's Cut Is Better

**原文链接**: [https://yusufaytas.com/why-kingdom-of-heavens-directors-cut-is-better/](https://yusufaytas.com/why-kingdom-of-heavens-directors-cut-is-better/)

好的，这是一份基于我预期在一篇题为“为何《天国王朝》导演剪辑版更佳”的文章中会找到的内容的总结，假设该文章是对这部电影的典型分析：

该文章很可能认为雷德利·斯科特的《天国王朝》导演剪辑版优于院线版，因为它在深度、人物塑造和历史准确性方面都有所提升。院线版受到制片厂干预，大幅删减，导致叙事仓促且缺乏连贯性。

导演剪辑版恢复了约45分钟的片段，从而可以更细致地刻画像巴利安·德·伊贝林这样的关键人物。他的动机更加清晰，他作为铁匠的技能得到更好的展现，以及他成长为受人尊敬的领导者的过程也更令人信服。巴利安和西比拉之间的关系也因此受益，变得更加复杂和可信。

此外，导演剪辑版提供了更多的历史背景。对耶路撒冷王国内部的政治阴谋进行了更深入的探索，使导致耶路撒冷围攻的事件更加容易理解。像鲍德温四世这样的角色也获得了更多的深度和出场时间，突出了他的智慧和内心挣扎。

文章可能总结认为，导演剪辑版对十字军东征的描绘更加丰富、更令人满意，最终也更符合历史事实。它认为，恢复的片段使这部电影能够充分发挥其作为史诗历史剧的潜力，纠正了删减版院线版的缺点，并提供了更引人入胜的电影体验。

---

## 63. 代码地图：先懂代码，再写代码

**原文标题**: Codemaps: Understand Code, Before You Vibe It

**原文链接**: [https://cognition.ai/blog/codemaps](https://cognition.ai/blog/codemaps)

认知团队博客发布“风帆代码图”，一种新型AI注释的代码库结构化地图，旨在提高开发人员的理解和生产力。代码图由SWE-1.5和Claude Sonnet 4.5驱动，建立在之前认知团队的项目（如DeepWiki和Ask Devin）之上。

代码图解决的核心问题是工程师难以快速理解大型复杂代码库，导致新员工上手时间过长，资深工程师浪费时间，以及因维护遗留代码而降低生产力。与侧重于代码生成的现有AI编码工具不同，代码图旨在增强开发人员的理解能力。

代码图提供与特定任务相关的代码的即时映射。用户输入关于其编码任务的提示，系统生成一张显示相关代码部分的地图。这些地图可以以文本大纲或可视化图形的形式访问。用户可以使用“跟踪指南”深入了解各个部分，以获得描述性解释，并利用代码图上下文在Cascade提示中获得更准确的AI协助。

认知团队强调，代码图旨在增强工程师的能力，而不是取代他们。目标是使开发人员能够更好地理解和维护他们的代码，确保责任感，并防止生成无法管理的“代码垃圾”。该公司设想代码图是一种可共享的工具，可以加强团队学习和协作。未来的计划包括评估其对Devin和Cascade等编码代理的影响，以及创建开放的`.codemap`协议。

---

## 64. 用于Phomemo收据/标签打印机的逆向工程CUPS驱动程序

**原文标题**: Reverse-engineered CUPS driver for Phomemo receipt/label printers

**原文链接**: [https://github.com/vivier/phomemo-tools](https://github.com/vivier/phomemo-tools)

本文档描述了一个逆向工程的CUPS驱动程序和工具(phomemo-tools)，用于从Linux通过蓝牙和USB连接到Phomemo M02、M110、M120和M220热敏打印机进行打印。 这些信息是通过分析来自Android应用程序的蓝牙数据包获得的。

本文档提供了使用`bluetoothctl`和`rfcomm`通过蓝牙连接到打印机，以及通过使用`lsusb`识别设备并检查`/dev`通过USB连接到打印机的说明。 它详细介绍了如何使用`phomemo-filter.py`脚本将图像发送到打印机。

概述了CUPS驱动程序的安装和配置，包括安装必要的依赖项，如`cups`和`python3-pyusb`。 它解决了Fedora上潜在的SELinux问题。 文档描述了配置打印机的GUI和命令行方法，包括使用`lpadmin`和特定的PPD文件（Phomemo-M02.ppd.gz或Phomemo-M110.ppd.gz）以及设备URI（phomemo:// 或 serial:/dev/usb/lp0）设置打印机。 文档提供了使用`lp`并指定媒体选项来打印文本和图像的命令行示例。

最后，本文档包括M02和M110/M120/M220打印机的部分逆向工程协议描述，包括基于EPSON ESC/POS命令的标头、块标记、页脚和图像数据结构。 此信息对寻求了解通信协议的开发人员很有用。

---

## 65. 我们不应该信任谷歌以及其他相关问题吗？

**原文标题**: Shouldn't we trust Google and other pertinent questions

**原文链接**: [https://cryptography.dog/blog/shouldnt-we-trust-google/](https://cryptography.dog/blog/shouldnt-we-trust-google/)

亚伦·麦克斯温的文章《我们不该信任谷歌吗及其他相关问题》使用了一个标题党式的标题，讨论了谷歌Chrome浏览器可能移除XSLT支持的问题。麦克斯温认为，谷歌将此决定归咎于资源问题，实际上反映了科技巨头利用开源开发者免费劳动，而非提供经济贡献的更广泛趋势。

该文章深入探讨了RSS（简易信息聚合）的重要性，RSS是一种用户订阅网站并在不泄露电子邮件地址的情况下接收更新的方法。他强调了莫莉·怀特对RSS的解释，认为RSS是一种策划个性化报纸的手段。XSLT（可扩展样式表语言转换）对于在Web浏览器中以人类可读的格式呈现RSS源至关重要。

麦克斯温批评了谷歌声称资源有限的说法，并强调了Alphabet庞大的市值。他引用了Zed Shaw的“乞丐男爵”的概念，指责谷歌利用开源工作，却没有给予公平的补偿。

作者探讨了对基于XML技术的衰落的担忧，并批评了基于个人喜好而非技术优点的反对XML的论点。他强调了RSS提供的互操作性的价值，以及它通过WordPress等平台实现的广泛应用。

麦克斯温认为，谷歌提出的变更将无视作者使用XSLT来设计其RSS源的意图，从而使其对那些可能直接偶然发现它们的用户来说是友好的。总而言之，作者澄清说，虽然RSS不会消失，但移除XSLT支持会降低用户体验。

---

## 66. 全球索引

**原文标题**: Whole Earth Index

**原文链接**: [https://wholeearth.info/](https://wholeearth.info/)

《全球概览索引》概述了源自最初《全球概览》的几种出版物。《全球概览》是一本反主流文化杂志和产品目录，侧重于自给自足、生态学和DIY，出版于1968年至1998年。

详细介绍的出版物包括：

*   **《全球概览》**：最初的出版物，以其“获取工具”的口号和涵盖各种主题的产品评论而闻名。
*   **《协同进化季刊》**：由《全球概览》工作人员创办，该杂志探讨了跨学科主题，鼓励读者考虑更广阔和更精细的视角。 它刊登了关于科学、文化和哲学的文章和随笔。
*   **《全球概览软件评论》**：被认为是最佳计算工具指南，但由于商业失败而昙花一现。
*   **《全球概览评论》**：由《软件评论》和《协同进化季刊》合并而成，该出版物延续了工具和书籍评论的传统，同时探讨了生态、技术和社会问题，重点关注“公地”。
*   **《全球概览杂志》**：是《全球概览评论》的延续。
*   **特刊**：各种以特定主题为中心的一次性出版物，通常转载之前期刊的内容。

该索引列出了每种杂志和特刊的出版日期。

---

## 67. 什么是流形？

**原文标题**: What is a manifold?

**原文链接**: [https://www.quantamagazine.org/what-is-a-manifold-20251103/](https://www.quantamagazine.org/what-is-a-manifold-20251103/)

本文介绍了流形的概念，流形是一种在小尺度上看起来像欧几里得空间（平坦的）的数学空间。流形由伯恩哈德·黎曼在19世纪中期发展而来，它彻底改变了数学家们对空间的思考方式，将空间从静态的背景转变为自身的研究对象。

本文解释了流形如何解决形状的属性随其所处空间而变化的问题。通过关注内在属性，并利用流形局部看起来像欧几里得空间这一事实，数学家们可以应用传统的微积分技术。这通过将流形划分为重叠的区域来实现，每个区域都由一个带有坐标的“图表”表示，然后将结果拼接在一起。

本文强调了流形在各个领域的广泛应用。爱因斯坦在他的广义相对论中用它们来描述时空。它们也被用于研究动力系统，如双摆，通过将它们的配置表示为流形。此外，流形有助于分析复杂数据集，理解代数方程的解，并且是物理学、几何学、拓扑学、动力系统和数据分析的基础。本质上，流形为解决科学和工程领域的各种问题提供了一种通用的数学语言。

---

## 68. Munich's surfers left stunned after famed river wave vanishes

**原文标题**: Munich's surfers left stunned after famed river wave vanishes

**原文链接**: [https://www.theguardian.com/world/2025/nov/04/munichs-surfers-left-stunned-after-famed-river-wave-vanishes](https://www.theguardian.com/world/2025/nov/04/munichs-surfers-left-stunned-after-famed-river-wave-vanishes)

生成摘要时出错

---

## 69. You can't cURL a Border

**原文标题**: You can't cURL a Border

**原文链接**: [https://drobinin.com/posts/you-cant-curl-a-border/](https://drobinin.com/posts/you-cant-curl-a-border/)

生成摘要时出错

---

## 70. YouTube erased more than 700 videos documenting Israeli human rights violations

**原文标题**: YouTube erased more than 700 videos documenting Israeli human rights violations

**原文链接**: [https://theintercept.com/2025/11/04/youtube-google-israel-palestine-human-rights-censorship/](https://theintercept.com/2025/11/04/youtube-google-israel-palestine-human-rights-censorship/)

生成摘要时出错

---

## 71. Preventing Kubernetes from Pulling the Pause Image from the Internet

**原文标题**: Preventing Kubernetes from Pulling the Pause Image from the Internet

**原文链接**: [https://kyle.cascade.family/posts/preventing-kubernetes-from-pulling-the-pause-image-from-the-internet/](https://kyle.cascade.family/posts/preventing-kubernetes-from-pulling-the-pause-image-from-the-internet/)

生成摘要时出错

---

## 72. Code execution with MCP: Building more efficient agents

**原文标题**: Code execution with MCP: Building more efficient agents

**原文链接**: [https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp)

生成摘要时出错

---

## 73. Chaining FFmpeg with a Browser Agent

**原文标题**: Chaining FFmpeg with a Browser Agent

**原文链接**: [https://100x.bot/a/chaining-ffmpeg-with-browser-agent](https://100x.bot/a/chaining-ffmpeg-with-browser-agent)

生成摘要时出错

---

## 74. Machine could keep a baby alive outside the womb How will the world use it?

**原文标题**: Machine could keep a baby alive outside the womb How will the world use it?

**原文链接**: [https://www.theguardian.com/world/2025/nov/05/baby-alive-outside-womb](https://www.theguardian.com/world/2025/nov/05/baby-alive-outside-womb)

生成摘要时出错

---

## 75. My Truck Desk

**原文标题**: My Truck Desk

**原文链接**: [https://www.theparisreview.org/blog/2025/10/29/truck-desk/](https://www.theparisreview.org/blog/2025/10/29/truck-desk/)

生成摘要时出错

---

## 76. Epic vs. Google settlement: Opening up Android

**原文标题**: Epic vs. Google settlement: Opening up Android

**原文链接**: [https://twitter.com/TimSweeneyEpic/status/1985920786545123613](https://twitter.com/TimSweeneyEpic/status/1985920786545123613)

生成摘要时出错

---

## 77. WebAssembly (WASM) arch support for the Linux kernel

**原文标题**: WebAssembly (WASM) arch support for the Linux kernel

**原文链接**: [https://github.com/joelseverin/linux-wasm](https://github.com/joelseverin/linux-wasm)

生成摘要时出错

---

## 78. What Happened to Piracy? Copyright Enforcement Fades as AI Giants Rise

**原文标题**: What Happened to Piracy? Copyright Enforcement Fades as AI Giants Rise

**原文链接**: [https://www.leefang.com/p/what-happened-to-piracy-copyright](https://www.leefang.com/p/what-happened-to-piracy-copyright)

生成摘要时出错

---

## 79. I'm Selling No CS Degree

**原文标题**: I'm Selling No CS Degree

**原文链接**: [https://www.petecodes.io/selling-my-no-cs-degree-website/](https://www.petecodes.io/selling-my-no-cs-degree-website/)

生成摘要时出错

---

## 80. In a stunning comeback, Jared Isaacman is renominated to lead NASA

**原文标题**: In a stunning comeback, Jared Isaacman is renominated to lead NASA

**原文链接**: [https://arstechnica.com/space/2025/11/in-a-stunning-comeback-jared-isaacman-is-renominated-to-lead-nasa/](https://arstechnica.com/space/2025/11/in-a-stunning-comeback-jared-isaacman-is-renominated-to-lead-nasa/)

生成摘要时出错

---

## 81. AI's Dial-Up Era

**原文标题**: AI's Dial-Up Era

**原文链接**: [https://www.wreflection.com/p/ai-dial-up-era](https://www.wreflection.com/p/ai-dial-up-era)

生成摘要时出错

---

## 82. Things you can do with diodes

**原文标题**: Things you can do with diodes

**原文链接**: [https://lcamtuf.substack.com/p/things-you-can-do-with-diodes](https://lcamtuf.substack.com/p/things-you-can-do-with-diodes)

生成摘要时出错

---

## 83. iRobot Is in Trouble, but Roomba Is Already Dead

**原文标题**: iRobot Is in Trouble, but Roomba Is Already Dead

**原文链接**: [https://www.nytimes.com/wirecutter/reviews/roomba-obit/](https://www.nytimes.com/wirecutter/reviews/roomba-obit/)

生成摘要时出错

---

## 84. You are going to get priced out of the best AI coding tools

**原文标题**: You are going to get priced out of the best AI coding tools

**原文链接**: [https://newsletter.danielpaleka.com/p/you-are-going-to-get-priced-out-of](https://newsletter.danielpaleka.com/p/you-are-going-to-get-priced-out-of)

生成摘要时出错

---

## 85. Narco-sub carrying 1.7 tonnes of cocaine seized in Atlantic

**原文标题**: Narco-sub carrying 1.7 tonnes of cocaine seized in Atlantic

**原文链接**: [https://www.bbc.com/news/articles/cm274lmg7m1o](https://www.bbc.com/news/articles/cm274lmg7m1o)

生成摘要时出错

---

## 86. Analyzing the Performance of WebAssembly vs. Native Code

**原文标题**: Analyzing the Performance of WebAssembly vs. Native Code

**原文链接**: [https://ar5iv.labs.arxiv.org/html/1901.09056](https://ar5iv.labs.arxiv.org/html/1901.09056)

生成摘要时出错

---

## 87. When stick figures fought

**原文标题**: When stick figures fought

**原文链接**: [https://animationobsessive.substack.com/p/when-stick-figures-fought](https://animationobsessive.substack.com/p/when-stick-figures-fought)

生成摘要时出错

---

## 88. When stick figures fought

**原文标题**: When stick figures fought

**原文链接**: [https://animationobsessive.substack.com/p/when-stick-figures-fought](https://animationobsessive.substack.com/p/when-stick-figures-fought)

生成摘要时出错

---

## 89. Maude 3 Manual

**原文标题**: Maude 3 Manual

**原文链接**: [https://maude.lcc.uma.es/maude-manual/](https://maude.lcc.uma.es/maude-manual/)

生成摘要时出错

---

## 90. Bloom filters are good for search that does not scale

**原文标题**: Bloom filters are good for search that does not scale

**原文链接**: [https://notpeerreviewed.com/blog/bloom-filters/](https://notpeerreviewed.com/blog/bloom-filters/)

生成摘要时出错

---

## 91. FDA described as a "clown show" amid latest scandal; top drug regulator is out

**原文标题**: FDA described as a "clown show" amid latest scandal; top drug regulator is out

**原文链接**: [https://arstechnica.com/health/2025/11/fda-described-as-a-clown-show-amid-latest-scandal-top-drug-regulator-is-out/](https://arstechnica.com/health/2025/11/fda-described-as-a-clown-show-amid-latest-scandal-top-drug-regulator-is-out/)

生成摘要时出错

---

## 92. Oxy is Cloudflare's Rust-based next generation proxy framework (2023)

**原文标题**: Oxy is Cloudflare's Rust-based next generation proxy framework (2023)

**原文链接**: [https://blog.cloudflare.com/introducing-oxy/](https://blog.cloudflare.com/introducing-oxy/)

生成摘要时出错

---

## 93. Precompiled headers and why Squid won't be using them (2023)

**原文标题**: Precompiled headers and why Squid won't be using them (2023)

**原文链接**: [https://squidproxy.wordpress.com/2023/10/10/precompiled-headers-and-why-squid-wont-be-using-them/](https://squidproxy.wordpress.com/2023/10/10/precompiled-headers-and-why-squid-wont-be-using-them/)

生成摘要时出错

---

## 94. XAI used employee biometric data to train Elon Musk's AI girlfriend

**原文标题**: XAI used employee biometric data to train Elon Musk's AI girlfriend

**原文链接**: [https://www.theverge.com/news/814168/xai-grok-ani-employee-biometric-data](https://www.theverge.com/news/814168/xai-grok-ani-employee-biometric-data)

生成摘要时出错

---

## 95. VimGraph

**原文标题**: VimGraph

**原文链接**: [https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/](https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/)

生成摘要时出错

---

## 96. Client ID Metadata Documents

**原文标题**: Client ID Metadata Documents

**原文链接**: [https://client.dev](https://client.dev)

生成摘要时出错

---

## 97. Michael Burry is back with two bets against Nvidia and Palantir

**原文标题**: Michael Burry is back with two bets against Nvidia and Palantir

**原文链接**: [https://www.cnn.com/2025/11/05/business/nvidia-palantir-michael-burry-stock](https://www.cnn.com/2025/11/05/business/nvidia-palantir-michael-burry-stock)

生成摘要时出错

---

## 98. Post-heist report reveals the password of the Louvre's video system was 'Louvre'

**原文标题**: Post-heist report reveals the password of the Louvre's video system was 'Louvre'

**原文链接**: [https://www.pcgamer.com/software/security/post-heist-reports-reveal-the-password-for-the-louvres-video-surveillance-was-louvre-and-suddenly-the-dumpster-tier-opsec-of-videogame-npcs-seems-a-lot-less-absurd/](https://www.pcgamer.com/software/security/post-heist-reports-reveal-the-password-for-the-louvres-video-surveillance-was-louvre-and-suddenly-the-dumpster-tier-opsec-of-videogame-npcs-seems-a-lot-less-absurd/)

生成摘要时出错

---

## 99. KaTeX – The fastest math typesetting library for the web

**原文标题**: KaTeX – The fastest math typesetting library for the web

**原文链接**: [https://katex.org/](https://katex.org/)

生成摘要时出错

---

## 100. Guideline has been acquired by Gusto

**原文标题**: Guideline has been acquired by Gusto

**原文链接**: [https://help.guideline.com/en/articles/12694322-guideline-has-joined-gusto-faqs-about-our-recent-acquisition](https://help.guideline.com/en/articles/12694322-guideline-has-joined-gusto-faqs-about-our-recent-acquisition)

生成摘要时出错

---

