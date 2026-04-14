# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-14.md)

*最后自动更新时间: 2026-04-14 18:30:53*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 2 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 3 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 4 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 5 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 6 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 7 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 8 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 9 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 10 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 11 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 12 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 13 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 14 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 15 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 16 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 17 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 18 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 19 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 20 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 21 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 22 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 23 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 24 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 25 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 26 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 27 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 28 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 29 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 30 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 31 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 32 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 33 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 34 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 35 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 36 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 37 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 38 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 39 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 40 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 41 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 42 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 43 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 44 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 45 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 46 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 47 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 48 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 49 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 50 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 51 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 52 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 53 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 54 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 55 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 56 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 57 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 58 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 59 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 60 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 61 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 62 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 63 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 64 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 65 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 66 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 67 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 68 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 69 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 70 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 71 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 72 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 73 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 74 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 75 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 76 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 77 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 78 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 79 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 80 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 81 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 82 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 83 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 84 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 85 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 86 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 87 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 88 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 89 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 90 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 91 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 92 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 93 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 94 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 95 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 96 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 97 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 98 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 99 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 100 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 101 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 102 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 103 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 104 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 105 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 106 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 107 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 108 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 109 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 110 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 111 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 112 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 113 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 114 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 115 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 116 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 117 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 118 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 119 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 120 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 121 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 122 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 123 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 124 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 125 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 126 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 127 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 128 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 129 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 130 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 131 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 132 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 133 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 134 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 135 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 136 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 137 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 138 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 139 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 140 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 141 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 142 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 143 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 144 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 145 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 146 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 147 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 148 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 149 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 150 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 151 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 152 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 153 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 154 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 155 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 156 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 157 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 158 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 159 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 160 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 161 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 162 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 163 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 164 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 165 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 166 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 167 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 168 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 169 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 170 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 171 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 172 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 173 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 174 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 175 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 176 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 177 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 178 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 179 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 180 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 181 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 182 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 183 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 184 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 185 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 186 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 187 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 188 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 189 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 190 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 191 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 192 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 193 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 194 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 195 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 196 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 197 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 198 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 199 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 200 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 201 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 202 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 203 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 204 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 205 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 206 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 207 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 208 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 209 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 210 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 211 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 212 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 213 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 214 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 215 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 216 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 217 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 218 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 219 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 220 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 221 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 222 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 223 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 224 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 225 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 226 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 227 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 228 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 229 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 230 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 231 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 232 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 233 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 234 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 235 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 236 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 237 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 238 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 239 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 240 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 241 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 242 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 243 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 244 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 245 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 246 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 247 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 248 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 249 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 250 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 251 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 252 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 253 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 254 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 255 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 256 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 257 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 258 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 259 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 260 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 261 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 262 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 263 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 264 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 265 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 266 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 267 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 268 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 269 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 270 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 271 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 272 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 273 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 274 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 275 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 276 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 277 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 278 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 279 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 280 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 281 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 282 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 283 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 284 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 285 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 286 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 287 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 288 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 289 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 290 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 291 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 292 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 293 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 294 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 295 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 296 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 297 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 298 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 299 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 300 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 301 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 302 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 303 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 304 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 305 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 306 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 307 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 308 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 309 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 310 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 311 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 312 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 313 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 314 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 315 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 316 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 317 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 318 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 319 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 320 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 321 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 322 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 323 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 324 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 325 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 326 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 327 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 328 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 329 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 330 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 331 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 332 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 333 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 334 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 335 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 336 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 337 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 338 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 339 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 340 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 341 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 342 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 343 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 344 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 345 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 346 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 347 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 348 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 349 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 350 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 351 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 352 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 353 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 354 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 355 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 356 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 357 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 358 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 359 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 360 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 361 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 362 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 363 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 364 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 365 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 366 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 367 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 368 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 369 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 370 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 371 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 372 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 373 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 374 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 375 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 376 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 377 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 378 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 379 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 380 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 381 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 382 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 383 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 384 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 385 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 386 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 387 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 388 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 389 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 390 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
