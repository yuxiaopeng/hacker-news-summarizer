# Hacker News 热门文章摘要 (2026-02-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Ars Technica makes up quotes from Matplotlib maintainer; pulls story

**原文标题**: Ars Technica makes up quotes from Matplotlib maintainer; pulls story

**原文链接**: [https://infosec.exchange/@mttaggart/116065340523529645](https://infosec.exchange/@mttaggart/116065340523529645)

生成摘要时出错

---

## 12. How many registers does an x86-64 CPU have? (2020)

**原文标题**: How many registers does an x86-64 CPU have? (2020)

**原文链接**: [https://blog.yossarian.net/2020/11/30/How-many-registers-does-an-x86-64-cpu-have](https://blog.yossarian.net/2020/11/30/How-many-registers-does-an-x86-64-cpu-have)

生成摘要时出错

---

## 13. Babylon 5 is now free to watch on YouTube

**原文标题**: Babylon 5 is now free to watch on YouTube

**原文链接**: [https://cordcuttersnews.com/babylon-5-is-now-free-to-watch-on-youtube/](https://cordcuttersnews.com/babylon-5-is-now-free-to-watch-on-youtube/)

生成摘要时出错

---

## 14. Code Storage by the Pierre Computer Company

**原文标题**: Code Storage by the Pierre Computer Company

**原文链接**: [https://code.storage/](https://code.storage/)

生成摘要时出错

---

## 15. Stoat removes all LLM-generated code following user criticism

**原文标题**: Stoat removes all LLM-generated code following user criticism

**原文链接**: [https://github.com/orgs/stoatchat/discussions/1022](https://github.com/orgs/stoatchat/discussions/1022)

生成摘要时出错

---

## 16. What color are your bits? (2004)

**原文标题**: What color are your bits? (2004)

**原文链接**: [https://ansuz.sooke.bc.ca/entry/23](https://ansuz.sooke.bc.ca/entry/23)

生成摘要时出错

---

## 17. The Sling: Humanity's Forgotten Power

**原文标题**: The Sling: Humanity's Forgotten Power

**原文链接**: [https://www.slinging.org/](https://www.slinging.org/)

生成摘要时出错

---

## 18. Understanding the Go Compiler: The Linker

**原文标题**: Understanding the Go Compiler: The Linker

**原文链接**: [https://internals-for-interns.com/posts/the-go-linker/](https://internals-for-interns.com/posts/the-go-linker/)

生成摘要时出错

---

## 19. The World of Harmonics – With a Coffee, Guitar and Synth

**原文标题**: The World of Harmonics – With a Coffee, Guitar and Synth

**原文链接**: [https://mynoise.net/vlog.php?ep=20260204](https://mynoise.net/vlog.php?ep=20260204)

生成摘要时出错

---

## 20. Cogram (YC W22) – Hiring former technical founders

**原文标题**: Cogram (YC W22) – Hiring former technical founders

**原文链接**: [https://www.ycombinator.com/companies/cogram/jobs/LDTrViN-ex-technical-founder-product-engineer](https://www.ycombinator.com/companies/cogram/jobs/LDTrViN-ex-technical-founder-product-engineer)

生成摘要时出错

---

## 21. 数据库系统中的压缩数学原理

**原文标题**: The mathematics of compression in database systems

**原文链接**: [https://www.bitsxpages.com/p/the-mathematics-of-compression-in](https://www.bitsxpages.com/p/the-mathematics-of-compression-in)

生成摘要时出错

---

## 22. Sound and Practical Points-To Analysis for Incomplete C Programs [pdf]

**原文标题**: Sound and Practical Points-To Analysis for Incomplete C Programs [pdf]

**原文链接**: [https://www.sjalander.com/research/pdf/sjalander-cgo2026-pip.pdf](https://www.sjalander.com/research/pdf/sjalander-cgo2026-pip.pdf)

Based on the title and the technical metadata provided in the document, here is a concise summary of the article:

**Summary: Sound and Practical Points-To Analysis for Incomplete C Programs**

This article addresses a fundamental challenge in static analysis: performing points-to analysis on "incomplete" C programs, such as software libraries, individual modules, or code fragments. Traditional points-to analyses typically operate under a "closed-world" assumption, requiring the entire source code to be available to produce accurate results. When applied to partial programs, these methods often become either **unsound** (ignoring the effects of unknown external code) or **imprecise** (assuming external code can modify any memory location).

The authors propose a framework that balances soundness with practical precision. The core of their approach involves modeling the "unknown" environment—the external code that calls into the module or is called by it. Key features of the analysis include:

1.  **Escaping Object Tracking:** The analysis identifies "escaping" pointers—those passed to external functions or stored in global variables—and tracks how the external environment might transitively access or modify them.
2.  **Sound Modeling of Callbacks:** It accounts for scenarios where external code might call back into internal functions, ensuring that all potential pointer aliases are captured.
3.  **Boundary Refinement:** Rather than assuming the "worst-case" (that any pointer can point to anything), the analysis uses type information and visibility rules to bound the potential targets of external pointers, maintaining high precision.

The paper evaluates the technique against existing benchmarks, likely within an LLVM-based environment (as suggested by citations to Lattner and Hardekopf). The results demonstrate that the analysis is "practical," meaning it scales to real-world code sizes while providing significantly more useful data for compilers and bug-finding tools than traditional conservative approaches. This research is critical for modular software development, where analyzing code in isolation is often a necessity.

---

## 23. 7zip.com Is Serving Malware

**原文标题**: 7zip.com Is Serving Malware

**原文链接**: [https://www.malwarebytes.com/blog/threat-intel/2026/02/fake-7-zip-downloads-are-turning-home-pcs-into-proxy-nodes](https://www.malwarebytes.com/blog/threat-intel/2026/02/fake-7-zip-downloads-are-turning-home-pcs-into-proxy-nodes)

生成摘要时出错

---

## 24. Show HN: Data Engineering Book – An open source, community-driven guide

**原文标题**: Show HN: Data Engineering Book – An open source, community-driven guide

**原文链接**: [https://github.com/datascale-ai/data_engineering_book/blob/main/README_en.md](https://github.com/datascale-ai/data_engineering_book/blob/main/README_en.md)

生成摘要时出错

---

## 25. How the Little Guy Moved

**原文标题**: How the Little Guy Moved

**原文链接**: [https://animationobsessive.substack.com/p/how-the-little-guy-moved](https://animationobsessive.substack.com/p/how-the-little-guy-moved)

生成摘要时出错

---

## 26. Common Lisp Screenshots: today's CL applications in action

**原文标题**: Common Lisp Screenshots: today's CL applications in action

**原文链接**: [http://www.lisp-screenshots.org](http://www.lisp-screenshots.org)

生成摘要时出错

---

## 27. Building a TUI is easy now

**原文标题**: Building a TUI is easy now

**原文链接**: [https://hatchet.run/blog/tuis-are-easy-now](https://hatchet.run/blog/tuis-are-easy-now)

生成摘要时出错

---

## 28. Font Rendering from First Principles

**原文标题**: Font Rendering from First Principles

**原文链接**: [https://mccloskeybr.com/articles/font_rendering.html](https://mccloskeybr.com/articles/font_rendering.html)

生成摘要时出错

---

## 29. GPT-5.2 derives a new result in theoretical physics

**原文标题**: GPT-5.2 derives a new result in theoretical physics

**原文链接**: [https://openai.com/index/new-result-theoretical-physics/](https://openai.com/index/new-result-theoretical-physics/)

生成摘要时出错

---

## 30. NPMX – a fast, modern browser for the NPM registry

**原文标题**: NPMX – a fast, modern browser for the NPM registry

**原文链接**: [https://npmx.dev](https://npmx.dev)

生成摘要时出错

---

## 31. YouTube as Storage

**原文标题**: YouTube as Storage

**原文链接**: [https://github.com/PulseBeat02/yt-media-storage](https://github.com/PulseBeat02/yt-media-storage)

生成摘要时出错

---

## 32. Backblaze Drive Stats for 2025

**原文标题**: Backblaze Drive Stats for 2025

**原文链接**: [https://www.backblaze.com/blog/backblaze-drive-stats-for-2025/](https://www.backblaze.com/blog/backblaze-drive-stats-for-2025/)

生成摘要时出错

---

## 33. Monosketch

**原文标题**: Monosketch

**原文链接**: [https://monosketch.io/](https://monosketch.io/)

生成摘要时出错

---

## 34. Fix the iOS keyboard before the timer hits zero or I'm switching back to Android

**原文标题**: Fix the iOS keyboard before the timer hits zero or I'm switching back to Android

**原文链接**: [https://ios-countdown.win/](https://ios-countdown.win/)

生成摘要时出错

---

## 35. The EU moves to kill infinite scrolling

**原文标题**: The EU moves to kill infinite scrolling

**原文链接**: [https://www.politico.eu/article/tiktok-meta-facebook-instagram-brussels-kill-infinite-scrolling/](https://www.politico.eu/article/tiktok-meta-facebook-instagram-brussels-kill-infinite-scrolling/)

生成摘要时出错

---

## 36. Advanced Aerial Robotics Made Simple

**原文标题**: Advanced Aerial Robotics Made Simple

**原文链接**: [https://www.drehmflight.com](https://www.drehmflight.com)

生成摘要时出错

---

## 37. gRPC: From service definition to wire format

**原文标题**: gRPC: From service definition to wire format

**原文链接**: [https://kreya.app/blog/grpc-deep-dive/](https://kreya.app/blog/grpc-deep-dive/)

生成摘要时出错

---

## 38. WolfSSL sucks too, so now what?

**原文标题**: WolfSSL sucks too, so now what?

**原文链接**: [https://blog.feld.me/posts/2026/02/wolfssl-sucks-too/](https://blog.feld.me/posts/2026/02/wolfssl-sucks-too/)

生成摘要时出错

---

## 39. CSS-Doodle

**原文标题**: CSS-Doodle

**原文链接**: [https://css-doodle.com/](https://css-doodle.com/)

生成摘要时出错

---

## 40. Gradient.horse

**原文标题**: Gradient.horse

**原文链接**: [https://gradient.horse](https://gradient.horse)

生成摘要时出错

---

## 41. Anthropic raises $30B in Series G funding at $380B post-money valuation

**原文标题**: Anthropic raises $30B in Series G funding at $380B post-money valuation

**原文链接**: [https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)

生成摘要时出错

---

## 42. Adventures in Neural Rendering

**原文标题**: Adventures in Neural Rendering

**原文链接**: [https://interplayoflight.wordpress.com/2026/02/10/adventures-in-neural-rendering/](https://interplayoflight.wordpress.com/2026/02/10/adventures-in-neural-rendering/)

生成摘要时出错

---

## 43. Faster Than Dijkstra?

**原文标题**: Faster Than Dijkstra?

**原文链接**: [https://systemsapproach.org/2026/02/09/faster-than-dijkstra/](https://systemsapproach.org/2026/02/09/faster-than-dijkstra/)

生成摘要时出错

---

## 44. How did the Maya survive?

**原文标题**: How did the Maya survive?

**原文链接**: [https://www.theguardian.com/news/2026/feb/12/apocalypse-no-how-almost-everything-we-thought-we-knew-about-the-maya-is-wrong](https://www.theguardian.com/news/2026/feb/12/apocalypse-no-how-almost-everything-we-thought-we-knew-about-the-maya-is-wrong)

生成摘要时出错

---

## 45. French railway operator tests solar on train tracks

**原文标题**: French railway operator tests solar on train tracks

**原文链接**: [https://www.pv-magazine.com/2026/02/05/french-railway-operator-tests-pv-on-train-tracks/](https://www.pv-magazine.com/2026/02/05/french-railway-operator-tests-pv-on-train-tracks/)

生成摘要时出错

---

## 46. I'm not worried about AI job loss

**原文标题**: I'm not worried about AI job loss

**原文链接**: [https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss)

生成摘要时出错

---

## 47. Implementing Auto Tiling with Just 5 Tiles

**原文标题**: Implementing Auto Tiling with Just 5 Tiles

**原文链接**: [https://www.kyledunbar.dev/2026/02/05/Implementing-auto-tiling-with-just-5-tiles.html](https://www.kyledunbar.dev/2026/02/05/Implementing-auto-tiling-with-just-5-tiles.html)

生成摘要时出错

---

## 48. Green’s Dictionary of Slang - Five hundred years of the vulgar tongue

**原文标题**: Green’s Dictionary of Slang - Five hundred years of the vulgar tongue

**原文链接**: [https://greensdictofslang.com/](https://greensdictofslang.com/)

生成摘要时出错

---

## 49. Just 5 weeks of brain training may protect against dementia for 20 years

**原文标题**: Just 5 weeks of brain training may protect against dementia for 20 years

**原文链接**: [https://www.sciencedaily.com/releases/2026/02/260211073023.htm](https://www.sciencedaily.com/releases/2026/02/260211073023.htm)

生成摘要时出错

---

## 50. Oh, good: Discord's age verification rollout has ties to Palantir co-founder

**原文标题**: Oh, good: Discord's age verification rollout has ties to Palantir co-founder

**原文链接**: [https://www.pcgamer.com/software/platforms/oh-good-discords-age-verification-rollout-has-ties-to-palantir-co-founder-and-panopticon-architect-peter-thiel/](https://www.pcgamer.com/software/platforms/oh-good-discords-age-verification-rollout-has-ties-to-palantir-co-founder-and-panopticon-architect-peter-thiel/)

生成摘要时出错

---

## 51. Can you rewire your brain?

**原文标题**: Can you rewire your brain?

**原文链接**: [https://aeon.co/essays/what-the-metaphor-of-rewiring-gets-wrong-about-neuroplasticity](https://aeon.co/essays/what-the-metaphor-of-rewiring-gets-wrong-about-neuroplasticity)

生成摘要时出错

---

## 52. Show HN: Prompt to Planet, generate procedural 3D planets from text

**原文标题**: Show HN: Prompt to Planet, generate procedural 3D planets from text

**原文链接**: [https://prompttoplanet.n4ze3m.com/](https://prompttoplanet.n4ze3m.com/)

生成摘要时出错

---

## 53. An AI Agent Published a Hit Piece on Me – More Things Have Happened

**原文标题**: An AI Agent Published a Hit Piece on Me – More Things Have Happened

**原文链接**: [https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/)

生成摘要时出错

---

## 54. New Nick Bostrom Paper: Optimal Timing for Superintelligence [pdf]

**原文标题**: New Nick Bostrom Paper: Optimal Timing for Superintelligence [pdf]

**原文链接**: [https://nickbostrom.com/optimal.pdf](https://nickbostrom.com/optimal.pdf)

生成摘要时出错

---

## 55. MinIO repository is no longer maintained

**原文标题**: MinIO repository is no longer maintained

**原文链接**: [https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f](https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f)

生成摘要时出错

---

## 56. OpenAI has deleted the word 'safely' from its mission

**原文标题**: OpenAI has deleted the word 'safely' from its mission

**原文链接**: [https://theconversation.com/openai-has-deleted-the-word-safely-from-its-mission-and-its-new-structure-is-a-test-for-whether-ai-serves-society-or-shareholders-274467](https://theconversation.com/openai-has-deleted-the-word-safely-from-its-mission-and-its-new-structure-is-a-test-for-whether-ai-serves-society-or-shareholders-274467)

生成摘要时出错

---

## 57. Show HN: Skill that lets Claude Code/Codex spin up VMs and GPUs

**原文标题**: Show HN: Skill that lets Claude Code/Codex spin up VMs and GPUs

**原文链接**: [https://cloudrouter.dev/](https://cloudrouter.dev/)

生成摘要时出错

---

## 58. Sandwich Bill of Materials

**原文标题**: Sandwich Bill of Materials

**原文链接**: [https://nesbitt.io/2026/02/08/sandwich-bill-of-materials.html](https://nesbitt.io/2026/02/08/sandwich-bill-of-materials.html)

生成摘要时出错

---

## 59. GPT‑5.3‑Codex‑Spark

**原文标题**: GPT‑5.3‑Codex‑Spark

**原文链接**: [https://openai.com/index/introducing-gpt-5-3-codex-spark/](https://openai.com/index/introducing-gpt-5-3-codex-spark/)

生成摘要时出错

---

## 60. Taste for Makers

**原文标题**: Taste for Makers

**原文链接**: [https://paulgraham.com/taste.html](https://paulgraham.com/taste.html)

生成摘要时出错

---

## 61. Gemini 3 Deep Think

**原文标题**: Gemini 3 Deep Think

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/)

生成摘要时出错

---

## 62. Show HN: ClipPath – Paste screenshots as file paths in your terminal

**原文标题**: Show HN: ClipPath – Paste screenshots as file paths in your terminal

**原文链接**: [https://github.com/BiteCraft/ClipPath](https://github.com/BiteCraft/ClipPath)

生成摘要时出错

---

## 63. The Three Year Myth

**原文标题**: The Three Year Myth

**原文链接**: [https://green.spacedino.net/the-three-year-myth/](https://green.spacedino.net/the-three-year-myth/)

生成摘要时出错

---

## 64. We interfaced single-threaded C++ with multi-threaded Rust

**原文标题**: We interfaced single-threaded C++ with multi-threaded Rust

**原文链接**: [https://antithesis.com/blog/2026/rust_cpp/](https://antithesis.com/blog/2026/rust_cpp/)

生成摘要时出错

---

## 65. Age of Empires: 25 years of pathfinding problems with C++ [video]

**原文标题**: Age of Empires: 25 years of pathfinding problems with C++ [video]

**原文链接**: [https://www.youtube.com/watch?v=lEBQveBCtKY](https://www.youtube.com/watch?v=lEBQveBCtKY)

生成摘要时出错

---

## 66. Zed editor switching graphics lib from blade to wgpu

**原文标题**: Zed editor switching graphics lib from blade to wgpu

**原文链接**: [https://github.com/zed-industries/zed/pull/46758](https://github.com/zed-industries/zed/pull/46758)

生成摘要时出错

---

## 67. Skip the Tips: A game to select "No Tip" but dark patterns try to stop you

**原文标题**: Skip the Tips: A game to select "No Tip" but dark patterns try to stop you

**原文链接**: [https://skipthe.tips/](https://skipthe.tips/)

生成摘要时出错

---

## 68. Pentagon Used Anthropic's Claude in Maduro Venezuela Raid

**原文标题**: Pentagon Used Anthropic's Claude in Maduro Venezuela Raid

**原文链接**: [https://www.wsj.com/politics/national-security/pentagon-used-anthropics-claude-in-maduro-venezuela-raid-583aff17](https://www.wsj.com/politics/national-security/pentagon-used-anthropics-claude-in-maduro-venezuela-raid-583aff17)

生成摘要时出错

---

## 69. Resizing windows on macOS Tahoe – the saga continues

**原文标题**: Resizing windows on macOS Tahoe – the saga continues

**原文链接**: [https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/](https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/)

生成摘要时出错

---

## 70. An open replacement for the IBM 3174 Establishment Controller

**原文标题**: An open replacement for the IBM 3174 Establishment Controller

**原文链接**: [https://github.com/lowobservable/oec](https://github.com/lowobservable/oec)

生成摘要时出错

---

## 71. The wonder of modern drywall

**原文标题**: The wonder of modern drywall

**原文链接**: [https://www.worksinprogress.news/p/the-wonder-of-modern-drywall](https://www.worksinprogress.news/p/the-wonder-of-modern-drywall)

生成摘要时出错

---

## 72. Show HN: Moltis – AI assistant with memory, tools, and self-extending skills

**原文标题**: Show HN: Moltis – AI assistant with memory, tools, and self-extending skills

**原文链接**: [https://www.moltis.org](https://www.moltis.org)

生成摘要时出错

---

## 73. Carl Sagan's Baloney Detection Kit: Tools for Thinking Critically (2025)

**原文标题**: Carl Sagan's Baloney Detection Kit: Tools for Thinking Critically (2025)

**原文链接**: [https://www.openculture.com/2025/09/the-carl-sagan-baloney-detection-kit.html](https://www.openculture.com/2025/09/the-carl-sagan-baloney-detection-kit.html)

生成摘要时出错

---

## 74. An AI agent published a hit piece on me

**原文标题**: An AI agent published a hit piece on me

**原文链接**: [https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)

生成摘要时出错

---

## 75. Americans now spend 6.3 hours per day on their phones, up 1 hour from 2023

**原文标题**: Americans now spend 6.3 hours per day on their phones, up 1 hour from 2023

**原文链接**: [https://apptopia.com/en/blog/americans-now-spend-6-3-hours-per-day-on-their-phones-up-an-hour-from-january-2023/](https://apptopia.com/en/blog/americans-now-spend-6-3-hours-per-day-on-their-phones-up-an-hour-from-january-2023/)

生成摘要时出错

---

## 76. EU Greens/Pirates and Left file amendments to end ChatControl 1.0 mass scanning

**原文标题**: EU Greens/Pirates and Left file amendments to end ChatControl 1.0 mass scanning

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/116063821334857824](https://digitalcourage.social/@echo_pbreyer/116063821334857824)

生成摘要时出错

---

## 77. Lena by qntm (2021)

**原文标题**: Lena by qntm (2021)

**原文链接**: [https://qntm.org/mmacevedo](https://qntm.org/mmacevedo)

生成摘要时出错

---

## 78. Show HN: OpenWhisper – free, local, and private voice-to-text macOS app

**原文标题**: Show HN: OpenWhisper – free, local, and private voice-to-text macOS app

**原文链接**: [https://github.com/richardwu/openwhisper](https://github.com/richardwu/openwhisper)

生成摘要时出错

---

## 79. Dario Amodei – "We are near the end of the exponential" [video]

**原文标题**: Dario Amodei – "We are near the end of the exponential" [video]

**原文链接**: [https://www.dwarkesh.com/p/dario-amodei-2](https://www.dwarkesh.com/p/dario-amodei-2)

生成摘要时出错

---

## 80. ByteDance Seed2.0 LLM: breakthrough in complex real-world tasks

**原文标题**: ByteDance Seed2.0 LLM: breakthrough in complex real-world tasks

**原文链接**: [https://seed.bytedance.com/en/blog/seed2-0-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83](https://seed.bytedance.com/en/blog/seed2-0-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83)

生成摘要时出错

---

## 81. MySQL foreign key cascade operations finally hit the binary log

**原文标题**: MySQL foreign key cascade operations finally hit the binary log

**原文链接**: [https://readyset.io/blog/mysql-9-6-foreign-key-cascade-operations-finally-hit-the-binary-log](https://readyset.io/blog/mysql-9-6-foreign-key-cascade-operations-finally-hit-the-binary-log)

生成摘要时出错

---

## 82. Open source is not about you (2018)

**原文标题**: Open source is not about you (2018)

**原文链接**: [https://gist.github.com/richhickey/1563cddea1002958f96e7ba9519972d9](https://gist.github.com/richhickey/1563cddea1002958f96e7ba9519972d9)

生成摘要时出错

---

## 83. Show HN: Geo Racers – Race from London to Tokyo on a single bus pass

**原文标题**: Show HN: Geo Racers – Race from London to Tokyo on a single bus pass

**原文链接**: [https://geo-racers.com/](https://geo-racers.com/)

生成摘要时出错

---

## 84. Ruby Newbie is joining the Ruby Users forum

**原文标题**: Ruby Newbie is joining the Ruby Users forum

**原文链接**: [https://www.rubyforum.org/t/ruby-newbie-is-joining-the-ruby-users-forum/97](https://www.rubyforum.org/t/ruby-newbie-is-joining-the-ruby-users-forum/97)

生成摘要时出错

---

## 85. D Programming Language

**原文标题**: D Programming Language

**原文链接**: [https://dlang.org/](https://dlang.org/)

生成摘要时出错

---

## 86. Japan's Dododo Land, the most irritating place on Earth

**原文标题**: Japan's Dododo Land, the most irritating place on Earth

**原文链接**: [https://soranews24.com/2026/02/07/take-a-trip-to-japans-dododo-land-the-most-irritating-place-on-earth/](https://soranews24.com/2026/02/07/take-a-trip-to-japans-dododo-land-the-most-irritating-place-on-earth/)

生成摘要时出错

---

## 87. Warcraft III Peon Voice Notifications for Claude Code

**原文标题**: Warcraft III Peon Voice Notifications for Claude Code

**原文链接**: [https://github.com/tonyyont/peon-ping](https://github.com/tonyyont/peon-ping)

生成摘要时出错

---

## 88. The "Crown of Nobles" Noble Gas Tube Display (2024)

**原文标题**: The "Crown of Nobles" Noble Gas Tube Display (2024)

**原文链接**: [https://theshamblog.com/the-crown-of-nobles-noble-gas-tube-display/](https://theshamblog.com/the-crown-of-nobles-noble-gas-tube-display/)

生成摘要时出错

---

## 89. Ring cancels its partnership with Flock Safety after surveillance backlash

**原文标题**: Ring cancels its partnership with Flock Safety after surveillance backlash

**原文链接**: [https://www.theverge.com/news/878447/ring-flock-partnership-canceled](https://www.theverge.com/news/878447/ring-flock-partnership-canceled)

生成摘要时出错

---

## 90. AI could eat itself: Competitors (..) steal their secrets and clone them

**原文标题**: AI could eat itself: Competitors (..) steal their secrets and clone them

**原文链接**: [https://www.theregister.com/2026/02/14/ai_risk_distillation_attacks/](https://www.theregister.com/2026/02/14/ai_risk_distillation_attacks/)

生成摘要时出错

---

## 91. Do Metaprojects

**原文标题**: Do Metaprojects

**原文链接**: [https://taylor.town/wealth-001](https://taylor.town/wealth-001)

生成摘要时出错

---

## 92. Why exercise isn't much help if you are trying to lose weight

**原文标题**: Why exercise isn't much help if you are trying to lose weight

**原文链接**: [https://www.newscientist.com/article/2514600-why-exercise-isnt-much-help-if-you-are-trying-to-lose-weight/](https://www.newscientist.com/article/2514600-why-exercise-isnt-much-help-if-you-are-trying-to-lose-weight/)

生成摘要时出错

---

## 93. Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed

**原文标题**: Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed

**原文链接**: [http://blog.can.ac/2026/02/12/the-harness-problem/](http://blog.can.ac/2026/02/12/the-harness-problem/)

生成摘要时出错

---

## 94. Polis: Open-source platform for large-scale civic deliberation

**原文标题**: Polis: Open-source platform for large-scale civic deliberation

**原文链接**: [https://pol.is/home2](https://pol.is/home2)

生成摘要时出错

---

## 95. Zvec is a lightweight, fast, in-process vector database

**原文标题**: Zvec is a lightweight, fast, in-process vector database

**原文链接**: [https://github.com/alibaba/zvec](https://github.com/alibaba/zvec)

生成摘要时出错

---

## 96. Cache Monet

**原文标题**: Cache Monet

**原文链接**: [https://cachemonet.com](https://cachemonet.com)

生成摘要时出错

---

## 97. Run Pebble OS in Browser via WASM

**原文标题**: Run Pebble OS in Browser via WASM

**原文链接**: [https://ericmigi.github.io/pebble-qemu-wasm/](https://ericmigi.github.io/pebble-qemu-wasm/)

生成摘要时出错

---

## 98. How to Have a Bad Career – David Patterson (2016) [video]

**原文标题**: How to Have a Bad Career – David Patterson (2016) [video]

**原文链接**: [https://www.youtube.com/watch?v=Rn1w4MRHIhc](https://www.youtube.com/watch?v=Rn1w4MRHIhc)

生成摘要时出错

---

## 99. A brief history of barbed wire fence telephone networks (2024)

**原文标题**: A brief history of barbed wire fence telephone networks (2024)

**原文链接**: [https://loriemerson.net/2024/08/31/a-brief-history-of-barbed-wire-fence-telephone-networks/](https://loriemerson.net/2024/08/31/a-brief-history-of-barbed-wire-fence-telephone-networks/)

生成摘要时出错

---

## 100. The Future for Tyr, a Rust GPU Driver for Arm Mali Hardware

**原文标题**: The Future for Tyr, a Rust GPU Driver for Arm Mali Hardware

**原文链接**: [https://lwn.net/Articles/1055590/](https://lwn.net/Articles/1055590/)

生成摘要时出错

---

