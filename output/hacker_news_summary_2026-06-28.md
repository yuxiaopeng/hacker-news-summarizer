# Hacker News 热门文章摘要 (2026-06-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我用 Claude Code 获取了关于我 MRI 的第二意见。

**原文标题**: I used Claude Code to get a second opinion on my MRI

**原文链接**: [https://antoine.fi/mri-analysis-using-claude-code-opus](https://antoine.fi/mri-analysis-using-claude-code-opus)

在本文中，作者详细介绍了一项利用 Claude Code (Opus 4.8) 获取肩部核磁共振（MRI）第二诊疗意见的实验。在遭受持续疼痛后，一名人类骨科医生诊断作者患有肩胛下肌腱“III 级部分撕裂”。然而，当 ChatGPT 5.5 Pro 指出诊所建议的即时治疗方案——冲击波疗法和 Traumeel 注射——可能不合适或针对该特定病情缺乏适应症时，作者产生了怀疑。

为了进一步探究，作者使用 Claude Code 分析了 MRI 的原始 DICOM 文件。与标准的聊天机器人不同，该界面允许 AI 安装软件包并运行代码，从而对数据进行系统性的审查。结果令人震惊：Opus 4.8 得出结论称肌腱“完好无损”，这与人类放射科医生关于严重撕裂的诊断直接矛盾。

为了解决这一分歧，作者启动了一个“仲裁”流程，由 Claude 调用多个子代理进行双盲、公正的审查。这项二次 AI 分析以极高的置信度确认，并没有明显的撕裂，仅存在轻度的肌腱病。

作者总结道，虽然 AI 能够针对潜在的“重干预性”或不成熟的人类诊断提供严谨且极具参考价值的复核，但它也会让患者陷入一种“悬而不决”的状态。尽管 AI 的发现表明医生可能“操之过急”，但作者指出，AI 目前尚不能取代医疗专业人员。这项实验预示了一个 AI 可能会常规化审计医疗诊断的未来，尽管在当下，它也给夹在冲突专家意见之间的患者带来了新的不确定性。

---

## 2. 1880-1920年间5000份餐厅菜单

**原文标题**: 5k Restaurant Menus, Years 1880-1920

**原文链接**: [https://pudding.cool/2026/06/menu-collection/](https://pudding.cool/2026/06/menu-collection/)

本文介绍了一个数字档案馆，其中收录了1880年至1920年间的**5,000份餐厅菜单**。这一历史数据库全面展示了19世纪末至20世纪初的烹饪趋势、饮食习惯和食品价格。

该馆藏的主要特色包括：

*   **按年代浏览：** 用户可以按年份检索馆藏，从而对比研究菜单在40年间的演变。
*   **AI增强信息：** 为帮助现代读者理解晦涩或陈旧的烹饪术语，平台利用**AI生成的菜品定义**提供背景支持。这些信息有助于弥合历史术语与当代理解之间的鸿沟。
*   **交互式界面：** 数字展厅包含“返回”、“下一页”和“展开”等标准导航工具，方便用户探索高分辨率的菜单图像。

对于关注全球历史变革时期美食演化和餐饮业的历史学家、社会学家及美食爱好者而言，这一资源是一项重要的研究工具。

---

## 3. 在龙梦逸珑笔记本和 OpenBSD 上与“龙”共舞

**原文标题**: Working around dragons with the Lemote Yeeloong laptop and OpenBSD

**原文链接**: [http://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html](http://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html)

本文探讨了龙梦逸珑（Lemote Yeeloong）的历史与技术演进。这是一款独特的中国国产笔记本电脑，搭载了兼容 MIPS64 的龙芯（Loongson，原称 Godson）处理器。作者的兴趣源于该设备在自由软件社区中的声望——理查德·斯托曼（Richard Stallman）曾使用过它——因为它无需私有二进制块或固件即可运行，是运行 OpenBSD 的理想平台。

该处理器的起源可追溯至中国的“863计划”，该计划于 1986 年启动，旨在培育本土高科技产业并减少对外国芯片的依赖。2001 年，中国科学院计算技术研究所开始设计“龙芯”系列 CPU。虽然最初为了规避专利冲突而采用了类似 32 位 MIPS II 的架构，但该项目经历了多次迭代：

*   **龙芯1号 (2002)：** 一款低功耗 32 位芯片，早期曾面临与 MIPS 公司的商标和许可争议。
*   **龙芯2号系列：** 向 MIPS III 兼容迈进的 64 位扩展版本。**龙芯2E** (2006) 通过与意法半导体（STMicroelectronics）合作，主频达到了 1GHz。
*   **龙芯2F (2007)：** 首个获得 MIPS “正式”授权的版本，集成了北桥并提升了能效。

这些芯片的商业化促成了龙梦（Lemote）公司的成立。这家合资企业推出了福珑（Fuloong）台式机，并于 2008 年 10 月发布了**逸珑（Yeeloong）笔记本电脑**。逸珑作为全球首款基于龙芯的笔记本电脑上市，将 2F 处理器与 AMD 南桥和瑞昱（Realtek）网卡等通用组件相结合。

最后，本文将逸珑定义为中国计算机史上的重要里程碑，也是令技术极客们趋之若鹜的“极客杀手”。对于那些寻求高度便携、完全自由且架构独特，以便在 OpenBSD 等替代操作系统上进行实验的爱好者来说，它是一款理想的机器。

---

## 4. 台杉：日本“树中生树”的培育技艺 (2020)

**原文标题**: Daisugi, the Japanese technique of trees out of trees (2020)

**原文链接**: [https://www.openculture.com/2020/10/daisugi.html](https://www.openculture.com/2020/10/daisugi.html)

起源于15世纪的京都，“台杉”（Daisugi，意为“平台杉”）是一项精妙的日本林业技术，其核心在于让树木从现有的树木之上生长。作为对土地和树苗短缺的一种应对方案，该方法的原理类似于巨型盆栽。通过修剪基底杉树，使其形状如同张开的手掌，林业工作者可以从单一树干上培育出多根垂直向上生长的侧枝。

在16世纪，受茶道大师千利休的需求以及“数寄屋造”建筑风格盛行的推动，这项技术声名大噪。当时，贵族和武士渴望在宅邸中使用高品质的北山杉，但原材料供应紧缺。台杉提供了一种巧妙的解决方案，既能产出木材，又无需占用大量土地或面临森林砍伐的风险。

由此产出的木材被称为“垂木”（Taruki），因其兼具美学价值和卓越的结构性能而备受推崇。由于这种特殊的培育方式，该木材的韧性是普通杉木的140%，密度和强度则是其200%。这些特性使得木材极为笔直、纤细且抗风能力强，是传统日本茶室椽子和屋顶用材的理想选择。

在其诞生六个世纪后的今天，台杉依然是可持续工艺的典范，这种产出高品质材料的方法至今仍令世界惊叹。

---

## 5. 人工智能时代的软件工程思考

**原文标题**: Reflections on Software Engineering in the Age of AI

**原文链接**: [https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/](https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/)

In "Reflections on Software Engineering in the Age of AI," the author—a software engineer and novelist—explores how generative AI is fundamentally altering the nature of creative work. While AI can efficiently produce "pretty good" code, it has shifted the developer’s role from a creator to a supervisor or editor. 

The author argues that this shift destroys the "flow state"—the deep, immersive engagement described by psychologist Mihaly Csikszentmihalyi. By offloading the "hard thinking" to AI, developers suffer from skill atrophy, becoming "lazier and stupider" as they lose the drive to solve complex problems manually. 

A significant systemic concern raised is the "pipeline problem." Because companies are replacing junior developers with AI, the industry is failing to train the next generation of senior engineers. Without "doing the work," new engineers will lack the institutional and systems-level knowledge required to manage the massive, complex codebases that AI cannot fully grasp. The author uses a U.S. Navy analogy: just as the Navy must build ships they don't need simply to preserve the craftsmanship, the software industry must write code to maintain its expertise.

Ultimately, the author warns of a future filled with "digital plastic"—vast amounts of AI-generated content and code that "just works" for now but is poorly understood and difficult to maintain. He concludes that while software development has been reduced to a reactive task, individuals must reclaim their "flow" through non-automated pursuits like writing, reading, and human connection to preserve their capacity for original thought and imagination.

---

## 6. Examining circuit boards from the Space Shuttle's I/O Processor

**原文标题**: Examining circuit boards from the Space Shuttle's I/O Processor

**原文链接**: [https://www.righto.com/2026/06/space-shuttle-io-processor-boards.html](https://www.righto.com/2026/06/space-shuttle-io-processor-boards.html)

生成摘要时出错

---

## 7. Tokenmaxxing is dead, long live Tokenmaxxing

**原文标题**: Tokenmaxxing is dead, long live Tokenmaxxing

**原文链接**: [https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing](https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing)

生成摘要时出错

---

## 8. Show HN: Zanagrams

**原文标题**: Show HN: Zanagrams

**原文链接**: [https://zanagrams.com/](https://zanagrams.com/)

生成摘要时出错

---

## 9. The curious case of the disappearing Polish S (2015)

**原文标题**: The curious case of the disappearing Polish S (2015)

**原文链接**: [https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/)

生成摘要时出错

---

## 10. The Boeing 747 Begins Its Final Descent

**原文标题**: The Boeing 747 Begins Its Final Descent

**原文链接**: [https://www.theatlantic.com/magazine/2026/07/boeing-747-retirement/687304/](https://www.theatlantic.com/magazine/2026/07/boeing-747-retirement/687304/)

生成摘要时出错

---

## 11. A way to exclude sensitive files issue still open for OpenAI Codex

**原文标题**: A way to exclude sensitive files issue still open for OpenAI Codex

**原文链接**: [https://github.com/openai/codex/issues/2847](https://github.com/openai/codex/issues/2847)

生成摘要时出错

---

## 12. Flock cameras track more than your license plate, and they're spreading fast

**原文标题**: Flock cameras track more than your license plate, and they're spreading fast

**原文链接**: [https://www.engadget.com/2203000/flock-cameras-recording-license-plate/](https://www.engadget.com/2203000/flock-cameras-recording-license-plate/)

生成摘要时出错

---

## 13. Show HN: DRM-Free Books

**原文标题**: Show HN: DRM-Free Books

**原文链接**: [https://frequal.com/Perspectives/DrmFreeAuthors.html](https://frequal.com/Perspectives/DrmFreeAuthors.html)

生成摘要时出错

---

## 14. Michigan bill would bar employers from requiring after-hours coms with workers

**原文标题**: Michigan bill would bar employers from requiring after-hours coms with workers

**原文链接**: [https://www.cbsnews.com/detroit/news/workplace-boundaries-act-employees-after-hours/](https://www.cbsnews.com/detroit/news/workplace-boundaries-act-employees-after-hours/)

生成摘要时出错

---

## 15. Build Yourself Flowers

**原文标题**: Build Yourself Flowers

**原文链接**: [https://vickiboykis.com/2026/04/20/build-yourself-flowers/](https://vickiboykis.com/2026/04/20/build-yourself-flowers/)

生成摘要时出错

---

## 16. EU to legislate about Chat Control behind closed doors

**原文标题**: EU to legislate about Chat Control behind closed doors

**原文链接**: [https://www.patrick-breyer.de/en/double-threat-to-private-communications-undemocratic-chat-control-backroom-deals-and-imminent-concessions-spark-relaunch-of-fightchatcontrol-eu/](https://www.patrick-breyer.de/en/double-threat-to-private-communications-undemocratic-chat-control-backroom-deals-and-imminent-concessions-spark-relaunch-of-fightchatcontrol-eu/)

生成摘要时出错

---

## 17. Programmable Probabilistic Computer with 1M p-bits

**原文标题**: Programmable Probabilistic Computer with 1M p-bits

**原文链接**: [https://arxiv.org/abs/2606.25313](https://arxiv.org/abs/2606.25313)

生成摘要时出错

---

## 18. Marfa Public Radio Puts You to Sleep

**原文标题**: Marfa Public Radio Puts You to Sleep

**原文链接**: [https://www.marfapublicradio.org/podcast/marfa-public-radio-puts-you-to-sleep](https://www.marfapublicradio.org/podcast/marfa-public-radio-puts-you-to-sleep)

生成摘要时出错

---

## 19. Do Babies Dream of Baby Sheep?

**原文标题**: Do Babies Dream of Baby Sheep?

**原文链接**: [https://devz.cl/posts/do-babies-dream-of-electric-sheep/](https://devz.cl/posts/do-babies-dream-of-electric-sheep/)

生成摘要时出错

---

## 20. California legislature agrees to upload driver's licenses to national database

**原文标题**: California legislature agrees to upload driver's licenses to national database

**原文链接**: [https://papersplease.org/wp/2026/06/27/california-legislature-agrees-to-upload-drivers-licenses-to-national-database/](https://papersplease.org/wp/2026/06/27/california-legislature-agrees-to-upload-drivers-licenses-to-national-database/)

生成摘要时出错

---

## 21. DLL that was not present in memory despite not being formally unloaded

**原文标题**: DLL that was not present in memory despite not being formally unloaded

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260625-00/?p=112467](https://devblogs.microsoft.com/oldnewthing/20260625-00/?p=112467)

生成摘要时出错

---

## 22. The MUMPS 76 Primer – anniversary edition

**原文标题**: The MUMPS 76 Primer – anniversary edition

**原文链接**: [https://github.com/rochus-keller/MUMPS/blob/main/docs/MUMPS_Primer.adoc](https://github.com/rochus-keller/MUMPS/blob/main/docs/MUMPS_Primer.adoc)

生成摘要时出错

---

## 23. Google limits Meta's use of its Gemini AI models

**原文标题**: Google limits Meta's use of its Gemini AI models

**原文链接**: [https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)

生成摘要时出错

---

## 24. Designing a Personal Pebble Watchface

**原文标题**: Designing a Personal Pebble Watchface

**原文链接**: [https://www.jonashietala.se/blog/2026/06/26/designing_a_personal_pebble_watchface/](https://www.jonashietala.se/blog/2026/06/26/designing_a_personal_pebble_watchface/)

生成摘要时出错

---

## 25. Bringing Swift to the Apple ][

**原文标题**: Bringing Swift to the Apple ][

**原文链接**: [https://yeokhengmeng.com/2026/06/swift-on-apple-ii/](https://yeokhengmeng.com/2026/06/swift-on-apple-ii/)

生成摘要时出错

---

## 26. Anonymous GitHub account mass-dropping undisclosed 0-days

**原文标题**: Anonymous GitHub account mass-dropping undisclosed 0-days

**原文链接**: [https://github.com/bikini/exploitarium](https://github.com/bikini/exploitarium)

生成摘要时出错

---

## 27. AMD Strix Halo RDMA Cluster Setup Guide

**原文标题**: AMD Strix Halo RDMA Cluster Setup Guide

**原文链接**: [https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md)

生成摘要时出错

---

## 28. Choosing a Public DNS Resolver

**原文标题**: Choosing a Public DNS Resolver

**原文链接**: [https://evilbit.de/dns-resolver-guide.html](https://evilbit.de/dns-resolver-guide.html)

生成摘要时出错

---

## 29. EU Open Sources Ten-Year Network Development Planning Tools

**原文标题**: EU Open Sources Ten-Year Network Development Planning Tools

**原文链接**: [https://github.com/open-energy-transition/open-tyndp](https://github.com/open-energy-transition/open-tyndp)

生成摘要时出错

---

## 30. The origins of the school system aimed to produce independent, critical thinkers (2024)

**原文标题**: The origins of the school system aimed to produce independent, critical thinkers (2024)

**原文链接**: [https://www.cbc.ca/radio/ideas/humboldt-education-system-bildung-1.7172093](https://www.cbc.ca/radio/ideas/humboldt-education-system-bildung-1.7172093)

生成摘要时出错

---

## 31. Bashblog – a single bash script to create blogs

**原文标题**: Bashblog – a single bash script to create blogs

**原文链接**: [https://github.com/cfenollosa/bashblog](https://github.com/cfenollosa/bashblog)

生成摘要时出错

---

## 32. Lenovo saying RAM prices may never go back to how they were

**原文标题**: Lenovo saying RAM prices may never go back to how they were

**原文链接**: [https://www.rockpapershotgun.com/oh-no-thats-lenovo-saying-they-think-these-ram-prices-will-be-the-new-normal-and-may-never-go-back-to-how-they-were](https://www.rockpapershotgun.com/oh-no-thats-lenovo-saying-they-think-these-ram-prices-will-be-the-new-normal-and-may-never-go-back-to-how-they-were)

生成摘要时出错

---

## 33. Wayfinder Router: deterministic routing of queries between local and hosted LLM

**原文标题**: Wayfinder Router: deterministic routing of queries between local and hosted LLM

**原文链接**: [https://github.com/itsthelore/wayfinder-router](https://github.com/itsthelore/wayfinder-router)

生成摘要时出错

---

## 34. Show HN: Decomp Academy – Learn to decompile GameCube games into matching C

**原文标题**: Show HN: Decomp Academy – Learn to decompile GameCube games into matching C

**原文链接**: [https://decomp-academy.dev](https://decomp-academy.dev)

生成摘要时出错

---

## 35. Professor denounces mass AI fraud on an exam at Brown University

**原文标题**: Professor denounces mass AI fraud on an exam at Brown University

**原文链接**: [https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)

生成摘要时出错

---

## 36. Engineering for Bounded Cognition

**原文标题**: Engineering for Bounded Cognition

**原文链接**: [https://shapeofthesystem.com/posts/2026/02/03/bounded-cognition](https://shapeofthesystem.com/posts/2026/02/03/bounded-cognition)

生成摘要时出错

---

## 37. Turning music into a chore is how I became a musician (2022)

**原文标题**: Turning music into a chore is how I became a musician (2022)

**原文链接**: [https://the.scapegoat.dev/turning-music-into-a-chore-is-what-made-me-an-artist/](https://the.scapegoat.dev/turning-music-into-a-chore-is-what-made-me-an-artist/)

生成摘要时出错

---

## 38. WAL-RUS: a Rust Rewrite of WAL-G for PostgreSQL Backups

**原文标题**: WAL-RUS: a Rust Rewrite of WAL-G for PostgreSQL Backups

**原文链接**: [https://clickhouse.com/blog/walrus-postgres-backups-in-rust](https://clickhouse.com/blog/walrus-postgres-backups-in-rust)

生成摘要时出错

---

## 39. Turn your site into a place people can bump into each other

**原文标题**: Turn your site into a place people can bump into each other

**原文链接**: [https://cauenapier.com/blog/townsquare_release/](https://cauenapier.com/blog/townsquare_release/)

生成摘要时出错

---

## 40. Space Shuttle Endeavour's 20-story vertical display

**原文标题**: Space Shuttle Endeavour's 20-story vertical display

**原文链接**: [https://californiasciencecenter.org/about-us/samuel-oschin-air-and-space-center/go-for-stack](https://californiasciencecenter.org/about-us/samuel-oschin-air-and-space-center/go-for-stack)

生成摘要时出错

---

## 41. Regular expressions that work “everywhere”

**原文标题**: Regular expressions that work “everywhere”

**原文链接**: [https://www.johndcook.com/blog/2026/06/23/regex-everywhere/](https://www.johndcook.com/blog/2026/06/23/regex-everywhere/)

生成摘要时出错

---

## 42. A stray "j" ruined my evening

**原文标题**: A stray "j" ruined my evening

**原文链接**: [https://napkins.mtmn.name/posts/stray-jay.html](https://napkins.mtmn.name/posts/stray-jay.html)

生成摘要时出错

---

## 43. Reducing tick density along recreational trails in Ottawa, Canada

**原文标题**: Reducing tick density along recreational trails in Ottawa, Canada

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S1877959X26000476](https://www.sciencedirect.com/science/article/pii/S1877959X26000476)

生成摘要时出错

---

## 44. AI learns the “dark art” of RFIC design

**原文标题**: AI learns the “dark art” of RFIC design

**原文链接**: [https://spectrum.ieee.org/ai-radio-chip-design](https://spectrum.ieee.org/ai-radio-chip-design)

生成摘要时出错

---

## 45. OpenRA

**原文标题**: OpenRA

**原文链接**: [https://www.openra.net/](https://www.openra.net/)

生成摘要时出错

---

## 46. Supabase (YC S20) Is Hiring for Multigres

**原文标题**: Supabase (YC S20) Is Hiring for Multigres

**原文链接**: [https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228](https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228)

生成摘要时出错

---

## 47. Mobile Web Computing Before Smartphones. (University of Liverpool, ~2010) [pdf]

**原文标题**: Mobile Web Computing Before Smartphones. (University of Liverpool, ~2010) [pdf]

**原文链接**: [https://cgi.csc.liv.ac.uk/~trp/Teaching_Resources/COMP327/327-Lecture4-MobileWeb.pdf](https://cgi.csc.liv.ac.uk/~trp/Teaching_Resources/COMP327/327-Lecture4-MobileWeb.pdf)

生成摘要时出错

---

## 48. It's dead, Jim – the old Microsoft UEFI CA from 2011 expired yesterday

**原文标题**: It's dead, Jim – the old Microsoft UEFI CA from 2011 expired yesterday

**原文链接**: [https://blog.einval.com/2026/06/27](https://blog.einval.com/2026/06/27)

生成摘要时出错

---

## 49. Suspicious Discontinuities (2020)

**原文标题**: Suspicious Discontinuities (2020)

**原文链接**: [https://danluu.com/discontinuities/](https://danluu.com/discontinuities/)

生成摘要时出错

---

## 50. From Pentagons to Pentagrams

**原文标题**: From Pentagons to Pentagrams

**原文链接**: [https://johncarlosbaez.wordpress.com/2026/05/29/from-pentagons-to-pentagrams/](https://johncarlosbaez.wordpress.com/2026/05/29/from-pentagons-to-pentagrams/)

生成摘要时出错

---

## 51. Austria Lobbies EU to Host Anthropic After US Access Curbs

**原文标题**: Austria Lobbies EU to Host Anthropic After US Access Curbs

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-28/austria-lobbies-eu-to-host-anthropic-after-us-access-curbs](https://www.bloomberg.com/news/articles/2026-06-28/austria-lobbies-eu-to-host-anthropic-after-us-access-curbs)

生成摘要时出错

---

## 52. DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文标题**: DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文链接**: [https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

生成摘要时出错

---

## 53. Post-Mythos Cybersecurity: Keep calm and carry on

**原文标题**: Post-Mythos Cybersecurity: Keep calm and carry on

**原文链接**: [https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/)

生成摘要时出错

---

## 54. The best response to AI slop and online noise is from Robin Williams

**原文标题**: The best response to AI slop and online noise is from Robin Williams

**原文链接**: [https://jayacunzo.com/blog/your-move-chief](https://jayacunzo.com/blog/your-move-chief)

生成摘要时出错

---

## 55. Asian AI startups launch Mythos-like models

**原文标题**: Asian AI startups launch Mythos-like models

**原文链接**: [https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)

生成摘要时出错

---

## 56. From Hallmark to neon signs: A look at Jim Parkinson's career in letter art

**原文标题**: From Hallmark to neon signs: A look at Jim Parkinson's career in letter art

**原文链接**: [https://typographica.org/on-typography/jim-parkinson-1941-2025/](https://typographica.org/on-typography/jim-parkinson-1941-2025/)

生成摘要时出错

---

## 57. Why does kinetic energy increase quadratically, not linearly, with speed? (2011)

**原文标题**: Why does kinetic energy increase quadratically, not linearly, with speed? (2011)

**原文链接**: [https://physics.stackexchange.com/questions/535/why-does-kinetic-energy-increase-quadratically-not-linearly-with-speed](https://physics.stackexchange.com/questions/535/why-does-kinetic-energy-increase-quadratically-not-linearly-with-speed)

生成摘要时出错

---

## 58. How H-E-B became Texas' most beloved brand (2024)

**原文标题**: How H-E-B became Texas' most beloved brand (2024)

**原文链接**: [https://texashighways.com/culture/how-heb-became-texas-most-beloved-brand/](https://texashighways.com/culture/how-heb-became-texas-most-beloved-brand/)

生成摘要时出错

---

## 59. Armadillo – A DNS Server in Gleam for Homelab Use

**原文标题**: Armadillo – A DNS Server in Gleam for Homelab Use

**原文链接**: [https://github.com/vshakitskiy/armadillo](https://github.com/vshakitskiy/armadillo)

生成摘要时出错

---

## 60. The US Army Issued Ocarinas to Soldiers in World War II

**原文标题**: The US Army Issued Ocarinas to Soldiers in World War II

**原文链接**: [https://www.flutetunes.com/articles/my-flute-goes-to-war/](https://www.flutetunes.com/articles/my-flute-goes-to-war/)

生成摘要时出错

---

## 61. Fintech Engineering Handbook

**原文标题**: Fintech Engineering Handbook

**原文链接**: [https://w.pitula.me/fintech-engineering-handbook/](https://w.pitula.me/fintech-engineering-handbook/)

生成摘要时出错

---

## 62. Reflecting to optimise

**原文标题**: Reflecting to optimise

**原文链接**: [https://magnusross.github.io/posts/reflecting-to-optimise/](https://magnusross.github.io/posts/reflecting-to-optimise/)

生成摘要时出错

---

## 63. How do you keep Web MIDI from crashing a 1983 synthesizer?

**原文标题**: How do you keep Web MIDI from crashing a 1983 synthesizer?

**原文链接**: [https://knob.monster/how-do-you-keep-web-midi-from-crashing-a-1983-synthesizer](https://knob.monster/how-do-you-keep-web-midi-from-crashing-a-1983-synthesizer)

生成摘要时出错

---

## 64. IP Crawl: Living atlas of open webcams discovered on the public internet

**原文标题**: IP Crawl: Living atlas of open webcams discovered on the public internet

**原文链接**: [https://ipcrawl.com/](https://ipcrawl.com/)

生成摘要时出错

---

## 65. One man, two kernels, and a lot of RISC-V

**原文标题**: One man, two kernels, and a lot of RISC-V

**原文链接**: [https://www.theregister.com/software/2026/06/26/one-man-two-kernels-and-a-lot-of-risc-v/5262858](https://www.theregister.com/software/2026/06/26/one-man-two-kernels-and-a-lot-of-risc-v/5262858)

生成摘要时出错

---

## 66. Experimenting with Random() in CSS

**原文标题**: Experimenting with Random() in CSS

**原文链接**: [https://polypane.app/blog/experimenting-with-random-in-css/](https://polypane.app/blog/experimenting-with-random-in-css/)

生成摘要时出错

---

## 67. Previewing GPT‑5.6 Sol: a next-generation model

**原文标题**: Previewing GPT‑5.6 Sol: a next-generation model

**原文链接**: [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/)

生成摘要时出错

---

## 68. Apple Neural Engine: Architecture, Programming, and Performance

**原文标题**: Apple Neural Engine: Architecture, Programming, and Performance

**原文链接**: [https://arxiv.org/abs/2606.22283](https://arxiv.org/abs/2606.22283)

生成摘要时出错

---

## 69. Enhancing x11 Application Security with LXC (2025)

**原文标题**: Enhancing x11 Application Security with LXC (2025)

**原文链接**: [https://dobrowolski.dev/article/enhancing-x11-application-security-with-lxc/](https://dobrowolski.dev/article/enhancing-x11-application-security-with-lxc/)

生成摘要时出错

---

## 70. The 'Almost Homeless' Subreddit Is a Stark Glimpse at Soaring Wealth Inequality

**原文标题**: The 'Almost Homeless' Subreddit Is a Stark Glimpse at Soaring Wealth Inequality

**原文链接**: [https://www.wired.com/story/the-almost-homeless-subreddit-is-a-stark-glimpse-at-soaring-wealth-inequality/](https://www.wired.com/story/the-almost-homeless-subreddit-is-a-stark-glimpse-at-soaring-wealth-inequality/)

生成摘要时出错

---

## 71. What Ozempic does to the gut-brain axis

**原文标题**: What Ozempic does to the gut-brain axis

**原文链接**: [https://www.psychologytoday.com/au/blog/mood-by-microbe/202606/what-ozempic-does-to-the-gut-brain-axis](https://www.psychologytoday.com/au/blog/mood-by-microbe/202606/what-ozempic-does-to-the-gut-brain-axis)

生成摘要时出错

---

## 72. Running a software jam in a world of slop

**原文标题**: Running a software jam in a world of slop

**原文链接**: [https://foxmoss.com/blog/radish/](https://foxmoss.com/blog/radish/)

生成摘要时出错

---

## 73. Zuckerberg's war on whistleblowers

**原文标题**: Zuckerberg's war on whistleblowers

**原文链接**: [https://pluralistic.net/2026/06/27/zuckerstreisand-2/](https://pluralistic.net/2026/06/27/zuckerstreisand-2/)

生成摘要时出错

---

## 74. IBM claims first sub-1 nanometer chip technology

**原文标题**: IBM claims first sub-1 nanometer chip technology

**原文链接**: [https://arstechnica.com/gadgets/2026/06/ibm-claims-worlds-first-sub-1-nanometer-chip-technology/](https://arstechnica.com/gadgets/2026/06/ibm-claims-worlds-first-sub-1-nanometer-chip-technology/)

生成摘要时出错

---

## 75. The eerie interface of man and machine (Life Magazine, October 1967)

**原文标题**: The eerie interface of man and machine (Life Magazine, October 1967)

**原文链接**: [https://blog.jgc.org/2026/06/the-eerie-interface-of-man-and-machine.html](https://blog.jgc.org/2026/06/the-eerie-interface-of-man-and-machine.html)

生成摘要时出错

---

## 76. Show HN: Metaspec: The DpANS3R Common Lisp Spec in S-Expr and HTML Format

**原文标题**: Show HN: Metaspec: The DpANS3R Common Lisp Spec in S-Expr and HTML Format

**原文链接**: [https://metaspec.dev/#](https://metaspec.dev/#)

生成摘要时出错

---

## 77. Anatomy of a Failed (Nation-State?) Attack

**原文标题**: Anatomy of a Failed (Nation-State?) Attack

**原文链接**: [https://grack.com/blog/2026/06/25/dissecting-a-failed-nation-state-attack/](https://grack.com/blog/2026/06/25/dissecting-a-failed-nation-state-attack/)

生成摘要时出错

---

## 78. Paradise Revisited: What Darwin Saw in the Galápagos

**原文标题**: Paradise Revisited: What Darwin Saw in the Galápagos

**原文链接**: [https://www.theatlantic.com/magazine/2026/08/writers-way-galapagos-charles-darwin-travel/687480/](https://www.theatlantic.com/magazine/2026/08/writers-way-galapagos-charles-darwin-travel/687480/)

生成摘要时出错

---

## 79. The case for physical media ownership

**原文标题**: The case for physical media ownership

**原文链接**: [https://dervis.de/physical/](https://dervis.de/physical/)

生成摘要时出错

---

## 80. Yap – free offline voice dictation for Mac/Windows/Linux (Wispr Flow alt)

**原文标题**: Yap – free offline voice dictation for Mac/Windows/Linux (Wispr Flow alt)

**原文链接**: [https://github.com/AkuchiS/yap](https://github.com/AkuchiS/yap)

生成摘要时出错

---

## 81. An entire Herculaneum scroll has been read for the first time

**原文标题**: An entire Herculaneum scroll has been read for the first time

**原文链接**: [https://scrollprize.org/firstscroll](https://scrollprize.org/firstscroll)

生成摘要时出错

---

## 82. Beer CSS – Build material design in record time

**原文标题**: Beer CSS – Build material design in record time

**原文链接**: [https://www.beercss.com](https://www.beercss.com)

生成摘要时出错

---

## 83. Show HN: Adrafinil – keep a lid-closed Mac awake only while agents work

**原文标题**: Show HN: Adrafinil – keep a lid-closed Mac awake only while agents work

**原文链接**: [https://github.com/kageroumado/adrafinil](https://github.com/kageroumado/adrafinil)

生成摘要时出错

---

## 84. Brace Expansion Tree

**原文标题**: Brace Expansion Tree

**原文链接**: [https://www.johndcook.com/blog/2026/06/27/brace-expansion-tree/](https://www.johndcook.com/blog/2026/06/27/brace-expansion-tree/)

生成摘要时出错

---

## 85. Michigan spent $1.8B and only created 602 jobs

**原文标题**: Michigan spent $1.8B and only created 602 jobs

**原文链接**: [https://www.msn.com/en-us/money/general/michigan-spent-1-8-billion-and-only-created-602-jobs/ar-AA26Cusu](https://www.msn.com/en-us/money/general/michigan-spent-1-8-billion-and-only-created-602-jobs/ar-AA26Cusu)

生成摘要时出错

---

## 86. Om Malik has died

**原文标题**: Om Malik has died

**原文链接**: [https://om.co/2026/06/24/1966-2026/](https://om.co/2026/06/24/1966-2026/)

生成摘要时出错

---

## 87. How Many Elementary Particles Are There, Really?

**原文标题**: How Many Elementary Particles Are There, Really?

**原文链接**: [https://www.quantamagazine.org/how-many-elementary-particles-are-there-really-20260615/](https://www.quantamagazine.org/how-many-elementary-particles-are-there-really-20260615/)

生成摘要时出错

---

## 88. Streaming services' obnoxiously loud ads become illegal on July 1 in California

**原文标题**: Streaming services' obnoxiously loud ads become illegal on July 1 in California

**原文链接**: [https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/](https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/)

生成摘要时出错

---

## 89. Task Failed Successfully: Saturating NIC and Disk Bandwidth

**原文标题**: Task Failed Successfully: Saturating NIC and Disk Bandwidth

**原文链接**: [https://blog.mrcroxx.com/posts/task-failed-successfully-saturating-nic-and-disk-bandwidth/](https://blog.mrcroxx.com/posts/task-failed-successfully-saturating-nic-and-disk-bandwidth/)

生成摘要时出错

---

## 90. Climate.us launches independent website for trusted climate information

**原文标题**: Climate.us launches independent website for trusted climate information

**原文链接**: [https://www.climate.us/news-features/feed/climateus-launches-independent-website-trusted-climate-information](https://www.climate.us/news-features/feed/climateus-launches-independent-website-trusted-climate-information)

生成摘要时出错

---

## 91. My Steam Machine is a 50ft HDMI cable

**原文标题**: My Steam Machine is a 50ft HDMI cable

**原文链接**: [https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/](https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/)

生成摘要时出错

---

## 92. Show HN: FSM – an advanced system monitor for Linux

**原文标题**: Show HN: FSM – an advanced system monitor for Linux

**原文链接**: [https://github.com/mskrasnov/FSM](https://github.com/mskrasnov/FSM)

生成摘要时出错

---

## 93. International investment and local rules push prices up faster than supply

**原文标题**: International investment and local rules push prices up faster than supply

**原文链接**: [https://news.mccombs.utexas.edu/research/foreign-funds-help-make-housing-unaffordable/](https://news.mccombs.utexas.edu/research/foreign-funds-help-make-housing-unaffordable/)

生成摘要时出错

---

## 94. Monlite – documents, vectors, cache, and job queue in one SQLite file

**原文标题**: Monlite – documents, vectors, cache, and job queue in one SQLite file

**原文链接**: [https://github.com/qataruts/monlite](https://github.com/qataruts/monlite)

生成摘要时出错

---

## 95. One Million Passports Leaked Online

**原文标题**: One Million Passports Leaked Online

**原文链接**: [https://www.schneier.com/blog/archives/2026/06/one-million-passports-leaked-online.html](https://www.schneier.com/blog/archives/2026/06/one-million-passports-leaked-online.html)

生成摘要时出错

---

## 96. Long Wave radio era set to end with switch-off

**原文标题**: Long Wave radio era set to end with switch-off

**原文链接**: [https://www.economist.com/britain/2026/06/25/the-bbc-switches-off-its-oldest-service](https://www.economist.com/britain/2026/06/25/the-bbc-switches-off-its-oldest-service)

生成摘要时出错

---

## 97. Researchers have developed pixels that can emit and analyse light together

**原文标题**: Researchers have developed pixels that can emit and analyse light together

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2026/06/a-new-type-of-pixel.html](https://ethz.ch/en/news-and-events/eth-news/news/2026/06/a-new-type-of-pixel.html)

生成摘要时出错

---

## 98. Faster KNN search in Manticore: 2-pass HNSW, batched distances, and AVX-512

**原文标题**: Faster KNN search in Manticore: 2-pass HNSW, batched distances, and AVX-512

**原文链接**: [https://medium.com/@s_nikolaev/faster-knn-search-in-manticore-2-pass-hnsw-batched-distances-and-avx-512-b85604647aab](https://medium.com/@s_nikolaev/faster-knn-search-in-manticore-2-pass-hnsw-batched-distances-and-avx-512-b85604647aab)

生成摘要时出错

---

## 99. Hellishly Slow Level 13 Deflate Compression

**原文标题**: Hellishly Slow Level 13 Deflate Compression

**原文链接**: [https://kirill.korins.ky/articles/hellishly-slow-level-13-deflate-compression/](https://kirill.korins.ky/articles/hellishly-slow-level-13-deflate-compression/)

生成摘要时出错

---

## 100. We can still stop California's 3D printer surveillance scheme

**原文标题**: We can still stop California's 3D printer surveillance scheme

**原文链接**: [https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme](https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme)

生成摘要时出错

---

