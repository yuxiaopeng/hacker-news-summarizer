# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-21.md)

*最后自动更新时间: 2026-04-21 18:28:09*
## 1. Vercel 泄露事件：OAuth 攻击暴露平台环境变量风险

**原文标题**: The Vercel breach: OAuth attack exposes risk in platform environment variables

**原文链接**: [https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html](https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html)

2026年4月披露的Vercel数据泄露事件，凸显了OAuth供应链及平台级环境变量管理中固有的关键风险。此次攻击始于2024年6月，攻击者通过攻破Context.ai所属的一个Google Workspace OAuth应用程序，成功渗透进一名Vercel员工的账户并获取了内部系统权限，随后对客户环境变量进行了枚举。

造成此次泄露影响重大的一个主要因素是Vercel的架构设计——该设计将许多环境变量归类为“非敏感”，导致任何拥有内部系统访问权限的人员均可读取。此事件的显著特征是长达22个月的潜伏期。值得注意的是，在客户报告OpenAI凭据泄露与Vercel官方披露之间存在9天的间隔，这引发了外界对“从检测到通知”延迟时间的质疑。

Vercel首席执行官Guillermo Rauch将攻击者“令人惊讶的速度”归因于**AI加速的攻击手段**，认为大语言模型（LLM）驱动的侦察与自动化正在压缩传统的攻击时间线。这一事件符合2026年攻击者针对CI/CD及托管平台开发人员凭据的普遍趋势。

**核心要点：**
*   **OAuth是薄弱环节：** 受信任的第三方应用可以绕过传统安全边界，提供在密码轮换后依然有效的持久访问权限，且极少受到审计。
*   **设计缺陷：** 将环境变量设为“非敏感”造成了默认不安全的配置，扩大了攻击的波及范围。
*   **AI驱动的威胁：** 针对人为操作速度校准的防御基准，可能无法抵御能够并行化攻击的AI增强型对手。
*   **安全强化

---

## 2. 软件工程定律

**原文标题**: Laws of Software Engineering

**原文链接**: [https://lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com)

《软件工程定律》全面收录了 56 项主导软件系统开发、团队动态和专业决策的原则、模式及思维模型。其内容被划分为七大核心领域：

*   **架构：** 专注于系统的结构演化和内在约束。核心原则包括**康威定律**（系统设计镜像于组织的沟通结构）、**盖尔定律**（复杂系统必须由简单系统演化而来）以及 **CAP 定理**（分布式系统中的权衡）。
*   **团队与规划：** 强调人力和时间的局限性。著名的条目包括**布鲁克斯法则**（向进度落后的项目增加人力，只会使其更落后）、**帕金森定律**（工作会自动膨胀以填满所有可用时间）以及**巴士系数**（失去关键团队成员带来的风险）。
*   **设计与质量：** 强调简洁性、可维护性和严谨性。这包括 **KISS**（保持简单）和 **DRY**（不要重复自己）原则、**SOLID** 准则，以及**童子军军规**（离开代码时，始终要让它比你发现它时更整洁）。
*   **规模：** 探讨增长的物理特性，例如定义了通过并行化提升速度极限的**阿姆达尔定律**，以及关于网络价值的**梅特卡夫定律**。
*   **决策：** 探索认知偏差和问题解决框架，例如**奥卡姆剃刀**（倾向于简单方案）、**沉没成本谬误**以及**第一性原理思维**。

最终，这套合集为工程师和管理者提供了启发式指南。通过认知这些“定律”——从**抽象泄漏**等技术现实到**达克效应**等心理现象——从业者可以更好地应对现代软件开发中固有的权衡、社交摩擦和复杂性。

---

## 3. 奶酪周期地图

**原文标题**: A Periodic Map of Cheese

**原文链接**: [https://cheesemap.netlify.app/](https://cheesemap.netlify.app/)

《芝士周期图谱》探索了奶酪制作的“组合空间”，利用系统化的方法来识别既有的传统、稀有品种以及可能创造新奶酪的“空白领域”。虽然某些空白的产生是因为特定奶类的化学性质与特定工艺不兼容，但更多空白仅仅是地理、文化或物流障碍导致的。

文章重点介绍了几个极具潜力的“空白领域”，大胆的尝试或能产生非凡的结果：

*   **牦牛奶格鲁耶尔与花皮牦牛芝士**：牦牛奶的高脂肪和酪蛋白含量可以生产出风味鲜美、焦糖奶油味浓郁的阿尔卑斯风格奶酪，或是“四倍奶油”花皮奶酪，目前仅受限于喜马拉雅地区基础设施的匮乏。
*   **水牛奶创新**：鉴于水牛奶的高脂肪含量，文章建议开发“花皮水牛芝士”（一种天然的三倍奶油布里风格）或“菜蓟凝乳酶水牛托塔芝士”，将水牛奶的浓郁与伊比利亚制酪传统的植物苦味结合。
*   **布裹绵羊奶切达**：虽然布裹工艺传统上用于牛奶，但将其应用于绵羊奶将产生质地更致密、风味更浓烈且带有结晶感的奶酪。
*   **熏制骆驼奶芝士**：由于骆驼奶难以形成陈年奶酪所需的结构，对新鲜凝乳进行冷熏可以在无需结构完整性的情况下增加风味层次并掩盖酸味。
*   **驯鹿奶硬质芝士**：驯鹿奶含有20%的脂肪，可以制成现存最浓郁的硬质奶酪，尽管驯鹿挤奶极其困难，使得大规模生产几乎不可能实现。

归根结底，文章认为奶酪制作的未来在于弥合地理与传统之间的鸿沟，去创造那些在化学上可行但在历史上尚未被探索的产品。

---

## 4. Show HN: GoModel – 基于 Go 的开源 AI 网关

**原文标题**: Show HN: GoModel – an open-source AI gateway in Go

**原文链接**: [https://github.com/ENTERPILOT/GOModel/](https://github.com/ENTERPILOT/GOModel/)

**GoModel** 是一个使用 Go 语言编写的高性能开源 AI 网关，为各种大语言模型（LLM）提供商提供统一且兼容 OpenAI 的 API。它支持包括 OpenAI、Anthropic、Gemini、xAI、Groq、Azure OpenAI 以及通过 Ollama 接入的本地模型。其设计初衷是让开发者通过单一接口即可访问多种 LLM，从而简化多模型集成工作。

**核心特性：**
*   **广泛的供应商支持：** 桥接众多服务，提供用于聊天补全、嵌入（embeddings）、文件管理和批处理的端点。
*   **双层缓存：** 为降低延迟和成本，GoModel 采用了**精确匹配缓存**（通过 Redis）和**语义缓存**（通过 Qdrant 或 Pinecone 等向量数据库）。语义层能够识别相似查询，在高重复性的工作负载中，命中率可达 60-70%。
*   **可观测性与管理：** 包含管理面板、Prometheus 指标及详细的使用日志。它能按模型和周期追踪 Token 消耗，并提供审计日志和对话上下文历史。
*   **灵活性：** 支持多种存储后端（SQLite、PostgreSQL、MongoDB），并针对标准 OpenAI 架构未涵盖的功能提供供应商原生的“透传”路由。
*   **安全性：** 提供可选的防护栏（guardrails）流水线，以及适用于生产环境的主密钥（master key）身份验证系统。

**路线图：**
项目正朝着 0.2.0 版本迈进，计划实现智能路由、带用户限额的预算管理、可编辑的模型定价，并扩展对更多供应商（如 Cohere、DeepSeek）的支持。

GoModel 可通过 Docker 或 Docker Compose 轻松部署，对于需要以可扩展、低成本方式统一管理多个 AI 模型的开发者来说，这是一个强有力的解决方案。

---

## 5. 核聚变电站模拟器

**原文标题**: Fusion Power Plant Simulator

**原文链接**: [https://www.fusionenergybase.com/fusion-power-plant-simulator](https://www.fusionenergybase.com/fusion-power-plant-simulator)

由 Fusion Energy Base 开发的**核聚变电站模拟器**是一款旨在模拟核聚变能源技术与经济可行性的互动工具。它允许用户通过调整各项变量，探索如何将实验室规模的聚变反应转化为功能完善的并网发电站。

该模拟器的核心功能和参数包括：

*   **能量输入与运行模式：** 用户可以设置每脉冲加热能量和脉冲频率，或在**稳态**与**脉冲**运行模式之间进行选择。
*   **科学增益 ($Q_{sci}$)：** 该工具的核心在于科学增益（聚变输出功率与加热输入功率之比）与实际净发电量之间的关系。
*   **效率与负荷因子：** 模拟器考虑了现实中的工程约束，如加热系统效率（默认 50%）、电能转换效率（默认 33%）以及“厂用电”（维持电站自身系统运行所需的功率，设定为 20 MW）。
*   **燃料循环：** 高级设置支持对比不同燃料类型，包括 **D-T（氘-氚）**、**D-D**、**D-³He** 和 **p-¹¹B（质子-硼）**。每种燃料都会影响中子与带电粒子的能量分配转换效率。
*   **包层倍增：** 该工具还考虑了增殖包层在倍增能量输出中的作用。

最终，该模拟器充当了连接聚变物理学与电站工程学的教育桥梁，证明了实现高科学 $Q$ 值仅仅是创建净正能量源挑战中的一部分。

---

## 6. Britannica11.org – 1911年版《大英百科全书》结构化版本

**原文标题**: Britannica11.org – a structured edition of the 1911 Encyclopædia Britannica

**原文链接**: [https://britannica11.org/](https://britannica11.org/)

**Britannica11.org** 是历史悠久的第11版《不列颠百科全书》（最初出版于1910年至1911年间）的数字化、结构化版本。该在线平台通过实现全文搜索和便捷导航，使这部经典参考著作焕发了现代活力。其主要特色包括文章间广泛的交叉引用以及新增的注释，为这一20世纪初具有里程碑意义的资源提供了一个全面且用户友好的档案库。

---

## 7. Kasane: New drop-in Kakoune front end with GPU rendering and WASM Plugins

**原文标题**: Kasane: New drop-in Kakoune front end with GPU rendering and WASM Plugins

**原文链接**: [https://github.com/Yus314/kasane](https://github.com/Yus314/kasane)

Kasane is a modern, high-performance front-end for the Kakoune text editor, designed to enhance the editing experience while maintaining full backward compatibility with existing `kakrc` configurations and plugins. It serves as a drop-in replacement for the standard `kak` command.

**Key Features and Improvements:**
*   **Dual Rendering Backends:** Kasane supports both terminal and GPU-accelerated GUI rendering. The GPU mode (`--ui gui`) enables system font rendering, smooth animations, and inline image display.
*   **WASM Plugin System:** It introduces a sandboxed WebAssembly (WASM) plugin architecture using a Rust-based SDK. This allows for complex UI extensions—such as floating overlays, virtual text, and gutter decorations—with minimal code.
*   **Native Functionality:** The tool provides native multi-pane splits (eliminating the need for external multiplexers like tmux), flicker-free rendering, and robust Unicode/emoji support.
*   **Enhanced Connectivity:** It includes a built-in clipboard manager that works out-of-the-box across Wayland, X11, macOS, and SSH without requiring external utilities.

**Technical Details and Availability:**
Kasane is built with Rust and requires Kakoune version 2024.12.09 or later. It is currently stable for daily use, though the plugin API is still evolving. Users can install it via Arch Linux (AUR), Homebrew, Nix, or Cargo. The project includes several pre-bundled plugins, such as a fuzzy finder, a pane manager for splits, and an image previewer.

Kasane is open-source and licensed under MIT/Apache-2.0.

---

## 8. Trellis AI (YC W24) Is hiring engineers to build self-improving agents

**原文标题**: Trellis AI (YC W24) Is hiring engineers to build self-improving agents

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/SvzJaTH-member-of-technical-staff-product-engineering-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/SvzJaTH-member-of-technical-staff-product-engineering-full-time)

生成摘要时出错

---

## 9. 现代前端复杂度：本质还是偶然？

**原文标题**: Modern Front end Complexity: essential or accidental?

**原文链接**: [https://binaryigor.com/modern-frontend-complexity.html](https://binaryigor.com/modern-frontend-complexity.html)

生成摘要时出错

---

## 10. Show HN: VidStudio, a browser based video editor that doesn't upload your files

**原文标题**: Show HN: VidStudio, a browser based video editor that doesn't upload your files

**原文链接**: [https://vidstudio.app/video-editor](https://vidstudio.app/video-editor)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 2 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 3 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 4 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 5 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 6 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 7 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 8 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 9 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 10 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 11 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 12 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 13 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 14 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 15 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 16 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 17 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 18 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 19 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 20 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 21 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 22 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 23 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 24 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 25 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 26 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 27 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 28 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 29 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 30 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 31 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 32 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 33 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 34 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 35 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 36 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 37 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 38 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 39 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 40 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 41 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 42 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 43 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 44 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 45 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 46 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 47 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 48 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 49 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 50 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 51 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 52 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 53 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 54 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 55 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 56 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 57 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 58 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 59 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 60 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 61 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 62 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 63 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 64 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 65 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 66 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 67 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 68 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 69 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 70 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 71 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 72 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 73 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 74 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 75 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 76 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 77 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 78 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 79 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 80 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 81 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 82 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 83 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 84 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 85 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 86 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 87 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 88 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 89 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 90 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 91 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 92 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 93 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 94 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 95 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 96 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 97 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 98 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 99 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 100 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 101 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 102 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 103 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 104 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 105 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 106 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 107 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 108 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 109 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 110 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 111 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 112 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 113 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 114 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 115 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 116 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 117 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 118 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 119 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 120 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 121 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 122 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 123 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 124 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 125 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 126 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 127 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 128 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 129 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 130 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 131 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 132 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 133 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 134 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 135 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 136 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 137 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 138 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 139 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 140 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 141 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 142 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 143 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 144 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 145 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 146 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 147 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 148 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 149 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 150 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 151 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 152 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 153 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 154 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 155 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 156 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 157 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 158 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 159 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 160 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 161 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 162 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 163 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 164 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 165 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 166 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 167 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 168 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 169 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 170 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 171 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 172 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 173 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 174 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 175 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 176 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 177 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 178 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 179 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 180 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 181 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 182 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 183 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 184 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 185 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 186 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 187 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 188 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 189 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 190 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 191 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 192 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 193 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 194 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 195 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 196 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 197 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 198 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 199 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 200 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 201 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 202 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 203 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 204 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 205 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 206 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 207 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 208 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 209 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 210 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 211 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 212 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 213 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 214 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 215 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 216 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 217 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 218 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 219 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 220 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 221 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 222 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 223 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 224 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 225 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 226 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 227 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 228 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 229 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 230 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 231 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 232 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 233 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 234 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 235 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 236 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 237 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 238 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 239 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 240 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 241 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 242 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 243 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 244 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 245 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 246 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 247 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 248 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 249 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 250 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 251 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 252 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 253 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 254 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 255 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 256 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 257 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 258 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 259 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 260 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 261 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 262 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 263 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 264 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 265 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 266 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 267 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 268 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 269 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 270 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 271 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 272 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 273 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 274 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 275 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 276 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 277 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 278 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 279 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 280 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 281 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 282 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 283 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 284 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 285 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 286 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 287 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 288 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 289 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 290 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 291 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 292 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 293 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 294 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 295 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 296 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 297 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 298 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 299 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 300 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 301 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 302 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 303 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 304 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 305 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 306 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 307 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 308 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 309 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 310 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 311 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 312 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 313 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 314 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 315 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 316 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 317 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 318 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 319 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 320 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 321 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 322 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 323 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 324 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 325 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 326 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 327 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 328 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 329 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 330 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 331 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 332 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 333 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 334 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 335 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 336 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 337 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 338 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 339 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 340 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 341 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 342 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 343 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 344 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 345 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 346 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 347 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 348 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 349 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 350 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 351 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 352 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 353 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 354 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 355 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 356 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 357 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 358 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 359 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 360 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 361 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 362 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 363 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 364 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 365 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 366 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 367 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 368 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 369 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 370 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 371 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 372 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 373 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 374 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 375 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 376 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 377 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 378 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 379 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 380 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 381 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 382 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 383 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 384 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 385 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 386 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 387 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 388 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 389 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 390 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 391 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 392 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 393 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 394 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 395 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 396 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 397 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
