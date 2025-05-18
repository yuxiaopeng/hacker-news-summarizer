# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-18.md)

*最后自动更新时间: 2025-05-18 17:46:12*
## 1. Show HN: 我用SBERT对伏尼契手稿建模，以测试其结构

**原文标题**: Show HN: I modeled the Voynich Manuscript with SBERT to test for structure

**原文链接**: [https://github.com/brianmg/voynich-nlp-analysis](https://github.com/brianmg/voynich-nlp-analysis)

该“Show HN”帖子详细介绍了一个计算语言学项目，该项目分析了伏尼契手稿，重点关注结构特性而非翻译尝试。作者使用SBERT嵌入和聚类来对手稿的结构进行建模，旨在确定它是否表现出类似语言的行为，尽管它尚未被解读。

一个关键的预处理步骤包括从单词中剥离重复出现的“类似后缀”的结尾，以分离潜在的词根形式。然后，该项目使用这些剥离后的词根进行SBERT聚类，推断词性（POS），建立马尔可夫转移模型，并构建词典假设。分析表明，手稿确实具有重要的内部结构。聚类显示出类似功能词和类似内容词的特征，并且转移矩阵显示出非随机模式。此外，聚类使用情况和词性分布在手稿的不同部分有所不同。

主要发现包括识别出一个高频“功能词”聚类和一个高度多样化的“内容词”聚类。转移矩阵揭示了一个独特的结构，并且聚类使用模式因对开页部分而异。作者假设该手稿编码了一种结构化的语言，可能是构建的或助记的，采用了音节填充和重复。

该帖子提供了通过GitHub存储库重现分析的说明，强调了诸如启发式后缀剥离和缺乏语义翻译的局限性。作者鼓励语言学家、密码学家和自然语言处理研究人员贡献力量，强调该项目的目标是结构建模而非解密。

---

## 2. 间隔重复系统已经变得好多了。

**原文标题**: Spaced repetition systems have gotten way better

**原文链接**: [https://domenic.me/fsrs/](https://domenic.me/fsrs/)

本文重点介绍了由Jarrett Ye开发的新型FSRS算法驱动的间隔重复系统(SRS)的显著改进。像Anki这样的SRS程序使用抽认卡和间隔时间来优化学习和长期记忆。其核心思想是在遗忘信息之前及时复习。

旧的SuperMemo-2算法使用固定的指数退避间隔，失败后重置为第一天，这通常令人沮丧且效率低下。相比之下，FSRS利用机器学习来预测最佳复习时间，其依据是个别卡片的难度、稳定性（遗忘所需时间）和可检索性（回忆概率）。它使用21个参数，并可以使用您的复习历史进行个性化设置。

FSRS允许用户设置期望的记忆保持率，并通过模拟工作量来优化知识与工作量之比。这减少了复习次数，并改善了记忆效果。Anki自23.10版本起已将FSRS集成作为其默认调度算法。作者报告说，复习质量显著提高，复习负担减轻，并且对知识的记忆保持更有信心。

本文还批判了WaniKani和Bunpro等订阅式语言学习服务所使用的算法，这些算法使用固定的间隔模式，并在失败时采用有害的降级机制。作者提倡Anki，因为它专注于高效学习、频繁更新和灵活性。最后，本文为那些有兴趣了解更多关于间隔重复和FSRS算法的人提供了一个全面的资源列表。

---

## 3. Show HN: Buckaroo – Notebook的数据表格UI

**原文标题**: Show HN: Buckaroo – The data table UI for Notebooks

**原文链接**: [https://github.com/paddymul/buckaroo](https://github.com/paddymul/buckaroo)

Buckaroo是一款现代化的Jupyter Notebook数据表格，旨在改善探索性数据分析体验。它通过提供高性能、可排序的数据表格，并具备无限滚动、数值格式化、汇总统计、直方图、智能抽样、自动清理功能以及低代码UI，解决了标准Pandas工具的不足之处。

Buckaroo兼容JupyterLab、Jupyter Notebook、Marimo、VS Code notebooks、JupyterLite和Google Colab，并支持Pandas、Polars和Geopandas（已弃用）。

主要功能包括：

*   **高性能表格：** 基于AG-Grid，可快速加载数千个单元格，并具有可定制的显示和延迟加载功能。
*   **固定宽度格式：** 数字列采用固定宽度格式，以便快速进行视觉量级比较。
*   **直方图与汇总统计：** 提供列式数据分布概览和汇总统计信息。
*   **排序与搜索：** 方便数据探索和行查找。
*   **低代码UI：** 生成用于数据操作的Python代码片段。
*   **自动清理：** 启发式地识别并建议清理操作，例如解析日期或删除非整数字符。
*   **可扩展性：** 构建在可插拔分析框架之上，用于自定义汇总统计和自动清理。

该项目提供丰富的文档、示例笔记本和视频来指导用户。同时也鼓励贡献和问题报告。可以通过 `pip install buckaroo` 轻松安装。

---

## 4. 间隔重复记忆系统

**原文标题**: Spaced Repetition Memory System

**原文链接**: [https://notes.andymatuschak.org/Spaced_repetition_memory_system](https://notes.andymatuschak.org/Spaced_repetition_memory_system)

本文探讨了间隔重复系统（SRS）作为记忆辅助工具，结合了测试效应和间隔效应，以有效记忆大量信息。虽然常被视为死记硬背的工具，但SRS也可以通过自动化消除死记硬背来培养概念理解并促进对主题的更深入参与。本文重点介绍了Supermemo，作为第一个消费者系统和“间隔重复”一词的普及者。

本文探讨了各种SRS的实现方式，从Anki和Mnemosyne等传统程序到不寻常的变体和应用，如编程注意力和提示合成。 它深入研究了记忆系统的属性，包括摄入率和优化策略。

本文的很大一部分讨论了采用障碍。 这些障碍包括编写有效提示的难度、实践与实际应用之间感知到的脱节，以及定期实践的繁重性。它还解决了常见的反对意见，例如认为SRS仅用于死记硬背、与通过兴趣自然记住的信息无关，或者外部辅助工具就足够了。本文驳斥了这些观点，认为SRS可以通过自动化重复性任务、加速初始学习阶段和提高整体记忆力来增强学习。最后，本文简要介绍了算法、采用案例，并包含参考文献。

---

## 5. 放弃 Obsidian，自己动手构建

**原文标题**: Ditching Obsidian and building my own

**原文链接**: [https://amberwilliams.io/blogs/building-my-own-pkms](https://amberwilliams.io/blogs/building-my-own-pkms)

Amber Williams的文章详细介绍了她如何因隐私、成本和长期可用性的担忧，放弃了像Obsidian这样的商业笔记应用，并构建了自己的“笔记库”（PKMS）的历程。由于订阅费、潜在的数据泄露以及在Evernote、Notion和Obsidian等应用之间循环迁移而感到沮丧，身为软件工程师的她决定创建一个定制解决方案。

她对新的PKMS的关键要求是易于使用、类似插件的功能和强大的安全性。她优先考虑控制自己的数据，并避免潜在的将她的笔记用于定向广告或人工智能训练的滥用。

她使用开源平台Directus构建了她的PKMS，利用其现有的身份验证和安全层。这使她能够以Markdown格式创建、更新和预览笔记，无需订阅费即可跨设备访问。这些笔记以纯文本形式存储在数据库中，确保易于导出。

Williams强调了数字PKMS的优势，包括提高记忆力、互联思维和个人成长记录。她从Ryan Holiday的《Commonplace Book》中汲取灵感，强调了数字笔记卓越的搜索和组织能力。此外，AI代码生成使得创建自定义“插件”比以往任何时候都容易，取代了潜在的不安全第三方选项。

她强调了简单安全系统的重要性，告诫人们不要陷入分析瘫痪和隐私偏执。虽然商业应用提供了便利，但构建自己的应用提供了更大的控制权，降低了成本，并最终提高了她的笔记效率。她鼓励其他开发人员和知识工作者考虑构建自己的PKMS，以满足他们的特定需求，并提供了一个逐步指南来复制她的设置。

---

## 6. Show HN: Hardtime.nvim – 戒除陋习，精通 Vim 移动

**原文标题**: Show HN: Hardtime.nvim – break bad habits and master Vim motions

**原文链接**: [https://github.com/m4xshen/hardtime.nvim](https://github.com/m4xshen/hardtime.nvim)

Hardtime.nvim 是一个 Neovim 插件，旨在帮助用户改掉不良的 Vim 习惯并掌握高效的移动方式。它通过以下方式实现：

*   **限制重复按键：** 在可配置的时间范围内阻止快速重复按键，以避免低效的习惯。
*   **提供提示：** 建议更快、更 Vim 式的替代方案来代替常见的按键。
*   **报告不良习惯：** 记录频繁触发的限制和提示，供用户查看。

该插件建议使用相对跳转、基于 CTRL 的移动、单词移动、`f/F/t/T`、操作符-移动组合和括号命令来实现最佳导航。

**安装：** 需要 Neovim v0.10.0 或更高版本，可以通过 lazy.nvim 等包管理器安装。

**使用：** 默认启用，可以通过 `:Hardtime enable/disable/toggle` 切换。 `:Hardtime report` 显示习惯统计信息。 日志存储在 `~/.local/state/nvim/hardtime.nvim.log` 中。

**配置：** 提供了广泛的配置选项来自定义行为，包括：

*   `max_time`: 重复按键检测的时间窗口。
*   `max_count`: 允许的最大重复按键次数。
*   `disable_mouse`: 禁用鼠标使用。
*   `hint`: 启用/禁用提示。
*   `notification`: 控制通知。
*   自定义按键限制和提示。
*   管理插入模式空闲状态的选项。
*   文件类型排除。

欢迎贡献者，可以在 `CONTRIBUTING.md` 文件中找到说明。

---

## 7. Show HN: Racketmeter – 用声音频率测量羽毛球拍线张力

**原文标题**: Show HN: Racketmeter – Measure Badminton String Tension Using Sound Frequency

**原文链接**: [https://www.racketmeter.com/](https://www.racketmeter.com/)

RacketMeter是一款利用设备麦克风测量羽毛球拍线床张力的工具。用户输入球拍头形状（等距型、平头型、椭圆型或圆头型）和线径。点击“开始测量”按钮后，通过用手敲击球拍线床，应用程序分析声音频率来确定线床张力（磅数）。该应用程序鼓励用户分享结果，并提供包括“操作指南”视频链接在内的测量优化说明。输出结果显示线床张力水平，并指示其是低张力（< 18磅）还是更高。

---

## 8. Apple Card禁用我的iCloud、App Store和Apple ID账户（2021年）

**原文标题**: Apple Card Disabled My iCloud, App Store, and Apple ID Accounts (2021)

**原文链接**: [https://dcurt.is/apple-card-can-disable-your-icloud-account](https://dcurt.is/apple-card-can-disable-your-icloud-account)

2021年3月，作者的Apple ID、App Store、iCloud和Apple Music账户意外被禁用。最初的Apple支持互动毫无帮助，代表们无法识别或解决该问题。

根本原因追溯到Apple Card自动付款失败，原因是银行账户号码已更改，以及旧MacBook Pro的折抵款延迟到账。Apple在购买新款M1 MacBook Pro时已为旧设备的折抵发行了抵免额，但当旧设备未及时收到（由于缺少折抵套件）时，Apple将抵免额重新添加到了Apple Card余额中。

由于Apple Card自动付款失败，增加的费用触发了一个流程，Apple威胁要阻止访问Apple服务。作者收到一封电子邮件，声明该公司将禁用iPhone（错误地识别为债务来源）以及与设备购买相关的账户的iTunes和App Store访问权限。

最初错过了这封电子邮件，导致账户被锁定。尽管解决了Apple Card问题并按照说明通知了Apple，但重新激活被延迟，并且需要与Apple和高盛（Apple Card发行方）进行多次互动。该过程涉及通过电子邮件联系各个部门，导致了漫长的等待时间。最终，在联系了Apple的正确部门后，账户被重新激活。作者强调了Apple以付款问题劫持账户这种令人担忧的做法，缺乏关于Apple Card费用的清晰度，以及缓慢而脱节的客户支持体验。

---

## 9. 纪念：Cryptome联合创始人约翰·L·扬

**原文标题**: In Memoriam: John L. Young, Cryptome Co-Founder

**原文链接**: [https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder](https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder)

密码网站Cryptome联合创始人约翰·L·杨于3月28日去世，享年89岁。他是信息民主化和揭露官方秘密的先驱，这正是Cryptome的核心使命：“对民主的最大威胁是偏袒少数人的官方秘密。” Cryptome由他与妻子黛博拉·纳特西奥斯于1996年创立，成为了一个在线图书馆，发布与言论自由、隐私、国家安全和其他关键领域相关的政府、公司和法院文件。

杨的工作在存档20世纪90年代的“密码战争”，倡导加密自由不受政府控制方面发挥了重要作用。Cryptome还在早期阶段支持了维基解密，之后杨因担心其盈利化而断绝了关系。

杨是西德克萨斯人，受过建筑师训练，在创办Cryptome之前，他对公共利益的奉献精神延伸到了揭露隐秘的开发实体。他的行动主义和奉献精神导致了联邦调查局的审查以及微软等公司试图压制信息的行为。尽管面临这些挑战，杨仍然致力于透明度和公众的知情权。他自认为是激进分子，成立了城市截止日（Urban Deadline），这是一个受到全市认可的社区服务团体。杨通过信息获取实现数字化民主世界的愿景使他成为数字时代一位默默无闻的英雄，他对透明度的坚定承诺将被人们怀念。

---

## 10. 使用Arduino测量脑电波

**原文标题**: Measure EEG with Arduino

**原文链接**: [https://www.instructables.com/Measure-EEG-With-ARduino/](https://www.instructables.com/Measure-EEG-With-ARduino/)

本文介绍如何使用Arduino和名为“ardEEG”的专用扩展板来测量脑电图(EEG)、肌电图(EMG)和心电图(ECG)生物信号。核心思想是ardEEG扩展板简化了这一过程，实质上将Arduino转换成脑机接口(BCI)。

ardEEG扩展板配备了强大的ADS1299 24位ADC IC，直接连接到Arduino（特别提到的是Uno R4 WiFi）。 电极随后连接到扩展板，并根据国际10-20系统进行脑电图定位。 文章提到易于使用的Arduino和Python (Windows)脚本，用于数据采集和处理。

文章通过记录的生物数据示例突出了该设备的实用性。一个例子展示了使用Fz位置的干电极记录的咀嚼和眨眼伪迹。 另一个例子演示了在alpha波段(8-12Hz)内滤波的睁眼和闭眼脑电信号记录。

文章最后指出了该扩展板在各种需要生物信号采集的项目中的潜在应用，并提供了一个网站链接以获取更多信息。它展示了该设置的易用性和可以实现的良好数据质量。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 2 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 3 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 4 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 5 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 6 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 7 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 8 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 9 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 10 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 11 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 12 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 13 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 14 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 15 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 16 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 17 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 18 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 19 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 20 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 21 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 22 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 23 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 24 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 25 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 26 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 27 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 28 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 29 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 30 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 31 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 32 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 33 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 34 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 35 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 36 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 37 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 38 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 39 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 40 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 41 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 42 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 43 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 44 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 45 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 46 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 47 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 48 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 49 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 50 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 51 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 52 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 53 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 54 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 55 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 56 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 57 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 58 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 59 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 60 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
