# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-01.md)

*最后自动更新时间: 2025-06-01 17:49:05*
## 1. M8.2级太阳耀斑，强烈G4级地磁暴预警

**原文标题**: M8.2 solar flare, Strong G4 geomagnetic storm watch

**原文链接**: [https://www.spaceweatherlive.com/en/news/view/581/20250531-m8-2-solar-flare-strong-g4-geomagnetic-storm-watch.html](https://www.spaceweatherlive.com/en/news/view/581/20250531-m8-2-solar-flare-strong-g4-geomagnetic-storm-watch.html)

太阳耀斑爆发：M8.2级耀斑引发地磁暴预警

文章报道了从太阳黑子区域3697爆发的M8.2级太阳耀斑。这次耀斑导致日冕物质抛射(CME) направляющийся към Земята. 因此，已针对2024年6月2日发布了G4（强）地磁暴观测预警。

M8.2级耀斑意义重大，因为它是一种中等强度的耀斑，可能会导致地球向阳面发生无线电中断。 由于CME направляющийся към Земята， 地磁扰动的可能性和强度有所增加。 G4级风暴可能会导致广泛的电压控制问题、保护装置运行故障和卫星异常。 它还可能导致高频无线电传播变得零星或不存在，并且极光可能会在阿拉巴马州和加利福尼亚州北部以南的地方出现。

文章强调了CME的预计到达时间以及由此产生的地磁暴可能产生的影响。 建议监测空间天气状况，以了解预测的任何变化或更新。 简而言之，发生了一次重大的太阳事件，并且正在密切监测其对地球的影响，可能会对技术造成破坏并增强极光显示。

---

## 2. 如何在信用卡终端上获取 Root Shell 权限

**原文标题**: How I got a Root Shell on a Credit Card Terminal

**原文链接**: [https://stefan-gloor.ch/yomani-hack](https://stefan-gloor.ch/yomani-hack)

本文详细介绍了安全研究人员对 Worldline Yomani XR 信用卡终端的探索。研究人员发现，尽管存在硬件防篡改机制，但通过设备上的调试接口仍可访问 root shell 漏洞。

最初，拆解显示了篡改保护措施，如斑马条纹和蜿蜒的铜线，这些措施在物理入侵时会触发“检测到篡改”状态。然而，研究人员从闪存芯片中提取了固件，发现其未加密。该设备运行的是一个使用 Buildroot 2010.02 构建的过时的 Linux 内核 (3.6)。重新连接闪存芯片后，研究人员发现了一个串行控制台，只需以“root”身份登录，无需密码，即可轻松访问 root shell。

尽管存在篡改检测，但设备外部可访问的调试端口意味着攻击者可以在不触发篡改保护的情况下获得 root 权限，并可能在几秒钟内部署恶意软件。

然而，进一步的分析揭示了一个双核系统架构。运行在一个内核 (mp2) 上的 Linux 系统主要处理网络、更新和业务逻辑。另一个内核 (mp1) 处理敏感操作，如读卡、PIN 码输入和显示输出。两个内核之间的通信依赖于处理器间消息。安全内核从加密和签名的镜像启动，这意味着不安全内核无法直接访问敏感信息。

研究人员已向制造商披露了该漏洞，并得出结论，虽然暴露的 root shell 是一个重大疏忽，但由于安全和不安全内核的分离，其对卡数据安全的影响似乎有限。作者怀疑该漏洞可能意外地存在于某些生产固件中，并可能在他们披露之前已得到修复。

---

## 3. 雅达利 Mega ST 商务新选择

**原文标题**: Atari Means Business with the Mega ST

**原文链接**: [https://www.goto10retro.com/p/atari-means-business-with-the-mega](https://www.goto10retro.com/p/atari-means-business-with-the-mega)

本文探讨了雅达利Mega ST，这是雅达利公司于1987年推出的首款面向专业用户的工作站尝试。Mega ST采用了低矮的“披萨盒”设计，可分离的Cherry机械键盘，内置风扇和电池供电的时钟。与之前的ST型号相比，其主要优势在于包含了一个用于更快图形处理的图形加速芯片，以及提供2MB或4MB的RAM，这在当时是一笔可观的容量。它还搭载了TOS 1.02，这是TOS的第一个ROM更新版本。

尽管具备这些特点，Mega ST仍然面临挑战。它的机箱设计具有局限性，处理器速度与更早、更便宜的ST型号相同，并且内部总线连接器插槽没有得到广泛使用。雅达利将其作为桌面出版解决方案与SLM804激光打印机一同销售，但由于雅达利品牌与游戏紧密相关，因此很难销售昂贵的产品。

Mega ST也面临着交付问题，原因是1Mbit DRAM的短缺和价格上涨，这影响了整个计算机行业。生产转向欧洲市场。Mega ST最终在1991/1992年被Mega STE取代。作者总结说，由于其尺寸、有限的可升级性和与1040ST相同的速度（除了键盘之外），Mega ST在今天并不受欢迎。

---

## 4. 《安多》的摄影

**原文标题**: Cinematography of "Andor"

**原文链接**: [https://www.pushing-pixels.org/2025/05/20/cinematography-of-andor-interview-with-christophe-nuyens.html](https://www.pushing-pixels.org/2025/05/20/cinematography-of-andor-interview-with-christophe-nuyens.html)

本文是对《安多》第二季摄影师克里斯托夫·纽恩斯的采访，他探讨了自己的职业生涯、电影制作技术的演变以及他在该剧中的工作。纽恩斯从胶片过渡到数字，欣赏这两种媒介，并强调LED照明的进步是一项颠覆性变革。他指出剧集制作发生了转变，如今质量可以与电影媲美，而他在整个职业生涯中都一直支持这种转变。

关于《安多》，纽恩斯与导演阿里尔·克莱曼、视觉特效总监莫汉·利奥和美术指导卢克·赫尔密切合作，广泛使用预演和情绪板。他希望提升该剧的视觉效果，通过使用全画幅传感器和变形镜头，力求风格更接近《侠盗一号》。他强调尽可能多地实景拍摄的重要性，以及在可行的情况下，使用LED墙和手绘背景而非绿幕的好处。

纽恩斯详细介绍了与视觉特效的合作过程，以及实景搭建和数字延伸之间的平衡，并举例说明了戈尔曼广场和抢劫场景。他分享说，该剧在包括巴塞罗那和伦敦在内的多个国家拍摄。他强调为不同的故事情节创造独特的视觉感受，例如，第4-6集具有受意大利都灵启发的寒冷冬季美学。对于婚礼场景，他选择了钨丝灯来实现经典外观，而雅文则力求营造“老星球大战电影”的感觉。

---

## 5. Figma幻灯片：美丽的灾难

**原文标题**: Figma Slides Is a Beautiful Disaster

**原文链接**: [https://allenpike.com/2025/figma-slides-beautiful-disaster](https://allenpike.com/2025/figma-slides-beautiful-disaster)

演示老手艾伦，因经常使用 Figma 进行设计，而探索将 Figma Slides 作为 Keynote 的替代方案。他称赞 Figma Slides 的网格视图、自动布局和组件能高效创建幻灯片，并强调其在构建诸如图表等视觉元素方面的优势。

然而，他很快就遇到了限制，包括缺乏自动调整大小的文本以及难以创建逐行显示的子弹要点。尽管存在这些缺点，艾伦仍然觉得构建过程令人愉快，并看到了 Figma 作为一家公司的发展潜力。

真正的问题出现在演示过程中。他发现离线演示不可靠，需要特定的、不直观的过程才能启用。演示视图笨拙，缺少全屏模式和简单的显示切换。最关键的失败发生在动画崩溃时，导致他每张幻灯片都需要多次点击，并尴尬地回溯来解释复杂的概念。

艾伦将这些失败归因于 Figma 没有将 Slides 的演示方面视为至关重要的任务。他将此与 Keynote 进行了对比，后者虽然在某些方面很笨拙，但受益于苹果公司对可靠演示体验的承诺。他总结说，虽然 Figma Slides 提供了有前途的设计功能，但其演示功能不可靠，最终巩固了像 Keynote 这样“无聊”但有效的技术的价值。他以幽默的口吻结束，成为了一个告诫人们不要优先考虑华而不实的新工具，而应选择可靠解决方案的反面教材。

---

## 6. 新一代Tailscale访问控制

**原文标题**: A new generation of Tailscale access controls

**原文链接**: [https://tailscale.com/blog/grants-ga](https://tailscale.com/blog/grants-ga)

Tailscale发布"Grants"，新一代访问控制系统正式可用。 Grants的设计比现有的ACL语法更易于读写，同时提供新的功能。重要的是，现有的ACL不会被弃用，可以与Grants共存。

主要改进和新功能包括：

*   **简化语法：** Grants将端口和协议合并到单个“ip”字段中，并删除冗余的“action”字段，使规则更简洁。
*   **应用能力：** Grants允许在Tailscale访问控制策略中直接定义特定于应用程序的权限。这是通过命名空间的JSON对象实现的，这些对象被传递给应用程序，然后应用程序可以使用它们进行授权决策，从而更容易与`tsnet`等工具集成。 一个Golink示例演示了如何使用Grants来分配管理员角色。
*   **路由感知（via）：** “via”字段允许指定设备在访问特定资源时必须使用的出口节点、子网路由器或应用连接器。 这支持基于位置的路由、区域路由和高可用性设置。

文章强调了一种渐进式的采用策略，向用户保证现有的ACL规则仍然完全支持，并且只有在他们希望利用Grants的新功能时才能增量更新。 TailSQL、Setec 和 Kubernetes API 服务器代理等多个开源工具证明了使用 Grants 的强大功能。

---

## 7. 微调的意义：开发者指南

**原文标题**: When Fine-Tuning Makes Sense: A Developer's Guide

**原文链接**: [https://getkiln.ai/blog/why_fine_tune_LLM_models_and_how_to_get_started](https://getkiln.ai/blog/why_fine_tune_LLM_models_and_how_to_get_started)

本文是一篇开发者指南，解释了何时以及为何微调大型语言模型（LLMs）。它认为微调解决了具体、可衡量的问题，例如JSON输出不一致、高昂的推理成本、复杂的提示和专业化的行为。

本文详细介绍了微调的益处，包括：

*   **提高任务质量：** 提升特定任务的性能、风格一致性和JSON格式的准确性。
*   **降低成本和提高速度：** 缩短提示长度，支持使用更小、更快的模型，并促进本地模型部署以实现隐私保护和成本节约。
*   **工具调用：** 教会模型如何以及何时有效地使用特定工具。
*   **更好的逻辑/规则遵循：** 帮助模型比单独使用提示更有效地学习规则和条件逻辑，并修复模型行为中的“错误”。
*   **从更大模型中提炼知识：** 将知识从更大的模型转移到更小、更高效的模型。
*   **更好的思考/推理：** 使模型能够有效地使用推理模式。

本文还告诫不要使用微调来添加知识，建议使用RAG、上下文加载和工具调用作为替代方案。

该指南强调了基于所需目标（移动部署、成本降低、最大化质量）选择适当的基础模型，并使用实验和评估（评估）来迭代和优化微调过程的重要性。最后，它建议使用Kiln，一个旨在简化微调工作流程的免费应用程序。

---

## 8. 为什么DeepSeek在大规模使用时很便宜，但本地运行却很昂贵

**原文标题**: Why DeepSeek is cheap at scale but expensive to run locally

**原文链接**: [https://www.seangoedecke.com/inference-batching-and-deepseek/](https://www.seangoedecke.com/inference-batching-and-deepseek/)

本文解释了为什么像 DeepSeek-V3 这样的模型大规模使用时成本低廉，但在本地运行时却很昂贵，原因在于服务大型语言模型 (LLM) 时吞吐量/延迟之间的权衡。

GPU 擅长进行大型矩阵乘法 (GEMM)。将用户请求批量处理可以更有效地利用 GPU，因为单个大型 GEMM 比许多小型 GEMM 更快。推理提供商通过排队传入的 token 请求，然后将它们一起处理来实现请求的批量处理。批量大小是一种权衡：大的批次可以提高吞吐量，但也会增加延迟，因为用户需要等待批次填满。

像 DeepSeek-V3 这样使用混合专家 (MoE) 架构并具有许多层的模型，需要大的批次大小才能提高效率。MoE 模型将计算分散在多个“专家”中，如果不进行批量处理，会导致许多小型矩阵乘法。具有许多层的大型模型需要在多个 GPU 上进行流水线处理，需要大的批次以避免流水线气泡（GPU 空闲时间）。

Transformer 中的注意力机制是基于序列长度进行批处理的。为了批量处理注意力，序列必须具有相同的长度，因此使用“ticks”系统。大的批次大小会导致更高的延迟，但可以提高 GPU 利用率和吞吐量。

作者认为 OpenAI 和 Anthropic 的模型速度更快，是因为它们要么具有更高效的架构，要么使用巧妙的技巧来提供推理服务，要么过度配置了 GPU。总而言之，DeepSeek-V3 的架构需要大的批次大小，因此导致高延迟，使其不适合单用户本地部署。

---

## 9. 从Amiga API/ABI中学习

**原文标题**: Learning from the Amiga API/ABI

**原文链接**: [https://asm-basic-coder.neocities.org/rants/amigaapilearn](https://asm-basic-coder.neocities.org/rants/amigaapilearn)

本文是对Amiga API/ABI的褒扬之词，称赞其设计和功能优于现代操作系统。作者强调其通过已知地址的跳转指令表直接调用共享库，特别提到Exec.library是访问其他库的基础。

Amiga ABI因其CPU独立性和与内存保护方案的兼容性而备受赞誉，使其非常适合多种编程语言。作者强调Amiga OS精心设计的内核（Exec）、列表管理、消息传递和多任务处理能力。Intuition的回调控件和BOOPSI在无需OO语言的情况下进行面向对象编程也受到赞扬。

本文将AmigaDOS最初受BCPL影响的API与后来的ARP.library进行了对比，后者提供了更友好的C接口。作者强调了Amiga的库系统所提供的动态性如何促成了这样的改进。

Intuition独特的事件处理机制也得到了展示，其中窗口系统可以调用应用程序来传递消息，即使主任务暂时冻结也能确保响应。这被认为是优于现代系统的一个重大优势，在现代系统中，主程序循环负责事件处理。作者认为Amiga OS是有史以来最直接、构思最完善的操作系统。

---

## 10. RenderFormer：基于全局光照的三角形网格神经渲染

**原文标题**: RenderFormer: Neural rendering of triangle meshes with global illumination

**原文链接**: [https://microsoft.github.io/renderformer/](https://microsoft.github.io/renderformer/)

RenderFormer是一种新型神经渲染管线，可以直接从场景的三角形网格表示生成图像，无需针对每个场景进行训练或微调即可包含完整的全局光照效果。与传统的基于物理的渲染不同，RenderFormer将渲染构建为使用Transformer架构的序列到序列转换。它将具有反射属性的三角形令牌序列转换为像素块令牌序列。

该管线由两个阶段组成：一个模拟三角形到三角形光传输的与视角无关的阶段，以及一个将光线束转换为像素值的与视角相关的阶段，该阶段由第一阶段的输出引导。这两个阶段都利用了具有最少先验约束的Transformer架构，从而消除了光栅化或光线追踪的需要。

该论文通过渲染图库展示了RenderFormer的功能，展示了康奈尔盒、斯坦福兔子以及更复杂的场景中各种照明条件、材质和几何复杂性。它还展示了RenderFormer渲染动画和基于物理的模拟的能力，突出了其在动态场景渲染方面的潜力。作者提供了视频结果，包括物体旋转、光照变化和材质调整的演示。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 2 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 3 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 4 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 5 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 6 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 7 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 8 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 9 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 10 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 11 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 12 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 13 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 14 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 15 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 16 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 17 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 18 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 19 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 20 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 21 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 22 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 23 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 24 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 25 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 26 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 27 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 28 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 29 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 30 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 31 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 32 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 33 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 34 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 35 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 36 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 37 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 38 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 39 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 40 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 41 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 42 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 43 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 44 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 45 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 46 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 47 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 48 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 49 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 50 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 51 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 52 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 53 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 54 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 55 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 56 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 57 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 58 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 59 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 60 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 61 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 62 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 63 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 64 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 65 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 66 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 67 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 68 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 69 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 70 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 71 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 72 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 73 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 74 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
