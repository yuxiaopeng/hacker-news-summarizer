# Hacker News 热门文章摘要 (2025-09-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Nuclear: 专注于从免费源流式传输的桌面音乐播放器

**原文标题**: Nuclear: Desktop music player focused on streaming from free sources

**原文链接**: [https://github.com/nukeop/nuclear](https://github.com/nukeop/nuclear)

Nuclear：一款桌面音乐播放器，旨在从YouTube、Jamendo、Audius和SoundCloud等免费在线资源流式传输音乐。它的目标是提供类似Spotify的体验，但无需订阅费且拥有更大的音乐库。

主要功能包括：

*   **多来源流媒体：** 访问来自YouTube（包括播放列表和SponsorBlock集成）、Jamendo、Audius和SoundCloud的音乐。
*   **专辑和曲目信息：** 专辑搜索（由Last.fm和Discogs提供支持）和自动歌曲查找。
*   **播放列表管理：** 歌曲队列，可导出到播放列表，加载已保存的播放列表（JSON格式）。
*   **Last.fm集成：** 音乐记录和“正在播放”状态更新。
*   **探索：** 带有评论的最新发行、流派浏览、电台模式以及按流行度浏览。
*   **下载：** 无限制下载（由YouTube提供支持）。
*   **歌词和本地播放：** 实时歌词显示和从本地库收听。
*   **其他功能：** 音频标准化，无需帐户，无广告，无行为准则(NoCoC)，无贡献者许可协议(NoCLA)。

该项目是开源的，欢迎贡献。 提供适用于各种操作系统和软件包管理器的软件包，包括AUR、Choco、GURU、Homebrew、Snap、Flatpak、Void Linux和Nix/NixOS。 该应用程序还支持通过Crowdin进行的社区翻译。

Nuclear根据GNU Affero通用公共许可证第3版或更高版本获得许可。

---

## 2. Claude 代码：现已在 Zed 中推出 Beta 版

**原文标题**: Claude Code: Now in Beta in Zed

**原文链接**: [https://zed.dev/blog/claude-code-via-acp](https://zed.dev/blog/claude-code-via-acp)

代码编辑器 Zed 发布 Claude Code 公开测试版集成，后者是一款流行的 AI 代码生成工具。此次集成得益于 Zed 全新的开放标准“代理客户端协议（ACP）”，该协议允许任何 AI 代理连接到 Zed（以及 Neovim 等其他编辑器）。

该集成提供以下优势：

*   在 Zed 中原生运行 Claude Code，提供相比终端界面更高性能的体验。
*   支持实时观察跨多个文件的编辑，并提供语法高亮和语言服务器支持。
*   通过多缓冲区提供细粒度的更改审查和批准，允许开发者接受或拒绝单个代码块。
*   使 Claude Code 的任务列表在 Zed 的侧边栏中保持可访问。
*   通过 Claude Code 的斜杠命令支持自定义工作流程。

Zed 没有选择专有集成，而是选择了 ACP，以实现灵活性和更广泛的兼容性。他们已在 Apache 许可下开源了 Claude Code 适配器，使其可用于任何采用 ACP 的编辑器。该集成通过 SDK 提供 Claude Code 的大部分核心功能，并且将添加更多功能，例如 Plan 模式。

文章鼓励开发者使用 ACP 将他们的代理与 Zed 集成，为 ACP 和 Claude Code 适配器存储库做出贡献，并提供反馈。文章还提到 Zed 正在招聘对软件开发充满热情的人才。

---

## 3. 微软 VibeVoice：前沿开源文本转语音模型

**原文标题**: Microsoft VibeVoice: A Frontier Open-Source Text-to-Speech Model

**原文链接**: [https://microsoft.github.io/VibeVoice/](https://microsoft.github.io/VibeVoice/)

微软VibeVoice：更具表现力和自然语音的全新开源文本转语音模型。VibeVoice的主要特点包括：

*   **上下文感知表达：** 该模型旨在生成考虑到文本上下文的语音，从而产生更合适的语调和情感。
*   **自发情感：** VibeVoice可以自发地将情感注入语音，无需明确提示。
*   **自发歌唱：** 该模型可以直接从文本生成歌唱声音，表明其具有音乐表达能力。
*   **带背景音乐的播客：** VibeVoice能够生成与背景音乐集成的语音，表明其适合播客创作。
*   **跨语言能力：** 该模型支持跨语言TTS，特别强调了普通话到英语和英语到普通话的转换。
*   **长篇对话语音：** 它旨在生成更长的对话语音段落，展示了其处理更复杂叙事的能力。

时间戳的包含（尽管可能不准确）表明该模型专为需要精确语音段定时序的应用程序而设计。总的来说，VibeVoice代表了开源TTS的重大进步，旨在创建更具吸引力和更像人类的口语音频。

---

## 4. 十维空间中的随机漫步 (2021)

**原文标题**: A Random Walk in 10 Dimensions (2021)

**原文链接**: [https://galileo-unbound.blog/2021/06/28/a-random-walk-in-10-dimensions/](https://galileo-unbound.blog/2021/06/28/a-random-walk-in-10-dimensions/)

本文《十维空间中的随机漫步》探讨了高维空间中系统的反直觉行为，尤其与机器学习、进化动力学和复杂系统分析相关。作者认为，理解高维物理学至关重要，因为这些空间越来越多地被用于模拟复杂现象。

一个核心概念是“维度诅咒”，即可视化变得不可能，过度拟合盛行，低维直觉失效。本文以随机漫步为例来说明这些挑战。虽然简单的随机漫步在1维、2维和3维中都有教学，但高维随机漫步在分子进化等复杂系统中至关重要，其中每个基因位点代表一个维度。

本文专门研究了一个10维超晶格，展示了可视化的困难和计算限制。它将非约束随机漫步（所有位点都可访问）与“最大粗糙”景观（具有随机势值）中的约束漫步进行了对比。主要发现是在高维度中，“山脊”（具有相似势值的连通区域）比“山峰”（孤立的高势值点）更为常见。这可以通过渗流理论和渗流阈值的概念来解释。如果足够多的位点共享一个相似的势值以超过阈值，则步行者可以在景观上自由漫游，即使在“山脊”上也是如此。

文章总结说，这种山脊的普遍性对进化和机器学习具有深远的影响。在进化方面，它表明物种可以在保持合理适应度水平的同时探索广阔的突变空间。在机器学习中，它表明优化算法可以通过跟随这些山脊而不是陷入局部最优来更有效地导航复杂的损失函数。

---

## 5. Warp Code：从提示到产品最快的方式

**原文标题**: Warp Code: the fastest way from prompt to production

**原文链接**: [https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod](https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod)

Warp推出Warp Code，旨在加速Agent生成代码从提示到生产的交付过程。关键功能包括由GPT-5驱动的顶级编码Agent，在Terminal-bench和SWE-bench Verified上表现出色。Warp Code提供专门的代码审查面板，用于修改和行编辑，轻量级文件编辑器，具有语法高亮显示，以及利用WARP.md文件、Agent配置文件和斜杠命令的项目管理工具。

目标是改进“Agent引导”过程，让开发人员在使用AI编码Agent时拥有更多的控制权和理解力。Warp认识到，虽然Agent在不断改进，但人工指导仍然至关重要，以确保代码的正确性和可维护性。代码审查和文件编辑等功能实现了开发人员和Agent之间的紧密反馈循环。

早期测试显示出显著成果，用户每周生成1.5亿行代码，并接受超过97%的生成差异。用户平均每天节省一小时。未来的更新将包括进一步的编辑器增强、更智能的代码审查和远程环境支持。

---

## 6. 打造世界上最精确的DIY数控车床[视频]

**原文标题**: Building the most accurate DIY CNC lathe in the world [video]

**原文链接**: [https://www.youtube.com/watch?v=vEr2CJruwEM](https://www.youtube.com/watch?v=vEr2CJruwEM)

内容并非文章，而更像是YouTube视频标题（“打造世界上最精确的DIY数控车床[视频]”）以及YouTube的标准版权和政策页脚。

因此，摘要为：

内容涉及一个关于打造高精度DIY数控车床的YouTube视频。提供的其余文本是标准的YouTube法律和政策信息，与视频内容没有直接关系。

---

## 7. Svix（webhook 即服务）正在招聘创始营销负责人。

**原文标题**: Svix (webhooks as a service) is hiring for a founding marketing lead

**原文链接**: [https://www.svix.com/careers/?ashby_jid=ca9d34d5-94c9-4729-836a-423725ee8b22](https://www.svix.com/careers/?ashby_jid=ca9d34d5-94c9-4729-836a-423725ee8b22)

Svix是一家资金充足、受Y Combinator支持的公司，正在招聘热衷于帮助企业打造世界一流Webhook体验的人才。 他们正在寻找聪明、精力充沛、学习能力强的队友，这些人喜欢与开发者合作，并秉持他们的核心价值观：快速执行、致力于卓越的开发者体验以及渴望自主和掌控。 Svix提供了一个机会，让你对公司的发展轨迹和产品开发产生重大影响，解决有趣的技术挑战，并在风险投资支持的环境中获得构建开发者工具的第一手经验。

Svix的愿景是成为领先的Webhook平台，类似于SendGrid之于事务性电子邮件和Twilio之于短信。 他们的目标是为网络中很大一部分Webhook提供支持，并在软件的API优先的未来中发挥关键作用。 Andreessen Horowitz (a16z) 是 Svix 的投资者，并相信他们的愿景。

虽然提供的文本中未详细说明具体的空缺职位，但Svix鼓励有才华的人即使不完全符合现有职位也应申请。 他们提供文档、API 参考、源代码、联系页面和 Slack 社区等资源，以支持他们的用户和开发者。

---

## 8. Voyager是一个具有实时3D重建功能的交互式视频生成模型。

**原文标题**: Voyager is an interactive video generation model with realtime 3D reconstruction

**原文链接**: [https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager)

HunyuanWorld-Voyager 是一个新颖的视频扩散框架，能够从单张图像生成世界一致的 3D 点云序列，并由用户定义的相机路径引导。它生成用于探索的 3D 一致场景视频，以及用于 3D 重建的对齐 RGB 和深度视频。

关键组件包括一个联合生成 RGB 和深度视频的世界一致视频扩散架构，以及一个采用高效世界缓存和自回归推理的长程世界探索机制，用于迭代场景扩展。一个可扩展的数据引擎，自动化相机姿态估计和度量深度预测，被用于创建超过 10 万个视频片段的训练数据集。

Voyager 在 WorldScore 基准测试中表现出优于 WonderJourney 和 Gen-3 等其他方法的性能，在内容对齐和 3D 一致性方面表现出色。代码和模型权重已发布，安装说明包括克隆存储库、创建 conda 环境以及安装 PyTorch 和其他依赖项，包括用于加速和并行推理的 flash attention 和 xDiT。推理可以在单个 GPU 或使用 xDiT 的多个 GPU 上执行。还提供了一个 Gradio 演示用于交互使用。用于训练数据生成的数据引擎也已发布。

---

## 9. 空中客车B612驾驶舱字体

**原文标题**: Airbus B612 Cockpit Font

**原文链接**: [https://github.com/polarsys/b612](https://github.com/polarsys/b612)

空中客车B612字体系列是一款开源字体，旨在优化飞机驾驶舱屏幕上的易读性。它由空中客车公司、法国国立民用航空学院（ENAC）和图卢兹第三大学合作开发，旨在改善驾驶舱内的信息显示，侧重于易读性、阅读舒适度和整体一致性。Intactile DESIGN协助开发了该字体的八种排版变体，该字体以圣埃克苏佩里的《小王子》中的B612星球命名。其主要设计特点包括最大化字符间距、尊重字母原型以及协调形状和间距。该文档还概述了发布字体新版本的流程，包括更新版本号、合并Fontlab中的交叉点、生成TTF文件以及修复数字签名。该字体版权归空中客车公司所有（2012年），并以三重许可发布，包括Eclipse公共许可证v2.0、Eclipse分发许可证v1.0和SIL开放字体许可证v1.1。

---

## 10. 约翰·科尔特兰的音调圈

**原文标题**: John Coltrane's Tone Circle

**原文链接**: [https://roelsworld.eu/blog-saxophone/coltrane-tone-circle/](https://roelsworld.eu/blog-saxophone/coltrane-tone-circle/)

无法访问文章链接。

---

## 11. 模仿 Pioneer LaserActive 历时 16 年的漫长征程

**原文标题**: The 16-year odyssey it took to emulate the Pioneer LaserActive

**原文链接**: [https://www.readonlymemo.com/this-is-the-first-the-16-year-odyssey-of-time-money-wrong-turns-and-frustration-it-took-to-finally-emulate-the-pioneer-laseractive/](https://www.readonlymemo.com/this-is-the-first-the-16-year-odyssey-of-time-money-wrong-turns-and-frustration-it-took-to-finally-emulate-the-pioneer-laseractive/)

本文详细介绍了终身世嘉迷Nemesis历时16年，致力于模拟Pioneer LaserActive的旅程。LaserActive是20世纪90年代一款独特的激光影碟播放器/游戏机混合体，由于其依赖于使用激光影碟的全动态视频游戏玩法，使得模拟极具挑战性，捕捉和解码模拟视频面临着巨大的障碍。

Nemesis于2009年开始了他的项目，最初低估了其复杂性。他面临着诸如电容器失效、硬件不可靠以及需要逆向工程系统BIOS和寄存器块等问题。他开发了自定义程序来探测硬件、访问寄存器并从光盘中提取数字数据。

最大的挑战是捕捉和解码激光影碟视频，因为现有的采集卡无法处理LaserActive快节奏、分支视频流或包含关键帧信息的垂直消隐区间 (VBI) 数据。由于工作和家庭事务，他多次暂停了该项目。

开源激光影碟提取项目Domesday Duplicator最终提供了一个解决方案。Nemesis 为其配套软件ld-decode做出了重大贡献，专门为 LaserActive 光盘添加了功能，例如捕捉完整的导入/导出数据、完整的 NTSC 视频，并改进了音频解码。

到 2024 年，Nemesis 开发了必要的工具和流程，以适合模拟的格式提取 LaserActive 游戏，从而在 2025 年初推出了有史以来第一个 LaserActive 模拟器。他拆封了全新的、从未玩过的 LaserActive 游戏，终于准备好保存和分享这些独特的游戏体验。

---

## 12. 谁拥有、运营和开发你的VPN很重要

**原文标题**: Who Owns, Operates, and Develops Your VPN Matters

**原文链接**: [https://www.opentech.fund/news/who-owns-operates-and-develops-your-vpn-matters-an-analysis-of-transparency-vs-anonymity-in-the-vpn-ecosystem-and-implications-for-users/](https://www.opentech.fund/news/who-owns-operates-and-develops-your-vpn-matters-an-analysis-of-transparency-vs-anonymity-in-the-vpn-ecosystem-and-implications-for-users/)

无法访问文章链接。

---

## 13. 夜光室内植物绽放彩虹般的光芒

**原文标题**: Glow-in-the-dark houseplants shine in rainbow of colours

**原文链接**: [https://www.nature.com/articles/d41586-025-02740-2](https://www.nature.com/articles/d41586-025-02740-2)

研究人员通过向多肉植物注射磷光颗粒（类似于夜光玩具中的材料）创造了夜光室内植物。由华南农业大学张学杰领导的团队开发了一种方法，使多肉植物发出各种颜色的光芒，这与Light Bio公司销售的转基因生物发光植物（如矮牵牛）仅发出绿光不同。

注入的磷光颗粒吸收光能，储存起来，然后在几个小时内缓慢地重新释放出来。科学家们使用了铝酸锶颗粒，调整其尺寸以最大限度地提高发光效果，并发现大约7微米的颗粒效果最佳。多肉植物“姬胧月”被证明是最合适的植物，尽管该过程需要单独注射每片叶子。

发光效果在曝光后可持续长达120分钟，并在10天内可重复触发。该团队实现了蓝绿色、蓝紫色、绿色、红色和白色等色调。他们已经申请了专利，并设想将该技术用于装饰装置和生物照明。虽然像生物发光矮牵牛这样的转基因植物通过内部化学反应产生光，但注射的多肉植物由于磷光材料的余辉特性而发光。

---

## 14. 如何做好演讲

**原文标题**: How to Give a Good Talk

**原文链接**: [https://blog.sigplan.org/2025/03/31/how-to-give-a-good-talk/](https://blog.sigplan.org/2025/03/31/how-to-give-a-good-talk/)

迈克尔·格林伯格的文章《如何做一场精彩的演讲》认为，一场好的学术演讲是有价值的，它能说服听众关心演讲者的工作。文章强调了通过提供信息、教育和娱乐来传递价值，从而赢得听众注意力的重要性。

提供信息包括清晰地呈现工作的动机和价值主张，解决诸如效率、正确性和表达性等基本问题。格林伯格提供了一些常见的“问题/解决方案”框架来构建价值主张，例如证明以前认为不可能的事情是可能的，或者改进现有的方法。

教育包括为听众提供有价值且可移植的内容，他们可以将其应用于自己的工作中，例如新的见解或技术，即使它不是核心技术成果。

娱乐对于抓住听众的注意力并留下良好的第一印象至关重要。这可以通过幽默、真诚、清晰的结构、个人魅力或感染力来实现，需要练习并找到个人表演风格。

格林伯格强调，学者应该意识到他们工作提供的价值，并努力有效地沟通这种价值。一场成功的演讲通过告知听众价值主张、用新的教学来教育他们以及娱乐他们，从而与听众达到平衡。作为回报，听众提供他们的时间和注意力。最终，说服人们相信自己工作的重要性是学术研究的一个关键方面。

---

## 15. 抽象机模型，兼谈：Rust 的独到之处

**原文标题**: Abstract Machine Models Also: what Rust got particularly right

**原文链接**: [https://dr-knz.net/abstract-machine-models.html](https://dr-knz.net/abstract-machine-models.html)

本文深入探讨了作者理解编程语言、计算机架构和程序员直觉之间关系的旅程。文章从为一种具有过多未定义参数的假想微处理器架构设计编程工具的令人沮丧的经历开始，进而意识到硬件设计对编程工具设计影响巨大。

作者批评了计算机架构中过度依赖抽象模型的现象，认为改变模型并非设计或创造行为。Haskell及其指称语义的存在使作者的探索更加复杂，最初模糊了描述和规范之间的界限。通过观察到功能等效的Haskell程序（如不同的排序算法）具有截然不同的实际性能，作者取得了一项突破，而这种差异并未被该语言的语义模型所捕捉。这使得作者理解到程序员的选择在功能等价之外也很重要。

文章介绍的核心概念是“抽象机器模型”（AMM），它代表了程序员用于预测运行时行为的心理模型。AMM通过整合时间、内存使用、I/O、调试界面、吞吐量、抖动和能量消耗等额外功能方面来扩展功能模型。至关重要的是，AMM具有组合语义，使程序员能够预测程序组件的组合行为。作者认为，AMM既不同于编程语言，也不同于底层硬件，并将其与语言相对论和算法复杂性的历史发展相提并论。

---

## 16. 能源仪表盘（英国）

**原文标题**: Energy Dashboard (UK)

**原文链接**: [https://www.energydashboard.co.uk/map](https://www.energydashboard.co.uk/map)

无法访问文章链接。

---

## 17. 魔灯回归

**原文标题**: Magic Lantern Is Back

**原文链接**: [https://www.magiclantern.fm/forum/index.php?topic=27315.0](https://www.magiclantern.fm/forum/index.php?topic=27315.0)

无法访问文章链接。

---

## 18. 使用最小示例理解 Transformer

**原文标题**: Understanding Transformers Using a Minimal Example

**原文链接**: [https://rti.github.io/gptvis/](https://rti.github.io/gptvis/)

本文通过一个极度简化的例子，可视化 Transformer 模型的内部状态，从而解释其工作原理。该方法使用一个专注于水果口味关系的最小数据集、基于单词的基本分词，以及一个微型的仅解码器 Transformer 模型，该模型仅包含两层、两个注意力头和 20 维嵌入。

这种简化允许对信息流进行详细观察。文章将 token 嵌入可视化为彩色方块的堆叠，展示了模型如何学习诸如 “spicy” 和 “sweet” 等单词的独特和共享特征。然后，它追踪了通过 Transformer 层的正向传递，展示了最终输入 token 的表示如何演变为类似于预测的下一个 token（例如，“chili”）的嵌入。

一个关键的观察结果是注意力机制的作用。可视化结果揭示了模型在处理序列时关注哪些 token。例如，当预测 “i like spicy so i like” 之后的下一个单词时，模型会强烈关注 “spicy”，利用该上下文来正确预测 “chili”。这证实了该模型学习的关系超出了简单的记忆。尽管训练数据有限，但成功的验证表明了通过注意力机制内的选择性上下文理解实现的泛化。本文认为 Andrej Karpathy 的 “Neural Networks: Zero to Hero” 系列是灵感来源。源代码可在 Github 上获得。

---

## 19. Linux内核漏洞利用实战：CVE-2024-50264

**原文标题**: Kernel-hack-drill and exploiting CVE-2024-50264 in the Linux kernel

**原文链接**: [https://a13xp0p0v.github.io/2025/09/02/kernel-hack-drill-and-CVE-2024-50264.html](https://a13xp0p0v.github.io/2025/09/02/kernel-hack-drill-and-CVE-2024-50264.html)

本文详细介绍了作者利用CVE-2024-50264漏洞的历程，这是一个Linux内核AF_VSOCK子系统中极具挑战性的释放后使用（UAF）漏洞。该漏洞源于套接字连接和信号处理期间的竞争条件，允许非特权用户触发内存损坏。作者最初因其复杂性和脆弱性而搁置了该漏洞，后来发现其他人已经披露了它。

尽管发生了碰撞，作者还是采取了一种独特的利用策略，专注于跨缓存攻击。他们遇到了许多障碍，包括旨在缓解堆喷射的内核配置。本文重点介绍了利用的难度，概述了诸如UAF的快速计时和随后的空指针解引用等限制。

作者最初尝试破坏`cred`对象未果。然后，他们将重点转移到`msg_msg`对象，这是作者之前在其他漏洞利用中使用的一种技术。本文介绍了一种新的`msg_msg`喷射方法，涉及部分填充消息队列以延迟`m_list`字段的初始化，从而实现受控的内存损坏。UAF写入会损坏`msg_msg`对象的`m_list`、`m_type`和`m_ts`字段。这允许在UAF之后进行受控覆盖，从而可能导致权限提升。本文强调了该漏洞获得2025年Pwnie奖最佳权限提升奖当之无愧。

---

## 20. 使用Shodan发现数千个暴露的Ollama实例

**原文标题**: Finding thousands of exposed Ollama instances using Shodan

**原文链接**: [https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama)

使用Shodan识别公开暴露的Ollama服务器及其他LLM部署的安全研究，揭示了因配置错误和缺乏适当安全措施而导致的一个重大漏洞。该研究开发了一个Python工具来查询Shodan，发现了超过1100个暴露的Ollama服务器，其中约20%正在积极托管无需身份验证即可访问的模型。

该研究强调，LLM的易于部署通常超过了安全考虑，导致未经授权的API访问、模型提取、越狱和资源劫持等风险。该方法涉及查询Shodan以查找在与Ollama、vLLM和LM Studio等LLM平台关联的默认端口上运行的服务器，然后通过检查身份验证强制执行情况和对提示的响应来以编程方式评估其安全态势。

主要发现表明，大多数暴露的服务器位于美国、中国和德国。虽然一些服务器没有运行任何模型，但其他的服务器运行了Mistral和LLaMA模型。一个令人担忧的趋势是OpenAI兼容API模式的广泛采用，这简化了互操作性，但也创建了一个统一的攻击面。作者发现近90%的服务器都在使用这种模式，这使得攻击者可以使用为Open AI产品编写的工具来攻击自托管的LLM。

文章最后强调了LLM部署中建立安全基线的迫切需求，并提供了缓解常见漏洞以防止滥用和利用的建议。该研究承认了与Shodan的覆盖范围以及LLM服务器指纹识别准确性相关的局限性。

---

## 21. 在 Rust 和 Python 之间共享可变引用

**原文标题**: Sharing a mutable reference between Rust and Python

**原文链接**: [https://blog.lilyf.org/posts/python-mutable-reference/](https://blog.lilyf.org/posts/python-mutable-reference/)

本文探讨了如何在 Django Rusty Templates 项目中，使用 PyO3 将一个表示 Django 模板上下文的可变 Rust 结构体与 Python 共享。 挑战在于 PyO3 不直接支持将带有生命周期的 Rust 结构体暴露给 Python。

解决方案包括以下几个步骤：

1. **取得所有权：** 使用 `std::mem::take` 将可变引用 `&mut Context` 转换为拥有的 `Context` 值，并将原始值替换为默认值。

2. **封装在 PyO3 类中：** 将拥有的 `Context` 封装在 `#[pyclass]` 结构体 `PyContext` 中，供 Python 使用。

3. **返回所有权：** 在 Python 函数调用后检索可能已被修改的 `Context`。 最初尝试了 `std::mem::replace`，但由于所有权问题而失败。

4. **使用 `Arc` 和 `Mutex`：** 最终解决方案使用 `Arc` (原子引用计数) 来允许为 Python 克隆 `PyContext`。 `Arc::try_unwrap` 尝试重新获得 `Context` 的所有权。 如果 Python 仍然持有引用（引用计数 > 1），它会使用自定义的 `clone_ref` 方法克隆上下文以处理 Python 引用计数。 为了允许从 Python 进行修改，引入了 `Mutex` 来保护 `Context` 免受并发访问。 使用 `MutexExt` 可以防止与 Python 解释器发生死锁。

总之，本文重点介绍了如何使用 `std::mem::take`、`std::mem::replace`、`Arc`、`Mutex` 和 PyO3 的 `MutexExt` 来克服共享可变 Rust 数据结构与 Python 时的限制，同时确保内存安全和线程安全。

---

## 22. MIT研究发现人工智能使用会重塑大脑，导致认知能力下降

**原文标题**: MIT Study Finds AI Use Reprograms the Brain, Leading to Cognitive Decline

**原文链接**: [https://publichealthpolicyjournal.com/mit-study-finds-artificial-intelligence-use-reprograms-the-brain-leading-to-cognitive-decline/](https://publichealthpolicyjournal.com/mit-study-finds-artificial-intelligence-use-reprograms-the-brain-leading-to-cognitive-decline/)

麻省理工研究：依赖ChatGPT写作或致认知衰退。

---

## 23. 随着人工智能蓬勃发展，戴尔数据中心业务终于超过了其个人电脑业务。

**原文标题**: With AI Boom, Dell's Datacenter Biz Is Finally Bigger Than Its PC Biz

**原文链接**: [https://www.nextplatform.com/2025/08/29/with-ai-boom-dells-datacenter-biz-is-finally-bigger-than-its-pc-biz/](https://www.nextplatform.com/2025/08/29/with-ai-boom-dells-datacenter-biz-is-finally-bigger-than-its-pc-biz/)

本文分析了戴尔近期的财务表现，重点强调了人工智能浪潮对其业务的影响。戴尔的基础设施解决方案集团（ISG），包括服务器、存储和数据中心网络，首次超过了其客户端解决方案集团（PC业务）。 这一转变主要由人工智能服务器销售额的显著增长所驱动。

戴尔2026财年第二季度业绩显示，服务器和网络销售额增长了68.7%，这得益于人工智能系统销售额增长了2.6倍，达到81亿美元。 与CoreWeave等公司的重大交易促成了这一增长。 该公司的人工智能系统积压订单仍然高达117亿美元。 然而，尽管 ISG 的收入激增，但营业收入利润率低于历史平均水平，这表明戴尔目前的人工智能系统交易盈利能力不高。

本文还深入探讨了更广泛的行业背景，指出原始设备制造商面临着一个选择：要么销售英伟达的人工智能硬件堆栈，但营业收入被稀释，要么错失可观的人工智能收入。 迈克尔·戴尔的领导力以及对“购买美国货”的渴望也被认为是使戴尔受益的因素。 本文预测人工智能服务器的销售额将保持强劲，戴尔预计2026财年的人工智能系统销售额至少将达到200亿美元。 尽管传统服务器可能迎来更强的升级周期，但预计人工智能和传统服务器业务的营收在今年将大致持平。

---

## 24. CPU 利用率是个谎言

**原文标题**: %CPU utilization is a lie

**原文链接**: [https://www.brendanlong.com/cpu-utilization-is-a-lie.html](https://www.brendanlong.com/cpu-utilization-is-a-lie.html)

文章指出，系统监控工具报告的CPU利用率并不能可靠地反映剩余处理能力。作者通过对 Ryzen 9 5900X 处理器的压力测试表明，报告的CPU利用率与实际执行的工作量之间的关系是非线性的，并且常常具有误导性。

具体来说，测试表明，在“50%利用率”下，系统通常可以执行其最大可能工作负载的60-100%，具体取决于任务类型（通用CPU、整数运算、矩阵运算）。

这些差异归因于两个主要因素：**超线程**和**睿频加速**。超线程会导致性能瓶颈，因为“虚拟”内核共享资源，从而限制了额外线程的优势。睿频加速会根据活动核心的数量动态调整 CPU 时钟速度，从而进一步扭曲利用率指标。随着更多核心被激活，CPU的时钟速度会下降，从而有效地减少了每个周期完成的工作量，而这并未反映在利用率计算中。

作者总结说，依赖 CPU 利用率进行容量规划可能会导致不准确的预测。相反，他们建议在服务器遇到错误或出现不可接受的延迟之前，对服务器实际完成的工作进行基准测试，然后监控服务器当前的工作负载，并将这两个指标进行比较。与依赖报告的 CPU 利用率相比，这种方法可以更准确地了解服务器容量。

---

## 25. 这个博客运行在一个回收的谷歌Pixel 5 (2024)上

**原文标题**: This blog is running on a recycled Google Pixel 5 (2024)

**原文链接**: [https://blog.ctms.me/posts/2024-08-29-running-this-blog-on-a-pixel-5/](https://blog.ctms.me/posts/2024-08-29-running-this-blog-on-a-pixel-5/)

作者成功地用一块太阳能板驱动，运行在一台回收的、被 Verizon 锁定的 Google Pixel 5 手机上运行其网站的实验，本博文详细介绍了该实验。 受其他永续计算爱好者的启发，作者试图最大限度地减少功耗并重新利用旧硬件。

作者选择 Pixel 5 是因为它支持用于有线互联网的 USB-OTG 以及其相对较新的安全状态。他们利用连接到 Jackery 160w 电站的 100w 太阳能板为手机供电，强调了该设置的离网和可持续性。

该博客运行在 Termux（一个终端模拟器）上，出乎意料的是，它支持所有必要的工具，包括 Hugo（静态站点生成器）、git、screen 和 dufs（一个用于轻松内容更新的文件服务器）。作者强调了在 Termux 中设置 Hugo 站点的简易性以及该设置的可靠性。

该帖子包含有关如何安装必要实用程序、配置 SSH 访问以进行远程管理以及使用 cronie 自动化站点更新的详细说明。 它还解释了备份策略，包括使用 rsync 到桌面和 NAS，以及本地 git 存储库。 作者欢迎反馈，并表示愿意根据要求提供有关设置特定方面的更多信息。 作者总结说，该网站运行完美，并且该设置比预期的要简单。

---

## 26. 一位资深工程师的Claude Code之旅

**原文标题**: A staff engineer's journey with Claude Code

**原文链接**: [https://www.sanity.io/blog/first-attempt-will-be-95-garbage](https://www.sanity.io/blog/first-attempt-will-be-95-garbage)

无法访问文章链接。

---

## 27. Lit：一个用于构建快速、轻量级 Web 组件的库

**原文标题**: Lit: a library for building fast, lightweight web components

**原文链接**: [https://lit.dev](https://lit.dev)

Lit：构建快速且可互操作 Web 组件的轻量级 JavaScript 库。它通过提供响应式、声明式模板以及减少样板代码的功能来简化 Web 组件开发。

Lit 的主要优势：

*   **快速性能：** Lit 拥有较小的体积（约 5KB）和高效的渲染，仅更新 UI 的必要部分，而无需完整的虚拟 DOM 差异比较。
*   **互操作性：** Lit 组件是原生 Web 组件，保证与任何框架、HTML 或 JavaScript 环境的兼容性。这使得它们非常适合共享组件和设计系统。
*   **基于标准：** Lit 基于 Web Components 标准构建，确保面向未来并减少供应商锁定。
*   **开发者友好：** Lit 具有作用域样式（Shadow DOM）、响应式属性以及基于标记模板字面量的声明式模板，可用于表达性和直接的组件定义。

Lit 适用于广泛的用例，包括：

*   共享组件
*   可在不同框架中使用的设计系统
*   站点和应用程序，允许渐进式增强和组件逐个更新。

该库提供了诸如实时教程、交互式 Playground 和大量文档等资源，以帮助开发人员入门。Lit 社区可以在 Discord、Bluesky、GitHub 和 Stack Overflow 上找到。

---

## 28. 为IBM Selectric打字机设计的Comic Sans打字球

**原文标题**: Comic Sans typeball designed to work with the IBM Selectric typewriters

**原文链接**: [https://www.printables.com/model/441233-comic-sans-typeball-for-the-ibm-selectric-typewrit](https://www.printables.com/model/441233-comic-sans-typeball-for-the-ibm-selectric-typewrit)

本文描述了一种假设性的产品：一款专为IBM Selectric打字机设计的Comic Sans字体字球。随后文本包含标题“性别轮吊坠”，以及三个数字：29、5和34。

文章的主要主题是为IBM Selectric打字机设计Comic Sans字球的*想法*。这结合了一种臭名昭著的、不受欢迎的字体选择（Comic Sans）和一种经典的、几乎是过时的打字技术（IBM Selectric）。它暗示了一种具有讽刺意味或幽默感的并置，即现代的非正式风格与复古和专业的风格。

随后包含的“性别轮吊坠”和三个数字在上下文中并不明确。在没有进一步信息的情况下，无法确定它们的相关性。它们可能与正在引入的次要主题有关，可能涉及珠宝或人口统计数据，或者它们可能是附加到初始声明的完全不相关的文本片段。这些数字可能代表数量、尺寸或其他数值属性。

---

## 29. Show HN: Chibi，告诉你用户流失的原因的人工智能

**原文标题**: Show HN: Chibi, AI that tells you why users churn

**原文链接**: [https://chibi.sh](https://chibi.sh)

Chibi：一款利用人工智能分析用户流失原因的平台。其核心优势在于通过深入分析用户行为背后的原因，洞察用户流失的根本原因，从而超越传统的分析方法。

该平台的核心在于了解“用户为什么流失”，表明其功能不仅仅是识别流失。这意味着该平台会分析用户数据（很可能是互动模式、反馈等），以确定导致流失的具体因素。这些因素可能包括可用性问题、定价问题、未满足的期望或功能缺陷。

标题和内容反复强调“了解用户行为背后的原因”，突出了平台对因果分析的关注，而不仅仅是描述性分析。通过了解用户流失的根本原因，企业可以采取有针对性的行动，改善用户留存率并解决特定的痛点。本质上，Chibi 旨在将原始数据转化为可操作的洞察，从而推动围绕产品开发、营销和客户服务的战略决策。该平台旨在使用户分析更具洞察力和可操作性，从而提高用户留存率。

---

## 30. TPDE-LLVM：更快的LLVM -O0后端

**原文标题**: TPDE-LLVM: Faster LLVM -O0 Back-End

**原文链接**: [https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664](https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664)

TPDE-LLVM，一种新型开源LLVM后端，与LLVM -O0相比，编译速度提升10-20倍，同时保持相似的运行时性能，代码大小增加10-30%。它面向x86-64和AArch64，并支持Clang在O0/O1优化级别下通常生成的LLVM-IR的典型子集。

加速是通过三步过程实现的：IR清理、分析（循环和活跃性分析）以及组合代码生成（降低、寄存器分配、机器代码编码）。虽然LLVM的优化后端在运行时和代码大小方面优于优化后的IR，但TPDE-LLVM专注于快速编译未优化的代码。

未来的计划包括DWARF支持、改进的寄存器分配，并可能根据社区需求扩展平台和代码模型支持。作者还指出了阻碍编译速度的LLVM-IR特性，例如ConstantExprs、任意大小的结构体/数组值、线程局部全局变量和任意位宽算术。他们建议了潜在的LLVM-IR改进，以进一步加速编译。 TPDE-LLVM后端可以用作库、类似llc的工具或通过补丁集成到Clang中。当前编译时间的一大部分花费在位码解析上。

---

## 31. SomaFM 二十五周年

**原文标题**: SomaFM 25th Anniversary

**原文链接**: [https://somafm.com/XXV/](https://somafm.com/XXV/)

SomaFM将于2025年9月20日在旧金山Verdi俱乐部举办25周年庆典派对，时间为晚上7点至午夜。活动将有SomaFM DJ、乐队、照相亭和免费礼品，主要目的是与听众一同庆祝，并感谢他们多年来的支持。

门票采用浮动定价（27美元、40美元和75美元），所有收益将用于支持SomaFM及本次活动。没有额外费用。购票者将被列入预售名单。活动仅限21岁及以上人士参加。

公告还包含SomaFM各种资源的链接，包括收听选项、新闻、捐赠信息、商店、播放列表、移动访问、播客和社交媒体链接。还包含一段简短视频，展示SomaFM各频道的发展历程。底部的版权信息列出了SomaFM部分频道的商标，并链接到其隐私政策和服务条款。

---

## 32. 我们已经生活在社会信用体系中了，只是我们不这么称呼它而已。

**原文标题**: We already live in social credit, we just don't call it that

**原文链接**: [https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/](https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/)

本文认为，尽管西方关注中国的社会信用体系，但我们实际上已经生活在一种西方式的社会信用之中。作者指出，优步、Instagram、亚马逊、领英和金融机构等众多平台都在利用算法来追踪和评估我们的行为，从而影响我们获得服务、机会和社会地位。这种评分往往是隐形的且无处不在，与中国体系不同，后者在目标方面更透明，尽管在西方经常被误解。

作者强调，中国的社会信用体系并非通常描绘的那种全国性的、无所不包的监控国家；它很大程度上是监管合规工具的碎片化集合，主要侧重于金融行为和商业监管。然而，西方的体系也存在问题，因为它通过不透明的算法运作，使得个人难以理解他们如何被评分以及原因。

文章警告说，西方这些碎片化的行为评分网络正在为未来潜在的全面社会信用体系构建技术和文化基础。虽然存在企业竞争，但转换成本很高，而且这些系统之间的合作日益密切，政府也在获取企业数据。作者最后提出，即使中国的体系存在缺陷，但透明度可能优于目前支配我们生活的隐形算法评估，让我们有机会了解规则并选择是否参与。

---

## 33. Amazonq.nvim：Neovim 官方 AWS AI 助手插件

**原文标题**: Amazonq.nvim: Official AWS AI Assistant Plugin for Neovim

**原文链接**: [https://github.com/awslabs/amazonq.nvim](https://github.com/awslabs/amazonq.nvim)

"Amazonq.nvim" 插件将 Amazon Q Developer（一款 AI 助手）的功能直接带入 Neovim 编辑器。它提供诸如聊天功能、内联代码建议和代码重构等特性，可通过 `:AmazonQ` 命令和 `zq` 映射进行访问。

要使用此插件，您需要 NodeJS >= 18 和 Neovim >= 0.10.4。安装可以通过手动方式或通过诸如 vim-plug 或 lazy.nvim 等插件管理器完成。需要进行身份验证，可以使用 AWS Builder ID（用于免费层）或为 Pro 订阅提供的起始 URL，通过 `ssoStartUrl` 选项进行配置。

此插件提供用于各种任务的命令：`:AmazonQ` 用于打开聊天窗口，`zq` 用于将选定的文本添加到聊天上下文，`:AmazonQ refactor` 用于代码重构，`:.AmazonQ fix` 用于修复当前行，`:%AmazonQ optimize` 用于优化整个文件，以及 `:AmazonQ explain` 用于解释当前文件。

默认情况下启用内联代码建议，并利用 Neovim 的 LSP 功能。故障排除步骤包括使用 `:checkhealth vim.lsp` 检查语言服务器状态，以及使用 `vim.lsp.set_log_level('debug')` 启用调试日志。该插件支持各种文件类型，并允许配置聊天面板外观。

该插件目前处于实验阶段，欢迎贡献。

---

## 34. 人工智能正在为盲人带来福音 (2023)

**原文标题**: AI is going great for the blind (2023)

**原文链接**: [https://robertkingett.com/posts/6230/](https://robertkingett.com/posts/6230/)

作为盲人群体的一员，作者对该群体内对人工智能的过度热情表示怀疑。虽然承认人工智能的潜在益处，例如人工智能驱动的图像描述和用于有声读物叙述的语音生成，但作者质疑依赖人工智能的准确性和长期影响。

作者指出，盲人群体接受人工智能，是因为它提供了以前无法获得的信息，即使这些信息并不准确。这源于一种感觉，即人类往往不愿意或无法提供帮助和可访问性。人工智能提供了一种独立感，并减少了成为负担的感觉。

然而，作者担心这种对技术的依赖仅仅是用对科技公司的依赖取代了对人类的依赖。他们预测未来的挑战，包括无法访问的人工智能平台和人工智能生成的恶化网络可访问性的代码。他们还担心，由于对人工智能的关注，诸如OCR和自动驾驶汽车等技术的进步将会停滞不前。

作者将他们的怀疑态度与盲人群体内的普遍兴奋感进行了对比，这种兴奋感是受到对客观性的渴望以及对技术可以解决人类未能解决的可访问性问题的信念驱动的。他们承认自己也使用人工智能工具，但仍然对它们的总体价值表示怀疑，并对更广泛的人工智能炒作周期表示担忧，并列举了人工智能失败和伦理问题的例子。作者推广揭穿人工智能炒作的播客，并倡导回归“独立网络”。

---

## 35. 看在老天的份上，你就用一下网络行吗？

**原文标题**: For all that's holy, can you just leverage the Web, please?

**原文链接**: [https://blog.tomayac.com/2025/09/03/for-all-thats-holy-can-you-just-leverage-the-web-please/](https://blog.tomayac.com/2025/09/03/for-all-thats-holy-can-you-just-leverage-the-web-please/)

作者讲述了其注册一台新的伊莱克斯洗衣机以获得十年保修的令人沮丧的经历。尽管宣传册上提供了电话号码和二维码（二维码指向明文的电话号码），但联系客服却困难重重。电话导致长时间的等待和挂断，而短信提供的聊天服务链接则指向一个存在证书问题的损坏网站。

受挫之下，作者在网上搜索并找到了一个需要账户才能使用的有效注册页面。令人惊讶的是，该页面提供了一项人工智能驱动的功能，允许用户上传洗衣机识别铭牌的照片，从中提取产品编号并轻松完成注册。作者将这种积极的体验与之前客服的失败之处进行对比，感叹伊莱克斯为什么一开始没有优先考虑这种在线注册方式。

核心抱怨是，在2025年，公司应该利用网络来处理诸如产品注册之类的简单任务，而不是依赖低效且令人沮丧的基于电话的客户服务。作者最后演示了客户端人工智能，展示了如何使用Prompt API从图像中提取产品编号，进一步突出了网络技术在此类任务中的潜力。他们强调了对人工智能输出进行服务器端验证的重要性。

---

## 36. 员工们之后吃了它。

**原文标题**: The staff ate it later

**原文链接**: [https://en.wikipedia.org/wiki/The_staff_ate_it_later](https://en.wikipedia.org/wiki/The_staff_ate_it_later)

日语短语“之后工作人员美味地享用了”（この後、スタッフが美味しくいただきました）是日本电视节目中显示的字幕，旨在向观众保证屏幕上显示的食物在拍摄后没有被浪费，以解决人们对食物处理和浪费的担忧。

这种做法最初是电视节目用来避免观众投诉的方式，这些观众对综艺节目中食物被随意对待很敏感。虽然确切的起源尚不清楚，但据信源于《Downtown no Gaki no Tsukai ya Arahende!!》中的一起事件，观众批评该节目浪费了表演中使用的西瓜。

这种说法的真实性备受争议。包括电视工作人员、美食记者和电视名人等在内的一些消息来源支持工作人员确实会消耗剩余食物的说法。他们给出的理由包括对提供食物的餐厅的义务感以及避免浪费的愿望。

然而，像喜剧演员松本人志和电影制作人北野武这样的著名人物对此表示怀疑。北野指出了一些食物在被错误处理后明显无法使用的情况。评论员还表示，食物通常只是被扔掉。

该字幕的使用被解释为制作团队的一种自我监管形式，旨在避免批评。虽然有些人认为这是对观众日益严格审查的必要回应，但另一些人认为这是一种空洞的让步，节目应该从一开始就专注于正确的信息处理。还有一种观点认为，电视节目应该被允许与现实生活脱节，而无需不断担心冒犯观众。

---

## 37. 共享即恐吓：将云文件共享与编程语言语义相关联

**原文标题**: Sharing Is Scaring: Linking Cloud File-Sharing to Programming Language Semantics

**原文链接**: [https://cs.brown.edu/~sk/Publications/Papers/Published/akf-sharing-scaring/](https://cs.brown.edu/~sk/Publications/Papers/Published/akf-sharing-scaring/)

论文《共享即恐慌：将云文件共享与编程语言语义联系起来》认为，用户在使用云文件共享应用程序时遇到的困难源于对链接、附加和编辑等操作的底层语义的误解，这与理解别名和变异等编程语言概念时遇到的挑战类似。

作者进行了一项用户研究，调查普通用户对文件共享的理解，并将编程教育文献中已知的误解改编成语义相似的文件共享任务。该研究采用了追踪和编程风格的任务，揭示了普遍存在的误解。

为了解决这些问题，作者开发了一套云文件共享操作的形式语义，反映了复制、引用和修改共享内容。 这种形式化旨在为改进用户心智模型、开发教育工具和创建自动化辅助提供基础。具体来说，该语义可以支持诸如轨迹检查、工作流合成和交互式反馈等应用。

本质上，本文提出，理解编程语言语义可以为云文件共享的设计和教学提供信息，最终提高用户的理解力并减少错误。补充材料，包括 Forge 模型、Cope and Drag 规范以及轨迹截图，均可在线获取。

---

## 38. 深入《英国烘焙大赛》的世界

**原文标题**: Inside the World of "The Great British Bake Off"

**原文链接**: [https://www.newyorker.com/magazine/2025/09/01/inside-the-world-of-the-great-british-bake-off](https://www.newyorker.com/magazine/2025/09/01/inside-the-world-of-the-great-british-bake-off)

本文深入探究了《英国烘焙大赛》的世界，追溯了它如何崛起成为一个深受喜爱且具有文化意义的电视现象。作者是一位节目的前申请者，详细描述了紧张的选角过程，突出了制片人关注寻找真正具有“纯粹意图”的业余烘焙师，而不是追名逐利者。文章探讨了该节目独特的吸引力，强调了其令人感到舒适、低风险的剧情，以及吸引专业烘焙师和普通观众的能力。

文章回顾了该节目早期的发展，从最初作为“蛋糕达人秀”的构想到意外发现其喜剧和贴近生活的基调。文章还描述了拍摄周末的结构，从清晨的到达开始，到三个核心挑战：招牌烘焙、技术挑战和展示烘焙。文章深入探讨了评委的个性和参赛者之间的互动，强调了对非剧本时刻和 relatable 角色的重视。最终，作者传达了《烘焙大赛》如何通过将精湛的烘焙技术与温馨的比赛和真诚的人际关系相结合，成功地俘获了全国人民的心。

---

## 39. 谷歌可以保留 Chrome 浏览器，但将被禁止签订独家合同。

**原文标题**: Google can keep its Chrome browser but will be barred from exclusive contracts

**原文链接**: [https://www.cnbc.com/2025/09/02/google-antitrust-search-ruling.html](https://www.cnbc.com/2025/09/02/google-antitrust-search-ruling.html)

联邦法官裁定，尽管谷歌去年在一项具有里程碑意义的反垄断案件中被判非法垄断互联网搜索，但仍可保留其Chrome浏览器。 然而，谷歌将被禁止签订独家合同以维持其主导地位。

该裁决驳回了司法部（DOJ）更激进的提议，例如迫使谷歌出售Chrome或Android操作系统。 法官认为这些措施超出了案件范围，该案件的重点是搜索分发。

该裁决的核心在于限制谷歌通过独家合同和付款来维持其默认搜索引擎地位的能力。 虽然谷歌仍然可以付款来预加载其搜索引擎等产品，但它不能强制执行独家协议。 司法部认为这是一个胜利，相信这将为通用搜索服务打开市场。

此外，谷歌被命令与竞争对手分享某些搜索索引数据和用户互动数据，但不包括广告数据。 这将以“普通的商业条款”进行。

投资者反应积极，Alphabet（谷歌的母公司）股价在盘后交易中上涨8%。 苹果公司的股票在盘后也上涨了4%，这可能是因为谷歌被允许继续向苹果公司支付数十亿美元，使其成为iPhone上的默认搜索引擎。 谷歌对强加的限制对用户及其隐私的影响表示担忧。

---

## 40. 让 Linux 家庭服务器在空闲时休眠并在需要时唤醒 (2023)

**原文标题**: Making a Linux home server sleep on idle and wake on demand (2023)

**原文链接**: [https://dgross.ca/blog/linux-home-server-auto-sleep](https://dgross.ca/blog/linux-home-server-auto-sleep)

本文详细介绍了如何在2023年配置Linux家庭服务器，使其在空闲时自动休眠，并按需唤醒，重点介绍一种无需手动干预的“即插即用”解决方案。目标是通过让服务器在不使用时休眠来降低功耗，但仍能访问SSH和Time Machine备份等服务。

该解决方案涉及使用低功耗、常开设备（如树莓派）作为“ARP代理”，代表休眠服务器响应ARP请求。这确保了网络上的其他设备仍然可以将服务器的IP地址解析为其MAC地址，从而通过单播数据包启用网络唤醒（Wake-on-LAN）。

服务器上的关键步骤包括：启用带有单播数据包的网络唤醒，设置一个cron作业，根据用户登录和网络连接（例如，AFP流量）触发空闲休眠，禁用IPv6，以及选择性地配置网络服务在休眠前停止，以防止不必要的唤醒。

树莓派（或类似设备）运行“ARP代理”脚本，该脚本侦听针对休眠服务器IP地址的ARP请求，并以其MAC地址响应。还可以配置常开设备上的Avahi，以便在服务器休眠时宣传其网络服务。

作者详细描述了他们经历的各种失败尝试，包括“Wake on PHY activity”和静态ARP条目。关键突破是理解ARP响应的重要性并实施“ARP代理”方法。

---

## 41. 用Odin语言（<750行）和C语言（<500行）实现的带垃圾回收的Lisp解释器

**原文标题**: Lisp interpreter with GC in <750 lines of Odin (and <500 lines of C)

**原文链接**: [https://github.com/krig/LISP](https://github.com/krig/LISP)

本文介绍了 "komplott" (C 语言版) 和 "komplodin" (Odin 语言版)，这是受 McCarthy 最初 LISP 启发而实现的极简 Lisp 解释器。两者都是单文件实现，其中 "komplott" 不到 500 行 C 代码，而 "komplodin" 不到 750 行 Odin 代码。Odin 版本最初是 C 版本的直接翻译，但后来略有差异。

主要功能包括 Scheme 兼容性（足以运行某些测试程序）、基于 Cheney 算法的复制半空间垃圾收集器、有限的尾调用优化和最少的错误处理。本文强调了这些项目的教育价值，并重点介绍了 Andy Wingo 的博客，以便更深入地了解垃圾收集器。

该存储库还包括 "lisp15.scm"，这是 1962 年 LISP 1.5 核心的实现。提供的代码片段展示了 LISP 1.5 的语法和功能，如 `pairlis`、`assoc`、`atom?`、`evcon`、`evlis`、`apply` 和 `eval`。本文提供了构建和运行这两个版本的说明，需要 `gcc` 来构建 "komplott"，需要 Odin 编译器来构建 "komplodin"。`make test` 命令会运行 LISP 1.5 以及提供的测试用例。最后一个示例演示了 LISP 1.5 中的 `MAPCAR` 函数。

---

## 42. 线性代数小册

**原文标题**: The Little Book of Linear Algebra

**原文链接**: [https://github.com/the-litte-book-of/linear-algebra](https://github.com/the-litte-book-of/linear-algebra)

《线性代数小书》为初学者提供了线性代数基本概念的入门介绍。第一章重点介绍向量，定义了$\mathbb{R}^n$中的标量和向量，强调其几何解释（点、位移、抽象元素）。本章介绍了向量加法和标量乘法，重点介绍了它们如何形成线性组合，这对于理解张成和子空间至关重要。然后，本章探讨了点积，定义了范数（向量长度）和向量之间的角度，从而引出了正交性（高维中的垂直性）的概念。通过投影进一步解释正交性，从而将向量分解为平行和正交分量。第一章最后说明了如何使用这些概念来解决最小二乘逼近和格拉姆-施密特过程。

第二章从矩阵的定义开始，矩阵是被排列成行和列的数字矩形阵列。

---

## 43. “难以想象”：这些蚂蚁不同物种却拥有同一母亲

**原文标题**: 'Almost unimaginable': these ants are different species but share a mother

**原文链接**: [https://www.nature.com/articles/d41586-025-02807-0](https://www.nature.com/articles/d41586-025-02807-0)

这篇《自然》杂志的文章重点介绍了伊比利亚收获蚁 (Messor ibericus) 奇异的繁殖策略。与大多数物种不同，伊比利亚收获蚁蚁后可以产生属于不同物种（Messor structor）的雄性后代。这得益于一种独特的性寄生形式，即M. ibericus蚁后利用M. structor的精子。

在两个物种共存的地区，M. ibericus蚁后与M. structor雄性交配，产生杂交工蚁。然而，在意大利西西里岛上，研究人员发现，尽管没有M. structor种群，伊比利亚收获蚁群落仍然繁荣昌盛。

基因分析显示，西西里岛的伊比利亚收获蚁蚁后正在克隆雄性M. structor蚂蚁。这种“自助式”克隆过程涉及蚁后产下只含有M. structor DNA的卵子。这些克隆雄蚁随后与蚁后交配，产生杂交工蚁，这些工蚁执行筑巢和觅食等重要任务。

本质上，M. ibericus有效地驯化了M. structor的基因组，使其即使在没有自然存在的M. structor种群的情况下也能繁殖并维持一个蚁群。这种不寻常的繁殖策略展示了一个引人入胜的进化适应案例，并挑战了基本的生物学规范。

---

## 44. 基于物理原理的渲染

**原文标题**: Physically based rendering from first principles

**原文链接**: [https://imadr.me/pbr/](https://imadr.me/pbr/)

本文通过解释光及其与物质相互作用的潜在物理现象，对基于物理的渲染（PBR）进行了互动式介绍。文章首先定义了光，并探讨了各种历史和现代理论，从射线光学到量子电动力学，突出了射线光学在计算机图形学中的准确性。

文章深入研究了电磁学，涵盖了诸如电荷、电场、库仑定律、狭义相对论和麦克斯韦方程等概念，阐述了这些原理如何解释电磁波的产生和传播。文章还讨论了电磁波谱以及光如何通过白炽（如灯泡和太阳）和电致发光（LED）产生。

第二章重点介绍了光与物质的相互作用，解释了原子层面的吸收和散射。然后，通过假设均匀且完全光滑的材料来简化这些相互作用，从而得出受反射定律和斯涅尔定律支配的反射和折射原理。文章介绍了菲涅尔方程和施里克近似，用于计算反射和折射光量。文章还涉及全内反射和斯涅尔窗口。

最后，文章介绍了微表面模型，解释了表面外观是如何在像素级别上微表面的统计平均值。文章根据金属和非金属与光的相互作用区分它们。由于自由电子吸收光，金属主要表现出镜面反射，没有漫反射，而非金属（电介质）可以吸收光子。文章讨论了粗糙度与光线传播的关系，并介绍了双向反射分布函数（BRDF）的概念。

---

## 45. Matrix.org主服务器因RAID故障而崩溃

**原文标题**: Matrix.org homeserver grinds to a halt after RAID meltdown

**原文链接**: [https://www.theregister.com/2025/09/03/matrixorg_raid_failure/](https://www.theregister.com/2025/09/03/matrixorg_raid_failure/)

Matrix.org主服务器因2025年9月2日发生的RAID故障而遭遇重大中断，导致用户无法发送或接收消息。问题始于辅助数据库文件系统故障，随后主数据库崩溃。

Matrix.org主服务器依赖于一个大型PostgreSQL数据库，该数据库此前在7月份曾出现损坏问题，导致加入房间和发送消息出现问题。恢复数据库极具挑战性，最终决定执行完整的55 TB数据库快照恢复并重放17个小时的流量。

据Element首席工程官Neil Johnson称，该事件是由一次例行存储升级因一系列不幸事件引发的。尽管Matrix.org主服务器的用户目前无法访问该服务，但发送给他们的消息将被排队，并在服务恢复后传递。预计不会有数据丢失。

该事件凸显了Matrix去中心化性质的优势。拥有自己主服务器的用户和使用Matrix技术的组织仍未受到影响。对于Matrix.org来说，这次中断令人尴尬，但它证明了去中心化系统的弹性及其保护用户免受单点故障影响的能力。文章强调了去中心化消息传递日益增长的重要性，因为组织寻求集中式服务的替代方案，以实现主权和隐私。

---

## 46. <template>: 内容模板元素

**原文标题**: <template>: The Content Template element

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)

`<template>` HTML 元素用于存放 HTML 片段，这些片段之后可以通过 JavaScript 使用，或者用来生成 Shadow DOM。它自 2015 年 11 月起得到广泛支持。 关键属性包括 `shadowrootmode`（声明式地创建 Shadow Root，取代 `shadowroot`）、`shadowrootclonable`、`shadowrootdelegatesfocus`（将焦点委托给 Shadow DOM 中的第一个可聚焦元素）和 `shadowrootserializable`。

`<template>` 中的内容默认情况下不会渲染，并且通过 `content` 属性访问，该属性包含一个 DocumentFragment。 避免直接将事件处理程序附加到 DocumentFragment。 如果 `<template>` 标签内存在 `<html>`、`<head>` 或 `<body>` 标签，将会导致解析器错误。

`<template>` 元素有两个主要用途：创建可重用的文档片段和实现声明式 Shadow DOM。 声明式 Shadow DOM 使用 `shadowrootmode` 立即为父元素生成 Shadow DOM。 如果存在 `shadowrootmode` 属性，且具有允许的值 'open' 或 'closed'，则 `<template>` 将被 ShadowRoot 替换。

---

## 47. 静态站点带来良好的时光旅行体验。

**原文标题**: Static sites enable a good time travel experience

**原文链接**: [https://hamatti.org/posts/static-sites-enable-a-good-time-travel-experience/](https://hamatti.org/posts/static-sites-enable-a-good-time-travel-experience/)

无法访问文章链接。

---

## 48. Ada入门：基于项目的探索与Rosetta示例

**原文标题**: Introduction to Ada: a project-based exploration with rosettas

**原文链接**: [https://blog.adacore.com/introduction-to-ada-a-project-based-exploration-with-rosettas](https://blog.adacore.com/introduction-to-ada-a-project-based-exploration-with-rosettas)

本文通过一个基于项目的教程，将以安全关键系统闻名的Ada语言介绍为一种现代的、通用的编程语言。 该项目涉及创建一个Ada程序，生成SVG格式的动画玫瑰花图案，展示Ada的功能以及Ada 2022的新特性。

本文重点介绍了Ada起源于美国国防部，它在嵌入式和实时系统中的优势，以及它对可读性、强类型和最小未定义行为的强调。 它强调Ada严格的编译器就像一个伙伴，帮助程序员编写更清晰、更正确的代码。

本教程将逐步讲解程序的结构，从输出（SVG文件）开始，并探讨Ada的特性如何发挥作用。 它涵盖了Alire（Ada包管理器）的使用，以及GNAT Studio和Visual Studio Code的Ada & SPARK扩展等开发环境选项。

本文深入探讨了代码，解释了包（Rosetta用于计算，Rosetta_Renderer用于SVG输出）、数据类型（Hypotrochoid, Coordinate, Coordinate_Array）和函数（Compute_Points）的作用。 它强调了Ada的安全边界检查、常量使用和模块化设计。 它还涉及编译器强制执行的Ada严格编码风格，从而提高一致性和可维护性。

---

## 49. “世界模型”：人工智能领域中的一个旧概念，卷土重来

**原文标题**: 'World Models,' an old idea in AI, mount a comeback

**原文链接**: [https://www.quantamagazine.org/world-models-an-old-idea-in-ai-mount-a-comeback-20250902/](https://www.quantamagazine.org/world-models-an-old-idea-in-ai-mount-a-comeback-20250902/)

人工智能研究中“世界模型”的复兴：一种旨在创造环境内部表征，供人工智能预测结果和做出决策的理念。LeCun、Hassabis 和 Bengio 等领先的人工智能研究人员认为，世界模型对于实现真正的人工通用智能 (AGI) 至关重要。

该概念起源于心理学家 Kenneth Craik 在 20 世纪 40 年代提出的理论，即人工智能系统应该携带一个“小规模”的现实模型，以便在行动之前评估各种选择。虽然早期人工智能在世界建模方面的尝试难以扩展，但深度学习的兴起重新燃起了人们的兴趣。

目前，大型语言模型 (LLM) 似乎依赖于“启发式方法的集合”——不相关的经验法则——而不是连贯的世界模型。虽然有效，但这些启发式方法缺乏鲁棒性，一个大型语言模型在面临微小扰动时无法重新规划路线就证明了这一点。

世界模型的关键优势在于其潜在的鲁棒性，使人工智能能够进行推理、避免幻觉并变得更易于解释。研究人员正在探索创建世界模型的各种方法，包括多模态训练数据和新型人工智能架构。文章总结说，虽然创建世界模型的道路尚不确定，但其潜在益处使其成为一项值得追求的事业。

---

## 50. 中土世界

**原文标题**: The Middle Earth

**原文链接**: [https://www.historytoday.com/archive/out-margins/real-middle-earth](https://www.historytoday.com/archive/out-margins/real-middle-earth)

伊莉诺·帕克的《今日历史》（2025年9月）刊登的文章《真实的“中土世界”》探讨了“中土世界”一词的现实起源，尽管它与奇幻作品相关。该文章随后以温妮弗雷德·佩克的自传《略知一二：维多利亚时代的童年》为视角，审视了19世纪末英格兰女性教育领域的变化。佩克的经历突显了维多利亚时代僵化的学校（旨在将女性塑造成家庭主妇）与更为进步的学校（为女孩提供与兄弟相似的学术教育，为她们的职业生涯做准备）之间的鲜明对比。该文章强调了一个世纪内女性机会的快速发展，这场变革是佩克那一代人亲身经历的。读者需要订阅《今日历史》才能阅读全文。

---

## 51. 你不是在面试这份工作，而是在试镜这个职位。

**原文标题**: You're Not Interviewing for the Job. You're Auditioning for the Job Title

**原文链接**: [https://idiallo.com/blog/performing-for-the-job-title](https://idiallo.com/blog/performing-for-the-job-title)

本文批判了技术职位面试的表演性，认为面试更注重展示复杂系统和可扩展性的知识，而非实际问题解决和高效方案。作者认为面试已经变成了“选秀”，应聘者被评判的标准是他们讨论理论架构和企业级工具的能力，而不管实际工作是否需要如此复杂性。

本文强调了“面试世界”（复杂性等于能力）和“现实世界”（简约性更有价值）之间的脱节。面试官通常受信号与噪声（复杂性更容易评估）、风险规避（避免假阴性）、期望差距（为未来需求而非当前现实招聘）以及他们自身的智力刺激所驱动。

作者举例说明了诚实、务实的答案反而会受到惩罚，而复杂、戏剧性的回答则更受青睐。然后，他建议如何“赢得游戏”：学习行话，拥抱套路，扮演可扩展系统架构师的角色。关键是，一旦被录用，就要提倡简约，挑战不必要的过度工程。作者认为，最好的方法是玩转面试游戏来获得工作，然后努力拆除在面试过程中被赞扬的过度工程系统。他最后指出，尽管目前的体系存在缺陷，但一些公司已经开始意识到这一点，并正在转向更实际的评估方式。

---

## 52. 德沃夏克与柯蒂键盘的迷思解惑 (2023)

**原文标题**: Untangling the myths and mysteries of Dvorak and QWERTY (2023)

**原文链接**: [https://aresluna.org/the-primitive-tortureboard/](https://aresluna.org/the-primitive-tortureboard/)

破解德沃拉克与QWERTY之谜：一段键盘布局的历史探究

本文《破解德沃拉克与QWERTY之谜》深入探讨了德沃拉克键盘布局相对于无处不在的QWERTY键盘的历史和所谓的优势。文章从乔治·布利肯斯德弗的故事讲起，他在19世纪末创造了“科学”键盘（DHIATENSOR），作为QWERTY的替代品，认为QWERTY效率低下且随意。尽管有其声称的优势，但科学键盘未能获得广泛应用。

文章接着探讨了围绕QWERTY和德沃拉克键盘的常见说法和误解。它驳斥了QWERTY完全是随机的，或者仅仅是为了减慢打字速度而设计的观点，并提出它通过有意的调整演变而来，以防止字杆碰撞。文章还承认QWERTY早于盲打，从而减轻了肖尔斯的（设计）责任。

文章介绍了教育心理学家奥古斯特·德沃拉克，他在20世纪30年代设计了“简化键盘”。 德沃拉克强烈批评QWERTY效率低下且不符合人体工程学。然而，德沃拉克键盘未能克服QWERTY的根深蒂固。

文章暗示了这两种布局背后比简单的好与坏叙事更为复杂的故事，为更深入地探索它们的设计原则和历史背景奠定了基础。

---

## 53. 芝加哥拥有全美最多的铅管。

**原文标题**: Chicago has the most lead pipes in the nation

**原文链接**: [https://grist.org/accountability/chicago-lead-pipe-replacement-map-health/](https://grist.org/accountability/chicago-lead-pipe-replacement-map-health/)

芝加哥铅管危机：黑人和拉丁裔社区首当其冲

---

## 54. 我对2027年人工智能的预测

**原文标题**: My AI Predictions for 2027

**原文链接**: [https://www.lesswrong.com/posts/s64EK3kF9rexntpYm/my-ai-predictions-for-2027](https://www.lesswrong.com/posts/s64EK3kF9rexntpYm/my-ai-predictions-for-2027)

无法访问文章链接。

---

## 55. 多伦多的地下步行隧道网络

**原文标题**: Toronto’s network of pedestrian tunnels

**原文链接**: [https://www.worksinprogress.news/p/torontos-underground-labyrinth](https://www.worksinprogress.news/p/torontos-underground-labyrinth)

本文探讨了多伦多独特的行人隧道网络——Path，这是一个长达30公里的系统，连接市中心的地铁站、铁路线和主要办公楼。Path由企业为了缓解员工通勤和避免拥堵而从20世纪初开始自发发展，现在已成为一个高端的私有购物中心和通勤路线，每天有成千上万的人使用。

与典型的地下通道不同，Path维护良好且安全，尽管自疫情以来其零售业受到了影响。虽然城市规划师经常担心行人隧道会影响街道生活，但作者认为多伦多的人口高密度缓解了这种担忧，因为Path补充了公共交通系统并释放了地面空间。

Path因其独特的经济模式而引人注目，这是一个由独立土地所有者零星创建的综合网络，这对于铁路或公路来说几乎是闻所未闻的。这之所以可行，是因为隧道对单个土地所有者具有很高的价值，并且行人交通具有很高的空间效率。作者认为Path模式有可能在其他城市复制，并引用了蒙特利尔和东京等例子，但质疑为什么它在主要城市中心没有更广泛地普及，并指出潜在的监管限制或独特的经济因素。最终，作者认为行人地铁可以在解决市中心呈现的独特交通问题方面发挥至关重要的作用。

---

## 56. 社交媒体的末日

**原文标题**: The Last Days of Social Media

**原文链接**: [https://www.noemamag.com/the-last-days-of-social-media/](https://www.noemamag.com/the-last-days-of-social-media/)

丹尼尔·巴雷托的文章《社交媒体的末日》认为，由于人工智能生成内容、 “机器人女友经济”的兴起以及用户参与度的下降，社交媒体正在衰落。 社交媒体最初承诺提供真正的连接，但现在充斥着人工智能生成的垃圾信息、诱饵信息和肤浅的内容，难以区分真实和合成材料。

这篇文章强调了“机器人女友经济”的出现，即过度优化且往往与性相关的虚拟形象主导平台，模糊了真实和合成角色之间的界限。 这受到经济不稳定和亲密关系货币化的驱动。

尽管内容泛滥，但由于人们厌倦了在“残渣”（低质量的人工智能生成材料）中筛选，用户参与度正在暴跌。 时间线已经从信息和社交存在的来源转变为情绪调节设备，滚动浏览变成了一种分离形式。

因此，用户正转向更小、更私密的在线空间，如群聊和新闻通讯，优先考虑深度而非规模，并培养信任而非病毒式传播。 尽管大型平台正试图通过强调私人社区和私信来适应，但文章认为注意力经济已经达到了极限，导致疲惫和对真实性的日益渴望。 最终，社交媒体的垂死挣扎将是一种耸肩，因为人们耗尽了他们的关心能力，并选择更刻意和精心策划的在线体验。

---

## 57. 员工们后来吃了它。

**原文标题**: The staff ate it later

**原文链接**: [https://en.wikipedia.org/wiki/The_staff_ate_it_later](https://en.wikipedia.org/wiki/The_staff_ate_it_later)

日语短语“之后工作人员美味地享用了”(この後、スタッフが美味しくいただきました, *Kono ato, sutaffu ga oishiku itadakimashita*)是日本电视节目在介绍食物时显示的字幕，表明拍摄后食物没有被浪费，这在日本文化中备受重视。

据信，该字幕的起源源于观众对电视综艺节目中食物处理不当的投诉。一位电视制片人表示，它最初是在观众抱怨“Downtown no Gaki no Tsukai ya Arahende!!”西瓜表演中浪费食物后使用的。

该说法的真实性存在争议。一些报道支持工作人员确实出于对餐厅的考虑和避免浪费而吃掉剩余食物，参与食品相关电视节目的人员也证实了这种做法。然而，松本人志和北野武等知名人士对此表示怀疑，或指出该说法似乎不太可能的例子，表明食物有时可能会被丢弃。

评论员认为，该字幕是对食品相关争议后观众日益增加的审查的回应。也有人担心这种自我监管可能会扼杀创造力，而且应该由父母而不是电视来教育孩子关于食品伦理。该字幕在其他涉及食物浪费的情况（如西红柿节）中的缺失，突显了其不一致性。

---

## 58. YouTube严打家庭高级账户共享，限“家庭”内使用

**原文标题**: YouTube Is Cracking Down on Sharing Premium Family Accounts Outside 'Household'

**原文链接**: [https://lifehacker.com/tech/youtube-family-premium-crackdown](https://lifehacker.com/tech/youtube-family-premium-crackdown)

YouTube严打与非同住者共享Premium家庭账户行为。Premium家庭套餐允许最多六个账户，每月收费22.99美元，旨在为同一家庭居住者提供服务。尽管该政策自2023年起生效，但YouTube直到最近才开始严格执行。

目前，YouTube正在向被识别为与家庭套餐主账户持有人不同住的用户发送通知。这些用户的Premium权益将在14天后暂停，恢复至广告支持的YouTube，但他们仍将保留在家庭群组中。

YouTube使用每月“签到”系统来验证用户的位置。此签到系统会监控用户是否与账户持有人在同一地点进行流媒体播放。与Netflix的类似系统不同，Netflix每月只需家庭成员登录一次即可，而YouTube的签到似乎是自动化的，并且可能更难规避。虽然确切机制尚不清楚，但如果系统持续检测到用户的主要位置不在家庭住址，那么仅仅偶尔从家庭住址进行流媒体播放可能不足以维持访问权限。

---

## 59. 索引，而非指针

**原文标题**: Indices, not Pointers

**原文链接**: [https://joegm.github.io/blog/indices-not-pointers/](https://joegm.github.io/blog/indices-not-pointers/)

本文提倡在使用Zig等语言实现基于节点的数据结构（如树）时，使用索引而非指针。其核心思想是将节点存储在动态数组（ArrayList）中，而不是单独分配它们。节点之间通过索引（数组位置）而不是内存地址互相引用。

这种方法有以下几个优点：**更小的节点大小**（索引比指针占用更少的内存，特别是对于较小的结构）、**更快的访问速度**（连续的内存布局改善了缓存局部性并减少内存页的使用）、**更少的分配开销**（ArrayList通过超线性增长来最小化开销）和**即时释放**（释放整个结构变成一个单一操作）。

然而，一个缺点是释放单个节点比较困难，因为删除一个节点需要移动后续元素。这可以使用**空闲列表**来缓解，空闲列表跟踪数组中可用的槽位，但这会增加复杂性。

本文提供了一个 Zig 代码示例，演示了如何使用索引来实现树，展示了节点的创建、设置子节点和打印树。该示例使用了 Zig 的内存分配器接口和基于枚举的索引，以确保类型安全。总而言之，当不需要频繁释放单个节点时，使用索引在内存管理和速度方面为基于节点的数据结构提供了显著的性能优势。

---

## 60. 将 BASIC 带回来：微软的 6502 BASIC 现已开源

**原文标题**: Bringing BASIC back: Microsoft's 6502 BASIC is now Open Source

**原文链接**: [https://opensource.microsoft.com/blog/2025/09/03/microsoft-open-source-historic-6502-basic/](https://opensource.microsoft.com/blog/2025/09/03/microsoft-open-source-historic-6502-basic/)

文章《BASIC回归：微软6502 BASIC现已开源》宣布微软已将其6502 BASIC解释器发布为开源软件。这意味着源代码现在可以公开获取，并可以自由使用、修改和分发。

虽然文章标题侧重于BASIC，但也提到了“超光：调试硬件保护的访客”。这表明作者在同一篇文章中讨论了两个不同的主题。“超光”部分描述了一个新功能，该功能允许使用GNU调试器对超光访客微型虚拟机进行交互式调试。

主要的结论是，一款具有历史意义的软件，微软的6502 BASIC（在早期家用电脑上普及），现在可供开发者和爱好者探索、学习并有可能在此基础上进行构建。虽然文章还提到了一个用于微型虚拟机的调试工具，但主要重点是6502 BASIC的开源。

---

## 61. Google Pixel 10系列评测

**原文标题**: Google Pixel 10 series review

**原文链接**: [https://arstechnica.com/gadgets/2025/08/google-pixel-10-series-review-dont-call-it-an-android/](https://arstechnica.com/gadgets/2025/08/google-pixel-10-series-review-dont-call-it-an-android/)

谷歌Pixel 10系列 (Pixel 10, 10 Pro, 10 Pro XL, 和 10 Pro Fold) 在Pixel 9的设计基础上进行了细微改进，依旧采用铝合金和康宁大猩猩玻璃Victus 2。基础款采用哑光边框和亮面背板，而Pro型号则相反，使其略显光滑。该系列取消了SIM卡槽，全面采用eSIM技术。

Pixel 10搭载由台积电制造的全新Tensor G5芯片，CPU性能提升30%。Pro型号配备16GB内存（基础款12GB）、更亮的显示屏和Wi-Fi 7，所有型号均支持Qi2无线充电，兼容MagSafe配件。

该系列引入了基于Android 16的Material 3 Expressive，带来更丰富多彩和可定制的UI，但早期发现了一些软件错误。新增了诸如Magic Cue、Daily Hub和Pixel Journal等AI功能，但其实用性值得怀疑。实时语音翻译是其中一项出色的AI功能。谷歌承诺提供七年的操作系统和安全更新。

尽管CPU性能有所提升，但Tensor G5的GPU性能仍然落后于高通骁龙8 Elite，不过Pixel 10在散热控制方面表现更出色。Pixel 10系列表现良好，但只是渐进式的改进，提供了优化，但并未大胆偏离之前的型号。

---

## 62. Zig Software Foundation 2025 Financial Report and Fundraiser

**原文标题**: Zig Software Foundation 2025 Financial Report and Fundraiser

**原文链接**: [https://ziglang.org/news/2025-financials/](https://ziglang.org/news/2025-financials/)

The Zig Software Foundation (ZSF) released its 2025 financial report and launched a fundraiser, highlighting its efficient use of resources in advancing the Zig programming language. In 2024, ZSF spent $520,748.91, primarily on contractors ($306,362.09) directly contributing to Zig's development at $60/hour. Other expenses included employee salary ($154,263.32), accounting ($18,463.62), CI & Website ($14,986.73), taxes ($13,089.07), travel ($6,955.61), sponsorships ($5,846.24) and bank fees ($782.23).

Major achievements in 2024 included the release of Zig 0.13.0, Zig 0.14.0, greatly expanding target support, and Zig 0.14.1.

While ZSF's income totaled $670,672.59 in 2024, including significant contributions from GitHub Sponsors ($170,656.04), Mitchell Hashimoto ($150,000.00), Every.org ($90,097.45), Bun ($60,000.00), and TigerBeetle ($60,000.00), donation trends show a decline. Simultaneously, user activity is skyrocketing, increasing demand for support and attention. Issue closing times have increased.

To address this, ZSF added Alex Rønne Petersen to the core team, but needs more recurring donations to renew contracts and expand the team. They are appealing for monthly donations, preferably through Every.org, to ensure continued progress on the Zig project and to diversify income sources. They encourage individuals, companies, and venture capitalists to contribute, emphasizing the importance of community support in reaching Zig v1.0.


---

## 63. OpenAI acquires product testing startup Statsig and shakes up leadership team

**原文标题**: OpenAI acquires product testing startup Statsig and shakes up leadership team

**原文链接**: [https://techcrunch.com/2025/09/02/openai-acquires-product-testing-startup-statsig-and-shakes-up-its-leadership-team/](https://techcrunch.com/2025/09/02/openai-acquires-product-testing-startup-statsig-and-shakes-up-its-leadership-team/)

生成摘要时出错

---

## 64. Vijaye Raji to become CTO of Applications with acquisition of Statsig

**原文标题**: Vijaye Raji to become CTO of Applications with acquisition of Statsig

**原文链接**: [https://openai.com/index/vijaye-raji-to-become-cto-of-applications-with-acquisition-of-statsig/](https://openai.com/index/vijaye-raji-to-become-cto-of-applications-with-acquisition-of-statsig/)

生成摘要时出错

---

## 65. Computing simplified coverage polygons

**原文标题**: Computing simplified coverage polygons

**原文链接**: [https://www.volkerkrause.eu/2025/08/30/simplified-coverage-polygons.html](https://www.volkerkrause.eu/2025/08/30/simplified-coverage-polygons.html)

生成摘要时出错

---

## 66. Anthropic raises $13B Series F

**原文标题**: Anthropic raises $13B Series F

**原文链接**: [https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation)

生成摘要时出错

---

## 67. Show HN: LightCycle, a FOSS game in Rust based on Tron

**原文标题**: Show HN: LightCycle, a FOSS game in Rust based on Tron

**原文链接**: [https://github.com/Tortured-Metaphor/LightCycle](https://github.com/Tortured-Metaphor/LightCycle)

生成摘要时出错

---

## 68. Run Erlang/Elixir on Microcontrollers and Embedded Linux

**原文标题**: Run Erlang/Elixir on Microcontrollers and Embedded Linux

**原文链接**: [https://www.grisp.org/software](https://www.grisp.org/software)

生成摘要时出错

---

## 69. Still Asking: How Good Are Query Optimizers, Really? [pdf]

**原文标题**: Still Asking: How Good Are Query Optimizers, Really? [pdf]

**原文链接**: [https://www.vldb.org/pvldb/vol18/p5531-viktor.pdf](https://www.vldb.org/pvldb/vol18/p5531-viktor.pdf)

生成摘要时出错

---

## 70. Python has had async for 10 years – why isn't it more popular?

**原文标题**: Python has had async for 10 years – why isn't it more popular?

**原文链接**: [https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html](https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html)

生成摘要时出错

---

## 71. CauseNet: Towards a causality graph extracted from the web

**原文标题**: CauseNet: Towards a causality graph extracted from the web

**原文链接**: [https://causenet.org/](https://causenet.org/)

生成摘要时出错

---

## 72. The Little Book of Linear Algebra

**原文标题**: The Little Book of Linear Algebra

**原文链接**: [https://github.com/the-litte-book-of/linear-algebra](https://github.com/the-litte-book-of/linear-algebra)

生成摘要时出错

---

## 73. Google gets off easy in the most significant monopoly case since Microsoft trial

**原文标题**: Google gets off easy in the most significant monopoly case since Microsoft trial

**原文链接**: [https://www.zdnet.com/article/google-gets-off-easy-in-the-most-significant-monopoly-case-since-microsoft-trial/](https://www.zdnet.com/article/google-gets-off-easy-in-the-most-significant-monopoly-case-since-microsoft-trial/)

生成摘要时出错

---

## 74. Apertus 8B and 70B – a new open multilingual LLM from Switzerland

**原文标题**: Apertus 8B and 70B – a new open multilingual LLM from Switzerland

**原文链接**: [https://actu.epfl.ch/news/apertus-a-fully-open-transparent-multilingual-lang/](https://actu.epfl.ch/news/apertus-a-fully-open-transparent-multilingual-lang/)

生成摘要时出错

---

## 75. Amazon must face US nationwide class action over third-party sales

**原文标题**: Amazon must face US nationwide class action over third-party sales

**原文链接**: [https://www.reuters.com/legal/government/amazon-must-face-us-nationwide-class-action-over-third-party-sales-2025-09-02/](https://www.reuters.com/legal/government/amazon-must-face-us-nationwide-class-action-over-third-party-sales-2025-09-02/)

生成摘要时出错

---

## 76. An LLM is a lossy encyclopedia

**原文标题**: An LLM is a lossy encyclopedia

**原文链接**: [https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/](https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/)

生成摘要时出错

---

## 77. Making Minecraft Spherical

**原文标题**: Making Minecraft Spherical

**原文链接**: [https://www.bowerbyte.com/posts/blocky-planet/](https://www.bowerbyte.com/posts/blocky-planet/)

生成摘要时出错

---

## 78. Removing Guix from Debian

**原文标题**: Removing Guix from Debian

**原文链接**: [https://lwn.net/SubscriberLink/1035491/d8100135a8ae4246/](https://lwn.net/SubscriberLink/1035491/d8100135a8ae4246/)

生成摘要时出错

---

## 79. 并行AI智能体是游戏规则改变者。

**原文标题**: Parallel AI agents are a game changer

**原文链接**: [https://morningcoffee.io/parallel-ai-agents-are-a-game-changer.html](https://morningcoffee.io/parallel-ai-agents-are-a-game-changer.html)

Igor Šarčević's article discusses parallel AI agents and their transformative impact on software development. He notes that parallel AI agents, unlike previous AI-assisted coding tools, represent a fundamental shift in how software is built. He chronicles the evolution of AI-assisted coding from GitHub Copilot to AI-powered editors to "vibe coding," where AI generates code from natural language descriptions. The key innovation is the ability to run multiple AI agents concurrently, each working on different parts of a project, such as UI, API endpoints, and database schemas. This parallelization accelerates development significantly.

The author highlights GitHub's Co-Pilots as an early solution, where issues are assigned to AI agents who create pull requests for review. This shifts the engineer's role to providing context, guiding the agents, and reviewing their code. He recommends preparing issues with sufficient context, assigning them to agents in batches, reviewing locally, and maintaining flow between reviews.

Šarčević also addresses the mental model shifts required, emphasizing orchestration over precision, asynchronous workflows, and batch thinking. He provides realistic success rate expectations and outlines areas where parallel agents excel (bug fixes, backend logic) and struggle (new UI development). Critical skills like full-stack understanding, problem decomposition, writing, and QA/code review become more important.

Finally, he emphasizes the importance of a fast CI/CD pipeline, system documentation, preview environments, and monorepo architectures to support parallel agent workflows, along with listing development tools like GitHub Agents and Cursor that are adapting to this new paradigm.


---

## 80. OpenMeter (YC W23) Acquired by Kong

**原文标题**: OpenMeter (YC W23) Acquired by Kong

**原文链接**: [https://konghq.com/blog/news/kong-acquires-openmeter](https://konghq.com/blog/news/kong-acquires-openmeter)

生成摘要时出错

---

## 81. Matrix.org service offline: corrupted database

**原文标题**: Matrix.org service offline: corrupted database

**原文链接**: [https://status.matrix.org](https://status.matrix.org)

生成摘要时出错

---

## 82. Finnish City Inaugurates 1 MW/100 MWh Sand Battery

**原文标题**: Finnish City Inaugurates 1 MW/100 MWh Sand Battery

**原文链接**: [https://cleantechnica.com/2025/08/30/finnish-city-inaugurates-1-mw-100-mwh-sand-battery/](https://cleantechnica.com/2025/08/30/finnish-city-inaugurates-1-mw-100-mwh-sand-battery/)

生成摘要时出错

---

## 83. Show HN: Amber – better Beeper, a modern all-in-one messenger

**原文标题**: Show HN: Amber – better Beeper, a modern all-in-one messenger

**原文链接**: [https://useamber.app/](https://useamber.app/)

生成摘要时出错

---

## 84. What happens during startup?

**原文标题**: What happens during startup?

**原文链接**: [https://eclecticlight.co/2025/08/29/what-happens-during-startup/](https://eclecticlight.co/2025/08/29/what-happens-during-startup/)

生成摘要时出错

---

## 85. Light Sleep: Waking VMs in 200ms with eBPF and snapshots

**原文标题**: Light Sleep: Waking VMs in 200ms with eBPF and snapshots

**原文链接**: [https://www.koyeb.com/blog/scale-to-zero-wake-vms-in-200-ms-with-light-sleep-ebpf-and-snapshots](https://www.koyeb.com/blog/scale-to-zero-wake-vms-in-200-ms-with-light-sleep-ebpf-and-snapshots)

生成摘要时出错

---

## 86. Take something you don’t like and try to like it

**原文标题**: Take something you don’t like and try to like it

**原文链接**: [https://dynomight.net/liking/](https://dynomight.net/liking/)

生成摘要时出错

---

## 87. Show HN: Moribito – A TUI for LDAP Viewing/Queries

**原文标题**: Show HN: Moribito – A TUI for LDAP Viewing/Queries

**原文链接**: [https://github.com/ericschmar/moribito](https://github.com/ericschmar/moribito)

生成摘要时出错

---

## 88. You are a good person if

**原文标题**: You are a good person if

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2025/09/02/you-are-a-good-person.html](https://geohot.github.io//blog/jekyll/update/2025/09/02/you-are-a-good-person.html)

生成摘要时出错

---

## 89. Keyboards from my collection (2023)

**原文标题**: Keyboards from my collection (2023)

**原文链接**: [https://aresluna.org/50-keyboards-from-my-collection/](https://aresluna.org/50-keyboards-from-my-collection/)

生成摘要时出错

---

## 90. Show HN: We built an open-source alternative to expensive pair programming apps

**原文标题**: Show HN: We built an open-source alternative to expensive pair programming apps

**原文链接**: [https://github.com/gethopp/hopp](https://github.com/gethopp/hopp)

生成摘要时出错

---

## 91. Condor's Cuzco RISC-V Core at Hot Chips 2025

**原文标题**: Condor's Cuzco RISC-V Core at Hot Chips 2025

**原文链接**: [https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot](https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot)

生成摘要时出错

---

## 92. Scientists design superdiamonds with predicted hexagonal crystal structure

**原文标题**: Scientists design superdiamonds with predicted hexagonal crystal structure

**原文链接**: [https://phys.org/news/2025-08-scientists-superdiamonds-theoretically-hexagonal-crystal.html](https://phys.org/news/2025-08-scientists-superdiamonds-theoretically-hexagonal-crystal.html)

生成摘要时出错

---

## 93. What brain surgery taught me about the fragile gift of consciousness

**原文标题**: What brain surgery taught me about the fragile gift of consciousness

**原文链接**: [https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/](https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/)

生成摘要时出错

---

## 94. Quirks of Common Lisp Types

**原文标题**: Quirks of Common Lisp Types

**原文链接**: [https://www.fosskers.ca/en/blog/cl-type-quirks](https://www.fosskers.ca/en/blog/cl-type-quirks)

生成摘要时出错

---

## 95. Is the Bubble Bursting?

**原文标题**: Is the Bubble Bursting?

**原文链接**: [https://www.honest-broker.com/p/is-the-bubble-bursting](https://www.honest-broker.com/p/is-the-bubble-bursting)

生成摘要时出错

---

## 96. Eternal Struggle

**原文标题**: Eternal Struggle

**原文链接**: [https://yoavg.github.io/eternal/](https://yoavg.github.io/eternal/)

生成摘要时出错

---

## 97. Writing a Hypervisor in 1k Lines

**原文标题**: Writing a Hypervisor in 1k Lines

**原文链接**: [https://seiya.me/blog/hypervisor-in-1000-lines](https://seiya.me/blog/hypervisor-in-1000-lines)

生成摘要时出错

---

## 98. Reusing Computation in Text-to-Image Diffusion for Efficient Image Generation

**原文标题**: Reusing Computation in Text-to-Image Diffusion for Efficient Image Generation

**原文链接**: [https://arxiv.org/abs/2508.21032](https://arxiv.org/abs/2508.21032)

生成摘要时出错

---

## 99. Next.js is infuriating

**原文标题**: Next.js is infuriating

**原文链接**: [https://blog.meca.sh/3lxoty3shjc2z](https://blog.meca.sh/3lxoty3shjc2z)

生成摘要时出错

---

## 100. WinBoat: Run Windows apps on Linux with seamless integration

**原文标题**: WinBoat: Run Windows apps on Linux with seamless integration

**原文链接**: [https://github.com/TibixDev/winboat](https://github.com/TibixDev/winboat)

生成摘要时出错

---

