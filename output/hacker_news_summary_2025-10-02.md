# Hacker News 热门文章摘要 (2025-10-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 信号协议与后量子棘轮

**原文标题**: Signal Protocol and Post-Quantum Ratchets

**原文链接**: [https://signal.org/blog/spqr/](https://signal.org/blog/spqr/)

本文宣布稀疏后量子棘轮（SPQR），它是Signal协议的增强版，旨在防御未来量子计算威胁。SPQR加强了该协议的前向保密性（FS）和泄露后安全性（PCS）保证。

原始的Signal协议使用哈希函数（量子安全）来实现FS，并使用椭圆曲线Diffie-Hellman（ECDH）交换（非量子安全）来实现PCS。SPQR通过引入量子安全密钥封装机制（KEM）来解决ECDH对量子攻击的脆弱性。

KEM的实施面临诸多挑战，包括密钥尺寸过大以及处理离线客户端、消息丢失和重排序等问题。本文探讨了诸如使用状态机协调消息发送和使用纠删码以更小的块有效传输大型密钥等解决方案，从而减轻消息丢失和恶意干扰的影响。

SPQR棘轮与原始双棘轮混合使用时，被称为三重棘轮。对于Signal用户而言，此更新是无缝的，并将最终应用于所有对话，在保持现有安全保证的同时，加强通信以防御潜在的量子计算机威胁。

---

## 2. 我们买了整个GPU，就他妈要用整个GPU。

**原文标题**: We bought the whole GPU, so we're damn well going to use the whole GPU

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main](https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main)

本文详细介绍了一种针对H100 GPU上Llama-70B模型张量并行推理的吞吐量优化型巨内核，其端到端吞吐量性能超过SGLang 22%以上。基于他们之前在Llama-1B低延迟巨内核方面的工作，作者解决了大批量Llama-70B推理的挑战，其中计算、内存带宽和GPU间通信成为瓶颈。

关键思想是重叠这些操作，以最大化GPU资源利用率。与顺序运行内核的传统方法不同，巨内核将整个前向传递融合到一个单元中，使用指令和解释器模型。前向传递被分解为细粒度的指令，由GPU上的解释器执行，从而实现积极的流水线和资源共享。

本文重点介绍了巨内核如何在多个层级上实现重叠：通过流水线化指令阶段在SM（流式多处理器）内部重叠，通过同时运行不同类型的指令在SM之间重叠，以及通过将通信与计算重叠在GPU之间重叠。一项关键创新是“分布式转置”操作，它取代了reduce-scatter，以方便O投影矩阵乘法与通信的重叠。

虽然代码面向研究且可能比较挑剔，但它通过最大化硬件资源利用率，展示了巨内核在高吞吐量推理方面的潜力。作者最后强调了他们的核心巨内核抽象在低延迟和高吞吐量领域的可迁移性。

---

## 3. 白内障手术史

**原文标题**: The history of cataract surgery

**原文链接**: [https://www.asimov.press/p/cataracts](https://www.asimov.press/p/cataracts)

本文追溯了白内障手术四千年的演变历程，从最初级的拨障术到如今高度成功的手术。白内障，即眼球晶状体的混浊，是全球失明的主要原因之一，这也使得白内障手术成为全球最常施行的外科手术。

这段历史始于《妙闻本集》(约公元前600年)中记载的拨障术，这种方法通过将混浊的晶状体移位来恢复有限的视力。虽然这种方法在几个世纪中被不同文化所采用，但它并没有移除白内障，而且常常导致视力不佳。伊斯兰世界在10世纪时有了进步，Al-Mawsili使用空心针来提取白内障。

1747年，雅克·达维尔的囊外白内障摘除术(ECCE)取得重大突破，保留了后囊并减少了并发症。塞缪尔·夏普后来提出了囊内白内障摘除术(ICCE)，即移除整个晶状体。这两种技术都使得患者成为“无晶状体眼”，需要佩戴厚厚的眼镜。

Harold Ridley在观察到二战受伤飞行员的眼睛对PMMA材料的耐受性后，产生了人工晶状体(IOL)植入这一关键创新。1949年，Ridley植入了第一枚IOL，在白内障摘除后恢复了聚焦能力。虽然最初的结果好坏参半，但它为现代白内障手术的高成功率和可及性铺平了道路，尽管更广泛的普及，特别是在低收入国家，仍然是一个挑战。

---

## 4. N8n新增了使用DataTables的原生持久化存储

**原文标题**: N8n added native persistent storage with DataTables

**原文链接**: [https://community.n8n.io/t/data-tables-are-here/192256](https://community.n8n.io/t/data-tables-are-here/192256)

N8n 将在 1.113 版本及以上的所有计划中推出数据表 (beta)，在 n8n 平台内直接提供原生持久存储。 这解决了用户长期以来希望拥有内置表格以便在工作流执行之间存储数据的需求，从而无需外部平台和凭据。

数据表使用户能够：

* 持久保存工作流运行中的数据。
* 跨多个工作流执行维护数据。
* 跟踪执行状态以防止重复运行。
* 存储 AI 工作流的可重用提示。
* 收集 AI 工作流的评估数据。
* 执行查找、合并和数据增强。

为了保持性能，默认大小限制为 50MB，可以使用 `N8N_DATA_TABLES_MAX_SIZE_BYTES` 环境变量为自托管实例调整此限制。 N8n 鼓励用户升级到 v1.113，试用数据表，并提供关于缺失功能和潜在改进的反馈。 文档已发布，可供查阅以获取更多信息。

---

## 5. 工作不是学校：如何在体制的愚蠢中生存

**原文标题**: Work is not school: Surviving institutional stupidity

**原文链接**: [https://www.leadingsapiens.com/surviving-institutional-stupidity/](https://www.leadingsapiens.com/surviving-institutional-stupidity/)

本文探讨了高成就人士从以能力为基础的学校环境过渡到职场时常遇到的挫折，职场往往充斥着非逻辑性和主观性，制度性的“愚蠢”也可能滋生。文章指出，虽然组织声称是精英体制，但接近权力、时机、认知和政治价值等因素往往发挥着重要作用。

作者建议读者将组织中的失误归因于“愚蠢”而非恶意，从而培养好奇心并防止愤世嫉俗。主要观点包括：认知通常被视为“数据”，必须有意识地进行管理；争取“客观公平”通常是浪费时间。相反，应该学习主观逻辑和不成文的规则。

文章还强调了有效定位工作的重要性，理解组织内部不同的标准和动机，以及承认更高层级存在的瓶颈。文章鼓励读者选择自己参与的“游戏”，并承担这个选择，专注于自己的控制范围，并通过工作之外的身份和社区多样化来建立平衡的“意义组合”。

最终，文章倡导理解组织内部的主观暗流，从而更巧妙地运作，不是愤世嫉俗地玩弄体制，而是积极参与、做出贡献并创造意义，同时认识到组织是不完美的，但可以改变的人类构造。

---

## 6. 两架亚马逊送货无人机在亚利桑那州托莱森商业区撞上起重机

**原文标题**: Two Amazon delivery drones crash into crane in commercial area of Tolleson, AZ

**原文链接**: [https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson](https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson)

周三上午，两架亚马逊送货无人机在亚利桑那州托勒森市96号大街和罗斯福街附近的一个商业区撞到了一台起重机。托勒森警察局正在调查这起事故。目前尚不清楚是否有人受伤。亚马逊已承认此事，并表示正在配合当局进行调查。该事件正在发展中，更多信息将在稍后更新。

---

## 7. Liva AI (YC S25) 正在招聘

**原文标题**: Liva AI (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/liva-ai/jobs/6xM8JYU-founding-operations-lead](https://www.ycombinator.com/companies/liva-ai/jobs/6xM8JYU-founding-operations-lead)

Liva AI (YC S25) 是一家致力于通过构建丰富的人类语音和视频数据资料库来实现人工智能人性化的初创公司，正在旧金山招聘创始运营负责人。该职位涉及管理数据收集项目、改进内部工作流程以及设计人/人工智能协作系统。

理想的候选人应具备高度的组织能力、强大的问题解决能力以及人员管理经验。 需对人工智能代理和数据有浓厚的兴趣，具备咨询、投资银行、产品管理或先前的人工智能代理/机器学习经验者优先。 该职位要求承诺长时间工作（每天12小时，每周6天）。

Liva AI提供具有竞争力的薪资、免费食品和设备等福利、带薪家事假，以及成为YC支持的初创公司早期成员的机会。 公司的使命是通过捕捉多样化的声音和面孔来创造更逼真的人工智能，从而解决当前通用人工智能的局限性。 Liva AI 成立于 2025 年，目前正在旧金山积极组建团队。

---

## 8. 科学家表示，自闭症不应被视为单一病因的单一疾病。

**原文标题**: Autism should not be seen as single condition with one cause, say scientists

**原文链接**: [https://www.theguardian.com/society/2025/oct/01/autism-should-not-be-seen-as-single-condition-with-one-cause-say-scientists](https://www.theguardian.com/society/2025/oct/01/autism-should-not-be-seen-as-single-condition-with-one-cause-say-scientists)

一项新研究表明，自闭症应被视为一系列不同的病症，而非具有单一根本原因的单一实体。 研究人员分析了超过45,000名自闭症患者的基因和行为数据，发现早期（6岁之前）和晚期（10岁之后）确诊的患者之间存在显著差异。

早期确诊的个体从小就表现出稳定的行为困难，包括社交互动问题，并显示出独特的基因特征。 相比之下，晚期确诊的个体在青春期经历了越来越多的社交和行为挑战，并且更有可能患有抑郁症等精神健康疾病。 他们的基因特征也更类似于患有 ADHD、抑郁症和 PTSD 的个体。

虽然科学家们并不主张设立单独的诊断类别，但他们强调，“自闭症”可能包含具有不同生物学和发育途径的多种病症。 该研究发现，早期和晚期诊断的自闭症患者的基因特征重叠程度有限。 这些发现可能有助于解释自闭症诊断率的不断上升，一些专家认为这归因于诊断标准的扩大以及对该病症的更好认知。

---

## 9. 荷兰法官：Meta 必须尊重用户对推荐系统的选择

**原文标题**: NL Judge: Meta must respect user's choice of recommendation system

**原文链接**: [https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/](https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/)

荷兰法院裁定，Meta公司因未尊重用户在Facebook和Instagram等平台上对推荐系统的选择，违反了《数字服务法案》(DSA)。该案件由数字人权组织Bits of Freedom提起，他们认为Meta的设计削弱了用户的自主权和对其信息流的控制。

法官对此表示赞同，称Meta的“非持久选择选项”与DSA赋予用户真正自主权和选择自由的目标相悖。法院认为，Meta的设计通过微妙地将用户推向最大化广告收入的基于兴趣的信息流，同时隐藏非个性化选项并限制在替代时间线内访问诸如私信之类的功能，从而严重扰乱了用户的自主权。

法院已责令Meta调整其应用程序，以确保用户的Feed偏好得以保留，即使在导航到不同部分或重新启动应用程序时也是如此。Bits of Freedom对该裁决表示欢迎，称少数美国科技公司来决定人们如何看待世界是不可接受的。Bits of Freedom承认该裁决只是迈出的一小步，并希望它能激励其他人挑战Meta的权力。

---

## 10. 大西洋量子团队加入谷歌

**原文标题**: The Atlantic Quantum team is joining Google

**原文链接**: [https://blog.google/technology/research/scaling-quantum-computing-even-faster-with-atlantic-quantum/](https://blog.google/technology/research/scaling-quantum-computing-even-faster-with-atlantic-quantum/)

谷歌量子AI收购大西洋量子团队，加速量子计算发展。

---

## 11. 启动 HN：Simplex (YC S24) – 开发者浏览器自动化平台

**原文标题**: Launch HN: Simplex (YC S24) – Browser automation platform for developers

**原文链接**: [https://www.simplex.sh/](https://www.simplex.sh/)

Simplex (YC S24) 推出一款面向开发者的浏览器自动化平台，为现代自动化任务提供基础设施，例如远程浏览器和可控网络代理。它旨在可靠地自动化与传统系统和门户的交互，这些系统和门户通常对现代集成方法构成挑战。

Simplex 已在多个领域展示了成功的自动化应用，包括：账单门户（下载发票）、预先授权门户（填写复杂表格）、ERP 系统（数据录入和报告下载）、政府门户（数据提取）以及 TMS/WMS 软件（货运管理）。

主要功能包括：用于可靠部署和扩展的生产级基础设施、代理操作缓存以实现一致的工作流程，以及为低延迟应用（如电话呼叫）创建实时流程的能力。Simplex 提供身份验证处理、可扩展的无头浏览器、隐身模式（CAPTCHA 解决和反机器人保护）、可控和优化的工作流程、Python 和 TypeScript 中的强大 SDK，以及用于会话监控和调试的详细日志记录和重放功能。该平台旨在简化浏览器自动化，使其对开发者而言更强大、更易于使用，尤其是在处理较旧或复杂的 Web 界面时。

---

## 12. 丹尼尔·斯滕贝格谈人工智能发现并修复的22个curl漏洞

**原文标题**: Daniel Stenberg on 22 curl bugs found by AI and fixed

**原文链接**: [https://mastodon.social/@bagder/115241241075258997](https://mastodon.social/@bagder/115241241075258997)

丹尼尔·斯滕贝格的 Mastodon 帖子讨论了 Joshua Rogers 的一项重要贡献：一个通过 AI 驱动分析在 curl 中发现的潜在 bug 的“巨大”列表。该帖子重点介绍了其中 22 个 AI 识别的问题被确认为真实 bug 并已修复。 虽然完整的细节可能在其他地方提供，但本段文字的关键要点是 AI 在发现和解决 curl 项目中的漏洞方面取得了成功应用。这突显了 AI 工具在提高软件安全性和可靠性方面的潜力，它可以识别传统方法可能遗漏的 bug。该帖子强调了这种合作努力的积极影响，展示了外部贡献在加强像 curl 这样的开源项目中的价值。

---

## 13. 我用Minecraft红石搭建了ChatGPT[视频]

**原文标题**: I built ChatGPT with Minecraft redstone [video]

**原文链接**: [https://www.youtube.com/watch?v=VaeI9YgE1o8](https://www.youtube.com/watch?v=VaeI9YgE1o8)

这篇“文章”本质上是一个YouTube视频标题和一些样板式的YouTube页脚文本。

关键在于，有人声称已在Minecraft中使用红石构建了一个类似ChatGPT的系统。该视频很可能演示了这个创造。

其余内容包括标准的YouTube法律和信息链接，包括版权、联系信息、创作者资源、服务条款、隐私政策以及有关Google参与的详细信息。这些与视频标题的核心主张无关。

---

## 14. 红帽证实安全事件，此前黑客声称 GitHub 遭入侵

**原文标题**: Red Hat confirms security incident after hackers claim GitHub breach

**原文链接**: [https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/](https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/)

红帽证实了一起安全事件，涉及其用于红帽咨询项目的GitLab实例遭到入侵，而非最初报道的GitHub。一个名为“猩红集团”的勒索组织声称已从28,000个内部开发代码仓库中窃取了570GB的压缩数据，其中包括大约800份客户参与报告（CER）。

CER是包含敏感客户信息的咨询文件，例如基础设施详细信息、配置数据和身份验证令牌，这些信息可能被利用来入侵客户网络。红帽承认了这起事件，并正在采取补救措施，但未证实有关被盗数据的具体说法。他们声称此次泄露不会影响其他红帽服务或产品，并对其软件供应链的完整性保持信心。

黑客声称，他们利用在被盗数据中发现的身份验证令牌和数据库URI，获得了对下游客户基础设施的访问权限。他们公布了一份被盗GitLab仓库和2020-2025年CER的目录清单，其中列出了美国银行、T-Mobile、美国海军等知名组织。

“猩红集团”试图勒索红帽，但只收到了通用回复。该组织还声称对任天堂页面的一次临时篡改负责。

---

## 15. 乒乓战役：昼夜善恶之争

**原文标题**: Pong Wars: A battle between day and night, good and bad

**原文链接**: [https://github.com/vnglst/pong-wars](https://github.com/vnglst/pong-wars)

“乒乓战争”是一款基于JavaScript的游戏，以视觉方式呈现了昼夜、善恶之间的冲突。它使用HTML和CSS构建于单个文件中，鼓励重用和修改。该项目易于使用`npx serve`运行，代码旨在保持极简和简单。

作者感谢之前的灵感来源（可能更早），并感谢Alex Cristache的Mindful Palette为游戏提供的配色。虽然欢迎通过pull request提供反馈和改进，但该项目旨在保持简洁。鼓励将扩展和替代版本作为单独的项目进行开发。

列出了一系列用各种编程语言和平台创建的“乒乓战争”的替代版本，展示了该游戏的广泛吸引力和适应性。此列表包括ASCII Python、Atari 2600、C#、C++、Flutter、Godot、Java、Rust、Scratch、SwiftUI等版本。还提供了指向宣传该游戏的原始Mastodon和Twitter帖子的链接。

---

## 16. F3：面向未来的开源数据文件格式 [pdf]

**原文标题**: F3: Open-source data file format for the future [pdf]

**原文链接**: [https://db.cs.cmu.edu/papers/2025/zeng-sigmod2025.pdf](https://db.cs.cmu.edu/papers/2025/zeng-sigmod2025.pdf)

该PDF文档似乎是一篇题为“F3：面向未来的开源数据文件格式”的文章，重点介绍了一种名为F3的新型列式存储文件格式。该文章发表于2025年ACM数据管理国际会议（SIGMOD）论文集中，可能旨在解决对更高效、可扩展和压缩的数据存储解决方案的需求。

根据嵌入的元数据，该文章由曾新宇、孟瑞君、Martin Prammer、Wes McKinney、Jignesh M. Patel、Andrew Pavlo和张焕琛撰写。探讨的关键主题包括列式存储、文件格式设计、数据压缩技术以及为适应未来数据类型和处理方法的可扩展性。

该元数据包含标准出版详情，例如DOI（10.1145/3749163）、ISSN/eISSN/ISBN（可能对应于SIGMOD论文集）和页码范围（27）。XMP元数据的存在表明其关注标准化和互操作性。提及LaTeX和hyperref表明这是一篇技术性学术文档。文档的大部分是与文档本身相关的编码和压缩数据，包括字体、图像和文章文本。

---

## 17. Gmail 将不再支持通过 POP 协议检查第三方帐户的电子邮件。

**原文标题**: Gmail will no longer support checking emails from third-party accounts via POP

**原文链接**: [https://support.google.com/mail/answer/16604719?hl=en](https://support.google.com/mail/answer/16604719?hl=en)

自2026年1月起，Gmail将停止对第三方电子邮件帐户的Gmailify和POP连接的支持。Gmailify（将Gmail的垃圾邮件防护等功能应用于其他电子邮件帐户）将不再可用。用于将其他帐户的电子邮件下载到Gmail的POP连接也将被禁用。

用户将无法再在电脑上的Gmail中使用“从其他帐户查收邮件”功能。虽然已经通过POP导入的电子邮件仍然可以访问，但无法通过此方法检索新的电子邮件。

主要的替代方案是使用仍然受支持的IMAP。用户可以通过将他们的第三方电子邮件帐户直接添加到适用于Android和iOS的Gmail移动应用来继续访问这些帐户。文章建议用户查阅其电子邮件提供商的文档以启用其帐户的IMAP。

这些变更的原因是为在Gmail中访问消息提供更安全和最新的选项。该文档还指出，工作或学校帐户的管理员可以使用Google Workspace数据迁移服务来移动电子邮件数据。

---

## 18. 药品仅占美国医疗保健支出的一小部分

**原文标题**: Pharma is a small component of US health care spending

**原文链接**: [https://www.economist.com/business/2025/10/02/does-big-pharma-gouge-americans](https://www.economist.com/business/2025/10/02/does-big-pharma-gouge-americans)

无法访问文章链接。

---

## 19. 欧盟资金流入间谍软件公司，政客要求给出答案

**原文标题**: EU funds are flowing into spyware companies and politicians demanding answers

**原文链接**: [https://www.theregister.com/2025/10/02/eu_spyware_funding/](https://www.theregister.com/2025/10/02/eu_spyware_funding/)

39名欧洲议会议员要求欧盟委员会就欧盟资金流向Intellexa、Cy4Gate、Verint和Cognyte等间谍软件公司作出解释。这些公司的技术与在欧盟内部以及人权记录不佳的国家非法监视记者、人权捍卫者和政治人物有关。

调查显示，意大利、希腊、匈牙利和西班牙等国已使用纳税人的钱来支持这些间谍软件制造商。议员们列举了具体例子，包括“地平线2020”和“欧洲区域发展基金”等项目向Innova和Movia等公司提供的资金。欧盟委员会本身也向Nexa Technologies授予了一份合同，该公司是Intellexa联盟的一部分，该联盟因参与Predator间谍软件而受到美国制裁。

议员们质疑欧盟委员会对接受欧盟资金的实体的核查流程、对间谍软件公司投资的风险评估，以及资金机制与人权和数字韧性政策的总体一致性。他们还呼吁落实PEGA调查的建议，该调查此前将间谍软件的使用称为“欧洲水门事件”，是对欧盟价值观的严重侵犯。

议员们要求对自2015年以来欧盟对间谍软件公司的补贴进行公开审查，承诺将间谍软件供应商排除在未来的欧盟资金之外，并跟进PEGA的建议。大赦国际技术部和欧洲数字权利组织（EDRi）等组织支持议员们呼吁的透明度和欧盟禁止商业间谍软件。他们批评欧盟委员会的不作为，并认为这无意中助长了全球范围内的人权侵犯行为。

---

## 20. 展示：路由追踪可视化工具

**原文标题**: Show HN: Traceroute Visualizer

**原文链接**: [https://kriztalz.sh/traceroute-visualizer/](https://kriztalz.sh/traceroute-visualizer/)

Show HN：Traceroute可视化工具

此免费在线工具旨在利用地理数据可视化网络路径。它支持标准traceroute、flyingroutes和MTR输出，允许用户分析数据包如何在互联网上传输。用户只需将traceroute输出粘贴到工具中，它会自动检测其IP地址作为起点。

然后，该工具会在表格和交互式地图上呈现结果。该表格包括跃点数、IP地址（链接到IPinfo以获取详细信息）、主机名、位置、ISP信息、数据包丢失（对于MTR）和响应时间。该地图以可视方式显示地理路径，并用绿色闪电突出显示互联网交换点 (IXP)。Flyingroutes输出显示备用路径，而MTR输出包括丢失百分比和时序统计信息，如最佳、最差和标准偏差。

该工具的主要功能包括 IXP 检测、ISP/AS 编号识别、数据包丢失突出显示和协议特定的时序分析（对于 flyingroutes）。它可用于网络故障排除、安全调查、地理路由分析以及了解网络基础设施。隐私声明指出，数据在浏览器本地处理，依赖于 IPinfo 和 PeeringDB API 分别获取位置和 IXP 数据。需要 JavaScript 才能使该工具正常运行。

---

## 21. 科马克·麦卡锡的个人图书馆

**原文标题**: Cormac McCarthy's personal library

**原文链接**: [https://www.smithsonianmag.com/arts-culture/two-years-cormac-mccarthys-death-rare-access-to-personal-library-reveals-man-behind-myth-180987150/](https://www.smithsonianmag.com/arts-culture/two-years-cormac-mccarthys-death-rare-access-to-personal-library-reveals-man-behind-myth-180987150/)

本文深入探讨了已故著名但隐居的作家科马克·麦卡锡浩瀚而引人入胜的个人图书馆。在他去世后，学者们启动了一个项目，对估计超过20000册的藏书进行编目，希望从中了解他的生活、灵感和学术追求。

该图书馆的规模以及书籍中的注释揭示了一位“天才级博学者”，其兴趣范围从量子物理学和数学到鲸鱼生物学和法国历史。作者的家，被描述为既“庄严”又“混乱无序”，收藏了汽车、男装和数量惊人的厨房用具，暗示了他的古怪之处。

学者们正在仔细检查这些书籍，寻找书页空白处的评论、笔记以及与他小说的联系。这些注释揭示了麦卡锡令人惊讶的方面，例如他对一个良性宇宙的思考以及他对哲学文本的不同意见。

该图书馆还收藏了莎士比亚《哈姆雷特》等文学作品的注释副本，这些作品影响了他的小说《萨特里》。文章还涉及麦卡锡的成长经历，据说他的父亲专横跋扈，他从小就对户外活动和各种爱好着迷。他的图书馆有望更深入地了解这位复杂而神秘的文学人物。

---

## 22. 随着Windows 10停止支持在即，Windows 7市场份额跃升至近10%。

**原文标题**: Windows 7 marketshare jumps to nearly 10% as Windows 10 support is about to end

**原文链接**: [https://www.neowin.net/news/windows-7-marketshare-jumps-to-nearly-10-as-windows-10-enters-final-weeks-of-support/](https://www.neowin.net/news/windows-7-marketshare-jumps-to-nearly-10-as-windows-10-enters-final-weeks-of-support/)

**摘要：**

Neowin的文章报道称，在Windows 10（版本21H2）官方支持结束前的几周内，Windows 7的市场份额出现了惊人的增长，达到近10%。这一增长归因于多种因素，包括一些用户可能正在切换回Windows 7，尽管它自己在2020年就已经停止了支持。尽管如此，运行不受支持的操作系统存在固有的风险，例如缺乏安全更新以及更容易受到恶意软件的攻击。

文章强调，具有讽刺意味的是，当微软准备结束对较新操作系统（Windows 10版本21H2）的支持时，相当一部分人似乎正在*远离*较新的受支持版本，而选择了一个几年前就已停止维护的平台。这表明对升级的抵制或对较新Windows版本的不满。

虽然这种增长的具体原因尚属推测，但潜在的原因包括硬件限制阻止升级、用户对Windows 7的熟悉和偏好，或组织政策延迟过渡。文章强调了用户迁移到受支持的操作系统以保证安全的重要性，并警告了继续使用Windows 7的危险性。

---

## 23. 万国千年大会第三天庭王座 (2021)

**原文标题**: Throne of the Third Heaven of the Nations' Millennium General Assembly (2021)

**原文链接**: [https://americanart.si.edu/blog/throne-james-hampton](https://americanart.si.edu/blog/throne-james-hampton)

霍华德·卡普兰的文章反思了詹姆斯·汉普顿的标志性艺术作品《万国千年第三圣殿宝座》，该作品现藏于史密森尼美国艺术博物馆（SAAM）。作者描述了他与这件作品的个人联系，欣赏其复杂性和视觉吸引力。宝座由大约180个混合媒介元素组成，其中许多是从废弃物品中回收而来，并覆盖着银色和金色箔纸。

策展人莱斯利·昂伯格强调了这件艺术作品的矛盾性质，突出了其宏伟壮丽与取材于废弃材料的卑微出身并存。汉普顿是一名看门人，根据一系列宗教幻象，花费了大约14年的时间创作了这个宝座。他甚至租了一间马车房来组装这件日益庞大的作品。

SAAM的展览包括宝座本身以及补充材料，例如汉普顿的素描黑板和一本写满了无法辨认的自创文字的书籍，从而深入了解了他的工作方法和心态。汉普顿自认为是“永恒国度特殊项目总监”和“圣詹姆斯”，呼应了圣约翰的神圣指示。汉普顿在完成这件艺术品或看到它在SAAM展出之前就去世了，但它很快成为一件受欢迎且持久的作品。文章最后引导读者观看一段视频，其中策展人昂伯格讨论了这件艺术品的创作、相关性和影响。

---

## 24. 在LLVM的RISC-V后端添加新指令

**原文标题**: Adding a new instruction to RISC-V back end in LLVM

**原文链接**: [https://blog.gustavoleite.me/llvm-riscv-instruction](https://blog.gustavoleite.me/llvm-riscv-instruction)

本文提供了一份实用的指南，介绍如何在 LLVM 编译器的 RISC-V 后端添加一条名为 "foo" 的自定义指令。它证明了修改像 LLVM 这样复杂的编译器是出人意料地易于管理的。

文章首先将 "foo" 指令定义为一种具有特定操作码 (custom-0) 和编码的 R 型指令。然后，它介绍了 TableGen，这是一种领域特定语言，在 LLVM 中被广泛用于定义记录。作者解释了如何在 `RISCVInstrInfo.td` 中使用 TableGen 定义 "foo" 指令，指定其格式、操作数和汇编助记符。这包括创建一个 RVInstR 类型的记录并填充其字段。

文章强调，LLVM 利用 llvm-tblgen 工具在构建过程中从 TableGen 记录生成 C++ 代码，从而无需手动为新指令编写 C++ 代码。

该指南继续概述了如何在 `RISCVFeatures.td` 中定义一个名为 "xdummy" 的特性标志，以启用新指令。这在 RISC-V 的模块化架构中至关重要，其中扩展被置于标志之后。文章演示了如何使用 TableGen 中的谓词将 "foo" 指令与 "xdummy" 特性相关联。

最后，作者演示了如何使用新定义的指令和特性标志编译和汇编一个简单的程序，展示了从指令定义到可执行代码的完整过程。文章最后鼓励进一步探索 LLVM 内部机制，并强调编译器定制的潜力。

---

## 25. 一个三千年前的炼铜遗址可能是了解铁起源的关键。

**原文标题**: A 3K-year-old copper smelting site could be key to understanding origins of iron

**原文链接**: [https://phys.org/news/2025-09-year-copper-smelting-site-key.html](https://phys.org/news/2025-09-year-copper-smelting-site-key.html)

本文探讨了克兰菲尔德大学的研究，该研究揭示了从青铜时代到铁器时代的过渡。对格鲁吉亚拥有3000年历史的克韦莫-博尔尼西炼铜遗址的冶金遗迹的重新分析表明，炼铜者对富铁岩石的实验可能促成了炼铁的发明。

最初的挖掘工作因存在赤铁矿和矿渣而错误地将该遗址认定为早期的炼铁地点。然而，新的研究表明，工人实际上是在炼铜，并将赤铁矿用作助熔剂以提高铜的产量。这一发现支持了铜冶炼者在发现炼铁方面发挥了重要作用的理论。

虽然铁器在青铜时代就已存在，但它们是由稀有的陨石铁制成的。提取冶金术的发展，使得能够从丰富的铁矿石中提取铁，这是一项革命性的技术进步。

内森尼尔·埃尔布-萨图洛博士强调了克韦莫-博尔尼西作为铜冶炼中有意使用铁的证据的重要性。这表明金属工人将氧化铁理解为一种独特的材料，并尝试了其特性，这是发展炼铁冶金的关键一步。现代分析技术被用于分析矿渣，以深入了解古代金属工人使用的工艺。

---

## 26. Meta 将监听 AI 对话以个性化广告

**原文标题**: Meta will listen into AI conversations to personalize ads

**原文链接**: [https://www.theregister.com/2025/10/01/meta_ai_use_informs_ads/](https://www.theregister.com/2025/10/01/meta_ai_use_informs_ads/)

Meta计划自2025年12月16日起，利用其人工智能服务（Meta AI、Facebook、Instagram、WhatsApp和Messenger）的对话来个性化内容和广告。该公司声称，这与使用用户帖子和页面点赞的数据类似，例如，聊天内容涉及徒步旅行的用户可能会看到徒步旅行靴的广告。

通知活动将于2025年10月7日开始。除了欧盟、英国和韩国的用户外，没有退出选项。Meta坚称不会使用宗教、性取向或健康等敏感话题进行个性化。文章建议用户可以通过在每次互动中包含这些话题来潜在地扰乱这一计划。

此举是在Meta对人工智能进行大量投资并且严重依赖广告收入之后进行的。2024年，Meta的1650亿美元收入中有98%来自广告，净利润为624亿美元。专家警告称，这可能会降低广告定位的透明度并混淆归因模型。Meta目前还面临一起70亿美元的集体诉讼，指控其广告覆盖范围报告存在欺诈行为。

---

## 27. 展示 HN：自闭症模拟器

**原文标题**: Show HN: Autism Simulator

**原文链接**: [https://autism-simulator.vercel.app/](https://autism-simulator.vercel.app/)

“自闭症模拟器”是一款互动式教育工具，旨在从自闭症患者的角度模拟职场体验。它旨在通过让用户体验感觉敏感、社交沟通障碍以及可能影响工作场所表现的认知差异，从而提高对自闭症患者的理解和同情。该模拟器可能利用互动场景和虚拟环境来复制常见的职场情境，突出显示自闭症患者可能面临的困难。最终目标是教育雇主、同事和其他人了解自闭症，从而营造更具包容性和支持性的工作环境。它是一种实用的方法，可以将理论理解转化为更深刻、更有影响力的学习体验。

---

## 28. Immich v2.0.0 – 首个稳定版本

**原文标题**: Immich v2.0.0 – First stable release

**原文链接**: [https://github.com/immich-app/immich/discussions/22546](https://github.com/immich-app/immich/discussions/22546)

本文宣布 Immich 稳定版 v2.0.0 发布，这是一个开源、自托管的照片和视频管理解决方案，标志着经过约 1337 天的开发和广泛的社区支持后，迎来了一个重要的里程碑。稳定版的发布意味着技术债务的减少、兼容性的优先考虑以及更简便的更新。新网站也伴随此次发布上线，并且移除了“警告横幅”。

为了庆祝，Immich 将发布一张包含可启动实例和精选照片的实体 DVD，可在其商品商店购买，该 DVD 具有复古设计和服务器/客户端产品密钥。

未来的计划包括完成路线图项目，如自动堆叠和 Web 与移动应用程序之间的功能对等，改进堆栈支持、共享、群组管理和所有权功能。Immich 还计划实施透明的使用数据收集，并推出付费的、端到端加密的异地备份和恢复服务。

本文还包含一个常见问题解答，其中涉及持续备份的必要性、v2.0.0 的发布时间表、更新过程、版本控制策略和移动应用程序兼容性等主题。

Immich 团队对社区的支持表示感谢。计划于 2025 年 10 月 2 日 UTC 时间下午 6 点举行现场问答环节。文章还重点介绍了最近版本中的性能改进，包括优化的缩略图管道、减少的内存使用以及资源问题的修复。

---

## 29. 构建堆：为预训练安装30拍字节硬盘

**原文标题**: Building the heap: racking 30 petabytes of hard drives for pretraining

**原文链接**: [https://si.inc/posts/the-heap/](https://si.inc/posts/the-heap/)

该公司自建30PB存储集群，用于视频数据机器学习模型预训练，与云存储方案相比，显著节省成本。他们发现AWS和Cloudflare等云选项由于冗余和可用性功能，价格过于昂贵，而这些功能对他们的训练数据来说是不必要的。通过在旧金山租用托管空间并堆叠自己的硬件，他们将存储成本从AWS上估计的每年1200万美元降低到35.4万美元。

该集群由2400个硬盘驱动器组成，安装在NetApp机箱中，并通过高速网络连接到CPU头节点。软件是一个简单的Rust脚本用于写入数据，以及一个nginx web服务器用于读取，避免了Ceph或MinIO等复杂解决方案。

文章重点介绍了成本明细，一次性支出总计426,500美元（包括硬盘驱动器、机箱、计算和数据中心设置），每月经常性支出为17,500美元，用于互联网和电力。他们将1美元/TB/月的成本与AWS的38美元/TB/月和Cloudflare的10美元/TB/月进行了比较。

作者强调了简单性的重要性、高质量的电缆管理，以及在本地构建数据中心以便于调试的好处。他们还分享了经验教训，包括避免菊花链网络节点以及网络中品牌兼容性的重要性。文章最后提供了一个复制其设置的指南，包括硬件建议和网络配置。

---

## 30. 特斯拉Robotaxi七月在奥斯汀发生3起事故，隐瞒详情

**原文标题**: Tesla Robotaxi Reports 3 Crashes in Austin in July, Hides Details

**原文链接**: [https://www.forbes.com/sites/bradtempleton/2025/09/18/tesla-robotaxi-reports-3-crashes-in-austin-on-july-1-details-hidden/](https://www.forbes.com/sites/bradtempleton/2025/09/18/tesla-robotaxi-reports-3-crashes-in-austin-on-july-1-details-hidden/)

福布斯文章报道称，特斯拉在得克萨斯州奥斯汀的Robotaxi试点项目启动后不久，于7月发生了三起事故。作者表示担忧，因为车辆内有“安全监控员”（一名坐在乘客座位上，可以接触紧急停止按钮和方向盘的安全驾驶员），这应该会显著降低事故风险。

特斯拉向联邦政府提交的报告中删减了关于这些事故的关键细节，理由是专有信息。现有细节显示：一起是停车时的追尾事故（可能不是特斯拉的责任），一起是以8英里/小时的速度撞上静止物体导致轻微受伤且车辆被拖走的事故，还有一起可能是右转时与一辆SUV发生的碰撞。考虑到较低的里程（7,000-25,000英里）以及安全驾驶员的存在，撞击静止物体的事故尤其令人担忧。

作者将特斯拉的删减报告与Waymo、Zoox和May的报告进行了对比，后者的报告提供了完整的细节。虽然Waymo也报告了许多事故，但他们的行驶里程明显更多，并且通常在这些事故中没有过错。这篇文章对特斯拉的删减做法提出了质疑，并表明特斯拉需要显著提高其安全记录，才能与Waymo等竞争对手相匹配。文章还指出可能发生了第四起事故，因其可能发生在私人财产上且仅造成轮胎痕迹而未被列出，突显了缺乏透明度。作者表示担忧，并希望8月份的报告能更加干净。

---

## 31. Unix哲学和文件系统访问让Claude Code表现出色。

**原文标题**: Unix philosophy and filesystem access makes Claude Code amazing

**原文链接**: [https://www.alephic.com/writing/the-magic-of-claude-code](https://www.alephic.com/writing/the-magic-of-claude-code)

诺亚·布里尔的文章强调了Claude Code作为自主操作系统所具有的变革力量，尤其是在与Unix哲学和文件系统访问相结合时。他认为，Claude Code之所以卓越，是因为它能够利用简单、文档完善的Unix命令以及与文件系统的直接交互，从而克服了其他人工智能工具（如ChatGPT和基于浏览器的Claude）的局限性。

Unix哲学注重简单、可组合的工具，可以将输出“管道”传输到输入，这与LLM理想地利用工具的方式完美契合。文件系统访问的关键补充使Claude Code能够保持记忆，积累知识，并在单次对话之外运作，有效解决了上下文窗口大小和缺乏状态的限制。

布里尔强调，Claude Code的力量不仅仅在于其编码能力，还在于其构建新应用程序的潜力。他引用了他的“Claudesidian”项目（将Claude Code与Obsidian笔记集成）和他即将推出的“Inbox Magic”项目（一个利用Gmail工具的电子邮件EA）作为例子。这些项目通过使用简单、可组合的工具（旨在做好一件事并协同工作）来体现Unix哲学。

他最后倡导在LLM中广泛采用文件系统访问，重申Claude Code的蓝图——文件系统+Unix哲学——为构建未来的AI代理提供了一个可靠且可调试的模板。关键在于保持工具交互的简单性，并使主模型能够有效地进行线程处理和管道传输。

---

## 32. 在 Apple Silicon 上实践 Linux 桌面 (2022)

**原文标题**: Linux Desktop on Apple Silicon in Practice (2022)

**原文链接**: [https://gist.github.com/akihikodaki/87df4149e7ca87f18dc56807ec5a1bc5](https://gist.github.com/akihikodaki/87df4149e7ca87f18dc56807ec5a1bc5)

本文详细介绍了作者于 2022 年在 Apple Silicon (M1) MacBook Air 上运行 Linux 桌面环境的经验。当时，由于 Corellium 和 Asahi Linux 等现有解决方案在图形加速方面不足以满足实际桌面使用的需求，作者选择修改 QEMU 以利用 Virgil 3D 进行 OpenGL 加速。

作者概述了对 QEMU 的 Cocoa UI 和 coreaudio 所做的具体修改，以及对 Virgil 3D 渲染器的改进，重点关注 OpenGL ES 支持。他们提供了一份 DIY 指南，参考了 knazarov 的 Homebrew Formulae，并详细介绍了安装必要依赖项、创建虚拟磁盘镜像、下载 Fedora Silverblue ISO 以及执行运行脚本以启动系统的步骤。该指南还包括有关更新系统和选择不同 OpenGL 配置文件的说明。

作者承认，由于缺乏图形加速的进程隔离，QEMU 修改是不安全的。他们讨论了使用 vhost-user-gpu 的可能性，但由于其依赖于 Linux 特定的功能而尚未实现。

尽管存在安全问题，但作者发现这种虚拟化方法实用且高效，提供了可接受的性能以及与 macOS 功能（如触控板手势和 VirtFS）的集成。然而，他们承认资源分配的复杂性，并认为像 Asahi Linux 这样的原生 Linux 移植是最佳的长期解决方案。作者正在积极地向上游 QEMU、Epoxy 和 Virgil 3D 渲染器项目贡献他们的修改。

---

## 33. RAG讣告：被代理杀死，被上下文窗口埋葬

**原文标题**: The RAG Obituary: Killed by agents, buried by context windows

**原文链接**: [https://www.nicolasbustamante.com/p/the-rag-obituary-killed-by-agents](https://www.nicolasbustamante.com/p/the-rag-obituary-killed-by-agents)

在本文中，Nicolas Bustamante 认为，过去三年主导人工智能领域的检索增强生成 (RAG) 系统，正因大型语言模型 (LLM) 中不断扩展的上下文窗口和基于代理的架构的兴起而逐渐过时。

RAG 的出现是为了解决早期 LLM 无法处理大型文档的局限性。它涉及将文档分块、嵌入这些块、根据用户查询检索相关块，并将它们提供给 LLM 进行综合。然而，这种方法面临着诸如上下文碎片化、数字语义搜索失败、缺乏因果理解、词汇不匹配和时间盲点等挑战。为了缓解这些问题，引入了混合搜索（结合语义和关键词搜索）和重排序，但它们增加了复杂性、延迟和成本。

Bustamante 强调了 RAG 中的“级联失败问题”，即分块、嵌入、检索、融合或重排序中的错误会相互叠加。他将此与 Anthropic 的 Claude Code 使用的基于代理的搜索方法进行对比，后者利用诸如 `grep` 和 `glob` 之类的直接文件系统工具来调查代码库，而无需分块或嵌入。由于假设 LLM 将变得上下文丰富，因此这种方法更快、更有效。

文章强调，上下文窗口的爆炸式增长，例如 Gemini 2.5 能够处理数百万个 tokens，使得 LLM 能够直接加载整个文档并在无需 RAG 复杂检索管道的情况下导航信息。随着注意力机制的改进，LLM 可以保持跨越大量上下文的连贯性，从而使 RAG 的分块、嵌入和重排序变得不必要。

---

## 34. OpenAI 估值达 5000 亿美元

**原文标题**: OpenAI Valuation Hits $500B

**原文链接**: [https://www.wsj.com/tech/ai/openai-valuation-hits-500-billion-while-altman-signs-more-deals-in-asia-59b47a0d](https://www.wsj.com/tech/ai/openai-valuation-hits-500-billion-while-altman-signs-more-deals-in-asia-59b47a0d)

无法访问文章链接。

---

## 35. Keyhive – 本地优先的访问控制

**原文标题**: Keyhive – Local-first access control

**原文链接**: [https://www.inkandswitch.com/keyhive/notebook/](https://www.inkandswitch.com/keyhive/notebook/)

Keyhive 旨在解决本地优先应用中的访问控制难题。与传统的云端系统不同，本地优先应用需要重新思考认证机制，因为每个用户都拥有数据的完整副本。诸如“隐蔽式安全”（依赖于秘密文档 ID）或通过云服务器路由更新等现有方法并不充分。其目标是创建一个既安全高效的本地优先认证系统，又能提供类似于流行协作平台的用户体验。

文章强调了清晰直观的访问控制行为的重要性，尤其是在并发和潜在冲突的情况下，例如惊喜派对或法律文件。与可以合并数据但会引入语义错误的 CRDT 不同，访问控制需要可靠，即使在并发编辑的情况下也能防止未经授权的访问。

Keyhive 旨在结合自认证的简洁性、中心化认证服务器的强大功能以及去中心化解决方案的用户代理。这涉及到跟踪谁在文档历史的哪个时间点有权执行什么操作，从而实现撤销和精细控制（读与写）等功能，即使在断开连接后也能生效。该项目建立在现有研究和系统（如 Causal TreeKEM、UCAN 和 Web Native File System）之上，力求打造下一代本地优先访问控制解决方案。

---

## 36. 盗版运营者出狱一月后入职科技独角兽公司

**原文标题**: Piracy Operator Goes from Jail to Getting Hired by a Tech Unicorn in a Month

**原文链接**: [https://torrentfreak.com/sports-piracy-operator-goes-from-jail-to-getting-hired-by-a-tech-unicorn-in-a-month/](https://torrentfreak.com/sports-piracy-operator-goes-from-jail-to-getting-hired-by-a-tech-unicorn-in-a-month/)

25歲阿根廷人阿莱霍·瓦莱斯（网名“Shishi”）因运营盗版网站Al Ángulo TV于八月被捕，该网站据称每月有数百万用户。西班牙足球联赛西甲协助了逮捕。尽管指控严重，瓦莱斯仍获得了朋友和家人的支持，他们甚至为他的辩护发起了一项筹款活动。

瓦莱斯入狱后，与被指控犯有重罪的人同处一室，三天后获准保释。他继续控制Al Ángulo TV的X账户，逮捕后获得了数千名粉丝，并表示他将继续在社交媒体上工作。当局没收了他的手机、电脑和一个加密货币钱包，瓦莱斯声称其中只有263美元。

最令人惊讶的是，尽管面临调查且有前科，瓦莱斯还是被9z Globant聘用，这是一家由阿根廷科技独角兽公司Globant支持的专业电子竞技队伍。讽刺的是，Globant曾与西甲合作监测直播体验。9z Globant认为瓦莱斯与他之前的活动无关，可以为团队做出积极贡献。瓦莱斯本人充满信心地接受了这一新角色，并自称是“偶像”和“GOAT”。

---

## 37. Edge264 – 极简高性能H.264/AVC视频软件解码器

**原文标题**: Edge264 – Minimalist, high-performance software decoder for H.264/AVC video

**原文链接**: [https://github.com/tvlabs/edge264](https://github.com/tvlabs/edge264)

Edge264是一款极简、高性能的H.264/AVC视频软件解码器，目前正在开发中，旨在集成到GStreamer/VLC。它支持高达6.2级的逐行高级和MVC 3D配置文件，高达8K UHD分辨率，以及8位4:2:0平面YUV输出。支持的功能包括切片、多线程、每切片参考列表、内存管理控制和长期参考帧。

该解码器用C语言编写，利用128位向量扩展和内部函数，兼容Windows、Linux和macOS在x86、x64和ARM64架构上的运行。它可以使用GCC或Clang编译，并可选择使用SDL2支持通过`edge264_test`进行显示。编译选项允许针对特定的x86-64微架构进行调优并启用日志记录。

`edge264_test`程序允许解码并将输出与YUV文件进行比较。本文提供了用于解码Annex B格式文件并输出解码帧的示例代码。该API由一小部分函数组成，用于分配、解码、帧检索和释放。

Edge264采用了各种编程技术进行优化，包括单头文件组织、代码块代替函数、树形分支、默认邻近值、寄存器饱和SIMD和活塞缓存的比特流读取器。未来的开发包括持续的压力测试、错误恢复、与多媒体框架集成以及支持其他格式和架构。正在使用自定义比特流编写器开发一套测试。

---

## 38. 为何今日人形机器人难以学会灵巧

**原文标题**: Why today's humanoids won't learn dexterity

**原文链接**: [https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/](https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/)

尽管投入巨大，本文认为今天的人形机器人近期内无法达到人类水平的灵巧度。作者回顾了机器人技术的发展历程，强调了数十年来在复制人类操作技能方面的努力，从20世纪60年代的早期尝试开始。虽然配备简单“末端执行器”（如平行爪夹具和吸盘）的工业机器人很常见，但事实证明，复杂的多关节手过于脆弱且无法在现实世界中有效应用。

论点的核心在于使用“端到端学习”的缺陷方法，即向机器人展示人类执行任务的视频。作者呼应本杰·霍尔森的批评，强调了由于缺乏力反馈、手指控制有限、缺乏触觉传感以及中等精度，这种方法的局限性。这些缺点使得机器人无法真正“感受”并响应操作过程中涉及的力，而这对于灵巧度至关重要。

作者认为，像叠衣服或清理手上的花生酱这样的任务，人类可以轻松完成，但对于当前的人形机器人来说却构成了重大挑战，因为它们需要当前系统所缺乏的视觉、触觉和力反馈的结合。作者认为，围绕人形机器人作为能够取代人类劳动的通用机器的炒作是不成熟的，并且是基于对其实现类似人类灵巧能力的不切实际的期望。

---

## 39. 充分利用68000上的编译C循环

**原文标题**: Make the most of compiled C loops on the 68000

**原文链接**: [https://dciabrin.net/posts/make-the-most-of-compiled-c-loops-on-the-68000/make-the-most-of-compiled-c-loops-on-the-68000/](https://dciabrin.net/posts/make-the-most-of-compiled-c-loops-on-the-68000/make-the-most-of-compiled-c-loops-on-the-68000/)

本文详细介绍了作者优化 Neo Geo MVS 和 AES 硬件上一个简单的 C 语言 `clear_screen` 函数的过程，重点在于实现高效的 68000 汇编代码。Neo Geo 的视频 RAM (VRAM) 存储着瓦片和精灵数据，只能通过内存映射的 GPU 寄存器间接访问。

作者从一个直接的 C 语言实现开始，使用 `for` 循环将瓦片数据写入 VRAM 以清除屏幕。最初，`gcc` 生成的未优化汇编代码效率低下。应用诸如 `-fomit-frame-pointer -O2` 之类的优化标志可以显著改善代码，消除堆栈使用并执行常量折叠。

然而，作者的目标是进一步优化。最初的优化代码使用一个常量内存地址来访问 VRAM，这可以通过使用地址寄存器来改进。由于 GCC 的全局公共子表达式消除，尝试使用 `register volatile` 声明来强制使用寄存器失败。

然后，作者使用内联汇编将 GPU 寄存器定义为外部符号，欺骗编译器将其视为非常量，从而强制使用地址寄存器。这减少了循环的内存访问指令大小。

最后，作者探索利用 68000 的 `dbra` 指令进行进一步的循环优化，但 GCC 的循环优化会干扰。通过使用 `optimize` 函数属性来有选择地为 `clear_screen` 函数禁用 `-ftree-loop-optimize` 可以解决这个问题，从而生成所需的 `dbra` 指令和一个高度优化的循环。本文展示了如何为特定场景操控 GCC 的优化行为，以实现高效的 68000 汇编代码。

---

## 40. OpenTSLM: 理解时间序列的语言模型

**原文标题**: OpenTSLM: Language models that understand time series

**原文链接**: [https://www.opentslm.com/](https://www.opentslm.com/)

OpenTSLM 推出时间序列语言模型 (TSLM)，一种新型 AI 基础模型，能够原生理解和推理时间序列数据以及文本。与当前难以处理心跳、价格变动和传感器数据等时间信号的 AI 模型不同，TSLM 旨在直接处理和推理时间数据，从而实现自然语言解释、推理和预测。

OpenTSLM 项目包含开源和专有模型。"OpenTSLM" 开源模型基于公共数据训练，旨在建立时间推理的标准，并促进全球研发生态系统的发展。"Frontier TSLM" 是先进的专有模型，基于专业数据训练，目标是企业级性能，并为 API 和垂直解决方案提供支持。

OpenTSLM 的目标是创建一个“AI 的时间接口”，将真实世界的信号与智能决策和自主代理连接起来。该愿景包括主动医疗保健、自适应机器人和弹性基础设施等应用，从而促进新型人机协作。OpenTSLM 团队由来自领先大学和科技公司的研究人员和工程师组成。他们邀请读者了解更多关于 TSLM 如何改变其领域的信息，并鼓励他们加入该项目。白皮书和 GitHub 仓库已发布。

---

## 41. 分散软件工程师的注意力比大多数管理者认为的更有害。

**原文标题**: Distracting software engineers is more harmful than most managers think

**原文链接**: [https://workweave.dev/blog/distracting-software-engineers-is-more-harmful-than-managers-think-even-in-the-ai-times](https://workweave.dev/blog/distracting-software-engineers-is-more-harmful-than-managers-think-even-in-the-ai-times)

干扰软件工程师的危害远超管理者认知：AI 时代的深度工作至关重要

本文认为，干扰软件工程师的危害远超管理者通常的认知，尤其是在人工智能时代。文章强调了“深度工作”的重要性，将其定义为需要大量脑力、高度专注、不被打断并能创造独特价值的工作，并将其与“浅层工作”（如回复电子邮件）进行对比。

作者 Anton Zaides 指出，尽管远程工作具有实现专注时间的潜力，但会议的增加，尤其是远程会议的增加，导致了更多的多任务处理和更少的深度工作。这导致工作质量下降，需要更多的会议来解决问题，并且工程师难以达到“心流”状态，这需要大约 45 分钟的不间断工作才能实现。干扰会重置这个时钟，从而大大减少生产时间。

文章为管理者提出了切实可行的解决方案：改善会议文化，包括制定清晰的议程、固定会议时间以及仅邀请必要的与会者，并且如果可能，尽可能取消会议。文章还建议重新思考拉取请求 (PR) 工作流程，以尽量减少上下文切换，并认为信任熟练的工程师和减少强制性审查可能是有益的。最后，作者倡导管理者以身作则，保护自己的深度工作时间。作者总结说，随着对人工智能的依赖程度增加，专注时间将变得更加重要，并强调掌握人工智能的深度工作将成为工程师和公司的关键差异化因素。

---

## 42. 触感：ESP32 操作系统

**原文标题**: Tactility: An ESP32 OS

**原文链接**: [https://tactility.one](https://tactility.one)

文章《触觉：ESP32操作系统》介绍了一个名为“触觉”的ESP32微控制器新操作系统。该文章极其简短，仅包含标题“触觉”和单词“加载中...”。由于内容极少，无法提供其特性、目标受众或功能的详细摘要。本质上，唯一获得的信息是“触觉”正在被开发为ESP32平台的操作系统，并且在文章撰写时，它处于加载或早期开发状态。任何进一步的解读都将是推测。

---

## 43. Show HN: Unite 实时操作系统

**原文标题**: Show HN: The Unite real time operating system

**原文链接**: [https://jacquesmattheij.com/unite-operating-system/](https://jacquesmattheij.com/unite-operating-system/)

这款“Show HN”帖子介绍 Unite，这是一个受 QNX 启发，在 90 年代初开发的 32 位保护模式多任务操作系统。Unite 中的一切，包括驱动程序和文件系统，都作为用户进程运行，旨在实现网络透明性，远程资源就像本地资源一样被访问。

作者受到 Tanenbaum 和 Torvalds 关于内核设计的争论的激励，在 30 年后重新启动了这个项目，利用 VirtualBox 和 QEMU 等现代虚拟化工具来克服过去的硬件限制。

该操作系统具有带有细粒度优先级控制的实时内核，使其适用于嵌入式系统。复兴涉及恢复二进制文件和启动软盘镜像，但仍然存在挑战，特别是重新编译 bootfs.com 引导加载程序组件。

Unite 配备了实用程序、C/C++ 编译器、shell 和基本的网络支持。它以文本模式启动，并提供图形模式，但启用它需要手动控制台命令。该操作系统以 torrent 形式分发，并包含设置和基本使用说明。

局限性包括无法正常工作的网络和 COM 端口、有 bug 的 vi 编辑器以及缺乏安全考虑。作者正在发布代码作为贡献，并且不会管理该项目，将未来的开发留给社区。内核、编辑器和图形库均置于公共领域，但需注明项目来源。

---

## 44. 在CPU上实时本地运行的开源语音基础模型

**原文标题**: Open source speech foundation model that runs locally on CPU in real-time

**原文链接**: [https://huggingface.co/neuphonic/neutts-air](https://huggingface.co/neuphonic/neutts-air)

NeuTTS Air：实时本地CPU运行的开源语音基础模型

---

## 45. 基于哈雷尔论文介绍状态图的西铁城石英表复刻品

**原文标题**: A replica of Citizen Quartz watch based on Harel's paper introducing statecharts

**原文链接**: [https://andyjakubowski.github.io/statechart-watch/](https://andyjakubowski.github.io/statechart-watch/)

这似乎是一个非常初步且不完整的描述。内容“Citizen WatchYou need to enable JavaScript to run this app.”表明这是一个损坏的Web应用程序，而不是一篇文章。看来其目的是使用 David Harel 提出的状态图原理来创建一个西铁城石英表的复制品。

假设存在一个可运行的应用程序版本，以下*可能*是这种情况，以及文章*可能*是关于什么的：

这篇文章很可能旨在展示状态图在建模复杂系统方面的强大功能，并以西铁城石英表作为实践示例。状态图是一种用于建模复杂反应式系统的可视化形式主义，优于传统的有限状态机，尤其是在处理并发性和分层状态时。

该应用程序可能模拟了西铁城石英表的各种状态（例如，计时、计时模式、闹钟设置、日期调整）。它可能使用状态图来表示嵌套状态及其之间的转换，包括处理用户输入（按钮按下）和管理内部时钟和日历。

该应用程序和相关解释可能涵盖的关键要素是：

*   **分层状态：** 展示状态图如何允许嵌套状态，以比平面状态机更具组织性的方式表示复杂行为。例如，“计时”状态可能具有显示小时、分钟和秒的子状态。
*   **并发性：** 演示状态图如何表示并行活动，例如计时器与主时间显示同时运行。
*   **转换：** 说明用户操作（按钮按下）如何触发状态之间的转换，包括涉及多个状态和条件的复杂转换。
*   **事件处理：** 解释状态图如何响应外部事件，例如按钮按下和时间信号。

本质上，目标是展示如何使用状态图来创建具有复杂行为的真实世界设备（如西铁城石英表）的强大且可维护的模型。不幸的是，在没有可运行的应用程序或完整文档的情况下，这纯粹是基于标题指示的推测。

---

## 46. 福特将基本导航功能锁在订阅服务之后

**原文标题**: Ford locking basic navigation behind a subscription

**原文链接**: [https://old.reddit.com/r/LinusTechTips/comments/1nw5s9f/ford_locking_basic_navigation_behind_a/](https://old.reddit.com/r/LinusTechTips/comments/1nw5s9f/ford_locking_basic_navigation_behind_a/)

无法访问文章链接。

---

## 47. 在C++模块中，全局唯一的模块名称似乎是不可避免的。

**原文标题**: In C++ modules globally unique module names seem to be unavoidable

**原文链接**: [https://nibblestew.blogspot.com/2025/09/in-c-modules-globally-unique-module.html](https://nibblestew.blogspot.com/2025/09/in-c-modules-globally-unique-module.html)

尤西2025年9月28日的博客文章认为，全局唯一的模块名是C++模块正确运行的*必要条件*，而不仅仅是最佳实践。这是因为当多个同名模块被链接到同一个可执行文件中时，可能会出现ODR（单一定义规则）违规的情况。模块名被用作模块链接实体的区分符，导致了这一问题。

作者提出了一个常见的场景：一个项目中的可执行文件链接到多个内部和外部静态库，其中一些库可能具有同名模块（例如，`utils`）。尽管构建系统可能会尝试管理这些冲突，但GCC的错误跟踪器声明这种设置本质上是存在问题的，编译器可以自由地以不可预测的方式运行（IFNDR）。

接受全局唯一的模块名可以简化模块构建系统。通过为所有模块文件使用单个目录（如GCC的`gcm.cache`），可以避免冲突，并且模块映射器变得不必要。然而，从系统范围的预构建库导入模块目前存在问题，因为模块文件格式（如更好的PCH）在编译器版本和标志设置之间通常是不稳定的，因此目前无法将预构建库作为模块导入。

作者总结说，开发人员面临一个选择：要么接受全局唯一模块名的现实，并构建一个简单、可靠的系统；要么拒绝它，并创建一个复杂、不可靠的系统。

评论员Jannik强调稳定的模块文件不是目标，但尤西指出，其他人（如Visual Studio）对模块文件稳定性有不同的看法，这让他们相信预构建库可以取代头文件。

---

## 48. 激光网络协议

**原文标题**: IP over Lasers

**原文链接**: [https://www.mikekohn.net/micro/ip_over_lasers.php](https://www.mikekohn.net/micro/ip_over_lasers.php)

Michael Kohn的“激光IP传输”项目详细介绍了如何使用激光而非传统以太网或WiFi连接两台计算机。该项目利用Linux tun网络设备，允许用户空间程序处理路由到它的网络流量。

该设置涉及使用USB-UART电缆将笔记本电脑/树莓派5连接到ATtiny85微控制器。这些微控制器随后控制激光器和光电晶体管，从而实现通过光信号进行数据传输。一个设备上的激光器指向另一个设备上的光电晶体管，反之亦然，从而创建双向链路。

ATtiny85代码很简单，根据UART输入调制激光器，并将光电晶体管输入转换回UART输出。数据流经`tun0`接口，该接口配置了每台计算机上的特定IP地址。

一个“中继”程序持续监控`tun0`和UART，在它们之间转发数据包。它检查tun0上的数据包，如果找到，则将数据发送到UART。它还会检查UART上的数据，读取数据并将其发送到tun0。

最初使用38kHz红外传感器的目标被放弃，转而使用光电晶体管。在测试期间，使用了4800的波特率，但只得到乱码，因此降至2400。

该项目的源代码可在GitHub上找到。Kohn还强调了在使用激光器时佩戴护目镜以保护眼睛的重要性。

---

## 49. 增加练习面积

**原文标题**: Increasing your practice surface area

**原文链接**: [https://www.indiehackers.com/post/lifestyle/increasing-your-practice-surface-area-agxYGi9bL0gd1WYYQZAu](https://www.indiehackers.com/post/lifestyle/increasing-your-practice-surface-area-agxYGi9bL0gd1WYYQZAu)

通过扩大“练习表面积”来提高技能

---

## 50. 气候变暖而非过度放牧是草原面临的最大威胁，研究表明

**原文标题**: Warming climate–not overgrazing–is biggest threat to rangelands, study suggests

**原文链接**: [https://phys.org/news/2025-09-climate-overgrazing-biggest-threat-rangelands.html](https://phys.org/news/2025-09-climate-overgrazing-biggest-threat-rangelands.html)

本文报道了一项康奈尔大学的研究，该研究挑战了长期以来认为过度放牧是草场退化的主要驱动因素的观点。研究人员分析了蒙古41年的数据（蒙古70%的土地为草场），得出结论认为，气候变化对草场生产力的影响远大于牲畜数量。

该研究发表在《科学》杂志上，发现虽然较大的畜群可能对草场生产力产生较小的、短期的负面影响，但气候变化和长期气候变化才是主导因素。研究人员使用两阶段统计分析来评估畜群规模和气候的影响，区分了短期天气波动和长期气候趋势。

研究结果表明，年度天气变化对草场生产力的影响大约是畜群规模的20倍。这表明，与全球温室气体排放的更广泛影响相比，蒙古牧民的放牧做法的影响相对较小。

作者认为，政策制定者应该将重点从向牧民征税和限制畜群规模，转移到解决全球气候减缓问题以及为气候损害提供国际赔偿。他们批评了普遍认为牧民缺乏有效管理草场知识的假设，并认为目前的政策可能会不公平地加重牧民的负担。该研究强调，有必要重新思考草场保护战略，承认气候变化的压倒性影响。

---

## 51. Show HN: Glide，一款可扩展、以键盘操作为主的网页浏览器

**原文标题**: Show HN: Glide, an extensible, keyboard-focused web browser

**原文链接**: [https://blog.craigie.dev/introducing-glide/](https://blog.craigie.dev/introducing-glide/)

Glide：基于Firefox的、面向键盘操作且可扩展的macOS和Linux Web浏览器。它旨在提供完整的可定制性，同时避免浏览器扩展的安全限制。与扩展不同，Glide使用TypeScript配置，允许用户修改浏览器的行为和UI，访问Web扩展API，派生进程，定义宏，并创建自定义键盘映射。

该浏览器借鉴了Vim的模式概念，根据上下文自动在“普通”和“插入”等模式之间切换。它还提供“忽略”模式，以绕过有问题网站上的键盘映射。提示模式允许基于键盘的网络页面导航。

主要功能包括聚焦最大输入元素的命令，标签页的模糊查找器，导航历史快捷键，用于配置测试的REPL，以及受which-key启发的UI以显示键盘映射。作者强调了他们自己的用于克隆当前github仓库并在kitty + neovim中打开它的键盘映射，以此作为Glide实现的节省时间的定制示例。

Glide目前处于早期alpha阶段，因此一些API仍然缺失，但该项目的主要目标是允许完全控制浏览器的功能。作者鼓励用户尝试，并在浏览器中提供教程以开始使用。

---

## 52. JackTrip: 基于互联网的多机音频网络演奏

**原文标题**: JackTrip: Multi-machine audio network performance over the Internet

**原文链接**: [https://github.com/jacktrip/jacktrip](https://github.com/jacktrip/jacktrip)

JackTrip是一个多机音频系统，专为通过互联网进行高质量、实时音乐表演而设计。它能够双向传输多通道未压缩音频，仅受参与机器的计算能力和网络带宽限制。该系统是跨平台的，可在 Linux、macOS、Windows 和 FreeBSD 上运行，允许用户连接运行不同操作系统的设备。更多信息，包括使用说明，可在 JackTrip 的 GitHub 页面上找到。开发者鼓励用户将任何安全漏洞报告到提供的电子邮件地址。本质上，JackTrip使音乐家能够以最小的音频延迟和最大的保真度进行远程协作和表演。

---

## 53. 范畴论图解——自然变换

**原文标题**: Category Theory Illustrated – Natural Transformations

**原文链接**: [https://abuseofnotation.github.io/category-theory-illustrated/11_natural_transformations/](https://abuseofnotation.github.io/category-theory-illustrated/11_natural_transformations/)

本文介绍了范畴论中的自然变换，阐述了其在定义范畴等价中的重要性。文章认为，关注态射（关系/过程）比仅仅关注对象更有启发性，这与赫拉克利特的万物皆变的哲学相呼应。

文章强调了同构不变性，即同构对象共享属性，本质上等同于范畴论中的同构和相等。然而，文章指出范畴同构本身并不具备同构不变性，因此需要一个新的概念：等价。

文章使用地图和区域的类比来阐释同构和等价之间的区别。同构地图能够完整地表示区域，而等价地图可能会折叠同构的交集，但仍然保留所有路线（态射）。

文章对比了基于对象（等价类）和态射定义等价的方式。虽然基于对象定义等价适用于序关系，但它对于范畴来说是不够的。范畴的等价性是通过在范畴同构的定义中用同构替换相等来定义的。

最后，文章介绍了自然变换，作为函子之间的态射，对于定义函子同构（自然同构）以及由此产生的范畴等价至关重要。自然变换被描述为“2-态射”，由“对象映射的映射”和“态射映射的映射”组成。“对象映射的映射”包括为源范畴中的每个对象指定目标范畴中的态射。

---

## 54. 不要回避职场政治

**原文标题**: Don't avoid workplace politics

**原文链接**: [https://terriblesoftware.org/2025/10/01/stop-avoiding-politics/](https://terriblesoftware.org/2025/10/01/stop-avoiding-politics/)

本文旨在挑战职场中，特别是工程师群体中对“政治”普遍存在的厌恶。文章认为，“政治”本身并非坏事；相反，当优秀的人拒绝参与时，“糟糕的政治”才会盛行。作者将政治定义为组织内部的关系、影响力和权力动态网络，这对于协调和决策至关重要。回避政治意味着决策会在没有你参与的情况下做出，可能导致有缺陷的技术成果。

关键在于拥抱“好的政治”，这包括策略性地处理人际关系和施加影响力以实现积极成果。这包括建立跨团队联系、了解利益相关者的动机，以及用通俗易懂的方式沟通技术理念。好的政治的例子包括向上管理、创造双赢局面，以及确保你的工作成果被看见。

作者强调，好的政治不是关于操纵或自我推销，而是关于倡导好的想法和保护你的团队。通过积极参与组织动态，工程师可以影响决策、防止不良结果，并最终为更有效和积极的工作环境做出贡献。不参与政治只会让能力较差或动机不良的人占据主导地位，从而导致公司及其员工获得次优的结果。

---

## 55. 美国备忘录提议大学接受意识形态和外国学生入学条款以获取联邦资金

**原文标题**: US memo to colleges proposes terms on ideology, foreign enrollment for fed funds

**原文链接**: [https://www.reuters.com/world/us/white-house-sets-hiring-foreign-enrolment-terms-colleges-get-funding-advantage-2025-10-02/](https://www.reuters.com/world/us/white-house-sets-hiring-foreign-enrolment-terms-colleges-get-funding-advantage-2025-10-02/)

路透社文章《美国备忘录提议大学接受意识形态和外国学生入学条款以获取联邦资金》报道了一份拟议的白宫备忘录，该备忘录概述了高校和大学在联邦资金方面获得优惠待遇的条件。 备忘录建议各机构在招聘实践中促进“意识形态多样性”，似乎是为了解决人们对校园内普遍存在的自由主义偏见的担忧。 虽然备忘录没有详细说明衡量或确保这种多样性的具体方法，但它暗示，在这一领域表现出的努力可能会提高大学获得联邦资金的机会。

备忘录的另一个关键方面是关注外国学生的入学。 它建议奖励那些吸引来自更广泛国家的学生的机构，特别是旨在减少对中国学生的依赖。 其根本原因似乎与国家安全问题和校园视角多样化有关。

本质上，该备忘录建议将联邦资金优势与机构在招聘中意识形态平衡和外国学生群体多样化方面的具体行为联系起来。 此举可能会遇到支持和反对，引发人们对政府过度干预学术事务以及对大学自主权的潜在影响的质疑。 如何实施和执行这些条件的细节仍不清楚。

---

## 56. 顶尖艺术家揭秘他们信赖的创作者

**原文标题**: Leading artists reveal the fabricators they entrust with their creations

**原文链接**: [https://www.ft.com/content/d84c8502-d413-4a26-a59c-494af11978b5](https://www.ft.com/content/d84c8502-d413-4a26-a59c-494af11978b5)

金融时报：艺术家与专业制造商合作趋势渐增

本文探讨了艺术家与专业制造商合作创作艺术品的日益增长的趋势。文章认为，尽管孤独艺术家的传统形象依然存在，但许多当代作品都是集体努力的结果。

玛丽娜·阿布拉莫维奇、加达·阿梅尔、威廉·肯特里奇、贾斯琳·考尔、艾玛·威特和弗朗西斯·乌普里查德等多位知名艺术家接受了采访，谈论了他们与制造商合作的经历。阿布拉莫维奇强调，在人工智能时代，想法比工艺更重要，并赞扬了她与Factum Arte的合作。阿梅尔强调制造商在解决技术挑战和贡献特定技能方面的关键作用，同时保持对核心艺术愿景的控制。肯特里奇重视斯威士兰的史蒂芬斯挂毯工作室的诠释性投入，模糊了作者身份的界限。考尔强调了给予合作者署名的伦理重要性。威特描述了与铁匠合作如何使她完成了她的艺术创作。乌普里查德谈到了给予与她合作的陶艺家署名。

文章还涉及了署名权方面的挑战，以及艺术市场通常更偏爱单一署名作者，这使得合作作品更难销售。国家美术馆的普里耶什·米斯特里指出，博物馆也在努力解决作者身份问题。文章总结说，艺术越来越关乎网络和关系，超越了孤独天才的神话。

---

## 57. 珍·古道尔去世了

**原文标题**: Jane Goodall has died

**原文链接**: [https://www.latimes.com/obituaries/story/2025-10-01/jane-goodall-chimpanzees-dead](https://www.latimes.com/obituaries/story/2025-10-01/jane-goodall-chimpanzees-dead)

珍·古道尔，开创性的英国动物行为学家和灵长类动物学家，逝世，享年91岁。古道尔凭借其对野生黑猩猩的开创性观察，彻底改变了灵长类动物学领域，挑战了关于工具使用和人类独特性的现有科学信念。她发现黑猩猩制造和使用工具，狩猎，吃肉，并表现出与人类相似的一系列情感和行为，包括爱、悲伤和暴力。

她在坦桑尼亚贡贝溪国家公园的长期研究（她为黑猩猩研究对象命名）为黑猩猩的行为和社会结构提供了前所未有的见解。尽管最初受到科学界的怀疑，但她的工作最终被认为是重大的科学成就。

古道尔为灵长类动物学领域的其他女性铺平了道路，并成为黑猩猩保护和动物权利的全球倡导者。通过珍·古道尔研究所和“根与芽”等项目，她促进了研究、教育和可持续发展。在她的晚年，她广泛旅行，以提高人们对森林砍伐、栖息地保护以及人类与环境相互联系的认识。她的遗产超越了她的科学贡献，激励着一代又一代人与自然建立联系，并为更可持续的未来而努力。

---

## 58. DSEG：原始七段和十四段字体 (2014)

**原文标题**: "DSEG": Original 7-segment and 14-segment fonts (2014)

**原文链接**: [https://www.keshikan.net/fonts-e.html](https://www.keshikan.net/fonts-e.html)

DSEG是一款免费字体家族，模仿七段和十四段数码管显示，提供超过50种样式。它包括罗马字母、符号、TrueType字体和Web开放字体格式（WOFF，WOFF2）。DSEG根据SIL开放字体许可1.1授权，允许商业/非商业用途、修改和再分发。

这些字体提供特殊功能，例如交替使用冒号和空格字符来实现闪烁效果，以及使用零宽度句点来实现迁移效果。感叹号被指定为“全灭”状态。特定字符映射到相应的段（例如，DSEG7中用“8”表示所有段都亮起）。提供DSEG7和DSEG14的完整字符代码映射表。它还包括一个“DSEGWeather”字体，包含不同天气状况的图标。

文章详细介绍了使用规范、许可条款和开发历史，重点介绍了关键更新，如增加WOFF2支持、新的天气图标以及许可更改为SIL开放字体许可1.1。该字体使用FontForge在Ubuntu上创建。

---

## 59. 据报道，苹果放弃更轻的Vision Pro，转而支持智能眼镜。

**原文标题**: Apple reportedly scraps lighter Vision Pro in favor of smart glasses

**原文链接**: [https://www.tomsguide.com/computing/smart-glasses/apple-reportedly-scraps-vision-pro-headset-follow-up-in-favor-of-smart-glasses](https://www.tomsguide.com/computing/smart-glasses/apple-reportedly-scraps-vision-pro-headset-follow-up-in-favor-of-smart-glasses)

据报道，苹果已暂停开发更轻、更便宜的Vision Pro头显版本“Vision Air”，转而专注于开发智能眼镜。彭博社的马克·古尔曼报道称，这一转变旨在加速苹果进入智能眼镜市场，目前苹果在该市场落后于Meta等竞争对手。

据称，苹果正在研发两种类型的智能眼镜。第一种代号为N50，将与iPhone配对使用，并且没有显示屏，类似于Meta的Ray-Ban智能眼镜，预计将于2027年发布。第二种类型将配备显示屏，直接与Meta的Ray-Ban Display竞争，目标是2028年发布。报告表明，苹果正试图加速开发以赶上竞争对手。预计这些智能眼镜将大量集成语音控制和人工智能，而这些领域正是苹果努力改进的方向，尤其是在计划于明年春天对Siri进行全面改革之后。

尽管有此转变，苹果预计仍将很快发布配备更快芯片的改进版Vision Pro。最初的Vision Pro并未被完全放弃，只是优先级降低。

---

## 60. 活细菌中基因表达的长距离和广域检测

**原文标题**: Long-distance and wide-area detection of gene expression in living bacteria

**原文链接**: [https://www.asimov.press/p/hyperspectral](https://www.asimov.press/p/hyperspectral)

本文探讨了生物传感器技术的一项新进展：开发出能够利用高光谱相机对活细菌中的基因表达进行远距离、大面积检测的传感器。

作者尼科·麦卡蒂解释说，传统的生物传感器依赖于GFP或荧光素酶等输出，但这些输出受到距离和可见性的限制。然而，这项新技术采用了基因编码的传感器，可产生独特的高光谱特征，这些特征可由配备专用相机的无人机检测到。

研究人员对细菌进行基因改造，使其产生胆绿素IXα和细菌叶绿素a等具有独特光谱指纹的分子。然后，他们将这些经过基因改造的微生物喷洒到土壤中，并成功地使用高光谱相机从高达90米远的距离检测到它们，证明了监测生态系统分子活动的潜力。

文章还探讨了此类生物传感器商业化面临的挑战，原因是围绕基因工程微生物释放的严格法规。《有毒物质控制法》(TSCA)提出了一个重大障碍，因为它基于微生物的工程方法而不是安全性来对其进行监管。像Pivot Bio这样的公司已经找到了规避这些法规的方法，即避免物种之间的基因转移。

尽管存在监管方面的挑战，高光谱报告基因的开发标志着向更通用的传感器转变，从而能够在以前难以进入的环境中测量生物过程。未来的重点在于工程化从细胞到人类更可靠的通信渠道，而不是仅仅关注细胞可以感知什么。

---

## 61. 你刚收到的那条烦人的短信诈骗可能就来自这样的设备。

**原文标题**: That annoying SMS phish you just got may have come from a box like this

**原文链接**: [https://arstechnica.com/security/2025/10/that-annoying-sms-phish-you-just-got-may-have-come-from-a-box-like-this/](https://arstechnica.com/security/2025/10/that-annoying-sms-phish-you-just-got-may-have-come-from-a-box-like-this/)

诈骗分子利用工业环境中未受保护的蜂窝路由器漏洞发起基于短信的网络钓鱼（短信诈骗）活动。 安全公司Sekoia发现超过18,000台此类路由器可在线访问，其中数百台允许不受限制地访问编程接口。 许多路由器运行着存在已知漏洞的过时固件。

攻击者利用这些路由器向多个国家/地区的电话号码发送欺诈短信，主要集中在瑞典、比利时和意大利。 这些短信诱骗接收者登录虚假网站以窃取凭据，通常冒充政府服务。 Sekoia的研究人员强调了这种“不复杂但有效”的方法的有效性，因为它将短信分发分散到多个国家，使检测和取缔工作变得复杂。

一种可能的漏洞是CVE-2023-43261，攻击者可以通过该漏洞获取管理员密码。 然而，Sekoia的分析表明，这可能不是唯一的攻击方式。

这些网络钓鱼网站采用逃避分析的策略，例如阻止非移动设备访问以及禁用调试工具。 一些网站与一位使用阿拉伯语和法语的Telegram机器人运营商有关。 这项调查突显了容易被忽视的工业设备如何被用于大规模短信诈骗活动。

---

## 62. 理解文化差异：密歇根鱼测试 (2013)

**原文标题**: Understanding Cultural Differences: The Michigan Fish Test (2013)

**原文链接**: [http://michael-roberto.blogspot.com/2013/07/understanding-cultural-differences.html](http://michael-roberto.blogspot.com/2013/07/understanding-cultural-differences.html)

这篇2013年7月22日的博文讨论了“密歇根鱼测试”，以此来展示感知和理解方面的文化差异。该测试由Richard Nisbett和Takahiko Masuda进行，向美国和日本参与者展示了一幅鱼的图片。

关键发现是，美国人倾向于关注个体的大鱼（“主要角色”），将其视为强大的行动者。相比之下，日本参与者则关注整个场景以及各个元素之间的关系，认为环境是影响一切的主导因素。

后续的图像修改测试表明，日本参与者更可能注意到背景或环境的变化，而美国人则擅长识别大鱼，无论环境如何。这表明美国人优先考虑个体元素，而日本人则关注背景和关系。

这篇博文强调，这些不同的感知反映了在个体能动性和环境作用方面文化叙事的根本差异。代表更加个人主义文化的美国人，倾向于将个体视为强大的驱动者，而代表更加集体主义文化的日本人，则强调背景和相互依赖的重要性。该文章还提到了Sheena Iyengar教授关于跨文化决策差异的更广泛研究。

---

## 63. 公司人

**原文标题**: The Company Man

**原文链接**: [https://www.lesswrong.com/posts/JH6tJhYpnoCfFqAct/the-company-man](https://www.lesswrong.com/posts/JH6tJhYpnoCfFqAct/the-company-man)

无法访问文章链接。

---

## 64. Greg Kroah-Hartman 讲解开源开发者的网络韧性法案

**原文标题**: Greg Kroah-Hartman explains the Cyber Resilience Act for open source developers

**原文链接**: [https://www.theregister.com/2025/09/30/cyber_reiliance_act_opinion_column/](https://www.theregister.com/2025/09/30/cyber_reiliance_act_opinion_column/)

本文探讨了Greg Kroah-Hartman对欧盟网络弹性法案(CRA)的看法及其对开源开发者影响。与最初的担忧相反，Kroah-Hartman认为CRA可能对开源有利。

CRA旨在通过要求公司记录、保护和维护其软件供应链来确保具有数字元素产品的安全性。这包括生成软件物料清单(SBOM)、跟踪漏洞以及透明的安全实践。一个关键方面是区分无偿的、业余爱好者开发者和将开源软件商业化的法人实体。

从事非商业项目的个体开源开发者面临的最低要求是，主要需要在“readme”文件中提供安全联系人。然而，管理开源项目并接受资助的组织必须满足更严格的管理要求。

CRA主要针对商业制造商和分销商，要求他们在将开源代码集成到在欧盟销售的产品中时，遵守文档、事件响应和生命周期管理要求。这实际上将CRA的影响范围扩展到全球。

虽然公司最初可能会试图将CRA合规的负担转移给开发者，但Kroah-Hartman认为他们不必接受这一点。他认为CRA将增加对开源的需求，因为公司比专有软件更能控制代码。他预计，使用开源代码的企业将很快意识到CRA的重要性，并需要帮助来应对合规性。虽然可能最初会出现恐慌，但Kroah-Hartman表示乐观，认为CRA旨在追究大公司的责任，并支持而不是损害开源生态系统。

---

## 65. Sora 2

**原文标题**: Sora 2

**原文链接**: [https://openai.com/index/sora-2/](https://openai.com/index/sora-2/)

无法访问文章链接。

---

## 66. 基于WiFi地图的高分辨率高效图像生成

**原文标题**: High-resolution efficient image generation from WiFi Mapping

**原文链接**: [https://arxiv.org/abs/2506.10605](https://arxiv.org/abs/2506.10605)

本文介绍了一种名为LatentCSI的新颖高效方法，该方法利用WiFi信道状态信息(CSI)测量生成物理环境的高分辨率图像。与之前依赖于计算密集型GAN或复杂图像到图像管道的方法不同，LatentCSI利用预训练的潜在扩散模型(LDM)。

核心思想是使用轻量级神经网络将WiFi CSI幅度直接映射到预训练LDM的潜在空间中。这避免了对显式图像编码的需求，并实现了高效的图像合成。然后，LDM的去噪扩散模型会细化潜在表示，并在文本提示的引导下实现可控性，之后LDM的解码器会生成最终的高分辨率图像。

作者在两个数据集上验证了LatentCSI：一个使用WiFi设备和摄像头收集的定制宽带CSI数据集和一个MM-Fi数据集的子集。实验结果表明，在计算效率和感知质量方面，LatentCSI优于在真实图像上训练的同类基线模型。此外，该方法还提供了文本引导可控性的实际优势，允许用户通过文本提示来影响生成的图像。本文的结论是，LatentCSI为从WiFi CSI生成图像提供了一种高效、高质量的解决方案，并通过基于文本的指导增加了灵活性。

---

## 67. 勒索软件攻击后，日本最受欢迎的啤酒面临短缺。

**原文标题**: Japan is running out of its favorite beer after ransomware attack

**原文链接**: [https://arstechnica.com/security/2025/10/japan-is-running-out-of-its-favorite-beer-after-ransomware-attack/](https://arstechnica.com/security/2025/10/japan-is-running-out-of-its-favorite-beer-after-ransomware-attack/)

勒索软件攻击瘫痪朝日集团日本国内啤酒厂，或致朝日超爽啤酒短缺。攻击导致订购和交付系统瘫痪，朝日啤酒在日本的30家工厂自周一以来大部分已离线。零售商预计数日内朝日产品，包括超爽啤酒，将在便利店、超市和居酒屋等渠道出现货架空置现象。

虽然零售商正在寻找三得利和麒麟等其他品牌来弥补，但许多顾客对超爽啤酒情有独钟。朝日啤酒是日本最大的啤酒制造商，通常每天生产相当于670万瓶大啤酒瓶的产量。该公司已推迟推出八款新产品，并正在探索手动订单处理。

此次事件是针对日本公司的网络攻击日益增长趋势的一部分，这些公司被认为防御薄弱且倾向于支付赎金。日本警察厅报告称勒索软件攻击有所增加，但专家认为实际数字远高于此。从此类攻击中恢复可能需要一个月或更长时间。作为回应，日本于五月通过了一项法律，以积极打击网络犯罪分子。朝日啤酒仍在调查该攻击是否确实是勒索软件攻击。在日本境外的业务，如欧洲，仍未受到影响。

---

## 68. Announcing Tinker

**原文标题**: Announcing Tinker

**原文链接**: [https://thinkingmachines.ai/blog/announcing-tinker/](https://thinkingmachines.ai/blog/announcing-tinker/)

生成摘要时出错

---

## 69. General strike against 13-hour work day brings Greece to a halt

**原文标题**: General strike against 13-hour work day brings Greece to a halt

**原文链接**: [https://www.theguardian.com/world/2025/oct/01/general-strike-against-13-hour-day-brings-greece-to-a-halt](https://www.theguardian.com/world/2025/oct/01/general-strike-against-13-hour-day-brings-greece-to-a-halt)

生成摘要时出错

---

## 70. Show HN: ChartDB Agent – Cursor for DB schema design

**原文标题**: Show HN: ChartDB Agent – Cursor for DB schema design

**原文链接**: [https://app.chartdb.io/ai](https://app.chartdb.io/ai)

生成摘要时出错

---

## 71. Fossabot: AI code review for Dependabot/Renovate on breaking changes and impacts

**原文标题**: Fossabot: AI code review for Dependabot/Renovate on breaking changes and impacts

**原文链接**: [https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/](https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/)

生成摘要时出错

---

## 72. Uxntal: A programming language for the Uxn virtual machine

**原文标题**: Uxntal: A programming language for the Uxn virtual machine

**原文链接**: [https://wiki.xxiivv.com/site/uxntal.html](https://wiki.xxiivv.com/site/uxntal.html)

生成摘要时出错

---

## 73. NJ theme park puts animatronic dinosaurs on Facebook Marketplace

**原文标题**: NJ theme park puts animatronic dinosaurs on Facebook Marketplace

**原文链接**: [https://gizmodo.com/new-jersey-theme-park-puts-animatronic-dinosaurs-on-facebook-marketplace-as-it-shuts-down-2000664489](https://gizmodo.com/new-jersey-theme-park-puts-animatronic-dinosaurs-on-facebook-marketplace-as-it-shuts-down-2000664489)

生成摘要时出错

---

## 74. Intelligent Kubernetes Load Balancing at Databricks

**原文标题**: Intelligent Kubernetes Load Balancing at Databricks

**原文链接**: [https://www.databricks.com/blog/intelligent-kubernetes-load-balancing-databricks](https://www.databricks.com/blog/intelligent-kubernetes-load-balancing-databricks)

生成摘要时出错

---

## 75. Measuring My DIY Air Purifier

**原文标题**: Measuring My DIY Air Purifier

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/measuring-my-diy-air-purifier](https://chillphysicsenjoyer.substack.com/p/measuring-my-diy-air-purifier)

生成摘要时出错

---

## 76. I only use Google Sheets

**原文标题**: I only use Google Sheets

**原文链接**: [https://mayberay.bearblog.dev/why-i-only-use-google-sheets/](https://mayberay.bearblog.dev/why-i-only-use-google-sheets/)

生成摘要时出错

---

## 77. Building an IoT Notification Device from Scratch

**原文标题**: Building an IoT Notification Device from Scratch

**原文链接**: [https://bertwagner.com/posts/splashflag-building-an-iot-swimming-notification-device-from-scratch/](https://bertwagner.com/posts/splashflag-building-an-iot-swimming-notification-device-from-scratch/)

生成摘要时出错

---

## 78. DARPA project for automated translation from C to Rust (2024)

**原文标题**: DARPA project for automated translation from C to Rust (2024)

**原文链接**: [https://www.darpa.mil/news/2024/memory-safety-vulnerabilities](https://www.darpa.mil/news/2024/memory-safety-vulnerabilities)

生成摘要时出错

---

## 79. Implementing /Usr Merge in Alpine

**原文标题**: Implementing /Usr Merge in Alpine

**原文链接**: [https://alpinelinux.org/posts/2025-10-01-usr-merge.html](https://alpinelinux.org/posts/2025-10-01-usr-merge.html)

生成摘要时出错

---

## 80. There is a huge pool of exceptional junior engineers

**原文标题**: There is a huge pool of exceptional junior engineers

**原文链接**: [https://workweave.dev/blog/hiring-only-senior-engineers-is-killing-companies](https://workweave.dev/blog/hiring-only-senior-engineers-is-killing-companies)

生成摘要时出错

---

## 81. CDC File Transfer

**原文标题**: CDC File Transfer

**原文链接**: [https://github.com/google/cdc-file-transfer](https://github.com/google/cdc-file-transfer)

生成摘要时出错

---

## 82. Our efforts, in part, define us

**原文标题**: Our efforts, in part, define us

**原文链接**: [https://weakty.com/posts/efforts/](https://weakty.com/posts/efforts/)

生成摘要时出错

---

## 83. Egg-Shaped Curves (2007)

**原文标题**: Egg-Shaped Curves (2007)

**原文链接**: [https://nyjp07.com/index_egg_E.html](https://nyjp07.com/index_egg_E.html)

生成摘要时出错

---

## 84. Evaluating the impact of AI on the labor market: Current state of affairs

**原文标题**: Evaluating the impact of AI on the labor market: Current state of affairs

**原文链接**: [https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs](https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs)

生成摘要时出错

---

## 85. Extreme branchless: Expr without GADTs or sum-types

**原文标题**: Extreme branchless: Expr without GADTs or sum-types

**原文链接**: [https://gautier.difolco.dev/2025-09/extreme-branchless-expr-fields/](https://gautier.difolco.dev/2025-09/extreme-branchless-expr-fields/)

生成摘要时出错

---

## 86. Washi: The Japanese paper crafted to last 1000 years [video]

**原文标题**: Washi: The Japanese paper crafted to last 1000 years [video]

**原文链接**: [https://www.bbc.com/reel/video/p0m4mg2j/washi-the-japanese-paper-crafted-to-last-1-000-years](https://www.bbc.com/reel/video/p0m4mg2j/washi-the-japanese-paper-crafted-to-last-1-000-years)

生成摘要时出错

---

## 87. Imgur pulls out of UK as data watchdog threatens fine

**原文标题**: Imgur pulls out of UK as data watchdog threatens fine

**原文链接**: [https://www.express.co.uk/news/uk/2115228/image-site-imgur-pulls-out](https://www.express.co.uk/news/uk/2115228/image-site-imgur-pulls-out)

生成摘要时出错

---

## 88. The biggest semantic mess in Futhark

**原文标题**: The biggest semantic mess in Futhark

**原文链接**: [https://futhark-lang.org/blog/2025-09-26-the-biggest-semantic-mess.html](https://futhark-lang.org/blog/2025-09-26-the-biggest-semantic-mess.html)

生成摘要时出错

---

## 89. Detect Electron apps on Mac that hasn't been updated to fix the system wide lag

**原文标题**: Detect Electron apps on Mac that hasn't been updated to fix the system wide lag

**原文链接**: [https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58](https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58)

生成摘要时出错

---

## 90. Inflammation now predicts heart disease more strongly than cholesterol

**原文标题**: Inflammation now predicts heart disease more strongly than cholesterol

**原文链接**: [https://www.empirical.health/blog/inflammation-and-heart-health/](https://www.empirical.health/blog/inflammation-and-heart-health/)

生成摘要时出错

---

## 91. The Prehistory of Computing, Part II

**原文标题**: The Prehistory of Computing, Part II

**原文链接**: [https://www.oranlooney.com/post/history-of-computing-2/](https://www.oranlooney.com/post/history-of-computing-2/)

生成摘要时出错

---

## 92. How did Renaissance fairs begin?

**原文标题**: How did Renaissance fairs begin?

**原文链接**: [https://www.history.com/articles/renaissance-fair-origins](https://www.history.com/articles/renaissance-fair-origins)

生成摘要时出错

---

## 93. Mind the encryptionroot: How to save your data when ZFS loses its mind

**原文标题**: Mind the encryptionroot: How to save your data when ZFS loses its mind

**原文链接**: [https://sambowman.tech/blog/posts/mind-the-encryptionroot-how-to-save-your-data-when-zfs-loses-its-mind/](https://sambowman.tech/blog/posts/mind-the-encryptionroot-how-to-save-your-data-when-zfs-loses-its-mind/)

生成摘要时出错

---

## 94. Pushing the Boundaries of C64 Graphics with Nuflix

**原文标题**: Pushing the Boundaries of C64 Graphics with Nuflix

**原文链接**: [https://cobbpg.github.io/articles/nuflix.html](https://cobbpg.github.io/articles/nuflix.html)

生成摘要时出错

---

## 95. Claude Sonnet 4.5

**原文标题**: Claude Sonnet 4.5

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-5](https://www.anthropic.com/news/claude-sonnet-4-5)

生成摘要时出错

---

## 96. Kagi News

**原文标题**: Kagi News

**原文链接**: [https://blog.kagi.com/kagi-news](https://blog.kagi.com/kagi-news)

生成摘要时出错

---

## 97. Launch HN: Airweave (YC X25) – Let agents search any app

**原文标题**: Launch HN: Airweave (YC X25) – Let agents search any app

**原文链接**: [https://github.com/airweave-ai/airweave](https://github.com/airweave-ai/airweave)

生成摘要时出错

---

## 98. Can you use GDPR to circumvent BlueSky's adult content blocks?

**原文标题**: Can you use GDPR to circumvent BlueSky's adult content blocks?

**原文链接**: [https://shkspr.mobi/blog/2025/09/can-you-use-gdpr-to-circumvent-blueskys-adult-content-blocks/](https://shkspr.mobi/blog/2025/09/can-you-use-gdpr-to-circumvent-blueskys-adult-content-blocks/)

生成摘要时出错

---

## 99. FlowSynx – Orchestrate Declarative, Plugin-Driven DAG Workflows on .NET

**原文标题**: FlowSynx – Orchestrate Declarative, Plugin-Driven DAG Workflows on .NET

**原文链接**: [https://flowsynx.io/](https://flowsynx.io/)

生成摘要时出错

---

## 100. Design of the SCHEME-78 Lisp-based microprocessor (1980)

**原文标题**: Design of the SCHEME-78 Lisp-based microprocessor (1980)

**原文链接**: [https://dl.acm.org/doi/10.1145/359024.359031](https://dl.acm.org/doi/10.1145/359024.359031)

生成摘要时出错

---

