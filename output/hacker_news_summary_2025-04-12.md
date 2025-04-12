# Hacker News 热门文章摘要 (2025-04-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 开源且可自托管/私有的文件转换器

**原文标题**: Open source and self hostable/private file converter

**原文链接**: [https://vert.sh](https://vert.sh)

VERT.sh：开源且可自托管的文件转换器。其主要特点包括：

*   **注重隐私：** 所有文件处理都在用户本地设备上进行，确保隐私安全，并消除文件大小限制和广告。
*   **开源：** 该软件是开源的，允许用户检查和修改代码。
*   **广泛的格式支持（开发中）：** 该工具旨在支持各种图片、音频和视频文件格式。
*   **当前状态：** 虽然前景可观，但列出的格式及其支持状态表明，图片和音频的各项功能仍“未就绪”，且某些视频默认需要服务器端处理（附有关于如何设置本地处理的说明）。
*   **用户界面：** 提供简单的拖放或点击上传界面。
*   **板块：** 网页包含上传、转换、设置和关于等板块。

---

## 2. Tunarr: 从服务器上的媒体创建和配置直播电视频道

**原文标题**: Tunarr: Create and configure live TV channels from media on your servers

**原文链接**: [https://tunarr.com/](https://tunarr.com/)

Tunarr 是一款软件，可以从存储在 Plex、Jellyfin 或 Emby 服务器上的媒体创建直播电视频道。它允许您通过 Web UI 配置频道、节目、广告和设置。 然后，您可以通过将 Tunarr 模拟的 HDHomerun 调谐器添加到您的媒体服务器或使用生成的 M3U 文件与任何 IPTV 播放器来观看这些频道。

Tunarr 是 dizqueTV 的重新构想，旨在实现技术栈现代化、为现有用户提供迁移、稳定程序、提高性能 (使用 Node 20.11.1)、更新 Web UI 并添加新功能。 本质上，Tunarr 允许您从现有的媒体库中创建个性化的直播电视体验。

---

## 3. 巴黎告别汽车。空气污染地图显示显著变化。

**原文标题**: Paris said au revoir to cars. Air pollution maps reveal a dramatic change

**原文链接**: [https://www.washingtonpost.com/climate-solutions/2025/04/12/air-pollution-paris-health-cars/](https://www.washingtonpost.com/climate-solutions/2025/04/12/air-pollution-paris-health-cars/)

无法访问文章链接。

---

## 4. 谷歌将允许企业在自有数据中心运行 Gemini 模型

**原文标题**: Google will let companies run Gemini models in their own data centers

**原文链接**: [https://www.cnbc.com/2025/04/09/google-will-let-companies-run-gemini-models-in-their-own-data-centers.html](https://www.cnbc.com/2025/04/09/google-will-let-companies-run-gemini-models-in-their-own-data-centers.html)

谷歌云将允许企业在其自有数据中心运行 Gemini AI 模型，此项名为 Google Distributed Cloud 的服务将于第三季度开始提供。 这一举措使谷歌有别于 OpenAI 和 Anthropic 等竞争对手，后者更倾向于通过不提供数据中心部署来保持对其模型的严格控制。 Cohere 提供类似选项，但设置时间较长。

此项服务满足了包括具有高度安全需求的政府实体在内的组织的需求，这些组织希望在利用谷歌 AI 技术的同时，保持对其数据的控制。 一个与互联网断开连接的“气隙”版 Google Distributed Cloud 将满足具有绝密分类级别的客户的需求。

英伟达也将在其 Blackwell GPU 上提供 Gemini 模型，可通过谷歌或其他供应商购买。 这项举措是谷歌扩大其云市场份额的更广泛战略的一部分，谷歌云在 2023 年的市场份额为 8%，而亚马逊为 39%，微软为 23%。 谷歌云首席执行官 Thomas Kurian 强调，公司致力于多云环境和对人工智能的投资，这将推动客户增长。 Gemini 模型支持多种输入（文本、音频、视频）和 100 多种语言。 此公告是在谷歌以 320 亿美元收购云安全初创公司 Wiz 之后发布的。

---

## 5. 一个漏洞不够：通过SAP的Setuid环境两次升级权限

**原文标题**: One Bug Wasn't Enough: Escalating Twice Through SAP's Setuid Landscape

**原文链接**: [https://www.anvilsecure.com/blog/one-bug-wasnt-enough-escalating-twice-through-saps-setuid-landscape.html](https://www.anvilsecure.com/blog/one-bug-wasnt-enough-escalating-twice-through-saps-setuid-landscape.html)

Tao Sauvage 披露了他们发现 SAP 软件中两个本地权限提升漏洞 (CVE-2024-47595) 的过程，这些漏洞允许 `sapsys` 用户获得 root 权限。这是通过利用 setuid 二进制文件 `icmbnd` 和 `hostexecstart` 实现的。

初步的侦察涉及识别潜在的 setuid 二进制文件。由于存在现有漏洞，`hdbmdcdispatcher` 和 `sapuxuserchk` 被排除。重点转移到 `icmbnd` 和 `hostexecstart`。

`icmbnd` 漏洞是通过使用 `-f` 选项覆盖 `/etc/passwd` 来利用的。通过注入包含修改后的 `/etc/passwd` 条目的精心设计的 `-l` 参数，`hxeadm` 用户的组 ID 被更改为 0 (root)。这导致 `hxeadm` 用户在新的登录时获得 root 权限。

利用 `hostexecstart` 更具挑战性。接受 SAR 归档文件路径的 `-upgrade` 选项似乎很有希望。但是，SAR 归档文件是经过签名的，并且在提取之前会验证签名。作者探索了诸如使用 `-L` 选项注入参数以加载自定义库之类的选项，但由于对文件路径的限制而未成功。

由于 SAP 的专有签名过程涉及时间戳机构 (TSA) 并且仅信任 SAP 信任的 CA，因此签署 SAR 归档文件的尝试也未成功。

因此，作者开发了 SAPCARve，这是一个基于 Kaitai Struct 格式的 Python 工具，用于解析和操作 SAR 归档文件，以探索利用 `hostexecstart` 的其他方法。第二个漏洞的细节未在本摘要的上下文中提供。

---

## 6. Roo还是Cline？我们在构建一个超集。

**原文标题**: Roo or Cline? We're building a superset

**原文链接**: [https://blog.kilocode.ai/p/roo-or-cline-were-building-a-superset](https://blog.kilocode.ai/p/roo-or-cline-were-building-a-superset)

Kilo Code正在构建一个开源AI编码工具，目标是成为像Cline和Roo Code等现有工具的“超集”，融合它们的最佳特性，而不是专注于新颖的创新。这种“快速跟随”策略，受到苹果和Linux等例子的启发，利用开源社区并鼓励特性的相互采用。

Kilo Code首先通过fork Roo Code（本身就是Cline的一个fork），然后融入Cline的独特特性，使Kilo Code成为两者的超集。他们将继续合并Roo Code的代码，以保持其超集地位。目前Roo Code的独特特性包括温度控制、国际化和增强的提示功能。Cline的独特特性包括MCP市场集成和零配置启动。Kilo Code自身的增加功能包括免费的Claude 3.7 Sonnet访问、快捷键和“氛围编码”（自动接受）。

该公司计划将来自其他流行工具（包括像Cursor和Windsurf这样的专有工具）的更多特性集成到Kilo Code中。他们积极鼓励用户建议需要包含的特性，旨在成为功能最广泛的首选工具。通过开源他们的工作，他们希望加速AI编码工具的整体进步，即使这意味着其他人“偷回”他们的改进。最终，Kilo Code专注于提高开发人员的生产力并减少麻烦，强调为开源社区构建真正有用的东西。

---

## 7. Artie (YC S23) 招聘第三位工程师

**原文标题**: Artie (YC S23) Is Hiring Engineer #3

**原文链接**: [https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer](https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer)

Artie (Y Combinator S23) 招募创始产品工程师

Artie (一家 Y Combinator S23 的创业公司，致力于构建数据库和数据仓库的实时数据流解决方案) 正在旧金山招聘第三名工程师，担任创始产品工程师。他们利用变更数据捕获 (CDC) 和 Kafka 实现亚分钟级延迟的数据传输，为传统的批量 ETL 解决方案提供了一种替代方案。在推出云产品一年内，他们已实现 100 万美元的年度经常性收入 (ARR)，并获得了知名投资者的支持。

理想的候选人将拥有 4 年以上在初创公司从事 Web 开发的经验，扎实的计算机科学基础，以及以务实的方法构建用户友好且可扩展的产品。虽然精通 Go 语言者优先，但并非强制性要求。该职位涉及与技术客户直接互动以改进产品的用户体验，构建诸如列排除和模式更改警报等新功能，以及改进内部工具和构建自动化。

Artie 的技术栈包括用于前端的 TypeScript (React, Material UI) 和用于后端的 Go、PostgreSQL、Redis、Kafka 和 Elasticsearch，基础设施使用 Terraform、Kubernetes 和 Helm 在 GCP 和 AWS 上进行管理。面试流程包括与首席技术官的电话沟通、技术电话筛选以及现场面试。

Artie 团队规模为 8 人，是一家于 2023 年成立的活跃公司。

---

## 8. 妄想主题可能比我们想象的更加多样化

**原文标题**: Delusional themes may be more varied than we thought

**原文链接**: [https://www.bps.org.uk/research-digest/delusional-themes-may-be-more-varied-we-thought](https://www.bps.org.uk/research-digest/delusional-themes-may-be-more-varied-we-thought)

精神分裂症公报近期发表的一项研究挑战了对妄想主题的传统理解，发现其变异程度远超之前的假设。由伦敦大学学院的Elisavet Pappa领导的这项研究分析了涵盖全球173,920名精神病患者的155项研究。该研究确定了37种不同的妄想主题，超过了DSM-5等诊断手册中概述的有限类别。

该研究揭示了妄想体验方式中显著的文化差异，表明现有的诊断框架可能过于狭隘，且不具有普遍适用性。研究人员发现妄想中存在“社会梯度”，即个体更可能体验到与亲近家庭成员相关的妄想。这突出了人际关系在塑造妄想内容中的重要性。

该研究还发现特定妄想主题与精神疾病诊断之间存在联系，挑战了一些现有的假设。例如，通常与妄想症相关的嫉妒妄想在精神分裂症和双相情感障碍中也很常见。文化背景也起着重要作用，南亚的嫉妒妄想患病率较高，东欧的负罪感/罪孽妄想患病率较高，与“盎格鲁”国家相比，中东的性妄想和嫉妒妄想患病率较高。

该研究强调，需要采取更加细致、个体化和具有文化意识的方法来理解和治疗精神病。通过拓宽对妄想主题的理解，临床医生可以开发更有效的诊断工具，改进治疗干预措施，并改善患者的治疗效果。

---

## 9. Sphere即将上映的《绿野仙踪》体验背后的AI魔法

**原文标题**: The AI magic behind Sphere's upcoming 'The Wizard of Oz' experience

**原文链接**: [https://blog.google/products/google-cloud/sphere-wizard-of-oz/](https://blog.google/products/google-cloud/sphere-wizard-of-oz/)

本文探讨了即将于2025年8月28日在拉斯维加斯Sphere首映的“Sphere绿野仙踪”体验。该项目利用先进的生成式人工智能，包括谷歌DeepMind的Imagen和Veo，以及谷歌云的Gemini，为Sphere巨大的沉浸式环境重新构想1939年的经典电影。

目标是在尊重原片完整性的前提下，创造一种包围17600个座位的场馆的感官体验。团队没有添加任何新的对话或音乐，而是使用人工智能来增强和扩展原始素材。

关键挑战包括将原始35毫米胶片扩展到Sphere的16K LED屏幕，并填补因镜头切换造成的空白。人工智能工具被用于“超分辨率”以提高图像质量，“外绘”以扩展场景范围，以及“性能生成”以将表演融入扩展的环境中。

为了提高人工智能输出的质量，团队正在使用微调，利用大量的补充材料（包括拍摄剧本、制作插图和场景设计图）来训练人工智能模型。这使人工智能能够生成超逼真的细节，并将多萝西和托托等角色无缝集成到增强的环境中。该项目涉及谷歌DeepMind、谷歌云、Sphere Studios、Magnopus和华纳兄弟探索公司的合作。

---

## 10. 江诗丹顿打破世界纪录，推出最复杂腕表

**原文标题**: Vacheron Constantin breaks the world record for most complicated wristwatch

**原文链接**: [https://www.hodinkee.com/articles/introducing-vacheron-constantin-les-cabinotiers-solaria](https://www.hodinkee.com/articles/introducing-vacheron-constantin-les-cabinotiers-solaria)

江诗丹顿打破世界纪录，打造最复杂腕表：文章聚焦江诗丹顿在创造一款具有空前复杂功能的全新腕表上所取得的成就。文章很可能强调这款腕表是钟表史上的一项重大成就。由于文章出现在“编辑精选：2025年钟表与奇迹表展上我们最喜爱的腕表”中，因此表明这款腕表在2025年钟表与奇迹表展上首次亮相（或将首次亮相），并在其他发布的产品中脱颖而出，成为首选。核心信息是江诗丹顿突破了制表复杂性的界限，为其他制造商树立了新的标杆。

---

## 11. 你可能不需要WebSockets。

**原文标题**: You might not need WebSockets

**原文链接**: [https://hntrl.io/posts/you-dont-need-websockets/](https://hntrl.io/posts/you-dont-need-websockets/)

WebSockets并非始终最佳：HTTP流媒体的替代方案

*   **非事务性消息：** WebSockets缺乏将命令与响应（尤其是错误消息）关联的内置机制。实现此功能需要额外的复杂性，如请求ID和错误处理。
*   **Socket生命周期管理：** WebSockets需要管理连接状态（打开、关闭、错误）、重连尝试和资源清理，与HTTP的简单请求/响应模型相比增加了复杂性。
*   **增加服务器端复杂性：** 处理WebSocket握手升级、管理潜在故障以及处理部分数据帧会增加服务器端代码的复杂性，尤其是当与请求/响应语义结合使用时。

本文提出**HTTP流媒体**作为一种可行的替代方案。 通过使用HTTP的内置流媒体功能，服务器可以将实时更新推送到客户端，而无需全双工WebSocket连接的开销。 客户端可以使用Stream API在数据可用时读取数据。

最后，作者介绍了**eventkit**，这是一个旨在简化异步数据流管理的库，进一步简化了使用HTTP流媒体实现实时更新的过程。 作者鼓励读者探索eventkit及其HTTP流媒体指南。 本质上，本文建议在选择WebSockets之前仔细考虑应用程序的特定需求，因为像HTTP流媒体这样更简单的替代方案通常可以在降低复杂性的同时提供所需的功能。

---

## 12. 谷歌在人工智能的各个领域都取得了胜利。

**原文标题**: Google Is Winning on Every AI Front

**原文链接**: [https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front](https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front)

该文章认为，谷歌，特别是谷歌DeepMind，目前在人工智能领域占据主导地位，超越了OpenAI和Anthropic。作者Alberto Romero强调了谷歌在最初推出ChatGPT时表现不佳后的卷土重来。

支持这一论点的关键点包括：

*   **卓越的AI模型：** Gemini 2.5 Pro被认为是全球最佳模型，在LMArena和GPQA Diamond等基准测试以及私有基准测试和代理竞技场中表现出色。Gemini 2.5 Flash具有速度和成本效益。谷歌还拥有Gemma 3，一个具有竞争力的开源模型。
*   **在生成式AI领域的主导地位：** 谷歌在文本之外的各种生成式AI领域处于领先地位，其Lyria（音乐）、Imagen 3（图像）、Veo 2（视频）和Chirp 3（语音/语音）等工具正被集成到Vertex AI中。
*   **高级智能代理：** 谷歌的Deep Research模式优于OpenAI，并且正在开发Project Astra（助理）和Project Mariner（计算机交互）。
*   **强大的研究能力：** 谷歌持续发表高质量的研究论文。
*   **软件生态系统：** 谷歌受益于其现有庞大的用户群，遍布搜索、YouTube、Android、Gmail和Workspace等多个平台，为数十亿用户提供默认的AI访问权限。
*   **基础设施优势：** 谷歌是一家拥有谷歌云的超大规模企业，出租芯片并与英伟达合作，而OpenAI和Anthropic则依赖于其他云提供商。
*   **硬件能力：** 谷歌开发自己的AI芯片（TPU），与英伟达竞争并获得收入。
*   **移动集成：** 谷歌将Gemini集成到其Pixel手机中，提供独特的AI功能。

作者认为，谷歌在AI、软件、云、硬件和移动等方面的多方面方法，使其比竞争对手具有显著优势。

---

## 13. Fedora 更改旨在实现 99% 的软件包可复现性

**原文标题**: Fedora change aims for 99% package reproducibility

**原文链接**: [https://lwn.net/Articles/1014979/](https://lwn.net/Articles/1014979/)

LWN.net文章：Fedora计划在Fedora 43（预计2025年10月发布）实现99%软件包可复现性。可复现构建确保相同的源代码、构建环境和指令产生逐位相同的工件。虽然Fedora对构建过程有良好的控制，但可复现构建通过缓解供应链攻击和支持独立验证来增强安全性。

Fedora对可复现性的定义与Debian略有不同，排除了签名和一些元数据（如BUILDTIME、BUILDHOST），以适应RPM软件包的特性。之前的更改，如将修改时间钳制到SOURCE_DATE_EPOCH以及使用`add-determinism`工具标准化元数据，已经实现了90%的可复现性。

达到99%的要求需要打包者将可复现性问题视为bug。`fedora-repro-build`实用程序将允许本地重新构建测试，而公共的`rebuilderd`实例将提供独立验证。Fedora的打包指南将被更新，以鼓励可复现构建，并针对不可复现的软件包提交bug。虽然一些软件包（如使用Haskell或Go的软件包）面临可复现性挑战，但该工作旨在通过发现错误来提高软件包质量。

Fedora Discourse论坛上的讨论围绕托管和维护`rebuilderd`实例展开，可能在Fedora基础设施之外进行以保证独立性。还将考虑将`rebuilderd`与现有工具（如Koji和Copr）集成，以实现无缝的工作流程和测试。该提案在实施之前还需要获得FESCo的批准，目标是在Fedora 43发布之前完成。

---

## 14. Adobe 因强烈反对删除 Bluesky 帖子

**原文标题**: Adobe deletes Bluesky posts after backlash

**原文链接**: [https://petapixel.com/2025/04/10/adobe-deletes-bluesky-posts-after-furious-backlash/](https://petapixel.com/2025/04/10/adobe-deletes-bluesky-posts-after-furious-backlash/)

Adobe在Bluesky上与艺术家和设计师互动的尝试惨遭滑铁卢。在创建Adobe和Photoshop的账户后，该公司遭到了大量用户的批评，这些用户对Adobe的商业行为感到不满。主要的抱怨集中在该公司的订阅模式、价格上涨以及对人工智能的采用。

用户提到了被认为质量下降的软件价格上涨，并指责Adobe在“法西斯所有”的X（前身为Twitter）上支持人工智能生成的艺术。

负面反应非常强烈，以至于Adobe最终删除了其在两个账户上的初始帖子。Bluesky用户庆祝这些帖子的删除，突显了艺术界对该公司的普遍敌意。这种不受欢迎源于Adobe十多年前转向订阅模式，加上最近的价格上涨以及该公司对人工智能的拥抱。PetaPixel的一位编辑指出，由于沟通不畅和负面新闻，Adobe与摄影师和媒体的关系一直紧张。

---

## 15. 刻意结交密友 (2021)

**原文标题**: Intentionally Making Close Friends (2021)

**原文链接**: [https://www.neelnanda.io/blog/43-making-friends](https://www.neelnanda.io/blog/43-making-friends)

尼尔·南达的文章《有意结交挚友》详细描述了他从只有肤浅友谊到刻意培养深厚情感联系的历程。他意识到，对他而言，建立亲密友谊并非自然而然的过程，而是一种可以学习和优化的技能。

他最初的方法包括识别现有友谊中的转折点，并通过设计脆弱的、一对一的对话来复制它们，通常使用一份精选的个人问题清单。虽然最初很尴尬，但这个实验被证明出人意料地成功，使他摆脱了肤浅互动的循环。

南达强调了在积极寻找和培养这些联系中的主动性的重要性，挑战了友谊应该“自然发生”的被动心态。他提倡保持真诚的同时保持有意为之，并建议采用公开讨论他的策略等方法。

关键建议包括通过关注双方都感兴趣的内容，在对话中“寻求兴奋点”，并运用“递归好奇心”来深入研究有趣的话题。他还强调了脆弱性的作用，主张创造一个安全的空间，以便进行分享并在更深的情感层面上建立联系。南达认为，深思熟虑地应用有意的努力可以显著提高友谊的质量和深度，从而带来更充实的生活。核心信息是，亲密的友谊需要积极的努力，并且个人可以提高他们建立和维持这些关系的能力。

---

## 16. 为什么“鲁珀特王子之泪”玻璃能强大到击碎子弹 (2023)

**原文标题**: Why 'Prince Rupert's Drop' Glass Is Strong Enough to Shatter a Bullet (2023)

**原文链接**: [https://www.popularmechanics.com/science/a40008994/why-the-prince-ruperts-drop-is-so-strong/](https://www.popularmechanics.com/science/a40008994/why-the-prince-ruperts-drop-is-so-strong/)

这篇《大众机械》的文章解释了鲁珀特之泪惊人强度背后的科学原理。鲁珀特之泪是一种玻璃泪珠，甚至可以击碎子弹。它是通过将熔融玻璃滴入冷水中制成的，导致表面迅速冷却并形成硬化外壳。然后，内部冷却并收缩，压缩内部核心并在泪珠内部产生巨大的张力。这种压缩力就像一个减震器，使泪珠的圆形部分异常坚固。

文章详细介绍了当冲击泪珠球部时，冲击波如何在泪珠中传播，导致其近乎瞬间的破坏。由于玻璃中压缩力的释放，子弹本身在撞击时可能会破碎。

除了其新颖性之外，鲁珀特之泪还展示了抗压强度的原理，该原理已应用于诸如大猩猩玻璃之类的技术中。大猩猩玻璃是使用离子交换制成的，其中较大的钾离子取代了玻璃表面的较小钠离子，从而产生压力并压缩内部。正如探索频道节目《流言终结者》在链接的康宁视频中所展示的那样，这种平衡的压缩创造了一个坚固的保护层，并且可以应用于像手机这样的设备。虽然不是坚不可摧的，但大猩猩玻璃提供了显著的防损伤保护。

---

## 17. Yakread排名算法

**原文标题**: Yakread's Ranking Algorithm

**原文链接**: [https://obryant.dev/p/yakread-algorithm/](https://obryant.dev/p/yakread-algorithm/)

本文介绍 Yakread 背后的核心排序算法，它是一个结合了新闻邮件/RSS订阅和书签文章的个性化信息流。该算法专注于选择和排序内容，以便在用户的“为你推荐”信息流中呈现。

对于**书签**，项目最初按“新鲜度”（最少跳过，最新书签）排序。 接近线性的洗牌，带有一个 `p` 参数（设置为 0.1，导致 65% 的几率第一个项目将位于最新项目的前 10 名）增加了一些随机性。 最后，该算法将推荐限制为每个网站一个书签，以避免单个域名占据主导地位。

对于**订阅**，该过程涉及两个关键步骤。 首先，该算法基于用户交互（浏览、跳过、喜欢、不喜欢）使用加权值和“贝塔分布期望值”来计算每个订阅的“亲和力得分”。 新订阅会获得一个起始奖励。 然后，订阅按优先级排序，并将置顶订阅根据亲和力穿插到列表中，无论分数如何，都有 30% 的几率选择置顶订阅。 最后，对订阅进行洗牌，算法从每个订阅中选择“最新”的项目，类似于书签选择。

**交错**书签和订阅是通过成对比较项目来完成的。 基于每个项目被跳过的次数使用加权随机选择，从而偏向于跳过次数较少的项目。 这确保了两种内容类型之间的平衡。

---

## 18. 用原子级薄半导体制造的32位处理器

**原文标题**: A 32-bit processor made with an atomically thin semiconductor

**原文链接**: [https://arstechnica.com/science/2025/04/researchers-build-a-risc-v-processor-using-a-2d-semiconductor/](https://arstechnica.com/science/2025/04/researchers-build-a-risc-v-processor-using-a-2d-semiconductor/)

中国研究人员利用二硫化钼（MoS2）——一种原子级薄半导体材料，而非硅，制造了一款名为RV32-WUJI的32位RISC-V处理器。这是向“超越硅”硬件迈出的重要一步。二硫化钼与石墨烯类似，形成单原子厚度的薄片，但与石墨烯不同，它是一种半导体。

该处理器使用了近6000个晶体管，可以执行完整的32位RISC-V指令集，但其运行频率为千赫兹级别，并且每次只能添加单个比特。一个关键的挑战是无法像硅一样掺杂二硫化钼。该团队通过使用不同的金属（铝和金）进行布线，并根据布线材料和嵌入调整晶体管阈值电压来克服了这一问题。机器学习被用于优化布线和材料，以提高单个晶体管的性能。

该处理器采用耗尽型反相器，并使用18个功能逻辑门（在25个测试的逻辑门中）构建。芯片级的良率很高（99.8%），但较大寄存器（例如，64位）的良率明显较低。

虽然该处理器证明了用二硫化钼构建复杂电路的可行性，但作者并不认为它可以取代硅。相反，他们设想了诸如简单传感器超低功耗处理等特定应用，并承认其未来扩展的潜力。这项研究突出了在先进电子产品中使用二维材料的进展。

---

## 19. Erlang并非关于轻量级进程和消息传递 (2023)

**原文标题**: Erlang's not about lightweight processes and message passing (2023)

**原文链接**: [https://stevana.github.io/erlangs_not_about_lightweight_processes_and_message_passing.html](https://stevana.github.io/erlangs_not_about_lightweight_processes_and_message_passing.html)

Erlang真正强大的地方并非轻量级进程和消息传递，而是其使用“行为”的结构化方法。作者解释说，Erlang最初为爱立信的可靠分布式系统而设计，依靠被称为行为的通用组件来实现可靠性。

行为类似于其他语言中的接口，定义了实现的契约。本文重点介绍了`gen_server`行为作为一个关键示例，展示了它如何封装并发性，使开发人员能够编写顺序代码，而`gen_server`处理并发请求。

作者强调，Erlang提供了一组关键行为，如`gen_server`、`gen_event`（事件管理器）、`gen_statem`（状态机）、`supervisor`、`application`和`release`，并认为这些足以构建健壮的分布式系统。尤其是Supervisor，通过根据预定义的策略监视和重启失败的进程，从而实现容错，秉承了“任其崩溃！”的理念。

本文以爱立信用Erlang构建的AXD301电话交换机为例，展示了其卓越的可靠性（99.9999999%）。作者最后建议，其他语言应采用Erlang的结构化行为方法，而不仅仅是模仿其并发原语，并提出Input -> State -> (State, Output)的通用接口签名，作为在其他语言中实现行为的起点。

---

## 20. 复古计算文物直播

**原文标题**: Retro Computing Artifacts Stream

**原文链接**: [https://retro-computing-stream.onrender.com/](https://retro-computing-stream.onrender.com/)

本文介绍了一种“复古计算文物流”，这是一个持续且自动更新的 feed，其复古计算材料来源于互联网档案馆。该流允许用户浏览与计算历史相关的数字化文物。用户可以手动滚动浏览内容，也可以被动地观看新图像自动出现。其核心功能是提供一个经过策划、不断发展的窗口，让人们了解复古计算的历史，使浩瀚的档案资料对那些对计算机发展感兴趣的人来说更易于访问和参与。用户界面包含暂停自动滚动的特性，以便更仔细地检查单个项目。本质上，该流就像一台“时间机器”，将用户带回计算的数字历史。

---

## 21. Rust到C编译器 – 95.9%测试通过率，奇特平台

**原文标题**: Rust to C compiler – 95.9% test pass rate, odd platforms

**原文链接**: [https://fractalfir.github.io/generated_html/cg_clr_odd_platforms.html](https://fractalfir.github.io/generated_html/cg_clr_odd_platforms.html)

`rustc_codegen_clr` 项目进展：Rust to C 编译器近况及 Rust Week 演讲预告

本文更新作者的 Rust to C 编译器项目 `rustc_codegen_clr` 的进展。重磅消息是作者将在乌得勒支的 Rust Week 上就该项目发表演讲。

项目已取得显著进展，核心测试通过率提升至 95.9%。最近的错误修复主要集中在 128 位内部函数、溢出检查算术和子切片上。通过对高低 64 位半部分进行 popcount 求和，解决了位计数内部函数中截断 128 位整数的问题。对 128 位乘法实现了一个简单但低效的溢出检查。修复了由不正确的指针偏移引起的子切片错误。

作者尽可能利用 Rust 内置的模拟内部函数版本，特别是对于像 `carrying_mul_add` 这样需要 256 位计算的复杂操作。 还在努力提高与更广泛的 C 编译器的兼容性，包括那些在冷门平台上的编译器，以期在 LLVM 或 GCC 不可用的情况下实现 Rust 支持。目标是定位标准的 C99/ANSI C 和 POSIX API。

通过优化整数文字格式化和简化 `#line` 指令在调试信息中的使用，实现了小幅性能提升。`rustc_codegen_clr` 的内部重构正在进行中，部分代码被拆分为单独的 crate 以缩短构建时间，并且正在朝着更节省内存的 interned IR 方向发展。

最后，作者计划将来撰写关于 Rust 恐慌和内存分析器的文章。

---

## 22. C++: 更精简的 Lambda == SHORTY (滥用?)

**原文标题**: C++: terser (shorter) lambda == SHORTY (ab-use?)

**原文链接**: [https://github.com/hanickadot/shorty](https://github.com/hanickadot/shorty)

"SHORTY" C++ 库为 lambda 表达式提供了更简洁的语法，旨在减少样板代码，而无需创建完整的惰性 DSL。它利用 `shorty::literals` 命名空间为常用的 lambda 操作提供简写。

主要特性包括简化的比较（例如，`$lhs > $rhs` 用于排序），使用视图进行简洁的过滤和转换（例如，`$i % 2 == 0` 用于过滤偶数），以及使用 `$call<sqrt>` 或 `$<sqrt>` 轻松调用外部函数。 使用 `$cast<int>` 或 `<int>` 也简化了类型转换。

SHORTY 提供了几种访问 lambda 表达式中参数的方法：使用 `$0-$9` 或 `$arg<N>` 进行数值访问，使用 `$a-$f`、`$x`、`$y`、`$z` 或 `$i`、`$n`、`$k`、`$in` 进行名称访问，以及使用 `$lhs`、`$rhs`（用于二元可调用对象）或 `$it`（用于单参数迭代器）进行专用访问。 它会自动解包单参数 lambda 表达式和惰性调用的类元组参数。 `$argc` 返回参数数量，`$args` 将所有参数作为元组提供。

该库还处理按引用捕获变量 (`$(v)` 或 `$ref(v)`)，按值捕获变量 (`$value(v)`、`$val(v)` 或 `$copy(v)`)，以及作为编译时常量捕获变量 (`$fixed<v>` 或 `$const<v>`)。 它支持使用 `$call<callable>(args...)` 调用函数（或构造新对象），并使用 `($a, $b, $c)` 创建元组。 也支持直接对参数使用赋值运算符，如 `+=`、`-=` 等。

---

## 23. 蓝王子：类Rogue益智杰作

**原文标题**: Blue Prince is a roguelike puzzle masterpiece

**原文链接**: [https://mssv.net/2025/04/07/a-puzzle-designer-on-blue-prince-a-roguelike-puzzle-masterpiece/](https://mssv.net/2025/04/07/a-puzzle-designer-on-blue-prince-a-roguelike-puzzle-masterpiece/)

《蓝王子》是一款roguelike解谜游戏，背景设定在一座广阔的豪宅中。玩家扮演已故的赫伯特·S·辛克莱的侄孙，必须找到第46号房间才能继承遗产。该游戏结合了roguelike机制与解谜、探索和故事讲述。

每次“挑战”都需要从三个房间中选择一个来构建一个5x9的网格豪宅布局，平衡资源、出口和目标。房间里充满了线索、笔记和环境谜题，这些都构成了一个关于痴迷、期望和代际创伤的非线性故事。虽然解谜能提供奖励，但游戏也提供了到达第46号房间的替代路径，因此没有谜题是强制性的。

《蓝王子》包含一个类似老虎机的元素，有机会获得所需的物品，评论员认为这令人上瘾。游戏包含永久升级，可以减轻重复元素，并提供微妙的提示系统。尽管存在运气成分，但游戏是公平的，并能弥补坏运气。

评论员承认，随机系统可能导致一些玩家将故事更多地体验为一种“氛围”而非连贯的叙事，但赞扬了游戏的整体设计、故事和令人上瘾的游戏玩法。评论员在17小时内完成了游戏，但表示仍有大量内容等待发现。

---

## 24. 艾姆斯铁锹工具公司铁锹、铲子和勺子目录 (1926) [pdf]

**原文标题**: Ames Shovel and Tool Catalog of Shovels, Spades and Scoops (1926) [pdf]

**原文链接**: [https://stonehill-website.s3.amazonaws.com/files/resources/1926-ames-catalog-2.pdf](https://stonehill-website.s3.amazonaws.com/files/resources/1926-ames-catalog-2.pdf)

该文档是一个严重损坏或无法读取的PDF文件，虽然具有标准的PDF文件头和文件尾结构，但其内容基本为乱码。标题显示其为Ames Shovel and Tool公司1926年的目录，内容包括铲子、锹和勺子。然而，PDF数据本身似乎受到了严重损坏，无法提取任何与目录内容、产品详情或关于Ames的历史信息相关的有意义的内容。文件中存在大量的二进制数据和编码问题，使得总结标题所暗示的实际目录信息成为不可能。尝试解码和提取相关信息需要高级数据恢复技术，并且无法保证成功重建原始目录内容。简而言之，虽然标题暗示着一个有价值的历史资源，但该文档目前的状态是无法使用的。

---

## 25. 曾经绿意盎然的撒哈拉是令人惊讶的独特人类群体的家园。

**原文标题**: Once lush Sahara was home to a surprisingly unique group of humans

**原文链接**: [https://www.sciencealert.com/once-lush-sahara-was-home-to-a-surprisingly-unique-group-of-humans](https://www.sciencealert.com/once-lush-sahara-was-home-to-a-surprisingly-unique-group-of-humans)

一项新的基因分析显示，撒哈拉沙漠在7000年前曾是一片茂盛的热带草原，是居住着一个令人惊讶的孤立和独特人类群体的家园。研究人员对在利比亚塔卡科里岩棚发现的两名女性个体的古代DNA进行了测序，发现她们与来自摩洛哥的15000年前的采集者拥有最多的基因相似性。这表明，在撒哈拉湿润期之前和期间，存在一个稳定的北非人口，该人口不同于撒哈拉以南非洲人，尽管他们都起源于最初的非洲人类迁徙。

虽然在很大程度上与世隔绝，但这个撒哈拉血统接受了来自黎凡特地区的少量基因，包括一些尼安德特人DNA。有趣的是，塔卡科里个体所含的尼安德特人DNA比摩洛哥采集者少，这表明存在一个屏障，阻止了来自欧洲的进一步基因流动延伸到撒哈拉沙漠之外。

考古证据表明，塔卡科里人是早期的牲畜牧民，这一习俗是在没有重大基因交流的情况下采用的。这表明畜牧业是通过文化交流传播的，而不是大规模迁徙。撒哈拉沙漠的多样化生态系统，包括湿地和山脉，可能充当了南部迁徙的屏障。这项研究为了解非洲关键地区的人类迁徙、适应和文化进化提供了见解。

---

## 26. 倭黑猩猩使用一种曾被认为人类独有的句法。

**原文标题**: Bonobos use a kind of syntax once thought to be unique to humans

**原文链接**: [https://www.newscientist.com/article/2474993-bonobos-use-a-kind-of-syntax-once-thought-to-be-unique-to-humans/](https://www.newscientist.com/article/2474993-bonobos-use-a-kind-of-syntax-once-thought-to-be-unique-to-humans/)

本文报道了一项突破性发现：倭黑猩猩表现出一种句法形式，特别是“非平凡组合性”，这曾被认为是人类独有的。由梅丽莎·贝尔特（Mélissa Berthet）领导的研究人员在刚果民主共和国的科科洛波里倭黑猩猩保护区分析了近 1000 种倭黑猩猩的发声，仔细记录了背景信息，以解读单个叫声及其组合的含义。

利用语言学技术，他们创建了一个倭黑猩猩叫声及其含义的“字典”。他们识别出四种组合叫声，其中三种表现出非平凡组合性，这意味着组合后的叫声传达的含义与单个组成部分的简单相加不同。例如，“高音呼叫 + 低音呼叫”结合了“注意我”和“我感到兴奋”的意思，表示“注意我，因为我处于困境中”，通常在寻求支持以对抗恐吓时使用。

研究结果表明，这种类型的句法在进化上是很古老的，早于人类、黑猩猩和倭黑猩猩的分化。虽然这并不意味着倭黑猩猩拥有人类意义上的语言，但它表明存在一种复杂的交流系统，与人类语言有相似之处。这项被誉为革命性的发现为比较和进化语言学开辟了新途径，表明组合能力很可能是从我们共同的祖先那里继承下来的，可能在 700 多万年前。

---

## 27. 名为微软高峰的Windows 2000服务器

**原文标题**: Windows 2000 Server named peak Microsoft

**原文链接**: [https://www.theregister.com/2025/04/11/windows_2000_best_microsoft/](https://www.theregister.com/2025/04/11/windows_2000_best_microsoft/)

本文探讨了一项调查的结果，该调查邀请《The Register》的读者回顾微软 50 年的历史，重点关注里程碑和失误。评论者的普遍共识是 Windows 2000 Server 代表了微软的巅峰。读者们赞赏其功能性和稳定性，并将其与后来的操作系统（如 Windows 8 和 11）进行了鲜明对比。虽然有些人承认 XP、Windows 7 甚至 Vista 的优点，但总体情绪倾向于 Windows 2000 之后的衰落。

本文还涉及了对微软收购诺基亚及其随后对 Windows Phone 处理的复杂情感，认为缺乏升级路径和不一致的开发框架是主要的失败之处。有趣的是，一位评论者指出，微软软件的高价格和低质量分别是显著的“高点”和“低点”。 Office 套件获得了积极评价。

本文承认微软成功转型到云端是一项成就，尽管缺乏原创性。它还认识到该公司在克服法律挑战方面的韧性。最终，本文认为微软最好的日子已经过去，Windows 2000 Server 是一个亮点。未来将决定微软当前对人工智能的关注是否会被视为成功或失误。

---

## 28. 求知者的WebRTC

**原文标题**: WebRTC for the Curious

**原文链接**: [https://webrtcforthecurious.com](https://webrtcforthecurious.com)

面向求知者的WebRTC 是一本开源书籍，旨在提供对WebRTC技术的全面且公正的理解。它面向所有级别的开发者，从WebRTC新手到寻求超越基本API的更深入知识的经验丰富的实施者。本书侧重于协议和API，总结了RFC和未公开的知识，而不受特定软件供应商的束缚，也不提供包含大量代码的教程。

本书的结构设计旨在实现灵活学习，各个章节彼此独立，可以以任何顺序阅读。每章都从三个层面解决一个问题：要解决的问题、技术解决方案以及进一步学习的资源。无需任何先验知识，读者可以从任何地方开始。虽然承认其他资源可能提供关于特定主题的更深入的信息，但本书优先教授整个WebRTC系统。

本书以ePub和PDF格式在GitHub和WebRTCforTheCurious.com上提供，并采用CC0许可，这意味着可以免费使用而无需署名。本书致力于保护隐私，由个人为个人编写，与供应商无关，并且该网站没有分析或跟踪。欢迎通过GitHub提供贡献和改进，用户可以提出问题、建议更改或为开发做出贡献。

---

## 29. 金星地表的所有照片 (2021)

**原文标题**: Every picture from Venus' surface, ever (2021)

**原文链接**: [https://www.planetary.org/articles/every-picture-from-venus-surface-ever](https://www.planetary.org/articles/every-picture-from-venus-surface-ever)

本文展示了所有从金星表面拍摄的图像，这项壮举仅由苏联的金星探测器于1975年和1982年完成。金星上的极端高温和高压使得着陆和拍摄图像极其困难。金星任务总共四次，传回了全景图像，揭示了黄色的天空和荒凉、龟裂的景观，让我们得以一窥这个可能曾经类似于地球，但在灾难性的气候变化事件发生之前的世界。

本文重点介绍了哲学教授泰德·斯特里克的工作，他专门从事早期太空任务图像的重建工作。斯特里克利用俄罗斯科学院的数据，创建了原始金星全景图像的最佳版本。文章展示了六张全景图像：金星9号（1975年）、金星10号（1975年）、金星13号前置和后置摄像头（1982年），以及金星14号前置和后置摄像头（1982年）。

最后，本文包含一项行动号召，敦促读者通过联系他们的国会代表来支持美国宇航局的科学经费，并通过捐赠给行星学会来推进太空科学和探索。

---

## 30. 但如果我想要一匹更快的马呢？

**原文标题**: But what if I want a faster horse?

**原文链接**: [https://rakhim.exotext.com/but-what-if-i-really-want-a-faster-horse](https://rakhim.exotext.com/but-what-if-i-really-want-a-faster-horse)

科技公司正日益牺牲实用功能和用户控制，转而优先发展模仿 TikTok 无尽、算法驱动的内容流的“创新”。本文认为，作者借用通常用于支持激进创新的“更快的马”类比，指出有时用户仅仅想要现有解决方案的改进版本。

作者以 Netflix 和 Spotify 为例。他感叹 Netflix 已经从一个拥有良好推荐的可靠资源库，转变为一个令人困惑的“体验”，其界面不断变化、类别毫无意义，目录管理也并不可靠。同样，Spotify 也因偏离用户可控的简单音乐库，转向不断变化的内容和播客流而受到批评。

核心问题是，这些平台正在牺牲一致性、用户自主性和真正的用户体验改进，以追逐 TikTok 的参与模式，即用户被动地消费源源不断的内容。这种趋势已经蔓延到 YouTube、LinkedIn 甚至 Substack，它们都在加入短视频和算法驱动的信息流。作者将其比作“蟹化”现象，一种趋同进化，不同的平台都在进化成同质化的、类似 TikTok 的体验，而忽略了它们最初的目的或用户需求。他总结说，人们对现有模式的有用改进的渴望，正被追逐短暂的参与度指标所忽视。

---

## 31. 铅仍然对你的大脑有害

**原文标题**: Lead is still bad for your brain

**原文链接**: [https://neurofrontiers.blog/why-lead-is-still-bad-for-your-brain/](https://neurofrontiers.blog/why-lead-is-still-bad-for-your-brain/)

铅仍然对你的大脑有害

这篇文章《铅仍然对你的大脑有害》强调了铅暴露的持续危害，尽管过去已经努力减少其使用。虽然在汽油和油漆等产品中对铅的热情使用已经减少，但它在环境中的持久性仍然令人担忧。铅不易降解，这意味着过去的污染仍然构成风险，再加上它继续在电池等产品中使用，情况更加复杂。

作者强调，铅暴露没有安全水平，即使是少量浓度也会产生神经系统影响，尤其是在儿童身上，他们的身体更容易吸收铅。铅通过肠道或肺部进入人体，并积聚在软组织和骨骼中，有可能在日后渗回血液中。

长期铅暴露与记忆问题、认知和行为问题有关，包括智商下降和攻击性增加。铅的神经毒性机制包括破坏细胞膜流动性，干扰基于钙的神经通讯，以及产生损害细胞的活性氧。

文章鼓励采取积极措施来减轻铅暴露，例如安全移除含铅油漆或管道，倡导社区铅移除计划，并支持受影响的个人。虽然早期干预和丰富的环境有助于逆转铅暴露的某些影响，但作者强调预防是关键，尤其是在较旧的房屋、工业区和资金不足的社区，这些地方铅污染更为普遍。

---

## 32. 泄露数据揭示以色列政府要求 Meta 删除支持巴勒斯坦帖文的活动

**原文标题**: Leaked data reveals Israeli govt campaign to remove pro-Palestine posts on Meta

**原文链接**: [https://www.dropsitenews.com/p/leaked-data-israeli-censorship-meta](https://www.dropsitenews.com/p/leaked-data-israeli-censorship-meta)

根据Drop Site News获得的泄露Meta数据，以色列政府一直在积极游说从Facebook和Instagram上删除支持巴勒斯坦的内容，自2023年10月7日以来，Meta已配合了94%的删除请求。这些请求通常针对阿拉伯和穆斯林占多数国家的用戶，以色列是全球删除请求的最大发起者。这些请求经常将内容归类为“恐怖主义”或“暴力和煽动”，即使没有具体细节。Meta的人工智能也在接受这些删除数据的训练，可能导致未来出现带有偏见的审查。

在Meta内部，关键职位由与以色列政府有关联的个人担任，这引起了人们对偏见的担忧。由前以色列军方官员盖伊·罗森运营的诚信组织负责执行政策组织制定的政策，而政策组织现在由曾与以色列官员合作过的乔尔·卡普兰领导。Meta负责以色列和犹太人散居地公共政策的主管约尔达娜·卡特勒也曾介入标记支持巴勒斯坦的内容，包括与已故巴勒斯坦作家加桑·卡纳法尼有关的材料。

虽然大多数国家都将审查重点放在本国公民身上，但以色列主要针对来自阿拉伯和穆斯林占多数国家的用戶，只有一小部分删除请求针对以色列用戶。尽管内部提出了关于过度强制执行针对支持巴勒斯坦内容的担忧，但Meta领导层已优先考虑删除潜在的违规内容，而不是冒着执行不足的风险。人权观察组织也记录了Meta平台上不成比例地删除了支持巴勒斯坦的内容。

---

## 33. 使用重心坐标在四边形上进行双线性插值

**原文标题**: Bilinear interpolation on a quadrilateral using Barycentric coordinates

**原文链接**: [https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/](https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/)

通过 AgilitySDK 预览版 1.716.0 发布 DirectX 和视频编码新功能通知。

---

## 34. Datastar：面向未来的Web框架？

**原文标题**: Datastar: Web Framework for the Future?

**原文链接**: [https://chrismalek.me/posts/data-star-first-impressions/](https://chrismalek.me/posts/data-star-first-impressions/)

Chris Malek 探索 Datastar，一款旨在简化实时 Web 应用开发的新型超媒体框架，并将其视为 HTMX 的潜在替代方案。他强调 Datastar 的服务器驱动架构、利用服务器发送事件 (SSE) 实现快速更新，以及用于自动 UI 更改的“信号”，这与他偏爱源于 PeopleSoft ERP 背景的后端中心解决方案的倾向相符。

Malek 对 HTMX 复杂性的不满，尤其是在前端交互和依赖 JavaScript（他不喜欢）方面，促使他重新审视 Datastar。他强调了 Datastar 的关键方面，包括用于反应式编程的信号、用于高效数据流的 SSE、用于触发服务器逻辑的操作以及用于 UI 更新的 HTML 片段。

Datastar 融合了 HTMX 和 AlpineJS 的优势于单一库中。 这种方法允许开发人员在不严重依赖 JavaScript 的情况下处理 UI 状态和交互，使其适合那些喜欢后端控制的人。 Malek 强调了理解“信号”对于简化 UI 开发和反应式编程的重要性。 他还指出 Datastar 的后端无关性，使其与 Go（他首选的语言）和其他服务器端语言兼容。

---

## 35. AI无法停止捏造软件依赖项并破坏一切

**原文标题**: AI can't stop making up software dependencies and sabotaging everything

**原文链接**: [https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/](https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/)

本文探讨了使用人工智能代码生成工具所带来的日益增长的安全风险：人工智能倾向于虚构不存在的软件包，以及恶意行为者随后对这种现象的利用。这些人工智能编码助手会建议包含不存在的软件包的代码，研究人员已在商业和开源模型中量化了这个问题。

网络罪犯正在利用这种“抢占虚名”行为，创建具有虚构名称的恶意软件包，并将它们上传到PyPI和npm等公共存储库。当人工智能再次虚构软件包名称时，代码将安装恶意软件。

安全专家警告说，开发人员越来越依赖人工智能进行编码，但常常不验证人工智能的建议，导致潜在的漏洞代码。搜索引擎上人工智能生成的摘要可能会通过错误地验证这些虚假软件包，从而加剧这个问题，产生一种虚假的安全感。

文章重点介绍了具体案例，包括谷歌的AI Overview建议了一个恶意npm软件包，以及一份暗网剧本，详细介绍了如何使用人工智能辅助生成的恶意npm软件包构建基于区块链的僵尸网络。

Python软件基金会正在积极努力缓解这个问题。文章敦促开发人员在安装之前验证软件包名称，检查拼写错误，并审查软件包内容。还鼓励组织在内部镜像软件包存储库，以便更好地控制可用的软件包。

---

## 36. 苹果、英伟达、戴尔等公司获得关税豁免，适用新规

**原文标题**: Apple, Nvidia, Dell, and Others Get a Tariffs Exemption Under New Rules

**原文链接**: [https://www.barrons.com/articles/tariffs-exclusions-exemptions-apple-nvidia-dell-smartphones-pcs-b2e069ff](https://www.barrons.com/articles/tariffs-exclusions-exemptions-apple-nvidia-dell-smartphones-pcs-b2e069ff)

无法访问文章链接。

---

## 37. 能源部将大学科研经费间接费用削减至15%

**原文标题**: Energy Department cuts university overhead rates to 15% on research grants

**原文链接**: [https://www.science.org/content/article/energy-department-cuts-university-overhead-rates-to-15-on-research-grants](https://www.science.org/content/article/energy-department-cuts-university-overhead-rates-to-15-on-research-grants)

能源部将部分大学科研项目管理费上限设定为15%

---

## 38. AI编码与花生酱果冻问题

**原文标题**: AI Coding and the Peanut Butter and Jelly Problem

**原文链接**: [https://iamcharliegraham.substack.com/p/ai-coding-and-the-peanut-butter-and](https://iamcharliegraham.substack.com/p/ai-coding-and-the-peanut-butter-and)

无法访问文章链接。

---

## 39. 现代 6502

**原文标题**: Modern 6502

**原文链接**: [https://www.mikekohn.net/micro/modern_6502.php](https://www.mikekohn.net/micro/modern_6502.php)

迈克尔·科恩的《现代6502》展示了使用Western Design Center W65C265SXB开发板的项目，这是一款现代微控制器，以6502（实际上是65C816）处理器为特色。科恩作为6502的长期爱好者，展示了四个小项目，演示了该芯片的功能：LED闪烁（使用65C816和6502汇编语言）、音乐播放（使用Java和芯片的音调发生器）、软件SPI DAC声音播放器（汇编语言）以及脚踏板控制的音调发生器（汇编语言）。

文章详细介绍了所使用的硬件（带有UART、IO、音调发生器的W65C265SXB开发板）和软件工具（naken_asm、Java Grinder、EasySXB）。科恩重点介绍了使用Java Grinder进行65C816开发，并强调了芯片音调发生器产生的正弦波声音的质量。他还描述了如何通过软件SPI与MCP4921 DAC芯片连接，以播放声音样本（特别提到了《终结者》中的一个声音样本）。最后，他描述了如何使用按钮和W65C265SXB开发板创建一个脚踏控制的音调发生器。文中包含了指向源代码和演示这些项目的视频的链接。该页面还提到了mikekohn.net上其他与6502处理器相关的项目。

---

## 40. 德国设立“超高科技部”，主管科研、技术和航空航天

**原文标题**: Germany creates 'super–high-tech ministry' for research, technology, aerospace

**原文链接**: [https://www.science.org/content/article/germany-creates-super-high-tech-ministry-research-technology-and-aerospace](https://www.science.org/content/article/germany-creates-super-high-tech-ministry-research-technology-and-aerospace)

德国合并现有研究、技术和航空航天相关部门，成立新的“超级高科技部”。此次重组由部长贝蒂娜·施塔克-瓦青格主持，旨在简化创新流程、减少官僚主义并提高德国在关键技术领域的竞争力。

其核心目标是解决德国研究领域内被认为存在的效率低下和碎片化问题。此前，研究和技术各方面的职责分散在多个部门。新的架构旨在促进更好的协调、更快的决策制定以及更连贯的国家创新战略。

该部门将专注于人工智能、生物技术、量子计算和太空探索等关键领域。它还将负责支持基础研究并促进技术从学术界向工业界的转移。通过集中这些职能，政府希望加速尖端技术的开发和商业化。

此举被视为对战略技术领域日益激烈的全球竞争，特别是来自美国和中国的竞争的回应。德国政府希望这种更精简和集中的方法能够使该国保持其作为领先创新国家的地位并确保其经济未来。施塔克-瓦青格部长强调了投资研发以创造就业机会和应对社会挑战的重要性。

---

## 41. Rust CUDA 项目

**原文标题**: Rust CUDA Project

**原文链接**: [https://github.com/Rust-GPU/Rust-CUDA](https://github.com/Rust-GPU/Rust-CUDA)

Rust CUDA 项目旨在使 Rust 成为使用 CUDA 工具包进行 GPU 计算的一流语言。它提供了将 Rust 代码编译为 PTX 并利用 CUDA 库的库和工具。

该项目旨在解决 Rust 与 CUDA 结合使用的历史挑战，这种结合以前依赖于经常出现问题的 LLVM PTX 后端。受到 rust-gpu 等项目的启发，该计划提供了一个专门的解决方案。

该项目涵盖了广泛的 CUDA 生态系统，并包括几个关键的 crate：

*   **rustc\_codegen\_nvvm:** 一个以 NVVM IR 为目标的 rustc 后端，用于优化 PTX 代码生成。
*   **cuda\_std:** GPU 端函数和实用程序，用于更简洁、更可靠的内核。
*   **cudnn:** 用于深度神经网络的 GPU 加速原语。
*   **cust:** CPU 端的 CUDA 功能，例如内核启动和内存分配，具有 RAII 和 Rust Results 以实现更好的管理。
*   **gpu\_rand:** GPU 友好的随机数生成。
*   **optix:** 使用 CUDA OptiX 库的 CPU 端硬件光线追踪和降噪。

该项目正在积极开发中（预计存在错误），并鼓励贡献。它提供了示例 Dockerfile，用于在容器环境中构建和运行 Rust-CUDA。该代码以 Apache 2.0 和 MIT 双重许可证获得许可。

---

## 42. 如何制作长弓

**原文标题**: How to Make a Longbow

**原文链接**: [https://www.howtomakealongbow.co.uk](https://www.howtomakealongbow.co.uk)

关于《如何制作长弓》的文章或网站的简介：

*   **主题：** 本文将提供关于如何制作长弓的信息。
*   **动态内容：** 本网站正在积极更新和扩展。
*   **用户互动：** 作者鼓励读者提供反馈和建议，以供未来内容参考。

---

## 43. 玻尔兹-1

**原文标题**: Boltz-1

**原文链接**: [https://github.com/jwohlwend/boltz](https://github.com/jwohlwend/boltz)

Boltz-1 是一个新型开源模型，用于预测复杂生物分子的 3D 结构，包括蛋白质、RNA、DNA 以及其他分子（如修饰残基、配体和聚糖）的组合。它采用 MIT 许可证发布，可免费用于学术和商业用途。该模型允许用户基于特定的相互作用口袋或接触来设定预测条件。

其主要亮点包括处理多样生物分子组分的能力、宽松的许可协议以及代码和权重的可用性。可以通过 PyPI 或直接从 GitHub 安装。可以使用 `boltz predict` 命令，采用 FASTA 文件、YAML 模式或这些文件的目录等各种输入格式来运行推理。该工具还提供评估脚本和预测结果，用于将其性能与其他模型（如 Chai-1 和 AlphaFold3）进行比较。

文章鼓励通过 Slack 频道进行讨论和协作，促进社区参与。提供了训练模型和贡献开发的说明。作者还感谢 Moritz Thüning 提供的 Tenstorrent 硬件优化分支。最后，为 Boltz-1 模型本身和 ColabFold MSA 生成方法都提供了适当的引用。

---

## 44. 慢付、少付或拒付：蓝十字批准手术后拒绝支付

**原文标题**: "Slow Pay, Low Pay or No Pay": Blue Cross Approved Surgeries Then Refused to Pay

**原文链接**: [https://www.propublica.org/article/blue-cross-blue-shield-louisiana-insurance-lawsuit-breast-cancer-doctors](https://www.propublica.org/article/blue-cross-blue-shield-louisiana-insurance-lawsuit-breast-cancer-doctors)

ProPublica文章调查路易斯安那州蓝十字蓝盾保险公司批准乳腺癌手术（特别是乳房切除术和乳房再造术）后，拒绝全额支付医生账单，甚至有时完全不予支付的行为，这些手术均在修复性乳房外科中心进行。患者惠特尼·阿奇获得了授权，但被迫寻求其他治疗方案。

该中心由外科医生弗兰克·德拉克罗切和斯科特·沙利文创立，专门从事自体组织重建，并提供舒适、以患者为中心的环境。他们多次起诉蓝十字，指控其存在批准后拒绝支付的模式，这场激烈的法律战最终以外科医生的重大胜利而告终。

陪审团裁定蓝十字犯有欺诈罪，判给该中心 4.21 亿美元。蓝十字已提出上诉，声称该判决是错误的。这篇文章强调了保险公司和医生之间的权力失衡，保险公司制定自己的指导方针，并且常常获得有利地位。

内部文件显示，蓝十字高管制定了降低费用和延迟付款的流程，甚至从节省外州患者的索赔中获利。虽然通常拒绝全额支付患者费用，但蓝十字已达成特殊协议，以支付高管妻子在同一中心接受的癌症治疗费用。这导致沙利文指责该保险公司虚伪且“道德破产”。

---

## 45. 两秒克隆运行中的虚拟机 (2022)

**原文标题**: We clone a running VM in 2 seconds (2022)

**原文链接**: [https://codesandbox.io/blog/how-we-clone-a-running-vm-in-2-seconds](https://codesandbox.io/blog/how-we-clone-a-running-vm-in-2-seconds)

本文详细介绍了 CodeSandbox 如何使用 Firecracker MicroVM 和内存快照技术，实现开发环境的极速（2 秒以内）VM 克隆。 核心挑战在于使用户能够快速 Fork 正在运行的环境，而无需漫长的设置时间。

最初，CodeSandbox 在浏览器中运行代码，但这受到了限制。 迁移到 VM 引入了启动时间慢的问题。 Firecracker MicroVM 提供了更快的 VM 启动时间，但仍然需要克隆存储库、安装依赖项和启动开发服务器，这花费了太长时间。

解决方案是内存快照。 Firecracker 允许暂停 VM，将其整个状态（内存和配置）保存到磁盘，然后从该快照恢复。 这大大缩短了启动时间，但保存快照最初很慢。

为了加速快照，作者利用了带有 `MAP_SHARED` 标志的 `mmap` 系统调用。 这会将内存快照文件映射到内存，以延迟的方式将更改同步回文件，从而将 I/O 工作分摊到一段时间内。 这将快照保存时间从几秒减少到几毫秒。

然后使用写时复制 (CoW) 加速克隆快照。 新的 VM 不会复制整个内存文件，而是与原始 VM 共享相同的数据。 只有当新的 VM 修改数据时才会复制数据，从而实现近乎瞬时的克隆时间。

最终，VM 克隆过程耗时不到 2 秒，从而可以快速 Fork 和测试任何开发环境中的更改，即使是像 Minecraft 服务器这样复杂的环境。 文章最后列出了尚未编写的细节和计划的未来改进。

---

## 46. 60秒内赚取7000万美元：内幕消息如何助人获利28倍

**原文标题**: $70M in 60 Seconds: How Insider Info Helped Someone 28x Their Money

**原文链接**: [https://data-and-politics.ghost.io/70-million-in-60-seconds-how-insider-information-helped-someone-28x-their-money/](https://data-and-politics.ghost.io/70-million-in-60-seconds-how-insider-information-helped-someone-28x-their-money/)

2025年4月9日，某个人或团体进行了一笔利润极高的交易，利用SPY ETF（追踪标普500指数）的零日期权，在不到一小时内将250万美元的投资变成了超过7000万美元。 这笔交易涉及购买行权价为509美元的看涨期权，当时SPY的交易价格低于500美元。 当地时间下午1点30分，唐纳德·特朗普宣布暂停关税，导致市场飙升，SPY突破509美元大关，使得这些期权变得极具价值，这种冒险策略获得了回报。

该文章强调了交易的异常精确性和时机，暗示可能存在内幕消息。 美东时间下午1点01分也购买了大量SPY股票，如果在收盘价卖出，可能会在六十秒内为买家带来超过1亿美元的利润。 公告发布前交易量迅速增加，这与过去市场冲击不同，过去通常是新闻发布后交易量才会增加。

作者强调，这些交易不仅利润丰厚，而且风险极高，如果市场没有朝着有利的方向发展，全部250万美元都有可能损失殆尽。 作者质疑交易员的成功是源于运气、直觉，还是更令人担忧的、对即将发布的公告的预先了解。 文章总结称，无论原因如何，这些交易都非常成功，并且不能排除内幕交易的可能性。

---

## 47. 一项最新研究表明昆虫起源于甲壳类动物。

**原文标题**: A recent study suggests that insects branched out from crustaceans

**原文链接**: [https://www.smithsonianmag.com/science-nature/you-might-think-of-shrimp-as-bugs-of-the-sea-but-a-remarkable-discovery-shows-the-opposite-bugs-are-actually-shrimp-of-the-land-180986303/](https://www.smithsonianmag.com/science-nature/you-might-think-of-shrimp-as-bugs-of-the-sea-but-a-remarkable-discovery-shows-the-opposite-bugs-are-actually-shrimp-of-the-land-180986303/)

本文探讨了一项近期研究，该研究将昆虫重新归类为甲壳动物的一个亚群，特别是泛甲壳动物群内的一个亚群。这种基于基因数据的转变将昆虫与诸如潜水虾、鳃足纲动物和头甲纲动物等甲壳动物并列。

多年来，昆虫和甲壳动物之间的相似之处已为人所知，但由于趋同进化的可能性，昆虫从甲壳动物进化而来的观点并未被广泛接受。然而，包括2013年一项将昆虫与潜水虾联系起来的研究在内的研究，都指向了更紧密的关系。2023年的研究分析了基因数据，巩固了这种联系，将昆虫置于异甲总目甲壳动物群中。

这种重新分类对理解昆虫进化具有更广泛的意义。此前，人们认为昆虫是从类似马陆的陆生祖先进化而来的。现在，与诸如潜水虾等海洋甲壳动物的联系表明昆虫起源于水生祖先。这种转变有必要重新评估昆虫的起源和进化，包括研究潜水虾的祖先和重新审视化石记录。

本文还与其他重要的系统性转变进行了类比，例如将鸟类视为恐龙以及将鲸类视为偶蹄类动物的认知。这些转变不仅重新排列了进化树，还导致了对性状进化和物种之间关系的新见解。理解昆虫是甲壳动物为理解它们的起源和进化提供了一个新的框架，重点关注水生环境，并有可能揭示被错误分类的化石。

---

## 48. 五角大楼将终止与埃森哲、德勤的51亿美元IT合同

**原文标题**: Pentagon to terminate $5.1B in IT contracts with Accenture, Deloitte

**原文链接**: [https://www.reuters.com/world/us/pentagon-terminate-51-billion-it-contracts-with-accenture-deloitte-others-2025-04-11/](https://www.reuters.com/world/us/pentagon-terminate-51-billion-it-contracts-with-accenture-deloitte-others-2025-04-11/)

**概要：**

五角大楼计划终止与埃森哲、德勤和博思艾伦汉密尔顿等多家大型咨询公司的价值51亿美元的IT合同。这些合同是在国防飞地服务（DES）项目下授予的，旨在将五角大楼的IT基础设施整合并现代化为一个单一的、基于云的网络。据报道，终止合同的原因是战略方向的改变以及DES项目不断变化的需求。

负责监督DES项目的国防信息系统局（DISA）预计将正式宣布合同终止。虽然在提供的上下文中具体原因尚未披露，但该决定标志着五角大楼在实现其IT系统现代化方面的一个重大转变。

此举将影响受影响的公司，这些公司原本计划在未来十年内在DES项目中发挥关键作用。这也引发了人们对五角大楼未来IT现代化战略以及潜在的新合同机会或重组方法以实现该项目最初目标的质疑。终止合同表明对优先事项的重新评估，以及在管理和保护五角大楼IT基础设施方面可能转向新战略。

---

## 49. 弹珠兄弟 - 一家瑞典-意大利弹珠公司

**原文标题**: Pinball Brothers – A Swedish-Italian Pinball Company

**原文链接**: [https://www.pinballbrothers.com/](https://www.pinballbrothers.com/)

无法访问文章链接。

---

## 50. 约束求解器中处理无穷大

**原文标题**: Grappling with Infinity in Constraint Solvers

**原文链接**: [https://tuzz.tech/blog/grappling-with-infinity](https://tuzz.tech/blog/grappling-with-infinity)

在约束求解器中处理无限的挑战：Patuzzo 的 Sentient 语言视角

克里斯·帕图佐的文章探讨了在约束求解器中处理无限的挑战，特别是在他的编程语言 Sentient 的背景下。许多问题，即使是简单的问题，也存在无限多的解决方案和潜在的测试值。然而，像大多数系统一样，Sentient 使用有限的位数来表示整数，即使存在无限解，也会导致程序终止。

作者探讨了将有限表示视为无限数学概念的近似值的想法。增加位表示可以改善近似值，但会重新开始搜索，重新探索已经测试过的区域。他提出了对近似策略的一流支持。

文章探讨了无限不仅出现在整数值中，还出现在数组大小和指数中，从而导致多维搜索空间。作者建议通过外部程序将近似控制委托给程序员，从而实现灵活的策略。

他还考虑利用增量 SAT (IPASIR) 通过重用近似级别之间的知识来提高效率，而不是从头开始。作者思考了操作如何适应不断变化的位表示，以及近似可能如何影响 NP 困难的优化问题。

最后，他探讨了 Sentient 通过近似实现图灵完备性的可能性，特别是通过限制递归深度和循环展开。这与增量 SAT 相结合，可能会极大地提高 Sentient 的问题解决能力。

---

## 51. 我为何用Lisp编程

**原文标题**: Why I Program in Lisp

**原文链接**: [http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html)

乔·马歇尔的博客文章《我为什么用Lisp编程》（2025年4月10日）解释了他对Lisp的偏爱，尽管与其他语言相比，Lisp并不流行。他认为Lisp更容易记忆，因为它统一且通用的剑桥波兰表示法降低了认知负荷。其函数式编程支持，强调替换、易于重构以及值和函数之间的无缝抽象，进一步增强了它的吸引力。

马歇尔重视Lisp的快速原型设计能力，新程序可以与现有程序无缝集成。调试器和安全的内存模型有助于探索，避免灾难性故障。REPL允许立即评估代码片段，从而实现实时程序开发。动态类型提供临时多态性，促进操作各种数据类型的泛型代码。

评论区扩展了文章的观点，特别是对多态性的讨论。一些评论者指出了Lisp的临时多态性与具有类型类（如Haskell或Rust）或泛型类型参数（如C#）的语言相比的局限性，后者允许更精确的类型约束。随后讨论转向与C的比较，作者为Lisp在更广泛地应用数学函数（如阶乘和欧几里得算法）辩护。该帖子还涉及Lisp的审美情趣及其在配置Emacs中的应用，并简要提到了基于Lisp的历史操作系统。

---

## 52. 伦敦地铁实时地图

**原文标题**: Live Map of the London Underground

**原文链接**: [https://www.londonunderground.live/](https://www.londonunderground.live/)

伦敦地铁实时互动地图。

---

## 53. 展示HN：使用AI Gemini 2.5 Pro构建的雅达利导弹指挥官游戏

**原文标题**: Show HN: Atari Missile Command Game Built Using AI Gemini 2.5 Pro

**原文链接**: [https://missile-command-game.centminmod.com/](https://missile-command-game.centminmod.com/)

“Show HN”：基于HTML5 Canvas重制的雅达利经典游戏《导弹指挥官》

这款“Show HN”帖子展示了一个使用现代HTML5 Canvas技术重制的经典雅达利游戏《导弹指挥官》。该游戏保留了与原作相似的核心玩法，并增加了一些新特性。这些特性包括一个游戏内商店，玩家可以在其中购买特殊武器，如声波、巨型炸弹和卫星防御基地，以及导弹加速和爆炸范围扩大等升级。玩家可以通过点击/触摸来发射导弹，并使用特殊武器图标来控制游戏。空格键可以暂停和恢复游戏。

该游戏主要由George Liu开发，并借助了Google Gemini 2.5 Pro和Claude 3.7 Sonnet的AI辅助。该项目托管在Cloudflare Pages上，排行榜由Cloudflare Page Functions/KV驱动。游戏分析则通过Cloudflare AI Gateway与OpenRouter AI结合进行。帖子包含游戏截图，展示了难度选择、游戏过程、带有可购买升级的波间商店，以及关于游戏特性、控制方式和贡献者的信息。同时也提供了该项目的GitHub仓库地址。

---

## 54. GCC 15 的可用性改进

**原文标题**: Usability Improvements in GCC 15

**原文链接**: [https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15](https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15)

好的，我已经阅读了来自所提供URL的文章“GCC 15中的可用性改进”。

以下是摘要：

GCC 15引入了几项可用性改进，旨在使编译器对开发人员更有用且更易于使用。一个主要主题是增强的诊断功能，提供更具信息性和可操作性的错误和警告消息。 具体改进包括：

1.  **改进的范围分析诊断：** 提供与越界访问和数组索引相关的更详细的诊断信息，帮助开发人员精确定位此类错误的确切位置和原因。

2.  **诊断分组：** 将相关的诊断信息分组在一起，使您可以更轻松地了解问题的上下文和根本原因。通过以更有组织的方式呈现级联错误，从而减少噪音。

3.  **更好的拼写建议：** 为拼写错误的关键字和标识符提供更准确和相关的拼写建议，从而减少因简单拼写错误而导致的调试时间。

4.  **改进的 -Wformat 诊断：** 增强了`printf`和相关函数中的格式字符串检查，更有效地捕获潜在的漏洞和不正确的使用。

5.  **标准头文件包含修复建议：** 当缺少需要的头文件时，GCC 15 会建议包含哪个头文件，从而简化开发过程。

6.  **增强的LTO诊断：** 链接时优化 (LTO) 期间改进的诊断功能可以更好地了解性能瓶颈和优化机会。

总而言之，GCC 15 的可用性改进侧重于提供更清晰、更可操作和更分组的错误和警告消息，从而促进更快的调试和改进的代码质量。 这篇文章展示了这些改进将如何在开发人员的日常编码工作流程中使他们受益。

---

## 55. 在危地马拉，蒂卡尔发现彩绘祭坛，为玛雅历史增添新背景

**原文标题**: In Guatemala, painted altar found at Tikal adds new context to Maya history

**原文链接**: [https://phys.org/news/2025-04-guatemala-altar-tikal-context-mysterious.html](https://phys.org/news/2025-04-guatemala-altar-tikal-context-mysterious.html)

在危地马拉蒂卡尔发现的彩绘祭坛揭示了玛雅文明与特奥蒂瓦坎古城之间的新关系。该祭坛可追溯至公元300年代末，其壁画类似于墨西哥中部的“风暴之神”神祇，据信由来自特奥蒂瓦坎的工匠而非玛雅艺术家创作。

研究人员认为，该祭坛证实了一段动荡时期，特奥蒂瓦坎对蒂卡尔施加了重大影响。考古证据表明，最初的贸易关系升级为权力斗争，最终在公元378年左右发生政变，特奥蒂瓦坎用傀儡统治者取代了蒂卡尔的国王。在蒂卡尔附近发现的特奥蒂瓦坎城堡复制品进一步支持了这一占领理论。

在祭坛内部，考古学家发现了一个以坐姿埋葬的儿童和一个带有绿色黑曜石飞镖尖端的成年人，这两种做法和材料在特奥蒂瓦坎很常见，但在蒂卡尔却很少见。随后对祭坛和周围建筑的埋葬表明了对特奥蒂瓦坎存在的复杂且可能消极的看法。

尽管最初遭到破坏，但特奥蒂瓦坎的影响最终促成了蒂卡尔在随后几个世纪的崛起。研究人员注意到对这个时代的怀旧之情，表明玛雅人将其视为一个重要性和影响力高度提升的时期。文章最后强调了特奥蒂瓦坎的行为与其他强大帝国剥削资源丰富地区的历史实例之间的相似之处。

---

## 56. h1元素的默认样式正在更改

**原文标题**: Default styles for h1 elements are changing

**原文链接**: [https://developer.mozilla.org/en-US/blog/h1-element-styles/](https://developer.mozilla.org/en-US/blog/h1-element-styles/)

本文探讨了网页浏览器对 `<h1>` 元素样式即将进行的更改，特别是取消基于其在诸如 `<section>`、`<article>`、`<nav>` 和 `<aside>` 等分段元素中嵌套的隐式样式。

历史上，浏览器会根据 `<h1>` 元素在这些元素中的嵌套深度自动调整其字体大小和边距（例如，`section > h1` 看起来像 `<h2>`）。这种行为源于现已移除的 HTML 大纲算法，目前正在逐步淘汰。

主要要点是：

*   浏览器正在移除根据嵌套自动调整 `<h1>` 元素大小的默认 UA 样式。
*   `<h1>` 现在将始终以相同的样式呈现，无论周围的分段元素如何，除非明确指定样式。
*   Lighthouse 和其他页面审核工具会将 `<h1>` 元素缺少显式字体大小声明的情况标记为不良做法，并显示诸如“H1UserAgentFontSizeInSection”之类的警告。
*   Firefox 和 Chrome 已经开始实施这些更改并发出弃用警告，预计 Safari 也会跟进。

本文建议开发者：

*   避免依赖默认浏览器样式来实现标题层次结构。
*   始终为 `<h1>` 元素显式定义字体大小和边距。
*   考虑更新 CSS 重置以反映此更改。
*   使用 Lighthouse 和浏览器 DevTools 来识别已弃用的用法。

本质上，Web 开发者需要更加明确地设置 `<h1>` 元素的样式，以确保一致的呈现效果并避免审核工具发出警告。

---

## 57. 没有加菲猫的加菲猫

**原文标题**: Garfield Minus Garfield

**原文链接**: [https://garfieldminusgarfield.net](https://garfieldminusgarfield.net)

《加菲猫减去加菲猫》描述，以及一些包含Facebook和Twitter链接的日期列表。这表明存在一个名为《加菲猫减去加菲猫》的项目，并在Facebook和Twitter上拥有社交媒体存在。"一月 27"（1月27日）和"十一月 03"（11月3日）可能代表在该平台上分享或更新内容的日期。

本质上，这段文字是一段元数据片段，暗示着一个名为《加菲猫减去加菲猫》的项目利用社交媒体进行推广或内容分享。在没有更多背景信息的情况下，很难知道该项目的确切性质。

---

## 58. 谷歌员工...前谷歌员工

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

谷歌Chrome团队成员Adam意外遭到裁员，令他感到震惊、愤怒和悲伤。这次解雇被描述为并非基于能力，且令他的经理们也感到意外。解雇发生在他参加Chrome团队线下会议期间，非常突然。他立即被切断了与谷歌资源的连接，如日历、文档和代码。

Adam对失去众多他积极参与的职责和机会感到沮丧，包括Google I/O视频、舞台演讲、展位管理以及对开发者主题演讲的贡献。他还惋惜失去了CSS工作组成员资格、开发者办公时间以及对代码的访问权限。此外，他担心多年来建立的关系会因此瓦解。

他形容自己感到被背后捅刀、不被赏识，觉得自己像大型公司中一个可有可无的零件。他难以入睡，并对这种情况感到羞愧和愤怒。他提供了联系方式，方便那些想通过Bluesky或电子邮件（adam.is@nerdy.dev）联系他的人，但他承认由于情况过于复杂，可能回复较慢。

---

## 59. 2025年人工智能指数报告

**原文标题**: 2025 AI Index Report

**原文链接**: [https://hai.stanford.edu/ai-index/2025-ai-index-report](https://hai.stanford.edu/ai-index/2025-ai-index-report)

无法访问文章链接。

---

## 60. 月球背面土壤表明其比朝向地球一面更干燥

**原文标题**: Soil from the moon's far side suggests drier conditions than side facing Earth

**原文链接**: [https://apnews.com/article/moon-far-side-near-side-water-18081418600ea93bac69ac6af86a761b](https://apnews.com/article/moon-far-side-near-side-water-18081418600ea93bac69ac6af86a761b)

美联社新闻：“月球背面土壤表明比面向地球一侧更干燥”一文讨论了新的研究，该研究表明月球背面比近地面显著干燥。这一结论基于对嫦娥五号任务从近地面带回的土壤样本的分析，以及将其与来自月球背面嫦娥五号着陆点光谱数据的比较。

科学家发现，远侧土壤含水量较低，特别是羟基 (OH)，这是一种含有一个氢原子和一个氧原子的分子，被认为是水冰的前体。对此差异的主要理论是，数十亿年前的火山喷发在近地面沉积了富含水的物质，而远地面经历的火山活动较少，因此保留的水也较少。或者，可能是由于磁场环境的差异，太阳风和其他空间天气效应对远侧产生了更明显的干燥效应。

了解月球上水的分布对于未来的月球任务至关重要，因为水冰可用作饮用水、火箭燃料和氧气的资源。该发现强调了进一步探索月球背面以更全面地了解月球水分布及其形成的重要性。这项研究为月球的地质历史和塑造其表面的过程提供了宝贵的见解。

---

## 61. 我们的全新AI网站构建器

**原文标题**: Our New AI Website Builder

**原文链接**: [https://wordpress.com/blog/2025/04/09/ai-website-builder/](https://wordpress.com/blog/2025/04/09/ai-website-builder/)

WordPress.com推出全新AI网站构建器，简化网站创建流程。用户只需描述所需网站，无需手动设计和创建内容，AI即可立即生成包含文本、布局和图片的完整WordPress站点。

该构建器旨在帮助企业家、小型企业主、自由职业者、博主和开发者快速轻松地建立专业的在线形象。虽然目前还不适用于复杂的电子商务或需要大量集成的网站，但它可以在几分钟内创建功能齐全且视觉上吸引人的网站。

该过程包括描述所需网站，登录或创建WordPress.com账户，并让AI构建站点。用户随后可以通过手动编辑或在聊天框中使用提示进行更改。WordPress.com托管计划提供安全的在线空间，第一年免费域名，并可以立即启动网站。

文章强调提供具体和详细的提示以获得最佳结果的重要性，并强调AI构建器仅适用于新的WordPress.com站点。用户最初获得30个免费提示，而拥有托管计划则可获得无限提示。AI生成的站点可以使用标准的WordPress功能进一步自定义。文章最后鼓励读者使用AI网站构建器，为他们的业务、想法或个人项目快速建立在线形象。

---

## 62. 优势即是弱点

**原文标题**: Strengths Are Your Weaknesses

**原文链接**: [https://terriblesoftware.org/2025/03/31/your-strengths-are-your-weaknesses/](https://terriblesoftware.org/2025/03/31/your-strengths-are-your-weaknesses/)

本文认为，个人的优势和劣势往往是一体两面，作者通过自己作为工程师的个人经历阐述了这一概念。作者的编码速度起初备受赞扬，但却导致忽略了关键细节并引发了生产问题。

作者认为这是一种普遍现象，即被赞扬的品质也可能成为重大问题的根源。为了解决这种二元性，作者提出了三种有效的管理策略：

1.  **在1对1会议中承认二元性：** 将优势和劣势重新定义为同一特质的相互关联的方面，以培养自我意识并减少自我批评。
2.  **提供明确的背景指导：** 明确界定特定倾向何时有利或有害，从而使个人能够做出明智的决定。
3.  **利用团队中的张力：** 鼓励具有不同方法的人员进行协作，以培养更全面的视角并改善结果。

本文强调了培养能够根据环境调整自身倾向的、具有自我意识的工程师的重要性。目标不是消除个体差异或“修复”工程师，而是帮助他们理解并有效利用自己的优势，同时减轻潜在的劣势。最终，认识到优势和劣势之间的相互关联性能够促进更好的管理并提升同理心。

---

## 63. R语言大全

**原文标题**: Big Book of R

**原文链接**: [https://www.bigbookofr.com/](https://www.bigbookofr.com/)

《R语言大全》收录了400多本免费且经济实惠的R编程书籍。作者Oscar希望它能成为用户唯一需要的R语言资源书签。该系列始于2020年8月，当时约有100本书，并且 благодаря contributions不断壮大。

用户可以使用菜单或搜索图标搜索此系列。作者欢迎捐款以支持该项目，并鼓励通过GitHub或Google表格贡献付费和免费书籍。

Oscar感谢Fathom Data将该网站转换为Quarto。本网站采用Creative Commons Attribution-NonCommercial-NoDerivs 3.0许可协议。 实时、注重隐私的网站统计数据可供查看。

Oscar邀请读者在Mastodon或LinkedIn上联系，并订阅新闻通讯，以获取有关他的数据相关项目和这本书的更新。

---

## 64. .localhost 域名

**原文标题**: .localhost Domains

**原文链接**: [https://inclouds.space/localhost-domains](https://inclouds.space/localhost-domains)

查尔斯·张伯伦介绍了一种通过自定义`.localhost`域名而非`localhost:端口`组合来访问本地Web应用的方法，从而简化开发并使其更易于记忆。 该系统包含三个步骤：

1.  **Launchd守护进程：** 每个应用程序都作为launchd守护进程运行，监听唯一的端口。
2.  **/etc/hosts配置：** 编辑`/etc/hosts`文件，将每个自定义`.localhost`域名的流量重定向到`127.0.0.1`（localhost）。例如，`127.0.0.1 inclouds.localhost`。
3.  **Caddy反向代理：** 配置Web服务器Caddy，将来自自定义域名上`127.0.0.1`的流量反向代理到应用程序运行的相应端口。 此配置在Caddyfile中完成，指定域名、localhost端口以及TLS和编码。

作者表示希望进一步简化该过程，设想使用单个命令来安装和卸载应用程序以及相应的`.localhost`域名配置。 他还提到了来自Cristóbal的使用dnsmasq来改进该过程的更新。

---

## 65. PS3舔了许多饼干

**原文标题**: The PS3 Licked the Many Cookie

**原文链接**: [https://darkcephas.github.io/ps3_failed/ps3_failed.html](https://darkcephas.github.io/ps3_failed/ps3_failed.html)

本文从游戏开发者的角度分析了PS3未能实现多核处理承诺的原因。作者认为，PS3的主要问题在于其过度异构，导致难以有效利用其Cell处理器的SPE（协同处理器单元）。

虽然SPE最初看起来体现了多核架构的原则，但实际上开发者只能访问有限数量的可用的SPE，使其核心数量仅比Xbox 360略高。此外，SPE和PS3的GPU在计算能力上都比较弱，需要开发者协调它们之间复杂的同步才能实现有竞争力的性能。GPU具有独立的顶点和像素着色单元，并且像素着色不像Xbox 360的统一架构那样具有常量。

作者强调了SPE的本地内存限制（256KB，实际上在堆栈和程序之后为128KB）带来的挑战。这种限制迫使开发者创建专门的、对SPE友好的代码，而不是轻易移植通用代码。诸如C++虚函数和动态内存分配之类的概念变得成问题，进一步突出了该平台的复杂性。

最终，PS3成为了多核架构失败的代名词。作者认为，更同质化、高性能的多核设计，比如最初的多个Cell处理器设计，本可以释放该游戏机的真正潜力。PS3尝试采用异构方法最终导致了“舔过的饼干”——一个妥协且最终令人失望的多核愿景的实现。

---

## 66. PyReason：面向带注释、实值、图和时间序列数据的可解释推理

**原文标题**: PyReason: Explainable inference for annotated, real valued, graph based and tem

**原文链接**: [https://github.com/lab-v2/pyreason](https://github.com/lab-v2/pyreason)

PyReason 是一款基于 Python 的图形推理工具，旨在利用逻辑规则和事实对图结构进行推理。它支持带注释的、实值的、基于图的以及时序逻辑，从而实现可解释的推理。该软件附带包括研究论文、视频、网站、PyReason Gym 以及 ReadTheDocs 上提供的全面文档在内的配套资源。

PyReason 可以通过 `pip install pyreason` 安装，目前支持 Python 3.7 到 3.10 版本，但多核并行支持仅限于 3.9 和 3.10 版本。

该软件以 BSD-2-Clause 许可授权。尽管 PyReason™ 和 PyReason Design Logo ™ 是亚利桑那州立大学的商标，但用户可以结合软件使用 "PyReason™" 商标，教育机构可以出于非商业目的使用 PyReason Design Logo ™。

创建者鼓励在工作中使用 PyReason 的用户引用提供的 Bibtex 条目。如有疑问，请通过提供的电子邮件地址联系 Dyuman Aditya、Kaustuv Mukherji 或 Paulo Shakarian。

---

## 67. Clojure：无需ClojureScript的实时协作Web应用

**原文标题**: Clojure: Realtime collaborative web apps without ClojureScript

**原文链接**: [https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html](https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html)

本文介绍了 Datastar，一个轻量级的超媒体框架，它可以使用 Clojure 创建实时协作的 Web 应用程序，而无需依赖 ClojureScript 或用户编写的 JavaScript。作者展示了一个用 Datastar 构建的多人“生命游戏”应用程序，重点介绍了它使用 Server-Sent Events (SSE) 每 200 毫秒将整个 `<main>` 元素从服务器流式传输到客户端的方法。

这种方法的主要优点包括简单性、性能和网络效率。 Datastar 利用快速的 morph 算法来高效地更新客户端 DOM。 通过 SSE 进行 Brotli 压缩实现了高压缩率，可能优于细粒度的更新，并简化了视图/会话维护。

作者认为，由于 SSE 本身与 HTTP 功能（如压缩、多路复用和自动重新连接）兼容，并且避免了与 WebSockets 相关的操作挑战，因此 SSE 在实时通信方面优于 WebSockets。

本文强调了 Datastar 的 "view = f(state)" 模型，将视图保留在客户端，将状态函数保留在服务器上。Hyperlith 是一个构建在 Datastar 之上的实验性迷你框架，可处理诸如 SSE、压缩和事件管理之类的复杂问题。本文展示了由于服务器端渲染逻辑，如何将单用户应用程序轻松转换为多人应用程序，而无需进行重大代码更改。Datastar 是后端无关的，它承诺提供一个比 Phoenix LiveView 等框架更简单有效的替代方案。

---

## 68. 揭秘Shebang：内核探险

**原文标题**: Demystifying the (Shebang): Kernel Adventures

**原文链接**: [https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/](https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/)

本文深入探讨Linux内核如何处理可执行文件，特别关注shebang（`#!`）在脚本执行中的作用。作者解释说，shebang不仅仅是shell的提示，而是由内核本身主动处理的。

本文使用`strace`和内核代码探索来演示`execve`系统调用如何导致内核中的`do_execveat_common`、`bprm_execve`和`search_binary_handler`等函数。`search_binary_handler`通过读取文件的前256个字节并将其与注册格式（ELF、FLAT、SCRIPT、MISC）进行比较来识别文件的格式。`binfmt_script.c`模块专门处理带有shebang的脚本，解析解释器路径和参数，然后执行解释器。

作者还探讨了`binfmt_misc.c`，这是一个内核特性，用于通过将非本地二进制文件（如Java JAR文件）与特定解释器相关联来执行它们。本文演示了当存在shebang时，内核如何有效地将进程映像替换为解释器的进程映像。

最后，本文阐明，虽然shebang是指定解释器的标准方法，但shell具有一种回退机制，可以通过显式调用`/bin/sh`来执行没有shebang的脚本。它还涉及权限检查，展示了内核的`do_open_execat`函数如何使用`path_noexec`来验证执行权限，然后在允许执行之前，如果权限被拒绝，则返回EACCES。

---

## 69. 仲粒子：量子粒子的第三种王国

**原文标题**: 'Paraparticles' Would Be a Third Kingdom of Quantum Particle

**原文链接**: [https://www.quantamagazine.org/paraparticles-would-be-a-third-kingdom-of-quantum-particle-20250411/](https://www.quantamagazine.org/paraparticles-would-be-a-third-kingdom-of-quantum-particle-20250411/)

本文探讨了第三类量子粒子的潜在存在，这种粒子被称为“准粒子”，它与已知的费米子（物质粒子）和玻色子（力载粒子）类别不同。物理学家王志远和卡登·哈扎德提出，准粒子可能存在隐藏的量子态，当粒子交换位置时，这些量子态会发生变化。与不能占据同一空间的费米子和可以占据同一空间的玻色子不同，准粒子允许有限数量的粒子处于同一状态。

这个概念挑战了数十年历史的DHR理论，该理论认为，在局域性和三维空间等特定假设下，只有玻色子和费米子才有可能存在。王和哈扎德的模型认为，通过放宽对不可区分性的更严格定义，准粒子是有可能存在的。他们认为，交换准粒子不会影响单个观察者的测量结果，但两个观察者比较笔记可以分辨出是否发生了交换。

马库斯·穆勒的团队也通过考虑处于叠加量子态的观察者来探索这一想法。他们的结果表明，在对不可区分性的严格假设下，准粒子是不可能存在的。然而，穆勒承认王和哈扎德的模型可能是有效的。

如果准粒子存在，它们很可能是在量子材料中出现的准粒子，有可能解释以前难以理解的奇异相。实验物理学家布莱斯·加德威乐观地认为，在不久的将来，可以使用里德堡原子在实验室中实现准粒子。虽然这仍然是理论上的，但准粒子的发现可能会导致新的物质状态，并彻底改变我们对量子世界的理解。

---

## 70. 我们最好的客户现在是机器人

**原文标题**: Our Best Customers Are Now Robots

**原文链接**: [https://fly.io/blog/fuckin-robots/](https://fly.io/blog/fuckin-robots/)

库尔特·麦基的文章《我们最好的客户现在是机器人》探讨了Fly.io令人惊讶的转变，即其主要增长驱动力并非人类开发者，而是服务于人工智能驱动的应用程序（“机器人”）。Fly.io是一家以开发者为中心的云平台，以其卓越的开发者体验（DX）而闻名，特别是其CLI优先的方法，但它发现其平台出乎意料地对LLM（大型语言模型）具有吸引力。

麦基将此归因于几个平台特性：启动和停止Fly Machines（运行Docker容器的硬件隔离虚拟机）的速度和成本效益、用于迭代、有状态代码构建的持久存储，以及平台的网络功能，特别是其对MCP（LLM使用的协议）的处理。机器人很欣赏在Fly Machines中快速创建、修改和运行代码的能力。

他承认Fly.io并非有意瞄准机器人；该平台的特性只是恰好与基于LLM的应用程序的需求相吻合。他强调，机器人使用平台的方式与人类不同，它们不是运行现有应用程序，而是构建新的应用程序。麦基认为，下一个挑战是为机器人优化平台，即创建机器人体验（RX），探索诸如更简单的MCP集成和安全密钥管理（令牌化的OAuth令牌）等功能，以便授予机器人受控的API访问权限。尽管Fly.io仍然专注于其人类用户，并不断改进其托管Postgres（MPG）和DX，但机器人作为重要用户群的出现，迫使人们转变思维，朝着构建出色的RX方向发展。

---

## 71. 在小溪里玩耍

**原文标题**: Playing in the Creek

**原文链接**: [https://www.hgreer.com/PlayingInTheCreek/](https://www.hgreer.com/PlayingInTheCreek/)

文章《在小溪中玩耍》探讨了在特定领域获得精通后，失去最初无拘无束的玩耍和探索的喜悦和自由，这种苦乐参半的体验。作者用童年时筑坝小溪的轶事作比喻：发现更有效的方法（用铲子铲平河岸）剥夺了作者用石头和树叶精心筑坝的复杂而有趣的乐趣。

这种模式在生活中不断重复。作者描述了搭建K'Nex弹射器、制作烟花炸弹以及制作弓箭等场景，在这些场景中，新获得的知识或技能限制了无忧无虑的实验。作者甚至将此与投资银行的工作邀请联系起来，意识到实现收入最大化的“目标”实际上消除了为实现该目标而奋斗的游戏。

关键的收获是，“胜利的代价”可能是一个更小的游乐场。作者承认，面对超出自己能力范围的挑战才能继续玩耍。然而，当全力以赴的后果在道德上变得令人质疑（比如利用市议会影响力来操纵海滩）或具有潜在破坏性（比如人工智能开发中隐喻的“烟花炸弹”）时，限制就变得必要。

文章最后以对人工智能发展的谨慎观点结尾。作者暗示，即使在竞争激烈的竞赛中，鲁莽地推动人工智能的界限也可能导致不良后果。他们希望像Anthropic这样的公司在追求人工智能进步的过程中，能够考虑到“鸟蛤”——那些可能被忽视的后果和较小的担忧。

---

## 72. 疯子们做到了：世界最快电动汽车倒立行驶并击败了一辆F1赛车

**原文标题**: The madlads did it: world’s fastest EV drives upside-down & beat an F1 car, too

**原文链接**: [https://electrek.co/2025/04/11/the-crazy-bastards-did-it-they-drove-the-worlds-quickest-ev-upside-down/](https://electrek.co/2025/04/11/the-crazy-bastards-did-it-they-drove-the-worlds-quickest-ev-upside-down/)

麦克默特里 Speirling 电动赛车以其破纪录的性能而闻名，功率达 1000 马力，现已取得两项新的里程碑：打破了 Top Gear 测试赛道的记录，并成为第一辆倒置行驶的汽车。

Speirling 使用风扇在车下产生真空，从而产生巨大的下压力（在 1000 公斤的汽车上产生 2000 公斤），而不会增加质量，从而实现更大的抓地力和更快的速度。这种“风扇车”概念虽然以前在赛车运动中被禁止，但允许 Speirling 即使在低速下也能产生下压力，这与传统的空气动力学元件不同。

在 Top Gear 赛道上，Speirling 实现了 0:55.9 的单圈时间，击败了 2004 年雷诺 F1 赛车创下的 59 秒的先前记录，并且比最快的电动汽车（福特 SuperVan）快了近十秒。

此外，Speirling 通过倒置行驶十秒钟，并在整个过程中保持控制，展示了其极端的下压力能力。虽然不是一项高速特技，但它是对汽车下压力技术潜力的概念验证。麦克默特里旨在进一步探索这种可能性，未来可能会倒置行驶更长的距离。

---

## 73. 展示 HN：Rust 速度的 Python

**原文标题**: Show HN: Python at the Speed of Rust

**原文链接**: [https://blog.fxn.ai/python-at-the-speed-of-rust/](https://blog.fxn.ai/python-at-the-speed-of-rust/)

本文介绍了“Function”项目，该项目旨在将Python代码编译成原生代码，以实现接近Rust水平的性能和跨平台兼容性。其核心思想是追踪Python函数的执行，从而创建一个中间表示（IR）图，该图捕获所有操作。这种追踪是通过CPython的帧评估API实现的，动态捕获指令输入、操作和输出。

随后，该过程通过在诸如C语言等语言中生成Python操作的相应实现，将IR图降级为原生代码。Python函数上的类型注释和操作的原生实现允许类型在IR图中传播。然后，生成的原生代码可以为各种平台进行交叉编译。

本文使用融合乘加（FMA）函数作为一个例子。它演示了如何使用Function框架编译这个函数，包括安装、使用`@compile`装饰器进行装饰，以及通过命令行进行编译。

一项将编译后的Python代码与等效的Rust实现进行比较的基准测试表明，编译后的Python代码仅慢了一个常数因子。虽然仍然是一个概念验证，但该编译器已被设计合作伙伴在生产环境中用于诸如单目深度估计和实时姿态检测等应用，未来的目标包括设备上的LLM推理。该项目鼓励通过Discord服务器进行社区参与，并提供一个GitHub存储库，用于检查生成的代码和重现基准测试。

---

## 74. Awe – Algol W 的现代编译器

**原文标题**: Awe – Modern compiler for Algol W

**原文链接**: [https://github.com/glynawe/awe](https://github.com/glynawe/awe)

Awe：ALGOL W编程语言的现代编译器，Algol 60的后继者。它旨在兼容为OS/360 ALGOL W编译器编写的代码，并遵循《ALGOL W语言描述》（1972年6月）。该编译器提供该语言的完整实现。

编译Awe需要类Unix操作系统、GCC、Python3、OCaml和Boehm GC。可通过`awe(1)`和`awe.mk(7)`访问的Awe手册提供了更多详细信息。安装说明可在INSTALL文件中找到。

该项目感谢Hendrick Boom、Tony Marsland、Carey Bloodworth、John Boutland和Nicolas Brouard的建议、鼓励和测试。它还感谢Algol W语言描述的作者，感谢他们清晰明确的规范。作者感谢已故的Frank Key，并建议读者考虑购买他的书籍。

---

## 75. 持有者令牌指南：JWT与不透明令牌

**原文标题**: A Guide to Bearer Tokens: JWT vs. Opaque Tokens

**原文链接**: [https://www.permit.io/blog/a-guide-to-bearer-tokens-jwt-vs-opaque-tokens](https://www.permit.io/blog/a-guide-to-bearer-tokens-jwt-vs-opaque-tokens)

本文全面介绍了持有者令牌，重点关注JSON Web Tokens (JWTs) 和不透明令牌之间的差异，这对于保护API和管理用户会话至关重要。文章解释说，持有者令牌充当数字密钥，授予对受保护资源的访问权限，而无需重新身份验证。

JWTs是自包含的，包括用户和访问数据，可实现快速的无状态验证，非常适合API和微服务。但是，它们难以撤销，如果未加密，可能会暴露数据。不透明令牌是简单的引用字符串，需要服务器端验证，提供更好的安全性和撤销控制，但会增加开销并降低可扩展性。

文章详细介绍了每种令牌类型的结构、优点和缺点。 JWTs因其无状态性、速度和互操作性而受到青睐，但在撤销和数据暴露方面提出了挑战。不透明令牌在安全性、实时撤销和隐私方面表现出色，但需要集中验证，从而影响性能。

文章还探讨了何时使用每种令牌类型，建议对于需要撤销和敏感数据保护的系统使用不透明令牌，而对于速度至关重要的微服务使用JWTs。最后，它建议采用混合方法，例如使用JWTs作为访问令牌，使用不透明令牌作为刷新令牌。文章强调，无论令牌类型如何，使用专用策略引擎进行适当的授权至关重要，警告不要仅仅依靠令牌声明来进行访问控制，并提倡使用策略作为代码进行外部授权。

---

## 76. 研究人员发现塑料释放危险碎片的原因

**原文标题**: Researchers discover why plastic sheds dangerous fragments

**原文链接**: [https://www.sciencedaily.com/releases/2025/04/250407172923.htm](https://www.sciencedaily.com/releases/2025/04/250407172923.htm)

无法访问文章链接。

---

## 77. 金融科技创始人被控欺诈；人工智能应用被发现实为菲律宾人在操作

**原文标题**: Fintech founder charged with fraud; AI app found to be humans in the Philippines

**原文链接**: [https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/](https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/)

AI购物应用Nate创始人兼前CEO Albert Saniger 被指控欺诈投资者。美国司法部（DOJ）指控Saniger虚假声称Nate的“通用”结账体验由人工智能驱动，只需一键即可从任何电商网站完成购买，无需人工干预，以此筹集了超过5000万美元。

事实上，Nate严重依赖菲律宾数百名人工承包商手动完成购买，尽管该公司已收购人工智能技术并聘请了数据科学家。美国司法部声称该应用程序的实际自动化率实际上为 0%。此前，《The Information》杂志曾在 2022 年对此行为进行过调查。

美国司法部的起诉书指出，Nate资金耗尽，被迫于 2023 年 1 月出售其资产，导致投资者“几乎全部”损失。 Saniger现在是风险投资公司Buttercore Partners的管理合伙人。

Nate加入了一份日益增长的初创公司名单，这些公司被指控夸大其人工智能能力，其中包括一家“人工智能”得来速软件公司和法律科技独角兽EvenUp，这两家公司都被发现严重依赖人工劳动。

---

## 78. 适用于经典 Macintosh OS 7/8/9 的 Mbed-TLS 移植版

**原文标题**: A port of Mbed-TLS for the Classic Macintosh OS 7/8/9

**原文链接**: [https://github.com/bbenchoff/MacSSL](https://github.com/bbenchoff/MacSSL)

本文档详细介绍了“MacSSL”，它是Mbed-TLS库到Classic Macintosh OS 7/8/9的移植版本，专门针对Metrowerks CodeWarrior Pro 4编译器。该项目旨在为这些旧系统上的应用程序启用HTTPS功能，特别是针对一个“复古数码相机”Instagram克隆应用。

该仓库包含CodeWarrior项目、Mbed-TLS文件（项目所需的一个子集，以及原始仓库的完整副本）和一个示例应用程序。此应用程序执行对指定API端点的GET请求并显示结果，以及调试信息。

该移植基于polarssl的一个版本，它是Mbed-TLS 2.29.9的一个分支。它支持TLS 1.1，但仅限于一组密码套件（AES-128和AES-256 CBC with SHA），SECP256R1椭圆曲线和特定的签名算法（SHA-256/384/1 + RSA）。

主要挑战包括将代码适配到C89/C90标准（变量声明、缺少可变参数宏和方法重载）、创建兼容的64位整数类型、处理包含路径限制以及为安全随机性生成足够的熵。自定义熵源基于系统时钟、鼠标移动、内存状态、硬件时序和网络统计信息。ISRG Root X1和Let's Encrypt R11证书用于证书处理。由于Toolbox的限制，调试信息会输出到应用程序的文本框和一个单独的文件中。由于熵收集的限制，该实现被标记为可能不安全。

---

## 79. 特朗普政府推翻社保局员工意见，将移民列为死亡。

**原文标题**: Trump administration overrode Social Security staff to list immigrants as dead

**原文链接**: [https://www.washingtonpost.com/politics/2025/04/12/trump-immigrants-dead-social-security/](https://www.washingtonpost.com/politics/2025/04/12/trump-immigrants-dead-social-security/)

无法访问文章链接。

---

## 80. 使用Django的地图⁽³⁾：GeoDjango、Pillow和GPS

**原文标题**: Maps with Django⁽³⁾: GeoDjango, Pillow and GPS

**原文链接**: [https://www.paulox.net/2025/04/11/maps-with-django-part-3-geodjango-pillow-and-gps/](https://www.paulox.net/2025/04/11/maps-with-django-part-3-geodjango-pillow-and-gps/)

本文是关于使用 Django 创建地图的系列文章的第三部分，重点介绍集成图像和 GPS 数据。 它指导读者使用 Django、GeoDjango、SpatiaLite、Leaflet 和 Pillow 构建一个 Web 地图。目标是创建一个地图，可以显示标记、从图像中提取 GPS 信息，并将图像与特定位置相关联。

该过程首先设置一个包含 GeoDjango 和 SpatiaLite 的 Django 项目，然后创建一个“markers”应用程序来管理地图标记。 本文演示了如何定义一个包含位置和名称字段的 Marker 模型，并使用 Django 管理界面来添加带有地图小部件的标记。 它涵盖了生成数据库迁移和创建超级用户以访问管理界面。

接下来，本文详细介绍了使用 Leaflet 集成 Web 地图的步骤，包括在 HTML 模板中链接 JavaScript 和 CSS 模块。 它展示了如何创建一个自定义 JavaScript 文件来初始化 OpenStreetMap 图层并将标记显示为 GeoJSON。 本文提供了用于创建 MapView 类、定义 URL 模式以及在 Web 浏览器中测试填充地图的代码片段。 最后，它解释了使用 Pillow 进行图像处理以及从图像中提取 GPS 信息以自动填充地图标记。

---

## 81. 《闪灵》诡异照片背后的45年谜团据信已解开

**原文标题**: 45-year mystery behind eerie photo from The Shining is believed to be solved

**原文链接**: [https://www.cbc.ca/lite/story/1.7507349](https://www.cbc.ca/lite/story/1.7507349)

《闪灵》诡异照片谜团终被破解，疑为45年后揭晓

---

## 82. 《“100个Go语言常见错误”及其规避方法背后的故事》

**原文标题**: The Story Behind “100 Go Mistakes and How to Avoid Them”

**原文链接**: [https://www.thecoder.cafe/p/100-go-mistakes](https://www.thecoder.cafe/p/100-go-mistakes)

泰瓦·哈尔萨尼讲述了他从2018年开始创作《围棋百错及如何避免》一书的历程。最初使用Scala和Akka，他发现了Go语言，并迅速意识到它的潜力。在获得一份Go语言工作后，他写了一篇博客文章《我在Go项目中见过的最常见的十大错误》，出乎意料地走红，这启发他将这个概念扩展成一本书。

2020年11月，在收集了100个错误后，他联系了Manning出版社，这家出版社以其严格的审查流程而闻名。他强调了与出版社合作的价值，因为他们有广泛的审查系统和更高的知名度，尽管版税相对较低（10%）。

写作过程包括完善最低合格读者 (MQR) 档案，与一位开发编辑 (DE) 密切合作，这位编辑极大地改进了他的写作风格，并经历了多轮外部审查。哈尔萨尼的目标是创作出最好的Go语言书籍，他致力于解决反馈并改进内容。他从Bill Kennedy那里获得了宝贵的建议，甚至处理了细微的评论。

他提到了一段与他的技术开发编辑 (TDE) 之间的小插曲，这位编辑没有达到最低Go语言知识水平，阻碍了他们提供有用的技术指导。尽管如此，他继续通过MEAP（Manning Early Access Program）工作，并纳入了评论者的反馈。

---

## 83. 泰坦尼克号数字扫描揭示沉没前新细节

**原文标题**: Titanic digital scan reveals new details of ship's final hours

**原文链接**: [https://www.bbc.com/news/articles/cwy6gjwd0g6o](https://www.bbc.com/news/articles/cwy6gjwd0g6o)

泰坦尼克号残骸全面数字扫描揭示了关于该船最后时刻前所未有的细节，为这场灾难提供了新的见解。这个3D复制品由水下机器人拍摄的70多万张图像创建，揭示了该船解体的剧烈程度以及冰山造成的破坏。

主要发现包括证实了目击者的描述，即工程师们工作到最后一刻以维持电力，这由凹陷的锅炉和船尾上打开的蒸汽阀门所表明。这突显了约瑟夫·贝尔等工程师的英雄主义，他们保持照明以帮助救生艇的部署。

扫描还显示了一个破碎的舷窗，证实了幸存者关于冰在碰撞过程中进入船舱的故事。此外，基于泰坦尼克号蓝图的计算机模拟表明，该船的沉没是由一系列分布在六个舱室中的、A4纸大小的小穿孔造成的。尽管该船的设计能够承受四个舱室的洪水，但这些小孔最终导致了洪水和沉没。

该数字扫描被描述为用于分析的“犯罪现场”，它提供的残骸全貌比以往潜水器探索所能提供的更为完整。虽然需要数年时间才能完全分析这个3D复制品，但它仍在不断提供关于泰坦尼克号悲剧沉没的新线索和细节。

---

## 84. 一台2000美元“美国制造”的手机是如何生产的

**原文标题**: How a $2k 'Made in the USA' Phone Is Manufactured

**原文链接**: [https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/](https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/)

本文探讨了在美国制造智能手机的挑战与现实，重点关注Purism的Liberty Phone，这款售价2000美元的“美国制造”产品，是其中国制造的Librem 5（800美元）的替代品。创始人Todd Weaver解释了Purism致力于在美国制造的原因，包括安全性、透明度以及对供应链的控制。

Liberty Phone在Purism位于加利福尼亚州的工厂生产，通过焊接元件将裸电路板制成成品。这符合美国联邦贸易委员会对“美国制造”的定义，而不是仅仅“组装”。虽然Purism的目标是尽可能从美国或西方分销商/制造商处采购元件，但由于供货和成本原因，原材料和特定元件（如某些晶体）仍然经常来自美国境外。

Weaver承认，复制中国制造业的效率和专业知识是一项艰巨的任务，需要大量的投资和时间。虽然先进的芯片*可以*在美国制造，但将它们与所有其他元件整合到手机中的完整流程目前集中在中国。尽管存在这些障碍，Purism对其采购保持透明，公布原理图、硬件物料清单和源代码。本文强调了美国制造业的复杂性以及成本、性能和原产地之间的权衡。

---

## 85. 你的“和谐”团队为何失败

**原文标题**: Why Your 'Harmonious' Team Is Failing

**原文链接**: [https://terriblesoftware.org/2025/03/12/why-your-harmonious-team-is-actually-failing/](https://terriblesoftware.org/2025/03/12/why-your-harmonious-team-is-actually-failing/)

本文认为，表面上“和谐”的团队，往往因回避冲突而走向失败。它挑战了一种误解，即心理安全等同于没有分歧。正如Amy Edmondson所定义的，真正的心理安全是营造一种环境，让个人能够放心地提出顾虑、挑战观点和承认错误，而不必担心受到惩罚或羞辱。

作者强调了富有成效的分歧带来的好处，包括及早发现问题、充分辩论观点、专注于解决问题而不是人身攻击，以及将错误视为学习机会。相反，回避冲突的“友善”团队，往往由于缺乏诚实的沟通和批判性思维而产生平庸的工作。分歧被压制，导致决策失误和问题悬而未决。

文章为工程经理们提供了实用技巧，以培养鼓励建设性冲突的心理安全环境：展现脆弱性、为辩论设定基本规则（关注观点，而不是人），并赞扬那些提出挑战性问题的人。通过公开且尊重地处理分歧，团队可以防止分歧升级为怨恨和消极攻击行为，最终带来更好的代码、更完善的想法以及更强大、更具韧性的团队。

---

## 86. 废弃核电站变身世界一流声学实验室

**原文标题**: An unused nuclear power plant became home to a world-class acoustics lab

**原文链接**: [https://www.theverge.com/tech/644385/nuclear-power-plant-acoustics-lab](https://www.theverge.com/tech/644385/nuclear-power-plant-acoustics-lab)

艾莉森·约翰逊的文章探讨了华盛顿州萨特索普商业园的一座废弃核电站如何被改造成世界级的声学实验室——NWAA实验室，由罗恩·索罗和邦妮·索罗运营。由于预算问题和热情消退，WNP-3核电站从未完工，最终成为萨特索普商业园的一部分。

前NASA科学家罗恩·索罗看到了这座巨大混凝土结构的潜力，特别是辅助反应堆大楼及其厚实的墙壁，可以用来创造一个可控的声音环境。该地点偏远以及建筑固有的温度稳定性为声学测试提供了理想的条件。NWAA实验室测量各种产品的隔音效果和噪声水平，并遵守严格的ANSI和ISO标准。

该实验室设有混响室，用于测试声音传输损耗，其中包括一个独特的“室中室”，被称为世界上最安静的非消音室。他们还在涡轮机大楼里利用自由场扬声器测试装置，应对漏水屋顶等挑战。索罗强调了运营该实验室所需的足智多谋，身兼木匠、水管工等多种角色。该设施的独特特性，例如无法轻易修改反应堆外壳，既带来了挑战也带来了好处，使实验室能够在非常规的空间中蓬勃发展。

---

## 87. 我们选择了Tauri而非Electron来开发对性能要求严苛的桌面应用

**原文标题**: We Chose Tauri over Electron for Our Performance-Critical Desktop App

**原文链接**: [https://gethopp.app/blog/tauri-vs-electron](https://gethopp.app/blog/tauri-vs-electron)

科斯塔·阿莱克斯格卢的文章比较了Tauri和Electron，这两种流行的跨平台桌面应用程序构建框架，重点介绍了它们的差异、权衡以及Hopp团队为何选择Tauri来构建其低延迟远程结对编程应用程序。

文章强调，Electron使用Node.js作为其主进程，并使用Chromium进行渲染，由于捆绑了Node.js运行时和完整的Chromium引擎，导致应用程序体积较大。另一方面，Tauri使用Rust作为后端，编译成原生二进制文件，并依赖操作系统的原生WebView组件进行UI渲染，从而减小了应用程序包的大小并降低了内存使用率。然而，由于WebView实现的差异，这可能会导致跨平台的UI不一致。

一项比较使用每个框架构建的简单应用程序的基准测试表明，Tauri的捆绑包大小和内存使用率明显更低，尽管由于Rust编译，初始构建时间较慢。启动时间可以忽略不计。

Hopp选择Tauri是因为其基于Rust的后端为使用WebRTC进行视频流传输等密集型任务提供了更好的性能，并且Tauri内置的“Sidecar”功能简化了对屏幕流传输和远程控制输入的单独进程的管理。文章总结说，Tauri和Electron之间的最佳选择取决于具体的项目需求、团队专业知识和用例，这两种框架都能够构建强大的桌面应用程序。

---

## 88. 欧盟游戏内虚拟货币的关键原则

**原文标题**: Key principles on in-game virtual currencies in the EU

**原文链接**: [https://tiendil.org/en/posts/eu-key-principles-on-in-game-virtual-currencies](https://tiendil.org/en/posts/eu-key-principles-on-in-game-virtual-currencies)

本文探讨了欧盟委员会关于监管游戏内虚拟货币的建议及其对免费游戏（F2P）的潜在影响。作者概述了关键原则，包括将游戏内货币视为现实货币、保护交易中的消费者权益、禁止剥削性行为、同时显示现实货币价格和虚拟货币价格、不鼓励复杂的货币系统以及提供交易取消权。

作者预计实施这些法规会面临挑战，特别是对于中小型企业。开发者可能面临为欧盟市场调整游戏（可能减少收入）或完全避免该市场的抉择。转向更合乎道德的盈利模式可能需要重新培训游戏设计师并重新思考界面。

文章强调了技术挑战，例如实施可靠的交易日志，特别是对于具有客户端逻辑的游戏。它还建议必要的实施，如智能退款和家长控制。

作者推测了该法规的潜在结果：转向买断制或订阅模式，或者过度盈利的免费游戏退出欧盟市场。然而，他们对它的有效性表示怀疑，并将它与GDPR进行了比较。他们预测开发者会通过稍微调整他们的游戏并采用巧妙的游戏设计策略来规避规则，例如销售与游戏内货币间接相关的资源或收藏品，从而找到漏洞。

---

## 89. Charts.css

**原文标题**: Charts.css

**原文链接**: [https://chartscss.org/](https://chartscss.org/)

Charts.css 是一个现代 CSS 框架，它允许开发者仅使用 CSS 实用类和 HTML 创建各种图表。它拥有语义结构、通过 CSS 的可定制性、响应式、可访问性以及零 JavaScript 依赖等特性。该框架支持广泛的图表类型，包括面积图、条形图、柱状图、折线图、饼图和甜甜圈图，并提供多数据集、百分比、堆叠和 3D 变体。

该框架轻量级，gzip 压缩后文件大小仅为 7kb，由于无需 JavaScript 渲染，因此性能更佳。它在 MIT 许可下开源，可以自由修改。

该项目由开发者 Rami Yushuvaev 开发，由 Lana Gordiievska 设计。源代码可在 GitHub 上找到，欢迎用户为该存储库点亮星星。

---

## 90. 开发者工具蜜罐：为何我们总在构建无人问津的工具

**原文标题**: Dev Tools Honeytrap: Why We Can't Stop Building Tools Nobody Buys

**原文链接**: [https://substack.com/home/post/p-161145826](https://substack.com/home/post/p-161145826)

无法访问文章链接。

---

## 91. Rust 编译器中一个令人惊讶的枚举大小优化

**原文标题**: A surprising enum size optimization in the Rust compiler

**原文链接**: [https://jpfennell.com/posts/enum-type-size/](https://jpfennell.com/posts/enum-type-size/)

Rust编译器中一种令人惊讶的枚举大小优化

---

## 92. 在 Varnish 中使用 TinyKVM 运行 Deno

**原文标题**: Deno Under TinyKVM in Varnish

**原文链接**: [https://info.varnish-software.com/blog/tinykvm-in-varnish-and-some-deno](https://info.varnish-software.com/blog/tinykvm-in-varnish-and-some-deno)

本文介绍了高性能沙箱环境TinyKVM，及其作为Varnish Cache中计算框架的潜力。核心概念是在Varnish中直接启用任意代码执行以进行请求处理，从而提供诸如直接缓存访问和数据处理能力等优势。

作者重点介绍了TinyKVM的架构，强调其低开销的请求处理，包括通过临时VM实现的每个请求隔离。这允许干净的执行环境，每次请求后重置，有利于诸如JavaScript等语言中垃圾收集等内存密集型任务。

Laurence Rowe讨论了将Deno JavaScript运行时嵌入TinyKVM，展示了其利用每个请求隔离进行服务器端渲染的潜力。基准测试显示了令人鼓舞的结果，与现有的解决方案（如V8 isolates或进程forking）相比，延迟显著降低。Deno的实现受益于静态链接和一个新的“wait_for_requests_paused”API，用于同步调用。

文章还提到了一个GBC模拟器示例，展示了通过轻量级fork和对专用存储VM的函数调用实现的共享可变存储。还强调了通过hugepages提高性能，无需修改代码即可提升Deno性能。

最终，作者证明了TinyKVM提供高性能沙箱和每个请求隔离的能力（一个微小程序的平均时间为14us），为Varnish Cache内的高效数据处理打开了大门。他们强调正在进行的开发和可用的语言API（C、C++、Go、Javascript、Rust、Zig等），并邀请贡献以扩展其功能。

---

## 93. 还记得FastCGI吗？ (2021)

**原文标题**: Remember FastCGI? (2021)

**原文链接**: [https://brokenco.de/2021/06/27/remember-fastcgi.html](https://brokenco.de/2021/06/27/remember-fastcgi.html)

本文回顾了 FastCGI 协议，该协议允许长时间运行的进程处理多个 Web 请求，其定位介于 CGI 和现代“无服务器”函数之间。尽管它仍在 PHP 社区中使用，但已基本不再流行。作者探讨了它在 Rust 中的实用性，使用 `fastcgi` crate 创建了一个简单的 FastCGI 服务器。

然后，作者将 FastCGI 实现与使用 Rust 中的 Tide Web 框架构建的功能相同的程序进行了比较。 主要的结论是，设置 FastCGI 涉及进程管理和 Web 服务器配置（在示例中使用 Nginx），这引发了一个问题，即它是否比直接运行嵌入式 Web 服务器更有效。

Tide 示例突出了现代 Web 框架的简单性，允许直接测试而无需外部 Web 服务器。 用于 Tide 的 Nginx 配置也与 FastCGI 设置类似。

作者的结论是，FastCGI 在脚本语言对于处理 HTTP 请求而言速度太慢或不安全的情况下可能仍然有用。 然而，对于大多数用例而言，现代 HTTP Web 服务器是一种更简单且更实用的解决方案。 像 Tide 这样允许轻松嵌入服务器并直接处理路由的框架的兴起，使得 FastCGI 成为一个不太引人注目的选择。

---

## 94. Show HN: 构建更好的基础镜像

**原文标题**: Show HN: Building better base images

**原文链接**: [https://github.com/avkcode/container-tools](https://github.com/avkcode/container-tools)

容器工具旨在构建优化的、最小化的基于Debian的容器镜像，以解决常见的Dockerfile效率低下问题，如存储膨胀、网络冗余和重建速度慢。它利用`debootstrap`创建只包含必要组件的自定义根文件系统。

该工具允许用户使用简单的`make`命令构建各种Debian镜像（例如，Debian 11、带有Java的Debian 11、Kafka、GraalVM等）。它生成根文件系统的`.tar`归档文件，可以直接导入Docker。优点包括减小镜像大小和加快构建速度。

该项目被设计为可扩展的。用户可以通过创建配方（针对特定软件如Java或Kafka的安装脚本）并在Makefile中定义新目标来添加新的镜像变体。这些配方指定组件的下载URL和校验和。还集成了安全扫描脚本，用于构建后的漏洞评估。

该存储库的组织方式是将Debian配置文件、GPG密钥、配方（包括Java和Kafka）以及构建后脚本分别放置在单独的目录中。`dist/`目录包含输出镜像，而临时`download/`目录在构建过程中存储下载的软件包。这种方法有助于创建干净、高效和安全的容器镜像。

---

## 95. 无溅尿池：基于物理学和微分方程的设计

**原文标题**: Splash-free urinals: Design through physics and differential equations

**原文链接**: [https://academic.oup.com/pnasnexus/article/4/4/pgaf087/8098745?login=false](https://academic.oup.com/pnasnexus/article/4/4/pgaf087/8098745?login=false)

无法访问文章链接。

---

## 96. 哺乳动物程序化生成与运动

**原文标题**: Procedural Generation of Mammals and Locomotion

**原文链接**: [https://blog.runevision.com/2025/01/procedural-creature-progress-2021-2024.html](https://blog.runevision.com/2025/01/procedural-creature-progress-2021-2024.html)

本文详细介绍了游戏开发者从2021年至2024年，为游戏《大森林》程序化生成并动画制作逼真四足哺乳动物的进展。目标是使用一套可控的参数，创建具有合理解剖结构且始终有效的多样化森林生物。

开发者最初使用简单的拉伸矩形来表示生物的身体部位，这些矩形由从蒙皮参考网格中提取的大量底层参数控制。这种方法允许创建不同的生物并在它们之间进行插值，但这些参数过于细化且难以控制。

尝试使用主成分分析（PCA）自动识别有意义的参数失败了，因为由此产生的参数同时影响了太多的特征，使其不利于直观的生物设计。开发者得出结论，手动参数化是必要的。

随后，重点转向手动定义控制底层参数的高级参数。创建了一个工具来可视化参数之间的相关性，以帮助完成这个过程。一个重要的挑战是关节的准确定位，这需要解剖学研究以及处理参考模型中不一致的绑定。

为了加快示例生物的创建速度，开发了一个基于梯度下降的工具，以自动调整生物参数来匹配参考模型的轮廓。该工具使用有符号距离场（SDF）来比较轮廓并迭代优化生物的形状。到本文所述期间结束时，作者已经建立了106个控制所有503个底层参数的高级参数。

---

## 97. Systemd ParticleOS:

ParticleOS 系统管理器

**原文标题**: Systemd ParticleOS

**原文链接**: [https://github.com/systemd/particleos](https://github.com/systemd/particleos)

ParticleOS是使用mkosi构建的完全可定制的不可变Linux发行版。与其他不可变发行版不同，用户自行构建ParticleOS镜像，并使用自己的密钥对其进行签名，从而完全控制基础发行版和已安装的软件包。支持的发行版包括Arch和Fedora。

更新通过克隆ParticleOS仓库、配置`mkosi.local.conf`并运行`mkosi -ff sysupdate`来执行。建议使用OBS profile来访问systemd从其git main分支的每日构建版本。或者，用户可以从源代码构建systemd，并通过在`mkosi.local.conf`中指定构建产物将其集成到ParticleOS中。

通过使用用户生成的密钥（使用`mkosi genkey`创建）对镜像进行签名来启用安全启动，这些密钥可以存储在智能卡上。安装过程包括将构建的镜像刻录到USB驱动器，并使用`systemd-repart`将ParticleOS安装到目标驱动器。安全启动在安装期间必须处于设置模式。

对于LUKS加密分区，可以使用`cryptenroll`添加恢复密码。为了提高性能，应在安装后配置systemd-homed以禁用自动调整大小、启用LUKS discard并设置BTRFS挂载选项。

最后，当使用`mkosi vm`在虚拟机中运行ParticleOS时，为了方便起见，会自动创建一个默认的root密码和用户。

---

## 98. macOS 9 上的 SDL2“粗略草稿”

**原文标题**: SDL2 for macOS 9 “rough draft”

**原文链接**: [https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft](https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft)

无法访问文章链接。

---

## 99. Servo 中的生成式 AI

**原文标题**: Generative AI in Servo

**原文链接**: [https://www.azabani.com/2025/04/11/generative-ai-in-servo.html](https://www.azabani.com/2025/04/11/generative-ai-in-servo.html)

本文反对在 Servo 浏览器项目中使用 GitHub Copilot 等生成式 AI 工具。作者作为 Servo 的主要贡献者，对最近 TSC 投票放宽对 AI 贡献的禁令表示失望，认为这是一个未经适当社区协商而犯的错误。

核心论点是，生成式 AI 的缺点，例如生成不准确或误导性内容、增加维护者负担、潜在的法律问题和伦理问题，超过了在 Servo 开发中任何被认为的益处。作者强调社区对这些工具的压倒性共识是反对的，并强调了对项目健康、贡献质量以及向更广泛的 AI 运动发出的信号的担忧。

在主张对 Copilot 等工具采取坚定立场的同时，作者承认对用于狭隘目的的特定工具，例如语音识别和机器翻译，可能存在例外情况，但需要仔细考虑和社区驱动的评估。任何允许都将需要明确定义的用例、具体示例以及对工具的有效性和潜在风险的全面评估。

作者还反思了 TSC 内部的治理问题，指出社区协商和决策过程缺乏一致的结构，并建议公开 RFC 流程将是有益的。作者呼吁 TSC 重申其致力于将生成式 AI 排除在 Servo 之外，并重建与社区的信任。

---

## 100. 伊夫林·沃的颓废救赎

**原文标题**: Evelyn Waugh’s Decadent Redemption

**原文链接**: [https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/](https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/)

无法访问文章链接。

---

