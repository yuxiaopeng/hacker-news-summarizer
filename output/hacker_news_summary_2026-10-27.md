# Hacker News 热门文章摘要 (2026-10-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Wikipedia's Cleanup of AI-Generated Content

**原文标题**: Wikipedia's Cleanup of AI-Generated Content

**原文链接**: [https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup](https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup)

生成摘要时出错

---

## 12. Three TLS Bugs in GoAhead

**原文标题**: Three TLS Bugs in GoAhead

**原文链接**: [https://foxio.io/blog/choose-your-backend-three-tls-bugs-in-goahead](https://foxio.io/blog/choose-your-backend-three-tls-bugs-in-goahead)

生成摘要时出错

---

## 13. Introducing LFM3: Every Modality for Specialized Intelligence

**原文标题**: Introducing LFM3: Every Modality for Specialized Intelligence

**原文链接**: [https://www.liquid.ai/blog/lfm3](https://www.liquid.ai/blog/lfm3)

生成摘要时出错

---

## 14. Four Months of Zig

**原文标题**: Four Months of Zig

**原文链接**: [https://gracefulliberty.com/articles/four-months-of-zig/](https://gracefulliberty.com/articles/four-months-of-zig/)

生成摘要时出错

---

## 15. US Government is hiding a secret court ruling about how it spies on Americans

**原文标题**: US Government is hiding a secret court ruling about how it spies on Americans

**原文链接**: [https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/](https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/)

生成摘要时出错

---

## 16. Why Micron Is Suddenly Ditching 4F² DRAM as Rivals Double Down

**原文标题**: Why Micron Is Suddenly Ditching 4F² DRAM as Rivals Double Down

**原文链接**: [https://hothardware.com/news/why-micron-is-suddenly-ditching-4f-dram](https://hothardware.com/news/why-micron-is-suddenly-ditching-4f-dram)

生成摘要时出错

---

## 17. Here be monsters: What do you still need to know when agents do the work?

**原文标题**: Here be monsters: What do you still need to know when agents do the work?

**原文链接**: [https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work](https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work)

生成摘要时出错

---

## 18. Anthropic trained Claude on illegally obtained Stanford professors' books

**原文标题**: Anthropic trained Claude on illegally obtained Stanford professors' books

**原文链接**: [https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/)

生成摘要时出错

---

## 19. Microsoft and others tell crypto platform not to tokenize their stocks

**原文标题**: Microsoft and others tell crypto platform not to tokenize their stocks

**原文链接**: [https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368](https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368)

生成摘要时出错

---

## 20. Amazon Is Gutting Its AI Division After Sustained Failure

**原文标题**: Amazon Is Gutting Its AI Division After Sustained Failure

**原文链接**: [https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova](https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova)

生成摘要时出错

---

## 21. PHP2Shell, LiteLLM, GitLab: Find What You Need to Patch

**原文标题**: PHP2Shell, LiteLLM, GitLab: Find What You Need to Patch

**原文链接**: [https://cloudsleuth.io/blog/php2shell-litellm-gitlab-find-what-you-run/](https://cloudsleuth.io/blog/php2shell-litellm-gitlab-find-what-you-run/)

生成摘要时出错

---

## 22. Rosettes and Other Hidden Traces of Hamburg's Tram

**原文标题**: Rosettes and Other Hidden Traces of Hamburg's Tram

**原文链接**: [https://alsterrunde.com/rosettes-and-other-hidden-traces-of-hamburgs-tram/](https://alsterrunde.com/rosettes-and-other-hidden-traces-of-hamburgs-tram/)

生成摘要时出错

---

## 23. Discord will soon let anyone find public server messages through Google

**原文标题**: Discord will soon let anyone find public server messages through Google

**原文链接**: [https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover](https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover)

生成摘要时出错

---

## 24. Land Value Capture in Practice: Ethiopia's Urban Land Lease System

**原文标题**: Land Value Capture in Practice: Ethiopia's Urban Land Lease System

**原文链接**: [https://blog.landeconomics.org/p/land-value-capture-in-practice-reflections](https://blog.landeconomics.org/p/land-value-capture-in-practice-reflections)

生成摘要时出错

---

## 25. OpenLDK: Bringing the Java World into Common Lisp

**原文标题**: OpenLDK: Bringing the Java World into Common Lisp

**原文链接**: [https://atgreen.github.io/repl-yell/posts/openldk-java-in-common-lisp/](https://atgreen.github.io/repl-yell/posts/openldk-java-in-common-lisp/)

生成摘要时出错

---

## 26. PHP2Shell: Exploitation attempts and remediation trends

**原文标题**: PHP2Shell: Exploitation attempts and remediation trends

**原文链接**: [https://www.wiz.io/blog/php2shell-exploitation-so-far](https://www.wiz.io/blog/php2shell-exploitation-so-far)

生成摘要时出错

---

## 27. 警方正利用人工智能拦截有“可疑”行为的司机。

**原文标题**: Police are using AI to pull over drivers for 'suspicious' behavior

**原文链接**: [https://gizmodo.com/police-are-using-ai-to-pull-over-drivers-for-suspicious-behavior-2000831220](https://gizmodo.com/police-are-using-ai-to-pull-over-drivers-for-suspicious-behavior-2000831220)

生成摘要时出错

---

## 28. Vicious Cycles: Theses on a philosophy of news (2020)

**原文标题**: Vicious Cycles: Theses on a philosophy of news (2020)

**原文链接**: [https://harpers.org/archive/2020/01/vicious-cycles-theses-on-a-philosophy-of-news/](https://harpers.org/archive/2020/01/vicious-cycles-theses-on-a-philosophy-of-news/)

生成摘要时出错

---

## 29. A Stackless Floodfill Automaton

**原文标题**: A Stackless Floodfill Automaton

**原文链接**: [https://t3x.org/files/floodfill.pdf](https://t3x.org/files/floodfill.pdf)

生成摘要时出错

---

## 30. The Mythical Man-Month in the Age of AI

**原文标题**: The Mythical Man-Month in the Age of AI

**原文链接**: [https://j11g.com/the-mythical-man-month-in-the-age-of-ai](https://j11g.com/the-mythical-man-month-in-the-age-of-ai)

生成摘要时出错

---

## 31. Show HN: Specification First Agentic Development Plugin and Prove

**原文标题**: Show HN: Specification First Agentic Development Plugin and Prove

**原文链接**: [https://spec-first.dev/](https://spec-first.dev/)

生成摘要时出错

---

## 32. Gforth 1.0

**原文标题**: Gforth 1.0

**原文链接**: [https://gforth.org/manual/1.0/NEWS.html](https://gforth.org/manual/1.0/NEWS.html)

生成摘要时出错

---

## 33. A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies

**原文标题**: A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies

**原文链接**: [https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497)

生成摘要时出错

---

## 34. Software may be getting worse, but it used to be horrible

**原文标题**: Software may be getting worse, but it used to be horrible

**原文链接**: [https://www.bitlog.com/2026/10/27/software-may-be-getting-worse-but-it-used-to-be-horrible/](https://www.bitlog.com/2026/10/27/software-may-be-getting-worse-but-it-used-to-be-horrible/)

生成摘要时出错

---

## 35. Three new discoveries in mathematics, computer science, and physics

**原文标题**: Three new discoveries in mathematics, computer science, and physics

**原文链接**: [https://openai.com/index/building-scientific-understanding-with-academic-communities/](https://openai.com/index/building-scientific-understanding-with-academic-communities/)

生成摘要时出错

---

## 36. Is my data used for model training?

**原文标题**: Is my data used for model training?

**原文链接**: [https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)

生成摘要时出错

---

## 37. A 28-Year-Old DOGE Operative Gutted USAID. HR Had No Record of Him Working There

**原文标题**: A 28-Year-Old DOGE Operative Gutted USAID. HR Had No Record of Him Working There

**原文链接**: [https://www.wired.com/story/a-28-year-old-doge-operative-gutted-usaid-hr-had-no-record-of-him-working-there/](https://www.wired.com/story/a-28-year-old-doge-operative-gutted-usaid-hr-had-no-record-of-him-working-there/)

生成摘要时出错

---

## 38. Roblox downloaded 145GB models from us (including adult content) without asking

**原文标题**: Roblox downloaded 145GB models from us (including adult content) without asking

**原文链接**: [https://open3dlab.com/news/roblox-downloaded-145-gb-of-models-from-our-sites/](https://open3dlab.com/news/roblox-downloaded-145-gb-of-models-from-our-sites/)

生成摘要时出错

---

## 39. Analysis of ‘Demon Seed’ (2025)

**原文标题**: Analysis of ‘Demon Seed’ (2025)

**原文链接**: [https://mawrgorshin.com/2025/07/12/analysis-of-demon-seed/](https://mawrgorshin.com/2025/07/12/analysis-of-demon-seed/)

生成摘要时出错

---

## 40. Maine banned phones in schools to help teens focus and connect. It's working

**原文标题**: Maine banned phones in schools to help teens focus and connect. It's working

**原文链接**: [https://apnews.com/article/maine-cellphone-ban-positive-changes-83bb538cf45879ce6ab4639c6cc73b7b](https://apnews.com/article/maine-cellphone-ban-positive-changes-83bb538cf45879ce6ab4639c6cc73b7b)

生成摘要时出错

---

## 41. I still teach OpenGL ES 3.0

**原文标题**: I still teach OpenGL ES 3.0

**原文链接**: [https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html](https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html)

生成摘要时出错

---

## 42. 188-Year-Old Mystery of Photography's First Human Subjects Solved

**原文标题**: 188-Year-Old Mystery of Photography's First Human Subjects Solved

**原文链接**: [https://news.artnet.com/art-world/daguerre-photograph-subjects-location-2826596](https://news.artnet.com/art-world/daguerre-photograph-subjects-location-2826596)

生成摘要时出错

---

## 43. Show HN: Encarta 95 Web

**原文标题**: Show HN: Encarta 95 Web

**原文链接**: [https://benwinding.github.io/encarta_95_web/#/article/Art](https://benwinding.github.io/encarta_95_web/#/article/Art)

生成摘要时出错

---

## 44. Antique Fonts Collection – Restored 19th Century Typefaces

**原文标题**: Antique Fonts Collection – Restored 19th Century Typefaces

**原文链接**: [https://centurylibrary.com/collection/antique-fonts/](https://centurylibrary.com/collection/antique-fonts/)

生成摘要时出错

---

## 45. New 14‑inch MacBook Pro with M6

**原文标题**: New 14‑inch MacBook Pro with M6

**原文链接**: [https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/](https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)

生成摘要时出错

---

## 46. The Exponential Time Hypothesis Is False [pdf]

**原文标题**: The Exponential Time Hypothesis Is False [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf)

The provided text describes a file metadata entry for a paper titled **"The Exponential Time Hypothesis Is False,"** hosted on a GitHub repository. While the full text of the paper is not included in your prompt, the title refers to a revolutionary and highly controversial claim in the field of theoretical computer science.

**Key Information and Context:**

*   **The Claim:** The paper asserts that the **Exponential Time Hypothesis (ETH)** is incorrect. ETH is a fundamental conjecture which posits that the 3-Satisfiability problem (3-SAT) cannot be solved in sub-exponential time (specifically, it requires $2^{\delta n}$ time for some $\delta > 0$).
*   **Significance:** ETH is a cornerstone of "fine-grained complexity." Many researchers use ETH as a baseline to prove that certain algorithms are as efficient as they can possibly be. If ETH is false, it would mean that many NP-complete problems might be solvable much faster than currently believed, potentially collapsing long-standing assumptions about the limits of computation.
*   **Scientific Standing:** In the computer science community, ETH is widely believed to be true. Most papers claiming to disprove such foundational hypotheses are viewed with extreme skepticism. Without peer review or validation from the broader academic community, such a document is generally considered an unverified or "fringe" claim.

**Summary:**
The document represents an attempt to refute one of the most important conjectures in computational complexity. If the author’s proof were found to be correct, it would necessitate a massive rewrite of modern complexity theory and suggest that problems previously thought to be intractable may have significantly more efficient solutions. However, given its placement on a public repository rather than a major peer-reviewed journal, the findings remain unvalidated by the scientific community.

---

## 47. How to grow a cacao tree at home (2024)

**原文标题**: How to grow a cacao tree at home (2024)

**原文链接**: [https://www.cocoterra.com/guide-on-how-to-grow-chocolate-at-home/](https://www.cocoterra.com/guide-on-how-to-grow-chocolate-at-home/)

生成摘要时出错

---

## 48. Data Recovery CEO Indicted for Allegedly Scamming Ransomware Victims

**原文标题**: Data Recovery CEO Indicted for Allegedly Scamming Ransomware Victims

**原文链接**: [https://www.propublica.org/article/zohar-pinhasi-monstercloud-ransomware-indictment](https://www.propublica.org/article/zohar-pinhasi-monstercloud-ransomware-indictment)

生成摘要时出错

---

## 49. 16-bit Windows (Windows 1.x, 2.x, 3.0, 3.1, etc.) on 64-bit Windows

**原文标题**: 16-bit Windows (Windows 1.x, 2.x, 3.0, 3.1, etc.) on 64-bit Windows

**原文链接**: [https://github.com/otya128/winevdm](https://github.com/otya128/winevdm)

生成摘要时出错

---

## 50. Kauldron: Modular, scalable library to train ML models

**原文标题**: Kauldron: Modular, scalable library to train ML models

**原文链接**: [https://github.com/google-research/kauldron](https://github.com/google-research/kauldron)

生成摘要时出错

---

## 51. Police Are Pulling People over Because AI Deems Their Driving "Suspicious"

**原文标题**: Police Are Pulling People over Because AI Deems Their Driving "Suspicious"

**原文链接**: [https://www.aclu.org/news/privacy-technology/ai-driven-police-stops](https://www.aclu.org/news/privacy-technology/ai-driven-police-stops)

生成摘要时出错

---

## 52. Writing about pratt parsing so I remember it

**原文标题**: Writing about pratt parsing so I remember it

**原文链接**: [https://www.unix.dog/~yosh/blog/2026-10-25_pratt-parsing.html](https://www.unix.dog/~yosh/blog/2026-10-25_pratt-parsing.html)

生成摘要时出错

---

## 53. We let our cloud agents query prod (with OIDC, not secrets)

**原文标题**: We let our cloud agents query prod (with OIDC, not secrets)

**原文链接**: [https://www.formal.ai/blog/cloud-agents-oidc-infrastructure/](https://www.formal.ai/blog/cloud-agents-oidc-infrastructure/)

生成摘要时出错

---

## 54. A Man from the Future: Why Johnny Can't Stop Abstracting

**原文标题**: A Man from the Future: Why Johnny Can't Stop Abstracting

**原文链接**: [http://muratbuffalo.blogspot.com/2026/10/the-man-from-future-why-johnny-cant.html](http://muratbuffalo.blogspot.com/2026/10/the-man-from-future-why-johnny-cant.html)

生成摘要时出错

---

## 55. Sebastian Raschka's from-scratch video course on building reasoning models

**原文标题**: Sebastian Raschka's from-scratch video course on building reasoning models

**原文链接**: [https://magazine.sebastianraschka.com/p/building-reasoning-models](https://magazine.sebastianraschka.com/p/building-reasoning-models)

生成摘要时出错

---

## 56. Show HN: Agent-relay for multi-vendor coding sessions

**原文标题**: Show HN: Agent-relay for multi-vendor coding sessions

**原文链接**: [https://github.com/saranyan/agent-relay](https://github.com/saranyan/agent-relay)

生成摘要时出错

---

## 57. JetBrains IDEs are now powered by libghostty

**原文标题**: JetBrains IDEs are now powered by libghostty

**原文链接**: [https://blog.jetbrains.com/platform/2026/10/jetbrains-terminal-now-uses-ghostty/](https://blog.jetbrains.com/platform/2026/10/jetbrains-terminal-now-uses-ghostty/)

生成摘要时出错

---

## 58. Play Cyberpunk 2077 in the Browser

**原文标题**: Play Cyberpunk 2077 in the Browser

**原文链接**: [https://cyberpunk2077.lol/](https://cyberpunk2077.lol/)

生成摘要时出错

---

## 59. Nietzschian Debugger

**原文标题**: Nietzschian Debugger

**原文链接**: [https://github.com/DilawarShafiq/nietzschian-debugger](https://github.com/DilawarShafiq/nietzschian-debugger)

生成摘要时出错

---

## 60. Solar power is becoming bigger than nuclear

**原文标题**: Solar power is becoming bigger than nuclear

**原文链接**: [https://www.bbc.com/future/article/20261023-how-solar-became-bigger-than-nuclear](https://www.bbc.com/future/article/20261023-how-solar-became-bigger-than-nuclear)

生成摘要时出错

---

## 61. Who Is Responsible for Tackling Professional Deskilling?

**原文标题**: Who Is Responsible for Tackling Professional Deskilling?

**原文链接**: [https://www.degruyterbrill.com/document/doi/10.1515/humaff-2026-0080/html](https://www.degruyterbrill.com/document/doi/10.1515/humaff-2026-0080/html)

生成摘要时出错

---

## 62. Oldest GUI application that still runs on Windows 11

**原文标题**: Oldest GUI application that still runs on Windows 11

**原文链接**: [https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/)

生成摘要时出错

---

## 63. Microsoft offers mass buyouts for roughly a quarter of its workforce

**原文标题**: Microsoft offers mass buyouts for roughly a quarter of its workforce

**原文链接**: [https://www.seattletimes.com/business/microsoft/microsoft-offers-mass-buyouts-for-roughly-a-quarter-of-its-workforce/](https://www.seattletimes.com/business/microsoft/microsoft-offers-mass-buyouts-for-roughly-a-quarter-of-its-workforce/)

生成摘要时出错

---

## 64. Reducibility Among Combinatorial Problems (1972) [pdf]

**原文标题**: Reducibility Among Combinatorial Problems (1972) [pdf]

**原文链接**: [https://cgi.di.uoa.gr/~sgk/teaching/grad/handouts/karp.pdf](https://cgi.di.uoa.gr/~sgk/teaching/grad/handouts/karp.pdf)

生成摘要时出错

---

## 65. APC says let there be light, with standards to speed up photonics manufacturing

**原文标题**: APC says let there be light, with standards to speed up photonics manufacturing

**原文链接**: [https://www.nextplatform.com/connect/2026/10/23/apc-says-let-there-be-light-with-raft-of-standards-to-speed-up-photonics-manufacturing/5304950](https://www.nextplatform.com/connect/2026/10/23/apc-says-let-there-be-light-with-raft-of-standards-to-speed-up-photonics-manufacturing/5304950)

生成摘要时出错

---

## 66. GPT-6.1 Terra

**原文标题**: GPT-6.1 Terra

**原文链接**: [https://openai.com/index/introducing-gpt-6-1-terra/](https://openai.com/index/introducing-gpt-6-1-terra/)

生成摘要时出错

---

## 67. Txoko: Basques' traditional feast a gastronomic peek into a culture (2024)

**原文标题**: Txoko: Basques' traditional feast a gastronomic peek into a culture (2024)

**原文链接**: [https://johnhendersontravel.com/txoko/](https://johnhendersontravel.com/txoko/)

生成摘要时出错

---

## 68. 'I Felt Blind Panic.' They Opened Their New $2k iPhone Duo–and It Broke

**原文标题**: 'I Felt Blind Panic.' They Opened Their New $2k iPhone Duo–and It Broke

**原文链接**: [https://www.wsj.com/tech/personal-tech/iphone-duo-broken-hinge-screen-31b2b28a](https://www.wsj.com/tech/personal-tech/iphone-duo-broken-hinge-screen-31b2b28a)

生成摘要时出错

---

## 69. Fixing Tool-Call Accuracy in vLLM

**原文标题**: Fixing Tool-Call Accuracy in vLLM

**原文链接**: [https://www.ubicloud.com/blog/fixing-tool-call-accuracy-in-vllm](https://www.ubicloud.com/blog/fixing-tool-call-accuracy-in-vllm)

生成摘要时出错

---

## 70. LISPy things you can do in 64K bytes of core (2019)

**原文标题**: LISPy things you can do in 64K bytes of core (2019)

**原文链接**: [https://t3x.org/lisp64k/index.html](https://t3x.org/lisp64k/index.html)

生成摘要时出错

---

## 71. CSS-Tricks has a new owner

**原文标题**: CSS-Tricks has a new owner

**原文链接**: [https://css-tricks.com/css-tricks-has-a-new-owner/](https://css-tricks.com/css-tricks-has-a-new-owner/)

生成摘要时出错

---

## 72. Ghostty 1.4

**原文标题**: Ghostty 1.4

**原文链接**: [https://twitter.com/mitchellh/status/2115124583170974193](https://twitter.com/mitchellh/status/2115124583170974193)

生成摘要时出错

---

## 73. We should be more ambitious with the software we build

**原文标题**: We should be more ambitious with the software we build

**原文链接**: [https://danluu.com/ambitious/](https://danluu.com/ambitious/)

生成摘要时出错

---

## 74. Virtual and Real World Combine at LAN Party (1998)

**原文标题**: Virtual and Real World Combine at LAN Party (1998)

**原文链接**: [https://www.latimes.com/archives/la-xpm-1998-aug-10-mn-11870-story.html](https://www.latimes.com/archives/la-xpm-1998-aug-10-mn-11870-story.html)

生成摘要时出错

---

## 75. Alleged Israeli spy company targeted Starlink users

**原文标题**: Alleged Israeli spy company targeted Starlink users

**原文链接**: [https://www.reuters.com/business/media-telecom/alleged-israeli-spy-company-heavily-targeted-starlink-users-sources-say-2026-10-27/](https://www.reuters.com/business/media-telecom/alleged-israeli-spy-company-heavily-targeted-starlink-users-sources-say-2026-10-27/)

生成摘要时出错

---

## 76. Type Server Protocol

**原文标题**: Type Server Protocol

**原文链接**: [https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)

生成摘要时出错

---

## 77. Behind the scenes at the NeXT Computer office

**原文标题**: Behind the scenes at the NeXT Computer office

**原文链接**: [https://exhibits.stanford.edu/menuez/browse/next-computer-inc?per_page=96&sort=pub_year_isi+asc%2C+title_sort+asc&view=masonry](https://exhibits.stanford.edu/menuez/browse/next-computer-inc?per_page=96&sort=pub_year_isi+asc%2C+title_sort+asc&view=masonry)

生成摘要时出错

---

## 78. Chocolate Is Getting Worse

**原文标题**: Chocolate Is Getting Worse

**原文链接**: [https://www.grubstreet.com/article/chocolate-hersheys-reeses-conspiracy.html](https://www.grubstreet.com/article/chocolate-hersheys-reeses-conspiracy.html)

生成摘要时出错

---

## 79. New iPad mini

**原文标题**: New iPad mini

**原文链接**: [https://www.apple.com/newsroom/2026/10/apple-gives-ipad-mini-its-biggest-update-ever/](https://www.apple.com/newsroom/2026/10/apple-gives-ipad-mini-its-biggest-update-ever/)

生成摘要时出错

---

## 80. Birdwatching rewires the brain and slows cognitive decline

**原文标题**: Birdwatching rewires the brain and slows cognitive decline

**原文链接**: [https://www.bbc.com/future/article/20261019-birdwatching-rewires-the-brain-and-slows-cognitive-decline](https://www.bbc.com/future/article/20261019-birdwatching-rewires-the-brain-and-slows-cognitive-decline)

生成摘要时出错

---

## 81. A Printer Printing onto Paper

**原文标题**: A Printer Printing onto Paper

**原文链接**: [https://twitter.com/macrofying/status/2112904628509528219](https://twitter.com/macrofying/status/2112904628509528219)

生成摘要时出错

---

## 82. Sigma Says the Compact, Modular FP2 Is the Ultimate Hybrid Camera

**原文标题**: Sigma Says the Compact, Modular FP2 Is the Ultimate Hybrid Camera

**原文链接**: [https://petapixel.com/2026/10/22/sigma-says-the-compact-modular-fp2-is-the-ultimate-hybrid-camera/](https://petapixel.com/2026/10/22/sigma-says-the-compact-modular-fp2-is-the-ultimate-hybrid-camera/)

生成摘要时出错

---

## 83. Local Wikipedia: Wikipedia, but only for things a half hour walk from you

**原文标题**: Local Wikipedia: Wikipedia, but only for things a half hour walk from you

**原文链接**: [https://edjefferson.com/localwiki/](https://edjefferson.com/localwiki/)

生成摘要时出错

---

## 84. Websites Should Be Printable

**原文标题**: Websites Should Be Printable

**原文链接**: [https://brennenputh.me/blog/printable-websites/](https://brennenputh.me/blog/printable-websites/)

生成摘要时出错

---

## 85. Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)

**原文标题**: Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)

**原文链接**: [https://blog.cloudflare.com/kv-cache-exposure-remediation/](https://blog.cloudflare.com/kv-cache-exposure-remediation/)

生成摘要时出错

---

## 86. Show HN: A Truly Modular Keyboard

**原文标题**: Show HN: A Truly Modular Keyboard

**原文链接**: [https://github.com/notaroomba/keybytes](https://github.com/notaroomba/keybytes)

生成摘要时出错

---

## 87. Show HN: Hob - Open-source, on device alternative to Claude Cowork and ChatGPT

**原文标题**: Show HN: Hob - Open-source, on device alternative to Claude Cowork and ChatGPT

**原文链接**: [https://github.com/FrigadeHQ/hob](https://github.com/FrigadeHQ/hob)

生成摘要时出错

---

## 88. Is PHP Running on Your ColdFusion Server? How to Check, and Remove It

**原文标题**: Is PHP Running on Your ColdFusion Server? How to Check, and Remove It

**原文链接**: [https://www.gregoryalexander.com/blog/2026/10/23/is-php-quietly-running-on-your-coldfusion-server-how-to-check-and-remove-it](https://www.gregoryalexander.com/blog/2026/10/23/is-php-quietly-running-on-your-coldfusion-server-how-to-check-and-remove-it)

生成摘要时出错

---

## 89. Industry Knew for Decades That Microplastics Could Infiltrate Human Bodies

**原文标题**: Industry Knew for Decades That Microplastics Could Infiltrate Human Bodies

**原文链接**: [https://e360.yale.edu/digest/chemical-industry-microplastics](https://e360.yale.edu/digest/chemical-industry-microplastics)

生成摘要时出错

---

## 90. Diamond Transistor

**原文标题**: Diamond Transistor

**原文链接**: [https://www.df.com/diamond-transistor](https://www.df.com/diamond-transistor)

生成摘要时出错

---

## 91. Wanted: Robot-Dog Walkers. $20/Hour

**原文标题**: Wanted: Robot-Dog Walkers. $20/Hour

**原文链接**: [https://www.nytimes.com/2026/10/27/technology/robot-dog-walkers.html](https://www.nytimes.com/2026/10/27/technology/robot-dog-walkers.html)

生成摘要时出错

---

## 92. Blaise Pascal invented fixed route public transport (2024)

**原文标题**: Blaise Pascal invented fixed route public transport (2024)

**原文链接**: [https://humantransit.org/2024/12/one-of-the-greatest-inventions-in-the-history-of-human-transport.html](https://humantransit.org/2024/12/one-of-the-greatest-inventions-in-the-history-of-human-transport.html)

生成摘要时出错

---

## 93. In China, the AI bubble has burst

**原文标题**: In China, the AI bubble has burst

**原文链接**: [https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html](https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html)

生成摘要时出错

---

## 94. I will no longer upload to NEW

**原文标题**: I will no longer upload to NEW

**原文链接**: [https://lists.debian.org/debian-devel/2026/10/msg00263.html](https://lists.debian.org/debian-devel/2026/10/msg00263.html)

生成摘要时出错

---

## 95. Colorfigures

**原文标题**: Colorfigures

**原文链接**: [https://april-zhu.com/colorfigures](https://april-zhu.com/colorfigures)

生成摘要时出错

---

## 96. PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP

**原文标题**: PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP

**原文链接**: [https://github.com/KrushnaVardhanReddy/PaperPilot](https://github.com/KrushnaVardhanReddy/PaperPilot)

生成摘要时出错

---

## 97. Hy-Nomas, Tencent's new open-source world model you can steer with text

**原文标题**: Hy-Nomas, Tencent's new open-source world model you can steer with text

**原文链接**: [https://huggingface.co/tencent/Hy-Nomas](https://huggingface.co/tencent/Hy-Nomas)

生成摘要时出错

---

## 98. Methane Hotspot Explorer

**原文标题**: Methane Hotspot Explorer

**原文链接**: [https://atmosphere.copernicus.eu/ghg-services/cams-methane-hotspot-explorer](https://atmosphere.copernicus.eu/ghg-services/cams-methane-hotspot-explorer)

生成摘要时出错

---

## 99. LimonOS Custom x86-64 Kernel

**原文标题**: LimonOS Custom x86-64 Kernel

**原文链接**: [https://github.com/AnonimusShamshiAlex/LimonOS](https://github.com/AnonimusShamshiAlex/LimonOS)

生成摘要时出错

---

## 100. Anthropic S-1

**原文标题**: Anthropic S-1

**原文链接**: [https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)

生成摘要时出错

---

