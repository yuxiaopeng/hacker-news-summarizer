# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-12.md)

*最后自动更新时间: 2026-05-12 19:23:20*
## 1. Google 图书

**原文标题**: Googlebook

**原文链接**: [https://googlebook.google/](https://googlebook.google/)

谷歌正在推出名为“Googlebook”的全新高级笔记本电脑系列，将人工智能作为其核心特色。该系列以“智能即新规格”为口号，专注于集成 **Gemini AI** 以提升生产力和创造力。

重点功能包括：
*   **Magic Pointer：** 一款 AI 工具，允许用户选取屏幕上的任何内容，从而即时提问、对比信息或生成内容。
*   **自定义小组件：** 用户只需使用自然语言提示即可构建个性化小组件。
*   **Android 集成：** 这些笔记本电脑被设计为 Android 手机的“完美拍档”。其中包括无需安装即可在电脑上运行移动应用的“应用投屏 (Cast My Apps)”，以及能像管理本地文件一样管理手机文件的“快速访问 (Quick Access)”。

硬件方面，该系列拥有“轻盈设计”与“强悍动力”，完美平衡了便携性与高性能。产品定于**秋季发布**，谷歌目前正邀请感兴趣的用户订阅通知，以获取最新的发布动态。

---

## 2. CERT 发布 dnsmasq 中六个严重安全漏洞的 CVE

**原文标题**: CERT is releasing six CVEs for serious security vulnerabilities in dnsmasq

**原文链接**: [https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html)

2026年5月11日，Simon Kelley 宣布 CERT 正发布六个 CVE 漏洞，以修复 **dnsmasq** 中严重的长期安全漏洞。这些缺陷影响了该软件几乎所有的现代版本。

为解决这些漏洞，Kelley 发布了 **2.92rel2 版本**，其中包含即时补丁。虽然已预先通知供应商以便及时更新软件包，但相关细节和补丁也已在 dnsmasq 官方网站上公开。

该公告强调了安全格局的变化，指出 AI 生成的漏洞报告和基于 AI 的安全研究正形成一股“海啸”。这种涌入迫使策略发生转变，转而优先考虑快速公开修复，而非长期的披露禁运，因为“正邪”双方识别漏洞的速度都在加快。

未来的关键步骤包括：
*   **2.93rc1 版本：** 将立即标记一个候选版本供社区测试。
*   **2.93 稳定版：** 计划在一周内发布完整的稳定版本，对受影响的代码进行更全面的重写。
*   **持续维护：** 鉴于 AI 驱动的报告量巨大，Kelley 预计这种高频安全补丁周期将会持续。

建议用户立即更新至 2.92rel2 版本或供应商提供的补丁版本，并协助测试 2.93 候选版本，以确保更持久的修复方案能够稳定发布。

---

## 3. Why senior developers fail to communicate their expertise

**原文标题**: Why senior developers fail to communicate their expertise

**原文链接**: [https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise)

生成摘要时出错

---

## 4. 渲染天空、日落与行星

**原文标题**: Rendering the Sky, Sunsets, and Planets

**原文链接**: [https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/)

本文探讨了大气散射着色器的技术实现，用于实时渲染逼真的天空、日落和行星外壳。受 NASA 图像的启发，作者详细介绍了从简单渐变到基于物理的体积方法的探索历程。

该渲染技术的核心是**光线步进 (raymarching)**，通过在不同高度采样大气密度，来计算光线沿视线方向被重新定向（散射）或损失（透射）的情况。其实现依赖于三个核心构建模块：

1.  **瑞利散射 (Rayleigh Scattering)**：模拟光与微小空气分子的相互作用，解释了天空呈现蓝色的原因（短波长散射更强），以及随着高空大气变薄，天空如何过渡到深邃的黑色。
2.  **米氏散射 (Mie Scattering)**：考虑了灰尘和气溶胶等较大的颗粒，产生了太阳周围特有的朦胧光辉或“光晕”。
3.  **臭氧吸收 (Ozone Absorption)**：模拟臭氧层对特定波长的吸收，从而加深天空的蓝色，并在薄暮和日落时分增添独特的紫色调。

为了实现逼真的光照效果，作者引入了**光步进 (light-marching)**。这种嵌套循环计算了光线从太阳传播到特定采样点过程中的损耗，从而实现了日出和日落时动态的色彩变化。

最后，文章解释了如何将这些原理转化为一种**后处理效果**。通过从场景的深度缓冲中重建世界空间坐标，着色器可以将大气渲染为环绕行星的体积壳，或在 3D 场景中提供大气雾效。作者在结尾指出，出于性能考虑，可以参考 Sebastian Hillaire 的研究，利用查找表 (LUT) 来优化复杂的模型。

---

## 5. Dead.Letter (CVE-2026-45185) – XBOW 如何在 Exim 中发现未经身份验证的 RCE

**原文标题**: Dead.Letter (CVE-2026-45185) – How XBOW found an unauthenticated RCE on Exim

**原文链接**: [https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim](https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim)

XBOW最近披露了CVE-2026-45185，这是Exim邮件服务器中的一个关键未授权远程代码执行（RCE）漏洞。这一发现之所以特别引人注目，是因为它是通过自主漏洞利用开发工具识别出来的。

**技术缺陷**
该漏洞是一个释放后重用（UAF）漏洞，发生在Exim使用GnuTLS库（Ubuntu等基于Debian的系统的默认配置）处理TLS连接时。该漏洞在TLS关闭期间触发：
1. Exim释放其TLS传输缓冲区（`xfer_buffer`）。
2. 然而，由于Exim处理BDAT（分块）命令的方式，一个嵌套的接收包装器仍处于激活状态。
3. 随后调用的 `ungetc()` 会将一个换行符（`\n`）写入已释放的内存区域。

虽然单字节写入看起来微不足道，但它恰好落在了Exim分配器的元数据上。这种损坏允许攻击者操纵堆的内部结构，最终将该漏洞原语提升为完全的远程代码执行。

**重要性与影响**
该漏洞被认为是高等级的，因为它几乎不需要对目标服务器进行任何特殊配置，影响了Ubuntu 24.04 LTS等主流发行版中Exim 4.97的默认安装。

**研究叙述**
除了技术细节，本文还强调了安全研究的转变。作者作为资深的漏洞利用开发人员，利用XBOW在一个从未亲自审计过的代码库中发现并武器化了该缺陷。这证明了大语言模型和自主代理在识别传统方法可能遗漏的、具有“全球影响力”的复杂漏洞方面，效能正日益增强。

---

## 6. 重新构想 AI 时代的鼠标指针

**原文标题**: Reimagining the mouse pointer for the AI era

**原文链接**: [https://deepmind.google/blog/ai-pointer/](https://deepmind.google/blog/ai-pointer/)

在《重新想象 AI 时代的鼠标指针》一文中，研究员 Adrien Baranes 和 Rob Marchant 概述了用户界面设计的一种转变：从被动式光标转向由 Gemini 驱动的 AI 指针。其目标是通过将智能直接整合到用户的工作流中，消除“AI 绕路”——即用户必须将数据复制粘贴到独立的 AI 窗口中的操作。

这一重新设计遵循四个核心原则：
1.  **保持流畅感 (Maintain the Flow)**：AI 功能可在所有应用程序中运行，让用户无需切换应用即可完成总结 PDF 或创建图表等任务。
2.  **直观指引 (Show and Tell)**：指针能捕捉视觉和语义上下文，让计算机能够“看见”用户所指的内容，从而消除对详细文字提示的需求。
3.  **拥抱“这个”与“那个” (Embrace "This" and "That")**：通过将指向操作与语音或简单指令相结合，用户可以使用自然的简略语（如“把这个移到那里”）来完成复杂的请求。
4.  **将像素转化为可操作实体 (Turn Pixels into Actionable Entities)**：AI 可以识别像素中的对象，将静态图像转化为交互式数据，例如将一张餐厅照片转化为预订链接。

谷歌已经开始将这些概念整合到其生态系统中。**Chrome** 用户现在可以使用指针向 Gemini 询问特定的网页元素，例如对比产品。此外，即将推出的 **Googlebook** 笔记本电脑将配备 **“魔法指针” (Magic Pointer)**，以提供直观的系统级 AI 辅助。通过让技术适应人类行为，而不是强迫用户去适应工具，这种新型指针旨在让 AI 协作变得无缝且流畅。

---

## 7. Obsidian 插件的未来

**原文标题**: The Future of Obsidian Plugins

**原文链接**: [https://obsidian.md/blog/future-of-plugins/](https://obsidian.md/blog/future-of-plugins/)

Obsidian 推出了 **Obsidian Community**，这是一个全新的中心化目录和开发者仪表盘，旨在优化其拥有超过 4,000 个插件和主题的生态系统的发现、管理和安全性。

**此次发布的主要功能包括：**

*   **开发者仪表盘：** 作者现在可以通过连接其 GitHub 账号来认领现有项目或提交新项目。这实现了更快的提交速度并能实时追踪项目状态。
*   **自动化审核：** 为了解决日益严重的待审积压问题，Obsidian 引入了自动化系统，扫描每个版本的插件是否存在安全漏洞、恶意软件和代码质量问题。该系统已处理了超过 2,300 份排队提交，显著缩短了等待时间。人工审核将继续针对高知名度或被标记的项目进行。
*   **增强的发现与安全性：** 新网站为每个项目提供了改进的搜索、筛选功能和“安全评分卡”。用户现在可以清晰地看到**免费、付费或可选付费**插件的标签，以及经过验证的集成的“官方”徽章。
*   **提高透明度：** 在接下来的几个月里，插件将被要求披露对网络和文件系统等敏感权限的访问。Obsidian 还计划引入已认证作者标签，以建立社区信任。
*   **团队工具：** 官方正在开发新功能，以帮助组织管理许可插件，并向团队成员分发私有工具。

虽然目前未能通过新自动化检查的现有插件会获得临时豁免，但如果它们不进行更新以符合新标准，最终将被逐步淘汰。总体而言，随着平台的不断发展，该举措为 Obsidian 生态系统奠定了可扩展的基础，并优先考虑了用户安全和开发者效率。

---

## 8. When life gives you lemons, write better error messages

**原文标题**: When life gives you lemons, write better error messages

**原文链接**: [https://wix-ux.com/when-life-gives-you-lemons-write-better-error-messages-46c5223e1a2f](https://wix-ux.com/when-life-gives-you-lemons-write-better-error-messages-46c5223e1a2f)

生成摘要时出错

---

## 9. Bambu Lab is abusing the open source social contract

**原文标题**: Bambu Lab is abusing the open source social contract

**原文链接**: [https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/)

This article criticizes Bambu Lab for allegedly violating the "open source social contract" by threatening legal action against the developer of **OrcaSlicer-bambulab**, a small fork of the open-source OrcaSlicer software. 

The conflict centers on Bambu Lab’s shift toward a cloud-dependent ecosystem. The specific fork in question allowed power users to access printer features without routing data through Bambu’s servers. Bambu Lab issued a cease-and-desist, publicly accusing the developer of using "impersonation attacks" to bypass security and potentially destabilizing their infrastructure. 

The author and the developer defend the fork, noting that it uses the same **AGPLv3-licensed code** found in Bambu’s own Linux client. They argue that Bambu is mischaracterizing standard open-source practices as malicious hacking. The author highlights the irony of Bambu’s stance, given that their own software is a fork of PrusaSlicer (which is itself a fork of Slic3r). 

Key points include:
*   **Privacy Concerns:** The author highlights the frustration of users who want to own their hardware without mandatory cloud connectivity or telemetry.
*   **Legal Aggression:** Bambu Lab is accused of using its "legal might" to suppress a tiny developer rather than addressing their own architectural vulnerabilities.
*   **Community Backlash:** High-profile figures like Louis Rossmann have offered financial support to the developer to fight the legal threats.

The article concludes that Bambu Lab fails to understand open-source culture and suggests that the best way for users to demand change is to purchase 3D printers from competing companies that prioritize local control and open-source principles.

---

## 10. Instructure pays ransom to Canvas hackers

**原文标题**: Instructure pays ransom to Canvas hackers

**原文链接**: [https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 2 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 3 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 4 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 5 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 6 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 7 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 8 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 9 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 10 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 11 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 12 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 13 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 14 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 15 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 16 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 17 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 18 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 19 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 20 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 21 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 22 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 23 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 24 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 25 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 26 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 27 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 28 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 29 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 30 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 31 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 32 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 33 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 34 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 35 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 36 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 37 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 38 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 39 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 40 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 41 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 42 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 43 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 44 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 45 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 46 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 47 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 48 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 49 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 50 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 51 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 52 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 53 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 54 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 55 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 56 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 57 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 58 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 59 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 60 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 61 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 62 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 63 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 64 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 65 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 66 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 67 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 68 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 69 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 70 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 71 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 72 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 73 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 74 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 75 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 76 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 77 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 78 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 79 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 80 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 81 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 82 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 83 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 84 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 85 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 86 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 87 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 88 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 89 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 90 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 91 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 92 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 93 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 94 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 95 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 96 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 97 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 98 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 99 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 100 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 101 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 102 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 103 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 104 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 105 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 106 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 107 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 108 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 109 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 110 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 111 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 112 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 113 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 114 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 115 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 116 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 117 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 118 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 119 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 120 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 121 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 122 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 123 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 124 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 125 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 126 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 127 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 128 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 129 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 130 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 131 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 132 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 133 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 134 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 135 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 136 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 137 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 138 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 139 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 140 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 141 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 142 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 143 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 144 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 145 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 146 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 147 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 150 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 151 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 152 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 153 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 154 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 155 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 156 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 157 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 158 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 159 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 160 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 161 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 162 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 163 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 164 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 165 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 166 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 167 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 168 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 169 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 170 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 171 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 172 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 173 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 174 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 175 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 176 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 177 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 178 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 179 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 180 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 181 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 182 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 183 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 184 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 185 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 186 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 187 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 188 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 189 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 190 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 191 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 192 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 193 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 194 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 195 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 196 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 197 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 198 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 199 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 200 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 201 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 202 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 203 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 204 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 205 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 206 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 207 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 208 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 209 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 210 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 211 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 212 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 213 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 214 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 215 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 216 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 217 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 218 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 219 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 220 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 221 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 222 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 223 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 224 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 225 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 226 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 227 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 228 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 229 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 230 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 231 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 232 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 233 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 234 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 235 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 236 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 237 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 238 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 239 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 240 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 241 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 242 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 243 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 244 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 245 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 246 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 247 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 248 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 249 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 250 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 251 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 252 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 253 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 254 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 255 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 256 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 257 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 258 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 259 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 260 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 261 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 262 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 263 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 264 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 265 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 266 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 267 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 268 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 269 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 270 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 271 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 272 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 273 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 274 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 275 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 276 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 277 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 278 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 279 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 280 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 281 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 282 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 283 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 284 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 285 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 286 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 287 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 288 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 289 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 290 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 291 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 292 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 293 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 294 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 295 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 296 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 297 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 298 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 299 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 300 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 301 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 302 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 303 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 304 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 305 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 306 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 307 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 308 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 309 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 310 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 311 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 312 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 313 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 314 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 315 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 316 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 317 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 318 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 319 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 320 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 321 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 322 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 323 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 324 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 325 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 326 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 327 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 328 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 329 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 330 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 331 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 332 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 333 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 334 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 335 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 336 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 337 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 338 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 339 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 340 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 341 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 342 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 343 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 344 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 345 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 346 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 347 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 348 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 349 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 350 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 351 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 352 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 353 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 354 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 355 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 356 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 357 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 358 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 359 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 360 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 361 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 362 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 363 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 364 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 365 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 366 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 367 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 368 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 369 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 370 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 371 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 372 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 373 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 374 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 375 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 376 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 377 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 378 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 379 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 380 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 381 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 382 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 383 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 384 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 385 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 386 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 387 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 388 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 389 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 390 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 391 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 392 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 393 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 394 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 395 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 396 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 397 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 398 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 399 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 400 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 401 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 402 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 403 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 404 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 405 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 406 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 407 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 408 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 409 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 410 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 411 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 412 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 413 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 414 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 415 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 416 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 417 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 418 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
