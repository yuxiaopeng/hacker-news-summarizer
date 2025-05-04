# Hacker News 热门文章摘要 (2025-05-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 阿拉巴马州那条响个不停的座机线路

**原文标题**: The Alabama Landline That Keeps Ringing

**原文链接**: [https://oxfordamerican.org/oa-now/the-alabama-landline-that-keeps-ringing](https://oxfordamerican.org/oa-now/the-alabama-landline-that-keeps-ringing)

本文探讨了奥本大学 Foy 信息台的持久意义。该电话热线始于 1953 年，至今仍在解答公众咨询。尽管互联网兴起，该信息台仍然是一个重要的资源，处理范围广泛的问题，从实际查询到哲学思考。

该信息台由学生工作人员值班，他们接受最少的培训，强调礼貌和足智多谋。学生们对待所有来电者都彬彬有礼，无论他们的问题性质如何，也无论他们的背景如何。许多来电者缺乏互联网访问权限或对其使用缺乏信心，因此 Foy 信息台成为他们获取信息的主要来源。

本文重点介绍了学生与常客之间建立的个人联系，例如“比尤拉”，她古怪的问题和对动物的喜爱创造了一种独特的联系。学生们经常试图了解来电者的情况，并提供超越简单回答问题的帮助和安慰。

故事还包含一些轶事，说明了这项服务的情感影响，例如一位学生倾听了一位老年妇女哀悼朋友。作者回忆了与科拉的一次个人会面，科拉是一位学生，她从一位来电者那里获得了意想不到的职业建议，这强化了这样一种观点，即即使是看似随机的互动也可能具有重要意义。尽管技术进步，Foy 信息台仍提供人际联系，并为世界各地的人们提供有价值的服务。

---

## 2. TScale – 基于消费级GPU的分布式训练

**原文标题**: TScale – distributed training on consumer GPUs

**原文链接**: [https://github.com/Foreseerr/TScale](https://github.com/Foreseerr/TScale)

TScale：在消费级GPU上训练和推理Transformer模型的C++/CUDA框架，具备克服在性能较弱硬件上运行大型语言模型（LLMs）限制的功能。

主要特性包括：优化的Transformer架构以降低注意力成本，支持低精度（FP8、INT8）模型权重和激活值，CPU卸载以最小化GPU内存使用，同步和异步分布式训练，以及1比特梯度压缩以降低网络带宽需求。

TScale支持在消费级GPU上以经济实惠的成本训练15亿参数等大型模型，重点突出在竞价实例上的异步分布式训练。该项目还探索了创新的方法，例如使用1T索引搭配较小模型（1.25亿参数）来实现显著的困惑度降低，本质上是创建了一个具有1T查询索引的模型。

本文提供了Windows和Linux的构建说明，利用CMake和一个名为“fo”的轻量级解决方案/构建文件生成器。它详细介绍了如何获取训练数据（通常使用enwik9数据集、Hugging Face数据集），以及如何使用“gpt_train”通过数据和训练脚本启动训练。分布式训练需要配置相同的、数量为2的幂的worker主机。可以使用“gpt_infer”测试推理，该命令会运行一个基本的HTTP服务器。TScale采用MIT许可证。

---

## 3. 现代LLM采样傻瓜指南

**原文标题**: Dummy's Guide to Modern LLM Sampling

**原文链接**: [https://rentry.co/samplers](https://rentry.co/samplers)

“现代LLM采样新手指南”：本文全面概述了大型语言模型(LLM)如何生成文本，重点介绍了采样方法在控制输出的随机性和创造性方面的关键作用。

文章首先解释了LLM为何使用token（子词）而非整个词或字母，强调了子词分词在词汇量大小、处理罕见词以及捕捉形态信息方面的优势。文章将文本生成过程描述为两步：预测（计算token的概率分布）和选择（选择一个token添加到文本中）。采样方法被引入作为一种将受控的随机性注入选择过程的方式，超越了简单的“贪婪”采样。

文章随后详细介绍了各种流行的采样技术，包括温度（调整整体随机性）、存在惩罚（抑制至少使用过一次的token）、频率惩罚（抑制频繁使用的token）以及重复惩罚（不对称地惩罚来自提示和输出的token）。每个解释都包括直观的描述和更具技术性的、基于算法的解释。文章还介绍了许多更专业的方法，如Top-K、Top-P和Mirostat采样，并附有相应的技术描述和伪代码。

该指南最后强调了采样器顺序的重要性以及不同采样方法之间的相互作用，突出了潜在的协同作用和冲突。它强调了应用采样器的顺序会显著影响最终输出。

---

## 4. 展示HN：EZ-TRAK卫星手部追踪套件

**原文标题**: Show HN: EZ-TRAK Satellite Hand Tracking Suite

**原文链接**: [https://github.com/benb0jangles/EzTrak](https://github.com/benb0jangles/EzTrak)

EZ-TRAK 是一款卫星跟踪套件，专为业余无线电爱好者、气象卫星爱好者和教育目的而设计。它使用安装在便携式天线上的 EZ-TRAK BLE 设备，为手动跟踪卫星提供实时方位角和仰角数据。

该套件包含：

*   **EZ-TRAK 启动器：** 一个图形界面，用于配置位置、跟踪卫星、最小仰角和 TLE 数据源（Celestrak 或 SatNOGS）等设置。
*   **卫星跟踪器：** 主要应用程序，显示方位角/仰角的极坐标图、实时位置、过境预测信息和轨迹记录功能。
*   **旋转器控制：** (可选) 用于控制 wifi + IMU 天线旋转器的应用程序。

要使用 EZ-TRAK，您需要 Python 3.8+、一台支持蓝牙的计算机以及 EZ-TRAK BLE 硬件。安装包括克隆存储库并运行启动器脚本。用户配置其位置，选择卫星，下载 TLE 数据，并启动跟踪器应用程序。跟踪器显示卫星位置和预测的过境。

EZ-TRAK BLE 设备可从 Ez-Trak 销售页面获得，它与 Farabrella 卫星天线连接，并通过蓝牙进行现场操作。故障排除信息可通过串行控制台日志获得，用于解决诸如设备连接、TLE 解析和过境预测等问题。该软件为专有软件，禁止重新分发。它感谢 Celestrak、SatNOGS 和 Skyfield 提供数据和计算。

---

## 5. 儿童脑电图意识监测可安全减少麻醉剂用量

**原文标题**: In kids, EEG monitoring of consciousness safely reduces anesthetic use

**原文链接**: [https://news.mit.edu/2025/kids-eeg-monitoring-consciousness-safely-reduces-anesthetic-use-0429](https://news.mit.edu/2025/kids-eeg-monitoring-consciousness-safely-reduces-anesthetic-use-0429)

本研究报告了一项临床试验，该试验表明，在接受手术的 1-6 岁儿童中使用脑电图监测指导七氟醚麻醉剂量，可显著改善预后。 这项在日本进行的研究将标准麻醉方案与脑电图引导剂量进行了比较，后者由麻醉师使用脑电波读数来调整麻醉剂的用量。

结果表明，脑电图引导剂量允许显著降低七氟醚浓度（诱导从 5% 降至 2%，维持从 2.5% 降至 0.9%），同时保持所需的意识丧失水平。 此外，接受脑电图引导麻醉的儿童，小儿麻醉苏醒期谵妄 (PAED) 的发生率显著降低——标准方案组为 35%，而该组为 21%。

脑电图引导下的患者平均也更早地拔除了呼吸管（3.3 分钟），更快地从麻醉中苏醒（21.4 分钟），并更快地从急性后期护理中出院（16.5 分钟）。 作者认为，减少急性后期护理时间转化为每例病例约 750 美元的成本节约，并且在医学上对儿童更有益。 此外，减少七氟醚的使用对环境有益。

该研究还比较了两组之间的脑电图记录，揭示了与麻醉深度和 PAED 发生相关的脑电波模式的明显差异。 研究结果表明，脑电图监测为麻醉师优化患者护理提供了可操作的指导，并且可以整合到现有的医学教育项目中。

---

## 6. 奥伯龙 Pi

**原文标题**: Oberon Pi

**原文链接**: [http://pascal.hansotten.com/niklaus-wirth/project-oberon/oberon-pi/](http://pascal.hansotten.com/niklaus-wirth/project-oberon/oberon-pi/)

Oberon Pi 是 Project Oberon 模拟器的 Raspberry Pi OS 移植版本，该模拟器最初由 Niklaus Wirth 和 Jürg Gutknecht 开发，后来由 Wirth 和 Paul Reed 重新实现。前 UCSD Pascal 项目成员 Richard Gleaves 改编了 Peter de Wachter 的模拟器，专注于改善用户界面和新用户的可访问性，同时保留了 Oberon 系统的核心方面。

Gleaves 的工作包括修改用户界面以降低学习曲线，并整合 Andreas Pirklbauer 的编译器更新，以支持 CASE 语句和修复错误。一个关键特性是全面的文档，包括 Oberon OS 和 draw 应用程序的更新用户指南，并辅以 Wirth 的原始 Oberon 文档，添加了目录以便于导航。

Oberon Pi 旨在作为 Raspberry Pi OS 中的一个应用程序运行，提供一个代表独立 Oberon 系统环境的窗口。它旨在通过将非必要的 UI 元素更新到现代标准，同时保留其独特的特性，使 Oberon 系统更易于访问。

本文提供了系统要求（Raspberry Pi 4 或 5，32 位或 64 位 Raspberry Pi OS）和安装说明，并提供了 Github 存储库的链接。它还详细介绍了在 64 位 Raspberry Pi OS 上运行 Oberon Pi 的步骤，需要重新编译 'risc' 可执行文件。

---

## 7. Hightouch (YC S19) 正在招聘

**原文标题**: Hightouch (YC S19) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/hightouch/jobs/kIoY0yH-machine-learning-engineer-ai-decisioning](https://www.ycombinator.com/companies/hightouch/jobs/kIoY0yH-machine-learning-engineer-ai-decisioning)

Hightouch招聘机器学习工程师（AI决策团队），估值12亿美元，Y Combinator投资(S19)。Hightouch是领先的可组合CDP和AI决策平台，通过利用企业的数据仓库，赋能企业基于数据采取行动。 公司的使命是使每个业务用户都能使用数据和人工智能来提供个性化的客户体验并优化效果营销。

机器学习工程师将负责从零开始构建智能解决方案，领域包括个性化和产品推荐、自动化实验、预测性受众、内容生成和预算优化。 该职位涉及客户研究、问题定义、预测建模和机器学习基础设施。

Hightouch正在寻找具有强烈求知欲、沟通能力和成长型思维的个人。 该职位的年薪范围为20万美元至26万美元（美元），地点不限。 面试过程侧重于产品意识、系统架构以及与公司价值观的一致性，包括介绍性电话、系统设计筛选和面试，以及与招聘经理的面试。 Hightouch帮助公司将数据仓库转变为营销客户数据平台，从而弥合数据和运营系统之间的差距。

---

## 8. 无所谓，一张用大调和弦写的专辑

**原文标题**: Nevermind, an album on major chords

**原文链接**: [https://farina00.github.io/essays/nevermind/](https://farina00.github.io/essays/nevermind/)

本文探讨了对涅槃乐队标志性专辑《Nevermind》的一个新颖视角，认为其开创性的成功源于其独特的和声结构：在非常规的进行中始终如一地使用大和弦，摒弃了典型摇滚专辑的惯例，如小和弦或复杂和弦。

作者认为，虽然专辑原始的声音和科本“尖叫般的歌唱”最初掩盖了其音乐的精致，但更深入的分析揭示了建立在主要在标准音阶之外使用的大调强力和弦之上的创新和声习语。

核心论点是，科本尽管承认自己缺乏正规的音乐知识，但却直觉地创作了一整张专辑，采用了这种大和弦方法，这使得《Nevermind》与其他可能零星地采用类似技巧的摇滚专辑区分开来。

文章强调了专辑原始、失真的声音与其潜在的和声简单性之间的对比，表明这种意想不到的并置有助于其广泛的吸引力。 作者引用了科本1993年的采访，以此证明他是本能地而非学术地进行歌曲创作的。 最后，文章鼓励读者收听提供的作为资源的孤立的人声、吉他、贝斯和鼓音轨，亲耳聆听这种意想不到的和声。

---

## 9. 莉莉斯与 Modula-2

**原文标题**: Lilith and Modula-2

**原文链接**: [https://astrobe.com/Modula2/](https://astrobe.com/Modula2/)

本文着重介绍尼克劳斯·维尔特创建的编程语言Modula-2，以及它与苏黎世联邦理工学院开发的Lilith工作站的紧密联系。Lilith是一款专为Modula-2编程设计的个人电脑，于1980年发布，包含一套完整的Modula-2编写的软件套件。

本文提供各种历史悠久的Modula-2编译器源码，包括用于Lilith M代码的多遍和单遍编译器。此外，还提供M2M-PC系统，该系统允许在运行MS-DOS的IBM PC上执行Lilith Modula-2编译器。此外，本文还提供用于Apple Macintosh中使用的Mac 68000处理器的单遍Modula-2编译器的源代码。

除了编译器本身，本文还提供必要的文档，如《Modula-2手册》和《MacMETH用户手册》。此外，还链接到相关的论文，特别是关注Lilith架构的代码生成和Modula-2中的单独编译。

最后，本文重点介绍进一步的阅读材料，包括维尔特的《Modula-2编程》和《尼克劳斯·维尔特学派》，其中包含与Lilith的Medos操作系统、Lilith对商业世界的适应以及一家公司使用Modula-2取得的成功相关的章节。本文最后提供了诸如EmuLith模拟器和其他相关Modula-2项目等资源的链接。

---

## 10. Show HN: 用于批量处理的MP3文件编辑器

**原文标题**: Show HN: MP3 File Editor for Bulk Processing

**原文链接**: [https://cjmapp.net/](https://cjmapp.net/)

Cjam：一款针对Windows PC的简易MP3文件编辑软件，专注于批量处理。用户可将MP3文件拖放到界面中，并使用文本命令执行多个连续操作，无需重新编码，从而节省时间并保持音频质量。主要功能包括切割和合并MP3、添加淡入淡出效果和静音间隔，以及播放文件。该软件支持MP3、CUE和M3U文件，以及Cjam的自定义格式。

最新版本1.9.6.0于2025年5月3日发布，需要Windows 10或更高版本以及Microsoft .NET 6.0或更高版本。用户可以下载该软件，解压ZIP文件，然后运行“Cjam.exe”来启动程序。更新日志详细介绍了增量更新、错误修复、功能添加以及从1.9.0.0版本开始的程序名称更改。自2019年12月首次发布以来，Cjam经历了多次更新，重点在于错误修复和改进。

---

## 11. Show HN: 免费的在线PDF编辑器

**原文标题**: Show HN: Free, in-browser PDF editor

**原文链接**: [https://breezepdf.com](https://breezepdf.com)

Breeze PDF 是一款免费的浏览器 PDF 编辑器，完全离线运行，优先保障用户隐私。无需上传任何文件，确保文档始终留在用户电脑上。这种离线处理方式保证了对敏感信息的完全保密和控制。

该编辑器提供一系列强大的功能，包括向 PDF 添加文本、图像和数字签名。用户还可以创建带有交互式文本输入框的可填写表单，合并多个 PDF 文件，删除不需要的页面以及密码保护文档。

Breeze PDF 基于浏览器，无需安装。它直接在现代 Web 浏览器中运行，在初始加载后提供离线编辑功能。虽然针对桌面使用进行了优化，但也可在移动浏览器上使用。

该服务完全免费，没有隐藏费用或使用限制。虽然没有特定的文件大小限制，但处理大型文件取决于用户设备的 RAM 和 CPU。总而言之，Breeze PDF 提供了一种安全且易于访问的解决方案，用于管理和编辑 PDF 文档，同时不损害用户隐私。

---

## 12. 华丽GRUB：精选社区制作的优秀GRUB主题

**原文标题**: Gorgeous-GRUB: collection of decent community-made GRUB themes

**原文链接**: [https://github.com/Jacksaur/Gorgeous-GRUB](https://github.com/Jacksaur/Gorgeous-GRUB)

“Gorgeous-GRUB”：精选的GRUB主题，旨在提升启动过程的视觉体验。作者创建此资源的原因是网上许多主题质量低下且难以查找。该页面旨在突出显示分散在互联网上，具有自定义背景、字体和颜色的，质量尚可、制作精良的主题。

文章强调了自定义主题以满足个人偏好的简易性，鼓励用户尝试背景、元素位置和配色方案。它提供了有用的工具和教程链接，包括用于从存储库下载单个文件的GitZip、用于进一步自定义的GRUB-Tweaks、主题教程以及背景循环脚本。

该页面还鼓励用户通过在Pling上对主题进行评分并在Github上给存储库加星来支持创作者，从而为社区做出贡献。主要部分是超过40个独立GRUB主题和主题集的列表供选择。

---

## 13. VITs和CNNs的速度

**原文标题**: The Speed of VITs and CNNs

**原文链接**: [https://lucasb.eyer.be/articles/vit_cnn_speed.html](https://lucasb.eyer.be/articles/vit_cnn_speed.html)

卢卡斯·拜尔的这篇文章挑战了视觉Transformer (ViT) 在高分辨率下不如卷积神经网络 (CNN) 实用的观点。拜尔认为，ViT 可以很好地扩展到至少 1024x1024 像素²，这对于大多数图像编码任务来说已经足够了。

作者提供了基准数据，比较了 ViT 和 CNN 在各种 GPU（RTX 3070、RTX 4090、H100）和批量大小上的推理速度、FLOPs 和内存使用情况，得出结论：ViT 通常更快，尤其是在现代 GPU 上，并且开箱即用时内存效率更高。他还强调，FLOPs 并不能直接转化为速度。

拜尔还认为，专注于极高的分辨率通常是不必要的。他提出，对于许多应用，像自然图像的 224 像素²、富含文本图像的 448 像素² 和文档的 896 像素² 这样的分辨率就足够了。他通过使用不同方法调整大小的各种图像类型证明了这一点，并强调计算机视觉模型不需要人类观看所需的美学清晰度。

文章进一步讨论了增加分辨率会增加模型的容量 (FLOPs)，并且在高分辨率下性能的显著提升可以归因于这种容量的增加，而不仅仅是分辨率本身。最后，它介绍了局部注意力机制，特别是 ViTDet 架构，作为一种简单有效的方法，使 ViT 在高分辨率下更快且更节省内存。作者还承认，像 MoCo v3、SimCLR、DINO 和 Masked Autoencoders 这样的想法可能比 CNN 更适合 ViT。

---

## 14. DuckDB可能是过去十年最重要的地理空间软件。

**原文标题**: DuckDB is probably the most important geospatial software of the last decade

**原文链接**: [https://www.dbreunig.com/2025/05/03/duckdb-is-the-most-impactful-geospatial-software-in-a-decade.html](https://www.dbreunig.com/2025/05/03/duckdb-is-the-most-impactful-geospatial-software-in-a-decade.html)

本文认为，DuckDB的空间扩展是近十年来最重要的地理空间软件开发成果，极大地拓宽了对地理空间数据和工具的访问渠道。作者认为，将地理空间功能嵌入DuckDB这类通用数据工具中，降低了入门门槛，使更广泛的受众能够参与地理数据的使用。

文章引用了一张图表，显示2023年末人们对“地理空间”的兴趣复苏，这与DuckDB空间扩展的发布相吻合。在DuckDB之前，开始进行地理空间分析通常涉及复杂的安装和专业的数据库，这让许多普通数据用户望而却步。DuckDB将这一过程简化为几行SQL代码。

作者认为，诸如Overture Maps Foundation等倡议的成功，可能部分归功于DuckDB的空间扩展所提供的可访问性。DuckDB团队的Max评论强调了将标准FOSS GIS软件包（包括PROJ数据库）静态捆绑到一个具有最少依赖项的二进制文件中，并在多个平台上提供一致性能的重要性。

最终，作者赞扬了DuckDB团队通过承担复杂的底层任务（例如通过GDAL进行格式转换和基于SQL的转换）来简化用户体验，从而使地理空间分析更易于访问和用户友好。

---

## 15. 无线USB出了什么问题

**原文标题**: What went wrong with wireless USB

**原文链接**: [http://oldvcr.blogspot.com/2025/05/what-went-wrong-with-wireless-usb.html](http://oldvcr.blogspot.com/2025/05/what-went-wrong-with-wireless-usb.html)

本文探讨了无线USB技术的兴衰，深入研究了相互竞争的标准及其最终失败的原因。文章首先解释了无线USB背后的动机，即对无线个人区域网络（WPAN）的渴望以及早期蓝牙的局限性。无线USB的核心技术是超宽带（UWB），它利用短时、低功率脉冲进行高带宽通信。

文章随后详细介绍了两种相互竞争的UWB实现方案之间的标准之争：DS-UWB（由摩托罗拉/飞思卡尔支持）和MB-OFDM（由英特尔倡导）。DS-UWB采用直接序列扩频，而MB-OFDM使用多个子载波和时频编码。这种不兼容性导致市场分裂并阻碍了普及。

尽管存在标准之争，原始设备制造商（OEM）还是探索了潜在的应用，包括取代蓝牙和火线。摩托罗拉/飞思卡尔推出了Cable-Free USB（CF-USB），而英特尔则率先推出了Certified Wireless USB（CW-USB）。CF-USB旨在与有线USB实现更紧密的兼容，支持所有传输类型，而CW-USB虽然更灵活，但需要新的驱动程序和操作系统支持，从而延缓了其开发。

最终，贝尔金的Cable-Free USB套件等CF-USB产品率先出现。文章戛然而止，为讨论这些技术的命运奠定了基础。相互竞争的标准、延误的开发以及最终，改进的Wi-Fi等替代无线技术的兴起可能促成了无线USB的衰落。

---

## 16. 从红外到X射线的星系视觉盛宴

**原文标题**: A visual feast of galaxies, from infrared to X-ray

**原文链接**: [https://www.esa.int/ESA_Multimedia/Images/2025/04/A_visual_feast_of_galaxies_from_infrared_to_X-ray](https://www.esa.int/ESA_Multimedia/Images/2025/04/A_visual_feast_of_galaxies_from_infrared_to_X-ray)

詹姆斯·韦布、哈勃和XMM-牛顿望远镜联袂呈现星系壮丽景象

---

## 17. Tippy Coco：一款受史莱姆排球启发的免费开源游戏

**原文标题**: Tippy Coco: A Free, Open-Source Game Inspired by Slime Volleyball

**原文链接**: [https://tippycoco.com/](https://tippycoco.com/)

Tippy Coco是一款受史莱姆排球启发的免费开源游戏。它专为电脑设计，而非手机或平板电脑。文本明确指出，虽然iPad可能搭配折叠键盘可以运行，但该游戏与手机设备不兼容。文本随后表明游戏已准备就绪，提示用户按下空格键开始游戏。

---

## 18. 科德细胞自动机

**原文标题**: Codd's Cellular Automaton

**原文链接**: [https://en.wikipedia.org/wiki/Codd%27s_cellular_automaton](https://en.wikipedia.org/wiki/Codd%27s_cellular_automaton)

科德细胞自动机(CA)是由埃德加·F·科德于1968年创建的2D CA，旨在仅使用8种状态而不是29种状态来实现冯·诺伊曼CA的计算和构造通用性。科德在理论上证明了他的CA中存在一种自我复制机器，类似于冯·诺伊曼的通用构造器，尽管多年来一直未能完全实现。

在冯·诺伊曼工作的基础上，科德更简单的CA引出了关于自我复制的*必要*逻辑组织的问题。后来，埃德温·罗杰·班克斯创建了一个具有通用计算和构造能力的4状态CA。约翰·德沃雷改进了科德的规则以减小设计尺寸，并于1992年展示了德沃雷设计的模拟。克里斯托弗·兰顿于1984年进一步修改了科德的CA，创建了兰顿环，它以更少的细胞展示了自我复制，但缺乏通用计算能力。

CA规则集的比较揭示了状态数量、对称性、通用性和自我复制机器尺寸之间的权衡。科德的CA使用具有旋转对称性的冯·诺伊曼邻域，并采用特定的信号序列来完成诸如扩展、缩回、标记和擦除细胞之类的任务。

尽管科德设计了一种基于王氏W机的自复制计算机，但其复杂性阻碍了实际应用。直到2009年，蒂姆·赫顿才构建了一个显式配置，这需要对科德的设计进行轻微修改。

---

## 19. 传奇Bose魔毯悬挂系统终于走向全球

**原文标题**: Legendary Bose Magic Carpet Suspension Is Finally Going Global

**原文链接**: [https://www.thedrive.com/news/legendary-bose-magic-carpet-suspension-is-finally-going-global](https://www.thedrive.com/news/legendary-bose-magic-carpet-suspension-is-finally-going-global)

文章讨论了由 Bose 在 20 多年前开发、备受期待的“魔毯”悬架系统终于进入量产车型的消息。该系统采用机电主动悬架来消除道路不平，最初被认为不适合大规模生产。

然而，这项技术被 ClearMotion 收购并进一步开发，现已在中国电动汽车蔚来 ET9 上首次亮相。这标志着将该悬架系统整合到 300 万辆蔚来汽车中的协议的开始，有可能降低成本并为更广泛的应用铺平道路。

ClearMotion 还与保时捷合作，并与其他欧洲汽车制造商进行谈判。保时捷将使用 ClearMotion1 并推出 RoadMotion，该软件创建本地化的街道剖面图以自动调整悬架。虽然与最初使用线性电机的 Bose 系统不完全相同，但 ClearMotion 的版本调整了控制软件，并适用于带有磁性流体的主动阀减震器。

文章强调了这项技术终于从概念走向现实的意义，并指出投资公司 CYVN Holdings（迈凯伦的投资者）也是蔚来的投资者。作者认为“涓滴效应”即将到来，可能会导致该技术应用于更广泛的车辆。

---

## 20. 布莱恩·伊诺的民主理论

**原文标题**: Brian Eno's Theory of Democracy

**原文链接**: [https://www.programmablemutter.com/p/brian-enos-theory-of-democracy](https://www.programmablemutter.com/p/brian-enos-theory-of-democracy)

亨利·法雷尔的文章提出，布莱恩·伊诺关于艺术和组织的理论，为理解民主的运作方式以及如何动态地理解其稳定性提供了宝贵的见解。文章将伊诺的观点与传统的博弈论民主理解方式（以亚当·普热沃斯基的著作为例）进行了对比。普热沃斯基认为，当各方接受选举失败，因为他们预期未来会获胜时，民主是稳定的。然而，法雷尔认为，这种模式虽然有影响力，但未能解释民主倒退。

法雷尔认为，伊诺关于“组织和产生多样性”的思想为民主提供了一个更细致的“动态模型”。伊诺的音乐作品，使用简单的指令来产生涌现的多样性，而不是严格地规定结果，可以作为一个类比。这种方法强调对环境和内部变化的持续适应。它与博弈论的静态、以均衡为中心的观点形成对比，后者将环境视为一组参数，并难以解释变化。

法雷尔认为，博弈论将民主视为一种试图消除环境变化的刚性结构，而伊诺的观点则认为民主是一种通过不断调整其身份来适应环境的反应性有机体。因此，法雷尔认为，一种更类似于伊诺式的民主方法可能更好地解释了最近美国和其他地方的民主衰退。

---

## 21. 秀：我教AI实时解说乒乓球游戏

**原文标题**: Show HN: I taught AI to commentate Pong in real time

**原文链接**: [https://github.com/pncnmnp/xpong](https://github.com/pncnmnp/xpong)

这个"Show HN"帖子介绍了xPong，一款独特的Pong游戏，它集成了基于LLM的实时解说，使用OpenAI的gpt-4o-mini-tts。作者构思这个项目已经多年，并认为TTS技术的最新进展使其具有成本效益和可行性。他们预见未来的游戏机将采用类似的边缘AI来增强体育模拟和其他游戏体验。

xPong特点：

*   **AI解说游戏：** 两个AI对手进行Pong游戏，同时两个AI解说员提供开场、游戏中和结尾解说。
*   **锦标赛模拟：** 使用Elo评分进行为期15年的锦标赛模拟，最终在两名顶级选手之间进行世界锦标赛决赛。
*   **动态解说：** 解说是事件驱动的，根据游戏中发生的事件进行优先级排序，并使用最近邻搜索与历史比赛进行比较。
*   **技术实现：** 该游戏使用Eel来获得类似Electron的体验，并且需要OpenAI API密钥。提供了安装和运行游戏的说明。

作者鼓励用户探索源代码。该游戏旨在展示AI驱动的解说在游戏中的潜力，并包含玩家元数据缓存、基于事件的解说管道，甚至包括幽默元素。该项目采用MIT许可证，并感谢所使用的音效来源。

---

## 22. 为什么 Flatpak 应用占用 Linux 上如此多的磁盘空间

**原文标题**: Why Flatpak Apps Use So Much Disk Space on Linux

**原文链接**: [https://ostechnix.com/why-flatpak-apps-use-so-much-disk-space/](https://ostechnix.com/why-flatpak-apps-use-so-much-disk-space/)

以下是关于文章“为什么 Flatpak 应用在 Linux 上占用如此多的磁盘空间”的摘要，基于 Flatpak 的常识和类似主题的文章：

由于几个关键因素，Flatpak 应用通常比 Linux 上传统打包的同类应用（例如，.deb 或 .rpm）占用更多的磁盘空间：

*   **捆绑依赖项：** Flatpak 将应用程序与其所有必需的依赖项（包括库、字体和其他运行时组件）打包在一起。 这与传统的软件包管理器形成对比，后者依赖于系统范围的共享库。 这种捆绑确保应用程序拥有运行所需的一切，而不管底层系统的配置如何。

*   **共享运行时：** 虽然每个 Flatpak 应用都自带其依赖项，但一些依赖项在多个应用之间是通用的。 Flatpak 试图通过使用共享运行时来缓解磁盘空间问题。 这些运行时包含通用库和框架（如 GNOME 或 KDE 运行时），并由多个 Flatpak 应用程序共享。 但是，即使使用共享运行时，开销仍然很大，尤其是在许多应用程序需要不同或不太常见的运行时的情况下。

*   **重复和效率低下：** 即使使用共享运行时，仍然可能存在一些依赖项重复。 此外，flatpak 的设计有时会导致空间使用效率低下，从而导致整体膨胀。

*   **运行时的多个版本：** 随着时间的推移，运行时会更新。 较旧的应用程序可能仍然需要尚未更新的较旧运行时。 这导致存储同一运行时的多个版本，从而增加磁盘使用量。

*   **沙盒环境：** Flatpak 为每个应用程序创建一个沙盒环境。 这种隔离进一步增加了磁盘空间的使用量，因为基础环境将需要额外的空间。

本质上，Flatpak 优先考虑应用程序隔离、一致性和依赖项管理，但这以增加磁盘空间使用量为代价，与传统的打包方法相比。 清理未使用的运行时并定期更新 Flatpak 应用程序有助于减轻存储影响。

---

## 23. 宏基因组检测助女子摆脱神秘感染，保住视力

**原文标题**: Metagenomics test saves woman's sight after mystery infection

**原文链接**: [https://www.bbc.co.uk/news/articles/czx45vze0vyo](https://www.bbc.co.uk/news/articles/czx45vze0vyo)

29岁医生艾莉·欧文五年眼部炎症不愈，后通过宏基因组学检测挽救视力。传统检测未能确定病因，医生曾认为她患有自身免疫性疾病。病情恶化，需强效药物治疗甚至接受白内障手术，令她濒临崩溃，考虑摘除眼球。

作为最后的手段，医生采用先进的基因组测序技术——宏基因组学，分析了艾莉眼部液体样本。检测结果显示她感染了一种罕见的钩端螺旋体细菌，据推测是在亚马逊河游泳时感染。

接受抗生素治疗后，艾莉的视力得到改善，炎症也消退。宏基因组学虽然目前比标准诊断方法昂贵，但能识别传统方法遗漏的感染，是一项重大进步。专家认为，随着技术的发展，它将变得更快、更便宜、更普及，有可能成为诊断感染的一线检测方法。这项突破让艾莉能够专注于她的事业并结婚，生活质量显著提高。

---

## 24. 小型机器上的Pascal

**原文标题**: Pascal for Small Machines

**原文链接**: [http://pascal.hansotten.com/](http://pascal.hansotten.com/)

本网站致力于小型机上的Pascal编程，重点关注Niklaus Wirth及其学生的工作，以及作者本人在使用相关语言和系统方面的经验。它涵盖了一系列适用于资源受限环境的Pascal变体和实现。

本网站探索Pascal的历史和演变，从苏黎世联邦理工学院的编译器（P2和P4）开始，到UCSD Pascal P-System、Borland的Turbo Pascal和Delphi，以及现代实现如Free Pascal和Lazarus。特别关注作者自己的系统Pascal-M。该网站还深入研究Oberon系统，作为Wirth和Gutknecht的另一项贡献。

本网站提供有关Pascal各个方面的信息，包括标准Pascal和验证，Wirth、Dijkstra、Hansen和Hoare等有影响力的人物，以及UCSD Pascal、Turbo Pascal和树莓派上的Free Pascal等特定实现。它包括扫描的书籍、编译器源代码以及与UCSD Pascal、MSX和CP/M上的Pascal以及Delphi编程相关的其他资源。

“时间线”部分详细介绍了作者40多年来参与Wirth语言家族的经历，涵盖学生时代、软件工程和个人项目。该网站还包括指向验证工具、Pascal新闻通讯以及包含Pascal信息的站点的链接。

---

## 25. 相隔23年天空勘测揭示争议性行星九的证据

**原文标题**: Evidence of controversial Planet 9 uncovered in sky surveys taken 23 years apart

**原文链接**: [https://www.space.com/astronomy/solar-system/evidence-of-controversial-planet-9-uncovered-in-sky-surveys-taken-23-years-apart](https://www.space.com/astronomy/solar-system/evidence-of-controversial-planet-9-uncovered-in-sky-surveys-taken-23-years-apart)

天文学家或已通过分析相隔23年的两次红外天空巡天档案数据，发现“第九行星”这一难以捉摸的假想巨行星的潜在候选者。

第九行星最初由布朗和巴蒂金于2016年提出，旨在解释一些柯伊伯带天体的异常轨道，预计在红外光中会更亮。Terry Long Phan及其团队搜索了红外天文卫星（IRAS）和AKARI的数据，寻找在两次巡天之间似乎移动过的物体，并考虑了视差。

他们的搜索发现了一个候选天体。该天体在1983年的IRAS数据中的位置与2006年的AKARI数据中的位置不同，其差异在第九行星可能移动的范围内。虽然这令人鼓舞，但有限的数据无法计算出该天体的完整轨道，确认需要通过更近期的图像对其进行重新捕捉。

基于候选天体的亮度，Phan估计如果它是第九行星，那么它比海王星质量更大，这比最初的预期更大。第九行星高度偏心轨道的起源（可能在280到1120天文单位之间）也是一个谜。可能的解释包括其他巨行星的引力散射或来自另一个恒星系统的捕获。即将到来的南希·格雷斯·罗曼太空望远镜和维拉·C·鲁宾天文台，以及现有仪器，可能很快会证实或否定这颗长期以来寻找的行星的存在。

---

## 26. 为什么HTML自身无法实现包含？

**原文标题**: Why can't HTML alone do includes?

**原文链接**: [https://frontendmasters.com/blog/seeking-an-answer-why-cant-html-alone-do-includes/](https://frontendmasters.com/blog/seeking-an-answer-why-cant-html-alone-do-includes/)

无法访问文章链接。

---

## 27. 异世界

**原文标题**: 'Bizarro World'

**原文链接**: [https://archive.boston.com/news/globe/magazine/articles/2007/08/19/bizarro_world/](https://archive.boston.com/news/globe/magazine/articles/2007/08/19/bizarro_world/)

比利·贝克的文章《反常世界》记录了他的妻子洛瑞尝试打破Game Boy版俄罗斯方块世界纪录的故事。最初，贝克在与Twin Galaxies（官方电子游戏纪录记分牌）的凯利·R·弗勒文的谈话中，发现了洛瑞惊人的俄罗斯方块技巧。弗勒文告诉贝克，黑白Game Boy版俄罗斯方块的世界纪录是327行，并邀请洛瑞在新罕布什尔州威尔斯海滩举行的国际经典电子游戏和弹球锦标赛上尝试打破该纪录。

文章详细描述了锦标赛的气氛，突出了其对经典街机游戏的关注，以及像布莱恩·库这样的硬核游戏玩家的奉献精神，他全职追求电子游戏世界纪录。洛瑞虽然最初有些紧张，但还是为她的尝试做准备，选择了一件特别的T恤并进行了热身。

在游戏玩家和Twin Galaxies官员的观察下，洛瑞的尝试中超过了最初声明的327行纪录。 Twin Galaxies的创始人沃尔特·戴进行了评论，强调了洛瑞非凡的手眼协调能力和理解力。然而，在超过327行之后，他们得知洛瑞使用的彩色Game Boy俄罗斯方块DX版属于一个单独的类别，哈里·J·洪保持着更高的545行纪录。文章结尾暗示洛瑞有能力达到545行，但故事的结局悬而未决。

---

## 28. 固定报价搬家公司不接你电话时

**原文标题**: When flat rate movers won't answer your calls

**原文链接**: [https://aphyr.com/posts/381-when-flat-rate-movers-wont-answer-your-calls](https://aphyr.com/posts/381-when-flat-rate-movers-wont-answer-your-calls)

2023年，作者雇佣Flat Rate Movers, LTD.公司进行一次“全包”州际搬家，包括打包服务、特殊保护和“扩展估值保障”。搬家过程糟糕：另一家公司，Esquire Moving Inc.，派来一个两人团队，缺少必要的包装材料和板条箱，并在搬家过程中损坏了物品和作者的房屋。

尽管作者多次尝试联系Flat Rate Movers解决服务不足和损坏问题，但均未得到回应。该公司的理赔部门变得毫无反应，通过法律途径和消费者投诉解决问题的努力均未成功。

作者发现了一个关键的解决方法：联邦汽车运输安全管理局 (FMCSA) 数据库。该数据库提供有关搬家公司的信息，包括其保险详情。作者确定Hanover Insurance Company是Flat Rate的货物保险公司，并直接向其提出了索赔。

Hanover Insurance确认他们不知道该索赔，并且联系Flat Rate有困难。然而，根据作者提供的文件，Hanover同意赔偿损坏的货物。

虽然作者从Hanover获得了一些赔偿，但他们仍然对Flat Rate未能提供承诺的服务和赔偿房屋损坏感到不满。作者考虑过小型索赔法庭，但因其他紧迫的问题而放弃。本文强调了与不响应的搬家公司打交道的挑战，并提供了一个宝贵的提示，即通过FMCSA数据库直接向其保险公司提出索赔。

---

## 29. Elvish – 强大的脚本语言和多功能的交互式 Shell

**原文标题**: Elvish – Powerful scripting language and versatile interactive shell

**原文链接**: [https://github.com/elves/elvish](https://github.com/elves/elvish)

Elvish 是一种强大的脚本语言和交互式 Shell，专为 Linux、BSDs、macOS 和 Windows 设计，并以静态链接的二进制文件形式分发。尽管仍处于 1.0 之前的版本，且可能会有重大变更，但它对于脚本编写和交互式使用来说都是稳定的。用户文档，包括安装指南、教程和参考页面，可在官方网站 (elv.sh) 上找到。开发文档可以在存储库的 `docs` 目录中找到。该项目鼓励通过 Awesome Elvish 软件包和工具进行贡献。 大部分源代码采用 BSD 2-clause 许可证，例外情况是：`pkg/diff` 和 `pkg/rpc` 使用 BSD 3-clause 许可证，`pkg/persistent` 及其子目录使用 EPL 1.0 许可证，`pkg/md/spec` 由于分别源自 Go、Clojure 和 CommonMark 规范，因此使用 Creative Commons CC-BY-SA 4.0 许可证。

---

## 30. Debian testing/trixie amd64版本的可复现构建现已超过95%。

**原文标题**: The Debian testing/trixie release on amd64 is now reproducible for over 95%

**原文链接**: [https://micronews.debian.org/2025/1746302888.html](https://micronews.debian.org/2025/1746302888.html)

本文宣布 Debian testing/trixie 版本在 amd64 架构上已超过 95% 可重现，标志着在保护发行版免受供应链攻击方面取得了重大进展。这意味着相同的源代码可以被可靠地重新构建以产生相同的二进制文件，从而验证软件的完整性。新的 `debian-repro-status` 软件包允许用户检查其系统上安装的 Debian 软件包的可重现性状态。本文引导读者访问 https://reproduce.debian.net/ 以获取有关可重现构建的更多信息。

---

## 31. 我为什么不打算买电脑（1987）[pdf]

**原文标题**: Why I Am Not Going to Buy a Computer (1987) [pdf]

**原文链接**: [https://classes.matthewjbrown.net/teaching-files/philtech/berry-computer.pdf](https://classes.matthewjbrown.net/teaching-files/philtech/berry-computer.pdf)

由于提供的内容是PDF文件的原始数据，包含编码文本和元数据，而非文章“我为什么不打算买电脑（1987）”的实际可读内容，因此无法总结该文章。我需要文章的实际文本才能提供摘要。

---

## 32. 非官方 Ruby 使用指南

**原文标题**: The Unofficial Ruby Usage Guide

**原文链接**: [https://caliban.org/ruby/rubyguide.shtml](https://caliban.org/ruby/rubyguide.shtml)

非官方 Ruby 使用指南旨在为编写可维护的 Ruby 代码提供指导，尤其是在系统管理环境中。它源自 Google 内部文档，旨在推广一种通用的风格词汇，以提高代码的可读性和共享性。

该指南强调编写易读的代码，而非追求巧妙，提倡清晰简单的解决方案。它介绍了诸如 `irb` (交互式 Ruby) 用于代码实验，`ri` 用于在线文档，以及 Ruby 调试器等基本工具。此外，还介绍了基准测试和性能分析工具，使开发人员能够优化性能。

核心部分侧重于 Ruby 风格指南，包括代码组织、异常处理、变量使用、缩进、注释、字符串操作、库管理、访问控制、标识符命名和一致性。它强调处理警告、初始化对象以及使用默认方法参数的最佳实践。该指南倡导使用 Test::Unit 模块进行单元测试，以确保代码的正确性。

最后，该指南提供了进一步阅读的建议，包括邮件列表、书籍、文章、教程和标准资源。它还提供了 Ruby 的倡导要点，并突出了 Vim 和 Emacs 用于 Ruby 开发的有用功能。总的来说，其目标是提高 Ruby 程序员的代码清晰度、可维护性和协作能力。

---

## 33. 圣所 || 一个pq安全且沙盒化的VPN守护程序

**原文标题**: Sanctum || A pq-safe and sandboxed VPN daemon

**原文链接**: [https://github.com/jorisvink/sanctum](https://github.com/jorisvink/sanctum)

Sanctum：一个小型、可审查、后量子安全且完全特权分离的VPN守护进程，专为OpenBSD、Linux和MacOS设计。其主要优势在于其安全架构，该架构将关键功能（加密、解密、密钥交换、I/O）分离为不同的进程，每个进程都在有限的系统调用访问权限下进行沙盒化。这种隔离最大限度地减少了潜在安全漏洞的影响。

Sanctum使用混合密钥交换，结合ECDH (x25519)和ML-KEM-1024以实现后量子安全性，并使用AES256-GCM进行加密（提供替代方案）。它使用ESP以隧道模式封装流量，并使用递增的64位序列号。

Sanctum支持单向隧道（“pilgrim”和“shrine”模式），其中一方只能发送数据，而另一方只能接收，从而提供强大的单向通信保证。

“Cathedrals”是经过身份验证的中继和密钥分发点，即使在NAT之后也能促进对等连接，而Cathedral无法访问会话密钥。它们还可以分发使用每设备密钥包装的共享密钥，从而解决密钥分发问题。

构建Sanctum需要pkg-config和libsodium。配置文件指定实例名称、共享密钥路径、控制套接字、隧道配置、路由以及每个进程（bless、confess、chapel、heaven-rx/tx、purgatory-rx/tx、bishop）的用户分配。bishop进程需要提升的权限才能配置隧道。

libkyrka库允许将Sanctum协议集成到应用程序中，但它不提供与守护进程相同级别的沙盒化。

---

## 34. Julia语言的慕尼黑工业大学数值线性代数课

**原文标题**: Numerical Linear Algebra Class in Julia TUM

**原文链接**: [https://venkovic.github.io/NLA-for-CS-and-IE.html](https://venkovic.github.io/NLA-for-CS-and-IE.html)

本网页介绍了尼古拉斯·文科维奇在慕尼黑工业大学开设的“计算科学与信息工程数值线性代数”课程（CITHN2006）。该课程包含18次讲座，涵盖数值线性代数中的一系列主题，重点是使用Julia编程语言。

每次讲座都包括幻灯片形式的理论演示（提供TeX和PDF格式）以及相关的家庭作业。许多讲座还附有Julia编程作业，以Jupyter Notebook的形式呈现（提供ipynb和PDF格式）。

课程主题涵盖数值线性代数的基本方面，从基本的线性代数概念和Julia语言基础到更高级的方法。 主要主题包括：浮点运算和误差分析、稠密和稀疏线性系统的直接方法、正交化和最小二乘问题、线性系统和特征值问题的迭代方法、Krylov子空间方法、多重网格方法、预处理迭代方法、随机数值线性代数、通信避免算法和矩阵函数求值。 还有额外的笔记可供参考。 本课程全面介绍了数值线性代数，并着重强调使用Julia进行实际实施。

---

## 35. 打造摇头丸帝国的德州人

**原文标题**: The Texan Who Built an Empire of Ecstasy

**原文链接**: [https://www.texasmonthly.com/news-politics/ecstasy-starck-club-drugs-eighties-dallas/](https://www.texasmonthly.com/news-politics/ecstasy-starck-club-drugs-eighties-dallas/)

无法访问文章链接。

---

## 36. 我们不再爱 Next.js，又重新爱上了 Ruby on Rails。

**原文标题**: We fell out of love with Next.js and back in love with Ruby on Rails

**原文链接**: [https://hardcover.app/blog/part-1-how-we-fell-out-of-love-with-next-js-and-back-in-love-with-ruby-on-rails-inertia-js](https://hardcover.app/blog/part-1-how-we-fell-out-of-love-with-next-js-and-back-in-love-with-ruby-on-rails-inertia-js)

Adam Fortuna 详述了 Hardcover 从 Next.js 到使用 Inertia.js 的 Ruby on Rails 的迁移历程。最初，选择 Next.js 是因为其 SSR 功能有利于 SEO，但随后出现了缓存不明确、无服务器架构成本不可预测（Vercel 和 Google Cloud）以及开发速度缓慢等问题。一个关键的架构决策，即在客户端获取用户数据，加剧了缓存问题。

尽管迁移到了 Next.js 的 App Router，但期望的性能提升并未实现，托管成本却大幅增加。旨在提高开发速度的 Turbopack 也被证明不兼容。

在寻求替代方案时，Fortuna 优先考虑 SSR、直接数据库连接以及继续使用 React。Remix 和 Ruby on Rails 都被纳入考虑范围。Rails 与 Inertia.js 结合使用，成为了最佳解决方案。Inertia.js 能够实现高性能的 SSR 体验，利用 Rails 的缓存和路由与 React 组件。一个典型的请求包括 Rails 控制器渲染 React 组件，获取数据（通常使用 Rails 内置的缓存机制进行缓存），并将其作为 props 传递。这带来了更快的加载时间和更可预测的成本结构，同时保持了服务器端渲染和 SEO 的优势。Fortuna 强调了 Inertia.js 方法的简单性和有效性。

---

## 37. QModem 4.51 源代码

**原文标题**: QModem 4.51 Source Code

**原文链接**: [https://github.com/AaronFriel/qmodem-4.51](https://github.com/AaronFriel/qmodem-4.51)

本文宣布发布 QModem 4.51 的源代码，这是一款由 John Friel III 在 20 世纪 90 年代初开发的流行 MS-DOS 远程通信程序。此次发布旨在作为一份历史文物，供复古计算和电信爱好者研究，使他们能够探索这款经典通信软件包的内部运作。

QModem 是 Procomm 和 Telix 的竞争对手，提供诸如调制解调器协议支持（XMODEM、YMODEM、ZMODEM）、全屏拨号目录、广泛的脚本编写、程序内配置、ANSI/VT100 终端仿真、内置 BBS “主机模式” 等功能。

该存储库包含完整的 Turbo Pascal 源代码、x86 汇编程序例程、批处理文件和支持数据。关键模块包括 QMODEM.PAS（主入口点）、COMM.PAS（串行通信）、DOWNLD/UPLD*.PAS（文件传输协议）和 HOST.PAS（主机模式）。

构建 QModem 需要 Turbo Pascal 5.x/6.0 环境和诸如 Turbo Professional 等依赖项。该文档概述了潜在的构建方法，包括使用原始工具链或尝试通过 Free Pascal 进行仿真（尽管存在重大挑战）。它强调了代码的硬件依赖性以及覆盖管理的重要性。包含若干构建自动化批处理文件以供修改。此次发布的主要目标是用于研究和历史求知，对于在现代环境中运行或移植代码存在重大警告。

---

## 38. DotnetSnes: 使用C#创建SNES ROM的库

**原文标题**: DotnetSnes: Library allowing to use C# to create SNES ROMs

**原文链接**: [https://github.com/KallDrexx/DotnetSnes](https://github.com/KallDrexx/DotnetSnes)

DotnetSnes是一个允许开发者使用C#创建SNES ROM的库。它通过Dotnet To C transpiler (dntc)将.NET DLL转换为C代码，然后针对PvSnesLib SDK进行编译，从而创建一个可用的ROM。

由于SNES的限制，例如最小的类型支持、没有动态分配以及内存方面的考虑，存在一些局限性，这些限制会影响C#编码风格。尽管如此，仍然可以创建真正的SNES游戏。dntc transpiler本身在MSIL支持方面也存在局限性。

要开始使用，请克隆存储库（使用SSH），递归更新子模块，并在WSL Ubuntu上安装所需的依赖项（cmake, g++, dotnet-sdk-8.0），设置`PVSNESLIB_HOME`。该存储库包含诸如"Hello World"和"LikeMario"之类的示例项目，以演示基本功能和更复杂的游戏概念。

创建一个新项目涉及创建.NET类库，引用`DotnetSnes.Core`和`Dntc.Attributes`，定义带有`[CustomFunctionName("main")]`属性的`Main()`函数，创建带有项目特定设置的Makefile，并创建一个指示transpiler的`manifest.json`文件。诸如精灵和地图之类的资源需要手动转换，并使用`Makefile`中的`game_assets`规则进行链接。程序集内容使用`[AssemblyLabel("labelName")]`属性进行引用。

---

## 39. 我为什么在做了15年天使投资后停止，以及我现在在做什么

**原文标题**: Why I stopped angel investing after 15 years, and what I'm doing instead

**原文链接**: [https://halletecco.substack.com/p/why-i-stopped-angel-investing-after](https://halletecco.substack.com/p/why-i-stopped-angel-investing-after)

以下是基于文章标题对其内容的摘要，假设它讨论了作者停止天使投资的原因：

文章《为什么我在15年后停止了天使投资，以及我现在在做什么》详细阐述了作者在经历了相当长一段时间的天使投资后，决定退出该领域的决定。虽然具体原因将在全文中详细说明，但我们可以根据天使投资者面临的常见问题推断出一些潜在的动机。

可能的原因包括：

*   **时间投入：** 天使投资需要大量时间进行尽职调查、人脉拓展、指导和监控投资组合公司。 15 年后，作者可能希望将时间重新分配到其他追求上。
*   **财务回报：** 作者可能对其天使投资的总体财务回报不满意。早期公司的不确定性意味着许多公司会失败，而成功投资的回报可能无法弥补损失。
*   **市场变化：** 投资环境的变化，例如来自风险投资基金的竞争加剧或行业趋势的变化，可能使天使投资的吸引力降低。
*   **倦怠：** 作者可能已经经历了天使投资的高压环境带来的倦怠。
*   **优先级转移：** 个人优先级或财务目标可能已经改变，导致作者重新评估其投资策略。

文章可能随后概述了作者*代替*天使投资所做的事情。这可能包括：

*   **专注于现有投资组合：** 专注于培育和支持其现有投资组合公司。
*   **不同的投资策略：** 转向不同的资产类别，例如房地产、公共股票或风险投资基金。
*   **慈善事业：** 将更多的时间和资源投入到慈善事业中。
*   **其他商业冒险：** 追求新的创业活动或咨询机会。

本质上，这篇文章很可能是对作者天使投资经验、他们面临的挑战以及他们决定以新的方向利用自己的时间和资本的反思。

---

## 40. 最小可行博客

**原文标题**: Minimum Viable Blog

**原文链接**: [https://ostwilkens.se/blog/setting-up-blog](https://ostwilkens.se/blog/setting-up-blog)

卡尔·厄斯特·威尔肯斯描述了他创建“最小可行博客”的方法，优先考虑内容创作的简洁性和便捷性，而非像Jekyll、Ghost或WordPress这样功能丰富的博客平台。他想要一个使用他自己的域名、遵循现代Web标准、具有良好SEO、易于添加内容以及静态页面生成的博客。

他的解决方案包括一个基本的`template.html`文件、用于将Markdown转换为HTML的`markdown2`库以及一个Python脚本（`render.py`）来自动化该过程。该脚本从“posts”目录读取Markdown文件，使用模板将它们转换为HTML，并将生成的HTML文件保存在“blog”目录中。该脚本还会生成一个链接到所有博客文章的索引页面。

`template.html`文件提供了博客的基本HTML结构和样式。`render.py`脚本读取此模板，然后迭代“posts”目录中的子目录。对于每个子目录，它读取一个`eng.md`文件，从第一个`#`标题中提取标题，将Markdown内容转换为HTML，将模板中的`{{ content }}`占位符替换为生成的HTML，并保存最终的HTML文件。它还会构建一个包含每个帖子链接的索引页面。作者使用O1（可能是一个大型语言模型）来生成`render.py`脚本。

关键在于以最小的依赖性实现自动化，以最低的开销获得一个功能性博客。作者在结尾附上了一首深夜音乐推荐。

---

## 41. Google Gemini 的 LLM API 最差。

**原文标题**: Google Gemini has the worst LLM API

**原文链接**: [https://venki.dev/notes/google-gemini-is-bad](https://venki.dev/notes/google-gemini-is-bad)

无法访问文章链接。

---

## 42. Bethesda认为粉丝重制版《湮灭》“非常特别”，并支持它。

**原文标题**: Bethesda Thinks Fan Remaster of Oblivion Is 'Very Special' and Supports It

**原文链接**: [https://kotaku.com/bethesda-oblivion-remastered-skyblivion-mod-support-1851778773](https://kotaku.com/bethesda-oblivion-remastered-skyblivion-mod-support-1851778773)

本文探讨了贝塞斯达对Skyblivion的积极反应。Skyblivion是一款开发已久的粉丝模组，旨在在《天际》引擎中重现《上古卷轴IV：湮没》。尽管贝塞斯达最近发布了他们自己的《湮没》重制版，但他们仍然支持Skyblivion项目。

贝塞斯达的开发者Dan Lee曾在原版《湮没》及其重制版上工作，他在开发者聚焦视频中表达了对Skyblivion的兴奋之情，甚至加入了该模组的游戏画面。他称赞了模组制作者的诠释，并称之为“湮没粉丝的伟大一年”。

Skyblivion团队对Lee的评论做出了积极回应，表达了他们自己发布该模组的兴奋之情。这并非一次性的姿态；贝塞斯达一直以来都非常支持，甚至向Skyblivion团队发送了《湮没》重制版的拷贝。

本文强调这是一个大型发行商支持粉丝制作项目的正面例子，与任天堂和Take-Two等公司经常采取的诉讼方式形成对比。这种支持姿态表明了贝塞斯达对其社区的欣赏以及他们对游戏模组制作的热情。

---

## 43. 战略石油轰炸行动

**原文标题**: The Strategic Oil Bombing Campaign

**原文链接**: [https://www.calum-douglas.com/the-strategic-oil-bombing-campaign/](https://www.calum-douglas.com/the-strategic-oil-bombing-campaign/)

卡勒姆·E·道格拉斯的这篇文章探讨了二战期间盟军自1944年3月开始对德国石油轰炸行动取得的战略性成功。文章将重点从道德辩论转移开来，深入研究了优先将石化工业作为目标的实际原因。

作者强调了众多潜在目标，从电力和粮食生产到军事设施。然而，文章解释说，石化工业之所以成为关键，是因为它对德国的战争努力至关重要，包括燃料生产、氮气以及用于推进剂和肥料的氨。摧毁相对较少的炼油厂（约20座）可能会削弱德国军队，尤其是德国空军。

盟军在英国和美国工程师，甚至像F.R. Banks这样的间谍收集的战前情报的帮助下，清楚地了解了德国的燃料生产和库存。文章还讨论了不断发展的战斗机护航战术，解释了P-51野马战斗机的引入如何对确保空中优势至关重要。野马在性能上优于P-38和P-47，使盟军战斗机能够积极交战并摧毁德国空军，从而为有效的轰炸扫清了道路。

尽管英国皇家空军在不列颠战役期间曾试图以德国石油设施为目标，但由于精度和火力不足而失败。然而，凭借更好的情报、改进的战术和卓越的战斗机护航，1944年的战略石油攻势最终被证明在削弱德国军队方面非常成功。

---

## 44. 美国批准CRISPR猪用于食品

**原文标题**: The US has approved CRISPR pigs for food

**原文链接**: [https://www.technologyreview.com/2025/05/02/1116059/the-us-approves-crispr-pigs-for-food/](https://www.technologyreview.com/2025/05/02/1116059/the-us-approves-crispr-pigs-for-food/)

美国FDA批准了英国公司Genus开发的CRISPR编辑猪用于食用，这些猪具有抵抗猪繁殖与呼吸综合征（PRRS）的能力，PRRS是一种影响工厂化养殖猪的高成本呼吸道病毒。这些猪代表了转基因食用动物的重大进步，可能每年为美国猪肉产业节省3亿美元。

Genus利用CRISPR技术去除了PRRS病毒进入细胞所使用的受体，使猪几乎对该疾病免疫。虽然该项目引发了与中国CRISPR婴儿事件类似的伦理考量，但其经济效益是巨大的。

该批准标志着一个重要的里程碑，是首个进入食品系统的CRISPR编辑动物产品，提升了Genus的股票价值。然而，该公司正在寻求墨西哥、加拿大、日本和中国等主要出口市场的批准，然后才会在美国市场推出猪肉，可能在明年某个时候。他们预计不需要将猪肉标记为生物工程产品。

这篇文章将基因编辑的这种实用应用与更具戏剧性的项目进行了对比，例如试图复活已灭绝物种或创造奇幻动物。它强调了CRISPR和DNA测序在改善牲畜健康和降低动物向人类传播疾病风险方面的日益增长的潜力，同时也提醒人们注意转基因动物在进入市场时面临的监管障碍和挑战。

---

## 45. 在苹果神经引擎（ANE）上运行大型语言模型

**原文标题**: Run LLMs on Apple Neural Engine (ANE)

**原文链接**: [https://github.com/Anemll/Anemll](https://github.com/Anemll/Anemll)

ANEMLL 是一个开源项目，旨在简化在 Apple 神经网络引擎 (ANE) 上运行大型语言模型 (LLM) 的流程，实现低功耗、设备端推理，确保隐私和安全。 0.3.0 版本（Alpha）专注于将 Hugging Face 模型转换为 ANE 的 CoreML 格式。

主要组件包括：
*   **LLM 转换工具:** 直接从 Hugging Face 转换模型的脚本。
*   **Swift 参考实现:** 针对 Swift 应用程序的优化推理代码。
*   **Python 示例代码:** 用于测试和基础/高级聊天界面的工具。
*   **iOS/macOS 示例应用程序:** 开箱即用的示例应用程序。
*   **ANEMLL-BENCH:** 用于性能测试和模型优化的基准测试。

该版本支持 LLAMA 模型（包括 DeepSeek 和 DeepHermes 提炼模型），并在 Hugging Face 上提供预转换模型。 用户可以下载模型，使用提供的脚本转换它们，并使用 Python 或 Swift 运行它们。

该项目提供示例 iOS/macOS 应用程序、Swift CLI 参考以及模型转换和使用方面的详细指南。 需要带有 ANE 的 macOS Sequoia、至少 16GB RAM 和 Python 3.9。 安装说明包括设置虚拟环境、安装依赖项和配置 Xcode 命令行工具。

该项目鼓励贡献，并提供联系方式以获得支持。 它采用 MIT 许可证。

---

## 46. Netflix的专利揭示了电影观看的未来

**原文标题**: What Netflix's patents reveal about the future of watching movies

**原文链接**: [https://stephenfollows.com/p/what-netflixs-patents-reveal](https://stephenfollows.com/p/what-netflixs-patents-reveal)

本文深入探讨奈飞的专利组合，揭示这家流媒体巨头如何塑造未来观影方式，涵盖的不仅是消费，还包括制作和营销。奈飞的大部分专利围绕内容存储、检索和传送展开，其次是个性化内容推荐。

本文将奈飞的专利分解为四个关键领域：

1.  **我们得到什么：** 重点关注下一代推荐引擎，它们变得更快、更开放，并且能够通过推荐超越典型观看模式的新颖内容来解决“推荐泡沫”。这些引擎会考虑多种因素，从观看历史到区域趋势，甚至根据用户的浏览行为实时调整。

2.  **如何制作：** 讨论人工智能和自动化如何改变电影剪辑、本地化和营销。 这包括人工智能生成的预告片、自动剪辑建议以及自动视觉特效和对象跟踪。

3.  **奈飞的界面呈现：** 强调奈飞界面本身的个性化和互动性。

4.  **幕后花絮：** 重点关注新的基础设施和交付方式。

奈飞使用A/B测试来优化艺术作品和剧集顺序，其决策延伸至内容创作，人工智能会选择宣传艺术作品并生成预告片。人工智能驱动的配音和字幕实现了全球发行，而数据驱动的营销会实时改进艺术作品和营销活动。这些专利为电影制作人提供了对观众期望以及电影行业未来工作流程的深刻见解。

---

## 47. AMIBIOS程序员指南 (1993) [pdf]

**原文标题**: Programmers Guide to the AMIBIOS (1993) [pdf]

**原文链接**: [http://bitsavers.org/pdf/americanMegatrends/Programmers_Guide_to_the_AMIBIOS_1993.pdf](http://bitsavers.org/pdf/americanMegatrends/Programmers_Guide_to_the_AMIBIOS_1993.pdf)

题为“AMIBIOS程序员指南(1993)”的文档是一个PDF文件，其内容主要为与PDF格式相关的二进制数据和元数据。可见内容主要是PDF结构元素，如对象定义、流和引用。存在表明创建和修改日期的时间戳，时间为2010年8月。该文档很可能使用Adobe Acrobat 8.2创建。

PDF结构中嵌入了图像数据流，可通过“JFIF”标头识别。解压缩的数据表明，存在可能压缩的图像数据，并散布着PDF标记。其他片段似乎包含PDF渲染器关于颜色处理和页面布局的指令。

PDF流和嵌入图像中包含的文本内容包括分散的字符、数字、格式指令和版权信息。还可见类似代码的片段，包含可识别的关键字和语法，表明它可能包含汇编代码、反汇编输出或与系统BIOS例程相关的材料。

总而言之，该文档是一个PDF，可能包含与系统BIOS编程相关的图像内容。由于大量编码，需要进行提取和更深入的分析才能揭示指南的完整预期目的和功能。

---

## 48. 创造 Commodore 64：工程师的故事

**原文标题**: Creating the Commodore 64: The Engineers' Story

**原文链接**: [https://spectrum.ieee.org/commodore-64](https://spectrum.ieee.org/commodore-64)

本文从MOS Technology工程师的角度，讲述了史上最畅销电脑Commodore 64 (C-64) 的诞生过程。最初，该项目旨在为电子游戏设计先进的图形和声音芯片，后来，Commodore总裁Jack Tramiel将其重新定位，打造一台拥有64KB内存的家用电脑，参加1982年的消费电子展（CES）。

在Albert Charpentier和Charles Winterble的指导下，包括Robert Yannes在内的一个小团队在不到九个月的时间里开发出了这些芯片，他们利用MOS Technology内部的芯片制造厂进行快速原型设计和调试。工程师们优先考虑成本效益和简洁性，重复使用VIC-20的组件，并专注于最大限度地减少组件数量。设计过程包括对竞争对手技术的广泛研究，并将诸如精灵和位图图形等成功的功能融入到他们的设计中。

Commodore 64在1982年1月的CES上获得热烈好评后，迅速投入生产，并取得了商业上的成功，这主要归功于其令人印象深刻的图形和声音性能，以及595美元（后来低至149美元）的极低价格，击败了竞争对手。本文强调了MOS Technology独特的内部制造的关键作用，它可以通过利用闲置的设备和人员来实现快速迭代和成本节约。该设计强调模块化而非紧凑性，优先考虑开发速度而非硅利用率。

---

## 49. 人工智能代理协议综述

**原文标题**: A Survey of AI Agent Protocols

**原文链接**: [https://arxiv.org/abs/2504.16736](https://arxiv.org/abs/2504.16736)

人工智能代理协议综述：本文探讨了大型语言模型（LLM）代理缺乏标准化通信协议这一新兴问题。随着LLM代理在各行各业的日益普及，这些代理无法与外部工具和数据源无缝交互，阻碍了它们的协作、可扩展性以及处理复杂任务的能力。

作者提出了一种系统的二维分类方法，对现有代理协议进行分类，区分了面向上下文和代理间协议，以及通用和特定领域协议。他们还进行了侧重于安全性、可扩展性和延迟的对比性能分析。

本文进一步探讨了代理协议的未来研究方向，强调了对适应性、隐私保护、基于群组的交互能力、分层架构以及集体智能基础设施的需求。作者预计他们的工作将为参与智能代理通信基础设施设计、评估和集成的研究人员和工程师提供宝贵的资源。

---

## 50. 重新思考DNS解析器：部署至CF Workers、Deno Deploy、Fastly、Fly.io

**原文标题**: RethinkDNS Resolver That Deploys to CF Workers, Deno Deploy, Fastly, Fly.io

**原文链接**: [https://github.com/serverless-dns/serverless-dns](https://github.com/serverless-dns/serverless-dns)

无服务器 DNS：基于无服务器平台的 Pi-Hole 式内容拦截 DNS 解析器

---

## 51. 一个简单的Common Lisp Web应用

**原文标题**: A simple Common Lisp web app

**原文链接**: [https://www.scotto.me/blog/a-simple-common-lisp-web-app/](https://www.scotto.me/blog/a-simple-common-lisp-web-app/)

本文提供了一个创建简单Common Lisp Web应用程序（留言簿）的教程，旨在解决Common Lisp生态系统中常常缺乏初学者友好型文档的问题。它利用现代库来简化开发过程，并提供类似于其他语言的开发体验。

本教程涵盖了使用`cl-project`设置新的Common Lisp项目、使用Quicklisp管理依赖项，以及使用Clack、Lack、Caveman2、djula和cl-dbi等库构建Web应用程序。Clack和Lack处理服务器设置和中间件（例如，静态文件服务），而Caveman2充当Web框架，djula处理模板渲染，cl-dbi管理数据库交互。

本文概述了配置应用程序的步骤，包括数据库连接设置，并详细介绍了数据库模式（SQLite）的创建。它展示了如何在Caveman2中使用`defroute`定义路由，用于显示消息、添加新消息和删除现有消息。它还介绍了如何使用djula渲染模板，并实现了一个将时间戳转换为可读日期时间字符串的函数。最后，它定义了一个自定义的404错误异常处理程序。本文最后提供了加载和运行项目的说明，为Common Lisp Web开发提供了一个起点。

---

## 52. 巴菲特将卸任伯克希尔掌门，结束长达六十年的执掌。

**原文标题**: Buffett to step down following six-decade run atop Berkshire

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-03/warren-buffett-to-step-down-from-berkshire-hathaway-at-year-end](https://www.bloomberg.com/news/articles/2025-05-03/warren-buffett-to-step-down-from-berkshire-hathaway-at-year-end)

无法访问文章链接。

---

## 53. 责任真空

**原文标题**: Accountability Sinks

**原文链接**: [https://250bpm.substack.com/p/accountability-sinks](https://250bpm.substack.com/p/accountability-sinks)

无法访问文章链接。

---

## 54. 理解-j：J 编程语言入门

**原文标题**: Understanding-j: An introduction to the J programming language that gets to the

**原文链接**: [https://github.com/bugsbugsbux/understanding-j](https://github.com/bugsbugsbux/understanding-j)

本文介绍了J编程语言，它是APL的后继者，以其数学符号和数组操作能力而闻名。文章强调一种实用、动手实践的方法，鼓励读者运行示例并查阅附录以了解所涵盖的内置函数。

J语言涵盖的关键方面包括：

*   **数据类型：** 各种数字表示法（整数、浮点数、复数、N进制数），布尔值（表示为0和1），字符串（UTF-8编码的字面量）。名词是数据值，包括数组和盒子。符号和稀疏数组是特殊的数据类型。
*   **数组：** 数组是基础，所有元素具有相同类型和一致的形状。形状即秩。
*   **盒子：** 任何数据类型的容器，能够实现异构列表和树状结构。
*   **函数（动词）：** 一元（一个参数）和二元（两个参数）函数，特殊变量`x`和`y`分别代表左参数和右参数。函数可以是二义性的，具有一元和二元形式。
*   **修饰符（副词、连词）：** 修改其他函数或表达式的函数，可以通过`u`、`v`、`m`和`n`访问原始参数。
*   **赋值：** 全局赋值 (`=:` ) 和局部赋值 (`=.`)。
*   **导入代码：** 用于从外部文件加载和执行代码的动词，如`load`、`loadd`和`require`。
*   **显式定义：** 使用 `:` 连词创建函数和名词，使用整数代码指定实体类型。
*   **直接定义 (DDs)：** 使用双大括号 `{{}}` 定义函数的简洁方法，通过变量名推断函数类型。
*   **索引：** 本文引用了像 {:: 这样的函数，用于索引复杂树状结构中的元素。

文章还提供了J语言重要资源的链接，例如Jsoftware主页、在线解释器、词汇表文档和参考卡。

---

## 55. “我找到了你爸爸”：一位失踪登山者的谜团

**原文标题**: 'I found your dad': The mystery of a missing climber

**原文链接**: [https://www.espn.com/olympics/story/_/id/44690603/bill-stampfl-missing-climber-peru-huascaran](https://www.espn.com/olympics/story/_/id/44690603/bill-stampfl-missing-climber-peru-huascaran)

ESPN文章《“我找到你爸爸了”：失踪登山者的谜团》详细讲述了美国登山者比尔·斯坦普弗尔于1972年在秘鲁瓦斯卡兰山失踪的故事。文章主要讲述了他的儿子克里斯·斯坦普弗尔为寻找父亲遗骸并了解他失踪情况所做的努力。

几十年来，比尔·斯坦普弗尔一直被认为是在探险期间因雪崩而遇难。然而，克里斯从未完全接受这种说法。在寻求了结和更深入了解父亲的渴望的驱使下，他开始了独自调查，并最终多次前往秘鲁。

文章强调了克里斯面临的挑战，包括克服瓦斯卡兰山的险恶地形，应对秘鲁的官僚障碍，以及寻找父亲遗骸所带来的情感打击。他采访了当地的向导和登山者，将关于他父亲探险以及可能发生事故地点的零碎信息拼凑起来。

最终，克里斯收到了秘鲁向导米格尔发来的消息：“我找到你爸爸了。”米格尔发现了一些骨骼遗骸、衣物和装备，与比尔·斯坦普弗尔在1972年携带的物品相符。DNA检测证实这些遗骸是比尔的，这让克里斯得以将他带回家。

文章探讨了这一发现对克里斯的深刻影响，它带来了一种了结感，并使他能够与父亲的冒险精神联系起来。这是一个关于毅力、家族遗产以及人类精神在悲剧发生几十年后找到答案的持久力量的故事。

---

## 56. 太阳的未来并不追随太阳

**原文标题**: The future of solar doesn't track the sun

**原文链接**: [https://terraformindustries.wordpress.com/2025/04/29/the-future-of-solar-doesnt-track-the-sun/](https://terraformindustries.wordpress.com/2025/04/29/the-future-of-solar-doesnt-track-the-sun/)

太阳能板安装的经济性演变：单轴跟踪阵列是否仍为最优选择？

本文探讨了太阳能板安装不断演变的经济性，质疑在光伏组件价格大幅下降的情况下，单轴跟踪阵列是否仍然是最优选择。作者Xavier Dedenbach认为，固定式东西向阵列正变得越来越有竞争力，在某些情况下甚至可能超过跟踪阵列。

虽然跟踪阵列可以最大化每个太阳能板的能量产出，但随着光伏组件变得更便宜，东西向阵列具有材料和劳动力成本更低、占地面积更小以及成本效益不断提高等优势。跟踪阵列需要复杂的机械装置、坚固的结构和精密的跟踪系统，从而增加了其成本。文章强调，近年来光伏组件的成本降低速度已显著超过跟踪器的成本降低速度，这可能会削弱跟踪系统的经济优势。

作者比较了这两种系统，概述了单轴跟踪阵列和东西向阵列的组件和功能，并以Jurchen PEG系统为例，说明了东西向系统。文章使用美国不同气候下的模拟来确定产生1兆瓦等效功率输出所需的太阳能板数量。结论倾向于认为，如果仅考虑每瓦价格，东西向阵列是明显的经济选择，但强调环境因素，特别是冰雹等恶劣天气，可能仍使某些地区的更为坚固和可调节的跟踪阵列更具优势。

---

## 57. 人工智能节省的时间被创造的新工作抵消，研究表明

**原文标题**: Time saved by AI offset by new work created, study suggests

**原文链接**: [https://arstechnica.com/ai/2025/05/time-saved-by-ai-offset-by-new-work-created-study-suggests/](https://arstechnica.com/ai/2025/05/time-saved-by-ai-offset-by-new-work-created-study-suggests/)

无法访问文章链接。

---

## 58. 复古计算

**原文标题**: Retro Computing

**原文链接**: [http://retro.hansotten.nl/](http://retro.hansotten.nl/)

本网站致力于复古计算领域，专注于 8 位小型计算机系统和电子产品。作者详细介绍了他们对 KIM-1 以及 Apple 1 和 Junior 等相关设备和 Z80 系统的个人兴趣和经验。内容结构为一个个人档案和研究资源，供其他可能觉得有用的人分享。

本网站包含大量资源，包括：

*   **最新文章：** 关于各种复古计算项目和信息的修改和添加的更新，特别是与 KIM-1 及其相关硬件相关的更新。
*   **杂志：** 探索像 Elektuur 和 Radio Bulletin 这样的电子杂志在普及微处理器方面的作用，以及作者作为 Radio Bulletin 技术编辑的参与。
*   **单板计算机 (SBC)：** SBC 的定义和讨论，强调它们在 1970 年代后期对业余爱好者和专业人士的经济性和可访问性，以及它们如何导致个人计算机的演变。
*   **特定系统和组件：** 关于 KIM-1、Apple 1、Junior 等各种系统以及 6530 和 6532 等单个 IC 的详细章节，包括手册、原理图、软件和克隆信息。
*   **软件和编程：** 用于这些系统的各种编程语言和工具的资源，包括汇编器、BASIC 解释器和其他应用程序。
*   **扩展和外围设备：** 关于复古系统的硬件扩展、接口和外围设备的信息，例如内存板、软盘控制器和 I/O 设备。
*   **克隆系统：** 关于 Apple 1 和 KIM-1 等流行系统的各种克隆和复制品的文档。

该网站是复古计算爱好者的综合存储库，提供历史背景、技术细节和实用资源，用于保存和使用这些老式系统。

---

## 59. Pandoc 与 MathML

**原文标题**: MathML with Pandoc

**原文链接**: [https://leancrew.com/all-this/2025/05/mathml-with-pandoc/](https://leancrew.com/all-this/2025/05/mathml-with-pandoc/)

Dr. Drang讨论了他将LaTeX方程转换为MathML以便用于其博客ANIAT的过程，他转而使用Pandoc，原因是其他转换方法不足。他强调了Pandoc的易用性，尤其是在处理多行表达式和矩阵等复杂方程时，许多其他转换器都难以处理。他提供了一个使用Pandoc转换简单方程的示例，并展示了生成的MathML代码。

文章指出了Pandoc在方程中渲染极限的一个具体错误，其中“n→∞”部分被错误地格式化为下标。他提供了Pandoc生成的MathML代码，并指出空元素`<mo>⁡</mo>`是导致错误渲染的原因，并展示了移除该元素后的正确格式。

为了简化MathML生成过程，Dr. Drang使用了一个Python脚本，该脚本接收LaTeX代码，通过Pandoc运行，然后通过删除不必要的元素和属性来清理输出，例如`<annotation>`标签、`<semantics>`包装器、块显示方程中的顶级`<mrow>`包装器，以及内联方程的`display="inline"`属性。这样做是为了使MathML代码更紧凑，以便集成到他的博客文章中。他提到使用Keyboard Maestro来自动化转换，尽管他正在考虑直接使用BBEdit。

---

## 60. 你好，我变态的朋友。

**原文标题**: Hello My Perverted Friend

**原文链接**: [https://hackerfactor.com/blog/index.php?/archives/1066-Hello-my-perverted-friend.html](https://hackerfactor.com/blog/index.php?/archives/1066-Hello-my-perverted-friend.html)

在一篇题为“你好，我的变态朋友”的博文中，尼尔·克拉维茨博士回顾了他分析垃圾邮件的历史，从识别各种团体（包括儿童和国家行为者）用于垃圾邮件中的隐蔽通道开始。随着垃圾邮件过滤器的改进，这些隐藏在垃圾邮件中的隐蔽通道大多消失了。

文章的主要焦点是他最近收到的一封垃圾邮件，这是一次典型的勒索企图，声称拥有他观看色情视频的妥协视频。该邮件要求支付 1200 美元的比特币。克拉维茨博士认为，这种骗局是薄弱而无效的，并指出与类似骗局相关的任何区块链地址都从未收到过付款。他质疑骗子的做法，并指出要求一个可能足够老练能识别骗局的人支付比特币，这是具有讽刺意味的。

克拉维茨随后探讨了此类垃圾邮件活动背后的潜在动机。他考虑了简单的勒索之外的可能性，例如测试邮件列表、评估邮件服务器安全性、评估托管提供商的滥用容忍度，或创建网络流量作为其他恶意活动的转移。

在评论区，读者提供了进一步的见解。一位评论者建议，每封电子邮件可能包含一个唯一的比特币地址，允许诈骗者追踪谁上当受骗。另一位评论者声称已经观察到对这些比特币地址的付款，这表明该骗局可能比克拉维茨博士最初评估的更成功。

---

## 61. N8n - 面向技术团队的灵活AI工作流自动化

**原文标题**: N8n – Flexible AI workflow automation for technical teams

**原文链接**: [https://n8n.io/](https://n8n.io/)

N8n 是一个灵活且强大的工作流程自动化平台，专为技术团队设计，提供可视化的拖放界面和基于代码的自定义的混合方式。与其他工具相比，这让用户能够以更大的自由度构建复杂的 AI 代理并集成各种应用程序。它可以部署在本地以实现完全控制，也可以部署在云端以获得便利。

该平台在开发者社区中很受欢迎，在 GitHub 上拥有超过 87.5k 个星标，并在 G2 上拥有很高的评分。它拥有一个超过 20 万成员的庞大社区。N8n 使 IT 运维、安全运维、开发运维和销售等技术团队能够自动化诸如员工入职、安全事件丰富、API 调用转换和客户洞察生成等任务。

主要功能包括编写 JavaScript 或 Python 代码、添加库、粘贴 cURL 请求、合并工作流程分支以及通过短反馈循环高效调试的能力。该平台还提供超过 1700 个模板，以加速项目开发。

客户评价突显了显著的效率提升。Delivery Hero 通过单个 IT 运维工作流程每月节省了 200 小时，而 StepStone 在短短两小时内完成了两周的工作量。

N8n 还提供企业级安全功能，包括本地部署、SSO SAML、LDAP、加密的密钥存储、版本控制和高级 RBAC 权限。性能监控功能包括审计日志、工作流程历史记录、自定义变量和外部存储。协作功能支持 Git 控制、隔离环境和多用户工作流程。该平台还提供可嵌入版本。

---

## 62. 构建超越谷歌翻译和DeepL翻译应用的学习经验

**原文标题**: Lessons from Building a Translator App That Beats Google Translate and DeepL

**原文链接**: [https://dingyu.me/blog/lessons-translator-app-beats-google-translate-deepl](https://dingyu.me/blog/lessons-translator-app-beats-google-translate-deepl)

本文详细介绍了作者构建 Kintoun 的经验，这是一款文档翻译应用程序，令人惊讶的是，它在某些情况下优于 Google 翻译和 DeepL。 Kintoun 擅长保持原始布局并准确翻译复杂的格式，例如文档中的语音指南，而成熟的服务在这方面却表现不佳。

作者强调了在此过程中学到的三个关键教训。 首先，Kintoun 意外的成功凸显了个人开发者在特定利基领域超越大型公司的潜力。 其次，产品分发至关重要，应优先考虑，甚至可能在开发开始之前，强调寻找积极寻求解决方案的受众的重要性。 作者强调了首先获得客户的“先假装成功，直到真正成功”的方法。

第三，作者赞扬了 Inertia.js 和 Svelte 在前端开发中的结合。 这种组合通过 Action Cable 与 Rails 集成，可以轻松创建高度响应的视图，而无需传统单页应用程序 (SPA) 的复杂性。 作者建议尝试 Inertia-Rails、Svelte 和 livestores 以实现高效的 Web 开发。

由于直接收到来自他的妻子（翻译服务用户）的积极反馈，作者发现该项目非常有意义。 他最后强调了推广 Kintoun 的持续挑战，并邀请读者尝试该应用程序并提供反馈。

---

## 63. FAA为应对空管人员短缺加剧提供更多激励措施

**原文标题**: FAA offering more incentives as air traffic controller shortage worsens

**原文链接**: [https://ktla.com/news/travel/faa-offering-more-incentives-as-air-traffic-controller-shortage-worsens/](https://ktla.com/news/travel/faa-offering-more-incentives-as-air-traffic-controller-shortage-worsens/)

无法访问文章链接。

---

## 64. 我们对亚马逊的卫星了解更多了。

**原文标题**: We know a little more about Amazon's satellites

**原文链接**: [https://arstechnica.com/space/2025/05/we-finally-know-a-little-more-about-amazons-super-secret-satellites/](https://arstechnica.com/space/2025/05/we-finally-know-a-little-more-about-amazons-super-secret-satellites/)

无法访问文章链接。

---

## 65. AI驱动机器人助力澳大利亚安装近万块太阳能板

**原文标题**: AI-driven robot installs nearly 10k solar modules in Australia

**原文链接**: [https://renewablesnow.com/news/ai-driven-robot-installs-nearly-10-000-solar-modules-in-australia-1274232/](https://renewablesnow.com/news/ai-driven-robot-installs-nearly-10-000-solar-modules-in-australia-1274232/)

好的，以下是根据标题推断出的摘要：

一个人工智能驱动的机器人在澳大利亚成功安装了近 10,000 个太阳能组件。这表明可再生能源领域，特别是太阳能农场建设中自动化技术的应用。人工智能的使用表明该机器人可能具备自主导航、物体识别（识别太阳能电池板和安装点）以及自适应控制（适应不同的地形和环境条件）等功能。该文章可能详细介绍了与传统人工安装方法相比，该机器人的效率和潜在的成本节约。它还可能涉及机器人的安全功能及其对劳动力的影响，以及具体的项目地点和机器人系统背后的公司。如此大量组件的成功安装标志着在大型太阳能项目采用机器人技术方面的一个重要里程碑，并可能暗示着太阳能农场建设的未来。

---

## 66. 不同开关的开关抖动参考波形

**原文标题**: Switch bouncing reference traces for a variety of different switches

**原文链接**: [https://github.com/gsuberland/switch_bouncing](https://github.com/gsuberland/switch_bouncing)

本仓库提供各种开关的触点弹跳行为参考数据，旨在帮助开发稳健的消抖系统。 它包含从几种不同开关收集的波形数据：拨动开关、按钮（瞬时）和钥匙开关，所有开关均来自不同的制造商，且具有不同的规格（IP 等级等）。

这些开关在下拉配置中进行了测试，并使用 PicoScope 3206B 以 8.93 MSa/s 的采样率测量了开关两端的电压。 测试包括每个开关 32 次按压，涵盖不同的致动方式（速度、力度等），以捕获一系列弹跳特性。 记录了上升沿和下降沿。

该存储库包含几个有用的资源：

*   **图表：** 开关弹跳行为的可视化表示，显示了每个设备的叠加上升沿和下降沿。
*   **分段线性数据：** 包含开关电阻值随时间变化的分段线性数据文件，允许使用 LTSpice 等软件精确模拟弹跳。
*   **原始数据：** 包含每个开关的电压和时间戳数据的 CSV 文件，可进行详细分析。

数据按设备组织，双掷开关的常开 (NO) 和常闭 (NC) 触点分别位于不同的目录中。 数据和资源均发布到公共领域。

---

## 67. 新奥尔良教我的事

**原文标题**: What New Orleans Taught Me

**原文链接**: [https://commonedge.org/what-new-orleans-taught-me/](https://commonedge.org/what-new-orleans-taught-me/)

在新奥尔良教会我的事中，作者反思了在新奥尔良度过的十年，以及离开前学到的宝贵经验。文章主要围绕三个核心主题：节奏、关怀和直觉。

新奥尔良教会了作者放慢节奏，以更注重人际关系的方式对待时间，突显了这座城市多元文化的时间观，与美国大部分地区单一的时间节奏形成对比。他将这座城市轻松慷慨的氛围与东海岸僵化的结构进行了对比。

作者探讨了“关怀”的概念，强调了新奥尔良在普世理想与亲密的社区层面支持之间取得平衡的独特能力。借鉴一项关于道德圈的研究，他认为这座城市培养了一种集体关怀的精神，这种精神超越了亲密圈子，延伸到陌生人和更广泛的社区。他认为这种具象化的政治对于超越政治两极分化至关重要。

最后，作者讨论了直觉的重要性以及“发自内心的”感受。他描述了学习信任自己的直觉，以及意识到何时该离开新奥尔良，即使这座城市已经变得舒适和熟悉。他的离开是出于对变革的需求以及参与更广泛挑战的愿望。

作者最后强调了新奥尔良提供的独特经验，倡导将这些价值观融入更广阔的视野，并认识到南方在吸收国家选择方面的作用。

---

## 68. Tcl 中的闭包

**原文标题**: Closures in Tcl

**原文链接**: [https://world-playground-deceit.net/blog/2024/10/tcl-closures.html](https://world-playground-deceit.net/blog/2024/10/tcl-closures.html)

本文探讨了 Tcl 中闭包的概念，其动机源于围绕 Tcl/Tk 9.0 发布的讨论以及对缺乏原生闭包支持的看法。作者阐明了他们对“闭包”的理解，强调真正的环境捕获（如在 Python 和 Common Lisp 中）而不是简单的值复制（如在 C++ 中）。

作者强调了真正闭包的实用性，特别是在诸如使用回调遍历数据结构以收集特定项目等场景中，其中捕获的环境需要超出初始范围持续存在。

虽然 Tcl 没有内置的 lambda 或闭包，但作者利用 Tcl 的 `apply` 命令（自 Tcl 8.5 起可用）创建了一个 `lambda` proc，提供了基本的 lambda 功能和部分应用。

本文的核心详细介绍了作者使用 TclOO 创建唯一命名空间来模拟 Tcl 中闭包的方法。这允许将与闭包相关的变量存储在对象的命名空间中。`closure::new` proc 创建一个闭包对象，将当前作用域中指定的变量捕获到对象中的 `lexenv` 字典中。然后，`apply` 方法在对象的上下文中执行闭包的代码。`lexenv` 方法提供对捕获变量的访问。

当前的实现复制环境的值，而不是引用它们，并且需要手动销毁 (`closure destroy`) 以防止内存泄漏，直到 TIP 550 实现。作者还简要地考虑了更复杂的环境回写和生命周期管理的想法。

---

## 69. Redis 再次开源

**原文标题**: Redis is open source again

**原文链接**: [https://antirez.com/news/151](https://antirez.com/news/151)

Redis再次开源公告

---

## 70. 马拉松主播，直播三年，面临孤立与倦怠

**原文标题**: Marathon streamer, online for three years, faces isolation and burnout

**原文链接**: [https://www.washingtonpost.com/technology/2025/05/04/longest-marathon-streamer-emilycc/](https://www.washingtonpost.com/technology/2025/05/04/longest-marathon-streamer-emilycc/)

无法访问文章链接。

---

## 71. Show HN: 在 JetBrains AI Assistant 中使用第三方 LLM API

**原文标题**: Show HN: Use Third Party LLM API in JetBrains AI Assistant

**原文链接**: [https://github.com/Stream29/ProxyAsLocalModel](https://github.com/Stream29/ProxyAsLocalModel)

此“Show HN”帖子介绍了`ProxyAsLocalModel`，一个旨在JetBrains AI Assistant中启用第三方LLM API的工具。作者开发它的原因是JetBrains AI Assistant的免费额度很快耗尽，并且他们希望利用现有的API密钥来使用诸如Gemini和Qwen之类的服务。

该工具充当代理服务器，模仿LM Studio和Ollama的API，这些API由JetBrains AI Assistant原生支持。这允许用户配置AI Assistant连接到`ProxyAsLocalModel`，然后由它将请求转发到配置的第三方LLM API。

该应用程序使用Kotlin、Ktor和kotlinx.serialization构建，强调无反射方法，以兼容GraalVM原生镜像编译。这产生了一个跨平台、快速启动的应用程序，以胖JAR和原生镜像两种方式分发。

`ProxyAsLocalModel`目前支持代理来自OpenAI、Claude、DashScope（阿里巴巴Qwen）、Gemini、Deepseek、Mistral、SiliconFlow和OpenRouter的请求。它支持流式聊天完成API，并提供了通过可配置的YAML文件设置代理服务器的详细说明，包括API密钥和模型列表。该配置文件支持热重载，在保存更改时自动更新服务器。该项目旨在弥合JetBrains AI Assistant与更广泛的LLM提供商之间的差距。

---

## 72. 燃烧的毛泽东

**原文标题**: Burning Mao

**原文链接**: [https://granta.com/burning-mao/](https://granta.com/burning-mao/)

在《燃烧的毛》中，费尔南达·埃伯斯塔特回忆了1977年夏天她在安迪·沃霍尔工厂工作的经历。她自称是迷恋沃霍尔的“青少年跟踪者”，最初通过她的父母认识了他，她的父母从沃霍尔早期当插画家时就认识他了。她遇到的沃霍尔与她听说的传奇人物不同——他是一个商人，而不是一个幽灵般的艺术家。

这篇文章详细描述了她在一家高级餐厅与沃霍尔的第一次见面，记录了他的腼腆、他著名的同伴以及他们关于《Interview》杂志的谈话。埃伯斯塔特获得了一次为该杂志撰稿的机会，但发现沃霍尔对她为该出版物提出的选题和人物大多不屑一顾。

埃伯斯塔特反思了沃霍尔的孤独以及她自己作为局外人的感受，尽管她出身优越。她暗示了一种共同的分裂感，以及一种宁愿从远处观察而不愿完全参与社交场景的偏好。她将沃霍尔描绘成一个被焦虑困扰的人，在重复和相同中寻求慰藉。最终，这篇文章探讨了埃伯斯塔特年轻时对沃霍尔的迷恋，并揭示了一种共同的疏离感和无法完全建立联系的感觉，尽管名声和归属感极具诱惑力。

---

## 73. 我把乐谱放进了智能眼镜 [视频]

**原文标题**: I put sheet music into smart glasses [video]

**原文链接**: [https://www.youtube.com/watch?v=j36u2i7PKKE](https://www.youtube.com/watch?v=j36u2i7PKKE)

这个名为“我把乐谱放进了智能眼镜”的YouTube视频很可能展示了一个项目，该项目成功地在智能眼镜上显示乐谱。该视频可能会演示使用眼镜免提阅读乐谱的过程和功能。

然而，所提供的文本片段是通用的YouTube样板，没有提供关于项目本身的任何具体细节。它仅仅是在YouTube视频描述或页脚中常见的标准法律和信息链接。因此，摘要是基于视频标题和对视频内容的合理猜测，因为该文本片段没有提供关于项目的任何实质性信息。

---

## 74. 你一直需要的地图软件：QGIS (2023)

**原文标题**: QGIS is the mapping software you didn't know you needed (2023)

**原文链接**: [https://chollinger.com/blog/2023/01/qgis-is-the-mapping-software-you-didnt-know-you-needed/](https://chollinger.com/blog/2023/01/qgis-is-the-mapping-software-you-didnt-know-you-needed/)

本文介绍了QGIS，一款免费且开源的地理信息系统(GIS)软件，着重强调了其在处理地理空间数据方面的实用性，尤其是在美国南部进行休闲地产分析。文章强调了大量可公开获取的地理空间数据，包括人口普查信息、人口统计数据、来自NASA航天飞机雷达地形测绘任务(SRTM)的高程数据、美国土壤调查局的土壤数据以及县级GIS地图。

作者提供了一个使用QGIS分析地块的实际例子，展示了如何结合各种数据源，例如用于地块边界的KML文件、用于高程的DEM文件、用于底图的TMS API、用于时间背景的历史航空摄影以及用于土壤数据的Shapefile。

QGIS涵盖的关键功能包括：导入不同的数据格式、创建地图投影（推荐EPSG:3857）、对未进行地理标记的图像（如扫描的测量图）进行地理配准、样式化地图图层、从高程数据生成等高线，以及创建用于可视化地形的山体阴影地图。文章强调了理解在线GIS数据局限性的重要性，并建议进行土地测量以确定法律边界。最终，QGIS能够让用户创建详细的地图并分析超出标准地图服务所能提供的财产特征。

---

## 75. 工艺 001：与 Neal Agarwal 谈论工艺、代码和自由

**原文标题**: The Craft 001: A conversation about craft, code, and freedom with Neal Agarwal

**原文链接**: [https://www.workingtheorys.com/p/the-craft-neal-agarwal](https://www.workingtheorys.com/p/the-craft-neal-agarwal)

本文是Anu Atluru与Neal.fun的创建者Neal Agarwal之间的一场对话，探讨了工艺、代码和创作自由。Agarwal讲述了他从童年时期制作100个游戏到创造像《密码游戏》和《无限工艺》等爆款游戏的历程。

要点包括：

* Agarwal从小就开始游戏开发和网页设计，这得益于他“终日沉迷网络”的童年。
* 他决定创建Neal.fun作为其项目的中心枢纽，源于父母担心他过度购买域名。
* 他曾在MSCHF短暂工作过，并在那里享受了非正统且具有创造性挑战的项目。
* 他更喜欢在Neal.fun上独立工作，以追求自己的创作愿景。
* 他在游戏设计中平衡创意想法与技术限制的方法。
* 他目前使用Cursor等AI工具来扩展其项目的范围并克服样板代码。
* Agarwal对《无限工艺》的独特方法，包括为LLM设计提示，而不是编写传统的游戏玩法代码。
* 他认为人工智能可以带来很酷的新游戏类型，例如动态NPC对话，但也承认其潜在危害，例如取代游戏行业中的人类工人。
* 他强调在人工智能生成内容的世界中，手工制作的独特创作的重要性。
* Agarwal渴望创造能够经受时间考验并为玩家提供持久乐趣的游戏。

---

## 76. 古埃及图像中描绘的银河

**原文标题**: Depictions of the Milky Way found in ancient Egyptian imagery

**原文链接**: [https://phys.org/news/2025-04-depictions-milky-ancient-egyptian-imagery.html](https://phys.org/news/2025-04-depictions-milky-ancient-egyptian-imagery.html)

朴茨茅斯大学的奥尔·格劳尔博士在古埃及图像中发现了银河系的潜在视觉描绘，特别是在天空女神努特的形象中。格劳尔分析了近5000年前的古埃及棺材上发现的125幅努特的图像，将天文学与埃及学相结合，探索努特与银河系之间可能存在的联系。

努特的典型形象是一位布满星辰、拱形身躯的女性，保护着地球。然而，在内西陶杰塔赫特的棺材上，努特的身体上有一条独特的、起伏的黑色曲线，星星均匀地分布在曲线的上方和下方。格劳尔认为这条曲线代表银河系，特别是银河系中的一条黑暗尘埃带，即大裂谷。他在国王谷的墓穴中也发现了类似的曲线。

虽然格劳尔早期的研究表明，基于古代文献，努特与银河系之间存在密切联系，但对棺材和墓穴壁画的视觉分析完善了他的观点。他现在认为，银河系是装饰努特身体的几种天体现象之一，而不是女神本人的直接代表。

格劳尔的工作是一个更大项目的一部分，该项目旨在编录银河系的多文化神话，其灵感来自他的女儿们对努特形象的着迷。他的研究结果发表在《天文史与遗产杂志》上。

---

## 77. ePub-utils: 用于从终端检查 ePub 的 Python 库和 CLI 工具

**原文标题**: ePub-utils: A Python library and CLI tool for inspecting ePub from the terminal

**原文链接**: [https://github.com/ernestofgonzalez/epub-utils](https://github.com/ernestofgonzalez/epub-utils)

`epub-utils` 是一个 Python 库和命令行工具，旨在检查和操作 EPUB 文件。它允许用户解析和验证 EPUB 容器和包文件，提取诸如标题、作者和标识符等元数据，并提供一个命令行界面，用于从终端快速检查 EPUB 文件。该 CLI 提供语法高亮的 XML 输出。

主要功能包括：

*   **解析和验证：** 分析 EPUB 文件的结构是否正确。
*   **元数据提取：** 检索重要的信息，如标题、作者和唯一标识符。
*   **CLI 工具：** 提供了一种用户友好的方式，可以直接从命令行访问容器、包和目录信息。
*   **Python 库：** 允许集成到 Python 项目中，用于以编程方式操作 EPUB 文件。

该库可以使用 `pip install epub-utils` 轻松安装。 CLI 用法包括诸如 `epub-utils your-book.epub container` 用于查看容器文件，`epub-utils your-book.epub package` 用于查看包信息，以及 `epub-utils your-book.epub toc` 用于查看目录的命令。 在 Python 中，可以使用 `Document` 类来加载和访问 EPUB 文件信息，提取诸如包文件位置、标题、作者和标识符等详细信息。

---

## 78. “僵尸”火山解剖：调查乌图伦古火山内部动荡的原因

**原文标题**: Anatomy of a 'zombie' volcano: Investigating the cause of unrest inside Uturuncu

**原文链接**: [https://www.sciencedaily.com/releases/2025/04/250428220444.htm](https://www.sciencedaily.com/releases/2025/04/250428220444.htm)

好的，我已经阅读了提供的URL中的文章。以下是摘要：

**摘要：**

该文章讨论了一项针对玻利维亚乌图伦库火山骚动的研究。该火山已经大约27万年没有喷发，但一直在经历地面形变（抬升），因此被称为“僵尸”火山。研究人员旨在了解这种膨胀的原因。

该研究结合了卫星雷达数据、GPS测量和先进的建模技术，揭示了地面形变是由少量岩浆在地球深处（地表下约17公里）积累所驱动的。该岩浆储集层估计体积约为1立方公里，部分熔融且相对粘稠。

主要发现是，岩浆积累与区域构造力没有直接联系。相反，研究表明，膨胀很可能是由部分熔融岩浆储集层的内部动力学驱动的。具体来说，作者提出，糊状岩浆房内细微的密度变化可能导致了抬升。致密的晶体可能会从熔体中沉淀出来，使剩余的熔体密度降低，并导致其上升和膨胀上覆地壳。这为理解为什么一些火山即使没有即将发生的喷发也会表现出骚动提供了新的视角。这项研究对理解全球其他火山的行为具有重要意义。

---

## 79. 逆向工程：隐形作弊应用Cluely

**原文标题**: Reverse-Engineering Cluely, the Invisible Cheating App

**原文链接**: [https://prathit.vercel.app/blog/reverse-engineering-cluely](https://prathit.vercel.app/blog/reverse-engineering-cluely)

本文剖析了 Roy Lee 为编程面试创建的隐形作弊应用 “Cluely” 背后的技术。尽管该应用引发争议，但其底层技术本身颇具趣味性，且在合乎道德的使用情况下具有潜在益处。

Cluely 利用 Electron 创建屏幕上的透明、置顶覆盖层。这通过 Electron 的 `BrowserWindow` 属性（如 `transparent: true` 和 `alwaysOnTop: true`）实现。然后，覆盖层通过剪贴板监控、屏幕截图或选中文本捕获信息，并将其发送到 AI 后端（如 OpenAI）进行处理。高级版本使用原生模块和 OCR（通过 Tesseract.js 等库）直接从屏幕提取文本。

文章承认了潜在的缺点，如 macOS 和 Windows 上的安全限制，以及因 OCR 和持续剪贴板监控导致的 CPU 和 GPU 使用率引起的性能问题。

然而，文章将该技术重新定义为对道德应用有价值，并提出了其在以下方面的潜力：

*   **销售副驾驶：** 提供实时情境和成交话术。
*   **客户支持助手：** 建议准确且相关的回复。
*   **入职伙伴：** 为新员工提供情境化建议。

文章最后开源了代码，并邀请读者联系作者（邮箱：prathit3.14@gmail.com）以合作进行合法且符合道德的项目。

---

## 80. 致命螺旋蝇卷土重来，威胁德州牛群及美国牛肉供应

**原文标题**: Deadly Screwworm Parasite's Comeback Threatens Texas Cattle, US Beef Supply

**原文链接**: [http://www.bloomberg.com/news/features/2025-05-02/deadly-screwworm-parasite-s-comeback-threatens-texas-cattle-us-beef-supply](http://www.bloomberg.com/news/features/2025-05-02/deadly-screwworm-parasite-s-comeback-threatens-texas-cattle-us-beef-supply)

无法访问文章链接。

---

## 81. 苏联旧金星探测器正接近地球重返大气层

**原文标题**: Old Soviet Venus descent craft nearing Earth reentry

**原文链接**: [https://www.leonarddavid.com/old-soviet-venus-descent-craft-nearing-earth-reentry/](https://www.leonarddavid.com/old-soviet-venus-descent-craft-nearing-earth-reentry/)

莱昂纳德·戴维的文章讨论了苏联1972年发射的宇宙482号金星着陆舱模块即将重返大气层的问题。该任务未能进入金星轨道，导致着陆舱滞留在地球轨道上。卫星追踪器正在密切监测其下降过程。

文章强调了重返大气层过程的不确定性。由于着陆器被设计用于承受金星的大气层，因此它有可能在地球大气层中完整地存活下来。然而，浅 trajectory 和该物体的年代久远使预测变得复杂。目前的估计显示，重返大气层的时间大约在2025年5月10日左右，误差幅度为3.1天。

拉尔夫·范德伯格拍摄的新的高分辨率图像显示了一个紧凑的球状物体。与星链卫星的比较表明了其大小。有趣的是，一些图像暗示了一个微弱的、细长的结构可能附着在“球”上，导致人们猜测它可能是一个部分展开的降落伞。范德伯格强调，该物体可能在翻滚，这解释了潜在降落伞的间歇性可见性。他强调，需要进一步分析来证实这一理论，并承诺随着分析的进展提供更新。

---

## 82. 布隆过滤器

**原文标题**: Bloom Filters

**原文链接**: [https://eli.thegreenplace.net/2025/bloom-filters/](https://eli.thegreenplace.net/2025/bloom-filters/)

布隆过滤器是一种空间效率高的概率数据结构，用于测试一个元素是否属于一个集合。它擅长快速拒绝非成员，这使得它在预期大多数查询为否定时非常理想。

布隆过滤器由一个 `m` 位的位数组和 `k` 个哈希函数组成。插入操作包括对一个元素进行 `k` 次哈希，并将数组中对应的位设置为 1。成员测试对元素进行 `k` 次哈希，并检查所有对应的位是否都为 1。如果任何一位是 0，则该元素肯定不在集合中。如果所有位都是 1，则该元素可能在集合中（存在潜在的误报）。

主要的优点是速度和空间效率。缺点是可能存在误报。本文解释了如何根据预期的元素数量 (`n`) 和期望的误报率 (`ε`) 来计算 `m`（位数组的大小）和 `k`（哈希函数的数量）的最佳值。一个 Go 实现演示了核心操作。本文提供了计算这些参数的数学公式，并最大限度地降低错误率。在磁盘读取成本高昂且负查找频繁的情况下，布隆过滤器是有益的，它能显著加快依赖于集合成员测试的系统。

---

## 83. 编程语言能力比数学能力对编程更重要吗？(2020)

**原文标题**: The language brain matters more for programming than the math brain? (2020)

**原文链接**: [https://massivesci.com/articles/programming-math-language-python-women-in-science/](https://massivesci.com/articles/programming-math-language-python-women-in-science/)

明尼苏达大学2020年的一篇文章探讨了一项研究，该研究表明在学习编程（尤其是Python）时，语言技能比数学技能更为重要。一项针对42名参加在线Python课程的参与者的研究表明，语言能力解释了人们学习速度差异的近20%，而数学技能仅解释了2%。此外，数学技能与参与者学习Python的程度没有相关性。

该研究还使用了脑电图数据，发现与第二语言学习相关联的较高水平的β振荡与更快的学习速度和更多的编程知识相关。这些发现挑战了编程作为数学密集型领域的普遍看法。

作者认为，这些结果对编程的认知和教学方式具有影响。计算机科学中对高级数学先决条件的关注可能是不必要的，并且可能会使潜在的学生（尤其是女性）望而却步，她们可能具有很强的语言技能，但对数学缺乏信心。文章建议，强调语言技能并提供替代教育途径（例如训练营）可以提高计算机科学的多样性，并更好地反映许多编程工作所需的实际技能。同行评论支持这一观点，主张进行更多以语言为导向的编程练习，并将学习编程语言与学习外语进行类比。总而言之，一个“语言大脑”可能比一个“数学大脑”对编程的成功更为关键。

---

## 84. Show HN: Pipask – 更安全的pip，不牺牲便捷性

**原文标题**: Show HN: Pipask – safer pip without compromising convenience

**原文链接**: [https://github.com/feynmanix/pipask](https://github.com/feynmanix/pipask)

Pipask 是一款注重安全性的 `pip`（Python 包安装器）的即插即用替代品。其主要目的是通过在安装包*之前*执行安全检查来提高安全性，在不牺牲 `pip` 便利性的前提下，降低潜在风险。

Pipask 优先使用 PyPI 的元数据，以避免不必要的代码执行。当执行不可避免时（为了获取依赖关系元数据，`pip` 需要执行代码），它会请求用户明确同意。获得批准后，实际安装会委托给标准 `pip`。

安全检查包括：
*   仓库流行度（GitHub/GitLab 星星数）
*   包/发布版本存在时间
*   已知漏洞（来自 OSV.dev）
*   下载统计数据
*   元数据验证（许可证、开发状态、撤回的包）。

这些检查是对明确请求的包执行的，而仅对传递依赖项执行漏洞检查。Pipask 从 PyPI、pypistats.org、GitHub/GitLab 和 OSV.dev 收集数据，以生成需要用户批准的格式化报告。

建议通过 `pipx` 安装，但也可以使用标准 `pip`。该工具可以通过 `pipask` 调用，也可以通过别名 `pip` 调用，并提供回退到标准 `pip` 的选项。`--dry-run` 选项允许用户执行检查而不进行实际安装。

---

## 85. Connomore64：使用并行微控制器实现的C64精确周期模拟

**原文标题**: Connomore64: Cycle exact emulation of the C64 using parallel microcontrollers

**原文链接**: [https://github.com/c1570/Connomore64](https://github.com/c1570/Connomore64)

Connomore64：一个利用多个 RP2040/RP2350 微控制器并行运行，旨在实现 Commodore 64 周期精确仿真的项目。这种芯片级重建方案采用大约 8 MHz 的多路复用 8 位总线，并通过 DVI/HDMI 输出视频和音频，实现微秒级精确信号时序，从而兼容原始 C64 硬件，如软盘驱动器和用户端口设备。

该项目的产生源于探索 RP2040 微控制器及其 PIO 功能的愿望。与现有的 RP2040 C64 模拟器不同，Connomore64 致力于通过精确模拟 CPU 操作码和 VIC-II 视频芯片来实现精确性，从而解决基于 PC 的模拟器在实时时序方面的局限性以及基于 FPGA 的模拟器的成本和复杂性问题。

该模拟器的代码建立在“chips”仿真库的基础上，并针对速度进行了大量优化，尤其是在 VIC-II 和精灵渲染方面。该项目受益于扩展的 rp2040js 模拟器，用于开发和调试，包括 RP2350 支持、周期精确时序和 GPIO 信号跟踪。

硬件包括一个 Breadbox v0 原型，旨在安装在 C64 外壳中，提供原始 C64 端口、HDMI 和音频。功能包括用户端口、IEC 和操纵杆端口，并计划支持扩展端口。早期原型涉及堆叠的 RP2040 板。

Connomore64 能够良好运行许多游戏和演示程序，包括快速加载器和用户端口硬件。缺失的功能包括用于完全扩展端口兼容性的完整周期仿真。该项目目前尚未发布，但作者计划将其作为开源发布。

---

## 86. 实现人类水平的竞技机器人乒乓球

**原文标题**: Achieving Human Level Competitive Robot Table Tennis

**原文链接**: [https://sites.google.com/view/competitive-robot-table-tennis/home?pli=1](https://sites.google.com/view/competitive-robot-table-tennis/home?pli=1)

谷歌DeepMind的这篇文章详细介绍了开发一种能够在竞技乒乓球比赛中达到业余人类水平的机器人代理。该机器人采用分层模块化策略架构，包括低级技能控制器（例如，正手抽球）和一个高级控制器，该控制器根据比赛统计数据、技能描述和对手的能力来选择合适的技能。

一项关键贡献是使用了零样本模拟到真实技术，包括基于真实世界数据定义训练任务分布的迭代方法，从而创建一个用于改进的自动课程。该机器人通过混合模拟-真实循环学习：首先在模拟中进行训练，然后在真实世界中与人类对手进行比赛，从而产生新的训练条件以进行进一步的完善。还加入了对未见对手的实时适应能力。

该机器人的性能在29场与不同技能水平的人类进行的比赛中进行了评估。它的总体胜率为45%，对初学者胜率为100%，对中级选手胜率为55%，表明其具有扎实的业余水平。虽然它输掉了所有与高级选手的比赛，但这些选手仍然觉得与它比赛很有趣。该研究还发现了弱点，例如处理下旋球，为未来的训练提供了方向。用户研究表明，参与者喜欢与机器人对战，即使输了也觉得很有趣。

---

## 87. 什么是观风暴？应该在哪里尝试？

**原文标题**: What is storm-watching and where should you try it?

**原文链接**: [https://www.nationalgeographic.com/travel/article/what-is-storm-watching-how-to-do-it](https://www.nationalgeographic.com/travel/article/what-is-storm-watching-how-to-do-it)

**摘要：**

观风暴是一种休闲活动，即从安全的有利位置观察和欣赏强大的天气事件，特别是冬季风暴。《国家地理》的文章探讨了这一日益增长的趋势，强调了它对那些寻求见证大自然原始力量和美丽的人的吸引力。

文章详细描述了观风暴的感官体验，强调了戏剧性的海浪、狂风和大气条件，这些创造了独特而迷人的景象。文章强调了安全的重要性，敦促观看者与风暴保持适当的距离，并注意任何当地的警告或建议。观风暴的热门地点通常包括崎岖的海岸线，在那里海洋的能量最为明显。

文章重点介绍了以提供绝佳观风暴机会而闻名的特定区域。这些区域通常包括太平洋西北地区（俄勒冈州、华盛顿州和不列颠哥伦比亚省）以及英国的沿海地区。文章建议考虑在淡季前往这些目的地，以获得最壮观的风暴，同时也强调需要为恶劣的天气条件做好准备。文章还简要介绍了负责任的观风暴行为，以最大限度地减少对当地环境的干扰。本质上，这篇文章将观风暴描述为一种令人兴奋且具有教育意义的活动，它可以让人们与大自然的力量建立联系，前提是他们优先考虑安全和环境责任。

---

## 88. 奇异鸟的蛋为什么这么大？

**原文标题**: Why Is the Kiwi's Egg So Big?

**原文链接**: [https://www.audubon.org/magazine/why-kiwis-egg-so-big](https://www.audubon.org/magazine/why-kiwis-egg-so-big)

提供的文本并非关于奇异鸟蛋为何如此之大的文章，而是奥杜邦学会关于气候变化的行动呼吁。其主旨是鼓励读者承诺支持气候行动，敦促人们与奥杜邦学会站在一起，呼吁民选官员倾听科学证据，并努力实施气候解决方案。该文本直接链接到一个个人可以签署的承诺书，强调了该组织的“鸟类告诉我们采取气候行动”倡议，强调鸟类作为环境健康指标的作用，以及解决气候变化以保护它们的紧迫性。 该文本是针对公众参与环保倡议的简短而直接的呼吁。

---

## 89. 小心你的UDP服务：Windows部署服务的预认证DoS攻击

**原文标题**: Be Careful of Your UDP Service: Preauth DoS on Windows Deployment Service

**原文链接**: [https://sites.google.com/site/zhiniangpeng/blogs/WDS-DoS](https://sites.google.com/site/zhiniangpeng/blogs/WDS-DoS)

本文详细描述了Windows部署服务(WDS)中的一个预认证拒绝服务(DoS)漏洞。WDS是企业环境中基于网络的操作系统部署的关键组件。该漏洞源于WDS对UDP连接的处理，特别是其在69端口上的TFTP服务。

发送到该服务的每个UDP数据包都会创建一个新的`CTftpSession`对象，该对象在`EndpointSessionMapEntry`中进行管理。该漏洞在于可以创建的会话数量没有限制。攻击者可以通过伪造大量具有随机源IP和端口的UDP数据包来利用此漏洞，迫使服务器不断为新会话分配内存。

本文描述了一个成功的测试，在一台具有8GB内存的机器上，系统在内存使用量达到15GB后，在7分钟内崩溃。作者提供了伪代码来说明攻击的简单性。

时间线详细说明了向微软报告该漏洞、微软的确认、随后微软对预认证DoS漏洞赏金规则的修改，以及微软最终将该漏洞归类为“中等”等级，未达到安全服务修复的标准。作者认为此漏洞的重要性及其对依赖WDS的组织的影响。因此，作者建议避免使用Windows部署服务。

---

## 90. 基于耳朵传感应用的开源人工智能平台

**原文标题**: Open-source AI platform for ear-based sensing applications

**原文链接**: [https://open-earable.teco.edu/](https://open-earable.teco.edu/)

OpenEarable：全球首款全开源耳戴式人工智能传感平台，该平台以真无线耳机形式呈现，内置高精度传感器，专为开发和研究设计，具有模块化和可重构性。

主要特性包括真无线音频、生物传感功能和微型外形。它配备了包括双红外/超声麦克风、骨传导加速度计、光电容积脉搏波描记（PPG）传感器、9轴IMU、光学皮肤温度传感器和耳道压力传感器在内的多种传感器。这些传感器可以检测超过30种现象，从而实现耳道认证、心脏监测、无声语音识别等应用。

该平台采用 Nordic nRF5340 双核 Arm Cortex-M33 处理器和 Analog Devices ADAU1860 DSP，以实现高效数据处理和高保真音频。OpenEarable 拥有模块化架构，通过排针连接器和 microSD 卡槽实现调试和扩展功能。

软件生态系统包括基于 ZephyrOS 的开源固件、基于 Web 的仪表板、基于 Flutter 的移动应用程序和一个用于自定义工具开发的 Flutter 库。示例应用程序包括录音机、姿势追踪器、跳跃高度测试、跳绳计数器和轻度午睡监视器。

OpenEarable 提供开发者入门套件，其中包括耳机和所有必要的配件。硬件设计文件将以开源形式发布。该平台优先考虑开源和免费使用。文章还提供了设备比较和常见问题解答。

---

## 91. 游戏保护人士称Switch 2游戏卡令人沮丧但不可避免

**原文标题**: Game preservationists say Switch2 GameKey Cards are disheartening but inevitable

**原文链接**: [https://www.videogameschronicle.com/news/game-preservationists-say-switch-2-game-key-cards-are-disheartening-but-inevitable/](https://www.videogameschronicle.com/news/game-preservationists-say-switch-2-game-key-cards-are-disheartening-but-inevitable/)

本文探讨了游戏保存人士对任天堂Switch 2新型“游戏密钥卡”的担忧。与包含完整游戏数据的传统卡带不同，这些密钥卡仅作为从在线商店下载游戏的密钥。这引发了人们对这些游戏长期可玩性的担忧，一旦Switch 2的在线服务器最终关闭，游戏可能无法运行。

文章强调，相当数量的第三方Switch 2游戏将使用游戏密钥卡。Nightdive Studios首席执行官Stephen Kick对此表示失望，并希望任天堂能更加重视游戏保存。尽管詹姆斯·纽曼教授认为，即使是卡带也经常需要更新和补丁，随着时间的推移，原始卡带数据的相关性会降低，但国际电子游戏历史中心的Paul Dyson认为这是走向完全数字化游戏未来的必然一步，并指出任天堂与竞争对手相比，采用这一趋势的速度相对较慢。核心问题是，如果下载服务器不再可用，游戏可能会变得无法运行，从而影响游戏保存工作。

---

## 92. 一种新的科学理论：适应性耗散组织定律

**原文标题**: A novel scientific theory: The Law of Adaptive Dissipative Organization

**原文链接**: [https://chatgpt.com/s/dr_6817001b49988191b1f0dbd01e69a1ab](https://chatgpt.com/s/dr_6817001b49988191b1f0dbd01e69a1ab)

提供的文本介绍了“自适应耗散组织定律”的概念，并链接到多个探讨相关思想的资源。这些资源主要围绕生命的熱力学、自组织以及能量耗散作为适应和进化驱动力展开。

重点强调的关键概念包括：

*   **耗散结构（伊利亚·普里戈金）：** 开放系统可以通过耗散能量来维持甚至增加其组织度，从而远离热力学平衡。
*   **最大功率原理（洛特卡）：** 系统进化以最大化其能量流动，选择有效捕获和耗散能量的结构和过程。
*   **耗散与利用：** 自组织源于能量耗散和利用能量来构建和维持结构之间的相互作用。
*   **杰里米·英格兰的研究：** 他的工作重点是，当系统受到外部能量源驱动时，将如何重组自身以更好地吸收和耗散能量。 这对理解生命的起源具有重要意义。
*   **自由能原理：** 该原理认为生物系统通过调整其内部模型以更好地预测其环境，从而最小化其“意外”。
*   **适应的统计物理学：** 从统计物理学的角度理解适应的理论框架。

本质上，这些资源指向一个理论框架，其中生命和复杂系统被视为耗散结构，它们通过有效地捕获、利用和耗散能量而蓬勃发展。适应是最大化能量流动并在波动的环境中维持内部稳定性的这种驱动力的结果。“自适应耗散组织定律”可能旨在形式化这一总体原则。

---

## 93. 展示一下：我用3D物理引擎做的合成器

**原文标题**: Show HN: I built a synthesizer based on 3D physics

**原文链接**: [https://anukari.com](https://anukari.com)

Anukari是一款新颖的合成器和效果器处理器，它利用3D物理模拟进行声音生成和操控。它允许用户在3D环境中连接质量块、弹簧和其他物理组件来构建虚拟乐器和效果器。然后，用户可以使用MIDI键盘或音频输入与这些创造物进行交互。

主要特性包括：

*   **3D物理游乐场：** 使用交互式物理组件创建乐器和效果器。
*   **MIDI和MPE支持：** 兼容标准MIDI键盘和MPE控制器，实现富有表现力的演奏。
*   **强大的调制：** 提供LFO、包络、MIDI控制和DAW自动化，以进行广泛的参数调制。
*   **GPU加速：** 利用GPU处理能力处理高要求的音频任务，释放CPU资源。
*   **插件和独立模式：** 可作为DAW中的VST3、AU或AAX插件使用，或作为独立应用程序使用。
*   **触觉3D界面：** 提供可视化直观的3D编辑器，用于乐器设计和实时性能反馈。
*   **多功能效果：** 能够创造独特的回响、故障和音效。
*   **可定制的视觉效果：** 允许用户使用天空盒和3D模型自定义3D环境。
*   **构建模块：** 质量块、锚点、弹簧、激励器（槌、振荡器、拨片、弓、音频信号）、麦克风
*   **调制器：** 可视化矩阵、LFO、MIDI控制、DAW自动化、触发包络、包络跟随器

Anukari目前处于Beta测试阶段，并提供免费演示。它可在Windows（仅限于CUDA或OpenCL，不包括AMD GPU）和MacOS上运行。

---

## 94. 超人总动员：地底突袭竞速与MOD

**原文标题**: Speedrunning and Modding the Incredibles: Rise of the Underminer

**原文链接**: [https://farlow.dev/2025/05/02/rotu](https://farlow.dev/2025/05/02/rotu)

这篇博文详细介绍了作者通过逆向工程和修改，优化GameCube平台游戏《超人总动员：地底危机》(rotu)速通流程的努力。为了和他的兄弟一起重夺失去的速通纪录，作者使用Ghidra深入研究了游戏代码，并利用了罕见的调试符号。

由于静态分析战斗系统过于复杂，作者决定创建一个mod，实时显示敌人的生命值。他描述了如何使用DevkitPPC搭建C工具链，将C代码编译成PowerPC指令，然后通过金手指代码将其注入到游戏中。这个mod揭示了战斗机制的关键信息，特别是超能先生的拳头的有效性。

这篇文章还探讨了网上找到的不完整和不准确的作弊代码的谜团。作者发现许多无法使用的代码实际上是被标志锁定的开发者作弊码，并展示了他们如何找到以前未知的开发者作弊码。他们甚至提供了一个金手指代码来启用开发者模式，并展示了诸如L+R+方向键飞行之类的调试功能。

最后，作者简要提到了在练习中遇到的出界漏洞。虽然优化速通的主要目标尚未实现，但作者希望分享他们的研究成果能够帮助到小型的rotu速通社区。

---

## 95. CMU TheAgentCompany：基准测试LLM Agent在有实际影响的真实世界任务中的表现

**原文标题**: CMU TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

**原文链接**: [https://arxiv.org/abs/2412.14161](https://arxiv.org/abs/2412.14161)

这篇题为“TheAgentCompany：LLM智能体在重要真实世界任务上的基准测试”的arXiv论文，介绍了一个新的基准，用于评估人工智能智能体，特别是那些由大型语言模型（LLM）驱动的智能体，在真实世界专业任务上的表现。其核心思想是评估这些智能体在执行模仿软件公司数字员工的任务时的表现，这些任务涉及网页浏览、代码编写、程序执行以及员工间的交流。

作者创建了一个自包含的环境，模拟了一个小型软件公司，包括内部网站和数据，并在该环境中定义了各种与工作相关的任务。然后，他们测试了由闭源API和开源权重LM驱动的基线智能体。

结果表明，表现最佳的智能体能够自主完成24%的任务。这表明，虽然LLM智能体能够独立处理更简单、更直接的任务，但它们仍然难以处理需要更高推理和规划能力的更复杂、长期的任务。该论文强调了LLM智能体在自动化专业任务方面的当前能力和局限性，为行业采用提供了宝贵的见解，并有助于理解人工智能对劳动力市场的潜在影响。

---

## 96. 出人意料的简单方法制造出低成本可调液体透镜

**原文标题**: Surprisingly simple method makes a low-cost, tuneable liquid lens

**原文链接**: [https://cosmosmagazine.com/science/physics/low-cost-tuneable-liquid-lens/](https://cosmosmagazine.com/science/physics/low-cost-tuneable-liquid-lens/)

菲律宾科学家开发低成本可调液体透镜

---

## 97. 最新的AI扩展图——以及为何它几乎毫无意义

**原文标题**: The latest AI scaling graph – and why it hardly makes sense

**原文链接**: [https://garymarcus.substack.com/p/the-latest-ai-scaling-graph-and-why](https://garymarcus.substack.com/p/the-latest-ai-scaling-graph-and-why)

无法访问文章链接。

---

## 98. Rust助手: 使用LLM修复Rust代码中的编译错误

**原文标题**: RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code

**原文链接**: [https://www.microsoft.com/en-us/research/publication/rustassistant-using-llms-to-fix-compilation-errors-in-rust-code/](https://www.microsoft.com/en-us/research/publication/rustassistant-using-llms-to-fix-compilation-errors-in-rust-code/)

本文介绍了RustAssistant，这是微软研究院开发的一款工具，它利用大型语言模型(LLMs)来自动修复Rust代码中的编译错误。 Rust的安全性保证和所有权等特性使其成为底层编程的热门选择，但其复杂性给开发人员带来了陡峭的学习曲线。

RustAssistant通过结合精心设计的提示技术以及LLM和Rust编译器之间的迭代交互来解决这一挑战。 该工具首先构建代码并解析错误，提取相关的代码片段和错误详细信息。 然后，将此本地化信息打包到LLM的提示中，该提示生成代表建议修复的代码差异。 RustAssistant应用此修复，重新编译代码，并与LLM迭代，直到代码编译没有错误。

该工具在GitHub上流行的开源Rust存储库中的真实编译错误上实现了约74%的峰值准确率。 本文重点介绍了该工具处理复杂的多步骤修复的能力。 该研究贡献了一个Rust编译错误数据集，以促进该领域的进一步研究。 ICSE论文提供了有关提示设计以及将RustAssistant扩展到大型代码库的技术的详细信息。

---

## 99. 击败模拟城市的极权主义佛教徒 (2010)

**原文标题**: The Totalitarian Buddhist Who Beat SIM City (2010)

**原文链接**: [https://www.vice.com/en/article/the-totalitarian-buddhist-who-beat-sim-city/](https://www.vice.com/en/article/the-totalitarian-buddhist-who-beat-sim-city/)

这篇Vice文章介绍了文森特·奥卡斯拉，一位来自菲律宾的22岁建筑系学生，以及他的作品：反乌托邦的模拟城市3000大都会“马格纳桑提”。奥卡斯拉花费了一年多的时间规划和建造这个“极权主义地狱”，通过将六百万市民塞进一个受到严格控制的环境中，将游戏推向了极限。

马格纳桑提的特点是人口密度极高、污染严重、失业率高企，缺乏学校和医院等基本服务，以及一个超高效的警察国家，镇压任何形式的反抗。模拟市民过着短暂而刻板的生活，被困在一个永无止境的工作和消费循环中。奥卡斯拉根据佛教的生命之轮（Bhavacakra）设计了这座城市，以代表永无止境的奴役循环。

他认为模拟城市不仅仅是一款游戏，更是一种艺术表达的工具，用它来呈现社会压迫的本质以及独裁者和社会工程师的野心。这篇文章强调了马格纳桑提与现实世界问题的相似之处，例如经济奴役、环境忽视以及将利润置于社会福祉之上的后果。

尽管他的作品性质阴暗，但奥卡斯拉被描绘成一个普通人，一个迷恋神圣几何学和时间循环概念的“自由思想家”。他强调自己没有任何精神健康问题。在通过模拟城市探索了对社会的深刻批判之后，他不再玩其他游戏，觉得它们毫无意义。

---

## 100. Webflow 讓 GSAP 完全免費 – 加上更多更新

**原文标题**: Webflow makes GSAP 100% free – plus more updates

**原文链接**: [https://webflow.com/blog/gsap-becomes-free](https://webflow.com/blog/gsap-becomes-free)

Webflow将领先的JavaScript动画库GSAP (GreenSock Animation Platform) 对所有用户完全免费开放，包括之前付费的“俱乐部”插件和商业使用许可。 此举是Webflow在2024年收购GSAP之后采取的，旨在为开发者和设计师提供高级动画功能。

伴随这一重大声明，Webflow和GSAP发布了多项更新和改进，包括：

*   **GSAP SplitText插件的重大升级：** 经过重写和改进的SplitText插件，文件大小减少了50%，内置可访问性，易于遮罩，新增了deepSlice功能和响应式功能。
*   **在Webflow中更轻松地集成GSAP插件：** 所有GSAP插件现在都可以直接在Webflow中访问和托管，从而简化了在Webflow项目中使用它们的过程。
*   **在Webflow中预览自定义代码：** 用户现在可以在发布之前预览带有自定义HTML、CSS或JavaScript（包括GSAP动画）的Webflow网站。

Webflow计划进一步将GSAP功能集成到其原生的Webflow Interactions中，从而允许用户以可视化的方式构建GSAP驱动的动画。 他们还计划在GSAP上重新构建Webflow Interactions，并将其与网站体验平台集成。

为了庆祝这些公告，Webflow将于5月9日在YouTube上举办一场活动，并与Codepen合作举办一场社区挑战赛。

---

