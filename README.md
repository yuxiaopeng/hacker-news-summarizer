# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-28.md)

*最后自动更新时间: 2025-06-28 17:45:37*
## 1. MCP：一个（意外地）通用的插件系统

**原文标题**: MCP: An (Accidentally) Universal Plugin System

**原文链接**: [https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin](https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin)

无法访问文章链接。

---

## 2. Jane Street 悄然的留人策略

**原文标题**: Jane Street's sneaky retention tactic

**原文链接**: [https://www.economist.com/finance-and-economics/2025/06/26/jane-streets-sneaky-retention-tactic](https://www.economist.com/finance-and-economics/2025/06/26/jane-streets-sneaky-retention-tactic)

简·街：一家对冲基金及其非同寻常的员工保留策略——为其内部编程语言构建编译器。印刷版“金融与经济”版块的其他文章包括股票避税、减少移民的后果、预测市场的兴起以及大宗商品价格波动等主题。

---

## 3. 忙碌海狸(6)非常大

**原文标题**: BusyBeaver(6) Is Quite Large

**原文链接**: [https://scottaaronson.blog/?p=8972](https://scottaaronson.blog/?p=8972)

Raymond Laflamme的博客文章探讨了确定忙碌海狸函数（具体为BB(6)）下界的最新突破性进展。忙碌海狸函数BB(n)表示具有“n”个状态的图灵机在全零磁带上启动后停止之前可以执行的最大步数。

Laflamme强调了BB(5)和BB(6)之间量级的巨大飞跃。虽然已知BB(5)为47,176,870，但来自“BBchallenge”团队的“mxdys”的最新工作已经大幅提高了BB(6)的已知下限。 该下限首先提高到10,000,000叠代10次，然后进一步提高到2叠代2叠代2叠代9次，这个数字如此之大，以至于超越了简单的可视化。 这意味着BB(6)至少为2五迭代5次。

作者反思了这些发现，特别是BB(6)的巨大规模，使他重新考虑了BB(n)的值在何处变得独立于集合论的ZFC公理。 他假设这种独立性可能发生在比之前认为的“n”值（目前已知为n=745）更低的“n”（7、8或9）处。

最后，Laflamme提到了他最近在布拉格参加STOC'2025的行程，并提供了他关于“量子加速的现状”的全会讲座幻灯片链接。他还简要地谈到了他对世界现状的挣扎，并在这样的研究突破中找到了慰藉。

---

## 4. 我们在自制的 CPU 上，使用自制的 C 编译器运行了类 Unix 的 OS Xv6。

**原文标题**: We ran a Unix-like OS Xv6 on our home-built CPU with a home-built C compiler

**原文链接**: [https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/](https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/)

佐伯多佳也讲述了一个学生项目，其中东京大学的一个本科生团队设计了自己的CPU架构（ISA），在FPGA上构建了一个处理器，从头开始创建了一个C编译器（Ucc），并将类Unix操作系统Xv6移植到他们自制的名为GAIA的CPU上。

该项目源于一个CPU实验，该实验通常涉及设计CPU，构建一个OCaml子集的编译器，并运行一个光线追踪程序。佐伯的团队，X小组，旨在将一个操作系统移植到他们的CPU上以供娱乐。他们选择Xv6是因为它的简单性和与Unix v6的相似性。

该项目面临若干挑战，包括需要一个C编译器，理解操作系统所需的CPU特性（如特权保护和虚拟地址），一个基本的模拟器，以及Xv6的低可移植性。该团队通过构建Ucc编译器、将Xv6移植到MIPS以供学习，以及实现关键的CPU特性来克服了这些障碍。

主要成就包括GAIA的CPU设计、具有调试功能的模拟器增强、修复Ucc的char大小与Xv6的假设之间的不兼容问题，以及使用“页面着色”解决方案解决缓存别名问题。最终，Xv6在模拟器上成功运行，然后在真正的GAIA CPU上运行。作为最后的润色，他们添加了娱乐功能，例如运行sl命令并创建一个高质量的2048游戏，甚至向Xv6添加了ioctl等功能以启用它。

---

## 5. 埃里克·萨蒂逝世百年后，其未闻世作品将首演

**原文标题**: Unheard works by Erik Satie to premiere 100 years after his death

**原文链接**: [https://www.theguardian.com/music/2025/jun/26/unheard-works-by-erik-satie-to-premiere-100-years-after-his-death](https://www.theguardian.com/music/2025/jun/26/unheard-works-by-erik-satie-to-premiere-100-years-after-his-death)

埃里克·萨蒂去世百年后，二十七首此前从未公开的这位创新法国作曲家的作品即将首演。这些作品包括从歌舞厅歌曲到极简主义夜曲等多种类型，由音乐学家詹姆斯·奈和作曲家佐藤松井从在各个档案馆发现的数百本萨蒂笔记本中精心整理而成。据信，这些作品创作于20世纪初萨蒂在巴黎蒙马特波西米亚小酒馆担任钢琴师期间。

这些草稿已由著名法国钢琴家亚历山大·塔罗准备演奏，并将于周五由Erato发行一张名为《萨蒂：发现》的新专辑。奈表达了对这一发现的兴奋之情，并强调了萨蒂作品的多样性和创造性。他描述了萨蒂的创作过程，指出他经常在散步或在咖啡馆里记下想法，很少在钢琴上创作。

新发现的作品包括类似于萨蒂广为人知的《吉姆诺培迪》和《格诺西恩》的作品，例如《夜曲思考》和《围绕第一首夜曲》，以及实验性作品。7月1日萨蒂逝世一百周年将通过英国广播公司（BBC）的多个频道进行纪念。彼得·迪金森和约翰·凯奇等人物一直倡导萨蒂的遗产，进一步巩固了他对现代音乐的影响。

---

## 6. 用四十行 Awk 解析 JSON

**原文标题**: Parsing JSON in Forty Lines of Awk

**原文链接**: [https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk](https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk)

本文介绍了一个用大约 40 行 `awk` 代码编写的简洁 JSON 解析器。作者因需要在现有 POSIX shell 脚本中解析 JSON，选择了 `awk`，因为它在 POSIX 环境中普遍存在且可用，而像 `jq` 这样的替代方案需要额外的依赖项。

该解析器优先考虑简洁性，并假设输入来自可信来源的格式良好的 JSON，并承认在全面错误处理方面的局限性。它提供了一个简单的接口：`get_json_value` 函数接受一个 JSON 字符串和一个指向键或数组索引的点路径，并返回相应的值。此函数处理对象和数组，将数组视为具有整数键的对象。本文提供了完整的、带有注释的 `awk` 代码，用于 `get_json_value`，解释了它遍历 JSON 结构、识别键和值以及处理嵌套对象和数组的逻辑。

此外，本文还包括一个 `decode_json_string` 函数来处理基本的 JSON 字符串解码，特别是转义序列（不包括 Unicode 转义）。还提供了一个简单的 `error` 函数，用于进行基本的错误报告，并将输出重定向到 `stderr`。本文强调实用性和简洁性，而不是完全符合 JSON 标准，因此它适用于需要在 POSIX 环境中使用轻量级 JSON 解析解决方案的场景。

---

## 7. 展示一下：我是一名飞行员，我构建了我飞行航线的交互式图表/地球仪

**原文标题**: Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights

**原文链接**: [https://jameshard.ing/pilot](https://jameshard.ing/pilot)

飞行员自制交互式飞行日志可视化 (Show HN)

一位空客A350飞行员（英国航空副驾驶，自2016年开始飞行，最初驾驶A320系列，2023年起驾驶A350）创建了其飞行日志数据的交互式可视化。

该飞行员使用LogTen Pro进行数字化飞行记录，并使用SQL查询数据，以多种交互式格式呈现。亮点包括：

*   **GitHub风格的飞行历史：** 日历图显示每日飞行小时数，揭示了与职业变动（短途到长途）和 Covid-19 影响相关的模式。
*   **3D地球可视化：** 显示按国家和机场划分的飞行活动的地球仪。
*   **目的地矩阵：** 显示国家之间航班频率的圆形图。
*   **年度小时数图表：** 显示每年飞行的小时数，按飞行员角色（PIC，PICUS，P2，Heavy）分解，并定义英国航空环境中的PIC和PICUS等缩写。
*   **累计小时数图表：** 显示每种机型的总飞行小时数，使用ICAO代码（例如，A320系列，A350）。
*   **飞行时间和距离散点图：** 展示了飞行时间和距离之间的关系，突出了盛行风对从伦敦出发的西行航班的影响。

该项目展示了一种可视化和分析飞行数据的创造性方法，提供了对飞行员职业发展和飞行体验的洞察。

---

## 8. LMCache 实现无损 LLM 吞吐量提升 3 倍

**原文标题**: Lossless LLM 3x Throughput Increase by LMCache

**原文链接**: [https://github.com/LMCache/LMCache](https://github.com/LMCache/LMCache)

LMCache 是一种 LLM 服务引擎扩展，旨在显著提高吞吐量并降低首个 Token 生成时间 (TTFT)，尤其是在长上下文场景中。它通过缓存和重用跨不同存储位置（GPU、CPU DRAM、本地磁盘）的可重用文本的键值 (KV) 缓存来实现这一点，从而有效节省 GPU 周期并减少用户响应延迟。这种重用适用于任何重用的文本，而不仅仅是前缀。

当与 vLLM 结合使用时，LMCache 可以在多轮 QA 和 RAG 等各种 LLM 用例中提供 3-10 倍的延迟和 GPU 周期减少。

LMCache V1 的主要功能包括高性能 CPU KVCache 卸载、分离式预填充、P2P KVCache 共享、对非前缀 KV 缓存的稳定支持以及与最新 vLLM 的 pip 安装兼容性。它现在在 vLLM 生产堆栈生态系统中得到支持，并提供用户和开发者文档。

该项目正在积极开发中，每周定期举行社区会议，欢迎贡献和合作。 有几篇研究论文详细介绍了底层技术。 LMCache 根据 Apache License 2.0 获得许可。

---

## 9. 工程师利用增强现实眼镜为现实世界创建广告拦截器

**原文标题**: Engineer creates ad block for the real world with augmented reality glasses

**原文链接**: [https://www.tomshardware.com/maker-stem/engineer-creates-ad-block-for-the-real-world-with-augmented-reality-glasses-no-more-products-or-branding-in-your-everyday-life](https://www.tomshardware.com/maker-stem/engineer-creates-ad-block-for-the-real-world-with-augmented-reality-glasses-no-more-products-or-branding-in-your-everyday-life)

一名名叫Stijn Spanhove的软件工程师为Snap的AR眼镜开发了一款增强现实应用程序，可以屏蔽现实世界的广告。该应用程序使用谷歌的Gemini AI识别通过眼镜可见的广告牌、产品品牌和其他广告，并将其替换为红色方块，从而有效地为现实世界创建了一个“AdBlock”。

Spanhove在一个视频中展示了该应用程序屏蔽海报、行人广告牌甚至食品包装上的广告的能力。他设想未来用户可以用个性化内容自定义屏蔽区域。

该应用程序是使用Snap的共享库和API构建的，目前仅供Snap Spectacles用户使用。虽然其他AR平台（如Apple Vision Pro和Meta Quest）尚未得到支持，但该项目引发了人们对未来控制我们所见事物以及对广告潜在影响的质疑。

文章评论区反响不一，一些人觉得这个概念很有趣，特别是对于那些对广告敏感或有成瘾症的人。另一些人则认为红色方块比广告本身更分散注意力，或者认为在线广告拦截是一个更紧迫的问题。一位评论员表示，广告收入补贴了票价，因此在这些区域屏蔽广告可能被视为一种盗窃行为。

---

## 10. 自行车地图史

**原文标题**: History of Cycling Maps

**原文链接**: [https://cyclemaps.blogspot.com/](https://cyclemaps.blogspot.com/)

本网站提供全面的自行车地图历史，精选并修复了来自主要供应商的一百多份重要摘录。专为对该主题感兴趣的公众创建，它作为一个电子“咖啡桌”读物，供休闲浏览和事实参考，而不是一个带有评论和论坛的传统博客。

该网站最初于2021年发布，现已扩展，包含以下主题的专门页面：

*   **简介：** 为该主题奠定基础。
*   **自行车运动的发展：** 将自行车运动对地图制作的影响置于背景之中。
*   **独立地图出版商：** 探索各个地图出版商的贡献。
*   **来源和参考：** 为所呈现的信息提供基础。
*   **如何确定自行车地图的年代：** 确定地图年代的指南。
*   **黑色博物馆 - 地图错误：** 突出显示自行车地图中发现的错误和奇闻异事。

内容并非以博文形式呈现，而是组织成可通过主页访问的独立页面，为对自行车地图的历史和演变感兴趣的人提供结构化的信息体验。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 2 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 3 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 4 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 5 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 6 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 7 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 8 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 9 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 10 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 11 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 12 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 13 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 14 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 15 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 16 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 17 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 18 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 19 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 20 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 21 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 22 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 23 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 24 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 25 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 26 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 27 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 28 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 29 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 30 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 31 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 32 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 33 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 34 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 35 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 36 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 37 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 38 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 39 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 40 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 41 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 42 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 43 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 44 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 45 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 46 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 47 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 48 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 49 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 50 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 51 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 52 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 53 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 54 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 55 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 56 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 57 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 58 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 59 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 60 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 61 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 62 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 63 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 64 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 65 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 66 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 67 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 68 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 69 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 70 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 71 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 72 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 73 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 74 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 75 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 76 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 77 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 78 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 79 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 80 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 81 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 82 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 83 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 84 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 85 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 86 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 87 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 88 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 89 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 90 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 91 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 92 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 93 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 94 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 95 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 96 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 97 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 98 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 99 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 100 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 101 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
