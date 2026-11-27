# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-27.md)

*最后自动更新时间: 2026-11-27 01:20:45*
## 1. AI 让自托管再次变得有趣。

**原文标题**: AI made self-hosting fun again

**原文链接**: [https://janlukas.blog/posts/ai-self-hosting](https://janlukas.blog/posts/ai-self-hosting)

AI 极大地降低了传统服务器维护和实验中的“摩擦”，重燃了作者对自托管（Self-hosting）的热情。在经历了数年的停滞后，作者发现 AI 编程助手使得管理 Docker Compose 文件和复杂配置变得更加轻松。

文中强调的核心优势包括：

*   **降低技术门槛：** 以前被认为过于耗时或复杂的系统（如 NixOS 和自定义可启动容器镜像）现在变得触手可及。AI 将这些系统的设置时间从几周缩短到了区区几小时。
*   **全面的自动化：** AI 帮助作者实现了完整的 DevOps 流水线。通过整合 Renovate 和 CI/CD 工作流，软件更新和部署现在通过 Git 自动完成，通常只需在手机上进行简单的审核即可执行。
*   **定制化工具：** 与其寻找可能并不完全匹配需求的开源软件，作者现在利用 AI 使用 Go 语言构建满足特定需求的定制工具，例如自动发票下载器。
*   **硬件复兴：** 活跃度的提升促使作者回归更强大的家用硬件，从瘦客户端重新转向升级后的个人服务器，以承载更多服务。

作者承认了使用由科技巨头主导的 AI 技术来获得独立性这一事实存在的讽刺。虽然作者告诫要警惕 AI 产生的技术债以及过度构建的诱惑，但最后总结道，AI 的核心价值在于消除了繁琐的杂务。通过自动化日常维护并缩短从创意到实现的路径，自托管再次成为了一个充满乐趣和创造力的爱好。

---

## 2. 卡米尔·汗·蒙塔兹：享誉国内但在国外鲜为人知的巴基斯坦建筑师

**原文标题**: Kamil Khan Mumtaz: Pakistani architect, admired at home, almost invisible abroad

**原文链接**: [https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/](https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/)

卡米尔·汗·穆塔兹（Kamil Khan Mumtaz）是一位卓越的巴基斯坦建筑师，他的职业生涯代表了从西方现代主义向本土传统复兴的深刻转变。20世纪60年代，穆塔兹在伦敦建筑联盟学院（Architectural Association）接受教育，起初他信奉“标准现代主义方法”，并在回到巴基斯坦后成为一名共产主义活动家。然而，到了70年代末，他开始感到一种“挥之不去的忧虑”，担心自己的现代主义设计无法与当地民众沟通。

1980年，在接触到波斯建筑的苏菲派传统后，他迎来了人生的关键转折点。这一发现促使他放弃了马克思主义和唯物主义的世界观，转而信奉精神与传统主义哲学。自此，穆塔兹致力于复兴南亚的建筑语言，尤其是他家乡拉合尔的建筑传统。

穆塔兹作品的一个鲜明标志是他与世袭工匠的合作。通过寻找这些工匠家族的“传人”，他重新发掘了许多“失传”的技艺，如特殊的砖石工艺、穆卡纳斯（蜂窝状拱顶）和扁平穹顶——其中一些技艺已中断了300年之久。他的设计作品十分多样，涵盖了卡拉奇的牛津大学出版社办公楼、帕克维加清真寺，以及拥有精致庭院、手工石刻和大理石“手帕穹顶”的低成本学校与私人住宅。

除了设计工作，穆塔兹在保护拉合尔历史悠久的古城（Walled City）免受现代化冲击方面也起到了关键作用，并助力其获得联合国教科文组织世界遗产认定。如今，年逾八旬的他依然是一位举足轻重的人物，他通过证明传统工艺和本土材料仍能满足现代需求，为全球化城市环境提供了一种当代的替代选择。尽管他在国际媒体上的声名并不显赫，但他的作品见证了巴基斯坦文化认同的持久生命力。

---

## 3. AMD 专用的 llama.cpp 分支

**原文标题**: AMD-specific fork of llama.cpp

**原文链接**: [https://devnull.land/amd-specific-llama-cpp](https://devnull.land/amd-specific-llama-cpp)

这篇文章站在 2026 年 11 月的角度，讨论了旨在超越 `llama.cpp` 和 `vLLM` 等通用工具的专业化 LLM 推理引擎的激增。虽然许多像 *Strata* 这样新兴的“定制化”引擎通过“氛围编码”（vibe-coding）和存疑的捷径（例如不顾模型逻辑而优先考虑驻留显存的专家模型）实现了极高的速度，但作者推荐了一个更符合原则的替代方案：**llama-cpp-rdna-boosts**。

**llama-cpp-rdna-boosts** 是一套应用于稳定版 `llama.cpp` 代码库的极简、AMD 专用补丁。作者青睐这种方法，因为它在显著优化 RDNA 硬件性能的同时，保持了原始项目的可靠性。主要亮点包括：

*   **性能提升**：在 AMD R9700 eGPU 配置下，预填充（prefill）速度从 **700 t/s 提升至 1300 t/s**，Token 生成速度从 **35 t/s 提升至 55 t/s**。
*   **理念**：与“过度构建”的 *vllm-radiance* 或不透明的 *Strata* 不同，该项目精简且透明，专注于硬件层面的特定优化，而非改变模型行为。
*   **易用性**：该引擎可通过集成了 ROCm 库的预构建 Podman 镜像轻松部署，绕过了繁琐的手动构建步骤。

作者总结道，对于 AMD 用户而言，与其他新兴推理引擎相比，这个分支版本在速度和软件完整性之间取得了更优的平衡。

---

## 4. YouTube 广告惩罚者 – 播放广告时自动重新加载 YouTube 页面

**原文标题**: YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays

**原文链接**: [https://github.com/antonpictures/youtube-punisher](https://github.com/antonpictures/youtube-punisher)

**YouTube Ad Punisher** 是一款浏览器扩展，旨在通过一种新颖的策略绕过 YouTube 的反广告拦截系统：自动刷新页面。与 YouTube 目前能够检测到的过滤网络请求的传统拦截器不同，该工具会识别广告播放的时机，记录视频的确切播放时间点，并重新加载页面。

由于 YouTube 在每次页面加载时都会重新评估广告投放，通常 1-2 次重载即可产生空白广告位，从而让视频能够无干扰地播放。该扩展通过 `&t=Xs` URL 参数和 JavaScript 进度定位来保留用户的播放位置，确保衔接无缝。

**核心技术策略：**
*   **首选重载：** 通过 `.ad-showing` 类检测广告，并重新加载页面 1-3 次以清除广告位。
*   **后备重定向：** 如果重载三次后仍然失败，它将重定向到无广告镜像网站（`yout-ube.com`）。
*   **标签页节流：** 它会自动切换“辅助标签页”以让广告状态沉淀，这是一种绕过持续广告投放的技术。

**功能与理念：**
该扩展包含一个本地**广告历史数据库**，记录了所遇到的每个广告的详细元数据，包括广告商名称、广告时长和跳过文本。这些数据可以导出为 JSON 或 CSV 格式。开发者 George Anton 将该工具描述为一种“被动抗议”。通过在消除广告展示的同时增加服务器请求（页面加载），该工具旨在破坏侵入性广告的经济模型。

该扩展目前已针对 Chrome 系浏览器（加载已解压的扩展程序）进行了优化，并为 Safari 提供了实验性的 AppleScript 变通方案。它旨在与 uBlock Origin 和 SponsorBlock 协同工作，为希望“惩罚”广告且不被 YouTube 检测脚本拦截的用户提供全面的解决方案。

---

## 5. “RansomwareHelp”首席技术官因电信诈骗被起诉

**原文标题**: CTO of 'RansomwareHelp' indicted for wire fraud

**原文链接**: [https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/)

佛罗里达州公司 RansomwareHelp 的首席技术官兼联合创始人胡安·里卡多·帕拉西奥·埃斯科瓦尔（Juan Ricardo Palacio Escobar）在联邦调查局（FBI）的一次钓鱼执法行动后，因电信欺诈被起诉。尽管该公司公开声称利用“先进的加密工具”和专有算法在不支付赎金的情况下恢复数据，但联邦调查人员发现，该公司实际上是在秘密向攻击者购买解密密钥，并对从未实际提供的服务向受害者收取巨额加价。

在 FBI 的钓鱼行动中，特工分别伪装成勒索软件受害者和虚构的勒索软件组织。帕拉西奥与该“组织”协商出了较低的价格（6,000 美元），同时向“受害者”开出了超过 16,000 美元的账单，并谎称该费用涵盖了“诊断评估”。为了维持骗局，该公司使用远程访问软件删除了受害者网络中的勒索信，以防止客户直接联系攻击者或发现受骗真相。

安全专家强调，该公司所谓的使用 510 台“取证服务器”暴力破解加密等技术声明完全是“荒诞的”，旨在剥削那些处境绝望且不懂技术的小企业主。在另一起案例中，RansomwareHelp 试图向一家会计师事务所收取近 43.9 万美元的恢复费用，而实际工作仅涉及与 Lockbit 勒索软件组织的简单谈判。

此案是美国司法部严厉打击欺诈性网络安全公司行动的一部分。近期，针对 MonsterCloud 和 Cybersteward 高管，以及被发现与 BlackCat 等勒索软件组织勾结的个人谈判者的起诉相继展开。这些案例凸显了掠夺型公司日益增多的趋势，它们通过虚报恢复手段或与宣称要对抗的威胁者暗中勾结来诈骗受害者。

---

## 6. Rvoip：基于 Rust 的 VoIP 协议栈

**原文标题**: Rvoip: VoIP stack in Rust

**原文链接**: [https://github.com/eisenzopf/rvoip](https://github.com/eisenzopf/rvoip)

**Rvoip** is a high-performance, all-in-one Rust library designed for building communication applications without the need for external SIP servers, media engines, or RTP proxies. It integrates signaling, media, codecs, and NAT traversal directly into the application stack, supporting SIP, RTP, WebRTC, and Media over QUIC.

**Key Features and Performance:**
*   **Performance:** In RFC 7501/7502 benchmarks, a single process on an AWS c8i.4xlarge instance achieved over 8,200 calls per second (CPS) for signaling and approximately 1,200 CPS for full UDP/RTP media sessions.
*   **Modular Architecture:** The workspace consists of 47 crates. Developers typically interface with `rvoip-sip` for telephony or the `rvoip` facade for advanced features like WebRTC and AI gateways.
*   **Unified Model:** An "Orchestrator" manages a shared conversation model, treating different transport legs (SIP, WebRTC, or QUIC) as uniform objects. This allows for seamless bridging between diverse communication protocols.

**Functional Paths:**
1.  **SIP Telephony:** Provides APIs for softphones, registrars, and B2BUAs. It is "Beta-qualified" and verified for interoperability with major platforms like Asterisk and FreeSWITCH.
2.  **Gateways:** Enables browser-to-SIP routing via WebRTC and UCTP substrates.
3.  **Voice AI:** Supports hosted AI agents (via Vapi) and custom pipelines (ASR/TTS) with support for signed vCon conversation records.

**Maturity:**
The core SIP and media components are Beta-qualified, offering stable performance and security evidence. Advanced features, including WebRTC, Media over QUIC, and specific AI integrations, are currently in Developer Preview. Overall, Rvoip provides a modern, memory-safe alternative for building scalable PBXs, IVRs, and AI-driven voice agents.

---

## 7. Novita、StreamLake 等都是字节跳动方舟的套壳。

**原文标题**: Novita, StreamLake, etc. are ByteDance Ark wrappers

**原文链接**: [https://kendell.dev/blog/arkwrapper/](https://kendell.dev/blog/arkwrapper/)

这份调查报告揭示，Novita、StreamLake（快手）和蚂蚁数科（Ant Digital）等几家知名的 AI 推理供应商正充当“套壳”角色，将用户流量转发至字节跳动的方舟平台（国内为火山引擎，国际为 BytePlus），而非独立托管模型。

**流量转发至字节跳动的关键证据：**
*   **技术指纹：** Novita 和 StreamLake 产生的请求 ID 和工具调用格式与字节跳动特有的十六进制结构相匹配。此外，提供给这些服务的图像数据经常从字节跳动位于北京和新加坡的 IP 地址下载。
*   **审查一致性：** 当涉及政治敏感话题（如“坦克人”）时，这些供应商返回的拒绝话术与字节跳动审核系统使用的预设话术完全一致。
*   **定价对齐：** 研究发现蚂蚁数科的费率与 BytePlus 的“经济型”档位定价完全吻合。

**隐私与透明度担忧：**
报告强调了这些供应商在“零数据保留”（ZDR）承诺上存在的严重诚信违约。针对 MiniMax 模型的调查证明，Novita 和 StreamLake 等供应商将“ZDR”请求转发给了第三方，而第三方的自动化安全系统访问了用户提示词中的私有 URL。因此，OpenRouter 撤销了这些供应商的多项 ZDR 标签，Novita 也从其服务中移除了 16 个模型端点。

**经济动机：**
这种行为的主要驱动力是成本。BytePlus 和腾讯等大型云供应商提供 30% 至 60% 的大额折扣，这使得“中间商”供应商可以通过转售访问权限获利，同时掩盖了跨越美国、新加坡和中国等多个司法管辖区的复杂子处理商链。报告总结称，表面上看起来多元的独立托管市场，实际上是一个流量最终流向中国主要云基础设施的整合网络。

---

## 8. Intel One Mono font (2023)

**原文标题**: Intel One Mono font (2023)

**原文链接**: [https://github.com/intel/intel-one-mono](https://github.com/intel/intel-one-mono)

Intel One Mono 是一款免费、开源的等宽字体，专门为提升开发者的可读性而设计。该字体由 Frere-Jones Type 与英特尔及 VMLY&R 合作开发，并在设计过程中直接采纳了低视力和法律盲开发者的反馈，旨在减轻眼部疲劳、减少劳累并降低编码错误。

该字体家族包含四种字重——Light、Regular、Medium 和 Bold——并配有相应的斜体。它支持 200 多种拉丁语系语言，提供多种格式，包括 .otf、.ttf 以及针对网页优化的 .woff 文件。为了获得最佳清晰度，设计师建议在屏幕上使用 9px 或更大的字号。官方版本还包含手动“微调”（hinting），以确保在 Windows 平台上实现锐利的渲染效果。

Intel One Mono 的一大亮点是支持专为编程定制的 OpenType 特性。开发者可以启用编程连字（ligatures）和样式集（ss01–ss03）来使用数学简写和箭头符号。其他特性还包括备选的数字“3”（ss04）以及能与数学运算符上下文对齐的“悬浮冒号”（ss11–ss12）。文中还为 VSCode、Sublime Text 和 IntelliJ 等主流编辑器提供了具体的启用说明。

除了即装即用的字体文件，英特尔还向社区开放了可编辑的 UFO 源文件和“母版”（masters）。这些资源允许用户使用 RoboFont 等字体编辑器进行深度定制。虽然官方构建版本已针对屏幕显示进行了手动优化，但该项目的开源特性允许用户提出修改建议，或根据特定需求重新构建整个字体家族。

---

## 9. Show HN: Olumino, a Markdown notes and spaced repetition app

**原文标题**: Show HN: Olumino, a Markdown notes and spaced repetition app

**原文链接**: [https://olumino.app](https://olumino.app)

生成摘要出错

---

## 10. Largest 2D Chart library in the world using BUI: BlenderUI

**原文标题**: Largest 2D Chart library in the world using BUI: BlenderUI

**原文链接**: [https://bui.preetham.top/charts/](https://bui.preetham.top/charts/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-27](output/hacker_news_summary_2026-11-27.md) |
| 2 | [2026-11-24](output/hacker_news_summary_2026-11-24.md) |
| 3 | [2026-11-22](output/hacker_news_summary_2026-11-22.md) |
| 4 | [2026-11-25](output/hacker_news_summary_2026-11-25.md) |
| 5 | [2026-11-26](output/hacker_news_summary_2026-11-26.md) |
| 6 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 7 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 8 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 9 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 10 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 11 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 12 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 13 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 14 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 15 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 16 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 17 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 18 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 19 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 20 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 21 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 22 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 23 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 24 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 25 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 26 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 27 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 28 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 29 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 30 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 31 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 32 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 33 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 34 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 35 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 36 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 37 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 38 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 39 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 40 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 41 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 42 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 43 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 44 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 45 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 46 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 47 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 48 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 49 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 50 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 51 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 52 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 53 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 54 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 55 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 56 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 57 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 58 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 59 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 60 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 61 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 62 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 63 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 64 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 65 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 66 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 67 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 68 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 69 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 70 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 71 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 72 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 73 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 74 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 75 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 76 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 77 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 78 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 79 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 80 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 81 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 82 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 83 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 84 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 85 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 86 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 87 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 88 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 89 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 90 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 91 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 92 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 93 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 94 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 95 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 96 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 97 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 98 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 99 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 100 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 101 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 102 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 103 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 104 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 105 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 106 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 107 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 108 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 109 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 110 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 111 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 112 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 113 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 114 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 115 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 116 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 117 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 118 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 119 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 120 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 121 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 122 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 123 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 124 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 125 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 126 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 127 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 128 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 129 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 130 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 131 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 132 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 133 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 134 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 135 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 136 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 137 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 138 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 139 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 140 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 141 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 142 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 143 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 144 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 145 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 146 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 147 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 148 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 149 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 150 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 151 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 152 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 153 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 154 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 155 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 156 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 157 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 158 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 159 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 160 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 161 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 162 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 163 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 164 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 165 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 166 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 167 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 168 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 169 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 170 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 171 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 172 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 173 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 174 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 175 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 176 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 177 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 178 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 179 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 180 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 181 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 182 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 183 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 184 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 185 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 186 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 187 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 188 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 189 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 190 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 191 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 192 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 193 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 194 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 195 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 196 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 197 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 198 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 199 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 200 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 201 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 202 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 203 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 204 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 205 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 206 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 207 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 208 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 209 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 210 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 211 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 212 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 213 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 214 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 215 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 216 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 217 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 218 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 219 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 220 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 221 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 222 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 223 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 224 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 225 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 226 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 227 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 228 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 229 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 230 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 231 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 232 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 233 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 234 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 235 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 236 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 237 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 238 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 239 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 240 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 241 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 242 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 243 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 244 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 245 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 246 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 247 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 248 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 249 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 250 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 251 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 252 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 253 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 254 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 255 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 256 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 257 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 258 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 259 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 260 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 261 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 262 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 263 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 264 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 265 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 266 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 267 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 268 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 269 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 270 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 271 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 272 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 273 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 274 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 275 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 276 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 277 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 278 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 279 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 280 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 281 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 282 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 283 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 284 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 285 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 286 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 287 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 288 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 289 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 290 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 291 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 292 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 293 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 294 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 295 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 296 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 297 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 298 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 299 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 300 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 301 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 302 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 303 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 304 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 305 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 306 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 307 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 308 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 309 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 310 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 311 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 312 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 313 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 314 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 315 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 316 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 317 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 318 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 319 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 320 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 321 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 322 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 323 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 324 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 325 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 326 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 327 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 328 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 329 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 330 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 331 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 332 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 333 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 334 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 335 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 336 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 337 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 338 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 339 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 340 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 341 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 342 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 343 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 344 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 345 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 346 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 347 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 348 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 349 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 350 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 351 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 352 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 353 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 354 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 355 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 356 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 357 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 358 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 359 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 360 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 361 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 362 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 363 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 364 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 365 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 366 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 367 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 368 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 369 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 370 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 371 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 372 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 373 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 374 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 375 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 376 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 377 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 378 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 379 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 380 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 381 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 382 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 383 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 384 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 385 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 386 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 387 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 388 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 389 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 390 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 391 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 392 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 393 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 394 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 395 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 396 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 397 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 398 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 399 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 400 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 401 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 402 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 403 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 404 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 405 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 406 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 407 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 408 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 409 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 410 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 411 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 412 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 413 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 414 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 415 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 416 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 417 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 418 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 419 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 420 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 421 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 422 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 423 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 424 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 425 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 426 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 427 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 428 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 429 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 430 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 431 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 432 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 433 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 434 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 435 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 436 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 437 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 438 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 439 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 440 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 441 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 442 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 443 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 444 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 445 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 446 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 447 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 448 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 449 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 450 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 451 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 452 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 453 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 454 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 455 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 456 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 457 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 458 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 459 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 460 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 461 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 462 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 463 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 464 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 465 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 466 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 467 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 468 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 469 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 470 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 471 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 472 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 473 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 474 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 475 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 476 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 477 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 478 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 479 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 480 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 481 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 482 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 483 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 484 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 485 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 486 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 487 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 488 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 489 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 490 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 491 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 492 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 493 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 494 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 495 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 496 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 497 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 498 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 499 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 500 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 501 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 502 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 503 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 504 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 505 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 506 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 507 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 508 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 509 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 510 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 511 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 512 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 513 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 514 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 515 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 516 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 517 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 518 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 519 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 520 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 521 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 522 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 523 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 524 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 525 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 526 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 527 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 528 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 529 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 530 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 531 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 532 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 533 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 534 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 535 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 536 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 537 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 538 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 539 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 540 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 541 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 542 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 543 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 544 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 545 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 546 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 547 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 548 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 549 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 550 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 551 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 552 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 553 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 554 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 555 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 556 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 557 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 558 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 559 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 560 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 561 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 562 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 563 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 564 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 565 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 566 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 567 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 568 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 569 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 570 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 571 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 572 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 573 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 574 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 575 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 576 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 577 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 578 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 579 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 580 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 581 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 582 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 583 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 584 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 585 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 586 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 587 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 588 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 589 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 590 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 591 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 592 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 593 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 594 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 595 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 596 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 597 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 598 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 599 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 600 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 601 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 602 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 603 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 604 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 605 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 606 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 607 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 608 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 609 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 610 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 611 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
