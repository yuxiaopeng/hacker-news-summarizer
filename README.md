# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-15.md)

*最后自动更新时间: 2025-10-15 17:47:54*
## 1. 苹果M5芯片

**原文标题**: Apple M5 chip

**原文链接**: [https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)

以下是苹果M5芯片新闻稿的简要总结：

苹果发布M5芯片，基于第三代3纳米技术，是AI性能的重大飞跃。它采用下一代10核GPU，每个核心都带有神经加速器，与M4相比，AI的峰值GPU计算性能提高了4倍以上。M5还拥有高达10核CPU（6个效能核心，最多4个性能核心），提供15%更快的多线程性能，改进的16核神经网络引擎，以及统一内存带宽提高了30%，达到153GB/s。

主要改进包括：

*   **AI焦点：**优化的GPU架构，每个核心都带有神经加速器，可显著加快AI工作负载。
*   **图形性能提升：**第三代光线追踪和增强型着色器核心，图形性能提升高达45%。
*   **更快的神经网络引擎：**改进应用程序中由AI驱动的功能，并增强Apple Intelligence性能。
*   **提高内存带宽：**统一内存架构使更大的AI模型能够在设备上运行。

M5将为新款14英寸MacBook Pro、iPad Pro和Apple Vision Pro提供动力，增强它们在AI、图形和整体性能方面的能力。苹果硬件技术高级副总裁 Johny Srouji 强调了 M5 在提升 Apple 芯片 AI 性能方面的作用。 该版本还强调了苹果公司对可持续发展的承诺，M5 的节能设计有助于公司实现 Apple 2030 碳中和目标。

---

## 2. 攻陷 Nix 生态系统

**原文标题**: Pwning the Nix ecosystem

**原文链接**: [https://ptrpa.ws/nixpkgs-actions-abuse](https://ptrpa.ws/nixpkgs-actions-abuse)

本文详细介绍了一个在 Nix 生态系统的 GitHub Actions 设置中发现的漏洞，具体是在 nixpkgs 内部。该漏洞可能允许攻击者注入恶意代码。作者和一位朋友发现了两个可利用的工作流，这些工作流使用了 `pull_request_target` 触发器，该触发器即使从派生的拉取请求中也能授予读/写访问权限和秘密访问权限。

第一个漏洞涉及 editorconfig 检查器。通过制作包含命令行参数的恶意文件名，攻击者可以由于不安全地使用 `xargs` 而注入命令。

第二个，更严重的漏洞，集中在 CODEOWNERS 文件验证器上。通过将 OWNERS 文件替换为指向运行器上敏感文件（例如，GitHub Actions 凭据文件）的符号链接，攻击者可以强制验证器打印文件的内容，从而有效地泄露具有对 nixpkgs 的写入权限的 GitHub Actions 令牌。这允许直接提交，绕过审查流程。

这些漏洞已被迅速报告，并且 nixpkgs 维护者已修复了这些漏洞，他们禁用了易受攻击的工作流，正确地分离了不受信任的数据，并重命名了已修复的工作流。本文强调了将不受信任的用户输入与特权操作混合的危险性，强调了理解 GitHub Actions 权限的重要性，并为保护 GitHub Actions 工作流提供了建议。作者将他们的知识归功于之前关于 GitHub Actions 安全性的研究和演讲，并鼓励读者探索其他资源以了解更多信息。

---

## 3. 我差点被“求职面试”给黑了。

**原文标题**: I almost got hacked by a 'job interview'

**原文链接**: [https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview](https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview)

文章“我差点被‘求职面试’入侵”详细描述了作者差点成为一个伪装成工作机会的复杂网络钓鱼诈骗受害者的经历。作者是一位软件工程师，收到了一条来自一位自称招聘人员的未经请求的 LinkedIn 消息，该消息提供了一家合法（但很可能被冒充）的科技公司的工作职位。

面试过程起初看起来很标准，包括最初的电话筛选，然后是技术任务。然而，“技术任务”是诈骗的核心。它要求作者克隆一个看似合法的 GitHub 仓库，并在他们的机器上本地运行一个脚本。

至关重要的是，作者注意到该脚本发出了可疑的网络活动。经过仔细检查，他们发现该脚本旨在从他们的计算机中提取敏感信息，如 SSH 密钥、.git 配置文件和其他凭证。然后，该脚本会将这些数据发送到攻击者控制的远程服务器。

作者立即停止了脚本，删除了仓库，并通过更改密码和轮换 SSH 密钥来保护他们的帐户安全。这篇文章强调了诈骗的复杂性，强调了攻击者为了使其看起来合法而付出的努力，包括冒充一家真实的公司和一个合法的招聘人员档案。

作者最后敦促读者对未经请求的工作机会保持极其谨慎的态度，尤其是那些要求他们在个人设备上运行未知代码的工作机会，并且在执行脚本之前始终要仔细检查脚本是否存在可疑活动。他们还建议使用容器化或虚拟机来运行不受信任的代码，作为一种安全措施。

---

## 4. Mac 源代码移植 – 在新 Mac 上运行旧游戏

**原文标题**: Mac Source Ports – Run old games on new Macs

**原文链接**: [https://www.macsourceports.com/](https://www.macsourceports.com/)

本文介绍了“Mac Source Ports”网站，该网站致力于提供经典游戏源代码移植的本地应用程序构建版本，使用户能够在现代 Apple Silicon 和 Intel Mac 上畅玩这些游戏。这些构建版本通常经过签名和公证，以确保安全性。

该网站提供了一个游戏目录，目前展示了 167 款游戏，列表包括游戏的开发者、发布日期、简要描述和源代码移植详情。每个列表通常包含有关所使用的源代码移植、兼容性（Apple Silicon、Intel 等）、是否为完整游戏、其签名/公证状态以及下载链接的信息。还提供安装说明，通常涉及将原始游戏安装中的数据文件复制到特定目录中。

精选游戏示例包括 Carmageddon（使用 Dethrace 源代码移植）、Warzone 2100（完整游戏）、重返德军总部 (Return to Castle Wolfenstein)（使用 iortcw）、雷神之锤 II (Quake II)（使用 Yamagi Quake II）、魔法门英雄无敌 II (Heroes of Might and Magic II)（使用 fheroes2）、过山车大亨 2 (RollerCoaster Tycoon 2)（使用 OpenRCT2）、爵士兔 2 (Jazz Jackrabbit 2)（使用 Jazz² Resurrection）、琥珀月亮 (Ambermoon)（使用 Ambermoon.net）以及马拉松三部曲 (Marathon trilogy)（使用 Aleph One）。这些列表通常提供在 GOG.com 或 Humble Store 上购买游戏的链接，并提及使用提取实用程序来获取数据文件。该网站还使用标签按流派、主题和其他相关关键词对游戏进行分类。

---

## 5. Show HN: Halloy – 现代 IRC 客户端

**原文标题**: Show HN: Halloy – Modern IRC client

**原文链接**: [https://github.com/squidowl/halloy](https://github.com/squidowl/halloy)

Halloy：一款现代、开源的IRC客户端，使用Rust和Iced GUI库编写，专为Mac、Windows和Linux平台的速度和简洁性而设计。它支持IRCv3.2功能，包括帐户通知、SASL和消息标签等。用户可以通过提供的文档链接、Flathub或Snap Store安装Halloy。

主要功能包括DCC发送、键盘快捷键、昵称/命令/频道自动补全、通知、跨服务器的多频道支持、命令栏、自定义主题和便携模式。

Halloy基于GPL-3.0协议授权。如需支持，用户可以加入libera.chat上的#halloy频道，或在GitHub存储库上提交问题。最新版本和主分支均提供文档，方便从源代码安装的用户。

---

## 6. Show HN: Scriber Pro – macOS 离线 AI 语音转文字

**原文标题**: Show HN: Scriber Pro – Offline AI transcription for macOS

**原文链接**: [https://scriberpro.cc/hn/](https://scriberpro.cc/hn/)

Scriber Pro 是一款 macOS 应用程序，用于对音频和视频文件进行离线 AI 转录。它拥有比 Rev 和 Otter 等在线服务更快的转录速度，仅需 3.5 分钟即可转录一个 4.5 小时的视频。其主要优势在于离线功能，可确保数据隐私，因为所有处理都在用户的 Mac 本地进行，消除了云上传和监控方面的担忧。

该应用程序支持多种音频和视频格式（MP3、WAV、MP4、MOV、M4A、FLAC），并提供准确的时间码，无论文件长度如何。Scriber Pro 提供灵活的导出选项，包括 SRT、VTT 和 JSON 等时间码格式，PDF、DOCX、TXT 和 Markdown 等文档格式，以及 CSV 和 JSON 等数据格式。

该应用程序可在 Mac App Store 下载。由于需求旺盛，最初的 HN 促销代码已全部申领完毕。

---

## 7. 内核栈释放后使用漏洞：利用英伟达 GPU Linux 驱动

**原文标题**: A kernel stack use-after-free: Exploiting Nvidia's GPU Linux drivers

**原文链接**: [https://blog.quarkslab.com/./nvidia_gpu_kernel_vmalloc_exploit.html](https://blog.quarkslab.com/./nvidia_gpu_kernel_vmalloc_exploit.html)

本文详细介绍了 NVIDIA Linux Open GPU Kernel Modules 中的两个漏洞，具体位于 `nvidia.ko` 和 `nvidia-uvm.ko` 中，本地非特权进程可以利用这些漏洞。这些漏洞被标识为 CVE-2025-23300 和 CVE-2025-23280，允许进行内核读写操作。

CVE-2025-23300 是 `nvidia-uvm` 模块中的一个空指针解引用漏洞，由于在使用带有 `NV01_MEMORY_DEVICELESS` 内存的 `UVM_MAP_EXTERNAL_ALLOCATION` ioctl 时，未检查 `MEMORY_DESCRIPTOR` 结构中的 `pGpu` 字段而导致。NVIDIA 通过在 `dupMemory` 中添加检查来跳过对无设备内存需要有效 GPU 上下文的操作，从而修复了此问题。

CVE-2025-23280 是一个 use-after-free (UAF) 漏洞，存在于 `nvidia` 模块中的 `threadStateInit()` 和 `threadStateFree()` 函数中。由于 `THREAD_STATE_NODE` 结构是在栈上分配的，如果在这两个函数调用之间发生内核 oops（如 bug #1 触发），内核栈会被释放，从而在全球红黑树中留下一个无效指针。当稍后访问释放的栈时，例如在打开 `/dev/nvidia0` 时，会导致 UAF。NVIDIA 通过引入基于堆的 `threadStateAlloc` 函数来解决这个问题，但尚未在所有地方使用。

然后，本文深入探讨了 CVE-2025-23280 的利用，重点是操纵 vmalloc 以回收 UAF 内存。该漏洞利用使用 fork、Video4Linux2 (v4l2) 缓冲区和副作用清除来控制 vmalloc 区域，并将 UAF 地址与 v4l2 缓冲区重叠。通过控制 UAF 内存，攻击者可以操纵红黑树数据结构，从而有可能实现内核读/写原语。

---

## 8. 克劳德俳句4.5

**原文标题**: Claude Haiku 4.5

**原文链接**: [https://www.anthropic.com/news/claude-haiku-4-5](https://www.anthropic.com/news/claude-haiku-4-5)

Claude Haiku 4.5 发布：Anthropic 最新小型模型，兼具卓越性价比和速度。

---

## 9. 重塑 Canon Cat 文档界面

**原文标题**: Recreating the Canon Cat document interface

**原文链接**: [https://lab.alexanderobenauer.com/updates/the-jasper-report](https://lab.alexanderobenauer.com/updates/the-jasper-report)

亚历山大·奥本诺尔详述了他用名为 Jasper 的 Web 应用重现佳能猫独特文档界面的经验。佳能猫的特点是以键盘为中心，没有 WIMP 环境，围绕着一个长文本流，主要使用“跳跃键”进行导航，这使得用户可以“瞬移”到键入模式的实例。这促进了用户自定义的导航和组织约定，有效地将环境变成了一个个性化的系统。

奥本诺尔实现了跳跃键（在 Jasper 中使用 option 键）、循环搜索、光标回弹以及类似于佳能猫基于字符的标尺的固定宽度编辑器等关键功能。他强调了这个系统的优势，包括其简单的数据模型，对用户约定的依赖以实现自定义，以及能够手动对条目进行时间戳和排序的“正确性”。

奥本诺尔发现跳跃键非常直观，并欣赏该系统对自由联想思维的支持，类似于他在 Obsidian 中使用单个长文档的方式。他使用 Jasper 在会议期间记录笔记、记录零星的想法并记录有趣的链接。

他还讨论了潜在的扩展，例如将用户约定编码到类似于佳能猫的“CALC”键功能或 Archy 的用户程序的自定义程序中，从而模糊文本和系统命令之间的界限。

---

## 10. 打破“可证明正确”的 Leftpad

**原文标题**: Breaking "provably correct" Leftpad

**原文链接**: [https://lukeplant.me.uk/blog/posts/breaking-provably-correct-leftpad/](https://lukeplant.me.uk/blog/posts/breaking-provably-correct-leftpad/)

本文探讨了正式验证“正确”代码的挑战，并以经典的“Leftpad”函数为例。尽管使用Haskell、Java、Lean和Rust等语言的正式方法证明了几个实现的“可证明的正确性”，但作者证明了它们在处理Unicode字符串时输出的不一致性。

核心问题在于处理Unicode复杂的字符表示（代码点、组合字符、字形簇和编码（UTF-8、UTF-16））时，对“字符串长度”的不同解释。 各种语言对这些方面的处理方式不同，导致它们衡量字符串长度的方式以及它们应用填充的方式有所不同。

例如，Java使用UTF-16，错误地计算了基本多文种平面（BMP）之外的字符（如高音谱号）的长度，导致填充不足。 类似地，计算代码点而不是字形簇的语言错误地计算了包含组合字符或复杂脚本（如希伯来语）的字符串的长度。

作者将“可证明的正确”实现与一个使用字形簇的简单“感觉编码”的Swift实现进行了对比，该实现可以在固定宽度的上下文中产生预期的视觉对齐效果。 本文认为，虽然形式验证确保代码满足特定规范，但这些规范可能无法捕获预期行为或自然语言需求（如“字符串长度”）的复杂性。 它突出了形式上的正确性与现实世界的可用性之间的差距，尤其是在处理Unicode的细微方面时。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 2 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 3 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 4 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 5 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 6 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 7 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 8 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 9 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 10 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 11 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 12 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 13 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 14 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 15 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 16 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 17 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 18 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 19 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 20 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 21 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 22 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 23 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 24 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 25 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 26 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 27 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 28 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 29 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 30 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 31 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 32 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 33 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 34 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 35 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 36 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 37 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 38 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 39 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 40 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 41 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 42 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 43 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 44 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 45 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 46 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 47 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 48 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 49 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 50 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 51 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 52 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 53 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 54 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 55 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 56 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 57 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 58 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 59 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 60 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 61 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 62 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 63 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 64 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 65 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 66 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 67 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 68 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 69 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 70 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 71 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 72 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 73 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 74 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 75 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 76 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 77 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 78 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 79 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 80 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 81 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 82 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 83 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 84 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 85 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 86 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 87 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 88 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 89 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 90 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 91 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 92 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 93 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 94 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 95 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 96 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 97 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 98 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 99 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 100 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 101 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 102 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 103 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 104 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 105 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 106 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 107 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 108 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 109 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 110 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 111 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 112 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 113 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 114 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 115 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 116 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 117 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 118 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 119 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 120 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 121 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 122 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 123 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 124 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 125 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 126 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 127 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 128 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 129 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 130 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 131 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 132 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 133 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 134 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 135 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 136 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 137 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 138 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 139 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 140 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 141 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 142 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 143 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 144 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 145 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 146 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 147 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 148 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 149 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 150 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 151 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 152 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 153 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 154 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 155 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 156 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 157 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 158 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 159 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 160 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 161 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 162 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 163 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 164 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 165 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 166 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 167 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 168 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 169 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 170 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 171 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 172 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 173 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 174 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 175 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 176 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 177 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 178 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 179 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 180 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 181 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 182 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 183 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 184 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 185 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 186 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 187 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 188 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 189 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 190 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 191 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 192 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 193 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 194 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 195 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 196 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 197 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 198 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 199 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 200 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 201 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 202 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 203 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 204 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 205 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 206 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 207 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 208 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 209 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 210 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
