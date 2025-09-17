# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-17.md)

*最后自动更新时间: 2025-09-17 17:47:10*
## 1. 苹果照片应用损坏图像

**原文标题**: Apple Photos App Corrupts Images

**原文链接**: [https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/](https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/)

这篇博文详述了作者在使用 Apple Photos 应用从 OM System OM-1 相机导入照片时，照片损坏的令人沮丧的经历。起初，作者忽略了偶尔出现的损坏，但一次严重的婚礼照片丢失促使他们展开调查。

他们系统地排除了硬件问题，更换了 USB-C 数据线、SD 卡、笔记本电脑，甚至升级到了新的相机机身（OM System OM-1 MKii），但照片损坏的情况仍然存在。通过禁用“导入后删除”选项并手动验证照片，他们确认损坏发生在 Photos 应用*导入*过程中，因为 SD 卡上的照片是完好的。他们发现该应用有时会损坏 JPG 文件、RAW 文件或两者都损坏。

作者发现重新导入损坏的文件通常会成功，这表明损坏是随机的。他们提供了校验和和文件大小，表明损坏的和未损坏的文件大小相同，但包含的数据不同。

沮丧之下，作者放弃了调试，转而使用 Darktable 进行初始导入、筛选和处理的新工作流程。然后，他们将 JPG 和 RAW 文件从 Darktable 导出到 Photos 应用中进行查看和共享。这一改变解决了照片损坏的问题，进一步表明 Photos 应用是罪魁祸首。虽然作者对花费在故障排除上的时间和金钱感到遗憾，但他们现在拥有冗余的硬件和一个可靠的工作流程。

---

## 2. Tau² 基准测试：提示重写如何使 GPT-5-Mini 性能提升 22%

**原文标题**: Tau² Benchmark: How a Prompt Rewrite Boosted GPT-5-Mini by 22%

**原文链接**: [https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/](https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/)

本文详细介绍了提示词改写如何显著提升 GPT-5-mini 模型在 Tau² 基准测试上的表现，该基准测试是一个用于评估 LLM 在电信等领域代理任务中的框架。作者发现，简单地改写代理策略使模型的成功率提高了 22%。

该实验涉及在电信基准测试的一个子集上运行 GPT-5-mini，最初的成功率很低，为 55%。为了改进这一点，他们使用 Claude 分析并改写了 AI 代理策略，针对更快、非旗舰级的 LLM 进行了优化。改写侧重于清晰、指令性的指示、逐步逻辑和二元决策，而不是冗长的策略声明。

结果令人印象深刻：成功率（pass^k 指标）提高了 22.73%，达到 67.5%（k=1），提高了 25%，达到 50%（k=2）。更重要的是，优化后的提示词使 GPT-5-mini 能够解决以前无法解决的任务，将永久失败任务的数量减少了 50%。更新后的提示词使 GPT-5-mini 的性能更接近旗舰级的 GPT-5，甚至在基准测试中超过了 o3。

本文总结道，周到的提示词设计可以有意义地提高较小 LLM 的性能。通过简化语言、减少歧义并将推理分解为可操作的步骤，较小的模型可以取得更好的结果。作者建议使用前沿模型自动优化较小 LLM 的提示词，使其成为重视效率的情况下具有成本效益的替代方案。

---

## 3. 发布HN：RunRL (YC X25) – 强化学习即服务

**原文标题**: Launch HN: RunRL (YC X25) – Reinforcement learning as a service

**原文链接**: [https://runrl.com](https://runrl.com)

RunRL，一家Y Combinator（YC X25）毕业的公司，正在推出强化学习即服务（RLaaS）平台。此举旨在普及强化学习的使用，因为强化学习通常很复杂且需要专业知识。RunRL通过提供预训练模型、自动超参数调整和易于使用的API来简化流程。这使得没有丰富强化学习经验的企业和开发者能够将强化学习集成到他们的应用程序中。

其强调的关键优势是缩短开发时间、降低成本并加快部署速度。通过抽象化强化学习训练和优化的复杂性，RunRL允许用户专注于应用该技术来解决各个领域的实际问题。这包括机器人、游戏、金融和供应链管理。

RunRL的解决方案为运行强化学习算法提供了一个托管的基础设施，消除了用户管理基础设施或自行优化算法的需求。他们提供了一系列预构建的强化学习代理和环境，并支持自定义环境和奖励函数。他们的API使得将强化学习模型集成到现有软件应用程序中变得简单。最终，RunRL旨在降低强化学习的入门门槛，使其更容易被更广泛的受众所接受。

---

## 4. 阿里巴巴新AI芯片：关键规格媲美H20

**原文标题**: Alibaba's new AI chip: Key specifications comparable to H20

**原文链接**: [https://news.futunn.com/en/post/62202518/alibaba-s-new-ai-chip-unveiled-key-specifications-comparable-to](https://news.futunn.com/en/post/62202518/alibaba-s-new-ai-chip-unveiled-key-specifications-comparable-to)

无法访问文章链接。

---

## 5. 如何激励自己去做不想做的事

**原文标题**: How to motivate yourself to do a thing you don't want to do

**原文链接**: [https://ashleyjanssen.com/how-to-motivate-yourself-to-do-a-thing-you-dont-want-to-do/](https://ashleyjanssen.com/how-to-motivate-yourself-to-do-a-thing-you-dont-want-to-do/)

本文探讨了缺乏动力的常见困境，特别是对于我们不喜欢或拖延的任务。作者通过自己不愿进行空气自行车锻炼的个人轶事，来说明我们经常面临的心理斗争。

核心信息是，动力是复杂的，并且受到多种因素的影响，例如睡眠、饮食、身心健康、压力，甚至激素周期。认识到这些因素是第一步。

本文提供了五项关键策略来提高动力：

1.  **了解根本原因：** 找出你缺乏动力的原因。考虑你能控制什么——你的环境、情绪或身体健康——并做出相应的调整。确定是否存在消极的激励因素，以及该任务是否真的有必要。

2.  **识别并利用你的动力来源：** 将不愉快的任务与愉快的活动结合起来（比如一边听音乐一边打扫卫生）。通过朋友或专业人士利用外部问责制。通过设定目标和奖励来游戏化这个过程。庆祝里程碑，以保持动力。

3.  **分解任务：** 当一项任务让人感到难以承受时，将其分解为更小、更易于管理的步骤。即使只是投入 5 分钟也能启动进展。

4.  **优先考虑一致性：** 对于重复性任务，不要仅仅依赖动力。建立一个包含计划时间、提醒和专用时间段的例行程序。持续的努力，即使是少量，也更有效。

5.  **暂缓处理：** 推迟不重要的任务是可以的。有意识地决定它是否是“塑料球”（不那么关键），并专注于其他领域，而不是感到内疚。

作者强调，动力波动是正常的，并鼓励读者评估自己的情况，管理可控因素，并努力取得进展。

---

## 6. 第五个忙碌海狸值的确定

**原文标题**: Determination of the fifth Busy Beaver value

**原文链接**: [https://arxiv.org/abs/2509.12337](https://arxiv.org/abs/2509.12337)

该arXiv文章(arXiv:2509.12337)宣布利用Coq证明助手确定了第五个忙碌海狸值，$S(5) = 47,176,870$。忙碌海狸函数，$S(n)$，表示从全零纸带开始，$n$状态、2符号图灵机在停机前可以执行的最大步数。作者们，来自"bbchallenge"的19位研究人员的合作团队，枚举并分析了181,385,789个具有5个状态的图灵机，以确定它们是否会停机。这标志着40多年来首次确定的新的忙碌海狸值，也是第一个使用证明助手进行正式验证的忙碌海狸值。该论文强调了大规模协作在线研究的有效性。文章包括诸如页数(48)、图数(17)、主题类别(计算机科学逻辑、形式语言与自动机理论、逻辑)以及相关的MSC和ACM分类等详细信息。Tristan Stérin提交了该文章。

---

## 7. 事件视界实验室 (YC W24) 正在招聘

**原文标题**: Event Horizon Labs (YC W24) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/event-horizon-labs/jobs/U6oyyKZ-founding-engineer-at-event-horizon-labs](https://www.ycombinator.com/companies/event-horizon-labs/jobs/U6oyyKZ-founding-engineer-at-event-horizon-labs)

事件视界实验室 (YC W24) 正在寻找一位创始工程师来构建他们的“后人类交易者”，这是一个将数据和计算直接转化为超额收益的自主系统，从而消除交易中的人为偏见。该职位位于旧金山，薪资范围为 15 万美元至 21 万美元，股权为 1.00% 至 3.00%。

该工程师将负责设计和构建高并发管道以及稳健、容错的系统，塑造公司的核心基础设施。理想的候选人应具备顶尖的系统设计专业知识，精通容器化和云技术（Docker、Kubernetes），并拥有在高并发和近实时数据处理方面扩展和优化数据库性能的经验。

事件视界实验室强调建立一支专注于突破人工智能系统界限的小型高素质团队。他们寻找在编程、研究或系统设计方面有经验，并渴望应对人工智能基础设施领域挑战性问题的人才。该公司成立于 2023 年，目前正积极致力于在人工智能交易领域构建创新解决方案。

---

## 8. UUIDv47：数据库存储UUIDv7，外部输出UUIDv4（SipHash掩码的时间戳）

**原文标题**: UUIDv47: Store UUIDv7 in DB, emit UUIDv4 outside (SipHash-masked timestamp)

**原文链接**: [https://github.com/stateless-me/uuidv47](https://github.com/stateless-me/uuidv47)

UUIDv47 提供了一种使用 UUIDv7 的方式，由于其时间顺序特性，UUIDv7 对数据库友好，同时向外部系统呈现一个 UUIDv4 兼容的界面。这是通过使用 SipHash-2-4（一种带密钥的伪随机函数 (PRF)）导出的值屏蔽 UUIDv7 的时间戳部分（该值来源于 UUID 的随机位）来实现的。

核心思想是将 UUIDv7 存储在数据库中，以获得更好的索引局部性和分页性能，然后在通过 API 公开之前，将其转换为一个看起来像 UUIDv4 的标识符。 这可以防止暴露 UUIDv7 中固有的时间模式。 该转换是确定性的且可逆的，从而确保数据完整性。

该过程包括将 UUIDv7 的 48 位时间戳与 SipHash-2-4 生成的 48 位掩码进行异或运算。 SipHash 的输入来源于 UUID 的随机位。 编码将 UUIDv7 转换为 UUIDv4 界面，而解码则反转该过程。 UUIDv47 以仅包含头文件的 C 库实现，没有依赖项，并且包含测试。 它提供了用于编码、解码、解析、格式化和检查 UUID 的函数。 安全性通过使用 SipHash-2-4 来防止密钥泄露，并确保 UUID 界面看起来与普通的 UUIDv4 无法区分来得到保证。 该库的设计注重速度，并避免内存分配。

---

## 9. 用于 SQL Server 的 Microsoft Python 驱动程序

**原文标题**: Microsoft Python Driver for SQL Server

**原文链接**: [https://github.com/microsoft/mssql-python](https://github.com/microsoft/mssql-python)

`mssql-python` 驱动是由微软开发的 Python 库，用于连接到 SQL Server 和 Azure SQL 数据库。它提供直接的数据库连接，无需外部驱动程序管理器，并且符合 DB API 2.0 规范，同时引入了 Python 化的增强功能。目前处于公开预览阶段（谨慎使用），它支持一系列数据库操作，包括连接管理、查询执行和事务处理。

该驱动与 Python 3.10 及以上版本兼容，可以使用 pip 在 Windows、MacOS 和 Linux 上安装。它支持多种平台，包括 Windows、MacOS、Linux (Debian, Ubuntu, RHEL, SUSE, Alpine)。主要功能包括 DBAPI v2.0 兼容性，从而实现与各种 Python 应用程序和框架的兼容性。它还支持 Microsoft Entra ID 身份验证，提供多种身份验证方法，如用户名/密码、托管身份、集成 Windows 身份验证（仅限 Windows）、交互式登录、设备代码流和默认身份验证。

此外，该驱动还提供增强的 Python 化功能，例如内置的连接池，以提高性能。该文档提供了如何连接到 SQL Server 和执行简单查询的示例，并指出了有关贡献、支持和许可信息（MIT 许可证，但 libs 文件夹中的 DLL 除外）的资源。

---

## 10. GNU 午夜指挥官

**原文标题**: GNU Midnight Commander

**原文链接**: [https://midnight-commander.org/](https://midnight-commander.org/)

GNU Midnight Commander (mc) 是一款免费、可视化、双面板的文本环境文件管理器。它允许用户执行文件操作，如复制、移动和删除文件及目录。它包含内置的查看器、编辑器和差异查看器。mc 用途广泛，可在控制台、X Window 终端、SSH 连接和远程 shell 中运行。

可以使用系统包管理器轻松安装（Debian/Ubuntu 使用 apt-get，Fedora/Red Hat 使用 dnf，FreeBSD 使用 pkg，macOS 使用 brew）。源代码可通过 OSU OSL 镜像和 GitHub 仓库获取。

文档可通过上下文相关的在线帮助 (F1) 和大量的 man 手册页（mc、mcedit、mcview、mcdiff）访问，也可在线获取。

Midnight Commander 支持主题，可在 skins.midnight-commander.org 获取可用皮肤。

用户可在“交流”页面找到支持信息。贡献信息可在“开发”部分找到，开发版本的发行说明位于 wiki 上。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 2 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 3 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 4 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 5 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 6 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 7 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 8 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 9 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 10 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 11 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 12 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 13 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 14 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 15 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 16 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 17 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 18 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 19 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 20 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 21 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 22 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 23 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 24 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 25 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 26 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 27 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 28 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 29 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 30 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 31 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 32 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 33 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 34 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 35 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 36 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 37 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 38 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 39 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 40 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 41 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 42 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 43 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 44 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 45 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 46 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 47 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 48 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 49 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 50 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 51 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 52 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 53 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 54 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 55 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 56 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 57 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 58 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 59 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 60 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 61 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 62 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 63 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 64 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 65 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 66 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 67 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 68 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 69 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 70 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 71 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 72 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 73 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 74 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 75 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 76 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 77 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 78 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 79 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 80 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 81 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 82 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 83 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 84 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 85 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 86 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 87 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 88 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 89 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 90 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 91 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 92 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 93 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 94 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 95 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 96 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 97 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 98 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 99 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 100 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 101 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 102 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 103 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 104 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 105 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 106 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 107 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 108 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 109 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 110 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 111 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 112 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 113 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 114 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 115 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 116 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 117 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 118 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 119 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 120 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 121 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 122 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 123 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 124 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 125 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 126 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 127 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 128 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 129 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 130 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 131 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 132 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 133 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 134 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 135 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 136 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 137 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 138 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 139 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 140 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 141 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 142 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 143 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 144 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 145 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 146 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 147 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 148 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 149 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 150 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 151 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 152 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 153 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 154 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 155 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 156 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 157 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 158 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 159 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 160 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 161 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 162 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 163 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 164 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 165 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 166 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 167 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 168 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 169 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 170 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 171 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 172 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 173 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 174 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 175 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 176 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 177 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 178 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 179 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 180 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 181 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 182 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
