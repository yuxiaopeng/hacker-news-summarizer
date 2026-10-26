# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-26.md)

*最后自动更新时间: 2026-10-26 21:53:05*
## 1. 类型服务器协议

**原文标题**: Type Server Protocol

**原文链接**: [https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)

类型服务器协议 (Type Server Protocol, TSP) 是一种 JSON-RPC 协议，旨在向客户端提供 Python 分析数据，包括类型查询、导入解析和搜索路径。它沿用了语言服务器协议 (LSP) 的数据格式，特别是针对位置和范围使用从零开始的 UTF-16 偏移量。

该协议的主要特性包括：

*   **快照 (Snapshots)：** 分析状态通过快照进行管理。快照是随工作区或文档状态变化而递增的非负整数。为确保数据一致性，请求必须包含快照 ID。如果快照已过期，服务器将返回 `ServerCancelled` 错误 (-32802)，提示客户端使用最新的快照重试。
*   **连接模型 (Connection Model)：** TSP 通常通过处理初始化和状态变更同步的主连接（stdio 或 IPC）运行。它还支持可选的**多连接模式 (Multi-Connection Mode)**，客户端可以协商额外的只读 IPC 通道，以便在不阻塞主连接的情况下并发处理大量类型查询。
*   **类型查询 (Type Queries)：** 该协议区分了三种特定的类型查询：
    *   **计算类型 (Computed)：** 从代码流中推断出的类型。
    *   **声明类型 (Declared)：** 在源代码中显式定义的类型。
    *   **预期类型 (Expected)：** 周边上下文所要求的类型。
*   **数据表示 (Data Representation)：** 类型结果以标记的 JSON 对象形式返回（例如 Class、Function、Union）。这些对象在单次响应中使用 ID 进行去重和引用，但这些 ID 在不同快照之间并不固定。

为了保持兼容性，服务器必须遵循语义化版本控制，执行标准的启动握手，并确保额外连接拒绝处理变更状态的 LSP 流量。该协议的规范以其 TypeScript 定义和 JSON 架构为准。

---

## 2. Sebastian Raschka 的从零开始构建推理模型视频课程

**原文标题**: Sebastian Raschka's from-scratch video course on building reasoning models

**原文链接**: [https://magazine.sebastianraschka.com/p/building-reasoning-models](https://magazine.sebastianraschka.com/p/building-reasoning-models)

Sebastian Raschka 发布了一套长达 11 小时的全方位视频课程，题为 **《从零开始构建推理模型》**。作为其此前大语言模型（LLM）相关工作的续作，这门基于 PyTorch 的课程将引导学习者深入探索现代人工智能推理能力的技术实现。

该课程将推理模型定义为一种升级版 LLM “引擎”，利用强化学习（RL）和推理时扩展（Inference-time scaling）来解决复杂的数学和逻辑问题。该系列视频共分为八个部分，以预训练的 Qwen3 模型为基础，内容涵盖：

*   **模型基础：** 加载权重、实现 KV 缓存以及优化文本生成。
*   **评估：** 构建自动化数学答案验证器以提供奖励信号。
*   **推理时扩展：** 实现自我一致性（Self-consistency）、多项式采样、Top-p 过滤和自我修正循环等技术。
*   **强化学习：** 深入探讨带可验证奖励的强化学习（RLVR）和群体相对策略优化（GRPO）。
*   **蒸馏：** 训练小型模型以模拟 DeepSeek R1 等大型“教师”模型的推理轨迹。

Raschka 强调采用“从零开始”的编码方式，旨在帮助学生理解 AI 智能体的底层机制。虽然该课程是独立的，但其设计初衷是与其著作《从零构建推理模型》（*Build a Reasoning Model (From Scratch)*）配套使用。学习该课程需精通 Python 和 PyTorch，并建议在后期的训练模块中使用 GPU。该系列课程为从开发简单聊天机器人转向构建精密、可验证的推理系统提供了一份实用的路线图。

---

## 3. CSS-Tricks has a new owner

**原文标题**: CSS-Tricks has a new owner

**原文链接**: [https://css-tricks.com/css-tricks-has-a-new-owner/](https://css-tricks.com/css-tricks-has-a-new-owner/)

2026年，知名Web开发资源 **CSS-Tricks** 在2022年被 DigitalOcean 收购后，现已重新回归独立运营。新业主是一位在该网站工作了12年的资深员工，他将担任“出版人”一职，致力于将该网站重新打造为一个面向各水平前端开发者的、以社区为中心的包容性平台。

此次转型的核心要点包括：

*   **财务可持续性：** 摆脱企业支持，回归传统广告模式，包括展示广告和赞助文章。此外，网站还推出了**付费会员模式**（包含私人 Discord 社区）和周边商店。
*   **教育内容：** 为应对行业内日益扩大的“技能鸿沟”，出版人正在开发新的教育资源，首个项目是针对初学者的 HTML/CSS 课程，旨在降低入行门槛。
*   **内容策略：** 网站将持续发布新文章，初期频率略微降至每周一到两篇。**客座写作计划**已重新开放以鼓励多元发声，长期停更的**电子邮件通讯**也将正式恢复。
*   **编辑愿景：** 新业主的主要角色将是策展人和编辑而非唯一作者，重点在于帮助其他开发者发声，并为他们提供分享专业知识的平台。

总的来说，这一举措标志着该网站向其“独立网络”（indie web）起源的重大回归，相较于企业所有权，更加优先考虑社区参与和教育普及。

---

## 4. 能在 Windows 11 上运行的最古老 GUI 应用程序

**原文标题**: Oldest GUI application that still runs on Windows 11

**原文链接**: [https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/)

本文探讨了 Windows 11 向下兼容性的极限，旨在找出在无需修改或模拟的情况下，能够原生运行的最古老 GUI 应用程序。

由于 64 位 Windows 11 缺少 NT 虚拟 DOS 机（NTVDM），因此无法运行 Windows 1.0 到 3.x 时代的 16 位应用程序。因此，搜索重点转向了 Windows NT 开发初期的早期 32 位程序。作者指出，许多 1991 年和 1992 年初的预发布版程序由于可执行格式不兼容，或因“cdecl”调用约定冲突导致现代系统崩溃而运行失败。

调查重点突出了两个主要的成功案例：

1.  **FREECELL.EXE（1993 年 2 月 22 日）：** 该程序源自早期的 Win32s 版本，这款已有 33 年历史的应用在现代 Windows 11 上依然可以完美运行。
2.  **CDPLAYER.EXE（1992 年 11 月 16 日）：** 发现于 Windows NT Build 347，是目前已确认的能原生运行的最古老程序。它之所以能正常工作，是因为它链接到了 `crtdll.dll`（Windows 11 的 `SysWOW64` 文件夹中仍保留此库），且遵循了现代 Windows API 所使用的“stdcall”调用约定。虽然它需要一个小型辅助 DLL 来模拟物理光驱，但代码本身无需修改即可运行。

最后，作者展示了虽然像 **REVERSI.EXE**（1985 年 11 月 15 日）这样的 16 位程序可以使用“otvdm”兼容层在 Windows 11 上运行，但由于这依赖于模拟，因此不计入原生运行的成功案例。最终，该实验证明 Windows 11 能够原生支持近 34 年前的软件。

---

## 5. 尼采式调试器

**原文标题**: Nietzschian Debugger

**原文链接**: [https://github.com/DilawarShafiq/nietzschian-debugger](https://github.com/DilawarShafiq/nietzschian-debugger)

**尼采式调试器**（Nietzschian Debugger）是一款基于命令行界面（CLI）的“反AI”工具，旨在通过拒绝提供直接解决方案来锻造更强大的开发者。与提供即时修复的传统AI助手不同，该工具利用哲学挑衅和苏格拉底式提问，迫使用户直面自身逻辑，审查证据并独立揭示问题的根源。

其核心哲学认为，“复制粘贴”式的AI文化正在削弱开发者的能力。通过在调试过程中引入“磨难”，该工具确保开发者能够真正理解自己的代码。它提供三个强度等级：
*   **苏格拉底（Socrates）：** 温和的引导式提问，适用于初级开发者。
*   **尼采（Nietzsche，默认）：** 直接且具有对抗性。
*   **查拉图斯特拉（Zarathustra）：** 充满敌意与挑战性，专为追求极致挑战的高级开发者设计。

**核心功能：**
*   **主动调试：** 它从不提供答案；只负责提问，直到用户自行找到解决方案。
*   **上下文感知：** 能够读取本地文件，针对实际代码库提供具体的反馈。
*   **成长追踪：** 会话结束后生成“调试档案”，针对用户的假设验证、证据收集和解决速度进行评分。
*   **技术栈：** 基于 Python/Node.js 构建，由 Anthropic (Claude) API 驱动（需用户自备 API 密钥）。

尼采式调试器面向那些看重长期精进而非速成方案的开发者、管理者及学生。通过将智力劳动的重担重新交还给人类，它的目标是让开发者——而非AI——在每一次调试中变得更加睿智。

---

## 6. GPT-6.1 泰拉

**原文标题**: GPT-6.1 Terra

**原文链接**: [https://openai.com/index/introducing-gpt-6-1-terra/](https://openai.com/index/introducing-gpt-6-1-terra/)

OpenAI 推出了 **GPT-6.1 Terra**，这是一款快速且极具成本效益的模型，旨在弥合高级推理与实际高频计算机操作之间的差距。作为 GPT-5.6 Terra 的重大升级版本，新模型在自动化职场任务方面表现出色，如撰写提案、解析技术图纸以及操作桌面应用程序。

**核心亮点：**

*   **效率与成本：** 相比 GPT-5.6 Terra 和 GPT-6.1 Sol，Terra 的价格降低了 50%，API 费率为每百万输入 token 1 美元。它的速度和 token 利用率显著优于 Claude Opus 5.5 等竞争对手，且通常能以十分之一的成本达到旗舰级 GPT-6 Astra 的性能。
*   **计算机操作与视觉推理：** 在 *Agents’ Last Exam* 和 *OSWorld 2.1* 等基准测试中，Terra 展示了在桌面应用内执行多步任务的卓越能力。它在视觉推理方面实现了巨大飞跃，几乎可以媲美 OpenAI 最强大的模型。
*   **真实性与编程：** OpenAI 报告称其幻觉现象大幅减少；在低推理强度下，错误率从 53.6% 降至 16.7%。此外，它在 *Terminal-Bench 4.0* 基准测试中的软件工程能力提升了一倍以上。
*   **安全与对齐：** 该模型在网络安全方面达到了“关键（Critical）”阈值，并具备先进的抗提示词注入攻击能力。其设计旨在向用户更透明地呈现其局限性。

**可用性：** 
GPT-6.1 Terra 即日起向 ChatGPT Plus、Pro、企业版（Enterprise）和教育版（Edu）用户开放，并可通过 OpenAI API 获取。

---

## 7. 美国环保局正在悄然关停其网站存档。

**原文标题**: The EPA Is Quietly Killing Its Web Archive

**原文链接**: [https://www.motherjones.com/environment/2026/10/epa-online-archive-deletion-zeldin-camp-lejeune-trump-clean-power/](https://www.motherjones.com/environment/2026/10/epa-online-archive-deletion-zeldin-camp-lejeune-trump-clean-power/)

美国国家环境保护局（EPA）宣布计划在2026年12月31日前关停其在线网页存档，批评人士称此举将抹去数十载至关重要的环境历史。该存档库收录了追溯至20世纪90年代的数万份文件，包括监管行动、政策变动，以及《清洁电力计划》和《晴空倡议》等重大举措。

这并非该机构首次尝试关闭该资源。2022年，拜登政府曾以每年200万美元的维护费用为由提议关闭，但在遭到历史学家、图书管理员和环保人士的强烈反对后推迟了这一行动。尽管环保局表示将保留“快照合集”，但倡导者警告称，这些碎片化的记录无法替代一个可检索、全面的存档库。

来自环境数据与治理倡议（EDGI）和新闻自由基金会的专家强调，该存档库对于“民主监督”和公众信任至关重要。他们指出，该库在追踪环境执法和评估化学品暴露（如北卡罗来纳州勒琼营地长达数十年的污染调查）方面发挥了关键作用。

批评人士认为，取消对这些记录的便捷访问将迫使研究人员和立法者依赖积压严重的《信息自由法》（FOIA）申请流程，从而在历史记录中造成“巨大空白”。这一决定正值政治敏感时刻，因为即将上任的政府及其环保局局长提名人李·泽尔丁已表示有意撤销多项环境法规和联邦计划。

---

## 8. A Man from the Future: Why Johnny Can't Stop Abstracting

**原文标题**: A Man from the Future: Why Johnny Can't Stop Abstracting

**原文链接**: [http://muratbuffalo.blogspot.com/2026/10/the-man-from-future-why-johnny-cant.html](http://muratbuffalo.blogspot.com/2026/10/the-man-from-future-why-johnny-cant.html)

"A Man from the Future" explores the extraordinary life and intellectual "superpower" of John von Neumann, a polymath whose contributions fundamentally shaped modern science and technology. Von Neumann’s primary strength was the **art of abstraction**: the ability to strip complex, "messy" systems down to their minimal logical axioms.

Born into a brilliant cluster of Hungarian-Jewish intellectuals in Budapest, von Neumann was a child prodigy whose early education involved intense dinner-table seminars and elite mathematical tutoring. His career was defined by a recurring pattern: arriving at a field in flux, providing it with a rigorous mathematical foundation, and moving on to the next challenge. 

His key achievements include:
*   **Physics:** Unifying rival theories of quantum mechanics into a single rigorous framework using Hilbert space.
*   **Economics:** Co-founding Game Theory (the Minimax theorem) and axiomatizing expected utility, which remains the foundation of mathematical economics.
*   **Computing:** Designing the "von Neumann architecture" (the stored-program model) used in almost every modern computer. He also pioneered Monte Carlo methods, pseudorandom generation, and numerical weather prediction.
*   **Biology:** Logically deriving the mechanism for self-reproducing automata—separating "instructions" (translation) from "data" (transcription)—years before the physical structure of DNA was discovered.
*   **Engineering:** Developing "fault-tolerant computing" to build reliable systems from unreliable components.

Despite his controversial role in Cold War nuclear strategy, von Neumann’s legacy is defined by his generosity toward the scientific commons, particularly in placing his foundational computer designs in the public domain. He redefined the logical structures of every field he touched, from the inner workings of the atom to the architecture of the human brain.

---

## 9. Anthropic S-1

**原文标题**: Anthropic S-1

**原文链接**: [https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)

生成摘要时出错

---

## 10. SIMD-accelerated computer vision on a $2 microcontroller

**原文标题**: SIMD-accelerated computer vision on a $2 microcontroller

**原文链接**: [https://shraiwi.com/blog/simd-fast-esp32s3/](https://shraiwi.com/blog/simd-fast-esp32s3/)

This article details the optimization of a **FAST feature detector** on the **ESP32-S3**, a $2 microcontroller, by leveraging its 128-bit SIMD (Single Instruction, Multiple Data) instructions. The author achieved a **220% performance increase**, boosting throughput from 5.1MP/s to 11.2MP/s. This allows the chip to process a QVGA frame in roughly 6ms and enables real-time 30fps VGA computer vision tasks.

The author highlights two primary technical challenges and their creative solutions:

1.  **Misaligned Memory Access:** The ESP32-S3 ISA does not support direct misaligned reads. To sample the "east" and "west" pixel blocks required for the FAST algorithm, the author used specialized instructions to extract slices from two concatenated 128-bit registers.
2.  **Signed vs. Unsigned Comparisons:** The chip’s SIMD instructions only support **signed 8-bit comparisons**, while pixel data is unsigned. Standard subtraction to re-range the data was impossible because the chip’s arithmetic is **saturating** (clamping values rather than allowing underflow). The author circumvented this by **XORing the pixel data with 0x80**. This bit-flip effectively shifts the unsigned range [0, 255] to a linear signed range [-128, 127], allowing for accurate comparisons.

The project involved writing assembly code and developing a custom register allocator called **basm**. While the ESP32-S3's SIMD capabilities are documented, the author notes they are relatively underutilized. This implementation proves that the ESP32-S3 is a cost-effective powerhouse for edge computer vision, provided one can navigate its architectural eccentricities.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 2 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 3 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 4 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 5 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 6 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 7 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 8 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 9 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 10 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 11 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 12 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 13 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 14 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 15 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 16 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 17 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 18 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 19 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 20 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 21 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 22 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 23 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 24 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 25 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 26 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 27 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 28 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 29 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 30 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 31 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 32 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 33 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 34 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 35 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 36 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 37 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 38 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 39 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 40 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 41 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 42 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 43 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 44 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 45 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 46 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 47 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 48 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 49 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 50 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 51 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 52 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 53 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 54 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 55 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 56 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 57 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 58 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 59 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 60 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 61 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 62 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 63 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 64 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 65 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 66 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 67 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 68 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 69 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 70 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 71 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 72 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 73 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 74 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 75 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 76 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 77 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 78 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 79 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 80 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 81 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 82 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 83 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 84 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 85 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 86 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 87 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 88 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 89 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 90 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 91 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 92 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 93 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 94 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 95 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 96 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 97 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 98 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 99 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 100 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 101 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 102 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 103 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 104 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 105 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 106 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 107 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 108 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 109 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 110 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 111 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 112 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 113 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 114 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 115 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 116 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 117 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 118 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 119 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 120 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 121 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 122 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 123 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 124 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 125 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 126 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 127 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 128 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 129 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 130 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 131 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 132 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 133 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 134 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 135 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 136 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 137 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 138 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 139 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 140 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 141 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 142 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 143 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 144 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 145 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 146 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 147 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 148 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 149 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 150 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 151 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 152 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 153 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 154 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 155 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 156 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 157 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 158 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 159 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 160 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 161 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 162 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 163 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 164 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 165 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 166 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 167 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 168 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 169 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 170 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 171 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 172 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 173 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 174 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 175 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 176 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 177 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 178 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 179 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 180 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 181 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 182 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 183 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 184 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 185 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 186 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 187 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 188 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 189 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 190 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 191 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 192 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 193 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 194 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 195 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 196 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 197 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 198 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 199 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 200 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 201 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 202 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 203 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 204 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 205 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 206 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 207 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 208 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 209 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 210 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 211 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 212 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 213 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 214 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 215 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 216 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 217 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 218 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 219 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 220 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 221 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 222 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 223 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 224 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 225 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 226 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 227 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 228 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 229 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 230 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 231 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 232 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 233 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 234 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 235 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 236 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 237 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 238 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 239 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 240 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 241 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 242 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 243 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 244 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 245 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 246 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 247 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 248 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 249 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 250 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 251 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 252 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 253 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 254 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 255 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 256 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 257 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 258 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 259 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 260 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 261 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 262 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 263 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 264 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 265 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 266 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 267 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 268 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 269 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 270 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 271 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 272 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 273 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 274 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 275 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 276 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 277 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 278 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 279 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 280 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 281 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 282 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 283 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 284 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 285 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 286 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 287 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 288 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 289 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 290 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 291 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 292 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 293 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 294 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 295 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 296 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 297 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 298 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 299 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 300 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 301 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 302 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 303 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 304 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 305 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 306 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 307 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 308 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 309 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 310 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 311 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 312 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 313 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 314 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 315 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 316 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 317 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 318 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 319 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 320 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 321 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 322 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 323 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 324 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 325 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 326 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 327 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 328 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 329 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 330 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 331 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 332 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 333 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 334 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 335 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 336 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 337 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 338 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 339 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 340 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 341 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 342 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 343 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 344 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 345 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 346 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 347 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 348 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 349 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 350 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 351 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 352 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 353 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 354 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 355 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 356 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 357 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 358 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 359 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 360 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 361 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 362 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 363 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 364 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 365 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 366 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 367 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 368 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 369 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 370 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 371 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 372 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 373 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 374 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 375 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 376 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 377 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 378 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 379 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 380 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 381 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 382 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 383 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 384 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 385 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 386 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 387 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 388 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 389 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 390 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 391 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 392 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 393 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 394 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 395 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 396 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 397 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 398 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 399 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 400 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 401 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 402 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 403 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 404 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 405 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 406 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 407 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 408 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 409 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 410 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 411 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 412 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 413 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 414 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 415 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 416 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 417 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 418 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 419 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 420 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 421 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 422 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 423 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 424 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 425 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 426 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 427 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 428 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 429 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 430 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 431 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 432 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 433 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 434 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 435 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 436 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 437 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 438 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 439 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 440 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 441 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 442 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 443 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 444 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 445 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 446 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 447 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 448 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 449 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 450 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 451 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 452 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 453 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 454 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 455 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 456 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 457 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 458 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 459 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 460 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 461 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 462 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 463 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 464 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 465 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 466 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 467 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 468 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 469 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 470 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 471 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 472 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 473 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 474 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 475 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 476 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 477 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 478 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 479 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 480 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 481 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 482 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 483 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 484 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 485 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 486 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 487 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 488 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 489 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 490 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 491 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 492 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 493 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 494 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 495 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 496 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 497 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 498 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 499 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 500 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 501 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 502 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 503 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 504 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 505 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 506 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 507 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 508 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 509 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 510 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 511 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 512 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 513 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 514 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 515 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 516 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 517 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 518 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 519 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 520 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 521 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 522 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 523 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 524 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 525 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 526 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 527 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 528 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 529 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 530 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 531 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 532 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 533 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 534 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 535 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 536 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 537 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 538 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 539 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 540 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 541 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 542 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 543 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 544 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 545 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 546 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 547 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 548 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 549 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 550 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 551 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 552 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 553 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 554 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 555 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 556 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 557 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 558 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 559 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 560 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 561 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 562 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 563 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 564 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 565 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 566 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 567 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 568 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 569 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 570 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 571 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 572 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 573 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 574 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 575 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 576 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 577 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 578 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 579 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 580 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 581 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 582 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 583 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
