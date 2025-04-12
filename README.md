# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-12.md)

*最后自动更新时间: 2025-04-12 17:46:37*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 2 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 3 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 4 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 5 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 6 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 7 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 8 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 9 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 10 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 11 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 12 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 13 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 14 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 15 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 16 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 17 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 18 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 19 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 20 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 21 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 22 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 23 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 24 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
