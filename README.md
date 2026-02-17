# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-17.md)

*最后自动更新时间: 2026-02-17 18:19:46*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 2 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 3 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 4 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 5 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 6 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 7 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 8 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 9 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 10 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 11 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 12 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 13 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 14 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 15 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 16 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 17 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 18 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 19 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 20 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 21 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 22 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 23 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 24 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 25 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 26 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 27 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 28 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 29 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 30 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 31 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 32 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 33 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 34 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 35 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 36 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 37 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 38 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 39 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 40 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 41 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 42 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 43 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 44 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 45 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 46 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 47 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 48 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 49 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 50 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 51 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 52 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 53 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 54 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 55 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 56 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 57 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 58 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 59 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 60 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 61 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 62 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 63 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 64 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 65 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 66 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 67 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 68 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 69 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 70 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 71 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 72 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 73 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 74 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 75 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 76 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 77 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 78 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 79 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 80 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 81 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 82 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 83 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 84 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 85 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 86 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 87 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 88 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 89 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 90 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 91 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 92 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 93 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 94 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 95 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 96 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 97 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 98 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 99 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 100 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 101 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 102 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 103 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 104 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 105 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 106 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 107 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 108 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 109 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 110 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 111 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 112 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 113 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 114 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 115 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 116 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 117 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 118 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 119 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 120 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 121 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 122 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 123 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 124 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 125 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 126 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 127 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 128 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 129 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 130 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 131 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 132 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 133 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 134 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 135 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 136 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 137 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 138 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 139 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 140 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 141 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 142 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 143 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 144 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 145 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 146 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 147 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 148 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 149 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 150 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 151 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 152 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 153 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 154 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 155 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 156 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 157 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 158 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 159 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 160 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 161 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 162 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 163 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 164 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 165 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 166 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 167 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 168 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 169 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 170 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 171 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 172 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 173 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 174 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 175 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 176 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 177 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 178 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 179 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 180 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 181 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 182 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 183 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 184 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 185 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 186 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 187 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 188 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 189 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 190 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 191 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 192 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 193 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 194 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 195 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 196 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 197 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 198 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 199 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 200 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 201 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 202 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 203 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 204 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 205 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 206 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 207 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 208 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 209 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 210 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 211 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 212 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 213 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 214 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 215 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 216 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 217 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 218 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 219 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 220 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 221 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 222 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 223 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 224 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 225 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 226 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 227 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 228 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 229 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 230 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 231 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 232 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 233 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 234 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 235 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 236 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 237 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 238 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 239 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 240 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 241 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 242 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 243 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 244 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 245 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 246 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 247 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 248 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 249 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 250 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 251 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 252 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 253 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 254 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 255 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 256 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 257 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 258 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 259 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 260 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 261 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 262 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 263 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 264 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 265 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 266 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 267 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 268 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 269 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 270 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 271 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 272 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 273 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 274 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 275 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 276 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 277 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 278 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 279 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 280 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 281 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 282 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 283 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 284 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 285 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 286 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 287 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 288 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 289 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 290 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 291 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 292 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 293 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 294 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 295 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 296 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 297 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 298 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 299 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 300 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 301 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 302 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 303 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 304 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 305 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 306 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 307 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 308 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 309 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 310 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 311 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 312 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 313 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 314 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 315 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 316 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 317 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 318 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 319 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 320 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 321 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 322 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 323 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 324 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 325 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 326 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 327 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 328 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 329 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 330 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 331 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 332 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 333 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 334 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
