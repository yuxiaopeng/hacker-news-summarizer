# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-16.md)

*最后自动更新时间: 2025-08-16 17:47:59*
## 1. 头发制成的牙膏，天然固本修护牙齿。

**原文标题**: Toothpaste made from hair provides natural root to repair teeth

**原文链接**: [https://www.kcl.ac.uk/news/toothpaste-made-from-hair-provides-natural-root-to-repair-teeth](https://www.kcl.ac.uk/news/toothpaste-made-from-hair-provides-natural-root-to-repair-teeth)

2025年8月，伦敦国王学院的科学家宣布在牙科护理方面取得突破：一种由角蛋白（一种存在于头发、皮肤和羊毛中的蛋白质）制成的牙膏可以修复牙釉质并阻止早期龋齿。该研究发表在《先进医疗保健材料》上，详细介绍了角蛋白如何形成一种保护性涂层，在与唾液中的矿物质相互作用时，模仿天然牙釉质。

与仅能减缓龋齿的含氟牙膏不同，基于角蛋白的治疗方法可以通过形成致密的矿物质层来完全阻止龋齿，该矿物质层可以保护牙齿并封闭暴露的神经通道，从而减轻敏感性。该疗法可能会在2-3年内以牙膏或专业涂抹的凝胶形式上市。

该团队从羊毛中提取角蛋白，将其应用于牙齿表面，形成类似晶体的支架，吸引钙和磷酸根离子，并生长出类似牙釉质的涂层。这标志着再生牙科领域的重大进展。

研究员萨拉·加梅亚强调了角蛋白从生物废物中可持续获取的特性，以及它在修复牙科中替代有毒塑料树脂的作用。它还能更自然地匹配牙齿颜色。随着人们越来越关注医疗保健材料的可持续性和长期使用氟化物的问题，角蛋白作为一种有希望的替代品脱颖而出，与废物转化为健康的创新相一致。

Elsharkawy 博士设想，在未来，生物技术能够利用人体自身的材料来恢复生物功能，从而可能通过简单的理发带来更坚固、更健康的笑容。

---

## 2. 好的系统设计

**原文标题**: Good system design

**原文链接**: [https://www.seangoedecke.com/good-system-design/](https://www.seangoedecke.com/good-system-design/)

本文概述了良好系统设计的原则，强调简洁和最小化复杂性。系统设计涉及组装服务，类似于软件设计组装代码行。好的设计是“平淡无奇”的，其特点是易于实现和可靠运行，而过于复杂的系统往往掩盖了根本的设计缺陷。

一个核心原则是尽量减少有状态组件，因为它们容易出错且难以自动修复。作者提倡将状态管理隔离到与数据库交互的单个服务，而其他服务保持无状态。

数据库至关重要，精心设计的模式和索引必不可少。性能瓶颈可以通过优化数据库查询（使用JOIN）、利用只读副本以及限制查询峰值来缓解。

对于慢速操作，作者建议将工作分成面向用户的即时任务和由队列系统管理的后台作业。缓存是另一种提高性能的策略，但由于其固有的有状态性，应谨慎使用。作者建议使用诸如使用带有文档存储的计划作业之类的替代缓存方法。

事件由Kafka之类的事件中心管理，可在不需要立即响应时促进服务之间的通信。最后，本文讨论了“推送”和“拉取”数据，主张在高效且可扩展的情况下，特别是当向大量客户端提供频繁更新的信息时，将数据推送到客户端。

---

## 3. 支付处理器乐趣 2025 – 自建你的商户服务提供商

**原文标题**: Payment Processor Fun 2025 – Making Your Own Merchant Service Provider

**原文链接**: [https://voidfox.com/blog/payment_processor_fun_2025_making_your_own_msp/](https://voidfox.com/blog/payment_processor_fun_2025_making_your_own_msp/)

本文剖析了支付处理的复杂性，以及为何对于面临压力要移除成人内容（由于支付处理商的限制）的Itch等平台来说，它不是一个简单的解决方案。

作者是一位拥有金融科技经验的站点可靠性工程师，他解释了支付生态系统的复杂层次：支付卡网络（Visa、Mastercard）、收单行（银行）、商户服务提供商（MSP）、支付便利商（PayFac，如Stripe、PayPal）、商户（Itch）以及子商户（Itch创作者）。 他强调，建立PayFac需要银行（收单行）的赞助，以及在安全性、合规性（KYC）和可靠性方面的大量资源。与成人内容相关的“风险”（高拒付率、法律问题）使得获得赞助变得困难。

文章驳斥了Itch可以轻松创建自己的支付处理商或使用处理成人内容的支付处理商的想法。 开发自己的PayFac或成为收单行在财务和后勤上都是不可行的，尤其是考虑到Itch的规模较小。 此外，Itch已经通过处理成人内容违反了PayPal和Stripe等PayFac的服务条款。

切换到像CCBill这样的“高风险”PayFac是可能的，但会带来高昂的费用（15% + 1美元/次刷卡）和托管要求（年度支付额的25%），这使得它不切实际。 此外，作者强调，一些高风险服务商可能会因成人内容的法律风险表面而将其排除在外。

---

## 4. 箭鹳

**原文标题**: Pfeilstorch

**原文链接**: [https://en.wikipedia.org/wiki/Pfeilstorch](https://en.wikipedia.org/wiki/Pfeilstorch)

箭鹳（德语：Pfeilstorch）是指从非洲迁徙回欧洲时，身体上插着箭或矛的白鹳。截至2003年，德国已记录到约25起此类案例。

最著名的箭鹳于1822年在德国克吕茨附近被发现，它身上带着一根来自非洲中部的75厘米长的矛。这只特殊的鸟，现在被称为罗斯托克箭鹳，保存在罗斯托克大学的动物学收藏中，在理解鸟类迁徙方面发挥了关键作用。在迁徙的概念被广泛接受之前，人们试图用各种理论来解释鸟类在冬季的消失，包括变成其他动物或冬眠。罗斯托克箭鹳提供了确凿的证据，证明鸟类会进行长途迁徙到越冬地。

虽然由于弓箭被枪支取代，带有箭矢的鸟类目击事件有所减少，但箭鹳仍然是鸟类学研究中一个重要的历史象征，代表着理解鸟类迁徙模式的一个关键时刻。

---

## 5. PuTTY有了一个新网站。

**原文标题**: PuTTY has a new website

**原文链接**: [https://putty.software/](https://putty.software/)

PuTTY，一款主要用于Windows和类Unix系统（包括xterm风格终端）的免费SSH和终端仿真客户端，有了新的网站。该软件主要由Simon Tatham开发和维护。用户可以直接访问下载页面获取最新版本，或访问主网站获取更全面的信息。

---

## 6. 几天内从头开始用 Ada 编写有竞争力的 BZip2 编码器 – 第二部分

**原文标题**: Writing a competitive BZip2 encoder in Ada from scratch in a few days – part 2

**原文链接**: [https://gautiersblog.blogspot.com/2025/07/writing-bzip2-encoder-in-ada-from.html](https://gautiersblog.blogspot.com/2025/07/writing-bzip2-encoder-in-ada-from.html)

无法访问文章链接。

---

## 7. 给开发者的陷阱

**原文标题**: Traps to Developers

**原文链接**: [https://qouteall.fun/qouteall-blog/2025/Traps%20to%20Developers](https://qouteall.fun/qouteall-blog/2025/Traps%20to%20Developers)

本文总结了开发者在使用各种技术时可能遇到的常见陷阱和不直观的行为，这些行为可能导致错误和意外结果。

**HTML/CSS:** 重点介绍 `min-width`、水平与垂直布局、外边距折叠、块格式化上下文 (BFC)、堆叠上下文、移动设备上的视口高度、绝对定位、flex/grid 中的浮动元素、基于百分比的尺寸、空白处理、box-sizing、累积布局偏移以及文件下载请求检查的细微之处。

**Unicode & 文本编码:** 解释了码位与字形簇、UTF-8/UTF-16、不同语言（Rust、Go、Java、C#、JS、Python、C++）中的不同字符串实现、BOM、易混淆字符、规范化、零宽度/不可见字符以及 Unicode 统一。

**浮点数:** 讨论了 NaN 的独特属性、无穷大、负零、直接比较问题、JavaScript 中的浮点数表示、结合律和分配律失效、除法性能、硬件特定行为（FMA、次正规数、舍入模式）以及提高精度的技术。

**时间:** 讨论了闰秒、时区、夏令时 (DST)、NTP 同步、服务器时区配置以及硬件时钟与系统时钟。

**特定语言：**
*   **Java:** `==` 与 `.equals`、`equals`/`hashCode` 重写、可变 Map 键、不可变 List 返回值、`Optional` 空值、在 `finally` 中吞噬异常、线程池异常处理、八进制字面量、调试器副作用。
*   **Golang:** `append` 行为、`defer` 执行时机和变量捕获、nil 切片与空切片、接口 nil 怪异现象、死等待、超时问题。
*   **C/C++:** Vector 重新分配和指针失效、临时字符串、迭代器失效、`std::remove` 与 `erase`、八进制字面量、未定义行为（未初始化的内存、空指针、整数溢出、别名、未对齐的内存访问）、对齐。

---

## 8. 用数学最优方法切洋葱

**原文标题**: Dicing an Onion, the Mathematically Optimal Way

**原文链接**: [https://pudding.cool/2025/08/onions/](https://pudding.cool/2025/08/onions/)

本文探讨了将洋葱切成丁以获得最均匀块状的数学最优方法。文章首先研究了常见的切丁技术，即垂直和放射状切割，并使用相对标准偏差 (RSD) 分析块状大小的变化，其中较低的 RSD 表示更均匀的块状。

文章随后深入研究了 J. Kenji López-Alt 关于在洋葱半径约 60% 深度进行放射状切割的说法，数学分析支持了这一说法，表明 34.5% 是我们目前看到的最小标准偏差。然而，文章进一步研究了如何通过有限数量的切割和层数来优化切丁，结果表明，在 10 层洋葱中以 96% 的深度进行 10 次放射状切割，RSD 降低至 29.5%。

该分析考虑了 19,320 种层数、切割次数和切割深度的组合。研究发现，根据切割次数和层数以不同深度进行的放射状切割通常优于垂直切割。水平切割很少能提高均匀性。理想的放射状深度始终≥48%，并且随着层数和切割次数的增加，接近约 55.731% 的“洋葱常数”。

最后，文章以 J. Kenji López-Alt 的实际检验作为结论，他指出，实现数学上完美的均匀性对于理论讨论比实际烹饪更有意义，洋葱丁大小的细微变化不会显着影响菜肴的结果。

---

## 9. Git中大型文件的未来是Git

**原文标题**: The future of large files in Git is Git

**原文链接**: [https://tylercipriani.com/blog/2025/08/15/git-lfs/](https://tylercipriani.com/blog/2025/08/15/git-lfs/)

在Git仓库中处理大型文件的持续挑战，以及探索Git LFS的替代方案。虽然Git LFS一直是事实上的解决方案，但它引入了供应商锁定、成本和复杂性。作者提倡使用Git内置的部分克隆功能作为当前的替代方案。部分克隆使用过滤器来避免在克隆期间下载大型文件，从而显著减少克隆时间和存储库大小。本文解释了如何实现部分克隆，并承认它们需要在需要时获取缺失的文件才能执行某些Git命令。

作者随后强调了未来的方向：Git大型对象承诺器。这个仍在开发中的功能，旨在将大型文件卸载到单独的远程仓库，从而解决服务器端成本问题，而不会给用户带来Git LFS的复杂性。目标是让Git主机在后台无缝管理大型文件，提高克隆速度并降低存储成本。虽然Git LFS仍然是当前处理超大型文件的解决方案，但本文总结说，Git中大型文件处理的未来在于Git本身，通过像部分克隆和对象承诺器这样的功能来实现。

---

## 10. 沃兹：我是最幸福的人

**原文标题**: Woz: 'I Am the Happiest Person'

**原文链接**: [https://daringfireball.net/linked/2025/08/15/woz-on-slashdot](https://daringfireball.net/linked/2025/08/15/woz-on-slashdot)

沃兹：我一直都是最幸福的人

这篇文章题为《沃兹：我一直都是最幸福的人》，重点讲述了史蒂夫·沃兹尼亚克的人生哲学以及他对财富的看法。起因是一个Slashdot评论批评他出售苹果股票，沃兹尼亚克回应说他更看重幸福而不是财富和权力。他捐赠了自己的苹果财富，资助了圣何塞的艺术和博物馆，并奉行“微笑减去皱眉”的原则。

文章强调，沃兹尼亚克从未“出卖”他年轻时形成的价值观。虽然他在Apple II之后停止为苹果贡献技术工作，但他的精神和个性仍然深植于公司的DNA中。 他被许多苹果员工和局外人视为英雄，体现了技术与人文艺术的交汇。

文章还引用了迈克尔·莫里茨的著作《小王国》中的一段摘录，描述了沃兹尼亚克对待财富的随意态度。他慷慨地将股票分发给家人和朋友，进行了冲动的投资，并且通常不关心财务管理。他在圣何塞购买电影院，以及随后参与社区事务和电影审查，进一步说明了他独特而平易近人的个性。文章最后强调了沃兹尼亚克对幸福的重视和他的慷慨天性。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 2 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 3 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 4 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 5 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 6 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 7 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 8 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 9 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 10 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 11 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 12 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 13 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 14 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 15 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 16 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 17 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 18 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 19 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 20 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 21 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 22 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 23 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 24 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 25 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 26 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 27 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 28 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 29 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 30 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 31 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 32 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 33 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 34 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 35 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 36 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 37 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 38 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 39 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 40 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 41 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 42 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 43 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 44 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 45 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 46 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 47 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 48 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 49 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 50 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 51 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 52 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 53 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 54 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 55 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 56 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 57 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 58 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 59 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 60 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 61 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 62 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 63 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 64 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 65 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 66 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 67 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 68 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 69 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 70 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 71 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 72 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 73 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 74 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 75 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 76 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 77 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 78 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 79 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 80 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 81 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 82 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 83 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 84 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 85 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 86 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 87 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 88 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 89 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 90 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 91 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 92 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 93 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 94 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 95 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 96 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 97 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 98 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 99 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 100 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 101 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 102 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 103 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 104 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 105 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 106 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 107 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 108 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 109 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 110 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 111 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 112 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 113 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 114 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 115 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 116 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 117 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 118 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 119 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 120 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 121 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 122 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 123 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 124 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 125 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 126 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 127 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 128 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 129 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 130 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 131 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 132 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 133 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 134 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 135 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 136 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 137 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 138 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 139 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 140 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 141 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 142 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 143 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 144 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 145 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 146 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 147 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 148 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 149 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 150 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
