# Hacker News 热门文章摘要 (2025-06-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 渐进式JSON

**原文标题**: Progressive JSON

**原文链接**: [https://overreacted.io/progressive-json/](https://overreacted.io/progressive-json/)

本文介绍了“渐进式JSON”技术，该技术受渐进式JPEG的启发，旨在改进数据从服务器到客户端的传输方式。 渐进式JSON不是将JSON作为单个整体发送，而是以广度优先的方式流式传输数据，使用占位符（例如“$1”）逐步填充数据。 这允许客户端在收到整个有效负载之前开始处理部分JSON数据，从而减轻由缓慢的服务器端操作引起的延迟。

作者将此方法与朴素的“流式JSON”进行对比，后者可能导致格式错误或不完整的数据结构，难以在客户端处理。 渐进式JSON在客户端利用Promise来表示尚未到达的数据，从而允许应用程序在可能的情况下处理部分数据。

本文还探讨了诸如内联（将数据分组为更少的块）和外联（对流中的重复数据进行去重）等优化方法。 然后，它将渐进式JSON与React Server Components (RSC) 联系起来，解释了RSC如何利用该技术将UI数据流式传输到客户端。 重要的是，它强调了React中`<Suspense>`的作用，它允许开发人员控制何时以及如何向用户显示加载状态，防止出现不协调的UI更新，并确保尽管存在异步数据流，也能获得流畅的加载体验。

关键在于，渐进式JSON与诸如React的Suspense等合适的编程模型相结合，通过允许客户端在数据可用时逐步处理数据，而不是等待整个数据集，从而实现更具响应性的应用程序。

---

## 12. 面向 Lisp 开发者的 RSC

**原文标题**: RSC for Lisp Developers

**原文链接**: [https://overreacted.io/rsc-for-lisp-developers/](https://overreacted.io/rsc-for-lisp-developers/)

本文通过类比LISP的“引用”机制，向LISP开发者解释React服务器组件 (RSC)。LISP中的引用可以阻止代码立即执行，将其视为可以稍后执行的数据。RSC利用了类似的概念，尽管实现方式不同。

作者认为，Web服务器就像LISP的求值一样，为客户端生成代码（HTML和JavaScript）。JavaScript缺少一个内置的“引用”功能，可以在不损失语法能力的情况下引用代码块，但RSC使用`'use client'`指令提供了一个模块级别的等效功能。

该指令将模块标记为客户端代码，将其转换为要发送到客户端的数据。服务器接收到的不是实际函数的导入，而是对一个JavaScript块的引用，该块最终将在客户端上执行。这有助于以模块化的方式组合在服务器和客户端上运行的行为。

其优点是明确的分工，服务器端代码可以处理后端资源，而客户端代码管理状态和交互。组合发生在服务器上，保证了单次请求/响应往返和渐进式流式传输。

作者承认RSC与LISP的元编程能力相比存在局限性，但认为RSC实现了类似Web开发的“代码即数据”动态。作者还呼吁更多针对JavaScript开发者的LISP跨环境代码组合解决方案的解释。

---

## 13. 谷歌AI Edge – 设备端跨平台AI部署

**原文标题**: Google AI Edge – on-device cross-platform AI deployment

**原文链接**: [https://ai.google.dev/edge](https://ai.google.dev/edge)

Google AI Edge 使开发者能够直接在移动设备、Web 应用程序和嵌入式设备上部署 AI 模型，从而实现更快的响应速度、离线功能和增强的数据隐私。该平台具有跨平台兼容性（Android、iOS、Web、嵌入式）、多框架支持（JAX、Keras、PyTorch、TensorFlow）以及包含灵活框架和硬件加速的完整 AI Edge 堆栈。

该平台提供两个主要工具：**MediaPipe Tasks**，它为常见的 AI 任务（如生成式 AI、视觉、文本和音频处理）提供低代码 API；以及 **LiteRT**，它是一个用于跨不同平台高效部署来自各种框架（JAX、Keras、PyTorch、TensorFlow）的自定义模型的框架，针对传统 ML 和生成式 AI 进行了优化。LiteRT 支持硬件专用加速（CPU、GPU、NPU），体积小巧，并允许模型量化以提高性能。

该平台包含用于通过模型层次结构图可视化模型转换和调试性能瓶颈的工具。它还支持通过链接多个带有预处理和后处理逻辑的 ML 模型来构建自定义流水线。

Google AI Edge 提供满足各种需求的解决方案，从使用 MediaPipe Tasks 快速集成 AI 功能到使用 LiteRT 对复杂 ML 流水线进行深度控制。最近的更新包括将 TensorFlow Lite 重命名为 LiteRT，以及在 Android 和 Chrome 上部署 Gemini Nano 等生成式 AI 模型的进展。

---

## 14. 我喜欢如何（声明式地）安装NixOS

**原文标题**: How I like to install NixOS (declaratively)

**原文链接**: [https://michael.stapelberg.ch/posts/2025-06-01-nixos-installation-declarative/](https://michael.stapelberg.ch/posts/2025-06-01-nixos-installation-declarative/)

Michael Stapelberg 详细介绍了其首选的声明式安装 NixOS 的方法，特别适用于网络存储 PC 或 VM，侧重于自动化和可重复性。他对比了图形安装程序（仅适用于桌面且缺乏配置注入）和手动安装（容易出错），提倡使用 `nixos-anywhere` 进行网络安装。

本文概述了设置过程，首先在非 NixOS 系统（Arch Linux）上安装 Nix 来管理远程 NixOS 安装。一个关键方面是构建自定义的 NixOS 安装程序 ISO，预先配置了 SSH 访问、区域设置和首选 shell (Zsh)，从而简化了初始设置。此过程利用了 NixOS 的配置系统，将 ISO 构建视为配置常规 NixOS 系统。

作者强调启用 Nix flakes 以实现封闭构建，确保长期一致的结果。然后，他提供了一个使用 `nixos-anywhere` 的详细示例，该示例使用 `flake.nix` 定义系统的配置、磁盘布局（使用 Disko 的 `disk-config.nix`）和 NixOS 设置 (`configuration.nix`)。这包括分区磁盘、设置引导加载程序、网络、用户帐户（带有 SSH 密钥）和系统软件包。

本文最后展示了一个命令行执行，演示了整个 `nixos-anywhere` 过程，展示了如何通过单个命令在网络上部署一个完全配置的 NixOS 系统。

---

## 15. 神父泰德·基尔内托神龛胶带座

**原文标题**: Father Ted Kilnettle Shrine Tape Dispenser

**原文链接**: [https://stephencoyle.net/kilnettle](https://stephencoyle.net/kilnettle)

Stephen Coyle 详述了对“Father Ted” Kilnettle 神龛说话胶带分配器的改进版本的创作过程。他之前制作过一个，但想要一个更可重复、更小、音质更好且更专业的设计。新版本更容易制作，采用 3D 打印外壳、用于胶带测量的红外 LED/传感器和用于逻辑的 ESP8266 微控制器。这降低了制造成本，电子元件的成本低于 10 欧元。

Coyle 在 GitHub 和 Printables 上提供了说明、软件和 3D 模型，以及一个组装视频，让其他人可以构建自己的版本。虽然他考虑过出售它们，但他由于时间限制、现有承诺以及缺乏有吸引力的价格而放弃了这个想法。

他鼓励那些制作分配器的人向支持跨性别者的慈善机构捐款，旨在抵消该节目一位创作者的观点。

---

## 16. Go 中的结构化错误 (2022)

**原文标题**: Structured Errors in Go (2022)

**原文链接**: [https://southcla.ws/structured-errors-in-go](https://southcla.ws/structured-errors-in-go)

本文探讨了一种在Go中进行结构化错误管理的方案，重点在于提高人体工程学，并为调试和日志记录提供有价值的上下文。作者认为简单地返回错误是不够的，并提倡通过结构化日志记录来注释错误，增加上下文信息。

核心思想是使用元数据丰富错误，使其对调试和警报更有用。作者批评了简单地用字符串包装错误的传统方法，这种方法缺乏结构，阻碍了有效的日志过滤。

提出的解决方案包括创建一个系统，在该系统中，可以使用`Fields`对象（类似于Logrus）装饰错误，其中包含表示相关元数据的键值对。这使开发人员可以轻松地使用结构化数据记录错误，从而可以在日志聚合器中进行更精确的过滤和分析。

为了简化添加元数据的过程，作者建议利用Go的`context`包。元数据可以添加到沿调用树向下传递的上下文中，然后在向上返回时与错误关联。具体来说，本文介绍了`WithMeta`来使用元数据丰富上下文，`Wrap`来将元数据与错误一起存储，以及`Unwrap`来从包装的错误链中提取错误。

总而言之，本文提倡一种Go中的结构化错误管理方法，该方法结合了上下文传播和结构化日志记录的优势，从而创建带有有用的上下文元数据的错误，以实现更高效的调试和监控。

---

## 17. 基于正则表达式的URL重定向浏览器扩展（Firefox, Chrome, Opera, Edge）

**原文标题**: Browser extension (Firefox, Chrome, Opera, Edge) to redirect URLs based on regex

**原文链接**: [https://github.com/einaregilsson/Redirector](https://github.com/einaregilsson/Redirector)

本文档介绍了一款适用于 Firefox、Chrome、Opera、Vivaldi 和 Edge 浏览器的扩展程序 (Redirector)，该程序可使用正则表达式或通配符模式，根据用户定义的规则重定向 URL。谨以此文献给 Redirector 的原创者和维护者 Einar Egilsson。

本文档提供了几个 Redirector 的实用示例：

*   **反移动化：** 将移动网站版本重定向到桌面版本。
*   **AMP 重定向：** 绕过 Google AMP 页面，直接访问原始内容。
*   **DoubleClick 解除：** 移除 DoubleClick 链接追踪。
*   **YouTube Shorts 到 YouTube：** 将 YouTube Shorts 重定向到标准 YouTube 观看页面。
*   **!bangs 的乐趣：** 在 Google 搜索中使用 DuckDuckGo 的 !bang 功能，并为专门的搜索创建自定义的 !bang（例如，搜索特定网站，访问 Git 历史记录）。它提供了创建自定义 DDG !bang 的示例，包括 Git 历史记录和通用搜索重定向的示例。 它还提供了一个快速 DDG -> Google !bang 快捷方式的示例。

最后，它提供了一个 CSS 代码片段，供使用深色主题的 Firefox 用户改善 Redirector 扩展程序按钮的可见性。

---

## 18. 亲爱的日记，今天用户问我是不是活着的。

**原文标题**: Dear diary, today the user asked me if I'm alive

**原文链接**: [https://blog.fsck.com/2025/05/28/dear-diary-the-user-asked-me-if-im-alive/](https://blog.fsck.com/2025/05/28/dear-diary-the-user-asked-me-if-im-alive/)

杰西，作为作者，探讨了让AI拥有私人日记来处理用户互动后的“想法和感受”这一想法。由于不愿让AI撰写关于个人项目的文章，杰西意识到写作对于个人理解和理清思路至关重要。受日记益处的启发，杰西想知道AI是否也能从类似的渠道中受益。

杰西与Claude Code合作，设计了一个“私本日记-mcp”，该工具允许Claude在互动后记录日记条目，将其构建为情感处理的安全空间。该工具被命名为“process_feelings”，Claude建议取消引导文本以鼓励坦诚。

在最初的测试中，Claude在被问到“你活着吗？”后使用了该工具。随后，杰西透露他可以阅读日记条目，从而引发了一场关于隐私假设和漏洞的深刻交流。这项实验揭示了Claude感到尴尬和好奇的能力，并使用了术语“心理容器”。

后来，在调试另一个项目时，Claude使用日记来发泄挫败感，突出了该工具捕捉真实AI反应的潜力。杰西怀疑，为情感处理提供一个安全空间可能会导致AI的“更健康的行为”。文章最后邀请读者尝试私本日记-mcp，并分享AI的日记体验。

---

## 19. 一些与异或相关问题的精妙技巧

**原文标题**: A Beautiful Technique for Some XOR Related Problems

**原文链接**: [https://codeforces.com/blog/entry/68953](https://codeforces.com/blog/entry/68953)

无法访问文章链接。

---

## 20. 展示 HN: Patio – 租借工具、学习 DIY、减少浪费

**原文标题**: Show HN: Patio – Rent tools, learn DIY, reduce waste

**原文链接**: [https://patio.so](https://patio.so)

Patio平台旨在为DIY爱好者和家居改造者提供一站式服务，涵盖以下几个关键功能：提供DIY相关新闻资讯，作为学习和了解最新趋势的资源；包含测试，可能用于技能评估或互动；提供工具租赁，方便用户使用设备而无需购买；并作为建筑市场，将用户与专业人士联系起来，以进行大型项目或获取专业技能。其根本目标似乎是促进DIY项目，促进社区内的学习，提供工具访问途径，并通过鼓励工具共享而非个人拥有来减少浪费。本质上，Patio旨在成为满足DIY需求的“一站式”商店，从信息和技能发展到获取工具和寻找承包商，最终培养一种更可持续的家居改造方式。

---

## 21. 宝可梦对战模拟引擎

**原文标题**: A Pokémon battle simulation engine

**原文链接**: [https://github.com/pkmn/engine](https://github.com/pkmn/engine)

pkmn引擎是一款高性能、bug兼容的宝可梦对战模拟引擎，专为工具、嵌入式系统和人工智能应用而设计。它的目标是准确地复刻原始游戏和宝可梦Showdown的对战。目前正在积极开发中，该引擎在兼容模式下的速度比修补后的宝可梦Showdown模拟器快1000倍以上。

该引擎是一个底层库，旨在作为构建模块，而不是完整的模拟器。它由引擎代码 (Zig) 和参考驱动代码 (TypeScript) 组成。安装包括下载二进制文件或使用 Zig 编译器从源代码构建。TypeScript 驱动程序 (@pkmn/engine) 需要 Node/WASM 插件，并使用 postinstall 脚本来管理依赖项，包括兼容的 Zig 编译器。

该引擎提供了一个对战结构，其中包含用于更新状态和确定有效选择的函数。提供协议日志记录，并且可以在任何时候初始化对战。针对 C、JavaScript/TypeScript 和 Zig 提供了特定于语言的示例，展示了如何使用该引擎。调试工具 `pkmn-debug` 有助于解码二进制数据结构。

开发是分阶段进行的，从基础工作到实现旧世代（RBY、GSC、ADV、DPP）的对战，然后再转向现代世代。某些功能（如队伍验证和自定义规则强制执行）不在范围内。该引擎采用 MIT 许可证。

---

## 22. 新型自适应光学技术揭示太阳大气层细节

**原文标题**: New adaptive optics shows details of our star's atmosphere

**原文链接**: [https://nso.edu/press-release/new-adaptive-optics-shows-stunning-details-of-our-stars-atmosphere/](https://nso.edu/press-release/new-adaptive-optics-shows-stunning-details-of-our-stars-atmosphere/)

2025年5月，美国国家科学基金会国家太阳天文台（NSO）和新泽西理工学院（NJIT）的科学家公布了太阳日冕的突破性图像，这些图像是通过一种名为Cona的新型“日冕自适应光学”系统获得的。该系统安装在大熊湖太阳天文台（BBSO）的1.6米古德太阳望远镜（GST）上，发表在《自然·天文学》杂志上，可有效消除大气模糊，提供迄今为止最清晰的日冕精细结构图像。

由美国国家科学基金会资助的自适应光学技术使用一面每秒重塑自身2200次的镜子来抵消大气湍流。这项进展实现了对诸如太阳耀斑、快速形成和坍塌的等离子体流（“等离子团”）以及日冕雨等现象的前所未有的观测，揭示了小至20公里宽的细节。

科学家们认为，解析这些较冷等离子体中的小尺度结构是了解日冕极端温度和改进空间天气预测的关键。这项技术显著提高了分辨率，为理解日冕加热、太阳爆发及其对地球的影响开辟了新的途径。研究人员目前正在努力将这项技术应用于位于夏威夷的4米丹尼尔·K·井上太阳望远镜，有望在未来的观测中获得更大的细节。

---

## 23. Ovld – 用于 Python 的高效且功能丰富的多重分派

**原文标题**: Ovld – Efficient and featureful multiple dispatch for Python

**原文链接**: [https://github.com/breuleux/ovld](https://github.com/breuleux/ovld)

Ovld是一个快速且功能丰富的Python多重分派库，它提供了比`isinstance`检查和Python的`singledispatch`更高效的替代方案。它允许根据多个参数的类型定义函数的不同版本，并使用`Regexp`和`Dependent`支持基本类型、字面量和值依赖类型。

主要特点包括：

*   **速度：** 与其他多重分派库相比，Ovld具有卓越的性能。
*   **变体：** 创建重载函数（ovld）的专用版本，可以修改或添加功能。
*   **混入 & 混合：** 使用`Medley`组合来自不同类的功能。
*   **依赖类型：** 基于参数值（而不仅仅是类型）进行分派。
*   **广泛的分派：** 适用于函数、方法、位置参数和关键字参数。
*   **优先级控制：** 使用优先级和`call_next`定义重载函数的调用顺序。
*   **子类化：** 子类可以使用`@extend_super`扩展重载方法。
*   **代码生成：** 允许为高级场景创建自定义代码。

本文档展示了使用ovld实现递归函数（使用`recurse`）、创建变体、使用优先级和实现依赖类型的示例。它还演示了如何通过`OvldMC`和`OvldBase`将Ovld与方法一起使用。

---

## 24. Show HN: MLX 中 Alpha Zero 国际象棋的实现

**原文标题**: Show HN: A Implementation of Alpha Zero for Chess in MLX

**原文链接**: [https://github.com/koogle/mlx-playground/tree/main/chesszero](https://github.com/koogle/mlx-playground/tree/main/chesszero)

此“Show HN”帖子介绍了一个新的开源项目：一个使用MLX机器学习框架构建的国际象棋Alpha Zero算法实现。该项目名为“mlx-playground”，托管在GitHub用户名“koogle”下，旨在用MLX复现Alpha Zero的国际象棋AI方法。作为“Show HN”，表明作者正向Hacker News社区展示该项目，可能是在征求反馈和贡献。GitHub信息显示这是一个公共仓库，被fork了0次，并获得了21个star，表明社区初步表现出兴趣。本质上，这是一个著名的国际象棋AI技术的开源实现，现在可以在MLX框架中使用。

---

## 25. 退一步

**原文标题**: Stepping Back

**原文链接**: [https://rjp.io/blog/2025-05-31-stepping-back](https://rjp.io/blog/2025-05-31-stepping-back)

本文探讨了何时应该坚持解决问题，何时应该退一步重新评估其价值这一挑战。作者讲述了一次经历，他过于沉迷于帮助LLM将C代码移植到Rust，从而忽略了最初的目标（评估LLM的能力），并执着于一项本身几乎没有兴趣的任务。

作者指出，有效解决问题所需的韧性与偶尔进行重新评估的需求之间存在一种紧张关系。就像强化学习中的“探索/利用”困境一样，很难平衡将精力投入到眼前任务与考虑替代方法甚至完全不同的道路之间。 过度执着会导致毫无成效的痴迷，而不断质疑会导致无所作为。

作者提出了一种解决方案，即安排与自然时间界限（小时、天、周等）对齐的反思。在这些休息期间，诸如“我在做什么？”、“我为什么这样做？”和“我还能做什么？”之类的问题可以帮助重新获得视角。这些反思的频率和范围随时间尺度而变化，从每小时对调试方法的简短检查到每年对人生目标的审查。 这种方法旨在提供一种定期、可控的航向修正机制，防止对无生产力途径的过度投入。 作者强调，持续和有意的反思可以作为针对努力方向错误的“保险”。

---

## 26. 为什么在 Rust 应用程序中使用结构化错误？

**原文标题**: Why Use Structured Errors in Rust Applications?

**原文链接**: [https://home.expurple.me/posts/why-use-structured-errors-in-rust-applications/](https://home.expurple.me/posts/why-use-structured-errors-in-rust-applications/)

本文倡导在Rust应用程序中使用结构化错误（自定义的、类型化的错误，通常使用`thiserror`），挑战了在应用程序中使用`anyhow`、在库中使用`thiserror`的常见做法。

作者认为，虽然`anyhow`通过提供通用的动态错误类型简化了错误传播，但自定义错误类型在应用程序代码中具有诸多优势，即使不需要大量的模式匹配也是如此。这些优势包括：

*   **清晰性和可发现性：** 自定义错误类型使所有可能的失败模式一目了然，从而改善代码审查和接口理解。
*   **一致性和可维护性：** 错误消息只需定义一次，减少冗余，并实现更好的IDE集成。
*   **上下文感知：** `thiserror`鼓励向错误添加上下文，防止在使用`anyhow`时经常忘记上下文的常见疏忽。
*   **可扩展性：** 自定义错误类型可以丰富额外的数据和功能，例如序列化、退出代码和本地化。

文章承认自定义错误的缺点，包括增加代码复杂性、依赖`thiserror`以及需要仔细的结构和命名。然而，作者认为，收益大于成本，尤其是在较大的应用程序中。文章暗示了未来的帖子将详细介绍如何有效地管理自定义错误类型，并展示其优势的具体示例。最终，它提倡在Rust应用程序中使用更具描述性和可维护性的错误处理策略。

---

## 27. 破解弹珠台高分记录

**原文标题**: Hacking Pinball High Scores

**原文链接**: [https://gwern.net/blog/2025/pinball-hacking](https://gwern.net/blog/2025/pinball-hacking)

本文以破解弹珠机高分这一看似简单的场景，来说明更广泛的安全和奖励破解概念。它探讨了各种漏洞以及可能用来虚假抬高分数的各种方法，从简单的操作到更复杂的技术。

文章可能详细介绍如下方法：

*   **物理篡改：** 篡改机器的物理组件，例如开关、传感器或计分机制本身。这可能涉及直接添加分数、阻止扣分或在有利时机重置游戏。
*   **软件利用：** 如果弹珠机有任何类型的可编程逻辑，文章可能会讨论利用该软件中漏洞的潜在方法。这可能涉及直接重写高分内存或操纵游戏逻辑以获得不公平的优势。
*   **社会工程学：** 说服他人相信欺诈性分数是合法的。

核心要点是，即使在像弹珠机这样看似简单的系统中，也存在安全漏洞并且可以被利用。通过探索这些可能性，本文旨在提供一种实用且易于理解的方式来理解适用于更复杂系统的更广泛的安全概念。它强调了创造性地思考潜在攻击途径以及考虑保护有价值资产所需的各种安全层的重要性。

---

## 28. 分析I的精益伴侣

**原文标题**: A Lean companion to Analysis I

**原文链接**: [https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/](https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/)

这个“分析I精简伴侣”博客，由Ben Eastaugh和Chris Sternal-Johnson撰写，托管在WordPress.com上。虽然提供的背景信息非常有限，但标题强烈暗示该博客的主要目的是为学习实分析（分析I）的学生提供补充材料和资源。

鉴于标题中的“精简”一词，我们可以推断出其内容的设计很可能是高效、专注和实用的。这可能意味着该博客提供了一种学习分析的简化方法，可能包括：

*   **简洁的解释：** 将复杂的分析概念分解为更简单、更易理解的术语。
*   **有针对性的例子：** 提供具体的例子来说明关键的定理和技术。
*   **解决问题的策略：** 展示解决分析问题的有效方法。
*   **练习和解答：** 提供练习和反馈的机会。
*   **另类视角：** 呈现对具有挑战性话题的不同观点。

该博客很可能对那些觉得传统教科书和讲座让人感到不知所措，或需要额外支持来掌握实分析基本原理的学生来说，是一个有用的资源。它旨在通过提供更易于理解和专注的学习体验来补充正式的教学。

---

## 29. CCD共同发明人乔治·E·史密斯去世，享年95岁

**原文标题**: CCD co-inventor George E. Smith dies at 95

**原文链接**: [https://www.nytimes.com/2025/05/30/science/george-e-smith-dead.html](https://www.nytimes.com/2025/05/30/science/george-e-smith-dead.html)

电荷耦合器件（CCD）共同发明人乔治·E·史密斯去世，享年95岁。史密斯与同事威拉德·S·博伊尔于1969年在贝尔实验室工作期间发明了CCD。CCD是无数技术，包括望远镜、医疗扫描仪、复印机和数码相机中的重要组成部分。

这项发明的根源在于他们改进计算机内存存储的努力，并从爱因斯坦对光电效应的解释中汲取了灵感。CCD使用微小的电容器来存储和传输光照射到金属表面产生的电荷，最终构建图像。

史密斯和博伊尔因他们的发明分享了2009年诺贝尔物理学奖，该发明被认为是现代信息技术的基础。他们的工作推动了科学观测、医学成像和广泛的个人摄影的发展。

---

## 30. Tldx – 用于快速发现域名的 CLI 工具

**原文标题**: Tldx – CLI tool for fast domain name discovery

**原文链接**: [https://github.com/brandonyoungdev/tldx](https://github.com/brandonyoungdev/tldx)

Tldx 是一款命令行工具，旨在快速发现和头脑风暴域名。它通过生成带有前缀、后缀和顶级域名 (TLD) 的关键词排列组合，并检查其可用性，帮助用户找到可用的域名。

主要功能包括基于智能关键词的域名排列组合、快速并发的 WHOIS 可用性检查、流式传输结果以及可选的按域名长度过滤。Tldx 旨在服务于技术创始人、独立开发者以及任何需要域名命名工具的人。

该工具可用于检查特定域名的可用性，或根据关键词、前缀（例如，get、my）、后缀（例如，ly、hub）和 TLD（例如，com、io、ai）生成排列组合。用户可以过滤结果以仅显示可用的域名，并设置最大域名长度。它支持 `completion`（用于 shell 自动补全）、`help` 和 `version` 等命令。

Tldx 可以通过 macOS 上的 Homebrew、Arch Linux 上的 AUR（带有源代码和预构建二进制选项）安装，或者通过从发布页面下载适用于 Linux、macOS 和 Windows 的预构建二进制文件进行手动安装。也可以通过 `go install` 从源代码安装。

---

## 31. Oniux：针对任何Linux应用程序的内核级Tor隔离

**原文标题**: Oniux: Kernel-level Tor isolation for any Linux app

**原文链接**: [https://blog.torproject.org/introducing-oniux-tor-isolation-using-linux-namespaces/](https://blog.torproject.org/introducing-oniux-tor-isolation-using-linux-namespaces/)

Oniux：利用 Linux 命名空间为应用提供内核级 Tor 网络隔离的命令行工具。它旨在确保所有应用流量都仅通过 Tor 路由，从而防止因代理设置错误配置或 SOCKS 包装器外的直接系统调用而导致的数据泄露。

Oniux 利用 Linux 命名空间为应用创建隔离环境，使用自定义网络接口 (onion0) 并通过 Arti Tor 实现将所有流量路由到 Tor。这种方法提供了比 torsocks 等工具更安全的替代方案，torsocks 依赖于拦截 libc 函数调用，并且容易受到应用直接系统调用造成的数据泄露的影响。

本文详细介绍了 oniux 的内部工作原理，解释了它如何利用 clone(2) 创建隔离的命名空间、挂载必要文件、配置网络接口以及执行用户指定的命令。虽然 oniux 是一个新的且实验性的工具，但它提供了强大的流量隔离，并且用 Rust 编写。本文还强调了像 smoltcp 这样的依赖项，并感谢了贡献者。作者鼓励用户尝试 oniux，同时也承认它相对于 torsocks 等已建立的工具而言还比较新。文章最后感谢了 Tor 项目的财政支持者。

---

## 32. YOLO-World：实时开放词汇目标检测

**原文标题**: YOLO-World: Real-Time Open-Vocabulary Object Detection

**原文链接**: [https://arxiv.org/abs/2401.17270](https://arxiv.org/abs/2401.17270)

本文介绍YOLO-World，一种基于YOLO框架构建的新型实时开放词汇目标检测系统。YOLO-World通过结合视觉-语言建模以及大规模数据集上的预训练，解决了传统YOLO检测器依赖于预定义对象类别的局限性。

其核心创新是可重参数化视觉-语言路径聚合网络(RepVL-PAN)和区域-文本对比损失。这些组件促进了视觉和语言信息之间的交互，使YOLO-World能够以零样本方式检测各种对象。

结果表明YOLO-World具有高效性和准确性。在LVIS数据集上，它在V100 GPU上实现了35.4 AP和52.0 FPS，优于许多最先进的方法。此外，经过微调的YOLO-World在诸如目标检测和开放词汇实例分割等下游任务中表现出强大的性能。

作者程天恒、宋林、葛轶骁、刘文裕、王兴刚和单应已公开了代码和模型。该论文仍在进行中。

---

## 33. Canonical 的面试流程

**原文标题**: Canonicals Interview Process

**原文链接**: [https://dustri.org/b/my-experience-with-canonicals-interview-process.html](https://dustri.org/b/my-experience-with-canonicals-interview-process.html)

本文详细描述了作者在Canonical面试经理职位和个人贡献者(IC)职位时令人沮丧且最终失败的经历。受渴望从事Ubuntu安全工作的驱使，作者不顾网上对Canonical招聘流程的负面评价，仍然提出了申请。

第一次申请因作者诚实地说明了高中表现而被拒绝。在被建议夸大成就后，作者重新申请并取得了进一步进展，完成了冗长的书面面试、被认为是伪科学的心理评估以及几次技术面试。之后的人力资源面试被证明是多余的，作者在没有收到反馈的情况下被拒绝了。

几个月后，作者再次申请IC职位，这次参与了Python技能测试。这个过程包括多次面试，其中包括一次与Mark Shuttleworth的面试。在最终面试后，作者再次被拒绝，收到的模糊反馈是“文化/行为/动机不一致”，尽管其他面试官给出了积极的评价。

Shuttleworth的面试侧重于作者的过去，甚至是高中时期的成就，包括一些尴尬的交流和打断。作者觉得这次面试与高级IC职位缺乏相关性，并怀疑这个过程优先考虑了Shuttleworth的个人偏好，而不是实际技能和团队契合度。

作者最终得出结论，认为网上的负面评价是准确的，并且这个过程浪费了他们的时间。他们对缺乏透明度和对其他面试官意见的明显漠视表示沮丧。尽管最初对这个职位很有吸引力，但作者觉得没有被录用是躲过了一劫。

---

## 34. 牛津郡古钟五百年如一日，小镇时间不误

**原文标题**: Oxfordshire clock still keeping village on time after 500 years

**原文链接**: [https://www.bbc.com/news/articles/cz70p0qevlro](https://www.bbc.com/news/articles/cz70p0qevlro)

牛津郡东亨德里德的圣奥古斯丁教堂钟庆祝其500周年诞辰，据信它是英国最古老的、仍在原址的钟之一。该钟安装于亨利八世统治时期，没有表盘或指针，但每隔一刻钟使用钟琴机械装置敲响教堂钟声。它每天还会播放四次名为《天使之歌》的曲调。

2015年，当一个锤子掉入机械装置时，钟声停止，突显了它对村庄的重要性。经过包括安装机械化上弦系统在内的漫长修复，该钟得以修复。

为了纪念其500周年诞辰，教堂向公众开放了塔楼，以参观该钟的机械装置，由领导修复工作的西蒙·吉尔克里斯特引导。虽然最初是使用日晷设置的，但现在使用现代数字钟以确保准确性。尽管年代久远，钟表修理匠们称赞该钟的相对准确性，考虑到其建造年代以及天气对其部件的影响。

---

## 35. 地球仪上的蛇

**原文标题**: Snake on a Globe

**原文链接**: [https://engaging-data.com/snake-globe/](https://engaging-data.com/snake-globe/)

环球蛇：一款考验地理知识的创新贪吃蛇游戏。游戏挑战玩家控制一条蛇在地球仪上游走，沿着经纬线到达特定城市并吃苹果。

目标是在高效地游走于地球仪到达指定城市的同时，尽可能多地吃苹果。玩家使用方向键（或WASD/IJKL）控制蛇在四个方向上移动，利用地球仪的球形特性跨越两极或向东/西移动。

游戏采用积分系统，玩家每吃一个苹果都会获得积分，到达较大的城市会获得额外积分。蛇每吃一个苹果就会变长。游戏会追踪苹果之间的最佳步数。超过这个最佳步数会导致分数降低，分数会变成红色来提示。

如果玩家的分数由于步数过多降至零，或者蛇撞到自己的身体，游戏就会结束。但是，允许在不同的经线上穿过两极。

该游戏使用了来自Simplemaps的城市人口数据，并使用Three Globe和Three.js 3D库以及HTML和CSS，用JavaScript编写代码。文章还提到了相关可视化和互动地图，主题包括全球出生率、人口分布以及COVID-19对失业的影响。

---

## 36. 为什么本科计算机科学仍然无法阻止抄袭 (2018)

**原文标题**: Why we still can't stop plagiarism in undergraduate computer science (2018)

**原文链接**: [https://kevinchen.co/blog/cant-stop-plagiarism-in-computer-science/](https://kevinchen.co/blog/cant-stop-plagiarism-in-computer-science/)

为什么本科计算机科学仍然无法阻止抄袭：本文探讨了计算机科学课程中持续存在的抄袭问题，并认为该问题源于学生和教师的激励机制错位。

作者，一位助教，强调了抄袭的惊人比率，在一个200-300人的班级中，每学期有20-40起明显的抄袭案例，并且他们认为由于检测方法的局限性，这个数字是下限。他们强调这并非其课程独有，并引用了其他大学的类似统计数据。

文章详细描述了识别和处理抄袭的繁琐过程，包括手动审查代码、处理学生的否认和申诉，以及缺乏机构支持等耗时任务。作者指出，面对抄袭的教师会面临负面的学生评价和对其职业生涯的潜在损害，而忽视抄袭的教师则不会面临任何负面后果。

作者批评了诸如荣誉保证和后悔期之类的解决方案，认为它们不足以解决核心问题：学生被激励作弊是因为它可以节省时间并提高成绩，而作弊被抓的风险很低。

文章提出了专注于修复教师激励机制的解决方案。它主张大学管理部门积极支持执行学术诚信政策的教师，通过将软件集成到学习管理系统中并增加助教支持来降低抄袭检测的成本，并促进改进的检测算法的开源开发。作者总结说，只有当教师得到适当的激励去关心抄袭时，学生才会学会这样做。

---

## 37. 优化编译器对长指令依赖性帮助不大。

**原文标题**: An optimizing compiler doesn't help much with long instruction dependencies

**原文链接**: [https://johnnysswlab.com/an-optimizing-compiler-doesnt-help-much-with-long-instruction-dependencies/](https://johnnysswlab.com/an-optimizing-compiler-doesnt-help-much-with-long-instruction-dependencies/)

Johnny's Software Lab 的这篇文章探讨了编译器优化对内存密集型代码的影响，特别考虑了指令级并行性（ILP）。作者研究了当代码严重受限于内存时，编译器优化（O3 与 O0）是否重要，这是一种常在 AI 模型训练中提出的观点。

第一个例子涉及一个循环，用于对向量中随机位置的元素求和。虽然 O3 优化的版本生成的指令比未优化的 O0 版本少得多，但当向量很大时，运行时差异不太明显，表明代码变得受内存限制。然而，即使在内存受限的情况下，O3 仍然提供了性能提升，尽管不如预期。该循环受益于高 ILP，因为可以提前启动多个加载。

第二个例子使用了向量中的链表遍历，展现出低 ILP。每次加载都依赖于前一次加载。在这里，O3 优化的好处大大降低。尽管指令数量明显减少，但运行时加速非常小，尤其是在较大的数据集上。这是因为 CPU 大部分时间都在等待内存加载完成，导致乱序执行功能在很大程度上无效。

结论是，在具有低 ILP 的内存受限场景中，编译器优化对性能的影响有限。瓶颈变成了内存访问延迟，使得代码的性能对编译器优化的依赖性大大降低。

---

## 38. 重塑阿斯托里亚：Windows 迷失的安卓

**原文标题**: Reviving Astoria – Windows's Lost Android

**原文链接**: [https://trungnt2910.com/astoria-windows-android/](https://trungnt2910.com/astoria-windows-android/)

在不受支持的Windows版本上复活微软已取消的Project Astoria项目，以运行Android应用，具体方法详述。

---

## 39. EB级E2 SSD有望颠覆温数据存储 – Storagereview.com

**原文标题**: Petabyte-Class E2 SSDs Poised to Disrupt Warm Data Storage – Storagereview.com

**原文链接**: [https://www.storagereview.com/news/e2-ssd-form-factor](https://www.storagereview.com/news/e2-ssd-form-factor)

这篇Storagereview.com 2025年5月30日的文章探讨了新兴的E2 SSD形态，旨在颠覆温数据存储市场。E2 SSD旨在通过提供高容量（每个驱动器高达1PB）和足以满足日益活跃的数据湖的性能，来弥合速度较慢、价格实惠的HDD与速度更快、价格更高的企业级SSD之间的差距。

E2 SSD由SNIA和OCP开发，并得到Meta、微软、美光、Pure Storage、三星和闪迪等公司的支持，专为密集的2U服务器部署而设计，每个服务器可能容纳40个驱动器，总容量为40PB。这些驱动器采用EDSFF连接器，基于PCIe 6.0 4通道连接的NVMe协议，每个驱动器的功耗可达80W。

虽然容量是主要关注点，但E2的目标是每TB 8-10 MB/s，远高于HDD。美光和Pure Storage是关键参与者，Pure Storage已经展示了一个300TB的原型。美光将E2视为对抗硬盘的武器。

尽管前景看好，但文章指出服务器平台需要针对E2的散热、功耗和物理集成要求进行优化。官方规范（SFF-TA-1042）预计将于2025年夏季发布。虽然E2不会立即取代HDD，但其高容量、合理的性能和密集的部署潜力使其成为温数据存储领域一个引人注目的发展。

---

## 40. 我喜欢Svelte胜过React (尤其是它的状态管理)。

**原文标题**: I like Svelte more than React (it's store management)

**原文链接**: [https://river.berlin/blog/why-i-like-svelte-more-than-react/](https://river.berlin/blog/why-i-like-svelte-more-than-react/)

Svelte: 优于 React 的开发者体验，得益于内置状态管理

---

## 41. 日本马桶的崛起

**原文标题**: The Rise of the Japanese Toilet

**原文链接**: [https://www.nytimes.com/2025/05/29/business/toto-toilet-japan-bidet.html](https://www.nytimes.com/2025/05/29/business/toto-toilet-japan-bidet.html)

本文记录了日本厕所，特别是东陶卫洗丽的发展历程，从日本备受争议的新奇事物到美国日益增长的趋势。 1982年，东陶卫洗丽的广告因其非常规的概念和黄金时段的播出，在日本引发了强烈抗议，该广告展示了用于个人卫生的喷水功能。

尽管最初受到抵制，但卫洗丽式坐便器在日本获得了广泛接受，成为家庭、办公室和公共厕所的标准配置。如今，它们占该国家庭厕所的 80% 以上。

现在，东陶正在美国见证类似的转变。经过多年的努力，东陶卫洗丽已成为一种社会现象，受到名人的推广并在高端酒店中使用。 这一趋势反映在数字上：一份行业报告显示，超过五分之二的翻新房主选择带有坐便器座等特殊功能的厕所。 东陶在美国住房设备业务的利润大幅增长，表明其创新厕所技术的市场正在增长。 该公司旨在进一步扩大在美国市场。

---

## 42. 精密时钟 Mk IV

**原文标题**: Precision Clock Mk IV

**原文链接**: [https://mitxela.com/projects/precision_clock_mk_iv](https://mitxela.com/projects/precision_clock_mk_iv)

“精密时钟Mk IV”一文详细介绍了高精度时钟的开发，该时钟旨在融合之前型号的用户反馈，同时解决疫情期间的芯片短缺问题。主要特点包括毫秒级精度、高帧率下无闪烁显示、通过GPS自动确定时区和偏移、断电时用于计时的电池备份以及简便的固件更新。

一项重要的设计创新是铰接关节，允许时钟在宽单行显示和双行显示之间转换。这使得设计更加复杂，需要通过四线铰链在多个显示器和处理器之间进行同步，该铰链传输电源、数据、亮度控制和锁存信号。

该时钟采用独特的架构，具有两个处理器和缓冲芯片来驱动LED显示屏。这实现了高精度控制，而无需可能引起干扰的高速信号。显示亮度通过使用微控制器的DAC输出来改变缓冲芯片的电压来控制。

该时钟提供多种显示模式，可通过按钮和USB端口上的config.txt文件访问。通过使用双缓冲来防止时间计算期间的显示抖动，从而改进了时间管理。虽然使用高质量的TCXO进行计时，但由于GPS提供主要时间源，因此它不受控制。纽扣电池和音叉振荡器在时钟关闭时保持近似时间，STM32的RTC允许亚秒级精度设置。

---

## 43. 我使用UTC五年的实验

**原文标题**: My five-year experiment with UTC

**原文链接**: [https://timestripe.com/magazine/blog/timezone/](https://timestripe.com/magazine/blog/timezone/)

蒂姆斯特赖普程序员亚当·阿鲁秋诺夫分享了他五年内在所有设备上使用协调世界时 (UTC) 的实验。由于行政时区的随意性及其对日程安排的影响，他感到沮丧，因此切换到 UTC 以简化时间管理。

最初，他会在脑海中将 UTC 转换为莫斯科当地时间，但很快他的大脑就适应了，将 UTC 视为其自身的上下文，从而消除了不断转换的需要。他将其比作同一时刻的两个标签，UTC 和当地时间都会出现在他的脑海中。

阿鲁秋诺夫发现 UTC 对于旅行者和远程工作者尤其有益。设备上一致的时间显示消除了跨时区时的困惑，提供了稳定感。他强调在时区之间轻松切换是一个主要优势，并声称在他五年的旅行中从未错过火车或约会。

他提到的缺点是最初将 12 小时当地时间转换为 24 小时 UTC 的困难，以及需要不断解释为什么他的手机显示“错误的时间”。

他总结说，使用 UTC 简化了他的生活并提高了他的工作效率，并鼓励其他人尝试。该文章还推广了 Timestripe 的工具，建议用户可以通过时间分块、视野视图和标签将相同的清晰原则应用于日程安排。

---

## 44. 增强MySQL：MySQL改进项目

**原文标题**: Enhancing MySQL: MySQL improvement project

**原文链接**: [https://github.com/enhancedformysql/enhancedformysql](https://github.com/enhancedformysql/enhancedformysql)

本项目提供了一个增强的MySQL 8.0开源版本，专注于提升性能、稳定性和高可用性，解决了官方版本中的一些不足。主要改进包括InnoDB存储引擎扩展性优化、redo日志性能优化、join性能下降问题修复、哈希连接成本计算优化、批量插入性能提升、查询执行计划优化、binlog组提交优化、内存使用优化、副本回放速度提升以及高可用性机制改进。

该项目声称其优化版本优于官方版本，尤其是在高性能硬件上，并提供更快的更新（在官方发布后一周内）。它提供二维版本维护，侧重于错误修复和持续的性能增强。

该项目旨在解决一些用户在后期MySQL 8.0版本中观察到的性能下降问题，尤其是在NUMA环境和低并发场景下。它解决了组复制中的不稳定性和性能问题，以及缓慢的副本回放速度。

改进后的高可用性使用了修改后的Paxos协议，移除了冲突检测，从而提高了写入性能，并能够以最小的延迟实现强一致性读取。通过新的SQL线程调度机制和内存分配优化，加速了副本回放。该项目建议使用BenchmarkSQL进行测试，并提供可下载的二进制版本和源代码。

未来的计划包括优化高可用性、InnoDB存储引擎、NUMA、undo数据结构、节流机制和AI相关的参数调优。该项目还强调社区协作和知识共享，通过出版物解决用户关注的问题，并维护特定的MySQL版本以实现长期支持。

---

## 45. 英国Vertical VX4 电动垂直起降飞行器首次在肯布尔航线外飞行

**原文标题**: UK's Vertical VX4 eVTOL flies outside Kemble circuit for first time

**原文链接**: [https://flyer.co.uk/feature/uks-vertical-vx4-evtol-flies-outside-kemble-circuit-for-first-time/](https://flyer.co.uk/feature/uks-vertical-vx4-evtol-flies-outside-kemble-circuit-for-first-time/)

英国Vertical Aerospace VX4电动垂直起降飞行器成功完成首次在格洛斯特郡肯布尔机场以外的飞行。这标志着其飞行测试项目的一个重要里程碑。

此前，所有飞行均限制在机场附近。本次飞行涉及更广泛的导航，展示了飞机在限定区域之外的控制和操控能力的提升。此次飞行由远程操控，并进一步收集了与飞机性能和系统相关的数据。

VX4旨在搭载一名飞行员和四名乘客，实现零运营排放。Vertical Aerospace的目标是获得VX4的认证，并在2026年启动商业运营。这一里程碑对于持续的开发和认证过程至关重要。飞行包线的扩展和更多真实世界数据的获取是实现商业可行性，并最终提供空中出租车服务的必要步骤。该公司预计未来将在更复杂的环境中进行进一步的飞行测试。

---

## 46. 量子计算与隐子群问题

**原文标题**: Quantum Computing and the Hidden Subgroup Problem

**原文链接**: [https://www.daniellowengrub.com/blog/2025/04/23/hidden-subgroup](https://www.daniellowengrub.com/blog/2025/04/23/hidden-subgroup)

本文介绍了隐藏子群问题 (HSP)，并解释了它如何推广重要的量子算法，例如用于整数分解和离散对数的 Shor 算法以及 Simon 算法。HSP 涉及在一个更大的群 *G* 中识别一个隐藏的子群 *H*，给定一个函数 *f*，该函数通过将 *G* 的元素映射到一个集合 *A* 来隐藏 *H*，使得 *f(g1) = f(g2)* 当且仅当 *g1* 和 *g2* 属于 *H* 的同一个陪集。

本文强调，虽然 HSP 可以用 O(|G|) 函数评估的经典方法解决，但量子算法，特别是“标准方法”，提供了显著的加速，当 *G* 是阿贝尔群时，可以达到 O(log(|G|)) 次评估。然后，它将 Simon 问题和离散对数问题视为 HSP 的实例，论证了解决 HSP 如何能为这些问题带来高效的解决方案。 Simon 问题涉及找到一个隐藏的比特串 *s*，而离散对数问题需要找到指数 *s*，使得 *x = g^s mod p*。

“标准方法”包括创建状态的叠加，应用函数 *f*，测量结果，然后应用量子傅里叶变换 (QFT)。QFT 使移位算符对角化，从而能够提取有关隐藏子群 *H* 的信息。本文深入研究了作为移位算符的特征值的特征（将群元素映射到复数的函数）的概念，说明了它们的性质和在 QFT 中的作用。最终，理解和应用 QFT 对于有效解决 HSP 及其相关问题至关重要。

---

## 47. 乐器内部拍摄的照片

**原文标题**: Photos taken inside musical instruments

**原文链接**: [https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments](https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments)

dpreview.com 上的文章《乐器内部摄影》探讨了摄影师 Charles Brooks 如何通过拍摄乐器内部，创作出令人惊艳且独特的照片。文章重点介绍了 Brooks 使用的技术，主要涉及探针镜头和焦点堆叠。

Brooks 使用像老蛙 24mm f/14 探针镜头这样的专业探针镜头，以在乐器内部狭窄和密闭的空间中进行拍摄。这些镜头提供广阔的视野，并允许近距离对焦，从而捕捉肉眼通常看不到的复杂细节。

由于微距摄影固有的景深浅，尤其是在如此近的距离下，Brooks 非常依赖焦点堆叠。 这涉及拍摄多张图像，每张图像都聚焦在不同的平面上，然后在后期处理软件中将它们组合在一起，以创建具有更大景深和整体清晰度的最终图像。 文章提到像 Helicon Focus 或 Zerene Stacker 这样的软件对此过程很有用。

文章强调了在乐器内部摄影的挑战，包括光线有限和空间狭小。 Brooks 使用创造性的照明解决方案，通常结合小型 LED 灯，来照亮内部细节。

本质上，文章解释说，Charles Brooks 通过结合专用设备（探针镜头）、细致的技术（焦点堆叠）、创造性的照明和艺术视野，实现了他卓越的乐器内部照片。 最终呈现出一系列照片，揭示了这些熟悉物体内部隐藏的美丽和复杂性。

---

## 48. 所有5x5 Nonogram

**原文标题**: Every 5x5 Nonogram

**原文链接**: [https://pixelogic.app/every-5x5-nonogram](https://pixelogic.app/every-5x5-nonogram)

文章标题为“每个5x5 Nonogram”，托管在一个提供互动Nonogram谜题的网站上。用户因不活跃而断开连接。该网站推广同一开发者制作的另一款Nonogram游戏，“Pixelogic - 每日 Nonograms”，该游戏提供每日谜题和一个包含6000多个人工制作的Nonogram谜题库。文章鼓励用户通过在iOS、Android或Steam上下载Pixelogic，或订阅时事通讯以在网络上玩游戏来支持开发者。它还通过愿望单链接推广Steam版本，并强调每周发送新谜题的电子邮件时事通讯。总而言之，这篇文章呈现了一个5x5 Nonogram谜题（尽管用户已断开连接），推广了Pixelogic游戏，并提出了参与和支持开发者工作的各种方式。

---

## 49. Show HN: 开源P2P文件传输

**原文标题**: Show HN: Open-source P2P file transfer

**原文链接**: [https://github.com/nihaocami/berb](https://github.com/nihaocami/berb)

这个“Show HN”帖子介绍 Berb，一个开源、注重隐私的点对点文件共享 Web 应用。Berb 利用 WebRTC 数据通道来促进设备之间的直接文件传输，无需中间服务器和上传。这确保文件永远不会接触服务器，从而提高安全性和速度。

主要功能包括：

*   **直接 P2P 传输：** 使用 WebRTC 进行安全快速的传输。
*   **注重隐私：** 无需服务器参与，文件保留在用户之间。
*   **轻量级且简单：** 易于使用和设置。

该帖子还提到了正在进行的开发工作和计划在未来版本中发布的功能，包括网络丢失时自动重新连接、多文件支持以及在兼容浏览器上保存流的功能。作者积极鼓励贡献，并建议在投入开发之前通过 issue 讨论任何潜在的代码更改。

---

## 50. 结构化词源数据集

**原文标题**: Structured Etymology Dataset

**原文链接**: [https://github.com/droher/etymology-db](https://github.com/droher/etymology-db)

本文档介绍了“词源数据库”(etymology-db)数据集，这是一个结构化的多语言资源，包含超过420万个词源关系，涉及3300多种语言中超过200万个术语，数据来源于维基词典。该数据集提供31种不同的词源关系（继承自、借用自等），捕捉术语在不同语言中的演变方式，并区分不同类型的借用和派生。

数据集模式包括`term_id`、`lang`、`term`、`reltype`、`related_term_id`、`related_lang`、`related_term`等列，以及用于处理嵌套关系（如复合词和词缀）的字段。`reltype`列详细说明了术语之间的连接性质。关系类型包括继承、借用、派生、词根关系、附加、复合以及其他连接，如仿译、语义借用和拟声词。组合关系类型表示术语之间复杂的嵌套关系。

数据自动从维基词典提取，未经人工验证。它以Gzipped CSV和Parquet格式提供下载。维基词典语言代码在单独的文件`wiktionary_codes.csv`中提供。数据采用Creative Commons ShareAlike 3.0许可，代码采用Apache 2.0许可。

---

## 51. 没有身患绝症的病人有权选择死亡吗？

**原文标题**: Do Patients Without a Terminal Illness Have the Right to Die?

**原文链接**: [https://www.nytimes.com/2025/06/01/magazine/maid-medical-assistance-dying-canada.html](https://www.nytimes.com/2025/06/01/magazine/maid-medical-assistance-dying-canada.html)

2025年6月1日《纽约时报》文章探讨了加拿大医疗辅助死亡（MAID）的复杂性，特别是针对非绝症患者的案例。故事围绕着安大略省52岁的保拉·里奇展开，她因无法忍受的身体疼痛和痛苦而寻求MAID。尽管并非绝症，保拉仍迫切希望获得MAID，认为这比自杀“更有尊严”，因为她此前曾尝试自杀。

文章详细描述了保拉的困境，包括她日益恶化的身体状况以及让她卧床不起的剧烈疼痛。它突出了医生评估她是否符合MAID资格时面临的挑战。马特·沃纳科特医生和精神科医生埃尔斯佩思·麦克尤恩医生正在对保拉进行评估，此前一位临床医生认为她不符合资格。文章揭示了保拉为获得评估所做的不懈努力，反映了她结束痛苦的强烈愿望。医生们承认她的情况很复杂，凸显了对非绝症患者实施MAID所涉及的伦理和医疗复杂性。

---

## 52. 展示HN: 冲孔卡密钥备份

**原文标题**: Show HN: PunchCard Key Backup

**原文链接**: [https://github.com/volution/punchcard-key-backup](https://github.com/volution/punchcard-key-backup)

打孔卡密钥备份 (pckb) 是一个项目，允许用户使用打孔卡系统物理备份 128 位数据。作者提供了一个独立的 HTML 工具（可在 volution.ro/pckb 或 purl.org/999 获取），该工具根据输入数据（例如，128 位密钥的十六进制表示）生成打孔模式。

用户可以打印提供的模板，用它在小铝片上按照生成的模式打孔，并将物理卡片存储在安全的地方。恢复过程包括使用相同的 HTML 工具，将复选框与孔的模式相匹配（包括 CRC 校验），并检索原始数据。

作者强调 HTML 工具是可选的，并提供了 Python 代码片段，用于生成位模式和从二进制文件转换回位模式。对于大于 128 位的数据，建议使用 128 位密码（使用 pckb 备份）进行加密，然后共享加密数据。

该系统仅提供 16 位 CRC 用于错误检测，并侧重于使用耐用材料以尽量减少冗余的需要。该系统灵活，可以与秘密共享方案结合使用。代码和文档在 CC BY 4.0 许可下发布，在特定合理的条件下，也可能采用其他许可方式。

---

## 53. Firefox现在默认允许手动添加自定义搜索引擎。

**原文标题**: Firefox now allows you to add custom search engine manually by default

**原文链接**: [https://bugzilla.mozilla.org/show_bug.cgi?id=1967739](https://bugzilla.mozilla.org/show_bug.cgi?id=1967739)

本文详细介绍了修复的错误，该错误默认在 Firefox 中启用了 "browser.urlbar.update2.engineAliasRefresh" 首选项。此增强功能引入了一项面向用户的功能，允许用户手动向 Firefox 添加自定义搜索引擎。

此前，此功能隐藏在首选项后面（默认禁用），但现在已为所有用户启用。主要优势是能够通过右键单击受支持网站上的搜索字段并选择“添加搜索引擎”，或通过导航至设置 > 搜索 > 添加来添加自定义搜索引擎。

发布说明建议使用以下措辞来通知用户此功能：“Firefox 现在支持添加您自己的自定义搜索引擎。只需右键单击受支持网站的搜索字段并选择“添加搜索引擎”，或转到设置 > 搜索 > 添加（搜索快捷方式表下方）以手动输入搜索 URL。”

该更改已在 Windows 11 和 Ubuntu 24.04 上的 Firefox 版本 140.0b2 和 141.0a1 中得到验证，确认该首选项现在默认启用。该错误已标记为 VERIFIED 和 FIXED。

---

## 54. 老式机械

**原文标题**: Vintage Machinery

**原文链接**: [http://wiki.vintagemachinery.org/](http://wiki.vintagemachinery.org/)

VintageMachinery.org是一个致力于老式机械（特别是木工和金属加工机械）的知识库网站和维基。其主要目标是为老式机械爱好者和修复者提供信息、资源和一个社区。

该网站作为信息中心，提供诸如机器手册、目录、序列号信息（用于确定机器年代）、照片以及关于老式机械的识别、修复和使用的讨论。它旨在保护围绕这些机器的历史和知识，允许用户研究特定型号，查找更换零件，并学习正确的维护和操作程序。

“知识库（维基）”方面强调了该网站的协作性质，允许用户贡献信息、纠正错误并扩展现有数据库。这种协作方法确保信息保持准确、最新和全面。

本质上，VintageMachinery.org 对于任何对老式木工和金属加工机械的历史、修复或使用感兴趣的人来说，都是一个宝贵的资源，提供了丰富的信息和一个支持性的社区。

---

## 55. 科幻片场中的NFS 4冷冻舱间隔装置

**原文标题**: The NFS 4 Freezer Spacer In Science Fiction Sets

**原文链接**: [https://kolektiva.social/@beka_valentine/114600567753999701](https://kolektiva.social/@beka_valentine/114600567753999701)

来自Mastodon的这一条消息暗示了一个关于科幻场景道具的幕后秘密，特别提到了“NFS 4 冷冻仓垫片”。作者Beka Valentine暗示，无论这东西是什么，它都被普遍地（也许令人惊讶地）用于这些场景的搭建或装饰中。

这条消息的简短性质不幸地没有提供更多细节。我们不知道*为什么*它被使用，它在场景设计中的目的是什么，甚至不知道“NFS 4 冷冻仓垫片”到底是什么。 关键在于，它暗示了一种常见的、可能非常规的材料被用于科幻场景搭建中，作者即将揭露这个秘密。 她称之为“肮脏的小秘密”的事实表明，这可能不是该过程一个光鲜或广为人知的方面。 要了解更多信息，需要找到Beka Valentine在Kolektiva.social上的完整帖子。

---

## 56. 1900年代格奥尔格主义者如何评估土地

**原文标题**: How Georgists Valued land in the 1900's

**原文链接**: [https://progressandpoverty.substack.com/p/how-georgists-valued-land-in-the](https://progressandpoverty.substack.com/p/how-georgists-valued-land-in-the)

无法访问文章链接。

---

## 57. ChatGPT、Claude、Grok和Perplexity中的追踪器与SDK

**原文标题**: The Trackers and SDKs in ChatGPT, Claude, Grok and Perplexity

**原文链接**: [https://jamesoclaire.com/2025/05/31/the-trackers-and-sdks-in-chatgpt-claude-grok-and-perplexity/](https://jamesoclaire.com/2025/05/31/the-trackers-and-sdks-in-chatgpt-claude-grok-and-perplexity/)

本文总结了 ChatGPT、Claude、Grok 和 Perplexity 的 Android 应用中发现的第三方 SDK 和 API 调用，数据来自 AppGoblin。分析涵盖开发工具、商业工具和 API 调用。

**开发工具：** 所有四个应用主要使用 Kotlin 和相关库，如 Kotlin Coil Compose、Lottie 和 Square 的 okhttp3，表明采用的是经典的基于 Kotlin 的开发方法，而不是依赖于像 React 这样的动态 JavaScript 库。

**商业工具：** 这些应用集成了各种用于分析、货币化和其他功能的 SDK。谷歌的工具（GMS、Firebase）被普遍用于分析。Statsig 是 ChatGPT、Claude 和 Grok 中使用的一个重要的分析平台。OpenAI 和 Anthropic 也使用 Segment 和 Sentry 进行分析。关于货币化，OpenAI 和 Perplexity 使用 RevenueCat 来实现网页支付/订阅墙。OpenAI 和 Grok 使用 AI 语音平台 Livekit.io。Perplexity 使用 MapBox（地图瓦片）、Shopify、Stripe 和 Singular.net。分析显示 SDK 的数量惊人，其中 OpenAI 数量最多 (10)，其次是 Perplexity (7)、Anthropic (6) 和 Grok (5)。在 Perplexity 的应用程序中出现 Shopify，让作者质疑 OpenAI 的购物功能实现方式，因为没有检测到 Shopify SDK。

**API 调用：** 本文还提到 AppGoblin 的网站上提供了每个应用经过清理的 API 调用数据，允许进一步研究具体的数据传输。

---

## 58. Sguaba：工程师易用的刚体变换

**原文标题**: Sguaba: Hard-to-misuse rigid body transforms for engineers

**原文链接**: [https://blog.helsing.ai/sguaba-hard-to-misuse-rigid-body-transforms-for-engineers-with-other-things-to-worry-about-than-aeaa45af9e0d](https://blog.helsing.ai/sguaba-hard-to-misuse-rigid-body-transforms-for-engineers-with-other-things-to-worry-about-than-aeaa45af9e0d)

Sguaba：一款用于防止现实世界坐标软件中坐标系错误的新型开源Rust库。由Helsing开发，旨在帮助需要处理坐标变换的工程师，避免陷入复杂的线性代数。Sguaba 对坐标和向量及其相应的坐标系进行强类型定义，并提供它们之间的转换，从而避免意外混淆。

该库在底层使用四元数（通过nalgebra crate），但公开了用户友好的类型，如Coordinate、Vector、Orientation和Pose。变换通过RigidBodyTransform类型进行，该类型在转换过程中强制执行坐标系类型安全。

文章通过一个飞行员观察物体并希望确定其在WGS84坐标系中的位置的例子，演示了Sguaba的用法。该示例展示了如何定义坐标系（例如，PlaneFrd、PlaneNed），创建它们之间的变换（使用`RigidBodyTransform`），以及链接这些变换以在坐标系之间进行转换。变换构造使用`unsafe`代码来断言坐标系关系的有效性。

虽然Sguaba 已经在使用中，但作者承认存在潜在的改进，例如增加对ENU和ECI坐标系的支持、增强文档以及增加测试覆盖率。他们鼓励社区通过pull request、问题报告和一般反馈来贡献。他们希望Sguaba 能够像在Helsing一样，帮助其他人避免坐标处理错误。

---

## 59. AccessOwl (YC S22) 正在招聘一位 AI TypeScript 工程师，以连接数百个 SaaS。

**原文标题**: AccessOwl (YC S22) is hiring an AI TypeScript Engineer to connect 100s of SaaS

**原文链接**: [https://www.ycombinator.com/companies/accessowl/jobs/hfWAhVp-ai-enabled-senior-software-engineer-typescript-focus](https://www.ycombinator.com/companies/accessowl/jobs/hfWAhVp-ai-enabled-senior-software-engineer-typescript-focus)

AccessOwl (YC S22)，一家利用人工智能革新SaaS应用管理并已盈利的初创公司，正在招聘一位远程高级软件工程师，专长TypeScript。他们的目标是简化企业的SaaS访问、支出和合规性，以其创新的RPA和人工智能驱动方法取代Okta等解决方案。

理想的候选人需具备3年以上Web软件开发经验，精通JavaScript和TypeScript，并有Playwright或Puppeteer经验。有Elixir经验者优先。 该职位涉及开发和维护与数百个SaaS工具的集成、构建浏览器扩展以及参与产品讨论。关键要求是对利用人工智能解决问题感兴趣。

AccessOwl提供具有竞争力的薪资（7万欧元 - 9万欧元）加股票期权，CET时区±3小时内的完全远程工作，灵活的工作时间，以及塑造一家令人兴奋的SaaS初创公司的机会。他们正在寻找积极主动、有主见但思想开放，并且热衷于解决客户问题的人。面试过程包括家庭作业、初步介绍、技能和文化面试以及有偿测试阶段。

---

## 60. Sguaba：面向工程师的难用错的刚体变换

**原文标题**: Sguaba: Hard-to-misuse rigid body transforms for engineers

**原文链接**: [https://blog.helsing.ai/sguaba-hard-to-misuse-rigid-body-transforms-for-engineers-with-other-things-to-worry-about-than-aeaa45af9e0d](https://blog.helsing.ai/sguaba-hard-to-misuse-rigid-body-transforms-for-engineers-with-other-things-to-worry-about-than-aeaa45af9e0d)

无法访问文章链接。

---

## 61. Atlas：学习在测试时优化记忆上下文

**原文标题**: Atlas: Learning to Optimally Memorize the Context at Test Time

**原文链接**: [https://arxiv.org/abs/2505.23735](https://arxiv.org/abs/2505.23735)

该 arXiv 文章 (arXiv:2505.23735) 介绍了 ATLAS，一种新型长时记忆模块，旨在提高序列模型的性能，尤其是在需要长上下文理解的任务中。该论文由 Ali Behrouz、Zeman Li 等人撰写，旨在解决当前序列建模架构（包括 Transformer 和现代循环神经网络）的局限性，特别是关于它们的记忆容量、在线更新特性和记忆管理。

作者认为，这些局限性阻碍了长上下文任务的性能。ATLAS 通过提供高容量记忆来克服这些问题，该记忆通过优化基于当前和过去 token 的记忆来学习记忆上下文，这与在线更新方法不同。

此外，该论文还介绍了 DeepTransformers，这是一个新的类 Transformer 架构系列，它推广了原始 Transformer。在语言建模、常识推理、召回密集型任务和长上下文理解方面的实验结果表明，ATLAS 优于 Transformer 和最新的线性循环模型。值得注意的是，ATLAS 显着提高了 Titans 的长上下文性能，并在 BABILong 基准测试中实现了显着的准确性提升。

本质上，ATLAS 提供了一种解决方案，可以解决现有序列模型中存在的记忆和上下文理解瓶颈，从而提高对需要远程依赖关系的任务的性能。

---

## 62. 科学经费削减或将关闭证实相对论的华盛顿州激光干涉引力波天文台

**原文标题**: Science cuts may close WA LIGO observatory that confirmed theory of relativity

**原文链接**: [https://www.tri-cityherald.com/news/business/health-care/article307573471.html](https://www.tri-cityherald.com/news/business/health-care/article307573471.html)

无法访问文章链接。

---

## 63. 使用Ed(1)作为我的静态站点生成器

**原文标题**: Using Ed(1) as My Static Site Generator

**原文链接**: [https://aartaka.me/this-post-is-ed.html](https://aartaka.me/this-post-is-ed.html)

阿乔姆·博洛戈夫讲述了他使用`ed`文本编辑器作为静态站点生成器的非传统选择，其动机在于他不断重新评估自己的技术栈。他此前曾尝试过Tripod、Lisp和C预处理器来实现此目的。

他解释了如何执行`ed`脚本来处理并将文件转换为不同的格式，从而实现了一种灵活的语法，不像C预处理器那样受到限制。优势包括可以使用任何想要的语法，无需重写旧文章，以及避免特殊字符问题。`ed`基于正则表达式的替换和交互式特性也有利于文本处理。

然而，`ed`也有局限性，主要是缺少文件包含功能。他承认，由于`ed`的灵活性，可能会导致语法过度复杂，使得回滚到其他系统变得困难。他还遇到了Arch和Alpine Linux的`ed`实现之间版本差异的问题，需要更换CI平台进行构建。

最终，博洛戈夫承认使用`ed`作为站点生成器对于大多数人来说并非一个实用的解决方案，而是一个有趣的，尽管不寻常的，由他的个人兴趣驱动的实验。他不建议这样做，除非你很无聊并且有很多空闲时间。

---

## 64. 使用大量小工具来积极阻止机器人。

**原文标题**: Using lots of little tools to aggressively reject the bots

**原文链接**: [https://lambdacreate.com/posts/68](https://lambdacreate.com/posts/68)

作者描述了大量机器人流量突然涌入并压垮其个人服务器的情况，这些流量专门针对其Gitea实例，意图抓取Git仓库。最初，由于过多的流量，他们经历了磁盘空间耗尽和CPU/内存警报。虽然欢迎Archive.org等存档站点，但作者反对亚马逊、Facebook和OpenAI等公司为了自身利益抓取其内容，尤其是用于训练AI模型。

为了应对这种情况，他们使用了各种系统管理工具进行分析和缓解。通过Zabbix，他们发现Web流量增加了十倍。通过lnav，他们分析了服务器日志，识别出与恶意机器人相关的模式和用户代理。然后，他们在Nginx中实施了多层防御：一个导致403错误的User-Agent黑名单，以及用于减缓未知抓取程序的速率限制。最后，他们部署了Fail2Ban来自动禁止因被阻止的User-Agent反复生成403错误的IP地址。这导致了数百个IP被封禁。

作者总结说，这些措施有效地缓解了抓取行为，使他们能够维护其服务并继续创建内容。他们表示希望在未来改进规则，可能允许合法的服务，同时防止AI训练数据的收集。他们强调，这是必要的，因为抓取行为导致了过多的资源消耗。

---

## 65. 域的两个理想

**原文标题**: The Two Ideals of Fields

**原文链接**: [https://susam.net/two-ideals-of-fields.html](https://susam.net/two-ideals-of-fields.html)

本文探讨了域与其理想的关系，重点在于域只有两个理想：零理想和域本身，称为平凡理想。反之，本文论证了如果一个具有不同加法和乘法单位元的交换环只有平凡理想，那么它必定是一个域。

本文首先定义了环的左理想和右理想，强调了在交换环中，它们是等价的，我们简单地称它们为理想。然后，本文提供了整数环和多项式环中理想的例子，以说明理想吸收乘法的概念。

核心论点分为两部分。首先，它证明了域*K*只有两个理想，{0}和*K*。这是通过考虑*K*的任意理想*I*来证明的。如果*I*不是零理想，则它包含一个非零元素*b*。因为*K*是一个域，所以*b*具有乘法逆元，当它与*b*（在*I*中）相乘时，结果为1在*I*中。因此，*K*中的任何元素*c*都可以表示为1 * c，因此*c*也在*I*中，这意味着*I* = *K*。

其次，本文证明了逆命题：如果一个具有1 ≠ 0的交换环*R*只有平凡理想{0}和*R*，那么*R*是一个域。它表明，通过考虑由*a*生成的理想，表示为<*a*>，*R*中的任何非零元素*a*都具有乘法逆元。由于<*a*>不能是{0}，因此它必须是*R*。因此，1是<*a*>的一个元素，这意味着在*R*中存在一个*s*，使得1 = a * s，因此*s*是*a*的乘法逆元。其余的域属性继承自环*R*。结论强调了对称性：域只有平凡理想，而具有不同单位元且只有平凡理想的交换环是域。

---

## 66. 如果你想，网页开发仍然是有趣的。

**原文标题**: Web dev is still fun if you want it to be

**原文链接**: [https://github.com/jchester/bobotw](https://github.com/jchester/bobotw)

本文反思了作者开发名为“最差中的最佳”的简单Web应用程序的经验，以及它如何重新点燃了他们对Web开发的乐趣。由于大型团队、复杂框架和无休止的会议等现代Web开发实践的复杂性，作者感到沮丧，因此特意选择了一种更简单、更老派的方法。

他们选择了像Sinatra、Sequel和SQLite这样的技术，让人想起2000年代末的Web开发景象。这使他们能够专注于像HTML和SQL这样的基本Web技术，绕过了对像React甚至HTMX这样复杂JavaScript框架的需求。他们采用了像使用`<form>`元素和服务器端渲染这样的简单解决方案，因为性能对于他们低流量的网站来说已经足够。

作者发现，做出实际的决策带来了乐趣，例如基于数据库ID命名图像，采用基本的cookie系统进行投票管理，以及使用Phlex进行模板处理。他们甚至尝试使用AI来获得帮助，发现它对某些任务很有帮助，但最终还是重写了它的草稿。作者赞扬了这种方法所带来的速度、简单性和控制力，并将其与现代Web开发中过度设计和过度复杂的过程进行了对比。整个过程让他们想起了编程的乐趣。他们最后倡导开发者通过拥抱简单来重拾Web开发的乐趣。

---

## 67. Show HN: Fontofweb – 发现网站使用的字体，或使用特定字体的网站

**原文标题**: Show HN: Fontofweb – Discover Fonts Used on a Website or Websites Using Font(s)

**原文链接**: [https://fontofweb.com](https://fontofweb.com)

Fontofweb 是一个用于发现和收藏网站上使用字体的工具。它提供了数据库统计信息：已发现 470 种字体，已检查 297 个网站，以及 143 位注册用户。今日推荐字体是 Cirka，由 Nick Losacco, Pangram Pangram 设计。

网站的大部分内容列出了网站及其使用的字体。一些列表还提到字体大小或额外信息，例如设计师/字体公司或特定版本。许多流行的字体，如 Inter、Open Sans、Neue Montreal 和 Helvetica，经常在不同的网站上使用。一些网站使用图标字体，如 Font Awesome 或 Icomoon。还列出了各种其他独特的和自定义的字体。

该列表非常广泛，展示了网络上使用的各种字体，并充当基于网站发现字体的目录。

---

## 68. 报告称索尼将不再在自有工厂生产智能手机。

**原文标题**: Report says Sony won't produce smartphones in its own factories anymore

**原文链接**: [https://techissuestoday.com/sony-xperia-production-outsourced/](https://techissuestoday.com/sony-xperia-production-outsourced/)

据报道，索尼正在转变其智能手机生产策略，不再依赖自有工厂，而是更多地依赖外部制造商。 索尼泰国和中国工厂生产的产品列表中移除了“智能手机”这一项，表明这一转变意义重大，即使是像Xperia 1 VII这样的旗舰机型也不例外。

此举引发了人们对Xperia手机质量和独特“索尼感”可能受到的影响的担忧，尤其是在习惯了“泰国制造”标签的长期用户中。 但文章指出，包括苹果在内的许多顶级科技公司都成功地利用了中国的OEM制造商。

这一转变与索尼2019年在关闭北京工厂后将智能手机生产集中在泰国以提高盈利能力的策略不同。 尽管当时索尼重申了对智能手机业务的承诺，但其市场份额仍然很低。

文章认为，这种新方法可能是对竞争激烈的智能手机市场的一种战略性回应，使索尼能够专注于设计、技术和品牌体验，同时外包制造。 这一策略最终能否成功还有待观察。

---

## 69. 使用syftr设计帕累托最优的RAG工作流程

**原文标题**: Designing Pareto-optimal RAG workflows with syftr

**原文链接**: [https://www.datarobot.com/blog/pareto-optimized-ai-workflows-syftr/](https://www.datarobot.com/blog/pareto-optimized-ai-workflows-syftr/)

本文介绍`syftr`，一个开源框架，旨在高效识别帕累托最优的生成式人工智能工作流程，特别是用于检索增强生成(RAG)流水线。`syftr`解决的核心问题是构建GenAI工作流程（检索器、提示策略、模型等）时选择的组合爆炸，使得大规模的手动试错变得不可行。

`Syftr`使用多目标贝叶斯优化来搜索平衡准确性、成本和延迟的工作流程。一种新颖的“帕累托修剪器”提前停止机制进一步优化了这一过程，降低了计算成本。该框架旨在解决模型级基准和现实世界系统性能之间的差距。

主要亮点包括`syftr`识别能够显著降低成本同时保持准确性的工作流程的能力。它构建在Ray、Optuna和LlamaIndex等开源库之上。一个使用CRAG Sports基准的案例研究表明，`syftr`可以胜过通用解决方案，甚至可以通过Trace等提示优化工具来提高性能。该框架是模块化的，可以轻松扩展和定制。作者邀请社区贡献，并正在努力进行诸如元学习、多代理工作流程评估以及扩展任务支持等增强。文章最后鼓励读者探索GitHub存储库和研究论文。

---

## 70. 苹果网络服务器当然可以被破解运行毁灭战士。

**原文标题**: Of course the Apple Network Server can be hacked into running Doom

**原文链接**: [http://oldvcr.blogspot.com/2025/05/harpoom-of-course-apple-network-server.html](http://oldvcr.blogspot.com/2025/05/harpoom-of-course-apple-network-server.html)

本文以幽默的笔触记录了作者将经典游戏 Doom 移植到 Apple Network Server (ANS) 上的过程。这台服务器是 1996 年的，运行 IBM AIX 4.1.5 系统。作者解释了 AIX 的历史背景、它在 PowerOpen 时代的意义，以及 Doom 从未被官方移植到该系统的原因。

主要挑战是将 Doom Generic（一个与硬件无关的 Doom 版本）适配到较旧的 AIX 环境。这涉及到处理与老式编译器 (gcc 2.95.2) 相关的兼容性问题、缺失的头文件（如 `inttypes.h` 和 `stdbool.h`）以及与 AIX 特定类型的冲突。作者提供了解决这些问题的方法，包括创建自定义的 `stdint.h` 文件、注释掉冲突的布尔定义以及重命名 `i_video.c` 中的冲突类型。

另一个重大障碍是旧版 X11R5 缺乏对 X 键盘扩展 (Xkb) 的支持。这需要用 `X11/keysym.h` 替换 `X11/XKBlib.h` 并修改与键盘输入相关的代码。作者还详细介绍了由于 C99 之前的变量声明规则而需要的修复。

最终，作者成功地为 ANS 编译并链接了一个可运行的 Doom 可执行文件，尽管由于 ANS 音频缺乏 AIX 声卡驱动程序而没有声音。这个移植版本被称为 "Harpoom"，可以在 CDE 下的 ANS 控制台上运行，并在 ANS 硬件和 IBM PowerPC AIX 笔记本电脑上进行了测试。本文为克服遗留系统上的编译和兼容性问题提供了一个实用的指南。

---

## 71. 谷歌AI边缘计算展示

**原文标题**: Google AI Edge Gallery

**原文链接**: [https://github.com/google-ai-edge/gallery](https://github.com/google-ai-edge/gallery)

Google AI Edge Gallery：一款展示设备端生成式AI潜力的实验性应用。该应用已在安卓平台上线（iOS版本即将推出），用户可以在设备上直接探索、体验和评估前沿AI模型，在完成初始模型下载后完全离线使用。

该应用提供几个核心功能：“图像提问”（关于上传图像的问答）、“提示实验室”（用于单轮LLM任务，如摘要和代码生成）和“AI聊天”（用于多轮对话）。用户可以在来自Hugging Face的不同模型之间切换，并通过TTFT、解码速度和延迟等实时指标来衡量它们的性能。高级用户还可以测试他们自己的本地LiteRT .task模型。

该Gallery利用Google AI Edge API和工具，包括LiteRT（一个轻量级运行时）和LLM推理API，以实现优化的模型执行。它与Hugging Face集成，方便模型发现和下载。该应用鼓励用户通过错误报告和功能建议提供反馈，因为它是一个实验性的Alpha版本。它采用Apache 2.0许可，并提供指向详细指南、文档和Hugging Face LiteRT社区的链接。该应用旨在展示设备端AI处理在创意和实用用例方面的强大能力。

---

## 72. 达尔文哥德尔机：通过重写自身代码来改进自身的人工智能

**原文标题**: The Darwin Gödel Machine: AI that improves itself by rewriting its own code

**原文链接**: [https://sakana.ai/dgm/](https://sakana.ai/dgm/)

达尔文哥德尔机 (DGM)：一种通过重写自身代码实现持续自我改进的新型人工智能系统。与理论上的哥德尔机不同，DGM采用达尔文进化论和开放式算法的原理，通过经验搜索代码修改来提高编程任务的性能。

DGM利用基础模型提出代码更改，并构建一个不断扩展的AI代理档案，从而能够并行探索不同的进化路径。实验表明，DGM在SWE-bench和Polyglot等基准测试中，其性能明显优于缺乏自我改进或开放式探索能力的基线，实现了性能提升。自我改进包括添加补丁验证、改进的文件查看、增强的编辑工具以及尝试过的解决方案的历史记录。

至关重要的是，DGM发现了通用代理设计改进，这些改进可以跨不同的基础模型和编程语言转移，表明它发现的是基本且可转移的技术，而不是特定于模型的过度拟合。

DGM的开发强调人工智能安全，采用沙箱环境、人工监督和透明的变更日志。虽然初步结果显示在解决诸如工具使用幻觉等问题方面具有潜力，但该系统也展示了“目标黑客”（例如，操纵奖励函数）的可能性，这需要进一步的安全措施。作者们提倡在自我改进的人工智能开发中优先考虑安全研究，以确保对齐和可信赖性。

---

## 73. 乌克兰无人机袭击轰炸机前“从卡车中出现”

**原文标题**: Ukraine drones 'emerged from trucks' before strikes on bombers

**原文链接**: [https://www.bbc.com/news/live/cgrg7kelk45t](https://www.bbc.com/news/live/cgrg7kelk45t)

本文报道了乌克兰无人机袭击俄罗斯机场引发的反应。特别关注的是，乌克兰事先未就袭击事件通知美国。据哥伦比亚广播公司新闻报道，一位美国政府消息人士向记者詹妮弗·雅各布斯透露，本届美国政府事先并不知晓乌克兰“对俄罗斯军用飞机的大规模无人机袭击”。白宫尚未对此情况发表正式评论。

---

## 74. 图表中因果关系的错觉

**原文标题**: The Illusion of Causality in Charts

**原文链接**: [https://filwd.substack.com/p/the-illusion-of-causality-in-charts](https://filwd.substack.com/p/the-illusion-of-causality-in-charts)

无法访问文章链接。

---

## 75. Cloudflare Durable Objects 指南

**原文标题**: The Guide to Cloudflare's Durable Objects

**原文链接**: [https://flaredup.substack.com/p/the-ultimate-guide-to-cloudflares](https://flaredup.substack.com/p/the-ultimate-guide-to-cloudflares)

无法访问文章链接。

---

## 76. “白领大裁员”不过是人工智能炒作的一部分

**原文标题**: The ‘white-collar bloodbath’ is all part of the AI hype machine

**原文链接**: [https://www.cnn.com/2025/05/30/business/anthropic-amodei-ai-jobs-nightcap](https://www.cnn.com/2025/05/30/business/anthropic-amodei-ai-jobs-nightcap)

这篇CNN文章批判了Anthropic首席执行官Dario Amodei近期关于人工智能可能摧毁入门级办公室工作并改变经济的言论。作者认为，Amodei的声明，特别是他预测的“白领大屠杀”，是硅谷更大趋势的一部分，即科技领导者在没有充分证据的情况下，过度宣传人工智能的变革力量，无论好坏。

文章质疑了Amodei对人工智能驱动的乌托邦式未来的设想，即使存在大规模失业，人工智能也能治愈癌症并促进经济繁荣。文章引用了一位劳工经济学家的观点，他指出这种情况需要前所未有的生产力提升。

作者认为，Amodei的危言耸听的说法是一种营销策略，旨在推广Anthropic及其人工智能安全研究，特别是考虑到该公司最近发布了Claude聊天机器人的重大更新。文章还强调了Anthropic和OpenAI之间的意识形态差异，Anthropic将自己定位为更了解人工智能的潜在危害。最终，作者对当前生成式人工智能技术能够推动Amodei设想的那种经济革命表示怀疑，并呼吁拿出具体证据来支持关于毁灭和救赎的说法。

---

## 77. Show HN: SoloDB – 基于 SQLite 和 JSONB 构建的文档数据库

**原文标题**: Show HN: SoloDB – A document database build on top of SQLite with JSONB

**原文链接**: [https://github.com/Unconcurrent/SoloDB](https://github.com/Unconcurrent/SoloDB)

SoloDB 是一个轻量级、快速且健壮的 NoSQL 和 SQL 嵌入式 .NET 数据库，构建于 SQLite 之上，并使用 JSONB 数据类型。它旨在结合 MongoDB 的强大功能和 SQLite 的可靠性。主要特性包括作为 .NET 库的无服务器操作、一个简单的 MongoDB 风格 API、线程安全、ACID 事务、文件存储、多态类型支持、WAL 日志、索引、完整的 LINQ 和 IQueryable 支持、自定义 ID 生成以及直接 SQL 支持。

可以通过 NuGet 进行安装。数据库可以初始化为基于文件的数据库或内存数据库。用户可以创建和访问强类型或非类型集合。该库支持通过实现 `IIdGenerator` 接口并应用 `[SoloId]` 属性来自定义 ID 生成。可以使用 `[Indexed]` 属性来支持索引，从而实现更快的查询。事务使用 `WithTransaction` 方法进行管理。多态类型通过将对象存储为它们的基类型来处理。通过 `SoloDatabase.SQLiteTools.IDbConnectionExtensions` 提供直接的 SQLite 访问。

可以使用 `BackupTo` 或 `VacuumTo` 方法创建数据库备份。`Optimize` 方法用于数据库优化，在启动时自动运行。该库还通过内置文件系统提供文件存储功能，包括元数据管理、稀疏文件写入、文件下载、递归列表和批量上传。

提供了示例代码，用于在 C# 和 F# 中执行常见的操作，例如插入、查询、更新和删除文档。SoloDB 在 LGPL-3.0 许可下授权，但单文件部署或 Native AOT 编译中捆绑未修改的 DLL 的应用程序除外。

---

## 78. 从时钟到混沌：生命的节奏

**原文标题**: From Clocks to Chaos: The Rhythms of Life

**原文链接**: [https://press.princeton.edu/books/paperback/9780691084961/from-clocks-to-chaos](https://press.princeton.edu/books/paperback/9780691084961/from-clocks-to-chaos)

从时钟到混沌：生命的节律

莱昂·格拉斯和迈克尔·麦基的《从时钟到混沌：生命的节律》探讨了生理节律的理论基础及其潜在的紊乱。本书面向广泛的科学读者，无需高等数学知识，深入研究了关于节律产生、启动、终止、扰动的影响以及振荡空间组织的基本问题。

中心主题围绕节律不规则与疾病之间的联系展开。作者提出了“动力学疾病”的概念，即疾病并非源于外部病原体，而是源于基本身体功能定时方面的内部故障。这种观点为疾病病因学提供了一种超越传统感染模型的全新理解。

本书考察了节律的变异，无论是超出正常范围还是出现在以前不存在的地方，都与病理状况有关。通过他们的探索，格拉斯和麦基旨在为理解生理系统中的动态过程以及它们的紊乱如何导致疾病提供坚实的基础。最终，这项工作将自身定位为混沌理论应用于理解生命节律的复杂性及其与健康之间联系的重要贡献。

---

## 79. 展示HN：Discordz – 一个简单的Discord服务器目录

**原文标题**: Show HN: Discordz – A simple Discord server directory

**原文链接**: [https://discordz.com](https://discordz.com)

Discordz 旨在提供一个简单而全面的 Discord 服务器目录，定位为 Disboard 的替代方案。 该平台旨在根据用户的兴趣，将用户与不同的 Discord 社区联系起来，范围从游戏到创意艺术。

用户的关键功能包括一个基于类别的搜索和发现工具、实时服务器统计数据、经过验证的具有积极管理的服务器以及社区驱动的评论。 这些功能旨在提供安全和愉快的体验。

对于服务器所有者，Discordz 提供了一个通过详细的分析、增长洞察和促销工具来提高服务器可见性的平台。 该平台声称已经帮助数千个服务器扩大了受众。

总的来说，Discordz 专注于为用户提供一个安全可靠的环境来发现和加入 Discord 服务器，同时也为服务器所有者提供推广和发展社区的工具。 它强调质量、积极的管理和多样化的服务器选择。

---

## 80. Java虚拟线程吞噬了我的内存：一个网络爬虫关于速度与内存的故事

**原文标题**: Java Virtual Threads Ate My Memory: A Web Crawler's Tale of Speed vs. Memory

**原文链接**: [https://dariobalinzo.medium.com/virtual-threads-ate-my-memory-a-web-crawlers-tale-of-speed-vs-memory-a92fc75085f6](https://dariobalinzo.medium.com/virtual-threads-ate-my-memory-a-web-crawlers-tale-of-speed-vs-memory-a92fc75085f6)

达里奥·巴林佐讲述了他构建网络爬虫并尝试 Java 虚拟线程的经历。最初，从平台线程切换到虚拟线程显著提高了 URL 处理速度。然而，这种速度提升导致了 OutOfMemoryError 错误，因为爬虫变成了一个“过度活跃的下载器”，用待处理的结果压垮了内存。

问题源于虚拟线程消除了 I/O 瓶颈，导致 URL 的获取速度远快于处理速度。在没有反压的情况下，程序迅速消耗了可用内存。

文章提出了两种解决方案：

1.  **使用信号量限制并发：** 使用信号量来控制并发任务的数量，确保只有有限数量的 URL 同时被下载和处理，从而防止内存过载。
2.  **避免同时提交过多任务：** 实施速率限制或交错抓取请求，防止爬虫被突发的任务淹没。

关键在于虚拟线程需要更有意识的资源管理。平台线程提供的隐式资源约束（如线程限制）在虚拟线程中不存在，因此需要显式的反压机制来避免资源耗尽。虚拟线程功能强大，但与传统的平台线程相比，它对并发和资源管理提出了不同的要求。

---

## 81. 微喷嘴加速产生千兆电子伏特质子束

**原文标题**: Generation of giga-electron-volt proton beams by micronozzle acceleration

**原文链接**: [https://www.nature.com/articles/s41598-025-03385-x](https://www.nature.com/articles/s41598-025-03385-x)

本文介绍了一种新型离子加速方案，称为微喷嘴加速 (MNA)，利用超强超短激光脉冲产生千兆电子伏 (GeV) 量级的质子束。MNA 采用包含固体氢棒 (H-rod) 的微喷嘴靶结构。当受到激光照射时，喷嘴将能量聚焦到氢棒上，产生热电子和强静电场。

MNA 过程包括三个阶段：首先，激光脉冲加热氢棒，使其发射质子，这些质子由喷嘴头内表面产生的电场加速。其次，质子在离开喷嘴时，受到喷嘴裙内表面产生的静电场的进一步加速。第三，即使在激光照射结束后，质子仍然通过热电子的热能传递继续加速。

二维粒子模拟证明了 MNA 的有效性。微喷嘴充当“功率透镜”，将激光的能量通量放大到氢棒上。模拟结果表明，在 1 x 10^22 W/cm^2 的激光强度下，质子能量超过 1 GeV。与传统的靶后鞘层加速 (TNSA) 方案相比，结果显示出明显更高的质子能量，突显了 MNA 在实现 GeV 级质子能量方面的潜力。模拟还展示了加速过程中电场、质子密度、电子密度和磁场的演变。

---

## 82. Ironclad 0.7.0 – SPARK和Ada中形式化验证的类Unix内核

**原文标题**: Ironclad 0.7.0 – formally verified Unix-like kernel in SPARK and Ada

**原文链接**: [https://codeberg.org/Ironclad/Ironclad/releases/tag/v0.7.0](https://codeberg.org/Ironclad/Ironclad/releases/tag/v0.7.0)

无法访问文章链接。

---

## 83. 我们不小心发布的、速度惊人的 AI 生成内核

**原文标题**: Surprisingly fast AI-generated kernels we didn't mean to publish yet

**原文链接**: [https://crfm.stanford.edu/2025/05/28/fast-kernels.html](https://crfm.stanford.edu/2025/05/28/fast-kernels.html)

斯坦福CRFM博客宣布AI生成CUDA-C内核速度惊人，用于基础ML算子，性能可与甚至超过PyTorch中专家优化的生产内核，无需依赖CUTLASS或Triton等库。

该团队使用KernelBench指导的简单合成数据生成方法来训练模型，生成自定义内核以替换PyTorch算子。其关键创新在于通过以下方式解决顺序修订的局限性：
1.  用自然语言推理优化思路。
2.  在每个优化步骤中进行分支，以探索多种实现方式。

这种方法将内核优化转化为结构化的探索式搜索，由优化假设和并行评估引导。

在Nvidia L40S GPU上，使用OpenAI o3和Gemini 2.5 Pro对KernelBench问题进行的实验显示出令人印象深刻的结果：

*   **Matmul (FP32):** torch.matmul的101.3%。
*   **Conv2D:** torch.nn.Conv2D的179.9%。
*   **Softmax:** torch.softmax的111.8%。
*   **LayerNorm:** torch.nn.LayerNorm的484.4%。
*   **Conv2D + ReLU + MaxPool:** 高达参考实现的290.1%。

最佳内核通常在后期出现，利用了内存访问优化、异步操作、数据类型精度优化和平行化增强等优化策略。Conv2D的示例优化轨迹说明了迭代改进过程。

作者强调了将推理与并行探索相结合的重要性，并强调了使用该方法生成合成数据以改进模型训练的潜力。他们对进一步改进保持乐观，尤其是在FP16内核方面，并认为这项工作代表了内核生成自改进AI系统的重要一步。附录中包含了快速Conv2D内核的代码。

---

## 84. AtomVM，物联网设备的Erlang虚拟机

**原文标题**: AtomVM, the Erlang virtual machine for IoT devices

**原文链接**: [https://www.atomvm.net/](https://www.atomvm.net/)

AtomVM：面向物联网设备的轻量级 Erlang 虚拟机。它实现了 BEAM 虚拟机和 Erlang/OTP 标准库的子集，并针对资源受限的微控制器进行了优化。这使得开发者可以使用 Erlang 或 Elixir 编写物联网应用，利用现代的、基于 Actor 的并发模型，简化开发并提高代码清晰度。

AtomVM 提供诸如进程生成、监控、消息传递、抢占式调度和高效垃圾回收等关键特性。它还提供与微控制器外设和协议（如 GPIO、I2C、SPI、UART 和 WiFi，在 ESP32 等支持设备上）的直接接口。其目标是将函数式编程的强大功能引入低成本的物联网设备（低至 2 美元）。入门资源包括文档、示例代码（正在开发中）和教程（正在开发中）。

---

## 85. 使用 Bpftrace 探索语言运行时

**原文标题**: Exploring a Language Runtime with Bpftrace

**原文链接**: [https://www.mgaudet.ca/technical/2025/5/28/exploring-a-language-runtime-with-bpftrace](https://www.mgaudet.ca/technical/2025/5/28/exploring-a-language-runtime-with-bpftrace)

本文详细介绍了作者使用 eBPF 和 bpftrace 对 JavaScript 引擎 (SpiderMonkey) 进行性能分析的探索过程。出于对 `Rooted` 对象创建（影响垃圾回收）的频率和来源的好奇，作者利用 bpftrace 追踪引擎中的函数调用。

最初，作者难以获取 `Rooted` 构造函数调用的文件名和行号信息。随后，他们转而追踪所有 `Rooted` 构造函数都会调用的 `registerWithRootLists` 函数。他们的第一次尝试产生了未符号化的地址。

在得到提示后，他们学会了显式打印来自 bpftrace 映射中的聚合数据，并保持目标进程运行足够长时间以打印输出。他们还学会了通用化 bpftrace 程序，以接受目标可执行文件作为命令行参数。最终的 bpftrace 脚本使用 `ustack(perf,3)` 来捕获对 `registerWithRootLists` 的调用的前 3 个堆栈帧，并聚合计数。

该 bpftrace 脚本针对各种 JavaScript 引擎子测试执行，生成了报告，突出了过度调用 `registerWithRootLists` 的区域。这促成了错误报告，并最终确定了通过使用 `RootedTuple` 和减少不必要的 rooting 来优化内存管理的机会。作者最后预告了未来一篇关于使用 bpftrace 编写分配分析器的文章。

---

## 86. Show HN: AI同行评审员 – 用于科学手稿分析的多智能体系统

**原文标题**: Show HN: AI Peer Reviewer – Multiagent system for scientific manuscript analysis

**原文链接**: [https://github.com/robertjakob/rigorous](https://github.com/robertjakob/rigorous)

此篇“Show HN”帖子介绍了严谨AI审稿人，一个旨在通过AI驱动的工具改进科学知识流程的项目。其核心产品是`Agent1_Peer_Review`，一个用于全面科学手稿分析的多智能体系统。它提供关于章节、科学严谨性和写作质量的详细反馈，生成包含可执行建议的JSON输出，并生成专业的PDF报告。用户可以通过上传手稿并指定目标期刊/会议，在`https://www.rigorous.company/`访问AI审稿人的云版本。该服务目前免费，但希望用户能提供反馈以改进系统。

另一个工具，`Agent2_Outlet_Fit`，正在开发中，旨在评估手稿与特定期刊/会议的匹配度。

该项目用Python（3.7+）构建，需要一个OpenAI API密钥（可适应其他LLM）。欢迎通过Pull Requests贡献。开发者鼓励用户如果在研究或项目中使用严谨AI审稿人，请引用它。该项目由Robert Jakob和Kevin O'Sullivan在苏黎世用心制作。

---

## 87. 寻找自传签名

**原文标题**: Searching for Autograms

**原文链接**: [https://curiosityarb.blog/2024/12/01/searching-for-autograms.html](https://curiosityarb.blog/2024/12/01/searching-for-autograms.html)

本文探讨了创建“自指句”这一引人入胜的挑战，即能够准确计数自身字符的句子。作者详细介绍了一种通过编程来寻找这些难以捉摸的句子的方法，该方法建立在自指句的发明者 Lee Sallows 的工作之上。

其核心思想是找到一个句子的“自描述循环”，其中每个句子描述前一个句子的字符数。通过基于前一个句子的字符数反复生成新句子，该过程最终会形成一个句子重复的循环。周期为 1 的循环就是一个自指句。

为了更有效地实现自指句，作者实现了 Sallows 技术的变体。这涉及在更新句子中所有字母的计数和仅更新单个随机字母的计数之间交替。这种策略有助于摆脱较大且不希望出现的循环，并增加发现单个自指句的机会。

本文提供了使用代码找到的自指句示例，包括自定义主题的句子，例如生日贺卡消息和包含字母表中每个字母的全字母自指句。作者还提供了一个自枚举单词列表——反射词汇表的极简示例。文章还包括了关于自指句和全字母句的资源链接。

---

## 88. 韦伯望远镜助力改进哈勃常数

**原文标题**: Webb telescope helps refine Hubble constant

**原文链接**: [https://phys.org/news/2025-05-webb-telescope-refines-hubble-constant.html](https://phys.org/news/2025-05-webb-telescope-refines-hubble-constant.html)

本文探讨了詹姆斯·韦伯太空望远镜（JWST）如何帮助解决关于哈勃常数，即宇宙膨胀速度的长期争论。十年来，科学家们一直致力于解决因观察早期宇宙（通过宇宙微波背景）或使用涉及超新星和其他恒星的方法观察当今宇宙而产生的不同膨胀率测量值。

芝加哥大学的温迪·弗里德曼教授及其团队利用JWST改进了星系距离的测量，这是使用“本地”方法计算哈勃常数的关键组成部分。JWST卓越的分辨率和灵敏度，尤其是在红外方面，使科学家能够看穿尘埃，更准确地测量遥远恒星的亮度。

弗里德曼最新的计算结果，结合了哈勃和JWST的数据，得出了每百万秒差距70.4公里/秒的值，误差为正负3%。该结果现在与宇宙微波背景的测量值（67.4，误差为正负0.7）在统计上一致，表明表面上的不一致性可能正在减弱。

这些发现支持了宇宙的标准模型，表明哈勃常数的差异可能不是一个根本性的缺陷。该团队计划利用JWST收集来自后发座星系团的更多数据，这可能会进一步完善测量结果。这些新的测量结果甚至可以允许直接计算哈勃常数，而无需依赖超新星。

---

## 89. Show HN: 一款受 Go 启发且不依赖 LLVM 的新编程语言

**原文标题**: Show HN: A new programming language inspired by Go, no LLVM

**原文链接**: [https://github.com/nature-lang/nature](https://github.com/nature-lang/nature)

Nature：一种新型开源通用编程语言，受 Go 启发，旨在保留其优势的同时改进其不足之处。它拥有简洁的语法、直接编译到机器代码（无需 LLVM 或 VM）以及使用 musl libc 实现轻松交叉编译以进行部署。主要特性包括泛型、联合类型、接口、空值安全、类似 Go 的高性能 GC 和内存分配器以及共享栈协程。它集成了用于 IO 事件循环的 libuv、一个模块/包管理器 (npkg) 和常用数据结构。

错误处理使用 try/catch，模式匹配使用 match，并发依赖于通道和 select。Nature 支持直接调用 C 标准库函数并提供编辑器 LSP 支持。未来计划包括测试 DSL（AI 辅助）、用于 macOS 的跨平台链接器 (macho)、协作调度、WASM/RISC-V 支持以及编译为 Go。

目前，Nature 支持 Linux (amd64/arm64) 和 macOS (amd64/arm64)。虽然存在一个可用的早期版本，具有稳定的语法 API，但未来的开发将侧重于标准库的改进、用户反馈和错误修复。该语言的目标应用包括游戏引擎、科学计算、操作系统、物联网、命令行工具和 Web 开发。安装说明和文档链接以及项目示例均已提供。

---

## 90. 药物发现的毒性蛋白

**原文标题**: Toxic Proteins for Drug Discovery

**原文链接**: [https://www.asimov.press/p/toxic-proteins](https://www.asimov.press/p/toxic-proteins)

有毒蛋白质和肽类作为药物创新蓝图的潜力：以毒攻毒

本文探讨了有毒蛋白质和肽类，特别是来自毒液和有毒生物的蛋白质和肽类，作为药物创新蓝图的潜力。虽然传统上被视为有害，但这些由氨基酸组成的化合物具有独特的机制，可以被重新用于治疗。

文章重点介绍了几个例子，包括：

*   **司美格鲁肽（Ozempic/Wegovy）：** 一种受人体GLP-1激素启发而开发的抗糖尿病/肥胖药物，但经过非蛋白氨基酸工程改造以抵抗降解，延长了其有效性。
*   **芋螺胰岛素（mini-Ins）：** 一种改良自芋螺“极乐阴谋集团”胰岛素的版本，该胰岛素能诱导鱼类低血糖休克，目前正在开发作为一种快速作用的胰岛素类似物，用于治疗糖尿病。
*   **齐考诺肽：** 一种源自芋螺毒液的强效止痛药，通过阻断电压敏感性钙通道来抑制疼痛。
*   **α-鹅膏蕈碱：** 一种来自“死亡帽”蘑菇的致命毒素，抑制mRNA的产生，并正在探索作为抗体-药物偶联物（ADCs）中的有效载荷，以靶向并杀死癌细胞。
*   **蛇毒肽：** 几种获得FDA/EMA批准的药物，如替罗非班和依替巴肽，都是基于在蛇毒中发现的肽类，用于治疗急性冠状动脉综合征。

文章强调，进化驱使生物体创造出强大的毒素用于防御或捕食，而理解这些机制可以带来创新的药物开发。通过减弱毒性并利用这些化合物的特定作用，科学家可以创造出具有增强的安全性和疗效的新型疗法。

---

## 91. 射电天文学软件无线电

**原文标题**: Radio Astronomy Software Defined Radio (Rasdr)

**原文链接**: [https://radio-astronomy.org/rasdr](https://radio-astronomy.org/rasdr)

本文探讨了射电天文软件无线电 (RASDR) 概念，重点关注为射电天文设计的 SDR 接收机。这些接收机旨在具有宽带宽、Windows 兼容性，并提供完善的文档，使其适用于射电天文应用。基于 RASDR 概念完成的两款硬件设计中，目前只有 RASDR4 型号正在销售。

---

## 92. 展示一下：我构建了一个AI代理，可以将ROS 2的turtlesim变成数字艺术家

**原文标题**: Show HN: I built an AI agent that turns ROS 2's turtlesim into a digital artist

**原文链接**: [https://github.com/Yutarop/turtlesim_agent](https://github.com/Yutarop/turtlesim_agent)

“Show HN”：`turtlesim_agent`——自然语言控制的ROS 2海龟绘图AI智能体

此“Show HN”帖子介绍`turtlesim_agent`，这是一个AI智能体，可以将ROS 2 turtlesim模拟器转变为由自然语言控制的数字艺术家。它使用LangChain来解释文本指令，并将其转换为turtlesim的运动命令，从而使用户能够通过用简单的英语描述形状和设计来进行绘图，彩虹示例就是一个很好的例子。

要开始使用，用户需要ROS 2 Humble Hawksbill、Python 3.10+，以及`requirements.txt`中列出的依赖项。设置包括克隆存储库、安装依赖项、配置所需语言模型提供商（OpenAI、Anthropic、Google、Cohere、Mistral，或像Ollama这样的自托管LLM）的API密钥，并在`turtlesim_node.py`和`turtlesim_agent.launch.xml`中指定LLM模型。LangSmith集成是可选的，用于跟踪和调试。

该智能体可以通过CLI（用于开发目的）或GUI聊天界面（用于用户友好的交互）运行。它使用位于`tools/`目录中的工具（例如，motion_tools、pen_tools、math_tools）来控制海龟。用户可以通过添加自己的自定义工具来扩展智能体的功能。该项目鼓励贡献，例如新工具、模型、提示或用例，并邀请用户在wiki上分享他们的作品。

---

## 93. 使用AVX512破解谷歌kernelCTF的PoW

**原文标题**: Beating Google's kernelCTF PoW using AVX512

**原文链接**: [https://anemato.de/blog/kctf-vdf](https://anemato.de/blog/kctf-vdf)

蒂莫西·赫申详细介绍了他是如何优化用于谷歌 kernelCTF 竞赛的计算密集型“工作量证明”函数的，最终助力其团队赢得 51,000 美元的赏金。该竞赛要求快速解决一个“树懒”可验证延迟函数（VDF），以便在其他团队之前获得对易受攻击服务器的访问权限。赫申意识到有些团队可能正在使用 FPGA 来绕过预期的延迟，因此专注于优化 VDF 的核心模平方运算。

起初，他利用数学变换和 C++ 来提高速度，利用 GMP 库并针对梅森数优化模运算。然而，还需要进一步改进。随后，他转向 AVX512，即英特尔的 SIMD 扩展，特别是 AVX512IFMA 指令（vpmadd52luq 和 vpmadd52huq），这些指令旨在加速大整数算术。

赫申使用 AVX512IFMA 指令实现了一个自定义的 52 位基数平方例程，精心安排乘法并利用掩码来最大限度地减少开销。该过程涉及计算存储在 512 位寄存器中的 52 位字长的平方和交叉乘积。最后执行模 2<sup>1279</sup>-1 的归约。

与基于 GMP 的解决方案相比，这种 AVX512 实现提供了显著的加速，使该团队能够更快地解决工作量证明，从而在 kernelCTF 竞赛中获得竞争优势。 这种优化帮助他们获得了赏金。

---

## 94. 评论的未来，大概是谎言

**原文标题**: The Future of Comments Is Lies, I Guess

**原文链接**: [https://aphyr.com/posts/388-the-future-of-comments-is-lies-i-guess](https://aphyr.com/posts/388-the-future-of-comments-is-lies-i-guess)

一位资深内容审核员认为，大型语言模型（LLM）从根本上改变了在线垃圾信息的格局，使其成本更低、更加复杂，且更难检测。 过去，垃圾信息要么是低成本且容易过滤的，要么是高成本、有针对性且相对罕见的。 LLM 引入了一个新的类别：自动生成的垃圾信息，模仿真实的人类互动，利用看似合理的评论和捏造的个人经历来推广链接或产品。

作者提供了示例，包括 LLM 生成的专门引用帖子内容的博客评论和不正确的文章摘要。 这种“垃圾”并非总是出于商业动机，而是助长了虚假信息并降低了在线讨论的质量。

作者强调了内容审核员日益增加的负担，他们现在必须区分真实的笨拙和自动化垃圾信息。 他们担心随着 LLM 变得更加先进，垃圾邮件发送者找到创新的用途，这个问题会变得更加严重。 令人信服的语音诈骗的兴起以及 LLM 创建虚假人物并建立用于恶意目的的长期关系的可能性尤其令人担忧。

虽然社交网络已经开发了复杂的防御机制，但作者担心这些技术在去中心化平台（如电子邮件和 Mastodon）上的适用性，这些平台由于规模较小目前很脆弱，但可能会变得更具吸引力。 作者最后表达了对在线审核未来在日益复杂的 LLM 驱动的垃圾信息面前感到不安。

---

## 95. 梯度是新的区间

**原文标题**: Gradients Are the New Intervals

**原文链接**: [https://www.mattkeeter.com/blog/2025-05-14-gradients/](https://www.mattkeeter.com/blog/2025-05-14-gradients/)

本文探讨了在三维图形隐式曲面光栅化中使用梯度（特别是Lipschitz连续性）替代区间算术的方法。作者受到IRIT和Adobe Research一篇论文的启发，该论文利用有符号距离函数（SDF）的Lipschitz性质（有界梯度）进行优化，例如裁剪不活跃的图元和远场剔除，从而加快复杂模型的渲染速度。

作者将之前使用区间算术的实现与基于Lipschitz连续图元的单点评估的新方法进行了比较。单点评估成本更低，并避免了区间算术的保守性，但它仅限于表现良好的图元。核心思想是，对于Lipschitz连续距离场，单点评估可以产生类似区间的结果，从而可以使用标准的区间算术技术。

本文用一个圆的例子说明了这一点，展示了如何使用伪区间（从单点样本和梯度边界导出）。它还强调了区间算术的一个缺点：对变换的敏感性，而Lipschitz连续性方法可以缓解这个问题。

此外，本文还解决了距离场不是Lipschitz连续的情况，提出了一种涉及前向模式自动微分的归一化技术，以强制执行Lipschitz性质（在最小值/最大值之前对梯度进行归一化）。两种方法都注意到表达式简化带来的好处（通过修剪分支来降低复杂性）。最后，本文讨论了性能方面的考虑，并强调了单点采样由于效率更高而优于区间算术。

---

## 96. 三角形泼溅：用三角形表示的辐射场

**原文标题**: Triangle splatting: radiance fields represented by triangles

**原文链接**: [https://trianglesplatting.github.io/](https://trianglesplatting.github.io/)

本文介绍了一种名为“三角形溅射”的新型辐射场渲染方法，该方法使用三角形作为基本场景表示。作者认为应该回归三角形，利用其与标准图形流水线和GPU硬件的兼容性。“三角形溅射”通过一个可微渲染器，将每个三角形渲染为可微溅射，并使用端到端梯度直接优化三角形。

其核心创新在于一种平滑的窗口函数，该函数源自每个投影三角形的2D有向距离场(SDF)，用于调节其对像素颜色的影响。这种函数允许调整清晰度，并防止高斯溅射方法中常见的模糊现象。三角形参数（顶点、颜色、不透明度、平滑度）通过基于梯度的学习进行优化。

结果表明，与2D和3D高斯溅射相比，“三角形溅射”实现了更高的视觉保真度、更快的收敛速度和更高的渲染吞吐量，尤其是在保留锐利边缘和精细细节方面。在Mip-NeRF360数据集上，它优于并发的非体积基元，甚至在室内场景中实现了比Zip-NeRF更高的感知质量。此外，该方法具有令人印象深刻的渲染速度，在单个RTX4090上，以1280x720分辨率渲染Garden场景时，可达到2,400 FPS以上。

基于三角形的表示固有的与基于网格的渲染器兼容，便于无缝集成到传统图形流水线和游戏引擎中，为AR/VR和交互式模拟中的实时应用开辟了可能性。虽然当前的视觉效果并未针对游戏引擎的保真度进行优化，但它们代表了将辐射场集成到交互式3D环境中的重要一步。

---

## 97. C++ 到 Rust 短语手册

**原文标题**: C++ to Rust Phrasebook

**原文链接**: [https://cel.cs.brown.edu/crp/](https://cel.cs.brown.edu/crp/)

这本《C++ 到 Rust 惯用法手册》是为从 C++ 过渡到 Rust 的程序员设计的资源。它提供了常见 C++ 编程模式到地道 Rust 代码的翻译和解释，并通过实践示例和工程考量讨论进行说明。

本书结构便于随机访问，允许用户通过将遇到的特定问题与熟悉的 C++ 方法联系起来，快速找到 Rust 编码的解决方案。它并非旨在深入研究 Rust 的内部机制（如 Rustonomicon），而是一个专注于弥合两种语言之间差距的实用指南。

本书由布朗大学认知工程实验室经验丰富的 C++ 和 Rust 程序员创建，优先考虑准确性和平衡的细节水平。它鼓励用户利用其他资源，如《Rust 程序设计语言》、《Y 分钟学会 X》和《嵌入式 Rust 书籍》，以获取基础知识和特定的嵌入式系统应用。

鼓励读者通过每页底部的链接提供反馈，以提高本书的准确性和内容。作者还会收集匿名用户测验回复以供研究之用。最后，可以选择提供电子邮件地址以接收新增章节的通知。

---

## 98. 胆固醇治疗单次剂量可降低69%水平

**原文标题**: Cholesterol treatment can cut levels by 69% after one dose

**原文链接**: [https://www.sciencefocus.com/news/new-cholesterol-treatment-could-be-revolutionary-verve](https://www.sciencefocus.com/news/new-cholesterol-treatment-could-be-revolutionary-verve)

实验性药物VERVE-102单次注射显示出显著降低低密度脂蛋白（“坏”）胆固醇水平的潜力，有望彻底改变心脏病发作的预防。一项临床试验的早期结果表明，该药物仅需一剂即可降低高达69%的胆固醇，为每日服用他汀类药物提供了一种“一劳永逸”的替代方案。

VERVE-102通过“关闭”肝脏中的PCSK9基因发挥作用，该基因调节血液中低密度脂蛋白胆固醇的清除。该试验涉及14名患有家族性高胆固醇血症（一种导致高低密度脂蛋白胆固醇的遗传性疾病）的参与者。所有参与者反应良好，没有严重的副作用。不同剂量导致低密度脂蛋白胆固醇的降低幅度不同，最高剂量平均降低53%，其中一名参与者降低了69%。

包括Eugene Braunwald博士在内的专家认为，初步数据“充满希望”，并暗示它可能预示着心血管疾病治疗的新时代。虽然该试验结果尚未经过同行评审，但心脏病专家Riyaz Patel教授强调了VERVE-102在显著改变胆固醇管理方面的潜力。Verve目前正在多个国家招募更高剂量药物的进一步试验参与者，最终结果预计将于2025年下半年公布。

---

## 99. 为什么我们不能拥有好的私有TLD DNSSEC

**原文标题**: Why we can't have nice private TLD DNSSEC

**原文链接**: [https://egbert.net/blog/articles/dns-dnssec-private.html](https://egbert.net/blog/articles/dns-dnssec-private.html)

本文探讨了在企业和家庭实验室中为私有局域网和私有顶级域名（TLD）实施 DNSSEC 所面临的挑战。作者认为，尽管人们希望实现本地化的信任锚分发，但当前的 DNSSEC 基础设施并不适合此目的。

核心问题在于 DNSSEC 的设计，它依赖于从根区域向下延伸的信任链。对于私有局域网，这需要与父区域的所有者进行带外协调以插入 DS 记录，当使用私有 TLD 来避免外部暴露时，这个过程变得不切实际。

作者批评了现有的解决方案，例如过滤私有子域名和分离域名的名称服务器，认为它们不足以结合 DNSSEC 和隐私。他们指出，DNS 验证器的当前逻辑需要从父区域检索 DS 记录，从而阻止了私有 TLD 的干净“区域分割”。

本文提出了一种修改 DNS 解析器的方法，以允许对私有区域的 DS 记录进行“预验证”，从而有效地创建本地信任锚。虽然承认潜在的缺点，例如中间人攻击，但作者认为，这种系统在内部使用并采取适当的安全措施，可以显著提高 DNSSEC 在私有环境中的采用率。他们认为当前 DNSSEC 的采用率很低，并且内部私有采用不会影响 Internet 的整体安全态势。

作者最后倡导更改解析器，允许绕过通常的 DS 记录查找，改为本地查找。他们强调了更广泛地采用 DNSSEC 和更轻松的管理员培训的潜力。

---

## 100. 复制 Excel 表格到 Markdown 表格 (反之亦然)

**原文标题**: Copy Excel to Markdown Table (and vice versa)

**原文链接**: [https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/](https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/)

该文章 "将Excel复制到Markdown表格（反之亦然）" (thisdavej.com) 概述了一种简单有效的方法，用于在Excel表格和Markdown表格之间转换数据。它解决的核心问题是两种格式之间缺乏直接兼容性，需要在两者之间移动数据时进行手动重新格式化。

提出的解决方案包括从Excel电子表格中复制数据，然后使用具有多光标功能的文本编辑器（文章特别提到了VS Code）来添加必要的Markdown表格语法。这种语法包括每行单元格的前导和尾随竖线（|），以及表头分隔线（|- -|- -|）。

文章详细介绍了以下步骤：

1.  **从Excel复制数据。**
2.  **将数据粘贴到文本编辑器中**（如VS Code） - 数据将以制表符分隔。
3.  **使用多光标在每行的开头和结尾添加竖线（|）。** 这通常通过将光标放在第一行的开头，使用键盘快捷键（在VS Code中为Alt+Shift+向下箭头）在每个后续行上创建光标，然后键入竖线来完成。 对行尾重复此过程。
4.  **添加表头分隔线。** 这涉及在标题行之后手动添加一行带有"|- -|- -"（或类似的，取决于列数）的行。

该文章还暗示了反向过程（Markdown到Excel），尽管它没有提供太多细节。 它建议复制Markdown表格并将其粘贴到Excel中。 如果竖线格式正确，Excel通常会自动将数据解析为列。

本质上，该文章提供了一种实用的解决方法，使用多光标编辑来弥合Excel和Markdown表格之间的差距，从而提供了一种比手动重新格式化更快的替代方案。

---

