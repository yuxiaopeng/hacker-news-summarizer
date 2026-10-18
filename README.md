# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-18.md)

*最后自动更新时间: 2026-10-18 19:44:26*
## 1. RepRap微米

**原文标题**: RepRapMicron

**原文链接**: [https://github.com/VikOlliver/RepRapMicron/wiki](https://github.com/VikOlliver/RepRapMicron/wiki)

**RepRapMicron (μRepRap)** 是一款开源、可自我复制的 3D 打印机，专为利用常见易得的材料进行微米（1μm）及亚微米级制造而设计。受 OpenFlexure 项目显微镜平台的启发，该项目旨在通过提供低成本方案来替代昂贵的、以硅为核心的工业工艺，从而推动微制造（如微电子和微机电系统 MEMS）的普及。

当前推荐的硬件版本 **PIKA V0.02** 在 8mm 立方行程空间内具有约 1μm 的重复定位精度和 10μm 的可靠精度。它已成功沉积了 4μm 的 UV 树脂液滴并固化出 9μm 的线条。早期版本 **MAUS** 曾作为柔性机构组件的测试平台，但现已被精度更高的 PIKA 系统取代。

**技术规格与能力：**
*   **机械结构：** 系统采用 3D 打印的柔性机构（Flexures），由 NEMA17 步进电机驱动，并通过 GCODE（通常使用 Arduino GRBL）进行控制。
*   **打印头：** 探针具有多样性，包括用于机械刻蚀的皮下注射针头，以及用于毛细沉积的电化学蚀刻金属丝。此外，还可以使用光纤传输 UV 光以实现精密固化。
*   **材料：** 主要使用 UV 固化树脂（如指甲油胶）和离子凝胶进行制造。由于氧气会抑制薄层树脂的固化，系统采用了特定技术以确保结构完整性。
*   **监控：** 由于在该尺度下无法进行人工操作，系统使用 USB 显微镜进行对准，并辅以台式显微镜进行检查。

μRepRap 项目的最终目标是创建一个自我进化的微制造生态系统。除了基础打印外，该项目正在开发分离、运输和组装微米级组件的方法，旨在最终实现一个能够在更小尺度上自我复制的系统。

---

## 2. 软件背后的人

**原文标题**: Someone behind the software

**原文链接**: [https://karrisaarinen.com/posts/someone-behind-the-software/](https://karrisaarinen.com/posts/someone-behind-the-software/)

《软件背后的人》一文指出，卓越的产品拥有一种源自创造者独特视角与直觉的“灵魂”或性格。作者将此与行业内将软件视为受制于严苛流程和数据的“工厂式”产出的倾向进行对比，断言真正的品质源于人类的判断与经验。

在 Linear 这样的公司，直觉的重要性优于冰冷的数据。这种直觉并非简单的个人偏好，而是一种通过深度接触客户并从错误中学习而不断沉淀的观点。产品的独特性不仅取决于创造者选择优先做什么，更关键在于他们决定“不”做什么。

然而，作者观察到一个令人担忧的趋势：产品正变得愈发“臃肿”且“盲目堆砌”。许多公司不再致力于完善核心解决方案，而是专注于技术“能”做什么，导致功能碎片化。AI 智能体和自动化流程的兴起加剧了这一现象，因为它们允许在缺乏统一愿景的情况下进行独立变更。如果没有共同的视角，软件就有可能沦为“弗兰肯斯坦式的怪物”——即自动化产出的平庸均值，而非一件精雕细琢的雕塑。

作者总结道，随着自动化降低了开发门槛，创造者应利用由此节省的精力去构建更深邃的视角。其核心目标是摆脱“工厂”思维，确保用户在使用工具时，依然能感受到背后的人文意图与匠心。

---

## 3. 业主协会正加剧住房危机

**原文标题**: HOA's are making the home crisis worse

**原文链接**: [https://hoaspy.com/hoa/fl/florida-hoa-housing-crisis.html](https://hoaspy.com/hoa/fl/florida-hoa-housing-crisis.html)

佛罗里达州的业主协会（HOA）和公寓协会通过推高成本、阻碍销售和激进地驱逐居民，显著加剧了该州的住房危机。目前，佛罗里达州在协会相关法律诉讼方面居全国之首，占全美所有 HOA 止赎诉讼的 73% 以及所有 HOA 相关诉讼的三分之一。

文章强调了这些协会加剧危机的五种主要方式：

1. **激进的止赎：** 协会经常因相对较小的债务对成员行使止赎权。一旦提交留置权申请，滞纳金、利息和法律费用会导致债务膨胀，往往迫使业主进入高压拍卖程序。
2. **留置权导致的市场停滞：** 随着超过 460,000 份记录在案的留置权，许多房主无法出售房产或进行再融资，因为产权公司和贷款机构在协会的法律索赔结清之前不会受理。
3. **成本飙升：** 在瑟夫赛德（Surfside）公寓倒塌事故后，新的州法律（SB 4-D）强制要求进行结构检查和足额拨备储备金。这引发了月费和专项评估费的大幅飙升（在主要城市涨幅超过 16%），同时也导致了公寓市场价值的下跌。
4. **持续的诉讼：** 协会经常动用成员缴纳的会费参与耗资巨大的法律诉讼。佛罗里达州在涉及协会的保险纠纷和民权诉讼方面领先全美。
5. **企业管理不善：** 佛罗里达州约有 6% 的协会存在企业状态失效或违规的情况，这可能导致相关社区内的所有房产交易停滞。

该报告建议潜在买家在购买前严格审计协会的诉讼历史、储备金研究和预算。对于政策制定者，报告建议救济措施可能需要限制协会通过留置权收取的费用上限，并提高强制性收费的透明度。

---

## 4. Mitos 编辑器是 Helix 的一个分支。

**原文标题**: Mitos editor is a fork of Helix

**原文链接**: [https://mitos.computer/](https://mitos.computer/)

Mitos 是一款“开箱即用”的模态文本编辑器，是 Helix 编辑器的一个分支。它专为现代开发设计，其工作流程以基于选择的编辑模型为核心，并内置多光标支持，允许用户同时操作多个位置。

Mitos 的主要特性包括：

*   **先进的工具链：** 它利用语言服务器协议 (LSP) 实现代码补全、诊断和格式化，并结合调试适配协议 (DAP) 提供断点和变量检查等集成调试功能。
*   **语法智能：** 通过利用 Tree-sitter，该编辑器提供高质量的语法高亮、语法感知文本对象以及结构化导航。
*   **独特的终端功能：** 与许多基于终端的编辑器不同，Mitos 支持在终端内直接预览图像。
*   **导航与搜索：** 该编辑器包含内置的文件浏览器、用于快速导航的文件选择器，以及跨工作区的全局搜索功能。

总体而言，Mitos 将自己定位为一个功能丰富的基于终端的环境，开箱即用地集成了核心语言工具和调试工具。

---

## 5. PalmOS 版《百战小旅鼠》，作者 Aaron Ardiri

**原文标题**: PalmOS Lemmings by Aaron Ardiri

**原文链接**: [https://github.com/ardiri/palmos-lemmings](https://github.com/ardiri/palmos-lemmings)

本文介绍了由 Aaron Ardiri 开发的经典游戏《百战小兵》（Lemmings）PalmOS 版本的发布。作者以“原样”形式提供了该游戏的源代码，专门用于教学目的。除代码外，该资源还包含该游戏在 PalmOS 平台上运行的截图。它为那些对早期移动游戏开发和软件工程感兴趣的人士提供了技术参考。

---

## 6. Java 密封类与穷举模式匹配

**原文标题**: Java sealed classes and exhaustive pattern matching

**原文链接**: [https://neilmadden.blog/2026/04/24/java-sealed-classes-and-exhaustive-pattern-matching/](https://neilmadden.blog/2026/04/24/java-sealed-classes-and-exhaustive-pattern-matching/)

本文探讨了 Java 17 中引入的**密封类**（sealed classes）的影响，特别是它们与**穷举模式匹配**（exhaustive pattern matching）之间的交互。

密封类允许开发者限制哪些子类型可以实现接口或继承类。这使得编译器能够在 `switch` 表达式中执行“穷举性检查”。如果涵盖了所有允许的子类型，则无需 `default` 子句；而如果缺失了某个分支，编译器将报错。

然而，作者指出一个重大风险：向密封类添加新的子类型属于**破坏性变更**。在标准的开发环境中，这会导致任何未处理新分支的使用方出现编译时错误。

关键的是，作者警告了**独立编译**的问题。如果库通过添加新子类型更新了密封接口，但该库的使用方并未重新编译，那么穷举性检查将在**运行时**而非编译时失败。这将导致 `MatchException`，并可能引发意想不到的应用崩溃。

**核心结论：**
*   **内部使用**：在所有代码都会统一重新编译的单个组件或项目中，密封类非常有益，因为它们提供了强大的安全保障。
*   **公共 API**：在公共 API 或库中公开密封类型存在风险。这限制了 API 的演进，因为添加新分支可能会破坏下游使用方的代码。
*   **设计建议**：开发者在面向公众的代码中使用密封接口时应保持谨慎（文中以即将推出的 PEM 编码对象支持为例，指出其可能成为该设计缺陷的受害者），以避免向用户强加破坏性变更。

---

## 7. 英特尔 8087 芯片：浮点加法与减法

**原文标题**: The Intel 8087 chip: floating-point addition and subtraction

**原文链接**: [https://www.righto.com/2026/10/8087-addition-subtraction-microcode.html](https://www.righto.com/2026/10/8087-addition-subtraction-microcode.html)

本文深入探讨了1980年英特尔8087浮点协处理器的内部架构和微代码，特别是其加法和减法的具体实现。通过将这些运算从8086 CPU卸载到专用硬件，8087实现了近100倍的速度提升。

**硬件与数据格式**
8087采用了包含1,648条指令的微代码ROM和80位数据通路。它以“临时实数”（temporary real）格式处理数字，其中包括1个符号位、15位偏移阶码和64位尾数。关键硬件组件包括：
*   **69位整数加法器：** 处理核心算术运算。
*   **桶形移位器：** 通过移位快速对齐小数点并规格化结果。
*   **前导零电路：** 计算零的个数，以确定规格化所需的移位量。

**加法/减法过程**
该芯片遵循严格的多步流程来处理浮点逻辑：
1.  **对齐：** 微代码比较阶码，并将较小值的尾数向右移位，直到小数点对齐。
2.  **执行：** 芯片对尾数进行整数加法或减法。文中指出其使用了“无符号”逻辑；例如，正数与负数相加在内部被作为减法处理。
3.  **规格化：** 运算完成后，对结果进行移位以确保首位为1，并相应调整阶码。
4.  **特殊情况：** 微代码包含处理零、无穷大和“NaN”（非数）值的特定例程。

通过将专用电路与复杂的微代码子例程相结合，8087处理高精度80位计算的效率远高于同时代基于软件的整数模拟。

---

## 8. Sigsaly: Churchill's top secret hotline to the President

**原文标题**: Sigsaly: Churchill's top secret hotline to the President

**原文链接**: [https://www.iwm.org.uk/history/iwm/cwr/telephone](https://www.iwm.org.uk/history/iwm/cwr/telephone)

During the Second World War, the need for secure communication between British Prime Minister Winston Churchill and U.S. President Franklin D. Roosevelt led to the development of **SIGSALY**, the world’s first truly secure digital voice encryption system.

Developed by Bell Telephone Laboratories as "Project X," SIGSALY utilized cutting-edge technology that digitized the human voice and masked it with random noise. To decrypt the signal, operators at both ends had to play identical noise-generating records in perfect synchronization. Because these records were destroyed after a single use, conversations had to be pre-scheduled rather than spontaneous.

The system was both massive and highly classified. Each terminal weighed over 50 tons and cost $1 million (in 1943 values). Of the twelve terminals installed globally, the London hub was hidden in the basement of Selfridges department store. To maintain absolute secrecy, an extension to the Churchill War Rooms was disguised as a private toilet intended only for the Prime Minister’s use.

While Churchill and Roosevelt first used the link in April 1944, the system ultimately facilitated over 3,000 secure conversations among Allied military and political leaders, including vital post-war planning between Churchill and Harry S. Truman. 

The existence of SIGSALY serves as a powerful symbol of the "Special Relationship" between the U.S. and the U.K. The immense investment of resources, manpower, and technology required to maintain the hotline underscored the level of trust and cooperation necessary for the Allied victory. Today, visitors to the Churchill War Rooms can still see the secret cupboard where these historic calls took place.

---

## 9. DeepSeek search and fetch – $0.75 per 1000 successful requests

**原文标题**: DeepSeek search and fetch – $0.75 per 1000 successful requests

**原文链接**: [https://api-docs.deepseek.com/guides/search/](https://api-docs.deepseek.com/guides/search/)

DeepSeek 推出了 **Search** 和 **Fetch** API，旨在为智能体（Agent）和 RAG 应用提供实时网络内容访问。两者均为原生 JSON API，通过 DeepSeek API 基础 URL 使用标准的 Bearer 令牌进行身份验证。

### 核心功能
*   **Search API**：利用 DeepSeek 内部引擎搜索网页。它返回包括标题、片段、长摘要（600-800 字符）和重排序分数在内的结构化结果，并支持按网站、语言和日期过滤的高级操作符。
*   **Fetch API**：获取特定 URL 的内容并将其直接转换为 Markdown 格式，便于大语言模型（LLM）处理。

### 定价与计费
两个 API 的定价均为 **每 1,000 次成功请求 0.75 美元**。值得注意的是，仅对成功的“命中”计费：
*   **Search** 仅在返回非空结果数组时计费。
*   **Fetch** 仅在成功返回页面内容时计费。
*   请求失败、超时和空结果均免费。
*   **注**：虽然直接使用 API 目前已开始计费，但通过 DeepSeek Harness 或 Claude Code 进行的服务端工具调用在 **2026 年 11 月 1 日**之前仍保持免费。

### 速率限制与性能
*   **QPS 限制**：每个账户的两个 API 均限制为 **每秒 5 次请求 (QPS)**。
*   **Fetch 约束**：Fetch 受目标网站访问政策及额外的分域名速率限制。
*   **质量信号**：搜索结果包含 `rerank_score` (0–3) 和 `authority` 分级 (0–4)，帮助应用程序优先处理高质量数据。

错误处理遵循 OpenAI 兼容格式，并设有针对余额不足 (402)、速率限制 (429) 和安全屏蔽 (403) 的特定 HTTP 代码。

---

## 10. Legal experts warn Meta's new terms still grant broad scraping permissions

**原文标题**: Legal experts warn Meta's new terms still grant broad scraping permissions

**原文链接**: [https://www.niemanlab.org/2026/10/legal-experts-warn-metas-new-terms-still-grant-broad-scraping-permissions-despite-language-changes/](https://www.niemanlab.org/2026/10/legal-experts-warn-metas-new-terms-still-grant-broad-scraping-permissions-despite-language-changes/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 2 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 3 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 4 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 5 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 6 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 7 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 8 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 9 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 10 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 11 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 12 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 13 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 14 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 15 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 16 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 17 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 18 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 19 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 20 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 21 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 22 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 23 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 24 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 25 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 26 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 27 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 28 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 29 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 30 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 31 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 32 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 33 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 34 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 35 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 36 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 37 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 38 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 39 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 40 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 41 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 42 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 43 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 44 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 45 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 46 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 47 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 48 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 49 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 50 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 51 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 52 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 53 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 54 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 55 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 56 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 57 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 58 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 59 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 60 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 61 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 62 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 63 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 64 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 65 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 66 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 67 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 68 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 69 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 70 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 71 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 72 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 73 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 74 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 75 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 76 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 77 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 78 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 79 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 80 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 81 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 82 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 83 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 84 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 85 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 86 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 87 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 88 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 89 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 90 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 91 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 92 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 93 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 94 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 95 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 96 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 97 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 98 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 99 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 100 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 101 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 102 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 103 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 104 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 105 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 106 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 107 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 108 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 109 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 110 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 111 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 112 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 113 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 114 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 115 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 116 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 117 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 118 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 119 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 120 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 121 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 122 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 123 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 124 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 125 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 126 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 127 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 128 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 129 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 130 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 131 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 132 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 133 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 134 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 135 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 136 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 137 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 138 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 139 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 140 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 141 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 142 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 143 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 144 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 145 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 146 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 147 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 148 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 149 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 150 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 151 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 152 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 153 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 154 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 155 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 156 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 157 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 158 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 159 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 160 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 161 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 162 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 163 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 164 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 165 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 166 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 167 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 168 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 169 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 170 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 171 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 172 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 173 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 174 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 175 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 176 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 177 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 178 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 179 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 180 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 181 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 182 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 183 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 184 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 185 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 186 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 187 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 188 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 189 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 190 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 191 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 192 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 193 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 194 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 195 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 196 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 197 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 198 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 199 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 200 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 201 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 202 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 203 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 204 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 205 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 206 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 207 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 208 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 209 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 210 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 211 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 212 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 213 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 214 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 215 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 216 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 217 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 218 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 219 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 220 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 221 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 222 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 223 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 224 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 225 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 226 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 227 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 228 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 229 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 230 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 231 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 232 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 233 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 234 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 235 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 236 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 237 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 238 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 239 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 240 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 241 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 242 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 243 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 244 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 245 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 246 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 247 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 248 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 249 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 250 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 251 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 252 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 253 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 254 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 255 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 256 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 257 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 258 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 259 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 260 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 261 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 262 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 263 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 264 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 265 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 266 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 267 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 268 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 269 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 270 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 271 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 272 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 273 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 274 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 275 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 276 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 277 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 278 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 279 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 280 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 281 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 282 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 283 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 284 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 285 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 286 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 287 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 288 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 289 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 290 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 291 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 292 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 293 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 294 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 295 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 296 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 297 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 298 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 299 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 300 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 301 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 302 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 303 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 304 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 305 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 306 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 307 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 308 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 309 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 310 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 311 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 312 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 313 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 314 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 315 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 316 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 317 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 318 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 319 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 320 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 321 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 322 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 323 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 324 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 325 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 326 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 327 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 328 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 329 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 330 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 331 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 332 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 333 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 334 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 335 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 336 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 337 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 338 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 339 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 340 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 341 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 342 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 343 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 344 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 345 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 346 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 347 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 348 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 349 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 350 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 351 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 352 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 353 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 354 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 355 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 356 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 357 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 358 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 359 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 360 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 361 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 362 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 363 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 364 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 365 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 366 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 367 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 368 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 369 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 370 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 371 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 372 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 373 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 374 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 375 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 376 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 377 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 378 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 379 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 380 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 381 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 382 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 383 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 384 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 385 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 386 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 387 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 388 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 389 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 390 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 391 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 392 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 393 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 394 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 395 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 396 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 397 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 398 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 399 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 400 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 401 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 402 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 403 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 404 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 405 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 406 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 407 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 408 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 409 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 410 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 411 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 412 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 413 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 414 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 415 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 416 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 417 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 418 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 419 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 420 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 421 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 422 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 423 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 424 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 425 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 426 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 427 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 428 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 429 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 430 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 431 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 432 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 433 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 434 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 435 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 436 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 437 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 438 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 439 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 440 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 441 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 442 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 443 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 444 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 445 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 446 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 447 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 448 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 449 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 450 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 451 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 452 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 453 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 454 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 455 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 456 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 457 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 458 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 459 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 460 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 461 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 462 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 463 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 464 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 465 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 466 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 467 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 468 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 469 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 470 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 471 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 472 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 473 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 474 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 475 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 476 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 477 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 478 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 479 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 480 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 481 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 482 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 483 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 484 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 485 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 486 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 487 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 488 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 489 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 490 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 491 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 492 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 493 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 494 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 495 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 496 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 497 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 498 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 499 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 500 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 501 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 502 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 503 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 504 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 505 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 506 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 507 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 508 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 509 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 510 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 511 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 512 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 513 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 514 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 515 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 516 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 517 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 518 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 519 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 520 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 521 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 522 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 523 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 524 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 525 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 526 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 527 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 528 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 529 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 530 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 531 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 532 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 533 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 534 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 535 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 536 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 537 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 538 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 539 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 540 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 541 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 542 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 543 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 544 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 545 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 546 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 547 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 548 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 549 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 550 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 551 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 552 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 553 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 554 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 555 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 556 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 557 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 558 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 559 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 560 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 561 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 562 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 563 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 564 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 565 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 566 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 567 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 568 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 569 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 570 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 571 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 572 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 573 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 574 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 575 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
