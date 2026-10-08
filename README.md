# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-08.md)

*最后自动更新时间: 2026-10-08 22:22:37*
## 1. Whistle：16.9 MB 语音转文字

**原文标题**: Whistle: Speech to Text in 16.9 MB

**原文链接**: [https://cactuscompute.com/blog/whistle](https://cactuscompute.com/blog/whistle)

**Whistle** 是一款新发布的、高效的语音转文本模型，专为移动设备、穿戴设备、机器人和微控制器上的端侧执行而设计。该模型大小仅为 **16.9 MB**，完全在 CPU 上运行，无需外部依赖，并支持转写、词级时间戳以及语音嵌入。

**关键技术规格：**
*   **性能：** 其运行速度显著优于 Whisper base (145.3 MB) 和 Moonshine tiny v2 等更大型的模型。在 Apple M4 Pro 上，Whistle 的解码速度达到 1,319 tokens/秒，首个 token 延迟仅为 11.1 毫秒。
*   **准确度：** 在 LibriSpeech 和 FLEURS 等基准测试中，其词错误率 (WER) 表现优于竞争对手。
*   **功能：** 支持七种语言（英语、德语、法语、西班牙语、意大利语、荷兰语和波兰语），并具备自动语言检测功能。单次可处理长达 30 秒的 16 kHz 单声道音频。
*   **架构：** Whistle 采用与 "Needle" 模型通用的 C++ 引擎，其特点包括 8 层注意力模块、门控交叉注意力，以及通过 Aho-Corasick 自动机实现的关键词偏置。

**部署与集成：**
该引擎具有极佳的可移植性，为包括 iOS、Android、Linux、macOS 和 WASI 在内的 17 个目标平台提供了预编译的二进制文件。集成过程非常简便，可通过简单的 Python API (`pip install cactus-needle`) 或 C API 完成。一大亮点是它能与 Needle 引擎配合，提供无缝的“语音到工具调用”流水线，直接从音频输入返回结构化的 JSON 结果。

通过优先考虑极小的资源占用和高速本地处理，Whistle 为跨多样化硬件平台的隐私敏感型、低延迟应用提供了强大的解决方案。

---

## 2. 为什么业界没有对 DeepSeek 4.1 Flash 感到震惊？

**原文标题**: Why isn't the industry freaking out about DeepSeek 4.1 Flash?

**原文链接**: [https://www.dgt.is/blog/2026-10-07-deepseek-freek-out/](https://www.dgt.is/blog/2026-10-07-deepseek-freek-out/)

本文探讨了中国大语言模型 DeepSeek 4.1 Flash 的颠覆性影响。作者认为，尽管该模型的性能已足以媲美 Claude Opus 5.5 等“前沿”模型，但却被科技界所忽视。

作者的核心论点是，DeepSeek 4.1 Flash 以低出几个数量级的成本提供了顶级智能，从根本上改变了开发工作流。由于其订阅费用低廉（如每月 10 美元）且基本不限使用次数，开发者现在可以自动化处理那些在其他平台上成本极高的“机械性”或探索性任务。作者指出，在盲测中，该模型与西方顶级模型难分伯仲。

技术上的核心亮点是 DeepSeek 的极高效率。据报道，该模型较其首个版本将 KV 缓存大小缩减了 437 倍。这种“缓存魔术”大幅降低了 GPU 显存需求，使复杂的长周期编程任务仅需极低成本，同时减少了水耗和电耗等环境影响。

作者批评了“前沿实验室”及整个科技行业“贵即是好”的思维定势，认为中国模型正凭借对可持续性和普及化的专注，准备“抢走他们的饭碗”。当行业仍沉溺于高价订阅和大规模硬件竞赛时，作者总结道，DeepSeek 的效率提升代表了 AI 的未来——随着这些优化方案的演进，最终将实现强大且高性价比模型的本地化部署。

---

## 3. 注意缺陷多动障碍作为一种昼夜节律障碍：证据及对时间疗法的启示

**原文标题**: ADHD as a circadian rhythm disorder: evidence and implications for chronotherapy

**原文链接**: [https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1697900/full](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1697900/full)

本文指出，昼夜节律功能障碍是ADHD（注意力缺陷多动障碍）中极为普遍的表型，影响约73–80%的患者。研究表明，这些个体通常表现出以显著生物相位延迟为特征的“晚间表型”。

**关键生物学发现：**
*   **褪黑素：** ADHD患儿的弱光褪黑素分泌起始（DLMO）延迟约45分钟，成年患者则延迟约90分钟。研究还显示患者松果体体积缩小且日间褪黑素水平异常。
*   **皮质醇：** 患者通常表现出晨间皮质醇节律迟钝且延迟。
*   **分子层面：** 核心时钟基因（BMAL1和PER2）的节律减弱，表明分子生物钟存在根本性紊乱。

**临床干预措施：**
作者强调，计时疗法（旨在调整内部生物钟的干预措施）可以改善睡眠和ADHD核心症状。
*   **褪黑素：** 低剂量补充能有效提前睡眠时间，并已被证实可减轻高达14%的ADHD症状。
*   **强光疗法：** 晨间接受强光照射（特别是10,000勒克斯）有助于稳定昼夜节律，尤其是在季节性抑郁容易加重ADHD症状的冬季。
*   **行为转变：** 包括固定起床时间、晨练和晚间光线限制（屏幕卫生）在内的多模态方法，已被证明能有效提前“夜猫子”人群的昼夜节律相位。

**建议的临床路径：**
本文倡导在ADHD护理中采用“行为优先”的方法。这包括常规筛查睡眠障碍、通过睡眠追踪进行表型表征，以及实施规范化的“授时因子”（如光线和运动等环境线索）。

**结论：**
虽然作者并未将ADHD完全重新分类为睡眠障碍，但他们认为昼夜节律表型是该疾病中具有临床意义的重要组成部分。将计时疗法作为标准治疗的一种低风险、可扩展的辅助手段，可以改善患者预后，并推动ADHD治疗向更精准的模式发展。

---

## 4. 不直奔主题的价值 (2015)

**原文标题**: The value of not getting to the point (2015)

**原文链接**: [https://ken.arneson.name/2015/11/the-value-of-not-getting-to-the-point/](https://ken.arneson.name/2015/11/the-value-of-not-getting-to-the-point/)

在《不直奔主题的价值》（The Value of Not Getting to the Point）一文中，肯·阿内森（Ken Arneson）探讨了对话中“废话”所隐藏的社会效用。阿内森曾是一个凡事“直奔主题”的人，但在与读大学的女儿进行了一次漫长的谈话后，他产生了一番感悟：委婉和闲聊并非浪费时间，而是建立信任和情感安全感必不可少的仪式。

阿内森认为，由于语言是不精确的，且表达感受会让人产生脆弱感，人们会将共进晚餐或“闲聊”等仪式作为对话的预热。这些缓冲机制让说话者在触及敏感或令人不快的话题之前，能够应对自身情感的复杂性，并营造出一个安全的环境。他指出，虽然大多数人直觉上都明白这一点，但其重要性却很少被明确表述。

这一见解也构成了对现代数字通信（尤其是 Twitter）的批判。阿内森指出，该平台的字数限制迫使用户直截了当，从而剥离了面对面交流中存在的保护性仪式。由于缺乏“对话之舞”或“轻抿咖啡”的缓冲空间，言语中固有的脆弱性被暴露无遗，导致了网络空间中常见的摩擦和误解。

最终，阿内森得出结论，明确阐述人性的这些直觉层面具有重要价值。他承认自己过去在社交直觉方面表现得“笨拙”，并致力于探索和解释这些“显而易见”的真理，以便更好地理解人际关系的运作机制。这篇文章本身就是对他观点的一种“元演示”，因为他特意采取了迂回的方式来引出结论。

---

## 5. 希拉洛斯世界

**原文标题**: Theranos.world

**原文链接**: [https://www.theranos.world/](https://www.theranos.world/)

**Theranos.world** 似乎是一个互动数字模拟或艺术装置，它重现了已倒闭的血液检测初创公司 Theranos 那位声名狼藉的创始人伊丽莎白·霍姆斯（Elizabeth Holmes）的虚拟及实体办公空间。

其界面模拟了经典的 macOS 桌面环境，配有标准的菜单栏（访达、文件、编辑）以及 Keynote 和电子表格等办公应用。登录界面明确将用户身份识别为“伊丽莎白·霍姆斯”，并包含一个显著的设计选择：无需密码即可进入，这或许象征着该公司缺乏透明度或监管。

除了二维桌面，该项目还包含 3D 或沉浸式元素。它提供了诸如“点击椅子坐下”、“拖动查看”和“捏合缩放”等操作指令。这些元素表明，该项目是对 Theranos 事件的一种元评论，让用户能够虚拟地置身于霍姆斯的环境中，并与她用来构建公司叙事的工具进行互动。

---

## 6. 面向AI的生物数据：18亿美元全球承诺

**原文标题**: AI-ready biological data: $1.8B global commitment

**原文链接**: [https://biohub.org/news/virtual-biology-initiative-expansion/](https://biohub.org/news/virtual-biology-initiative-expansion/)

2026年10月7日，一项重大的国际合作宣布投入18亿美元用于生成“AI就绪”（AI-ready）的生物数据，标志着该领域迄今为止规模最大的协同行动。该倡议由Biohub、美国能源部（DOE）和美国国家卫生研究院（NIH）牵头，谷歌DeepMind、Isomorphic Labs和Meta等科技巨头共同参与，旨在构建基础的开放获取数据集，为生物学预测AI模型提供动力。

其核心目标是创建一个“虚拟细胞”——一种允许科学家进行数字化实验的模型。通过模拟细胞的运作方式及其对干预措施的反应，研究人员希望大幅加速对人类疾病的理解、预防和治疗。

资金分配涵盖以下几个关键支柱：
* **美国能源部（5亿多美元）：** 投资于整个国家实验室系统的百亿亿次级（Exascale）超算、自主实验室和先进成像技术。
* **美国国家卫生研究院（5亿多美元）：** 协调现有生物医学存储库和知识库的标准化，使其具备AI兼容性。
* **Biohub（5亿美元）：** 通过开发新型测量技术（包括冷冻电子断层扫描和大规模显微技术）来解析近原子级的细胞细节，为该计划提供核心支持。
* **科技合作伙伴（3亿美元）：** 谷歌DeepMind、Isomorphic Labs和Meta正在资助“虚拟生物学倡议”，以创建多模态数据集和预测建模工具。

这一跨部门合作伙伴关系强调“开放科学”，通过建立共享标准和通用标识符，确保全球科学界能够访问并利用这些资源。通过将生物学从实验室工作台转向数字模拟，该倡议力求为生物技术设定新标准，并显著缩短医学突破的周期。

---

## 7. I hired an illustrator to draw my house. Now it's my Home Assistant dashboard

**原文标题**: I hired an illustrator to draw my house. Now it's my Home Assistant dashboard

**原文链接**: [https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my](https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my)

生成摘要时出错

---

## 8. A Terminal Protocol for Program Status (OSC 7501)

**原文标题**: A Terminal Protocol for Program Status (OSC 7501)

**原文链接**: [https://mitchellh.com/writing/program-status-osc7501](https://mitchellh.com/writing/program-status-osc7501)

生成摘要时出错

---

## 9. Man discovers his parents' coffee machine used 1TB of data in 10 days

**原文标题**: Man discovers his parents' coffee machine used 1TB of data in 10 days

**原文链接**: [https://www.dexerto.com/entertainment/man-discovers-his-parents-coffee-machine-used-1tb-of-data-in-10-days-3416399/](https://www.dexerto.com/entertainment/man-discovers-his-parents-coffee-machine-used-1tb-of-data-in-10-days-3416399/)

生成摘要时出错

---

## 10. Yes, and

**原文标题**: Yes, and

**原文链接**: [https://htmx.org/essays/yes-and/](https://htmx.org/essays/yes-and/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 2 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 3 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 4 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 5 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 6 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 7 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 8 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 9 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 10 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 11 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 12 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 13 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 14 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 15 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 16 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 17 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 18 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 19 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 20 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 21 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 22 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 23 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 24 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 25 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 26 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 27 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 28 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 29 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 30 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 31 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 32 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 33 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 34 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 35 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 36 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 37 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 38 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 39 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 40 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 41 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 42 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 43 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 44 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 45 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 46 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 47 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 48 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 49 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 50 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 51 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 52 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 53 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 54 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 55 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 56 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 57 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 58 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 59 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 60 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 61 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 62 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 63 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 64 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 65 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 66 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 67 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 68 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 69 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 70 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 71 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 72 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 73 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 74 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 75 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 76 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 77 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 78 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 79 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 80 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 81 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 82 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 83 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 84 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 85 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 86 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 87 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 88 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 89 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 90 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 91 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 92 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 93 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 94 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 95 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 96 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 97 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 98 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 99 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 100 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 101 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 102 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 103 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 104 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 105 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 106 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 107 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 108 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 109 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 110 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 111 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 112 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 113 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 114 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 115 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 116 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 117 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 118 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 119 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 120 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 121 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 122 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 123 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 124 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 125 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 126 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 127 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 128 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 129 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 130 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 131 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 132 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 133 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 134 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 135 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 136 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 137 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 138 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 139 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 140 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 141 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 142 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 143 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 144 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 145 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 146 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 147 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 148 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 149 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 150 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 151 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 152 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 153 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 154 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 155 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 156 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 157 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 158 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 159 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 160 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 161 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 162 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 163 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 164 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 165 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 166 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 167 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 168 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 169 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 170 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 171 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 172 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 173 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 174 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 175 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 176 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 177 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 178 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 179 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 180 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 181 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 182 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 183 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 184 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 185 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 186 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 187 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 188 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 189 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 190 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 191 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 192 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 193 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 194 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 195 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 196 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 197 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 198 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 199 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 200 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 201 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 202 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 203 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 204 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 205 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 206 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 207 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 208 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 209 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 210 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 211 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 212 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 213 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 214 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 215 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 216 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 217 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 218 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 219 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 220 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 221 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 222 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 223 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 224 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 225 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 226 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 227 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 228 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 229 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 230 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 231 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 232 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 233 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 234 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 235 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 236 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 237 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 238 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 239 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 240 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 241 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 242 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 243 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 244 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 245 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 246 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 247 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 248 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 249 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 250 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 251 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 252 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 253 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 254 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 255 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 256 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 257 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 258 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 259 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 260 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 261 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 262 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 263 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 264 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 265 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 266 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 267 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 268 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 269 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 270 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 271 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 272 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 273 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 274 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 275 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 276 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 277 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 278 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 279 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 280 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 281 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 282 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 283 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 284 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 285 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 286 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 287 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 288 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 289 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 290 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 291 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 292 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 293 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 294 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 295 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 296 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 297 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 298 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 299 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 300 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 301 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 302 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 303 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 304 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 305 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 306 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 307 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 308 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 309 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 310 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 311 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 312 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 313 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 314 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 315 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 316 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 317 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 318 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 319 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 320 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 321 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 322 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 323 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 324 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 325 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 326 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 327 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 328 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 329 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 330 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 331 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 332 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 333 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 334 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 335 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 336 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 337 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 338 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 339 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 340 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 341 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 342 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 343 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 344 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 345 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 346 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 347 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 348 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 349 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 350 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 351 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 352 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 353 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 354 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 355 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 356 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 357 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 358 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 359 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 360 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 361 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 362 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 363 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 364 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 365 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 366 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 367 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 368 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 369 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 370 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 371 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 372 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 373 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 374 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 375 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 376 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 377 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 378 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 379 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 380 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 381 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 382 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 383 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 384 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 385 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 386 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 387 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 388 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 389 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 390 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 391 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 392 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 393 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 394 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 395 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 396 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 397 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 398 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 399 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 400 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 401 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 402 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 403 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 404 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 405 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 406 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 407 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 408 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 409 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 410 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 411 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 412 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 413 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 414 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 415 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 416 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 417 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 418 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 419 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 420 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 421 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 422 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 423 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 424 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 425 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 426 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 427 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 428 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 429 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 430 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 431 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 432 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 433 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 434 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 435 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 436 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 437 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 438 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 439 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 440 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 441 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 442 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 443 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 444 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 445 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 446 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 447 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 448 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 449 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 450 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 451 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 452 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 453 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 454 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 455 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 456 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 457 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 458 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 459 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 460 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 461 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 462 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 463 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 464 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 465 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 466 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 467 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 468 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 469 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 470 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 471 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 472 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 473 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 474 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 475 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 476 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 477 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 478 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 479 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 480 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 481 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 482 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 483 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 484 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 485 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 486 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 487 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 488 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 489 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 490 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 491 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 492 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 493 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 494 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 495 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 496 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 497 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 498 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 499 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 500 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 501 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 502 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 503 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 504 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 505 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 506 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 507 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 508 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 509 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 510 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 511 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 512 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 513 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 514 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 515 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 516 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 517 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 518 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 519 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 520 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 521 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 522 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 523 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 524 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 525 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 526 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 527 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 528 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 529 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 530 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 531 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 532 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 533 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 534 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 535 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 536 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 537 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 538 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 539 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 540 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 541 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 542 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 543 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 544 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 545 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 546 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 547 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 548 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 549 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 550 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 551 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 552 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 553 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 554 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 555 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 556 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 557 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 558 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 559 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 560 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 561 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 562 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 563 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 564 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 565 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
