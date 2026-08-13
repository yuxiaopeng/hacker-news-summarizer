# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-13.md)

*最后自动更新时间: 2026-08-13 18:22:31*
## 1. Gemini 3.7 Flash

**原文标题**: Gemini 3.7 Flash

**原文链接**: [https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash)

Gemini 3.7 Flash 是 Gemini 系列中最新的高性能原生多模态推理模型。现已通过 Interactions API 和 Google AI Studio 全面开放，专为提升速度和解决复杂问题而设计。

**关键技术规格：**
*   **输入支持：** 支持处理文本、图像、视频、音频和 PDF。
*   **Token 限制：** 拥有高达 1,048,576 个输入 Token 和 65,536 个输出 Token 的庞大限制。
*   **版本：** 稳定版模型代码为 `gemini-3.7-flash`。

**核心能力：**
该模型引入了专门的**“思考 (Thinking)”**功能，允许用户选择低、中、高三种推理强度。它支持高级开发者功能，如**计算机使用（预览版）**、代码执行、函数调用、文件搜索和结构化输出。此外，它还支持通过 Google 搜索和 Google 地图进行 Grounding（数据核实），以确保信息的准确性。

**可用性与限制：**
尽管该模型在推理和处理方面表现出色，但目前暂不支持原生音频生成、图像生成或 Live API。用户可以通过多种调用模式访问，包括 Batch API、Flex 推理和 Priority 推理。根据文档显示，最近一次更新记录于 2026 年 8 月。

---

## 2. DRAM 面条化

**原文标题**: Spaghettifying DRAM

**原文链接**: [https://github.com/xoreaxeaxeax/skitter-creek-bath-salts](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts)

《DRAM 乱序化》（Spaghettifying DRAM）一文详述了一个名为 **skitter-creek-bath-salts** 的项目，该项目展示了如何通过操纵 DRAM 控制器的内部地址转换逻辑来绕过硬件安全边界。

**核心机制**
作者指出，尽管 CPU 使用多层保护（如 MMU、IOMMU 和内存区域排除）来隔离系统管理模式（SMM）和平台安全处理器（PSP）等敏感区域，但这些防护机制是基于**物理地址**运行的。然而，内存控制器（MCT）和 DRAM 控制器（DCT）会对这些物理地址进行最后的、通常未公开的转换，将其变为原始的 DRAM 坐标（Bank、Rank、行和列）。

**攻击手段：“乱序化”（Spaghettification）**
通过修改 DRAM 控制器中的特定寄存器（例如 Bank-Swizzle 模式），攻击者可以“重连”内存层级的底层逻辑。这会导致物理地址最终指向的 DRAM 位置与预期不符。由于安全“围栏”位于该层级之上，它们会继续监控原始物理地址，却察觉不到其下方的数据已被重定向。这使得攻击者能够创建“别名”来访问受保护的内存区域，而这些区域对内核而言原本是不可见的。

**技术实现**
该利用技术涉及对 DRAM 控制器寄存器进行高速“注入”（poke），同时通过禁用中断和预填充缓存来尽量减少 DRAM 交互，以防止系统崩溃。由于特定的硬件转换通常未公开，作者利用线性代数来解析新的映射关系。通过将 DRAM 控制器的转换视为 **GF(2) 线性映射**，他们使用 **Z3 SMT 求解器**从观察到的内存模式中重构出转换矩阵。

**目标系统**
该研究在 **AMD Family 16h CPU** 上开发并测试，这些处理器的 DRAM 控制器寄存器已有文档说明且未锁定。作者认为，其底层原理——“*p 的奥德赛”——适用于包括 ARM 和 RISC-V 在内的大多数现代架构。

---

## 3. Mistral OCR 4.1

**原文标题**: Mistral OCR 4.1

**原文链接**: [https://docs.mistral.ai/models/ocr-4-1](https://docs.mistral.ai/models/ocr-4-1)

Mistral OCR 4.1 于 2026 年 7 月 16 日开启公开预览（Public Preview），是专为赋能 Mistral 文档 AI 技术栈而设计的顶级服务。此次更新引入了重大的技术增强，旨在提升文档数字化的精确度与实用性。

**核心特性：**
*   **细粒度提取：** 原生支持段落级边界框（Bounding Box）提取及结构化区块标注。
*   **质量控制：** 提供区块级置信度评分，以确保数据准确性。
*   **API 集成：** 通过 `/v1/ocr` 和 `/v1/batch` 端点支持结构化注释和批量处理。

**定价方案：**
该模型（`mistral-ocr-4-1`）的定价极具竞争力：
*   **标准 OCR：** 每 1,000 页 3.5 欧元（约合 3.81 美元）。
*   **标注页：** 每 1,000 页 4.38 欧元（约合 4.77 美元）。

通过优先提升速度与性能，Mistral OCR 4.1 将自身定位为生态系统中的强大解决方案，该生态系统还包括 Z.ai GLM 5.2 和 Shieldstral 1.0 等其他专业模型。此次发布标志着在为开发者提供复杂结构化文档分析所需工具方面迈出了重要一步。

---

## 4. 为ENIAC而来，为UNIVAC和Skeduflo而留

**原文标题**: Come for ENIAC, Stay for UNIVAC and Skeduflo

**原文链接**: [https://uniqueatpenn.wordpress.com/2026/08/05/come-for-eniac-stay-for-univac-and-skeduflo/](https://uniqueatpenn.wordpress.com/2026/08/05/come-for-eniac-stay-for-univac-and-skeduflo/)

本文重点介绍了计算机先驱约翰·莫奇利（John Mauchly）的生平与遗产，其大量的个人档案现收藏于基斯拉特特藏中心。尽管莫奇利因 1946 年与 J. 普雷斯珀·埃克特共同发明了世界上第一台通用电子计算机 ENIAC 而闻名于世，但作者强调，他的贡献远不止于这一单一成就。

在 ENIAC 之后，莫奇利与埃克特又开发了多个具有里程碑意义的系统，包括 BINAC、EDVAC 以及世界上第一台商用电子计算机 UNIVAC。作者特别突出了莫奇利在 20 世纪 50 年代领导 UNIVAC 应用与研究中心（UARC）时期的成就。在 UARC，莫奇利将重点从仅用计算机解决现有问题，转向主动为商业机构和政府探索利用技术的新途径。这一创新时代也为包括葛丽丝·穆雷·霍珀准将在内的其他先驱提供了支持。

莫奇利的前瞻性通过“Skeduflo”得到了进一步印证，这是一款装在手提箱中、专为建筑进度调度设计的便携式计算机。令人惊叹的是，莫奇利在 1967 年就预言商人终将随身携带口袋式计算机，这一愿景在现代智能手机上得到了实现。

文章最后对莫奇利的品格进行了回顾。作者引用了 J. 普雷斯珀·埃克特在悼词中的话，将莫奇利描述为一位“卓越”的创新者，同时也是一位“正直的人”。基斯拉特中心邀请公众探索莫奇利的丰富藏品，以进一步了解这位助力开启现代计算机工业的伟人。

---

## 5. 选择乏味的技术 (2015)

**原文标题**: Choose Boring Technology (2015)

**原文链接**: [https://mcfunley.com/choose-boring-technology](https://mcfunley.com/choose-boring-technology)

在《选择乏味的技术》中，丹·麦金利（Dan McKinley）认为，公司的成功取决于其专注于核心业务使命而非技术新颖性的能力。他提出了“**创新令牌**”（innovation tokens）的概念：这是一种有限的资源（通常约为三个），公司可以将其用于采用新技术或未经证实的技术。在“光鲜亮丽”的工具（如新数据库或新语言）上过度消耗这些令牌，会分散公司对实际目标的关键注意力。

**乏味 vs. 光鲜**
麦金利将“乏味”技术（如 Postgres、Python、Memcached）定义为能力已被充分理解，且更重要的是其故障模式也已被充分理解的工具。新技术充满风险，因为它们充斥着“未知的未知数”。虽然它们看起来令人兴奋，但危机期间不可预测的表现会产生沉重的运维负担，甚至可能“压垮”团队。

**全局优化**
作者对“最适合该工作的工具”这一观念提出了挑战，称其为忽略了“全局”成本的局部优化。每一项新技术都会以运维开销、监控和认知负荷的形式增加永久性的“税收”。因此，“最佳”工具往往是现有技术栈中“最不差”的选择。开发人员应致力于用最少的一套工具解决尽可能多的问题。

**采用新技术**
麦金利建议采用严谨的流程来引入新技术：
1. **穷尽现有工具**：首先尝试用当前技术栈解决问题。
2. **定义差距**：明确说明为什么当前技术栈在处理此特定任务时成本极高或极其困难。
3. **承诺迁移**：如果新工具是为了替代旧工具，必须有迁移旧功能的计划，以防止留下“残骸”。

最终的目标是“**交付即可**”（Just Ship）。通过选择乏味的技术，工程师可以获得认知上的自由，去解决有意义的业务问题，而不是把时间浪费在基础设施管理上。

---

## 6. DeepSeek Harness 开发者预览版

**原文标题**: DeepSeek Harness developer preview

**原文链接**: [https://deepseek.com/harness/en/](https://deepseek.com/harness/en/)

DeepSeek 宣布推出 DeepSeek Harness (DSH) 开发者预览版，这是一个旨在构建、管理和部署 AI 智能体（AI Agents）的开源框架。该平台秉持“一切皆插件”的核心理念，允许开发者在不修改源代码的情况下，自由更换或重组包括模型、工具、沙箱、存储和 UI 在内的每一项能力。

DSH 基于 Cordis 内核构建，通过管理插件依赖和事件来确保高度模块化的环境。它将智能体定义为“模型”（灵魂）与“Harness”（环境和工具）的结合。

核心特性包括：
*   **全流程可追溯性：** 每一次交互（包括推理、工具调用和上下文注入）都会记录在仅追加的会话日志中。这实现了“轨迹视图”，用户可以恢复、派生、搜索或重放事件流中的任何部分。
*   **多种运行模式：** 
    *   **Standard（标准模式）：** 具备完整网页和文件搜索能力的综合性编码智能体。
    *   **Code（代码模式）：** 利用 TypeScript SDK 允许模型在单个程序中编排复杂的多步操作。
    *   **Minimal（极简模式）：** 仅包含 Shell 和文件编辑器的轻量化环境，针对模型基准测试进行了优化。
    *   **Creator（创作者模式）：** 用于检查运行时并编写自定义智能体预设的专用模式。

DeepSeek Harness 目前已面向全球开放测试。开发者可以通过运行 `npx @deepseek-ai/dsh web` 或从 GitHub 克隆仓库开始体验。该项目旨在培育一个可复用、可组合的智能体基础设施开源生态系统。

---

## 7. 吐火罗语在线

**原文标题**: Tocharian Online

**原文链接**: [https://lrc.la.utexas.edu/eieol/tokol/0](https://lrc.la.utexas.edu/eieol/tokol/0)

"Tocharian Online" provides a comprehensive introduction to Tocharian A and B, two distinct but closely related Indo-European languages discovered in the Tarim Basin of East Turkestan (modern-day Xinjiang). Recovered from Silk Road sites like Turfan and Kučā, the surviving documents date primarily between the 6th and 8th centuries AD.

While most Tocharian texts are Buddhist translations written in a variant of the Brāhmī script, secular documents—such as caravan passes and business letters—exist exclusively in Tocharian B. This leads scholars to suggest that Tocharian A may have already been an extinct liturgical language, similar to Latin, by the time these records were created.

The name "Tocharian" is a historical misnomer. Early 20th-century scholars mistakenly identified the language with the "Toxrï" people of Bactria; however, research now shows these groups were distinct. Native terms for the languages likely included *ārśi* (Tocharian A) and *kuśiññe* (Tocharian B).

Tocharian holds a unique place in historical linguistics as the easternmost Indo-European language. Surprisingly, it is a "centum" language—a characteristic usually reserved for western branches like Celtic and Germanic. This discovery overturned previous theories that divided Indo-European dialects strictly by geography. Furthermore, the language features a reduced phonetic inventory (lacking voiced stops like *b, d, g*) and an agglutinative case system. These features suggest a long period of contact with non-Indo-European families, such as Turkic, Uralic, and Mongolian. 

The article serves as a preface to a series of lessons from the University of Texas at Austin aimed at documenting and preserving these ancient languages.

---

## 8. How art invented humanity

**原文标题**: How art invented humanity

**原文链接**: [https://aeon.co/essays/humans-did-not-invent-art-it-was-the-other-way-around](https://aeon.co/essays/humans-did-not-invent-art-it-was-the-other-way-around)

生成摘要时出错

---

## 9. Gloomberb

**原文标题**: Gloomberb

**原文链接**: [https://gloom.sh/](https://gloom.sh/)

生成摘要时出错

---

## 10. Kubernetes on Oxide: How customer needs shaped our integrations

**原文标题**: Kubernetes on Oxide: How customer needs shaped our integrations

**原文链接**: [https://oxide.computer/blog/kubernetes-on-oxide](https://oxide.computer/blog/kubernetes-on-oxide)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 2 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 3 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 4 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 5 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 6 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 7 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 8 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 9 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 10 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 11 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 12 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 13 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 14 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 15 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 16 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 17 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 18 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 19 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 20 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 21 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 22 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 23 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 24 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 25 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 26 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 27 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 28 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 29 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 30 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 31 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 32 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 33 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 34 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 35 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 36 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 37 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 38 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 39 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 40 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 41 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 42 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 43 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 44 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 45 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 46 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 47 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 48 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 49 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 50 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 51 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 52 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 53 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 54 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 55 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 56 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 57 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 58 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 59 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 60 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 61 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 62 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 63 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 64 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 65 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 66 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 67 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 68 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 69 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 70 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 71 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 72 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 73 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 74 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 75 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 76 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 77 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 78 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 79 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 80 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 81 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 82 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 83 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 84 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 85 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 86 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 87 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 88 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 89 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 90 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 91 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 92 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 93 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 94 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 95 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 96 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 97 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 98 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 99 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 100 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 101 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 102 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 103 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 104 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 105 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 106 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 107 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 108 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 109 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 110 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 111 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 112 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 113 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 114 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 115 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 116 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 117 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 118 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 119 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 120 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 121 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 122 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 123 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 124 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 125 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 126 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 127 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 128 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 129 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 130 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 131 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 132 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 133 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 134 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 135 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 136 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 137 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 138 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 139 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 140 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 141 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 142 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 143 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 144 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 145 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 146 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 147 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 148 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 149 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 150 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 151 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 152 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 153 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 154 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 155 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 156 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 157 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 158 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 159 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 160 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 161 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 162 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 163 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 164 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 165 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 166 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 167 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 168 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 169 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 170 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 171 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 172 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 173 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 174 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 175 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 176 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 177 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 178 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 179 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 180 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 181 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 182 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 183 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 184 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 185 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 186 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 187 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 188 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 189 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 190 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 191 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 192 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 193 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 194 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 195 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 196 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 197 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 198 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 199 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 200 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 201 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 202 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 203 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 204 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 205 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 206 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 207 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 208 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 209 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 210 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 211 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 212 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 213 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 214 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 215 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 216 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 217 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 218 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 219 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 220 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 221 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 222 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 223 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 224 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 225 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 226 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 227 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 228 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 229 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 230 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 231 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 232 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 233 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 234 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 235 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 236 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 237 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 238 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 239 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 240 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 241 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 242 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 243 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 244 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 245 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 246 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 247 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 248 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 249 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 250 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 251 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 252 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 253 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 254 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 255 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 256 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 257 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 258 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 259 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 260 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 261 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 262 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 263 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 264 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 265 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 266 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 267 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 268 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 269 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 270 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 271 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 272 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 273 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 274 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 275 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 276 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 277 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 278 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 279 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 280 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 281 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 282 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 283 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 284 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 285 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 286 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 287 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 288 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 289 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 290 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 291 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 292 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 293 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 294 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 295 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 296 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 297 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 298 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 299 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 300 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 301 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 302 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 303 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 304 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 305 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 306 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 307 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 308 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 309 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 310 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 311 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 312 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 313 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 314 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 315 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 316 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 317 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 318 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 319 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 320 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 321 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 322 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 323 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 324 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 325 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 326 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 327 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 328 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 329 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 330 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 331 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 332 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 333 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 334 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 335 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 336 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 337 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 338 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 339 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 340 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 341 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 342 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 343 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 344 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 345 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 346 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 347 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 348 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 349 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 350 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 351 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 352 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 353 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 354 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 355 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 356 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 357 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 358 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 359 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 360 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 361 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 362 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 363 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 364 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 365 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 366 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 367 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 368 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 369 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 370 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 371 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 372 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 373 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 374 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 375 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 376 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 377 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 378 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 379 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 380 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 381 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 382 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 383 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 384 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 385 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 386 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 387 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 388 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 389 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 390 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 391 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 392 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 393 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 394 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 395 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 396 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 397 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 398 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 399 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 400 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 401 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 402 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 403 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 404 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 405 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 406 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 407 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 408 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 409 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 410 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 411 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 412 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 413 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 414 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 415 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 416 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 417 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 418 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 419 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 420 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 421 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 422 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 423 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 424 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 425 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 426 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 427 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 428 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 429 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 430 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 431 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 432 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 433 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 434 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 435 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 436 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 437 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 438 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 439 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 440 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 441 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 442 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 443 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 444 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 445 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 446 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 447 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 448 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 449 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 450 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 451 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 452 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 453 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 454 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 455 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 456 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 457 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 458 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 459 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 460 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 461 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 462 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 463 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 464 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 465 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 466 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 467 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 468 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 469 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 470 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 471 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 472 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 473 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 474 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 475 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 476 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 477 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 478 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 479 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 480 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 481 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 482 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 483 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 484 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 485 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 486 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 487 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 488 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 489 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 490 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 491 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 492 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 493 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 494 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 495 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 496 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 497 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 498 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 499 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 500 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 501 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 502 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 503 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 504 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 505 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 506 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 507 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 508 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 509 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 510 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
