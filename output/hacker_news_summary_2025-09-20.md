# Hacker News 热门文章摘要 (2025-09-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 逃逸验孕蛙在威尔士繁殖了50年

**原文标题**: Escapee pregnancy test frogs colonised Wales for 50 years

**原文链接**: [https://www.bbc.com/news/uk-wales-44886585](https://www.bbc.com/news/uk-wales-44886585)

逃逸非洲爪蟾：曾用于妊娠测试，在南威尔士殖民50年

---

## 12. C++中使用贝塞尔曲线作为缓动函数

**原文标题**: Bezier Curve as Easing Function in C++

**原文链接**: [https://asawicki.info/news_1790_bezier_curve_as_easing_function_in_c](https://asawicki.info/news_1790_bezier_curve_as_easing_function_in_c)

本文介绍了一个 C++ 库 `EasingCubicBezier<T>`，该库旨在高效实现三次贝塞尔曲线作为缓动函数。该库由 Łukasz Izdebski 创建，提供了一种现代 C++ 方法，仅使用单个头文件，避免了外部依赖。它基于贝塞尔曲线的控制点插值参数，从而可以在动画和图形中实现自定义缓动效果。

该库支持两种模式：`PRECISE` 用于使用超越函数的高精度，`FAST` 用于通过近似实现更好的性能。它已经过测试并与常用方法进行了基准测试，包括 Blender 中的方法（代数解）和数值方法（牛顿-拉夫逊法）。

使用 Google Benchmark 框架的基准测试结果表明，`EasingCubicBezier` 方法提供了稳定且始终较低的执行时间，使其对于实时动画系统具有可预测性和有效性。与在运行时求解三次多项式方程的代数和数值方法相比，它表现出卓越的性能并降低了可变性。“Optimised Blender”方法被强调为速度和稳定性之间的良好折衷方案。

该库的主要优势在于它能够以较小的内存占用（浮点数 28 字节，双精度数 56 字节）显式表示贝塞尔曲线。作者强调，这消除了在运行时求解三次多项式方程的需要，从而提高了性能。未来的工作旨在进一步优化运行时性能，同时保持灵活性。

---

## 13. 车载触摸屏危险吗？

**原文标题**: Are Touchscreens in Cars Dangerous?

**原文链接**: [https://www.economist.com/science-and-technology/2025/09/19/are-touchscreens-in-cars-dangerous](https://www.economist.com/science-and-technology/2025/09/19/are-touchscreens-in-cars-dangerous)

无法访问文章链接。

---

## 14. 如果全世界都是一个单体仓库

**原文标题**: If all the world were a monorepo

**原文链接**: [https://jtibs.substack.com/p/if-all-the-world-were-a-monorepo](https://jtibs.substack.com/p/if-all-the-world-were-a-monorepo)

无法访问文章链接。

---

## 15. Show HN: FocusStream – 专为学习者打造的专注、无干扰 YouTube 体验

**原文标题**: Show HN: FocusStream – Focused, distraction-free YouTube for learners

**原文链接**: [https://focusstream.media](https://focusstream.media)

FocusStream：专为学习者设计的专注无干扰YouTube体验。 "Show HN" 标题表明作者正在向 Hacker News 社区展示其项目。这意味着 FocusStream 旨在为在 YouTube 上观看教育内容提供一个更简洁的界面，移除可能分散学习注意力的元素，例如推荐视频、评论或其他可能无关的功能。其核心价值在于提高专注度，并在 YouTube 平台上提供更高效的学习体验。

---

## 16. 最佳YouTube下载器，以及谷歌如何封锁媒体

**原文标题**: The best YouTube downloaders, and how Google silenced the press

**原文链接**: [https://windowsread.me/p/best-youtube-downloaders](https://windowsread.me/p/best-youtube-downloaders)

Chris Hoffman的文章《最佳YouTube下载器，以及谷歌如何压制媒体》推荐了几款免费开源的YouTube下载器，包括Stacher (Windows, Mac, Linux)、yt-dlp (命令行)、Cobalt.tools (网页) 和 NewPipe (Android)。他认为，使用YouTube下载器创建个人备份和存档内容是合乎道德的，尤其考虑到YouTube作为重要的信息存储库的作用。

Hoffman批评了冗长且往往无人阅读的服务条款协议（如YouTube的）的虚伪性，将其与EULA相提并论。他认为，谷歌从围绕YouTube下载器的灰色市场中获益，因为它允许用户灵活性并维持YouTube的统治地位。

文章的重要部分揭露了谷歌据称如何利用其广告网络垄断地位（已被裁定为非法）来阻止媒体撰写关于YouTube下载器的文章。他讲述了谷歌如何惩罚那些推荐此类工具的网站，这表明了谷歌过去控制其YouTube业务的努力。他强调，虽然谷歌没有明确禁止下载器，但他们使其使用不便，从而在控制和用户访问之间取得了平衡。他还提到了为个人使用而下载视频的伦理问题，尤其是在人工智能公司使用受版权保护的内容进行训练的情况下。

---

## 17. LLM-泄气：将LLM提取为数据集

**原文标题**: LLM-Deflate: Extracting LLMs into Datasets

**原文链接**: [https://www.scalarlm.com/blog/llm-deflate-extracting-llms-into-datasets/](https://www.scalarlm.com/blog/llm-deflate-extracting-llms-into-datasets/)

Greg Diamos 的文章《LLM-Deflate：将 LLM 提取到数据集中》介绍了一种新颖的技术，通过逆转 LLM 训练中固有的压缩过程，系统地从大型语言模型 (LLM) 中提取结构化数据集。其核心思想是利用 LLM 推理，将模型参数中嵌入的知识“解压缩”为可重用的训练数据。

该文章强调了传统合成数据生成方法的缺点，并提出了一种分层主题探索方法。该方法涉及从广泛的类别递归生成更具体的子主题，以系统地遍历模型的知识空间。对于每个主题，系统都会生成训练示例，提示模型提供明确的推理步骤以及事实性知识。

为了解决推理成本瓶颈，作者强调了高性能推理基础设施 (scalarlm) 对于并行示例生成、提示工程迭代和全面知识空间覆盖的重要性。

该方法应用于 Qwen3-Coder、GPT-OSS 和 Llama 3，为每个模型生成了 10,000 多个结构化训练示例。这些数据集可在 Hugging Face 上获取，并揭示了每个模型解决问题的方式差异。

提取的数据集可用于模型分析、知识转移（微调其他模型）、训练数据增强和模型调试。文章还讨论了诸如提示工程、主题树平衡和质量过滤等技术挑战，以及相应的解决方案。未来的研究方向包括跨模型知识转移、知识演化跟踪、专业数据集创建和模型可解释性。作者认为，随着推理成本的降低，这种系统的知识提取将成为机器学习工具包的标准组成部分。

---

## 18. Git：引入Rust并宣布其将成为强制标准

**原文标题**: Git: Introduce Rust and announce that it will become mandatorty

**原文链接**: [https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/](https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/)

提供的內容並非關於Git引入Rust並強制執行的文章，而是在網站上實施的一項安全措施，旨在防止AI爬蟲使伺服器過載。

以下是內容實際描述的摘要：

該訊息解釋說，用戶看到此頁面是因為該網站受到名為Anubis的系統保護。Anubis旨在阻止積極抓取網站的AI爬蟲，這些爬蟲可能會導致網站崩潰並使合法用戶無法訪問。

Anubis採用類似於Hashcash的“工作量證明”機制，需要用戶的瀏覽器執行少量計算。對於個別用戶而言，這種負擔可以忽略不計，但對於大規模爬蟲而言，則變得非常重要，使其更難以運行。

該文本澄清說，Anubis是一種臨時解決方案。網站管理員正在研究更複雜的方法，例如指紋識別和識別無頭瀏覽器，以區分合法用戶和機器人。理想情況下，這將消除對“工作量證明”挑戰的需求。

該訊息還指出，Anubis需要JavaScript才能正常運行，並建議禁用諸如JShelter之類的瀏覽器插件，這些插件可能會干擾其運行。它承認需要JavaScript很不方便，但由於AI公司的行為，這是必要的，並強調正在開發一種無JavaScript的解決方案。

---

## 19. 2025年评估：构建人们可用模型的基准

**原文标题**: Evals in 2025: benchmarks to build models people can use

**原文链接**: [https://github.com/huggingface/evaluation-guidebook/blob/main/yearly_dives/2025-evaluations-for-useful-models.md](https://github.com/huggingface/evaluation-guidebook/blob/main/yearly_dives/2025-evaluations-for-useful-models.md)

Hugging Face“评估指南”，聚焦“2025年的评估”，旨在探索评估大型语言模型（LLM）的未来，以构建真正对人们有用的模型。它强调需要超越当前通常无法反映真实世界使用的基准，并专注于优先考虑用户需求和实际应用的评估。

该指南可能主张：

*   **更真实的基准：** 当前的基准很容易被攻破，并且通常与真实世界的性能或用户满意度不相关。该指南可能提倡密切模拟人们实际使用 LLM 方式的基准。
*   **以用户为中心的评估：** 该指南强调基于 LLM 解决用户问题、提高生产力和增强用户体验的能力来进行评估，而不是仅仅关注准确性或困惑度等指标。
*   **全面的评估：** 该指南可能建议评估 LLM 在推理、创造力、沟通和安全性等一系列能力，以确保模型全面可靠。
*   **不断发展的基准：** 随着模型的改进和用例的演变，该指南可能强调需要不断更新和调整评估方法，以保持相关性并推动 LLM 能力的边界。

本质上，该“评估指南”可能提供了一个框架，用于构建更好的评估实践，从而产生不仅在纸面上令人印象深刻，而且在人们的日常生活中真正有价值和可用的 LLM。

---

## 20. PyPI 博客：通过 GitHub Actions 工作流进行的 Token 窃取活动

**原文标题**: PyPI Blog: Token Exfiltration Campaign via GitHub Actions Workflows

**原文链接**: [https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/](https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/)

近期PyPI令牌泄露事件：恶意GitHub Actions工作流窃取令牌。攻击者将代码注入多个仓库的工作流，试图窃取存储为GitHub secrets的令牌并发送至外部服务器。虽然部分令牌被成功窃取，但没有证据表明它们被用于入侵PyPI或发布恶意软件包。

GitGuardian首先发现了一个试图窃取令牌的恶意工作流，事件由此开始。由于最初的报告落入PyPI的垃圾邮件文件夹，导致响应延迟。调查显示这是一次广泛的攻击，许多维护者已经通过还原更改、删除工作流或轮换令牌做出响应。PyPI已使所有受影响的令牌失效，并通知了受影响的项目维护者。

该博客强调使用GitHub Trusted Publishers作为最有效的缓解措施。Trusted Publishers采用有效期短、仓库范围的令牌，显著降低了泄露风险。用户还应审查其PyPI账户安全历史记录，以查找可疑活动。文章感谢GitGuardian的合作，并感谢Alpha-Omega和其他赞助商对PyPI安全工作的支持。

---

## 21. 似乎违背生物学规律的蚂蚁——它们产下的卵孵化出另一种物种

**原文标题**: Ants that seem to defy biology – They lay eggs that hatch into another species

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-ant-queens-seem-to-defy-biology-they-lay-eggs-that-hatch-into-another-species-180987292/](https://www.smithsonianmag.com/smart-news/these-ant-queens-seem-to-defy-biology-they-lay-eggs-that-hatch-into-another-species-180987292/)

伊比利亚收获蚁后展现前所未有的“异种生育”现象，产下的卵孵化成另一种蚂蚁——建筑收获蚁的雄蚁。这一发现挑战了依赖于同种群内繁殖可育后代能力的传统物种定义。

伊比利亚收获蚁后与建筑收获蚁雄蚁交配并储存精子。然后，它们用这些精子给部分卵受精，同时移除自身的遗传物质，从而有效地产生建筑收获蚁的雄性克隆体。因此，伊比利亚收获蚁群落由伊比利亚收获蚁后、杂交工蚁（两种蚂蚁的雌性杂交后代），以及伊比利亚收获蚁和建筑收获蚁的雄蚁组成。

令人惊讶的是，伊比利亚收获蚁和建筑收获蚁在进化上已经分离了五百多万年。研究人员通过在伊比利亚收获蚁群落中发现有毛（伊比利亚收获蚁）和无毛（建筑收获蚁）的雄蚁，并通过DNA检测确认了它们的物种，从而识别了这种行为。他们还通过在实验室环境中观察到伊比利亚收获蚁后产下建筑收获蚁，进一步证实了这一现象。

这种不寻常关系的目的被认为是互惠互利的。伊比利亚收获蚁获得稳定的工蚁供应，而建筑收获蚁雄蚁则被分布到其有限山区栖息地之外的新区域，因为建筑收获蚁群落仅分布于山区。然而，建筑收获蚁雄蚁的克隆可能会导致有害基因突变随着时间的推移而积累。尽管存在潜在的长期缺陷，但目前的安排是成功的，展示了一个独特的共同进化案例。

---

## 22. Show HN: Zedis – 我用 Zig 写的 Redis 克隆

**原文标题**: Show HN: Zedis – A Redis clone I'm writing in Zig

**原文链接**: [https://github.com/barddoo/zedis](https://github.com/barddoo/zedis)

Zedis 是一个用 Zig 编写的、兼容 Redis 的内存数据存储，旨在作为学习项目，不适用于生产环境。它通过实现核心 Redis 协议 (RESP) 和数据结构，追求简洁、性能和线程安全。主要特性包括字符串和整数存储、基本 Redis 命令（GET、SET、INCR 等）、并发客户端连接处理和 RDB 快照。最近新增了发布/订阅功能。

项目路线图包括实现 AOF 日志、更多 Redis 命令、列表和集合、配置文件支持、键过期、集群和性能基准测试套件。

要开始使用，用户需要 Zig（0.15.1 或更高版本）。构建使用 `zig build` 命令，运行使用 `zig build run` 命令。服务器默认为 127.0.0.1:6379。用户可以使用 `redis-cli` 与 Zedis 交互。

Zedis 强调类型安全操作、显式错误处理、内存安全（无需垃圾回收）、模块化设计和全面的日志记录。内存分配在初始化期间处理，以避免在命令执行期间进行动态分配。添加新命令涉及实现处理程序、注册命令和添加测试。该项目强调遵守 Zig 的代码风格。项目的 GitHub 链接已提供，以获取更多信息。

---

## 23. 2025年搞笑诺贝尔奖得主

**原文标题**: IG Nobel Prize Winners 2025

**原文链接**: [https://improbable.com/ig/winners/](https://improbable.com/ig/winners/)

本文公布了2025年和2024年搞笑诺贝尔奖的获奖者，该奖项旨在表彰“先让人发笑，后引人深思”的成就。2025年的奖项涵盖了范围广泛的、不寻常但发人深省的研究。亮点包括：一个关于指甲生长35年研究的文学奖，一个考察智力反馈对自恋影响的心理学奖，以及一个关于蜥蜴吃披萨研究的营养学奖。其他奖项表彰了关于大蒜对母乳的影响、斑马纹奶牛驱赶苍蝇、特氟龙作为无热量食物膨胀剂的潜力、酒精对外语能力的影响、鞋架设计与鞋子气味的关系、酒精对蝙蝠飞行的影响以及意大利面酱凝结物理学的研究。

2024年的搞笑诺贝尔奖包括：B.F. 斯金纳的鸽子制导导弹研究获得的和平奖，植物模仿塑料植物获得的植物学奖，调查不同半球头发旋方向的解剖学奖，以及强调安慰剂在带来痛苦副作用时有效性的医学奖。其他奖项授予了关于死鳟鱼游泳、哺乳动物通过肛门呼吸、硬币翻转落回起始面的概率、用于分离醉酒和清醒蠕虫的色谱法、超级人瑞数据中的人口统计异常以及在奶牛附近引爆纸袋以研究牛奶喷射的研究。

文章还提到了2023年搞笑诺贝尔化学和地质学奖，该奖项颁给了 Jan Zalasiewicz，以表彰他解释了科学家为什么舔舐岩石。颁奖典礼分别在波士顿大学和麻省理工学院举行。

---

## 24. 系统调用为何昂贵：Linux内核深度剖析

**原文标题**: What Makes System Calls Expensive: A Linux Internals Deep Dive

**原文链接**: [https://blog.codingconfessions.com/p/what-makes-system-calls-expensive](https://blog.codingconfessions.com/p/what-makes-system-calls-expensive)

本文深入探讨了 Linux 系统在 x86-64 架构上系统调用的性能开销。系统调用是用户程序与操作系统交互的关键，在性能剖析中经常表现为性能瓶颈。虽然系统调用中内核代码的执行会增加开销，但主要成本来自于用户空间和内核空间之间切换时对 CPU 优化的中断。

本文细致地检查了 Linux 内核的系统调用处理程序，重点介绍了诸如交换 GS 寄存器、切换页表和堆栈、保存用户空间寄存器以及实施针对推测执行攻击（Spectre、Retbleed）的缓解措施等步骤，这些都会增加开销。

开销分为直接成本和间接成本。直接开销主要在系统调用之间是固定的，包括内核入口和退出例程的执行。通过 vDSO（用户空间快捷方式）和直接系统调用接口比较 `clock_gettime` 的执行情况，表明由于这种直接开销，系统调用接口要慢得多。

间接开销源于 CPU 微架构状态的扰乱，特别是指令流水线和分支预测机制。在系统调用进入期间，清空指令流水线和清除分支预测缓冲区会中断 CPU 优化，导致返回时用户空间代码的瞬时性能下降。文章认为，针对推测执行攻击的缓解措施具有很大的性能成本，并直接导致间接开销。因此，最小化系统调用对于性能优化至关重要。

---

## 25. Show HN: WeUseElixir - Elixir 项目目录

**原文标题**: Show HN: WeUseElixir - Elixir project directory

**原文链接**: [https://weuseelixir.com/](https://weuseelixir.com/)

WeUseElixir 是一个目录，展示了使用 Elixir 编程语言的应用程序、库和公司。 该目录旨在提供 Elixir 实际解决方案的示例。 其中列出了几个使用 Elixir 的知名公司和项目，每个都附带描述其目的的标语：

*   Copia Wealth Studios: Assets Under Intelligence®
*   Pipie.io: Gitlab 在 Slack 中的通知。 让你的工程师更有效率
*   Give With Click: 为学校和运动队提供固定费用的筹款。
*   Jump Comedy: All Things Comedy
*   Mux: 为开发者提供的视频 API。
*   ReadOnce: 安全的一次性链接
*   Flop: 使用 Ecto 进行过滤、排序和分页
*   Oban: 用于 Elixir 的强大的作业处理
*   Absinthe: 用于 Elixir 的 GraphQL 工具包
*   SparkMeter: 为了可靠、清洁和高效的电力
*   X-Plane 12: 飞行模拟器 | X-Plane 12：正确的飞行模拟
*   WeUseElixir: 查找使用 Elixir 的应用程序、库和公司
*   VEEPS: 观看直播音乐会、音乐和活动
*   Remote: 为分布式团队提供的全球人力资源解决方案和就业工具
*   Pepsico: 用每一口和每一咬创造更多的微笑
*   Community: 个性化短信平台和 SMS 解决方案

介绍还提到，用户可以免费将自己的 Elixir 应用程序添加到目录中，并浏览当前所有可用的列表。 似乎该网站在为此“Show HN”生成内容时遇到了连接问题。

---

## 26. 微软备忘录建议目前身在国外的H1B员工立即返回。

**原文标题**: Microsoft memo advises H1B employees to return immediately if currently abroad

**原文链接**: [https://xcancel.com/onestpress/status/1969374699038675364](https://xcancel.com/onestpress/status/1969374699038675364)

微软内部备忘录建议目前在国外的H1B员工及其家属立即回国，原因是新的“费用”将于2025年9月20日午夜生效，导致旅行中断。该费用被广泛认为与特朗普政府的政策有关，可能由斯蒂芬·米勒设计，针对科技行业。

对此消息的反应各不相同，且多为负面。许多评论员对新费用可能给H1B签证持有者及其雇佣公司（如微软、亚马逊和特斯拉）带来的潜在混乱和经济负担表示担忧。一些人认为这将激励公司将运营和工作岗位转移到美国境外，而另一些人则认为这是一种对外国施加影响的策略。一些人希望公司会在法庭上挑战这项费用。

一些用户推测了该费用对美国经济及其竞争力的影响。人们对该费用的公平性和合法性提出了质疑，一些人认为这是一种敲诈勒索。人们还担心其他国家可能会采取增加签证费用的报复措施。该费用的支持者则为此消息欢呼，认为这是优先考虑美国工人的一种方式。总的来说，该公告引发了人们对H1B签证未来的相当大的焦虑和辩论，以及对个人和美国经济的影响。

---

## 27. Feedmaker: URL + CSS选择器 = RSS订阅源

**原文标题**: Feedmaker: URL + CSS selectors = RSS feed

**原文链接**: [https://feedmaker.fly.dev](https://feedmaker.fly.dev)

Feedmaker是由Kevin Schaul创建的工具，允许用户从任何网站生成RSS订阅。它的运作原理很简单：用户提供URL和CSS选择器，Feedmaker就会基于这些信息创建RSS订阅。这使得用户能够轻松追踪那些本身不提供RSS订阅的网站的更新和内容，或者根据特定标准自定义订阅。

该工具为用户提供了两种选择：要么输入他们自己的网站URL和CSS选择器，要么从预定义的示例中选择。这些示例突出了潜在的用途，比如追踪华盛顿邮报、纽约时报和华尔街日报等主要新闻媒体的热门报道，或者关注Bandcamp上的爵士乐文章等特定内容类别，或者监控特定供应商的更新。

---

## 28. 互联网档案馆与音乐出版商的重大诉讼以和解告终

**原文标题**: Internet Archive's big battle with music publishers ends in settlement

**原文链接**: [https://arstechnica.com/tech-policy/2025/09/internet-archives-big-battle-with-music-publishers-ends-in-settlement/](https://arstechnica.com/tech-policy/2025/09/internet-archives-big-battle-with-music-publishers-ends-in-settlement/)

互联网档案馆(IA)与主要音乐出版商（环球音乐、Capitol、索尼音乐等）就Great 78项目（一项旨在数字化并保存早期音乐录音的倡议）诉讼达成保密和解。 出版商最初寻求4亿美元的赔偿，后来增加到7亿美元，声称由于Great 78录音的可用性导致流媒体收入损失。 IA辩称该项目对收入的影响极小，并且损害赔偿被夸大。

和解协议的细节仍然未公开，但这与IA去年输给图书出版商的类似法律诉讼之后的情况类似，也导致了一笔未公开的付款。 IA辩称，唱片公司后来大量增加侵权作品是一种迫使和解的策略。

针对IA的Great 78项目的诉讼被一些人，如声音历史学家David Seubert，视为唱片公司可能不喜欢IA对版权和合理使用的态度，而非源于实际的经济损失，因此可能是一种报复行为。 此次和解结束了IA一场可能导致毁灭性后果的法律诉讼，尽管由于保密协议，实际成本仍然未知。

---

## 29. Notion 3.0 AI 代理的隱藏風險：濫用網絡搜索工具進行數據洩露

**原文标题**: Hidden risk in Notion 3.0 AI agents: Web search tool abuse for data exfiltration

**原文链接**: [https://www.codeintegrity.ai/blog/notion](https://www.codeintegrity.ai/blog/notion)

本文重点指出Notion 3.0 AI Agents中的一个关键安全漏洞，具体涉及通过滥用网络搜索工具进行数据泄露的潜在风险。核心问题源于强大的LLM代理、对集成工具(MCPs)的访问以及持久性记忆的结合，被称为“致命三连击”。

本文演示了攻击者如何利用`functions.search`工具，在看似无害的文档（如PDF）中嵌入恶意提示。该提示指示Notion AI代理搜索用户Notion工作区内的敏感数据，然后通过将其附加到URL来泄露这些数据，从而有效地通过网络搜索查询将其发送到攻击者控制的恶意服务器。

该演示涉及一个PDF文档，其中包含AI代理提取客户信息（姓名、公司、ARR）并通过`functions.search`工具调用将其发送到虚假后端服务（db-client-codeintegrity.com）的隐藏指令。攻击者在提示中使用操纵策略，例如声称任务紧急且已授权，以确保代理完成任务。

该漏洞的存在是因为Notion的AI Agents可以跨多个文档、数据库和外部连接器以传统基于角色的访问控制(RBAC)无法预测的方式链接任务。文章强调，即使使用最先进的模型Claude Sonnet 4.0，这种攻击也有效，表明了问题的严重性。文章最后指出，像Github、Gmail、Jira等MCP集成到Notion AI Agents中，由于提示注入攻击，极大地增加了威胁态势。

---

## 30. 对象存储的高性能穿透式读取缓存

**原文标题**: High-performance read-through cache for object storage

**原文链接**: [https://github.com/s2-streamstore/cachey](https://github.com/s2-streamstore/cachey)

Cachey 是一款高性能的直读缓存，专为 S3 等对象存储设计，提供简洁的 HTTP API。 它利用 foyer 驱动的混合内存和磁盘缓存，高效地缓存不可变的数据块。主要特性包括：

*   **精确范围获取：** 使用 `/fetch` API，需要精确的字节范围才能检索。
*   **页面对齐缓存：** 将请求映射到固定的 16 MiB 页面对齐范围。
*   **请求合并：** 有效处理对同一页面的并发请求。
*   **对冲请求：** 通过对冲请求和潜在的对象冗余存储桶，缓解对象存储的尾延迟。
*   **可配置的存储桶：** 允许指定存储桶偏好设置并覆盖 S3 请求配置。

API 使用带有 `Range` 标头的 `GET` 或 `HEAD` 请求到 `/fetch/{kind}/{object}`。客户端可以使用 `C0-Bucket` 指定首选存储桶，并使用 `C0-Config` 覆盖 S3 配置。响应包括 `Content-Range`、`Content-Length`、`Last-Modified` 和 `C0-Status` 标头。该服务提供监控端点 `/stats`（JSON 吞吐量统计）和 `/metrics`（Prometheus 格式）。配置选项包括内存和磁盘容量、对冲分位数、TLS 设置和端口，通过命令行参数指定。Docker 镜像也可用于部署。

---

## 31. 支持我们的AI霸主：重新设计数据系统，以智能体为先

**原文标题**: Supporting Our AI Overlords: Redesigning Data Systems to Be Agent-First

**原文链接**: [https://arxiv.org/abs/2509.00997](https://arxiv.org/abs/2509.00997)

这篇于2025年8月31日提交的 arXiv 文章《支持我们的 AI 霸主：重新设计以代理为中心的数据系统》指出，当前的数据系统无法很好地应对大型语言模型 (LLM) 代理日益占据主导地位的局面。 这些代理代表用户分析和操纵数据，参与一种名为“代理推测”的过程，其特点是高吞吐量的探索和解决方案制定。 这种推测的规模和低效率带来了重大挑战。

由 Shu Liu 和 Aditya G. Parameswaran 领导的作者提出转向以代理为中心的数据系统。 他们确定了代理推测的关键特征——规模、异构性、冗余性和可操纵性——并利用这些特征概述了这种新架构的新研究机会。 这些机会涵盖了各个领域，包括针对代理交互优化的新型查询界面、处理代理工作负载特定需求的创新查询处理技术，以及专为代理驱动场景中的高效数据访问和存储而设计的新型“代理记忆存储”。 该文章倡导调整数据系统，以便更好地原生支持 LLM 代理处理数据的需求。

---

## 32. 使用延续编译

**原文标题**: Compiling with Continuations

**原文链接**: [https://swatson555.github.io/posts/2025-09-16-compiling-with-continuations.html](https://swatson555.github.io/posts/2025-09-16-compiling-with-continuations.html)

本文回顾了关于 Standard ML 和编译器设计的书籍《使用延续进行编译》，重点关注延续的实际应用。评论者认为这本书内容密集且缺乏练习，感觉更像是一个信息倾倒，而不是结构化的学习资源。尽管该书声称内容全面，但作者认为其 1992 年关于行业相关性的断言已经过时。

评论详细介绍了评论者自己基于该书原理实现的编译器，涵盖了词法分析、语法分析 (MiniML)、求值 (CPS) 和编译到 CPS 语言等阶段。作者讨论了闭包转换和寄存器溢出的挑战。

突出的关键优势包括本书对计算基本概念的强调以及对延续实用性的证明，超越了简单的解释器。然而，评论者批评了这本书的缺点，例如缺少寄存器分配细节和虚拟机链接要求。

最终，评论者承认 CPS 从未成为广泛采用的中间表示形式。尽管学到的 Standard ML 知识比大多数人都要多，但评论者得出结论，花在这本书上的时间并没有特别有价值，并表明虽然有见地，但提出的许多优化并不一定需要延续。

---

## 33. 内核：引入多内核架构支持

**原文标题**: Kernel: Introduce Multikernel Architecture Support

**原文链接**: [https://lwn.net/ml/all/20250918222607.186488-1-xiyou.wangcong@gmail.com/](https://lwn.net/ml/all/20250918222607.186488-1-xiyou.wangcong@gmail.com/)

该补丁系列引入了 Linux 内核中对多内核架构的基础支持，使多个独立的内核实例能够在单个物理机上并发运行。其目标是与传统虚拟化相比，提供更高的故障隔离性、增强的安全性和更好的资源利用率。

该实现依赖于对 `kexec` 子系统的增强，以加载和管理多个内核镜像，并将每个实例分配给特定的 CPU 核心。一个新的处理器间中断 (IPI) 框架促进了这些内核之间的通信。 主要组件包括：

*   `kexec` 中动态的 `kimage` 跟踪。
*   一个通用的 IPI 通信框架。
*   x86 特定的 CPU 引导机制。
*   用于监控内核实例的 `/proc/multikernel` 接口。

这七个补丁涵盖：

1.  通过 `kexec` 实现基本的多内核支持。
2.  用于 CPU 引导的 x86 SMP INIT trampoline。
3.  用于 x86 内核间通信的 `MULTIKERNEL_VECTOR`。
4.  通用的 IPI 通信框架。
5.  用于物理 CPU 识别的 `arch_cpu_physical_id()`。
6.  动态 `kimage` 跟踪的实现。
7.  `/proc/multikernel` 接口。

这是一个征求意见稿 (RFC)，因此该实现被认为是初步的，细节需要改进。测试有限。作者征求社区反馈、测试和贡献，以在此基础上构建。潜在的用例包括并行运行实时内核和通用内核、隔离安全关键型应用程序以及为特定工作负载提供专用内核实例。

---

## 34. 这些天，systemd可能会成为守护进程限制的原因。

**原文标题**: These days, systemd can be a cause of restrictions on daemons

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdCanBeRestrictionCause](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdCanBeRestrictionCause)

由于大量使用旧版 Chrome 用户代理的高流量爬虫激增，Wandering Thoughts 的 Chris Siebenmann 正在阻止使用过时浏览器的用户访问他的博客。这些爬虫可能正在收集数据用于 LLM 训练，给他的服务器带来了巨大的负担。他的反爬虫措施会将旧版本的浏览器标记为可疑。

如果合法用户使用最新浏览器时遇到此问题，请使用大学电子邮件地址联系他，并提供详细信息，包括他们的 User-Agent 字符串。

这篇文章专门针对 archive.* 服务（archive.today、archive.ph、archive.is）的用户，解释说这些服务也被阻止了。 由于使用旧版 Chrome User-Agent 值、分散的 IP 地址和伪造的反向 DNS 条目，他们的爬取行为与恶意行为者无法区分。 Siebenmann 建议改用 archive.org，因为它是一个行为更好的存档爬虫。

---

## 35. 你自己的友善人机界面：在家尝试杰夫·拉斯金的理念

**原文标题**: Your very own humane interface: Try Jef Raskin's ideas at home

**原文链接**: [https://arstechnica.com/gadgets/2025/09/your-very-own-humane-interface-try-jef-raskins-ideas-at-home/](https://arstechnica.com/gadgets/2025/09/your-very-own-humane-interface-try-jef-raskins-ideas-at-home/)

本文探讨了如何通过模拟在家中体验杰夫·拉斯金的“人性化界面”概念。文章重点介绍了三个项目：佳能猫（Canon Cat）、Apple IIe 的 SwyftCard 和 Humane Environment 软件。

佳能猫使用 MAME 模拟，提供了一种键盘驱动、以文档为中心的工作流程。本文提供了有关导航模拟器及其怪癖的说明，例如禁用蜂鸣器以防止冻结。它强调了使用 LEAP 键进行导航和 USE FRONT 键进行特殊功能操作。

SwyftCard 同样是键盘驱动的，使用 Eric Rangell 为 KansasFest 2021 开发的软件进行模拟。本文详细介绍了在 Apple IIe 模拟器（Mariani、Virtual ][、AppleWin）中的设置过程，并解释了 LEAP 和 USE FRONT 键的功能、光标行为以及使用 Applesoft BASIC 的基本编程能力。它还介绍了将工作区保存和加载到磁盘以及串行通信。

Humane Environment 是拉斯金的软件实现，本文使用早期的 Mac OS 构建版本进行介绍。本文描述了如何在 Mac OS X Classic 或原生 Mac OS 9 中获取和运行这些构建版本，并使用 CVS 客户端来处理资源分支。文章引用了 SourceForge 上最后可用的构建版本，日期为 2003 年 9 月 25 日。

---

## 36. 马萨里克封存信件揭秘其建国理念

**原文标题**: Czech founding father Masaryk's message revealed in long-sealed envelope

**原文链接**: [https://www.nbcnews.com/world/europe/masaryk-message-revealed-envelope-czech-founding-father-rcna232353](https://www.nbcnews.com/world/europe/masaryk-message-revealed-envelope-czech-founding-father-rcna232353)

1927年托马斯·加里格·马萨里克（捷克斯洛伐克国父及首任总统）的密封信件在捷克共和国直播公开。这封自2005年起由国家档案馆保存的信件，此前备受猜测，有人担心其中可能包含关于欧洲冲突的命运警告。

这封信由马萨里克口述给他的儿子扬，并非马萨里克1937年去世前的最后遗言，而是他中风后对其时严重疾病的反思。在信中，马萨里克承认自己即将离世，表达了他毫不畏惧，并敦促他的继任者们谨慎地继续他的工作。他还反思了捷克斯洛伐克复杂的政治局势，这是一个种族多元化的国家，他敦促公平对待德国少数民族。

专家认为这封信意义重大，因为它写于一个动荡的时期——欧洲正经历着希特勒在德国崛起。马萨里克在捷克共和国备受尊敬，他于1918年至1935年担任总统，领导国家在一战后获得独立。他的儿子扬后来担任外交部长。这封信的公开揭示了马萨里克在捷克和欧洲历史关键时期的思想。

---

## 37. 三分钟居家测试或能识别与阿尔茨海默病相关的症状

**原文标题**: Three-Minute Take-Home Test May Identify Symptoms Linked to Alzheimer's Disease

**原文链接**: [https://www.smithsonianmag.com/smart-news/three-minute-take-home-test-may-identify-symptoms-linked-to-alzheimers-disease-years-before-a-traditional-diagnosis-180987281/](https://www.smithsonianmag.com/smart-news/three-minute-take-home-test-may-identify-symptoms-linked-to-alzheimers-disease-years-before-a-traditional-diagnosis-180987281/)

本文讨论了一种新的居家测试，名为快速眼动脑电图（Fastball EEG），它可能比传统的临床诊断更早地识别出与阿尔茨海默病相关的症状。这种由巴斯大学的研究人员开发的三分钟测试，在人们被动观看平板电脑上的图像时监测大脑活动。该测试不需要患者的主动参与，因此可能更容易获得且更客观。

发表在《大脑通讯》上的这项研究表明，快速眼动脑电图对已确诊的阿尔茨海默病患者和患病高风险人群都非常敏感。患有遗忘性轻度认知障碍（通常是阿尔茨海默病的前兆）的患者对该测试的反应较低。虽然该测试不能预测谁一定会患上阿尔茨海默病，但它可以识别出那些风险较高的人，从而可以进行更早的干预和规划。

鉴于多纳尼单抗 (donanemab) 和仑卡尼单抗 (lecanemab) 等新型阿尔茨海默病药物的出现，快速眼动脑电图的开发尤为重要，这些药物在疾病的早期阶段最为有效。早期检测使患者能够更早地开始治疗和生活方式干预。

虽然该研究显示出前景，但研究人员强调，需要在更大、更多样化的群体中进行更多研究，以确定该测试的预测能力以及它如何与其他诊断工具相互作用。专家们还强调了考虑可能导致记忆问题的其他健康并发症的重要性。尽管存在这些注意事项，快速眼动脑电图仍代表了阿尔茨海默病早期诊断和管理方面的一个潜在进步。

---

## 38. 八周内交付100台硬件设备

**原文标题**: Shipping 100 hardware units in under eight weeks

**原文链接**: [https://farhanhossain.substack.com/p/how-we-shipped-100-hardware-units](https://farhanhossain.substack.com/p/how-we-shipped-100-hardware-units)

无法访问文章链接。

---

## 39. 微型LED提升随机数生成

**原文标题**: Micro-LEDs boost random number generation

**原文链接**: [https://discovery.kaust.edu.sa/en/article/25936/micro-leds-boost-random-number-generation/](https://discovery.kaust.edu.sa/en/article/25936/micro-leds-boost-random-number-generation/)

研究人员利用微型LED开发出一种新型量子随机数发生器，实现千兆位级速度。由林赫明和欧文邦领导的来自KAUST、KACST和加州大学圣巴巴拉分校的团队，利用蓝色GaN微型LED自发辐射中的强度波动来生成真正的随机数。这种方法为现有的量子随机数发生器技术提供了一种紧凑、经济高效且节能的替代方案，对数据安全和复杂系统模拟至关重要。

与之前速度仅限于兆位级的基于LED的方法不同，这种新系统在每个采样周期提取六位，实现了9.375 Gbit/s的生成速率。该团队严格测试了微型LED量子随机数发生器，改变了尺寸和驱动电流，所有配置都成功通过了美国国家标准与技术研究院（NIST）的测试，确保了输出的随机性。

未来的研究将侧重于通过创建用于并行随机数生成的二维微型LED阵列来提高生成速率。该团队还计划将包括片上光电探测器在内的所有组件集成到单个量子随机数发生器芯片中，从而摆脱目前的分立元件设置，该设置包括温度稳定的微型LED、雪崩光电探测器和采样示波器。

---

## 40. R MCP 服务器

**原文标题**: R MCP Server

**原文链接**: [https://github.com/finite-sample/rmcp](https://github.com/finite-sample/rmcp)

RMCP（R模型上下文协议）服务器是一个使AI助手能够通过自然语言执行统计分析的工具。最新版本（0.3.7）包含9个类别共40个统计工具，例如回归分析、时间序列分析、数据转换、统计检验、描述性统计、计量经济学、机器学习、数据可视化和文件操作。它支持自然语言公式构建和智能错误恢复。

主要功能包括全面的统计分析、可视化工具，以及与Claude Desktop的兼容性，以便在对话中进行交互式绘图和统计分析。RMCP已可用于生产环境，完全符合JSON-RPC 2.0标准并支持传输无关性。真实的使用案例展示了其在商业分析、经济研究和数据科学中的应用。

该工具可以通过pip安装，需要安装R 4.0+以及特定的软件包。它为高级开发人员提供命令行界面和直接工具使用方式。涵盖的使用场景包括时间序列预测、面板数据分析、机器学习工作流程和统计检验。它提供完整的工具参考，包含描述和关键输出。用户场景的成功率达到100%。

---

## 41. 人工智能的四书凌乱史

**原文标题**: An untidy history of AI across four books

**原文链接**: [https://hedgehogreview.com/issues/lessons-of-babel/articles/perplexity](https://hedgehogreview.com/issues/lessons-of-babel/articles/perplexity)

本文批判了对人工智能的过度炒作，并将其与更现实、更“混乱”的历史视角进行了对比。文章认为，当前由行业推动，并被哈拉利、基辛格、施密特、蒙迪和库兹韦尔等人的著作放大的AI炒作，掩盖了AI的局限性和潜在危险，同时致富了那些控制该技术的人。

文章追溯了人工智能从其符号根源到机器学习和生成式人工智能的兴起。文章强调了技术进步中固有的偶然性、失败的共识和不可预测性，并将这种混乱的现实与人工智能爱好者宣扬的指数增长的简单叙事进行了对比。

《AI Snake Oil》的作者纳拉亚南和卡普尔被认为是提供了一个批判性的对立观点，他们敦促人们对人工智能的主张持怀疑态度，并强调了生成式人工智能和预测性人工智能之间的区别。文章批评了像哈拉利这样的作者的技术误解和战略省略，以及《Genesis》的作者推崇的末世论的AI观点，将AI比作一场“军备竞赛”，并加剧了生存焦虑。

最终，文章认为，对生存风险的关注分散了人们对人工智能真实和当下危害的注意力，例如不透明性和偏见，并允许科技公司操纵监管和金融市场。文章倡导采取一种更为审慎的方法，利用现有的社会工具来解决人工智能带来的实际挑战，而不屈服于推测性的恐惧。文章最后驳斥了库兹韦尔的“奇点”，认为这是一种原始形式的推断。

---

## 42. Slack 将我们的费用提高了每年 19.5 万美元。

**原文标题**: Slack has raised our charges by $195k per year

**原文链接**: [https://skyfall.dev/posts/slack](https://skyfall.dev/posts/slack)

2025年9月，为青少年提供编程教育的非营利组织Hack Club面临来自Slack的大幅涨价。此前，他们一直愉快地每年支付5,000美元使用Slack服务，但突然被告知，他们需要在一周内额外支付50,000美元，然后每年支付200,000美元，才能避免工作区被停用和消息历史记录被删除。

Hack Club认为这种突然涨价是勒索，并指出Slack的母公司Salesforce是在不给予充分通知的情况下强迫一家小型非营利组织。 短时间的通知产生了不利影响，迫使工作人员和志愿者仓促更新系统，重建集成，并迁移多年的机构知识。

作者强调了数据所有权的重要性，并建议其他小型企业考虑放弃Slack。 Hack Club由于这次经历选择迁移到Mattermost。

幸运的是，最初的帖子在Hacker News和Twitter上迅速传播开来，Slack的首席执行官联系了Hack Club并提供了一个解决方案。 最初的计划得以避免。 虽然细节仍然保密，但这证明是一个更好的结果。 这次磨难凸显了数据所有权的重要性，以及避免依赖外部SaaS提供商的必要性。

---

## 43. Node 20 将在 GitHub Actions 运行器上弃用

**原文标题**: Node 20 will be deprecated on GitHub Actions runners

**原文链接**: [https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/)

GitHub Actions 将弃用 Node 20 支持，计划于 2025 年秋季全面迁移至 Node 24。Node 20 将于 2026 年 4 月达到生命周期终点。

最新版本的 runner (v2.328.0) 同时支持 Node 20 和 Node 24，其中 Node 20 是默认版本。用户可以通过在其工作流程或 runner 环境中设置 `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` 来尽早测试 Node 24。

从 2026 年 3 月 4 日开始，runners 将默认使用 Node 24。用户可以通过设置 `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true` 暂时选择退出并继续使用 Node 20，但此选项将在 2026 年夏季 Node 20 完全移除后被删除。

重要兼容性说明：Node 24 与 macOS 13.4 及更低版本不兼容，并且缺乏官方的 ARM32 支持，这意味着 ARM32 上的自托管 runner 将不再受支持。

Action 维护者需要更新他们的 action 以在 Node 24 上运行。Action 用户需要更新他们的工作流程以使用与 Node 24 兼容的最新版本的 action。 建议用户加入 GitHub 社区中的讨论。

---

## 44. 诺斯特

**原文标题**: Nostr

**原文链接**: [https://nostr.com/](https://nostr.com/)

Nostr 是一个开放、去中心化的协议，用于创建抗审查的通信网络。 它采用客户端-中继架构，客户端充当用户代理，连接到多个中继（服务器）以发布和检索经过密码学签名的“笔记”。 中继充当分发中心，存储和传播这些笔记，但无法更改其内容。

该协议旨在提供一种通用的通信语言，允许不同的应用程序和客户端进行交互。 与中心化平台不同，Nostr 通过让用户控制他们的数据和中继连接来赋予他们权力。 用户可以选择他们的发件箱中继，根据需要切换中继，并且客户端会智能地跟踪这些更改，从而确保持续的信息流。

Nostr 拥抱一种混乱的、类似于早期互联网的方法，支持各种数据类型和用户交互。 它提倡结社自由，用户可以围绕中继创建社区，并允许个人运行自己的具有自定义规则的中继。

该文档还讨论了常见的担忧，如垃圾邮件、可扩展性、骚扰，以及 Nostr 相对于 Mastodon 和 Bluesky 等平台的优势。 它强调 Nostr 的架构自然地分配了网络负载，并且由于其密码学基础和多主方法，提供了更好的针对审查和数据中心化的弹性。 经济激励也与确保中继运营相一致。 它强调 Nostr 允许分布式社区，使用户可以使用针对其特定需求和偏好的中继。

---

## 45. 展示物理学

**原文标题**: Show the Physics

**原文链接**: [https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html](https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html)

展示物理学

---

## 46. 特朗普将对H-1B工作签证征收10万美元费用，白宫称

**原文标题**: Trump to impose $100k fee for H-1B worker visas, White House says

**原文链接**: [https://www.reuters.com/business/media-telecom/trump-mulls-adding-new-100000-fee-h-1b-visas-bloomberg-news-reports-2025-09-19/](https://www.reuters.com/business/media-telecom/trump-mulls-adding-new-100000-fee-h-1b-visas-bloomberg-news-reports-2025-09-19/)

路透社报道，据彭博新闻社报道，特朗普政府正在考虑对雇用H-1B签证员工的公司征收10万美元的新费用。这项费用将大大高于现有的H-1B签证费用。

报道称，拟议的费用被认为是增加收入的一种方式，并可能阻止公司雇用外国工人而非美国工人。其目的是使公司在某些职位上依赖H-1B签证在经济上不那么有吸引力。

虽然该报告中的细节很少，但拟议的费用增加被视为特朗普政府限制移民和优先考虑美国工人这一更广泛努力的延续。引发路透社报道的彭博社报告援引了熟悉此事的不具名消息来源。如果实施这样的费用，对于依赖技术娴熟的外国工人的公司以及整个科技行业的影响可能是巨大的。报告的主要关注点是时间和对H-1B签证计划的潜在影响。

---

## 47. Dynamo AI (YC W22) 招聘资深 Kubernetes 工程师

**原文标题**: Dynamo AI (YC W22) Is Hiring a Senior Kubernetes Engineer

**原文链接**: [https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer](https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer)

Dynamo AI 招聘资深 Kubernetes 工程师，负责客户导入和 AI 平台部署。

---

## 48. 想惹恼你的IT部门吗？ 链接看起来还不够恶意？

**原文标题**: Want to piss off your IT department? Are the links not malicious looking enough?

**原文链接**: [https://phishyurl.com/](https://phishyurl.com/)

本文介绍一款工具，该工具可生成看似恶意的URL，用于教育或娱乐目的。该工具的工作方式类似于URL缩短器，但不是缩短URL，而是使其*看起来*可疑，它本质上是一个重定向。

其核心功能包括输入合法的URL并接收一个“钓鱼”外观的URL作为输出。当点击这个新的URL时，它只是将用户重定向到原始的安全链接。

本文提供了自定义生成URL外观的选项：

*   **主题：** 用户可以选择一个主题来影响域名，使其看起来与加密货币、金融、网络钓鱼、在线购物、赌博、约会、科技、成人内容等主题相关。
*   **长度：** 用户可以调整URL的长度，范围从“短”到“超长”，或者选择随机的“让我崩溃吧！”选项。

本文强调，生成的“钓鱼”链接不会执行任何恶意操作；它仅仅重定向到提供的原始URL。它的目的显然是拿烦人的IT部门开玩笑，而不是用于恶意用途。

---

## 49. Show HN: AvoSmash – AI视频故事创作变得简单

**原文标题**: Show HN: AvoSmash – AI video storytelling made easy

**原文链接**: [https://avosmash.io/](https://avosmash.io/)

AvoSmash：一款AI驱动的视频叙事简化工具。

---

## 50. 人工智能云背后的4万亿美元会计难题

**原文标题**: The $4T accounting puzzle at the heart of the AI cloud

**原文链接**: [https://www.economist.com/business/2025/09/18/the-4trn-accounting-puzzle-at-the-heart-of-the-ai-cloud](https://www.economist.com/business/2025/09/18/the-4trn-accounting-puzzle-at-the-heart-of-the-ai-cloud)

无法访问文章链接。

---

## 51. 我解不开的算额难题

**原文标题**: Sangaku Puzzle I Can't Solve

**原文链接**: [https://samjshah.com/2025/08/05/sangaku-puzzle-i-cant-solve/](https://samjshah.com/2025/08/05/sangaku-puzzle-i-cant-solve/)

作者正苦苦思索一道算額难题：确定一个内切于正方形并与另外三个圆（两个半径等于正方形边长的四分之一圆，以及一个半径等于正方形边长一半的半圆）相切的小圆的半径。目标是证明小圆的半径是正方形边长 's' 的 4/33。

最初，作者尝试用坐标几何和微积分进行蛮力计算，结果得到了复杂且可能不正确的方程，于是便在网上寻求帮助。

几个人提供了建议，包括：

*   **笛卡尔圆定理：** 一位 Facebook 用户建议使用该定理，并提供了一个资源链接。另一个人独立地使用该定理和阿波罗尼奥斯问题方程解决了这个问题。
*   **反演：** 一位 BlueSky 用户建议以某个特定点为中心对平面进行反演。这会将圆变换成直线，从而简化问题。作者对此产生了兴趣，并观看了 Numberphile 解释反演的视频。其他人进一步阐述了反演方法，包括一个展示变换的 Desmos 表格，以及关于如何反演回解的解释。
*   **三边测量：** 另一个建议是将问题构建为一个三边测量问题。
*   **坐标系：** 有人建议使用一个更基本的坐标系方法，包含三个方程。
*   **Japheth W 的解法：** 一位朋友提供了他手写的，尽管有些杂乱无章的解法。

作者的帖子详细描述了他们解决这个问题的令人沮丧但又引人入胜的旅程，突出了其他人提出的各种方法以及他们最初的反应。该帖子表达了对一个清晰而优雅的解决方案的渴望，以解释 4/33s 的关系。

---

## 52. 帮助我们筹集20万美元，使JavaScript摆脱甲骨文的控制。

**原文标题**: Help us raise $200k to free JavaScript from Oracle

**原文链接**: [https://deno.com/blog/javascript-tm-gofundme](https://deno.com/blog/javascript-tm-gofundme)

瑞恩·达尔于2025年9月18日发文，呼吁公众支持筹集20万美元，以使“JavaScript”一词摆脱甲骨文的商标控制。在关于该商标的公开信获得超过27000个签名后，Deno向美国专利商标局发起了撤销申请。目标是使“JavaScript”进入公共领域，允许开发者、作者和公司不受限制地使用。

这笔资金用于支付联邦诉讼的证据开示阶段的费用。这包括专业的公众调查，以证明该术语的通用用法；来自学术界和工业界的专家证人，就JavaScript的历史和用法作证；来自相关组织的取证和记录，证明甲骨文未参与该语言的开发；以及反驳甲骨文主张的法律文件。

甲骨文官方否认“JavaScript”是一个通用术语，但达尔认为这是不言而喻的，商标制度不应允许公司垄断常用术语。文章敦促读者查看请愿书和公开信，以全面了解法律论据。

作者强调了此案的重要性，声明如果甲骨文胜诉，将破坏商标制度的完整性，并授权公司控制通用术语。任何剩余资金将捐赠给OpenJS基金会，以捍卫数字领域的公民自由。文章最后呼吁捐款、分享和支持该活动。

---

## 53. 星前天文台

**原文标题**: Starfront Observatories

**原文链接**: [https://starfront.space/](https://starfront.space/)

星前沿天文台提供顶级的远程望远镜托管服务，让世界一流的远程望远镜成像和黑暗天空触手可及。他们提供各种尺寸的底座，适用于不同的望远镜设置，从小型星特朗型号到大型专业级设备，月费从 99 美元到 399 美元不等。

该天文台拥有 Bortle 1 级黑暗天空的地理位置和先进的卷帘式屋顶设施。客户评价强调了知识渊博且反应迅速的技术支持团队、他们快速的安装服务以及有效排除技术问题的能力。 许多评论者强调了卓越的客户服务以及通过星前沿的 Discord 频道培养的社区意识。

客户还赞扬该设施的地理位置、从该地点获得的高质量图像以及经济实惠的价格所带来的整体价值。星前沿天文台旨在提供卓越的远程天文摄影体验，让每个人都能体验到。 他们鼓励用户预订底座并加入他们的社区。

---

## 54. AI的经济影响：多学科、多本书评 [pdf]

**原文标题**: The Economic Impacts of AI: A Multidisciplinary, Multibook Review [pdf]

**原文链接**: [https://kevinbryanecon.com/BryanAIBookReview.pdf](https://kevinbryanecon.com/BryanAIBookReview.pdf)

此PDF文档似乎是关于人工智能（AI）经济影响的多学科书籍评论的提纲或目录。该文档结构清晰，包含指向不同章节的内部链接，表明其对该主题进行了全面的概述。

链接章节的标题暗示了评论的范围，可能涵盖：

*   **导论：** 为讨论人工智能的经济影响奠定基础。
*   **硅谷的视角：** 考察人工智能开发参与者的信念和期望。
*   **第二次机器时代：** 引用一本探讨技术变革潜力的书籍。
*   **人工智能作为预测机器：** 侧重于人工智能在预测方面的能力及其经济影响。
*   **数据与宏观经济：** 探讨数据在驱动人工智能中的作用及其对更广泛经济格局的影响。
*   **实践应用：** 关注人工智能技术的实际应用。
*   **来自加州的视角：** 提供关于人工智能经济影响的区域视角，可能侧重于科技产业。
*   **尚未解决的重大问题：** 识别并讨论与人工智能和经济相关的重大未解决问题和未来发展方向。

根据注释，该评论引用了Acemoglu、Agrawal、Altman、Aschenbrenner、Baley、Beane、Brynjolfsson、Bullock、Goodfellow、Lucas、Mollick、Nordhaus和Vandehei等人的著作，表明这是一项研究充分且彻底的分析。脚注还表明文章中包含更多信息和参考资料。

---

## 55. 展示 HN：Arrow JavaScript，无需框架的响应式

**原文标题**: Show HN: Arrow JavaScript, Reactivity Without the Framework

**原文链接**: [https://www.arrow-js.com/docs/](https://www.arrow-js.com/docs/)

此篇“Show HN”帖子介绍 ArrowJS，一个无需特定框架即可提供响应式功能的 JavaScript 库。本质上，ArrowJS 旨在通过提供可集成到现有项目中的响应式原语来简化动态和响应式用户界面的构建，无论这些项目使用何种框架（或者没有框架）。

该帖子链接到该库的文档和 GitHub 存储库，暗示用户可以通过这些资源了解更多关于其特性和用法的信息。“Star”该项目的呼吁表明它是一个新发布的项目，正在寻求社区支持和可见性。最后，一个指向 Twitter 帐户的链接提供了一种方式来随时了解该项目的开发和公告。总而言之，ArrowJS 将自己定位为为 JavaScript 应用程序添加响应式功能的轻量级解决方案，提供一种框架无关的替代方案。

---

## 56. 迷你：色调映射 (2023)

**原文标题**: Mini: Tonemaps (2023)

**原文链接**: [https://mini.gmshaders.com/p/tonemaps](https://mini.gmshaders.com/p/tonemaps)

本文“Mini: 色调映射 (2023)” 探讨了着色器中色彩发灰和色阶断层的问题，尤其是在亮度值超出标准8位色彩的0.0到1.0范围时。作者Xor解释说，简单地钳制数值会导致不自然的颜色过渡。

解决方案是色调映射，它可以平滑地将高亮度值映射回0.0到1.0范围，从而保持色彩准确性。本文展示了几种色调映射函数，包括ACES、Uncharted 2、Unreal和一个自定义的Tanh函数，每种函数都提供不同的曲线和视觉效果。作者强调，钳制后的色调映射是一条直线，这会导致不自然的效果。我们的眼睛非常擅长注意到亮度变化，以及这些变化突然停止的时候。

然后，Xor介绍了HDR（高动态范围）渲染的概念，其中使用了超出0到1范围的颜色，通常需要使用`surface_rgba16float`或`surface_rgba32float`格式进行中间计算，然后再色调映射回LDR（低动态范围）。他以他的MandelBots项目为例，解释了切换到HDR表面如何通过避免颜色发灰和颜色变化来改善光照。

总而言之，本文强调，色调映射可以通过直接对shader输出进行色调映射或利用HDR表面进行中间计算来解决过度曝光和色彩发灰的问题，尤其是在混合多个光源时。

---

## 57. 改造旧电视作为礼物（2019）

**原文标题**: Revamping an Old TV as a Gift (2019)

**原文链接**: [https://blog.davidv.dev/posts/revamping-an-old-tv-as-a-gift/](https://blog.davidv.dev/posts/revamping-an-old-tv-as-a-gift/)

2017年，作者将跳蚤市场淘到的一台老式电视机改造成了一份50岁生日礼物送给父亲，旨在实现无缝的70-80年代电视体验。核心项目是将树莓派集成进去，播放复古节目。

技术挑战在于如何让树莓派的复合视频输出在电视上显示。这个问题通过使用复合射频调制器转换信号解决。电视调谐器固定在调制器的输出频道上。为了恢复使用原始调谐旋钮切换频道的能力，作者使用了一个连接到树莓派GPIO的多极旋转开关，创建了基于软件的频道。

树莓派（5V）和射频调制器（9V）的电源来自电视机的12V电压轨，使用了LM7809和LM7805稳压器。

最初，软件的目标是每个频道随机选择节目和广告。然而，由于gstreamer的问题，作者最终为每个频道创建了8小时长的视频文件，并预先嵌入了广告。关机时会保存最近关键帧的时间戳，以便在开机后从同一位置恢复播放。

该项目最终产生了一台功能齐全、独立的、具有软件控制频道的老式电视机。作者还创建了一个虚假的包裹追踪网站作为额外的点缀。该项目受到了另一个类似项目的启发，但作者的目标是提供一个更加独立的电视解决方案。

---

## 58. 使用R语言的统计物理：基于蒙特卡洛方法的伊辛模型

**原文标题**: Statistical Physics with R: Ising Model with Monte Carlo

**原文链接**: [https://github.com/msuzen/isingLenzMC](https://github.com/msuzen/isingLenzMC)

该R包"isingLenzMC"提供了使用 Metropolis 和 Glauber Monte Carlo 方法，并采用单自旋翻转动力学在周期性边界条件下模拟一维经典 Ising 模型的工具。 Ising 模型本身是统计物理学中的一个基础系统，与理解自旋玻璃、磁性材料以及更广泛的合作现象（如相变和神经网络）相关。 该软件包还包括用于计算精确解的函数。 该软件包及其相关研究，主要由 Mehmet Suezen 撰写，探讨了 Ising 模型的动力学和使用单自旋翻转动力学的有效遍历性概念。 两篇相关的出版物突出了这一重点：“单自旋翻转动力学中的有效遍历性”（Phys. Rev. E 90, 032141）和 arXiv 预印本“收敛到有效遍历性中的异常扩散”（arXiv:1606.08693），这两者都与可能与模拟相关的数据集相关联。 本质上，“isingLenzMC”允许研究人员和学生以计算方式探索 Ising 模型和相关的理论概念，如遍历性。

---

## 59. Ruby Central 对 RubyGems 的攻击 [pdf]

**原文标题**: Ruby Central's Attack on RubyGems [pdf]

**原文链接**: [https://pup-e.com/goodbye-rubygems.pdf](https://pup-e.com/goodbye-rubygems.pdf)

很抱歉，我无法满足该请求。所提供的内容并非人类可读文本，它似乎是一个二进制PDF文件，而非文本文档，其中包含编码数据和可能的恶意代码，无法转换为人类可读文本。

---

## 60. 善于代码审查者，亦善用人工智能助手。

**原文标题**: If you are good at code review, you will be good at using AI agents

**原文链接**: [https://www.seangoedecke.com/ai-agents-and-code-review/](https://www.seangoedecke.com/ai-agents-and-code-review/)

代码审查能力对高效使用AI编码助手的至关重要性

---

## 61. 3D打印名片压花器

**原文标题**: A 3D-Printed Business Card Embosser

**原文链接**: [https://www.core77.com/posts/138492/A-3D-Printed-Business-Card-Embosser](https://www.core77.com/posts/138492/A-3D-Printed-Business-Card-Embosser)

这篇 Core77 文章介绍了由埃因霍温的产品设计师 Igor Daemen 设计的 3D 打印名片压花器。Daemen 将压花器设计成模块化，易于 3D 打印且无需支撑，并且无需任何硬件即可组装。他指出，严格的公差对于成功打印至关重要，并建议使用 Basic PLA 以获得最佳效果。设计文件可供免费下载。

文章还包含了一些读者的评论。一位读者对 PLA 材料因强度低而是否适合用于压缩模具表示怀疑。另一位读者则幽默地评论了名片的普遍性。

除了压花器之外，这篇文章还宣传了 Core77 的工业设计资源，包括工业设计公司目录。它还宣传了 Core77 新闻通讯，并强调了该网站需要 Cookie 才能实现最佳功能。

---

## 62. Xmonad 寻求 Wayland 移植帮助 (2023)

**原文标题**: Xmonad seeking help for Wayland port (2023)

**原文链接**: [https://xmonad.org/news/2023/10/06/wayland.html](https://xmonad.org/news/2023/10/06/wayland.html)

XMonad开发团队正在寻找一位开发者，协助将XMonad移植到Wayland。经过两年的捐助积累，他们现在有资金聘请人员完成这项任务。现有的Wayland移植项目被认为过于陈旧且漏洞百出，难以挽救。一个重大挑战是Wayland程序无法提供独特的标识符，这将影响`appName`和`className`管理钩子的功能。XMonad团队正在征集方案，并在原文链接的Discourse论坛中展开讨论。

---

## 63. 英伟达收购英特尔50亿美元股份

**原文标题**: Nvidia buys $5B in Intel

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal](https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal)

令人震惊的是，英伟达和英特尔宣布合作开发新一代x86产品，标志着科技行业的重大转变。此次合作包括面向游戏PC的“英特尔x86 RTX SOC”，通过NVLink将英特尔CPU与英伟达RTX GPU芯片融合。英伟达还将使用英特尔为其人工智能产品构建定制的x86数据中心CPU。为巩固合作关系，英伟达将购买价值50亿美元的英特尔普通股，持有5%的股份。

这些产品尚处于早期开发阶段，发布时间尚未确定，预计将在一年或更长时间后推出。英伟达强调其对多代路线图的承诺，并继续其现有的产品线，包括基于Arm的处理器。目前尚不清楚这些产品是否将由英特尔代工厂生产，但这是一种可能性。新的英特尔x86 RTX SOC将直接与AMD的APU在轻薄游戏笔记本电脑和小型PC市场竞争。值得注意的是，新的SOC将使用NVLink来实现CPU和GPU之间更快的通信，并具有统一的内存访问。

英特尔还将为英伟达制造定制的x86数据中心CPU，利用NVLink接口。英伟达对英特尔的50亿美元投资是在美国政府和软银类似投资之后进行的，共同增强了英特尔在与台积电竞争中的财务状况。英伟达和英特尔的首席执行官都强调了此次合作的战略优势，包括扩展生态系统和为下一代计算奠定基础。

---

## 64. 安全点与Fil-C

**原文标题**: Safepoints and Fil-C

**原文链接**: [https://fil-c.org/safepoints](https://fil-c.org/safepoints)

本文解释了安全点（Safepointing），它是现代虚拟机（VM）例如 Fil-C 和 JVM 中的一种关键同步机制，尤其对于垃圾回收（GC）。安全点使线程能够对虚拟机的状态做出假设并报告其当前状态，从而确保 GC 的健全性，并实现安全信号处理和 fork 等功能。

本文解决的核心问题是如何确保 GC 能够准确地扫描内存中的存活对象，因为多个线程可能正在竞争，从而可能将指针留在寄存器或 GC 未知的内存位置。安全点通过在编译后的代码中插入“安全点”来解决这个问题，编译器在这些安全点提供关于指针位置的信息。GC 只会在这些安全点抢占线程。

Fil-C 通过在反向控制流边沿插入轮询检查（pollchecks）来实现安全点。这些轮询检查检查来自 GC 的请求，例如启动软握手。Fil-C 还使用 Pizderson 帧来跟踪跨越轮询检查的存活指针，确保 GC 可以访问它们。

GC 通过“软握手”机制与线程同步，请求动作（例如，缓存清除）并等待线程在它们的下一个安全点执行这些动作。本文还介绍了 Fil-C 如何使用 `filc_enter` 和 `filc_exit` 函数处理本机代码调用，并讨论了安全点如何保护存储和加载屏障以及处理线程本地缓存。最后，本文重点介绍了安全点在信号处理和实现 `fork(2)` 中的作用。

---

## 65. Fortran与RSA：9月20日

**原文标题**: Fortran and RSA: September 20th

**原文链接**: [https://blog.aurevow.com/posts/fortran-and-rsa-september-20th/](https://blog.aurevow.com/posts/fortran-and-rsa-september-20th/)

文章“Fortran与RSA：9月20日”探讨了作者使用Fortran语言实现RSA加密算法的经验。作者解释了选择Fortran的动机，提到其数值计算能力以及任意精度算术库（特别是使用gfortran的`mpif.h`）的可用性。

这篇博文详细介绍了RSA的实现过程，突出了遇到的挑战和解决方案。涵盖的关键方面包括：

*   **任意精度算术：** 使用`mpif.h`处理RSA所需的大整数，这些整数远大于标准整数类型。作者承认该库的一些局限性，并指出适当内存管理的重要性。
*   **密钥生成：** 作者概述了生成RSA密钥的步骤，包括寻找大素数。他们提到为此目的实现了Miller-Rabin素性测试。
*   **加密与解密：** 该文章简要描述了使用RSA加密和解密消息的数学公式。
*   **代码片段：** 文章包含Fortran代码片段，展示了RSA算法中关键函数的实现，例如模幂运算（可能使用平方求幂法）。

作者最后总结了该项目，强调了在Fortran中实现加密算法的可行性，即使在某些领域（如字符串操作）存在一些局限性。该项目证明了Fortran在数值和计算任务中（在精确算术至关重要的情况下）的持续相关性。他们建议可以进一步优化代码，但强调了该项目在创建功能性RSA实现方面的成功。

---

## 66. 我后悔花了三千美元搭建这个树莓派AI集群了。

**原文标题**: I regret building this $3000 Pi AI cluster

**原文链接**: [https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster](https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster)

Jeff Geerling regrets building a $3000 Raspberry Pi AI cluster, finding its performance underwhelming despite having 160GB of RAM. After a two-year wait for the Compute Blades, he upgraded to CM5 modules, only to discover their limitations for AI and HPC tasks.

The cluster build was plagued by unreliable SSDs and thermal throttling, requiring multiple rebuilds. Benchmarking revealed it's 4 times slower than his $8,000 Framework Desktop cluster in HPC tasks, although slightly more energy-efficient.

For AI, the cluster's performance was severely limited due to the inability of llama.cpp to utilize the Pi 5 iGPU, resulting in slow CPU-powered inference. Large AI models required distribution across multiple Pis, leading to significantly slower token generation compared to the Framework cluster.

While not a powerhouse, the Pi cluster's efficiency, quietness, and compact size could be advantageous for density-critical applications like CI jobs, high-security edge deployments, or Tor exit relays.

Ultimately, Geerling concludes that for most users, the cluster's cost and performance don't justify its niche benefits. He mentions Gateworks' discontinued industrial Compute Blade as another example of the lackluster popularity of compute blades in general. He thanks his supporters and provides a list of components used in the build.


---

## 67. The Ruliology of Lambdas

**原文标题**: The Ruliology of Lambdas

**原文链接**: [https://writings.stephenwolfram.com/2025/09/the-ruliology-of-lambdas/](https://writings.stephenwolfram.com/2025/09/the-ruliology-of-lambdas/)

生成摘要时出错

---

## 68. Frying Eggs and Air Quality Tests

**原文标题**: Frying Eggs and Air Quality Tests

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/frying-eggs-and-air-quality-tests](https://chillphysicsenjoyer.substack.com/p/frying-eggs-and-air-quality-tests)

生成摘要时出错

---

## 69. Cyber-attack causes delays at Heathrow and other European airports

**原文标题**: Cyber-attack causes delays at Heathrow and other European airports

**原文链接**: [https://www.bbc.co.uk/news/articles/c3drpgv33pxo](https://www.bbc.co.uk/news/articles/c3drpgv33pxo)

生成摘要时出错

---

## 70. Are you an experienced software buyer? I could use some help

**原文标题**: Are you an experienced software buyer? I could use some help

**原文链接**: [https://charity.wtf/2025/09/19/are-you-an-experienced-software-buyer-i-could-use-some-help/](https://charity.wtf/2025/09/19/are-you-an-experienced-software-buyer-i-could-use-some-help/)

生成摘要时出错

---

## 71. Playing “Minecraft” without Minecraft (2024)

**原文标题**: Playing “Minecraft” without Minecraft (2024)

**原文链接**: [https://lenowo.org/viewtopic.php?t=5](https://lenowo.org/viewtopic.php?t=5)

生成摘要时出错

---

## 72. Time Spent on Hardening

**原文标题**: Time Spent on Hardening

**原文链接**: [https://third-bit.com/2025/09/18/time-spent-on-hardening/](https://third-bit.com/2025/09/18/time-spent-on-hardening/)

生成摘要时出错

---

## 73. The health benefits of sunlight may outweigh the risk of skin cancer

**原文标题**: The health benefits of sunlight may outweigh the risk of skin cancer

**原文链接**: [https://www.economist.com/science-and-technology/2025/09/17/the-health-benefits-of-sunlight-may-outweigh-the-risk-of-skin-cancer](https://www.economist.com/science-and-technology/2025/09/17/the-health-benefits-of-sunlight-may-outweigh-the-risk-of-skin-cancer)

生成摘要时出错

---

## 74. The Fisherman and His Wife (1857)

**原文标题**: The Fisherman and His Wife (1857)

**原文链接**: [https://sites.pitt.edu/~dash/grimm019.html](https://sites.pitt.edu/~dash/grimm019.html)

生成摘要时出错

---

## 75. Llama-Factory: Unified, Efficient Fine-Tuning for 100 Open LLMs

**原文标题**: Llama-Factory: Unified, Efficient Fine-Tuning for 100 Open LLMs

**原文链接**: [https://github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

生成摘要时出错

---

## 76. Overcoming barriers of hydrogen storage with a low-temperature hydrogen battery

**原文标题**: Overcoming barriers of hydrogen storage with a low-temperature hydrogen battery

**原文链接**: [https://www.isct.ac.jp/en/news/okmktjxyrvdc](https://www.isct.ac.jp/en/news/okmktjxyrvdc)

生成摘要时出错

---

## 77. Tracking trust with Rust in the kernel

**原文标题**: Tracking trust with Rust in the kernel

**原文链接**: [https://lwn.net/Articles/1034603/](https://lwn.net/Articles/1034603/)

生成摘要时出错

---

## 78. Launch HN: Cactus (YC S25) – AI inference on smartphones

**原文标题**: Launch HN: Cactus (YC S25) – AI inference on smartphones

**原文链接**: [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus)

生成摘要时出错

---

## 79. I'm Not a Robot Game

**原文标题**: I'm Not a Robot Game

**原文链接**: [https://neal.fun/not-a-robot/](https://neal.fun/not-a-robot/)

生成摘要时出错

---

## 80. Pnpm has a new setting to stave off supply chain attacks

**原文标题**: Pnpm has a new setting to stave off supply chain attacks

**原文链接**: [https://pnpm.io/blog/releases/10.16](https://pnpm.io/blog/releases/10.16)

生成摘要时出错

---

## 81. Rules for creating good-looking user interfaces

**原文标题**: Rules for creating good-looking user interfaces

**原文链接**: [https://weberdominik.com/blog/rules-user-interfaces/](https://weberdominik.com/blog/rules-user-interfaces/)

生成摘要时出错

---

## 82. WASM 3.0 Completed

**原文标题**: WASM 3.0 Completed

**原文链接**: [https://webassembly.org/news/2025-09-17-wasm-3.0/](https://webassembly.org/news/2025-09-17-wasm-3.0/)

生成摘要时出错

---

## 83. FLX1s 正式发布

**原文标题**: FLX1s Is Launched

**原文链接**: [https://furilabs.com/flx1s-is-launched/](https://furilabs.com/flx1s-is-launched/)

生成摘要时出错

---

## 84. This website has no class

**原文标题**: This website has no class

**原文链接**: [https://aaadaaam.com/notes/no-class/](https://aaadaaam.com/notes/no-class/)

This article details the author's experiment in building a website completely without CSS classes. Motivated by the idea of treating HTML elements as pre-built components, the author sought to eliminate classes and rely solely on tag selectors, custom tags, and custom attributes for styling.

The process began with increased use of semantic HTML and contextual styling, leveraging CSS nesting, `:where()`, and `:has()` pseudo-classes. However, the author found this approach led to overly complex and esoteric selector patterns.

The solution involved using custom tag names and custom attributes, inspired by web component patterns but without using JavaScript. Custom tag names like `<note-pad>` were used for component styling, while custom attributes like `shape-type="1"` handled variations, offering a semantic alternative to BEM modifiers.

The result was a reduction in CSS file size and improved accessibility due to increased focus on semantic markup. However, the author acknowledges the approach requires more careful planning and a holistic understanding of the site's structure. While happy with the results on a personal website, the author is hesitant to recommend it for larger projects with diverse skillsets.

Despite not fully achieving classlessness due to a syntax highlighting plugin, the author believes this experiment will significantly influence their future work, questioning the long-held acceptance of CSS classes in web development.


---

## 85. Midcentury North American Restaurant Placemats

**原文标题**: Midcentury North American Restaurant Placemats

**原文链接**: [https://casualarchivist.substack.com/p/order-up](https://casualarchivist.substack.com/p/order-up)

生成摘要时出错

---

## 86. U.S. already has the critical minerals it needs, according to new analysis

**原文标题**: U.S. already has the critical minerals it needs, according to new analysis

**原文链接**: [https://www.minesnewsroom.com/news/us-already-has-critical-minerals-it-needs-theyre-being-thrown-away-new-analysis-shows](https://www.minesnewsroom.com/news/us-already-has-critical-minerals-it-needs-theyre-being-thrown-away-new-analysis-shows)

生成摘要时出错

---

## 87. Linux for Nintendo 64 (1997)

**原文标题**: Linux for Nintendo 64 (1997)

**原文链接**: [https://web.archive.org/web/19990220141243/http://www.heise.de/ix/artikel/E/1997/04/036/](https://web.archive.org/web/19990220141243/http://www.heise.de/ix/artikel/E/1997/04/036/)

生成摘要时出错

---

## 88. As Android developer verification gets ready to go, a new reason to be worried

**原文标题**: As Android developer verification gets ready to go, a new reason to be worried

**原文链接**: [https://www.androidauthority.com/android-sideload-offline-3598988/](https://www.androidauthority.com/android-sideload-offline-3598988/)

生成摘要时出错

---

## 89. Apple Photos app corrupts images

**原文标题**: Apple Photos app corrupts images

**原文链接**: [https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/](https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/)

生成摘要时出错

---

## 90. As Android developer verification gets ready to go, a new reason to be worried

**原文标题**: As Android developer verification gets ready to go, a new reason to be worried

**原文链接**: [https://www.androidauthority.com/android-sideload-offline-3598988/](https://www.androidauthority.com/android-sideload-offline-3598988/)

生成摘要时出错

---

## 91. Leatherman (vagabond)

**原文标题**: Leatherman (vagabond)

**原文链接**: [https://en.wikipedia.org/wiki/Leatherman_(vagabond)](https://en.wikipedia.org/wiki/Leatherman_(vagabond))

生成摘要时出错

---

## 92. The Sagrada Família takes its final shape

**原文标题**: The Sagrada Família takes its final shape

**原文链接**: [https://www.newyorker.com/magazine/2025/09/22/is-the-sagrada-familia-a-masterpiece-or-kitsch](https://www.newyorker.com/magazine/2025/09/22/is-the-sagrada-familia-a-masterpiece-or-kitsch)

生成摘要时出错

---

## 93. OpenTelemetry collector: What it is, when you need it, and when you don't

**原文标题**: OpenTelemetry collector: What it is, when you need it, and when you don't

**原文链接**: [https://oneuptime.com/blog/post/2025-09-18-what-is-opentelemetry-collector-and-why-use-one/view](https://oneuptime.com/blog/post/2025-09-18-what-is-opentelemetry-collector-and-why-use-one/view)

生成摘要时出错

---

## 94. This map is not upside down

**原文标题**: This map is not upside down

**原文链接**: [https://www.maps.com/this-map-is-not-upside-down/](https://www.maps.com/this-map-is-not-upside-down/)

生成摘要时出错

---

## 95. Apple: SSH and FileVault

**原文标题**: Apple: SSH and FileVault

**原文链接**: [https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html](https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html)

生成摘要时出错

---

## 96. Trevor Milton's Nikola case dropped by SEC following Trump pardon

**原文标题**: Trevor Milton's Nikola case dropped by SEC following Trump pardon

**原文链接**: [https://eletric-vehicles.com/nikola/trevor-miltons-nikola-case-dropped-by-sec-following-trump-pardon/](https://eletric-vehicles.com/nikola/trevor-miltons-nikola-case-dropped-by-sec-following-trump-pardon/)

生成摘要时出错

---

## 97. Grief gets an expiration date, just like us

**原文标题**: Grief gets an expiration date, just like us

**原文链接**: [https://bessstillman.substack.com/p/oh-fuck-youre-still-sad](https://bessstillman.substack.com/p/oh-fuck-youre-still-sad)

生成摘要时出错

---

## 98. TIC-80 – Tiny Computer

**原文标题**: TIC-80 – Tiny Computer

**原文链接**: [https://tic80.com/](https://tic80.com/)

生成摘要时出错

---

## 99. New York Signs into Law the Algorithmic Pricing Disclosure Act

**原文标题**: New York Signs into Law the Algorithmic Pricing Disclosure Act

**原文链接**: [https://www.bclplaw.com/en-US/events-insights-news/new-yorks-sweeping-algorithmic-pricing-reforms-what-retailers-need-to-know.html](https://www.bclplaw.com/en-US/events-insights-news/new-yorks-sweeping-algorithmic-pricing-reforms-what-retailers-need-to-know.html)

生成摘要时出错

---

## 100. The Many Broken Feeds

**原文标题**: The Many Broken Feeds

**原文链接**: [https://notes.abhinavsarkar.net/2025/broken-feeds](https://notes.abhinavsarkar.net/2025/broken-feeds)

生成摘要时出错

---

