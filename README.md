# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-14.md)

*最后自动更新时间: 2026-02-14 17:58:24*
## 1. 我的智能睡眠眼罩将用户的脑电波广播到一个公开的 MQTT 代理。

**原文标题**: My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

**原文链接**: [https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/](https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/)

本文详述了在一款具备脑电图（EEG）监测、肌肉电刺激（EMS）及其他感官功能的“智能”睡眠眼罩中发现的重大安全与隐私缺陷。由于官方应用程序存在诸多漏洞，作者试图对其进行替换，并利用 Claude (Opus 4.6) 对该产品的通信协议进行了逆向工程。

通过使用专业工具对基于 Flutter 开发的安卓 APK 进行反编译，Claude 提取了硬编码的 MQTT 凭据以及 15 种不同指令的具体字节结构。虽然这最初只是为了让作者能为自己的设备构建一个私有的 Web 控制面板，但随后却导致了一个令人不安的发现：该公司的消息代理（message broker）是开放的，且在所有设备上共用一套通用凭据。

通过连接到该公司的 MQTT 代理，作者能够：
*   **访问实时数据：** 查看全球其他活跃用户的实时脑电图数据，识别快速眼动期（REM）和深层睡眠等特定睡眠阶段。
*   **远程控制：** 向这些设备发送指令，这可能允许陌生人在用户睡眠时远程触发振动、加热或电脉冲（EMS）。

作者已就这些漏洞通知了这家未具名的制造商，并称此次事件是针对“数字卫生”和物联网（IoT）安全的一次严正警告。关键在于，作者强调整个逆向工程过程——包括蓝牙分析、二进制反编译和漏洞发现——均由 AI 模型在约 30 分钟内自主完成。这凸显了 AI 在快速识别和利用消费级硬件关键缺陷方面日益增强的能力。

---

## 2. Ooh.directory：发现你感兴趣的优质博客。

**原文标题**: Ooh.directory: a place to find good blogs that interest you

**原文链接**: [https://ooh.directory/](https://ooh.directory/)

**Ooh.directory** 是一个精心收录的在线目录，旨在帮助用户根据特定兴趣发现高质量的独立博客。该平台将海量内容组织成易于检索的类别，包括艺术与媒体（最大的类别，收录了 905 个博客）、计算机与技术、人文、科学以及个人博客。

该目录充当了“小众网络”（small web）的探索引擎，重点推介近期更新的网站以及具有里程碑意义的站点。精选博客涵盖了广泛的主题，例如：
*   **文学与艺术：** *Split Lip Magazine*（风格独特的写作）、*roughghosts*（关于生活与文学的沉思）以及 *halloumi season*（经典电影分析）。
*   **科学与技术：** *Molecular Design*（化合物处理）、*theHigherGeometer*（高等数学）以及 *tonsky.me*（编程与 UI 设计）。
*   **专业兴趣：** *Everything Flows*（苏格兰音乐）、*Structure Tech*（房屋检查）以及 *Every Day Is Like Wednesday*（漫画）。
*   **个人与学术：** *One Starry Night*（慢性病历险记）以及 *prior probability*（经济与法律）。

该平台强调全球多样性，汇集了来自美国、英国、西班牙、德国、塞浦路斯和澳大利亚的博主。通过对博客进行分类并提供近期文章片段——内容涵盖从传统诗歌到实验性的“Brainfuck”代码——Ooh.directory 为读者提供了一个中心枢纽，用于在主流社交媒体算法之外寻找小众的长篇内容。

---

## 3. Show HN：Sameshi —— 大小不到 2KB、Elo 约 1200 的国际象棋引擎

**原文标题**: Show HN: Sameshi – a ~1200 Elo chess engine that fits within 2KB

**原文链接**: [https://github.com/datavorous/sameshi](https://github.com/datavorous/sameshi)

**Sameshi** 是一款追求极致便携性的极简国际象棋引擎，其核心源代码 (`sameshi.h`) 仅为 1.95 KB。尽管体积微小，但根据对阵 Stockfish（1320–1600 等级）的 240 场测试赛，其估计强度达到了约 **1170 Elo**。

该引擎利用多种经典的国际象棋编程技术，在严苛的尺寸限制下优化性能：
*   **棋盘表示：** 采用 120 格的“邮箱式”（mailbox）棋盘。
*   **搜索算法：** 采用带有 Alpha-beta 剪枝的 Negamax 搜索。
*   **走子排序：** 实现了“吃子优先”的启发式算法以提高效率。
*   **评估系统：** 使用简单的纯子力评估系统。
*   **走法校验：** 支持完整的合法走法校验，包括将军、将死和逼和。

为了将体积控制在 2KB 以内，Sameshi 省略了几项复杂的比赛规则，包括王车易位、吃过路兵、兵的升变、50步规则和三次重复局面。其性能是在固定深度 5 且每局限 60 步（ply）的情况下测得的。总的来说，Sameshi 高效地展示了如何用极简的代码编写出功能完备且具备竞争力的国际象棋 AI。

---

## 4. Zig – io_uring 与 Grand Central Dispatch 的 std.Io 实现已合并

**原文标题**: Zig – io_uring and Grand Central Dispatch std.Io implementations landed

**原文链接**: [https://ziglang.org/devlog/2026/#2026-02-13](https://ziglang.org/devlog/2026/#2026-02-13)

2026 年初的 Zig 开发日志概述了该语言标准库和工作流工具的几项重大进展：

**I/O 与事件化运行时**
Zig 已经为 `std.Io.Evented` 实现了 `io_uring` (Linux) 和 Grand Central Dispatch (macOS) 支持。基于用户态栈切换（fiber），这些实现允许开发者在线程化 I/O 和事件化 I/O 之间轻松切换，而无需更改应用逻辑。虽然目前由于性能回退和诊断功能缺失仍处于实验阶段，但它们代表了向统一、可切换的 I/O 架构迈进的重要一步。

**包管理增强**
两项重大更新改进了依赖工作流。首先，获取的包现在存储在项目本地的 `zig-pkg` 目录中，这有利于离线构建，也更方便对依赖项源码进行“调试与修改”。全局缓存还会存储压缩版本，以支持未来的点对点（P2P）共享。其次，新增的 `--fork=[path]` 命令行标志允许开发者使用本地源码检出来全局覆盖特定的依赖项。这简化了在不立即修改构建脚本的情况下修复生态系统损坏的过程。

**向 Windows Native API 迁移**
标准库正从 Win32 API (`kernel32.dll`) 转向更底层的 Native API (`ntdll.dll`)。其目标是消除由高层封装引入的臃肿、不必要的堆分配以及隐藏的失败模式。关键示例包括：一种避免了有问题的 DLL 加载且更可靠的熵（entropy）实现，以及通过使用 `NtReadFile`/`NtWriteFile` 来提供与任务取消和异步句柄更好的集成。

**Zig libc**
简要提到了社区贡献者在 `zig libc` 实现方面取得的持续进展。

总之，这些更新专注于提高 Zig 的可靠性、减少外部依赖，并为系统编程提供更灵活的环境。

---

## 5. 半色调之影

**原文标题**: Shades of Halftone

**原文链接**: [https://blog.maximeheckel.com/posts/shades-of-halftone/](https://blog.maximeheckel.com/posts/shades-of-halftone/)

《半色调之影》探讨了基于图案的后处理技术的复兴，重点关注半色调效果——一种利用不同大小的点阵列来模拟连续色调的视错觉。它最初是受限于油墨印刷的技术折中方案，如今已成为一种多功能的数字工具，为图像、视频和 3D 场景增添质感与艺术气息。

作者详细解析了使用 GLSL 着色器的技术实现。该过程始于创建一个基于距离场的圆，并使用 `fract` 函数生成重复网格。为了将此效果应用于数字媒体，必须使用 `floor` 函数对底层纹理进行像素化处理，以确保每个网格单元采样一致的颜色。通过根据底层像素的“亮度”（Luma）缩放圆点半径，可以实现真实的半色调效果。

文章强调了标准圆点之外的几种创意变体：
*   **交错网格：** 偏移各行以增加圆点密度并减少空白区域。
*   **双重图案：** 将标准圆点与“反转”的正方形（深色背景上的白点）相结合，以更好地保留暗部区域的细节。
*   **环状：** 使用同心圆创造一种“低分辨率”或类似终端界面的美感。

最后，作者讨论了多通道半色调，即为 RGB 或 CMYK 颜色通道叠加独立的网格。这引发了对莫列波纹（Moiré patterns）的探索——一种因重叠网格的旋转或位移而产生的视觉干扰现象。通过掌握这些数学技术，开发者和设计师可以将简单的几何图案转化为复杂且极具感染力的视觉体验。

---

## 6. Vim 9.2 发布

**原文标题**: Vim 9.2 Released

**原文链接**: [https://www.vim.org/vim-9.2-released.php](https://www.vim.org/vim-9.2-released.php)

Vim 9.2 于 2026 年 2 月 14 日发布，在脚本编写、用户界面和平台兼容性方面引入了重大更新。核心重点是 **Vim9 script** 的演进，现已支持枚举 (Enums)、泛型函数 (Generic functions) 和元组 (Tuple) 数据类型。这些现代架构增强了生态系统，实现了更高效的插件开发，并能更好地与 GitHub Copilot 等 AI 工具集成。

**核心功能亮点：**
*   **增强补全：** 用户现在可以在插入模式补全时使用模糊匹配，并能直接从寄存器中补全单词。
*   **高级 Diff 模式：** 此更新引入了“linematch”算法以实现更好的对齐，并新增了 `diffanchors` 选项来处理复杂的文件对比。行内高亮也得到了改进。
*   **现代平台支持：** Vim 9.2 增加了对 Wayland 的实验性支持，并遵循 XDG 基本目录规范，将配置文件移至 `$HOME/.config/vim`。
*   **UI 与 UX 改进：** 新功能包括垂直标签面板、MS-Windows GUI 的原生深色模式，以及通过 `:Tutor` 命令访问的现代化交互式学习插件。

**更新的默认设置：**
为适应当前硬件，多项长期存在的默认设置已完成现代化。值得注意的是，'history' 增加到 200，'ruler' 和 'showcmd' 默认开启，针对高分辨率显示器，GTK 的 'fontsize' 增加到 12pt。

**公益软件传承：**
在 Bram Moolenaar 去世后，该项目的慈善使命已从已解散的 ICCF Holland 移交给 **Kuwasha**。Vim 仍然是“公益软件 (Charityware)”，鼓励用户通过这家总部位于加拿大的新合作伙伴继续为乌干达儿童提供支持。

此版本还包含大量错误修复、安全补丁和性能优化。

---

## 7. Platforms bend over backward to help DHS censor ICE critics, advocates say

**原文标题**: Platforms bend over backward to help DHS censor ICE critics, advocates say

**原文链接**: [https://arstechnica.com/tech-policy/2026/02/platforms-bend-over-backward-to-help-dhs-censor-ice-critics-advocates-say/](https://arstechnica.com/tech-policy/2026/02/platforms-bend-over-backward-to-help-dhs-censor-ice-critics-advocates-say/)

Advocacy groups are suing the Trump administration, alleging that Department of Homeland Security (DHS) officials are illegally coercing tech platforms to censor critics of Immigration and Customs Enforcement (ICE). Lawsuits filed by the Foundation for Individual Rights and Expression (FIRE) and the Electronic Frontier Foundation (EFF) claim that Attorney General Pam Bondi and DHS Secretary Kristi Noem are using regulatory pressure to force the removal of First Amendment-protected content.

Key instances of alleged censorship include Apple’s removal of ICE-monitoring apps like "ICEBlock" and "Eyes Up," and Meta’s deletion of the 100,000-member Facebook group "ICE Sightings–Chicagoland." Additionally, FBI Director Kash Patel recently confirmed an investigation into encrypted Signal chats used to track ICE activity. 

The government justifies these actions by citing "officer safety" and "doxing." However, advocates argue that documenting government employees performing public duties is protected speech and that officials are intentionally broadening the definition of doxing to suppress accountability and public awareness.

A central criticism in the report is that tech giants—including Google and Meta—are "bending over backward" to comply with government requests. Advocacy groups note that platforms often fulfill subpoenas without requiring court orders, fail to provide users with advance notice, or ignore their own internal policies to appease officials. 

Legal experts suggest that platforms have the resources to resist these demands but often choose not to. The EFF noted that when the administration has been challenged in court, it has sometimes withdrawn its requests, suggesting the censorship relies on platform compliance rather than legal authority. The ongoing lawsuits seek to expose government-platform communications and secure permanent injunctions against government-coerced censorship.

---

## 8. Show HN: I spent 3 years reverse-engineering a 40 yo stock market sim from 1986

**原文标题**: Show HN: I spent 3 years reverse-engineering a 40 yo stock market sim from 1986

**原文链接**: [https://www.wallstreetraider.com/story.html](https://www.wallstreetraider.com/story.html)

生成摘要时出错

---

## 9. A Review of M Disc Archival Capability. With long term testing results

**原文标题**: A Review of M Disc Archival Capability. With long term testing results

**原文链接**: [http://www.microscopy-uk.org.uk/mag/artsep16/mol-mdisc-review.html](http://www.microscopy-uk.org.uk/mag/artsep16/mol-mdisc-review.html)

生成摘要时出错

---

## 10. Show HN: SQL-tap – Real-time SQL traffic viewer for PostgreSQL and MySQL

**原文标题**: Show HN: SQL-tap – Real-time SQL traffic viewer for PostgreSQL and MySQL

**原文链接**: [https://github.com/mickamy/sql-tap](https://github.com/mickamy/sql-tap)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 2 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 3 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 4 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 5 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 6 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 7 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 8 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 9 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 10 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 11 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 12 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 13 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 14 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 15 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 16 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 17 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 18 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 19 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 20 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 21 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 22 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 23 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 24 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 25 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 26 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 27 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 28 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 29 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 30 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 31 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 32 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 33 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 34 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 35 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 36 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 37 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 38 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 39 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 40 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 41 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 42 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 43 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 44 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 45 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 46 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 47 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 48 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 49 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 50 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 51 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 52 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 53 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 54 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 55 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 56 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 57 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 58 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 59 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 60 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 61 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 62 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 63 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 64 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 65 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 66 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 67 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 68 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 69 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 70 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 71 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 72 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 73 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 74 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 75 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 76 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 77 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 78 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 79 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 80 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 81 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 82 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 83 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 84 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 85 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 86 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 87 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 88 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 89 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 90 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 91 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 92 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 93 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 94 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 95 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 96 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 97 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 98 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 99 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 100 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 101 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 102 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 103 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 104 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 105 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 106 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 107 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 108 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 109 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 110 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 111 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 112 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 113 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 114 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 115 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 116 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 117 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 118 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 119 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 120 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 121 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 122 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 123 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 124 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 125 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 126 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 127 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 128 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 129 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 130 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 131 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 132 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 133 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 134 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 135 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 136 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 137 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 138 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 139 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 140 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 141 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 142 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 143 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 144 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 145 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 146 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 147 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 148 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 149 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 150 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 151 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 152 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 153 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 154 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 155 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 156 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 157 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 158 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 159 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 160 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 161 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 162 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 163 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 164 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 165 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 166 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 167 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 168 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 169 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 170 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 171 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 172 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 173 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 174 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 175 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 176 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 177 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 178 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 179 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 180 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 181 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 182 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 183 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 184 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 185 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 186 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 187 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 188 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 189 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 190 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 191 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 192 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 193 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 194 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 195 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 196 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 197 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 198 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 199 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 200 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 201 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 202 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 203 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 204 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 205 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 206 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 207 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 208 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 209 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 210 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 211 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 212 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 213 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 214 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 215 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 216 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 217 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 218 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 219 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 220 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 221 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 222 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 223 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 224 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 225 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 226 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 227 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 228 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 229 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 230 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 231 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 232 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 233 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 234 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 235 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 236 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 237 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 238 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 239 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 240 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 241 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 242 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 243 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 244 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 245 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 246 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 247 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 248 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 249 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 250 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 251 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 252 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 253 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 254 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 255 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 256 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 257 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 258 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 259 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 260 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 261 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 262 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 263 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 264 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 265 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 266 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 267 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 268 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 269 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 270 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 271 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 272 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 273 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 274 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 275 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 276 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 277 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 278 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 279 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 280 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 281 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 282 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 283 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 284 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 285 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 286 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 287 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 288 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 289 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 290 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 291 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 292 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 293 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 294 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 295 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 296 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 297 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 298 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 299 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 300 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 301 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 302 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 303 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 304 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 305 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 306 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 307 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 308 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 309 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 310 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 311 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 312 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 313 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 314 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 315 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 316 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 317 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 318 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 319 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 320 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 321 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 322 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 323 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 324 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 325 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 326 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 327 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 328 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 329 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 330 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 331 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
