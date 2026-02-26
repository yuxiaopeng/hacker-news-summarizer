# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-26.md)

*最后自动更新时间: 2026-02-26 18:20:49*
## 1. AirSnitch：揭秘与破解 Wi-Fi 网络中的客户端隔离 [pdf]

**原文标题**: AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]

**原文链接**: [https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

论文《AirSnitch：揭秘并破解 Wi-Fi 网络中的客户端隔离》探讨了 Wi-Fi 客户端隔离（CI）中的系统性漏洞。CI 是一项旨在防止同一网络上的无线设备相互通信或攻击的安全功能，是公共热点（如机场、酒店）和企业环境中的标准安全措施。

作者指出，尽管 CI 被宣传为一种强大的防御手段，但在大多数现代实现中，它从根本上是失效的。核心问题在于 IEEE 802.11 标准并未正式定义应如何实现客户端隔离，导致不同厂商和固件之间的行为不一致且不安全。

**主要研究发现包括：**

*   **AirSnitch 框架：** 研究人员开发了“AirSnitch”，这是一种旨在分析和利用 CI 缺陷的工具。利用该框架，他们识别出三大类漏洞：
    1.  **信息泄露：** 接入点（AP）经常泄露敏感元数据或广播流量，使攻击者能够绘制网络拓扑。
    2.  **侧信道攻击：** 攻击者可以利用时序和电源管理侧信道来探测其他“受隔离”客户端的存在和活动。
    3.  **隔离绕过：** 最重要的发现是，攻击者可以诱导接入点（AP）充当单播流量的中继，从而有效打通隔离客户端之间的连接。
*   **实际利用：** 通过绕过 CI，作者成功实施了经典的对等网络攻击，包括 **ARP 欺骗、DNS 污染和 TCP 会话劫持**，而这些攻击正是 CI 专门旨在预防的。
*   **广泛的易感性：** 该研究测试了大量的商用路由器和开源固件（如 OpenWrt），发现绝大多数设备都容易受到至少一种形式的绕过攻击。

论文最后得出结论，CI 提供了一种**虚假的安全感**，并呼吁 IEEE 和硬件厂商实现隔离协议的标准化，以确保针对内部网络威胁提供一致的跨厂商保护。

---

## 2. 开源基金 —— 开源维护者的新资金来源

**原文标题**: Open Source Endowment – new funding source for open source maintainers

**原文链接**: [https://endowment.dev/](https://endowment.dev/)

**开源禀赋基金 (OSE)** 是一项社区驱动的非营利倡议，旨在为关键开源软件 (OSS) 提供永久且可持续的资金支持。它致力于解决技术生态系统中的“可持续性危机”——即全球数字基础设施高度依赖无偿志愿者，从而导致维护者倦怠以及类似 Heartbleed 和 Log4Shell 的安全风险。

OSE 采用了顶尖大学所使用的财务模式：通过募集捐赠建立永久本金，并将其投资于低风险的投资组合。该基金不消耗本金，而是仅分配投资回报（目标为 **5% 的年度支出率**）来资助开源软件维护者。这确保了资金流的稳定性，使其不受波动不定的企业预算或经济变动的影响。

**OSE 的核心特点包括：**
*   **数据驱动的资助决策：** 资助决策基于可衡量的影响力和 SMART 目标，以支持那些资金匮乏但至关重要的项目。
*   **中立与透明：** 组织运行受公共治理监督，并保持独立，不受政治或企业影响。
*   **社区治理：** 捐赠 1,000 美元或以上的捐赠者将成为“成员”，参与塑造基金的战略方向。

该倡议已获得多位知名“开源校友”的支持，包括来自 **HashiCorp、Nginx、Vue.js、Sentry 和 GitHub** 的创始人及高管。目前，该基金已从 60 多位捐赠者处筹集了超过 **69.3 万美元**。通过利用去中心化的全球视野，OSE 旨在凭借精简、数字化优先且透明的组织架构，保护全球软件供应链的长期健康。

---

## 3. Nano Banana 2：谷歌最新的 AI 图像生成模型

**原文标题**: Nano Banana 2: Google's latest AI image generation model

**原文链接**: [https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)

2026年2月26日，Google DeepMind 宣布推出 **Nano Banana 2** (Gemini 3.1 Flash Image)。这是一款顶尖的图像生成模型，旨在将“Pro”级的智能与“Flash”级的速度完美结合。

**核心功能与能力：**
*   **速度与质量：** 该模型弥合了高保真视觉质量与快速迭代之间的差距，让专业级工具触手可及，满足日常使用需求。
*   **先进智能：** 通过利用 Google 的实时网络搜索和全球知识，Nano Banana 2 能够精准呈现特定主体，创作复杂的信息图表，并根据笔记生成数据可视化图表。
*   **创意控制：** 重大升级包括**主体一致性**（在不同图像中保持多达五个角色的一致外观）、精准的指令遵循，以及图像内准确的文本呈现与翻译。
*   **制作规格：** 该模型支持从 512px 到 **4K** 的分辨率，提供适用于营销和社交媒体的鲜活光影与丰富纹理。

**可用性：**
Nano Banana 2 正在 Google 生态系统中全面推广：
*   **Gemini 应用：** 它将作为默认模型提供；Pro 和 Ultra 订阅用户仍可访问原有的 Nano Banana Pro 以处理特定任务。
*   **搜索与广告：** 已集成至 AI 模式、Google 镜头 (Lens) 和 Google Ads 营销工具。
*   **开发者工具：** 可通过 AI Studio 和 Vertex AI 中的 Gemini API 获取。
*   **全球覆盖：** 部署范围涵盖 141 个新国家和地区，并新增支持 8 种语言。

**安全与溯源：**
Google 正在通过将 **SynthID** 技术与 **C2PA 内容凭据 (Content Credentials)** 相结合，深化其对 AI 透明度的承诺。这些工具为 AI 创作或编辑媒体的过程提供了“全方位视角”。Google 指出，其 SynthID 验证功能在 Gemini 应用中的使用次数已突破 2000 万次。

---

## 4. Palm OS 用户界面指南 [PDF, 2003]

**原文标题**: Palm OS User Interface Guidelines [pdf, 2003]

**原文链接**: [https://cs.uml.edu/~fredm/courses/91.308-spr05/files/palmdocs/uiguidelines.pdf](https://cs.uml.edu/~fredm/courses/91.308-spr05/files/palmdocs/uiguidelines.pdf)

《Palm OS 用户界面指南》(2003) 是在 Palm 计算平台上开发应用程序的权威设计手册。其核心是“Palm 禅学”（Zen of Palm）理念，强调为以“短促碎片化”而非长时间坐定方式使用设备的用户提供简单、快速且高效的体验。

关键原则与信息包括：

*   **为移动而设计**：与桌面软件不同，Palm OS 应用程序必须针对即时访问进行优化。指南强调“单手操作”和“三击规则”，即用户应能通过最少的导航步骤完成绝大多数任务。
*   **硬件限制**：设计必须考虑有限的屏幕空间（传统为 160x160 像素）、有限的电池寿命以及基于手写笔的输入。手册提供了按钮、复选框和列表的具体布局规范，以确保它们易于点击。
*   **减少数据输入**：由于通过 Graffiti 或屏幕键盘输入文字的速度慢于实体键盘，指南鼓励开发者使用选取列表、选择器和复选框，以尽量减少打字需求。
*   **界面一致性**：文档详细说明了标准 UI 元素（如应用程序启动器、命令工具栏和菜单），以确保统一的用户体验。它规定了“确定”和“取消”按钮的标准行为，以防止用户产生困惑。
*   **性能与反馈**：应用程序应具备即时响应感。指南建议对耗时任务使用进度指示器，并使用视觉“高亮”效果来显示按钮或列表项已被成功点击。
*   **扁平化层级**：敦促开发者避免嵌套对话框和复杂的导航树，提倡扁平的应用结构，使用户能够专注于数据本身。

最终，这些指南旨在使界面变得“透明”，让用户能够快速管理信息并随即回归到现实世界的任务中。

---

## 5. 2026年的谷歌街景

**原文标题**: Google Street View in 2026

**原文链接**: [https://tech.marksblogg.com/google-street-view-coverage.html](https://tech.marksblogg.com/google-street-view-coverage.html)

本文详细介绍了一个处理和分析 Google 街景全球覆盖范围数据集的技术工作流，该数据集记录了数百万个数据点的最新采集日期。

作者使用高性能工作站（AMD Ryzen 9 9950X，96GB 内存），利用 **DuckDB v1.4.3** 及其空间扩展功能来管理数据。处理流程始于从第三方源下载 131 个 JSON 文件（约 647 MB）。随后将这些文件导入 DuckDB，并将其转换为经过空间排序和 ZStandard 压缩的 **Parquet 文件**。最终数据集包含超过 **710 万行**，体积精简至 85 MB。

关键发现与技术步骤包括：
*   **时间分布**：数据跨度从 2003 年到 2025 年。虽然大多数数据点集中在 2008 年至 2024 年之间，但该数据集已包含 8.3 万个标注为 2025 年的数据点。
*   **地理空间可视化**：作者利用 **QGIS 3.44** 生成了欧洲、北美、拉丁美洲和亚太地区的地图。这些地图通过颜色编码来区分早期覆盖（可追溯至 2007 年）与近期更新。
*   **数据缺失**：作者指出，该特定版本目前缺少越南、波斯尼亚和黑塞哥维那以及纳米比亚等几个国家的覆盖数据。

本文既是对高效地理空间数据工程（特别是利用 **希尔伯特编码 (Hilbert encoding)** 进行 Parquet 空间排序）的技术演示，也是对 Google 全球地图测绘进度的现状报告。作者在结尾表示可为类似的地理空间和开发项目提供专业咨询服务。

---

## 6. Show HN: Terminal Phone – 命令行端到端加密对讲机

**原文标题**: Show HN: Terminal Phone – E2EE Walkie Talkie from the Command Line

**原文链接**: [https://gitlab.com/here_forawhile/terminalphone](https://gitlab.com/here_forawhile/terminalphone)

**Terminal Phone** 是一款开源的命令行界面 (CLI) 工具，旨在实现安全、实时的语音通信——其功能类似于数字对讲机。

主要特性与技术亮点包括：

*   **端到端加密 (E2EE)：** 该工具将隐私放在首位，确保音频数据在传输前在本地完成加密，这意味着任何中间服务器都无法访问通话内容。
*   **点对点连接：** 它利用 **WebRTC** 在用户之间建立直接连接。这使得应用程序能够有效地处理 NAT 穿透，无需复杂的手动配置即可实现跨网络通信。
*   **极简设计：** 专为大部分时间在终端环境中工作的开发人员和系统管理员打造，为 Discord、Slack 或 Zoom 等资源密集型 GUI 应用提供了一个低开销的替代方案。
*   **简单易用：** 用户可以通过简单的命令和唯一标识符发起或加入通话，保持以键盘为中心的工作流程。

本质上，Terminal Phone 提供了一种安全、轻量且“极客友好”的方式，让用户无需离开命令行提示符即可进行语音聊天。

---

## 7. Google API keys weren't secrets, but then Gemini changed the rules

**原文标题**: Google API keys weren't secrets, but then Gemini changed the rules

**原文链接**: [https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules)

For over a decade, Google advised developers that certain API keys (such as those for Maps or Firebase) were project identifiers rather than secrets, making them safe to embed in public client-side code. However, a report by Truffle Security reveals that the introduction of Gemini has turned these public keys into sensitive credentials.

**The Problem**
When the Gemini API (Generative Language API) is enabled on a Google Cloud project, any existing API keys in that project—including those already deployed in public HTML or JavaScript—automatically gain access to Gemini endpoints. This "Retroactive Privilege Expansion" happens without notification to the developer. Because Google Cloud keys default to an "unrestricted" state, a key intended for a simple map widget can suddenly be used to:
*   Access private uploaded files and cached AI data.
*   Incur massive charges by running up LLM usage.
*   Exhaust account quotas, shutting down legitimate services.

**Scale and Impact**
Truffle Security identified nearly 3,000 live keys on the public internet that were vulnerable to this privilege escalation, including keys belonging to major financial institutions and Google itself. Google initially dismissed the report but later reclassified it as a "Single-Service Privilege Escalation" (Tier 1) after seeing evidence of their own exposed internal infrastructure.

**Remediation**
Google is currently working on "scoped defaults" for new keys and better leaked-key detection. In the meantime, developers should:
1.  **Audit GCP Projects:** Check if the "Generative Language API" is enabled.
2.  **Restrict Keys:** Ensure API keys are restricted to specific services and not left "Unrestricted."
3.  **Rotate Exposed Keys:** Any key previously embedded in client-side code should be rotated if Gemini access is now enabled on that project.

---

## 8. Bild AI (YC W25) Is Hiring Interns to Make Housing Affordable

**原文标题**: Bild AI (YC W25) Is Hiring Interns to Make Housing Affordable

**原文链接**: [https://www.workatastartup.com/jobs/80596](https://www.workatastartup.com/jobs/80596)

生成摘要时出错

---

## 9. Anthropic 抛弃核心安全承诺

**原文标题**: Anthropic ditches its core safety promise

**原文链接**: [https://www.cnn.com/2026/02/25/tech/anthropic-safety-policy-change](https://www.cnn.com/2026/02/25/tech/anthropic-safety-policy-change)

Anthropic, an AI company founded on the principle of safety-first development, has replaced its rigid “Responsible Scaling Policy” with a more flexible “Frontier Safety Roadmap.” This shift moves the company away from "hard commitments"—such as the promise to pause training if models become uncontrollable—toward nonbinding "public goals" that can be adjusted as the market evolves.

The company cited several reasons for this pivot:
*   **Industry Competition:** Anthropic noted that its hope for a "race to the top" regarding safety standards did not materialize. Chief Science Officer Jared Kaplan argued that unilateral pauses are counterproductive if less-cautious competitors continue to advance.
*   **Political Climate:** The company acknowledged that its previous stance was out of sync with Washington’s current anti-regulatory environment.
*   **Transparency:** Anthropic maintains the new policy is actually stronger because it commits to regular, detailed public reports on threat models and risk mitigation.

The policy change arrives amid a high-stakes conflict with the U.S. government. Defense Secretary Pete Hegseth recently issued an ultimatum to CEO Dario Amodei: roll back specific AI safeguards or face a $200 million contract loss and a government blacklist via the Defense Production Act. Anthropic is reportedly resisting demands to allow its AI to be used for autonomous weaponry and mass domestic surveillance. 

While Anthropic claims the policy update is unrelated to the Pentagon dispute, the timing highlights the immense pressure on the company to balance its "safety soul" with the demands of national security and a hyper-competitive AI market.

---

## 10. BuildKit: Docker's Hidden Gem That Can Build Almost Anything

**原文标题**: BuildKit: Docker's Hidden Gem That Can Build Almost Anything

**原文链接**: [https://tuananh.net/2026/02/25/buildkit-docker-hidden-gem/](https://tuananh.net/2026/02/25/buildkit-docker-hidden-gem/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 2 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 3 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 4 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 5 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 6 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 7 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 8 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 9 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 10 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 11 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 12 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 13 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 14 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 15 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 16 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 17 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 18 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 19 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 20 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 21 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 22 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 23 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 24 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 25 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 26 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 27 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 28 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 29 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 30 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 31 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 32 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 33 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 34 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 35 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 36 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 37 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 38 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 39 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 40 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 41 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 42 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 43 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 44 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 45 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 46 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 47 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 48 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 49 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 50 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 51 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 52 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 53 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 54 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 55 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 56 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 57 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 58 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 59 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 60 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 61 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 62 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 63 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 64 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 65 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 66 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 67 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 68 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 69 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 70 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 71 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 72 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 73 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 74 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 75 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 76 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 77 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 78 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 79 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 80 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 81 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 82 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 83 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 84 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 85 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 86 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 87 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 88 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 89 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 90 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 91 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 92 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 93 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 94 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 95 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 96 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 97 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 98 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 99 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 100 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 101 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 102 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 103 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 104 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 105 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 106 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 107 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 108 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 109 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 110 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 111 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 112 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 113 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 114 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 115 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 116 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 117 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 118 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 119 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 120 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 121 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 122 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 123 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 124 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 125 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 126 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 127 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 128 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 129 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 130 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 131 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 132 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 133 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 134 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 135 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 136 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 137 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 138 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 139 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 140 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 141 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 142 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 143 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 144 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 145 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 146 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 147 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 148 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 149 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 150 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 151 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 152 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 153 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 154 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 155 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 156 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 157 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 158 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 159 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 160 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 161 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 162 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 163 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 164 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 165 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 166 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 167 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 168 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 169 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 170 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 171 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 172 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 173 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 174 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 175 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 176 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 177 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 178 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 179 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 180 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 181 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 182 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 183 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 184 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 185 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 186 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 187 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 188 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 189 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 190 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 191 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 192 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 193 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 194 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 195 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 196 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 197 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 198 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 199 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 200 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 201 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 202 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 203 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 204 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 205 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 206 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 207 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 208 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 209 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 210 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 211 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 212 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 213 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 214 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 215 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 216 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 217 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 218 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 219 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 220 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 221 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 222 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 223 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 224 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 225 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 226 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 227 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 228 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 229 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 230 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 231 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 232 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 233 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 234 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 235 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 236 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 237 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 238 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 239 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 240 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 241 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 242 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 243 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 244 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 245 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 246 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 247 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 248 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 249 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 250 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 251 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 252 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 253 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 254 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 255 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 256 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 257 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 258 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 259 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 260 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 261 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 262 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 263 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 264 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 265 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 266 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 267 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 268 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 269 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 270 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 271 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 272 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 273 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 274 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 275 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 276 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 277 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 278 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 279 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 280 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 281 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 282 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 283 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 284 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 285 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 286 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 287 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 288 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 289 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 290 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 291 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 292 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 293 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 294 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 295 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 296 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 297 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 298 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 299 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 300 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 301 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 302 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 303 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 304 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 305 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 306 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 307 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 308 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 309 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 310 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 311 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 312 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 313 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 314 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 315 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 316 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 317 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 318 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 319 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 320 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 321 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 322 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 323 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 324 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 325 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 326 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 327 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 328 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 329 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 330 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 331 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 332 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 333 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 334 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 335 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 336 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 337 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 338 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 339 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 340 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 341 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 342 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 343 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
