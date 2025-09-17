# Hacker News 热门文章摘要 (2025-09-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 沙丘蠕虫恶意软件攻击：Tinycolor 及超过 40 个 NPM 包被入侵

**原文标题**: Shai-Hulud malware attack: Tinycolor and over 40 NPM packages compromised

**原文链接**: [https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

**概要:**

Socket.dev的文章详细描述了一起名为“Shai-Hulud”的持续供应链攻击，该攻击已入侵超过40个NPM包，包括流行的`tinycolor`库。 该攻击的目标是 CrowdStrike Falcon Insight 的用户，专门旨在窃取凭据和潜在的其他敏感数据。

这些恶意软件包包含经过混淆的 JavaScript 代码，该代码试图识别使用 CrowdStrike Falcon 的环境。 如果检测到 Falcon 代理，恶意软件会收集环境变量，可能包括 API 密钥、密钥和凭据，并将它们泄露到攻击者控制的服务器。 `tinycolor` 包特别是在 1.6.0 版本中注入了一个恶意的 postinstall 脚本，该脚本随后被迅速删除。

攻击者利用拼写错误和依赖混淆技术来传播恶意软件。 这包括创建名称与合法、广泛使用的软件包相似的软件包，并将它们发布到公共 NPM 注册表中，希望开发人员会意外安装恶意版本，或者它们会作为依赖项包含在使用较松散的依赖项解析的项目中。

此次攻击的影响是巨大的，可能会暴露敏感信息，并允许攻击者获得对目标系统的未经授权的访问权限。 受感染的软件包已从 NPM 中删除，但建议开发人员审查其依赖项，特别是那些最近更新的依赖项，并确保他们使用的是合法版本。 Socket.dev 建议审核 NPM 项目以识别和删除任何恶意软件包，并审查其依赖树以查找任何意外或可疑的添加项。 他们还建议在安装来自不熟悉的发布者的软件包时要小心。

---

## 12. 程序化岛屿生成（三）

**原文标题**: Procedural Island Generation (III)

**原文链接**: [https://brashandplucky.com/2025/09/17/procedural-island-generation-iii.html](https://brashandplucky.com/2025/09/17/procedural-island-generation-iii.html)

本文是关于程序化岛屿生成的系列文章的第三篇，重点在于使用多尺度噪声、山峰的距离场以及混合技术来细化地形高程。

它首先回顾了第一部分中的绘制图基础，该基础提供了基本的陆地/水域分布。下一步涉及分层多个倍频程的 Simplex 噪声，频率从 1 倍到 64 倍不等，以在不同尺度上增加细节。应用了一种沿海噪声增强技术，使用一种在水位（e=0）处达到峰值的公式，将高频细节集中在海岸线附近。

第一部分中识别出的山峰用于通过 Delaunay 三角剖分网格上的广度优先搜索 (BFS) 生成距离场。这确保了遵循地形连通性的有机山形。在距离计算过程中引入随机化，以创建自然的脊线模式。

最终高程通过沿海高程、山丘高程（受噪声调制）和山峰高程（源自距离场）的加权混合来计算。混合使用二次函数来实现平滑过渡。沿海噪声强度、山丘高度、海洋深度、山坡和锐度等参数是可调节的，以控制最终外观。

最后，本文解释了如何通过平均共享区域种子点作为顶点的三角形的高程来为 Voronoi 区域分配高程。下一步，即第四部分将涵盖水文过程的模拟，例如降雨、河流和侵蚀。

---

## 13. PureVPN IPv6 泄露

**原文标题**: PureVPN IPv6 Leak

**原文链接**: [https://anagogistis.com/posts/purevpn-ipv6-leak/](https://anagogistis.com/posts/purevpn-ipv6-leak/)

本文详细描述了PureVPN Linux客户端（GUI v2.10.0和CLI v2.0.1）中发现的关于IPv6保护和防火墙管理的严重安全漏洞。作者于2025年8月末向PureVPN的漏洞披露计划（VDP）提交了这些问题，但未收到任何回应，因此公开披露。

第一个问题涉及IPv6泄漏。在Wi-Fi切换或从睡眠状态恢复后，客户端未能重新建立IPv6保护，导致流量通过用户的ISP地址传输，即使VPN客户端报告连接成功。具体而言，CLI客户端建立了一个默认的IPv6路由，而GUI客户端阻止了IPv4，但保持IPv6活动状态，直到手动重新连接。

第二个主要漏洞是客户端在连接时完全重置用户的iptables防火墙配置，将INPUT链设置为ACCEPT并清除所有现有规则（包括UFW和Docker规则）。关键是，这种修改后的防火墙状态在断开连接后*不会*恢复，使得系统比连接VPN之前更易受攻击。这种行为违背了用户期望通过使用VPN来增强安全性的期望，并削弱了本地防火墙的有效性。

作者强调了这些问题对现实世界的影响，突出了IPv6泄漏和自定义防火墙配置的丢失会损害隐私。他们向PureVPN的安全团队提交了全面的技术报告和屏幕录像，但未收到任何确认。文章最后警告用户在使用PureVPN的Linux客户端时要谨慎。

---

## 14. YouTube 回应广告拦截器导致观看次数下降问题

**原文标题**: YouTube addresses lower view counts which seem to be caused by ad blockers

**原文链接**: [https://9to5google.com/2025/09/16/youtube-lower-view-counts-ad-blockers/](https://9to5google.com/2025/09/16/youtube-lower-view-counts-ad-blockers/)

9to5Google报道称近期YouTube视频观看次数显著下降，引发创作者猜测。尽管YouTube否认存在“系统性问题”，但最合理的解释指向广告拦截器。包括Josh Strife Hayes和TechLinked（Linus Tech Tips旗下）在内的许多YouTuber观察到，电脑端观看次数大幅下降，而其他设备的观看次数保持稳定。这与YouTube打击广告拦截器的持续努力相吻合。

YouTube的声明承认广告拦截器“可能会影响报告观看次数的准确性”，间接暗示了联系。进一步支持这一理论的是，Linus Tech Tips注意到，尽管观看次数下降，但广告收入并未受到影响，表明被广告拦截的观看未被货币化，因此可能未被完全计算在内。

文章驳斥了其他潜在原因，例如YouTube新的AI驱动的年龄验证工具，YouTube明确否认了这一点。该公司还提出了诸如“季节性观看习惯”和竞争加剧等因素，但广告拦截器的解释似乎最令人信服，因为它与观察到的数据和YouTube含糊的声明直接一致。一条热门评论突出了用户的观点，即如果该网站没有受到侵入式广告的困扰，他们就不需要广告拦截器。

---

## 15. 安卓版火狐 143 将引入 DoH

**原文标题**: Firefox 143 for Android to introduce DoH

**原文链接**: [https://blog.mozilla.org/en/firefox/dns-android/](https://blog.mozilla.org/en/firefox/dns-android/)

本文宣布即将发布安卓版 Firefox 143，该版本将为移动平台引入 DNS-over-HTTPS (DoH) 功能。DoH 加密 DNS 查询，防止互联网服务提供商或公共 WiFi 提供商窃听浏览活动。Firefox 是第一个默认实施 DoH 的浏览器，2020 年在美国开始，2023 年扩展到加拿大。

在安卓平台上的应用是 DoH 性能显著提升后的结果，使其速度几乎与原生 DNS 解析一样快。与 CIRA 和 Akamai 的合作使 75% 的用户的 DoH 查询速度提高了 61%。安卓版 Firefox 用户可以通过在设置中选择“增强保护”来启用 DoH。如果性能测试结果积极，Mozilla 计划在某些地区为安卓用户默认启用 DoH。

Mozilla 强调其对用户隐私和透明度的承诺。Firefox 允许用户选择退出 DoH，选择自己的解析器并调整保护级别。只有符合 Mozilla 严格的受信任递归解析器 (TRR) 策略的 DNS 提供商才能成为 Firefox 中的 DoH 提供商。该公司强调合作伙伴关系在提高互联网隐私和速度方面的益处，不仅对 Firefox 用户有益，而且对更广泛的互联网社区也有益。

---

## 16. 状态图：将 Terraform 状态视为分布式系统问题

**原文标题**: Stategraph: Terraform state as a distributed systems problem

**原文链接**: [https://stategraph.dev/blog/why-stategraph/](https://stategraph.dev/blog/why-stategraph/)

本文认为，Terraform基于文件的状态管理与其所解决的分布式系统问题存在根本的架构不匹配，导致扩展性问题和诸如状态拆分之类的变通方法。核心问题在于Terraform在单个JSON文件上使用全局互斥锁，导致锁争用随着团队规模和资源数量的增加而超线性增长。这迫使进程锁定和读取整个状态文件，即使只有一小部分被修改。

Stategraph建议将Terraform状态视为资源的有向无环图，利用已建立的分布式系统原则，如细粒度锁定、多版本并发控制 (MVCC) 和ACID事务。通过将状态规范化到图数据库 (PostgreSQL) 中，Stategraph能够实现子图隔离（并行处理不相交的子图上的操作）、精确锁定（基于依赖关系的行/边级别锁定）和增量刷新（将刷新工作范围限定在受影响的子图）。

关键优势包括显著提高的并发吞吐量、缩短的刷新时间和更好的整体可扩展性。Stategraph被实现为一个通过Terraform远程后端协议访问的PostgreSQL模式，无需更改现有的Terraform配置。它自动从现有的`tfstate`文件构建图表示。本文将Stategraph定位为存储层的替代方案，在保留Terraform执行模型的同时解决协调问题。

---

## 17. SQLiteData: 一个使用SQL和CloudKit的快速、轻量级SwiftData替代方案

**原文标题**: SQLiteData: A fast, lightweight replacement for SwiftData using SQL and CloudKit

**原文链接**: [https://github.com/pointfreeco/sqlite-data](https://github.com/pointfreeco/sqlite-data)

SQLiteData 是一个快速、轻量级的替代 SwiftData 的方案，用于数据持久化和同步，它直接利用 SQLite 并支持 CloudKit 集成。它允许开发者使用熟悉的 Swift 数据类型，同时受益于 SQLite 的性能。

主要特性和优势包括：

*   **SwiftData 替代方案：** 提供类似于 SwiftData 的 `@Model` 和 `@Query` 的属性包装器，如 `@Table` 和 `@FetchAll`，提供类似的功能。
*   **SQLite 驱动：** 直接利用 SQLite 进行存储，提供潜在的更好性能。
*   **CloudKit 同步：** 支持使用 CloudKit 在设备之间无缝同步数据。
*   **广泛的兼容性：** 可部署到 iOS 13 及更高版本。
*   **需要 SQL 知识：** 假设用户熟悉 SQLite 的概念，如模式设计、SQL 查询和性能优化。
*   **性能：** 根据提供的基准测试，提供与其他 SQLite 库相当或更优越的性能。
*   **示例项目：** 包括演示常见应用程序问题和 CloudKit 集成的示例，包括 Apple 的 Reminders 和 Scrumdinger (SyncUps) 应用的重建。
*   **易于安装：** 可以通过 Swift Package Manager 安装。
*   **社区支持：** 鼓励通过 GitHub Discussions 和 Point-Free Community Slack 进行社区讨论。

这篇文章强调了该库为数据持久化提供强大而灵活的解决方案的能力，同时拥抱了 SQLite 的成熟生态系统。

---

## 18. 慢社交媒体

**原文标题**: Slow social media

**原文链接**: [https://herman.bearblog.dev/slow-social-media/](https://herman.bearblog.dev/slow-social-media/)

作者，一位自称的当代社交媒体评论家，概述了他们对一个“慢社交媒体”平台的愿景，该平台旨在促进真正的联系和深思熟虑的互动，而不是成瘾和商业剥削。他们认为，当前的平台以牺牲用户福祉为代价，优先考虑利润驱动的参与，变成了“推荐媒体”，而不是培养关系的工具。

他们提出的平台将有意限制旨在推动用户参与的功能，并优先考虑人际连接。关键功能包括：

*   **对称的“朋友”关系：**用互惠关系取代“粉丝”，以阻止自我驱动的行为和准社会交往。
*   **有限的连接数量：**将朋友数量限制在300左右，以阻止收集行为并鼓励真正的人际关系。
*   **时间线信息流：**按时间顺序呈现帖子，并具有明确的结束点，不同于无限滚动，从而促进有意识的使用。
*   **帖子频率限制：**将每日帖子数量限制在5个左右，以鼓励有意识的分享。
*   **无分析功能：**专注于连接而不是追踪参与度和触及范围。
*   **基本功能：**一个简单的界面，包含评论和反应，但不包括短视频和推荐算法等令人上瘾的元素。

作者承认构建和资助这样一个平台的挑战，因为它将与更引人注目的商业替代品竞争。尽管不打算自己构建，但他们表示希望有人能够创造这种替代方案，并提供他们的专业知识。

---

## 19. 软件定义无线电的应用 (2024)

**原文标题**: Things you can do with a Software Defined Radio (2024)

**原文链接**: [https://blinry.org/50-things-with-sdr/](https://blinry.org/50-things-with-sdr/)

Blinry 的文章《利用软件无线电可以做的那些事 (2024)》详细介绍了他们使用廉价的 RTL-SDR Blog V4 USB 加密狗和天线套件，对电磁频谱进行为期一周的探索。受“制造五十个某物”技巧的启发，作者旨在发现并记录五十种不同的信号和 SDR 技术的用途。

这篇文章可作为初学者指南，解释了入门所需的硬件和软件（主要是 SDR++）。然后，它记录了 Blinry 每天的发现，包括收听 FM 广播、Freenet 通信、机场天气广播 (ATIS)、通过 ADS-B 跟踪飞机、收听 2 米业余无线电波段的对话、接收数字广播 (DAB+) 以及窃听 PMR446 传输。

这次旅程不仅限于简单的收听，还包括更复杂的活动，例如解码来自邻居 433 MHz 传感器的信号、通过 AIS 跟踪船舶以及检测来自手机的 GSM 活动。作者花费大量精力接收来自 NOAA 卫星的信号。作者还跟踪并尝试回收气象气球，甚至在此过程中遇到了一位气象气球猎手。最后，作者尝试构建“随机线”天线以改善较低频率的接收效果，并尝试解码业余无线电数据包信号。作者小心地指出他们没有参与的非法活动。通篇，文章强调了 SDR 技术的可及性和令人惊讶的各种可能性。

---

## 20. Notion API 导入器，含数据库至基地的转换奖励

**原文标题**: Notion API importer, with Databases to Bases conversion bounty

**原文链接**: [https://github.com/obsidianmd/obsidian-importer/issues/421](https://github.com/obsidianmd/obsidian-importer/issues/421)

本文档是一份Github issue，提议悬赏开发一个Obsidian Markdown编辑器用的Notion API导入器。该导入器会将Notion数据库转换为Obsidian Base（在.base文件中使用YAML语法）。赏金为5,000美元，时限为30天，作者要求申请者具备Obsidian Importer代码库和Notion API的使用经验。

该导入器必须使用Notion API（包括2025年9月发布的新数据源对象），将文件转换为Obsidian风格的Markdown（包括表格和待办事项列表），通过在Markdown中嵌入链接来处理图像和附件，并将Notion数据库转换为Obsidian Base。任务的一个关键方面是确定如何最好地将Notion数据库表示为Obsidian Base，考虑到它们在基本结构和功能上的差异（如视图、列、公式等）。提案承认某些Notion数据库功能可能无法完美地转换为Base，可能需要合适的替代方案。需要提供可用的测试用例或测试Notion帐户来演示功能。

---

## 21. 在真实硬件上证实《毁灭战士》在现实世界运行2.5年后崩溃

**原文标题**: Doom crash after 2.5 years of real-world runtime confirmed on real hardware

**原文链接**: [https://lenowo.org/viewtopic.php?t=31](https://lenowo.org/viewtopic.php?t=31)

某个人进行了一项真实世界的实验，以测试初代Doom的演示追踪变量中潜在的溢出漏洞。该变量持续递增，即使在演示之间也是如此，作者推测它最终会溢出，并在足够长的时间后导致游戏崩溃。经过计算，表明大约2.5年的连续运行后会崩溃，作者在由定制UPS供电并通过路由器连接以保持恒定电源的PDA上设置了Doom。该系统在那段时间内运行未被打扰。大约2.5年后，Doom游戏确实由于预期的变量溢出而崩溃，证实了最初的假设，并为实际硬件上的理论漏洞提供了实践证据。提供了一张记录崩溃的照片。作者承认实验开始时文档记录存在缺失。

---

## 22. 欧盟聊天监控：德国立场改为未决

**原文标题**: EU Chat Control: Germany's position has been reverted to undecided

**原文链接**: [https://mastodon.social/@chatcontrol/115215006562371435](https://mastodon.social/@chatcontrol/115215006562371435)

文章指出，德国对欧盟聊天监控提案的立场已恢复为“未决”。这表明其立场发生了变化，之前可能支持或反对该提案。信息来源是Mastodon上的一篇帖子。该帖子本身是一则简短的声明，并且Mastodon平台需要启用JavaScript才能查看内容，这表明帖子本身可能包含更多上下文或讨论。因此，主要结论是德国对欧盟聊天监控的立场目前尚不确定。

---

## 23. 华硕游戏本ACPI固件漏洞：深度技术调查

**原文标题**: The Asus Gaming Laptop ACPI Firmware Bug: A Deep Technical Investigation

**原文链接**: [https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive](https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive)

本文深入技术层面，详细调查了影响华硕 ROG 游戏笔记本电脑的一个固件错误，该错误会导致性能卡顿、音频问题，甚至系统崩溃。调查显示，问题源于嵌入笔记本电脑 BIOS 中的低效 ACPI 机器语言 (AML) 代码，而非驱动程序或操作系统本身。

作者使用 LatencyMon 和 Windows 事件跟踪 (ETW)，确定 ACPI.sys 是罪魁祸首，特别指出源自 _GPE._L02 通用事件的高 DPC 延迟。分析揭示，中断峰值以 30-60 秒的周期性模式出现，与电池/AC 适配器状态检查有关，令人惊讶的是，还与重复尝试打开和关闭独立显卡 (dGPU) 有关，即使它是在终极模式下连接外部显示器时唯一活动的 GPU。

通过从 BIOS 中提取和反编译 ACPI 表，作者揭示了 _GPE._L02 调用的有缺陷的 ECLV 实现。此实现包含严重的错误：在中断上下文中休眠，并可能强制另一个中断事件挂起，从而垄断 CPU 时间，特别是核心 0，并导致观察到的性能问题。文章总结说，这些不合逻辑的固件操作是受影响用户遇到的系统不稳定和性能下降的根本原因。

---

## 24. Murex – 一款为现代命令行设计的直观且内容感知的Shell

**原文标题**: Murex – An intuitive and content aware shell for a modern command line

**原文链接**: [https://murex.rocks/](https://murex.rocks/)

Murex：一款为增强命令行体验而设计的现代、直观且内容感知的 Shell。它拥有多项独特功能，包括原生支持处理 JSON、YAML 和 CSV 等数据格式，从而简化数据集成和操作。Murex 还提供更智能的变量和表达式处理，旨在减少脚本错误。

该 Shell 旨在实现直观的交互，提供来自 man 手册、AI LLM 和其他智能集成的命令行提示，从而使导航更快、更高效。Murex 还设计为易于扩展，内置的包管理器可促进共享配置、导入模块以及跨机器移植环境。

提供了适用于 macOS（通过 Homebrew 和 MacPorts）、Arch Linux（通过 AUR）和 FreeBSD（通过 `pkg install`）的安装说明。可以通过语言导览、面向 Bash 用户的 Rosetta Stone 速查表以及交互式 shell 指南轻松获得文档。

---

## 25. 你无法验证量子力学是否使用了复数。

**原文标题**: You can't test if quantum uses complex numbers

**原文链接**: [https://algassert.com/post/2501](https://algassert.com/post/2501)

本文批判了2021年发表的论文《基于实数的量子理论可以被实验证伪》，认为其标题具有误导性。该论文声称设计了一种测试来区分使用复数的量子计算机和仅限于实数的量子计算机。本文作者证明，通过采用特定的欺骗策略，“纯实数”量子计算机 *可以* 通过该测试。

关键思想是利用预共享的纠缠和一个相位梯度态（或其变体）。虽然最初的测试旨在防止以保持局部性的方式用实数模拟复数运算，但作者表明，一个 CHM (CCX + H + M) 门集合可以通过在测试之前将精心构建的纯实数态 (G') 的纠缠副本分发给每台计算机，来模拟 CHMT (CCX + H + M + T) 电路。在测试过程中，每个 T 门都被替换为对 G' 的本地纠缠副本进行受控增量。这种构造本质上是使用“相位反冲”和一个巧妙的叠加来绕过直接复数运算的需求。

作者指出，Renou等人不可能性的证明依赖于参与测试的量子计算机在测试开始时没有预先存在的纠缠这一假设。虽然Renou等人确实在其补充材料深处承认了这一警告，但作者认为这个关键假设被淡化了，应该突出显示，甚至在标题中也应如此。由于纠缠在量子系统中很常见，尤其是在涉及局部性的测试中（如贝尔测试，Renou等人的测试就是基于贝尔测试），因此缺乏这种明确的限制使得最初的可证伪性声明变得非常弱。作者总结道，鉴于使用预共享纠缠的现成欺骗方法，该论文的结论值得怀疑。

---

## 26. 与Lyft合作，将全自动驾驶带到纳什维尔。

**原文标题**: Bringing fully autonomous rides to Nashville, in partnership with Lyft

**原文链接**: [https://waymo.com/blog/2025/09/waymo-is-coming-to-nashville-in-partnership-with-lyft](https://waymo.com/blog/2025/09/waymo-is-coming-to-nashville-in-partnership-with-lyft)

Waymo与Lyft合作，将其全自动叫车服务引入田纳西州纳什维尔。Waymo的技术已在美国其他主要城市扩展至每周数十万次乘车，并在公共道路上实现了超过1亿英里的自动驾驶里程，证明其运营安全性远高于人类驾驶员。

纳什维尔的全自动运营将在未来几个月内开始，并于明年向公众开放。Lyft旗下的Flexdrive子公司将提供车队管理专业知识。乘客最初将通过Waymo应用程序叫车，随着服务的扩展，计划与Lyft应用程序集成。

Waymo和Lyft的首席执行官均对此次合作表示兴奋，强调Waymo的自动驾驶技术与Lyft的客户服务和车队管理的结合。田纳西州州长比尔·李也表示支持，强调Waymo的技术在交通运输创新和经济增长方面的潜力。

Waymo鼓励有兴趣的人士在其网站上注册以获取最新信息，了解纳什维尔的发布情况，并表达将Waymo引入自己城市的意愿。

---

## 27. 哦，不，又来一篇关于NPM供应链攻击的冥想。

**原文标题**: Oh no, not again a meditation on NPM supply chain attacks

**原文链接**: [https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/](https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/)

无法访问文章链接。

---

## 28. 如何让 Framework 桌面运行得更安静

**原文标题**: How to make the Framework Desktop run even quieter

**原文链接**: [https://noctua.at/en/how-to-make-the-framework-desktop-run-even-quieter](https://noctua.at/en/how-to-make-the-framework-desktop-run-even-quieter)

本文详细介绍了如何降低Framework Desktop迷你电脑的噪音，重点在于散热改进。最初，Framework Desktop已经受益于猫头鹰NF-A12x25风扇和一个定制风扇导管。为了进一步降低噪音，猫头鹰试验了一个定制侧面板，该侧面板采用了其标志性的风扇格栅设计（为符合安全法规而进行了修改）和一个漏斗状的风扇导管。

测试表明，与原装设置相比，这种定制侧面板和导管组合显著降低了噪音，在50%风扇转速下噪音降低了约7分贝(A)，在更高风扇转速下噪音降低了高达5分贝(A)，同时保持了相同的APU温度。

虽然没有计划批量生产定制侧面板和导管，但猫头鹰提供了3D CAD文件供用户自行3D打印，可在Printables.com上获取。

进一步的实验，包括添加一个NF-A8 PWM排气风扇，证明对噪音水平不利，尽管温度略有降低。虽然NF-A12x25 G2风扇提供了一些声学优势，但与原始的HS-PWM版本相比，其较低的最大速度牺牲了极端条件下的性能空间。

文章总结说，降低噪音最有效的方法是3D打印并安装定制的侧面板和风扇导管。其他修改可能会损害性能或引入不必要的噪音。

---

## 29. 丹麦推广疫苗后，有望消除致癌HPV病毒株

**原文标题**: Denmark close to wiping out cancer-causing HPV strains after vaccine roll-out

**原文链接**: [https://www.gavi.org/vaccineswork/denmark-close-wiping-out-leading-cancer-causing-hpv-strains-after-vaccine-roll-out](https://www.gavi.org/vaccineswork/denmark-close-wiping-out-leading-cancer-causing-hpv-strains-after-vaccine-roll-out)

丹麦全国研究显示HPV疫苗接种显著降低HPV16/18感染率

---

## 30. 代数类型并不可怕

**原文标题**: Algebraic Types are not Scary

**原文链接**: [https://blog.aiono.dev/posts/algebraic-types-are-not-scary,-actually.html](https://blog.aiono.dev/posts/algebraic-types-are-not-scary,-actually.html)

本文解释了代数数据类型 (ADTs) 这一简单实用的概念。它介绍了将类型视为可能值的集合的观点，从而使 ADT 概念更直观。

文章涵盖了两种主要的 ADT 类型：乘积类型和和类型。乘积类型将多个类型组合成一个新类型，该类型包含每个类型的值（如结构体或元组，产生 N * M 个可能的值）。和类型表示一种可以包含一种类型或另一种类型的值的类型（产生 N + M 个可能的值），例如 `Option` 或 `Result` 类型，这些类型对于处理潜在的空值或错误很有用。

作者认为，缺乏对 ADT 的一流支持会导致不太优雅的解决方案、增加认知负荷，甚至导致错误。文章通过 Java 和 Go 的示例说明了这一点。

最后，文章提供了一个使用 OCaml 中的 ADT（和类型）构建算术表达式解释器的实际示例。然后，它将这种方法与替代的面向对象解决方案（继承和访问者模式）进行比较，强调 ADT 与模式匹配通常更简洁、可读且易于维护，因为它们避免了这些模式引入的意外复杂性。

---

## 31. 施乐怀旧网

**原文标题**: XeroxNostalgia.com

**原文链接**: [https://xeroxnostalgia.com/](https://xeroxnostalgia.com/)

XeroxNostalgia.com 是一个致力于保存施乐公司历史的网站，特别是其早期的复印机和油印机。该网站包含关于各种施乐机器、研究中心、制造地点和纪念品的文章、图片和信息。

该网站突出了该公司在静电复印（在普通纸上进行复印的工艺）方面的先锋作用，并感谢施乐档案管理员 Ray Brewer 提供了许多图片。它展示了施乐产品的时间线，包括 914 型号之前的机器、System 123、2202、10 系列和 50 系列，以及它们的发布情况和规格。

该网站还包括施乐历史档案馆的虚拟之旅，并介绍了施乐在世界各地的研究中心。 访客可以在该网站的 YouTube 频道上浏览旧的施乐广告，甚至可以将他们以前或现在的施乐办公地点添加到地图中。

该网站邀请用户通过分享他们自己关于旧施乐复印机/油印机的图片和宣传册来为该系列做出贡献。它还概述了静电复印的历史及其重要性。

---

## 32. AMD Vulkan 开源驱动项目已停止。

**原文标题**: AMD Open Source Driver for Vulkan project is discontinued

**原文链接**: [https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416](https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416)

2025年9月15日，AMD宣布停止其开源AMDVLK Vulkan驱动项目。为了统一其Linux Vulkan驱动策略，AMD将全力支持RADV驱动，将其定位为Linux上Radeon显卡的官方支持的开源Vulkan驱动。

此举旨在简化开发工作，并将资源集中在一个高性能代码库上。AMD鼓励开发者和用户使用并贡献于RADV驱动。

该声明引发了评论区的一些问题。用户询问了对Windows上的AMDPAL和ROCm的影响，澄清回复表明，基于代码库，其功能将继续存在。其他人则希望确认AMD是否会将更多工程资源分配给RADV。

有人提出了RADV未来是否有可能登陆Windows的问题，并提及了关于该主题的持续工作和演示。还有一个问题是关于专业版Vulkan驱动的状态。

总而言之，AMD正在整合其Linux Vulkan驱动工作，通过停止AMDVLK并全力支持RADV，旨在实现更专注和高效的开源开发方法。 这旨在改善Radeon GPU上的开源Vulkan支持，特别是对于Linux用户。

---

## 33. z3入门傻瓜教程

**原文标题**: A dumb introduction to z3

**原文链接**: [https://asibahi.github.io/thoughts/a-gentle-introduction-to-z3/](https://asibahi.github.io/thoughts/a-gentle-introduction-to-z3/)

本文是使用z3求解器的入门介绍，特别关注Rust绑定。文章首先定义了什么是求解器——一种基于给定规则和约束来解决问题的工具——以及它们在现实世界中的应用，如调度和资源分配。作者阐明了z3特定的术语，如“Sort”（意为类型）和“constants”（求解器使用的变量）。

然后，本文逐步介绍了几个复杂度递增的例子，从求解简单的代数方程，如“x + 4 = 7”开始。 逐步发展到求解具有两个变量的方程组，突出显示了`Int`（整数）和`Real`类型之间的区别，以及类型选择如何影响可满足性。作者演示了如何使用`solutions`方法为诸如“x * x = 4”和“x*x + y*y = 25”之类的方程找到多个解。

本文接着讨论了找零问题，并介绍了用于优化问题的`Optimize`对象。 它强调了约束（例如，非负硬币计数）对于获得有意义的解决方案的重要性。最后，本文提供了一个使用z3解决数独问题的起点，但没有包含完整的解决方案。还演示了使用`push`和`pop`来管理跨多个类似问题的断言。

---

## 34. Waymo已获得在旧金山国际机场（SFO）进行商业运营的试点许可。

**原文标题**: Waymo has received our pilot permit allowing for commercial operations at SFO

**原文链接**: [https://waymo.com/blog/#short-all-systems-go-at-sfo-waymo-has-received-our-pilot-permit](https://waymo.com/blog/#short-all-systems-go-at-sfo-waymo-has-received-our-pilot-permit)

Waymo计划于2026年与Lyft合作在纳什维尔推出自动驾驶叫车服务。纳什维尔的乘客将可以通过Waymo应用程序呼叫完全自动驾驶的Waymo车辆。随着服务的成熟，Waymo车辆也将通过Lyft应用程序提供，整合到Lyft现有的叫车平台中。这表明双方旨在扩大Waymo自动驾驶技术的可用性和可及性，以覆盖更广泛的用户群体。该公告发布于2025年9月17日，表明Waymo致力于将其自动驾驶叫车业务扩展到现有服务区域以外。

---

## 35. 我自制了一部手机，因为现在的创新令人沮丧[视频]

**原文标题**: I built my own phone because innovation is sad rn [video]

**原文链接**: [https://www.youtube.com/watch?v=qy_9w_c2ub0](https://www.youtube.com/watch?v=qy_9w_c2ub0)

该YouTube视频名为“我自制了一部手机，因为现在的创新令人沮丧”，可能展示了创作者尝试自制智能手机的过程。标题暗示了对当前智能手机创新的不满，表明其渴望探索替代性且可能更具创新性的移动技术方法。

然而，提供的内容（“YouTube关于新闻版权联系我们创作者广告开发者条款隐私权政策与安全YouTube 的运作方式测试新功能NFL Sunday Ticket© 2025 Google LLC”）仅仅是YouTube的页脚信息，没有提供关于手机制造项目或创作者对当前智能手机创新的具体不满的任何细节。

因此，总结只能包含：该视频探讨了创作者因对当前智能手机创新状态不满而进行的手机制造项目。 除此之外，无法从提供的内容中得出关于手机功能、制造过程或创作者具体批评的更多信息。

---

## 36. DataTables CDN中断 - 事后回顾

**原文标题**: DataTables CDN Outage – post incident review

**原文链接**: [https://datatables.net/blog/2025/july-29-outage](https://datatables.net/blog/2025/july-29-outage)

2025年7月29日DataTables.net宕机事件事后回顾：本次宕机由域名劫持攻击导致。攻击者通过社工手段欺骗域名注册商，提交欺诈性文件，此前他们通过垃圾邮件淹没了所有者的邮箱，以掩盖转移确认请求。这使得他们能够重定向域名的域名服务器，导致主站点、支持论坛以及关键的DataTables CDN下线。

虽然DataTables服务器和用户数据保持安全，但CDN中断严重影响了依赖其Javascript和CSS资源的用户，影响了数百万次请求。 迅速部署了一个临时镜像CDN（datatables-cdn.com）来缓解问题。 在向注册商提供所有权证明后，最终恢复了域名。 但是，DNS传播延迟仍然给某些用户带来问题。

作者对针对提供免费服务的开源项目的攻击表示失望，并强调了网络安全意识的重要性。 采取的立即行动包括优先处理来自域名注册商的电子邮件和添加DNS监控。 未来的计划包括开源CDN服务器设置并改进整体安全监控。 敦促用户对外部资源使用子资源完整性（SRI），并考虑自托管文件以增加安全性。 作者感谢域名注册商和CloudFlare的协助，并感谢DataTables社区在危机期间的支持。

---

## 37. 伯特兰·罗素致奥斯瓦尔德·莫斯利 (1962年)

**原文标题**: Bertrand Russell to Oswald Mosley (1962)

**原文链接**: [https://lettersofnote.com/2016/02/02/every-ounce-of-my-energy/](https://lettersofnote.com/2016/02/02/every-ounce-of-my-energy/)

本文介绍著名思想家伯特兰·罗素于1962年1月写给英国法西斯联盟创始人奥斯瓦尔德·莫斯利的一封信。时年89岁的罗素在信中回复了莫斯利的来信，以坚定和原则性的态度拒绝任何关联。

文章着重介绍了罗素作为哲学家、数学家、逻辑学家、活动家、历史学家和诺贝尔奖获得者的多重成就，强调了他一生致力于反对法西斯主义等意识形态。他将莫斯利的精神气质描述为“格格不入”和“令人厌恶”，并列举了他对与法西斯主义相关的“残酷偏执、强迫性暴力和虐待狂式迫害”的坚定反对。

罗素强调了他们情感世界之间深刻且不可调和的差异，并断言他们的交往不会产生任何富有成效或真诚的互动。他强调了他的信念的强度，解释说他的反对源于他对人类经验和成就中珍视的价值观。 他最后表示，他的拒绝并非出于粗鲁，而是源于他的核心信念。 本质上，这封信有力地宣告了罗素对他价值观的坚定承诺，以及对法西斯主义的坚决抵制。

---

## 38. 美国投资者与特朗普接近达成TikTok对华协议

**原文标题**: U.S. investors, Trump close in on TikTok deal with China

**原文链接**: [https://www.wsj.com/tech/details-emerge-on-u-s-china-tiktok-deal-594e009f](https://www.wsj.com/tech/details-emerge-on-u-s-china-tiktok-deal-594e009f)

无法访问文章链接。

---

## 39. 联合国顶级法律调查员得出结论：以色列在加沙犯有种族灭绝罪

**原文标题**: Top UN legal investigators conclude Israel is guilty of genocide in Gaza

**原文链接**: [https://www.middleeasteye.net/news/un-concludes-israel-guilty-genocide-gaza](https://www.middleeasteye.net/news/un-concludes-israel-guilty-genocide-gaza)

联合国巴勒斯坦和以色列问题调查委员会得出结论，以色列在加沙犯有种族灭绝罪，这是迄今为止联合国机构发布的最权威的声明。这份72页的报告发现，以色列犯下了1948年《灭绝种族罪公约》禁止的五项行为中的四项，有证据表明以色列领导人意图摧毁加沙的巴勒斯坦人作为一个群体。

该委员会由前联合国人权事务高级专员纳维·皮莱担任主席，其调查结果采用了国际法院（ICJ）设定的法律标准。该报告确认的种族灭绝行为包括杀害巴勒斯坦人、造成严重伤害、施加旨在摧毁该群体的生活条件以及阻止生育。报告引用摧毁加沙最大的生育诊所作为阻止生育的一个例子。

该报告强调了以色列当局的种族灭绝意图，引用了赫尔佐格总统和内塔尼亚胡总理等领导人的声明。它确定了支持这一推论的六种行为模式，包括大规模杀戮、文化破坏、蓄意制造痛苦、医疗保健系统崩溃、性暴力和针对儿童。

该委员会呼吁联合国成员国停止向以色列转让武器，并对参与种族灭绝或煽动种族灭绝的人实施制裁。它强调所有国家都有义务防止种族灭绝，并敦促英国审查其立场。该报告将于10月提交联合国大会。

---

## 40. 容器文件系统工作原理：从零构建类似 Docker 的容器

**原文标题**: How Container Filesystem Works: Building a Docker-Like Container from Scratch

**原文链接**: [https://labs.iximiuz.com/tutorials/container-filesystem-from-scratch](https://labs.iximiuz.com/tutorials/container-filesystem-from-scratch)

本教程解释了容器文件系统的工作原理，演示了如何使用 Linux 工具（如 `unshare`、`mount` 和 `pivot_root`）从头开始构建类似 Docker 的容器。它着重于将挂载命名空间作为容器文件系统隔离的核心，其他命名空间则发挥辅助作用。

文章首先阐述了挂载命名空间隔离了挂载表，允许不同的进程拥有不同的文件系统视图。然后深入探讨了挂载传播，解释了其在控制挂载事件如何在命名空间之间共享的重要性，并对比了直接使用 `unshare()` 系统调用与 `unshare` 命令的行为。 `unshare` 命令行工具使用 `mount --make-rprivate /` 来防止挂载传播，从而完全隔离新的挂载命名空间。

本教程涵盖了私有、共享和从属挂载传播类型。目标是提供容器文件系统隔离，并促进应用程序需要在主机上挂载文件系统或在容器内检测主机挂载的文件系统的场景。

文章随后开始设置一个基本的容器，创建根文件系统目录并将 Alpine 镜像提取到其中，为下一步的容器内文件系统隔离做准备。

---

## 41. 三星870 QVO 4TB SATA SSD固态硬盘：使用四年后的表现如何？

**原文标题**: Samsung 870 QVO 4TB SATA SSD-s: how are they doing after 4 years of use?

**原文链接**: [https://ounapuu.ee/posts/2025/09/15/samsung-870-qvo/](https://ounapuu.ee/posts/2025/09/15/samsung-870-qvo/)

本文是对作者在家用服务器和备份驱动器设置中使用四块三星 870 QVO 4TB SATA SSD 四年经验的回顾。这些硬盘于 2021 年购入，作为硬盘驱动器的更安静、更快速替代品，总体表现良好，作者仅注意到一个小的 Linux 内核问题。 即使在持续写入工作负载期间，它们也能保持预期的速度，并且性能明显优于更便宜的 SATA SSD。

虽然其中一块硬盘报告了 4 个坏块，但其通电时间最短，总体硬盘健康状况仍然良好。 S.M.A.R.T 数据显示剩余寿命约为 94%，已写入超过 170TB，远低于三星声明的 1440TBW 耐用性限制。

作者指出，虽然价格已从最初的每块硬盘约 400 欧元降至约 270 欧元，但降幅并不像最初预期的那么大。 虽然存在来自其他制造商的更便宜的 4TB SSD，但作者质疑它们与 870 QVO 相比的持续写入性能。

作者最后提供了每块硬盘的 smartctl -ax 输出，并邀请读者订阅以获取更多技术技巧。 他们还分享了联系方式和其他感兴趣的帖子。

---

## 42. 赞颂闲暇 (1932)

**原文标题**: In Praise of Idleness (1932)

**原文链接**: [https://harpers.org/archive/1932/10/in-praise-of-idleness/](https://harpers.org/archive/1932/10/in-praise-of-idleness/)

在《赞美闲暇》中，伯特兰·罗素认为现代工业社会对工作的过度重视对其自身不利。他挑战了闲暇天生有罪的传统观念，提出广泛减少工作时间对于幸福和繁荣至关重要。

罗素驳斥了富人从事工作会抢占他人工作的说法，指出消费收入会创造就业。他批评储蓄，尤其是在政府战争或不成功的工业企业上的投资，认为它可能比慈善支出更有害。

他将工作定义为操纵物质或指示他人这样做，并注意到两者在薪酬和声望上的差异。罗素将对工作的推崇追溯到前工业时代，那时大众的劳动支撑着少数特权阶层。他认为，现代技术已经使我们能够以大大减少的劳动时间来满足每个人的基本需求，正如战时所证明的那样。

罗素以针的制造为例，说明了技术发达社会中过度工作的荒谬性。当生产力提高时，社会往往不是减少工作时间，而是创造失业和痛苦。

他认为，适量的工作，足以贡献自己的一份力量给社会，是一种责任。然而，期望工薪阶层过度工作是有害的。罗素认为，如果每个人都减少工作时间，就会有足够的资源供所有人使用，但富人抵制这种想法，因为他们怀疑穷人是否有能力明智地利用休闲时间。他断言，休闲对于文明和教育至关重要，并且凭借现代技术，现在可以公平地分配它。

---

## 43. 为C++辩护

**原文标题**: In Defense of C++

**原文链接**: [https://dayvster.com/blog/in-defense-of-cpp/](https://dayvster.com/blog/in-defense-of-cpp/)

Dayvi Schuster 的《为 C++ 辩护》一文驳斥了对该语言的常见批评，并断言其在现代技术领域仍然具有相关性和强大功能。 该文章反驳了 C++ 过度复杂、过时且不安全的说法。

关于复杂性，Schuster 认为，虽然 C++ 具有许多特性，但开发人员无需掌握所有特性即可编写有效的代码。 可读性和可维护性比坚持所谓的“最佳”方法更重要。

针对“过时”的说法，作者指出 C++20 和 C++23 等持续开发和新标准引入了现代特性。 该语言仍然广泛应用于游戏开发、高性能计算和操作系统等关键应用中。

关于“不安全”的论点，特别是与 Rust 相比的内存安全性，文章通过强调代码质量和重写过程中的重新设计，对于提高安全性而言，比语言本身更重要来反驳这一观点。 作者承认，如果使用不当，C++ 可能是不安全的，但建议使用智能指针和其他工具来降低风险。 此外，任何语言在被滥用时都可能产生不安全的代码。

Schuster 强调，C++ 代码可以写得清晰明了，并主张谨慎使用 C++ 特性，甚至建议最初将 C++ 视为 C，仅在需要时才引入复杂性。 虽然 C++ 有一个庞大的生态系统，但作者建议优先使用标准库，并研究维护良好的替代方案，以避免像 Boost 这样的过时库。

最后，文章认为 C++ 不一定是初学者的糟糕选择，并建议学习其基础知识从长远来看是有益的。 结论是，C++ 仍然是一种至关重要的语言，尤其是在对性能要求严苛的领域，并且可以与 Rust 等语言共存。

---

## 44. 立方体卫星是引人入胜的太空学习工具。

**原文标题**: CubeSats are fascinating learning tools for space

**原文链接**: [https://www.jeffgeerling.com/blog/2025/cubesats-are-fascinating-learning-tools-space](https://www.jeffgeerling.com/blog/2025/cubesats-are-fascinating-learning-tools-space)

本文探索了立方星这个迷人的世界。立方星是一种小型、标准化的卫星，由树莓派等设备驱动，被用作学习空间技术的便捷工具。文章定义了立方星，强调了它们相对于传统卫星的成本效益，并讨论了它们作为具有挑战性的工程项目的吸引力。

作者强调了建造立方星，及其严格的尺寸、重量和功率限制，如何迫使硬件和软件设计进行创新性的问题解决，重点关注安全和高效的资源管理。文章介绍了参与立方星开发的人员和项目，包括“Build a CubeSat”的 Manuel 和 Ethos Labs 的 Tim 及其强调安全的“T.E.M.P.E.S.T. 立方星”。

文章还展示了 MySat Kit 和 RASCube 等用于 STEM 教育的教育立方星套件。文章重点介绍了学生建造的即将发射的立方星项目“SilverSat”，并讨论了业余无线电在立方星通信中的作用。文章提供了跟踪卫星的资源，强调了太空探索的可及性以及立方星社区富有感染力的热情，最后还提供了一个展示更多立方星硬件的奖励视频。

---

## 45. 关于 iOS 15.8.5 和 iPadOS 15.8.5 的安全性内容

**原文标题**: About the security content of iOS 15.8.5 and iPadOS 15.8.5

**原文链接**: [https://support.apple.com/en-us/125142](https://support.apple.com/en-us/125142)

本文档详细介绍了2025年9月15日发布的iOS 15.8.5 和 iPadOS 15.8.5 的安全内容。苹果通常不会透露安全漏洞，直到调查完成且修复可用。此次更新修复了 ImageIO 中的一个安全漏洞，具体来说是一个越界写入问题，该问题可能导致在处理恶意图像文件时出现内存损坏。苹果承认此漏洞可能已被用于针对特定个人的定向攻击。

修复方案涉及改进边界检查以防止越界写入。此安全更新适用于一系列旧设备，包括 iPhone 6s（所有型号）、iPhone 7（所有型号）、iPhone SE（第 1 代）、iPad Air 2、iPad mini（第 4 代）和 iPod touch（第 7 代）。该漏洞的识别码为 CVE-2025-43300。

---

## 46. 我们应该排干大沼泽地吗？

**原文标题**: Should we drain the Everglades?

**原文链接**: [https://rabbitcavern.substack.com/p/should-we-drain-the-everglades](https://rabbitcavern.substack.com/p/should-we-drain-the-everglades)

无法访问文章链接。

---

## 47. 正序语法规则与call/cc不动点证明

**原文标题**: Normal-order syntax-rules and proving the fix-point of call/cc

**原文链接**: [https://okmij.org/ftp/Scheme/callcc-calc-page.html](https://okmij.org/ftp/Scheme/callcc-calc-page.html)

本文探讨了`call/cc`（call-with-current-continuation）的不动点，并使用卫生Scheme宏作为lambda演算的证明助手。核心论点在一个定理中形式化，该定理指出，涉及重复应用`call/cc`自身、将`call/cc`应用于恒等函数以及自应用的表达式，当应用于值`p`时，在按值调用（CBV）延续传递风格（CPS）转换后，会产生beta等价的项。

作者证明了虽然`(call/cc call/cc)`和`(lambda (x) (x x))`通常不等价，但它们在特定上下文中，如应用于值时，会变得可观察等价。然后，本文深入研究，使用作为Scheme宏实现的CPS转换来证明该定理。

为了提高CPS转换后代码的可读性，作者使用`syntax-rules`开发了一个beta范式化器。提出了两种方法：一种基于Hilsdale-Friedman正规序beta范式化器，另一种是新型的直接风格lambda计算器，该计算器实现为单个宏。直接风格计算器使用显式替换，并避免过早的alpha重命名或替换。最后，本文将规范化过程直接集成到CPS转换宏中，展示了两者之间的协同作用。使用已开发的工具证明了关键引理，从而支持关于`call/cc`不动点的主要定理。

---

## 48. 泄露视频显示Meta雷朋AR眼镜采用Lumus波导结构

**原文标题**: Meta RayBan AR glasses shows Lumus waveguide structures in leaked video

**原文链接**: [https://kguttag.com/2025/09/16/meta-rayban-ar-glasses-shows-lumus-waveguide-structures-in-leaked-video/](https://kguttag.com/2025/09/16/meta-rayban-ar-glasses-shows-lumus-waveguide-structures-in-leaked-video/)

本文讨论了一段泄露的Meta即将推出的单目AR眼镜的视频，预计该眼镜将于9月17日在Meta Connect上发布。作者Karl Guttag认为，这款眼镜，传闻名为“Celest”，售价约为800美元，采用了Lumus波导技术。

Guttag指出，泄露视频中可见的对角线“板条”是Lumus 2-D瞳孔扩展技术的证据，并将它们与Rivet的AR眼镜中的类似特征进行了比较，后者也使用Lumus波导。他预计在扎克伯格的演示中可以看到Lumus波导。

文章还提到了Guttag将于2025年9月23日至25日在荷兰埃因霍温举行的MicroLED和AR/VR Connect大会上发表讲话。他提供折扣码“KarlARVR”，供他的读者虚拟或亲自参加会议。该会议提供“虚拟通行证”和“混合通行证”选项，提供在线内容、社交机会，并可能提供现场参会机会。

---

## 49. 我再次通过将Python换成英语，在ARC-AGI上获得了最高分。

**原文标题**: I got the highest score on ARC-AGI again swapping Python for English

**原文链接**: [https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again](https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again)

无法访问文章链接。

---

## 50. 用户界面中的“你的”与“我的”

**原文标题**: "Your" vs. "My" in user interfaces

**原文链接**: [https://adamsilver.io/blog/your-vs-my-in-user-interfaces/](https://adamsilver.io/blog/your-vs-my-in-user-interfaces/)

本文探讨了在用户界面中引用用户的项目或操作时，如何优化使用“你的”与“我的”。文章首先质疑在诸如“我的账户”或“你的账户”的例子中，哪个前缀更好，并提出通常根本不需要前缀，因为上下文已经很明显。

然而，文章深入探讨了区分属于用户和其他人的项目是必要的场景，例如在案例管理系统中。它反对使用“我的案例”，因为在主要导航菜单之外的上下文中，如入职流程、电子邮件通知或支持对话中，这可能会导致混淆。在这些情况下，（其他人说的）“前往我的案例”会变得模棱两可。

作者主张在大多数用户沟通中使用“你的”（“前往你的案例”），但提供了一个关键的例外：当用户与系统进行*沟通*时，例如在单选按钮或表单选择中，则首选“我的”。 例如，“分享我的个人资料”比“分享你的个人资料”更清晰。

总而言之，文章建议当系统与用户沟通关于他们的信息或操作时，使用“你的”，而当用户与系统交互以指定他们自己的信息或操作时，使用“我的”。文章最后提供了一个表单设计课程的推广链接。

---

## 51. 发布HN：Rowboat (YC S24) – 多智能体系统的开源IDE

**原文标题**: Launch HN: Rowboat (YC S24) – Open-source IDE for multi-agent systems

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

Rowboat (YC S24) 发布开源 IDE，用于构建多智能体系统。它允许用户使用自然语言快速创建 AI 智能体和自动化工作流程。主要功能包括一键式工具集成、由文档上传驱动的 RAG 能力、带有触发器和操作的自动化工作流程，以及通过 API 或 SDK 进行的灵活部署。

用户可以通过设置 OpenAI 密钥、克隆 Rowboat 仓库并运行启动脚本（需要 Docker）来快速入门。然后可以在 localhost:3000 访问该应用程序。

Rowboat 提供原生 RAG 支持，允许使用像 OpenRouter 和 LiteLLM 这样的自定义 LLM 提供商，并支持添加工具和事件触发器（例如，Gmail、Slack）。它还提供 API 和 SDK，用于将 Rowboat 智能体集成到现有应用程序中。

本次发布包括会议准备助手、客户支持助手和个人助手等演示，展示了该平台的功能。用户可以通过详细的文档了解如何使用 Rowboat 构建智能体。 同时也提供托管的云版本，可立即使用。

---

## 52. AI 在预测术后致命并发症方面优于医生

**原文标题**: AI fares better than doctors at predicting deadly complications after surgery

**原文链接**: [https://hub.jhu.edu/2025/09/17/artificial-intelligence-predicts-post-surgery-complications/](https://hub.jhu.edu/2025/09/17/artificial-intelligence-predicts-post-surgery-complications/)

约翰·霍普金斯大学研究人员开发出一种人工智能（AI）模型，该模型能以比医生目前使用的风险评估方法更高的准确性预测致命的术后并发症。 该人工智能分析来自常规心电图（ECG）的数据，识别肉眼无法检测到的细微信号，这些信号能强烈预测术后30天内心脏病发作、中风或死亡。

该团队利用来自37,000名患者的术前心电图数据训练了两个人工智能模型。 一个模型仅使用心电图数据，而“融合”模型则将心电图数据与患者的病历（如年龄、性别和现有疾病）相结合。 融合模型在预测术后并发症方面达到了令人印象深刻的85%准确率，显著优于现有风险评分，后者的准确率仅约为60%。

研究人员认为，这项技术可以改变外科决策，从而使医生和患者之间能够就手术的风险和益处进行更知情的对话。 他们现在计划在更大的数据集上进一步测试该模型，并对接受手术的患者进行前瞻性研究。 该团队还旨在探索使用人工智能可以从心电图结果中提取哪些其他有价值的信息。

---

## 53. 在每个Entra ID租户中获取全局管理员权限

**原文标题**: Obtaining Global Admin in Every Entra ID Tenant

**原文链接**: [https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/](https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/)

作者发现 Entra ID 中存在一个严重漏洞，该漏洞可能允许未经授权访问全球任何 Entra ID 租户。该漏洞源于两个问题：Microsoft 用于服务间通信的未记录的“Actor 令牌”，以及旧版 Azure AD Graph API 未能验证这些令牌的来源租户的缺陷。

本质上，作者可以在其自己的测试租户中请求一个 Actor 令牌，并使用它来模拟任何其他租户中的任何用户，包括全局管理员。Actor 令牌绕过了条件访问策略，使得即使是强化的租户也容易受到攻击。由于 Azure AD Graph API 缺乏全面的日志记录，因此该漏洞允许攻击者访问用户数据、组信息、租户设置、应用程序详细信息、设备信息和 BitLocker 密钥，而不会留下任何痕迹。

入侵全局管理员将授予完整的租户控制权，允许访问 Microsoft 365 服务（如 SharePoint Online 和 Exchange Online）以及 Azure 资源。攻击者可以创建具有提升权限的新帐户、将凭据添加到现有应用程序或泄露敏感数据。

作者向 Microsoft 报告了该漏洞，Microsoft 迅速修复了该漏洞并发布了 CVE-2025-55241。虽然 Microsoft 未检测到任何滥用行为，但作者提供了一个 KQL 检测查询，供管理员搜索潜在的利用痕迹。该攻击依赖于利用缺乏对租户 ID 的验证以及找到有效的 `netId` 来生成恶意令牌的能力。

---

## 54. Irssi：Docker镜像中的IRC客户端

**原文标题**: Irssi: IRC client in a Docker image

**原文链接**: [https://hub.docker.com/_/irssi](https://hub.docker.com/_/irssi)

好的，以下是基于我从 Docker Hub 页面标题以及 Docker 化 Irssi 等应用程序的常见做法推断出的 Irssi Docker 镜像的摘要：

**摘要：**

此 Docker 镜像提供了一种方便且隔离的方式来运行 Irssi IRC 客户端。 您可以使用此预构建镜像在容器内运行 Irssi，而无需直接在主机操作系统上安装 Irssi。 这提供了几个优点，包括：

*   **简化设置：** 避免依赖冲突并简化安装。 您无需担心手动安装 Irssi 及其依赖项。
*   **可移植性：** 可以在支持 Docker 的不同操作系统（Linux、macOS、Windows）上一致地运行相同的镜像。
*   **隔离性：** Irssi 在沙盒环境中运行，防止它干扰系统上的其他应用程序，反之亦然。
*   **配置管理：** 可能支持环境变量或卷挂载来定制 Irssi 的配置（例如，服务器设置、用户身份、脚本）。 即使重新创建容器，这也能实现持久配置。

Docker Hub 页面可能提供了有关如何拉取镜像、运行它以及配置 Irssi 以连接到所需 IRC 网络的说明。 它也可能详细说明如何使用 Docker 卷来持久化 Irssi 配置和日志，这样在容器停止或删除时，您就不会丢失它们。 常见的用法将包括从 Docker Hub 拉取镜像，配置 Irssi（通常通过环境变量或配置目录的卷映射），并在分离模式下运行容器以使 Irssi 在后台运行。

---

## 55. “私有化溢价”：英国能源账单数十亿英镑流入股东囊中

**原文标题**: 'Privatisation premium': billions from UK energy bills paid to shareholders

**原文链接**: [https://www.theguardian.com/politics/2025/sep/17/privatisation-premium-billions-from-uk-energy-bills-paid-to-shareholders](https://www.theguardian.com/politics/2025/sep/17/privatisation-premium-billions-from-uk-energy-bills-paid-to-shareholders)

本文重点强调了英国能源部门私有化给英国能源消费者带来的巨大经济负担。智库Common Wealth的一项分析显示，2024年英国平均能源账单的很大一部分（24.2%）都流向了大型能源公司的税前利润，而非用于再投资。

该研究进一步表明，自私有化以来，能源公司在2010年至2025年间至少向股东支付了707亿英镑的股息。批评人士认为，这种“私有化溢价”导致更高的账单，并阻碍了对可再生能源基础设施的投资。能源网络的利润率也很高，超过了富时350指数的平均水平。

该报告将当前的私有化系统与公共所有制时代进行了对比，声称相对于GDP而言，当时的投资更高，从而促进了创新和基础设施发展。公共所有制的倡导者认为，能源作为一项至关重要的服务，应优先考虑公共利益而非股东股息。

尽管能源公司辩称其受监管的回报对于吸引私人投资和电网现代化是必要的，但本文指出，英国的能源价格在欧洲名列前茅。公众对国有化的支持增加以及工党政府的行动表明，人们可能会逐渐放弃私有化的共识。公共所有制的拥护者认为，它可以降低成本，推动对清洁能源的投资，并重新获得公众对能源转型的认可。

---

## 56. 当求职变得不可能时

**原文标题**: When the job search becomes impossible

**原文链接**: [https://www.jeffwofford.com/wp/?p=2240](https://www.jeffwofford.com/wp/?p=2240)

本文探讨了长期求职带来的令人沮丧的体验，将其分解为三个不同的阶段：显而易见却不可能的搜索，接近不可能的搜索，以及怪异搜索。

第一阶段，求职者不知疲倦地申请自己有资格胜任的职位，却鲜有回应，导致精疲力竭。第二阶段涉及将搜索范围扩大到相邻的角色、行业或地点，通常需要妥协。虽然这有时会奏效，但也可能失败，导致接近不可能的搜索倦怠（AISB）。第三阶段，“怪异搜索”，探索非常规的职业道路，例如创业或重返校园。

作者承认每个阶段固有的挫败感和疲惫感，最终导致搜索倦怠（BOOS），这是一种精神和情绪上的疲劳状态，个人甚至厌倦了思考求职。

作者没有提供具体的解决方案，而是提供了安慰和视角。他们强调求职者并不孤单，并承认失业对幸福感产生的重大负面影响。文章虽然没有淡化困境，但强调大多数人最终会从失业中恢复过来并找到新的机会，强调了人类的韧性和足智多谋。关键的建议是优先考虑休息。真正的休息，包括独处、参与活动和深度阅读，可以让大脑充电，探索新的可能性，并最终找到前进的道路，这表明有时最好的搜索方式就是根本不搜索。

---

## 57. AI芯片初创公司Groq融资7.5亿美元，估值69亿美元

**原文标题**: AI Chip Startup Groq Raises $750M at $6.9B Valuation

**原文链接**: [https://www.bloomberg.com/news/articles/2025-09-17/ai-chip-startup-groq-raises-750-million-at-6-9-billion-valuation](https://www.bloomberg.com/news/articles/2025-09-17/ai-chip-startup-groq-raises-750-million-at-6-9-billion-valuation)

AI芯片初创公司Groq Inc. 获得 7.5 亿美元融资，投后估值达 69 亿美元。 这笔投资突显了投资者对解决当前人工智能芯片和算力短缺问题的公司抱有巨大信心。 本轮融资由 Disruptive 领投，Blackrock Inc.、Neuberger Berman Group LLC、德国电信资本合伙公司等主要参与者以及三星电子、思科系统、D1 和 Altimeter 等现有投资者也做出了重大贡献。 一家“总部位于美国西海岸的大型共同基金”也参与其中。 Groq 的 PetaOp 级架构，用于其张量流处理器，是推动投资者兴趣的关键因素。 该公司旨在利用其创新技术缓解人工智能工作负载处理的瓶颈。

---

## 58. 结核病如何影响维多利亚时期的时尚 (2016)

**原文标题**: Tuberculosis shaped Victorian fashion (2016)

**原文链接**: [https://www.smithsonianmag.com/science-nature/how-tuberculosis-shaped-victorian-fashion-180959029/](https://www.smithsonianmag.com/science-nature/how-tuberculosis-shaped-victorian-fashion-180959029/)

本文探讨了肺结核与维多利亚时代时尚之间令人惊讶的联系。在19世纪中期，当肺结核达到流行病级别时，这种疾病的症状却产生了矛盾的浪漫化效果。消瘦、苍白的皮肤、红润的脸颊和放大的瞳孔，所有这些肺结核的症状，都成为了美的标准。像尖头胸衣和化妆技巧这样的时尚潮流，都旨在模仿这种“肺痨时尚”。

然而，罗伯特·科赫在1882年发现引起肺结核的细菌以及细菌理论的兴起，改变了人们的看法。公共卫生运动侧重于预防肺结核的传播，并将时尚选择作为目标。长而拖地的裙子被认为不卫生，容易收集细菌，而胸衣则因限制肺功能而受到批评。甚至男士的面部毛发，如胡须和髭，也因可能藏匿细菌而受到审查，导致其受欢迎程度下降。

虽然“肺痨”审美逐渐消失，但肺结核的影响依然存在。较短的裙边导致人们更加关注鞋子的款式，而最初被视为肺结核治疗方法之一的日光浴，则促进了美黑的兴起。本文揭示了一种致命疾病如何深刻地影响了时尚和美的标准，突显了维多利亚时代科学、公共卫生和流行文化之间的交集。

---

## 59. 适用于Windows的全新Google实验性应用

**原文标题**: A new experimental Google app for Windows

**原文链接**: [https://blog.google/products/search/google-app-windows-labs/](https://blog.google/products/search/google-app-windows-labs/)

Google正在通过其Labs项目推出一款Windows实验性应用，旨在提供更快捷的信息访问，而不会中断工作流程。 通过按下Alt + 空格键，用户可以立即搜索他们的电脑文件、已安装的应用、Google Drive文件和网络。 该应用集成了Google Lens，允许用户选择和搜索屏幕上的任何内容，用于图像和文本翻译或作业帮助等任务。 此外，该应用还具有AI模式，可提供更深入、由AI驱动的答案，并提供后续问题和相关链接。 用户可以通过选择加入Labs项目中的实验来试用该应用。

---

## 60. 最“令人讨厌”的CSS特性：cos() 和 sin()

**原文标题**: The "most hated" CSS feature: cos() and sin()

**原文链接**: [https://css-tricks.com/the-most-hated-css-feature-cos-and-sin/](https://css-tricks.com/the-most-hated-css-feature-cos-and-sin/)

本文深入探讨CSS三角函数的实际应用，特别是`sin()`和`cos()`，旨在消除它们是“最令人讨厌”的CSS功能的看法。

文章首先使用单位圆解释`cos()`和`sin()`的基本原理，展示了这些函数如何将角度映射到笛卡尔坐标，分别返回X和Y坐标。

然后，文章展示了三个实际用途：

1.  **圆形布局：** 说明如何使用`cos()`和`sin()`将元素均匀地定位在圆形或半圆形周围，创建圆形菜单或其他视觉上吸引人的排列，而无需依赖魔法数字。
2.  **波浪形布局：** 解释了如何利用`cos()`和`sin()`的振荡特性来创建波浪形图案和交织多个元素链，并通过一个视觉效果惊艳的英雄横幅示例进行演示。
3.  **阻尼振荡动画：** 详细介绍了如何通过结合阻尼常数、频率和偏移等概念，使用`cos()`模拟阻尼振荡（如弹跳球或衰减弹簧）。文章提供了数学公式，以及用于实现的CSS变量。

作者鼓励读者尝试这些函数，并挑战“最令人讨厌”的称号，强调了创造性和动态布局的潜力。

---

## 61. 通过虚假谷歌电话、伪造谷歌邮件和认证同步骗取 13 万美元

**原文标题**: Scammed out of $130K via fake Google call, spoofed Google email and auth sync

**原文链接**: [https://bewildered.substack.com/p/i-was-scammed-out-of-130000-and-google](https://bewildered.substack.com/p/i-was-scammed-out-of-130000-and-google)

文章详述了作者遭遇诈骗的经历，通过冒充谷歌的电话、伪造的谷歌邮箱地址和恶意授权同步等复杂的手段，被骗走了 13 万美元。 诈骗始于一个自称是谷歌支持的电话，提醒作者其谷歌广告帐户存在可疑活动。 诈骗者随后使用伪造的谷歌电子邮件地址进一步确认威胁的真实性。

至关重要的是，作者被骗通过恶意授权同步授予诈骗者对其 Google 帐户的访问权限。 这使得诈骗者能够创建和批准欺诈性广告，从而有效地利用作者的 Google Ads 帐户来花费大量资金。 作者反复授权这些请求，最初认为他们是在批准“谷歌支持”建议的合法更改。

文章强调了诈骗的复杂性，利用看起来逼真的沟通方式和技术操作来获得作者的信任并访问敏感信息。 作者强调谷歌显然缺乏有效的安全措施来预防和检测此类欺诈活动，特别是滥用授权同步。 这篇文章是一个警示故事，讲述了诈骗者不断演变的策略以及用户的潜在脆弱性，即使是那些通常精通技术的人。 它还质疑像谷歌这样的大型科技公司在保护用户免受此类攻击方面的责任。

---

## 62. Gmail邮件传递子系统被用于垃圾邮件传递，绕过过滤器

**原文标题**: Gmail Mail Delivery Subsystem Being Used for Spam Delivery Bypassing Filters

**原文链接**: [https://old.reddit.com/r/GMail/comments/1mulonu/mail_delivery_subsystem_spam/](https://old.reddit.com/r/GMail/comments/1mulonu/mail_delivery_subsystem_spam/)

无法访问文章链接。

---

## 63. 中央情报局信息自由法电子阅览室

**原文标题**: CIA Freedom of Information Act Electronic Reading Room

**原文链接**: [https://www.cia.gov/readingroom](https://www.cia.gov/readingroom)

无法访问文章链接。

---

## 64. 插件系统

**原文标题**: Plugin System

**原文链接**: [https://iina.io/plugins/](https://iina.io/plugins/)

IINA的插件系统于1.4.0版本引入，允许用户使用JavaScript扩展媒体播放器的功能。该系统赋予用户对播放的控制权、访问mpv API的权限、网络和文件系统操作能力，以及自定义UI元素创建能力。"Official User Scripts" 插件进一步简化了自定义，用户可以直接粘贴代码片段而无需打包插件。

插件系统的关键功能包括控制播放和访问状态信息（Core），使用mpv API（MPV），响应事件（Event），发送HTTP请求（HTTP），管理播放列表（Playlist），创建自定义字幕下载器（Subtitle），添加菜单项（Menu），在视频上覆盖自定义网页内容（Overlay），添加侧边栏标签页（Sidebar View），显示独立窗口（Standalone Window），控制多个播放器实例（Global Controller），文件访问（File），存储偏好设置（Preferences），显示系统对话框和运行可执行文件（Utils），以及日志记录（Console）。

IINA安装包包含一个 `iina-plugin` 命令行工具，以帮助插件的创建、构建和运行。包含教程和API参考的完整文档可在 docs.iina.io 找到。还提供了插件API的TypeScript定义，简化开发。用户可以通过输入“iina/iina-plugin-userscript”来安装Official User Scripts插件。

---

## 65. UTF-8 历史 (2003)

**原文标题**: UTF-8 history (2003)

**原文链接**: [https://doc.cat-v.org/bell_labs/utf-8_history](https://doc.cat-v.org/bell_labs/utf-8_history)

本文记录了UTF-8的创建过程，纠正了一个常见的误解，即它是由IBM设计并由Plan 9实现的。Rob Pike回忆说，他和Ken Thompson在1992年9月的一个晚上设计了UTF-8。

故事始于Pike和Thompson对Plan 9的原始UTF的不满。他们接到了可能来自IBM的个人的联系，这些人参与了关于他们的FSS/UTF设计的X/Open委员会会议。看到创造更好标准的机会，Pike和Thompson提出了他们自己的设计。Thompson设计了位打包方案，他们向X/Open展示了他们的纲要，并被接受。

然后，他们迅速在Plan 9上实现了UTF-8，Thompson编写了编码/解码代码，而Pike修改了C和图形库。到周五，Plan 9已完全运行在UTF-8上。他们的设计优于FSS/UTF的关键优势在于，能够在运行中同步字节流，而不会消耗超过一个字符。

通过档案发现的Russ Cox的电子邮件提供了佐证。他提到了1992年9月4日实施的代码更改，并包含了显示早期草案以及与X/Open的通信的电子邮件。这些电子邮件揭示了一个快速的设计和实现过程，并且最初的提案显示出与原始X/Open设计的相似之处，但进行了重大改进。Pike特别记得Thompson在最初的设计会议期间在餐垫上涂写。

---

## 66. 隐式ODE求解器并非总是比显式ODE求解器更稳健。

**原文标题**: Implicit ODE solvers are not universally more robust than explicit ODE solvers

**原文链接**: [https://www.stochasticlifestyle.com/implicit-ode-solvers-are-not-universally-more-robust-than-explicit-ode-solvers-or-why-no-ode-solver-is-best/](https://www.stochasticlifestyle.com/implicit-ode-solvers-are-not-universally-more-robust-than-explicit-ode-solvers-or-why-no-ode-solver-is-best/)

Christopher Rackauckas的文章挑战了一种普遍的观念，即隐式ODE求解器普遍比显式求解器更稳健。作者认为，虽然隐式方法通常因其稳定性而受到青睐，尤其是在显式方法表现出不稳定（如振荡）的情况下，但这并非总是如此。

该论点的核心在于使用线性测试方程`u' = λu`分析ODE求解器的行为。隐式方法，如隐式欧拉法，在复平面上具有更大的稳定区域，可以防止解决方案在应该收敛到零时发散到无穷大。然而，同样的性质也会导致过度阻尼，从而在真实解涉及振荡时导致不准确的结果。

作者用一个冷却问题来说明这一点，其中显式方法由于步长过大而产生虚假振荡，而隐式方法提供了更稳定（但并非完全准确）的解决方案。然而，当应用于简单的谐波振荡器时，隐式方法的阻尼效应会显著扭曲振荡行为，突出了其“稳健性”的局限性。

文章强调，理解ODE的性质对于选择合适的求解器至关重要。当稳定性至关重要时，隐式方法是有利的，但对于振荡是固有的系统，显式方法可能更合适，过度阻尼将是不利的。因此，没有一种ODE求解器是普遍优越的；最佳选择取决于具体问题。

---

## 67. 猪头牌工厂再现令人毛骨悚然的肉类问题，引国会关注

**原文标题**: Repeat creepy meat problems at Boar's Head plants draw congressional scrutiny

**原文链接**: [https://arstechnica.com/health/2025/09/repeat-creepy-meat-problems-at-boars-head-plants-draw-congressional-scrutiny/](https://arstechnica.com/health/2025/09/repeat-creepy-meat-problems-at-boars-head-plants-draw-congressional-scrutiny/)

Congressional lawmakers are expressing serious concerns about Boar's Head's food safety practices after inspections at multiple facilities revealed alarming sanitation issues similar to those found at the Jarratt, Virginia plant, the source of a deadly Listeria outbreak last year. The outbreak, linked to liverwurst produced at the Jarratt facility, sickened 61 people, hospitalizing 60 and resulting in 10 deaths.

Despite Boar's Head's promise to clean up its act after the initial outbreak and closure of the Jarratt plant, subsequent inspections at facilities in Arkansas, Indiana, and another Virginia location uncovered problems like mold, condensation, meat residue, and poor hygiene practices. These findings have led Rep. Rosa DeLauro and other Congress members to question the safety of reopening the Jarratt plant.

In a letter to Boar's Head COO Larry Helfant, the lawmakers accused the company of "repeated pattern of food safety negligence" and requested Helfant testify before the Congressional Food Safety Caucus to address the issues. They expressed a lack of confidence that the Jarratt plant could safely reopen, citing the company's apparent disregard for food safety and public health.

Boar's Head, in a statement, acknowledged the Listeria outbreak as an unprecedented event in their history and claimed to have taken aggressive steps to prevent recurrence. However, the company did not respond to specific questions about the lawmakers' letter or the issues identified at the other facilities.


---

## 68. I just want an 80×25 console, but that's no longer possible

**原文标题**: I just want an 80×25 console, but that's no longer possible

**原文链接**: [https://changelog.complete.org/archives/10881-i-just-want-an-80x25-console-but-thats-no-longer-possible](https://changelog.complete.org/archives/10881-i-just-want-an-80x25-console-but-thats-no-longer-possible)

生成摘要时出错

---

## 69. Learn x86-64 assembly by writing a GUI from scratch (2023)

**原文标题**: Learn x86-64 assembly by writing a GUI from scratch (2023)

**原文链接**: [https://gaultier.github.io/blog/x11_x64.html](https://gaultier.github.io/blog/x11_x64.html)

生成摘要时出错

---

## 70. The Linux Process Journey (2023) [pdf]

**原文标题**: The Linux Process Journey (2023) [pdf]

**原文链接**: [https://thelearningjourneyebooks.com/wp-content/uploads/2023/09/TheLinuxProcessJourney_v6_Sep2023.pdf](https://thelearningjourneyebooks.com/wp-content/uploads/2023/09/TheLinuxProcessJourney_v6_Sep2023.pdf)

生成摘要时出错

---

## 71. Hosting a website on a disposable vape

**原文标题**: Hosting a website on a disposable vape

**原文链接**: [https://bogdanthegeek.github.io/blog/projects/vapeserver/](https://bogdanthegeek.github.io/blog/projects/vapeserver/)

生成摘要时出错

---

## 72. Show HN: A PSX/DOS style 3D game written in Rust with a custom software renderer

**原文标题**: Show HN: A PSX/DOS style 3D game written in Rust with a custom software renderer

**原文链接**: [https://totenarctanz.itch.io/a-scavenging-trip](https://totenarctanz.itch.io/a-scavenging-trip)

生成摘要时出错

---

## 73. Wait4X allows you to wait for a port or a service to enter the requested state

**原文标题**: Wait4X allows you to wait for a port or a service to enter the requested state

**原文链接**: [https://github.com/wait4x/wait4x](https://github.com/wait4x/wait4x)

生成摘要时出错

---

## 74. Wind turbine blade transportation challenges

**原文标题**: Wind turbine blade transportation challenges

**原文链接**: [https://spectrum.ieee.org/wind-turbine-blade-transport-plane](https://spectrum.ieee.org/wind-turbine-blade-transport-plane)

生成摘要时出错

---

## 75. Development of the MOS Technology 6502: A Historical Perspective (2022)

**原文标题**: Development of the MOS Technology 6502: A Historical Perspective (2022)

**原文链接**: [https://www.EmbeddedRelated.com/showarticle/1453.php](https://www.EmbeddedRelated.com/showarticle/1453.php)

生成摘要时出错

---

## 76. Writing an operating system kernel from scratch – RISC-V/OpenSBI/Zig

**原文标题**: Writing an operating system kernel from scratch – RISC-V/OpenSBI/Zig

**原文链接**: [https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/](https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/)

生成摘要时出错

---

## 77. Public static void main(String[] args) is dead

**原文标题**: Public static void main(String[] args) is dead

**原文链接**: [https://mccue.dev/pages/9-16-25-psvm](https://mccue.dev/pages/9-16-25-psvm)

生成摘要时出错

---

## 78. Mixed Excitation Linear Predictive (MELP) Vocoders

**原文标题**: Mixed Excitation Linear Predictive (MELP) Vocoders

**原文链接**: [https://melpe.org/](https://melpe.org/)

生成摘要时出错

---

## 79. Scientists uncover extreme life inside the Arctic ice

**原文标题**: Scientists uncover extreme life inside the Arctic ice

**原文链接**: [https://news.stanford.edu/stories/2025/09/extreme-life-arctic-ice-diatoms-ecological-discovery](https://news.stanford.edu/stories/2025/09/extreme-life-arctic-ice-diatoms-ecological-discovery)

生成摘要时出错

---

## 80. Migrating to React Native's new architecture

**原文标题**: Migrating to React Native's new architecture

**原文链接**: [https://shopify.engineering/react-native-new-architecture](https://shopify.engineering/react-native-new-architecture)

生成摘要时出错

---

## 81. Paper Folding Assembly Line [video]

**原文标题**: Paper Folding Assembly Line [video]

**原文链接**: [https://www.youtube.com/watch?v=XhUuhl9iWpQ](https://www.youtube.com/watch?v=XhUuhl9iWpQ)

生成摘要时出错

---

## 82. Teen safety, freedom, and privacy

**原文标题**: Teen safety, freedom, and privacy

**原文链接**: [https://openai.com/index/teen-safety-freedom-and-privacy](https://openai.com/index/teen-safety-freedom-and-privacy)

生成摘要时出错

---

## 83. Global Peace Index 2025

**原文标题**: Global Peace Index 2025

**原文链接**: [https://www.visionofhumanity.org/maps/](https://www.visionofhumanity.org/maps/)

生成摘要时出错

---

## 84. Generative AI as Seniority-Biased Technological Change

**原文标题**: Generative AI as Seniority-Biased Technological Change

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555)

生成摘要时出错

---

## 85. Apple Explains Why Mac Users in the EU Can't Use iPhone Mirroring

**原文标题**: Apple Explains Why Mac Users in the EU Can't Use iPhone Mirroring

**原文链接**: [https://www.thurrott.com/apple/322065/apple-explains-why-mac-users-in-the-eu-cant-use-iphone-mirroring](https://www.thurrott.com/apple/322065/apple-explains-why-mac-users-in-the-eu-cant-use-iphone-mirroring)

生成摘要时出错

---

## 86. Science's answer to the ultimate question: Where do we come from?

**原文标题**: Science's answer to the ultimate question: Where do we come from?

**原文链接**: [https://bigthink.com/starts-with-a-bang/science-answer-ultimate-question/](https://bigthink.com/starts-with-a-bang/science-answer-ultimate-question/)

生成摘要时出错

---

## 87. Cex.C – Comprehensively EXtended C Language

**原文标题**: Cex.C – Comprehensively EXtended C Language

**原文链接**: [https://github.com/alexveden/cex](https://github.com/alexveden/cex)

生成摘要时出错

---

## 88. Micro-LEDs boost random number generation

**原文标题**: Micro-LEDs boost random number generation

**原文链接**: [https://discovery.kaust.edu.sa/en/article/25936/micro-leds-boost-random-number-generation/](https://discovery.kaust.edu.sa/en/article/25936/micro-leds-boost-random-number-generation/)

生成摘要时出错

---

## 89. Java 25 officially released

**原文标题**: Java 25 officially released

**原文链接**: [https://mail.openjdk.org/pipermail/announce/2025-September/000360.html](https://mail.openjdk.org/pipermail/announce/2025-September/000360.html)

生成摘要时出错

---

## 90. React is winning by default and slowing innovation

**原文标题**: React is winning by default and slowing innovation

**原文链接**: [https://www.lorenstew.art/blog/react-won-by-default/](https://www.lorenstew.art/blog/react-won-by-default/)

生成摘要时出错

---

## 91. Mystery in the Moon

**原文标题**: Mystery in the Moon

**原文链接**: [https://engelsbergideas.com/reviews/mystery-in-the-moon/](https://engelsbergideas.com/reviews/mystery-in-the-moon/)

生成摘要时出错

---

## 92. Devenv 1.9: Scaling Nix projects using modules and profiles

**原文标题**: Devenv 1.9: Scaling Nix projects using modules and profiles

**原文链接**: [https://devenv.sh/blog/2025/09/17/devenv-19-scaling-nix-projects-using-modules-and-profiles/](https://devenv.sh/blog/2025/09/17/devenv-19-scaling-nix-projects-using-modules-and-profiles/)

生成摘要时出错

---

## 93. Hypervisor from Scratch

**原文标题**: Hypervisor from Scratch

**原文链接**: [https://github.com/SinaKarvandi/Hypervisor-From-Scratch](https://github.com/SinaKarvandi/Hypervisor-From-Scratch)

生成摘要时出错

---

## 94. ByteDance unveils new AI image model to rival Google DeepMind's 'Nano Banana'

**原文标题**: ByteDance unveils new AI image model to rival Google DeepMind's 'Nano Banana'

**原文链接**: [https://www.scmp.com/tech/big-tech/article/3325058/bytedance-unveils-new-ai-image-model-rival-google-deepminds-nano-banana](https://www.scmp.com/tech/big-tech/article/3325058/bytedance-unveils-new-ai-image-model-rival-google-deepminds-nano-banana)

生成摘要时出错

---

## 95. PyPI Blog: Token Exfiltration Campaign via GitHub Actions Workflows

**原文标题**: PyPI Blog: Token Exfiltration Campaign via GitHub Actions Workflows

**原文链接**: [https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/](https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/)

生成摘要时出错

---

## 96. 60 years after Gemini, newly processed images reveal details

**原文标题**: 60 years after Gemini, newly processed images reveal details

**原文链接**: [https://arstechnica.com/space/2025/09/60-years-after-gemini-newly-processed-images-reveal-incredible-details/](https://arstechnica.com/space/2025/09/60-years-after-gemini-newly-processed-images-reveal-incredible-details/)

生成摘要时出错

---

## 97. Show HN: STT –> LLM –> TTS pipeline in C

**原文标题**: Show HN: STT –> LLM –> TTS pipeline in C

**原文链接**: [https://github.com/RhinoDevel/mt_llm/tree/main/stt_llm_tts-pipeline-example](https://github.com/RhinoDevel/mt_llm/tree/main/stt_llm_tts-pipeline-example)

生成摘要时出错

---

## 98. Microsoft Favors Anthropic over OpenAI for Visual Studio Code

**原文标题**: Microsoft Favors Anthropic over OpenAI for Visual Studio Code

**原文链接**: [https://www.theverge.com/report/778641/microsoft-visual-studio-code-anthropic-claude-4](https://www.theverge.com/report/778641/microsoft-visual-studio-code-anthropic-claude-4)

生成摘要时出错

---

## 99. Which NPM package has the largest version number?

**原文标题**: Which NPM package has the largest version number?

**原文链接**: [https://adamhl.dev/blog/largest-number-in-npm-package/](https://adamhl.dev/blog/largest-number-in-npm-package/)

生成摘要时出错

---

## 100. Death to type classes

**原文标题**: Death to type classes

**原文链接**: [https://jappie.me/death-to-type-classes.html](https://jappie.me/death-to-type-classes.html)

生成摘要时出错

---

