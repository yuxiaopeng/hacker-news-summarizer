# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-12.md)

*最后自动更新时间: 2026-11-12 23:01:42*
## 1. 黄仁勋辞职

**原文标题**: Jensen Huang resigns

**原文链接**: [https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f)

所提供链接的文章（发布于2023年12月）并未提及黄仁勋将辞职。相反，文章详细报道了他对新加坡的访问，以及他在美中贸易紧张局势下对英伟达业务战略的看法。

**文章摘要：**

在访问新加坡期间，英伟达首席执行官黄仁勋谈到了美国对华高端人工智能芯片出口管制所带来的挑战。黄仁勋强调，英伟达正与美国政府密切合作，确保其面向中国市场的新产品符合贸易规定。他指出，虽然相关限制影响了英伟达的收入，但公司仍致力于通过开发不违反出口限制的替代产品来为中国客户提供服务。

文章还强调了新加坡对英伟达的战略重要性。由于拥有先进的数据中心基础设施以及作为区域技术枢纽的地位，这个城市国家已成为英伟达重要的收入来源。黄仁勋会见了新加坡官员，讨论了进一步的投资机会和该国的国家人工智能战略，并对新加坡贡献全球人工智能生态系统的潜力表示信心。

总体而言，该报道凸显了黄仁勋在维持英伟达市场主导地位并扩大东南亚版图的同时，为应对半导体行业复杂的地缘政治局势所做的努力。文中并未提及任何关于辞职的消息；黄仁勋目前仍担任公司首席执行官。

---

## 2. Rust 1.100

**原文标题**: Rust 1.100

**原文链接**: [https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/)

Rust 1.100.0 是一个里程碑版本，带来了数项期待已久的语言特性稳定化，并对 Cargo 生态系统进行了重大的安全性增强。

**关键语言与 API 更新：**
*   **Never 类型 (`!`)**：历经十年，never 类型终于稳定了。它代表发散式计算，现在可以在代码中的任何位置命名。`Infallible` 现在是 `!` 的别名。这包含一个轻微的破坏性变更，因为在旧版本中，编译器现在会回退到 `!` 而不是 `()`。
*   **分配器 API (Allocator API)**：核心 `Allocator` trait 已稳定，允许在 `Box` 和 `Vec` 中使用自定义分配器。
*   **`DropGuard`**：一个新的辅助类型 `core::mem::DropGuard` 允许开发者在每个退出路径（包括 panic）上运行闭包，并提供 `dismiss` 方法以实现类似于事务的回滚逻辑。
*   **`conjure_zst`**：一个新的 unsafe 函数，提供了一种在安全的情况下创建零大小类型 (ZST) 的专用方式。

**Cargo 改进：**
*   **依赖冷却期**：为了缓解供应链攻击，Cargo 现在支持 `min-publish-age` 配置。这允许用户在指定期限内（例如三天）自动推迟使用新的 crate 版本，以确保它们已经过社区审查。
*   **未使用依赖检查**：Cargo 现在会对 `Cargo.toml` 中未使用的依赖发出警告，有助于缩短构建时间并减少冗余。
*   **减少缓存冲突**：构建目录布局经过重新调整，以更一致地使用配置哈希，从而防止重新构建问题并提高在 git 工作树之间的可靠性。

其他稳定的 API 包括 `bool::toggle`、`Vec::from_fn` 以及用于字符串和路径的各种前缀/后缀修剪方法。可以通过 `rustup update stable` 安装 Rust 1.100。

---

## 3. Gemini 4 Hydrogen 与编排器

**原文标题**: Gemini 4 Hydrogen and Orchestrator

**原文链接**: [https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/)

Antigravity 团队宣布在 Google Antigravity 平台上发布 **Gemini 4 Hydrogen** 以及一项名为 **Orchestrator** 的全新路由功能。

**Orchestrator** 旨在通过动态配对 Gemini 4 Hydrogen 与更强大的 Gemini 4 Carbon，平衡质量、效率和延迟。与在提示词开始时选择模型的传统静态路由器不同，Orchestrator 可以在单个任务执行过程中在模型之间进行双向切换。Carbon 通常处理高级规划和复杂的故障排除，而 Hydrogen 则负责执行，例如编写代码和运行测试。在 Terminal-Bench 4.1 测试中，这种混合方法实现了接近 Carbon 的成功率，同时速度提升了 19%，配额消耗减少了 24%。

**Gemini 4 Hydrogen** 也可作为日常编程的独立模型使用。它提供四个可调节的“思考层级”（低、中、高、极高），以控制推理深度。在性能方面，Hydrogen 在 Artificial Analysis 智能指数中获得 51 分，在 Terminal-Bench 4.1 中得分为 57%，显著优于之前的 Argon 和 3.8 Flash 等模型。

对于开发者，**Antigravity SDK** 支持编程控制，允许用户针对特定角色将 Carbon 和 Hydrogen 协作——例如使用 Hydrogen 进行快速 UI 迭代，而使用 Carbon 进行复杂的重构或安全审计。

**可用性：**
*   **Gemini 4 Hydrogen：** 正在向 Google AI Pro 和 Ultra 订阅者推出。
*   **Orchestrator：** 目前面向 Google AI Ultra 订阅者开放。
*   **企业版：** 两者均可通过 Gemini 商业版获取。

---

## 4. 基础模型框架

**原文标题**: Foundation Models framework

**原文链接**: [https://developer.apple.com/foundation-models-framework/](https://developer.apple.com/foundation-models-framework/)

Foundation Models 框架是一个原生 Swift API，旨在将大语言模型 (LLM) 集成到 Apple 生态系统的应用中。它通过私有云计算 (PCC) 提供对设备端 Apple 基础模型和高性能服务器模型的直接访问。

**核心功能与特性：**
*   **多样化的模型支持：** 开发者可以利用设备端模型处理隐私和离线任务，或者通过统一的语言模型协议切换到第三方前沿模型（如 Claude 和 Gemini）。
*   **多模态智能：** 该框架支持图像理解，允许同时处理文本和图像。通过与 Vision 框架集成，可实现 OCR 和条形码扫描等专业任务。
*   **动态配置 (Dynamic Profiles)：** 这一声明式 API 允许开发者在单个连续会话中更换模型、工具和指令。由于对话记录在更换过程中是共享的，因此它非常适合构建复杂的 AI 智能体和“技能”。
*   **开发者工具：** 评估框架 (Evaluations framework) 有助于在传统单元测试之外测试和优化提示词。此外，macOS 27 中全新的 `fm` 命令行工具和 Python SDK 进一步简化了快速原型设计、脚本编写以及与现有 AI 研究工具的集成。

**隐私与可访问性：**
通过私有云计算，Apple 在提供前沿级智能的同时确保了严格的隐私保护，保证用户数据绝不会被存储，Apple 也无法访问。对于下载量少于 200 万次的 App Store 小型企业计划开发者，该服务不收取云端 API 费用。

其使用受特定的《可接受使用要求》约束，并包含相关文档以协助开发者遵守《欧盟 AI 法案》。

---

## 5. 发现一颗绕太阳公转一周约需280年的候选矮行星。

**原文标题**: Dwarf planet candidate appears which takes roughly 280 years to orbit our sun

**原文链接**: [https://www.smithsonianmag.com/smart-news/astronomers-found-a-mysterious-object-orbiting-far-beyond-pluto-it-could-be-a-new-dwarf-planet-hidden-in-our-solar-system-180989857/](https://www.smithsonianmag.com/smart-news/astronomers-found-a-mysterious-object-orbiting-far-beyond-pluto-it-could-be-a-new-dwarf-planet-hidden-in-our-solar-system-180989857/)

天文学家利用薇拉·鲁宾天文台的数据发现了一颗重要的新矮行星候选体，编号为**2026 ED138**。该天体距离太阳约为地日距离的46倍，绕轨道运行一周需要281.1年。其轨道倾角接近25度，暗示其过去曾与海王星发生过引力相互作用。

首席研究员马修·霍尔曼（Matthew Holman）及其团队通过将现代数据与历史记录（包括追溯至1937年的照相底片）进行交叉比对，确认了该天体的存在。虽然目前被标记为“候选体”，但估计2026 ED138的直径在370至930英里之间。若要正式归类为矮行星——并入冥王星、阋神星、鸟神星、妊神星和谷神星的行列——必须证明其体积足够大，能依靠自身引力使其呈现近乎球形的形状。

由于仅凭亮度无法确定其大小（因为反射率高的小型冰冷天体看起来可能与反射率低的大型天体一样亮），天文学家计划利用红外观测或掩星现象来确定其确切尺寸。

这一发现是薇拉·鲁宾天文台的一座重大里程碑，突显了在太阳系“未探索”区域寻找更多大型天体的潜力，特别是在南半球以及被银河系密集核心遮挡的区域。专家表示，这一发现可能只是“冰山一角”，预示着在太阳系边缘仍有许多遥远的大型天体——甚至可能是地球大小的天体——尚未被发现。

---

## 6. Show HN：我的 300 美元刺绣机需要订阅，于是我开发了自己的应用

**原文标题**: Show HN: My $300 embroidery machine needed a subscription, so I built my own app

**原文链接**: [https://github.com/simpsoka/zigzag](https://github.com/simpsoka/zigzag)

**ZigZag** 是一款使用 Rust 语言开发的视觉化刺绣编辑器，旨在为家用刺绣机提供高性能、免订阅的替代方案。它的诞生是为了绕过像兄弟（Brother）Skitch (PP1) 等硬件常见的付费门槛，并提供一套专业级工具，用于将 SVG 矢量作品转换为可直接刺绣的针迹。

**核心功能与特性：**
*   **专业设计工具：** 界面参考了 Adobe Illustrator，提供钢笔工具、画笔（支持路径平滑）、形状工具以及“智能辅助线”等高级矢量工具。它还内置了强大的“图像描摹”功能，可将徽标和照片转换为可刺绣路径。
*   **AI 集成：** ZigZag 内置支持模型上下文协议（MCP）。这使得 AI 智能体（如 Claude）能够作为设计伙伴，在编辑器中实时创建或修改刺绣设计。
*   **精密的针迹引擎：** 该软件支持多种针法类型，包括榻榻米填充、平包针、直线针和贴布绣。内置的“规划器”通过消除重叠、管理剪线以及优化走针路径以减少断线，从而提升设计质量。
*   **广泛的兼容性：** 用户可以将设计导出为行业标准格式（PES、DST、EXP、JEF、VP3），或通过蓝牙直接发送至 Brother Skitch 机器。
*   **开发者友好：** 凭借高性能的 Rust 引擎，该软件同时提供图形用户界面（GUI）和命令行工具。它为 macOS 提供已签名且经过公证的应用，为 Windows 提供便携版本。

通过将专业矢量编辑、智能路径优化和尖端 AI 集成相结合，ZigZag 为刺绣社区（从普通 DIY 爱好者到技术开发者）提供了一套强大的开源工作流。

---

## 7. Microsoft 365 服务降级

**原文标题**: Service degradation on Microsoft 365

**原文链接**: [https://status.cloud.microsoft/](https://status.cloud.microsoft/)

The provided text indicates a service degradation affecting Microsoft 365, but it does not contain specific details regarding the nature or scope of the issue.

The content consists primarily of a technical notice from the Microsoft service health status page, stating that JavaScript must be enabled to run the application. Consequently, the key information—such as which specific services are impacted, the cause of the degradation, or the estimated time for resolution—is not visible in this snippet. To access the full report and live updates, a user would need to view the page in a JavaScript-enabled web browser.

---

## 8. 22-Year-Old PostgreSQL Bug Turned into Remote Code Execution

**原文标题**: 22-Year-Old PostgreSQL Bug Turned into Remote Code Execution

**原文链接**: [https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/)

The article chronicles security researcher Mehmet’s discovery of a 22-year-old type-confusion vulnerability in the PostgreSQL core, which leads to reliable memory corruption and Remote Code Execution (RCE).

The investigation began while Mehmet was exploiting memory corruption in PostgreSQL extensions like `pg_clickhouse`. This led him to a deep dive into PostgreSQL internals, specifically how the engine represents data using a structure called a **Datum**. He learned that a `Datum` is an opaque 8-byte header that does not inherently know its own data type; instead, PostgreSQL relies on external metadata (Object Identifiers or OIDs) to decide which internal function (e.g., `textout` or `int4out`) should process the value.

Mehmet hypothesized that if he could change a value’s type after the database had already "decided" how to process it but before execution, he could trigger a type confusion. He discovered a primitive to achieve this by using **Composite Types** and **Prepared Statements**:

1.  **Preparation:** Define a custom composite type (e.g., containing a `UUID`) and create a prepared statement using that type.
2.  **Alteration:** Before executing the statement, use `ALTER TYPE` to change the composite type’s attribute to a different type (e.g., `bytea`).
3.  **Execution:** When the prepared statement is executed, the engine uses the cached plan but processes the data using the new, mismatched type logic.

This vulnerability allows a user to force the database to treat one data structure as another, leading to memory corruption. The article highlights that while prepared statements are typically viewed as a security feature against SQL injection, the way PostgreSQL cached these plans failed to account for changes in composite type definitions, leaving a critical flaw in the core engine for over two decades.

---

## 9. 我正在让大语言模型在小型和老旧设备上运行。

**原文标题**: I'm making LLMs work on small and old devices

**原文链接**: [https://github.com/hyperionaidev/smolmaxxing/](https://github.com/hyperionaidev/smolmaxxing/)

生成摘要时出错

---

## 10. Abandoned Quake 4 expansion finished by modders and now playable

**原文标题**: Abandoned Quake 4 expansion finished by modders and now playable

**原文链接**: [https://www.moddb.com/mods/openq4/downloads/openq4-0141-windows-x64](https://www.moddb.com/mods/openq4/downloads/openq4-0141-windows-x64)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 2 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 3 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 4 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 5 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 6 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 7 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 8 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 9 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 10 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 11 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 12 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 13 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 14 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 15 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 16 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 17 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 18 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 19 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 20 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 21 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 22 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 23 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 24 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 25 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 26 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 27 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 28 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 29 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 30 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 31 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 32 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 33 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 34 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 35 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 36 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 37 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 38 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 39 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 40 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 41 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 42 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 43 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 44 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 45 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 46 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 47 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 48 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 49 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 50 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 51 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 52 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 53 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 54 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 55 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 56 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 57 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 58 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 59 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 60 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 61 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 62 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 63 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 64 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 65 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 66 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 67 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 68 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 69 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 70 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 71 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 72 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 73 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 74 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 75 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 76 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 77 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 78 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 79 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 80 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 81 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 82 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 83 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 84 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 85 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 86 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 87 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 88 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 89 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 90 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 91 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 92 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 93 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 94 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 95 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 96 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 97 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 98 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 99 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 100 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 101 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 102 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 103 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 104 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 105 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 106 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 107 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 108 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 109 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 110 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 111 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 112 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 113 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 114 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 115 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 116 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 117 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 118 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 119 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 120 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 121 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 122 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 123 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 124 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 125 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 126 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 127 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 128 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 129 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 130 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 131 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 132 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 133 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 134 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 135 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 136 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 137 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 138 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 139 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 140 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 141 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 142 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 143 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 144 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 145 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 146 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 147 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 148 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 149 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 150 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 151 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 152 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 153 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 154 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 155 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 156 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 157 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 158 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 159 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 160 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 161 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 162 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 163 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 164 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 165 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 166 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 167 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 168 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 169 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 170 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 171 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 172 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 173 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 174 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 175 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 176 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 177 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 178 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 179 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 180 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 181 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 182 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 183 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 184 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 185 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 186 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 187 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 188 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 189 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 190 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 191 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 192 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 193 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 194 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 195 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 196 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 197 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 198 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 199 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 200 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 201 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 202 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 203 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 204 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 205 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 206 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 207 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 208 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 209 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 210 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 211 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 212 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 213 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 214 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 215 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 216 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 217 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 218 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 219 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 220 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 221 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 222 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 223 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 224 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 225 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 226 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 227 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 228 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 229 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 230 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 231 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 232 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 233 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 234 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 235 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 236 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 237 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 238 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 239 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 240 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 241 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 242 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 243 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 244 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 245 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 246 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 247 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 248 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 249 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 250 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 251 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 252 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 253 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 254 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 255 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 256 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 257 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 258 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 259 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 260 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 261 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 262 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 263 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 264 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 265 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 266 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 267 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 268 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 269 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 270 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 271 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 272 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 273 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 274 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 275 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 276 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 277 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 278 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 279 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 280 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 281 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 282 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 283 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 284 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 285 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 286 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 287 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 288 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 289 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 290 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 291 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 292 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 293 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 294 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 295 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 296 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 297 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 298 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 299 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 300 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 301 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 302 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 303 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 304 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 305 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 306 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 307 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 308 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 309 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 310 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 311 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 312 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 313 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 314 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 315 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 316 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 317 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 318 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 319 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 320 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 321 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 322 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 323 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 324 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 325 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 326 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 327 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 328 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 329 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 330 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 331 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 332 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 333 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 334 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 335 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 336 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 337 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 338 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 339 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 340 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 341 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 342 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 343 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 344 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 345 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 346 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 347 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 348 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 349 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 350 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 351 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 352 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 353 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 354 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 355 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 356 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 357 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 358 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 359 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 360 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 361 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 362 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 363 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 364 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 365 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 366 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 367 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 368 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 369 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 370 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 371 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 372 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 373 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 374 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 375 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 376 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 377 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 378 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 379 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 380 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 381 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 382 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 383 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 384 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 385 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 386 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 387 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 388 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 389 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 390 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 391 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 392 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 393 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 394 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 395 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 396 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 397 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 398 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 399 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 400 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 401 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 402 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 403 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 404 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 405 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 406 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 407 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 408 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 409 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 410 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 411 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 412 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 413 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 414 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 415 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 416 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 417 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 418 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 419 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 420 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 421 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 422 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 423 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 424 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 425 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 426 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 427 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 428 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 429 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 430 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 431 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 432 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 433 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 434 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 435 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 436 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 437 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 438 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 439 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 440 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 441 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 442 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 443 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 444 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 445 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 446 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 447 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 448 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 449 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 450 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 451 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 452 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 453 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 454 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 455 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 456 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 457 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 458 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 459 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 460 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 461 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 462 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 463 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 464 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 465 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 466 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 467 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 468 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 469 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 470 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 471 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 472 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 473 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 474 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 475 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 476 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 477 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 478 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 479 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 480 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 481 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 482 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 483 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 484 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 485 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 486 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 487 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 488 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 489 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 490 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 491 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 492 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 493 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 494 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 495 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 496 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 497 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 498 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 499 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 500 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 501 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 502 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 503 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 504 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 505 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 506 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 507 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 508 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 509 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 510 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 511 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 512 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 513 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 514 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 515 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 516 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 517 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 518 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 519 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 520 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 521 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 522 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 523 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 524 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 525 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 526 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 527 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 528 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 529 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 530 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 531 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 532 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 533 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 534 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 535 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 536 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 537 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 538 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 539 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 540 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 541 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 542 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 543 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 544 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 545 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 546 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 547 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 548 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 549 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 550 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 551 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 552 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 553 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 554 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 555 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 556 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 557 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 558 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 559 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 560 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 561 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 562 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 563 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 564 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 565 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 566 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 567 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 568 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 569 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 570 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 571 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 572 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 573 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 574 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 575 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 576 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 577 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 578 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 579 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 580 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 581 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 582 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 583 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 584 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 585 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 586 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 587 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 588 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 589 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 590 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 591 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 592 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 593 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 594 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 595 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 596 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 597 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 598 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
