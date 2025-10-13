# Hacker News 热门文章摘要 (2025-10-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 环境变量是个历史遗留的烂摊子：让我们深入了解一下

**原文标题**: Environment variables are a legacy mess: Let's dive deep into them

**原文链接**: [https://allvpv.org/haotic-journey-through-envvars/](https://allvpv.org/haotic-journey-through-envvars/)

Przemysław Kusiak 的文章深入探讨了常常被忽视的环境变量（envvars）领域，揭示了它们的历史遗留特性和怪癖。他解释说，在 Linux 中，环境变量通过 `execve` 系统调用从父进程传递到子进程。该调用接受可执行文件路径、命令行参数和一个环境变量数组作为参数。

虽然大多数工具会继承环境变量，但有些工具（如 `login` 可执行文件）会创建全新的环境。内核将环境变量作为以 null 结尾的字符串转储到堆栈中，然后程序将其复制到自己的数据结构中。文章重点介绍了不同语言如何内部处理环境变量，重点介绍了 Bash（使用带有本地作用域和导出特性的哈希映射堆栈）、glibc（具有线性复杂度的 `getenv` 和 `putenv` 的动态数组）和 Python（与 C 库耦合，可能导致 `os.environ` 和实际环境之间的不一致）。

Kusiak 还介绍了内核允许的宽松格式，这可能导致诸如名称重复和没有等号的条目等问题。他解释了单个变量的大小限制（128 KiB）和总环境的大小限制（2 MiB）。他驳斥了 POSIX 强制要求大写环境变量的误解，澄清说它只是建议标准实用程序使用大写，并为应用程序保留小写名称。他建议使用带下划线的大写字母作为名称，并使用 UTF-8 作为值，以获得广泛的兼容性，但建议坚持使用可移植字符集以获得最大的安全性。他最后呼吁使用 RSS 进行独立博客写作。

---

## 2. Show HN: SQLite Online – 11年独立开发，日活用户1.1万

**原文标题**: Show HN: SQLite Online – 11 years of solo development, 11K daily users

**原文链接**: [https://sqliteonline.com/](https://sqliteonline.com/)

SQLite Online 是一个独立开发的基于网络的 SQLite 编辑器，拥有 11 年的开发历史和 11,000 名日活跃用户。它提供导入、导出和运行功能，以及语法高亮、表格视图、历史记录和数据科学图表功能。图表功能使用自定义查询语言，在 `SELECT` 前加上 `QLINE-`、`QAREA-`、`QBAR-`、`QPIE-` 和 `QBUBBLE-`，以实现数据的可视化表示。它利用了各种开源库，包括 Sql.js、DuckDB、PGLite、Font-Awesome、CodeMirror、Toastify 和 Chart.js。

该平台不断更新，详细的历史记录日志展示了随着时间的推移添加的功能，包括 DuckDB 和 PGLite 集成、虚拟表联合、改进的图表解析器和导出、Ai 帮助、XLSX 导出、OpFS 支持、云保存链接、定期 SQLite WASM 迁移、删除查询大小限制、添加 regexp 函数、改进的 UI/UX、颜色主题、SQLite 服务器共享、Docker 版本、智能导入等等。

用户可以配置设置，例如存储类型（内存、IndexDB、OpFS）、左侧菜单行为、编辑器首选项（自动完成、错误突出显示、AI 建议）、UI 皮肤、表格外观（悬停效果、数字格式）和旧按钮面板可见性。

该平台按“原样”提供，包含一般免责声明，并强调用户对上传内容以及遵守数据隐私的责任。

---

## 3. NanoChat - 100美元能买到的最佳ChatGPT

**原文标题**: NanoChat – The best ChatGPT that $100 can buy

**原文链接**: [https://github.com/karpathy/nanochat](https://github.com/karpathy/nanochat)

NanoChat：一个极简的全栈类ChatGPT大语言模型，旨在单台8XH100节点上以约100美元的成本运行。`speedrun.sh`脚本自动化整个流程，包括分词、预训练、微调、评估、推理和网络服务。大约4小时后，用户可以通过简单的Web界面与他们自己的大语言模型交互。

该项目旨在使大语言模型更易于访问，强调简洁性、可读性和可破解性，而不是详尽的配置。虽然100美元的预算只能产生一个基础模型，但该项目建议扩展到约300美元或1000美元，以获得更好的性能，与GPT-2相当。这可以通过下载更多数据并减少设备批量大小来管理内存来实现。

该存储库鼓励用户向代码库提问，可以通过将文件打包到大语言模型的提示中或使用DeepWiki来实现。对NanoChat的贡献侧重于改进在有限预算下可访问的微型模型，同时保持代码的最小化和易于理解。该项目受到nanoGPT和modded-nanoGPT的启发，并感谢HuggingFace、Lambda和Alec Radford的贡献。

---

## 4. JSON 河流 - 增量解析流式JSON数据

**原文标题**: JSON River – Parse JSON incrementally as it streams in

**原文链接**: [https://github.com/rictic/jsonriver](https://github.com/rictic/jsonriver)

`jsonriver` 是一个轻量级的 JavaScript 库，用于在 JSON 数据流式传输时对其进行增量解析，从而提供一系列逐渐完整的数值。这允许从网络请求或语言模型等来源处理 JSON，而无需等待整个文档加载完成。

主要特点：

*   **增量解析：** 提供 JSON 值的流，展示 JSON 对象在解析过程中的演变。
*   **轻量快速：** 体积小，无依赖，并利用标准 JavaScript 功能。它专为广泛的兼容性而设计。
*   **正确性：** 保证最终解析的值与 `JSON.parse` 的输出一致。经过广泛的测试，确保符合 JSONTestSuite 标准。
*   **不变性：** 在整个增量更新过程中保持数据类型的一致性，确保可预测的行为。数组会被追加或修改最后一个元素，对象会被添加或修改最近的属性。
*   **应用场景：** 在解析来自网络请求或语言模型等来源的数据流时非常有用。

虽然 `JSON.parse` 在处理完整的 JSON 字符串时速度更快，而 `stream-json` 提供了更多的功能，但 `jsonriver` 在速度和增量处理能力之间取得了平衡，使其适用于需要实时更新或对大型 JSON 文档进行内存高效解析的应用程序。

---

## 5. 聚焦pdfly：PDF文件的瑞士军刀

**原文标题**: Spotlight on pdfly, the Swiss Army knife for PDF files

**原文链接**: [https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html](https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html)

本文介绍pdfly，一个用Python编写的命令行工具，基于fpdf2 & pypdf库，用于处理PDF文件。pdfly由Lucas Cimon维护，提供一系列功能，堪称PDF任务的“瑞士军刀”。它可以显示元数据、合并PDF、删除页面、将图像转换为PDF、压缩文档以及创建小册子。它还包括提取图像和带注释文本的工具。

一个关键特性是`pdfly update-offsets`命令，它通过修复交叉引用表来修复手动编辑的PDF文件。本文宣布发布0.5.0版本，该版本引入了新功能，例如由@moormaster实现的用于签名和验证PDF签名的`pdfly sign`和`pdfly check-sign`。另一项新增功能是由Hal Wine实现的`pdfly extract-annotated-pages`，用于仅提取带有注释的页面。以及Subhajit Sahu实现的`pdfly rotate`，用于旋转特定页面。

本文强调了通过“up-for-grabs”问题进行贡献的机会，并鼓励用户反馈和功能建议，特别是扩展签名功能。目标是使pdfly成为一个更通用和用户友好的PDF文档管理工具。

---

## 6. 2025年 纪念阿尔弗雷德·诺贝尔瑞典国家银行经济学奖

**原文标题**: The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2025

**原文链接**: [https://www.nobelprize.org/prizes/economic-sciences/2025/summary/](https://www.nobelprize.org/prizes/economic-sciences/2025/summary/)

2025年瑞典国家银行纪念阿尔弗雷德·诺贝尔经济学奖授予乔尔·莫基尔、菲利普·阿吉翁和彼得·豪伊特，以表彰他们对理解创新驱动型经济增长所做的贡献。

乔尔·莫基尔因其在识别技术进步推动持续经济增长的必要因素方面的工作而获得一半奖金。他探讨了促进创新的历史和文化条件，强调了思想开放、交流以及支持技术进步的机构的重要性。

菲利普·阿吉翁和彼得·豪伊特因共同发展了关于持续增长的“创造性破坏”理论而共同获得另一半奖金。该理论强调创新不可避免地会扰乱现有产业和技术，从而导致新产业和技术的产生。这种持续的破坏和创造的循环是长期经济繁荣的核心驱动力。

文章导航允许用户访问关于每位获奖者的详细信息，包括摘要、颁奖公告、新闻稿、大众信息和高级信息。它还提供获奖者的视觉呈现。“返回顶部”功能简化了页面内的导航。

---

## 7. Optery (YC W22) – 招聘有Node.js经验的技术主管（美国及拉丁美洲）

**原文标题**: Optery (YC W22) – Hiring Tech Lead with Node.js Experience (U.S. & Latin America)

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22 孵化公司) 正在招聘一位具有 Node.js 经验的技术主管。 该职位面向美国和拉丁美洲的候选人开放。 这是关于 Optery 潜在工作机会的关键信息。 文章可能包含关于公司、职位职责、所需技能和福利的更多细节，但这些信息未包含在提供的文本中。

---

## 8. 最近学到的一些家庭实验室零碎知识

**原文标题**: More random home lab things I've recently learned

**原文链接**: [https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/](https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/)

本文详细介绍了作者最近在家用实验室中的经验和学习，该实验室包含 Proxmox、TrueNAS、Raspberry Pi 以及各种网络组件。他们遇到了一些问题，并分享了他们发现的解决方案。

首先，用作 Proxmox 节点的 Raspberry Pi 5 由于 SD 卡故障而出现严重减速。作者发现 Pi 5 支持通过适配器使用 NVMe SSD，从而显著提升性能。但是，在 SSD 上安装操作系统需要一种解决方法，即修改 Raspberry Pi OS 以启用 PCI-E。

接下来，Pi 5 上的 Proxmox 经历了虚拟机意外的 OOM（内存不足）终止，通过显式设置内核页面大小解决了该问题。他们还指出，ARM 虚拟机需要 OVMF (UEFI) BIOS 才能正常工作。一个有用的技巧是使用 `kpartx` 来挂载 QEMU 虚拟机磁盘以进行调试。

此外，当 ZFS 卷已满时，作者遇到了 Proxmox Backup Server (PBS) 的死锁问题。解决方案是删除 ZFS 快照以释放空间，防止垃圾回收失败。设置了配额以防止将来发生这种情况。

其他见解包括作者找到并使用了 CyberPower UPS 管理软件，在使用 Davis 进行 CALDAV 服务器托管方面获得了积极的体验，以及热衷于使用 Mealie 进行食谱管理，包括贡献了一个小型 PR。他们提倡使用 Mealie 而不是典型的食谱博客，赞扬其结构化格式和组织。

---

## 9. 美国太阳能农场

**原文标题**: American solar farms

**原文链接**: [https://tech.marksblogg.com/american-solar-farms.html](https://tech.marksblogg.com/american-solar-farms.html)

本文详细介绍了美国地面安装太阳能（GM-SEUS）数据集的创建和探索，该数据集全面收集了美国本土48州和哥伦比亚特区公用事业和商业级太阳能发电场的数据。该数据集由来自NOAA、NASA和USGS的研究人员创建，分为阵列和面板两部分。

作者描述了用于分析的强大工作站，包括其CPU、RAM、SSD和操作系统。然后，他们概述了安装必要先决条件的过程，如GDAL和DuckDB以及用于空间和数据操作的各种扩展。

文章的核心集中在使用DuckDB对GM-SEUS数据进行清理、转换和优化。这包括将数据转换为ZStandard压缩的、空间排序的Parquet文件，处理缺失值，以及为每个要素创建几何字段和边界框。作者提供了用于此过程的DuckDB命令。

文章随后探讨了阵列数据集，提供了一个示例记录，总结了每个字段的数据类型和统计信息，并使用H3地理空间索引和ArcGIS Pro生成了资产位置的热图。分析还考察了数据来源、安装年份、安装类型、组件类型和阵列容量之间的关系。最后，作者提供了面板数据集的示例记录和数据统计信息。

---

## 10. Linux 的 MPTCP

**原文标题**: MPTCP for Linux

**原文链接**: [https://www.mptcp.dev/](https://www.mptcp.dev/)

MPTCP (多径TCP) 是标准TCP (RFC 8684) 的扩展，允许设备同时使用多个网络接口进行单次连接，从而聚合带宽、优先选择低延迟路径并提供无缝故障转移。与使用单路径的TCP不同，MPTCP在不同的接口上创建多个“子流”（TCP连接）。

主要用例包括网络间的无缝切换（例如智能手机在Wi-Fi和蜂窝网络之间切换）、基于延迟或成本等因素选择最佳网络，以及聚合来自多个网络的带宽以获得更高的吞吐量。

从技术上讲，MPTCP套接字会创建初始子流，并且可以协商更多子流。TCP头中的 `MP_CAPABLE` 选项表示支持MPTCP。如果远程主机不支持MPTCP，则连接会回退到标准TCP。

该系统使用路径管理器来处理子流创建和地址通告（服务器端），并使用数据包调度器根据配置的策略将数据包分发到各个子流。Linux提供内核内（全局应用规则，通过 `ip mptcp` 管理）和用户空间路径管理器（由守护程序（如 `mptcpd`）管理，规则按连接应用）。数据包调度器负责在可用的子流之间分配数据包。

Linux v6.10 支持 IPPROTO_MPTCP 协议、回退到TCP、内核内/用户空间路径管理、套接字选项和调试功能。MPTCP社区维护的项目包括内核开发、mptcpd守护程序以及对诸如iproute2和Network Manager等工具的MPTCP增强功能。

---

## 11. 人工智能与美国政治的未来

**原文标题**: AI and the Future of American Politics

**原文链接**: [https://www.schneier.com/blog/archives/2025/10/ai-and-the-future-of-american-politics.html](https://www.schneier.com/blog/archives/2025/10/ai-and-the-future-of-american-politics.html)

这篇发表于2025年10月的文章探讨了人工智能在塑造美国政治，尤其是在即将到来的2026年中期选举中，所扮演的多重角色。文章指出主要有三类群体正在利用人工智能：竞选者、组织者和公民。

竞选者正在利用人工智能提高效率，实现诸如筹款请求和定向广告等任务的自动化。虽然看似是现有计算机化的延伸，但人工智能显著地扩展了这些能力，可能甚至会影响到安全的选区竞选。共和党和民主党都在投资人工智能用于竞选活动，但存在资金差距，民主党拥有更多的风险投资支持。

组织者正在探索更激进的应用，从人工智能生成的政治纲领到促进公众审议和公民大会。同时，也有一种将控制权从公司手中转移出来的“公共人工智能”的呼声。工会既在抵制人工智能取代工人的潜力，也在利用它来加强自身的组织工作。

公民正在利用人工智能进行各种活动，包括质疑选民登记（尽管存在争议）以及通过虚假信息检测来维护选举的公正性。更常见的是，人工智能被用于自我表达，例如起草给当选官员的信息。

文章警告说，人工智能破坏选举的潜力不仅仅在于深度伪造，还在于威权政府可能利用人工智能来监视和控制政治言论。作者总结说，人工智能的影响取决于这些不同用途的相互作用以及缺乏监管，因为人工智能公司大力游说反对监管。即将到来的中期选举将受到当前人工智能实验的影响，这将使那些找到有效用途的人获得显著优势。

---

## 12. 加密货币最大清算潮：190亿美元蒸发

**原文标题**: $19B Wiped Out in Crypto's Biggest Liquidation

**原文链接**: [https://decrypt.co/344038/morning-minute-19b-wiped-out-in-cryptos-biggest-liquidation-ever](https://decrypt.co/344038/morning-minute-19b-wiped-out-in-cryptos-biggest-liquidation-ever)

《加密货币最大清算：190亿美元蒸发》这篇文章呈现了加密货币价格的快照。虽然标题暗示了一场巨大的市场事件，但随附的内容主要提供了一个加密货币价格及其在给定时期内的百分比变化的长列表。该列表包括比特币（BTC）、以太坊（ETH）、币安币（BNB）和瑞波币（XRP）等主要加密货币，以及各种较小的山寨币和稳定币。百分比变化反映了涨跌互现的情况，一些代币上涨，另一些代币下跌。值得注意的大幅波动包括COAI下跌35.43%和ATH上涨25.17%。

在没有进一步的背景或分析的情况下，很难充分评估190亿美元清算的含义。所提供的数据仅提供了各种加密货币价格波动的狭隘视角，没有详细说明所谓清算的根本原因或更广泛的市场状况。然而，这份广泛的价格列表可以作为衡量各种代币表现的参考点。

---

## 13. 周末软件更新导致部分Jeep 4xe插电混动版变砖

**原文标题**: Software update bricks some Jeep 4xe hybrids over the weekend

**原文链接**: [https://arstechnica.com/cars/2025/10/software-update-bricks-some-jeep-4xe-hybrids-over-the-weekend/](https://arstechnica.com/cars/2025/10/software-update-bricks-some-jeep-4xe-hybrids-over-the-weekend/)

Jeep牧马人4xe混动车型Uconnect信息娱乐系统最近的一次无线软件更新引发了大范围问题，导致部分车主被困。这次周末推送的更新导致车辆在行驶中失去动力，进而引发动力系统故障，有时甚至是在高速公路上。

受影响的车主已在网上报告了他们的遭遇，详细描述了安装更新后突然失去动力的情况。虽然问题不是立即出现，但它在驾驶过程中显现，使其成为一个更加危险的问题。

在收到大量投诉后，Jeep已撤回了有问题的更新。他们建议尚未安装更新的车主忽略弹出通知，并警告已更新的车主避免使用混合动力或电动模式。修复程序已经发布。该事件凸显了未经充分测试的软件更新的潜在风险，尤其是在星期五下午，正如Crowdstrike之前所展示的那样。Ars Technica已联系Stellantis寻求置评。

---

## 14. 智能手机与当下

**原文标题**: Smartphones and being present

**原文链接**: [https://herman.bearblog.dev/being-present/](https://herman.bearblog.dev/being-present/)

本文探讨了作者对过度使用智能手机的担忧，以及它对活在当下和有意识生活所产生的负面影响。作者引用统计数据表明人们花费大量时间在手机上，并认为这会分散人们对有意义的经历和关系的注意力。

作者详细描述了自己与智能手机使用的斗争，以及为重新掌控局面所采取的策略。这些策略包括通过删除基于推荐的社交媒体应用和积极屏蔽分散注意力的内容（尤其是在YouTube上）来最大限度地降低手机的吸引力。他们禁用了YouTube观看历史记录，以消除算法驱动的推荐，并使用广告拦截器来隐藏短视频和推荐视频。

作者批评了时间限制应用程序的无效性，因为它们无法解决根本的成瘾问题，并且很容易被规避。他们的做法侧重于使手机“尽可能无趣”，从而减少不断查看手机的冲动。虽然承认打破根深蒂固的习惯很困难，但作者强调了他们方法的积极成果：增强的临场感、减少的分心以及更多用于丰富生活的活动的时间。作者认为全球范围内因智能手机而损失的集体时间令人震惊，并且主要用于无益的娱乐。他们提倡读者尝试他们的方法来重新获得时间和注意力，从而过上更充实和乐观的生活。

---

## 15. 无线控制你的佳能相机

**原文标题**: Control your Canon Camera wirelessly

**原文链接**: [https://github.com/JulianSchroden/cine_remote](https://github.com/JulianSchroden/cine_remote)

Cine Remote 是一款应用程序，允许使用佳能相机内置的 WiFi 功能进行无线遥控。目前，它支持佳能 C100II、EOS 70D 和 EOS R7。该应用程序的开发依赖于逆向工程协议，因此可能无法完美处理极端情况。

主要功能包括：搜索支持的相机、配对和记住连接、控制光圈、ISO、快门角度和白平衡、开始/停止录制、图像捕获（有限）、属性更新处理和实时预览。演示模式允许用户在没有支持的相机的情况下试用该应用程序。

支持的相机使用不同的协议。C100II 使用 EosCineHttp，但无法捕获图像。EOS 70D 和 R7 使用 PTP/IP；但是，70D 在启用 WiFi 的情况下无法录制电影。

未来的开发计划包括：改进使用 UPNP 的相机搜索、增加对更多相机的支持（尤其是基于 CCAPI 的 EOS 型号），以及增强错误处理，特别是对于相机断开连接的情况。

---

## 16. 美国迎来人工智能淘金热，而非工厂繁荣

**原文标题**: America is getting an AI gold rush instead of a factory boom

**原文链接**: [https://www.washingtonpost.com/business/2025/10/13/manufacturing-artificial-intelligence/](https://www.washingtonpost.com/business/2025/10/13/manufacturing-artificial-intelligence/)

无法访问文章链接。

---

## 17. 矩阵可以是你的朋友

**原文标题**: Matrices can be your Friends

**原文链接**: [https://www.sjbaker.org/steve/omniv/matrices_can_be_your_friends.html](https://www.sjbaker.org/steve/omniv/matrices_can_be_your_friends.html)

史蒂夫·贝克的《矩阵可以成为你的朋友》一文为初级图形程序员揭开了矩阵的神秘面纱，尤其侧重于它们在OpenGL中的应用。其核心思想是将矩阵可视化为对位于原点的单位立方体的变换。

文章解释说，一个OpenGL矩阵，表示为一个16个元素的数组（m[0]到m[15]），可以通过概念性地将其排列成四列来理解。对于刚体变换，最后一行（m[3], m[7], m[11], m[15]）通常是0、0、0和1，可以暂时忽略。最后一列的前三个元素（m[12], m[13], m[14]）代表平移向量。

剩余的九个元素（前三列的顶部三个）定义了旋转。文章详细介绍了这九个数字如何决定变换后单位立方体的x、y和z轴的新位置。例如，(1,0,0)变为(m[0], m[1], m[2])。然后将平移向量添加到每个变换后的点。

文章进一步阐述了如何通过操纵矩阵元素来实现缩放、剪切和挤压效果，并将矩阵中的变化与可视化立方体的变形联系起来。最后，它解释了“单位”矩阵作为“什么都不做”的变换的功能，使轴保持不变。通过在脑海中可视化立方体，可以避免复杂的数学运算并优化图形变换。

---

## 18. 苹果将“Apple TV+”更名为“Apple TV”

**原文标题**: Apple Renames 'Apple TV+' to 'Apple TV'

**原文链接**: [https://www.apple.com/tv-pr/news/2025/10/apple-original-films-blockbuster-feature-f1-the-movie-from-joseph-kosinski-to-make-global-streaming-debut-on-friday-december-12-2025/](https://www.apple.com/tv-pr/news/2025/10/apple-original-films-blockbuster-feature-f1-the-movie-from-joseph-kosinski-to-make-global-streaming-debut-on-friday-december-12-2025/)

新闻稿宣布，由布拉德·皮特主演、约瑟夫·科辛斯基执导的Apple Original Films电影《F1赛车》，在院线大获成功后，将于2025年12月12日在Apple TV上全球首播。这部电影已经打破纪录，成为有史以来票房最高的体育电影，全球票房超过6.29亿美元。它也是今年票房最高的原创电影，也是布拉德·皮特迄今为止票房最高的电影。

该片讲述了前一级方程式赛车天才索尼·海耶斯（布拉德·皮特饰）的故事，他重返赛场，与新秀约书亚·皮尔斯（达姆森·伊德里斯饰）一起拯救一支苦苦挣扎的车队。该片在实际的F1大奖赛周末拍摄，哈维尔·巴登、凯瑞·康顿和托比亚斯·门基斯也参与演出。

制片人杰瑞·布鲁克海默强调了通过Apple TV的全球影响力将这部电影带给更广泛观众的兴奋之情。新闻稿还强调了《F1赛车专辑》原声带的成功，该专辑的全球播放量已超过10亿次。

重要的是，该新闻稿还宣布“Apple TV+”已更名为“Apple TV”。最后，它指出《F1赛车》也可在Apple TV应用程序和Amazon Prime Video等平台上购买。

---

## 19. A16Z支持的数据公司Fivetran和dbt Labs将以全股票方式合并

**原文标题**: A16Z-backed data firms Fivetran, dbt Labs to merge in all-stock deal

**原文链接**: [https://www.reuters.com/business/a16z-backed-data-firms-fivetran-dbt-labs-merge-all-stock-deal-2025-10-13/](https://www.reuters.com/business/a16z-backed-data-firms-fivetran-dbt-labs-merge-all-stock-deal-2025-10-13/)

无法访问文章链接。

---

## 20. 从百万到十亿

**原文标题**: From Millions to Billions

**原文链接**: [https://www.geocod.io/code-and-coordinates/2025-10-02-from-millions-to-billions/](https://www.geocod.io/code-and-coordinates/2025-10-02-from-millions-to-billions/)

TJ Miller的博文详细介绍了Geocodio从基于MariaDB的请求日志系统到使用ClickHouse、Kafka和Vector构建的可扩展性更强的解决方案的历程。最初，MariaDB搭配TokuDB被用于追踪用户请求以进行计费和调试，但它面临着诸如弃用、大规模性能下降以及缓存击穿风险等问题。

最初的解决方案是用列式数据库ClickHouse替换MariaDB，但大量的单个请求插入压垮了系统，导致了`TOO_MANY_PARTS`错误。随后尝试使用ClickHouse缓冲表只会加剧问题，导致`TOO_MANY_LINKS`错误。

最终的解决方案，灵感来自Honeybadger的架构，引入了Kafka作为事件流平台，用于持久存储和高吞吐量，并引入了Vector作为高性能数据管道，以有效地将数据从Kafka批量传输到ClickHouse。Kafka将生产者（Geocodio的应用程序）与消费者（ClickHouse）解耦，而Vector将消息批量处理成最佳大小，以实现高效的ClickHouse插入，目标是每个批次包含30,000-50,000条记录。这种架构成功解决了扩展问题，并为Geocodio每月处理数十亿次请求做好了准备。

---

## 21. 安卓限制侧载是其迄今为止最反消费者的举措

**原文标题**: Android's sideloading limits are its most anti-consumer move yet

**原文链接**: [https://www.makeuseof.com/androids-sideloading-limits-are-anti-consumer-move-yet/](https://www.makeuseof.com/androids-sideloading-limits-are-anti-consumer-move-yet/)

本文认为，谷歌即将对安卓侧载进行的更改——要求在搭载谷歌移动服务 (GMS) 的设备上安装应用时，开发者必须进行身份验证——是一种反消费者行为，威胁着平台的开放性并阻碍创新。 从 2025 年 10 月开始，并在 2026 年 9 月强制执行，这项更改要求开发者向谷歌验证其身份，才能在大多数主流安卓手机上安装应用，但不包括自定义 ROM 和去谷歌化的设备。

作者批评了谷歌以增强安全性为理由的辩解，指出现有的安全措施，如 Google Play Protect 和用户控制的未知来源阻止功能已经存在。他们认为，要求身份验证并不能保证完整性，甚至可能通过将信任从设备上的警告转移到谷歌的控制上来削弱用户的选择。

这篇文章强调了对 F-Droid、独立开发者和依赖于 Play 商店之外自由分发的 APK 的小众应用社区等生态系统的潜在“附带损害”。作者担心，身份验证带来的摩擦增加和潜在的隐私问题可能会打击开发者，缩小安卓生态系统，并扼杀创新。虽然侧载不会完全消除，但此举创造了一个“强制性的谷歌控制的扼制点”，限制了参与度，并威胁着自由和灵活性，而自由和灵活性一直是安卓吸引力的核心。文章的结论是，虽然存在解决方法，但它们也伴随着权衡，而安卓的开放性无疑正在减弱。

---

## 22. LaTeXpOsEd：预印本档案中信息泄露的系统性分析

**原文标题**: LaTeXpOsEd: A Systematic Analysis of Information Leakage in Preprint Archives

**原文链接**: [https://arxiv.org/abs/2510.03761](https://arxiv.org/abs/2510.03761)

"你已被LaTeXpOsEd：使用大型语言模型对预印本档案库中信息泄露的系统性分析" 这篇arXiv预印本，强调了如arXiv等预印本存储库中的安全漏洞。作者Richard A. Dubniczky、Bertalan Borsos和Tihanyi Norbert展示了对LaTeX源文件的不受限制的访问如何暴露敏感信息。

该研究引入了LaTeXpOsEd，一个结合模式匹配、逻辑过滤、传统收集和大型语言模型（LLM）的四阶段框架，用于检测LaTeX源代码、注释和辅助文件中的隐藏披露。为了评估LLM在秘密检测方面的能力，他们创建了LLMSec-DB，一个用于评估这些模型的基准。

他们的大规模审计分析了来自10万份arXiv提交的超过1.2TB的数据，揭示了大量的信息泄露，包括PII、带有GPS标记的EXIF文件、共享驱动器链接、各种平台的凭据以及机密通信。这些泄露对研究人员和机构构成了严重的名誉和安全风险。

作者强调，研究界和存储库运营商迫切需要解决这些漏洞。在发布他们的脚本和方法以促进开放科学的同时，他们保留了敏感发现，以防止滥用。源代码和相关材料可在他们的项目网站上找到。

---

## 23. CLOCKSS：学术出版商与图书馆运营的数字保存服务

**原文标题**: Clockss: Digital preservation services run by academic publishers and libraries

**原文链接**: [https://clockss.org/](https://clockss.org/)

CLOCKSS：学术内容的长期数字保存合作计划，由学术出版商和研究图书馆共同运营。它利用屡获殊荣的LOCKSS技术，确保书籍、期刊和数字馆藏免受人为错误、计算机攻击和组织失败等潜在威胁。

主要特点包括：

*   **可持续档案：** 当“触发事件”发生时，数字内容将被保存并可访问。
*   **全球协作：** 在全球领先的研究图书馆中设有12个存档节点组成的网络。
*   **优质内容：** 内容由图书馆选择，并由信誉良好的出版商保证。
*   **创新技术：** 使用LOCKSS技术，迁移内容格式以确保可用性。
*   **开放获取：** 为触发的出版物分配知识共享许可，使其公开可用。

CLOCKSS与图书馆、出版商和其他利益相关者合作，以减轻学术内容面临的风险。 作为一个财务安全、独立的非营利组织，它由图书馆和出版商组成的董事会管理。 目前，CLOCKSS拥有6140万篇期刊文章和555,650本书籍，由300家图书馆和656家参与出版商提供支持，确保我们共同知识遗产的保存。

---

## 24. 把一个简易气象站放到互联网上

**原文标题**: Putting a dumb weather station on the internet

**原文链接**: [https://colincogle.name/blog/byo-weather-station/](https://colincogle.name/blog/byo-weather-station/)

科林·科格尔的博文详细介绍了如何使用廉价组件创建一个DIY互联网连接的气象站。该项目从Temu上购买的一个廉价、不起眼的无线温度计开始，该温度计在433 MHz频段上传输温度和湿度数据。然后，他使用RTL-SDR USB加密狗监听这些传输，并使用开源软件`rtl_433`解码数据。

解码后的数据随后被传递到PowerShell脚本，该脚本解析温度和湿度信息。此脚本利用科格尔现有的命令行工具`aprs-weather-submit`将天气数据传输到APRS-IS网络，使其可供业余无线电爱好者使用。他限制了APRS数据包提交的频率，以避免垃圾信息泛滥网络。

除了业余无线电社区，作者还将气象站连接到Mastodon。PowerShell脚本被配置为向为此目的创建的专用Mastodon机器人帐户发送天气更新。他承认，由于是个人在家使用，将Mastodon API令牌硬编码到脚本中的做法不太理想。

文章包括GitHub上`rtl_433`和`aprs-weather-submit`的链接、APRS规范、他在APRS.to上的气象站页面以及Mastodon帐户。该项目展示了使用现成的硬件和开源软件，业余无线电和物联网项目是多么容易访问和定制。

---

## 25. 内存安全的两条路径：CHERI 和 OMA

**原文标题**: Two Paths to Memory Safety: CHERI and OMA

**原文链接**: [https://ednutting.com/2025/10/05/cheri-vs-oma.html](https://ednutting.com/2025/10/05/cheri-vs-oma.html)

本文探讨了两种硬件级别的架构方法，CHERI和OMA，旨在缓解内存安全漏洞，这些漏洞是约70%软件漏洞的根本原因，也是重大网络安全问题的来源。作者引用了英国的许多代价高昂的例子。

CHERI（Capability Hardware Enhanced RISC Instructions，即具有硬件增强功能的RISC指令集）由剑桥大学率先开发，通过硬件强制执行的能力来扩展现有的指令集架构。它使用包含内存地址、边界、权限和有效性元数据的“胖指针”，提供引用和空间安全。一个缺点是指针大小的增加，基本上使内存消耗和带宽翻倍。CHERI中的时间安全是通过基于软件的指针撤销来实现的，这增加了复杂性和验证开销。

OMA（Object Memory Architecture，对象内存架构）由布里斯托大学开发，并由Doubtless Computing公司商业化，它直接在硬件中采用基于对象的内存管理。每个内存分配都变成一个硬件对象，具有自己的身份、边界和由处理器管理的元数据。OMA使用更精简的指针，并将对象信息集中在硬件管理的目录中。一个关键的区别是硬件级别的垃圾回收，它提供了硬件保证的时间安全，以及引用和空间保护。由于硬件优化，OMA还为托管语言带来了显著的性能提升。

虽然CHERI针对嵌入式系统，但OMA面向服务器级和应用程序处理器，在这些处理器中，托管语言很普遍。文章总结说，CHERI和OMA是互补的解决方案，在解决内存安全问题方面针对不同的用例。

---

## 26. 英国通信管理局因违反英国网络安全法对4chan处以两万英镑罚款，且罚款持续累积。

**原文标题**: Ofcom fines 4chan £20K and counting for violating UK's Online Safety Act

**原文链接**: [https://www.theregister.com/2025/10/13/4chan_ofcom_fine/](https://www.theregister.com/2025/10/13/4chan_ofcom_fine/)

本文详述了英国通信管理局（Ofcom）首次根据英国《在线安全法案》对4chan处以罚款，原因是其未遵守有关保护儿童免受有害内容侵害的信息请求。初始罚款为2万英镑，如果4chan继续无视Ofcom对风险评估和收入信息的请求，则可能额外罚款6000英镑。

文章强调，在4chan未能回应4月份的信息请求后，Ofcom于6月份对该平台展开了调查。违反《在线安全法案》的最高罚款为1800万英镑或全球收入的10%。

文章还提到，目前正在对其他在线服务进行调查，例如Im.ge和AVS Group Ltd，分别与儿童性虐待材料和年龄验证有关。科技大臣莉兹·肯德尔强调了《在线安全法案》及其执行的重要性。

虽然一些平台面临处罚，但另一些平台正在采取措施遵守规定。一些文件共享服务通过对英国用户进行地理封锁，避免了进一步的行动，一个自杀论坛也实施了地理封锁。Ofcom还在推动使用哈希匹配技术来打击非法内容的传播。文章最后，Ofcom的执法主管表示，这项罚款发出了一个明确的信息，即必须认真对待《在线安全法案》。

---

## 27. 使普通GPS达到超高精度

**原文标题**: Making regular GPS ultra-precise

**原文链接**: [https://norwegianscitechnews.com/2025/10/making-regular-gps-ultra-precise/](https://norwegianscitechnews.com/2025/10/making-regular-gps-ultra-precise/)

本文探讨了挪威科技大学 (NTNU) 研究人员开发的一项名为 SmartNav 的新技术，该技术旨在提高城市环境中自动驾驶汽车和日常设备的 GPS 精度。由于建筑物造成的信号反射和遮挡，常规 GPS 信号在城市中通常不可靠，从而形成“城市峡谷”。

SmartNav 结合了多种技术来校正 GPS 信号。它使用载波相位定位，通过分析无线电波提供高精度，并且还结合了谷歌的一项新服务，该服务利用其 3D 城市地图来预测和校正信号反射。通过将这些校正与其自身的算法相结合，挪威科技大学的研究人员在特隆赫姆进行的测试中，90% 的时间都达到了 10 厘米以内的精度。

该系统还利用 PPP-RTK（精密单点定位-实时动态），它将全球校正与实时数据相结合，使该技术更易于访问且更经济实惠。这种方法减少了对昂贵的本地基站的依赖，从而可以在大众市场设备中更广泛地实施。SmartNav 提供的更高精度对于自动驾驶汽车在城市环境中安全可靠地导航至关重要，并且有望提高手机和其他消费类设备的 GPS 精度。

---

## 28. 吉普软件更新致车辆变砖，车主被困。

**原文标题**: Jeep software update bricks vehicles, leaves owners stranded

**原文链接**: [https://www.thestack.technology/jeep-software-update-bricks-vehicles-leaves-owners-stranded/](https://www.thestack.technology/jeep-software-update-bricks-vehicles-leaves-owners-stranded/)

Jeep 4xE车型Uconnect系统10月10日（周五）的软件更新出现漏洞，导致大量车辆“变砖”，车主被困，可能面临危险。此次无线（OTA）更新导致车辆失去动力，有时在行驶过程中突然发生，仪表盘上亮起错误信息。

该问题至少影响了2024款Jeep牧马人4xe车型。Jeep客户支持承认了该问题，当天取消了更新，并随后发布了修复OTA，解决了部分问题。然而，最初的更新已经影响了许多用户，一些人报告了危险情况，他们的车辆在高速公路上失去了推进力。据报道，经销商处出现了多辆受影响的车辆，一些经销商向车主收取诊断费用，进一步激怒了客户。

该事件引发了人们对车辆OTA软件更新安全性的担忧，以及制造商远程禁用车辆的潜力，甚至更糟糕的是，恶意行为者也可能这样做。一位受影响的车主描述了一种情况，Jeep完全瘫痪，无法重新启动。另一位车主提到经销商收取高达200美元的维修费用。该事件还突显了软件更新需要进行严格的测试和分阶段推出，CrowdStrike对类似事件的回应就是一个例证，当时一个有漏洞的更新使数百万台计算机瘫痪。

---

## 29. 一些石墨烯公司已从中获益，但另一些公司则举步维艰。

**原文标题**: Some graphene firms have reaped its potential but others are struggling

**原文链接**: [https://www.theguardian.com/business/2025/oct/13/lab-to-fab-are-promises-of-a-graphene-revolution-finally-coming-true](https://www.theguardian.com/business/2025/oct/13/lab-to-fab-are-promises-of-a-graphene-revolution-finally-coming-true)

本文探讨了自2004年石墨烯发现以来，英国石墨烯公司所取得的进展和面临的挑战。 石墨烯从石墨中提取，具有卓越的强度和导电性等特性，但将其潜力从“实验室”转化为“工厂”已被证明是困难的。

一些公司，如剑桥大学的衍生公司2D Photonics，在基于石墨烯的光子微芯片方面取得了成功。 这些芯片有望以显著降低的能耗实现更快的数据传输，目标应用领域包括数据中心、5G 和自动驾驶汽车。 另一家剑桥衍生公司 Paragraf 也凭借基于石墨烯的电子设备蓬勃发展，包括用于电动汽车的传感器和生物传感器。 Graphene Innovations Manchester 与沙特阿拉伯达成了一项协议，生产用于建筑的富含石墨烯的碳纤维。

然而，其他企业则步履维艰。 早期的参与者 Applied Graphene Materials 最终因亏损而被清算。 Versarien 尽管开发了用于各种应用的石墨烯粉末，但面临财务困难，目前正在寻求出售资产，可能面临清算。

文章强调了扩大石墨烯生产规模和满足价格预期以与现有技术竞争的难度。 拜耳碳纳米管工厂的失败凸显了预测市场需求的挑战。 这些公司的经历表明，材料创新需要很长时间才能进入市场，许多公司都在努力实现盈利。 尽管遭遇挫折，但 2D Photonics 和 Paragraf 等公司的成功表明，石墨烯革命正在缓慢实现。

---

## 30. MicroPythonOS – 适用于微控制器的类安卓操作系统

**原文标题**: MicroPythonOS – An Android-like OS for microcontrollers

**原文链接**: [https://micropythonos.com](https://micropythonos.com)

MicroPythonOS 是一款轻量级、多功能的操作系统，专为 ESP32 等微控制器和桌面系统设计。其主要特点是类似于 Android 的触摸屏用户界面，使其直观且用户友好。它包括一个应用商店，方便访问应用程序，以及空中 (OTA) 更新，实现无缝维护和功能添加。

该操作系统具有快速性能和轻量级设计，使其适用于资源受限的设备。它基于原生 MicroPython 构建，简化了开发并确保了跨平台兼容性。除了支持触摸屏和手势识别外，它还支持 IMU 和摄像头。

MicroPythonOS 开辟了各种可能性，包括构建智能家居控制器等物联网设备、创建具有交互式显示屏的教育工具、开发去中心化支付系统、设计便携式触摸屏设备、驱动机器人、打造智能可穿戴设备以及制作 DIY 项目原型。其用户友好性、效率和强大功能的结合使其成为新手和经验丰富的开发人员都极具吸引力的平台。该项目可在 GitHub 上找到。

---

## 31. 使用Pyo3实现的Tauri Python绑定

**原文标题**: Tauri binding for Python through Pyo3

**原文链接**: [https://github.com/pytauri/pytauri](https://github.com/pytauri/pytauri)

PyTauri 提供 Tauri 框架的 Python 绑定，使 Python 开发者能够使用 Web 技术构建跨平台桌面应用程序，无需 Node.js。 利用 Pyo3，它提供 Python 和 Tauri 前端之间快速且安全的通信，消除了进程间通信的开销。

主要功能包括与 tauri-cli 集成以构建可执行文件、对代码保护的 Cython 支持、对 Tauri 插件的支持、原生 asyncio 支持、100% 类型完整性以及镜像 Tauri Rust API 的符合人体工程学的 API。 它会自动生成 TypeScript 类型和用于 IPC 的客户端。 `pytauri-wheel` 包允许在无需 Rust 编译器的情况下进行开发。

该项目提供了示例，演示了与 NiceGUI、Gradio 和 FastAPI 等框架的集成，以实现全栈 Python 开发。 PyTauri 遵循语义化版本控制，保持核心和插件的主要/次要版本号一致。

PyTauri 旨在为 Python 开发者提供类似于 Electron 或 PySide 的全面 GUI 开发体验。 在开发体验方面，它受到了 FastAPI 和 Pydantic 的启发。 该项目还使 Rust 开发者能够更有效地利用 Python 生态系统。 虽然是一个独立的项目，但它尊重 Tauri 的目标和价值。 PyTauri 在 Apache License 2.0 许可下发布。

---

## 32. 沃达丰承认“重大故障”，超过13万用户报告问题

**原文标题**: Vodafone admits 'major outage' as more than 130,000 report problems

**原文链接**: [https://www.bbc.co.uk/news/articles/c5yldldx659o](https://www.bbc.co.uk/news/articles/c5yldldx659o)

沃达丰于2025年10月13日星期一遭遇重大网络中断，影响了英国超过13万用户。此次中断影响了宽带、4G和5G服务，而2G语音通话和短信功能仍然可用。客户报告称，访问移动数据、宽带、沃达丰网站和应用程序均存在困难。问题始于英国夏令时15:00左右，Netblocks证实了影响宽带和移动数据的全国性中断。

此次中断也影响了Voxi和Lebara等使用沃达丰网络基础设施的其他电信公司的客户。沮丧的客户纷纷在社交媒体上表达他们无法工作、访问在线服务以及联系客户服务。

沃达丰对此次不便表示歉意，并表示其网络正在恢复中，但没有说明中断的原因或预计持续时间。Cloudflare Radar指出，沃达丰的流量一度降至零。专家表示，技术故障或配置错误比网络攻击更有可能造成此次中断。

---

## 33. 桃子梗：关于CRT显示器、像素和信号质量（再次）

**原文标题**: The Peach meme: On CRTs, pixels and signal quality (again)

**原文链接**: [https://www.datagubbe.se/crt2/](https://www.datagubbe.se/crt2/)

本文重新审视了作者之前一篇关于CRT和像素艺术的争议性文章，澄清了观点并纠正了常见的误解。作者强调，虽然CRT无疑会通过混合和柔化图像来影响像素艺术的外观，但认为它们完全消除了可见像素的观点是不准确的。信号质量至关重要。

文章批判了流行的“桃子梗”（将放大后的精灵图与模糊的CRT照片进行比较），认为它不能很好地代表CRT的效果，并强调了诸如焦点和未知连接类型等问题。作者提供了使用各种连接（RGB、复合）在CRT和LCD屏幕上的替代比较，展示了信号质量如何显著影响图像清晰度、色彩保真度和模糊程度。特别是复合信号，无论显示器类型如何，都会引入诸如色彩溢出和噪点之类的伪影。

作者还探讨了“索尼克瀑布”效应，认为这主要是由于复合视频的信号质量差，而不是CRT固有的特性。这强调了“CRT优势”梗通常过于简化了信号质量的作用。

文章承认在诸如Game Boy之类的缺乏CRT屏幕的平台上使用了诸如抖动和抗锯齿之类的像素艺术技术，以说明它们在增强感知图像质量方面的重要性。文章还讨论了艺术家如何有意识地针对特定的显示硬件功能，调整技术以在限制范围内工作。

总之，作者认为，虽然CRT会影响像素艺术的外观，但特写照片可能会产生误导，而在正常观看距离处的整体感知才是真正重要的。至关重要的是，信号质量和像素艺术技术是实现视觉质量的关键因素，无论显示技术如何。

---

## 34. gsay：从谷歌获取英语词汇发音

**原文标题**: gsay: Fetch pronunciation of English vocabulary from Google

**原文链接**: [https://github.com/pvonmoradi/gsay](https://github.com/pvonmoradi/gsay)

`gsay` 是一个 shell 脚本，用于从 Google 的发音“答案框”获取并播放英语单词的发音。它使用 `curl` 访问 Google 的搜索结果，然后提取包含发音的 MP3 音频文件的 URL。该脚本随后使用像 `ffplay`、`mpv` 或 `pw-play` 这样的无头 MP3 播放器播放音频。

主要功能包括支持 2020 年和 2024 年的声音文件，提供英式 (`gb`) 和美式 (`us`) 发音。它还实现了缓存机制，用于在本地存储发音，从而提高性能。默认情况下启用缓存，并存储在 `~/.cache/gsay` 中。该脚本接受一个查询字符串（要发音的单词）和几个选项，包括指定发音数据库的年份 (`-y`)、口音 (`-a`)、是否仅打印发音链接而不播放它 (`-l`) 以及是否禁用缓存 (`-n`)。它还包括用于调试 (`-v`) 和显示帮助 (`-h`) 的选项。

该脚本采用启发式方法来提取 MP3 URL，因为由于反爬虫措施，抓取 Google 的搜索结果变得越来越困难。

---

## 35. Show HN: 宝贝的第一个国际长途电话

**原文标题**: Show HN: Baby's first international landline

**原文链接**: [https://wip.tf/posts/telefonefix-building-babys-first-international-landline/](https://wip.tf/posts/telefonefix-building-babys-first-international-landline/)

这个“Show HN”帖子详细介绍了Téléfonefix，一个儿童友好的固定电话系统，用于安全国际通话。它使用实体电话，避免屏幕时间，并连接到运行Asterisk（一个软件PBX）的Raspberry Pi。国际通话通过Twilio以低成本路由。

该系统只允许呼叫预先批准的号码，基于由名为`allo-wed`的自定义Golang程序管理的、可配置的规则集。这包括时区考虑，以避免深夜通话，并可以选择禁用呼入电话。

该设置包括：连接到Grandstream HT801模拟电话适配器的有绳电话，该适配器再连接到Raspberry Pi。需要一个购买了电话号码的Twilio帐户来进行国际通话路由。Ansible用于自动化配置Asterisk、HT801和DHCP服务器。

主要功能包括使用gopipertts为不同通话场景定制语音提示，例如用对方的语言宣布正在呼叫的人。还提供家长覆盖功能。未来的改进包括防止过早挂断、限制通话频率、改进带语音反馈的错误处理，以及可能强制使用扬声器模式。作者提供了代码仓库和有用的指南的链接。

---

## 36. 加州下月将停止使用煤炭发电。

**原文标题**: California Will Stop Using Coal as a Power Source Next Month

**原文链接**: [https://www.latimes.com/california/newsletter/2025-10-08/essential-california-california-dumps-coal-power](https://www.latimes.com/california/newsletter/2025-10-08/essential-california-california-dumps-coal-power)

加州下月将停止从犹他州州际电力公司电厂接收电力，此举标志着该州将结束对煤电的依赖。据《洛杉矶时报》詹姆斯·雷尼的文章报道，这代表了加州在应对气候变化方面迈出的重要一步，转向更便宜、更可靠的风能、太阳能和天然气等能源。

洛杉矶水电局（DWP）发挥了关键作用，减少了从犹他州电厂的电力订单，并在附近建造了一座天然气和氢气燃烧发电站。虽然这项新技术存在环境问题，但人们认为它比煤炭燃烧的风险小得多。

包括纳瓦霍发电站在内的燃煤电厂的关闭，给依赖煤矿开采的社区，如纳瓦霍族，带来了挑战。尽管存在失业问题，但包括迪内族长者劳伦斯·吉尔摩在内的一些人认识到摆脱煤炭对环境的好处。

尽管特朗普政府通过激励措施和土地准入来支持煤炭，但加州仍然致力于更清洁的能源。即使是犹他州的保守派政治家也对这种转变持开放态度。这篇文章还涉及了其他加州新闻，包括潜在的背靠背地震、南加州大学教职员工拒绝特朗普协议以及对州长候选人凯蒂·波特的尖刻采访。

---

## 37. 古代巴塔哥尼亚的狩猎采集者会照顾受伤和残疾的同伴。

**原文标题**: Ancient Patagonian hunter-gatherers took care of their injured and disabled

**原文链接**: [https://phys.org/news/2025-10-ancient-patagonian-hunter-disabled.html](https://phys.org/news/2025-10-ancient-patagonian-hunter-disabled.html)

一项发表在《国际古病理学杂志》上的新研究分析了来自全新世晚期巴塔哥尼亚的189名狩猎采集者的骨骼遗骸，以了解这些非定居群体如何照顾受伤的成员。由维多利亚·罗马诺博士领导的研究人员检查了来自25个考古遗址的3000多件骨骼，发现约20%的个体表现出骨骼创伤。

虽然难以确定受伤的确切原因，但大多数归因于事故而非人际暴力。这些损伤被分为轻度、中度和重症监护，反映了所需的支持程度以及对群体动态的影响。轻度损伤，如鼻骨骨折，在几周内痊愈。中度损伤，如手臂骨折，需要3-5个月的护理，并可能影响日常活动。重症监护损伤占病例的13%，需要至少六个月或终身的护理。

该研究重点介绍了一个严重的髋关节损伤病例，该病例显示出完全愈合的迹象，表明接受了重要的长期护理。这项研究意义重大，因为它是对非定居狩猎采集者中护理行为的首次群体水平分析。虽然早期的证据表明先前的巴塔哥尼亚时期存在护理行为，但这项研究为流动性限制如何影响这些行为提供了宝贵的见解。未来的研究旨在探索护理动态如何随时间演变。

---

## 38. 罗杰·迪恩 – 他在游戏史上的传奇艺术作品 (Psygnosis)

**原文标题**: Roger Dean – His legendary artwork in gaming history (Psygnosis)

**原文链接**: [https://spillhistorie.no/2025/10/03/legends-of-the-games-industry-roger-dean/](https://spillhistorie.no/2025/10/03/legends-of-the-games-industry-roger-dean/)

本文深入探讨了著名艺术家罗杰·迪恩的电子游戏艺术作品，他以与Yes乐队和亚洲乐队等前卫摇滚乐队的标志性合作而闻名。重点是他对游戏行业的贡献，特别是他与英国发行商Psygnosis的长期合作关系。迪恩讲述了他如何通过Henk Rogers（后来因《俄罗斯方块》而闻名）和Psygnosis的Jonathan Ellis参与到这个行业中。

他设计了Psygnosis的标志，包括名称和猫头鹰图像。他的工作通常涉及根据描述来构思游戏的核心内容，从而影响游戏的视觉效果，就像内容影响他的艺术一样。迪恩还为《The Black Onyx》、《Barbarian》和《Shadow of the Beast》等游戏创作了封面，经常与其他艺术家合作，例如Tim White，后者会为他的画作上色。

迪恩讨论了游戏包装的演变，感叹曾经堪比专辑封面的精美游戏盒的消失。他强调了后期CD包装缺乏用心，并将其与日本保持的质量进行了对比。他还提到了他后来参与的《俄罗斯方块》标志设计，以及一个被取消的、更具雄心的《The Black Onyx》续作，为此他组建了一个团队来创作游戏内容和包装。文章强调了迪恩对早期电子游戏视觉形象的重大影响以及他的艺术创作过程。

---

## 39. OpenAI和博通将部署10吉瓦OpenAI设计的AI加速器

**原文标题**: OpenAI and Broadcom to deploy 10 GW of OpenAI-designed AI accelerators

**原文链接**: [https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/)

OpenAI与博通宣布战略合作，专注于部署OpenAI设计的AI加速器，目标总容量为10吉瓦（GW）。这一重大举措标志着OpenAI正在加大对专用硬件的投资，以满足其AI模型日益增长的计算需求。

该合作利用了博通在定制芯片设计和制造方面的专业知识。OpenAI将定义这些AI加速器的架构和规范，专门用于优化其AI工作负载的性能和效率。博通将负责这些芯片的物理设计、制造和测试。

10吉瓦的部署规模巨大，表明OpenAI正在大力加强其基础设施和处理能力。这可能会转化为更快的训练时间、改进的模型性能以及处理更复杂和苛刻的AI任务的能力。

此次合作旨在解决高级AI模型日益增长的资源需求。通过开发定制AI加速器，OpenAI希望更好地控制其计算基础设施，并减少对通用处理器的依赖。这一战略举措应使OpenAI能够优化其AI开发流程，并在快速发展的AI领域保持竞争优势。本质上，这次合作就是OpenAI设计大脑，博通大规模地制造它们。

---

## 40. 超大质量黑洞相互锁定在稳定轨道上

**原文标题**: Supermassive black holes locked in a stable orbit around each other

**原文链接**: [https://www.helsinkitimes.fi/themes/themes/science-and-technology/28090-scientists-capture-first-image-of-two-black-holes-in-orbit.html](https://www.helsinkitimes.fi/themes/themes/science-and-technology/28090-scientists-capture-first-image-of-two-black-holes-in-orbit.html)

**摘要:**

《赫尔辛基时报》报道了科学家首次拍摄到两个超大质量黑洞在稳定且相对接近的轨道上相互运行的图像。 这一发现为星系合并和增长的过程，以及黑洞在该过程中的作用提供了宝贵的见解。

要点包括：

*   **双黑洞系统：** 科学家们直接观测到两个超大质量黑洞在引力作用下相互束缚，彼此绕行。
*   **图像确认：** 这是首次直接拍摄到稳定的、相互绕行的超大质量黑洞对的图像。 以往的证据主要基于间接观测。
*   **星系合并：** 该黑洞对为研究合并星系的动力学提供了一个机会，星系合并是宇宙演化中的一个常见过程。 当星系碰撞时，它们中心的黑洞会沉入中心并形成一个双星系统。
*   **轨道动力学：** 该文章强调了理解黑洞轨道动力学的重要性。 这将有助于预测它们是否最终会合并，释放出引力波。
*   **科学意义：** 这一观测为星系演化和双星结构中超大质量黑洞行为的理论模型和模拟提供了重要的验证。 研究该系统的特征为科学家提供了理解宇宙的重要数据点。

---

## 41. 形式化验证代码在实践中出错的三种方式

**原文标题**: Three ways formally verified code can go wrong in practice

**原文链接**: [https://buttondown.com/hillelwayne/archive/three-ways-formally-verified-code-can-go-wrong-in/](https://buttondown.com/hillelwayne/archive/three-ways-formally-verified-code-can-go-wrong-in/)

本文探讨了形式验证在保证代码无缺陷方面的局限性，尽管它对“正确性”有着精确的定义，即符合规范（“spec”）。虽然形式验证旨在证明代码符合其规范，但作者概述了经过验证的代码在实践中仍然可能失效的三种主要方式：

1. **无效证明：** 证明本身可能存在缺陷，原因在于定理证明器中的错误，或使用了无意中遗留在最终代码中的快捷方式（“直接接受此项”）。
2. **错误属性：** 规范可能无法准确捕捉期望的行为。leftpad 示例说明了这一点，它验证了长度约束，但没有验证 Unicode 字符之间的预期视觉对齐。更强的属性可能难以证明、表达，或者可能取决于用户实际如何使用代码。
3. **错误假设：** 经过验证的代码通常依赖于对环境的假设，例如足够的内存、并发访问和外部服务。如果这些假设被违反，正确性保证将不再有效。这也适用于对未经验证的代码的依赖，其中经过验证的代码的正确性取决于未经验证的代码按预期运行。

作者强调了理解“已证明正确”的代码的特定含义和局限性的重要性。关键是要识别并向团队成员传达假设和局限性，以避免误用并管理对形式验证提供的保证的期望。关键在于，虽然形式验证是一种有价值的工具，但它并不能消除出现 bug 的可能性，对系统及其环境的整体理解至关重要。

---

## 42. Emacs agent-shell (由ACP驱动)

**原文标题**: Emacs agent-shell (powered by ACP)

**原文链接**: [https://xenodium.com/introducing-agent-shell](https://xenodium.com/introducing-agent-shell)

本文介绍了 `agent-shell`，一个由作者构建的 Emacs 软件包，它提供了一个原生的 Emacs shell，用于通过 Agent Client Protocol (ACP) 与 AI 代理进行交互。作者之前开发了 `acp.el` (一个 Emacs Lisp ACP 实现) 和 `chatgpt-shell`，受 ACP 启发，在 Emacs 中创建了一个统一的代理体验。

`agent-shell` 利用 `comint-mode` 获得无缝的 Emacs 缓冲区体验，提供与代理无关的交互。用户可以通过指定代理特定的命令和环境变量来配置不同的代理（例如，Gemini CLI，Claude Code）。

作者还开发了用于检查 ACP 流量的工具，包括用于调试和理解代理通信的流量缓冲区。为了避免不断与付费代理交互的成本和延迟，他们创建了一个“假代理”系统，该系统可以重放来自先前会话的已保存流量，从而实现更快的开发和调试。

作者承认 `agent-shell` 和 `acp.el` 都处于早期版本，并鼓励用户尝试、报告错误和提出功能建议。最后，他们请求从这些工具中受益的用户提供支持，建议用户考虑赞助开发，因为他们可能已经在为 LLM token 使用付费了。

---

## 43. 年度鸟类摄影师大赛教会我们规划和耐心

**原文标题**: Bird photographer of the year gives a lesson in planning and patience

**原文链接**: [https://www.thisiscolossal.com/2025/09/2025-bird-photographer-of-the-year-contest/](https://www.thisiscolossal.com/2025/09/2025-bird-photographer-of-the-year-contest/)

2025年度鸟类摄影师大赛，展现了鸟类摄影的奉献精神和艺术性，其最高奖项授予了利隆·格茨曼，以表彰他精心策划的太阳日食期间拍摄的丽色军舰鸟照片。 本次大赛收到全球超过33,000份参赛作品，通过城市鸟类、最佳肖像和鸟类栖息地等各种类别，突出了各种鸟类行为和栖息地。 获奖者包括施特芬·福斯特拍摄的南方巨海燕特写、卢卡·洛伦茨拍摄的暴风雪中高山兀鹫肖像，以及贝诺伊特·亨里昂拍摄的西方仓鸮。 本次大赛还表彰年轻人才并支持保护工作，捐款给“濒危鸟类”。获奖照片画廊已在线提供，普林斯顿大学出版社正在出版一本相关书籍。 2026年大赛现已开放报名。

---

## 44. 沃顿商学院的西格尔称美国没有稀土储备是可耻的。

**原文标题**: Wharton's Siegel says it's scandalous the US doesn't have a rare earths reserve

**原文链接**: [https://www.cnbc.com/2025/10/13/siegel-says-its-scandalous-the-us-doesnt-have-a-rare-earths-reserve.html](https://www.cnbc.com/2025/10/13/siegel-says-its-scandalous-the-us-doesnt-have-a-rare-earths-reserve.html)

沃顿商学院金融学荣誉退休教授杰里米·西格尔认为，美国应建立稀土战略储备，并称美国缺乏储备“令人愤慨”，尤其是在中国控制着90%稀土提炼的情况下。他认为，这种控制对西方供应链构成长期威胁。

西格尔的提议正值美中贸易紧张关系升级之际，起因是中国可能限制稀土出口。这些矿物对包括智能手机和国防技术在内的各个行业至关重要，并且主要在中国开采和加工。这种依赖性在全球供应链中造成了一个潜在的瓶颈。

西格尔参考了1975年建立的美国战略石油储备，强调需要为稀土元素建立类似的缓冲。尽管市场对特朗普的关税威胁反应消极，但西格尔仍然乐观地认为，美国和中国将在11月1日设定的最后期限前解决贸易冲突。他认为这个最后期限表明特朗普有意进行谈判。他相信，一旦贸易问题得到解决，市场很可能会反弹，并有可能达到新的高度。

---

## 45. WireGuard FPGA

**原文标题**: Wireguard FPGA

**原文链接**: [https://github.com/chili-chips-ba/wireguard-fpga](https://github.com/chili-chips-ba/wireguard-fpga)

本文概述了一个项目，旨在创建一个基于FPGA的Wireguard VPN开源实现，以提供比现有软件和专有硬件解决方案更易用且性能更高的替代方案。该项目旨在克服之前尝试的局限性，例如基于昂贵硬件和专有工具的Blackwire项目。

该项目的目标是在廉价的Artix7 FPGA上开发一个自给自足的Wireguard实现，使用开源工具和通用的SystemVerilog。无需PC主机即可访问。该项目分为几个阶段，首先是概念验证（第一阶段），然后是进一步的优化（第二阶段）。

关键挑战包括硬件/软件划分、协同开发、高速测试以及使用开源工具实现时序收敛。该项目的执行计划涉及一系列“任务”，重点是电路板启动、Wireguard链路实现、嵌入式软件开发、VPN隧道管理以及测试/移植到openXC7。

该架构包括一个在RISC-V CPU上以软件实现的控制平面和一个完全在FPGA上的RTL中实现的数据平面。数据平面处理以太网协议、头部解析、加密/解密 (ChaCha20-Poly1305) 和 IP 查找等任务。软件架构包括 Curve25519、ChaCha20-Poly1305 和 BLAKE2s 等组件，用于密码学功能。最终目标是创建一个社区驱动的高性能Wireguard VPN解决方案。

---

## 46. 亨利埃塔·玛丽亚王后宫廷侏儒杰弗里·哈德森

**原文标题**: Jeffrey Hudson the Court Dwarf of the English Queen Henrietta Maria of France

**原文链接**: [https://en.wikipedia.org/wiki/Jeffrey_Hudson](https://en.wikipedia.org/wiki/Jeffrey_Hudson)

杰弗里·哈德逊（1619-约1682）是17世纪英国法国的亨利埃塔·玛丽亚王后著名的“宫廷侏儒”，被称为“王后的侏儒”和“小不点勋爵”。7岁时，他从一个馅饼中出现，被献给王后，当时身高仅18英寸。他凭借其智慧和宫廷风度成为王后宫廷中的一个显赫人物，以娱乐大众，并曾出现在宫廷假面舞剧中。

哈德逊陪伴王后执行任务，包括一次前往法国的危险航行，他们的船被敦刻尔克海盗俘获。在英国内战期间，他曾担任保皇党的骑兵上尉，后来与王后一同逃往法国。

1644年，他在一场决斗中杀死了威廉·克罗夫茨的兄弟，导致他被逐出王后宫廷，他的生活发生了转变。他被巴巴里海盗俘获，在北非遭受了25年的奴役后被赎回。大约在1669年返回英格兰后，他声称自己在囚禁期间长高了很多。

哈德逊住在奥克姆，后来回到伦敦，因信奉天主教而被短暂监禁。他于1682年左右死于贫困，被埋葬在一个没有标记的贫民墓地。尽管他的人生经历非同寻常，但他仍然是英国历史上一个值得关注的人物，代表了斯图亚特时代宫廷生活中一个独特而复杂的方面。

---

## 47. HTTP3详解

**原文标题**: HTTP3 Explained

**原文链接**: [https://http3-explained.haxx.se](https://http3-explained.haxx.se)

HTTP/3详解是一个旨在记录HTTP/3和QUIC协议的协作项目。 我们诚挚邀请大家贡献力量，共同打造关于这些技术的全面资源。

该文档提供网页版和PDF版，可通过提供的链接（http3-explained.haxx.se）访问。 其主要优势在于内容动态更新，能够反映对底层Git仓库的每一次提交。 这确保了信息的及时性和准确性。

本质上，HTTP/3详解是一个提供HTTP/3和QUIC相关解释和细节的动态文档，鼓励社区参与其开发和维护。 最近一次更新大约在一年前，表明可能需要对其进行审核，以反映最新的协议更改。

---

## 48. 没有科学，就没有创业：我们正在关闭的创新引擎

**原文标题**: No Science, No Startups: The Innovation Engine We're Switching Off

**原文链接**: [https://steveblank.com/2025/10/13/no-science-no-startups-the-unseen-engine-were-switching-off/](https://steveblank.com/2025/10/13/no-science-no-startups-the-unseen-engine-were-switching-off/)

史蒂夫·布兰克在其2025年发表的文章中指出，美国的创新实力源于其强大的科学生态系统，尤其是对大学研究的独特投资。他区分了科学家（理论家和实验家）、工程师、企业家和风险投资家，并解释了他们之间相互关联的作用。科学家受好奇心驱使，探索基本原理，从而在基础科学和应用科学领域取得突破。工程师则以这些发现为基础创造实用的解决方案，而企业家则将它们商业化，通常由风险投资家提供资金。

布兰克强调了大学研究的重要性，它占美国所有基础科学研究的约50%。他将此与1982年后企业研究实验室的衰落进行了对比。大学实验室就像“迷你创业公司”，培养未来的科学家并产生像谷歌搜索和CRISPR这样的创新。他还强调了外籍研究人员的贡献，这一群体正受到移民限制的威胁。

布兰克警告说，削减科学经费将削弱美国经济和国防，使其依赖于那些投资科学的国家。虽然他承认科技公司在人工智能方面的大量投资，但他强调这些投资侧重于工程，而非科学，并且人工智能应该增强而不是取代科学家。他总结说，忽视科学会导致依赖其他国家，并以二战后英国削减科学投资后的衰落以及苏联的解体为例。

---

## 49. 2025年诺贝尔经济学奖

**原文标题**: Nobel Prize in Economic Sciences 2025

**原文链接**: [https://www.nobelprize.org/prizes/economic-sciences/2025/popular-information/](https://www.nobelprize.org/prizes/economic-sciences/2025/popular-information/)

2025年诺贝尔经济学奖授予乔尔·莫基尔、菲利普·阿吉翁和彼得·豪伊特，以表彰他们对理解由技术创新驱动的持续经济增长所作出的贡献。

莫基尔的历史研究强调了“有用知识”持续流动的重要性，其中包括命题性（理解事物为何运作）和规范性（理解事物如何运作）组成部分。他认为，工业革命是由这些知识类型之间的联系，以及熟练的工匠和一个对变革持开放态度的社会推动的，从而克服了来自既得利益的阻力。

阿吉翁和豪伊特开发了一种“创造性破坏”的数学模型，其中公司投资于创新以击败现有产品和流程，从而推动增长。这一过程涉及拥有尖端技术的公司通过专利从临时垄断中获利，从而激励进一步的研发和创新。他们的模型强调了研发激励、家庭储蓄和整体经济增长之间的动态平衡。

该模型还探讨了研发投资的福利效应。虽然创新有益于社会，但它也可能导致“商业窃取”，因为新产品取代旧产品。补贴研发可能是有益的，也可能是有害的，这取决于新知识的社会效益是否超过了取代现有公司的成本。总的来说，他们的工作提供了一个框架，用于理解通过技术进步促进持续经济增长的复杂因素。

---

## 50. Kotlin 编译器中存在多年的土耳其语字母表 Bug

**原文标题**: A years-long Turkish alphabet bug in the Kotlin compiler

**原文链接**: [https://sam-cooper.medium.com/the-country-that-broke-kotlin-84bdd0afb237](https://sam-cooper.medium.com/the-country-that-broke-kotlin-84bdd0afb237)

本文详细介绍了 Kotlin 编译器中一个存在多年的漏洞，该漏洞源于土耳其语字母表对大小写“I”的处理方式如何影响字符串转换。 该漏洞表现为土耳其开发者遇到神秘的构建失败和 `NoSuchMethodError` 异常。

核心问题在于 `CompilerOutputParser` 类，该类将 XML 标签名称（如 `<INFO/>`）转换为小写，以匹配 `CATEGORIES` 映射中的条目。 在土耳其语区域设置中，"INFO".toLowerCase() 结果为 "ınfo"（带有无点“ı”），导致不匹配和编译器错误。

Kotlin 1.3 中引入的协程加剧了这个问题。 编译器使用 `capitalize()` 函数生成 boxing 函数名称，如 `boxInt()`。 但是，在土耳其语区域设置中，`capitalize()` 错误地将 "int" 大写为 "İnt"（带有带点“İ”），导致创建不存在的函数 `boxİnt()` 并导致运行时崩溃。

由于该漏洞发生频率较低，并且假设错误是由于依赖项不匹配造成的，因此该漏洞一直未被发现。 本文强调了在编程中考虑特定于区域设置的行为的重要性，以及调试难以重现的问题的挑战。 最终，该问题被追溯到 Kotlin 编译器中对区域设置敏感的字符串操作。

---

## 51. OpenAI 与博通 [视频]

**原文标题**: OpenAI x Broadcom [video]

**原文链接**: [https://www.youtube.com/watch?v=qqAbVTFnfk8](https://www.youtube.com/watch?v=qqAbVTFnfk8)

提供的文本并非文章，而是YouTube的标准页脚信息。它出现在YouTube页面的页脚中，特别是名为“OpenAI x Broadcom”的YouTube视频的页脚。

文本包括：

*   标准法律和政策链接（版权、联系我们、创作者、广告、开发者、条款、隐私、安全）
*   关于YouTube运营的信息
*   提及测试新功能
*   提到NFL Sunday Ticket，表明平台上可能存在与之相关的内容。
*   版权归属Google LLC。

关键在于背景是关于“OpenAI x Broadcom”的YouTube视频。提供的文本本身并不提供信息，仅指示YouTube页面底部的标准法律样板。要了解视频的实际内容，需要观看它。

---

## 52. 3D打印自动气象站

**原文标题**: 3D-Printed Automatic Weather Station

**原文链接**: [https://3dpaws.comet.ucar.edu](https://3dpaws.comet.ucar.edu)

3D打印自动气象站（3D-PAWS）是由UCAR和美国国家气象局合作，并由美国国际开发署支持的一项倡议，旨在扩展偏远、农村和服务欠缺地区的天气观测网络。该项目能够利用3D打印和现成的传感器在当地建造低成本（300-500美元）的可靠气象站。

目标是提高天气监测密度，通过预警系统降低与天气相关的风险，使当地社区掌握数据收集的所有权，并促进环境传感领域的开源创新。3D-PAWS气象站使用Arduino和Raspberry Pi等平台进行数据处理，测量压力、温度、湿度、风力、降水和光照。

主要优势包括低成本、本地组装和维修以及社区所有权。该系统正在包括美国和国际站点的多个地点进行测试，以评估在各种气候条件下的性能。试点网络已在肯尼亚和巴巴多斯等国家建立，分别在学校和气象部门中使用。

实时数据可通过CHORDS项目数据服务器访问。3D-PAWS观测结果可应用于区域天气预报、预警系统、农业监测和健康监测。提供了UCAR/COMET项目负责人的联系信息。

---

## 53. MAML – 一种新的配置语言

**原文标题**: MAML – A new configuration language

**原文链接**: [https://maml.dev/](https://maml.dev/)

MAML：一种旨在替代 JSON 的配置语言

MAML 是一种新的配置语言，旨在成为比 JSON 更易读和更实用的替代方案。在保留 JSON 简洁性的同时，MAML 添加了配置必不可少的功能，如注释、多行字符串、可选逗号和可选键引号。

该文档展示了一个简单的 MAML 示例，演示了嵌套对象、对象数组和多行字符串。MAML 背后的理由是，JSON 虽然作为一种数据交换格式很受欢迎，但缺乏配置文件的关键功能。MAML 通过提供更友好的语法来解决这个问题。

该文档还包括一个常见问题解答部分（尽管此处的问题并未完全解答）以及各种编程语言（JavaScript、Python、Rust、C 和 PHP）的实现列表，表明 MAML 正在积极开发和采用中。目标是创建一个最小的、人类可读的、易于解析的配置语言，并在 JSON 的优势基础上构建。

---

## 54. Show HN: I built a simple ambient sound app with no ads or subscriptions

**原文标题**: Show HN: I built a simple ambient sound app with no ads or subscriptions

**原文链接**: [https://ambisounds.app/](https://ambisounds.app/)

作者正在展示他们新开发的名为“Ambi”的环境音效App。该App专注于通过可定制的音景提供放松和专注的体验。用户可以将多种声音混合在一起，并单独调节每种声音的音量。Ambi在播放时长方面具有灵活性，允许用户无限期地播放音景或设置定时器。一个关键特点是其离线可用性；所有声音都可以立即播放，无需互联网连接。该App被呈现为一个简单的解决方案，没有广告或订阅，暗示它是免费的或者提供一次性购买选项。本质上，Ambi旨在成为一个无干扰、易于使用的工具，通过可定制的环境声音组合来增强放松、专注和睡眠。

---

## 55. Fentanyl overdoses among seniors surge 9k% – A hidden crisis few saw coming

**原文标题**: Fentanyl overdoses among seniors surge 9k% – A hidden crisis few saw coming

**原文链接**: [https://www.sciencedaily.com/releases/2025/10/251012054606.htm](https://www.sciencedaily.com/releases/2025/10/251012054606.htm)

生成摘要时出错

---

## 56. Shut the Fuck Up

**原文标题**: Shut the Fuck Up

**原文链接**: [https://romanzipp.com/blog/shut-the-fuck-up](https://romanzipp.com/blog/shut-the-fuck-up)

生成摘要时出错

---

## 57. An initial investigation into WDDM on ReactOS

**原文标题**: An initial investigation into WDDM on ReactOS

**原文链接**: [https://reactos.org/blogs/investigating-wddm/](https://reactos.org/blogs/investigating-wddm/)

生成摘要时出错

---

## 58. Free software hasn't won

**原文标题**: Free software hasn't won

**原文链接**: [https://dorotac.eu/posts/fosswon/](https://dorotac.eu/posts/fosswon/)

生成摘要时出错

---

## 59. Database Linting and Analysis for PostgreSQL

**原文标题**: Database Linting and Analysis for PostgreSQL

**原文链接**: [https://pglinter.readthedocs.io/en/latest/](https://pglinter.readthedocs.io/en/latest/)

生成摘要时出错

---

## 60. Free software hasn't won

**原文标题**: Free software hasn't won

**原文链接**: [https://dorotac.eu/posts/fosswon/](https://dorotac.eu/posts/fosswon/)

生成摘要时出错

---

## 61. Database Linting and Analysis for PostgreSQL

**原文标题**: Database Linting and Analysis for PostgreSQL

**原文链接**: [https://pglinter.readthedocs.io/en/latest/](https://pglinter.readthedocs.io/en/latest/)

生成摘要时出错

---

## 62. The Tiny Teams Playbook

**原文标题**: The Tiny Teams Playbook

**原文链接**: [https://www.latent.space/p/tiny](https://www.latent.space/p/tiny)

生成摘要时出错

---

## 63. Show HN: Local Browser AI

**原文标题**: Show HN: Local Browser AI

**原文链接**: [https://blog.alexewerlof.com/p/local-browser-ai](https://blog.alexewerlof.com/p/local-browser-ai)

生成摘要时出错

---

## 64. NASA Exoplanet Travel Bureau Posters

**原文标题**: NASA Exoplanet Travel Bureau Posters

**原文链接**: [https://science.nasa.gov/exoplanets/immersive/exoplanet-travel-bureau/](https://science.nasa.gov/exoplanets/immersive/exoplanet-travel-bureau/)

生成摘要时出错

---

## 65. A better SQL validator and comparison with existing SQL validators

**原文标题**: A better SQL validator and comparison with existing SQL validators

**原文链接**: [https://app.sqlai.ai/posts/better-sql-validator/](https://app.sqlai.ai/posts/better-sql-validator/)

生成摘要时出错

---

## 66. Completing a BASIC language interpreter in 2025

**原文标题**: Completing a BASIC language interpreter in 2025

**原文链接**: [https://nanochess.org/ecs_basic_2.html](https://nanochess.org/ecs_basic_2.html)

生成摘要时出错

---

## 67. For centuries massive meals amazed visitors to Korea (2019)

**原文标题**: For centuries massive meals amazed visitors to Korea (2019)

**原文链接**: [https://www.atlasobscura.com/articles/history-of-korean-food](https://www.atlasobscura.com/articles/history-of-korean-food)

生成摘要时出错

---

## 68. Novelty Automation

**原文标题**: Novelty Automation

**原文链接**: [https://www.novelty-automation.com/](https://www.novelty-automation.com/)

生成摘要时出错

---

## 69. Event Horizon Telescope images reveal new dark matter detection method

**原文标题**: Event Horizon Telescope images reveal new dark matter detection method

**原文链接**: [https://phys.org/news/2025-10-event-horizon-telescope-images-reveal.html](https://phys.org/news/2025-10-event-horizon-telescope-images-reveal.html)

生成摘要时出错

---

## 70. Holes in the Web

**原文标题**: Holes in the Web

**原文链接**: [https://aeon.co/essays/generative-ai-has-access-to-a-small-slice-of-human-knowledge](https://aeon.co/essays/generative-ai-has-access-to-a-small-slice-of-human-knowledge)

生成摘要时出错

---

## 71. Feds: Brothers stole $25M in crypto in 12 seconds. Defense: outsmarted bots

**原文标题**: Feds: Brothers stole $25M in crypto in 12 seconds. Defense: outsmarted bots

**原文链接**: [https://www.businessinsider.com/crypto-brothers-peraire-bueno-trial-heist-ethereum-blockchain-arguments-2025-10](https://www.businessinsider.com/crypto-brothers-peraire-bueno-trial-heist-ethereum-blockchain-arguments-2025-10)

生成摘要时出错

---

## 72. CamoLeak: Critical GitHub Copilot Vulnerability Leaks Private Source Code

**原文标题**: CamoLeak: Critical GitHub Copilot Vulnerability Leaks Private Source Code

**原文链接**: [https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code)

生成摘要时出错

---

## 73. A whirlwind introduction to dataflow graphs (2018)

**原文标题**: A whirlwind introduction to dataflow graphs (2018)

**原文链接**: [https://fgiesen.wordpress.com/2018/03/05/a-whirlwind-introduction-to-dataflow-graphs/](https://fgiesen.wordpress.com/2018/03/05/a-whirlwind-introduction-to-dataflow-graphs/)

生成摘要时出错

---

## 74. Constraint satisfaction to optimize item selection for bundles in Minecraft

**原文标题**: Constraint satisfaction to optimize item selection for bundles in Minecraft

**原文链接**: [https://www.robw.fyi/2025/10/12/using-constraint-satisfaction-to-optimize-item-selection-for-bundles-in-minecraft/](https://www.robw.fyi/2025/10/12/using-constraint-satisfaction-to-optimize-item-selection-for-bundles-in-minecraft/)

生成摘要时出错

---

## 75. Syntax highlighting is a waste of an information channel

**原文标题**: Syntax highlighting is a waste of an information channel

**原文链接**: [https://buttondown.com/hillelwayne/archive/syntax-highlighting-is-a-waste-of-an-information/](https://buttondown.com/hillelwayne/archive/syntax-highlighting-is-a-waste-of-an-information/)

生成摘要时出错

---

## 76. Nostr and ATProto (2024)

**原文标题**: Nostr and ATProto (2024)

**原文链接**: [https://shreyanjain.net/2024/07/05/nostr-and-atproto.html](https://shreyanjain.net/2024/07/05/nostr-and-atproto.html)

生成摘要时出错

---

## 77. A Retrospective Survey of 2024/2025 Open Source Supply Chain Compromises

**原文标题**: A Retrospective Survey of 2024/2025 Open Source Supply Chain Compromises

**原文链接**: [https://words.filippo.io/compromise-survey/](https://words.filippo.io/compromise-survey/)

生成摘要时出错

---

## 78. Countering Trusting Trust Through Diverse Double-Compiling (DDC)

**原文标题**: Countering Trusting Trust Through Diverse Double-Compiling (DDC)

**原文链接**: [https://dwheeler.com/trusting-trust/](https://dwheeler.com/trusting-trust/)

生成摘要时出错

---

## 79. Macro Splats 2025

**原文标题**: Macro Splats 2025

**原文链接**: [https://danybittel.ch/macro.html](https://danybittel.ch/macro.html)

生成摘要时出错

---

## 80. Modern Linux tools

**原文标题**: Modern Linux tools

**原文链接**: [https://ikrima.dev/dev-notes/linux/linux-modern-tools/](https://ikrima.dev/dev-notes/linux/linux-modern-tools/)

生成摘要时出错

---

## 81. Schleswig-Holstein completes migration to open source email

**原文标题**: Schleswig-Holstein completes migration to open source email

**原文链接**: [https://news.itsfoss.com/schleswig-holstein-email-system-migration/](https://news.itsfoss.com/schleswig-holstein-email-system-migration/)

生成摘要时出错

---

## 82. Oavif: Faster target quality image compression

**原文标题**: Oavif: Faster target quality image compression

**原文链接**: [https://giannirosato.com/blog/post/oavif/](https://giannirosato.com/blog/post/oavif/)

生成摘要时出错

---

## 83. Show HN: I made an esoteric programming language that's read like a spellbook

**原文标题**: Show HN: I made an esoteric programming language that's read like a spellbook

**原文链接**: [https://github.com/sirbread/spellscript](https://github.com/sirbread/spellscript)

生成摘要时出错

---

## 84. Edge AI for Beginners

**原文标题**: Edge AI for Beginners

**原文链接**: [https://github.com/microsoft/edgeai-for-beginners](https://github.com/microsoft/edgeai-for-beginners)

生成摘要时出错

---

## 85. I/O Multiplexing (select vs. poll vs. epoll/kqueue)

**原文标题**: I/O Multiplexing (select vs. poll vs. epoll/kqueue)

**原文链接**: [https://nima101.github.io/io_multiplexing](https://nima101.github.io/io_multiplexing)

生成摘要时出错

---

## 86. John Searle has died

**原文标题**: John Searle has died

**原文链接**: [https://www.nytimes.com/2025/10/12/books/john-searle-dead.html](https://www.nytimes.com/2025/10/12/books/john-searle-dead.html)

生成摘要时出错

---

## 87. "Fuck You" Companies

**原文标题**: "Fuck You" Companies

**原文链接**: [https://aimode.substack.com/p/fuck-you-companies](https://aimode.substack.com/p/fuck-you-companies)

生成摘要时出错

---

## 88. We need (at least) ergonomic, explicit handles [in Rust]

**原文标题**: We need (at least) ergonomic, explicit handles [in Rust]

**原文链接**: [https://smallcultfollowing.com/babysteps/blog/2025/10/13/ergonomic-explicit-handles/](https://smallcultfollowing.com/babysteps/blog/2025/10/13/ergonomic-explicit-handles/)

生成摘要时出错

---

## 89. Addictive-like behavioural traits in pet dogs with extreme motivation for toys

**原文标题**: Addictive-like behavioural traits in pet dogs with extreme motivation for toys

**原文链接**: [https://www.nature.com/articles/s41598-025-18636-0](https://www.nature.com/articles/s41598-025-18636-0)

生成摘要时出错

---

## 90. C++ Reflection and Qt MOC

**原文标题**: C++ Reflection and Qt MOC

**原文链接**: [https://wiki.qt.io/C%2B%2B_reflection_(P2996)_and_moc](https://wiki.qt.io/C%2B%2B_reflection_(P2996)_and_moc)

生成摘要时出错

---

## 91. The neurons that let us see what isn't there

**原文标题**: The neurons that let us see what isn't there

**原文链接**: [https://arstechnica.com/science/2025/10/the-neurons-that-let-us-see-what-isnt-there/](https://arstechnica.com/science/2025/10/the-neurons-that-let-us-see-what-isnt-there/)

生成摘要时出错

---

## 92. The <output> Tag

**原文标题**: The <output> Tag

**原文链接**: [https://denodell.com/blog/html-best-kept-secret-output-tag](https://denodell.com/blog/html-best-kept-secret-output-tag)

生成摘要时出错

---

## 93. Apple sued over use of copyrighted books to train Apple Intelligence

**原文标题**: Apple sued over use of copyrighted books to train Apple Intelligence

**原文链接**: [https://www.yahoo.com/news/articles/apple-sued-over-copyrighted-books-181037992.html](https://www.yahoo.com/news/articles/apple-sued-over-copyrighted-books-181037992.html)

生成摘要时出错

---

## 94. Moonlander.BAS

**原文标题**: Moonlander.BAS

**原文链接**: [https://basic-code.bearblog.dev/moonlander/](https://basic-code.bearblog.dev/moonlander/)

生成摘要时出错

---

## 95. AdapTive-LeArning Speculator System (ATLAS): Faster LLM inference

**原文标题**: AdapTive-LeArning Speculator System (ATLAS): Faster LLM inference

**原文链接**: [https://www.together.ai/blog/adaptive-learning-speculator-system-atlas](https://www.together.ai/blog/adaptive-learning-speculator-system-atlas)

生成摘要时出错

---

## 96. Konrad Zuse's Helix Tower [pdf]

**原文标题**: Konrad Zuse's Helix Tower [pdf]

**原文链接**: [https://www.iaarc.org/publications/fulltext/The_helix-tower_by_konrad_zuse_automated_con-_and_deconstruction.pdf](https://www.iaarc.org/publications/fulltext/The_helix-tower_by_konrad_zuse_automated_con-_and_deconstruction.pdf)

生成摘要时出错

---

## 97. KDE Connect: Enabling communication between all your devices

**原文标题**: KDE Connect: Enabling communication between all your devices

**原文链接**: [https://community.kde.org/KDEConnect](https://community.kde.org/KDEConnect)

生成摘要时出错

---

## 98. The World's 2.75B Buildings

**原文标题**: The World's 2.75B Buildings

**原文链接**: [https://tech.marksblogg.com/building-footprints-gba.html](https://tech.marksblogg.com/building-footprints-gba.html)

生成摘要时出错

---

## 99. AI Is Juicing the Economy. Is It Making American Workers More Productive?

**原文标题**: AI Is Juicing the Economy. Is It Making American Workers More Productive?

**原文链接**: [https://www.wsj.com/tech/ai/ai-worker-productivity-economy-77498195](https://www.wsj.com/tech/ai/ai-worker-productivity-economy-77498195)

生成摘要时出错

---

## 100. How I'm using Helix editor

**原文标题**: How I'm using Helix editor

**原文链接**: [https://rushter.com/blog/helix-editor/](https://rushter.com/blog/helix-editor/)

生成摘要时出错

---

