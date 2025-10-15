# Hacker News 热门文章摘要 (2025-10-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 使用 RTL SDR 逆向工程 27MHz 遥控玩具通信

**原文标题**: Reverse engineering a 27MHz RC toy communication using RTL SDR

**原文链接**: [https://nitrojacob.wordpress.com/2025/09/03/reverse-engineering-a-27mhz-rc-toy-communication-using-rtl-sdr/](https://nitrojacob.wordpress.com/2025/09/03/reverse-engineering-a-27mhz-rc-toy-communication-using-rtl-sdr/)

本文详细介绍了使用 RTL-SDR 和 GNU Radio 对 27MHz 遥控消防车通信协议进行逆向工程的过程。作者 Jacob 旨在用笔记本电脑控制该玩具。

该过程始于确定精确频率（27.1MHz）并使用瀑布图可视化信号。通过观察时域，确定调制方案为幅度键控 (ASK)。使用 AM 解调模块以及 AGC2 和抽取 FIR 滤波器模块来解调 ASK 信号。添加低通滤波器以降低音频输出的采样率。

对解调信号的分析揭示了重复的 1 和 0 序列，不同的遥控器按键由高频（1010...）区域的长度编码。然后实现符号同步块进行降采样。创建一个自定义 Python 块来关联数据流、识别帧起始位置并计算它们之间的距离（帧长度）。

作者遇到了一个问题，由于 GNU Radio 中缓冲区大小较小，某些按键无法被检测到。通过实现流到向量和向量到流块来将多个块聚合为一个更大的块，然后在处理之前，解决了这个问题。

最后，作者整理了一个表格，将按键组合映射到帧长度和数据长度，从而凭经验确定遥控玩具如何编码其命令。本文提供了 GNU Radio 流程图的框图，并包含一个视频教程。

---

## 12. M5 MacBook Pro

**原文标题**: M5 MacBook Pro

**原文链接**: [https://www.apple.com/macbook-pro/](https://www.apple.com/macbook-pro/)

新款M5 MacBook Pro现已开启预订，将于10月22日起发货，搭载M5、M4 Pro和M4 Max芯片，性能显著提升。这些芯片提供更高的CPU和统一内存速度，是强大的AI任务平台。电池续航时间长达24小时。该设备采用macOS Tahoe系统，具有Liquid Glass设计和直观的工具，以及带有实时活动的新Phone应用程序。

14英寸型号可选配M5、M4 Pro或M4 Max芯片，而16英寸型号则提供M4 Pro或M4 Max。有深空黑和银色两种颜色。Liquid Retina XDR显示屏提供高达1600尼特的峰值亮度和1,000,000:1的对比度。连接选项包括Thunderbolt 4/5端口、HDMI、MagSafe 3、SDXC卡插槽和耳机插孔。

与前几代产品相比，M5芯片系列在AI任务、游戏和专业应用方面实现了显著的速度提升。M4 Pro以更强大的功能满足科学家、工程师和创意专业人士的需求。M4 Max专为3D VFX、AI开发和电影合成等极端工作负载而设计。新款笔记本电脑采用100%再生铝制造。该笔记本电脑还将配备Apple Intelligence，提供专注于写作、表达自我和轻松完成任务的功能。

---

## 13. C++26：std::optional 的范围支持

**原文标题**: C++26: range support for std:optional

**原文链接**: [https://www.sandordargo.com/blog/2025/10/08/cpp26-range-support-for-std-optional](https://www.sandordargo.com/blog/2025/10/08/cpp26-range-support-for-std-optional)

本文探讨了在C++26中为`std::optional`添加范围支持。起初，作者觉得这个概念很奇怪，但深入研究后理解了它的价值。主要优势在于与范围管道的无缝集成，允许跳过缺失的可选值，而无需显式的空值检查。

作者用P3168R2中的一个例子来说明，`std::optional`作为范围消除了范围转换中手动`if`检查的需要。这种集成有效地将`std::optional`视为最多包含一个元素的视图。

本文还强调了一个竞争提案，涉及`views::maybe`和`views::nullable`，但最终被否决，转而采用更简单的方法，即将`std::optional`作为视图。这是通过专门化`std::ranges::enable_view<std::optional<T>>`实现的。虽然最初考虑过，但继承自`std::ranges::view_interface`被认为是不必要的。

该实现仅为`std::optional`引入了`iterator`和`const_iterator`，将其具体实现定义为未定义，以防止潜在的误用。作者总结说，这种增强虽然起初令人困惑，但提供了一种在基于范围的代码中组合可选值的强大方法，简化了复杂的操作并避免了手动分支。

---

## 14. Apple Vision Pro升级采用M5芯片

**原文标题**: Apple Vision Pro upgraded with M5 chip

**原文链接**: [https://www.apple.com/newsroom/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/](https://www.apple.com/newsroom/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/)

以下是苹果Vision Pro升级公告的简要总结：

苹果发布了升级版Apple Vision Pro，采用全新、更强大的M5芯片和重新设计的双编织带，以增强舒适度。 M5芯片带来了显著的性能提升，包括更快的处理速度、更好的显示渲染（像素增加10%）、改进的AI功能（速度提升50%）以及更长的电池续航时间（一般使用长达2.5小时，视频播放3小时）。

双编织带提供更好的缓冲、透气性和稳定性，并有多种尺寸可供选择。 该设备还引入了visionOS 26，解锁了新的空间体验，包括小部件、增强的Personas、交互式木星环境以及新的Apple Intelligence功能。

更新后的Vision Pro拥有超过100万个应用程序、数千款游戏以及不断增长的Apple沉浸式内容库，包括新的剧集、电影，以及即将推出的NBA直播比赛。 正在开发新的应用程序，以利用该设备的功能，包括使用设备端AI的企业解决方案。 该设备还支持来自运动相机的180/360/广角视频拍摄和播放。

增强的功能使消费者和专业人士都受益，在设计、教育、医疗保健和其他行业中涌现出新的用例。 该设备还具有环保意识，采用回收材料并为节能而设计。

部分国家/地区已开始接受预订，Apple Store将于10月22日开始发售。 起价为3,499美元（美国）。

---

## 15. 放弃无服务器架构带来了性能提升和架构简化。

**原文标题**: Leaving serverless led to performance improvement and a simplified architecture

**原文链接**: [https://www.unkey.com/blog/serverless-exit](https://www.unkey.com/blog/serverless-exit)

好的，这是基于我*假设*文章中包含的信息的摘要，考虑到标题为“离开Serverless带来性能提升和架构简化”以及URL `https://www.unkey.com/blog/serverless-exit`。由于我无法访问实际文章，这只是对文章*可能*包含内容的逻辑推断。

**摘要（假设逻辑内容）：**

文章可能讨论了Unkey决定放弃serverless架构以及他们所获得的积极成果。它可能详细描述了他们在serverless使用过程中面临的具体挑战，这些挑战可能包括性能瓶颈、冷启动以及调试和监控方面的复杂性增加。这些挑战可能超过了serverless带来的预期好处，例如自动扩展和降低运营开销（至少在Unkey的特定用例中）。

文章可能解释了Unkey在放弃serverless后采用了什么替代架构，这可能涉及使用专用服务器、容器或虚拟机。作者随后强调了这种转变如何带来性能提升，这可能是由于更好地控制资源、减少延迟以及消除冷启动。

此外，文章可能讨论了他们整体架构的简化。Serverless虽然提供了好处，但有时会导致更复杂的架构，包括分布式函数和事件驱动的工作流程。通过放弃serverless，Unkey可能实现了一个更直接且更易于管理的系统。这篇博客文章可能以对他们经验的总结作为结尾，建议读者根据其特定需求和情况，仔细评估serverless和更传统架构之间的权衡。他们可能强调serverless不是一种万能的解决方案。

---

## 16. Rust 的垃圾回收：终结器的前沿

**原文标题**: Garbage collection for Rust: The finalizer frontier

**原文链接**: [https://soft-dev.org/pubs/html/hughes_tratt__garbage_collection_for_rust_the_finalizer_frontier/](https://soft-dev.org/pubs/html/hughes_tratt__garbage_collection_for_rust_the_finalizer_frontier/)

本文摘录探讨了在 Rust 中使用标准引用计数类型 `Rc<T>` 实现类似垃圾回收功能所面临的挑战。虽然 `Rc<T>` 提供了内存管理，但当创建循环图时，它可能会导致内存泄漏。为了缓解这种情况，摘录使用了图中节点之间的弱引用（`Weak<T>`）来打破循环。

主要观点是，与具有内置垃圾回收的系统相比，为此目的使用 `Rc<T>` 和 `Weak<T>` 引入了显著的复杂性。 摘录特别强调了需要手动将 `Rc<T>` 降级为 `Weak<T>`，然后再将其升级回 `Rc<T>` 才能访问相邻节点。 这一过程可能失败，这使得代码比可以直接访问邻居的更简单的解决方案（如与“Listing 1”的比较所暗示的）更复杂且更难阅读。

本质上，本文认为，虽然 Rust 提供了管理内存和防止泄漏的工具，但使用 `Rc<T>` 和 `Weak<T>` 手动实现类似于垃圾回收的功能可能很麻烦，并会给代码增加相当大的复杂性。

---

## 17. 机器人越来越擅长模仿互动。

**原文标题**: Bots are getting good at mimicking engagement

**原文链接**: [https://joindatacops.com/resources/how-73-of-your-e-commerce-visitors-could-be-fake](https://joindatacops.com/resources/how-73-of-your-e-commerce-visitors-could-be-fake)

无法访问文章链接。

---

## 18. 美国人对台球的热爱为合成塑料铺平了道路

**原文标题**: Americans' love of billiards paved the way for synthetic plastics

**原文链接**: [https://invention.si.edu/invention-stories/imitation-ivory-and-power-play](https://invention.si.edu/invention-stories/imitation-ivory-and-power-play)

19世纪台球的流行如何促成首个商业化合成塑料赛璐珞的发明，进而对现代生活产生深远影响。随着台球成为一项普及的消遣活动，象牙台球的需求激增，引发了人们对大象数量减少和材料成本高昂的担忧。台球界的重要人物迈克尔·费兰甚至悬赏寻找合适的象牙替代品。

印刷工约翰·韦斯利·海厄特响应了这一号召，在最初的失败之后，意外发现了由硝化纤维素衍生的火棉胶制造耐用材料的潜力。经过多年的实验，他将其与樟脑油结合，创造出一种可塑、可染色的物质，并命名为赛璐珞。虽然赛璐珞台球因偶尔的易燃性而褒贬不一，但这种材料在其他应用中证明了其革命性。

海厄特的公司宣称赛璐珞是缓解大象和海龟等自然资源压力的途径。它很快被应用于大规模生产胸衣扣、梳子、钢琴键，以及至关重要的照相胶片和早期电影胶片等产品。尽管赛璐珞在很大程度上已被后来的合成塑料所取代，但它作为首个商业上成功的塑料的遗产仍然意义重大，表明了对更好台球比赛的渴望如何为20世纪和21世纪塑料的广泛使用铺平了道路。

---

## 19. 像素劫持攻击

**原文标题**: Pixnapping Attack

**原文链接**: [https://www.pixnapping.com/](https://www.pixnapping.com/)

Pixnapping：一种新型攻击，无需任何权限即可窃取安卓设备上其他应用或网站显示的敏感信息。它利用安卓API和一个名为GPU.zip的硬件侧信道，影响大多数现代安卓设备。

该攻击包含三个步骤：调用目标应用渲染敏感信息，诱导对敏感像素进行图形操作（使用安卓的窗口模糊API），并利用GPU.zip侧信道逐个窃取这些像素，通过OCR重建信息。易受攻击的数据包括聊天信息、双因素认证代码和电子邮件内容。

Pixnapping已在谷歌和三星手机上得到演示，成功提取了Gmail、谷歌验证器、Signal、Venmo和谷歌地图的数据。值得注意的是，它可以在不到30秒的时间内从谷歌验证器中窃取双因素认证代码，且能对用户隐藏攻击行为。

虽然谷歌最初发布了补丁，但发现了一种绕过方法，使其失效。截至2025年10月，GPU供应商尚未承诺修复GPU.zip漏洞。建议用户及时安装安全补丁，而开发者目前缺乏缓解策略。该漏洞的追踪编号为CVE-2025-48561。该研究还发现了一个“应用列表绕过”漏洞，允许应用程序通过确定已安装的应用程序来分析用户，谷歌不打算修复此漏洞。

---

## 20. 人力资源管理在高级推理能力与通用人工智能上的隐藏驱动因素

**原文标题**: Hidden drivers of HRM's performance on ARC-AGI

**原文链接**: [https://arcprize.org/blog/hrm-analysis](https://arcprize.org/blog/hrm-analysis)

本文分析了分层推理模型 (HRM) 在 ARC-AGI 基准测试上的表现，重点在于识别其成功的关键驱动因素。虽然原始论文强调了受大脑启发的层级架构，但本次分析揭示了令人惊讶的见解。

该团队验证了 HRM 因其小尺寸而展现出的卓越性能（ARC-AGI-1 上达到 32%）。 然而，消融研究表明，“分层”架构本身对性能的贡献微乎其微。 同样大小的 Transformer 模型也取得了相当的结果。

最重要的性能驱动因素是“外循环”细化过程，即模型迭代地细化其预测。 在训练期间增加细化循环的数量显著提高了性能。 虽然自适应计算时间 (ACT) 提高了性能，但它并没有比固定循环次数好多少。 事实证明，使用更多的细化循环进行训练比在推理期间广泛使用它们更重要。

跨任务迁移学习的影响有限。 仅在评估任务上训练模型（没有标准的 ARC-AGI-1 训练集或 ConceptARC 数据）只会导致性能略有下降。 这表明 HRM 主要记忆特定评估任务的解决方案，使其类似于“零预训练测试时训练”方法。

本质上，该研究表明，HRM 的成功与其说是其分层架构，不如说是迭代细化过程和对评估任务的记忆。

---

## 21. 大卫·伯恩电台

**原文标题**: David Byrne Radio

**原文链接**: [https://www.davidbyrne.com/radio#filter=all&sortby=date:desc](https://www.davidbyrne.com/radio#filter=all&sortby=date:desc)

所提供的文本描述了“大卫·伯恩电台”，特别突出了一个名为“十月电台”的部分，其中似乎有一个名为“最近又听”的定期节目。主要功能是允许用户收听此内容，通过“弹出播放”选项体现。还有一个“更多信息”按钮，表明有关于节目的更多细节可用。“关闭”按钮表明用户可以关闭此特定窗口或演示文稿。

本质上，该内容宣传或介绍了一个由大卫·伯恩策划的名为“最近又听”的电台节目，它是“大卫·伯恩电台”中更大的“十月电台”部分的一部分。鼓励用户通过弹出播放器收听，并可以找到有关该节目的更多信息。

---

## 22. 搭载M5芯片的iPad Pro

**原文标题**: iPad Pro with M5 chip

**原文链接**: [https://www.apple.com/newsroom/2025/10/apple-introduces-the-powerful-new-ipad-pro-with-the-m5-chip/](https://www.apple.com/newsroom/2025/10/apple-introduces-the-powerful-new-ipad-pro-with-the-m5-chip/)

以下是搭载M5芯片的iPad Pro发布的简要概述：

苹果发布了新款iPad Pro，搭载M5芯片，承诺在AI性能、图形处理和整体速度方面取得显著进步。M5芯片拥有下一代GPU，每个核心都有一个神经加速器，从而使AI性能比M4快3.5倍，比M1 iPad Pro快5.6倍。它还在3D渲染、视频转码以及应用程序中的AI相关任务方面带来了显著的改进。

新款iPad Pro的存储速度提高了2倍，统一内存增加（某些型号高达12GB），并且内存带宽更快，从而实现更流畅的多任务处理。蜂窝网络型号采用了苹果设计的新C1X调制解调器，蜂窝数据性能提高了50％，而N1芯片支持Wi-Fi 7、蓝牙6和Thread。

iPad Pro有11英寸和13英寸两种尺寸，颜色有深空黑和银色，配备了采用串联OLED技术的超视网膜XDR显示屏，可提供出色的亮度和对比度。13英寸型号非常纤薄，仅为5.1毫米。iPadOS 26引入了重新设计的界面、用于多任务处理的新窗口系统、增强的文件应用程序和用于PDF编辑的预览应用程序。Apple Intelligence功能也集成在整个操作系统中。

Apple Pencil Pro、Apple Pencil (USB-C) 和妙控键盘等配件进一步增强了iPad Pro的功能。新款iPad Pro体现了苹果对可持续发展的承诺，在制造过程中使用了回收材料和可再生能源。现已开放预购，将于10月22日开始发售。11英寸Wi-Fi型号的起价为999美元，13英寸Wi-Fi型号的起价为1299美元。

---

## 23. 爱尔兰将艺术家基本收入计划永久化

**原文标题**: Ireland is making basic income for artists program permanent

**原文链接**: [https://www.artnews.com/art-news/news/ireland-basic-income-artists-program-permanent-1234756981/](https://www.artnews.com/art-news/news/ireland-basic-income-artists-program-permanent-1234756981/)

爱尔兰将于2026年起永久实施艺术家基本收入计划(BIA)，每周向2000名选定艺术家提供约375美元。该计划于2022年启动，旨在作为一项试点，以支持疫情后收入损失的艺术行业，将于2026年9月开放申请。

Alma Economics最近的一份报告发现，耗资7200万欧元的试点计划为爱尔兰经济带来了近8000万欧元的效益。受益者的艺术相关收入有所增加，对其他社会项目的依赖有所减少。该报告还预测，一项永久性的、规模扩大的计划将提高艺术家的产量，并降低消费者的艺术品成本。

公众舆论普遍支持该计划，97%的受访者表示赞成。然而，对于选择标准的偏好各不相同，大多数人倾向于经济需求或价值，而不是随机选择。

艺术家基本收入计划(BIA)是一种普遍基本收入(UBI)的形式，在人们对技术驱动型失业感到担忧之际，受到了广泛关注。倡导者援引爱尔兰的计划作为普遍基本收入潜力的证据，敦促更广泛地实施该计划，以应对社会和经济挑战。

---

## 24. FSF宣布Librephone项目

**原文标题**: FSF announces Librephone project

**原文链接**: [https://www.fsf.org/news/librephone-project](https://www.fsf.org/news/librephone-project)

自由软件基金会宣布“自由手机”项目

---

## 25. 扑翼机器人通过采用可重构机构实现自主起飞

**原文标题**: Flapping-wing robot achieves self-takeoff by adopting reconfigurable mechanisms

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adx0465](https://www.science.org/doi/10.1126/sciadv.adx0465)

无法访问文章链接。

---

## 26. 展示HN：Firm，一个基于文本的工作管理系统

**原文标题**: Show HN: Firm, a text-based work management system

**原文链接**: [https://github.com/42futures/firm](https://github.com/42futures/firm)

Firm：面向技术人员的文本化工作管理系统，旨在为希望统一管理并进行版本控制的业务数据提供解决方案。它代表一种“业务即代码”的方法，允许用户使用 Firm DSL 以纯文本文件定义组织、联系人、项目及其关系。这种结构化的表示使业务数据既可供人类读取，也可供人工智能读取。

主要功能包括：将业务信息整合于一处，以纯文本文件形式拥有您的数据，使用模式自定义数据模型，通过代码自动执行任务，以及为人工智能交互准备数据。

用户通过 CLI 与 Firm 交互，从而能够添加、列出和查询实体。实体是具有唯一 ID、类型和字段的基本对象，可以是字符串、整数、布尔值、货币、日期时间、列表、对其他实体的引用或文件路径。实体之间的关系通过引用建立，系统构建实体图以方便遍历和查询。

Firm 基于 Rust 构建，由三个主要 crate 组成：`firm_core`（核心数据结构和图操作）、`firm_lang`（DSL 解析和生成）和 `firm_cli`（命令行界面）。它利用 REA 模型和 Schema.org 原则来实现灵活高效的实体分类。用户还可以使用 `firm_core` 和 `firm_lang` Rust 包将 Firm 的核心逻辑集成到他们自己的软件中。

---

## 27. 美国司法部查封柬埔寨“杀猪盘”骗局中的150亿美元比特币

**原文标题**: DOJ seizes $15B in Bitcoin from 'pig butchering' scam based in Cambodia

**原文链接**: [https://www.cnbc.com/2025/10/14/bitcoin-doj-chen-zhi-pig-butchering-scam.html](https://www.cnbc.com/2025/10/14/bitcoin-doj-chen-zhi-pig-butchering-scam.html)

美国司法部已查获价值150亿美元的比特币，这是其历史上最大规模的没收行动，与柬埔寨境内一个大规模“杀猪盘”诈骗活动有关。据称主谋陈志，太子集团创始人，被指控犯有电汇诈骗和洗钱阴谋罪，如果罪名成立，将面临最高40年的监禁。他目前仍然在逃。

太子集团是一家跨国商业集团，被指控在柬埔寨运营10个诈骗园区，在那里被贩运的人被迫实施加密货币投资诈骗，目标是包括美国在内的全球受害者。这些“杀猪盘”诈骗涉及在网上与受害者建立信任，然后在有利可图的加密货币投资的幌子下窃取他们的资金。

财政部已将太子集团指定为跨国犯罪组织，并制裁了陈志以及100多名相关个人和实体。检察官指控陈志及其高管利用政治影响力和贿赂来保护他们的犯罪企业。该诈骗涉及数百名被贩运并被迫在园区工作，经常受到暴力威胁的受害者。

---

## 28. 欧洲数字主权悖论——“聊天监控”更新

**原文标题**: Europe's Digital Sovereignty Paradox – "Chat Control" Update

**原文链接**: [https://www.process-one.net/blog/chat-control-update-oct-2025/](https://www.process-one.net/blog/chat-control-update-oct-2025/)

本文探讨了欧盟提议的“聊天控制”立法，该立法旨在扫描所有私人通信，包括加密通信。由于德国撤回支持，形成否决少数派，投票已被推迟。作者认为，这项立法为欧洲制造了一个“数字主权悖论”。

核心问题是，强制欧洲公司为了监控目的而削弱加密，会破坏欧盟试图实现的安全和独立。像Proton和NordVPN这样致力于构建欧洲数字主权替代方案的公司，正被要求妥协使其服务安全和自主的根本性加密技术。

作者强调了政策制定者对安全的理解与互联网技术现实之间的脱节。加密不是一个可选功能，而是安全通信协议的基本组成部分。削弱它，即使是“仅此一次”的例外，也会产生可被恶意行为者利用的漏洞。

作者认为，鉴于安全数字基础设施在控制关键基础设施和防御网络攻击方面的作用，它对国家安全至关重要。通过破坏加密，欧盟正在削弱自身的防御能力。

此次推迟为政策制定者和科技界之间的对话提供了两个月的窗口期，以弥合政治愿景与技术现实之间的差距。作者希望这段时间能够促成一个更加连贯的科技战略，优先发展基于健全工程并服务于民主价值观的安全、专用技术。即将到来的12月投票将揭示欧盟是否真正致力于向其技术界学习，并建立真正的数字主权。

---

## 29. 意大利的反盗版盾牌正如所有人预料的一样，是个大灾难

**原文标题**: Italy's Piracy Shield Is Just as Big a Disaster as Everyone Predicted

**原文链接**: [https://www.techdirt.com/2025/10/14/research-italys-piracy-shield-is-just-as-big-a-disaster-as-everyone-predicted/](https://www.techdirt.com/2025/10/14/research-italys-piracy-shield-is-just-as-big-a-disaster-as-everyone-predicted/)

评论作者承认他们没有读过题为“意大利反盗版盾牌正如所有人预料的那样是一场灾难”的文章。 他们评论的主要意思是担心IP地址被添加到反盗版盾牌黑名单的机制。 具体而言，他们担心该系统可能被滥用，允许个人或组织不公平地针对和屏蔽他们不喜欢的网站，无论这些网站是否真的参与盗版。 作者本质上是提出了一个关键问题，即由于IP地址列入黑名单的过程缺乏透明度或问责制，意大利的反盗版盾牌系统存在审查和操纵的潜在风险。

---

## 30. OVM6948微型相机模块[pdf]

**原文标题**: OVM6948 miniature camera module [pdf]

**原文链接**: [https://www.ovt.com/wp-content/uploads/2023/03/OVM6948-PB-v1.5-WEB.pdf](https://www.ovt.com/wp-content/uploads/2023/03/OVM6948-PB-v1.5-WEB.pdf)

抱歉，我无法处理PDF文件，因此无法提供文章摘要。

---

## 31. 大脑在现实与心理地图间“穿梭”以探索新空间

**原文标题**: The Brain Navigates New Spaces by 'Darting' Between Reality and Mental Maps

**原文链接**: [https://medicine.yale.edu/news-article/brain-navigates-new-spaces-by-flickering-between-reality-and-old-mental-maps/](https://medicine.yale.edu/news-article/brain-navigates-new-spaces-by-flickering-between-reality-and-old-mental-maps/)

耶鲁大学研究人员发现，大脑中的“GPS”——海马体，如何修改认知地图以导航新空间。这项研究以大鼠迷宫实验为例，揭示了海马体在当前环境和记忆中的路径之间“闪烁”，从而实现灵活导航。

研究发现，即使在遇到迷宫中的绕道之前，大鼠的大脑就表现出“预先布线”，显示出模拟替代、不熟悉路线的神经活动模式。这种准备使它们能够快速学习绕道。在绕道导航过程中，大鼠的大脑在其当前位置和对原始路径的记忆之间快速切换。绕道移除后，大鼠对原始路径的心理地图被更新，包含了绕道体验，而并非简单地被删除。

研究人员认为，现实和记忆之间的这种“闪烁”是由θ脑波组织的，θ脑波允许在当前和过去经历之间进行快速比较。Dragoi博士强调，想象捷径的关键脑网络在受到干扰时，会导致闯入性记忆，例如创伤后应激障碍（PTSD）中的经历，在PTSD中，过去和现在被不恰当地混合。该研究强调了认知地图的动态性质及其在空间导航之外的相关性。

---

## 32. F5 Networks遭“高度复杂民族国家”攻击，根据SEC备案文件

**原文标题**: F5 Networks breach by "highly sophisticated nation-state" based on SEC filing

**原文链接**: [https://www.sec.gov/ix?doc=/Archives/edgar/data/1048695/000104869525000149/ffiv-20251015.htm](https://www.sec.gov/ix?doc=/Archives/edgar/data/1048695/000104869525000149/ffiv-20251015.htm)

F5 Networks在提交给美国证券交易委员会的文件（日期为2025年10月15日）中报告了一起安全事件，该事件源于一起他们认为是“高度复杂的国家行为者”实施的入侵。该公司检测到对其系统的未授权访问，并因此在外部网络安全专家的帮助下展开了调查。

攻击者通过利用F5软件开发环境中先前未知的漏洞获得了访问权限。尽管攻击者获得了访问权限，但F5表示，受影响的系统包含非生产源代码存储库。至关重要的是，F5声称没有发现客户数据或生产系统受到损害的证据。

该文件指出，F5立即采取措施控制事件，包括隔离受影响的系统、应用安全补丁和对策，并通知相关执法部门。他们正在继续调查此次入侵的全部范围和影响。F5预计将产生与调查、补救和加强其安全措施相关的费用。

虽然该文件没有提供关于被利用的漏洞或国家行为者的具体信息，但它强调了高级持续性威胁 (APT) 针对软件供应链日益增长的威胁。该公司强调其对网络安全的承诺及其为保护其系统和数据所做的持续努力。尽管发生了此次入侵，但F5认为该事件不会对其业务、财务状况或运营结果产生重大不利影响。

---

## 33. Show HN: Trott – 搜索、排序、提取社交媒体视频(ig,yt,tiktok)

**原文标题**: Show HN: Trott – search,sort,extract social media videos(ig,yt,tiktok)

**原文链接**: [https://trott.hattimatimlabs.in](https://trott.hattimatimlabs.in)

Trott：一款整理和利用社交媒体视频的应用

Trott是一款新应用，旨在帮助用户整理和利用从Instagram、YouTube和TikTok等平台保存的社交媒体视频（Reels、Shorts、视频）。该应用解决了保存视频无法搜索、视频内上下文信息丢失以及不同内容类型缺乏组织等问题。

Trott利用人工智能自动从视频中提取关键细节，例如基于内容的地点、食谱、产品规格和步骤。这通过三个步骤实现：将内容分享到Trott，自动AI处理，然后使用提取的信息进行搜索和整理。

主要功能包括模糊搜索、AI聊天功能（允许用户询问有关其保存内容的具体问题，例如“巴厘岛的精美咖啡馆”）以及智能集成，例如旅行内容的地图和烹饪视频的食谱卡。

Beta测试人员称赞Trott能够将以前无组织和未使用的保存视频转变为计划旅行、寻找推荐等的宝贵资源。该应用程序目前可在iOS（App Store）和Android（Google Play）上下载。Trott是在 RevenueCat Shipathon 2025期间构建的。

---

## 34. 防止Go中CSRF的现代方法

**原文标题**: A modern approach to preventing CSRF in Go

**原文链接**: [https://www.alexedwards.net/blog/preventing-csrf-in-go](https://www.alexedwards.net/blog/preventing-csrf-in-go)

本文探讨了一种现代化的Go语言CSRF（跨站请求伪造）防御方法，即使用Go 1.25中引入的标准库`http.CrossOriginProtection`中间件。该中间件利用`Sec-Fetch-Site`和`Origin`标头验证请求来源，拒绝非安全跨域请求。

尽管`http.CrossOriginProtection`强大而简单，但由于较旧浏览器（2020年之前）的支持有限，因此单独使用并不足够。然而，作者认为，如果强制使用HTTPS且TLS 1.3为最低版本，`http.CrossOriginProtection`会变得非常有效，因为几乎所有支持TLS 1.3的浏览器也支持这些标头。

为了进一步增强安全性，本文建议使用`SameSite` cookie（Lax或Strict）。这种组合可以覆盖来自Firefox v60-69的风险，因为这些版本缺乏对这些标头的支持。

依赖此方法（无需基于令牌的检查）的条件包括：HTTPS和TLS 1.3，使用`http.CrossOriginProtection`和`SameSite` cookie，保护或消除同一可注册域名下的其他网站，使用HSTS标头处理HTTP来源，以及接受来自未知非主流浏览器的小而难以量化的风险。

总而言之，作者建议在特定且明确定义的条件下，结合`http.CrossOriginProtection`、强制TLS 1.3和`SameSite` cookie可以提供相当安全的CSRF攻击防御，从而可能无需传统的基于令牌的方法。本文强调了理解Web安全上下文中“origin”与“site”的区别的重要性。

---

## 35. 英伟达DGX Spark：硬件出色，生态尚早

**原文标题**: Nvidia DGX Spark: great hardware, early days for the ecosystem

**原文链接**: [https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/](https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/)

本文评测了英伟达DGX Spark，一款面向AI研究人员，价值4000美元的桌面“AI超级计算机”。评测者收到了一台预览样机，并重点介绍了其强大的ARM64架构，配备了128GB内存、4TB固态硬盘和一个英伟达Blackwell GPU。

最初的障碍是在ARM64上驾驭CUDA生态系统，这与评测者基于Mac的ML经验大相径庭。挑战包括寻找兼容的PyTorch wheels和理解CUDA版本。英伟达官方Docker容器被证明很有帮助。作者严重依赖Claude Code（Anthropic的编码助手）来克服Ubuntu、CUDA和Docker的配置问题，尤其是在使llama.cpp在GPU加速下运行方面。

一个显著的改进是英伟达官方文档的发布，包括入门指南和操作手册。Tailscale因能够从任何地方远程访问Spark而受到称赞。

评测者注意到最近生态系统支持的激增。Ollama开箱即用，llama.cpp基准测试已经发布，LM Studio提供了一个Spark版本，vLLM有一个官方的英伟达NGC容器。Unsloth也有一个关于微调gpt-oss-20b的教程。

虽然承认由于不熟悉CUDA、ARM64和Ubuntu GPU设置而导致的最初困难，但评测者避免给出明确的推荐，理由是过去24小时内生态系统的快速改进。作者认为，其整体适用性将在未来几周内变得更加明显。

---

## 36. 采访英特尔x86核心首席架构师

**原文标题**: Interviewing Intel's Chief Architect of x86 Cores

**原文链接**: [https://chipsandcheese.com/p/interviewing-intels-chief-architect](https://chipsandcheese.com/p/interviewing-intels-chief-architect)

本文是 George Cozma 对英特尔 x86 核心首席架构师 Stephen Robinson 的采访，讨论了英特尔即将推出的 Panther Lake 和 Clearwater Forest CPU 的架构细节，重点介绍了 Cougar Cove (P-core) 和 Darkmont (E-core) 架构。

采访要点：

*   **Skymont (上一代 E-core):** 显著变化包括更宽、更深的乱序执行机器，提升了 IPC，加大了乱序深度，增加了 load 端口，向量硬件（FMA）翻倍，以及更宽的前端。
*   **Skymont 的 Store 端口:** Store（4 个）与 load（3 个）端口的不对称性，是因为致力于快速生成 store 地址以减少 load 阻塞，从而提高性能。
*   **Darkmont 内存消歧:** Darkmont 在地址生成之前预测 load/store 依赖性，而不是使用历史表，从而优化 load 调度。
*   **Cougar Cove 内存消歧:** 与 Darkmont 类似的概念（优化相对于 store 的 load 调度），但实现方式不同。
*   **SMT (同步多线程):** 客户端处理器（Lunar Lake、Arrow Lake）移除了 SMT，原因是混合计算的优势和设计执行的优势（更低的功耗、更小的面积、更高的频率）。 SMT 在服务器环境中仍然有价值，因为混合计算不太常见，并且工作负载受益于缓解延迟。
*   **客户端与服务器核心差异:** 服务器核心通常包含额外的 RAS（可靠性、可用性和可服务性）特性，例如缓存中的 ECC，因为服务器环境对可靠性要求更高。 某些特性，如 SGX 或 TDX，需要 SOC 级别的支持才能正常运行。
*   **分支预测:** 分支预测的改进有益于客户端和服务器工作负载，因为各种应用程序（游戏、数据库、Web 服务器）共享类似的代码特征。

---

## 37. ASP.NET 安全功能绕过漏洞

**原文标题**: ASP.NET Security Feature Bypass Vulnerability

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-55315](https://nvd.nist.gov/vuln/detail/CVE-2025-55315)

本文描述了CVE-2025-55315，一个影响ASP.NET Core的安全漏洞。该漏洞涉及HTTP请求的不一致解释，具体为HTTP请求/响应走私，允许经过身份验证的攻击者绕过网络上的安全功能。该漏洞被认为是严重级别，CVSS 3.1基本评分为9.9，向量为CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L。这意味着基于网络的攻击，攻击复杂度低，仅需低权限即可执行，无需用户交互，并会导致范围变更，对保密性和完整性产生高影响，对可用性产生低影响。该漏洞被归类为CWE-444，HTTP请求不一致解释（“HTTP请求/响应走私”）。缓解措施和更多详细信息可在提供的微软安全响应中心（MSRC）链接中找到：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55315。

---

## 38. 解包Cloudflare Workers CPU性能基准测试

**原文标题**: Unpacking Cloudflare Workers CPU Performance Benchmarks

**原文链接**: [https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/](https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/)

本文剖析了Cloudflare针对基准测试中Cloudflare Workers在CPU密集型JavaScript执行方面性能低于Vercel (Node.js)的回应。最初，Workers的性能明显更差（高达3.5倍）。Cloudflare进行了调查，并找出了导致这种差异的几个问题，包括基础设施调整、JavaScript库差异和测试方法缺陷。

Cloudflare解决了两个主要问题：**分片和热隔离路由**以及**V8垃圾回收器调优**。 针对一般延迟优化的路由策略对于持续的CPU密集型工作负载效率不高，导致排队。 Cloudflare更新了算法，以更有效地检测和处理CPU密集型工作。 此外，过时的V8垃圾回收器设置导致内存管理效率低下。 调整这些设置使基准测试的性能提高了25％。

剩余的性能差距集中在Next.js上。 Cloudflare发现在OpenNext项目中存在效率低下的问题，包括不必要的分配和数据复制，以及用于数据处理的效率低下的流适配器。 他们已经开始向OpenNext提交pull requests，并计划为Next.js和React做出贡献，以解决这些问题并优化性能。

经过这些更改后，Cloudflare Workers现在在大多数基准测试中与Vercel的性能相当，并且Next.js的性能得到了显着提高，他们希望进一步缩小差距。 他们感谢原始基准测试创建者突出显示了需要改进的领域，最终使所有用户受益。

---

## 39. F5网络报告其产品系统遭受国家级网络攻击

**原文标题**: F5 Networks reports nation-state cyberattack on product systems

**原文链接**: [https://www.streetinsider.com/Corporate+News/F5+Networks+reports+nation-state+cyberattack+on+product+systems/25457824.html](https://www.streetinsider.com/Corporate+News/F5+Networks+reports+nation-state+cyberattack+on+product+systems/25457824.html)

**概要：**

F5 Networks披露其产品开发系统遭受了一起来自国家行为体的复杂网络攻击。据该公司称，攻击者未经授权访问了这些系统。尽管F5证实了此次入侵，但他们表示没有发现客户数据或F5生产系统遭到破坏的证据。

该公司目前正在第三方网络安全专家的协助下，调查该事件的全部范围。F5已采取措施控制攻击并加强其系统的安全性。他们还在努力了解可能被访问的特定数据或知识产权。

该公告强调，公司致力于透明化，并将随着调查的进展提供进一步的更新。该披露凸显了公司面临的来自国家支持的网络攻击的风险日益增加，特别是那些拥有敏感技术信息的公司。虽然直接影响似乎仅限于产品开发系统而非客户数据，但被盗知识产权的潜在长期影响正在调查中。

---

## 40. 英特尔发布配备160GB显存的推理优化Xe3P显卡

**原文标题**: Intel Announces Inference-Optimized Xe3P Graphics Card with 160GB VRAM

**原文链接**: [https://www.phoronix.com/review/intel-crescent-island](https://www.phoronix.com/review/intel-crescent-island)

英特尔发布基于Xe3P Celestial微架构的全新推理优化企业级GPU“新月岛”，计划于2026年下半年向客户提供样品，并可能在2027年或之后进行更广泛的发布。其主要特性包括160GB LPDDR5x内存、性能功耗比优化、风冷以及成本优化设计，使其适用于大型语言模型和令牌即服务提供商。

“新月岛”旨在与AMD的Instinct MI450系列和NVIDIA的Vera Rubin在AI推理领域展开竞争。英特尔目前正在使用现有的Arc Pro B系列GPU来完善其开源软件堆栈。此次发布旨在为Project Battlematrix Linux驱动程序的持续开发增加分量和背景。

除了“新月岛”之外，英特尔还在展示新的Gaudi 3机架级参考设计，每个机架最多可支持64个加速器，采用液冷和8.2TB高带宽内存。然而，对Gaudi 3的支持并不稳定，缺乏主线内核驱动程序。“美洲虎海岸”和现在的“新月岛”的出现可能预示着Gaudi产品线的终结。

---

## 41. 逆向工程 iWork

**原文标题**: Reverse Engineering iWork

**原文链接**: [https://andrews.substack.com/p/reverse-engineering-iwork](https://andrews.substack.com/p/reverse-engineering-iwork)

无法访问文章链接。

---

## 42. 更新桌面 Rust

**原文标题**: Updating Desktop Rust

**原文链接**: [https://tritium.legal/blog/update](https://tritium.legal/blog/update)

本文探讨了更新桌面应用程序所面临的挑战，尤其是在速度、安全性和可靠性至关重要的法律科技领域。与Web应用程序不同，桌面应用程序需要显式更新，这可能会造成中断并可能存在问题。

本文探讨了自动更新的不同方法，评估了它们对法律科技应用程序Tritium的适用性。作者因隐私问题（遥测）和安全风险（提升的权限、网络访问）而拒绝使用后台更新守护程序。文章考察了Zed编辑器的异步后台线程方法，重点介绍了其每小时的更新检查以及使用单独的二进制文件（`auto_update_helper`）来克服Windows上的文件锁定问题。

最终，作者为Tritium提出了一种“减速带”方法。每次应用程序启动时，它都会执行一次性的更新检查。如果有可用更新，应用程序将下载它，退出，并使用辅助进程来部署更新并重新启动。这种方法通过使其成为用户体验中可见的一部分，从而优先考虑更新质量和性能。更新程序二进制文件也通过重命名旧版更新程序和部署处理清理的新版本来进行更新。本文强调了健壮的更新机制的重要性，特别是对于隐私敏感的软件，以防止用户运行易受攻击或存在缺陷的版本。

---

## 43. 代数数据类型的早期历史

**原文标题**: A Early History of Algebraic Data Types

**原文链接**: [https://www.hillelwayne.com/post/algdt-history/](https://www.hillelwayne.com/post/algdt-history/)

本文追溯了代数数据类型（ADTs）——特别是“和”类型和“积”类型——在计算机科学中的早期历史。文章首先对 ADTs 进行标准解释，指出积类型组合字段，和类型提供选项之间的选择，并注意到它们的名称反映了结果类型的基数。

作者的研究表明，John McCarthy 1961 年的论文《计算数学理论的基础》最早对 ADTs 进行了处理，使用“笛卡尔积”和“直接并”来定义新的数据空间。 McCarthy 还认识到了分配律等代数性质。

文章随后探讨了这些概念是如何演变的，重点介绍了 Tony Hoare 1970 年的论文《数据结构笔记》，该论文独立地将和类型和积类型设想为“可区分联合”和“笛卡尔积”。 Hoare 还讨论了使用和类型进行编译时错误检测。然而，和类型后来在命令式编程中基本上消失了。

Rod Burstall 1968 年的论文《通过结构归纳法证明程序的性质》使用 Landin 的符号定义了递归类型，暗示了和类型。

最后，Robin Milner 1977 年的论文《编程中的类型多态性理论》被认为是“和类型”和“积类型”这两个术语的起源，在 ML 的上下文中正式使用 + 符号表示不相交的和。 ML 的早期实现还没有带标签的类型。

---

## 44. F5称黑客窃取了未公开的BIG-IP漏洞和源代码

**原文标题**: F5 says hackers stole undisclosed BIG-IP flaws, source code

**原文链接**: [https://www.bleepingcomputer.com/news/security/f5-says-hackers-stole-undisclosed-big-ip-flaws-source-code/](https://www.bleepingcomputer.com/news/security/f5-says-hackers-stole-undisclosed-big-ip-flaws-source-code/)

2025年10月，F5披露了一起安全漏洞事件，民族国家背景的黑客长期入侵其系统（包括BIG-IP产品开发环境），窃取了未公开的BIG-IP安全漏洞和源代码。该漏洞于2025年8月被发现。虽然攻击者窃取了源代码和漏洞数据，但F5声称没有证据表明这些数据被用于攻击或公开披露。

F5断言，该漏洞并未危及其软件供应链或其他产品，如NGINX、F5分布式云服务或Silverline系统。发现漏洞后，F5加强了访问控制，改进了威胁监控，并强化了其产品开发环境。NCC集团和IOActive的外部安全评估未发现将恶意代码注入BIG-IP源代码的证据。

F5正在联系受影响的客户，提供配置和实施细节。该公司已发布针对BIG-IP、F5OS、BIG-IP Next for Kubernetes、BIG-IQ和APM客户端的更新，并敦促客户安装。他们还为客户提供威胁狩猎指南和改进的iHealth诊断工具。CrowdStrike和Mandiant等网络安全公司已验证了BIG-IP版本的安全性。NCSC和CISA等机构建议保护F5产品和管理界面。此次披露应美国政府的要求被推迟。F5表示，该事件对其运营没有重大影响。

---

## 45. 适用于常规软件但应用于人工智能时错误的信念

**原文标题**: Beliefs that are true for regular software but false when applied to AI

**原文链接**: [https://boydkane.com/essays/boss](https://boydkane.com/essays/boss)

本文强调了一种危险的误解，即认为适用于传统软件的假设也适用于像ChatGPT这样的现代人工智能系统。作者认为，公众对软件漏洞及其修复的理解固然有益，但将其应用于人工智能则具有误导性。

与传统软件的漏洞源于可以识别和纠正的编码错误不同，人工智能的脆弱性通常源于庞大的训练数据集。这些数据集非常庞大，以至于没有人能够完全理解其内容，从而几乎不可能查明人工智能不良行为的根源。因此，修复人工智能的“漏洞”不是一个精确的过程，而是涉及使用更多或经过筛选的数据进行再训练，且不能保证问题真正得到解决。

本文还驳斥了其他常见的假设：与确定性的传统软件不同，人工智能的行为即使在轻微的输入变化下也会发生剧烈变化。此外，创建满足特定要求的人工智能系统具有挑战性，并且人工智能系统可能会表现出甚至其创造者都不知道的、不可预见的能力，这可能很危险。

作者强调了传统软件和人工智能之间的架构差异，并敦促专家向公众传达这些差异，以促进对人工智能安全性的更好理解。通过消除这些错误的信念，作者希望弥合人工智能领域专家和新手之间的理解差距。

---

## 46. 破解 Humane AI Pin

**原文标题**: Hacking the Humane AI Pin

**原文链接**: [https://writings.agg.im/posts/hacking_ai_pin/](https://writings.agg.im/posts/hacking_ai_pin/)

本文记录了Humane公司宣布关闭后，作者破解Humane AI Pin的历程。最初，作者获得了几个Pin，但由于服务器关闭导致无法激活，发现它们无法使用。

作者毫不气馁，专注于通过连接Pin的USB焊盘来获取访问权限，最终在社区成员的帮助下使用了定制设计的转接器。然后，作者深入研究泄露的APK，以绕过引导过程，并大量依赖LLM进行研究和理解Android系统。

获得一个私有ADB密钥是转折点，这授予了作者shell访问权限。尽管有此访问权限，AI Pin强大的SELinux配置限制了用户应用程序的功能，阻止了标准的网络通信。

作者探索了潜在的漏洞，重点关注CVE-2024-31317，这是一个Android漏洞，可以通过利用具有不正确清理的全局设置来授予系统权限。文章详细介绍了构建有效负载以利用此漏洞的复杂过程，操纵Zygote进程以执行具有提升权限的命令。作者广泛记录了整个过程，分享他们的发现以帮助他人。这项工作的重点是绕过Pin的限制性安全措施，并实现对设备的更大控制。

---

## 47. 人工智能工作坊快把我逼疯了。

**原文标题**: AI workslop is driving me insane

**原文链接**: [https://www.cnbc.com/2025/09/23/ai-generated-workslop-is-destroying-productivity-and-teams-researchers-say.html](https://www.cnbc.com/2025/09/23/ai-generated-workslop-is-destroying-productivity-and-teams-researchers-say.html)

本文探讨了一种名为“AI注水文”（workslop）的新现象，即人工智能生成的内容缺乏实质，无法有效推进任务，从而阻碍生产力和团队协作。BetterUp和斯坦福大学的研究人员将“AI注水文”定义为看似合格但最终达不到要求的AI生成作品。一项调查显示，40%的员工遇到过“AI注水文”，估计收到的内容中有15%是低质量且由AI生成。

文章强调了“AI注水文”的负面影响，包括增加了接收者重写、研究或重做工作的工作量。这会导致同事之间的沮丧、困惑以及信任和尊重的下降。“AI注水文”可能表现为过于冗长的文本、不完整的信息或措辞不佳的沟通。

“AI注水文”的经济影响巨大，对于一个拥有10,000名员工的组织来说，由于浪费时间处理这些问题，估计每年损失900万美元。除了金钱成本外，“AI注水文”还会给员工带来情感压力，使他们质疑同事的能力，并导致不愿合作。

文章建议组织需要实施结构化的AI采用方法，提供明确的指南、政策和培训。鼓励公开沟通AI的使用，关注任务质量，并强调人的主观能动性，对于最大限度地减少“AI注水文”并最大限度地提高AI在工作场所的益处至关重要。最终，关键是将AI用作增强人类能力的工具，而不是依赖它来获得复制粘贴的解决方案。

---

## 48. 你是森林里最可怕的怪物。

**原文标题**: You are the scariest monster in the woods

**原文链接**: [https://jamie.ideasasylum.com/2025/10/15/you-are-the-scariest-monster-in-the-woods](https://jamie.ideasasylum.com/2025/10/15/you-are-the-scariest-monster-in-the-woods)

本文认为，真正的威胁并非通用人工智能（AGI）或人工智能本身，而是人类滥用人工智能的可能性。作者将此比作儿童故事《古鲁法洛》，认为人类才是世界上最危险的力量，拥有无与伦比的破坏和剥削能力。他们认为，人工智能只是一种工具，像锤子或步枪一样，放大了人类已有的倾向。

作者驳斥了人工智能奴役或毁灭人类的担忧，而是认为人类将利用人工智能来实现他们现有的目标：获取权力、控制资源和剥削他人。核心问题不是人工智能技术本身，而是“人类+人工智能”的结合，以及人类将如何利用人工智能的能力来实现邪恶的目的。

作者强调，人工智能不是一种无法控制的力量，而是一种我们正在积极开发的技术。关键问题不是人工智能会*对*我们做什么，而是人类会*用*人工智能做什么。因此，我们不应害怕这项技术，而应专注于监管和控制其使用，以防止那些寻求权力和控制的人将其武器化。忽视这一关键方面，而只关注技术，会转移我们对真正问题的注意力：人性和其滥用强大工具的潜力。

---

## 49. 为什么SQLite用C语言编写？

**原文标题**: Why Is SQLite Coded In C

**原文链接**: [https://www.sqlite.org/whyc.html](https://www.sqlite.org/whyc.html)

本文解释了为什么 SQLite 使用 C 语言编写，尽管存在其他编程语言，如 C++、Java、Rust 或 Go。 主要原因是性能、兼容性、低依赖性和稳定性。

由于 C 语言具有“可移植的汇编语言”特性，因此提供了卓越的性能，允许开发人员在保持可移植性的同时，编写接近硬件的代码。 C 语言也具有高度的兼容性，因为几乎所有系统都可以调用 C 语言库，这与其他语言编写的库不同。 SQLite 的低依赖性是另一个关键因素； 它只需要一组最小的标准 C 语言库例程，避免了更现代的语言所需的大型运行时和众多接口。 最后，C 语言的悠久历史和稳定性是有益的，因为该语言已被充分理解且不会快速变化，这对于可靠的数据库引擎至关重要。

本文探讨了为什么 SQLite 没有使用像 C++ 或 Java 这样的面向对象语言进行编码，并强调面向对象编程是一种设计模式，而不是语言要求。 C 语言可以用于面向对象编程，并且过程式代码有时可能更有效和更易于维护。

最后，它讨论了像 Rust 和 Go 这样的“安全”语言。 虽然这些语言旨在防止常见错误，但它们相对较新。 使用这些语言重新编码 SQLite 可能会引入更多错误并可能降低性能。 安全语言也难以从内存不足错误中优雅恢复，这是 SQLite 的一项关键设计特性。 虽然不排除将来使用 Rust 重新编码的可能性，但 Rust 需要成熟，展示跨语言兼容性和对嵌入式系统的支持，实现 100% 的分支覆盖测试，并有效地处理 OOM 错误。

---

## 50. 我们如何知道一个性能分析器是否准确？

**原文标题**: Can we know whether a profiler is accurate?

**原文链接**: [https://stefan-marr.de/2025/10/can-we-know-whether-a-profiler-is-accurate/](https://stefan-marr.de/2025/10/can-we-know-whether-a-profiler-is-accurate/)

本文探讨了评估Java性能分析器（尤其是采样性能分析器）准确性的挑战。采样性能分析器容易受到“观察者效应”的影响，在性能分析期间会改变程序行为。作者认为，由于现代系统的复杂性，通过仿真获得“真实”的性能数据是不切实际的。

所提出的解决方案涉及一种新颖的“基于减速的方法”。通过在机器代码级别精确地减慢Java程序的速度，研究人员旨在近似获得真实数据。核心思想是性能分析器应准确反映引入的减速；如果跨方法的运行时分布发生意外变化，则认为性能分析器不准确。他们通过两种方式精确地减慢程序的速度：首先是恒定量的减速，其次是减慢单个基本块的速度。

作者测试了async-profiler、JFR、JProfiler和YourKit。他们的发现揭示了准确性方面的显着差异。例如，在Havlak基准测试中，async-profiler和JFR表现良好，而JProfiler和YourKit则表现出不准确性，这可能是由于内联问题或未能检测到变化。

减速方法提供了一种通过近似真实数据来评估性能分析器准确性的实用方法。该方法保留了程序的优化和编译决策，使研究人员能够识别性能分析器的缺点，并为提高性能分析器的准确性铺平道路。该研究论文详细介绍了实现和发现，并得出结论，基于减速的方法是评估和改进JIT编译环境中采样性能分析器的宝贵工具。

---

## 51. 美国人的死因 vs. 新闻报道的死因

**原文标题**: What Americans die from vs. what the news reports on

**原文链接**: [https://ourworldindata.org/does-the-news-reflect-what-we-die-from](https://ourworldindata.org/does-the-news-reflect-what-we-die-from)

本文探讨了2023年美国死亡原因与媒体（特别是《纽约时报》、《华盛顿邮报》和福克斯新闻》）对其报道之间的差异。研究发现存在显著脱节：心脏病和癌症占研究原因死亡人数的56%，但媒体报道仅占7%。相反，凶杀和恐怖主义等罕见事件被过度报道。

该研究利用美国疾病控制与预防中心（CDC）和媒体云（Media Cloud）的数据，分析了死亡统计数据和媒体提及情况，纳入了同义词，并且只统计了多次提及的文章，以确保相关性。分析表明，无论政治倾向如何，媒体都倾向于关注引人注目的、情绪化的事件，而忽视了更常见的慢性疾病，如心脏病、中风和呼吸系统疾病。

文章认为，这种不匹配现象的存在是因为“新”事件比持续的现实更具吸引力。罕见事件有可识别的故事，而常见的健康风险则被视为单纯的统计数据。文章指出，这种媒体偏见会扭曲公众认知，影响公众对某些威胁的焦虑程度，并歪曲健康和安全方面的趋势。文章最后认为，认识到这种选择性偏见对于准确理解全球问题至关重要，尤其是在新闻消费持续且广泛的时代。

---

## 52. 使用CSS美化Markdown文章

**原文标题**: CSS for Styling a Markdown Post

**原文链接**: [https://webdev.bryanhogan.com/miscellaneous/styling-markdown/](https://webdev.bryanhogan.com/miscellaneous/styling-markdown/)

本文提供了一份指南，用于为自定义网站设计 Markdown 内容样式。它强调编写自己的 CSS 以获得更大的设计控制权，而不是仅仅依赖预构建的 CSS 框架。

作者概述了一种结构，其中 Markdown 内容放置在 `<main>` 和 `<article class="markdown-container">` 元素中，然后提供 CSS 代码片段来设置此容器中各种 Markdown 元素的样式。

涵盖的关键元素包括：

*   **基本布局：** 为容器设置 `max-width` 和 `margin-block-start` 以控制整体宽度和间距。
*   **段落：** 依赖现有的 CSS 变量和正文样式来保持段落的一致性。
*   **章节标题（h1-h6）：** 添加 `margin-block-start`、`overflow-wrap` 和可自定义的字体属性以实现层次结构和可读性。
*   **图像：** 设置 `max-width`、`height: auto`、`border-radius`，并使用 `margin-inline: auto` 和 `display: block` 居中图像。
*   **列表（ol, ul）：** 使用 `margin-left` 进行间距设置，并使用 `overflow-wrap` 防止溢出。
*   **块引用：** 使用边框、内边距、背景颜色设置样式，并为归属信息设置 `<footer>` 的样式。
*   **表格：** 应用 `display: block` 和 `overflow: auto` 以实现响应式，使用 `border-collapse`、`border-spacing` 并设置 `th` 和 `td` 元素的样式。 使用交替的行背景来提高可读性。
*   **代码（code, pre）：** 应用独特的背景颜色、等宽字体和 `overflow: auto` 以实现可滚动代码块。

作者最后强调了响应式设计的重要性，并提供了指向 MDN 文档中关于标题元素和 Astro 的 Starlight 项目中的 Markdown.css 文件等资源的链接。

---

## 53. 监控数据挑战了我们对位置追踪的认知。

**原文标题**: Surveillance data challenges what we thought we knew about location tracking

**原文链接**: [https://www.lighthousereports.com/investigation/surveillance-secrets/](https://www.lighthousereports.com/investigation/surveillance-secrets/)

一项合作调查“监控秘辛”揭露了First Wap公司及其Altamides软件在全球范围内对电话追踪技术的滥用。该调查由泄露的150万条追踪记录档案引发，揭示了First Wap如何监控超过160个国家/地区的14000多个独特的电话号码。

调查发现受害者包括世界领导人，如卡塔尔前首相和巴沙尔·阿萨德的同伙，以及记者、商人甚至普通公民。报告强调了该软件被用于出于个人原因跟踪个人的案例，超出了执法目的。

First Wap通过中介网络销售其软件，内部文件揭露了其试图向专制政府出售该技术的行为。一项在监控贸易展览会上的卧底行动揭示了First Wap规避制裁的意愿，并为一个私人矿业公司将环境活动家作为目标。First Wap高管建议使用空壳公司来掩盖联系。

虽然First Wap否认非法活动，但调查质疑了该行业声称这些工具仅被政府用于打击严重犯罪的说法。调查结果表明，监控技术很容易被滥用于商业间谍、政治压迫和个人跟踪，凸显了监控行业缺乏监管和监督。报告指出英国企业调查公司KCS Group参与了Altamides的销售和使用，该公司对此予以否认。

---

## 54. 爱尔兰隐私监管机构任命前Meta游说者为第三位委员

**原文标题**: Irish privacy regulator picks ex-Meta lobbyist as third commissioner

**原文链接**: [https://www.euractiv.com/news/irish-privacy-regulator-picks-ex-meta-lobbyist-as-third-commissioner/](https://www.euractiv.com/news/irish-privacy-regulator-picks-ex-meta-lobbyist-as-third-commissioner/)

爱尔兰数据保护委员会（DPC），Meta的主要欧盟隐私监管机构，已任命前WhatsApp、Facebook和Stripe的游说者Niamh Sweeney为其第三位委员。此任命意义重大，因为DPC负责对设立在爱尔兰的公司执行GDPR，包括Meta、谷歌、苹果和微软等大型科技巨头，使其对欧盟的科技监管具有相当大的影响力。

Sweeney作为游说者的背景，尤其是她与Meta的合作经历，引发了对潜在利益冲突的担忧。她的工作涉及WhatsApp在欧洲、非洲和中东地区的公共政策，以及在爱尔兰为Facebook进行游说。

此次任命正值DPC计划增加资源之际，并完成了由三位委员组成的委员会领导架构，其中包括此前任命的Des Hogan和Dale Sunderland。前任委员Helen Dixon因其对大型科技公司执行GDPR的方式而受到批评。虽然Hogan和Sunderland承诺采取更严格的立场，但人们对DPC严格执行法规的意愿仍然持怀疑态度。

隐私权活动家Max Schrems强烈批评了Sweeney的任命，认为这标志着在全球舞台上公然拥抱美国大型科技公司的利益。

---

## 55. 更快地打印Petscii

**原文标题**: Printing Petscii Faster

**原文链接**: [https://retrogamecoders.com/printing-petscii-faster/](https://retrogamecoders.com/printing-petscii-faster/)

无法访问文章链接。

---

## 56. 数组语言动物园

**原文标题**: Zoo of array languages

**原文链接**: [https://ktye.github.io/](https://ktye.github.io/)

本文档作为一个“动物园”，展示了各种数组编程语言，重点是源自APL（A Programming Language）和K的语言家族。主要探讨的语言是K（特别是ktye/k、k9、ngn/k等版本），着重介绍其简洁的语法和强大的数组操作能力。

它简要介绍了K的核心运算符和函数，包括算术、逻辑、关系和数据操作。示例说明了K如何处理算术（+, -, *, /）、比较 (<, >, =)、逻辑运算 (~, &, |)、数组操作（take, drop, cut, join, sort）以及函数式编程概念（each, over, scan）等任务。还涵盖了条件逻辑（`$[a;b;...]`, `while[c;a;b;d;e;..]`）和函数定义（`f:{x+y}`）。文档列出了数据类型和一些随机数生成函数。

除了K之外，它还提到了相关的语言，如APL/360、APL\iv、BQN、KAP和J，展示了数组编程中的传承和多样性。它还包括对实现的引用（如ngn/apl）和资源（ktye.github.io/k.html），以便进一步探索这些语言。

最后，本文档暗示了K环境中的内部结构和优化策略，并提到了“TURBO.K”中的ASM和C组件。

---

## 57. Bozohttpd(8) – NetBSD 手册页

**原文标题**: Bozohttpd(8) – NetBSD Manual Pages

**原文链接**: [https://man.netbsd.org/bozohttpd.8](https://man.netbsd.org/bozohttpd.8)

`bozohttpd` 是一个小型、简单且功能相对简单的 HTTP/1.1 守护进程，专为 NetBSD 系统设计，注重安全性。它处理来自标准输入的 HTTP 请求，并将回复发送到标准输出。主要用于 `inetd(8)`，但也可用作独立守护进程运行。

主要功能包括：
*   **虚拟主机：** 支持根据请求的主机名提供不同的内容。
*   **用户目录转换：** 将 `/~user/` 映射到用户的公共目录。
*   **CGI/1.1 接口：** 允许从指定目录执行 CGI 脚本。
*   **SSL/TLS 支持：** 使用 SSL/TLS 协议提供加密连接。
*   **目录索引：** 如果不存在默认索引文件，则生成目录列表。
*   **HTTP 基本身份验证：** 可以使用 `.htpasswd` 文件限制访问。
*   **阻止列表支持：** 与 `blocklistd(8)` 集成以增强安全性。
*   **压缩：** 支持提供预压缩的 `.gz` 文件。
*   **重写映射：** 允许使用 `.bzremap` 文件进行内部 URL 重写。
*   **符号链接重定向：** 基于符号链接重定向到不同的服务器。

手册页面详细介绍了用于配置的各种命令行选项，包括端口设置、用户/组切换、chroot、MIME 类型映射以及启用/禁用功能。 它还解释了如何使用 `inetd(8)` 配置 `bozohttpd`，并提供了虚拟主机和 PHP 集成的示例。 该文档描述了诸如 `.bzabsredirect`、`.bzredirect`、`.bzremap` 和 `.htpasswd` 等每个目录文件的用法，以启用功能。 存在编译选项可以删除对不需要的功能的支持。

---

## 58. 如何将液态玻璃变成固态界面

**原文标题**: How to turn liquid glass into a solid interface

**原文链接**: [https://tidbits.com/2025/10/09/how-to-turn-liquid-glass-into-a-solid-interface/](https://tidbits.com/2025/10/09/how-to-turn-liquid-glass-into-a-solid-interface/)

本文详细介绍如何在 macOS、iOS、watchOS 和 tvOS 中自定义和控制 Apple 的“液态玻璃”界面设计，以提高可用性和可读性。“液态玻璃”引入了透明和模糊效果，但一些用户认为这会分散注意力。

**macOS：** 最有效的设置是“辅助功能”中的“降低透明度”，它可以使菜单栏和其他元素不透明，防止壁纸穿透。“提高对比度”通过勾勒元素进一步清晰界面，但会改变某些颜色。存在一个隐藏的终端命令可以完全禁用“液态玻璃”，但会导致严重的 UI 问题，不建议使用。可以使用应用程序包标识符通过终端按应用程序禁用。“减弱动态效果”主要影响全屏过渡。

**iOS：** 与 macOS 类似，“降低透明度”是巩固通知的关键。“提高对比度”添加边框并使文本突出，但会改变颜色。将两者结合可以提供最大的不透明度和对比度。“粗体文本”增加了文本的粗细。“减弱动态效果”消除了通知中心中的折射。

**watchOS：** 辅助功能设置与 iOS 相似。作者发现“降低透明度”有助于使通知文本更易于阅读。“提高对比度”提高了控制中心图标的可见性。“粗体文本”影响甚微。

**tvOS：** “液态玻璃”对 tvOS 的影响较小。“降低透明度”消除了侧边栏、顶层和控制中心中的背景穿透。“提高对比度”效果甚微，主要体现在提亮标题上。“粗体文本”不受欢迎，并被认为不利于可读性。

---

## 59. 应对人工智能的经济影响：探索政策应对

**原文标题**: Preparing for AI's economic impact: exploring policy responses

**原文链接**: [https://www.anthropic.com/research/economic-policy-responses](https://www.anthropic.com/research/economic-policy-responses)

Anthropic概述了应对人工智能不确定经济影响的潜在政策，强调积极规划。他们认识到人工智能的影响可能从温和到剧烈，并将政策构想分为三种情景：几乎所有情景、适度加速情景和快速发展情景。

**几乎所有情景的政策**侧重于劳动力发展（通过培训补助金进行技能提升，通过税收改革激励工人保留/再培训）以及通过人工智能基础设施（数据中心、电力）的许可改革来提高生产力。还建议堵塞公司税收漏洞以保护政府收入。

**适度加速情景的政策**，即人工智能导致失业和工资下降，包括调整贸易调整援助以适应人工智能取代（人工智能保险），并考虑对计算或人工智能生成的代币征税，以抵消负面外部性。

**快速发展情景的政策**，可能导致严重的失业和不平等，涉及更具雄心的变革，例如创建主权财富基金来分配人工智能收入，以及采用或更新增值税（VATs）来解释劳动在经济价值中可能减少的份额。像企业财富税这样的新收入结构也可能变得必要。

Anthropic承认围绕人工智能经济影响的不确定性，并强调研究人员、政策制定者和人工智能行业之间持续研究、辩论和合作的重要性，以确保人工智能的收益得到广泛分享。他们承诺投入1000万美元扩大经济期货计划，以支持这些努力。这些想法不代表明确的建议，而是旨在激发进一步的探索和发展。

---

## 60. 动物森友会语.js 演示

**原文标题**: Animalese.js Demo

**原文链接**: [https://acedio.github.io/animalese.js/](https://acedio.github.io/animalese.js/)

本网页演示了`animalese.js`库。该库的详细信息位于其GitHub仓库(https://github.com/Acedio/animalese.js)，旨在生成听起来像《动物森友会》游戏系列中的“动物语”的音频。

此演示允许用户测试该库的功能。页面包含被转换为动物语音频格式的文本，使用户可以听到效果。它似乎还具有缩短单词的功能以及诸如“GrumpIsabelle”之类的示例。用户可以“预览！”和“下载！”生成的音频，表明该库具有收听输出和保存以供以后使用的能力。

总而言之，该网页作为`animalese.js`库的实际展示，使访问者能够体验其功能并通过提供的GitHub链接了解有关其实现的更多信息。

---

## 61. GrapheneOS 准备摆脱 Pixel 束缚

**原文标题**: GrapheneOS is ready to break free from Pixels

**原文链接**: [https://www.androidauthority.com/graphene-os-major-android-oem-partnership-3606853/](https://www.androidauthority.com/graphene-os-major-android-oem-partnership-3606853/)

本文讨论了GrapheneOS计划通过与一家大型安卓OEM厂商合作，将其产品扩展到Pixel手机之外。GrapheneOS，一个专注于隐私的安卓分支，目前仅限于Pixel设备，旨在将其安全操作系统带到未来由骁龙处理器驱动的旗舰手机上。

这项始于2025年6月的合作，标志着另一家OEM厂商终于满足了GrapheneOS严格的安全和更新要求，此前只有谷歌的Pixel系列才能满足这些要求。新款设备定价将与Pixel相似，并在全球范围内销售。虽然合作伙伴的身份尚未公开，但猜测指向了Nothing，尽管他们尚未被认为是“大型”OEM厂商。

此举的部分原因是GrapheneOS批评谷歌延长安全补丁发布时间线，他们认为这会导致漏洞暴露时间过长。与提供更早补丁访问权限的合作伙伴合作，将使GrapheneOS能够独立维护其高安全标准。

Pixel用户可以期待现有设备（包括即将推出的Pixel 10）的持续支持。然而，对Pixel 11的支持仍在考虑中。此次扩展旨在扩大GrapheneOS的影响范围，在更广泛的设备上提供以隐私为中心的Android体验。

---

## 62. 沃尔玛与OpenAI合作，允许顾客通过ChatGPT购物。

**原文标题**: Walmart partners with OpenAI to let shoppers buy items through ChatGPT

**原文链接**: [https://ktla.com/news/consumer-business/walmart-partners-with-openai-to-let-shoppers-buy-items-through-chatgpt/](https://ktla.com/news/consumer-business/walmart-partners-with-openai-to-let-shoppers-buy-items-through-chatgpt/)

沃尔玛与OpenAI合作，将商品目录整合至ChatGPT，使用户可以直接通过AI聊天机器人从沃尔玛购买商品。此举旨在使购物更加便捷和对话化。

用户现在可以向ChatGPT描述他们的需求或愿望，AI将推荐相关的沃尔玛商品。然后，ChatGPT将提供链接，引导用户访问沃尔玛网站或应用程序以完成购买。此功能允许顾客通过自然语言请求购买商品，从而简化购物体验。

此次合作建立在沃尔玛现有的人工智能和对话式商务投资之上。其目标是利用AI聊天机器人日益增长的普及度，并以一种新的、直观的方式触达客户。例如，计划露营旅行的用户可以向ChatGPT询问必备物品，聊天机器人会推荐并链接到沃尔玛提供的相关商品，如帐篷、睡袋和露营炉。

此次整合正在向ChatGPT Plus用户推出，代表着沃尔玛在利用人工智能增强其全渠道零售战略方面迈出了重要一步。它也使OpenAI受益，为其技术提供了一个切实的电子商务应用，展示了其商业潜力。此次合作可能通过吸引那些喜欢更具对话性和精选购物体验的顾客，从而促进沃尔玛的销售额。

---

## 63. 一个2.97美元的ADC能有多差？

**原文标题**: How bad can a $2.97 ADC be?

**原文链接**: [https://excamera.substack.com/p/how-bad-can-a-297-adc-be](https://excamera.substack.com/p/how-bad-can-a-297-adc-be)

无法访问文章链接。

---

## 64. Python 的 splitlines 不止于换行

**原文标题**: Python's splitlines does more than just newlines

**原文链接**: [https://yossarian.net/til/post/python-s-splitlines-does-a-lot-more-than-just-newlines/](https://yossarian.net/til/post/python-s-splitlines-does-a-lot-more-than-just-newlines/)

Python的`str.splitlines()`方法的一个令人惊讶的方面：它分割字符串所依据的字符范围比通常所知的换行符（\n、\r、\r\n）更广。

作者最初假设`splitlines()`只处理“通用换行符”，但后来发现它还根据Unicode的定义，分割其他行边界字符，包括：垂直制表符（\v或\x0b）、换页符（\f或\x0c）、文件分隔符（\x1c）、组分隔符（\x1d）、记录分隔符（\x1e）、下一行（C1控制码 - \x85）、行分隔符（\u2028）和段落分隔符（\u2029）。

文章通过一个包含各种此类字符的示例字符串展示了这一点，说明`splitlines()`将字符串分割成比最初仅考虑标准换行符时可能预期的更多段。

作者最后强调，Unicode包含的内容不仅仅是可打印字符，而且许多生态系统仍然使用C0和C1控制码用于特定的语义目的。这提醒人们处理跨不同系统和标准的文本数据所涉及的复杂性。

---

## 65. 展示 HN: Metorial (YC F25) – 面向 MCP 的 Vercel

**原文标题**: Show HN: Metorial (YC F25) – Vercel for MCP

**原文链接**: [https://github.com/metorial/metorial](https://github.com/metorial/metorial)

Metorial (YC F25) 是一个平台，旨在简化 AI 模型与外部 API、数据源和工具的集成，它使用了模型上下文协议 (MCP)。 它被称为“MCP 的 Vercel”，为构建 Agentic AI 应用程序的开发者提供了一个统一的界面，包含 SDK、监控和自定义选项。

主要功能包括适用于 JavaScript/TypeScript 和 Python 的一键式 SDK、MCP 合规性以及快速设置。 虽然可以进行自托管，但官方推荐使用托管平台，因为它使用 Metorial 最简单快捷的方式。 该平台处理 OAuth 身份验证等复杂问题，并提供会话管理和对话循环等功能。

该平台提供了一个包含 5000 多个 MCP 服务器的大型服务器目录、一个用于测试的嵌入式 MCP Explorer，以及全面的监控和调试工具。 官方提供了 OpenAI 和 Anthropic 集成等常见用例的示例。

Metorial 支持 OpenAI、Anthropic、Google 等各种 AI 提供商，简化了跨不同模型的集成。 它简化了 MCP 的实施，使开发人员能够构建可靠且安全的 Agentic AI 应用程序。 该平台的技术栈包括 Docker、TypeScript、Bun、Go、PostgreSQL、Redis、MongoDB 和 React。 Metorial 提供详细的文档、以开发者为中心的仪表板和完整的 API 访问权限，并获得 FSL-1.1 许可。

---

## 66. 超越 SQLite 单写限制，实现并发写入

**原文标题**: Beyond the SQLite single-writer limitation with concurrent writes

**原文链接**: [https://turso.tech/blog/beyond-the-single-writer-limitation-with-tursos-concurrent-writes](https://turso.tech/blog/beyond-the-single-writer-limitation-with-tursos-concurrent-writes)

本文宣布 Turso Beta 发布，这是一种基于 SQLite 构建的新型数据库系统，它通过使用多版本并发控制（MVCC）进行并发写入，克服了单写入器的限制。SQLite 传统的单写入器模型在许多场景中虽然高效，但在现代多核和多线程环境中却成为瓶颈，导致 SQLITE_BUSY 错误和 CPU 资源利用不足，尤其是在事务涉及业务逻辑或计算时。

Turso 的 MVCC 实现，灵感来自 Hekaton 系统，维护着一个内存索引来跟踪行版本，从而使并发事务能够通过仅在提交时检查行级冲突来继续进行。与涉及计算的场景中的 SQLite 相比，这允许高达 4 倍的写入吞吐量。

文章重点介绍了受益于并发写入的用例，包括具有业务逻辑的事务、大容量数据摄取、流物化和数据增强。虽然 Turso 目前处于早期技术预览阶段，存在诸如低效的行版本表示和缺乏异步 I/O 等限制，但在基于 SQLite 的系统中扩展写入操作的潜力大大扩展了数据库在更广泛的应用中的适用性。作者们正在积极致力于改进以解决这些限制并提高性能。

---

## 67. A 12,000-year-old obelisk with a human face was found in Karahan Tepe

**原文标题**: A 12,000-year-old obelisk with a human face was found in Karahan Tepe

**原文链接**: [https://www.trthaber.com/foto-galeri/karahantepede-12-bin-yil-oncesine-ait-insan-yuzlu-dikili-tas-bulundu/73912.html](https://www.trthaber.com/foto-galeri/karahantepede-12-bin-yil-oncesine-ait-insan-yuzlu-dikili-tas-bulundu/73912.html)

A 12,000-year-old T-shaped obelisk with a human face has been discovered at Karahantepe, Turkey, as part of the Taş Tepeler Project. This find, announced by the Minister of Culture and Tourism, Mehmet Nuri Ersoy, marks the first time a human face has been depicted on such a stone.

The discovery is significant because it reinforces the idea that the T-shaped obelisks found in Göbeklitepe and surrounding areas, with their arm and hand carvings, were intended to symbolize humans. The newly found face, characterized by sharp features, deep eye sockets, and a blocky nose, bears stylistic similarities to previously discovered human sculptures at Karahantepe.

Experts believe this find is a turning point in Neolithic period research, demonstrating the Neolithic people's technical skill, self-expression, and abstract thinking. It suggests that these obelisks are not just symbolic representations of humans, but a direct depiction of human likeness through facial features.

The Taş Tepeler Project, exploring sites dating back approximately 12,000 years, is a comprehensive archaeological endeavor aimed at documenting the transition to settled life and the evolution of belief systems. It continues to provide new insights into the earliest periods of human history in southeastern Anatolia.


---

## 68. Beating the L1 cache with value speculation (2021)

**原文标题**: Beating the L1 cache with value speculation (2021)

**原文链接**: [https://mazzo.li/posts/value-speculation.html](https://mazzo.li/posts/value-speculation.html)

生成摘要时出错

---

## 69. Network Partitions in the Internet

**原文标题**: Network Partitions in the Internet

**原文链接**: [https://bgp.tools/kb/partitions](https://bgp.tools/kb/partitions)

生成摘要时出错

---

## 70. Panther Lake's Reveal at ITT 2025 – By George Cozma

**原文标题**: Panther Lake's Reveal at ITT 2025 – By George Cozma

**原文链接**: [https://chipsandcheese.com/p/panther-lakes-reveal-at-itt-2025](https://chipsandcheese.com/p/panther-lakes-reveal-at-itt-2025)

生成摘要时出错

---

## 71. Ultrasound is ushering a new era of surgery-free cancer treatment

**原文标题**: Ultrasound is ushering a new era of surgery-free cancer treatment

**原文链接**: [https://www.bbc.com/future/article/20251007-how-ultrasound-is-ushering-a-new-era-of-surgery-free-cancer-treatment](https://www.bbc.com/future/article/20251007-how-ultrasound-is-ushering-a-new-era-of-surgery-free-cancer-treatment)

生成摘要时出错

---

## 72. AI and Home-Cooked Software

**原文标题**: AI and Home-Cooked Software

**原文链接**: [https://mrkaran.dev/posts/ai-home-cooked-software/](https://mrkaran.dev/posts/ai-home-cooked-software/)

生成摘要时出错

---

## 73. Why is everything so scalable?

**原文标题**: Why is everything so scalable?

**原文链接**: [https://www.stavros.io/posts/why-is-everything-so-scalable/](https://www.stavros.io/posts/why-is-everything-so-scalable/)

The article argues that startups and developers are often overly focused on building scalable architectures (using microservices, cloud platforms, and orchestrators) from the beginning, even when it's unnecessary and detrimental to their progress. The author criticizes the trend of blindly adopting "FAANG architecture by default" without considering the real costs and benefits.

The core argument is that scalability is expensive and complex, and most startups should prioritize solving fundamental problems like product-market fit and revenue generation. Jumping straight to a complex, distributed system adds unnecessary overhead and distracts from these crucial early stages.

The author proposes a simpler alternative: a well-structured monolith. This involves using modules within a single codebase with clearly defined, statically typed interfaces. This approach enforces separation of concerns, allows for easy API changes and atomic deployments, and offers significant performance benefits through intra-process communication.

While acknowledging the limitations of scaling individual components within a monolith, the author argues that vertical scaling (bigger servers) is often sufficient. The article emphasizes the benefits of a simple architecture, allowing faster development and a competitive advantage in the early stages, advocating for delaying the complexities of distributed systems until they are absolutely necessary. The author suggests that avoiding the upfront cost of a distributed architecture is a key advantage for most startups.


---

## 74. The cost of turning down wind turbines in Britain

**原文标题**: The cost of turning down wind turbines in Britain

**原文链接**: [https://wastedwind.energy/](https://wastedwind.energy/)

生成摘要时出错

---

## 75. Prefix sum: 20 GB/s (2.6x baseline)

**原文标题**: Prefix sum: 20 GB/s (2.6x baseline)

**原文链接**: [https://github.com/ashtonsix/perf-portfolio/tree/main/delta](https://github.com/ashtonsix/perf-portfolio/tree/main/delta)

生成摘要时出错

---

## 76. What Sleep Is

**原文标题**: What Sleep Is

**原文链接**: [https://aeon.co/essays/two-billion-humans-are-doing-something-bizarre-right-now-sleeping](https://aeon.co/essays/two-billion-humans-are-doing-something-bizarre-right-now-sleeping)

生成摘要时出错

---

## 77. Signed Backdoor Hiding in Plain Sight on Framework Devices

**原文标题**: Signed Backdoor Hiding in Plain Sight on Framework Devices

**原文链接**: [https://eclypsium.com/blog/bombshell-the-signed-backdoor-hiding-in-plain-sight-on-framework-devices/](https://eclypsium.com/blog/bombshell-the-signed-backdoor-hiding-in-plain-sight-on-framework-devices/)

生成摘要时出错

---

## 78. Show HN: Greenonion.ai – AI-Powered Design Assistant

**原文标题**: Show HN: Greenonion.ai – AI-Powered Design Assistant

**原文链接**: [https://exuberant-premise-723012.framer.app/](https://exuberant-premise-723012.framer.app/)

生成摘要时出错

---

## 79. Disk Prices

**原文标题**: Disk Prices

**原文链接**: [https://diskprices.com/?locale=us](https://diskprices.com/?locale=us)

生成摘要时出错

---

## 80. SmolBSD – 构建你自己的最小BSD系统

**原文标题**: SmolBSD – build your own minimal BSD system

**原文链接**: [https://smolbsd.org](https://smolbsd.org)

SmolBSD is a meta-operating system built on NetBSD that allows users to create custom, minimal UNIX environments. It leverages the netbsd-MICROVM kernel for its foundation, ensuring portability and reliability. Users select the components they need (like sshd or httpd) and smolBSD builds a bootable image. The goal is to build BSD systems quickly, reproducibly, and with minimal bloat.

Key features include: composability (selecting only necessary components), reproducibility (deterministic and version-controllable builds), instant boot times (powered by netbsd-MICROVM), and universal compatibility (runs on QEMU or Firecracker).

The article provides examples of building systems with bozohttpd (a static web server), nbakery (a build/image creation service), and nitrosshd (a minimal SSH server). It includes commands for cloning the SmolBSD repository, building images using `bmake`, and running them with `startnb.sh`. The article also encourages community involvement through GitHub, Mastodon, and email.


---

## 81. Dutch government takes control of Chinese-owned chipmaker Nexperia

**原文标题**: Dutch government takes control of Chinese-owned chipmaker Nexperia

**原文链接**: [https://www.cnbc.com/2025/10/13/dutch-government-takes-control-of-chinese-owned-chipmaker-nexperia.html](https://www.cnbc.com/2025/10/13/dutch-government-takes-control-of-chinese-owned-chipmaker-nexperia.html)

生成摘要时出错

---

## 82. Astronomers 'image' a mysterious dark object in the distant Universe

**原文标题**: Astronomers 'image' a mysterious dark object in the distant Universe

**原文链接**: [https://www.mpg.de/25518363/1007-asph-astronomers-image-a-mysterious-dark-object-in-the-distant-universe-155031-x](https://www.mpg.de/25518363/1007-asph-astronomers-image-a-mysterious-dark-object-in-the-distant-universe-155031-x)

生成摘要时出错

---

## 83. Show HN: CSS Extras

**原文标题**: Show HN: CSS Extras

**原文链接**: [https://github.com/sindresorhus/css-extras](https://github.com/sindresorhus/css-extras)

生成摘要时出错

---

## 84. Student's alleged torture death by Cambodia scammers sparks turmoil in S. Korea

**原文标题**: Student's alleged torture death by Cambodia scammers sparks turmoil in S. Korea

**原文链接**: [https://www.theguardian.com/world/2025/oct/14/south-korea-student-alleged-torture-death-cambodia-scammers-sparks-turmoil](https://www.theguardian.com/world/2025/oct/14/south-korea-student-alleged-torture-death-cambodia-scammers-sparks-turmoil)

生成摘要时出错

---

## 85. Nvidia sells tiny new computer that puts big AI on your desktop

**原文标题**: Nvidia sells tiny new computer that puts big AI on your desktop

**原文链接**: [https://arstechnica.com/ai/2025/10/nvidia-sells-tiny-new-computer-that-puts-big-ai-on-your-desktop/](https://arstechnica.com/ai/2025/10/nvidia-sells-tiny-new-computer-that-puts-big-ai-on-your-desktop/)

生成摘要时出错

---

## 86. An Interactive Introduction to Fourier Transforms

**原文标题**: An Interactive Introduction to Fourier Transforms

**原文链接**: [https://www.jezzamon.com/fourier/](https://www.jezzamon.com/fourier/)

生成摘要时出错

---

## 87. NanoChat – The best ChatGPT that $100 can buy

**原文标题**: NanoChat – The best ChatGPT that $100 can buy

**原文链接**: [https://github.com/karpathy/nanochat](https://github.com/karpathy/nanochat)

生成摘要时出错

---

## 88. AppLovin nonconsensual installs

**原文标题**: AppLovin nonconsensual installs

**原文链接**: [https://www.benedelman.org/applovin-nonconsensual-installs/](https://www.benedelman.org/applovin-nonconsensual-installs/)

生成摘要时出错

---

## 89. Dolphins show Alzheimer's signs linked to toxic blooms

**原文标题**: Dolphins show Alzheimer's signs linked to toxic blooms

**原文链接**: [https://newatlas.com/biology/beached-dolphins-alzheimers-polluted-waters/](https://newatlas.com/biology/beached-dolphins-alzheimers-polluted-waters/)

生成摘要时出错

---

## 90. Italy's Piracy Shield Is Just as Big a Disaster as Everyone Predicted

**原文标题**: Italy's Piracy Shield Is Just as Big a Disaster as Everyone Predicted

**原文链接**: [https://www.techdirt.com/2025/10/14/research-italys-piracy-shield-is-just-as-big-a-disaster-as-everyone-predicted/](https://www.techdirt.com/2025/10/14/research-italys-piracy-shield-is-just-as-big-a-disaster-as-everyone-predicted/)

生成摘要时出错

---

## 91. New England's last coal plant has stopped operating, according to its owners

**原文标题**: New England's last coal plant has stopped operating, according to its owners

**原文链接**: [https://www.nhpr.org/nh-news/2025-10-06/new-englands-last-coal-plant-has-stopped-operating-according-to-its-owners](https://www.nhpr.org/nh-news/2025-10-06/new-englands-last-coal-plant-has-stopped-operating-according-to-its-owners)

生成摘要时出错

---

## 92. Testing a compiler-driven full-stack web framework

**原文标题**: Testing a compiler-driven full-stack web framework

**原文链接**: [https://wasp.sh/blog/2025/10/07/how-we-test-a-web-framework](https://wasp.sh/blog/2025/10/07/how-we-test-a-web-framework)

生成摘要时出错

---

## 93. How AI hears accents: An audible visualization of accent clusters

**原文标题**: How AI hears accents: An audible visualization of accent clusters

**原文链接**: [https://accent-explorer.boldvoice.com/](https://accent-explorer.boldvoice.com/)

生成摘要时出错

---

## 94. Don’t Look Up: Sensitive internal links in the clear on GEO satellites [pdf]

**原文标题**: Don’t Look Up: Sensitive internal links in the clear on GEO satellites [pdf]

**原文链接**: [https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf](https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf)

生成摘要时出错

---

## 95. Why the push for Agentic when models can barely follow a simple instruction?

**原文标题**: Why the push for Agentic when models can barely follow a simple instruction?

**原文链接**: [https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154](https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154)

生成摘要时出错

---

## 96. Pyrefly: Python type checker and language server in Rust

**原文标题**: Pyrefly: Python type checker and language server in Rust

**原文链接**: [https://pyrefly.org/?featured_on=talkpython](https://pyrefly.org/?featured_on=talkpython)

生成摘要时出错

---

## 97. LLMs are getting better at character-level text manipulation

**原文标题**: LLMs are getting better at character-level text manipulation

**原文链接**: [https://blog.burkert.me/posts/llm_evolution_character_manipulation/](https://blog.burkert.me/posts/llm_evolution_character_manipulation/)

生成摘要时出错

---

## 98. Waymo's Robotaxis Are Coming to London

**原文标题**: Waymo's Robotaxis Are Coming to London

**原文链接**: [https://www.wired.com/story/waymos-robotaxis-are-coming-to-london/](https://www.wired.com/story/waymos-robotaxis-are-coming-to-london/)

生成摘要时出错

---

## 99. ADS-B Exposed

**原文标题**: ADS-B Exposed

**原文链接**: [https://adsb.exposed/](https://adsb.exposed/)

生成摘要时出错

---

## 100. Copy-and-Patch: A Copy-and-Patch Tutorial

**原文标题**: Copy-and-Patch: A Copy-and-Patch Tutorial

**原文链接**: [https://transactional.blog/copy-and-patch/tutorial](https://transactional.blog/copy-and-patch/tutorial)

生成摘要时出错

---

