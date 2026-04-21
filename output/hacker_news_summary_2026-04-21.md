# Hacker News 热门文章摘要 (2026-04-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Running a Minecraft Server and More on a 1960s Univac Computer

**原文标题**: Running a Minecraft Server and More on a 1960s Univac Computer

**原文链接**: [https://farlow.dev/2026/04/17/running-a-minecraft-server-and-more-on-a-1960s-univac-computer](https://farlow.dev/2026/04/17/running-a-minecraft-server-and-more-on-a-1960s-univac-computer)

生成摘要时出错

---

## 12. Edit store price tags using Flipper Zero

**原文标题**: Edit store price tags using Flipper Zero

**原文链接**: [https://github.com/i12bp8/TagTinker](https://github.com/i12bp8/TagTinker)

生成摘要时出错

---

## 13. Tindie store under "scheduled maintenance" for days

**原文标题**: Tindie store under "scheduled maintenance" for days

**原文链接**: [https://www.tindie.com/](https://www.tindie.com/)

生成摘要时出错

---

## 14. A type-safe, realtime collaborative Graph Database in a CRDT

**原文标题**: A type-safe, realtime collaborative Graph Database in a CRDT

**原文链接**: [https://codemix.com/graph](https://codemix.com/graph)

生成摘要时出错

---

## 15. Clojure: Transducers

**原文标题**: Clojure: Transducers

**原文链接**: [https://clojure.org/reference/transducers](https://clojure.org/reference/transducers)

生成摘要时出错

---

## 16. Original GrapheneOS responses to WIRED fact checker

**原文标题**: Original GrapheneOS responses to WIRED fact checker

**原文链接**: [https://discuss.grapheneos.org/d/34369-original-grapheneos-responses-to-wired-fact-checker](https://discuss.grapheneos.org/d/34369-original-grapheneos-responses-to-wired-fact-checker)

生成摘要时出错

---

## 17. Anthropic says OpenClaw-style Claude CLI usage is allowed again

**原文标题**: Anthropic says OpenClaw-style Claude CLI usage is allowed again

**原文链接**: [https://docs.openclaw.ai/providers/anthropic](https://docs.openclaw.ai/providers/anthropic)

生成摘要时出错

---

## 18. MNT Reform is an open hardware laptop, designed and assembled in Germany

**原文标题**: MNT Reform is an open hardware laptop, designed and assembled in Germany

**原文链接**: [http://mnt.stanleylieber.com/reform/](http://mnt.stanleylieber.com/reform/)

生成摘要时出错

---

## 19. Tim Cook's Impeccable Timing

**原文标题**: Tim Cook's Impeccable Timing

**原文链接**: [https://stratechery.com/2026/tim-cooks-impeccable-timing/](https://stratechery.com/2026/tim-cooks-impeccable-timing/)

生成摘要时出错

---

## 20. Show HN: Mediator.ai – Using Nash bargaining and LLMs to systematize fairness

**原文标题**: Show HN: Mediator.ai – Using Nash bargaining and LLMs to systematize fairness

**原文链接**: [https://mediator.ai/](https://mediator.ai/)

生成摘要时出错

---

## 21. Leonardo, Borgia, and Machiavelli: A Fateful Collusion

**原文标题**: Leonardo, Borgia, and Machiavelli: A Fateful Collusion

**原文链接**: [https://www.historytoday.com/archive/leonardo-borgia-and-machiavelli-fateful-collusion](https://www.historytoday.com/archive/leonardo-borgia-and-machiavelli-fateful-collusion)

生成摘要时出错

---

## 22. Anthropic takes $5B from Amazon and pledges $100B in cloud spending in return

**原文标题**: Anthropic takes $5B from Amazon and pledges $100B in cloud spending in return

**原文链接**: [https://techcrunch.com/2026/04/20/anthropic-takes-5b-from-amazon-and-pledges-100b-in-cloud-spending-in-return/](https://techcrunch.com/2026/04/20/anthropic-takes-5b-from-amazon-and-pledges-100b-in-cloud-spending-in-return/)

生成摘要时出错

---

## 23. Slava's Monoid Zoo

**原文标题**: Slava's Monoid Zoo

**原文链接**: [https://factorcode.org/slava/monoids.html](https://factorcode.org/slava/monoids.html)

生成摘要时出错

---

## 24. Show HN: Ctx – a /resume that works across Claude Code and Codex

**原文标题**: Show HN: Ctx – a /resume that works across Claude Code and Codex

**原文链接**: [https://github.com/dchu917/ctx](https://github.com/dchu917/ctx)

生成摘要时出错

---

## 25. Salmon exposed to cocaine and its main byproduct roam more widely

**原文标题**: Salmon exposed to cocaine and its main byproduct roam more widely

**原文链接**: [https://www.science.org/content/article/cocaine-pollution-gives-salmon-wanderlust](https://www.science.org/content/article/cocaine-pollution-gives-salmon-wanderlust)

生成摘要时出错

---

## 26. Colorado River disappeared record for 5M years: now we know where it was

**原文标题**: Colorado River disappeared record for 5M years: now we know where it was

**原文链接**: [https://phys.org/news/2026-04-colorado-river-geological-million-years.html](https://phys.org/news/2026-04-colorado-river-geological-million-years.html)

生成摘要时出错

---

## 27. Show HN: Daemons – we pivoted from building agents to cleaning up after them

**原文标题**: Show HN: Daemons – we pivoted from building agents to cleaning up after them

**原文链接**: [https://charlielabs.ai/](https://charlielabs.ai/)

生成摘要时出错

---

## 28. The Beauty of Bonsai Styles

**原文标题**: The Beauty of Bonsai Styles

**原文链接**: [https://longwoodgardens.org/blog/2023-05-17/beauty-bonsai-styles](https://longwoodgardens.org/blog/2023-05-17/beauty-bonsai-styles)

生成摘要时出错

---

## 29. Qwen3.6-Max-Preview: Smarter, Sharper, Still Evolving

**原文标题**: Qwen3.6-Max-Preview: Smarter, Sharper, Still Evolving

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-max-preview](https://qwen.ai/blog?id=qwen3.6-max-preview)

生成摘要时出错

---

## 30. Less human AI agents, please

**原文标题**: Less human AI agents, please

**原文链接**: [https://nial.se/blog/less-human-ai-agents-please/](https://nial.se/blog/less-human-ai-agents-please/)

生成摘要时出错

---

## 31. Meta to start capturing employee mouse movement, keystrokes for AI training data

**原文标题**: Meta to start capturing employee mouse movement, keystrokes for AI training data

**原文链接**: [https://tech.yahoo.com/ai/meta-ai/articles/exclusive-meta-start-capturing-employee-162745587.html](https://tech.yahoo.com/ai/meta-ai/articles/exclusive-meta-start-capturing-employee-162745587.html)

生成摘要时出错

---

## 32. A History of Erasures Learning to Write Like Leylâ Erbil

**原文标题**: A History of Erasures Learning to Write Like Leylâ Erbil

**原文链接**: [https://thepointmag.com/criticism/a-history-of-erasures/](https://thepointmag.com/criticism/a-history-of-erasures/)

生成摘要时出错

---

## 33. Expansion Artifacts

**原文标题**: Expansion Artifacts

**原文链接**: [https://mattstromawn.com/writing/expansion-artifacts/](https://mattstromawn.com/writing/expansion-artifacts/)

生成摘要时出错

---

## 34. High-Fidelity KV Cache Summarization Using Entropy and Low-Rank Reconstruction

**原文标题**: High-Fidelity KV Cache Summarization Using Entropy and Low-Rank Reconstruction

**原文链接**: [https://jchandra.com/posts/hae-ols/](https://jchandra.com/posts/hae-ols/)

生成摘要时出错

---

## 35. Louis Zocchi, games industry pioneer, has died

**原文标题**: Louis Zocchi, games industry pioneer, has died

**原文链接**: [https://icv2.com/articles/news/view/62176/r-i-p-louis-zocchi-the-godfather-dice](https://icv2.com/articles/news/view/62176/r-i-p-louis-zocchi-the-godfather-dice)

生成摘要时出错

---

## 36. As oceans warm, great white sharks are overheating

**原文标题**: As oceans warm, great white sharks are overheating

**原文链接**: [https://e360.yale.edu/digest/great-white-sharks-climate](https://e360.yale.edu/digest/great-white-sharks-climate)

生成摘要时出错

---

## 37. Apple ignores DMA interoperability requests and contradicts own documentation

**原文标题**: Apple ignores DMA interoperability requests and contradicts own documentation

**原文链接**: [https://fsfe.org/news/2026/news-20260420-01.html](https://fsfe.org/news/2026/news-20260420-01.html)

生成摘要时出错

---

## 38. Meta capturing employee mouse movements, keystrokes for AI training data

**原文标题**: Meta capturing employee mouse movements, keystrokes for AI training data

**原文链接**: [https://economictimes.indiatimes.com/tech/technology/meta-to-start-capturing-employee-mouse-movements-keystrokes-for-ai-training-data/articleshow/130422612.cms?from=mdr](https://economictimes.indiatimes.com/tech/technology/meta-to-start-capturing-employee-mouse-movements-keystrokes-for-ai-training-data/articleshow/130422612.cms?from=mdr)

生成摘要时出错

---

## 39. How to make a fast dynamic language interpreter

**原文标题**: How to make a fast dynamic language interpreter

**原文链接**: [https://zef-lang.dev/implementation](https://zef-lang.dev/implementation)

生成摘要时出错

---

## 40. The purist's guide to phở in Hanoi

**原文标题**: The purist's guide to phở in Hanoi

**原文链接**: [https://connla.substack.com/p/pho-in-hanoi-a-purists-guide](https://connla.substack.com/p/pho-in-hanoi-a-purists-guide)

生成摘要时出错

---

## 41. ChatGPT Recommends the Same 3 Companies to Every B2B Buyer. Until They Specify

**原文标题**: ChatGPT Recommends the Same 3 Companies to Every B2B Buyer. Until They Specify

**原文链接**: [https://growtika.com/blog/chatgpt-b2b-persona-recommendations](https://growtika.com/blog/chatgpt-b2b-persona-recommendations)

生成摘要时出错

---

## 42. Kimi vendor verifier – verify accuracy of inference providers

**原文标题**: Kimi vendor verifier – verify accuracy of inference providers

**原文链接**: [https://www.kimi.com/blog/kimi-vendor-verifier](https://www.kimi.com/blog/kimi-vendor-verifier)

生成摘要时出错

---

## 43. Roo code shuts down, Team will focus on roomote agent

**原文标题**: Roo code shuts down, Team will focus on roomote agent

**原文链接**: [https://twitter.com/mattrubens/status/2046636598859559114](https://twitter.com/mattrubens/status/2046636598859559114)

生成摘要时出错

---

## 44. Ternary Bonsai: Top Intelligence at 1.58 Bits

**原文标题**: Ternary Bonsai: Top Intelligence at 1.58 Bits

**原文链接**: [https://prismml.com/news/ternary-bonsai](https://prismml.com/news/ternary-bonsai)

生成摘要时出错

---

## 45. Air is full of DNA

**原文标题**: Air is full of DNA

**原文链接**: [https://www.nature.com/articles/d41586-026-01099-2](https://www.nature.com/articles/d41586-026-01099-2)

生成摘要时出错

---

## 46. Meta to start capturing employee mouse movements, keystrokes for AI training

**原文标题**: Meta to start capturing employee mouse movements, keystrokes for AI training

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

生成摘要时出错

---

## 47. Vera C. Rubin Observatory has Discovered 11,000 New Asteroids

**原文标题**: Vera C. Rubin Observatory has Discovered 11,000 New Asteroids

**原文链接**: [https://www.universetoday.com/articles/the-vera-c-rubin-observatory-has-discovered-11000-new-asteroids-and-its-barely-even-started](https://www.universetoday.com/articles/the-vera-c-rubin-observatory-has-discovered-11000-new-asteroids-and-its-barely-even-started)

生成摘要时出错

---

## 48. Smoking ban for people born after 2008 in the UK agreed

**原文标题**: Smoking ban for people born after 2008 in the UK agreed

**原文链接**: [https://www.bbc.co.uk/news/articles/cn08jy6w0l5o](https://www.bbc.co.uk/news/articles/cn08jy6w0l5o)

生成摘要时出错

---

## 49. ggsql: A Grammar of Graphics for SQL

**原文标题**: ggsql: A Grammar of Graphics for SQL

**原文链接**: [https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/](https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/)

生成摘要时出错

---

## 50. Quantum Computers Are Not a Threat to 128-Bit Symmetric Keys

**原文标题**: Quantum Computers Are Not a Threat to 128-Bit Symmetric Keys

**原文链接**: [https://words.filippo.io/128-bits/](https://words.filippo.io/128-bits/)

生成摘要时出错

---

## 51. How a subsea cable is repaired (2021)

**原文标题**: How a subsea cable is repaired (2021)

**原文链接**: [https://www.onesteppower.com/post/subsea-cable-repair](https://www.onesteppower.com/post/subsea-cable-repair)

生成摘要时出错

---

## 52. Types and Neural Networks

**原文标题**: Types and Neural Networks

**原文链接**: [https://www.brunogavranovic.com/posts/2026-04-20-types-and-neural-networks.html](https://www.brunogavranovic.com/posts/2026-04-20-types-and-neural-networks.html)

生成摘要时出错

---

## 53. All phones sold in the EU to have replaceable batteries from 2027

**原文标题**: All phones sold in the EU to have replaceable batteries from 2027

**原文链接**: [https://www.theolivepress.es/spain-news/2026/04/20/eu-to-force-replaceable-batteries-in-phones-and-tablets-from-2027/](https://www.theolivepress.es/spain-news/2026/04/20/eu-to-force-replaceable-batteries-in-phones-and-tablets-from-2027/)

生成摘要时出错

---

## 54. Japan's cherry blossom database, 1,200 years old, has a new keeper

**原文标题**: Japan's cherry blossom database, 1,200 years old, has a new keeper

**原文链接**: [https://www.nytimes.com/2026/04/17/climate/japan-cherry-blossom-database-scientist.html](https://www.nytimes.com/2026/04/17/climate/japan-cherry-blossom-database-scientist.html)

生成摘要时出错

---

## 55. Modern Rendering Culling Techniques

**原文标题**: Modern Rendering Culling Techniques

**原文链接**: [https://krupitskas.com/posts/modern_culling_techniques/](https://krupitskas.com/posts/modern_culling_techniques/)

生成摘要时出错

---

## 56. Monero Community Crowdfunding System

**原文标题**: Monero Community Crowdfunding System

**原文链接**: [https://ccs.getmonero.org/ideas/](https://ccs.getmonero.org/ideas/)

生成摘要时出错

---

## 57. John Ternus to become Apple CEO

**原文标题**: John Ternus to become Apple CEO

**原文链接**: [https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/](https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/)

生成摘要时出错

---

## 58. Soul Player C64 – A real transformer running on a 1 MHz Commodore 64

**原文标题**: Soul Player C64 – A real transformer running on a 1 MHz Commodore 64

**原文链接**: [https://github.com/gizmo64k/soulplayer-c64](https://github.com/gizmo64k/soulplayer-c64)

生成摘要时出错

---

## 59. WebUSB Extension for Firefox

**原文标题**: WebUSB Extension for Firefox

**原文链接**: [https://github.com/ArcaneNibble/awawausb](https://github.com/ArcaneNibble/awawausb)

生成摘要时出错

---

## 60. Even 'uncensored' models can't say what they want

**原文标题**: Even 'uncensored' models can't say what they want

**原文链接**: [https://morgin.ai/articles/even-uncensored-models-cant-say-what-they-want.html](https://morgin.ai/articles/even-uncensored-models-cant-say-what-they-want.html)

生成摘要时出错

---

## 61. M 7.4 earthquake – 100 km ENE of Miyako, Japan

**原文标题**: M 7.4 earthquake – 100 km ENE of Miyako, Japan

**原文链接**: [https://earthquake.usgs.gov/earthquakes/eventpage/us6000sri7/](https://earthquake.usgs.gov/earthquakes/eventpage/us6000sri7/)

生成摘要时出错

---

## 62. Four Horsemen of the AIpocalypse

**原文标题**: Four Horsemen of the AIpocalypse

**原文链接**: [https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/](https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/)

生成摘要时出错

---

## 63. Kefir C17/C23 Compiler

**原文标题**: Kefir C17/C23 Compiler

**原文链接**: [https://sr.ht/~jprotopopov/kefir/](https://sr.ht/~jprotopopov/kefir/)

生成摘要时出错

---

## 64. OpenClaw isn't fooling me. I remember MS-DOS

**原文标题**: OpenClaw isn't fooling me. I remember MS-DOS

**原文链接**: [https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/](https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/)

生成摘要时出错

---

## 65. Jujutsu megamerges for fun and profit

**原文标题**: Jujutsu megamerges for fun and profit

**原文链接**: [https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit)

生成摘要时出错

---

## 66. 10 years ago, someone wrote a test for Servo that included an expiry in 2026

**原文标题**: 10 years ago, someone wrote a test for Servo that included an expiry in 2026

**原文链接**: [https://mastodon.social/@jdm_/116429380667467307](https://mastodon.social/@jdm_/116429380667467307)

生成摘要时出错

---

## 67. Atlassian enables default data collection to train AI

**原文标题**: Atlassian enables default data collection to train AI

**原文链接**: [https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8](https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8)

生成摘要时出错

---

## 68. I learned Unity the wrong way

**原文标题**: I learned Unity the wrong way

**原文链接**: [https://darkounity.com/blog/how-i-learned-unity-the-wrong-way](https://darkounity.com/blog/how-i-learned-unity-the-wrong-way)

生成摘要时出错

---

## 69. Year of the IPv6 Overlay Network

**原文标题**: Year of the IPv6 Overlay Network

**原文链接**: [https://www.defined.net/blog/year-of-the-ipv6-overlay-network/](https://www.defined.net/blog/year-of-the-ipv6-overlay-network/)

生成摘要时出错

---

## 70. GitHub's fake star economy

**原文标题**: GitHub's fake star economy

**原文链接**: [https://awesomeagents.ai/news/github-fake-stars-investigation/](https://awesomeagents.ai/news/github-fake-stars-investigation/)

生成摘要时出错

---

## 71. Sauna effect on heart rate

**原文标题**: Sauna effect on heart rate

**原文链接**: [https://tryterra.co/research/sauna-effect-on-heart-rate](https://tryterra.co/research/sauna-effect-on-heart-rate)

生成摘要时出错

---

## 72. Using Changesets in a polyglot monorepo

**原文标题**: Using Changesets in a polyglot monorepo

**原文链接**: [https://luke.hsiao.dev/blog/changesets-polyglot-monorepo/](https://luke.hsiao.dev/blog/changesets-polyglot-monorepo/)

生成摘要时出错

---

## 73. Figma's woes compound with Claude Design

**原文标题**: Figma's woes compound with Claude Design

**原文链接**: [https://martinalderson.com/posts/figmas-woes-compound-with-claude-design/](https://martinalderson.com/posts/figmas-woes-compound-with-claude-design/)

生成摘要时出错

---

## 74. Why Crystal, 10 Years Later: Performance and Joy

**原文标题**: Why Crystal, 10 Years Later: Performance and Joy

**原文链接**: [https://serdardogruyol.com/why-crystal-10-years-later-performance-and-joy](https://serdardogruyol.com/why-crystal-10-years-later-performance-and-joy)

生成摘要时出错

---

## 75. Focused microwaves allow 3D printers to fuse circuits onto almost anything

**原文标题**: Focused microwaves allow 3D printers to fuse circuits onto almost anything

**原文链接**: [https://newatlas.com/electronics/meta-nfc-focused-microwaves-circuits/](https://newatlas.com/electronics/meta-nfc-focused-microwaves-circuits/)

生成摘要时出错

---

## 76. Kimi K2.6: Advancing open-source coding

**原文标题**: Kimi K2.6: Advancing open-source coding

**原文链接**: [https://www.kimi.com/blog/kimi-k2-6](https://www.kimi.com/blog/kimi-k2-6)

生成摘要时出错

---

## 77. Brands got worse on purpose

**原文标题**: Brands got worse on purpose

**原文链接**: [https://www.worseonpurpose.com/p/your-favorite-brands-got-worse-on-purpose](https://www.worseonpurpose.com/p/your-favorite-brands-got-worse-on-purpose)

生成摘要时出错

---

## 78. OpenAI ad partner now selling ChatGPT ad placements based on “prompt relevance”

**原文标题**: OpenAI ad partner now selling ChatGPT ad placements based on “prompt relevance”

**原文链接**: [https://www.adweek.com/media/exclusive-leaked-deck-reveals-stackadapts-playbook-for-chatgpt-ads/](https://www.adweek.com/media/exclusive-leaked-deck-reveals-stackadapts-playbook-for-chatgpt-ads/)

生成摘要时出错

---

## 79. I Made the "Next-Level" Camera and I love it

**原文标题**: I Made the "Next-Level" Camera and I love it

**原文链接**: [https://thelibre.news/i-made-the-next-level-camera-and-i-love-it/](https://thelibre.news/i-made-the-next-level-camera-and-i-love-it/)

生成摘要时出错

---

## 80. Brussels launched an age checking app. Hackers took 2 minutes to break it

**原文标题**: Brussels launched an age checking app. Hackers took 2 minutes to break it

**原文链接**: [https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/](https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/)

生成摘要时出错

---

## 81. Up to 8M Bees Are Living in an Underground Network Beneath This Cemetery

**原文标题**: Up to 8M Bees Are Living in an Underground Network Beneath This Cemetery

**原文链接**: [https://www.discovermagazine.com/up-to-8-million-bees-are-living-in-an-underground-network-beneath-this-cemetery-48977](https://www.discovermagazine.com/up-to-8-million-bees-are-living-in-an-underground-network-beneath-this-cemetery-48977)

生成摘要时出错

---

## 82. What if database branching was easy?

**原文标题**: What if database branching was easy?

**原文链接**: [https://xata.io/blog/what-if-database-branching-was-easy](https://xata.io/blog/what-if-database-branching-was-easy)

生成摘要时出错

---

## 83. Deezer says 44% of songs uploaded to its platform daily are AI-generated

**原文标题**: Deezer says 44% of songs uploaded to its platform daily are AI-generated

**原文链接**: [https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/](https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/)

生成摘要时出错

---

## 84. Writing string.h functions using string instructions in asm x86-64 (2025)

**原文标题**: Writing string.h functions using string instructions in asm x86-64 (2025)

**原文链接**: [https://pmasschelier.github.io/x86_64_strings/](https://pmasschelier.github.io/x86_64_strings/)

生成摘要时出错

---

## 85. Show HN: WeTransfer Alternative for Developers

**原文标题**: Show HN: WeTransfer Alternative for Developers

**原文链接**: [https://dlvr.sh/](https://dlvr.sh/)

生成摘要时出错

---

## 86. Blue Origin New Glenn rocket grounded after launching satellite into wrong orbit

**原文标题**: Blue Origin New Glenn rocket grounded after launching satellite into wrong orbit

**原文链接**: [https://www.boston25news.com/news/science/blue-origins-new/5ORGDBBN746LTDZ46OPZF7UAIQ/](https://www.boston25news.com/news/science/blue-origins-new/5ORGDBBN746LTDZ46OPZF7UAIQ/)

生成摘要时出错

---

## 87. F-35 is built for the wrong war

**原文标题**: F-35 is built for the wrong war

**原文链接**: [https://warontherocks.com/cogs-of-war/the-f-35-is-a-masterpiece-built-for-the-wrong-war/](https://warontherocks.com/cogs-of-war/the-f-35-is-a-masterpiece-built-for-the-wrong-war/)

生成摘要时出错

---

## 88. SDF Public Access Unix System

**原文标题**: SDF Public Access Unix System

**原文链接**: [https://sdf.org/?ssh](https://sdf.org/?ssh)

生成摘要时出错

---

## 89. 'The status quo is unsustainable': scrutiny of Kalshi, Polymarket explodes

**原文标题**: 'The status quo is unsustainable': scrutiny of Kalshi, Polymarket explodes

**原文链接**: [https://www.politico.com/news/2026/04/01/congress-kalshi-polymarket-regulation-00852370](https://www.politico.com/news/2026/04/01/congress-kalshi-polymarket-regulation-00852370)

生成摘要时出错

---

## 90. Israeli soldiers using sexual assault to force Palestinians out of West Bank

**原文标题**: Israeli soldiers using sexual assault to force Palestinians out of West Bank

**原文链接**: [https://www.theguardian.com/world/2026/apr/21/israeli-soldiers-using-sexual-assault-to-force-palestinians-out-of-west-bank-report-says](https://www.theguardian.com/world/2026/apr/21/israeli-soldiers-using-sexual-assault-to-force-palestinians-out-of-west-bank-report-says)

生成摘要时出错

---

## 91. 'The status quo is unsustainable': scrutiny of Kalshi, Polymarket explodes

**原文标题**: 'The status quo is unsustainable': scrutiny of Kalshi, Polymarket explodes

**原文链接**: [https://www.politico.com/news/2026/04/01/congress-kalshi-polymarket-regulation-00852370](https://www.politico.com/news/2026/04/01/congress-kalshi-polymarket-regulation-00852370)

生成摘要时出错

---

## 92. Claude Token Counter, now with model comparisons

**原文标题**: Claude Token Counter, now with model comparisons

**原文链接**: [https://simonwillison.net/2026/Apr/20/claude-token-counts/](https://simonwillison.net/2026/Apr/20/claude-token-counts/)

生成摘要时出错

---

## 93. A mad undertaking: An undefinitive guide to the Aadam Jacobs collection

**原文标题**: A mad undertaking: An undefinitive guide to the Aadam Jacobs collection

**原文链接**: [https://aadamjacobscollection.org/](https://aadamjacobscollection.org/)

生成摘要时出错

---

## 94. AI is changing how Texas universities teach computer science as job market slows

**原文标题**: AI is changing how Texas universities teach computer science as job market slows

**原文链接**: [https://www.texastribune.org/2026/04/21/texas-computer-science-college-degree-ai/](https://www.texastribune.org/2026/04/21/texas-computer-science-college-degree-ai/)

生成摘要时出错

---

## 95. Grafana 13

**原文标题**: Grafana 13

**原文链接**: [https://grafana.com/blog/grafana-13-release-all-the-latest-features/](https://grafana.com/blog/grafana-13-release-all-the-latest-features/)

生成摘要时出错

---

## 96. We accepted surveillance as default

**原文标题**: We accepted surveillance as default

**原文链接**: [https://vivianvoss.net/blog/why-we-accepted-surveillance](https://vivianvoss.net/blog/why-we-accepted-surveillance)

生成摘要时出错

---

## 97. Zero-Copy Pages in Rust: Or How I Learned to Stop Worrying and Love Lifetimes

**原文标题**: Zero-Copy Pages in Rust: Or How I Learned to Stop Worrying and Love Lifetimes

**原文链接**: [https://redixhumayun.github.io/databases/2026/04/14/zero-copy-pages-in-rust.html](https://redixhumayun.github.io/databases/2026/04/14/zero-copy-pages-in-rust.html)

生成摘要时出错

---

## 98. NSA is using Anthropic's Mythos despite blacklist

**原文标题**: NSA is using Anthropic's Mythos despite blacklist

**原文链接**: [https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon)

生成摘要时出错

---

## 99. Linux PTP mainline development war story and new features

**原文标题**: Linux PTP mainline development war story and new features

**原文链接**: [https://bootlin.com/blog/linux-ptp-mainline-development-war-story-and-new-features/](https://bootlin.com/blog/linux-ptp-mainline-development-war-story-and-new-features/)

生成摘要时出错

---

## 100. Not buying another Kindle

**原文标题**: Not buying another Kindle

**原文链接**: [https://www.androidauthority.com/amazon-kindle-2026-3657863/](https://www.androidauthority.com/amazon-kindle-2026-3657863/)

生成摘要时出错

---

