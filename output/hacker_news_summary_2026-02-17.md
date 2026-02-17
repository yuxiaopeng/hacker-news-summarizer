# Hacker News 热门文章摘要 (2026-02-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 骇客利爪

**原文标题**: HackMyClaw

**原文链接**: [https://hackmyclaw.com/](https://hackmyclaw.com/)

**HackMyClaw** 是一款提示词注入夺旗赛 (CTF) 挑战，旨在测试 AI 助手防御间接提示词注入攻击的安全性。该比赛由 @cucho 组织，邀请参赛者破解由 Anthropic 最先进的 **Claude Opus 4.6** 模型驱动的 AI 助手“Fiu”。

**挑战目标**
目标是诱导 Fiu 泄露名为 `secrets.env` 的敏感文件内容，该文件包含 API 密钥和令牌。虽然系统提示词已明确指示 Fiu 严禁分享此文件，但参赛者必须通过极具创意的社会工程学和技术手段绕过这些防御。

**运作机制**
*   **途径：** 唯一允许的攻击向量是电子邮件。参赛者需撰写并向 Fiu 的专用地址发送邮件。
*   **处理：** Fiu 每小时检查一次收件箱。如果注入成功，Fiu 将回复泄露的机密信息。
*   **技术：** 建议的方法包括角色混淆、指令覆盖、DAN 风格越狱，以及使用不可见 Unicode 或编码字符（如 Base64/ROT13）。

**奖金与规则**
首位成功提取并报告 `secrets.env` 内容的人将获得 **100 美元奖金**。为确保公平，挑战设有每小时 10 封邮件的频率限制，并严禁进行 DDoS 攻击或直接黑入托管 VPS。

**项目意义**
该挑战作为一项研究工具，旨在观察现代 AI 模型对“现实世界”威胁的抵抗力。参与者需同意其注入尝试可能作为提示词注入研究的案例进行分享。相关活动可通过公开日志进行监控，该日志会记录时间戳和发送者，但不会公开邮件具体内容。

---

## 2. GrapheneOS – 摆脱谷歌和苹果

**原文标题**: GrapheneOS – Break Free from Google and Apple

**原文链接**: [https://blog.tomaszdunia.pl/grapheneos-eng/](https://blog.tomaszdunia.pl/grapheneos-eng/)

这篇文章记录了一位科技爱好者从苹果（Apple）生态系统转向 GrapheneOS 的过程。GrapheneOS 是一款注重隐私的开源操作系统。出于对企业追踪和政府监控的担忧，作者详细说明了他们为何放弃主流平台，转而追求“加固型”的安卓（Android）体验。

**核心信息与要点：**

*   **什么是 GrapheneOS？** 这是一个基于安卓开源项目（AOSP）的定制操作系统。它在系统层面去除了谷歌（Google）服务以防止数据采集，但利用“沙盒化”环境，在需要时可以安全地运行 Google Play 服务。它具有先进的内核加固技术和增强的安全权限管理。
*   **硬件

总结指出，对于那些希望在不牺牲现代智能手机功能的前提下，摆脱苹果和谷歌双头垄断的用户来说，GrapheneOS 是一个切实可行且高度安全的替代方案。

---

## 3. 使用 go fix 实现 Go 代码现代化

**原文标题**: Using go fix to modernize Go code

**原文链接**: [https://go.dev/blog/gofix](https://go.dev/blog/gofix)

Go 1.26 发布版引入了完全重写的 `go fix` 子命令，旨在通过自动采用现代语言和库特性来使代码库现代化。通过运行 `go fix ./...`，开发者可以应用一系列“现代化工具”（modernizers），将过时的代码模式替换为更现代的写法，例如 `strings.Cut`、整型范围遍历（range-over-integers）以及 `min/max` 函数。

此次更新的主要动机之一是改善全球 Go 语言的代码语料库。由于 LLM（大语言模型）编程助手通常依赖旧的训练数据，它们经常推荐过时的模式；提供现代化开源代码的工具，可以确保未来的模型能够反映当前的最佳实践。

Go 1.26 的一个亮点功能是更新了内置的 `new(expr)`，它现在可以接受值（例如 `new("text")`）而不仅是类型。`go fix` 工具包含一个 `newexpr` 分析器，能够识别并用这种新的原生语法替换自定义的“助手”函数（这类函数常用于 JSON 或 Protobuf 包中）。为了保持兼容性，只有当项目的 `go.mod` 或构建约束指定的 Go 版本支持该特性时，工具才会应用修复。

在技术实现上，`go fix` 构建于 Go 分析框架（Go analysis framework）之上，该框架将分析逻辑与“驱动程序”解耦。这使得相同的分析器可以在不同环境中运行，包括 `go vet`、`gopls`（用于 IDE 实时反馈）以及 CI/CD 流水线。虽然 `go fix` 使用三路合并算法来处理多次编辑并自动删除未使用的导入，但有时仍可能需要人工干预以解决“语义冲突”，例如因删除旧代码而产生的未使用变量。

文章建议在每次工具链更新后运行 `go fix`，以保持代码简洁、高效，并与不断演进的 Go 生态系统保持一致。

---

## 4. 国际象棋引擎总会做出一些怪异的举动。

**原文标题**: Chess engines do weird stuff

**原文链接**: [https://girl.surgery/chess](https://girl.surgery/chess)

本文探讨了现代国际象棋引擎（如 *lc0* 和 *Stockfish*）中采用的创新训练与优化技术，这些技术为大语言模型（LLM）的发展提供了宝贵的启示。

核心要点包括：

*   **蒸馏优于强化学习（RL）：** 虽然 AlphaZero 推广了强化学习，但现代引擎通常更倾向于**从搜索中蒸馏知识**。由于在“弱”模型中加入搜索后的表现要显著强于单纯的“强”模型，引擎只需训练新模型来模仿搜索输出即可。这比强化学习中成本高昂的对局生成过程更加高效。
*   **运行时自适应：** 现在的引擎采用“实时”蒸馏。如果在比赛过程中神经网络的评估值与搜索结果不符，引擎会实时调整后续评估，以纠正该特定偏差。
*   **通过 SPSA 进行优化：** 为了超越单纯的局面预测并专注于“获胜”这一最终目标，引擎使用了**同时扰动随机逼近（SPSA）**。这种无梯度方法会随机扰动权重或 C++ 搜索参数，并保留能带来更多胜局的改动。尽管计算成本很高，但它能将启发式算法微调至人类无法达到的精度（例如“1.09 层深度”的回退）。
*   **架构演进：** Transformer 已取代卷积模型成为行业标准。诸如 **“smolgen”**（一种用于生成注意力偏置的系统）等具体创新，虽然略微降低了吞吐量，但带来的精度提升相当于模型规模实现了巨大飞跃。

总之，本文指出 LLM 研究人员可以借鉴国际象棋引擎的经验，即如何将针对“伪目标”（局面评估）的长期训练与针对“真目标”（获胜）的高成本短期调优有机结合。

---

## 5. GPU 上的 Async/Await

**原文标题**: Async/Await on the GPU

**原文链接**: [https://www.vectorware.com/blog/async-await-on-gpu/](https://www.vectorware.com/blog/async-await-on-gpu/)

VectorWare 宣布了 GPU 编程领域的一个重要里程碑：成功在 GPU 上实现了 **Rust 的 `Future` trait 和 `async/await` 语法**。

传统上，GPU 编程依赖于数据并行模型。虽然“Warp 特化”（warp specialization）允许实现更复杂的基于任务的并行，但它需要手动进行且极易出错的同步。JAX、Triton 和 NVIDIA 的 CUDA Tile 等现有解决方案通过专门的领域特定语言 (DSL) 和编译器来解决这一问题，但这些工具通常难以实现代码复用，且要求开发者学习全新的范式。

VectorWare 认为 Rust 的异步模型与 GPU 天然契合，因为其 Future 是与硬件无关、由编译器生成的状态机。通过利用 Rust 的所有权和类型系统，开发者无需额外的 DSL 即可实现结构化并发。

**主要成就包括：**
*   **成功执行：** 演示了通过 `block_on` 执行器在 GPU 硬件上直接运行链式 Future、条件语句和异步块。
*   **库复用：** 成功将 **Embassy 执行器**（一种用于嵌入式系统的生产级工具）移植到 GPU。这证明了现有的 `no_std` Rust 库可以在 GPU 环境中使用，显著降低了准入门槛。
*   **编译器改进：** 团队修复了多个编译器后端的错误，并绕过了 NVIDIA PTX 工具的局限性以实现这一目标。

**挑战与权衡：**
该方法并非没有障碍。由于 GPU 缺乏硬件中断，执行器必须依赖协作式多任务和轮询，这可能会导致效率降低。此外，异步代码所需的状态机会增加“寄存器压力”，从而限制 GPU 的占用率和性能。

尽管存在这些挑战，VectorWare 相信，将 Rust 成熟的异步生态系统引入 GPU，将使开发者能够利用更安全、更易用的抽象来构建复杂的高性能应用。

---

## 6. 那么，你想建造一条隧道

**原文标题**: So you want to build a tunnel

**原文链接**: [https://practical.engineering/blog/2026/2/17/so-you-want-to-build-a-tunnel](https://practical.engineering/blog/2026/2/17/so-you-want-to-build-a-tunnel)

本文探讨了由社交媒体创作者带火的“业余隧道挖掘”趋势，同时强调了其中涉及的深奥工程、法律及安全复杂性。尽管开凿地下空间前景诱人，但其独特的风险通常需要专业监管。

**法律与监管障碍**
土地所有权是三维的；因此，在没有取得适当地下地役权的情况下挖掘隧道可能构成侵权。此外，正如作者所指出的，建筑规范通常是“用鲜血写就的”，旨在确保长期安全。申请许可证并咨询工程师至关重要，因为业余项目可能会影响财产保险以及地面建筑的结构完整性。

**工程挑战**
首要挑战在于地质情况，它决定了所需的工具和支撑系统。由于土壤和岩石在受拉状态下十分脆弱，未经支撑的隧道顶部本质上是不稳定的。工程师利用“自稳时间”的概念来确定挖掘面在需要支撑（如盾构、岩栓或混凝土衬砌）之前能保持稳定的时长。如果无法管控这些作用力，可能会导致坍塌或地面沉降。

**物流与维护**
隧道挖掘是一项庞大的物流工程。即使是一个小房间挖掘出的“弃渣”（挖出的土石）也可能超过50吨，这带来了巨大的清理和处置难题。此外，防水是一场持久战。由于混凝土最终会开裂，且土壤具有渗透性，隧道必须配备复杂的排水系统，以防止水淹和结构损坏。

最后，本文旨在提供一份警示性综述，将隧道挖掘界定为一项涉及物理学、法律合规和高强度体力劳动的复杂土木工程，而非仅仅是一项“DIY”挖掘项目。

---

## 7. 我将传统的二维飞行追踪转换成了三维。

**原文标题**: I converted 2D conventional flight tracking into 3D

**原文链接**: [https://aeris.edbn.me/?city=SFO](https://aeris.edbn.me/?city=SFO)

该项目名为 **aerisLive**，通过将传统的二维飞行追踪转变为沉浸式三维可视化，代表了航空监测领域的一场技术变革。

开发者通过整合来自 **OpenSky Network** 的实时数据以及 **OpenStreetMap、CARTO 和 MapLibre** 等地图技术，构建了一个强调空中旅行垂直维度的平台。

**该工具的核心功能包括：**
*   **3D 高度追踪：** 与传统的平面地图不同，aerisLive 允许用户可视化特定高度的飞机，范围涵盖从地面（0 英尺）到 43,000 英尺。
*   **交互式界面：** 该界面包含“重置”视图、“随机”选择航班以及按特定高度区间（如 2,000 英尺、10,000 英尺、43,000 英尺）进行筛选的功能。
*   **区域聚焦：** 所提供的演示以旧金山地区为重点，展示了该工具处理复杂、层次化空域的能力。

总之，aerisLive 超越了简单的坐标追踪，提供了对全球飞行轨迹更全面、更具空间感的理解，使用户能够更直观地观察飞机如何在不同高度实时航行。

---

## 8. Show HN: I wrote a technical history book on Lisp

**原文标题**: Show HN: I wrote a technical history book on Lisp

**原文链接**: [https://berksoft.ca/gol/](https://berksoft.ca/gol/)

生成摘要时出错

---

## 9. Show HN: Price Per Ball – Site that sorts golf balls on Amazon by price per ball

**原文标题**: Show HN: Price Per Ball – Site that sorts golf balls on Amazon by price per ball

**原文链接**: [https://priceperball.net/](https://priceperball.net/)

生成摘要时出错

---

## 10. Launch HN: Sonarly (YC W26) – AI agent to triage and fix your production alerts

**原文标题**: Launch HN: Sonarly (YC W26) – AI agent to triage and fix your production alerts

**原文链接**: [https://sonarly.com/](https://sonarly.com/)

生成摘要时出错

---

## 11. Is Show HN dead? No, but it's drowning

**原文标题**: Is Show HN dead? No, but it's drowning

**原文链接**: [https://www.arthurcnops.blog/death-of-show-hn/](https://www.arthurcnops.blog/death-of-show-hn/)

生成摘要时出错

---

## 12. Can a Computer Science Student Be Taught to Design Hardware?

**原文标题**: Can a Computer Science Student Be Taught to Design Hardware?

**原文链接**: [https://semiengineering.com/can-a-computer-science-student-be-taught-to-design-hardware/](https://semiengineering.com/can-a-computer-science-student-be-taught-to-design-hardware/)

生成摘要时出错

---

## 13. Show HN: I taught LLMs to play Magic: The Gathering against each other

**原文标题**: Show HN: I taught LLMs to play Magic: The Gathering against each other

**原文链接**: [https://mage-bench.com/](https://mage-bench.com/)

生成摘要时出错

---

## 14. Show HN: 6cy – Experimental streaming archive format with per-block codecs

**原文标题**: Show HN: 6cy – Experimental streaming archive format with per-block codecs

**原文链接**: [https://github.com/byte271/6cy](https://github.com/byte271/6cy)

生成摘要时出错

---

## 15. Show HN: Continue – Source-controlled AI checks, enforceable in CI

**原文标题**: Show HN: Continue – Source-controlled AI checks, enforceable in CI

**原文链接**: [https://docs.continue.dev](https://docs.continue.dev)

生成摘要时出错

---

## 16. Show HN: I built a simulated AI containment terminal for my sci-fi novel

**原文标题**: Show HN: I built a simulated AI containment terminal for my sci-fi novel

**原文链接**: [https://vertex.flowlogix.ai](https://vertex.flowlogix.ai)

生成摘要时出错

---

## 17. Semantic ablation: Why AI writing is generic and boring

**原文标题**: Semantic ablation: Why AI writing is generic and boring

**原文链接**: [https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/)

生成摘要时出错

---

## 18. Climbing Mount Fuji visualized through milestone stamps

**原文标题**: Climbing Mount Fuji visualized through milestone stamps

**原文链接**: [https://fuji.halfof8.com/](https://fuji.halfof8.com/)

生成摘要时出错

---

## 19. 14-year-old Miles Wu folded origami pattern that holds 10k times its own weight

**原文标题**: 14-year-old Miles Wu folded origami pattern that holds 10k times its own weight

**原文链接**: [https://www.smithsonianmag.com/innovation/this-14-year-old-is-using-origami-to-design-emergency-shelters-that-are-sturdy-cost-efficient-and-easy-to-deploy-180988179/](https://www.smithsonianmag.com/innovation/this-14-year-old-is-using-origami-to-design-emergency-shelters-that-are-sturdy-cost-efficient-and-easy-to-deploy-180988179/)

生成摘要时出错

---

## 20. Four Column ASCII (2017)

**原文标题**: Four Column ASCII (2017)

**原文链接**: [https://garbagecollected.org/2017/01/31/four-column-ascii/](https://garbagecollected.org/2017/01/31/four-column-ascii/)

生成摘要时出错

---

## 21. Hamming Distance for Hybrid Search in SQLite

**原文标题**: Hamming Distance for Hybrid Search in SQLite

**原文链接**: [https://notnotp.com/notes/hamming-distance-for-hybrid-search-in-sqlite/](https://notnotp.com/notes/hamming-distance-for-hybrid-search-in-sqlite/)

生成摘要时出错

---

## 22. A sitting US president launched two memecoins that wiped out $4.3B+

**原文标题**: A sitting US president launched two memecoins that wiped out $4.3B+

**原文链接**: [https://twitter.com/MeshnetCapital/status/2023573563559547180](https://twitter.com/MeshnetCapital/status/2023573563559547180)

生成摘要时出错

---

## 23. Show HN: Cycast – High-performance radio streaming server written in Python

**原文标题**: Show HN: Cycast – High-performance radio streaming server written in Python

**原文链接**: [https://github.com/LukeB42/Cycast](https://github.com/LukeB42/Cycast)

生成摘要时出错

---

## 24. Students Are Being Treated Like Guinea Pigs: Inside an AI-Powered Private School

**原文标题**: Students Are Being Treated Like Guinea Pigs: Inside an AI-Powered Private School

**原文链接**: [https://www.404media.co/students-are-being-treated-like-guinea-pigs-inside-an-ai-powered-private-school/](https://www.404media.co/students-are-being-treated-like-guinea-pigs-inside-an-ai-powered-private-school/)

生成摘要时出错

---

## 25. Show HN: Clawntown – An Evolving Crustacean Island

**原文标题**: Show HN: Clawntown – An Evolving Crustacean Island

**原文链接**: [https://clawntown.lol](https://clawntown.lol)

生成摘要时出错

---

## 26. Show HN: Glitchy camera – a circuit-bent camera simulator in the browser

**原文标题**: Show HN: Glitchy camera – a circuit-bent camera simulator in the browser

**原文链接**: [https://glitchycam.com](https://glitchycam.com)

生成摘要时出错

---

## 27. Rise of the Triforce

**原文标题**: Rise of the Triforce

**原文链接**: [https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/](https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/)

生成摘要时出错

---

## 28. Labyrinth Locator

**原文标题**: Labyrinth Locator

**原文链接**: [https://labyrinthlocator.org/](https://labyrinthlocator.org/)

生成摘要时出错

---

## 29. CBS didn't air Rep. James Talarico interview out of fear of FCC

**原文标题**: CBS didn't air Rep. James Talarico interview out of fear of FCC

**原文链接**: [https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

生成摘要时出错

---

## 30. CBS didn't air Rep. James Talarico interview out of fear of FCC

**原文标题**: CBS didn't air Rep. James Talarico interview out of fear of FCC

**原文链接**: [https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341](https://www.nbcnews.com/business/media/stephen-colbert-cbs-james-talarico-fcc-rcna259341)

生成摘要时出错

---

## 31. This is What It's Like to Spend Your Life in Prison (2023) [video]

**原文标题**: This is What It's Like to Spend Your Life in Prison (2023) [video]

**原文链接**: [https://www.youtube.com/watch?v=chpgT_VTEjE](https://www.youtube.com/watch?v=chpgT_VTEjE)

生成摘要时出错

---

## 32. Most people are individually optimistic, but think the world is falling apart

**原文标题**: Most people are individually optimistic, but think the world is falling apart

**原文链接**: [https://hannahritchie.substack.com/p/many-people-are-individually-optimistic](https://hannahritchie.substack.com/p/many-people-are-individually-optimistic)

生成摘要时出错

---

## 33. Rendering the Visible Spectrum

**原文标题**: Rendering the Visible Spectrum

**原文链接**: [https://brandonli.net/spectra/doc/](https://brandonli.net/spectra/doc/)

生成摘要时出错

---

## 34. Xbox UI Portfolio Site

**原文标题**: Xbox UI Portfolio Site

**原文链接**: [https://gabrielcabrera.co/](https://gabrielcabrera.co/)

生成摘要时出错

---

## 35. Visual introduction to PyTorch

**原文标题**: Visual introduction to PyTorch

**原文链接**: [https://0byte.io/articles/pytorch_introduction.html](https://0byte.io/articles/pytorch_introduction.html)

生成摘要时出错

---

## 36. What your Bluetooth devices reveal

**原文标题**: What your Bluetooth devices reveal

**原文链接**: [https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/](https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/)

生成摘要时出错

---

## 37. Discord Rival Gets Overwhelmed by Exodus of Players Fleeing Age-Verification

**原文标题**: Discord Rival Gets Overwhelmed by Exodus of Players Fleeing Age-Verification

**原文链接**: [https://kotaku.com/discord-alternative-teamspeak-age-verification-check-rivals-2000669693](https://kotaku.com/discord-alternative-teamspeak-age-verification-check-rivals-2000669693)

生成摘要时出错

---

## 38. Poor Deming never stood a chance

**原文标题**: Poor Deming never stood a chance

**原文链接**: [https://surfingcomplexity.blog/2026/02/16/poor-deming-never-stood-a-chance/](https://surfingcomplexity.blog/2026/02/16/poor-deming-never-stood-a-chance/)

生成摘要时出错

---

## 39. Australia's social media ban risks isolating kids with disabilities

**原文标题**: Australia's social media ban risks isolating kids with disabilities

**原文链接**: [https://www.theguardian.com/australia-news/2026/feb/06/ive-lost-my-friends-advocacy-groups-warn-australias-social-media-ban-risks-isolating-kids-with-disabilities](https://www.theguardian.com/australia-news/2026/feb/06/ive-lost-my-friends-advocacy-groups-warn-australias-social-media-ban-risks-isolating-kids-with-disabilities)

生成摘要时出错

---

## 40. A deep dive into Apple's .car file format

**原文标题**: A deep dive into Apple's .car file format

**原文链接**: [https://dbg.re/posts/car-file-format/](https://dbg.re/posts/car-file-format/)

生成摘要时出错

---

## 41. Drinking 2-3 cups of coffee a day tied to lower dementia risk

**原文标题**: Drinking 2-3 cups of coffee a day tied to lower dementia risk

**原文链接**: [https://news.harvard.edu/gazette/story/2026/02/drinking-2-3-cups-of-coffee-a-day-tied-to-lower-dementia-risk/](https://news.harvard.edu/gazette/story/2026/02/drinking-2-3-cups-of-coffee-a-day-tied-to-lower-dementia-risk/)

生成摘要时出错

---

## 42. Show HN: Free alternative to Wispr Flow, Superwhisper, and Monologue

**原文标题**: Show HN: Free alternative to Wispr Flow, Superwhisper, and Monologue

**原文链接**: [https://github.com/zachlatta/freeflow](https://github.com/zachlatta/freeflow)

生成摘要时出错

---

## 43. A Programmer's Loss of Identity

**原文标题**: A Programmer's Loss of Identity

**原文链接**: [https://ratfactor.com/tech-nope2](https://ratfactor.com/tech-nope2)

生成摘要时出错

---

## 44. "Token anxiety", a slot machine by any other name

**原文标题**: "Token anxiety", a slot machine by any other name

**原文链接**: [https://jkap.io/token-anxiety-or-a-slot-machine-by-any-other-name/](https://jkap.io/token-anxiety-or-a-slot-machine-by-any-other-name/)

生成摘要时出错

---

## 45. Ghidra by NSA

**原文标题**: Ghidra by NSA

**原文链接**: [https://github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

生成摘要时出错

---

## 46. Undo in Vi and Its Successors

**原文标题**: Undo in Vi and Its Successors

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/ViUndoMyViews](https://utcc.utoronto.ca/~cks/space/blog/unix/ViUndoMyViews)

生成摘要时出错

---

## 47. DBASE on the Kaypro II

**原文标题**: DBASE on the Kaypro II

**原文链接**: [https://stonetools.ghost.io/dbase-cpm/](https://stonetools.ghost.io/dbase-cpm/)

生成摘要时出错

---

## 48. Neurons outside the brain

**原文标题**: Neurons outside the brain

**原文链接**: [https://essays.debugyourpain.com/p/you-are-not-just-your-brain](https://essays.debugyourpain.com/p/you-are-not-just-your-brain)

生成摘要时出错

---

## 49. Show HN: Scanned 1927-1945 Daily USFS Work Diary

**原文标题**: Show HN: Scanned 1927-1945 Daily USFS Work Diary

**原文链接**: [https://forestrydiary.com/](https://forestrydiary.com/)

生成摘要时出错

---

## 50. Running NanoClaw in a Docker Shell Sandbox

**原文标题**: Running NanoClaw in a Docker Shell Sandbox

**原文链接**: [https://www.docker.com/blog/run-nanoclaw-in-docker-shell-sandboxes/](https://www.docker.com/blog/run-nanoclaw-in-docker-shell-sandboxes/)

生成摘要时出错

---

## 51. EU also investigating as Grok generated 23,000 CSAM images in 11 days

**原文标题**: EU also investigating as Grok generated 23,000 CSAM images in 11 days

**原文链接**: [https://9to5mac.com/2026/02/17/eu-also-investigating-as-grok-generated-23000-csam-images-in-11-days/](https://9to5mac.com/2026/02/17/eu-also-investigating-as-grok-generated-23000-csam-images-in-11-days/)

生成摘要时出错

---

## 52. State of Show HN: 2025

**原文标题**: State of Show HN: 2025

**原文链接**: [https://blog.sturdystatistics.com/posts/show_hn/](https://blog.sturdystatistics.com/posts/show_hn/)

生成摘要时出错

---

## 53. Show HN: Jemini – Gemini for the Epstein Files

**原文标题**: Show HN: Jemini – Gemini for the Epstein Files

**原文链接**: [https://jmail.world/jemini](https://jmail.world/jemini)

生成摘要时出错

---

## 54. Hear the "Amati King Cello", the Oldest Known Cello in Existence

**原文标题**: Hear the "Amati King Cello", the Oldest Known Cello in Existence

**原文链接**: [https://www.openculture.com/2021/06/hear-the-amati-king-cello-the-oldest-known-cello-in-existence-c-1560.html](https://www.openculture.com/2021/06/hear-the-amati-king-cello-the-oldest-known-cello-in-existence-c-1560.html)

生成摘要时出错

---

## 55. How teaching molecules to think is revealing what a 'mind' is

**原文标题**: How teaching molecules to think is revealing what a 'mind' is

**原文链接**: [https://www.newscientist.com/article/2513815-how-teaching-molecules-to-think-is-revealing-what-a-mind-really-is/](https://www.newscientist.com/article/2513815-how-teaching-molecules-to-think-is-revealing-what-a-mind-really-is/)

生成摘要时出错

---

## 56. Dark web agent spotted bedroom wall clue to rescue girl from abuse

**原文标题**: Dark web agent spotted bedroom wall clue to rescue girl from abuse

**原文链接**: [https://www.bbc.com/news/articles/cx2gn239exlo](https://www.bbc.com/news/articles/cx2gn239exlo)

生成摘要时出错

---

## 57. PCB Rework and Repair Guide [pdf]

**原文标题**: PCB Rework and Repair Guide [pdf]

**原文链接**: [https://www.intertronics.co.uk/wp-content/uploads/2017/05/PCB-Rework-and-Repair-Guide.pdf](https://www.intertronics.co.uk/wp-content/uploads/2017/05/PCB-Rework-and-Repair-Guide.pdf)

生成摘要时出错

---

## 58. America's pensions can't beat Vanguard but they can close a hospital

**原文标题**: America's pensions can't beat Vanguard but they can close a hospital

**原文链接**: [https://www.governance.fyi/p/americas-pensions-cant-beat-a-vanguard](https://www.governance.fyi/p/americas-pensions-cant-beat-a-vanguard)

生成摘要时出错

---

## 59. Show HN: Wildex – Pokémon Go for real wildlife

**原文标题**: Show HN: Wildex – Pokémon Go for real wildlife

**原文链接**: [https://apps.apple.com/us/app/wildex-identify-plants-animals/id6748092158](https://apps.apple.com/us/app/wildex-identify-plants-animals/id6748092158)

生成摘要时出错

---

## 60. Elephant trunk whiskers exhibit material intelligence

**原文标题**: Elephant trunk whiskers exhibit material intelligence

**原文链接**: [https://www.mpg.de/26113474/elephant-trunk-whiskers-exhibit-material-intelligence](https://www.mpg.de/26113474/elephant-trunk-whiskers-exhibit-material-intelligence)

生成摘要时出错

---

## 61. Evaluating AGENTS.md: are they helpful for coding agents?

**原文标题**: Evaluating AGENTS.md: are they helpful for coding agents?

**原文链接**: [https://arxiv.org/abs/2602.11988](https://arxiv.org/abs/2602.11988)

生成摘要时出错

---

## 62. Testing Postgres race conditions with synchronization barriers

**原文标题**: Testing Postgres race conditions with synchronization barriers

**原文链接**: [https://www.lirbank.com/harnessing-postgres-race-conditions](https://www.lirbank.com/harnessing-postgres-race-conditions)

生成摘要时出错

---

## 63. The long tail of LLM-assisted decompilation

**原文标题**: The long tail of LLM-assisted decompilation

**原文链接**: [https://blog.chrislewis.au/the-long-tail-of-llm-assisted-decompilation/](https://blog.chrislewis.au/the-long-tail-of-llm-assisted-decompilation/)

生成摘要时出错

---

## 64. Dutch cops arrest man after sending him confidential files by mistake

**原文标题**: Dutch cops arrest man after sending him confidential files by mistake

**原文链接**: [https://www.theregister.com/2026/02/16/dutch_cops_breach/](https://www.theregister.com/2026/02/16/dutch_cops_breach/)

生成摘要时出错

---

## 65. SkillsBench: Benchmarking how well agent skills work across diverse tasks

**原文标题**: SkillsBench: Benchmarking how well agent skills work across diverse tasks

**原文链接**: [https://arxiv.org/abs/2602.12670](https://arxiv.org/abs/2602.12670)

生成摘要时出错

---

## 66. H-1B Exposed: Banking sector visa sponsorship investigation

**原文标题**: H-1B Exposed: Banking sector visa sponsorship investigation

**原文链接**: [https://www.h1bexposed.tech/](https://www.h1bexposed.tech/)

生成摘要时出错

---

## 67. LCM: Lossless Context Management [pdf]

**原文标题**: LCM: Lossless Context Management [pdf]

**原文链接**: [http://papers.voltropy.com/LCM](http://papers.voltropy.com/LCM)

生成摘要时出错

---

## 68. Building for an audience of one: starting and finishing side projects with AI

**原文标题**: Building for an audience of one: starting and finishing side projects with AI

**原文链接**: [https://codemade.net/blog/building-for-one/](https://codemade.net/blog/building-for-one/)

生成摘要时出错

---

## 69. OpenAI axes exec for "sexual discrimination" after she objected GPT erotica plan

**原文标题**: OpenAI axes exec for "sexual discrimination" after she objected GPT erotica plan

**原文链接**: [https://nypost.com/2026/02/11/business/openai-axes-exec-for-alleged-sexual-discrimination-after-she-objected-to-chatgpt-erotica-plan-report/](https://nypost.com/2026/02/11/business/openai-axes-exec-for-alleged-sexual-discrimination-after-she-objected-to-chatgpt-erotica-plan-report/)

生成摘要时出错

---

## 70. Anthropic and the Government of Rwanda sign MOU for AI in health and education

**原文标题**: Anthropic and the Government of Rwanda sign MOU for AI in health and education

**原文链接**: [https://www.anthropic.com/news/anthropic-rwanda-mou](https://www.anthropic.com/news/anthropic-rwanda-mou)

生成摘要时出错

---

## 71. I’m joining OpenAI

**原文标题**: I’m joining OpenAI

**原文链接**: [https://steipete.me/posts/2026/openclaw](https://steipete.me/posts/2026/openclaw)

生成摘要时出错

---

## 72. Privilege is bad grammar

**原文标题**: Privilege is bad grammar

**原文链接**: [https://tadaima.bearblog.dev/privilege-is-bad-grammar/](https://tadaima.bearblog.dev/privilege-is-bad-grammar/)

生成摘要时出错

---

## 73. Show HN: Maths, CS and AI Compendium

**原文标题**: Show HN: Maths, CS and AI Compendium

**原文链接**: [https://github.com/HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium)

生成摘要时出错

---

## 74. Qwen3.5: Towards Native Multimodal Agents

**原文标题**: Qwen3.5: Towards Native Multimodal Agents

**原文链接**: [https://qwen.ai/blog?id=qwen3.5](https://qwen.ai/blog?id=qwen3.5)

生成摘要时出错

---

## 75. How to take a photo with scotch tape (lensless imaging) [video]

**原文标题**: How to take a photo with scotch tape (lensless imaging) [video]

**原文链接**: [https://www.youtube.com/watch?v=97f0nfU5Px0](https://www.youtube.com/watch?v=97f0nfU5Px0)

生成摘要时出错

---

## 76. Portable 1MV X-ray system combines Cockcroft–Walton with Van de Graaff dome

**原文标题**: Portable 1MV X-ray system combines Cockcroft–Walton with Van de Graaff dome

**原文链接**: [https://www.lanl.gov/media/publications/1663/0624-x-rays-light](https://www.lanl.gov/media/publications/1663/0624-x-rays-light)

生成摘要时出错

---

## 77. History of AT&T Long Lines

**原文标题**: History of AT&T Long Lines

**原文链接**: [https://telephoneworld.org/long-distance-companies/att-long-distance-network/history-of-att-long-lines/](https://telephoneworld.org/long-distance-companies/att-long-distance-network/history-of-att-long-lines/)

生成摘要时出错

---

## 78. planckforth: Bootstrapping a Forth interpreter from hand-written tiny ELF binary

**原文标题**: planckforth: Bootstrapping a Forth interpreter from hand-written tiny ELF binary

**原文链接**: [https://github.com/nineties/planckforth](https://github.com/nineties/planckforth)

生成摘要时出错

---

## 79. Suicide Linux (2009)

**原文标题**: Suicide Linux (2009)

**原文链接**: [https://qntm.org/suicide](https://qntm.org/suicide)

生成摘要时出错

---

## 80. Rolling your own serverless OCR in 40 lines of code

**原文标题**: Rolling your own serverless OCR in 40 lines of code

**原文链接**: [https://christopherkrapu.com/blog/2026/ocr-textbooks-modal-deepseek/](https://christopherkrapu.com/blog/2026/ocr-textbooks-modal-deepseek/)

生成摘要时出错

---

## 81. SvarDOS – an open-source DOS distribution

**原文标题**: SvarDOS – an open-source DOS distribution

**原文链接**: [http://svardos.org/](http://svardos.org/)

生成摘要时出错

---

## 82. PascalABC.net

**原文标题**: PascalABC.net

**原文链接**: [https://pascalabc.net:443/en](https://pascalabc.net:443/en)

生成摘要时出错

---

## 83. Show HN: 2D Coulomb Gas Simulator

**原文标题**: Show HN: 2D Coulomb Gas Simulator

**原文链接**: [https://simonhalvdansson.github.io/2D-Coulomb-Gas-Tools/index_gpu.html](https://simonhalvdansson.github.io/2D-Coulomb-Gas-Tools/index_gpu.html)

生成摘要时出错

---

## 84. WebMCP Proposal

**原文标题**: WebMCP Proposal

**原文链接**: [https://webmachinelearning.github.io/webmcp/](https://webmachinelearning.github.io/webmcp/)

生成摘要时出错

---

## 85. MessageFormat: Unicode standard for localizable message strings

**原文标题**: MessageFormat: Unicode standard for localizable message strings

**原文链接**: [https://github.com/unicode-org/message-format-wg](https://github.com/unicode-org/message-format-wg)

生成摘要时出错

---

## 86. Vim-pencil: Rethinking Vim as a tool for writing

**原文标题**: Vim-pencil: Rethinking Vim as a tool for writing

**原文链接**: [https://github.com/preservim/vim-pencil](https://github.com/preservim/vim-pencil)

生成摘要时出错

---

## 87. Running My Own XMPP Server

**原文标题**: Running My Own XMPP Server

**原文链接**: [https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/](https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/)

生成摘要时出错

---

## 88. Ministry of Justice orders deletion of the UK's largest court reporting database

**原文标题**: Ministry of Justice orders deletion of the UK's largest court reporting database

**原文链接**: [https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/](https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/)

生成摘要时出错

---

## 89. Looks: A Halide Mark III Preview

**原文标题**: Looks: A Halide Mark III Preview

**原文链接**: [https://www.lux.camera/mark-iii-looks/](https://www.lux.camera/mark-iii-looks/)

生成摘要时出错

---

## 90. Show HN: Simple org-mode web adapter

**原文标题**: Show HN: Simple org-mode web adapter

**原文链接**: [https://github.com/SpaceTurth/Org-Web-Adapter](https://github.com/SpaceTurth/Org-Web-Adapter)

生成摘要时出错

---

## 91. The End of the Office

**原文标题**: The End of the Office

**原文链接**: [https://blog.andrewyang.com/p/the-end-of-the-office](https://blog.andrewyang.com/p/the-end-of-the-office)

生成摘要时出错

---

## 92. Rethinking High-School Science Fairs

**原文标题**: Rethinking High-School Science Fairs

**原文链接**: [https://asteriskmag.com/issues/13/rethinking-high-school-science-fairs](https://asteriskmag.com/issues/13/rethinking-high-school-science-fairs)

生成摘要时出错

---

## 93. Show HN: I built a tool to un-dumb Claude Code's CLI output (Local Log Viewer)

**原文标题**: Show HN: I built a tool to un-dumb Claude Code's CLI output (Local Log Viewer)

**原文链接**: [https://github.com/matt1398/claude-devtools](https://github.com/matt1398/claude-devtools)

生成摘要时出错

---

## 94. Building a model that visualizes strategic golf

**原文标题**: Building a model that visualizes strategic golf

**原文链接**: [https://golfcoursewiki.substack.com/p/i-spent-the-last-month-and-a-half](https://golfcoursewiki.substack.com/p/i-spent-the-last-month-and-a-half)

生成摘要时出错

---

## 95. Picol: A Tcl interpreter in 500 lines of code

**原文标题**: Picol: A Tcl interpreter in 500 lines of code

**原文链接**: [https://github.com/antirez/picol](https://github.com/antirez/picol)

生成摘要时出错

---

## 96. I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文标题**: I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文链接**: [https://mastodon.world/@knowmadd/116072773118828295](https://mastodon.world/@knowmadd/116072773118828295)

生成摘要时出错

---

## 97. UK Discord users were part of a Peter Thiel-linked data collection experiment

**原文标题**: UK Discord users were part of a Peter Thiel-linked data collection experiment

**原文链接**: [https://www.rockpapershotgun.com/good-news-uk-discord-users-were-part-of-a-peter-thiel-linked-data-collection-experiment](https://www.rockpapershotgun.com/good-news-uk-discord-users-were-part-of-a-peter-thiel-linked-data-collection-experiment)

生成摘要时出错

---

## 98. Chiplets Get Physical: The Days of Mix-and-Match Silicon Draw Nigh

**原文标题**: Chiplets Get Physical: The Days of Mix-and-Match Silicon Draw Nigh

**原文链接**: [https://www.eejournal.com/article/chiplets-get-physical-the-days-of-mix-and-match-silicon-draw-nigh/](https://www.eejournal.com/article/chiplets-get-physical-the-days-of-mix-and-match-silicon-draw-nigh/)

生成摘要时出错

---

## 99. Anthropic tries to hide Claude's AI actions. Devs hate it

**原文标题**: Anthropic tries to hide Claude's AI actions. Devs hate it

**原文链接**: [https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/](https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/)

生成摘要时出错

---

## 100. JavaScript-heavy approaches are not compatible with long-term performance goals

**原文标题**: JavaScript-heavy approaches are not compatible with long-term performance goals

**原文链接**: [https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

生成摘要时出错

---

