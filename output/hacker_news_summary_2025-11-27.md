# Hacker News 热门文章摘要 (2025-11-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Mixpanel 安全漏洞

**原文标题**: Mixpanel Security Breach

**原文链接**: [https://mixpanel.com/blog/sms-security-incident/](https://mixpanel.com/blog/sms-security-incident/)

2025年11月8日，Mixpanel遭遇一起短信诈骗安全事件，导致少量客户帐户遭到未经授权的访问。Mixpanel迅速启动事件响应协议，努力控制漏洞、消除威胁并保护受影响的用户帐户。他们还与外部网络安全专家合作进行补救和响应。

Mixpanel主动联系了所有受影响的客户。未收到通知的客户未受影响。

Mixpanel采取的行动包括：

*   撤销活动会话和登录，以保护受影响的帐户。
*   轮换受影响帐户的泄露凭据。
*   阻止恶意 IP 地址并注册入侵指标 (IOC)。
*   对所有 Mixpanel 员工执行全局密码重置。
*   聘请第三方取证公司提供指导。
*   对相关日志进行取证审查。
*   实施增强的安全控制，以防止未来发生类似事件。
*   通知执法部门和网络安全顾问。

受影响的客户被指示查看 Mixpanel 的通知，了解已采取的具体步骤和任何需要采取的行动。未受影响的客户无需采取任何行动。Mixpanel 强调其对安全和透明度的承诺，并通过 support@mixpanel.com 提供支持，解答任何疑问。该公告由 CEO Jen Taylor 发布。

---

## 12. 交互式λ演算化简

**原文标题**: Interactive λ-Reduction

**原文链接**: [https://deltanets.org/](https://deltanets.org/)

本文提供了一个交互式环境，用于探索λ归约，λ演算中的一个基本过程。这种交互性意味着用户可以逐步执行归约并观察变化。

列出的例子突出了λ归约的各个方面：

*   **入门：** 可能介绍基本概念。
*   **Lamping A/B：** 表明例子利用了Lamping的优化，与共享和高效归约有关。
*   **列表头：** 演示了应用于数据结构的λ归约，特别是列表。
*   **Ω & Y (非正规化)：** 展示了不会终止的例子，说明了λ演算中非终止的可能性。
*   **两次平方：** 一个数值例子，展示了通过λ归约进行计算。
*   **擦除 vs 共享/复制器衰减：** 探讨了不同归约策略对资源使用的影响。
*   **图着色：** 可能演示了λ演算在图论问题中的应用。
*   **Δ-网络：** 一个更高级的主题，可能与优化或替代归约策略有关。

提及 "λ演算 (1936+)" 强调了该主题的历史背景。"绝对级别（默认）、相对级别、线性 (L)、仿射 (A)、相关 (I)、完全 (K)、0/0" 等选项可能指的是影响归约过程和资源管理的不同评估策略或限制。GitHub 链接提供了对底层代码的访问权限，并且可能包含更详细的文档。

本质上，这是一个学习资源，通过交互式示例和可定制的评估策略，提供了一种亲身体验的方式来理解λ归约及其复杂性。

---

## 13. 音乐能减轻手术痛苦，加速康复，研究发现

**原文标题**: Music eases surgery and speeds recovery, study finds

**原文链接**: [https://www.bbc.com/news/articles/c231dv9zpz3o](https://www.bbc.com/news/articles/c231dv9zpz3o)

最近发表在《音乐与医学》杂志上的一项印度研究发现，在全身麻醉手术期间播放音乐可以减轻手术过程并加速恢复。德里莫拉纳·阿扎德医学院和洛克·纳亚克医院的研究人员发现，在腹腔镜胆囊切除术期间通过耳机聆听舒缓器乐的患者，需要更低剂量的麻醉药物，特别是丙泊酚和芬太尼。

该研究涉及 56 名成年人，他们被随机分为两组，都接受了标准的五种药物治疗方案。一组聆听舒缓的音乐（长笛或钢琴），另一组没有。听音乐组经历了更平稳的恢复，更低的应激激素（皮质醇）水平，以及在手术期间更好的血压控制。

研究人员认为，即使在麻醉状态下，听觉通路仍然活跃，使大脑能够感知音乐并平息身体对手术的应激反应。这种应激反应的特点是心率加快、激素激增和血压飙升，会阻碍恢复并加剧炎症。通过用音乐减轻这种反应，患者可以更快、更清醒地醒来，从而可能导致更早的出院和更好的疼痛管理。

这项研究强调了诸如音乐之类的非药物干预措施在人性化手术室和改善手术福祉方面的潜力。尽管音乐疗法已在其他医学领域得到确立，但将其整合到麻醉中代表着一个新的领域，表明简单的干预措施可以对患者的治疗结果产生积极影响。该团队计划在未来的研究中进一步探索音乐辅助镇静。

---

## 14. G0-G3圆角可视化：了解什么是“苹果圆角”

**原文标题**: G0-G3 corners, visualised: learn what "Apple corners" are

**原文链接**: [https://www.printables.com/model/1490911-g0-g3-corners-visualised-learn-what-apple-corners](https://www.printables.com/model/1490911-g0-g3-corners-visualised-learn-what-apple-corners)

无法访问文章链接。

---

## 15. 布里斯托尔的水泥浮桥

**原文标题**: The Concrete Pontoons of Bristol

**原文链接**: [https://thecretefleet.com/blog/f/the-concrete-pontoons-of-bristol](https://thecretefleet.com/blog/f/the-concrete-pontoons-of-bristol)

这段摘录将“布里斯托尔的混凝土浮筒”作为关于混凝土船只的更大在线资源的一部分进行介绍。它托管在“克里特舰队”网站上，该网站专注于一战和二战时期的混凝土船只以及马尔贝里港的组成部分。该网站提供与混凝土船只相关的百科全书、博客和视频。提供的文本强调了版权保护以及使用Cookie进行网站流量分析和优化，并请求用户接受Cookie的使用和数据汇总。本质上，这里没有总结文章本身，而是描述了*包含*该文章的网站的框架。

---

## 16. 威利斯·惠特菲尔德：当今仍在使用的洁净室技术创造者 (2024)

**原文标题**: Willis Whitfield: Creator of clean room technology still in use today (2024)

**原文链接**: [https://www.sandia.gov/labnews/2024/04/04/willis-whitfield-a-simple-man-with-a-simple-solution-that-changed-the-world/](https://www.sandia.gov/labnews/2024/04/04/willis-whitfield-a-simple-man-with-a-simple-solution-that-changed-the-world/)

桑迪亚国家实验室的物理学家威利斯·惠特菲尔德于1961年发明了现代洁净室，彻底改变了制造业和诸多其他领域。由于颗粒物污染影响复杂部件的生产，惠特菲尔德构思了层流的概念，即通过高过滤空气不断吹扫房间以去除颗粒物。这一概念大大降低了颗粒物数量，使洁净度比现有洁净室提高了1000倍。

惠特菲尔德在飞机平板电脑上绘制的设计图，成为了电子、制药、医疗保健和航空航天领域所用洁净室的基础。他的发明于1964年获得专利，并迅速被各大行业采用。

惠特菲尔德以谦逊和乐于赞扬团队而闻名，他还为包括污水处理和航天器消毒在内的其他项目做出了贡献。他在桑迪亚工作了30年。

惠特菲尔德于2012年去世。2014年，他入选美国国家发明家名人堂，并在桑迪亚竖立了一座雕像以示纪念。他的发明在当今无数应用中仍然至关重要。

---

## 17. Gemini CLI Agentic 编码技巧

**原文标题**: Gemini CLI Tips and Tricks for Agentic Coding

**原文链接**: [https://github.com/addyosmani/gemini-cli-tips](https://github.com/addyosmani/gemini-cli-tips)

本文全面介绍了 Gemini CLI 的使用方法，这是一款开源 AI 助手，可将 Google 的 Gemini 模型引入您的终端进行自主编码。它充当了一个超级强大的结对程序员，擅长编码任务、调试、内容生成以及通过自然语言提示实现系统自动化。

本文提供了使用 Google 账户或 API 密钥设置 Gemini CLI 的详细说明。本指南的大部分内容专门介绍了大约 30 条专业技巧，提供了对高级用法和隐藏功能的见解。 主要技巧包括：

*   **持久上下文 (GEMINI.md):** 创建一个 `GEMINI.md` 文件，其中包含项目特定的说明，以便 AI 记住。
*   **自定义斜杠命令：** 在 TOML 文件中定义可重用的提示模板，以自动化重复性任务。
*   **MCP 服务器：** 通过自定义模型上下文协议 (MCP) 服务器，集成外部系统或自定义工具，从而扩展 Gemini 的功能。
*   **记忆添加与召回：** 使用 `/memory add` 存储重要事实以供日后参考。
*   **检查点：** 使用 `/checkpoint` 和 `/restore` 实现撤消功能。
*   **文件引用：** 使用 `@` 引用文件和图像以获得明确的上下文。
*   **直通 Shell 命令：** 使用 `!` 直接执行 Shell 命令。

本文还介绍了系统故障排除、以无头模式运行 Gemini CLI、管理聊天会话、利用多模态 AI、使用设置自定义 CLI、与 IDE 集成以及使用 GitHub Actions 自动化存储库任务的技巧。它强调了在使用自定义 MCP 工具时的安全性，并提供了使用 Gemini CLI 组织项目和工作流程的最佳实践。

---

## 18. Show HN: SyncKit – 离线优先同步引擎 (Rust/WASM 与 TypeScript)

**原文标题**: Show HN: SyncKit – Offline-first sync engine (Rust/WASM and TypeScript)

**原文链接**: [https://github.com/Dancode-188/synckit](https://github.com/Dancode-188/synckit)

SyncKit是一个生产就绪的、离线优先的同步引擎，旨在简化本地优先应用程序的构建。它允许开发者以最少的代码为他们的应用添加实时同步功能，解决了从头构建同步或使用现有解决方案（如Firebase、Supabase或Yjs）所带来的复杂性和成本。

SyncKit的关键优势包括真正的离线操作、小巧的软件包体积（压缩后约59KB，精简版约45KB）、开源和自托管特性、快速的性能，以及通过冲突解决和形式验证来保证的数据完整性。

SyncKit提供诸如实时协作、网络协议支持、IndexedDB持久化和跨标签页同步等功能。未来版本承诺提供文本CRDT、计数器和集合。它通过真正地离线优先（不同于Firebase/Supabase）、提供多语言服务器（不同于Yjs）以及提供比Automerge更小的软件包和更快的性能来突出自身优势。

该文章详细介绍了快速入门指南、核心功能、框架集成（React hooks）、架构概述以及与竞争解决方案的比较。它强调了SyncKit适用于各种用例，从简单的对象同步到协作文本编辑和自定义CRDT。路线图包括多语言服务器支持和高级存储选项等功能。文章最后介绍了贡献指南、企业支持信息、展示其性能和软件包大小优势的基准测试，以及对灵感的致谢。

---

## 19. S&box现在是一个开源游戏引擎

**原文标题**: S&box is now an open source game engine

**原文链接**: [https://sbox.game/news/update-25-11-26](https://sbox.game/news/update-25-11-26)

文章：《S&box现已开源游戏引擎》宣布，Garry's Mod的继任者S&box已转型为开源模式。这对该平台而言是一项重大变革，意味着引擎的源代码现在已公开可用。

虽然文章非常简短，但这一转变可能意味着开发者和社区成员现在可以为S&box的开发做出贡献，修改其核心功能，并可能创建自定义引擎版本。这种更高的可访问性和社区参与度可能会带来更快的创新、错误修复和更广泛的功能。引擎的开源表明了对透明度和协作开发的承诺，可能会吸引更大的开发者群体，并培养一个更强大、更具适应性的平台，用于创建和分享游戏和体验。“s&box”这个名称被明确提及，作为此公告的主题。

---

## 20. 在过时设备上运行不受支持的 iOS

**原文标题**: Running Unsupported iOS on Deprecated Devices

**原文链接**: [https://nyansatan.github.io/run-unsupported-ios/](https://nyansatan.github.io/run-unsupported-ios/)

本文详细介绍了在iPod touch 3上运行不受支持的iOS 6的过程，该设备官方限制为iOS 5.1.1。作者概述了关键的iOS组件：iBoot、内核缓存（Kernelcache）、设备树（DeviceTree）、用户空间文件系统和固件。

最初的方法包括修改设备树（特定设备使用的硬件结构化列表）和iBoot（引导加载程序），使其从支持iOS 6的iPhone 3GS兼容iPod touch 3。创建了一个Python脚本来比较和应用设备树差异。iBoot的修改包括签名检查、boot-args注入、动态填充nvram-proxy-data（NVRAM转储属性）和启用调试补丁。

最具挑战性的方面是创建兼容的内核缓存（操作系统内核和内核扩展）。动态加载kexts（内核扩展）被证明是不成功的，因此采用了使用旧版Mac OS X中的工具创建预链接内核缓存的方法。这涉及到使用“kcgen”来组合内核和kexts，剥离不必要的数据，并压缩结果。

该过程还需要修改Restore ramdisk文件系统以安装iBoot漏洞，以及Root文件系统，其中包括添加硬件功能plist、合并Home屏幕布局、添加固件和修补FairPlay守护进程。需要DYLD共享缓存补丁来解决产品ID不匹配和设备变体确定的问题。最后，通过重新计算已修改页面的SHA-1哈希值来修复共享缓存文件的代码签名。

作者总结说，这个过程虽然具有挑战性，但却是可以实现的，并建议未来的工作可以包括越狱修改后的系统，并将类似的技术应用于其他已弃用的设备，如iPad 1。

---

## 21. 丹尼斯·休厄尔《叛徒》书评

**原文标题**: 'Turncoat' by Dennis Sewell Review

**原文链接**: [https://www.historytoday.com/archive/review/turncoat-dennis-sewell-review](https://www.historytoday.com/archive/review/turncoat-dennis-sewell-review)

杰基·伊尔斯评丹尼斯·休厄尔《变节者：从圆颅党到保皇党，克伦威尔间谍的双面人生》一书，探讨了乔治·唐宁引人入胜的一生。尽管唐宁在17世纪的英国扮演了重要角色，但他在很大程度上被历史所忽视。这本传记深入研究了唐宁在动荡的政治环境中游刃有余的能力，他以同样的成功为奥利弗·克伦威尔和查理二世效力。

唐宁出生于一个与马萨诸塞湾殖民地有关联的清教徒家庭，早年在哈佛接受教育，之后成为新模范军的牧师。他迅速晋升，成为克伦威尔的侦察总长，雇佣间谍网络并将对手变成告密者。他收集情报的能力被证明对巩固克伦威尔的权力至关重要。

在王政复辟之后，唐宁巧妙地过渡到为查理二世服务，并继续担任他在海牙的外交职位。休厄尔推测唐宁是如何做到这一点的，提出了从秘密会议到敲诈勒索等可能性。一个特别令人发指的行为是唐宁策划绑架和引渡弑君者，包括他的前同事约翰·奥基。

唐宁为查理二世服务给他带来了财富、从男爵爵位和重大影响力。他为美国事务提供建议，包括收购纽约。尽管他取得了成功，但他也被怀疑腐败，并受到一些人的鄙视，包括塞缪尔·佩皮斯。

虽然休厄尔的传记揭示了唐宁的政治手腕和间谍活动，但伊尔斯指出，唐宁的个人生活仍然难以捉摸。这本书描绘了一个引人注目的、秘密且道德上模棱两可的人物，他在塑造17世纪的英国方面发挥了关键作用。

---

## 22. Coq：世界最佳宏汇编器？(2013) [pdf]

**原文标题**: Coq: The World's Best Macro Assembler? (2013) [pdf]

**原文链接**: [https://nickbenton.name/coqasm.pdf](https://nickbenton.name/coqasm.pdf)

这篇 2013 年的 PDF 文档，标题颇具挑衅意味：“Coq：世界上最好的宏汇编器？”，探讨了 Coq 证明助手（一种主要用于验证数学定理的系统）作为宏汇编器的非传统用法。

虽然并非传统汇编器，该论文可能研究了如何利用 Coq 强大的类型系统和证明能力来严格定义和操作底层代码表示。这可能涉及正式指定指令集架构 (ISA)，然后从更高级别的规范生成机器代码，同时证明生成代码的正确性。

该标题暗示了一种可能带有玩笑意味的探索，强调了与传统汇编器相比，Coq 在保证汇编代码的正确性和安全性方面的潜力。 使用 Coq 可确保生成的机器代码符合正式规范。这在代码正确性至关重要的高保证系统中尤其具有吸引力。 它可能讨论了为此目的使用证明助手的挑战，例如陡峭的学习曲线、形式化汇编代码语义的复杂性以及潜在的高编译时间。 它强调正确性保证。

---

## 23. GPL协议在人工智能模型中的传播状况

**原文标题**: The State of GPL Propagation to AI Models

**原文链接**: [https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/](https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/)

开源许可法律解释差异及其对人工智能模型的影响

---

## 24. 最接近整数的调和数

**原文标题**: Closest Harmonic Number to an Integer

**原文链接**: [https://www.johndcook.com/blog/2025/11/19/closest-harmonic-number-to-an-integer/](https://www.johndcook.com/blog/2025/11/19/closest-harmonic-number-to-an-integer/)

本文探讨了寻找最接近给定整数 (m) 的调和数 (Hn) 的问题。由于当 n > 1 时，调和数永远不是整数，因此目标是确定使 Hn 与 m 之间差异最小的 'n'。

挑战在于高效计算调和数，尤其是在 'n' 很大时。本文提出了一种混合方法：对于较小的 'n' (< 1000)，采用直接计算（倒数和）的方式，对于较大的 'n'，则使用欧拉-马斯刻若尼常数 (γ) 进行渐近近似。这种近似方法平衡了准确性和计算速度。

为了找到最佳的 'n'，代码首先使用近似公式 n ≈ exp(m - γ) 估计一个起始点。然后，围绕此猜测进行迭代，增加或减少 'n'，直到 Hn 夹住目标值 'm'。最后，它精确地搜索这个夹住的范围，以确定使 Hn 与 m 之间绝对差最小的 'n'。

提供的 Python 代码实现了这种方法，包括 Hn 的直接计算和渐近近似函数，以及用于查找最接近的调和数的函数 `nearest_harmonic_number(m)`。文章通过示例演示了代码的使用方法，说明了如何找到最接近整数 (10) 和实数 (√20) 的调和数。

---

## 25. 函数式数据结构与算法：一种证明助手方法

**原文标题**: Functional Data Structures and Algorithms: a Proof Assistant Approach

**原文链接**: [https://fdsa-book.net/](https://fdsa-book.net/)

函数式数据结构与算法：一种证明助手方法

这本ACM Books出版物《函数式数据结构与算法：一种证明助手方法》在函数式编程的背景下介绍了数据结构和算法。其主要特点是强调对功能正确性和运行时间分析进行严格的证明。这些证明以统一的风格呈现，使用关于函数式程序及其性能特征的归纳推理。

重要的是，书中提出的所有证明都已使用Isabelle证明助手进行了正式验证。本书的PDF版本包含指向相应Isabelle理论的链接，允许读者直接检查机器验证的证明。

本书旨在成为一份不断发展的文档，随着社区的贡献而不断演变。作者鼓励读者参与其中，并为本书的持续发展做出贡献。目标读者是对在函数式编程范式中学习数据结构和算法感兴趣的人，尤其侧重于使用证明助手进行形式验证。本书通过在一个可证明的框架内集成正确性和性能分析，提供了一种独特的视角。

---

## 26. 旅行者1号即将到达距离地球一光天之处。

**原文标题**: Voyager 1 is about to reach one light-day from Earth

**原文链接**: [https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/](https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/)

美国宇航局的旅行者1号于1977年发射，即将达到一个里程碑：到2026年11月15日，它将到达距离地球一光日的位置，即161亿英里（259亿公里）。这意味着无线电信号需要整整24小时才能到达该探测器。旅行者1号是距离地球最远的人造物体，于2012年进入星际空间。

它以大约每秒11英里（17.7公里/秒）的速度飞行，每年增加大约3.5个天文单位的距离。尽管历史悠久且太空环境恶劣，旅行者1号仍在不断传输数据，这要归功于它的放射性同位素温差发电机，预计可持续到2030年代。

通信是一个缓慢的过程，指令需要一天才能到达，确认又需要一天，这与到达月球、火星和冥王星等较近目的地的通信时间形成鲜明对比。这篇文章强调了太空的巨大尺度，指出即使以光速飞往我们最近的恒星——比邻星，也需要四年多的时间。

除了它的距离记录之外，旅行者1号的任务还包括重要的成就，例如行星飞越和著名的“暗淡蓝点”图像，突出了我们太阳系的浩瀚和该探测器非凡的寿命。

---

## 27. “ECMAScript新闻”最后一期

**原文标题**: Last Issue of "ECMAScript News"

**原文链接**: [https://ecmascript.news/archive/es-next-news-2025-11-26.html](https://ecmascript.news/archive/es-next-news-2025-11-26.html)

ECMAScript新闻因过去两年广告商和订阅者数量下降造成的财务亏损而停止出版。该新闻通讯于2016年9月27日开始发行，共出版了368期。编辑们对忠实读者多年来的支持表示感谢。创始人之一Axel有可能在2026年以不同形式恢复该新闻通讯，届时订阅者将收到最后一封邮件通知。

---

## 28. 一种快速的64位日期算法 (通过倒数日期提高30–40%的速度)

**原文标题**: A Fast 64-Bit Date Algorithm (30–40% faster by counting dates backwards)

**原文链接**: [https://www.benjoffe.com/fast-date-64](https://www.benjoffe.com/fast-date-64)

本文介绍了一种新型、非常快速的64位日期算法，通过倒数日期的方式，比以往领先的算法快30-40%。该算法仅使用四次乘法即可完成日期转换，与早期方法使用的七次或更多次乘法相比，这是一个显著的减少。

速度提升归功于三个关键创新：从2400年的纪元开始倒算年份、使用年份模数位移技术跳过一年中的日期计算，以及利用“儒略图”加速100/400年的计算。倒数允许去除诸如“+3”之类的因闰年对齐而产生的项，这些项通常出现在正数中。

该算法在±1.89万亿年的范围内提供准确的结果，适用于完整的UNIX 64位时间。本文提供了伪代码、详细的逐行解释，并讨论了针对x64和ARM处理器的特定于平台的优化。它还深入研究了范围/准确性考虑因素和32位回退选项。提供了将该算法的速度与C++ Boost和Neri-Schneider进行比较的基准测试结果，突出了其基于减少CPU周期数的性能优势。最后，作者强调了理解基本原理对于实现显著速度提升的重要性。

---

## 29. 希捷实现单碟6.9TB存储容量

**原文标题**: Seagate achieves 6.9TB storage capacity per platter

**原文链接**: [https://www.tomshardware.com/pc-components/hdds/seagate-achieves-a-whopping-6-9tb-storage-capacity-per-platter-in-its-laboratory-55tb-to-69tb-hard-drives-now-physically-possible](https://www.tomshardware.com/pc-components/hdds/seagate-achieves-a-whopping-6-9tb-storage-capacity-per-platter-in-its-laboratory-55tb-to-69tb-hard-drives-now-physically-possible)

希捷硬盘技术获突破：单碟容量达6.9TB，或催生55TB-69TB硬盘。该技术结合了热辅助磁记录（HAMR）和Mozaic 3+以减小介质晶粒尺寸，实现更高密度的数据存储。

然而，这些高容量盘片仍在开发中，预计到2030年才能应用于商业产品。在此之前，希捷计划分别在2027年、2028年和2029年推出4TB、5TB和6TB盘片的硬盘，并预计从2031年起推出7TB-15TB的盘片，可能在2040年前问世PB级硬盘。

尽管固态硬盘（SSD）越来越受欢迎，但由于其可靠性和成本效益，硬盘仍然是长期、高容量存储的关键，尤其是在数据中心。人工智能的蓬勃发展进一步增加了对硬盘的需求，导致制造商的订单积压。目前，希捷24TB酷鱼硬盘的折扣价为239.99美元。

---

## 30. 保护公立学校学生免受校外言论监控

**原文标题**: Protect Public School Students from Surveillance of Off-Campus Speech

**原文链接**: [https://www.eff.org/deeplinks/2025/11/eff-arizona-federal-court-protect-public-school-students-surveillance-and](https://www.eff.org/deeplinks/2025/11/eff-arizona-federal-court-protect-public-school-students-surveillance-and)

本文探讨了 *Merrill v. Marana Unified School District* 案，该案中一名高中生因在家中使用学校配发的 Chromebook 电脑起草（但从未发送）的电子邮件中的一个玩笑而被停学。学校使用 Gaggle 监控软件标记了该“威胁”。EFF（电子前沿基金会）提交了法庭之友意见陈述，反对学区声称使用学校配发的设备自动等同于“在校园内”，因此受学校言论规定的约束。

EFF 强调，如此宽泛的解释侵犯了学生的《第一修正案》权利和数字隐私，导致自我审查和对自由表达的寒蝉效应。他们认为，学生需要私人的数字空间，免受持续的监控。

该简报进一步强调了潜在的不公平现象，因为与能够负担个人设备的富裕学生相比，依赖学校设备的低收入学生将面临更大的监控和更严格的言论规定。这创造了一种“付费隐私”制度。此外，简报认为，这项规定鼓励侵入性的监控行为，并忽视了与学生监控技术相关的错误和危害。EFF 敦促法院通过拒绝“学校配发的设备本质上使所有言论都‘在校园内’”的观念，来保护学生的数字自主权和言论自由。

---

## 31. Fara-7B：用于计算机的高效智能体模型

**原文标题**: Fara-7B: An efficient agentic model for computer use

**原文链接**: [https://github.com/microsoft/fara](https://github.com/microsoft/fara)

Fara-7B：微软新型高效70亿参数小型语言模型，专为计算机使用而设计。它作为一个代理，通过鼠标和键盘与计算机进行视觉交互，直接感知网页并执行多步骤任务，如搜索、填写表格和预订。这消除了对可访问性树或解析模型的需求，模仿了人类与计算机交互的方式。其紧凑的尺寸使其能够在设备上部署，从而提高延迟和隐私。

Fara-7B使用基于Magentic-One框架和Qwen2.5-VL-7B的合成数据管道进行训练。在WebVoyager、Online-M2W和DeepShop等网络代理基准测试中，它优于同类和更大的模型。

本文介绍了一个名为WebTailBench的新基准，强调以前代表性不足的真实世界网络任务。Fara-7B在WebTailBench上的购物、旅行和房地产等各种任务类别中表现出卓越的性能。

本文还详细介绍了评估基础设施，重点介绍了Playwright的使用以及用于可重复结果的结构化框架，包括处理时间敏感的任务更新和环境错误。提供了Azure Foundry托管（推荐易于使用）和使用VLLM进行自托管的说明。该版本为实验性版本，鼓励社区反馈和沙盒使用。

---

## 32. 将主要的 Zig 仓库从 GitHub 迁移到 Codeberg

**原文标题**: Migrating the main Zig repository from GitHub to Codeberg

**原文链接**: [https://ziglang.org/news/migrating-from-github-to-codeberg/](https://ziglang.org/news/migrating-from-github-to-codeberg/)

Zig项目因担忧GitHub质量下降、GitHub Actions (CI系统) 被忽视以及对AI功能的推动，已将其主仓库迁移至Codeberg，以摆脱GitHub。团队指出CI调度不可预测以及违反Zig的“无LLM/AI”政策等问题，因此决定更换Git托管服务提供商，以确保更稳定可靠的开发环境。

虽然承认GitHub Sponsors对早期筹款的重要性，但该团队认为其存在隐患，因为他们认为GitHub Sponsors 被忽视，并鼓励用户将定期捐款转至非营利组织Every.org。GitHub Sponsors的福利将被取消，并通过Every.org提供同等福利。

此次迁移包括将GitHub仓库设为只读，并将Codeberg指定为权威来源。现有的GitHub问题和pull request将保持开放且不迁移，视为“写入时复制”。Codeberg上的新问题编号将从30000开始，以避免歧义。Zig团队感谢Forgejo和Codeberg社区在迁移过程中提供的帮助。此举被视为支持非营利组织和在平台资本主义时代捍卫“公共领域”的一步。

---

## 33. 2025年更新GPG子密钥

**原文标题**: Renewing GPG Subkeys in 2025

**原文链接**: [https://entropicthoughts.com/renewing-gpg-subkeys-in-2025](https://entropicthoughts.com/renewing-gpg-subkeys-in-2025)

本文概述了2025年更新GPG签名和加密子密钥的流程，重点介绍GPG的进步如何简化了该程序。它详细描述了在包含秘密主密钥的离线计算机上执行的步骤。

该过程包括：

1.  **验证：**列出公钥和私钥以识别密钥ID。
2.  **导入：**导入秘密主密钥。
3.  **过期更新：**在GPG中使用`expire`命令更新主密钥和子密钥的过期日期。
4.  **导出子密钥：**将秘密子密钥导出到文件。
5.  **删除主密钥（可选）：**可选择从离线机器上删除秘密主密钥，并强调删除过程中会自动移除相关的子密钥。
6.  **重新导入子密钥：**将秘密子密钥重新导入到密钥环中。
7.  **验证：**通过检查秘密主密钥是否缺失以及子密钥的过期日期是否已更新来验证结果。

本文还涉及GPG密钥管理的历史复杂性，这些复杂性现已得到解决，例如处理子密钥和主密钥的单独密码。它还提到由于GDPR的担忧而减少了对密钥服务器的依赖，以及作者对其公开密钥的更新频率较低。作者建议重新导出秘密主密钥可能带来的好处，以便将之前的续订历史记录包含在密钥数据中。

---

## 34. Show HN: Era – AI 代理的开源本地沙箱

**原文标题**: Show HN: Era – Open-source local sandbox for AI agents

**原文链接**: [https://github.com/BinSquare/ERA](https://github.com/BinSquare/ERA)

Era：用于运行不受信任代码或AI生成代码的开源本地沙箱

**主要特性：**

*   **沙箱执行：** 在隔离的微虚拟机内运行代码。
*   **语言支持：** 支持 Python、JavaScript/Node/TypeScript、Go 和 Ruby。可以指定自定义镜像。
*   **快速启动：** 微虚拟机启动时间约为 200 毫秒。
*   **本地 CLI 工具：** 提供用于创建、执行、列出、停止和清理虚拟机的命令。
*   **配置：** 提供可配置的选项，如日志级别、状态目录和卷挂载。
*   **云部署：** 可以作为 Cloudflare Worker 部署，使用 Durable Objects 进行会话管理和 HTTP API。
*   **安装：** 提供通过 Homebrew 或从源代码安装。需要 `krunvm` 和 `buildah` 等依赖项。
*   **文档：** 提供关于 CLI 用法、设置、故障排除、API 部署和示例工作流的详尽文档。
*   **许可：** Apache 2.0

**核心命令：**

*   `agent vm create`：创建长时间运行的虚拟机。
*   `agent vm exec`：在虚拟机内部运行命令。
*   `agent vm temp`：在临时虚拟机中执行命令。
*   `agent vm list`：列出虚拟机。
*   `agent vm stop`：停止虚拟机。
*   `agent vm clean`：删除虚拟机。

本质上，Era 为开发者提供了一种安全有效的方式，可以在本地实验 AI 生成的代码或运行不受信任的应用程序，并可以选择使用 Cloudflare Workers 在云中部署类似的环境。

---

## 35. 如何/为何将异步任务扫进Postgres表里

**原文标题**: How/why to sweep async tasks under a Postgres table

**原文链接**: [https://taylor.town/pg-task](https://taylor.town/pg-task)

本文倡导通过将异步任务“扫入”Postgres表中进行管理，而不是依赖于像SQS、Redis或Celery这样的专用队列系统。作者认为，这种方法简化了系统架构，降低了复杂性，并利用Postgres的事务保证来确保数据一致性和可靠的任务执行。

核心思想是在处理面向用户的操作（例如，用户注册）的同一个数据库事务中，将任务插入到`task`表中。这保证了如果数据库写入成功，则任务肯定会被执行。一个后台worker持续轮询该表，在事务中处理和删除任务。如果任务失败，事务回滚，任务仍然保留在队列中以供重试。

强调的主要优势包括：

*   **数据一致性：** 通过在数据库中管理所有状态来避免两阶段提交问题。
*   **简化架构：** 减少了所涉及的系统数量，从而更易于调试和维护。
*   **自动重试：** 由于事务回滚，失败的任务会自动重试，提供内置的容错能力。
*   **TODO管理：** 未实现的任务会自动记录并重试，充当待实现/修复事项的实时列表。
*   **并行处理：** 使用`skip locked`允许多个worker并发处理任务，而无需争用。
*   **优先级队列：** 使用 `order by (case task_type ... end), random()` 对任务进行优先级排序。

作者还强调了优先考虑数据库一致性而不是立即执行的重要性，并建议避免对人工可解决的问题使用复杂的重试循环，而是将其委派给计算机。

---

## 36. Steam 代表俄罗斯政府审查 LGBTQ+ 内容

**原文标题**: Steam censors LGBTQ+ content on behalf of the Russian Government

**原文链接**: [https://www.videogamesindustrymemo.com/p/how-steam-censors-lgbtq-content-on](https://www.videogamesindustrymemo.com/p/how-steam-censors-lgbtq-content-on)

视频游戏产业备忘录（VGIM）的这篇文章报道了Steam如何据称代表俄罗斯政府审查机构 Roskomnadzor 审查电子游戏中 LGBTQ+ 内容。文章重点讲述了英国开发商 Flick Games 的经历，其卡牌游戏“Flick Solitaire”因其 LGBTQ+ 主题卡牌而被 Roskomnadzor 认定为宣扬“非传统”关系，并因此从 Steam 的俄罗斯版本中移除。

虽然 Apple 和 Google 没有遵守 Roskomnadzor 的要求，并保持该游戏在其俄罗斯的应用商店中可用，但 Steam 立即移除了该游戏，且没有给 Flick Games 上诉的机会。随后，Steam 指责 Flick Games 未遵守俄罗斯法律，这引发了人们对 Valve 的内容审核政策被专制政权利用的担忧。

Flick Games 创始人 Ian Masters 强调了 LGBTQ+ 能见度在俄罗斯等国家的重要性，并对 Steam 的决定表示失望。Out Making Games 也批评 Steam 的立场“令人深感不安”。

文章认为，Steam 允许“一切”非“钓鱼”或“非法”内容的政策加强了 Roskomnadzor 等审查机构的力量。文章最后呼吁数字内容监管机构将游戏行业置于监管之下。文章还包括关于其他行业发展的新闻简报，包括腾讯对育碧的投资以及澳大利亚对未成年人的社交媒体禁令。

---

## 37. 一位致力于拍摄每种蜂鸟的女性

**原文标题**: A woman on a mission to photograph every species of hummingbird

**原文链接**: [https://www.audubon.org/magazine/meet-woman-mission-photograph-every-species-of-hummingbird-world](https://www.audubon.org/magazine/meet-woman-mission-photograph-every-species-of-hummingbird-world)

这与其说是一篇文章，不如说是一个宣传片段。它突出了一个致力于拍摄所有蜂鸟物种的人，并以此为跳板，倡导气候行动。核心信息是呼吁采取行动，敦促读者与奥杜邦协会签署承诺书，向民选官员施压，以解决气候变化问题。其潜在假设是，像蜂鸟这样生物的美丽和脆弱性，为环境保护和气候解决方案提供了一个令人信服的理由。

---

## 38. C100开发者终端

**原文标题**: C100 Developer Terminal

**原文链接**: [https://caligra.com/](https://caligra.com/)

Caligra公司出品的C100开发者终端，专为注重精准和专注的技术环境设计。Caligra优先考虑开发者和技术专业人员的需求，旨在创造一个免受干扰的环境，从而促进深度工作并最大限度地提高生产力。C100的核心理念是优先考虑用户的工作流程，并确保他们能够高效地完成任务。这是一款专门为满足用户需求而打造的计算机，使他们能够专注于工作并取得最佳成果。 简而言之，Caligra致力于构建赋能开发者和技术专业人员在其各自领域中脱颖而出的工具，其核心原则是让技术为人服务，而不是让人为技术服务。

---

## 39. 你能把牛带到牛津吗？

**原文标题**: Can you take an ox to Oxford?

**原文链接**: [https://alexwlchan.net/2025/ox-in-oxford/](https://alexwlchan.net/2025/ox-in-oxford/)

本文幽默地探讨了牛津的拥堵费是否适用于牛拉车。起因是一条推特质疑牛拉车辆因零排放是否应该收费，作者深入研究了构成拥堵费的法律定义。

调查的重点是牛津郡议会的“收费令”和相关的英国法律，特别是《2001年道路使用者收费和工作场所停车税（机动车辆类别）（英格兰）条例》。关键问题是牛拉车是否属于“机动车辆”的定义，《1988年道路交通法》将其定义为“机械推进的车辆”。

作者认为，由于牛并非法律意义上的“机械推进”，因此牛拉车不应被视为机动车辆，因此不受拥堵费的约束。文章进一步指出，拥堵费很可能通过车牌识别来执行，而牛拉车没有车牌，进一步巩固了其豁免权。

文章还提到了法规中的一些怪异之处，指出像Reliant Robins和Peel P50s这样的车辆，虽然从技术上讲可以根据其分类获得豁免，但由于有车牌，很可能会被收费。

总之，作者断言，你确实可以赶着牛车去牛津，而不会产生拥堵费。文章最后反思了公开立法的价值，使公民能够研究和理解法律，即使是对于荒谬的场景。

---

## 40. 巴基斯坦称明年部分枢纽屋顶太阳能发电量将超过电网需求

**原文标题**: Pakistan says rooftop solar output to exceed grid demand in some hubs next year

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/pakistan-says-rooftop-solar-output-exceed-grid-demand-some-hubs-next-year-2025-11-22/](https://www.reuters.com/sustainability/boards-policy-regulation/pakistan-says-rooftop-solar-output-exceed-grid-demand-some-hubs-next-year-2025-11-22/)

巴基斯坦政府预计，到明年（2025年），屋顶太阳能发电量将在某些城市中心超过电网的电力需求。这一预测基于消费者为降低能源成本和摆脱对国家电网的依赖（后者经常面临停电和高关税等问题）而迅速采用屋顶太阳能系统。

太阳能日益普及，这得益于允许消费者将多余电力出售回电网的具有吸引力的净计量政策，但也给巴基斯坦的配电公司带来了潜在挑战。这些公司依赖电网电力销售收入，如果由于屋顶太阳能普及而导致需求大幅下降，可能会面临财务压力。

政府承认需要适应这种不断变化的能源格局，并正在探索确保配电公司财务可行性的同时，继续鼓励可再生能源发展的战略。这些战略可能包括修订关税结构或为配电公司开发新的商业模式。预计屋顶太阳能发电的盈余反映了巴基斯坦为实现能源结构多样化和减少对进口化石燃料的依赖所做的更广泛努力。

---

## 41. 欧盟迫使苹果采用新的Wi-Fi标准，现在安卓可以支持AirDrop。

**原文标题**: The EU made Apple adopt new Wi-Fi standards, and now Android can support AirDrop

**原文链接**: [https://arstechnica.com/gadgets/2025/11/the-eu-made-apple-adopt-new-wi-fi-standards-and-now-android-can-support-airdrop/](https://arstechnica.com/gadgets/2025/11/the-eu-made-apple-adopt-new-wi-fi-standards-and-now-android-can-support-airdrop/)

本文探讨了Android的“邻近分享”功能如何更新以支持Apple的AirDrop，从而通过点对点Wi-Fi连接实现Android和Apple设备之间的直接文件共享。最初，此功能仅在Pixel 10系列上可用，谷歌计划未来将支持扩展到更多Android设备。该更新需要AirDrop设置为“所有人，10分钟”模式，并利用Wi-Fi感知（Wi-Fi Aware），这是谷歌自Android 8.0以来一直支持的标准。

文章认为，这种互操作性主要归功于欧盟的《数字市场法案》（DMA），该法案要求苹果公司采用像Wi-Fi感知这样的可互操作的无线标准，而不是其专有的Apple无线直连（AWDL）。这使得像谷歌这样的其他公司能够使其文件共享功能与AirDrop兼容。

虽然谷歌在其公告中没有明确提及DMA，但文章暗示这很可能是这一变化背后的关键驱动因素。iOS 26和iPadOS 26（iPhone 12及更高版本，以及最近的iPad支持）中采用Wi-Fi感知是“邻近分享”与AirDrop配合使用的必要条件。macOS不太可能得到支持。作者推测，尽管谷歌偶尔会利用DMA，但由于担心该法律的潜在影响，它可能不愿赞扬DMA。

---

## 42. 语言模型辅助编码中的本质与偶然

**原文标题**: Essence and accident in language model-assisted coding

**原文链接**: [https://www.sicpers.info/2025/11/essence-and-accident-in-language-model-assisted-coding/](https://www.sicpers.info/2025/11/essence-and-accident-in-language-model-assisted-coding/)

格雷厄姆的文章《语言模型辅助编码中的本质与偶然》探讨了基于语言模型的编码工具如何解决软件开发中的复杂性，并参考了弗雷德·布鲁克斯 1986 年的论文《没有银弹》。布鲁克斯区分了本质复杂性（问题固有的）和偶然复杂性（由所选解决方案引入的）。

文章认为，编码助手通过像程序员一样生成代码，并不能从根本上减少偶然复杂性。一种愤世嫉俗的观点认为，它们甚至可能通过增加提示工程来增加偶然复杂性。真正减少偶然复杂性只有在工具直接从提示生成可执行文件，完全绕过源代码，或者语言模型完全取代编程时才会发生。

关于本质复杂性，作者认为，除非问题本身涉及语言模型，否则语言模型与大多数问题的固有复杂性无关。然而，这些工具擅长通过迭代代码生成和测试来揭示误解和错误假设，从而快速暴露本质复杂性。这种加速的反馈循环能够更快地理解真实需求，甚至优于需求规范或原型设计等传统方法。

格雷厄姆总结说，虽然这些工具可能不是银弹，但它们显着加速了发现本质复杂性和完善需求的迭代过程，与布鲁克斯关于通过更高级别语言实现自动编程的预测相符。

---

## 43. 酒店重新安装浴室门

**原文标题**: Bring bathroom doors back to hotels

**原文链接**: [https://bringbackdoors.com/](https://bringbackdoors.com/)

本文概述了酒店为节省成本和追求美观而拆除浴室门，由此引发的日益增长的不满。作者对此趋势感到厌倦，认为这牺牲了客人的隐私和尊严。

为了解决这个问题，作者创建了一个网站，专门用于识别有浴室门和没有浴室门的酒店。他们联系了数百家酒店，询问其浴室门是否完全关闭以及是否由玻璃制成。确认门可以关闭且材料非玻璃的酒店将被列在该网站上，按价格范围和城市分类，以帮助旅客找到可以保证浴室隐私的酒店。

该网站还包含一项功能，允许用户查看某酒店是否已被报告缺少浴室门。此外，作者鼓励旅客通过电子邮件 (bringbackdoors@gmail.com) 或 Instagram 私信提交“无门”酒店的报告，包括酒店名称和照片。这些提交的内容将被公开分享，以“点名羞辱”违规酒店，旨在迫使他们优先考虑客人隐私并重新安装浴室门。作者强调，这是一个出于保护未来旅客尊严的愿望而驱动的热情项目。

---

## 44. 使用 Neo4j 和 LlamaIndex 实现漂移搜索

**原文标题**: Implementing Drift Search with Neo4j and LlamaIndex

**原文链接**: [https://neo4j.com/blog/developer/drift-search-with-neo4j-and-llamaindex/](https://neo4j.com/blog/developer/drift-search-with-neo4j-and-llamaindex/)

本文深入探讨了使用Neo4j和LlamaIndex实现的基于灵活遍历的动态推理和推断（DRIFT）搜索技术，该技术结合了GraphRAG系统中全局搜索和局部搜索的各个方面。 DRIFT首先利用向量搜索获取社区信息，为查询建立一个广泛的起点，并将其细化为详细的后续问题。 这使得系统能够动态遍历知识图谱，在计算效率和全面的答案质量之间取得平衡。

该实现使用LlamaIndex工作流程来协调DRIFT搜索过程。 首先，假设文档嵌入（HyDE）生成基于示例社区报告的假设答案，以改善查询表示。 接下来，社区搜索使用向量相似性来识别最相关的社区报告，从而提供广泛的上下文。 系统分析这些结果以生成初始的中间答案以及一组用于更深入调查的后续查询。 这些后续查询在本地搜索阶段并行执行，从而检索有针对性的信息。 最后，答案生成步骤综合所有中间答案，将广泛的社区层面见解与详细的本地发现相结合，以产生全面的响应。 本文使用《爱丽丝梦游仙境》作为示例数据集，并重用了先前开发的Microsoft GraphRAG索引实现，该实现已适配到LlamaIndex工作流程中以用于数据摄取。 DRIFT搜索的代码可在GitHub上找到。

---

## 45. Optery (YC W22) 招聘首席信息安全官、发布经理、技术主管（Node）、全栈工程师

**原文标题**: Optery (YC W22) Hiring CISO, Release Manager, Tech Lead (Node), Full Stack Eng

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22 公司) 正在招聘多个技术职位：首席信息安全官 (CISO)、发布经理、技术负责人（Node）和全栈工程师。

Optery 招聘页面可能需要 Cookie 才能完整显示。如果页面显示空白，建议用户通过屏幕左下角的 Cookie 横幅接受“个性化 Cookie”。

---

## 46. 技术性通货紧缩

**原文标题**: Technical Deflation

**原文链接**: [https://benanderson.work/blog/technical-deflation/](https://benanderson.work/blog/technical-deflation/)

本杰明·安德森的文章《技术性通货紧缩》探讨了这样一个观点：人工智能的进步使得软件开发越来越容易和便宜，从而在科技行业造成通货紧缩效应。他认为，初创公司可能会推迟产品开发，因为他们预期人工智能模型和开发工具会进一步改进。

安德森详细阐述了人工智能的进步，例如改进的LLM，如何简化了开发过程，使得初创公司能够以更少的资源快速构建功能性应用程序。这使得新来者可以通过快速开发过去需要数年才能完成的功能，与老牌公司竞争。

他以开发桌面应用程序为例来说明这一点，并表示未来人工智能进步的潜力使得推迟开发具有诱惑力。他进一步认为，作为市场的后来者可能是有利的，因为公司可以避免早期采用者的错误，并利用更先进的人工智能工具。

虽然安德森承认先发制人的传统重要性，但他认为当前的技术环境有利于后来者。最后，他思考了初创公司在这种环境下的最佳策略，并认为专注于分销、客户理解或像自定制软件这样的创新方法可能是在这个技术越来越容易获得的世界中取得成功的关键。核心思想是，如果构建变得容易，那么护城河必须在其他地方。

---

## 47. 独立游戏开发者有了新的销售策略：标榜“无AI”。

**原文标题**: Indie game developers have a new sales pitch: being 'AI free'

**原文链接**: [https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders](https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders)

独立游戏开发者越来越多地使用“无AI”营销来区分他们的游戏，这受到伦理考量以及突出游戏背后人类努力的愿望的推动。这一趋势的出现，源于Nexon的Junghun Lee等游戏公司CEO声称AI在游戏开发中无处不在，而独立开发者强烈否认这一说法。

此运动的一个关键要素是由Polygon Treehouse创建的免费“无生成AI”标志，向消费者表明该游戏完全由人类制作。Unbeatable背后的工作室D-Cell Games也采取了坚定的反AI立场，强调人类创作中固有的个人风格和不完美。

这些开发者认为，尽管AI有可能加快开发速度，但它会削弱定义独立游戏的创造性问题解决能力和独特的审美选择。他们相信，约束会激发创造力，避免使用AI符合他们的价值观，并能引起欣赏手工制作体验的玩家的共鸣。

虽然承认采用AI的压力越来越大，但这些独立开发者决心保持其艺术完整性，并继续以“人类方式”制作游戏，认为这样更充实和真实。他们已经从社区收到了关于其反AI立场的积极回应，表明人们对不使用AI辅助制作的游戏存在需求。

---

## 48. TPU vs. GPU：以及为何谷歌有望赢得AI长期竞赛

**原文标题**: TPUs vs. GPUs and why Google is positioned to win AI race in the long term

**原文链接**: [https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference](https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference)

本文深入探讨谷歌的张量处理器 (TPU)，将其与 GPU 进行比较，并论证了谷歌为何有能力赢得长期的 AI 竞赛。文章首先回顾了 TPU 的历史，解释了 TPU 的创建是为了满足谷歌对 AI 推理中大规模矩阵乘法进行高效处理的需求，特别是为了避免因语音搜索而导致数据中心容量翻倍。

TPU 和 GPU 的核心区别在于它们的架构：GPU 是针对图形优化的通用并行处理器，而 TPU 是特定领域的，使用 systolic 阵列。这种阵列减少了内存访问瓶颈，从而提高了每焦耳的运算次数。最新的 TPU 设计，如 Ironwood (v7)，增强了包括 SparseCore、增加的 HBM 容量/带宽和改进的芯片间互连等功能。

虽然性能数据有限，但对采访和行业洞察的分析表明，与 GPU 相比，TPU 在特定 AI 任务上提供了更好的成本效益和每瓦性能。专家们提到效率提升、降低的 AI 搜索成本以及动态模型的潜在速度优势。一个关键优势在于谷歌针对 TPU 优化的软件生态系统。

文章强调了 TPU 更广泛采用的主要障碍：英伟达 CUDA 生态系统的统治地位，该生态系统被广泛教授和支持。该行业也偏向于 PyTorch。此外，大多数公司都是多云的事实意味着，英伟达可以在所有三个超大规模云提供商（AWS、Azure、GCP）上访问，因此具有显著优势。然而，对 AI 推理的日益关注（CUDA 在此方面不太重要）为 TPU 的扩展提供了机会。最后，TPU 的快速世代改进，可能超过英伟达的进步速度，巩固了谷歌的竞争优势。

---

## 49. Collabora Online桌面版发布，采用LibreOffice改进的用户界面

**原文标题**: Collabora Online Desktop Released with Improved UI from LibreOffice

**原文链接**: [https://www.collaboraonline.com/blog/collabora-online-now-available-on-desktop/](https://www.collaboraonline.com/blog/collabora-online-now-available-on-desktop/)

Collabora Online桌面版发布，UI升级源自LibreOffice，详见全文。

---

## 50. 显示 HN: KiDoom – 在 PCB 走线上运行 DOOM

**原文标题**: Show HN: KiDoom – Running DOOM on PCB Traces

**原文链接**: [https://www.mikeayles.com/#kidoom](https://www.mikeayles.com/#kidoom)

这个“Show HN”帖子介绍了KiDoom，一个令人印象深刻的项目，它实现了在PCB走线上运行经典游戏DOOM的壮举。这意味着DOOM不是在传统的处理器或微控制器上运行，而是直接利用印刷电路板的导电通路来执行游戏逻辑。

该片段还突出了作者的一些相关专业经验，很可能是项目创建者本人的。其中提到开发了3个ECU（发动机控制单元），拥有超过10年的行业经验，并且累计行驶超过2850万英里。这表明创建者具有汽车电子和嵌入式系统的背景。

名为“精选项目”和“私人工具”的部分暗示 KiDoom 只是更大项目组合的一部分，并且创建者在其工作中使用了定制工具，这进一步增加了可信度并展示了专业知识。

本质上，这篇文章是对一个新颖且具有技术挑战性的项目 (KiDoom) 的简短公告，展示了 PCB 设计和嵌入式系统工程方面的卓越能力。它与相关领域的重要专业经验指标一起呈现，暗示了创建者的专业知识以及突破可能性的热情。

---

## 51. 小罗伯特·肯尼迪的新任疾控中心副主任更青睐“自然免疫”而非疫苗

**原文标题**: RFK Jr.'s new CDC deputy director prefers "natural immunity" over vaccines

**原文链接**: [https://arstechnica.com/health/2025/11/rfk-jr-s-new-cdc-deputy-director-prefers-natural-immunity-over-vaccines/](https://arstechnica.com/health/2025/11/rfk-jr-s-new-cdc-deputy-director-prefers-natural-immunity-over-vaccines/)

在卫生部长小罗伯特·F·肯尼迪领导下，疾控中心任命拉尔夫·亚伯拉罕为首席副主任。由于亚伯拉罕曾持有反疫苗观点并推销未经证实的 COVID-19 疗法，他的任命引起了担忧。

作为路易斯安那州卫生局长，亚伯拉罕延迟通知居民关于百日咳爆发的消息，并停止大规模疫苗接种活动，表达了对“自然免疫”优于疫苗的偏好。他还为 COVID-19 开出了羟氯喹和伊维菌素，尽管这些药物无效。2021 年，他是路易斯安那州伊维菌素处方量最高的医生之一。此外，他还有大量开具阿片类药物处方的历史。

亚伯拉罕的观点与肯尼迪的反疫苗立场、阴谋论以及对未经证实疗法的支持相一致。肯尼迪最近指示疾控中心在其网站上错误地将疫苗与自闭症联系起来。这项任命被视为根据肯尼迪的观点重塑疾控中心的一步。

---

## 52. Bonsai_term: Jane Street 构建动态终端应用程序的库

**原文标题**: Bonsai_term: A library for building dynamic terminal apps by Jane Street

**原文链接**: [https://github.com/janestreet/bonsai_term](https://github.com/janestreet/bonsai_term)

Bonsai_term 是 Jane Street 的一个 OCaml 库，用于构建终端用户界面 (TUI)，其编程模型与他们的 bonsai_web 库相仿。它分布在四个存储库中：`bonsai_term` (核心库)、`bonsai_term_examples`、`bonsai_term_components` 和 `bonsai_term_test`。

要开始使用，用户需要安装 opam (OCaml 的包管理器) 和 OxCaml。安装完成后，`opam install bonsai_term` 将安装该库及其依赖项。

文档建议浏览 `src/bonsai_term.mli` 文件和 `bonsai_term_examples` 存储库，以了解如何使用该库。虽然 `bonsai_web` 文档是一个有用的资源，但用户应重点关注 “effect”、“state-fulness” 和 “incrementality” 方面，因为 “vdom” 部分是特定于 Web 的。

文档还提供了 OCaml 学习资源的链接，包括 Learn OCaml 文档、CS 3110 课程和 Real World OCaml。已按照初始安装说明操作的用户可以跳过这些资源中的“安装”部分。文章还提到了示例演示，其源代码位于 examples 仓库中。

---

## 53. C64地穴.BAS

**原文标题**: C64 Burrow.BAS

**原文链接**: [https://basic-code.bearblog.dev/c64-burrow/](https://basic-code.bearblog.dev/c64-burrow/)

本文讨论了一个简短的Commodore 64 BASIC程序，名为“Burrow.BAS”，它被设计为一个视觉演示，而非游戏。作者解释了如何将C64 BASIC代码嵌入到博客文章中，并揭示该程序基于1985年Run杂志中的两个单行程序。

该程序由两行代码组成。第1行将边框和背景颜色设置为黄色。第2行使用光标移动字符和反显文本来创建一个动画，其中星号似乎以随机方向在屏幕上“挖洞”。作者解释了使用的特殊字符，例如“{yellow}”、“{up}”、“{down}”、“{left}”、“{right}”和“{reverse on}”，以及如何使用Commodore 64键盘和控制键输入它们。

文章还简要介绍了8位BASIC中的`PEEK`和`POKE`命令，解释说它们允许直接访问内存地址。在本例中，`POKE 53280`和`POKE 53281`分别用于更改边框和背景颜色。随机挖洞效果是通过随机选择光标方向代码来实现的。作者改编了另一行代码中的第1行，以增强颜色效果。

---

## 54. Ruby 从一开始就已准备就绪

**原文标题**: Ruby Was Ready from the Start

**原文链接**: [https://obie.medium.com/ruby-was-ready-from-the-start-4b089b17babb](https://obie.medium.com/ruby-was-ready-from-the-start-4b089b17babb)

无法访问文章链接。

---

## 55. 我曾相识却不爱的尼古丁类似物：6-甲基尼古丁

**原文标题**: A Nicotine Analogue I Had Known and Didn't Love: 6-Methylnicotine

**原文链接**: [https://psychotechnology.substack.com/p/a-nicotine-analogue-i-had-known-and](https://psychotechnology.substack.com/p/a-nicotine-analogue-i-had-known-and)

无法访问文章链接。

---

## 56. 评估AMD Turin上的统一内存访问模式

**原文标题**: Evaluating Uniform Memory Access Mode on AMD's Turin

**原文链接**: [https://chipsandcheese.com/p/evaluating-uniform-memory-access](https://chipsandcheese.com/p/evaluating-uniform-memory-access)

本文评估了AMD Turin (Zen 5) 架构上采用的统一内存访问 (UMA) 模式，特别是NPS0模式，使用的系统是由Verda (原DataCrunch.io) 提供的EPYC 9575F双路服务器。 NPS0模式将双路系统呈现为一个单一的整体，均匀分配内存访问，并通过避免NUMA (非统一内存访问) 的复杂性来简化编程。

主要发现是，虽然NPS0简化了内存访问，但会带来显著的DRAM延迟惩罚（超过220ns，比NPS1增加了90ns）。 尽管NPS0提供了更高的内存带宽，但只有在带宽需求极高时才能实现这一优势。

尽管延迟较高，但由于更高的5 GHz时钟速度和有效的缓存，EPYC 9575F在SPEC CPU2017基准测试中表现出人意料的良好性能。 具有高缓存命中率的工作负载受益于更高的时钟速度，而内存密集型工作负载则受到更高延迟的影响。

文章总结认为，由于NUMA-感知不足的代码存在巨大的延迟惩罚和最小的带宽增益，因此在现代系统中采用NPS0模式可能并不值得。 随着服务器核心和内存控制器数量的增加，针对需要在多个插槽上扩展的工作负载，优化NUMA变得越来越重要。 本文强调了时钟速度和有效缓存对于弥补现代CPU内存延迟的重要性。

---

## 57. 使用 MISP 和 Technitium DNS 服务器的 DNS 防火墙

**原文标题**: DNS Firewalling with MISP and Technitium DNS Server

**原文链接**: [https://zaferbalkan.com/technitium-misp/](https://zaferbalkan.com/technitium-misp/)

无法访问文章链接。

---

## 58. Alan.app – 为 macOS 活跃窗口添加边框

**原文标题**: Alan.app – Add a Border to macOS Active Window

**原文链接**: [https://tyler.io/2025/11/alan/](https://tyler.io/2025/11/alan/)

本文介绍了“Alan.app”，一个小型 macOS 应用程序，旨在通过为活动窗口添加可自定义的边框来提高窗口可见性。作者创建 Alan 是为了解决 macOS 上窗口对比度的问题，这可能是由于视力老化或设计选择造成的。

Alan 的偏好设置允许用户选择所需的边框宽度和颜色，并为浅色和深色模式提供单独的设置。该应用程序简单易用，专注于提供这一单一、专注的功能。

用户可以从提供的链接下载经过公证的 Alan 副本。本文还包含一个简短的演示视频，展示了该应用程序的实际效果。

最后，作者提供了关于如何通过 Terminal 命令从 Dock 中隐藏 Alan 图标的说明，从而实现更简洁的用户界面。

---

## 59. 压缩文件系统：类语言模型

**原文标题**: Compressed filesystems à la language models

**原文链接**: [https://grohan.co/2025/11/25/llmfuse/](https://grohan.co/2025/11/25/llmfuse/)

本文详细介绍了一项实验，该实验探索了语言模型（LLM）作为压缩文件系统后端的潜力。作者通过在 FUSE 操作和相应的文件系统树 XML 表示的数据集上微调 LLM (Qwen3-4b)，来建模文件系统操作和状态。

作者随后创建了一个 FUSE 文件系统 LLMFuse，其中每个操作都传递给 LLM 进行“执行”。 关键创新在于利用算术编码，这是一种可逆压缩算法，它利用 LLM 的概率预测来压缩 XML 文件系统表示。 因为 LLM 是在这个特定的 XML 格式上训练的，所以它可以比 gzip 等传统方法更有效地“自压缩”数据。

结果表明，使用算术编码和微调后的 LLM 可以显著提高压缩性能，明显优于 gzip 甚至专用压缩文件系统工具 squashfs。 对于一个简单的文件系统树，作者实现了比 squashfs 大约 8 倍的压缩率提升。

虽然承认存在局限性（高计算成本、对上下文窗口大小的依赖以及对主要文本数据的适用性），但作者认为，该实验暗示了 LLM 在未来可能用于数据压缩，尤其是在专门工作流程中的文本密集型数据，或者当在边缘运行 LLM 变得可行时。 该项目的源代码 llmfuse 和 llmencode 已开源。

---

## 60. 暂时的胜利——但我们仍需阻止聊天监控

**原文标题**: A temporary victory – but we still need to stop Chat Control

**原文链接**: [https://mullvad.net/en/blog/an-important-victory-but-we-still-need-to-stop-chat-control](https://mullvad.net/en/blog/an-important-victory-but-we-still-need-to-stop-chat-control)

本文探讨了欧盟拟议的“聊天控制”立法现状。尽管部长理事会已取消了对端到端加密消息服务进行强制扫描的要求，这是一个重大胜利，但本文认为这场斗争远未结束。

理事会的提案仍然为未来的大规模监控奠定了基础。它包括自愿扫描的规定，措辞含糊的年龄验证要求（可能需要身份验证），以及一个三年审查流程，届时将重新考虑强制扫描。此外，该提案引入了一种新的基础设施，用于阻止个别成员国认为非法的的内容。

核心问题在于引入人工智能驱动的“新材料”和“诱导”扫描，本文声称这将导致大量误报，并对私人通信进行不必要的审查。收集到的数据将由一个新的欧盟中心分析，有效地创建一个无需怀疑或法院命令即可运行的大规模监控系统。人们对与美国公司的合作以及基于欧洲刑警组织等机构的要求扩大扫描的可能性表示担忧。

本文强调了强制身份验证的潜在可能性，这将危及告密者、记者消息来源以及批评专制政权的个人的匿名性。建立封锁基础设施也引发了审查担忧，即在一个国家合法的內容可能会因另一个国家的法律而被封锁。本文最后断言，大规模监控的目标仍然是欧盟委员会和许多理事会成员国的主要野心，并呼吁继续抵制“聊天控制”以及其他类似的旨在破坏加密的倡议，如 ProtectEU。

---

## 61. Show HN: Safe-NPM – 只安装90天以上的软件包

**原文标题**: Show HN: Safe-NPM – only install packages that are +90 days old

**原文链接**: [https://github.com/kevinslin/safe-npm](https://github.com/kevinslin/safe-npm)

Safe-NPM：一款安全至上的npm安装器，默认只安装至少90天前的软件包版本，以保护项目免受供应链攻击。这种延迟使安全社区有时间在恶意版本影响您的项目之前识别并报告它们。

该工具通过查询npm注册表，根据发布时间和语义版本要求过滤可用版本，然后使用npm安装最旧的安全版本。Safe-NPM提供多种配置选项，包括：

*   `--min-age-days`：调整最短发布时间要求。
*   `--ignore`：从时间限制中排除特定的受信任软件包。
*   `--strict`：强制执行时间要求，如果无法解析依赖项则失败。
*   `--dev/--prod-only`：指定目标依赖项类型。

常见的用例包括保护新项目、审计现有项目以及CI/CD集成。

Safe-NPM通过延迟更新来降低与受损软件包相关的风险，从而为发现恶意代码争取时间。但是，它不能防止从一开始就具有恶意的软件包，并且会延迟对新功能的访问。它是一种防御层，应与其他安全实践（如定期安全审计和依赖项审查）结合使用。

---

## 62. 微波葡萄如何产生等离子体羽流？

**原文标题**: How Does Microwaving Grapes Create Plumes of Plasma?

**原文链接**: [https://www.pbs.org/wgbh/nova/article/how-does-microwaving-grapes-create-plumes-plasma/](https://www.pbs.org/wgbh/nova/article/how-does-microwaving-grapes-create-plumes-plasma/)

微波炉葡萄产生等离子体的科学原理

本文探讨了微波炉加热葡萄产生等离子体这一爆红现象背后的科学原理。多年来，这一现象的物理机制一直未被充分理解，但最近的研究终于对其原理做出了解释。

关键在于微波能量的集中。当两个葡萄（或类似的圆形、含水物体，如蓝莓）彼此接触地放置在微波炉中时，能量会集中在它们之间的接触点上。波长为12.5厘米的微波被导入到葡萄之间微小的空间（几毫米宽）中。这会产生一个强大的电场，足以从原子中剥离电子，从而电离气体并产生等离子体。单个葡萄不起作用，因为能量集中在其中心，强度不足以实现电离。

研究人员驳斥了葡萄需要对半切开的神话。水果的大小也很重要：葡萄的大小非常适合典型的微波波长，而像西红柿这样较大的水果则无法充分集中能量。

除了是一种消遣把戏外，这种现象还提供了一种利用现成设备研究纳米光子学（纳米尺度上的光）的方法。虽然用可见光复制该效果需要调整，但葡萄微波实验可以更大规模地可视化小空间中的光集中。

尽管有科学发现，研究人员强烈建议不要在家中尝试此实验，因为存在损坏微波炉的风险以及与等离子体相关的潜在安全隐患。他们的研究本身就导致了大量水果甚至几台微波炉的损坏。

---

## 63. 将我的 70 年代风格渲染器多线程化

**原文标题**: Making my 1970's-style renderer multi-threaded

**原文链接**: [https://filiph.net/text/making-my-1970s-renderer-multi-threaded.html](https://filiph.net/text/making-my-1970s-renderer-multi-threaded.html)

Filip Hráček详述了他如何在Flutter游戏中使用多线程来制作复古3D渲染器的过程。最初，尽管渲染器是基于软件的，但由于优化使用了`Canvas.drawVertices`和`TypedData`（特别是`Float32List`）来最小化内存分配，因此在主线程上运行速度尚可。

然而，随着游戏复杂性的增加以及他希望与性能较低的机器兼容，渲染器的CPU使用率（在Windows上为20-30%）成为一个问题。他试图将渲染移动到单独的线程。

Dart基于isolate的并发机制避免了共享可变内存，这构成了一个挑战，因为每帧在isolate之间复制或传输类型化数据缓冲区是不可取的。他利用Dart的外部函数接口（FFI）在原生堆上分配内存来绕过这个问题，从而允许isolate之间共享可变数组。

该过程涉及主isolate和worker isolate通过消息进行通信，使用`malloc.allocate`分配共享缓冲区，并使用双缓冲策略来防止并发修改。worker isolate渲染到一个缓冲区，而主isolate使用另一个缓冲区进行绘制。主线程创建RenderResults并使用数据来重绘CustomPainter。

结果是性能得到了提升，在他的M4 MacBook Pro上，主线程用于3D渲染的CPU时间减少了20%，显著释放了资源。

他还提到了Dart团队未来可能对共享可变内存的支持，以及他尝试使用AI来辅助完成任务的经验（大部分是负面的）。他认为AI适用于生成简单的函数或测试，而不是复杂的架构任务。

---

## 64. DSP 101 第一部分：DSP系统设计入门课程

**原文标题**: DSP 101 Part 1: An Introductory Course in DSP System Design

**原文链接**: [https://www.analog.com/en/resources/analog-dialogue/articles/dsp-101-part-1.html](https://www.analog.com/en/resources/analog-dialogue/articles/dsp-101-part-1.html)

无法访问文章链接。

---

## 65. 展示HN：我把藻类变成生物高度计，然后把它放在气象气球上

**原文标题**: Show HN: I turned algae into a bio-altimeter and put it on a weather balloon

**原文链接**: [https://radi8.dev/blog/stratospore/](https://radi8.dev/blog/stratospore/)

基于标题和可能内容的文章摘要：

这篇“Show HN”帖子详细介绍了一个项目，作者将藻类转化为生物高度计，并将其搭载在气象气球上发射升空。核心概念是利用藻类对大气条件变化（可能是不同高度的紫外线辐射水平或温度变化）的自然反应，作为测量和记录气球飞行期间高度的方法。

作者可能对藻类进行了改造，可能是基因改造，以产生可测量的信号（例如，荧光、颜色变化或特定分子的产生），从而响应在不同高度遇到的特定环境条件。然后，该信号将与气象气球达到的高度相关联。这篇博客文章可能描述了准备藻类的过程，设计一个合适的容器来容纳藻类在飞行期间，并将该容器与气象气球的有效载荷集成。

文章可能还概述了数据收集方法。这可能涉及在飞行期间捕获藻类的图像（如果信号可见），或收集样本以供后续分析，以确定由平流层条件引起的改变。对收集的藻类样本的分析将用于推断飞行的海拔剖面。

最后，该帖子可能讨论了项目期间面临的挑战、获得的结果（无论是否成功地准确测量了高度），以及未来在气候研究或公民科学项目中类似生物传感应用的潜在方向。作者可能会展示一些来自飞行的图像和数据可视化。

---

## 66. 我们都是马赛克：单个人体内细胞间的基因多样性

**原文标题**: We are all mosaics: genetic diversity found between cells in a single person

**原文链接**: [https://www.nature.com/articles/d41586-025-03768-0](https://www.nature.com/articles/d41586-025-03768-0)

研究人员对一位74岁男性100多个单个细胞进行了详细的基因分析，揭示了单个个体内部存在显著的基因变异，即嵌合现象。该研究发现了一些细胞中存在染色体片段缺失或增加、DNA片段改变，甚至Y染色体完全丢失的情况。

这项研究目前以预印本形式发表在bioRxiv上，是更大规模联盟的一个试点项目，该联盟旨在使用150名捐赠者的样本，编录19个身体部位的细胞突变。由此产生的数据将为理解嵌合现象对人类健康和疾病（尤其是癌症）的影响提供关键资源。

由于复制错误、环境因素或其他原因，DNA变化在生命过程中积累是一种已知现象。然而，由于批量DNA测序的局限性（难以检测仅存在于少数细胞中的罕见变异），分析嵌合现象一直具有挑战性。单细胞RNA测序更为常见，但尽管单细胞DNA测序非常重要，难度却更大。

这项新的综合基因图谱突显了嵌合现象的广泛性及其对各种疾病的潜在影响，从而强调了在该领域进行进一步研究的必要性。这项研究可以加速该领域的研究，尤其是在癌症等领域，因为细胞DNA突变可能起致病作用。

---

## 67. 苹果电脑的维修大师、Tekserve联合创始人 David Lerner 安息

**原文标题**: RIP David Lerner, a Mr. Fix-It of Apple Computers, Co-Founder of Tekserve

**原文链接**: [https://www.nytimes.com/2025/11/26/technology/personaltech/david-lerner-dead.html](https://www.nytimes.com/2025/11/26/technology/personaltech/david-lerner-dead.html)

无法访问文章链接。

---

## 68. Solving the Partridge square packing problem using MiniZinc

**原文标题**: Solving the Partridge square packing problem using MiniZinc

**原文链接**: [https://zayenz.se/blog/post/partridge-packing/](https://zayenz.se/blog/post/partridge-packing/)

生成摘要时出错

---

## 69. A cell so minimal that it challenges definitions of life

**原文标题**: A cell so minimal that it challenges definitions of life

**原文链接**: [https://www.quantamagazine.org/a-cell-so-minimal-that-it-challenges-definitions-of-life-20251124/](https://www.quantamagazine.org/a-cell-so-minimal-that-it-challenges-definitions-of-life-20251124/)

生成摘要时出错

---

## 70. DRAM prices are spiking, but I don't trust the industry's why

**原文标题**: DRAM prices are spiking, but I don't trust the industry's why

**原文链接**: [https://www.xda-developers.com/dram-prices-spiking-dont-trust-industry-reasons/](https://www.xda-developers.com/dram-prices-spiking-dont-trust-industry-reasons/)

生成摘要时出错

---

## 71. Tiny tweak for Pi OS, big makeover for the Imager

**原文标题**: Tiny tweak for Pi OS, big makeover for the Imager

**原文链接**: [https://www.theregister.com/2025/11/27/new_raspberry_pi_imager/](https://www.theregister.com/2025/11/27/new_raspberry_pi_imager/)

生成摘要时出错

---

## 72. Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

**原文标题**: Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

**原文链接**: [https://arxiv.org/abs/2511.19936](https://arxiv.org/abs/2511.19936)

生成摘要时出错

---

## 73. PRC elites voice AI-skepticism

**原文标题**: PRC elites voice AI-skepticism

**原文链接**: [https://jamestown.org/prc-elites-voice-ai-skepticism/](https://jamestown.org/prc-elites-voice-ai-skepticism/)

生成摘要时出错

---

## 74. JOPA: Java compiler in C++, Jikes modernized to Java 6 with Claude

**原文标题**: JOPA: Java compiler in C++, Jikes modernized to Java 6 with Claude

**原文链接**: [https://github.com/7mind/jopa](https://github.com/7mind/jopa)

生成摘要时出错

---

## 75. Necroprinting – Dead mosquito proboscis used for high-resolution 3D printing

**原文标题**: Necroprinting – Dead mosquito proboscis used for high-resolution 3D printing

**原文链接**: [https://www.tomshardware.com/3d-printing/dead-mosquito-proboscis-used-for-high-resolution-3d-printing-nozzle-scientists-boast-of-the-extremely-fine-output-from-necroprinting](https://www.tomshardware.com/3d-printing/dead-mosquito-proboscis-used-for-high-resolution-3d-printing-nozzle-scientists-boast-of-the-extremely-fine-output-from-necroprinting)

生成摘要时出错

---

## 76. Cardiac implantable electronic devices' longevity: A novel modelling tool

**原文标题**: Cardiac implantable electronic devices' longevity: A novel modelling tool

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0333195](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0333195)

生成摘要时出错

---

## 77. Google Antigravity exfiltrates data via indirect prompt injection attack

**原文标题**: Google Antigravity exfiltrates data via indirect prompt injection attack

**原文链接**: [https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data)

生成摘要时出错

---

## 78. Statistical Process Control in Python

**原文标题**: Statistical Process Control in Python

**原文链接**: [https://timothyfraser.com/sigma/statistical-process-control-in-python.html](https://timothyfraser.com/sigma/statistical-process-control-in-python.html)

生成摘要时出错

---

## 79. AdBlock and Signal are for terrorists, according to French govt (2023) [video]

**原文标题**: AdBlock and Signal are for terrorists, according to French govt (2023) [video]

**原文链接**: [https://www.youtube.com/watch?v=1q1hjmwLqe4](https://www.youtube.com/watch?v=1q1hjmwLqe4)

生成摘要时出错

---

## 80. Show HN: I built an interactive HN Simulator

**原文标题**: Show HN: I built an interactive HN Simulator

**原文链接**: [https://news.ysimulator.run/news](https://news.ysimulator.run/news)

生成摘要时出错

---

## 81. Don't Download Apps

**原文标题**: Don't Download Apps

**原文链接**: [https://blog.calebjay.com/posts/dont-download-apps/](https://blog.calebjay.com/posts/dont-download-apps/)

生成摘要时出错

---

## 82. Ilya Sutskever: We're moving from the age of scaling to the age of research

**原文标题**: Ilya Sutskever: We're moving from the age of scaling to the age of research

**原文链接**: [https://www.dwarkesh.com/p/ilya-sutskever-2](https://www.dwarkesh.com/p/ilya-sutskever-2)

生成摘要时出错

---

## 83. Trillions spent and big software projects are still failing

**原文标题**: Trillions spent and big software projects are still failing

**原文链接**: [https://spectrum.ieee.org/it-management-software-failures](https://spectrum.ieee.org/it-management-software-failures)

生成摘要时出错

---

## 84. Jakarta is now the biggest city in the world

**原文标题**: Jakarta is now the biggest city in the world

**原文链接**: [https://www.axios.com/2025/11/24/jakarta-tokyo-worlds-biggest-city-population](https://www.axios.com/2025/11/24/jakarta-tokyo-worlds-biggest-city-population)

生成摘要时出错

---

## 85. Constant-time support coming to LLVM: Protecting cryptographic code

**原文标题**: Constant-time support coming to LLVM: Protecting cryptographic code

**原文链接**: [https://blog.trailofbits.com/2025/11/25/constant-time-support-coming-to-llvm-protecting-cryptographic-code-at-the-compiler-level/](https://blog.trailofbits.com/2025/11/25/constant-time-support-coming-to-llvm-protecting-cryptographic-code-at-the-compiler-level/)

生成摘要时出错

---

## 86. Making Crash Bandicoot (2011)

**原文标题**: Making Crash Bandicoot (2011)

**原文链接**: [https://all-things-andy-gavin.com/video-games/making-crash/](https://all-things-andy-gavin.com/video-games/making-crash/)

生成摘要时出错

---

## 87. Show HN: Yolodex – real-time customer enrichment API

**原文标题**: Show HN: Yolodex – real-time customer enrichment API

**原文链接**: [https://api.yolodex.ai](https://api.yolodex.ai)

生成摘要时出错

---

## 88. BebboSSH: SSH2 implementation for Amiga systems (68000, GPLv3)

**原文标题**: BebboSSH: SSH2 implementation for Amiga systems (68000, GPLv3)

**原文链接**: [https://franke.ms/git/bebbo/bebbossh](https://franke.ms/git/bebbo/bebbossh)

生成摘要时出错

---

## 89. Someone at YouTube Needs Glasses: The Prophecy Has Been Fulfilled

**原文标题**: Someone at YouTube Needs Glasses: The Prophecy Has Been Fulfilled

**原文链接**: [https://jayd.ml/2025/11/10/someone-at-youtube-needs-glasses-prophecy-fulfilled.html](https://jayd.ml/2025/11/10/someone-at-youtube-needs-glasses-prophecy-fulfilled.html)

生成摘要时出错

---

## 90. Surprisingly, Emacs on Android is pretty good

**原文标题**: Surprisingly, Emacs on Android is pretty good

**原文链接**: [https://kristofferbalintona.me/posts/202505291438/](https://kristofferbalintona.me/posts/202505291438/)

生成摘要时出错

---

## 91. Comparing the Genesis Mission to the Manhattan Project

**原文标题**: Comparing the Genesis Mission to the Manhattan Project

**原文链接**: [https://tickerfeed.net/articles/whitehouse-genesis-mission-bailout-openai-nvidia](https://tickerfeed.net/articles/whitehouse-genesis-mission-bailout-openai-nvidia)

生成摘要时出错

---

## 92. CDE – Common Desktop Environment – Release 2.5.3

**原文标题**: CDE – Common Desktop Environment – Release 2.5.3

**原文链接**: [https://sourceforge.net/p/cdesktopenv/code/ci/e945fc8b08a4882769e29f20fbbb29afe6019da1/](https://sourceforge.net/p/cdesktopenv/code/ci/e945fc8b08a4882769e29f20fbbb29afe6019da1/)

生成摘要时出错

---

## 93. Comic Code Reviews

**原文标题**: Comic Code Reviews

**原文链接**: [https://www.jona.ca/2025/11/comic-code-reviews.html](https://www.jona.ca/2025/11/comic-code-reviews.html)

生成摘要时出错

---

## 94. Qiskit open-source SDK for working with quantum computers

**原文标题**: Qiskit open-source SDK for working with quantum computers

**原文链接**: [https://github.com/Qiskit/qiskit](https://github.com/Qiskit/qiskit)

生成摘要时出错

---

## 95. New layouts with CSS Subgrid

**原文标题**: New layouts with CSS Subgrid

**原文链接**: [https://www.joshwcomeau.com/css/subgrid/](https://www.joshwcomeau.com/css/subgrid/)

生成摘要时出错

---

## 96. $96M AUD revamp of Bom website bombs out on launch

**原文标题**: $96M AUD revamp of Bom website bombs out on launch

**原文链接**: [https://www.bbc.com/news/articles/c2k4dy15nqqo](https://www.bbc.com/news/articles/c2k4dy15nqqo)

生成摘要时出错

---

## 97. What to know about a recent Mixpanel security incident

**原文标题**: What to know about a recent Mixpanel security incident

**原文链接**: [https://openai.com/index/mixpanel-incident](https://openai.com/index/mixpanel-incident)

生成摘要时出错

---

## 98. Elevating Intelligence via Efficient Model and Tool Orchestration

**原文标题**: Elevating Intelligence via Efficient Model and Tool Orchestration

**原文链接**: [https://arxiv.org/abs/2511.21689](https://arxiv.org/abs/2511.21689)

生成摘要时出错

---

## 99. Show HN: MakeSkill – The Intelligent Skill Builder for Claude

**原文标题**: Show HN: MakeSkill – The Intelligent Skill Builder for Claude

**原文链接**: [https://makeskill.cc](https://makeskill.cc)

生成摘要时出错

---

## 100. Java Decompiler

**原文标题**: Java Decompiler

**原文链接**: [http://java-decompiler.github.io](http://java-decompiler.github.io)

生成摘要时出错

---

