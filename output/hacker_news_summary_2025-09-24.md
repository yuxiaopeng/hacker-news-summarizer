# Hacker News 热门文章摘要 (2025-09-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 陶哲轩：小型组织在社会中的作用已显著缩小。

**原文标题**: Terence Tao: The role of small organizations in society has shrunk significantly

**原文链接**: [https://mathstodon.xyz/@tao/115259943398316677](https://mathstodon.xyz/@tao/115259943398316677)

这篇文章实际上是陶哲轩在Mastodon上发布的一则帖子。根据提供的内容，这似乎是更深入讨论的起点，而非一篇完整的文章。其中提到了“关于当前Ze…的一些零散的想法”，暗示该主题与“Ze”相关（可能指代代词，或使用“Ze”的特定组织/话题）。

因此，基于提供的标题和内容（主要是一个链接和一段简短的介绍性短语），以下是一个重点关注可获取信息的摘要：

陶哲轩正在Mastodon上发起一场讨论，开篇语是“关于当前Ze…的一些零散的想法”。帖子的标题“陶哲轩：小型组织在社会中的作用已显著缩小”可能代表了陶哲轩希望在讨论中提出的核心论点。他似乎认为小型组织在当今社会中拥有的权力和影响力较小。关于讨论的其余部分，只能通过访问Mastodon帖子本身来获取。我们只有陶哲轩的初始声明和隐含的整体主题。

---

## 2. Yt-dlp：YouTube下载即将迎来新要求

**原文标题**: Yt-dlp: Upcoming new requirements for YouTube downloads

**原文链接**: [https://github.com/yt-dlp/yt-dlp/issues/14404](https://github.com/yt-dlp/yt-dlp/issues/14404)

此公告详细说明了yt-dlp即将进行的更改，这些更改要求用户安装Deno JavaScript运行时，才能使YouTube下载继续正常工作。YouTube已对其JavaScript挑战进行了更改，导致yt-dlp的内置解释器不足以应对。

所需操作取决于yt-dlp的安装方式：

*   **官方PyInstaller捆绑的可执行文件用户（.exe, _macos, _linux）：** 只需要安装Deno。
*   **PyPI软件包用户 (pip, pipx)：** 使用`default`可选依赖组更新yt-dlp：`pip install -U "yt-dlp[default]"`。
*   **官方zipimport二进制文件用户 (Unix executable)：** 可以使用一个新标志（名称待定）运行yt-dlp以允许Deno下载npm依赖项，或者在其Python环境中安装yt-dlp的JS求解器软件包（软件包名称待定）。
*   **第三方软件包用户（pacman, brew）：** 请按照存储库维护者提供的说明进行操作，或使用针对zipimport二进制文件用户描述的方法。

本质上，几乎所有用户都需要安装Deno，并可能需要更新其yt-dlp安装方法以包含必要的JavaScript组件。预计后续将发布更具体的说明，特别是针对zipimport用户。

---

## 3. Zed 的定价已变更：LLM 使用现已基于 Token。

**原文标题**: Zed's Pricing Has Changed: LLM Usage Is Now Token-Based

**原文链接**: [https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based](https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based)

Zed 即日起对新用户实行基于 Token 的 AI 定价，现有用户将在三个月内过渡。此举旨在使定价与运行 AI 的实际成本保持一致，解决先前系统效率低下和激励机制错位的问题。

新的定价模式简化了成本，同时扩展了 AI 模型的访问权限。Pro 计划从每月 20 美元降至 10 美元，免费计划保持免费。Pro 用户现在每月获得 5 美元的 Token 额度，额外使用按 API 标价 + 10% 收费。Zed 还将在其托管服务中添加 GPT-5、Gemini 2.5 Pro/Flash 和其他模型。

Zed 强调，它仍将提供无需付费的 AI 功能。他们提供了大量托管服务的替代方案，包括自带 API 密钥、使用像 Ollama 这样的本地模型以及利用第三方代理。用户也可以完全禁用 AI 功能。

转向基于 Token 的定价使 Zed 能够可持续地投资于其核心编辑器功能，专注于企业销售并改善开发者协作。他们认为，新系统提供了更好的激励机制，降低了复杂性，并允许在编辑器中更灵活地使用 AI。

现有 Pro 客户可以在 2025 年 12 月 17 日之前迁移。免费和试用用户将更快过渡，并将获得一个新的 14 天 Pro 试用期，并提供 20 美元的 Token 额度。

---

## 4. Product Hunt 已死

**原文标题**: Product Hunt Is Dead

**原文链接**: [https://sedimental.org/product_hunt_is_dead.html](https://sedimental.org/product_hunt_is_dead.html)

本文认为，尽管表面上看起来并非如此，但Product Hunt (PH) 实际上已经名存实亡。作者在推出自己的财务规划平台FinFam时，观察到一些令人担忧的趋势，从而得出这一结论。

作者指出，PH的太平洋标准时间午夜每日重置，严重偏袒了欧洲、亚太地区，尤其是印度的受众。更令人担忧的是，作者发现可以通过付费服务，以低至100美元的价格，通过人工点赞来保证前五名的位置。这使得获取真实的用户反馈和流量变得困难。作者认为，这些不是真正的用户，对长期增长没有价值。

作者承认PH试图通过“精选”发布来管理首页，但他认为这导致大多数发布永远不会被看到。他认为这些精选功能的应用是不透明的，而且很可能与某种形式的盈利有关。

作者认为，PH的根本问题在于其只关注新产品，从而阻碍了健康社区的发展。他将PH与Indie Hackers（由共同价值观团结在一起）和AlternativeTo（致力于收录所有软件，而不仅仅是最新的）等平台进行了对比。

最终，作者得出结论，Product Hunt 不再是发布产品的有价值的平台，并呼吁重新评估其用处，同时提出了 Betalist、Peerlist 和 Indie Hackers 等替代方案。最后，作者以一个关于吉祥物的笑话结尾，建议应该将它换成一只鸭子。

---

## 5. SedonaDB：一个用 Rust 编写的全新地理空间 DataFrame 库

**原文标题**: SedonaDB: A new geospatial DataFrame library written in Rust

**原文链接**: [https://sedona.apache.org/latest/blog/2025/09/24/introducing-sedonadb-a-single-node-analytical-database-engine-with-geospatial-as-a-first-class-citizen/](https://sedona.apache.org/latest/blog/2025/09/24/introducing-sedonadb-a-single-node-analytical-database-engine-with-geospatial-as-a-first-class-citizen/)

SedonaDB：一款为地理空间数据而生的单节点开源分析数据库引擎。它是 Apache Sedona 项目的一部分，用 Rust 编写，轻量、快速且原生支持空间数据，包括空间类型、连接、CRS 和函数。它具有查询优化、索引和数据剪枝等特性，以实现高性能。SedonaDB 提供 Pythonic、SQL、R 和 Rust 接口，可运行于本地文件或数据湖。

SedonaDB 集成了 Apache Arrow 和 DataFusion，无需扩展即可原生处理空间工作负载。一个快速入门示例展示了城市和国家表之间的空间连接。

本文介绍了 Apache Sedona SpatialBench，一个用于地理空间 SQL 分析查询性能的基准测试，比较了 SedonaDB 与 GeoPandas 和 DuckDB Spatial。SedonaDB 在各种查询类型中表现出均衡的性能，而 DuckDB 在某些领域表现出色，但在复杂连接方面表现不佳，GeoPandas 则需要手动优化。

SedonaDB 还提供 CRS 管理，在读取/写入文件和 DataFrames 时自动跟踪 CRS，从而提高 pipeline 安全性。一个真实的示例演示了 KNN 连接，用于识别网约车数据中接载点附近的建筑物。

SedonaDB 使用 Rust 构建，以实现高性能和内存安全，它与 SedonaSpark 互补，后者更适合大规模分布式环境。建议将 SedonaDB 用于较小的数据集和本地计算。

---

## 6. 那个特勤局SIM卡农场的故事是假的。

**原文标题**: That Secret Service SIM farm story is bogus

**原文链接**: [https://cybersect.substack.com/p/that-secret-service-sim-farm-story](https://cybersect.substack.com/p/that-secret-service-sim-farm-story)

好的，以下是文章“特勤局SIM卡农场故事是假的”的摘要，基于我能够访问并阅读它的假设：

文章驳斥了社交媒体上流传的关于特勤局运营“SIM卡农场”以拦截通信和犯罪的说法。 《今日网络安全》的作者帕特里克·格雷认为，这个故事极不可能，缺乏可信的证据。

格雷强调了SIM卡农场说法不太可能的几个原因。 首先，在不被发现的情况下运营这样一个系统所需的后勤和技术专业知识将是巨大的，涉及到与移动运营商的大量协调，并躲避他们可能已经部署的检测机制。 其次，暴露的风险将超过任何潜在的好处。 如果被抓到从事此类活动，对特勤局来说后果将是灾难性的。

第三，作者指出了法律和伦理影响。 在没有适当搜查令的情况下广泛拦截通信将是对隐私法的严重侵犯，并会严重损害公众信任。

最后，格雷认为，谣言的来源可能源于错误信息或对执法机构通常如何运作的误解。 他暗示执法部门通常使用其他方法来访问加密通信，这些方法不太容易被发现且风险较小。 他敦促读者批判性地看待耸人听闻的说法，并依赖于来自信誉良好的来源的可验证信息。 简而言之，文章得出结论，SIM卡农场的故事是一个毫无根据的阴谋论。

---

## 7. 边缘 Python：快速、沙箱化且由 WebAssembly 驱动

**原文标题**: Python on the Edge: Fast, sandboxed, and powered by WebAssembly

**原文链接**: [https://wasmer.io/posts/python-on-the-edge-powered-by-webassembly](https://wasmer.io/posts/python-on-the-edge-powered-by-webassembly)

Wasmer Edge (Beta) 全面支持 Python：边缘端快速、沙箱化 Python 执行

---

## 8. 在土壤中发现新细菌和两种潜在抗生素

**原文标题**: New bacteria, and two potential antibiotics, discovered in soil

**原文链接**: [https://www.rockefeller.edu/news/38239-hundreds-of-new-bacteria-and-two-potential-antibiotics-found-in-soil/](https://www.rockefeller.edu/news/38239-hundreds-of-new-bacteria-and-two-potential-antibiotics-found-in-soil/)

本文宣布发现一种新的土壤细菌，并鉴定出两种源自该细菌的潜在抗生素。虽然标题清楚地表明了这一关键发现，但其余内容与此无关，可能来自另一篇讨论神经退行性疾病的文章。因此，摘要侧重于标题中的信息。

重点是在土壤样本中发现了一种新的细菌。这一发现意义重大，因为同时发现了两种源自这种新细菌的潜在抗生素。这可能对解决日益严重的抗生素耐药性问题具有重要意义。本文未提供关于细菌的具体类型、潜在抗生素的作用机制或土壤样本来源的详细信息。未来有必要进行进一步研究，以鉴定该细菌的特征并充分评估已鉴定抗生素的临床应用潜力。

---

## 9. 美国航空公司力推取消旅客权利，削弱关键保障

**原文标题**: US Airlines Push to Strip Away Travelers' Rights by Rolling Back Key Protections

**原文链接**: [https://www.travelandtourworld.com/news/article/american-joins-delta-southwest-united-and-other-us-airlines-push-to-strip-away-travelers-rights-and-add-more-fees-by-rolling-back-key-protections-in-new-deregulation-move/](https://www.travelandtourworld.com/news/article/american-joins-delta-southwest-united-and-other-us-airlines-push-to-strip-away-travelers-rights-and-add-more-fees-by-rolling-back-key-protections-in-new-deregulation-move/)

美国主要航空公司，包括美国航空、达美航空、西南航空和联合航空，正在推动放松监管，以降低成本和促进竞争为幌子，削弱消费者保护。具体来说，航空公司旨在撤销关于自动退款、费用透明度、家庭座位保证以及残疾乘客无障碍保护等方面的规定。

代表航空公司的美国航空协会（A4A）认为，放松监管将导致价格降低和对服务的投资增加，并指出自1978年以来放松监管的成功。他们批评目前美国交通部（DOT）关于辅助费用透明度、退款规则以及航班延误/取消的规定，声称这些规定过于繁琐。

批评人士认为，放松监管将导致更多隐藏费用，家庭因座位费用而感到压力，航空公司逃避取消航班的责任，以及对残疾乘客的保护减弱。他们认为这可能导致竞争减少，并允许主要航空公司剥削乘客。

文章强调了过度监管和消费者保护之间的争论，表明需要取得平衡，以确保公平待遇和透明度。文章敦促乘客保持知情，联系代表，并了解自己的权利，以倡导公平的航空旅行惯例。总体信息是，放松监管对乘客权利构成重大威胁，可能导致更昂贵和更不透明的旅行体验。

---

## 10. 用Anki、ChatGPT和YouTube学习波斯语

**原文标题**: Learning Persian with Anki, ChatGPT and YouTube

**原文链接**: [https://cjauvin.github.io/posts/learning-persian/](https://cjauvin.github.io/posts/learning-persian/)

本文详细介绍了作者使用 Anki、ChatGPT 和 YouTube 结合学习波斯语的方法。Anki，一个间隔重复系统，是核心工具，作者主要从 Majid 的“Persian Learning”YouTube 频道创建自定义闪卡。

作者从视频内容创建三种 Anki 卡片：用于阅读练习的基础卡片（仅波斯语脚本），以及反向基础卡片（波斯语/罗马化短语和英语/法语翻译）。 ChatGPT 作为即时复习工具集成到 Anki 复习过程中。当遇到难以理解的卡片时，作者会截取屏幕截图并向 ChatGPT 寻求解释，以帮助更深入地理解。

YouTube 通过“双字幕”和“Tweaks for YouTube”Chrome 扩展程序加以利用。“双字幕”提供波斯语和英语字幕，用于词汇和语法学习，并为 Anki 卡片创建提供素材。“Tweaks for YouTube”允许精确控制播放（1 秒倒退/快进）。

文中描述了一种特定的语音理解技巧：以 75% 的速度收听带有双字幕的 YouTube 视频（波斯语字幕大于英语字幕）。 该过程包括快速阅读英语字幕，然后听波斯语音频，同时专注于理解的“感觉”，即使遇到不熟悉的单词。 阅读波斯语脚本可以加强理解。 重复和朗读可以巩固学习，目标是实现实时理解和强烈的流畅感。 该方法强调感觉和联想，而不是死记硬背，从而实现有效的语言习得。

---

## 11. 智能手机相机走向高光谱

**原文标题**: Smartphone Cameras Go Hyperspectral

**原文链接**: [https://spectrum.ieee.org/hyperspectral-imaging](https://spectrum.ieee.org/hyperspectral-imaging)

普渡大学杨金带领的研究团队开发出一种算法，可将标准智能手机摄像头转变为先进的高光谱传感器。这项突破利用计算机视觉、色彩科学和光学光谱学，从普通智能手机摄像头拍摄的常规照片中提取详细的光谱信息。这项创新有望扩展日常智能手机摄像头的功能，使其能够执行通常需要专门且昂贵的高光谱成像设备才能完成的任务。文章强调，这项技术可以通过消费设备使复杂的光谱分析更易于获取和使用。作者查尔斯·Q·崔是IEEE Spectrum的特约编辑。文章发表于2025年9月23日，预计阅读时间为2分钟。

---

## 12. 如何在专家云集的场合发挥领导力

**原文标题**: How to Lead in a Room Full of Experts

**原文链接**: [https://idiallo.com/blog/how-to-lead-in-a-room-full-of-experts](https://idiallo.com/blog/how-to-lead-in-a-room-full-of-experts)

本文重新定义了专家云集环境下的技术领导力，认为其重点不在于成为最聪明的人，而在于有效的沟通和协调。首席开发人员的主要角色是“翻译者”，弥合不同团队及其专业语言（开发人员、产品、管理层）之间的差距。

作者强调了社交技能与技术专长同等重要，突出了建设性地管理辩论、理解未明说的需求以及确保每个人都理解所要解决的问题的必要性。优秀的领导者会清晰地阐述问题，使团队能够集体找到解决方案。

“我不知道”被视为一种优势，可以营造一种智力上的谦逊氛围，并让专家能够贡献他们最好的工作。领导者的工作是构建决策框架、权衡利弊并提供背景信息，而不是拥有所有的答案。

本文强调清晰的沟通和提供决策背后的“原因”，从而培养信任和协作。专家团队中有效的领导力侧重于提供清晰的问题定义、决策的背景信息、不同视角之间的转换、免受不必要复杂性的保护，以及个人发挥优势的空间。最终，领导者帮助团队理解“他们共同演奏的乐章”。

---

## 13. 氛围不对时如何成为领导者

**原文标题**: How to Be a Leader When the Vibes Are Off

**原文链接**: [https://chaoticgood.management/how-to-be-a-leader-when-the-vibes-are-off/](https://chaoticgood.management/how-to-be-a-leader-when-the-vibes-are-off/)

本文探讨了科技行业氛围的转变，即从乐观转向焦虑，其原因是人工智能、重返办公室的要求以及裁员等因素。作者认为，虽然领导者无法控制这些宏观力量，但他们可以控制如何支持他们的团队。

要点包括：

*   **问题：** 源于人工智能恐惧、僵化的重返办公室政策、大规模裁员以及转向以效率为中心的领导方式而日益加剧的焦虑和不信任感。
*   **领导者的困境：** 在需要“戴着公司的帽子”并支持领导层决策与需要承认团队的担忧并保持他们的信任之间取得平衡。
*   **解决方案：** 私下与你的团队承认负面情况，并验证他们的情绪，但不要承诺不切实际的解决方案。 相反，尽可能地倡导更好的政策，并寻找小的变通方法来改善团队士气并展示信任。 这可以包括酌情执行某些公司政策。
*   **稳定的重要性：** 在动荡时期，员工会向他们的直接领导寻求稳定，这可以通过平静的诚实、信誉和培养忠诚度来实现。
*   **长远观点：** 作者认为目前的情况是暂时的，行业最终会找到新的常态。 关心团队的领导者可以通过保持冷静和表现出温和的反抗精神，在保持团队的参与度和生产力方面发挥重要作用。

---

## 14. 欧盟年龄验证应用暂不计划支持桌面端

**原文标题**: EU age verification app not planning desktop support

**原文链接**: [https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/issues/22](https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/issues/22)

该文件对欧盟数字身份钱包应用程序的可用性表示担忧，特别是其明显侧重于智能手机用户，可能导致老年或没有智能手机的人无法进行年龄验证。作者强调了没有智能手机或注重隐私的用户在浏览网页时面临的困难，因为年龄验证将被反复要求，使私密浏览变得繁琐。他们建议使用浏览器扩展程序作为潜在解决方案，但对其可信度以及对整体可用性的影响表示怀疑。最后，作者质疑实施该应用程序的成本，并引用了过去欧盟科技项目成本高昂且限制开发者使用特定技术的经验，这可能会阻碍小型初创企业的发展。核心论点是，目前的应用程序设计为某些用户群体创造了可访问性和可用性障碍，并引发了隐私问题。

---

## 15. 谁资助非主流研究？

**原文标题**: Who Funds Misfit Research?

**原文链接**: [https://blog.spec.tech/p/who-funds-misfit-research](https://blog.spec.tech/p/who-funds-misfit-research)

谁资助“另类研究”？

本文旨在为理解不符合传统学术、初创企业或公司模式的研究的资助情况提供实用指南。它将资助者分为非稀释性（无所有权赠款）和稀释性（期望回报的投资）两种模式。

**非稀释性资助者：**

*   **基金会：** 投放慈善资金，但由于官僚流程，通常偏向传统研究。 存在例外情况。
*   **慈善聚合平台：** 为特定项目筹集资金，比基金会更灵活。 示例包括文艺复兴慈善组织、创始人承诺和Xprize。
*   **政府组织：** 主要资助传统学术研究，但一些机构，如DARPA和SBIR，通过奖金竞赛和赠款支持另类研究。
*   **众筹平台：** 适用于具有公众吸引力的小规模项目，但很少筹集到大量资金。

**稀释性资助者：**

*   **天使投资人：** 投资于早期初创企业的个人，有时优先考虑影响力而非财务回报。
*   **风险投资家（VC）：** 主要在“泡沫”时期或拥有非传统基金结构时进行投资。
*   **公司研究：** 呈下降趋势，但一些大型公司支持探索性研究，尽管主要通过大学作为招聘渠道。
*   **公司风险投资：** 公司风险投资部门除了纯粹的回报外，还根据公司对初创企业的“战略利益”进行投资。
*   **影响力投资者：** 接受较低的财务回报以实现较高的社会或环境影响力，提供“耐心资本”。
*   **项目相关投资（PRIs）：** 基金会和捐助者建议基金进行与其使命相关的稀释性投资。

**同时进行两种模式的实体：**

*   **去中心化自治组织（DAOs）：** 通过区块链代币汇集资金的社区，采用赠款和稀释性融资。
*   **高净值人士（HNWIs）：** 拥有最大的灵活性，但通常难以联系。
*   **家族办公室：** 管理富裕家庭的资金，平衡财富创造、风险缓解和慈善事业。

文章警告说，稀释性资金可能会将研究导向短期商业目标，并且它并不总是适合可能永远不适合风险投资的另类研究项目。

---

## 16. 宜家风格解释快速排序

**原文标题**: Quicksort explained IKEA-style

**原文链接**: [https://idea-instructions.com/quick-sort/](https://idea-instructions.com/quick-sort/)

本文题为“宜家风格解释快速排序”，介绍了快速排序算法。文章强调快速排序是一种高效的排序方法，它采用“分而治之”的策略。文章还强调了在算法中随机选择分割元素的重要性，以减少最坏情况下运行时间性能不佳的可能性。

本文经历了几次修订：

*   **v1.0:** 初始版本
*   **v1.1:** 标题从“KWICK SÖRT”更改为“KVICK SÖRT”，大概是为了更好地唤起瑞典/宜家的联想。
*   **v1.2:** IDEA logo已更新。

本文最初发表于2018年3月16日。

---

## 17. λ演算 – 斯坦福哲学百科全书

**原文标题**: The Lambda Calculus – Stanford Encyclopedia of Philosophy

**原文链接**: [https://plato.stanford.edu/entries/lambda-calculus/](https://plato.stanford.edu/entries/lambda-calculus/)

Lambda演算是一种函数及其应用的表示法，建立在抽象和应用之上。它的语法简单却富有表现力，将函数表示为计算规则，与将函数视为有序对集合的外延式观点形成对比。

关键概念包括：

*   **抽象：** 使用lambda运算符（`λ`）绑定变量并创建函数。
*   **应用：** 将函数应用于参数，表示为`Ma`。
*   **Beta归约：** 演算的核心原则，用参数替换lambda项中的变量：`(λx[M])N`归约为`M[x := N]`。
*   **多参数函数：** 通过一次一个地顺序应用函数来表示（柯里化）。
*   **非外延性：** 与集合论不同，lambda演算将函数视为规则，而不仅仅是输入-输出对的集合。函数在行为上可以等效，但在定义上可以不同。

本文还涉及外延、内涵和超内涵函数概念之间的区别，强调lambda演算通常表现出超内涵性，即使是内涵上等价的函数也可能是不同的。

本文概述了lambda演算的基本语法，以归纳方式定义术语，并强调了括号的重要性。后续章节（概括为“顺带提及”）涵盖了归约策略、lambda理论、语义、组合逻辑和类型系统等扩展，以及在逻辑、计算和关系表示中的应用。

---

## 18. HubSpot 如何扩展人工智能的应用

**原文标题**: How HubSpot Scaled AI Adoption

**原文链接**: [https://product.hubspot.com/blog/context-is-key-how-hubspot-scaled-ai-adoption](https://product.hubspot.com/blog/context-is-key-how-hubspot-scaled-ai-adoption)

HubSpot人工智能编码工具普及之路：从谨慎试用到近乎全面应用，历时两年，彻底改变了其软件开发模式。这涉及战略投资、组织承诺和学习意愿。

创始人Dharmesh和Brian的高层支持是成功的关键，他们加速了试点项目并协调了各个团队。大规模的、由不同团队参与的试点项目，以及专门的支持工作（培训、沟通渠道）都至关重要。他们认真地衡量结果，尽管最初存在怀疑，但结果显示生产力有适度但显著的提高。

为了推动采用，提高人工智能工具的影响力（通过针对HubSpot的技术栈进行定制），在组织内部倡导人工智能，调整采购流程以加快工具评估，并构建数据驱动的评估能力，HubSpot成立了一个专门的“开发者体验人工智能”团队。

最初，制定了谨慎的使用规则。然而，数据分析显示人工智能的应用与生产事故之间没有负相关关系，这促使HubSpot取消了限制，主动向所有工程师提供人工智能工具的访问权限，从而大大提高了采用率。

要覆盖大部分后期使用者，需要同伴验证（视频演示）、人工智能成功使用的量化证明、提供多种编码助手选项，以及提供经过优化的配置和精心策划的体验。最后，HubSpot将人工智能流畅使用作为工程岗位的基本要求，巩固了他们对人工智能应用的承诺，并为未来的员工队伍做好准备。这种广泛的应用为更高级的人工智能应用铺平了道路，包括人工智能助手和快速UI原型设计。

---

## 19. 更佳 Curl Saul：一个注重用户体验和简洁性的轻量级 API 测试 CLI

**原文标题**: Better Curl Saul: a lightweight API testing CLI focused on UX and simplicity

**原文链接**: [https://github.com/DeprecatedLuar/better-curl-saul](https://github.com/DeprecatedLuar/better-curl-saul)

“更优 Curl Saul”：一款轻量级、用户友好的 API 测试 CLI，旨在简化复杂的 HTTP 请求并改善开发者体验。它以更具组织性和直观性的方式解决了传统 `curl` 命令的笨重问题。

主要功能包括：

*   **基于工作区的组织：** API 在专用文件夹中进行管理，以实现更好的组织。
*   **智能变量：** 支持持久性 (`{@}`) 和提示性 (`{?}`) 变量，用于动态请求构建。
*   **响应过滤：** 允许用户仅显示 API 响应中的相关字段。
*   **Git 友好的配置：** 使用 TOML 文件进行版本控制的 API 配置。
*   **Unix 可组合性：** 与 shell 脚本和管道无缝集成。

该 CLI 提供命令来设置、获取、编辑和删除请求体、标头、查询参数、URL、方法和超时的配置，以及查看请求历史记录。通过适用于 Linux、macOS 和（希望是）Windows 的一键式脚本简化了安装，以及手动下载或从源代码构建等替代方法。

路线图包括诸如内联终端字段编辑、更全面的响应过滤、批量操作和用户配置系统等增强功能。它强调用户反馈以进行错误报告和功能建议。该工具目前处于 beta 阶段，核心功能已正常运行，但文档仍在编写中。

---

## 20. 就让我选择文本

**原文标题**: Just Let Me Select Text

**原文链接**: [https://aartaka.me/select-text.html](https://aartaka.me/select-text.html)

阿尔乔姆·博洛戈夫的《就让我选择文本》一文， lamenting 了禁用用户界面中，特别是像 Bumble 这样的应用中的文本选择功能的令人沮丧的做法。作者讲述了一次经历，他想翻译一位德国女性的个人资料，但因为文本无法选择而作罢。这迫使他放弃了尝试，突显了这种设计选择造成的毫无必要的障碍。

博洛戈夫认为，使文本无法选择本质上将其转换为像图像这样的媒体格式，失去了与文本相关的关键功能：可复制性、可翻译性、可访问性和轻量级特性。他强调了文本在传达意义和促进理解方面的重要性，认为禁用选择会阻碍这些核心功能。

他指出，禁用选择会使文本更难处理和理解，迫使用户求助于截图和 OCR 等繁琐的变通方法。他将这种做法等同于对理解力、可访问性和文本本身含义的“犯罪”。作者最后发出了强烈的行动号召，敦促开发者停止禁用文本选择，并赋予用户按照预期的方式与文本交互的能力。

---

## 21. S3在低速硬盘基础上可扩展到每秒拍字节级。

**原文标题**: S3 scales to petabytes a second on top of slow HDDs

**原文链接**: [https://bigdata.2minutestreaming.com/p/how-aws-s3-scales-with-tens-of-millions-of-hard-drives](https://bigdata.2minutestreaming.com/p/how-aws-s3-scales-with-tens-of-millions-of-hard-drives)

本文深入探讨了 AWS S3 的工程奇迹，解释了它如何利用普通的 HDD 实现 PB 级吞吐量和 1.5 亿 QPS，尽管 HDD 在 IOPS 和延迟方面存在固有的局限性。S3 利用大规模并行性（通过纠删码等技术实现）来克服单个 HDD 缓慢的随机 I/O 性能。纠删码将数据分解成碎片，使 S3 能够从这些碎片的一个子集中重建数据，从而提高容错能力并实现从多个驱动器的并行读取。

本文重点介绍了 S3 在前端服务器、硬盘驱动器和 PUT/GET 操作中的并行性，从而防止瓶颈并最大限度地提高吞吐量。建议用户使用多个连接，并将数据拆分成碎片并分布在大量存储后端。此外，还推荐使用分段上传和字节范围 GET。

为了避免热点，S3 在数据放置中采用随机化和持续的重新平衡。“两个随机选择的力量”策略进一步优化了负载均衡。通过系统庞大的规模实现的工作负载去相关性确保了更可预测的聚合负载，使 S3 能够高效运行。本文强调，S3 通过结合这些技术，为各种数据基础设施需求（特别是数据湖上的分析和机器学习）提供可扩展、持久且经济高效的存储解决方案。

---

## 22. 数据共享平台模型上下文协议（MCP）服务器

**原文标题**: The Data Commons Model Context Protocol (MCP) Server

**原文链接**: [https://developers.googleblog.com/en/datacommonsmcp/](https://developers.googleblog.com/en/datacommonsmcp/)

谷歌开发者博客发布 Data Commons 模型上下文协议 (MCP) 服务器，助力 AI 开发和数据科学家访问海量公共数据集。MCP 服务器为 AI 智能体提供标准化途径原生消费 Data Commons 数据，加速创建数据丰富的应用，并减少大型语言模型 (LLM) 的幻觉。

重点强调的关键优势包括使智能体能够处理数据驱动的查询，从探索性分析到生成报告，提供可信的、溯源的信息。它专为无缝集成到智能体开发工作流程而设计，可在 Google Cloud Platform 的 Agent Development Kit (ADK) 和 Gemini CLI 等客户端中使用，也可与其他智能体平台一起使用。

文章介绍了一个真实用例：与 ONE Campaign 合作开发的 ONE 数据智能体。该智能体帮助用户快速搜索和可视化数百万个卫生融资数据点，从而改善与全球卫生相关的倡导、报告和政策制定。它展示了 MCP 服务器如何让用户轻松查找和编译以前分散在众多不同来源的数据，从而节省大量时间和精力。

该博文鼓励开发者通过提供的资源开始使用 MCP 服务器，包括 ADK 示例智能体的 Colab 笔记本、使用 Gemini CLI 的服务器说明以及访问 GitHub 存储库。

---

## 23. 人权团体敦促英国首相斯塔默放弃强制性数字身份识别计划。

**原文标题**: Rights groups urge UK PM Starmer to abandon plans for mandatory digital ID

**原文链接**: [https://bigbrotherwatch.org.uk/press-releases/rights-groups-urge-starmer-to-abandon-plans-for-mandatory-digital-id/](https://bigbrotherwatch.org.uk/press-releases/rights-groups-urge-starmer-to-abandon-plans-for-mandatory-digital-id/)

包括老大哥观察组织、第十九条、自由协会和开放权利组织在内的多个权利团体，已敦促英国首相基尔·斯塔默放弃强制性数字身份识别计划。这些组织在一封联名信中警告说，拟议的计划将从根本上改变公民与国家之间的关系，侵犯公民自由，并且很可能无法阻止非法移民，尽管其声明的目的如此。他们表示担心，强制性数字身份识别系统未来可能成为访问各种公共和私人服务的必要条件，超出其最初对移民管制的关注。

老大哥观察组织还发布了一份关于数字身份识别危险的报告，并在工党和保守党大会上举办活动，以提高人们对这个问题的认识。这些团体认为，日常生活中频繁的身份检查，可能是强制性数字身份识别的一个可能后果，将代表隐私和自主权的显著侵蚀。他们鼓励公众更多地了解潜在的影响并表达他们的担忧。

---

## 24. 我的Ed(1)工具箱

**原文标题**: My Ed(1) Toolbox

**原文链接**: [https://aartaka.me/my-ed.html](https://aartaka.me/my-ed.html)

自诩为ed(1)爱好者的Artyom Bologov详细介绍了他的个人“ed(1)工具箱”，其中包含他在标准编辑器之外使用的各种实现和脚本。

他从**GNU ed**和受限版本**red**开始，发现后者不太有用。为了解决可移植性问题，他使用**OpenBSD ed (oed)**，因为GNU ed不符合POSIX标准。他尝试过**wed (ed wImproved)**，一个更友好的、支持脚本的ed(1)，但他更喜欢自己的解决方案。

对于交互式使用，Bologov创建了**aed**，一个更具交互性的ed(1)，它通过Readline和shell脚本增强，提供了更友好的体验。对于脚本编写，他开发了**xed**，一个脚本，它能够实现类似于sed(1)的单行命令，用于字符串操作等任务。他认为sed(1)和ex(1)（vi的前身）是不必要的。

他还提到了他自己用Brainfuck、BASIC和Modal编写的ed(1)实现，主要作为练习，但也承认它们不如标准编辑器的质量。他鼓励大家使用和欣赏ed(1)，特别是他创建的aed(1)。最后，他提供了一个ed-museum的链接，并通过电子邮件邀请反馈。

---

## 25. 美国国土安全部多年来一直在采集美国人的DNA。

**原文标题**: The DHS has been harvesting DNA from Americans for years

**原文链接**: [https://www.wired.com/story/dhs-has-been-collecting-us-citizens-dna-for-years/](https://www.wired.com/story/dhs-has-been-collecting-us-citizens-dna-for-years/)

根据乔治城大学法律隐私与技术中心分析的数据，美国国土安全部（DHS）一直在收集美国公民（包括未成年人）的DNA，并将其输入联邦调查局的CODIS犯罪数据库。2020年至2024年间，此举影响了近2000名美国公民（包括估计95名未成年人），从未经国会授权，且包括从未被指控犯罪的个人。

批评者认为，这构成了对基因监控的非法扩张，因为DHS探员在收集DNA方面拥有广泛的自由裁量权，即使是对那些因民事理由而被拘留的人。规模庞大：自2020年以来，DHS已向CODIS贡献了约260万个样本，这得益于2020年司法部的一项规则变更，该变更取消了阻止从移民拘留者那里收集DNA的豁免。这已使联邦调查局的系统不堪重负，造成了未处理试剂盒的积压。

根据2025年的一项行政命令，DHS机构被指示使用“任何可用的技术”（包括基因检测）来验证家庭关系，从而进一步扩大了该计划。专家和立法者对缺乏监督、潜在的滥用以及DNA样本的无限期保留提出了警告。担忧包括对少数族裔的 disproportionate impact 以及个人被永久视为嫌疑人的风险。已提起诉讼，迫使DHS公布有关该计划的记录，突显了缺乏透明度以及将CODIS重新用于广泛监控档案的潜在可能性。

---

## 26. 为.NET 10 GC做准备

**原文标题**: Preparing for the .NET 10 GC

**原文链接**: [https://maoni0.medium.com/preparing-for-the-net-10-gc-88718b261ef2](https://maoni0.medium.com/preparing-for-the-net-10-gc-88718b261ef2)

本文旨在使 .NET 开发者为 .NET 10 中动态应用目标大小调整 (DATAS) 的默认启用做好准备。DATAS 是一项重要的垃圾回收 (GC) 功能，它可以根据应用程序的大小调整内存使用量。与典型的 GC 改进不同，DATAS 可能会因其对性能配置文件的影响而需要用户注意。

DATAS 旨在优化内存使用，可能会大幅减少内存占用，尤其是在突发工作负载和小型服务器 GC 应用程序中。它的目标是在非高峰时段释放内存有利的场景，例如 Kubernetes 等编排环境。

作者解释说，传统的服务器 GC 不会根据应用程序大小进行调整，而是侧重于生存率。相反，DATAS 会根据实时数据大小 (LDS) 进行调整，从而在不同的核心数下实现更一致的堆大小。

DATAS 的核心在于两个组成部分：通过 DATAS 计算的预算 (BCD)，用于设置 gen0 预算的上限；以及目标吞吐量成本百分比 (TCP)，旨在保持合理的性能（默认为 2%）。通过根据工作负载强度调整 gen0 预算，DATAS 可以在较轻的时期显著减少内存使用量。

本文强调，DATAS 并非一刀切的解决方案。虽然它有利于内存受限的环境和适应性资源分配，但它可能会降低优先考虑最高性能的应用程序的吞吐量。建议开发人员评估其应用程序的性能指标，并在其权衡不理想时考虑调整或禁用 DATAS。

---

## 27. 探索 GrapheneOS 安全分配器：强化版 Malloc

**原文标题**: Exploring GrapheneOS secure allocator: Hardened Malloc

**原文链接**: [https://www.synacktiv.com/en/publications/exploring-grapheneos-secure-allocator-hardened-malloc](https://www.synacktiv.com/en/publications/exploring-grapheneos-secure-allocator-hardened-malloc)

本文深入探讨了强化型malloc，GrapheneOS定制的内存分配器，旨在增强安全性，抵御内存损坏漏洞。GrapheneOS通过扩展的48位地址空间、增加的ASLR熵，以及通过`exec`安全地生成应用程序，创建随机化的地址空间，防止可预测的库位置，从而增强安全性。它还在支持的设备上利用内存标签扩展（MTE），对分配进行标记，以检测越界访问和释放后使用漏洞。

强化型malloc将元数据隔离在`ro`（在.bss中）和`allocator_state`结构中，与用户数据分离。它使用 arena（虽然目前配置为单个 arena）来进行线程特定的内存管理。用户数据存储在 slab（用于小额分配）中，位于一个大的预留区域内，或者存储在动态分配的大区域中（用于较大分配）。

小额分配被划分为49个大小类别（bins），每个类别都由一个`size_class`结构管理。每个类别都有一个专门的内存区域，该区域被分割成 slab，slab又被进一步分割成 slot，这些 slot 代表返回给用户的内存块。这种严格的结构和MTE的使用，共同为GrapheneOS 创造了一个更安全的内存管理环境。

---

## 28. 亨廷顿舞蹈症首次得到治疗

**原文标题**: Huntington's disease treated for first time

**原文链接**: [https://www.bbc.com/news/articles/cevz13xkxpro](https://www.bbc.com/news/articles/cevz13xkxpro)

一种突破性基因疗法首次在治疗亨廷顿舞蹈症方面取得显著成功。该疗法涉及精细的脑部手术以进行基因治疗，使患者的疾病进展减缓了75%，有望将“高质量生活”延长数十年。

亨廷顿舞蹈症是一种破坏性的遗传性疾病，会破坏脑细胞，导致类似于痴呆症、帕金森病和运动神经元疾病的症状。该疗法旨在降低有毒的亨廷顿蛋白的水平，该蛋白是由于基因突变而产生的。该疗法使用一种改良病毒来传递一段DNA序列，该序列可以禁用构建突变蛋白的指令。

这项涉及29名患者的试验表明，该疗法不仅基于认知和运动功能减缓了疾病进展，还显示出保护脑细胞的迹象。一名因病退休的患者得以重返工作岗位。

虽然该疗法可能价格昂贵且需要复杂的手术，但它为受亨廷顿舞蹈症影响的个人和家庭提供了前所未有的希望。UniQure计划于2026年初在美国申请许可。研究人员现在正计划针对携带亨廷顿基因但尚未出现症状的个体进行预防性试验。科学家们认为这种疗法是“一个开端”，并希望它能为未来更易获得的疗法铺平道路。

---

## 29. 我的游戏服务器在西班牙每当有足球比赛时就会被屏蔽。

**原文标题**: My game's server is blocked in Spain whenever there's a football match on

**原文链接**: [https://old.reddit.com/r/gamedev/comments/1np6kyn/my_games_server_is_blocked_in_spain_whenever/](https://old.reddit.com/r/gamedev/comments/1np6kyn/my_games_server_is_blocked_in_spain_whenever/)

无法访问文章链接。

---

## 30. 找到旧金山停车执法人员

**原文标题**: Find SF parking cops

**原文链接**: [https://walzr.com/sf-parking/](https://walzr.com/sf-parking/)

无法访问文章链接。

---

## 31. 我花了三晚解 Listen Labs Berghain 挑战 (并获得了第16名)

**原文标题**: I Spent Three Nights Solving Listen Labs Berghain Challenge (and Got #16)

**原文链接**: [https://kuber.studio/blog/Projects/How-I-Spent-Three-Nights-Solving-Listen-Labs-Berghain-Challenge](https://kuber.studio/blog/Projects/How-I-Spent-Three-Nights-Solving-Listen-Labs-Berghain-Challenge)

2025年，聆听实验室发起了“博格黑恩挑战”，这是一个伪装成夜店保安模拟器的隐秘编码谜题，引发了一场令人沉迷的优化竞赛。挑战内容是接受或拒绝具有二元属性的虚拟“俱乐部访客”，以满足特定配额，同时尽量减少拒绝次数。大奖是前往真正的博格黑恩夜店的旅行以及一次工作面试机会。

作者详细描述了自己沉迷于该挑战的过程，最初因过载的API而感到沮丧。他们构建了一个本地模拟器来试验各种算法，从最初的幼稚的“贪婪接受”方法，到使用高斯-科普拉模型和线性规划的复杂数学模型。最终，他们发现针对每种场景进行调整的实用阈值算法产生了最佳结果。

作者获得了第16名的成绩，并有机会了解顶级选手的见解。分析公开的GitHub仓库揭示了各种方法，包括动态规划和微分方程表示。冠军的方法，即DualThresholdSolver，使用了对偶变量和特定场景的参数调整。

作者学到了关于算法设计的宝贵经验，工程实用主义胜过纯理论的重要性，以及运气在挑战结果中的作用。这次经历将他们从算法新手转变为一名熟练的问题解决者。

---

## 32. Qwen3-VL

**原文标题**: Qwen3-VL

**原文链接**: [https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list)

提供的信息极其有限。我们只知道一篇文章的标题是“Qwen3-VL”，内容是“Qwen”。

因此，最简洁的总结是：

这篇标题为“Qwen3-VL”的文章，似乎是关于或与一个名为“Qwen”的系统、模型或概念有关。由于内容仅仅是“Qwen”，没有提供关于Qwen或Qwen3-VL的具体性质、能力或目的的更多信息。 这篇文章可能需要更多内容才有意义。

---

## 33. 博德之门3 Steam Deck 原生版

**原文标题**: Baldur's Gate 3 Steam Deck – Native Version

**原文链接**: [https://larian.com/support/faqs/steam-deck-native-version_121](https://larian.com/support/faqs/steam-deck-native-version_121)

本文详细介绍了博德之门3的Steam Deck原生版本，该版本随热修复补丁#34一同发布，相比Proton版本，由于降低了CPU和内存占用，性能有所提升。玩家可以通过检查游戏的兼容性设置，确保选择了Linux Runtime来验证是否安装了原生版本。

文章解释说，虽然拉瑞安工作室没有正式支持Linux，但这个原生版本是专门为Steam Deck优化的。如果玩家遇到问题，可以在兼容性设置中强制使用Proton 8或更高版本来恢复到Proton版本。

一个关键的重点是存档位置。在原生版本之前，存档存储在`compatdata`文件夹中（Proton版本）。现在，存档存储在SteamOS的原生文件夹中。如果Steam云存档未启用，文章详细说明了如何手动将存档从旧位置转移到新位置。文章还指出，除非手动删除，否则旧存档仍会占用存储空间。

关于Mod，连接到其拉瑞安帐户和mod.io的用户将自动下载订阅的Mod。对于未连接的用户，文章提供了在桌面模式下将Mod文件从`compatdata`文件夹手动转移到新的原生位置的说明。

---

## 34. WiGLE：无线网络地图

**原文标题**: WiGLE: Wireless Network Mapping

**原文链接**: [https://wigle.net/index](https://wigle.net/index)

本文档介绍了WiGLE，一个协作式无线网络地图绘制项目。该平台收集用户和贡献者发现的无线网络数据（“所有网络”），并使用经纬度显示网络位置，放大后可查看单个SSID。蜂窝塔以蓝色标示。

WiGLE使用的关键指标是信号质量（QoS），基于每个网络的观测次数和观测者数量。本文档重点介绍了随时间变化的交互式统计数据，特别是WiFi网络随时间变化和WiFi加密随时间变化。

这些统计数据以图形的形式呈现，提供缩放和多日数据平滑等交互功能。这些图形还提供全屏版本，WiFi加密有更集中的两年视图。本文档鼓励用户将鼠标悬停在图形上以探索数据，选择范围进行缩放，并双击以缩小。最后，它提供了一个“关闭”按钮，可能用于关闭与图形相关的弹出窗口或模态框。

---

## 35. 神经超分辨率采样工作原理：架构、训练和推理

**原文标题**: How Neural Super Sampling Works: Architecture, Training, and Inference

**原文链接**: [https://semiengineering.com/how-neural-super-sampling-works-architecture-training-and-inference/](https://semiengineering.com/how-neural-super-sampling-works-architecture-training-and-inference/)

本文深入探讨神经超采样（NSS），这是Arm开发的一种用于移动游戏的人工智能驱动的放大解决方案。NSS旨在克服传统时间超采样（TSS）方法的局限性，后者依赖于手工调整的启发式方法，在与放大结合使用时，尤其是在鬼影、伪影和不稳定性方面表现不佳。

NSS通过使用循环学习方法和时空损失函数来优化空间保真度和时间一致性，在低分辨率帧序列和高分辨率真值图像对上进行训练。NSS网络采用UNet骨干网络，并输出每像素参数（滤波器内核、时间系数、隐藏状态），从而驱动后处理步骤。这种参数预测方法对量化友好且带宽高效。

NSS的主要优势包括动态内核滤波器、使用先前帧的隐藏状态进行时间反馈，以及能够针对特定游戏内容进行微调。预处理阶段准备输入（颜色、运动矢量、深度、亮度导数），而后处理阶段通过运动矢量扩张、历史重投影、滤波、稀疏放大、校正和样本累积来构建输出颜色。

验证指标包括PSNR、SSIM和FLIP，视觉比较证实了在快速运动和复杂几何场景中提高了稳定性和细节保留。早期模拟表明，NSS可以在4毫秒的预算内于移动硬件上实时运行，在效率方面可能优于Arm ASR。Arm神经图形开发套件为开发者提供了用于实验的示例代码和网络结构。

---

## 36. 具有测试时扩散的深度研究者

**原文标题**: Deep researcher with test-time diffusion

**原文链接**: [https://research.google/blog/deep-researcher-with-test-time-diffusion/](https://research.google/blog/deep-researcher-with-test-time-diffusion/)

本文介绍了谷歌云开发的新型AI智能体Test-Time Diffusion Deep Researcher (TTD-DR)，它能显著提升研究报告撰写和复杂推理任务的性能。TTD-DR将研究建模为扩散过程，从初步草稿开始，通过检索到的信息迭代改进，模拟人类的研究过程。

TTD-DR的关键方面：

*   **基于扩散的方法：** 将初始草稿视为“噪声”版本，通过检索增强的去噪过程逐步改进。
*   **组件式自我进化：** 使用自我进化算法优化研究工作流程的每个阶段（研究计划生成、迭代搜索和最终报告生成），该算法利用LLM作为评判者进行反馈和修订。
*   **基于检索的报告级去噪：** 使用检索到的信息不断改进报告草稿，并将去噪后的报告反馈到搜索查询生成过程中。

该智能体的性能在长篇报告撰写（DeepConsult）和多跳推理（Humanity's Last Exam 和 GAIA）的基准数据集上进行了评估，结果表明其达到了最先进的水平。TTD-DR在胜率和正确性评分方面始终优于OpenAI Deep Research。消融研究证实了每个组件（backbone DR、自我进化和基于检索的扩散）在实现这些结果方面的有效性。 与其他DR智能体相比，TTD-DR在延迟和质量方面也表现出更高的效率。

TTD-DR的产品版本已在Google Agentspace上提供，并通过Google Cloud Agent Development Kit实现。

---

## 37. 身份类型

**原文标题**: Identity Types

**原文链接**: [https://bartoszmilewski.com/2025/09/22/identity-types/](https://bartoszmilewski.com/2025/09/22/identity-types/)

Bartosz Milewski 的博文“恒等类型”（2025年9月22日）探讨了类型理论中等价的概念，并将其与传统数学进行了对比。在传统数学中，等价是一种二元关系，但在类型理论中，等价是一种*类型*，代表着等价的证明。这种“恒等类型”，记作，取决于被比较的值（类型 A 的 x 和 y）。如果 x 和 y 不相等，则该类型是空的；如果相等，则它由等价的“证明”或“见证”填充。

构造器生成一个等价的平凡证明：自反性 (refl x :: IdA x x)。该文章强调，恒等类型可以具有非平凡的居住者（路径），从而导致高阶等价（证明的等价，等等）。

核心概念是“恒等消去规则”，或路径归纳。要定义一个从路径到某个类型的函数（该类型可以取决于路径及其端点），只需指定该函数如何作用于平凡路径 (refl x)。这唯一地决定了该函数对任何路径的作用。

该博文随后介绍了恒等类型的范畴模型，将该类型表示为纤维化。引入规则对应于选择对角元素的箭头，而消除规则涉及定义一个依赖函数并构造一个映射（截面）。路径归纳用一个交换图表示，突出了它与同伦理论中提升属性的相似性。作者提到，对恒等类型的建模将在下一篇博文中讨论。

---

## 38. 马尔可夫链是最早的语言模型。

**原文标题**: Markov chains are the original language models

**原文链接**: [https://elijahpotter.dev/articles/markov_chains_are_the_original_language_models](https://elijahpotter.dev/articles/markov_chains_are_the_original_language_models)

伊利亚·波特的文章《马尔科夫链是最初的语言模型》探讨了作者从最初对大型语言模型的惊叹到最终的厌倦，并渴望回归基础概念的旅程。文章认为，马尔科夫链，一种用于序列事件的概率模型，与复杂的人工智能相比，提供了一种更简单、更透明的文本补全方法。

作者概述了人工智能炒作的四个阶段：惊叹、沮丧、困惑和厌倦。达到厌倦阶段后，作者深入研究了马尔科夫链，并以爱丽丝在杂货店和天文馆之间移动的例子来解释它们。核心概念涉及在矩阵中表示转移概率，并使用矩阵乘法来预测未来状态。

文章然后演示了如何将马尔科夫链应用于文本补全。它详细介绍了从样本文本构建字典和转移矩阵的过程。转移矩阵捕获了一个单词跟随另一个单词的概率。通过使用用户的最后一个单词作为起点，该模型预测自动完成建议中最有可能的下一个单词。

文章承认了马尔科夫链的局限性，特别是它们倾向于收敛到稳态，这使得简单的文本生成变得重复。作者提出了一种使用随机矩阵来引入不可预测性的解决方案。总之，作者回归基础，在使用更简单的系统时感到更加投入和满足。

---

## 39. 字节跳动提议Linux采用“Parker”：多个内核同时运行

**原文标题**: ByteDance Proposes "Parker" for Linux: Multiple Kernels Running Simultaneously

**原文链接**: [https://www.phoronix.com/news/Linux-Parker-Proposal](https://www.phoronix.com/news/Linux-Parker-Proposal)

字节跳动发布“Parker”，一种在单台机器上同时运行多个Linux内核的新方案，独立于KVM或其他虚拟化技术。此前不久，Multikernel Technologies也提出了类似的“多内核”架构建议。

Parker的工作原理是为每个内核实例划分CPU核心、内存和设备。“引导内核”管理硬件分配和分区，而辅助的“应用内核”在其分配的资源上独立运行。尽管概念相似，但该设计与Multikernel的RFC不同。

字节跳动设想Parker主要用于核心数量高的系统，在这些系统中可扩展性是一个问题。该设计的“无共享”方法（内核实例之间不通信）旨在提高可扩展性。每个内核都需要专用的PCIe设备，如NVMe驱动器或网卡来进行I/O。另一种用例包括运行具有不同性能调优和配置的内核实例，这些实例针对特定工作负载进行了优化。

文章最后指出，人们对多内核方法的兴趣日益浓厚，以应对现代高核心数量系统的挑战，并表示期待这些想法的未来发展和可能集成到上游Linux内核中。

---

## 40. Show HN: Mosaic – 一款用于编写更简洁后端代码的 Kotlin 框架

**原文标题**: Show HN: Mosaic – A Kotlin framework for cleaner back end code

**原文链接**: [https://github.com/Nick-Abbott/Mosaic](https://github.com/Nick-Abbott/Mosaic)

Mosaic 是一款 Kotlin 框架，旨在通过将重点从数据库查询转移到响应组合来简化后端开发。它通过“瓷片 (tiles)”实现这一目标，这些瓷片是可组合的代码单元，可自动处理缓存、并发和依赖项解析。

Mosaic 的主要特性包括类型安全的组合、消除冗余数据获取、自动并行执行、通过轻松模拟单个瓷片实现的自然可测试性，以及“响应优先”的设计。

该框架通过“画布 (Canvas)”支持依赖注入，从而允许分离应用程序级别和特定于请求的依赖项。 这有助于实现更简洁的代码和资源管理。 类型化的键提高了编译时安全性。

Mosaic 提供“MultiTile”以实现高效的批处理操作，从而将批处理策略从消费者代码中抽象出来。它还通过使开发人员能够单独模拟复杂组合中的单个瓷片来简化测试。

该框架与 Spring Boot、Ktor 和 Micronaut 无缝集成，并为每个框架提供代码示例。 它非常适合高性能 API、复杂后端、微服务、GraphQL 解析器、实时应用程序以及偏向于以响应角度思考的系统。

本质上，Mosaic 旨在通过促进可组合性、高效的资源管理、可测试性和以响应为中心的方法来简化后端开发。

---

## 41. 卑诗省救援人员用直升机载手机信号塔找到失踪男子。

**原文标题**: B.C. rescuers use helicopter-mounted cell tower to find missing man

**原文链接**: [https://www.cbc.ca/news/canada/british-columbia/north-shore-rescue-lifeseeker-portable-cell-tower-1.7639677](https://www.cbc.ca/news/canada/british-columbia/north-shore-rescue-lifeseeker-portable-cell-tower-1.7639677)

卑诗省北岸救援队利用新型“生命搜寻者”成功搜救一名在纳奈莫附近失踪的男子。该技术是一种安装在直升机上的便携式信号塔，使他们能够在信号原本缺失的偏远地区检测到该男子的手机信号。北岸救援队认为他们是卑诗省，乃至可能是加拿大，首个以志愿搜救能力使用该技术的组织。

该男子骑电动自行车摔倒后失踪。虽然最初通过他的手机有一些联系，但他的确切位置仍然未知。“生命搜寻者”设备需要手机的IMEI序列号并且手机处于开机状态，事实证明这对于确定他的位置至关重要。北岸救援队搜索经理艾伦·麦克莫迪强调，如果没有“生命搜寻者”的帮助，找到该男子将非常困难。

这项技术耗资约25万加元，代表了对社区资助资源的一项重大投资。“生命搜寻者”背后的公司Centum声称，该技术已为四大洲的220次成功救援做出了贡献。麦克莫迪敦促偏远地区使用者告知他人他们的路线，携带指南针和急救箱等必需品，并节省手机电量，携带外置电池组作为备用。

---

## 42. 让AI在复杂代码库中工作

**原文标题**: Getting AI to work in complex codebases

**原文链接**: [https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)

GitHub仓库“humanlayer/advanced-context-engineering-for-coding-agents”旨在解决在复杂代码库中有效使用AI编码代理的难题。它专注于**高级上下文工程**，即在正确的时间为AI代理提供正确的信息，以解决特定的编码问题的技术。

其核心思想是，简单地将整个代码库转储到AI上下文中等简单方法通常无效，并可能导致性能不佳。相反，该仓库提倡一种更具战略性和细致性的方法。

该仓库可能探索的关键方面（尽管此处无法获得全部内容）包括：

*   **上下文选择：** 用于识别并仅向AI提供相关的代码片段、文档或测试用例的技术。这可能涉及语义搜索、依赖性分析或使用专门的检索方法。
*   **上下文增强：** 使用额外信息来丰富上下文的方法，例如澄清指令、提供相关示例或向代码添加注释。
*   **上下文管理：** 用于管理上下文的大小和复杂性以避免使AI代理不堪重负的策略。这可能涉及将大型任务分解为具有重点上下文的较小子任务。
*   **评估和迭代：** 评估AI的性能并迭代上下文工程策略以提高结果的重要性。

该仓库可能提供示例、工具或框架来实现这些高级上下文工程技术，从而帮助开发人员在实际项目中更有效地利用AI编码代理。其主要目标是提高在具有挑战性的复杂软件环境中AI辅助编码的准确性、速度和整体实用性。

---

## 43. 2025年热门编程语言

**原文标题**: Top Programming Languages 2025

**原文链接**: [https://spectrum.ieee.org/top-programming-languages-2025](https://spectrum.ieee.org/top-programming-languages-2025)

计算分析的文章《2025年顶级编程语言》探讨了在人工智能不断发展的背景下，编程语言的未来。该文章由IEEE Spectrum的Stephen Cass撰写，很可能分析并预测哪些编程语言将在2025年保持其相关性和主导地位。

虽然从这段摘录中尚未明确指出具体语言，但提出的核心问题是，人工智能的崛起是否会导致某些语言过时，或者从根本上改变软件开发的格局。该文章很可能调查了人工智能工具和自动化如何影响对各种语言的需求，可能更有利于那些适合人工智能开发、数据科学或与人工智能工作流程互补的通用脚本的语言。

鉴于作者与IEEE Spectrum的隶属关系，该文章很可能提供数据驱动和专家视角的分析，并考虑行业趋势、语言普及程度、生态系统支持和新兴技术等因素。重点可能在于不同语言在日益受到人工智能影响的未来中的寿命和适应性。

---

## 44. 通往更安全互联网的更简单途径：我们的CSAM扫描工具更新

**原文标题**: A simpler path to a safer Internet: an update to our CSAM scanning tool

**原文链接**: [https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/](https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/)

Cloudflare更新CSAM扫描工具，简化网站运营商保护平台免受儿童性虐待材料侵害的流程。主要改进在于取消了网站运营商创建和提供自身NCMEC凭证的要求，此举先前阻碍了工具的采用。自从二月份实施这项变更以来，该工具的月度采用率增长了1600%。

该工具的工作原理是将上传内容的模糊哈希（感知指纹）与NCMEC等组织维护的已知CSAM哈希列表进行比较。模糊哈希允许该工具识别即使经过更改的CSAM图像。

更新后的流程很简单：用户启用该工具，Cloudflare扫描缓存内容以寻找匹配项，如果找到匹配项，Cloudflare会阻止该URL并通知网站运营商。虽然Cloudflare会阻止相关内容，但网站运营商仍有责任向NCMEC或其区域对等机构提交报告。

Cloudflare强调其致力于让所有人（而不仅仅是大型公司）都能使用互联网安全工具。该公司鼓励网站运营商启用该工具，并提供开发者文档和一个社区论坛来提供支持。文章还包含有关Cloudflare其他在线安全服务的信息以及指向职业机会的链接。

---

## 45. 新研究表明动植物会发出一种可见光，并在死亡时消失。

**原文标题**: New study shows plants and animals emit a visible light that expires at death

**原文链接**: [https://pubs.acs.org/doi/10.1021/acs.jpclett.4c03546](https://pubs.acs.org/doi/10.1021/acs.jpclett.4c03546)

无法访问文章链接。

---

## 46. 迪士尼将提高Disney+和Hulu的价格。

**原文标题**: Disney is raising the price of Disney+ and Hulu

**原文链接**: [https://techcrunch.com/2025/09/23/disney-is-raising-the-price-of-disney-hulu-subscriptions-next-month/](https://techcrunch.com/2025/09/23/disney-is-raising-the-price-of-disney-hulu-subscriptions-next-month/)

迪士尼将于2025年10月21日起提高Disney+和Hulu订阅价格。含广告的Disney+套餐将涨至每月11.99美元，无广告的Premium套餐将涨至每月18.99美元。Disney+ Premium年度套餐将涨至每年189.99美元。含广告的Hulu套餐将涨至每月11.99美元，但无广告版本将保持每月18.99美元不变。ESPN Select的价格也将上涨，达到每月12.99美元。

捆绑套餐价格也将上涨：含广告的Disney+和Hulu将为12.99美元，含广告的Disney+、Hulu和ESPN Select捆绑套餐将为19.99美元。完整的捆绑套餐涨价列表可以在迪士尼的支持页面上找到。

自Disney+于2019年以每月6.99美元的价格推出以来，一直在涨价，最近一次涨价发生在2024年10月。此次涨价的时间恰逢有关吉米·坎摩尔争议导致Disney+订阅取消的报道。本文由TechCrunch的消费者新闻记者Aisha Malik撰写。

---

## 47. Podman Desktop 庆祝下载量达 300 万

**原文标题**: Podman Desktop celebrates 3M downloads

**原文链接**: [https://podman-desktop.io/blog/3-million](https://podman-desktop.io/blog/3-million)

Podman Desktop 庆祝下载量突破 300 万次，这一重要里程碑归功于社区的贡献，例如问题报告、功能建议和扩展开发。文章对社区表示感谢，并在 https://3m.podman-desktop.io 公布了一个庆祝惊喜。

文章重点介绍了用户对该工具易用性、稳定性和无根容器执行的积极反馈。它还指出 Podman Desktop 已被接受为官方 CNCF 沙箱项目，这加强了其对云原生生态系统中开源、社区驱动开发的承诺。

过去一年中的主要改进包括：增强的 Kubernetes 工作流程、改进的 Docker 兼容性、生活质量改进、更简单的 Podman AI Lab 以及不断增长的社区构建的扩展生态系统。文章强调了企业采用率的提高，并提供了 Amadeus 关于他们成功将数千名工程师迁移到 Podman Desktop 的证明。

文章最后邀请新老用户从 https://podman-desktop.io/downloads 下载最新版本并提供反馈。Podman Desktop 团队对社区的信任和对项目未来发展的持续投入表示感谢。

---

## 48. 从 Rust 到现实：fetch_max 的隐秘之旅

**原文标题**: From Rust to reality: The hidden journey of fetch_max

**原文链接**: [https://questdb.com/blog/rust-fetch-max-compiler-journey/](https://questdb.com/blog/rust-fetch-max-compiler-journey/)

本文详细介绍了 Rust 中 `fetch_max` 原子操作的隐藏历程，从其看似简单的语法到最终在 x86-64 架构上实现为比较并交换 (CAS) 循环。作者受一次面试启发，调查了在 x86-64 缺乏原生原子最大值指令的情况下，Rust 如何提供 `fetch_max` 作为内置原子操作。

该调查揭示了五个抽象层：

1. **Rust 代码：** 最初简洁的 `high_score.fetch_max(new_score, Ordering::Relaxed)` 调用。
2. **宏展开：** `fetch_max` 由 `atomic_int!` 宏生成，该宏为无符号类型调用 `atomic_umax`。
3. **LLVM IR：** `atomic_umax` 是一个编译器内联函数，它转换为 LLVM 的 `atomicrmw umax`，一个高级原子读-修改-写指令。
4. **转换 (AtomicExpandPass)：** 由于 x86-64 缺乏原生 `umax` 指令，LLVM 的 `AtomicExpandPass` 将 `atomicrmw umax` 降低为 CAS 循环：读取当前值，计算无符号最大值，并使用 `cmpxchg` 原子地尝试更新，如果需要则重试。
5. **最终汇编 (x86-64)：** 生成的汇编代码揭示了 CAS 循环中使用的特定 `cmpxchg` 指令，展示了如何实现原子最大值。

本文提供了使用 `rustc` 和 `llc` 跟踪转换过程的实际步骤，展示了每个阶段的中间表示。 它强调了编译器在弥合高级原子操作和硬件特定指令之间差距的作用，说明了看似简单的 Rust 代码背后隐藏的力量和复杂性。

---

## 49. 具有相同MD5值的Webshell和一个普通文件

**原文标题**: A webshell and a normal file that have the same MD5

**原文链接**: [https://github.com/phith0n/collision-webshell](https://github.com/phith0n/collision-webshell)

本仓库演示了一个PHP webshell（`webshell.php`）和一个看似正常的PHP文件（`normal.php`）之间的MD5碰撞。这两个文件拥有相同的MD5哈希值：`b719a17ae091ed45fb874c15b2d9663f`。

`webshell.php`文件包含一个简单的PHP webshell，它执行通过GET参数`1`传递的代码：`<?=eval($_GET[1]);?>`。文件的其余部分填充了看似随机的数据以实现碰撞。

`normal.php`以一些'x'和'a'字符开头，随后是一段看似随机的数据。

作者认为此碰撞可用于绕过一些缓存的webshell检测机制，这些机制可能仅依赖于MD5哈希进行识别。包含的参考资料（中文）可能提供了有关此绕过的更多上下文或示例。两个文件的hexdump突出了如何构造看似随机的数据，从而在具有不同初始内容的情况下实现相同的MD5哈希值。

---

## 50. 生命是一种计算形式吗？

**原文标题**: Is life a form of computation?

**原文链接**: [https://thereader.mitpress.mit.edu/is-life-a-form-of-computation/](https://thereader.mitpress.mit.edu/is-life-a-form-of-computation/)

布莱斯·阿古埃拉·伊·阿卡斯的文章《生命是一种计算形式吗？》探讨了生命本质上可以被理解为一种计算过程的观点，并借鉴了艾伦·图灵和约翰·冯·诺伊曼的见解。文章强调了冯·诺伊曼的自我复制机器的概念，这与DNA通过遵循编码指令在生物繁殖中的作用相似。尽管生物计算在“大规模并行”、去中心化和随机性方面与数字计算不同，但它仍然是一种计算形式。

文章强调，随机性是生物计算的一个特征，而不是一个缺陷，这与计算机科学算法中随机性的使用相呼应。此外，文章还深入探讨了图灵关于形态发生的著作和他提出的“无序机器”，展示了不依赖于中央处理器的替代计算模型。冯·诺伊曼的细胞自动机，其中简单的计算单元在局部进行交互，进一步说明了这一点。

作者强调，计算不需要像逻辑门或顺序程序这样的传统组件，并强调了计算的“平台独立性”，这意味着任何计算机都可以模拟另一台计算机。文章最终以“神经细胞自动机”(NCA)达到高潮，这是神经网络、形态发生和细胞自动机的现代综合，能够模拟复杂的类似生命的行为，如再生，展示了计算如何在不同尺度上产生类似生命的行为，并提供了一瞥生命系统的计算基础。

---

## 51. 构建自定义 eBPF 文件系统监视器，以捕获 Root 权限错误

**原文标题**: Building a Custom eBPF Filesystem Watcher to Catch Root Ownership Goofs

**原文链接**: [https://amandeepsp.github.io/blog/fs-watcher/](https://amandeepsp.github.io/blog/fs-watcher/)

本文详述了作者构建自定义文件系统监视器以检测特定服务目录中root所有权变更的历程，这是一个在高度定制化环境中常见的问题。最初，他们探索了`fanotify`，但发现其局限性（缺乏递归监控以及需要解析`/proc`以获取UID/GID）使其不切实际。

随后，作者转向`eBPF`，利用其在内核空间运行程序以实现高效过滤的能力。虽然`eBPF`提供了诸多优势，如直接访问内核VFS函数，但也面临着诸如`vfs_*` kprobes的ABI不稳定以及需要在内核空间中使用受限资源（循环限制、堆栈大小）来实现路径过滤的挑战。

为了克服eBPF中的目录遍历限制，作者使用`dentry`结构实现了一个解决方案，通过有限的`MAX_DEPTH`向上遍历目录树。他们还使用了RCU锁以确保安全遍历。

本文还提到了LSM hooks作为更稳定的文件系统事件监控的潜在替代方案（可以访问path结构和`bpf_path_d_path`），尽管在作者当前的内核版本中不可用。

总而言之，作者强调，虽然`eBPF`功能强大，但由于其复杂性和局限性，需要仔细考虑。这次实验提供了对Linux内核内部的深入了解，并突出了相关文档的零散性。

---

## 52. 振动器帮我调试摩托车刹车灯系统。

**原文标题**: A vibrator helped me debug a motorcycle brake light system

**原文链接**: [https://bikesafe.me/blogs/news/how-a-vibrator-helped-me-debug-a-motorcycle-brake-light-system](https://bikesafe.me/blogs/news/how-a-vibrator-helped-me-debug-a-motorcycle-brake-light-system)

此博文详细介绍了BrakeBright的持续开发和改进，这是一种旨在提升摩托车刹车灯功能的设备。作者讨论了在防止误报方面面临的挑战，即由于路况或发动机振动导致刹车灯意外闪烁。

最初，平均传感器数据和实施低通滤波器被证明是不够的。然后，作者转而使用中位数，通过忽略异常值，从而更准确地表示骑行行为。然而，高速公路测试进一步揭示了与传感器轮询速率与发动机转速同步相关的问题，导致误触发。

为了解决这个问题，作者在采样间隔中引入了抖动，增加了随机性以防止与发动机脉冲同步。在一个幽默的轶事中，振动器被重新用作测试台工具，以模拟高频发动机振动，从而加快了调试过程。

最终的解决方案涉及一个消抖延时，系统会等待确认持续制动后才激活灯光。消抖周期会根据最近的误报发生情况动态调整，在短暂的灯光激活后增加，在更平稳的骑行条件下减少。

作者强调了实际测试和持续改进的重要性，并邀请骑手提供反馈。文章最后提供了一个特别折扣码，供对购买BrakeBright感兴趣的读者使用。

---

## 53. 构建更好的 TypeScript 在线编辑器

**原文标题**: Building a better online editor for TypeScript

**原文链接**: [https://blog.val.town/vtlsp](https://blog.val.town/vtlsp)

Wolf Mermelstein 详述了 Val Town 对其在线 TypeScript 编辑器的改造。之前的编辑器依赖于在 Web Worker 中运行 TypeScript Language Service Host，导致 Deno 的独特功能出现问题，并且庞大的 NPM 依赖树使浏览器不堪重负。

为了解决这个问题，Val Town 转而远程在云容器中运行官方的 Deno Language Server，利用 Deno 项目的 Rust 代码来处理 Deno 特有的怪异之处，并将依赖管理卸载到强大的服务器上。这种架构利用 WebSockets 和 LSP 协议在基于浏览器的客户端和服务器之间进行通信，其灵感来自现有的实现和 VS Code LSP 客户端库。

该实现包括一个用于修改消息和 URI 转换的语言服务器代理库，从而允许自定义和依赖管理。选择 Cloudflare 容器进行部署，利用其持久对象生态系统来管理容器生命周期，并将用户路由到隔离的、持久的语言服务器实例。

最终的架构采用基于 WebSocket 的通信系统取代 Web Worker，利用 Deno Language Server 和隔离的服务器进行模块解析和依赖管理。所有组件，包括客户端、服务器和代理，都以 `vtlsp` 的形式开源。这个新系统在 Val Town 中提供了更快、更准确、更可靠的 TypeScript 编辑体验，并计划进行进一步的改进和 Val Town 特有的功能开发。

---

## 54. 锌 (YC W14) 正在招聘高级后端工程师 (纽约市)

**原文标题**: Zinc (YC W14) Is Hiring a Senior Back End Engineer (NYC)

**原文链接**: [https://app.dover.com/apply/Zinc/4d32fdb9-c3e6-4f84-a4a2-12c80018fe8f/?rs=76643084](https://app.dover.com/apply/Zinc/4d32fdb9-c3e6-4f84-a4a2-12c80018fe8f/?rs=76643084)

纽约市 Zinc (YC W14) 高级后端工程师招聘 (Dover平台发布，需启用 Javascript 才能查看详情，无法获取职位描述、要求、福利或公司信息)

---

## 55. Google AI Pro和Ultra套餐获得Gemini CLI和代码助手，并提升了上限。

**原文标题**: Google AI Pro and Ultra Plans Get Gemini CLI and Code Assist with Higher Limits

**原文链接**: [https://blog.google/technology/developers/gemini-cli-code-assist-higher-limits/](https://blog.google/technology/developers/gemini-cli-code-assist-higher-limits/)

谷歌增强其AI Pro和Ultra订阅计划，为订阅者提供Gemini CLI和Gemini Code Assist的访问权限，并提高模型请求限制。此次升级使开发者能够花费更多时间利用Gemini 2.5 Pro和Flash进行构建和编码。Gemini Code Assist于5月在VS Code和IntelliJ中推出，而将Gemini引入终端的开源Gemini CLI于6月首次亮相。现在可以使用VSCode中的IDE模式、Zed集成以及CLI的新GitHub操作等新功能。潜在订阅者可以注册Google AI Pro或Ultra计划。使用限制列于www.developers.google.com。这些更改将在24小时内推出。

---

## 56. Libghostty 即将到来

**原文标题**: Libghostty is coming

**原文链接**: [https://mitchellh.com/writing/libghostty-is-coming](https://mitchellh.com/writing/libghostty-is-coming)

米切尔·桥本宣布即将发布 libghostty，一个可嵌入的库，允许任何应用程序集成一个功能完备的终端模拟器。初始组件 libghostty-vt 是一个零依赖库，可以解析终端序列并维护从 Ghostty 核心提取的终端状态（光标位置、样式等）。它甚至不需要 libc，因此具有高度可移植性。

libghostty 的动机是提供一个稳定、可重用且一致的终端模拟解决方案，从而消除各种应用程序（如终端模拟器、多路复用器、编辑器，甚至显示日志的网站）中临时且通常存在错误的实现。桥本强调，终端模拟比看起来复杂得多，共享库将使许多开发人员受益。

libghostty-vt 继承了 Ghostty 的强大功能，例如 SIMD 优化的解析、Unicode 支持、优化的内存使用以及与 Kitty Graphics 等协议的兼容性。它最初将面向 macOS 和 Linux (x86_64 和 aarch64)，并计划扩展到 Windows、嵌入式设备和通过 WASM 的 Web。

更长远的计划包括更多的 libghostty 组件，包括输入处理、GPU 渲染、GTK 小部件和 Swift 框架。libghostty-vt 的 Zig 模块已可供测试，C API 正在开发中。桥本鼓励开发人员进行实验并提供反馈以塑造 API。他的目标是在六个月内发布一个带标签的版本，具体取决于准备情况。

---

## 57. 5G并非总是比4G快：一项在8个世界城市的研究

**原文标题**: 5G doesn't always deliver faster connections than 4G: a study in 8 world cities

**原文链接**: [https://techxplore.com/news/2025-09-5g-deployed-doesnt-faster-4g.html](https://techxplore.com/news/2025-09-5g-deployed-doesnt-faster-4g.html)

这篇2025年9月发表于GIST的文章，基于东北大学牵头、多家国际机构参与的研究，调查了八个主要城市中5G网络相对于4G的实际性能表现。该研究发表在《计算机通信》杂志上，揭示了尽管5G已广泛部署，但在延迟等方面，它并未始终如一地提供优于4G的性能。

研究人员收集了一年多的数据，发现不同地理位置和运营商的5G上行链路性能存在显著差异。该研究表明，“5G”标签本身不如运营商在频谱频段、部署密度和基础设施方面的决策重要。 对于用户而言，切换到5G并不一定能保证更低的延迟或更高的响应速度。

作者告诫不要过早地投资于6G，认为专注于解决5G的运营问题，如覆盖盲区和回程链路，至关重要。他们强调需要大规模、前瞻性的测量来了解用户的真实体验，然后再推进到下一代。该研究强调，虽然5G部署稳定，但其性能优势仍然不均衡，尤其是在延迟方面，导致了一种有条件的成熟：已部署，但尚未始终如一地优于4G。政策和未来的投资应基于透明、可重复的结果，而不是乐观的承诺。

---

## 58. 人工智能时代最大的讽刺：人类受雇清理人工智能的垃圾

**原文标题**: Greatest irony of the AI age: Humans hired to clean AI slop

**原文链接**: [https://www.sify.com/ai-analytics/greatest-irony-of-the-ai-age-humans-being-increasingly-hired-to-clean-ai-slop/](https://www.sify.com/ai-analytics/greatest-irony-of-the-ai-age-humans-being-increasingly-hired-to-clean-ai-slop/)

文章《人工智能时代的最大讽刺：人类受雇清理人工智能垃圾》和《从仿制药到天才药物：人工智能革命重塑印度制药业 09/24/2025》揭示了一个随着人工智能应用日益广泛而出现的矛盾局面。虽然人工智能正在自动化许多任务并有望提高效率，但它也产生了对人工的新需求。这种劳动包括清理人工智能生成的内容和数据集中存在的错误、偏见和不一致之处，这些通常被称为“人工智能垃圾”。

第一篇文章表明，旨在取代人类劳动者的这项技术，具有讽刺意味地创造了对他们的需求，特别是为了确保人工智能输出的质量和可靠性。这些人类“清洁工”的任务包括事实核查、纠正错误、消除有害偏见以及改进人工智能产生信息的整体质量。这突出了目前人工智能的局限性以及对人类监督和判断的持续需求。

第二篇文章表明了人工智能对印度制药行业的影响。截至 2025 年 9 月 24 日，印度制药业似乎已经因这场革命而被重塑。

---

## 59. 永远邀请安娜

**原文标题**: Always Invite Anna

**原文链接**: [https://sharif.io/anna-alexei](https://sharif.io/anna-alexei)

沙里夫·沙米姆的《永远邀请安娜》反思了包容性的重要性，特别是对于那些可能会拒绝邀请的人。作者回忆起他的大学第一个学期，他的朋友们经常外出参加聚会。安娜，一个来自阿拉巴马州的害羞好学的女孩，总是拒绝他们的邀请。最终，除了阿列克谢，这群人不再邀请她，阿列克谢坚持不懈地邀请安娜，尽管她一再拒绝。

作者对阿列克谢的坚持感到好奇，便问他为什么一直邀请安娜。阿列克谢解释说，他想让安娜感到被包容，即使她从未加入他们。多年后，作者与安娜重新联系，安娜透露说，她在第一个学期一直受思乡之苦。她对这个朋友群体表示感谢，因为她觉得她有了一个远离家乡的家庭，并且因为他们总是花时间邀请她，即使她总是拒绝，她也感到被包容。

这篇文章强调了发出邀请的简单而深刻的影响，即使是对那些可能拒绝的人，也能为那些最需要它的人培养一种归属感和社区感。

---

## 60. FDD揭露一起疑似三年前开始的中国情报活动

**原文标题**: FDD Uncovers Likely Chinese Intelligence Operation That Began 3 Years Ago

**原文链接**: [https://www.fdd.org/analysis/2025/09/11/fdd-uncovers-likely-chinese-intelligence-operation-that-began-more-than-3-years-ago/](https://www.fdd.org/analysis/2025/09/11/fdd-uncovers-likely-chinese-intelligence-operation-that-began-more-than-3-years-ago/)

无法访问文章链接。

---

## 61. 编程语言入门

**原文标题**: Introduction to Programming Languages

**原文链接**: [https://hjaem.info/itpl](https://hjaem.info/itpl)

《编程语言导论》是由Jaemin Hong和Sukyoung Ryu编写的教材，专为编程语言入门课程设计，特别是KAIST编程语言课程。不过，它免费提供给任何有兴趣学习或教授基本编程语言概念的人。作者鼓励使用本书，并要求教师注明作者和网页。他们也欢迎通过电子邮件（jaemin.hong@kaist.ac.kr）提供反馈和更正。

本书涵盖了语法、语义、类型系统以及解释器/类型检查器实现等基本主题。内容基于KAIST课程，并承认PLT材料的影响。作者感谢以前的学生和助教的贡献，包括练习的创建和编辑。

该页面还提供变更日志，列出不同版本中的更新和修订，包括错别字修复、添加练习和答案以及新增关于垃圾回收和类型推断的章节。最新版本于2023年8月10日发布。

---

## 62. 如何为孩子们画工程设备

**原文标题**: How to draw construction equipment for kids

**原文链接**: [https://alyssarosenberg.substack.com/p/how-to-draw-construction-equipment](https://alyssarosenberg.substack.com/p/how-to-draw-construction-equipment)

无法访问文章链接。

---

## 63. 苹果 A19 SoC 芯片照片

**原文标题**: Apple A19 SoC die shot

**原文链接**: [https://chipwise.tech/our-portfolio/apple-a19-dieshot/](https://chipwise.tech/our-portfolio/apple-a19-dieshot/)

本文展示了从iPhone 17中提取的苹果A19 SoC的首批高分辨率芯片照片，预计iPhone 17将于2025年9月发布。A19采用台积电改进的3nm N3P工艺制造，是对A18系列中使用的N3E的升级，有望提高晶体管密度，提升能效，并带来适度的性能提升。

A19保留了混合CPU核心设计（性能核心和效率核心），并配备了升级的GPU，Pro型号受益于更多的核心数量。图像信号处理器、显示引擎和神经网络引擎等配套模块也进行了增强。这些升级旨在提高设备上的AI能力、成像性能和电源管理。

芯片照片可视化了A19的物理布局，包括逻辑块、缓存库和互连，展示了苹果在工艺技术和架构设计改进方面的持续努力。提供了图像来源Chipwise的联系信息，以及相关芯片照片项目的链接。

---

## 64. Autodesk 上调 APS 价格

**原文标题**: Autodesk Increases APS Pricing

**原文链接**: [https://aps.autodesk.com/blog/aps-business-model-evolution](https://aps.autodesk.com/blog/aps-business-model-evolution)

Autodesk宣布了Autodesk平台服务 (APS，前身为Forge) 的定价模式变更，称之为商业模式的演进。核心信息是APS定价将会上涨，影响依赖该平台API构建应用程序的开发者。

此次变更的主要驱动因素是基础设施成本增加、APS平台的持续创新以及对长期可持续性的承诺。Autodesk强调，价格上涨对于维持APS服务的质量和可靠性，以及持续投资于新功能和新特性是必要的。

虽然价格上涨的具体细节并不总是以单一的百分比增长来明确说明，但沟通中强调不同服务受到的影响将有所不同。建议开发者查看APS网站上更新的定价信息，并评估对各自应用程序和项目的影响。

Autodesk还提供了关于优化APS使用情况的信息，以潜在地减轻价格变动的影响。建议包括利用可用的免费层级、优化API调用以及高效管理数据存储。

该公告鼓励开发者与APS团队沟通，并利用可用的资源，包括文档、论坛和支持渠道，以了解这些变更并就其APS使用情况做出明智的决策。

---

## 65. Zutty: 零成本 Unicode 电传打字机，低端系统的高端终端

**原文标题**: Zutty: Zero-cost Unicode Teletype, high-end terminal for low-end systems

**原文链接**: [https://git.hq.sig7.se/zutty.git](https://git.hq.sig7.se/zutty.git)

无法访问该文章链接。

---

## 66. Fortran 比 Python 更适合教授数值线性代数的基础知识吗？

**原文标题**: Is Fortran better than Python for teaching basics of numerical linear algebra?

**原文链接**: [https://loiseaujc.github.io/posts/blog-title/fortran_vs_python.html](https://loiseaujc.github.io/posts/blog-title/fortran_vs_python.html)

The article discusses the merits of using Fortran over Python for teaching the basics of numerical linear algebra to engineering students with limited programming experience. While acknowledging the power and popularity of the Python's NumPy/SciPy ecosystem, the author argues that Python's permissiveness and syntax can be detrimental to learning fundamental concepts.

The author contends that Python's reliance on external libraries like NumPy, 0-based indexing, and indentation-based syntax introduce unnecessary cognitive load and potential for errors, distracting students from the core principles of numerical methods. Examples include the need to import and alias NumPy, common indentation errors, and off-by-one errors due to the 0-based indexing conflicting with mathematical notation.

Conversely, the author posits that Fortran's strong typing, explicit loop delineation, and 1-based indexing provide a more structured and intuitive learning environment. The explicit variable declarations in Fortran force students to think more carefully about input, output, types, and dimensions, reducing potential surprises and clarifying the code-user contract. Fortran's do/enddo constructs remove indentation-related errors, and 1-based indexing aligns directly with mathematical conventions, minimizing off-by-one mistakes.

The article illustrates these points with a Jacobi method example, showcasing how Python implementations can be prone to errors due to syntax and implicit type handling, whereas Fortran's verbosity and explicitness can promote a deeper understanding and error prevention. The author clarifies that this is not about performance comparisons but about improving the initial learning experience for students encountering numerical linear algebra for the first time.


---

## 67. Mesh: I tried Htmx, then ditched it

**原文标题**: Mesh: I tried Htmx, then ditched it

**原文链接**: [https://ajmoon.com/posts/mesh-i-tried-htmx-then-ditched-it](https://ajmoon.com/posts/mesh-i-tried-htmx-then-ditched-it)

生成摘要时出错

---

## 68. Processing Strings 109x Faster Than Nvidia on H100

**原文标题**: Processing Strings 109x Faster Than Nvidia on H100

**原文链接**: [https://ashvardanian.com/posts/stringwars-on-gpus/](https://ashvardanian.com/posts/stringwars-on-gpus/)

生成摘要时出错

---

## 69. Context Engineering for AI Agents: Lessons

**原文标题**: Context Engineering for AI Agents: Lessons

**原文链接**: [https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

生成摘要时出错

---

## 70. From MCP to shell: MCP auth flaws enable RCE in Claude Code, Gemini CLI and more

**原文标题**: From MCP to shell: MCP auth flaws enable RCE in Claude Code, Gemini CLI and more

**原文链接**: [https://verialabs.com/blog/from-mcp-to-shell/](https://verialabs.com/blog/from-mcp-to-shell/)

生成摘要时出错

---

## 71. Go has added Valgrind support

**原文标题**: Go has added Valgrind support

**原文链接**: [https://go-review.googlesource.com/c/go/+/674077](https://go-review.googlesource.com/c/go/+/674077)

生成摘要时出错

---

## 72. Sampling and structured outputs in LLMs

**原文标题**: Sampling and structured outputs in LLMs

**原文链接**: [https://parthsareen.com/blog.html#sampling.md](https://parthsareen.com/blog.html#sampling.md)

生成摘要时出错

---

## 73. 破纪录的DDoS攻击峰值达22 Tbps和10 Bpps

**原文标题**: Record-Breaking DDoS Attack Peaks at 22 Tbps and 10 Bpps

**原文链接**: [https://www.securityweek.com/record-breaking-ddos-attack-peaks-at-22-tbps-and-10-bpps/](https://www.securityweek.com/record-breaking-ddos-attack-peaks-at-22-tbps-and-10-bpps/)

生成摘要时出错

---

## 74. macOS becomes iOS: Safari video controls

**原文标题**: macOS becomes iOS: Safari video controls

**原文链接**: [https://underpassapp.com/news/2025/9/8.html](https://underpassapp.com/news/2025/9/8.html)

生成摘要时出错

---

## 75. YAML document from hell (2023)

**原文标题**: YAML document from hell (2023)

**原文链接**: [https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell)

生成摘要时出错

---

## 76. Processing Strings 109x Faster Than Nvidia on H100

**原文标题**: Processing Strings 109x Faster Than Nvidia on H100

**原文链接**: [https://ashvardanian.com/posts/stringwars-on-gpus/](https://ashvardanian.com/posts/stringwars-on-gpus/)

生成摘要时出错

---

## 77. Shopify, pulling strings at Ruby Central, forces Bundler and RubyGems takeover

**原文标题**: Shopify, pulling strings at Ruby Central, forces Bundler and RubyGems takeover

**原文链接**: [https://joel.drapper.me/p/rubygems-takeover/](https://joel.drapper.me/p/rubygems-takeover/)

生成摘要时出错

---

## 78. Altoids by the Fistful

**原文标题**: Altoids by the Fistful

**原文链接**: [https://www.scottsmitelli.com/articles/altoids-by-the-fistful/](https://www.scottsmitelli.com/articles/altoids-by-the-fistful/)

生成摘要时出错

---

## 79. 更具战略性

**原文标题**: Getting More Strategic

**原文链接**: [https://cate.blog/2025/09/23/getting-more-strategic/](https://cate.blog/2025/09/23/getting-more-strategic/)

生成摘要时出错

---

## 80. Periodic Table of Cognition

**原文标题**: Periodic Table of Cognition

**原文链接**: [https://kk.org/thetechnium/the-periodic-table-of-cognition/](https://kk.org/thetechnium/the-periodic-table-of-cognition/)

生成摘要时出错

---

## 81. Show HN: Run Qwen3-Next-80B on 8GB GPU at 1tok/2s throughput

**原文标题**: Show HN: Run Qwen3-Next-80B on 8GB GPU at 1tok/2s throughput

**原文链接**: [https://github.com/Mega4alik/ollm](https://github.com/Mega4alik/ollm)

生成摘要时出错

---

## 82. Nine things I learned in ninety years

**原文标题**: Nine things I learned in ninety years

**原文链接**: [http://edwardpackard.com/wp-content/uploads/2025/09/Nine-Things-I-Learned-in-Ninety-Years.pdf](http://edwardpackard.com/wp-content/uploads/2025/09/Nine-Things-I-Learned-in-Ninety-Years.pdf)

生成摘要时出错

---

## 83. How is einx notation universal?

**原文标题**: How is einx notation universal?

**原文链接**: [https://einx.readthedocs.io/en/stable/faq/universal.html](https://einx.readthedocs.io/en/stable/faq/universal.html)

生成摘要时出错

---

## 84. consumed.today

**原文标题**: consumed.today

**原文链接**: [https://consumed.today/](https://consumed.today/)

生成摘要时出错

---

## 85. Permeable materials in homes act as sponges for harmful chemicals: study

**原文标题**: Permeable materials in homes act as sponges for harmful chemicals: study

**原文链接**: [https://news.uci.edu/2025/09/22/indoor-surfaces-act-as-massive-sponges-for-harmful-chemicals-uc-irvine-led-study-shows/](https://news.uci.edu/2025/09/22/indoor-surfaces-act-as-massive-sponges-for-harmful-chemicals-uc-irvine-led-study-shows/)

生成摘要时出错

---

## 86. Michigan's Anticorruption of Public Morals Act Could Ban VPNs

**原文标题**: Michigan's Anticorruption of Public Morals Act Could Ban VPNs

**原文链接**: [https://reason.com/2025/09/22/michigan-anti-porn-bill-would-criminalize-asmr-written-erotica-and-even-nonsexual-depictions-of-trans-people/](https://reason.com/2025/09/22/michigan-anti-porn-bill-would-criminalize-asmr-written-erotica-and-even-nonsexual-depictions-of-trans-people/)

生成摘要时出错

---

## 87. The Hardware Knowledge That Every Programmer Should Know

**原文标题**: The Hardware Knowledge That Every Programmer Should Know

**原文链接**: [https://needoneapp.medium.com/the-hardware-knowledge-that-every-programmer-should-know-f62cf4ba8bdc](https://needoneapp.medium.com/the-hardware-knowledge-that-every-programmer-should-know-f62cf4ba8bdc)

生成摘要时出错

---

## 88. OpenDataLoader-PDF: An open source tool for structured PDF parsing

**原文标题**: OpenDataLoader-PDF: An open source tool for structured PDF parsing

**原文链接**: [https://github.com/opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)

生成摘要时出错

---

## 89. 'Send a clear message': law firm's dirty tactics on behalf of $4B crypto scam

**原文标题**: 'Send a clear message': law firm's dirty tactics on behalf of $4B crypto scam

**原文链接**: [https://www.thebureauinvestigates.com/stories/2025-09-23/send-a-clear-message-law-firms-dirty-tactics-on-behalf-of-4bn-crypto-scam](https://www.thebureauinvestigates.com/stories/2025-09-23/send-a-clear-message-law-firms-dirty-tactics-on-behalf-of-4bn-crypto-scam)

生成摘要时出错

---

## 90. YouTube says it'll bring back creators banned for Covid and election content

**原文标题**: YouTube says it'll bring back creators banned for Covid and election content

**原文链接**: [https://www.businessinsider.com/youtube-reinstate-channels-banned-over-covid-content-policies-2025-9](https://www.businessinsider.com/youtube-reinstate-channels-banned-over-covid-content-policies-2025-9)

生成摘要时出错

---

## 91. Zip Code Map of the United States

**原文标题**: Zip Code Map of the United States

**原文链接**: [https://engaging-data.com/us-zip-code-map/](https://engaging-data.com/us-zip-code-map/)

生成摘要时出错

---

## 92. Restrictions on house sharing by unrelated roommates

**原文标题**: Restrictions on house sharing by unrelated roommates

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2025/08/the-war-on-roommates-why-is-sharing-a-house-illegal.html](https://marginalrevolution.com/marginalrevolution/2025/08/the-war-on-roommates-why-is-sharing-a-house-illegal.html)

生成摘要时出错

---

## 93. x402 — An open protocol for internet-native payments

**原文标题**: x402 — An open protocol for internet-native payments

**原文链接**: [https://www.x402.org/](https://www.x402.org/)

生成摘要时出错

---

## 94. MLB approves robot umpires for 2026 as part of challenge system

**原文标题**: MLB approves robot umpires for 2026 as part of challenge system

**原文链接**: [https://www.espn.com/mlb/story/_/id/46357017/mlb-approves-robot-umpires-2026-part-challenge-system](https://www.espn.com/mlb/story/_/id/46357017/mlb-approves-robot-umpires-2026-part-challenge-system)

生成摘要时出错

---

## 95. Thundering herd problem: Preventing the stampede

**原文标题**: Thundering herd problem: Preventing the stampede

**原文链接**: [https://distributed-computing-musings.com/2025/08/thundering-herd-problem-preventing-the-stampede/](https://distributed-computing-musings.com/2025/08/thundering-herd-problem-preventing-the-stampede/)

生成摘要时出错

---

## 96. I built a dual RTX 3090 rig for local AI in 2025 (and lessons learned)

**原文标题**: I built a dual RTX 3090 rig for local AI in 2025 (and lessons learned)

**原文链接**: [https://www.llamabuilds.ai/build/portable-25l-nvlinked-dual-3090-llm-rig](https://www.llamabuilds.ai/build/portable-25l-nvlinked-dual-3090-llm-rig)

生成摘要时出错

---

## 97. NYC Telecom Raid: What's Up with Those Weird SIM Banks?

**原文标题**: NYC Telecom Raid: What's Up with Those Weird SIM Banks?

**原文链接**: [https://tedium.co/2025/09/23/secret-service-raid-sim-bank-telecom-hardware/](https://tedium.co/2025/09/23/secret-service-raid-sim-bank-telecom-hardware/)

生成摘要时出错

---

## 98. Show HN: We built our own technology radar

**原文标题**: Show HN: We built our own technology radar

**原文链接**: [https://technologieradar.tryresearchly.com](https://technologieradar.tryresearchly.com)

生成摘要时出错

---

## 99. Show HN: The Blots Programming Language

**原文标题**: Show HN: The Blots Programming Language

**原文链接**: [https://blots-lang.org/](https://blots-lang.org/)

生成摘要时出错

---

## 100. Show HN: Ggc – A Git CLI tool written in Go with interactive UI

**原文标题**: Show HN: Ggc – A Git CLI tool written in Go with interactive UI

**原文链接**: [https://github.com/bmf-san/ggc/releases/tag/v6.0.0](https://github.com/bmf-san/ggc/releases/tag/v6.0.0)

生成摘要时出错

---

