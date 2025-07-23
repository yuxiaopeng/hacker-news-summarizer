# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-23.md)

*最后自动更新时间: 2025-07-23 17:53:32*
## 1. 你现在可以禁用 Zed 中的所有 AI 功能了

**原文标题**: You Can Now Disable All AI Features in Zed

**原文链接**: [https://zed.dev/blog/disable-ai-features](https://zed.dev/blog/disable-ai-features)

Zed 现在允许用户禁用代码编辑器中的所有 AI 功能。此举是为了回应用户反馈，用户出于各种原因避免使用 AI，包括对训练数据、环境影响、组织限制以及偏好传统开发方法的担忧。

用户可以通过在 `settings.json` 文件中添加 `"disable_ai": true` 来禁用 AI，此功能现已在 Preview 版本中提供，下周将在 Stable 版本中发布。新用户很快就能在 onboarding 期间禁用 AI。

Zed 认可选择不使用 AI 的合理工程决策，并为那些担心数据隐私的用户提供替代解决方案。用户可以使用自己的 API 密钥连接到 AI 提供商（“自带密钥”），或使用将代码完全保存在其机器上的本地 AI 模型。使用 Zed AI 时，代码和提示会在每次请求后被丢弃，绝不会用于训练；与 Anthropic 也签订了零保留协议。

Zed 意识到围绕 AI 工具的怀疑态度，并鼓励了解其功能，即使使用者选择不使用它们。Agentic Engineering 系列旨在促进围绕利用 AI 同时保持工艺水平的讨论和学习。

Zed 强调用户控制，并提供自定义编辑器的选项，包括禁用 AI 功能。由于 Zed 在 GPL 许可下开源，因此它授权用户根据自己的偏好修改编辑器。该公司仍然致力于通过添加 Windows 支持、改进其 AI 体验以及关注非 AI 用户，使 Zed 成为最好的代码编辑器。

---

## 2. Proxmox 向 Perl 和 Raku 基金会捐赠 1 万欧元

**原文标题**: Proxmox Donates €10k to the Perl and Raku Foundation

**原文链接**: [https://www.perl.com/article/proxmox-donates-to-tprf/](https://www.perl.com/article/proxmox-donates-to-tprf/)

Proxmox Server Solutions GmbH 向 Perl 和 Raku 基金会 (TPRF) 捐赠 10,000 欧元，以支持 Perl 5 核心维护基金。 这笔捐款对于 TPRF 实现其推进 Perl 和 Raku 编程语言的使命至关重要。

Proxmox，一个开源服务器管理平台，是重视透明度、社区参与和可访问性的典范公司。 Perl 编程语言是各个行业的基石，维护其核心需要专门的资金来保障稳定性、安全更新和功能增强。

Perl 5 核心维护基金用于安全更新、性能优化、平台兼容性、漏洞修复和文档维护。 Proxmox 的贡献确保了这项工作能够不间断地进行，体现了对技术管理的承诺。

这次捐赠突显了从开源生态系统中受益的组织积极投资于该生态系统的重要性。 通过投资 Perl 的开发，Proxmox 为服务于全球开发人员、系统管理员和组织的编程语言生态系统做出了贡献。 这种伙伴关系使 TPRF 能够维护其多样化的社区服务项目。

---

## 3. 阿波罗11号登月人员返回美国需签署美国海关申报单

**原文标题**: Trip to moon required Apollo 11 crew to sign US Customs declaration to enter US

**原文链接**: [https://magazine.uc.edu/editors_picks/recent_features/armstrong/moonrocks.html](https://magazine.uc.edu/editors_picks/recent_features/armstrong/moonrocks.html)

文章讲述了一个有趣的事实：1969年阿波罗11号宇航员完成历史性的登月任务返回后，被要求填写美国海关申报单。该表格通常供国际旅客使用，询问携带入境的物品，如植物、食物、动物和土壤。宇航员们申报了“月球岩石和月球尘埃样本”，并注明出发地为“月球”，抵达地为檀香山。表格还包含一个健康部分，他们在可能导致疾病传播的任何状况一栏中注明“待定”，这表明即使在他们返回后也采取了谨慎措施。文章突出了在非凡的科学成就之后，出人意料的官僚程序。这个故事是由一位加州大学校友Luama Mays分享的，他在尼尔·阿姆斯特朗担任加州大学教授期间与他成为了朋友。梅斯在阿姆斯特朗在加州大学期间帮助了他，让他使用直升机为操作登月舱做准备。文章还提供了关于尼尔·阿姆斯特朗的生平、工作和贡献的相关故事的链接。

---

## 4. 停止倒着构建人工智能工具

**原文标题**: Stop Building AI Tools Backwards

**原文链接**: [https://hazelweakly.me/blog/stop-building-ai-tools-backwards/](https://hazelweakly.me/blog/stop-building-ai-tools-backwards/)

本文认为当前人工智能工具的开发存在缺陷，过度重视人工智能行动，而忽视了人类学习和协作，导致技能下降和系统效率低下。作者提出了一种以人为本的方法，重点关注人类的学习方式：通过检索练习、掌握流程和累积迭代。

核心问题在于，现有的人工智能工具通常在收到提示后立即启动行动，绕过了关键的人工步骤，例如回忆、任务启动、流程强化和知识转移。这剥夺了人类进步的机会以及本可以增强人工智能能力的数据收集。

作者建议将人工智能视为“健忘的导师”，而不是同事，引导用户学习，而不是简单地自动化任务。文章概述了一种改进的 EDGE（解释、演示、指导、提升）教学方法，强调人类在每个阶段的参与：

*   **解释：**人工智能建议缺失的步骤或解释流程指南，促进回忆。
*   **演示：**人工智能将查询转换为系统语法，演示 UI 导航，强化实践技能。
*   **指导：**人工智能提示批判性思维，验证响应，并建议相关的思维模型，培养理解力。
*   **提升：**人工智能建议逐步改进，并识别流程优化和知识共享的机会，促进持续学习。

作者以事件管理为例，提倡人工智能放大人类的效能，而不是自动化整个过程。文章最后总结了关键原则：强化人类学习，改善协作，加速流程执行，避免从空白到结果的自动化，并将团队学习纳入工具输出。最后，文章提供了将以人为本的方法应用于代码生成的另一个例子。

---

## 5. Debian/Trixie 的预期

**原文标题**: What to Expect from Debian/Trixie

**原文链接**: [https://michael-prokop.at/blog/2025/07/20/what-to-expect-from-debian-trixie-newintrixie/](https://michael-prokop.at/blog/2025/07/20/what-to-expect-from-debian-trixie-newintrixie/)

本文预览Debian 13 "Trixie"，预计于2025年8月9日发布，重点关注其从系统管理员角度对服务器系统的影响。作者强调为升级做好积极准备，重点介绍软件包的可用性和潜在问题。

本文提供了Debian 12 "Bookworm"和Trixie之间关键软件（如Ansible、Apache、Docker、Emacs、Git、MariaDB、Nginx、OpenJDK、OpenSSH、Perl、PHP、PostgreSQL、Puppet、Python3 等）的软件包版本比较列表，以便快速了解用户可以预期的重大版本升级。

详细介绍了关键更改和新功能，包括更新后的`apt`软件包，它具有增强的功能，如彩色输出、改进的可读性以及`apt-key`的移除。systemd升级为现有命令带来了许多新工具和选项，可能会影响网络命名方案。

本文还重点介绍了Linux内核更新（基于6.12），其中包含新的系统调用、完整性策略强制执行LSM、io_uring的改进、文件系统更新（ntfs3取代ntfs）以及各种性能和安全增强功能。

最后，作者提到了Debian中Puppet软件包的可用性，同时指出上游软件包尚未提供给trixie。

---

## 6. Manticore Search: 快速、高效的 Elasticsearch 即时替代品

**原文标题**: Manticore Search: Fast, efficient, drop-in replacement for Elasticsearch

**原文链接**: [https://github.com/manticoresoftware/manticoresearch](https://github.com/manticoresoftware/manticoresearch)

Manticore Search 是一个快速的开源搜索数据库，定位为 Elasticsearch 的直接替代品。它拥有显著的性能优势，基准测试表明其在各种数据规模和摄取速度上均优于 Elasticsearch。其主要特性包括现代化的多线程架构、支持行式和列式存储、使用 PGM-index 的高性能二级索引、基于成本的查询优化器以及与 MySQL 协议兼容的 SQL-first 语法。

Manticore 提供了多种搜索功能，包括具有自定义排序的全文本搜索、丰富的过滤、模糊搜索、分面搜索、地理空间搜索和向量搜索。它还提供 NLP 功能，如词干提取、词形还原和高级分词。 为了实现高可用性，它支持同步复制和内置负载均衡。 数据可以从各种来源同步，包括 MySQL、PostgreSQL、XML 和 CSV。

Manticore 易于安装和部署，可通过 Docker、适用于各种操作系统的软件包和云平台进行部署。它被 Craigslist 和 PubChem 等公司使用。 该项目提供广泛的文档、互动课程和社区支持渠道。 用户可以通过捐赠或成为审计、支持、咨询、开发和培训服务的客户来支持 Manticore Search。 Manticore 在 GPLv3 许可下授权，并使用其他开源组件。

---

## 7. Optery (YC W22) 正在招聘工程、法律、销售、市场人员（美国、拉美）

**原文标题**: Optery (YC W22) Is Hiring in Engineering, Legal, Sales, Marketing (U.S., Latam)

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22) 正在招聘多个职位，涵盖工程、法律、销售和市场等多个部门。这些职位面向位于美国和拉丁美洲 (Latam) 的候选人开放。这表明 Optery 正在扩张团队，拥有分布式劳动力，或者愿意接受这些地区的远程员工。作为 Y Combinator (YC) 2022 年冬季项目的校友，表明 Optery 是一家相对年轻、快速增长的初创公司，可能专注于创新和积极扩张。这可能会吸引那些在充满活力和快节奏的环境中寻找机会的候选人。广泛的职位表明该公司正在解决其业务的不同方面，从产品开发和法律合规到收入产生和品牌知名度。有兴趣的人士应访问 Optery 的职业页面，了解有关具体职位空缺和申请说明的更多详细信息。

---

## 8. Cerebras发布Qwen3-235B，实现每秒1.5k tokens

**原文标题**: Cerebras launches Qwen3-235B, achieving 1.5k tokens per second

**原文链接**: [https://www.cerebras.ai/press-release/cerebras-launches-qwen3-235b-world-s-fastest-frontier-ai-model-with-full-131k-context-support](https://www.cerebras.ai/press-release/cerebras-launches-qwen3-235b-world-s-fastest-frontier-ai-model-with-full-131k-context-support)

Cerebras Systems 在其 Cerebras 推理云上推出了 Qwen3-235B，并宣称它是世界上最快的具有完整 131K 上下文支持的前沿 AI 模型。独立测试表明，该模型的智能水平可与 Claude 4 Sonnet 和 Gemini 2.5 Flash 等模型相媲美。

主要优势包括：

*   **速度：** 达到每秒 1,500 个 tokens，将推理时间从几分钟缩短到亚秒级。
*   **成本效益：** 定价为每百万输入 tokens 0.60 美元，每百万输出 tokens 1.20 美元，远低于闭源替代方案。
*   **上下文长度：** 支持 131K 上下文，通过同时处理大型代码库和复杂文档，实现生产级代码生成。

这种增强的上下文长度直接针对企业代码生成市场。为了展示模型的能力，Cerebras 与 Microsoft VS Code 的编码代理 Cline 合作，允许 Cline 用户直接在编辑器中访问 Cerebras Qwen 模型。最初从 Qwen3-32B 开始，推广将扩展到包括 Qwen3-235B，从而显著提高代码生成速度。

Cerebras 强调，其推理产品提供了一种开放的替代方案，可替代 OpenAI 和 Anthropic，以无与伦比的速度和成本效益提供可比的智能和代码生成能力。

---

## 9. 展示HN：书店技术栈的缺失环节

**原文标题**: Show HN: The missing link of a bookstore's tech stack

**原文链接**: [https://bookhead.net/](https://bookhead.net/)

Bookhead：实体书店技术栈的缺失环节，旨在无缝连接线下库存与线上销售渠道。它通过自动化库存同步，缓解书商痛点，使其能够专注于客户服务和专业知识。

其核心功能围绕自动同步店内POS系统库存到 Biblio、eBay 和 Squarespace 等在线平台（Shopify 集成即将推出）。Bookhead 通过书目数据丰富这些库存，创建产品列表，从而节省书商手动数据录入的时间和精力。 目标是管理一个统一库存，当店内发生销售时，该库存会在所有在线销售渠道中更新。

重点强调的关键优势包括：简化在线图书销售、消除复制/粘贴操作、利用 AI 图书评估估算加速定价以及扩展书店的在线品牌。 该软件旨在通过促进数据共享与现有工具（如 POS 系统和电子商务网站）集成。Bookhead 强调其软件“由书商为书商创建”的出身，理解该行业独有的挑战。目前该软件处于测试阶段，并鼓励早期使用者通过电子邮件注册。

---

## 10. 使用 Radicle CI

**原文标题**: Using Radicle CI

**原文链接**: [https://radicle.xyz/2025/07/23/using-radicle-ci-for-development](https://radicle.xyz/2025/07/23/using-radicle-ci-for-development)

本文详细介绍了作者 (lars) 使用 Radicle CI 进行软件开发的工作流程，特别是使用 Ambient 作为 CI 引擎。作者从一个“hello world” Rust 项目开始，初始化一个 Radicle 仓库，并使用 `.radicle/ambient.yaml` 文件设置 CI 配置，以运行 `cargo clippy` 和 `cargo test`。

该工作流程的一个关键方面是使用 `rad ci` 扩展进行本地 CI 执行，这允许调试 CI 配置，而无需依赖远程服务器。这可以实现更快的迭代，并避免资源争用。

作者还使用专用 CI 节点 (`ci0`) 来运行 Radicle CI broker 和 Ambient，确保所有项目的一致环境。该节点发布 HTML 报告页面以供公开访问。

本文然后演示了报告问题和进行更改的过程。创建了一个关于默认问候语的问题。创建一个新分支，对问候语进行更改，并创建和推送一个 Radicle 补丁。由于测试失败，初始 CI 运行失败，作者通过 CI broker 发布的网页识别出此问题。

作者然后修复测试，提交更改，并推送更新后的补丁。在 CI 运行成功后，该补丁被合并到主分支，并且该分支被删除，从而完成开发周期。整个过程突出了 Radicle、Ambient 和本地测试的集成，从而在 Radicle 生态系统中实现简化的 CI/CD 体验。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 2 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 3 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 4 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 5 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 6 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 7 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 8 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 9 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 10 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 11 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 12 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 13 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 14 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 15 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 16 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 17 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 18 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 19 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 20 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 21 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 22 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 23 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 24 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 25 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 26 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 27 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 28 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 29 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 30 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 31 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 32 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 33 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 34 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 35 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 36 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 37 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 38 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 39 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 40 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 41 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 42 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 43 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 44 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 45 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 46 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 47 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 48 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 49 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 50 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 51 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 52 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 53 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 54 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 55 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 56 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 57 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 58 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 59 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 60 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 61 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 62 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 63 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 64 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 65 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 66 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 67 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 68 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 69 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 70 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 71 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 72 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 73 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 74 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 75 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 76 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 77 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 78 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 79 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 80 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 81 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 82 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 83 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 84 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 85 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 86 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 87 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 88 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 89 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 90 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 91 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 92 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 93 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 94 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 95 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 96 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 97 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 98 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 99 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 100 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 101 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 102 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 103 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 104 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 105 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 106 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 107 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 108 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 109 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 110 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 111 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 112 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 113 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 114 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 115 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 116 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 117 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 118 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 119 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 120 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 121 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 122 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 123 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 124 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 125 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 126 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
