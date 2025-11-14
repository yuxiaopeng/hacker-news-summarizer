# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-14.md)

*最后自动更新时间: 2025-11-14 17:50:23*
## 1. I think nobody wants AI in Firefox, Mozilla

**原文标题**: I think nobody wants AI in Firefox, Mozilla

**原文链接**: [https://manualdousuario.net/en/mozilla-firefox-window-ai/](https://manualdousuario.net/en/mozilla-firefox-window-ai/)

本文探讨了Mozilla计划将内置AI助手“Window AI”作为第三种浏览模式（与普通标签页和隐私标签页并列）集成到Firefox中的方案。尽管细节有限，但它似乎比现有侧边栏访问第三方聊天机器人更深入地实施了AI。Mozilla强调该功能将是可选的，并由用户控制。

然而，受邀“塑造”该计划的志愿者们的早期反应却出乎意料地消极，最初的52个论坛回复全部拒绝这一想法，并要求Mozilla放弃AI集成。

作者质疑Mozilla的战略，认为与已经确立了AI赋能浏览器地位并且用户更容易接受AI功能的大型科技公司和初创公司竞争是一个挑战。Mozilla的目标是同时满足AI爱好者和那些更喜欢无AI体验的用户，提供对AI集成的用户控制。作者认为，这种方法可能试图取悦所有人，但可能不会成功。

最后，文章指出，反对Firefox中AI集成的用户可以选择替代的“无AI”Firefox分支，如LibreWolf、Waterfox或Zen Browser。

---

## 2. Incus-OS：运行 Incus 作为虚拟机监控器的不可变 Linux 操作系统

**原文标题**: Incus-OS: Immutable Linux OS to run Incus as a hypervisor

**原文链接**: [https://linuxcontainers.org/incus-os/](https://linuxcontainers.org/incus-os/)

IncusOS 是一款不可变的 Linux 操作系统，专门设计用于以 Incus 作为虚拟机管理程序运行。它通过 UEFI 安全启动、TPM 2.0 测量和全盘加密等功能，优先考虑安全性和可靠性。更新采用 A/B 分区方案原子性地应用，以便在出现问题时轻松回滚。系统已锁定，没有本地或远程 shell 访问权限，管理完全通过经过身份验证的 REST API 处理。

主要功能包括自动 ZFS 池创建，支持各种存储技术（光纤通道、NVME-over-TCP、iSCSI、集群 LVM、Ceph）以及高级网络功能，如支持 VLAN 的桥接、链路聚合、LLDP 以及对代理服务器和 Tailscale 的支持。

IncusOS 基于 Debian 13 构建，采用定制的 Incus 和内核版本，并利用 systemd 进行镜像创建、更新和 TPM 支持的磁盘加密。它提供稳定和测试更新通道，自动更新每 6 小时进行一次，或可自定义周期。稳定通道每周更新一次，而测试通道每天更新。IncusOS 还可以用作运营中心和迁移管理器的操作系统。

开发在 GitHub 上以 Apache 2.0 许可证开源，利用 mkosi 进行镜像构建，并使用 Go 进行操作系统管理。

---

## 3. AGI幻想阻碍实际工程

**原文标题**: AGI fantasy is a blocker to actual engineering

**原文链接**: [https://www.tomwphillips.co.uk/2025/11/agi-fantasy-is-a-blocker-to-actual-engineering/](https://www.tomwphillips.co.uk/2025/11/agi-fantasy-is-a-blocker-to-actual-engineering/)

本文认为，对通用人工智能（AGI）的追求，尤其是受到大型语言模型（LLM）的成功以及OpenAI等机构人物信念的推动，正在阻碍真正的技术进步。作者认为，“AGI幻想”为环境破坏和伦理上有问题的行为辩护，例如大规模数据中心建设和对数据工作者的剥削。

核心论点是，源于“纯语言”假设的对AGI的信念，驱动了一种以规模为中心的策略，将计算能力和数据获取置于一切之上。反过来，这种策略导致不可持续的资源消耗并将成本外部化到社会和环境。作者批评了用于为AGI开发辩护的期望值（EV）计算，称其为“无稽之谈”，因为所涉及的价值观和概率是主观的且无法证伪的。

作者主张，与其将AGI作为万灵药来追求，不如采取更务实、工程驱动的方法。这包括评估LLM和其他生成模型以解决特定的、定义明确的问题，并进行适当的成本效益分析。它还建议探索替代解决方案，例如更小、专门构建的生成模型，甚至判别模型，以最大限度地减少资源消耗和伦理问题。本质上，作者呼吁将人工智能开发的重点从宏大、推测性的AGI愿景转变为以解决问题为中心的思维模式。

---

## 4. Honda: 2 years of ml vs 1 month of prompting - heres what we learned

**原文标题**: Honda: 2 years of ml vs 1 month of prompting - heres what we learned

**原文链接**: [https://www.levs.fyi/blog/2-years-of-ml-vs-1-month-of-prompting/](https://www.levs.fyi/blog/2-years-of-ml-vs-1-month-of-prompting/)

本田的分析部门传统上使用SQL进行保修索赔分类，但由于索赔描述中语言的不断演变而面临局限性。 2023年启动了一个多年项目，旨在通过监督机器学习模型实现此过程的自动化。 初期阶段包括数月的数据收集和成千上万索赔的手动标记，随后花了六个月时间构建一个复杂的9阶段预处理流程。 建模工作主要集中在使用XGBoost的TF-IDF。 然而，生产部署方面的挑战、数据稀缺以及不断变化的优先级促使团队探索大型语言模型（LLM）。

最初尝试使用GPT-3.5令人失望，但LLM的进步促使重新评估。 经过与现有XGBoost模型进行基准测试后，Nova Lite成为最具成本效益的LLM。 通过结构化的提示调优过程，包括评估、推理分析以及使用更大的LLM进行迭代改进，Nova Lite在5个索赔类别中的4个类别中达到或略微超过了监督式XGBoost模型。

关键在于，LLM已将约束从数据可用性和标注周期转移到提示工程。 虽然监督模型仍然适用于稳定目标和丰富数据，但对于具有不断演变的分类标准、稀缺数据或快速变化的需求的领域，LLM提供了一种灵活且更快的解决方案。 LLM的成功集成使本田能够替换整个流程，而不仅仅是一个模型，从而实现更快，更高效的保修索赔分类。

---

## 5. Magit 手册已恢复在线访问。

**原文标题**: Magit manuals are available online again

**原文链接**: [https://github.com/magit/magit/issues/5472](https://github.com/magit/magit/issues/5472)

此GitHub issue (#5472)报告 Magit 网站 magit.vc 和 emacsair.me 宕机。报告者 ador 是 Magit 新手，想在线访问教程，但网站无法访问。该 issue 于 2025 年 11 月 4 日开启。页面显示错误“加载时出错。请重新加载此页面”，表明问题可能仍在持续。它还包含标准的 GitHub 元素，例如 fork 数量 (842) 和 star 数量 (6.9k)、需要登录的通知设置，以及用于指定负责人、标签、项目、里程碑、关系和与 issue 相关的开发活动的版块。该 issue 收到了来自 bo0ts、drichardson、tasmo 和 mynameismon 的 4 个赞 (thumbs up)。总体问题是 Magit 在线文档无法访问。

---

## 6. EDE：小型快速桌面环境（2014）

**原文标题**: EDE: Small and Fast Desktop Environment (2014)

**原文链接**: [https://edeproject.org/](https://edeproject.org/)

This article introduces EDE (Equinox Desktop Environment), a desktop environment designed for speed and low resource usage. Key features include its responsiveness and familiar user interface. EDE is compatible with various operating systems, including Linux, BSD variants, Solaris, Minix, Zaurus, and even XBox. The article provides a link to download version 2.1 and access older releases. It also highlights recent activity, mentioning resolved Bugzilla issues and a "Autumn cleanup" blog post. Finally, it provides links to the EDE homepage, news archive, about page, gallery, wiki, and a bug reporting page, offering users resources for further exploration and engagement with the project.


---

## 7. RetailReady (YC W24) 正在招聘

**原文标题**: RetailReady (YC W24) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/retailready/jobs/kGHAith-support-engineer](https://www.ycombinator.com/companies/retailready/jobs/kGHAith-support-engineer)

RetailReady (YC W24) 招聘驻旧金山技术支持工程师。RetailReady 是一家人工智能驱动的供应链合规引擎公司，已完成 YC 后的 330 万美元种子轮融资，并签约了超过 15 家企业客户，目前正在扩大运营规模。RetailReady 通过 EDI、API 和平面文件与仓库运营集成，实现零售供应链合规要求的自动化。

技术支持工程师将成为客户问题的首要联系人，负责解决问题、上报错误，并为内部使用和 AI 支持模型培训创建文档。该职位要求早起，愿意在早上 5 点到下午 2 点亲自上班，以支持美国东海岸的客户。

理想的候选人应以客户为中心、具有分析能力、注重细节，并能熟练调试日志、API 和数据映射。拥有技术学位以及具备供应链或知识库维护经验者优先考虑。

该职位提供在一家快速增长、获得 YC 支持的初创公司从零开始的机会，有机会对实时仓库运营产生实际影响，以及协作的团队环境。薪酬包括 10 万至 14 万美元的工资、0.04%-0.20% 的股权、全面的健康保险和无限 PTO。面试流程包括与联合创始人的简短面试、支持场景小组讨论以及与团队的现场访问。

---

## 8. 甲骨文因人工智能押注在华尔街科技股抛售中遭受重创

**原文标题**: Oracle hit hard in Wall Street's tech sell-off over its AI bet

**原文链接**: [https://www.ft.com/content/583e9391-bdd0-433e-91e0-b1b93038d51e](https://www.ft.com/content/583e9391-bdd0-433e-91e0-b1b93038d51e)

甲骨文股价大幅下跌，受华尔街科技股抛售潮影响。文章暗示此次下跌与投资者对甲骨文“巨额人工智能赌注”的担忧有关。《金融时报》的文章随后引导读者订阅以解锁更多细节。订阅选项包括FT Edit的有限访问权限以及Premium Digital的完整报道，每种都提供不同级别的FT新闻访问权限。 未订阅的情况下，无法从文本中获得对人工智能赌注担忧的具体原因。文章强调了FT新闻的价值，并鼓励读者探索其订阅选项。

---

## 9. Writerdeck.org
作家平台.org

**原文标题**: Writerdeck.org

**原文链接**: [http://www.writerdeck.org/](http://www.writerdeck.org/)

Writerdeck.org 介绍了一种名为“写作甲板 (writerDeck)”的概念，这是一种专为写作而设计的专用设备，旨在最大限度地减少干扰。它将写作甲板定义为一种计算机化的文字处理器，通常是定制的，在精神上类似于“赛博甲板 (cyberDeck)”。该网站认为，写作甲板通过消除干扰、提供愉悦的写作体验以及成为一个有趣的构建项目，优于通用计算机。

该网站提供有关商业写作甲板（如 Astrohaus Freewrite）和定制构建商的信息，以及 DIY 选项。一种廉价且简单的选择是将笔记本电脑通过 writerdeckOS 或 USB-DOS 转换为专用写作设备。替代选项包括使用带有蓝牙键盘的手机/平板电脑，但需要解决潜在的干扰问题。

构建 DIY 写作甲板涉及将计算机（如 Raspberry Pi）、屏幕和键盘组合在一个创意外壳中。软件通常包括基于 Linux 的操作系统和专用的写作程序，如 WareWoolf 或 ZeroWriter。该网站强调，只需一些基本的计算机技能和在线研究，就可以实现制作写作甲板的目标。

该指南提供了 WriterDeck 专用软件和相关教程的链接，包括 Micro Journal 构建、ZeroWriter、Penkesu Pocket Computer、Lisperati、Framedeck、Mainboard Terminal 和 Chonky Palmtop 的教程。

最后，该网站提醒读者，写作不需要昂贵的设备；一个简单的笔记本和笔通常就足够了。它引导读者访问 r/writerDeck 和 r/ZeroWriter 子版块，以获取更多信息和参与社区。该指南是社区驱动的，托管在 Github Pages 上，并欢迎贡献。

---

## 10. 线性代数解释了为何有些词语实际上无法翻译

**原文标题**: Linear Algebra Explains Why Some Words Are Effectively Untranslatable

**原文链接**: [https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable](https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable)

Marco Giancotti uses a linear algebra analogy to explain why some words are effectively untranslatable. He argues that concepts, like vectors, are abstract ideas that require a "basis" (language) to be expressed. Just as vectors have different coordinates depending on the chosen basis, concepts are represented by different words in different languages.

The article emphasizes that while translation aims to convey the same underlying concept, the choice of language significantly impacts the resulting representation. Giancotti argues that certain words, common in one language, might lack direct equivalents in another, leading to "practical untranslatability."

He highlights two key reasons for this: communication costs (time and space limitations) and precision. Translators often simplify complex terms, akin to Principal Component Analysis, losing nuances for brevity. Even when explicating fully, the nuances of added words can introduce unintended connotations. Furthermore, language is "quantized," offering a finite selection of words, limiting the ability to perfectly capture a concept's nuances, similar to the limitations of digital storage of numbers. This forces a "lowering of resolution" of concepts during translation, causing an inevitable loss of accuracy and supporting the argument that some words are, for all practical purposes, untranslatable.


---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 2 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 3 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 4 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 5 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 6 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 7 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 8 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 9 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 10 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 11 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 12 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 13 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 14 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 15 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 16 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 17 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 18 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 19 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 20 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 21 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 22 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 23 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 24 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 25 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 26 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 27 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 28 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 29 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 30 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 31 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 32 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 33 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 34 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 35 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 36 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 37 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 38 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 39 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 40 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 41 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 42 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 43 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 44 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 45 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 46 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 47 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 48 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 49 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 50 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 51 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 52 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 53 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 54 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 55 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 56 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 57 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 58 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 59 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 60 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 61 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 62 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 63 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 64 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 65 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 66 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 67 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 68 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 69 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 70 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 71 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 72 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 73 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 74 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 75 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 76 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 77 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 78 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 79 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 80 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 81 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 82 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 83 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 84 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 85 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 86 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 87 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 88 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 89 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 90 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 91 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 92 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 93 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 94 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 95 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 96 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 97 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 98 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 99 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 100 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 101 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 102 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 103 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 104 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 105 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 106 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 107 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 108 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 109 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 110 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 111 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 112 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 113 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 114 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 115 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 116 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 117 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 118 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 119 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 120 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 121 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 122 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 123 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 124 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 125 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 126 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 127 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 128 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 129 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 130 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 131 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 132 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 133 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 134 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 135 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 136 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 137 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 138 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 139 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 140 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 141 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 142 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 143 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 144 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 145 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 146 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 147 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 148 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 149 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 150 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 151 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 152 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 153 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 154 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 155 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 156 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 157 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 158 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 159 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 160 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 161 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 162 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 163 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 164 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 165 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 166 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 167 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 168 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 169 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 170 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 171 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 172 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 173 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 174 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 175 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 176 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 177 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 178 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 179 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 180 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 181 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 182 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 183 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 184 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 185 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 186 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 187 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 188 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 189 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 190 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 191 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 192 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 193 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 194 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 195 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 196 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 197 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 198 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 199 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 200 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 201 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 202 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 203 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 204 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 205 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 206 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 207 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 208 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 209 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 210 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 211 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 212 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 213 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 214 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 215 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 216 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 217 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 218 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 219 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 220 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 221 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 222 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 223 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 224 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 225 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 226 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 227 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 228 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 229 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 230 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 231 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 232 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 233 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 234 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 235 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 236 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 237 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 238 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 239 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
