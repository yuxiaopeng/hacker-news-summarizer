# Hacker News 热门文章摘要 (2026-04-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国可再生能源发电量首次超过天然气

**原文标题**: For the first time in the U.S., renewables generate more power than natural gas

**原文链接**: [https://e360.yale.edu/digest/us-renewables-natural-gas-coal](https://e360.yale.edu/digest/us-renewables-natural-gas-coal)

今年3月，美国达成了一项重大的清洁能源里程碑：包括太阳能、风能、水能和生物质能在内的可再生能源，其发电量首次超过天然气，成为全美最主要的电力来源。根据智库Ember的数据，若结合核能，零碳能源提供了该国一半以上的总电力。

这一破纪录的表现主要由两大因素驱动：风能和太阳能基础设施的快速扩张，以及电力需求的季节性下降。温和的春季天气减少了供暖和制冷需求，使得化石燃料发电量降至至少25年来的3月最低水平。

然而，电力需求的激增使脱离化石燃料的转型变得复杂。高耗能数据中心的发展促使科技公司安装新的天然气发电机，而电网运营商为了确保供电可靠性，正在推迟老旧煤电厂的退役。去年，美国煤电产能退役量降至15年来最低点，共有九座电厂获得了运营延期，其中五座是基于美国能源部的紧急命令。

尽管美国能源信息署预测，太阳能、风能和电池将占今年新增电网容量的93%，但总需求的持续增长仍在为清洁能源旨在取代的老旧煤电和天然气基础设施提供“生命线”。

---

## 2. 有人买下 30 个 WordPress 插件并全部植入了后门。

**原文标题**: Someone bought 30 WordPress plugins and planted a backdoor in all of them

**原文链接**: [https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/](https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/)

本文详细介绍了一起影响超过30个WordPress插件的大规模供应链攻击。一个原名为“Essential Plugin”（或“WP Online Support”）的插件组合在Flippa上以六位数的价格被收购，买家随后立即植入了后门。恶意代码潜伏了八个月，直到2026年4月才被正式激活利用。

此次攻击利用PHP反序列化后门实现了远程代码执行。一旦激活，它会向`wp-config.php`注入一段6KB的代码块，并下载一个伪装成WordPress核心组件的恶意文件。该恶意软件充当SEO垃圾信息注入器，专门向Googlebot（谷歌爬虫）提供隐藏重定向和虚假页面，以规避网站所有者的检测。值得注意的是，攻击者利用以太坊智能合约来解析指令与控制（C2）域名，导致传统的域名接管手段无法奏效。

作为回应，WordPress.org插件团队永久关闭了31个受影响的插件，并强制推送了安全更新。然而，作者警告称，此次更新仅中和了“自动回传”机制，并未清理已被感染的`wp-config.php`文件。网站所有者被敦促手动检查其配置文件是否存在未经授权的代码，并使用经过清理的修复版本替换受损插件。

归根结底，这一事件暴露了WordPress生态系统中的一个系统性漏洞：插件所有权转让缺乏监管。由于WordPress.org在插件易主时不会触发代码审查或通知用户，攻击者可以购买已建立的信任，并将其武器化以攻击数十万个安装实例。

---

## 3. Multi-Agentic Software Development Is a Distributed Systems Problem

**原文标题**: Multi-Agentic Software Development Is a Distributed Systems Problem

**原文链接**: [https://kirancodes.me/posts/log-distributed-llms.html](https://kirancodes.me/posts/log-distributed-llms.html)

生成摘要时出错

---

## 4. WiiFin — 适用于任天堂 Wii 的 Jellyfin 客户端

**原文标题**: WiiFin – Jellyfin Client for Nintendo Wii

**原文链接**: [https://github.com/fabienmillet/WiiFin](https://github.com/fabienmillet/WiiFin)

**WiiFin** 是一款实验性的开源自制客户端，旨在将 Jellyfin 媒体服务器体验带到 Nintendo Wii 和 vWii 平台。该应用采用 C++ 语言并基于 GRRLIB 和 MPlayer CE 开发，为浏览和串流电影、电视剧及音乐提供了一个轻量级且针对主机优化的界面。

**核心功能：**
*   **身份验证与个人资料：** 支持传统登录和快速连接（通过其他设备配对）。通过访问令牌（access tokens）安全地存储多个用户配置。
*   **媒体库管理：** 用户可以浏览包含完整封面图和元数据的媒体库。具备“继续观看”和“下一集”栏目，并支持播放报告功能以同步服务器播放进度。
*   **用户界面：** 专为 Wii 优化，支持 Wiimote 红外指针、虚拟屏幕键盘、背景音乐，以及用于进度调整和音轨切换的全功能播放器控制层。
*   **安全性：** 通过 mbedTLS 处理 HTTPS 连接，并支持自签名证书。

**技术限制：**
由于 Wii 缺乏支持现代编解码器的硬件，WiiFin 不支持“直接播放”。所有视频必须由 Jellyfin 服务器进行转码。此外，音频仅限双声道，且字幕必须由服务器烧录至视频流中。

**部署与未来：**
该项目采用 GPLv3 协议授权，可通过 Homebrew Channel 以 `.dol` 文件形式运行，或安装为 `.wad` 频道。虽然目前已具备功能，但仍处于实验阶段。开发路线图包括媒体库排序/筛选、“收藏”系统以及可自定义的 UI 主题。对于开发者，构建该项目需要 devkitPro 工具链和特定的 Wii 开发库。

---

## 5. NimConf 2026：日期公布，报名开启

**原文标题**: NimConf 2026: Dates Announced, Registrations Open

**原文链接**: [https://nim-lang.org/blog/2026/04/07/nimconf-2026.html](https://nim-lang.org/blog/2026/04/07/nimconf-2026.html)

The Nim Team has announced **NimConf 2026**, scheduled for **June 20, 2026**. The conference will follow its traditional online format, featuring pre-recorded talks premiered on YouTube, where presenters can engage with the audience through live chat Q&A.

NimConf is a community-driven event focused on the Nim programming language. It covers a broad spectrum of topics, including language development, ecosystem updates, personal projects, niche libraries, and business use cases. The event serves as a platform for viewers to learn about the latest progress in Nim and for presenters to showcase their work to a global audience.

**Key Deadlines for Presenters:**
*   **Talk Proposals:** Must be submitted by **May 10, 2026**.
*   **Talk Recordings:** Accepted presenters must submit their final video recordings by **June 7, 2026**.

The organizers encourage all Nim enthusiasts to submit proposals, regardless of the topic's complexity, highlighting the community's openness to all Nim-related content. For those looking for inspiration, recordings of previous installments (2020–2024) are available on YouTube.

---

## 6. Show HN: Run GUIs as Scripts

**原文标题**: Show HN: Run GUIs as Scripts

**原文链接**: [https://github.com/skinnyjames/hokusai-pocket](https://github.com/skinnyjames/hokusai-pocket)

生成摘要时出错

---

## 7. 软体机器人无需电机和齿轮即可自如移动。

**原文标题**: A soft robot has no problem moving with no motor and no gears

**原文链接**: [https://engineering.princeton.edu/news/2026/04/08/soft-robot-has-no-problem-moving-no-motor-and-no-gears](https://engineering.princeton.edu/news/2026/04/08/soft-robot-has-no-problem-moving-no-motor-and-no-gears)

普林斯顿大学的研究人员开发出一种新型刚柔耦合混合机器人，无需电机、齿轮或外部气动控制即可运行。由 Emily Davidson 和 Glaucio Paulino 教授领导的团队将材料科学与折纸灵感设计相结合，创造出一种耐用且可编程的机器，能够执行复杂且可重复的运动。

该机器人的构造采用了 3D 打印的液晶弹性体（LCE），这是一种具有有序分子结构的聚合物。通过在打印过程中控制分子的取向，研究人员可以对特定的“铰链”进行编程，使其在受热时弯曲。为驱动这种运动，柔性印制电路板被直接嵌入到材料中。这些电路对特定区域进行精准电加热，促使聚合物收缩并触发折叠序列。

该设计的一个关键特征是集成了嵌入式温度传感器。这实现了“闭环控制”，使机器人的软件能够实时监控运动，并补偿微小误差或物理磨损。这确保了机器人可以恢复到原始形状，而不会出现软体机器人中常见的性能退化。作为演示，研究人员制作了一只折纸风格的千纸鹤，它通过电脉冲而非机械部件扇动翅膀。

该项目最初由 David Bershadsky 作为本科毕业论文构思，重点关注系统集成和可制造性。为了鼓励进一步开发，该团队发布了一款软件工具，以帮助他人设计类似的机器人系统。这些既“柔软”又耐用的机器在医疗植入物、体内药物输送以及危险环境探测等未来应用中具有巨大潜力。

---

## 8. GitHub 堆叠式 PR

**原文标题**: GitHub Stacked PRs

**原文链接**: [https://github.github.com/gh-stack/](https://github.github.com/gh-stack/)

GitHub has introduced native support for **Stacked PRs**, a feature designed to streamline the management of complex code changes. 

Instead of submitting a single, monolithic pull request, developers can now organize their work into an ordered sequence of smaller, "focused layers." Each layer exists as an individual PR that can be reviewed independently, making the feedback process more manageable and granular. 

The primary benefit of this workflow is the ability to land the entire sequence of changes simultaneously; once the stack is ready, all associated PRs can be merged with a single click. This approach improves code quality by encouraging smaller commits while maintaining the convenience of a unified release.

---

## 9. Zig 0.16.0 发布说明

**原文标题**: Zig 0.16.0 Release Notes

**原文链接**: [https://ziglang.org/download/0.16.0/release-notes.html](https://ziglang.org/download/0.16.0/release-notes.html)

Zig 0.16.0 版本由 244 名贡献者历经八个月开发而成。此版本引入了重大的架构变革，最引人注目的是 **I/O 接口化 (I/O as an Interface)**，它为标准库带来了对 I/O 组、批处理和取消操作的结构化支持。

**语言与编译器**
主要的语言变化包括弃用 `@cImport`，转而通过构建系统处理 C 语言转换。通用的 `@Type` 内建函数已被特定的类型创建函数取代，且 `switch` 语句现在支持紧凑型结构体 (packed structs) 和联合体。通过禁止运行时向量索引以及紧凑型结构体中的某些指针类型，安全性得到了进一步加强。此外，编译器现已采用 **LLVM 21**，改进了 x86_64 后端，并引入了全新的 ELF 链接器。

**标准库**
标准库正经历重大转型，旨在移除全局状态；环境变量和进程参数不再是全局的。关键数据结构已迁移至“非托管” (Unmanaged) 变体，且 `heap.ArenaAllocator` 现已实现线程安全且无锁。其他新增功能包括 AES-GCM-SIV 和 Ascon-AEAD 加密支持，以及重构的调试信息系统。

**目标平台支持**
Zig 细化了其目标分层系统（Tier 1–4）以明确支持级别。为了优先支持具有开放系统头文件的平台，已移除对专有操作系统（Solaris、AIX 和 z/OS）的支持。与此同时，针对 Power ISA 和 AArch64 等多个架构扩展了 CI 测试，且所有主要目标的堆栈回溯支持均得到了显著改进。

**工具链与质量**
此版本包含名为“Smith”的新型 AST 模糊测试工具 (fuzzer)，它已识别并修复了大量的编译器错误。构建系统现在允许本地包覆盖和项目本地依赖获取，进一步提升了 Zig 作为软件维护鲁棒工具链的能力。

---

## 10. Lumina – a statically typed web-native language for JavaScript and WASM

**原文标题**: Lumina – a statically typed web-native language for JavaScript and WASM

**原文链接**: [https://github.com/nyigoro/lumina-lang](https://github.com/nyigoro/lumina-lang)

生成摘要时出错

---

## 11. War as a Pretext: Gulf States Are Tightening the Screws on Speech–Again

**原文标题**: War as a Pretext: Gulf States Are Tightening the Screws on Speech–Again

**原文链接**: [https://www.eff.org/deeplinks/2026/04/war-pretext-gulf-states-are-tightening-screws-speech-again](https://www.eff.org/deeplinks/2026/04/war-pretext-gulf-states-are-tightening-screws-speech-again)

生成摘要时出错

---

## 12. Design and implementation of DuckDB internals

**原文标题**: Design and implementation of DuckDB internals

**原文链接**: [https://duckdb.org/library/design-and-implementation-of-duckdb-internals/](https://duckdb.org/library/design-and-implementation-of-duckdb-internals/)

生成摘要时出错

---

## 13. Write less code, be more responsible

**原文标题**: Write less code, be more responsible

**原文链接**: [https://blog.orhun.dev/code-responsibly/](https://blog.orhun.dev/code-responsibly/)

生成摘要时出错

---

## 14. MOS tech 6502 8-bit microprocessor in pure SQL powered by Postgres

**原文标题**: MOS tech 6502 8-bit microprocessor in pure SQL powered by Postgres

**原文链接**: [https://github.com/lasect/pg_6502](https://github.com/lasect/pg_6502)

生成摘要时出错

---

## 15. How to make Firefox builds 17% faster

**原文标题**: How to make Firefox builds 17% faster

**原文链接**: [https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/](https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/)

生成摘要时出错

---

## 16. Building a CLI for all of Cloudflare

**原文标题**: Building a CLI for all of Cloudflare

**原文链接**: [https://blog.cloudflare.com/cf-cli-local-explorer/](https://blog.cloudflare.com/cf-cli-local-explorer/)

生成摘要时出错

---

## 17. The Great Majority: Body Snatching and Burial Reform in 19th-Century Britain

**原文标题**: The Great Majority: Body Snatching and Burial Reform in 19th-Century Britain

**原文链接**: [https://publicdomainreview.org/essay/the-great-majority/](https://publicdomainreview.org/essay/the-great-majority/)

生成摘要时出错

---

## 18. I just want simple S3

**原文标题**: I just want simple S3

**原文链接**: [https://blog.feld.me/posts/2026/04/i-just-want-simple-s3/](https://blog.feld.me/posts/2026/04/i-just-want-simple-s3/)

生成摘要时出错

---

## 19. All 5 units of life's genetic code were just discovered in an asteroid sample

**原文标题**: All 5 units of life's genetic code were just discovered in an asteroid sample

**原文链接**: [https://theconversation.com/all-5-fundamental-units-of-lifes-genetic-code-were-just-discovered-in-an-asteroid-sample-278099](https://theconversation.com/all-5-fundamental-units-of-lifes-genetic-code-were-just-discovered-in-an-asteroid-sample-278099)

生成摘要时出错

---

## 20. To teach in the era of ChatGPT is to know pain

**原文标题**: To teach in the era of ChatGPT is to know pain

**原文链接**: [https://arstechnica.com/science/2026/04/to-teach-in-the-time-of-chatgpt-is-to-know-pain/](https://arstechnica.com/science/2026/04/to-teach-in-the-time-of-chatgpt-is-to-know-pain/)

生成摘要时出错

---

## 21. Rust Threads on the GPU

**原文标题**: Rust Threads on the GPU

**原文链接**: [https://www.vectorware.com/blog/threads-on-gpu/](https://www.vectorware.com/blog/threads-on-gpu/)

生成摘要时出错

---

## 22. Amazon acquires Apple's satellite partner

**原文标题**: Amazon acquires Apple's satellite partner

**原文链接**: [https://sixcolors.com/link/2026/04/amazon-acquires-apples-satellite-partner/](https://sixcolors.com/link/2026/04/amazon-acquires-apples-satellite-partner/)

生成摘要时出错

---

## 23. Google, Microsoft, Meta All Tracking You Even When You Opt Out

**原文标题**: Google, Microsoft, Meta All Tracking You Even When You Opt Out

**原文链接**: [https://www.404media.co/google-microsoft-meta-all-tracking-you-even-when-you-opt-out-according-to-an-independent-audit/](https://www.404media.co/google-microsoft-meta-all-tracking-you-even-when-you-opt-out-according-to-an-independent-audit/)

生成摘要时出错

---

## 24. On hacker mindset

**原文标题**: On hacker mindset

**原文链接**: [https://www.henrikkarlsson.xyz/p/hacker-mindset](https://www.henrikkarlsson.xyz/p/hacker-mindset)

生成摘要时出错

---

## 25. Air Powered Segment Display? [video]

**原文标题**: Air Powered Segment Display? [video]

**原文链接**: [https://www.youtube.com/watch?v=E1BLGpE5zH0](https://www.youtube.com/watch?v=E1BLGpE5zH0)

生成摘要时出错

---

## 26. Single-Dose Creatine Reduces Sleep Deprivation-Induced Deterioration

**原文标题**: Single-Dose Creatine Reduces Sleep Deprivation-Induced Deterioration

**原文链接**: [https://www.mdpi.com/2072-6643/18/8/1192](https://www.mdpi.com/2072-6643/18/8/1192)

生成摘要时出错

---

## 27. Tracking down a 25% Regression on LLVM RISC-V

**原文标题**: Tracking down a 25% Regression on LLVM RISC-V

**原文链接**: [https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/](https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/)

生成摘要时出错

---

## 28. Stanford HAI Index Report 2026

**原文标题**: Stanford HAI Index Report 2026

**原文链接**: [https://hai.stanford.edu/ai-index/2026-ai-index-report](https://hai.stanford.edu/ai-index/2026-ai-index-report)

生成摘要时出错

---

## 29. My brother's minesweeper site (minesweeper.org) has been running for 27 years

**原文标题**: My brother's minesweeper site (minesweeper.org) has been running for 27 years

**原文链接**: [https://restlessforge.substack.com/p/sweeping-for-mines](https://restlessforge.substack.com/p/sweeping-for-mines)

生成摘要时出错

---

## 30. PyCon US 2026: Why we're asking you to think about your hotel reservation

**原文标题**: PyCon US 2026: Why we're asking you to think about your hotel reservation

**原文链接**: [https://pyfound.blogspot.com/2026/04/pycon-us-2026-hotels.html](https://pyfound.blogspot.com/2026/04/pycon-us-2026-hotels.html)

生成摘要时出错

---

## 31. N-Day-Bench – Can LLMs find real vulnerabilities in real codebases?

**原文标题**: N-Day-Bench – Can LLMs find real vulnerabilities in real codebases?

**原文链接**: [https://ndaybench.winfunc.com](https://ndaybench.winfunc.com)

生成摘要时出错

---

## 32. GAIA – Open-source framework for building AI agents that run on local hardware

**原文标题**: GAIA – Open-source framework for building AI agents that run on local hardware

**原文链接**: [https://amd-gaia.ai/docs](https://amd-gaia.ai/docs)

生成摘要时出错

---

## 33. Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets

**原文标题**: Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets

**原文链接**: [https://github.com/sterlingcrispin/nothing-ever-happens](https://github.com/sterlingcrispin/nothing-ever-happens)

生成摘要时出错

---

## 34. Anastasia (1997) live action reference material

**原文标题**: Anastasia (1997) live action reference material

**原文链接**: [https://lostmediawiki.com/Anastasia_(partially_found_live-action_reference_material_for_Don_Bluth_animated_film;_1997)](https://lostmediawiki.com/Anastasia_(partially_found_live-action_reference_material_for_Don_Bluth_animated_film;_1997))

生成摘要时出错

---

## 35. US appeals court declares 158-year-old home distilling ban unconstitutional

**原文标题**: US appeals court declares 158-year-old home distilling ban unconstitutional

**原文链接**: [https://nypost.com/2026/04/11/us-news/us-appeals-court-declares-158-year-old-home-distilling-ban-unconstitutional/](https://nypost.com/2026/04/11/us-news/us-appeals-court-declares-158-year-old-home-distilling-ban-unconstitutional/)

生成摘要时出错

---

## 36. What we learned building a Rust runtime for TypeScript

**原文标题**: What we learned building a Rust runtime for TypeScript

**原文链接**: [https://encore.dev/blog/rust-runtime](https://encore.dev/blog/rust-runtime)

生成摘要时出错

---

## 37. The secrets of the Shinkansen

**原文标题**: The secrets of the Shinkansen

**原文链接**: [https://www.worksinprogress.news/p/the-secret-behind-japans-railways](https://www.worksinprogress.news/p/the-secret-behind-japans-railways)

生成摘要时出错

---

## 38. Show HN: Ithihāsas – a character explorer for Hindu epics, built in a few hours

**原文标题**: Show HN: Ithihāsas – a character explorer for Hindu epics, built in a few hours

**原文链接**: [https://www.ithihasas.in](https://www.ithihasas.in)

生成摘要时出错

---

## 39. I Found It: The Best Free Restaurant Bread in America

**原文标题**: I Found It: The Best Free Restaurant Bread in America

**原文链接**: [https://www.theatlantic.com/magazine/2026/05/best-free-restaurant-bread-america/686582/](https://www.theatlantic.com/magazine/2026/05/best-free-restaurant-bread-america/686582/)

生成摘要时出错

---

## 40. Repository Pattern with Hygienic Macros in Scheme – Lisp

**原文标题**: Repository Pattern with Hygienic Macros in Scheme – Lisp

**原文链接**: [https://jointhefreeworld.org/blog/articles/lisps/functional-repository-pattern-in-scheme-with-macros/index.html](https://jointhefreeworld.org/blog/articles/lisps/functional-repository-pattern-in-scheme-with-macros/index.html)

生成摘要时出错

---

## 41. Visualizing CPU Pipelining (2024)

**原文标题**: Visualizing CPU Pipelining (2024)

**原文链接**: [https://timmastny.com/blog/visualizing-cpu-pipelining/](https://timmastny.com/blog/visualizing-cpu-pipelining/)

生成摘要时出错

---

## 42. EasyPost (YC S13) Is Hiring

**原文标题**: EasyPost (YC S13) Is Hiring

**原文链接**: [https://www.easypost.com/careers](https://www.easypost.com/careers)

生成摘要时出错

---

## 43. Servo is now available on crates.io

**原文标题**: Servo is now available on crates.io

**原文链接**: [https://servo.org/blog/2026/04/13/servo-0.1.0-release/](https://servo.org/blog/2026/04/13/servo-0.1.0-release/)

生成摘要时出错

---

## 44. I shipped a transaction bug, so I built a linter

**原文标题**: I shipped a transaction bug, so I built a linter

**原文链接**: [https://leonh.fr/posts/go-transaction-linter/](https://leonh.fr/posts/go-transaction-linter/)

生成摘要时出错

---

## 45. Make tmux pretty and usable (2024)

**原文标题**: Make tmux pretty and usable (2024)

**原文链接**: [https://hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/](https://hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/)

生成摘要时出错

---

## 46. The Case Against Gameplay Loops (2024)

**原文标题**: The Case Against Gameplay Loops (2024)

**原文链接**: [https://blog.joeyschutz.com/the-case-against-gameplay-loops/](https://blog.joeyschutz.com/the-case-against-gameplay-loops/)

生成摘要时出错

---

## 47. B-trees and database indexes (2024)

**原文标题**: B-trees and database indexes (2024)

**原文链接**: [https://planetscale.com/blog/btrees-and-database-indexes](https://planetscale.com/blog/btrees-and-database-indexes)

生成摘要时出错

---

## 48. Android now stops you sharing your location in photos

**原文标题**: Android now stops you sharing your location in photos

**原文链接**: [https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/](https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/)

生成摘要时出错

---

## 49. Initial mainline video capture and camera support for Rockchip RK3588

**原文标题**: Initial mainline video capture and camera support for Rockchip RK3588

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/mainline-video-capture-and-camera-support-for-rockchip-rk3588.html](https://www.collabora.com/news-and-blog/news-and-events/mainline-video-capture-and-camera-support-for-rockchip-rk3588.html)

生成摘要时出错

---

## 50. The AI revolution in math has arrived

**原文标题**: The AI revolution in math has arrived

**原文链接**: [https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)

生成摘要时出错

---

## 51. All elementary functions from a single binary operator

**原文标题**: All elementary functions from a single binary operator

**原文链接**: [https://arxiv.org/abs/2603.21852](https://arxiv.org/abs/2603.21852)

生成摘要时出错

---

## 52. MEMS Array Chip Can Project Video the Size of a Grain of Sand

**原文标题**: MEMS Array Chip Can Project Video the Size of a Grain of Sand

**原文链接**: [https://spectrum.ieee.org/mems-photonics](https://spectrum.ieee.org/mems-photonics)

生成摘要时出错

---

## 53. If you started a company two years ago, many assumptions are no longer true

**原文标题**: If you started a company two years ago, many assumptions are no longer true

**原文链接**: [https://steveblank.com/2026/03/17/your-startup-is-probably-dead-on-arrival/](https://steveblank.com/2026/03/17/your-startup-is-probably-dead-on-arrival/)

生成摘要时出错

---

## 54. Stolen Rockstar Games analytics data leaked by extortion gang

**原文标题**: Stolen Rockstar Games analytics data leaked by extortion gang

**原文链接**: [https://www.bleepingcomputer.com/news/security/stolen-rockstar-games-analytics-data-leaked-by-extortion-gang/](https://www.bleepingcomputer.com/news/security/stolen-rockstar-games-analytics-data-leaked-by-extortion-gang/)

生成摘要时出错

---

## 55. Math Is Still Catching Up to the Mysterious Genius of Srinivasa Ramanujan (2024)

**原文标题**: Math Is Still Catching Up to the Mysterious Genius of Srinivasa Ramanujan (2024)

**原文链接**: [https://www.quantamagazine.org/srinivasa-ramanujan-was-a-genius-math-is-still-catching-up-20241021/](https://www.quantamagazine.org/srinivasa-ramanujan-was-a-genius-math-is-still-catching-up-20241021/)

生成摘要时出错

---

## 56. Man suspected of Molotov attack Sam Altmans home charged with attempted murder

**原文标题**: Man suspected of Molotov attack Sam Altmans home charged with attempted murder

**原文链接**: [https://www.theregister.com/2026/04/14/altman_attempted_murder/](https://www.theregister.com/2026/04/14/altman_attempted_murder/)

生成摘要时出错

---

## 57. US Treasury Seeking Access to Anthropic's Mythos to Find Flaws

**原文标题**: US Treasury Seeking Access to Anthropic's Mythos to Find Flaws

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-14/us-treasury-seeking-access-to-anthropic-s-mythos-to-find-flaws](https://www.bloomberg.com/news/articles/2026-04-14/us-treasury-seeking-access-to-anthropic-s-mythos-to-find-flaws)

生成摘要时出错

---

## 58. I ran Gemma 4 as a local model in Codex CLI

**原文标题**: I ran Gemma 4 as a local model in Codex CLI

**原文链接**: [https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4](https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4)

生成摘要时出错

---

## 59. Exploiting the most prominent AI agent benchmarks

**原文标题**: Exploiting the most prominent AI agent benchmarks

**原文链接**: [https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

生成摘要时出错

---

## 60. Introduction to Obsidian

**原文标题**: Introduction to Obsidian

**原文链接**: [https://bryanhogan.com/blog/obsidian-introduction](https://bryanhogan.com/blog/obsidian-introduction)

生成摘要时出错

---

## 61. Why it’s impossible to measure England’s coastline

**原文标题**: Why it’s impossible to measure England’s coastline

**原文链接**: [https://www.bbc.com/travel/article/20260410-why-its-impossible-to-measure-englands-coastline](https://www.bbc.com/travel/article/20260410-why-its-impossible-to-measure-englands-coastline)

生成摘要时出错

---

## 62. The Journal of C Language Translation

**原文标题**: The Journal of C Language Translation

**原文链接**: [http://jclt.iecc.com/](http://jclt.iecc.com/)

生成摘要时出错

---

## 63. Microsoft isn't removing Copilot from Windows 11, it's just renaming it

**原文标题**: Microsoft isn't removing Copilot from Windows 11, it's just renaming it

**原文链接**: [https://www.neowin.net/opinions/microsoft-isnt-removing-copilot-from-windows-11-its-just-renaming-it/](https://www.neowin.net/opinions/microsoft-isnt-removing-copilot-from-windows-11-its-just-renaming-it/)

生成摘要时出错

---

## 64. Show HN: A stateful UI runtime for reactive web apps in Go

**原文标题**: Show HN: A stateful UI runtime for reactive web apps in Go

**原文链接**: [https://github.com/doors-dev/doors](https://github.com/doors-dev/doors)

生成摘要时出错

---

## 65. Tool to explore regularly sampled time series

**原文标题**: Tool to explore regularly sampled time series

**原文链接**: [https://github.com/rajivsam/tseda](https://github.com/rajivsam/tseda)

生成摘要时出错

---

## 66. TanStack Start Now Support React Server Components

**原文标题**: TanStack Start Now Support React Server Components

**原文链接**: [https://tanstack.com/blog/react-server-components](https://tanstack.com/blog/react-server-components)

生成摘要时出错

---

## 67. The Future of Everything Is Lies, I Guess: Safety

**原文标题**: The Future of Everything Is Lies, I Guess: Safety

**原文链接**: [https://aphyr.com/posts/417-the-future-of-everything-is-lies-i-guess-safety](https://aphyr.com/posts/417-the-future-of-everything-is-lies-i-guess-safety)

生成摘要时出错

---

## 68. Can Claude Fly a Plane?

**原文标题**: Can Claude Fly a Plane?

**原文链接**: [https://so.long.thanks.fish/can-claude-fly-a-plane/](https://so.long.thanks.fish/can-claude-fly-a-plane/)

生成摘要时出错

---

## 69. Just Enough Chimera Linux

**原文标题**: Just Enough Chimera Linux

**原文链接**: [https://www.dwarmstrong.org/chimera-install-zfs/](https://www.dwarmstrong.org/chimera-install-zfs/)

生成摘要时出错

---

## 70. This year’s insane timeline of hacks

**原文标题**: This year’s insane timeline of hacks

**原文链接**: [https://ringmast4r.substack.com/p/we-may-be-living-through-the-most](https://ringmast4r.substack.com/p/we-may-be-living-through-the-most)

生成摘要时出错

---

## 71. We need Post-Quantum Cryptography more than ever

**原文标题**: We need Post-Quantum Cryptography more than ever

**原文链接**: [https://hawksley.dev/blog/need-for-post-quantum-cryptography/](https://hawksley.dev/blog/need-for-post-quantum-cryptography/)

生成摘要时出错

---

## 72. A name is succession, legacy and celebration in Japan's Kabuki theater

**原文标题**: A name is succession, legacy and celebration in Japan's Kabuki theater

**原文链接**: [https://apnews.com/article/kabuki-name-succession-japan-tradition-theater-d1e9621bc91385498314f36e1481b6fd](https://apnews.com/article/kabuki-name-succession-japan-tradition-theater-d1e9621bc91385498314f36e1481b6fd)

生成摘要时出错

---

## 73. Ascending into the Realm of Japanese Charts

**原文标题**: Ascending into the Realm of Japanese Charts

**原文链接**: [https://www.chartography.net/p/ascending-into-the-realm-of-japanese](https://www.chartography.net/p/ascending-into-the-realm-of-japanese)

生成摘要时出错

---

## 74. Michigan 'digital age' bills pulled after privacy concerns raised

**原文标题**: Michigan 'digital age' bills pulled after privacy concerns raised

**原文链接**: [https://www.thecentersquare.com/michigan/article_7ca4e268-4a68-42fb-9042-f9d8604ebd7f.html](https://www.thecentersquare.com/michigan/article_7ca4e268-4a68-42fb-9042-f9d8604ebd7f.html)

生成摘要时出错

---

## 75. Claude Code may be burning your limits with invisible tokens

**原文标题**: Claude Code may be burning your limits with invisible tokens

**原文链接**: [https://efficienist.com/claude-code-may-be-burning-your-limits-with-invisible-tokens-you-cant-see-or-audit/](https://efficienist.com/claude-code-may-be-burning-your-limits-with-invisible-tokens-you-cant-see-or-audit/)

生成摘要时出错

---

## 76. UpDown: Efficient Manycore based on Many Threading & Scalable Memory Parallelism

**原文标题**: UpDown: Efficient Manycore based on Many Threading & Scalable Memory Parallelism

**原文链接**: [https://people.cs.uchicago.edu/~aachien/lssg/research/10x10/ics26-single-chip-updown.pdf](https://people.cs.uchicago.edu/~aachien/lssg/research/10x10/ics26-single-chip-updown.pdf)

生成摘要时出错

---

## 77. The economics of software teams: Why most engineering orgs are flying blind

**原文标题**: The economics of software teams: Why most engineering orgs are flying blind

**原文链接**: [https://www.viktorcessan.com/the-economics-of-software-teams/](https://www.viktorcessan.com/the-economics-of-software-teams/)

生成摘要时出错

---

## 78. Bear Roll – Daily roll of Bear Blog's top posts

**原文标题**: Bear Roll – Daily roll of Bear Blog's top posts

**原文链接**: [https://bearroll.dev/](https://bearroll.dev/)

生成摘要时出错

---

## 79. DIY Soft Drinks

**原文标题**: DIY Soft Drinks

**原文链接**: [https://blinry.org/diy-soft-drinks/](https://blinry.org/diy-soft-drinks/)

生成摘要时出错

---

## 80. State of Homelab 2026

**原文标题**: State of Homelab 2026

**原文链接**: [https://mrlokans.work/posts/state-of-homelab-2026/](https://mrlokans.work/posts/state-of-homelab-2026/)

生成摘要时出错

---

## 81. Tax Wrapped 2025

**原文标题**: Tax Wrapped 2025

**原文链接**: [https://taxwrapped.com](https://taxwrapped.com)

生成摘要时出错

---

## 82. Roblox devs now need a subscription to share their games freely

**原文标题**: Roblox devs now need a subscription to share their games freely

**原文链接**: [https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166)

生成摘要时出错

---

## 83. Verification Debt Is Your Next Headache

**原文标题**: Verification Debt Is Your Next Headache

**原文链接**: [https://leadership.garden/verification-debt/](https://leadership.garden/verification-debt/)

生成摘要时出错

---

## 84. Bring Back Idiomatic Design (2023)

**原文标题**: Bring Back Idiomatic Design (2023)

**原文链接**: [https://essays.johnloeber.com/p/4-bring-back-idiomatic-design](https://essays.johnloeber.com/p/4-bring-back-idiomatic-design)

生成摘要时出错

---

## 85. Seven countries now generate nearly all their electricity from renewables (2024)

**原文标题**: Seven countries now generate nearly all their electricity from renewables (2024)

**原文链接**: [https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html](https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html)

生成摘要时出错

---

## 86. JVM Options Explorer

**原文标题**: JVM Options Explorer

**原文链接**: [https://chriswhocodes.com/vm-options-explorer.html](https://chriswhocodes.com/vm-options-explorer.html)

生成摘要时出错

---

## 87. New Orleans's Car-Crash Conspiracy

**原文标题**: New Orleans's Car-Crash Conspiracy

**原文链接**: [https://www.newyorker.com/magazine/2026/04/20/the-car-crash-conspiracy](https://www.newyorker.com/magazine/2026/04/20/the-car-crash-conspiracy)

生成摘要时出错

---

## 88. Show HN: boringBar – a taskbar-style dock replacement for macOS

**原文标题**: Show HN: boringBar – a taskbar-style dock replacement for macOS

**原文链接**: [https://boringbar.app/](https://boringbar.app/)

生成摘要时出错

---

## 89. An open letter to the UK Government on digital privacy

**原文标题**: An open letter to the UK Government on digital privacy

**原文链接**: [https://www.jimmyff.co.uk/blog/open-letter-uk-digital-privacy/](https://www.jimmyff.co.uk/blog/open-letter-uk-digital-privacy/)

生成摘要时出错

---

