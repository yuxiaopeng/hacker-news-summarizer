# Hacker News 热门文章摘要 (2026-01-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Happy Public Domain Day 2026

**原文标题**: Happy Public Domain Day 2026

**原文链接**: [https://publicdomainreview.org/blog/2026/01/public-domain-day-2026/](https://publicdomainreview.org/blog/2026/01/public-domain-day-2026/)

生成摘要时出错

---

## 12. ThingsBoard: Open-Source IoT Platform

**原文标题**: ThingsBoard: Open-Source IoT Platform

**原文链接**: [https://github.com/thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)

生成摘要时出错

---

## 13. A small collection of text-only websites

**原文标题**: A small collection of text-only websites

**原文链接**: [https://shkspr.mobi/blog/2025/12/a-small-collection-of-text-only-websites/](https://shkspr.mobi/blog/2025/12/a-small-collection-of-text-only-websites/)

生成摘要时出错

---

## 14. What You Need to Know Before Touching a Video File

**原文标题**: What You Need to Know Before Touching a Video File

**原文链接**: [https://gist.github.com/arch1t3cht/b5b9552633567fa7658deee5aec60453/](https://gist.github.com/arch1t3cht/b5b9552633567fa7658deee5aec60453/)

生成摘要时出错

---

## 15. A website to destroy all websites

**原文标题**: A website to destroy all websites

**原文链接**: [https://henry.codes/writing/a-website-to-destroy-all-websites/](https://henry.codes/writing/a-website-to-destroy-all-websites/)

生成摘要时出错

---

## 16. Matz 2/2: The trajectory of Ruby's growth, Open-Source Software today etc.

**原文标题**: Matz 2/2: The trajectory of Ruby's growth, Open-Source Software today etc.

**原文链接**: [https://en.kaigaiiju.ch/episodes/matz2](https://en.kaigaiiju.ch/episodes/matz2)

生成摘要时出错

---

## 17. Can I throw a C++ exception from a structured exception?

**原文标题**: Can I throw a C++ exception from a structured exception?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20170728-00/?p=96706](https://devblogs.microsoft.com/oldnewthing/20170728-00/?p=96706)

生成摘要时出错

---

## 18. FreeBSD: Home NAS, part 1 – configuring ZFS mirror (RAID1)

**原文标题**: FreeBSD: Home NAS, part 1 – configuring ZFS mirror (RAID1)

**原文链接**: [https://rtfm.co.ua/en/freebsd-home-nas-part-1-configuring-zfs-mirror-raid1/](https://rtfm.co.ua/en/freebsd-home-nas-part-1-configuring-zfs-mirror-raid1/)

生成摘要时出错

---

## 19. Show HN: I built a clipboard tool to strip/keep specific formatting like Italics

**原文标题**: Show HN: I built a clipboard tool to strip/keep specific formatting like Italics

**原文链接**: [https://custompaste.com](https://custompaste.com)

生成摘要时出错

---

## 20. Show HN: Jsonic – Python JSON serialization that works

**原文标题**: Show HN: Jsonic – Python JSON serialization that works

**原文链接**: [https://medium.com/dev-genius/jsonic-python-serialization-that-just-works-3b38d07c426d](https://medium.com/dev-genius/jsonic-python-serialization-that-just-works-3b38d07c426d)

生成摘要时出错

---

## 21. Cameras and Lenses (2020)

**原文标题**: Cameras and Lenses (2020)

**原文链接**: [https://ciechanow.ski/cameras-and-lenses/](https://ciechanow.ski/cameras-and-lenses/)

生成摘要时出错

---

## 22. Parental Controls Aren't for Parents

**原文标题**: Parental Controls Aren't for Parents

**原文链接**: [https://beasthacker.com/til/parental-controls-arent-for-parents.html](https://beasthacker.com/til/parental-controls-arent-for-parents.html)

生成摘要时出错

---

## 23. Can Bundler be as fast as uv?

**原文标题**: Can Bundler be as fast as uv?

**原文链接**: [https://tenderlovemaking.com/2025/12/29/can-bundler-be-as-fast-as-uv/](https://tenderlovemaking.com/2025/12/29/can-bundler-be-as-fast-as-uv/)

生成摘要时出错

---

## 24. Kling Motion Control AI

**原文标题**: Kling Motion Control AI

**原文链接**: [https://motion-control.io](https://motion-control.io)

生成摘要时出错

---

## 25. Joseph Campbell Meets George Lucas – Part I (2015)

**原文标题**: Joseph Campbell Meets George Lucas – Part I (2015)

**原文链接**: [https://www.starwars.com/news/mythic-discovery-within-the-inner-reaches-of-outer-space-joseph-campbell-meets-george-lucas-part-i](https://www.starwars.com/news/mythic-discovery-within-the-inner-reaches-of-outer-space-joseph-campbell-meets-george-lucas-part-i)

生成摘要时出错

---

## 26. Contact the ISS

**原文标题**: Contact the ISS

**原文链接**: [https://www.ariss.org/contact-the-iss.html](https://www.ariss.org/contact-the-iss.html)

生成摘要时出错

---

## 27. Marmot – A distributed SQLite server with MySQL wire compatible interface

**原文标题**: Marmot – A distributed SQLite server with MySQL wire compatible interface

**原文链接**: [https://github.com/maxpert/marmot](https://github.com/maxpert/marmot)

生成摘要时出错

---

## 28. Linux is good now

**原文标题**: Linux is good now

**原文链接**: [https://www.pcgamer.com/software/linux/im-brave-enough-to-say-it-linux-is-good-now-and-if-you-want-to-feel-like-you-actually-own-your-pc-make-2026-the-year-of-linux-on-your-desktop/](https://www.pcgamer.com/software/linux/im-brave-enough-to-say-it-linux-is-good-now-and-if-you-want-to-feel-like-you-actually-own-your-pc-make-2026-the-year-of-linux-on-your-desktop/)

生成摘要时出错

---

## 29. BYD Sells 4.6M Vehicles in 2025, Meets Revised Sales Goal

**原文标题**: BYD Sells 4.6M Vehicles in 2025, Meets Revised Sales Goal

**原文链接**: [https://www.bloomberg.com/news/articles/2026-01-01/byd-sells-4-6-million-vehicles-in-2025-meets-revised-sales-goal](https://www.bloomberg.com/news/articles/2026-01-01/byd-sells-4-6-million-vehicles-in-2025-meets-revised-sales-goal)

生成摘要时出错

---

## 30. One Number I Trust: Plain-Text Accounting for a Multi-Currency Household

**原文标题**: One Number I Trust: Plain-Text Accounting for a Multi-Currency Household

**原文链接**: [https://lalitm.com/post/one-number-i-trust/](https://lalitm.com/post/one-number-i-trust/)

生成摘要时出错

---

## 31. Show HN: Enroll, a tool to reverse-engineer servers into Ansible config mgmt

**原文标题**: Show HN: Enroll, a tool to reverse-engineer servers into Ansible config mgmt

**原文链接**: [https://enroll.sh](https://enroll.sh)

生成摘要时出错

---

## 32. US Government demands access to European police databases and biometrics [video]

**原文标题**: US Government demands access to European police databases and biometrics [video]

**原文链接**: [https://media.ccc.de/v/39c3-trump-government-demands-access-to-european-police-databases-and-biometrics](https://media.ccc.de/v/39c3-trump-government-demands-access-to-european-police-databases-and-biometrics)

生成摘要时出错

---

## 33. Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust

**原文标题**: Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust

**原文链接**: [https://openworkers.com/introducing-openworkers](https://openworkers.com/introducing-openworkers)

生成摘要时出错

---

## 34. Bluetooth Headphone Jacking: A Key to Your Phone [video]

**原文标题**: Bluetooth Headphone Jacking: A Key to Your Phone [video]

**原文链接**: [https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone](https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone)

生成摘要时出错

---

## 35. 2025 Letter

**原文标题**: 2025 Letter

**原文链接**: [https://danwang.co/2025-letter/](https://danwang.co/2025-letter/)

生成摘要时出错

---

## 36. 50% of U.S. vinyl buyers don't own a record player

**原文标题**: 50% of U.S. vinyl buyers don't own a record player

**原文链接**: [https://lightcapai.medium.com/the-great-return-from-digital-abundance-to-analog-meaning-cfda9e428752](https://lightcapai.medium.com/the-great-return-from-digital-abundance-to-analog-meaning-cfda9e428752)

生成摘要时出错

---

## 37. Python numbers every programmer should know

**原文标题**: Python numbers every programmer should know

**原文链接**: [https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/](https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/)

生成摘要时出错

---

## 38. Florida county introduces self driving patrol cars

**原文标题**: Florida county introduces self driving patrol cars

**原文链接**: [https://www.cbsnews.com/video/florida-police-department-tests-nations-first-self-driving-patrol-car/](https://www.cbsnews.com/video/florida-police-department-tests-nations-first-self-driving-patrol-car/)

生成摘要时出错

---

## 39. Soho 1851: The Greatest Christmas Meal Ever Cooked

**原文标题**: Soho 1851: The Greatest Christmas Meal Ever Cooked

**原文链接**: [https://londonist.com/london/food-and-drink/soho-1851-the-greatest-christmas-meal-ever-cooked](https://londonist.com/london/food-and-drink/soho-1851-the-greatest-christmas-meal-ever-cooked)

生成摘要时出错

---

## 40. I rebooted my social life

**原文标题**: I rebooted my social life

**原文链接**: [https://takes.jamesomalley.co.uk/p/this-might-be-oversharing](https://takes.jamesomalley.co.uk/p/this-might-be-oversharing)

生成摘要时出错

---

## 41. Quickemu: Quickly create and run optimised Windows, macOS and Linux VMs

**原文标题**: Quickemu: Quickly create and run optimised Windows, macOS and Linux VMs

**原文链接**: [https://github.com/quickemu-project/quickemu](https://github.com/quickemu-project/quickemu)

生成摘要时出错

---

## 42. If you care about security you might want to move the iPhone Camera app

**原文标题**: If you care about security you might want to move the iPhone Camera app

**原文链接**: [https://blog.jgc.org/2025/12/if-you-care-about-security-you-might.html](https://blog.jgc.org/2025/12/if-you-care-about-security-you-might.html)

生成摘要时出错

---

## 43. Extensibility: The "100% Lisp" Fallacy

**原文标题**: Extensibility: The "100% Lisp" Fallacy

**原文链接**: [https://kyo.iroiro.party/en/posts/100-percent-lisp/](https://kyo.iroiro.party/en/posts/100-percent-lisp/)

生成摘要时出错

---

## 44. WebAssembly as a Python Extension Platform

**原文标题**: WebAssembly as a Python Extension Platform

**原文链接**: [https://nullprogram.com/blog/2026/01/01/](https://nullprogram.com/blog/2026/01/01/)

生成摘要时出错

---

## 45. Dell's version of the DGX Spark fixes pain points

**原文标题**: Dell's version of the DGX Spark fixes pain points

**原文链接**: [https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points)

生成摘要时出错

---

## 46. Finland detains ship and its crew after critical undersea cable damaged

**原文标题**: Finland detains ship and its crew after critical undersea cable damaged

**原文链接**: [https://www.cnn.com/2025/12/31/europe/finland-estonia-undersea-cable-ship-detained-intl](https://www.cnn.com/2025/12/31/europe/finland-estonia-undersea-cable-ship-detained-intl)

生成摘要时出错

---

## 47. High-Fidelity 3D Shape Generation

**原文标题**: High-Fidelity 3D Shape Generation

**原文链接**: [https://pku-yuangroup.github.io/UltraShape-1.0/](https://pku-yuangroup.github.io/UltraShape-1.0/)

生成摘要时出错

---

## 48. Tokamak experiments exceed plasma density limit

**原文标题**: Tokamak experiments exceed plasma density limit

**原文链接**: [https://phys.org/news/2025-12-tokamak-exceed-plasma-density-limit.html](https://phys.org/news/2025-12-tokamak-exceed-plasma-density-limit.html)

生成摘要时出错

---

## 49. Beddel Protocol: Sequential Pipeline Executor (YAML)

**原文标题**: Beddel Protocol: Sequential Pipeline Executor (YAML)

**原文链接**: [https://www.npmjs.com/package/beddel](https://www.npmjs.com/package/beddel)

生成摘要时出错

---

## 50. C-events, yet another event loop, simpler, smaller, faster, safer

**原文标题**: C-events, yet another event loop, simpler, smaller, faster, safer

**原文链接**: [https://zelang-dev.github.io/c-events/](https://zelang-dev.github.io/c-events/)

生成摘要时出错

---

## 51. Round the tree, yes, but not round the squirrel

**原文标题**: Round the tree, yes, but not round the squirrel

**原文链接**: [https://www.futilitycloset.com/2026/01/02/round-and-round/](https://www.futilitycloset.com/2026/01/02/round-and-round/)

生成摘要时出错

---

## 52. Worlds largest electric ship launched by Tasmanian boatbuilder

**原文标题**: Worlds largest electric ship launched by Tasmanian boatbuilder

**原文链接**: [https://www.theguardian.com/australia-news/2025/may/02/hull-096-worlds-largest-electric-ship-battery-power-launched](https://www.theguardian.com/australia-news/2025/may/02/hull-096-worlds-largest-electric-ship-battery-power-launched)

生成摘要时出错

---

## 53. Going immutable on macOS, using Nix-Darwin

**原文标题**: Going immutable on macOS, using Nix-Darwin

**原文链接**: [https://carette.xyz/posts/going_immutable_macos/](https://carette.xyz/posts/going_immutable_macos/)

生成摘要时出错

---

## 54. Build a Deep Learning Library

**原文标题**: Build a Deep Learning Library

**原文链接**: [https://zekcrates.quarto.pub/deep-learning-library/](https://zekcrates.quarto.pub/deep-learning-library/)

生成摘要时出错

---

## 55. Square Minus Square – A coding agent benchmark

**原文标题**: Square Minus Square – A coding agent benchmark

**原文链接**: [https://aedm.net/blog/square-minus-square-2025-12-22/](https://aedm.net/blog/square-minus-square-2025-12-22/)

生成摘要时出错

---

## 56. iOS allows alternative browser engines in Japan

**原文标题**: iOS allows alternative browser engines in Japan

**原文链接**: [https://developer.apple.com/support/alternative-browser-engines-jp/](https://developer.apple.com/support/alternative-browser-engines-jp/)

生成摘要时出错

---

## 57. AB316: No AI Scapegoating Allowed

**原文标题**: AB316: No AI Scapegoating Allowed

**原文链接**: [https://shub.club/writings/2026/january/ab316/](https://shub.club/writings/2026/january/ab316/)

生成摘要时出错

---

## 58. James Moylan, engineer behind arrow signaling which side to refuel a car, dies

**原文标题**: James Moylan, engineer behind arrow signaling which side to refuel a car, dies

**原文链接**: [https://fordauthority.com/2025/12/ford-engineer-that-designed-gas-tank-indicator-passes-away/](https://fordauthority.com/2025/12/ford-engineer-that-designed-gas-tank-indicator-passes-away/)

生成摘要时出错

---

## 59. James Moylan, engineer behind arrow signaling which side to refuel a car, dies

**原文标题**: James Moylan, engineer behind arrow signaling which side to refuel a car, dies

**原文链接**: [https://fordauthority.com/2025/12/ford-engineer-that-designed-gas-tank-indicator-passes-away/](https://fordauthority.com/2025/12/ford-engineer-that-designed-gas-tank-indicator-passes-away/)

生成摘要时出错

---

## 60. 2025: The Year in LLMs

**原文标题**: 2025: The Year in LLMs

**原文链接**: [https://simonwillison.net/2025/Dec/31/the-year-in-llms/](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)

生成摘要时出错

---

## 61. Common Lisp SDK for the Datastar Hypermedia Framework

**原文标题**: Common Lisp SDK for the Datastar Hypermedia Framework

**原文链接**: [https://github.com/fsmunoz/datastar-cl](https://github.com/fsmunoz/datastar-cl)

生成摘要时出错

---

## 62. Love your customers

**原文标题**: Love your customers

**原文链接**: [https://bcantrill.dtrace.org/2025/12/31/love-your-customers/](https://bcantrill.dtrace.org/2025/12/31/love-your-customers/)

生成摘要时出错

---

## 63. GoGoGrandparent (YC S16) Is Hiring Tech Leads

**原文标题**: GoGoGrandparent (YC S16) Is Hiring Tech Leads

**原文链接**: [https://www.ycombinator.com/companies/gogograndparent/jobs/w2jGKM7-gogograndparent-yc-s16-is-hiring-tech-leads](https://www.ycombinator.com/companies/gogograndparent/jobs/w2jGKM7-gogograndparent-yc-s16-is-hiring-tech-leads)

生成摘要时出错

---

## 64. Building an internal agent: Code-driven vs. LLM-driven workflows

**原文标题**: Building an internal agent: Code-driven vs. LLM-driven workflows

**原文链接**: [https://lethain.com/agents-coordinators/](https://lethain.com/agents-coordinators/)

生成摘要时出错

---

## 65. Children and Helical Time

**原文标题**: Children and Helical Time

**原文链接**: [https://moultano.wordpress.com/2025/12/30/children-and-helical-time/](https://moultano.wordpress.com/2025/12/30/children-and-helical-time/)

生成摘要时出错

---

## 66. Hierarchical Navigable Small World (HNSW) in PHP

**原文标题**: Hierarchical Navigable Small World (HNSW) in PHP

**原文链接**: [https://centamori.com/index.php?slug=hierarchical-navigable-small-world-hnsw-php&lang=en](https://centamori.com/index.php?slug=hierarchical-navigable-small-world-hnsw-php&lang=en)

生成摘要时出错

---

## 67. Show HN: Wario Synth – Turn any song into Game Boy version

**原文标题**: Show HN: Wario Synth – Turn any song into Game Boy version

**原文链接**: [https://www.wario.style](https://www.wario.style)

生成摘要时出错

---

## 68. Simple 3D Packing

**原文标题**: Simple 3D Packing

**原文链接**: [https://github.com/Vrroom/psacking](https://github.com/Vrroom/psacking)

生成摘要时出错

---

## 69. Moving Images Related to the Apollo Missions, 1967–1969

**原文标题**: Moving Images Related to the Apollo Missions, 1967–1969

**原文链接**: [https://catalog.archives.gov/id/133360601](https://catalog.archives.gov/id/133360601)

生成摘要时出错

---

## 70. Street-Fighting Mathematics (2008)

**原文标题**: Street-Fighting Mathematics (2008)

**原文链接**: [https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/pages/readings/](https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/pages/readings/)

生成摘要时出错

---

## 71. Pokémon Team Optimization

**原文标题**: Pokémon Team Optimization

**原文链接**: [https://nchagnet.pages.dev/blog/pokemon-team-optimization/](https://nchagnet.pages.dev/blog/pokemon-team-optimization/)

生成摘要时出错

---

## 72. Easel Turns One One year of building my own IDE in Clojure

**原文标题**: Easel Turns One One year of building my own IDE in Clojure

**原文链接**: [https://blog.phronemophobic.com/easel-one-year.html](https://blog.phronemophobic.com/easel-one-year.html)

生成摘要时出错

---

## 73. All my Deutschlandtickets gone: Fraud at an industrial scale [video]

**原文标题**: All my Deutschlandtickets gone: Fraud at an industrial scale [video]

**原文链接**: [https://media.ccc.de/v/39c3-all-my-deutschlandtickets-gone-fraud-at-an-industrial-scale](https://media.ccc.de/v/39c3-all-my-deutschlandtickets-gone-fraud-at-an-industrial-scale)

生成摘要时出错

---

## 74. Tesla sales fall for the second year in a row

**原文标题**: Tesla sales fall for the second year in a row

**原文链接**: [https://www.businessinsider.com/tesla-sales-fall-second-year-ev-elon-musk-2026-1](https://www.businessinsider.com/tesla-sales-fall-second-year-ev-elon-musk-2026-1)

生成摘要时出错

---

## 75. Sony PS5 ROM keys leaked – jailbreaking could be made easier with BootROM codes

**原文标题**: Sony PS5 ROM keys leaked – jailbreaking could be made easier with BootROM codes

**原文链接**: [https://www.tomshardware.com/video-games/playstation/playstation-5-rom-keys-leaked-jailbreaking-could-be-made-easier-with-bootrom-codes](https://www.tomshardware.com/video-games/playstation/playstation-5-rom-keys-leaked-jailbreaking-could-be-made-easier-with-bootrom-codes)

生成摘要时出错

---

## 76. Five archetypes of small-scale fisheries reveal a continuum of strategies

**原文标题**: Five archetypes of small-scale fisheries reveal a continuum of strategies

**原文链接**: [https://www.nature.com/articles/s43016-025-01237-5](https://www.nature.com/articles/s43016-025-01237-5)

生成摘要时出错

---

## 77. Richest People Gained Record $2.2T in 2025, Fueling Calls for Wealth Tax

**原文标题**: Richest People Gained Record $2.2T in 2025, Fueling Calls for Wealth Tax

**原文链接**: [https://www.commondreams.org/news/billionaire-list-2025](https://www.commondreams.org/news/billionaire-list-2025)

生成摘要时出错

---

## 78. Rust--: Rust without the borrow checker

**原文标题**: Rust--: Rust without the borrow checker

**原文链接**: [https://github.com/buyukakyuz/rustmm](https://github.com/buyukakyuz/rustmm)

生成摘要时出错

---

## 79. Norway zips ahead in EV race as car sales hit 96% electric

**原文标题**: Norway zips ahead in EV race as car sales hit 96% electric

**原文链接**: [https://www.reuters.com/sustainability/climate-energy/norways-new-car-sales-were-96-electric-2025-2026-01-02/](https://www.reuters.com/sustainability/climate-energy/norways-new-car-sales-were-96-electric-2025-2026-01-02/)

生成摘要时出错

---

## 80. Memory Subsystem Optimizations

**原文标题**: Memory Subsystem Optimizations

**原文链接**: [https://johnnysswlab.com/memory-subsystem-optimizations/](https://johnnysswlab.com/memory-subsystem-optimizations/)

生成摘要时出错

---

## 81. A love song for Linux gamers with old GPUs

**原文标题**: A love song for Linux gamers with old GPUs

**原文链接**: [https://timur.hu/blog/2025/love-song-for-linux-gamers-with-old-gpus-eoy2025](https://timur.hu/blog/2025/love-song-for-linux-gamers-with-old-gpus-eoy2025)

生成摘要时出错

---

## 82. Only 5 Sears stores remain in the U.S.

**原文标题**: Only 5 Sears stores remain in the U.S.

**原文链接**: [https://www.nytimes.com/2025/12/26/business/sears-seritage-edward-lampert.html](https://www.nytimes.com/2025/12/26/business/sears-seritage-edward-lampert.html)

生成摘要时出错

---

## 83. Gaming on a Receipt Printer [video]

**原文标题**: Gaming on a Receipt Printer [video]

**原文链接**: [https://www.youtube.com/watch?v=oEqvYXYI56s](https://www.youtube.com/watch?v=oEqvYXYI56s)

生成摘要时出错

---

## 84. Meta made scam ads harder to find instead of removing them

**原文标题**: Meta made scam ads harder to find instead of removing them

**原文链接**: [https://sherwood.news/tech/rather-than-fully-cracking-down-on-scam-ads-meta-worked-to-make-them-harder/](https://sherwood.news/tech/rather-than-fully-cracking-down-on-scam-ads-meta-worked-to-make-them-harder/)

生成摘要时出错

---

## 85. How to construct complex data declaratively and progressively?

**原文标题**: How to construct complex data declaratively and progressively?

**原文链接**: [https://github.com/allmonday/pydantic-resolve](https://github.com/allmonday/pydantic-resolve)

生成摘要时出错

---

## 86. Akin's Laws of Spacecraft Design (2011) [pdf]

**原文标题**: Akin's Laws of Spacecraft Design (2011) [pdf]

**原文链接**: [https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf](https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf)

生成摘要时出错

---

## 87. Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文标题**: Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文链接**: [https://exopriors.com/scry](https://exopriors.com/scry)

生成摘要时出错

---

## 88. Demystifying DVDs

**原文标题**: Demystifying DVDs

**原文链接**: [https://hiddenpalace.org/News/One_Bad_Ass_Hedgehog_-_Shadow_the_Hedgehog#Demystifying_DVDs](https://hiddenpalace.org/News/One_Bad_Ass_Hedgehog_-_Shadow_the_Hedgehog#Demystifying_DVDs)

生成摘要时出错

---

## 89. A terminal-based browser with Sixel graphics

**原文标题**: A terminal-based browser with Sixel graphics

**原文链接**: [https://codeberg.org/janantos/brow6el](https://codeberg.org/janantos/brow6el)

生成摘要时出错

---

## 90. Heap Overflow in FFmpeg EXIF

**原文标题**: Heap Overflow in FFmpeg EXIF

**原文链接**: [https://bugs.pwno.io/0014](https://bugs.pwno.io/0014)

生成摘要时出错

---

## 91. Ÿnsect, a French insect farming startup, has been been placed into liquidation

**原文标题**: Ÿnsect, a French insect farming startup, has been been placed into liquidation

**原文链接**: [https://techcrunch.com/2025/12/26/how-reality-crushed-ynsect-the-french-startup-that-had-raised-over-600m-for-insect-farming/](https://techcrunch.com/2025/12/26/how-reality-crushed-ynsect-the-french-startup-that-had-raised-over-600m-for-insect-farming/)

生成摘要时出错

---

## 92. I canceled my book deal

**原文标题**: I canceled my book deal

**原文链接**: [https://austinhenley.com/blog/canceledbookdeal.html](https://austinhenley.com/blog/canceledbookdeal.html)

生成摘要时出错

---

## 93. My role as a founder-CTO: year 8

**原文标题**: My role as a founder-CTO: year 8

**原文链接**: [https://miguelcarranza.es/cto-year-8](https://miguelcarranza.es/cto-year-8)

生成摘要时出错

---

## 94. Show HN: Feather – a fresh Tcl reimplementation (WASM, Go)

**原文标题**: Show HN: Feather – a fresh Tcl reimplementation (WASM, Go)

**原文链接**: [https://www.feather-lang.dev](https://www.feather-lang.dev)

生成摘要时出错

---

## 95. Setting up a new PC used to be fun, now it is ad-ridden nightmare

**原文标题**: Setting up a new PC used to be fun, now it is ad-ridden nightmare

**原文链接**: [https://www.neowin.net/editorials/setting-up-a-new-pc-used-to-be-fun-now-it-is-ad-ridden-nightmare/](https://www.neowin.net/editorials/setting-up-a-new-pc-used-to-be-fun-now-it-is-ad-ridden-nightmare/)

生成摘要时出错

---

## 96. The compiler is your best friend

**原文标题**: The compiler is your best friend

**原文链接**: [https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it](https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it)

生成摘要时出错

---

## 97. A font with built-in TeX syntax highlighting

**原文标题**: A font with built-in TeX syntax highlighting

**原文链接**: [https://rajeeshknambiar.wordpress.com/2025/12/27/a-font-with-built-in-tex-syntax-highlighting/](https://rajeeshknambiar.wordpress.com/2025/12/27/a-font-with-built-in-tex-syntax-highlighting/)

生成摘要时出错

---

## 98. IPv6 just turned 30 and still hasn't taken over the world

**原文标题**: IPv6 just turned 30 and still hasn't taken over the world

**原文链接**: [https://www.theregister.com/2025/12/31/ipv6_at_30/](https://www.theregister.com/2025/12/31/ipv6_at_30/)

生成摘要时出错

---

## 99. Flow5 released to open source

**原文标题**: Flow5 released to open source

**原文链接**: [https://flow5.tech/docs/releasenotes.html](https://flow5.tech/docs/releasenotes.html)

生成摘要时出错

---

## 100. Pixar's True Story

**原文标题**: Pixar's True Story

**原文链接**: [https://computerhistory.org/blog/pixars-true-story/](https://computerhistory.org/blog/pixars-true-story/)

生成摘要时出错

---

