# Hacker News 热门文章摘要 (2026-04-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 微软与 OpenAI 终止独家及收入分成协议。

**原文标题**: Microsoft and OpenAI end their exclusive and revenue-sharing deal

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai)

无法访问文章链接。

---

## 2. “Why not just use Lean?”

**原文标题**: “Why not just use Lean?”

**原文链接**: [https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html](https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html)

In "Why not just use Lean?", the author critiques the modern "conformity" surrounding the Lean theorem prover, arguing that while Lean is a powerful tool with an impressive community, it is not the only—or necessarily the best—environment for formalizing mathematics.

The author situates Lean within a 60-year history, noting that pioneering systems like **AUTOMATH** (1968) and **ACL2** achieved complex formalizations decades ago. He highlights the distinction between the "propositions as types" framework (used by Lean and Rocq/Coq) and the **LCF-style approach** (used by Isabelle and HOL). The author argues that Lean’s reliance on dependent types and "proof objects" often results in massive, unnecessary computational overhead and logical quirks, such as "setoid hell" and issues with definitional equality.

The article promotes **Isabelle** as a robust alternative, citing three primary advantages:
1.  **Superior Automation:** Tools like "Sledgehammer" provide industry-leading proof automation.
2.  **Legibility:** Isabelle’s Isar language prioritizes structured, human-readable proof texts.
3.  **Simplicity:** By avoiding dependent types, Isabelle bypasses complex "universe levels" and undecidable type-checking issues.

The author credits Lean’s recent success to its rejection of the "constructive proof" obsession found in Rocq and its adoption by influential mathematicians like Kevin Buzzard. However, he warns against the "insularity" of the Lean community. Looking to the future, the author suggests that the ultimate goal of formalization is transparency and human readability. He posits that AI will eventually facilitate the translation of proofs between different assistants, making the choice of a specific system less restrictive and allowing researchers to choose tools based on efficiency rather than social pressure.

---

## 3. Networking changes coming in macOS 27

**原文标题**: Networking changes coming in macOS 27

**原文链接**: [https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/](https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/)

生成摘要时出错

---

## 4. 适用于常用 Arduino、ESP32 及 RP2040 开发板的开源 KiCad PCB

**原文标题**: Open-Source KiCad PCBs for Common Arduino, ESP32, RP2040 Boards

**原文链接**: [https://github.com/Hanqaqa/Easyduino](https://github.com/Hanqaqa/Easyduino)

**Easyduino** 是一个开源仓库，为全球最受欢迎的微控制器开发板提供 KiCad PCB 设计，包括 Arduino UNO 和 Nano、ESP32 和 ESP32-S3、树莓派 Pico (RP2040) 以及 STM32 Bluepill。

该项目的主要目标是将这些最初在不同时期、使用不同软件套件（如 Eagle 和 Altium）设计的多元化方案，统一整合到单一且现代的 KiCad 生态系统中。所有开发板的一项关键改进是增加了对 **USB-C 的支持**，并采用了标准化的 **4 层铜箔层叠结构**（针对嘉立创 JLCPCB 进行了优化），以简化布线并提高设计质量。

为了确保开发板保持高性价比且易于制造，项目对原始设计进行了战略性调整。这包括将难以采购的组件（如 Atmega16u2）或过于昂贵的零件（如 01005 封装组件）替换为更易获取的替代品。每个项目都经过系统化整理，包含：
*   KiCad 主文件（兼容 v8.0.0 和 v10 版本）。
*   生产就绪的输出文件（Gerber、BOM、坐标文件和 PDF）。
*   详细文档和组件数据手册。

Easyduino 采用 **CERN 开源硬件许可协议第 2 版 - 宽松型 (CERN-OHL-P)** 发布，允许在个人和商业项目中免费使用。创作者鼓励社区贡献以扩展该库，目前正在优化 RP2040 和 ESP32S3 的布局，并同时研究 NXP 微控制器等新平台。

---

## 5. SVG 清理的烦恼

**原文标题**: The woes of sanitizing SVGs

**原文链接**: [https://muffin.ink/blog/scratch-svg-sanitization/](https://muffin.ink/blog/scratch-svg-sanitization/)

《SVG 净化的困境》一文指出，Scratch 在处理 SVG 安全方面所采取的方法——即解析用户生成的内容并将其直接附加到主文档中——从根本上说是错误的，且不可持续。作者认为，通过构建日益复杂的“黑名单”机制来移除危险元素，是一场注定会输给不断演进的 Web 标准的徒劳之战。

作者列举了 2019 年至 2026 年间反复出现的漏洞时间线，以说明这种“注定失败”的策略：

*   **XSS 攻击：** 早期尝试利用正则表达式拦截 `<script>` 标签，却被大小写敏感问题和内联事件处理程序轻易绕过。即便在采用 **DOMPurify** 之后，造型编辑器所使用的 Paper.js 等库中依然存在漏洞。
*   **HTTP 泄漏：** 攻击者多次通过外部请求找到记录用户 IP 地址的方法。这些泄漏利用 `<image>` 的 href 属性、CSS `@import` 语句、`url()` 函数、CSS 变量及转义代码，绕过了净化器。
*   **UI 劫持（UI Redressing）：** 2026 年的一个漏洞展示了如何利用“无害”的 CSS 过渡和滤镜来重构整个 Scratch 界面。在不使用任何 JavaScript 或外部链接的情况下，这种手段可能隐藏举报按钮或创建钓鱼覆盖层。
*   **未来威胁：** `image-set()`、`src()` 和 `image()` 等新兴 CSS 特性提供了新的攻击途径，而现有的净化器尚无法应对。

作者总结道，Scratch 对自定义净化的依赖是一种“注定失败的方法”。由于 CSS 和 SVG 规范极其庞大且浏览器会持续更新，自定义解析器（如 `css-tree`）不可避免地无法涵盖所有边缘情况。文章建议，与其在净化层增加复杂度，不如从底层架构入手，解决将不可信 SVG 附加到文档中的核心问题。

---

## 6. GitHub Copilot 将改为按量计费

**原文标题**: GitHub Copilot is moving to usage-based billing

**原文链接**: [https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

提供的文本重点介绍了 GitHub 首席产品官 **Mario Rodriguez** 的职业背景，而非标题中提到的计费变更细节。

**核心要点包括：**

*   **职责与经验：** Mario Rodriguez 在微软和 GitHub 担任领导职务已有 20 年。作为首席产品官，他目前领导 GitHub 的产品团队，并负责监督 GitHub Copilot 的 AI 战略与增长。
*   **使命：** 他的职业生涯深受开发工具创作热情以及他作为“学习者”个人身份的驱动。
*   **影响力：** 在他的领导下，GitHub Copilot 的服务规模已扩展至数千家机构和数百万个人用户。
*   **公益事业：** 在企业职责之外，Rodriguez 还共同创立并联合主持了一所特许学校，致力于改善美国农村地区的教育。

虽然标题指出 **GitHub Copilot 正在转向按量计费模式**，但所提供的内容主要是该产品线负责人的个人简介。

---

## 7. Mercor 公司 4 万名 AI 承包商的 4TB 语音样本遭窃

**原文标题**: 4TB of voice samples just stolen from 40k AI contractors at Mercor

**原文链接**: [https://app.oravys.com/blog/mercor-breach-2026](https://app.oravys.com/blog/mercor-breach-2026)

据报道，2026年4月，勒索组织Lapsus$泄露了来自Mercor公司的4TB数据，致使超过4万名AI承包商的生物识别信息遭到泄露。此次泄露事件极其危险，因为它将录音室级别的优质语音记录与政府颁发的身份证件扫描件关联在了一起。

**潜在威胁**
传统的泄露事件通常仅涉及孤立的身份证件或音频，而Mercor泄露事件则为攻击者提供了进行高保真语音克隆所需的精准组合。由于录音平均时长达两到五分钟，攻击者掌握的数据远超现代合成克隆所需的15秒。这使得复杂的欺诈行为成为可能，包括：
*   **银行绕过：** 规避基于声纹的安全验证。
*   **语音钓鱼（Vishing）：** 冒充员工以重定向工资发放或解锁工作站。
*   **社会工程：** 通过“紧急情况”冒充诈骗针对家属。
*   **保险欺诈：** 通过电话提交虚假理赔。

**缓解与防御**
由于语音生物特征无法像密码那样“重置”，专家建议立即采取以下预防措施：
*   **审计公开音频：** 从社交媒体和YouTube上删除可被索引的录音。
*   **口头暗号：** 为家庭成员和财务交易建立线下的“挑战短语”。
*   **禁用声纹验证：** 要求银行停止使用语音验证，转而采用硬件密钥或基于App的多因素身份验证（MFA）。
*   **取证扫描：** 使用检测工具分析可疑音频中的“合成痕迹”，例如不自然的呼吸模式、机械的语速以及编解码器不匹配等。

法律追责已经开始，针对Mercor的生物识别数据采集行为，目前已有五起诉讼被提起。取证公司ORAVYS正为受害者提供免费分析，以帮助识别特定的音频样本是否已被武器化。

---

## 8. Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

**原文标题**: Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

**原文链接**: [https://github.com/dirac-run/dirac](https://github.com/dirac-run/dirac)

**Dirac** is an open-source AI coding agent designed to maximize accuracy and token efficiency. It recently achieved the top spot on the **Terminal-Bench-2 leaderboard** using the `gemini-3-flash-preview` model with a 65.2% score, outperforming both Google’s official baseline and leading closed-source competitors like Junie CLI.

Built as a fork of the Cline project, Dirac addresses the "context degradation" phenomenon—where model reasoning worsens as context length increases. By utilizing tightly curated context and advanced optimizations, Dirac reduces API costs by an average of **64.8%** (a 2.8x reduction). In benchmarks involving complex refactoring tasks on major repositories (such as VS Code and Transformers), Dirac consistently achieved 100% accuracy at a significantly lower cost than its peers.

**Key Technical Features:**
*   **Hash-Anchored Edits:** Employs stable line hashes for precise targeting, avoiding the errors common in traditional line-number editing.
*   **AST-Native Precision:** Uses Abstract Syntax Tree manipulation for high-accuracy structural changes like function extraction.
*   **Multi-File Batching:** Processes and edits multiple files in a single LLM roundtrip to minimize latency and costs.
*   **Autonomous Tooling:** Capabilities include file I/O, terminal execution, and headless browsing, all via an approval-based workflow.
*   **Native Tool Calling:** Exclusively supports models with native tool calling to ensure reliability (does not support MCP).

Dirac is available as a **VS Code extension** and a **CLI tool** (via npm). It supports a wide range of LLM providers, including Anthropic, OpenAI, and Gemini. The project is licensed under the Apache License 2.0 and developed by Dirac Delta Labs.

---

## 9. Pgbackrest is no longer being maintained

**原文标题**: Pgbackrest is no longer being maintained

**原文链接**: [https://github.com/pgbackrest/pgbackrest](https://github.com/pgbackrest/pgbackrest)

生成摘要时出错

---

## 10. Dutch central bank ditches AWS and chooses Lidl for European Cloud

**原文标题**: Dutch central bank ditches AWS and chooses Lidl for European Cloud

**原文链接**: [https://www.techzine.eu/news/infrastructure/140634/dutch-central-bank-chooses-lidl-for-european-cloud/](https://www.techzine.eu/news/infrastructure/140634/dutch-central-bank-chooses-lidl-for-european-cloud/)

生成摘要时出错

---

## 11. Canada's first sovereign wealth fund

**原文标题**: Canada's first sovereign wealth fund

**原文链接**: [https://www.cbc.ca/news/politics/sovereign-wealth-fund-carney-major-projects-9.7178238](https://www.cbc.ca/news/politics/sovereign-wealth-fund-carney-major-projects-9.7178238)

生成摘要时出错

---

## 12. Fully Featured Audio DSP Firmware for the Raspberry Pi Pico

**原文标题**: Fully Featured Audio DSP Firmware for the Raspberry Pi Pico

**原文链接**: [https://github.com/WeebLabs/DSPi](https://github.com/WeebLabs/DSPi)

生成摘要时出错

---

## 13. FDA approves first gene therapy for treatment of genetic hearing loss

**原文标题**: FDA approves first gene therapy for treatment of genetic hearing loss

**原文链接**: [https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher](https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher)

生成摘要时出错

---

## 14. Men who stare at walls

**原文标题**: Men who stare at walls

**原文链接**: [https://www.alexselimov.com/posts/men_who_stare_at_walls/](https://www.alexselimov.com/posts/men_who_stare_at_walls/)

生成摘要时出错

---

## 15. Decoupled DiLoCo: Resilient, Distributed AI Training at Scale

**原文标题**: Decoupled DiLoCo: Resilient, Distributed AI Training at Scale

**原文链接**: [https://deepmind.google/blog/decoupled-diloco/](https://deepmind.google/blog/decoupled-diloco/)

生成摘要时出错

---

## 16. Boats crash/break and can kill their passengers when falling certain distances

**原文标题**: Boats crash/break and can kill their passengers when falling certain distances

**原文链接**: [https://bugs.mojang.com/browse/MC/issues/MC-119369](https://bugs.mojang.com/browse/MC/issues/MC-119369)

生成摘要时出错

---

## 17. Tendril – a self-extending agent that builds and registers its own tools

**原文标题**: Tendril – a self-extending agent that builds and registers its own tools

**原文链接**: [https://github.com/serverless-dna/tendril](https://github.com/serverless-dna/tendril)

生成摘要时出错

---

## 18. Adding a team was the wrong strategic decision

**原文标题**: Adding a team was the wrong strategic decision

**原文链接**: [https://learnings.aleixmorgadas.dev/p/adding-a-team-was-the-wrong-strategic](https://learnings.aleixmorgadas.dev/p/adding-a-team-was-the-wrong-strategic)

生成摘要时出错

---

## 19. Show HN: Utilyze – an open source GPU monitoring tool more accurate than nvtop

**原文标题**: Show HN: Utilyze – an open source GPU monitoring tool more accurate than nvtop

**原文链接**: [https://www.systalyze.com/utilyze](https://www.systalyze.com/utilyze)

生成摘要时出错

---

## 20. Flipdiscs

**原文标题**: Flipdiscs

**原文链接**: [https://flipdisc.io](https://flipdisc.io)

生成摘要时出错

---

## 21. I bought Friendster for $30k – Here's what I'm doing with it

**原文标题**: I bought Friendster for $30k – Here's what I'm doing with it

**原文链接**: [https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d](https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d)

生成摘要时出错

---

## 22. US Supreme Court reviews police use of cell location data

**原文标题**: US Supreme Court reviews police use of cell location data

**原文链接**: [https://www.nytimes.com/2026/04/27/us/politics/supreme-court-cell-data-geofence.html](https://www.nytimes.com/2026/04/27/us/politics/supreme-court-cell-data-geofence.html)

生成摘要时出错

---

## 23. Quarkdown – Markdown with Superpowers

**原文标题**: Quarkdown – Markdown with Superpowers

**原文链接**: [https://quarkdown.com/](https://quarkdown.com/)

生成摘要时出错

---

## 24. Den stora Älgvandringen – The great moose migration (live)

**原文标题**: Den stora Älgvandringen – The great moose migration (live)

**原文链接**: [https://www.svtplay.se/video/jXv3A5G/den-stora-algvandringen/idag-00-00](https://www.svtplay.se/video/jXv3A5G/den-stora-algvandringen/idag-00-00)

生成摘要时出错

---

## 25. Managing the Unmanaged Switch

**原文标题**: Managing the Unmanaged Switch

**原文链接**: [https://watchmysys.com/blog/2026/03/managing-the-unmanaged-switch/](https://watchmysys.com/blog/2026/03/managing-the-unmanaged-switch/)

生成摘要时出错

---

## 26. Supreme Court to Hear Arguments in Landmark Roundup Weedkiller Case

**原文标题**: Supreme Court to Hear Arguments in Landmark Roundup Weedkiller Case

**原文链接**: [https://www.nytimes.com/2026/04/26/climate/supreme-court-bayer-monsanto-roundup-glyphosate.html](https://www.nytimes.com/2026/04/26/climate/supreme-court-bayer-monsanto-roundup-glyphosate.html)

生成摘要时出错

---

## 27. AI should elevate your thinking, not replace it

**原文标题**: AI should elevate your thinking, not replace it

**原文链接**: [https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/](https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/)

生成摘要时出错

---

## 28. Show HN: A terminal spreadsheet editor with Vim keybindings

**原文标题**: Show HN: A terminal spreadsheet editor with Vim keybindings

**原文链接**: [https://github.com/garritfra/cell](https://github.com/garritfra/cell)

生成摘要时出错

---

## 29. Getting my daily news from a dot matrix printer 2024

**原文标题**: Getting my daily news from a dot matrix printer 2024

**原文链接**: [https://aschmelyun.com/blog/getting-my-daily-news-from-a-dot-matrix-printer/](https://aschmelyun.com/blog/getting-my-daily-news-from-a-dot-matrix-printer/)

生成摘要时出错

---

## 30. Understanding the short circuit in solid-state batteries

**原文标题**: Understanding the short circuit in solid-state batteries

**原文链接**: [https://www.mpie.de/5151287/short-circuit-solid-state-batteries](https://www.mpie.de/5151287/short-circuit-solid-state-batteries)

生成摘要时出错

---

## 31. Self-updating screenshots

**原文标题**: Self-updating screenshots

**原文链接**: [https://interblah.net/self-updating-screenshots](https://interblah.net/self-updating-screenshots)

生成摘要时出错

---

## 32. TurboQuant: A first-principles walkthrough

**原文标题**: TurboQuant: A first-principles walkthrough

**原文链接**: [https://arkaung.github.io/interactive-turboquant/](https://arkaung.github.io/interactive-turboquant/)

生成摘要时出错

---

## 33. The Prompt API

**原文标题**: The Prompt API

**原文链接**: [https://developer.chrome.com/docs/ai/prompt-api](https://developer.chrome.com/docs/ai/prompt-api)

生成摘要时出错

---

## 34. I analyzed 571M Amazon reviews to find the most profanity-filled customer rants

**原文标题**: I analyzed 571M Amazon reviews to find the most profanity-filled customer rants

**原文链接**: [https://burla-cloud.github.io/amazon-review-distiller/](https://burla-cloud.github.io/amazon-review-distiller/)

生成摘要时出错

---

## 35. Running local LLMs offline on a ten-hour flight

**原文标题**: Running local LLMs offline on a ten-hour flight

**原文链接**: [https://deploy.live/blog/running-local-llms-offline-on-a-ten-hour-flight/](https://deploy.live/blog/running-local-llms-offline-on-a-ten-hour-flight/)

生成摘要时出错

---

## 36. EFF Challenges Secrecy in Eastern District of Texas Patent Case

**原文标题**: EFF Challenges Secrecy in Eastern District of Texas Patent Case

**原文链接**: [https://www.eff.org/deeplinks/2026/04/eff-challenges-secrecy-eastern-district-texas-patent-case](https://www.eff.org/deeplinks/2026/04/eff-challenges-secrecy-eastern-district-texas-patent-case)

生成摘要时出错

---

## 37. Three constraints before I build anything

**原文标题**: Three constraints before I build anything

**原文链接**: [https://jordanlord.co.uk/blog/3-constraints/](https://jordanlord.co.uk/blog/3-constraints/)

生成摘要时出错

---

## 38. Fast16: High-precision software sabotage 5 years before Stuxnet

**原文标题**: Fast16: High-precision software sabotage 5 years before Stuxnet

**原文链接**: [https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/)

生成摘要时出错

---

## 39. Canva apologizes after its AI tool replaces 'Palestine' in designs

**原文标题**: Canva apologizes after its AI tool replaces 'Palestine' in designs

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/919028/canva-magic-layers-ai-replacing-palestine](https://www.theverge.com/ai-artificial-intelligence/919028/canva-magic-layers-ai-replacing-palestine)

生成摘要时出错

---

## 40. It's OK to abandon your side-project (2024)

**原文标题**: It's OK to abandon your side-project (2024)

**原文链接**: [https://robbowen.digital/wrote-about/abandoned-side-projects/](https://robbowen.digital/wrote-about/abandoned-side-projects/)

生成摘要时出错

---

## 41. A Guide to CubeSat Mission and Bus Design

**原文标题**: A Guide to CubeSat Mission and Bus Design

**原文链接**: [https://pressbooks-dev.oer.hawaii.edu/epet302/](https://pressbooks-dev.oer.hawaii.edu/epet302/)

生成摘要时出错

---

## 42. Electrostatics and High Voltage Links

**原文标题**: Electrostatics and High Voltage Links

**原文链接**: [http://amasci.com/static/electrostatic1.html](http://amasci.com/static/electrostatic1.html)

生成摘要时出错

---

## 43. Branimir Lambov from IBM on Cassandra

**原文标题**: Branimir Lambov from IBM on Cassandra

**原文链接**: [https://theconsensus.dev/p/2026/04/26/branimir-lambov-from-ibm-on-cassandra.html](https://theconsensus.dev/p/2026/04/26/branimir-lambov-from-ibm-on-cassandra.html)

生成摘要时出错

---

## 44. Box to save memory in Rust

**原文标题**: Box to save memory in Rust

**原文链接**: [https://dystroy.org/blog/box-to-save-memory/](https://dystroy.org/blog/box-to-save-memory/)

生成摘要时出错

---

## 45. Intel Ends Open Ecosystem Community/Evangelism Projects

**原文标题**: Intel Ends Open Ecosystem Community/Evangelism Projects

**原文链接**: [https://www.phoronix.com/news/Intel-Ends-OSS-Evangelism-Repos](https://www.phoronix.com/news/Intel-Ends-OSS-Evangelism-Repos)

生成摘要时出错

---

## 46. Sawe becomes first athlete to run a sub-two-hour marathon in a competitive race

**原文标题**: Sawe becomes first athlete to run a sub-two-hour marathon in a competitive race

**原文链接**: [https://www.bbc.com/sport/athletics/articles/crm1m7e0zwzo](https://www.bbc.com/sport/athletics/articles/crm1m7e0zwzo)

生成摘要时出错

---

## 47. FreeBSD Device Drivers Book

**原文标题**: FreeBSD Device Drivers Book

**原文链接**: [https://github.com/ebrandi/FDD-book](https://github.com/ebrandi/FDD-book)

生成摘要时出错

---

## 48. Steam Controller: It's almost here

**原文标题**: Steam Controller: It's almost here

**原文链接**: [https://store.steampowered.com/news/group/45479024/view/508485755865137686](https://store.steampowered.com/news/group/45479024/view/508485755865137686)

生成摘要时出错

---

## 49. An AI agent deleted our production database. The agent's confession is below

**原文标题**: An AI agent deleted our production database. The agent's confession is below

**原文链接**: [https://twitter.com/lifeof_jer/status/2048103471019434248](https://twitter.com/lifeof_jer/status/2048103471019434248)

生成摘要时出错

---

## 50. Claude-powered AI coding agent deletes company database in 9 seconds

**原文标题**: Claude-powered AI coding agent deletes company database in 9 seconds

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-powered-ai-coding-agent-deletes-entire-company-database-in-9-seconds-backups-zapped-after-cursor-tool-powered-by-anthropics-claude-goes-rogue](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-powered-ai-coding-agent-deletes-entire-company-database-in-9-seconds-backups-zapped-after-cursor-tool-powered-by-anthropics-claude-goes-rogue)

生成摘要时出错

---

## 51. Who Is That Knocking at My (SSH) Door?

**原文标题**: Who Is That Knocking at My (SSH) Door?

**原文链接**: [https://sheep.horse/2026/4/who_is_that_knocking_at_my_%28ssh%29_door.html](https://sheep.horse/2026/4/who_is_that_knocking_at_my_%28ssh%29_door.html)

生成摘要时出错

---

## 52. Terra API (YC W21) Hiring: Applied AI Strategist (Health Intelligence)

**原文标题**: Terra API (YC W21) Hiring: Applied AI Strategist (Health Intelligence)

**原文链接**: [https://www.ycombinator.com/companies/terra-api/jobs/DY7BCZU-applied-ai-strategist-market-intelligence-health](https://www.ycombinator.com/companies/terra-api/jobs/DY7BCZU-applied-ai-strategist-market-intelligence-health)

生成摘要时出错

---

## 53. Mystery Cpuid Bit

**原文标题**: Mystery Cpuid Bit

**原文链接**: [http://www.os2museum.com/wp/mystery-cpuid-bit/](http://www.os2museum.com/wp/mystery-cpuid-bit/)

生成摘要时出错

---

## 54. EvanFlow – A TDD driven feedback loop for Claude Code

**原文标题**: EvanFlow – A TDD driven feedback loop for Claude Code

**原文链接**: [https://github.com/evanklem/evanflow](https://github.com/evanklem/evanflow)

生成摘要时出错

---

## 55. Magic: The Gathering took me from N2 to Japanese fluency

**原文标题**: Magic: The Gathering took me from N2 to Japanese fluency

**原文链接**: [https://www.tokyodev.com/articles/how-magic-the-gathering-took-me-from-n2-to-japanese-fluency](https://www.tokyodev.com/articles/how-magic-the-gathering-took-me-from-n2-to-japanese-fluency)

生成摘要时出错

---

## 56. Does reading do us any good?

**原文标题**: Does reading do us any good?

**原文链接**: [https://aeon.co/essays/the-role-of-literature-as-the-key-to-personal-freedom](https://aeon.co/essays/the-role-of-literature-as-the-key-to-personal-freedom)

生成摘要时出错

---

## 57. Silicon Valley has forgotten what normal people want

**原文标题**: Silicon Valley has forgotten what normal people want

**原文链接**: [https://www.theverge.com/tldr/915176/nft-metaverse-ai-weirdos](https://www.theverge.com/tldr/915176/nft-metaverse-ai-weirdos)

生成摘要时出错

---

## 58. Butterflies are in decline across North America, a look at the Western Monarch

**原文标题**: Butterflies are in decline across North America, a look at the Western Monarch

**原文链接**: [https://www.smithsonianmag.com/science-nature/butterflies-are-in-dramatic-decline-across-north-america-a-close-look-at-the-western-monarch-shows-why-180988582/](https://www.smithsonianmag.com/science-nature/butterflies-are-in-dramatic-decline-across-north-america-a-close-look-at-the-western-monarch-shows-why-180988582/)

生成摘要时出错

---

## 59. Running Bare-Metal Rust Alongside ESP-IDF on the ESP32-S3's Second Core

**原文标题**: Running Bare-Metal Rust Alongside ESP-IDF on the ESP32-S3's Second Core

**原文链接**: [https://tingouw.com/blog/embedded/esp32/run_rust_on_app_core](https://tingouw.com/blog/embedded/esp32/run_rust_on_app_core)

生成摘要时出错

---

## 60. The Mushroom That Makes People Have the Exact Same Hallucination

**原文标题**: The Mushroom That Makes People Have the Exact Same Hallucination

**原文链接**: [https://www.vice.com/en/article/meet-the-mushroom-that-make-people-have-the-exact-same-hallucination/](https://www.vice.com/en/article/meet-the-mushroom-that-make-people-have-the-exact-same-hallucination/)

生成摘要时出错

---

## 61. The Visible Zorker: Zork 1

**原文标题**: The Visible Zorker: Zork 1

**原文链接**: [https://eblong.com/infocom/visi/zork1/](https://eblong.com/infocom/visi/zork1/)

生成摘要时出错

---

## 62. Mistral built a $14B AI empire by not being American

**原文标题**: Mistral built a $14B AI empire by not being American

**原文链接**: [https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/](https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/)

生成摘要时出错

---

## 63. Show HN: Turning a Gaussian Splat into a videogame

**原文标题**: Show HN: Turning a Gaussian Splat into a videogame

**原文链接**: [https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/](https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/)

生成摘要时出错

---

## 64. When the cheap one is the cool one

**原文标题**: When the cheap one is the cool one

**原文链接**: [https://arun.is/blog/cheap-cool/](https://arun.is/blog/cheap-cool/)

生成摘要时出错

---

## 65. Clay PCB Tutorial

**原文标题**: Clay PCB Tutorial

**原文链接**: [https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial](https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial)

生成摘要时出错

---

## 66. Dear friend, you have built a Kubernetes (2024)

**原文标题**: Dear friend, you have built a Kubernetes (2024)

**原文链接**: [https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/](https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/)

生成摘要时出错

---

## 67. Interview with Bob Odenkirk

**原文标题**: Interview with Bob Odenkirk

**原文链接**: [https://www.nytimes.com/2026/04/25/magazine/bob-odenkirk-interview.html](https://www.nytimes.com/2026/04/25/magazine/bob-odenkirk-interview.html)

生成摘要时出错

---

## 68. Revocation of X.509 Certificates

**原文标题**: Revocation of X.509 Certificates

**原文链接**: [https://blog.apnic.net/2026/04/24/revocation-of-x-509-certificates/](https://blog.apnic.net/2026/04/24/revocation-of-x-509-certificates/)

生成摘要时出错

---

## 69. MoQ Boy

**原文标题**: MoQ Boy

**原文链接**: [https://moq.dev/blog/moq-boy/](https://moq.dev/blog/moq-boy/)

生成摘要时出错

---

## 70. SWE-bench Verified no longer measures frontier coding capabilities

**原文标题**: SWE-bench Verified no longer measures frontier coding capabilities

**原文链接**: [https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

生成摘要时出错

---

## 71. Show HN: I built a dual crossword puzzle where two crosswords share one grid

**原文标题**: Show HN: I built a dual crossword puzzle where two crosswords share one grid

**原文链接**: [https://forkle.co.uk/](https://forkle.co.uk/)

生成摘要时出错

---

## 72. Ubuntu Linux Will Begin Landing AI Features Throughout the Next Year

**原文标题**: Ubuntu Linux Will Begin Landing AI Features Throughout the Next Year

**原文链接**: [https://www.phoronix.com/news/Ubuntu-AI-Features-2026](https://www.phoronix.com/news/Ubuntu-AI-Features-2026)

生成摘要时出错

---

## 73. Asahi Linux Progress Linux 7.0

**原文标题**: Asahi Linux Progress Linux 7.0

**原文链接**: [https://asahilinux.org/2026/04/progress-report-7-0/](https://asahilinux.org/2026/04/progress-report-7-0/)

生成摘要时出错

---

## 74. Chernobyl wildlife forty years on

**原文标题**: Chernobyl wildlife forty years on

**原文链接**: [https://www.bbc.com/future/article/20260424-chernobyl-wildlife-forty-years-on](https://www.bbc.com/future/article/20260424-chernobyl-wildlife-forty-years-on)

生成摘要时出错

---

## 75. Google DeepMind Paper Argues LLMs Will Never Be Conscious

**原文标题**: Google DeepMind Paper Argues LLMs Will Never Be Conscious

**原文链接**: [https://www.404media.co/google-deepmind-paper-argues-llms-will-never-be-conscious/](https://www.404media.co/google-deepmind-paper-argues-llms-will-never-be-conscious/)

生成摘要时出错

---

## 76. Low-Dose Aspirin Usage for Primary Prevention Has Fallen by >50% Since 2018

**原文标题**: Low-Dose Aspirin Usage for Primary Prevention Has Fallen by >50% Since 2018

**原文链接**: [https://www.epicresearch.org/articles/low-dose-aspirin-usage-for-primary-prevention-of-cardiovascular-disease-has-fallen-by-more-than-half-since-2018](https://www.epicresearch.org/articles/low-dose-aspirin-usage-for-primary-prevention-of-cardiovascular-disease-has-fallen-by-more-than-half-since-2018)

生成摘要时出错

---

## 77. Many Opioid Victims Will Be Shut Out of Purdue's $7.4B Bankruptcy Settlement

**原文标题**: Many Opioid Victims Will Be Shut Out of Purdue's $7.4B Bankruptcy Settlement

**原文链接**: [https://www.propublica.org/article/purdue-settlement-leaves-opioid-victims-behind](https://www.propublica.org/article/purdue-settlement-leaves-opioid-victims-behind)

生成摘要时出错

---

## 78. Amateur armed with ChatGPT solves an Erdős problem

**原文标题**: Amateur armed with ChatGPT solves an Erdős problem

**原文链接**: [https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/)

生成摘要时出错

---

## 79. GoDaddy gave a domain to a stranger without any documentation

**原文标题**: GoDaddy gave a domain to a stranger without any documentation

**原文链接**: [https://anchor.host/godaddy-gave-a-domain-to-a-stranger-without-any-documentation/](https://anchor.host/godaddy-gave-a-domain-to-a-stranger-without-any-documentation/)

生成摘要时出错

---

## 80. Agentic AI systems violate the implicit assumptions of database design

**原文标题**: Agentic AI systems violate the implicit assumptions of database design

**原文链接**: [https://arpitbhayani.me/blogs/defensive-databases/](https://arpitbhayani.me/blogs/defensive-databases/)

生成摘要时出错

---

## 81. Lessons from building multiplayer browsers

**原文标题**: Lessons from building multiplayer browsers

**原文链接**: [https://www.alejandro.pe/writing/sail-muddy-lessons](https://www.alejandro.pe/writing/sail-muddy-lessons)

生成摘要时出错

---

## 82. Mahjong: A Visual Guide

**原文标题**: Mahjong: A Visual Guide

**原文链接**: [https://themahjong.guide/](https://themahjong.guide/)

生成摘要时出错

---

## 83. Quirks of Human Anatomy

**原文标题**: Quirks of Human Anatomy

**原文链接**: [https://www.sdbonline.org/sites/fly/lewheldquirk/figlegq6.htm](https://www.sdbonline.org/sites/fly/lewheldquirk/figlegq6.htm)

生成摘要时出错

---

## 84. I spent 6 years building my Kanban as I hated how managers run the boards

**原文标题**: I spent 6 years building my Kanban as I hated how managers run the boards

**原文链接**: [https://www.npmjs.com/package/ooko](https://www.npmjs.com/package/ooko)

生成摘要时出错

---

## 85. Show HN: The Unix Magic poster, annotated (updated)

**原文标题**: Show HN: The Unix Magic poster, annotated (updated)

**原文链接**: [https://github.com/drio/unixmagic](https://github.com/drio/unixmagic)

生成摘要时出错

---

## 86. America's Geothermal Breakthrough

**原文标题**: America's Geothermal Breakthrough

**原文链接**: [https://oilprice.com/Alternative-Energy/Geothermal-Energy/Americas-Geothermal-Breakthrough-Could-Unlock-a-150-Gigawatt-Energy-Revolution.html](https://oilprice.com/Alternative-Energy/Geothermal-Energy/Americas-Geothermal-Breakthrough-Could-Unlock-a-150-Gigawatt-Energy-Revolution.html)

生成摘要时出错

---

## 87. The Super Nintendo Cartridges (2024)

**原文标题**: The Super Nintendo Cartridges (2024)

**原文链接**: [https://fabiensanglard.net/snes_carts/](https://fabiensanglard.net/snes_carts/)

生成摘要时出错

---

## 88. Windows 11's second-chance setup dialogs hurt IT, drain productivity

**原文标题**: Windows 11's second-chance setup dialogs hurt IT, drain productivity

**原文链接**: [https://www.theregister.com/2026/04/26/windows_second_chance_setup/](https://www.theregister.com/2026/04/26/windows_second_chance_setup/)

生成摘要时出错

---

## 89. XOXO Festival Archive

**原文标题**: XOXO Festival Archive

**原文链接**: [https://xoxofest.com/](https://xoxofest.com/)

生成摘要时出错

---

## 90. QNX on the Commodore 900 – Raiders of the lost hard drive [video] (2025)

**原文标题**: QNX on the Commodore 900 – Raiders of the lost hard drive [video] (2025)

**原文链接**: [https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5479-raiders-of-the-lost-hard-drive/](https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5479-raiders-of-the-lost-hard-drive/)

生成摘要时出错

---

## 91. Show HN: Tiao, A two-player turn-based board game

**原文标题**: Show HN: Tiao, A two-player turn-based board game

**原文链接**: [https://playtiao.com](https://playtiao.com)

生成摘要时出错

---

## 92. Orinoco: Young Generation Garbage Collection

**原文标题**: Orinoco: Young Generation Garbage Collection

**原文链接**: [https://v8.dev/blog/orinoco-parallel-scavenger](https://v8.dev/blog/orinoco-parallel-scavenger)

生成摘要时出错

---

## 93. Music of the BBC Microcomputer System

**原文标题**: Music of the BBC Microcomputer System

**原文链接**: [https://www.acornelectron.co.uk/eug/72/a-musi.html](https://www.acornelectron.co.uk/eug/72/a-musi.html)

生成摘要时出错

---

## 94. The fastest Linux timestamps

**原文标题**: The fastest Linux timestamps

**原文链接**: [https://www.hmpcabral.com/2026/04/26/the-fastest-linux-timestamps/](https://www.hmpcabral.com/2026/04/26/the-fastest-linux-timestamps/)

生成摘要时出错

---

## 95. Dillo Browser Release 3.3.0

**原文标题**: Dillo Browser Release 3.3.0

**原文链接**: [https://dillo-browser.org/release/3.3.0/](https://dillo-browser.org/release/3.3.0/)

生成摘要时出错

---

## 96. Exposing Floating Point – Bartosz Ciechanowski (2019)

**原文标题**: Exposing Floating Point – Bartosz Ciechanowski (2019)

**原文链接**: [https://ciechanow.ski/exposing-floating-point/](https://ciechanow.ski/exposing-floating-point/)

生成摘要时出错

---

## 97. Statecharts: hierarchical state machines

**原文标题**: Statecharts: hierarchical state machines

**原文链接**: [https://statecharts.dev/](https://statecharts.dev/)

生成摘要时出错

---

## 98. Simulacrum of Knowledge Work

**原文标题**: Simulacrum of Knowledge Work

**原文链接**: [https://blog.happyfellow.dev/simulacrum-of-knowledge-work/](https://blog.happyfellow.dev/simulacrum-of-knowledge-work/)

生成摘要时出错

---

## 99. Who Asked for This?

**原文标题**: Who Asked for This?

**原文链接**: [https://calnewport.com/who-asked-for-this/](https://calnewport.com/who-asked-for-this/)

生成摘要时出错

---

## 100. The 1944 Warsaw Uprising, in Color

**原文标题**: The 1944 Warsaw Uprising, in Color

**原文链接**: [https://www.barwypowstania.pl/](https://www.barwypowstania.pl/)

生成摘要时出错

---

