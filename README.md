# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-02.md)

*最后自动更新时间: 2025-12-02 17:55:25*
## 1. 使用Strudel学习音乐

**原文标题**: Learning Music with Strudel

**原文链接**: [https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92](https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92)

题为“用Strudel学习音乐”的文章似乎是关于在Notion中使用Strudel进行音乐教育的。然而，提供的内容非常有限，仅包含一条指示使用Notion需要JavaScript的消息。

因此，无法确定Strudel如何用于学习音乐的具体细节。唯一的结论是，这篇文章可能讨论了如何在Notion中实施一个名为“Strudel”的工具来帮助音乐教育，但要访问描述其功能的实际内容，需要在Notion环境中启用JavaScript。我们没有任何关于Strudel*是什么*或*如何*促进音乐学习的细节。

---

## 2. Mistral 3 模型系列发布

**原文标题**: Mistral 3 family of models released

**原文链接**: [https://mistral.ai/news/mistral-3](https://mistral.ai/news/mistral-3)

Mistral AI发布新一代模型Mistral 3系列，采用Apache 2.0许可。其中包括：

*   **Mistral Large 3:** 一款最先进的开放权重稀疏混合专家模型（410亿活跃参数，6750亿总参数），在NVIDIA H200 GPU上训练而成。它擅长通用提示、图像理解和多语言对话。提供基础版本和指令微调版本。
*   **Ministral 3系列:** 三款小型密集模型（30亿、80亿和140亿参数），适用于边缘和本地用例，每款均有基础版、指令版和推理版，均具备图像理解能力。它们旨在实现最佳的性能成本比。

这些模型通过与vLLM、Red Hat和NVIDIA的合作进行了优化，以提高可访问性和速度，包括NVFP4检查点和在NVIDIA硬件上高效的推理支持。

Mistral Large 3在LMArena排行榜上名列前茅。Ministral 3系列为各种需求（包括边缘部署）提供量身定制的选择，并具有最先进的准确性。

这些模型可在Mistral AI Studio、Amazon Bedrock、Azure Foundry和Hugging Face等多个平台上使用。Mistral AI还提供定制模型训练服务。

Mistral AI强调开放访问、透明度和协作，邀请社区探索和构建新的模型。

---

## 3. Nixtml：用Nix编写的静态网站和博客生成器

**原文标题**: Nixtml: Static website and blog generator written in Nix

**原文链接**: [https://github.com/arnarg/nixtml](https://github.com/arnarg/nixtml)

Nixtml 是一个用 Nix 编写的静态网站和博客生成器，灵感来源于 Hugo。它使用 Nix 来定义网站结构、内容处理和主题。

**主要特性：**

*   **Nix 驱动：** 利用 Nix 实现可复现性和声明式配置。
*   **Markdown 内容：** 将 Markdown 文件转换为 HTML 页面。
*   **模板：** 使用 Nix 函数作为 HTML 模板，支持函数式 HTML 和字符串模板。标准模板包括 `base`、`hom`、`page`、`collection`、`taxonomy` 和 `partials` 用于自定义。
*   **集合（Collections）：** 对内容进行分组和分页，例如博客文章，并生成 RSS 订阅。
*   **分类（Taxonomies）：** 通过关键词（标签、类别）组织内容，为每个术语创建专用页面。
*   **灵活性：** 提供用于常见 HTML 标签的函数，以实现 HTML 的程序化构建。
*   **示例：** 提供简单网站和博客的示例配置。

**工作流程：**

1.  `flake.nix` 文件定义网站结构、依赖项（包括 `nixtml`）和构建过程。
2.  内容放置在指定的目录 (`content.dir`) 中。
3.  配置集合和分类以对内容进行分组和分类。
4.  模板定义网站的布局和样式。
5.  Nixtml 处理内容和模板，生成可以部署的静态网站。

该框架通过 Nix 驱动的自动化实现网站创建，在主题、内容组织和整体网站结构方面提供灵活性。

---

## 4. 解决添加问题

**原文标题**: Addressing the adding situation

**原文链接**: [https://xania.org/202512/02-adding-integers](https://xania.org/202512/02-adding-integers)

应对加法困境：编译器如何利用x86指令实现三操作数加法

---

## 5. 注意通知

**原文标题**: YesNotice

**原文链接**: [https://infinitedigits.co/docs/software/yesnotice/](https://infinitedigits.co/docs/software/yesnotice/)

YesNotice，于2025年10月10日上线，是一个旨在通知用户所追踪事项从否定（“否”）状态变为肯定（“是”）状态的网站。它被归类为软件和投资组合相关。YesNotice的核心功能是主动提醒，在特定条件或状态朝着有利于用户的方向转变时立即通知用户。本质上，它自动化了监控积极变化的过程，无需进行持续的手动检查。

---

## 6. 2025编译器优化前沿

**原文标题**: Advent of Compiler Optimisations 2025

**原文链接**: [https://xania.org/202511/advent-of-compiler-optimisation](https://xania.org/202511/advent-of-compiler-optimisation)

作者宣布推出“2025编译器优化降临”活动，这是一个从12月1日到12月25日每日更新的项目。每天将发布一篇博文和一个视频，详细介绍一种不同的C或C++编译器优化。内容将涵盖底层、特定于架构的技巧和高层优化，主要侧重于x86-64，但也涉及64位和32位ARM。作者将解释每种优化何时适用、如何解释生成的汇编代码以及何时可能不适用。该项目旨在展示现代编译器令人惊叹的功能。读者可以通过AoCO2025博客标签、YouTube订阅或专门的YouTube播放列表来关注。

---

## 7. Poka Labs (YC S24) 招聘创始工程师

**原文标题**: Poka Labs (YC S24) Is Hiring a Founding Engineer

**原文链接**: [https://www.ycombinator.com/companies/poka-labs/jobs/RCQgmqB-founding-engineer](https://www.ycombinator.com/companies/poka-labs/jobs/RCQgmqB-founding-engineer)

Poka Labs（Y Combinator S24孵化企业）正在招募创始工程师，为亟待数字化和人工智能转型的6万亿美元化工制造业构建“智能层”。该职位年薪13万至18万美元，股权1-3%，要求搬迁至旧金山。

创始工程师将负责处理模糊的问题领域，交付制造企业各团队每日使用的生产级人工智能代理。职责包括构建端到端代理，用于报价、定价和库存管理，集成ERP和CRM系统，并塑造产品体验。该职位涉及前端和后端功能开发，确保代理的可靠性，以及评估新的人工智能能力。

Poka Labs正在寻找具备强大的全栈能力、行动导向、清晰的沟通技巧和快速学习能力的人才。其技术栈包括现代LLM、TypeScript、React和AWS。公司提供重要的所有权、在全球制造业的影响力、塑造企业文化的机会，以及与创始人直接合作的机会。面试流程包括初步沟通、居家技术评估和带薪工作试用。Poka Labs成立于2023年，目前团队有3人。

---

## 8. 我设计并打印了一个定制的鼻罩来帮助我的狗对抗DLE。

**原文标题**: I Designed and Printed a Custom Nose Guard to Help My Dog with DLE

**原文链接**: [https://snoutcover.com/billie-story](https://snoutcover.com/billie-story)

比利，一只比特犬，被诊断患有盘状红斑狼疮(DLE)，导致她的鼻子出现色素脱失、结痂、疼痛和出血，阳光会加剧病情。传统的治疗方法，如药用软膏和防晒霜，都无效，因为比利会把它们舔掉。现有的鼻子防护罩也都不成功。

出于绝望并配备了3D打印机，比利的主人设计了SnoutCover，一个定制的鼻子防护罩。设计过程涉及多次迭代，最初使用PLA进行测量，然后过渡到柔软的TPU以提高舒适度。早期的原型缺乏通风，导致不适。随后的版本专注于增加战略性的通风孔，同时阻挡紫外线。

经过13次迭代，最终的SnoutCover设计保护了比利的鼻子免受阳光照射，让她能够正常呼吸和进食，防止她舔掉药物，并舒适地固定到位。使用SnoutCover五个月后，比利的出血停止，结痂减少，色素恢复，她的鼻子完全痊愈。

在网上分享比利的成功案例后，收到了来自其他面临类似挑战的狗主人的热烈反响。主人现在在MakerWorld上免费分享SnoutCover设计，希望帮助其他患有DLE的狗狗过上无痛且健康的生活。该设计适用于中大型犬，可以通过切片软件中的缩放进行调整。

---

## 9. Python数据科学手册

**原文标题**: Python Data Science Handbook

**原文链接**: [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)

Jake VanderPlas 编写的《Python数据科学手册》是使用 Python 学习数据科学的全面资源。完整文本可以作为 Jupyter 笔记本在 GitHub 上在线获取，采用 CC-BY-NC-ND 许可（文本）和 MIT 许可（代码）。该手册鼓励用户通过购买本书来支持这项工作。

本书涵盖了广泛的主题，首先深入探讨了 IPython，包括其帮助、快捷方式、魔法命令、历史记录、 shell 命令、调试、性能分析等功能。然后深入研究 NumPy，解释了数据类型、数组、通用函数、聚合、广播、比较、索引、排序和结构化数据。

该手册继续介绍 Pandas，重点介绍使用 Pandas 对象进行数据操作、索引、运算、处理缺失数据、分层索引、组合数据集（concat、merge、join）、聚合、分组、透视表、向量化字符串操作、时间序列以及使用 `eval()` 和 `query()` 的高性能技术。

接下来，它探讨了使用 Matplotlib 进行数据可视化，涵盖各种绘图类型（折线图、散点图、轮廓图、直方图），绘图元素的自定义（图例、颜色条、子图、文本、注释、刻度线）、样式表、3D 绘图、使用 Basemap 的地理数据，并介绍了 Seaborn。

最后，本书涵盖了使用 Scikit-Learn 进行的机器学习，包括模型验证、特征工程等主题，并深入分析了朴素贝叶斯、线性回归、支持向量机、决策树、随机森林、主成分分析、流形学习、k-Means 聚类、高斯混合模型和核密度估计等算法。最后以人脸检测的应用和进一步的机器学习资源作为结束。

---

## 10. Show HN: Marmot - 单一二进制数据目录 (无需 Kafka, 无需 Elasticsearch)

**原文标题**: Show HN: Marmot – Single-binary data catalog (no Kafka, no Elasticsearch)

**原文链接**: [https://github.com/marmotdata/marmot](https://github.com/marmotdata/marmot)

Marmot 是一个开源的单二进制数据目录，旨在简化组织机构整个数据栈中的数据发现。它旨在提供强大的搜索能力，而无需传统企业解决方案的复杂性，也不需要 Kafka 或 Elasticsearch。

主要特点包括：

*   **易于部署：** Marmot 可以使用单个二进制文件、Docker 或 Kubernetes 快速部署，只需最少的设置。
*   **强大的搜索：** 提供丰富的查询语言，包括全文搜索、元数据过滤、布尔逻辑和比较运算符，以查找任何数据资产。
*   **交互式血缘可视化：** 提供交互式依赖关系图，以跟踪数据流并理解数据血缘。
*   **灵活的集成：** 支持 CLI、REST API、Terraform 和 Pulumi 进行资产编目。
*   **元数据优先架构：** 存储各种资产类型的丰富元数据。
*   **团队协作：** 允许分配所有权、记录业务背景以及创建术语表，以实现集中式数据知识管理。

Marmot 根据 MIT 许可证获得许可，并欢迎以错误报告、功能建议、文档改进和插件开发的形式进行贡献。新用户可使用快速入门指南和在线演示。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 2 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 3 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 4 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 5 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 6 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 7 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 8 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 9 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 10 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 11 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 12 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 13 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 14 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 15 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 16 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 17 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 18 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 19 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 20 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 21 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 22 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 23 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 24 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 25 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 26 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 27 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 28 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 29 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 30 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 31 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 32 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 33 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 34 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 35 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 36 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 37 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 38 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 39 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 40 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 41 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 42 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 43 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 44 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 45 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 46 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 47 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 48 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 49 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 50 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 51 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 52 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 53 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 54 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 55 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 56 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 57 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 58 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 59 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 60 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 61 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 62 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 63 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 64 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 65 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 66 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 67 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 68 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 69 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 70 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 71 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 72 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 73 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 74 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 75 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 76 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 77 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 78 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 79 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 80 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 81 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 82 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 83 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 84 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 85 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 86 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 87 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 88 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 89 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 90 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 91 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 92 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 93 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 94 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 95 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 96 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 97 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 98 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 99 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 100 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 101 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 102 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 103 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 104 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 105 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 106 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 107 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 108 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 109 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 110 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 111 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 112 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 113 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 114 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 115 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 116 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 117 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 118 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 119 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 120 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 121 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 122 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 123 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 124 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 125 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 126 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 127 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 128 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 129 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 130 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 131 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 132 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 133 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 134 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 135 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 136 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 137 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 138 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 139 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 140 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 141 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 142 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 143 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 144 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 145 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 146 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 147 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 148 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 149 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 150 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 151 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 152 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 153 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 154 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 155 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 156 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 157 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 158 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 159 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 160 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 161 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 162 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 163 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 164 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 165 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 166 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 167 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 168 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 169 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 170 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 171 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 172 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 173 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 174 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 175 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 176 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 177 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 178 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 179 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 180 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 181 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 182 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 183 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 184 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 185 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 186 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 187 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 188 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 189 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 190 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 191 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 192 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 193 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 194 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 195 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 196 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 197 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 198 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 199 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 200 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 201 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 202 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 203 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 204 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 205 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 206 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 207 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 208 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 209 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 210 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 211 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 212 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 213 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 214 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 215 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 216 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 217 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 218 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 219 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 220 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 221 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 222 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 223 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 224 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 225 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 226 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 227 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 228 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 229 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 230 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 231 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 232 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 233 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 234 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 235 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 236 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 237 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 238 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 239 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 240 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 241 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 242 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 243 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 244 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 245 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 246 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 247 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 248 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 249 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 250 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 251 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 252 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 253 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 254 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 255 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 256 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 257 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
