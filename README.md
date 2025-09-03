# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-03.md)

*最后自动更新时间: 2025-09-03 17:46:13*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 2 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 3 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 4 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 5 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 6 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 7 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 8 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 9 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 10 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 11 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 12 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 13 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 14 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 15 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 16 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 17 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 18 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 19 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 20 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 21 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 22 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 23 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 24 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 25 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 26 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 27 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 28 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 29 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 30 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 31 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 32 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 33 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 34 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 35 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 36 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 37 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 38 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 39 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 40 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 41 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 42 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 43 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 44 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 45 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 46 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 47 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 48 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 49 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 50 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 51 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 52 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 53 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 54 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 55 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 56 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 57 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 58 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 59 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 60 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 61 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 62 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 63 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 64 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 65 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 66 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 67 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 68 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 69 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 70 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 71 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 72 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 73 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 74 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 75 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 76 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 77 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 78 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 79 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 80 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 81 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 82 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 83 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 84 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 85 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 86 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 87 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 88 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 89 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 90 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 91 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 92 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 93 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 94 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 95 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 96 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 97 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 98 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 99 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 100 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 101 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 102 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 103 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 104 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 105 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 106 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 107 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 108 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 109 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 110 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 111 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 112 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 113 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 114 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 115 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 116 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 117 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 118 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 119 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 120 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 121 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 122 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 123 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 124 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 125 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 126 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 127 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 128 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 129 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 130 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 131 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 132 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 133 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 134 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 135 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 136 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 137 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 138 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 139 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 140 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 141 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 142 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 143 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 144 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 145 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 146 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 147 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 148 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 149 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 150 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 151 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 152 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 153 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 154 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 155 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 156 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 157 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 158 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 159 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 160 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 161 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 162 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 163 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 164 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 165 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 166 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 167 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 168 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
