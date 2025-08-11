# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-11.md)

*最后自动更新时间: 2025-08-11 17:52:48*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 2 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 3 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 4 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 5 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 6 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 7 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 8 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 9 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 10 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 11 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 12 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 13 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 14 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 15 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 16 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 17 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 18 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 19 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 20 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 21 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 22 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 23 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 24 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 25 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 26 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 27 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 28 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 29 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 30 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 31 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 32 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 33 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 34 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 35 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 36 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 37 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 38 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 39 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 40 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 41 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 42 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 43 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 44 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 45 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 46 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 47 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 48 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 49 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 50 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 51 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 52 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 53 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 54 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 55 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 56 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 57 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 58 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 59 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 60 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 61 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 62 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 63 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 64 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 65 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 66 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 67 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 68 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 69 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 70 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 71 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 72 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 73 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 74 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 75 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 76 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 77 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 78 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 79 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 80 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 81 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 82 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 83 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 84 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 85 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 86 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 87 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 88 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 89 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 90 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 91 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 92 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 93 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 94 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 95 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 96 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 97 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 98 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 99 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 100 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 101 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 102 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 103 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 104 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 105 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 106 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 107 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 108 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 109 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 110 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 111 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 112 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 113 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 114 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 115 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 116 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 117 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 118 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 119 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 120 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 121 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 122 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 123 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 124 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 125 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 126 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 127 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 128 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 129 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 130 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 131 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 132 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 133 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 134 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 135 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 136 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 137 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 138 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 139 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 140 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 141 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 142 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 143 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 144 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 145 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
