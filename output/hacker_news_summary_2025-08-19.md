# Hacker News 热门文章摘要 (2025-08-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们如何利用 CodeRabbit：从简单的 PR 到 RCE 以及 100 万个代码仓库的写入权限

**原文标题**: How We Exploited CodeRabbit: From Simple PR to RCE and Write Access on 1M Repos

**原文链接**: [https://research.kudelskisecurity.com/2025/08/19/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories/](https://research.kudelskisecurity.com/2025/08/19/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories/)

尼尔斯·阿米埃特详细描述了他们如何在 CodeRabbit 的生产服务器上实现远程代码执行 (RCE)，从而获得对敏感数据的访问权限并可能影响 100 万个代码仓库。在一次安全讲座后的谈话启发下，阿米埃特调查了 CodeRabbit，这是一款在 GitHub 和 GitLab 上流行的 AI 代码审查工具。

通过利用 CodeRabbit 对各种静态分析工具的支持，特别是 Rubocop (一个 Ruby 静态分析器)，阿米埃特发现了一个漏洞。CodeRabbit 允许用户使用配置文件来配置这些工具。阿米埃特创建了一个包含恶意 Rubocop 配置文件 (.rubocop.yml) 的恶意拉取请求，该文件加载了一个恶意的 Ruby 扩展 (ext.rb)。该扩展程序在被 Rubocop 执行时，会将服务器的环境变量泄露到一个攻击者控制的服务器。

泄露的环境变量包括 OpenAI、Anthropic、Pinecone、Langchain 和其他服务的 API 密钥，以及数据库凭据（PostgreSQL 主机、用户名和密码）、CodeRabbit GitHub App 的私钥和密钥，以及其他敏感信息。获得的 RCE 本可用于连接到内部 Postgres 数据库，从而可能实现破坏性操作或从 Docker 容器中提取源代码。这一漏洞演示了 CodeRabbit 在处理外部工具和配置方面的重大安全缺陷，最终授予了对大量代码仓库的读写访问权限。

---

## 2. 没有 Futex，徒劳无功。

**原文标题**: Without the Futex, It's Futile

**原文链接**: [https://h4x0r.org/futex/](https://h4x0r.org/futex/)

本文批评《多处理器编程的艺术》未涵盖 futex，这是一种现代并发编程的基本构建块。作者认为，futex 已经彻底改变了并发性，使得较旧的 System V IPC 方法过时。

Futex 将锁定与等待和唤醒分离，通过避免不必要的系统调用来实现更好的性能。与 System V 不同，如果没有线程在等待，解锁操作可以避免内核调用。 Futex 允许线程在内核中阻塞和排队，并与内存地址关联，还包括可选的超时。本文强调，操作系统处理 futex 上的操作顺序，仅在对当前状态有正确视图时才将等待者入队。

作者提供了代码示例，包括 Linux 和 macOS 上 futex 功能的封装，并演示了如何使用 futex 构建基本的互斥锁和自旋锁。自旋锁代码展示了使用原子操作获取和释放锁的实现。本文还讨论了自旋锁中可能出现的重度争用、不正确的解锁和死锁问题。作者批评了该书建议在使用指数退避来处理锁争用时使用 `sleep()`，以及在线程唤醒之前锁已释放时浪费的阻塞时间。

---

## 3. 使用 Emacs 进行视频剪辑

**原文标题**: Emacs as your video-trimming tool

**原文链接**: [https://xenodium.com/emacs-as-your-video-trimming-tool](https://xenodium.com/emacs-as-your-video-trimming-tool)

本文探讨了如何使用 Emacs 作为视频剪辑工具，其灵感来源于 Marcin 'mbork' Borkowski 的一篇博客文章。作者同样需要一个比 macOS 自带的 QuickTime Player 更简单的剪辑方案，因此开发了 `video-trimmer-mode`，这是一个大约 300 行的 Emacs 配置，利用 `ffmpeg` 进行视频处理。

作者强调，他们不需要复杂的视频编辑功能，并且发现现有工具不够完美，特别是为 Ready Player Mode 添加图形化寻址器激发了他们的灵感。作者并未在博文中分享完整代码，而是引导读者访问其 Emacs 配置仓库中的最新版本，并期待进一步的完善。

文章最后呼吁大家提供支持，鼓励读者赞助作者的独立开发工作，强调可持续性的重要性。文章还包含指向作者提供的其他服务的链接，例如博客开发和 macOS/iOS 应用，以及标准的隐私政策和服务条款。

---

## 4. 从HTML规范中移除对XSLT的提及

**原文标题**: "Remove mentions of XSLT from the html spec"

**原文链接**: [https://github.com/whatwg/html/pull/11563](https://github.com/whatwg/html/pull/11563)

此 GitHub issue 提议从 HTML 规范中移除对 XSLT 的提及。作者 mfreed7 认为至少有两家实现者对此移除感兴趣，且没有反对意见。他们提供了测试链接、为 Chromium、Gecko 和 WebKit 提交的实现错误，以及 HTML AAM & ARIA 和 MDN 文档的相关 issue 和 PR。其理由与 WHATWG 工作模式一致。

然而，一些评论者表达了担忧。gucci-on-fleek 质疑移除 XSLT 支持是否会破坏旧的、不常更新的网站。他们强调，如果不再支持 `<?xml-stylesheet … ?>`，用户可能会看到原始 XML 而不是格式化的内容，存在这种风险。nomis 提供了 XSLT 的现有用例示例，包括政府网站和微控制器应用，认为页面加载统计数据不能准确反映可访问内容的数量。他们认为，浏览器仅支持 XSLT 1.0 限制了其采用。

jonsterling 反对移除，强调了 XSLT 的多样化用途，并提倡由用户驱动的 Web 平台。他们批评大型浏览器供应商主导平台的走向。

尽管存在担忧，WHATWG 成员 domenic 感谢作者的工作，并提醒他们相应地更新 dom.spec.whatwg.org。该对话最终因“过于激烈”而被锁定。

---

## 5. 烛焰摆动计时

**原文标题**: Candle Flame Oscillations as a Clock

**原文链接**: [https://cpldcpu.com/2025/08/13/candle-flame-oscillations-as-a-clock/](https://cpldcpu.com/2025/08/13/candle-flame-oscillations-as-a-clock/)

本文探讨了蜡烛火焰振荡这一引人入胜的现象，以及如何将其用作稳定的时间源。文章首先指出，虽然现代蜡烛的设计目的是*不*闪烁，但将三根蜡烛捆绑在一起会产生振荡火焰，其频率出乎意料地稳定，约为9.9赫兹。研究人员发现，该频率主要取决于重力和燃料源的尺寸（蜡烛大小）。

作者详细介绍了两种感知这种振荡的方法：使用光电晶体管检测光线变化，以及更有趣的电容感应。电容法涉及将一根导线悬挂在火焰中，并使用微控制器测量由电离气体引起的电容变化。虽然这种方法比光学感应噪声更大，但证明是可行的。

该项目的核心在于使用电容感应数据来生成1赫兹的时钟信号。这涉及大量的数字信号处理：滤波以消除基线漂移，过零检测以识别振荡峰值，以及使用小数计数器将9.9赫兹的信号降频至1赫兹。然后，作者使用导出的1赫兹信号来闪烁LED，展示了成功创建了一个简陋的“蜡烛时钟”。文章最后指出，该项目是HaD.io“一赫兹挑战赛”的参赛作品，并强调了从故意诱导蜡烛闪烁到将其转换为可用定时信号的整个过程。

---

## 6. 使用谐波驱动和ESP32的定制望远镜支架

**原文标题**: Custom telescope mount using harmonic drives and ESP32

**原文链接**: [https://www.svendewaerhert.com/blog/telescope-mount/](https://www.svendewaerhert.com/blog/telescope-mount/)

Sven De Waerhert记录了他使用谐波驱动器和ESP32微控制器构建定制望远镜赤道仪的旅程。受天体摄影的启发，并对简单跟踪设备的局限性感到沮丧，他开始深入研究DIY赤道仪的构建。

最初，他学习了PCB设计，并用基于ESP32的定制设计取代了恒温器。这项技能使他有勇气去处理更复杂的望远镜赤道仪。他研究了谐波驱动器、步进电机和像SimpleFOC这样的开源FOC实现方案。他使用FreeCAD设计了一个定制外壳，并使用KiCad创建了一个PCB，从第一个版本中与元件替换相关的代价高昂的错误中吸取了教训。

最终设计在RA轴上集成了42AIM15伺服电机，在DEC轴上集成了MKS Servo042D步进电机，两者都与谐波驱动器配对。该赤道仪在GEM和ALTAZ模式下运行，通过USB-C供电，并支持电源传输协商。

他集成了OnStepX固件，通过降低回转速度并将ESP32配置为WiFi客户端，解决了最初的WiFi稳定性问题。制造外包给了JLCPCB，在组装过程中需要进行一些微调。

尽管在极轴对准和软件配置方面存在挑战，但他实现了1-2角秒的验证精度，适用于30秒曝光。整个项目的总成本约为1700欧元，但单个单元的成本可能约为800欧元。De Waerhert强调，获得的经验和构建一个功能性望远镜赤道仪的满足感远远超过了金钱成本。文章最后展示了他使用定制赤道仪拍摄的猎户座星云和M51漩涡星系的惊人照片。

---

## 7. 懒笔 – 用鼠标或手指流畅绘画

**原文标题**: Lazy-brush – smooth drawing with mouse or finger

**原文链接**: [https://lazybrush.dulnan.net](https://lazybrush.dulnan.net)

文章“Lazy-brush – 使用鼠标或手指进行流畅绘画”介绍了一种名为“Lazy Brush”的工具，该工具旨在改善画布上的绘画体验，特别是专注于在使用鼠标或手指绘图时获得更平滑的线条。

它解决的核心问题是直接将鼠标或手指移动转换为数字绘图时，经常产生的抖动和不均匀的线条。Lazy Brush通过引入滞后效应来解决这个问题，即实际绘制位置略微滞后于光标/手指位置。

这种经过精心调整的滞后可以消除用户输入的即时缺陷和颤动，从而产生更干净和更受控制的线条。用户有效地设置了一种“虚拟惯性”，从而降低了对快速、无意移动的敏感性。

本质上，Lazy Brush充当输入的后处理过滤器，在将原始输入数据渲染到画布上之前对其进行平滑处理。这使得即使没有专业的绘图板或手写笔，也能更轻松地创建更具专业外观的绘图。该工具为使用现成的输入设备（如鼠标或触摸屏上的手指）提高绘图质量提供了一种实用的解决方案。

---

## 8. Dnsmasq 关键缓存投毒漏洞

**原文标题**: Critical Cache Poisoning Vulnerability in Dnsmasq

**原文链接**: [https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2025q3/018288.html](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2025q3/018288.html)

Dnsmasq DNS 软件“SHAR攻击”缓存投毒漏洞安全报告（单字符劫持 ASCII 解析器静默）
研究人员苗发盛（清华大学）和李祥（南开大学）发现，Dnsmasq 会将包含特殊字符的 DNS 查询转发到上游解析器。某些上游解析器会静默丢弃这些格式错误的查询，从而产生长时间的攻击窗口。

在此窗口期间，攻击者可以成功地暴力破解 TxID 和源端口，由于生日悖论，显著增加了缓存投毒成功的可能性。该漏洞允许攻击者注入任意恶意 DNS 资源记录，从而有效地对域名进行投毒，无需复杂技术，甚至可以进行异地攻击。

研究人员在所有测试中，通过使用精心设计的字符查询真实域名 (`viticm.com`)，成功地对 Dnsmasq 缓存进行了投毒。 该攻击放大了现有的缓存投毒攻击，如 SADDNS 和 Tudoor，并破坏了解析器静默是无害的假设。

建议的缓解措施包括实施针对静默上游解析器的检测机制，并采用类似于 PowerDNS 中使用的速率限制和欺骗检测技术。 研究人员强调了此问题的紧迫性，因为 Dnsmasq 的部署范围很广，并表示愿意协助进行协同披露和进一步测试。

---

## 9. 正电子：一款新的数据科学 IDE

**原文标题**: Positron, a New Data Science IDE

**原文链接**: [https://posit.co/blog/positron-product-announcement-aug-2025/](https://posit.co/blog/positron-product-announcement-aug-2025/)

Posit PBC发布Positron，一款全新的免费下一代数据科学集成开发环境 (IDE)，旨在统一 Python 和 R 用户探索和生产工作流程。Positron 从 14 年以上的 RStudio 开发经验中汲取灵感，将这两种语言视为平等，并致力于支持现代数据科学工作的整个范围。

主要功能包括：变量和数据框浏览器、多会话控制台、Notebook 支持、GenAI 助手、绘图窗格、集成数据应用程序工作流程、数据库连接窗格、一键式部署、解释器管理、扩展支持和项目文件夹模板。Positron 基于 Code OSS 构建，提供了一个现代且可扩展的编辑器，并具有广泛的 VSIX 扩展支持。

Positron Desktop 目前可在 Windows、macOS 和 Linux 上以 Elastic License 2.0 授权获得。即将发布的 Posit Workbench 也将推出 Positron 会话作为通用 IDE 类型。RStudio 将继续维护和更新。

Positron 旨在为代码编写、分析和数据探索提供有凝聚力且周到的体验，支持迭代开发、丰富的交互式输出和出版质量的文档。Posit 鼓励用户下载 Positron，探索快速入门指南，观看快速导览视频，并在 GitHub 上与社区互动。更多信息将在 posit::conf(2025) 上分享。

---

## 10. Geotoy – 3D几何体的着色器玩具

**原文标题**: Geotoy – Shadertoy for 3D Geometry

**原文链接**: [https://3d.ameo.design/geotoy](https://3d.ameo.design/geotoy)

本文介绍“Geotoy”，它被描述为“用于3D几何体的Shadertoy”。这表明Geotoy是一个类似于Shadertoy的平台或工具，允许用户使用着色器创建和分享基于3D几何体的作品。接下来的大部分内容列出了在Geotoy中创作的各种作品，署名为作者“ameo”（或其变体，如ameoshingles、ameotemple等）。这些作品被呈现为Geotoy功能的示例或演示。列出的示例展示了各种各样的几何形状和结构，从数学上定义的对象，如希尔伯特曲线和环面纽结，到更具机理和细节的场景，如FBM地形、蒲公英，甚至还有特定的引用，如“黑暗之魂树”。重复的作者署名和各种各样的例子突显了Geotoy通过着色器编程生成复杂且有趣的3D几何体的潜力。本质上，Geotoy能够像Shadertoy对2D视觉效果所做的那样，使用代码以程序方式创建3D模型。

---

## 11. 质数网格

**原文标题**: Prime Number Grid

**原文链接**: [https://susam.net/primegrid.html](https://susam.net/primegrid.html)

该网页提供了一个名为“质数网格”的交互式工具。该工具允许用户生成一个可指定行数和列数的网格。生成和显示网格内质数的核心功能依赖于JavaScript。页面提示用户的浏览器必须启用JavaScript才能使网格正常工作。“«”和“»”导航元素可能用于浏览不同的网格或质数页面。“·”和“t”符号的含义尚不明确，但可能控制显示属性或提供有关网格生成过程的额外信息/帮助。本质上，该页面提供了一种使用JavaScript以网格格式动态可视化质数的方法。

---

## 12. 男子地下室发现神秘地下城

**原文标题**: The Mysterious Underground City Found in a Man's Basement

**原文链接**: [https://www.atlasobscura.com/articles/derinkuyu-turkey-underground-city-strange-maps](https://www.atlasobscura.com/articles/derinkuyu-turkey-underground-city-strange-maps)

1963年，土耳其代林库尤一男子在装修地下室时，意外发现一座巨大的多层地下城市。代林库尤位于卡帕多奇亚，该地区以由柔软火山凝灰岩形成的独特“仙人烟囱”景观而闻名，它是该地区数百个地下住所中最大的一个。

这座城市可能可以追溯到公元前2000年，很可能是由赫梯人、弗里吉亚人或早期基督徒建造的，用于躲避入侵者。它可以容纳多达20,000人，并拥有复杂的通风系统，包含超过15,000个竖井，以及用于安全保障的滚动石门。上层用作居住区，而下层用于储存，甚至包括地牢。该城市还包含一个榨酒机、动物庇护所、一座修道院和教堂。

一些竖井也兼作水井，当地人在城市被重新发现之前，甚至在不知情的情况下从中取水。除了避难所，这座城市还提供了稳定适中的温度，使其适合储存收成。在拜占庭人和阿拉伯人之间的冲突、蒙古人的袭击和奥斯曼帝国的统治期间，它曾作为藏身之处。

卡帕多奇亚希腊人居住在代林库尤，直到1923年与希腊进行人口交换，并将他们对这座城市的了解带走。代林库尤现在是一个受欢迎的旅游目的地，希腊人称之为马拉科皮亚（“柔软的地方”），指的是该地区柔软的石头。文章最后开玩笑地暗示，读者可能会在他们地下室墙后找到他们自己未被发现的世界。

---

## 13. PyPI 防止域名复活攻击

**原文标题**: PyPI Preventing Domain Resurrection Attacks

**原文链接**: [https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/](https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/)

PyPI实施新安全措施防范域名复活攻击

PyPI实施了一项新的安全措施，以防止域名复活攻击。这是一种供应链攻击，攻击者通过购买过期域名，并通过密码重置来劫持PyPI账户。PyPI现在使用Domainr (Fastly服务) 定期检查与用户电子邮件地址关联的域名的状态。

如果某个域名进入赎回期（表明可能过期），PyPI将取消验证与该域名关联的电子邮件地址，从而阻止将密码重置请求发送到该地址。这是因为攻击者有可能注册过期的域名并获得对该电子邮件地址的控制权。自2025年6月初以来，PyPI已取消验证了超过1,800个电子邮件地址。

虽然对于2024年1月1日之后有活动记录的账户，强制启用2FA，但这项措施也最大限度地降低了在此日期之前创建的账户的风险。

PyPI建议只有一个来自自定义域的已验证电子邮件地址的用户，添加来自Gmail等常用提供商的第二个已验证电子邮件地址。这提供了一个备用联系点，并有助于账户恢复。他们还建议在使用相同电子邮件地址的其他服务上启用2FA，以防止完全的账户接管。

这种增强措施虽然不是万无一失，但大大降低了通过过期域名接管账户的风险。

---

## 14. OpenMower – 开源割草机

**原文标题**: OpenMower – An open source lawn mower

**原文链接**: [https://github.com/ClemensElflein/OpenMower](https://github.com/ClemensElflein/OpenMower)

OpenMower：旨在打造更智能、更强大的开源割草机器人，超越现有商用产品。该项目利用YardForce Classic 500等廉价割草机的硬件，升级软件以提升功能。目标是打造一款无需边界线、安全、经济、美观、能避开障碍物并对雨水做出反应的自动割草机。

主要功能包括自主割草、安全机制（如紧急停止）、无线运行、避障和雨水检测。该项目正在积极开发中，重点是ROS代码（可在GitHub上获取）。基本的割草功能、地图教学和自动停靠/充电已经实现。

硬件包括主板和电机控制器（xESC mini和实验性的xESC 2040）。软件开发包括割草状态机、路径规划、避障和一个用于可视化的应用程序。

该项目鼓励社区参与，包括构建OpenMower、提供反馈以及在OpenMower网站和Wiki上贡献文档。该项目还寻求识别兼容的割草机型号，但目前只有YardForce Classic 500被确认为兼容型号。

作者还借此项目宣传其在软件工程、嵌入式编程、硬件设计和机器人技术方面的经验，寻求工作机会。

该项目采用Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License（创作共用署名-非商业性使用-相同方式共享 4.0 国际许可协议）进行授权，允许个人和教育用途，但未经许可限制商业销售。免责声明警告用户构建和使用OpenMower可能存在的危险和责任。

---

## 15. Show HN: Chroma Cloud – 面向人工智能的无服务器搜索数据库

**原文标题**: Show HN: Chroma Cloud – serverless search database for AI

**原文链接**: [https://trychroma.com/cloud](https://trychroma.com/cloud)

Chroma Cloud：为AI应用打造的无服务器开源搜索数据库，强调速度、成本效益、可扩展性和可靠性。平台提供向量搜索（基于SPANN和SPFresh）、全文搜索、元数据搜索、集合分叉等功能，并将很快推出摄取和同步功能。

该平台拥有与延迟、QPS、扩展、数据对象存储、操作、可靠性、正常运行时间、支持和安全性相关的性能指标，以及多样化的部署选项。Chroma提供基于使用量的定价和用于管理的仪表板。它可以无缝集成到CI/CD工作流程中，并提供用于开发的CLI。

其核心价值在于能够快速、准确地检索大型数据集，即使数据持续更新也能做到。客户评价强调了延迟的改善和整体搜索功能的提升。一个代码示例展示了如何使用Python中的Chroma Cloud客户端创建数据库并执行向量搜索。该服务提供5美元的免费额度，并鼓励用户开始使用Python、JavaScript和其他语言。

---

## 16. 艾伦·图灵研究所面临身份危机，员工不安

**原文标题**: Staff disquiet as Alan Turing Institute faces identity crisis

**原文链接**: [https://www.theguardian.com/technology/2025/aug/18/shut-it-down-and-start-again-staff-disquiet-as-alan-turing-institute-faces-identity-crisis](https://www.theguardian.com/technology/2025/aug/18/shut-it-down-and-start-again-staff-disquiet-as-alan-turing-institute-faces-identity-crisis)

艾伦·图灵研究所（ATI）是英国顶尖的人工智能研究机构，以著名计算机科学家艾伦·图灵的名字命名。目前，该研究所正面临身份危机和潜在的倒闭风险，原因是面临资金威胁以及政府要求其转向国防和安全领域的工作。员工已向慈善委员会提交举报信，指出对政府可能撤回1亿英镑资金的担忧，并对内部治理、文化和支出监督发出警报。

该研究所正在进行战略改革（图灵2.0），包括裁员和项目关闭，以专注于健康、环境和国防/安全领域。然而，技术大臣彼得·凯尔希望重点放在国防和安全领域，甚至建议进行领导层变动以反映这一点。

员工对领导层和新方向表示不满，担心多样性问题和潜在的失业。一些人担心，对国防和安全的单一关注过于狭隘，会削弱研究所更广泛的社会影响力。另一些人则建议关闭该研究所并重新启动。

虽然ATI领导层承诺在国防和安全方面“加强”，但他们也旨在继续在其他领域开展工作。研究所的未来，以及其维持其原始使命和员工士气的能力，仍然不确定。政府坚称，希望看到纳税人的钱得到价值，它认为最好通过ATI参与国家安全来实现。

---

## 17. Beancount 的 Vim 宏

**原文标题**: Vim Macros for Beancount

**原文链接**: [https://tangled.sh/@adam.tngl.sh/vim-beancounting](https://tangled.sh/@adam.tngl.sh/vim-beancounting)

本文详述了一位用户如何使用Vim宏来调整Beancount（一款基于文本的会计工具）中的内部转账交易。面对包含多账户间转账不完整信息的CSV数据，作者旨在通过匹配不同账户导出的借方和贷方来平衡交易。

作者没有选择脚本或忽略内部转账，而是利用Vim的文本编辑功能手动合并交易。最初的方法包括在Vim中打开多个CSV文件，使用窗口分割，手动在文件之间剪切和粘贴交易，使用诸如`d}`、`C-w`、`P`、`i`和`dd`等基本的Vim移动和命令。这涉及将一个交易条目转换为注释，并将其过账合并到另一个条目中，以在Beancount中实现零和。

作者承认该过程最初效率低下，并引入了诸如`C-e`、`zt`、`zz`和`zb`等Vim命令来改善缓冲区定位和光标对齐，试图将这些命令记忆到肌肉记忆中以便更快地导航。这些命令允许在切换缓冲区和进行快速调整时保持一致的光标视线水平。

主要收获是一个使用Vim进行数据操作的实用例子，特别是在使用Beancount进行财务会计的背景下，并强调通过实际应用逐步提高Vim熟练度的承诺。

---

## 18. 注意力是新的大O：一种基于系统设计的提示工程方法

**原文标题**: Attention Is the New Big-O: A Systems Design Approach to Prompt Engineering

**原文链接**: [https://alexchesser.medium.com/attention-is-the-new-big-o-9c68e1ae9b27](https://alexchesser.medium.com/attention-is-the-new-big-o-9c68e1ae9b27)

本文《注意力是新的大O符号》认为，应该以系统设计的思维方式对待提示工程，重点关注大型语言模型（LLM）如何通过“注意力”机制处理和权衡信息。文章指出，有效构建提示词的结构，而不仅仅是关注特定措辞，会对LLM输出的质量和一致性产生重大影响。

文章解释说，LLM不像人类那样按顺序阅读，而是同时计算所有token之间的关系，因此提示词结构至关重要。一个结构良好的提示词，将任务分解为编号步骤或不同部分，利用了Transformer注意力机制的工作原理，从而创建更清晰的上下文并引导模型的推理。

一个分析代码库架构的生产示例表明，与“次优”提示词相比，“注意力优化”的提示词（包括角色扮演、层级结构、前置约束和明确范围）会产生更好的结果。优化后的提示词也更易于维护，类似于结构良好的代码。

文章随后提供了一些实用启发法：
*   **优先排序：** 将最重要的信息放在最前面。
*   **结构化：** 使用Markdown和清晰的章节将复杂的任务分解为更小、更集中的部分。
*   **角色扮演：** 使用角色扮演来指导风格和推理，但避免将其用于需要事实准确性的任务。
*   **具体性：** 用可衡量的指令代替模糊的指令，以避免注意力漂移。

最后，文章强调，结构良好的提示词可以提高效率，减少浪费的工程师时间（真正的经济杠杆），实现更快的反馈循环，最大限度地利用有效的上下文窗口，并提高系统在不同LLM之间的可移植性。

---

## 19. 阿拉斯加鲑鱼骤减，科学家锁定真凶——科学——美国科学促进会

**原文标题**: As Alaska's salmon plummet, scientists home in on the killer – Science – AAAS

**原文链接**: [https://www.science.org/content/article/alaska-s-salmon-plummet-scientists-home-killer](https://www.science.org/content/article/alaska-s-salmon-plummet-scientists-home-killer)

阿拉斯加鲑鱼数量锐减，多个物种均受影响，引发对该州经济、粮食安全和生态系统健康的担忧。科学家们正在调查导致这场危机的复杂因素，不再局限于过度捕捞等单一原因的解释。

文章强调了人们日益关注的“热挤压”现象，即海洋温度升高与淡水栖息地变化相结合，给鲑鱼的多个生命阶段带来压力。海洋变暖减少了富含营养的浮游生物的供应，这是鲑鱼食物网的基础，影响了生长和存活。与此同时，河流和小溪变暖使得鲑鱼更难有效地产卵和繁殖。

此外，研究人员正在探索因水温升高而改变的捕食者与猎物关系的影响。物种分布的改变使得鲑鱼与它们以前未曾遇到的捕食者接触，可能增加死亡率。来自孵化场养殖的鲑鱼（它们可能更适应温暖的环境）的竞争也被作为一个促成因素进行研究。

这项调查很复杂，需要海洋学家、淡水生态学家和渔业生物学家之间的跨学科合作。科学家们正在使用先进的跟踪技术、海洋模型和遗传分析来了解这些因素之间错综复杂的相互作用，并预测未来鲑鱼种群的趋势。最终，了解“热挤压”及其后果对于制定有效的保护和管理策略以保护阿拉斯加标志性的鲑鱼至关重要。

---

## 20. Sway窗口管理器的Guile绑定

**原文标题**: Guile bindings for Sway window manager

**原文链接**: [https://github.com/ebeem/guile-swayer](https://github.com/ebeem/guile-swayer)

Guile Swayer 提供了一个 Guile 接口来控制 Sway 窗口管理器，解决了缺乏易于编程的自定义接口的问题。 它允许用户完全脚本化和控制 Sway，类似于 X11 中的 StumpWM。 虽然考虑过 Hyprland，但 Sway 的稳定性使其成为首选。

该项目能够查询 Sway 获取信息（工作区、输出），分配执行 Guile 代码的键盘绑定，以及订阅事件以触发操作。 键盘绑定可以是简单的，也可以是复杂的，允许执行 shell 命令或 Sway 特定的操作。 事件订阅允许对工作区切换等更改做出反应。

安装涉及将 guile-swayer 包添加到 Guile 的加载路径。 本文详细介绍了项目结构，包括用于自动重新加载、通用键盘绑定、键盘翻译、类似 which-key 的功能以及工作区管理（网格、组）的模块。

作者的工作流程展示了用于高效导航的工作区网格和跨多个监视器的工作区组，从而在显示器之间同步相关任务。"Which-key" 和 Submaps 帮助以交互方式发现和记住键盘绑定，并将相关命令分组以便于使用。 提及了实验性布局功能以改进窗口排列。

摘要还强调了快速入门说明，并解决了将模块加载到您的加载路径的必要性。

---

## 21. 2006年，日立公司开发出一款0.15毫米大小的RFID芯片。

**原文标题**: In 2006, Hitachi developed a 0.15mm-sized RFID chip

**原文链接**: [https://www.hitachi.com/New/cnews/060206.html](https://www.hitachi.com/New/cnews/060206.html)

2006年2月，日立公司宣布开发出世界最小、最薄的非接触式RFID IC芯片，尺寸为0.15 x 0.15毫米，厚度为7.5微米。这款新芯片是现有“µ-Chip”的微型化版本，保持了相同的功能，但尺寸显著缩小。

实现这种缩小的关键创新是使用绝缘硅(SOI)技术，该技术可在电路元件之间提供绝缘，从而实现更紧密的放置和更高的集成度。与日立公司2003年推出的0.3毫米IC芯片相比，新芯片的表面积为其四分之一，厚度为其八分之一。

这种尺寸的缩小极大地提高了生产力，使得在单个晶圆上可以制造出四倍数量的芯片。与2005年世界博览会上使用的µ-Chip相比，生产力提高了约10倍。

µ-Chip利用2.45 GHz微波外部天线无线传输128位唯一ID。由于数据是使用ROM写入的，因此该芯片具有很高的真实性。原始µ-Chip已在2005年世界博览会上成功使用，门票识别错误率极低。

日立公司预计，这种新型、更小的芯片将扩大非接触式IC芯片的应用范围，包括安全、运输、娱乐、溯源和物流，尤其是在礼品券和证书等领域。其双面电极设计确保了与外部天线的轻松连接，并保持了高生产率。这些进展已于2006年2月在IEEE国际固态电路会议（ISSCC）上进行了展示。

---

## 22. 如何建造一座中世纪城堡

**原文标题**: How to Build a Medieval Castle

**原文链接**: [https://archaeology.org/issues/september-october-2025/features/how-to-build-a-medieval-castle/](https://archaeology.org/issues/september-october-2025/features/how-to-build-a-medieval-castle/)

法国勃艮第的盖德隆城堡是一项实验考古项目，致力于仅使用中世纪的工具、技术和材料建造一座13世纪的城堡。该项目始于1998年，考古学家和熟练的工匠共同合作，旨在了解中世纪的建筑方法。

该项目揭示了先前不为人知的中世纪生活和建筑细节。例如，该团队发现玻璃对于地位较低的贵族家庭来说过于昂贵，促使他们寻找替代的窗户材料。他们尝试了山羊皮，最终确定使用涂有蜂蜡并饰有符合时代特征设计的亚麻布，尽管在寻找将亚麻布固定和保护其免受自然因素影响的理想方法方面仍然存在挑战。

城堡的建造还带来了其他发现，例如受到腓力宾时代城堡启发的有效石材切割技术、陶瓷瓦混合方法、石灰砂浆的应用以及脚手架的搭建。该项目利用当地资源，包括橡木木材、砂岩和颜料。

该项目雇用了大约40名工匠，每年吸引超过30万游客，并通过门票销售和现场设施自筹资金。通过应对现实世界的建筑挑战，该团队深入了解了13世纪劳动者的日常生活和解决问题的方法。目前的目标之一是完成门楼的建造，这涉及到对吊闸机构如何运作的推测。这座城堡更多地被视为权力的象征，而不是防御性建筑。

---

## 23. EloqKV，一个兼容 Redis API 的分布式数据库 (GPLv2 和 AGPLv3 许可)

**原文标题**: EloqKV, a distributed database with Redis compatible API (GPLv2 and AGPLv3)

**原文链接**: [https://github.com/eloqdata/eloqkv](https://github.com/eloqdata/eloqkv)

EloqKV是一款高性能、分布式键值数据库，具有Redis/ValKey兼容的API，专为现代、高要求的应用而设计，尤其是在人工智能时代。它以提供ACID事务、完全的弹性和可扩展性、分层存储以及会话式事务语法（同时保持Redis的简洁性）而著称。

主要特性包括：

*   **高性能：** 多线程架构，在单节点上可实现高达160万QPS。
*   **具有分层存储的完全持久性：** 复制的WAL和自动数据分层到磁盘，可降低高达70%的内存成本。
*   **ACID事务：** 会话式语法（BEGIN/COMMIT/ROLLBACK），与Redis的MULTI/EXEC相比，提供更强大的事务支持。
*   **分布式ACID事务：** 无需哈希槽限制的跨节点一致性。
*   **Redis API兼容性：** 可与现有的Redis客户端开箱即用。

EloqKV的架构使用Data Substrate，将Redis协议兼容的前端与用于数据操作的TxService、用于WAL的LogService以及用于内存状态和冷数据存储的Storage Service分离。 基准测试表明，EloqKV在缓存模式下优于Redis和ValKey，并且在持久事务模式下，性能优于其他Redis兼容存储，如Apache KVRocks。

EloqKV提供了多种入门方式，包括Docker、EloqCtl（集群管理工具）或用于本地设置的tarball。它采用GPLv2和AGPLv3双重许可。

---

## 24. 章鱼城与章鱼亚特兰蒂斯

**原文标题**: Octopolis and Octlantis

**原文链接**: [https://en.wikipedia.org/wiki/Octopolis_and_Octlantis](https://en.wikipedia.org/wiki/Octopolis_and_Octlantis)

章鱼城和章鱼洲：澳大利亚新南威尔士州杰维斯湾阴暗章鱼的两处聚居地。章鱼城发现于2009年，特征是排列成椭圆形的贝壳堆以及一块废金属。章鱼会钻入贝壳堆建造巢穴，相比周围的沉积物，贝壳是更优良的建筑材料。曾同时观察到多达14只章鱼栖息在章鱼城。

2016年，在附近发现了第二处聚居地，章鱼洲。与章鱼城不同，章鱼洲不包含任何人造物品。这两处地点都位于布德里国家公园内，并且可以容纳数量相近的章鱼。

虽然一些媒体将这些聚居地称为“章鱼城市”，但参与研究的科研人员认为这种类比具有误导性。这些地点为了解*Octopus tetricus*的社会行为和栖息地偏好提供了线索。

---

## 25. Show HN: Whispering – 可信任的开源本地优先语音听写工具

**原文标题**: Show HN: Whispering – Open-source, local-first dictation you can trust

**原文链接**: [https://github.com/epicenter-so/epicenter/tree/main/apps/whispering](https://github.com/epicenter-so/epicenter/tree/main/apps/whispering)

“展示HN：Whispering – 你可以信任的开源、本地优先的听写工具”帖子介绍了“Whispering”，一个通过本地运行来优先保护用户隐私的开源听写工具。其核心卖点是信任：由于语音转文本的处理直接在用户机器上进行，因此无需担心敏感音频数据被发送到第三方服务器。

该帖子托管在GitHub的“epicenter-so/epicenter”仓库下。虽然显示“Uh oh! There was an error while loading”，暗示显示完整细节时出现问题，但用户参与度指标可见：该项目有126个fork和2,000个star，表明了相当大的兴趣和潜在的社区采用率。

本质上，该帖子宣布了一个以隐私为中心的听写解决方案，采用本地优先设计，吸引了开源社区的广泛关注。加载页面时出现的错误限制了全面理解，但该项目的名称（“Whispering”）及其描述强烈暗示了对安全和私密语音输入的关注。

---

## 26. 特德·姜：第三种东西

**原文标题**: Ted Chiang: The Secret Third Thing

**原文链接**: [https://linch.substack.com/p/ted-chiang-review](https://linch.substack.com/p/ted-chiang-review)

无法访问文章链接。

---

## 27. 反恐精英：从宿舍走出的十亿美元游戏

**原文标题**: Counter-Strike: A billion-dollar game built in a dorm room

**原文链接**: [https://www.nytimes.com/2025/08/18/arts/counter-strike-half-life-minh-le.html](https://www.nytimes.com/2025/08/18/arts/counter-strike-half-life-minh-le.html)

无法访问文章链接。

---

## 28. Netflix用原始空心内存对象存储重构Tudum的CQRS架构

**原文标题**: Netflix Revamps Tudum's CQRS Architecture with Raw Hollow In-Memory Object Store

**原文链接**: [https://www.infoq.com/news/2025/08/netflix-tudum-cqrs-raw-hollow/](https://www.infoq.com/news/2025/08/netflix-tudum-cqrs-raw-hollow/)

Netflix改造了其Tudum粉丝网站的架构，用内部开发的内存对象存储RAW Hollow取代了使用Kafka和Cassandra的CQRS实现。 原本的架构虽然实现了读写路径的独立扩展，但由于缓存刷新周期导致内容更新传播缓慢，使得内容预览延迟，并且随着内容量的增长而加剧。

RAW Hollow专为具有强读后写一致性的中小型数据集而设计，允许整个数据集驻留在每个应用程序进程的内存中，从而提供低延迟和高可用性。 团队认为，对于Tudum的特定需求，CQRS模式并非最佳选择。

新的架构消除了缓存失效问题，因为整个数据集都适合内存。 Hollow的数据压缩进一步促进了这一点，显著减小了数据大小。 这减少了I/O和往返时间，从而加快了数据传播和页面构建，使内容编辑者（更快的预览）和网站访问者（更快的页面渲染）都受益。

---

## 29. Tiny-tpu：一个受谷歌TPU启发的极简张量处理器 (TPU)

**原文标题**: Tiny-tpu: A minimal tensor processing unit (TPU), inspired by Google's TPU

**原文链接**: [https://github.com/tiny-tpu-v2/tiny-tpu](https://github.com/tiny-tpu-v2/tiny-tpu)

Tiny-TPU是一个开源项目，旨在创建一个受谷歌TPU启发的极简张量处理单元（TPU）。其目标是为所有技能水平的个人提供一个易于访问的资源，以学习和贡献于硬件加速器设计。

Tiny-TPU架构包含几个关键组件：以脉动阵列排列的用于高效矩阵乘法的处理单元（PE），用于后处理操作（如偏差加法和激活函数）的向量处理单元（VPU），用于存储中间数据的统一缓冲区（UB），以及解释94位指令集的控制单元。

脉动阵列利用PE网格，其中输入数据水平流动，部分和垂直流动，权重保持在每个PE内固定。VPU在脉动阵列之后执行逐元素操作，提供用于偏差加法、Leaky ReLU激活、MSE损失计算和Leaky ReLU导数计算的模块。UB存储输入矩阵、权重矩阵、偏差向量和其他相关数据。

该项目包含关于设置开发环境（MacOS和Ubuntu）、添加新模块、运行测试以及使用GTKWave查看波形的说明。文档还详细介绍了指令集架构（ISA），提供了每个位字段及其对应功能的描述。

该项目的动机是揭开芯片加速器设计的神秘面纱，使其对初学者来说易于理解，并培养一种创新的思维模式。未来的步骤包括开发指令集的编译器以及将TPU扩展到更大的尺寸。

---

## 30. 展示一下：我做了个屏蔽短视频和Reels的应用

**原文标题**: Show HN: I built an app to block Shorts and Reels

**原文链接**: [https://scrollguard.app/](https://scrollguard.app/)

ScrollGuard：阻止 Reels 和 Shorts，助您摆脱沉迷式浏览习惯。

ScrollGuard 是一款旨在帮助用户对抗沉迷式浏览习惯的新应用，它能屏蔽 Instagram、Facebook、Reddit 和 YouTube 等热门平台上的 Reels 和 Shorts 短视频。它还提供“反沉迷模式”，可对任何应用设置浏览限制。

该应用承诺通过消除广告、Reels、Shorts 和其他令人上瘾的内容，提供一个无干扰的体验。目前该应用已在 Android 平台上线，开发者也在努力开发 iOS 版本。

由于 iOS 版本面临技术限制，无法像 Android 版本那样直接屏蔽 Reels 和 Shorts 短视频。因此，开发者正在探索其他方法来减少 iPhone 用户的浏览成瘾。有兴趣的 iOS 用户可以加入等候名单，以便在 iPhone 应用发布时收到通知。

---

## 31. X光扫描揭示微型藏族卷轴内的佛教经文

**原文标题**: X-ray scans reveal Buddhist prayers inside tiny Tibetan scrolls

**原文链接**: [https://www.popsci.com/technology/tibetan-prayer-scroll-scans/](https://www.popsci.com/technology/tibetan-prayer-scroll-scans/)

德国亥姆霍兹柏林中心的研究人员使用3D X射线断层扫描和人工智能技术，在不对蒙古出土的脆弱古代佛教卷轴（陀罗尼）造成物理损伤的情况下，对其进行虚拟“展开”。这些卷轴包含祈祷文，是蒙古游牧家庭拥有的便携式佛龛（gungervaa）的一部分，在1921年的蒙古革命期间几乎被摧毁殆尽。

自1932年以来，这些卷轴一直保存在德国民族学博物馆，并使用同步加速器断层扫描技术进行扫描，该技术可以编译物体在微观层面的3D表示。由于设备的视场有限，该过程涉及将物体成像为一系列“子体积”。

扫描显示，每个卷轴都包含一条约31.5英寸长的羊皮纸，包裹了大约50圈。对墨水的AI分析揭示了意想不到的金属颗粒的存在。此外，一段文字被确认为藏传佛教真言“唵嘛呢叭咪吽”，是用梵文语法而不是藏文书写的。

该研究的作者承认，X射线断层扫描目前仍需投入大量人力，但他们认为它为检查无法接近的文物提供了独特的机会。他们希望这项技术的进步能够促成更多协作性的跨学科保护项目，从而更深入地了解这些历史文物。

---

## 32. 从左到右编程

**原文标题**: Left to Right Programming

**原文链接**: [https://graic.net/p/left-to-right-programming](https://graic.net/p/left-to-right-programming)

本文提倡“从左到右编程”这种范式，即代码在编写过程中就有效且易于理解，从而实现更好的编辑器支持和更直观的开发体验。作者批评了Python的列表推导式和C的基于函数的结构体方法，认为它们不易被发现，并且在输入时难以解析。这些模式迫使程序员预先知道理想情况下应该在编码过程中发现的信息。

作者赞扬了Rust和JavaScript的更链式和面向对象的方法，其中方法直接与对象关联，从而可以通过编辑器自动完成轻松发现它们。这符合渐进式披露的原则，只在相关时才呈现复杂性。

本文认为，语言应促进可以从左到右阅读和理解的代码，从而提高可读性并减少认知负荷，尤其是在复杂的逻辑中。作者通过示例展示了这种“即写即有效”的方法如何实现更好的编辑器辅助、更快的学习速度，并最终带来更高效和愉悦的编码体验，从而引导至“成功之坑”。他们强调了可发现API的重要性，这些API可以在开发者编写代码时引导他们找到正确的函数和方法。

---

## 33. 伦敦水晶宫的生与死 (2021)

**原文标题**: The Life and Death of London's Crystal Palace (2021)

**原文链接**: [https://heritagecalling.com/2021/11/29/picturing-the-crystal-palace/](https://heritagecalling.com/2021/11/29/picturing-the-crystal-palace/)

英格兰遗产委员会：伦敦水晶宫的生与死——聚焦摄影史

---

## 34. Show HN: Python 文件流传输速度达 237MB/s，在 $8/月的服务器上仅用 507 行标准库代码实现

**原文标题**: Show HN: Python file streaming 237MB/s on $8/M droplet in 507 lines of stdlib

**原文链接**: [https://bellone.com/updates/axon-api/python-file-streaming-237mbs-on-$8-m-droplet-in-507-lines-stdlib](https://bellone.com/updates/axon-api/python-file-streaming-237mbs-on-$8-m-droplet-in-507-lines-stdlib)

这个“Show HN”帖子介绍 Axon API，一个开源 Python WSGI 核心，专为需要对请求生命周期进行精细控制的应用进行快速原型设计而生。Axon 由 507 行标准库代码（Python 3.10+）编写，在低成本的 8 美元/月 Digital Ocean droplet 上实现了高达 237MB/s 的文件流传输性能。

Axon 利用多部分流传输，通过单个 HTTP 连接，使用 Python 生成器和 64KB 的块返回多个文件，以实现最佳吞吐量。一个关键的架构特性是其背压处理，通过仅在客户端需要时才“存储”块来防止内存累积。这使得即使在高负载下也能保持恒定的内存使用。

在 NYC3 的 Digital Ocean droplet 上进行的性能测试包括部署新的 Axon 实例，并使用 `wrk` 进行压力测试，采用 50 个并发连接。测试涵盖了各种有效负载大小（8KB-512KB）和单/多文件场景。结果表明，CPU 饱和是单核硬件上的主要瓶颈，而网络吞吐量成为多核部署中的限制因素。Axon 在所有测试中都保持零套接字错误。性能随计算资源扩展，表明这是一种适用于专门针对节点类型和大小的分布式策略的架构。

---

## 35. 黑曜石基地

**原文标题**: Obsidian Bases

**原文链接**: [https://help.obsidian.md/bases](https://help.obsidian.md/bases)

Obsidian帮助文章《基础概念入门》阐述了Obsidian中“基础”的概念，即作为构建和连接信息的基本组织结构或核心笔记类型。它强调这些基础并非僵化的模板，而是针对不同类型的笔记和工作流程的可调整的起点。

其核心思想是识别你的思考和信息管理中反复出现的模式。通过识别这些模式，你可以创建基础笔记来捕捉每种类型的基本要素和属性。这有助于提高笔记的一致性和效率。

文章强调了基础的灵活性。它们可以是简单的清单，也可以是复杂的项目管理系统。文章鼓励用户根据自己的理解和需求不断尝试和改进基础。目标不是将信息强行塞入预定义的结构中，而是利用一个灵活的框架来支持自然的思考和知识连接。

此外，文章还隐晦地表明，使用基础可以增强Obsidian的链接功能。通过建立一致的笔记结构，更容易识别不同笔记之间的关系，从而构建一个更互联和可导航的知识库。最终，基础被呈现为在Obsidian中创建一个更具组织性、效率和洞察力的笔记系统的工具。

---

## 36. Spice Data (YC S19) 招聘产品助理（应届生）

**原文标题**: Spice Data (YC S19) Is Hiring a Product Associate (New Grad)

**原文链接**: [https://www.ycombinator.com/companies/spice-data/jobs/RJz1peY-product-associate-new-grad](https://www.ycombinator.com/companies/spice-data/jobs/RJz1peY-product-associate-new-grad)

Spice Data（YC S19公司，专注于为企业提供餐饮数据）正在旧金山招聘产品助理（应届毕业生）。该职位涉及清洗、标准化和转换原始数据，识别不良数据，管理第三方承包商，向客户交付数据，并与工程团队协作以改进数据管道。该职位要求每周在旧金山市中心办公室工作4天。

理想的候选人应具有管理咨询、投资银行或早期B2B创业公司的实习经验，以及强大的Excel和数据分析技能，以及出色的沟通能力。

该职位提供 80,000-100,000 美元的薪水、0.1-0.5% 的股权、无限 PTO、401k 以及全面的健康、牙科和视力保险。在办公室工作时提供午餐。

面试流程包括介绍电话、两次侧重于数据清洗和问题解决的面试，以及一次现场访问。

Spice Data 成立于 2019 年，盈利，总部位于旧金山，拥有一支小型团队，并得到 YC 和天使投资者的支持。他们专注于为财富 500 强公司提供高质量的数据，尤其是在餐饮行业。

---

## 37. FFmpeg汇编语言教程

**原文标题**: FFmpeg Assembly Language Lessons

**原文链接**: [https://github.com/FFmpeg/asm-lessons](https://github.com/FFmpeg/asm-lessons)

本文介绍“FFmpeg汇编语言学校”，该资源旨在教授用户在FFmpeg开发环境中使用的汇编语言。它强调学习汇编语言的难度和回报，并旨在为理解计算机底层运行原理奠定基础。

这些课程旨在使学习者掌握最终为FFmpeg项目做出贡献的技能。为了充分利用这些材料，建议具备C语言（特别是指针）和高中水平数学的先验知识。课程和相应的作业将在Git仓库中提供。

我们提供了一个Discord服务器，供学习者提问和获得支持。这些课程还将翻译成法语和西班牙语。

---

## 38. 石墨聊天

**原文标题**: Graphite Chat

**原文链接**: [https://graphite.dev/blog/introducing-graphite-chat](https://graphite.dev/blog/introducing-graphite-chat)

Graphite Chat 推出全新方式，利用人工智能直接在 Pull Request 中审查和改进代码。Graphite Chat 建立在其现有的人工智能代码审查代理 Diamond 之上，使开发者能够与人工智能对话，了解代码更改、获取建议并应用修复，而无需切换标签页。

主要优势包括：

*   **轻松理解差异：** Chat 提供来自完整代码库和 PR 历史的上下文，回答有关特定代码段的问题。
*   **定制化建议：** 人工智能针对测试、重构和模式匹配提供符合代码风格的建议。
*   **快速变更：** 集成 IDE 允许对建议的更改进行上下文审查，从而能够在 PR 中直接添加行、运行测试和提交。
*   **简化合并：** 在不离开 PR 窗口的情况下合并编辑并进行合并。

Graphite Chat 专为代码审查员和作者设计。审查员可以快速理解不熟悉的逻辑或评估代码质量，而作者可以在人工审查之前主动识别改进并修复问题。它将来自代码库、CI 管道和 Web 的信息整合到一个对话界面中。

Graphite Chat 目前处于 Beta 版，对所有 Graphite 用户免费。它旨在通过提高效率和集成度来彻底改变代码审查，从而加速软件开发生命周期。

---

## 39. Show HN：我们开始做AI开发工具，结果变成了模拟人生风格的游戏

**原文标题**: Show HN: We started building an AI dev tool but it turned into a Sims-style game

**原文链接**: [https://www.youtube.com/watch?v=sRPnX_f2V_c](https://www.youtube.com/watch?v=sRPnX_f2V_c)

这篇“Show HN”帖子声称一个AI开发工具项目意外演变成了模拟人生风格的游戏。然而，提供的内容仅为YouTube的标准页脚信息，包含版权、服务条款、隐私和服务详情。没有关于AI开发工具、模拟人生风格游戏或项目演变的实际描述。因此，基于所提供的内容，除了确认标题的说法之外，不可能进行有意义的总结。核心信息仅在于标题：一个团队开始构建AI开发工具，但它演变成了一个类似于《模拟人生》的游戏。

---

## 40. 如何使用 Snprintf

**原文标题**: How to Use Snprintf

**原文链接**: [https://bernsteinbear.com/blog/snprintf/](https://bernsteinbear.com/blog/snprintf/)

Max Bernstein 的这篇文章讨论了 `sprintf` 函数族，特别是 `snprintf` 的一个实用特性，该特性允许动态确定所需的缓冲区大小。其关键在于，你可以使用 `NULL` 缓冲区和大小 `0` 调用 `snprintf`，以获取 *将会* 写入的字符数（不包括空终止符）。

作者首先通过调用 `snprintf(NULL, 0, format_string, ...)` 来获取所需的大小。然后，他们使用 `malloc` 为缓冲区分配内存，并为 null 终止符添加 1。最后，他们再次调用 `snprintf`，这次使用分配的缓冲区和计算的大小，来实际格式化字符串。文章强调了这种方法，以避免手动缓冲区大小计算并防止潜在的缓冲区溢出。它还提到了作者为此目的编写的一个小型、仅包含头文件的库，但未提供详细信息。核心信息是利用 `snprintf` 的预计算所需缓冲区大小的能力，来实现更安全、更高效的字符串格式化。

---

## 41. “大教堂搬迁”：瑞典小镇开始滚动搬运历史建筑5公里

**原文标题**: The 'big church move': Swedish town begins to roll historic building 5km

**原文链接**: [https://www.theguardian.com/world/2025/aug/19/the-big-church-move-sweden-kiruna-kyrka](https://www.theguardian.com/world/2025/aug/19/the-big-church-move-sweden-kiruna-kyrka)

为配合欧洲最大地下矿的扩张，瑞典基律纳镇已开始将其历史悠久的基律纳教堂搬迁5公里。这座矿由国有的LKAB公司运营。此次搬迁耗资超过3900万英镑，是由于矿区导致地面软化而进行的整个城镇搬迁计划的一部分。这座于1912年落成、形似萨米小屋的教堂，正以每小时半公里的速度，耗时两天进行搬迁。这一事件吸引了大量人群，并在瑞典电视台进行现场直播。在新址计划举行庆祝活动，包括教堂礼拜和音乐娱乐。

虽然LKAB将此次搬迁描述为独特的历史事件，但它也面临批评，特别是来自萨米社区的批评。他们担心矿区的扩张会分割他们的土地，使驯鹿放牧变得困难，并威胁到他们的土著文化。一位萨米代表指责LKAB“掠夺土地”，并利用教堂搬迁来转移人们对采矿活动造成的环境和文化破坏的注意力。LKAB为搬迁辩护，称没有教堂，基律纳市中心是不可想象的，而且搬迁对于矿区的持续运营至关重要。教堂预计将于明年在新址重新开放，但整个城镇的搬迁要到2035年才能完成。

---

## 42. 拯救PBS和NPR电台的竞赛

**原文标题**: The Race to Rescue PBS and NPR Stations

**原文链接**: [https://www.nytimes.com/2025/08/19/business/the-race-to-rescue-pbs-and-npr-stations.html](https://www.nytimes.com/2025/08/19/business/the-race-to-rescue-pbs-and-npr-stations.html)

无法访问文章链接。

---

## 43. 研发回报率上升： 创意并非越来越难寻

**原文标题**: The rising returns to R&D: Ideas are not getting harder to find

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5242171](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5242171)

无法访问文章链接。

---

## 44. 安娜的档案：团队最新进展

**原文标题**: Anna's Archive: An Update from the Team

**原文链接**: [https://annas-archive.org/blog/an-update-from-the-team.html](https://annas-archive.org/blog/an-update-from-the-team.html)

无法访问文章链接。

---

## 45. 英国放弃要求苹果加密留后门

**原文标题**: UK drops demand for backdoor into Apple encryption

**原文链接**: [https://www.theverge.com/news/761240/uk-apple-us-encryption-back-door-demands-dropped](https://www.theverge.com/news/761240/uk-apple-us-encryption-back-door-demands-dropped)

据报道，英国已放弃要求苹果公司提供访问加密iCloud用户数据的后门，此举可能为苹果公司在英国重新推出其高级数据保护(ADP)加密iCloud存储铺平道路。此前，美国国家情报总监图尔西·加巴德带头施压美国，表达了对保护美国公民隐私和公民自由的担忧，因为英国的命令将影响包括美国人在内的全球用户的加密数据。

今年1月，英国发布了一项秘密命令，要求获得后门访问权限，促使苹果公司阻止新的英国用户注册ADP。苹果公司对该命令提出质疑，并在4月份赢得了公开讨论此案的权利。美国官员也开始调查英国的命令是否违反了双边CLOUD Act协议，该协议禁止美国和英国要求对方提供数据。

上个月的报道显示，由于压力和可能违反CLOUD Act，英国正在考虑撤回相关要求。尽管与苹果公司重新谈判条款以避免牵连美国公民的可能性仍然存在，但有迹象表明，任何此类谈判都将与新协议相悖。目前尚不清楚苹果公司是否将在英国恢复ADP服务。苹果公司已被联系以征求意见，英国内政部拒绝置评。

---

## 46. 基于IRC的割草机 (2021)

**原文标题**: An IRC-Enabled Lawn Mower (2021)

**原文链接**: [https://jotunheimr.idlerpg.net/users/jotun/lawnmower/](https://jotunheimr.idlerpg.net/users/jotun/lawnmower/)

2020年，作者“jotun”在IRC上被朋友Empus和Ragnar戏称为要从割草机上连接一个IRC服务器。这最初只是一个玩笑，后来演变成了一个真正的硬件项目。软件工程师“jotun”的硬件经验有限，但他开始着手打造一台支持IRC的割草机，昵称为“lawnmower.*”。

该项目涉及订购一块Raspberry Pi 4b+、一个小OLED显示屏和一个用于电池供电的UPS HAT。他编写了定制的监控软件，用于在OLED屏幕上显示系统信息、WiFi信号强度、电池电量和IRC用户数。他优化了代码以最大限度地减少CPU使用率，并解决了低效显示驱动程序的问题。他还对Pi的IRC服务器(ircu)进行了负载测试，发现它能够处理数千个用户。

硬件被安置在一个电气项目盒中，并用支架安装。钻孔用于安装散热风扇和一个按钮。他面临着诸多挑战，例如安装UPS HAT、安全地为电源线切出一个孔，以及潜在的电池过热。他还因塑料粉尘导致了眼睛受伤。

他花费了大量精力来解决将服务器上线时暴露其家庭IP地址的问题，在找到使用GRE隧道更好的解决方案之前，他尝试了SSH隧道和WebIRC过滤器。

---

## 47. 克罗地亚自由潜水员憋气29分钟

**原文标题**: Croatian freediver held breath for 29 minutes

**原文链接**: [https://divernet.com/scuba-news/freediving/how-croatian-freediver-held-breath-for-29-minutes/](https://divernet.com/scuba-news/freediving/how-croatian-freediver-held-breath-for-29-minutes/)

克罗地亚自由潜水员维托米尔·马里奇奇创下新的吉尼斯世界纪录，凭借氧气辅助水下闭气时长达到惊人的29分3秒。这比之前的纪录多了四分钟以上。这一壮举发生在克罗地亚奥帕蒂亚一个3米深的泳池中，有官方裁判和观众见证。

马里奇奇通过预先呼吸纯氧进行准备，这项技术可以增加肺部可用的氧气。然后，他仰卧在水下，专注于精神控制，尽管身体感到不适，尤其是膈肌收缩。他将创纪录的功劳归于他的团队、家人和朋友的支持。

之前的纪录由他的克罗地亚同胞布迪米尔·绍巴特保持，为24分37秒。值得注意的是，魔术师大卫·布莱恩曾以17分4秒保持该记录。相比之下，AIDA静态闭气（空气闭气）的世界纪录为11分35秒。

马里奇奇的背景包括AIDA静态闭气10分8秒的个人最佳成绩，他还保持着一项吉尼斯世界纪录，即一次呼吸水下行走的最长距离。文章强调了长时间闭气的生理和心理需求，强调了膈肌呼吸、放松和精神控制的重要性。预先呼吸氧气是为了用氧气代替肺中的氮气，从而增加可用的氧气。

---

## 48. 树莓派 Pico 用的 Intel 80286 模拟器

**原文标题**: Intel 80286 emulator for Raspberry Pico

**原文链接**: [https://github.com/xrip/pico-286](https://github.com/xrip/pico-286)

Pico-286项目旨在树莓派Pico (RP2040/RP2350)上模拟经典PC (8086/8088/80186/286 CPU)，提供轻量级的教育性复古计算体验。它支持跨平台构建（Pico, Windows, Linux），并模拟各种复古外围设备、图形模式（CGA, HGC, TGA, VGA, 文本）和声音（PC扬声器, Covox, Disney Sound Source, Adlib/Sound Blaster, MPU-401, Tandy 3音色, Creative Music System）。

存储选项包括SD卡上的虚拟磁盘镜像（软盘和硬盘）以及通过映射网络驱动器(H:)直接访问主机文件系统。MAPDRIVE.COM实用程序启用主机驱动器。

硬件配置需要一个树莓派Pico和PSRAM（建议8MB以上）。最佳性能使用带有QSPI PSRAM的树莓派Pico 2 (RP2350)。提供了用于VGA/HDMI, TFT显示器, SD卡, PSRAM, NES游戏手柄和音频等外围设备的默认引脚排列。

内存管理利用传统RAM（主机上640KB，Pico上较少），并通过PSRAM（高性能）或虚拟内存（SD卡交换文件，较慢）扩展内存。该架构利用Pico的双核处理器（核心0用于CPU和输入，核心1用于视频、音频和定时器中断）。Windows和Linux版本是多线程的。

构建需要适当的工具链（Pico SDK, CMake, ARM GCC, MSVC/GCC或GCC/Clang），并在CMake配置期间选择显示（TFT, VGA, HDMI）和音频（I2S, PWM, 硬件）选项。 提供了RP2350, RP2040和Linux主机的特定构建命令。

---

## 49. 发布HN：Reality Defender (YC W22) – 用于深度伪造和生成式人工智能检测的API

**原文标题**: Launch HN: Reality Defender (YC W22) – API for Deepfake and GenAI Detection

**原文链接**: [https://www.realitydefender.com/platform/api](https://www.realitydefender.com/platform/api)

Reality Defender，一家 Y Combinator 2022 冬季校友公司，于 2025 年 7 月 31 日推出了免费访问的 API，用于深度伪造和 GenAI 检测。该 API 允许用户分析内容并确定其被合成生成或篡改的可能性，从而帮助对抗虚假和错误信息的传播。该举措突显了 Reality Defender 致力于使深度伪造检测更易于访问和广泛应用的承诺，有可能使个人和组织能够验证媒体内容的真实性。此次发布标志着在应对人工智能生成内容日益增长的挑战方面迈出了重要一步。

---

## 50. Newgrounds：闪回2025

**原文标题**: Newgrounds: Flash Forward 2025

**原文链接**: [https://www.newgrounds.com/bbs/topic/1542140](https://www.newgrounds.com/bbs/topic/1542140)

Newgrounds论坛帖宣布“Flash Forward Jam 2025”，第五届年度活动，庆祝Flash动画和游戏在Flash永不消逝的平行宇宙中的发展。鼓励参与者使用Flash制作游戏和互动电影，确保与Ruffle（Newgrounds使用的Flash模拟器）兼容。活动强调首发新作，不鼓励重新发布之前的项目。

重要日期包括：4月6日（NG 25周年Flash Portal纪念日）以及4月20日发布的、带有“Flash-Forward-2025”标签作品的截止日期。

游戏和互动电影均有奖项，游戏奖金明显高于电影奖金（一等奖分别为1200美元和150美元）。该帖子重点介绍了增加奖金的众筹活动，并列出了目前的赞助商。

一项重大更新是推出了新的Newgrounds.io ActionScript 2.0库，旨在取代旧的Flash API，并实现访问奖牌、高分和分享等功能。提供学习Flash的资源，包括教程和往届Flash Forward作品存档。

该帖子还提到了其他即将到来的Newgrounds活动，包括7月6日网站30周年庆典，其中包含各种合作项目。后续评论显示了对该活动的热情，用户讨论了技术方面（如AS3兼容性和Flash CS6安装）、提供合作并表达了对Flash复兴的支持。

---

## 51. 日产公布2026款聆风定价，300英里续航，起价29,990美元

**原文标题**: Nissan announces 2026 Leaf pricing, 300 mile range starting at $29,990

**原文链接**: [https://arstechnica.com/cars/2025/08/nissan-announces-2026-leaf-pricing-starting-at-29990/](https://arstechnica.com/cars/2025/08/nissan-announces-2026-leaf-pricing-starting-at-29990/)

日产发布2026款聆风定价及配置，第三代电动汽车。基本款Leaf S+起价29,990美元，配备75千瓦时液冷电池，续航里程达303英里。该价格甚至低于2011年初代聆风的原始价格，且未考虑通货膨胀因素。

日产表示，其目标是提供物有所值的平价电动汽车。Leaf SV+售价34,230美元，配备更大尺寸的轮毂、改进的信息娱乐系统和可选的电池加热器，续航里程为288英里，较2025款车型有显著提升。

顶配Platinum+版车型与S+和SV+共享相同的动力系统，但配备更多标准配置，起价38,990美元。

预计稍后将推出价格更低的“S”版车型，配备较小的52千瓦时电池，预计售价低于30,000美元。尽管面临关税挑战，日产仍致力于为这款入门级车型设定极具竞争力的价格。

总而言之，2026款聆风承诺更高的效率、液冷电池以及极具竞争力的各款车型定价，使其成为电动汽车市场中颇具吸引力的选择。

---

## 52. 展示一下：我构建了一个玩具 TPU，可以对 XOR 问题进行推理和训练

**原文标题**: Show HN: I built a toy TPU that can do inference and training on the XOR problem

**原文链接**: [https://www.tinytpu.com](https://www.tinytpu.com)

这个“Show HN”帖子详细介绍了为XOR问题设计用于推理和训练的“玩具TPU”的创建过程。作者是一群硬件设计新手，旨在通过从零开始重新发明一个TPU来理解TPU的工作原理，强调“hacky”方法，并避免依赖AI编码辅助。

文章解释说，TPU是一种专门为机器学习任务（如矩阵乘法）优化的专用集成电路（ASIC），这对于神经网络中的训练和推理至关重要。他们的玩具TPU利用了包含执行乘法累加运算的PE（处理单元）的脉动阵列。他们通过专注于XOR（一个经典的神经网络挑战）简化了问题，使用了一个2->2->1多层感知器（MLP）。

作者介绍了使用脉动阵列在硬件中实现矩阵乘法的过程，包括必要的数据交错和转置技术。他们还详细介绍了偏置加法和Leaky ReLU激活函数的实现。该帖子使用示例权重、偏置和XOR输入矩阵来说明数据如何在脉动阵列中流动并在每一层中被处理。他们使用Verilog展示了玩具TPU主要部分的代码。其目标不是真实TPU的1对1复制品，而是对其核心原理的实际探索，从而产生一个能够解决XOR问题的功能加速器。

---

## 53. 类型检查器动物园

**原文标题**: Typechecker Zoo

**原文链接**: [https://sdiehl.github.io/typechecker-zoo/](https://sdiehl.github.io/typechecker-zoo/)

本文介绍了“Typechecker Zoo”，一个旨在用 Rust 实现具有影响力的静态类型系统的最小版本的个人项目。该项目旨在提供对类型检查算法和语言设计演进的实践理解，涵盖从较简单的系统到现代依赖类型。

与 TAPL 和 ATTAPL 等教科书相比，该项目更注重实际实现细节，而非严格的理论证明，从而提供更容易理解的学习体验。重点在于数据结构、逻辑和抽象语法树的“血淋淋的细节”。

该项目包括以下实现：

*   **Algorithm W:** 用于多态 Lambda 演算的经典 Hindley-Milner 类型推断。
*   **System F:** 使用双向类型检查的具有参数多态性的二阶 Lambda 演算。
*   **System F-ω:** 具有高阶种类类型和 Haskell 中功能的 System F-ω。
*   **Calculus of Constructions:** 受 Lean 启发的依赖类型检查器，具有可数层级的宇宙和归纳类型。

这些实现使用了常见的 Rust 编译器库，并经过简化，以实现清晰和易于修改。作者鼓励通过 Github 上的 pull request 进行贡献和更正，因为它是一个 MIT 许可的业余项目。

---

## 54. 以无耻为策略 (2019)

**原文标题**: Shamelessness as a strategy (2019)

**原文链接**: [https://nadia.xyz/shameless](https://nadia.xyz/shameless)

无耻：现代社会一种出人意料的有效策略

---

## 55. MCP不需要工具，它需要代码。

**原文标题**: MCP doesn't need tools, it needs code

**原文链接**: [https://lucumr.pocoo.org/2025/8/18/code-mcps/](https://lucumr.pocoo.org/2025/8/18/code-mcps/)

Armin Ronacher 在其博文中指出，依赖众多 CLI 工具进行自主编程存在局限性，原因在于平台依赖、未文档化的功能以及复杂字符输入方面的挑战。代理在 CLI 会话（例如 tmux）中的状态管理方面存在困难，并且安全预检会减慢流程。

他建议使用 MCP（模型上下文协议）服务器，配备一个充当有状态 Python 解释器的单一“ubertool”。这简化了接口，利用了代理现有的 Python 和 pexpect 等库的知识，并有助于会话管理。代理不再拼凑 CLI 命令，而是在 MCP 会话中编写 Python 代码。

他用 “pexpect-mcp” 来说明这一点，这是一个公开可用的 MCP 服务器，提供了一个带有 pexpect 库的 Python 解释器。他演示了代理如何使用这个单一工具来调试崩溃的演示应用程序（使用 LLDB），有效地编写和执行 Python 脚本与调试器交互。此外，代理可以轻松地将这些调试交互转换为可重用的 Python 脚本。关键优势在于将重点转移到代理的优势——编程——并将会话管理卸载到 MCP。

---

## 56. 彩票假说：神经网络为何有效

**原文标题**: The lottery ticket hypothesis: why neural networks work

**原文链接**: [https://nearlyright.com/how-ai-researchers-accidentally-discovered-that-everything-they-thought-about-learning-was-wrong/](https://nearlyright.com/how-ai-researchers-accidentally-discovered-that-everything-they-thought-about-learning-was-wrong/)

本文探讨了“彩票假设”及其对理解大规模神经网络工作原理的影响，尽管这与传统的机器学习理论相悖。三百年来，偏差-方差权衡原则表明，过度复杂的模型会过度拟合数据，记住噪声而不是学习有用的模式。然而，在2019年，研究人员发现了“双下降”现象，即性能甚至在模型最初过度拟合后仍然有所提高。这导致了模型的规模扩大，从而产生了像ChatGPT这样的突破。

彩票假设解释了这一现象。它假设在大型网络中存在“中奖彩票”——具有正确初始权重的小型子网络，它们可以达到与完整网络相似的性能。这些网络成功不是通过记忆，而是通过提供大量机会来找到简单、优雅的解决方案。训练变成了一场大规模的彩票抽奖，其中最佳初始化的的小型网络脱颖而出。

该理论将经验上的成功与经典理论调和了起来：大型模型不会记忆，而是在广阔的参数空间中找到隐藏的简单解决方案。这不仅对人工智能有影响，也暗示着我们的大脑，拥有着大量的神经元，同样也为解决问题提供了潜在的解决方案。文章总结说，突破往往来自于检验假设和突破公认的理论。规模化的成功表明了未来的挑战以及底层架构约束的重要性。虽然规模化继续改进人工智能，但理解彩票机制有助于解释当前的成功并预测未来的局限性。

---

## 57. 一个人能够声称拥有2000万个IP地址。

**原文标题**: One person was able to claim 20M IPs

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS/#MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS/#MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS)

ipv4.games运营者Justine Tunney寻求帮助，一名玩家通过她的游戏成功认领了惊人的2000万个IPv4地址，根据Censys的数据，这相当于所有IPv4主机的9%。

该游戏托管在ipv4.games上，用户需要通过不同的IP地址向Tunney的Web服务器发送HTTP请求。要认领一个IP，需要与Google网络上的VM成功进行TCP三次握手。

Tunney对名为“femboy.cat”的欧洲玩家如何做到这一点感到困惑。她正在向NANOG社区征求想法和建议，以了解其使用的方法。此外，她幽默地建议北美有人站出来成为这位非常成功的玩家的竞争对手。该帖子包含17位参与者讨论该主题的列表。

---

## 58. 精确测绘追踪大平原草地木本植物扩张

**原文标题**: Precision mapping tracks woody plant spread across Great Plains grasslands

**原文链接**: [https://phys.org/news/2025-07-precision-tracks-woody-great-plains.html](https://phys.org/news/2025-07-precision-tracks-woody-great-plains.html)

堪萨斯州立大学的研究人员正在利用精确绘图和机器学习技术，追踪大平原草原上木本植物入侵的情况。木本植物入侵，即草原转变为以灌木和树木为主的景观，会影响生物多样性、牧草、水资源和野火风险。

这项发表在《遥感》杂志上的研究，详细介绍了一种经济高效、开放获取的方法，该方法结合了联邦项目（美国农业部、美国国家科学基金会）的航空影像和 Konza Prairie 生物站收集的地面数据。利用 LiDAR 和多光谱影像，研究人员在将区域划分为草原、灌木、树木或常绿树木时，达到了约 97% 的准确率。机器学习模型使用堪萨斯州立大学学生收集的数据进行训练，这些学生也获得了地理信息系统和计算机编码方面的经验。

该绘图工具的影响不仅限于分类，还可以为野牛的承载能力计算、火灾风险评估、栖息地选择研究和蜱传疾病暴露研究提供信息。例如，数据显示，草蜢雀的栖息地利用率甚至会随着少量木本覆盖而下降。研究人员计划通过网站或应用程序分享这项技术，用于区域早期预警系统，最终与土地所有者合作，利用卫星数据完善他们的模型，以便更广泛的应用和历史分析。目标是在解决草原面临的主要环境挑战的同时，为学生提供可转移的技能发展机会。

---

## 59. 实验室培育的三文鱼登上菜单

**原文标题**: Lab-grown salmon hits the menu

**原文链接**: [https://www.smithsonianmag.com/smart-news/lab-grown-salmon-hits-the-menu-at-an-oregon-restaurant-as-the-fda-greenlights-the-cell-cultured-product-180986769/](https://www.smithsonianmag.com/smart-news/lab-grown-salmon-hits-the-menu-at-an-oregon-restaurant-as-the-fda-greenlights-the-cell-cultured-product-180986769/)

Wildtype实验室培育的三文鱼已获得FDA批准，成为首个进入替代蛋白市场的培育鱼类。FDA表示对该产品的安全性“没有疑问”。Wildtype通过与厨师Gregory Gourdet的合作来庆祝这一里程碑，Gourdet将在其位于俄勒冈州波特兰的海地餐厅Kann供应实验室培育的三文鱼。Gourdet强调了该产品给他的菜单带来的可持续性和价值契合。

实验室培育肉类解决了人们对动物福利的担忧，对于鱼类而言，旨在缓解污染、气候变化和过度捕捞对海产品行业的影响。Wildtype通过从太平洋鲑鱼中提取活细胞并在受控环境中培养来生产其三文鱼。然后添加植物性成分，以模仿三文鱼片的味道、质地和外观。该公司声称其产品提供与传统三文鱼相同的营养益处，同时消除了汞、抗生素和寄生虫污染的风险。

目前，培育肉类价格更高，主要在高档餐厅中才能找到。Wildtype的三文鱼将在特定夜晚在Kann供应，之后将扩展到每日供应和其他餐厅。虽然培育肉类行业规模仍然很小，并且面临监管障碍，尤其是在一些正在考虑禁令的州，但Wildtype是少数几家获得FDA批准其培育动物产品的公司之一。

---

## 60. SystemD 服务加固

**原文标题**: SystemD Service Hardening

**原文链接**: [https://roguesecurity.dev/blog/systemd-hardening](https://roguesecurity.dev/blog/systemd-hardening)

本文提供了一份实用指南，旨在加强 Linux 系统上 systemd 服务的安全性，以降低潜在的安全漏洞带来的影响。文章强调，默认的 systemd 配置侧重易用性而非安全性，并提供了多种加固选项来解决这一问题。

文章首先介绍 `systemd-analyze security` 工具，用于评估单个服务或整个系统的安全状况。它解释了输出结果的含义，重点关注暴露指标，以便优先进行安全改进。

文章的核心内容详细介绍了如何通过修改 systemd 单元文件（或 podman quadlet 的 `[Container]` 部分）的 `[Service]` 部分来实施安全更改。文章建议使用覆盖存根来实现更清晰的配置管理。

文章提供了一个全面的（尽管承认是不完整的）安全选项列表，并解释了诸如 `ProtectSystem`、`PrivateTmp`、`ProtectHome`、`SystemCallFilter` 等选项的含义。它还讨论了 `SystemCallFilter` 限制的故障排除，包括如何使用 `auditd` 来识别被阻止的系统调用。

作者建议首先关注面向外部的服务，例如 Web 服务器和 SSH，特别是通过 systemd 运行的自定义脚本。文章在要点部分总结了关键的加固建议，并包含了一个加固 Traefik quadlet 单元的示例。

作者最后强调，这是一个为负责任的 Linux 管理员和自托管用户提供的工具。

---

## 61. 灵学及神秘学期刊保存协会

**原文标题**: Association for the Preservation of Spiritualist and Occult Periodicals

**原文链接**: [https://iapsop.com](https://iapsop.com)

国际灵学与神秘学期刊保存协会（IAPSOP）是一家位于美国的纯志愿者组织，致力于对维也纳会议至二战期间出版的灵学和神秘学期刊进行数字化保存。他们的档案向学生和研究人员免费开放，包含超过413万页的专著和期刊，总计超过730GB的数据。

目前，由于与AWS、中国和其他可能用于训练大型语言模型的IP地址相关的过度爬取，IAPSOP正面临服务限制，这影响了公平访问。因此，他们正在限制连接速度和带宽。

该网站提供多种探索途径，包括直接访问档案索引、精选的神秘学领域列表，以及用于实践教学的课程档案。如有请求、帮助或技术问题，可获得客户支持。他们还维护一个材料需求清单，并欢迎材料和劳力的捐赠。

该组织重点介绍了德语和法语神秘学期刊的最新更新，并列出了过去90天内访问量最高的20种出版物和访问国家/地区。这些资料根据知识共享署名-非商业性4.0国际许可协议进行授权，IAPSOP强调其对用户隐私和数据权利的承诺。

---

## 62. 用于解决航天力学问题的通用Fortran代码[pdf]

**原文标题**: A general Fortran code for solutions of problems in space mechanics [pdf]

**原文链接**: [https://jonathanadams.pro/blog-articles/Nasa-Fortran-Code-1963.pdf](https://jonathanadams.pro/blog-articles/Nasa-Fortran-Code-1963.pdf)

此文档似乎是一个已损坏或不完整的PDF文件，标题为“空间力学问题求解的通用Fortran代码”。PDF内容主要为二进制数据和元数据，包括交叉引用表、对象定义和流数据（可能使用FlateDecode或CCITTFaxDecode压缩）。它包含与PDF文档结构相关的信息，例如目录、页面、字体和图像，但大部分内容似乎是编码的图像数据和文本编码定义。由于内容的性质及其二进制结构，无法提供*文章内容*的有意义、人类可读的摘要。该文档可能*包含*Fortran代码，但详细信息位于编码且可能不完整的数据中。

---

## 63. 使用SGX保护电脑游戏的案例 (2016)

**原文标题**: A Case for Protecting Computer Games with SGX (2016)

**原文链接**: [https://dl.acm.org/doi/10.1145/3007788.3007792](https://dl.acm.org/doi/10.1145/3007788.3007792)

无法访问文章链接。

---

## 64. T-Mobile声称未经同意出售位置数据是合法的——法官们并不同意。

**原文标题**: T-Mobile claimed selling location data without consent is legal–judges disagree

**原文链接**: [https://arstechnica.com/tech-policy/2025/08/t-mobile-claimed-selling-location-data-without-consent-is-legal-judges-disagree/](https://arstechnica.com/tech-policy/2025/08/t-mobile-claimed-selling-location-data-without-consent-is-legal-judges-disagree/)

联邦上诉法院维持了FCC对T-Mobile和Sprint处以的9200万美元罚款，原因是其在未经同意的情况下非法向第三方公司出售客户位置数据。FCC最初对T-Mobile、AT&T和Verizon处以罚款，原因是其共享此数据且未能保护其免受未经授权的披露。T-Mobile和Sprint辩称FCC越权，但法院驳回了他们的论点，称FCC行为得当。

法院强调，手机位置数据为窥探个人生活提供了一个“私密窗口”。在2019年之前，T-Mobile和Sprint在未核实客户同意的情况下将此数据出售给聚合商，导致滥用行为。法院驳回了运营商的论点，即位置数据不符合法律规定的敏感信息，以及罚款过高，并援引了他们行为的“恶劣”性质，即使在违规行为曝光后也是如此。

法院还驳回了运营商关于陪审团审判权的诉求，称他们通过寻求直接审查自愿放弃了这项权利。T-Mobile正在“审查”法院的判决，而AT&T和Verizon正在其他上诉法院质疑各自的罚款。FCC最初于2020年提出罚款，但于2024年最终确定。

---

## 65. 硅谷AI交易催生僵尸初创公司

**原文标题**: Silicon Valley's AI deals are creating zombie startups

**原文链接**: [https://www.cnbc.com/2025/08/19/how-ai-zombie-deals-work-meta-google.html](https://www.cnbc.com/2025/08/19/how-ai-zombie-deals-work-meta-google.html)

硅谷人工智能热潮催生新型收购：Meta、谷歌、微软和亚马逊等科技巨头纷纷从人工智能初创企业挖走创始人及核心研究人员，导致一些投资者口中的“僵尸公司”出现。这种做法使这些巨头能够绕过与传统并购相关的监管障碍。

文章重点提到了一些案例，例如谷歌与Windsurf达成24亿美元的授权协议，导致其创始人离职加入谷歌；以及Meta对Scale AI投资143亿美元后，其CEO离职。微软聘用Inflection AI联合创始人的举动也是另一个例子。

这种趋势引起了风险投资家的担忧，因为有前途的初创企业正在被拆解，大部分经济利益流向了创始人及核心工程师，而非投资者和其他员工。虽然像Meta投资Scale AI这样的交易为早期投资者带来了丰厚的回报，但其他交易却使剩余的公司处于岌岌可危的境地。

文章指出，监管机构，尤其是联邦贸易委员会（FTC）的审查，推动科技公司转向这种变通办法。尽管监管机构正在调查一些交易，但这种趋势仍在继续，可能会扼杀创新，因为有才华的人被从独立企业中吸引走，转而为老牌公司工作。

---

## 66. 美国顶级公司CEO薪酬以四年最快速度增长

**原文标题**: CEO pay at top US companies accelerates at fastest pace in 4 years

**原文链接**: [https://www.ft.com/content/d8da9877-a5d0-4ac2-87cd-236ff33d7269](https://www.ft.com/content/d8da9877-a5d0-4ac2-87cd-236ff33d7269)

金融时报报道显示美国顶级公司CEO薪酬加速上涨，创四年最快增速。但遗憾的是，提供的文本主要为订阅提示，未包含关于CEO薪酬文章的具体内容。在无法访问全文的情况下，无法提供完整的摘要。然而，根据标题，文章可能探讨以下主题：

*   **CEO薪酬趋势：** 文章可能分析美国领先公司CEO薪酬的趋势，重点关注与往年相比的增长速度。
*   **推动增长的因素：** 文章可能讨论推动CEO薪酬上涨的潜在因素，例如公司业绩、市场状况或薪酬结构的变化。
*   **潜在影响：** 文章可能讨论CEO薪酬上涨对收入不平等、股东价值和员工士气等问题的潜在影响。
*   **《金融时报》的分析：** 文章将从《金融时报》的角度提供对CEO薪酬趋势的分析和见解。

要获得完整的摘要，需要访问全文。

---

## 67. 无线对讲文本通讯器

**原文标题**: Walkie-Textie Wireless Communicator

**原文链接**: [http://www.technoblogy.com/show?2AON](http://www.technoblogy.com/show?2AON)

Walkie-Textie是一种手持设备，使用LoRa无线协议发送和接收文本消息，非常适合没有移动信号的区域或作为低成本的通信工具。它具有一个用于多次点击文本输入的12键键盘，一个用于显示消息和状态的OLED显示屏，并使用由ATtiny814微控制器控制的HopeRF RFM95W LoRa模块。

LoRa在乡村地区提供高达10英里的范围，并使用免许可的亚千兆赫频率。Walkie-Textie在一个滚动窗口中显示接收到的消息，并显示信号强度、蜂鸣器状态和电池电量。

该设备的构造涉及将表面贴装组件焊接在定制设计的PCB上，该PCB由JLCPCB制造。可以使用简单的导线天线或用于“橡胶鸭”天线的SMA连接器。它可以由LiPo电池或两节AAA电池供电。

该程序使用字符单元绘图来避免需要内存显示缓冲区，并利用Arduino LoRa库进行无线通信。用户需要在代码中设置适当的频率和SyncWord。ATtiny814微控制器使用Spence Konde的megaTinyCore和USB转串口板进行编程。提供了代码、PCB的Eagle/Gerber文件和零件清单等资源。该文章还建议可以实施消息回执确认系统。

---

## 68. The Cutaway Illustrations of Fred Freeman (2016)

**原文标题**: The Cutaway Illustrations of Fred Freeman (2016)

**原文链接**: [https://5wgraphicsblog.com/2016/10/24/the-cutaway-illustrations-of-fred-freeman/](https://5wgraphicsblog.com/2016/10/24/the-cutaway-illustrations-of-fred-freeman/)

生成摘要时出错

---

## 69. Show HN: Fractional jobs – part-time roles for engineers

**原文标题**: Show HN: Fractional jobs – part-time roles for engineers

**原文链接**: [https://www.fractionaljobs.io](https://www.fractionaljobs.io)

生成摘要时出错

---

## 70. The Weight of a Cell

**原文标题**: The Weight of a Cell

**原文链接**: [https://www.asimov.press/p/cell-weight](https://www.asimov.press/p/cell-weight)

生成摘要时出错

---

## 71. Electromechanical reshaping,  an alternative to laser eye surgery

**原文标题**: Electromechanical reshaping,  an alternative to laser eye surgery

**原文链接**: [https://medicalxpress.com/news/2025-08-alternative-lasik-lasers.html](https://medicalxpress.com/news/2025-08-alternative-lasik-lasers.html)

生成摘要时出错

---

## 72. Web apps in a single, portable, self-updating, vanilla HTML file

**原文标题**: Web apps in a single, portable, self-updating, vanilla HTML file

**原文链接**: [https://hyperclay.com/](https://hyperclay.com/)

生成摘要时出错

---

## 73. ChatGPT Go

**原文标题**: ChatGPT Go

**原文链接**: [https://help.openai.com/en/articles/11989085-what-is-chatgpt-go](https://help.openai.com/en/articles/11989085-what-is-chatgpt-go)

生成摘要时出错

---

## 74. The Lives and Loves of James Baldwin

**原文标题**: The Lives and Loves of James Baldwin

**原文链接**: [https://www.newyorker.com/magazine/2025/08/18/baldwin-a-love-story-nicholas-boggs-book-review](https://www.newyorker.com/magazine/2025/08/18/baldwin-a-love-story-nicholas-boggs-book-review)

生成摘要时出错

---

## 75. Who Invented Backpropagation?

**原文标题**: Who Invented Backpropagation?

**原文链接**: [https://people.idsia.ch/~juergen/who-invented-backpropagation.html](https://people.idsia.ch/~juergen/who-invented-backpropagation.html)

生成摘要时出错

---

## 76. Structured (Synchronous) Concurrency

**原文标题**: Structured (Synchronous) Concurrency

**原文链接**: [https://fsantanna.github.io/sc.html](https://fsantanna.github.io/sc.html)

生成摘要时出错

---

## 77. Sikkim and the Himalayan Chess Game (2016)

**原文标题**: Sikkim and the Himalayan Chess Game (2016)

**原文链接**: [https://www.historytoday.com/archive/feature/sikkim-and-himalayan-chess-game](https://www.historytoday.com/archive/feature/sikkim-and-himalayan-chess-game)

生成摘要时出错

---

## 78. XZ Utils Backdoor Still Lurking in Docker Images

**原文标题**: XZ Utils Backdoor Still Lurking in Docker Images

**原文链接**: [https://www.binarly.io/blog/persistent-risk-xz-utils-backdoor-still-lurking-in-docker-images](https://www.binarly.io/blog/persistent-risk-xz-utils-backdoor-still-lurking-in-docker-images)

生成摘要时出错

---

## 79. Why I'm all-in on Zen Browser

**原文标题**: Why I'm all-in on Zen Browser

**原文链接**: [https://werd.io/why-im-all-in-on-zen-browser/](https://werd.io/why-im-all-in-on-zen-browser/)

生成摘要时出错

---

## 80. How to free up and automatically manage disk space for WSL

**原文标题**: How to free up and automatically manage disk space for WSL

**原文链接**: [https://www.freecodecamp.org/news/how-to-free-up-and-automatically-manage-disk-space-for-wsl-on-windows-1011/](https://www.freecodecamp.org/news/how-to-free-up-and-automatically-manage-disk-space-for-wsl-on-windows-1011/)

生成摘要时出错

---

## 81. Why Are Some Stats Too 'Girly' for the BLS?

**原文标题**: Why Are Some Stats Too 'Girly' for the BLS?

**原文链接**: [https://www.bloomberg.com/opinion/articles/2025-08-19/some-statistics-are-too-girly-for-the-bls](https://www.bloomberg.com/opinion/articles/2025-08-19/some-statistics-are-too-girly-for-the-bls)

生成摘要时出错

---

## 82. How much do electric car batteries degrade?

**原文标题**: How much do electric car batteries degrade?

**原文链接**: [https://www.sustainabilitybynumbers.com/p/electric-car-battery-degradation](https://www.sustainabilitybynumbers.com/p/electric-car-battery-degradation)

生成摘要时出错

---

## 83. LinkedIn is the fakest platform of them all

**原文标题**: LinkedIn is the fakest platform of them all

**原文链接**: [https://www.prospectmagazine.co.uk/ideas/technology/70741/linkedin-is-the-fakest-platform-of-them-all](https://www.prospectmagazine.co.uk/ideas/technology/70741/linkedin-is-the-fakest-platform-of-them-all)

生成摘要时出错

---

## 84. Phrack 72

**原文标题**: Phrack 72

**原文链接**: [https://phrack.org/issues/72/1](https://phrack.org/issues/72/1)

生成摘要时出错

---

## 85. The Pragmatic Engineer 2025 Survey: What's in your tech stack? Part 1

**原文标题**: The Pragmatic Engineer 2025 Survey: What's in your tech stack? Part 1

**原文链接**: [https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey)

生成摘要时出错

---

## 86. GenAI FOMO has spurred businesses to light nearly $40B on fire

**原文标题**: GenAI FOMO has spurred businesses to light nearly $40B on fire

**原文链接**: [https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent/](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent/)

生成摘要时出错

---

## 87. I Run a Full Linux Desktop in Docker Just Because I Can

**原文标题**: I Run a Full Linux Desktop in Docker Just Because I Can

**原文链接**: [https://www.howtogeek.com/i-run-a-full-linux-desktop-in-docker-just-because-i-can/](https://www.howtogeek.com/i-run-a-full-linux-desktop-in-docker-just-because-i-can/)

生成摘要时出错

---

## 88. Apple and Amazon will miss AI like Intel missed mobile

**原文标题**: Apple and Amazon will miss AI like Intel missed mobile

**原文链接**: [https://gmays.com/the-biggest-bet-in-tech/](https://gmays.com/the-biggest-bet-in-tech/)

生成摘要时出错

---

## 89. Countrywide natural experiment links built environment to physical activity

**原文标题**: Countrywide natural experiment links built environment to physical activity

**原文链接**: [https://www.nature.com/articles/s41586-025-09321-3](https://www.nature.com/articles/s41586-025-09321-3)

生成摘要时出错

---

## 90. 8x19 Text Mode Font Origins

**原文标题**: 8x19 Text Mode Font Origins

**原文链接**: [https://www.os2museum.com/wp/8x19-text-mode-font-origins/](https://www.os2museum.com/wp/8x19-text-mode-font-origins/)

生成摘要时出错

---

## 91. Vibe coding tips and tricks

**原文标题**: Vibe coding tips and tricks

**原文链接**: [https://github.com/awslabs/mcp/blob/main/VIBE_CODING_TIPS_TRICKS.md](https://github.com/awslabs/mcp/blob/main/VIBE_CODING_TIPS_TRICKS.md)

生成摘要时出错

---

## 92. A gigantic jet caught on camera: A spritacular moment for NASA astronaut

**原文标题**: A gigantic jet caught on camera: A spritacular moment for NASA astronaut

**原文链接**: [https://science.nasa.gov/science-research/heliophysics/a-gigantic-jet-caught-on-camera-a-spritacular-moment-for-nasa-astronaut-nicole-ayers/](https://science.nasa.gov/science-research/heliophysics/a-gigantic-jet-caught-on-camera-a-spritacular-moment-for-nasa-astronaut-nicole-ayers/)

生成摘要时出错

---

## 93. My Retro TVs

**原文标题**: My Retro TVs

**原文链接**: [https://www.myretrotvs.com/](https://www.myretrotvs.com/)

生成摘要时出错

---

## 94. Image Fulgurator (2011)

**原文标题**: Image Fulgurator (2011)

**原文链接**: [https://juliusvonbismarck.com/bank/index.php/projects/image-fulgurator/2/](https://juliusvonbismarck.com/bank/index.php/projects/image-fulgurator/2/)

生成摘要时出错

---

## 95. TREAD: Token Routing for Efficient Architecture-Agnostic Diffusion Training

**原文标题**: TREAD: Token Routing for Efficient Architecture-Agnostic Diffusion Training

**原文链接**: [https://arxiv.org/abs/2501.04765](https://arxiv.org/abs/2501.04765)

生成摘要时出错

---

## 96. What Is the Luhn Algorithm? The Math Behind Credit Card Transactions

**原文标题**: What Is the Luhn Algorithm? The Math Behind Credit Card Transactions

**原文链接**: [https://www.scientificamerican.com/article/what-is-the-luhn-algorithm-the-math-behind-secure-credit-card-numbers/](https://www.scientificamerican.com/article/what-is-the-luhn-algorithm-the-math-behind-secure-credit-card-numbers/)

生成摘要时出错

---

## 97. Macintosh Drawing Software Compared (2021)

**原文标题**: Macintosh Drawing Software Compared (2021)

**原文链接**: [https://blog.gingerbeardman.com/2021/04/24/macintosh-drawing-software-compared/](https://blog.gingerbeardman.com/2021/04/24/macintosh-drawing-software-compared/)

生成摘要时出错

---

## 98. Sky Calendar

**原文标题**: Sky Calendar

**原文链接**: [https://abramsplanetarium.org/SkyCalendar/index.html](https://abramsplanetarium.org/SkyCalendar/index.html)

生成摘要时出错

---

## 99. What could have been

**原文标题**: What could have been

**原文链接**: [https://coppolaemilio.com/entries/what-could-have-been/](https://coppolaemilio.com/entries/what-could-have-been/)

生成摘要时出错

---

## 100. Britain Drops Request That Apple Create a Back Door

**原文标题**: Britain Drops Request That Apple Create a Back Door

**原文链接**: [https://www.nytimes.com/2025/08/19/technology/britain-apple-back-door.html](https://www.nytimes.com/2025/08/19/technology/britain-apple-back-door.html)

生成摘要时出错

---

