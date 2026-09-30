# Hacker News 热门文章摘要 (2026-09-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 双子座 4 氩

**原文标题**: Gemini 4 Argon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

Google DeepMind has announced **Gemini 4 Argon**, a new frontier AI model engineered for deep reasoning and complex, long-horizon professional workflows. Released on September 30, 2026, the model excels in software engineering, enterprise knowledge work (legal and finance), and cybersecurity defense.

**Key Technical Advancements**
The model features an industry-leading **1-million-token output limit** (up from 64K), allowing it to generate massive, multi-step solutions in a single trajectory. Internally, Google has already utilized Argon to optimize quantum algorithms, save over 300 TiB of data center memory, and migrate hundreds of thousands of lines of C++ code to memory-safe Rust. 

**Performance and Benchmarks**
Argon sets new standards across several industry benchmarks:
*   **Coding:** 77.9% on DeepSWE v1.1.
*   **Economic Impact:** Leads the Vals Index for finance, legal, and tax work.
*   **Visual/Video:** 91.7% on LVBench for long video understanding.
*   **Cybersecurity:** Ties for first on CWE-bench v1 for remediating security vulnerabilities.

**Cybersecurity and Safety**
Through the **Fairwind Program**, Argon is being rolled out to trusted defenders without certain cyber guardrails to enable autonomous vulnerability patching. To ensure safety for the general public, Google is employing a phased release, working with the U.S. government on pre-release access, and implementing advanced monitoring for model misalignment and prompt injections.

**Pricing and Availability**
Argon will launch at an introductory price of **$2 per million input tokens** and **$10 per million output tokens**. While currently limited to trusted testers and cyber defenders, it will soon expand to developers, enterprise customers, and Google AI Ultra subscribers.

---

## 2. Surprisingly Complex Waves Reveal the Brain's Inner Workings

**原文标题**: Surprisingly Complex Waves Reveal the Brain's Inner Workings

**原文链接**: [https://www.quantamagazine.org/surprisingly-complex-waves-reveal-the-brains-inner-workings-20260930/](https://www.quantamagazine.org/surprisingly-complex-waves-reveal-the-brains-inner-workings-20260930/)

生成摘要时出错

---

## 3. EDG C++ front-end goes public

**原文标题**: EDG C++ front-end goes public

**原文链接**: [https://edgcpp.org/#transition](https://edgcpp.org/#transition)

生成摘要时出错

---

## 4. Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents

**原文标题**: Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents

**原文链接**: [https://github.com/magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)

生成摘要时出错

---

## 5. 边缘函数提速 5 倍：从 V8 Isolate 迁移至 Firecracker MicroVMs

**原文标题**: 5x faster Edge Functions: V8 isolates to Firecracker MicroVMs

**原文链接**: [https://www.netlify.com/blog/edge-functions-firecracker-microvms/](https://www.netlify.com/blog/edge-functions-firecracker-microvms/)

Netlify 重构了其边缘函数（Edge Functions）基础设施，从托管的 V8 isolate 转向运行在自有边缘网络上的 Firecracker MicroVM。这一转变带来了 5 倍的性能提升，中值延迟从 25–40ms 降至仅 5–6ms，同时保持了 99.998% 的可用性。

**关键技术改进：**
*   **MicroVM 架构：** 通过与 Unikraft 合作，Netlify 现在采用可在 1 毫秒内启动的 Firecracker MicroVM。利用快照和内存映射技术，函数在空闲时可“缩减至零”，并在收到请求时即时恢复，仅通过 EROFS 镜像读取函数包的必要部分。
*   **增强的隔离性：** 与 V8 isolate 不同，MicroVM 为每次部署提供专用的 Linux 环境。这能防止受损的函数影响其他客户或底层平台，显著提升了安全性。
*   **优化路由：** 边缘节点使用“汇合哈希（rendezvous hashing）”将请求路由到特定的计算节点。这使函数能保持“热启动”并缓存在磁盘上，同时允许系统在流量激增时灵活调整粘性，以防止出现热点。
*   **开发者体验：** 此次过渡对用户是无缝的；现有的代码、npm 包和 Node 内置模块无需修改即可直接运行。

**未来展望：**
通过将计算能力整合进自有网络，Netlify 正在消除以往的限制。未来的优势包括支持完整的 npm 包（包括原生二进制文件）、更高的 CPU 和内存限制，以及对网络路径更精准的控制。这一新架构为 Netlify 持续提升复杂边缘计算任务的性能上限奠定了基础。

---

## 6. Halfspace：基于距离场的实验性实体建模 IDE

**原文标题**: Halfspace experimental IDE for solid modeling with distance fields

**原文链接**: [https://www.mattkeeter.com/projects/halfspace/](https://www.mattkeeter.com/projects/halfspace/)

**Halfspace** 是一款基于 **Fidget** 几何内核构建的实验性集成开发环境 (IDE)，专用于利用距离场进行实体建模。该工具由一位具有 CAD/CAM 背景的开发者设计，专注于创建具有明确内外边界的“实体”模型，适用于物理制造和 3D 打印。

该项目旨在弥合底层隐式表面与高层抽象之间的鸿沟。与传统的构造实体几何 (CSG) 工具不同，Halfspace 将底层的距离场置于核心位置。这种透明度允许用户诊断并修复诸如“跳跃”不连续性和非均匀梯度等问题，这些问题通常会导致着色效果差和网格质量低。

**主要特性与技术规格包括：**
*   **跨平台性能：** Halfspace 使用 **Rust** 构建，兼顾原生和 Web 平台。它利用 **WebGPU (wgpu)** 进行 GPU 加速的光栅化和着色，确保即使在浏览器中通过 WebAssembly 运行也能获得实时性能。
*   **混合工作流：** 用户可以结合使用标准基元库和手写脚本 (**Rhai**) 来逐步构建模型。
*   **Fidget 内核集成：** 该 IDE 作为 Fidget 内核的试验场，推动了其 GPU 渲染和 API 设计的改进。
*   **输出：** 模型可导出为高分辨率图像或三角网格。

Halfspace 基于 **MPLv2 许可证**开源，目前定位为“展示型应用”和实验性工具。虽然作者提醒不要将其用于关键任务，但它代表了一种将隐式表面建模变得对个人化制造更加直观且高效的深入探索。

---

## 7. A brief history of the Bloomberg terminal

**原文标题**: A brief history of the Bloomberg terminal

**原文链接**: [https://spectrum.ieee.org/bloomberg-terminal](https://spectrum.ieee.org/bloomberg-terminal)

生成摘要时出错

---

## 8. 你说过不使用 MCP。

**原文标题**: You said no MCP

**原文链接**: [https://earendil.com/posts/you-said-no-mcp/](https://earendil.com/posts/you-said-no-mcp/)

Earendil Engineering 宣布“Pi”现已原生支持**模型上下文协议 (MCP)**，这标志着该公司此前立场的重大转变。这一转变是由 MCP 的演进驱动的，同时也源于公司意识到 MCP 的要求与 Pi 对健壮解释器沙箱的需求高度契合。

此次更新的核心要点包括：

*   **集成优于扩展**：MCP 未被作为可选扩展，而是直接集成到核心中以支持“代码模式 (Codemode)”。这使得 Earendil 能够推动 MCP 标准向结构化数据和智能工具发现方向发展，而非仅停留在简单的文本响应。
*   **代码模式 (Codemode)**：这是一个由 WASM 驱动的新型 JavaScript 沙箱，运行在智能体循环中受信任的“驾驭端 (harness)”。它允许 AI 高效地编排、协调和组合多个工具调用。由于它在驾驭端运行，其状态保存在会话记录中，而非文件系统中。
*   **增强的组合能力**：Codemode 解决了 MCP 长期以来在“组合性”方面的难题。智能体现可以使用 JavaScript 将不同工具连接在一起——例如将 Linear MCP 服务器与“Jev”（一种类型安全分类器）相结合——以执行复杂任务（如对数百个 Issue 进行情感分析），且不会耗尽上下文窗口。
*   **现代大语言模型支持**：通过为工具可用性提供更完善的元数据，此次更新让 Pi 为更先进的模型能力（如延迟工具加载和推理层级的变化）做好了准备。

最终，Earendil Engineering 旨在将 MCP 从一个简单的工具堆砌机制转型为类似于 OpenAPI 的功能性系统，使智能体能够在安全的环境中以“类 bash”的高效方式操作结构化数据。

---

## 9. Gitea 28.0

**原文标题**: Gitea 28.0

**原文链接**: [https://blog.gitea.com/release-of-28.0.0/](https://blog.gitea.com/release-of-28.0.0/)

2026年8月29日，用户 **bircni** 宣布发布 **Gitea 1.27.3**。尽管公告标题提到了“Gitea 28.0”，但核心内容明确指出该更新版本为 1.27.3。所提供的文本仅作为发布的简要通知，未详细列出具体的功能更新或错误修复。

---

## 10. I could've accessed 17T Microsoft records

**原文标题**: I could've accessed 17T Microsoft records

**原文链接**: [https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records](https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records)

生成摘要时出错

---

## 11. Gemini 4 Argon (High): Intelligence, Performance and Price Analysis

**原文标题**: Gemini 4 Argon (High): Intelligence, Performance and Price Analysis

**原文链接**: [https://artificialanalysis.ai/models/gemini-4-argon](https://artificialanalysis.ai/models/gemini-4-argon)

生成摘要时出错

---

## 12. Carnegie Mellon University Announces Historic $3B Gift from Ken Griffin

**原文标题**: Carnegie Mellon University Announces Historic $3B Gift from Ken Griffin

**原文链接**: [https://www.cmu.edu/news/stories/archives/2026/september/carnegie-mellon-university-announces-historic-3-billion-gift-from-ken-griffin-pioneering-a-new-model](https://www.cmu.edu/news/stories/archives/2026/september/carnegie-mellon-university-announces-historic-3-billion-gift-from-ken-griffin-pioneering-a-new-model)

生成摘要时出错

---

## 13. The last time my family was replaced by technology

**原文标题**: The last time my family was replaced by technology

**原文链接**: [https://manuel.darcemont.fr/posts/the-last-time-my-family-was-replaced-by-technology/](https://manuel.darcemont.fr/posts/the-last-time-my-family-was-replaced-by-technology/)

生成摘要时出错

---

## 14. What TLA+ can and can't check

**原文标题**: What TLA+ can and can't check

**原文链接**: [https://buttondown.com/hillelwayne/archive/what-tla-can-and-cant-check/](https://buttondown.com/hillelwayne/archive/what-tla-can-and-cant-check/)

生成摘要时出错

---

## 15. Bild AI (YC W25) Is Hiring a Founding Product Engineer

**原文标题**: Bild AI (YC W25) Is Hiring a Founding Product Engineer

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/dAbC3Gd-founding-product-engineer](https://www.ycombinator.com/companies/bild-ai/jobs/dAbC3Gd-founding-product-engineer)

生成摘要时出错

---

## 16. Claude Says

**原文标题**: Claude Says

**原文链接**: [https://ohhfishal.net/Posts/claude](https://ohhfishal.net/Posts/claude)

生成摘要时出错

---

## 17. Doing a Machine Learning PhD While Working in Japan

**原文标题**: Doing a Machine Learning PhD While Working in Japan

**原文链接**: [https://www.tokyodev.com/articles/doing-a-machine-learning-phd-while-working-in-japan](https://www.tokyodev.com/articles/doing-a-machine-learning-phd-while-working-in-japan)

生成摘要时出错

---

## 18. Commit description as a thinking tool

**原文标题**: Commit description as a thinking tool

**原文链接**: [https://yedhu.me/posts/commit-description-as-a-thinking-tool/](https://yedhu.me/posts/commit-description-as-a-thinking-tool/)

生成摘要时出错

---

## 19. SDF vs. MSDF vs. Slug: GPU Text Rendering

**原文标题**: SDF vs. MSDF vs. Slug: GPU Text Rendering

**原文链接**: [https://alphapixeldev.com/sdf-vs-msdf-vs-slug-vs-rive-gpu-text-rendering/](https://alphapixeldev.com/sdf-vs-msdf-vs-slug-vs-rive-gpu-text-rendering/)

生成摘要时出错

---

## 20. Understanding the Dual Polytope for Hull Simplification

**原文标题**: Understanding the Dual Polytope for Hull Simplification

**原文链接**: [https://cairnc.github.io/posts/understanding-the-dual-polytope/](https://cairnc.github.io/posts/understanding-the-dual-polytope/)

生成摘要时出错

---

## 21. SDF Public Access Unix System ... est. 1987

**原文标题**: SDF Public Access Unix System ... est. 1987

**原文链接**: [https://sdf.org/](https://sdf.org/)

生成摘要时出错

---

## 22. Moist-Electric Wallpaper for Indoor Energy Harvesting and Humidity Management

**原文标题**: Moist-Electric Wallpaper for Indoor Energy Harvesting and Humidity Management

**原文链接**: [https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.71603](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.71603)

生成摘要时出错

---

## 23. Dear Software Makers

**原文标题**: Dear Software Makers

**原文链接**: [https://blog.jim-nielsen.com/2026/dear-software-makers/](https://blog.jim-nielsen.com/2026/dear-software-makers/)

生成摘要时出错

---

## 24. CS240 AI Cheating Retrospective

**原文标题**: CS240 AI Cheating Retrospective

**原文链接**: [https://turkeyland.net/thoughts/ai.php](https://turkeyland.net/thoughts/ai.php)

生成摘要时出错

---

## 25. LinkedIn Larpmaxxing

**原文标题**: LinkedIn Larpmaxxing

**原文链接**: [https://hereticpleb.vercel.app/blog/linkedin-larpmaxxing/](https://hereticpleb.vercel.app/blog/linkedin-larpmaxxing/)

生成摘要时出错

---

## 26. America.gov goes crazy on "play Minecraft"

**原文标题**: America.gov goes crazy on "play Minecraft"

**原文链接**: [https://america.gov/chat](https://america.gov/chat)

生成摘要时出错

---

## 27. Dear User, email is here to stay

**原文标题**: Dear User, email is here to stay

**原文链接**: [https://github.com/tursomari/machtiani/tree/main](https://github.com/tursomari/machtiani/tree/main)

生成摘要时出错

---

## 28. Reverse-engineering a $35 backup camera display (AMT630A)

**原文标题**: Reverse-engineering a $35 backup camera display (AMT630A)

**原文链接**: [https://github.com/mogrinz/AMT630A](https://github.com/mogrinz/AMT630A)

生成摘要时出错

---

## 29. Functional Ultrasound Imaging from Scratch

**原文标题**: Functional Ultrasound Imaging from Scratch

**原文链接**: [https://www.neuroai.science/p/functional-ultrasound-imaging-from](https://www.neuroai.science/p/functional-ultrasound-imaging-from)

生成摘要时出错

---

## 30. Show HN: Ledge.sh – Runnable Markdown Notes

**原文标题**: Show HN: Ledge.sh – Runnable Markdown Notes

**原文链接**: [https://ledge.sh](https://ledge.sh)

生成摘要时出错

---

## 31. Show HN: JBR-001 – An open-source 3D printable desktop robot

**原文标题**: Show HN: JBR-001 – An open-source 3D printable desktop robot

**原文链接**: [https://projecthub.arduino.cc/syntheticaidata/jbr-001-a-desktop-companion-robot-powered-by-arduino-uno-q-b11c96](https://projecthub.arduino.cc/syntheticaidata/jbr-001-a-desktop-companion-robot-powered-by-arduino-uno-q-b11c96)

生成摘要时出错

---

## 32. Burning Man death rates – A short lesson in statistics

**原文标题**: Burning Man death rates – A short lesson in statistics

**原文链接**: [https://ihavenapkinthoughts.substack.com/p/burning-man-death-rates-a-short-lesson](https://ihavenapkinthoughts.substack.com/p/burning-man-death-rates-a-short-lesson)

生成摘要时出错

---

## 33. Solving Factorio Quality

**原文标题**: Solving Factorio Quality

**原文链接**: [https://exyr.org/2026/solving-factorio-quality/](https://exyr.org/2026/solving-factorio-quality/)

生成摘要时出错

---

## 34. Getting out of the way: my robotics crash course

**原文标题**: Getting out of the way: my robotics crash course

**原文链接**: [https://thisismypersonalblog.com/posts/2026-09-25-getting-out-of-the-way/](https://thisismypersonalblog.com/posts/2026-09-25-getting-out-of-the-way/)

生成摘要时出错

---

## 35. Recursive `Make` and `-J`

**原文标题**: Recursive `Make` and `-J`

**原文链接**: [https://quuxplusone.github.io/blog/2026/09/30/recursive-make-j/](https://quuxplusone.github.io/blog/2026/09/30/recursive-make-j/)

生成摘要时出错

---

## 36. Anthropic's IPO Prospectus Is a Fucking Doozy

**原文标题**: Anthropic's IPO Prospectus Is a Fucking Doozy

**原文链接**: [https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus](https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus)

生成摘要时出错

---

## 37. Vermont replacing power plants with home batteries

**原文标题**: Vermont replacing power plants with home batteries

**原文链接**: [https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms)

生成摘要时出错

---

## 38. Mathematical Origami

**原文标题**: Mathematical Origami

**原文链接**: [https://mathigon.org/origami](https://mathigon.org/origami)

生成摘要时出错

---

## 39. NASA asked several former SR-71A staffers to help secret restart

**原文标题**: NASA asked several former SR-71A staffers to help secret restart

**原文链接**: [https://aviationweek.com/defense/aircraft-propulsion/nasa-asked-several-former-sr-71a-staffers-help-secret-restart](https://aviationweek.com/defense/aircraft-propulsion/nasa-asked-several-former-sr-71a-staffers-help-secret-restart)

生成摘要时出错

---

## 40. Show HN: Dental Scope – Interactive 3D dental anatomy

**原文标题**: Show HN: Dental Scope – Interactive 3D dental anatomy

**原文链接**: [https://dental-scope.com/](https://dental-scope.com/)

生成摘要时出错

---

## 41. Chompi portable sampler instrument is now open-source (hardware and software)

**原文标题**: Chompi portable sampler instrument is now open-source (hardware and software)

**原文链接**: [https://www.chompiclub.com/opensource](https://www.chompiclub.com/opensource)

生成摘要时出错

---

## 42. Aurora PostgreSQL now supports querying of Apache Iceberg and Parquet data

**原文标题**: Aurora PostgreSQL now supports querying of Apache Iceberg and Parquet data

**原文链接**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aurora-postgresql-query-apache-iceberg-and-parquet/](https://aws.amazon.com/about-aws/whats-new/2026/09/aurora-postgresql-query-apache-iceberg-and-parquet/)

生成摘要时出错

---

## 43. Show HN: A working 3D model of an Enigma machine

**原文标题**: Show HN: A working 3D model of an Enigma machine

**原文链接**: [https://enigma.design](https://enigma.design)

生成摘要时出错

---

## 44. Denying Insulin and Meds: Disturbing Pictures of Neglect in ICE Mortality Report

**原文标题**: Denying Insulin and Meds: Disturbing Pictures of Neglect in ICE Mortality Report

**原文链接**: [https://prospect.org/2026/09/30/ice-neglect-immigration-deportation-mortality-reviews/](https://prospect.org/2026/09/30/ice-neglect-immigration-deportation-mortality-reviews/)

生成摘要时出错

---

## 45. Show HN: Strata – an expressive semantic layer that can say no to your LLM

**原文标题**: Show HN: Strata – an expressive semantic layer that can say no to your LLM

**原文链接**: [https://strata.do/](https://strata.do/)

生成摘要时出错

---

## 46. Energy Timelines Photovoltaic

**原文标题**: Energy Timelines Photovoltaic

**原文链接**: [https://www.eia.gov/kids/history-of-energy/timelines/photovoltaic.php](https://www.eia.gov/kids/history-of-energy/timelines/photovoltaic.php)

生成摘要时出错

---

## 47. Great Dirhombicosidodecahedron ("Miller's Monster")

**原文标题**: Great Dirhombicosidodecahedron ("Miller's Monster")

**原文链接**: [https://www.software3d.com/MillersMonster.php](https://www.software3d.com/MillersMonster.php)

生成摘要时出错

---

## 48. Livenerf: Has Opus 5.5 been nerfed yet?

**原文标题**: Livenerf: Has Opus 5.5 been nerfed yet?

**原文链接**: [https://github.com/ninjahawk/livenerf](https://github.com/ninjahawk/livenerf)

生成摘要时出错

---

## 49. Show HN: Real-time Solar System with 526k asteroids and all tracked satellites

**原文标题**: Show HN: Real-time Solar System with 526k asteroids and all tracked satellites

**原文链接**: [https://space.bl2.net/](https://space.bl2.net/)

生成摘要时出错

---

## 50. Bologna Bottle

**原文标题**: Bologna Bottle

**原文链接**: [https://en.wikipedia.org/wiki/Bologna_bottle](https://en.wikipedia.org/wiki/Bologna_bottle)

生成摘要时出错

---

## 51. Phyllotaxis: An audio-reactive LED display

**原文标题**: Phyllotaxis: An audio-reactive LED display

**原文链接**: [https://jagi.studio/posts/phyllotaxis/](https://jagi.studio/posts/phyllotaxis/)

生成摘要时出错

---

## 52. U.S. postal inspectors shut down website selling counterfeit postage labels

**原文标题**: U.S. postal inspectors shut down website selling counterfeit postage labels

**原文链接**: [https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/)

生成摘要时出错

---

## 53. India restores ancient water systems (stepwells)

**原文标题**: India restores ancient water systems (stepwells)

**原文链接**: [https://www.bbc.com/future/article/20260820-india-is-turning-to-ancient-water-systems-as-modern-ones-run-dry](https://www.bbc.com/future/article/20260820-india-is-turning-to-ancient-water-systems-as-modern-ones-run-dry)

生成摘要时出错

---

## 54. Google Grapples with Employee Skepticism About New Gemini Model

**原文标题**: Google Grapples with Employee Skepticism About New Gemini Model

**原文链接**: [https://www.bloomberg.com/news/articles/2026-09-30/google-grapples-with-employee-skepticism-about-new-gemini-model](https://www.bloomberg.com/news/articles/2026-09-30/google-grapples-with-employee-skepticism-about-new-gemini-model)

生成摘要时出错

---

## 55. Show HN: Parrot – Open-Source Smart Meeting Recorder with Co-Pilot on Mac

**原文标题**: Show HN: Parrot – Open-Source Smart Meeting Recorder with Co-Pilot on Mac

**原文链接**: [https://openparrot.app](https://openparrot.app)

生成摘要时出错

---

## 56. Floppy Emu Hardware Failure Analysis Results

**原文标题**: Floppy Emu Hardware Failure Analysis Results

**原文链接**: [https://www.bigmessowires.com/2026/09/29/floppy-emu-hardware-failure-analysis-results/](https://www.bigmessowires.com/2026/09/29/floppy-emu-hardware-failure-analysis-results/)

生成摘要时出错

---

## 57. Language models for text classification: From bag-of-words to Jev

**原文标题**: Language models for text classification: From bag-of-words to Jev

**原文链接**: [https://magazine.sebastianraschka.com/p/classifier-history-and-jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev)

生成摘要时出错

---

## 58. Reddit will block Old.Reddit.com from people who haven't used it in 6 months

**原文标题**: Reddit will block Old.Reddit.com from people who haven't used it in 6 months

**原文链接**: [https://arstechnica.com/gadgets/2026/09/reddit-will-block-old-reddit-com-from-people-who-havent-used-it-in-6-months/](https://arstechnica.com/gadgets/2026/09/reddit-will-block-old-reddit-com-from-people-who-havent-used-it-in-6-months/)

生成摘要时出错

---

## 59. Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers

**原文标题**: Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers

**原文链接**: [https://www.phoronix.com/news/Branch-Target-Reuse-BTR](https://www.phoronix.com/news/Branch-Target-Reuse-BTR)

生成摘要时出错

---

## 60. The Ethernet spec was first drafted on this day in 1980

**原文标题**: The Ethernet spec was first drafted on this day in 1980

**原文链接**: [https://www.tomshardware.com/networking/the-ethernet-spec-was-first-drafted-on-this-day-in-1980-dec-intel-and-xerox-defined-the-standard-several-years-before-the-internet-existed](https://www.tomshardware.com/networking/the-ethernet-spec-was-first-drafted-on-this-day-in-1980-dec-intel-and-xerox-defined-the-standard-several-years-before-the-internet-existed)

生成摘要时出错

---

## 61. RSS Feeds for Last.fm

**原文标题**: RSS Feeds for Last.fm

**原文链接**: [https://lfm.xiffy.nl/](https://lfm.xiffy.nl/)

生成摘要时出错

---

## 62. FTC opens probe into AI giants including Anthropic and OpenAI

**原文标题**: FTC opens probe into AI giants including Anthropic and OpenAI

**原文链接**: [https://www.reuters.com/business/ftc-opens-probe-into-ai-giants-including-anthropic-openai-new-york-post-reports-2026-09-30/](https://www.reuters.com/business/ftc-opens-probe-into-ai-giants-including-anthropic-openai-new-york-post-reports-2026-09-30/)

生成摘要时出错

---

## 63. Testing WebGPU data layouts with Facet

**原文标题**: Testing WebGPU data layouts with Facet

**原文链接**: [https://www.mattkeeter.com/blog/2026-08-23-wgpu-facet/](https://www.mattkeeter.com/blog/2026-08-23-wgpu-facet/)

生成摘要时出错

---

## 64. GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文标题**: GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文链接**: [https://openai.com/index/introducing-gpt-6-1-sol/](https://openai.com/index/introducing-gpt-6-1-sol/)

生成摘要时出错

---

## 65. Adding Giscus to Your Hugo Site – Hayden's Blog

**原文标题**: Adding Giscus to Your Hugo Site – Hayden's Blog

**原文链接**: [https://blog.mrhaydendp.com/posts/giscus-hugo/](https://blog.mrhaydendp.com/posts/giscus-hugo/)

生成摘要时出错

---

## 66. Show HN: Using 2D DFT, dithering, etc. to maximize eInk manga image quality

**原文标题**: Show HN: Using 2D DFT, dithering, etc. to maximize eInk manga image quality

**原文链接**: [https://github.com/ciromattia/kcc](https://github.com/ciromattia/kcc)

生成摘要时出错

---

## 67. When oil prices spike, where does the money go?

**原文标题**: When oil prices spike, where does the money go?

**原文链接**: [https://theconversation.com/when-oil-prices-spike-where-does-the-money-go-280763](https://theconversation.com/when-oil-prices-spike-where-does-the-money-go-280763)

生成摘要时出错

---

## 68. Los Alamos Bets on Eniac: Nuclear Monte Carlo Simulations, 1947–1948 [pdf]

**原文标题**: Los Alamos Bets on Eniac: Nuclear Monte Carlo Simulations, 1947–1948 [pdf]

**原文链接**: [https://www.tomandmaria.com/Tom/Writing/LosAlamosBetsOnENIAC.pdf](https://www.tomandmaria.com/Tom/Writing/LosAlamosBetsOnENIAC.pdf)

生成摘要时出错

---

## 69. Dots: Always-on agents

**原文标题**: Dots: Always-on agents

**原文链接**: [https://openai.com/index/introducing-dots/](https://openai.com/index/introducing-dots/)

生成摘要时出错

---

## 70. Needed 1+1, built a functional programming language

**原文标题**: Needed 1+1, built a functional programming language

**原文链接**: [https://hereticpleb.vercel.app/blog/needed-one-plus-one/](https://hereticpleb.vercel.app/blog/needed-one-plus-one/)

生成摘要时出错

---

## 71. Before pixels: Modular industrial dashboards

**原文标题**: Before pixels: Modular industrial dashboards

**原文链接**: [https://unsung.aresluna.org/before-pixels-modular-industrial-dashboards/](https://unsung.aresluna.org/before-pixels-modular-industrial-dashboards/)

生成摘要时出错

---

## 72. America.gov

**原文标题**: America.gov

**原文链接**: [https://america.gov/](https://america.gov/)

生成摘要时出错

---

## 73. The Cuckoo's Egg (Book)

**原文标题**: The Cuckoo's Egg (Book)

**原文链接**: [https://en.wikipedia.org/wiki/The_Cuckoo%27s_Egg_(book)](https://en.wikipedia.org/wiki/The_Cuckoo%27s_Egg_(book))

生成摘要时出错

---

## 74. NAND-16: a computer built from 277,248 NAND gates

**原文标题**: NAND-16: a computer built from 277,248 NAND gates

**原文链接**: [https://somethingbig.ai/computer](https://somethingbig.ai/computer)

生成摘要时出错

---

## 75. Japan officially overhauls permanent residency rules

**原文标题**: Japan officially overhauls permanent residency rules

**原文链接**: [https://www.japantimes.co.jp/news/2026/10/01/japan/permanent-residency-guidelines-revision/](https://www.japantimes.co.jp/news/2026/10/01/japan/permanent-residency-guidelines-revision/)

生成摘要时出错

---

## 76. Show HN: NSL – WSL for Linux

**原文标题**: Show HN: NSL – WSL for Linux

**原文链接**: [https://frostyard.github.io/nsl/](https://frostyard.github.io/nsl/)

生成摘要时出错

---

## 77. Pilot of Israel-bound FlyDubai flight tried to crash plane

**原文标题**: Pilot of Israel-bound FlyDubai flight tried to crash plane

**原文链接**: [https://www.ft.com/content/7ed6ed48-79e4-46c2-968f-f2a69d263d35](https://www.ft.com/content/7ed6ed48-79e4-46c2-968f-f2a69d263d35)

生成摘要时出错

---

## 78. The Homeless Community in Portland, Oregon That Became a Self-Governed Village

**原文标题**: The Homeless Community in Portland, Oregon That Became a Self-Governed Village

**原文链接**: [https://www.nytimes.com/2026/09/26/headway/portland-diginity-village-homeless-community.html](https://www.nytimes.com/2026/09/26/headway/portland-diginity-village-homeless-community.html)

生成摘要时出错

---

## 79. Tcl/Tk 9.1

**原文标题**: Tcl/Tk 9.1

**原文链接**: [https://www.tcl-lang.org/software/tcltk/9.1.html](https://www.tcl-lang.org/software/tcltk/9.1.html)

生成摘要时出错

---

## 80. Most data centers refusing to say how much water, electricity they use

**原文标题**: Most data centers refusing to say how much water, electricity they use

**原文链接**: [https://nltimes.nl/2026/09/30/data-centers-refusing-say-much-water-electricity-use](https://nltimes.nl/2026/09/30/data-centers-refusing-say-much-water-electricity-use)

生成摘要时出错

---

## 81. Backblaze drive stats for Q2 2026

**原文标题**: Backblaze drive stats for Q2 2026

**原文链接**: [https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/)

生成摘要时出错

---

## 82. PS5 Relapse Exploit

**原文标题**: PS5 Relapse Exploit

**原文链接**: [https://github.com/ntfargo/Relapse-Exploit](https://github.com/ntfargo/Relapse-Exploit)

生成摘要时出错

---

## 83. We’re forgetting what darkness feels like

**原文标题**: We’re forgetting what darkness feels like

**原文链接**: [https://www.theguardian.com/environment/2026/sep/29/night-sky-darkness-city-regulation](https://www.theguardian.com/environment/2026/sep/29/night-sky-darkness-city-regulation)

生成摘要时出错

---

## 84. How Delhi cut electricity loss from 50 to 5 percent

**原文标题**: How Delhi cut electricity loss from 50 to 5 percent

**原文链接**: [https://spectrum.ieee.org/delhi-electricity-loss](https://spectrum.ieee.org/delhi-electricity-loss)

生成摘要时出错

---

## 85. NRC issues first U.S. construction permit for a BWRX-300 small modular reactor

**原文标题**: NRC issues first U.S. construction permit for a BWRX-300 small modular reactor

**原文链接**: [https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river](https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river)

生成摘要时出错

---

## 86. Stuck in the Suez Canal – the short version (2021)

**原文标题**: Stuck in the Suez Canal – the short version (2021)

**原文链接**: [https://cathsenker.co.uk/stuck-in-the-suez-canal-the-short-version/](https://cathsenker.co.uk/stuck-in-the-suez-canal-the-short-version/)

生成摘要时出错

---

## 87. A Staff Engineer's Guide to Inventing Work

**原文标题**: A Staff Engineer's Guide to Inventing Work

**原文链接**: [https://sujithjay.com/inventing-work](https://sujithjay.com/inventing-work)

生成摘要时出错

---

## 88. A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]

**原文标题**: A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]

**原文链接**: [https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)

生成摘要时出错

---

## 89. Commodore 64: Mercenary

**原文标题**: Commodore 64: Mercenary

**原文链接**: [https://gamesexplained.com/c64/mercenary/](https://gamesexplained.com/c64/mercenary/)

生成摘要时出错

---

## 90. When did Google get so weird?

**原文标题**: When did Google get so weird?

**原文链接**: [https://sancho.bearblog.dev/google-weird/](https://sancho.bearblog.dev/google-weird/)

生成摘要时出错

---

## 91. Walking Men

**原文标题**: Walking Men

**原文链接**: [https://bookofjoe2.blogspot.com/2026/09/walking-men.html](https://bookofjoe2.blogspot.com/2026/09/walking-men.html)

生成摘要时出错

---

## 92. Digital Audio on the ZX Spectrum's 1-Bit Beeper

**原文标题**: Digital Audio on the ZX Spectrum's 1-Bit Beeper

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/09/26/digital-audio-on-the-zx-spectrums-1-bit-beeper/](https://bumbershootsoft.wordpress.com/2026/09/26/digital-audio-on-the-zx-spectrums-1-bit-beeper/)

生成摘要时出错

---

## 93. Sustainable energy without the hot air (2008)

**原文标题**: Sustainable energy without the hot air (2008)

**原文链接**: [https://www.withouthotair.com/](https://www.withouthotair.com/)

生成摘要时出错

---

## 94. Cities Forced to Funnel License Plate Data to Federal Surveillance Program

**原文标题**: Cities Forced to Funnel License Plate Data to Federal Surveillance Program

**原文链接**: [https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/](https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/)

生成摘要时出错

---

## 95. Virus Stole a Human Gene and Won't Let Go of It

**原文标题**: Virus Stole a Human Gene and Won't Let Go of It

**原文链接**: [https://www.nytimes.com/2026/09/28/science/virus-molluscum-human-gene.html](https://www.nytimes.com/2026/09/28/science/virus-molluscum-human-gene.html)

生成摘要时出错

---

## 96. Deser: Rethinking Rust Serialization

**原文标题**: Deser: Rethinking Rust Serialization

**原文链接**: [https://lucumr.pocoo.org/2026/9/29/deser/](https://lucumr.pocoo.org/2026/9/29/deser/)

生成摘要时出错

---

## 97. What if Jev spoke Arrow?

**原文标题**: What if Jev spoke Arrow?

**原文链接**: [https://columnar.tech/blog/what-if-jev-spoke-arrow/](https://columnar.tech/blog/what-if-jev-spoke-arrow/)

生成摘要时出错

---

## 98. Half of world’s population exposed to dangerous levels of ozone in 2026

**原文标题**: Half of world’s population exposed to dangerous levels of ozone in 2026

**原文链接**: [https://www.scientificamerican.com/article/dangerous-ozone-threatened-half-of-worlds-population-this-year/](https://www.scientificamerican.com/article/dangerous-ozone-threatened-half-of-worlds-population-this-year/)

生成摘要时出错

---

## 99. PSSA: A non-transformer language model written from scratch in Rust

**原文标题**: PSSA: A non-transformer language model written from scratch in Rust

**原文链接**: [https://github.com/Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

生成摘要时出错

---

## 100. Software occlusion culling in Block Game

**原文标题**: Software occlusion culling in Block Game

**原文链接**: [https://enikofox.com/posts/software-rendered-occlusion-culling-in-block-game/](https://enikofox.com/posts/software-rendered-occlusion-culling-in-block-game/)

生成摘要时出错

---

