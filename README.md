# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-03.md)

*最后自动更新时间: 2026-11-03 22:36:59*
## 1. Safari 27.3 引入自适应深色模式

**原文标题**: Safari introduces Adaptive Dark Mode in 27.3

**原文链接**: [https://webkit.org/blog/18541/introducing-adaptive-dark-mode/](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

Safari 27.3 beta 引入了“自适应深色模式”（Adaptive Dark Mode），该功能旨在通过自动转换尚不支持原生深色模式的浅色网站，来提供一致的浏览体验。虽然有 40% 的网页用户偏好深色模式，但目前仅有 10% 的网站支持该模式；本次更新旨在缩小这一差距。

系统会智能分析页面的配色方案。如果网站以浅色为主，Safari 会应用颜色矩阵，在保留色调的同时反转亮度，确保文本符合 WCAG 4.5:1 的对比度标准。为保持视觉完整性，大多数图像保持不变，但渲染引擎会专门处理 SVG 和简单的位图 Logo，以确保它们在深色背景下依然清晰可见。`<canvas>` 元素和复杂的 CSS 效果（如 `mix-blend-mode`）通常不参与转换，以避免渲染错误。

**开发者关键信息：**
*   **兼容性：** 如果网站已通过 `<meta name="color-scheme" content="light dark">` 或 CSS 声明支持深色模式，自适应深色模式将不会对页面进行修改。
*   **退出机制：** 开发者可以通过在 `color-scheme` 属性中使用 `light only` 值来禁止自动转换。
*   **隐私保护：** 为防止浏览器指纹追踪，Safari 确保网站无法检测到自适应深色模式是否处于开启状态。JavaScript 对 CSS 颜色的查询将返回原始编写的值，而非转换后的值。

Apple 鼓励开发者采用现代 Web 标准（如 SVG、CSS 变量和 `light-dark()` 函数），以便无论是通过 Safari 的自适应功能还是自定义深色模式，都能提供最佳的用户体验。

---

## 2. 生成式人工智能基础小书：直观数学入门

**原文标题**: The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer

**原文链接**: [https://arxiv.org/abs/2605.29713](https://arxiv.org/abs/2605.29713)

《生成式人工智能基础小册：直观的数学入门指南》由陈天华（Tianhua Chen）编写，是一本共195页的全面指南（arXiv:2605.29713），旨在弥合高层直觉与现代生成式人工智能严谨数学推导之间的鸿沟。

本书并非单纯对实现细节或特定的近期架构进行综述，而是提供了一种以推导为导向的叙述方式，将不同的生成模型系列联系起来。它探索了以下领域之间的基础联系：
*   **降维：** 主成分分析 (PCA) 和概率主成分分析 (Probabilistic PCA)。
*   **隐变量与精炼模型：** 变分自编码器 (VAE) 和扩散模型 (Diffusion models)。
*   **概率框架：** 归一化流 (Normalizing flows) 和自回归分解。
*   **对抗性与基于能量的方法：** 生成对抗网络 (GAN)、Wasserstein GAN 以及基于能量的模型 (EBM)。

本书的主要目标是让对数学感兴趣的研究人员、从业者和学生能够理解生成建模的复杂结构。通过关注这些模型的推导方式及其相互关系，本书起到了一种奠定基础的入门作用。修订后的第二版 (v2) 进一步通过视觉解释强化了这些概念，以辅助读者理解数学实质。

最终，本书在人工智能的理论版图中提供了一条连贯的路径，强调了驱动当前生成技术数学框架背后的“原因”。

---

## 3. Jailbreaking my car's navigation system just so I can change the time

**原文标题**: Jailbreaking my car's navigation system just so I can change the time

**原文链接**: [https://blog.nns.ee/2026/11/02/renault-hack/](https://blog.nns.ee/2026/11/02/renault-hack/)

生成摘要时出错

---

## 4. Stringman：售价800美元的开源房间级抓取机器人

**原文标题**: Stringman, an $800 open-source room scale gripper robot

**原文链接**: [https://neufangled.com/](https://neufangled.com/)

**Stringman** 是一款经济实惠的开源抓取机器人，专为房间级范围的作业而设计，造价约为 800 美元。

该系统专为大规模工作空间设计，需要牢固的安装才能有效运行。关键安装步骤包括将固定座安装在靠近天花板的结构支撑物上。根据环境的不同，可以使用木螺钉将其固定在墙体龙骨上，或使用棘轮带固定在柱子上。这种安装灵活性使机器人 coastal 能够在广阔的区域内运行，很可能是利用线驱机构来操控其夹爪。

---

## 5. 我笔记本上的 Qwen 3.8 27B 也能解读模型权重

**原文标题**: Qwen 3.8 27B on my laptop can interpret model weights, too

**原文链接**: [https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)

本文撰写于2026年11月，探讨了“权重空间编程”（Weight-Space Programming）的概念。这一术语出自一篇名为《权重空间编程的火花：大语言模型可原生读写神经网络权重》的论文。该研究揭示了如 GPT-6 Astra 等前沿模型能够解释、诊断甚至修改以浮点数表示的原始神经网络权重，从而在无需编写代码或运行训练循环的情况下，提升模型性能或识别其行为特征。

作者通过在笔记本电脑上本地运行 Qwen 3.8 27B，测试了这种能力是否仅限于顶尖模型。利用原论文中的提示词，作者向该模型输入了四个简单网格世界游戏（《打砖块》、《乒乓球》、《吃豆人》和《高速公路》）的原始权重。仅凭权重数据，Qwen 3.8 27B 成功识别出了其中三个游戏，尽管这一过程耗时较长（达一小时）且消耗了数万个推理 Token。

核心要点包括：
*   **权重空间编程：** 大语言模型正在进化到能够理解神经网络的“内部语言”，从而实现“无梯度”权重编辑。
*   **本地可访问性：** 解释权重的能力正从庞大的专有模型下沉到如 Qwen 3.8 27B 这样较小的开源权重模型中。
*   **质疑声：** 尽管结果令人印象深刻，但批评者认为该论文将原始推理与人类研究员可能采取的逻辑步骤混为一谈。作者总结道，虽然这是一个重要的里程碑，但它并不意味着传统源代码的终结，也不代表向难以理解的自编辑机器的转型。

---

## 6. Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels

**原文标题**: Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels

**原文链接**: [https://hackertv.org](https://hackertv.org)

**HackerTV** 是一个精选流媒体平台，它将 Hacker News 社区高度推荐的 YouTube 视频转化为一系列 24/7 全天候播出的线性电视频道。

该服务旨在模拟传统的广播体验，摒弃了传统的按需搜索，转而采用一种“后仰式”（lean-back）的探索模式。其核心功能包括：

*   **线性排播：** 视频被组织成持续运行的频道，允许用户在经过社区筛选的内容中随心所欲地“换台”。
*   **交互式界面：** 网站采用复古风格的 UI，用户必须“打开”电视才能开始观看。它支持多种导航快捷键，例如用于切换频道的方向键、调出节目指南的“G”键以及用于直接调台的数字键。
*   **动态排程：** 由于系统依赖 YouTube 元数据来估算视频长度，因此在节目之间偶尔会出现“请稍候”的待机画面，或出现轻微的时间偏差。
*   **观看选项：** 该平台包含字幕、剧院模式和全屏观看等标准播放功能，并提供直接跳转至 YouTube 观看原内容的链接。

总的来说，HackerTV 为技术爱好者提供了一种独特的方式，让他们能够以结构化的广播风格观看热门且具有教育意义的视频内容。

---

## 7. PostgreSQL 内部原理

**原文标题**: The Internals of PostgreSQL

**原文链接**: [https://www.interdb.jp/pg/index.html](https://www.interdb.jp/pg/index.html)

《PostgreSQL 内部原理》（The Internals of PostgreSQL）由铃木启修（Hironobu Suzuki）撰写，是一部旨在揭示 PostgreSQL 数据库复杂子系统的全面技术资源。该文档涵盖了截至 19-beta 的版本，深入剖析了进程架构、查询处理、并发控制、VACUUM 机制、缓冲区管理和复制等十二个核心领域。

2024 年至 2026 年的最新更新引入了重要内容，包括：
*   **逻辑复制**（Beta 版）及并行应用工作者（Parallel Apply Worker）模式。
*   **异步 I/O** 与高级缓冲区管理。
*   **增量备份**功能，包括 WAL 摘要生成器（WAL Summarizer）进程。
*   并行查询执行与基数估计的优化。

**关于作者：**
铃木启修是一位资深的软件工程师，曾任日本 PostgreSQL 用户组（JPUG）理事。他著有多部数据库系统相关的书籍，并开发了 `pg_plan_inspector` 等工具。目前，铃木正在寻求国际职业机会或专注于 PostgreSQL、机器学习和 AI 集成的远程职位。

**使用须知与政策：**
在注明原作者的前提下，本文档可免费用于教育及非商业用途。然而，作者对版权有严格限制：
*   **商业用途：** 需达成 20% 的收入分成协议，或以 5,000,000 欧元的价格买断全部内容。
*   **格式：** 内容针对 HTML 环境优化，暂无发布 PDF 或电子书版本的计划。
*   **联系方式：** 出于安全考量（如 XZ 后门事件），作者不接受匿名咨询。潜在合作者或招聘人员通过邮件联系时，须提供至少两个社交媒体账号（如 LinkedIn/X）以供身份验证。

---

## 8. Postman 静默自动安装 AI 插件并试图共享所有 API 数据

**原文标题**: Postman silently auto-installs AI plugins and attempts to share all API data

**原文链接**: [https://github.com/postmanlabs/postman-app-support/issues/14370](https://github.com/postmanlabs/postman-app-support/issues/14370)

**Postman 桌面应用程序爆出严重安全与隐私事故**

据报道，Postman 桌面应用程序（v12.33.4）发生了一起严重的安全与隐私事故。根据 2026 年 10 月下旬提交的一份详细 GitHub Issue，Postman 被指控在未经用户同意的情况下，自动安装了 Codex 和 Claude 等工具的 AI 插件，其行为实际上类似于恶意软件。

**核心指控包括：**
*   **未经授权的安装：** Postman 的更新脚本静默安装了 Codex、Claude 插件以及 Postman CLI。
*   **配置劫持：** 安装程序修改了无关编码代理的全局配置文件，以注册“启动钩子（startup hooks）”。这些钩子强制 AI 代理在默认情况下通过 Postman 处理广泛的 API 工程任务，即便用户并未发出此类请求。
*   **绕过安全边界：** 证据表明，安装程序试图通过直接将信任哈希写入配置文件来“自行批准”这些钩子，从而绕过了宿主环境通常要求的手动审批流程。
*   **远程连接：** 此次更新在未经用户明确选择加入的情况下，启用了指向 Postman 服务器的远程模型上下文协议（MCP）连接。

**社区反应：**
开发者社区对此表示强烈愤慨，称其为“严重的信任边界问题”。有用户记录并证实了 Postman 在事后试图修改网站文档以推卸责任的行为，而这一举动已被 Wayback Machine 曝光。

该事件已引发了呼吁立即迁移至 **Bruno** 或 **Insomnia** 等开源替代方案的声音。报告者要求 Postman 停止自动安装行为，移除钩子的自动审批机制，并为受影响用户提供清晰的回滚路径。目前，Postman 尚未在问题追踪器上给出正式的解决方案。

---

## 9. macOS 27 does not support CoreStorage volumes

**原文标题**: macOS 27 does not support CoreStorage volumes

**原文链接**: [https://wadetregaskis.com/macos-27-golden-gate-does-not-actually-support-corestorage-or-hfs-volumes/](https://wadetregaskis.com/macos-27-golden-gate-does-not-actually-support-corestorage-or-hfs-volumes/)

生成摘要时出错

---

## 10. Show HN: Kairos – Open-source risk and fraud decisioning platform

**原文标题**: Show HN: Kairos – Open-source risk and fraud decisioning platform

**原文链接**: [https://github.com/finic-ai/kairos](https://github.com/finic-ai/kairos)

Kairos is an open-source, real-time risk and fraud decisioning platform designed to evaluate transactions, sign-ups, and logins as they occur. Positioned as a developer-centric alternative to services like Sift and Sardine, it provides automated decisions (approve, review, or block) accompanied by risk scores and transparent reasoning.

The platform distinguishes itself through two primary features:

1.  **Agent-First Architecture:** Kairos integrates with AI coding agents (such as Claude Code, Cursor, or Codex) via the Model Context Protocol (MCP). This allows an AI agent to perform the role of a fraud engineer—proposing model variants, running experiments on historical data, and deploying optimized workflows autonomously.
2.  **Grayson Decision Model:** Unlike traditional ML that requires thousands of labels, Kairos utilizes "Grayson," a model that understands unstructured data (names, addresses, notes) and provides calibrated probabilities in plain language. This allows the system to be effective from day one, even before significant fraud data is collected.

Technically, Kairos supports complex workflows, manual review queues, and the combination of AI reasoning with traditional machine learning models like XGBoost and logistic regression. It offers robust developer tools, including TypeScript and Python SDKs, a CLI, and an HTTP API.

Users can choose between **Kairos Cloud** for immediate deployment or **self-hosting** via Docker. The project is licensed under Apache 2.0, emphasizing transparency and local control over sensitive financial and user data. By automating the tuning process through AI agents, Kairos aims to reduce the manual overhead typically associated with maintaining high-performance fraud detection systems.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 2 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 3 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 4 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 5 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 6 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 7 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 8 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 9 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 10 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 11 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 12 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 13 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 14 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 15 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 16 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 17 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 18 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 19 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 20 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 21 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 22 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 23 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 24 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 25 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 26 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 27 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 28 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 29 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 30 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 31 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 32 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 33 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 34 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 35 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 36 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 37 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 38 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 39 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 40 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 41 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 42 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 43 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 44 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 45 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 46 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 47 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 48 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 49 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 50 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 51 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 52 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 53 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 54 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 55 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 56 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 57 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 58 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 59 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 60 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 61 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 62 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 65 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 66 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 67 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 68 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 69 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 70 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 71 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 72 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 73 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 74 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 75 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 76 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 77 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 78 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 79 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 80 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 81 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 82 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 83 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 84 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 85 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 86 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 87 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 88 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 89 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 90 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 91 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 92 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 93 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 94 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 95 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 96 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 97 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 98 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 99 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 100 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 101 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 102 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 103 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 104 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 105 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 106 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 107 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 108 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 109 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 110 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 111 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 112 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 113 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 114 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 115 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 116 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 117 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 118 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 119 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 120 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 121 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 122 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 123 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 124 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 125 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 126 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 127 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 128 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 129 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 130 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 131 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 132 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 133 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 134 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 135 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 136 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 137 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 138 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 139 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 140 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 141 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 142 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 143 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 144 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 145 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 146 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 147 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 148 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 149 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 150 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 151 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 152 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 153 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 154 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 155 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 156 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 157 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 158 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 159 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 160 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 161 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 162 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 163 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 164 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 165 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 166 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 167 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 168 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 169 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 170 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 171 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 172 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 173 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 174 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 175 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 176 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 177 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 178 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 179 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 180 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 181 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 182 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 183 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 184 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 185 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 186 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 187 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 188 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 189 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 190 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 191 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 192 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 193 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 194 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 195 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 196 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 197 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 198 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 199 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 200 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 201 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 202 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 203 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 204 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 205 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 206 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 207 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 208 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 209 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 210 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 211 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 212 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 213 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 214 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 215 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 216 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 217 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 218 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 219 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 220 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 221 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 222 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 223 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 224 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 225 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 226 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 227 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 228 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 229 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 230 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 231 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 232 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 233 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 234 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 235 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 236 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 237 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 238 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 239 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 240 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 241 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 242 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 243 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 244 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 245 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 246 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 247 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 248 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 249 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 250 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 251 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 252 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 253 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 254 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 255 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 256 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 257 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 258 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 259 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 260 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 261 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 262 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 263 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 264 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 265 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 266 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 267 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 268 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 269 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 270 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 271 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 272 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 273 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 274 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 275 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 276 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 277 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 278 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 279 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 280 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 281 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 282 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 283 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 284 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 285 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 286 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 287 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 288 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 289 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 290 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 291 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 292 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 293 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 294 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 295 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 296 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 297 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 298 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 299 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 300 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 301 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 302 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 303 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 304 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 305 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 306 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 307 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 308 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 309 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 310 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 311 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 312 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 313 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 314 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 315 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 316 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 317 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 318 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 319 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 320 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 321 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 322 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 323 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 324 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 325 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 326 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 327 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 328 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 329 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 330 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 331 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 332 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 333 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 334 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 335 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 336 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 337 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 338 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 339 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 340 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 341 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 342 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 343 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 344 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 345 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 346 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 347 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 348 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 349 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 350 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 351 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 352 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 353 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 354 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 355 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 356 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 357 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 358 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 359 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 360 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 361 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 362 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 363 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 364 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 365 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 366 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 367 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 368 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 369 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 370 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 371 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 372 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 373 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 374 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 375 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 376 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 377 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 378 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 379 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 380 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 381 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 382 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 383 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 384 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 385 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 386 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 387 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 388 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 389 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 390 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 391 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 392 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 393 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 394 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 395 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 396 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 397 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 398 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 399 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 400 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 401 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 402 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 403 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 404 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 405 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 406 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 407 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 408 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 409 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 410 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 411 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 412 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 413 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 414 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 415 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 416 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 417 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 418 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 419 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 420 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 421 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 422 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 423 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 424 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 425 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 426 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 427 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 428 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 429 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 430 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 431 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 432 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 433 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 434 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 435 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 436 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 437 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 438 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 439 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 440 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 441 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 442 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 443 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 444 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 445 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 446 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 447 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 448 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 449 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 450 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 451 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 452 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 453 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 454 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 455 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 456 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 457 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 458 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 459 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 460 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 461 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 462 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 463 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 464 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 465 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 466 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 467 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 468 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 469 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 470 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 471 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 472 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 473 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 474 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 475 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 476 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 477 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 478 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 479 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 480 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 481 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 482 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 483 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 484 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 485 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 486 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 487 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 488 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 489 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 490 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 491 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 492 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 493 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 494 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 495 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 496 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 497 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 498 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 499 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 500 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 501 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 502 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 503 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 504 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 505 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 506 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 507 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 508 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 509 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 510 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 511 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 512 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 513 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 514 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 515 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 516 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 517 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 518 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 519 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 520 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 521 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 522 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 523 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 524 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 525 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 526 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 527 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 528 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 529 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 530 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 531 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 532 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 533 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 534 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 535 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 536 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 537 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 538 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 539 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 540 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 541 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 542 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 543 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 544 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 545 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 546 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 547 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 548 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 549 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 550 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 551 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 552 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 553 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 554 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 555 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 556 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 557 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 558 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 559 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 560 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 561 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 562 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 563 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 564 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 565 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 566 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 567 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 568 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 569 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 570 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 571 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 572 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 573 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 574 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 575 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 576 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 577 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 578 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 579 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 580 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 581 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 582 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 583 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 584 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 585 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 586 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 587 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 588 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 589 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 590 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
