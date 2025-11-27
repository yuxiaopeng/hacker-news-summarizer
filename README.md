# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-27.md)

*最后自动更新时间: 2025-11-27 17:47:29*
## 1. 骁龙 8 Elite Gen 5 芯片当日提交 Linux 上游支持

**原文标题**: Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

**原文链接**: [https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support](https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support)

文章《骁龙8 Elite Gen 5当日上游Linux支持》宣布骁龙8 Elite Gen 5芯片组可立即获得上游Linux支持。这意味着用户和开发者可以在搭载该处理器的设备发布之时，即可使用标准、未经修改的Linux内核。这消除了对定制内核或等待社区移植的需求，从而带来更精简的开发和使用体验。当日上游支持的可用性是一项重大进步，与依赖于供应商特定的或树外解决方案相比，它可能简化软件集成、提高安全性并实现更快的特性更新。简短的内容表明，这对Linux社区和骁龙8 Elite Gen 5的采用者来说是一个积极的消息。

---

## 2. 我们正在因为大型语言模型而失去自我表达的声音

**原文标题**: We're Losing Our Voice to LLMs

**原文链接**: [https://tonyalicea.dev/blog/were-losing-our-voice-to-llms/](https://tonyalicea.dev/blog/were-losing-our-voice-to-llms/)

本文认为，社交媒体上大型语言模型（LLM）的日益普及正在侵蚀个人声音，并造成同质化的在线形象。作者认为，依赖 LLM 生成帖子是一个错误，因为个人声音是一种宝贵的资产。

作者强调个人声音的独特性，它由个人经历塑造并随着时间的推移而演变。这种独特的声音是可识别的，可以促进联系和信任，并且对于在职业和个人环境中留下积极印象至关重要。作者分享了一个个人轶事，讲述了因为独特的写作风格而获得一份工作。

本文警告说，使用 LLM 以“你的声音”写作是不够的，因为真正的声音是动态的，并且对生活经历和情感做出反应。作者认为，允许 LLM 主导在线交流会导致认知上的懒惰，并使这种宝贵的资产萎缩。

结论敦促读者优先考虑自己的真实声音，而不是 LLM 生成的内容。作者强调个人视角的重要性，并反对通过人工智能同质化在线交流。核心信息是一个行动呼吁：培养和表达你独特的声音，而不是将其交给 LLM。

---

## 3. 亚瑟·柯南·道尔通过夏洛克·福尔摩斯探索男性心理健康

**原文标题**: Arthur Conan Doyle explored men’s mental health through Sherlock Holmes

**原文链接**: [https://scienceclock.com/arthur-conan-doyle-delved-into-mens-mental-health-through-his-sherlock-holmes-stories/](https://scienceclock.com/arthur-conan-doyle-delved-into-mens-mental-health-through-his-sherlock-holmes-stories/)

本文认为，亚瑟·柯南·道尔利用他的夏洛克·福尔摩斯故事，探讨了维多利亚时代男性精神健康和脆弱性这一禁忌话题。道尔借鉴了他自己家庭中父亲酗酒和精神疾病的经历，塑造了夏洛克·福尔摩斯这一角色，尽管他天赋异禀，却也与毒瘾、孤独和抑郁作斗争，从而使读者产生共鸣。

本文重点介绍了《歪唇男人》、《工程师的大拇指》和《证券经纪人的书记员》等故事，其中男性角色面临着情绪动荡、背叛和道德困境。道尔利用这些叙事来审视维多利亚时代社会对男性气概的期望以及男性面临的压力，特别是关于经济稳定和声誉方面。他描绘了男性与羞耻、恐惧和自杀的可能性作斗争的场景。

作者强调，福尔摩斯不仅是一位侦探，还是这些男性的保护者、知己和安慰者，为他们提供身体和心理上的支持。通过展示福尔摩斯对客户身心创伤的关注，道尔强调了对男性进行心理支持的重要性。文章总结道，虽然当代读者可能更关注福尔摩斯的天赋，但这些故事为我们提供了了解维多利亚时代男性精神困境的宝贵视角，并与现代读者建立了联系。

---

## 4. Show HN: Runprompt – 从命令行运行 .prompt 文件

**原文标题**: Show HN: Runprompt – run .prompt files from the command line

**原文链接**: [https://github.com/chr15m/runprompt](https://github.com/chr15m/runprompt)

`runprompt` 是一个单文件 Python 脚本，使用户能够从命令行执行 `.prompt` 文件，从而方便与各种 AI 模型进行交互。提示词的结构包含前置元数据（模型选择、输入/输出模式）和一个模板提示词正文。

主要功能包括：

*   **轻松设置：** 使用 `curl` 和 `chmod` 下载并执行。
*   **Stdin 集成：** `{{STDIN}}` 变量允许将文本通过管道传递到提示词中。
*   **结构化输出：** 定义输出模式以进行结构化 JSON 提取，从而实现数据处理。
*   **提示词链：** 将一个提示词的 JSON 输出通过管道作为另一个提示词的输入。
*   **CLI 覆盖：** 从命令行覆盖前置元数据值（例如，指定不同的模型）。
*   **环境变量配置：** 设置 API 密钥（ANTHROPIC\_API\_KEY、OPENAI\_API\_KEY、GOOGLE\_API\_KEY、OPENROUTER\_API\_KEY）并通过 `RUNPROMPT_*` 变量覆盖前置元数据。
*   **详细模式：** 使用 `-v` 进行请求/响应调试。
*   **供应商支持：** 它支持 Anthropic、OpenAI、Google AI 和 OpenRouter 模型。 OpenRouter 为多个供应商提供统一的 API。 模型选择遵循 `provider/model-name` 格式。

---

## 5. Linux内核探索

**原文标题**: Linux Kernel Explorer

**原文链接**: [https://reverser.dev/linux-kernel-explorer](https://reverser.dev/linux-kernel-explorer)

"Linux内核探险家"提供了一个交互式资源，用于学习Linux内核，其基于Moon Hee Lee的著作"The Kernel in The Mind"。它强调**内核不是一个进程，而是系统本身**，服务于用户进程并连接硬件和软件。它协调系统调用、中断和调度，以保持用户任务的运行。

该平台提供结构化的学习路径，从理解内核与进程的根本区别及其作为权威的角色开始。它突出了内核的**分层系统：虚拟的、映射的、隔离的和受控的**。

该资源允许用户通过文件浏览器直接探索内核源代码，提供对诸如`init/main.c`、`kernel/fork.c`、`include/linux/sched.h`和`arch/x86/kernel/entry_64.S`等关键文件的访问。每个章节都建立在前一个章节的基础上，涵盖从系统基础和内存管理到调度和虚拟化的主题。

每章末尾都包含知识检查，以测试理解情况。最终目标是通过交互式探索和结构化学习，更深入地理解Linux内核的架构和功能。

---

## 6. 雷神之锤引擎指标

**原文标题**: Quake Engine Indicators

**原文链接**: [https://fabiensanglard.net/quake_indicators/index.html](https://fabiensanglard.net/quake_indicators/index.html)

Fabien Sanglard 的这篇文章深入探讨了原始 Quake 引擎中隐藏的“指示器”，这些指示器可以在游戏文件中找到。这些图标，TURTLE、RAM、DISC 和 NET，旨在提供关于游戏性能的反馈。

当帧率降至 10 fps 以下时，TURTLE 指示器就会出现，主要用于开发者和地图设计师识别由于过多多边形或低效代码导致的性能瓶颈。命令 `showturtle 1/0` 控制其可见性。

RAM 指示器警告“表面缓存颠簸”，这是一个关键的性能问题，即引擎被迫重复生成和丢弃表面数据（纹理和光照贴图的组合）。当地图几何体超过引擎的表面缓存容量时，就会出现这种情况，导致帧率严重下降。这很可能帮助地图设计师优化地图复杂性。

DISC 指示器通过 `Sys_FileRead` 反映 HDD 访问，主要显示加载活动。虽然最初旨在提供玩家反馈，但它与 TURTLE 指示器的重叠可能限制了其在开发过程中的效用。

最后，NET 指示器表示来自服务器的网络数据包丢失超过 300 毫秒，从而告知玩家潜在的连接问题和糟糕的延迟。

作者最后用一个场景来说明所有指示器同时出现的情况，代表着一个充斥着性能和连接问题的灾难性游戏体验。

---

## 7. Penpot：开源的Figma

**原文标题**: Penpot: The Open-Source Figma

**原文链接**: [https://github.com/penpot/penpot](https://github.com/penpot/penpot)

Penpot 是一个开源的设计与代码协作工具，定位为 Figma 的替代品。它赋能设计师创建设计稿、原型和设计系统，同时为开发者提供可直接使用的代码，从而简化设计-代码工作流程，消除交接问题。Penpot 支持 SVG、CSS、HTML 和 JSON 等开放标准，免费使用，并可通过浏览器部署或自托管。

最近的更新包括原生设计令牌集成，以提高效率和协作；主要的 2.0 版本引入了 CSS Grid Layout、UI 重新设计以及新的组件系统。需要额外支持的组织可以联系 Penpot 寻求服务。文章重点介绍了即将于 2025 年在马德里举行的 Penpot Fest。

Penpot 的主要优势包括用于扩展功能的插件系统、实时协作或单人工作选项、用于即时代码访问的检查模式，以及具有设计令牌、组件和变体的设计系统支持。Penpot 是部署无关的，提供 Docker 和 Kubernetes 等安装选项。

文章强调了社区参与的重要性，邀请通过代码、设计分享、错误报告、翻译和反馈进行贡献。资源包括文档、教程和开发者日志。Penpot 在 Mozilla Public License v2.0 许可下授权，是 Kaleidos INC. 的一个项目。

---

## 8. Show HN: MkSlides – 用类似于 MkDocs 的工作流程将 Markdown 转换为幻灯片

**原文标题**: Show HN: MkSlides – Markdown to slides with a similar workflow to MkDocs

**原文链接**: [https://github.com/MartenBE/mkslides](https://github.com/MartenBE/mkslides)

MkSlides是一个静态站点生成器，它使用Reveal.js将Markdown文件转换为视觉上吸引人的幻灯片。它提供类似于MkDocs的工作流程，简化了从使用单个YAML文件配置的Markdown源文件创建演示文稿的过程。

主要功能包括：从Markdown构建静态HTML幻灯片；支持单个Markdown文件或目录来创建幻灯片；易于在各种平台上部署；使用python-livereload的实时预览功能；可使用网站图标、CSS主题和模板进行自定义；以及表情符号支持。

使用`pip install mkslides`即可轻松安装。 `mkslides build`命令从Markdown文件生成静态站点，可以在指定的文件夹（例如，`mkslides build slides/`）或单个文件（例如，`mkslides build test.md`）中生成。 `mkslides serve`命令在编辑期间提供实时预览。 YAML配置文件（mkslides.yml）允许自定义索引页和单个幻灯片，包括主题、标题、reveal.js选项和插件。 Markdown文件还可以使用Frontmatter来覆盖每个幻灯片的配置选项。 该工具提供了广泛的自定义功能，允许用户定制幻灯片的外观和功能。 展示其可能性的示例，包括Mermaid.js和PlantUML支持，可在网上找到。

---

## 9. 二维光线步进软阴影（2020）

**原文标题**: Ray Marching Soft Shadows in 2D (2020)

**原文链接**: [https://www.rykap.com/2020/09/23/distance-fields/](https://www.rykap.com/2020/09/23/distance-fields/)

本文阐述了如何使用距离场在2D中实现光线步进软阴影。作者描述了一种创建视觉上吸引人但物理上不精确的、且性能良好的软阴影的方法。

核心思想是光线步进：通过从像素向光源追踪光线来计算该像素是否处于阴影中。该算法不是采用固定大小的步长，而是使用距离场来确定每一步沿光线推进的最大安全距离，避免跳过潜在的遮挡物。

文章随后详细介绍了创建软阴影的三个规则：

1.  光线越接近与形状相交，像素应该被阴影覆盖得越多。这可以通过在光线步进过程中到场景的最小距离来近似。
2.  像素距离近交点越远，阴影应该越分散。这可以通过总的光线推进距离来近似。
3.  光照强度随距离减弱，通过二次衰减来实现。

作者使用 GLSL 代码片段来说明这些规则的实现，将最小距离比率 (sceneDist / rayProgress) 与距离因子相结合。

最后，作者承认了这种技术的常见伪像：条带化。他们提到了两种缓解方法：使用对光线到场景距离的改进近似，以及在光线步进的步长中引入随机抖动。他们指出后者是在条带化和颗粒感之间的一种权衡，并且他们对改进持开放态度。

---

## 10. DIY NAS：2026版

**原文标题**: DIY NAS: 2026 Edition

**原文链接**: [https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html](https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html)

作者在本篇博文中详细介绍了他们2026年DIY NAS的构建过程，延续了他们每年分享构建网络附加存储服务器经验的传统。核心标准保持不变：小尺寸规格、至少六个硬盘位、低功耗CPU以及用于虚拟机和容器的家庭实验室潜力。

作者强调了组件价格上涨的挑战，尤其是硬盘、固态硬盘和内存。尽管如此，他们还是决定继续构建，预计未来可能会进一步上涨。

选择的组件包括采用英特尔酷睿3 N355 CPU的Topton N22主板，为家庭实验室使用提供更高的性能。对于机箱，选择了JONSBO N4，因为它占用空间更小且具有六个3.5英寸硬盘位，尽管在硬盘访问方面存在一些限制。为了解决潜在的噪音问题，选择了Noctua NF-A12x25 PWM风扇。

作者使用了原有的32GB DDR5内存。一对128GB Silicon Power A55 SATA固态硬盘用作启动盘，两块1TB Silicon Power NVMe固态硬盘用于应用程序和虚拟机。由于成本高昂，作者选择使用退役的硬盘进行批量存储测试。他们还强调了选择合适硬盘的重要性。

对于操作系统，选择了TrueNAS Community Edition（版本25.10.0.1），因为它具有企业级功能且易于使用。

构建的最终成本（不包括批量存储硬盘）约为989.36美元，总计1,189.34美元。作者还简要概述了组装过程，指出电源的电缆管理面临挑战，并且在没有SATA背板的情况下难以在托架中安装硬盘。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 2 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 3 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 4 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 5 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 6 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 7 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 8 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 9 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 10 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 11 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 12 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 13 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 14 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 15 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 16 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 17 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 18 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 19 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 20 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 21 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 22 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 23 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 24 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 25 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 26 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 27 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 28 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 29 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 30 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 31 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 32 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 33 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 34 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 35 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 36 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 37 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 38 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 39 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 40 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 41 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 42 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 43 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 44 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 45 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 46 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 47 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 48 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 49 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 50 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 51 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 52 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 53 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 54 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 55 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 56 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 57 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 58 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 59 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 60 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 61 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 62 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 63 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 64 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 65 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 66 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 67 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 68 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 69 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 70 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 71 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 72 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 73 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 74 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 75 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 76 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 77 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 78 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 79 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 80 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 81 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 82 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 83 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 84 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 85 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 86 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 87 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 88 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 89 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 90 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 91 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 92 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 93 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 94 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 95 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 96 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 97 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 98 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 99 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 100 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 101 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 102 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 103 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 104 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 105 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 106 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 107 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 108 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 109 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 110 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 111 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 112 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 113 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 114 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 115 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 116 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 117 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 118 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 119 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 120 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 121 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 122 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 123 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 124 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 125 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 126 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 127 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 128 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 129 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 130 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 131 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 132 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 133 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 134 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 135 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 136 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 137 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 138 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 139 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 140 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 141 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 142 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 143 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 144 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 145 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 146 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 147 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 148 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 149 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 150 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 151 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 152 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 153 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 154 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 155 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 156 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 157 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 158 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 159 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 160 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 161 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 162 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 163 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 164 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 165 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 166 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 167 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 168 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 169 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 170 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 171 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 172 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 173 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 174 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 175 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 176 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 177 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 178 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 179 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 180 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 181 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 182 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 183 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 184 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 185 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 186 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 187 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 188 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 189 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 190 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 191 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 192 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 193 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 194 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 195 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 196 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 197 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 198 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 199 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 200 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 201 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 202 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 203 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 204 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 205 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 206 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 207 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 208 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 209 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 210 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 211 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 212 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 213 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 214 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 215 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 216 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 217 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 218 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 219 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 220 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 221 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 222 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 223 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 224 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 225 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 226 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 227 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 228 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 229 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 230 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 231 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 232 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 233 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 234 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 235 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 236 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 237 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 238 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 239 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 240 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 241 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 242 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 243 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 244 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 245 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 246 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 247 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 248 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 249 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 250 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 251 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 252 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
