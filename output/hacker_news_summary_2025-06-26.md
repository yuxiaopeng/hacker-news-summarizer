# Hacker News 热门文章摘要 (2025-06-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 谷歌DeepMind发布AlphaGenome

**原文标题**: Google DeepMind Releases AlphaGenome

**原文链接**: [https://deepmind.google/discover/blog/alphagenome-ai-for-better-understanding-the-genome/](https://deepmind.google/discover/blog/alphagenome-ai-for-better-understanding-the-genome/)

谷歌DeepMind发布AlphaGenome，一种旨在全面预测DNA序列变异对基因调控影响的新型AI工具。该模型可分析多达100万个DNA碱基对，并预测数千种分子特性，包括基因起始和终止点、剪接、RNA产生和蛋白质结合。它利用来自ENCODE、GTEx和其他公共联盟的数据，覆盖人类和小鼠细胞中的基因调控。

AlphaGenome的关键特性包括其能够以高分辨率处理长DNA序列、提供全面的多模态预测、高效评估遗传变异的影响以及直接从序列中建模剪接连接。它在各种基因组预测基准中实现了最先进的性能。

该模型的通用性使科学家能够同时探索变异对多种模式的影响，从而加速假设生成。专家认为，AlphaGenome可以通过查明疾病原因、指导合成DNA设计以及绘制基因组的关键功能元件，显著帮助疾病理解、合成生物学和基础研究。

尽管AlphaGenome标志着一项重大进展，但它也存在局限性，包括捕获非常遥远的调控元件的影响以及完全捕获细胞和组织特异性模式的能力。它通过API提供给非商业研究使用，并计划在未来发布模型。DeepMind鼓励研究人员利用API，参与社区论坛并提供反馈，以提高模型的功能。该公司强调，AlphaGenome的预测仅供研究使用，未经临床验证。

---

## 2. Aerospike喷管综述：航空航天应用的当前趋势

**原文标题**: A Review of Aerospike Nozzles: Current Trends in Aerospace Applications

**原文链接**: [https://www.mdpi.com/2226-4310/12/6/519](https://www.mdpi.com/2226-4310/12/6/519)

无法访问文章链接。

---

## 3. 展示一下：我做了一个AI数据集生成器

**原文标题**: Show HN: I built an AI dataset generator

**原文链接**: [https://github.com/metabase/dataset-generator](https://github.com/metabase/dataset-generator)

此“Show HN”帖子介绍了一个AI数据集生成器，该工具旨在为演示、学习和仪表板创建逼真的数据集。它利用OpenAI API（特别是GPT-4o）根据用户定义的提示来定义数据模式和业务规则，然后使用Faker进行本地数据生成。主要功能包括会话式提示构建器、实时数据预览、CSV/SQL导出选项和一键式Metabase集成，用于数据探索。

该生成器使用Next.js、Tailwind CSS和TypeScript构建，需要Docker和一个OpenAI API密钥才能运行。用户可以克隆存储库，配置他们的API密钥，并启动Next.js应用程序以开始生成数据集。工作流程包括定义数据集的特征，预览样本，然后将其导出为CSV或SQL。一个关键优势是成本效益：OpenAI API调用仅在数据预览期间进行，产生少量费用（约0.05美元），而随后的下载是免费的。

该工具支持生成“一张大表”（OBT）或“星型模式”格式的数据集。Metabase集成通过允许用户在Docker化的Metabase实例中探索他们生成的数据，简化了数据分析。该帖子还概述了项目结构，并提供了通过修改`lib/spec-prompts.ts`来使用新的业务类型或模式逻辑扩展生成器的指南。

---

## 4. Gemma 3n 发布

**原文标题**: Introducing Gemma 3n

**原文链接**: [https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)

文章宣布Gemma 3n全面发布：谷歌新一代面向设备端性能的开源AI模型。Gemma 3n建立在最初Gemma版本成功的基础之上，是一种移动优先的架构，提供针对边缘设备优化的多模态能力（图像、音频、视频和文本）。

主要创新包括：

*   **MatFormer架构：** 一种嵌套Transformer架构（俄罗斯套娃Transformer），允许弹性推理，有效地在一个更大的模型中包含更小的、功能完整的版本。这使得用户可以在不同性能级别之间选择预提取的模型（E2B和E4B），或者使用“Mix-n-Match”技术创建自定义尺寸。
*   **逐层嵌入（PLE）：** 通过允许大部分参数在CPU上高效加载和计算，提高了内存效率，从而减少了设备加速器上的内存占用。
*   **KV缓存共享：** 加速长上下文处理，显著提升流媒体应用程序的首次token响应时间。
*   **增强的音频理解：** 集成了基于通用语音模型（USM）的音频编码器，支持自动语音识别（ASR）和自动语音翻译（AST）。
*   **MobileNet-V5：** 一种新型、高效的视觉编码器，在边缘设备上为具有高吞吐量的多模态任务提供最先进的性能。

Gemma 3n旨在具有可访问性，并得到各种开源工具和平台的支持。谷歌还发起了Gemma 3n影响挑战赛，鼓励开发者利用该模型的设备端、离线和多模态能力构建具有实际影响的产品。文章最后提供了有关如何开始使用Gemma 3n的信息，包括下载模型、文档和集成指南的链接。

---

## 5. 我开发了一个多动症应用程序，包含互动应对工具、噪音混合器和自我测试。

**原文标题**: I built an ADHD app with interactive coping tools, noise mixer and self-test

**原文链接**: [https://www.adhdhelp.app/en](https://www.adhdhelp.app/en)

该文章推广一款名为“ADHD助手”的ADHD应用程序，旨在帮助个人应对常见的ADHD症状，如注意力不集中、焦虑、易怒、不知所措、多动和健忘。该应用程序强调，这些不是懒惰或品行不端的表现，而是大脑的运作方式不同。

ADHD助手提供以下功能来支持用户：

*   **互动应对工具：** 基于CBT、DBT和正念的迷你自助技巧，解释简单易懂。
*   **音频肯定语：** 针对特定ADHD状态量身定制的简短、支持性录音。
*   **环境声音混合器：** 大气音轨（雨声、壁炉声等），通过屏蔽分散注意力的噪音来帮助用户集中注意力。
*   **自我评估：** 一个简短的测试，用于评估症状并获得个性化建议。

高级版本解锁所有25个音频肯定语，提供对新内容的早期访问权限，提供更广泛的技巧集、情绪日记、环境混合器、个性化推荐和优先支持。该应用程序还包含一个博客，其中包含讨论ADHD各个方面的文章，包括个人经历、后期诊断的挑战以及超聚焦的潜力。该应用程序鼓励用户免费试用7天高级版本，并提供“任务”来帮助养成积极的习惯。

---

## 6. FLUX.1 Kontext [开发] – 用于图像编辑的开放权重

**原文标题**: FLUX.1 Kontext [Dev] – Open Weights for Image Editing

**原文链接**: [https://bfl.ai/announcements/flux-1-kontext-dev](https://bfl.ai/announcements/flux-1-kontext-dev)

黑森林实验室（BFL）发布 FLUX.1 Kontext [dev]，一款性能媲美专有工具且可在消费级硬件上运行的开放权重图像编辑模型。这个拥有 120 亿参数的模型，采用 FLUX.1 非商业许可，可用于研究和非商业用途。

FLUX.1 Kontext [dev] 擅长迭代编辑、角色保留以及局部和全局编辑。在 KontextBench 基准测试和独立评估中，其性能优于现有的开放和封闭模型。该模型支持 ComfyUI、HuggingFace Diffusers 和 TensorRT 等流行的推理框架。即用型 API 端点和代码可通过 FAL 和 Replicate 等合作伙伴获得。

BFL 与 NVIDIA 合作，为 Blackwell 架构创建了优化的 TensorRT 权重，从而提高了推理速度并减少了内存使用。BF16、FP8 和 FP4 TensorRT 变体也可在 Hugging Face 上找到。

对于商业用途，BFL 正在推出一个自助许可门户，其中包含 FLUX.1 Kontext [dev]、FLUX.1 Tools [dev] 和 FLUX.1 [dev] 的透明条款。

FLUX.1 [dev] 非商业许可已更新，以明确非商业目的，要求内容过滤器/手动审查，强制执行内容溯源合规性，并明确使用限制。

提供包括模型权重、代码、API 文档和许可信息在内的资源。BFL 也在积极招聘。

---

## 7. 一种新型金字塔形状的物体总是同一面朝上落地。

**原文标题**: A new pyramid-like shape always lands the same side up

**原文链接**: [https://www.quantamagazine.org/a-new-pyramid-like-shape-always-lands-the-same-side-up-20250625/](https://www.quantamagazine.org/a-new-pyramid-like-shape-always-lands-the-same-side-up-20250625/)

Quanta杂志文章探讨了首个单稳态四面体物理模型的创建——这是一种金字塔状的形状，无论其起始位置如何，总是落在同一面上。

几十年来，数学家们一直在思考是否存在具有均匀重量分布的这种形状。虽然最初被证明是不可能的，但在允许不均匀重量分布的情况下，这个问题仍然引人入胜。以平衡问题研究闻名的加博尔·多莫科斯（尤其以他的单单稳态形状“Gömböc”闻名）接受了这个挑战。

2023年，多莫科斯及其团队从理论上证明了单稳态四面体的可能性。然后，他们开始了构建它的过程，这是一项更为复杂的任务。他们使用计算机算法来寻找四面体的顶点，并确定三个连续的边需要形成钝角，并且重心必须位于四个“加载区”之一内。

最终的模型由轻质碳纤维和高密度碳化钨制成，重120克，尺寸为50厘米。实现精确的重量分布需要在工程上达到极高的精度。经过数月的努力并克服了未预料到的挑战（例如一滴意外的胶水），他们成功地创造了一个始终落在其指定面上的四面体。

这项成就突出了实验在数学中的重要性，并且可能具有实际应用，例如在自扶正航天器设计中。该团队希望他们的工作能激发对多面体及其性质的进一步探索。

---

## 8. 访问Supermicro X11SSH上的BMC UART

**原文标题**: Access BMC UART on Supermicro X11SSH

**原文链接**: [https://github.com/zarhus/zarhusbmc/discussions/3](https://github.com/zarhus/zarhusbmc/discussions/3)

这是一个论坛帖子，记录了 3mkusiak 成功访问 Supermicro X11SSH 主板上 BMC UART 的过程。由于 X11SSH 缺少调试头或探针点以便于 UART 访问，因此需要更深入的“破解”方法。

3mkusiak 以 Keno Fisher 的博客文章作为起点，并参考了 X11SSH Gerber 文件（由 Tim Ansell 提供）和 AST2400 数据手册。最初，3mkusiak 追踪了 Keno 使用的 TX 引脚，但需要确定 RX 引脚。在利用 Gerber 文件追踪 PCB 层后，3mkusiak 找到适合焊接的未填充焊盘。

电线焊接到这些焊盘上，然后重新组装主板。实验证明成功，允许访问原始 BMC 固件的 UART。

用户 miczyg1 最初质疑这种方法的必要性，建议使用 COM1 接口，但 3mkusiak 澄清说原始固件缺少 UART 重定向，因此需要硬连线解决方案来访问原始 BMC 固件。

该项目在一天内完成，维护者 pietrushnic 祝贺 3mkusiak 迅速成功，并宣布将在社交媒体上分享这一成果。帖子以 3mkusiak 认为讨论结束而告终。

---

## 9. 波多黎各太阳能微电网战胜停电

**原文标题**: Puerto Rico's Solar Microgrids Beat Blackout

**原文链接**: [https://spectrum.ieee.org/puerto-rico-solar-microgrids](https://spectrum.ieee.org/puerto-rico-solar-microgrids)

本文探讨了波多黎各的太阳能微电网，特别是在Adjuntas镇，如何在岛上大范围停电期间成功供电。这些微电网与橡树岭国家实验室合作开发，为波多黎各持续的电力中断提供了一个具有韧性的解决方案。尽管这些微电网提供了本地化的电力，但本文强调了一项对比鲜明的联邦决定，即将最初用于太阳能项目的3.65亿美元转移到更广泛的电网改进上。这种转变表明，对于解决波多黎各能源危机的最佳方法存在争议，权衡了分散式、本地化的太阳能解决方案与大规模电网改造的优缺点。本文强调了在波多黎各持续的能源挑战中，微电网作为一种可行且可靠的电力来源的重要性。该文章由科学和环境记者朱莉娅·蒂尔顿撰写。

---

## 10. Muvera: 让多向量检索速度媲美单向量搜索

**原文标题**: Muvera: Making multi-vector retrieval as fast as single-vector search

**原文链接**: [https://research.google/blog/muvera-making-multi-vector-retrieval-as-fast-as-single-vector-search/](https://research.google/blog/muvera-making-multi-vector-retrieval-as-fast-as-single-vector-search/)

本文介绍了一种名为MUVERA的新型算法，该算法能显著加速多向量检索，使其速度与单向量搜索一样快。诸如ColBERT之类的多向量模型通过用多个嵌入表示数据点，从而提高了信息检索（IR）的准确性，但其计算成本很高。MUVERA通过将多向量检索转换为单向量最大内积搜索（MIPS）问题来弥合了这种效率差距。

MUVERA通过固定维度编码（FDE）来实现这一点。它将复杂的多向量集合转换为单个、更易于处理的向量（FDE），同时保留相似性信息。它对嵌入空间进行分区，并将向量映射到FDE中，从而可以使用优化的MIPS算法进行快速相似性比较。初始检索之后，使用原始的Chamfer相似度进行重新排序，以提高准确性。至关重要的是，FDE转换是数据无关的，并为Chamfer相似度的近似提供了理论保证。

在BEIR基准上的实验结果表明，MUVERA优于现有方法（如PLAID）。它在检索显著更少的候选文档的同时实现了更高的召回率，并且与PLAID相比，延迟降低了90%。FDE还可以有效地压缩，从而进一步减少内存占用。MUVERA为搜索引擎和推荐系统等实际应用提供了一个实用的解决方案，有望实现更快、更高效的多向量检索。MUVERA的开源实现在GitHub上提供。

---

## 11. C语言中malloc(0)被允许返回NULL的一些讨论

**原文标题**: Some bits on malloc(0) in C being allowed to return NULL

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/programming/CZeroSizeMallocSomeNotes](https://utcc.utoronto.ca/~cks/space/blog/programming/CZeroSizeMallocSomeNotes)

克里斯·西本曼的页面解释了为什么访问者在访问他的博客“Wandering Thoughts”或 CSpace 时可能会遇到“旧浏览器”错误。这是一种有意的反爬虫措施，旨在应对大量网络爬虫的涌入，特别是那些为 LLM 训练抓取数据的爬虫，它们通常使用过时的浏览器用户代理，尤其是旧版本的 Chrome。

该页面承认合法用户可能被错误地标记，并为他们提供了联系作者（通过他的大学电子邮件）的说明，以提供有关其浏览器和用户代理字符串的详细信息。

特别警告访问 archive.today、archive.ph 和 archive.is 的用户。这些存档服务被标记为有问题，因为它们的爬取行为与恶意行为者无法区分，使用旧的 Chrome 用户代理、分布式 IP 地址，有时还会伪造模仿 Googlebot 的反向 DNS 条目。作者建议使用 archive.org 代替，因为它是一种行为更好且可爬取的存档服务。

---

## 12. -两千行代码

**原文标题**: -2000 Lines of code

**原文链接**: [https://www.folklore.org/Negative_2000_Lines_Of_Code.html](https://www.folklore.org/Negative_2000_Lines_Of_Code.html)

这篇来自Folklore.org的文章，题为《-2000行代码》，讲述了比尔·阿特金森的故事。阿特金森是1982年初苹果公司Lisa软件团队的关键执行者。Lisa的管理者试图通过每周编写的代码行数来追踪每位工程师的生产力。负责Quickdraw和用户界面的阿特金森强烈反对这一指标。他认为编写高效简洁的代码比简单地生成大量代码更重要。

阿特金森最近优化了Quickdraw的区域计算，用更高效的算法重写了引擎。这次重写带来了六倍的性能提升，更重要的是，代码减少了大约2000行。当被要求提交代码行数时，阿特金森大胆地输入了“-2000”。

这个故事突显了仅用代码行数衡量软件生产力的错误逻辑。它表明这种指标会激励不良的编码习惯，并阻碍优化。虽然管理者的反应没有明确说明，但故事的结尾暗示他们最终停止要求阿特金森填写表格，这表明他们认识到这种指标的无效性。评论进一步强化了这样一种观点，即在软件开发中，依赖代码行数作为绩效衡量标准是一种错误的途径。

---

## 13. 构建AI智能体的经验与教训

**原文标题**: Learnings from building AI agents

**原文链接**: [https://www.cubic.dev/blog/learnings-from-building-ai-agents](https://www.cubic.dev/blog/learnings-from-building-ai-agents)

Paul Sangle-Ferriere (cubic 联合创始人) 分享了构建 AI 代码审查代理的经验教训。最初，该代理过于嘈杂，充斥着低价值评论和误报，淹没了 pull 请求。最初的架构使用单个大型 prompt 来分析代码更改，导致诸如样式错误被标记为严重错误、用户失去信任以及推理过程不透明等问题。

为了改进，他们实施了三个主要改变。首先，他们要求 AI 为其发现提供明确的推理日志，以便更好地调试和结构化思考。其次，他们简化了代理的工具集，专注于基本组件，例如简化的 LSP 和基本终端。这减少了干扰并提高了精度。第三，他们从通用规则过渡到专门的微型代理，每个代理都专注于特定的任务，例如安全性、重复性或编辑检查。

这些改变带来了 51% 的误报率降低、每个 pull 请求的评论中位数减少 50% 以及更顺畅的审查流程。关键的经验教训是：明确的推理提高了清晰度和调试能力，简化工具集增强了精度，而使用微型代理进行专门化则减少了认知超载。这些经验教训广泛适用于设计有效的 AI 系统。

---

## 14. 押注灾难的生意

**原文标题**: The Business of Betting on Catastrophe

**原文链接**: [https://thereader.mitpress.mit.edu/the-business-of-betting-on-catastrophe/](https://thereader.mitpress.mit.edu/the-business-of-betting-on-catastrophe/)

苏珊·埃里克森的文章《押注灾难的生意》探讨了保险连接证券（ILS）的世界，重点关注世界银行的疫情债券，以此为例说明如何将灾难转化为资本。这些债券旨在通过让私人投资者投机疫情风险来筹集应对疫情的资金。如果未发生疫情，投资者将获得投资利息，但如果达到预定义的疫情阈值，他们将损失本金。

埃里克森的研究受到债券创建的推动，使她了解了再保险行业及其在 20 世纪 90 年代采用 ILS 来分散投资组合以应对重大天气事件的情况。 ILS 允许对冲基金和养老金对证券化的风险进行赌博。 ILS 的一个关键特征是参数的使用，参数会根据预设条件（如飓风中的风速）触发赔付，而不是实际的损害评估。

该文章强调了投资者的动机：承担灾难风险带来的潜在巨额回报。就世界银行的疫情债券而言，如果 COVID-19 没有触发赔付，投资者本可以在三年内获得 40% 的回报。

埃里克森强调，ILS 投资者不是为特定实体或资产提供保险，而是投机风险本身，根据预设参数定义的灾难的发生和强度来获利（或亏损）。尽管 ILS 只是一个小众市场，但它代表着一个蓬勃发展的 1950 亿美元的产业，通过疫情和其他灾难风险的可投资性，为投资者提供了独特的多元化机会。

---

## 15. 雪 - 经典Macintosh模拟器

**原文标题**: Snow - Classic Macintosh emulator

**原文链接**: [https://snowemu.com/](https://snowemu.com/)

Snow：一款用 Rust 编写的开源、硬件级经典 Macintosh 电脑（使用 Motorola 680x0 处理器）模拟器。与一些模拟器不同，Snow 的目标是精确的硬件模拟，而不是依赖 ROM 补丁或系统调用拦截。它目前支持模拟 Macintosh 128K、512K、Plus、SE、Classic 和 II 型号。

该模拟器具有图形用户界面并提供调试工具。虽然有一个有限的在线演示版本，但完整的软件以“前沿”构建版本提供，这些版本会随着项目的进展自动生成。这些构建版本适用于 Windows 10+、MacOS 11.7 (Big Sur)+（通用架构）和 Linux (x86 64 位)。

如需报告错误，用户请前往 GitHub issues。如需支持或一般讨论，文章建议加入 MartyPC and Friends Discord 服务器上的 #snow 频道。更多设置信息和文档可以在网上找到。

---

## 16. OpenAI按分钟收费，加快你的音频速度。

**原文标题**: OpenAI charges by the minute, so speed up your audio

**原文链接**: [https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/](https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/)

通过加速音频来降低 OpenAI 音频转录成本和时间的技巧

---

## 17. 什么使可理解性输入变得可理解？

**原文标题**: What makes comprehensible input comprehensible?

**原文链接**: [https://cij-analysis.streamlit.app](https://cij-analysis.streamlit.app)

由于该文章只显示“您需要启用JavaScript才能运行此应用”的消息，我无法提供其内容摘要。 要理解是什么使可理解性输入变得可理解，我需要访问文章的实际文本。

---

## 18. 氛围花园

**原文标题**: Ambient Garden

**原文链接**: [https://ambient.garden](https://ambient.garden)

环境花园（ambient.garden）：一个算法音频景观网站。用户可以通过拖动来环顾四周，点击来前往不同区域，从而浏览这个景观。该网站提供“自动驾驶”选项，允许自动探索。同时还提供音频暂停和播放速度调节的控制功能。

描述强调环境是算法生成的，这意味着音频是通过程序生成，而不是固定的录音。这很可能会创造一种动态且不断变化的声音体验。该网站强调其音频重点，并提供最少的视觉信息，表明主要的体验是听觉的。

加载画面表明该网站依赖于动态加载或生成内容，链接到“关于/音乐”提供了关于项目本身以及音乐创作和生成方面的更多信息。

---

## 19. 以280字建模世界

**原文标题**: Modeling the World in 280 Characters

**原文链接**: [https://tympanus.net/codrops/2025/06/23/modeling-the-world-in-280-characters/](https://tympanus.net/codrops/2025/06/23/modeling-the-world-in-280-characters/)

Xor，一位图形程序员，分享了他对创作紧凑型着色器程序（通常被称为“推特着色器”，适合于280个字符内）的热情。他使用名为Twigl.app的工具来创建这些演示，并针对代码大小、性能和艺术吸引力进行优化。

他的动力源于好奇心、学习、代码高尔夫的挑战以及社区参与。着色器在GPU上运行，并行处理操作，使其非常适合生成实时视觉效果。推特着色器是片段着色器，作用于单个像素以输出颜色和不透明度。核心输入包括片段坐标 (FC)、分辨率 (r) 和时间 (t)。

Xor 以紧凑的形式进行原型设计，优先考虑代码大小缩减技术，如缩写名称、最小化初始化、避免 `if` 语句和优化循环结构。他还利用函数替换来进一步压缩代码。

他回答了常见问题，强调了湍流效应的实用性以及学习着色器背后数学知识时耐心和分解复杂主题的重要性。Xor 鼓励初学者探索像GameMaker或Godot这样的游戏引擎，或者像ShaderToy或compute.toys这样的平台，来开始学习着色器编程。他感谢 xygthop3、Inigo Quilez 和 Fabrice Neyret 等关键人物对他的学习之旅所做出的贡献。

---

## 20. 当你对Linux驱动一无所知时，编写一个基本的Linux设备驱动程序

**原文标题**: Writing a basic Linux device driver when you know nothing about Linux drivers

**原文链接**: [https://crescentro.se/posts/writing-drivers/](https://crescentro.se/posts/writing-drivers/)

本文记录了作者在没有Linux驱动开发经验的情况下，编写Nanoleaf Pegboard Desk Dock（一款带RGB LED的USB集线器）Linux驱动的历程。

作者首先使用`lsusb`识别设备，发现一个通用的HID驱动已经识别了它。面对创建内核驱动或通过`libusb`创建用户空间驱动的选择，作者因后者复杂度较低而选择了后者。

该过程包括设置`udev`规则以授予用户访问设备的权限。然后，作者使用`rusb` crate创建一个基本的Rust二进制文件来与设备交互。

遇到的一个常见错误是声明接口时出现“Busy”，通过分离内核驱动程序来解决。然后，作者使用适当端点上的`write_interrupt`发送命令，将洞洞板设置为纯红色。

本文强调了理解USB概念（如配置、接口和端点）的重要性。它还指出需要处理来自设备的中断响应，以避免固件崩溃。作者强调了写入设备的简易性，称其就像打开管道并写入一样简单。

---

## 21. 更好的身份验证服务，由一位自学成才的埃塞俄比亚开发者创建，获 Peak XV 和 YC 投资 500 万美元

**原文标题**: Better Auth, by a self-taught Ethiopian dev, raises $5M from Peak XV, YC

**原文链接**: [https://techcrunch.com/2025/06/25/this-self-taught-ethiopian-dev-built-an-authentication-tool-and-got-into-yc/](https://techcrunch.com/2025/06/25/this-self-taught-ethiopian-dev-built-an-authentication-tool-and-got-into-yc/)

来自埃塞俄比亚的自学成才程序员Bereket Engida创建了Better Auth，这是一个开源身份验证框架，可简化开发人员的用户管理。这家初创公司最近获得了500万美元的种子轮融资，投资者包括Peak XV、Y Combinator、P1 Ventures和Chapter One等知名机构。

Engida在埃塞俄比亚开发了整个产品，原因是现有的Auth0和Firebase等身份验证解决方案存在局限性和高成本。他想要一个提供更多定制、用户数据控制和可扩展性的系统。

Better Auth允许开发人员直接在其数据库上实施身份验证，将用户数据保留在本地，这对关注第三方数据处理的公司具有很大的吸引力。其基于TypeScript的框架支持常见的权限用例，并通过插件进行扩展，从而以最少的代码实现高级功能。

自2024年9月在GitHub上发布以来，Better Auth已获得显著关注，每周下载量超过15万次，GitHub Stars达1.5万，并拥有蓬勃发展的社区。它在需要自定义身份验证流程的人工智能初创公司中尤其受欢迎。

目前Better Auth可以免费使用，未来计划专注于改进核心功能并推出付费的企业级基础设施，该基础设施与其开源基础相结合，为开发人员提供灵活的托管选项。Engida还计划组建一支小团队来支持不断增长的代码库和企业用户。

Better Auth的成功被视为一位埃塞俄比亚创始人构建全球产品的重大成就，并激励了该地区其他有抱负的开发人员。

---

## 22. 使用 LangChain 和 Llamafile 的结构化输出

**原文标题**: Structured Output with LangChain and Llamafile

**原文链接**: [https://blog.brakmic.com/structured-output-with-langchain-and-llamafile/](https://blog.brakmic.com/structured-output-with-langchain-and-llamafile/)

使用Llamafile和LangChain生成结构化JSON输出

---

## 23. ebtree/cebtree/rbtree 的实际性能比较

**原文标题**: Real-world performance comparison of ebtree/cebtree/rbtree

**原文链接**: [http://wtarreau.blogspot.com/2025/06/real-world-performance-comparison-of.html](http://wtarreau.blogspot.com/2025/06/real-world-performance-comparison-of.html)

本文利用"treebench"工具，对三种树实现的真实性能进行了比较，这三种树分别是：弹性二叉树（ebtree）、紧凑型弹性二叉树（cebtree）和红黑树（rbtree）。测试分析了插入、查找和删除操作的时间，使用了不同的键类型（u32/u64计时器、64位随机数、短字符串、真实IPv4地址、真实用户代理）和树的大小（512到100万条目）。还研究了键分布的影响以及基于哈希的多个树头（1、256、65536）的使用。

主要发现：
*   **计时器：** 由于对规则分布的键具有更好的平衡性，Ebtree在插入/删除类似计时器的键时比rbtree快得多（3倍）。如果原始性能不是关键，Cbtree提供了一种内存高效的替代方案。
*   **64位哈希：** Ebtree通常是最佳选择，除非空间至关重要，否则cebtree没有提供显着的优势。哈希处理显着提高了所有树类型的插入速度。
*   **短字符串：** 如果不需要排序，使用大量桶进行哈希处理并使用rbtree可以提供最快的查找速度。如果需要排序，ebtree比cebtree更好。
*   **IPv4地址：** 由于地址分布不佳，没有一种单一的实现能够在整个范围内表现出色。建议在索引之前对IPv4键进行哈希处理。
*   **用户代理：** 对于大型、大部分相似的字符串，Rbtree更胜一筹。在这种情况下，Cbtree的性能很差。如果不需要排序，建议对输入进行哈希处理。

文章得出结论，前缀树（ebtree和cebtree）对键分布更为敏感。对于具有大键的高性能，如果不需要排序，建议使用rbtree或哈希处理。

---

## 24. LLM代码生成可能导致信任侵蚀

**原文标题**: LLM code generation may lead to an erosion of trust

**原文链接**: [https://jaysthoughts.com/aithoughts1](https://jaysthoughts.com/aithoughts1)

无法访问文章链接。

---

## 25. AccessOwl（YC S22）正在招聘一名Elixir工程师，以连接数百个SaaS。

**原文标题**: AccessOwl (YC S22) is hiring an Elixir Engineer to connect 100s of SaaS

**原文链接**: [https://www.ycombinator.com/companies/accessowl/jobs/1shGwy2-senior-software-engineer-elixir-focus](https://www.ycombinator.com/companies/accessowl/jobs/1shGwy2-senior-software-engineer-elixir-focus)

AccessOwl，一家由 Y Combinator (S22) 支持、正在革新 SaaS 管理的初创公司，现招聘一位 Elixir 资深软件工程师。该职位为完全远程，工作时间需在欧洲中部时间 (柏林) ±3 小时内，提供 7 万欧元至 9.5 万欧元薪资以及 0.05%-0.10% 的股权。

AccessOwl 旨在通过利用 RPA 和自主 AI 工作流的创新方法，取代过时的系统，从而简化 SaaS 访问、支出和合规性。他们正在寻找一位拥有 5 年以上 Web 开发经验、精通 Elixir 和其他语言，并拥抱 AI 以实现快速迭代的人才。理想的候选人应乐于解决客户问题，将其分解为可管理的部分，并为 TDD 和持续交付等现代工程原则做出贡献。

职责包括推进 AccessOwl 平台发展、构建集成、为云基础设施做出贡献以及积极参与产品讨论。

公司提供灵活的、远程优先的环境，最先进的技术栈（Elixir、Phoenix、LiveView），以及年度团队休假。AccessOwl 是一家盈利公司，专注于建立可持续发展的业务，并培养包容和雄心勃勃的团队环境。申请者请在求职信中包含三句话，说明是什么吸引您与 AccessOwl 交流。

---

## 26. 要解决哪些问题 (1966)

**原文标题**: What Problems to Solve (1966)

**原文链接**: [http://genius.cat-v.org/richard-feynman/writtings/letters/problems](http://genius.cat-v.org/richard-feynman/writtings/letters/problems)

费曼在一封给以前的学生真野浩一的信中，谈及他对目前在相干理论和湍流大气中电磁波传播研究的不满。费曼认为，真野的不快乐源于对什么是有价值的科学问题的误解，这很可能受到了他以前教授的影响。

费曼认为，最有价值的问题是科学家能够切实解决或做出贡献的问题。他建议真野专注于更简单，甚至看似微不足道的问题，因为这些问题更容易取得成功。不应低估取得进展和帮助他人的乐趣，即使是以微小的方式。

费曼后悔过去指派给真野一个问题，而不是让他自己去发现，这导致了他对什么是有趣和重要的问题的误解——即那些可以积极研究并可能解决的问题。

他强调，如果科学家能够做出切实的贡献，那么没有问题太小或微不足道。他用自己的一系列研究项目来说明这一点，从平凡的（摩擦、电镀）到复杂的（中子扩散、冲击波、弹性弯曲体、湍流）。他建议真野接受他回答同事简单问题的能力，并在他的贡献中找到价值，而不是仅仅渴望“宏大”的问题。最后，费曼鼓励真野认识到自身的价值，并在解决问题中找到快乐，无论问题的规模大小。

---

## 27. RSS服务器端阅读器

**原文标题**: RSS Server Side Reader

**原文链接**: [https://matklad.github.io/2025/06/26/rssssr.html](https://matklad.github.io/2025/06/26/rssssr.html)

本文探讨了作者创建个性化RSS阅读器的过程，重点介绍了一种服务器端方法。 由于现有RSS阅读器功能丰富（如离线文章保存和嵌入式浏览器），作者对其不满意，而他只需要通知。

作者最初的客户端尝试，一个使用浏览器本地存储的网页，因CORS限制而失败。 成功的解决方案包括将其博客构建过程的一部分构建为个性化feed，并将其托管为静态HTML页面 (blogroll.html)。 此页面显示每个feed的最新三篇文章，而不维护已读/未读状态。 blogroll.txt文件包含一个简单的feed URL列表。 本文包含用于获取和解析博客列表、将数据转换为HTML的代码片段（Deno），以及用于每日重建博客列表的GitHub Actions工作流。

由于Atom feeds的简洁性，作者更喜欢Atom feeds而不是原始RSS（尽管更喜欢JSON Feed，但未维护）。 这种方法的关键好处是能够从任何设备访问精选的feed。 最后，作者指出还有一个额外的资源：他们所有时间最喜欢的链接的静态列表，单独托管。

---

## 28. 用Claude构建和托管AI驱动的应用 - 无需部署

**原文标题**: Build and Host AI-Powered Apps with Claude – No Deployment Needed

**原文链接**: [https://www.anthropic.com/news/claude-powered-artifacts](https://www.anthropic.com/news/claude-powered-artifacts)

此文章宣布Claude应用推出一项新功能，允许开发者直接在平台内构建、托管和分享AI驱动的应用，无需传统的部署流程。这项新功能使Claude能够生成作为其API驱动的应用程序的交互式作品。开发者的主要优势包括：

*   **简化分享：** 用户使用自己的Claude账户进行身份验证，其API使用量将计入他们的订阅，而不是开发者的，这意味着开发者无需为用户的使用付费。
*   **开放代码：** Claude编写驱动应用的实际代码，允许开发者自由查看、修改和分享。
*   **快速迭代：** 开发者可以快速构建和迭代他们的应用，而无需与扩展相关的复杂性和成本。
*   **专注于创作：** Claude处理诸如提示工程、错误处理和编排等技术细节，让开发者专注于应用程序的核心功能。

早期示例包括AI驱动的游戏、个性化学习工具、数据分析应用、写作助手和代理工作流程。要开始使用，用户可以在Claude应用中启用交互功能并描述所需的应用程序。然后，Claude将编写代码，根据反馈进行调试，并允许通过链接进行即时分享。目前的限制包括没有外部API调用，没有持久存储，以及基于文本的完成API。此功能目前处于测试阶段，适用于Free、Pro和Max计划用户。

---

## 29. 美国的监禁率正在下降

**原文标题**: America’s incarceration rate is in decline

**原文链接**: [https://www.theatlantic.com/ideas/archive/2025/06/prisoner-populations-are-plummeting/683310/](https://www.theatlantic.com/ideas/archive/2025/06/prisoner-populations-are-plummeting/683310/)

美国大规模监禁时代即将终结

---

## 30. LM Studio 中的 MCP

**原文标题**: MCP in LM Studio

**原文链接**: [https://lmstudio.ai/blog/lmstudio-v0.3.17](https://lmstudio.ai/blog/lmstudio-v0.3.17)

LM Studio 博客宣布在 0.3.17 版本中引入模型上下文协议 (MCP) 支持，使用户可以将 MCP 服务器连接到应用程序并与本地模型一起使用。MCP 允许 LLM 访问外部工具和资源，LM Studio 支持本地和远程 MCP 服务器。用户可以通过编辑 `mcp.json` 文件或通过“添加到 LM Studio”按钮添加 MCP 服务器。

该文章提供了一个使用 Hugging Face MCP 服务器进行模型和数据集搜索的示例，并警告用户谨慎安装来自不受信任来源的 MCP，因为存在潜在的安全风险。它还描述了工具调用确认对话框，该对话框允许用户在执行前审查和编辑工具调用参数。

该文章进一步解释了 LM Studio 如何加载 MCP 服务器，强调了安装必要的工具（如 `npx` 或 `uvx`）对于本地服务器的重要性。它还包括一个面向开发者的部分，介绍如何为他们的 MCP 服务器创建“添加到 LM Studio”按钮。

最后，该文章详细介绍了 0.3.17 版本中的其他更新，包括对 11 种新语言的支持、错误修复、UI 改进（如“Solarized Dark”主题），以及对聊天功能、工具调用处理和 MCP 可靠性的各种增强。最后鼓励开发者注册私人测试版，以创建他们自己的工具和自定义资源。

---

## 31. Linux 下 Windows Hello 风格的面部识别认证

**原文标题**: Howdy – Windows Hello style facial authentication for Linux

**原文链接**: [https://github.com/boltgolt/howdy](https://github.com/boltgolt/howdy)

Howdy：在Linux上启用Windows Hello风格的面部识别认证

Howdy利用红外发射器和摄像头，通过PAM系统在Linux上实现Windows Hello风格的面部识别认证，可用于登录、锁屏、sudo等操作。它适用于Debian/Ubuntu、Arch Linux、Fedora和openSUSE，并为每个发行版提供特定的安装说明。

安装通常涉及添加软件源、更新软件包和安装`howdy`包。某些发行版可能需要额外的配置步骤，如其各自的Wiki中所述。也可以从源代码构建，这需要Python 3.6+、pip、setuptools、meson、ninja和其他依赖项。

安装后，用户必须使用`sudo howdy add`添加面部模型。然后可以使用`sudo -i`测试面部识别认证。配置选项可通过`sudo howdy config`访问。`howdy`命令提供诸如添加、删除、列出面部模型、拍摄快照和测试摄像头输入等功能。

本文强调，Howdy是一项便利功能，**并非安全增强**。它容易受到相貌相似的人或高质量照片的攻击。强烈建议不要将Howdy作为唯一的身份验证方法。Python错误会被记录到控制台，认证失败可能会记录在`/var/log/auth.log`中。

---

## 32. 禁止使用AI代码生成器的政策定义

**原文标题**: Define policy forbidding use of AI code generators

**原文链接**: [https://github.com/qemu/qemu/commit/3d40db0efc22520fa6c399cf73960dced423b048](https://github.com/qemu/qemu/commit/3d40db0efc22520fa6c399cf73960dced423b048)

本文概述了QEMU项目禁止使用ChatGPT、Claude、Copilot和Llama等AI代码生成器进行代码贡献的政策。该政策源于对AI生成代码版权和许可状态不明的担忧，这可能给项目带来潜在的法律风险。

QEMU要求贡献者遵守开发者原创声明（DCO），这要求完全理解贡献内容的版权和许可影响。AI生成输出的许可不确定性使得难以遵守DCO。这些AI模型使用的训练数据通常包含具有限制性许可证的材料，可能与QEMU的要求不兼容。

因此，QEMU将拒绝任何疑似或已知包含AI生成代码的贡献。但是，该政策并不限制将AI用于研究、静态分析或调试，只要输出不被纳入提交的代码中。

该政策强调当前AI生成内容周围法律环境的缺乏清晰性。虽然该政策可能会随着AI工具的成熟和法律先例的建立而发展，但例外情况将根据具体情况进行考虑，需要证明许可证和版权状态的清晰性。关键在于降低与AI生成代码相关的法律风险，并确保符合DCO。

---

## 33. 离线俱乐部

**原文标题**: The Offline Club

**原文链接**: [https://www.theoffline-club.com](https://www.theoffline-club.com)

线下俱乐部是一个全球性运动，旨在通过提供屏幕时间替代方案来促进现实世界的连接。他们举办线下活动、数字排毒静修和商务活动，旨在帮助人们解除网络连接、放松身心并与志同道合的人建立联系。

该俱乐部拥有基于251条评论的4.7/5评分，突显了客户满意度。他们提供各种活动，包括咖啡馆聚会、无手机晚餐以及用于阅读、绘画和写作的创意空间。线下俱乐部旨在提供一种人们可以进行有意义的对话、集中精力并从社交媒体中休息的环境。

他们在包括阿姆斯特丹、伦敦、巴黎、巴塞罗那、米兰、柏林和哥本哈根在内的七个国家/地区的多个城市设有分会，并且正在积极寻求扩张。个人可以加入城市等候名单或申请启动自己的本地线下俱乐部。

线下俱乐部还提供数字排毒静修，提供远离数字干扰的周末。对于企业，他们为团队和组织策划独特的线下体验和活动。他们的工作已在各种媒体上得到报道，突显了人们对更真实联系的日益增长的追求。该俱乐部发行“线下时报”，这是一份包含线下灵感和数字排毒技巧的通讯，并提供24小时数字排毒挑战。

---

## 34. Apptainer: Linux 应用程序容器

**原文标题**: Apptainer: Application Containers for Linux

**原文链接**: [https://apptainer.org/](https://apptainer.org/)

Apptainer (原 Singularity) 是一个容器系统，专为软件的可移植性和可重复性而设计。它简化了容器的创建和执行，允许用户封装应用程序组件，以便轻松共享和归档。

Apptainer 的主要特性和优势包括：

*   **安全性：** Apptainer 专为安全执行而设计，禁止容器内的权限提升，确保用户在容器内外拥有相同的权限。
*   **可移植性：** 单文件 SIF 格式便于在各种环境中轻松共享和移动工作负载，从工作站到 HPC 集群和边缘设备。
*   **加密：** Apptainer 支持容器加密，并与 Vault 等密钥管理平台集成，以保护应用程序、模型和数据。
*   **Docker 兼容性：** Apptainer 提供与来自 OCI 注册表的 Docker 容器的最大兼容性，允许用户以最小或无需修改的方式从 Docker Hub 拉取、运行和构建容器。 这简化了已熟悉 Docker 的用户的过渡。

Apptainer 旨在提供一种安全、可移植且易于使用的容器解决方案，适用于工业界和学术界。

---

## 35. 花瓣折叠艺术

**原文标题**: The Art of Hanakami, or Flower-Petal Folding

**原文链接**: [https://origamiusa.org/thefold/article/art-hanakami-or-flower-petal-folding](https://origamiusa.org/thefold/article/art-hanakami-or-flower-petal-folding)

赖迈克的文章《花瓣折纸艺术》介绍了一种独特的折纸技巧，使用花瓣代替纸张。花瓣折纸（Hanakami）是作者创造的一个术语，强调用有机花瓣替代传统纸张。文章详细介绍了整个过程，从选择和准备花瓣到将它们折叠成精致的折纸模型。

赖强调，找到合适的花瓣至关重要。他建议考虑花期、花瓣形状和大小、干燥后的颜色、厚度、表面纹理和香味。平整、花瓣少的、不太厚的花朵最容易折叠。

这个过程包括收集花瓣，最好是落下的花瓣，以尽量减少对环境的影响，然后将它们干燥并压平，以去除多余的水分并使它们平整。目标是达到柔韧的状态，而不是完全干燥。干燥后，将花瓣切割成正方形，最大限度地利用可用表面积并考虑纹路。实验是关键，如果花瓣太脆，可以小心地重新引入水分。

文章强调了花瓣折纸固有的挑战，承认花瓣并非为折叠而设计。它鼓励耐心，并强调过程的价值，即使最终的模型并不完美。最终，花瓣折纸提供了一种欣赏花朵之美的新颖方式，通过将它们转化为精致的折纸艺术。

---

## 36. Gemini 命令行工具

**原文标题**: Gemini CLI

**原文链接**: [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)

Gemini CLI：将 Gemini 模型带到终端的开源 AI 助手

本文介绍 Gemini CLI，一款开源 AI 助手，它将 Gemini AI 模型的强大功能直接带到开发者的终端。它定位为一个多功能工具，适用于编码、内容生成、问题解决、研究和任务管理。

主要优势包括：

*   **免费访问：** 用户可以通过个人 Google 帐户登录以获得免费的 Gemini Code Assist 许可证，从而免费访问 Gemini 2.5 Pro (100 万 token 上下文窗口)，并享有慷慨的使用限制（每分钟 60 个请求，每天 1000 个）。付费选项可用于更高的使用量或特定模型。
*   **强大的功能：** Gemini CLI 提供诸如通过 Google 搜索进行实时上下文扎根提示、通过模型上下文协议 (MCP) 扩展功能、自定义提示以及自动化任务等功能。
*   **开源和可扩展：** 开发者可以检查代码、贡献改进意见并自定义工具以满足他们的需求。
*   **与 Gemini Code Assist 集成：** Gemini CLI 与 Google 的 AI 编码助手 Gemini Code Assist 共享技术，从而可以在终端和 VS Code 中实现无缝的 AI 驱动编码。Gemini Code Assist 的代理模式在所有计划中均可用，提供诸如多步规划和错误恢复等高级功能。

本文强调了 Gemini CLI 在显著升级命令行体验和简化开发者工作流程方面的潜力。它鼓励开发者尝试使用。

---

## 37. 在日本靠陌生人的慷慨解囊度日

**原文标题**: Getting by on the Generosity of Strangers in Japan

**原文链接**: [https://theworld.org/stories/2025/06/20/out-of-eden-walk-getting-by-on-the-generosity-of-strangers](https://theworld.org/stories/2025/06/20/out-of-eden-walk-getting-by-on-the-generosity-of-strangers)

在本次访谈中，国家地理探险家保罗·萨洛佩克探讨了款待在他为期 12 年的“走出伊甸园”徒步旅行中的重要作用，这是一次追溯人类跨越大陆迁徙的旅程。他讲述了在日本 Migita 旅馆的经历，这家旅馆由 84 岁的山名芳子经营，并强调了她的热情、韧性以及她为客人提供的独特的欢迎感。

萨洛佩克强调，款待是一种普遍的人类特征，在他的旅程中始终如一地遇到，即使是在意想不到的地方，如牧羊人的小屋、宫殿和洞穴。他指出，那些拥有最少资源的人往往提供最慷慨的款待，这源于对苦难的理解。

他反思了偶然相遇和同情在他的项目中的重要性，并表示人是他的最终目的地。在承认文化差异和他自己的失误的同时，萨洛佩克欣赏日本高度规范化的款待传统，即使是鞋子的摆放也具有重要意义。他强调，多年来穿越各种文化，提高了他对人类善良和美好的认识，加强了他对它在世界范围内普遍存在的信念。

---

## 38. 机器人还是人类？为互联网打造隐形图灵测试

**原文标题**: Bot or human? Creating an invisible Turing test for the internet

**原文链接**: [https://research.roundtable.ai/proof-of-human/](https://research.roundtable.ai/proof-of-human/)

圆桌科技的文章认为，当前机器人检测方法（如谷歌的reCAPTCHA v3）不足以有效识别AI代理，因为即使表现出非人类行为，AI代理也能通过验证。作者提出了一种基于行为和认知特征的新方法，强调人类在按键动态和鼠标移动方面具有独特的模式，而机器人难以令人信服地复制，因为这样做的成本过于复杂。

文章展示了交互式演示，突出了人类和机器人之间在按键模式、鼠标移动和认知表现（使用Stroop任务）上的差异。这些演示表明，机器人通常在打字和移动方面表现出不自然的规律性，并且缺乏人类所经历的认知干扰。

作者认为，复制人类认知的完整范围，而不仅仅是模仿输出，对AI代理来说是一个巨大的挑战。他们描述了他们的早期研究，其中包括“波士顿温度测试”等任务，在这些任务中，人类的错误是可以预测的，这与机器人随机或过于完美的反应不同。

圆桌科技提供了一个人类身份验证API，该API使用行为和认知分析来隐形、连续和即时地验证用户。这种方法侧重于使机器人复制人类认知在经济上具有挑战性，而不是依赖于侵犯隐私的方法。最终，目标是创建一个“隐形的图灵测试”，可以有效地在互联网上区分人类和AI代理。

---

## 39. 首个非阿片类止痛药

**原文标题**: The first non-opoid painkiller

**原文链接**: [https://www.worksinprogress.news/p/the-first-non-opioid-painkiller](https://www.worksinprogress.news/p/the-first-non-opioid-painkiller)

本文详细介绍了Journavx (suzetrigine) 的研发和批准过程。Journavx是首个适用于术后疼痛的非阿片类镇痛药，于2025年1月获得FDA批准。 传统的止痛药依赖于阿片类药物，虽然有效，但存在严重的成瘾和过量风险。 Journavx 的作用机制不同，它靶向位于外周伤害性感受器（疼痛感应神经元）上的NaV1.8钠离子通道，以阻止疼痛信号到达大脑，这与作用于大脑中枢的阿片类药物不同。

Journavx 的研发是一个漫长而复杂的过程，历时数十年，因为在不扰乱其他重要身体功能的情况下靶向疼痛通路面临诸多挑战。 之前尝试的非阿片类镇痛方法，如TRPV1和神经生长因子抑制剂，因显著的副作用而失败。

Vertex Pharmaceuticals 公司利用其E-VIPR 技术筛选了数百万种化合物，以寻找一种选择性的NaV1.8阻滞剂，在此过程中面临许多挫折和终止的项目。 成功的候选药物 VX-548 (suzetrigine) 在临床试验中显示出治疗急性疼痛的疗效，且不良反应极小。

虽然 Journavx 并非完美解决方案，因为它在疗效上并未超过阿片类-对乙酰氨基酚的组合，并且其在慢性疼痛中的应用仍在研究中，但它代表着在最大限度地减少阿片类药物使用方面迈出了重要一步。 Vertex 公司正在继续研究更有效和更具选择性的 NaV1.8 阻滞剂，并探索与 NaV1.7 抑制剂的潜在互补性。

---

## 40. 我在乌克兰作战，以下是我认为FPV无人机有点糟糕的原因

**原文标题**: I fought in Ukraine and here's why FPV drones kind of suck

**原文链接**: [https://warontherocks.com/2025/06/i-fought-in-ukraine-and-heres-why-fpv-drones-kind-of-suck/](https://warontherocks.com/2025/06/i-fought-in-ukraine-and-heres-why-fpv-drones-kind-of-suck/)

雅库布·亚伊凯（Jakub Jajcay）是一名在乌克兰参与FPV攻击无人机作战的志愿者，他认为虽然FPV无人机被吹捧为革命性的，但它们的效果往往不如所描述的那样。尽管无人机可以在视频中执行令人印象深刻的打击，但这些只是例外。

亚伊凯的团队成功率只有43%（无人机击中目标并引爆），但大多数出击的目标区域已经被迫击炮或其他无人机打击过。只有个位数的任务利用了无人机独特的性能（其他手段无法实现的精确打击）。这是因为指挥官即使在存在更廉价的替代方案（如成本远低于500美元无人机出击的迫击炮）时也使用它们，并且因为无人机在技术上不可靠。

无人机经常出现技术故障、夜视能力有限且易受天气影响。四分之一的无人机在起飞前就发生故障，通常是由于无线电接收器或视频发射器问题。即使在空中，电池也经常耗尽，弹头有时也无法引爆。它们很难飞行，需要大量训练，并且缺乏导航辅助设备。

最大的问题是不可靠的无线电链路，很容易受到地形和电子战干扰。来自其他无人机（友方或敌方）的信号干扰和干扰导致了相当一部分任务失败。仅敌方干扰就击落了31%的出击。

虽然技术正在改进（更好的组件、数字信号、信号增强器），但目前的解决方案，如光纤电缆无人机，也存在机动性有限、成本更高和生产能力有限等缺点。

---

## 41. 一个新的PNG规范

**原文标题**: A new PNG spec

**原文链接**: [https://www.programmax.net/articles/png-is-back/](https://www.programmax.net/articles/png-is-back/)

本文宣布在停滞二十余年后，PNG规范迎来重大更新。主要更新包括：仅使用4字节即可实现正确的HDR支持、官方认可APNG动画以及支持Exif数据。此次更新由W3C定时文本工作组对HDR支持的需求驱动，并获得了Adobe、Apple、Google和BBC等主要公司的支持。

文章强调，包括Chrome、Safari、Firefox、Photoshop和DaVinci Resolve在内的许多程序已经支持新规范，广播公司也在更新其硬件和工具。作者还预计，下一个版本（第四版）将侧重于提高HDR和SDR的互操作性。第五版将侧重于更好的压缩和并行编码/解码。作者感谢PNG工作组为使更新后的规范成为现实所付出的辛勤努力。作者还指出，美国国会图书馆、加拿大图书馆和档案馆以及澳大利亚国家档案馆都在使用和推荐PNG格式。

---

## 42. 可嵌入网页的通用 Lisp

**原文标题**: Web Embeddable Common Lisp

**原文链接**: [https://turtleware.eu/static/paste/wecl-test-gl/main.html](https://turtleware.eu/static/paste/wecl-test-gl/main.html)

文章“Web Embeddable Common Lisp”可能探讨了在 Web 应用程序中嵌入 Common Lisp (CL) 代码的潜力或实际实现。仅从标题来看，我们可以推断出以下可能方面：

*   **关注 Web 集成：** 核心主题围绕着在 Web 环境中利用 CL。这将其与通常在 Web 浏览器之外运行的传统 CL 应用程序区分开来。
*   **嵌入 vs. 仅服务器端：** 术语“embeddable”（可嵌入）表明 CL 代码可以集成到网页或应用程序中，其方式超越了简单的服务器端处理（例如，生成 HTML）。 它可能暗示在浏览器中直接执行 CL 代码，或者具有某种形式的客户端 CL 功能。
*   **潜在技术：** 文章可能涵盖支持这种嵌入的技术或方法，例如：
    *   将 CL 转译为 JavaScript（或 WebAssembly）。
    *   创建基于 CL 的 Web 框架，以方便嵌入组件。
    *   使用 CL 作为服务器端语言，并与客户端 JavaScript 紧密集成。
*   **优势/用例：** 它还可能探讨在 Web 开发中使用 CL 的优势（例如，其表现力、强大的宏系统或性能）以及嵌入 CL 可能特别有益的潜在用例。
*   **局限性/挑战：** 最后，文章可能会讨论与在 Web 环境中嵌入 CL 相关的挑战，例如部署复杂性、调试或性能考虑因素。

本质上，该文章可能探讨了 Common Lisp 和 Web 技术的交叉点，特别是侧重于直接在 Web 应用程序中嵌入 CL 功能的方法和机会。

---

## 43. Iroh: 建立对等连接的库

**原文标题**: Iroh: A library to establish direct connection between peers

**原文链接**: [https://github.com/n0-computer/iroh](https://github.com/n0-computer/iroh)

Iroh 是一个 Rust 库，旨在建立直接的对等连接，最大限度地减少对网络的依赖。它通过公钥促进连接，寻找并维护最快的路由，即使通过使用打孔技术的 NAT，并回退到公共中继服务器。Iroh 通过持续的连接测量来优先考虑速度，并基于 QUIC 构建，以实现经过身份验证的加密、并发流和避免队头阻塞。

该库支持可组合的协议，例如用于内容寻址的 blob 传输的 iroh-blobs、用于可扩展的发布-订阅网络的 iroh-gossip、用于 blob 的键值存储的 iroh-docs，以及 iroh-willow（正在建设中）。

入门涉及通过 `cargo add iroh` 使用 Rust 库。文档包含示例代码，演示了基本的连接和通信。Iroh 提供了 FFI 绑定，以便在其他语言中使用。

该存储库包含多个 crate：`iroh`（核心库）、`iroh-relay`（中继服务器）、`iroh-base`（通用类型）、`iroh-dns-server`（NodeId 的 DNS 服务器）和 `iroh-net-report`（网络分析工具）。该项目采用 Apache 2.0 和 MIT 双重许可。

---

## 44. Android工作组成立公告

**原文标题**: Announcing the Android Workgroup

**原文链接**: [https://forums.swift.org/t/announcing-the-android-workgroup/80666](https://forums.swift.org/t/announcing-the-android-workgroup/80666)

Swift社区启动Android工作组，以正式支持Android作为Swift平台。该工作组旨在建立并维护Android作为Swift的官方支持平台。要参与其中，个人可以查看Android工作组章程，参与Android论坛上的讨论，并使用论坛上的@android-workgroup账号直接联系工作组。

---

## 45. 星际航行：视角与耐心

**原文标题**: Interstellar Flight: Perspectives and Patience

**原文链接**: [https://www.centauri-dreams.org/2025/06/25/interstellar-flight-perspectives-and-patience/](https://www.centauri-dreams.org/2025/06/25/interstellar-flight-perspectives-and-patience/)

保罗·吉尔斯特的《星际航行：视角与耐心》反思了星际旅行所涉及的巨大距离和时间尺度，这源于科尔特雷恩的音乐和帕克太阳探测器的成就。文章将人类的速度记录（阿波罗10号、旅行者1号、帕克太阳探测器）与我们与最近的恒星比邻星之间存在的巨大鸿沟进行对比。他指出，以帕克探测器的速度，仍然需要6600年才能到达比邻星。

吉尔斯特强调了旅行者1号将于2027年到达距离太阳一个光日的里程碑意义，这是一个象征性的里程碑。然后，他将庞大的旅行者项目（11000个工作年）与历史上诸如大金字塔建造等壮举相提并论。胡夫太阳船进一步强调了人类对宇宙旅程的持久迷恋。

他强调需要重新校准我们对时间和距离的感知。在承认挑战的同时，他表达了对诸如突破摄星等定向能量推进的希望，这可能会在几十年内实现对比邻星的飞掠。评论部分进一步深入探讨了星际探索的伦理考量、技术进步的可能性以及长期生存的重要性。

---

## 46. Libxml2 的“不设安全封锁”政策

**原文标题**: Libxml2's "no security embargoes" policy

**原文链接**: [https://lwn.net/SubscriberLink/1025971/73f269ad3695186d/](https://lwn.net/SubscriberLink/1025971/73f269ad3695186d/)

LWN.net文章讨论了libxml2新的安全策略，起因是维护者Nick Wellnhofer对维护一个广泛使用的开源项目却缺乏足够支持感到沮丧。Wellnhofer宣布libxml2将不再遵守安全禁运，而是将安全漏洞视为普通bug，一旦报告就会公开。他认为安全研究人员要求的无偿工作负担不可持续，且苹果、谷歌和微软等主要公司严重依赖libxml2，却没有提供相应的企业贡献。他还辞去了相关libxslt项目的维护者职务。

Wellnhofer认为这些公司从libxml2宽松的MIT许可证中获益良多，但未能充分支持其维护，实际上是在利用志愿者的善意。这项政策转变旨在鼓励贡献，并迫使公司通过改进libxml2、开发自己的解决方案或切换到更好的替代方案来解决其技术债务。

文章还探讨了开源生态系统中更广泛的企业行为问题，强调了一种“公共领域的监管俘获”，即公司在没有贡献的情况下利用开源资源。它提出了公共维护条款 (MAINTENANCE-TERMS.md) 的概念，以给予维护者“心理安全”，从而拒绝企业的需求。文章表明Wellnhofer的立场反映了开源维护者中日益增长的情绪，他们感到被企业利用。最终，文章认为开源的可持续性取决于解决企业利益和维护者负担之间的不平衡。

---

## 47. 可爱多是否在盈利模式上出了问题？

**原文标题**: Is Lovable getting monetization wrong?

**原文链接**: [https://getlago.substack.com/p/lovable-makes-60m-in-6-monthsbut](https://getlago.substack.com/p/lovable-makes-60m-in-6-monthsbut)

以下是基于所提供URL的文章《Lovable是否在货币化方面犯了错误？》的摘要：

文章讨论了Lovable公司，据报道该公司在六个月内创造了6000万美元的收入，并质疑他们目前的货币化策略对于长期增长和盈利能力，尤其是在SaaS领域，是否是最优的。尽管收入增长迅速令人印象深刻，但作者认为Lovable可能因为产品定价过低或为他们所收取的费用提供了过多的价值而错失了赚钱的机会。

作者认为，Lovable专注于快速获取客户和看似激进的定价可能更注重短期收益，而不是建立一个可持续的高价值业务。他们指出，在SaaS领域，感知价值和支付意愿通常与功能、支持和整体体验相关。低估产品价值可能会吸引对价格高度敏感的客户，而这些客户不太可能忠诚或支持该平台。

文章建议Lovable考虑实施分层定价模式，提供不同的功能组合，以满足不同的客户需求和支付意愿。这将使他们能够从愿意为高级功能和专门支持付费的用户那里获得更多价值。作者强调了细分客户以及将定价与交付给每个细分市场的特定价值对齐的重要性。最终，文章认为，虽然令人印象深刻的收入增长是一个积极的指标，但Lovable应仔细评估其货币化策略，以确保其与长期可持续性和盈利能力相符。

---

## 48. 微软依赖有风险

**原文标题**: Microsoft Dependency Has Risks

**原文链接**: [https://blog.miloslavhomer.cz/p/microsoft-dependency-has-risks](https://blog.miloslavhomer.cz/p/microsoft-dependency-has-risks)

米洛斯拉夫·霍默的文章《微软依赖的风险》分析了过度依赖微软产品可能造成的后果。起因是微软据称因美国制裁而封锁了一名国际刑事法院 (ICC) 员工的邮箱。作者探讨了组织机构面临微软服务中断的可能性和成本。

他认为，美国政治决策（尤其是关于制裁的决策）具有不可预测性，加上微软对美国政府合同的依赖，使得微软很可能遵守制裁要求，从而可能中断对受影响客户的服务。他承认这种可能性很低，但后果可能很严重。

文章讨论了公司如何在通信、文件管理、身份管理和备份方面严重依赖微软。这些服务的完全中断可能会造成极其高昂的代价，对于大型企业而言，每天可能损失数百万美元。

然后，他试图应用安全投资回报率 (ROSI) 模型来确定防止这种情况发生的合理投资水平。然而，他得出结论，由于事件发生的可能性较低，因此很难证明进行大量投资是合理的，并且缺乏可靠的数据使得准确建模成为不可能。他表示，由于安全领域的数据不成熟，这些 ROSI 计算实际上是不可能的。他强调了平衡使用微软产品的好处与依赖的潜在风险所面临的挑战，并且如果没有准确的预测，几乎不可能对合理的防御进行建模。

---

## 49. Ars测试发现，SteamOS上游戏运行速度比Windows 11快

**原文标题**: Games run faster on SteamOS than Windows 11, Ars testing finds

**原文链接**: [https://arstechnica.com/gaming/2025/06/games-run-faster-on-steamos-than-windows-11-ars-testing-finds/](https://arstechnica.com/gaming/2025/06/games-run-faster-on-steamos-than-windows-11-ars-testing-finds/)

Ars Technica测试联想拯救者Go S上SteamOS 3.7与Windows 11的游戏性能，发现SteamOS通常能在近期游戏中提供更高的帧率。这标志着相对于表现不如Windows的初代SteamOS而言，是一项重大改进。

测试包括在两个操作系统上使用内置基准测试，以不同的图形设置运行五款高端3D游戏。虽然Windows 11安装了联想更新的驱动程序，但文章指出获取真正最新的驱动程序存在挑战，最终使用了非官方的华硕驱动程序。

结果表明，SteamOS在大多数测试游戏中提供了显著的帧率提升。在某些情况下，操作系统之间的差异可能意味着可玩帧率和不可玩帧率之间的差异。虽然《无主之地3》表现出相似的性能，但其他游戏在Windows上的帧率下降高达36%。

SteamOS性能的提升归功于Valve持续致力于Proton（Windows游戏的翻译层）和Linux的Mesa图形驱动程序，以及与通用Windows操作系统相比，消除了不必要的开销。

尽管性能有所提升，但文章承认某些游戏与SteamOS不兼容，其硬件兼容性仍然有限。然而，性能优势、较低的零售价和更精简的用户界面，巩固了SteamOS作为游戏掌机上Windows的可行替代方案的地位。

---

## 50. RaptorCast：消息层设计

**原文标题**: RaptorCast: Designing a Messaging Layer

**原文链接**: [https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer](https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer)

RaptorCast旨在解决权益证明区块链中区块提议从领导者高效、安全地传播到验证者的问题。它专注于性能、安全性和稳健性，尤其是在存在丢包和拜占庭行为者的情况下。

该设计采用UDP以提高速度，并通过编码系统和数据包级身份验证来缓解固有的可靠性问题。Raptor码的一种实现R10，因其在前向纠错（FEC）中的性能和可扩展性而被选择，增加了冗余以确保在发生丢包时的数据恢复。为了防止篡改，每个数据块都包含一个Merkle证明和领导者的签名，以验证数据的完整性和来源。

该系统将区块提议结构化为适合UDP数据包的数据块。每个数据包包含一个Merkle证明、一个头部（包括领导者的签名、版本、纪元、时间戳和区块提议哈希）、一个数据块头部以及数据有效负载。Merkle树方法减少了所需的签名数量。

广播策略采用结构化转发，其中验证者将特定的数据部分重新广播到预定义的对等组。冗余级别是根据潜在的丢包和恶意节点确定的，以确保诚实的验证者收到足够的编码数据包来重建原始提议。R10编码系统建立在LT码的基础上，能够从源数据块生成编码符号。解码涉及一个剥离过程，从接收到的编码符号中逐步恢复源数据块。

---

## 51. 人间福祉的象征，也是劳作的直接目标

**原文标题**: The symbol of earthly good, and the immediate object of toil

**原文链接**: [https://crookedtimber.org/2025/06/23/the-symbol-of-earthly-good-and-the-immediate-object-of-toil/](https://crookedtimber.org/2025/06/23/the-symbol-of-earthly-good-and-the-immediate-object-of-toil/)

Hannah Forsyth的文章《尘世福祉的象征与劳动的直接目标》以乔治·艾略特的《织工马南》为视角，探讨了工作、金钱、权利与社会价值观之间的关系。受到偶然听到一个孩子因获得贴纸而兴奋的启发，作者探索了金钱作为尘世福祉的象征和劳动目标的概念。

她将西拉斯·马南对囤积黄金的痴迷与新教伦理相提并论，在后者中，金钱成为衡量价值和精神回报的标准。Forsyth将此与邓斯坦等认为自己理应获得财富而不论努力的角色形成对比，突显了社会体系中固有的不平等。

作者将这些主题与当代问题联系起来，例如基于种族、阶级和性别的权利持续存在。她批判了精英统治制度的理念，认为它常常强化现有的权力结构，并奖励那些已经享有特权的人。

最终，Forsyth强调了爱的变革力量，西拉斯·马南在抚养孩子而不是追求物质财富中找到了救赎和真正的价值。她以乐观的语调结尾，暗示人与人之间的联系和目标可以取代对金钱的追求，成为衡量价值的最终标准。

---

## 52. 准备颁发IP地址证书

**原文标题**: Getting ready to issue IP address certificates

**原文链接**: [https://community.letsencrypt.org/t/getting-ready-to-issue-ip-address-certificates/238777](https://community.letsencrypt.org/t/getting-ready-to-issue-ip-address-certificates/238777)

Let's Encrypt即将支持IP地址SAN证书

要点：

*   **即将支持IP地址SAN：** Let's Encrypt正准备支持签发证书，其中证书中的域名为IP地址。
*   **有效期短：** 带有IP地址SAN的证书将采用“shortlived”配置文件，意味着有效期仅为6天。
*   **初始仅限白名单：** 此功能最初将限制在批准用户的白名单中。尚未给出更广泛可用性的时间表，且暂不接受白名单申请。
*   **测试：** 他们提供了一个示例证书和一个使用该证书的网站用于测试，并要求对遇到的任何问题提供反馈。
*   **发现Bug：** 已经在Firefox的IP地址SAN显示中发现了一个Bug。

---

## 53. 希姆斯空心人

**原文标题**: The Hollow Men of Hims

**原文链接**: [https://www.alexkesin.com/p/the-hollow-men-of-hims](https://www.alexkesin.com/p/the-hollow-men-of-hims)

亚历克斯·凯辛的文章《Hims的空心人》严厉批评了Hims & Hers Health公司，指责该公司是一个利用漏洞和消费者绝望心理牟利的“医疗骗局”。凯辛认为，Hims & Hers通过欺骗性营销和订阅陷阱销售价格过高、可能存在危险的产品，将利润置于患者护理之上。

文章强调了Hims & Hers对FDA复配豁免条款的利用，用其大量生产“个性化”药物，例如从可疑的中国供应商处采购的司美格鲁肽（用于减肥）。他们与诺和诺德短暂的合作就证明了这一点，Hims在诺和诺德终止合作后仍继续销售仿冒Wegovy。

凯辛还批评了Hims & Hers治疗勃起功能障碍的方法，特别是他们的“硬糖”，其中混合了西地那非和他达拉非，即伟哥和希爱力的活性成分。这种组合被比作加油站出售的危险“犀牛”药丸，被视为一种隐藏在处方合法性下的危险捷径。

文章强调，该公司仿制药的价格很高，通常比传统药房贵得多，再加上自动化咨询和订阅陷阱。客户经常被锁定在长期承诺中，在没有警告的情况下被收费，并且难以获得退款，同时接受的医疗监督极少。凯辛总结说，Hims & Hers体现了监管套利，以牺牲真正的医疗保健和患者福祉为代价，通过便利性来优先考虑利润。

---

## 54. CUDA光线追踪速度是RTX的两倍：我的CUDA光线追踪之旅

**原文标题**: CUDA Ray Tracing 2x Faster Than RTX: My CUDA Ray Tracing Journey

**原文链接**: [https://karimsayedre.github.io/RTIOW.html](https://karimsayedre.github.io/RTIOW.html)

本文记录了作者创建一个高性能CUDA光线追踪器的历程，该追踪器在同一硬件上出人意料地超越了Vulkan/RTX实现 (RayTracingInVulkan)，在纠正了一个对比疏忽后，速度提高了2倍。主要结论是，在某些具有最小着色和程序几何图形（球体）的合成场景中，CUDA以计算为中心的方法可能比依赖专用RTX硬件核心进行BVH遍历更快。

作者强调了理解底层GPU架构和利用CUDA优化能力的重要性。他们重点指出了诸如递归之类的陷阱，这些陷阱会导致寄存器压力和内存溢出，以及避免虚函数调用和动态多态的必要性。

关键优化包括：

*   **采用仅头文件设计：** 实现了设备函数的主动内联，显著减少了寄存器溢出并提高了性能。
*   **用显式栈替换递归：** 改善了寄存器控制，限制了栈深度，并避免了不必要的内存溢出。
*   **策略性内联：** 谨慎选择内联较小的函数，并保留可以多次调用并节省编译时间的大型函数，不进行内联。

本文强调了在CUDA中管理寄存器压力和像GPU一样思考以实现最佳性能的重要性。作者总结说，CUDA提供了创建极速图形的工具，但开发者需要了解GPU的工作原理。

---

## 55. “僵化思维”阻碍抑郁症患者的决策

**原文标题**: 'Sticky thinking' hampers decisions in depression

**原文链接**: [https://www.bps.org.uk/research-digest/sticky-thinking-hampers-decisions-depression](https://www.bps.org.uk/research-digest/sticky-thinking-hampers-decisions-depression)

最近发表在《情绪》(Emotion)期刊上的一项研究（Yang & van Vugt, 2025）探讨了“思维固着”（难以摆脱某种想法）与易患抑郁症和焦虑症的个体决策能力受损之间的联系。研究人员发现，反刍思维，特别是“思维固着”，会妨碍做出决策时有效权衡各种选择的能力。

该研究让参与者填写问卷，以评估抑郁症状和他们思维的“固着性”。随后，一部分参与者撰写了关于负面经历的文章以诱发反刍思维，之后，在使用脑电图监测他们大脑活动的同时，他们完成了一项认知任务。报告思维越固着的参与者犯的错误越多，反应时间也越长。脑电图数据显示，思维固着与阿尔法波活动增加相关，表明一种注意力不集中的精神状态。

研究人员得出结论，“思维固着”可以解释易患抑郁症和焦虑症的个体决策能力受损的原因。然而，该研究的一个局限性是，在高“思维固着”组中，女性人数不成比例，这表明可能存在性别影响，值得进一步调查。研究结果支持这样一种观点，即解决反刍思维并促进灵活思维可能改善有抑郁倾向的个体的决策能力。

---

## 56. 第三空间与社区创业 (2024)

**原文标题**: Third places and neighborhood entrepreneurship (2024)

**原文链接**: [https://www.nber.org/papers/w32604](https://www.nber.org/papers/w32604)

Choi、Guzman和Small撰写的工作论文（NBER，2024年6月，2024年10月修订）调查了“第三空间”，特别是星巴克咖啡馆，对美国社区创业的影响。该研究发现，在没有现有咖啡店的社区引入星巴克会导致创业活动的显著增加。

通过比较开设了星巴克的普查区和计划开设但未开设的普查区，研究人员观察到，在7年期间，每年新创企业数量增加了9.1%至18%（即2.9至5.7家企业）。在星巴克-魔术师约翰逊合作项目所针对的弱势社区，这种影响更为显著。

作者认为，这种效应是由“网络机制”驱动的，这意味着星巴克咖啡馆促进了对创业成功至关重要的社会和专业关系的发展和利用。该研究得到了哥伦比亚Tamer社会企业研究所的支持，并使用了来自创业制图项目（Startup Cartography Project，部分由考夫曼基金会资助）的数据。作者感谢多位学者和机构提供的有益反馈。

---

## 57. 比尔·阿特金森：宝丽来照片展示Lisa GUI的演变 [视频]

**原文标题**: Bill Atkinson: Polaroids Showing the Evolution of the Lisa GUI [video]

**原文链接**: [https://www.youtube.com/watch?v=Qg0mHFcB510](https://www.youtube.com/watch?v=Qg0mHFcB510)

所述文章是一部YouTube视频，标题为“Bill Atkinson：展示Lisa GUI演变的宝丽来照片”。下方列出的内容是标准的YouTube样板文字，涉及版权、联系方式、广告、开发者信息、服务条款、隐私政策、安全以及关于YouTube运作方式的常规信息。

因此，关键信息是：

*   该文章是一部YouTube视频。
*   该视频以Bill Atkinson为主角。
*   该视频的主题是关于Lisa GUI（图形用户界面）的演变。
*   该视频使用宝丽来照片作为媒介来展示这种演变。

该视频很可能通过展示开发过程中拍摄的宝丽来照片，直观地展示Lisa GUI如何随着时间的推移而变化和改进。它可能包含Lisa项目中的关键人物Bill Atkinson关于设计决策和所面临挑战的见解。

---

## 58. 我做了一个历史时间轴，用来了解同时期发生的事件。

**原文标题**: I made a history timeline to learn what events happened around the same time

**原文链接**: [https://seanhollen.com/1300-2000/](https://seanhollen.com/1300-2000/)

本文描述了一个互动式历史时间轴，其时间跨度从公元1300年至2000年。其目的是可视化历史事件，并允许用户探索不同时期同时发生的事件。该时间轴作为一个学习工具，使用户能够理解历史事件的相互关联性，并获得对特定时代的更广阔视角。通过并排显示事件，该时间轴使用户能够看到在孤立地研究事件时可能错过的关系和模式。本质上，它提供了一种动态且引人入胜的方式来学习历史，方法是将事件置于更广阔的历史背景中。

---

## 59. 实用代码生成中的LLM幻觉

**原文标题**: LLM Hallucinations in Practical Code Generation

**原文链接**: [https://dl.acm.org/doi/10.1145/3728894](https://dl.acm.org/doi/10.1145/3728894)

无法访问文章链接。

---

## 60. 深入兔子洞：Bash、OverlayFS 和一个 30 年的惊喜

**原文标题**: Deep Down the Rabbit Hole: Bash, OverlayFS, and a 30-Year-Old Surprise

**原文链接**: [https://sigma-star.at/blog/2025/06/deep-down-the-rabbit-hole-bash-overlayfs-and-a-30-year-old-surprise/](https://sigma-star.at/blog/2025/06/deep-down-the-rabbit-hole-bash-overlayfs-and-a-30-year-old-surprise/)

Bash、OverlayFS 与 30 年前的代码疏忽：一次复杂的调试之旅

该博文详细描述了一次复杂的调试过程，涉及 Bash、OverlayFS 和一个 30 年前的代码疏忽。起初，客户切换到 OverlayFS 后，`scp` 命令失败，并显示“不适合设备的 ioctl”错误。最终发现，该错误源于 Bash 无法确定当前工作目录。

调查显示，由于交叉编译环境配置错误，Bash 使用了自身古老的 `getcwd()` 实现，而非 glibc 版本。这种回退机制原本是为了缺少 `getcwd()` 系统调用的系统而设计的，但交叉编译导致构建过程错误地定义了 `GETCWD_BROKEN`，从而触发了它的使用。

回退的 `getcwd()` 依赖于比较从 `stat(".")` 和 `readdir("..")` 获取的 inode 号码来重建路径。OverlayFS，尤其是在 32 位系统上，无法保证这些 inode 号码匹配，从而打破了 Bash 的假设。OverlayFS 优先考虑快速目录列表，只有 stat() 提供完全稳定的 inode。

此外，调查还暴露了 Bash 的 `getcwd()` 实现中一个存在了几十年的 bug。它在调用 `readdir()` 后未能正确检查 `errno`，导致错误的错误报告，有时会导致误导性的 ENOTTY 错误。

通过在构建过程中显式设置 `bash_cv_getcwd_malloc=yes`，强制 Bash 使用 glibc 版本的 `getcwd()`，问题得以解决。本次调查突出了可移植性、遗留代码和文件系统交互的复杂性，尤其是在 OverlayFS 和 32 位系统上下文中。

---

## 61. Blender 5.0：引入Vulkan和Wayland对Linux的HDR支持

**原文标题**: Blender 5.0 Introducing HDR Support on Linux with Vulkan and Wayland

**原文链接**: [https://www.phoronix.com/news/Blender-5.0-HDR-Linux-Wayland](https://www.phoronix.com/news/Blender-5.0-HDR-Linux-Wayland)

Blender 5.0 将在 Linux 上引入实验性 HDR (高动态范围) 显示支持，特别是在使用 Wayland 和 Vulkan 图形加速时。此功能目前仅限于 Wayland 桌面，暂无计划支持 X11。

由于目前测试有限，HDR 实现被认为是实验性的。启用它需要 HDR 显示器、Wayland 桌面环境、Vulkan API 加速，以及在 Blender 5.0 中启用实验性功能。

在 Ubuntu Linux 上使用 Blender 5.0 alpha 版本，搭配 Samsung Odyssey OLED G8 G81SF 和 ASUS ROG Swift OLED PG27UCDM 显示器的初步测试显示出令人满意的结果。

我们鼓励有兴趣测试此功能的用户在 Blender DevTalk 论坛上提供反馈，以帮助确定 HDR 支持是否会在最终的 Blender 5.0 版本中超出实验阶段。

---

## 62. 关于外星智能的一些思考

**原文标题**: A Few Thoughts on Extraterrestrial Intelligence

**原文链接**: [https://www.rxjourney.net/a-few-thoughts-on-extraterrestrial-intelligence](https://www.rxjourney.net/a-few-thoughts-on-extraterrestrial-intelligence)

关于地外文明的一些思考

本文题为《关于地外文明的一些思考》，探讨了外星生命这种引人入胜的可能性，以及这种发现可能带来的潜在影响。作者用 10 世纪人类遇到现代科技的类比，来说明一个高度发达的外星文明可能被视为神一般。他强调了这句话：“任何足够先进的文明都与魔法无异。”

文章挑战了科幻作品中对外星人的常见描述，认为由于其他星球上存在着截然不同的进化压力，外星生命形式不太可能与人类相似。文章引用了地球自身多样化生态系统中的专业适应性案例，例如深海生物和蝙蝠，来说明环境因素如何塑造生物学。

作者还提出了关于人类与外星人相遇时潜在冲突的警示，并与技术先进的人类剥削技术落后人群的历史实例进行类比。这引出了对接触潜在危险的思考。

文章以亚瑟·克拉克的名言“存在两种可能性：要么我们是宇宙中唯一的生命，要么不是。两种可能性都同样可怕”作为结尾，概括了地外文明问题深刻而不稳定的本质。作者邀请读者捐款以支持未来的内容创作。

---

## 63. 将 JSON 反射到 C++ 对象

**原文标题**: Reflecting JSON into C++ Objects

**原文链接**: [https://brevzin.github.io/c++/2025/06/26/json-reflection/](https://brevzin.github.io/c++/2025/06/26/json-reflection/)

本文阐述了如何利用 C++26 的反射特性在编译时将 JSON 文件转换为 C++ 对象。作者逐步讲解了构建 `json_to_object` 函数的过程，该函数接收一个 JSON 文件，并生成一个 C++ 结构体，其字段对应于 JSON 的键和值。

解释从一个简化的场景开始：解析一个具有单个键和一个整数值的 JSON 对象。步骤包括：反射数据成员规范 (`data_member_spec`)，使用 `define_aggregate` 创建一个结构体类型，以及使用 `substitute` 来特化模板类型。

然后，本文扩展了解决方案以处理多个键/值对，将成员和初始化器存储在向量中。最后，它解决了通用的 JSON 对象解析问题，使用递归处理不同的值类型（数字、字符串和嵌套对象）。特别关注了使用 `std::meta::reflect_constant_string` 处理字符串字面量。

本文依赖于 Boost.JSON 的假设性 `constexpr` 支持来说明 JSON 解析逻辑。最终代码利用 C++26 反射来创建类似类型提供程序的功能，从而能够在编译时将 JSON 数据直接转换为 C++ 对象。文章还展示了使用 UDLs 将反射与字符串字面量结合使用的方法。

---

## 64. Anthropic 在 AI 合理使用方面获胜，但盗窃书籍一事仍陷困境

**原文标题**: Anthropic wins fair use victory for AI – but still in trouble for stealing books

**原文链接**: [https://simonwillison.net/2025/Jun/24/anthropic-training/](https://simonwillison.net/2025/Jun/24/anthropic-training/)

在人工智能行业的一项重要法律进展中，Anthropic在版权侵权诉讼中取得部分胜利。法官威廉·阿尔苏普发布了一项简易判决，认为Anthropic购买和扫描数百万本印刷书籍用于人工智能训练的做法属于“合理使用”，因为扫描版本具有转化性，且未对外分发。

然而，该判决也强调了Anthropic早期从Books3、LibGen和PiLiMi等来源下载数百万未经授权的电子书以构建其最初“研究图书馆”的做法。法官裁定，这种使用盗版材料的行为不构成合理使用，为确定后果的陪审团审判奠定了基础。

核心辩论围绕着在未经许可的数据上训练大型语言模型（LLMs）是否符合“合理使用”。法官在这一点上支持Anthropic，认为阅读和学习文本（即使是有版权的文本）是创作新作品的基础，施加限制将是“不可想象的”。该裁决的这一方面为人工智能行业对训练数据的依赖性树立了重要的先例。

文章还指出，Anthropic已转变为购买和扫描书籍以避免法律问题，并聘请了一位前谷歌图书扫描专家来获取“世界上所有的书籍”。法官威廉·阿尔苏普被描述为一个有趣的人物，具有编程经验，以积极参与与科技相关的法律案件而闻名。

---

## 65. 哈希碰撞的概率 (2022)

**原文标题**: The probability of a hash collision (2022)

**原文链接**: [https://kevingal.com/blog/collisions.html](https://kevingal.com/blog/collisions.html)

本文探讨了哈希冲突的概率，即哈希函数将相同的值分配给不同的输入的情况。作者用“生日悖论”作比喻，强调随着哈希项目数量的增加，冲突概率会以惊人的速度增长。

文章提出了四种计算该概率的方法：精确计算，它对于大型数据集而言计算量很大，以及三种近似方法。第一种近似方法，利用1-x ≈ e^-x （当x很小时）推导得出，在保证良好准确性的前提下，显著提高了速度，尤其是在N（可能的哈希值的数量）很大的情况下。文章进一步推导了近似公式，将其简化为k(k-1)/2N，然后简化为k^2/2N，其中k是被哈希项目的数量。

对这些近似方法的比较表明，指数近似法是最稳健的，而更简单的近似方法仅在较小的k值下可靠。作者在附录中提供了证明，以证明这些近似方法的有效性。最后，文章建议使用哈希冲突计算器，并强调了在数据库和数据存储等应用中最小化冲突概率的重要性。

---

## 66. How Cloudflare blocked a monumental 7.3 Tbps DDoS attack

**原文标题**: How Cloudflare blocked a monumental 7.3 Tbps DDoS attack

**原文链接**: [https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/)

In mid-May 2025, Cloudflare successfully blocked a record-breaking 7.3 Tbps DDoS attack targeting a hosting provider using Magic Transit. This massive attack, delivered 37.4 terabytes of data in just 45 seconds, originating from over 122,000 IP addresses across 161 countries. The attack primarily utilized UDP floods, but also included QOTD, Echo, NTP, Mirai UDP, Portmap, and RIPv1 reflection and amplification attacks.

Cloudflare's globally distributed network, leveraging Anycast, routed attack traffic to the closest data centers (477 data centers across 293 locations), mitigating it near the botnet source. The company's autonomous DDoS detection and mitigation systems, powered by the "dosd" heuristic engine, analyze packet samples in real-time to identify suspicious patterns and generate fingerprints for mitigation. These fingerprints are then compiled into eBPF programs to drop malicious packets.

Cloudflare also shares real-time threat intelligence (fingerprint permutations) across servers within data centers and globally, improving mitigation effectiveness. The company offers a free DDoS Botnet Threat Feed for Service Providers to identify and address abusive accounts launching these attacks. The successful mitigation of this massive attack demonstrates the effectiveness of Cloudflare's DDoS protection systems, aligning with their mission to provide free, unmetered DDoS protection and build a better internet.


---

## 67. Reading NFC Passport Chips in Linux

**原文标题**: Reading NFC Passport Chips in Linux

**原文链接**: [https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/)

生成摘要时出错

---

## 68. DeepSpeech Is Discontinued (2020)

**原文标题**: DeepSpeech Is Discontinued (2020)

**原文链接**: [https://github.com/mozilla/DeepSpeech](https://github.com/mozilla/DeepSpeech)

生成摘要时出错

---

## 69. Thnickels

**原文标题**: Thnickels

**原文链接**: [https://thick-coins.net/?_bhlid=8a5736885893b7837e681aa73f890b9805a4673e](https://thick-coins.net/?_bhlid=8a5736885893b7837e681aa73f890b9805a4673e)

生成摘要时出错

---

## 70. Build a Sentence-Level Text-to-Speech Reader in JavaScript

**原文标题**: Build a Sentence-Level Text-to-Speech Reader in JavaScript

**原文链接**: [https://jsdev.space/tts-sentence-reader/](https://jsdev.space/tts-sentence-reader/)

生成摘要时出错

---

## 71. Writing toy software is a joy

**原文标题**: Writing toy software is a joy

**原文链接**: [https://blog.jsbarretto.com/post/software-is-joy](https://blog.jsbarretto.com/post/software-is-joy)

生成摘要时出错

---

## 72. How to Write Compelling Release Announcements

**原文标题**: How to Write Compelling Release Announcements

**原文链接**: [https://refactoringenglish.com/chapters/release-announcements/](https://refactoringenglish.com/chapters/release-announcements/)

生成摘要时出错

---

## 73. The Unbearable Anger of Broken Audio

**原文标题**: The Unbearable Anger of Broken Audio

**原文链接**: [https://arunraghavan.net/2025/06/the-unbearable-anger-of-broken-audio/](https://arunraghavan.net/2025/06/the-unbearable-anger-of-broken-audio/)

生成摘要时出错

---

## 74. Gemini Users: We're Going to Look at Your Texts Whether You Like It or Not

**原文标题**: Gemini Users: We're Going to Look at Your Texts Whether You Like It or Not

**原文链接**: [https://gizmodo.com/google-to-gemini-users-were-going-to-look-at-your-texts-whether-you-like-it-or-not-2000620141](https://gizmodo.com/google-to-gemini-users-were-going-to-look-at-your-texts-whether-you-like-it-or-not-2000620141)

生成摘要时出错

---

## 75. Managing time when time doesn't exist

**原文标题**: Managing time when time doesn't exist

**原文链接**: [https://multiverseemployeehandbook.com/blog/temporal-resources-managing-time-when-time-doesnt-exist/](https://multiverseemployeehandbook.com/blog/temporal-resources-managing-time-when-time-doesnt-exist/)

生成摘要时出错

---

## 76. Fun with uv and PEP 723

**原文标题**: Fun with uv and PEP 723

**原文链接**: [https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723](https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723)

生成摘要时出错

---

## 77. Introducing Qodo Gen CLI: Build and Run Coding Agents Anywhere in the SDLC

**原文标题**: Introducing Qodo Gen CLI: Build and Run Coding Agents Anywhere in the SDLC

**原文链接**: [https://www.qodo.ai/blog/introducing-qodo-gen-cli-build-run-and-automate-agents-anywhere-in-your-sdlc/](https://www.qodo.ai/blog/introducing-qodo-gen-cli-build-run-and-automate-agents-anywhere-in-your-sdlc/)

生成摘要时出错

---

## 78. How to Think About Time in Programming

**原文标题**: How to Think About Time in Programming

**原文链接**: [https://shanrauf.com/archive/how-to-think-about-time-in-programming](https://shanrauf.com/archive/how-to-think-about-time-in-programming)

生成摘要时出错

---

## 79. Switching Pip to Uv in a Dockerized Flask / Django App

**原文标题**: Switching Pip to Uv in a Dockerized Flask / Django App

**原文链接**: [https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app](https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app)

生成摘要时出错

---

## 80. Thoughts on Asunción, Paraguay

**原文标题**: Thoughts on Asunción, Paraguay

**原文链接**: [https://cpsi.media/p/thoughts-on-asuncion-paraguay](https://cpsi.media/p/thoughts-on-asuncion-paraguay)

生成摘要时出错

---

## 81. Restmail – sendmail-compatible CLI for Gmail and outlook

**原文标题**: Restmail – sendmail-compatible CLI for Gmail and outlook

**原文链接**: [https://github.com/tonymet/restmail](https://github.com/tonymet/restmail)

生成摘要时出错

---

## 82. FICO to incorporate buy-now-pay-later loans into credit scores

**原文标题**: FICO to incorporate buy-now-pay-later loans into credit scores

**原文链接**: [https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later](https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later)

生成摘要时出错

---

## 83. Can AI speak the language Japan tried to kill?

**原文标题**: Can AI speak the language Japan tried to kill?

**原文链接**: [https://www.bbc.com/future/article/20250625-can-ai-speak-the-language-japan-tried-to-kill](https://www.bbc.com/future/article/20250625-can-ai-speak-the-language-japan-tried-to-kill)

生成摘要时出错

---

## 84. IBM's Dmitry Krotov wants to crack the 'physics' of memory

**原文标题**: IBM's Dmitry Krotov wants to crack the 'physics' of memory

**原文链接**: [https://research.ibm.com/blog/dmitry-krotov-ai-physics](https://research.ibm.com/blog/dmitry-krotov-ai-physics)

生成摘要时出错

---

## 85. Experience Making a 1-minute AI movie with my 7-year old daughter

**原文标题**: Experience Making a 1-minute AI movie with my 7-year old daughter

**原文链接**: [https://drsandor.net/ai/minecraft/](https://drsandor.net/ai/minecraft/)

生成摘要时出错

---

## 86. Europe's Manhattan Project moment, argues a tech boss

**原文标题**: Europe's Manhattan Project moment, argues a tech boss

**原文链接**: [https://www.economist.com/by-invitation/2025/06/26/this-is-europes-manhattan-project-moment-argues-a-tech-boss](https://www.economist.com/by-invitation/2025/06/26/this-is-europes-manhattan-project-moment-argues-a-tech-boss)

生成摘要时出错

---

## 87. Show HN: Elelem, a tool-calling CLI for Ollama and DeepSeek in C

**原文标题**: Show HN: Elelem, a tool-calling CLI for Ollama and DeepSeek in C

**原文链接**: [https://codeberg.org/politebot/elelem](https://codeberg.org/politebot/elelem)

生成摘要时出错

---

## 88. Building a Monostable Tetrahedron

**原文标题**: Building a Monostable Tetrahedron

**原文链接**: [https://arxiv.org/abs/2506.19244](https://arxiv.org/abs/2506.19244)

生成摘要时出错

---

## 89. Microsoft Edit

**原文标题**: Microsoft Edit

**原文链接**: [https://github.com/microsoft/edit](https://github.com/microsoft/edit)

生成摘要时出错

---

## 90. Deep Research as a Swim Coach

**原文标题**: Deep Research as a Swim Coach

**原文链接**: [https://suthakamal.substack.com/p/swimming-with-an-ai-coach](https://suthakamal.substack.com/p/swimming-with-an-ai-coach)

生成摘要时出错

---

## 91. NLNet: 62 new projects contribute to digital commons

**原文标题**: NLNet: 62 new projects contribute to digital commons

**原文链接**: [https://nlnet.nl/news/2025/20250624-announcement-grants-CommonsFund.html](https://nlnet.nl/news/2025/20250624-announcement-grants-CommonsFund.html)

生成摘要时出错

---

## 92. Show HN: Oasis – An open-source, 3D-printed smart terrarium

**原文标题**: Show HN: Oasis – An open-source, 3D-printed smart terrarium

**原文链接**: [https://github.com/justbuchanan/oasis](https://github.com/justbuchanan/oasis)

生成摘要时出错

---

## 93. Yet another insignificant programming notes

**原文标题**: Yet another insignificant programming notes

**原文链接**: [https://chua.bitbucket.io](https://chua.bitbucket.io)

生成摘要时出错

---

## 94. A Dictionary of the Language of Myst's D'ni

**原文标题**: A Dictionary of the Language of Myst's D'ni

**原文链接**: [http://www.eldalamberon.com/dni_dict.htm](http://www.eldalamberon.com/dni_dict.htm)

生成摘要时出错

---

## 95. Canal Boat Simulator

**原文标题**: Canal Boat Simulator

**原文链接**: [https://jacobfilipp.com/boat/](https://jacobfilipp.com/boat/)

生成摘要时出错

---

## 96. Mixed DPI in X11

**原文标题**: Mixed DPI in X11

**原文链接**: [https://wok.oblomov.eu/tecnologia/mixed-dpi-x11/](https://wok.oblomov.eu/tecnologia/mixed-dpi-x11/)

生成摘要时出错

---

## 97. PlasticList – Plastic Levels in Foods

**原文标题**: PlasticList – Plastic Levels in Foods

**原文链接**: [https://www.plasticlist.org/](https://www.plasticlist.org/)

生成摘要时出错

---

## 98. Web Translator API

**原文标题**: Web Translator API

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/API/Translator](https://developer.mozilla.org/en-US/docs/Web/API/Translator)

生成摘要时出错

---

## 99. ChatGPT's enterprise success against Copilot fuels OpenAI/Microsoft rivalry

**原文标题**: ChatGPT's enterprise success against Copilot fuels OpenAI/Microsoft rivalry

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry](https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry)

生成摘要时出错

---

## 100. Finding a 27-year-old easter egg in the Power Mac G3 ROM

**原文标题**: Finding a 27-year-old easter egg in the Power Mac G3 ROM

**原文链接**: [https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)

Doug Brown details his discovery of a previously undocumented easter egg hidden within the Power Mac G3's ROM (released 1997-1999). While exploring the ROM using Hex Fiend and Eric Harmon's Mac ROM template, he noticed a JPEG image resource of the development team and strings in the SCSI Manager 4.3 code referencing "secret ROM image" and "The Team".

Intrigued, Brown disassembled the SCSI Manager code using Ghidra and traced the usage of these strings. He found that the code checks for a volume named "secret ROM image" associated with the .EDisk driver (RAM disk). If found, it extracts the JPEG image from the ROM and creates a file named "The Team" on that volume.

While Brown initially struggled to activate the easter egg, a user named ^alex in the #mac68k Libera chat helped him figure out the activation method: formatting the RAM disk and naming it "secret ROM image" in the format dialog. This triggers the code to create the "The Team" file containing the hidden JPEG image.

Brown confirmed the easter egg works on real hardware and Infinite Mac emulation, from Mac OS 8.1 up to at least 9.0.4. He believes this easter egg, likely created before Steve Jobs banned them in 1997, was previously unknown despite knowledge of the hidden image's existence. He credits ^alex for their key contribution and invites anyone who was part of "The Team" to share their recollections.


---

