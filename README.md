# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-17.md)

*最后自动更新时间: 2025-11-17 17:51:23*
## 1. 展示一下：我为女儿做了一个合成器

**原文标题**: Show HN: I built a synth for my daughter

**原文链接**: [https://bitsnpieces.dev/posts/a-synth-for-my-daughter/](https://bitsnpieces.dev/posts/a-synth-for-my-daughter/)

这个“Show HN”帖子详细讲述了一位创客为女儿三岁生日制作便携式步进音序合成器的过程。受女儿对蒙特梭利板上的开关和旋钮的喜爱启发，他旨在创造一个触觉和创造性的音乐玩具。

他从Arduino Inventors Kit开始，逐步在面包板上构建了一个基本的MIDI控制器。然后，他集成了一个SAM2695合成器模块和一个用于视觉反馈的小型OLED屏幕，包括一只跳舞的熊猫。开发过程得到了Wokwi微控制器模拟器的帮助。

面对现有外壳的挑战，他学习了CAD并3D打印了一个定制外壳。最初，他在可焊接面包板上手工接线电路，但在遇到脆弱性问题后，转而使用Fusion 360设计定制PCB。他通过切换到带有Adafruit Miniboost的三节电池设置来解决了电源问题。

最终的合成器有四个滑块控制循环序列中的音符，节奏/音量/音阶/音高控制，以及一个定制外壳。女儿喜欢使用它，创作者注意到了一些需要改进的地方，例如屏幕延迟，并计划升级到ESP32。

他正在考虑将该项目转化为真正的产品的潜力，但也承认存在监管、财务和制造方面的障碍。他正在考虑开源设计供创客使用，或者发起Kickstarter活动，并向有小型硬件生产经验的人寻求建议。

---

## 2. 谷歌正在扼杀开放网络，第二部分

**原文标题**: Google is killing the open web, part 2

**原文链接**: [https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/](https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/)

无法访问文章链接。

---

## 3. Replicate 加入 Cloudflare

**原文标题**: Replicate is joining Cloudflare

**原文链接**: [https://replicate.com/blog/replicate-cloudflare](https://replicate.com/blog/replicate-cloudflare)

Replicate，一个通过API分享和运行AI模型的平台，将加入Cloudflare。根据公告，Replicate将作为一个独立的品牌运营，但会受益于Cloudflare的资源和更快的基础设施。现有的API和已部署的模型将继续像以前一样运行。

此次收购是受构建AI应用的基础设施的共同愿景驱动。Replicate在定义模型标准（使用Cog）和创建模型部署平台方面的工作被视为基础原语，类似于云中AI的分布式操作系统。Cloudflare强大的网络，包括Workers、Durable Objects和R2等产品，被视为AI基础设施的互补组件。

目标是构建更高层次的AI抽象，促进模型编排、实时推理和边缘部署。Replicate选择Cloudflare是因为其以开发者为中心的方法以及在构建强大的企业业务方面的成功。正如Cloudflare是Web应用程序开发的默认选择一样，两者的结合旨在成为构建AI应用程序的默认平台。

---

## 4. FreeMDU：开源Miele电器诊断工具

**原文标题**: FreeMDU: Open-source Miele appliance diagnostic tools

**原文链接**: [https://github.com/medusalix/FreeMDU](https://github.com/medusalix/FreeMDU)

FreeMDU：通过光学诊断接口与Miele电器通信的开源软硬件工具

---

## 5. 双子座计划

**原文标题**: Project Gemini

**原文链接**: [https://geminiprotocol.net/](https://geminiprotocol.net/)

双子星计划旨在创建轻量级在线空间，用于互联文本文档，优先考虑读者隐私、注意力和带宽。 它被描述为一个永恒的概念，不一定是创新或颠覆性的，而是从互联网过度颠覆中提供喘息之机。 Gemini的重点是文档就是文档，不旨在改变世界或破坏现有技术。 该文本鼓励读者探索官方资源，包括常见问题解答、视频概述、新闻、文档、历史记录和与该项目相关的已知软件。 最后，它声明 geminiprotocol.net 上的所有内容均已获得 CC BY-NC-ND 4.0 许可。

---

## 6. WBlock：一款Safari的新广告拦截器

**原文标题**: WBlock: A New Ad-Blocker for Safari

**原文链接**: [https://github.com/0xCUB3/wBlock](https://github.com/0xCUB3/wBlock)

WBlock：一款适用于macOS、iOS和iPadOS的全新免费开源Safari广告拦截器。它利用Safari的声明式内容拦截API实现高效性能，空闲时仅占用约40MB内存。它使用Protocol Buffers和LZ4压缩进行存储。

主要功能包括五个Safari扩展中75万条规则容量、支持AdGuard语法的自定义过滤规则列表，以及实现Greasemonkey API的用户脚本引擎。用户还可以使用元素移除功能手动删除元素（仅限macOS）。

WBlock提供全面的拦截功能，包括网络请求拦截、Cookie和本地存储过滤、CSS注入、脚本拦截以及弹窗/重定向阻止。用户可以配置自动更新间隔、管理白名单并使用区域过滤支持。

技术架构强调性能，采用异步I/O、流式序列化并遵循Web标准。它还使用`SafariConverterLib`和`AdGuard Scriptlets`进行规则转换和高级拦截。

常见问题解答涵盖了常见问题，重点介绍了WBlock的性能优势、自定义过滤规则列表支持、iOS上的用户脚本功能、可配置的更新频率以及与其他广告拦截器（如uBlock Origin Lite、AdGuard和Wipr）的比较。

---

## 7. 凯尔特密码：用Python绘制结

**原文标题**: Celtic Code: Drawing Knots with Python

**原文链接**: [https://2earth.github.io/website/20250202.html](https://2earth.github.io/website/20250202.html)

本文“凯尔特密码：用Python绘制绳结”详细介绍了Tom Ruddell的项目，该项目旨在创建一个用Python以编程方式生成凯尔特绳结的Web应用程序。文章首先简要概述了凯尔特民族、他们的历史以及绳结在其文化中的重要性，并指出绳结在不同社会和时期的实用性和象征意义。

文章的核心随后转向绳结生成器的编码技术过程。Ruddell概述了所涉及的步骤，首先创建网格（瓦片和屏障数组）以定义绳结的结构。他解释了如何放置屏障以引导绳结的路径，以及如何使用相邻屏障的数量来确定每个瓦片的类型（角、直、弯曲、对角）。程序使用罗盘系统计算每个瓦片的入口和出口方向。一个关键的挑战是放置弯曲瓦片，这涉及到确定它们的手性，并使用查找表来找到正确的入口/出口点。

最后，程序使用Pillow库绘制图形，创建线条笔触以产生视觉效果。程序识别交叉点并应用“上跨”，以创建凯尔特绳结特有的交织外观，每个“上跨”部分绘制两次。作者在承认该方法存在局限性的同时，强调了它的简单性和有效性。文章提供了Web应用程序和源代码的链接。

---

## 8. Ned：带GL Shader的ImGui文本编辑器

**原文标题**: Ned: ImGui Text Editor with GL Shaders

**原文链接**: [https://github.com/nealmick/ned](https://github.com/nealmick/ned)

Ned：一款复古风格、功能丰富的文本编辑器，使用Dear ImGui构建，既可独立使用，也可嵌入到其他ImGui应用程序中。它拥有用于视觉定制的OpenGL着色器效果，包括静态噪声、烧录、屏幕曲率、辉光和渐晕，并提供Amber和Solarized等主题。

主要功能包括支持超过15种语言的Tree Sitter语法高亮、用于高级语言支持的LSP集成（clangd、gopls、pyright、TypeScript）、基于suckless st.c的终端模拟器，以及可选的自定义词法分析器。Ned支持多光标编辑、文本书签，以及通过OpenRouter实现的类似Copilot的自动补全，利用各种LLM。独特的“彩虹模式”光标有助于提高可见性。

该项目适用于macOS（Intel/ARM）、Windows x64和Debian。Windows支持仍在测试中。提供了针对每个平台的构建说明，包括依赖管理。Ned可以使用ned_embed库嵌入到其他ImGui应用程序中，从而添加文件浏览、终端、表情符号支持、主题和其他功能。

Ned还拥有一个利用OpenRouter和专用模型（Morph）的AI代理，用于快速准确的代码编辑，并支持多光标功能以实现高效的文本操作。

---

## 9. WeatherNext 2: 我们最先进的天气预报模型

**原文标题**: WeatherNext 2: Our most advanced weather forecasting model

**原文链接**: [https://blog.google/technology/google-deepmind/weathernext-2/](https://blog.google/technology/google-deepmind/weathernext-2/)

WeatherNext 2：谷歌最新AI天气预报模型，更快、更准、更高分辨率的全球预测

谷歌DeepMind和Google Research推出的最新AI天气预报模型WeatherNext 2，提供更快、更准、更高分辨率的全球天气预测。它使用单个TPU在一分钟内生成数百种可能的天气情景，在99.9%的变量和提前期上显著优于之前的WeatherNext模型。

一项关键创新是功能生成网络（FGN）架构，该架构注入“噪声”以产生物理上真实且相互关联的预测，尤其适用于预测复杂的天气系统。

WeatherNext 2数据现在可通过Earth Engine和BigQuery访问。此外，Google Cloud的Vertex AI上提供早期访问计划，用于自定义模型推理。谷歌已将WeatherNext技术集成到搜索、Gemini、Pixel Weather和Google Maps Platform的天气API中，并计划将其纳入Google Maps。

谷歌旨在通过提供强大的工具和开放数据，帮助研究人员、开发者和企业解决复杂问题，并推动天气预报领域的未来创新。他们正在积极研究进一步改进模型的方法，包括整合新的数据源和扩大访问范围。

---

## 10. SIP、ICE、TURN及相关协议的C++实现

**原文标题**: C++ implementation of SIP, ICE, TURN and related protocols

**原文链接**: [https://github.com/resiprocate/resiprocate](https://github.com/resiprocate/resiprocate)

本文档介绍了reSIProcate项目，这是一个实现了SIP、ICE、TURN及相关协议的C++库和应用程序集合。关键组件包括：

*   **resip库：** 一个全面的SIP协议栈（RFC3261）。
*   **dum库：** 一个用于用户代理的高级SIP库（无媒体）。
*   **recon库：** 一个集成了媒体堆栈的高级SIP UA库。
*   应用程序：SIP代理（rePro），STUN/TURN服务器（reTurn），保持音乐服务器（MOHParkServer），以及一个B2BUA服务器（reConServer）。
*   **reTurn库：** STUN/TURN客户端。
*   **tfm库：** 一个基于SIP的SIP框架。

本文档提供了在*nix和Windows系统上构建项目的详细CMake说明。在*nix系统上，它概述了内部构建和外部构建过程、单元测试以及必需/可选的软件包。在Windows系统上，它涵盖了使用Visual Studio GUI和CMake命令行进行构建，包括使用sipXtapi媒体支持进行构建的具体说明。它还解释了如何通过Visual Studio GUI 使用Ninja构建系统。

本文档强调使用CMake变量来配置构建选项（例如，启用c-ares支持），并涉及创建安装包等未来考虑事项。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 2 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 3 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 4 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 5 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 6 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 7 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 8 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 9 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 10 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 11 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 12 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 13 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 14 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 15 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 16 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 17 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 18 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 19 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 20 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 21 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 22 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 23 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 24 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 25 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 26 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 27 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 28 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 29 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 30 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 31 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 32 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 33 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 34 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 35 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 36 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 37 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 38 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 39 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 40 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 41 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 42 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 43 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 44 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 45 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 46 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 47 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 48 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 49 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 50 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 51 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 52 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 53 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 54 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 55 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 56 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 57 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 58 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 59 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 60 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 61 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 62 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 63 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 64 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 65 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 66 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 67 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 68 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 69 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 70 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 71 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 72 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 73 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 74 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 75 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 76 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 77 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 78 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 79 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 80 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 81 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 82 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 83 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 84 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 85 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 86 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 87 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 88 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 89 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 90 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 91 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 92 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 93 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 94 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 95 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 96 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 97 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 98 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 99 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 100 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 101 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 102 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 103 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 104 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 105 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 106 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 107 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 108 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 109 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 110 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 111 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 112 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 113 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 114 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 115 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 116 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 117 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 118 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 119 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 120 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 121 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 122 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 123 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 124 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 125 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 126 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 127 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 128 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 129 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 130 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 131 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 132 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 133 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 134 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 135 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 136 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 137 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 138 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 139 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 140 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 141 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 142 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 143 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 144 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 145 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 146 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 147 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 148 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 149 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 150 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 151 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 152 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 153 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 154 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 155 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 156 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 157 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 158 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 159 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 160 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 161 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 162 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 163 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 164 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 165 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 166 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 167 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 168 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 169 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 170 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 171 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 172 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 173 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 174 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 175 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 176 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 177 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 178 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 179 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 180 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 181 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 182 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 183 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 184 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 185 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 186 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 187 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 188 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 189 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 190 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 191 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 192 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 193 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 194 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 195 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 196 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 197 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 198 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 199 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 200 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 201 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 202 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 203 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 204 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 205 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 206 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 207 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 208 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 209 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 210 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 211 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 212 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 213 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 214 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 215 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 216 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 217 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 218 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 219 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 220 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 221 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 222 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 223 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 224 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 225 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 226 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 227 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 228 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 229 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 230 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 231 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 232 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 233 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 234 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 235 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 236 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 237 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 238 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 239 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 240 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 241 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 242 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
