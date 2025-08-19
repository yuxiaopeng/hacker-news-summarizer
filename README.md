# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-19.md)

*最后自动更新时间: 2025-08-19 17:48:14*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 2 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 3 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 4 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 5 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 6 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 7 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 8 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 9 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 10 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 11 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 12 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 13 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 14 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 15 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 16 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 17 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 18 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 19 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 20 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 21 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 22 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 23 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 24 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 25 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 26 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 27 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 28 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 29 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 30 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 31 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 32 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 33 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 34 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 35 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 36 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 37 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 38 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 39 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 40 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 41 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 42 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 43 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 44 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 45 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 46 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 47 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 48 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 49 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 50 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 51 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 52 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 53 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 54 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 55 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 56 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 57 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 58 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 59 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 60 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 61 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 62 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 63 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 64 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 65 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 66 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 67 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 68 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 69 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 70 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 71 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 72 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 73 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 74 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 75 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 76 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 77 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 78 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 79 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 80 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 81 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 82 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 83 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 84 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 85 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 86 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 87 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 88 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 89 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 90 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 91 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 92 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 93 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 94 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 95 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 96 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 97 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 98 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 99 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 100 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 101 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 102 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 103 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 104 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 105 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 106 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 107 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 108 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 109 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 110 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 111 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 112 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 113 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 114 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 115 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 116 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 117 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 118 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 119 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 120 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 121 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 122 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 123 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 124 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 125 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 126 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 127 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 128 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 129 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 130 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 131 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 132 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 133 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 134 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 135 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 136 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 137 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 138 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 139 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 140 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 141 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 142 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 143 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 144 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 145 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 146 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 147 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 148 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 149 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 150 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 151 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 152 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 153 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
