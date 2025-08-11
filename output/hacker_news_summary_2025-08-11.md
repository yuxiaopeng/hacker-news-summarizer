# Hacker News 热门文章摘要 (2025-08-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 维基媒体基金会质疑英国网络安全法案条例

**原文标题**: Wikimedia Foundation Challenges UK Online Safety Act Regulations

**原文链接**: [https://wikimediafoundation.org/news/2025/08/11/wikimedia-foundation-challenges-uk-online-safety-act-regulations/](https://wikimediafoundation.org/news/2025/08/11/wikimedia-foundation-challenges-uk-online-safety-act-regulations/)

维基媒体基金会就英国《网络安全法案》(OSA)分类条例提起法律挑战，认为其威胁维基百科及其志愿贡献者。基金会认为，该条例，特别是第一类义务，可能会损害贡献者的隐私和安全，使维基百科面临操纵，并转移资源。他们认为，例如，要求身份验证可能会导致数据泄露和对志愿者的迫害。

高等法院于2025年8月11日驳回了这项挑战。然而，法院强调，Ofcom（英国通信管理局）和英国政府有责任在《网络安全法案》实施过程中保护维基百科，并指出如果他们未能做到这一点，可能会面临法律后果。法院建议Ofcom对规则进行灵活解释，或由议会对其进行修改。

发起这项法律挑战的原因在于，人们担心《网络安全法案》为高风险商业网站设计的严格义务会被不恰当地应用于维基百科。一位维基百科志愿编辑，用户：Zzuuzz，加入了这项挑战，强调了对个人贡献者权利的威胁。虽然没有挑战整个《网络安全法案》，但基金会特别关注分类条例。

基金会仍然致力于寻找保护维基百科的解决方案。他们强调了维基百科作为公共产品的重要性，它对志愿者管理的依赖，以及它在英国的广泛使用，包括它在保护文化遗产和威尔士语等语言方面的作用。Ofcom的首次分类决定预计将于今年夏季公布。

---

## 2. 微软CEO辞职后，GitHub不再独立。

**原文标题**: GitHub is no longer independent at Microsoft after CEO resignation

**原文链接**: [https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition](https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition)

在CEO Thomas Dohmke辞职后，GitHub将不再作为微软内部的独立公司运营。担任CEO近四年的Dohmke离职，寻求创业机会。他的离职标志着一个重大转变，微软将不再填补CEO职位，并将GitHub整合到其CoreAI组织中。

CoreAI是微软新成立的工程部门，由前Meta高管Jay Parikh领导，专注于为微软及其客户构建AI平台和工具。该部门还包括微软的平台和工具部门以及Dev Div团队。Parikh设想将该平台发展成为企业的“AI Agent工厂”。

Dohmke在给GitHub员工的备忘录中表示，GitHub的领导团队将继续其使命，作为微软CoreAI组织的一部分。他将留任到2025年底，协助过渡。

此举标志着微软对GitHub的策略发生了变化，结束了自2018年收购以来GitHub的独立运营状态。Dohmke最近在Decoder节目中的露面强调了他对竞争以及GitHub未来在软件开发中角色的关注，这使得他离职去创造潜在的AI竞争显得引人注目。

---

## 3. 我试遍了所有待办事项应用，最后还是用回了.txt文件。

**原文标题**: I tried every todo app and ended up with a .txt file

**原文链接**: [https://www.al3rez.com/todo-txt-journey](https://www.al3rez.com/todo-txt-journey)

阿利雷扎·巴希里详细讲述了他使用众多效率应用（Notion、Todoist、Things 3等）的历程，最终回归简单的`todo.txt`文件。他发现这些应用虽然最初很有吸引力，但要么变得过于复杂、昂贵或分散注意力，最终阻碍而非帮助了他的效率。

他的转折点是手机没电迫使他使用便签纸，这证明了简单列表的有效性。现在，他的系统围绕着一个每日更新的任务和笔记的文本文件展开。计划好的项目会列出时间，子弹头提供上下文。完成的任务会被删除或更新进度说明。

巴希里强调了这种极简主义方法的好处：持续的可见性、即时可访问性、人工智能集成以加快录入速度（可选）、快速添加任务、易于搜索、完全所有权、诚实以及面向未来的简洁性。他认为，真正的效率在于倾倒任务、定期检查列表并执行它们，而不是复杂的应用程序功能。

他解决了关于提醒（使用日历）、项目（使用笔记）、协作（使用工作工具）和移动访问（使用Dropbox与任何文本编辑器同步）的常见问题。他总结说，最好的效率系统是你始终如一使用的系统，并鼓励读者尝试他的文本文件方法一周，强调了简单性的力量。

---

## 4. OpenSSH 后量子密码学

**原文标题**: OpenSSH Post-Quantum Cryptography

**原文链接**: [https://www.openssh.com/pq.html](https://www.openssh.com/pq.html)

OpenSSH文档探讨了后量子密码学的实现，以防御未来量子计算机促成的“先存储，后解密”攻击。自9.0版本起，OpenSSH默认支持后量子密钥协商算法，最初是`sntrup761x25519-sha512`，最近是`mlkem768x25519-sha256`，后者是OpenSSH 10.0中的默认方案。当用户使用非后量子算法连接时，OpenSSH 10.1将发出警告，该警告可以使用`WarnWeakCrypto`选项禁用。

该文档阐述了采用后量子密码学的紧迫性，尽管目前尚不存在能够破解当前加密技术的量子计算机，但强调了攻击者今天存储加密数据以便以后解密的风险。虽然签名算法也容易受到量子计算攻击，但它们不像密钥协商算法那样构成同样的直接风险。

该文档还承认了对这些新后量子算法的担忧，并通过解释它们具有良好的安全裕度，并被实现为“混合”模式来捍卫其选择，即将后量子算法与经典算法相结合，确保即使后量子组件受到损害，混合算法仍然安全。它建议收到警告的用户将其SSH服务器更新到支持这些算法的版本，或有选择地禁用该警告。

---

## 5. 宇宙马蹄铁引力透镜中心的36B太阳质量黑洞

**原文标题**: 36B solar mass black hole at centre of the Cosmic Horseshoe gravitational lens

**原文链接**: [https://academic.oup.com/mnras/article/541/4/2853/8213862?login=false](https://academic.oup.com/mnras/article/541/4/2853/8213862?login=false)

好的，我已经阅读了来自所提供URL的文章“宇宙马蹄引力透镜中心360亿太阳质量的黑洞”。以下是摘要：

该研究论文提出了证据，表明位于造成“宇宙马蹄”这一著名引力透镜的星系中心存在一个估计质量为360亿太阳质量的超大质量黑洞（SMBH）。该研究利用哈勃太空望远镜和其他望远镜的高分辨率成像，结合复杂的透镜建模技术，来分析背景源星系的透镜图像。

关键发现是透镜星系中心SMBH的质量异常之高。这个结论来自于对透镜结构和透镜图像相对位置的详细分析。通过精心模拟透镜星系的质量分布，包括其恒星成分和暗物质晕，研究人员得以约束SMBH的质量。

这个异常巨大的SMBH质量表明，要么这些超大质量黑洞比之前认为的更常见，要么透镜星系经历了不寻常的吸积历史，使其能够增长到如此巨大的尺寸。作者指出，在透镜星系中观察到的类星体活动和恒星形成可能促进了SMBH的增长。

这项发现意义重大，因为它为星系及其中心黑洞的共同演化提供了宝贵的见解，尤其是在最大质量的系统中。该研究突出了引力透镜作为探测遥远星系及其中心SMBH的属性的工具的力量，这些SMBH通常太暗而无法直接研究。还需要进一步的观测和建模来证实这些发现，并研究可能导致如此巨大的黑洞形成的机制。

---

## 6. Trellis (YC W24) 招聘：自动化医疗预授权

**原文标题**: Trellis (YC W24) Is Hiring: Automate Prior Auth in Healthcare

**原文链接**: [https://www.ycombinator.com/companies/trellis/jobs/Cv3ZwXh-forward-deployed-engineers-all-levels-august-2025](https://www.ycombinator.com/companies/trellis/jobs/Cv3ZwXh-forward-deployed-engineers-all-levels-august-2025)

Trellis (YC W24) 正在招聘前线部署工程师（所有级别），利用人工智能自动化预先授权流程并简化医疗保健文书工作。这家位于旧金山的初创公司由斯坦福大学人工智能实验室衍生而来，并获得 YC 等机构的支持，通过自动化文件接收、预先授权和申诉，帮助医疗保健提供商更快地治疗更多患者。

Trellis 的前线部署工程师将直接与医疗保健提供商和制药公司合作，了解他们的运营挑战并实施人工智能驱动的解决方案。职责包括技术实施（构建人工智能工作流程和数据管道）、客户协作、数据工程（处理复杂的医疗保健数据）、产品开发（构建定制界面）和战略规划。

Trellis 正在寻找对人工智能和医疗保健数据充满热情、希望产生可衡量的影响并且能够胜任多项工作的候选人。该公司拥有一支世界一流的团队，并提供极高的自主权机会。

Trellis 的人工智能代理接受了数百万个临床数据点的训练，可以将非结构化文档转换为 EHR 中的结构化数据，从而带来缩短治疗时间、提高授权率和增强药物计划表现等益处。该公司的目标是解决占美国医疗保健支出 20% 以上的行政成本问题。

---

## 7. Claude Code，你只需它就够了。

**原文标题**: Claude Code is all you need

**原文链接**: [https://dwyer.co.za/static/claude-code-is-all-you-need.html](https://dwyer.co.za/static/claude-code-is-all-you-need.html)

本文讲述了作者使用Anthropic的终端编码工具Claude Code的经验，以及它如何在他们的工作流程中取代了GPT。作者赞扬了Claude Code与现有工作流程的无缝集成、易用性和有效性。他们描述了使用Claude Code构建的几个项目，包括一个“自主创业公司构建器”、一个SplitWise替代品、一个AI海报制作工具等等。

一个关键点是作者的“氛围编码”方法，即他们主要通过与AI模型的交互来开发软件，专注于所需的功能，而不是直接编写或编辑代码。他们用一个SplitWise克隆来说明这一点，展示了一个详细的规范文件如何能够以最小的努力产生一个完全可用的CRUD应用程序。

作者强调了向模型提供详细输入以及使用“危险地跳过权限”标志的重要性。他们还讨论了“自主创业公司构建器”项目，在该项目中，Claude Code被赋予了一个VPS和开发创业想法的指令。虽然由此产生的服务器监控应用程序有些误导，但作者对该工具在最少的人工输入下配置完整的全栈Web应用程序的能力印象深刻。

作者遇到了一个障碍，Anthropic的使用政策标记了该创业公司未经人工监督自动发布内容，导致帐户被阻止。

---

## 8. 混合自定义元素、Web Components 和 Markdown 的乐趣

**原文标题**: The Joy of Mixing Custom Elements, Web Components, and Markdown

**原文链接**: [https://deanebarker.net/tech/blog/custom-elements-markdown/](https://deanebarker.net/tech/blog/custom-elements-markdown/)

本文探讨了 Markdown 和自定义元素（Web Components）之间的协同作用，以创建更丰富、更复杂的 Web 内容。作者强调了 Markdown 在用更易读写的语法替代复杂 HTML 方面的简洁性。虽然 Markdown 允许与 HTML 混合使用，但它并没有解决可重复使用的复杂组件的问题。这就是自定义元素发挥作用的地方。

自定义元素是一种受现代浏览器支持的 Web 标准，它允许开发者定义自定义 HTML 标签，这些标签可以通过简单的标记输出复杂的 DOM 结构。本质上，它们充当 HTML 宏，简化源代码，同时产生复杂输出。作者演示了如何在 Markdown 文档中使用简单的 `<subscribe-to />` 标签，并通过自定义元素定义将此标签扩展为客户端上功能完整的订阅表单。

作者强调，Markdown 处理文本格式，而自定义元素处理更复杂的 UI 元素，从而形成强大的组合。文章还讨论了预处理 Markdown 的必要性，以解决自定义元素中自闭合标签和多行属性的限制。此外，作者还深入探讨了使用 Markdown 预处理创建微型语言的想法，但警告不要过度复杂化该过程。最后，作者谈到了自定义元素中的语言设计，强调了最大限度地减少编辑器所需的信息和最大限度地提高代码效率的重要性。虽然在服务器端处理 Markdown 很常见，但作者也提到了在客户端执行此操作的可能性。

---

## 9. 定价页面 - 精选定价页面设计图库

**原文标题**: Pricing Pages – A Curated Gallery of Pricing Page Designs

**原文链接**: [https://pricingpages.design/](https://pricingpages.design/)

本文精选了一系列定价页面设计案例，展示了不同公司呈现其定价模式的方式。该合集突出了定价页面中使用的各种设计元素和策略，包括：

*   **定价模式：** 基于使用量、定制定价、分层定价、月度/年度切换。
*   **设计元素：** 堆叠卡片、标准表格、对比表格、功能复选标记、功能列表、基于使用量的计算器。
*   **行业：** 展示的公司涵盖多个行业，包括人工智能与机器学习、内容与媒体、设计与创意、开发者工具与基础设施、商业与效率、金融科技与金融服务以及人力资源与招聘。

本文主要提供了一系列真实的定价页面示例，旨在为希望创建或改进自身定价页面的设计师和企业提供灵感。每个条目都包含公司名称、对所用设计或定价模式的简要描述以及指向实际定价页面的链接。本文根据这些实际案例指出了设计定价页面时可以采用的各种方法。

---

## 10. 制度记忆的价值

**原文标题**: The Value of Institutional Memory

**原文链接**: [https://timharford.com/2025/05/the-value-of-institutional-memory/](https://timharford.com/2025/05/the-value-of-institutional-memory/)

蒂姆·哈福德的文章《机构记忆的价值》强调了组织保留和利用其集体知识的重要性。他以一个疏浚团队因丢失历史记录而无意中移除运河塞的轶事开头，说明了机构失忆症的潜在后果。

哈福德提供了几个未能保存机构记忆导致重大问题的例子。他引用了大众汽车屡次发生的排放测试作弊丑闻以及挑战者号和哥伦比亚号航天飞机灾难，这些事件中都由于忘记了过去的教训而发生了类似的错误。他还讨论了洛克希德公司的三星客机，证明了缺乏持续生产导致专业知识的丧失和成本的增加。

哈福德指出了导致机构健忘症的几个因素：员工流动、物理档案的退化、数字格式的过时以及有意识地删除记录。他指出英国的“疾风一代”丑闻和美国政府网页的删除是有意遗忘并造成有害后果的例子。

文章强调，即使是努力保存信息的组织也可能面临困难。文章最后敦促组织积极对抗机构失忆症，以避免重蹈覆辙并失去宝贵的知识。

---

## 11. Chrome VRP小组决定为这份报告奖励25万美元。

**原文标题**: The Chrome VRP Panel has decided to award $250k for this report

**原文链接**: [https://issues.chromium.org/issues/412578726](https://issues.chromium.org/issues/412578726)

Chrome漏洞奖励计划（VRP）小组已为一份关于Chromium项目的安全报告颁发了25万美元的奖金。这表明该报告详细描述了Chromium代码库中一个非常重要或复杂的漏洞。巨额奖励表明，如果该漏洞被利用，可能会导致严重的安全性后果。虽然所提供的标题和内容中没有详细说明该漏洞的具体细节，但该公告强调了Chrome VRP持续致力于激励安全研究，并奖励对Chromium浏览器中安全漏洞的负责任披露。该计划在识别和缓解潜在的安全风险方面发挥着关键作用，从而在这些风险在野外被利用之前，增强了Chrome的整体安全性和稳定性，使其用户受益。高额奖励也再次证明了漏洞赏金计划在吸引熟练的安全研究人员以及促进软件安全协作方法方面的有效性。

---

## 12. 大规模软件设计

**原文标题**: Designing Software in the Large

**原文链接**: [https://dafoster.net/articles/2025/07/22/designing-software-in-the-large/](https://dafoster.net/articles/2025/07/22/designing-software-in-the-large/)

本文总结了《软件设计哲学》中的关键概念，重点关注大型软件系统中为实现可维护性而进行的复杂度管理。复杂度源于依赖性和晦涩性，两者都会阻碍理解和修改。

当代码无法独立理解时，就会产生依赖性，从而导致变更放大和认知负荷。依赖性复杂度的主要因素包括：重复、异常、继承和时序分解。解药是内聚的代码，通过深度模块实现——具有小接口并提供实质性功能的模块。

晦涩性源于不清晰或隐藏的信息，导致未知的未知和增加的认知负荷。其影响因素包括：模糊的名称、不一致性、不充分的文档以及某些间接用法。解决方案是显而易见的代码，其特点是精确的名称、一致性、详尽的文档和清晰的格式。

本文强调了一种战略思维，提倡积极投资于清晰的设计和问题解决，而不是仅仅关注功能完成的纯粹战术方法。这包括积极减少开发过程中引入的复杂度。核心要点是，能工作的代码是不够的；保持低复杂度对于长期的软件可维护性至关重要。

---

## 13. Zig中使用SIMD实现更快的子字符串搜索

**原文标题**: Faster substring search with SIMD in Zig

**原文链接**: [https://aarol.dev/posts/zig-simd-substr/](https://aarol.dev/posts/zig-simd-substr/)

本文详细介绍了作者探索使用SIMD（单指令多数据流）加速 Zig 中子字符串搜索的过程，相比于标准库的 `std.mem.indexOf`，性能得到了显著提升。

作者基于 Wojciech Muła 的工作实现了一种 SIMD 友好的算法，该算法使用 SIMD 寄存器，将“needle”（要搜索的子字符串）的第一个和最后一个字符与“haystack”（要搜索的文本）的 32 字节块进行比较。这可以识别潜在的匹配项，并显著减少所需的完整子字符串比较次数。

使用完整《白鲸记》文本的基准测试表明，与 `std.mem.indexOf` 相比，速度提高了 59%，CPU 周期减少了 80%。

随后，本文探讨了优化字符选择以减少分支预测错误的方法，即选择 needle 中最稀有的字符而不是第一个和最后一个字符。 这使性能进一步提高了 9%，并显著减少了分支预测错误。

最后，作者讨论了将代码适配到 AVX-512（一种更新的 SIMD 指令集，每次处理 64 字节）的情况。虽然无法直接测试，但作者预计会有显著的速度提升。作者还分析了在较小字符串上的性能，令人惊讶地发现 SIMD 算法仍然更快，尽管绝对时间差很小。

结论强调了 SIMD 在 Zig 中进行子字符串搜索的有效性，并突出了未来可以改进的潜在领域。

---

## 14. 移植到OS/2 – GitPius

**原文标题**: Porting to OS/2 – GitPius

**原文链接**: [https://gitpi.us/article-archive/porting-to-os2/](https://gitpi.us/article-archive/porting-to-os2/)

本文详细介绍了Microrim公司1987年将其R:BASE System V数据库管理系统从DOS移植到OS/2的過程。面对IBM即将发布的OS/2公告的紧迫期限，Microrim承诺展示一个可用的OS/2版本。该公司旨在利用OS/2的16MB内存来克服DOS的限制并提高性能。

Microrim的策略涉及一个两阶段的过程：首先，将语言从FORTRAN转换为C，然后是实际的DOS到OS/2移植。由于OS/2缺乏FORTRAN编译器，因此必须转换为C。他们使用Rapidtech Systems的FORTRix-C翻译器来加速这个过程，然后进行手动完善。

OS/2的移植本身由一位工程师在三个月内完成，R:BASE System V的模块化设计和结构良好的代码使移植变得更加容易。Microrim选择直接移植，立即利用OS/2更大的内存和多任务处理能力，而不是选择“家族应用程序”，后者虽然可以在DOS和OS/2上运行，但会限制功能。他们优先考虑一个单独的OS/2应用程序，以充分利用新操作系统的功能。他们决定使用标准数学库，牺牲一些在没有数学协处理器系统上的速度来提高准确性。最后，Microrim在R:BASE中构建了自己的配置控制系统，以管理DOS和OS/2版本之间的更新。

---

## 15. AOL将停止拨号上网服务

**原文标题**: AOL to discontinue dial-up internet

**原文链接**: [https://www.nytimes.com/2025/08/11/business/aol-dial-up-internet.html](https://www.nytimes.com/2025/08/11/business/aol-dial-up-internet.html)

无法访问文章链接。

---

## 16. UI 与 API 与 UAI

**原文标题**: UI vs. API. vs. UAI

**原文链接**: [https://www.joshbeckman.org/blog/practicing/ui-vs-api-vs-uai](https://www.joshbeckman.org/blog/practicing/ui-vs-api-vs-uai)

乔什·贝克曼的博客文章《UI vs. API vs. UAI》介绍了用户代理接口（UAI）的概念，与更成熟的用户界面（UI）和应用程序编程接口（API）并列。他认为，由于人工智能代理（如大型语言模型）越来越多地代表人类执行任务，UAI设计正逐渐成为一个关键的考量因素。

作者强调，在应用程序开发中，所有三种接口（UI、API 和 UAI）都应被视为同等重要。在构建功能时，开发人员需要有意识地设计它们，使其可以通过所有三种接口访问和理解。此外，底层应用程序逻辑的更改不应无意中降低任何接口的质量。

一个关键原则是将业务逻辑集中在底层应用程序中，而不是嵌入到任何单个接口中。这确保了所有接口的一致性。特定于接口的呈现和交互模式可以合法地不同，但核心功能应集中定义。

作者使用一个不允许周末预订的预订系统作为例子。与其实现一个阻止周末的 UI 特定日期选择器，不如在应用程序的核心逻辑中定义该限制。然后，UI 和 UAI 都可以访问该定义，并在各自的接口中适当地呈现它。

简而言之，贝克曼提倡一种全面的接口设计方法，确保功能在 UI、API 和新兴的 UAI 中都是可访问、一致且定义明确的，以满足人类和 AI 用户的需求。

---

## 17. Apache Iceberg V3规范：提升数据湖效率与灵活性

**原文标题**: Apache Iceberg V3 Spec new features for more efficient and flexible data lakes

**原文链接**: [https://opensource.googleblog.com/2025/08/whats-new-in-iceberg-v3.html](https://opensource.googleblog.com/2025/08/whats-new-in-iceberg-v3.html)

本文宣布 Apache Iceberg V3 规范，重点介绍旨在弥合数据湖和数据仓库之间差距的新功能。 主要改进侧重于大规模数据集的效率和灵活性。

**删除向量：** V3 引入了二进制删除向量，使用 Roaring 位图实现，以有效处理行级删除。 此方法将位图附加到每个数据文件，指示已删除的行，与以前的位置删除文件方法相比，显著提高了查询性能。

**默认列值：** V3 允许在添加新列时指定默认值，从而简化了模式演变。 这消除了对昂贵且具有破坏性的回填的需求，从而使模式更改变得即时且非破坏性。

**增强的数据类型和沿袭：** V3 规范通过改进的行级沿袭跟踪（用于审计和 CDC 管道）扩展了 Iceberg 的功能。 它还引入了更丰富的数据类型，包括用于半结构化数据的 VARIANT、用于地理空间分析的 GEOMETRY/GEOGRAPHY 以及纳秒级精度的时间戳。

总而言之，这些 V3 功能有助于构建更高效、更灵活和更开放的数据湖仓架构，从而实现更快的数据操作并消除数据湖和数据仓库之间的传统权衡。 Google 强调了其对 Iceberg 项目的支持和贡献，并鼓励用户探索 BigQuery 中的 BigLake 表（用于 Apache Iceberg），以获得托管的 Iceberg 体验。

---

## 18. 使用 Macroquad 在 Rust 中实现的简单像素物理模拟器

**原文标题**: A simple pixel physics simulator in Rust using Macroquad

**原文链接**: [https://github.com/gale93/sbixel](https://github.com/gale93/sbixel)

本文介绍了“Sbixel”，一个用 Rust 语言编写的简单像素物理模拟器，它使用了 Macroquad 游戏引擎。作者将其作为学习项目创建，并强调了 Macroquad 的便捷性和强大之处。

Sbixel 采用“扇区”系统来优化性能，通过将模拟集中在活跃像素区域。所有模拟设置都可以在 `src/def.rs` 中进行配置。作者明确表示，这个项目是一个基础学习沙盒，对进一步开发的期望有限。

然而，一个宽松的“TODO”列表包括潜在的改进，例如升级水模拟、改进沙/水交互、仅在活跃扇区中渲染像素、重构像素处理逻辑，以及可能添加气体模拟和静态对象。作者欢迎其他人的贡献。

本文提供了入门指南：确保已安装 Rust，然后使用 `cargo run` 运行项目。作者鼓励探索和试验代码。建议使用 `cargo run --release` 命令以提高性能。

---

## 19. Llama.cpp 中 Mistral 集成得到改进

**原文标题**: Mistral Integration Improved in Llama.cpp

**原文链接**: [https://github.com/ggml-org/llama.cpp/pull/14737](https://github.com/ggml-org/llama.cpp/pull/14737)

本文讨论了改进 Mistral 模型与 llama.cpp 集成的方案。目前将 Mistral 模型转换为 GGUF（llama.cpp 使用的格式）的过程效率低下，需要先转换为 Hugging Face 格式，这可能会引入错误。本次更新旨在解决这个问题，允许直接从 Hugging Face 转换为 GGUF，并在 llama.cpp 中原生注册 Mistral 架构。

主要改进包括用于直接转换的新脚本 `convert_mistral_to_gguf.py` 以及对 Mistral 模型的原生支持。它还建议使用 `mistral-common` 库进行分词，可通过 FastAPI REST API 访问，以确保准确性。建议用户使用 llama.cpp 服务器的 `/completions` 路由，并设置 `return_tokens=True` 以实现最佳集成。目前不支持多模态。

讨论包括来自 llama.cpp 社区的反馈，包括将滑动窗口注意力大小存储在 GGUF 文件中，以及将新的转换脚本合并到现有的 `convert_hf_to_gguf.py` 中，以便于维护和改善用户体验的建议。作者解决了关于代码重复的问题，并解释了单独文件的理由，同时努力解决与 pydantic 版本冲突和 pillow 冲突相关的 CI 错误。此外，还有一个使用 Voxtral 模型支持音频模型的有趣补充。

---

## 20. 全球图文电视概览

**原文标题**: A Global Look at Teletext

**原文链接**: [https://text-mode.org/?p=23643](https://text-mode.org/?p=23643)

本文概述了图文电视的全球概况，追溯了其在不同国家和标准下的起源和演变。文章从20世纪70年代英国的Ceefax和ORACLE开始，解释了以其块状图形而闻名的世界系统图文电视（WST）标准如何在欧洲被广泛采用。随后，文章将WST与法国的Antiope标准进行了对比，后者提供了更复杂的图形，并挑战了美国在技术领域的主导地位。

文章详细介绍了加拿大Telidon的开发及其矢量图形，以及美国复杂的局势，在那里，多种标准在NAPLPS被采用之前展开竞争。文章认为，NAPLPS虽然被认为是美国的发明，但严重依赖于法国和加拿大的公共资助研究。

文章探讨了图文电视在欧洲的政治和文化意义，强调了公共服务广播公司对其的采用，以及其在南斯拉夫等国家的使用。文章还提到了东欧集团（包括苏联）的延迟采用，并提到了俄罗斯独立图文电视广播的独特案例。

此外，文章还探讨了将WST适应不同语言（尤其是那些使用非拉丁字母的语言）的挑战，并将其与日本先进的JTES标准进行了对比，后者旨在支持大型字符集、可定制字体甚至声音。总而言之，文章强调了世界各地对图文电视的不同方法，反映了不同的技术能力、政治议程和文化需求。

---

## 21. 从现代汽车数据网络中消失

**原文标题**: Vanishing from Hyundai’s data network

**原文链接**: [http://techno-fandom.org/~hobbit/cars/ev/offnet.html](http://techno-fandom.org/~hobbit/cars/ev/offnet.html)

由于隐私顾虑以及防止远程追踪或干预的意愿，作者详细描述了其断开现代 Kona EV 与现代 Bluelink 数据网络连接的过程。他们在经销商处拒绝激活 Bluelink，并寻求物理禁用汽车的蜂窝通信。

他们最初的步骤是禁用车顶内衬中的麦克风，以防止窃听。经过一番研究，他们确定了汽车音频/视频主机内的蜂窝调制解调器。然后，作者小心地拆卸仪表板面板，移除了主机。

在工作台上，他们找到了 Continental 制造的蜂窝调制解调器子板。他们物理断开了天线引线，有效地切断了汽车的蜂窝连接。作者曾考虑移除整个子板，但保留了它，因为它还处理 Sirius XM（仅接收）和 P-CAN 连接，后者提供在主机上显示的车辆数据。

重新组装并重新安装主机后，其功能正常，没有任何关于缺少蜂窝调制解调器的警告。通过硬重置解决了日期/时间设置的小问题。后视镜上之前可以使用的 BlueLink 按钮变得无法操作。作者成功实现了让他们的汽车“进入黑暗模式”并断开与现代数据网络连接的目标。

---

## 22. 苹果将 OpenAI 的 GPT-5 带到 iOS 和 macOS。

**原文标题**: Apple brings OpenAI's GPT-5 to iOS and macOS

**原文链接**: [https://arstechnica.com/ai/2025/08/apple-brings-openais-gpt-5-to-ios-and-macos/](https://arstechnica.com/ai/2025/08/apple-brings-openais-gpt-5-to-ios-and-macos/)

塞缪尔·阿克松的这篇文章讨论了苹果公司预期将OpenAI的GPT-5模型集成到其iOS 26、iPadOS 26和macOS Tahoe 26操作系统中，预计将于9月份左右发布。虽然GPT-5已经在GitHub Copilot和微软Copilot等平台上可用，但它在苹果设备上的到来将升级iOS中现有的ChatGPT集成。

这篇文章强调了GPT-5相对于其前代的显著改进，包括据称幻觉减少了80%以及一种新的系统，该系统允许模型根据用户的提示自动选择推理优化模式和非推理模式。 这篇文章提出了关于这种新系统将如何在iOS中实施的问题，特别是对于免费和付费ChatGPT用户，以及苹果是否允许手动模型选择。

虽然苹果主要依靠其自己的“苹果智能”模型来实现大多数与人工智能相关的功能，但它允许用户在苹果模型不足时将提示提交给ChatGPT。 与苹果的本地模型相比，GPT-5具有更大的参数规模，有望显著增强其功能。

文章最后暗示，虽然GPT-5的立即集成可能不会大幅改变现有的ChatGPT实现，但苹果拥有未来的AI计划，可能会在随后的操作系统更新中带来更重大的变化。

---

## 23. 米约高架桥

**原文标题**: Millau Viaduct

**原文链接**: [https://www.fosterandpartners.com/projects/millau-viaduct](https://www.fosterandpartners.com/projects/millau-viaduct)

位于法国南部的米约高架桥，是建筑成功融入基础设施设计的典范。它由建筑师和结构工程师紧密合作打造而成，完成了A75高速公路中至关重要的缺失环节，提供了从巴黎到地中海的高速通道。

本文强调，该桥的设计优先考虑优雅和最小的环境影响，而非单纯地庆祝河流的跨越。其斜拉索、桅杆式结构实现了最佳跨度和透明度。

米约高架桥在竣工时打破了多项纪录，包括最高的桥塔和公路桥面，并超越埃菲尔铁塔成为法国最高的建筑物。其设计特点，如适应桥面膨胀的A型框架柱分裂，既保证了结构完整性，又提升了视觉吸引力。锥形柱最大限度地减少了它们对景观的视觉影响，创造了一种轻盈而流畅的设计，与周围环境和谐统一，有效地充当了“环境雕塑”。最后，本文还提供了同一设计公司的其他项目链接。

---

## 24. GPT-OSS-120B仅需8GB显存和64GB+系统内存即可运行

**原文标题**: GPT-OSS-120B runs on just 8GB VRAM & 64GB+ system RAM

**原文链接**: [https://old.reddit.com/r/LocalLLaMA/comments/1mke7ef/120b_runs_awesome_on_just_8gb_vram/](https://old.reddit.com/r/LocalLLaMA/comments/1mke7ef/120b_runs_awesome_on_just_8gb_vram/)

无法访问文章链接。

---

## 25. 超越 memcpy 的速度

**原文标题**: Going faster than memcpy

**原文链接**: [https://squadrick.dev/journal/going-faster-than-memcpy](https://squadrick.dev/journal/going-faster-than-memcpy)

本文详细探讨了对高性能发布-订阅系统Shadesmar中超越标准`memcpy`的内存复制操作的优化。性能分析表明，`memcpy`是大消息的主要瓶颈。

作者剖析了glibc的`memcpy`实现 (`__memmove_avx_unaligned_erms`)，注意到其使用`memmove`处理重叠内存区域，增强型REP MOVS (ERMS) 进行优化循环，AVX向量化实现32字节复制，以及对未对齐指针的处理。

实现了几种替代的内存复制方法并进行了基准测试：使用汇编的基本REP MOVSB，对齐的AVX复制，流式对齐的AVX复制（跳过缓存），以及流式对齐的AVX复制并带预取。 还研究了循环展开和使用自定义`Copier`接口进行多线程处理。

Shadesmar中的`Copier`接口允许自定义内存传输实现，最初旨在用于跨设备（CPU-GPU）数据传输。 创建了一个`MTCopier`适配器，以将多线程支持添加到任何`Copier`。

基准测试结果表明，`std::memcpy`通常提供最佳的整体性能，能很好地适应硬件。 流式预取复制在大尺寸复制（>1MB）时表现良好。 展开的AVX复制在中小型尺寸时占据优势。 作者得出的结论是，除非满足特定的对齐要求且性能至关重要，否则坚持使用`std::memcpy`是最佳方法。

---

## 26. 人工智能基础概念精选文章

**原文标题**: Hand-picked selection of articles on AI fundamentals/concepts

**原文链接**: [https://aman.ai/primers/ai/](https://aman.ai/primers/ai/)

本文精选了一系列资源，涵盖人工智能的基础概念，包括从模型构建到部署和评估的整个机器学习流程。

其组织结构分为几个关键领域：**算法/架构**，涵盖从经典机器学习（线性回归、支持向量机）到高级深度学习（GAN、Transformer、扩散模型）；**数据/训练**，涉及数据预处理、模型初始化、训练技巧（梯度下降、正则化）和微调策略；**语音、视觉和自然语言处理**，详细介绍特定于这些模态的技术和模型；**多模态**，重点关注视觉-语言模型；**模型**，列出各种著名的AI模型，如BERT、GPT、CLIP和LLaMA；**离线/在线评估**，涵盖指标和A/B测试；**MLOps**，解决数据漂移、工具和测试问题；**设备端AI**，探索模型压缩和隐私；**项目规划**，包括目标设定和项目管理框架；以及一个**杂项**部分，涵盖调试技巧、数学基础和实际考虑。

该系列旨在提供全面的知识，从基本概念到高级技术，如参数高效微调和分布式训练。资源列表还重点介绍了诸如命名实体识别和机器翻译等特定任务，以及相关基准。它还提供了关于检测幻觉和在大型语言模型中缓解幻觉等主题的见解。最后，本文包括有价值的实践元素，如面试问题和调试建议，使其成为学习和人工智能领域实际应用的有用指南。

---

## 27. CPU时钟周期内的操作成本 (2016)

**原文标题**: Operation Costs in CPU Clock Cycles (2016)

**原文链接**: [http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/](http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/)

“No Bugs” Hare 的这篇文章提供了一份指南，旨在帮助理解常见 CPU 操作在时钟周期中的相对成本，以避免代码中的“过早悲观优化”。其中提供的图表给出了现代 x86/x64 CPU 上操作成本的大致数字（预计 ARM Cortex A 和 SPARC 上也具有相似的模式），并承认具体时序因 CPU 型号、编译器和程序细节而异。

文章涵盖了 ALU/FPU 操作（仅限于寄存器间），由于并行性，像 ADD/MOV 这样的“简单”操作消耗不到一个周期。整数乘法/除法成本更高，乘法花费 1-7 个周期，除法花费 12-44 个周期。浮点运算的成本也各不相同，其中除法成本最高。向量运算（SSE/AVX/ARM Neon）允许并行处理数据。

分支（if 语句）如果 CPU 预测正确，则消耗 1-2 个周期，但预测错误可能会使 CPU 停顿 10-20 个周期。内存访问速度因缓存级别（L1 最快，RAM 最慢）而异，突出了数据局部性的重要性。内存写入通常比读取便宜。代码局部性也很重要，可以通过内联和使用 `__builtin_expect()` 来改善。

文章还讨论了 NUMA（非一致性内存访问）架构，这种架构在多路服务器中很常见，访问不同插槽上的内存会增加显著的延迟（100-300 个周期）。最后，它提到了原子操作，如 CAS（比较并交换），由于同步要求，原子操作比常规内存访问慢得多，在单核上花费约 15-30 个周期，在 NUMA 配置中则更多。

---

## 28. Meta泄密第一部分：以色列与Meta

**原文标题**: Meta Leaks Part 1: Israel and Meta

**原文链接**: [https://archive.org/details/meta_leaks_part_1](https://archive.org/details/meta_leaks_part_1)

“Meta泄露第一部分：以色列与Meta”文档，托管于互联网档案馆，似乎是一份泄露的信息集合（可能包含EPUB格式）。元数据显示，该文档主要关注以色列与社交媒体公司Meta之间的关系。

元数据中的关键信息包括：

*   **标题：** Meta泄露第一部分：以色列与Meta
*   **来源：** 2025年8月11日由“icw_nru”上传至互联网档案馆。
*   **格式：** 提供多种格式，包括EPUB、PDF和纯文本（OCR）。
*   **主题：** 归类于“icw”和“meta”下。
*   **OCR：** 文档进行了OCR（光学字符识别），表明其最初可能是一份扫描文档或基于图像的文件。这意味着文本可搜索和复制。
*   **标记：** 该文档可以被标记为存在诸如图形暴力、仇恨言论或虚假信息等问题。

该文档本身的存在表明，有关以色列与Meta之间联系的信息已被泄露。在未访问和分析文档内容的情况下，无法详细说明该关系的具体细节或泄露的性质。提供包括基于文本格式在内的多种下载选项，表明该信息可供进一步审查和分析。

---

## 29. 编译Lisp：Lambda提升

**原文标题**: Compiling a Lisp: Lambda lifting

**原文链接**: [https://bernsteinbear.com/blog/compiling-a-lisp-12/](https://bernsteinbear.com/blog/compiling-a-lisp-12/)

Max Bernstein的博文讲述了他学习Ghuloum Lisp编译器教程的经历，特别关注闭包转换（最初误认为是Lambda提升）。为了清晰起见，他用Python重写了编译器，省略了S表达式读取器和指令编码。

博文的核心详细介绍了闭包转换的实现，这是一个通过以下方式转换lambda的过程：

1. 跟踪绑定变量和自由变量。
2. 为lambda分配代码对象。
3. 在闭包中捕获外部环境（自由变量）。

`LambdaConverter`类管理这一点，维护一个标签字典并递归地遍历程序的抽象语法树。`convert`方法处理不同的表达式类型（常量、变量、`if`语句、`lambda`表达式和`let`表达式），并根据需要更新绑定变量和自由变量集。`lambda`表达式被转换为`closure`形式，引用代码对象并列出它们的自由变量。`let`表达式需要小心处理绑定作用域。函数调用也被转换为“funcall”操作，但内置的原始函数除外。

文章随后转向将`closure`和`funcall`形式编译为汇编代码。编译闭包涉及在堆上为代码指针和自由变量分配空间，标记闭包，并增加堆指针。编译`funcall`需要保存栈上的空间，编译参数，调整栈指针，通过闭包指针执行调用，并恢复栈。汇编代码使用内联注释以提高清晰度。他强调了栈调整计算以及闭包标记/取消标记的挑战。

---

## 30. 乐队和银行劫匪都爱它，福特全顺迎来60周年

**原文标题**: Beloved by bands and bank robbers, the Ford Transit turns 60

**原文链接**: [https://www.bbc.com/news/articles/c0j97xegz5no](https://www.bbc.com/news/articles/c0j97xegz5no)

福特全顺：广受欢迎的厢型车迎来60周年

深受工匠、乐队甚至银行劫匪喜爱的福特全顺厢型车迎来60周年纪念。自1965年问世以来，它以其宽敞的空间、强大的动力和实用性彻底改变了厢型车市场，迅速成为企业的必备品，也是齐柏林飞艇乐队和诅咒乐队等巡演乐队的自由象征。

全顺的多功能性和速度也吸引了犯罪分子，在20世纪70年代为它赢得了“英国最受通缉的厢型车”这一略带戏谑的称号。虽然最初在英国生产，但为了降低成本，2013年生产转移到土耳其，这一举动引发了争议。尽管如此，福特强调全顺的英国血统，突出其在英国持续进行的工程、设计和发动机生产。

如今，福特专注于全顺的未来，特别是电动车型和软件集成，以提高效率并降低运营成本。该公司认为，厢型车用户的核心需求保持不变——可靠性、多功能性和可负担性——但实现这些目标的手段正在不断发展。然而，厢型车市场日益激烈的竞争对全顺的统治地位构成了挑战，可能会削弱曾经是其成功的关键因素的品牌忠诚度。

---

## 31. C 语言中的泛型容器：使用 Maybe 实现安全除法

**原文标题**: Generic Containers in C: Safe Division Using Maybe

**原文链接**: [https://uecker.codeberg.page/2025-08-10.html](https://uecker.codeberg.page/2025-08-10.html)

在C语言中实现“Maybe”类型以处理潜在计算错误，特别是安全整数除法的探索。受Haskell的Maybe启发，该方法使用一个包含布尔`ok`标志和值的结构体，指示计算是否成功。定义了用于创建“Just”（成功）和“Nothing”（错误）Maybe实例的宏。

本文强调了错误检查的重要性，不仅仅是简单的除以零，还指出了在C语言中用`INT_MIN`除以-1时的未定义行为。文章展示了一个最初有缺陷的“safe_divide”函数，并使用GCC的带符号整数溢出清理器分析了其汇编代码。清理器揭示了一条导致陷阱指令的隐藏代码路径，表明该函数不完整。

在修正了错误检查以考虑`INT_MIN`的情况后，生成的汇编代码不再触发清理器，证明了`safe_divide`函数现在确实能够避免整数溢出和除以零的错误，至少由编译器及其清理器静态确定。

作者认为，虽然这种方法有限，但它可以成为确保C代码特定部分安全性的有用工具，特别是与使用VLA和可变修改类型进行边界检查等其他技术结合使用时。文章最后邀请读者探索一个实验性库，并分享改进该方法的想法。

---

## 32. 福特计划推出三万美元电动卡车，力求变革

**原文标题**: Ford Aims for Revolution with $30k Electric Truck

**原文链接**: [https://www.thedrive.com/news/ford-aims-for-revolution-with-30000-electric-truck](https://www.thedrive.com/news/ford-aims-for-revolution-with-30000-electric-truck)

福特计划于2027年推出一款价格亲民的中型电动卡车，目标起售价约为3万美元。这款卡车在尺寸上与福特 Maverick 相似，但内部空间更大，堪比丰田 RAV4。它不会取代 Maverick，并计划具备 BlueCruise 功能。 福特的目标是使其0-60英里/小时的加速时间与 EcoBoost Mustang 相似（4.5 秒）。 生产将在肯塔基州路易斯维尔组装厂进行，采用先进的制造技术。

该卡车将基于新的“通用电动汽车平台”构建，采用 400 伏架构和来自福特 BlueOval 电池园的磷酸铁锂电池。 福特计划提供无线软件更新，以实现持续改进。 提到的一个关键特性是，可能在驾驶室和货箱之间设置类似于雪佛兰 Avalanche 风格的货物通道。

福特的愿景超越了这款卡车，通用电动汽车平台旨在支撑各种车辆，从小型汽车到三排 SUV。 “通用电动汽车生产系统”将在最终组装之前，将车辆组装成三个独立的部分（前部、后部和电池/结构），从而可以在同一平台上高效生产不同类型的车辆。 这种方法旨在减少零件、紧固件、工作站和组装时间，最终降低成本。 福特声称这款电动汽车的拥有成本将低于一辆车龄三年的特斯拉 Model Y。

---

## 33. 展示HN：一百万行

**原文标题**: Show HN: 1 Million Rows

**原文链接**: [https://1mrows.pages.dev](https://1mrows.pages.dev)

此"Show HN"帖子介绍"1 Million Rows"，一款专为处理大型数据集而设计的闪电般快速的管理工具。其主要焦点在于高效管理和显示一百万行数据的能力，并提供了一个演示。

该帖子重点介绍了该工具的各种用例，从常见的项目管理和销售漏斗跟踪，到更具体的应用，如员工入职、市场调研，甚至社交媒体管理。它将"1 Million Rows"定位为一种适用于不同业务需求的多功能解决方案。

一份详细的路线图概述了跨三个阶段的计划功能。第一阶段侧重于核心功能，如可定制的列表/表格、基于角色的访问、实时更新、状态跟踪、筛选和审计跟踪。第二阶段引入了诸如通知系统、提醒、讨论空间、看板视图、时间跟踪、依赖关系跟踪、Markdown文档创建和文件附件等功能。第三阶段旨在增加人工智能功能、移动应用程序、协作编辑、仪表板、集成、插件平台、Excel导入、计算列和计划报告。

该帖子积极鼓励用户反馈和参与，以塑造该工具的开发。它强调用户建议的重要性，并邀请用户联系进行讨论和进一步完善平台。最终，其目标是创建一个强大且用户驱动的数据管理工具，能够处理大量信息。

---

## 34. 优化我的磁盘使用程序

**原文标题**: Optimizing My Disk Usage Program

**原文链接**: [https://healeycodes.com/optimizing-my-disk-usage-program](https://healeycodes.com/optimizing-my-disk-usage-program)

本文详细介绍了对 macOS 上的快速磁盘使用程序 `dumac` 所做的性能优化。 该程序之前的版本使用 `getattrlistbulk` 来提高速度，作者在本文中针对线程调度开销和 inode 锁竞争方面的反馈进行了改进。

最初的版本使用了 Tokio，为每个处理的目录生成许多线程，导致不必要的开销和线程间通信。 切换到 Rayon 的工作窃取线程池消除了这个问题，复用了线程并减少了系统调用，从而带来了约 28% 的性能提升。 Instruments 确认了更少的线程和上下文切换。

进一步的优化针对用于对 inode（硬链接）进行重复数据删除的分片哈希集。 最初的分片逻辑 (`inode % SHARD_COUNT`) 由于目录内 inode 分配的顺序性而导致了锁竞争。 通过在取模之前移动 inode 值 (`inode >> 8`)，作者将连续的 inode 分组到同一个分片中，从而显着减少了锁冲突（观察到的锁冲突从平均 176.66 次减少到 4.66 次）。 这提高了时间局部性并最大限度地减少了分片间的竞争。 虽然测试了各种哈希函数，但这种简单的位移方法产生了相当的性能。 作者选择移动 8 位，基于大多数目录包含少于 256 个文件的假设。 这种 inode 分片改进带来了额外的约 5% 的性能提升。

---

## 35. 忠诚之花：纪念黑森的伊丽莎白受洗 (1598)

**原文标题**: Flowers of Fealty: Commemoration of the Christening of Elisabeth of Hesse (1598)

**原文链接**: [https://publicdomainreview.org/collection/christening-of-lady-elisabeth-of-hesse/](https://publicdomainreview.org/collection/christening-of-lady-elisabeth-of-hesse/)

《忠诚之花：黑森的伊丽莎白洗礼纪念（1598）》一文，基于巴伐利亚州立图书馆所藏资料，可能着重于1598年黑森的伊丽莎白洗礼仪式的历史意义和视觉记录。其核心主题是对为该场合制作的庆典书籍或纪念材料的分析。

该文可能探讨了通过伴随该事件的艺术品和文本所传达的象征意义和寓言含义。“忠诚之花”的标题表明了所描绘的花朵与对伊丽莎白及其家族应尽的忠诚之间的主题联系。

该文很可能探讨了洗礼仪式周围的政治和社会背景，强调其作为巩固家族联盟和展示黑森统治家族权力与声望的象征性事件的重要性。它将分析纪念册的具体内容，详细说明是谁委托制作的，谁为此做出了贡献（艺术家、作家），以及它的预期读者。

最终，该文旨在深入了解16世纪末此类洗礼是如何庆祝和记录的，从而有助于更广泛地理解当时的宫廷生活、宗教习俗和艺术赞助。对巴伐利亚州立图书馆藏品的关注表明，该文严重依赖于该图书馆内所藏的原始资料，提供了独特而知情的视角。

---

## 36. 列表与列表：通过互动小说学习Lisp基础 (1996)

**原文标题**: Lists and Lists: Basics of Lisp through interactive fiction (1996)

**原文链接**: [https://eblong.com/zarf/zweb/lists/](https://eblong.com/zarf/zweb/lists/)

该网页片段描述了1996年的互动小说游戏《Lists and Lists: Basics of Lisp through interactive fiction》，该游戏旨在教授Lisp编程语言的基本概念。该游戏很可能使用Parchment（一个基于Javascript的互动小说解释器）在网络浏览器中呈现。标题暗示了其核心关注点在于列表，这是Lisp中的一种基本数据结构。介绍性文字还提供了与一般互动小说信息相关的链接，例如“如何玩IF”以及指向“Zarf's IF”的链接，表明Zarf是创作者或是互动小说社区中的重要人物。游戏本身需要Javascript才能运行，表明它是设计为在网络浏览器中运行的。“Lists and Lists”本质上旨在通过将其置于互动小说类型中，使学习Lisp更具吸引力。

---

## 37. 维基百科败诉，未能推翻《网络安全法案》验证规则

**原文标题**: Wikipedia loses challenge against Online Safety Act verification rules

**原文链接**: [https://www.bbc.com/news/articles/cjr11qqvvwlo](https://www.bbc.com/news/articles/cjr11qqvvwlo)

维基百科的母公司维基媒体基金会针对英国《网络安全法案》规则发起的法律挑战失败，该规则可能迫使这家在线百科全书验证其用户的身份。基金会认为，这些为大型社交媒体平台设计的法规过于宽泛，可能会无意中适用于维基百科，从而威胁到其志愿者编辑的隐私和安全。

具体而言，维基媒体基金会担心根据该法案被归类为“第一类”，这将需要用户验证，或要求他们大幅限制英国境内的访问或禁用关键功能。政府坚称，它已经考虑过并且合理地拒绝了豁免维基百科。

虽然法院在此次司法审查中驳回了维基媒体的论点，但基金会强调，裁决也承认了英国通信管理局(Ofcom)和英国政府保护维基百科的责任。该判决还允许未来可能提出的法律挑战，如果英国通信管理局将维基百科归类为第一类，或者如果这些法规妨碍维基百科的运营。法律专家认为，在审查后，维基百科仍有可能免受最严格规则的约束。英国通信管理局承认法院的判决，并将继续其与根据《网络安全法案》对服务进行分类相关的工作。

---

## 38. 福特发布降低电动汽车价格的突破性工艺

**原文标题**: Ford reveals breakthrough process for lower priced EVs

**原文链接**: [https://www.theverge.com/ford-motor-company/757243/ford-ev-truck-breakthrough-model-t](https://www.theverge.com/ford-motor-company/757243/ford-ev-truck-breakthrough-model-t)

福特押宝全新“通用”汽车平台和制造工艺，以生产价格更低的电动汽车，旨在电动汽车市场实现“T型车时刻”。该公司计划打造一系列低成本电动汽车，从2027年在其肯塔基州组装厂生产的3万美元中型皮卡开始。福特预计今年在电动汽车和软件方面的亏损将超过50亿美元，凸显了这项举措的紧迫性。

新平台将可扩展，适用于各种车型，并配备支持空中更新的软件定义系统。它将使用更经济耐用的磷酸铁锂（LFP）电池。制造过程将从传统的装配线转变为具有多条同时汇聚的生产线的“装配树”。这个新过程减少了20%的零件、25%的紧固件和40%的工作站，从而使组装时间缩短了15%。福特预计拥有成本将低于一辆三年车龄的特斯拉Model Y。

该“通用”平台是硅谷一个为期三年的“臭鼬工厂”项目的成果。它承诺采用更简单的布线网络，并通过采用更便宜的磷酸铁锂电池来降低电池成本。电池将作为结构部件，充当车辆的地板，从而增强操控性和内部空间。新款卡车有望拥有比丰田RAV4更大的乘客空间以及一个足以容纳冲浪板的货箱。

“装配树”制造方法涉及三个子装配同时运行，用单个铝铸件取代许多较小的零件。该过程还旨在通过自动化和基于工具包的工作站来改善工人的工作效率。虽然需要在肯塔基州工厂投资20亿美元，但新流程将需要更少的工人，可能会导致买断或调动，但预计不会裁员。廉价电动汽车的概念对于福特的未来至关重要，尤其是在需求放缓以及使电动汽车投资盈利面临挑战的情况下。

---

## 39. 一百万张截图

**原文标题**: One Million Screenshots

**原文链接**: [https://onemillionscreenshots.com/?q=random](https://onemillionscreenshots.com/?q=random)

无法访问文章链接。

---

## 40. 自我担保承诺

**原文标题**: Self-Guaranteeing Promises

**原文链接**: [https://stephango.com/self-guarantee](https://stephango.com/self-guarantee)

本文介绍了“自我担保承诺”的概念，即无需信任第三方、可验证且不可逆转的承诺。作者将其与典型的承诺（如服务条款或公司结构）进行对比，后者可以被更改或撤销。

文中提供了关键示例：“文件覆盖应用”功能，您无需导出即可在其他应用程序中直接使用文件；以及“不锈钢”，其耐水性是一种内在的、可测试的品质。这些与公司在数据隐私或治理方面做出的不可执行的承诺形成对比，因为这些承诺可能会发生变化且超出您的控制范围。

文章认为，即使是开源也不能保证自由，因为数据仍然可能被锁定在专有格式中。虽然承认任何工具的未来都存在固有的不确定性，因为技术变革、业务失败或不断变化的需求，但作者提倡选择做出自我担保承诺的工具。通过选择具有内在的、可测试的品质的工具，以确保持续的可访问性和控制权，用户可以降低仅仅依赖于可能被打破的承诺所带来的风险。

---

## 41. 格雷厄姆：利用本地时钟属性同步时钟 (2022) [pdf]

**原文标题**: Graham: Synchronizing Clocks by Leveraging Local Clock Properties (2022) [pdf]

**原文链接**: [https://www.usenix.org/system/files/nsdi22-paper-najafi_1.pdf](https://www.usenix.org/system/files/nsdi22-paper-najafi_1.pdf)

本研究论文《Graham：利用本地时钟属性进行时钟同步（2022）》探索了一种新颖的时钟同步方法。它侧重于利用系统内本地时钟的属性来实现准确高效的同步，而不是仅仅依赖外部时间源。

其核心思想是，尽管单个时钟可能存在不准确或漂移，但它们具有某些可预测的特性。通过建模和分析这些本地行为，系统可以补偿误差并改善同步。Graham 方法可能涉及考虑时钟漂移率、稳定性以及历史性能等因素的算法。

该论文可能深入探讨了所提出的同步算法的细节，概述了其如何收集和处理本地时钟数据。它可能描述了用于表示时钟行为的数学模型，以及如何应用这些模型来纠正时间差异。该文档可能分析了该方法在准确性、对时钟故障的弹性以及通信开销方面的性能。评估指标可能包括同步误差界限、收敛时间和消息复杂度。

---

## 42. 静电之谜

**原文标题**: The enduring puzzle of static electricity

**原文链接**: [https://pubs.aip.org/physicstoday/article/78/8/54/3355922/The-enduring-puzzle-of-static-electricityEven](https://pubs.aip.org/physicstoday/article/78/8/54/3355922/The-enduring-puzzle-of-static-electricityEven)

无法访问文章链接。

---

## 43. 试试看

**原文标题**: Try and

**原文链接**: [https://ygdp.yale.edu/phenomena/try-and](https://ygdp.yale.edu/phenomena/try-and)

本文探讨了“try and”后接原形动词的语言现象，这种结构中“and”取代了更标准的“to”不定式（例如，“try and eat”代替“try to eat”）。虽然通常被认为是规范上不正确的用法，但这种用法在英国和美国英语中都很常见，其起源可以追溯到16世纪末。

本文强调“try and”的行为不像典型的并列连词。 证据包括：允许疑问词从第二个动词短语中移位（与真正的并列连词不同），无法重新排序动词，无法在“try and”之前使用“both”，以及“原形形式条件”，要求“try”和后面的动词都不能屈折变化（尽管此条件因方言而异）。此外，“try”不能被副词或否定词与“and”分开，并且不允许动词短语的省略。

本文提供了方言差异的证据：虽然原形形式条件通常得到维持，但一些方言允许两个动词的平行屈折形式，而另一些方言只允许“try”上的屈折变化。

最后，本文讨论了其他伪并列结构，如“be sure and”、“mind and”，以及“and”与运动动词（如“come and”和“go and”）的用法，并指出运动动词的伪并列在句法和语义上与“try and”不同。 例如，“go and”通常意味着它所描述的事件已经完成。

---

## 44. 1910年：现代世界精神失常之年

**原文标题**: 1910: The year the modern world lost its mind

**原文链接**: [https://www.derekthompson.org/p/1910-the-year-the-modern-world-lost](https://www.derekthompson.org/p/1910-the-year-the-modern-world-lost)

德里克·汤普森的文章《1910：现代世界失去理智之年》探讨了20世纪初和21世纪在技术变革、社会焦虑和人类境况方面的相似之处。他大量借鉴了菲利普·布洛姆的《眩晕年代》，重点关注1910年这个转折点。

文章强调，交通运输（汽车、飞机、自行车）的快速发展如何导致了普遍的焦虑和一种世界失控的感觉。这种“速度”被认为是不自然的，特别是对于那些通过骑自行车拥抱新自由的女性来说，引发了道德恐慌。这个时代还出现了“美国神经症”（神经衰弱）的激增，主要影响了被技术和加速的生活节奏压垮的白领工人。在此期间，精神病院的入院人数激增。

文章还深入探讨了这种社会动荡如何影响艺术。斯特拉文斯基（《春之祭》）、康定斯基（抽象艺术）和毕加索（原始主义）等艺术家通过从前现代风格和主题中汲取灵感来对抗现代性。他们试图在现代的新奇和异化中捕捉到关于人类的古老而真实的东西。抽象艺术的兴起恰逢摄影的普及，这降低了纯粹具象艺术的价值。

最后，汤普森谈到了1910年的知识氛围，重点介绍了马克斯·韦伯和西格蒙德·弗洛伊德的作品，他们的理论致力于应对在快速社会变革面前对人性的转变理解。

---

## 45. 菲茨杰拉德的闹剧

**原文标题**: Fitzgerald's Follies

**原文链接**: [https://libertiesjournal.com/articles/fitzgeralds-follies/](https://libertiesjournal.com/articles/fitzgeralds-follies/)

无法访问文章链接。

---

## 46. GPT-OSS对比Qwen3，以及GPT-2以来发展历程的详细回顾

**原文标题**: GPT-OSS vs. Qwen3 and a detailed look how things evolved since GPT-2

**原文链接**: [https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the)

Sebastian Raschka的这篇文章分析了OpenAI最新开源权重的大语言模型gpt-oss-20b和gpt-oss-120b，并将它们与GPT-2以及其他现代架构（如Qwen3）进行了比较。文章重点介绍了自GPT-2以来取得的架构进步，例如移除dropout，用RoPE替换绝对位置嵌入，从GELU切换到Swish/SwiGLU激活函数，以及整合混合专家（MoE）模块。

文章强调了为提高效率，从多头注意力（MHA）到分组查询注意力（GQA）的转变，以及gpt-oss中滑动窗口注意力的使用，在完整上下文和有限窗口注意力之间交替。文章指出，虽然这些模型与其他大语言模型使用相似的基础架构，但数据和算法调整至关重要。作者还讨论了模型宽度和深度之间的权衡，并简要提到了注意力偏差和汇聚点，以及与GPT-5的基准测试。gpt-oss中128个token的滑动窗口尺寸非常小，文章指出滑动窗口注意力已在GPT-3中使用。

---

## 47. Reddit 将屏蔽互联网档案馆。

**原文标题**: Reddit will block the Internet Archive

**原文链接**: [https://www.theverge.com/news/757538/reddit-internet-archive-wayback-machine-block-limit](https://www.theverge.com/news/757538/reddit-internet-archive-wayback-machine-block-limit)

由于担心人工智能公司违反Reddit平台政策，从互联网档案馆的网络时光机抓取数据，Reddit正在阻止该网络时光机访问其大部分内容。此举将阻止网络时光机索引帖子详情页、评论和用户资料，使其仅能存档Reddit.com主页。

Reddit发言人Tim Rathschmidt表示，该决定是为了保护Reddit用户及其数据，因为Reddit认为人工智能公司正在抓取网络时光机，以访问违反其政策的Reddit内容，包括已删除的内容。Reddit此前已向互联网档案馆表达了对抓取问题的担忧。

在此之前，Reddit最近一直在限制抓取工具，尤其是人工智能公司对其数据的访问。Reddit此前已与谷歌和OpenAI等公司达成协议，为其搜索和人工智能训练提供数据，并已开始向搜索引擎收取抓取其数据的费用。2023年备受争议的API更改也被Reddit辩解为是为了防止通过API滥用进行人工智能模型训练的措施。Reddit甚至起诉了Anthropic，指控其抓取内容。互联网档案馆尚未对置评请求作出回应。

---

## 48. 人工智能：美好期望

**原文标题**: AI: Great Expectations

**原文链接**: [https://rodneybrooks.com/ai-great-expectations/](https://rodneybrooks.com/ai-great-expectations/)

罗德尼·布鲁克斯重温了他1988年撰写的一篇关于人工智能炒作周期性的文章，将过去的期望与现在的现实进行了对比。1988年，他观察到，包括专家系统、机器人和神经网络在内的人工智能，总是面临着被夸大的期望，随后是更为温和的现实世界的成功。他强调，人工智能不是魔法，而是一系列工具和方法，用于解决以前传统编程无法解决的问题。

回首37年后，布鲁克斯指出，年轻时的自己对人工智能的乐观是有根据的，但也承认该领域持续存在的炒作和幻灭周期。他强调了他之前认为过于乐观的两个具体预测：埃德蒙·伯克利1949年关于机器成为速记员、翻译和精神科医生的愿景，以及伯纳德·威德罗1962年关于神经网络将允许用户用英语与计算机交谈并“为我们编写程序”的预测。虽然这些预测的某些方面在几十年后已经实现，但布鲁克斯坚持认为，当时这些预测被严重夸大了，需要比最初设想的更多的计算能力和研究。他总结说，人工智能的发展是一个逐步解锁复杂过程的过程，从而不断产生实际应用，这种观点无论当时还是现在都让他感到兴奋。

---

## 49. 以色列利维坦与埃及签署350亿美元天然气供应协议

**原文标题**: Israel's Leviathan signs $35B natural gas supply deal with Egypt

**原文链接**: [https://www.reuters.com/business/energy/israels-leviathan-signs-35-billion-natural-gas-supply-deal-with-egypt-2025-08-07/](https://www.reuters.com/business/energy/israels-leviathan-signs-35-billion-natural-gas-supply-deal-with-egypt-2025-08-07/)

无法访问文章链接。

---

## 50. 伪装成安全的反竞争行为是一种危险的模式

**原文标题**: Anti-competitive practices masquerading as security is a dangerous pattern

**原文链接**: [https://blog.alinelerner.com/i-posted-some-interview-prep-materials-on-linkedin-then-they-deleted-me/](https://blog.alinelerner.com/i-posted-some-interview-prep-materials-on-linkedin-then-they-deleted-me/)

采访.io创始人Aline Lerner详述了她在推广一个包含批评LinkedIn内容的资源中心后，突然被锁住LinkedIn账户的经历。她的个人资料消失，公司的关注者数量降至零，LinkedIn以潜在的安全问题为由，要求提供照片身份证进行验证。

Lerner怀疑这背后存在反竞争行为，伪装成安全措施。她指出，她能恢复访问权限依赖于投资人关系，暗示这是一个有缺陷的系统，普通用户可能在没有任何解释的情况下被永久封禁。她质疑，即使是违反服务条款而非安全漏洞，LinkedIn为何还要收集身份证件。

她认为，考虑到她在招聘社区的知名度和一贯的登录习惯，LinkedIn的身份管理似乎不够完善。Lerner将此与采访.io强大的身份验证形成对比，尽管采访.io是一个匿名平台。

Lerner批评了LinkedIn锁定、删除账户然后要求提供身份证件的做法，且没有明确的解释或恢复措施，除非用户有人脉关系。她强调这可能违反了类似于言论自由、正当程序和法律面前人人平等原则。她总结说，LinkedIn似乎在利用所谓的安全问题来压制竞争对手。

---

## 51. PHP编译时泛型：可行还是不可行？

**原文标题**: PHP compile time generics: yay or nay?

**原文链接**: [https://thephp.foundation/blog/2025/08/05/compile-generics/](https://thephp.foundation/blog/2025/08/05/compile-generics/)

PHP编译时泛型的可能性探讨

---

## 52. TCP客户端自连接 (2013)

**原文标题**: TCP Client Self-Connect (2013)

**原文链接**: [http://sgros.blogspot.com/2013/08/tcp-client-self-connect.html](http://sgros.blogspot.com/2013/08/tcp-client-self-connect.html)

Stjepan Groš 于 2013 年撰写的这篇博文探讨了一个 TCP 客户端连接到自身的现象，具体来说是使用 `telnet` 连接到 localhost 上没有服务器监听的端口。

作者演示了使用 `telnet` 重复尝试连接到某个端口（例如，50000）最初会导致“Connection refused”错误。但是，最终会建立连接，客户端连接到自身，这可以通过 `netstat` 和 `tcpdump` 看到。

这发生的原因是内核为每次连接尝试为 `telnet` 客户端分配一个随机的临时端口。如果偶然地，内核将目标端口（在本例中为 50000）分配为源端口，则客户端会尝试连接到自身。

从技术上讲，此行为符合 TCP 规范，允许“同时打开”。然后，作者深入研究内核的源代码，以解释 TCP 状态机如何处理这种自连接情况。具体来说，代码在 `TCP_SYN_SENT` 状态中识别出自连接的情况，将套接字移动到 `TCP_SYN_RECV`，发送 SYN+ACK，然后发送最终的 ACK 以建立连接并将套接字移动到 `ESTABLISHED` 状态。

该文章最后警告不要将临时端口用于监听服务器，因为可能会出现这种意外且难以调试的行为。作者强调，这种情况要求客户端和服务器（在这种情况下，实际上是同一个进程）使用相同的 IP 地址，并且连接尝试发生在初始握手期间。

---

## 53. 如何用统计学说谎

**原文标题**: How to Lie with Statistics

**原文链接**: [https://en.wikipedia.org/wiki/How_to_Lie_with_Statistics](https://en.wikipedia.org/wiki/How_to_Lie_with_Statistics)

如何用统计说谎

记者达莱尔·哈夫所著的《如何用统计说谎》出版于1954年，是一本广受欢迎且易于理解的统计学解读和潜在误用入门书籍。该书由欧文·盖斯配图，展示了统计错误和蓄意操纵如何导致错误的结论。

书中重点介绍了常见的陷阱，例如混淆相关性和因果关系、不当使用随机抽样以及图表的欺骗性使用。哈夫解释了折线图和条形图等视觉表现形式如何被扭曲以夸大差异或误导读者对比例关系的理解，如图形文字中可见。

本书面向大众，在20世纪60年代和70年代作为大学生的入门教材而广受欢迎。它以英文售出了超过150万册，并已被广泛翻译，巩固了其作为有史以来最畅销的统计学书籍之一的地位。本书旨在使读者掌握批判性思维技能，从而评估统计信息并识别潜在的操纵或虚假陈述。

---

## 54. 苏联业余摄影反思

**原文标题**: Reflections on Soviet Amateur Photography

**原文链接**: [https://www.publicbooks.org/strangers-in-the-family-album-reflections-on-soviet-amateur-photography/](https://www.publicbooks.org/strangers-in-the-family-album-reflections-on-soviet-amateur-photography/)

泽伊内普·德夫里姆·居尔塞尔评《不可见的在场：家庭照片中的苏联遗存》（作者：奥克萨娜·萨尔基索娃和奥尔加·舍甫琴科），强调该书通过业余摄影理解苏联身份认同形成的重要意义。居尔塞尔强调，该书表明，苏联家庭相册尽管内容看似平凡，但在构建和维系一个想象中的苏联共同体方面至关重要。

一个关键例子是红场上合影的普遍存在，陌生人一起合影，之后收到照片的复制品，这些照片嵌入到不同的家庭收藏中，并形成了共同的苏联体验。萨尔基索娃和舍甫琴科的研究基于对俄罗斯各地家庭照片收藏的访谈和分析，揭示了家庭摄影的一个独特方面：它包含了非亲属，反映了更广泛的社会结构。

居尔塞尔还赞扬了该书对审查和沉默的探索，揭示了家庭如何以可见和不可见的方式处理苏联的过去。该书还展示了国家如何利用摄影图像进行自我合法化。

评论最后强调了该书超越摄影研究的更广泛相关性。居尔塞尔认为，《不可见的在场》通过使用图像揭示更广泛的社会和政治模式，从而提供了一种新的学术视野，使其成为理解后苏联时代历史和记忆复杂性的宝贵资源。评论者强调了该书的创新设计，包括视频访谈的剧照和书签带，这鼓励读者深入研究这些材料。

---

## 55. 再见，GitHub

**原文标题**: Auf Wiedersehen, GitHub

**原文链接**: [https://github.blog/news-insights/company-news/goodbye-github/](https://github.blog/news-insights/company-news/goodbye-github/)

本文是对GitHub首席执行官Thomas Dohmke的传记介绍，重点介绍了他从小在德国对软件开发产生的浓厚兴趣，以及他专注于创建工具以改善开发者体验的职业生涯。文章强调了他目前在GitHub的角色，他在开发和发布广泛使用的AI开发者工具（如GitHub Copilot、Copilot Workspace和GitHub Models）方面发挥了重要作用。文章还提及了他作为TED演讲者的身份，以及他格拉斯哥大学机械工程博士学位。总体重点是展示Dohmke在软件开发领域的专业知识和贡献，尤其是在人工智能驱动工具领域。

---

## 56. 盲人模型如何看待地球？

**原文标题**: How Does a Blind Model See the Earth?

**原文链接**: [https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth](https://outsidetext.substack.com/p/how-does-a-blind-model-see-the-earth)

无法访问文章链接。

---

## 57. Show HN: Bolt – 一款用 C 编写的超快静态类型脚本语言

**原文标题**: Show HN: Bolt – A super-fast, statically-typed scripting language written in C

**原文链接**: [https://github.com/Beariish/bolt](https://github.com/Beariish/bolt)

Bolt：一款适用于实时和嵌入式应用的新型轻量快速静态类型脚本语言，由C语言编写。它强调性能、小尺寸、易于嵌入和类型安全。

主要特性包括：

*   **速度：** 声称性能优于同类语言，编译速度快（50万行代码/线程/秒）。
*   **紧凑：** 对构建尺寸影响极小。
*   **易于嵌入：** 简单的API，便于集成到现有应用程序中。
*   **类型系统：** 丰富的类型系统，用于早期错误检测，可通过原生代码扩展。
*   **嵌入优先设计：** 优先考虑跨语言性能。

它提供了一个标准库（带有可选模块，如文件I/O），默认使用malloc/realloc/free（可配置），并嵌入picomatch用于正则表达式解析。该项目包括示例代码、测试和基准测试。

Bolt目前支持x64架构，并可使用MSVC、GCC和Clang构建（GCC/Clang中存在一些警告）。欢迎贡献，但该项目具有主观性，需要仔细考虑功能添加。它采用MIT许可证。请注意，Bolt仍在开发中，可能存在编译器错误。

---

## 58. Digital Foundry离开IGN，现已独立 [视频]

**原文标题**: Digital Foundry leaves IGN, now independent [video]

**原文链接**: [https://www.youtube.com/watch?v=tl7bIJ2yu4I](https://www.youtube.com/watch?v=tl7bIJ2yu4I)

视频内容是关于Digital Foundry这个以深度技术分析视频游戏和硬件而闻名的团队离开IGN并成为独立实体。所提供的内容片段似乎是标准的YouTube页脚，包括版权、联系YouTube、创作者资源、广告、开发者信息、服务条款、隐私政策、安全指南、YouTube运作方式、测试新功能以及NFL Sunday Ticket信息等链接。此页脚未提供任何关于Digital Foundry *为何* 离开IGN或他们作为独立团队的计划的信息。

**简而言之，视频标题表明Digital Foundry已经离开IGN并且现在是独立的。所提供的内容只是标准的YouTube样板文件，没有提供有关分裂或Digital Foundry未来的更多信息。**

---

## 59. 在“冬季挑战赛”中创造最长滑雪跳跃

**原文标题**: Creating the Longest Possible Ski Jump in “The Games: Winter Challenge”

**原文链接**: [https://mrwint.github.io/winter/writeup/writeup2.html](https://mrwint.github.io/winter/writeup/writeup2.html)

本文详细介绍了作者在游戏《The Games: Winter Challenge》中探索最远跳台滑雪距离的过程。作者没有依赖传统的游戏玩法和工具辅助方法，而是选择了二进制分析方法，旨在了解游戏的内部机制和模拟逻辑。

文章概述了游戏中跳台滑雪的四个阶段（斜坡下降、跳跃、飞行和着陆），并指出由于潜在的隐藏机制和涌现行为，游戏中的建议（保持滑雪板平行）可能并不代表实际的最佳策略。

随后，重点转移到逆向工程游戏的重播文件格式。通过分析文件结构和修改数据，作者发现前14个字节是标头，后跟一个保存状态部分和一个输入序列部分。

保存状态包含玩家数据（服装颜色）、影响风力的 RNG 种子以及初始滑雪角度。输入序列由 4 字节块组成，可能编码了玩家的操作。然后，作者深入研究游戏的反汇编代码，以查明与保存状态相关的内存位置（玩家数据、RNG 种子、跳台滑雪状态数据）。这提供了重播文件数据和游戏内变量之间的直接映射。进一步的代码分析揭示了游戏如何读取和处理重播文件中的输入数据，为理解玩家操作如何被解释和模拟奠定了基础。

---

## 60. 反对聊天监控

**原文标题**: Fight Chat Control

**原文链接**: [https://fightchatcontrol.eu/](https://fightchatcontrol.eu/)

“反对聊天监控”运动反对欧盟提出的“聊天监控”立法，该立法将强制扫描所有欧盟公民的所有私人数字通信，包括加密消息和照片。该运动认为，这种大规模监控侵犯了欧盟宪章保障的基本隐私权，并破坏了数字安全。

主要担忧包括：未经怀疑自动扫描所有数字内容；削弱端到端加密，使所有人面临漏洞；可能出现误报，导致虚假指控；以及大规模监控在儿童保护方面的无效性。儿童保护专家警告说，这种监控会将资源从已证实有效的方法中转移，并削弱所有人的安全性，使儿童更不安全。

该运动还强调，欧盟政客根据“职业保密”规则将自己排除在该政策之外，要求隐私权方面的公平。他们认为，该提案为专制政府实施侵入式监控开创了危险的全球先例。

该运动敦促欧盟公民联系他们的欧洲议会议员，表达他们的反对意见，强调个人消息、照片和私人对话将在未经同意的情况下被扫描。他们为公民提供了定制信息并发送给其代表的工具，强调了隐私权、破坏加密、无效的儿童保护、破坏民主、技术问题和经济影响等问题。最终目标是阻止该立法并保护隐私和自由。

---

## 61. Show HN: Engineering.fyi – 一站式搜索技术工程博客

**原文标题**: Show HN: Engineering.fyi – Search across tech engineering blogs in one place

**原文链接**: [https://engineering.fyi/](https://engineering.fyi/)

Engineering.fyi 是一个技术工程博客搜索引擎。以下是所列文章的摘要：

**AI & LLMs：** 大部分文章关注AI，特别是 OpenAI 的 GPT 模型（GPT-5，gpt-oss）和 Google 的 Gemini 模型方面的进展。主题包括安全训练、模型能力（推理、图像转视频）、嵌入技术、对话式AI，以及在各个领域的用例（编码、医学、商业）。Google 的 Veo 3 及其与 Gemini API 的集成（允许视频生成）也得到了强调。此外，还讨论了使用 Gemini CLI 和 ADK 等工具开发和使用 AI 代理。重点是使用 AI 来增强现有工作流程、提高代码质量（Microsoft Copilot）和自动化任务。

**云 & 基础设施：** 几篇文章讨论了云基础设施主题，包括 Airbnb 上 Kubernetes 的 Istio 升级、Cloudflare 的 AI Workers 以及构建灵活的数据管道。还有关于 Kubernetes 上的分布式数据库（Airbnb）以及使用 Apigee 为 AI 代理提供 API 安全性的文章。

**性能 & 架构：** 文章涉及优化 React Native 中的性能（FlashList v2）、检测 Go 代码中的性能优化机会（Uber 的 PerfInsights）以及使用 AI 驱动的代码审查来提高代码质量（Microsoft）。Netflix 分享了他们直播流媒体架构的见解。

**开源 & 工具：** 该集合包括有关新的开源工具和库的公告和信息，例如 LangExtract（Google）、用于设计混凝土混合料的 AI 工具（Meta）以及斯坦福大学的 Marin 基础模型。

**其他主题：** 一些文章涉及更广泛的主题，例如 AI 行动计划（美国白宫、Palantir）、Google 开发者计划的演变以及构建人机界面。Stripe Tax 的文章详细介绍了一个更快的管辖权解决方案系统。

---

## 62. 活动

**原文标题**: Events

**原文链接**: [https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)

本文介绍了JavaScript中事件的概念，解释了它们如何使网页响应用户交互和浏览器中发生的其他事件。事件是浏览器在发生重要事情时发出的信号，例如按钮点击、按键或页面加载。要对事件做出反应，你需要将一个*事件监听器*附加到它上面。推荐的添加事件监听器的方法是使用`addEventListener()`方法，该方法接受事件类型（例如，“click”、“mouseover”）和一个回调函数（*事件处理程序*）作为参数。你还可以使用`removeEventListener()`来分离事件监听器。

本文还简要讨论了处理事件的替代方法，但这些方法不太受欢迎：事件处理程序属性（例如，`element.onclick`）和HTML中的内联事件处理程序（例如，`<button onclick="...">`），并建议避免使用后者，因为存在可维护性和安全问题。

*事件对象*被介绍为自动传递给事件处理程序的参数，提供了有关事件的额外信息。关键属性包括`target`，它指的是触发事件的元素。最后，本文介绍了如何使用`preventDefault()`阻止事件的默认行为，例如阻止表单在验证失败时提交。

---

## 63. ChatGPT Pro订阅费用相当于低收入国家38.6个月的收入。

**原文标题**: A ChatGPT Pro subscription costs 38.6 months of income in low-income countries

**原文链接**: [https://policykahani.substack.com/p/a-chatgpt-pro-subscription-costs](https://policykahani.substack.com/p/a-chatgpt-pro-subscription-costs)

文章《ChatGPT Pro订阅费用在低收入国家相当于38.6个月的收入》突显了在获取ChatGPT Pro等先进人工智能工具方面的巨大经济差距。文章认为，虽然每月20美元的订阅费在高收入国家可能看似合理，但对于低收入国家的人来说，这是一笔巨大的经济负担。

作者利用世界银行和OpenAI的数据，将ChatGPT Pro的费用与不同国家的平均收入进行了比较。他们发现，在低收入国家，该订阅费用可能高达数年的收入，使大多数人望而却步。

文章强调，这种差距进一步加剧了在获取技术和知识方面已存在的不平等。当富裕国家的人们可以轻松利用人工智能工具进行教育、职业发展和创新时，低收入国家的人们实际上被排除在外，阻碍了他们参与人工智能革命并从中受益的能力。

作者建议，需要解决这种支付能力差距，以确保公平地获取人工智能。可能的解决方案包括分级定价模式、为发展中国家的学生和研究人员提供补贴访问，以及开发开源替代方案。文章最终呼吁采取更具包容性的人工智能开发和部署方法，承认全球不同的经济现实。

---

## 64. 核潜艇上的等级制度：核手、新兵和角落 (2020)

**原文标题**: Nukes, Nubs And Coners: The Social Hierarchy Aboard A Nuclear Submarine (2020)

**原文链接**: [https://www.twz.com/34104/nukes-nubs-and-coners-the-unique-social-hierarchy-aboard-a-nuclear-submarine](https://www.twz.com/34104/nukes-nubs-and-coners-the-unique-social-hierarchy-aboard-a-nuclear-submarine)

亚伦·阿米克，一位退役海军声呐兵，详细描述了核潜艇上的社会等级，重点介绍了艇员的独特角色和刻板印象。这段旅程始于作为一名“无用之人”(NUB)，一个必须在12个月内通过严格的四阶段流程（包括系统知识、实地考察和口头考核）获得潜艇资格的新兵。成功完成将为他们赢得海豚徽章，并被潜艇社区接受。

艇员大致分为“核动力组”和“非核动力组”。在机舱工作的核动力组被描述为聪明但社交笨拙，进一步分为反应堆操作员、核电工和核机械师，每个人都有独特的怪癖和职责。他们维护核动力装置，确保潜艇的推进。

非核动力组居住在机舱前方的区域，代表着各种不同的背景。该组包括无线电员（信息守门员）、舵手（导航员）、声呐兵（具有古怪个性的声音分析师）、导弹技师（核弹头管理员）、辅机兵（大气和废物管理）、鱼雷兵（武器专家）、厨师（通过食物提高士气）、文书（文件专家）和医务兵（医生）。

阿米克强调，尽管他们各有特点，但艇员作为一个有凝聚力和战斗力的部队发挥作用。他最后强调了潜艇服役的回报性质，展示了多元化的群体如何在充满挑战的条件下取得非凡的成就。

---

## 65. 好奇 OpenAI 新 GPT-OSS 模型的训练数据吗？我也是。

**原文标题**: Curious about the training data of OpenAI's new GPT-OSS models? I was too

**原文链接**: [https://twitter.com/jxmnop/status/1953899426075816164](https://twitter.com/jxmnop/status/1953899426075816164)

关于OpenAI新型GPT-OSS模型训练数据的好奇？我也是。但由于JavaScript错误，文章无法访问。显示内容表明浏览器禁用了JavaScript，导致网页无法完整加载。因此，无法检索关于OpenAI的GPT-OSS模型训练数据的实际内容。可见信息包括标准的网站页脚元素，如帮助中心链接、服务条款、隐私政策、Cookie政策、版本说明、广告信息和版权声明。没有启用JavaScript，核心文章不可用，因此无法提供OpenAI新型GPT-OSS模型所用训练数据的摘要。

---

## 66. CT扫描仪揭示386处理器陶瓷封装内的惊喜

**原文标题**: A CT scanner reveals surprises inside the 386 processor's ceramic package

**原文链接**: [https://www.righto.com/2025/08/intel-386-package-ct-scan.html](https://www.righto.com/2025/08/intel-386-package-ct-scan.html)

This article delves into the intricate internal structure of the Intel 386 processor's ceramic package, revealing surprising complexity through a 3-D CT scan performed by Lumafield. While the exterior appears simple, the scan exposes six layers of internal wiring, effectively a 6-layer ceramic printed circuit board, facilitating the connection between the silicon die and the motherboard. The package features two tiers of gold contacts connected to the die via thin gold bond wires, some pads supporting up to five wires for increased current. This hierarchical interface expands the scale from the die's microscopic circuitry to the chip's pins by a factor of 2500.

The article highlights the custom design of the package, necessitated by the limitations of standard packages in providing sufficient power. It also reveals nearly invisible wires extending from the sides, used for electroplating the pins during manufacturing.

A key finding is the presence of two separate power and ground networks within the 386: one for I/O and one for the CPU logic. This separation prevents power spikes from the I/O circuits from interfering with the processor's core logic.

Furthermore, the article explores the function of the "No Connect" pins, suggesting they were used for testing purposes, with some pins almost fully connected. By tracing the connections, the author has labelled the function of each pin of the 386 die, making this information now available to the public for the first time. The article concludes by discussing Intel's historical challenges with packaging and the evolution from limited pin counts to complex Ball Grid Arrays, emphasizing the 386's package as a significant advancement.


---

## 67. 扩散语言模型是超级数据学习者

**原文标题**: Diffusion language models are super data learners

**原文链接**: [https://jinjieni.notion.site/Diffusion-Language-Models-are-Super-Data-Learners-239d8f03a866800ab196e49928c019ac](https://jinjieni.notion.site/Diffusion-Language-Models-are-Super-Data-Learners-239d8f03a866800ab196e49928c019ac)

生成摘要时出错

---

## 68. 我想要一切本地化——构建我的离线AI工作空间

**原文标题**: I want everything local – Building my offline AI workspace

**原文链接**: [https://instavm.io/blog/building-my-offline-ai-workspace](https://instavm.io/blog/building-my-offline-ai-workspace)

生成摘要时出错

---

## 69. Bouncing on trampolines to run eBPF programs

**原文标题**: Bouncing on trampolines to run eBPF programs

**原文链接**: [https://bootlin.com/blog/bouncing-on-trampolines-to-run-ebpf-programs/](https://bootlin.com/blog/bouncing-on-trampolines-to-run-ebpf-programs/)

This blog post explores the eBPF trampoline, a mechanism designed to optimize the performance of eBPF tracing programs in the Linux kernel. Tracing programs like `fentry` and `fexit` allow monitoring of kernel function execution, but traditional methods like kprobes, which use exceptions, can introduce significant overhead when frequently triggered.

The eBPF trampoline provides a faster alternative by directly "calling" eBPF programs, similar to how kernel functions call each other. However, since eBPF instructions are not native, the trampoline acts as an "ABI bridge" between the native architecture and the eBPF ISA, handling calling conventions and data input.

Instead of patching instructions to trigger exceptions, the trampoline dynamically generates architecture-specific code to prepare and execute eBPF programs. For `fentry` programs, the trampoline saves function arguments, calls the eBPF program, restores the arguments, and then returns to the original function.

The trampoline mechanism extends to more complex scenarios like capturing return values with `fexit`. In these cases, the trampoline can completely replace the original execution order, orchestrating the execution of both `fentry`, the target function, and `fexit`. The article provides examples related to ARM64 trampoline implementations. This allows for efficient and low-overhead monitoring of kernel function entry and exit points by minimizing context switches and exception handling.


---

## 70. Squashing my dumb bugs and why I log build IDs

**原文标题**: Squashing my dumb bugs and why I log build IDs

**原文链接**: [https://rachelbythebay.com/w/2025/08/03/scope/](https://rachelbythebay.com/w/2025/08/03/scope/)

Unable to access the article link.


---

## 71. Flintlock – Create and manage the lifecycle of MicroVMs, backed by containerd

**原文标题**: Flintlock – Create and manage the lifecycle of MicroVMs, backed by containerd

**原文链接**: [https://github.com/liquidmetal-dev/flintlock](https://github.com/liquidmetal-dev/flintlock)

生成摘要时出错

---

## 72. Trump's new executive order threatens US scientific freedom

**原文标题**: Trump's new executive order threatens US scientific freedom

**原文链接**: [https://www.dw.com/en/trumps-new-executive-order-threatens-us-scientific-freedom/a-73603440](https://www.dw.com/en/trumps-new-executive-order-threatens-us-scientific-freedom/a-73603440)

生成摘要时出错

---

## 73. How I code with AI on a budget/free

**原文标题**: How I code with AI on a budget/free

**原文链接**: [https://wuu73.org/blog/aiguide1.html](https://wuu73.org/blog/aiguide1.html)

生成摘要时出错

---

## 74. Dear String-to-Integer Parsers

**原文标题**: Dear String-to-Integer Parsers

**原文链接**: [https://owl.billpg.com/dear-string-to-integer-parsers/](https://owl.billpg.com/dear-string-to-integer-parsers/)

生成摘要时出错

---

## 75. How Potatoes Evolved

**原文标题**: How Potatoes Evolved

**原文链接**: [https://www.nhm.ac.uk/discover/news/2025/july/we-finally-solved-the-mystery-of-how-potatoes-evolved.html](https://www.nhm.ac.uk/discover/news/2025/july/we-finally-solved-the-mystery-of-how-potatoes-evolved.html)

生成摘要时出错

---

## 76. Melonking Website

**原文标题**: Melonking Website

**原文链接**: [https://melonking.net/](https://melonking.net/)

生成摘要时出错

---

## 77. Amiga Programming in 2025 with AmiBlitz

**原文标题**: Amiga Programming in 2025 with AmiBlitz

**原文链接**: [https://hackaday.com/2025/08/10/amiga-programming-in-2025-with-amiblitz/](https://hackaday.com/2025/08/10/amiga-programming-in-2025-with-amiblitz/)

生成摘要时出错

---

## 78. One-size-fits-all pancreatic cancer vaccine showed promise in early trial

**原文标题**: One-size-fits-all pancreatic cancer vaccine showed promise in early trial

**原文链接**: [https://www.nbcnews.com/health/cancer/pancreatic-cancer-vaccine-prevents-recurrence-phase-1-clinical-trial-rcna223980](https://www.nbcnews.com/health/cancer/pancreatic-cancer-vaccine-prevents-recurrence-phase-1-clinical-trial-rcna223980)

生成摘要时出错

---

## 79. Ch.at – A lightweight LLM chat service accessible through HTTP, SSH, DNS and API

**原文标题**: Ch.at – A lightweight LLM chat service accessible through HTTP, SSH, DNS and API

**原文链接**: [https://ch.at/](https://ch.at/)

生成摘要时出错

---

## 80. Booting 5000 Erlangs on Ampere One 192-core

**原文标题**: Booting 5000 Erlangs on Ampere One 192-core

**原文链接**: [https://underjord.io/booting-5000-erlangs-on-ampere-one.html](https://underjord.io/booting-5000-erlangs-on-ampere-one.html)

生成摘要时出错

---

## 81. ECScape: Understanding IAM Privilege Boundaries in Amazon ECS

**原文标题**: ECScape: Understanding IAM Privilege Boundaries in Amazon ECS

**原文链接**: [https://www.sweet.security/blog/ecscape-understanding-iam-privilege-boundaries-in-amazon-ecs](https://www.sweet.security/blog/ecscape-understanding-iam-privilege-boundaries-in-amazon-ecs)

生成摘要时出错

---

## 82. British backpacker pleads guilty to killing man while drunk on e-scooter

**原文标题**: British backpacker pleads guilty to killing man while drunk on e-scooter

**原文链接**: [https://www.bbc.com/news/articles/c0e999y7vq2o](https://www.bbc.com/news/articles/c0e999y7vq2o)

生成摘要时出错

---

## 83. Don't “let it crash”, let it heal

**原文标题**: Don't “let it crash”, let it heal

**原文链接**: [https://www.zachdaniel.dev/p/elixir-misconceptions-1](https://www.zachdaniel.dev/p/elixir-misconceptions-1)

生成摘要时出错

---

## 84. Writing simple tab-completions for Bash and Zsh

**原文标题**: Writing simple tab-completions for Bash and Zsh

**原文链接**: [https://mill-build.org/blog/14-bash-zsh-completion.html](https://mill-build.org/blog/14-bash-zsh-completion.html)

生成摘要时出错

---

## 85. Abogen – Generate audiobooks from EPUBs, PDFs and text

**原文标题**: Abogen – Generate audiobooks from EPUBs, PDFs and text

**原文链接**: [https://github.com/denizsafak/abogen](https://github.com/denizsafak/abogen)

生成摘要时出错

---

## 86. Flock Now Using AI to Report to Police If Our Movement Patterns Are "Suspicious"

**原文标题**: Flock Now Using AI to Report to Police If Our Movement Patterns Are "Suspicious"

**原文链接**: [https://www.aclu.org/news/national-security/surveillance-company-flock-now-using-ai-to-report-us-to-police-if-it-thinks-our-movement-patterns-are-suspicious](https://www.aclu.org/news/national-security/surveillance-company-flock-now-using-ai-to-report-us-to-police-if-it-thinks-our-movement-patterns-are-suspicious)

生成摘要时出错

---

## 87. v0.dev is now v0.app

**原文标题**: v0.dev is now v0.app

**原文链接**: [https://twitter.com/v0/status/1954942203471831448](https://twitter.com/v0/status/1954942203471831448)

生成摘要时出错

---

## 88. An engineer's perspective on hiring

**原文标题**: An engineer's perspective on hiring

**原文链接**: [https://jyn.dev/an-engineers-perspective-on-hiring](https://jyn.dev/an-engineers-perspective-on-hiring)

生成摘要时出错

---

## 89. Debian 13 “Trixie”

**原文标题**: Debian 13 “Trixie”

**原文链接**: [https://www.debian.org/News/2025/20250809](https://www.debian.org/News/2025/20250809)

生成摘要时出错

---

## 90. Conversations remotely detected from cell phone vibrations, researchers report

**原文标题**: Conversations remotely detected from cell phone vibrations, researchers report

**原文链接**: [https://www.psu.edu/news/engineering/story/conversations-remotely-detected-cell-phone-vibrations-researchers-report](https://www.psu.edu/news/engineering/story/conversations-remotely-detected-cell-phone-vibrations-researchers-report)

生成摘要时出错

---

## 91. How I use Tailscale

**原文标题**: How I use Tailscale

**原文链接**: [https://chameth.com/how-i-use-tailscale/](https://chameth.com/how-i-use-tailscale/)

生成摘要时出错

---

## 92. Cybertruck deactivated on road after a cease and desist for using it in a song

**原文标题**: Cybertruck deactivated on road after a cease and desist for using it in a song

**原文链接**: [https://old.reddit.com/r/CyberStuck/comments/1mmbq9w/lets_go_ahead_and_deactivate_here_looks_like_a/](https://old.reddit.com/r/CyberStuck/comments/1mmbq9w/lets_go_ahead_and_deactivate_here_looks_like_a/)

生成摘要时出错

---

## 93. Show HN: The current sky at your approximate location, as a CSS gradient

**原文标题**: Show HN: The current sky at your approximate location, as a CSS gradient

**原文链接**: [https://sky.dlazaro.ca](https://sky.dlazaro.ca)

生成摘要时出错

---

## 94. Claude Code IDE integration for Emacs

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

生成摘要时出错

---

## 95. Google TV operating system struggling to generate revenue

**原文标题**: Google TV operating system struggling to generate revenue

**原文链接**: [https://thestreamable.com/google-tv-operating-system-struggling](https://thestreamable.com/google-tv-operating-system-struggling)

生成摘要时出错

---

## 96. ESP32 Bus Pirate 0.5 – A hardware hacking tool that speaks every protocol

**原文标题**: ESP32 Bus Pirate 0.5 – A hardware hacking tool that speaks every protocol

**原文链接**: [https://github.com/geo-tp/ESP32-Bus-Pirate](https://github.com/geo-tp/ESP32-Bus-Pirate)

生成摘要时出错

---

## 97. POML: Prompt Orchestration Markup Language

**原文标题**: POML: Prompt Orchestration Markup Language

**原文链接**: [https://github.com/microsoft/poml](https://github.com/microsoft/poml)

生成摘要时出错

---

## 98. I Scraped 4M Jobs

**原文标题**: I Scraped 4M Jobs

**原文链接**: [https://old.reddit.com/r/resumes/comments/1mmy44q/i_scraped_4_million_jobs/](https://old.reddit.com/r/resumes/comments/1mmy44q/i_scraped_4_million_jobs/)

生成摘要时出错

---

## 99. People returned to live in Pompeii's ruins, archaeologists say

**原文标题**: People returned to live in Pompeii's ruins, archaeologists say

**原文链接**: [https://www.bbc.com/news/articles/c62wx23y2v1o](https://www.bbc.com/news/articles/c62wx23y2v1o)

生成摘要时出错

---

## 100. Car has more than 1.2M km on it – and it's still going strong

**原文标题**: Car has more than 1.2M km on it – and it's still going strong

**原文链接**: [https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168](https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168)

生成摘要时出错

---

