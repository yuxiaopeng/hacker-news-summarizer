# Hacker News 热门文章摘要 (2026-11-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. AI is turning Apple's app review process into a nightmare for synth developers

**原文标题**: AI is turning Apple's app review process into a nightmare for synth developers

**原文链接**: [https://synthanatomy.com/2026/11/ai-is-turning-apples-app-review-process-into-a-nightmare-for-developers.html](https://synthanatomy.com/2026/11/ai-is-turning-apples-app-review-process-into-a-nightmare-for-developers.html)

生成摘要时出错

---

## 12. Relax: JIT compiler for Rust to reduce build times

**原文标题**: Relax: JIT compiler for Rust to reduce build times

**原文链接**: [https://makepad.github.io/relax/](https://makepad.github.io/relax/)

生成摘要时出错

---

## 13. Gemini 4 Hydrogen

**原文标题**: Gemini 4 Hydrogen

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

生成摘要时出错

---

## 14. Why writing correct software is hard and why math (alone) won’t help us (2016)

**原文标题**: Why writing correct software is hard and why math (alone) won’t help us (2016)

**原文链接**: [https://pron.github.io/posts/correctness-and-complexity](https://pron.github.io/posts/correctness-and-complexity)

生成摘要时出错

---

## 15. Talking Zen 6 with Mike Clark at AMD In-Depth

**原文标题**: Talking Zen 6 with Mike Clark at AMD In-Depth

**原文链接**: [https://chipsandcheese.com/p/talking-zen-6-with-mike-clark-at](https://chipsandcheese.com/p/talking-zen-6-with-mike-clark-at)

生成摘要时出错

---

## 16. Safety in Algae Home Experiments

**原文标题**: Safety in Algae Home Experiments

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/algae-safety-in-home-experiments](https://chillphysicsenjoyer.substack.com/p/algae-safety-in-home-experiments)

生成摘要时出错

---

## 17. Distributed Ray Tracer

**原文标题**: Distributed Ray Tracer

**原文链接**: [https://ray.hatchet.run](https://ray.hatchet.run)

生成摘要时出错

---

## 18. Adapting CPython for Yk

**原文标题**: Adapting CPython for Yk

**原文链接**: [https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html](https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html)

生成摘要时出错

---

## 19. Show HN: AgentRun – open-source, Self-improving Managed Agents

**原文标题**: Show HN: AgentRun – open-source, Self-improving Managed Agents

**原文链接**: [https://github.com/Parcha-ai/agentrun/blob/main/README.md](https://github.com/Parcha-ai/agentrun/blob/main/README.md)

生成摘要时出错

---

## 20. Anthropic IPO

**原文标题**: Anthropic IPO

**原文链接**: [https://ipo.anthropic.com/us/](https://ipo.anthropic.com/us/)

生成摘要时出错

---

## 21. Words of warning about radiocarbon dating medieval human bones

**原文标题**: Words of warning about radiocarbon dating medieval human bones

**原文链接**: [https://www.nature.com/articles/s40494-026-02958-x](https://www.nature.com/articles/s40494-026-02958-x)

生成摘要时出错

---

## 22. Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文标题**: Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文链接**: [https://unemploymentlabs.com/checkpoint-forensics](https://unemploymentlabs.com/checkpoint-forensics)

生成摘要时出错

---

## 23. Data centers need power – lower income, rural residents pay the price

**原文标题**: Data centers need power – lower income, rural residents pay the price

**原文链接**: [https://news.cornell.edu/stories/2026/11/data-centers-need-power-lower-income-rural-residents-pay-price](https://news.cornell.edu/stories/2026/11/data-centers-need-power-lower-income-rural-residents-pay-price)

生成摘要时出错

---

## 24. ExcalidrawZ: Local Native Excalidraw on macOS/iOS

**原文标题**: ExcalidrawZ: Local Native Excalidraw on macOS/iOS

**原文链接**: [https://github.com/chocoford/ExcalidrawZ](https://github.com/chocoford/ExcalidrawZ)

生成摘要时出错

---

## 25. Our software engineering interviews are changing a little

**原文标题**: Our software engineering interviews are changing a little

**原文链接**: [https://blog.janestreet.com/software-engineering-interviews-are-changing-a-little/](https://blog.janestreet.com/software-engineering-interviews-are-changing-a-little/)

生成摘要时出错

---

## 26. A live tree of systemd jobs on the boot console

**原文标题**: A live tree of systemd jobs on the boot console

**原文链接**: [https://codeberg.org/wvhulle/bootvine](https://codeberg.org/wvhulle/bootvine)

生成摘要时出错

---

## 27. Singapore Says U.S. Not Helpful on Investigation into Suspected Spy's Company

**原文标题**: Singapore Says U.S. Not Helpful on Investigation into Suspected Spy's Company

**原文链接**: [https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html](https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html)

生成摘要时出错

---

## 28. Nintendo Takes Down Emulators and Firmware in Massive GitHub DMCA Sweep

**原文标题**: Nintendo Takes Down Emulators and Firmware in Massive GitHub DMCA Sweep

**原文链接**: [https://www.ign.com/articles/nintendo-takes-down-switch-emulators-and-mod-chip-firmware-in-massive-github-dmca-sweep](https://www.ign.com/articles/nintendo-takes-down-switch-emulators-and-mod-chip-firmware-in-massive-github-dmca-sweep)

生成摘要时出错

---

## 29. Libreagi – Save OSS Models

**原文标题**: Libreagi – Save OSS Models

**原文链接**: [https://libreagi.com/](https://libreagi.com/)

生成摘要时出错

---

## 30. AWS Lambda Web Functions keep billing memory ~7 minutes after the last request

**原文标题**: AWS Lambda Web Functions keep billing memory ~7 minutes after the last request

**原文链接**: [https://www.easel.sh/blog/lambda-web-functions-idle-memory](https://www.easel.sh/blog/lambda-web-functions-idle-memory)

生成摘要时出错

---

## 31. Fitting Four 32 GB Resizable Bars Behind a PCIe Switch on Linux

**原文标题**: Fitting Four 32 GB Resizable Bars Behind a PCIe Switch on Linux

**原文链接**: [https://doug.sh/posts/gpu-bars-behind-a-pcie-switch/](https://doug.sh/posts/gpu-bars-behind-a-pcie-switch/)

生成摘要时出错

---

## 32. Researchers discover rare star system that emits radio signals every 8 minutes

**原文标题**: Researchers discover rare star system that emits radio signals every 8 minutes

**原文链接**: [https://www.curtin.edu.au/news/media-release/researchers-discover-rare-star-system-that-emits-radio-signals-every-eight-minutes/](https://www.curtin.edu.au/news/media-release/researchers-discover-rare-star-system-that-emits-radio-signals-every-eight-minutes/)

生成摘要时出错

---

## 33. Electric ship batteries promise compact, cooler power

**原文标题**: Electric ship batteries promise compact, cooler power

**原文链接**: [https://spectrum.ieee.org/electric-ship-batteries](https://spectrum.ieee.org/electric-ship-batteries)

生成摘要时出错

---

## 34. Show HN: Apron Chat Protocol

**原文标题**: Show HN: Apron Chat Protocol

**原文链接**: [https://apron.chat/](https://apron.chat/)

生成摘要时出错

---

## 35. Jensen Huang Third Affair Allegations Revealed

**原文标题**: Jensen Huang Third Affair Allegations Revealed

**原文链接**: [https://www.forbes.com/sites/alisondurkee/2026/11/12/jensen-huang-had-a-third-affair-with-another-nvidia-employee-report-says/](https://www.forbes.com/sites/alisondurkee/2026/11/12/jensen-huang-had-a-third-affair-with-another-nvidia-employee-report-says/)

生成摘要时出错

---

## 36. Making a €40 USB-C hub work as a Nintendo Switch 2 dock

**原文标题**: Making a €40 USB-C hub work as a Nintendo Switch 2 dock

**原文链接**: [http://blog.nozomi.space/posts/sw2_dock/](http://blog.nozomi.space/posts/sw2_dock/)

生成摘要时出错

---

## 37. PCMag demands $12000 to link to an article

**原文标题**: PCMag demands $12000 to link to an article

**原文链接**: [https://twitter.com/rickbrewPDN/status/2120970541331050926](https://twitter.com/rickbrewPDN/status/2120970541331050926)

生成摘要时出错

---

## 38. Decoding REXPaint Files in Odin

**原文标题**: Decoding REXPaint Files in Odin

**原文链接**: [https://tylerelton.com/posts/decoding-rexpaint-files-in-odin/](https://tylerelton.com/posts/decoding-rexpaint-files-in-odin/)

生成摘要时出错

---

## 39. Creating Worlds: Runes and Spells Prototype

**原文标题**: Creating Worlds: Runes and Spells Prototype

**原文链接**: [https://www.fractalkitty.com/creating-worlds-runes-and-spells/](https://www.fractalkitty.com/creating-worlds-runes-and-spells/)

生成摘要时出错

---

## 40. Socratic Tutor

**原文标题**: Socratic Tutor

**原文链接**: [https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md](https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md)

生成摘要时出错

---

## 41. Relate – the agent-native graph database

**原文标题**: Relate – the agent-native graph database

**原文链接**: [https://relatedb.ai/](https://relatedb.ai/)

生成摘要时出错

---

## 42. Paths in Pieces

**原文标题**: Paths in Pieces

**原文链接**: [https://stoppels.ch/2026/11/12/paths-in-pieces.html](https://stoppels.ch/2026/11/12/paths-in-pieces.html)

生成摘要时出错

---

## 43. Show HN: DRS-VPT. Localize a photo in a 3D point cloud without an initial pose

**原文标题**: Show HN: DRS-VPT. Localize a photo in a 3D point cloud without an initial pose

**原文链接**: [https://github.com/ori-drs/drs-vpt](https://github.com/ori-drs/drs-vpt)

生成摘要时出错

---

## 44. Tim Peters has died

**原文标题**: Tim Peters has died

**原文链接**: [https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028)

生成摘要时出错

---

## 45. Show HN: Build a PC in 3D in the Browser

**原文标题**: Show HN: Build a PC in 3D in the Browser

**原文链接**: [https://www.buildcores.com](https://www.buildcores.com)

生成摘要时出错

---

## 46. Vibes Don't Maintain

**原文标题**: Vibes Don't Maintain

**原文链接**: [https://roll.bybacon.com/2026/10/14/vibes-dont-maintain.html](https://roll.bybacon.com/2026/10/14/vibes-dont-maintain.html)

生成摘要时出错

---

## 47. Research taste in history: the importance of learning Babylonian math

**原文标题**: Research taste in history: the importance of learning Babylonian math

**原文链接**: [https://resobscura.substack.com/p/research-taste-in-history-the-importance](https://resobscura.substack.com/p/research-taste-in-history-the-importance)

生成摘要时出错

---

## 48. Hands-on fabrication of 2D material field-effect transistors for the classroom

**原文标题**: Hands-on fabrication of 2D material field-effect transistors for the classroom

**原文链接**: [https://iopscience.iop.org/article/10.1088/1361-6404/aeb51a](https://iopscience.iop.org/article/10.1088/1361-6404/aeb51a)

生成摘要时出错

---

## 49. Mercedes-Benz halts German investments as plant closures loom

**原文标题**: Mercedes-Benz halts German investments as plant closures loom

**原文链接**: [https://www.reuters.com/world/mercedes-benz-halts-german-investments-plant-closures-loom-2026-11-12/](https://www.reuters.com/world/mercedes-benz-halts-german-investments-plant-closures-loom-2026-11-12/)

生成摘要时出错

---

## 50. I'm Working on a FOSS Linux Pinbal Simulation Engine

**原文标题**: I'm Working on a FOSS Linux Pinbal Simulation Engine

**原文链接**: [https://www.getlazarus.org/forums/topic/17/](https://www.getlazarus.org/forums/topic/17/)

生成摘要时出错

---

## 51. Running web sites makes me not want to

**原文标题**: Running web sites makes me not want to

**原文链接**: [https://lowkey.party/running-web-sites-makes-me-not-want-to](https://lowkey.party/running-web-sites-makes-me-not-want-to)

生成摘要时出错

---

## 52. I gave an agent a lakehouse and control of my garden

**原文标题**: I gave an agent a lakehouse and control of my garden

**原文链接**: [https://jatorre.github.io/garden/](https://jatorre.github.io/garden/)

生成摘要时出错

---

## 53. 93% of paint splatters are valid Perl programs (2019)

**原文标题**: 93% of paint splatters are valid Perl programs (2019)

**原文链接**: [https://www.mcmillen.dev/sigbovik/](https://www.mcmillen.dev/sigbovik/)

生成摘要时出错

---

## 54. AWS emulator

**原文标题**: AWS emulator

**原文链接**: [https://github.com/aws/aws-emulator](https://github.com/aws/aws-emulator)

生成摘要时出错

---

## 55. A teacher that made $20M a year making videos for babies

**原文标题**: A teacher that made $20M a year making videos for babies

**原文链接**: [https://www.readfounded.com/p/baby-einstein](https://www.readfounded.com/p/baby-einstein)

生成摘要时出错

---

## 56. Critical RCE Vulnerability in Apache HTTP Server

**原文标题**: Critical RCE Vulnerability in Apache HTTP Server

**原文链接**: [https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability)

生成摘要时出错

---

## 57. Show HN: I built a calendar app that gives each event its own to-do list

**原文标题**: Show HN: I built a calendar app that gives each event its own to-do list

**原文链接**: [https://apps.apple.com/ph/app/daily-planner-tasks-zesfy/id6479947874](https://apps.apple.com/ph/app/daily-planner-tasks-zesfy/id6479947874)

生成摘要时出错

---

## 58. PostgreSQL 18.7, 17.12, 16.16, 15.20, 14.25, and 19 RC 2 Released

**原文标题**: PostgreSQL 18.7, 17.12, 16.16, 15.20, 14.25, and 19 RC 2 Released

**原文链接**: [https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)

生成摘要时出错

---

## 59. Apify Security Incident

**原文标题**: Apify Security Incident

**原文链接**: [https://status.apify.com/incidents/sxd1dj5j6749](https://status.apify.com/incidents/sxd1dj5j6749)

生成摘要时出错

---

## 60. Faster Retrieval for Better, More Efficient RAG

**原文标题**: Faster Retrieval for Better, More Efficient RAG

**原文链接**: [https://machinelearning.apple.com/research/faster-retrieval](https://machinelearning.apple.com/research/faster-retrieval)

生成摘要时出错

---

## 61. "Humble Bundle just killed most of their security through vibecoding"

**原文标题**: "Humble Bundle just killed most of their security through vibecoding"

**原文链接**: [https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/](https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/)

生成摘要时出错

---

## 62. Apple has new Mac app coming to make running local AI models easy

**原文标题**: Apple has new Mac app coming to make running local AI models easy

**原文链接**: [https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

生成摘要时出错

---

## 63. Show HN: AI Red Lines – write down what would make you act on AI

**原文标题**: Show HN: AI Red Lines – write down what would make you act on AI

**原文链接**: [https://yourairedlines.com](https://yourairedlines.com)

生成摘要时出错

---

## 64. Show HN: Yogurt – Free, private, open-source alternative to Granola

**原文标题**: Show HN: Yogurt – Free, private, open-source alternative to Granola

**原文链接**: [https://github.com/FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)

生成摘要时出错

---

## 65. A general purpose Apple Silicon layer for x86-64 PCs

**原文标题**: A general purpose Apple Silicon layer for x86-64 PCs

**原文链接**: [https://github.com/tylertms/Stela](https://github.com/tylertms/Stela)

生成摘要时出错

---

## 66. The internet won't necessarily go dark. It could simply stop working

**原文标题**: The internet won't necessarily go dark. It could simply stop working

**原文链接**: [https://www.washingtonpost.com/opinions/2026/11/12/ai-is-exposing-internets-cybersecurity-vulnerabilities/](https://www.washingtonpost.com/opinions/2026/11/12/ai-is-exposing-internets-cybersecurity-vulnerabilities/)

生成摘要时出错

---

## 67. The largest open-source DLE collection

**原文标题**: The largest open-source DLE collection

**原文链接**: [https://github.com/trizoza/dles/blob/main/assets/daily-games/DLES.md](https://github.com/trizoza/dles/blob/main/assets/daily-games/DLES.md)

生成摘要时出错

---

## 68. A Microsoft 365 outage is hitting users in regions around the world

**原文标题**: A Microsoft 365 outage is hitting users in regions around the world

**原文链接**: [https://globalnews.ca/news/12148204/microsoft-outage-2026/](https://globalnews.ca/news/12148204/microsoft-outage-2026/)

生成摘要时出错

---

## 69. Atuin Threads: All your agent sessions on every machine

**原文标题**: Atuin Threads: All your agent sessions on every machine

**原文链接**: [https://blog.atuin.sh/threads-agent-sessions/](https://blog.atuin.sh/threads-agent-sessions/)

生成摘要时出错

---

## 70. A false smoke alarm almost drowned Jane Street's only NYC datacenter

**原文标题**: A false smoke alarm almost drowned Jane Street's only NYC datacenter

**原文链接**: [https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/)

生成摘要时出错

---

## 71. Huawei releases MACaQ, its internal quantizer for local inference

**原文标题**: Huawei releases MACaQ, its internal quantizer for local inference

**原文链接**: [https://github.com/huawei-csl/MACaQ](https://github.com/huawei-csl/MACaQ)

生成摘要时出错

---

## 72. A click-fraud bot led me to 5,552 GitHub accounts tied to public inboxes

**原文标题**: A click-fraud bot led me to 5,552 GitHub accounts tied to public inboxes

**原文链接**: [https://shmulc.substack.com/p/click-fraud-bot-github-public-inbox-accounts](https://shmulc.substack.com/p/click-fraud-bot-github-public-inbox-accounts)

生成摘要时出错

---

## 73. Gemini Decisions API

**原文标题**: Gemini Decisions API

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

生成摘要时出错

---

## 74. Show HN: Fable52.games – Play and inspect Fable 5.2 single-file HTML games

**原文标题**: Show HN: Fable52.games – Play and inspect Fable 5.2 single-file HTML games

**原文链接**: [https://fable52.games](https://fable52.games)

生成摘要时出错

---

## 75. Roadside investigations of psyllids, ants and eucs

**原文标题**: Roadside investigations of psyllids, ants and eucs

**原文链接**: [https://bencology.bearblog.dev/eucalypt-psyllids-meat-ants/](https://bencology.bearblog.dev/eucalypt-psyllids-meat-ants/)

生成摘要时出错

---

## 76. Secure Exclaves and Ambient Sensing

**原文标题**: Secure Exclaves and Ambient Sensing

**原文链接**: [https://security.apple.com/blog/secure-exclaves/](https://security.apple.com/blog/secure-exclaves/)

生成摘要时出错

---

## 77. Gemini 4 Hydrogen

**原文标题**: Gemini 4 Hydrogen

**原文链接**: [https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen](https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen)

生成摘要时出错

---

## 78. Grote Reber and the 'Square Kilometre Array' Near Bothwell, Tasmania (2017)

**原文标题**: Grote Reber and the 'Square Kilometre Array' Near Bothwell, Tasmania (2017)

**原文链接**: [https://www.researchgate.net/publication/319702287_THE_HISTORY_OF_EARLY_LOW_FREQUENCY_RADIO_ASTRONOMY_IN_AUSTRALIA_8_GROTE_REBER_AND_THE_%27SQUARE_KILOMETRE_ARRAY%27_NEAR_BOTHWELL_TASMANIA_IN_THE_1960s_AND_1970s](https://www.researchgate.net/publication/319702287_THE_HISTORY_OF_EARLY_LOW_FREQUENCY_RADIO_ASTRONOMY_IN_AUSTRALIA_8_GROTE_REBER_AND_THE_%27SQUARE_KILOMETRE_ARRAY%27_NEAR_BOTHWELL_TASMANIA_IN_THE_1960s_AND_1970s)

生成摘要时出错

---

## 79. Washing dishes at Denny's to rockstar of AI, the rise and fall of Jensen Huang

**原文标题**: Washing dishes at Denny's to rockstar of AI, the rise and fall of Jensen Huang

**原文链接**: [https://www.theguardian.com/technology/2026/nov/12/rise-and-fall-of-nvidia-ceo-jensen-huang-profile](https://www.theguardian.com/technology/2026/nov/12/rise-and-fall-of-nvidia-ceo-jensen-huang-profile)

生成摘要时出错

---

## 80. Show HN: Aircad – Professional drafting and 3D modeling in the browser

**原文标题**: Show HN: Aircad – Professional drafting and 3D modeling in the browser

**原文链接**: [https://aircad.com](https://aircad.com)

生成摘要时出错

---

## 81. Lean Grimoire

**原文标题**: Lean Grimoire

**原文链接**: [https://terrytao.wordpress.com/2026/11/11/lean-grimoire/](https://terrytao.wordpress.com/2026/11/11/lean-grimoire/)

生成摘要时出错

---

## 82. Palantir's Karp says he and the company's products are actually 'progressive'

**原文标题**: Palantir's Karp says he and the company's products are actually 'progressive'

**原文链接**: [https://www.theregister.com/software/2026/11/12/palantirs-karp-takes-a-sharp-left-turn-says-he-and-the-companys-products-are-actually-progressive/5309441](https://www.theregister.com/software/2026/11/12/palantirs-karp-takes-a-sharp-left-turn-says-he-and-the-companys-products-are-actually-progressive/5309441)

生成摘要时出错

---

## 83. Legocam: My Lego webcam from 2000, working on a modern Mac

**原文标题**: Legocam: My Lego webcam from 2000, working on a modern Mac

**原文链接**: [https://blog.benjamin.ie/legocam](https://blog.benjamin.ie/legocam)

生成摘要时出错

---

## 84. Hugging Face CEO vows to keep fighting for open-source AI

**原文标题**: Hugging Face CEO vows to keep fighting for open-source AI

**原文链接**: [https://techcrunch.com/2026/11/12/hugging-face-ceo-vows-to-keep-fighting-for-open-source-ai-after-jensen-huangs-exit/](https://techcrunch.com/2026/11/12/hugging-face-ceo-vows-to-keep-fighting-for-open-source-ai-after-jensen-huangs-exit/)

生成摘要时出错

---

## 85. We need more goat sacrifices

**原文标题**: We need more goat sacrifices

**原文链接**: [https://www.experimental-history.com/p/we-need-more-goat-sacrifices](https://www.experimental-history.com/p/we-need-more-goat-sacrifices)

生成摘要时出错

---

## 86. 20 Years of Pyrolog

**原文标题**: 20 Years of Pyrolog

**原文链接**: [https://pypy.org/posts/2026/11/20-years-of-pyrolog.html](https://pypy.org/posts/2026/11/20-years-of-pyrolog.html)

生成摘要时出错

---

## 87. Show HN: I recreated Papers Please but you're deciding which YC startups to fund

**原文标题**: Show HN: I recreated Papers Please but you're deciding which YC startups to fund

**原文链接**: [https://termsheetplease.com/](https://termsheetplease.com/)

生成摘要时出错

---

## 88. United Airlines bans AI agents from booking flights on behalf of travelers

**原文标题**: United Airlines bans AI agents from booking flights on behalf of travelers

**原文链接**: [https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

生成摘要时出错

---

## 89. Binance lost $6.43B from a fake job interview

**原文标题**: Binance lost $6.43B from a fake job interview

**原文链接**: [https://rekt.news/binance-rekt](https://rekt.news/binance-rekt)

生成摘要时出错

---

## 90. The Confidential Payments Meta and TikTok Made to Addicted Teens

**原文标题**: The Confidential Payments Meta and TikTok Made to Addicted Teens

**原文链接**: [https://www.bloomberg.com/news/articles/2026-11-12/meta-tiktok-payouts-reveal-cost-to-settle-social-media-addiction-suits](https://www.bloomberg.com/news/articles/2026-11-12/meta-tiktok-payouts-reveal-cost-to-settle-social-media-addiction-suits)

生成摘要时出错

---

## 91. Lock Your GitHub Actions

**原文标题**: Lock Your GitHub Actions

**原文链接**: [https://hugovk.dev/blog/2026/lock-github-actions/](https://hugovk.dev/blog/2026/lock-github-actions/)

生成摘要时出错

---

## 92. Foldable Flight: The Best Paper Airplanes

**原文标题**: Foldable Flight: The Best Paper Airplanes

**原文链接**: [https://www.foldableflight.com](https://www.foldableflight.com)

生成摘要时出错

---

## 93. Darling Development Update – Q4 2026

**原文标题**: Darling Development Update – Q4 2026

**原文链接**: [https://blog.darlinghq.org/2026/11/08/development-update-q4-2026/](https://blog.darlinghq.org/2026/11/08/development-update-q4-2026/)

生成摘要时出错

---

## 94. Slavdom Unearthed: Marian Wawrzeniecki's Neopagan Paintings (1891–1923)

**原文标题**: Slavdom Unearthed: Marian Wawrzeniecki's Neopagan Paintings (1891–1923)

**原文链接**: [https://publicdomainreview.org/collection/marian-wawrzeniecki/](https://publicdomainreview.org/collection/marian-wawrzeniecki/)

生成摘要时出错

---

## 95. 30 years of Internet transfers with curl

**原文标题**: 30 years of Internet transfers with curl

**原文链接**: [https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/](https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/)

生成摘要时出错

---

## 96. Smart home devices should work without the internet

**原文标题**: Smart home devices should work without the internet

**原文链接**: [https://docodethatmatters.com/home-automation-overnight-success/](https://docodethatmatters.com/home-automation-overnight-success/)

生成摘要时出错

---

## 97. A Brief History of Sierra Online (2017)

**原文标题**: A Brief History of Sierra Online (2017)

**原文链接**: [https://retrofreakreviews.com/2017/01/30/sierra-retrospective/](https://retrofreakreviews.com/2017/01/30/sierra-retrospective/)

生成摘要时出错

---

## 98. The hardest notes to find on the guitar

**原文标题**: The hardest notes to find on the guitar

**原文链接**: [https://www.gitori.com/blog/articles/hardest-notes-on-the-guitar-fretboard](https://www.gitori.com/blog/articles/hardest-notes-on-the-guitar-fretboard)

生成摘要时出错

---

## 99. Emacs in the Age of Magic

**原文标题**: Emacs in the Age of Magic

**原文链接**: [https://commandlinesystems.com/magic.txt](https://commandlinesystems.com/magic.txt)

生成摘要时出错

---

## 100. How to make a CNC plasma cutter with high-frequency start

**原文标题**: How to make a CNC plasma cutter with high-frequency start

**原文链接**: [https://incoherency.co.uk/blog/stories/cnc-plasma-cutter.html](https://incoherency.co.uk/blog/stories/cnc-plasma-cutter.html)

生成摘要时出错

---

