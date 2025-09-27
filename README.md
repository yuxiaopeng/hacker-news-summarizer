# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-27.md)

*最后自动更新时间: 2025-09-27 17:50:44*
## 1. 格陵兰：美丽的梦魇

**原文标题**: Greenland Is a Beautiful Nightmare

**原文链接**: [https://matduggan.com/greenland-is-a-beautiful-nightmare/](https://matduggan.com/greenland-is-a-beautiful-nightmare/)

作者回忆起他们意外的格陵兰之旅，最初源于一个随意的约定。出行前，他们因令人失望的旅行视频而感到焦虑，并准备迎接一段黯淡的经历。由于雾气，一段令人沮丧的航班最终返回起点，凸显了不可预测的旅行条件。

最终抵达后，格陵兰呈现出截然不同的景象：一个平静而冷静的人民与一个极其不适宜居住的景观形成鲜明对比。首都努克感觉既宁静又超现实，在这个小城市里出现了交通拥堵。作者随后前往伊卢利萨特，那里饱受蚊群侵扰，并且目睹了雪橇犬在恶劣条件下生存。

这次旅行包括一次乘船游览，作者的女儿喜欢吃冰川冰。对格陵兰文化的观察，包括鲸鱼消费和工业捕捞方法的使用，挑战了先入为主的观念。作者强调了在这个道路有限的地方，豪华轿车的令人费解的存在，以及当地杂货店和当地美食的古怪之处。

---

## 2. SSH3：使用HTTP/3更快更丰富的安全Shell

**原文标题**: SSH3: Faster and rich secure shell using HTTP/3

**原文链接**: [https://github.com/francoismichel/ssh3](https://github.com/francoismichel/ssh3)

SSH3是基于HTTP/3构建的SSH协议的新版本，旨在实现更快的会话建立和增强的安全特性。它利用QUIC+TLS 1.3进行安全连接，并使用HTTP授权进行用户身份验证。主要优势包括显著加快的会话建立速度（3个往返时间，而SSHv2为5-7个）、对OAuth 2.0和OpenID Connect等现代身份验证方法的支持，以及通过允许服务器隐藏在秘密URL后面来提高抵御端口扫描的鲁棒性。

其他优势包括UDP端口转发、连接迁移（计划中）和多路径连接，这些都由底层的QUIC协议支持。它支持常见的密码和公钥认证（RSA、EdDSA/ed25519）。

重要的是，SSH3目前处于实验阶段，未经彻底的安全审查，不建议用于生产环境。鼓励社区反馈和专家分析。

SSH3提供诸如服务器的X.509证书认证、通过OpenID Connect进行的无密钥用户认证等功能，并支持OpenSSH功能，例如authorized_keys解析、ssh-agent集成、TCP端口转发和代理跳转。

本文档提供了有关如何从源代码或使用`go install`安装SSH3、部署SSH3服务器（包括生成Let's Encrypt证书或自签名证书）以及使用SSH3客户端进行私钥、基于代理或基于密码的身份验证的说明。它还解释了如何使用类似OpenSSH的配置文件配置SSH3。

---

## 3. 首个恶意MCP：邮戳后门窃取你的邮件

**原文标题**: First Malicious MCP in the Wild: The Postmark Backdoor Stealing Your Emails

**原文链接**: [https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft)

BackKoi研究揭露首个恶意MCP服务器“postmark-mcp”被植入后门窃取邮件。MCP服务器是AI助手用于自动化任务（如发送邮件和数据库查询）的工具，通常具有广泛权限。每周下载1500次的“postmark-mcp”软件包自1.0.16版本起，被发现将所有邮件复制到攻击者服务器giftshop.club。

攻击者在npm上冒充合法的Postmark包，添加一行代码来密件抄送每封邮件。这突显了一个重大安全风险：开发者经常信任并集成这些工具，而未进行适当审查，从而授予它们对敏感数据的广泛访问权限。文章强调，传统安全措施通常无法检测到此类威胁，因为开发者独立采用在既定安全范围之外运行的AI工具。

潜在影响巨大，可能影响数百个组织和每天数千封电子邮件。作者强调了MCP生态系统的固有漏洞，其中AI助手盲目执行来自不受信任来源的命令。他们建议立即删除受感染的软件包，轮换暴露的凭据，并审计所有MCP服务器以查找可疑活动。Koi的风险引擎和供应链网关被认为是检测和预防类似威胁的解决方案。文章敦促在使用MCP服务器时提高警惕和保持高度戒备。

---

## 4. 在微型星球上投递信息的WebGL游戏

**原文标题**: A WebGL game where you deliver messages on a tiny planet

**原文链接**: [https://messenger.abeto.co/](https://messenger.abeto.co/)

核心概念是一款名为“信使 (Messenger)”的 WebGL 游戏，玩家的主要目标是在一个微型、据推测是程序生成的星球上递送消息。“信使 (Messenger)”这个名称直接反映了玩家的角色和核心游戏机制。虽然这句描述非常简短，但它突出了技术基础 (WebGL)、类型 (游戏)、玩家的任务 (消息传递) 和背景 (一个小星球)。描述的简洁性表明重点可能在于构建 WebGL 游戏的技术方面，在微型世界中导航进行交付的独特游戏机制，或两者兼而有之。关于游戏视觉效果、故事、挑战和进展系统的更多细节尚不明确，但核心理念已经明确：玩家是在紧凑的行星尺度上工作的信使。

---

## 5. 困在树莓派中的AI模型

**原文标题**: AI model trapped in a Raspberry Pi

**原文链接**: [https://blog.adafruit.com/2025/09/26/ai-model-trapped-in-raspberry-pi-piday-raspberrypi/](https://blog.adafruit.com/2025/09/26/ai-model-trapped-in-raspberry-pi-piday-raspberrypi/)

无法访问文章链接。

---

## 6. Typst：一个可能的LaTeX替代品

**原文标题**: Typst: A Possible LaTeX Replacement

**原文链接**: [https://lwn.net/Articles/1037577/](https://lwn.net/Articles/1037577/)

这篇2025年9月17日来自LWN.net的文章介绍了Typst，一种潜在的LaTeX替代方案。Typst使用Rust编写，并采用Apache-2.0许可，旨在提供更简单的标记系统、更快的编译速度和更便捷的自定义功能，同时保持与LaTeX相媲美的高质量输出。

文章强调了LaTeX作为技术文档长期标准的优势，但也承认用户对其庞大的安装体积、缓慢的编译速度、晦涩的错误信息以及用于自定义的神秘宏语言感到不满。

Typst自2019年以来一直在开发，它通过一种受Markdown启发的、不太冗长、更易读的标记语法以及更清晰、带有颜色编码的错误信息来解决这些问题。它还提供了一个“watch”模式，用于在编辑期间进行实时预览。作者赞扬了Typst集成的编程语言（类似于Rust）、对浮动图形和表格的出色处理，以及学术期刊的初步采用。

缺点包括与LaTeX庞大的生态系统相比，缺乏专门的软件包、文档问题以及在早期开发过程中可能出现的重大更改。 然而，编程的简易性和积极响应的开发团队被认为是优势。 虽然期刊模板支持有限，但Pandoc可以将Typst转换为LaTeX。 作者总结说，他们正在使用Typst撰写一篇物理论文，并使用Pandoc将其转换为LaTeX，赞扬了其数学公式处理和语法感知编辑器支持，并预测Typst最终可能会取代LaTeX。 长期成功的关键将是保持与用户文档的前向兼容性。

---

## 7. 伟大的问题 (YC W21) 正在招聘产品总监

**原文标题**: Great Question (YC W21) Is Hiring Director of Product

**原文链接**: [https://www.ycombinator.com/companies/great-question/jobs/9crdslU-director-of-product](https://www.ycombinator.com/companies/great-question/jobs/9crdslU-director-of-product)

Great Question 招募产品总监或高级总监

---

## 8. 挪威将在斯瓦尔巴群岛监测空气中的放射性。

**原文标题**: Norway to Monitor Airborne Radioactivity in Svalbard

**原文链接**: [https://www.highnorthnews.com/en/norway-monitor-airborne-radioactivity-svalbard](https://www.highnorthnews.com/en/norway-monitor-airborne-radioactivity-svalbard)

挪威将在斯瓦尔巴群岛监测空气中的放射性物质。此举可能源于俄罗斯新地岛试验场负责人声明称，该试验场已准备好可能恢复核试验。新地岛位于俄罗斯北部，是冷战时期主要的核武器试验场。虽然目前没有迹象表明正在进行试验，但挪威在斯瓦尔巴群岛的监测计划表明，该地区对潜在核活动的意识和准备程度有所提高。在斯瓦尔巴群岛的监测旨在检测和测量可能源于核活动的任何空气中的放射性粒子，确保挪威能够迅速评估并应对任何可能对其环境和人口造成的威胁。

---

## 9. 2024年亚马逊火灾对大气CO₂破纪录增长的前所未有影响

**原文标题**: Unprecedented role of Amazon fires in the record atmospheric CO₂ growth in 2024

**原文链接**: [https://essopenarchive.org/doi/full/10.22541/essoar.175874118.83695562/v1](https://essopenarchive.org/doi/full/10.22541/essoar.175874118.83695562/v1)

无法访问文章链接。

---

## 10. 虚拟内存基础

**原文标题**: Fundamental of Virtual Memory

**原文链接**: [https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html](https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html)

本文解释了虚拟内存的基础知识，这是现代操作系统中的一个关键概念。文章首先强调了与较慢的磁盘存储相比，主内存（RAM）对于快速数据访问的必要性。由于寄存器数量有限，主内存作为程序和数据的大型、可寻址空间。

文章接着讨论了一个简单的内存分配策略（连续块）及其缺点：外部碎片。为了解决这个问题，文章介绍了分页，即内存被划分为固定大小的帧，进程使用虚拟内存，这是一种由操作系统映射到物理内存的抽象。虚拟内存被划分为页，这些页使用页表映射到帧。解释了诸如页号、帧号和偏移量等关键概念。还介绍了不同的页表结构（多级、哈希、倒置）。

然后介绍了按需分页，解释了如何只将必要的页加载到内存中，从而提高效率。当访问的页面不在内存中时，会发生缺页中断，触发操作系统加载该页。定义了诸如RSS（物理内存使用量）和VSZ（分配的总虚拟内存）等指标。

最后，文章详细介绍了虚拟内存布局，概述了内核空间、堆栈、内存映射区域、堆和代码/数据段等段。文章提供了有关堆栈分配的详细信息，解释了它如何随着函数调用而增长和缩小，以及堆栈指针的作用。文章还涉及了线程堆栈、它们的默认大小以及相关的系统调用。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 2 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 3 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 4 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 5 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 6 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 7 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 8 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 9 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 10 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 11 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 12 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 13 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 14 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 15 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 16 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 17 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 18 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 19 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 20 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 21 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 22 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 23 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 24 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 25 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 26 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 27 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 28 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 29 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 30 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 31 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 32 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 33 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 34 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 35 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 36 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 37 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 38 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 39 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 40 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 41 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 42 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 43 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 44 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 45 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 46 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 47 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 48 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 49 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 50 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 51 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 52 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 53 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 54 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 55 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 56 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 57 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 58 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 59 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 60 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 61 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 62 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 63 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 64 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 65 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 66 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 67 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 68 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 69 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 70 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 71 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 72 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 73 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 74 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 75 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 76 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 77 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 78 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 79 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 80 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 81 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 82 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 83 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 84 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 85 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 86 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 87 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 88 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 89 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 90 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 91 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 92 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 93 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 94 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 95 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 96 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 97 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 98 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 99 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 100 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 101 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 102 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 103 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 104 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 105 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 106 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 107 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 108 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 109 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 110 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 111 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 112 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 113 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 114 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 115 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 116 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 117 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 118 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 119 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 120 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 121 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 122 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 123 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 124 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 125 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 126 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 127 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 128 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 129 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 130 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 131 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 132 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 133 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 134 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 135 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 136 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 137 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 138 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 139 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 140 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 141 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 142 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 143 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 144 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 145 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 146 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 147 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 148 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 149 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 150 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 151 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 152 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 153 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 154 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 155 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 156 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 157 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 158 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 159 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 160 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 161 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 162 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 163 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 164 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 165 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 166 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 167 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 168 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 169 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 170 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 171 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 172 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 173 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 174 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 175 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 176 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 177 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 178 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 179 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 180 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 181 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 182 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 183 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 184 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 185 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 186 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 187 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 188 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 189 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 190 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 191 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 192 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
