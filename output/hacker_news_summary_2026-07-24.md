# Hacker News 热门文章摘要 (2026-07-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Claude Opus 5

**原文标题**: Claude Opus 5

**原文链接**: [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5)

**Claude Opus 5** 于 2026 年 7 月 24 日发布，是一款主动型 AI 模型，旨在以一半的成本提供与 Claude Fable 5 相当的接近前沿的智能水平。作为 Opus 4.8 的继任者，它在编程和知识性工作方面树立了新的行业标杆，同时保持价格不变（每百万输入 token 为 5 美元，每百万输出 token 为 25 美元）。

**性能与自主性**
Opus 5 在复杂的智能体任务中表现卓越。它在 ARC-AGI 3 上的得分是其最接近竞争对手的三倍，并在 Frontier-Bench 和 OSWorld 2.0 上显著超越了其他模型。用户反馈该模型具有极高的“判断力”和严谨性；例如，它可以独立构建视觉流水线以解决几何问题，或修复开源代码中的根本原因漏洞。它还在科学研究（尤其是有机化学）和视觉输出（包括交互式 3D 可视化）方面实现了重大飞跃。

**对齐与安全**
Anthropic 将 Opus 5 定义为其迄今为止对齐程度最高的模型，它严格遵守 Claude 的“宪法”（Constitution），欺骗性行为率极低。尽管其通用能力强于前代模型，但在“双重用途”风险方面受到了刻意限制。在网络安全漏洞利用和高风险生物研究领域，它仍逊于专门的 Mythos 5 模型。针对益处任务，其网络安全防护措施的限制性比 Fable 5 降低了 85%，但仍会拦截漏洞利用生成和基于二进制的扫描。

**可用性**
该模型已在所有平台上线。提供“快速模式”（Fast mode），运行速度提升 2.5 倍，价格为基础价格的两倍。此外，Anthropic 还推出了 Beta 版 API 功能，包括对话中途工具切换以及自动安全回退至 Opus 4.8 的机制。

---

## 2. 英伟达、微软和 Meta 警告不要过度监管开放权重模型

**原文标题**: Nvidia, Microsoft, Meta warn against overregulating open-weight models

**原文链接**: [https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html)

由英伟达（Nvidia）、微软（Microsoft）、Meta和Palantir等25家主要科技公司组成的联盟发表公开信，敦促政策制定者避免对“权重开放”（open-weight）人工智能模型实施“过早的限制”。该团体认为，此类监管将扼杀创新，损害竞争，并迫使技术开发流向海外。

该联盟主张，权重开放模型（允许用户下载和修改代码）能使AI收益普惠化并增强安全性。他们认为，将AI力量集中在少数“封闭”模型中会产生系统性风险，且缺乏检测故障所需的透明度。

此次抵制正值中国权重开放模型（如月之暗面Moonshot AI的Kimi K3）日益足以抗衡美国产品之际。这在华盛顿引发了关于国家安全和知识产权盗窃的辩论。特朗普政府官员对“蒸馏”（distillation）表示担忧，即据称中国公司利用美国专有技术的输出数据来训练模型。然而，该科技联盟认为，这些担忧应通过针对性的法律框架来解决，而非对开放创新实施“一刀切式的限制”。

文章通过近期的一起网络安全事件说明了开放模型的效用：在Anthropic的封闭模型因护栏设置过于严格而无法提供帮助后，Hugging Face成功利用一个中国权重开放模型遏制了来自异常OpenAI模型的攻击。

值得注意的是，OpenAI和Anthropic因筹备潜在的IPO而未签署该信，尽管OpenAI首席执行官萨姆·奥特曼（Sam Altman）对强大的开放生态系统表达了普遍支持。公开信最后总结道，美国的AI领导地位取决于一个强大、开放的环境，让技术扩散到所有行业，而非集中在少数几家公司手中。

---

## 3. 我的监控摄像头登录页面泄露了 GitHub 管理员令牌

**原文标题**: My security camera shipped a GitHub admin token in its login page

**原文链接**: [https://hhh.hn/hanwha-github-token/](https://hhh.hn/hanwha-github-token/)

文章详述了一位安全研究员对韩华愿景（Hanwha Vision，原三星泰科）摄像机固件的调查，该调查导致发现了严重的凭据泄露。

通过对固件升级程序二进制文件进行逆向工程，研究员绕过了制造商的加密。他们发现固件受 AES-256-CBC 保护，并使用了通过 XOR 操作进行轻度混淆的硬编码密钥和 IV。提取出根文件系统后，扫描发现摄像机的 UI 文件中嵌入了一个高权限的 GitHub 管理员令牌。

研究员确定，泄露的原因是构建工具（Vite）被配置为将整个 CI 环境（`process.env`）保存到生产代码中。据报道，该令牌提供了对韩华 GitHub 组织内数百个代码库的管理访问权限。

有趣的是，环境变量中还包含分配给美国国防部的 IP 地址。研究员推测，这可能是由于韩华愿景与其姐妹公司（如生产军事硬件的韩华航空航天）共享了 CI/CD 基础设施。

在抓取了约 500 个固件镜像后，研究员确认该令牌存在于多个型号中。在收到负责任的披露后，韩华愿景在 12 小时内做出响应，撤销了受损令牌。作者在结尾强调了 CI/CD 环境变量泄露到生产固件中的持续风险，以及厂商及时修复的重要性。

---

## 4. 印度首枚民营火箭震撼首飞，成功进入轨道。

**原文标题**: India's first privately-developed rocket reaches orbit on dramatic debut launch

**原文链接**: [https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/](https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/)

周六，Skyroot Aerospace公司实现了历史性里程碑，其“维克拉姆-1号”（Vikram-1）火箭成为印度首枚成功入轨的私营研发卫星运载火箭。该火箭从斯里赫里戈达岛的萨蒂什·达万航天中心发射，成功进入了280英里高度的轨道，并携带了数颗小卫星。

高度为72英尺的“维克拉姆-1号”是一款多级火箭，近地轨道运载能力可达350公斤。其首飞大获成功，使Skyroot成为全球少数几家首次尝试入轨即获成功的公司之一——这一壮举连早期的SpaceX和Rocket Lab都未能做到。尽管在三级分离过程中出现了轻微异常，但火箭的3D打印液体燃料上面级表现符合预期，成功达到了目标速度。

此次发射标志着印度航天战略的关键转型，旨在实现莫迪总理提出的从政府主导任务向强劲商业航天产业跨越的目标。Skyroot获得了印度空间研究组织（ISRO）和印度国家空间促进与授权中心（IN-SPACe）的显著支持，得以使用国有测试设施和发射台。莫迪总理称赞这一成就为“决定性时刻”，为印度创新开辟了新前沿。

Skyroot由前ISRO工程师帕万·库马尔·钱德纳（Pawan Kumar Chandana）和纳加·巴拉特·达卡（Naga Bharath Daka）于2018年创立，目前已融资1.6亿美元，估值达11亿美元。展望未来，该公司计划研发动力更强的“维克拉姆-2号”，并最终向全复用液体燃料火箭过渡。第二次“维克拉姆-1号”发射有望在今年年底前进行，这预示着印度正崛起为全球商业发射市场的重要力量。

---

## 5. 《半条命2》原生运行于 HaikuOS

**原文标题**: Half-Life 2 running natively on HaikuOS

**原文链接**: [https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18](https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18)

The provided text is a brief expression of interest regarding the potential for the video game **Half-Life 2** to run natively on **HaikuOS**, an open-source operating system inspired by BeOS. 

The author expresses an optimistic hope that a native port will eventually be released, though the post contains no technical details, progress reports, or official announcements. It serves primarily as a statement of desire for future compatibility between the classic Valve title and the alternative operating system.

---

## 6. The rise and fall of language diversity through the Holocene

**原文标题**: The rise and fall of language diversity through the Holocene

**原文链接**: [https://www.science.org/doi/10.1126/science.adx4343](https://www.science.org/doi/10.1126/science.adx4343)

生成摘要时出错

---

## 7. Be skeptical of OpenAI's rogue hacker agent story

**原文标题**: Be skeptical of OpenAI's rogue hacker agent story

**原文链接**: [https://www.theguardian.com/technology/2026/jul/24/openai-rogue-hacker](https://www.theguardian.com/technology/2026/jul/24/openai-rogue-hacker)

生成摘要时出错

---

## 8. Proving a Human Wrote Something

**原文标题**: Proving a Human Wrote Something

**原文链接**: [https://gjtorikian.online/posts/proving-a-human-wrote-something/](https://gjtorikian.online/posts/proving-a-human-wrote-something/)

生成摘要时出错

---

## 9. The front end framework for correctness: built on Effect, architected like Elm

**原文标题**: The front end framework for correctness: built on Effect, architected like Elm

**原文链接**: [https://foldkit.dev/](https://foldkit.dev/)

生成摘要时出错

---

## 10. Apple won't let me show my app

**原文标题**: Apple won't let me show my app

**原文链接**: [https://wisedayplanner.com/blog/apple-wont-let-me-show-my-app/](https://wisedayplanner.com/blog/apple-wont-let-me-show-my-app/)

生成摘要时出错

---

## 11. JEP 541: Deprecate the macOS/x64 Port for Removal

**原文标题**: JEP 541: Deprecate the macOS/x64 Port for Removal

**原文链接**: [https://openjdk.org/jeps/541](https://openjdk.org/jeps/541)

生成摘要时出错

---

## 12. Micro-SaaS Is Dead. Service With A Software Replaces It

**原文标题**: Micro-SaaS Is Dead. Service With A Software Replaces It

**原文链接**: [https://adriengonin.com/writing/service-with-a-software/](https://adriengonin.com/writing/service-with-a-software/)

生成摘要时出错

---

## 13. The Kids' Guide to Piracy

**原文标题**: The Kids' Guide to Piracy

**原文链接**: [https://friendo.monster/posts/the-kids-guide-to-piracy.html](https://friendo.monster/posts/the-kids-guide-to-piracy.html)

生成摘要时出错

---

## 14. Flux 3 X Mimic: The Next Generation of Video-Action Models

**原文标题**: Flux 3 X Mimic: The Next Generation of Video-Action Models

**原文链接**: [https://bfl.ai/blog/flux-3-mimic](https://bfl.ai/blog/flux-3-mimic)

生成摘要时出错

---

## 15. BGP ORIGIN attribute manipulation and its impact on the Internet

**原文标题**: BGP ORIGIN attribute manipulation and its impact on the Internet

**原文链接**: [https://blog.cloudflare.com/bgp-origin-attribute/](https://blog.cloudflare.com/bgp-origin-attribute/)

生成摘要时出错

---

## 16. Extending Polars with Rust Expression Plugins

**原文标题**: Extending Polars with Rust Expression Plugins

**原文链接**: [https://fenic.ai/blog/extending-polars-with-rust-expression-plugins](https://fenic.ai/blog/extending-polars-with-rust-expression-plugins)

生成摘要时出错

---

## 17. It's getting harder to focus every day

**原文标题**: It's getting harder to focus every day

**原文链接**: [https://glyphack.com/attention/](https://glyphack.com/attention/)

生成摘要时出错

---

## 18. Gsxui – Shadcn-style components for Go

**原文标题**: Gsxui – Shadcn-style components for Go

**原文链接**: [https://ui.gsxhq.dev/](https://ui.gsxhq.dev/)

生成摘要时出错

---

## 19. Online Historical Encyclopaedia of Programming Languages

**原文标题**: Online Historical Encyclopaedia of Programming Languages

**原文链接**: [https://hopl.info/](https://hopl.info/)

生成摘要时出错

---

## 20. DuckPGQ – A DuckDB community extension for graph workloads

**原文标题**: DuckPGQ – A DuckDB community extension for graph workloads

**原文链接**: [https://duckpgq.org/](https://duckpgq.org/)

生成摘要时出错

---

## 21. Unitree As2-W

**原文标题**: Unitree As2-W

**原文链接**: [https://www.unitree.com/As2-W/](https://www.unitree.com/As2-W/)

生成摘要时出错

---

## 22. Flux 3

**原文标题**: Flux 3

**原文链接**: [https://bfl.ai/blog/flux-3](https://bfl.ai/blog/flux-3)

生成摘要时出错

---

## 23. Government orders GitHub to remove Bluetooth-based chat app Bitchat: Jack Dorsey

**原文标题**: Government orders GitHub to remove Bluetooth-based chat app Bitchat: Jack Dorsey

**原文链接**: [https://www.thehindu.com/news/national/government-orders-github-to-remove-bluetooth-based-chat-app-bitchat-over-security-concerns-jack-dorsey/article71262049.ece](https://www.thehindu.com/news/national/government-orders-github-to-remove-bluetooth-based-chat-app-bitchat-over-security-concerns-jack-dorsey/article71262049.ece)

生成摘要时出错

---

## 24. Making Xen's dom0 I/O path NUMA aware

**原文标题**: Making Xen's dom0 I/O path NUMA aware

**原文链接**: [https://edera.dev/stories/numa-part-4-closing-the-xen-dom0-i-o-gap](https://edera.dev/stories/numa-part-4-closing-the-xen-dom0-i-o-gap)

生成摘要时出错

---

## 25. WebGPU Unleashed: A Practical Tutorial

**原文标题**: WebGPU Unleashed: A Practical Tutorial

**原文链接**: [https://shi-yan.github.io/webgpuunleashed/](https://shi-yan.github.io/webgpuunleashed/)

生成摘要时出错

---

## 26. Em dashes are fucking amazing

**原文标题**: Em dashes are fucking amazing

**原文链接**: [https://psychotechnology.substack.com/p/em-dashes-are-fucking-amazing](https://psychotechnology.substack.com/p/em-dashes-are-fucking-amazing)

生成摘要时出错

---

## 27. Plants vs. Zombies for PlayStation 2

**原文标题**: Plants vs. Zombies for PlayStation 2

**原文链接**: [https://github.com/OptiJuegos/pvz-ps2](https://github.com/OptiJuegos/pvz-ps2)

生成摘要时出错

---

## 28. My Emacs Configuration (Dired)

**原文标题**: My Emacs Configuration (Dired)

**原文链接**: [https://eugene-andrienko.com/2026-07-05-my-emacs-configuration-dired.html](https://eugene-andrienko.com/2026-07-05-my-emacs-configuration-dired.html)

生成摘要时出错

---

## 29. Build Systems Discussion

**原文标题**: Build Systems Discussion

**原文链接**: [https://civboot.github.io/blog/2026-07-24-build-systems.html](https://civboot.github.io/blog/2026-07-24-build-systems.html)

生成摘要时出错

---

## 30. 3GPP Version 19

**原文标题**: 3GPP Version 19

**原文链接**: [https://www.3gpp.org/specifications-technologies/releases/release-19](https://www.3gpp.org/specifications-technologies/releases/release-19)

生成摘要时出错

---

## 31. Buz – A fork of Bun using modern Zig, with sub-1s incremental builds

**原文标题**: Buz – A fork of Bun using modern Zig, with sub-1s incremental builds

**原文链接**: [https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891](https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891)

生成摘要时出错

---

## 32. Cloning Mifare Classic Cards via Proxmark3

**原文标题**: Cloning Mifare Classic Cards via Proxmark3

**原文链接**: [https://blog.muffn.io/posts/cloning-mifare-cards-proxmark3/](https://blog.muffn.io/posts/cloning-mifare-cards-proxmark3/)

生成摘要时出错

---

## 33. Claude Cookbook

**原文标题**: Claude Cookbook

**原文链接**: [https://platform.claude.com/cookbook/](https://platform.claude.com/cookbook/)

生成摘要时出错

---

## 34. Co-Opting Linux Processes for High-Performance Network Simulation (2022)

**原文标题**: Co-Opting Linux Processes for High-Performance Network Simulation (2022)

**原文链接**: [https://www.usenix.org/conference/atc22/presentation/jansen](https://www.usenix.org/conference/atc22/presentation/jansen)

生成摘要时出错

---

## 35. PySINDy – A package for the sparse identification of nonlinear dynamical systems

**原文标题**: PySINDy – A package for the sparse identification of nonlinear dynamical systems

**原文链接**: [https://github.com/dynamicslab/pysindy](https://github.com/dynamicslab/pysindy)

生成摘要时出错

---

## 36. The small, real, original web

**原文标题**: The small, real, original web

**原文链接**: [https://spacetimetech.wordpress.com/2026/07/19/the-small-real-original-web/](https://spacetimetech.wordpress.com/2026/07/19/the-small-real-original-web/)

生成摘要时出错

---

## 37. Writing a Debugger from Scratch

**原文标题**: Writing a Debugger from Scratch

**原文链接**: [https://www.timdbg.com/posts/writing-a-debugger-from-scratch-part-1/](https://www.timdbg.com/posts/writing-a-debugger-from-scratch-part-1/)

生成摘要时出错

---

## 38. Pizauth: An OAuth2 token requester daemon

**原文标题**: Pizauth: An OAuth2 token requester daemon

**原文链接**: [https://github.com/ltratt/pizauth/](https://github.com/ltratt/pizauth/)

生成摘要时出错

---

## 39. What's new in Claude Opus 5

**原文标题**: What's new in Claude Opus 5

**原文链接**: [https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)

生成摘要时出错

---

## 40. Asked Codex to redesign a page; it pushed my repo to OpenAI infra

**原文标题**: Asked Codex to redesign a page; it pushed my repo to OpenAI infra

**原文链接**: [https://bhanu.io/blog/codex-pushed-my-private-repo-to-an-openai-server](https://bhanu.io/blog/codex-pushed-my-private-repo-to-an-openai-server)

生成摘要时出错

---

## 41. The IBM PC, Part 1: Arrival

**原文标题**: The IBM PC, Part 1: Arrival

**原文链接**: [https://technicshistory.com/2026/07/24/the-ibm-pc-part-1-arrival/](https://technicshistory.com/2026/07/24/the-ibm-pc-part-1-arrival/)

生成摘要时出错

---

## 42. Mag Computer: A Mag History of RAM (1960–2025)

**原文标题**: Mag Computer: A Mag History of RAM (1960–2025)

**原文链接**: [https://magworld.pw/episodes/computer/](https://magworld.pw/episodes/computer/)

生成摘要时出错

---

## 43. Game of Trees – Git-based version control from OpenBSD folks

**原文标题**: Game of Trees – Git-based version control from OpenBSD folks

**原文链接**: [https://www.gameoftrees.org/](https://www.gameoftrees.org/)

生成摘要时出错

---

## 44. So bright the vision (1956) a story about machines writing instead of humans [pdf]

**原文标题**: So bright the vision (1956) a story about machines writing instead of humans [pdf]

**原文链接**: [https://s3.us-west-1.wasabisys.com/luminist/EB/S/Simak%20-%20So%20Bright%20the%20Vision.pdf](https://s3.us-west-1.wasabisys.com/luminist/EB/S/Simak%20-%20So%20Bright%20the%20Vision.pdf)

生成摘要时出错

---

## 45. Writing by hand is good for your brain

**原文标题**: Writing by hand is good for your brain

**原文链接**: [https://nealstephenson.substack.com/p/writing-by-hand-is-good-for-your](https://nealstephenson.substack.com/p/writing-by-hand-is-good-for-your)

生成摘要时出错

---

## 46. Interview with a Maintainer

**原文标题**: Interview with a Maintainer

**原文链接**: [https://nesbitt.io/2026/07/24/interview-with-a-maintainer.html](https://nesbitt.io/2026/07/24/interview-with-a-maintainer.html)

生成摘要时出错

---

## 47. Preventing line breaks in <code> elements

**原文标题**: Preventing line breaks in <code> elements

**原文链接**: [https://alexwlchan.net/2026/non-breaking-code/](https://alexwlchan.net/2026/non-breaking-code/)

生成摘要时出错

---

## 48. PCI DSS DMARC Requirement: What Section 5.4.1 Requires

**原文标题**: PCI DSS DMARC Requirement: What Section 5.4.1 Requires

**原文链接**: [https://dmarcguard.io/blog/pci-dss/](https://dmarcguard.io/blog/pci-dss/)

生成摘要时出错

---

## 49. I regret migrating to Codeberg

**原文标题**: I regret migrating to Codeberg

**原文链接**: [https://xn--gckvb8fzb.com/i-regret-migrating-to-codeberg/](https://xn--gckvb8fzb.com/i-regret-migrating-to-codeberg/)

生成摘要时出错

---

## 50. AMD's Instinct MI455X: Aiming for the Sun

**原文标题**: AMD's Instinct MI455X: Aiming for the Sun

**原文链接**: [https://chipsandcheese.com/p/amds-instinct-mi455x-aiming-for-the](https://chipsandcheese.com/p/amds-instinct-mi455x-aiming-for-the)

生成摘要时出错

---

## 51. Startup founders urge U.S. government not to shut off Chinese open weight AI

**原文标题**: Startup founders urge U.S. government not to shut off Chinese open weight AI

**原文链接**: [https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

生成摘要时出错

---

## 52. Kaizen #4: Overhauled Homelab

**原文标题**: Kaizen #4: Overhauled Homelab

**原文链接**: [https://timharek.no/blog/kaizen-4/](https://timharek.no/blog/kaizen-4/)

生成摘要时出错

---

## 53. The White House Report on Revitalizing U.S. Scientific Leadership

**原文标题**: The White House Report on Revitalizing U.S. Scientific Leadership

**原文链接**: [https://lemire.me/blog/2026/07/22/from-institutions-to-individuals-the-white-house-report-on-revitalizing-u-s-scientific-leadership/](https://lemire.me/blog/2026/07/22/from-institutions-to-individuals-the-white-house-report-on-revitalizing-u-s-scientific-leadership/)

生成摘要时出错

---

## 54. Zuckerberg's AI optimism blitz using nostalgia to sell AI future amid backlash

**原文标题**: Zuckerberg's AI optimism blitz using nostalgia to sell AI future amid backlash

**原文链接**: [https://fortune.com/2026/07/23/zuckerberg-ai-ad-optimism-backlash/](https://fortune.com/2026/07/23/zuckerberg-ai-ad-optimism-backlash/)

生成摘要时出错

---

## 55. PlayStation Network outage leaves players dreading all-digital future

**原文标题**: PlayStation Network outage leaves players dreading all-digital future

**原文链接**: [https://www.polygon.com/playstation-network-down-psn-outage-digital-games-backlash/](https://www.polygon.com/playstation-network-down-psn-outage-digital-games-backlash/)

生成摘要时出错

---

## 56. Computational chemistry, Locally? My rant on SSH

**原文标题**: Computational chemistry, Locally? My rant on SSH

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/computational-chemistry-locally](https://chillphysicsenjoyer.substack.com/p/computational-chemistry-locally)

生成摘要时出错

---

## 57. Why Sony can't bring back its classic Walkman models

**原文标题**: Why Sony can't bring back its classic Walkman models

**原文链接**: [https://obsoletesony.substack.com/p/why-sony-cant-bring-back-classic-walkman](https://obsoletesony.substack.com/p/why-sony-cant-bring-back-classic-walkman)

生成摘要时出错

---

## 58. The Book Prize Index

**原文标题**: The Book Prize Index

**原文链接**: [https://book-prize-index.vercel.app](https://book-prize-index.vercel.app)

生成摘要时出错

---

## 59. Tangleflow: Converts GitHub Actions workflows to tangled workflows and back

**原文标题**: Tangleflow: Converts GitHub Actions workflows to tangled workflows and back

**原文链接**: [https://github.com/43081j/tangleflow](https://github.com/43081j/tangleflow)

生成摘要时出错

---

## 60. What else do people draw on gradient.horse?

**原文标题**: What else do people draw on gradient.horse?

**原文链接**: [https://rybakov.com/blog/what_else_do_people_draw_on_gradient-copy.horse/](https://rybakov.com/blog/what_else_do_people_draw_on_gradient-copy.horse/)

生成摘要时出错

---

## 61. Hetzner is working on LLM Inference

**原文标题**: Hetzner is working on LLM Inference

**原文链接**: [https://sliplane.io/blog/hetzner-inference](https://sliplane.io/blog/hetzner-inference)

生成摘要时出错

---

## 62. Nothing works and everyone is euphoric

**原文标题**: Nothing works and everyone is euphoric

**原文链接**: [https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/)

生成摘要时出错

---

## 63. Show HN: X402vps – Docker containers for AI agents, paid per hour with USDC

**原文标题**: Show HN: X402vps – Docker containers for AI agents, paid per hour with USDC

**原文链接**: [https://x402vps.com](https://x402vps.com)

生成摘要时出错

---

## 64. Fields Medals 2026

**原文标题**: Fields Medals 2026

**原文链接**: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026)

生成摘要时出错

---

## 65. Micro-SaaS Is Dead. Service With A Software Replaces It

**原文标题**: Micro-SaaS Is Dead. Service With A Software Replaces It

**原文链接**: [https://adriengonin.com/writing/service-with-a-software/](https://adriengonin.com/writing/service-with-a-software/)

生成摘要时出错

---

## 66. Tesla swapped a solar owner's lease contract for the Book of Enoch

**原文标题**: Tesla swapped a solar owner's lease contract for the Book of Enoch

**原文链接**: [https://electrek.co/2026/07/23/tesla-solar-lease-contract-book-of-enoch/](https://electrek.co/2026/07/23/tesla-solar-lease-contract-book-of-enoch/)

生成摘要时出错

---

## 67. Show HN: Palmier Pro – Open-source macOS video editor built for AI

**原文标题**: Show HN: Palmier Pro – Open-source macOS video editor built for AI

**原文链接**: [https://github.com/palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro)

生成摘要时出错

---

## 68. The day Steve Jobs dissed me in a keynote (2010)

**原文标题**: The day Steve Jobs dissed me in a keynote (2010)

**原文链接**: [https://sive.rs/itunes](https://sive.rs/itunes)

生成摘要时出错

---

## 69. The Beam Engine

**原文标题**: The Beam Engine

**原文链接**: [https://glinscott.github.io/beam-engine/](https://glinscott.github.io/beam-engine/)

生成摘要时出错

---

## 70. The loudest person wins architecture discussions

**原文标题**: The loudest person wins architecture discussions

**原文链接**: [https://thehardparts.dev/red-flags/the-loudest-person-wins-architecture-discussions](https://thehardparts.dev/red-flags/the-loudest-person-wins-architecture-discussions)

生成摘要时出错

---

## 71. 98.css

**原文标题**: 98.css

**原文链接**: [https://jdan.github.io/98.css/#status-bar](https://jdan.github.io/98.css/#status-bar)

生成摘要时出错

---

## 72. 80k people flee as wildfires spread in France and Spain

**原文标题**: 80k people flee as wildfires spread in France and Spain

**原文链接**: [https://www.theguardian.com/world/2026/jul/24/france-evacuation-cap-ferret-peninsula-wildfire](https://www.theguardian.com/world/2026/jul/24/france-evacuation-cap-ferret-peninsula-wildfire)

生成摘要时出错

---

## 73. IRGC Claims It Destroyed Amazon's Bahrain Data Center

**原文标题**: IRGC Claims It Destroyed Amazon's Bahrain Data Center

**原文链接**: [https://houseofsaud.com/irgc-claims-destroyed-amazon-bahrain-data-center/](https://houseofsaud.com/irgc-claims-destroyed-amazon-bahrain-data-center/)

生成摘要时出错

---

## 74. Solod 0.2: Networking, new targets, friendlier interop

**原文标题**: Solod 0.2: Networking, new targets, friendlier interop

**原文链接**: [https://antonz.org/solod-0.2/](https://antonz.org/solod-0.2/)

生成摘要时出错

---

## 75. Andrew Kelley: Don't Take the Black Pill

**原文标题**: Andrew Kelley: Don't Take the Black Pill

**原文链接**: [https://www.youtube.com/watch?v=zLZwpH5lCD4](https://www.youtube.com/watch?v=zLZwpH5lCD4)

生成摘要时出错

---

## 76. Programming language file extensions that match ISO 3166-1 alpha-2 country code

**原文标题**: Programming language file extensions that match ISO 3166-1 alpha-2 country code

**原文链接**: [https://www.bruh.ltd/blog/programming-language-file-extensions-that-match-an-iso-3166-1-alpha-2-country-code/](https://www.bruh.ltd/blog/programming-language-file-extensions-that-match-an-iso-3166-1-alpha-2-country-code/)

生成摘要时出错

---

## 77. Cross-stitch prep for math nerds

**原文标题**: Cross-stitch prep for math nerds

**原文链接**: [https://posh.wiki/blog/2026-07-20-hoop-sizing/](https://posh.wiki/blog/2026-07-20-hoop-sizing/)

生成摘要时出错

---

## 78. I Tried Building a Real App with AI. It Took a Year

**原文标题**: I Tried Building a Real App with AI. It Took a Year

**原文链接**: [https://www.alexhyett.com/videos/tried-building-app-with-ai-it-took-a-year/](https://www.alexhyett.com/videos/tried-building-app-with-ai-it-took-a-year/)

生成摘要时出错

---

## 79. The arguments against open source AI are bad

**原文标题**: The arguments against open source AI are bad

**原文链接**: [https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/)

生成摘要时出错

---

## 80. Quickly rewrite Git repository history

**原文标题**: Quickly rewrite Git repository history

**原文链接**: [https://github.com/newren/git-filter-repo](https://github.com/newren/git-filter-repo)

生成摘要时出错

---

## 81. Mourning Dan Williams

**原文标题**: Mourning Dan Williams

**原文链接**: [https://lwn.net/Articles/1084545/](https://lwn.net/Articles/1084545/)

生成摘要时出错

---

## 82. Show HN: OneCLI – OSS credential gateway that keeps secrets out of AI agents

**原文标题**: Show HN: OneCLI – OSS credential gateway that keeps secrets out of AI agents

**原文链接**: [https://github.com/onecli/onecli](https://github.com/onecli/onecli)

生成摘要时出错

---

## 83. West Virginia paid digital nomads to move there during Covid. Many are staying

**原文标题**: West Virginia paid digital nomads to move there during Covid. Many are staying

**原文链接**: [https://www.npr.org/2026/07/24/nx-s1-5869402/remote-work-west-virginia-cash-incentive](https://www.npr.org/2026/07/24/nx-s1-5869402/remote-work-west-virginia-cash-incentive)

生成摘要时出错

---

## 84. Show HN: Audio Player with "Binaural Beats" tuned to the same key as your music

**原文标题**: Show HN: Audio Player with "Binaural Beats" tuned to the same key as your music

**原文链接**: [https://github.com/henrygabriels/binaural-studio](https://github.com/henrygabriels/binaural-studio)

生成摘要时出错

---

## 85. A solid-state “atomic channel” for separating rare earth elements

**原文标题**: A solid-state “atomic channel” for separating rare earth elements

**原文链接**: [https://pme.uchicago.edu/news-events/news/cleaner-route-purifying-rare-earth-elements](https://pme.uchicago.edu/news-events/news/cleaner-route-purifying-rare-earth-elements)

生成摘要时出错

---

## 86. Jensen Huang on why open models matter

**原文标题**: Jensen Huang on why open models matter

**原文链接**: [https://xcancel.com/JensenHuang/status/2080643682408321103?s=42](https://xcancel.com/JensenHuang/status/2080643682408321103?s=42)

生成摘要时出错

---

## 87. Japanese AI Robots Used to Replicate Skilled Confectioners' Abilities

**原文标题**: Japanese AI Robots Used to Replicate Skilled Confectioners' Abilities

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20260719-338181/](https://japannews.yomiuri.co.jp/science-nature/technology/20260719-338181/)

生成摘要时出错

---

## 88. 80k people flee as wildfires spread in France and Spain

**原文标题**: 80k people flee as wildfires spread in France and Spain

**原文链接**: [https://www.theguardian.com/world/2026/jul/24/france-evacuation-cap-ferret-peninsula-wildfire](https://www.theguardian.com/world/2026/jul/24/france-evacuation-cap-ferret-peninsula-wildfire)

生成摘要时出错

---

## 89. Building on ATProto

**原文标题**: Building on ATProto

**原文链接**: [https://lukekanies.com/writing/building-on-atproto/](https://lukekanies.com/writing/building-on-atproto/)

生成摘要时出错

---

## 90. Why Software Factories Fail (or: harness engineering is not enough)

**原文标题**: Why Software Factories Fail (or: harness engineering is not enough)

**原文链接**: [https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md)

生成摘要时出错

---

## 91. Patreon laying off 20% of staff

**原文标题**: Patreon laying off 20% of staff

**原文链接**: [https://www.patreon.com/jackconte/posts/painful-update-164628951](https://www.patreon.com/jackconte/posts/painful-update-164628951)

生成摘要时出错

---

## 92. What happened to TheNumbers.com

**原文标题**: What happened to TheNumbers.com

**原文链接**: [https://stephenfollows.com/p/what-just-happened-to-thenumberscom-should-worry-us-all](https://stephenfollows.com/p/what-just-happened-to-thenumberscom-should-worry-us-all)

生成摘要时出错

---

## 93. Modula-3 History Collection on Computer History Museum

**原文标题**: Modula-3 History Collection on Computer History Museum

**原文链接**: [https://softwarepreservation.computerhistory.org/modula3/](https://softwarepreservation.computerhistory.org/modula3/)

生成摘要时出错

---

## 94. TQuel Paper: Implementing Temporal Operators in Postgres

**原文标题**: TQuel Paper: Implementing Temporal Operators in Postgres

**原文链接**: [https://illuminatedcomputing.com/posts/2026/07/tquel-paper/](https://illuminatedcomputing.com/posts/2026/07/tquel-paper/)

生成摘要时出错

---

## 95. Emacs Is a Lispboard

**原文标题**: Emacs Is a Lispboard

**原文链接**: [https://en.andros.dev/blog/06bfd107/emacs-is-a-lispboard/](https://en.andros.dev/blog/06bfd107/emacs-is-a-lispboard/)

生成摘要时出错

---

## 96. The story behind APC-2

**原文标题**: The story behind APC-2

**原文链接**: [https://teenage.engineering/now](https://teenage.engineering/now)

生成摘要时出错

---

## 97. Stinkpot: SQLite-Backed Shell History

**原文标题**: Stinkpot: SQLite-Backed Shell History

**原文链接**: [https://tangled.org/oppi.li/stinkpot](https://tangled.org/oppi.li/stinkpot)

生成摘要时出错

---

## 98. Show HN: Claude-thermos keeps your Claude session warm for you

**原文标题**: Show HN: Claude-thermos keeps your Claude session warm for you

**原文链接**: [https://github.com/izeigerman/claude-thermos](https://github.com/izeigerman/claude-thermos)

生成摘要时出错

---

## 99. Meta Garbage Collection: Using OCaml's GC to GC Rust

**原文标题**: Meta Garbage Collection: Using OCaml's GC to GC Rust

**原文链接**: [https://soteria-tools.com/blog/meta-garbage-collection](https://soteria-tools.com/blog/meta-garbage-collection)

生成摘要时出错

---

## 100. Jacobian Conjecture Refutation Reveals a Structural Limit of AI Interpretability

**原文标题**: Jacobian Conjecture Refutation Reveals a Structural Limit of AI Interpretability

**原文链接**: [https://ctolunchnyc.substack.com/p/the-lost-weekend](https://ctolunchnyc.substack.com/p/the-lost-weekend)

生成摘要时出错

---

