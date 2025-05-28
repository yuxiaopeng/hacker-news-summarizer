# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-28.md)

*最后自动更新时间: 2025-05-28 17:50:31*
## 1. Show HN: 我用 Rust 重写了我的 Mac Electron 应用

**原文标题**: Show HN: I rewrote my Mac Electron app in Rust

**原文链接**: [https://desktopdocs.com/?v=2025](https://desktopdocs.com/?v=2025)

Desktop Docs：一款利用人工智能提供高级图像和视频搜索功能的Mac应用程序。它不仅分析文件名，还分析文件内容，允许用户使用自然语言描述或参考图像进行搜索。该应用专为视频编辑、摄影师和社交媒体经理等需要快速查找大型媒体库中特定文件的专业人士设计。

主要功能包括基于内容的匹配、图像相似度搜索、重复检测和跨格式支持。所有处理都在用户的Mac本地进行，确保隐私并无需上传到云端。该应用支持多种图像和视频格式，包括HEIC、JPG、PNG、GIF、BMP、WEBP、MP4、AVI、MOV、MKV和WEBM。

Desktop Docs需要配备Apple Silicon（M1、M2或M3）的Mac，一次性购买价格为99美元，无需订阅。它旨在帮助用户更快地查找文件，减少管理工作，并将数字混乱转化为有组织的知识库。用户评价强调了节省时间和改进文件组织。该应用程序可索引无限文件，允许在各种文档类型中进行智能搜索，并支持快速编辑。

---

## 2. 编译器探索器与永恒链接的承诺

**原文标题**: Compiler Explorer and the Promise of URLs That Last Forever

**原文链接**: [https://xania.org/202505/compiler-explorer-urls-forever](https://xania.org/202505/compiler-explorer-urls-forever)

本文详细介绍了保存Compiler Explorer链接的历史和即将面临的挑战。最初，该服务直接将编译器状态存储在URL中，但这变得笨拙。随后切换到谷歌的goo.gl链接缩短服务，但这在Stack Overflow禁止缩短链接时产生了问题。作为一种变通方法，实施了一个复杂的重定向系统，最终导致将状态存储在S3中，并由DynamoDB管理缩短的哈希URL。该系统包括对缩短链接中的亵渎行为进行幽默的检查，添加额外数据直到生成干净的哈希值。

现在核心问题是谷歌的goo.gl服务将于2025年8月关闭。尽管承诺永久性，但这些基于goo.gl的链接，包括godbolt.org/g/abc123形式的Compiler Explorer链接，将不再起作用。作者致力于“永久有效的URL”，一直在积极抓取互联网以抢救和编目这些链接，创建一个数据库以取代对goo.gl的依赖。

本文强调了依赖第三方服务作为关键基础设施的危险，并强调了拥有整个技术栈对于长期稳定性的重要性。作者鼓励用户重新访问旧的Compiler Explorer链接，以确保它们被添加到救援数据库中，从而将它们作为编程历史的宝贵组成部分保存下来。

---

## 3. Show HN: Tesseral – 开源认证

**原文标题**: Show HN: Tesseral – Open-Source Auth

**原文链接**: [https://github.com/tesseral-labs/tesseral](https://github.com/tesseral-labs/tesseral)

Tesseral：面向 B2B SaaS 应用的开源多租户身份验证基础设施。它是一个 API 优先的服务，提供一套全面的功能来管理用户身份验证、授权和访问控制，且不受特定语言或框架的限制。

主要功能包括：可定制的托管登录页面、B2B 多租户支持、用户模拟、客户自助配置、魔法链接、社交登录、SAML & SCIM 支持、RBAC、MFA、密码密钥/WebAuthn、验证器应用、API 密钥管理、用户邀请和 Webhooks。这些功能使开发人员能够轻松地将安全可靠的身份验证功能添加到他们的 B2B 应用程序中。

Tesseral 提供托管服务 (console.tesseral.com)，也可进行自托管。开发者可以通过阅读文档 (tesseral.com/docs) 并使用 React、Express、Flask 和 Golang 的 SDK 来开始使用。提供了一个使用 React 的前端集成示例，以及一个使用 Flask 的后端示例，演示了如何使用 Tesseral 对请求进行身份验证并提取用户详细信息。

该项目采用 MIT 许可证，欢迎贡献，但强调以谨慎的态度合并更改。安全漏洞应直接报告至 security@tesseral.com。Tesseral 鼓励通过 LinkedIn、X (Twitter)、新闻通讯、博客以及与创始人的直接联系来进行社区互动。Tesseral 由一家位于旧金山的初创公司管理，主要技术负责人为 Ulysse Carion、Blake Williams 和 Dillon Nys。

---

## 4. 戈壁石墙之谜

**原文标题**: The mysterious Gobi wall uncovered

**原文链接**: [https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html](https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html)

本文探讨了耶路撒冷希伯来大学考古学家及其合作者对戈壁长城的新研究。戈壁长城是蒙古国一处大型边境系统中的一段，长321公里。这项发表在《土地》（Land）杂志上的研究揭示了长城的起源、功能和历史背景。

该研究表明，长城主要由党项族在西夏王朝（公元1038-1227年）时期建造，挑战了长城仅作为防御结构的观点。研究人员认为，它具有多重功能，包括边界划分、资源管理和巩固皇权。证据还表明，从公元前2世纪到公元19世纪期间，该长城曾被周期性地使用，突显了其长期的战略意义。

长城的建造使用了当地材料，如夯土，并以石头和木材加固。其路线是根据水和木材等资源的可用性以及利用自然地理特征的堡垒和驻军的位置进行战略性选择的。

Shelach-Lavi教授强调，戈壁长城是管理移动、贸易和领土控制的“动态机制”。这些发现为了解中世纪帝国中环境适应与国家权力之间的关系提供了见解，并对理解古代基础设施具有重要意义。

---

## 5. 谁在乎的时代

**原文标题**: The Who Cares Era

**原文链接**: [https://dansinker.com/posts/2025-05-23-who-cares/](https://dansinker.com/posts/2025-05-23-who-cares/)

在“谁在乎的时代”中，Dan Sinker哀叹内容创作中日益增长的冷漠和质量下滑，这在很大程度上是由人工智能的兴起所推动的。他指出，一些例子如人工智能生成的新闻报纸增刊充斥着捏造的信息，却在无人注意或关心的情况下被发表，以及一个潜在的播客系列被简化成通用且可抛弃的东西。

Sinker认为，人工智能在某些情况下虽然有用，但经常被用来生产平庸的内容，因为对许多不在乎的人来说，“足够好”是可以接受的。他将这一趋势与更广泛的文化转变联系起来，即人们的注意力持续时间短，内容被设计成被动消费。

他进一步批评了政府和机构中普遍存在的漠不关心态度，并提到了特朗普政府和埃隆·马斯克的行为，这些行为将削减成本置于质量和专业知识之上。

尽管处境令人沮丧，Sinker还是发出了行动号召。他鼓励读者积极关心，创作真实且不完美的作品，支持那些正在创造真实事物的人，并全神贯注地参与内容。他强调了作为人类、保持不完美的重要性，并通过优先考虑真正的努力和参与来对抗平庸的浪潮。最终，在一个以冷漠为特征的时代，关心是最激进和最必要的行为。

---

## 6. 收到华夫饼屋的停止函

**原文标题**: Getting a Cease and Desist from Waffle House

**原文链接**: [https://www.jack.bio/blog/wafflehouse](https://www.jack.bio/blog/wafflehouse)

2024年9月末，当飓风威胁佛罗里达州时，作者对华夫饼屋的网站进行了逆向工程，创建了一个实时地图，追踪餐厅关闭情况，这是一个美国联邦紧急事务管理局（FEMA）用来衡量灾害严重程度的非官方“华夫饼屋指数”。 作者发现华夫饼屋使用了Next.js和React Server Components，找到了一个包含位置数据的JSON文件，然后使用Python对其进行抓取和处理，从而构建了该指数。

在发布网站（wafflehouseindex[.]org）并在推特上发布相关信息后，作者收到了华夫饼屋官方账号的关注，对方声明该信息不准确。 在政治评论员弗兰克·伦茨分享该网站后，人们的兴趣激增，但华夫饼屋迅速删除了他的推文并屏蔽了作者。

此后不久，作者收到了华夫饼屋发出的停止侵权通知，理由是未经授权使用其商标。 尽管作者做出了幽默的回应（“带着尊重和糖浆”），但还是照做了并关闭了网站。 虽然最初希望得到官方合作，但作者最终被无视了。

尽管寿命短暂，但作者珍视这次为乐趣而构建项目的经历，强调了数据操作创造有意义项目的力量。 作者还感谢华夫饼屋的良好体育精神，尽管存在商标侵权和数据抓取行为。

---

## 7. 喷灯理论：宇宙结构形成的新模型

**原文标题**: The Blowtorch Theory: A new model for structure formation in the universe

**原文链接**: [https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model](https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model)

朱利安·高夫的文章介绍了“喷灯理论”，作为宇宙结构形成的另一种模型，挑战了主流的Lambda冷暗物质（ΛCDM）模型。ΛCDM模型依赖于引力和理论上的“暗物质”来解释宇宙网的形成——一个由密集星系团通过丝状结构连接，周围环绕着巨大空洞的网络。然而，ΛCDM难以解释詹姆斯·韦伯太空望远镜观测到的成熟星系的快速出现。

喷灯理论提出，早期持续的超大质量黑洞喷流通过在早期宇宙中开辟空洞和铺设磁场，积极地塑造了宇宙。这些喷流创造了低压腔，随着时间的推移，这些低压腔膨胀，形成了我们今天观测到的宇宙空洞和丝状结构。

喷灯理论的一个主要优势是不需要暗物质；结构形成可以用喷流和普通物质来解释。该理论得到了近期早期超大质量黑洞、强大喷流以及这些黑洞周围快速星系形成的发现的支持。近期发现的来自早期宇宙的耀变体进一步加强了该理论的预测。

文章强调了20世纪70年代末对宇宙空洞的惊人发现，这些空间区域的密度极低，而最初的宇宙学模型未能预测到这些空洞。ΛCDM的开发是为了解释这些结构，但喷灯理论提供了一个更简单的解释。

---

## 8. 针对隐私币XMR去匿名化攻击的综合分析

**原文标题**: Comprehensive Analysis of De-Anonymization Attacks Against the Privacy Coin XMR

**原文链接**: [https://monero.forex/is-monero-totally-private-a-comprehensive-analysis-of-de-anonymization-attacks-against-the-privacy-coin/](https://monero.forex/is-monero-totally-private-a-comprehensive-analysis-of-de-anonymization-attacks-against-the-privacy-coin/)

本文全面分析了试图去匿名化门罗币（XMR）交易的尝试，门罗币是一种注重隐私的加密货币。文章强调，尽管门罗币旨在通过环签名、隐形地址和机密交易等功能实现不透明性，但各种实体一直在试图绕过其隐私保护。

文章考察了若干尝试，包括Chainalysis和CipherTrace开发的利用交易时间和网络分析的工具，这些工具取得了有限的、概率性的成功，尤其是在门罗币与隐私性较差的系统交互时。学术研究发现门罗币早期版本环签名实现中存在漏洞，这些漏洞随后得到了修复。一些公司还探索了通过交易所数据和IP地址进行链下数据关联，取得了一定的成功，但依赖于用户的操作安全。

美国国税局甚至悬赏破解门罗币的隐私，但没有公开证据表明有人成功。与此相反，门罗币社区积极致力于通过诸如“破解门罗币”系列等举措来加强隐私保护，这些举措旨在识别和缓解漏洞。

文章总结认为，尽管尝试众多，门罗币的隐私保护仍然具有韧性。虽然某些方法利用了弱点或以概率的方式降低了匿名性，但没有一种方法能够实现可靠、广泛的去匿名化。门罗币社区对其隐私功能的持续开发和加强确保了其作为注重隐私用户的首选地位。

---

## 9. Show HN: Loodio 2 – 简单可充电的浴室隐私设备

**原文标题**: Show HN: Loodio 2 – A Simple Rechargable Bathroom Privacy Device

**原文链接**: [https://loodio.com/](https://loodio.com/)

Loodio推出Loodio 2，一款简易可充电的浴室隐私设备。旨在帮助用户在私密时刻放松身心。该设备配有4GB存储卡，预装100首歌曲，并拥有长达一周的电池续航。售价149美元，包含免费国际运送。

---

## 10. 作为一名开发者，我最重要的工具是笔和笔记本。

**原文标题**: As a developer, my most important tools are a pen and a notebook

**原文链接**: [https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/](https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/)

文章《作为开发者，我最重要的工具是笔和笔记本》认为，尽管复杂的数字工具很普及，但简单的笔和笔记本对于开发者来说仍然至关重要。

作者认为，与直接在电脑上工作相比，使用纸笔可以进行更深入的思考和问题解决。他们发现，手绘图表、勾勒代码结构和做笔记有助于更好地理解复杂问题。这个过程可以进行更抽象的思考，并避免过早地陷入实现细节。

此外，作者强调了离线头脑风暴的好处。在没有通知和代码编辑器的干扰下，开发者可以完全专注于产生想法和探索不同的解决方案。他们认为这会带来更具创造性和经过深思熟虑的方法。

笔记本还可以作为想法、笔记和观察的重要存储库，可以轻松地重新访问和完善。与容易丢失或分散在不同应用程序中的数字笔记不同，物理笔记本为开发人员的思维过程提供了有形的、有组织的记录。

最后，文章强调笔和笔记本是思考的工具，而不仅仅是记录的工具。他们鼓励一种更深思熟虑的开发方法，从而产生更好的代码和更有效的问题解决。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 2 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 3 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 4 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 5 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 6 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 7 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 8 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 9 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 10 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 11 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 12 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 13 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 14 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 15 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 16 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 17 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 18 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 19 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 20 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 21 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 22 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 23 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 24 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 25 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 26 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 27 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 28 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 29 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 30 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 31 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 32 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 33 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 34 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 35 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 36 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 37 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 38 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 39 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 40 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 41 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 42 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 43 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 44 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 45 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 46 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 47 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 48 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 49 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 50 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 51 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 52 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 53 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 54 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 55 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 56 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 57 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 58 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 59 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 60 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 61 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 62 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 63 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 64 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 65 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 66 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 67 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 68 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 69 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 70 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
