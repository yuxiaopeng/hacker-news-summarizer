# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-23.md)

*最后自动更新时间: 2025-12-23 17:49:24*
## 1. 测试，而非（仅仅）验证

**原文标题**: Test, don't (just) verify

**原文链接**: [https://alperenkeles.com/posts/test-dont-verify/](https://alperenkeles.com/posts/test-dont-verify/)

文章《测试，而非（仅仅）验证》探讨了人工智能推动下形式化验证的复兴，同时指出测试仍然是一门必不可少且互补的学科。

**AI在验证领域的崛起**
AI和大语言模型（LLM）通过解决两个传统障碍正在改变形式化验证（使用Lean等工具）：形式化规范的缺失以及证明工程的高难度。LLM促进了“自动形式化”——将口头描述转化为数学定理——并实现了“可验证奖励的强化学习”（RLVR），模型可以通过不断迭代直到符号检查器确认证明。

**形式化验证的局限性**
尽管前景广阔，作者仍指出了几个关键缺陷：
*   **TCB问题：** 自动形式化是可信计算基（TCB）的一部分。如果AI错误地将口头意图转化为形式化规范，由此产生的证明将毫无意义。
*   **性能：** 证明助手计算速度较慢，因为它们使用归纳结构（如皮亚诺数）而非硬件优化的类型。为了追求速度而进行的优化通常需要扩大TCB，这会损害验证旨在提供的“绝对”信任。
*   **建模差距：** 某些领域（如缓存行、分支预测等现实硬件性能）几乎无法精确建模。在真实硬件上进行测试仍然是建立性能“基准事实”的唯一方法。
*   **证伪：** 验证可能在无法证明定理确实为假的情况下找不到证明。而测试能快速提供反例，防止工程师在无法证明的猜想上浪费时间。

**综合方案：验证引导的开发（VGD）**
作者倡导将“验证引导的开发”（VGD）作为一种折中方案。在这一工作流中，开发人员创建一个简单的、经过验证的参考实现，以及一个复杂的、高性能的生产版本。通过使用“差分随机测试”确保生产系统与验证模型相匹配，工程师可以开发出既具有数学严谨性又具有高效执行性能的软件。

最后，作者总结道，测试并不是验证的劣等替代方案，而是证伪和真实世界测量的必要工具。

---

## 2. Adobe Photoshop 1.0 源代码 (1990)

**原文标题**: Adobe Photoshop 1.0 Source Code (1990)

**原文链接**: [https://computerhistory.org/blog/adobe-photoshop-source-code/](https://computerhistory.org/blog/adobe-photoshop-source-code/)

在这篇2013年为计算机历史博物馆撰写的文章中，Leonard J. Shustek纪念了Adobe Photoshop 1.0原始源代码的发布。该软件最初于1990年2月首次问世。

文章详细介绍了该软件的起源——它最初是Thomas Knoll和John Knoll兄弟的一个个人项目。当时还是博士生的Thomas Knoll编写了核心图像处理代码（最初名为“Display”），而任职于工业光魔（Industrial Light & Magic）的John Knoll则预见到了其作为商业设计工具的潜力。在与扫描仪制造商 Barneyscan 达成短期授权协议后，该软件授权给了Adobe公司，并在Apple Macintosh平台上发布，取得了巨大的成功。

**关键技术细节：**
*   **组成：** 源代码包含约128,000行代码。
*   **语言：** 约75%使用Pascal语言编写，约15%为了处理关键性能任务而使用了Motorola 68000汇编语言，其余部分则分布在各种支持文件中。
*   **可用性：** 经Adobe公司许可，博物馆已将代码公开，供非商业性教育用途使用。

该总结强调了Photoshop的历史意义，指出了它是如何从一个两人项目转变为彻底改变数字摄影和视觉媒体的行业标准巨头的。源代码的发布是对Knoll兄弟在个人计算早期时代所展现出的精妙工程设计与卓越才华的致敬。

---

## 3. 瑞安航空因限制在线旅行社售票的“滥用策略”被处以 2.56 亿欧元罚款。

**原文标题**: Ryanair fined €256M over ‘abusive strategy’ to limit ticket sales by OTAs

**原文链接**: [https://www.theguardian.com/business/2025/dec/23/ryanair-fined-limit-online-travel-agencies-ticket-sales-ota](https://www.theguardian.com/business/2025/dec/23/ryanair-fined-limit-online-travel-agencies-ticket-sales-ota)

意大利竞争管理局对瑞安航空处以2.56亿欧元（约合2.23亿英镑）的罚款，理由是该公司滥用市场支配地位，打压在线旅行社（OTA）的机票销售。监管机构调查发现，该航空公司采用了一套包含技术和管理障碍的“精心设计的策略”，以阻碍第三方预订，并迫使乘客使用瑞安航空官网。

根据该机构的说法，瑞安航空在2023年4月至2025年4月期间实施的手段包括拦截支付方式、注销代理商账户，以及对通过第三方订票的乘客强制要求进行人脸识别。这些行为阻止了OTA将瑞安航空的航班与其他承运商或旅游服务组合销售，监管机构认为这削弱了市场竞争，并加重了消费者的负担。

瑞安航空首席执行官迈克尔·奥利里（Michael O’Leary）誓言要对这一“法律上有缺陷”的裁决提出上诉。他为公司的策略辩护，称在线旅行社是“海盗”，通过未经授权的加价和额外费用“坑害”客户。奥利里坚称，通过官网直销能让航空公司以更低票价的形式，将20%的成本节省回馈给消费者。

尽管存在法律纠纷，且在2023年底航班从某些代理网站撤下时销售额曾出现暂时下滑，但瑞安航空的财务状况依然稳健。该公司最近达到了创纪录的310亿欧元估值，巩固了其作为全球市值第二大航空公司（仅次于达美航空）的地位。

---

## 4. PostgreSQL 18 即时数据库克隆

**原文标题**: Instant database clones with PostgreSQL 18

**原文链接**: [https://boringsql.com/posts/instant-database-clones/](https://boringsql.com/posts/instant-database-clones/)

PostgreSQL 18 在数据库管理方面引入了一项重大突破：通过全新的 `file_copy_method = clone` 配置实现即时、零拷贝克隆。传统上，克隆大型数据库是一项耗时且耗费资源的任务，而此次更新利用现代文件系统的特性，使该过程几乎可以瞬间完成。

从演进历程来看，PostgreSQL 在第 15 版本中从 I/O 密集型文件复制（曾导致“检查点风暴”）转向了更平滑但速度较慢的 `WAL_LOG` 策略。而版本 18 弥补了这一性能差距。通过在受支持的文件系统（如 XFS、ZFS 或 APFS）上利用“reflinks”技术，`clone` 模式会创建指向原始物理块的新元数据条目，而不是直接复制数据。一项针对 6GB 数据库的基准测试充分展示了其威力：标准的 `WAL_LOG` 策略耗时 67 秒，而采用克隆技术的新策略仅需 **212 毫秒**。

该技术依赖于**写时复制 (CoW)** 机制。在执行写操作之前，源数据库和克隆副本共享物理存储；只有当数据页被修改时，才会将变更后的内容写入新数据块。这使得用户可以在不占用大量磁盘空间的情况下，实现可重复的快照并快速构建全新的测试环境。

然而，该功能有三个主要限制：
1. **排他性：** 在克隆过程中，源数据库不能有任何活动连接。
2. **文件系统范围：** 该操作仅在单个文件系统内有效；如果数据库跨越不同挂载点上的多个表空间，则会退回到标准的物理复制模式。
3. **云环境约束：** AWS RDS 或 Google Cloud SQL 等托管服务通常不提供启用此功能所需的文件系统级访问权限。

对于管理自建虚拟机或裸金属服务器的用户而言，这一特性将数据库克隆从一项沉重的运维负担转变为了一项轻而易举、近乎瞬时的操作。

---

## 5. Executorch：面向移动端、嵌入式和边缘设备的 PyTorch 端侧 AI

**原文标题**: Executorch: On-device AI across mobile, embedded and edge for PyTorch

**原文链接**: [https://github.com/pytorch/executorch](https://github.com/pytorch/executorch)

**ExecuTorch** 是 PyTorch 的统一解决方案，用于在设备端部署 AI 模型，覆盖从高端智能手机到资源受限的微控制器等各种设备。它旨在实现从研究到生产的无缝衔接，允许开发者使用熟悉的 PyTorch API，而无需进行手动的 C++ 重写或中间格式转换（如 ONNX 或 TFLite）。

**核心能力与性能：**
*   **经过生产验证：** 目前已为 Meta 生态系统（包括 Instagram、WhatsApp、Quest 3 和 Ray-Ban Meta 智能眼镜）中的数十亿用户提供设备端 AI 支持。
*   **高效：** 运行时基础占用极小，仅为 50KB，非常适合嵌入式系统。
*   **广泛的硬件支持：** 支持超过 12 种后端，包括 Apple (CoreML/MPS)、Qualcomm (QNN)、ARM、MediaTek 和 Vulkan，仅需更改一行代码即可实现硬件加速推理。

**工作原理：**
ExecuTorch 采用提前 (AOT) 编译工作流：
1.  **导出：** 使用 `torch.export()` 捕获模型图。
2.  **编译：** 将模型量化并优化为专为特定硬件定制的 `.pte` 二进制文件。
3.  **执行：** 在目标设备上使用轻量级 C++ 运行时加载并运行 `.pte` 文件。

**模型支持与特性：**
该平台支持广泛的架构，包括大语言模型 (Llama 3.2)、多模态模型 (Llava)、视觉模型 (MobileNet) 和语音模型 (Whisper)。高级生产特性包括通过 `torchao` 实现的内置量化、优化资源使用的内存规划，以及用于剥离未使用算子并最小化二进制体积的“选择性构建”。

ExecuTorch 开源（采用 BSD 许可），并提供针对 Python、C++、Swift (iOS) 和 Kotlin (Android) 的全面 SDK，确保了在移动和边缘 AI 领域的广泛可移植性。

---

## 6. 自带语法高亮的字体 (2024)

**原文标题**: Font with Built-In Syntax Highlighting (2024)

**原文链接**: [https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/](https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/)

本文探讨了一种新颖的代码语法高亮方法，通过将逻辑直接嵌入字体文件，从而无需 JavaScript 库或复杂的 HTML 标签。作者的目标是通过消除 Prism 或 highlight.js 等传统高亮工具带来的冗余，简化手写网站的维护工作。

### 技术实现
作者利用两项主要的 OpenType 特性修改了开源字体 **Monaspace Krypton**：
*   **COLR 表：** 支持多色字形。作者创建了一个调色板，并为字符的替代版本分配了特定颜色。
*   **上下文替代 (`calt`)：** 该功能利用替换逻辑让字符能够“感知”相邻字符。通过链式替换，字体可以识别特定的关键字（如 `if` 或 `console`），并将标准字符替换为对应的彩色版本。对于变长模式（如 CSS 函数或 HTML 标签），作者设计了复杂的查找规则，以匹配后接特定触发器（如左括号）的字符串。

### 主要优势
*   **极简主义：** 无需 JavaScript 和额外的 CSS 主题，保持了 HTML 源代码的整洁。
*   **支持 Textarea：** 一个重大突破是该方法可以在 `<textarea>` 和 `<input>` 元素内部实现语法高亮，而传统库通常无法做到这一点，因为这些字段仅支持纯文本。
*   **便携性：** 高亮效果可在任何支持 OpenType 的环境中使用，包括 InDesign 等桌面设计软件。

### 局限性
该方法并非功能强大的脚本插件的完全替代品。它缺乏正则表达式的处理能力，无法处理多行高亮（如长注释块），且修改时需要专门的字体设计知识。然而，对于追求极简的开发者来说，它为代码展示提供了一种快速、无需维护的替代方案。

---

## 7. Show HN: Yapi – 面向高级用户的开源终端 API 客户端

**原文标题**: Show HN: Yapi – FOSS terminal API client for power users

**原文链接**: [https://yapi.run/blog/what-is-yapi](https://yapi.run/blog/what-is-yapi)

**Yapi** (Yet Another Protocol Interface) 是一款免费开源 (FOSS) 的基于终端的 API 客户端，专为偏好命令行工作流而非 Postman 或 Insomnia 等沉重 GUI 应用程序的开发者和高级用户设计。

Yapi 采用 **Rust** 构建，专注于速度、效率以及“配置即代码”的理念。其主要特性和优势包括：

*   **HCL 配置：** 不同于许多使用臃肿 JSON 或私有格式的 API 客户端，Yapi 使用 HashiCorp 配置语言 (HCL)。这使得配置不仅易于阅读，而且具备模块化和高度可扩展性。
*   **Git 友好：** 由于请求和环境均以纯文本文件存储，它们易于进行版本控制、代码审查，并能通过标准的 Git 工作流在团队间共享。
*   **终端用户界面 (TUI)：** 它提供了一个快速、以键盘为中心并具备类 Vim 快捷键的界面，允许用户在不离开终端或不使用鼠标的情况下进行导航、编辑和执行请求。
*   **高性能：** 通过避开基于 Electron 的框架，Yapi 保持了极低的资源占用，并提供近乎瞬时的启动速度。
*   **环境管理：** 它支持强大的环境变量处理，允许用户在开发、测试和生产环境配置之间无缝切换。

总而言之，Yapi 瞄准的是那些重视隐私、本地优先数据和终端集成的开发者。它弥合了 `curl` 等基础工具与臃肿 GUI 套件之间的鸿沟，为现代 API 开发提供了一个强大、可脚本化且可版本化的替代方案。

---

## 8. The Coffee Warehouse

**原文标题**: The Coffee Warehouse

**原文链接**: [https://www.scopeofwork.net/the-coffee-warehouse/](https://www.scopeofwork.net/the-coffee-warehouse/)

生成摘要时出错

---

## 9. Show HN: CineCLI – Browse and torrent movies directly from your terminal

**原文标题**: Show HN: CineCLI – Browse and torrent movies directly from your terminal

**原文链接**: [https://github.com/eyeblech/cinecli](https://github.com/eyeblech/cinecli)

生成摘要时出错

---

## 10. Carnap – A formal logic framework for Haskell

**原文标题**: Carnap – A formal logic framework for Haskell

**原文链接**: [https://carnap.io/](https://carnap.io/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 2 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 3 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 4 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 5 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 6 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 7 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 8 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 9 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 10 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 11 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 12 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 13 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 14 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 15 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 16 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 17 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 18 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 19 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 20 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 21 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 22 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 23 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 24 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 25 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 26 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 27 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 28 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 29 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 30 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 31 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 32 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 33 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 34 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 35 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 36 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 37 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 38 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 39 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 40 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 41 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 42 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 43 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 44 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 45 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 46 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 47 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 48 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 49 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 50 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 51 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 52 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 53 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 54 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 55 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 56 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 57 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 58 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 59 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 60 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 61 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 62 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 63 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 64 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 65 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 66 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 67 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 68 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 69 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 70 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 71 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 72 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 73 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 74 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 75 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 76 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 77 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 78 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 79 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 80 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 81 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 82 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 83 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 84 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 85 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 86 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 87 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 88 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 89 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 90 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 91 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 92 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 93 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 94 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 95 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 96 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 97 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 98 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 99 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 100 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 101 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 102 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 103 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 104 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 105 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 106 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 107 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 108 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 109 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 110 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 111 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 112 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 113 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 114 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 115 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 116 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 117 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 118 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 119 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 120 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 121 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 122 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 123 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 124 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 125 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 126 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 127 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 128 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 129 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 130 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 131 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 132 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 133 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 134 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 135 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 136 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 137 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 138 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 139 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 140 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 141 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 142 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 143 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 144 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 145 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 146 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 147 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 148 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 149 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 150 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 151 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 152 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 153 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 154 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 155 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 156 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 157 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 158 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 159 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 160 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 161 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 162 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 163 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 164 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 165 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 166 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 167 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 168 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 169 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 170 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 171 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 172 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 173 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 174 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 175 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 176 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 177 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 178 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 179 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 180 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 181 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 182 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 183 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 184 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 185 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 186 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 187 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 188 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 189 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 190 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 191 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 192 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 193 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 194 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 195 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 196 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 197 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 198 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 199 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 200 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 201 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 202 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 203 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 204 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 205 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 206 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 207 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 208 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 209 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 210 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 211 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 212 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 213 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 214 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 215 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 216 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 217 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 218 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 219 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 220 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 221 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 222 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 223 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 224 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 225 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 226 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 227 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 228 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 229 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 230 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 231 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 232 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 233 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 234 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 235 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 236 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 237 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 238 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 239 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 240 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 241 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 242 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 243 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 244 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 245 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 246 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 247 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 248 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 249 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 250 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 251 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 252 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 253 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 254 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 255 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 256 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 257 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 258 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 259 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 260 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 261 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 262 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 263 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 264 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 265 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 266 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 267 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 268 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 269 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 270 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 271 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 272 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 273 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 274 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 275 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 276 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 277 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 278 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
