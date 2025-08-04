# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-04.md)

*最后自动更新时间: 2025-08-04 17:55:24*
## 1. Show HN: 我花了六年时间造了个奇葩的木制像素显示器

**原文标题**: Show HN: I spent 6 years building a ridiculous wooden pixel display

**原文链接**: [https://benholmen.com/blog/kilopixel/](https://benholmen.com/blog/kilopixel/)

作者历经六年开发，推出了Kilopixel (kilopx.com)，这是一个大型且不实用的木制显示器，尺寸为40x25（1000像素），通过网络界面控制，允许互联网上的任何人进行绘制。该项目受非传统镜子和慢速电子墨水屏的启发，旨在成为效率最低的显示器。

开发过程涉及众多原型，最初采用木制龙门系统，后转向挤压铝材。一个重大挑战是寻找合适的像素，作者尝试了各种球体（乒乓球、Nerf球等），最终因成本、重量和一致性问题而选择了定制的立方木制像素。作者在像素旋转机制上也遇到了困难，最初考虑使用小型电机和乐高轮子。

最终版本使用CNC机床，配备定制的龙门架，移动到每个像素，并使用独特的“戳动”机制来旋转木块。该系统使用树莓派来查询API获取下一个像素，编写g代码，戳动像素，并读取光传感器以确定其状态。

Web应用程序允许用户提交40x25像素的图像、投票选出提交内容，甚至可以实时协作。作者计划在YouTube上直播显示器，并创建绘制过程的延时视频，期待看到互联网如何与该项目互动，并计划可能将该项目传递下去。

---

## 2. 第一部分：Rust与C内存互操作性深度解析

**原文标题**: Part 1: A Deep Dive into Rust and C Memory Interoperability

**原文链接**: [https://notashes.me/blog/part-1-memory-management/](https://notashes.me/blog/part-1-memory-management/)

第一部分：Rust与C内存互操作深度剖析

本文探讨了混合Rust和C内存分配器的复杂性。首先强调了这种做法的潜在危险，即不正确的内存释放可能导致静默损坏，这是最坏的情况。作者强调理解内存分配器如何运作对于避免意外崩溃和bug的重要性。

文章随后深入探讨了内存基础知识，解释了诸如虚拟内存、虚拟地址如何转化为物理RAM以及与内存访问相关的成本等概念。它描述了堆在动态内存分配中的作用以及碎片化的挑战。CPU缓存架构，包括L1、L2和L3缓存，也被讨论，重点关注“伪共享”及其对性能的负面影响。

文章的重要部分详细介绍了内存测试实验室的创建。这个使用Rust和C构建的框架，旨在通过测试多种分配器实现、处理崩溃、测量性能以及提供详细的调试信息来安全地探索分配器交互。该框架使用子进程隔离、通过FFI加载C库、退出代码分析和性能测量工具。

最后，文章介绍了测试框架中使用的四种不同的C分配器实现：标准的`malloc`封装器、用于检测内存损坏的调试分配器、用于绕过堆的直接`mmap`分配器以及用于快速、临时分配的arena分配器。

---

## 3. 开放式IP摄像头固件

**原文标题**: Open IP Camera Firmware

**原文链接**: [https://openipc.org/à](https://openipc.org/à)

OpenIPC 是一款开源的第三方固件，旨在取代许多使用 ARM 和 MIPS 处理器的 IP 摄像头上封闭源代码、通常过时且不安全的固件。它为用户提供了对其摄像头更大的控制权和安全性。

该固件以预编译二进制文件的形式分发，以便于安装，但完整的源代码也以 MIT 许可证提供，鼓励社区贡献和修改。OpenIPC 项目使用 Buildroot 构建其 Linux 发行版，并利用 Majestic、Mini 或 Venc 流处理器。虽然 Majestic 目前是闭源的，但作者计划在未来获得足够的资金支持后将其开源。

OpenIPC 的主要优势在于它提供的自由。用户可以完全控制他们的摄像头和视频流，从而消除对后门、恶意软件或数据泄露的担忧。该固件优先考虑诸如固件升级和视频/音频流配置等核心功能。

除了基本功能之外，OpenIPC 还支持与 IPEYE 云存储、向 YouTube 和 Telegram 进行视频流、SOCKS5 代理和虚拟隧道的集成。该项目还满足无人机摄像头、建筑头盔、医学研究和水下捕鱼等专业应用的需求。本文还提到了一个支持者部分。

---

## 4. Perplexity 正使用隐蔽的、未声明的爬虫来规避禁止抓取的指令。

**原文标题**: Perplexity is using stealth, undeclared crawlers to evade no-crawl directives

**原文链接**: [https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)

Cloudflare 指责 Perplexity 使用隐形爬虫绕过网站“禁止抓取”指令。Cloudflare 观察到，在使用 robots.txt 和 WAF 规则阻止 Perplexity 声明的爬虫 (PerplexityBot 和 Perplexity-User) 后，Perplexity 仍然使用伪装成通用 Chrome 浏览器的未声明爬虫访问内容。这种“隐形爬虫”使用不同的 IP 和 ASN 来逃避检测和规避屏蔽。

Cloudflare 认为这种行为违反了互联网的信任原则，该原则要求爬虫具有透明度并遵守网站的偏好。相比之下，该文章赞扬 OpenAI 尊重 robots.txt 并且不试图规避屏蔽。

Cloudflare 已采取行动，将 Perplexity 从已验证的机器人列表中移除，并添加规则到其管理系统中以阻止这种隐形爬虫。 现有的拥有机器人管理规则的 Cloudflare 客户已经受到保护。该公司还提供了挑战来自可疑机器人的请求的选项，提供进一步的保护。

文章最后强调了 Cloudflare 对内容独立日（Content Independence Day）的承诺，该活动旨在让内容创作者控制 AI 如何访问他们的内容。Cloudflare 正在与技术和政策专家合作，为行为良好的机器人运营商建立明确的原则，并调整其方法来对抗不断演变的规避技术。

---

## 5. 事实无法拯救你 - 人工智能、历史与苏联科幻

**原文标题**: Facts will not Save You - AI, History and Soviet Sci-Fi

**原文链接**: [https://hegemon.substack.com/p/facts-will-not-save-you](https://hegemon.substack.com/p/facts-will-not-save-you)

无法访问文章链接。

---

## 6. 我理想的数组语言

**原文标题**: My Ideal Array Language

**原文链接**: [https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html](https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html)

本文概述了作者对理想数组语言的愿景，强调语言和编译器需要适应现代硬件日益增长的异构性。关键特性包括用户可扩展的秩多态、具有自动缓冲区化的值语义以及编译器透明性。

作者认为，秩多态对于数组语言至关重要，它允许用户编写自己的多态内核。他们强调了值语义和自动缓冲区化的优势，并将其与Fortran因其数组语义而生成高性能代码的能力相提并论。本文深入探讨了MLIR在数组编译中的作用，特别是张量和memref类型，展示了函数式数组语言如何与编译器内部表示很好地对齐。

本文强调了基于语言语义进行优化的编译步骤（离线或在线）的重要性。编译器透明性和可检查性被认为是至关重要的，它允许用户了解优化失败并调试性能问题。作者引用了LLVM的remarks框架作为很好的例子，尽管它面向编译器工程师。最终，本文倡导一种数组语言，该语言赋予用户控制和洞察编译过程的能力，使他们能够编写针对各种硬件架构优化的高效代码。

---

## 7. 日本沿海的百年石头“海啸石”（2015年）

**原文标题**: Century-Old Stone “Tsunami Stones” Dot Japan's Coastline (2015)

**原文链接**: [https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/](https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/)

本文探讨了日本历史上竖立“海啸石”的做法，旨在警示后代在沿海地区建设的危险。这些石头，有些可以追溯到1896年毁灭性海啸之后，提醒人们在地震后寻找更高地势以避免后续海浪。本文重点介绍了姉吉的海啸石，它明确指示人们不要在其下方建造房屋。

历史学家北原糸子强调，这些石头是跨世代的警告，旨在防止未来的苦难。然而，随着时间的推移，随着沿海城镇的扩张和对海堤的信任，它们的意义往往被忽视。尽管如此，一些社区，如姉吉，继续听取石头的警告，这在2011年的海啸中证明至关重要。

本文还提到，海啸在地名上留下了印记，指示着安全或危险的地点。今村文彦指出，灾难的记忆往往在三代之后消退，导致警告被遗忘。文章最后提到了2011年海啸和福岛第一核电站事故的持续恢复，强调了理解和尊重沿海地区潜在危险的持续重要性。

---

## 8. 科学家用激光照射人头

**原文标题**: Scientists shine a laser through a human head

**原文链接**: [https://spectrum.ieee.org/optical-brain-imaging](https://spectrum.ieee.org/optical-brain-imaging)

科学家首次成功地将激光穿透人头。这项由BiomedicalNews报道的突破是开发潜在的廉价新型医学成像技术的重要一步。格拉斯哥大学极端光研究小组的研究人员通过将激光中的光子穿过颅骨和大脑发送到另一侧的探测器来实现的。提供的图像显示了50个光子从激光器（红色）到探测器（绿色）的潜在路径。虽然文章没有详细说明成像技术的具体细节，但它清楚地表明，光线穿透颅骨的能力是其发展的根本。这一成就意义重大，因为它表明与现有的MRI或CT扫描等技术相比，有可能获得更经济实惠的医学成像解决方案。

---

## 9. 求职者躲避AI面试官

**原文标题**: Job-seekers are dodging AI interviewers

**原文链接**: [https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/](https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/)

财富杂志文章探讨了公司使用人工智能进行面试的日益增长的趋势，以及由此产生的求职者反弹。 虽然人力资源部门将人工智能面试官视为高效处理大量求职者和腾出时间进行更有意义的后期对话的方式，但许多候选人认为这种体验不人性化且无效。

求职者将人工智能面试描述为尴尬、冷漠，甚至是一个表明公司文化不佳的危险信号。他们对重复提问、人工智能无法回答有关公司的问题以及感觉自己被低估表示沮丧。有些人完全拒绝参加人工智能面试，宁愿冒着继续失业的风险，也不愿让自己接受这个过程。

该文章突出了对比鲜明的观点：人力资源专业人士强调节省时间的好处以及专注于优秀候选人的能力，而求职者则感叹缺乏人际交往，并对工作过度自动化的未来表示担忧。

尽管求职者的负面反馈，提供人工智能面试解决方案的公司声称他们的客户对结果感到满意，这表明该技术将继续存在，特别是在初始筛选阶段。 然而，即使是人工智能的支持者也承认其局限性，尤其是在评估文化契合度方面，突显了在招聘过程中仍然需要人的参与。

---

## 10. Show HN：为孩子们制作的迷你逻辑和数字游戏

**原文标题**: Show HN: Tiny logic and number games I built for my kids

**原文链接**: [https://quizmathgenius.com/](https://quizmathgenius.com/)

这个“Show HN”帖子介绍了一系列为作者孩子制作的微型逻辑和数字游戏。内容比较简单，主要由标题和导航元素“Prev”和“Next”组成，暗示可以通过这些导航链接访问一系列游戏。大脑表情符号“🧠”强化了这些游戏是基于谜题或逻辑的想法。该帖子强调了作者的个人动机（为他们的孩子制作游戏），并隐式地邀请其他人探索这个合集。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 2 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 3 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 4 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 5 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 6 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 7 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 8 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 9 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 10 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 11 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 12 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 13 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 14 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 15 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 16 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 17 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 18 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 19 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 20 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 21 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 22 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 23 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 24 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 25 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 26 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 27 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 28 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 29 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 30 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 31 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 32 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 33 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 34 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 35 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 36 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 37 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 38 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 39 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 40 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 41 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 42 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 43 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 44 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 45 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 46 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 47 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 48 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 49 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 50 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 51 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 52 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 53 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 54 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 55 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 56 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 57 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 58 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 59 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 60 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 61 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 62 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 63 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 64 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 65 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 66 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 67 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 68 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 69 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 70 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 71 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 72 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 73 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 74 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 75 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 76 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 77 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 78 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 79 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 80 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 81 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 82 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 83 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 84 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 85 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 86 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 87 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 88 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 89 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 90 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 91 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 92 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 93 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 94 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 95 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 96 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 97 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 98 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 99 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 100 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 101 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 102 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 103 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 104 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 105 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 106 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 107 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 108 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 109 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 110 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 111 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 112 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 113 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 114 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 115 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 116 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 117 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 118 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 119 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 120 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 121 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 122 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 123 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 124 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 125 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 126 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 127 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 128 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 129 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 130 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 131 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 132 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 133 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 134 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 135 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 136 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 137 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 138 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
