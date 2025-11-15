# Hacker News 热门文章摘要 (2025-11-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 富士通 Lifebook U729 上的 Linux

**原文标题**: Linux on the Fujitsu Lifebook U729

**原文链接**: [https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729](https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729)

本文详细介绍了作者在翻新的富士通 Lifebook U729 上使用 Linux 的体验。作者称赞这款笔记本电脑是一款令人愉快且功能强大的 Linux 设备，并强调了其小巧的尺寸、轻巧的设计、坚固的构建质量、良好的键盘以及开箱即用的硬件兼容性。

主要挑战是禁用 Secure Boot，该选项最初在 BIOS 中显示为灰色。作者通过以下方式解决了这个问题：首先安装 Windows 11（预装），通过 Windows Update 更新富士通特定的驱动程序，然后使用富士通提供的 DeskUpdate 工具更新 BIOS。更新后的 BIOS 启用了禁用 Secure Boot 的选项。

作者还在 BIOS 中发现并禁用了“Absolute Persistence”企业间谍软件。

本文证实，Wi-Fi、蓝牙、声音（使用 PipeWire）、显示屏亮度控制、触摸屏和网络摄像头都可以在 Linux（特别是 NixOS）上完美运行，无需额外配置。麦克风和指纹传感器未经测试。

最后，作者提供了有关启动时访问 BIOS (F2) 和启动菜单 (F12) 的说明。文章最后提供了指向富士通产品页面和数据表的链接。

---

## 2. 对Archive.today可疑压力的调查

**原文标题**: Our investigation into the suspicious pressure on Archive.today

**原文链接**: [https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html](https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html)

本文详细调查了一起针对Archive.today的可疑压力事件。AdGuard DNS（一项允许用户绕过付费墙的服务）收到了一个名为“Web Abuse Association Defense”（WAAD，网络滥用协会防御）的新成立的法国组织的联系，该组织声称致力于打击儿童色情。WAAD要求AdGuard屏蔽Archive.today，理由是其拒绝删除非法内容。

AdGuard认为这一要求很奇怪，并经过进一步调查，发现了不一致之处。WAAD的网站缺乏细节，其在线存在感极低，并且其声明的时间线与提供的“法警报告”不符。Archive.today迅速删除了被标记的内容，并表示他们之前没有收到过相关通知。他们还暗示存在“连续”投诉活动。

调查显示，WAAD的注册时间很短，并且很容易匿名进行。“法警报告”被WAAD用作证据，但大多数都是最近创建的，而不是像WAAD声称的那样在2023年创建的。2023年的两份报告与一位真正的律师有关，WAAD似乎冒充了他。

AdGuard得出结论，这些投诉非常可疑，可能是为了损害Archive.today而精心策划的，并且可能冒充了真实的人物。他们强调，法国法律会惩罚虚假报告。AdGuard将向法国警方提起正式投诉，理由是存在潜在的犯罪行为。这项调查恰逢有关FBI正在调查Archive.today所有者的报道，可能与CSAM有关，这增加了可疑的情况。

---

## 3. 适用于 Windows 11 的 Windhawk Windows 经典主题修改

**原文标题**: Windhawk Windows classic theme mod for Windows 11

**原文链接**: [https://windhawk.net/mods/classic-theme-enable](https://windhawk.net/mods/classic-theme-enable)

本文可能讨论一个使用Windhawk修改Windows 11的mod，旨在恢复或模拟经典Windows主题。由于仅显示“WindhawkYou need to enable JavaScript to run this app.”，表明文章的实际内容，可能是代码、说明或进一步解释，被隐藏，需要启用JavaScript才能查看。

核心思想是：**存在（或正在展示）一个Windhawk mod，旨在Windows 11中重现经典Windows主题的外观和感觉。** 启用JavaScript后可能才能访问该文章。

---

## 4. 最小化方差的平均加权

**原文标题**: Weighting an average to minimize variance

**原文链接**: [https://www.johndcook.com/blog/2025/11/12/minimum-variance/](https://www.johndcook.com/blog/2025/11/12/minimum-variance/)

本文探讨了如何在多个独立资产间进行最优投资配置以最小化投资组合波动性的问题。首先以两个资产A和B（A波动性更大）为例，证明了将两者混合，并向波动性较小的资产B倾斜是最佳策略。本文推导出了资产X（波动性较大的资产）的最优配置权重`t`，其基于X和Y（波动性较小的资产）的方差：`t = Var(Y) / (Var(X) + Var(Y))`。这表明Y的方差越小，X的配置越少。

然后，问题被推广到`n`个独立资产（Xi）。使用拉格朗日乘数法，本文得出了每个资产的最优配置权重`ti`的公式：`ti = 1/Var(Xi) / (Σ 1/Var(Xj))`，其中求和是对所有`j`从1到`n`进行的。该公式表明，每个资产的最优权重与其方差成反比，并由所有资产的逆方差之和进行归一化。分母被称为n个变量中的第(n-1)个基本对称多项式。本质上，为了最小化方差，应将更多的资金配置给波动性较低的资产。

---

## 5. 野兽的本性：夏尔·勒布伦的人兽混合体 (1806)

**原文标题**: The Nature of the Beast: Charles Le Brun's Human-Animal Hybrids (1806)

**原文链接**: [https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/](https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/)

野兽的本性：夏尔·勒布伦的人兽混合体（1806）

---

## 6. TCP，互联网的基石

**原文标题**: TCP, the workhorse of the internet

**原文链接**: [https://cefboud.com/posts/tcp-deep-dive-internals/](https://cefboud.com/posts/tcp-deep-dive-internals/)

本文阐述了TCP（传输控制协议）作为互联网“主力军”的重要性，它能够在底层网络不可靠的情况下实现可靠的数据传输。TCP在传输层运行，通过处理重传、校验和及其他可靠性机制，使开发者免受丢包、损坏、重复和重排序等问题的困扰。

本文重点介绍了流量控制，它可以防止接收方缓冲区溢出，以及拥塞控制，它可以防止网络崩溃。文中展示了一个用C语言编写的基本TCP服务器，用于回显客户端输入，以及一个使用TCP的简单HTTP服务器。

本文深入探讨了TCP段的结构，解释了关键字段，如源/目标端口、序列号和确认号（用于可靠性）以及标志位（SYN、ACK、FIN、RST用于连接管理）。序列号和确认号对于按顺序重组数据包至关重要。这些标志位用于创建、维护和关闭TCP连接。最后，校验和确保了数据完整性，窗口大小是流量控制的主要方法。

本文最后强调了互联网的卓越可靠性，这得益于致力于其开发和持续改进的个人。

---

## 7. Trellis AI (YC W24) 招聘：简化获取救生疗法的途径

**原文标题**: Trellis AI (YC W24) Is Hiring: Streamline access to life-saving therapies

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time)

Trellis AI (YC W24)，一家从斯坦福人工智能实验室分离出来的公司，正在招聘一名前置部署工程师，以帮助简化获取救生疗法的途径。 他们构建人工智能代理来自动化医疗保健文书工作，如文件录入、事先授权和申诉，影响遍及美国所有 50 个州的患者。该公司由 YC、General Catalyst 等机构投资。

该职位涉及为医疗保健决策设计和实施人工智能系统，构建 24/7 全天候人工智能同事，以及开发具有强大评估框架的生产级人工智能系统。 他们希望招聘具备全栈经验、精通 Python、Go 和 ML/NLP 库，具有数据库经验，以及积极主动、快速学习态度的人才。 具有云平台经验和开源贡献者优先。

Trellis 的目标是成为“医疗保健账单领域的 Stripe”，通过消除服务前文书工作，帮助供应商更快地治疗更多患者。 他们将治疗时间缩短 90% 以上，提高批准和报销率，并提高药物项目的绩效。 该公司在过去几个月中实现了 10 倍的收入增长，并声称在其细分市场中占据了相当大的市场份额。 团队由高成就者组成，并强调实际影响、客户参与和极致所有权。

---

## 8. 强大的单纯形 (2023)

**原文标题**: The Mighty Simplex (2023)

**原文链接**: [https://galileo-unbound.blog/2023/05/03/the-mighty-simplex/](https://galileo-unbound.blog/2023/05/03/the-mighty-simplex/)

强大的单纯形
探讨了单纯形在几何学、材料科学、机器学习和优化等各个领域的重要性和应用。文章强调了单纯形作为基本几何结构的简洁性、对称性和高效性。文章首先将d维单纯形定义为具有d+1个顶点的图形，并重点介绍了正单纯形（等边）及其性质。

随后，文章深入探讨了实际应用，展示了如何使用重心坐标表示合金成分、晶体学取向，以及使用复制方程建模生态系统动力学。文章还讨论了用于线性规划的Dantzig单纯形算法，该算法通过在多面体的顶点之间迭代移动来找到最优解。

最后，文章介绍了Nelder-Mead（变形虫）算法，这是一种非线性最小化技术，它使用动态调整的单纯形在超空间中“爬行”，寻找非线性目标函数的最小值。作者强调了单纯形在不同学科中的多功能性和重要性，将其描绘成一种用于表示、分析和优化的强大工具。

---

## 9. 人工智能世界时钟

**原文标题**: AI World Clocks

**原文链接**: [https://clocks.brianmoore.com/](https://clocks.brianmoore.com/)

AI世界时钟是一个网站，每分钟展示由九个不同AI模型生成的模拟时钟。该网站的创建者Brian Moore受到了Matthew Rayfield的启发。

每个AI模型都会收到提示：“创建显示${time}的模拟时钟的HTML/CSS。如果需要，可以包含数字（或数字符号），并设置CSS动画秒针。使其具有响应性并使用白色背景。仅返回HTML/CSS代码，不包含Markdown格式。” 它们被赋予2000个tokens来完成此请求。

该网站显示这些AI生成的时钟，每分钟更新一次。目前处于“加载中...”和“生成AI时钟中...”的状态，表明时钟正在积极生成。Brian Moore也可以在Instagram上找到。

---

## 10. 戏弄爬虫机器人

**原文标题**: Messing with scraper bots

**原文链接**: [https://herman.bearblog.dev/messing-with-bots/](https://herman.bearblog.dev/messing-with-bots/)

对抗恶意爬虫：一项实验报告

---

## 11. 绑带轨道

**原文标题**: Strap Rail

**原文链接**: [https://www.construction-physics.com/p/strap-rail](https://www.construction-physics.com/p/strap-rail)

本文探讨了带状铁轨的历史，这是一种早期在美国曾短暂流行的铁路技术。与英国昂贵的实心铁轨不同，美国采用了带状铁轨：一种固定在木材上的薄铁板。这种设计大大减少了铁的使用，使得在资金匮乏、铁资源有限且人口稀少的美国，建设铁路的成本显著降低。到1840年，带状铁轨占美国3000英里铁路的三分之二。

然而，最初的成本节省带来了长期的弊端。带状铁轨由于潮湿、昆虫和霉菌而迅速腐烂，导致高昂的维护成本。此外，铁条经常卷曲，导致脱轨。因此，带状铁轨的受欢迎程度下降。纽约州于1847年禁止将其用于公共铁路，强制转换为铁轨。

虽然带状铁轨在1860年左右基本被淘汰，但由于其重量较轻，它在马拉街车和一些私人工业铁路中继续使用，直到电动街车和更强大的铁路系统出现。文章最后强调，技术发展是如何受到问题解决努力和特定环境制约因素相互作用的影响的，带状铁轨在美国早期的兴衰就是一个例证。文章还提到了另一种更便宜但更短暂的技术——用于伐木的杆道。

---

## 12. 单手键盘

**原文标题**: One Handed Keyboard

**原文链接**: [https://github.com/htx-studio/One-Handed-Keyboard](https://github.com/htx-studio/One-Handed-Keyboard)

本文档介绍了一款单手机械键盘的开源设计，该设计是为了响应一位女儿失去右手功能的用户的需求而开发的。该键盘旨在提高计算机可访问性和打字速度。

主要特点：

*   **单手设计：** 允许单手操作。
*   **集成轨迹球：** 包含一个轨迹球用于鼠标控制，最大限度地减少手在键盘和鼠标之间的移动。
*   **QMK固件：** 使用QMK固件进行自定义和高级功能。
*   **开源硬件和软件：** 硬件设计（KiCad EDA格式的PCB布局）、固件源代码和3D模型均可在GitHub和Gitee上找到。
*   **多种键盘选项：** 该项目包括左手和右手版本的的设计，包括较大的热插拔配置和较小的焊接配置。
*   **详细的制造指南：** 提供PCB制造、3D打印和组装的详细说明，包括大型和小型键盘变体的BOM清单。
*   **使用STM32G431CBU6微控制器。**

该存储库包含文档、固件、硬件设计文件和3D模型。该指南涵盖PCB规格、打印材料、硬件组件（螺钉、轴承、开关）和组装说明，包括如何刷写固件。特别考虑了柔性电缆连接器的方向、ALPS开关安装和小子PCB的连接。该项目强调易于定制和修改。

---

## 13. 设计一门语言 (2017)

**原文标题**: Designing a Language (2017)

**原文链接**: [https://cs.lmu.edu/~ray/notes/languagedesignnotes/](https://cs.lmu.edu/~ray/notes/languagedesignnotes/)

本文旨在为有兴趣设计自有编程语言的个人提供指导。它强调语言设计是一个迭代过程，包括定义需求、设计语言、实现语言，然后根据反馈进行测试和改进。

作者强调了拥有扎实的编程范式、语言概念（如作用域、类型、并发）基础，以及熟悉现有语言（如Python、Smalltalk、Javascript等）的重要性。研究各种语言有助于理解不同的设计选择及其权衡。建议通过经典论文、在线课程和语言比较等资源进行准备。

本文在开始设计之前，列出了一系列需要考虑的事项，包括确定目标受众、确定语言的用途（实用、深奥等）、选择范式（OO、函数式等）以及选择并发模型。

文章的很大一部分集中在选择起始功能集上。它提出了一系列关于函数、类型系统、表达式、控制流和并发支持的详细问题，以帮助指导功能选择过程。

最后，文章介绍了抽象语法树（AST）的概念，作为一种结构化组织语言功能的方法，并以JavaScript的EsTree规范为例。作者强调了定义AST节点类型、它们的关系和属性的重要性。 文章建议学习和研究缺乏理解的领域。

---

## 14. 使用游戏协议的流式AI智能体桌面

**原文标题**: Streaming AI agent desktops with gaming protocols

**原文链接**: [https://blog.helix.ml/p/technical-deep-dive-on-streaming](https://blog.helix.ml/p/technical-deep-dive-on-streaming)

Luke Marsden 和 Chris Sterry 详细介绍了他们使用 Moonlight 游戏协议将 AI 代理桌面流式传输给 Helix Code 用户的历程。他们需要一种低延迟、GPU 加速的桌面流式传输解决方案，以便向浏览器和原生客户端提供服务，从而使用户能够与在容器化 Linux 环境中运行的 AI 代理进行交互。

虽然 Moonlight 提供了速度、效率和网络弹性，但它最初是为单人游戏设计的，这给他们的多用户代理访问需求带来了挑战。 最初的解决方法是“应用模式”，其中包含一个“启动会话”的技巧，以便在用户连接之前启动代理，但这会导致单用户会话，并可能导致多个冲突的代理实例。

解决方案以 Wolf 的“大厅模式”的形式出现，该模式专为多人游戏而设计。这允许多个客户端连接到同一个代理会话，无需启动技巧，并实现真正的多用户交互。目前，他们正在迁移到大厅模式，这解决了核心的架构问题。

尽管仍存在一些错误，例如输入缩放问题和某些客户端上的视频损坏，但长期愿景包括多个用户查看同一个代理、原生客户端支持以及具有预配置分辨率的正确移动客户端流式传输。

这篇文章强调了流式传输协议对于可视化 AI 代理的重要性，并强调即使协议在技术上可行，其底层假设也可能带来工程挑战。作者还强调了开源贡献和社区支持在解决独特技术问题方面的价值。

---

## 15. 立法者想禁用VPN。

**原文标题**: Lawmakers want to ban VPNs

**原文链接**: [https://www.eff.org/deeplinks/2025/11/lawmakers-want-ban-vpns-and-they-have-no-idea-what-theyre-doing](https://www.eff.org/deeplinks/2025/11/lawmakers-want-ban-vpns-and-they-have-no-idea-what-theyre-doing)

本文反对威斯康星州拟议的以及其他地区（密歇根州、英国）类似的法律，这些法律以保护儿童在线安全为名，旨在禁止或阻止VPN（虚拟专用网络）。核心问题在于，这些旨在强制执行访问某些内容时的年龄验证的法律，被视为侵犯隐私且技术上不可行。

文章解释说，VPN可以掩盖用户的位置，使网站无法确定用户的实际位置（例如，在威斯康星州内），从而无法遵守针对特定地区的VPN禁令。立法者试图扩大“对未成年人有害”的定义，以审查各种教育材料、性教育资源、艺术，甚至获奖文学作品。潜在的后果是可怕的：网站可能会阻止全球VPN用户，以避免在一个州的法律问题，从而损害合法用户。

文章强调，VPN对于企业、学生、弱势群体（家庭暴力幸存者、记者、LGBTQ+人士）以及任何寻求隐私的人来说至关重要。阻止VPN将迫使用户在没有隐私保护的情况下向网站提交个人信息（身份证、生物识别数据），从而造成数据泄露风险。文章还指出，精通技术的个人将规避VPN禁令，从而使这些法律失效。

最终，作者认为，禁止VPN不是解决在线安全问题的方案，而是对数字隐私和自由的攻击。它鼓励人们，特别是威斯康星州的人们，联系他们的代表并反对拟议的立法。

---

## 16. 谷歌新模型在自动手写识别方面接近完美。

**原文标题**: A new Google model is nearly perfect on automated handwriting recognition

**原文链接**: [https://generativehistory.substack.com/p/has-google-quietly-solved-two-of](https://generativehistory.substack.com/p/has-google-quietly-solved-two-of)

无法访问文章链接。

---

## 17. 如何忍受烦人的事情

**原文标题**: How to tolerate annoying things

**原文链接**: [https://psyche.co/guides/how-to-respond-to-annoying-things-with-greater-ease](https://psyche.co/guides/how-to-respond-to-annoying-things-with-greater-ease)

这篇文章《如何容忍烦人事》可能侧重于情绪调节策略，以管理由烦人情况或人物引起的沮丧和烦躁。根据标题和语境，其核心概念是提高人们处理压力情况的能力，避免升级为负面情绪状态。

提及“情绪调节”表明文章很可能涵盖有意识地影响和管理自身情绪体验的技巧。这可能包括识别触发因素、识别烦躁的早期迹象以及运用应对机制。

包含“呼吸与情绪之间的相互作用——以及如何获取它，翠西·马克斯博士的视频”表明文章重点关注生理反应（特别是呼吸）与情绪状态之间的联系。马克斯博士的视频很可能解释了如何利用受控的呼吸技巧来调节神经系统，并减少烦躁、焦虑或愤怒的感觉。这意味着文章提倡使用呼吸法作为一种情绪调节工具，以应对烦人的刺激。

总而言之，这篇文章很可能提倡情绪调节技巧，特别是强调呼吸法的力量，以帮助人们更好地容忍烦人事，并以健康和建设性的方式管理自己的情绪反应。它可能解释了呼吸和情绪之间的联系，并教授实用的呼吸练习以缓解烦躁情绪。

---

## 18. Linux平台的非官方Microsoft Teams客户端

**原文标题**: Unofficial Microsoft Teams client for Linux

**原文链接**: [https://github.com/IsmaelMartinez/teams-for-linux](https://github.com/IsmaelMartinez/teams-for-linux)

本文介绍了一个非官方的 Linux 版 Microsoft Teams 客户端，它提供了比网页版更优化的 Linux 集成原生桌面体验。主要功能包括系统通知、系统托盘集成、自定义背景、屏幕共享和多账户配置文件。文章强调这是一个独立项目，并指出其局限性源于底层的 Teams Web 应用。

可以通过专门的 Debian/Ubuntu 和 RHEL/Fedora 包存储库轻松安装，并提供了详细说明。用户还可以从 GitHub Releases 下载发行包 (AppImage、deb、rpm、snap、tar.gz)。文档涵盖安装、配置、故障排除、多配置文件和自定义背景。

文章强调了安全性的重要性，指出由于需要完整的 Teams 功能，Electron 的内置沙盒功能已被禁用。它建议使用系统级沙盒选项，如 Flatpak、Snap、Firejail、AppArmor 或 SELinux，以提高隔离性。

该项目欢迎贡献，提供了一个 Matrix 聊天链接以提供支持，并鼓励报告错误。它在 GPL-3.0 许可下运行。最后，文章还提到了该项目的历史，并注明了所用图标的来源。

---

## 19. 文字能否超越字面意义，传递更多信息？(2022)

**原文标题**: Can text be made to sound more than just its words? (2022)

**原文链接**: [https://arxiv.org/abs/2202.10631](https://arxiv.org/abs/2202.10631)

帕塔卡和科斯塔的文章《隐藏的哭喊、低语和尖叫：文字能否超越其字面意义发出更多声音？》探讨了将副语言特征（响度、音高、持续时间）的视觉表现形式嵌入文本中，以增强字幕并提高对所说内容的理解，使其超越字面意义。作者认为，通常以中性方式呈现语音的字幕会丢失通过声音韵律传达的重要细微差别。

他们的模型将声音韵律映射到排版的视觉维度：响度对应字体粗细，音高对应基线偏移，持续时间对应字母间距。这创造了“语音调节排版”。一项评估测试了参与者是否能将这种视觉增强的文本与其原始音频相匹配，并在相似的备选项中呈现。

该研究涉及117名参与者，他们在识别正确音频方面的平均准确率为65%，无论文本调制是以静态还是动画形式呈现。参与者的评论表明，对于排版如何反映语音，存在不同的心理模型。该论文得出结论：基于声音韵律对排版进行视觉调制可以提高对口语内容的理解，为丰富字幕并使其更准确地表达语音提供了一种潜在的方法。该文章发表在《IEEE情感计算汇刊》上。

---

## 20. Go语言十六岁了

**原文标题**: Go's Sweet 16

**原文链接**: [https://go.dev/blog/16years](https://go.dev/blog/16years)

Go 团队 16 周年博文回顾了过去一年 Go 语言及其生态系统的发展，特别是 Go 1.24 和 1.25 版本的发布。主要改进包括用于简化并发代码测试的 `testing/synctest` 包，对 `testing` 包中基准测试和清理的增强，用于改进容器中并行性的容器感知调度，以及用于生产系统诊断的新飞行记录器。

安全性仍然是重点，Go 原生密码学软件包的安全审计和 CAVP 认证取得了积极成果，为符合 FIPS 140-3 标准铺平了道路。`os.Root` API 增强了文件系统访问安全性。

底层改进包括重新设计的 map 实现以获得更好的性能，以及实验性的 Green Tea 垃圾回收器，有望显著降低垃圾回收开销。

除了语言本身，该团队还强调了 Go 的开发平台，持续发布 gopls 语言服务器，包括新的分析器、重构工具和一个用于 AI 助手的实验性模型上下文协议 (MCP) 服务器。引入了自动代码现代化工具，以帮助开发人员采用较新的习惯用法。

Go 在 AI 领域的参与受到关注，与 Anthropic 合作发布了官方 Go SDK for MCP，以及 Google 的 Go 代理开发工具包 (ADK)。

展望未来，该团队正专注于提高开发人员的生产力、Green Tea 垃圾回收器的全面可用性、SIMD 硬件支持，以及改进 `encoding/json` 和 `net/http` 等核心库。他们还计划扩展 Go 的开发流程并更深入地让贡献者社区参与进来。

---

## 21. Löb与Möb：Haskell中的循环 (2013)

**原文标题**: Löb and Möb: Loops in Haskell (2013)

**原文链接**: [https://github.com/quchen/articles/blob/master/loeb-moeb.md](https://github.com/quchen/articles/blob/master/loeb-moeb.md)

2013年Haskell文章《Löb and Möb：Haskell中的循环》探讨了在Haskell中实现递归和类循环行为的技术，特别关注如何处理递归调用需要访问整体计算结果的情况。它介绍了`löb`和`mü`（通常写作`m`）组合子，这些组合子为这些问题提供了优雅的解决方案，而无需诉诸显式可变引用或其他可能不太纯粹的函数式方法。

其核心思想围绕着“系结”的概念——本质上是创建一个循环依赖，即一个函数在完全计算完成之前需要它自身的结果。`löb`允许你定义一个接收自身结果作为输入的函数，从而实现依赖于最终结果的复杂计算。`mü`与`löb`密切相关，但在处理递归数据结构时通常更有用，因为每个元素可能依赖于结构的其他部分计算出的信息。

这篇文章可能深入探讨了这些组合子的实现，演示了它们的推导并强调了它们的属性。它可能提出了实际示例，演示了如何在诸如定义循环数据结构、实现不动点计算或解析图中的依赖关系等场景中使用`löb`和`mü`。

本质上，这篇文章倡导使用`löb`和`mü`作为强大的工具，在Haskell的纯函数式约束内表达递归和循环计算，与命令式循环结构相比，提供了一种更具声明性和优雅性的方法。

---

## 22. 《绝世女特务》25周年，你仍然无法合法购买它

**原文标题**: 'No One Lives Forever' turns 25 and you still can't buy it legitimately

**原文链接**: [https://www.techdirt.com/2025/11/13/no-one-lives-forever-turns-25-you-still-cant-buy-it-legitimately/](https://www.techdirt.com/2025/11/13/no-one-lives-forever-turns-25-you-still-cant-buy-it-legitimately/)

文章重点介绍了备受好评的间谍题材第一人称射击游戏“绝命保镖”25周年纪念。尽管该游戏广受欢迎并充满怀旧之情，但仍然无法通过合法途径购买或下载。这种不幸的局面是由于多年来困扰该游戏复杂的许可问题和所有权纠纷造成的，从而阻止了它的重新发布或数字发行。作者表达了一种惆怅的希望，也许有一天，这款游戏会再次上市，即使要等到博比·邦尼拉与纽约大都会队那份臭名昭著的延期合同到期。整体基调是对游戏遗产的庆祝以及对其持续无法获得的沮丧。

---

## 23. SSL配置生成器

**原文标题**: SSL Configuration Generator

**原文链接**: [https://ssl-config.mozilla.org/](https://ssl-config.mozilla.org/)

本文介绍“Mozilla SSL配置生成器”，该工具旨在帮助用户为其Web服务器创建最佳SSL配置。该工具需要JavaScript才能运行，旨在简化通常复杂的安全HTTPS连接设置过程。

其核心目的是根据用户输入生成定制的SSL配置，确保安全性、兼容性和性能之间的平衡。通过使用该生成器，用户可以避免常见的配置错误，这些错误可能会使他们的网站暴露于漏洞之下。它可能提供选择特定服务器软件（如Apache、Nginx等）和预期用例（如现代、中级或旧客户端支持）的选项。

本质上，Mozilla SSL配置生成器对于寻求实施强大而安全的HTTPS配置的Web管理员和开发人员来说是一项宝贵的资源，它可以节省他们的时间和精力，同时最大限度地降低配置错误的风险。“复制”一词表明该工具会输出一个配置文件或文本，用户可以将该文件或文本复制并粘贴到其服务器的配置中。

---

## 24. HipKittens：快速且激烈的AMD内核

**原文标题**: HipKittens: Fast and furious AMD kernels

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-11-09-hk](https://hazyresearch.stanford.edu/blog/2025-11-09-hk)

本文介绍HipKittens (HK)，一种新型C++嵌入式编程原语集合，旨在简化和加速AMD内核的AI开发。作者强调，由于AMD软件的不成熟，AMD GPU的理论峰值性能与当前AI工作负载中所达到的性能之间存在显著差距。现有的解决方案（如AITER、PyTorch和编译器（Triton、Mojo、TileLang））通常性能不佳或缺乏必要的功能，这迫使人们依赖手工优化的汇编代码，阻碍了广泛采用。

HipKittens旨在通过提供带有明确倾向的原语来弥合这一差距，使开发人员无需借助底层汇编即可编写高性能的AMD内核。作者借鉴了他们之前为NVIDIA开发的ThunderKittens，并证明基于tile的抽象可以推广到不同的GPU架构。

核心发现表明，虽然tile抽象具有通用性，但底层的内存访问模式和调度策略需要针对特定架构。HK实现了显著的性能提升，在注意力前向传递、GEMM和注意力反向传递中，优于AMD自己的基线，包括手工优化的AITER内核。作者强调，HK内核具有可读性和可修改性。

文章最后倡导多芯片AI，强调开放硬件的重要性，并使AMD GPU更容易被AI社区所接受。他们认为HipKittens是朝着在AI中充分发挥多样化硬件潜力的重要一步。

---

## 25. E Ink Spectra 6 与 ChLCD 的颜色对比

**原文标题**: Color Comparison Between E Ink's Spectra 6 and ChLCD

**原文链接**: [https://iris-opt.com/en/blog/eink-spectra6-vs-chlcd/](https://iris-opt.com/en/blog/eink-spectra6-vs-chlcd/)

本文比较了两种彩色电子纸技术：E Ink 的 Spectra 6 和 IRIS Optronics 的 ChLCD，重点关注它们的色彩表现和对各种应用的适用性。

Spectra 6 采用 ACeP 技术，利用包含红、蓝、黄、白墨水颗粒的微杯混合生成六种标准颜色。另一方面，ChLCD 使用三层液晶 (RGB) 来再现超过 1600 万种颜色，提供更丰富、更准确的色域。

比较表明，Spectra 6 在处理青色和品红色等特定颜色时存在困难，表现出不太准确的渐变和较低的饱和度。相比之下，ChLCD 在整个色谱中都表现出卓越的色彩准确度、更精细的细节和更高的饱和度，使其更适合于人像、食物图像和时尚广告等对色彩保真度至关重要的应用。

除了颜色之外，文章还强调了 ChLCD 凭借其液晶技术而具有的更宽的工作温度范围（-20°C 至 70°C），使其成为应对极端天气条件的户外显示器的理想选择。与 Spectra 6（约 15 秒）相比，它还拥有显着更快的刷新率（1-2 秒）。此外，ChLCD 利用现有的 LCD 制造工艺，有望以具有成本效益的方式生产大尺寸显示器，甚至可达到 100 英寸屏幕。

总之，本文将 ChLCD 定位为在色彩准确性、户外耐用性、刷新率和大规模生产方面都更胜一筹的技术，使其成为各种应用更具吸引力的选择。

---

## 26. 午餐阿姨，赞美你们！

**原文标题**: All praise to the lunch ladies

**原文链接**: [https://bittersoutherner.com/issue-no-12/all-praise-to-the-lunch-ladies](https://bittersoutherner.com/issue-no-12/all-praise-to-the-lunch-ladies)

珍妮弗·贾斯特斯的作品《一切赞美都献给午餐阿姨们》是一篇衷心的致敬之作，献给学校食堂工作人员以及她们在孩子们生活中所扮演的关键角色，她的祖母比尤拉·卡尔佩珀就是佐治亚州农村的一位午餐阿姨。作者回忆起她的祖母致力于喂饱孩子们的奉献精神，甚至变通规则以确保没有孩子饿肚子，并强调了学校食品计划的挑战和复杂性。

文章探讨了学校营养的更广阔领域，包括政府资助、法规和政治辩论的影响。它展示了现代“午餐英雄”，如斯蒂芬妮·迪拉德，她倡导更健康、本地采购的膳食；以及丽莎·塞伯-加兰，她创造性地应对资金削减，以提供营养丰富的选择。文章强调了在预算限制下平衡从零开始烹饪的斗争，以及联邦对农场到学校计划资金令人沮丧的削减，最终影响了学生获得新鲜、健康食品的机会。

文章强调了普遍免费膳食的重要性，例如加利福尼亚州等一些州提供的免费膳食，以消除污名，并确保所有儿童都能获得营养食品。文章还提到了艾丽丝·沃特斯和丹·朱斯蒂等倡导者，他们正在努力彻底改变学校食品。文章强调了食堂作为“学校中心”的作用，并认可午餐阿姨们的奉献精神和足智多谋，她们不知疲倦地为学生提供必要的营养和关怀。

---

## 27. 使用 Sqlorm 融合 SQL 和 Python

**原文标题**: Blending SQL and Python with Sqlorm

**原文链接**: [https://hyperflask.dev/blog/2025/11/11/blending-sql-and-python-with-sqlorm/](https://hyperflask.dev/blog/2025/11/11/blending-sql-and-python-with-sqlorm/)

SQLORM：一个注重直接SQL、对象脱离会话且专注于纯对象映射的Python ORM库。

主要特性和设计选择包括：

*   **以SQL为中心的方法：** 鼓励在Python函数中使用docstrings编写原始SQL查询，用于模板化和参数转义。
*   **分离对象：** 允许从一个数据库获取数据并插入到另一个数据库，使用相同的对象实例，避免会话依附。
*   **活动记录模式：** 使用`Model`类进行基本的CRUD操作，减少样板代码。
*   **上下文管理连接：** 利用上下文管理器，通过`Engine`类处理数据库连接和事务。
*   **动态列：** 支持使用Python注解定义模型列，用于类型检查和DDL生成，但不需要预先声明。
*   **读/写分离：** 促进诸如从副本数据库读取数据并写入主数据库的模式，因为模型不绑定到特定的引擎。

SQLORM提供了用于构建SQL语句、获取相关行和从查询结果中填充对象的实用程序。 该库旨在尽可能贴近DB-API原则，并包含用于处理关系、延迟加载和列类型的功能。它还提供Flask集成和全面的文档。

---

## 28. Estes AstroCam 110 的历史与应用

**原文标题**: History and use of the Estes AstroCam 110

**原文链接**: [https://www.dembrudders.com/history-and-use-of-the-estes-astrocam-110.html](https://www.dembrudders.com/history-and-use-of-the-estes-astrocam-110.html)

这篇2Modeler.com上的文章详细介绍了埃斯特斯AstroCam 110型火箭相机的历史和使用方法。文章首先将现代数码摄影的便利性与胶片摄影的复杂性进行对比，为理解AstroCam 110所提供的进步奠定了基础。

然后，文章回顾了埃斯特斯火箭相机的历史，从使用需要暗房处理的单张圆形黑白胶片的Camroc相机开始。Camroc之后是Cineroc电影摄影机。文章强调了从飞行火箭上拍摄高质量图像所涉及的工程挑战，突出了需要快速快门速度和高速胶片来对抗模糊。

1979年推出的AstroCam 110代表了一次重大升级。它使用了柯达的110胶卷盒，实现了彩色摄影，并简化了火箭爱好者的胶卷处理过程。文章指出，通过采用这种常见的胶卷格式，埃斯特斯最终可以停止其胶卷销售和冲洗服务。然而，与Camroc相比，较小的胶卷格式导致图像质量明显下降。

文章还描述了相机的操作、胶卷推进的机械原理，以及在降落伞弹出期间触发快门的方法。最后，作者分享了使用AstroCam 110的个人经历以及对改装的尝试，例如“Lookdown-AstroCam”，它可以将火箭本身拍摄到照片中。

---

## 29. 规范驱动开发：瀑布模型的反击

**原文标题**: Spec-Driven Development: The Waterfall Strikes Back

**原文链接**: [https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)

弗朗索瓦·扎尼诺托的文章《规格驱动开发：瀑布模型的反击》批判了人工智能编码助手时代新兴的规格驱动开发（SDD）实践。SDD旨在通过在编码前以Markdown格式生成详细规范来提供结构，但扎尼诺托认为这是一种倒退，让人联想到瀑布模型繁重的文档工作。

他强调了SDD的缺点，包括上下文盲视（遗漏现有函数）、“Markdown疯狂症”（过于冗长的规范）、系统官僚主义（过度的设计流程）、伪敏捷实践、双倍的代码审查工作、虚假的安全感（代理并非总是遵循规范）以及在大型现有代码库中的收益递减。

扎尼诺托认为SDD试图将开发人员从过程中移除，错误地认为他们只是执行者。他认为软件开发是非确定性的，并且SDD，就像无代码工具一样，仍然需要专门的专业知识。

他提倡使用“自然语言开发”的敏捷方法，即开发人员将复杂的需求分解为简单的需求，让编码代理基于自然语言指令迭代构建。这种受“精益创业”启发的的的方法侧重于通过简单的实验测试有风险的假设，从而实现快速开发和适应。扎尼诺托总结说，SDD错失了利用人工智能和自然语言赋能开发人员的机会，阻碍了他们的潜力，就像将内燃机限制在机车上一样。他建议专注于更丰富的视觉交互，以进一步改进编码代理。

---

## 30. Kagi失误 – 搜索结果出错

**原文标题**: Kagi Bloopers – Search Results Gone Wrong

**原文链接**: [https://help.kagi.com/kagi/bloopers/](https://help.kagi.com/kagi/bloopers/)

Kagi爆笑失误：搜寻结果出错集锦

---

## 31. 用RP2040驱动TFEL：逐步卸载CPU (2021)

**原文标题**: Driving TFEL with RP2040: Offloading the CPU step by step (2021)

**原文链接**: [https://www.zephray.me/post/rpi_pico_driving_el/](https://www.zephray.me/post/rpi_pico_driving_el/)

本文详细介绍了一个项目，作者探索使用RP2040微控制器驱动Planar EL640.480-AM TFEL显示屏，旨在减轻CPU的负担。TFEL面板使用单色STN LCD接口，这给寻找合适的控制器带来了挑战。

作者首先采用完全位操作的方式，直接控制GPIO引脚，但发现这会消耗所有CPU周期并且速度很慢。接下来，数据传输被卸载到RP2040的PIO（可编程输入/输出），使用两个状态机来处理双扫描显示。确保这些状态机之间的同步对于无故障图像至关重要。

下一步涉及使用DMA（直接内存访问）向PIO提供数据，进一步降低CPU负载。最初，实现了阻塞DMA传输，但CPU仍然需要等待DMA完成。为了释放CPU时间，引入了DMA中断。创建了一个中断处理程序来生成HVSync信号并启动下一行的DMA。这会将CPU使用率降低到大约48%。

最后，作者通过利用PIO生成HVsync信号，以及使用PIO的向下计数器功能，进一步推进了项目，完全将CPU从定时循环中移除。PIO处理数据输出和同步信号生成，仅在帧结束时中断CPU，从而最大限度地提高CPU的可用性以执行其他任务。

---

## 32. 无泄漏，无问题——通过ROP链绕过ASLR以获取RCE

**原文标题**: No Leak, No Problem – Bypassing ASLR with a ROP Chain to Gain RCE

**原文链接**: [https://modzero.com/en/blog/no-leak-no-problem/](https://modzero.com/en/blog/no-leak-no-problem/)

本文详细介绍了如何寻找和利用INSTAR IN-8401 2K+ IP摄像头中基于栈的缓冲区溢出漏洞，以实现未经身份验证的远程代码执行(RCE)。

作者首先使用UART接口提取摄像头的固件，并通过U-Boot引导加载程序和一个`init=/bin/sh`技巧绕过初始登录提示。这允许访问文件系统进行分析。

摄像头的Web界面使用`lighttpd` Web服务器，该服务器将请求转发到`fcgi_server`和`ipc_server`。作者专注于对这两个二进制文件进行漏洞研究，结合使用模糊测试、静态分析和动态分析以及gdb调试设置。

该漏洞在`fcgi_server`的基本身份验证处理程序中被发现。自定义的Base64解码函数将解码结果复制到固定大小（516字节）的栈缓冲区中。通过在HTTP基本身份验证的用户名字段中发送过长的Base64编码字符串，作者触发了栈缓冲区溢出，覆盖了返回地址。程序崩溃，PC寄存器包含“AAAA”（0x41414140）。作者计划在下一篇文章中开发ROP链以绕过ASLR并实现RCE。

---

## 33. Claude开发者平台上的结构化输出

**原文标题**: Structured outputs on the Claude Developer Platform

**原文链接**: [https://www.claude.com/blog/structured-outputs-on-the-claude-developer-platform](https://www.claude.com/blog/structured-outputs-on-the-claude-developer-platform)

Claude开发者平台上的结构化输出

---

## 34. 随机字体 – 探索随机性的排印实验 [pdf]

**原文标题**: Random Font – a typographic experiment exploring randomness [pdf]

**原文链接**: [https://www.ilcovile.it/scritti/COVILE_834_Reprint_Random_Font.pdf](https://www.ilcovile.it/scritti/COVILE_834_Reprint_Random_Font.pdf)

该文档似乎是PDF文件的原始内容，特别是名为“随机字体 – 探索随机性的排版实验”的文件。由于其为原始PDF格式，文本经过大量编码，包含大量二进制数据。这使得从所提供的文本中直接生成人类可读的摘要变得不可能。

然而，根据标题，我们可以推断出关于该文章的以下信息：

*   **主题：** 文章可能讨论一项实验，涉及使用随机元素创建或修改的字体。
*   **焦点：** 焦点可能在于设计过程、结果字体的美学以及在排版中使用随机性的意义。
*   **潜在主题：** 文章 *可能* 涵盖：
    *   在字体中生成随机性的技术方法（例如，编程、算法）。
    *   随机字体的外观和在不同上下文中的表现示例。
    *   实验背后的艺术或概念推理。
    *   对字体的可读性和可用性的讨论。

在没有PDF文本的解码版本的情况下，无法生成更详细和准确的摘要。

---

## 35. macOS 平台的 Swift 版 Winamp 克隆

**原文标题**: Winamp clone in Swift for macOS

**原文链接**: [https://github.com/mgreenwood1001/winamp](https://github.com/mgreenwood1001/winamp)

本文介绍了“Winamp macOS”，这是一款原生 macOS 应用程序，旨在为现代 Mac 重现经典的 Winamp 体验。它支持 MP3 和 FLAC 播放，具有受 Winamp 启发的用户界面，并通过 M3U 文件提供播放列表管理。

主要功能包括完整的播放控制、频谱分析仪、10 段均衡器、带有拖放支持的文件浏览器以及多种示波器可视化效果。值得注意的是，它集成了 Milkdrop，并提供全屏模式和歌词叠加功能。

该应用程序需要 macOS 13.0 或更高版本以及 Xcode 15.0 或更高版本才能构建。本文提供了使用 Xcode、Swift Package Manager 和 Shell 脚本进行构建的说明。

该项目采用 MIT 许可证，鼓励用户自由使用和修改代码。开发者还提供了一个“Buy Me a Coffee”链接，供希望支持项目开发的人使用。总而言之，Winamp macOS 是对经典音频播放器的现代重塑，为 macOS 用户提供怀旧体验和当代功能。

---

## 36. 爱德华·伯汀斯基的警告

**原文标题**: Edward Burtynsky's Warning

**原文链接**: [https://www.theatlantic.com/magazine/2025/12/edward-burtynsky-photographs/684604/](https://www.theatlantic.com/magazine/2025/12/edward-burtynsky-photographs/684604/)

爱德华·伯汀斯基是一位以拍摄记录人类活动影响下的“改变地貌”而闻名的加拿大摄影师。1999年，他拍摄了加利福尼亚州一个巨大的轮胎处理场。数百万轮胎堆积如山的景象既超现实又有一种奇异的美感。然而，在他访问后不久，该地点发生火灾，持续燃烧了一个月，融化的油料可能污染周围的土壤和水源，造成了严重的环境危害。

伯汀斯基的作品虽然有时在视觉上引人注目，但往往是对人类活动对环境造成后果的警告。自2012年以来，他还抽出时间拍摄原始景观，以激发人们的希望。他最近参观了澳大利亚的鲨鱼湾，这是一个以叠层石而闻名的联合国教科文组织世界遗产地，叠层石是由微生物形成的古老岩石结构。这些叠层石被认为是已知最古老的化石，比包括轮胎在内的许多人类发明还要古老。伯汀斯基从空中拍摄了鲨鱼湾，以确保他没有干扰这片未受破坏的景观。本文重点介绍了伯汀斯基对比鲜明的摄影主题，揭示了人类的破坏性影响和未受破坏的自然环境的持久美丽。

---

## 37. IncusOS

**原文标题**: IncusOS

**原文链接**: [https://discuss.linuxcontainers.org/t/announcing-incusos/25139](https://discuss.linuxcontainers.org/t/announcing-incusos/25139)

IncusOS，一款专为运行 Incus 而设计的现代、不可变操作系统，经过一年的开发现已正式发布。它基于最小化的 Debian 13 构建，具有原子 A/B 更新、UEFI 安全启动和 TPM 2.0 以增强安全性。它使用 Linux 内核、ZFS 和 Incus 的 Zabbly 构建版本以获得最新的稳定版本。该系统完全通过使用 TLS 客户端证书或 OIDC 身份验证的 Incus API 进行管理，提供了一个没有 shell 访问权限的锁定环境。

IncusOS 旨在用于裸机服务器，但可以在虚拟机中进行测试。通过在线镜像定制器创建为特定行为和受信任证书量身定制的自定义镜像，因为没有交互式安装。

开发团队计划每周进行稳定构建，包括 Linux 内核错误修复、Incus 和 Debian 错误修复。未来的功能包括 Linstor 支持、额外的系统服务（如 Netbird）以及通过 Web UI 实现的完整 Incus 部署和管理系统，从而无需 TLS 客户端证书。最终目标是自动化整个 Incus 堆栈的部署以及推荐的支持服务。

团队鼓励用户测试 IncusOS，尤其是在能够运行 Windows 11 的硬件上，请牢记安全启动和 TPM 2.0 要求。有一个专门的论坛类别和一个 GitHub 存储库用于提交错误和功能请求。

---

## 38. Aurora RDS 中的竞争条件

**原文标题**: A race condition in Aurora RDS

**原文链接**: [https://hightouch.com/blog/uncovering-a-race-condition-in-aurora-rds](https://hightouch.com/blog/uncovering-a-race-condition-in-aurora-rds)

Hightouch在尝试升级Amazon Aurora RDS数据库基础设施，以应对10月20日AWS中断后增加的事件处理负载时，遇到了竞态条件缺陷。

升级计划包括增加一个只读副本，升级一个现有副本，启动故障转移到升级后的副本，升级原始写入器，以及移除临时副本。然而，故障转移反复失败，几乎立即回滚。

调查显示问题在于：在故障转移期间，Aurora短暂地允许原始写入器和晋升的副本同时处理写入操作。共享存储层拒绝了这些并发的写入操作，导致两个实例崩溃。这表明在降级原始写入器和晋升副本之间存在竞态条件。

为了验证该假设，Hightouch缩减了写入服务，并成功执行了故障转移。他们将问题升级到AWS，AWS确认该缺陷与降级过程中的一个内部信号问题有关，导致旧的写入器在尝试故障转移后保持不变。

缓解措施包括在有意故障转移之前暂停写入器。Hightouch成功地扩大了集群规模，并实施了对意外写入器角色变更的监控。

主要经验包括：在迁移过程中为意外状态做好准备的重要性，用于检测问题的强大可观测性的价值，隔离分布式系统中组件影响的好处，以及分期环境在复制生产级别缺陷方面的局限性。

---

## 39. 欧盟聊天监控的变相回归

**原文标题**: The disguised return of EU Chat Control

**原文链接**: [https://reclaimthenet.org/the-disguised-return-of-the-eus-private-message-scanning-plot](https://reclaimthenet.org/the-disguised-return-of-the-eus-private-message-scanning-plot)

好的，以下是基于标题和我对该主题的了解，对ReclaimTheNet.org文章“欧盟聊天控制的伪装回归”的总结：

该文章可能讨论了欧盟为实施允许扫描私人通信的措施而做出的努力，这些措施通常被描述为打击儿童性虐待材料（CSAM）的一种方式。“伪装回归”可能指的是这样一种情况：在之前的“聊天控制”提案因隐私问题面临重大阻力和批评后，欧盟试图以不同的形式或通过修改后的立法引入类似的措施。

核心论点可能是，这些新的提案，尽管可能以不同的方式呈现，仍然对用户隐私和言论自由构成威胁。这篇文章可能认为，欧盟打击CSAM的目标是合理的，但大规模监视私人通信的拟议方法是不成比例的、无效的，并且容易被滥用。它可能会讨论对误报、对合法通信的潜在寒蝉效应以及加密的侵蚀的担忧。

此外，该文章可能强调，即使有了保障措施和监督机制，滥用这些权力的风险仍然很大。它可能呼吁采取替代解决方案，重点关注有针对性的调查和预防，而不是大规模监控。它也可能暗示，欧盟试图规避或忽视隐私倡导者和专家先前提出的关于大规模扫描私人信息可能造成的危害的担忧。标题表明该文章对欧盟的做法持批评态度，并认为这是先前被拒绝的想法的重现，存在问题。

---

## 40. 异步互斥锁

**原文标题**: Async Mutexes

**原文链接**: [https://matklad.github.io/2025/11/04/on-async-mutexes.html](https://matklad.github.io/2025/11/04/on-async-mutexes.html)

本文探讨了作者在并发和互斥锁方面的语言设计理念中潜在的矛盾。作者最初认为，单线程并发编程消除了对互斥锁的需求，因为数据竞争是不可能的。然而，作者意识到互斥是一种逻辑属性，即使在单线程环境中也需要显式注解，以防止因`.await`调用位置不当而导致意外的非原子操作。这倾向于像 Kotlin 这样的显式 async/await 模型。

作者随后强调了自己在 TigerBeetle 上的工作中所存在的矛盾。TigerBeetle 是一个依赖于单线程提供的隐式互斥的系统。TigerBeetle 利用回调函数来响应 IO 事件，从而改变共享状态。围绕所有访问共享状态的回调函数强制执行显式锁定（互斥锁），就像在 Compaction 过程中那样，很可能导致围绕事件循环中访问的所有状态的单一全局锁——实际上是重新实现了隐式锁定行为。

作者最后观察到，构建并发程序有两种截然不同的范式。Async/await 系统通常假定一种 CSP（通信顺序进程）风格，其中线程大多是独立的，并且共享少量数据。然而，TigerBeetle 采用了一种状态机/Actor 风格，专注于大量共享状态，这些状态响应 IO 事件以离散的步骤演变。此外，在 TigerBeetle 中使用手动回调函数降低了在关键部分意外引入并发的风险，因为新的并发需要具有严格状态断言的显式延续函数。

---

## 41. 锰是莱姆病的双刃剑

**原文标题**: Manganese is Lyme disease's double-edge sword

**原文链接**: [https://news.northwestern.edu/stories/2025/11/manganese-is-lyme-diseases-double-edge-sword](https://news.northwestern.edu/stories/2025/11/manganese-is-lyme-diseases-double-edge-sword)

本文呈现两个看似无关的信息：

1.  **标题暗示锰在莱姆病中扮演着复杂且可能有害的角色。** 它暗示锰可能提供一些益处，但同时也带来风险或负面后果。 理解这种双重性对于有效治疗莱姆病至关重要。 这种“双刃剑”效应的具体细节将在文章中详细阐述。

2.  **文章提到西北大学的毕业典礼定于2026年，具体时间是2025年10月28日。** 这似乎与莱姆病和锰无关，表明这篇文章可能是不同新闻项目的组合，或者是一篇重点不明确的文章。

在没有全文的情况下，无法确定这两点之间是否存在关联（如果有）。 毕业日期可能只是附加在关于锰和莱姆病标题上的无关信息。

---

## 42. Show HN: Tiny Diffusion – 从零开始的字符级文本扩散模型

**原文标题**: Show HN: Tiny Diffusion – A character-level text diffusion model from scratch

**原文链接**: [https://github.com/nathan-barry/tiny-diffusion](https://github.com/nathan-barry/tiny-diffusion)

Tiny Diffusion：基于nanoGPT架构从零构建的字符级文本扩散模型，用于文本生成。 它在Tiny Shakespeare数据集上进行训练，仅包含1070万个参数，占用空间小，便于本地实验。 该仓库提供预训练权重和脚本，用于训练、文本生成和扩散过程可视化。

主要特性和要点：

*   **字符级生成：** 基于单个字符而非单词进行操作。
*   **小参数量：** 能够在配置一般的硬件上进行训练和推理。
*   **预训练模型：** 开箱即用，可直接用于文本生成。
*   **训练脚本：** 用户可以在相同数据上重新训练模型。
*   **可视化工具：** 提供动画以了解扩散过程，包括一个受“生命游戏”启发的实验。
*   **易于设置：** 使用 `uv` 进行依赖管理，并提供简单的命令用于训练、采样和可视化。
*   **MIT许可证：** 采用开放许可，允许修改和分发。

---

## 43. 持续架构：为变革而设计的十年

**原文标题**: Continuous Architecture: A decade of designing for change

**原文链接**: [https://continuousarchitecture.com/2025/11/04/a-decade-of-ca/](https://continuousarchitecture.com/2025/11/04/a-decade-of-ca/)

本文回顾了持续架构(CA)提出十年以来的发展，强调了它在当今快节奏技术环境中的持久 relevance。CA优先考虑价值的持续流动，并适应软件交付不断变化的需求，从全面的建模转向持续的决策流。

作者强调，由于敏捷和DevOps实践以及微服务等独立组件的兴起，架构的重要性日益增加。这需要从单一架构方法转变为分布式架构工作。

本文的核心内容回顾了CA的六项原则：

1.  **架构产品：** 关注长期价值和客户需求，而不是特定于项目的解决方案。
2.  **关注质量属性：** 优先考虑诸如安全性和可扩展性等非功能性需求。
3.  **延迟设计决策：** 基于事实而非假设做出决策，但避免过度推迟。
4.  **为变更而架构：** 拥抱松散耦合的小组件，如微服务。
5.  **为构建、测试、部署和运营而架构：** 考虑整个交付流程，而不仅仅是开发。
6.  **对团队组织进行建模：** 应用康威定律，使团队结构与系统设计保持一致。

作者总结说，这些原则仍然有效且具有基础性，并已成功地经历了云计算、DevOps和微服务的兴起。当前的挑战在于在各个组织中始终如一地实施这些原则，以最大限度地发挥持续架构的优势。

---

## 44. Ucs-Detect
统一码检测

**原文标题**: Ucs-Detect

**原文链接**: [https://ucs-detect.readthedocs.io/intro.html](https://ucs-detect.readthedocs.io/intro.html)

`ucs-detect` 是一个命令行工具，可自动测试终端模拟器的 Unicode 支持级别，重点关注宽字符、Emoji ZWJ 序列、Emoji VS-16 序列以及受支持语言中的零宽度/组合字符。它使用查询光标位置终端序列，并将终端的输出与 `wcwidth` 库规范进行比较，以检测差异。

该工具可识别终端模拟器和库之间 Unicode 支持级别不同而可能产生的问题，这些问题会导致东亚语言和复杂字符组合的显示问题。

`ucs-detect` 允许用户保存测试结果的详细 YAML 报告。它还包含一个大型的《世界人权宣言》(UDHR) 翻译数据集，用于测试特定于语言的脚本渲染。各种终端的测试结果可在存储库中找到，但鼓励用户提交 pull request 以更新这些结果。

本文提供了使用说明，包括如何安装、运行测试、更新现有测试数据以及提交新的终端结果。此外，它还概述了如何使用 `--stop-at-error` 参数通过交互式调试来分析问题。该工具不断发展，功能也在不断改进（例如 Emoji 和 DEC 私有模式检测），并随着社区的贡献持续发展。

---

## 45. Minisforum 将整个 Arm 家庭实验室塞进 MS-R1

**原文标题**: Minisforum Stuffs Entire Arm Homelab in the MS-R1

**原文链接**: [https://www.jeffgeerling.com/blog/2025/minisforum-stuffs-entire-arm-homelab-ms-r1](https://www.jeffgeerling.com/blog/2025/minisforum-stuffs-entire-arm-homelab-ms-r1)

Minisforum MS-R1：搭载Cix CD8180 Arm SoC，旨在与苹果M1 Mac mini及其他迷你PC竞争，但结果喜忧参半。它拥有12核Arm CPU、Mali G720 iGPU、PCIe插槽、NVMe存储、WiFi 6E和丰富的端口。虽然硬件令人印象深刻且系统安静，但其性能不稳定，能效较差，尤其是在空闲时。

iGPU性能尚可，但Vulkan支持不足。CPU性能基准测试与较早的Arm开发套件相当，但逊于M1。一个重要问题是由于指令集不匹配导致的DGEMM性能不佳，这影响了内存访问速度。

MS-R1的亮点在于其64GB内存，使其适合本地AI，但内存速度会影响性能。凭借双10Gbps NIC和快速WiFi 6E，网络性能出色。通过PCIe插槽升级独立显卡可提高AI和游戏性能，但驱动程序兼容性可能存在问题。

BIOS功能丰富，但仍带有“Beta”标签。该机器支持Proxmox虚拟化，尽管是非官方的。虽然MS-R1因其扩展选项而具有家庭实验室潜力，但其500-600美元的价格使其与英特尔、AMD或苹果M系列Mac相比，价值主张值得怀疑。评测总结认为，虽然MS-R1是撼动Arm桌面市场的一次有趣尝试，但它需要固件修复、驱动程序主线化以及更好的Windows支持才能真正具有竞争力。

---

## 46. GEN-0 / 具身基础模型：随物理交互扩展

**原文标题**: GEN-0 / Embodied Foundation Models That Scale with Physical Interaction

**原文链接**: [https://generalistai.com/blog/nov-04-2025-GEN-0](https://generalistai.com/blog/nov-04-2025-GEN-0)

本文介绍了GEN-0，一种新型具身基础模型，旨在直接基于原始物理交互数据进行多模态训练，以推动机器人技术发展。GEN-0的目标是通过在机器人领域扩展多模态模型训练，从而建立类似于大型语言模型（LLM）的机器人智能扩展定律。

GEN-0的关键特性包括和谐推理，使模型能够无缝地思考和行动，以及一种旨在捕捉人类水平的反射和物理常识的架构。这些模型已经在各种机器人上进行了测试，展示了跨具身能力。一项重要的成就是创建了一个大规模的机器人数据集，目前包含27万小时的真实世界操作数据，并且还在迅速增长。

该研究强调了几个重要的发现：GEN-0模型表现出强大的扩展定律，即更多的预训练数据和计算能力可以预测性地提高下游性能。在70亿参数时观察到一个相变，更大的模型表现出持续的改进，而较小的模型则表现出僵化（权重无法吸收新信息）。预训练数据的质量和多样性至关重要，影响着模型的特性和下游任务的性能。可以通过A/B测试来优化数据混合的预训练效果。

---

## 47. Awk技术笔记 (2023)

**原文标题**: Awk Technical Notes (2023)

**原文链接**: [https://maximullaris.com/awk_tech_notes.html](https://maximullaris.com/awk_tech_notes.html)

Volodymyr Gubarkov 的这篇文章深入探讨了 AWK 有趣的技术细节，重点介绍了它的设计选择和解析复杂性。一个关键特性是 AWK 缺乏垃圾回收 (GC)，这影响了诸如无法从函数返回数组之类的设计决策。相反，为了确定性的内存管理，数组在函数范围内传递和修改。文章指出，默认情况下所有变量都是全局的，局部变量通过函数参数定义，这种设计选择虽然令 Brian Kernighan 后悔，但效果很好。

文章还讨论了 AWK 的“自动激活”特性，允许基于变量的使用隐式声明变量。然后，文章深入探讨了解析细节，揭示了 `$` 是一个适用于表达式的一元运算符，甚至可以在赋值语句的左侧。文章还解释了函数调用的不寻常行为，由于 AWK 的字符串连接规则，在用户自定义函数之前的括号前不允许有空格。

文章阐明了内置函数如何被视为语法的一部分，从而导致对用户自定义函数或变量以其命名施加限制。文章最后讨论了 ERE 与 DIV 词法分析的歧义以及解析正则表达式的解决方案。总的来说，这篇文章说明了 AWK 的设计是一种简洁、高效的语言，针对单行代码进行了优化，这也导致了一些临时的语法和解析怪癖。

---

## 48. 贫穷与身无分文

**原文标题**: Being poor vs. being broke

**原文链接**: [https://blog.ctms.me/posts/2025-11-14-being-poor-or-being-broke/](https://blog.ctms.me/posts/2025-11-14-being-poor-or-being-broke/)

本文区分了“身无分文”和“贫穷”这两种状态，认为它们是本质上不同的经历，经常被那些没有经历过贫困的人所误解。“身无分文”是一种暂时的经济困难，资金紧张但基本需求仍能得到满足。然而，“贫穷”是一种永无止境的经济不稳定状态，即使是微小的挫折也会造成毁灭性的后果。

作者批判了向穷人提出的常见建议，认为这些建议是针对那些身无分文且有能力通过短期牺牲来改善自身处境的人。他们强调，穷人往往已经做出了这些牺牲，将每项资源都用到极限。

作者用汽车维修的例子说明了这两者之间的区别，解释说，一个身无分文的人可能会通过自己修理来省钱，而一个穷人可能缺乏购买零件所需的300美元。他们还驳斥了穷人懒惰或缺乏技能的观点，指出许多人被迫花费大量时间和精力来自己修理东西、从零开始做饭和利用有限的资源。

文章最后强调，对于那些难以获得食物等基本生活必需品的人来说，像“在家做饭”这样的建议是不足的，强调了“身无分文”的经历与“贫穷”这种无情的、无法逃避的现实之间的巨大鸿沟。

---

## 49. 线性代数解释了为何有些词语实际上无法翻译。

**原文标题**: Linear algebra explains why some words are effectively untranslatable

**原文链接**: [https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable](https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable)

马可·詹科蒂认为，不可译词的概念可以通过线性代数的视角来理解。他将用不同语言表达概念类比为线性代数中改变向量的基底。

他认为概念是我们脑海中的抽象客体，而词语则是用于在特定语言（即“基底”）中表达它们的“坐标”。正如向量的数值表示在基底改变时会发生变化一样，概念的语言表达在翻译成不同语言时也会发生变化。

詹科蒂认为，“不可译”的词语之所以会出现，是因为某些语言用单个词来表达的概念，在另一种语言中需要多个词才能准确表达。就像在线性代数中选择合适的基底可以简化计算一样，某些语言为特定概念提供了更简洁、更易于使用的“基向量”（词语）。

他指出了实际不可译性的两个关键原因：沟通成本和精确度。用许多词语解释一个复杂的概念既耗时，又增加了引入意外细微差别的风险。此外，一种语言中词语的有限数量限制了精确度，类似于计算机中有限的小数位数，迫使我们“量化”我们的概念。这种量化导致在翻译过程中细微差别的损失，使得完美的等价往往是不可能的。这个类比解释了为什么在实践中，有些词语实际上是不可译的。

---

## 50. 发布 HN: Tweeks (YC W25) – 浏览器扩展程序，让网页不再糟糕

**原文标题**: Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web

**原文链接**: [https://www.tweeks.io/onboarding](https://www.tweeks.io/onboarding)

Tweeks：一款让你“净化”网络的Chrome浏览器扩展程序，赋予用户更多在线体验的控制权。该扩展程序允许用户使用自然语言提示和预置脚本自定义网站，从而移除干扰、个性化信息流并实现自定义品牌和主题。

安装过程包括从Chrome网上应用店安装该扩展程序，然后按照设置引导进行操作。Tweeks提供一个“灵感库”，其中包含示例调整，用户安装扩展程序后只需单击一下即可添加。

主要功能包括：

*   **专注模式：** 移除 LinkedIn、X (Twitter) 和 YouTube 等平台上的侧边栏、热点和推荐等分散注意力的元素。
*   **信息流个性化：** 允许用户过滤和控制他们的社交媒体信息流，通过隐藏广告并按日期和互动过滤帖子。
*   **自定义品牌和主题：** 允许用户使用自定义主题重新设计网站，例如将 Google 变成 20 世纪 70 年代的命令行界面。

该扩展程序适用于任何网站，并提供预览模式，以便在实施前可视化更改。“发布 HN”帖子鼓励用户安装该扩展程序以解锁实时演示并完成设置。

---

## 51. 营业利润率

**原文标题**: Operating Margins

**原文链接**: [https://fi-le.net/margin/](https://fi-le.net/margin/)

运营利润率

本文《运营利润率》通过分析不同行业和国家的运营利润率，探讨影响公司盈利能力的因素。文章将运营利润率定义为公司收入除以营收，代表剩余现金占营收的百分比。

文章强调，高利润率通常与规模较大的公司相关，赋予它们定价权。文章根据利润率驱动因素将公司分为几类：“绝对垄断企业”（例如，收费公路、证券交易所、港口）受益于监管和有限的资源，从而实现较高的平均利润率。“准垄断企业”（例如，英伟达、万事达）由于资本密集度高而面临较高的进入壁垒。“怪异垄断企业”（例如，水泥、邮轮）通过削价竞争或建立强大的行业关系等策略来维持利润率。特许经营商和销售品牌商品的公司（例如，披萨、路威酩轩、饮料）表现出出人意料的强劲利润率。“良好单位经济效益”的公司（例如，膳食补充剂、工具制造商、银行）创造了相对于原材料成本而言的高价值。

一项跨国比较揭示了平均运营利润率的显著差异，这可能受到资源可用性、行业组合、会计准则以及风险投资支持的初创企业（例如，以色列的负平均值）的普及程度的影响。作者总结认为，理解运营利润率对于评估企业的健康状况和战略定位至关重要。

---

## 52. 雇佣小丑

**原文标题**: Hiring the Joker

**原文链接**: [https://quarter--mile.com/hiring-the-joker](https://quarter--mile.com/hiring-the-joker)

**推测性概要：**

鉴于标题“雇佣小丑”，文章可能探讨雇佣一个性格混乱、难以预测、且可能怀有恶意的个体（以小丑角色为代表）的*理论*影响和潜在危险。 这可能是一个警示故事、一个思想实验或一篇讽刺文章。

可能探讨的主题包括：

*   **风险评估：** 分析与雇佣一个缺乏道德底线或有不稳定历史的人相关的极端风险。
*   **公司文化：** 考虑一个混乱的个体可能对团队士气、生产力和整体工作环境造成的毁灭性影响。
*   **法律和伦理影响：** 讨论因雇用一个动机可疑且可能存在危险行为的人而可能产生的法律责任和伦理困境。
*   **管理挑战：** 考察管理或控制一个积极寻求扰乱秩序和制造混乱的人的难度，甚至是不可能性。
*   **讽刺：** 使用小丑的极端例子来突出当前招聘实践或工作场所动态中的缺陷。

提供的链接（首页、订阅、联系方式、写作俱乐部、问题）表明它是一个专注于写作的博客或网站的一部分，提供社区和可能的提示。 该文章可能旨在通过探索一个非常不寻常的招聘场景来引发思考，甚至带有一些幽默。

**重要提示：** 由于缺乏实际文章内容，这是一个高度推断的概要。 真实的文章可能完全不同。

---

## 53. Incus-OS：运行Incus作为虚拟机监控程序的不可变Linux操作系统

**原文标题**: Incus-OS: Immutable Linux OS to run Incus as a hypervisor

**原文链接**: [https://linuxcontainers.org/incus-os/](https://linuxcontainers.org/incus-os/)

IncusOS是一款不可变的Linux操作系统，专为运行Incus作为虚拟机管理程序而设计。它通过UEFI安全启动、TPM 2.0测量和全盘加密等功能，优先考虑安全性和可靠性。更新是原子性的，采用A/B分区方案，以便在出现问题时轻松回滚。该操作系统已锁定，仅通过经过身份验证的REST API进行管理，使其成为专注于Incus的基础设施的理想选择。

主要特性包括自动本地ZFS池、对各种存储技术的支持（光纤通道、NVME-over-TCP、iSCSI、集群LVM、Ceph）以及高级网络功能，如VLAN感知桥接、链路聚合、LLDP、企业代理支持、强大的NTP、远程日志记录、OVS/OVN支持和Tailscale集成。

IncusOS基于Debian 13构建，具有定制的Incus和内核版本，还可以托管运营中心和迁移管理器。它利用systemd进行镜像构建、更新和磁盘加密。提供两个更新通道：“stable”（每周更新）和“testing”（每日更新）。自动更新每6小时进行一次，为下次重启暂存操作系统更新，并执行短暂的API停机时间以应用应用程序更新。该项目在Github上以Apache 2.0许可开发，由mkosi配置文件和用于操作系统管理的Go代码组成。

---

## 54. 加沙碧聊——无需网络的通讯

**原文标题**: Bitchat for Gaza – messaging without internet

**原文链接**: [https://updates.techforpalestine.org/bitchat-for-gaza-messaging-without-internet/](https://updates.techforpalestine.org/bitchat-for-gaza-messaging-without-internet/)

Bitchat：一款专为加沙巴勒斯坦人设计的无网安全通讯应用

---

## 55. AGI幻想阻碍实际工程

**原文标题**: AGI fantasy is a blocker to actual engineering

**原文链接**: [https://www.tomwphillips.co.uk/2025/11/agi-fantasy-is-a-blocker-to-actual-engineering/](https://www.tomwphillips.co.uk/2025/11/agi-fantasy-is-a-blocker-to-actual-engineering/)

本文认为，硅谷，特别是与 OpenAI 相关的人物中普遍存在的对通用人工智能（AGI）的信仰，不利于人工智能开发中负责任和有效的工程实践。作者认为，“AGI 幻想”驱动了对日益庞大的语言模型的追求，导致了破坏环境和剥削性的实践。

文章重点介绍了埃隆·马斯克和伊利亚·苏茨克维等关键人物的心态，他们将 AGI 视为人类的救星或威胁。这种信念，加上对 GPT-2 等语言模型扩展成功的认识，为投入巨额资源建设由污染性能源驱动的大型数据中心提供了理由。作者批评了对“纯语言”假设的依赖，该假设认为 AGI 可以仅从语言训练中产生，从而导致不受控制的数据消耗和剥削性的劳动实践来管理模型输出。

此外，文章质疑了用于证明 AGI 开发合理的预期价值（EV）论证，声称所使用的价值和概率是主观的，并且忽略了直接的负外部性，例如环境破坏和工人剥削。作者倡导一种更务实的方法，敦促技术人员放弃 AGI 幻想，转而专注于开发针对特定问题的 AI 解决方案，使用更小、更高效的模型，并仔细考虑成本效益分析。核心论点是，追逐 AGI 梦想会蒙蔽研究人员对现实世界成本的认识，并阻止他们从事负责任和有效的工程实践。

---

## 56. 从零开始的 Zig GUI

**原文标题**: Zig GUI from Scratch

**原文链接**: [https://www.vogt.world/zig-gui-from-scratch-part-1/](https://www.vogt.world/zig-gui-from-scratch-part-1/)

作者在一系列计划文章的第一部分中，详细介绍了他们使用 Zig 从头开始构建跨平台桌面 GUI 应用程序的旅程。出于对挑战、学习和创造性编码的渴望，该项目优先考虑理解底层系统，而非使用现有框架的快速解决方案。

技术栈包括 Zig，因其新颖性和编译时计算能力；WebAssembly，用于 Web 目标，并为其他平台进行原生编译；OpenGL/WebGL，用于渲染；以及 SDL2，用于跨 Linux、macOS 和 Windows 的窗口管理。应用程序架构使用平台特定模块（app、platform、glade、js）的编译时导入来处理 Web 和原生环境之间的差异，特别是 WebAssembly 的限制。

一个关键方面是使用“鸭子类型模块”创建跨平台的一致 API，以确保代码可重用性。作者使用 `zig-js` 库来促进 Zig 和 JavaScript 之间的通信，特别是用于传递复杂类型，例如用于 WebGL 渲染的顶点数组。文章接着介绍了一个简单的“hello canvas color”示例，重点介绍了在原生 (macOS) 和 Web 环境中创建窗口和清除颜色缓冲区的初始步骤。

未来的改进包括更好地管理 WebGL 上下文方法、代码生成 OpenGL 绑定，以及简化 Web 和原生构建之间的开发工作流程。

---

## 57. 笔与锹：谢默斯·希尼诗选

**原文标题**: The Pen and the Spade: The Poems of Seamus Heaney

**原文链接**: [https://literaryreview.co.uk/the-pen-the-spade-2](https://literaryreview.co.uk/the-pen-the-spade-2)

钢笔与铁锹：谢默斯·希尼诗选——文章可能探讨谢默斯·希尼的诗歌，重点关注与二战期间英国遭受猛烈空袭的“闪电战”相关或引发“闪电战”联想的诗歌，如《闪电战歌谣》。

文章的中心主题可能分析希尼如何运用其诗歌声音（“钢笔”）来探索和诠释闪电战的经历和影响。它可能考察触及破坏、韧性、损失、恐惧以及面对逆境的人类精神等主题的具体诗歌。“铁锹”在标题中暗示着对希尼通过其诗歌挖掘的更深层历史和个人经历的调查。

文章也可能讨论希尼在描绘闪电战时的风格选择，例如他如何运用意象、隐喻和节奏来传达战争的气氛。它可能会探讨闪电战的历史背景，以及希尼的诗歌如何帮助我们理解这一时期，或许会突出与该事件相关的个人或家庭联系，这些联系可能会影响他的作品。最终，文章旨在阐明希尼如何通过其强大而富有表现力的语言，将闪电战这一历史事件转化为引人入胜的诗歌。

---

## 58. 回到平铺窗口管理器 – XMonad

**原文标题**: Moving Back to a Tiling WM – XMonad

**原文链接**: [https://wssite.vercel.app/blog/moving-back-to-a-tiling-wm-xmonad](https://wssite.vercel.app/blog/moving-back-to-a-tiling-wm-xmonad)

本文详细介绍了作者在使用 Gnome 一段时间后，回归使用平铺窗口管理器 XMonad 的经历。作者强调了 XMonad 的优势，特别是其在 Haskell 中的可配置性，从而实现了强类型和模块化的设置。文章概述了作者的 XMonad 配置，该配置组织成用于键绑定、布局、偏好设置、主题和 xmobar 的模块，使其易于移植。

配置的关键要素包括每个工作区的布局，它限制了每个工作区可用的布局，以及显示窗口标题的自定义顶栏。作者强调了 XMonad 键绑定中的类型安全，确保更少的错误。使用子映射进行键绑定可以创建带有描述的和弦，从而增强可发现性。xmobar 配置也用 Haskell 编写并包含在项目中，从而促进了完整的桌面环境。使用视觉图标来表示当前布局。

文章涵盖了使用 Haskell 包管理器 Stack 设置 XMonad 的过程，提供了安装脚本并解释了构建过程。最后，作者描述了用于常用应用程序（如终端、Kanboard、CalibreWeb 和 Anki）的暂存区的实现，从而可以快速访问和恢复任务。作者还提供了讨论页面的链接，以便进一步提问。

---

## 59. Magit 手册再次上线

**原文标题**: Magit manuals are available online again

**原文链接**: [https://github.com/magit/magit/issues/5472](https://github.com/magit/magit/issues/5472)

在线Magit手册（位于magit.vc和emacsair.me）暂时无法访问。用户“ador”于2025年11月4日提出了该问题（#5472），表示尽管Magit在其Emacs环境中运行正常，但无法访问Magit网站查看教程。该问题随后被关闭，意味着问题已解决，网站现在可以访问。文章还提到了Magit的GitHub仓库，强调其受欢迎程度，拥有6.9k个星标和842个Fork。

---

## 60. Xqerl – Erlang XQuery 3.1 处理器

**原文标题**: Xqerl – Erlang XQuery 3.1 Processor

**原文链接**: [https://zadean.github.io/xqerl/](https://zadean.github.io/xqerl/)

Xqerl是一个积极开发的Erlang XQuery 3.1处理器和XML数据库，旨在嵌入到Erlang/Elixir应用程序中或作为独立应用使用。它将XQuery代码编译为BEAM字节码，并利用REST通过用户定义的端点进行外部通信。虽然尚未稳定，但它通过了很高比例的XQuery和XPath测试用例。

主要功能包括序列化、高阶函数和XQuery Update Facility 3.0。值得注意的缺失包括模式识别、类型化数据功能和全文扩展。Xqerl优先考虑规范的符合性，并通过提前编译将XQuery代码转化为可扩展的Erlang应用程序。

要使用Xqerl，请使用`xqerl:compile(FileName)`编译XQuery模块，并使用`xqerl:run(ModuleAtom, ContextMap)`执行它们。数据分别使用`xqldb_dml:insert_doc`和`xqldb_dml:delete_doc`进行加载和删除。

构建使用`rebar3`完成。该项目欢迎以代码、文档、教程和问题报告的形式提供的贡献。请通过Twitter (@xqerl)或xqerl.slack.com工作区联系该项目。未来的开发包括查询重写阶段、基于成本的实现、将原子操作转移到Rust NIF以及添加索引。

---

## 61. Steam Machine
蒸汽机

**原文标题**: Steam Machine

**原文链接**: [https://store.steampowered.com/sale/steammachine](https://store.steampowered.com/sale/steammachine)

此页面似乎是Steam平台关于“Steam Machine”的着陆页或一个版块。内容突出了Steam的几个关键方面：

*   **核心功能：** 提供Steam商店、探索队列、愿望单、点数商店、新闻和统计数据的访问入口。

*   **社区功能：** 显著展示了社区论坛、创意工坊（可能是用户生成内容）、Steam市场和直播的链接。

*   **支持和信息：** 提供“关于”和“客服支持”版块的链接，表明Valve提供与其服务相关的信息和帮助，包括Steam Machine（如果它仍然是一个相关的产品）。

*   **账号管理：** 提供安装Steam和登录的选项。

*   **语言选择：** 提供全面的语言列表，允许用户以其首选语言浏览平台。 它还包括报告翻译问题的链接，表明Steam积极维护和改进其本地化。

总而言之，这是一个典型的Steam页面，提供访问平台各个部分的导航，从购买游戏和参与社区，到访问支持和管理账户设置，特定的标题表明可能专注于Steam Machine（尽管缺少关于该设备的更多细节表明该页面是一个通用的导航中心）。

---

## 62. 谷歌必须向德国比价平台支付4.65亿欧元赔偿金

**原文标题**: Google must pay German price comparison platform 465M euros in damages

**原文链接**: [https://www.reuters.com/legal/litigation/google-must-pay-german-price-comparison-platform-465-mln-euros-damages-court-2025-11-14/](https://www.reuters.com/legal/litigation/google-must-pay-german-price-comparison-platform-465-mln-euros-damages-court-2025-11-14/)

德国法院判决谷歌向比价网站PriceRunner赔偿4.65亿欧元（合5.085亿美元）。该诉讼源于谷歌涉嫌滥用市场支配地位，在搜索结果中不公平地偏袒自身购物服务，从而损害PriceRunner和其他竞争对手的利益。

法院赞同PriceRunner的观点，认定谷歌的做法违反了反垄断法。PriceRunner认为谷歌的行为导致其平台流量和收入大幅损失。此案与2017年欧盟委员会因类似的反竞争行为对谷歌处以24亿欧元罚款的裁决相似。

虽然谷歌表示打算对德国法院的判决提出上诉，但这项裁决进一步增加了这家科技巨头在处理搜索引擎内部竞争方面所面临的压力。PriceRunner的首席执行官表示，他们计划就谷歌的持续行为造成的损失寻求进一步赔偿。该案件凸显了大型科技公司在潜在的反垄断违规行为以及其市场力量对小型竞争对手的影响方面所面临的持续审查和法律挑战。

---

## 63. 我不再推荐 Grafana 了

**原文标题**: I can't recommend Grafana anymore

**原文链接**: [https://henrikgerdes.me/blog/2025-11-grafana-mess/](https://henrikgerdes.me/blog/2025-11-grafana-mess/)

本文详细描述了作者使用 Grafana 产品不断演变的经历，从早期的成功开始，到最终的沮丧和不愿推荐。最初，Grafana、Loki 和 Prometheus 非常适合一家小型公司的容器化环境，尤其是与资源密集型的 Elastic Stack 相比。

随着作者转向 Kubernetes 环境，对长期存储的需求促使其采用了 Mimir 和 Grafana Agent 进行远程写入。然而，Grafana 的快速变化成为一个反复出现的主题，包括过渡到 Grafana Agent Flow、Grafana OnCall 的引入和弃用、大量的 Helm chart 更新，以及导致仪表盘失效的 Angular 到 React 的迁移。

“一体化”解决方案 Grafana Alloy 的推出，最初令人充满希望，但与 kube-prometheus 社区的 Prometheus Operator 及其 CRD 等既定标准相比，它缺乏完整的功能对等性。更复杂的是，Mimir 3.0 引入了 Apache Kafka 作为依赖项。

作者的核心抱怨是，Grafana 不断加快的变革步伐和频繁的弃用带来了不稳定性和维护负担。他们认为，这种对创新的驱动是由 Grafana 内部的职业目标驱动的，与大多数公司所需的稳定、“无聊”的监控解决方案的需求不符。虽然承认 Grafana 产品在技术上的优点，但作者最终表示，由于不断的变动和日益增加的复杂性，他们无法再自信地推荐它们。他们现在渴望 OTEL 变得稳定，并提供更灵活的后端解决方案，以避免频繁的监控设置大修。

---

## 64. 我学习成为一个社交正常人的六个阶段

**原文标题**: My six stages of learning to be a socially normal person

**原文链接**: [https://sashachapin.substack.com/p/my-six-stages-of-learning-to-be-a](https://sashachapin.substack.com/p/my-six-stages-of-learning-to-be-a)

无法访问文章链接。

---

## 65. EDE：小型快速桌面环境 (2014)

**原文标题**: EDE: Small and Fast Desktop Environment (2014)

**原文链接**: [https://edeproject.org/](https://edeproject.org/)

EDE（Equinox桌面环境）是一个小型快速的桌面环境，旨在提供快速响应和轻量级的系统资源占用。它致力于为用户提供熟悉的外观和感觉。该环境兼容多种操作系统，包括Linux、BSD变种、Solaris、Minix、Zaurus，甚至XBox。文章引导用户下载EDE 2.1版本，或浏览旧版本。文章重点介绍了近期更新，包括已解决的Bugzilla问题和一篇名为“秋季清理”的博客文章。最后，文章提供了EDE网站各版块的导航链接，包括主页、新闻存档、关于、图库、Wiki以及一个报告错误的链接。

---

## 66. Mullvad VPN 出现，然后呢？（聊天监控卷土重来）

**原文标题**: Mullvad VPN present And Then? (Chat Control is back on the menu)

**原文链接**: [https://mullvad.net/en/blog/mullvad-vpn-present-and-then](https://mullvad.net/en/blog/mullvad-vpn-present-and-then)

Mullvad VPN 强调欧盟再度推动“聊天控制”，警告其可能导致大规模监控、AI扫描私人数据以及强制性消息认证。他们发布了一个名为“然后呢？”的视频系列，以阐述不受约束的监控带来的后果，并提醒人们该提案腐败的根源。

文章详细介绍了“聊天控制”的历史，从阿什顿·库彻的组织Thorn倡导扫描设备以查找儿童性虐待材料（CSAM）开始。欧盟专员伊娃·约翰逊随后提出了一项因违反欧盟法律和人权而受到广泛批评的提案。部长理事会法律服务部门、欧洲议会数据保护委员会、联合国人权理事会以及众多专家都提出了担忧，他们警告说这会导致大规模监控和自我审查。

文章揭示了Thorn、欧盟委员会和游说“聊天控制”的“儿童权利组织”之间的联系。文章还指责欧洲刑警组织想要无限访问数据，甚至包括未经筛选和无辜的材料。尽管欧洲议会投票反对该提案，但欧盟理事会仍在考虑该提案。欧盟委员会还启动了“走向黑暗”和“保护欧盟”倡议，旨在以打击有组织犯罪为幌子获取私人对话。

Mullvad VPN 敦促人们要求政治家提高透明度并保护隐私，警告说，如果“聊天控制”或类似提案获得通过，欧盟将面临全面大规模监控、安全威胁和零隐私的风险。文章强调，非欧洲情报机构也参与其中，并使用了最初由阿什顿·库彻和伊娃·约翰逊提出的论点。最终，欧盟隐私的未来取决于公众行动。

---

## 67. RegreSQL: Regression Testing for PostgreSQL Queries

**原文标题**: RegreSQL: Regression Testing for PostgreSQL Queries

**原文链接**: [https://boringsql.com/posts/regresql-testing-queries/](https://boringsql.com/posts/regresql-testing-queries/)

RegreSQL is a tool designed to bring PostgreSQL's robust regression testing methodology to application queries, aiming to catch both correctness bugs and performance regressions before they hit production. It addresses the common issue of SQL query testing being overlooked, with developers often relying on ORMs or integration tests that don't directly test SQL behavior and performance under schema changes or index modifications.

RegreSQL treats SQL queries as strings and uses regression testing: writing queries, providing input data, and verifying that future changes don't break expectations. Beyond basic correctness, it tracks performance baselines, detects query plan regressions like sequential scans, and enables experimentation with schema and query changes.

Key features include:

*   **Basic Regression Testing:** Validates query results against expected data.
*   **Performance Regression Testing:** Tracks query execution time and flags common bad patterns (e.g., sequential scans, nested loops).
*   **ORM Integration:** Catches performance issues in ORM-generated SQL using SQLAlchemy's event system.
*   **Test Data Management:** Provides a declarative YAML-based fixture system for creating consistent, reproducible test data, including features for realistic data generation at scale.

By using RegreSQL, developers can systematically test their SQL queries, improving code quality and preventing performance problems from reaching production environments.


---

## 68. Scientists Produce Powerhouse Pigment Behind Octopus Camouflage

**原文标题**: Scientists Produce Powerhouse Pigment Behind Octopus Camouflage

**原文链接**: [https://today.ucsd.edu/story/scientists-produce-powerhouse-pigment-behind-octopus-camouflage](https://today.ucsd.edu/story/scientists-produce-powerhouse-pigment-behind-octopus-camouflage)

生成摘要时出错

---

## 69. Nano Banana can be prompt engineered for nuanced AI image generation

**原文标题**: Nano Banana can be prompt engineered for nuanced AI image generation

**原文链接**: [https://minimaxir.com/2025/11/nano-banana-prompts/](https://minimaxir.com/2025/11/nano-banana-prompts/)

生成摘要时出错

---

## 70. Android developer verification: Early access starts

**原文标题**: Android developer verification: Early access starts

**原文链接**: [https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html](https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html)

生成摘要时出错

---

## 71. GNOME 50 completes the migration to Wayland, dropping X11 backend code

**原文标题**: GNOME 50 completes the migration to Wayland, dropping X11 backend code

**原文链接**: [https://linuxiac.com/gnome-50-ends-the-x11-era-after-decades/](https://linuxiac.com/gnome-50-ends-the-x11-era-after-decades/)

生成摘要时出错

---

## 72. Statistical Process Control According to W. Edwards Deming

**原文标题**: Statistical Process Control According to W. Edwards Deming

**原文链接**: [https://www.thomas-huehn.com/deming/](https://www.thomas-huehn.com/deming/)

生成摘要时出错

---

## 73. Germany to ban Huawei from future 6G network

**原文标题**: Germany to ban Huawei from future 6G network

**原文链接**: [https://www.bloomberg.com/news/articles/2025-11-13/germany-to-ban-huawei-from-future-6g-network-in-sovereignty-push](https://www.bloomberg.com/news/articles/2025-11-13/germany-to-ban-huawei-from-future-6g-network-in-sovereignty-push)

生成摘要时出错

---

## 74. Anthropic Rides an Artificial Wave

**原文标题**: Anthropic Rides an Artificial Wave

**原文链接**: [https://berryvilleiml.com/2025/11/14/houston-we-have-a-problem-anthropic-rides-an-artificial-wave/](https://berryvilleiml.com/2025/11/14/houston-we-have-a-problem-anthropic-rides-an-artificial-wave/)

生成摘要时出错

---

## 75. Reservoir: Smart electric water heater

**原文标题**: Reservoir: Smart electric water heater

**原文链接**: [https://www.reservoirhome.com/](https://www.reservoirhome.com/)

生成摘要时出错

---

## 76. Lua 5.5.0 (rc1) 已发布供测试

**原文标题**: Lua 5.5.0 (rc1) has been released for testing

**原文链接**: [https://www.lua.org/work/doc/readme.html#changes](https://www.lua.org/work/doc/readme.html#changes)

Lua 5.5.0 Release Candidate 1 is available for testing. Lua is a lightweight, embeddable scripting language developed at PUC-Rio, freely available under the MIT license.

The document covers installation, changes, licensing, and provides a reference manual. Lua is distributed in source form and needs to be built. Instructions are given for Unix-like systems using "make." The Makefile controls the build and install process, with customization options for platform, build, and features available. Lua can also be built on other systems, requiring manual project setup for the library, interpreter, and compiler.

Key changes in Lua 5.5 since Lua 5.4 include: declarations for global variables, read-only for-loop variables, decimal printing of floats, more levels for constructors, `table.create`, expanded `utf8.offset` return, external strings, new library functions, incremental major collections, compact arrays (60% less memory), dynamic loading of 'readline', static binaries (reuse of original memory), dump/undump reuses all strings, and auxiliary buffer reuses buffer.

Installation creates 'bin', 'include', 'lib', 'man', and 'share' directories. Customization is possible by editing Makefiles or `src/luaconf.h`. The license allows for commercial use without cost, requiring only copyright attribution.


---

## 77. Writerdeck.org

**原文标题**: Writerdeck.org

**原文链接**: [http://www.writerdeck.org/](http://www.writerdeck.org/)

生成摘要时出错

---

## 78. A structural regular expression engine for Rust

**原文标题**: A structural regular expression engine for Rust

**原文链接**: [https://www.sminez.dev/match-it-again-sam/](https://www.sminez.dev/match-it-again-sam/)

生成摘要时出错

---

## 79. Ohm Editor

**原文标题**: Ohm Editor

**原文链接**: [https://ohmjs.org/editor/](https://ohmjs.org/editor/)

生成摘要时出错

---

## 80. A Common Semiconductor Just Became a Superconductor

**原文标题**: A Common Semiconductor Just Became a Superconductor

**原文链接**: [https://www.sciencedaily.com/releases/2025/10/251030075105.htm](https://www.sciencedaily.com/releases/2025/10/251030075105.htm)

生成摘要时出错

---

## 81. Show HN: Encore – Type-safe back end framework that generates infra from code

**原文标题**: Show HN: Encore – Type-safe back end framework that generates infra from code

**原文链接**: [https://github.com/encoredev/encore](https://github.com/encoredev/encore)

生成摘要时出错

---

## 82. Google Releases CodeWiki

**原文标题**: Google Releases CodeWiki

**原文链接**: [https://codewiki.google/](https://codewiki.google/)

生成摘要时出错

---

## 83. Raycore: GPU accelerated and modular ray intersections

**原文标题**: Raycore: GPU accelerated and modular ray intersections

**原文链接**: [https://makie.org/website/blogposts/raycore/](https://makie.org/website/blogposts/raycore/)

生成摘要时出错

---

## 84. What happened with the CIA and The Paris Review?

**原文标题**: What happened with the CIA and The Paris Review?

**原文链接**: [https://www.theparisreview.org/blog/2025/11/11/what-really-happened-with-the-cia-and-the-paris-review-a-conversation-with-lance-richardson/](https://www.theparisreview.org/blog/2025/11/11/what-really-happened-with-the-cia-and-the-paris-review-a-conversation-with-lance-richardson/)

生成摘要时出错

---

## 85. VisiData – open-source spreadsheet for the terminal

**原文标题**: VisiData – open-source spreadsheet for the terminal

**原文链接**: [https://www.visidata.org/](https://www.visidata.org/)

生成摘要时出错

---

## 86. I think nobody wants AI in Firefox, Mozilla

**原文标题**: I think nobody wants AI in Firefox, Mozilla

**原文链接**: [https://manualdousuario.net/en/mozilla-firefox-window-ai/](https://manualdousuario.net/en/mozilla-firefox-window-ai/)

生成摘要时出错

---

## 87. Honda: 2 years of ml vs 1 month of prompting - heres what we learned

**原文标题**: Honda: 2 years of ml vs 1 month of prompting - heres what we learned

**原文链接**: [https://www.levs.fyi/blog/2-years-of-ml-vs-1-month-of-prompting/](https://www.levs.fyi/blog/2-years-of-ml-vs-1-month-of-prompting/)

生成摘要时出错

---

## 88. Tesla Releases FSD Crash Data That Appears More Honest

**原文标题**: Tesla Releases FSD Crash Data That Appears More Honest

**原文链接**: [https://www.forbes.com/sites/bradtempleton/2025/11/14/tesla-finally-releases-fsd-crash-data-that-appears-more-honest/](https://www.forbes.com/sites/bradtempleton/2025/11/14/tesla-finally-releases-fsd-crash-data-that-appears-more-honest/)

生成摘要时出错

---

## 89. Steam Frame

**原文标题**: Steam Frame

**原文链接**: [https://store.steampowered.com/sale/steamframe](https://store.steampowered.com/sale/steamframe)

生成摘要时出错

---

## 90. AMD GPUs Go Brrr

**原文标题**: AMD GPUs Go Brrr

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr](https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr)

生成摘要时出错

---

## 91. Genergo: Propellantless space-propulsion system

**原文标题**: Genergo: Propellantless space-propulsion system

**原文链接**: [https://www.satcom.digital/news/genergo-an-italian-company-builds-the-worlds-first-known-propellantless-space-propulsion-system-flight-tested-and-validated-on-orbit](https://www.satcom.digital/news/genergo-an-italian-company-builds-the-worlds-first-known-propellantless-space-propulsion-system-flight-tested-and-validated-on-orbit)

生成摘要时出错

---

## 92. Oracle hit hard in Wall Street's tech sell-off over its AI bet

**原文标题**: Oracle hit hard in Wall Street's tech sell-off over its AI bet

**原文链接**: [https://www.ft.com/content/583e9391-bdd0-433e-91e0-b1b93038d51e](https://www.ft.com/content/583e9391-bdd0-433e-91e0-b1b93038d51e)

生成摘要时出错

---

## 93. Meeting notes between Forgejo and the Dutch government via Git commits

**原文标题**: Meeting notes between Forgejo and the Dutch government via Git commits

**原文链接**: [https://codeberg.org/forgejo/sustainability/pulls/137/files](https://codeberg.org/forgejo/sustainability/pulls/137/files)

生成摘要时出错

---

## 94. How to Get a North Korea / Antarctica VPS

**原文标题**: How to Get a North Korea / Antarctica VPS

**原文链接**: [https://blog.lyc8503.net/en/post/asn-5-worldwide-servers/](https://blog.lyc8503.net/en/post/asn-5-worldwide-servers/)

生成摘要时出错

---

## 95. Checkout.com hacked, refuses ransom payment, donates to security labs

**原文标题**: Checkout.com hacked, refuses ransom payment, donates to security labs

**原文链接**: [https://www.checkout.com/blog/protecting-our-merchants-standing-up-to-extortion](https://www.checkout.com/blog/protecting-our-merchants-standing-up-to-extortion)

生成摘要时出错

---

## 96. Adding Customizable Frame Contrast to KDE Plasma

**原文标题**: Adding Customizable Frame Contrast to KDE Plasma

**原文链接**: [https://akselmo.dev/posts/frame-contrast-settings/](https://akselmo.dev/posts/frame-contrast-settings/)

生成摘要时出错

---

## 97. NATO Ended Russia's Estonian Air Incursions

**原文标题**: NATO Ended Russia's Estonian Air Incursions

**原文链接**: [https://themilitaryanalyst.com/2025/11/13/the-real-story-how-nato-ended-russias-estonian-air-incursions/](https://themilitaryanalyst.com/2025/11/13/the-real-story-how-nato-ended-russias-estonian-air-incursions/)

生成摘要时出错

---

## 98. AI note-taking startup Fireflies was really two guys typing notes by hand

**原文标题**: AI note-taking startup Fireflies was really two guys typing notes by hand

**原文链接**: [https://www.pcgamer.com/software/ai/usd1-billion-ai-company-co-founder-admits-that-its-usd100-a-month-transcription-service-was-originally-two-guys-surviving-on-pizza-and-typing-out-notes-by-hand/](https://www.pcgamer.com/software/ai/usd1-billion-ai-company-co-founder-admits-that-its-usd100-a-month-transcription-service-was-originally-two-guys-surviving-on-pizza-and-typing-out-notes-by-hand/)

生成摘要时出错

---

## 99. SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds

**原文标题**: SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds

**原文链接**: [https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)

生成摘要时出错

---

## 100. Nvidia is gearing up to sell servers instead of just GPUs and components

**原文标题**: Nvidia is gearing up to sell servers instead of just GPUs and components

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/jp-morgan-says-nvidia-is-gearing-up-to-sell-entire-ai-servers-instead-of-just-ai-gpus-and-componentry-jensens-master-plan-of-vertical-integration-will-boost-profits-purportedly-starting-with-vera-rubin](https://www.tomshardware.com/tech-industry/artificial-intelligence/jp-morgan-says-nvidia-is-gearing-up-to-sell-entire-ai-servers-instead-of-just-ai-gpus-and-componentry-jensens-master-plan-of-vertical-integration-will-boost-profits-purportedly-starting-with-vera-rubin)

生成摘要时出错

---

