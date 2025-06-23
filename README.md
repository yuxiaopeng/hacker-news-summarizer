# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-23.md)

*最后自动更新时间: 2025-06-23 17:52:02*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 2 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 3 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 4 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 5 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 6 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 7 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 8 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 9 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 10 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 11 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 12 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 13 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 14 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 15 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 16 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 17 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 18 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 19 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 20 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 21 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 22 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 23 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 24 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 25 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 26 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 27 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 28 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 29 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 30 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 31 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 32 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 33 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 34 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 35 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 36 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 37 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 38 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 39 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 40 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 41 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 42 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 43 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 44 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 45 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 46 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 47 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 48 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 49 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 50 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 51 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 52 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 53 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 54 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 55 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 56 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 57 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 58 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 59 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 60 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 61 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 62 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 63 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 64 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 65 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 66 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 67 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 68 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 69 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 70 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 71 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 72 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 73 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 74 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 75 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 76 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 77 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 78 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 79 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 80 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 81 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 82 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 83 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 84 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 85 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 86 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 87 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 88 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 89 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 90 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 91 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 92 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 93 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 94 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 95 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 96 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
