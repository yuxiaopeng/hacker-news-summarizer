# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-05.md)

*最后自动更新时间: 2026-02-05 18:17:12*
## 1. Claude Opus 4.6

**原文标题**: Claude Opus 4.6

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6)

Anthropic 发布了其旗舰模型的重大升级版本 **Claude Opus 4.6**，专注于高级推理、代理式编程和长周期任务管理。该模型于 2026 年 2 月 5 日发布，旨在大型代码库和复杂的专业工作流程中更可靠地运行。

**关键技术特性：**
*   **100万 Token 上下文窗口：** Opus 级别模型首次支持 100 万 Token 的上下文窗口（测试版），显著提升了信息检索能力并减少了“上下文腐烂”现象。
*   **自适应思维与努力度控制：** 一项新功能允许模型根据任务复杂度自主扩展其推理深度。开发者还可以手动切换“努力程度”（从低到最高），以平衡延迟和智能。
*   **上下文压缩：** 该测试功能可对长对话中的陈旧上下文进行总结，防止模型在执行长期代理任务时触及 Token 限制。
*   **扩展输出：** 支持单次请求最高 128K Token 的输出。

**性能与基准测试：**
Opus 4.6 刷新了行业记录，在 GDPval-AA（一项针对经济类知识工作的评估）中，其 Elo 评分比 OpenAI 的 GPT-5.2 高出 144 分。它在“Humanity’s Last Exam”和“Terminal-Bench 2.0”基准测试中也处于领先地位。合作伙伴测试强调了其作为高级工程师的能力，能够在极少的人工干预下处理数百万行代码库的迁移以及复杂的法律和财务分析。

**安全性与可用性：**
尽管能力有所增强，Anthropic 仍保持着强大的安全性，行为偏差率较低。为了降低因编程能力提升而带来的风险，公司实施了新的网络安全探测。

Claude Opus 4.6 现已通过 Claude.ai 和 API 提供。标准定价维持在每百万输入 Token 5 美元、每百万输出 Token 25 美元，对于超过 200k Token 的提示词将收取溢价费用。

---

## 2. 与其租用云端，不如自主拥有

**原文标题**: Don't rent the cloud, own instead

**原文链接**: [https://blog.comma.ai/datacenter/](https://blog.comma.ai/datacenter/)

comma.ai的CTO Harald Schäfer认为，企业——尤其是机器学习领域的企业——应当建立并拥有自己的数据中心，而非租用云算力。其核心动力在于成本效率、自主权以及工程文化。Schäfer估算，comma.ai在基础设施上投入了约500万美元，而相比之下，同等规模的云端成本预计高达2500万美元。此外，拥有硬件能促使工程师针对现有资源优化代码，而不是单纯通过增加预算来解决低效问题。

**基础设施与硬件**
comma的数据中心位于圣迭戈，功耗约为450kW。为了节能，他们放弃了传统的机房空调（CRAC）系统，转而采用一套由进/排气风扇和PID回路组成的定制化室外空气系统。其硬件包括：
*   **计算：** 分布在75台自研“TinyBox Pro”机器中的600颗GPU。
*   **存储：** 基于Dell R630/R730服务器的4PB SSD存储。
*   **网络：** 具备Infiniband技术的100Gbps互连交换机，用于分布式训练。

**软件与工作流**
其软件栈的设计追求简洁，通常偏好单主（single-master）服务而非复杂的冗余设计。关键组件包括：
*   **任务管理：** 使用Slurm管理计算作业，PyTorch (FSDP) 处理分布式训练。
*   **minikeyvalue (mkv)：** 一种定制存储系统，支持以1TB/s的速度读取原始数据，从而消除了对缓存的需求。
*   **miniray：** 一个轻量级开源任务调度器，用于运行并行Python代码和模型推理。
*   **开发流程：** 通过NFS和`uv`同步的小型单体代码库（monorepo），使本地代码更改能在约两秒内部署到集群。

最后，Schäfer主张，这种“自建”模式让comma.ai能够完全掌控自己的“命运”，并能以市场成本的一小部分完成复杂的任务，例如训练同轨（on-policy）驾驶模型。

---

## 3. 全新 Collabora Office 桌面版

**原文标题**: The New Collabora Office for Desktop

**原文链接**: [https://www.collaboraonline.com/collabora-office/](https://www.collaboraonline.com/collabora-office/)

文章《The New Collabora Office for Desktop》概述了 Collabora 办公套件的战略演进，特别区分了现代化的 **Collabora Office** 与传统的 **Collabora Office Classic**。

**Collabora Office（新版本）**
“新版” Collabora Office（以 24.04 分支为代表）是当前的旗舰版本。它专为需要最新功能和性能增强的用户设计。主要亮点包括：
*   **增强的互操作性：** 与 Microsoft Office 格式（DOCX、XLSX、PPTX）具有卓越的兼容性。
*   **现代化的 UI：** 焕然一新的用户界面，包括对“NotebookBar”的重大更新，提供更直观的体验。
*   **性能提升：** 文档加载速度更快，复杂表格和演示文稿的渲染更流畅。
*   **创新：** 该版本会率先获得最新的办公工具和安全更新，是寻求替代专有软件的前沿开源方案的组织的理想选择。

**Collabora Office Classic**
“Classic”指较旧且高度稳定的版本（例如 21.06 分支）。该版本专为那些比起即时更新、更看重长期一致性和静态功能集的组织而维护。它为拥有特定工作流或与旧版本软件绑定的内部认证的企业提供了可靠的过渡。

**结论**
这两个版本的区分使 Collabora 能够满足两种截然不同的需求：“新”版本驱动创新和现代生产力，而“Classic”版本则为需要较慢更新周期的用户确保业务连续性。两个版本都拥有企业级支持、缺陷修复和安全补丁的保障，彰显了 Collabora 对专业开源桌面解决方案的承诺。

---

## 4. 欧盟委员会试用 Matrix 以取代 Teams

**原文标题**: European Commission Trials Matrix to Replace Teams

**原文链接**: [https://www.euractiv.com/news/commission-trials-european-open-source-communications-software/](https://www.euractiv.com/news/commission-trials-european-open-source-communications-software/)

欧盟委员会已启动一项试点项目，测试开源通信协议 Matrix，将其作为微软 Teams 等专有工具的潜在替代方案。该项目由信息化总司（DG DIGIT）管理，是增强欧盟数字主权并减少对美国主要科技供应商依赖的战略举措。

该试点项目被称为“EC-Matrix”，目前约有 450 名员工参与。与传统的中心化平台不同，Matrix 是一种去中心化、端到端加密的通信标准，支持不同服务商之间的安全通信和互操作性。通过采用开源解决方案，欧委会旨在确保更高的透明度，加强对其内部数据的控制，并避免“供应商锁定”。

这一转变符合欧盟更广泛的《开源软件战略》，该战略倡导在公共管理部门中使用可审计、可共享且可重用的软件。此举也是为了应对外界对美国云服务在欧盟数据保护法（GDPR）框架下的隐私和法律合规性的持续担忧。

虽然微软 Teams 目前仍是欧委会的主要工具，但 Matrix 试点的成功 lod 可能会推动其更大范围的普及。这一转型将标志着欧盟在构建更独立的欧洲数字基础设施方面迈出了重要一步，并可能鼓励欧洲大陆的其他公共机构采用具有主权属性的开源通信标准。

---

## 5. 公司即代码

**原文标题**: Company as Code

**原文链接**: [https://blog.42futures.com/p/company-as-code](https://blog.42futures.com/p/company-as-code)

在《公司即代码》（Company as Code）中，丹尼尔·罗斯曼（Daniel Rothmann）指出，尽管现代软件公司已经实现了基础架构和部署的自动化（基础架构即代码 IaC 和 GitOps），但其组织架构和政策仍停留在静态的“模拟”文档中。这种脱节导致了合规审计效率低下，且政策变更对组织产生的连锁反应缺乏透明度。

罗斯曼提议建立一个**“公司清单”（Company Manifest）**：对整个组织进行程序化、全局性的呈现。该模型将公司架构、角色和政策视为代码，具备以下特性：

*   **可查询：** 允许利益相关者追踪人员、系统与政策之间的关系。
*   **可版本化：** 使用版本控制系统（如 Git）跟踪组织变革的演进过程，并提供清晰的审计追踪。
*   **集成式：** 通过 API 连接到 Slack 或 GitHub 等工具，实现自动化的证据收集和政策执行。
*   **可测试：** 创建“预发布环境”，在正式实施前对组织变革进行建模。

从技术角度看，这将涉及一种类似于 Terraform 的**声明式领域特定语言 (DSL)**，其中角色、实体和合规要求被定义为相互关联的节点。由于组织结构比线性基础架构更为复杂，罗斯曼建议使用**无向有环图模型**来映射这些多维关系。

为了确保非技术领导者也能便捷使用，该系统需要一个**低代码界面**，允许通过拖拽方式进行组织设计，同时保持底层代码作为“单一真理源”。

尽管罗斯曼承认“公司即代码”的实际可行性仍在探索之中，但他总结道，构建该系统所需的技术——图数据库、DSL 和 API 优先架构——已经成熟。实施此类系统可以节省目前耗费在手动合规和文档编制上的数百小时，使技术领导者能够专注于创造价值。

---

## 6. 150 MB FreeBSD 最小化安装

**原文标题**: 150 MB Minimal FreeBSD Installation

**原文链接**: [https://vermaden.wordpress.com/2026/02/01/150-mb-minimal-freebsd-installation/](https://vermaden.wordpress.com/2026/02/01/150-mb-minimal-freebsd-installation/)

This article explores how to minimize the FreeBSD 15.0 disk footprint using **PKGBASE**, achieving a root installation of approximately **150 MB**. 

The process begins with a standard PKGBASE installation using ZFS with high-level compression (`zstd-19`), which initially occupies about 450 MB. To push this further, the author identifies the core dependencies required to keep the `pkg(8)` utility functional. These essential packages—including `FreeBSD-libarchive`, `FreeBSD-openssl-lib`, `FreeBSD-xz-lib`, `FreeBSD-libucl`, and `FreeBSD-libcasper`—are "locked" using the `pkg lock` command to prevent accidental removal.

Once the vital libraries are secured, the author removes non-essential sets, specifically `FreeBSD-set-devel` and `FreeBSD-set-optional`. While this successfully reduces the system size to 150 MB, a challenge arises: the package manager attempts to reinstall these sets during any future `pkg upgrade` because of hard-coded dependencies.

To resolve this, the author demonstrates a manual workaround involving the modification of the local package database. By using `pkg shell` to access the SQLite database at `/var/db/pkg/local.sqlite`, the author deletes the dependency records that link the removed sets to the base system. This "database hack" prevents the package manager from automatically triggering their reinstallation during upgrades.

The author concludes with a strong warning: this procedure is unsupported, potentially breaks the system, and should only be performed in test environments like a Bhyve VM. It serves as a technical proof-of-concept for how far FreeBSD's modularity can be pushed.

---

## 7. GB Renewables Map

**原文标题**: GB Renewables Map

**原文链接**: [https://renewables-map.robinhawkes.com/](https://renewables-map.robinhawkes.com/)

生成摘要时出错

---

## 8. Maihem (YC W24): hiring sr robotics perception engineer (London, on-site)

**原文标题**: Maihem (YC W24): hiring sr robotics perception engineer (London, on-site)

**原文链接**: [https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758](https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758)

生成摘要时出错

---

## 9. When internal hostnames are leaked to the clown

**原文标题**: When internal hostnames are leaked to the clown

**原文链接**: [https://rachelbythebay.com/w/2026/02/03/badnas/](https://rachelbythebay.com/w/2026/02/03/badnas/)

生成摘要时出错

---

## 10. Programming Patterns: The Story of the Jacquard Loom

**原文标题**: Programming Patterns: The Story of the Jacquard Loom

**原文链接**: [https://www.scienceandindustrymuseum.org.uk/objects-and-stories/jacquard-loom](https://www.scienceandindustrymuseum.org.uk/objects-and-stories/jacquard-loom)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 2 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 3 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 4 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 5 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 6 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 7 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 8 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 9 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 10 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 11 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 12 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 13 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 14 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 15 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 16 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 17 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 18 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 19 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 20 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 21 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 22 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 23 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 24 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 25 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 26 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 27 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 28 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 29 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 30 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 31 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 32 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 33 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 34 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 35 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 36 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 37 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 38 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 39 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 40 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 41 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 42 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 43 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 44 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 45 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 46 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 47 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 48 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 49 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 50 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 51 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 52 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 53 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 54 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 55 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 56 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 57 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 58 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 59 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 60 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 61 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 62 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 63 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 64 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 65 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 66 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 67 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 68 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 69 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 70 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 71 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 72 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 73 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 74 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 75 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 76 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 77 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 78 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 79 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 80 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 81 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 82 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 83 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 84 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 85 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 86 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 87 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 88 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 89 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 90 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 91 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 92 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 93 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 94 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 95 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 96 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 97 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 98 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 99 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 100 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 101 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 102 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 103 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 104 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 105 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 106 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 107 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 108 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 109 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 110 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 111 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 112 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 113 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 114 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 115 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 116 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 117 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 118 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 119 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 120 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 121 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 122 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 123 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 124 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 125 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 126 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 127 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 128 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 129 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 130 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 131 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 132 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 133 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 134 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 135 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 136 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 137 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 138 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 139 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 140 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 141 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 142 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 143 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 144 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 145 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 146 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 147 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 148 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 149 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 150 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 151 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 152 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 153 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 154 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 155 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 156 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 157 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 158 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 159 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 160 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 161 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 162 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 163 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 164 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 165 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 166 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 167 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 168 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 169 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 170 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 171 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 172 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 173 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 174 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 175 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 176 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 177 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 178 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 179 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 180 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 181 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 182 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 183 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 184 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 185 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 186 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 187 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 188 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 189 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 190 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 191 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 192 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 193 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 194 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 195 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 196 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 197 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 198 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 199 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 200 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 201 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 202 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 203 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 204 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 205 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 206 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 207 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 208 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 209 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 210 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 211 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 212 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 213 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 214 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 215 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 216 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 217 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 218 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 219 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 220 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 221 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 222 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 223 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 224 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 225 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 226 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 227 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 228 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 229 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 230 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 231 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 232 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 233 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 234 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 235 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 236 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 237 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 238 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 239 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 240 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 241 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 242 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 243 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 244 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 245 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 246 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 247 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 248 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 249 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 250 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 251 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 252 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 253 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 254 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 255 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 256 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 257 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 258 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 259 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 260 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 261 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 262 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 263 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 264 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 265 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 266 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 267 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 268 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 269 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 270 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 271 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 272 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 273 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 274 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 275 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 276 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 277 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 278 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 279 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 280 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 281 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 282 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 283 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 284 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 285 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 286 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 287 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 288 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 289 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 290 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 291 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 292 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 293 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 294 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 295 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 296 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 297 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 298 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 299 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 300 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 301 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 302 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 303 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 304 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 305 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 306 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 307 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 308 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 309 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 310 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 311 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 312 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 313 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 314 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 315 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 316 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 317 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 318 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 319 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 320 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 321 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 322 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
