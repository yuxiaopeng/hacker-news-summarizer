# Hacker News 热门文章摘要 (2025-09-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 曼哈顿工程的工程史

**原文标题**: An Engineering History of the Manhattan Project

**原文链接**: [https://www.construction-physics.com/p/an-engineering-history-of-the-manhattan](https://www.construction-physics.com/p/an-engineering-history-of-the-manhattan)

本文从工程角度回顾了二战期间美国开发原子弹的曼哈顿计划。虽然该计划通常与物理学和奥本海默等科学家联系在一起，但它也是一项大规模且复杂的工程项目。

本文强调了该计划早期阶段的不确定性。当时人们并不知道哪种生产裂变材料（铀235或钚）的方法最有效，炸弹应该如何设计，甚至不知道是否能造出可用的炸弹。由于战争的紧迫性，多种方法同时进行，需要前所未有的工业努力。

本文详细介绍了生产足够裂变材料所面临的挑战。铀235是一种稀有的铀同位素，必须通过电磁分离、气体扩散、液体热扩散和离心等方法从铀238中分离出来，每种方法都需要巨大而新颖的设施。另一方面，钚必须在核反应堆中合成，并且由于其放射性而需要特殊处理。

本文还提到了田纳西州的铀235生产设施橡树岭，以及用于电磁分离的复杂卡卢特管。文章强调了这项行动的巨大规模，以及它所需的创造性工程解决方案（例如使用借来的银制造电磁铁）。其驱动理念是“两者都建”，这意味着不遗余力地探索任何有希望的途径，无论成本如何。

---

## 12. 异步编程的兴起

**原文标题**: The Rise of Async Programming

**原文链接**: [https://www.braintrust.dev/blog/async-programming](https://www.braintrust.dev/blog/async-programming)

Ankur Goyal 的文章《异步编程的兴起》介绍了一种新颖的软件开发方法，即由 AI 智能体处理代码实现，使开发者能够专注于问题定义和代码审查。这种“异步编程”不同于传统定义，强调定义问题和实现问题之间的时间分离。

该工作流程包括：1) 明确定义问题并提供详细规范，2) 将实现委托给 AI 智能体、队友或有良好文档记录的未来的自己，以及 3) 审查结果并提供反馈。

Goyal 概述了异步编程的三个基本支柱：1) **清晰的问题定义：** 精确的规范会产生可用的代码，需要像详细的技术文档一样的需求。 2) **自动化验证：** 单元测试、类型检查、性能基准测试和代码检查器等系统对于独立验证至关重要。 3) **详细的代码审查：** 彻底的审查变得至关重要，即使是 AI 生成的代码，也要确保正确的问题解决、设计决策和代码质量。

异步编程允许开发人员同时处理多个任务，在同步和后台进程之间进行上下文切换。 Braintrust 正在利用这种方法，并正在开发像“Loop”这样的工具来自动化 AI 工程的各个方面，例如提示优化。

最终，异步编程将重点从打字速度和 IDE 快捷方式转移到清晰地表达问题和彻底地审查解决方案。 常规任务转移到后台，使开发人员能够专注于编程中更有价值的方面，例如设计和架构。

---

## 13. 超越包管理：Nix如何重塑我的数字生活

**原文标题**: Beyond package management: How Nix refactored my digital life

**原文链接**: [https://www.jimmyff.co.uk/blog/beyond-package-management-how-nix-refactored-my-digital-life/](https://www.jimmyff.co.uk/blog/beyond-package-management-how-nix-refactored-my-digital-life/)

本文详述了作者使用声明式包管理器Nix的历程及其对数字生活的影响。最初感到难以招架，但重新审视Nix后，发现它具有变革意义。

作者首先使用NixOS复活了一台旧Pixelbook，显著提升了其性能。受此启发，他们接着使用nix-darwin解决了MacBook上的混乱问题，实现了可复现的配置，并按模块管理软件包。跨不同架构共享配置的能力被证明非常有价值。

文中强调的一个关键优势是Nix能够使用Nix Flakes和direnv创建声明式开发环境。这使得项目特定的SDK和工具能够被轻松管理和版本控制，从而简化了开发工作流程。

一个特别引人注目的例子是，使用AI（Claude Code）解决了Pixelbook上一个长期存在的音频驱动问题，展示了Nix与AI辅助结合时的强大力量。

最后，作者表达了对未来项目的期待，包括使用Nix配置他们的Android手机，以及探索Nix用于云基础设施管理。文章以强烈推荐Nix作为结尾，强调了它能够为混乱的数字环境带来结构、可复现性和可靠性。

---

## 14. GrapheneOS 获取了 Android 安全补丁，但不允许发布源代码。

**原文标题**: GrapheneOS accessed Android security patches but not allowed to publish sources

**原文链接**: [https://grapheneos.social/@GrapheneOS/115164133992525834](https://grapheneos.social/@GrapheneOS/115164133992525834)

文章指出，正如GrapheneOS在Mastodon上发布的帖子所揭示的，GrapheneOS可以提前访问安卓安全公告。文章提到需要启用JavaScript才能使用Mastodon网页应用程序，并建议使用适合用户平台的Mastodon应用程序作为替代方案。虽然文章未明确说明，但暗示了GrapheneOS在安卓安全漏洞公开披露之前就已收到相关信息，这使其能够为用户准备补丁和更新。然而，基于对GrapheneOS的更广泛理解，他们很可能*不允许*提前公开发布这些补丁的*源代码*，即使他们可以*访问创建这些补丁所需的信息*。这种访问的意义在于，GrapheneOS可以主动解决安全问题，与没有提前访问安卓安全公告的发行版相比，它有可能为用户提供更快的安全更新。

---

## 15. 我解决了PyTorch的跨平台难题

**原文标题**: I Solved PyTorch's Cross-Platform Nightmare

**原文链接**: [https://svana.name/2025/09/how-i-solved-pytorchs-cross-platform-nightmare/](https://svana.name/2025/09/how-i-solved-pytorchs-cross-platform-nightmare/)

无法访问文章链接。

---

## 16. 感知映射到PICO-8调色板

**原文标题**: Mapping to the PICO-8 palette, perceptually

**原文链接**: [https://30fps.net/pages/perceptual-pico8-pixel-mapping/](https://30fps.net/pages/perceptual-pico8-pixel-mapping/)

本文探讨了不同的色彩空间和距离度量方法，用于将图像像素映射到有限的调色板，特别是PICO-8的16色调色板，采用基于距离的方法。作者比较了sRGB（有和没有亮度加权）、CAM16-UCS（具有不同的观察条件）、Oklab和CIELAB（具有加权HyAB距离）在像素映射后感知视觉质量方面的表现。

最简单的在sRGB空间中使用欧几里得距离的方法产生了不令人满意的结果。 通过亮度贡献对RGB通道进行加权可以改善结果。 CAM16-UCS是一种感知色彩空间，旨在使欧几里得距离与感知的颜色差异对齐，但其性能并未始终优于Oklab或加权CIELAB。 作者发现CAM16-UCS会根据观察条件假设产生不同的结果，但并未提供显着质量提升。

最终，作者得出结论，当忽略空间图像结构时，没有一种色彩空间能够提供完美的解决方案。 这个问题定义不明确。 即使是创建灰度效果的极端亮度加权也会被Helmholtz-Kohlrausch效应破坏。 本文包括实验中使用的各种距离函数和色彩空间转换的代码片段，并链接到进一步的结果以供比较。 作者认为，要获得可接受的质量，需要查看实际图像，而不仅仅是其颜色。

---

## 17. Piramidal (YC W24) 招聘后端工程师

**原文标题**: Piramidal (YC W24) Is Hiring Back End Engineer

**原文链接**: [https://www.ycombinator.com/companies/piramidal/jobs/1HvdaXs-full-stack-engineer-platform](https://www.ycombinator.com/companies/piramidal/jobs/1HvdaXs-full-stack-engineer-platform)

Piramidal (YC W24) 招募全栈工程师 - 平台，助力其最新技术交互和自动化。该公司是一家初创企业，致力于构建电生理脑数据的基础模型，旨在创建可扩展的神经解码器，使人类能够理解和控制神经语法，专注于认知自由和最大化人类潜力。

该职位涉及构建和维护 Piramidal 旗舰平台（专注于神经数据）的基础设施和后端系统，与机器学习工程师协作，并与产品团队合作实施有效解决方案。

理想的候选人应具有 3 年以上工程经验，精通 Python 和其他后端语言、容器化 (Kubernetes)、关系数据库 (Postgres/MySQL) 和 Web 技术 (JavaScript, React)。 公司重视积极主动、以客户为中心的工程师，他们优先考虑数据模型、架构和安全性。

薪酬范围为 12 万美元至 21 万美元，股权为 0.10% 至 0.50%。 工作地点为纽约州纽约市、加利福尼亚州旧金山市或远程（加利福尼亚州旧金山市；伊利诺伊州芝加哥市；德克萨斯州奥斯汀市）。

面试流程包括初步筛选、技术筛选（实时编码和系统设计）和产品筛选（战略、优先级和用户需求）。

Piramidal 成立于 2024 年，是 Y Combinator W24 批次的一部分，团队规模为 10 人，并且正在积极发展。

---

## 18. DeepCodeBench: 基于问答基准测试的真实世界代码库理解

**原文标题**: DeepCodeBench: Real-World Codebase Understanding by Q&A Benchmarking

**原文链接**: [https://www.qodo.ai/blog/deepcodebench-real-world-codebase-understanding-by-qa-benchmarking/](https://www.qodo.ai/blog/deepcodebench-real-world-codebase-understanding-by-qa-benchmarking/)

DeepCodeBench是由Qodo发布的一个新基准数据集，旨在评估人工智能通过问答理解真实世界代码库的能力。其动机源于开发者在浏览大型代码库时面临的困难，即使有AI辅助也是如此。与现有基准不同，DeepCodeBench专注于源自pull requests（PRs）的真实问题，这些问题需要跨多个互连文件进行检索，从而反映常见的开发者工作流程。

数据集的生成利用PRs作为功能相关代码的指标。通过从PR的代码更改中检索相关的代码片段（方法、类或文件），以及PR的标题和描述来创建上下文。然后提示大型语言模型（LLMs）基于此上下文生成真实的、以开发者为中心的问题和相应的答案。

该数据集包含来自八个开源存储库的1,144个问题，按范围（深/广）以及它们是否针对核心功能或包含可搜索的关键词进行分类。评估使用“事实召回”，从真实答案中提取可验证的事实，并检查它们是否存在于预测答案中。

基线评估包括具有完整上下文、没有上下文以及真实答案的LLMs，以建立性能基准。结果表明，Qodo的Deep Research agent实现了最佳的事实召回率（76%），略微领先于OpenAI的Codex（74%），并显著优于Claude和Gemini。数据集、元数据、提示和评估方法已公开发布，以鼓励在代码理解和AI辅助开发方面的进一步研究和发展。

---

## 19. PgEdge 开源

**原文标题**: PgEdge Goes Open Source

**原文链接**: [https://www.pgedge.com/blog/pgedge-goes-open-source](https://www.pgedge.com/blog/pgedge-goes-open-source)

pgEdge 全面开源：采用 PostgreSQL 许可证

本博文宣布 pgEdge 现已完全开源，从“源码可用”模式过渡到宽松的 PostgreSQL 许可证。 pgEdge 工程副总裁 Dave Page 对此变化表示欣喜，并强调 pgEdge 分布式 Postgres 的核心组件，包括 Spock 复制引擎以及 Snowflake 和 Lolor 等扩展，现在都可以根据新许可证自由使用和修改。

Page 解释说，之前的 pgEdge 社区许可证限制了源代码的使用方式，而 PostgreSQL 许可证提供了更大的自由度。 他强调 pgEdge 致力于支持开源软件并为 PostgreSQL 生态系统做出贡献。

该博文鼓励开发人员在 GitHub 上探索新开源的代码，特别提到了 spock、snowflake 和 lolor 仓库。 它还为喜欢受支持且易于部署的生产环境解决方案的用户提供了预构建的云、容器和 VM 选项。

作者 Dave Page 是 PostgreSQL 社区的长期贡献者，拥有超过 25 年的经验，进一步巩固了 pgEdge 对开源和 PostgreSQL 生态系统的承诺。 最后，文章邀请读者订阅 pgEdge 博客并尝试其非分布式和分布式 Postgres 部署产品。

---

## 20. KDE发布其自有发行版

**原文标题**: KDE launches its own distribution

**原文链接**: [https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/](https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/)

这篇2025年9月10日LWN.net的文章报道了KDE Linux的alpha版本发布，这是一个由KDE项目创建的新发行版。它旨在提供完整的KDE体验，目标是家庭、商业和OEM使用，但目前仍处于早期开发阶段。

KDE Linux 使用 Arch Linux 软件包作为其基础，但不被认为是基于 Arch 的发行版。 它的特点在于使用 KDE Builder 从源代码编译软件或使用 Flatpak。 KDE 创建自己的发行版的一个主要动机是直接控制软件分发，类似于他们对 Flathub 和其他应用商店的做法。KDE Linux 旨在取代 KDE neon，后者正受困于老化的 Ubuntu 基础。

该发行版仅支持 Wayland，支持 UEFI 系统，并具有可读/写 Btrfs 根文件系统和用于原子更新的只读 EROFS /usr 卷。它不提供向基础系统添加软件包的方法，而是依赖 Flatpak 和 Distrobox 进行应用程序管理。

未来的计划包括测试版、爱好者版和稳定版，分别针对开发者、高级用户和普通用户。 该文章强调了由于依赖 Arch 软件包以及缺乏用于系统库存的传统软件包管理器而可能导致的安全更新问题。 该项目采用“长老会”治理模式，Harald Sitter 拥有最终决策权。 存在生命周期结束应急计划，涉及将用户过渡到另一个发行版。 作者总结说，无论 KDE Linux 最终是否成功，它都是了解创建和维护 Linux 发行版所面临挑战的有用尝试。

---

## 21. C++20模块：实践洞见、现状与待办事项

**原文标题**: C++20 Modules: Practical Insights, Status and TODOs

**原文链接**: [https://chuanqixu9.github.io/c++/2025/08/14/C++20-Modules.en.html](https://chuanqixu9.github.io/c++/2025/08/14/C++20-Modules.en.html)

本文深入探讨了使用C++20模块的实用见解，包括其当前状态、优势、成本和未来考量。截至2025年末，尽管2019年已完成标准化，但采用率仍然有限。

**优势：** 模块提高了代码的模块化、封装性和编译速度（观察到25-45%的提升）。它们还通过避免冗余代码生成来减少对象、静态和动态库的大小（在.so文件中观察到12%的减少）。

**成本：** 重构现有代码是最大的障碍。一旦项目使用模块，下游依赖项通常也必须使用。编译器崩溃以及编译器/平台之间行为不一致也带来了挑战。

**何时使用：** 适用于使用最新编译器和语言标准的新项目或大部分是新项目，且没有严格的跨编译器/平台兼容性要求。

**模块封装器：** 项目可以通过"export-using"或"extern C++"封装器提供可选的模块，允许下游用户选择。"extern C++"样式通常提供更好的编译时性能。建议对模块单元使用`.cppm`等后缀。

**编译时间缩短：** 模块充当前端的缓存（模板展开、编译时计算），并通过创建预解析的文件来防止重复解析头文件，从而提高整体编译速度。

**待办事项：** 本文隐式地呼吁更好的构建系统支持、更强大的编译器实现以及库开发人员更多地采用模块。

---

## 22. 展示 HN: Term.everything – 在终端中运行任何 GUI 应用

**原文标题**: Show HN: Term.everything – Run any GUI app in the terminal

**原文链接**: [https://github.com/mmulet/term.everything](https://github.com/mmulet/term.everything)

Term.everything❗ 是一个 Linux 命令行程序，它允许你在终端内直接运行 GUI 应用程序，即使是通过 SSH。 它通过充当 Wayland 合成器来实现这一点，该合成器将输出发送到终端而不是标准显示器。GUI 渲染质量取决于终端的分辨率，但可以通过支持图像的终端（如 Kitty 或 iTerm2）来提高。

该项目目前处于 beta 阶段，其路线图从“Term some things”（目前的状态，可能出现崩溃和启动失败）发展到“Term most things”，最终到“Term everything❗”。 该项目鼓励用户报告问题并欢迎贡献。

该程序是用 Typescript（使用 Bun 引擎）和一些 C++ 编写的。 作者反对开发更多的终端文件查看器，因为用户现在可以在终端内利用现有的 GUI 文件查看器。 该文章还包括在终端内运行 Firefox 甚至 Doom 等应用程序的示例。

该项目是开源的，包含贡献指南、澄清版权的法律部分以及示例中使用的资产的署名。 一份名为 HowIDidIt.md 的文档详细解释了其内部运作原理。 这篇文章还介绍了 Gwerm the Term Worm，它现在状况良好。

---

## 23. 哈希排序通常比哈希表更快

**原文标题**: Hashed sorting is typically faster than hash tables

**原文链接**: [https://reiner.org/hashed-sorting](https://reiner.org/hashed-sorting)

本文认为，对于大型数组中唯一值的计数，尽管哈希表具有更好的理论时间复杂度（O(n) vs. O(n log n)），哈希基数排序通常比哈希表更快。作者通过在M2 Pro上的基准测试证明了这一点，结果表明，经过优化的基数排序实现比哈希表（包括Rust的“Swiss Table”）速度提高了1.5倍至4倍。

这种性能差异的关键原因是**内存带宽**。哈希表通过为每个8字节键访问获取整个缓存行（64字节）来浪费带宽，导致每个键至少128字节的流量。基数排序，特别是使用分流最低有效位优先排序（LSD sort），更有效地利用了缓存行，由于其空间局部性，每个键仅需要大约48字节的内存流量。

为了处理非均匀分布的数据，作者提倡在使用排序之前使用**可逆哈希函数**（如Murmur3或MulSwapMul）来预处理键。

虽然在许多情况下基数排序更快，但当每个唯一键的访问次数很高（大约30次或更多）或批量操作不可行时，**哈希表可能更可取**。基数排序需要批量处理。本文还讨论了基数排序和哈希表的优化，包括分流排序、单表哈希表、缓存行对齐探测、较低的负载因子和预取。

---

## 24. 末日刷屏：游戏

**原文标题**: DOOMscrolling: The Game

**原文链接**: [https://ironicsans.ghost.io/doomscrolling-the-game/](https://ironicsans.ghost.io/doomscrolling-the-game/)

大卫制作了一款名为“末日滚动：游戏”的网页浏览器游戏，灵感来自《毁灭战士》，唯一的玩法机制就是滚动。玩家通过滚动在类似《毁灭战士》的环境中移动，遭遇怪物和障碍。

他最初尝试使用LLM创建游戏失败了，但在GPT-5发布后，他能够在两个小时内完成原型。随后，他添加了武器升级、追逐火焰墙、障碍物、血瓶以及不同的背景纹理等功能。

为了将游戏与“末日滚动”概念联系起来，他将《纽约时报》RSS订阅的头条新闻整合为游戏环境中的“牌匾”，代表“巢穴”被封锁之日的新闻。这些牌匾起到了分散注意力的作用，反映了现实中沉迷末日滚动的诱惑。

他借助ChatGPT，使用带有交互元素（如滑块）的“实验室”来微调游戏内元素和怪物的外观，从而简化了美术创作流程。尽管他尝试过预渲染怪物，但他最终更喜欢计算生成的怪物设计，因为它们的外观更好。

大卫即将发布1.0版本的游戏，可在移动设备和桌面设备上运行，并邀请读者试玩。他鼓励读者通过订阅或捐款以及分享时事通讯来支持他的工作。

---

## 25. ChatGPT开发者模式：完整MCP客户端访问

**原文标题**: ChatGPT Developer Mode: Full MCP client access

**原文链接**: [https://platform.openai.com/docs/guides/developer-mode](https://platform.openai.com/docs/guides/developer-mode)

无法访问文章链接。

---

## 26. tz 数据库工作原理 (2020)

**原文标题**: How the tz database works (2020)

**原文链接**: [https://yatsushi.com/blog/tz-database/](https://yatsushi.com/blog/tz-database/)

文章《tz数据库的工作原理 (2020)》解释了tz（时区）数据库（也称为IANA时区数据库）的结构和功能。它强调了该数据库在为全球计算机系统和应用程序提供准确的历史和未来时区信息方面发挥的关键作用。

作者解释说，tz数据库由文本文件组成，每个文件代表一个地理区域或“时区”。这些文件包含指定本地时间何时以及如何更改的规则，主要原因是夏令时 (DST) 或其他历史异常。这些规则使用特定的、人类可读的格式定义，由诸如`Rule`、`Zone`和`Link`之类的关键字描述。

`Rule`记录定义了何时以及如何发生DST转换，包括开始和结束日期、时间以及与标准时间的偏移量。`Zone`记录指定适用于特定地理区域的规则以及与UTC的标准偏移量。`Link`记录为共享相同时区历史的时区提供别名。

文章强调了数据库的持续更新过程。世界各地的专家贡献时区信息，IANA（互联网号码分配机构）管理和分发这些更新。这些更新至关重要，因为时区规则可能会被政府更改，而且通常几乎没有通知。

最后，作者描述了软件如何使用tz数据库。程序通常将数据库加载到内存中，并使用它在UTC和本地时间之间进行转换，同时考虑到历史和未来的时区规则。文章强调了保持tz数据库更新的重要性，以确保准确的时间计算。

---

## 27. CRISPR为糖尿病治疗带来新希望

**原文标题**: CRISPR Offers New Hope for Treating Diabetes

**原文链接**: [https://www.wired.com/story/no-more-injections-crispr-offers-new-hope-for-treating-diabetes/](https://www.wired.com/story/no-more-injections-crispr-offers-new-hope-for-treating-diabetes/)

这篇《连线》杂志的文章讨论了CRISPR基因编辑技术在治疗1型糖尿病方面一项很有前景的新应用。研究人员成功地将CRISPR编辑过的胰腺细胞植入了一位患有1型糖尿病的人体患者体内。这些经过编辑的细胞，来源于已故捐赠者，并经过修饰以逃避免疫系统（“低免疫”），在不需要免疫抑制药物的情况下，产生了数月的胰岛素。这项发表在《新英格兰医学杂志》上的研究详细介绍了如何使用Crispr-Cas12b编辑细胞，并将细胞植入患者的前臂肌肉中。12周后，没有检测到排斥迹象，并且植入的细胞明显分泌胰岛素以响应葡萄糖水平。

最终目标是将这些编辑应用于干细胞，使其能够分化成分泌胰岛素的胰岛细胞，同时对免疫系统保持隐形。这种方法旨在消除对免疫抑制的需求，而免疫抑制是传统细胞移植中的一个主要障碍。

虽然这项研究代表着一个重要的里程碑，但需要注意的是，它只涉及一名接受低剂量细胞的参与者。这不足以消除对胰岛素注射的需求。此外，一些独立的研究小组一直在努力复制免疫逃避的结果。该疗法的幕后公司Sana Biotechnology计划进行更多的临床试验。尽管存在局限性，但该研究为再生医学提供了一条有希望的新途径，并有可能治愈糖尿病。

---

## 28. 最终一致性：CRDT背后的核心思想

**原文标题**: Strong Eventual Consistency – The Big Idea Behind CRDTs

**原文链接**: [https://lewiscampbell.tech/blog/250908.html](https://lewiscampbell.tech/blog/250908.html)

本文介绍了强最终一致性（SEC）及其与无冲突复制数据类型（CRDT）的联系。文章认为，CRDTs通过SEC赋能协同编辑等功能，有潜力彻底改变分布式数据库。

其核心思想是，作为最终一致性的增强形式，强最终一致性（SEC）保证副本在处理相同更新后立即达到状态一致。这通过“强收敛”实现，确保在节点独立更新时自动且确定性地解决冲突。

这具有显著优势：低延迟（无需协调）、高容错性（系统在节点大范围故障时也能正常运行）以及离线或网络分裂期间的适当功能。作者认为，SEC使最终一致性真正适用于本地优先和地理复制系统。

本文提倡将CRDTs不仅视为管理应用程序状态的工具，而且视为创建整个强最终一致性数据库的基本构建块。CRDTs使数据库在具有挑战性的分布式环境中具有高可用性、可扩展性和弹性。

---

## 29. 蓝精灵的帽子从哪儿来的 (2018)

**原文标题**: Where did the Smurfs get their hats (2018)

**原文链接**: [https://www.pipelinecomics.com/beginning-bd-smurfs-hats-origin/](https://www.pipelinecomics.com/beginning-bd-smurfs-hats-origin/)

本文探讨了蓝精灵标志性白色帽子的起源。首先，文章以贝约的漫画为权威来源，探讨了蓝精灵帽子下面可能是什么，并根据一幅老爹的帽子被风吹掉的画面得出结论：老爹是秃顶。

随后，文章深入探讨了蓝精灵帽子的历史，指出它是一种弗里吉亚帽，一种可以追溯到2000多年前的头饰，阿提斯和迈达斯国王等人物都曾佩戴过。弗里吉亚人是来自巴尔干半岛的古代民族。

文章还讨论了帽子与自由的联系，追溯了它在法国大革命期间被采用为“自由的红色帽子”的历史。然而，文章指出，革命者错误地采用了弗里吉亚帽，因为他们本想使用皮列乌斯帽，这是一种古罗马解放奴隶佩戴的无边毡帽或羊毛帽，作为他们自由的象征。

作者认为，与法国出版商合作的比利时艺术家贝约在创作蓝精灵帽子时，很可能从法国的这一象征符号中汲取了灵感。文章总结说，蓝精灵的帽子，虽然在历史上与自由有关，但很可能是因为其视觉吸引力和独特性而被选中的。

---

## 30. 法院驳回 Verizon 未经同意出售位置数据是合法的说法

**原文标题**: Court rejects Verizon claim that selling location data without consent is legal

**原文链接**: [https://arstechnica.com/tech-policy/2025/09/court-rejects-verizon-claim-that-selling-location-data-without-consent-is-legal/](https://arstechnica.com/tech-policy/2025/09/court-rejects-verizon-claim-that-selling-location-data-without-consent-is-legal/)

威瑞森因未经同意出售客户位置数据被罚款4690万美元的上诉被驳回。美国第二巡回上诉法院驳回了威瑞森关于联邦通信委员会（FCC）的处罚侵犯其权利的论点。这一裁决与针对T-Mobile的类似裁决一致，但与另一家法院支持AT&T的裁决相悖，增加了最高法院介入的可能性。

联邦通信委员会在2018年披露威瑞森、AT&T和T-Mobile向数据聚合商出售客户位置数据，后者又将其转售给包括Securus Technologies在内的第三方后，对这些公司处以罚款。Securus Technologies允许执法部门在没有适当搜查令的情况下访问数据。威瑞森辩称，《通信法》的隐私保护仅涵盖通话位置数据，不包括设备位置数据，这一说法被法院驳回。

法院还驳回了威瑞森关于罚款侵犯其第七修正案规定的接受陪审团审判权利的主张，指出威瑞森可以选择拒绝付款并在联邦法院寻求陪审团审判。第二巡回法院将此案与最高法院的Jarkesy案区分开来，称电信法允许选择陪审团审判，而证券法不允许。尽管联邦通信委员会主席此前反对这项罚款，但他还是支持该机构在法庭上的辩护。

---

## 31. 德国不支持聊天监控——少数派阻止成功

**原文标题**: Germany is not supporting ChatControl – blocking minority secured

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/115184350819592476](https://digitalcourage.social/@echo_pbreyer/115184350819592476)

基于帕特里克·布雷耶在Mastodon上的帖子，这篇文章庆祝德国明显不支持欧盟提议的“聊天控制”立法。该帖子托管在Mastodon实例digitalcourage.social上。关键信息是德国阻止了少数派，从而阻止了聊天控制法以目前的形式通过。

重要的是要注意，“聊天控制”可能指的是旨在监管在线内容的欧盟提案，可能涉及扫描私人通信以检测非法内容，例如儿童性虐待材料。这些提案遭到了隐私倡导者的强烈反对，他们认为这可能导致大规模监控并破坏加密。布雷耶作为欧洲议会议员，以倡导数字权利和隐私而闻名，他可能是在表达对德国不支持这项立法的赞赏，这表明隐私担忧取得了胜利。

---

## 32. 布鲁塞尔面临加密后门隐私困境

**原文标题**: Brussels faces privacy crossroads over encryption backdoors

**原文链接**: [https://www.theregister.com/2025/09/11/eu_chat_control/](https://www.theregister.com/2025/09/11/eu_chat_control/)

欧盟正面临一项关于隐私和安全的关键抉择，各成员国正在辩论一项旨在打击儿童性虐待材料（CSAM）的名为“聊天控制”的立法。该立法提议要求互联网服务提供商和消息应用程序扫描用户内容或为情报机构提供加密后门。批评者认为这是对私人通信前所未有的侵犯。

这项拟议立法面临强烈反对，超过600名安全专家签署了一封公开信，谴责其不可行且具有侵入性。他们强调了高误报率，这可能导致错误的指控。安全专家警告说，实施加密后门会造成“国家安全灾难”，因为敌对国家可能会利用它们。

该立法对检测“新”形式CSAM的模糊要求，以及将政府和军事通信排除在外，引发了进一步的担忧。批评者指出，通过人工智能可靠地检测新的CSAM在技术上是不可行的，估计客户端扫描的潜在误报率高达10%。

像Signal和Tuta这样的加密应用程序提供商表示强烈反对，Tuta威胁说，如果该立法通过，将搬迁到欧盟以外。他们认为该提案侵犯了欧盟的隐私权。虽然英国的类似立法已被证明是不可行的，但包括德国在内的一些欧盟成员国据报道正在重新考虑其支持。预计下个月将进行最终投票。

---

## 33. 人工智能对齐中心联盟中心

**原文标题**: Center for the Alignment of AI Alignment Centers

**原文链接**: [https://alignmentalignment.ai](https://alignmentalignment.ai)

这段简短的节选文章揭示了人工智能对齐研究领域中一个令人担忧的问题：一种“对齐错位危机”。文章认为，旨在确保人工智能系统与人类价值观和目标对齐的人工智能对齐领域正迅速发展，但其本身也正变得支离破碎。各项研究工作彼此之间并不对齐，可能导致灾难性后果。

核心问题是人工智能对齐研究的“无节制扩散”，而讽刺的是，这些研究本身就存在错位现象。这表明不同的研究人员和机构正在追求不同的人工智能对齐方法，甚至可能是相互矛盾的方法。文章警告说，缺乏统一的方法可能会导致负面结果，这意味着如果对齐研究本身是分裂和不协调的，那么它可能无法有效地应对确保人工智能有益的挑战。

---

## 34. Nano11将Windows 11瘦身，仅占用2.8GB磁盘空间

**原文标题**: Nano11 cuts Windows 11 down to size, grabbing just 2.8 GB of disk space

**原文链接**: [https://www.theregister.com/2025/09/11/nano11_cuts_windows_11_down/](https://www.theregister.com/2025/09/11/nano11_cuts_windows_11_down/)

理查德·斯皮德的文章讨论了Nano11，这是NTDEV创建的Windows 11的精简版，安装后仅占用2.8GB的磁盘空间，安装媒介仅为2.2GB。 这是通过删除众多组件实现的，包括Windows Update、系统服务和Windows Defender，甚至比NTDEV之前的“Tiny11”项目更进一步，后者移除了Copilot、Outlook和Teams等元素。

这篇文章强调，Nano11由于其严重受限的功能和缺乏更新支持，不适合日常使用；一旦移除，功能和语言都无法添加回来。 它主要设计用于虚拟机中的测试、开发或嵌入式系统，在这些系统中需要最小且静态的操作系统环境。 Nano11脚本基于Tiny11 Core的工作，使用LZX压缩，这个过程可能需要大量的RAM且耗时。

文章还强调了更广泛的含义，即标准Windows 11中的膨胀是微软有意识的选择，而像Nano11这样的项目表明了大幅缩小占用空间的潜力。 虽然不适用于日常使用，但Nano11令人印象深刻地展示了Windows 11的最低运行要求，并且是VM环境中专门用例的潜在解决方案。

---

## 35. 根据一份新报告，2025年全球最幸福国家

**原文标题**: Happiest Countries in the World for 2025, According to a New Report

**原文链接**: [https://www.forbes.com/sites/laurabegleybloom/2025/03/20/the-20-happiest-countries-in-the-world-for-2025-according-to-a-new-report/](https://www.forbes.com/sites/laurabegleybloom/2025/03/20/the-20-happiest-countries-in-the-world-for-2025-according-to-a-new-report/)

2025年世界幸福报告：芬兰连续八年蝉联榜首，美国跌至历史最低

---

## 36. 黑莓派CM5掌上电脑

**原文标题**: The HackberryPi CM5 handheld computer

**原文链接**: [https://github.com/ZitaoTech/HackberryPiCM5](https://github.com/ZitaoTech/HackberryPiCM5)

HackberryPi_CM5是由机械工程和工业设计专业的学生Zitao设计的，一款由树莓派Compute Module 5驱动的掌上电脑。它使用回收的黑莓键盘，旨在为用户提供一款便携的、基于Linux的设备，用于探索硬件、软件和Linux内核。

该设备配备4英寸720x720触摸屏显示器、四核Cortex-A76 CPU、2个USB 3.0端口、HDMI端口和一个5000mAh LiPo电池，可提供3-5小时的使用时间。它还包括一个用于SSD或AI加速卡的2242 NVMe插槽、RTC电池、通过蓝牙连接的双扬声器以及一个用于外部传感器的Stemma I2C端口。外壳由铝制前后面板和3D打印的中间部分组成。

用户可以通过VIAL自定义键盘布局。该设备还具有内置磁铁，可与iPhone式MagSafe充电宝兼容。该存储库提供用于打印或修改的3D模型、组装指南、硬件概述、扬声器配对说明和外部天线组装指南。HackberryPi_CM5不包含CM5单元，可在Elecrow购买。

---

## 37. 无图形界面的桌面环境 (类似 tmux)

**原文标题**: A desktop environment without graphics (tmux-like)

**原文链接**: [https://github.com/Julien-cpsn/desktop-tui](https://github.com/Julien-cpsn/desktop-tui)

Desktop-TUI 是一个基于文本的桌面环境，类似于 tmux，无需图形界面即可运行。它允许用户在终端界面中管理应用程序和命令。主要特性包括：

*   **快捷键解析：** 它可以解析定义应用程序、命令及其参数的快捷键文件（如 `helix.toml`）。
*   **应用显示：** 它可以在可调整大小和移动的窗口中显示任何使用 stdout 的应用程序或命令的输出。
*   **窗口管理：** 用户可以移动、调整大小和并排排列窗口。
*   **文件/文件夹选择：** 它提供了一种选择文件或文件夹的机制，允许它们用作应用程序或命令的参数。
*   **错误处理：** 它可以处理应用程序错误和 GNU 应用程序/命令崩溃。
*   **配置：** 快捷键文件定义了应用程序名称、命令、参数（带有文件/文件夹选择的占位符）、填充和操作栏上的位置。

由于 Crossterm 存在问题，该项目目前使用 ncurses 后端，但计划在这些问题解决后进行切换。使用当前后端颜色可能不正确。

安装和使用涉及使用 `cargo install desktop-tui`、构建项目以及运行 `desktop-tui` 可执行文件，并将快捷键文件夹的路径作为参数。 该项目采用 MIT 许可证。

---

## 38. Jiratui – 从命令行与 Atlassian Jira 交互的文本用户界面

**原文标题**: Jiratui – A Textual UI for interacting with Atlassian Jira from your shell

**原文链接**: [https://jiratui.sh/](https://jiratui.sh/)

JiraTUI 是一个命令行界面，旨在简化与 Atlassian Jira 的交互，使开发人员能够直接从终端管理任务。该工具旨在通过提供创建、更新和搜索 Jira 任务等功能来提高生产力，而无需离开命令行。

主要功能包括：

*   **搜索任务：** 按状态、负责人或优先级快速筛选任务。
*   **创建任务：** 轻松创建包含标题、描述和优先级的新任务。
*   **更新任务：** 修改任务详细信息，如状态、负责人、摘要、标签和截止日期。
*   **评论：** 添加或删除评论以促进团队沟通。
*   **管理相关任务：** 链接和取消链接任务以可视化依赖关系。
*   **JQL 搜索：** 利用 Jira 查询语言进行高级、自定义的任务筛选。

使用 JiraTUI 的优势包括其可配置性、简单性、速度和易用性。它允许用户根据其特定需求定制工具，提供直观的命令行界面，实现快速任务管理，并且适合所有技能水平的开发人员使用。 通过消除不必要的导航和点击，JiraTUI 帮助开发人员专注于他们的代码和整体工作流程，从而提高效率和生产力。

---

## 39. 击败LLM推理中的不确定性

**原文标题**: Defeating Nondeterminism in LLM Inference

**原文链接**: [https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

本文探讨了尽管设置了确定性参数（如温度=0），大型语言模型 (LLM) 推理仍出现不确定性结果的问题。它挑战了常见的“并发 + 浮点数”假设，认为虽然浮点数非结合性会导致数值差异，但并不能完全解释 LLM 中不确定性的来源。

文章解释说，虽然 LLM 前向传递中使用的单个 GPU 内核通常是确定性的，但从用户的角度来看，整个 LLM 推理服务器表现出不确定性行为。这是因为用户请求的输出可能取决于其他并行用户请求，原因是缺乏“批次不变性”。

“批次不变性”意味着批次中特定元素的计算结果应独立于批次中的其他元素和整个批次大小。然而，例如，matmul 运算并不总是具有批次不变性，这意味着改变批次大小可能会改变结果。

这种缺乏批次不变性，加上推理服务器上波动的负载（这会影响批次大小），引入了不确定性。用户的请求输出取决于服务器负载，这从用户的角度来看是随机的。因此，即使使用确定性内核，整个系统也会变得不确定，从而解释了为什么重复查询会产生不同的结果。文章建议，修复批次不变性是实现 LLM 推理中真正可重复结果的关键一步。

---

## 40. “小费免税”也包括数字内容创作者

**原文标题**: “No Tax on Tips” Includes Digital Creators, Too

**原文链接**: [https://www.hollywoodreporter.com/business/business-news/no-tax-on-tips-guidance-creators-trump-treasury-1236366513/](https://www.hollywoodreporter.com/business/business-news/no-tax-on-tips-guidance-creators-trump-treasury-1236366513/)

特朗普总统的“一项重大美丽法案”可能通过将“数字内容创作者”纳入“小费免税”政策，从而显著影响创作者经济。美国财政部现在认为播客主、社交媒体影响者和流媒体主播有资格享受这项福利，与传统的有小费职业（如调酒师和服务员）并列。

这项政策允许符合条件的纳税人扣除其小费收入，从而可能改变数字创作者寻求收入的方式。TikTok、YouTube 和 Twitch 等平台提供收入分成、订阅和直接打赏。这项税收优惠可能会激励创作者优先考虑用户打赏和礼物，而不是其他收入模式（如定期订阅）。

虽然扣除额上限为每年 25,000 美元，并在较高收入水平（单身申报者为 150,000 美元，已婚联合申报者为 300,000 美元）时逐步取消，并且不包括在特定领域（如健康、表演艺术和体育）赚取的小费，但它仍然为创作者提供了征求小费的激励。这可能会导致平台强调打赏功能，并鼓励创作者融入更多基于小费收入的机会。

这项政策将数字创作者纳入其中，认可了他们日益增长的力量和影响力，尤其是在政治领域，并可能鼓励更多人进入创作者领域。文章表明，这种转变可能会通过税收效率重塑创作者经济，促使用户“点赞、订阅和打赏”。

---

## 41. 为MicroHaskell重写数据帧

**原文标题**: Rewriting Dataframes for MicroHaskell

**原文链接**: [https://mchav.github.io/rewriting-dataframes-for-microhs/](https://mchav.github.io/rewriting-dataframes-for-microhs/)

本文探讨了创建一个跨 Haskell 数据帧库的挑战，目标是超越主流的 GHC 编译器，并实现与 MicroHs 等小型 Haskell 实现的兼容性。作者回顾了过去使用替代 Haskell（Frege、GHCJS、Eta）的经验，以及对更广泛、更通用兼容的 Haskell 生态系统的渴望。

文章随后深入探讨了一个简化的、基于基本 Haskell 的数据帧实现，避免了诸如类型族和 GADTs（除了 FlexibleInstances 扩展）等高级 GHC 功能。数据帧被定义为标记列的集合，为了简单起见，每列仅限于 Int、String 或 Double 数据类型。使用类型类 `toColumn` 提供了数据帧和列的构造函数，以实现类型特定的调度。

最复杂的部分涉及在数据帧中定义和解释表达式。在没有 GADTs 的情况下，本文概述了一个冗长的 `Expr` 数据类型，其中包含针对 Int、String 和 Double 类型宇宙中每个受支持的二元和一元运算的显式构造函数。`interpret` 函数处理针对给定数据帧评估这些表达式，并返回结果列。还提供了一个 `DataFrame.PrettyPrint` 模块，用于以 markdown 表格格式显示数据帧。

---

## 42. 英特尔E2200“摩根山”IPU亮相2025热芯片大会

**原文标题**: Intel's E2200 "Mount Morgan" IPU at Hot Chips 2025

**原文链接**: [https://chipsandcheese.com/p/intels-e2200-mount-morgan-ipu-at](https://chipsandcheese.com/p/intels-e2200-mount-morgan-ipu-at)

英特尔“摩根山”IPU，亮相Hot Chips 2025，旨在卸载云环境中服务器CPU的基础设施服务，提供更高的隔离性，并释放核心用于客户工作负载。作为“埃文斯山”的升级版，“摩根山”强调灵活性，既能作为强大的网卡，也能作为独立服务器运行。

主要升级包括更强大的计算复合体，配备24个Arm Neoverse N2内核（由16个N1内核升级而来），四通道LPDDR5-6400内存以及32 MB系统级缓存。Lookaside加密和压缩引擎（LCE）提供非对称加密支持，解决了之前的局限性。

网络子系统具有400 Gbps以太网吞吐量，并集成了基于P4的可编程数据包处理流水线（FXP），用于处理云网络任务。它还包括用于数据包处理的内联加密块、用于服务质量的流量整形器以及支持Falcon和Swift协议的RDMA传输卸载。

“摩根山”具有32条PCIe Gen 5通道，支持多主机（最多四个服务器）、无头（独立服务器）和融合（PCIe交换机）模式，展示了IO灵活性。它允许连接到SSD、GPU和其他设备，以适应各种云基础设施需求。

英特尔希望通过其可定制和适应性强的IPU设计，扩展到传统CPU之外，并占领云加速市场的一部分份额。

---

## 43. 西班牙蓬特韦德拉宣布其整个市区为“限行区”

**原文标题**: Pontevedra, Spain declares its entire urban area a "reduced traffic zone"

**原文链接**: [https://www.greeneuropeanjournal.eu/made-for-people-not-cars-reclaiming-european-cities/](https://www.greeneuropeanjournal.eu/made-for-people-not-cars-reclaiming-european-cities/)

西班牙蓬特韦德拉：以居民为先的“减车区”典范

西班牙蓬特韦德拉成功地将其市区转变为“减车区”，在没有完全禁车的情况下，优先考虑居民而非汽车。自市长米格尔·安赫·费尔南德斯·洛雷斯于1999年当选以来，该市实施了一系列旨在收回公共空间和改善空气质量的政策，其成果甚至超过了国家标准。

与其他因政府强制令而实施低排放区 (LEZ) 的西班牙城市不同，蓬特韦德拉采取了更为雄心勃勃的措施，限制不必要的交通。 过境交通和绕圈寻找停车位的行为被禁止，交通被分流到环城公路，从而实现了整体交通量减少40%的目标。只有“必要的交通”，如紧急车辆和需要进入车库的车辆才被允许通行，并且对送货和搬家的时间进行了限制。

这一转变带来了显著的改善：十年内未发生致命事故，步行和自行车出行率大幅提高（2021年达到90%），二氧化碳排放量减少了67%。 该城市的布局优先考虑行人，其次是自行车、公共交通，最后才是私家车。

蓬特韦德拉的成功归功于其专注于创建一个紧凑型城市，拥有混合用途的街区，不鼓励在郊区建立大型百货商店，并保持适宜步行的环境。 这种方法重振了市中心，支持了当地企业，并培养了更强的社区意识。该市的成功为其他旨在改善城市环境和优先考虑行人友好空间的欧洲城市提供了一个典范。

---

## 44. Hot Chips 2025：第一场 – CPU

**原文标题**: Hot Chips 2025: Session 1 – CPUs

**原文链接**: [https://chipsandcheese.com/p/hot-chips-2025-session-1-cpus](https://chipsandcheese.com/p/hot-chips-2025-session-1-cpus)

本文总结了Hot Chips 2025大会上以CPU为主题的会议。该会议包括来自四家公司的演讲：

*   **Condor Computing:** 推出了他们新的“Cuzco”RISC-V核心。
*   **PEZY:** 讨论了他们即将推出的“SC4s”芯片。
*   **IBM:** 展示了他们已经上市的“Power11”芯片。
*   **Intel:** 分享了有关他们即将推出的基于E-Core的Xeon CPU的详细信息，代号为“Clearwater Forest”。

本文还提供了指向关于每个展示的芯片及其各自演示文稿的更详细文章的链接。

---

## 45. 纯粹与非纯粹的软件工程

**原文标题**: Pure and Impure Software Engineering

**原文链接**: [https://www.seangoedecke.com/pure-and-impure-engineering/](https://www.seangoedecke.com/pure-and-impure-engineering/)

本文区分了“纯粹”和“不纯粹”的软件工程，认为它们是具有不同目标和技能组合的不同领域。纯粹工程侧重于技术上的完美，类似于艺术或研究，常见于开源项目中。不纯粹工程优先考虑高效地解决现实世界的问题，这在付费科技公司的工作中很常见，其中截止日期和妥协至关重要。

作者认为，在2010年代，科技公司经常资助纯粹工程项目以进行公关和占用工程师的时间，但2020年代向盈利能力的转变已经贬低了这些角色的价值。虽然科技公司需要这两种类型，但不纯粹工程对于发布功能和在大型组织内进行妥协至关重要。

作者认为，纯粹的工程师经常低估不纯粹工程的复杂性，后者涉及驾驭政治格局、遗留代码和业务需求。像Casey Muratori和George Hotz这样的例子被用来展示高技能的纯粹工程师如何在不纯粹的环境中挣扎。

文章还探讨了人工智能工具的不同看法。纯粹的工程师经常发现它们毫无用处，而不纯粹的工程师可以利用它们来提高效率，因为他们专注于在时间限制下解决不熟悉的问题。

总之，纯粹和不纯粹的工程都有价值，但它们需要不同的技能组合。由于不纯粹工程对商业价值的直接影响，科技公司优先考虑它。Leetcode招聘被解释为一种遗留方法，也是一种方便但并不完美的方式来识别一定程度的纯粹工程能力。

---

## 46. FFmpeg终极指南

**原文标题**: FFmpeg – The Ultimate Guide

**原文链接**: [https://img.ly/blog/ultimate-guide-to-ffmpeg/](https://img.ly/blog/ultimate-guide-to-ffmpeg/)

本文旨在作为FFmpeg的入门指南。FFmpeg是一个强大的多媒体框架，用于以自动化或脚本方式处理音频和视频。本文重点介绍了FFmpeg的功能，将其与非线性视频编辑器进行比较，并展示了其通过命令行操作执行导入、裁剪、添加叠加、应用效果以及以各种格式导出等任务的能力。

本指南涵盖了在不同平台（Linux、Mac、Windows）上的安装、其历史以及广泛支持的编解码器和格式。它强调了编译标志对于定制和优化的重要性，包括用于可移植性的静态构建和用于许可或大小考虑的有选择地包含编解码器。

FFmpeg的优势概述如下：广泛的过滤功能、硬件加速支持（例如，NVIDIA显卡）以及通用的输入/输出方法（网络摄像头、麦克风、网址、文件、流等）。本文还包括用于将示例命令适应于不同操作系统的实用建议。

本指南的很大一部分致力于解释基本的媒体概念，例如音频采样率、比特率、通道（单声道、立体声、5.1）、图像分辨率、位深度、透明度、视频帧速率以及视频编解码器对于压缩的重要性。它为各种设置提供大致值，并解释了这些参数如何影响质量和文件大小。

---

## 47. 欧盟Apple账号的AirPods实时翻译功能被阻止

**原文标题**: AirPods Live Translation Blocked for EU Users with EU Apple Accounts

**原文链接**: [https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/](https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/)

苹果AirPods实时翻译功能下周发布，欧盟Apple ID用户将无法使用 (AirPods Pro 3同期发布，受欧盟人工智能法案和GDPR等严格法规影响，隐私、同意和数据处理或需监管机构审查。该功能也将支持旧款AirPods，包括AirPods 4（带主动降噪）和AirPods Pro 2，可在英语、法语、德语、巴西葡萄牙语和西班牙语之间进行实时免提翻译，并利用Apple Intelligence在iPhone上显示实时字幕，当双方都佩戴兼容的AirPods时，自动降低另一位说话者的音量。实时翻译需要最新的AirPods固件、iOS 26（9月15日可用）和支持Apple Intelligence的iPhone（iPhone 15 Pro及更新机型）。计划今年晚些时候支持意大利语、日语、韩语和简体中文。欧盟用户限制原因尚不明确，作者已联系苹果寻求更多细节。)

---

## 48. 美国电动汽车销量8月打破纪录，特斯拉失去市场份额

**原文标题**: US EV sales smash records in August as Tesla loses ground

**原文链接**: [https://electrek.co/2025/09/10/us-ev-sales-smash-records-in-august-as-tesla-loses-ground/](https://electrek.co/2025/09/10/us-ev-sales-smash-records-in-august-as-tesla-loses-ground/)

美国8月电动汽车销量创历史新高，达146,332辆，占新车总销量的9.9%。 这次激增归因于联邦电动汽车税收抵免即将到期，分析师预测2025年第三季度将是美国历史上电动汽车销量最强劲的季度。

8月电动汽车的平均交易价格 (ATP) 上升至 57,245 美元，比 7 月份上涨 3.1%，但与去年同期相比相对持平。 激励措施仍然相当可观，平均每辆电动汽车超过 9,000 美元，远高于整个汽车市场的激励措施。

虽然特斯拉仍然是美国电动汽车销量的领导者，但它正面临越来越大的压力。 特斯拉的销量同比下降 6.7%，导致其市场份额降至创纪录的 38%。 尽管 8 月份价格上涨，但特斯拉的 ATP 仍比去年下降 5.5%。 专家指出，特斯拉缺乏创新和新产品是销量下降的主要原因，因为竞争对手推出了新的电动汽车车型，为消费者提供了更多选择。 目前，电动汽车销量的激增是由产品创新和经销商的积极性推动的。

---

## 49. 我用Varnish和Nginx搭建了自己的CDN。

**原文标题**: I built my own CDN with Varnish and Nginx

**原文链接**: [https://polso.info/i-built-my-own-cdn](https://polso.info/i-built-my-own-cdn)

克里斯蒂安·波尔索详细介绍了使用Varnish和Nginx构建自定义CDN的经验，其动机是为了获得更大的控制权、潜在的成本节约以及比BunnyCDN等商业服务更高的缓存命中率。

他选择了Leaseweb，因为它拥有廉价的全球网络和快速的NVMe存储。他的设置使用Debian，Nginx作为Web服务器，Varnish用于缓存，并将缓存存储在磁盘上。目前，他使用法兰克福、洛杉矶和新加坡的三台服务器。

最初的设置很顺利，直到他遇到SSL证书的问题。他实施了一种“推送策略”，即在后端服务器上颁发Let's Encrypt证书，然后每天通过rsync同步到所有CDN服务器。

对于基于地理位置的DNS路由，由于管理自己的权威DNS服务器的复杂性，他不得不依赖Bunny的DNS平台。

尽管没有比商业选项便宜很多（目前每月90美元，而之前的服务为每月100美元），但他对结果感到满意。他的网站感觉更快，缓存命中率正在攀升，已经超过了他使用BunnyCDN时所达到的水平。增加的控制权也允许更多的自定义。

未来的计划包括扩展到更多的服务器位置、托管自己的地理路由DNS以及实施更好的Web应用程序防火墙（WAF）以提高安全性。

---

## 50. 我带儿子去博物馆不是为了看屏幕的。

**原文标题**: I didn't bring my son to a museum to look at screens

**原文链接**: [https://sethpurcell.com/writing/screens-in-museums/](https://sethpurcell.com/writing/screens-in-museums/)

作者追忆童年时期在费城富兰克林学会（TFI）——一家互动式科学博物馆——的珍贵经历，并将其与最近一次带儿子参观的经历进行对比。他对馆内屏幕和触摸屏展览的过度泛滥表示失望，他认为这些展品偏离了博物馆提供切实的、互动式科学体验的初衷。

他将屏幕与童年时期操控真实物体并亲身体验科学现象的记忆进行对比，认为触摸屏并非真正意义上的“动手”，也无法以同样的方式激发孩子们的思维。

虽然承认TFI仍然有一些有价值的动手展览，尤其是在艾萨克爵士的阁楼和航空展厅等区域，但他指出，这些展览中的许多都维护不善。他对预算优先事项明显转向屏幕展览表示遗憾，这些展览占据了中心位置，而物理展览则被降级到不太显眼的位置。

作者怀疑博物馆引入屏幕是为了在这个屏幕主导的世界中争夺注意力，但他认为这是误入歧途。他呼吁TFI和其他博物馆优先考虑真实世界的、切实的体验，并移除屏幕展览，他认为孩子们需要远离屏幕，并与物理世界建立更强的联系。他强调，博物馆的价值在于呈现真实的物体和体验，从而调动感官，而不是数字模拟。

---

## 51. Kerberoasting
克爾布羅斯汀攻擊

**原文标题**: Kerberoasting

**原文链接**: [https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/](https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/)

马修·格林的这篇文章深入探讨了微软活动目录(AD)中的Kerberoasting漏洞，AD是网络访问控制的关键系统。格林强调，AD虽然可以追溯到1999年，但仍然依赖于1989年的Kerberos协议，而且至关重要的是，它支持像RC4这样过时的加密技术。

Kerberoasting利用了这样一个事实：攻击者一旦攻陷一台员工笔记本电脑，就可以从AD请求加密的“票据”来访问网络“服务”。如果某个服务配置了弱的、人为生成的密码，而不是强大的、随机生成的密钥，攻击者就可以获得此票据，并使用字典攻击离线破解它。成功破解密码会使他们获得对目标服务的完全控制权，通常会导致勒索软件攻击。

虽然现代身份验证模式使用带有PBKDF2哈希的AES加密，但较旧的配置可能会退回到RC4与未加盐的NT哈希组合。这使得密码破解速度呈指数级增长（大约快1000倍），每秒允许数十亿次的密码猜测。

格林批评微软没有主动禁用这些不安全的、遗留的加密选项。尽管Kerberoasting漏洞广为人知，并在最近发生的攻击（如对Ascension Health的攻击）中被利用，但微软的建议仅仅是管理员使用强密码、禁用RC4并实施适当的密钥管理。格林总结说，微软需要更加积极地强制升级并消除过时的服务，以防止这些攻击，并认为在现代安全环境中继续支持过时的加密技术是不可接受的。

---

## 52. 展示HN：Haystack – 像写自己代码一样审查pull request

**原文标题**: Show HN: Haystack – Review pull requests like you wrote them yourself

**原文链接**: [https://haystackeditor.com](https://haystackeditor.com)

Haystack旨在简化拉取请求审查流程，最终加快合并速度。其标语“像自己编写代码一样审查拉取请求”表明该平台旨在为审查者提供深刻的理解和上下文，从而实现更高效的反馈。这意味着Haystack提供的功能超越了基本的差异查看和评论。它可能包含帮助审查者快速掌握拉取请求中代码更改的目的、影响和整体作用的功能。对速度和高效合并的关注表明，Haystack可能提供与现有开发工作流程和工具的集成，以最大限度地减少代码审查过程中的摩擦和瓶颈。通过提高审查者的理解能力并减少来回沟通，Haystack旨在加速软件开发生命周期。

海斯塔克旨在简化拉取请求审查流程，从而最终加快合并速度。 标语“像自己编写代码一样审查拉取请求”表明该平台旨在为审查者提供深刻的理解和背景信息，从而实现更有效和高效的反馈。 这意味着 Haystack 提供的功能不仅限于基本的差异查看和评论。 它可能包括帮助审阅者快速掌握拉取请求中代码更改的目的、影响和整体影响的功能。 对速度和高效合并的关注表明，Haystack 可能会提供与现有开发工作流程和工具的集成，以最大限度地减少代码审查过程中的摩擦和瓶颈。 通过提高审阅者的理解能力并减少来回沟通，Haystack 旨在加速软件开发生命周期。

---

## 53. 数学科学中的欺诈性出版

**原文标题**: Fraudulent Publishing in the Mathematical Sciences

**原文链接**: [https://arxiv.org/abs/2509.07257](https://arxiv.org/abs/2509.07257)

这篇arXiv预印本(arXiv:2509.07257)于2025年9月8日提交，探讨了数学科学领域内欺诈性出版的问题。该论文由Ilka Agricola和另外五位研究人员撰写，是国际数学联盟(IMU)和国际工业与应用数学理事会(ICIAM)联合工作组的首个出版物。

该报告分析了当前数学出版的现状，并指出了由此产生的问题。它为第二份出版物奠定了基础，该出版物将为研究人员、政策制定者和数学研究评估者提供具体的建议、指南和最佳实践。这份后续论文旨在为社区提供检测和抵制操纵文献计量指标企图的工具，从而恢复对研究评估的控制，并促进该领域必要的变革。

这篇文章被归类为数学领域内的“历史与概述”主题（math.HO）。该论文的印刷版，精选了最重要的参考文献，计划在2025年10月的美国数学学会通告（Notices of the AMS）上发表。该预印本提供完整的可点击参考文献，并可以使用提供的arXiv标识符进行引用。提交内容包括查看PDF和实验性HTML版本的链接。该页面还提供指向书目工具、相关论文以及可能与该研究相关的代码/数据存储库的链接。

---

## 54. Clojure解决表达式问题方案

**原文标题**: Clojure's Solutions to the Expression Problem

**原文链接**: [https://www.infoq.com/presentations/Clojure-Expression-Problem/](https://www.infoq.com/presentations/Clojure-Expression-Problem/)

InfoQ文章摘要：Chris Houser关于Clojure解决表达式问题的演讲。该演讲重点介绍Clojure如何解决表达式问题，这是软件设计中的一个经典挑战，涉及在不修改现有代码的情况下添加新的数据类型和操作。

Houser在深入探讨Clojure的方法之前，先介绍了表达式问题以及其他语言中的传统解决方案。他展示了Clojure的两个关键特性，多方法和协议，作为解决该问题的可行方案。

该演讲可能强调了Clojure环境中每种方法的优缺点。多方法允许基于参数类型进行动态调度，提供了灵活性，但也可能牺牲一些性能。协议定义了接口，提供编译时类型检查和改进的性能，但需要更多的前期设计。

Chris Houser是《Clojure的乐趣》的合著者和Clojure贡献者，他在2010年的Strange Loop大会上录制了这次演讲。Strange Loop是一个由开发者运营的大会，专注于创新技术和各种编程范例的交叉。文章还提到Clojure是一种JVM语言，并且该演讲与开发、Java和LISP相关。

---

## 55. 展示HN：TailGuard – 通过容器将你的WireGuard路由器桥接到Tailscale

**原文标题**: Show HN: TailGuard – Bridge your WireGuard router into Tailscale via a container

**原文链接**: [https://github.com/juhovh/tailguard](https://github.com/juhovh/tailguard)

TailGuard：将WireGuard桥接到Tailscale网络的Docker容器应用。它特别适用于WireGuard设备缺乏原生Tailscale支持或直接访问的情况。TailGuard通过一个服务器（理想情况下是靠近WireGuard服务器的VPS）将WireGuard连接隧道传输到Tailscale网络。

这种方法的优势包括集中式WireGuard密钥管理、更简单的新设备加入、灵活的出口节点切换、在单VPN设备上同时访问WireGuard和Tailscale，以及将仅支持WireGuard的路由器连接到Tailscale。

安装过程包括下载WireGuard客户端配置（wg0.conf）并运行具有适当网络和卷映射的Docker容器。该容器需要NET_ADMIN权限和sysctl配置以进行IP转发。系统会提示用户通过提供的URL使用其Tailscale帐户对容器进行身份验证。 Docker compose是构建镜像的另一种选择。

高级设置允许通过设置`TS_DEST_IP`环境变量来路由发往WireGuard服务器的流量。该配置还可以广播WireGuard背后的LAN网络。

配置参数作为环境变量提供，用于控制WireGuard和Tailscale设备名称、端口、身份验证密钥、目标IP和主机名。

虽然TailGuard会自动在Tailscale网络上广播WireGuard子网，但需要在WireGuard端进行手动路由配置，才能将Tailscale流量路由回隧道。

---

## 56. 语义化换行 (2017)

**原文标题**: Semantic Line Breaks (2017)

**原文链接**: [https://sembr.org](https://sembr.org)

语义换行提倡在源代码中使用换行符来提高可读性和可维护性，而不改变最终的渲染输出。它侧重于使用这些换行符来反映文本的逻辑结构，以便更容易地进行创作、编辑和协作。其核心思想是在重要的思想单元之后插入换行符，例如句子、从句或列表项。

规范 (SemBr) 概述了实施指南：换行符*必须*不改变输出，*应该*不改变含义，并且*必须*出现在句子之后。它们*应该*出现在独立从句之后，并且*可以*出现在从属从句之前或列表之前。*建议*最大行长度为 80 个字符。

文章解答了常见问题，建议大声朗读文本以识别自然停顿点进行换行。它建议对现有文档逐步迁移到语义换行，并提供 `git diff --word-diff` 命令以实现更好的修订跟踪。它还建议不要使用尾随空格进行换行，因为它与某些编辑器不兼容，而是倾向于使用 `<br/>` 元素进行强制换行。

支持的标记语言包括 AsciiDoc、CommonMark、Markdown 等。最终，语义换行对于最终用户是不可见的，但为编写者和编辑者在管理和理解源代码方面提供了显著的好处。

---

## 57. Tarsnap 很舒适

**原文标题**: Tarsnap is cozy

**原文链接**: [https://til.andrew-quinn.me/posts/tarsnap-is-cozy/](https://til.andrew-quinn.me/posts/tarsnap-is-cozy/)

本文表达了作者使用Tarsnap在线备份服务（尤其是针对关键数据）的积极体验。作者强调了Tarsnap令人感到舒适和周全的感觉，突出了其对Unix系统管理员的可用性及其强大的产品设计。

要点包括：

*   **Tarsnap概述：** 它被描述为一种以安全性和可靠性著称的备份解决方案，由Colin Percival博士创建，主要由他和他的兄弟运营。
*   **可用性和设计：** 命令行界面（CLI）因其与`tar`的相似性而受到称赞，使其熟悉且易于使用。
*   **匿名性：** 预付费模式允许用户通过粉碎密钥文件并让剩余余额过期来保持匿名性，从而导致备份数据的删除。
*   **自动化：** 作者感到足够安全，可以使用cronjob自动化备份。
*   **定价：** 作者通过提供Tarsnap成本估算器来解决对定价的担忧，并指出对于少量关键数据，即使是少量初始付款也可以持续很长时间。
*   **功能请求：** 作者建议硬件密钥支持可能带来的额外安全性，并承认创建者可能已经考虑过这一点。
*   **总体印象：** 作者最后赞扬Tarsnap是“梦寐以求的产品”。

---

## 58. 我通过入侵GameCube内存，用实时LLM替换了《动物森友会》的对话。

**原文标题**: I replaced Animal Crossing's dialogue with a live LLM by hacking GameCube memory

**原文链接**: [https://joshfonseca.com/blogs/animal-crossing-llm](https://joshfonseca.com/blogs/animal-crossing-llm)

乔希破解了GameCube上的《动物森友会》，用实时AI生成的对话替换了重复的对话。他通过使用Dolphin模拟器和一个巧妙的“内存邮箱”系统实现了这一点，而没有修改原始游戏的代码。这涉及到识别对话文本和说话者姓名的稳定内存地址，允许一个Python脚本直接读写数据到GameCube的RAM中。

这个过程始于分析反编译的游戏代码，以了解对话系统及其自定义编码。乔希发现游戏使用类似于HTML标签的控制代码来控制文本格式、情感和对话流程。然后，他创建了一个Python编码器/解码器，以在人类可读的文本和游戏的内部语言之间进行转换。

为了生成对话，乔希使用了一个双模型AI流水线：一个专注于创造性的、符合角色设定的对话的“作者”LLM（基于抓取的角色信息），以及一个使用游戏的控制代码来添加停顿、颜色和情感等技术元素的“导演”LLM。

该系统被输入新闻订阅源和一个共享内存用于“八卦”，以在游戏中创建突发行为，导致村民将时事融入到他们的对话中，并形成对汤姆·努克的看法。尽管GameCube有一个宽带适配器，但使用内存邮箱被证明是一个更简单、更确定的解决方案，绕过了在游戏中实现复杂网络协议栈的需要。整个项目的代码，包括内存接口和AI逻辑，都可以在GitHub上找到。

---

## 59. 用蓝光去除织物上的黄渍

**原文标题**: Removing yellow stains from fabric with blue light

**原文链接**: [https://phys.org/news/2025-09-yellow-fabric-blue.html](https://phys.org/news/2025-09-yellow-fabric-blue.html)

ACS Sustainable Chemistry & Engineering 上的这篇文章报道了一种利用高强度蓝色 LED 光去除织物上黄色污渍的新方法。 研究人员发现，这种方法可以有效去除棉、丝绸和聚酯等各种织物上由汗液、橙汁和番茄汁引起的污渍。 该方法是环境友好的，因为它利用可见蓝光和环境氧气作为氧化剂，避免使用过氧化氢或干洗溶剂等刺激性化学物质，这些物质可能有害且不适合精致织物。

研究人员发现，将黄色污渍暴露于蓝色 LED 光下短时间（约 10 分钟），可显着减少黄色。 其原理是将污渍中存在的有色化合物（如 β-胡萝卜素、番茄红素、角鲨烯和油酸）分解成无色化合物。 在去除棉花上的角鲨烯污渍方面，蓝光法被证明比过氧化氢或紫外线照射更有效，紫外线照射甚至会产生新的黄色化合物。 此外，蓝光处理不会损坏测试的织物。

研究人员计划在将该技术商业化用于家庭和工业用途之前，进行进一步的色牢度和安全性测试。 该研究强调了使用可见光作为化学去污方法的可持续替代方案的潜力。

---

## 60. 所有带有点击轮的iPod游戏现已全部保存下来，以供后人瞻仰。

**原文标题**: All clickwheel iPod games have now been preserved for posterity

**原文链接**: [https://arstechnica.com/gaming/2025/09/all-54-lost-clickwheel-ipod-games-have-now-been-preserved-for-posterity/](https://arstechnica.com/gaming/2025/09/all-54-lost-clickwheel-ipod-games-have-now-been-preserved-for-posterity/)

一个经典iPod爱好者社区成功保存了苹果在2000年代后期销售的所有54款官方滚轮游戏。通过克服苹果的FairPlay DRM，由GitHub用户Olsro领导的iPod滚轮游戏保存项目，通过一个协调的虚拟机，从原版游戏拥有者那里同步游戏，创建了一个“主库”。

这个过程充满挑战，需要付出巨大的努力来指导拥有游戏库的个人克服技术障碍，并处理老化的iPod和硬盘的硬件故障。该社区还面临苹果关闭游戏授权所需服务器的威胁。

现在，完整的游戏合集可供iPod 5G+和iPod Nano 3G+用户访问，他们可以离线同步游戏库。他们可以使用GitHub上的说明设置虚拟机，或者下载一个在互联网档案馆上发布的种子合集。该项目旨在确保苹果的这段游戏历史能够被永久保存，并有可能用于安全研究。社区成员称赞了这项保存工作所带来的怀旧价值，例如一位用户称iPod版的刺猬索尼克是他接触该系列和速通的启蒙。

---

## 61. 时区数据库的工作原理

**原文标题**: How the Tz Database Works

**原文链接**: [https://yatsushi.com/blog/tz-database/](https://yatsushi.com/blog/tz-database/)

无法访问文章链接。

---

## 62. 多语种程序员的多重分派指南 (2016)

**原文标题**: A polyglot's guide to multiple-dispatch (2016)

**原文链接**: [https://eli.thegreenplace.net/2016/a-polyglots-guide-to-multiple-dispatch/](https://eli.thegreenplace.net/2016/a-polyglots-guide-to-multiple-dispatch/)

多重分发：概念、C++实现及形状相交示例

---

## 63. OrioleDB 专利：现已免费提供给 Postgres 社区

**原文标题**: OrioleDB Patent: now freely available to the Postgres community

**原文链接**: [https://supabase.com/blog/orioledb-patent-free](https://supabase.com/blog/orioledb-patent-free)

该文章宣布，旨在提升性能和可扩展性的Postgres扩展OrioleDB相关专利现已免费提供给Postgres社区使用。这意味着开发者和用户可以利用该专利涵盖的技术，无需担心侵权或许可费用。此举体现了对开源原则的承诺，并促进Postgres生态系统内的创新。它允许社区在没有法律限制的情况下进一步开发、改进和集成OrioleDB。 这种可用性可能会扩大OrioleDB的应用和影响，通过提供一个处理大型和复杂数据集的潜在强大工具，从而使更广泛的Postgres用户受益。该声明强调了作者对协作开发的信念，并旨在鼓励Postgres社区内的贡献和进步，特别是与OrioleDB相关的方面。

---

## 64. Dotter：用 Rust 编写的点文件管理器和模板引擎

**原文标题**: Dotter: Dotfile manager and templater written in Rust

**原文链接**: [https://github.com/SuperCuber/dotter](https://github.com/SuperCuber/dotter)

Dotter 是一个用 Rust 编写的 dotfile 管理器和模板引擎，旨在简化配置文件 (dotfiles) 的管理和部署。它解决了手动管理 dotfiles 的常见问题，例如难以追踪来源、在新机器上设置繁琐以及缺乏针对特定机器的配置。

Dotter 提供灵活的配置、自动模板和符号链接到目标位置。可以通过 Homebrew (Mac)、AUR (Arch Linux)、Scoop (Windows)、预构建的二进制文件或 Cargo 进行安装。

主要特性包括：

*   **组织化管理：** 解决了追踪 dotfile 来源的问题。
*   **自动化部署：** 简化了在新机器上的设置。
*   **机器特定配置：** 处理不同机器之间的差异。
*   **模板化：** 允许使用模板进行动态配置。
*   **部署/撤销部署：** `deploy` 命令创建或更新符号链接，`undeploy` 命令删除它们。
*   **Dry-run 模式：** 模拟部署而不进行更改。
*   **Watch 模式：** 在文件修改后自动部署更改。

`dotter` 命令提供各种选项，例如指定配置文件位置、启用 dry-run 模式、强制覆盖以及控制详细程度。 欢迎贡献，并可以通过捐赠提供支持。 Wiki 提供了有关设置、配置、模板和部署的广泛文档。

---

## 65. Picat：一种基于逻辑的多范式语言 (2014) [pdf]

**原文标题**: Picat: A Logic-based Multi-paradigm Language (2014) [pdf]

**原文链接**: [https://logicprogramming.org/wp-content/uploads/2014/07/alp14.pdf](https://logicprogramming.org/wp-content/uploads/2014/07/alp14.pdf)

该PDF文档似乎是2014年发表的题为“Picat：一种基于逻辑的多范式语言”的研究论文的开头部分。遗憾的是，提供的内容主要由压缩的PDF数据组成，只能确定标题。因此，无法根据文章的完整内容进行完整的摘要。

然而，仅根据标题，我们可以推断该论文可能讨论了Picat编程语言。标题表明Picat是一种基于逻辑的语言，这意味着它可能包含了逻辑编程的原理。此外，它被描述为多范式，这意味着Picat除了逻辑编程之外，还支持多种编程风格，可能包括命令式、函数式或其他范式。因此，该论文可能解释了Picat语言的特性、设计原则和潜在应用，重点在于其逻辑和其他编程范式的独特结合。它可能描述了这些范式如何集成以及如何用于解决各种计算问题。2014年的日期也表明该论文提供了关于当时人们对Picat的理解和发展的相关信息。

---

## 66. 附近厕所 – 厕所界的Airbnb，出租厕所赚钱

**原文标题**: NearToilets – Airbnb of toilets, earn from toilets for rent

**原文链接**: [https://neartoilets.com/](https://neartoilets.com/)

NearToilets 致力于成为“厕所界的 Airbnb”，创建一个平台，方便人们寻找和租用干净、附近的公共厕所。其核心概念围绕着私人厕所的货币化，允许房主、企业和其他房产所有者将其设施出租给公众。 这解决了寻找无障碍且干净厕所的常见问题，尤其是在城市地区或旅行时。

该平台很可能促进寻求厕所的人和提供厕所的人之间的联系。这可能涉及一个移动应用程序或网站，根据位置、清洁度评分和价格显示可用的厕所。 然后，用户可以通过该平台预订并支付费用。

“从出租厕所中赚钱”这一方面强调了房产所有者通过提供厕所来产生收入的潜力。 NearToilets 大概会处理付款流程，并可能提供管理预订和维护清洁标准的功能。 总体目标似乎是在改善公共厕所的访问的同时，为拥有厕所的人创造新的收入来源。

---

## 67. 使用Gappa正式验证浮点除法程序 – 第一部分

**原文标题**: Formally verifying a floating-point division routine with Gappa – part 1

**原文链接**: [https://community.arm.com/arm-community-blogs/b/embedded-and-microcontrollers-blog/posts/formally-verifying-a-floating-point-division-routine-with-gappa-p1](https://community.arm.com/arm-community-blogs/b/embedded-and-microcontrollers-blog/posts/formally-verifying-a-floating-point-division-routine-with-gappa-p1)

本文介绍了一个项目，该项目专注于使用Gappa工具对浮点除法程序进行形式化验证。核心思想在于严格证明以浮点运算实现的除法算法的正确性。这至关重要，因为浮点运算本质上是不精确的，并且误差会累积，可能导致不正确的结果。

本文强调了验证浮点计算所涉及的挑战。这些挑战源于浮点运算的非直观性，包括舍入误差、溢出和下溢的可能性，以及确保在各种输入范围内准确性的复杂性。特别是，“挑战验证”部分可能表示作者打算使用此除法程序验证作为Gappa的一个具有挑战性但有价值的测试用例。他们的目标是展示Gappa在处理复杂数值验证任务方面的能力。 本质上，本文为详细解释他们使用Gappa对浮点除法程序进行形式化验证的方法奠定了基础，突出了该任务的重要性以及与之相关的固有困难。

---

## 68. Some thoughts on personal Git hosting

**原文标题**: Some thoughts on personal Git hosting

**原文链接**: [https://shkspr.mobi/blog/2025/09/some-thoughts-on-personal-git-hosting/](https://shkspr.mobi/blog/2025/09/some-thoughts-on-personal-git-hosting/)

This article discusses the author's exploration of self-hosting personal Git projects as an alternative to platforms like GitHub, GitLab, and CodeBerg, aiming for greater decentralization. They are using PikaPod to host a Gitea instance under their own domain (git.edent.tel).

The author identifies several drawbacks to this approach, including the significant network effects of GitHub, making collaboration and contribution easier. While Gitea supports OAuth for easier login, it's still a barrier compared to GitHub's ubiquity. Forking is also not federated; users must create forks on the author's server, lacking the seamlessness of forking on platforms like GitHub. Discoverability is another issue, as the author's code will primarily be found via general search engines rather than platform-specific searches. They also highlight the administrative overhead, even with PikaPod handling hosting, and the loss of potential sponsorship income that comes from GitHub.

The author concludes that while self-hosting offers control, it comes with trade-offs. Their plan is to keep popular and sponsored repositories on GitHub while moving smaller projects and creating new ones on their Gitea instance. They are also seeking a hosted Forgejo instance with similar domain name support at a comparable or lower price. The author acknowledges the challenges in replacing GitHub entirely but aims for a balanced approach.


---

## 69. iPhone Air

**原文标题**: iPhone Air

**原文链接**: [https://www.apple.com/newsroom/2025/09/introducing-iphone-air-a-powerful-new-iphone-with-a-breakthrough-design/](https://www.apple.com/newsroom/2025/09/introducing-iphone-air-a-powerful-new-iphone-with-a-breakthrough-design/)

生成摘要时出错

---

## 70. A love letter to the CSV format (2024)

**原文标题**: A love letter to the CSV format (2024)

**原文链接**: [https://medialab.sciencespo.fr/en/news/a-love-letter-to-the-csv-format/](https://medialab.sciencespo.fr/en/news/a-love-letter-to-the-csv-format/)

生成摘要时出错

---

## 71. Zoox robotaxi launches in Las Vegas

**原文标题**: Zoox robotaxi launches in Las Vegas

**原文链接**: [https://zoox.com/journal/las-vegas](https://zoox.com/journal/las-vegas)

生成摘要时出错

---

## 72. R-Zero: Self-Evolving Reasoning LLM from Zero Data

**原文标题**: R-Zero: Self-Evolving Reasoning LLM from Zero Data

**原文链接**: [https://arxiv.org/abs/2508.05004](https://arxiv.org/abs/2508.05004)

生成摘要时出错

---

## 73. Things you can do with a debugger but not with print debugging

**原文标题**: Things you can do with a debugger but not with print debugging

**原文链接**: [https://mahesh-hegde.github.io/posts/what_debugger_can/](https://mahesh-hegde.github.io/posts/what_debugger_can/)

生成摘要时出错

---

## 74. Charlie Kirk killed at event in Utah

**原文标题**: Charlie Kirk killed at event in Utah

**原文链接**: [https://www.nbcnews.com/news/us-news/live-blog/live-updates-shooting-charlie-kirk-event-utah-rcna230437](https://www.nbcnews.com/news/us-news/live-blog/live-updates-shooting-charlie-kirk-event-utah-rcna230437)

生成摘要时出错

---

## 75. Distributing your own scripts via Homebrew

**原文标题**: Distributing your own scripts via Homebrew

**原文链接**: [https://justin.searls.co/posts/how-to-distribute-your-own-scripts-via-homebrew/](https://justin.searls.co/posts/how-to-distribute-your-own-scripts-via-homebrew/)

生成摘要时出错

---

## 76. The origin story of merge queues

**原文标题**: The origin story of merge queues

**原文链接**: [https://mergify.com/blog/the-origin-story-of-merge-queues](https://mergify.com/blog/the-origin-story-of-merge-queues)

生成摘要时出错

---

## 77. NASA bars Chinese citizens from its facilities, networks

**原文标题**: NASA bars Chinese citizens from its facilities, networks

**原文链接**: [https://www.theregister.com/2025/09/11/nasa_china_ban/](https://www.theregister.com/2025/09/11/nasa_china_ban/)

生成摘要时出错

---

## 78. Vietnam to close 86M bank accounts for lack of biometric data

**原文标题**: Vietnam to close 86M bank accounts for lack of biometric data

**原文链接**: [https://vietnamnet.vn/en/vietnam-to-close-86-million-inactive-bank-accounts-by-september-2407820.html](https://vietnamnet.vn/en/vietnam-to-close-86-million-inactive-bank-accounts-by-september-2407820.html)

生成摘要时出错

---

## 79. Knowledge and memory

**原文标题**: Knowledge and memory

**原文链接**: [https://www.robinsloan.com/lab/knowledge-and-memory/](https://www.robinsloan.com/lab/knowledge-and-memory/)

生成摘要时出错

---

## 80. E-paper display reaches the realm of LCD screens

**原文标题**: E-paper display reaches the realm of LCD screens

**原文链接**: [https://spectrum.ieee.org/e-paper-display-modos](https://spectrum.ieee.org/e-paper-display-modos)

生成摘要时出错

---

## 81. Harvey Mudd Miniature Machine

**原文标题**: Harvey Mudd Miniature Machine

**原文链接**: [https://www.cs.hmc.edu/~cs5grad/cs5/hmmm/documentation/documentation.html](https://www.cs.hmc.edu/~cs5grad/cs5/hmmm/documentation/documentation.html)

生成摘要时出错

---

## 82. We can’t circumvent the work needed to train our minds

**原文标题**: We can’t circumvent the work needed to train our minds

**原文链接**: [https://zettelkasten.de/posts/the-scam-called-you-dont-have-to-remember-anything/](https://zettelkasten.de/posts/the-scam-called-you-dont-have-to-remember-anything/)

生成摘要时出错

---

## 83. In 1979 one of the best guitar solos recorded was cut for radio time

**原文标题**: In 1979 one of the best guitar solos recorded was cut for radio time

**原文链接**: [https://www.seekhifi.com/my-sharona-by-the-knack/](https://www.seekhifi.com/my-sharona-by-the-knack/)

生成摘要时出错

---

## 84. XNEdit – fast and classic X11 text editor

**原文标题**: XNEdit – fast and classic X11 text editor

**原文链接**: [https://www.unixwork.de/xnedit/](https://www.unixwork.de/xnedit/)

生成摘要时出错

---

## 85. Show HN: Bottlefire – Build single-executable microVMs from Docker images

**原文标题**: Show HN: Bottlefire – Build single-executable microVMs from Docker images

**原文链接**: [https://bottlefire.dev/](https://bottlefire.dev/)

生成摘要时出错

---

## 86. Claude now has access to a server-side container environment

**原文标题**: Claude now has access to a server-side container environment

**原文链接**: [https://www.anthropic.com/news/create-files](https://www.anthropic.com/news/create-files)

生成摘要时出错

---

## 87. Mistral raises 1.7B€, partners with ASML

**原文标题**: Mistral raises 1.7B€, partners with ASML

**原文链接**: [https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai)

生成摘要时出错

---

## 88. TikTok has turned culture into a feedback loop of impulse and machine learning

**原文标题**: TikTok has turned culture into a feedback loop of impulse and machine learning

**原文链接**: [https://www.thenexus.media/tiktok-won-now-everything-is-60-seconds/](https://www.thenexus.media/tiktok-won-now-everything-is-60-seconds/)

生成摘要时出错

---

## 89. Christie's Deletes Digital Art Department

**原文标题**: Christie's Deletes Digital Art Department

**原文链接**: [https://news.artnet.com/market/christies-scraps-digital-art-department-2685784](https://news.artnet.com/market/christies-scraps-digital-art-department-2685784)

生成摘要时出错

---

## 90. US High school students' scores fall in reading and math

**原文标题**: US High school students' scores fall in reading and math

**原文链接**: [https://apnews.com/article/naep-reading-math-scores-12th-grade-c18d6e3fbc125f12948cc70cb85a520a](https://apnews.com/article/naep-reading-math-scores-12th-grade-c18d6e3fbc125f12948cc70cb85a520a)

生成摘要时出错

---

## 91. Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文标题**: Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文链接**: [https://smalltransfers.com/](https://smalltransfers.com/)

生成摘要时出错

---

## 92. Rendering flame fractals with a compute shader (2023)

**原文标题**: Rendering flame fractals with a compute shader (2023)

**原文链接**: [https://wrighter.xyz/blog/2023_08_17_flame_fractals_in_comp_shader](https://wrighter.xyz/blog/2023_08_17_flame_fractals_in_comp_shader)

生成摘要时出错

---

## 93. Microsoft is officially sending employees back to the office

**原文标题**: Microsoft is officially sending employees back to the office

**原文链接**: [https://www.businessinsider.com/microsoft-send-employees-back-to-office-rto-remote-work-2025-9](https://www.businessinsider.com/microsoft-send-employees-back-to-office-rto-remote-work-2025-9)

生成摘要时出错

---

## 94. Deliberate Abstraction

**原文标题**: Deliberate Abstraction

**原文链接**: [https://entropicthoughts.com/deliberate-abstraction](https://entropicthoughts.com/deliberate-abstraction)

生成摘要时出错

---

## 95. Hypervisor in 1k Lines

**原文标题**: Hypervisor in 1k Lines

**原文链接**: [https://1000hv.seiya.me/en](https://1000hv.seiya.me/en)

生成摘要时出错

---

## 96. Bending Spoons Buys Video Platform Vimeo for $1.38B

**原文标题**: Bending Spoons Buys Video Platform Vimeo for $1.38B

**原文链接**: [https://petapixel.com/2025/09/10/bending-spoons-buys-video-platform-vimeo-for-1-38-billion/](https://petapixel.com/2025/09/10/bending-spoons-buys-video-platform-vimeo-for-1-38-billion/)

生成摘要时出错

---

## 97. Immunotherapy drug clinical trial results: half of tumors shrink or disappear

**原文标题**: Immunotherapy drug clinical trial results: half of tumors shrink or disappear

**原文链接**: [https://www.rockefeller.edu/news/38120-immunotherapy-drug-eliminates-aggressive-cancers-in-clinical-trial/](https://www.rockefeller.edu/news/38120-immunotherapy-drug-eliminates-aggressive-cancers-in-clinical-trial/)

生成摘要时出错

---

## 98. California bill that would regulate AI companion chatbots close to becoming law

**原文标题**: California bill that would regulate AI companion chatbots close to becoming law

**原文链接**: [https://techcrunch.com/2025/09/10/a-california-bill-that-would-regulate-ai-companion-chatbots-is-close-to-becoming-law/](https://techcrunch.com/2025/09/10/a-california-bill-that-would-regulate-ai-companion-chatbots-is-close-to-becoming-law/)

生成摘要时出错

---

## 99. NASA finds Titan's lakes may be creating vesicles with primitive cell walls

**原文标题**: NASA finds Titan's lakes may be creating vesicles with primitive cell walls

**原文链接**: [https://www.sciencedaily.com/releases/2025/08/250831112449.htm](https://www.sciencedaily.com/releases/2025/08/250831112449.htm)

生成摘要时出错

---

## 100. Four Fallacies of Modern AI

**原文标题**: Four Fallacies of Modern AI

**原文链接**: [https://blog.apiad.net/p/the-four-fallacies-of-modern-ai](https://blog.apiad.net/p/the-four-fallacies-of-modern-ai)

生成摘要时出错

---

