# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-27.md)

*最后自动更新时间: 2026-04-27 18:33:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 2 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 3 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 4 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 5 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 6 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 7 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 8 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 9 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 10 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 11 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 12 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 13 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 14 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 15 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 16 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 17 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 18 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 19 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 20 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 21 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 22 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 23 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 24 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 25 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 26 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 27 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 28 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 29 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 30 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 31 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 32 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 33 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 34 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 35 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 36 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 37 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 38 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 39 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 40 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 41 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 42 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 43 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 44 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 45 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 46 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 47 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 48 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 49 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 50 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 51 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 52 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 53 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 54 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 55 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 56 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 57 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 58 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 59 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 60 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 61 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 62 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 63 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 64 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 65 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 66 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 67 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 68 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 69 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 70 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 71 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 72 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 73 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 74 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 75 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 76 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 77 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 78 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 79 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 80 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 81 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 82 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 83 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 84 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 85 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 86 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 87 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 88 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 89 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 90 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 91 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 92 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 93 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 94 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 95 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 96 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 97 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 98 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 99 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 100 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 101 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 102 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 103 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 104 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 105 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 106 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 107 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 108 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 109 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 110 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 111 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 112 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 113 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 114 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 115 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 116 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 117 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 118 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 119 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 120 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 121 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 122 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 123 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 124 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 125 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 126 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 127 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 128 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 129 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 130 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 131 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 132 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 133 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 134 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 135 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 136 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 137 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 138 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 139 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 140 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 141 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 142 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 143 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 144 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 145 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 146 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 147 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 148 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 149 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 150 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 151 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 152 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 153 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 154 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 155 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 156 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 157 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 158 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 159 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 160 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 161 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 162 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 163 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 164 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 165 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 166 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 167 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 168 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 169 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 170 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 171 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 172 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 173 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 174 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 175 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 176 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 177 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 178 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 179 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 180 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 181 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 182 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 183 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 184 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 185 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 186 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 187 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 188 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 189 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 190 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 191 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 192 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 193 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 194 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 195 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 196 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 197 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 198 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 199 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 200 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 201 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 202 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 203 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 204 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 205 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 206 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 207 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 208 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 209 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 210 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 211 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 212 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 213 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 214 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 215 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 216 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 217 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 218 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 219 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 220 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 221 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 222 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 223 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 224 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 225 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 226 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 227 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 228 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 229 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 230 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 231 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 232 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 233 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 234 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 235 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 236 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 237 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 238 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 239 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 240 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 241 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 242 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 243 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 244 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 245 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 246 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 247 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 248 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 249 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 250 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 251 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 252 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 253 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 254 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 255 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 256 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 257 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 258 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 259 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 260 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 261 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 262 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 263 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 264 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 265 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 266 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 267 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 268 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 269 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 270 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 271 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 272 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 273 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 274 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 275 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 276 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 277 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 278 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 279 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 280 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 281 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 282 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 283 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 284 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 285 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 286 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 287 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 288 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 289 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 290 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 291 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 292 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 293 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 294 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 295 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 296 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 297 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 298 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 299 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 300 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 301 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 302 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 303 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 304 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 305 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 306 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 307 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 308 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 309 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 310 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 311 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 312 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 313 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 314 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 315 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 316 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 317 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 318 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 319 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 320 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 321 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 322 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 323 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 324 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 325 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 326 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 327 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 328 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 329 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 330 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 331 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 332 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 333 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 334 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 335 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 336 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 337 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 338 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 339 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 340 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 341 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 342 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 343 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 344 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 345 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 346 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 347 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 348 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 349 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 350 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 351 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 352 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 353 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 354 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 355 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 356 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 357 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 358 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 359 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 360 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 361 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 362 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 363 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 364 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 365 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 366 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 367 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 368 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 369 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 370 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 371 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 372 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 373 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 374 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 375 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 376 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 377 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 378 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 379 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 380 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 381 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 382 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 383 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 384 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 385 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 386 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 387 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 388 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 389 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 390 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 391 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 392 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 393 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 394 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 395 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 396 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 397 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 398 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 399 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 400 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 401 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 402 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 403 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
