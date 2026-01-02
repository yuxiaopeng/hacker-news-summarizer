# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-02.md)

*最后自动更新时间: 2026-01-02 17:47:26*
## 1. 分段式 JSON

**原文标题**: FracturedJson

**原文链接**: [https://github.com/j-brooke/FracturedJson/wiki](https://github.com/j-brooke/FracturedJson/wiki)

**FracturedJson** 是一套旨在将 JSON 数据格式化为既易于阅读又结构紧凑的工具套件。它弥补了压缩版 JSON（高效但不可读）与标准“美化”版 JSON（往往过于分散且难以快速浏览）之间的空白。

该工具的核心创新在于模拟人类自然格式化数据的方式。它根据数据的复杂程度和长度，采用四种不同的格式化策略：

1.  **内联 (Inlined)：** 简单的数组和对象保持在单行内。
2.  **紧凑多行数组 (Compact Multiline Array)：** 长数组会跨多行折叠，每行包含多个项目。
3.  **表格 (Table)：** 将相似的对象或数组垂直对齐成列，方便一眼对比各个字段。
4.  **展开 (Expanded)：** 当结构过于复杂而无法简化时，恢复到传统的逐行缩进格式。

除了核心格式化逻辑外，FracturedJson 还具备以下关键特性：
*   **支持注释：** 尽管注释并非 JSON 官方标准的一部分，但它能够保留并智能地放置注释。
*   **高度自定义：** 用户可以通过 `MaxInlineComplexity`、`MaxTableRowComplexity` 以及逗号放置选项等设置来微调输出效果。
*   **跨平台可用性：** 提供 .NET 库、JavaScript/TypeScript 软件包、Visual Studio Code 扩展，并为 Python 用户提供相关选项。

总之，FracturedJson 实现了 JSON “洁净化”过程的自动化，使数据既美观又便于开发者查阅，同时兼顾了紧凑格式节省空间的优点。

---

## 2. 用纯文本文件记录的十年个人财务

**原文标题**: 10 years of personal finances in plain text files

**原文链接**: [https://sgoel.dev/posts/10-years-of-personal-finances-in-plain-text-files/](https://sgoel.dev/posts/10-years-of-personal-finances-in-plain-text-files/)

在本文中，作者回顾了使用纯文本记账工具 **Beancount** 管理个人财务的十年历程。自 2016 年 1 月以来，作者一直维护着一个经过版本控制的账本，目前已包含超过 4.5 万行数据、1 万笔交易和 1,000 个虚拟账户。

**工作流程**
该系统依赖于每月一次、耗时约 30 至 45 分钟的“例行流程”。作者从各大银行下载 CSV 账单，并通过自定义的 Python“导入程序”将其转换为 Beancount 条目。这一过程遵循复式记账法，通过手动或自动平衡分录来确保准确性。作者还将电子收据和发票（超过 500 份 PDF）直接关联至交易，从而简化了报税和财务审计。

**对生态系统的贡献**
定居德国的作者开发并维护了多家德国银行（如 DKB、ING 和 N26）的开源导入程序。针对新手面临的学习曲线陡峭问题，作者还撰写了《使用 Python 管理个人财务》（*Personal Finance with Python*）一书，帮助他人掌握这一工作流程。

**纯文本的价值**
作者总结道，这种方法的核心优势在于**数据自主权与持久性**。与可能最终关停的专有应用或云服务不同，纯文本文件保存在用户的本地机器上。它们易于检索、可通过 Git 进行版本控制，并能确保在未来几十年内仍可被任何文本编辑器读取。这十年的里程碑凸显了使用简单、耐用的工具进行长期财务追踪的强大力量。

---

## 3. Punkt. 发布 MC03 智能手机

**原文标题**: Punkt. Unveils MC03 Smartphone

**原文链接**: [https://www.punkt.ch/blogs/news/punkt-unveils-mc03](https://www.punkt.ch/blogs/news/punkt-unveils-mc03)

瑞士科技公司 Punkt. 推出了最新极简主义智能手机 **MC03**，其核心设计理念聚焦于隐私保护、数据所有权和有节制地使用技术。作为 MC02 的继任者，该设备在德国制造，搭载订阅制操作系统 **AphyOS**。

MC03 的独特之处在于其双库系统：
*   **保险库 (The Vault)：** 一个安全的隔离空间，内置来自 Threema 和 Proton（包括 Proton Mail、Calendar 和 Drive）等合作伙伴预先核准的隐私核心应用。
*   **开放网络 (The Wild Web)：** 用户可以在此空间安装任何应用，同时通过严格的防护机制防止未经授权的数据追踪，确保隐私掌控权。

硬件亮点包括 120Hz OLED HDR 显示屏、6400 万像素主摄像头，以及可持续使用的**可拆卸式 5200mAh 电池**。该设备具备 IP68 级防尘防水性能。核心软件功能包括 **Digital Nomad**（内置 VPN）和 **Ledger**（一款用于管理应用权限并追踪软件碳排放与能源消耗的工具）。

Punkt. 的哲学核心是“瑞士科技 (Swiss Tech)”运动——即通过为服务付费来保留数据所有权，而非向科技巨头“以数据换服务”。因此，MC03 售价为 **699 美元/699 欧元**，包含 12 个月的 AphyOS 订阅服务。首年之后，该服务费用为 **9.99 美元/月**，并提供多年订阅折扣。

目前已开启预订。欧洲地区预计将于 2026 年 1 月下旬开始发货，北美地区则定于 2026 年春季发货。

---

## 4. 第39届混沌通信大会视频

**原文标题**: 39th Chaos Communication Congress Videos

**原文链接**: [https://media.ccc.de/b/congress/2025](https://media.ccc.de/b/congress/2025)

第39届混沌通讯大会（39C3）于2025年12月27日至30日在汉堡举行，主题为“权力循环”（Power Cycles）。该年度盛会由混沌计算机俱乐部（CCC）主办，为期四天，是探讨技术、社会与乌托邦交汇点的全球平台。

2025年的议程涵盖了丰富的讲座和工作坊，分为安全、伦理、社会与政治、硬件、科学以及艺术与美学等板块。重点亮点及热门环节包括：

*   **社会影响与伦理：** 著名演讲者柯利·多克托罗（Cory Doctorow）讨论了如何构建一个“反平台腐烂化”的互联网；其他嘉宾探讨了人工智能在战争中的作用、“中国防火长城”以及数字监控对边缘群体的影响。
*   **安全与黑客技术：** 备受关注的话题包括工业规模的诈骗（德国交通票）、GPG和蓝牙漏洞、Android及Windows BitLocker的漏洞利用，以及“代理式”AI编码助手的安全性。
*   **硬件与科学：** 环节涵盖了从洗衣机和轮椅的实用破解，到Apple Silicon移植、3D打印设计以及通过人工智能研发新药的技术深度探讨。
*   **社区与文化：** “CCC年度回顾”（CCC-Jahresrückblick）、“安全噩梦”和基础设施回顾等传统活动，展示了俱乐部的动态以及大会本身的技术后端。

随着热门视频播放量突破8万次，39C3继续培养对技术进步的“批判性创造态度”。它依然是黑客、活动家和科学家分析数字化对人类生存状况影响，并针对当前技术趋势提出乌托邦式替代方案的重要场所。

---

## 5. less(1) 技巧汇总

**原文标题**: Assorted less(1) tips

**原文链接**: [https://blog.thechases.com/posts/assorted-less-tips/](https://blog.thechases.com/posts/assorted-less-tips/)

本文提供了 `less` 命令行工具高级功能的全面指南，不仅限于基础的文件查看，还涵盖了更高级的文本处理和导航技巧。

**关键功能与命令：**

*   **多文件管理：** `less` 可以同时打开多个文件。用户可以使用 `:e` 将文件添加到当前会话，通过 `:n`（下一个）和 `:p`（上一个）在文件间切换，并使用 `:d` 从列表中移除文件。
*   **导航与搜索：** 除了标准滚动，用户可以使用 `[count]G` 跳转到特定行，或使用 `[count]%` 跳转到文件的指定百分比位置。搜索功能支持修饰符：`!` 用于显示不匹配的行，`@*` 用于从第一个文件开始在所有已打开的文件中进行搜索。
*   **过滤：** `&` 命令类似于内部 `grep`，可过滤显示内容，仅显示匹配特定模式的行（或使用 `&!` 显示不匹配的行）。
*   **书签与括号匹配：** 用户可以使用 `m[字母]` 设置多达 52 个标记，并使用 `'[字母]` 跳回标记处。这些标记支持跨文件使用。此外，输入括号字符（`(`、`[` 或 `{`）将跳转到其匹配的对应括号。
*   **动态配置：** 无需重启即可通过输入 `-` 后跟标志来切换选项（例如：`-S` 开启/关闭折行，`-N` 显示行号，`-R` 处理 ANSI 颜色）。若需持久化配置，用户可以在其 shell 配置文件中定义 `$LESS` 环境变量。
*   **外部集成：** `v` 命令可在文本编辑器中打开当前文件，而 `!` 允许执行 shell 命令。`o` 命令在将管道传输的 `stdin` 数据保存到永久文件时非常有用。

---

## 6. Standard Ebooks：2026年文学公有领域日

**原文标题**: Standard Ebooks: Public Domain Day 2026 in Literature

**原文链接**: [https://standardebooks.org/blog/public-domain-day-2026](https://standardebooks.org/blog/public-domain-day-2026)

Standard Ebooks 庆祝 2026 年 1 月 1 日的“公有领域日”，标志着 1930 年出版的文学作品正式进入美国公有领域。根据现行美国法律，版权在作品出版 95 年后到期，这一期限显著长于美国开国元勋们最初设定的 28 年。自 2019 年以来，每年一度的版权到期终结了长达数十年的“文化寒冬”，让经典之作得以被自由地阅读、分享和再创作。

为纪念 2026 年的作品发布，Standard Ebooks 精心准备了 1930 年 20 部重要作品的高质量数字版本。该系列涵盖了多项里程碑式的文学成就，包括：

*   **达希尔·哈米特**的《马耳他之鹰》：黑色侦探小说的巅峰之作。
*   **威廉·福克纳**的《我弥留之际》：南方哥特式意识流文学的杰作。
*   **弗兰茨·卡夫卡**的《城堡》：对官僚主义的超现实主义探索。
*   **兰斯顿·休斯**的《并非没有笑声》：他在哈莱姆文艺复兴时期出版的极具影响力的处女作。
*   **阿加莎·克里斯蒂**的《牧师住宅谋杀案》：标志性人物马普尔小姐的首次登场之作。
*   **卡洛琳·基恩**的前四部《南希·朱尔》探案系列：包括《古钟的秘密》。
*   **T. S. 艾略特**的现代主义诗歌《圣灰星期三》。

其他备受关注的作品还包括伊夫林·沃的《邪恶的躯体》、多萝西·L·塞耶斯的《烈性毒药》以及埃德娜·费伯的畅销书《希马隆》。随着这些涵盖了硬汉派推理、现代主义诗歌及儿童冒险文学的作品步入公有领域，它们正式成为全人类共享的文化遗产，供公众免费取阅。

---

## 7. Clicks 通讯器

**原文标题**: Clicks Communicator

**原文链接**: [https://www.clicksphone.com/en/communicator](https://www.clicksphone.com/en/communicator)

**Clicks Communicator** 是 Clicks Technology 推出的一款独立智能手机，旨在提升生产力和实现“有目的的交流”，而非用于“无休止刷屏”。该设备超越了品牌标志性的键盘保护壳产品，配备了实体 QWERTY 全键盘，并搭载 Android 16 系统。

**核心硬件与功能：**
*   **设计与显示：** 采用 4.03 英寸 AMOLED 紧凑型显示屏（分辨率 1080x1200）及“Fastback”溜背式设计。实体键盘支持触控滚动，空格键集成了指纹传感器，并配有用于语音转文字和录音的专用侧边键。
*   **性能：** 搭载联发科 4 纳米 5G SoC，拥有 256GB 存储空间（支持最高 2TB MicroSD 卡扩展），并配备 4,000 mAh 硅碳电池。
*   **影像：** 装备 5000 万像素后置摄像头（支持 OIS 光学防抖）及 2400 万像素前置摄像头。
*   **连接性：** 全网通 5G 设备，支持 NanoSIM 与 eSIM、Wi-Fi 6，并保留了 3.5mm 耳机孔和保护隐私的物理断路开关。

**软件与生产力：**
“消息中心”（Message Hub）将各类通讯应用集成在主屏幕上，便于高效处理信息。Clicks 承诺提供两年的 Android 系统更新和五年的安全更新。

**价格与上市：**
Communicator 目前已开放预订，预计于今年晚些时候发货。全额付款或支付 199 美元可退还定金的用户可享受 **399 美元**的“早鸟价”（原价 499 美元）。全额预订还将获赠价值 100 美元的备选背壳。该设备既可作为主力手机使用，也可作为旗舰设备的辅助副机。

---

## 8. HPV vaccination reduces oncogenic HPV16/18 prevalence from 16% to <1% in Denmark

**原文标题**: HPV vaccination reduces oncogenic HPV16/18 prevalence from 16% to <1% in Denmark

**原文链接**: [https://www.eurosurveillance.org/content/10.2807/1560-7917.ES.2025.30.27.2400820](https://www.eurosurveillance.org/content/10.2807/1560-7917.ES.2025.30.27.2400820)

生成摘要时出错

---

## 9. Why users cannot create Issues directly

**原文标题**: Why users cannot create Issues directly

**原文链接**: [https://github.com/ghostty-org/ghostty/issues/3558](https://github.com/ghostty-org/ghostty/issues/3558)

生成摘要时出错

---

## 10. Show HN: Dealta – A game-theoretic decentralized trading protocol

**原文标题**: Show HN: Dealta – A game-theoretic decentralized trading protocol

**原文链接**: [https://github.com/orgs/Dealta-Foundation/repositories](https://github.com/orgs/Dealta-Foundation/repositories)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 2 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 3 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 4 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 5 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 6 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 7 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 8 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 9 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 10 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 11 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 12 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 13 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 14 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 15 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 16 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 17 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 18 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 19 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 20 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 21 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 22 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 23 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 24 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 25 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 26 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 27 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 28 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 29 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 30 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 31 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 32 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 33 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 34 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 35 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 36 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 37 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 38 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 39 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 40 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 41 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 42 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 43 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 44 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 45 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 46 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 47 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 48 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 49 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 50 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 51 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 52 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 53 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 54 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 55 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 56 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 57 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 58 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 59 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 60 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 61 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 62 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 63 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 64 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 65 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 66 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 67 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 68 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 69 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 70 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 71 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 72 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 73 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 74 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 75 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 76 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 77 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 78 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 79 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 80 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 81 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 82 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 83 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 84 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 85 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 86 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 87 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 88 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 89 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 90 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 91 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 92 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 93 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 94 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 95 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 96 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 97 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 98 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 99 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 100 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 101 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 102 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 103 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 104 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 105 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 106 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 107 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 108 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 109 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 110 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 111 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 112 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 113 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 114 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 115 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 116 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 117 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 118 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 119 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 120 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 121 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 122 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 123 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 124 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 125 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 126 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 127 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 128 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 129 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 130 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 131 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 132 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 133 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 134 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 135 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 136 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 137 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 138 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 139 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 140 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 141 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 142 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 143 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 144 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 145 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 146 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 147 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 148 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 149 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 150 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 151 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 152 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 153 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 154 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 155 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 156 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 157 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 158 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 159 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 160 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 161 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 162 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 163 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 164 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 165 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 166 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 167 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 168 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 169 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 170 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 171 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 172 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 173 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 174 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 175 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 176 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 177 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 178 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 179 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 180 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 181 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 182 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 183 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 184 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 185 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 186 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 187 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 188 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 189 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 190 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 191 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 192 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 193 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 194 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 195 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 196 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 197 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 198 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 199 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 200 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 201 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 202 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 203 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 204 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 205 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 206 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 207 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 208 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 209 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 210 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 211 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 212 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 213 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 214 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 215 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 216 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 217 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 218 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 219 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 220 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 221 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 222 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 223 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 224 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 225 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 226 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 227 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 228 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 229 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 230 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 231 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 232 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 233 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 234 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 235 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 236 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 237 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 238 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 239 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 240 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 241 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 242 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 243 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 244 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 245 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 246 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 247 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 248 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 249 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 250 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 251 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 252 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 253 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 254 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 255 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 256 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 257 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 258 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 259 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 260 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 261 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 262 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 263 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 264 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 265 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 266 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 267 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 268 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 269 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 270 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 271 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 272 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 273 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 274 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 275 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 276 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 277 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 278 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 279 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 280 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 281 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 282 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 283 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 284 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 285 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 286 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 287 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 288 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
