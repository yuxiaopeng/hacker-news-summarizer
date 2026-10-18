# Hacker News 热门文章摘要 (2026-10-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: The Zelda timeline to catch up before the Ocarina of Time remake

**原文标题**: Show HN: The Zelda timeline to catch up before the Ocarina of Time remake

**原文链接**: [https://legendofhyrule.com/](https://legendofhyrule.com/)

This article provides a comprehensive overview of *The Legend of Zelda*’s complex chronology to prepare players for a potential *Ocarina of Time* remake. The narrative spans from the world’s creation by the Golden Goddesses to the distant "Era of Myth."

The history begins with **Skyward Sword**, establishing the eternal conflict between the goddess Hylia and the Demon King Demise. However, **Ocarina of Time** serves as the timeline's ultimate pivot point. Depending on the outcome of Link’s battle with Ganondorf, the history splits into three distinct branches:

1.  **The Fallen Hero Era:** Link is defeated, leading to the Imprisoning War. This branch contains the classic titles, including *A Link to the Past*, the original NES games, and the recent *Echoes of Wisdom*.
2.  **The Child Era:** Link is sent back to his childhood and warns Zelda of Ganondorf’s treachery, leading to the events of *Majora’s Mask* and *Twilight Princess*.
3.  **The Adult Era:** Following Link’s departure from the future, Hyrule is eventually flooded by the gods to seal Ganon, leading to the seafaring adventures of *The Wind Waker* and the founding of "New Hyrule" in *Spirit Tracks*.

The timeline eventually reaches a distant future—tens of thousands of years later—where previous events have faded into legend. This era encompasses **Breath of the Wild** and **Tears of the Kingdom**, focusing on the ancient Zonai civilization and the recurring threat of Calamity Ganon. By mapping these eras, the article contextualizes the entire franchise, illustrating how the cycle of the Triforce connects every iteration of Link, Zelda, and Ganon across different realities.

---

## 12. Investing in the Public Benefit

**原文标题**: Investing in the Public Benefit

**原文链接**: [https://www.anthropic.com/news/public-benefit-fund](https://www.anthropic.com/news/public-benefit-fund)

生成摘要时出错

---

## 13. Open MicroManipulator – A sub-micrometer 3D motion control plattform

**原文标题**: Open MicroManipulator – A sub-micrometer 3D motion control plattform

**原文链接**: [https://github.com/0x23/MicroManipulatorStepper](https://github.com/0x23/MicroManipulatorStepper)

The **Open MicroManipulator** is an open-source, low-cost motorized XYZ motion control platform designed for sub-micrometer precision (steps down to 50nm). It is optimized for high-accuracy applications such as microscopy, optical alignment, and electronics probing.

**Key Technical Features:**
*   **Mechanical Design:** Utilizing a parallel kinematic structure with miniature ball joints, the device offers high stiffness and a large range of motion. While parts can be 3D printed, CNC milling is recommended to minimize thermal drift.
*   **Hardware:** The system uses off-the-shelf stepper motors and a "magnetic gearing" approach that increases the resolution of affordable rotary encoders by a factor of 30. The latest hardware version (v4.0) improves linkage manufacturing and fixes previous self-collision issues.
*   **Electronics & Firmware:** The platform runs on a 30 kHz closed-loop controller with a motion planning stack featuring look-ahead capabilities. The electronics utilize a simple PCB (KiCAD) designed for accessibility, requiring no SMD soldering.

**Control and Integration:**
The device is controlled via simple G-Code commands over a USB serial interface. To facilitate ease of use, the project provides:
*   **A Python API:** For serial communication, calibration, and movement execution.
*   **A Graphical User Interface (GUI):** Featuring manual controls, a G-Code runner, and a live camera feed for real-time monitoring.
*   **Tool Support:** Recent firmware updates (v1.0.4) enable PWM-controlled tools via GPIO pins for applications like laser engraving.

**Accessibility:**
The project is fully open-source, utilizing FreeCAD and PlatformIO. Documentation includes a comprehensive Bill of Materials (BOM), setup guides, and a community Discord server for troubleshooting and discussion. Users are encouraged to contribute to the build guides or support the project via Ko-fi.

---

## 14. Beyond Tetris: The Other Games of Alexey Pajitnov [video]

**原文标题**: Beyond Tetris: The Other Games of Alexey Pajitnov [video]

**原文链接**: [https://www.youtube.com/watch?v=QH_LPimUJMs](https://www.youtube.com/watch?v=QH_LPimUJMs)

生成摘要时出错

---

## 15. Namecheap just seized and disabled all my domains

**原文标题**: Namecheap just seized and disabled all my domains

**原文链接**: [https://www.reddit.com/r/sysadmin/comments/1x8cycd/namecheap_just_seized_and_disabled_all_my_domains/](https://www.reddit.com/r/sysadmin/comments/1x8cycd/namecheap_just_seized_and_disabled_all_my_domains/)

生成摘要时出错

---

## 16. Free Pascal Compiler Now Supports Dynamic Packages

**原文标题**: Free Pascal Compiler Now Supports Dynamic Packages

**原文链接**: [https://www.getlazarus.org/dynamic/](https://www.getlazarus.org/dynamic/)

生成摘要时出错

---

## 17. How the Elizabeth Holmes documentary “You Can See Everything” is deceiving

**原文标题**: How the Elizabeth Holmes documentary “You Can See Everything” is deceiving

**原文链接**: [https://www.readtheprofile.com/p/elizabeth-holmes-documentary-you-can-see-everything](https://www.readtheprofile.com/p/elizabeth-holmes-documentary-you-can-see-everything)

生成摘要时出错

---

## 18. macOS 15.8.2 Breaks OpenGL

**原文标题**: macOS 15.8.2 Breaks OpenGL

**原文链接**: [https://developer.apple.com/forums/verify-human/verify.html?next=/forums/thread/850550](https://developer.apple.com/forums/verify-human/verify.html?next=/forums/thread/850550)

生成摘要时出错

---

## 19. Parser Combinators

**原文标题**: Parser Combinators

**原文链接**: [https://t3.at/blog/2026-10-17-parser-combinators/](https://t3.at/blog/2026-10-17-parser-combinators/)

生成摘要时出错

---

## 20. I Electrified My Push Scooter with a Power Drill

**原文标题**: I Electrified My Push Scooter with a Power Drill

**原文链接**: [https://eddieabbondanz.io/post/shop/drill-powered-scooter/](https://eddieabbondanz.io/post/shop/drill-powered-scooter/)

生成摘要时出错

---

## 21. CKKS – Addition and Multiplication

**原文标题**: CKKS – Addition and Multiplication

**原文链接**: [https://www.jeremykun.com/2026/10/11/ckks-addition-and-multiplication/](https://www.jeremykun.com/2026/10/11/ckks-addition-and-multiplication/)

生成摘要时出错

---

## 22. Will it be a golden age or a dark age for mathematics (and science)?

**原文标题**: Will it be a golden age or a dark age for mathematics (and science)?

**原文链接**: [https://terrytao.wordpress.com/2026/10/18/will-it-be-a-golden-age-or-a-dark-age-for-mathematics-and-science/](https://terrytao.wordpress.com/2026/10/18/will-it-be-a-golden-age-or-a-dark-age-for-mathematics-and-science/)

生成摘要时出错

---

## 23. The Electronic Disturbance Theater and Electronic Civil Disobedience (1998)

**原文标题**: The Electronic Disturbance Theater and Electronic Civil Disobedience (1998)

**原文链接**: [https://www.thing.net/~rdom/ecd/EDTECD.html](https://www.thing.net/~rdom/ecd/EDTECD.html)

生成摘要时出错

---

## 24. Voyage of the Paper Canoe: 2500 Miles from Quebec to the Gulf of Mexico, 1874-5

**原文标题**: Voyage of the Paper Canoe: 2500 Miles from Quebec to the Gulf of Mexico, 1874-5

**原文链接**: [http://www.ibiblio.org/eldritch/nhb/paperc/intro.html](http://www.ibiblio.org/eldritch/nhb/paperc/intro.html)

生成摘要时出错

---

## 25. Teal – A statically-typed dialect of Lua

**原文标题**: Teal – A statically-typed dialect of Lua

**原文链接**: [https://teal-language.org/](https://teal-language.org/)

生成摘要时出错

---

## 26. Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping

**原文标题**: Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping

**原文链接**: [https://sphinx-six-theta.vercel.app/](https://sphinx-six-theta.vercel.app/)

生成摘要时出错

---

## 27. The Brain Sandwich

**原文标题**: The Brain Sandwich

**原文链接**: [https://terriblesoftware.org/2026/10/02/the-brain-sandwich/](https://terriblesoftware.org/2026/10/02/the-brain-sandwich/)

生成摘要时出错

---

## 28. CFPB Opens Debanking Investigation into Nine Large National Banks

**原文标题**: CFPB Opens Debanking Investigation into Nine Large National Banks

**原文链接**: [https://www.forbes.com/sites/ajdhaliwal/2026/10/16/cfpb-opens-debanking-investigation-into-nine-large-national-banks/](https://www.forbes.com/sites/ajdhaliwal/2026/10/16/cfpb-opens-debanking-investigation-into-nine-large-national-banks/)

生成摘要时出错

---

## 29. Hatching (Heraldry)

**原文标题**: Hatching (Heraldry)

**原文链接**: [https://en.wikipedia.org/wiki/Hatching_(heraldry)](https://en.wikipedia.org/wiki/Hatching_(heraldry))

生成摘要时出错

---

## 30. Regex visualized as 3D marble run

**原文标题**: Regex visualized as 3D marble run

**原文链接**: [https://www.regexmarblerun.com/](https://www.regexmarblerun.com/)

生成摘要时出错

---

## 31. Dam removals are bringing fish back across the northeastern United States

**原文标题**: Dam removals are bringing fish back across the northeastern United States

**原文链接**: [https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/](https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/)

生成摘要时出错

---

## 32. Lean now ships with verified kernels

**原文标题**: Lean now ships with verified kernels

**原文链接**: [https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/](https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/)

生成摘要时出错

---

## 33. Tiny Brutalism – Thanks to HN It's on Steam

**原文标题**: Tiny Brutalism – Thanks to HN It's on Steam

**原文链接**: [https://store.steampowered.com/app/5426130/Tiny_Brutalism/](https://store.steampowered.com/app/5426130/Tiny_Brutalism/)

生成摘要时出错

---

## 34. Chirp Pong – uses microphones and audio for networked game play

**原文标题**: Chirp Pong – uses microphones and audio for networked game play

**原文链接**: [https://simonwillison.net/2026/Oct/15/chirp-pong/](https://simonwillison.net/2026/Oct/15/chirp-pong/)

生成摘要时出错

---

## 35. A History of Curves and Surfaces in Computer Aided Geometric Design [pdf]

**原文标题**: A History of Curves and Surfaces in Computer Aided Geometric Design [pdf]

**原文链接**: [https://math.pku.edu.cn/teachers/jiangm/courses/CG/Lectures/spline-history.pdf](https://math.pku.edu.cn/teachers/jiangm/courses/CG/Lectures/spline-history.pdf)

生成摘要时出错

---

## 36. Furifont, a Japanese font that shows furigana

**原文标题**: Furifont, a Japanese font that shows furigana

**原文链接**: [https://furifont.antfu.me/](https://furifont.antfu.me/)

生成摘要时出错

---

## 37. Hyper Optimizing Kimi K3 in vLLM

**原文标题**: Hyper Optimizing Kimi K3 in vLLM

**原文链接**: [https://vllm.ai/blog/2026-10-16-kimi-k3-megakernel](https://vllm.ai/blog/2026-10-16-kimi-k3-megakernel)

生成摘要时出错

---

## 38. How Far Will AI Assistants Go for a Refund They Can't Get?

**原文标题**: How Far Will AI Assistants Go for a Refund They Can't Get?

**原文链接**: [https://www.vals.ai/blogs/impossible-refund](https://www.vals.ai/blogs/impossible-refund)

生成摘要时出错

---

## 39. You could have invented transformers from memory

**原文标题**: You could have invented transformers from memory

**原文链接**: [https://alexwang.ai/posts/associative-memory/](https://alexwang.ai/posts/associative-memory/)

生成摘要时出错

---

## 40. Bleached corals thrive within days when touching healthy neighbour

**原文标题**: Bleached corals thrive within days when touching healthy neighbour

**原文链接**: [https://www.nature.com/articles/d41586-026-03266-x](https://www.nature.com/articles/d41586-026-03266-x)

生成摘要时出错

---

## 41. The Commodore 64 hardware simulator: break chips and pins, see the results

**原文标题**: The Commodore 64 hardware simulator: break chips and pins, see the results

**原文链接**: [https://github.com/antirez/c64-hw-simulator](https://github.com/antirez/c64-hw-simulator)

生成摘要时出错

---

## 42. The Public Pays to Produce Research. Shareholders Collect the Return

**原文标题**: The Public Pays to Produce Research. Shareholders Collect the Return

**原文链接**: [https://sparcopen.org/news/2026/sparc-releases-cost-of-knowledge-accounting-analysis-profitability-report/](https://sparcopen.org/news/2026/sparc-releases-cost-of-knowledge-accounting-analysis-profitability-report/)

生成摘要时出错

---

## 43. OpenCode has a security breach last that impacted 1.4% of console users

**原文标题**: OpenCode has a security breach last that impacted 1.4% of console users

**原文链接**: [https://twitter.com/opencode/status/2111519637049319818](https://twitter.com/opencode/status/2111519637049319818)

生成摘要时出错

---

## 44. Southern ground hornbill gets 3D printed beak prostheses at Artis Zoo

**原文标题**: Southern ground hornbill gets 3D printed beak prostheses at Artis Zoo

**原文链接**: [https://nltimes.nl/2026/10/15/world-first-southern-ground-hornbill-gets-3d-printed-beak-prostheses-artis-zoo](https://nltimes.nl/2026/10/15/world-first-southern-ground-hornbill-gets-3d-printed-beak-prostheses-artis-zoo)

生成摘要时出错

---

## 45. Lorenz and Little: How Much Does Your Tail Cost?

**原文标题**: Lorenz and Little: How Much Does Your Tail Cost?

**原文链接**: [https://brooker.co.za/blog/2026/07/29/lorenz-and-little.html](https://brooker.co.za/blog/2026/07/29/lorenz-and-little.html)

生成摘要时出错

---

## 46. How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill

**原文标题**: How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill

**原文链接**: [https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly](https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly)

生成摘要时出错

---

## 47. Websites are closing their doors to AI agents

**原文标题**: Websites are closing their doors to AI agents

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web](https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web)

生成摘要时出错

---

## 48. Interactive Linear Programming in the Browser

**原文标题**: Interactive Linear Programming in the Browser

**原文链接**: [https://lpviz.net/](https://lpviz.net/)

生成摘要时出错

---

## 49. Fun Extending the C Preprocessor

**原文标题**: Fun Extending the C Preprocessor

**原文链接**: [https://www.davidpriver.com/Fun-Extending-the-C-Preprocessor.html](https://www.davidpriver.com/Fun-Extending-the-C-Preprocessor.html)

生成摘要时出错

---

## 50. Artie (YC S23) Is Hiring Enterprise AES and Senior Engineers

**原文标题**: Artie (YC S23) Is Hiring Enterprise AES and Senior Engineers

**原文链接**: [https://www.artie.com/careers](https://www.artie.com/careers)

生成摘要时出错

---

## 51. Anthropic's proposed AI safety bill only kicks in if 50 deaths or $1B in damages

**原文标题**: Anthropic's proposed AI safety bill only kicks in if 50 deaths or $1B in damages

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model)

生成摘要时出错

---

## 52. Codex Desktop continuously generates Crashpad pending dumps

**原文标题**: Codex Desktop continuously generates Crashpad pending dumps

**原文链接**: [https://github.com/openai/codex/issues/25921](https://github.com/openai/codex/issues/25921)

生成摘要时出错

---

## 53. NY announces game ownership bill requiring ownership rather than licensing

**原文标题**: NY announces game ownership bill requiring ownership rather than licensing

**原文链接**: [https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends](https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends)

生成摘要时出错

---

## 54. Gold is now the top U.S. export

**原文标题**: Gold is now the top U.S. export

**原文链接**: [https://www.numismaticnews.net/gold-now-top-u-s-export](https://www.numismaticnews.net/gold-now-top-u-s-export)

生成摘要时出错

---

## 55. Show HN: High-quality duck audio synthesizer

**原文标题**: Show HN: High-quality duck audio synthesizer

**原文链接**: [https://celphase.github.io/duck-pond/](https://celphase.github.io/duck-pond/)

生成摘要时出错

---

## 56. DeepSeek-v4.1-Flash-1017

**原文标题**: DeepSeek-v4.1-Flash-1017

**原文链接**: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

生成摘要时出错

---

## 57. Pele – Mermaid diagrams as themeable SVG

**原文标题**: Pele – Mermaid diagrams as themeable SVG

**原文链接**: [https://pele.run/](https://pele.run/)

生成摘要时出错

---

## 58. Show HN: Esp32sim – Run ESP32 firmware in the browser

**原文标题**: Show HN: Esp32sim – Run ESP32 firmware in the browser

**原文链接**: [https://github.com/mikroverk/esp32sim](https://github.com/mikroverk/esp32sim)

生成摘要时出错

---

## 59. Notes on the Complex Roots of Unity

**原文标题**: Notes on the Complex Roots of Unity

**原文链接**: [https://eli.thegreenplace.net/2026/notes-on-the-complex-roots-of-unity/](https://eli.thegreenplace.net/2026/notes-on-the-complex-roots-of-unity/)

生成摘要时出错

---

## 60. High performance policy routed IPsec mesh SD-WAN

**原文标题**: High performance policy routed IPsec mesh SD-WAN

**原文链接**: [https://ranet3.com/](https://ranet3.com/)

生成摘要时出错

---

## 61. Solar surpasses nuclear power globally for first time

**原文标题**: Solar surpasses nuclear power globally for first time

**原文链接**: [https://www.pv-magazine.com/2026/09/29/solar-surpasses-nuclear-power-globally-for-first-time/](https://www.pv-magazine.com/2026/09/29/solar-surpasses-nuclear-power-globally-for-first-time/)

生成摘要时出错

---

## 62. Custom server to revive neato bots

**原文标题**: Custom server to revive neato bots

**原文链接**: [https://github.com/vacuula/vacuula](https://github.com/vacuula/vacuula)

生成摘要时出错

---

## 63. Superoptimizing an FPU Emulator

**原文标题**: Superoptimizing an FPU Emulator

**原文链接**: [https://purplesyringa.moe/blog/superoptimizing-an-fpu-emulator/](https://purplesyringa.moe/blog/superoptimizing-an-fpu-emulator/)

生成摘要时出错

---

## 64. Tesla Roadster

**原文标题**: Tesla Roadster

**原文链接**: [https://www.tesla.com/roadster](https://www.tesla.com/roadster)

生成摘要时出错

---

## 65. 'I'm on a War Footing': Terry Tao and the Crisis in Math

**原文标题**: 'I'm on a War Footing': Terry Tao and the Crisis in Math

**原文链接**: [https://www.nytimes.com/2026/10/16/us/math-ai-terence-tao.html](https://www.nytimes.com/2026/10/16/us/math-ai-terence-tao.html)

生成摘要时出错

---

## 66. A skeptic's first contact with Kubernetes (2024)

**原文标题**: A skeptic's first contact with Kubernetes (2024)

**原文链接**: [https://blog.davidv.dev/posts/first-contact-with-k8s/](https://blog.davidv.dev/posts/first-contact-with-k8s/)

生成摘要时出错

---

## 67. Making chicken transparent using Dorito dust

**原文标题**: Making chicken transparent using Dorito dust

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using)

生成摘要时出错

---

## 68. Rendering pretty sky in Around The World game

**原文标题**: Rendering pretty sky in Around The World game

**原文链接**: [https://frozenfractal.com/blog/2026/10/12/around-the-world-34-a-pretty-sky/](https://frozenfractal.com/blog/2026/10/12/around-the-world-34-a-pretty-sky/)

生成摘要时出错

---

## 69. Show HN: Parin – A 2D game engine between raylib and Godot, written in Dlang

**原文标题**: Show HN: Parin – A 2D game engine between raylib and Godot, written in Dlang

**原文链接**: [https://github.com/Kapendev/parin](https://github.com/Kapendev/parin)

生成摘要时出错

---

## 70. Vintage Cassettes: 1963-2010

**原文标题**: Vintage Cassettes: 1963-2010

**原文链接**: [http://vintagecassettes.com/](http://vintagecassettes.com/)

生成摘要时出错

---

## 71. Claude reveals ECDSA curve origins

**原文标题**: Claude reveals ECDSA curve origins

**原文链接**: [https://www.anthropic.com/research/ecdsa-curve-origins](https://www.anthropic.com/research/ecdsa-curve-origins)

生成摘要时出错

---

## 72. Laser Fault Injection on a Budget: RP2350 Edition (2025)

**原文标题**: Laser Fault Injection on a Budget: RP2350 Edition (2025)

**原文链接**: [https://courk.cc/rp2350-challenge-laser](https://courk.cc/rp2350-challenge-laser)

生成摘要时出错

---

## 73. August in Servo: CSS Grid, text selection, and more

**原文标题**: August in Servo: CSS Grid, text selection, and more

**原文链接**: [https://servo.org/blog/2026/10/09/august-in-servo/](https://servo.org/blog/2026/10/09/august-in-servo/)

生成摘要时出错

---

## 74. World Bank says 'small AI' could transform developing countries

**原文标题**: World Bank says 'small AI' could transform developing countries

**原文链接**: [https://www.theguardian.com/technology/2026/oct/18/world-bank-artificial-intelligence-developing-economies](https://www.theguardian.com/technology/2026/oct/18/world-bank-artificial-intelligence-developing-economies)

生成摘要时出错

---

## 75. Show HN: CallSitter – bot that answers my calls and wastes scammers' time

**原文标题**: Show HN: CallSitter – bot that answers my calls and wastes scammers' time

**原文链接**: [https://github.com/szerintedmi/callsitter](https://github.com/szerintedmi/callsitter)

生成摘要时出错

---

## 76. The future of programming (1982)

**原文标题**: The future of programming (1982)

**原文链接**: [https://dl.acm.org/doi/10.1145/358453.358459](https://dl.acm.org/doi/10.1145/358453.358459)

生成摘要时出错

---

## 77. A story of WiFi secrets, UART lockdowns and a damaged flash memory chip

**原文标题**: A story of WiFi secrets, UART lockdowns and a damaged flash memory chip

**原文链接**: [https://adepts.of0x.cc/eufy-homestation2-firmware/](https://adepts.of0x.cc/eufy-homestation2-firmware/)

生成摘要时出错

---

## 78. Show HN: A forest's wildlife, synthesized live in Rust, playable in the browser

**原文标题**: Show HN: A forest's wildlife, synthesized live in Rust, playable in the browser

**原文链接**: [https://zaghaghi.github.io/spore-and-skog-dev-log/](https://zaghaghi.github.io/spore-and-skog-dev-log/)

生成摘要时出错

---

## 79. A Mole Infiltrated the Highest Ranks of American Militias (2025)

**原文标题**: A Mole Infiltrated the Highest Ranks of American Militias (2025)

**原文链接**: [https://www.propublica.org/article/ap3-oath-keepers-militia-mole](https://www.propublica.org/article/ap3-oath-keepers-militia-mole)

生成摘要时出错

---

## 80. Matthew Prince on why Cloudflare offers a free version and always will (2016)

**原文标题**: Matthew Prince on why Cloudflare offers a free version and always will (2016)

**原文链接**: [https://webmasters.stackexchange.com/questions/88659/how-can-cloudflare-offer-a-free-cdn-with-unlimited-bandwidth/88685#88685](https://webmasters.stackexchange.com/questions/88659/how-can-cloudflare-offer-a-free-cdn-with-unlimited-bandwidth/88685#88685)

生成摘要时出错

---

## 81. One Parser, Two Bugs, Many Routers: Exploiting Broadcom WiFi Across ECos, Linux

**原文标题**: One Parser, Two Bugs, Many Routers: Exploiting Broadcom WiFi Across ECos, Linux

**原文链接**: [https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/](https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/)

生成摘要时出错

---

## 82. Show HN: Things to Do API

**原文标题**: Show HN: Things to Do API

**原文链接**: [https://thingstodoapi.com/](https://thingstodoapi.com/)

生成摘要时出错

---

## 83. Python's binary wheels and supply chain attacks

**原文标题**: Python's binary wheels and supply chain attacks

**原文链接**: [https://rushter.com/blog/python-binary-wheels/](https://rushter.com/blog/python-binary-wheels/)

生成摘要时出错

---

## 84. MapQuest will now show you where Flock cameras are in your neighborhood

**原文标题**: MapQuest will now show you where Flock cameras are in your neighborhood

**原文链接**: [https://www.engadget.com/2288729/mapquest-will-now-show-you-where-flock-cameras-are-in-your-neighborhood/](https://www.engadget.com/2288729/mapquest-will-now-show-you-where-flock-cameras-are-in-your-neighborhood/)

生成摘要时出错

---

## 85. 0/1 Knapsack Problem in PyTorch

**原文标题**: 0/1 Knapsack Problem in PyTorch

**原文链接**: [https://jedrzej.maczan.pl/2025_11_21_dp_knapsack_sliding_hirschberg](https://jedrzej.maczan.pl/2025_11_21_dp_knapsack_sliding_hirschberg)

生成摘要时出错

---

## 86. Ultramarine 1 Flash

**原文标题**: Ultramarine 1 Flash

**原文链接**: [https://www.paperinstruments.com/ultramarine](https://www.paperinstruments.com/ultramarine)

生成摘要时出错

---

## 87. OpenCode Hacked: User credentials leaked

**原文标题**: OpenCode Hacked: User credentials leaked

**原文链接**: [https://twitter.com/opencode/status/2111516673953935833](https://twitter.com/opencode/status/2111516673953935833)

生成摘要时出错

---

## 88. Propagation of Sound in Strongly Viscous Liquids (1966) [pdf]

**原文标题**: Propagation of Sound in Strongly Viscous Liquids (1966) [pdf]

**原文链接**: [https://jetp.ras.ru/cgi-bin/dn/e_023_05_0893.pdf](https://jetp.ras.ru/cgi-bin/dn/e_023_05_0893.pdf)

生成摘要时出错

---

## 89. Each step of decoding a PNG (2022)

**原文标题**: Each step of decoding a PNG (2022)

**原文链接**: [https://iter.ca/post/png/](https://iter.ca/post/png/)

生成摘要时出错

---

## 90. Each step of decoding a PNG (2022)

**原文标题**: Each step of decoding a PNG (2022)

**原文链接**: [https://iter.ca/post/png/](https://iter.ca/post/png/)

生成摘要时出错

---

## 91. The math that OpenAI keeps for itself

**原文标题**: The math that OpenAI keeps for itself

**原文链接**: [https://newsletter.danielpaleka.com/p/the-math-that-openai-keeps-for-itself](https://newsletter.danielpaleka.com/p/the-math-that-openai-keeps-for-itself)

生成摘要时出错

---

## 92. Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware

**原文标题**: Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware

**原文链接**: [https://llmspeed.dev/](https://llmspeed.dev/)

生成摘要时出错

---

## 93. I love software rendering

**原文标题**: I love software rendering

**原文链接**: [https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/](https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/)

生成摘要时出错

---

## 94. Designing more efficient quantum circuits with Claude

**原文标题**: Designing more efficient quantum circuits with Claude

**原文链接**: [https://www.anthropic.com/research/designing-efficient-quantum-circuits](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

生成摘要时出错

---

## 95. A Tudor life in the time of plague (2020)

**原文标题**: A Tudor life in the time of plague (2020)

**原文链接**: [https://www.historytoday.com/archive/history-matters/tudor-life-time-plague](https://www.historytoday.com/archive/history-matters/tudor-life-time-plague)

生成摘要时出错

---

## 96. Development statistics for the 7.2 kernel

**原文标题**: Development statistics for the 7.2 kernel

**原文链接**: [https://lwn.net/Articles/1088776/](https://lwn.net/Articles/1088776/)

生成摘要时出错

---

## 97. Study shows cannabis is not associated with better sleep quality

**原文标题**: Study shows cannabis is not associated with better sleep quality

**原文链接**: [https://news.northwestern.edu/stories/2026/10/think-cannabis-helps-you-sleep-better-think-again](https://news.northwestern.edu/stories/2026/10/think-cannabis-helps-you-sleep-better-think-again)

生成摘要时出错

---

## 98. Source code of the Estonian online voting system

**原文标题**: Source code of the Estonian online voting system

**原文链接**: [https://github.com/valimised/ivxv](https://github.com/valimised/ivxv)

生成摘要时出错

---

## 99. JDK 28

**原文标题**: JDK 28

**原文链接**: [https://openjdk.org/projects/jdk/28/](https://openjdk.org/projects/jdk/28/)

生成摘要时出错

---

## 100. 90% of US working hours are spent on tasks not covered well by AI benchmarks

**原文标题**: 90% of US working hours are spent on tasks not covered well by AI benchmarks

**原文链接**: [https://www.mercor.com/research/labor-index/benchmark-map/](https://www.mercor.com/research/labor-index/benchmark-map/)

生成摘要时出错

---

