# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-20.md)

*最后自动更新时间: 2025-09-20 17:42:09*
## 1. 小说家科马克·麦卡锡关于如何撰写优秀科学论文的建议 [pdf]

**原文标题**: Novelist Cormac McCarthy's tips on how to write a great science paper [pdf]

**原文链接**: [https://gwern.net/doc/science/2019-savage.pdf](https://gwern.net/doc/science/2019-savage.pdf)

该文件似乎是一个损坏的PDF文件，据称标题为“小说家科马克·麦卡锡关于如何撰写优秀科学论文的建议”。然而，其内容由原始PDF代码和元数据组成，而非文章的实际文本或科马克·麦卡锡的任何写作技巧。它包含与字体、图像、页面布局和其他PDF元素相关的压缩数据流。其中没有关于写作建议或任何直接归因于科马克·麦卡锡的内容的可辨识信息。由于内容无法读取，因此无法总结该文章。该文件可能已损坏或包含某种形式的嵌入内容，需要特定的软件才能正确提取和显示。

---

## 2. 科学家发现冰在弯曲时会产生电。

**原文标题**: Scientists find that ice generates electricity when bent

**原文链接**: [https://phys.org/news/2025-09-scientists-ice-generates-electricity-bent.html](https://phys.org/news/2025-09-scientists-ice-generates-electricity-bent.html)

以下是文章的简明总结：

ICN2共同领导的一项新研究发现冰具有挠曲电性，意味着它在不均匀变形时会产生电。该发现发表在《自然·物理》上，揭示了冰像电子陶瓷材料一样，可以响应机械应力而产生电荷。这种挠曲电性存在于所有温度下。此外，在-113°C以下的温度下，冰表面还发现了一个薄的铁电层，使表面能够产生天然的电极化。

该研究表明，这种挠曲电性可以解释雷暴期间云的带电以及闪电的起源。虽然冰不具有压电性（仅通过压缩产生电荷），但该研究表明，弯曲或不规则变形的冰会产生电势，这与雷暴中冰粒碰撞的观测结果相呼应。

研究人员目前正在探索这项发现的潜在应用，设想未来利用冰作为活性材料的电子设备，尤其是在寒冷环境中。这项研究为理解自然现象和开发基于冰的电学特性的新技术开辟了道路。

---

## 3. 具有可再激活能量存储的活性微生物水泥超级电容器

**原文标题**: Living microbial cement supercapacitors with reactivatable energy storage

**原文链接**: [https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(25)00409-6](https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(25)00409-6)

无法访问文章链接。

---

## 4. 尖叫密码 ("ǠĂȦẶAẦ ĂǍÄẴẶȦ")

**原文标题**: SCREAM CIPHER ("ǠĂȦẶAẦ ĂǍÄẴẶȦ")

**原文链接**: [https://sethmlarson.dev/scream-cipher](https://sethmlarson.dev/scream-cipher)

赛斯·拉尔森介绍了“尖叫密码”，这是一种简单的替换密码，它用各种Unicode“拉丁大写字母A”字符来替换英文字母。他的灵感来自于Unicode“A”变体比英文字母表中的字母更多这一事实。

文章提供了密码的密钥，将每个字母（包括大写和小写）映射到唯一的“A”变体。定义了函数`SCREAM`和`unscream`，分别用于使用此密钥加密和解密文本。作者通过加密短语“SCREAM CIPHER”，然后将其解密回原始形式来演示该密码。

文章最后号召读者分享他们的想法，并提供了在Mastodon、电子邮件、RSS和Bluesky上关注该博客的链接。它还提供了浏览博客存档、查看互联网发现列表或理想情况下出去走走的链接。

---

## 5. 基于DNS的图像传输

**原文标题**: Images over DNS

**原文链接**: [https://dgl.cx/2025/09/images-over-dns](https://dgl.cx/2025/09/images-over-dns)

本文探讨了直接通过 DNS TXT 记录传输图像的可能性，突破了通常认为的极限。 虽然 TXT 记录通常被认为限制在 255 字节以内，但作者证明，通过在单个 TXT 记录中使用多个字符串并利用 TCP 进行 DNS 查询，可以传输更大的负载（高达 64KB）。

作者通过使用 Google Public DNS 的 JSON API 和自定义的 Go DNS 服务器来提供包含图像数据的大型 TXT 响应来实现这一点。 一个关键的挑战是在 JSON 中处理二进制数据，这需要自定义解析。 使用原始二进制数据的优点是避免了像 Base64 这样的编码开销。

本文提供了一个实际的例子，即一张狗的图片，并展示了如何使用 `dig` 和 Perl 脚本来检索 TXT 数据并将其转换为可用的图像文件。 同时，它也承认某些 DNS 递归器可能不支持大型 TXT 记录，并建议使用 Google Public DNS 或其他开放递归器作为替代方案。

作者认为，将 DNS 用作隧道直接向浏览器传递大型负载具有新颖性。 这具有潜在的安全隐患，特别是随着像 Let's Encrypt 这样的倡议使 IP 地址证书的可用性不断提高，因为它可能会绕过某些环境中的 DNS 过滤。 最后，作者承认 AI 在生成服务器端代码中的作用，同时强调他们是博客文章和客户端代码的作者。

---

## 6. 英国与Palantir达成15亿英镑国防协议

**原文标题**: Britain jumps into bed with Palantir in £1.5B defense pact

**原文链接**: [https://www.theregister.com/2025/09/20/uk_palantir_defense_pact/](https://www.theregister.com/2025/09/20/uk_palantir_defense_pact/)

英国政府与美国间谍技术公司帕兰提尔达成15亿英镑国防协议，旨在促进英国创新并创造数百个技术岗位。该协议在美国总统进行国事访问期间宣布，是来自各美国科技巨头声称的310亿英镑投资的一部分。

帕兰提尔以其与中情局和美国移民及海关执法局备受争议的数据分析工作而闻名，计划在英国建立其欧洲国防总部，创造350个就业岗位。该合作将涉及英国军方与帕兰提尔在人工智能驱动的能力方面进行合作，以实现更快的决策、军事规划和目标锁定，借鉴帕兰提尔在乌克兰的经验。

国防大臣约翰·希利表示，该合作将释放数十亿英镑的投资，使英国成为北约创新的领导者。该合同将属于“数字目标网络”，这是“战略防御评估”的一个组成部分，旨在整合各种数据源以增强目标选择。

帕兰提尔首席执行官亚历克斯·卡普承诺在英国投资高达7.5亿英镑，强调英国作为帕兰提尔在美国以外的最大存在的重要性。帕兰提尔的协议是来自包括微软、谷歌和CoreWeave在内的美国科技公司更广泛投资浪潮的一部分。

---

## 7. 克劳德有时能证明这一点

**原文标题**: Claude Can (Sometimes) Prove It

**原文链接**: [https://www.galois.com/articles/claude-can-sometimes-prove-it](https://www.galois.com/articles/claude-can-sometimes-prove-it)

Mike Dodds 的文章《Claude 确实 (有时) 能证明》探讨了 Anthropic 的 Claude Code，一种 AI 编码代理，在使用 Lean 进行交互式定理证明 (ITP) 方面令人惊讶的能力。ITP 虽然在形式化验证方面功能强大，但却以其难度大且耗时而闻名。Dodds 强调了 Claude Code 如何独立完成复杂的证明步骤，充当“项目经理”来指导整个形式化过程，暗示了 ITP 工具在未来会更易于使用。

他详细描述了 ITP 的挑战，强调它不仅仅是证明单个定理，还包括诸如概念数学、将概念映射到 Lean 的语法、分解定理以及调试错误等任务——本质上是“证明工程”。 Claude Code 的优势在于它能够将复杂的请求分解为子任务，并利用 Lean 的严格性反馈来迭代地纠正错误。

Dodds 通过在 Lean 中形式化一篇关于 Deny-Guarantee Reasoning 的研究论文来测试 Claude Code。 该代理处理了各种级别的任务，包括重构、定理的定义和证明，结果出乎意料地积极。 然而，Dodds 承认这种 AI 辅助的形式化比手动工作慢，遇到了诸如抖动（反复失败）、浅层持久错误（解析）和深层持久错误（概念错误）等问题。 尽管 AI 犯了错误，但通常可以用最少的指导来解决。 Dodds 建议，专门为 AI 代理设计工具，侧重于详细的反馈而不是精美的输出，可以进一步提高它们在 ITP 中的效率。

---

## 8. MapSCII – 终端中的世界地图

**原文标题**: MapSCII – World Map in Terminal

**原文链接**: [https://github.com/rastapasta/mapscii](https://github.com/rastapasta/mapscii)

MapSCII：一个基于终端的应用，它使用盲文和ASCII字符渲染世界地图，允许用户直接从控制台探索全球。它利用矢量瓦片来提供详细和交互式的地图体验。如果用户的终端支持鼠标事件，则可以使用键盘快捷键（方向键、'a'、'z'、'c'、'q'）和鼠标控制（拖动和滚动）与地图交互。

该应用拥有诸如兴趣点发现、通过Mapbox Styles进行自定义样式设置、与公共和私有矢量瓦片服务器的兼容性、使用本地VectorTile/MBTiles进行离线使用以及优化的算法等功能，以提供流畅的用户体验。

可以使用 `npm` 或 `snap` 轻松安装。要运行它，只需在终端中键入 `mapscii` 即可。

在幕后，MapSCII利用多个库来完成诸如颜色转换 (`x256`)、鼠标处理 (`term-mouse`)、输入处理 (`keypress`)、字符串长度计算 (`string-width`)、矢量瓦片解析 (`vector-tile`, `pbf`, `mbtiles`)、多边形三角剖分 (`earcut`)、空间索引 (`rbush`)、线点计算 (`bresenham`)、折线简化 (`simplify-js`)、HTTP请求 (`node-fetch`) 和瓦片存储管理 (`env-paths`) 等任务。

该项目有几个计划中的改进，包括 GeoJSON 支持、CLI 增强以及瓦片渲染和标签绘制的优化。地图数据来自OpenStreetMap，采用Open Data Commons Open Database License（ODbL）许可，而制图采用Creative Commons Attribution-ShareAlike 2.0许可（CC BY-SA）。

---

## 9. 少即是安全：Obsidian 如何降低供应链攻击的风险

**原文标题**: Less is safer: How Obsidian reduces the risk of supply chain attacks

**原文链接**: [https://obsidian.md/blog/less-is-safer/](https://obsidian.md/blog/less-is-safer/)

Obsidian 通过尽量减少对第三方代码的依赖来优先考虑安全性，从而降低供应链攻击的风险。这种“少即是安全”的方法包括从头开始构建核心功能，重新实现小型实用程序函数，Fork 中型模块，并通过使用版本锁定的文件以及偶尔经过彻底测试的升级来谨慎管理大型库（如 pdf.js、Mermaid 和 MathJax）。

只有 Electron 和 CodeMirror 等必要的软件包是用户运行的应用程序的一部分。构建依赖项保持分离。Obsidian 采用严格的版本固定和锁定文件来实现确定性构建和清晰的审计跟踪。避免使用 Postinstall 脚本，以防止在安装过程中执行任意代码。

依赖项更新采取谨慎的态度，进行细致的审查，包括变更日志分析、子依赖项检查、上游差异比较和广泛的测试。Obsidian 有意延迟升级，以便社区和安全研究人员有时间发现潜在的问题。

这种多方面的策略，结合最小的依赖项、浅层的依赖关系图、版本固定以及深思熟虑的升级过程，显著降低了 Obsidian 遭受供应链攻击的脆弱性，并为在问题影响用户之前检测到问题提供了宝贵的窗口。有关 Obsidian 安全措施的更多详细信息，请访问其安全页面和过去的审计报告。

---

## 10. Zig的新作家不安全吗？

**原文标题**: Is Zig's New Writer Unsafe?

**原文链接**: [https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/](https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/)

本文重点指出 Zig 新的 `std.Io.Reader` 和 `Writer` 接口中一个潜在的安全问题，特别是关于缓冲区大小的要求。作者演示了一个旨在从通用 `Reader` 读取并写入 `stdout` 的函数，其行为可能因分配给 `Writer` 的缓冲区大小而呈现未定义状态。

该问题的根源在于，某些 `Reader` 实现，例如 `zstd.Decompress`，对与其一起使用的 `Writer` 施加特定的缓冲区大小要求。如果 `Writer` 的缓冲区太小，代码可能会在调试模式下触发断言，或者在发布模式下进入无限循环。

作者认为，这个问题不仅仅是文档问题。存在某些情况下，`Reader` 所需的缓冲区大小要么未知，要么是条件性的（例如，基于 HTTP 标头），或者被库抽象所掩盖。此外，故障可能取决于正在处理的特定输入数据，从而使得该问题在开发期间难以检测。作者表达了担忧，认为这种看似细微的配置错误可能导致 Zig 程序中出现不可预测且难以调试的行为。他们质疑是否遗漏了某些东西，如果不是，则断言这代表当前 `Reader`/`Writer` 设计的一个重大问题。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 2 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 3 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 4 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 5 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 6 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 7 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 8 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 9 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 10 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 11 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 12 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 13 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 14 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 15 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 16 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 17 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 18 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 19 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 20 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 21 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 22 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 23 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 24 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 25 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 26 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 27 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 28 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 29 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 30 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 31 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 32 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 33 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 34 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 35 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 36 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 37 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 38 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 39 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 40 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 41 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 42 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 43 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 44 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 45 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 46 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 47 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 48 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 49 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 50 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 51 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 52 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 53 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 54 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 55 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 56 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 57 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 58 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 59 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 60 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 61 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 62 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 63 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 64 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 65 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 66 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 67 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 68 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 69 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 70 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 71 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 72 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 73 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 74 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 75 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 76 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 77 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 78 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 79 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 80 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 81 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 82 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 83 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 84 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 85 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 86 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 87 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 88 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 89 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 90 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 91 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 92 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 93 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 94 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 95 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 96 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 97 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 98 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 99 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 100 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 101 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 102 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 103 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 104 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 105 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 106 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 107 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 108 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 109 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 110 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 111 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 112 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 113 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 114 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 115 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 116 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 117 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 118 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 119 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 120 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 121 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 122 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 123 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 124 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 125 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 126 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 127 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 128 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 129 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 130 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 131 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 132 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 133 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 134 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 135 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 136 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 137 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 138 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 139 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 140 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 141 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 142 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 143 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 144 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 145 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 146 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 147 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 148 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 149 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 150 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 151 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 152 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 153 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 154 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 155 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 156 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 157 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 158 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 159 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 160 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 161 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 162 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 163 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 164 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 165 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 166 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 167 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 168 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 169 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 170 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 171 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 172 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 173 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 174 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 175 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 176 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 177 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 178 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 179 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 180 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 181 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 182 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 183 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 184 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 185 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
