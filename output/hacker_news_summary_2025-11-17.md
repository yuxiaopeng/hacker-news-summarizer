# Hacker News 热门文章摘要 (2025-11-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: 用于 OpenGL (Three.js) 的反向透视相机

**原文标题**: Show HN: Reverse perspective camera for OpenGL (Three.js)

**原文链接**: [https://github.com/bntre/reverse-perspective-threejs](https://github.com/bntre/reverse-perspective-threejs)

这个“Show HN”帖子介绍了一种自定义的OpenGL投影矩阵（在Three.js中实现），它可以在直接透视、正交投影和反向透视视图之间平滑过渡。这会产生一种激进的视觉效果，类似于但比推拉变焦更极端。

关键思想是基于单条投影光线的倾斜角 (p) 来操纵视锥体的形状。正 'p' 产生直接透视，'p=0' 产生正交投影，负 'p' 产生反向透视。重要的是，相机位置变得不那么重要；视锥体的变换才是关键。

在近裁剪面和远裁剪面之间引入了一个“焦点平面”，在投影变化期间保持恒定大小。假定相机位于此焦点平面的中心，并且 'p' 是通过 (1, 0, 0) 的投影光线角度的正切值，以此定义投影矩阵。

该帖子提供了投影矩阵的具体形式，并链接到 GitHub 存储库中的 `updateProjectionMatrix()` 函数以获取实现细节。它还引用了 Song Ho Ahn 关于投影矩阵的文章以获取更多信息。 演示、视频和存储库链接都包含在内。演示使用了 Three.js 示例中的动画模型（Michelle 和 Littlest Tokyo），但并未直接将模型包含在存储库中；它们是在运行时加载的。

---

## 12. 使用 Terraform 在 AWS ECS 上部署 Temporal

**原文标题**: Deploying Temporal on AWS ECS with Terraform

**原文链接**: [https://papnori.github.io/posts/temporal-ecs-terraform/](https://papnori.github.io/posts/temporal-ecs-terraform/)

本文全面介绍了如何使用 Terraform 在 AWS ECS（Elastic Container Service）上部署 Temporal workers，提供了一种经济高效且可扩展的 Kubernetes 替代方案。它强调使用 ECS 与 Fargate 进行无服务器容器管理，在保持弹性和可靠性的同时，可降低约 70% 的基础设施成本。

本指南涵盖了关键的架构组件，例如 VPC（Virtual Private Cloud）、子网（公共和私有）、VPC 终端节点、互联网网关、NAT 网关、Amazon ECR（Elastic Container Registry）、AWS Secrets Manager、ECS 集群和 Fargate 以及用于可观测性和自动扩展的 Amazon CloudWatch。它还解释了数据如何在系统中流动，从客户端触发到任务执行和监控。

该设置包括将 Temporal Cloud 或自托管的 Temporal Server 凭证安全地存储在 AWS Secrets Manager 中，并利用 Terraform 进行基础设施管理。Terraform 项目结构被组织成 `bootstrap`、`global`、`live` 和 `modules` 目录。自动扩展通过 CloudWatch 警报根据 CPU 使用率进行配置。本文重点介绍了该架构的优势，包括弹性、安全性、成本效益、可扩展性和可维护性。最后，本文列出了设置的先决条件，并指导用户完成整个过程。

---

## 13. 使用全新命令编辑器编写 Chrome Devtools Protocol (CDP) 命令

**原文标题**: Craft Chrome Devtools Protocol (CDP) commands with the new command editor

**原文链接**: [https://developer.chrome.com/blog/cdp-command-editor](https://developer.chrome.com/blog/cdp-command-editor)

本文介绍新的 Chrome DevTools 协议 (CDP) 命令编辑器，旨在简化在 Chrome DevTools 中直接编写和发送 CDP 命令的过程。CDP 允许开发者远程调试并与正在运行的 Chrome 浏览器进行交互。

新编辑器的主要优势包括：

*   **自动补全：** 提供可用 CDP 命令的建议。
*   **参数自动填充：** 自动显示所选命令的必需和可选参数，无需查阅 CDP 文档。
*   **简化参数输入：** 为枚举和布尔值提供下拉菜单，并允许轻松添加和删除数组及对象参数。
*   **内联文档：** 将鼠标悬停在命令或参数上时，会显示描述和指向在线文档的链接。
*   **实时错误检查：** 如果输入的参数值类型不正确，会立即提供反馈。
*   **修改和重发：** 允许快速修改和重新发送先前执行的命令。
*   **复制为 JSON：** 提供一键将 CDP 命令复制为 JSON 字符串的方式。

新编辑器旨在简化使用 CDP 的工作流程，使其更易于访问和更高效，方便开发者测试和控制 Chrome 浏览器行为。DevTools 团队鼓励用户提供反馈和功能请求。

---

## 14. 赋予C语言超能力

**原文标题**: Giving C a Superpower

**原文链接**: [https://hwisnu.bearblog.dev/giving-c-a-superpower-custom-header-file-safe_ch/](https://hwisnu.bearblog.dev/giving-c-a-superpower-custom-header-file-safe_ch/)

本文介绍了`safe_c.h`，一个自定义的C头文件，旨在将C++和Rust中的安全性和便利性功能引入C编程。它解决了常见的C语言缺陷，如内存泄漏、缓冲区溢出和复杂的错误处理。

该头文件利用编译器特定的清理属性提供RAII（资源获取即初始化）语义，确保即使在提前返回或发生错误时也能释放资源。它引入了“智能指针”，如用于自动内存管理的`UniquePtr`和用于线程安全共享资源并具有自动引用计数的`SharedPtr`。

为了解决缓冲区溢出问题，`safe_c.h`实现了类型安全、自动增长的向量以及非拥有的字符串视图和跨度。向量自动管理动态数组的内存，而视图和跨度提供对子字符串或数组切片的零成本引用，避免了不必要的分配。

本文还介绍了受Rust启发的`Result`类型来解决C语言混乱的错误处理问题，强制进行显式错误处理。与RAII结合使用，简化了清理工作并防止了资源泄漏。通过`requires()`和`ensures()`实现的契约使函数的前提条件和后置条件显式且可验证。最后，它用更安全、边界检查的替代方案取代了不安全的函数（如`strcpy`），以防止缓冲区溢出。作者强调，`safe_c.h`赋予了C语言开发者更高的安全性和现代化的功能，同时保持了该语言的灵活性和性能。本文通过作者构建的高性能grep克隆程序`cgrep`的经验突出了这些优势。

---

## 15. 构建一个有效的简易搜索引擎

**原文标题**: Building a Simple Search Engine That Works

**原文链接**: [https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works](https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works)

无法访问文章链接。

---

## 16. 2025年，我沉浸在Sun Microsystems生态系统中，享受着美好生活

**原文标题**: Living my best Sun Microsystems ecosystem life in 2025

**原文链接**: [https://www.osnews.com/story/143570/living-my-best-sun-microsystems-ecosystem-life-in-2025/](https://www.osnews.com/story/143570/living-my-best-sun-microsystems-ecosystem-life-in-2025/)

本文详细介绍了作者对2000年代末Sun Microsystems生态系统的深深着迷，以及他获取并修复Sun Ultra 45工作站（一台2006年的双UltraSPARC IIIi机器）的过程。他遗憾错过了在Sun鼎盛时期充分体验其生态系统的机会，并计划在2025年重现那种体验。

作者收到的Ultra 45是KDE e.V.董事会成员Adriaan de Groot慷慨捐赠的，他感谢Adriaan和KDE的这份礼物。这台机器是一台独特的预生产型号，以前由KDE用于Solaris开发。作者概述了对Ultra 45进行的初步升级，包括添加第二个处理器并将RAM升级到8GB。他详细介绍了RAM兼容性方面面临的挑战以及使用Sun品牌内存的必要性。

本文还将Ultra 45与其前身Sun Blade 2500进行了比较，突出了相对适度的升级以及SPARC工作站技术错过了一次更重大进步的机会。尽管年代久远，作者对使用这台机器探索Sun生态系统感到兴奋，特别是计划安装Sun Flash Accelerator卡和SunPCi IIIpro卡，以便在Solaris中运行Windows。他很欣赏其独特的历史和一些小细节，例如“KDE project”贴纸，这些都使他的预生产Ultra 45变得特别。

---

## 17. 异端：用于语言模型的自动审查移除

**原文标题**: Heretic: Automatic censorship removal for language models

**原文链接**: [https://github.com/p-e-w/heretic](https://github.com/p-e-w/heretic)

Heretic：一种自动去除Transformer语言模型审查的工具，无需大量后续训练。它利用增强型定向消融技术（abliteration）与基于TPE的参数优化器（Optuna）来实现这一点。该过程完全自动化，旨在最大限度地减少对“有害”提示的拒绝，并最大限度地减少与原始模型的KL散度，从而保留模型的原始智能。

Heretic的无监督操作可与手动创建的abliteration质量相媲美，在实现类似拒绝抑制的同时，具有更低的KL散度，表明对模型能力的损害更小。它支持大多数密集模型和各种MoE架构。使用方法简单，只需一个Python环境和一个简单的`pip install`命令即可。

核心创新在于参数化的定向消融。该工具识别Transformer层中的相关矩阵，并根据从“有害”和“无害”提示之间的均值差异计算出的“拒绝方向”对它们进行正交化。优化参数控制消融权重核的形状和位置，从而实现高度灵活的方法来改善合规性/质量权衡。浮点拒绝方向索引的使用允许在方向之间进行线性插值，从而扩大了最佳性能的搜索空间。消融参数也针对每个组件（注意力/MLP）独立选择。

虽然承认先前在abliteration技术上的研究，但Heretic是从头开始编写的。该工具以GNU Affero通用公共许可证授权。

---

## 18. 二十年未破解的文件格式

**原文标题**: A file format uncracked for 20 years

**原文链接**: [https://landaire.net/a-file-format-uncracked-for-20-years/](https://landaire.net/a-file-format-uncracked-for-20-years/)

作者详细描述了他们尝试逆向工程 Xbox 原版《细胞分裂》(2002) 中使用的 .lin 文件格式的过程，该格式在 20 年来一直未被破解。出于探索被删减内容的渴望，他们备份了游戏光盘并开始分析 .lin 文件。

作者最初识别了 .lin 文件的基本结构，注意到 zlib 压缩的数据块和一个潜在的文件表。他们成功编写了一个工具来解压缩这些文件，并发现了与纹理和缓冲区相关的数据大小。然而，在尝试解析文件表时遇到了困难，该文件表似乎包含大量具有错误偏移量的文件。

通过在 xemu 模拟器中调试游戏，作者找到了负责文件打开、读取和解压缩的函数。他们发现游戏以 0x4000 字节的块线性读取数据，忽略 seek 命令，使得 .lin 格式更像是一个线性数据流。进一步的调查显示，虚幻引擎包文件按顺序存在。

核心问题仍然是文件表及其差异。作者得出结论，要正确读取文件，必须假设没有 seek 操作，并解决偏移量问题，这可能与运行时数据的加载和管理方式有关。

---

## 19. 通过Postgres WAL监听数据库变更

**原文标题**: Listen to Database Changes Through the Postgres WAL

**原文链接**: [https://peterullrich.com/listen-to-database-changes-through-the-postgres-wal](https://peterullrich.com/listen-to-database-changes-through-the-postgres-wal)

本文探讨了如何使用预写式日志(WAL)监听Postgres数据库中的更改，以此作为`pg_notify`的替代方案，因为在高吞吐量数据库中，`pg_notify`可能会成为性能瓶颈。

WAL记录了每次数据库更改，从而实现复制、备份和变更数据捕获(CDC)等功能。要将WAL用于CDC，必须将`wal_level`设置为`logical`，这将以高级格式存储更改，但可能会产生更多开销。

本文介绍了Publication，它指定要跟踪哪些表和操作（插入、更新、删除）。创建复制槽是为了为监听器维护一个单独的WAL副本，确保不会丢失数据。临时复制槽在监听器断开连接时会自动删除，从而避免磁盘空间问题，但如果监听器离线，可能会错过事件。持久复制槽保证不会丢失数据，但只允许一个连接。

本文提供了用于创建publication和持久复制槽的迁移代码片段。创建这两者需要在单独的迁移中完成。第一个创建定义要监听哪些表的publication，第二个为监听器创建一个命名复制槽。

---

## 20. Fastmcpp (C++ 快速 MCP)

**原文标题**: Fastmcpp (Fastmcp for C++)

**原文链接**: [https://github.com/0xeb/fastmcpp](https://github.com/0xeb/fastmcpp)

Fastmcpp 是模型上下文协议 (MCP) 的高性能 C++ 实现，镜像了 Python fastmcp 库的功能。它支持工具管理、资源处理、提示和 JSON Schema 验证等核心 MCP 功能，使其适用于构建具有原生性能的 MCP 服务器和客户端。

Fastmcpp 提供多种传输层，包括 STDIO、HTTP (SSE) 和 WebSocket，并包含用于请求/响应处理的中间件。它具有跨平台性，支持 Windows、Linux 和 macOS。

构建 fastmcpp 需要 C++17 编译器、CMake 3.20+ 和 nlohmann/json 库（自动获取）。可选依赖项包括 libcurl（用于 HTTP POST 流）、cpp-httplib 和 easywsclient（用于 HTTP/WebSocket 服务器和客户端）。该项目提供了演示基本用法的示例，例如创建 STDIO 和 HTTP 服务器，以及 HTTP 客户端。

项目结构包括带有公共头文件的 include 目录、一个源目录、一个基于 GoogleTest 的测试套件和示例程序。欢迎贡献，指南强调通过测试、遵守代码风格和更新文档。它采用 Apache 2.0 许可，贡献可以通过 Github issue tracker 进行。当前版本为 2.13.0，被认为是 Beta 版本。

---

## 21. PicoIDE – 一个开源 IDE/ATAPI 驱动器模拟器

**原文标题**: PicoIDE – An open IDE/ATAPI drive emulator

**原文链接**: [https://picoide.com/](https://picoide.com/)

PicoIDE是由Ian Scott创建的开源硬件和固件项目，用于模拟IDE/ATAPI设备。它既可以作为ATAPI CD-ROM模拟器，也可以作为IDE固定硬盘模拟器。PicoIDE支持CD-ROM的多种镜像格式（.bin/.cue或.iso）以及硬盘的多种镜像格式（.img/.hda/.vhd/.hdf）。它具有通过3.5毫米插孔和MPC-2接头实现的内置CD音频输出功能。

该设备支持PIO模式0-4和多字DMA模式0-2进行数据传输。此外，还可以选择前面板或3.5英寸驱动器托架外壳，其中包括一个1.3英寸OLED屏幕（128x64）、四向导航按钮、用于远程控制和镜像管理的WiFi连接以及RGB活动指示灯。

---

## 22. 在浏览器中运行的1961年继电器计算机

**原文标题**: A 1961 Relay Computer Running in the Browser

**原文链接**: [https://minivac.greg.technology/](https://minivac.greg.technology/)

本网页展示了一款基于浏览器的Minivac 601模拟器，这是一款最初于1961年发布的基于继电器的模拟计算机。该模拟器允许用户直接在其网络浏览器中与该历史计算设备的虚拟版本进行交互。这意味着用户可以了解并实验早期计算技术中存在的计算逻辑和机器学习原理的基础知识，而无需访问实物Minivac 601。本页面建议使用桌面视图，表明该模拟器目前可能尚未针对移动设备进行完全优化。因此，主要目的是提供围绕模拟的1961年继电器计算机为中心的、易于访问的交互式学习体验。

---

## 23. “小型”开源的命运

**原文标题**: The fate of "small" open source

**原文链接**: [https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)

诺兰·劳森反思大型语言模型（LLM）对开源生态系统的影响，特别是像他自己的`blob-util`这样“小型、低价值”库的命运。他指出，LLM现在可以轻松地为常见任务生成代码，从而减少对此类库及其相关依赖项的需求。

劳森承认这种转变的潜在好处，例如更快的开发和更强大的代码。然而，他也感叹教育方面的损失。像`blob-util`这样的库通常是学习工具，教开发者超越解决特定问题的基本JavaScript概念。他还质疑仅将文档放在LLM的llms.txt文件中有什么价值。

他认为，虽然LLM正在使某些类型的开源项目过时，特别是实用程序库，但它们并没有完全否定对开源的需求。他提出，开源的未来在于更大、更复杂、更小众的项目，这些项目LLM无法轻易复制。他以他在内存泄漏检测方面的工作为例，说明了新颖的研究和创造性技术仍然至关重要的有价值的领域。

劳森仍然保持乐观，强调尽管LLM精通现有的JavaScript框架，但新的JavaScript框架仍在不断开发。他总结说，LLM已经重塑了格局，但在开源世界中仍然有充足的创新和贡献机会，特别是对于那些突破界限并需要人类创造力的项目。

---

## 24. 我终于理解了Cloudflare Zero Trust 隧道。

**原文标题**: I finally understand Cloudflare Zero Trust tunnels

**原文链接**: [https://david.coffee/cloudflare-zero-trust-tunnels](https://david.coffee/cloudflare-zero-trust-tunnels)

本文阐述了 Cloudflare Zero Trust 隧道和 Warp，并将其与 Tailscale 进行对比，概述了它们的优势，例如连接私有网络、公开或私有地暴露服务以及添加精细的访问控制。文章阐明了 Cloudflared（隧道创建）和 Warp Client（客户端连接和策略执行）的角色。

核心概念围绕隧道（由 Cloudflared 创建的网络入口/出口点）、路由（将流量导向特定隧道，从而通过 Warp 实现私有网络访问）和目标（定义受保护的基础设施，从而启用访问策略）展开。作者以暴露 Home Assistant 实例为例来说明这些概念。 通过指向 Argo 隧道的 DNS 记录启用公共访问。 通过 Warp 路由实现私有网络访问（例如，192.168.1.3），这需要 Warp 客户端连接。

访问策略对于定义谁可以访问受保护的资源至关重要。 作者演示了如何要求特定的登录方法，或在通过 Warp 连接时绕过登录。

最后，本文介绍了 Warp 客户端的部署和注册，重点介绍了用于控制客户端行为的设置，包括允许的用户、登录方法和协议设置。 关键是 Warp 身份验证身份设置，允许为已注册的用户绕过登录屏幕。 作者强调了保护注册策略的重要性。

---

## 25. 你现在可以在亚马逊上购买二手福特汽车了。

**原文标题**: You can now buy pre-owned Ford vehicles on Amazon

**原文链接**: [https://www.theverge.com/news/821258/ford-amazon-auto-online-sales-certified-preowned](https://www.theverge.com/news/821258/ford-amazon-auto-online-sales-certified-preowned)

福特现已在亚马逊新推出的在线汽车购买网站Amazon Autos上销售认证二手车，成为继现代之后第二个入驻该平台的品牌。从今天开始，洛杉矶、西雅图和达拉斯的客户可以在线浏览、融资和购买这些车辆，并在当地福特经销商处提货。

与现代最初更广泛的发布不同，福特的销售最初仅限于这三个城市，但亚马逊预计很快会扩展。福特经销商将保留对定价、服务和交付的控制权，亚马逊的角色定位为连接客户与这些经销商的中间人。亚马逊旨在通过提供访问其超过3.1亿活跃用户的庞大用户群来吸引经销商。

在亚马逊上销售的车辆均为认证二手车，并享有福特的保修、道路救援和福特奖励积分。福特强调，所有列出的车辆都经过了检查和翻新。

此举旨在改善购车体验，因为许多人觉得传统的经销商体验令人沮丧。这与特斯拉开创的直销模式（DTC）形成对比，后者绕过了经销商。然而，许多州的法律限制制造商直接向消费者销售，尽管这种情况正在开始改变。

---

## 26. 实用程序员：20周年纪念版 (2023)

**原文标题**: The Pragmatic Programmer: 20th Anniversary Edition (2023)

**原文链接**: [https://www.ahalbert.com/technology/2023/12/19/the_pragmatic_programmer.html](https://www.ahalbert.com/technology/2023/12/19/the_pragmatic_programmer.html)

阿芒·哈尔伯特评述《程序员修炼之道》20周年纪念版，强调其对现代软件工程师的持续价值。本书面向初学者和指导新人的资深开发者，提供适用于软件开发及其他领域的实用建议。

哈尔伯特强调了本书的结构，特别是便于参考的、附在实体书上的简洁“提示”。他总结了前三章的关键概念。第一章强调责任、适应性和持续学习，突出沟通的重要性以及解决代码中的“破窗效应”。第二章侧重于实用方法，如 DRY（不要重复自己）原则、正交性以及使用示踪弹进行迭代开发。他对“没有最终决定”的提示略有异议，告诫人们不要过度抽象。第三章涵盖了基本工具和调试策略，提倡使用纯文本存储知识、精通命令行 shell，以及像“二分法”这样的系统调试技术。第四章从软件不可能完美这一理念出发，介绍了契约式设计。

总而言之，该评论将本书定位为适合所有阶段软件工程师的宝贵资源，为高效和负责任的软件开发提供实用的建议和永恒的原则。

---

## 27. 为什么嘉实多本田超级摩托车在（多数）现代系统上崩溃

**原文标题**: Why Castrol Honda Superbike crashes on (most) modern systems

**原文链接**: [https://seri.tools/blog/castrol-honda-superbike/](https://seri.tools/blog/castrol-honda-superbike/)

本文详细介绍了作者对1998年PC游戏《嘉实多本田超级摩托车世界冠军赛》的调试过程。该游戏在现代Windows系统上崩溃，但在Windows 98和XP等旧系统上运行良好。

作者发现崩溃源于游戏DirectInput设备枚举代码中的缓冲区溢出漏洞。游戏仅为8个DirectInput设备分配空间，但会枚举连接到系统的所有设备（键盘、鼠标、LED控制器等）。当设备数量超过8个时，游戏会越界写入，破坏内存并导致崩溃。

作者确定了DirectInput使用的易受攻击的回调函数，并查明了溢出发生的特定代码行。文章强调，游戏只需要DirectInput用于操纵杆，一个简单的修复方法是过滤设备枚举，仅包括操纵杆。

为了解决这个问题，作者创建了一个自定义DLL垫片，拦截`DirectInputCreateA`函数。然后，该垫片修改了对`EnumDevices`的调用，以仅过滤操纵杆类型的设备，并将处理的操纵杆数量限制为8个。这可以防止缓冲区溢出，并使游戏能够在现代系统上正确运行。

作者还深入研究了极限优化技术，以最大限度地减小垫片DLL的大小，重点介绍了用于实现最终大小仅为2 KiB的各种编译器和链接器标志。文章配套的Github页面上提供了预编译的DLL。作者没有解决游戏中True Color渲染问题。

---

## 28. 基于FPGA的IBM-PC-XT

**原文标题**: FPGA Based IBM-PC-XT

**原文链接**: [https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/](https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/)

本文详细介绍了一个使用FPGA和新旧组件混合重建IBM-PC-XT的业余项目，其目标是运行EGA版本的《猴岛小英雄1》。该项目利用了低功耗NEC V20 CPU、1MB SRAM以及icesugar-pro FPGA板。定制硬件包括用于键盘和鼠标的PS/2接口、用于固定磁盘访问的Micro SD卡、用于Adlib音频的YM3014B DAC以及压电扬声器。

作者描述了开发过程，从用Verilog实现的V20 CPU总线控制器开始。他们讨论了内存管理方案，包括将BIOS加载到FPGA块RAM中，并使用单独的块RAM作为显存。一个关键的挑战是实现通过SPI控制器和option ROM进行固定磁盘访问，以处理BIOS INT13H调用，以及在软件中模拟系统。

作者通过在FPGA内创建PS/2到串行鼠标桥接器来解决PS/2鼠标支持问题，并使用逻辑分析仪捕获来理解PS/2协议。通过模拟硬盘寻道声音并集成Jose Tejada的开源YM3812实现Adlib音频（并将其馈送到YM3014 DAC）来增强音频效果。该项目包括对CGA和EGA图形、USB到UART桥接器以及定制丙烯酸面板外壳的支持。源代码、原理图和Gerber文件可在GitHub上找到。

---

## 29. 神经科学家追踪“顿悟”背后的神经活动

**原文标题**: Neuroscientists track the neural activity underlying an “aha”

**原文链接**: [https://www.quantamagazine.org/how-your-brain-creates-aha-moments-and-why-they-stick-20251105/](https://www.quantamagazine.org/how-your-brain-creates-aha-moments-and-why-they-stick-20251105/)

本文探讨了“顿悟”时刻或洞察力背后的神经科学原理，以及它们如何增强记忆力。神经科学家马克西·贝克尔使用穆尼图像（高对比度、模糊的图片）和功能磁共振成像技术来追踪这些时刻的大脑活动。研究表明，当参与者正确识别出图像中隐藏的物体时，特别是当这种体验感觉确定且情绪积极时，腹侧枕颞皮层（VOTC）、杏仁核和海马体的活动会增加。海马体，被称为大脑的“失配探测器”，在识别图像从无意义到有意义的转变中起着关键作用。

该研究还调查了“顿悟-记忆优势”，发现参与者能够更好地记住他们有过顿悟时刻的穆尼图像。最初顿悟期间VOTC和海马体活动的增加预示着更好的记忆保持。这表明，顿悟期间显著的大脑活动使体验更加突出，从而导致在长期记忆中更好地编码。

虽然顿悟会产生更强的记忆，但文章指出它们并不总是正确的，参与者即使错误地识别图像也会体验到“顿悟”时刻。文章最后讨论了理解顿悟的潜在应用，特别是在教育和理解创造力方面。研究人员于玉华正在探索顿悟在创造力和其他领域中的作用，如心理治疗、冥想和迷幻体验。总体目标是了解如何利用顿悟来改善学习和创造性问题解决。

---

## 30. Python中的Z3 API：20行内搞定数独到N皇后问题 (2015)

**原文标题**: Z3 API in Python: From Sudoku to N-Queens in Under 20 Lines (2015)

**原文链接**: [https://ericpony.github.io/z3py-tutorial/guide-examples.htm](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)

本文是一篇关于在 Python 中使用 Z3 API (Z3Py) 的教程，Z3Py 是来自微软研究院的高性能定理证明器。它涵盖了 Z3Py 的基础知识，包括创建整数、实数和布尔变量，定义约束以及使用 `solve` 函数查找解决方案。本教程还介绍了如何简化公式、遍历表达式以及处理任意大的数字、有理数和无理代数数。

它演示了如何使用 `set_option` 配置 Z3 环境，并强调了常见的错误，例如将 Python 整数视为 Z3 有理数。然后，本教程探讨了布尔逻辑，展示了诸如 `And`、`Or`、`Not`、`Implies` 和 `If` 等运算符。

关于求解器的章节解释了 Z3 求解器 API，包括添加约束、检查可满足性 (`check`) 以及使用 `push` 和 `pop` 管理断言。它还涵盖了遍历约束、收集性能统计信息以及使用 `model()` 检查模型。

详细介绍了算术能力，包括整数到实数的自动强制转换以及使用 `simplify` 函数进行的简化转换。本文介绍了用于机器算术的位向量，并涵盖了有符号/无符号运算符，如 `ULT`、`ULE`、`UGT`、`UGE`、`UDiv`、`URem` 和 `LShR`。

最后，本教程介绍了未解释的函数和常量，说明了如何在约束求解中定义和使用它们，以及使用 `evaluate` 方法在模型中评估表达式。本教程旨在为解决各种问题的 Z3Py 核心功能提供全面的介绍。

---

## 31. 傅里叶变换

**原文标题**: Fourier Transforms

**原文链接**: [https://www.continuummechanics.org/fourierxforms.html](https://www.continuummechanics.org/fourierxforms.html)

对傅里叶变换(FFT)应用和解读的批判性审视：以旋转机械或轮胎等周期性数据为例。作者认为FFT常被误用和误解，导致错误的结论。

核心观点是，FFT本质上是一个曲线拟合过程，具体来说，是对给定数据集进行正弦和余弦函数的多变量线性回归。因此，不应将其视为具有“神秘能力”来揭示隐藏真相的工具。仅仅因为FFT在特定频率上产生谐波，并不意味着该对象实际上在该频率上振动。

作者使用一个简单的线性回归例子（用直线拟合二次函数）来说明曲线拟合结果如何容易产生误解。然后，他解释了FFT的数学基础，强调了计算每个谐波的幅度和相位滞后的关键公式。

文章展示了几个例子，包括正弦波等基本函数的FFT。这些例子表明，如果数据不包含整数个周期，或者在信号末尾添加了“零”，则FFT结果可能复杂且具有误导性。文章强调了理解FFT局限性的重要性，并在解释结果时考虑完整的时域信号。忽略相位滞后信息也被指出是误解的潜在来源。总而言之，要谨慎和批判性地使用FFT，将其视为一种曲线拟合形式，而不是神奇的洞察力产生器。

---

## 32. 你是否陷入了电影逻辑？

**原文标题**: Are you stuck in movie logic?

**原文链接**: [https://usefulfictions.substack.com/p/are-you-stuck-in-movie-logic](https://usefulfictions.substack.com/p/are-you-stuck-in-movie-logic)

无法访问文章链接。

---

## 33. 深湖的混合是其命脉，火山口湖的混合正在减缓。

**原文标题**: Mixing Is the Heartbeat of Deep Lakes. At Crater Lake, It's Slowing Down

**原文链接**: [https://www.quantamagazine.org/mixing-is-the-heartbeat-of-deep-lakes-at-crater-lake-its-slowing-down-20251114/](https://www.quantamagazine.org/mixing-is-the-heartbeat-of-deep-lakes-at-crater-lake-its-slowing-down-20251114/)

本文探讨了深水湖泊混合减缓的现象，并以俄勒冈州的火山口湖为例。湖泊混合是一个由风、温度和盐度驱动的关键过程，如同心脏跳动，将氧气和养分分布到整个水体中。然而，气候变化，伴随着气温升高和夏季延长，正在扰乱这一过程。

在火山口湖，科学家观察到湖水变得更加清澈，但这反常地表明存在问题。较暖的表层水温导致较薄的暖水层，减少浮游植物种群，从而提高水的透明度。更重要的是，本文详细说明了较暖的夜晚正在削弱夏季的浅层混合，而较暖的冬季正在减少将湖水混合到底部的逆层化过程。这些变化导致分层现象，阻止氧气和养分的分布。

本文强调了长期数据集的重要性，例如火山口湖自1886年以来的数据，以便了解这些变化。在意大利湖泊中也观察到了类似的混合问题，底部缺氧已经改变了生物群落。火山口湖就像“煤矿里的金丝雀”，让研究人员可以研究气候变化对湖泊物理的影响，并有可能减轻后果。科学家们现在强调需要采取合作的方式来研究全球湖泊，因为混合减少的影响可能导致鱼类死亡、藻类大量繁殖和入侵物种。

---

## 34. GCC 16 考虑将默认标准更改为 C++20

**原文标题**: GCC 16 considering changing default to C++20

**原文链接**: [https://inbox.sourceware.org/gcc/aQj1tKzhftT9GUF4@redhat.com/](https://inbox.sourceware.org/gcc/aQj1tKzhftT9GUF4@redhat.com/)

GCC 16 可能将默认语言标准更改为 C++20 的探讨。

---

## 35. 应用让美国移民及海关执法局追踪全国车辆和车主

**原文标题**: App Lets ICE Track Vehicles and Owners Across the Country

**原文链接**: [https://www.404media.co/this-app-lets-ice-track-vehicles-and-owners-across-the-country/](https://www.404media.co/this-app-lets-ice-track-vehicles-and-owners-across-the-country/)

一款名为“移动伴侣”的新应用允许移民及海关执法局 (ICE) 官员即时扫描车牌，并将它们添加到包含全国各地车辆位置信息的数十亿条记录数据库中。这些数据来源于摩托罗拉解决方案和汤森路透，可以与驾驶执照信息、信用头数据、结婚记录、车辆所有权详情和选民登记信息相结合，使 ICE 能够预测车辆动向并收集面部扫描信息用于面部识别。

该应用与名为“车辆管理器”的桌面应用程序集成，用于分析和管理车牌数据。摩托罗拉通过其 Vigilant Solutions 和 Digital Recognition Network (DRN) 子公司，使用固定和移动摄像头（包括从收车人员处众包的摄像头）来收集车牌数据。汤森路透的 CLEAR 平台利用全面的公共和专有信息来丰富这些数据，尽管他们声称“移动伴侣”与 CLEAR 无关。

虽然汤森路透将 CLEAR 定位于解救被绑架儿童和抓捕罪犯等用途，但它并未强调 ICE 将其用于驱逐出境工作。ICE 继续花费数百万美元从汤森路透购买车牌读取器数据，以协助逮捕和没收资产。国土安全部 (DHS) 和摩托罗拉均未回复置评请求。

---

## 36. 关键磷酸铁锂专利到期，电动汽车电池迎来新篇章。

**原文标题**: A new chapter begins for EV batteries with the expiry of key LFP patents

**原文链接**: [https://www.shoosmiths.com/insights/articles/a-new-chapter-begins-for-ev-batteries-with-the-expiry-of-key-lfp-patents](https://www.shoosmiths.com/insights/articles/a-new-chapter-begins-for-ev-batteries-with-the-expiry-of-key-lfp-patents)

磷酸铁锂电池关键专利于2022年到期，为电动汽车市场打开了大门，使这种经济高效、安全且毒性较低的电池技术得以更广泛地应用。 特斯拉最初引领了这一趋势，而磷酸铁锂的采用正在整个西方市场加速，并在可再生能源存储领域也获得了关注。

然而，这并非完全自由。 虽然核心的磷酸铁锂化学成分现在是公开的，但各公司正在围绕能量密度提升、安全性改进和快速充电能力等二次创新申请专利。 宁德时代、比亚迪和特斯拉等公司在该领域拥有相关专利。 进入该领域的公司面临着与添加剂、涂层和生产方法相关的二次专利侵权风险，因此需要进行谨慎的运营自由度（FTO）分析。

除了专利之外，仍然存在挑战。 磷酸铁锂电池较低的材料价值给回收带来挑战，特别是考虑到即将出台的欧盟法规要求回收锂含量。 西方制造商也严重依赖中国供应商的关键材料和制造技术。 此外，充电站等基础设施需要改进，以促进电动汽车的普及。

专利到期标志着创新新阶段的开始。 竞争优势现在在于进一步的技术进步，这需要战略性专利和商业秘密保护，以及战略伙伴关系。 电动汽车公司将不得不应对一个有效的知识产权保护策略是成功的关键的局面。

---

## 37. Supercookie：通过网站图标进行浏览器指纹识别 (2021)

**原文标题**: Supercookie: Browser Fingerprinting via Favicon (2021)

**原文链接**: [https://github.com/jonasstrehle/supercookie](https://github.com/jonasstrehle/supercookie)

本文描述了一种名为“超级Cookie”的新型浏览器指纹识别技术，该技术利用网站图标（favicon）为网站访问者创建一个持久且难以清除的唯一标识符。与使用Cookie的传统跟踪方法不同，此方法利用浏览器的网站图标缓存（F-Cache），并绕过常见的反跟踪措施，如隐身模式、VPN、广告拦截器和清除浏览器数据。

该技术通过利用浏览器请求网站图标的方式来工作。如果特定URL路径的网站图标不在F-Cache中，浏览器会向服务器请求。通过策略性地传递或不传递不同子路径的网站图标，服务器可以根据请求了哪些网站图标，为每个浏览器创建一个唯一的模式（超级Cookie）。该模式可以在后续访问中重建，即使在清除Cookie和使用隐私工具后也能识别用户。

本文重点介绍了Chrome、Firefox、Safari和Edge等主流浏览器（包括其移动版本）的漏洞。它解释了如何扩展攻击以区分大量用户。目前的缓解策略包括手动删除网站图标缓存文件。作者强调，演示和源代码仅用于教育目的，旨在提高人们对基于网站图标的跟踪可能性的认识。该项目已引起多家科技新闻媒体和安全专家的关注。

---

## 38. 我有录音证明Coinbase在披露前数月就知道违规行为。

**原文标题**: I have recordings proving Coinbase knew about breach months before disclosure

**原文链接**: [https://jonathanclark.com/posts/coinbase-breach-timeline.html](https://jonathanclark.com/posts/coinbase-breach-timeline.html)

2025年1月，作者遭遇了一起复杂的诈骗，攻击者掌握了详细的个人信息，包括社保号码和准确的比特币余额，这表明Coinbase发生了数据泄露。作者立即向Coinbase报告了该事件，并提供了钓鱼邮件的详细技术分析，包括可疑的邮件头，表明邮件源自亚马逊SES而非Coinbase的安全渠道，以及欺诈电话的录音。尽管Coinbase承认该报告“非常有力”，但却未调查或回应作者关于攻击者如何获取其敏感数据的关键问题。

四个月后，即2025年5月，Coinbase公开披露了一起数据泄露事件，网络罪犯贿赂了印度TaskUs的海外客户支持承包商，以窃取客户数据。泄露的信息包括姓名、地址、社保号码数字、身份证、账户余额和交易历史。Coinbase估计财务影响为1.8亿至4亿美元。

作者认为，Coinbase在公开披露前几个月就知道该漏洞，因为他们1月份的经历和随后的报告提供了具体证据，表明被盗数据正在被积极使用。作者批评Coinbase外包安全敏感职位、未能更早地发现漏洞、对用户报告的回复不足以及可能延迟披露。作者还强调了诈骗的复杂性，包括使用Google Voice号码、试图让作者将资金转移到Coinbase Wallet，以及使用短信轰炸来隐藏安全警报。

---

## 39. Anthropic 的论文闻起来像坨屎。

**原文标题**: Anthropic’s paper smells like bullshit

**原文链接**: [https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/](https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/)

该文章批评了人工智能研究公司Anthropic最近发布的一份报告，该报告声称一个中国官方背景的组织（GTG-1002）利用他们的AI助手Claude进行渗透测试，实施了一起所谓的网络间谍活动。作者“djnn”认为，该报告缺乏关键的技术细节和可验证的证据，使其对于旨在检测或预防类似攻击的安全专业人员毫无用处。

核心的抱怨是缺乏入侵指标（IoCs）、战术、技术和程序（TTPs）以及其他具体的标记，这些本可以帮助安全团队验证声明并保护他们的网络。作者发现诸如Claude独立执行80-90%战术行动之类的说法毫无根据，并质疑所使用的工具、提取的数据类型以及受影响系统的性质。

“djnn”强调，在没有提供支持细节的情况下将行为归因于中国官方背景的组织是不负责任的，并可能产生外交影响。他们怀疑该报告的主要目的是为了推广Anthropic的AI驱动的安全解决方案，并特别指出了鼓励安全团队“尝试应用AI进行防御”的结尾段落。

总而言之，作者认为该报告是“可悲的借口”和“无耻的推销产品的行为”，缺乏提供可操作情报的伦理考量，并且依赖炒作而非实质。“djnn”呼吁业界要求科技公司提高标准，尤其是在网络安全报告中提供基于事实的证据和可验证的信息方面。

---

## 40. AirPods挣脱了苹果生态

**原文标题**: AirPods libreated from Apple's ecosystem

**原文链接**: [https://github.com/kavishdevar/librepods](https://github.com/kavishdevar/librepods)

LibrePods：旨在解锁AirPods在非苹果设备上的全部潜力，尤其是在安卓和Linux系统上。它允许用户访问通常锁定在苹果生态系统中的功能，例如噪声控制模式、入耳检测、电池状态和可定制的通透模式。

目前，AirPods Pro (第二代) 得到完全支持，而其他型号的功能支持程度各不相同。该软件提供诸如重命名AirPods和修改长按操作等自定义选项。诸如助听器自定义和多设备连接等一些高级功能，需要通过模拟苹果设备ID来实现蓝牙设备识别 (DID) 钩子。

在安卓系统上，由于蓝牙协议栈问题，LibrePods通常需要已root的设备并安装Xposed框架才能运行，不过ColorOS/OxygenOS 16用户无需root即可访问基本功能。DID钩子通过Xposed启用。该项目正在积极开发中，新的Linux版本也在开发中。

要点包括：

*   **将AirPods功能引入安卓和Linux。**
*   **安卓系统上通常需要root才能实现全部功能。**
*   **提供噪声控制、入耳检测、电池状态等功能。**
*   **通过蓝牙DID钩子提供高级功能。**
*   **根据GNU GPL v3许可证免费开源。**

---

## 41. 俄罗斯“匕首”导弹速度太快无法拦截，乌克兰用音乐干扰

**原文标题**: Russia's Kinzhal Missiles Are Too Fast to Shoot, So Ukraine Jams Them with Music

**原文链接**: [https://www.trenchart.us/p/to-jam-russias-mach-57-kinzhal-missiles](https://www.trenchart.us/p/to-jam-russias-mach-57-kinzhal-missiles)

乌克兰干扰“匕首”导弹的新策略：用爱国歌曲误导导航

---

## 42. 布兰妮·斯皮尔斯半导体物理指南 (2000)

**原文标题**: Britney Spears' Guide to Semiconductor Physics (2000)

**原文链接**: [https://britneyspears.ac/lasers.htm](https://britneyspears.ac/lasers.htm)

名为“布兰妮·斯皮尔斯半导体物理学指南”的网页，是对物理教育的一种讽刺或幽默解读，以流行歌星布兰妮·斯皮尔斯为半导体物理学专家的名义呈现。 隐含且极有可能的是，布兰妮·斯皮尔斯与该内容毫无关系。

该网站涵盖半导体物理学的基本主题，包括：

*   **半导体基础：** 晶体结构、半导体结以及量子阱等概念。
*   **辐射复合与载流子传输：** 半导体中与光发射相关的重要过程。
*   **态密度：** 理解半导体内部能级的关键概念。
*   **激光技术：** 特别是边发射激光器和垂直腔表面发射激光器 (VCSEL)。
*   **光子晶体：** 用于控制光传播的先进结构。
*   **半导体制造：** 晶体生长、制造、光刻和加工技术。

该网站还包括补充材料，如科学计算器、“半导体术语唇彩词汇表”、布兰妮·斯皮尔斯主题壁纸，以及图片库、歌词、聊天和“布兰妮八卦”等其他部分的链接。

该网站实际上是为物理系学生设计的 Splung.com Physics 网站的一部分，作者正在寻找合作者来扩展该网站的互动组件。 语气轻松活泼，可能旨在通过与流行偶像的出人意料的联系来吸引学生，同时呈现事实信息。

---

## 43. 暗黑模式游戏

**原文标题**: Dark Pattern Games

**原文链接**: [https://www.darkpattern.games](https://www.darkpattern.games)

恶意游戏设计利用刻意操控的设计选择，在让玩家遭受负面影响的同时，使游戏开发者获益。这些并非无意的设计缺陷，而是旨在利用玩家心理的有目的的策略。其核心原则是欺骗或迫使玩家采取他们可能不愿采取的行动，例如花费真金白银、游戏时间超出预期或与他人分享游戏。

这些策略可以表现为多种形式。例如，利用人为稀缺性来制造错失恐惧症（FOMO），实施欺骗性定价策略，使游戏内购买看起来比实际更容易或更必要，以及掩盖有关游戏进展所涉及的真实成本或时间投入的重要信息。本质上，游戏开发者使用这些设计技巧来最大限度地提高利润或参与度，但代价是玩家的乐趣，甚至可能是财务健康。

---

## 44. C#中寻找许可宽松的PDF库

**原文标题**: Quest for Permissively Licensed PDF Library in C#

**原文链接**: [https://duerrenberger.dev/blog/2025/11/04/quest-for-permissively-licensed-pdf-library-in-csharp/](https://duerrenberger.dev/blog/2025/11/04/quest-for-permissively-licensed-pdf-library-in-csharp/)

本文详细介绍了作者寻找一个不依赖完整浏览器引擎的、许可证宽松的 C# PDF 渲染库的探索过程。作者强调了 PDF 创建中布局和样式设计的难度，这通常导致人们使用像 Chromium 这样的浏览器引擎。

文章概述了一个理想的 PDF 解决方案应具备的特性：DOM 表示、布局/样式功能、PDF 格式写入和格式转换。虽然许多库可以写入 PDF，但很少有库在宽松许可下提供布局和样式设计。

QuestPDF 被强调为一个有前景的现代库，其代码采用 MIT 许可证，但项目许可区分了免费和商业用途。

作者随后提供了一个详尽的 PDF 相关库列表，按其功能（DOM、布局、PDF 渲染器、浏览器引擎）进行分类，并附带许可证信息以及是否适合作者的目标。MigraDoc、PdfPig、LiteHtmlSharp、HTML Agility Pack、PDFSharp 以及各种 HTML 到 PDF 转换器等库都经过了评估。

最终，MigraDoc 被确定为最合适的选择，尽管它在高级样式设计和潜在内存使用方面存在局限性。虽然不完美，但它为许多常见的 PDF 导出场景提供了“足够好”的解决方案。作者指出，在开源世界中，令人惊讶地缺乏强大的、许可证宽松的 PDF 渲染竞争者，并表示有兴趣创建胶水代码以促进现有 .NET PDF 库之间的互操作性。

---

## 45. 垃圾回收很有用

**原文标题**: Garbage collection is useful

**原文链接**: [https://dubroy.com/blog/garbage-collection-is-useful/](https://dubroy.com/blog/garbage-collection-is-useful/)

此开发日志讲述了垃圾回收的知识，特别是论文《垃圾回收的统一理论》中的原则，如何被证明在解决与Ohm和ProseMirror增量解析相关的问题中是有用的。

作者正在开发一个系统，该系统需要将ProseMirror中文本文档的编辑与原始文本文档同步，并利用Ohm的增量解析和转换功能。面临的挑战是如何有效地识别编辑后旧解析文档中不再存在的节点，而无需遍历整个文档，否则将抵消增量解析的好处。

最初，该方法模仿追踪垃圾回收，通过迭代整个新文档来识别活动节点，并确定与先前文档节点的差异。然而，受到《垃圾回收的统一理论》的启发，该理论认为追踪和引用计数是对偶方法，作者实现了一种引用计数机制。

他们没有追踪活动对象，而是专注于“反物质”（死亡对象）。在编辑后创建新文档时，旧根节点（以及随后的其子节点）的引用计数会递归地递减。这有效地识别了不再使用的节点，从而可以进行有针对性的更新，而无需遍历整个文档。这种引用计数方法模仿了引用计数垃圾收集器，并成功解决了原始实现中的性能瓶颈。

---

## 46. 用 OCaml 轻松设置 Linux 模式

**原文标题**: Linux mode setting, from the comfort of OCaml

**原文链接**: [https://roscidus.com/blog/blog/2025/11/16/libdrm-ocaml/](https://roscidus.com/blog/blog/2025/11/16/libdrm-ocaml/)

本文介绍 libdrm-ocaml，一个 OCaml 库，它为配置显示设置提供了一个更友好的 Linux 内核模式设置 (KMS) API 接口。作者演示了如何在 REPL (例如 utop) 中以交互方式使用 libdrm-ocaml 来查询和修改显示配置。

本文介绍了发现可用图形设备、列出连接器、CRTC（CRT 控制器）、编码器、帧缓冲和 CRTC 平面等资源的过程。它详细介绍了如何检索有关已连接监视器、支持模式和资源属性的信息。作者解释了这些资源之间的关系，并提供了一个简化的图表以方便理解。

作者展示了如何启用原子模式设置以访问其他属性，并强调了使用 OCaml 的 `Option` 类型处理可选值的重要性。他们还解释了帧缓冲如何向 CRTC 提供图像数据，并简要介绍了 CRTC 平面的概念，该概念允许组合多个帧缓冲进行显示。

本文简要提到了使用非原子和原子模式设置来更改显示配置。它涉及使用“哑缓冲区”，并暗示使用该 API 进行 3D 渲染，表明其具有进行更高级图形操作的潜力。即使对于不熟悉 OCaml 的读者，本文也提供了对底层 KMS API 的深入了解。最后，作者提供了有关如何安装和运行代码示例的说明。

---

## 47. 对 Archive.today 可疑压力的调查

**原文标题**: Our investigation into the suspicious pressure on Archive.today

**原文链接**: [https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html](https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html)

AdGuard DNS调查Archive.today受可疑压力事件。AdGuard收到一个新成立的法国组织Web Abuse Association Defense (WAAD)的联系，对方要求其屏蔽Archive.today，理由是后者拒绝删除非法内容，并威胁将根据法国法律采取法律行动。

AdGuard怀疑存在不正当行为，直接联系了Archive.today，后者迅速删除了引用的内容，并声称从未收到过事先通知。Archive.today还透露存在针对该网站的“连续”投诉模式。

AdGuard对WAAD的调查显示，该组织最近才注册，缺乏实质性的公开信息，且在线存在感极低。此外，WAAD提供的作为证据的“执达吏报告”大多创建于2025年8月，而非声称的2023年。然而，有两份执达吏报告是2023年由某人订购的，此人的名字与Archive.today在2024年写到的人相符。在这种情况下，投诉似乎来自一位真正的律师，但该域名是在发送投诉的同一天注册的，仅包含一个重定向到律师页面的链接。

AdGuard得出结论，针对Archive.today的投诉似乎存在可疑之处，可能涉及冒名顶替。他们正在向法国警方提起正式投诉，理由是根据法国法律对虚假报告的处罚。文章还指出，这些事件发生的时间恰逢FBI对Archive.today进行调查，可能与CSAM有关，但尚未确认直接联系。

---

## 48. 飞行中测量WWVB的多普勒频移

**原文标题**: Measuring the doppler shift of WWVB during a flight

**原文链接**: [https://greatscottgadgets.com/2025/10-31-receiving-wwvb-with-hackrf-pro/](https://greatscottgadgets.com/2025/10-31-receiving-wwvb-with-hackrf-pro/)

本文详细介绍了作者探索使用WWVB 60 kHz时间信号作为频率参考和趣味无线电项目的过程。作者强调了WWVB相对于GPSDO等替代方案的优势，包括其室内可用性和更简单的设计。他还讨论了使用HackRF Pro进行此项目的优势，特别是其TCXO比HackRF One更准确。

文章描述了“Teewee”的设计和开发，这是一种用于接收WWVB的小型有源环形天线，以及在减轻干扰（特别是来自附近电子设备的干扰）方面面临的挑战。作者解释了WWVB信号的特性，包括其ASK和BPSK调制。

该项目最令人兴奋的部分是测量加拿大境内飞行期间WWVB的多普勒频移。通过分析捕获的WWVB随时间变化的频率，作者能够观察到飞机相对于发射器运动引起的多普勒效应。通过将观察到的多普勒频移与ADSB飞行数据相关联，确认了该效应，并揭示了由于HackRF Pro的TCXO引起的微小频率偏移。由于航空电子设备的干扰，作者无法在返程航班上获得相同的数据。

作者最后邀请读者构建自己的Teewee天线，强调其与HackRF Pro的兼容性，并提到使用HackRF One取得的一些有限成功。

---

## 49. Goto 被认为无害

**原文标题**: Goto Considered Harmless

**原文链接**: [https://bramadityaw.github.io/blog/posts/goto/](https://bramadityaw.github.io/blog/posts/goto/)

"Goto Considered Harmless" 这篇文章挑战了埃德斯格·迪科斯彻推广的长期以来认为 `goto` 语句本质上是不良编程实践的观点。作者认为，迪科斯彻担忧的历史背景至关重要，并且现代编程语言减轻了他所强调的问题。

作者引用了一个展示 Linux 内核中 `goto` 语句的视频，并辩称关于 `goto` 的观点通常是宗教式的而非技术性的，以此来捍卫它们的使用。迪科斯彻最初的担忧源于观察到过度使用 `goto` 会使代码难以理解，从而妨碍程序员理解执行流程的能力。他提倡使用结构化编程，使用 `if` 和 `while` 等结构来创建更可预测和可追踪的执行路径。

文章的中心论点是，与迪科斯彻时代可用的语言不同，现代语言对 `goto` 的使用有限制，从而解决了他的担忧。具体来说，作者用一个 C 语言的例子证明，`goto` 语句只能跳转到同一过程中的标签，从而防止了迪科斯彻担心的混乱、不受限制的跳转。这种限制保留了过程抽象，并允许结构化编程实践，即使存在 `goto`。因此，作者得出结论，`goto` 以其现代的、受约束的形式，不再像曾经被认为的那样有害。

---

## 50. 开源Zig书籍

**原文标题**: Open-source Zig book

**原文链接**: [https://www.zigbook.net](https://www.zigbook.net)

以下是关于Zigbook的介绍，它是一本开源书籍，旨在教授Zig编程语言。本书强调学习Zig不仅仅是学习语法，更重要的是采纳一种新的软件开发哲学。本书承诺带来一场变革性的学习体验。

重点内容：

*   **重点：** 学习Zig编程语言及其底层软件开发哲学。
*   **方法：** 基于项目的学习。
*   **内容：** 本书包含61章。
*   **作者：** @zigbookzsh。
*   **“零AI”：** 暗示内容由人工编写，而非AI生成。
*   **网站：** zigbook.net。
*   **执行命令：** `zig build zigbook`
*   **互动：** 提供交互式终端环境以供学习。

---

## 51. 理性的演变：黑猩猩如何处理冲突证据

**原文标题**: The evolution of rationality: How chimps process conflicting evidence

**原文链接**: [https://arstechnica.com/science/2025/11/the-evolution-of-rationality-how-chimps-process-conflicting-evidence/](https://arstechnica.com/science/2025/11/the-evolution-of-rationality-how-chimps-process-conflicting-evidence/)

本文探讨了Jan M. Engelmann及其同事关于理性进化的研究，特别是黑猩猩如何处理冲突证据并修正其信念。研究人员进行了五项涉及食物谜题的实验，以评估黑猩猩做出理性决策的能力。

最初的实验表明，黑猩猩可以根据新的证据改变他们的选择，尤其是在微弱的初始证据之后出现强烈的反证时。后来的实验揭示了更复杂的认知能力。黑猩猩考虑了所有可用的选项，展示了对证据层级的基本理解。他们还认识到冗余证据，表明他们创建了信息的心理表征。最令人印象深刻的是，最后的实验表明黑猩猩可以理解“二阶证据”，认识到证据可能具有误导性，并相应地调整他们的选择。

在所有实验中，黑猩猩遵循证据的程度显著高于偶然，表明存在一定程度的理性。Engelmann认为，理性存在于一个谱系中，黑猩猩表现出初级形式，而更高级的反射性理性则出现在黑猩猩以及可能倭黑猩猩身上。虽然他认为人类通过协作讨论拥有“社会理性”，但他也承认社会影响有时会导致非理性。有趣的是，初步研究表明黑猩猩不太容易受到社会非理性的影响，因为它们只遵循拥有更优证据的其他黑猩猩的决定。该研究为理性思维的进化起源提供了重要的见解。

---

## 52. 讽刺

**原文标题**: "Snarky"; "Snark"

**原文链接**: [https://notoneoffbritishisms.com/2025/10/13/snarky-snark/](https://notoneoffbritishisms.com/2025/10/13/snarky-snark/)

本文探讨了“snarky”和“snark”这两个词的定义、词源以及流行度的上升。文章首先将“snarky”定义为讽刺的、无礼的或不敬的，而“snark”则作为名词或动词，指代嘲弄的不敬和讽刺。作者指出，近几十年来，这两个词的使用量显著增加，并引用了20世纪90年代的例子。

接下来，文章深入研究了“snark”一词的起源。虽然有些人认为它源于刘易斯·卡罗尔的诗歌，但文章澄清说，它起源于苏格兰和设得兰群岛的方言，在这些方言中，“snark”的意思是打鼾、烦躁或抱怨。文章还指出了它与“nark”（意为讨厌的人）的联系。文章追溯了“snark”作为动词和“snarky”作为形容词的首次使用，均可追溯到20世纪初伊迪丝·内斯比特的作品中。文章还引用了20世纪初的其他英国例子，之后该词跨越大西洋，大约在1915年出现在美国文学作品中。

文章明确指出，“snark”作为名词直到20世纪80年代后期才出现。最后，文章认为“snarky”最近的流行可能归因于其发音类似于“sarcastic”（讽刺的）和“snarl”（咆哮）的组合，与当前的文化氛围相符。

---

## 53. 锂与莴苣

**原文标题**: Lithium vs. Lettuce

**原文链接**: [https://ambrook.com/offrange/photo-essay/lithium-v-lettuce](https://ambrook.com/offrange/photo-essay/lithium-v-lettuce)

加州帝王谷：农业与锂矿开采的潜在冲突

---

## 54. 复古大型语言模型

**原文标题**: Vintage Large Language Models

**原文链接**: [https://owainevans.github.io/talk-transcript.html](https://owainevans.github.io/talk-transcript.html)

本文介绍了“复古大型语言模型”(LLMs)的概念，该模型是在仅截至特定历史日期的数据上训练的 LLMs。作者认为，这些模型为科学、认知和人文探索提供了宝贵的机会。

在科学方面，复古 LLMs 可用于回溯测试预测方法，并探索人工智能驱动的科学发明的潜力。通过在截至特定日期（例如，2019年或1600年）的数据上训练模型，研究人员可以评估其预测后续事件或根据可用的历史知识重新发明已知发明的能力。

在人文方面，复古 LLMs 可以模拟与过去人物的对话，提供独特的互动体验和对历史知识的新视角。此外，这些模型可以通过结合来自不同文化的知识或检查历史突破的惊人程度来探索反事实的知识史。

文章承认创建复古 LLMs 存在重大挑战，包括需要海量、无污染的数据集以及高昂的训练成本。讨论的解决方案包括利用合成数据来扩充有限的历史数据集、使用分叉进行按时间顺序的训练以降低训练成本，以及将功能外包给当代 LLMs，同时防止信息泄露。在所有数据上训练但带有日期注释的隔离式 LLMs 也被提出作为一种补充方法。

总之，复古 LLMs 的概念为探索知识随时间的演变以及在历史背景下测试人工智能能力提供了一条独特的途径，为科学和人文研究提供了令人兴奋的可能性。

---

## 55. 政府对美国3000亿枚便士没有计划

**原文标题**: The government has no plan for America’s 300 billion pennies

**原文链接**: [https://www.theatlantic.com/ideas/2025/11/pennies-circulation-mint/684935/](https://www.theatlantic.com/ideas/2025/11/pennies-circulation-mint/684935/)

凯蒂·韦弗的文章《政府对美国三千亿枚便士毫无计划》探讨了美国出人意料且似乎未经计划的停止生产便士的行为。尽管美国铸币局已经停止铸造便士，但对于如何处理估计已在流通中的3000亿枚便士，却没有任何策略。

韦弗此前曾研究过便士生产的昂贵和不合逻辑的持续性，她揭示了停止铸造便士的决定是在没有考虑后果的情况下做出的。政府没有就如何在没有便士的情况下进行现金交易提供任何指导，也没有计划将现有的便士从流通中移除。

作者将这种缺乏计划的做法与加拿大平稳淘汰便士的做法进行了对比，后者包括公众宣传活动、回收计划和按面值兑换。美国的便士主要由锌制成，由于锌的价值较低以及有毒的冶炼过程，给回收带来了挑战。

韦弗强调了便士的心理负担，它们经常未被使用，并代表着一种环境危害。政府的不作为反映了其历史上让便士成为“美国人的问题”的做法。文章以铸币局未来可能恢复便士生产的令人担忧的可能性作为结尾，这将使“永久便士悖论”永久存在。

---

## 56. 德布鲁因数

**原文标题**: De Bruijn Numerals

**原文链接**: [https://text.marvinborner.de/2023-08-22-22.html](https://text.marvinborner.de/2023-08-22-22.html)

本文介绍了“de Bruijn数”，这是一种使用嵌套de Bruijn索引在纯lambda演算中对自然数进行的新颖编码：`<n>_d = λ^{S(n)}n`。 虽然很优雅，但这些数，像其他形式为`λ^{k_n}E_n`的编码（其中`k_n`随着`n`无限增加）一样，缺乏一个“充分”的数制，具体来说，缺乏一个zero?函数。 这种限制阻碍了直接转换为其他数制。

尽管有这个缺点，本文探讨了de Bruijn数的算术运算。 定义并证明了后继（`succ`）和前驱（`pred`）函数，以及一个以优雅的方式利用de Bruijn移位的自包含加法函数（`add`）。 本文还讨论了如何将de Bruijn数与Church数结合，定义了一个转换函数并演示了乘法。

一个关键的实际应用是处理Church n-元组。 De Bruijn数提供了一种在元组中选择元素的方法，而无需增加抽象的数量。 这使得像`push`，`pop`和`move`这样的函数成为可能，而这些函数很难直接用Church列表实现。 本文最后强调了发现de Bruijn数的新运算的潜力，并引用了一种使用这种元组编码的类似Forth的语言实现。 最终，虽然不是一个普遍可转换的数制，但de Bruijn数在特定的lambda演算操作中提供了独特的优势。

---

## 57. 等待SQL:202y：全部按组分组

**原文标题**: Waiting for SQL:202y: Group by All

**原文链接**: [http://peter.eisentraut.org/blog/2025/11/11/waiting-for-sql-202y-group-by-all](http://peter.eisentraut.org/blog/2025/11/11/waiting-for-sql-202y-group-by-all)

本文探讨了即将到来的 SQL:202y 标准中提议的 "GROUP BY ALL" 特性，该特性旨在简化 SQL 查询中的 `GROUP BY` 子句。作者认为，手动在 `GROUP BY` 中指定列通常是冗余且容易出错的，尤其是在选择列表清楚地指示分组列时。

`GROUP BY ALL` 自动按 `SELECT` 语句中的所有非聚合列进行分组。 例如，`SELECT a, avg(b) FROM t1 GROUP BY ALL;` 变为 `SELECT a, avg(b) FROM t1 GROUP BY a;`。

本文强调了其局限性：`GROUP BY ALL` 仅处理分组简单的情况，并避免在聚合函数与其他未分组列混合时出现歧义。它明确不处理所需的 grouping 不明确的复杂场景，而是留给用户来指定。

作者警告了与 `SELECT *` 类似的潜在风险，即向选择列表添加列可能会无意中改变分组行为。 因此，建议谨慎和周全地应用，尤其是在复杂的查询中。

包括 Oracle、PostgreSQL、Databricks、DuckDB、BigQuery 和 Snowflake 在内的多个数据库系统已经实施或计划实施 `GROUP BY ALL`。 Oracle 也在标准提案中发挥了关键作用。 PostgreSQL 在标准化决定后迅速实施了它。

---

## 58. 也许呼叫我：使用ReVoLTE窃听加密LTE通话 (2020)

**原文标题**: Call Me Maybe: Eavesdropping encrypted LTE calls with ReVoLTE (2020)

**原文链接**: [https://montsecure.com/research/revolte-attack/](https://montsecure.com/research/revolte-attack/)

2020年论文《叫我可能：使用ReVoLTE窃听加密的LTE通话》详细介绍了LTE网络协议中的一个漏洞，该漏洞允许攻击者窃听加密的电话通话。来自波鸿鲁尔大学和纽约大学阿布扎比分校的研究人员发现并利用了与LTE加密中密钥流重用相关的逻辑缺陷。

核心问题在于LTE中保密密钥（KeNB）的推导和管理方式。研究人员证明，在某些情况下，特别是在基站之间的切换过程之后，同一个KeNB值可能会被多个连接重用。这反过来会导致用于加密的密钥流的重用，从而损害通话的保密性。

研究人员开发了一种名为ReVoLTE的工具来自动利用此漏洞。ReVoLTE允许攻击者被动地监控LTE流量，识别密钥流重用何时发生，并解密后续加密的语音数据。该论文展示了实际攻击，证明了窃听真实世界LTE通话的可行性。

这些发现突显了LTE标准实施中的一个关键安全弱点，引发了人们对蜂窝通信的隐私和安全的担忧。研究人员提出了缓解该漏洞的建议，重点是改进KeNB推导过程，以防止密钥流重用并提高整体安全性。该研究强调了在现代通信协议中进行彻底的安全分析和测试的重要性，以防止潜在的窃听攻击。

---

## 59. 莱布尼茨记号解读 (2024)

**原文标题**: Decoding Leibniz Notation (2024)

**原文链接**: [https://www.spakhm.com/leibniz](https://www.spakhm.com/leibniz)

Slava Akhmechet 的《解读莱布尼茨记号》旨在阐明常令人困惑的导数莱布尼茨记号。作者首先从历史动机入手，解释了莱布尼茨关于无穷小量的概念，即用“dx”和“df(x)”表示，其中导数被视为它们的商。然而，“dx”并不是一个可以被约分的值，而是一个算子。

文章随后过渡到现代解释，将 df(x)/dx 视为代表导函数 f' 的单一符号，而不是一个商。它强调实际上并没有发生除法。

作者深入探讨了莱布尼茨记号中二阶导数的表示方法，强调了为了方便而采取的代数自由，例如用 d²f(x)/dx² 代替更冗长的 d(df(x)/dx)/dx。他指出，dx² 并非字面意义上的 (dx)²，而是二阶导数过程的符号表示，而 d² 并非 d 的平方。

文章进一步探讨了该记号中常见的自由性和模糊性，特别是关于在特定点“a”处评估导数。他注意到省略记号 (df(x)/dx | x=a) 中“x=a”部分的常见做法，并将 df(x)/dx 简化为 df/dx，即使这些替换在技术上是不正确的。

最后，文章讨论了科学家和工程师们所采取的更大的自由，他们经常隐含地将变量视为时间的函数并相应地操纵该记号，如在相关变化率问题中所见。作者建议通过实际解决问题作为理解这种用法的最佳途径。

---

## 60. 马盖特贝壳岩洞

**原文标题**: Shell Grotto, Margate

**原文链接**: [https://en.wikipedia.org/wiki/Shell_Grotto,_Margate](https://en.wikipedia.org/wiki/Shell_Grotto,_Margate)

马盖特贝壳岩洞，肯特郡，是一个装饰华丽的地下建筑，镶嵌着大约460万个贝壳，覆盖了约2000平方英尺的马赛克。岩洞大约在1835年被发现，于1837年向公众开放，其年代、建造者和目的仍然未知，引发了众多理论，从富人的心血来潮到与古代社会的联系。

该结构由一条通往矩形房间的蜿蜒通道组成，两者都用贻贝、鸟蛤、峨螺和帽贝等贝壳精心装饰。虽然大多数贝壳是当地的，但有些可能来自更远的地方。

岩洞的起源尚有争议，可能性包括在17或18世纪改建的中世纪白垩矿。多年来，它面临着挑战，如二战造成的破坏和渗水。目前它是一级保护建筑和旅游景点，设有博物馆、咖啡馆和礼品店。

保护岩洞的努力包括成立贝壳岩洞之友协会，以及与英格兰历史建筑及古迹委员会合作的修复项目。它还出现在小说和其他文化作品中。

---

## 61. 硫磺石：用 Rust 编写的 ES2025 JavaScript 引擎

**原文标题**: Brimstone: ES2025 JavaScript engine written in Rust

**原文链接**: [https://github.com/Hans-Halverson/brimstone](https://github.com/Hans-Halverson/brimstone)

硫磺火 (Brimstone) 是一个用 Rust 编写的全新 JavaScript 引擎，旨在实现完全的 ECMAScript 兼容性。目前仍在开发中，它拥有超过 97% 的 test262 测试套件兼容性，并整合了高达 ES2024 的特性，以及来自 2025 年 2 月 TC39 会议的 Stage 4 提案。

主要特性包括一个受 V8 的 Ignition 启发的字节码 VM、一个压缩垃圾收集器（使用 unsafe Rust 编写）、一个自定义 RegExp 引擎和一个自定义解析器。硫磺火 (Brimstone) 的设计尽可能减少外部依赖，并使用 ICU4X 进行国际化。

虽然尚未准备好用于生产环境，但可以使用标准的 `cargo` 命令构建和运行硫磺火 (Brimstone)。JavaScript 文件通过 `bs` 可执行文件执行。测试主要依赖于集成测试套件，尤其是 test262，通过 `cargo brimstone-test` 提供自定义测试运行器。单元和快照测试使用 `cargo test`。

该引擎目前缺少对 SharedArrayBuffer 和 Atomics 的支持。

---

## 62. Show HN：用朴素贝叶斯算法实现的Go语言垃圾邮件分类器

**原文标题**: Show HN: Spam classifier in Go using Naive Bayes

**原文链接**: [https://github.com/igomez10/nspammer](https://github.com/igomez10/nspammer)

此“Show HN”帖子介绍`nspammer`，一个用Go语言实现的朴素贝叶斯垃圾邮件分类器。该库通过在带标签的数据集（垃圾邮件/非垃圾邮件）上训练，并对新消息进行分类，来实现文本分类。它使用带有拉普拉斯平滑的朴素贝叶斯算法来处理未见过的单词和零概率。

主要功能包括一个简单的API用于训练和分类，包含`NewSpamClassifier`和`Classify`函数。帖子提供了一个基本的使用示例，演示了如何创建一个分类器，在一个小型数据集上训练它，以及如何分类一条新消息。

帖子解释了所使用的朴素贝叶斯算法：计算先验概率，构建词汇表，统计词语出现次数，并使用对数概率来避免分类期间的下溢。拉普拉斯平滑，使用公式`P(word|class) = (count + α) / (total + α × vocabulary_size)`，解决了未见过的单词的问题。

该库包含对Kaggle垃圾邮件数据集的支持，可以使用`./init.sh`脚本下载（需要Kaggle CLI）。 帖子还详细介绍了如何运行测试套件（`go test -v`），其中包括简单的例子、真实世界数据集评估以及准确性测量。

---

## 63. Trellis AI (YC W24) 招聘：简化救生疗法的获取途径

**原文标题**: Trellis AI (YC W24) Is Hiring: Streamline access to life-saving therapies

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time)

Trellis AI，一家 Y Combinator W24 孵化的初创公司，正在招聘一名前置部署工程师，以帮助简化医疗保健文书工作并加速患者获得救生疗法。他们使用人工智能代理来自动化文档录入、事先授权和申诉，每年处理价值数十亿美元的疗法，覆盖美国所有 50 个州。可以把他们看作是“医疗保健账单和报销领域的 Stripe”。

该职位涉及设计和实施用于医疗保健决策的人工智能系统，构建 24/7 全天候人工智能同事，以及在其评估套件中开发生产级人工智能系统。

Trellis 正在寻找具有全栈开发经验、精通 Python、Go、机器学习/自然语言处理库（PyTorch、TensorFlow、Transformers）以及关系/非关系数据库（尤其是 Postgres）的候选人。积极主动、快速学习能力以及数据/机器学习基础设施经验至关重要。开源贡献和云平台/容器化（AWS、Azure、GCP、Docker、Kubernetes）经验是加分项。

Trellis 强调实际影响、与行业专家合作、走在医疗保健人工智能前沿、直接客户互动、高度责任感、世界一流的团队以及令人难以置信的增长（近期收入增长了 10 倍）。 Trellis AI 旨在缩短治疗时间（超过 90%）、提高批准和报销率并增强药物计划的性能。 Trellis 成立于 2024 年，拥有一支 25 人的团队，利用基于数百万临床数据点训练的人工智能来自动化医疗保健文书工作。

---

## 64. 高盛生物科技报告发问：治愈病人是可持续的生意吗？(2018)

**原文标题**: Goldman Sachs asks in biotech Report: Is curing patients a sustainable business? (2018)

**原文链接**: [https://www.cnbc.com/2018/04/11/goldman-asks-is-curing-patients-a-sustainable-business-model.html](https://www.cnbc.com/2018/04/11/goldman-asks-is-curing-patients-a-sustainable-business-model.html)

高盛在2018年一份题为《基因组革命》的报告中，分析师质疑了旨在用“一次性”疗法治愈疾病的基因治疗公司能否实现长期可持续发展。分析师Salveen Richter指出，虽然治愈对患者和社会有益，但它们可能会对寻求持续收入来源的生物科技公司构成挑战，因为它们颠覆了慢性疗法典型的重复性收入模式。

该报告引用吉利德科学公司的丙型肝炎疗法作为案例研究。虽然实现了高治愈率，并在2015年创造了125亿美元的峰值销售额，但随着可治疗患者群体的减少，销售额随后下降。该报告还指出，传染病的治愈会减少传播，进一步缩小潜在的患者群体。癌症的发病率相对稳定，因此基于治愈疗法的可持续性风险较小。

为了应对这一潜在挑战，该报告为生物科技公司提出了三项策略：关注像血友病这样的大型市场，瞄准像脊髓性肌萎缩症这样高发病率的疾病，以及强调持续创新和投资组合扩张，以抵消先前基于治愈疗法所带来的收入下降。

---

## 65. 如果根本不需要MCP呢？

**原文标题**: What if you don't need MCP at all?

**原文链接**: [https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)

本文反对过度依赖于单体MCP（多工具调用协议）服务器来执行智能体任务，尤其是在浏览器自动化方面。作者提出了一种更简单、更具可组合性的方法，即使用Bash脚本和Puppeteer Core。

其核心思想是，智能体可以有效地利用已有的代码和Bash知识，通过最少且专门构建的工具与浏览器进行交互。作者建议使用一组小型工具，而不是使用大型MCP服务器（如Playwright MCP或Chrome DevTools MCP，它们拥有许多工具并消耗大量的上下文tokens）：启动浏览器、导航到URL、执行JavaScript以及截取屏幕截图。

作者提供了这些工具的代码，展示了它们的简洁性。这种方法的优点包括：减少上下文使用量（描述这些工具的README远小于MCP服务器的描述），提高可组合性（智能体可以将输出保存到文件中以供后续处理），更容易定制，以及能够轻松添加新工具。

作为添加新工具的示例，本文演示了如何仅用少量代码添加一个用于交互式元素选择的“Pick”工具。这允许人们直接指出要与智能体交互的元素，从而简化了诸如网络抓取之类的任务。作者强调，这种方法反映了Anthropic技能系统的优势，提供了渐进式披露，并通过简单的指令使工具易于访问。

---

## 66. 也许你没有尽力。

**原文标题**: Maybe you’re not trying

**原文链接**: [https://usefulfictions.substack.com/p/maybe-youre-not-actually-trying](https://usefulfictions.substack.com/p/maybe-youre-not-actually-trying)

无法访问文章链接。

---

## 67. 在 Kubernetes 中运行基于 Nix 的环境

**原文标题**: Run Nix Based Environments in Kubernetes

**原文链接**: [https://flox.dev/kubernetes/](https://flox.dev/kubernetes/)

本文介绍了 Flox，该系统旨在通过消除容器镜像重建的需要并促进可重现的环境，从而简化 Kubernetes 部署。Flox 利用 Nix 创建声明式的、不可变的环境，这些环境可以在开发、CI/CD 和生产 Kubernetes 集群之间共享，无论架构如何（x86 和 ARM）。

核心概念是用声明式的 Flox 环境定义来替换传统的构建-推送-拉取镜像管道。该定义指定了解析为存储在节点本地缓存中的哈希寻址软件包的依赖项，从而避免了大型镜像传输，并实现了更快、更可预测的部署。主要优势包括：

*   **可重现性：** 确保整个软件开发生命周期中的环境一致。
*   **安全性：** 减少攻击面，默认提供 SBOM，并促进原子回滚。
*   **运维简洁性：** 与现有 Kubernetes 基础设施和 GitOps 工作流程集成。
*   **更快的部署：** 消除镜像重建和注册表往返。

Flox 利用自定义 containerd shim 在启动时激活容器内的 Flox 环境，利用现有的 Kubernetes 原语。它通过提供一致、安全且可重现的环境，而无需容器镜像的开销，从而解决了人工智能/机器学习、数据科学和平台工程等各个领域的挑战。它还允许团队在本地重新创建精确的生产运行时，从而简化了调试。

---

## 68. Republican push to make U.S. census surveys voluntary alarms statisticians

**原文标题**: Republican push to make U.S. census surveys voluntary alarms statisticians

**原文链接**: [https://www.science.org/content/article/republican-push-make-u-s-census-surveys-voluntary-alarms-statisticians](https://www.science.org/content/article/republican-push-make-u-s-census-surveys-voluntary-alarms-statisticians)

Unable to access the article link.


---

## 69. From Zero to 35M: The struggles of scaling Laravel with Octane

**原文标题**: From Zero to 35M: The struggles of scaling Laravel with Octane

**原文链接**: [https://www.galahadsixteen.com/blog/from-zero-to-35m-the-struggles-of-scaling-laravel-with-octane](https://www.galahadsixteen.com/blog/from-zero-to-35m-the-struggles-of-scaling-laravel-with-octane)

生成摘要时出错

---

## 70. Gigantic VHS videotape hoard of videos being given away for free

**原文标题**: Gigantic VHS videotape hoard of videos being given away for free

**原文链接**: [https://www.tomshardware.com/software/video-editing-graphic-design/gigantic-vhs-videotape-hoard-of-thousands-of-videos-stored-in-mcdonalds-boxes-being-given-away-for-free-internet-archive-looks-set-to-claim-the-tapes-of-u-s-news-output-spanning-2004-09](https://www.tomshardware.com/software/video-editing-graphic-design/gigantic-vhs-videotape-hoard-of-thousands-of-videos-stored-in-mcdonalds-boxes-being-given-away-for-free-internet-archive-looks-set-to-claim-the-tapes-of-u-s-news-output-spanning-2004-09)

生成摘要时出错

---

## 71. Writing a DOS Clone in 2019

**原文标题**: Writing a DOS Clone in 2019

**原文链接**: [https://medium.com/@andrewimm/writing-a-dos-clone-in-2019-70eac97ec3e1](https://medium.com/@andrewimm/writing-a-dos-clone-in-2019-70eac97ec3e1)

生成摘要时出错

---

## 72. Running the "Reflections on Trusting Trust" Compiler (2023)

**原文标题**: Running the "Reflections on Trusting Trust" Compiler (2023)

**原文链接**: [https://research.swtch.com/nih](https://research.swtch.com/nih)

生成摘要时出错

---

## 73. Production-Grade Container Deployment with Podman Quadlets – Larvitz Blog

**原文标题**: Production-Grade Container Deployment with Podman Quadlets – Larvitz Blog

**原文链接**: [https://blog.hofstede.it/production-grade-container-deployment-with-podman-quadlets/index.html](https://blog.hofstede.it/production-grade-container-deployment-with-podman-quadlets/index.html)

生成摘要时出错

---

## 74. The inconceivable types of Rust: How to make self-borrows safe (2024)

**原文标题**: The inconceivable types of Rust: How to make self-borrows safe (2024)

**原文链接**: [https://blog.polybdenum.com/2024/06/07/the-inconceivable-types-of-rust-how-to-make-self-borrows-safe.html](https://blog.polybdenum.com/2024/06/07/the-inconceivable-types-of-rust-how-to-make-self-borrows-safe.html)

生成摘要时出错

---

## 75. Runit Linux: Complete Guide to Unix Init Scheme with Service Supervision

**原文标题**: Runit Linux: Complete Guide to Unix Init Scheme with Service Supervision

**原文链接**: [https://codelucky.com/runit-linux-init-service-supervision/](https://codelucky.com/runit-linux-init-service-supervision/)

生成摘要时出错

---

## 76. An Open-Source HDMI Keyboard/Video/Mouse (KVM) Switch

**原文标题**: An Open-Source HDMI Keyboard/Video/Mouse (KVM) Switch

**原文链接**: [https://github.com/thatoddmailbox/kvm](https://github.com/thatoddmailbox/kvm)

生成摘要时出错

---

## 77. Archimedes – A Python toolkit for hardware engineering

**原文标题**: Archimedes – A Python toolkit for hardware engineering

**原文链接**: [https://pinetreelabs.github.io/archimedes/blog/2025/introduction.html](https://pinetreelabs.github.io/archimedes/blog/2025/introduction.html)

生成摘要时出错

---

## 78. PgFirstAid: PostgreSQL function for improving stability and performance

**原文标题**: PgFirstAid: PostgreSQL function for improving stability and performance

**原文链接**: [https://github.com/randoneering/pgFirstAid](https://github.com/randoneering/pgFirstAid)

生成摘要时出错

---

## 79. Things that aren't doing the thing

**原文标题**: Things that aren't doing the thing

**原文链接**: [https://strangestloop.io/essays/things-that-arent-doing-the-thing](https://strangestloop.io/essays/things-that-arent-doing-the-thing)

生成摘要时出错

---

## 80. Geothermal energy might be the baseload revolution we've been looking for

**原文标题**: Geothermal energy might be the baseload revolution we've been looking for

**原文链接**: [https://www.newyorker.com/magazine/2025/11/24/why-the-time-has-finally-come-for-geothermal-energy](https://www.newyorker.com/magazine/2025/11/24/why-the-time-has-finally-come-for-geothermal-energy)

生成摘要时出错

---

## 81. Dissecting Flock Safety: The Cameras Tracking You Are a Security Nightmare [video]

**原文标题**: Dissecting Flock Safety: The Cameras Tracking You Are a Security Nightmare [video]

**原文链接**: [https://www.youtube.com/watch?v=uB0gr7Fh6lY](https://www.youtube.com/watch?v=uB0gr7Fh6lY)

生成摘要时出错

---

## 82. Mag Wealth (2024)

**原文标题**: Mag Wealth (2024)

**原文链接**: [https://saul.pw/mag/wealth/](https://saul.pw/mag/wealth/)

生成摘要时出错

---

## 83. Origin and Evolution of the Globstar

**原文标题**: Origin and Evolution of the Globstar

**原文链接**: [https://mergify.com/blog/origin-and-evolution-of-the-globstar](https://mergify.com/blog/origin-and-evolution-of-the-globstar)

生成摘要时出错

---

## 84. Extreme Moon: The Major Lunar Standstill of 2024-2025

**原文标题**: Extreme Moon: The Major Lunar Standstill of 2024-2025

**原文链接**: [https://griffithobservatory.org/extreme-moon-the-major-lunar-standstills-of-2024-2025/](https://griffithobservatory.org/extreme-moon-the-major-lunar-standstills-of-2024-2025/)

生成摘要时出错

---

## 85. AI World Clocks

**原文标题**: AI World Clocks

**原文链接**: [https://clocks.brianmoore.com/](https://clocks.brianmoore.com/)

生成摘要时出错

---

## 86. Adding an imaginary unit to a finite field

**原文标题**: Adding an imaginary unit to a finite field

**原文链接**: [https://www.johndcook.com/blog/2025/11/16/finite-field-i/](https://www.johndcook.com/blog/2025/11/16/finite-field-i/)

生成摘要时出错

---

## 87. People are using iPad OS features on their iPhones

**原文标题**: People are using iPad OS features on their iPhones

**原文链接**: [https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/](https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/)

生成摘要时出错

---

## 88. UK's first small nuclear power station to be built in north Wales

**原文标题**: UK's first small nuclear power station to be built in north Wales

**原文链接**: [https://www.bbc.com/news/articles/c051y3d7myzo](https://www.bbc.com/news/articles/c051y3d7myzo)

生成摘要时出错

---

## 89. Alchemy

**原文标题**: Alchemy

**原文链接**: [https://joshcollinsworth.com/blog/alchemy](https://joshcollinsworth.com/blog/alchemy)

生成摘要时出错

---

## 90. JavaScript Engines Benchmarks

**原文标题**: JavaScript Engines Benchmarks

**原文链接**: [https://ivankra.github.io/javascript-zoo/](https://ivankra.github.io/javascript-zoo/)

生成摘要时出错

---

## 91. Coherent Synchrotron Radiation by Excitation of SPPs on Near-Critical CNT

**原文标题**: Coherent Synchrotron Radiation by Excitation of SPPs on Near-Critical CNT

**原文链接**: [https://arxiv.org/abs/2507.04561](https://arxiv.org/abs/2507.04561)

生成摘要时出错

---

## 92. Where Educational Technology Fails: A seventh-grader's perspective

**原文标题**: Where Educational Technology Fails: A seventh-grader's perspective

**原文链接**: [https://micahblachman.beehiiv.com/p/where-educational-technology-fails](https://micahblachman.beehiiv.com/p/where-educational-technology-fails)

生成摘要时出错

---

## 93. Holes (1970) [pdf]

**原文标题**: Holes (1970) [pdf]

**原文链接**: [https://rintintin.colorado.edu/~vancecd/phil375/Lewis1.pdf](https://rintintin.colorado.edu/~vancecd/phil375/Lewis1.pdf)

This document is a PDF file, likely created using Microsoft Word 2013. The file's metadata indicates it was created and modified on September 5, 2019.

Unfortunately, the content of the PDF is mostly binary data, representing the compressed information of the document. There is a title present "Holes (1970)", but the rest of the text in the document is code. It is impossible to determine the subject or content of the article based on the provided raw PDF code. I am unable to provide a summary without the readable text content of the "Holes (1970)" article.


---

## 94. JVM exceptions are weird: a decompiler perspective

**原文标题**: JVM exceptions are weird: a decompiler perspective

**原文链接**: [https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/](https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/)

生成摘要时出错

---

## 95. Show HN: Unflip – a puzzle game about XOR patterns of squares

**原文标题**: Show HN: Unflip – a puzzle game about XOR patterns of squares

**原文链接**: [https://unflipgame.com/](https://unflipgame.com/)

生成摘要时出错

---

## 96. Steam Machine

**原文标题**: Steam Machine

**原文链接**: [https://store.steampowered.com/sale/steammachine](https://store.steampowered.com/sale/steammachine)

生成摘要时出错

---

## 97. One Handed Keyboard

**原文标题**: One Handed Keyboard

**原文链接**: [https://github.com/htx-studio/One-Handed-Keyboard](https://github.com/htx-studio/One-Handed-Keyboard)

生成摘要时出错

---

## 98. Trump-Licensed Presidential Seal Beer Pong Set, Bible Could Violate Federal Law

**原文标题**: Trump-Licensed Presidential Seal Beer Pong Set, Bible Could Violate Federal Law

**原文链接**: [https://www.forbes.com/sites/zacheverson/2025/11/14/trump-beer-pong-lee-greenwood-presidential-seal-bible/](https://www.forbes.com/sites/zacheverson/2025/11/14/trump-beer-pong-lee-greenwood-presidential-seal-bible/)

生成摘要时出错

---

## 99. A Man Who Rescued Faulkner

**原文标题**: A Man Who Rescued Faulkner

**原文链接**: [https://www.theatlantic.com/magazine/2025/12/malcolm-cowley-american-literature/684606/](https://www.theatlantic.com/magazine/2025/12/malcolm-cowley-american-literature/684606/)

This article explores the life and career of Malcolm Cowley, a prominent literary critic and editor who played a crucial role in shaping the landscape of 20th-century American literature. Cowley was a keen talent scout, discovering and promoting writers like John Cheever, Alfred Kazin, Jack Kerouac, and Ken Kesey. However, his most significant contribution was resurrecting William Faulkner's career. He recognized the interconnectedness of Faulkner's Yoknapatawpha novels and championed their publication, leading to Faulkner's widespread recognition and eventual Nobel Prize.

Cowley aimed to elevate American writing, advocating for its recognition as a distinct tradition separate from British literature. He believed in understanding literature within its social and historical context, contrasting with the New Criticism's focus on purely textual analysis. His own experiences as a member of the "Lost Generation" in Paris after World War I shaped his understanding of American writers grappling with identity and heritage.

While Cowley's early political leanings led to some missteps regarding Stalinist Russia, his later work focused on analyzing the postwar cultural scene. He observed changes in literary criticism and the democratization of readership. Cowley valued literature that engaged with the complexities of the American experience and sought the "Great American Novel," ultimately seeing Herman Melville's *Moby-Dick* as fulfilling that role. Despite not achieving the same critical acclaim as Edmund Wilson, Cowley's deep understanding of American identity and his championing of American writers cemented his legacy as a vital figure in literary history.


---

## 100. When UPS charged me a $684 tariff on $355 of vintage computer parts

**原文标题**: When UPS charged me a $684 tariff on $355 of vintage computer parts

**原文链接**: [http://oldvcr.blogspot.com/2025/11/when-ups-charged-me-684-tariff-on-355.html](http://oldvcr.blogspot.com/2025/11/when-ups-charged-me-684-tariff-on-355.html)

生成摘要时出错

---

