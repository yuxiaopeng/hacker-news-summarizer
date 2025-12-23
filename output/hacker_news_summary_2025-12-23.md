# Hacker News 热门文章摘要 (2025-12-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Astrophotography Target Planner: Discover Hidden Nebulas

**原文标题**: Astrophotography Target Planner: Discover Hidden Nebulas

**原文链接**: [https://astroimagery.com/techniques/imaging/astrophotography-target-planner/](https://astroimagery.com/techniques/imaging/astrophotography-target-planner/)

生成摘要时出错

---

## 12. Snitch – A friendlier ss/netstat

**原文标题**: Snitch – A friendlier ss/netstat

**原文链接**: [https://github.com/karol-broda/snitch](https://github.com/karol-broda/snitch)

生成摘要时出错

---

## 13. 10 years bootstrapped: €6.5M revenue with a team of 13

**原文标题**: 10 years bootstrapped: €6.5M revenue with a team of 13

**原文链接**: [https://www.datocms.com/blog/a-look-back-at-2025](https://www.datocms.com/blog/a-look-back-at-2025)

生成摘要时出错

---

## 14. It's Always TCP_NODELAY

**原文标题**: It's Always TCP_NODELAY

**原文链接**: [https://brooker.co.za/blog/2024/05/09/nagle.html](https://brooker.co.za/blog/2024/05/09/nagle.html)

生成摘要时出错

---

## 15. Meta Is Using the Linux Scheduler Designed for Valve's Steam Deck on Its Servers

**原文标题**: Meta Is Using the Linux Scheduler Designed for Valve's Steam Deck on Its Servers

**原文链接**: [https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server](https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server)

生成摘要时出错

---

## 16. The Illustrated Transformer

**原文标题**: The Illustrated Transformer

**原文链接**: [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

生成摘要时出错

---

## 17. Ultrasound Cancer Treatment: Sound Waves Fight Tumors

**原文标题**: Ultrasound Cancer Treatment: Sound Waves Fight Tumors

**原文链接**: [https://spectrum.ieee.org/ultrasound-cancer-treatment](https://spectrum.ieee.org/ultrasound-cancer-treatment)

生成摘要时出错

---

## 18. Dancing around the rhythm space with Euclid

**原文标题**: Dancing around the rhythm space with Euclid

**原文链接**: [https://pv.wtf/posts/euclidean-rhythms](https://pv.wtf/posts/euclidean-rhythms)

生成摘要时出错

---

## 19. Partial inlining

**原文标题**: Partial inlining

**原文链接**: [https://xania.org/202512/18-partial-inlining](https://xania.org/202512/18-partial-inlining)

生成摘要时出错

---

## 20. GLM-4.7: Advancing the Coding Capability

**原文标题**: GLM-4.7: Advancing the Coding Capability

**原文链接**: [https://z.ai/blog/glm-4.7](https://z.ai/blog/glm-4.7)

生成摘要时出错

---

## 21. Diary: Val McDermid, Deep Winter

**原文标题**: Diary: Val McDermid, Deep Winter

**原文链接**: [https://books.substack.com/p/diary-val-mcdermid-deep-winter](https://books.substack.com/p/diary-val-mcdermid-deep-winter)

生成摘要时出错

---

## 22. Inside CECOT – 60 Minutes [video]

**原文标题**: Inside CECOT – 60 Minutes [video]

**原文链接**: [https://archive.org/details/insidececot](https://archive.org/details/insidececot)

生成摘要时出错

---

## 23. NIST was 5 μs off UTC after last week's power cut

**原文标题**: NIST was 5 μs off UTC after last week's power cut

**原文链接**: [https://www.jeffgeerling.com/blog/2025/nist-was-5-μs-utc-after-last-weeks-power-cut](https://www.jeffgeerling.com/blog/2025/nist-was-5-μs-utc-after-last-weeks-power-cut)

生成摘要时出错

---

## 24. The Polyglot NixOS

**原文标题**: The Polyglot NixOS

**原文链接**: [https://x86.lol/generic/2025/12/19/polyglot.html](https://x86.lol/generic/2025/12/19/polyglot.html)

生成摘要时出错

---

## 25. Our New Sam Audio Model Transforms Audio Editing

**原文标题**: Our New Sam Audio Model Transforms Audio Editing

**原文链接**: [https://about.fb.com/news/2025/12/our-new-sam-audio-model-transforms-audio-editing/](https://about.fb.com/news/2025/12/our-new-sam-audio-model-transforms-audio-editing/)

生成摘要时出错

---

## 26. Debian adds LoongArch as officially supported architecture

**原文标题**: Debian adds LoongArch as officially supported architecture

**原文链接**: [https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html](https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html)

生成摘要时出错

---

## 27. The Garbage Collection Handbook

**原文标题**: The Garbage Collection Handbook

**原文链接**: [https://gchandbook.org/index.html](https://gchandbook.org/index.html)

生成摘要时出错

---

## 28. Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文标题**: Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文链接**: [https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/](https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/)

生成摘要时出错

---

## 29. Claude Code gets native LSP support

**原文标题**: Claude Code gets native LSP support

**原文链接**: [https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

生成摘要时出错

---

## 30. The Duodecimal Bulletin, Vol. 55, No. 1, Year 1209 [pdf]

**原文标题**: The Duodecimal Bulletin, Vol. 55, No. 1, Year 1209 [pdf]

**原文链接**: [https://dozenal.org/drupal/sites_bck/default/files/DuodecimalBulletinIssue551.pdf](https://dozenal.org/drupal/sites_bck/default/files/DuodecimalBulletinIssue551.pdf)

生成摘要时出错

---

## 31. FPGAs Need a New Future

**原文标题**: FPGAs Need a New Future

**原文链接**: [https://www.allaboutcircuits.com/industry-articles/fpgas-need-a-new-future/](https://www.allaboutcircuits.com/industry-articles/fpgas-need-a-new-future/)

生成摘要时出错

---

## 32. Solving the Problems of HBM-on-Logic

**原文标题**: Solving the Problems of HBM-on-Logic

**原文链接**: [https://morethanmoore.substack.com/p/solving-the-problems-of-hbm-on-logic](https://morethanmoore.substack.com/p/solving-the-problems-of-hbm-on-logic)

生成摘要时出错

---

## 33. Classical billiards can compute (2d billiard systems are Turing complete)

**原文标题**: Classical billiards can compute (2d billiard systems are Turing complete)

**原文链接**: [https://arxiv.org/abs/2512.19156](https://arxiv.org/abs/2512.19156)

生成摘要时出错

---

## 34. Scaling LLMs to Larger Codebases

**原文标题**: Scaling LLMs to Larger Codebases

**原文链接**: [https://blog.kierangill.xyz/oversight-and-guidance](https://blog.kierangill.xyz/oversight-and-guidance)

生成摘要时出错

---

## 35. The last product to get cancelled

**原文标题**: The last product to get cancelled

**原文链接**: [https://www.ablg.io/blog/last-product-to-get-cancelled](https://www.ablg.io/blog/last-product-to-get-cancelled)

生成摘要时出错

---

## 36. Remove Black Color with Shaders

**原文标题**: Remove Black Color with Shaders

**原文链接**: [https://yuanchuan.dev/remove-black-color-with-shaders](https://yuanchuan.dev/remove-black-color-with-shaders)

生成摘要时出错

---

## 37. Are We Loong Yet?

**原文标题**: Are We Loong Yet?

**原文链接**: [https://areweloongyet.com/en/](https://areweloongyet.com/en/)

生成摘要时出错

---

## 38. Programming languages used for music

**原文标题**: Programming languages used for music

**原文链接**: [https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes](https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes)

生成摘要时出错

---

## 39. Universal Reasoning Model (53.8% pass 1 ARC1 and 16.0% ARC 2)

**原文标题**: Universal Reasoning Model (53.8% pass 1 ARC1 and 16.0% ARC 2)

**原文链接**: [https://arxiv.org/abs/2512.14693](https://arxiv.org/abs/2512.14693)

生成摘要时出错

---

## 40. Debian's Git Transition

**原文标题**: Debian's Git Transition

**原文链接**: [https://diziet.dreamwidth.org/20436.html](https://diziet.dreamwidth.org/20436.html)

生成摘要时出错

---

## 41. Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文标题**: Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文链接**: [https://www.useparallel.com/uplane1/careers](https://www.useparallel.com/uplane1/careers)

生成摘要时出错

---

## 42. The biggest CRT ever made: Sony's PVM-4300

**原文标题**: The biggest CRT ever made: Sony's PVM-4300

**原文链接**: [https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/](https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/)

生成摘要时出错

---

## 43. The post-GeForce era: What if Nvidia abandons PC gaming?

**原文标题**: The post-GeForce era: What if Nvidia abandons PC gaming?

**原文链接**: [https://www.pcworld.com/article/3013044/the-post-geforce-era-what-if-nvidia-abandons-pc-gaming.html](https://www.pcworld.com/article/3013044/the-post-geforce-era-what-if-nvidia-abandons-pc-gaming.html)

生成摘要时出错

---

## 44. How the RESISTORS put computing into 1960s counter-culture

**原文标题**: How the RESISTORS put computing into 1960s counter-culture

**原文链接**: [https://spectrum.ieee.org/teenage-hackers](https://spectrum.ieee.org/teenage-hackers)

生成摘要时出错

---

## 45. Show HN: Python SDK – forecasting with foundation time-series and tabular models

**原文标题**: Show HN: Python SDK – forecasting with foundation time-series and tabular models

**原文链接**: [https://github.com/S-FM/faim-python-client](https://github.com/S-FM/faim-python-client)

生成摘要时出错

---

## 46. A centennial look back at Edward Gorey's macabre art and guarded life

**原文标题**: A centennial look back at Edward Gorey's macabre art and guarded life

**原文链接**: [https://www.washingtonpost.com/books/2025/12/13/edward-gorey-centennial-gregory-hischak-review/](https://www.washingtonpost.com/books/2025/12/13/edward-gorey-centennial-gregory-hischak-review/)

生成摘要时出错

---

## 47. Show HN: C-compiler to compile TCC for live-bootstrap

**原文标题**: Show HN: C-compiler to compile TCC for live-bootstrap

**原文链接**: [https://github.com/FransFaase/MES-replacement](https://github.com/FransFaase/MES-replacement)

生成摘要时出错

---

## 48. FCC Updates Covered List to Include Foreign UAS and UAS Critical Components [pdf]

**原文标题**: FCC Updates Covered List to Include Foreign UAS and UAS Critical Components [pdf]

**原文链接**: [https://docs.fcc.gov/public/attachments/DOC-416839A1.pdf](https://docs.fcc.gov/public/attachments/DOC-416839A1.pdf)

生成摘要时出错

---

## 49. The ancient monuments saluting the winter solstice

**原文标题**: The ancient monuments saluting the winter solstice

**原文链接**: [https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice](https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice)

生成摘要时出错

---

## 50. Lotusbail npm package found to be harvesting WhatsApp messages and contacts

**原文标题**: Lotusbail npm package found to be harvesting WhatsApp messages and contacts

**原文链接**: [https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages](https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages)

生成摘要时出错

---

## 51. Tc – Theodore Calvin's language-agnostic testing framework

**原文标题**: Tc – Theodore Calvin's language-agnostic testing framework

**原文链接**: [https://github.com/ahoward/tc](https://github.com/ahoward/tc)

生成摘要时出错

---

## 52. How I protect my Forgejo instance from AI web crawlers

**原文标题**: How I protect my Forgejo instance from AI web crawlers

**原文链接**: [https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html](https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html)

生成摘要时出错

---

## 53. Plugins case study: mdBook preprocessors

**原文标题**: Plugins case study: mdBook preprocessors

**原文链接**: [https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/](https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/)

生成摘要时出错

---

## 54. Pulled 60 Minutes segment on CECOT

**原文标题**: Pulled 60 Minutes segment on CECOT

**原文链接**: [https://archive.org/details/60minutes-cecotsegment](https://archive.org/details/60minutes-cecotsegment)

生成摘要时出错

---

## 55. Wax Figure of Idris Elba Unlocks Face ID

**原文标题**: Wax Figure of Idris Elba Unlocks Face ID

**原文链接**: [https://www.complex.com/pop-culture/a/treyalston/idris-elba-wax-figure-unlocks-face-id](https://www.complex.com/pop-culture/a/treyalston/idris-elba-wax-figure-unlocks-face-id)

生成摘要时出错

---

## 56. I announced my divorce on Instagram and then AI impersonated me

**原文标题**: I announced my divorce on Instagram and then AI impersonated me

**原文链接**: [https://eiratansey.com/2025/12/20/i-announced-my-divorce-on-instagram-and-then-ai-impersonated-me/](https://eiratansey.com/2025/12/20/i-announced-my-divorce-on-instagram-and-then-ai-impersonated-me/)

生成摘要时出错

---

## 57. Waymo halts service during S.F. blackout after causing traffic jams

**原文标题**: Waymo halts service during S.F. blackout after causing traffic jams

**原文链接**: [https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/](https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/)

生成摘要时出错

---

## 58. More on whether useful quantum computing is “imminent”

**原文标题**: More on whether useful quantum computing is “imminent”

**原文链接**: [https://scottaaronson.blog/?p=9425](https://scottaaronson.blog/?p=9425)

生成摘要时出错

---

## 59. Rue: Higher level than Rust, lower level than Go

**原文标题**: Rue: Higher level than Rust, lower level than Go

**原文链接**: [https://rue-lang.dev/](https://rue-lang.dev/)

生成摘要时出错

---

## 60. In Pursuit of Clancy Sigal (2021)

**原文标题**: In Pursuit of Clancy Sigal (2021)

**原文链接**: [https://yalereview.org/article/in-pursuit-of-clancy-sigal](https://yalereview.org/article/in-pursuit-of-clancy-sigal)

生成摘要时出错

---

## 61. Webb observes exoplanet that may have an exotic helium and carbon atmosphere

**原文标题**: Webb observes exoplanet that may have an exotic helium and carbon atmosphere

**原文链接**: [https://science.nasa.gov/missions/webb/nasas-webb-observes-exoplanet-whose-composition-defies-explanation/](https://science.nasa.gov/missions/webb/nasas-webb-observes-exoplanet-whose-composition-defies-explanation/)

生成摘要时出错

---

## 62. The Rise of SQL:the second programming language everyone needs to know

**原文标题**: The Rise of SQL:the second programming language everyone needs to know

**原文链接**: [https://spectrum.ieee.org/the-rise-of-sql](https://spectrum.ieee.org/the-rise-of-sql)

生成摘要时出错

---

## 63. Hybrid Aerial Underwater Drone – Bachelor Project [video]

**原文标题**: Hybrid Aerial Underwater Drone – Bachelor Project [video]

**原文链接**: [https://www.youtube.com/watch?v=g7vmPFZrYAk](https://www.youtube.com/watch?v=g7vmPFZrYAk)

生成摘要时出错

---

## 64. Jimmy Lai Is a Martyr for Freedom

**原文标题**: Jimmy Lai Is a Martyr for Freedom

**原文链接**: [https://reason.com/2025/12/19/jimmy-lai-is-a-martyr-for-freedom/](https://reason.com/2025/12/19/jimmy-lai-is-a-martyr-for-freedom/)

生成摘要时出错

---

## 65. Henge Finder

**原文标题**: Henge Finder

**原文链接**: [https://hengefinder.rcdis.co/#learn](https://hengefinder.rcdis.co/#learn)

生成摘要时出错

---

## 66. Build Android apps using Rust and Iced

**原文标题**: Build Android apps using Rust and Iced

**原文链接**: [https://github.com/ibaryshnikov/android-iced-example](https://github.com/ibaryshnikov/android-iced-example)

生成摘要时出错

---

## 67. If you don't design your career, someone else will (2014)

**原文标题**: If you don't design your career, someone else will (2014)

**原文链接**: [https://gregmckeown.com/if-you-dont-design-your-career-someone-else-will/](https://gregmckeown.com/if-you-dont-design-your-career-someone-else-will/)

生成摘要时出错

---

## 68. Show HN: Jmail – Google Suite for Epstein files

**原文标题**: Show HN: Jmail – Google Suite for Epstein files

**原文链接**: [https://www.jmail.world](https://www.jmail.world)

生成摘要时出错

---

## 69. Things I learnt about passkeys when building passkeybot

**原文标题**: Things I learnt about passkeys when building passkeybot

**原文链接**: [https://enzom.dev/b/passkeys/](https://enzom.dev/b/passkeys/)

生成摘要时出错

---

## 70. Kernighan's Lever

**原文标题**: Kernighan's Lever

**原文链接**: [https://linusakesson.net/programming/kernighans-lever/index.php](https://linusakesson.net/programming/kernighans-lever/index.php)

生成摘要时出错

---

## 71. Decompiling the Synergy: Human–LLM Teaming in Reverse Engineering [pdf]

**原文标题**: Decompiling the Synergy: Human–LLM Teaming in Reverse Engineering [pdf]

**原文链接**: [https://www.zionbasque.com/files/papers/dec-synergy-study.pdf](https://www.zionbasque.com/files/papers/dec-synergy-study.pdf)

生成摘要时出错

---

## 72. A guide to local coding models

**原文标题**: A guide to local coding models

**原文链接**: [https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude](https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude)

生成摘要时出错

---

## 73. Show HN: Netrinos – A keep it simple Mesh VPN for small teams

**原文标题**: Show HN: Netrinos – A keep it simple Mesh VPN for small teams

**原文链接**: [https://netrinos.com](https://netrinos.com)

生成摘要时出错

---

## 74. Toad is a unified experience for AI in the terminal

**原文标题**: Toad is a unified experience for AI in the terminal

**原文链接**: [https://willmcgugan.github.io/toad-released/](https://willmcgugan.github.io/toad-released/)

生成摘要时出错

---

## 75. Backing up Spotify

**原文标题**: Backing up Spotify

**原文链接**: [https://annas-archive.li/blog/backing-up-spotify.html](https://annas-archive.li/blog/backing-up-spotify.html)

生成摘要时出错

---

## 76. Show HN: Books mentioned on Hacker News in 2025

**原文标题**: Show HN: Books mentioned on Hacker News in 2025

**原文链接**: [https://hackernews-readings-613604506318.us-west1.run.app](https://hackernews-readings-613604506318.us-west1.run.app)

生成摘要时出错

---

## 77. We Just Unredacted the Epstein Files

**原文标题**: We Just Unredacted the Epstein Files

**原文链接**: [https://krassencast.com/p/breaking-we-just-unredacted-the-epstein](https://krassencast.com/p/breaking-we-just-unredacted-the-epstein)

生成摘要时出错

---

## 78. Deliberate Internet Shutdowns

**原文标题**: Deliberate Internet Shutdowns

**原文链接**: [https://www.schneier.com/blog/archives/2025/12/deliberate-internet-shutdowns.html](https://www.schneier.com/blog/archives/2025/12/deliberate-internet-shutdowns.html)

生成摘要时出错

---

## 79. State regulators vote to keep utility profits high angering customers across CA

**原文标题**: State regulators vote to keep utility profits high angering customers across CA

**原文链接**: [https://www.latimes.com/environment/story/2025-12-18/state-regulators-vote-to-keep-utility-profits-high-angering-customers](https://www.latimes.com/environment/story/2025-12-18/state-regulators-vote-to-keep-utility-profits-high-angering-customers)

生成摘要时出错

---

## 80. I wish people were more public

**原文标题**: I wish people were more public

**原文链接**: [https://borretti.me/article/i-wish-people-were-more-public](https://borretti.me/article/i-wish-people-were-more-public)

生成摘要时出错

---

## 81. There Is No Future for Online Safety Without Privacy and Security

**原文标题**: There Is No Future for Online Safety Without Privacy and Security

**原文链接**: [https://itsfoss.com/news/alexander-linton-interview/](https://itsfoss.com/news/alexander-linton-interview/)

生成摘要时出错

---

## 82. Gimp Source Code

**原文标题**: Gimp Source Code

**原文链接**: [https://gitlab.gnome.org/GNOME/gimp](https://gitlab.gnome.org/GNOME/gimp)

生成摘要时出错

---

## 83. Satellites reveal heat leaking from largest US cryptocurrency mining center

**原文标题**: Satellites reveal heat leaking from largest US cryptocurrency mining center

**原文链接**: [https://www.space.com/space-exploration/satellites/satellites-reveal-heat-leaking-from-largest-us-cryptocurrency-mining-center](https://www.space.com/space-exploration/satellites/satellites-reveal-heat-leaking-from-largest-us-cryptocurrency-mining-center)

生成摘要时出错

---

## 84. The gift card accountability sink

**原文标题**: The gift card accountability sink

**原文链接**: [https://www.bitsaboutmoney.com/archive/gift-card-accountability-sink/](https://www.bitsaboutmoney.com/archive/gift-card-accountability-sink/)

生成摘要时出错

---

## 85. Cartoon Network channel errors (1995 – 2025)

**原文标题**: Cartoon Network channel errors (1995 – 2025)

**原文链接**: [https://cnas.fandom.com/wiki/Channel_Errors](https://cnas.fandom.com/wiki/Channel_Errors)

生成摘要时出错

---

## 86. Ireland plans to make a $1,500 a month basic income for artists permanent

**原文标题**: Ireland plans to make a $1,500 a month basic income for artists permanent

**原文链接**: [https://www.aol.com/news/ireland-plans-1-500-month-202733101.html](https://www.aol.com/news/ireland-plans-1-500-month-202733101.html)

生成摘要时出错

---

## 87. Nanostructured coatings puncture bacteria to prevent biofilm formation

**原文标题**: Nanostructured coatings puncture bacteria to prevent biofilm formation

**原文链接**: [https://phys.org/news/2025-11-nanostructured-coatings-physically-bacteria-biofilm.html](https://phys.org/news/2025-11-nanostructured-coatings-physically-bacteria-biofilm.html)

生成摘要时出错

---

## 88. Measuring AI Ability to Complete Long Tasks

**原文标题**: Measuring AI Ability to Complete Long Tasks

**原文链接**: [https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

生成摘要时出错

---

## 89. Italian Competition Authority Fines Apple $115M for Abusing Dominant Position

**原文标题**: Italian Competition Authority Fines Apple $115M for Abusing Dominant Position

**原文链接**: [https://en.agcm.it/en/media/press-releases/2025/12/A561](https://en.agcm.it/en/media/press-releases/2025/12/A561)

生成摘要时出错

---

## 90. Show HN: An easy way of broadcasting radio around you (looking for feedback)

**原文标题**: Show HN: An easy way of broadcasting radio around you (looking for feedback)

**原文链接**: [https://github.com/dpipstudio/botwave](https://github.com/dpipstudio/botwave)

生成摘要时出错

---

## 91. ONNX Runtime and CoreML May Silently Convert Your Model to FP16

**原文标题**: ONNX Runtime and CoreML May Silently Convert Your Model to FP16

**原文链接**: [https://ym2132.github.io/ONNX_MLProgram_NN_exploration](https://ym2132.github.io/ONNX_MLProgram_NN_exploration)

生成摘要时出错

---

## 92. CO2 batteries that store grid energy take off globally

**原文标题**: CO2 batteries that store grid energy take off globally

**原文链接**: [https://spectrum.ieee.org/co2-battery-energy-storage](https://spectrum.ieee.org/co2-battery-energy-storage)

生成摘要时出错

---

## 93. Disney Imagineering Debuts Next-Generation Robotic Character, Olaf

**原文标题**: Disney Imagineering Debuts Next-Generation Robotic Character, Olaf

**原文链接**: [https://disneyparksblog.com/disney-experiences/robotic-olaf-marks-new-era-of-disney-innovation/](https://disneyparksblog.com/disney-experiences/robotic-olaf-marks-new-era-of-disney-innovation/)

生成摘要时出错

---

## 94. History LLMs: Models trained exclusively on pre-1913 texts

**原文标题**: History LLMs: Models trained exclusively on pre-1913 texts

**原文链接**: [https://github.com/DGoettlich/history-llms](https://github.com/DGoettlich/history-llms)

生成摘要时出错

---

## 95. Show HN: HN Wrapped 2025 - an LLM reviews your year on HN

**原文标题**: Show HN: HN Wrapped 2025 - an LLM reviews your year on HN

**原文链接**: [https://hn-wrapped.kadoa.com?year=2025](https://hn-wrapped.kadoa.com?year=2025)

生成摘要时出错

---

## 96. You’re not burnt out, you’re existentially starving

**原文标题**: You’re not burnt out, you’re existentially starving

**原文链接**: [https://neilthanedar.com/youre-not-burnt-out-youre-existentially-starving/](https://neilthanedar.com/youre-not-burnt-out-youre-existentially-starving/)

生成摘要时出错

---

## 97. US bars approvals of new models of DJI, all other foreign drones

**原文标题**: US bars approvals of new models of DJI, all other foreign drones

**原文链接**: [https://www.reuters.com/business/aerospace-defense/us-adds-dji-other-foreign-drones-national-security-list-2025-12-22/](https://www.reuters.com/business/aerospace-defense/us-adds-dji-other-foreign-drones-national-security-list-2025-12-22/)

生成摘要时出错

---

## 98. Frederick Douglass on the Book That Changed His Life

**原文标题**: Frederick Douglass on the Book That Changed His Life

**原文链接**: [https://derekbishton.com/frederick-douglass-on-the-book-that-changed-his-life/](https://derekbishton.com/frederick-douglass-on-the-book-that-changed-his-life/)

生成摘要时出错

---

## 99. A year of vibes

**原文标题**: A year of vibes

**原文链接**: [https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)

生成摘要时出错

---

## 100. Evaluating chain-of-thought monitorability

**原文标题**: Evaluating chain-of-thought monitorability

**原文链接**: [https://openai.com/index/evaluating-chain-of-thought-monitorability/](https://openai.com/index/evaluating-chain-of-thought-monitorability/)

生成摘要时出错

---

