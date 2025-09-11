# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-11.md)

*最后自动更新时间: 2025-09-11 17:45:26*
## 1. 螺旋

**原文标题**: Spiral

**原文链接**: [https://spiraldb.com/post/announcing-spiral](https://spiraldb.com/post/announcing-spiral)

Spiral Data 3.0 旨在解决“数据系统第三时代”的挑战，即机器消耗数据的规模已经超出为以人为中心的输入和输出而设计的传统平台的能力范围。文章认为，当前的基础设施在处理机器规模的输出时会崩溃，特别是对于像向量嵌入和图像这样的数据格式，从而导致效率低下的性价比和安全漏洞。

核心问题是第二时代工具（如数据湖和数据仓库）与第三时代需求之间的架构不匹配。Spiral 通过从头开始构建用于机器消费的系统，利用捐赠给 Linux 基金会的新的柱状文件格式 Vortex，提供了一种解决方案。Vortex 承诺比 Parquet 快得多的扫描、写入和随机访问读取速度，并且设计用于从 S3 直接解码数据到 GPU。

构建于 Vortex 之上的 Spiral 数据库是对象存储原生的，提供统一的治理、机器规模的吞吐量和“无畏的权限控制”来解决安全问题。它通过在单个系统中智能地处理从小型嵌入到大型视频文件的各种大小的数据，消除了性能和安全性之间的权衡。

凭借 2200 万美元的资金，Spiral 旨在增强 AI 工程师的能力，提高数据加载效率，并实现安全的数据共享。该公司认为，采用 AI 就绪的数据基础设施的企业将在不断发展的格局中获得显著的竞争优势。Spiral 正在积极寻找计算机视觉、机器人和多模态 AI 领域的设计合作伙伴。

---

## 2. 石墨烯操作系统与数据取证提取 (2024)

**原文标题**: GrapheneOS and Forensic Extraction of Data (2024)

**原文链接**: [https://discuss.grapheneos.org/d/13107-grapheneos-and-forensic-extraction-of-data](https://discuss.grapheneos.org/d/13107-grapheneos-and-forensic-extraction-of-data)

本文探讨了GrapheneOS，这是一款注重隐私和安全的基于安卓的操作系统，以及其抵御数字取证数据提取技术的能力，尤其是Cellebrite UFED等工具所采用的技术。它回应了近期社交媒体上对基于同意的数据提取的攻击性歪曲，这些攻击将此误解为GrapheneOS的妥协。

本文解释了数字取证及其潜在的滥用，强调了GrapheneOS为防止未经授权的数据提取所做的努力。它详细介绍了数据提取方法，区分了移动设备的BFU（首次解锁前）和AFU（首次解锁后）状态，以及它们如何影响数据可访问性。

本文分析了Cellebrite的功能，展示了其在利用非GrapheneOS安卓和一些iOS设备上的成功。关键的是，本文强调了Cellebrite在没有基于同意的访问权限的情况下，无法入侵完全更新的GrapheneOS设备，并且无法暴力破解运行GrapheneOS的Pixel 6及更高版本手机上的6位PIN码。

本文随后将此与社交媒体攻击联系起来，该攻击歪曲了Cellebrite执行基于同意的提取的能力，将其描绘成GrapheneOS的漏洞，并将此与关于Cellebrite破解Signal加密的类似虚假声明相提并论。

最后，本文详细介绍了GrapheneOS的安全对策，包括在AFU模式下锁定后禁用新的USB连接、硬件级别的USB数据禁用、固件改进，以及使用Titan M2安全芯片来防止暴力破解攻击。还讨论了强制进入BFU状态的自动重启功能。GrapheneOS的强化安全元件在防止绕过节流方面比iOS安全元件更成功。

---

## 3. Windows KASLR 绕过 – CVE-2025-53136

**原文标题**: Windows KASLR Bypass – CVE-2025-53136

**原文链接**: [https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/](https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/)

本文详细描述了一个Windows内核地址空间布局随机化 (KASLR) 绕过漏洞，CVE-2025-53136，由hieu.q发现。该漏洞通过对CVE-2024-43511的补丁分析发现，源于通过带有`SystemTokenInformation`类的`NtQuerySystemInformation()`调用`RtlSidHashInitialize()`函数时存在的竞争条件。

CVE-2024-43511的补丁无意中创建了一个小窗口，允许将内核地址，特别是`TOKEN`结构的`UserAndGroups`字段的指针，泄露到用户控制的缓冲区。这是因为`RtlSidHashInitialize()`在哈希初始化期间，会将此内核指针临时存储到用户提供的指针中。

此次泄露意义重大，因为微软此前已缓解了Windows 11/Server 2022 24H2中的其他内核信息泄露技术，使得KASLR绕过更具挑战性。CVE-2025-53136提供了一个可靠的内核地址泄露途径，可从低完整性级别 (IL) 或 AppContainer 上下文进行利用。当与写入任意地址/任意内容的原语（例如覆盖`TOKEN`对象的`Privileges`字段）结合使用时，可能会导致完整的本地权限提升 (LPE)。

该漏洞利用涉及创建两个线程：一个线程重复读取内核地址临时存储的内存位置，另一个线程重复调用`NtQuerySystemInformation()`来触发易受攻击的函数。作者成功地在2025年4月的Windows Insider Preview版本上演示了该漏洞，并从低IL和AppContainer上下文中运行。

文章最后反思了彻底的补丁分析的重要性，以及开发人员需要了解代码变更的潜在影响。还提供了与微软的披露时间表，突出显示了最初对错误报告的驳回，以及最终的承认和分配CVE。

---

## 4. 格雷格·凯洛格去世了

**原文标题**: Gregg Kellogg has passed away

**原文链接**: [https://lists.w3.org/Archives/Public/public-json-ld-wg/2025Sep/0012.html](https://lists.w3.org/Archives/Public/public-json-ld-wg/2025Sep/0012.html)

W3C的Coralie Mercier发出的邮件宣布Gregg Kellogg于2025年9月6日星期六去世。 Kellogg作为受邀专家，JSON-LD工作组的联合主席，以及多个数据相关社区组的主席，13年来一直是W3C多产且极具价值的贡献者。他非常感谢社区。

他的贡献包括共同编辑了九项已发布的推荐标准和十几个其他W3C规范，包括CSV2RDF套件、RDF 1.2套件、JSON-LD（1.0和1.1）以及RCH。他还开发了被W3C工作组使用的开源实现和测试套件。他的贡献对JSON-LD工作组的成功至关重要。

邮件强调了Kellogg的友善和善良，并指出人们会怀念他。 JSON-LD工作组正在计划一项纪念活动，希望参与贡献者请联系Pierre-Antoine Champin。 该消息已分发给W3C成员、小组主席和相关的公共邮件列表。

---

## 5. Bun 安装幕后花絮

**原文标题**: Behind the Scenes of Bun Install

**原文链接**: [https://bun.com/blog/behind-the-scenes-of-bun-install](https://bun.com/blog/behind-the-scenes-of-bun-install)

本文深入探讨了 Bun 的 `bun install` 命令比 npm、pnpm 和 yarn 快得多的原因。它认为现代包管理器受限于系统调用，这些调用涉及用户模式和内核模式之间昂贵的 CPU 模式切换。

传统的包管理器构建于 Node.js 之上，依赖 `libuv` 和线程池进行异步 I/O，这增加了文件操作的开销。这涉及到 JavaScript 参数验证、线程排队和数据编组。

Bun 使用 Zig 编写，通过进行直接系统调用绕过了这些层，消除了 JavaScript 运行时开销和线程池瓶颈。这大大减少了系统调用的数量，并消除了表明线程锁争用的高 futex 调用计数。Bun 还利用 macOS 特定的异步 DNS 解析，以避免在进行网络请求时阻塞线程。

Bun 以二进制格式缓存包清单，避免了重复的 JSON 解析和字符串复制。这种二进制缓存方法通过减少内存使用和加速字符串比较，进一步提高了性能。通过将包安装视为系统编程问题，Bun 以最小的开销实现了更快的安装时间。

---

## 6. 现实正在粉碎人形机器人的热潮

**原文标题**: Reality Is Ruining the Humanoid Robot Hype

**原文链接**: [https://spectrum.ieee.org/humanoid-robot-scaling](https://spectrum.ieee.org/humanoid-robot-scaling)

现实正在摧毁人形机器人的炒作
        
文章《现实正在摧毁人形机器人的炒作》探讨了人形机器人公司雄心勃勃的承诺与阻碍其广泛应用的实际挑战之间的差距。尽管各公司预测，像Agility的Digit、特斯拉的Optimus和Figure的机器人将在不久的将来大规模部署，但目前的市场很大程度上是假设性的，只有小规模、受控的试点项目。

扩大生产规模不如创造需求重要，因为现有的供应链可以支持制造。然而，找到每个工厂需要数千台机器人的应用是一个主要障碍。文章强调了关键的市场需求：电池续航、可靠性和安全性。目前的电池技术迫使人们在机器人设计上做出妥协，而潜在客户需要极高的可靠性（接近99.99%），以避免代价高昂的停机时间。

对于工业机械来说，安全法规已经非常严格，这带来了进一步的挑战。传统的安全措施，如切断电源，不适用于动态平衡的机器人，因此需要开发新的安全标准，并最初将部署限制在远离人群的低风险环境中。

根本问题仍然存在：双足机器人是最佳解决方案吗？虽然理论上能够导航复杂的环境，但与更可靠且成本效益更高的带臂轮式机器人相比，目前的人形机器人显示出有限的移动性。文章总结说，尽管热情高涨，但在人形机器人能够真正彻底改变劳动力市场之前，实现其潜力需要解决这些关键问题。

---

## 7. 你的每一次击键：事件监听器的技术法律测量与分析

**原文标题**: Every Keystroke You Make: A Tech-Law Measurement and Analysis of Event Listeners

**原文链接**: [https://arxiv.org/abs/2508.19825](https://arxiv.org/abs/2508.19825)

这篇 arXiv 文章《你的每一次按键：针对窃听的事件监听器的技术-法律测量与分析》调查了使用 JavaScript 事件监听器在网站上实时拦截按键的行为，及其对美国窃听法律潜在的违反。作者 Shaoor Munir、Nurullah Demir、Qian Li、Konrad Kollnig 和 Zubair Shafiq 弥合了技术测量与数十年之久的窃听法律之间的差距，他们认为此类法律可以提供私人诉权，并能为网络追踪带来有意义的改变。

该研究通过使用配备工具的网页浏览器爬取前一百万的网站，以检测拦截按键的第三方事件监听器。研究发现，38.52% 的网站安装了此类监听器，并且至少有 3.18% 的网站将拦截的数据传输到第三方服务器，符合窃听的标准。此外，证据表明，拦截的信息（例如电子邮件地址）被用于未经请求的电子邮件营销。

作者强调，虽然他们的工作识别了潜在窃听的技术方面，但还需要进一步的法律研究来确定观察到的拦截何时会超过非法门槛。该论文强调了将技术测量与法律框架联系起来，以解决网络追踪中的隐私问题的重要性。

---

## 8. 生命游戏，奏乐版

**原文标题**: Conway's Game of Life, but Musical

**原文链接**: [https://www.hudsong.dev/digital-darwin](https://www.hudsong.dev/digital-darwin)

本文通过康威生命游戏，探索了生物进化与文化趋势（尤其是在音乐方面）之间引人入胜的相似之处。作者创建了一个“旋律繁殖器”，这是一种数字工具，旋律可以在其中进化、竞争和繁殖，灵感来自理查德·道金斯的“模因”概念。该工具演示了音乐旋律如何像基因一样复制、变异并根据受欢迎程度进行选择。

然后，作者对康威生命游戏进行音乐诠释，为细胞诞生分配和谐音符，为细胞死亡分配互补音调，从而产生不断演变、不可预测的音乐，反映了游戏的模式。这突出了简单的规则如何驱动复杂的生物和音乐结构。

进一步延伸类比，本文将“Labubu”设计师玩具潮流的迅速传播比作病毒性流行病，表明相同的流行病学模型可以应用于两者。这强调了控制信息传播的模式的普遍性，无论是遗传密码、病毒颗粒还是文化观念。

作者认为，编程提供了可视化这些无形进化力量的工具，从而可以通过交互式模拟来探索复杂的想法。文章最后强调了代码将抽象概念转化为激发好奇心和理解力的有形体验的力量。

---

## 9. 美国现为商业间谍软件的最大投资国

**原文标题**: The US is now the largest investor in commercial spyware

**原文链接**: [https://arstechnica.com/security/2025/09/the-us-is-now-the-largest-investor-in-commercial-spyware/](https://arstechnica.com/security/2025/09/the-us-is-now-the-largest-investor-in-commercial-spyware/)

美国已成为全球商业间谍软件行业最大的投资者，超过了以色列和意大利等国。大西洋理事会的一份新报告指出，包括大型对冲基金和金融公司在内的31家美国投资者正在向Cognyte和Paragon Solutions等公司输送资金，其中一些公司据称与侵犯人权行为有关。

这种投资增长令人担忧，因为间谍软件行业被用于监视记者、人权捍卫者和其他人士，对人权和国家安全构成威胁。该报告强调了间谍软件市场日益增长和演变的性质，发现了新的供应商、经销商、供应商和相关个人。经销商和经纪人在掩盖行业内部联系方面发挥着关键作用，使追责变得困难。

尽管拜登政府努力通过行政命令和制裁来遏制该市场，但美国的投资仍在继续。大西洋理事会强调，美国政策与美国投资者之间存在差距，因为美国资金正在资助政府试图打击的实体。该报告还指出，公众意识有限，普通民众在不知情的情况下通过养老基金和其他投资来支持这项有争议的技术。

大西洋理事会呼吁采取进一步行动，包括针对美国的对外投资，并扩大现有行政命令的范围，将其纳入间谍软件。维持限制政府使用间谍软件的第14093号行政命令也至关重要，因为美国的购买力可以显著影响全球间谍软件市场。

---

## 10. 重塑已开源

**原文标题**: Reshaped is now open source

**原文链接**: [https://reshaped.so/blog/reshaped-oss](https://reshaped.so/blog/reshaped-oss)

Reshaped 的创建者 Dima Belyaev 宣布该组件库现已完全开源。Reshaped 最初是为了满足设计系统与 React 和 Figma 兼容的需求而构建的，它优先考虑设计与工程之间的一致性，并解决了诸如主题、暗黑模式和微动画等挑战。此前，Reshaped 采用付费许可模式，为个人提供一次性许可，为团队提供源代码许可。两年前，React 包已免费提供，现在 React 库源代码可在 GitHub 上获取，Figma 库可在 Figma Community 上获取。

Belyaev 希望此举能让设计和工程社区学习构建可扩展和极简设计系统的最佳实践。他还计划分享更多关于新功能实现的幕后见解，特别是关于与其他工具的集成。

现有许可证持有者将继续获得对更新的完全访问权限。未来的计划包括在核心库之上开发更复杂的高级组件。在经历了五年后，这次开源标志着该项目的一个重大转变，旨在回馈社区并探索新的发展途径。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 2 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 3 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 4 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 5 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 6 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 7 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 8 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 9 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 10 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 11 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 12 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 13 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 14 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 15 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 16 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 17 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 18 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 19 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 20 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 21 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 22 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 23 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 24 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 25 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 26 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 27 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 28 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 29 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 30 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 31 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 32 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 33 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 34 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 35 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 36 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 37 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 38 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 39 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 40 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 41 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 42 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 43 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 44 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 45 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 46 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 47 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 48 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 49 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 50 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 51 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 52 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 53 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 54 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 55 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 56 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 57 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 58 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 59 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 60 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 61 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 62 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 63 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 64 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 65 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 66 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 67 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 68 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 69 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 70 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 71 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 72 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 73 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 74 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 75 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 76 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 77 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 78 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 79 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 80 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 81 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 82 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 83 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 84 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 85 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 86 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 87 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 88 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 89 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 90 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 91 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 92 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 93 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 94 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 95 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 96 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 97 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 98 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 99 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 100 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 101 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 102 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 103 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 104 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 105 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 106 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 107 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 108 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 109 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 110 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 111 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 112 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 113 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 114 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 115 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 116 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 117 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 118 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 119 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 120 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 121 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 122 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 123 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 124 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 125 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 126 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 127 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 128 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 129 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 130 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 131 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 132 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 133 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 134 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 135 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 136 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 137 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 138 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 139 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 140 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 141 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 142 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 143 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 144 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 145 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 146 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 147 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 148 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 149 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 150 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 151 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 152 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 153 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 154 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 155 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 156 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 157 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 158 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 159 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 160 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 161 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 162 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 163 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 164 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 165 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 166 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 167 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 168 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 169 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 170 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 171 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 172 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 173 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 174 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 175 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 176 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
