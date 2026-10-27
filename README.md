# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-27.md)

*最后自动更新时间: 2026-10-27 21:33:53*
## 1. 精灵 4

**原文标题**: Genie 4

**原文链接**: [https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

您提供的内容仅包含标题“Genie 4”和“了解更多”提示，并未包含文章的正文内容。

为了为您提供准确、简明的摘要，**请粘贴文章全文或提供更多关于内容的细节。**

如果您是指最近发布的某项具体技术，请注意：
*   **Google DeepMind** 最近发布了 **Genie 2**，这是一个用于生成交互式 3D 世界的基础模型。
*   此外还有一个 **Genie AI** 平台，用于法律模板和起草。

一旦您提供了文章的正文，我很乐意在 300 字的限制内为您总结主要观点和关键信息。

---

## 2. Ghostty 1.4.0

**原文标题**: Ghostty 1.4.0

**原文链接**: [https://ghostty.org/docs/install/release-notes/1-4-0](https://ghostty.org/docs/install/release-notes/1-4-0)

Ghostty 1.4.0 于 2026 年 10 月 27 日发布，是一次重大的版本更新，带来了显著的性能优化、内存效率提升和全面的协议支持。该版本凝聚了 172 位贡献者历时七个月的开发成果。

**核心亮点：**

*   **性能与内存：** Ghostty 现已采用多线程 PTY 读取技术，使 macOS 上的 I/O 吞吐量提升高达 55%。ASCII 和中日韩（CJK）文本的终端处理速度大幅提高，启动时间进一步缩短。通过透明的回滚内容压缩（可减少 70%–90% 的物理内存占用）以及对隐藏标签页动态释放 GPU 资源，内存使用得到了深度优化。
*   **Kitty 图形与剪贴板：** Ghostty 是首个实现 Kitty 图形协议 100% 覆盖（包括动画和相对定位）的非 Kitty 终端。通过 SIMD 技术，其解析速度提升了 16 倍。此外，它还实现了 Kitty 剪贴板协议 (OSC 5522)，支持用户读写图片和 HTML 等非文本数据。
*   **Linux 与 macOS 更新：** Linux/GTK 用户迎来了全新的 OpenGL 渲染管线，在分数缩放下也能提供清晰的文本显示，并增加了分屏拖放功能。对于苹果用户，该版本全面兼容 macOS 27 (Golden Gate)，并修复了多处视觉回归问题。
*   **SSH 集成：** 新增的 `ghostty +ssh` 命令行包装器通过自动安装 terminfo 并转发环境变量简化了远程会话，确保在不同 Shell 中获得一致的体验。
*   **安全与仿真：** 此版本修复了十多个安全漏洞，包括粘贴保护、恶意 Kitty 图形命令以及不安全的 URL 处理等问题。终端仿真精度得到提升，能更好地匹配 xterm 标准，并已通过 CI 中的 `esctest` 测试套件。

Ghostty 1.4.0 依然兼容 macOS 13+ 及 64 位 Linux，继续履行其作为高性能、非营利终端模拟器的使命。

---

## 3. Tailscale SSH: Investigation and remediation update

**原文标题**: Tailscale SSH: Investigation and remediation update

**原文链接**: [https://tailscale.com/ssh-investigation-update](https://tailscale.com/ssh-investigation-update)

Tailscale 已发布针对 Tailscale SSH 中发现的漏洞的安全更新，这些漏洞主要涉及**权限提升**。在外部专家的支持下，调查发现，根据特定的系统配置，授权用户可能会获得超出其配置的本地用户级别的提升权限。

**修复措施与时间线**
Tailscale 工程师已针对大部分已发现的问题开发了修复方案。修复后的客户端版本目前正在测试中，计划于 **2026 年 10 月 27 日（周二）**结束前发布。虽然公司并不建议所有用户完全禁用 Tailscale SSH，但他们正严肃对待这些漏洞。

**针对客户的建议操作**
在补丁发布之前，Tailscale 建议采取以下缓解步骤：
*   **禁用 SSH 转发：** 在 tailscaled 服务环境中设置 `TS_SSH_DISABLE_FORWARDING=1` 并重启服务。这可以在不完全禁用 SSH 的情况下解决几个最严重的发现。
*   **审查访问策略：** 确保 SSH 访问严格限制在必要的用户和设备。
*   **限制敏感系统：** 暂时收紧高安全环境的访问控制。
*   **准备更新：** 准备好在修复后的 Tailscale 客户端发布后立即进行部署。

**后续步骤**
补丁发布后，Tailscale 将发布正式的安全公告，详细说明漏洞、受影响的版本及其技术影响。随后将发布一篇详细的技术博客文章，解释根本原因以及为解决这些问题而实施的工程变更。对特定环境有疑问的客户请联系 Tailscale 支持团队。

---

## 4. Survival LLM：运行在您个人电脑上的 AI 助手与应急知识库

**原文标题**: Survival LLM: AI assistant and emergency library that runs on your own computer

**原文链接**: [https://www.brangus.io/survival-llm](https://www.brangus.io/survival-llm)

**Survival LLM** 是一款免费、开源的 AI 助手和应急知识库，旨在完全脱离互联网运行。它专门用于在停电或危机期间提供关键信息，允许用户搜索急救、食品安全、水净化及维修等方面的救命指南。

**核心功能：**
*   **隐私与离线访问：** 初始设置完成后，所有处理均在用户电脑本地进行，数据不会离开设备。
*   **经过验证的来源：** 为减少 AI “幻觉”，该工具会为每个回答引用来源。其库中包含约 93 万篇维基百科文章、WikiMed、FEMA (Ready.gov) 指南、CDC 健康数据、美国军事手册、iFixit 维修指南以及 wikiHow。
*   **硬件兼容性：** 该应用兼容 Apple Silicon Mac (macOS 14+) 和 Windows 10/11。它会根据电脑内存自动下载 AI 模型，涵盖从适用于 16GB 系统的轻量模型 (IBM Granite) 到适用于 128GB 以上系统的高性能模型 (NVIDIA Nemotron)。
*   **自定义：** 用户可以导入自己的 PDF、Word 文档和电子书（如设备手册或个人应急预案），供 AI 进行索引和搜索。

**设置与运行：**
初始安装需要互联网连接以下载 AI 模型和知识库（根据版本不同，大小在 3GB 到 19GB 之间）。设置通常需要 20 分钟到 2.5 小时。在移动端使用时，MacBook Pro 的电池可支持约 100 到 300 次查询，适合配合小型便携式电源使用。

最终，Survival LLM 充当了一个本地化的“知识堡垒”，确保在传统通信网络失效时，关键信息依然触手可及。

---

## 5. 全新 14 英寸 MacBook Pro (搭载 M6 芯片)

**原文标题**: New 14‑inch MacBook Pro with M6

**原文链接**: [https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/](https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)

苹果发布了搭载下一代 **M6 芯片**的新款 14 英寸 MacBook Pro。发布日期为 2026 年 10 月 27 日，本次发布重点强调了端侧 AI 能力、专业性能以及创纪录电池续航的巨大飞跃。

**关键性能升级**
M6 芯片配备 12 核 CPU 和集成“神经加速器”的 12 核 GPU。与 M5 相比，M6 的图形处理速度提升了 30%，AI 工作负载处理速度提升了 25%。对于从 M1 升级的用户，性能提升更为惊人，AI 性能最高可达 13 倍。该设备支持最高 32GB 统一内存，并内置专门为本地运行大语言模型 (LLM) 优化的双 16 核神经网络引擎。

**硬件与连接性**
*   **电池续航：** 提供长达 24 小时的续航时间，为 Mac 史上之最。
*   **显示屏：** 配备 Liquid 视网膜 XDR 显示屏，并新增纳米纹理玻璃选项以最大限度减少眩光。
*   **连接性：** 升级至 Wi-Fi 7 和蓝牙 6，配备三个雷雳 4 端口、MagSafe 3 接口以及一个 HDMI 端口。
*   **摄像头：** 配备支持“桌上视角”功能的 1200 万像素人物居中摄像头。

**macOS 27 "Golden Gate"**
硬件随 macOS 27 同步推出，该系统引入了 **Siri AI**——一个更具个性化的助手，能够利用屏幕内容理解上下文并执行任务。该系统还采用了“液态玻璃 (Liquid Glass)”设计优化，允许用户自定义界面的色调和透明度。

**可持续性与发售信息**
新款 MacBook Pro 采用 45% 的再生材料打造，其中包括 100% 再生铝和再生钽。预订将于 2026 年 10 月 28 日开始，11 月 6 日正式发售。在印度市场，M6 机型的起售价为 **239,900 印度卢比**。

---

## 6. 利用 Claude 加速药物研发的早期进展

**原文标题**: Early progress on accelerating drug development with Claude

**原文链接**: [https://www.anthropic.com/research/early-progress-drug-development](https://www.anthropic.com/research/early-progress-drug-development)

Anthropic’s life sciences team is accelerating drug development by integrating Claude into every stage of the process, from initial molecule design to regulatory filings and clinical trial planning. Through partnerships with six major organizations and its own internal research, Anthropic aims to address bottlenecks distributed throughout the drug discovery lifecycle.

Key case studies demonstrate Claude's impact:
*   **Generate Biomedicines:** Used Claude to reengineer CAR T-cell therapy, creating a genetic design 70% shorter and 10 times more effective at producing receptors in lab tests.
*   **Divergence Labs:** Generated 35,000 antibody designs for food allergies, identifying "hits" that dislodge IgE more effectively than current medications.
*   **BigHat Biosciences:** Optimized antibody leads, improving binding affinity by over 10x and significantly increasing thermal stability.
*   **Enveda:** Reduced manufacturing paperwork review time by 89% and drafted complex regulatory documents in hours rather than months.
*   **Bristol Myers Squibb:** Leveraging Claude to analyze proprietary data and assess the success probability of clinical trial plans.

Additionally, Anthropic acquired **Mithril Medicine**, which used Claude to manage the operations of a one-person drug program for rare muscular dystrophy, reaching promising results in mice in less than 18 months. Human clinical trials are targeted for late 2028.

To support the broader scientific community, Anthropic has launched **Claude Science** (an AI workbench), provided research credits, and created the **Life Sciences Verification Program** to allow trusted researchers to bypass certain safeguards that might otherwise impede legitimate biological study. Ultimately, Anthropic aims to transform the economics of biotechnology, enabling smaller teams to tackle more ambitious medical challenges.

---

## 7. 美国与加拿大消失萤火虫物种的考查

**原文标题**: An examination of lost firefly species of the US and Canada

**原文链接**: [https://journaloflostspecies.org/index.php/jls/article/view/37/33](https://journaloflostspecies.org/index.php/jls/article/view/37/33)

生成摘要时出错

---

## 8. Classification of Finite Simple Groups Formalized in Lean

**原文标题**: Classification of Finite Simple Groups Formalized in Lean

**原文链接**: [https://cfsg.axiommath.ai/](https://cfsg.axiommath.ai/)

生成摘要时出错

---

## 9. New iMac with M6

**原文标题**: New iMac with M6

**原文链接**: [https://www.apple.com/imac/](https://www.apple.com/imac/)

生成摘要时出错

---

## 10. Python's experimental JIT to be removed

**原文标题**: Python's experimental JIT to be removed

**原文链接**: [https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 2 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 3 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 4 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 5 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 6 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 7 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 8 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 9 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 10 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 11 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 12 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 13 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 14 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 15 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 16 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 17 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 18 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 19 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 20 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 21 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 22 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 23 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 24 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 25 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 26 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 27 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 28 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 29 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 30 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 31 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 32 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 33 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 34 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 35 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 36 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 37 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 38 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 39 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 40 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 41 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 42 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 43 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 44 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 45 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 46 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 47 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 48 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 49 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 50 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 51 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 52 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 53 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 54 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 55 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 56 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 57 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 58 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 59 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 60 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 61 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 62 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 65 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 66 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 67 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 68 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 69 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 70 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 71 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 72 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 73 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 74 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 75 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 76 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 77 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 78 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 79 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 80 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 81 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 82 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 83 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 84 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 85 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 86 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 87 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 88 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 89 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 90 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 91 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 92 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 93 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 94 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 95 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 96 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 97 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 98 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 99 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 100 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 101 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 102 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 103 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 104 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 105 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 106 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 107 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 108 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 109 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 110 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 111 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 112 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 113 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 114 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 115 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 116 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 117 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 118 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 119 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 120 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 121 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 122 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 123 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 124 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 125 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 126 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 127 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 128 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 129 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 130 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 131 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 132 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 133 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 134 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 135 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 136 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 137 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 138 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 139 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 140 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 141 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 142 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 143 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 144 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 145 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 146 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 147 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 148 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 149 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 150 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 151 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 152 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 153 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 154 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 155 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 156 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 157 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 158 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 159 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 160 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 161 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 162 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 163 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 164 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 165 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 166 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 167 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 168 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 169 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 170 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 171 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 172 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 173 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 174 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 175 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 176 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 177 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 178 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 179 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 180 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 181 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 182 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 183 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 184 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 185 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 186 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 187 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 188 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 189 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 190 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 191 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 192 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 193 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 194 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 195 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 196 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 197 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 198 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 199 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 200 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 201 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 202 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 203 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 204 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 205 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 206 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 207 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 208 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 209 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 210 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 211 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 212 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 213 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 214 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 215 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 216 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 217 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 218 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 219 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 220 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 221 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 222 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 223 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 224 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 225 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 226 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 227 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 228 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 229 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 230 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 231 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 232 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 233 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 234 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 235 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 236 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 237 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 238 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 239 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 240 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 241 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 242 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 243 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 244 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 245 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 246 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 247 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 248 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 249 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 250 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 251 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 252 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 253 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 254 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 255 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 256 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 257 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 258 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 259 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 260 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 261 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 262 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 263 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 264 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 265 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 266 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 267 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 268 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 269 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 270 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 271 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 272 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 273 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 274 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 275 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 276 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 277 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 278 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 279 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 280 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 281 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 282 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 283 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 284 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 285 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 286 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 287 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 288 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 289 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 290 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 291 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 292 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 293 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 294 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 295 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 296 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 297 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 298 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 299 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 300 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 301 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 302 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 303 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 304 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 305 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 306 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 307 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 308 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 309 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 310 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 311 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 312 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 313 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 314 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 315 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 316 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 317 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 318 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 319 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 320 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 321 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 322 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 323 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 324 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 325 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 326 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 327 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 328 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 329 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 330 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 331 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 332 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 333 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 334 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 335 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 336 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 337 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 338 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 339 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 340 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 341 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 342 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 343 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 344 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 345 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 346 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 347 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 348 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 349 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 350 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 351 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 352 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 353 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 354 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 355 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 356 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 357 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 358 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 359 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 360 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 361 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 362 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 363 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 364 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 365 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 366 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 367 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 368 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 369 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 370 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 371 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 372 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 373 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 374 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 375 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 376 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 377 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 378 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 379 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 380 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 381 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 382 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 383 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 384 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 385 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 386 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 387 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 388 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 389 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 390 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 391 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 392 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 393 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 394 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 395 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 396 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 397 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 398 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 399 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 400 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 401 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 402 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 403 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 404 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 405 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 406 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 407 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 408 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 409 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 410 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 411 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 412 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 413 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 414 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 415 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 416 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 417 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 418 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 419 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 420 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 421 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 422 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 423 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 424 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 425 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 426 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 427 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 428 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 429 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 430 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 431 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 432 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 433 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 434 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 435 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 436 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 437 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 438 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 439 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 440 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 441 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 442 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 443 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 444 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 445 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 446 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 447 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 448 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 449 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 450 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 451 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 452 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 453 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 454 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 455 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 456 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 457 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 458 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 459 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 460 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 461 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 462 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 463 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 464 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 465 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 466 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 467 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 468 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 469 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 470 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 471 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 472 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 473 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 474 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 475 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 476 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 477 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 478 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 479 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 480 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 481 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 482 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 483 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 484 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 485 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 486 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 487 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 488 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 489 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 490 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 491 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 492 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 493 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 494 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 495 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 496 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 497 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 498 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 499 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 500 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 501 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 502 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 503 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 504 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 505 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 506 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 507 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 508 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 509 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 510 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 511 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 512 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 513 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 514 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 515 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 516 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 517 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 518 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 519 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 520 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 521 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 522 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 523 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 524 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 525 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 526 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 527 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 528 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 529 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 530 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 531 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 532 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 533 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 534 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 535 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 536 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 537 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 538 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 539 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 540 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 541 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 542 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 543 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 544 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 545 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 546 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 547 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 548 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 549 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 550 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 551 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 552 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 553 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 554 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 555 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 556 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 557 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 558 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 559 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 560 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 561 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 562 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 563 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 564 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 565 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 566 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 567 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 568 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 569 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 570 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 571 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 572 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 573 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 574 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 575 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 576 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 577 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 578 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 579 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 580 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 581 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 582 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 583 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 584 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
