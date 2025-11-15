# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-15.md)

*最后自动更新时间: 2025-11-15 17:44:01*
## 1. 富士通 Lifebook U729 上的 Linux

**原文标题**: Linux on the Fujitsu Lifebook U729

**原文链接**: [https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729](https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729)

本文详细介绍了作者在翻新的富士通 Lifebook U729 上使用 Linux 的体验。作者称赞这款笔记本电脑是一款令人愉快且功能强大的 Linux 设备，并强调了其小巧的尺寸、轻巧的设计、坚固的构建质量、良好的键盘以及开箱即用的硬件兼容性。

主要挑战是禁用 Secure Boot，该选项最初在 BIOS 中显示为灰色。作者通过以下方式解决了这个问题：首先安装 Windows 11（预装），通过 Windows Update 更新富士通特定的驱动程序，然后使用富士通提供的 DeskUpdate 工具更新 BIOS。更新后的 BIOS 启用了禁用 Secure Boot 的选项。

作者还在 BIOS 中发现并禁用了“Absolute Persistence”企业间谍软件。

本文证实，Wi-Fi、蓝牙、声音（使用 PipeWire）、显示屏亮度控制、触摸屏和网络摄像头都可以在 Linux（特别是 NixOS）上完美运行，无需额外配置。麦克风和指纹传感器未经测试。

最后，作者提供了有关启动时访问 BIOS (F2) 和启动菜单 (F12) 的说明。文章最后提供了指向富士通产品页面和数据表的链接。

---

## 2. 对Archive.today可疑压力的调查

**原文标题**: Our investigation into the suspicious pressure on Archive.today

**原文链接**: [https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html](https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html)

本文详细调查了一起针对Archive.today的可疑压力事件。AdGuard DNS（一项允许用户绕过付费墙的服务）收到了一个名为“Web Abuse Association Defense”（WAAD，网络滥用协会防御）的新成立的法国组织的联系，该组织声称致力于打击儿童色情。WAAD要求AdGuard屏蔽Archive.today，理由是其拒绝删除非法内容。

AdGuard认为这一要求很奇怪，并经过进一步调查，发现了不一致之处。WAAD的网站缺乏细节，其在线存在感极低，并且其声明的时间线与提供的“法警报告”不符。Archive.today迅速删除了被标记的内容，并表示他们之前没有收到过相关通知。他们还暗示存在“连续”投诉活动。

调查显示，WAAD的注册时间很短，并且很容易匿名进行。“法警报告”被WAAD用作证据，但大多数都是最近创建的，而不是像WAAD声称的那样在2023年创建的。2023年的两份报告与一位真正的律师有关，WAAD似乎冒充了他。

AdGuard得出结论，这些投诉非常可疑，可能是为了损害Archive.today而精心策划的，并且可能冒充了真实的人物。他们强调，法国法律会惩罚虚假报告。AdGuard将向法国警方提起正式投诉，理由是存在潜在的犯罪行为。这项调查恰逢有关FBI正在调查Archive.today所有者的报道，可能与CSAM有关，这增加了可疑的情况。

---

## 3. 适用于 Windows 11 的 Windhawk Windows 经典主题修改

**原文标题**: Windhawk Windows classic theme mod for Windows 11

**原文链接**: [https://windhawk.net/mods/classic-theme-enable](https://windhawk.net/mods/classic-theme-enable)

本文可能讨论一个使用Windhawk修改Windows 11的mod，旨在恢复或模拟经典Windows主题。由于仅显示“WindhawkYou need to enable JavaScript to run this app.”，表明文章的实际内容，可能是代码、说明或进一步解释，被隐藏，需要启用JavaScript才能查看。

核心思想是：**存在（或正在展示）一个Windhawk mod，旨在Windows 11中重现经典Windows主题的外观和感觉。** 启用JavaScript后可能才能访问该文章。

---

## 4. 最小化方差的平均加权

**原文标题**: Weighting an average to minimize variance

**原文链接**: [https://www.johndcook.com/blog/2025/11/12/minimum-variance/](https://www.johndcook.com/blog/2025/11/12/minimum-variance/)

本文探讨了如何在多个独立资产间进行最优投资配置以最小化投资组合波动性的问题。首先以两个资产A和B（A波动性更大）为例，证明了将两者混合，并向波动性较小的资产B倾斜是最佳策略。本文推导出了资产X（波动性较大的资产）的最优配置权重`t`，其基于X和Y（波动性较小的资产）的方差：`t = Var(Y) / (Var(X) + Var(Y))`。这表明Y的方差越小，X的配置越少。

然后，问题被推广到`n`个独立资产（Xi）。使用拉格朗日乘数法，本文得出了每个资产的最优配置权重`ti`的公式：`ti = 1/Var(Xi) / (Σ 1/Var(Xj))`，其中求和是对所有`j`从1到`n`进行的。该公式表明，每个资产的最优权重与其方差成反比，并由所有资产的逆方差之和进行归一化。分母被称为n个变量中的第(n-1)个基本对称多项式。本质上，为了最小化方差，应将更多的资金配置给波动性较低的资产。

---

## 5. 野兽的本性：夏尔·勒布伦的人兽混合体 (1806)

**原文标题**: The Nature of the Beast: Charles Le Brun's Human-Animal Hybrids (1806)

**原文链接**: [https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/](https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/)

野兽的本性：夏尔·勒布伦的人兽混合体（1806）

---

## 6. TCP，互联网的基石

**原文标题**: TCP, the workhorse of the internet

**原文链接**: [https://cefboud.com/posts/tcp-deep-dive-internals/](https://cefboud.com/posts/tcp-deep-dive-internals/)

本文阐述了TCP（传输控制协议）作为互联网“主力军”的重要性，它能够在底层网络不可靠的情况下实现可靠的数据传输。TCP在传输层运行，通过处理重传、校验和及其他可靠性机制，使开发者免受丢包、损坏、重复和重排序等问题的困扰。

本文重点介绍了流量控制，它可以防止接收方缓冲区溢出，以及拥塞控制，它可以防止网络崩溃。文中展示了一个用C语言编写的基本TCP服务器，用于回显客户端输入，以及一个使用TCP的简单HTTP服务器。

本文深入探讨了TCP段的结构，解释了关键字段，如源/目标端口、序列号和确认号（用于可靠性）以及标志位（SYN、ACK、FIN、RST用于连接管理）。序列号和确认号对于按顺序重组数据包至关重要。这些标志位用于创建、维护和关闭TCP连接。最后，校验和确保了数据完整性，窗口大小是流量控制的主要方法。

本文最后强调了互联网的卓越可靠性，这得益于致力于其开发和持续改进的个人。

---

## 7. Trellis AI (YC W24) 招聘：简化获取救生疗法的途径

**原文标题**: Trellis AI (YC W24) Is Hiring: Streamline access to life-saving therapies

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time)

Trellis AI (YC W24)，一家从斯坦福人工智能实验室分离出来的公司，正在招聘一名前置部署工程师，以帮助简化获取救生疗法的途径。 他们构建人工智能代理来自动化医疗保健文书工作，如文件录入、事先授权和申诉，影响遍及美国所有 50 个州的患者。该公司由 YC、General Catalyst 等机构投资。

该职位涉及为医疗保健决策设计和实施人工智能系统，构建 24/7 全天候人工智能同事，以及开发具有强大评估框架的生产级人工智能系统。 他们希望招聘具备全栈经验、精通 Python、Go 和 ML/NLP 库，具有数据库经验，以及积极主动、快速学习态度的人才。 具有云平台经验和开源贡献者优先。

Trellis 的目标是成为“医疗保健账单领域的 Stripe”，通过消除服务前文书工作，帮助供应商更快地治疗更多患者。 他们将治疗时间缩短 90% 以上，提高批准和报销率，并提高药物项目的绩效。 该公司在过去几个月中实现了 10 倍的收入增长，并声称在其细分市场中占据了相当大的市场份额。 团队由高成就者组成，并强调实际影响、客户参与和极致所有权。

---

## 8. 强大的单纯形 (2023)

**原文标题**: The Mighty Simplex (2023)

**原文链接**: [https://galileo-unbound.blog/2023/05/03/the-mighty-simplex/](https://galileo-unbound.blog/2023/05/03/the-mighty-simplex/)

强大的单纯形
探讨了单纯形在几何学、材料科学、机器学习和优化等各个领域的重要性和应用。文章强调了单纯形作为基本几何结构的简洁性、对称性和高效性。文章首先将d维单纯形定义为具有d+1个顶点的图形，并重点介绍了正单纯形（等边）及其性质。

随后，文章深入探讨了实际应用，展示了如何使用重心坐标表示合金成分、晶体学取向，以及使用复制方程建模生态系统动力学。文章还讨论了用于线性规划的Dantzig单纯形算法，该算法通过在多面体的顶点之间迭代移动来找到最优解。

最后，文章介绍了Nelder-Mead（变形虫）算法，这是一种非线性最小化技术，它使用动态调整的单纯形在超空间中“爬行”，寻找非线性目标函数的最小值。作者强调了单纯形在不同学科中的多功能性和重要性，将其描绘成一种用于表示、分析和优化的强大工具。

---

## 9. 人工智能世界时钟

**原文标题**: AI World Clocks

**原文链接**: [https://clocks.brianmoore.com/](https://clocks.brianmoore.com/)

AI世界时钟是一个网站，每分钟展示由九个不同AI模型生成的模拟时钟。该网站的创建者Brian Moore受到了Matthew Rayfield的启发。

每个AI模型都会收到提示：“创建显示${time}的模拟时钟的HTML/CSS。如果需要，可以包含数字（或数字符号），并设置CSS动画秒针。使其具有响应性并使用白色背景。仅返回HTML/CSS代码，不包含Markdown格式。” 它们被赋予2000个tokens来完成此请求。

该网站显示这些AI生成的时钟，每分钟更新一次。目前处于“加载中...”和“生成AI时钟中...”的状态，表明时钟正在积极生成。Brian Moore也可以在Instagram上找到。

---

## 10. 戏弄爬虫机器人

**原文标题**: Messing with scraper bots

**原文链接**: [https://herman.bearblog.dev/messing-with-bots/](https://herman.bearblog.dev/messing-with-bots/)

对抗恶意爬虫：一项实验报告

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 2 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 3 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 4 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 5 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 6 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 7 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 8 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 9 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 10 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 11 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 12 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 13 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 14 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 15 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 16 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 17 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 18 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 19 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 20 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 21 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 22 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 23 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 24 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 25 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 26 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 27 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 28 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 29 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 30 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 31 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 32 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 33 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 34 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 35 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 36 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 37 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 38 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 39 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 40 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 41 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 42 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 43 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 44 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 45 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 46 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 47 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 48 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 49 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 50 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 51 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 52 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 53 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 54 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 55 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 56 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 57 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 58 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 59 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 60 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 61 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 62 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 63 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 64 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 65 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 66 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 67 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 68 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 69 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 70 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 71 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 72 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 73 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 74 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 75 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 76 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 77 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 78 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 79 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 80 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 81 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 82 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 83 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 84 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 85 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 86 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 87 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 88 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 89 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 90 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 91 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 92 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 93 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 94 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 95 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 96 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 97 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 98 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 99 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 100 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 101 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 102 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 103 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 104 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 105 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 106 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 107 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 108 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 109 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 110 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 111 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 112 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 113 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 114 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 115 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 116 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 117 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 118 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 119 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 120 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 121 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 122 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 123 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 124 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 125 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 126 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 127 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 128 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 129 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 130 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 131 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 132 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 133 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 134 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 135 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 136 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 137 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 138 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 139 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 140 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 141 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 142 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 143 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 144 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 145 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 146 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 147 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 148 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 149 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 150 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 151 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 152 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 153 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 154 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 155 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 156 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 157 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 158 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 159 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 160 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 161 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 162 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 163 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 164 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 165 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 166 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 167 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 168 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 169 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 170 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 171 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 172 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 173 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 174 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 175 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 176 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 177 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 178 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 179 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 180 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 181 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 182 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 183 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 184 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 185 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 186 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 187 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 188 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 189 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 190 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 191 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 192 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 193 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 194 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 195 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 196 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 197 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 198 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 199 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 200 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 201 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 202 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 203 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 204 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 205 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 206 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 207 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 208 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 209 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 210 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 211 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 212 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 213 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 214 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 215 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 216 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 217 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 218 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 219 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 220 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 221 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 222 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 223 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 224 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 225 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 226 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 227 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 228 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 229 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 230 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 231 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 232 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 233 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 234 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 235 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 236 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 237 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 238 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 239 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 240 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
