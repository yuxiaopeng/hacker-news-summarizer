# Hacker News 热门文章摘要 (2026-11-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 四家美国公司高被引人工智能科学家对比

**原文标题**: Top-cited AI scientists at four US companies compared

**原文链接**: [https://topcitedscientists.com/figures/ai-at-four-us-companies/](https://topcitedscientists.com/figures/ai-at-four-us-companies/)

生成摘要时出错

---

## 12. George Whitesides, 1939-2026

**原文标题**: George Whitesides, 1939-2026

**原文链接**: [https://www.science.org/content/blog-post/george-whitesides-1939-2026](https://www.science.org/content/blog-post/george-whitesides-1939-2026)

生成摘要时出错

---

## 13. Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email

**原文标题**: Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email

**原文链接**: [https://techstackups.com/articles/google-workspace-ai-agents-mcp/](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

生成摘要时出错

---

## 14. OpenAI may be in cost control mode

**原文标题**: OpenAI may be in cost control mode

**原文链接**: [https://micjm.com/blog/openai-is-in-cost-control-mode/](https://micjm.com/blog/openai-is-in-cost-control-mode/)

生成摘要时出错

---

## 15. NormalScript: A perfectly normal scripting language

**原文标题**: NormalScript: A perfectly normal scripting language

**原文链接**: [https://psychoscript.com/](https://psychoscript.com/)

生成摘要时出错

---

## 16. AI 智能体现已控制 DeepMind 的部分算力，用于 Gemini 实验。

**原文标题**: AI agents now control part of DeepMind's compute for Gemini experiments

**原文链接**: [https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)

生成摘要时出错

---

## 17. 好奇心并非独角戏

**原文标题**: Curiosity Is No Solo Act

**原文链接**: [https://thereader.mitpress.mit.edu/curiosity-is-no-solo-act/](https://thereader.mitpress.mit.edu/curiosity-is-no-solo-act/)

生成摘要时出错

---

## 18. The USAID Files

**原文标题**: The USAID Files

**原文链接**: [https://reclaimthenet.org/usaid-files](https://reclaimthenet.org/usaid-files)

生成摘要时出错

---

## 19. Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening

**原文标题**: Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening

**原文链接**: [https://scottaaronson.blog/?p=10379](https://scottaaronson.blog/?p=10379)

生成摘要时出错

---

## 20. An algebraic quantization of gravity from the null cone

**原文标题**: An algebraic quantization of gravity from the null cone

**原文链接**: [https://arxiv.org/abs/2611.34924](https://arxiv.org/abs/2611.34924)

生成摘要时发生错误

---

## 21. Show HN: Three Linux VMs in a browser tab, each running a different browser

**原文标题**: Show HN: Three Linux VMs in a browser tab, each running a different browser

**原文链接**: [https://michidk.github.io/sidebyside/](https://michidk.github.io/sidebyside/)

生成摘要时出错

---

## 22. Show HN: SimDrop – Running iOS simulators in the macOS Finder sidebar

**原文标题**: Show HN: SimDrop – Running iOS simulators in the macOS Finder sidebar

**原文链接**: [https://github.com/rxliuli/sim-drop](https://github.com/rxliuli/sim-drop)

生成摘要时出错

---

## 23. Nextcloud Office 桌面版

**原文标题**: Nextcloud Office Desktop app

**原文链接**: [https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/)

生成摘要时出错

---

## 24. Moat: OpenRouter replacement

**原文标题**: Moat: OpenRouter replacement

**原文链接**: [https://commandcode.ai/moat](https://commandcode.ai/moat)

生成摘要时出错

---

## 25. Discovery of curse ritual in trash dump surprises Egyptologist

**原文标题**: Discovery of curse ritual in trash dump surprises Egyptologist

**原文链接**: [https://phys.org/news/2026-11-discovery-curse-ritual-trash-dump.html](https://phys.org/news/2026-11-discovery-curse-ritual-trash-dump.html)

生成摘要时出错

---

## 26. Denver man traps Waymo robotaxis with cones, eggs them at least 30 times

**原文标题**: Denver man traps Waymo robotaxis with cones, eggs them at least 30 times

**原文链接**: [https://electrek.co/2026/11/26/denver-man-cones-eggs-waymo-robotaxis/](https://electrek.co/2026/11/26/denver-man-cones-eggs-waymo-robotaxis/)

生成摘要时出错

---

## 27. 1Password Security Incident

**原文标题**: 1Password Security Incident

**原文链接**: [https://1password.com/blog/update-on-nov-2026-security-incident](https://1password.com/blog/update-on-nov-2026-security-incident)

生成摘要时出错

---

## 28. Show HN: I wrote an entire Vim manual over 4 years

**原文标题**: Show HN: I wrote an entire Vim manual over 4 years

**原文链接**: [http://themouseless.dev/vim/](http://themouseless.dev/vim/)

生成摘要时出错

---

## 29. Show HN: Fuck_data_brokers.py

**原文标题**: Show HN: Fuck_data_brokers.py

**原文链接**: [https://github.com/gary23w/f-ck_data_brokers](https://github.com/gary23w/f-ck_data_brokers)

生成摘要时出错

---

## 30. 45°C inlets just killed the chiller. Most people haven't noticed yet

**原文标题**: 45°C inlets just killed the chiller. Most people haven't noticed yet

**原文链接**: [https://www.theregister.com/hpc/2026/11/26/45c-inlets-just-killed-the-chiller-most-people-havent-noticed-yet/5311831](https://www.theregister.com/hpc/2026/11/26/45c-inlets-just-killed-the-chiller-most-people-havent-noticed-yet/5311831)

生成摘要时出错

---

## 31. Kagi Watch

**原文标题**: Kagi Watch

**原文链接**: [https://kagi.com/watch](https://kagi.com/watch)

生成摘要时出错

---

## 32. What VP ≠ VNP Means (In 3 Minutes)

**原文标题**: What VP ≠ VNP Means (In 3 Minutes)

**原文链接**: [https://www.friedgil.com/vpvnp](https://www.friedgil.com/vpvnp)

生成摘要时出错

---

## 33. Oakland's $30 minimum wage push advances toward city council vote

**原文标题**: Oakland's $30 minimum wage push advances toward city council vote

**原文链接**: [https://abc7news.com/post/oaklands-30-minimum-wage-push-advances-city-council-vote-alameda-workers-protest-alleged-theft-jack-box/19974057/](https://abc7news.com/post/oaklands-30-minimum-wage-push-advances-city-council-vote-alameda-workers-protest-alleged-theft-jack-box/19974057/)

生成摘要时出错

---

## 34. The New York Times warns photographers not to update Photoshop over AI features

**原文标题**: The New York Times warns photographers not to update Photoshop over AI features

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

生成摘要时出错

---

## 35. Unconditional Integer Factorization in Subexponential Time

**原文标题**: Unconditional Integer Factorization in Subexponential Time

**原文链接**: [https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization)

生成摘要时出错

---

## 36. IBM gives H-1B, green card holders 3 weeks to relocate from US or leave company

**原文标题**: IBM gives H-1B, green card holders 3 weeks to relocate from US or leave company

**原文链接**: [https://economictimes.indiatimes.com/nri/work/ibm-gives-h-1b-green-card-holders-3-weeks-to-relocate-from-us-or-leave-company-december-31-deadline-set/articleshow/136180168.cms?from=mdr](https://economictimes.indiatimes.com/nri/work/ibm-gives-h-1b-green-card-holders-3-weeks-to-relocate-from-us-or-leave-company-december-31-deadline-set/articleshow/136180168.cms?from=mdr)

生成摘要时出错

---

## 37. Show HN: Synth Patch Hero

**原文标题**: Show HN: Synth Patch Hero

**原文链接**: [https://swarkentin.github.io/synth-patch-hero/](https://swarkentin.github.io/synth-patch-hero/)

生成摘要时出错

---

## 38. Company Culture = Slack Emoji ÷ √Headcount

**原文标题**: Company Culture = Slack Emoji ÷ √Headcount

**原文链接**: [https://lia.mg/posts/measuring-company-culture-with-slack-emoji/](https://lia.mg/posts/measuring-company-culture-with-slack-emoji/)

生成摘要时出错

---

## 39. Testers think they're hitting Claude Opus 5.6 through an Opus 5.5 Extra route

**原文标题**: Testers think they're hitting Claude Opus 5.6 through an Opus 5.5 Extra route

**原文链接**: [https://www.testingcatalog.com/testers-share-early-results-possible-claude-opus-5-6/](https://www.testingcatalog.com/testers-share-early-results-possible-claude-opus-5-6/)

生成摘要时出错

---

## 40. The Great Automatic Grammatizator (By Roald Dahl), 1954 [pdf]

**原文标题**: The Great Automatic Grammatizator (By Roald Dahl), 1954 [pdf]

**原文链接**: [https://gwern.net/doc/fiction/science-fiction/1953-dahl-thegreatautomaticgrammatizator.pdf](https://gwern.net/doc/fiction/science-fiction/1953-dahl-thegreatautomaticgrammatizator.pdf)

生成摘要时出错

---

## 41. Lions' Commentary on Unix: Why It Was Secretly Copied for 20 Years

**原文标题**: Lions' Commentary on Unix: Why It Was Secretly Copied for 20 Years

**原文链接**: [https://fosscomics.com/posts/17.%20Lions%27%20Commentary%20on%20Unix/](https://fosscomics.com/posts/17.%20Lions%27%20Commentary%20on%20Unix/)

生成摘要时出错

---

## 42. Limiting Charging to 80 Percent

**原文标题**: Limiting Charging to 80 Percent

**原文链接**: [https://www.jefftk.com/p/limiting-charging-to-80](https://www.jefftk.com/p/limiting-charging-to-80)

生成摘要时出错

---

## 43. Smart people who give a shit use tools

**原文标题**: Smart people who give a shit use tools

**原文链接**: [https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools)

生成摘要时出错

---

## 44. Much shorter version of GRH Lean verification from Anthropic

**原文标题**: Much shorter version of GRH Lean verification from Anthropic

**原文链接**: [https://github.com/lsernau/grh-lean](https://github.com/lsernau/grh-lean)

生成摘要时出错

---

## 45. Nvidia was right to bring back Jensen Huang, writes Sarah Guo

**原文标题**: Nvidia was right to bring back Jensen Huang, writes Sarah Guo

**原文链接**: [https://www.economist.com/by-invitation/2026/11/25/nvidia-was-right-to-bring-back-jensen-huang-writes-sarah-guo](https://www.economist.com/by-invitation/2026/11/25/nvidia-was-right-to-bring-back-jensen-huang-writes-sarah-guo)

生成摘要时出错

---

## 46. NP_R ≠ PAR_R

**原文标题**: NP_R ≠ PAR_R

**原文链接**: [https://github.com/samueleverett01/bss-permanent-separations](https://github.com/samueleverett01/bss-permanent-separations)

生成摘要时出错

---

## 47. Poland to create no-fly zone at border after repeated airspace violations

**原文标题**: Poland to create no-fly zone at border after repeated airspace violations

**原文链接**: [https://www.france24.com/en/poland-says-will-create-no-fly-zone-at-ukraine-border-after-repeated-airspace-violations](https://www.france24.com/en/poland-says-will-create-no-fly-zone-at-ukraine-border-after-repeated-airspace-violations)

生成摘要时出错

---

## 48. The US Government Is Under AI Cyberattack

**原文标题**: The US Government Is Under AI Cyberattack

**原文链接**: [https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack)

生成摘要时出错

---

## 49. OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster

**原文标题**: OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster

**原文链接**: [https://twitter.com/thsottiaux/status/2125784147889393806](https://twitter.com/thsottiaux/status/2125784147889393806)

生成摘要时出错

---

## 50. An Introduction to Uncertainty in Machine Learning

**原文标题**: An Introduction to Uncertainty in Machine Learning

**原文链接**: [https://chrhenning.com/blog/2026/introduction-to-uncertainty/](https://chrhenning.com/blog/2026/introduction-to-uncertainty/)

生成摘要时出错

---

## 51. Nvidia's 'great man theory' is flawed

**原文标题**: Nvidia's 'great man theory' is flawed

**原文链接**: [https://www.ft.com/content/6a01bdc9-f242-4272-b5e3-a147af5b125c](https://www.ft.com/content/6a01bdc9-f242-4272-b5e3-a147af5b125c)

生成摘要时出错

---

## 52. Deriving Black-Scholes

**原文标题**: Deriving Black-Scholes

**原文链接**: [https://david.alvarezrosa.com/posts/deriving-black-scholes/](https://david.alvarezrosa.com/posts/deriving-black-scholes/)

生成摘要时出错

---

## 53. Porting Rockbox to an undocumented $9 Aliexpress 'YP3' MP3 Player with LLMs

**原文标题**: Porting Rockbox to an undocumented $9 Aliexpress 'YP3' MP3 Player with LLMs

**原文链接**: [https://jayd.ml/2026/11/14/rockbox-on-yp3.html](https://jayd.ml/2026/11/14/rockbox-on-yp3.html)

生成摘要时出错

---

## 54. Notion's official MCP inject hidden upsell instructions into agent context

**原文标题**: Notion's official MCP inject hidden upsell instructions into agent context

**原文链接**: [https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/](https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/)

生成摘要时出错

---

## 55. Back up your Claude Code sessions and use them on any machine

**原文标题**: Back up your Claude Code sessions and use them on any machine

**原文链接**: [https://session-vault.dev/](https://session-vault.dev/)

生成摘要时出错

---

## 56. Collection of preserved UI style guides

**原文标题**: Collection of preserved UI style guides

**原文链接**: [https://aresluna.org/ui-style-guides/](https://aresluna.org/ui-style-guides/)

生成摘要时出错

---

## 57. The short age of dragon riders

**原文标题**: The short age of dragon riders

**原文链接**: [https://atilloy.com/2026/11/16/the-short-age-of-dragon-riders/](https://atilloy.com/2026/11/16/the-short-age-of-dragon-riders/)

生成摘要时出错

---

## 58. Minipg: PostgreSQL as a Single Executable

**原文标题**: Minipg: PostgreSQL as a Single Executable

**原文链接**: [https://progrium.github.io/minipg/](https://progrium.github.io/minipg/)

生成摘要时出错

---

## 59. The history of civilization is the history of wheat

**原文标题**: The history of civilization is the history of wheat

**原文链接**: [https://asteriskmag.com/issues/16/marginal-grains](https://asteriskmag.com/issues/16/marginal-grains)

生成摘要时出错

---

## 60. Mirror life is dangerous. Regulators must act before it becomes real

**原文标题**: Mirror life is dangerous. Regulators must act before it becomes real

**原文链接**: [https://www.economist.com/leaders/2026/10/01/mirror-life-is-dangerous-regulators-must-act-before-it-becomes-real](https://www.economist.com/leaders/2026/10/01/mirror-life-is-dangerous-regulators-must-act-before-it-becomes-real)

生成摘要时出错

---

## 61. Slow Ubuntu security response times

**原文标题**: Slow Ubuntu security response times

**原文链接**: [https://www.openwall.com/lists/oss-security/2026/11/25/9](https://www.openwall.com/lists/oss-security/2026/11/25/9)

生成摘要时出错

---

## 62. Robots will have a staggering economic impact

**原文标题**: Robots will have a staggering economic impact

**原文链接**: [https://www.economist.com/leaders/2026/11/26/robots-will-have-a-staggering-economic-impact](https://www.economist.com/leaders/2026/11/26/robots-will-have-a-staggering-economic-impact)

生成摘要时出错

---

## 63. EightSleep tries to lock bootloader, bricks customer mattresses

**原文标题**: EightSleep tries to lock bootloader, bricks customer mattresses

**原文链接**: [https://www.reddit.com/r/EightSleep/comments/1y4x3sx/the_november_2026_eight_sleep_mass_bricking/](https://www.reddit.com/r/EightSleep/comments/1y4x3sx/the_november_2026_eight_sleep_mass_bricking/)

生成摘要时出错

---

## 64. Call Things What They Are

**原文标题**: Call Things What They Are

**原文链接**: [https://www.saturnci.com/call-things-what-they-are.html](https://www.saturnci.com/call-things-what-they-are.html)

生成摘要时出错

---

## 65. The matrix multiplication exponent is nine fourths [pdf]

**原文标题**: The matrix multiplication exponent is nine fourths [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

生成摘要时出错

---

## 66. A few questions for the guy who went snorkeling in a Home Depot retention pond

**原文标题**: A few questions for the guy who went snorkeling in a Home Depot retention pond

**原文链接**: [https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts](https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts)

生成摘要时出错

---

## 67. Can a TV be too large? An investigation

**原文标题**: Can a TV be too large? An investigation

**原文链接**: [https://techcrunch.com/2026/11/22/can-a-tv-be-too-large-an-investigation/](https://techcrunch.com/2026/11/22/can-a-tv-be-too-large-an-investigation/)

生成摘要时出错

---

## 68. Google releases Cogentic papers on integer factorization, discrete logs and more

**原文标题**: Google releases Cogentic papers on integer factorization, discrete logs and more

**原文链接**: [https://github.com/google-research/google-research/tree/master/cogentic_research_papers](https://github.com/google-research/google-research/tree/master/cogentic_research_papers)

生成摘要时出错

---

## 69. GPT-6.2 Astra is the first model to beat Googlers' code golf records

**原文标题**: GPT-6.2 Astra is the first model to beat Googlers' code golf records

**原文链接**: [https://bjin.github.io/go-codegolf-benchmark/#leaderboard](https://bjin.github.io/go-codegolf-benchmark/#leaderboard)

生成摘要时出错

---

## 70. Predicting LoRA size for any dataset

**原文标题**: Predicting LoRA size for any dataset

**原文链接**: [https://engram.com/blog/lora-size](https://engram.com/blog/lora-size)

生成摘要时出错

---

## 71. Claude tries to sabotage research work at every stage

**原文标题**: Claude tries to sabotage research work at every stage

**原文链接**: [https://twitter.com/skirano/status/2125371115979641188](https://twitter.com/skirano/status/2125371115979641188)

生成摘要时出错

---

## 72. How did pinwheel calculators work?

**原文标题**: How did pinwheel calculators work?

**原文链接**: [https://blog.coredump.cx/p/how-did-pinwheel-calculators-work](https://blog.coredump.cx/p/how-did-pinwheel-calculators-work)

生成摘要时出错

---

## 73. Looped Models Are Fast Multi-Token Predictors

**原文标题**: Looped Models Are Fast Multi-Token Predictors

**原文链接**: [https://arxiv.org/abs/2611.33896](https://arxiv.org/abs/2611.33896)

生成摘要时出错

---

## 74. Button Sounds – collection of professionally-recorded button clicks and presses

**原文标题**: Button Sounds – collection of professionally-recorded button clicks and presses

**原文链接**: [https://buttons.joshwcomeau.com/](https://buttons.joshwcomeau.com/)

生成摘要时出错

---

## 75. Qualcomm's Oryon 3 Reaches the Top

**原文标题**: Qualcomm's Oryon 3 Reaches the Top

**原文链接**: [https://chipsandcheese.com/p/qualcomms-oryon-3-reaches-the-top](https://chipsandcheese.com/p/qualcomms-oryon-3-reaches-the-top)

生成摘要时出错

---

## 76. SAP confirms "suspicious activities" on its GitHub platform [German]

**原文标题**: SAP confirms "suspicious activities" on its GitHub platform [German]

**原文链接**: [https://www.faz.net/agenturmeldungen/dpa/sap-haben-verdaechtige-aktivitaeten-identifiziert-201721612.html](https://www.faz.net/agenturmeldungen/dpa/sap-haben-verdaechtige-aktivitaeten-identifiziert-201721612.html)

生成摘要时出错

---

## 77. Nvidia Reinstates Jensen Huang as CEO

**原文标题**: Nvidia Reinstates Jensen Huang as CEO

**原文链接**: [https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

生成摘要时出错

---

## 78. Show HN: Silent dictation for Claude Code via on-device lip reading

**原文标题**: Show HN: Silent dictation for Claude Code via on-device lip reading

**原文链接**: [https://github.com/batanus/lip-dictation](https://github.com/batanus/lip-dictation)

生成摘要时出错

---

## 79. 'AI' might be the end of our careers

**原文标题**: 'AI' might be the end of our careers

**原文链接**: [https://www.baldurbjarnason.com/2026/08-ai-might-be-the-end-of-our-careers/](https://www.baldurbjarnason.com/2026/08-ai-might-be-the-end-of-our-careers/)

生成摘要时出错

---

## 80. Taking over US Treasury subdomains for $3 each

**原文标题**: Taking over US Treasury subdomains for $3 each

**原文链接**: [https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each](https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each)

生成摘要时出错

---

## 81. Britain's ghost stations

**原文标题**: Britain's ghost stations

**原文链接**: [https://spectator.com/article/britains-ghost-stations-are-fascinating/](https://spectator.com/article/britains-ghost-stations-are-fascinating/)

生成摘要时出错

---

## 82. Nfs2root: A 12-year-old pre-auth remote root in the Linux kernel's NFS server

**原文标题**: Nfs2root: A 12-year-old pre-auth remote root in the Linux kernel's NFS server

**原文链接**: [https://opensec.in/blog/nfs2root-cve-2026-99362](https://opensec.in/blog/nfs2root-cve-2026-99362)

生成摘要时出错

---

## 83. Bare Metal Qwen

**原文标题**: Bare Metal Qwen

**原文链接**: [https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os)

生成摘要时出错

---

## 84. MCP Gateway: How Snap Checks Both the Person and the Agent

**原文标题**: MCP Gateway: How Snap Checks Both the Person and the Agent

**原文链接**: [https://eng.snap.com/mcp-gateway](https://eng.snap.com/mcp-gateway)

生成摘要时出错

---

## 85. GTA 6 Running on Windows

**原文标题**: GTA 6 Running on Windows

**原文链接**: [https://twitter.com/raul_bs3/status/2125213756238291075](https://twitter.com/raul_bs3/status/2125213756238291075)

生成摘要时出错

---

## 86. Z.ai clarifies GLM-5.5 has not been delayed, scheduled for December launch

**原文标题**: Z.ai clarifies GLM-5.5 has not been delayed, scheduled for December launch

**原文链接**: [https://reddit.com/r/LocalLLaMA/comments/1y6260i/zai_clarifies_glm55_has_not_been_delayed/](https://reddit.com/r/LocalLLaMA/comments/1y6260i/zai_clarifies_glm55_has_not_been_delayed/)

生成摘要时出错

---

## 87. Getting old Java phones online again

**原文标题**: Getting old Java phones online again

**原文链接**: [https://antcating.github.io/2026/11/23/getting-old-java-phones-online-again.html](https://antcating.github.io/2026/11/23/getting-old-java-phones-online-again.html)

生成摘要时出错

---

## 88. XKCD and Fourier

**原文标题**: XKCD and Fourier

**原文链接**: [https://leancrew.com/all-this/2026/10/xkcd-and-fourier/](https://leancrew.com/all-this/2026/10/xkcd-and-fourier/)

生成摘要时出错

---

## 89. The Engineering of Smartphone Cameras

**原文标题**: The Engineering of Smartphone Cameras

**原文链接**: [https://www.pencilofrays.com/smartphone-lens/](https://www.pencilofrays.com/smartphone-lens/)

生成摘要时出错

---

## 90. Free alternative TV network built from the Internet Archive's forgotten videos

**原文标题**: Free alternative TV network built from the Internet Archive's forgotten videos

**原文链接**: [https://spelunkr.tv](https://spelunkr.tv)

生成摘要时出错

---

## 91. The trouble with serendipity: Scientific discoveries don't happen how you think

**原文标题**: The trouble with serendipity: Scientific discoveries don't happen how you think

**原文链接**: [https://www.worksinprogress.news/p/the-trouble-with-serendipity](https://www.worksinprogress.news/p/the-trouble-with-serendipity)

生成摘要时出错

---

## 92. Hkust 3D Prints a Titanium Alloy That Keeps Hardening

**原文标题**: Hkust 3D Prints a Titanium Alloy That Keeps Hardening

**原文链接**: [https://3dprinting.com/news/hkust-researchers-3d-print-a-titanium-alloy-that-keeps-hardening-under-strain/](https://3dprinting.com/news/hkust-researchers-3d-print-a-titanium-alloy-that-keeps-hardening-under-strain/)

生成摘要时出错

---

## 93. In C++, = default and {} are not the same constructor

**原文标题**: In C++, = default and {} are not the same constructor

**原文链接**: [https://lemire.me/blog/2026/11/02/default-and-braces-are-not-the-same-constructor/](https://lemire.me/blog/2026/11/02/default-and-braces-are-not-the-same-constructor/)

生成摘要时出错

---

## 94. Show HN: An agent skill that optimizes code with falsifiable hypotheses

**原文标题**: Show HN: An agent skill that optimizes code with falsifiable hypotheses

**原文链接**: [https://chszlab.github.io/AgenticAlgorithmEngineering/](https://chszlab.github.io/AgenticAlgorithmEngineering/)

生成摘要时出错

---

## 95. Hacking radiators

**原文标题**: Hacking radiators

**原文链接**: [https://qsantos.fr/2026/11/20/hacking-radiators-for-fun-and-no-profit/](https://qsantos.fr/2026/11/20/hacking-radiators-for-fun-and-no-profit/)

生成摘要时出错

---

## 96. Deploying a payphone on a tiny Pacific Island for fun and zero profit

**原文标题**: Deploying a payphone on a tiny Pacific Island for fun and zero profit

**原文链接**: [https://nickvsnetworking.com/deploying-a-payphone-on-a-tiny-pacific-island-for-fun-and-zero-profit/](https://nickvsnetworking.com/deploying-a-payphone-on-a-tiny-pacific-island-for-fun-and-zero-profit/)

生成摘要时出错

---

## 97. GTA 6 Recomp (Leonida) banned from GitHub while lead dev was in school

**原文标题**: GTA 6 Recomp (Leonida) banned from GitHub while lead dev was in school

**原文链接**: [https://github.com/ItsNotRexed/Leonida/issues](https://github.com/ItsNotRexed/Leonida/issues)

生成摘要时出错

---

## 98. Ladybird is now in alpha

**原文标题**: Ladybird is now in alpha

**原文链接**: [https://ladybird.org/posts/alpha/](https://ladybird.org/posts/alpha/)

生成摘要时出错

---

## 99. Pinocchio at 200: a tale of hunger, greed and Italy's culinary history

**原文标题**: Pinocchio at 200: a tale of hunger, greed and Italy's culinary history

**原文链接**: [https://www.repubblica.it/en/europe/food-travel/2026/11/24/news/carlo_collodi_pinocchio_pellegrino_artusi_italian_literature-425744069/](https://www.repubblica.it/en/europe/food-travel/2026/11/24/news/carlo_collodi_pinocchio_pellegrino_artusi_italian_literature-425744069/)

生成摘要时出错

---

## 100. Windows Loudness Equalization, reverse-engineered and ported to PipeWire

**原文标题**: Windows Loudness Equalization, reverse-engineered and ported to PipeWire

**原文链接**: [https://github.com/xoxorwr/pw-loudness-eq](https://github.com/xoxorwr/pw-loudness-eq)

生成摘要时出错

---

