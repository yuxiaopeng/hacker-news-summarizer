# Hacker News 热门文章摘要 (2025-06-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 让 TRAMP 嗡嗡作响

**原文标题**: Making TRAMP go Brrrr

**原文链接**: [https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./](https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./)

本文详细介绍了如何优化Emacs中的TRAMP (透明远程访问，多协议) 以实现更快的远程开发。TRAMP虽然强大，但由于网络延迟可能会很慢。

作者建议了几种配置调整来提高性能：

*   **基本设置：** 禁用锁，使用直接SCP进行文件传输，并禁止自动保存。
*   **内联与带外文件复制：** 增加`tramp-copy-size-limit`到2MB左右，因为即使在较慢的连接上，内联复制（使用压缩的、base64编码的文本）通常对较小的文件更快，从而抵消了建立新连接进行带外传输的开销。
*   **直接异步进程：** 启用`tramp-direct-async-process`可显著加速异步进程，从而提高像Magit这样的包的性能。
*   **修复远程编译：** 重新启用SSH连接共享，用于编译命令，因为它通常会禁用它。
*   **调试：** 使用内置的Emacs性能分析器和`debug-on-entry`在`tramp-send-command`上，以识别由特定包或命令引起的性能瓶颈。

文章随后重点介绍了优化Magit：

*   使用`magit-dispatch`和`magit-file-dispatch`以避免缓慢的状态缓冲区刷新。
*   考虑直接使用shell命令进行简单的Git操作。
*   禁用不必要的Magit功能，如自动还原、提交缓冲区中的diff、自动状态缓冲区刷新。

它还建议禁用TRAMP上的LSP (语言服务器协议)，因为它存在性能问题，并提供`lsp-bridge`作为替代方案（尽管未经测试）。

最后，作者介绍了一个`memoize-remote`函数来缓存频繁访问的远程信息，从而减少冗余的TRAMP调用。

作者打算进一步探索对TRAMP本身进行更重大的更改，以解决根本的性能限制。

---

## 2. 京都后院咖啡与爵士

**原文标题**: Backyard Coffee and Jazz in Kyoto

**原文链接**: [https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto](https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto)

无法访问文章链接。

---

## 3. Rocknix是一款用于掌上游戏设备且不可变的Linux发行版。

**原文标题**: Rocknix is an immutable Linux distribution for handheld gaming devices

**原文链接**: [https://rocknix.org/](https://rocknix.org/)

ROCKNIX 是一款为掌上游戏设备设计的不可变 Linux 发行版，专注于复古游戏模拟。由爱好者开发，旨在提供一个功能丰富且令人愉悦的操作系统，并采纳社区意见。

主要功能包括：集成网络游戏（本地和远程），游戏内触摸支持，电池续航和性能的精细控制，媒体播放支持（音乐和视频），蓝牙音频和控制器支持，HDMI 和 USB 音频/视频输出支持，通过 Syncthing 和 rclone 实现的设备间和云同步，VPN 支持（Wireguard、Tailscale、ZeroTier），以及内置的抓取和 RetroAchievements 支持。

ROCKNIX 社区主要通过 Discord 进行互动。该发行版基于在各自条款下获得许可的开源组件构建，其中一些组件仅供非商业用途。ROCKNIX 品牌以 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License 获得许可。ROCKNIX 团队的原创软件和脚本以 GNU GPL Version 2 获得许可。

该项目承认其依赖于更广泛的开源社区的贡献，特别是 CoreELEC 和 LibreELEC。

---

## 4. 我用我的终端

**原文标题**: I Use My Terminal

**原文链接**: [https://jyn.dev/how-i-use-my-terminal/](https://jyn.dev/how-i-use-my-terminal/)

这篇文章详细介绍了作者围绕 Tmux 构建的高度定制化终端工作流，使其能够高效地管理文件、代码并在它们之间导航，主要是在远程服务器上进行。由于对编辑器卡顿和快捷键冲突感到沮丧，他们构建了一个系统，可以直接在终端中模拟 IDE 的“Ctrl+单击打开文件”功能。

该工作流涉及使用 Tmux 搜索回滚中的文件名，突出显示它们，然后打开选定的文件。打开文件涉及多个步骤，包括利用 Tmux 在远程服务器上的新或现有 Neovim 实例中打开文件的脚本，处理文件名/行号解析，甚至默认使用自定义脚本（一个 Perl 脚本，默认使用 Neovim 打开）打开文本文件。

关键组件包括用于文件名搜索的 Tmux 配置、用于在默认应用程序或带有 Neovim 的新 Tmux 窗格中打开文件的 shell 脚本以及文件关联技巧。作者承认其设置的复杂性和脆弱性，并承认除非他们愿意投入时间来理解和调试它，否则它可能不适合其他人。

尽管存在一些怪癖，但作者发现该系统值得使用，理由是减少了编辑器延迟、更易于调试、一致的快捷键以及无需本地克隆即可处理远程文件的能力。虽然作者正在考虑切换到 Kitty 以改进终端仿真，但这篇文章最终认为终端功能强大且可编写脚本，从而实现令人惊讶的自定义级别。这篇文章还推荐了其他不太密集的选择（Fish + Zoxide + FZF、qf、e、vim --remote）来实现类似的结果。

---

## 5. 新的Linux udisks漏洞允许攻击者在主流Linux发行版上获取root权限

**原文标题**: New Linux udisks flaw lets attackers get root on major Linux distros

**原文链接**: [https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/](https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/)

本文详细介绍了影响主要Linux发行版的两个新发现的本地提权（LPE）漏洞。第一个漏洞(CVE-2025-6018)存在于openSUSE Leap 15和SUSE Linux Enterprise 15的PAM配置中，可能授予本地攻击者“allow_active”用户权限。第二个漏洞(CVE-2025-6019)存在于libblockdev中，允许“allow_active”用户通过udisks守护程序（大多数Linux系统上的默认服务）获得root权限。

安全公司Qualys发现了这两个漏洞，开发了概念验证的漏洞利用程序，并演示了使用CVE-2025-6019在Ubuntu、Debian、Fedora和openSUSE Leap 15上成功实现root权限提升。本文强调了udisks漏洞的严重性，因为它广泛存在，实际上使几乎所有Linux系统都容易受到攻击，即使获得“allow_active”权限需要额外的步骤。

强烈建议管理员立即应用PAM和libblockdev/udisks漏洞的可用补丁，以防止攻击者获得root访问权限，从而可能导致广泛的系统破坏。本文还指出Qualys在发现重大Linux安全漏洞方面的记录，并提到了其他最近的漏洞，如PwnKit、Looney Tunables、Sequoia和Baron Samedit。最后，文章呼吁使用自动化补丁管理解决方案。

---

## 6. 官员承认他们不知道伊朗铀储备的下落

**原文标题**: Officials Concede They Don't Know the Fate of Iran's Uranium Stockpile

**原文链接**: [https://www.nytimes.com/2025/06/22/us/politics/iran-uranium-stockpile-whereabouts.html](https://www.nytimes.com/2025/06/22/us/politics/iran-uranium-stockpile-whereabouts.html)

无法访问文章链接。

---

## 7. 如何从汇编中存储 Go 指针

**原文标题**: How to store Go pointers from assembly

**原文链接**: [https://mazzo.li/posts/go-asm-pointers.html](https://mazzo.li/posts/go-asm-pointers.html)

本文探讨了如何从汇编代码中正确存储 Go 指针，重点关注与 Go 垃圾回收器 (GC) 的交互。由于 Go 执行并发垃圾回收，它采用写屏障来跟踪指针存储并确保准确的内存管理。写屏障会在每个指针赋值中添加代码，以告知 GC 新的引用。

核心问题出现在从汇编写入内存时，因为 Go 编译器通常会自动处理写屏障的检测。本文重点介绍了一个涉及并发哈希表的场景，其中原子 128 位存储是在汇编中实现的，需要手动实现写屏障。

推荐的方法是使用 `runtime.gcWriteBarrier2` 来通知 GC 指针存储。但是，直接链接到 runtime 符号受到限制，以防止依赖问题。本文提供了一个使用 `//go:linkname` 和版本约束的解决方法，通过将未来的 Go 版本列入黑名单来访问 `gcWriteBarrier2` 和 `runtimeWriteBarrier`。

最后，本文解决了 Go 中分配对齐内存的相关问题（特别是 AVX 指令的 128 位对齐）。标准分配方法不能保证对齐，本文提出了一种巧妙但复杂的方法，涉及 `unsafe.Slice` 和多次分配尝试来实现所需的对齐。提供的代码尝试了不同的分配策略和偏移，以确保分配的内存是 16 字节对齐的。运行时根据 Go 的类型系统跟踪指针，而不是根据精确的来源，这使得这个技巧可行。

---

## 8. 美国宇航局的旅行者号在太阳系边缘发现3万-5万开尔文的“墙”

**原文标题**: NASA's Voyager Found a 30k-50k Kelvin "Wall" at the Edge of Solar System

**原文链接**: [https://www.iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-79454](https://www.iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-79454)

美国宇航局的旅行者探测器于1977年发射，旨在探索太阳系边缘和星际介质。它们已穿越日球层顶，即太阳磁场（日球层）与星际介质相遇的边界。该边界由太阳风形成，太阳风是来自太阳的带电粒子的持续流动，推挤着星际介质。平衡点，即日球层顶，导致太阳风向后折返，从而形成日球层的“尾巴”。

旅行者1号于2012年穿越日球层顶，旅行者2号随后于2018年穿越，两者穿越的距离不同，这支持了日球层顶是动态的，会随着太阳活动而膨胀和收缩的观点。虽然不是坚固的墙，但两个探测器都在这个边界测量到极高的温度，达到30,000-50,000开尔文（54,000-90,000华氏度），导致了“火墙”一词的出现。由于粒子密度低，最大限度地减少了热传递，探测器得以幸存。

旅行者号继续从日球层顶之外传输数据，提供了对星际介质的独特见解。一个令人惊讶的发现是，日球层顶之外的磁场与日球层内部的磁场平行，旅行者1号和2号都证实了这一发现。这些探测器代表了人类首次瞥见我们太阳系之外的空间。

---

## 9. 铁甲骑兵：黑海地区约公元1300年的中世纪奇幻角色扮演战争游戏

**原文标题**: Cataphract: Medieval-fantasy roleplaying wargame, in the Black-Sea C. 1300

**原文链接**: [https://samsorensen.blot.im/cataphracts-design-diary-1](https://samsorensen.blot.im/cataphracts-design-diary-1)

本文是“重骑兵”的首篇设计日志。“重骑兵”是一款异步的、通过帖子进行的、实时战争游戏，背景设定在 1300 年左右的伪黑海地区。作者的灵感来自军事历史学家布雷特·德弗罗的作品，特别是对经常被忽视的作战层面（后勤、通讯、行动）的关注，以及战略和战术。

“重骑兵”强调这些作战细节，实时追踪部队的移动、信使的旅行时间和信息延迟。规则集很简单，使用六边形和基本骰子投掷，但指挥结构很复杂。五个初始派系（诺万帝国、萨卡兹亚神圣教区、兹拉尼奇公国、第三瓦尔加王国和卡尔汗国）各自从一名指挥官开始，然后可以任命下属，从而创建一个分散的指挥网络。指挥官之间的沟通仅限于信使，除非他们实际共处一地。

游戏的一个关键要素是指挥官可获得的信息有限。他们只知道他们的侦察兵报告的内容以及通过信件到达的内容，从而营造出强大的“战争迷雾”。这会导致战略失误、协调失败和非理性决策。指挥官依赖于简单、可靠的计划，而不是复杂的演习，因为作战情报是最宝贵的资源。

尽管存在背叛的可能性，但指挥官往往忠于他们的上级，因为他们依赖方向和信息。联盟的失败往往不是因为故意的背叛，而是因为后勤问题和沟通中断。“重骑兵”的最终成功取决于协调、组织和态势感知，使其成为一种独特而具有挑战性的战争游戏体验。

---

## 10. 最小布尔公式

**原文标题**: Minimal Boolean Formulas

**原文链接**: [https://research.swtch.com/boolean](https://research.swtch.com/boolean)

本文详细介绍了确定表示五变量布尔函数所需的最小AND或OR运算符数量的计算工作。作者与Alex Healy共同发现，答案是28。

最初的方法是基于Floyd-Warshall所有对最短路径算法的蛮力方法，并将其调整为计算每个布尔函数的最小公式大小。这种方法计算成本很高，尤其是对于五个变量。作者使用伪代码解释了算法1。

为了提高效率，他们利用了布尔函数中的对称性，例如德摩根定律和输入置换/求反。通过识别具有相同复杂度的函数的等价类，他们可以减少存储和迭代的函数数量。这促成了算法2。

进一步的优化包括将搜索策略从“循环直到事物停止改变”更改为有条不紊的探索，按复杂性顺序构建函数（算法3和4）。这减少了仅考虑一次的函数对的迭代次数。

最后，在计算接近尾声时，他们切换到定向搜索。他们没有组合函数对，而是专注于特定的缺失函数，并探索使用已知函数创建它们的方法，从而大大加快了最后阶段。

这些优化的综合影响将计算时间从最初估计的800天缩短到更易于管理的20天。作者最终成功地确定了先前未知的五变量布尔函数所需的最小运算符数量。

---

## 11. RaptorCast：消息层设计

**原文标题**: RaptorCast: Designing a Messaging Layer

**原文链接**: [https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer](https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer)

RaptorCast是一种旨在高效且安全地在权益证明区块链中传播区块提议的解决方案，解决了性能、安全性和稳健性问题。它侧重于三个关键设计参数：数据传输协议、编码系统和广播策略。

RaptorCast选择UDP而非TCP以实现更快的数据传输，并使用R10编码系统（一种喷泉码，建立在Luby变换(LT)码之上并对其进行扩展）来解决UDP固有的不可靠性问题。R10通过发送额外的编码数据包来处理数据包丢失，允许接收者重建数据，而无需考虑哪些特定数据包到达。通过Merkle证明和数字签名添加符号级身份验证，以防止数据损坏。

广播策略采用结构化的两跳方法，为验证者分配特定的数据部分以重新广播到预定义的对等节点，从而提高带宽效率。每个UDP数据包都包含一个Merkle证明（100字节）、一个包含签名、版本、纪元、时间戳和区块提议元数据的头部（108字节），以及一个块头部（24字节）以及数据有效负载（1268字节）。这种结构化的方法增强了数据完整性，验证了消息，并确保验证者即使在数据包丢失和潜在的恶意节点的情况下也能重建区块提议。

---

## 12. Python 现在可以运行 Mojo 了

**原文标题**: Python can run Mojo now

**原文链接**: [https://koaning.io/posts/giving-mojo-a-spin/](https://koaning.io/posts/giving-mojo-a-spin/)

本文探讨了 Chris Lattner 宣布的从 Python 运行 Mojo 代码的新功能。作者热衷于寻找一种用于加速 Python 函数的编译型语言，测试了这种集成并分享了他们的经验。

使用 `uv` 进行设置的过程被描述为比以前更简单。作者提供了 `.mojo` 和 `.py` 代码示例，演示了从 Python 调用 Mojo 阶乘函数。虽然基本功能可以工作，但在计算 100 的阶乘时遇到了溢出问题，突显了 Modular 堆栈的早期状态。

为了进一步评估性能，作者使用 Mojo、Python 和 NumPy 实现了一个简单的素数计数算法。结果表明，在这个特定的测试用例中，Mojo 比 Python 和 NumPy 快得多。

作者总结说，虽然 Modular 堆栈仍处于早期阶段，并且存在一些粗糙之处，但在 Python 工作流程中使用 Mojo 获得显著加速的潜力令人兴奋，并且越来越触手可及。与 Rust 相比，学习 Mojo 的容易程度，加上所实现的加速效果，使其成为加速 Python 代码的一个有希望的选择。然而，作者建议它还没有完全准备好用于“黄金时段”的生产环境。

---

## 13. 透明的野心：论半透明用户界面

**原文标题**: Transparent Ambition: on translucent user interfaces

**原文链接**: [https://take.surf/2025/06/19/transparent-ambition](https://take.surf/2025/06/19/transparent-ambition)

本文批判了日益流行的半透明用户界面设计趋势，以苹果公司的“液态玻璃”以及之前的Aero和Vibrancy为例。作者认为，虽然这些设计旨在看起来很酷并展示内容，但最终会阻碍可用性。半透明降低了视觉清晰度，使UI元素更难辨认，并将美学置于功能之上。

作者认为，这些设计优先考虑视觉品牌和一致性，而不是用户体验。他们感叹用于UI定义的“墨水”正在减少，导致易读性问题并牺牲了既定的设计原则。虽然承认半透明在混合现实等特定环境中的潜力，但作者批评了它的广泛应用，尤其是在macOS系统设置等情况下，这些情况不恰当地借鉴了iOS设计。

作者将当前的趋势与早期版本（如Mac OS X的Aqua）进行了对比，后者尽管最初很华丽，但已经发展到将可用性与美学放在同等重要的位置。“液态玻璃”似乎优先考虑视觉吸引力，而牺牲了可靠且直观的界面。

文章最后将“液态玻璃”与iPhone X的手势界面进行了对比，认为后者提供了有形控制，而不是视觉错觉。作者认为半透明的UI元素类似于汽车上的镀铬：视觉上很有吸引力，但最终对交互效率较低。作者认为，核心问题在于这些设计背后的意图，似乎优先考虑外观而不是可用性。

---

## 14. 克莱因瓶亚马逊品牌劫持 (2021)

**原文标题**: Klein Bottle Amazon Brand Hijacking (2021)

**原文链接**: [https://www.kleinbottle.com/Amazon_Brand_Hijacking.html](https://www.kleinbottle.com/Amazon_Brand_Hijacking.html)

无法访问文章链接。

---

## 15. 使用Home Assistant、AdGuard Home和一个8美元的智能插座来避免脑死亡

**原文标题**: Using Home Assistant, adguard home and an $8 smart outlet to avoid brain rot

**原文链接**: [https://www.romanklasen.com/blog/beating-brainrot-by-button/](https://www.romanklasen.com/blog/beating-brainrot-by-button/)

本文介绍了一种利用Home Assistant、Adguard Home和一个智能插座来限制访问诸如社交媒体等令人分心的内容，以对抗“大脑腐烂”的方法。作者是一位软件开发者，意识到互联网既是必不可少的工具，也是主要的干扰源，因此寻求一种并非完全阻止的解决方案，因为这种方案对他们自己和他们的妻子来说都过于严格。

实施的解决方案围绕着一个支持Zigbee的智能插头和Adguard Home展开，Adguard Home是一个集成到他们的gli.net路由器中的全网络广告拦截器。核心思想是拥有一个物理按钮（由智能插头触发），暂时禁用Adguard Home的自定义过滤规则，允许在有限的时间内（15分钟）访问被阻止的内容。一个冷却期（一小时）可以防止立即重新访问。

设置涉及在Adguard Home中配置自定义过滤规则，通过手动将用户凭据添加到Adguard Home配置文件来启用API访问，并使用Home Assistant来控制Adguard Home集成公开的“过滤”开关。该系统的核心是一个Home Assistant自动化，当按下按钮时，它会关闭过滤，强制执行时间限制，并包括使用`input_datetime`和`input_boolean`助手跟踪上次禁用时间和活动覆盖状态的冷却期逻辑。

虽然作者承认用户仍然可以通过禁用WiFi来绕过该系统，但他认为该解决方案为实践适度和以更受控的剂量消费社交媒体提供了一个框架。

---

## 16. Fairphone 6 将采用更加可持续的新设计

**原文标题**: Fairphone 6 is switching to a new design that's even more sustainable

**原文链接**: [https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design](https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design)

即将上市的 Fairphone 6 预计将于 6 月 25 日发布，采用重新设计、更具可持续性和模块化的设计。泄露的渲染图展示了该手机的黑色、白色和绿色配色方案，具有扁平边缘和独特的霓虹主题电源按钮。与前代产品不同，Fairphone 6 放弃了突出的相机遮阳板，转而采用独立放置的相机传感器。

核心重点仍然是用户的可修复性。营销图片表明，该设计采用螺丝固定后盖和电池，无需胶水即可轻松拆卸。预计这种方法将扩展到相机、显示屏和扬声器模块，从而进一步实现手机的可持续发展目标。

传闻规格包括 6.31 英寸 pOLED 120Hz 显示屏、骁龙 7s Gen 3 处理器搭配 8GB 内存和 256GB 可扩展存储空间，以及 4415mAh 电池，支持 33W 快速充电。相机规格包括 50MP 主传感器、13MP 副传感器和 32MP 自拍摄像头。预计起价为 549 欧元。据报道，Fairphone 6 将获得 A 级可修复性和耐用性认证。

---

## 17. 同伦等价

**原文标题**: Homotopy Equivalences

**原文链接**: [https://bartoszmilewski.com/2025/06/20/weak-homotopy-equivalences/](https://bartoszmilewski.com/2025/06/20/weak-homotopy-equivalences/)

本文探讨了同伦等价的概念，它是拓扑学中同胚的一种放松形式，允许形状收缩，同时保留诸如孔洞数量等基本特征。

同伦等价涉及拓扑空间之间的连续函数，其复合函数与恒等映射同伦，这意味着一个可以连续形变为另一个。与点同伦等价的空间称为可收缩的。

本文随后将同伦与环路和基本群联系起来。空间中的环路可以基于同伦被分类为等价类，形成群胚结构。固定一个基点会导致基本群，反映了空间的“孔洞结构”。同伦等价的空间具有相同的基本群。

本文将这个想法扩展到高阶同伦群，用 n 维球面代替环路来检测高维孔洞。这引出了无穷群胚的概念，这是同伦类型理论中无穷群胚的灵感来源。

本文最后介绍了弱同伦等价，它在所有同伦群之间诱导同构，代表着比标准同伦等价更弱的等价概念。当局部异常阻止强等价时，这些等价是有用的。格罗滕迪克推测，无穷群胚捕获了拓扑空间的所有信息，直至弱同伦等价。弱等价、纤维化和上纤维化是弱分解系统和奎伦模型范畴中的基础。

---

## 18. 20亿人没有安全饮用水：这对他们意味着什么？

**原文标题**: 2B people don't have safe drinking water: what does this mean for them?

**原文链接**: [https://ourworldindata.org/what-no-safe-water-means](https://ourworldindata.org/what-no-safe-water-means)

本文探讨了全球20亿人缺乏安全饮用水的现实。文章强调，这些人中的大多数并非依赖河流或湖泊等地面水源，而是能获取管道供水或受保护的水井，但这些水源不在家中，无法持续供应，或不能保证无污染。

文章对用水获取水平进行了分类，并使用“美元街”项目的例子来说明每个层级的家庭所面临的挑战。文章强调了缺乏安全饮用水的两个主要后果：受污染水带来的健康风险和收集水所需的大量时间投入。

作者强调，尽管世界上95%的人口使用的是“改良”水源，但最终目标是在*家中*获得经检验无污染的安全饮用水。

文章最后重申了不安全用水的毁灭性影响：个人（主要是妇女和儿童）花费在收集水上的过多时间负担，以及每年因水源性疾病和营养不良而造成的超过80万人的悲惨死亡，其中儿童居多。这些死亡集中在低收入国家，凸显了实现全民安全饮用水普及的紧迫性。

---

## 19. Postgres语法拾趣

**原文标题**: Interesting Bits of Postgres Grammar

**原文链接**: [https://steve.dignam.xyz/2025/06/20/interesting-bits-of-postgres-grammar/](https://steve.dignam.xyz/2025/06/20/interesting-bits-of-postgres-grammar/)

本文基于作者开发linter的经验，重点介绍了Postgres SQL语法中一些有趣且不寻常的方面。

首先，Postgres大量使用自定义运算符，从而可以进行几何类型等专门操作。 这些可以是前缀或中缀，并且令人惊讶地能够解析Trino lambda语法（尽管存在优先级问题）。

其次，复合`SELECT`语句表现出意外的优先级。 与`UNION`一起使用时，`ORDER BY`子句适用于整个组合结果，而不仅仅是最终的`SELECT`。

第三，本文介绍了Postgres对类型的处理，特别是`CREATE FUNCTION`中的`%type`语法，该语法允许为函数参数指定列的数据类型。

第四，本文解释了Postgres如何处理字符串连接。 单独行上的相邻字符串文字会自动连接，但注释会破坏此连接并抛出语法错误。

第五，它讨论了带引号的标识符，表明`t`和`"t"`是等效的，以及如何在标识符名称中转义双引号（使用`""`）。 它解释了Unicode转义，展示了`U&`前缀和自定义转义字符。

最后，本文提到了`operator()`函数语法，这是一种使用运算符的替代方法，允许进行模式指定，并且还可以与前缀运算符一起使用。 作者总结说，由于自定义运算符的灵活性以及与其他语言的差异，它们在实现Postgres解析器时构成了最大的挑战。

---

## 20. 告诉我你最喜欢的树（一个慢速网络提案）

**原文标题**: Tell me about your favorite tree (a slow-web proposal)

**原文链接**: [https://nannnsss.omg.lol/2025/tell-me-about-your-favorite-tree/](https://nannnsss.omg.lol/2025/tell-me-about-your-favorite-tree/)

这篇文章，题为“告诉我你最喜欢的树（一个慢速网络的提议）”，是对互联网逝去时代的哀歌——一个将个人连接、脆弱性和发现置于货币化和引人注目的算法之上的时代。作者将此与当前互联网的状态进行对比，后者由挖掘数据、优先考虑利润并将用户锁定在生态系统中的科技巨头所主导。这种转变让个人感到孤立无援，并受制于精心设计的内容消费。

作者渴望一个更慢、更具目的性的互联网，其特点是个人隐私、创造力和真正的连接。他们描述了参与这种“小型网络”的策略，包括建立个人网站、有意识地选择有道德的科技供应商、摆脱盈利性社交媒体、投资于开源技术、限制在线数据跟踪以及与小型互联网内容创作者互动。

核心信息是一个行动号召。作者敦促读者想象一个摆脱资本主义控制的互联网，一个可以改善生活并促进与他人和自然世界之间有意义的联系的互联网。他们鼓励读者采取小步骤来创造这个设想的世界，优先考虑目的性，抵制大型科技公司的诱惑，并拥抱更个性化、更道德和更互联的在线体验。“告诉我你最喜欢的树”的情感概括了这种对亲密、具体细节的渴望，倾向于真正的人际连接而非肤浅的内容消费。

---

## 21. Show HN: 在浏览器中畅玩乐高岛

**原文标题**: Show HN: Lego Island Playable in the Browser

**原文链接**: [https://isle.pizza](https://isle.pizza)

这个“Show HN”帖子宣布了 1997 年 PC 游戏《乐高岛》的网页浏览器移植版，使这款经典游戏能够为所有人所体验。该项目是对原作的重制，使用 Emscripten 重建，并基于之前的一个反编译项目，该项目随后被改编成便携版本。这个网页移植版代表了一项历时一年的努力，涉及众多致力于保护游戏历史的贡献者。

虽然仍在开发中，该帖子重点介绍了诸如游戏开发纪录片、24/7 乐高岛广播流、乐高岛 Wiki、反编译源代码、游戏便携版本以及网站本身的源代码 (isle.pizza) 等资源。其他资源包括用于修补/修改原始游戏的工具 SIEdit、创意总监未完成的回忆录、可下载的海报、开发材料档案、采访和幕后视频。还有一个高质量的音轨重新数字化版本。

该帖子强调这是一个非官方的粉丝项目，未经乐高认可。最后，它以幽默的方式更新了游戏中的一句台词，提到了玩原版游戏需要 CD，并告知用户游戏正在加载。

---

## 22. 因卡夫放弃人工色素用于酷爱和果冻，对人工色素的抵制日益增长。

**原文标题**: Backlash to artificial dye grows as Kraft ditches coloring for Kool-Aid, Jell-O

**原文链接**: [https://www.washingtonpost.com/business/2025/06/17/kraft-heinz-artificial-food-dyes-us-products/](https://www.washingtonpost.com/business/2025/06/17/kraft-heinz-artificial-food-dyes-us-products/)

无法访问文章链接。

---

## 23. Nano-Vllm: 从头构建的轻量级 vLLM 实现

**原文标题**: Nano-Vllm: lightweight vLLM implementation built from scratch

**原文链接**: [https://github.com/GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm)

Nano-vLLM 是 vLLM 的一个轻量级、从零开始的实现，旨在通过约 1200 行 Python 的可读代码实现快速的离线推理。它拥有一套优化方案，包括前缀缓存、张量并行、Torch 编译和 CUDA 图的使用。可以通过 pip 轻松安装。API 在很大程度上镜像了 vLLM 的 API，简化了现有用户的过渡。在使用 Qwen3-0.6B 模型在 RTX 4070 笔记本电脑上进行的基准测试表明，在处理 256 个序列，输入和输出长度在 100 到 1024 个 token 之间随机采样时，Nano-vLLM 实现了与 vLLM 相当甚至略快的吞吐量（1434.13 tokens/s），而 vLLM 的吞吐量为 1361.84 tokens/s。`example.py` 和 `bench.py` 文件分别提供了使用示例和基准测试工具。Nano-vLLM 的重点是在不显著牺牲性能的前提下，提供一个精简且易于理解的 vLLM 替代方案。

---

## 24. uv：一个用Rust编写的极速Python包和项目管理器

**原文标题**: uv: An extremely fast Python package and project manager, written in Rust

**原文链接**: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

uv 是一个全新的、极快的 Python 包和项目管理器，用 Rust 编写，旨在取代 pip、pip-tools、poetry 等工具。它拥有比 pip 快 10-100 倍的速度，并提供全面的项目管理功能，包括锁定文件和 Cargo 式工作区。uv 可以运行带有内联依赖项元数据的脚本，安装和管理 Python 版本，以及执行作为 Python 包发布的工具。

主要特性包括通过全局缓存实现磁盘空间效率，无需 Rust 或 Python 即可安装，并支持 macOS、Linux 和 Windows。它由 Ruff 的创建者 Astral 提供支持。

uv 通过初始化、添加依赖项、运行脚本和管理锁定文件的命令简化了项目管理。它还通过管理依赖项和创建隔离环境，简化了处理单文件脚本的工作。用户可以安装和管理 Python 版本，并在它们之间快速切换。

uv 为 pip、pip-tools 和 virtualenv 命令提供了一个即插即用的替代方案，在不改变现有工作流程的情况下，提供了显著的速度提升。安装非常简单，可以使用独立安装程序或通过 pip/pipx。文档提供了关于 uv 各个方面的详细信息，并且项目鼓励贡献。

---

## 25. X窗口系统最初并没有X终端。

**原文标题**: The X Window System didn't immediately have X terminals

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate](https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate)

Chris Siebenmann的页面解释了为什么使用旧浏览器的用户无法访问他的博客“Wandering Thoughts”及其相关维基CSpace。他实施了反爬虫措施，原因是最近涌现大量高流量爬虫，特别是那些使用旧版Chrome用户代理的爬虫，这些爬虫通常用于收集数据以进行LLM训练。

Siebenmann认为这些爬虫给他的博客带来了不必要的负载，因此正在阻止它们，即使这无意中影响了使用过时浏览器的合法用户。他鼓励遇到此错误的用户，特别是使用当前浏览器的用户，向他提供他们的浏览器详细信息和User-Agent字符串。

该说明还针对通过archive.today、archive.ph和archive.is等存档服务访问该网站的用户。他解释说，这些服务以与恶意行为者无法区分的方式进行爬取，使用旧版Chrome用户代理、分布式IP地址，有时还伪造反向DNS条目。他建议改用archive.org，因为它是一个行为更好的存档爬虫，可以访问他的博客。

---

## 26. 众议院工作人员设备禁用 WhatsApp

**原文标题**: WhatsApp banned on House staffers' devices

**原文链接**: [https://www.axios.com/2025/06/23/whatsapp-house-congress-staffers-messaging-app](https://www.axios.com/2025/06/23/whatsapp-house-congress-staffers-messaging-app)

无法访问文章链接。

---

## 27. 无线电花园

**原文标题**: Radio Garden

**原文链接**: [https://radio.garden/?2025](https://radio.garden/?2025)

本文介绍了 Radio Garden，一个允许用户探索来自世界各地直播电台的网站。其核心功能是旋转的地球界面，以可视化的方式呈现不同电台的地理位置。为了充分利用该网站，用户需要在其网页浏览器中启用 JavaScript。本质上，Radio Garden 提供了一个数字平台，用于发现和收听全球多样化的广播内容，并通过其交互式地球界面强调易于导航。

---

## 28. 使用 SIMD 在 60 毫秒内找到十亿个阶乘

**原文标题**: Finding a billion factorials in 60 ms with SIMD

**原文链接**: [https://codeforces.com/blog/entry/143279](https://codeforces.com/blog/entry/143279)

好的，我已经阅读了提供的URL中的文章。这是一份摘要：

文章《使用SIMD在60毫秒内计算十亿阶乘》描述了一种优化技术，可以使用单指令多数据（SIMD）指令非常快速地计算大量阶乘。作者强调了传统阶乘计算的局限性，尤其是在需要在短时间内计算大量阶乘时。

核心思想是利用SIMD并行执行多个乘法运算。作者特别详细介绍了如何预先计算一个大型阶乘值表。然后，使用SIMD，他们计算此预计算表中几个连续值的乘积，从而实现大规模的并行计算。该博文强调，由于各个阶乘不一定是连续的，因此它们不能依赖于常用的阶乘计算方法（n！= n *（n-1）！）。

具体来说，文章提到了处理溢出的策略以及表示大数的必要性。虽然没有详细讨论，但它提到了使用超出典型整数大小的技术来处理更大的数字乘法。

关键要点是，通过预先计算阶乘并使用SIMD指令执行并行乘法，作者实现了显著的性能改进，使他们能够在大约60毫秒内计算十亿阶乘。这篇文章为常见的计算挑战提供了一种务实的方法，说明了SIMD优化的强大功能。

---

## 29. 滚动吸附、状态查询、怪物猎人与游戏化

**原文标题**: Scroll snapping, state queries, monster hunter, and gamification

**原文链接**: [https://utilitybend.com/blog/the-customizable-select-part-four-scroll-snapping-state-queries-monster-hunter-and-gamification](https://utilitybend.com/blog/the-customizable-select-part-four-scroll-snapping-state-queries-monster-hunter-and-gamification)

本文详细介绍了如何创建一个游戏化的、可定制的选择元素，其灵感来自于怪物猎人游戏中的用户界面，特别是物品轮盘。作者重现了带有视觉提示和键盘导航的水平滚动物品选择功能，同时探索了可访问性。

HTML结构包括一个 `<select>` 元素、一个 `.trigger` (作为选定项目显示)、一个 `.frame` (一个静态视觉元素) 和一个 `.items` 容器用于可滚动选项。CSS 侧重于对这些元素进行样式化和定位，使用特性查询以确保渐进增强。关键的 CSS 特性包括用于精确定位元素的锚定、具有滚动捕捉的水平滚动以及用于在捕捉时缩放图标的滚动状态查询。

JavaScript 处理拖放功能、箭头键导航（因为默认行为已损坏），并利用 `scrollsnapchange` 事件来动态更新选定的内容。使用 `dragging` 类启用拖动以操纵 `scroll-snap-type`。

作者还考虑了可访问性，特别是通过箭头按钮实现的单指针模式，但也承认了潜在的挑战。目标是展示样式化选择元素可以达到的程度，创造一种视觉上引人入胜且互动性强的体验，让人联想到怪物猎人用户界面。最后提供了 CodePen 演示，供用户体验创建的效果。

---

## 30. Rivulet：受书法和代码启发的深奥编程语言[视频]

**原文标题**: Rivulet: An esolang inspired by calligraphy && code [video]

**原文链接**: [https://media.ccc.de/v/gpn23-35-rivulet-an-esolang-inspired-by-calligraphy-and-other-experiments-in-natural-language-code](https://media.ccc.de/v/gpn23-35-rivulet-an-esolang-inspired-by-calligraphy-and-other-experiments-in-natural-language-code)

Gulaschprogrammiernacht 23 的视频演示“Rivulet：一种受书法和代码启发的深奥语言”介绍了 Rivulet，这是一种由 Daniel Temkin 创建的新型深奥编程语言 (esolang)。Rivulet 摒弃了关键字，其灵感来自书法写作和自然语言，而不是数学符号。该语言使用流畅的线条和“线束”来创建“字形”，不同的线束类型决定逻辑。

该讲座重点介绍了 Rivulet 背后的视觉灵感，汲取自迷宫、像 Anni Albers 的“Meanders”这样的艺术作品以及空间填充算法。它强调 Rivulet 的规则类似于自然演化的语言，优先考虑表达性而不是绝对清晰度。

该演示展示了 Rivulet 代码的示例，特别是展示了表示数字零的七种方法。Temkin 将 Rivulet 与其他拥抱自然语言的模糊性和表达性的深奥语言进行了对比，包括他自己的多义深奥语言 Valence 和一种未命名的构造语言/深奥语言字母表。其目的是展示如何将自然语言特征集成到编程语言设计中。该视频提供各种格式（AV1、MP4、WebM）和分辨率的下载，并附带音频下载。

---

## 31. DHEA-S激素与男性寿命缩短有关，但与女性无关

**原文标题**: DHEA-S hormone linked to shorter lifespan in men, but not women

**原文链接**: [https://medicalxpress.com/news/2025-06-dhea-hormone-linked-shorter-lifespan.html](https://medicalxpress.com/news/2025-06-dhea-hormone-linked-shorter-lifespan.html)

本研究报告了由CUNY SPH教授Mary Schooling领导的一项新的基因研究，该研究表明男性体内较高水平的脱氢表雄酮硫酸盐（DHEA-S）与寿命缩短有关，而女性则不然。这项发表在《营养、代谢和心血管疾病》上的研究，利用了来自大型欧洲人群的孟德尔随机化方法，以最大限度地减少混淆因素。

该研究调查了基因决定的较高DHEA-S水平对血压和寿命的影响，弥补了关于DHEA补充剂效果缺乏“金标准”证据（随机对照试验）的空白。研究结果表明，基因决定的较高DHEA-S会增加血压并缩短寿命，尤其是在男性中，而对女性没有观察到显著影响。

Schooling教授认为，这些发现与FDA关于睾酮产品会升高男性血压的警告相符，因为DHEA-S是睾酮的前体。她还对美国DHEA的非处方药可及性和标签问题表示担忧，因为它可能与男性寿命缩短有关。

---

## 32. Polystate：可组合的有限状态机

**原文标题**: Polystate: Composable Finite State Machines

**原文链接**: [https://github.com/sdzx-1/polystate](https://github.com/sdzx-1/polystate)

本文介绍 Polystate，一个用于构建可组合且类型安全的有限状态机 (FSM) 的 Zig 库。 Polystate 的核心理念围绕在类型层面表示状态机的状态，并通过类型组合实现可组合性。

该库强调通过声明式、组合式的结构来定义程序行为，从而提高代码的简洁性、正确性和安全性。一个关键优势是通过类型组合实现语义级别的代码重用。 Polystate 可以从这些声明中自动生成状态图，从而提供程序整体行为的视觉清晰度。

本文概述了使用 Polystate 的实用约定，重点在于 FST（FSM 类型）和 GST（全局状态类型）。文章展示了示例，包括一个简单的状态机和一个使用 "yes_or_no" 状态的可组合状态机，演示了如何定义状态、消息、处理函数和消息生成器。

至关重要的是，可组合性被强调为一个核心优势，它通过组合更简单的状态来创建复杂的状态机，例如在 ATM 示例中使用嵌套的 "checkPin" 状态来强制执行最大 PIN 输入尝试次数。 另一个示例涉及使用 `raylib` 库在图形环境中实现可重用的选择语义。 Polystate 鼓励一种从以类型为中心和组合的角度设计程序状态的编程风格，从而改进命令式程序结构。

---

## 33. Verlet积分与布料物理模拟（2022）

**原文标题**: Verlet Integration and Cloth Physics Simulation (2022)

**原文链接**: [https://pikuma.com/blog/verlet-integration-2d-cloth-physics-simulation](https://pikuma.com/blog/verlet-integration-2d-cloth-physics-simulation)

本文介绍了 Verlet 积分，一种用于游戏物理模拟的方法，重点在于其在布料模拟中的应用。文章首先将物理模拟框架化为一个离散过程，其中涉及对力、加速度、速度和位置的近似。Verlet 积分被认为是一种稳定且高效的欧拉和龙格-库塔方法的替代方案，尤其适用于粒子和约束系统，例如布料。

本文强调理解微积分的基础。它提供了“101”级别的微分和积分回顾，解释了诸如斜率、瞬时变化率、导数、曲线下面积和不定积分规则等概念。微分用一个二次函数来说明，演示了如何找到它的导数并将其解释为瞬时变化率。积分通过求线性函数下的面积的例子来解释，突出了不定积分规则和积分常数的概念。本节为读者提供了理解 Verlet 积分背后的机制及其在模拟逼真布料行为中的应用所需的基础知识。作者在深入探讨实际实现之前，先建立了数学基础。

---

## 34. 展示HN：Turbine – 用C语言构建的16位CPU架构和模拟器

**原文标题**: Show HN: Turbine – 16-bit CPU Architecture and Emulator built in C

**原文链接**: [https://www.errorcodezero.dev/blog/building-my-own-cpu-isa-and-virtual-machine/](https://www.errorcodezero.dev/blog/building-my-own-cpu-isa-and-virtual-machine/)

该“Show HN”帖子详细介绍了程序员深入底层编程和模拟的历程，最终完成了“Turbine”的创建，这是一个用 C 语言编写的 16 位 CPU 架构和模拟器。作者最初受 Advent of Code 的启发，探索系统编程和语言开发，最终对字节码虚拟机和老式计算机产生了浓厚的兴趣。

该帖子描述了构建 Turbine 的过程，包括其指令集（LOAD、DUMP、MOVE、PUSH、POP、ADD、SUB、NOT、OR、AND、CMP、JUMP、HLT）、寄存器标志和状态标志的设计。作者解释了指令指针、堆栈指针、基址指针和累加器等寄存器的重要性。数据总线为 16 位宽，而字长为 8 位。该帖子还解释了堆栈数据结构及其以相反顺序运行的方式。

代码片段展示了 C 语言中的 `VirtualMachine` 结构体，包括寄存器、内存和一个停止标志的字段。`init_vm` 函数初始化 VM，帖子介绍了 `step_vm` 函数，该函数执行指令。由于可移植性问题，作者选择使用标准的 `switch` 语句而不是计算的 goto 来进行指令分发。作者最后提到编译器可能会将 switch 语句优化成某种东西。

---

## 35. 使用波函数坍缩算法大规模生成拼图地图

**原文标题**: Using Wave Function Collapse to solve puzzle map generation at scale

**原文链接**: [https://sublevelgames.github.io/blogs/2025-06-22-nurikabe-map-gen-with-wfc/](https://sublevelgames.github.io/blogs/2025-06-22-nurikabe-map-gen-with-wfc/)

本文详细介绍了如何使用波函数坍缩（WFC）为游戏“逻辑岛屿”生成谜题地图，特别针对现代、极简和阴阳规则集遇到的挑战。由于其墙壁模式的复杂性，这些规则集使用传统方法难以生成大于7x7的有效地图。

核心问题是生成符合特定规则的有效墙/岛配置。WFC被选为解决方案，因为它能够基于复杂的连接关系创建模式。关键是通过精心定义的图块类型及其在Simple-Tiled WFC框架内的连接关系来表示墙壁连接要求和约束（如禁止2x2墙壁/岛屿）。

对于现代规则集，作者巧妙地生成*岛屿*而不是墙壁，简化了流程并通过策略性地控制图块连接来防止2x2岛屿。极简规则集要求所有墙壁区域恰好为3个单元格，通过将图块集限制为11种类型并仔细设计连接关系来解决，从而使所需的墙壁尺寸成为WFC过程的自然结果。阴阳规则集具有独特的互连岛屿和墙壁要求，涉及将岛屿和墙壁都创建为WFC线，然后通过指定两个最大区域来修改结果。

文章总结道，WFC是生成具有复杂逻辑规则的益智游戏内容的强大工具。通过重新构建问题并通过图块连接表达约束，作者成功地为所有六个逻辑岛屿规则集生成了大规模地图（高达12x12），证明了WFC在简单纹理合成之外的能力。

---

## 36. 苹果下架YouTube上的“说服你的父母给你买Mac”广告

**原文标题**: Apple Pulls 'Convince Your Parents to Get You a Mac' Ad from YouTube

**原文链接**: [https://www.macrumors.com/2025/06/21/apple-pulls-the-parent-presentation-video/](https://www.macrumors.com/2025/06/21/apple-pulls-the-parent-presentation-video/)

苹果已下架最近发布的YouTube广告“家长展示”，该广告旨在帮助学生说服家长购买Mac电脑用于大学学习。该视频由喜剧演员马丁·赫利希演示如何使用可定制的演示文稿，现已被标记为私有且无法访问。此外，苹果已将相关的“家长展示”下载（提供PowerPoint、Keynote和Google幻灯片格式）移至其大学生网页底部，有效地降低了其可见性。

该广告下架的原因尚不清楚，苹果公司尚未回应置评请求。猜测认为，社交媒体上的负面反响可能起到了一定作用，一些观众将该广告称为“尴尬”或“恶心”。然而，并非所有反馈都是负面的，有些人觉得这个视频很幽默。

这并非苹果公司首次在面临强烈反对后从YouTube撤下广告，尽管文章也提到了集体诉讼。“家长展示”本身是一个可定制的幻灯片，学生可以使用它来论证拥有Mac电脑对学习的好处。虽然演示文稿仍然可以下载，但随附的宣传视频现在已被隐藏。

---

## 37. 我用 Typst 撰写了我的博士论文。

**原文标题**: I wrote my PhD Thesis in Typst

**原文链接**: [https://fransskarman.com/phd_thesis_in_typst.html](https://fransskarman.com/phd_thesis_in_typst.html)

本文详述了作者使用现代排版语言Typst而非传统LaTeX撰写博士论文的经历。作者重点介绍了在此过程中遇到的优点和缺点。

**优点：** 相比LaTeX，Typst拥有显著更快的编译速度，从而允许快速迭代。该语言本身因其设计良好、一致且可脚本化的特性而受到赞扬，与Rust有相似之处。这使得数据集成和自定义图形生成变得容易。由于语言更简洁，Typst中的布局定制也更加容易。最后，Typst的语法高亮和错误消息优于LaTeX。

**缺点：** Typst的参考文献管理不够成熟。问题包括参考文献数量的限制、与BibTeX变量的不兼容以及根据特定要求自定义参考文献样式的困难。在复杂情况下，错误消息也可能没有帮助。

**复杂之处：** LaTeX的普遍存在带来了挑战，需要作者将现有文档转换为Typst，并创建一个自定义工具将Typst文档转换为LaTeX以供期刊投稿。由于Typst尚未被广泛采用，协作也可能受到阻碍。年轻的Typst生态系统意味着可能需要从头开始创建模板。

**结论：** 作者推荐Typst给熟悉编程和工具调整的用户，强调其通过更快的迭代来提高文档质量的潜力。然而，对于那些寻求开箱即用解决方案的人来说，LaTeX仍然是更实际的选择。

**导师的观点：** 导师承认最终结果很好，但警告说Typst需要大量的调整，并建议只给那些具有编程技能的人使用。他们强调了由于导师不熟悉Typst而导致的来回编辑过程的低效性。

---

## 38. Deskflow – 在多台电脑之间共享一套键盘和鼠标

**原文标题**: Deskflow – Share a single keyboard and mouse between multiple computers

**原文链接**: [https://github.com/deskflow/deskflow](https://github.com/deskflow/deskflow)

Deskflow：一款免费开源的KVM软件，允许用户在多台电脑间共享一套键盘鼠标。它支持Windows、macOS和Linux，包括Wayland，并提供TLS加密和剪贴板共享功能。

安装时，用户可以下载软件包、使用软件包仓库或从源代码构建。建议macOS用户使用Homebrew。Windows用户需要安装Microsoft Visual C++ Redistributable。Linux需要特定版本的`libei`、`libportal`和Qt。

对于macOS，必须在“隐私与安全性”设置中授予Deskflow应用和`deskflow`进程辅助功能权限。

Deskflow旨在与Lan Mouse、Input Leap和Synergy等类似项目实现互操作性，并且兼容Input Leap和Barrier。当在服务器设置中选择Synergy协议时，它也适用于Synergy 1。

该项目欢迎社区贡献和Pull Request。Wayland支持通过`libei`和`libportal`实现。Deskflow最初于2001年作为Synergy创建，现在由Synergy赞助，提供代码和资金支持。它在GPL-2.0许可下发布，并带有OpenSSL例外。

---

## 39. 仅用64位状态的2048游戏

**原文标题**: 2048 with only 64 bits of state

**原文链接**: [https://github.com/izabera/bitwise-challenge-2048](https://github.com/izabera/bitwise-challenge-2048)

本文介绍了一种独特的终端2048游戏实现，其特点在于极其紧凑的状态表示：仅需64位。这使得玩家只需交换一个数字即可与他人分享其精确的游戏状态。

核心概念围绕基于初始种子的确定性游戏展开。 如果未通过`$STATE`环境变量提供种子，则游戏会生成一个新的随机种子。 但是，如果设置了`$STATE`变量（包含一个64位数字），则游戏将使用该值作为种子，从而使棋盘状态和所有后续单元格生成完全可预测和可重现。

这种确定性是共享方面的关键。 通过共享64位的`$STATE`值，玩家可以有效地将其确切的游戏棋盘和未来的游戏事件传输给另一位玩家，从而实现协作解决问题、竞争性重播或仅仅展示令人印象深刻的分数。 本文重点介绍了与传统的2048实现相比，状态大小的显着减少，从而为游戏提供了一种新颖而有效的方法。

---

## 40. 张量操控单元 (TMU)：可重构、近内存、高吞吐量人工智能

**原文标题**: Tensor Manipulation Unit (TMU): Reconfigurable, Near-Memory, High-Throughput AI

**原文链接**: [https://arxiv.org/abs/2506.14364](https://arxiv.org/abs/2506.14364)

本文介绍了一种新型硬件模块——张量操控单元 (TMU)，旨在加速 AI SoC 中的张量操控运算。作者指出，虽然 AI SoC 研究侧重于张量计算，但数据密集型的张量操控经常被忽视。TMU 旨在通过可重构的近内存架构来解决这一差距。它以内存到内存的方式运行，采用 RISC 风格的执行模型和统一寻址，以支持各种张量转换。

TMU 旨在与高性能 AI SoC 中的张量处理单元 (TPU) 协同工作。通过利用双缓冲和输出转发，它可以提高整体流水线利用率。TMU 采用中芯国际 (SMIC) 40 纳米工艺制造，占地面积仅为 0.019 平方毫米，并支持超过 10 种张量操控算子。

基准测试结果表明了 TMU 的有效性。与 ARM A72（高达 1413 倍）和 NVIDIA Jetson TX2（高达 8.54 倍）相比，TMU 实现了显著的算子级延迟降低。此外，当与自研 TPU 集成时，整个系统显示端到端推理延迟降低了 34.6%，突出了可重构张量操控在现代 AI SoC 中的优势。作者得出结论，TMU 为处理 AI 应用中数据密集型任务提供了一种可扩展且高效的解决方案。

---

## 41. 文学小说的文化衰落

**原文标题**: The cultural decline of literary fiction

**原文链接**: [https://oyyy.substack.com/p/the-cultural-decline-of-literary](https://oyyy.substack.com/p/the-cultural-decline-of-literary)

无法访问文章链接。

---

## 42. Claude VSCode 代码助手

**原文标题**: Claude Code for VSCode

**原文链接**: [https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)

Claude Code for VSCode 是一个 Visual Studio Code 扩展，它将 Claude 的 AI 编码能力直接集成到 IDE 中。它需要从 claude.ai/code 单独安装 Claude Code。该扩展旨在通过允许开发者无需离开 VSCode 即可利用 Claude 的功能来增强编码工作流程。

主要功能包括：从 VSCode 终端启动 Claude Code 时自动安装、自动将选定的文本作为 Claude 的上下文、能够在 VSCode 的差异查看器中显示代码更改、键盘快捷键（例如 Alt+Cmd+K 用于将选定的代码推送到 Claude）以及标签页感知，以便 Claude 可以看到打开的文件。该扩展还允许配置，从而启用诸如自动差异工具选择等功能。

该扩展需要 VS Code 1.98.0 或更高版本，并被确认为早期版本，可能包含错误或不完整的功能。该扩展的安装量已超过 20,000 次，并且免费提供。

---

## 43. 与弗朗辛·普罗斯的访谈 [音频]

**原文标题**: Interview with Francine Prose [audio]

**原文链接**: [https://www.laphamsquarterly.org/content/episode-3-francine-prose](https://www.laphamsquarterly.org/content/episode-3-francine-prose)

这是对弗朗辛·普罗斯的采访，她是《1974：一部个人史》的作者。在采访中，她讨论了尼克松时代她在旧金山的经历。她回忆了科技繁荣之前这座城市的艺术自由，描述了在里诺酒店等地的公社生活，那里是艺术家们的天堂。普罗斯将此与她的背景进行了对比，提到她避免了反主流文化中更为极端的方面。

她回忆了她和她的丈夫参与的反越战抗议活动，包括她的丈夫攀爬五角大楼。对话涉及了20世纪60年代反主流文化的失败，以及她的经历与阿尔弗雷德·希区柯克的电影《迷魂记》之间的相似之处。

采访还提到了普罗斯的众多作品和其他有影响力的书籍和电影，从艾萨克·巴别尔到琼·狄迪恩和蒂姆·波顿。这次采访旨在宣传普罗斯的书，并探讨了理想主义、社会变革以及历史事件的持久影响等主题。采访中引用的作品列表也已提供。

---

## 44. 自上世纪30年代以来，我们一直拥有丹尼索瓦人头骨，只是无人知晓。

**原文标题**: We’ve had a Denisovan skull since the 1930s, only nobody knew

**原文链接**: [https://arstechnica.com/science/2025/06/the-controversial-dragon-man-skull-was-a-denisovan/](https://arstechnica.com/science/2025/06/the-controversial-dragon-man-skull-was-a-denisovan/)

本文讨论了近期对20世纪30年代在中国发现的哈尔滨头骨的鉴定，该头骨被认为是丹尼索瓦人所有，丹尼索瓦人是一个已灭绝的人科物种，主要通过基因证据为人所知。最初，在2021年，该头骨因其独特的特征组合而被归类为一个新物种，即“龙人”( *Homo longi*)。然而，一项分析头骨中保存的蛋白质的新研究发现，它与已知的丹尼索瓦人化石的特定蛋白质相匹配。

这项发现意义重大，因为它提供了第一个相对完整的丹尼索瓦人面部特征。此前，关于丹尼索瓦人的知识仅限于零碎的骨骼和牙齿。哈尔滨头骨表现出多种特征的混合，有些类似于较早的人科物种，有些更类似于现代人类。它有一个宽阔、扁平的脸，颧骨较小，眼窝较大，眉骨较重，头盖骨长而低，容纳着一个巨大的大脑。

文章强调，哈尔滨头骨只是一个个体，可能无法代表丹尼索瓦人群体的全部多样性，该群体分布范围广泛。此外，虽然该头骨揭示了许多关于面部特征的信息，但它提供的关于整体身体结构或其他身体属性的信息有限。

作者认为，中国先前发现的其他化石，如来自大荔、和龙洞和金牛山洞的化石，可能也属于丹尼索瓦人群体，如果能够从它们中提取出古代 DNA 或蛋白质，则可能会扩展我们对丹尼索瓦人多样性的理解。

---

## 45. 网络编程语言

**原文标题**: Cyber Programming Language

**原文链接**: [https://fubark.github.io/cyber/](https://fubark.github.io/cyber/)

本文档是 Cyber 编程语言的参考手册。 Cyber 是一种快速、高效且并发的脚本语言，支持静态和动态类型。 它涵盖了该语言的类型系统、基本语法、变量、运算符和内置类型。

Cyber 的语法设计简洁易读，使用换行符终止语句（换行除外）。 代码块由缩进定义。 使用 `var` 关键字声明的变量可以是局部变量或静态变量（但静态变量可能会被替换）。 类型约束可以显式定义，变量作用域由代码块决定。

本文档详细介绍了 Cyber 的运算符，包括算术、比较、逻辑和按位运算符。 它还涉及运算符重载。 定义了不同数据类型的零值，类型转换使用 `as` 关键字实现。 注释是单行注释，使用 `--`。

Cyber 包含 CYON，一种类似 JSON 的对象表示法。 本文档还描述了基本数据类型，包括布尔值、整数（byte、int8、int16、int32、int64）、浮点数、字符串（包括原始和常规字面量、转义序列、索引、连接、插值和格式化）、符号和可选类型。 还涵盖了数组、列表、表格和映射等集合。 介绍了用于动态类型的特殊类型 `any` 和 `dyn`。

标记为“未完成”或“计划中”的功能表示正在进行开发，并且该文档反映了该语言，就好像这些功能已经实现一样。

---

## 46. ASASSN-25cm的光谱分类为经典新星

**原文标题**: Spectroscopic Classification of ASASSN-25cm as a Classical Nova

**原文链接**: [https://www.astronomerstelegram.org/?read=17228](https://www.astronomerstelegram.org/?read=17228)

本天文电报(ATel #17228) 报告了对天体ASASSN-25cm (又名AT 2025nlr)的光谱分类，确认为一颗经典新星。 南非天文台和开普敦大学的丹波佑介于2025年6月14.745日（世界时）使用萨瑟兰莱塞迪1米望远镜上的莫科迪摄谱仪获得了该天体的光学光谱。

ASASSN-25cm最初由ASAS-SN巡天于2025年6月12日（世界时）发现，星等为g=8.7。 该天体没有已存档的光度对应体。

丹波获得的光谱显示了巴尔末线（Hα和Hβ）以及He I或Fe II线，均表现出P Cygni轮廓，这是膨胀气体壳的特征。 Hα和Hβ中P Cygni轮廓的吸收最小值表明速度分别约为-1200 km/s和-900 km/s。

基于这些光谱特征，以及该天体显著的爆发幅度，作者得出结论，ASASSN-25cm是一颗新发现的经典新星。 该ATel还引用了GOTO对豺狼座V462 (AT 2025nlr)的相关观测和探测。

---

## 47. 机械表：分解图

**原文标题**: Mechanical Watch: Exploded View

**原文链接**: [https://fellerts.no/projects/epoch.html](https://fellerts.no/projects/epoch.html)

This article details the author's journey to create a physical, exploded view model of a mechanical watch movement, inspired by an interactive online illustration. Dissatisfied with existing "steampunk art" and resin-embedded watch parts, the author embarks on a DIY project, initially facing challenges in resin casting.

The first attempts involved layered resin casting with UV and two-part epoxy, but issues with yellowing, slow curing, visible seams, and bubble formation led to abandoning this method. The author then explores suspending components with fishing line, utilizing CA glue for assembly, a process resembling actual watchmaking.

Experimentation with resin casting continues, focusing on achieving crystal clarity using a vacuum chamber to remove air bubbles. A borosilicate glass cylinder casting fails due to light refraction and shattering caused by resin shrinkage. The author then refines the process, disassembling, cleaning, and assembling a pocket watch movement, using fishing line to suspend parts and CA glue for joining.

The article outlines the assembly process, starting with the train wheel side, then flipping and working on the dial side. A mold made of acrylic sheets is prepared for resin casting. The author details improvements for the next iteration, including using a lab jack for precise assembly, ensuring proper airflow to prevent overheating and shrinkage, increasing the component spacing, and setting the hands to 10:10. Prototype #3 incorporates a lab jack and a magnet on the self-closing tweezers to hold tiny screws.


---

## 48. Show HN: Report idling vehicles in NYC (and get a cut of the fines) with AI

**原文标题**: Show HN: Report idling vehicles in NYC (and get a cut of the fines) with AI

**原文链接**: [https://apps.apple.com/us/app/idle-reporter-for-nyc-dep/id6747315971](https://apps.apple.com/us/app/idle-reporter-for-nyc-dep/id6747315971)

生成摘要时出错

---

## 49. Cross-Account and Cross-Region Backups with AWS Backup (and Friends)

**原文标题**: Cross-Account and Cross-Region Backups with AWS Backup (and Friends)

**原文链接**: [https://tylerrussell.dev/2025/06/20/cross-account-and-region-backups-with-aws-backup-and-friends/](https://tylerrussell.dev/2025/06/20/cross-account-and-region-backups-with-aws-backup-and-friends/)

生成摘要时出错

---

## 50. How fast are Linux pipes anyway?

**原文标题**: How fast are Linux pipes anyway?

**原文链接**: [https://mazzo.li/posts/fast-pipes.html](https://mazzo.li/posts/fast-pipes.html)

生成摘要时出错

---

## 51. Disabling Intel Graphics Security Mitigation Boosts GPU Compute Performance 20%

**原文标题**: Disabling Intel Graphics Security Mitigation Boosts GPU Compute Performance 20%

**原文链接**: [https://www.phoronix.com/news/Disable-Intel-Gfx-Security-20p](https://www.phoronix.com/news/Disable-Intel-Gfx-Security-20p)

生成摘要时出错

---

## 52. Remote MCP Support in Claude Code

**原文标题**: Remote MCP Support in Claude Code

**原文链接**: [https://www.anthropic.com/news/claude-code-remote-mcp?campaignId=13926158&source=i_email&medium=email&content=Oct2024AnalysisTool&messageTypeId=140367](https://www.anthropic.com/news/claude-code-remote-mcp?campaignId=13926158&source=i_email&medium=email&content=Oct2024AnalysisTool&messageTypeId=140367)

生成摘要时出错

---

## 53. Show HN: Luna Rail – Treating night trains as a spatial optimization problem

**原文标题**: Show HN: Luna Rail – Treating night trains as a spatial optimization problem

**原文链接**: [https://luna-rail.com/en/home-2](https://luna-rail.com/en/home-2)

生成摘要时出错

---

## 54. Kilauea volcano errupts, lava more than 1k feet high [video]

**原文标题**: Kilauea volcano errupts, lava more than 1k feet high [video]

**原文链接**: [https://www.youtube.com/watch?v=oG5zz9Sjw3E](https://www.youtube.com/watch?v=oG5zz9Sjw3E)

生成摘要时出错

---

## 55. Hawaii Highways

**原文标题**: Hawaii Highways

**原文链接**: [http://www.hawaiihighways.com/](http://www.hawaiihighways.com/)

生成摘要时出错

---

## 56. Git Notes: Git's coolest, most unloved­ feature (2022)

**原文标题**: Git Notes: Git's coolest, most unloved­ feature (2022)

**原文链接**: [https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/](https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/)

生成摘要时出错

---

## 57. Show HN: Ariadne – A Rust implementation of aperiodic cryptography

**原文标题**: Show HN: Ariadne – A Rust implementation of aperiodic cryptography

**原文链接**: [https://codeberg.org/CipherNomad/Ariadne](https://codeberg.org/CipherNomad/Ariadne)

生成摘要时出错

---

## 58. Using an $8 smart outlet to avoid brainrot

**原文标题**: Using an $8 smart outlet to avoid brainrot

**原文链接**: [https://www.neilchen.co/blog/kasa](https://www.neilchen.co/blog/kasa)

生成摘要时出错

---

## 59. Germany and Italy pressed to bring $245B of gold home from US

**原文标题**: Germany and Italy pressed to bring $245B of gold home from US

**原文链接**: [https://www.ft.com/content/e39390cc-ea02-4197-843a-1e4c242422cc](https://www.ft.com/content/e39390cc-ea02-4197-843a-1e4c242422cc)

生成摘要时出错

---

## 60. Caddy as a Reverse Proxy in Docker

**原文标题**: Caddy as a Reverse Proxy in Docker

**原文链接**: [https://github.com/DoTheEvo/selfhosted-apps-docker/tree/master/caddy_v2](https://github.com/DoTheEvo/selfhosted-apps-docker/tree/master/caddy_v2)

生成摘要时出错

---

## 61. 2025 Alonzo Church Award: Paul Blain Levy for Call-by-Push-Value (CBPV)

**原文标题**: 2025 Alonzo Church Award: Paul Blain Levy for Call-by-Push-Value (CBPV)

**原文链接**: [https://siglog.org/winner-of-the-2025-alonzo-church-award/](https://siglog.org/winner-of-the-2025-alonzo-church-award/)

生成摘要时出错

---

## 62. Largest Wildlife Bridge Spanning 10 Lanes of CA 101 Is Nearly Complete

**原文标题**: Largest Wildlife Bridge Spanning 10 Lanes of CA 101 Is Nearly Complete

**原文链接**: [https://www.thedrive.com/news/worlds-largest-wildlife-bridge-spanning-10-lanes-of-101-freeway-is-nearly-complete](https://www.thedrive.com/news/worlds-largest-wildlife-bridge-spanning-10-lanes-of-101-freeway-is-nearly-complete)

生成摘要时出错

---

## 63. Phoenix.new – Remote AI Runtime for Phoenix

**原文标题**: Phoenix.new – Remote AI Runtime for Phoenix

**原文链接**: [https://fly.io/blog/phoenix-new-the-remote-ai-runtime/](https://fly.io/blog/phoenix-new-the-remote-ai-runtime/)

生成摘要时出错

---

## 64. Low-Temperature Additive Manufacturing of Glass

**原文标题**: Low-Temperature Additive Manufacturing of Glass

**原文链接**: [https://www.ll.mit.edu/research-and-development/advanced-technology/microsystems-prototyping-foundry/low-temperature](https://www.ll.mit.edu/research-and-development/advanced-technology/microsystems-prototyping-foundry/low-temperature)

生成摘要时出错

---

## 65. AGI is Mathematically Impossible 2: When Entropy Returns

**原文标题**: AGI is Mathematically Impossible 2: When Entropy Returns

**原文链接**: [https://philarchive.org/archive/SCHAIM-14](https://philarchive.org/archive/SCHAIM-14)

生成摘要时出错

---

## 66. Otus Lisp

**原文标题**: Otus Lisp

**原文链接**: [https://yuriy-chumak.github.io/ol/](https://yuriy-chumak.github.io/ol/)

生成摘要时出错

---

## 67. LibRedirect – Redirects popular sites to alternative privacy-friendly frontends

**原文标题**: LibRedirect – Redirects popular sites to alternative privacy-friendly frontends

**原文链接**: [https://libredirect.github.io](https://libredirect.github.io)

生成摘要时出错

---

## 68. How to negotiate your salary package

**原文标题**: How to negotiate your salary package

**原文链接**: [https://www.complexsystemspodcast.com/episodes/how-to-negotiate-your-salary-package/](https://www.complexsystemspodcast.com/episodes/how-to-negotiate-your-salary-package/)

生成摘要时出错

---

## 69. Adobe Project Indigo is a new photo app from former Pixel camera engineers

**原文标题**: Adobe Project Indigo is a new photo app from former Pixel camera engineers

**原文链接**: [https://www.engadget.com/apps/adobe-project-indigo-is-a-new-photo-app-from-former-pixel-camera-engineers-213453207.html](https://www.engadget.com/apps/adobe-project-indigo-is-a-new-photo-app-from-former-pixel-camera-engineers-213453207.html)

生成摘要时出错

---

## 70. Show HN: Turn a paper's DOI into its full reference list (BibTeX/RIS, etc.)

**原文标题**: Show HN: Turn a paper's DOI into its full reference list (BibTeX/RIS, etc.)

**原文链接**: [https://references.mireklzicar.com](https://references.mireklzicar.com)

生成摘要时出错

---

## 71. TPU Deep Dive

**原文标题**: TPU Deep Dive

**原文链接**: [https://henryhmko.github.io/posts/tpu/tpu.html](https://henryhmko.github.io/posts/tpu/tpu.html)

生成摘要时出错

---

## 72. Telescopes Are Tries: A Dependent Type Shellac on SQLite

**原文标题**: Telescopes Are Tries: A Dependent Type Shellac on SQLite

**原文链接**: [https://www.philipzucker.com/telescope_tries/](https://www.philipzucker.com/telescope_tries/)

生成摘要时出错

---

## 73. There's Gold in the Hills

**原文标题**: There's Gold in the Hills

**原文链接**: [https://longreads.com/2025/06/12/blm-land-enduring-wild-josh-jackson/](https://longreads.com/2025/06/12/blm-land-enduring-wild-josh-jackson/)

生成摘要时出错

---

## 74. AI's Biggest Threat: Young People Who Can't Think

**原文标题**: AI's Biggest Threat: Young People Who Can't Think

**原文链接**: [https://www.wsj.com/opinion/the-biggest-ai-threat-young-people-who-cant-think-303be1cd](https://www.wsj.com/opinion/the-biggest-ai-threat-young-people-who-cant-think-303be1cd)

生成摘要时出错

---

## 75. Type Inference Zoo

**原文标题**: Type Inference Zoo

**原文链接**: [https://zoo.cuichen.cc/](https://zoo.cuichen.cc/)

生成摘要时出错

---

## 76. I was surprised by how simple an allocator is

**原文标题**: I was surprised by how simple an allocator is

**原文链接**: [https://tgmatos.github.io/allocators-are-for-monkeys-with-typewriters/](https://tgmatos.github.io/allocators-are-for-monkeys-with-typewriters/)

生成摘要时出错

---

## 77. A challenge to Eli Lilly's Tirzepatide patent

**原文标题**: A challenge to Eli Lilly's Tirzepatide patent

**原文链接**: [https://glp1.guide/content/a-challenge-to-eli-lillys-tirzepatide-patent/](https://glp1.guide/content/a-challenge-to-eli-lillys-tirzepatide-patent/)

生成摘要时出错

---

## 78. New York State Plans to Build New Nuclear Power Plant

**原文标题**: New York State Plans to Build New Nuclear Power Plant

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-23/new-york-plans-to-build-nuclear-power-plant-for-1-million-homes](https://www.bloomberg.com/news/articles/2025-06-23/new-york-plans-to-build-nuclear-power-plant-for-1-million-homes)

生成摘要时出错

---

## 79. Our sister died because of our mum's cancer conspiracy theories, say brothers

**原文标题**: Our sister died because of our mum's cancer conspiracy theories, say brothers

**原文链接**: [https://www.bbc.com/news/articles/crenzwyvpn1o](https://www.bbc.com/news/articles/crenzwyvpn1o)

生成摘要时出错

---

## 80. French 'merveilleux-scientifique' fiction reframed reality

**原文标题**: French 'merveilleux-scientifique' fiction reframed reality

**原文链接**: [https://aeon.co/essays/how-french-merveilleux-scientifique-fiction-reframed-reality](https://aeon.co/essays/how-french-merveilleux-scientifique-fiction-reframed-reality)

生成摘要时出错

---

## 81. Requiem for a Solar Plant

**原文标题**: Requiem for a Solar Plant

**原文链接**: [https://7goldfish.com/articles/Requiem_for_a_solar_plant.php](https://7goldfish.com/articles/Requiem_for_a_solar_plant.php)

生成摘要时出错

---

## 82. The Tandy Corporation

**原文标题**: The Tandy Corporation

**原文链接**: [https://www.abortretry.fail/p/the-tandy-corporation-part-1](https://www.abortretry.fail/p/the-tandy-corporation-part-1)

生成摘要时出错

---

## 83. Andrej Karpathy: Software in the era of AI [video]

**原文标题**: Andrej Karpathy: Software in the era of AI [video]

**原文链接**: [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

生成摘要时出错

---

## 84. 'Gwada negative': French scientists find new blood type in woman

**原文标题**: 'Gwada negative': French scientists find new blood type in woman

**原文链接**: [https://www.lemonde.fr/en/science/article/2025/06/21/gwada-negative-french-scientists-find-new-blood-type-in-woman_6742577_10.html](https://www.lemonde.fr/en/science/article/2025/06/21/gwada-negative-french-scientists-find-new-blood-type-in-woman_6742577_10.html)

生成摘要时出错

---

## 85. Show HN: Urpal – An AI-powered productivity canvas for file notes and tasks

**原文标题**: Show HN: Urpal – An AI-powered productivity canvas for file notes and tasks

**原文链接**: [https://urpal.com.au/](https://urpal.com.au/)

生成摘要时出错

---

## 86. Show HN: I'm a doctor and built a responsive breathing app for anxiety and sleep

**原文标题**: Show HN: I'm a doctor and built a responsive breathing app for anxiety and sleep

**原文链接**: [https://apps.apple.com/us/app/lungy-breathing-exercises/id1545223887](https://apps.apple.com/us/app/lungy-breathing-exercises/id1545223887)

生成摘要时出错

---

## 87. Scaling our observability platform by embracing wide events and replacing OTel

**原文标题**: Scaling our observability platform by embracing wide events and replacing OTel

**原文链接**: [https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel](https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel)

生成摘要时出错

---

## 88. Tabiew: A TUI for Viewing and Querying CSV, TSV, JSON, SQLite, and More

**原文标题**: Tabiew: A TUI for Viewing and Querying CSV, TSV, JSON, SQLite, and More

**原文链接**: [https://github.com/shshemi/tabiew](https://github.com/shshemi/tabiew)

生成摘要时出错

---

## 89. Samsung embeds IronSource spyware app on phones across WANA

**原文标题**: Samsung embeds IronSource spyware app on phones across WANA

**原文链接**: [https://smex.org/open-letter-to-samsung-end-forced-israeli-app-installations-in-the-wana-region/](https://smex.org/open-letter-to-samsung-end-forced-israeli-app-installations-in-the-wana-region/)

生成摘要时出错

---

## 90. Bluetooth Jammer

**原文标题**: Bluetooth Jammer

**原文链接**: [https://github.com/EmenstaNougat/ESP32-BlueJammer](https://github.com/EmenstaNougat/ESP32-BlueJammer)

生成摘要时出错

---

## 91. Mbake – A Makefile formatter and linter, that only took 50 years

**原文标题**: Mbake – A Makefile formatter and linter, that only took 50 years

**原文链接**: [https://github.com/EbodShojaei/bake](https://github.com/EbodShojaei/bake)

生成摘要时出错

---

## 92. Dynamic YAML with Python computed properties for fusing API workflows and SQL

**原文标题**: Dynamic YAML with Python computed properties for fusing API workflows and SQL

**原文链接**: [https://sequor.dev/](https://sequor.dev/)

生成摘要时出错

---

## 93. P-Hacking in Startups

**原文标题**: P-Hacking in Startups

**原文链接**: [https://briefer.cloud/blog/posts/p-hacking/](https://briefer.cloud/blog/posts/p-hacking/)

生成摘要时出错

---

## 94. U.S. bombs Iranian nuclear sites

**原文标题**: U.S. bombs Iranian nuclear sites

**原文链接**: [https://www.bbc.co.uk/news/live/ckg3rzj8emjt](https://www.bbc.co.uk/news/live/ckg3rzj8emjt)

生成摘要时出错

---

## 95. RedMonk Top Languages over Time: January 2025

**原文标题**: RedMonk Top Languages over Time: January 2025

**原文链接**: [https://redmonk.com/rstephens/2025/06/18/top20-jan2025/](https://redmonk.com/rstephens/2025/06/18/top20-jan2025/)

生成摘要时出错

---

## 96. AllTracker: Efficient Dense Point Tracking at High Resolution

**原文标题**: AllTracker: Efficient Dense Point Tracking at High Resolution

**原文链接**: [https://alltracker.github.io/](https://alltracker.github.io/)

生成摘要时出错

---

## 97. Sound As Pure Form: Music Language Inspired by Supercollider, APL, and Forth

**原文标题**: Sound As Pure Form: Music Language Inspired by Supercollider, APL, and Forth

**原文链接**: [https://github.com/lfnoise/sapf](https://github.com/lfnoise/sapf)

生成摘要时出错

---

## 98. If you're building a JavaScript library and need logging, you would love LogTape

**原文标题**: If you're building a JavaScript library and need logging, you would love LogTape

**原文链接**: [https://hackers.pub/@hongminhee/2025/logtape-for-libraries](https://hackers.pub/@hongminhee/2025/logtape-for-libraries)

生成摘要时出错

---

## 99. What is the most realistic submarine movie? (2019)

**原文标题**: What is the most realistic submarine movie? (2019)

**原文链接**: [https://www.usni.org/magazines/proceedings/2019/october/what-most-realistic-submarine-movie-ever-made](https://www.usni.org/magazines/proceedings/2019/october/what-most-realistic-submarine-movie-ever-made)

生成摘要时出错

---

## 100. That Revolutionary May Day in 1976 When California Wines Bested France's Finest

**原文标题**: That Revolutionary May Day in 1976 When California Wines Bested France's Finest

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/that-revolutionary-May-day-1976-when-california-wines-bested-france-finest-180958971/](https://www.smithsonianmag.com/smithsonian-institution/that-revolutionary-May-day-1976-when-california-wines-bested-france-finest-180958971/)

生成摘要时出错

---

