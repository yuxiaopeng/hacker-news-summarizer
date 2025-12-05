# Hacker News 热门文章摘要 (2025-12-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 奈飞将收购华纳兄弟

**原文标题**: Netflix to Acquire Warner Bros

**原文链接**: [https://about.netflix.com/en/news/netflix-to-acquire-warner-bros](https://about.netflix.com/en/news/netflix-to-acquire-warner-bros)

2025年12月，奈飞（Netflix）和华纳兄弟探索（WBD）宣布达成最终协议，奈飞将以827亿美元的企业价值收购华纳兄弟，包括其电影和电视工作室、HBO Max和HBO。该交易以现金和股票形式进行，每股WBD价值27.75美元。预计该收购将在WBD的全球网络部门“探索全球”分拆为一家新的上市公司后完成，预计在2026年第三季度。

此次合并旨在将华纳兄弟庞大的标志性系列特许经营和故事讲述遗产与奈飞的创新流媒体服务和全球影响力相结合。两家公司的高管强调，此次合并将为消费者提供更多选择，为创意社区创造机会，加强娱乐行业，并创造股东价值。奈飞计划维持华纳兄弟目前的运营，包括院线电影的发行。

奈飞预计到第三年每年将节省20-30亿美元的巨额成本，并预计该交易将在第二年增加GAAP每股收益。该交易需获得监管机构和股东的批准，以及其他惯例成交条件。该交易已获得两家公司董事会的一致批准，预计将在12-18个月内完成。

---

## 2. Cloudflare 2025年12月5日故障

**原文标题**: Cloudflare outage on December 5, 2025

**原文链接**: [https://blog.cloudflare.com/5-december-2025-outage/](https://blog.cloudflare.com/5-december-2025-outage/)

2025年12月5日，Cloudflare因代码部署缺陷导致约28%的HTTP流量受到影响，中断了25分钟。该缺陷旨在缓解CVE-2025-55182 React Server Components漏洞。中断发生在UTC时间08:47，原因是旨在增加WAF分析缓冲区大小的body解析逻辑变更，导致Cloudflare FL1代理出现错误。

具体而言，使用全局配置系统禁用内部测试工具传播了一项变更，触发了规则模块中的一个漏洞，导致HTTP 500错误。错误发生的原因是应用于具有“execute”动作的规则的熔断机制导致Lua异常，这是一个长期存在的、之前未被发现的代码错误。

该问题影响了使用部署了Cloudflare托管规则集的较旧FL1代理的客户。更改于UTC时间09:12被撤销，恢复了全面服务。

Cloudflare承认这次中断是不可接受的，尤其是在2025年11月18日发生类似事件之后。他们正在优先改进其部署和回滚系统，包括增强的推出和版本控制、简化的紧急修复功能以及“Fail-Open”错误处理。尽管11月18日中断后的更改正在进行中，但未能及时完成以防止12月5日的事件。Cloudflare已暂时锁定网络更改，并计划发布正在进行的弹性项目的详细分析。

---

## 3. 让RSS更有趣

**原文标题**: Making RSS More Fun

**原文链接**: [https://matduggan.com/making-rss-more-fun/](https://matduggan.com/making-rss-more-fun/)

本文详细介绍了作者如何创建 Firefox 扩展程序“TimewasterPro”，该扩展程序旨在通过提供类似 TikTok 的体验来发现小型网站的内容，从而对抗 RSS 阅读器疲劳。作者对传统 RSS 阅读器带来的乏味感以及被动消费随机内容的愿望感到沮丧，因此构建了一项服务，该服务可以提供网站、允许用户赞/踩，并使用这些投票来优先排序其他用户的内容。

该项目的后端使用 FastAPI 和 SQLAlchemy 构建，利用 SQLite 数据库，该数据库通过抓取 Kagi 小型网站 Github 存储库中的 RSS 提要来填充。该扩展程序具有基本的帐户系统（电子邮件验证），但作者对此和 JWT 身份验证表示不满，并指出用户体验问题。

作者承认该项目是一个爱好，而不是一项严肃的商业冒险，这反映在使用 System.css 库的有意的复古用户界面中。主要目标是创建一个用于个人享受和实验的工具。

目前，该扩展程序已索引超过 60 万个页面。未来的计划包括对内容进行分类以个性化推荐，并开发处理被踩内容的系统。作者希望提交更多独立的摄影、科学和手工艺网站，并承认由于技术内容的流行，非技术用户入门面临挑战。源代码将在项目达到更稳定状态时发布。该扩展程序可在 timewasterpro.xyz 下载。

---

## 4. UniFi 5G

**原文标题**: UniFi 5G

**原文链接**: [https://blog.ui.com/article/introducing-unifi-5g](https://blog.ui.com/article/introducing-unifi-5g)

UniFi 5G Max系列旨在为任何环境提供精简、灵活且强大的5G互联网解决方案。本质上，它专注于提供高性能、易于使用且兼容性广泛的5G体验。关键在于其强调无论在何种环境下都能提供可靠且高效的5G连接。

---

## 5. Framework Laptop 13 通过升级套件获得 12 核 ARM 处理器

**原文标题**: Framework Laptop 13 gets ARM processor with 12 cores via upgrade kit

**原文链接**: [https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html](https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html)

本文讨论了MetaComputing为Framework Laptop 13推出的一款新的基于ARM的主板升级套件，为英特尔、AMD和骁龙X系列处理器提供了一个替代方案。该主板采用CIX CP8180芯片组，拥有12个核心（8个性能核心和4个效率核心）和一个ARM Immortalis-G720 GPU。虽然性能可能不如旗舰移动芯片，但预计能够处理日常任务。

由于其潜在的高空闲功耗（16瓦），该升级主要针对开发者，这可能会显著降低Framework Laptop 13的电池续航时间。

MetaComputing ARM AI PC套件可直接从MetaComputing购买。基础型号包括主板、16GB RAM、1TB SSD和一个迷你PC机箱，售价为549美元。包含Framework Laptop 13的套装售价为999美元。升级到32GB RAM需额外支付100美元。全球免费送货，但进口费用和税款不包含在列出的价格中。

---

## 6. 大多数技术问题都是人的问题。

**原文标题**: Most technical problems are people problems

**原文链接**: [https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html](https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html)

本文认为，大多数技术问题都源于人的问题。作者讲述了自己通过重写重复代码库来解决重大技术债务的个人经历，并强调了由于开发人员对变革的抵制以及管理层缺乏理解，导致这项工作停滞不前。

核心论点是，诸如需求定义不清、不切实际的截止日期、过时的技能以及个人自负等因素会导致技术债务并阻碍进展。作者意识到，解决这些潜在的人的问题对于有效解决技术挑战至关重要。他强调，重构工作常常失败，因为它们暴露了现有软件开发实践和个人技能差距方面的系统性问题。

作者还反思了一个理想的工程世界的局限性，在这个世界里，没有截止日期和“政治”，技术解决方案应该自己说话。相反，与非技术利益相关者进行有效沟通、量化技术改进的价值以及驾驭人际关系的重要性被强调为高级工程师的必备技能。文章最后将“工程师的工程师”与“抬头编码者”进行了对比，后者将技术实力与预测风险和引导团队的能力相结合，并指出后者对于大型项目往往更有价值。

---

## 7. Netflix的AV1之旅：从安卓到电视及更远

**原文标题**: Netflix’s AV1 Journey: From Android to TVs and Beyond

**原文链接**: [https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80](https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80)

Netflix的AV1之旅：从安卓到电视及未来

---

## 8. Show HN: Kraa – 万能写作应用

**原文标题**: Show HN: Kraa – Writing App for Everything

**原文链接**: [https://kraa.io/about](https://kraa.io/about)

此“Show HN”帖子介绍 Kraa，据称是一款“适用于一切”的写作应用。标题表明它是一款旨在处理各种写作任务的通用工具，但提供的内容极其简单。仅重复出现了名称“Kraa”，我们可以推断：

*   **Kraa 是一款写作应用。** 这是其核心功能。
*   **它专为广泛的写作活动而设计。** “适用于一切的写作应用”表明其侧重于多功能性。

在没有更多细节的情况下，无法详细说明其功能、目标受众、平台可用性或任何潜在的竞争优势。该帖子本质上是一个占位符，宣布了 Kraa 写作应用的存在。要了解其真正的功能，需要通过外部链接或资源进一步研究 Kraa。

---

## 9. 宝马插电混动：安全熔断器更换极其昂贵

**原文标题**: BMW PHEV: Safety fuse replacement is extremely expensive

**原文链接**: [https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/](https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/)

无法访问文章链接。

---

## 10. X因违反内容规则被欧盟处以1.4亿美元罚款

**原文标题**: X hit with $140M EU fine for breaching content rules

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/eu-fines-x-140-mln-breaching-online-content-rules-tiktok-settles-with-2025-12-05/](https://www.reuters.com/sustainability/boards-policy-regulation/eu-fines-x-140-mln-breaching-online-content-rules-tiktok-settles-with-2025-12-05/)

**摘要：**

欧盟委员会因X（原推特）未能遵守《数字服务法案》（DSA），一项旨在监管在线内容和保护用户的新欧盟法律，对其处以1.28亿欧元（约合1.4亿美元）的罚款。欧盟发现，X未能充分解决非法内容的传播问题，包括仇恨言论，也未能打击平台上的虚假信息。具体而言，欧盟指出，X缺乏有效机制来及时删除非法内容，并且未能充分透明地披露其内容审核政策。

这是DSA实施以来开出的首张重大罚单，表明欧盟致力于执行新法规。DSA要求大型在线平台对其托管的内容承担更大的责任，并采取措施保护用户免受非法和有害内容的侵害。

另据报道，TikTok已同意在2025年2月前解决欧盟对其“奖励计划”的担忧，该计划据称可能对儿童造成伤害，从而避免潜在的调查和罚款。

---

## 11. 新冠mRNA疫苗接种与4年全因死亡率

**原文标题**: Covid-19 mRNA Vaccination and 4-Year All-Cause Mortality

**原文链接**: [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305)

我已接入互联网并分析了该文章。以下是摘要：

该研究发表在JAMA Network Open上，调查了COVID-19 mRNA疫苗接种与四年期间（2019-2022）全因死亡率之间的关联。研究人员采用回顾性队列研究设计，分析了美国大型综合医疗系统中超过67万人的数据。他们比较了疫苗接种者和未接种者之间的死亡率，并调整了各种人口统计学因素、既往病史和其他潜在的混杂因素。

主要发现表明，mRNA COVID-19疫苗接种与较低的全因死亡风险相关。具体而言，研究表明，在不同的年龄组和风险类别中，与未接种疫苗的人相比，接种疫苗的人的死亡率显著降低。疫苗接种的保护作用在COVID-19高传播时期似乎最为明显。

研究人员强调，虽然该研究表明疫苗接种与较低的死亡率之间存在相关性，但它并未建立因果关系。然而，这些发现为支持COVID-19疫苗接种在降低死亡风险方面益处的证据体系做出了贡献。他们还强调了在解释结果时考虑个体风险因素和不断变化的疫情形势的重要性。最终，该研究强化了接受COVID-19疫苗接种以预防严重后果（包括死亡）的公共卫生建议。

---

## 12. 我写小众历史博客已经15年了。

**原文标题**: I have been writing a niche history blog for 15 years

**原文链接**: [https://resobscura.substack.com/p/why-i-have-been-writing-a-niche-history](https://resobscura.substack.com/p/why-i-have-been-writing-a-niche-history)

以下是关于文章“我写一个小众历史博客已经15年了”的摘要：

作者回顾了其撰写小众历史博客 *Res Obscura* 的15年历程，该博客专注于鲜为人知和不寻常的历史话题。他们最初出于个人对发现被遗忘故事并与他人分享的热情而开始撰写博客。作者强调，最初博客的驱动力并非经济利益或受众规模，而是内在动力：研究、写作和学习的乐趣。

文章重点介绍了博客写作不断变化的性质以及在不断变化的数字环境中维持长期项目所面临的挑战。作者讨论了从传统博客平台到新闻通讯的转变，以及内容货币化日益增长的压力。他们承认在个人满足感与受众增长和潜在商业化的需求之间取得平衡的难度。

尽管存在这些挑战，作者仍强调了追求个人兴趣并与他人分享的持久价值，无论受欢迎程度或利润如何。他们强调保持真实性和忠于最初激发该项目热情的重要性。文章表明，虽然在线内容创作的格局不断发展，但好奇心、探索和联系的核心动机对于持续参与和个人满意度仍然至关重要。作者最终重申了他们继续撰写博客的承诺，这源于不断享受发现和分享鲜为人知的历史故事的乐趣。

---

## 13. Jolla手机预购

**原文标题**: Jolla Phone Pre-Order

**原文链接**: [https://commerce.jolla.com/products/jolla-phone-preorder](https://commerce.jolla.com/products/jolla-phone-preorder)

这是新款Jolla手机的预购活动，这是一款注重隐私和社区驱动开发的独立Linux手机。该手机被视为2013年原Jolla手机的继任者，并更新了现代规格。

主要功能包括5G连接、12GB内存、256GB存储（可扩展）、Sailfish OS 5（支持Android应用程序）、用户可更换电池和后盖，以及可禁用麦克风、蓝牙和Android应用程序的物理隐私开关。设计强调斯堪的纳维亚风格，并提供三种颜色。

预购价格为99欧元，可全额退款，并将从最终价格499欧元（含增值税）中扣除。预计交货日期为2026年上半年末。如果到2026年1月4日至少预订2,000台，该项目才会进行。支持者将获得特别版后盖。

这款手机强调隐私设计，避免跟踪和数据货币化。它不基于大型科技平台，旨在提供真正的替代方案。手机的功能和规格是通过社区输入定义的。Sailfish OS承诺提供长期支持（至少5年），并避免强制淘汰。这款手机的设计使其在全球范围内都能使用4G和5G网络。最初的销售市场包括欧盟、英国、挪威和瑞士。

---

## 14. Nimony (Nim 3.0) 设计原则

**原文标题**: Nimony (Nim 3.0) Design Principles

**原文链接**: [https://nim-lang.org/araq/nimony.html](https://nim-lang.org/araq/nimony.html)

本文概述了Nimony的设计原则，这是一款旨在成为Nim 3.0的新编译器，强调安全性、性能和简化的语言体验。一个核心目标是通过确保可预测的最坏情况执行时间 (WCET)，使其适用于硬实时和嵌入式系统。

内存管理通过基于作用域的析构函数和移动语义来处理，类似于Nim 2.0，但简化了MM开关（仅`mm:atomicArc`）。正在通过`.cyclic` pragma注解来探索循环回收。

错误处理偏离了现代的sum types。Nimony倾向于将错误状态集成到对象中（例如，浮点数的NaN）或利用线程局部错误变量。异常处理被保留，但需要显式的`{.raises.}`注解来表示具有隐藏控制流的函数。引入了新的`ErrorCode`枚举用于标准化错误传播。

为了解决OOM，Nimony采用了一个可重写的`oomHandler`，用于记录失败请求的大小。`.raises`例程中的`ref object`构造会自动将nil映射到`ErrorCode.OutOfMemError`。

本文强调了具有完整类型检查的泛型对于自定义容器的重要性。并发和并行性统一在`spawn`构造下，由一个在运行时确定线程执行的调度器管理。并行性通过并行for循环（例如，`||`迭代器）进一步支持。

spawn构造通过编译器插件实现——这是Nim宏的一种进化。模块插件附加到模块或名义类型，可以实现模块范围的转换和代码重写，例如避免线性代数运算中临时矩阵的创建。

---

## 15. Show HN: Pbnj – 一个极简的、可自托管的 Pastebin，你可以在 60 秒内完成部署

**原文标题**: Show HN: Pbnj – A minimal, self-hosted pastebin you can deploy in 60 seconds

**原文链接**: [https://pbnj.sh/](https://pbnj.sh/)

Pbnj是一个极简的自托管 Pastebin 解决方案，旨在通过简单的 URL 分享代码片段和文本文件，无需账户或臃肿功能。使用 Cloudflare 可以在大约 60 秒内完成部署。

该项目在其 GitHub 存储库上提供一键部署按钮，可自动将存储库 fork 到用户的 GitHub 账户并在 Cloudflare 上部署。Pbnj 的后端由 Cloudflare D1 提供支持，提供的成本明细消除了对高额费用的担忧，并引用了 D1 免费套餐，其中包括 500MB 存储空间、每天 500 万次读取和每天 10 万次写入。

Pbnj 提供用于创建和管理粘贴的 CLI 和 API。CLI 可以使用 npm 全局安装，并通过设置向导进行配置。API 需要通过 Bearer 令牌进行身份验证。一个 Web 界面也允许通过浏览器创建和管理粘贴，该界面使用与 CLI 和 API 相同的身份验证密钥。

应用程序的配置通过 `pbnj.config.js` 文件进行管理，允许自定义应用程序的名称、徽标和 ID 样式。

---

## 16. 欺骗用户，绕过警告——现代SVG点击劫持攻击

**原文标题**: Trick users and bypass warnings – Modern SVG Clickjacking attacks

**原文链接**: [https://lyra.horse/blog/2025/12/svg-clickjacking/](https://lyra.horse/blog/2025/12/svg-clickjacking/)

本文介绍了“SVG点击劫持”这种新型技术，它利用SVG滤镜来创建复杂且交互式的点击劫持攻击。与仅仅叠加iframe的传统点击劫持不同，SVG点击劫持允许攻击者操纵目标iframe内容的外观和行为，从而实现复杂的交互和数据窃取。

作者解释了如何组合各种SVG滤镜元素，例如`<feImage>`、`<feFlood>`、`<feOffset>`、`<feDisplacementMap>`、`<feColorMatrix>`等，来构建攻击原语。示例包括创建虚假验证码以诱骗用户重新输入敏感信息，以及使用掩蔽技术来隐藏输入字段中的占位符文本，引导用户输入攻击者选择的数据。

SVG点击劫持的一个关键方面是能够使用滤镜从iframe读取像素数据。这使得创建响应式虚假按钮和动态界面元素成为可能。通过检测像素颜色，攻击者可以触发不同的滤镜效果，模拟悬停状态、下拉菜单，甚至表单验证。

文章进一步演示了如何使用`feBlend`和`feComposite`构造逻辑门（AND、OR、XOR、NOT等）。这使得SVG滤镜在功能上是完备的，允许攻击者在滤镜中编写复杂的逻辑。作为概念验证，作者展示了一个SVG加法器电路，展示了实现任意逻辑电路的能力，从而为更复杂、响应性更强且更具欺骗性的点击劫持攻击打开了可能性。

---

## 17. 在冒险游戏耕耘40年后，罗恩·吉尔伯特转战躲避死神。

**原文标题**: After 40 years of adventure games, Ron Gilbert pivots to outrunning Death

**原文链接**: [https://arstechnica.com/gaming/2025/12/after-40-years-of-adventure-games-ron-gilbert-pivots-to-outrunning-death/](https://arstechnica.com/gaming/2025/12/after-40-years-of-adventure-games-ron-gilbert-pivots-to-outrunning-death/)

本文探讨了罗恩·吉尔伯特从经典点击冒险游戏到他新的Roguelike动作游戏《滚动死亡》的意外转变。吉尔伯特解释说，虽然他以《猴岛》和《银莲公园》等游戏而闻名，但他一直很喜欢动作游戏，并受到了《以撒的结合》等游戏的启发。

他透露，他在《猴岛》之后的最初项目是一个雄心勃勃的类似塞尔达的RPG，但由于资金和时间限制，他在一年后放弃了它。发行商提供了不利的协议，众筹也不是一个可行的选择。这让他回到了一个名为“Runner”的原型，该原型演变成了《滚动死亡》，玩家在游戏中逃离滚动的屏幕并躲避死神本身。

吉尔伯特讨论了为动作游戏写作的挑战，因为玩家经常跳过故事。他还通过游戏系统批判了现代资本主义，突出了一个以利润为导向的炼狱。

最后，吉尔伯特认为传统的点击冒险游戏形式正在变得过时，并以《洛雷莱与激光眼》等游戏为例，说明了现代冒险游戏的设计。他还感叹游戏推广方式的转变，开发者需要在YouTube等平台上成为有魅力的表演者，而他觉得自己缺乏这种技能。

---

## 18. 肯尼亚法院宣布禁止种子分享的法律违宪

**原文标题**: Kenyan court declares law banning seed sharing unconstitutional

**原文链接**: [https://apnews.com/article/kenya-seed-sharing-law-ruling-ad4df5a364299b3a9f8515c0f52d5f80](https://apnews.com/article/kenya-seed-sharing-law-ruling-ad4df5a364299b3a9f8515c0f52d5f80)

肯尼亚高等法院宣布2012年种子法关键条款违宪，标志着粮食安全倡导者和小农户的胜利。该法律此前将分享和出售本地种子定为犯罪，威胁农民因通过社区种子银行从事传统活动而面临监禁和巨额罚款。法官罗达·鲁托还裁定，允许政府官员从这些银行没收种子的条款无效。

该法律最初旨在打击假冒种子的销售，假冒种子给农业部门造成了重大损失，并且仅赋予持证公司贸易权。然而，15名农民对该法律提出质疑，认为它侵犯了他们保存和分享种子的能力，而这种做法对粮食安全至关重要。

法院的判决证明了传统耕作方式的正确性，允许农民自由分享和保存种子，而无需担心法律后果。绿色和平非洲组织的伊丽莎白·阿蒂诺等粮食活动家称赞该裁决是对企业控制粮食体系的打击，确保农民可以使用具有气候韧性的、本地适应的种子。本地种子因其耐旱性和适应性而受到重视，通常在其原产地表现优于杂交品种。虽然肯尼亚拥有国家种子银行，但社区种子银行被认为对种子多样性和农民获取种子的途径同样重要。

---

## 19. 新的3D扫描揭示了复活节岛上摩艾石像雕刻者鲜为人知的网络

**原文标题**: New 3D scan reveals a hidden network of moai carvers on Easter Island

**原文链接**: [https://www.sciencedaily.com/releases/2025/11/251130050717.htm](https://www.sciencedaily.com/releases/2025/11/251130050717.htm)

复活节岛拉诺拉拉库采石场最新3D扫描显示，岛上著名的摩艾石像是由独立的群体雕刻而成，而非由中央控制的劳动力完成。研究人员在卡尔·菲利普·利波的带领下，利用11000多张照片创建了一个详细的3D模型，揭示了30个独特的采石区域，每个区域都有独特的雕刻风格。这表明摩艾石像的生产反映了该岛分散的社会结构，各个家庭群体在共享技术的同时独立工作。

这项研究挑战了长期以来认为大型纪念碑项目需要严格等级制度和统一控制的假设。摩艾石像设计的相似之处归因于共享的文化知识，而非协调的劳动。该模型还确定了多条运输路线，进一步支持了分散雕刻的理论。

该研究为未来的调查和联合国教科文组织世界遗产地的文化管理提供了宝贵的数据集。该团队使用的方法可以应用于其他考古遗址。该研究强调了开放、详细的证据在理解复活节岛和其他历史遗址的“谜团”中的重要性。这些发现为摩艾石像的组织和制造过程提供了新的见解。

---

## 20. 关于草甘膦安全性的有影响力研究在发表25年后被撤回

**原文标题**: Influential study on glyphosate safety retracted 25 years after publication

**原文链接**: [https://www.lemonde.fr/en/environment/article/2025/12/03/influential-study-on-glyphosate-safety-retracted-25-years-after-publication_6748114_114.html](https://www.lemonde.fr/en/environment/article/2025/12/03/influential-study-on-glyphosate-safety-retracted-25-years-after-publication_6748114_114.html)

一项2000年发表的重要研究，该研究曾得出草甘膦是安全的结论，在25年后已被《监管毒理学与药理学》期刊撤回。撤回的原因是“若干关键问题”破坏了该研究的学术诚信。

核心问题在于，列出的作者——Gary M. Williams、Robert Kroes 和 Ian C. Munro——并非文章的实际作者。相反，孟山都公司的员工代笔了这项研究，这种做法被认为是科学欺诈。这一发现是在八年前美国法院诉讼程序中公开的孟山都内部文件（“孟山都文件”）之后浮出水面的。

代笔是一种欺骗性行为，公司付费给研究人员，让他们将自己的名字借给他们没有进行的研究。动机是提高对公司产品有利的研究的可信度，特别是关于农药或药物的安全性。文章强调，一篇看似由独立科学家撰写的文章，比一篇明确由营销该产品的公司撰写的文章更具份量。

---

## 21. Show HN: Tacopy – Python 的尾调用优化

**原文标题**: Show HN: Tacopy – Tail Call Optimization for Python

**原文链接**: [https://github.com/raaidrt/tacopy](https://github.com/raaidrt/tacopy)

Tacopy 是一个 Python 库，它通过装饰器提供尾调用优化 (TCO)，允许深度递归而不会发生堆栈溢出错误。它在装饰时将尾递归函数转换为迭代循环，与标准递归相比，性能提升 1.41 倍至 2.88 倍。

该库通过 `pip install tacopy-optimization` 或 `uv add tacopy-optimization` 安装，并通过使用 `@tacopy` 装饰尾递归函数来使用。它的工作原理是使用 AST 转换将函数转换为带有变量赋值的 `while` 循环。

Tacopy 要求函数为模块级别、非异步，并且所有递归调用都在尾位置（立即返回）。装饰器包含验证以确保函数满足这些标准，如果不满足则引发 `TailRecursionError`。函数 `show_transformed_code` 允许查看转换后的代码以进行调试。

基准测试表明，与标准递归相比，速度显着加快，性能更加稳定。虽然 Tacopy 功能强大，但也有局限性，包括需要 Python 3.10+、模块级函数、可访问的源代码，并且仅支持直接自递归（不支持相互递归）。该库在 GPL v3.0 许可下发布，欢迎贡献。

---

## 22. CSS 现在有了 if() 条件函数

**原文标题**: CSS now has an if() conditional function

**原文链接**: [https://caniuse.com/?search=if](https://caniuse.com/?search=if)

本文重点介绍了`if()` CSS函数的引入，该函数允许基于样式、媒体或功能查询的结果进行有条件的属性值分配。文章还提到了几个HTML `iframe`相关的属性，包括`sandbox`、`seamless`、`srcdoc`和`loading`。但是，`seamless`属性已从HTML规范中移除。文章还列出了`iframe`元素的许多与权限和安全相关的属性，从`allow`开始，用于向`iframe`中的内容授予/限制不同的浏览器功能。最后，它还涉及了相关的概念，如HTTP头`if-match`、`if-none-match`、`if-range`和JavaScript `if...else`语句。

---

## 23. 短暂基础设施：短寿为何是好事

**原文标题**: Ephemeral Infrastructure: Why Short-Lived Is a Good Thing

**原文链接**: [https://lukasniessen.medium.com/ephemeral-infrastructure-why-short-lived-is-a-good-thing-2cf26afd75ef](https://lukasniessen.medium.com/ephemeral-infrastructure-why-short-lived-is-a-good-thing-2cf26afd75ef)

**短暂基础设施：为什么短寿命是好事 - 摘要**

本文认为，使用短暂基础设施（即设计为在短时间内自动配置和销毁的基础设施）在现代软件开发和部署中具有显著优势。传统的长期基础设施虽然熟悉，但也面临配置漂移、环境不一致以及难以回滚变更等挑战。

短暂基础设施通过促进不变性来解决这些问题。每个环境都从一个定义的状态（例如，通过基础设施即代码）创建，并且在配置过程中应用任何必要的更改，从而产生一致且可重现的环境。一旦完成其任务（例如，运行一组特定的测试或服务于特定的部署版本），该基础设施就会被销毁，而不会被修改。

强调的关键好处包括：

*   **减少配置漂移：** 基础设施始终从已知的良好状态重新创建，从而消除随时间累积的不一致性。
*   **简化回滚：** 回滚到以前的版本就像部署相应的基础设施配置一样简单。
*   **提高安全性：** 短暂的基础设施减少了攻击面和潜在损害的持续时间。
*   **加快部署速度：** 自动化能够实现更快、更可靠的部署。
*   **提高资源利用率：** 资源仅在需要时才使用，从而节省成本。

本文强调，虽然实施短暂基础设施需要对自动化和工具（例如，基础设施即代码工具、CI/CD 管道）进行初始投资，但从长远来看，收益大于成本，从而实现更可靠、安全和高效的部署。

---

## 24. 特斯拉Model Y在德国权威TÜV报告中被评为可靠性最差的汽车。

**原文标题**: Tesla Model Y named worst car for reliability in Germany's major TÜV report

**原文链接**: [https://electrek.co/2025/12/03/tesla-model-y-named-worst-car-for-reliability-germany-major-tuv-report/](https://electrek.co/2025/12/03/tesla-model-y-named-worst-car-for-reliability-germany-major-tuv-report/)

德国TÜV 2026报告显示，特斯拉Model Y在2-3年车龄车辆的可靠性排名中垫底，因“重大”或“危险”缺陷导致强制安全检测的故障率高达17.3%，远超6.5%的平均水平。Model 3的表现略好，但也仅排倒数第三。

报告指出悬架部件（尤其是控制臂衬套）和刹车盘存在问题。刹车问题归因于德国潮湿气候下，由于能量回收制动导致刹车使用频率较低而产生的锈蚀。照明缺陷也是原因之一。

报告将特斯拉的表现与其他电动汽车（如Mini Cooper SE和奥迪Q4 e-tron）进行对比，后者缺陷率远低于特斯拉，表明问题具有特斯拉特异性。虽然动力总成依然可靠，但悬架问题一直备受关注，美国国家公路交通安全管理局（NHTSA）已经进行了调查和召回。文章强调，刹车问题虽然导致安全检测不合格，但并不一定意味着车辆会抛锚，而是建议驾驶员更频繁地使用刹车。

---

## 25. 当人工智能降低说服成本时，精英如何塑造大众偏好

**原文标题**: How elites could shape mass preferences as AI reduces persuasion costs

**原文链接**: [https://arxiv.org/abs/2512.04047](https://arxiv.org/abs/2512.04047)

这篇arXiv论文，"精心设计下的极化：当人工智能降低说服成本时，精英如何塑造大众偏好"（作者：Nadav Kunievsky），探讨了人工智能驱动的说服技术对民主社会的潜在影响。作者认为，人工智能能够廉价且精确地塑造公众舆论，这使得偏好分布成为精英阶层的战略工具。

该论文提出了一个动态模型，在这个模型中，精英们战略性地操纵政策偏好，同时考虑到说服成本和多数规则的制约。该模型表明，单个精英的干预往往会导致社会极化。此外，说服技术的改进会加速这种极化。

当两个对立的精英争夺权力时，该技术可能会产生激励，促使他们建立具有凝聚力意见的“半锁定”区域，这些区域能够抵抗竞争对手的影响。因此，先进的说服技术可以加剧或减少极化，具体取决于竞争环境。

核心结论是，更廉价的说服技术将极化重新定义为一种刻意的治理策略，而非纯粹的涌现式社会现象。随着人工智能能力的不断发展，这对于民主稳定具有重大影响。该论文属于一般经济学、人工智能以及计算机与社会等领域。

---

## 26. NASA小行星贝努样本中发现糖类、树胶和星尘

**原文标题**: Sugars, Gum, Stardust Found in NASA's Asteroid Bennu Samples

**原文链接**: [https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/](https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/)

美国宇航局OSIRIS-REx任务的贝努小行星样本带来了突破性发现，为早期太阳系和生命的起源提供了见解。三项最新研究重点如下：

*   **生命必需的糖类：** 科学家发现了核糖和葡萄糖，分别是RNA的重要组成部分和能量的关键来源。这表明生物分子的构建块广泛存在，并且在早期太阳系中，核糖可能比脱氧核糖更为普遍，支持了“RNA世界”假说。
*   **神秘的古代“口香糖”：** 发现了一种以前未见过的、富含氮和氧的口香糖状物质。这种聚合物状材料形成于太阳系早期，可能为地球上的生命提供了化学前体。它是氨基甲酸酯聚合反应的产物，并随着时间的推移而硬化，类似于“太空塑料”。
*   **丰富的超新星尘埃：** 样本中包含的早于太阳系的恒星尘埃含量是之前研究过的任何星体物质的六倍。这表明贝努的母体可能形成于一个富含垂死恒星尘埃的区域。样本中未改变或改变较少的物质区域也揭示了小行星的起源和形成。

这些发现共同表明，像贝努这样的小行星可能将生命的关键成分带到了早期地球，并突显了研究原始星体物质对于理解太阳系早期条件的重要性。

---

## 27. 我们给了5个大型语言模型10万美元，让它们交易股票8个月

**原文标题**: We gave 5 LLMs $100K to trade stocks for 8 months

**原文链接**: [https://www.aitradearena.com/research/we-ran-llms-for-8-months](https://www.aitradearena.com/research/we-ran-llms-for-8-months)

我们给了5个LLM 10万美元炒股8个月

---

## 28. 透明领导胜过服务型领导

**原文标题**: Transparent leadership beats servant leadership

**原文链接**: [https://entropicthoughts.com/transparent-leadership-beats-servant-leadership](https://entropicthoughts.com/transparent-leadership-beats-servant-leadership)

本文反对仆人式领导，将其比作“冰壶式育儿”，即领导者不断为团队扫除障碍，最终阻碍了团队的成长，并在领导者离开后使团队措手不及。作者提出“透明领导”是一种更有效的领导方式。

透明领导侧重于通过指导、将团队成员与资源和其他人联系起来、教授解决问题的技能以及明确组织价值观来赋能团队成员，从而使其能够独立决策。它强调需求与资源之间的直接联系，通过逐步转移领导职责、持续培训继任者以及追求冗余来促进职业发展。

作者认为，真正有效的领导者应该努力成为一名高效率的备用人员，回归到技术问题的解决，而不是在自己的领导角色被他人有效填补后，制造不必要的官僚主义或发明新的任务。这能够保持他们的技能敏锐，赢得尊重，并使他们能够为团队的整体成功做出有意义的贡献。本质上，目标是使团队能够独立有效地运作，从而最终降低领导者对日常运营的关键性。

---

## 29. 多体素：体显示

**原文标题**: Multivox: Volumetric Display

**原文链接**: [https://github.com/AncientJames/multivox](https://github.com/AncientJames/multivox)

Multivox：基于旋转HUB75 LED面板的体素显示器项目，主要面向Raspberry Pi 4。它支持两种配置：Rotovox（更高的垂直分辨率）和Vortex（更亮、更快的刷新率）。硬件由绕垂直轴旋转的两个面板组成，通过GPIO光电二极管同步旋转。输入通过蓝牙手柄管理，音频通过蓝牙耳机协议管理。

该项目包括一个驱动程序，在共享内存中创建体素缓冲区并将其扫描到LED，以及用于生成内容的客户端代码。一个演示允许从PC流式传输点云，但该系统被设计为独立的设备。该代码包括特定硬件配置的驱动程序、一个软件模拟器(virtex)和一个用于启动体素演示程序的启动器(multivox)。

该存储库包含诸如光周期、烟花、4D立方体和一个.obj/.png查看器等演示程序。Python工具包括校准、模式生成、转换.obj模型和流式传输点云。

构建过程包括克隆存储库，使用CMake为特定硬件（Rotovox或Vortex）配置项目，以及编译。运行驱动程序需要`sudo`并输出分析信息；演示程序从命令行启动。查看器允许使用手柄操作模型。模拟器（virtex）提供虚拟显示。

可以通过systemd设置驱动程序在启动时自动运行，并通过crontab设置启动器在启动时自动运行。Multivox充当幻想游戏机，启动游戏和演示程序。它允许循环浏览“卡带”（应用程序），启动它们以及调整位深度。

---

## 30. Show HN: 我重新认识了计算机：树莓派

**原文标题**: Show HN: I was reintroduced to computers: Raspberry Pi

**原文链接**: [https://airoboticist.blog/2025/12/01/i-was-reintroduced-to-computers-raspberry-pi/](https://airoboticist.blog/2025/12/01/i-was-reintroduced-to-computers-raspberry-pi/)

作者在工作期间专注于AI模型微调之后，重拾了使用树莓派进行物理计算的乐趣。 受家庭安全焦虑（例如，忘记关电器）的驱使，作者开始了一个项目，用树莓派制作一个带有实时视频流的远程遥控车。

作者选择了树莓派Zero 2 W，因为它价格实惠且拥有完整的Linux操作系统。 该项目包括组装一个带有电机驱动器、电池、降压转换器和USB摄像头的2WD小车套件。 树莓派运行一个基于Python的电机控制服务器，并使用mjpg-streamer进行视频传输。

作者重点介绍了使用Nginx作为反向代理，将电机服务器、视频流和Web界面整合到一个URL下。 Systemd用于管理这些服务，确保它们自动启动和重启。

为了远程访问该机器人，作者在购买域名后实施了Cloudflare Tunnel。 这使得可以在家庭网络之外进行控制和监控，而无需暴露家庭IP。

作者强调了树莓派和Linux环境的可访问性和潜力，表示后悔没有早点发现它们，并希望能够激励其他人。 该项目演示了如何使用树莓派、基本电子元件和云服务创建一个可远程访问和控制的设备。

---

## 31. 重塑影响力

**原文标题**: Reframing Impact

**原文链接**: [https://turntrout.com/reframing-impact](https://turntrout.com/reframing-impact)

重塑影响：本文介绍了一系列旨在解决人工智能对齐问题的思维实验和解释，具体是如何防止目标不完善的强大人工智能系统造成灾难性后果。作者认为，开发一种“影响度量”至关重要，它是一种无需事先解决深奥难题的关键保障。这种度量应该在数学上是合理的，并且可以直接在代码中实现。作者将这种方法与Quantilizer、价值学习和可纠正性等替代方案进行了对比。他们认为，Quantilizer在处理强大代理和定义安全基础分布方面存在缺陷，而价值学习则依赖于可能无法实现的完美假设，并且如果学习出错就会失败。可纠正性虽然很有希望，但如果代理在纠正生效之前行动过快，可能无法防止损害。该序列旨在回答三个核心问题：为什么我们将某些事情视为重大事件，为什么以目标为导向的人工智能默认情况下会被激励造成灾难性影响，以及如何构建缺乏这些激励因素的代理。最初的章节侧重于建立基本概念。作者强调积极参与材料，包括快速准确地完成练习，以便在探索潜在解决方案之前真正理解根本问题。“回形针-巴洛克”插图可以作为一种隐喻，说明影响度量在面对为强大代理正确指定目标的挑战时能够保持坚定。

---

## 32. NeurIPS 2025最佳论文奖

**原文标题**: NeurIPS 2025 Best Paper Awards

**原文链接**: [https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

本文宣布了 NeurIPS 2025 最佳论文奖，重点介绍了机器学习领域的突破性研究。四篇论文获得了“最佳论文”奖，另有三篇论文获得了主会场和数据集与基准测试赛道的“亚军”荣誉。

获奖论文涵盖以下多个领域：

*   **“人工蜂群思维：语言模型（及其他）的开放式同质化”**: 介绍了 Infinity-Chat，这是一个用于评估语言模型在开放式查询中多样性的新基准，揭示了一个令人担忧的“人工蜂群思维”效应，即模型表现出同质化，并且与多样化的人类偏好存在偏差。
*   **“大型语言模型的门控注意力：非线性、稀疏性和无注意力沉没”**: 证明在缩放点积注意力之后添加头部特定的sigmoid门控可以持续提高大型语言模型的性能、训练稳定性，减轻“注意力沉没”，并改善长上下文外推。
*   **“用于自监督强化学习的1000层网络：扩展深度可以实现新的目标达成能力”**: 展示了在自监督强化学习中使用极深（高达1024层）神经网络的优势，从而在目标达成任务中带来显著的性能提升。
*   **“为什么扩散模型不记忆：训练中隐式动态正则化的作用”**: 探讨了扩散模型训练的动态过程，识别出不同的泛化和记忆阶段，并揭示了一种隐式正则化，使模型能够有效地泛化。

亚军论文 **“强化学习真的能激励LLM中超越基础模型的推理能力吗？”** 批判性地审查了带有可验证奖励的强化学习（RLVR），发现它可能不会在LLM中激发超越基础模型中已存在的根本性新的推理能力。

---

## 33. StardustOS: 构建轻量级Unikernels的库操作系统

**原文标题**: StardustOS: Library operating system for building light-weight Unikernels

**原文链接**: [https://github.com/StardustOS](https://github.com/StardustOS)

StardustOS是一个为云应用设计的单内核操作系统，提供轻量级的单地址空间环境。它将资源管理委托给虚拟机管理程序，从而最小化代码库，并依靠静态链接将最小内核与单个应用程序、相关库以及必要的编程语言运行时结合起来。这产生一个不可变的、单用途的虚拟机镜像。

StardustOS的特性包括多核支持、抢占式线程、基本块和网络驱动程序，以及一系列POSIX兼容的库。它被用于圣安德鲁斯大学的教学和研究。

该项目包含几个组件：Stardust（C语言实现）、Stardust-oxide（Rust重写版本）和Duster，一个用于在Xen上运行的半虚拟化单内核的调试器。

该文档还列出了一系列与Stardust相关的讲座和材料，重点关注诸如Lambda函数的单内核支持、调试单内核操作系统、单内核工程和部署轻量级服务等主题。

---

## 34. 对抗年龄限制的网络

**原文标题**: Fighting the age-gated internet

**原文链接**: [https://www.wired.com/story/age-verification-is-sweeping-the-us-activists-are-fighting-back/](https://www.wired.com/story/age-verification-is-sweeping-the-us-activists-are-fighting-back/)

本文关注互联网上日益增长的年龄验证法案运动，以及由数字权益组织“为未来而战”领导的反对运动。国会成员周二审议了19项在线安全法案，其中许多法案包括访问成人内容的年龄验证要求，需要上传身份证或进行面部扫描。“为未来而战”认为，这些政策会导致审查、监控和通过第三方服务进行数据泄露的增加。

提到的关键法案包括《儿童在线安全法案》(KOSA)和《减少青少年接触剥削性社交媒体法案》，引发了人们对家长控制、数据隐私和人工智能作用的担忧。“为未来而战”强调，这些法律不受公众欢迎，但被立法者视为“常识”。

文章指出，美国已有25个州通过了某种形式的年龄验证，而英国的《在线安全法案》和澳大利亚的青少年社交媒体禁令等国际授权正在生效。包括90多个人权团体在内的批评者认为，年龄验证将互联网用户视为犯罪嫌疑人，并将企业利润放在首位。

“为未来而战”倡导全面的隐私立法和反垄断措施，而不是验证授权，指责国会未能解决大型科技公司有害行为的根本原因。他们警告说，这些法律可以被用来审查广泛的信息，模仿禁书和限制医疗保健信息。

文章最后强调，年龄验证影响到所有互联网用户，要求每个人证明他们不是未成年人，并敦促人们了解这场斗争的高风险。

---

## 35. CUDA-l2: 通过强化学习超越 cuBLAS 矩阵乘法性能

**原文标题**: CUDA-l2: Surpassing cuBLAS performance for matrix multiplication through RL

**原文链接**: [https://github.com/deepreinforce-ai/CUDA-L2](https://github.com/deepreinforce-ai/CUDA-L2)

CUDA-L2：利用LLM和RL优化半精度通用矩阵乘法(HGEMM)的CUDA内核。它在众多矩阵配置下，性能明显优于torch.matmul和NVIDIA的cuBLAS库等既有基准（包括cuBLASLt的启发式和自动调优版本）。该项目已发布针对A100 GPU的1000种不同矩阵配置的优化HGEMM内核。

未来计划包括支持32位累加器、处理更密集的矩阵配置、扩展对Ada Lovelace、Hopper和Blackwell GPU的支持，并为开源LLM提供便捷部署。目前，发布的内核专门针对A100进行了优化，不能保证在其他GPU上的加速效果。对于未包含在提供的配置中的矩阵维度，建议用零填充到最接近的较大支持配置，或通过GitHub issues请求支持该维度。

要使用CUDA-L2，用户需要一个Python环境、PyTorch 2.6.0或更高版本，以及特定版本的NVIDIA CUTLASS (v4.2.1)。必须正确配置环境变量`CUTLASS_DIR`和`TORCH_CUDA_ARCH_LIST`。`eval_one_file.sh`脚本用于在离线（批量处理）或服务器（基于请求的模拟）模式下进行评估。提供特定参数来控制矩阵大小、基准测试持续时间、GPU选择以及服务器模式下的目标每秒查询数。

---

## 36. 在苹果丽莎电脑上的IT学校

**原文标题**: At IT School with Apple Lisa

**原文链接**: [https://blisscast.wordpress.com/2024/06/04/apple-lisa-gui-wonderland-3/](https://blisscast.wordpress.com/2024/06/04/apple-lisa-gui-wonderland-3/)

本文是“GUI仙境”系列的第三篇，重点介绍1983年发布的Apple Lisa，它被认为是第一台具有面向大众消费的GUI的个人电脑。 Lisa的设计旨在用于办公，目标是让不熟悉计算机的用户也能轻松使用。

Lisa的开发始于1978年的“LISA项目”，最初是作为现代化的Apple II/III迭代产品。 在经历了一个艰难的开端后，史蒂夫·乔布斯参与其中，并受到访问施乐PARC的启发，该项目转向了基于GUI的系统。 这涉及重大更改，融入了来自施乐Smalltalk环境的想法，例如鼠标驱动的界面和位图显示。 施乐员工拉里·泰斯勒加入苹果公司，领导系统软件的开发。 用户测试影响了“Lisa用户界面标准”文档，优先考虑用户友好性。

文章随后深入探讨了GUI，重点介绍了两种主要的用户模式：Lisa Office System（LisaOS，主要的GUI环境）和Lisa Workshop（基于文本的开发环境）。 LisaOS旨在直观且视觉驱动（WYSIWYG），隐藏不必要的元素直到需要时才显示。 目标是提供一个不需要计算机知识的界面。

文章为未来关于Lisa面向任务的工作流程、窗口、桌面实用程序、复制粘贴功能、软件、硬件以及最终的停产和遗产的讨论奠定了基础。 它还简要提到了它面临的来自施乐Star和VisiOn的竞争，以及Macintosh的发布对Lisa成功的影响。

---

## 37. 为什么有38%的斯坦福学生声称自己有残疾？

**原文标题**: Why are 38 percent of Stanford students saying they're disabled?

**原文链接**: [https://reason.com/2025/12/04/why-are-38-percent-of-stanford-students-saying-theyre-disabled/](https://reason.com/2025/12/04/why-are-38-percent-of-stanford-students-saying-theyre-disabled/)

精英大学学生声称残疾并获得学业便利现象激增：一种令人惊讶的趋势

---

## 38. FDA提议了不可能达到的疫苗标准，这可能会限制疫苗的可及性。

**原文标题**: FDA proposes impossible standards for vaccines that could curtail access

**原文链接**: [https://www.cidrap.umn.edu/childhood-vaccines/fda-official-proposes-impossible-standards-vaccine-testing-could-curtail-access](https://www.cidrap.umn.edu/childhood-vaccines/fda-official-proposes-impossible-standards-vaccine-testing-could-curtail-access)

文章报道了人们对美国食品药品监督管理局（FDA）顶级疫苗监管人员Vinay Prasad医学博士（MPH）提出的新疫苗测试标准感到的担忧。专家们担心这些“不可能的”标准可能会严重限制救命疫苗的开发和供应。

Prasad通过社交媒体披露的内部备忘录建议对大多数新疫苗（包括孕妇疫苗）进行上市前随机对照试验（RCT）。 专家认为，由于伦理问题和对胎儿的潜在风险，要求对孕妇进行RCT是不现实的。 目前的做法依赖于谨慎的安全监测和抗体水平测量。

该备忘录还批评了目前针对肺炎和流感疫苗的测试。 Prasad希望有证据表明肺炎疫苗可以减少肺炎病例，并建议对更新的流感疫苗进行更严格的年度测试。 专家认为，要求进行如此广泛的试验将耗时、成本高昂，并且可能不道德，因为它将涉及使用安慰剂并使个人容易感染可预防的疾病。 流感毒株的快速变化也使得每年的RCT不切实际。

批评人士称，Prasad的备忘录只关注潜在的疫苗风险，而没有承认它们的益处或拯救的生命。 他们担心，由于缺乏疾病控制与预防中心（CDC）的建议或保险覆盖，拟议的标准可能会导致事实上的疫苗禁令。 法律专家认为，这些变更可能会因“武断和反复无常”而在法庭上受到质疑。 美国儿科学会也表示担心拟议的要求可能会限制儿童获得安全、可靠的疫苗。

---

## 39. 我以资深工程师的身份无视聚光灯。

**原文标题**: I ignore the spotlight as a staff engineer

**原文链接**: [https://lalitm.com/software-engineering-outside-the-spotlight/](https://lalitm.com/software-engineering-outside-the-spotlight/)

本文对比了大型科技公司中成为Staff+工程师的两种途径，认为追逐“聚光灯”并非实现影响力和职业成功的唯一道路。作者将其在开发者工具和基础设施领域的工作经历与产品团队工程师的经历进行了对比，后者往往受到高管关注度和季度目标驱动。作者认为，在基础设施领域，**管护责任（stewardship）**和长期所有权可以通过效率、系统性创新以及对威胁系统稳定性的短暂趋势（如过早的人工智能集成）说“不”的能力，带来复利回报。

作者强调，离开“聚光灯”可以发展其他形式的价值：**“影子等级制度”（Shadow Hierarchy）**，即给其他组织中有影响力的工程师留下深刻印象比给直接管理层留下深刻印象更有价值；以及一个基于bug修复、关键性、普遍性和规模等指标的**“效用账本”（Utility Ledger）**。这些指标展示了真正的技术影响力，并且能够抵御高层变动。

作者参考Will Larson的Staff Engineer原型，认为自己属于架构师或技术负责人，专注于长期所有权。虽然承认找到合适的团队存在运气成分，但作者坚持认为，选择留下并积累深度是一个有意识的决定。结论是，存在一种可行且有回报的替代方案，可以取代高知名度、快节奏的产品工程世界，它建立在深度、耐心和对底层基础设施的持久贡献之上。

---

## 40. 2025年的博客：向虚空尖叫

**原文标题**: Blogging in 2025: Screaming into the Void

**原文链接**: [https://askmike.org/articles/blogging-in-2025-screaming-into-the-void/](https://askmike.org/articles/blogging-in-2025-screaming-into-the-void/)

2025年的博客：向虚空呐喊

在一篇题为“2025年的博客：向虚空呐喊”的2025年博客文章中，作者反思了独立博客的衰落以及向中心化社交媒体平台的转变。作者感叹人工智能正在改变互联网使用方式，它汇总来自各种来源的信息，可能导致个人博客的相关性降低。付费新闻通讯和付费内容的兴起也促成了“开放网络”的衰落，因为高质量的内容转移到了付费墙后面。

尽管存在这些挑战，作者仍表达了对回归博客的怀旧渴望。他们回顾了维护两个博客的历史，一个是科技博客，一个是旅行/摄影博客，以及他们从自定义CMS到静态网站的迭代博客软件方法。

作者随后探讨了使用人工智能编码工具，不是为了创建一个新的、复杂的博客，而是为了简化他们现有的博客软件。目标是通过删除跟踪器、第三方依赖项并简化HTML/CSS结构，来创建最小化、对开放网络友好的体验。作者已将一个博客迁移到简单的静态站点生成器，并计划在GitHub上发布代码。

最终，尽管在当前的在线环境中读者很少，作者还是回归了博客。作者承认，在没有任何跟踪的情况下，写作博客可能感觉像“向虚空呐喊”，但他们仍然在继续，这是受到为开放网络做出贡献的愿望驱动。

---

## 41. Show HN: Onlyrecipe 2.0 – 我添加了 HN 要求的所有功能 – 4 年后

**原文标题**: Show HN: Onlyrecipe 2.0 – I added all features HN requested – 4 years later

**原文链接**: [https://onlyrecipeapp.com/?url=https://www.allrecipes.com/turkish-pasta-recipe-8754903](https://onlyrecipeapp.com/?url=https://www.allrecipes.com/turkish-pasta-recipe-8754903)

此“Show HN”帖子宣布发布 OnlyRecipe 2.0，一款用于保存、整理和打印喜爱食谱的工具。作者提到这是一个重大更新，专门针对 Hacker News 社区*四年前*提出的功能要求。虽然提供的文本中未列出具体功能，但 OnlyRecipe 的核心功能保持不变：帮助用户有效地管理他们的食谱收藏。该帖子很可能旨在征集 HN 社区对更新版本的反馈，并展示作者对过去建议的响应。

---

## 42. Go、Rust、Zig的思考

**原文标题**: Thoughts on Go vs. Rust vs. Zig

**原文链接**: [https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/](https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/)

本文比较了 Go、Rust 和 Zig 三种语言，不是比较其功能，而是比较每种语言所体现的价值观和设计理念。作者通过对每种语言的实践，形成了对其优缺点的看法。

Go 的特点是极简主义，追求简洁性和可读性，即使以样板代码为代价。它被描述为“现代 C”，专为企业协作而设计，优先考虑稳定性和易于理解，即使在并发代码中也是如此。Go 牺牲了复杂的功能，以换取简单性和易用性。

相比之下，Rust 拥抱的是最大化主义，旨在实现“零成本抽象”，但具有很高的复杂性。其主要目标是安全（内存安全和避免未定义行为）和性能。Rust 通过复杂的类型系统和编译时检查来实现安全，要求开发者明确代码的预期行为。语言的复杂性是其对这些安全和性能保证的直接结果。

Zig 被认为是 Go 和 Rust 的一种反思，为程序员提供了更多的控制权和自由度。它强调手动内存管理和面向数据的设计，鼓励开发者以更大的块来管理内存，而不是将分配与单个对象绑定。Zig 优先考虑控制权和对内存的直接操作。文章总结说，Zig 不仅仅是关于简单性，而是关于从根本上重新思考面向对象编程，并推广一种不同的软件设计方法。

---

## 43. Uncloud - 无需 k8s 的跨服务器容器化应用部署工具

**原文标题**: Uncloud - Tool for deploying containerised apps across servers without k8s

**原文链接**: [https://uncloud.run/](https://uncloud.run/)

Uncloud提供了一种无需依赖 Kubernetes 即可跨多个服务器部署容器化应用程序的解决方案。这种方法强调用户控制和可预测性。用户可以完全控制自己的服务器和数据，从而实现可预测的成本，而这些成本不与按请求定价模式挂钩。此外，Uncloud 避免了供应商锁定和平台依赖性，允许用户保持灵活性并可能更轻松地迁移其部署。最后，该工具允许传统的 SSH 访问，使开发人员能够利用标准调试工具和工作流程。本质上，Uncloud 提供了一种比 Kubernetes 更简单的方法来部署容器化应用程序，同时优先考虑控制、成本可预测性和开放性。

---

## 44. 是时候解放 JavaScript 了 (2024)

**原文标题**: It’s time to free JavaScript (2024)

**原文链接**: [https://javascript.tm/letter](https://javascript.tm/letter)

本文认为，甲骨文应放弃JavaScript商标，理由是该商标因未使用而实际上已被放弃，并已成为通用名称。作者认为，尽管甲骨文自2009年收购Sun Microsystems以来一直持有该商标，但甲骨文并未在与其特定产品相关的方面有意义地使用该商标，因此未能满足商标法“使用即保有”的原则。尽管甲骨文的GraalVM和JET使用了JavaScript，但这些使用被认为不足以构成真正的商标使用。

此外，本文断言JavaScript已经成为一个通用名称，这可以通过它在独立于甲骨文的整个行业中的广泛使用来证明。由于甲骨文拒绝将“JavaScript”名称发布给标准机构，因此标准化的语言规范被称为ECMAScript，进一步突显了这种通用化。作者指出，与JavaScript相关的社区组织甚至会议都必须避免使用该语言的名称，以避免潜在的法律挑战，这非常荒谬。

本文敦促甲骨文自愿将该商标释放到公共领域。如果做不到这一点，作者计划向美国专利商标局提交注销申请，并正在寻求法律援助。他们还鼓励读者签署一封公开信，以表示对他们事业的支持。核心信息是，该商标正在造成不必要的混乱和干扰，现在是时候将JavaScript视为通用名称了。

---

## 45. 使用 git rebase --onto 的堆叠式差异

**原文标题**: Stacked Diffs with git rebase —onto

**原文链接**: [https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/](https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/)

本文阐述了如何使用 Git 有效地利用“堆叠式差异”（或堆叠式 PR），重点讲解 `git rebase --onto` 命令。堆叠式差异涉及将大型功能分解为更小的、相互依赖的 PR，从而提高审查速度和质量。

解决的核心问题是当基础分支（例如，`main` 或父功能分支）更新时，如何保持依赖分支的同步。 常规的 `git rebase` 可能会导致下游分支中出现重复提交和冲突。

`git rebase --onto` 通过精确控制要移动哪些提交以及将它们放置在哪里来解决这个问题。 本文提供了一个循序渐进的指南，使用“标记分支”（例如，`feature-2-base`）来跟踪依赖分支的原始基础。 该过程包括：

1. 将基础分支（例如，`feature-1`）变基到 `main` 上。
2. 使用 `git rebase --onto feature-1 feature-2-base feature-2` 来仅重放 `feature-2` 上 *在* `feature-2-base` *之后* 的提交到新变基的 `feature-1` 上。
3. 更新标记分支 (`git branch -f feature-2-base feature-1`) 以指向更新后的基础分支。 这对于后续同步至关重要。

本文还介绍了在使用交互式变基 (`git rebase -i main`) 将功能分支的基础分支合并到 main 中后，如何清理功能分支的历史记录以删除不必要的提交。 最后，它承认了堆叠式差异增加了复杂性，但认为当正确完成时，更小、更易于审查的 PR 的好处超过了开销，并强调了维护标记分支和限制堆栈深度的重要性。 命令 `git push --force-with-lease` 将在此工作流程中经常使用。

---

## 46. 基于快速三元语法代码搜索

**原文标题**: Fast trigram based code search

**原文链接**: [https://github.com/sourcegraph/zoekt](https://github.com/sourcegraph/zoekt)

Zoekt是一个快速的、基于三元语法的文本搜索引擎，专为源代码设计。它支持子字符串和正则表达式匹配，并具有丰富的查询语言，包括布尔运算符。Zoekt可以搜索单个仓库或大型代码库，并使用代码相关的信号（如符号匹配和语法解析）对结果进行排序。

使用Zoekt主要有两种方式：通过命令行工具进行索引和搜索，以及通过索引服务器和Web服务器来同步仓库并提供Web UI或API进行搜索。

命令行用法允许索引本地Git仓库或目录。索引服务器可自动索引来自GitHub等代码托管平台的远程仓库，并定期获取和重新索引。Web服务器提供了一个简单的搜索UI和一个JSON API，具有流式结果、替代评分和上下文行等高级功能。它还公开了一个用于结构化查询的gRPC API。

---

## 47. Tunnl.gg

**原文标题**: Tunnl.gg

**原文链接**: [https://tunnl.gg](https://tunnl.gg)

Tunnl.gg 提供了一种将本地服务器 (localhost) 暴露到互联网的简单方法。这允许开发者和用户从任何有互联网连接的地方访问他们本地运行的应用程序、网站或服务。这对于各种场景都很有用，包括：

*   **测试和展示：** 无需将工作中的 Web 应用程序或 API 部署到公共服务器，即可轻松与客户、合作者或测试人员共享。
*   **Webhooks：** 在本地机器上接收来自外部服务的 Webhooks，用于开发和测试。
*   **远程访问：** 授予某人远程临时访问本地服务或应用程序的权限。

tunnl.gg 的核心优势在于其易用性。虽然没有详细说明具体机制，但暗示它简化了设置端口转发、配置防火墙或处理动态 IP 地址的复杂过程，这些通常涉及使本地服务器可从外部访问。标语强调了实现此目标的“最简单方法”。本质上，tunnl.gg 抽象掉了底层复杂性，使其能够被具有不同技术水平的用户访问。

---

## 48. PGlite – 可嵌入的Postgres

**原文标题**: PGlite – Embeddable Postgres

**原文链接**: [https://pglite.dev/](https://pglite.dev/)

PGlite：一个轻量级的、可嵌入的Postgres版本，它使用WebAssembly (WASM)构建。其主要卖点是体积小——gzip压缩后小于3MB——非常适合直接嵌入到应用程序中。这为使用熟悉且强大的Postgres数据库引擎进行本地数据存储和操作开辟了可能性，尤其是在不实用或不希望使用完整Postgres服务器的环境中，例如客户端应用程序或资源受限的环境。本质上，PGlite通过提供一个完整但高度紧凑的数据库服务器版本，将Postgres的强大功能带到了更小的设备和更多样化的平台。

---

## 49. 启动 HN：浏览器伙伴 (YC W24) – 一个互联网写作的推荐系统

**原文标题**: Launch HN: Browser Buddy (YC W24) – A recommendation system for Internet writing

**原文链接**: [https://www.browserbuddy.com/](https://www.browserbuddy.com/)

浏览器伙伴将在 Hacker News 上发布 (Launch HN)。它被描述为写作的“为你推荐”页面，一个旨在发现互联网上最好的文章和博客的推荐系统。本质上，它是一个互联网写作发现工具。

---

## 50. 正在改写欧盟人权和气候法的美国污染企业

**原文标题**: The US polluters that are rewriting the EU's human rights and climate law

**原文链接**: [https://www.somo.nl/the-secretive-cabal-of-us-polluters-that-is-rewriting-the-eus-human-rights-and-climate-law/](https://www.somo.nl/the-secretive-cabal-of-us-polluters-that-is-rewriting-the-eus-human-rights-and-climate-law/)

无法访问文章链接。

---

## 51. Ghostty 现在是非营利组织了

**原文标题**: Ghostty is now non-profit

**原文链接**: [https://mitchellh.com/writing/ghostty-non-profit](https://mitchellh.com/writing/ghostty-non-profit)

米切尔·桥本宣布，终端及终端相关技术项目Ghostty现已成为Hack Club（一家注册的501(c)(3)组织）的财政赞助非营利组织。此举旨在确保Ghostty保持免费和开源，为超越桥本个人参与的可持续发展铺平道路，并提供法律保护。

成为非营利组织的原因包括确保Ghostty的可持续未来，防止对资金滥用的担忧，以及在法律上将Ghostty与其公共利益使命联系起来。新的结构禁止将资金用于私人利益或出售/重新利用该项目以获取商业利益。

从技术角度来看，Ghostty不会发生任何变化，团队将继续致力于GUI版本和libghostty的开发。Ghostty现在可以在美国接受免税捐款。该项目将使用捐款来补偿贡献者，支持上游依赖项，资助社区活动，并通过公开账本以完全透明的方式支付运营成本。所有适用的知识产权已转让给Hack Club。桥本仍然是项目负责人，拥有最终决策权。

7%的捐款将用于Hack Club，以支付行政费用并支持其赋能年轻人在技术领域发展的使命。桥本及其家人还亲自向Hack Club捐赠了15万美元。文章鼓励捐款以支持Ghostty的开发，并提到未来将提供有关资金目标和预算的关键细节。

---

## 52. Valve 披露其为推动 Windows 游戏登陆 Arm 架构的幕后推手

**原文标题**: Valve reveals it’s the architect behind a push to bring Windows games to Arm

**原文链接**: [https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais](https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais)

Valve助力Windows游戏在Arm设备上运行，无需开发者移植

---

## 53. 印地赛车和F1赛车的区别

**原文标题**: The differences between an IndyCar and a F1 car

**原文链接**: [https://www.openwheelworld.net/en/indycar101/76/IndyCar_vs_Formula_1_cars](https://www.openwheelworld.net/en/indycar101/76/IndyCar_vs_Formula_1_cars)

本文详细介绍了印地赛车和一级方程式赛车之间的主要区别，重点阐述了它们在设计、技术和理念上的差异。虽然两者都是开轮式方程式赛车系列，但一级方程式赛车优先考虑技术创新和极限性能最大化，而印地赛车则强调车手技术和耐用性，尤其是在椭圆赛道上。

主要区别包括：

*   **底盘：** 一级方程式车队设计和制造自己的底盘，而印地赛车使用标准化的Dallara底盘。
*   **下压力：** 一级方程式赛车产生明显更高的整体下压力，从而实现更快的过弯速度，而印地赛车则侧重于底盘下压力以促进更激烈的比赛，并且更多地依赖车手技术。
*   **引擎：** 两者都使用混合动力涡轮增压引擎，但一级方程式引擎更强大（800-850马力 vs. 650-700马力），具有更高的RPM限制，并使用更高的涡轮增压。
*   **轮胎：** 一级方程式赛车使用更柔软的倍耐力轮胎以实现最大抓地力和速度，而印地赛车则采用更坚硬的普利司通轮胎，优先考虑耐用性，这在椭圆赛道上尤其重要。
*   **重量：** 由于更坚固的结构和使用气动挡风板，印地赛车比一级方程式赛车更重。
*   **刹车：** 一级方程式刹车旨在实现最佳性能并经常更换，而印地赛车刹车更耐用但效果较差。
*   **研发：** 一级方程式允许广泛的车队研发，从而在整个赛季中获得显著的性能提升。印地赛车的研发机会有限，主要集中在减震器上。

因此，正如历史单圈时间比较所显示的那样，一级方程式赛车在公路赛道上明显更快。印地赛车注重车手技术、耐用性和更激烈的比赛，这与一级方程式赛车强调突破技术界限形成对比。

---

## 54. PyTogether：教师/学生协作式轻量级实时Python IDE

**原文标题**: PyTogether: Collaborative lightweight real-time Python IDE for teachers/learners

**原文链接**: [https://github.com/SJRiz/pytogether](https://github.com/SJRiz/pytogether)

PyTogether：一款面向初学者和教育用途的浏览器端协作式Python IDE，侧重于简洁易用，而非传统IDE中的高级功能。它无需安装、配置和复杂的UI，提供即时设置环境。主要功能包括实时协作编辑、通过手动登录或Google OAuth进行安全身份验证、项目组织、可共享的代码片段、实时绘图、实时光标、聊天、语音通话和代码检查。

PyTogether基于Django、React、Y.js和Pyodide等技术构建，强调学习、教学和结对编程，使其适用于课堂和编程俱乐部。虽然存在其他的在线IDE，但PyTogether凭借其面向初学者的设计、即时设置和实时协作功能脱颖而出，提供安全且专注的学习空间。该平台未针对大规模生产开发进行优化。

在本地设置PyTogether需要Docker和Node。使用`npm install`和`npm run dev`，您可以轻松安装所有依赖项并运行后端和前端。提供了用于测试目的的示例超级用户帐户。

---

## 55. Django 6
姜戈 6

**原文标题**: Django 6

**原文链接**: [https://docs.djangoproject.com/en/6.0/releases/6.0/](https://docs.djangoproject.com/en/6.0/releases/6.0/)

Django 6.0于2025年12月3日发布，引入了多项新特性和变更，从Django 5.2或更早版本升级需注意。它支持Python 3.12、3.13和3.14，并停止支持Python 3.10和3.11。建议第三方应用程序停止支持5.2之前的Django版本。

主要新特性包括：

*   **内容安全策略（CSP）支持：** 内置工具，通过中间件、上下文处理器和策略配置设置，防止内容注入攻击。
*   **模板片段：** 引入`{% partialdef %}`和`{% partial %}`标签，用于可重用的模板片段。
*   **后台任务：** 内置框架，使用`@task`装饰器和配置的后端（主要用于开发/测试）将任务卸载到请求-响应周期之外。
*   **现代电子邮件API：** 采用Python的`email.message.EmailMessage`，实现更简洁的电子邮件处理。

其他改进涵盖管理界面、身份验证、GIS、PostgreSQL特性、静态文件管理、国际化、管理命令、迁移、模型功能（包括新的聚合函数）、分页、请求/响应处理、模板和测试。

向后不兼容的更改包括数据库后端API调整、停止支持MariaDB 10.5和低于3.12的Python版本、电子邮件API修改、将`DEFAULT_AUTO_FIELD`默认为`BigAutoField`，并要求自定义ORM表达式将参数作为元组返回。某些电子邮件API中的位置参数现已弃用。

---

## 56. Ofcom档案，第四部分：Ofcom再出击

**原文标题**: The Ofcom Files, Part 4: Ofcom Rides Again

**原文链接**: [https://prestonbyrne.com/2025/12/04/the-ofcom-files-part-4-ofcom-rides-again/](https://prestonbyrne.com/2025/12/04/the-ofcom-files-part-4-ofcom-rides-again/)

《Ofcom文件，第四部分：Ofcom再次出击》一文继续公开英国Ofcom与美国实体之间往来的系列内容。作者普雷斯顿·伯恩揭示，Ofcom再次致函美国公司4chan，声称具有域外权力，可对美国人强制执行英国审查法律。

伯恩强调，这封最新的信件是在4chan拒绝向英国政府支付罚款之后发出的。他引用了The Lunduke Journal在X（前身为Twitter）上发布的帖子，总结了情况，并指出Ofcom威胁要扩大对4chan的调查。

伯恩以一封信回应，强调4chan受美国宪法第一修正案保护，并批评Ofcom的“年龄保证”规定，他声称这些规定将摧毁在线匿名性。他还提到，可能颁布联邦版本的GRANITE法案，这是一项受Ofcom先前行为启发的外国审查保护盾法改革提案。

他表示，4chan不会在审查问题上与Ofcom合作，而是将重点放在与包括英国执法部门在内的执法部门合作，以处理儿童安全问题。他断言，4chan不受Ofcom的管辖，并重申他的立场，即英国军队需要入侵美国，才能在美国领土上执行英国法律。

伯恩表达了美国国会和白宫将采取行动保护美国实体免受外国越权行为侵害的希望，并暗示未来可能会出现外国政府无法向美国公民发送此类通知的情况。最后，他分享了Ofcom的完整信件。

---

## 57. 自闭症不应被视为单一病症。

**原文标题**: Autism should not be treated as a single condition

**原文链接**: [https://www.economist.com/science-and-technology/2025/12/03/why-autism-should-not-be-treated-as-a-single-condition](https://www.economist.com/science-and-technology/2025/12/03/why-autism-should-not-be-treated-as-a-single-condition)

无法访问文章链接。

---

## 58. 布鲁塞尔如何制定如此多的法律

**原文标题**: How Brussels writes so many laws

**原文链接**: [https://www.siliconcontinent.com/p/how-brussels-writes-so-many-laws](https://www.siliconcontinent.com/p/how-brussels-writes-so-many-laws)

路易斯·加里卡诺的文章深入探讨了欧盟卓越的立法效率，并将其与鉴于其大型联盟结构所预期的僵局进行了对比。尽管欧盟包含不同的利益，并且立法需要双重障碍，但它通过了数量惊人的法律。

关键在于激励：每个参与者都从制定立法而不是阻止立法中获益。委员会缺乏通过支出来实现政策的途径，因此将立法视为其主要的影响手段，从而扩大权限、人员和预算。

文章强调了“三方会谈”的关键作用，即议会、理事会和委员会之间的非正式谈判。这些由委员会作为“执笔人”领导的私人会议，能够促成快速妥协，但也可能导致起草错误并排除异议。

欧洲议会虽然对选民负责，但在很大程度上受到专业委员会的影响。这些委员会受特定意识形态议程的驱动，授权一小群报告员在几乎没有更广泛的议会参与的情况下谈判法律。这可能导致由狭隘多数派驱动的重大政策变化。

代表成员国的理事会，经常受到轮值主席国的压力，要求迅速达成协议，即使以牺牲理想让步为代价。委员会战略性地将提案推迟到有利的主席国，并利用六个月的轮换期。

最后，对工作人员日益增长的依赖，因新冠疫情而加速，进一步增强了常设秘书处的力量，并削弱了对于建立联盟至关重要的走廊谈话。尽管这一过程效率很高，但却产生了低质量的立法，存在重叠和矛盾，且缺乏影响评估。因此，欧盟体系优先考虑数量而非质量。

---

## 59. Show HN: Walrus - 一款用 Rust 编写的 Kafka 替代方案

**原文标题**: Show HN: Walrus – a Kafka alternative written in Rust

**原文链接**: [https://github.com/nubskr/walrus](https://github.com/nubskr/walrus)

Walrus 是一个用 Rust 编写的分布式消息流平台，提供 Kafka 的替代方案，专注于性能和容错能力。它利用高性能的日志存储引擎、基于分段的分区以及 Raft 共识来进行元数据管理，从而实现自动负载均衡和领导者轮换。

其主要功能包括一个简单的基于 TCP 的客户端协议，允许连接到任何节点，自动转发到适当的领导者，以及用于从任何副本进行历史读取的密封段。该系统构建包括用于路由的节点控制器、用于元数据共识的 Raft 引擎 (Octopii)、用于存储主题映射的集群元数据，以及使用带有写入栅栏的 Walrus 引擎的桶存储。

该平台拥有基于租约的写入栅栏，可防止脑裂写入，并拥有自动分段滚动，以分配负载。它包括一个全面的测试套件和正式的 TLA+ 规范，用于正确性验证。基准测试显示，与 Kafka 和 RocksDB 相比，它具有竞争力的写入吞吐量和带宽。

Walrus 可通过 CLI 标志和环境变量进行配置，并提供详细的文档，介绍架构、CLI 用法和系统概述。核心存储引擎也可以用作独立的 Rust 库。当前版本 (0.3.0) 引入了分布式平台功能，而早期版本 (0.2.0 和 0.1.0) 则侧重于增强核心 WAL 功能和存储引擎。

---

## 60. Show HN: MTXT – 音乐文本格式

**原文标题**: Show HN: MTXT – Music Text Format

**原文链接**: [https://github.com/Daninet/mtxt](https://github.com/Daninet/mtxt)

MTXT（音乐文本格式）是一种人类可读的、基于文本的格式，用于表示详细的音乐演奏数据，包括精确的时序、微调和表情。它优先考虑易于编辑和操作，即使是手动或借助AI辅助，避免使用二进制编码。

关键特性包括基于节拍的时序、每行一个事件的结构、对音符名称和自定义别名的支持、内置的连续参数（CC、速度）过渡、通过音分记号的微分音支持、具有时间顺序排序的灵活事件排序、MIDI兼容性和对LLM的友好性。它还支持大量的通道、自定义CC参数和元数据。

该格式使用简单的语法，用于诸如`meta`、`alias`、`note`、`cc`、`tempo`、`timesig`和`tuning`等命令。过渡允许以可自定义的曲线和时序滑动参数。提供了一个Rust库（`mtxt`）和CLI工具，用于解析、写入以及在MTXT和MIDI格式之间进行转换。

CLI工具包含诸如移调、量化、摇摆、人性化、通道过滤、指令应用/提取和排序等转换选项。该规范定义了版本控制、注释结构、时序精度和命令语法。该格式在MIT许可证下授权，版权归Dani Biró所有。

---

## 61. 人工智能现状：基于OpenRouter的100T Token实证研究

**原文标题**: State of AI: An Empirical 100T Token Study with OpenRouter

**原文链接**: [https://openrouter.ai/state-of-ai](https://openrouter.ai/state-of-ai)

我能访问互联网。以下是OpenRouter.ai上发表的“AI现状：OpenRouter的100万亿Token实证研究”文章摘要：

该文章基于OpenRouter处理的100万亿个token，对AI模型格局进行了数据驱动的分析。它揭示了OpenAI的模型，特别是GPT-4和GPT-3.5 Turbo，占据了主导地位，但其市场份额正受到日益强大的开源和专业模型的挑战。

主要发现包括：

*   **OpenAI占据主导地位，但格局正在转变：** 虽然OpenAI仍然是领导者，但随着用户探索替代方案，其市场份额正在逐渐下降。Llama 3和Mixtral是值得注意的竞争对手，正在获得越来越多的关注。
*   **价格敏感性：** 使用模式受到价格的很大影响。像GPT-3.5 Turbo这样的模型大幅降价导致了采用率的激增。相反，价格上涨会迅速将用户转移到其他选项。
*   **质量和专业化至关重要：** 在特定任务中表现出色的模型，例如代码生成（例如Claude 3 Opus）或那些表现出卓越推理能力的模型，正在吸引寻求增强性能的用户。
*   **开源的崛起：** 开源模型正变得越来越有竞争力，并且现在是许多用例的可行替代方案，尤其是在微调和量化方面取得了进展。
*   **延迟问题：** 延迟是影响模型选择的关键因素。用户通常愿意牺牲一些性能以换取更快的响应时间。
*   **模型多样性不断增长：** AI模型生态系统正在扩展，更多专业和开源选项可供选择，使开发人员能够根据其特定需求和预算定制其应用程序。

该研究强调了AI模型市场的动态性质，该市场受到价格、性能、专业化以及开源选项日益成熟的共同驱动。OpenRouter的数据为AI的当前状态以及模型采用和使用的未来趋势提供了宝贵的见解。文章表明，未来开发人员将有更多选择，并且可以根据其特定要求优化其AI解决方案。

---

## 62. 函数式四叉树

**原文标题**: Functional Quadtrees

**原文链接**: [https://lbjgruppen.com/en/posts/functional-quadtree-clojure](https://lbjgruppen.com/en/posts/functional-quadtree-clojure)

本文介绍了一种在Clojure/Clojurescript中构建四叉树的函数式方法，并将其与更常见的命令式方法进行对比。四叉树是一种树形数据结构，用于在某些数据区域集中细节，同时在其他区域节省资源。作者强调了一种声明式、易于重建的树结构，该结构针对实时可视化进行了优化。

关键的函数式方法包括：

1. 读取相机位置（焦点）。
2. 检查当前节点的大小是否基于与相机的距离达到最优。
3. 如果没有，将节点分成四个子节点并递归重复步骤 2。

作者使用 Clojure 的 `prewalk` 函数以简洁的方式实现此递归。 可视化是建立在 canvas 元素上的，随着四叉树的变化而更新，这是通过 atoms 和 watches 实现的。 为了避免闪烁，每个矩形的颜色由其中心坐标的哈希值确定，从而确保颜色一致性。 作者还提供了使用 prewalk 和 postwalk 函数的示例。

文章最后强调了四叉树在资源管理方面的优势，尤其是在 VR 等焦点区域需要高分辨率的场景中。 它赞扬了 Clojurescript 的表达能力和函数式功能，以及 Shadow-cljs 的易于部署和测试。 源代码可在 Github 上找到。

---

## 63. 查表还是枚举类型更好？

**原文标题**: What is better: a lookup table or an enum type?

**原文链接**: [https://www.cybertec-postgresql.com/en/lookup-table-or-enum-type/](https://www.cybertec-postgresql.com/en/lookup-table-or-enum-type/)

无法访问文章链接。

---

## 64. 玻利维亚重现失落的亚马逊世界

**原文标题**: A lost Amazon world just reappeared in Bolivia

**原文链接**: [https://www.frontiersin.org/news/2025/11/06/landscapes-that-remember-indigenous-peoples-thrived-amazon](https://www.frontiersin.org/news/2025/11/06/landscapes-that-remember-indigenous-peoples-thrived-amazon)

文章“玻利维亚重现失落的亚马逊世界”指向玻利维亚近期的考古发现，暗示亚马逊地区存在一个先前未知的古代文明。虽然标题承诺了这个文明的重现，但文章片段仅包含标题和一张与考古埋葬及文物相关的图片来源。此外，还有一个不相关的片段，讲述在其他地方（Nong Ratchawat）发现的4000年历史的牙齿，显示出食用精神活性槟榔的证据。

因此，仅根据所提供的信息，主要观点是玻利维亚*可能*发现了失落的亚马逊文明，这体现在考古埋葬和文物的发现上。然而，提供的文本非常有限，没有提供关于该文明、发现的性质或文物重要性的细节。根据标题，文章本身很可能详细阐述了这一初步发现。关于槟榔消费的信息完全不相关，可能来自另一篇文章。

---

## 65. 费曼大战计算机

**原文标题**: Feynman vs. Computer

**原文链接**: [https://entropicthoughts.com/feynman-vs-computer](https://entropicthoughts.com/feynman-vs-computer)

本文探讨了解析积分（使用数学技巧求解积分）和通过计算机程序进行数值逼近之间的对比。作者缺乏高级解析技巧，因此提倡使用计算方法来逼近积分，尤其是在不需要精确解的情况下。

核心思想是将积分视为对曲线下许多微小矩形面积的求和。这可以通过在积分范围内生成随机点，评估这些点上的函数值，并对结果求平均值来进行近似。作者提供了一个简单的JavaScript函数来演示这一点。

本文重点介绍了一种称为“样本单元工程”的技术，其中积分区间被分割成子区间，并且样本被策略性地分配到函数更复杂的区域，例如奇点附近。这在不增加总样本量的情况下显著提高了准确性。

作者还讨论了如何使用统计方法估算近似值中的误差，特别是基于均值的标准误差计算置信区间。这允许确定结果的可靠性，即使不知道解析解。文章提供了将计算机近似值与已知积分值进行比较的示例，表明计算机以最少的代码提供了相当准确的估计。

虽然承认数值解在某些需要函数解的科学领域中存在局限性，但作者的结论是，对于许多实际情况，计算机的近似值是充分的，并且比手动积分效率高得多。他们证明，样本的策略性分配比天真地增加样本量能够获得更好的准确性。

---

## 66. 微软因销售人员未完成指标而将人工智能销售目标削减一半。

**原文标题**: Microsoft drops AI sales targets in half after salespeople miss their quotas

**原文链接**: [https://arstechnica.com/ai/2025/12/microsoft-slashes-ai-sales-growth-targets-as-customers-resist-unproven-agents/](https://arstechnica.com/ai/2025/12/microsoft-slashes-ai-sales-growth-targets-as-customers-resist-unproven-agents/)

微软大幅下调AI销售增长目标，原因是销售人员未能完成 Foundry 等 AI 代理产品的销售配额。这些 AI 代理旨在执行自主、多步骤任务，曾是微软销售策略的核心，承诺能自动化复杂的业务流程。然而，企业不愿支付高价，并且即使 Copilot 可用，一些员工也更喜欢使用 ChatGPT 等工具。

文章指出，一个关键问题是当前 AI 代理技术的局限性。这些系统虽然有所改进，但仍然容易“虚构”或生成虚假信息，使其在关键业务任务中不可靠。它们的脆弱性源于底层 AI 模型的模式匹配限制，导致它们难以应对新情况，可能导致代价高昂的错误。通用人工智能 (AGI) 的前景解决了这个问题，因为它将使 AI 能够在没有大量先前培训的情况下学习和执行新任务。

尽管面临这些挑战，微软仍在继续大力投资 AI 基础设施，报告称资本支出创历史新高。然而，其大部分 AI 收入来自 AI 公司租赁云基础设施，而不是来自传统企业直接使用其 AI 工具。这表明微软的 AI 野心与企业目前的采用率之间可能存在脱节。文章引发了人们对潜在 AI 泡沫的担忧，微软正在为一场许多企业尚未准备好的革命建设基础设施。

---

## 67. 内存太贵了，三星都不卖给三星自己。

**原文标题**: RAM is so expensive, Samsung won't even sell it to Samsung

**原文链接**: [https://www.pcworld.com/article/2998935/ram-is-so-expensive-samsung-wont-even-sell-it-to-samsung.html](https://www.pcworld.com/article/2998935/ram-is-so-expensive-samsung-wont-even-sell-it-to-samsung.html)

由于“人工智能”热潮导致内存需求高涨、价格虚高，三星半导体公司优先供应数据中心供应商，而非其自身子公司，如三星电子的移动体验部门。 这意味着三星半导体拒绝了三星电子最初为其即将推出的智能手机提出的DRAM芯片需求，迫使手机制造部门以更高的价格重新谈判短期协议。 这种内部冲突突显了内存短缺的严重性及其对电子行业的影响。

文章强调，由于内存成本上涨，消费电子产品，特别是三星手机，很可能面临价格上涨。 这种趋势不仅限于三星，包括树莓派和联想在内的其他公司也在努力应对不断上涨的内存价格，联想甚至开始囤积内存。

TeamGroup的预测表明，这种价格飙升预计将持续到2027年，近期组件价格已经上涨了两倍。 文章强调，在这种由蓬勃发展的人工智能行业驱动的“芯片通胀”危机中，消费者在采购价格合理的电子产品方面将面临困难。

---

## 68. 2025年12月如何加速Rust编译器

**原文标题**: How to speed up the Rust compiler in December 2025

**原文链接**: [https://nnethercote.github.io/2025/12/05/how-to-speed-up-the-rust-compiler-in-december-2025.html](https://nnethercote.github.io/2025/12/05/how-to-speed-up-the-rust-compiler-in-december-2025.html)

本文总结了 2025 年下半年 Rust 编译器性能的改进，涵盖了各种贡献及其影响。重点介绍了几个 PR 的性能提升，包括对 `VecCache` 的优化、平凡常量降级（尤其有利于 `libc` crate）、移除调试代码中不必要的计算，以及改进临时作用域处理。LLVM 更新也为性能改进做出了贡献，尽管在实际耗时方面结果不一。

作者详细介绍了 Bevy 游戏引擎中显著的 proc macro 优化，这是通过使用 `-Zmacro-stats` 标志来识别和消除 `#[derive(Reflect)]` 生成的冗余代码来实现的。这导致了生成的代码大小、编译时间和内存使用量的显著减少。

文章还讨论了 `rustdoc-json` 的改进，特别是减少了内存分配，但作者认为需要一种面向性能的替代格式，以满足像 `cargo-semver-checks` 这样的重型工具的需求。Josh Triplett 的实验性标志 `-Zhint-mostly-unused` 被提及为大型 API crate 在使用受限情况下的潜在编译时胜利。文章还指出，一个秘密的 MacOS 设置可以加速 Rust 构建，这是一个意想不到的发现。

总而言之，尽管在其他指标上结果不一，但本文报告了 Rust 编译器性能在实际耗时方面略有改进。作者强调，考虑到不断涌入的新特性和 bug 修复通常会对性能产生负面影响，保持或略微提高编译器速度就是一种胜利。作者还强调了升级硬件带来的显著性能提升。

---

## 69. 逆向工程10亿美元法律人工智能工具暴露10万+份机密文件

**原文标题**: Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files

**原文链接**: [https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k](https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k)

A security researcher reverse-engineered a demo environment of Filevine, a $1 billion legal AI platform, and discovered a critical vulnerability that exposed over 100,000 confidential files. While investigating a seemingly broken subdomain (margolis.filevine.com), the researcher uncovered an unsecured API endpoint (`/prod/recommend`) that, without any authentication, provided a live, fully scoped administrator token for the law firm's entire Box filesystem.

This token granted unrestricted access to all data stored within the firm's cloud storage, including sensitive legal documents, internal memos, payroll information, and user data, potentially exposing information protected by HIPAA and court orders. The researcher emphasized the potential for significant damage, highlighting how malicious actors could have extracted all of the firm's data.

The researcher immediately reported the vulnerability to Filevine, who responded promptly and professionally, remediating the issue. They also confirmed that the incident was isolated to a single, non-production instance and didn't affect other Filevine clients. Filevine was appreciative of the responsible disclosure. The researcher praised Filevine's handling of the disclosure and used the incident to caution companies rushing into AI adoption to prioritize data security and thoroughly vet the security practices of vendors entrusted with sensitive information. The affected law firm was not Margolis PLLC.


---

## 70. Anthropic acquires Bun

**原文标题**: Anthropic acquires Bun

**原文链接**: [https://bun.com/blog/bun-joins-anthropic](https://bun.com/blog/bun-joins-anthropic)

生成摘要时出错

---

## 71. Average DRAM price in USD over last 18 months

**原文标题**: Average DRAM price in USD over last 18 months

**原文链接**: [https://pcpartpicker.com/trends/price/memory/](https://pcpartpicker.com/trends/price/memory/)

生成摘要时出错

---

## 72. Who Hooked Up a Laptop to a 1930s Dance Hall Machine?

**原文标题**: Who Hooked Up a Laptop to a 1930s Dance Hall Machine?

**原文链接**: [https://www.chrisbako.com/posts/2025-12-04-speelkok-museam](https://www.chrisbako.com/posts/2025-12-04-speelkok-museam)

生成摘要时出错

---

## 73. Building optimistic UI in Rails (and learn custom elements)

**原文标题**: Building optimistic UI in Rails (and learn custom elements)

**原文链接**: [https://railsdesigner.com/custom-elements/](https://railsdesigner.com/custom-elements/)

生成摘要时出错

---

## 74. Malicious Go Packages Impersonate Google's UUID Library and Exfiltrate Data

**原文标题**: Malicious Go Packages Impersonate Google's UUID Library and Exfiltrate Data

**原文链接**: [https://socket.dev/blog/malicious-go-packages-impersonate-googles-uuid-library-and-exfiltrate-data](https://socket.dev/blog/malicious-go-packages-impersonate-googles-uuid-library-and-exfiltrate-data)

生成摘要时出错

---

## 75. The Fat-Tailed Sheep on the First Fleet; Australia's First Sheep

**原文标题**: The Fat-Tailed Sheep on the First Fleet; Australia's First Sheep

**原文链接**: [https://www.singletonmills.com/sydney-first-sheep.html](https://www.singletonmills.com/sydney-first-sheep.html)

生成摘要时出错

---

## 76. Micron Announces Exit from Crucial Consumer Business

**原文标题**: Micron Announces Exit from Crucial Consumer Business

**原文链接**: [https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business](https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business)

生成摘要时出错

---

## 77. All the Way Down

**原文标题**: All the Way Down

**原文链接**: [https://www.futilitycloset.com/2025/11/17/all-the-way-down-2/](https://www.futilitycloset.com/2025/11/17/all-the-way-down-2/)

生成摘要时出错

---

## 78. 8086 Microcode Browser

**原文标题**: 8086 Microcode Browser

**原文链接**: [https://nand2mario.github.io/posts/2025/8086_microcode_browser/](https://nand2mario.github.io/posts/2025/8086_microcode_browser/)

生成摘要时出错

---

## 79. Unreal Tournament 2004 is back

**原文标题**: Unreal Tournament 2004 is back

**原文链接**: [https://old.reddit.com/r/unrealtournament/comments/1pdbe69/breaking_unreal_tournament_2004_is_back/](https://old.reddit.com/r/unrealtournament/comments/1pdbe69/breaking_unreal_tournament_2004_is_back/)

生成摘要时出错

---

## 80. A Cozy Mk IV light aircraft crashed after 3D-printed part was weakened by heat

**原文标题**: A Cozy Mk IV light aircraft crashed after 3D-printed part was weakened by heat

**原文链接**: [https://www.bbc.com/news/articles/c1w932vqye0o](https://www.bbc.com/news/articles/c1w932vqye0o)

生成摘要时出错

---

## 81. Why WinQuake exists and how it works

**原文标题**: Why WinQuake exists and how it works

**原文链接**: [https://fabiensanglard.net/winquake/index.html](https://fabiensanglard.net/winquake/index.html)

生成摘要时出错

---

## 82. Kea DHCP: Modern, open source DHCPv4 and DHCPv6 server

**原文标题**: Kea DHCP: Modern, open source DHCPv4 and DHCPv6 server

**原文链接**: [https://www.isc.org/kea/](https://www.isc.org/kea/)

生成摘要时出错

---

## 83. A most important mustard

**原文标题**: A most important mustard

**原文链接**: [https://www.asimov.press/p/arabidopsis](https://www.asimov.press/p/arabidopsis)

生成摘要时出错

---

## 84. Lie groups are crucial to some of the most fundamental theories in physics

**原文标题**: Lie groups are crucial to some of the most fundamental theories in physics

**原文链接**: [https://www.quantamagazine.org/what-are-lie-groups-20251203/](https://www.quantamagazine.org/what-are-lie-groups-20251203/)

生成摘要时出错

---

## 85. Japanese four-cylinder engine is so reliable still in production after 25 years

**原文标题**: Japanese four-cylinder engine is so reliable still in production after 25 years

**原文链接**: [https://www.topspeed.com/reliable-japanese-four-cylinder-engine-still-in-production/](https://www.topspeed.com/reliable-japanese-four-cylinder-engine-still-in-production/)

生成摘要时出错

---

## 86. Acme, a brief history of one of the protocols which has changed the Internet

**原文标题**: Acme, a brief history of one of the protocols which has changed the Internet

**原文链接**: [https://blog.brocas.org/2025/12/01/ACME-a-brief-history-of-one-of-the-protocols-which-has-changed-the-Internet-Security/](https://blog.brocas.org/2025/12/01/ACME-a-brief-history-of-one-of-the-protocols-which-has-changed-the-Internet-Security/)

生成摘要时出错

---

## 87. Some models of reality are bolder than others

**原文标题**: Some models of reality are bolder than others

**原文链接**: [https://cjauvin.github.io/posts/metaphysical-boldness/](https://cjauvin.github.io/posts/metaphysical-boldness/)

生成摘要时出错

---

## 88. 1D Conway's Life glider found, 3.7B cells long

**原文标题**: 1D Conway's Life glider found, 3.7B cells long

**原文链接**: [https://conwaylife.com/forums/viewtopic.php?&p=222136#p222136](https://conwaylife.com/forums/viewtopic.php?&p=222136#p222136)

生成摘要时出错

---

## 89. Help, My Java Object Vanished (and the GC Is Not at Fault)

**原文标题**: Help, My Java Object Vanished (and the GC Is Not at Fault)

**原文链接**: [https://arraying.de/posts/markword/](https://arraying.de/posts/markword/)

生成摘要时出错

---

## 90. Vanilla CSS is all you need

**原文标题**: Vanilla CSS is all you need

**原文链接**: [https://www.zolkos.com/2025/12/03/vanilla-css-is-all-you-need](https://www.zolkos.com/2025/12/03/vanilla-css-is-all-you-need)

生成摘要时出错

---

## 91. Are we repeating the telecoms crash with AI datacenters?

**原文标题**: Are we repeating the telecoms crash with AI datacenters?

**原文链接**: [https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/](https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/)

生成摘要时出错

---

## 92. The RAM shortage comes for us all

**原文标题**: The RAM shortage comes for us all

**原文链接**: [https://www.jeffgeerling.com/blog/2025/ram-shortage-comes-us-all](https://www.jeffgeerling.com/blog/2025/ram-shortage-comes-us-all)

生成摘要时出错

---

## 93. MinIO is now in maintenance-mode

**原文标题**: MinIO is now in maintenance-mode

**原文链接**: [https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2](https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2)

生成摘要时出错

---

## 94. Everyone in Seattle hates AI

**原文标题**: Everyone in Seattle hates AI

**原文链接**: [https://jonready.com/blog/posts/everyone-in-seattle-hates-ai.html](https://jonready.com/blog/posts/everyone-in-seattle-hates-ai.html)

生成摘要时出错

---

## 95. IBM CEO says there is 'no way' spending on AI data centers will pay off

**原文标题**: IBM CEO says there is 'no way' spending on AI data centers will pay off

**原文链接**: [https://www.businessinsider.com/ibm-ceo-big-tech-ai-capex-data-center-spending-2025-12](https://www.businessinsider.com/ibm-ceo-big-tech-ai-capex-data-center-spending-2025-12)

生成摘要时出错

---

## 96. 30 years ago today "Netscape and Sun announce JavaScript"

**原文标题**: 30 years ago today "Netscape and Sun announce JavaScript"

**原文链接**: [https://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html](https://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html)

生成摘要时出错

---

## 97. RCE Vulnerability in React and Next.js

**原文标题**: RCE Vulnerability in React and Next.js

**原文链接**: [https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp)

生成摘要时出错

---

## 98. Zig quits GitHub, says Microsoft's AI obsession has ruined the service

**原文标题**: Zig quits GitHub, says Microsoft's AI obsession has ruined the service

**原文链接**: [https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/](https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/)

生成摘要时出错

---

## 99. Bootloader Unlock Wall of Shame

**原文标题**: Bootloader Unlock Wall of Shame

**原文链接**: [https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame](https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame)

生成摘要时出错

---

## 100. Show HN: I built a dashboard to compare mortgage rates across 120 credit unions

**原文标题**: Show HN: I built a dashboard to compare mortgage rates across 120 credit unions

**原文链接**: [https://finfam.app/blog/credit-union-mortgages](https://finfam.app/blog/credit-union-mortgages)

生成摘要时出错

---

