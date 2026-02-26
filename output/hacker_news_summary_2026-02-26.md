# Hacker News 热门文章摘要 (2026-02-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. just-bash: Bash for Agents

**原文标题**: just-bash: Bash for Agents

**原文链接**: [https://github.com/vercel-labs/just-bash](https://github.com/vercel-labs/just-bash)

生成摘要时出错

---

## 12. Will vibe coding end like the maker movement?

**原文标题**: Will vibe coding end like the maker movement?

**原文链接**: [https://read.technically.dev/p/vibe-coding-and-the-maker-movement](https://read.technically.dev/p/vibe-coding-and-the-maker-movement)

生成摘要时出错

---

## 13. 硬件升级，跳过一年会更好吗？

**原文标题**: Better to Skip a Year for Hardware Upgrades?

**原文链接**: [https://boilingsteam.com/poll-better-to-skip-a-year-for-pc-upgrades/](https://boilingsteam.com/poll-better-to-skip-a-year-for-pc-upgrades/)

生成摘要时出错

---

## 14. Show HN: Hacker Smacker – spot great (and terrible) HN commenters at a glance

**原文标题**: Show HN: Hacker Smacker – spot great (and terrible) HN commenters at a glance

**原文链接**: [https://hackersmacker.org](https://hackersmacker.org)

生成摘要时出错

---

## 15. Jimi Hendrix was a systems engineer

**原文标题**: Jimi Hendrix was a systems engineer

**原文链接**: [https://spectrum.ieee.org/jimi-hendrix-systems-engineer](https://spectrum.ieee.org/jimi-hendrix-systems-engineer)

生成摘要时出错

---

## 16. Banned in California

**原文标题**: Banned in California

**原文链接**: [https://www.bannedincalifornia.org/](https://www.bannedincalifornia.org/)

生成摘要时出错

---

## 17. Those who can, teach history

**原文标题**: Those who can, teach history

**原文链接**: [https://www.historytoday.com/archive/making-history/those-who-can-teach-history](https://www.historytoday.com/archive/making-history/those-who-can-teach-history)

生成摘要时出错

---

## 18. How will OpenAI compete?

**原文标题**: How will OpenAI compete?

**原文链接**: [https://www.ben-evans.com/benedictevans/2026/2/19/how-will-openai-compete-nkg2x](https://www.ben-evans.com/benedictevans/2026/2/19/how-will-openai-compete-nkg2x)

生成摘要时出错

---

## 19. The Pentagon Feuding with an AI Company Is a Bad Sign

**原文标题**: The Pentagon Feuding with an AI Company Is a Bad Sign

**原文链接**: [https://foreignpolicy.com/2026/02/25/anthropic-pentagon-feud-ai/](https://foreignpolicy.com/2026/02/25/anthropic-pentagon-feud-ai/)

生成摘要时出错

---

## 20. Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents

**原文标题**: Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents

**原文链接**: [https://machinelearning.apple.com/research/ferret-ui](https://machinelearning.apple.com/research/ferret-ui)

生成摘要时出错

---

## 21. First Website (1992)

**原文标题**: First Website (1992)

**原文链接**: [https://info.cern.ch](https://info.cern.ch)

生成摘要时出错

---

## 22. A 26-Gram Butterfly-Inspired Robot Achieving Autonomous Tailless Flight

**原文标题**: A 26-Gram Butterfly-Inspired Robot Achieving Autonomous Tailless Flight

**原文链接**: [https://arxiv.org/abs/2602.06811](https://arxiv.org/abs/2602.06811)

生成摘要时出错

---

## 23. Windows 11 Notepad to support Markdown

**原文标题**: Windows 11 Notepad to support Markdown

**原文链接**: [https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/](https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/)

生成摘要时出错

---

## 24. Story of XZ Backdoor [video]

**原文标题**: Story of XZ Backdoor [video]

**原文链接**: [https://www.youtube.com/watch?v=aoag03mSuXQ](https://www.youtube.com/watch?v=aoag03mSuXQ)

生成摘要时出错

---

## 25. Making MCP cheaper via CLI

**原文标题**: Making MCP cheaper via CLI

**原文链接**: [https://kanyilmaz.me/2026/02/23/cli-vs-mcp.html](https://kanyilmaz.me/2026/02/23/cli-vs-mcp.html)

生成摘要时出错

---

## 26. Some silly Z3 scripts I wrote

**原文标题**: Some silly Z3 scripts I wrote

**原文链接**: [https://www.hillelwayne.com/post/z3-examples/](https://www.hillelwayne.com/post/z3-examples/)

生成摘要时出错

---

## 27. Artist who “paints” portraits on glass by hitting it with a hammer

**原文标题**: Artist who “paints” portraits on glass by hitting it with a hammer

**原文链接**: [https://simonbergerart.com](https://simonbergerart.com)

生成摘要时出错

---

## 28. Time Is Different

**原文标题**: Time Is Different

**原文链接**: [https://shkspr.mobi/blog/2026/02/this-time-is-different/](https://shkspr.mobi/blog/2026/02/this-time-is-different/)

生成摘要时出错

---

## 29. Bus stop balancing is fast, cheap, and effective

**原文标题**: Bus stop balancing is fast, cheap, and effective

**原文链接**: [https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/](https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/)

生成摘要时出错

---

## 30. Writers and Their Day Jobs

**原文标题**: Writers and Their Day Jobs

**原文链接**: [https://lithub.com/the-work-behind-the-writing-on-writers-and-their-day-jobs/](https://lithub.com/the-work-behind-the-writing-on-writers-and-their-day-jobs/)

生成摘要时出错

---

## 31. Large-Scale Online Deanonymization with LLMs

**原文标题**: Large-Scale Online Deanonymization with LLMs

**原文链接**: [https://simonlermen.substack.com/p/large-scale-online-deanonymization](https://simonlermen.substack.com/p/large-scale-online-deanonymization)

生成摘要时出错

---

## 32. Child-free 'Disney adults' are transforming the company's theme parks

**原文标题**: Child-free 'Disney adults' are transforming the company's theme parks

**原文链接**: [https://www.businessinsider.com/why-disney-parks-top-destinations-millennials-gen-z-2023-9](https://www.businessinsider.com/why-disney-parks-top-destinations-millennials-gen-z-2023-9)

生成摘要时出错

---

## 33. Show HN: Modern Reimplementation of the Speck Molecule Renderer

**原文标题**: Show HN: Modern Reimplementation of the Speck Molecule Renderer

**原文链接**: [https://github.com/vangelov/modern-speck](https://github.com/vangelov/modern-speck)

生成摘要时出错

---

## 34. Fentanyl makeover: Core structural redesign could lead to safer pain medications

**原文标题**: Fentanyl makeover: Core structural redesign could lead to safer pain medications

**原文链接**: [https://www.scripps.edu/news-and-events/press-room/2026/20260211-janda-molecule.html](https://www.scripps.edu/news-and-events/press-room/2026/20260211-janda-molecule.html)

生成摘要时出错

---

## 35. Show HN: Respectify – A comment moderator that teaches people to argue better

**原文标题**: Show HN: Respectify – A comment moderator that teaches people to argue better

**原文链接**: [https://respectify.org/](https://respectify.org/)

生成摘要时出错

---

## 36. America Chose Not to Hold the Powerful to Account

**原文标题**: America Chose Not to Hold the Powerful to Account

**原文链接**: [https://www.theatlantic.com/ideas/2026/02/elite-accountability-powerful-impunity/686134/](https://www.theatlantic.com/ideas/2026/02/elite-accountability-powerful-impunity/686134/)

生成摘要时出错

---

## 37. The First Fully General Computer Action Model

**原文标题**: The First Fully General Computer Action Model

**原文链接**: [https://si.inc/posts/fdm1/](https://si.inc/posts/fdm1/)

生成摘要时出错

---

## 38. Tech companies shouldn't be bullied into doing surveillance

**原文标题**: Tech companies shouldn't be bullied into doing surveillance

**原文链接**: [https://www.eff.org/deeplinks/2026/02/tech-companies-shouldnt-be-bullied-doing-surveillance](https://www.eff.org/deeplinks/2026/02/tech-companies-shouldnt-be-bullied-doing-surveillance)

生成摘要时出错

---

## 39. An autopsy of AI-generated 3D slop

**原文标题**: An autopsy of AI-generated 3D slop

**原文链接**: [https://aircada.com/blog/ai-vs-human-3d-ecommerce](https://aircada.com/blog/ai-vs-human-3d-ecommerce)

生成摘要时出错

---

## 40. The Om Programming Language

**原文标题**: The Om Programming Language

**原文链接**: [https://www.om-language.com/](https://www.om-language.com/)

生成摘要时出错

---

## 41. GNU Texmacs

**原文标题**: GNU Texmacs

**原文链接**: [https://www.texmacs.org/tmweb/home/welcome.en.html](https://www.texmacs.org/tmweb/home/welcome.en.html)

生成摘要时出错

---

## 42. Dissecting the CPU-memory relationship in garbage collection (OpenJDK 26)

**原文标题**: Dissecting the CPU-memory relationship in garbage collection (OpenJDK 26)

**原文链接**: [https://norlinder.nu/posts/GC-Cost-CPU-vs-Memory/](https://norlinder.nu/posts/GC-Cost-CPU-vs-Memory/)

生成摘要时出错

---

## 43. RAM now represents 35 percent of bill of materials for HP PCs

**原文标题**: RAM now represents 35 percent of bill of materials for HP PCs

**原文链接**: [https://arstechnica.com/gadgets/2026/02/ram-now-represents-35-percent-of-bill-of-materials-for-hp-pcs/](https://arstechnica.com/gadgets/2026/02/ram-now-represents-35-percent-of-bill-of-materials-for-hp-pcs/)

生成摘要时出错

---

## 44. Out of Light Adjust Share: Caravaggio, La Tour, and the Art of Attention

**原文标题**: Out of Light Adjust Share: Caravaggio, La Tour, and the Art of Attention

**原文链接**: [https://harpers.org/archive/2026/03/out-of-light-nicole-krauss-caravaggio-georges-de-la-tour/](https://harpers.org/archive/2026/03/out-of-light-nicole-krauss-caravaggio-georges-de-la-tour/)

生成摘要时出错

---

## 45. LM Link: Use local models on remote devices, powered by Tailscale

**原文标题**: LM Link: Use local models on remote devices, powered by Tailscale

**原文链接**: [https://tailscale.com/blog/lm-link-remote-llm-access](https://tailscale.com/blog/lm-link-remote-llm-access)

生成摘要时出错

---

## 46. Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文标题**: Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文链接**: [https://app.teamout.com/ai](https://app.teamout.com/ai)

生成摘要时出错

---

## 47. Show HN: Agent Swarm – Multi-agent self-learning teams (OSS)

**原文标题**: Show HN: Agent Swarm – Multi-agent self-learning teams (OSS)

**原文链接**: [https://github.com/desplega-ai/agent-swarm](https://github.com/desplega-ai/agent-swarm)

生成摘要时出错

---

## 48. Why Developers Keep Choosing Claude over Every Other AI

**原文标题**: Why Developers Keep Choosing Claude over Every Other AI

**原文链接**: [https://www.bhusalmanish.com.np/blog/posts/why-claude-wins-coding.html](https://www.bhusalmanish.com.np/blog/posts/why-claude-wins-coding.html)

生成摘要时出错

---

## 49. Learnings from 4 months of Image-Video VAE experiments

**原文标题**: Learnings from 4 months of Image-Video VAE experiments

**原文链接**: [https://www.linum.ai/field-notes/vae-reconstruction-vs-generation](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)

生成摘要时出错

---

## 50. I pitched a roller coaster to Disneyland at age 10 in 1978

**原文标题**: I pitched a roller coaster to Disneyland at age 10 in 1978

**原文链接**: [https://wordglyph.xyz/one-piece-at-a-time](https://wordglyph.xyz/one-piece-at-a-time)

生成摘要时出错

---

## 51. Never buy a .online domain

**原文标题**: Never buy a .online domain

**原文链接**: [https://www.0xsid.com/blog/online-tld-is-pain](https://www.0xsid.com/blog/online-tld-is-pain)

生成摘要时出错

---

## 52. LLM=True

**原文标题**: LLM=True

**原文链接**: [https://blog.codemine.be/posts/2026/20260222-be-quiet/](https://blog.codemine.be/posts/2026/20260222-be-quiet/)

生成摘要时出错

---

## 53. Danish government agency to ditch Microsoft software (2025)

**原文标题**: Danish government agency to ditch Microsoft software (2025)

**原文链接**: [https://therecord.media/denmark-digital-agency-microsoft-digital-independence](https://therecord.media/denmark-digital-agency-microsoft-digital-independence)

生成摘要时出错

---

## 54. RK3588 and RK3576 video decoders support merged in the upstream Linux Kernel

**原文标题**: RK3588 and RK3576 video decoders support merged in the upstream Linux Kernel

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/rk3588-and-rk3576-video-decoders-support-merged-in-the-upstream-linux-kernel.html](https://www.collabora.com/news-and-blog/news-and-events/rk3588-and-rk3576-video-decoders-support-merged-in-the-upstream-linux-kernel.html)

生成摘要时出错

---

## 55. Rule of Three (Computer Programming)

**原文标题**: Rule of Three (Computer Programming)

**原文链接**: [https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))

生成摘要时出错

---

## 56. What Pressure Does to an Athlete's Body

**原文标题**: What Pressure Does to an Athlete's Body

**原文链接**: [https://www.theatlantic.com/culture/2026/02/pressure-olympics-malinin-shiffrin/686097/](https://www.theatlantic.com/culture/2026/02/pressure-olympics-malinin-shiffrin/686097/)

生成摘要时出错

---

## 57. Gauss's Weekday Algorithm, Visualized

**原文标题**: Gauss's Weekday Algorithm, Visualized

**原文链接**: [https://lukasmetzner.github.io/blog/gauss-weekday.html](https://lukasmetzner.github.io/blog/gauss-weekday.html)

生成摘要时出错

---

## 58. Show HN: A real-time strategy game that AI agents can play

**原文标题**: Show HN: A real-time strategy game that AI agents can play

**原文链接**: [https://llmskirmish.com/](https://llmskirmish.com/)

生成摘要时出错

---

## 59. Why isn't LA repaving streets?

**原文标题**: Why isn't LA repaving streets?

**原文链接**: [https://lapublicpress.org/2026/02/why-isnt-la-repaving-streets/](https://lapublicpress.org/2026/02/why-isnt-la-repaving-streets/)

生成摘要时出错

---

## 60. 100M-Row Challenge with PHP

**原文标题**: 100M-Row Challenge with PHP

**原文链接**: [https://github.com/tempestphp/100-million-row-challenge](https://github.com/tempestphp/100-million-row-challenge)

生成摘要时出错

---

## 61. PA bench: Evaluating web agents on real world personal assistant workflows

**原文标题**: PA bench: Evaluating web agents on real world personal assistant workflows

**原文链接**: [https://vibrantlabs.com/blog/pa-bench](https://vibrantlabs.com/blog/pa-bench)

生成摘要时出错

---

## 62. Text-Based Google Directions

**原文标题**: Text-Based Google Directions

**原文链接**: [https://gdir.telae.net/](https://gdir.telae.net/)

生成摘要时出错

---

## 63. I asked Claude for 37,500 random names, and it can't stop saying Marcus

**原文标题**: I asked Claude for 37,500 random names, and it can't stop saying Marcus

**原文链接**: [https://github.com/benjismith/ai-randomness](https://github.com/benjismith/ai-randomness)

生成摘要时出错

---

## 64. New accounts on HN more likely to use em-dashes

**原文标题**: New accounts on HN more likely to use em-dashes

**原文链接**: [https://www.marginalia.nu/weird-ai-crap/hn/](https://www.marginalia.nu/weird-ai-crap/hn/)

生成摘要时出错

---

## 65. Access to a Shared Unix Computer

**原文标题**: Access to a Shared Unix Computer

**原文链接**: [http://tilde.club/](http://tilde.club/)

生成摘要时出错

---

## 66. Show HN: I ported Tree-sitter to Go

**原文标题**: Show HN: I ported Tree-sitter to Go

**原文链接**: [https://github.com/odvcencio/gotreesitter](https://github.com/odvcencio/gotreesitter)

生成摘要时出错

---

## 67. The Misuses of the University

**原文标题**: The Misuses of the University

**原文链接**: [https://www.publicbooks.org/the-misuses-of-the-university/](https://www.publicbooks.org/the-misuses-of-the-university/)

生成摘要时出错

---

## 68. The Government Just Made It Harder to See What Spy Tech It Buys

**原文标题**: The Government Just Made It Harder to See What Spy Tech It Buys

**原文链接**: [https://www.404media.co/the-government-just-made-it-harder-to-see-what-spy-tech-it-buys/](https://www.404media.co/the-government-just-made-it-harder-to-see-what-spy-tech-it-buys/)

生成摘要时出错

---

## 69. US orders diplomats to fight data sovereignty initiatives

**原文标题**: US orders diplomats to fight data sovereignty initiatives

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/us-orders-diplomats-fight-data-sovereignty-initiatives-2026-02-25/](https://www.reuters.com/sustainability/boards-policy-regulation/us-orders-diplomats-fight-data-sovereignty-initiatives-2026-02-25/)

生成摘要时出错

---

## 70. Show HN: Clocksimulator.com – A minimalist, distraction-free analog clock

**原文标题**: Show HN: Clocksimulator.com – A minimalist, distraction-free analog clock

**原文链接**: [https://www.clocksimulator.com/](https://www.clocksimulator.com/)

生成摘要时出错

---

## 71. You Want to Visit the UK? You Better Have a Google Play or App Store Account

**原文标题**: You Want to Visit the UK? You Better Have a Google Play or App Store Account

**原文链接**: [https://www.heltweg.org/posts/you-want-to-visit-the-uk-you-better-have-a-google-play-or-app-store-account/](https://www.heltweg.org/posts/you-want-to-visit-the-uk-you-better-have-a-google-play-or-app-store-account/)

生成摘要时出错

---

## 72. Is AI Making Us Dumb?

**原文标题**: Is AI Making Us Dumb?

**原文链接**: [https://profgmedia.substack.com/p/is-ai-making-us-dumb](https://profgmedia.substack.com/p/is-ai-making-us-dumb)

生成摘要时出错

---

## 73. AIs can't stop recommending nuclear strikes in war game simulations

**原文标题**: AIs can't stop recommending nuclear strikes in war game simulations

**原文链接**: [https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/](https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/)

生成摘要时出错

---

## 74. Show HN: Django Control Room – All Your Tools Inside the Django Admin

**原文标题**: Show HN: Django Control Room – All Your Tools Inside the Django Admin

**原文链接**: [https://github.com/yassi/dj-control-room](https://github.com/yassi/dj-control-room)

生成摘要时出错

---

## 75. Japanese Death Poems

**原文标题**: Japanese Death Poems

**原文链接**: [https://www.secretorum.life/p/japanese-death-poems-part-3](https://www.secretorum.life/p/japanese-death-poems-part-3)

生成摘要时出错

---

## 76. Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub

**原文标题**: Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub

**原文链接**: [https://github.com/Intrect-io/OpenSwarm](https://github.com/Intrect-io/OpenSwarm)

生成摘要时出错

---

## 77. Following 35% growth, solar has passed hydro on US grid

**原文标题**: Following 35% growth, solar has passed hydro on US grid

**原文链接**: [https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/](https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/)

生成摘要时出错

---

## 78. The Physics and Economics of Moving 44 Tonnes at 56mph

**原文标题**: The Physics and Economics of Moving 44 Tonnes at 56mph

**原文链接**: [https://www.mikeayles.com/blog/heavy-haulage-basics/](https://www.mikeayles.com/blog/heavy-haulage-basics/)

生成摘要时出错

---

## 79. Topological Naming Problem

**原文标题**: Topological Naming Problem

**原文链接**: [https://wiki.freecad.org/Topological_naming_problem](https://wiki.freecad.org/Topological_naming_problem)

生成摘要时出错

---

## 80. Half million 'Words with Spaces' missing from dictionaries

**原文标题**: Half million 'Words with Spaces' missing from dictionaries

**原文链接**: [https://www.linguabase.org/words-with-spaces.html](https://www.linguabase.org/words-with-spaces.html)

生成摘要时出错

---

## 81. PL/0

**原文标题**: PL/0

**原文链接**: [https://en.wikipedia.org/wiki/PL/0](https://en.wikipedia.org/wiki/PL/0)

生成摘要时出错

---

## 82. The Pleasures and Pains of Coffee (1830)

**原文标题**: The Pleasures and Pains of Coffee (1830)

**原文链接**: [https://quod.lib.umich.edu/m/mqrarchive/act2080.0035.002/10](https://quod.lib.umich.edu/m/mqrarchive/act2080.0035.002/10)

生成摘要时出错

---

## 83. Hetzner Prices increase 30-40%

**原文标题**: Hetzner Prices increase 30-40%

**原文链接**: [https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/)

生成摘要时出错

---

## 84. Number of UK workers on zero-hours contracts hits record high ahead of crackdown

**原文标题**: Number of UK workers on zero-hours contracts hits record high ahead of crackdown

**原文链接**: [https://www.bbc.co.uk/news/articles/czj1m7d4gxpo](https://www.bbc.co.uk/news/articles/czj1m7d4gxpo)

生成摘要时出错

---

## 85. Stripe valued at $159B, 2025 annual letter

**原文标题**: Stripe valued at $159B, 2025 annual letter

**原文链接**: [https://stripe.com/newsroom/news/stripe-2025-update](https://stripe.com/newsroom/news/stripe-2025-update)

生成摘要时出错

---

## 86. How to fold the Blade Runner origami unicorn (1996)

**原文标题**: How to fold the Blade Runner origami unicorn (1996)

**原文链接**: [https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html](https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html)

生成摘要时出错

---

## 87. Claude Code Remote Control

**原文标题**: Claude Code Remote Control

**原文链接**: [https://code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control)

生成摘要时出错

---

## 88. Devirtualization and Static Polymorphism

**原文标题**: Devirtualization and Static Polymorphism

**原文链接**: [https://david.alvarezrosa.com/posts/devirtualization-and-static-polymorphism/](https://david.alvarezrosa.com/posts/devirtualization-and-static-polymorphism/)

生成摘要时出错

---

## 89. Quasi-Zenith Satellite System

**原文标题**: Quasi-Zenith Satellite System

**原文链接**: [https://en.wikipedia.org/wiki/Quasi-Zenith_Satellite_System](https://en.wikipedia.org/wiki/Quasi-Zenith_Satellite_System)

生成摘要时出错

---

## 90. Quasi-Zenith Satellite System

**原文标题**: Quasi-Zenith Satellite System

**原文链接**: [https://en.wikipedia.org/wiki/Quasi-Zenith_Satellite_System](https://en.wikipedia.org/wiki/Quasi-Zenith_Satellite_System)

生成摘要时出错

---

## 91. Amazon accused of widespread scheme to inflate prices across the economy

**原文标题**: Amazon accused of widespread scheme to inflate prices across the economy

**原文链接**: [https://www.thebignewsletter.com/p/amazon-busted-for-widespread-price](https://www.thebignewsletter.com/p/amazon-busted-for-widespread-price)

生成摘要时出错

---

## 92. Scipy.stats. Chatterjeexi

**原文标题**: Scipy.stats. Chatterjeexi

**原文链接**: [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chatterjeexi.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chatterjeexi.html)

生成摘要时出错

---

## 93. Turing Completeness of GNU find

**原文标题**: Turing Completeness of GNU find

**原文链接**: [https://arxiv.org/abs/2602.20762](https://arxiv.org/abs/2602.20762)

生成摘要时出错

---

## 94. The Tax Nerd Who Bet His Life Savings Against DOGE

**原文标题**: The Tax Nerd Who Bet His Life Savings Against DOGE

**原文链接**: [https://www.wsj.com/finance/investing/the-tax-nerd-who-bet-his-life-savings-against-doge-6b59eda2](https://www.wsj.com/finance/investing/the-tax-nerd-who-bet-his-life-savings-against-doge-6b59eda2)

生成摘要时出错

---

## 95. UPP: Universal Predicate Pushdown to Smart Storage

**原文标题**: UPP: Universal Predicate Pushdown to Smart Storage

**原文链接**: [https://dl.acm.org/doi/10.1145/3695053.3731005](https://dl.acm.org/doi/10.1145/3695053.3731005)

生成摘要时出错

---

## 96. Cl-kawa: Scheme on Java on Common Lisp

**原文标题**: Cl-kawa: Scheme on Java on Common Lisp

**原文链接**: [https://github.com/atgreen/cl-kawa](https://github.com/atgreen/cl-kawa)

生成摘要时出错

---

## 97. Pi – A minimal terminal coding harness

**原文标题**: Pi – A minimal terminal coding harness

**原文链接**: [https://pi.dev](https://pi.dev)

生成摘要时出错

---

## 98. Hubble could re-enter atmosphere as early as 2028

**原文标题**: Hubble could re-enter atmosphere as early as 2028

**原文链接**: [https://www.theregister.com/2026/02/25/hubble_orbit_decay/](https://www.theregister.com/2026/02/25/hubble_orbit_decay/)

生成摘要时出错

---

## 99. Why the KeePass format should be based on SQLite

**原文标题**: Why the KeePass format should be based on SQLite

**原文链接**: [https://mketab.org/blog/sqlite_kdbx/](https://mketab.org/blog/sqlite_kdbx/)

生成摘要时出错

---

## 100. Anthropic Drops Flagship Safety Pledge

**原文标题**: Anthropic Drops Flagship Safety Pledge

**原文链接**: [https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/)

生成摘要时出错

---

