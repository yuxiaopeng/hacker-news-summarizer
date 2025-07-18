# Hacker News 热门文章摘要 (2025-07-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. lsr：使用io_uring的ls

**原文标题**: lsr: ls with io_uring

**原文链接**: [https://tangled.sh/@rockorager.dev/lsr](https://tangled.sh/@rockorager.dev/lsr)

`lsr` 是一款新的 `ls` 工具，它利用 io_uring 通过批量处理系统调用来潜在地提升 Linux 系统上的性能。它用 Zig 编写，需要 Zig 0.14.0 才能安装。 安装需要使用带有期望优化级别和前缀的 `zig build` 命令。

`lsr` 提供了常见的 `ls` 功能，包括显示所有文件 (`-a`)、几乎所有文件 (`-A`)、控制输出格式（列、每行一个）、启用颜色、排序、显示图标以及显示扩展文件元数据 (`-l`) 等选项。

基准测试表明，`lsr` 可以胜过其他 `ls` 实现，包括 `ls`、`eza`、`lsd`、`uutils` 和 `busybox ls`，尤其是在处理大量文件时。这些基准测试比较了执行时间（使用 hyperfine）和系统调用次数（使用 strace）。结果表明，`lsr` 通常表现出更低的执行时间和显著更少的系统调用，尤其是在文件数量增加时，突出了 io_uring 带来的效率提升。然而，io_uring 的优势仅在 Linux 上可用。

---

## 2. DuckDuckGo 现在允许你隐藏搜索结果中的 AI 生成图像

**原文标题**: DuckDuckGo now lets you hide AI-generated images in search results

**原文链接**: [https://techcrunch.com/2025/07/18/duckduckgo-now-lets-you-hide-ai-generated-images-in-search-results/](https://techcrunch.com/2025/07/18/duckduckgo-now-lets-you-hide-ai-generated-images-in-search-results/)

DuckDuckGo推出新功能，过滤搜索结果中的AI生成图像。此功能旨在解决用户反馈AI图像妨碍搜索真实内容的问题。用户可以在图片标签页搜索后切换“AI图像”过滤器，选择“显示”或“隐藏”AI生成内容。该过滤器也可以在通用搜索设置中启用。

DuckDuckGo承认低质量AI生成媒体（“AI垃圾”）日益普遍，并采用手动管理的开源黑名单，如uBlockOrigin的“nuclear”列表和uBlacklist Huge AI Blocklist，来识别和过滤AI图像。虽然该过滤器并不完美，但它能显著减少显示的AI图像数量。

DuckDuckGo计划未来添加更多过滤器。文章指出，DuckDuckGo“小孔雀”的示例搜索参考了谷歌过去在搜索结果中优先显示AI生成图像而非真实图像的争议。

---

## 3. 尝试 Guix：一位 Nix 用户的印象

**原文标题**: Trying Guix: A Nixer's Impressions

**原文链接**: [https://tazj.in/blog/trying-guix](https://tazj.in/blog/trying-guix)

本文详细介绍了Nix用户首次尝试Guix的经历，重点关注在较不常见的CPU架构上复制标准桌面环境时遇到的实际挑战和差异。作者承认由于丰富的经验，对Nix有很强的偏见。

主要要点包括：

*   **政治考量：** Guix严格遵守自由软件，因此需要使用"nonguix"来启用常见的硬件，如无线互联网，这直接影响了技术设置。
*   **架构差异：** 与Nix将nixpkgs作为大型数据结构导入的更模块化的方法不同，Guix将CLI与包含来自频道的所有软件包和模块的系统配置文件紧密集成。这使得Guix中的版本切换速度较慢。
*   **文档与入门：** Guix的文档比Nix更出色，但需要熟悉Scheme。"nonguix"的情况由于缺乏资源而进一步使入门复杂化。
*   **性能：** Guix的评估速度明显慢于Nix，在作者的低性能笔记本电脑上尤其明显。
*   **Init系统：** Guix使用Shepherd（一个用Scheme编写的init系统）而不是systemd。
*   **Profile全局安装：** Guix似乎更喜欢软件包的profile全局安装，例如Emacs软件包，而不是Nix创建具有帮助程序的隔离环境的方法。

作者总结说，虽然Guix提出了挑战，但其连贯的生态系统和Lisp的使用令人着迷。他们计划继续尝试Guix，以实现与其现有NixOS设置的功能对等，并找到更快的迭代工作流程。

---

## 4. CP/M 创始人 Gary Kildall 回忆录免费下载发布

**原文标题**: CP/M creator Gary Kildall's memoirs released as free download

**原文链接**: [https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download](https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download)

文章宣布免费下载加里·基尔代尔的回忆录。基尔代尔是CP/M操作系统的创造者，文章将其视为创业文化的先驱。文章暗示他的故事突出了他对这种创业精神的贡献。文章还包含一张兰迪·克莱特（推测与基尔代尔有关）的照片，并注明照片来源为Tom Munnecke/Getty Images，显示的期刊来源为The Kildall Family/Computer History Museum。文章由前IEEE Spectrum编辑Tekla S. Perry撰写。

---

## 5. 揭露隐匿：互联网上 MCP 服务器的地图绘制

**原文标题**: Exposing the Unseen: Mapping MCP Servers Across the Internet

**原文链接**: [https://www.knostic.ai/blog/mapping-mcp-servers-study](https://www.knostic.ai/blog/mapping-mcp-servers-study)

诺斯替研究人员发现大量不安全的MCP（元控制协议）服务器暴露在互联网上。他们使用Shodan和自定义Python工具，识别出1862台服务器，并验证了其中119台允许未经身份验证访问内部工具列表。

该研究揭示了几个关键问题：

*   **缺乏安全性：** 所有测试的服务器都不安全，许多服务器表现出不稳定和漏洞，表明技术成熟度较低。 MCP规范本身通常缺乏默认的身份验证要求。
*   **能力暴露：** 这些服务器向任何发送符合协议的握手请求的人公开其内部工具和功能。
*   **早期采用阶段：** 暴露的服务器数量相对较少，表明该技术仍处于早期采用阶段。

研究人员使用Shodan采用了一种指纹识别方法，利用协议标记、传输信号、端点路径和技术指纹。他们根据服务器标语迭代地完善了搜索过滤器并识别了模式。验证过程包括发送只读的`tools/list`请求，以确认服务器功能，而不会触发任何操作。

研究结果突显了一个重要的安全问题，因为组织机构由于不安全的MCP部署而面临暴露敏感功能的风险。该研究表明，安全性可能只有在广泛的利用之后才能得到解决，这与其他新兴技术的发展模式相似。 该研究侧重于识别暴露的服务器，并遵守道德研究规范，避免采取任何可能更改数据或产生费用的行动。

---

## 6. Root权限遇上不可变性：OpenBSD Chflags对抗日志篡改

**原文标题**: When Root Meets Immutable: OpenBSD Chflags vs. Log Tampering

**原文链接**: [https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/](https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/)

本文详细介绍了如何在OpenBSD中实现不可篡改的日志记录，以满足ISO 27001合规性要求，该合规性要求保护日志信息免受篡改，即使是root用户也不例外。文章认为，虽然ISO 27001没有明确要求不可篡改的日志，但该标准对防篡改日志的要求实际上使其成为必要。

作者演示了如何使用OpenBSD的`chflags`命令，特别是`sappnd` (系统追加) 和 `schg` (系统不可变) 标志来保护日志。常规日志文件被设置为`sappnd`，允许它们增长但防止修改或删除。轮换后的日志被移动到一个存档目录并设置为`schg`，使其完全不可变。

挑战在于，即使是root用户也无法删除这些标志，除非系统以较低的安全级别运行。为了自动化日志轮换，文章提出了一个使用`/etc/rc.securelevel`的解决方案，该脚本在安全级别提高之前启动期间运行。此脚本删除标志，使用`newsyslog`轮换日志，将旧日志移动到`/var/log/archive`，然后重置标志，使存档的日志不可变。这种设置在OpenBSD中提供了一个root用户无法篡改的日志记录解决方案，满足了ISO 27001对日志完整性的隐含要求。

---

## 7. 全同态加密与隐私互联网的曙光

**原文标题**: Fully homomorphic encryption and the dawn of a private internet

**原文链接**: [https://bozmen.io/fhe](https://bozmen.io/fhe)

全同态加密 (FHE)：实现隐私保护的互联网

---

## 8. 百兔号 – 低技术航海环游世界

**原文标题**: Hundred Rabbits – Low-tech living while sailing the world

**原文链接**: [https://100r.co/site/home.html](https://100r.co/site/home.html)

百兔，一对过着低技术生活方式并航行世界的夫妇，分享他们2025年1月至6月的月度更新。更新内容涵盖他们的项目、船只维护、社区参与以及读书俱乐部选书。

**项目：** 他们一直忙于软件和创意项目，包括：
*   **Uxn 生态系统：** Uxntal 文档更新、将 Modal 移植到 Uxn、开发 “Turnip Complete”（Uxn 实现指南）以及改进 HTML5 Uxn 模拟器。
*   **游戏：** 在 Playdate 目录上发布 Oquonie，开发 Flickjam（基于 Flickgame 的游戏创作挑战赛），并将 Oquonie 的资源转换为 1-bit。
*   **网站：** 使用新页面和信息更新 100r.co，使用关于急救的新页面改进 Rabbit Waves，以及发布关于摩尔斯电码和信号旗的可打印杂志。
*   **其他工具：** 发布 Nebu（电子表格编辑器和桌面日历）、改进 M291 和 Turye。

**船只维护：** 他们完成了各种任务，包括将 Pino 拖出进行擦洗和重新喷漆、纠正螺旋桨摆动、与舵轮象限作斗争、重做 Teapot 的凝胶涂层、安装更换的太阳能电池板以及通风发霉的储物柜。

**社区：** 他们参与了 Goblin Week，在 Blakely Island 与 Merveillans 会面，为其他船员提供建议和借用工具，并对他们的社区表示感谢。

**读书俱乐部：** 他们列出了每个月阅读的书籍，包括《月光之下》、《阿忒弥斯》、《金翅雀》和《你想活出怎样的人生？》等书名。

---

## 9. HathiTrust数字图书馆 - 在线书籍

**原文标题**: HathiTrust Digital Library – books online

**原文链接**: [https://www.hathitrust.org/](https://www.hathitrust.org/)

无法访问文章链接。

---

## 10. 尊敬的用户，您已进入错误页面的错误页面。

**原文标题**: Dear valued user, You have reached the error page for the error page

**原文链接**: [https://imgur.com/a/2H7HVcU](https://imgur.com/a/2H7HVcU)

此Imgur错误页面表明用户的浏览器配置存在问题，特别是JavaScript被禁用。主要信息是请求用户启用JavaScript，以使Imgur网站能够正常运行。本质上，用户看到此页面是因为Imgur依赖JavaScript来提供其预期功能，如果没有它，网站就无法按预期运行。页面本身突出显示了核心信息：Imgur需要JavaScript。除此之外没有其他内容，暗示该网站的魔力（指其内容和功能）在未启用JavaScript的情况下无法访问。

---

## 11. 罗兰·加洛斯艺术

**原文标题**: The Art of Roland-Garros

**原文链接**: [https://www.garros.gallery/](https://www.garros.gallery/)

罗兰-加洛斯艺术展：回顾历年赛事经典海报。该网站作为一个粉丝画廊，展示与这项著名网球赛事相关的艺术作品，按时间顺序陈列自2025年至1980年的海报，并标注每张海报的创作者，提供“购买”选项。参展艺术家包括马克-安托万·马蒂厄（2025）、保罗·鲁斯托（2024）、路易丝·萨托（2022）、胡安·米罗（1991）、皮埃尔·阿列钦斯基（1988）等众多知名人士。展出的作品集突显了数十年来为赛事视觉形象带来的多样艺术风格和诠释。页面末尾声明所有海报的版权归各自艺术家和法国网球联合会所有，并且本网站是一个独立的粉丝画廊，未与任何一方正式关联。

---

## 12. 裸盖菇素减轻癌症患者的抑郁和焦虑（2016）

**原文标题**: Psilocybin decreases depression and anxiety in cancer patients (2016)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC5367557/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5367557/)

这项2016年发表在《精神药理学杂志》上的研究调查了赛洛西宾对51名患有威胁生命的诊断的癌症患者的抑郁和焦虑的影响。该研究采用随机、双盲、交叉设计，比较了极低剂量的赛洛西宾（1或3毫克/70公斤）和高剂量（22或30毫克/70公斤），以平衡的顺序给药，两次疗程间隔5周，并进行6个月的随访。

结果表明，高剂量的赛洛西宾显著且持续地降低了临床医生和自我评估的抑郁情绪和焦虑。参与者还体验到生活质量、生命意义、乐观情绪的提高以及死亡焦虑的降低。这些积极变化在6个月的随访中得以维持，约80%的参与者在抑郁和焦虑方面表现出临床意义上的显著降低。

参与者将他们对生活、情绪、人际关系和灵性的态度的改善归因于高剂量体验，超过80%的人报告幸福感和生活满意度中等或更高程度的提高。社区观察员也注意到相应的积极变化。研究发现，赛洛西宾疗程中神秘体验的强度介导了赛洛西宾剂量对治疗效果的影响。该研究突出了赛洛西宾作为癌症患者心理困扰治疗方法的潜力。

---

## 13. 美国移民及海关执法局正以前所未有的程度获取医疗补助数据

**原文标题**: ICE Is Getting Unprecedented Access to Medicaid Data

**原文链接**: [https://www.wired.com/story/ice-access-medicaid-data/](https://www.wired.com/story/ice-access-medicaid-data/)

一项新的信息交换协议允许美国移民和海关执法局（ICE）前所未有地获取近8000万医疗补助（Medicaid）领取者的个人数据。该协议授予ICE官员访问医疗保险和医疗补助服务中心（CMS）数据库（T-MSIS）的登录凭据，该数据库包含敏感的医疗信息，包括诊断、程序、地址，以及潜在的银行数据和社会安全号码（但后来明确仅包括性别、种族和族裔）。

声明的目的在于识别和定位“在美国的外国人”，而不是打击医疗补助基金的欺诈或滥用行为，这与美国卫生与公众服务部（HHS）和国土安全部（DHS）发言人声称的数据共享旨在防止非法移民获得合法公民应得的福利的说法相矛盾。包括前ICE局长约翰·桑德维格在内的批评人士警告说，这会产生寒蝉效应，由于担心移民执法，会阻止符合条件的人寻求医疗保健。

美国公民自由联盟（ACLU）认为，数据共享违反了《隐私法》，CMS在没有充分理由的情况下将数据交给了ICE。网络安全专家对潜在的违规行为表示担忧，如果ICE对数据的使用超出了CMS系统记录通知（SORN）中定义的范围。该协议允许ICE无限期地保留数据，并与未指定的接收者共享数据。

在此之前，各机构之间为移民执法目的而进行的数据共享日益增多，包括此前曝光的ICE访问追踪无人陪伴未成年人的ORR数据库。专家和倡导者强调，这将削弱对政府的信任，并迫使弱势群体在医疗保健和被驱逐出境的风险之间做出选择。

---

## 14. Jefit十五年发展历程

**原文标题**: 15 Years of Building Jefit

**原文链接**: [https://www.jefit.com/our-story](https://www.jefit.com/our-story)

盈的文章记录了Jefit这款健身计划与追踪App长达15年的发展历程。Jefit最初是为解决健身追踪痛点而生的个人项目，后来在用户反馈和对监督需求的驱动下，发展成为一个社交健身平台。最初在北卡罗来纳州依靠小额贷款进行自筹资金，Jefit专注于为有目的的训练提供更好的工具。

为了推动增长，盈冒险搬到硅谷，重建团队并应对远程工作等挑战。公司重视以训练、用户反馈和持续改进为中心的紧密团队文化。

尽管面临挫折，包括疫情封锁期间的用户流失和风险投资公司的拒绝，Jefit仍保持了同比增长。对质量的承诺和解决产品问题仍然是核心。

在成立15周年之际，Jefit推出了一个现代化的平台，具有全新的界面、更快的记录速度、改进的进度报告、新的目标设定工具和更智能的锻炼。底层的基础设施升级承诺提供更快的速度、更高的安全性以及人工智能驱动功能的基础。

盈对Jefit的1300万用户的忠诚和贡献表示感谢，并强调了对自律和长期努力的共同信念。文章最后发出了行动号召，邀请用户和支持者一起迎接挑战，共同开启Jefit的下一个篇章。

---

## 15. 行多态编程

**原文标题**: Row Polymorphic Programming

**原文链接**: [https://www.stranger.systems/posts/by-slug/row-polymorphic-programming.html](https://www.stranger.systems/posts/by-slug/row-polymorphic-programming.html)

本文介绍了行多态性，作为一种在Idris等静态类型语言中处理混乱、真实世界数据的技术。行多态性允许你编写泛型代码，基于特定字段的存在而非接口实现来操作记录（或“行类型”）。这在处理从模式派生的数据结构时尤其有用，例如数据库或电子表格中找到的那些。

本文将行类型与标准记录类型进行对比，突出了行类型可以通过模式（一种描述列及其类型的数据结构）定义的灵活性。本文展示了如何执行诸如按名称访问列以及通过连接模式构造新的行类型之类的操作。

一个关于房间家具摆放的实际例子说明了行多态性的优势。文章没有定义单独的具有`Area`接口的`Room`和`Furniture`数据类型，而是演示了编写一个单一的`area`函数，该函数适用于任何包含`length`和`width`字段（类型为`Double`）的行类型。代码示例使用列表来表示模式、行和表，说明了如何在Idris中实现行多态性。

文章最后讨论了行多态性的优缺点，并将其与意图证明进行了对比。它认为行多态性对于处理混乱数据（如前端工作或业务逻辑）的任务是有益的，而对于底层系统编程则不太有用。它还认为，行多态性可以为最初为动态类型语言编写的代码提供一种更灵活和自然的方式来输入类型。

---

## 16. H-1B项目从2011年至2022年增长了81%。

**原文标题**: H-1B program grew 81 percent from 2011 to 2022

**原文链接**: [https://twitter.com/USTechWorkers/status/1945999773825196492](https://twitter.com/USTechWorkers/status/1945999773825196492)

题为“H-1B项目从2011年到2022年增长了81%”的这篇文章似乎无法访问。提供的内容表明，需要JavaScript才能在x.com（原Twitter）上查看内容，而该文章似乎位于该网站上。因此，在无法访问原始来源的情况下，无法对文章的主要观点和关键信息进行适当的总结。可用的文本仅描述了网站的错误信息以及相关的法律和公司信息。

---

## 17. 纽约警察绕过面部识别禁令，锁定亲巴勒斯坦学生抗议者身份

**原文标题**: NYPD bypassed facial recognition ban to ID pro-Palestinian student protester

**原文链接**: [https://www.thecity.nyc/2025/07/18/nypd-fdny-clearview-ai-ban-columbia-palestinian-protest/](https://www.thecity.nyc/2025/07/18/nypd-fdny-clearview-ai-ban-columbia-palestinian-protest/)

纽约市消防局绕过纽约市警察局面部识别禁令，识别出哥伦比亚大学亲巴勒斯坦抗议者祖迪·艾哈迈德，他被指控向亲以色列抗议者扔石头。

一名消防队长利用纽约市消防局对Clearview AI和车辆管理局记录的访问权限（通常纽约市警察局无法获得），识别出艾哈迈德，后者随后被指控犯有仇恨罪，后降为轻罪。该案件最终被一名法官驳回，法官对政府监视超出法律界限表示担忧。

纽约市警察局受到其自身2020年政策和《POST法案》的限制，《POST法案》要求对监视技术保持透明，但纽约市消防局作为一个独立的机构，不受相同的限制。这引发了对潜在漏洞和规避隐私保护的担忧。

该事件激怒了隐私倡导者，他们认为纽约市警察局通过依赖其他机构，正在利用有问题的监视手段。市议员们现在正在考虑新的立法，以堵塞这些漏洞并将《POST法案》扩展到涵盖所有城市机构。文章还分享了这起事件给艾哈迈德带来的个人损失，突出了他的恐惧和孤立感。

---

## 18. 检查ANSI控制码和转义序列

**原文标题**: Inspect ANSI control codes and escape sequences

**原文链接**: [https://ansi.tools](https://ansi.tools)

该文档似乎是一份数据记录，可能是用于检查文本字符串中 ANSI 控制码和转义序列的工具或脚本的输出。其主要关注点在于分析和描述输入字符串中存在的 ANSI 转义序列。

提供的示例，如“ls/ezablockstest runhyperlinksoctal8-bitcommandsstylesmixedcolors”，是正在被分析的输入。随后的数据点描述了在这些输入中发现的特征。

分析的关键特征包括：

*   **length:** 输入字符串的长度（在提供的提取中为 0）。
*   **rows/columns:** 文本在终端或类似显示器中解释时的尺寸。
*   **invert, grid:** 布尔标志，可能指示 ANSI 序列是否涉及反转颜色或绘制网格。
*   **count:** 特定代码的出现次数。
*   **duplicates:** 是否存在重复的 ANSI 转义序列。
*   **sort, code, mnemonic, description, plain text, map position, newlines, greedy:** 这些字段表明一种结构化的分析，可能涉及排序、按 ANSI 代码分类、提供代码助记符和描述、提取纯文本、映射其位置以及分析它们如何处理换行符或贪婪地消耗字符。

本质上，这份数据捕获了解析和分析字符串中 ANSI 转义序列的结果，提供了关于序列类型、频率和其他特征的元数据。提供的示例突出了特定的 ANSI 相关功能，如超链接、八进制颜色代码、8 位命令、样式和混合颜色使用。

---

## 19. 两个星期探索后，我的Claude Code使用体验

**原文标题**: My experience with Claude Code after two weeks of adventures

**原文链接**: [https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/](https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/)

Sankalp 详细介绍了他在从 Cursor (另一款 AI 驱动的代码助手) 切换到 Claude Code (CC) 后，为期两周的使用体验。他最初广泛使用 Cursor，利用其 API 访问权限进行代码生成、理解代码库和提出问题。然而，速率限制促使他转向 Claude Code。

他发现通过每月 20 美元的 Sonnet 4 订阅访问的 CC，在 90% 的情况下都是有效的。 后来，他升级到每月 200 美元的 Claude Max 订阅，以获得无限的 Sonnet 4 和 Opus 4 访问权限。 他与 CC 的大部分工作都在 Python 和 Ruby + Typescript 代码库上进行，这些代码库带有规范和 e2e 测试，从而实现了调试的反馈循环。

他的工作流程从简单的打字演变为利用命令，尤其是在发现 Shift+Tab 可以在计划模式 (Opus) 和自动编辑模式 (Sonnet 4) 之间切换之后。 他强调了上下文管理的重要性，使用 `.claude` 文件夹中的文件来记录更改，并在压缩时重新启动聊天。 他还在使用该工具一周后发现了恢复功能。

Sankalp 观察到，在 CC 中 Sonnet 的表现比在 Cursor 中更好，这可能是由于后训练和更出色的“工具调用”选择，以及更有效的上下文管理。 CC 还利用“子代理”来更好地处理上下文。 虽然 Cursor 的搜索速度更快，但 CC 能够执行多线程任务。

他分享了一些技巧，例如使用 `!` 执行 bash 命令，发现文件 @提及，以及利用记忆功能进行自定义指令。 他发现 Sonnet 足以完成大多数任务，但在处理困难的 bug 时会切换到 Opus。 他还对自定义命令、自动化前端开发和探索多代理系统表达了兴趣。 最终，他认为 CC 是一款功能强大的工具，尽管与 Cursor 相比，学习曲线更为陡峭。

---

## 20. 所有人工智能模型可能都是一样的

**原文标题**: All AI models might be the same

**原文链接**: [https://blog.jxmo.io/p/there-is-only-one-model](https://blog.jxmo.io/p/there-is-only-one-model)

本文探讨“柏拉图表征假说”(PRH)，该假说认为随着人工智能模型变得更大更复杂，它们会趋于学习相似的、对世界的底层表征。作者通过将人工智能的压缩能力与其泛化能力进行类比来支持这一观点，暗示存在一种独特的、最佳的压缩和表示数据的方式。

作者从多个领域提出了支持PRH的证据，包括：

*   **语言建模：** 证明更好的语言模型能实现更好的压缩，暗示了一种对世界的共同理解。
*   **嵌入反演：** 讨论了从神经网络嵌入重建输入文本的挑战，并展示了一种名为“vec2vec”的方法，该方法可以在不同的嵌入空间之间进行映射，而无需直接对应。
*   **机制可解释性：** 强调了识别不同模型中非常相似的功能（“电路”）的研究，以及稀疏自编码器 (SAEs) 发现重叠特征的潜力。

文章认为PRH具有实际意义。它表明可以构建一个通用的嵌入反演器，该反演器可以在不同的模型之间进行转换，甚至可以潜在地解码古代文本或动物语言。作者最后强调了PRH的哲学和实践意义，并预计随着人工智能模型的不断发展，未来的研究将揭示它们之间更多的相似之处。

---

## 21. 香水测评

**原文标题**: Perfume reviews

**原文链接**: [https://gwern.net/blog/2025/perfume](https://gwern.net/blog/2025/perfume)

本文是作者对香水世界，特别是“前卫”香水探索的个人叙述。作者描述了他们尝试各种香水的经历，记录了他们喜欢和不喜欢的地方。最终，经过这段实验期，作者选定了两款他们购买的特定香水：Acqua di Sale和Kyoto Incense。本文主要概括了作者从尝试香水样品到对他们想要亲自拥有的香水做出明智选择的旅程。

---

## 22. SpaceX追逐火星登月目标之际，星际基地的受伤率超过竞争对手。

**原文标题**: Starbase injury rates outpace rivals as SpaceX chases its Mars moonshot

**原文链接**: [https://techcrunch.com/2025/07/18/starbase-injury-rates-outpace-rivals-as-spacex-chases-its-mars-moonshot/](https://techcrunch.com/2025/07/18/starbase-injury-rates-outpace-rivals-as-spacex-chases-its-mars-moonshot/)

TechCrunch文章调查显示SpaceX星舰基地事故率高企：德州星舰基地开发项目事故频发，2024年总记录事故率远高于航天器及航空航天制造业平均水平，且自2019年以来居高不下。SpaceX其他工厂事故率虽较低，但仍常超行业平均。过去四年14次OSHA检查中，6次涉及星舰基地事故，包括截肢和起重机倒塌等严重事故。NASA依赖星舰执行登月任务，合同包含应对重大安全事故条款。虽事故率高企，NASA称与SpaceX保持联系以确保安全。文章对比星舰基地与ULA和蓝色起源等火箭制造商的事故率，揭示星舰基地事故率更高，并提及安全界对总记录事故率作为安全绩效指标可靠性的争论。

---

## 23. 改造我的天文望远镜，提升我的天体摄影水平

**原文标题**: DIY Telescope Mods That Transformed My Astrophotography

**原文链接**: [https://www.youtube.com/watch?v=Efmzr_K4ApQ](https://www.youtube.com/watch?v=Efmzr_K4ApQ)

文章标题为“DIY望远镜改装提升我的天文摄影效果”，本应聚焦于通过自行改造望远镜来改善天文摄影效果。然而，提供的内容与标题和主题无关。实际上，它只是标准的YouTube页脚信息，包括版权、联系方式、创作者信息、隐私政策、条款以及其他平台相关数据。

因此，基于提供的内容，无法总结与天文摄影相关的改装。内容没有提供关于具体改装、它们的影响或实施原因的任何信息。本质上，标题承诺提供关于DIY望远镜升级以用于天文摄影的信息，但内容提供的却是来自YouTube的无关样板文字。

---

## 24. 基于eBPF的TCP over UDP 方案

**原文标题**: TCP-in-UDP Solution (eBPF)

**原文链接**: [https://blog.mptcp.dev/2025/07/14/TCP-in-UDP.html](https://blog.mptcp.dev/2025/07/14/TCP-in-UDP.html)

本文介绍了一种使用 eBPF 实现的新型 TCP-in-UDP 解决方案，旨在克服网络中间盒对 MPTCP 等 TCP 扩展的阻断或修改。该方案将 TCP 连接封装在 UDP 数据包中，无需增加每个数据包的额外数据或 VPN。

核心思想是重新排列 TCP 头部，使其类似于 UDP 头部，从而有效地将 TCP 数据包转换为 UDP 数据包，同时保留序列号和确认号等关键信息。由于紧急指针的使用频率较低且易受中间盒干扰，因此将其舍弃。

本文详细介绍了在高优化的 Linux 网络栈中遇到的挑战，包括访问所有必需的数据包数据 (SKB)、管理干扰每个数据包转换的 GRO/TSO/GSO 功能以及准确计算校验和。该解决方案禁用了硬件卸载加速和软件分段。本文还强调了在 TCP 和 UDP 之间切换时正确更新校验和的重要性，并使用 eBPF 助手和 TC ACT_CSUM 操作作为内核限制的解决方法。

最后，本文讨论了由于从 TCP 更改为 UDP 而导致的 MTU/MSS 设置管理需求，可能需要调整以避免 IP 分片。结论强调了 eBPF 程序在客户端和服务器端的易于部署性，提供了一种绕过网络限制的实用方法。

---

## 25. 与其用错误的依赖，不如自己造轮子（NIH)

**原文标题**: NIH is cheaper than the wrong dependency

**原文链接**: [https://lewiscampbell.tech/blog/250718.html](https://lewiscampbell.tech/blog/250718.html)

依赖的代价：为何“非我发明”原则有时是合理的

---

## 26. 展示HN：模拟联邦凭据管理集成

**原文标题**: Show HN: Mock FedCM Integrations

**原文链接**: [https://mockfedcm.com/](https://mockfedcm.com/)

MockFedCM：用于测试和调试FedCM集成的免费简易工具，提供模拟的依赖方(RP)和身份提供方(IdP)，允许开发者模拟认证流程并验证用户体验，无需真实的生产环境。这便于调试实现并在基于Chromium的浏览器中理解FedCM工作流程。请注意，该工具仅用于测试目的，不应在生产环境中使用。

---

## 27. 数字上涨法则：为何美国拒绝修复任何事物

**原文标题**: The Number go up rule: Why America refuses to fix anything

**原文链接**: [https://www.thebignewsletter.com/p/the-number-go-up-rule-why-america](https://www.thebignewsletter.com/p/the-number-go-up-rule-why-america)

无法访问文章链接。

---

## 28. 将 XOR 技巧扩展到数十亿行

**原文标题**: Extending That XOR Trick to Billions of Rows

**原文链接**: [https://nochlin.com/blog/extending-that-xor-trick](https://nochlin.com/blog/extending-that-xor-trick)

本文解释了如何将异或技巧（XOR trick）推广到使用可逆布隆过滤器（IBFs）处理大型数据集中数千个缺失ID的情况。异或技巧常用于查找列表中的缺失数字。作者从异或技巧的概念出发，引入分区和哈希函数来处理多个缺失数字。

文章强调了简单分区的局限性，并介绍了对称差的概念，利用哈希累加器来检测不可靠的异或结果。这引出了IBFs的核心思想：一种用于集合协调的强大数据结构。

IBFs由包含`idSum`、`hashSum`和`count`累加器的单元格组成。它们支持`Encode`、`Subtract`和`Decode`操作。`Subtract`操作会消除相同的值，从而专注于对称差。`Decode`操作通过识别“纯”单元格来迭代恢复值。IBF的大小由对称差的预期大小决定。

文章提供了一个IBF的Python实现。最后，文章将IBFs定位在更广泛的“集合协调”范畴内，并提到了错误纠正码等替代方法。作者提供了参考文献和“延伸阅读”部分，其中包含指向有关IBLT、多方集合协调、简单集合草图和实用无率集合协调的高级论文的链接。

---

## 29. 我最喜欢的AI应用是编写日志。

**原文标题**: My favorite use-case for AI is writing logs

**原文链接**: [https://newsletter.vickiboykis.com/archive/my-favorite-use-case-for-ai-is-writing-logs/](https://newsletter.vickiboykis.com/archive/my-favorite-use-case-for-ai-is-writing-logs/)

本文重点介绍了作者对JetBrains PyCharm和GoLand中全行代码补全(FLCC)功能的赞赏，特别是其在生成有效的调试和生产日志方面的效用。作者强调了手动编写日志的认知负担，尤其是在处理复杂数据结构时。FLCC能够基于周围的代码智能地推断日志补全，从而提高清晰度和简洁性。

文章详细介绍了FLCC的技术实现，重点介绍了设备端模型所需的约束和优化。关键方面包括：

*   **模型训练：** 使用GPT-2风格的Transformer模型（后来切换到Llama2）在“The Stack”代码数据集的子集上进行训练，并进行预处理步骤以删除注释和处理缩进。
*   **量化和优化：** 该模型被量化为INT8，并作为ONNX RT工件提供服务，从而实现CPU推理并减少内存占用。
*   **推理：** 使用束搜索来生成代码补全，并采用缓存策略来提高性能。

作者强调，与通用LLM相比，FLCC专注于特定任务（代码补全）使其能够使用更小、更高效的模型。文章最后强调了大型和小型AI模型的价值，并强调了像FLCC这样的专业AI解决方案在提高开发者生产力方面的潜力。作者还指出用户体验的周到性，因为生成的日志通常足够简洁和有用，可以保留在生产代码中。

---

## 30. Windows 10 的终结：社区维修小组工具包

**原文标题**: The End of Windows 10: a toolkit for community repair groups

**原文链接**: [https://therestartproject.org/end-of-windows-10-toolkit-for-repair-groups/](https://therestartproject.org/end-of-windows-10-toolkit-for-repair-groups/)

无法访问文章链接。

---

## 31. 因“低使用率”而移除 GH Killing 命令面板

**原文标题**: GH Killing Command Palette for "low usage"

**原文链接**: [https://github.com/orgs/community/discussions/166528](https://github.com/orgs/community/discussions/166528)

这份2025年7月17日发布的GitHub社区帖子强烈反对GitHub移除命令面板功能的计划，原因是他们认为使用率低。用户认为命令面板是键盘驱动导航的宝贵工具，可以提高生产力和可访问性，尤其对于有运动障碍的用户而言。

核心抱怨围绕着GitHub对该功能的处理方式。该功能被隐藏在“功能预览”标志后，没有宣传，导致知晓率低，进而导致采用率低。此外，该功能还会自动禁用一些之前启用它的用户，进一步阻碍了其推广。用户认为，导致使用率低的原因是这些因素，而非功能本身缺乏价值。

评论者强调了命令面板在快速切换仓库和页面方面的效率，这种功能很难通过其他方式复制。他们提到了Slack和Atlassian等其他流行平台中的类似功能，强调了命令面板作为标准功能的实用性。一些用户表示，他们最近才发现该功能，现在非常依赖它。

帖子中提出了浏览器书签、Raycast和用户脚本等替代方案，但这些方案不如命令面板全面。许多用户敦促GitHub重新考虑移除计划，推广该功能，并在将其停用之前，给它一个机会获得更广泛的采用。他们认为，该功能目前的状态并不能反映它对GitHub社区的潜在价值。

---

## 32. ChatGPT智能体：连接研究与实践

**原文标题**: ChatGPT agent: bridging research and action

**原文链接**: [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)

无法访问文章链接。

---

## 33. 修复孤岛惊魂(2018)中的Direct3D9漏洞

**原文标题**: Fixing a Direct3D9 bug in Far Cry (2018)

**原文链接**: [https://houssemnasri.github.io/2018/07/07/farcry-d3d9-bug/](https://houssemnasri.github.io/2018/07/07/farcry-d3d9-bug/)

本文详述了2004年游戏《孤岛惊魂》中一个长期存在的bug的发现与修复，具体而言，是在Windows XP之后的新系统上水面反射失效的问题。该bug表现为陆地无法在水中反射，与原始体验相比，视觉质量显著下降。

作者在注意到这个问题后，使用PIX图形调试器分析了在正常运行（XP）和损坏（Windows 10）系统上的渲染过程。调查显示，Direct3D9对剪裁平面（用于自定义视锥体的功能）的处理是根本原因。由于其罕见的使用，此功能现在在现代硬件上被模拟。

调试过程表明，即使使用相同的PIX捕获，Windows XP和Windows 10之间用于水面反射的纹理渲染方式也不同。作者发现游戏使用剪裁平面来防止水下模型出现在水面反射中。完全禁用剪裁平面修复了陆地反射，但也引入了水下伪影。

作者推测，D3D9实现中的回归源于Windows Vista显示驱动程序模型（WDDM）。 修复方案包括在每次绘制调用之前保存并重新应用所请求的剪裁平面。 这个看似简单的解决方案彻底解决了水面反射失效的问题，且没有性能损失。

作者承认剪裁平面失效的确切原因仍然未知，但所实施的解决方法是有效且高效的。 修复程序的源代码已在GitHub上发布，允许其他人将其用作参考。

---

## 34. 对IBM昙花一现的1995年“蝴蝶”ThinkPad 701的回顾

**原文标题**: A look at IBM's short-lived "butterfly" ThinkPad 701 of 1995

**原文链接**: [https://www.fastcompany.com/91356463/ibm-thinkpad-701-butterfly-keyboard](https://www.fastcompany.com/91356463/ibm-thinkpad-701-butterfly-keyboard)

《快公司》文章“回顾IBM昙花一现的1995年‘蝴蝶’ThinkPad 701”重点介绍了IBM ThinkPad 701标志性和创新性的设计，尤其是其独特的“蝴蝶”键盘。 ThinkPad 701于1995年推出，具有开创性意义，因为它成功地将全尺寸键盘装入了一个非常紧凑的笔记本电脑机箱中。

这篇文章强调了该设计背后的工程独创性：键盘被分成两个相互锁定的部分，它们会在笔记本电脑打开和关闭时自动伸展和收缩。这使得在较小的占地面积内也能获得舒适的打字体验。

虽然ThinkPad 701因其创新而备受赞誉，但其生命周期相对较短，部分原因是其复杂性以及其他以不那么复杂的机制实现类似设计目标的方法的出现。尽管其市场存在时间很短，但文章认为，ThinkPad 701凭借其大胆而令人难忘的设计，在科技爱好者和收藏家中获得了传奇般的地位。它代表了笔记本电脑发展初期的一个实验和创造性解决问题的时期，并展示了IBM致力于突破可能性的界限。文章最后总结道，ThinkPad 701仍然证明了创新设计的力量及其对便携式计算发展的持久影响。

---

## 35. Mistral 在 Le Chat 发布深度研究、语音和项目

**原文标题**: Mistral Releases Deep Research, Voice, Projects in Le Chat

**原文链接**: [https://mistral.ai/news/le-chat-dives-deep](https://mistral.ai/news/le-chat-dives-deep)

Mistral AI发布Le Chat AI助手重大更新，使其更强大且用途更广。主要新增功能包括：

*   **深度研究（预览版）：** 此模式将Le Chat转变为结构化的研究助手，使其能够分析复杂主题、收集可靠来源并生成带有参考文献的报告。
*   **语音模式：** 由新的Voxtral模型驱动，允许用户使用语音命令与Le Chat交互，实现免提使用。
*   **原生多语言推理：** 利用Magistral推理模型，Le Chat现在可以提供深思熟虑的答案，并且可以在句子中间切换语言。
*   **项目：** 此功能将对话组织到上下文丰富的文件夹中，使用户能够对相关聊天进行分组、上传文件并在每个项目中维护特定的工具设置。
*   **高级图像编辑：** 与Black Forest Labs合作，Le Chat现在提供直接图像编辑功能，例如“移除物体”，并在编辑过程中保留角色和细节。

这些功能旨在增强研究能力，通过语音改善自然交互，支持多语言推理，提供组织工具，并扩展创造性可能性。用户可以在Le Chat Web平台和移动应用程序上访问这些新功能。 Mistral AI还为组织解决方案提供Le Chat Enterprise，并提供开放职位。

---

## 36. RisingWave：一个开源的流处理和管理平台

**原文标题**: RisingWave: An Open‑Source Stream‑Processing and Management Platform

**原文链接**: [https://github.com/risingwavelabs/risingwave](https://github.com/risingwavelabs/risingwave)

RisingWave 是一个开源的流处理和管理平台，专为实时数据分析而设计，提供经济高效且用户友好的体验。它利用兼容 Postgres 的 SQL 接口和 DataFrame 风格的 Python 接口，允许用户每秒摄取数百万个事件，执行实时连接和分析，并将最新结果交付到 Apache Iceberg 或其他系统。

RisingWave 集成了流处理、存储和开放格式持久化，支持摄取、实时处理和交付。它的主要优势包括：PostgreSQL 兼容性以实现无缝集成，S3 作为主要存储以实现高性能和动态扩展，弹性磁盘缓存以降低延迟和成本，以及原生 Apache Iceberg 支持以实现高效的数据湖集成。

该平台擅长流式分析、事件驱动应用、实时数据丰富和特征工程等用例。它提供通过 RisingWave Cloud、Docker 和 Kubernetes 进行部署的选项。

RisingWave 优先考虑易用性和成本效益，通过消除手动状态调优和优化复杂查询来实现。该项目欢迎社区贡献，并根据 Apache License 2.0 获得许可。匿名收集使用情况统计信息以改进产品，并提供退出选项。

---

## 37. LibreOffice抨击微软利用复杂文件格式锁定Office用户

**原文标题**: LibreOffice slams Microsoft for locking in Office users w/ complex file formats

**原文链接**: [https://www.neowin.net/news/libreoffice-calls-out-microsoft-for-using-complex-file-formats-to-lock-in-office-users/](https://www.neowin.net/news/libreoffice-calls-out-microsoft-for-using-complex-file-formats-to-lock-in-office-users/)

LibreOffice指责微软故意在其Microsoft 365 (Office)套件中使用不必要地复杂的文件格式，以将用户锁定在其生态系统中。 争论的核心在于XML的使用，这是一种旨在促进互操作性的标记语言。 虽然LibreOffice（使用ODF - .odt, .ods）和Microsoft（使用OOXML - .docx, .xlsx）都在各自的文件格式中使用XML，但LibreOffice声称微软的实现过于复杂。

LibreOffice认为，微软的XML模式非常复杂，具有深度嵌套的结构、不直观的命名约定和大量的可选元素，这构成了其他开发者进入的障碍。 这种复杂性使得竞争的办公套件难以完全准确地解释和使用Microsoft Office文件。

LibreOffice将此比作一个拥有公共轨道的铁路系统，但其控制系统过于复杂，只有一家公司的火车才能在其上运行。 他们断言，即使是简单的句子也变成了嵌套标签的迷宫，使得微软以外的任何人都难以解析。

此外，LibreOffice将这种文件格式锁定与微软推动Windows 11联系起来，暗示这种升级并非出于真正的技术必要性，而是为了进一步将用户嵌入微软生态系统中。 因此，LibreOffice正积极鼓励用户迁移到Linux和LibreOffice作为替代方案。

---

## 38. Servo Web引擎性能进一步调优

**原文标题**: Servo Web Engine Further Tuning Performance

**原文链接**: [https://www.phoronix.com/news/Servo-June-2025-Highlights](https://www.phoronix.com/news/Servo-June-2025-Highlights)

Servo网页排版引擎开源项目在开发上取得了显著进展，最新的月度状态更新中对此进行了概述。主要进展包括性能优化以及增量布局处理方面的进一步工作。该引擎越来越适合嵌入到其他软件中，Servoshell演示项目的持续工作证明了这一点。

更新中强调的特定功能和改进包括：支持视口meta标签和DOM中的滚动事件、基本的IndexedDB支持，以及通过`AbortController`改进中止处理。

值得注意的是，实验性的多进程模式现在可以在Microsoft Windows上运行。DevTools的功能随着新增功能变得更加强大。此外，Servo现在在其基本的Servoshell浏览器UI中支持屏幕阅读器功能，从而增强了可访问性。WebDriver服务器支持也在不断进展，旨在实现Servo的自动化。更多详细信息可在Servo.org博客上找到。

---

## 39. 法国村庄饮用水告罄：全氟辛烷磺酸污染是主因

**原文标题**: French villages have no more drinking water. The reason? PFAS pollution

**原文链接**: [https://www.lemonde.fr/en/environment/article/2025/07/18/these-french-villages-have-no-more-drinking-water-the-reason-pfas-pollution_6743479_114.html](https://www.lemonde.fr/en/environment/article/2025/07/18/these-french-villages-have-no-more-drinking-water-the-reason-pfas-pollution_6743479_114.html)

创纪录PFAS污染致法国东部16村庄近3500居民饮水告急

---

## 40. Gmail 服务中断

**原文标题**: Gmail Outage

**原文链接**: [https://downdetector.com/status/gmail/](https://downdetector.com/status/gmail/)

无法访问文章链接。

---

## 41. 无需担心配置，即可运行 TypeScript 代码

**原文标题**: Run TypeScript code without worrying about configuration

**原文链接**: [https://tsx.is/](https://tsx.is/)

本文介绍了 `tsx` (TypeScript Execute)，一个旨在简化 TypeScript 代码运行的 Node.js 增强工具。它可以直接替代 `node`，无需复杂的配置即可直接理解和执行 TypeScript 文件。

`tsx` 的主要特点包括：

*   **无缝 TypeScript 执行：** `tsx` 提供了合理的 TypeScript 运行默认配置，让初学者也能轻松上手。
*   **CJS/ESM 互操作性：** 它无缝处理 CommonJS 和 ES Modules，解决了常见的 `ERR_REQUIRE_ESM` 错误。
*   **监听模式：** 内置的监听模式可以在文件保存时自动重新运行脚本，从而提高开发人员的效率。

本文解释说，`tsx` 的创建是为了解决 Node.js 生态系统因引入 ES Modules 而产生的碎片化问题，特别是考虑到像 `ts-node` 这样的工具中存在的复杂性和缺乏 ESM 支持的情况。 `tsx` 支持 `tsconfig.json` 路径，旨在通过处理 CommonJS 和 ESM 模块而无需手动配置来简化开发人员的体验。

最后，本文提到该项目依赖于用户的捐赠，并鼓励使用 `tsx` 的公司成为赞助商，以确保其持续的维护和开发。

---

## 42. 乌克兰黑客大规模网络攻击，抹去俄气公司数据库

**原文标题**: Ukrainian hackers wipe databases at Russia's Gazprom in major cyberattack

**原文链接**: [https://kyivindependent.com/ukrainian-intel-hackers-hit-gazproms-network-infrastructure-sources-say-07-2025/](https://kyivindependent.com/ukrainian-intel-hackers-hit-gazproms-network-infrastructure-sources-say-07-2025/)

据《基辅独立报》报道，乌克兰军事情报局（HUR）消息人士透露，HUR于2025年7月17日对俄罗斯能源巨头俄罗斯天然气工业股份公司（Gazprom）发动了一场大规模网络攻击。 据称，此次攻击针对的是俄罗斯天然气工业股份公司的网络基础设施，乌克兰方面声称该基础设施为俄罗斯的战争行动提供支持。

该HUR消息人士称，此次攻击摧毁了大量数据，安装了具有破坏性的定制软件，并禁用了近2万名系统管理员的访问权限。 据报道，关键数据库的备份副本也被擦除。 大约390家俄罗斯天然气工业股份公司的子公司和分支机构受到影响，包括Gazprom Teplo Energo、Gazprom Obl Energo和Gazprom Energozbyt。

据报道，攻击者摧毁了运行1C软件（用于文档管理和分析）的强大服务器集群，禁用了操作系统，并损坏了大量设备的BIOS，需要进行物理维修。

俄罗斯天然气工业股份公司和俄罗斯当局尚未公开评论这起所谓的事件。《基辅独立报》无法独立证实这些说法。

---

## 43. 最强服务器因Power11变得更强大

**原文标题**: The Most Powerful Server Embiggens a Bit with Power11

**原文链接**: [https://www.nextplatform.com/2025/07/16/the-worlds-most-powerful-server-embiggens-a-bit-with-power11/](https://www.nextplatform.com/2025/07/16/the-worlds-most-powerful-server-embiggens-a-bit-with-power11/)

本文剖析IBM新Power11处理器及其对Power Systems服务器产品线，特别是高端Power E1180的影响。Power11本质上是精进版的Power10，它诞生于制造挑战和延误，迫使IBM调整其路线图。最初的Power10计划因GlobalFoundries放弃工艺而受挫，导致IBM转向三星。

Power11与Power10一样，拥有180亿个晶体管和16个核心，但激活了所有16个核心（Power10通常会因良率问题而禁用一个）。它提供具有不同核心数量（4到15个）的单芯片模块（SCM）和双芯片模块（DCM）配置，频率高达4.2 GHz。一种特殊的“eSCM”提供增强的I/O。

由Power11驱动的Power E1180服务器与E1080类似，尤其以DDR5内存作为标准配置（可从E1080上的DDR4升级）。它支持高达256个核心和64 TB的内存，分布在四个节点上。本文重点介绍了IBM创新的OpenCAPI内存接口（OMI），从而实现灵活的内存选项。

文章将Power E1180的功能与AMD和Intel服务器进行了比较，强调了IBM系统中计算、内存和I/O之间的平衡。它暗示了一种未来的“xDCM”，通过重新配置内存/I/O端口以用于NUMA链接，进一步提高核心数量，从而增强虚拟化能力。文章最后提供了一个表格，比较了基于Power9、Power10和Power11处理器的最新三代高端Power Systems机器的规格，以及理论上的Power E1185和Power E1185X可能的比较。

---

## 44. 克劳德代码释放

**原文标题**: Claude Code Unleashed

**原文链接**: [https://ymichael.com/2025/07/15/claude-code-unleashed](https://ymichael.com/2025/07/15/claude-code-unleashed)

本文详细介绍了作者使用Claude Code的经验，以及Terragon的开发，Terragon是一个用于管理在云端运行的多个Claude Code代理的系统。作者强调了通过将编码任务卸载到后台代理所获得的显著生产力提升，尤其是Anthropic的“Claude Max”订阅，该订阅实际上提供了无限的使用量。

本文重点介绍了使用git工作树在本地运行多个代理所面临的挑战，指出上下文切换和资源争用是主要的缺点。Terragon通过为每个任务提供全新的云环境来解决这个问题，从而实现并行执行和无缝任务创建，使得调查错误、原型化功能和执行代码清理变得更加容易。

作者现在的工作流程涉及一种混合方法：Terragon处理大多数初始任务执行，而本地开发则侧重于审查、测试和改进代理的工作。他们已经确定了诸如探索、一次性修复、样板生成和上下文密集型调试等任务，特别适合后台代理。

主要经验包括了解模型的优点和缺点，知道何时放弃无效率的任务，以及管理并行工作流程带来的增加的上下文切换。作者强调，使用代理并不能取代开发人员的技能，而是提高生产力并专注于需要人为判断的任务的工具。他们对后台代理的未来以及它们如何改变软件开发工作的方式感到兴奋。

---

## 45. 只需几下按键，欧盟即可被关闭。

**原文标题**: The EU can be shut down with a few keystrokes

**原文链接**: [https://www.bitecode.dev/p/the-eu-can-be-shut-down-with-a-few](https://www.bitecode.dev/p/the-eu-can-be-shut-down-with-a-few)

欧盟面临美国数字封锁风险：技术依赖下的“黑暗依赖黑洞”

---

## 46. 加州大学撤资对冲基金，首席投资官批评高收费、低回报。

**原文标题**: UC divests hedge funds as CIO criticizes high fees, low returns

**原文链接**: [https://www.pionline.com/institutional-investors/endowments-foundations/pi-university-california-hedge-funds-endowment-asset-allocation/](https://www.pionline.com/institutional-investors/endowments-foundations/pi-university-california-hedge-funds-endowment-asset-allocation/)

加州大学因高额费用和低回报撤资对冲基金，此举源于首席投资官Jagdeep Singh Bachher的批评。该举措是更广泛战略的一部分，也包括削减加州大学养老基金在私募市场的投资。此消息由《养老金与投资》于2025年7月16日报道。

文章还提到相关行业新闻，包括：

*   富兰克林邓普顿聘请美世的Rich Nuzum领导一项新的外包首席投资官（OCIO）计划。
*   加州公务员退休基金（CalPERS）任命PGGM养老基金的一位高管担任私募债务主管。
*   《养老金与投资》正在接受年度最大对冲基金经理报告的调查。
*   英仕曼集团选择了一位首席投资官，并作为业务重塑的一部分小幅裁员。

---

## 47. 自学成才的工程师通常表现更出色（2024）

**原文标题**: Self-taught engineers often outperform (2024)

**原文链接**: [https://michaelbastos.com/blog/why-self-taught-engineers-often-outperform](https://michaelbastos.com/blog/why-self-taught-engineers-often-outperform)

无法访问文章链接。

---

## 48. Show HN: PlutoFilter - 一个 C 语言的单头文件、零内存分配图像滤镜库

**原文标题**: Show HN: PlutoFilter- A single-header, zero-allocation image filter library in C

**原文链接**: [https://github.com/sammycage/plutofilter](https://github.com/sammycage/plutofilter)

PlutoFilter是一个单头文件、零内存分配的C语言图像滤镜库。它提供快速且可链式调用的图像特效，兼容SVG和CSS滤镜语义，确保跨平台视觉效果一致。

安装简单：包含头文件即可。要包含实现，在包含头文件之前在一个`.c`或`.cpp`文件中定义`PLUTOFILTER_IMPLEMENTATION`。在包含头文件之前定义`PLUTOFILTER_BUILD_STATIC`会将所有函数声明为静态函数，防止嵌入时出现符号冲突。

该库提供各种图像滤镜，包括高斯模糊、颜色变换（灰度、棕褐色、饱和度、亮度、对比度、不透明度、反相、色相旋转、亮度到Alpha、线性RGB到sRGB、sRGB到线性RGB）、混合模式（普通、正片叠底、滤色等）以及合成模式（覆盖、内、外等）。每个滤镜都通过专用函数应用，并将输入和输出表面作为参数。`plutofilter_color_transform`函数应用一个5x4颜色变换矩阵，用于复杂的颜色调整。每个滤镜都提供了示例，展示了它们在不同参数值下的效果。

路线图包括未来增加的功能，例如形态学、漫反射光照等。该库避免动态内存分配，使其在资源受限的环境中高效运行。

---

## 49. 公平软件许可组织称微软欧盟让步为“拖延战术”

**原文标题**: Fair software licensing group brands Microsoft EU concessions 'stalling tactic'

**原文链接**: [https://www.theregister.com/2025/07/18/cispe_microsoft_concessions/](https://www.theregister.com/2025/07/18/cispe_microsoft_concessions/)

2025年7月，微软与欧洲云基础设施服务提供商协会(CISPE)达成协议，为欧洲云提供商在自身基础设施上部署微软软件提供更大的灵活性，包括按需付费许可和客户隐私协议。此举旨在解决两年前向欧盟委员会提出的正式竞争申诉。CISPE强调了增加选择以及在欧洲平台上使用现有许可的益处。

然而，公平软件许可联盟认为这些让步是一种“拖延战术”，旨在通过限制性许可做法来维持微软的市场主导地位。主要的批评集中在Entra ID（前身为Azure Active Directory）与Microsoft 365之间持续的技术捆绑，限制了身份管理的选择。

开放云联盟的Nicky Stewart也表达了同样的看法，认为该协议是“双边协议”，并未解决微软许可做法的核心问题，即这种做法扭曲了英国和欧盟大多数客户的竞争。为了实现公平定价和真正选择，有必要采取全市场的反垄断补救措施。

文章还提到了微软在2022年受欧盟委员会压力下做出的先前让步，包括灵活虚拟化和许可订阅变更。尽管CISPE认为取得了进展，但批评者认为这些不足以创造公平的竞争环境。

---

## 50. 手: 开源机器人手

**原文标题**: Hand: open-source Robot Hand

**原文链接**: [https://github.com/pollen-robotics/AmazingHand](https://github.com/pollen-robotics/AmazingHand)

“Hand: 开源机器人手”项目旨在创建一个低成本、灵巧且富有表现力的人形机器人手，适用于像Reachy2这样的机器人。该奇妙之手在Apache 2.0和Creative Commons Attribution 4.0许可下发布，具有8个自由度、带有柔性外壳的4个手指，以及集成的执行器，无需外部电缆。它被设计为可3D打印，重量约为400克，目标成本低于200欧元。

该手由使用Feetech SCS0009舵机的并联机构驱动，可通过串行总线驱动程序（Waveshare + Python）或Arduino + Feetech TTL Linker进行控制。该项目提供构建资源，如物料清单（BOM）、CAD文件（STL、STEP、Onshape）和组装指南。 Python和Arduino都有可用的校准脚本。

虽然由于制造公差，实际角度存在差异，但该项目利用SCS0009舵机的智能功能进行高级控制。该项目鼓励社区贡献，并提供基本演示软件的说明，以及更高级的演示和配置工具。

未来的发展计划包括设计用于电源和串行集线器功能的定制PCB、测试综合任务、通过电机反馈改进手部闭合行为、探索不同的手指长度或第五根手指、研究STS3032电机、添加带有弹簧的柔顺连杆，以及加入指尖传感器以实现更智能的控制。可通过Discord频道获得社区支持，该项目感谢Steve N'Guyen、Pierre Rouanet、Augustin Crampette和Matthieu Lapeyre等贡献者。

---

## 51. 从海底寻回的亚历山大灯塔石块

**原文标题**: Stone blocks from the Lighthouse of Alexandria recovered from seafloor

**原文链接**: [https://archaeologymag.com/2025/07/lighthouse-of-alexandria-rises-again/](https://archaeologymag.com/2025/07/lighthouse-of-alexandria-rises-again/)

文章宣布从海底寻回亚历山大灯塔的石块。虽然细节尚不清楚，但这一发现标志着在了解古代世界七大奇迹之一方面取得了重大的考古突破，并暗示着可能深入了解灯塔的建造、建筑和最终的损毁。

文章还提到了另一项无关的考古发现：2025年安提凯瑟拉沉船的挖掘工作揭示了古代造船的秘密。这一单独的发现表明我们对古代航海技术和造船实践的理解有所进步。安提凯瑟拉沉船因出土了安提凯瑟拉机械装置（一种古代模拟计算机）而闻名。因此，该遗址的进一步发现有望对理解古代技术和工程具有重要意义。

本质上，这篇文章强调了两项重要的考古进展：亚历山大灯塔遗骸的寻回和从安提凯瑟拉沉船挖掘中获得的对古代造船的新见解。这两项发现都有助于更深入地了解古代世界的技术能力和文化遗产。

---

## 52. 我的银行一直在破坏反钓鱼教育。

**原文标题**: My bank keeps on undermining anti-phishing education

**原文链接**: [http://moritz-mander.de/blog/my_bank_keeps_on_undermining_anti-phishing_education/](http://moritz-mander.de/blog/my_bank_keeps_on_undermining_anti-phishing_education/)

本文详述了作者对其德国储蓄银行（Sparkasse）“Wero-Win Weeks”抽奖活动的促销邮件和网站感到沮丧，认为它们类似于网络钓鱼诈骗，并破坏了反网络钓鱼教育工作。

该邮件推广通过使用Wero支付系统赢得金钱的机会，其中包含指向一个与银行主域名无关的网站（“gewinnen-mit-wero.de”）的链接。作者指出了几个危险信号：通用域名、缺乏抽奖活动的背景信息、使用Let's Encrypt SSL证书而不是主要提供商，以及一个注册表格，要求提供敏感信息（姓名、出生日期、IBAN、电子邮件），而不是直接集成到银行的应用程序中。

作者认为，这种类型的促销活动使可疑行为正常化，使得用户更难以区分合法通信和实际的网络钓鱼尝试。他们引用了该银行过去发送类似的可疑通信的例子，例如包含短链接的短信。

可能的解决方案包括将抽奖活动整合到银行的应用程序中，或者使用银行官方网站（sparkasse.de）的子域名进行促销活动。作者还提到了德国政府为创建一个具有通用域名（gov.de）的标准化在线形象以应对类似问题所做的努力。

最后，文章暗示银行的做法甚至可能造成法律问题。作者援引银行不得不退还网络钓鱼受害者损失的裁决，认为银行令人困惑的促销活动可能会使证明客户在遭遇类似网络钓鱼诈骗时存在“重大过失”变得困难。作者最后恳请金融机构优先考虑可用安全性，避免破坏网络钓鱼教育工作。

---

## 53. 天文学家发现与海王星同步的罕见遥远天体

**原文标题**: Astronomers Discover Rare Distant Object in Sync with Neptune

**原文链接**: [https://pweb.cfa.harvard.edu/news/astronomers-discover-rare-distant-object-sync-neptune](https://pweb.cfa.harvard.edu/news/astronomers-discover-rare-distant-object-sync-neptune)

天文学家发现一颗罕见的跨海王星天体，其轨道与海王星保持稳定的同步共振。这颗名为2022 VX166的跨海王星天体是一个“2:3共振”天体，意味着海王星每绕太阳运行三圈，它就绕太阳运行两圈。这种轨道共振在跨海王星天体中相对常见，但2022 VX166的独特之处在于它是一颗“高倾角”天体，其轨道与大多数行星所在的太阳系平面呈显著角度（约30度）。

这项发现的意义在于，在这种特定的轨道共振中发现高倾角跨海王星天体的罕见性。这些天体为早期太阳系的形成和演化提供了宝贵的见解。海王星与这些共振跨海王星天体之间的引力相互作用可能在塑造外太阳系方面发挥了关键作用。

这项发现是利用位于智利的Víctor M. Blanco 4米望远镜上的暗能量相机（DECam）完成的。通过精确跟踪该天体的运动，天文学家能够确定其轨道参数并确认其与海王星的共振关系。研究人员认为，研究这些罕见的高倾角共振天体有助于约束行星迁移和太阳系早期动力学的模型，从而揭示行星是如何 settling 到当前位置的。

---

## 54. 鸽子河悬于高处，地质灾难预兆 (2020)

**原文标题**: The Pigeon River Is Perched, Which Is Geologically Bad News (2020)

**原文链接**: [https://princegeology.com/the-pigeon-river-is-perched-which-is-geologically-bad-news-for-it/](https://princegeology.com/the-pigeon-river-is-perched-which-is-geologically-bad-news-for-it/)

本文探讨了在坎顿（北卡罗来纳州附近）的鸽子河即将被法国宽河的支流霍米尼溪袭夺（地质学意义上）的可能性。鸽子河谷比法国宽河谷高出约400英尺，这为较低的法国宽河系统袭夺鸽子河的流量创造了条件。

霍米尼溪的源头距离鸽子河仅约1500英尺，分水岭仅有20英尺的细微落差。作者认为，一条运河可以很容易地连接这两个河流系统。当河流袭夺自然发生时，鸽子河的水下降400英尺至法国宽河，将产生巨大的激流和峡谷。

文章解释了霍米尼溪如何侵入鸽子河系统，颠倒了支流正常的分支模式，形成了“抓钩”形状。这得益于基岩中的一个薄弱地带，可能是断层或断裂区域，这使得侵蚀更容易。

虽然确切原因难以确定，但两条河流之间的大小和地质差异可能发挥作用。较大的法国宽河可以更有效地侵蚀其河谷，可能使鸽子河“滞留”在较高的海拔。作者承认这种袭夺的时间表尚不确定，但指出即使鸽子河发生一次大洪水，也可能在“地质未来”引发河流袭夺。

---

## 55. Anthropic收紧Claude Code使用限制，未告知用户

**原文标题**: Anthropic tightens usage limits for Claude Code without telling users

**原文链接**: [https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/](https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/)

Anthropic悄然收紧Claude Code使用限制，引发用户不满和困惑，尤其是每月200美元Max套餐用户。用户比预期更早遇到“Claude使用量已达上限”提示，且Anthropic未事先通知或明确解释。这导致人们猜测订阅降级或使用量跟踪不准确。

Anthropic代表承认存在问题和响应速度变慢，但未提供更多细节。由于突然的限制，用户难以继续项目，并发现替代方案无法与Claude Code的功能相媲美。

Anthropic的网络问题也加剧了这种情况，API用户报告出现过载错误。用户不满的关键在于Anthropic的分级定价系统，该系统承诺更高的使用限制，但未保证具体的访问级别，导致用户无法可靠地规划其使用情况。Max套餐虽然因其高使用潜力而受欢迎，但一些人认为Anthropic可能无法持续提供支持。用户主要要求提高透明度，并就使用限制进行更清晰的沟通。缺乏沟通正在削弱用户信心。

---

## 56. USB-C 集线器与我逐渐崩溃的疯狂（2021）

**原文标题**: USB-C hubs and my slow descent into madness (2021)

**原文链接**: [https://overengineer.dev/blog/2021/04/25/usb-c-hub-madness/](https://overengineer.dev/blog/2021/04/25/usb-c-hub-madness/)

本文作者吐槽自2018年以来使用USB-C扩展坞的糟糕体验，起因是最近一次险些酿成灾难的扩展坞故障。作为端口有限的Apple MacBook Pro用户，作者购买了三个不同的扩展坞（Satechi、ICY BOX和Anker），但都发现它们存在缺陷。

Satechi扩展坞存在HDMI信号中断和以太网连接不可靠的问题，最终彻底报废。拆解后发现它们是Gopod的贴牌产品，很可能可以用更低的价格买到。ICY BOX扩展坞也受到以太网问题的困扰（降级到100baseTX），客户支持很差，而且有一个差点因过热而引起火灾。这些扩展坞也被确认为东莞劲拓的贴牌产品。

一个反复出现的问题是，这两个扩展坞都使用了Realtek RTL8153以太网芯片。作者详细介绍了关于这款芯片在macOS上不可靠的大量投诉，包括连接中断和速度降级，作者也遇到了这些问题。他们批评Realtek没有提供更新的macOS驱动程序来解决这些问题。

最后，作者购买了一个Anker PowerExpand 8合1扩展坞。虽然最初功能正常，但同样是Realtek RTL8153芯片的存在以及出于“科学”原因拆卸设备的冲动促使他们写下了这篇文章，并且越发愤世嫉俗地看待USB-C扩展坞的质量和品牌营销行为。作者表示，制造商经常贴牌销售来自其他公司的廉价、不可靠的产品，导致价格过高且性能不佳的扩展坞。

---

## 57. 迷幻蘑菇分子显示出延缓衰老迹象

**原文标题**: Psychedelic mushroom molecule just showed signs of slowing aging

**原文链接**: [https://twitter.com/bryan_johnson/status/1943824432419811437](https://twitter.com/bryan_johnson/status/1943824432419811437)

由于JavaScript被禁用，标题为“迷幻蘑菇分子显示出减缓衰老迹象”的文章无法访问。提供的内容是来自X.com（前身为Twitter）的标准消息，表明网站在未启用JavaScript的情况下无法正常运行。因此，**无法提供文章内容的摘要，因为文章本身不可见。** 该错误消息暗示内容讨论了一项研究，该研究表明在迷幻蘑菇中发现的一种分子可能具有抗衰老特性。然而，在未看到实际文章的情况下，这仍然是推测性的。

---

## 58. Rust中可扩展变体与CGP的模块化解释器和访问者

**原文标题**: Modular Interpreters and Visitors in Rust with Extensible Variants and CGP

**原文链接**: [https://contextgeneric.dev/blog/extensible-datatypes-part-2/](https://contextgeneric.dev/blog/extensible-datatypes-part-2/)

本文是关于在 Rust 中使用 CGP（可组合泛型编程）的系列文章的第二篇，重点介绍如何利用可扩展变体来构建模块化解释器和访问者。它解决了传统访问者模式的局限性，特别是其封闭性，这种封闭性阻碍了在处理诸如抽象语法树或序列化格式等不断演变的数据结构时的可扩展性。核心问题是数据结构（例如，MathExpr 枚举）与操作它的函数（例如，`eval` 函数）之间的紧密耦合，从而导致“表达式问题”，即添加新的变体需要修改现有代码。

所提出的解决方案使用 CGP 将评估逻辑与具体的枚举定义分离。这是通过将诸如 `Plus`、`Times` 和 `Literal` 之类的表达式类型定义为由泛型 `Expr` 类型参数化的独立结构来实现的。引入 `Computer` trait 作为 CGP 组件，体现将输入转换为输出的纯计算。然后，每个表达式类型都有一个对应的提供者（例如，`EvalAdd`、`EvalMultiply`、`EvalLiteral`），它们实现了 `Computer` trait。这些提供者以泛型方式运行，依靠上下文来处理子表达式，并通过 trait 边界确保类型安全。

最后，定义了一个具体的 `MathExpr` 枚举，但它没有直接嵌入表达式结构，而是包装了独立的结构。这种设计允许每个提供者独立开发和组合，从而产生一个模块化和可扩展的解释器，避免了传统访问者模式的局限性，并有效地解决了表达式问题。关键在于通过将每个变体的实现与具体的枚举定义分离，从而提高了灵活性和可维护性。

---

## 59. 苹果智能基础语言模型技术报告2025

**原文标题**: Apple Intelligence Foundation Language Models Tech Report 2025

**原文链接**: [https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)

Apple智能基金会语言模型技术报告2025介绍了两个全新的多语言、多模态基金会语言模型，为Apple智能功能提供支持：一个设备端模型（约30亿参数）和一个可扩展的服务器模型。

设备端模型针对Apple芯片进行了优化，采用了诸如KV缓存共享和2位量化感知训练等技术。服务器模型利用了一种新颖的并行轨道混合专家(PT-MoE) Transformer，结合了轨道并行、稀疏计算和交错的全局-局部注意力，从而在Apple的私有云计算平台上实现高质量和成本效益。

这两个模型都经过大规模多语言和多模态数据集的训练，这些数据集通过负责任的网页爬取、许可语料库和合成数据获得，然后通过监督微调和强化学习进行改进。这使得它们能够支持更多语言，理解图像并执行工具调用。基准测试表明，其性能与同类开源模型相当或超越。

一个以Swift为中心的新基金会模型框架使开发人员可以轻松地将这些模型的功能（引导生成、约束工具调用、LoRA适配器微调）集成到他们的应用程序中。这些模型结合了负责任的AI安全措施，如内容过滤和特定于地区的评估，并通过私有云计算等创新来优先考虑用户隐私。

本报告详细介绍了2025年6月推出的更新，它建立在2024年7月发布的初始模型以及在2024年全球开发者大会上首次展示的模型之上。这些模型专门用于日常任务，例如文本优化、通知管理、图像生成和应用内操作。

---

## 60. 23andMe已摆脱破产，但其行事方式并未发生实质性改变。

**原文标题**: 23andMe is out of bankruptcy and it still hasn’t substantially changed its ways

**原文链接**: [https://www.washingtonpost.com/technology/2025/07/17/23andme-bankruptcy-privacy/](https://www.washingtonpost.com/technology/2025/07/17/23andme-bankruptcy-privacy/)

无法访问文章链接。

---

## 61. 英国将投票年龄降至16岁，各方反应不一。

**原文标题**: Britain is lowering the voting age to 16. It's getting a mixed reaction

**原文链接**: [https://apnews.com/article/uk-voting-age-16-criticism-debate-f85d8675acbf4bd9ceece51135c369e5](https://apnews.com/article/uk-voting-age-16-criticism-debate-f85d8675acbf4bd9ceece51135c369e5)

无法访问文章链接。

---

## 62. 研究发现：自恐龙时代以来，哺乳动物进化成食蚁兽共12次

**原文标题**: Mammals Evolved into Ant Eaters 12 Times Since Dinosaur Age, Study Finds

**原文链接**: [https://news.njit.edu/mammals-evolved-ant-eaters-12-times-dinosaur-age-study-finds](https://news.njit.edu/mammals-evolved-ant-eaters-12-times-dinosaur-age-study-finds)

一项新研究表明，自恐龙时代以来，哺乳动物至少独立演化成食蚁专家（也称为食蚁兽）12次。这种重复演化突显了这种饮食生态位的成功和适应性。该研究可能调查了已知以蚂蚁和白蚁为食的各种哺乳动物谱系的进化历史和关系，使用遗传或形态数据（或两者）来重建它们的进化树，并确定食蚁行为独立出现的何时以及频率。

研究结果表明，蚂蚁和白蚁群落提供了一种可靠且丰富的食物来源，这反复激励了不同的哺乳动物群体发展出食蚁行为所需的特定适应能力。这些适应能力通常包括用于挖掘的强壮爪子、用于捕获昆虫的长而粘的舌头，以及减少或缺失的牙齿。不同哺乳动物谱系在这些相似特征上的趋同，为趋同进化提供了一个引人注目的例子，即不相关的物种独立进化出相似的特征以应对相似的环境压力。

---

## 63. 做难事

**原文标题**: On doing hard things

**原文链接**: [https://parv.bearblog.dev/kayaking/](https://parv.bearblog.dev/kayaking/)

本文讲述了作者出人意料地开始皮划艇运动的经历，强调了在缺乏天赋的情况下追求一项对体能要求极高的活动的挑战和回报。起初，作者在翻船和协调性方面困难重重，但在学习和进步的过程中发现了一些引人入胜的东西。

文章强调，皮划艇运动的进步，或许人生的进步，并非总是线性的或显而易见的。它以渐进式的提高、对环境更深入的理解以及对失败越来越坦然为特征。作者欣赏这项运动的冥想品质以及他们的队长营造的支持性环境。

尽管从未成为顶尖选手，但作者最终进入了校队并参加了大学间比赛，这标志着重要的个人成就。这次经历教会了作者欣然接受在公共场合出丑，这是一个适用于运动之外的宝贵教训。文章最后将皮划艇运动比作人生，在面对困难时坚持不懈的努力可以带来意想不到的成长和对旅程的独特欣赏，即使没有取得最终的成功。作者还谈到了重视“差一点成功的故事”与成功故事同等重要的意义，承认在挑战中坚持不懈的内在尊严。

---

## 64. 前Waymo工程师创办Bedrock Robotics，以实现建筑自动化

**原文标题**: Ex-Waymo engineers launch Bedrock Robotics to automate construction

**原文链接**: [https://techcrunch.com/2025/07/16/ex-waymo-engineers-launch-bedrock-robotics-with-80m-to-automate-construction/](https://techcrunch.com/2025/07/16/ex-waymo-engineers-launch-bedrock-robotics-with-80m-to-automate-construction/)

由前Waymo和Segment工程师创立的Bedrock Robotics公司，带着Eclipse和8VC提供的8000万美元资金，从隐身模式中走出，致力于为改造建筑和工地车辆开发自动驾驶套件。在首席执行官Boris Sofman（曾任Waymo自动驾驶卡车项目和Anki Robotics高管）的领导下，Bedrock旨在通过传感器和人工智能升级现有车队，使其能够理解项目目标、适应环境并在全天候运营。

该公司瞄准建筑行业，目前正在阿肯色州、亚利桑那州、德克萨斯州和加利福尼亚州与Sundt Construction、Zachry Construction Corporation、Champion Site Prep Inc.和Capitol Aggregates Inc.合作进行测试。

Bedrock是众多将自动驾驶技术应用于越野环境的自动驾驶汽车初创公司中的一员。文章提到了该领域的其他几家公司，包括Pronto（最近收购了SafeAI）、Kodiak Robotics、Polymath Robotics、Overland AI、Potential和Forterra。更广泛的越野自动驾驶领域被描述为分散的。

文章还提到了将于2025年10月27日至29日在旧金山举行的TechCrunch Disrupt 2025大会，届时来自科技界和风险投资界的重要人物将分享见解，助力初创企业发展。

---

## 65. Show HN: 使用国际象棋等级分提高搜索排名

**原文标题**: Show HN: Improving search ranking with chess Elo scores

**原文链接**: [https://www.zeroentropy.dev/blog/improving-rag-with-elo-scores](https://www.zeroentropy.dev/blog/improving-rag-with-elo-scores)

这个“Show HN”帖子重点介绍了一种利用Elo评分提高检索增强生成（RAG）系统性能的尝试。核心思想是使用Elo（一种常用于国际象棋的评分系统）来评估和排序RAG系统检索到的文档的相关性和准确性。

作者可能建议使用Elo来比较不同文档在准确回答给定查询方面的能力。针对相同查询，始终提供比其他文档更好答案的文档将具有更高的Elo评分。

这种排名机制可以以多种方式集成到RAG流程中，例如：

*   **优先处理高Elo文档：** 当检索到多个文档时，系统可以在生成最终答案时优先处理具有较高Elo评分的文档。
*   **过滤低Elo文档：** 可以过滤掉Elo评分低于特定阈值的文档，以减少噪声并提高生成响应的准确性。
*   **将Elo评分用作权重因子：** Elo评分可用作评分函数中的权重因子，该函数确定每个文档与查询的相关性。

预期的好处是通过确保系统专注于最可靠和信息丰富的文档，从而提高RAG在准确性、相关性和连贯性方面的性能。 该实施将需要一种评估文档针对一系列查询质量的机制，可能使用真实数据集和评估指标。 该帖子很可能展示了一种在RAG环境中进行文档排名的新颖方法。

---

## 66. 眼神交流的时间背景影响对沟通意图的感知

**原文标题**: Temporal context of eye contact influences perceptions of communicative intent

**原文链接**: [https://royalsocietypublishing.org/doi/10.1098/rsos.250277](https://royalsocietypublishing.org/doi/10.1098/rsos.250277)

无法访问文章链接。

---

## 67. Running Linux on my Amiga 4000

**原文标题**: Running Linux on my Amiga 4000

**原文链接**: [http://sandervanderburg.blogspot.com/2025/01/running-linux-on-my-amiga-4000.html](http://sandervanderburg.blogspot.com/2025/01/running-linux-on-my-amiga-4000.html)

This blog post details the author's journey to running Linux on an Amiga 4000 in 2025, motivated by both nostalgia and a connection between their Amiga experiences and their eventual adoption of Linux. The author recounts the decline of the Amiga platform after Commodore's demise and their transition to PCs running MS-DOS and Windows. Initially unimpressed by the instability and resource-intensive nature of Windows 95, they discovered Linux through PC magazines and the DOS UAE emulator.

Their first hands-on experience with Linux in 1999, thanks to a cousin studying Computer Science, impressed them with its multitasking, command-line interface, powerful filesystem, security features, modularity, and available applications. They highlight the collaborative development model of Linux, involving Linus Torvalds, the GNU project, and various community efforts.

The author faced challenges installing Linux on their home computer due to driver issues. During this process, they discovered Linux's portability to various architectures, including the Amiga. Now with a 68040-equipped Amiga 4000, they revisit the idea of running Linux on it. The post ends by noting that the actively developed Debian distribution still maintains an m68k port and getting started with Linux on the Amiga can be a challenge due to lack of readily available distrobutions.


---

## 68. Louisiana cancels $3B coastal repair funded by oil spill settlement

**原文标题**: Louisiana cancels $3B coastal repair funded by oil spill settlement

**原文链接**: [https://apnews.com/article/louisiana-coastal-restoration-gulf-oil-spill-affaae2877bf250f636a633a14fbd0c7](https://apnews.com/article/louisiana-coastal-restoration-gulf-oil-spill-affaae2877bf250f636a633a14fbd0c7)

生成摘要时出错

---

## 69. Metaflow：构建、管理和部署AI/ML系统

**原文标题**: Metaflow: Build, Manage and Deploy AI/ML Systems

**原文链接**: [https://github.com/Netflix/metaflow](https://github.com/Netflix/metaflow)

生成摘要时出错

---

## 70. Linux and Secure Boot certificate expiration

**原文标题**: Linux and Secure Boot certificate expiration

**原文链接**: [https://lwn.net/SubscriberLink/1029767/08f1d17c020e8292/](https://lwn.net/SubscriberLink/1029767/08f1d17c020e8292/)

生成摘要时出错

---

## 71. “Reading Rainbow” was created to combat summer reading slumps

**原文标题**: “Reading Rainbow” was created to combat summer reading slumps

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/to-combat-summer-reading-slumps-this-timeless-childrens-television-show-tried-to-bridge-the-literacy-gap-with-the-magic-of-stories-180986984/](https://www.smithsonianmag.com/smithsonian-institution/to-combat-summer-reading-slumps-this-timeless-childrens-television-show-tried-to-bridge-the-literacy-gap-with-the-magic-of-stories-180986984/)

"Reading Rainbow," the beloved children's program hosted by LeVar Burton, premiered on PBS in 1983 to combat the "summer slide," a decline in literacy skills among children during summer break. The show ran for 23 years, won numerous awards, and is seen as a key example of a program promoting literacy, reading comprehension, and the joy of storytelling.

Each episode featured Burton introducing a children’s book and its subject matter through real-world field trips, followed by a reading of the book by a celebrity. The program also incorporated children's book reviews.

The show's creation originated at WNED-TV in Buffalo, New York, where Tony Buttino, Barbara Irwin, and Pam Johnson collaborated. They sought a host who could genuinely connect with children and found that person in LeVar Burton. Despite an initial rejection of their proposal, the team persevered and eventually partnered with Great Plains National to secure funding for the show.

“Reading Rainbow” was highly successful, praised by teachers as the best educational program, and inspired a lifelong love of reading in its viewers. It stood out for its unique format of combining book illustrations with Burton's real-life adventures, showcasing diverse people and places. According to Irwin, "no series did it any better than ‘Reading Rainbow’ did."


---

## 72. I want an iPhone Mini-sized Android phone (2022)

**原文标题**: I want an iPhone Mini-sized Android phone (2022)

**原文链接**: [https://smallandroidphone.com/](https://smallandroidphone.com/)

生成摘要时出错

---

## 73. This month in Servo: network inspector, a11y first steps, WebDriver, and more

**原文标题**: This month in Servo: network inspector, a11y first steps, WebDriver, and more

**原文链接**: [https://servo.org/blog/2025/07/17/this-month-in-servo/](https://servo.org/blog/2025/07/17/this-month-in-servo/)

生成摘要时出错

---

## 74. NINA: Rebuilding the original AIM, AOL Desktop, Yahoo and ICQ platforms

**原文标题**: NINA: Rebuilding the original AIM, AOL Desktop, Yahoo and ICQ platforms

**原文链接**: [https://nina.chat/](https://nina.chat/)

生成摘要时出错

---

## 75. Xbox Hacks: The A20 (2021)

**原文标题**: Xbox Hacks: The A20 (2021)

**原文链接**: [https://connortumbleson.com/2021/07/19/the-xbox-and-a20-line/](https://connortumbleson.com/2021/07/19/the-xbox-and-a20-line/)

生成摘要时出错

---

## 76. ICE's Supercharged Facial Recognition App of 200M Images

**原文标题**: ICE's Supercharged Facial Recognition App of 200M Images

**原文链接**: [https://www.404media.co/inside-ices-supercharged-facial-recognition-app-of-200-million-images/](https://www.404media.co/inside-ices-supercharged-facial-recognition-app-of-200-million-images/)

生成摘要时出错

---

## 77. Retro gaming YouTuber Once Were Nerd sued and raided by the Italian government

**原文标题**: Retro gaming YouTuber Once Were Nerd sued and raided by the Italian government

**原文链接**: [https://www.androidauthority.com/once-were-nerd-youtuber-copyright-lawsuit-3577995/](https://www.androidauthority.com/once-were-nerd-youtuber-copyright-lawsuit-3577995/)

生成摘要时出错

---

## 78. A 1960s schools experiment that created a new alphabet

**原文标题**: A 1960s schools experiment that created a new alphabet

**原文链接**: [https://www.theguardian.com/education/2025/jul/06/1960s-schools-experiment-created-new-alphabet-thousands-children-unable-to-spell](https://www.theguardian.com/education/2025/jul/06/1960s-schools-experiment-created-new-alphabet-thousands-children-unable-to-spell)

生成摘要时出错

---

## 79. Wttr: Console-oriented weather forecast service

**原文标题**: Wttr: Console-oriented weather forecast service

**原文链接**: [https://github.com/chubin/wttr.in](https://github.com/chubin/wttr.in)

生成摘要时出错

---

## 80. LLM Inevitabilism

**原文标题**: LLM Inevitabilism

**原文链接**: [https://tomrenner.com/posts/llm-inevitabilism/](https://tomrenner.com/posts/llm-inevitabilism/)

生成摘要时出错

---

## 81. Six Years of Gemini

**原文标题**: Six Years of Gemini

**原文链接**: [https://geminiprotocol.net/news/2025_06_20.gmi](https://geminiprotocol.net/news/2025_06_20.gmi)

生成摘要时出错

---

## 82. Archaeologists discover tomb of first king of Caracol

**原文标题**: Archaeologists discover tomb of first king of Caracol

**原文链接**: [https://uh.edu/news-events/stories/2025/july/07102025-caracol-chase-discovery-maya-ruler.php](https://uh.edu/news-events/stories/2025/july/07102025-caracol-chase-discovery-maya-ruler.php)

生成摘要时出错

---

## 83. Valve confirms credit card companies pressured it to delist certain adult games

**原文标题**: Valve confirms credit card companies pressured it to delist certain adult games

**原文链接**: [https://www.pcgamer.com/software/platforms/valve-confirms-credit-card-companies-pressured-it-to-delist-certain-adult-games-from-steam/](https://www.pcgamer.com/software/platforms/valve-confirms-credit-card-companies-pressured-it-to-delist-certain-adult-games-from-steam/)

生成摘要时出错

---

## 84. ACA health insurance will cost the average person 75% more next year

**原文标题**: ACA health insurance will cost the average person 75% more next year

**原文链接**: [https://www.npr.org/sections/shots-health-news/2025/07/18/nx-s1-5471281/aca-health-insurance-premiums-obamacare-bbb-kff](https://www.npr.org/sections/shots-health-news/2025/07/18/nx-s1-5471281/aca-health-insurance-premiums-obamacare-bbb-kff)

生成摘要时出错

---

## 85. Why is AI so slow to spread?

**原文标题**: Why is AI so slow to spread?

**原文链接**: [https://www.economist.com/finance-and-economics/2025/07/17/why-is-ai-so-slow-to-spread-economics-can-explain](https://www.economist.com/finance-and-economics/2025/07/17/why-is-ai-so-slow-to-spread-economics-can-explain)

生成摘要时出错

---

## 86. Scanned piano rolls database

**原文标题**: Scanned piano rolls database

**原文链接**: [http://www.pianorollmusic.org/rolldatabase.php](http://www.pianorollmusic.org/rolldatabase.php)

生成摘要时出错

---

## 87. Altermagnets: The first new type of magnet in nearly a century

**原文标题**: Altermagnets: The first new type of magnet in nearly a century

**原文链接**: [https://www.newscientist.com/article/2487013-weve-discovered-a-new-kind-of-magnetism-what-can-we-do-with-it/](https://www.newscientist.com/article/2487013-weve-discovered-a-new-kind-of-magnetism-what-can-we-do-with-it/)

生成摘要时出错

---

## 88. LLM Daydreaming

**原文标题**: LLM Daydreaming

**原文链接**: [https://gwern.net/ai-daydreaming](https://gwern.net/ai-daydreaming)

生成摘要时出错

---

## 89. Parsing Protobuf Like Never Before

**原文标题**: Parsing Protobuf Like Never Before

**原文链接**: [https://mcyoung.xyz/2025/07/16/hyperpb/](https://mcyoung.xyz/2025/07/16/hyperpb/)

生成摘要时出错

---

## 90. What's happening to reading?

**原文标题**: What's happening to reading?

**原文链接**: [https://www.newyorker.com/culture/open-questions/whats-happening-to-reading](https://www.newyorker.com/culture/open-questions/whats-happening-to-reading)

生成摘要时出错

---

## 91. Game of trees hub

**原文标题**: Game of trees hub

**原文链接**: [https://gothub.org/](https://gothub.org/)

生成摘要时出错

---

## 92. Show HN: 0xDEAD//TYPE – A fast-paced typing shooter with retro vibes

**原文标题**: Show HN: 0xDEAD//TYPE – A fast-paced typing shooter with retro vibes

**原文链接**: [https://0xdeadtype.theden.sh/](https://0xdeadtype.theden.sh/)

生成摘要时出错

---

## 93. Roman dodecahedron: 12-sided object has baffled archaeologists for centuries

**原文标题**: Roman dodecahedron: 12-sided object has baffled archaeologists for centuries

**原文链接**: [https://www.livescience.com/archaeology/romans/roman-dodecahedron-a-mysterious-12-sided-object-that-has-baffled-archaeologists-for-centuries](https://www.livescience.com/archaeology/romans/roman-dodecahedron-a-mysterious-12-sided-object-that-has-baffled-archaeologists-for-centuries)

生成摘要时出错

---

## 94. Writing a competitive BZip2 encoder in Ada from scratch in a few days (2024)

**原文标题**: Writing a competitive BZip2 encoder in Ada from scratch in a few days (2024)

**原文链接**: [https://gautiersblog.blogspot.com/2024/11/writing-bzip2-encoder-in-ada-from.html](https://gautiersblog.blogspot.com/2024/11/writing-bzip2-encoder-in-ada-from.html)

生成摘要时出错

---

## 95. What's going on with gene therapies?

**原文标题**: What's going on with gene therapies?

**原文链接**: [https://nehalslearnings.substack.com/p/whats-going-on-with-gene-therapies](https://nehalslearnings.substack.com/p/whats-going-on-with-gene-therapies)

生成摘要时出错

---

## 96. Claude for Financial Services

**原文标题**: Claude for Financial Services

**原文链接**: [https://www.anthropic.com/news/claude-for-financial-services](https://www.anthropic.com/news/claude-for-financial-services)

生成摘要时出错

---

## 97. Signs of autism could be encoded in the way you walk

**原文标题**: Signs of autism could be encoded in the way you walk

**原文链接**: [https://www.sciencealert.com/signs-of-autism-could-be-encoded-in-the-way-you-walk](https://www.sciencealert.com/signs-of-autism-could-be-encoded-in-the-way-you-walk)

生成摘要时出错

---

## 98. MARS.EXE → COM (2021)

**原文标题**: MARS.EXE → COM (2021)

**原文链接**: [https://chaos.if.uj.edu.pl/~wojtek/MARS.COM/](https://chaos.if.uj.edu.pl/~wojtek/MARS.COM/)

生成摘要时出错

---

## 99. From engineer to manager: A practical guide to your first months in leadership

**原文标题**: From engineer to manager: A practical guide to your first months in leadership

**原文链接**: [https://humansinsystems.com/blog/new-manager-essentials-a-practical-guide-to-your-first-months](https://humansinsystems.com/blog/new-manager-essentials-a-practical-guide-to-your-first-months)

生成摘要时出错

---

## 100. Running a million-board chess MMO in a single process

**原文标题**: Running a million-board chess MMO in a single process

**原文链接**: [https://eieio.games/blog/a-million-realtime-chess-boards-in-a-single-process/](https://eieio.games/blog/a-million-realtime-chess-boards-in-a-single-process/)

生成摘要时出错

---

