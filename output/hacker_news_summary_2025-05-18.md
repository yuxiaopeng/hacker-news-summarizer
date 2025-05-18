# Hacker News 热门文章摘要 (2025-05-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Magic Leap One 引导加载程序漏洞

**原文标题**: Magic Leap One Bootloader Exploit

**原文链接**: [https://github.com/EliseZeroTwo/ml1hax](https://github.com/EliseZeroTwo/ml1hax)

该仓库记录了对 Magic Leap One (ML1) 头显的漏洞利用研究。详细描述了两个允许代码执行的漏洞：

1.  **sparsehax:** 通过 Fastboot USB 利用 CBoot（引导加载程序）中 NVIDIA SparseFS 解析器的栈溢出，从而实现代码执行。这是通过构造一个恶意稀疏镜像，使其溢出堆栈来实现的。
2.  **dtbhax:** 可以使用放置在存储上的超大 kernel-dtb 镜像覆盖内存中的 CBoot，从而允许持久的代码执行。这可能会影响使用 NVIDIA TX2 的其他设备，尤其是在汽车应用中。

该仓库包含 ML1 控制台（在 `fastbooted` 目录中）和主机（在 `fastbootrs` 目录中）的代码，后者是 Fastboot 客户端的 Rust 实现。

要利用这些漏洞，用户需要一个设备唯一的签名上下文（从固件更新中获得），并且必须准备好 `payload.bin` 文件。需要将 ML1 置于 Fastboot 模式，并执行 Rust 客户端以触发漏洞利用。警告用户存在主机变砖的风险。稍后将添加详细的文档，解释该过程和漏洞。

---

## 12. LLM群体中涌现的社会习俗和集体偏见

**原文标题**: Emergent social conventions and collective bias in LLM populations

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adu9368](https://www.science.org/doi/10.1126/sciadv.adu9368)

无法访问文章链接。

---

## 13. 用AR眼镜和安卓Linux编码两周

**原文标题**: Coding without a laptop: Two weeks with AR glasses and Linux on Android

**原文链接**: [https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/)

作者描述了他们为期两周的实验，即放弃笔记本电脑，仅使用手机、AR眼镜和折叠键盘进行编码。他们成功地在Android手机上的chroot容器内运行了完整的桌面Linux环境，配备了窗口管理器、Firefox以及Neovim、Flutter和语言服务器等开发工具。

动机是为了获得更大的自由，并在包括户外和狭小空间在内的各种环境中舒适地工作，克服笔记本电脑的局限性。硬件设置包括一台二手Pixel 8 Pro（用于DisplayPort Alt Mode）、一副二手Xreal Air 2 Pro AR眼镜和一个蓝牙折叠键盘，总成本约为636美元。

作者详细介绍了在Android上设置Linux的挑战，最终由于性能和与其他方法的兼容性问题，选择了使用Void Linux的chroot方法。他们发现AR眼镜的图像质量非常出色，尤其是用于阳光下的电致变色调光功能，但指出FOV仍有改进空间。键盘是最薄弱的环节，突出了对更好折叠键盘的需求。

性能方面，这款手机比旧款Thinkpad更快，但不如现代笔记本电脑。电池续航时间平均为4-5小时。最终，作者得出结论，该实验是成功的，强调了新获得的自由和便携性。即使存在缺陷，他们也计划继续使用该设置，以利用其独特的优势。他们强调，与Apple Vision Pro等设备相比，这种更便宜的解决方案提供了更实用的编码功能。

---

## 14. 在Apple Mail中使用Git补丁 (2023)

**原文标题**: Working with Git Patches in Apple Mail (2023)

**原文链接**: [https://btxx.org/posts/mail/](https://btxx.org/posts/mail/)

本文介绍了一种在MacOS上使用Apple Mail应用Git电子邮件补丁的简单工作流程。虽然可能存在更自动化的解决方案，但本文旨在提供一种可行的方法。

该过程包括在Apple Mail中创建一个专用的“补丁”邮箱文件夹，用于存储包含Git补丁的电子邮件。收到补丁电子邮件后，将其移动到此文件夹。然后，将“补丁”邮箱导出到本地目录，生成一个`.mbox`文件。

最后，在终端中使用`git apply`命令将补丁应用到所需的Git存储库。作者导航到存储库的目录并执行`git apply ~/Patches/<已保存的补丁邮箱文件夹>/mbox`，其中`<已保存的补丁邮箱文件夹>`对应于邮箱导出期间创建的文件夹。

文章最后提醒读者定期清理本地“补丁”文件夹以保持组织性。核心要点是提供了一种手动方法，用于将通过电子邮件接收的Git补丁集成到Git项目中，并使用Apple Mail作为中间媒介。

---

## 15. AniSora：开源动漫视频生成模型

**原文标题**: AniSora: Open-source anime video generation model

**原文链接**: [https://komiko.app/video/AniSora](https://komiko.app/video/AniSora)

Bilibili开发的AniSora是一款强大的开源AI模型，用于生成动漫风格视频。作为Index-AniSora项目的一部分，它旨在普及动漫创作，实现一键生成各种风格的视频，如动漫剧集、中国动画、漫画改编和VTuber内容。

用户可以上传图像并提供文本提示来指导AI创建动态视频。该平台允许选择不同的AI模型。AniSora经过专门训练，使用了大量的动漫和漫画数据集，以确保真实的视觉效果和艺术细微差别。

主要优势包括直观的界面、高质量的动画视频输出以及对动漫美学的专注。用例包括生成社交媒体短片、宣传视频、动画漫画面板以及开发VTuber内容。它专为一致的角色动画和富有表现力的动作而构建，使其成为动漫和动画领域的创作者的理想选择。虽然主要专注于视频，但音频集成可能是可能的，应该进行验证。用户可以通过输入图像和文本提示来影响风格和动作，并具有进行高级定制的潜力。

---

## 16. 新视野号飞掠冥王星

**原文标题**: Pluto Flyover from New Horizons

**原文链接**: [https://apod.nasa.gov/apod/ap250518.html](https://apod.nasa.gov/apod/ap250518.html)

今日天文图片（APOD）：这段延时视频由新视野号探测器在2015年7月飞掠冥王星期间拍摄的图像制作而成，引人入胜。视频提供了这颗矮行星的虚拟“飞越”景象，让观众得以一窥其多样而迷人的地形。

视频展示了冥王星的景观，包括由冰冻氮着色的水冰构成的巍峨山脉。一片广阔、平坦的固态氮海也十分突出，显示出不寻常的多边形形状，据信这是由冥王星相对温暖的内部对流造成的。这次飞越揭示了许多陨石坑和冰山。

视频以“刀刃状”地形的景象达到高潮，其特征是高达500米的山脊被公里级的间隙分隔开来。新视野号以大约8万公里/小时的速度飞行，无法返回冥王星，目前正驶出太阳系。这些图像经过增强处理，以突出冥王星表面的颜色和特征。

---

## 17. 地狱之门的征服 [pdf]

**原文标题**: The Conquest of Hell Gate [pdf]

**原文链接**: [https://www.nan.usace.army.mil/portals/37/docs/history/hellgate.pdf](https://www.nan.usace.army.mil/portals/37/docs/history/hellgate.pdf)

无法访问文章链接。

---

## 18. 打造我的童年梦想电脑

**原文标题**: Building my childhood dream PC

**原文链接**: [https://fabiensanglard.net/2168/index.html](https://fabiensanglard.net/2168/index.html)

Fabien Sanglard回忆了他童年时梦想拥有一台高端 IBM PS/1 2168 PC 的经历。这个梦想源于一次令人失望的早期 PC 购买体验以及对邻居家更高级电脑的羡慕。多年后，他开始了一个项目，旨在获取并修复这台梦想中的 PC。

文章详细描述了他寻找 IBM PS/1 2168 的过程，突出了它令人向往的特性，例如带有提手的迷你塔式设计、圆角造型带来的用户友好美感以及巧妙的前面板设计。他强调了这些系统通常配备的、具有清脆敲击声的 Model M 键盘的吸引力，赞扬了它的质量和声音。Sanglard 还提到了该机器全面的文档资料和扩展选项，包括用于 CPU 升级、RAM 和 ISA 卡的插槽。

由于该型号的年代久远和受欢迎程度，他的搜索过程充满挑战，他需要找到一台仍然能够启动，尤其是 33Mhz 型号的机器。最终，他在芬兰找到了一台 PS/1 2168-594 DX2-66Mhz，配备了原装包装盒和手册，经过与卖家的协商，最终达成了交易。

---

## 19. 宾夕法尼亚州议会扣押太阳能拨款——需求激增

**原文标题**: Solar grants held hostage in Pennsylvania legislature – as demand soars

**原文链接**: [https://capitalandmain.com/solar-grants-held-hostage-in-pennsylvania-legislature-as-demand-soars](https://capitalandmain.com/solar-grants-held-hostage-in-pennsylvania-legislature-as-demand-soars)

宾夕法尼亚州太阳能需求增长与政治阻碍

本文重点介绍了宾夕法尼亚州对太阳能日益增长的需求以及阻碍其发展的政治障碍。尽管拥有广泛的公众支持和潜在的经济效益，太阳能计划在该州立法机构中面临僵局。

文章介绍了通克汉诺克地区学区，该学区寻求州政府拨款安装太阳能电池板，每年可节省 100 万美元。然而，太阳能学校项目只有 2500 万美元的资金，却被总额达四倍的申请所淹没。

尽管宾夕法尼亚州具有强大的潜力，但在太阳能发展方面仍落后于其他州。社区太阳能法案和提高该州可再生能源目标的提案均未获得立法机构通过。

一项用于住宅太阳能装置的联邦拨款也因立法障碍而被搁置。前公用事业公司律师克雷格·威廉姆斯众议员提出的一项修正案，引发了人们对净计量未来的担忧，净计量是太阳能用户的重要激励措施。

尽管面临这些挑战，一些保守派人士正在软化他们对可再生能源的立场。虽然太阳能计划的未来仍然不确定，但倡导者仍然对太阳能造福宾夕法尼亚州社区的潜力持乐观态度。

---

## 20. Show HN: 在 Chrome 侧边栏中的 Web 浏览器代理

**原文标题**: Show HN: A web browser agent in your Chrome side panel

**原文链接**: [https://github.com/parsaghaffari/browserbee](https://github.com/parsaghaffari/browserbee)

BrowserBee是一款开源Chrome扩展，允许用户通过LLM使用自然语言控制浏览器。与其他浏览器自动化工具不同，BrowserBee主要在浏览器本身内运行（LLM除外），使其注重隐私，适合在登录网站上使用，而无需后端基础设施。

主要功能包括支持主流LLM提供商（Anthropic、OpenAI、Gemini、Ollama）、token使用跟踪、访问由Playwright驱动的各种浏览器工具以实现可靠的自动化，以及用于存储和重用成功操作序列的记忆功能。该代理还旨在要求用户批准购买或社交媒体更新等操作。

BrowserBee支持各种各样的工具，从基本的导航和标签管理到DOM操作、文本提取、鼠标和键盘操作。记忆工具允许保存、查找和删除特定网站的学习操作序列。

用例包括社交媒体管理、新闻策划、充当个人/研究助理、知识书签和摘要，以及通过聊天与网站交互。

安装选项包括从GitHub下载最新版本、从源代码构建，以及最终从Chrome网上应用店安装。该工具通过Chrome工具栏图标或键盘快捷键激活。

该项目利用Playwright在浏览器内进行强大的浏览器交互，并强调“反思和学习”记忆模式，以提高效率并减少token使用。作者强调了为LLM处理网页的挑战，并提倡基于开源原则构建的以隐私为先的个人AI工具。

---

## 21. 富人买什么，而普通人一无所知？(2015)

**原文标题**: What do wealthy people buy, that ordinary people know nothing about? (2015)

**原文链接**: [https://old.reddit.com/r/AskReddit/comments/2s9u0s/comment/cnnmca8/](https://old.reddit.com/r/AskReddit/comments/2s9u0s/comment/cnnmca8/)

无法访问文章链接。

---

## 22. 维罗纳项目：Python的无畏并发

**原文标题**: Project Verona: Fearless Concurrency for Python

**原文链接**: [https://microsoft.github.io/verona/pyrona.html](https://microsoft.github.io/verona/pyrona.html)

维罗纳项目：探索Python的“无畏并发”，通过开发名为Lungfish的新所有权模型。该模型旨在为Python提供一种安全高效的内存和并发管理方式，解决Python随着PEP703全面并发模型而可能产生的并发问题。

该项目始于使用名为FrankenScript的玩具语言进行原型设计，以快速测试基于区域的所有权理念。FrankenScript使用动态检查并生成图表来展示程序区域结构。

该团队正与Faster CPython团队和更广泛的Python社区进行互动，并在Python语言峰会等活动中寻求反馈。

该策略采用循序渐进的方法，从Python中的深度不变性开始。这包括起草PEP、在CPython中进行原型设计、使用引用计数管理循环不变的垃圾，以及与子解释器之间的消息传递（PEP734）集成以实现并行性能。深度不变性对于安全地在并发线程之间共享类型信息至关重要。在不变性之后，他们将应用基于区域的所有权模型来允许安全地共享可变状态，并借鉴FrankenScript原型。

目标不是复制Rust的所有权模型，因为它对于Python的动态类型来说过于严格。相反，他们正在设计一种新的基于区域的所有权模型，该模型具有动态检查，并借鉴了Rust、Cyclone、Encore和Pony等语言。

在Python上的工作显着提高了维罗纳项目对动态类型语言中所有权的理解，并导致重新评估其所有权模型中静态和动态检查之间的平衡。

---

## 23. 纸艺机械

**原文标题**: Paper Mechanisms

**原文链接**: [https://cutfoldtemplates.com](https://cutfoldtemplates.com)

纸质机械：展示了34种纸基装置和机械结构，演示了各种不同的功能、光学错觉和叙事能力。这些机械结构，从简单的折叠到复杂的弹出式结构，突出了纸张作为一种动态材料的潜力。

该系列包括常见的形式，如六角环和三浦折叠，以及更复杂的结构，如双稳态机构、折纸闪光器和旋转凸轮。一些例子展示了机械工程原理在纸张上的应用，创造了运动和动画。还包括光学错觉，包括“无限形式”和创造运动幻觉的形式。

许多机械结构，如威尼斯百叶窗揭示和旋转图片揭示，都是改编自历史资料，特别是维多利亚时代的贺卡和约瑟夫·阿尔伯斯在包豪斯的学生的作品。本文突出了这些机制在广告、讲故事、艺术甚至卫星设计等领域的潜力，展示了纸张作为一种功能性和表现性媒介的多功能性。反复出现的来源“制作机械卡片：希拉·斯特罗克设计的25种纸质工程设计”表明，有一个随时可用的资源可以复制和学习这些设计。视频经常伴随着描述。

---

## 24. 不起眼的栗子如何见证罗马帝国的兴衰

**原文标题**: How the humble chestnut traced the rise and fall of the Roman Empire

**原文链接**: [https://www.bbc.com/future/article/20250513-what-chestnuts-reveal-about-the-roman-empire](https://www.bbc.com/future/article/20250513-what-chestnuts-reveal-about-the-roman-empire)

本文探讨了罗马帝国通过传播甜栗树对欧洲森林产生的令人惊讶的影响。罗马帝国以道路和渡槽等基础设施而闻名，同时也为了其快速生长的木材（对于建筑和军事扩张至关重要）而种植和传播栗树。地理学家帕特里克·克雷布斯及其团队利用花粉记录、古代文献以及栗树和胡桃树的分布来追踪这种树木遗产。

罗马人最初并不一定对果实本身感兴趣，而是对甜栗树的萌蘖潜力感兴趣，这为堡垒和其他建筑物提供了一种可持续的木材来源。本文强调，在罗马帝国鼎盛时期，栗树花粉显著增加，而在帝国衰落后则减少，反映了果园的废弃。虽然罗马人的影响在欧洲大陆是显而易见的，但研究表明，他们并没有将栗子引入英国。

本文还探讨了人类与栗树之间的共生关系，特别是在瑞士提契诺等地区，那里的栽培实践使栗树能够存活长达1000年，并成为主食。这种从罗马人到当地居民的知识转移使得栗树即使在帝国衰落后也能蓬勃发展。如今，甜栗树面临着疾病和气候变化等新的挑战，但它的遗产仍然提醒着我们罗马人的聪明才智和当地管理所产生的持久影响。

---

## 25. 混合Rust和Java的教训：快速、安全、实用

**原文标题**: Lessons from Mixing Rust and Java: Fast, Safe, and Practical

**原文链接**: [https://medium.com/@greptime/how-to-supercharge-your-java-project-with-rust-a-practical-guide-to-jni-integration-with-a-86f60e9708b8](https://medium.com/@greptime/how-to-supercharge-your-java-project-with-rust-a-practical-guide-to-jni-integration-with-a-86f60e9708b8)

本文提供了一份将 Rust 和 Java 集成以获得性能和系统级编程优势的实用指南。它重点介绍了常见的用例，例如绕过 Java 的垃圾回收器以执行对性能至关重要的任务，以及利用 Rust 的速度和实现隐藏。

文章的核心集中在四个关键的互操作性挑战及其解决方案上：

1.  **打包特定于平台的 Rust 库：** 它建议将特定于平台的 Rust 库嵌入到单个 JAR 文件中，按每个架构组织到不同的文件夹中，然后使用实用程序类在运行时动态加载相应的库。
2.  **统一日志：** 它提倡通过相同的 SLF4J 后端传递 Rust 和 Java 日志，这可以通过在 Java 中创建一个 Logger 包装器并通过 JNI 从 Rust 调用它来实现。
3.  **调用 Rust 异步函数：** 它通过使用异步任务生成与 Java 端的 CompletableFuture 相结合来解决 JNI 方法与 Rust 异步函数的不兼容性问题。
4.  **将 Rust 错误映射到 Java 异常：** 它描述了如何将 Rust 的 `Result::Err` 转换为 Java `RuntimeExceptions` 以实现统一的异常处理。

文章强调了实用的代码示例，并指向一个开源的 `rust-java-demo` 存储库以提供完整的可运行演示。文章最后邀请社区贡献。作者 Greptime 介绍了其为实时可观测性设计的开源、云原生数据库。

---

## 26. Sun Enterprise 10000 的诞生 (2007)

**原文标题**: How the Sun Enterprise 10000 was born (2007)

**原文链接**: [https://www.filibeto.org/aduritz/truetrue/e10000/how-e10k-wasborn.html](https://www.filibeto.org/aduritz/truetrue/e10000/how-e10k-wasborn.html)

本文详细介绍了Sun Enterprise 10000服务器（又名Starfire）的诞生，追溯其起源于一群最初离开圣地亚哥老牌公司，致力于使用Sparc处理器构建大规模并行计算机的工程师。 经过几次收购和合并，这项努力促成了Cray Research旗下的CS6400（SuperDragon）的诞生，并融入了动态系统域和备用路径等功能。

运行Solaris的CS6400在工程师和Sun Microsystems之间建立了合作关系。 当SGI收购Cray时，它认为基于Sparc的部门与其现有技术相冲突，并以5000万美元的价格将其出售给Sun。

Sun看到了该部门工作的潜力，并在他们即将完成Ultra Enterprise Server 10000时收购了他们。 在Sun的领导下，Enterprise 10000得以完成并取得了成功，通过更简单的动态重配置和更快的硬件完善了CS6400的概念。 由于先进的ASIC，它因其SMP扩展能力而备受赞誉。 Scott McNealy认为这次收购是Sun的重大胜利，为Sun带来了数十亿美元的收入。

本文还包括一份新闻稿，宣布Sun收购Cray业务系统部门的意向，强调了该收购对于Sun扩展其企业服务器解决方案以及为Cray的SPARC/Solaris客户提供兼容路径的战略意义。

---

## 27. Kubernetes上的高可用Mosquitto MQTT

**原文标题**: High Available Mosquitto MQTT on Kubernetes

**原文链接**: [https://raymii.org/s/tutorials/High_Available_Mosquitto_MQTT_Broker_on_Kubernetes.html](https://raymii.org/s/tutorials/High_Available_Mosquitto_MQTT_Broker_on_Kubernetes.html)

本文提供了一个完整的 Kubernetes 原生设置方案，用于构建高可用 Mosquitto MQTT 消息代理，确保最小停机时间和故障期间的无缝消息传播。它利用了核心 Kubernetes 组件，如 Deployments、Services、ConfigMaps 和 RBAC，以及 Traefik IngressRouteTCP 用于外部访问。

该方案使用两个 Mosquitto 消息代理：一个主代理和一个辅助代理，两者都配置为桥接消息，以实现近乎实时的状态同步。一个自定义的故障转移控制器，以 Pod 的形式部署，监控主代理的就绪状态。如果主代理不可用，控制器会自动修补 Kubernetes Service，在 5 秒内将流量重新路由到辅助代理，从而最大限度地减少服务中断。与单个 Pod 部署相比，这种方法具有显著的改进，后者可能需要长达 5 分钟才能从节点故障中恢复。

本文详细介绍了每个组件的配置，包括：

* 用于消息代理配置的命名空间和 ConfigMaps。
* 用于主代理、辅助代理和故障转移 Pod 的 Deployments。
* 用于将流量路由到消息代理的 Services。
* 用于授予故障转移 Pod 必要权限的 RBAC 配置。
* 用于外部 MQTT 访问的 Traefik IngressRouteTCP。

作者强调了使用 ServiceAccount 和 RBAC 为故障转移 Pod 授权的重要性，使其能够监控消息代理的健康状况并动态地重新路由流量。文章提供了一个包含所有必要资源的完整 YAML 文件。

---

## 28. 程序员应该知道的枚举组合数学

**原文标题**: What Every Programmer Should Know About Enumerative Combinatorics

**原文链接**: [https://leetarxiv.substack.com/p/counting-integer-compositions](https://leetarxiv.substack.com/p/counting-integer-compositions)

无法访问文章链接。

---

## 29. 神秘

**原文标题**: Mystical

**原文链接**: [https://suberic.net/~dmm/projects/mystical/README.html](https://suberic.net/~dmm/projects/mystical/README.html)

"神秘"：一种将PostScript代码表示为魔法圆圈的可视化编程语言概念。它的结构依赖于嵌套的环，这些环对应于PostScript的可执行数组 (`{}`)、非可执行数组 (`[]`) 和字典 (`<< >>`)。这些环通过边框样式和内部符号在视觉上区分，连接点用指向附属环的线标记。

该语言使用“符记”——代表运算符、变量和关键字的符号——来代替文本，从而增强代码的视觉和符号性质。标准运算符被分配特定的符记，而用户定义的函数和变量可以创建自定义符记，从而实现个性化的视觉表示。

对于将名称定义为函数的常见模式 (`/name { ring } def`)，引入了一种独特的连字语法，从而节省空间并强调定义。

本文描述了用于从PostScript数组和字典渲染“神秘”图像的函数（在“mystical.ps”中定义）。这些函数 `mystical`、`mystical_evoke` 和 `mystical_evoke_label` 处理环的视觉布局和缩放。当前的布局算法优先考虑避免碰撞，从而导致可能稀疏的图表。

作者承认，“神秘”目前是PostScript的一种视觉表示，而不是一种完全可解释的语言。然而，它可以由人来解释，或转录回PostScript以供执行。这个概念有可能适用于其他基于运算符的语言，如 Forth，但复杂的语句结构可能会带来挑战。该代码可在GitHub和Codeberg上找到。

---

## 30. Show HN: 将任何工作流程图转换为可编译、运行且有状态的代码

**原文标题**: Show HN: Turn any workflow diagram into compilable, running and stateful code

**原文链接**: [https://workflows.diagrid.io/](https://workflows.diagrid.io/)

此“Show HN”帖子介绍 Workflow Composer，一款利用 Dapr Workflows 将工作流图转换为功能性、可运行且有状态代码的工具。 基本上，它允许用户可视化地设计工作流，然后自动生成执行它们所需的底层代码，以持久且可靠的方式运行。 该工具突出了使用开源技术的优势，并提供了文档、Discord 社区、Dapr 网站和使用条款的链接，表明它是一个易于访问且受到良好支持的产品。“加载图库…”表明有一个视觉组件展示了该工具的功能。 总的来说，Workflow Composer 通过 Dapr 的强大功能，弥合了可视化工作流设计和代码实现之间的差距，从而简化了持久应用程序的开发。

---

## 31. 涂鸦艺术

**原文标题**: Graffiti Art

**原文链接**: [https://graffitiart.app](https://graffitiart.app)

本文介绍一款人工智能驱动的涂鸦艺术生成器，它能将文本转化为专业级别的涂鸦设计。该工具无需设计技能，即可创作自定义的涂鸦字体和各种风格的独特设计，从经典的狂野风格到现代的泡泡字体。

主要功能包括文本转涂鸦转换器、自定义字体生成器、专业风格控制（颜色、阴影、高光）、多种涂鸦风格以及高分辨率输出选项（高清到8K）。该生成器允许用户通过直观的编辑功能微调设计。

文章概述了一个简单的五步流程：输入文本、选择风格、生成艺术作品、自定义设计并下载。

提供多种定价方案：标准版、高级版和专业版，每种方案在积分、风格访问、分辨率和商业使用权方面有所不同。用户评价赞扬了该工具的多功能性、真实性以及为数字艺术家、街头艺术家和设计师节省时间的优点。

最后，常见问题解答部分回答了关于生成器的功能、风格、商业用途、输出质量、自定义、易用性、速度以及保存收藏设置等常见问题。

---

## 32. 最先进的 PFAS [pdf]

**原文标题**: State of the Art PFAS [pdf]

**原文链接**: [https://iplo.nl/publish/pages/235260/state-of-the-art-pfas.pdf](https://iplo.nl/publish/pages/235260/state-of-the-art-pfas.pdf)

文件标题为“当前 PFAS 土壤地下水知识状况”(PFAS Knowledge Soil Groundwater)，是一份关于土壤和地下水中 PFAS 污染的 PDF 文件。元数据显示这是一份关于该领域知识差距和研究需求的概述，可能由 Arcadis Nederland B.V. 委托制作。

元数据还提到：

* **创建和修改日期：**2023 年 2 月，表明是相对较新的工作。
* **CollaborationHub：** 表明是一个协作项目或共享文档。
* **土壤和地下水知识差距和研究需求概述：** 强调了文档的目的。

由于提取的文本主要由 PDF 元数据和压缩数据（来自 FlateDecode 过滤器）组成，因此无法提供关于特定 PFAS 化合物、污染水平、研究结果或拟议解决方案的文档内容的详细摘要。然而，该文档的标题和元数据明确表明它是一个处理土壤和地下水中 PFAS 污染的知识现状和所需研究的资源，鉴于 Arcadis Nederland B.V. 的参与，重点可能在荷兰。

---

## 33. 软件工程手册反思

**原文标题**: Reflecting on Software Engineering Handbook

**原文链接**: [https://yusufaytas.com/reflecting-on-software-engineering-handbook/](https://yusufaytas.com/reflecting-on-software-engineering-handbook/)

2024年5月，作者们在历经两年辛勤工作后，庆祝了《软件工程手册》的发布，并将其设想为软件工程师的全面指南。然而，一年后，这本书远未达到预期。

尽管内容本身获得了积极反馈，但两个主要问题阻碍了它的成功：误导性的“手册”标题（因为它更像是一本指南）以及未能脱颖而出的通用名称。数据显示，销量极低，最初的小幅增长之后迅速下降。虽然谷歌显示了很高的单位份额，但几乎没有产生任何收入，这主要是由于赠送给大学生的折扣副本。亚马逊是唯一可行的销售渠道，但即使如此也令人失望。

包括亚马逊和Reddit广告在内的营销尝试，在很大程度上都无效。亚马逊广告存在格式问题，而Reddit广告则遭遇了差评。尽管领英拥有不错的关注者，但由于该平台向肤浅的网红内容转变，未能转化为显著的销售额。

作者们将这本书表现不佳归因于缺乏营销专业知识、紧张写作过程后的倦怠以及不愿参与不真实的营销策略。他们低估了有效营销和推广所需的努力，主要侧重于内容创作。

然而，这次经历并非完全没有收获。令人惊讶的是，这本书为作者们带来了即时的信誉提升，并已成为指导和教学的宝贵工具，提供了一个结构化的资源来指导个人学习特定主题。

---

## 34. 如果没有任何筛选，我们如何找到东西？

**原文标题**: If nothing is curated, how do we find things

**原文链接**: [https://tadaima.bearblog.dev/if-nothing-is-curated-how-do-we-find-things/](https://tadaima.bearblog.dev/if-nothing-is-curated-how-do-we-find-things/)

在一个信息过载、算法主导的世界里，作者感叹策展的衰落及其对我们发现和参与艺术文化的影响。作者回忆起过去，那时获取信息更加容易，依靠大学广播、音乐杂志和电视节目等精选来源，它们提供了经过过滤且易于管理的内容。

现在，社交媒体和算法通过分散信息和需要不断搜索，制造了一种“便利的幻觉”。这种持续的搜索变得令人疲惫，导致一种不知所措的感觉，以及无法充分参与推荐内容。算法将用户困在信息茧房中，强化现有的偏好，而不是引入新的和多样化的内容。

作者认为，策展的消亡迫使个人自己从“垃圾堆”般的信息中筛选，这项任务感觉就像一份工作。即使是像Vulture和Pitchfork这样的传统策展来源，也通过发布过量的内容来追逐点击量，从而加剧了问题。

作为一种个人解决方案，作者已经开始在Obsidian中做笔记和列清单，但这并不完美，仍然需要付出大量的努力。作者认为，社会可能正在分裂为两类人：一类优先考虑算法带来的舒适感，另一类则积极寻求新的体验，接受驾驭这片信息汪洋的挑战。作者承认确实存在一个策展事物的新网站，但在本文写作时还不存在，突显了策展的问题。

---

## 35. 如何在CSS中让浏览器选择对比色

**原文标题**: How to have the browser pick a contrasting color in CSS

**原文链接**: [https://webkit.org/blog/16929/contrast-color/](https://webkit.org/blog/16929/contrast-color/)

本文介绍了CSS的`contrast-color()`函数，该函数允许浏览器根据背景颜色的对比度自动选择黑色或白色文字颜色。这简化了Web开发，无需为不同的背景颜色手动管理文字颜色配对，尤其是在动态场景中，例如带有悬停效果的按钮样式。

然而，作者强调`contrast-color()`本身并不能保证可访问性。其有效性取决于所选的背景颜色和浏览器使用的对比度算法。目前，Safari技术预览版使用WCAG 2算法，虽然权威，但在准确反映感知对比度方面存在已知局限性，尤其是在中等色调颜色方面。文章强调了APCA算法的潜力，这是一种基于感知的替代方案，正被考虑用于WCAG 3，它提供了更准确的对比度评估。

作者强调了考虑可访问性指南（例如APCA提供的指南）以及评估字体大小和粗细的重要性。为了进一步增强可访问性，可以使用`prefers-contrast`媒体查询为需要更高对比度的用户提供替代样式，例如，根据用户的偏好交换颜色。最终，即使使用像`contrast-color()`这样的高级工具，人为判断和仔细设计对于确保所有用户都能获得足够的对比度和可访问性至关重要。

---

## 36. 死亡的星星不会发光

**原文标题**: Dead Stars Don’t Radiate

**原文链接**: [https://johncarlosbaez.wordpress.com/2025/05/17/dead-stars-dont-radiate-and-shrink/](https://johncarlosbaez.wordpress.com/2025/05/17/dead-stars-dont-radiate-and-shrink/)

本文批判了一篇最新的论文，该论文声称所有大质量物体，甚至包括死亡恒星，都会辐射霍金辐射并最终蒸发，从而导致宇宙更快地终结。作者认为这一说法基于有缺陷的近似，并与已建立的物理原理相悖。

Wondrak、van Suijlekom 和 Falcke 这篇问题论文断言，任何质量的引力场都会产生辐射掉的粒子-反粒子对，导致物体失去质量并违反重子数守恒。作者强调，如果这是真的，这将是一项革命性的发展，推翻了数十年来对弯曲时空量子场论的既定理解。

然而，作者指出了反驳和现有的文献，特别是 Ashtekar 和 Magnon 1975 年的论文以及 Wald 的教科书，这些文献严格证明，具有类时 Killing 矢量场（时间平移对称性）的静态时空不会产生自发的粒子产生。作者批评原论文采用了粗略的近似，导致了不正确的结果，并且没有充分地解决关于该主题的现有知识。

文章进一步感叹媒体对这一有缺陷的研究进行了耸人听闻且不加批判的报道，导致了错误信息的传播。作者强调了咨询专家和批判性地评估科学主张的重要性，然后再将其视为事实。他还回应了读者的评论，解释说，与电场不同，引力不会产生类似的施温格效应。虽然黑洞允许信息（但不是净重子数）逃离其视界，但对于争议论文中描述的情况，情况并非如此。

---

## 37. 迷你工艺 (Windows 95 及以上)

**原文标题**: Craft Basic (Windows 95 and up)

**原文链接**: [https://www.lucidapogee.com/?page=craftbasic](https://www.lucidapogee.com/?page=craftbasic)

本网页推广 Craft Basic，一款适用于 Windows 95 及以上系统的免费 BASIC 解释器，当前版本为 1.7.1，上次更新于 2023 年 12 月 19 日。它旨在帮助用户学习编程、创建简单游戏、编写脚本、执行计算和显示图形。 它包含位图绘制、WAV 文件播放以及带有静态文本和按钮的窗体处理等功能，并附带供初学者使用的示例程序。

该页面提供下载链接（lucidapogee.com 和 itch.io）、文档和支持论坛。 支持的操作系统范围从 Windows 9X 到 Windows 11。

该页面还详细介绍了 Lucid Apogee 的另一个项目“Express BASIC”的最新更新。 更新包括新函数（SPACE$, HEX$, OCT$）、位运算符（BAND, BOR, BNOT）、COLOR 和 LOCATE 等命令以及字符串操作改进。 他们还宣布发布了命令行工具“Express Calculator”。 Craft Basic v1.7.1 的最新更新包括清理示例并从其他语言添加更多示例。

最后，该页面包含指向支持论坛、新闻、注册、登录和搜索的链接。 页面底部还提供联系方式和分享选项，以及 Lucid Apogee 2025 年的版权声明。

---

## 38. 专家轻松搞定 (2024)

**原文标题**: Experts have it easy (2024)

**原文链接**: [https://boydkane.com/essays/experts](https://boydkane.com/essays/experts)

本文探讨了专家和新手之间的显著差异，强调了专家的高效率和更佳成果往往被低估和误解。新手常常效率低下，创建复杂且难以维护的抽象概念，而专家则能凭借经验和洞察力直接解决问题。

作者用迷宫导航的类比来说明这些差异。缺乏专家预先准备的方法（如线团）的新手，会做出糟糕的决定，从而加剧困难。这些问题往往是他们自己造成的，并且远比专家遇到的问题复杂。

主要要点如下：

*   新手经常在不相关的问题上浪费时间，扭曲了他们对该领域的看法。
*   由于缺乏对相互依赖性的理解，他们会在信息有限的情况下做出随机决策。
*   他们经常错过专家能够轻易看到的关键决策点。
*   专家通常依靠无法总是清楚表达的直觉，强调了观察的价值。
*   专家拥有用于支持的网络，新手很难有效利用这些网络。

文章最后为新手提出了建议：寻找一位有同情心的专家进行指导，或寻找专家网络。重要的是，要强调与专家进行随意的“闲聊”互动，以实现隐性知识的传递的好处。此外，新手应独立深入地探索利基领域，以获得特定领域的专业知识。最重要的是，新手需要勇气、信心和一位善良的专家，以避免灰心丧气。

---

## 39. 任天堂64的调色板光照技巧

**原文标题**: Palette lighting tricks on the Nintendo 64

**原文链接**: [https://30fps.net/pages/palette-lighting-tricks-n64/](https://30fps.net/pages/palette-lighting-tricks-n64/)

本文详细介绍了一种在任天堂64（一款以处理能力有限而闻名的游戏机）上实现实时着色的新方法。作者概述了一种利用调色板纹理实现烘焙定向环境光和镜面反射着色与法线贴图的技术，尽管N64硬件存在局限性。

核心思想是在CPU上执行着色计算，但只更新纹理的颜色调色板，而不是单独的纹素。由于许多N64纹理都使用调色板，这大大降低了计算成本，从而创造了实时着色的假象。

该技术采用对象空间法线贴图，其中法线直接编码在纹理中。漫反射和法线纹理共享同一调色板，并使用K-means聚类进行压缩。在着色期间，处理每个调色板颜色，获取法线和漫反射颜色，从而为该索引生成新的着色RGB颜色。

烘焙光照通过使用顶点颜色存储环境光和直射阳光信息来整合。环境光进一步分解为定向强度和颜色，而阳光可见性存储在顶点Alpha通道中。这允许更丰富、更逼真的光照效果。

本文还讨论了将该技术应用于具有重复纹理的模型时所面临的挑战，需要将网格拆分为具有近似切线空间的子网格。虽然可以通过近似实现镜面反射着色，但“调色板空间”方法最适合漫反射定向光。

作者承认该技术的局限性，包括着色不连续性和缺乏对点光源的支持，但强调了其通过精心预处理的潜力。文章最后呼吁进一步研究解决这些局限性并提高整体着色质量。

---

## 40. 通过N元语法统计理解Transformer

**原文标题**: Understanding Transformers via N-gram Statistics

**原文链接**: [https://arxiv.org/abs/2407.12034](https://arxiv.org/abs/2407.12034)

论文《通过N-gram统计理解Transformer》由Timothy Nguyen撰写，通过将Transformer大型语言模型(LLM)的预测与从训练数据中得出的简单N-gram统计相关联，研究了其运作方式。核心思想是用基于N-gram出现频率的规则来近似Transformer的预测。

该研究揭示了几个有趣的发现：一种无需预留集的过拟合检测新方法，衡量Transformer在训练过程中从简单到复杂统计规则过渡的指标，一种解释N-gram规则何时能很好地描述Transformer预测的模型方差标准，以及对N-gram规则近似随着复杂性增加而产生的局限性的洞察。

具体来说，该研究发现，对于LLM下一个token分布的很大一部分（在TinyStories上为79%，在Wikipedia上为68%），Transformer模型的top-1预测与N-gram规则集提供的预测一致。这表明N-gram统计在LLM行为中起着重要作用。

该论文已在NeurIPS 2024上发表，并公开了其数据集和N-gram统计数据。其主题领域包括计算与语言、人工智能和机器学习。

---

## 41. O2 VoLTE：通过通话定位任何客户

**原文标题**: O2 VoLTE: locating any customer with a phone call

**原文链接**: [https://mastdatabase.co.uk/blog/2025/05/o2-expose-customer-location-call-4g/](https://mastdatabase.co.uk/blog/2025/05/o2-expose-customer-location-call-4g/)

本文详细描述了O2英国VoLTE（“4G通话”）实现中的一个严重隐私漏洞，该漏洞暴露了通过4G/WiFi拨打或接听电话的任何O2客户的位置。作者发现VoLTE通话期间发送的IMS/SIP消息包含敏感数据，包括接收方的IMSI、IMEI和Cell ID。

Cell ID结合cellmapper.net等网站的众包数据，使得任何发起呼叫的人都能够相当精确地定位接收者的位置，尤其是在蜂窝塔更加密集的稠密城市区域。即使接收者在国际漫游时，此漏洞仍然存在。

作者强调，标准手机无需任何特殊修改，即可在VoLTE通话期间接收到此泄露位置的数据。禁用“4G通话”并不能阻止暴露上次连接的基站及其使用时间。

作者曾尝试向O2的首席执行官和一个与隐私相关的电子邮件地址报告该漏洞，但未收到任何回复。与竞争对手（EE）明确的漏洞报告流程形成对比，作者对O2缺乏回应表示失望，并倡导立即从IMS/SIP消息中删除暴露的标头。结论是该漏洞允许对O2客户进行简单的地理定位，并突出了客户缺乏防止这种情况发生的途径。

---

## 42. RISC OS 图形用户界面

**原文标题**: The RISC OS GUI

**原文链接**: [https://telcontar.net/Misc/GUI/RISCOS/](https://telcontar.net/Misc/GUI/RISCOS/)

本文探讨了独特的RISC OS 3.11图形用户界面，并将其与Apple System 7等同时代的产品进行了比较。 它突出了RISC OS非同寻常的设计选择和创新功能，赞扬了其在当时的先进性。

桌面由图钉板（背景和固定图标）和图标栏（已挂载的文件系统/服务和活动任务）组成。 三键鼠标提供不同的功能：“选择”、“菜单”和“调整”，后者作为修改键的替代方案，提供替代操作，而无需依赖键盘。

本文强调了通过鼠标中键调用的弹出式菜单的使用，模糊了标准菜单和上下文菜单之间的界限。 一个显著的特点是将对话框直接集成到菜单系统中，允许用户输入自定义值或将完整的对话框作为菜单项访问，从而简化交互。

窗口以单一堆栈方式管理，除了将窗口推到后面或使用缩放按钮外，控件有限。 窗口焦点独立于窗口堆栈；可以在不将其置于最前面的情况下操作窗口。 键盘焦点更加独特，通常与活动窗口无关，仅应用于特定元素，如文本输入字段。 总的来说，本文将RISC OS描绘成一个图形界面，它以有趣且非常规的方式进行用户交互。

---

## 43. 模因学——美军行动中的新兴产业 (2006) [pdf]

**原文标题**: Memetics – A Growth Industry in US Military Operations (2006) [pdf]

**原文链接**: [https://apps.dtic.mil/sti/pdfs/ADA507172.pdf](https://apps.dtic.mil/sti/pdfs/ADA507172.pdf)

由于PDF转换造成的OCR质量差，难以生成《模因学——美军行动中的一个成长型产业（2006）》的完整准确摘要。

然而，PDF代码和有限的提取文本表明，该文件可能讨论了**模因学及其在美国军事行动中的潜在应用。**

以下是可推断的内容：

*   **关注模因学：** 标题明确提到了“模因学”，表明中心主题围绕着这个研究领域。模因学是研究思想和文化信息如何在社会中传播、进化和复制的学科，类似于基因。
*   **军事应用：** “美军行动”一词表明，该文件探讨了模因原理如何在军事战略、信息战，甚至可能是心理战的背景下应用、利用或理解。
*   **成长型产业（2006）：** 这表明在文件创建时，在军方内部探索模因学是一个新兴或不断扩大的重点领域。
*   **技术文档：** PDF代码的存在意味着这篇文章可能是一篇技术性或研究性的文档，其中可能包含可视化信息。

根据现有的少量数据，这篇文章最有可能讨论通过战略性地部署思想，利用模因学影响民众、对手，甚至内部军队的战略和战术可能性。

---

## 44. Espanso – 用 Rust 编写的跨平台文本扩展器

**原文标题**: Espanso – Cross-Platform Text Expander Written in Rust

**原文链接**: [https://github.com/espanso/espanso](https://github.com/espanso/espanso)

Espanso：一款跨平台文本扩展器，用Rust编写，基于关键词自动替换文本。它能节省打字时间、创建代码片段、执行自定义脚本并启用表情符号。它可在Windows、macOS和Linux上运行，并与大多数程序集成。

主要功能包括表情符号和图像支持、搜索栏、日期扩展、自定义脚本和Shell命令、特定于应用程序的配置、表单支持，以及通过软件包和内置软件包管理器(espanso hub)进行扩展。配置基于文件，并支持Regex触发器，还提供实验性的Wayland支持。

本文鼓励用户访问官方文档，加入Reddit或Discord社区获取支持，并考虑捐赠以支持进一步开发。该项目由Federico Terzi创建，采用GPL-3.0许可，并感谢开源社区以及libxdo、xclip、libxkbcommon、wl-clipboard和wxWidgets等特定库的贡献。

---

## 45. Pyrefly: 一种用于 Python 的新型类型检查器和 IDE 体验

**原文标题**: Pyrefly: A new type checker and IDE experience for Python

**原文链接**: [https://engineering.fb.com/2025/05/15/developer-tools/introducing-pyrefly-a-new-type-checker-and-ide-experience-for-python/](https://engineering.fb.com/2025/05/15/developer-tools/introducing-pyrefly-a-new-type-checker-and-ide-experience-for-python/)

Meta发布了Pyrefly的Alpha版本，这是一个用Rust开发的新开源Python类型检查器和IDE扩展。Pyrefly专为速度和可扩展性而设计，旨在将类型检查转移到每次击键时进行，即使对于大型代码库也能提供响应迅速的IDE体验。它优先考虑性能，提供高达每秒180万行代码的检查速度。

Pyrefly采用“IDE优先”的方法构建，确保IDE和命令行之间类型检查的一致性。它还具有自动类型推断功能，允许用户即使在未类型化的代码中也能受益于类型信息，并且可以通过双击插入推断的类型。

Pyrefly在MIT许可下开源，鼓励社区贡献和反馈。它旨在改进Python的类型系统和开发者体验。该项目从Meta之前的类型检查器Pyre中汲取灵感，但从头开始构建，以满足不断增长的可扩展性、代码导航和类型导出需求。

此次发布包括VSCode扩展、通过`pip install pyrefly`安装的命令行工具，并鼓励用户迁移现有配置并在GitHub上提供反馈。Meta计划在今年夏天取消Alpha标签，并寻求社区意见以完善该工具。

---

## 46. 爬树1：什么是决策树？

**原文标题**: Climbing trees 1: what are decision trees?

**原文链接**: [https://mathpn.com/posts/climbing-trees-1/](https://mathpn.com/posts/climbing-trees-1/)

关于决策树系列文章的第一篇，本文介绍了机器学习中决策树的基本概念。决策树被呈现为一系列将数据划分为区域的问题，最终在叶节点上做出预测。文章解释了决策树的结构，重点介绍了内部节点（提出问题）和叶节点（根据类别概率提供预测）。

探讨了两种主要的决策树类型：分类树（预测分类结果）和回归树（预测连续数值）。讨论了最具影响力的决策树算法，如ID3、C4.5和CART，重点介绍了CART，该系列文章将实现CART算法。

在数学上，决策树被定义为一个由区域和值组成的 piecewise 函数。一个关键特征是使用轴平行分割，这简化了计算，但也限制了模型捕捉复杂关系的能力。

然后，本文深入探讨了决策树中固有的偏差-方差权衡。较深的树往往具有高方差（过拟合），而较浅的树可能受到高偏差（欠拟合）的影响，尤其是在处理表现出加性结构、XOR关系或多路复用器问题的数据时。由轴对齐分割引起的“阶梯效应”也被认为是常见的限制。虽然决策树单独使用时存在局限性，但通过 bagging 和 boosting 在集成中使用时，它们会变得非常强大。

---

## 47. Proton威胁退出瑞士，因新监控法

**原文标题**: Proton threatens to quit Switzerland over new surveillance law

**原文链接**: [https://www.techradar.com/vpn/vpn-privacy-security/we-would-be-less-confidential-than-google-proton-threatens-to-quit-switzerland-over-new-surveillance-law](https://www.techradar.com/vpn/vpn-privacy-security/we-would-be-less-confidential-than-google-proton-threatens-to-quit-switzerland-over-new-surveillance-law)

Proton威胁离开瑞士，因拟议的监控法修正案要求VPN和消息应用保留用户数据。

---

## 48. 松鼠 (编程语言)

**原文标题**: Squirrel (Programming Language)

**原文链接**: [https://en.wikipedia.org/wiki/Squirrel_(programming_language)](https://en.wikipedia.org/wiki/Squirrel_(programming_language))

Squirrel是一种轻量级、高级、多范式（脚本、命令式、函数式、面向对象）编程语言，专为具有大小、内存带宽和实时约束的应用而设计，例如视频游戏。它由Alberto Demichelis创建，于2003年首次发布，具有动态类型、委托、类、继承、高阶函数、生成器、协程、尾递归、异常处理和自动内存管理等特性。其语法类似于C语言，并从Lua中汲取了灵感。

Squirrel已被用于各种应用程序，包括Code::Blocks IDE、Electric Imp IoT平台，以及《求生之路2》、《传送门2》、《最终幻想水晶编年史：国王之王》和《银莲公园》等游戏。它还被用于旧游戏的非官方更新，例如《神偷2》的NewDark引擎更新。

该语言以MIT许可证分发，包含一个紧凑的编译器和一个用大约7000行C++代码编写的虚拟机。其历史包括2010年从zlib/libpng许可证更改为MIT许可证，以方便在Google Code上托管。本文重点介绍了演示阶乘计算、生成器和类继承的代码示例。

---

## 49. 谷歌Logo连字错误

**原文标题**: Google Logo Ligature Bug

**原文链接**: [https://www.jefftk.com/p/google-logo-ligature-bug](https://www.jefftk.com/p/google-logo-ligature-bug)

本文讨论了Jeffrey Yasskin发现的与Google产品使用的“Google Sans”字体相关的安全漏洞。该漏洞的核心在于字体中的连字，一种将特定字母组合合并成单个字形的特性。在这种情况下，连字将字符串“googlelogoligature”渲染成与“Google”在视觉上相似的表示形式。

该漏洞的潜在危害在于恶意行为者可以注册诸如“googlelogoligature.net”之类的域名。由于连字的存在，Android上的Chrome以及可能其他Google产品可能会将此域名显示为“Google.net”，从而可能欺骗用户，让他们相信自己访问的是合法的Google网站。

作者通过建议在Google上搜索“googlelogoligature”来演示此效果，当“Google Sans”字体处于活动状态时，搜索结果会将该字符串显示为“Google”。禁用该字体会将显示恢复为原始的“googlelogoligature”。

虽然连字在排版中具有合法的用途，但在安全敏感的环境中使用它们来渲染攻击者控制的文本是有问题的。作者认为，在通用字体（尤其是用于渲染URL的字体）中包含这种特定的连字是一个糟糕的设计决策，从而创建了一个潜在的网络钓鱼漏洞。作者最初怀疑是Unicode漏洞，但发现它专门与字体的连字功能相关。

---

## 50. “流式 vs. 批处理”是一种错误的二分法，我认为它令人困惑。

**原文标题**: “Streaming vs. Batch” Is a Wrong Dichotomy, and I Think It's Confusing

**原文链接**: [https://www.morling.dev/blog/streaming-vs-batch-wrong-dichotomy/](https://www.morling.dev/blog/streaming-vs-batch-wrong-dichotomy/)

冈纳·莫林认为，传统的“流式与批处理”二分法具有误导性。他认为许多流式系统内部利用批处理进行性能优化，例如将记录分组以进行高效处理和传输，尤其是在存储/计算分离架构中。这种内部批处理通常对用户透明，并根据数据到达速率动态调整批处理大小，以实现最佳吞吐量和延迟。

莫林建议，核心区别应在于“拉取与推送”语义。拉取式系统按间隔查询数据源，可能遗漏更新和删除，而推送式（流式）系统立即接收更新，提供完整、实时的视图。流式处理提供了强大的功能，如实时数据转换和放置，但也引入了复杂性，如处理流式连接和乱序数据。

他承认，由于像分离状态后端和事务性流处理等创新，流式处理的复杂性正在改善。莫林鼓励尝试流式处理，强调许多怀疑者一旦体验到它的好处，尤其是数据新鲜度，就会接受它。最终，他表示拉取和推送方法相互补充。批处理对于回填等任务仍然有用，甚至可以暂停和恢复流式管道，以根据数据量管理成本。

---

## 51. X220 ThinkPad 是世界上最好的笔记本电脑

**原文标题**: The X220 ThinkPad Is the Best Laptop in the World

**原文链接**: [https://btxx.org/posts/x220/](https://btxx.org/posts/x220/)

本文认为联想ThinkPad X220是有史以来最好的笔记本电脑，因为它在制造质量、功能和可修复性方面都优于现代笔记本电脑。作者强调了X220坚固的构造，并指出其抗弯曲和抗损坏能力是优于更薄、更脆弱设备的主要优势。

一个关键点是X220丰富的端口，消除了对转换器的需求。作者赞扬了经典的ThinkPad键盘，包括其布局和TrackPoint。虽然承认电池寿命可能有所不同，但作者强调了可更换电池的便利性。

本文推崇X220的可修复性，强调使用标准工具和联想详细的硬件手册拆卸和更换组件的容易程度。最后，作者指出X220在二手市场上的可负担性是一个额外的好处，促进了电子垃圾的预防。虽然作者承认标题有些夸张，但他们真诚地认为X220是一款顶级笔记本电脑，因为它专注于功能、耐用性和用户控制。作者列出了其机器的规格（i7-2640M、16GB DDR3、Arch Linux/OpenBSD、1366x768分辨率）以提供背景信息。

---

## 52. 日本的IC卡既奇怪又精彩

**原文标题**: Japan's IC cards are weird and wonderful

**原文链接**: [https://aruarian.dance/blog/japan-ic-cards/](https://aruarian.dance/blog/japan-ic-cards/)

本文探讨了日本IC卡系统，特别是FeliCa技术的迷人世界。与西方NFC主流的MIFARE标准不同，日本和其他亚洲国家使用索尼开发的FeliCa，该技术以其非接触式交易中的卓越速度和效率而闻名。这使得日本车站的刷卡进出闸机比伦敦地铁等系统快得多。

作者解释了NFC技术的基础知识，重点介绍了FeliCa（NFC F型）与Oyster卡和门禁系统中使用的MIFARE（NFC A型）的不同之处。一个关键区别是，FeliCa卡直接将余额存储在卡上，而西方系统通常依赖后端服务器进行交易授权。

本文深入研究了Osaifu-Keitai（手机钱包）系统，该系统允许日本手机模拟IC卡，甚至解决了关于其与苹果和安卓设备兼容性的误解。全球所有iPhone都具备Osaifu-Keitai功能。

在安全性方面，尽管采用存储值模式，但由于其强大的加密和防克隆措施，FeliCa被认为非常安全。作者讨论了潜在的攻击途径，例如利用读卡器设备或针对自动售货机等离线终端，但最终得出结论，该系统设计良好，经受住了时间的考验。

作者最后概述了未来的想法，包括建立一个微型火车站网络，以探索交通系统背后的软件堆栈，以及研究FeliCa速度背后的物理原理，以期进一步提高NFC通信速度。

---

## 53. 墨西哥海军船只撞上布鲁克林大桥，致两人死亡

**原文标题**: Mexican Navy ship crashes into Brooklyn Bridge leaving two people dead

**原文链接**: [https://www.theguardian.com/us-news/2025/may/18/mexican-navy-ship-hits-brooklyn-bridge-during-promotional-tour](https://www.theguardian.com/us-news/2025/may/18/mexican-navy-ship-hits-brooklyn-bridge-during-promotional-tour)

墨西哥海军训练舰“夸乌特莫克”号周六晚在纽约市撞上布鲁克林大桥，造成两名海军学员死亡，另有22名船员受伤。其中11人伤势危重。该船是庆祝墨西哥独立200周年推广巡游的一部分，失去动力后撞击大桥，导致三根桅杆断裂。

碰撞发生时，数十名身着礼服的水手正在横桁上。墨西哥政府已确认伤亡情况，并向遇难者家属表示慰问，承诺调查该事件。天亮后，船只受损程度显而易见，桅杆破碎并悬挂着。

据报道，布鲁克林大桥未受损，桥上无人受伤。“夸乌特莫克”号正在进行为期254天的航行，访问15个国家的22个港口，以促进和平与友谊。目击者称，碰撞后一片混乱，有人看到一名水手从安全带上悬挂，后被救出。这艘长297英尺的训练船自1982年开始航行。

---

## 54. 丢失的Macintosh Plus日文ROM

**原文标题**: The Lost Japanese ROM of the Macintosh Plus

**原文链接**: [https://www.journaldulapin.com/2025/05/17/the-lost-japanese-rom-of-the-macintosh-plus-which-isnt-lost-anymore/](https://www.journaldulapin.com/2025/05/17/the-lost-japanese-rom-of-the-macintosh-plus-which-isnt-lost-anymore/)

皮埃尔·丹杜蒙详述了他寻找并保存难以捉摸的Macintosh Plus日文ROM的经历。这款ROM与标准的128KB版本不同，大小为256KB，并且内置了用于日语汉字的字体，专门用于Apple的日语系统KanjiTalk。

作者解释了找到该ROM的困难，因为许多来源质疑其存在或错误地认为它与标准ROM相同。最终，他找到了一块来自日本的Macintosh Plus主板，上面有正确的ROM芯片，通过黄色标签和特定的芯片参考来识别。

文章强调了由于其专有引脚排列而导致ROM转储的技术挑战。在其他人的帮助下，他成功提取了256KB的数据。

日文ROM的主要优势在于KanjiTalk的启动速度更快。在西方的Macintosh Plus上，启动KanjiTalk需要从软盘加载字体，耗时超过一分钟并消耗宝贵的RAM（113KB）。日文ROM凭借其集成的字体，可将启动时间缩短约15秒并释放该RAM。

最后，丹杜蒙描述了模拟日文ROM的挑战。标准模拟器无法识别它。他与一位开发者合作修改了MAME以支持该ROM，从而可以正确地进行模拟，并展示了缩短的启动时间和集成的字体功能。

---

## 55. Show HN: Pixelagent – 用200行代码构建你的有状态代理框架

**原文标题**: Show HN: Pixelagent – Build your Stateful Agent Framework in 200 lines of code

**原文链接**: [https://github.com/pixeltable/pixelagent](https://github.com/pixeltable/pixelagent)

Pixelagent：基于Pixeltable数据基础设施构建，是一个框架，用于构建自定义、有状态的智能体，仅需约200行代码。它提供了一个统一的接口，结合了LLM、存储和编排，使工程师能够创建具有定制内存、工具调用和其他功能的智能体应用。

主要功能包括：

*   **数据编排和存储：** 利用Pixeltable进行数据管理。
*   **多模态支持：** 处理文本、图像、音频和视频。
*   **声明式和可扩展：** 类型安全的Python框架，模型无关，并支持多个提供商（Anthropic、OpenAI、AWS Bedrock）。
*   **可观测性：** 记录消息、工具调用和性能。
*   **智能体扩展：** 支持推理、反思、记忆、知识和团队工作流。
*   **即插即用扩展：** 允许添加自定义工具、长期记忆、反思和推理能力。

该框架支持创建可分发的智能体软件包，提供了一种构建您自己的部署方法。示例展示了基本智能体的创建，添加工具（使用`yfinance`），使用Pixeltable表格进行状态管理，以及实现复杂的推理模式（如ReAct）。教程和示例涵盖基本概念、高级模式（如反思和规划）以及专门的实现。Pixelagent 旨在通过处理底层数据基础设施来简化智能体工程，使开发人员能够专注于创新。

---

## 56. 展示HN：与HN 19年的历史聊天

**原文标题**: Show HN: Chat with 19 years of HN

**原文链接**: [https://app.camelai.com/log-in?next=/hn/](https://app.camelai.com/log-in?next=/hn/)

Show HN：camelAI - 与19年Hacker News数据聊天

---

## 57. FreeBASIC是一款适用于Windows DOS和Linux的免费/开源BASIC编译器。

**原文标题**: FreeBASIC is a free/open source BASIC compiler for Windows DOS and Linux

**原文链接**: [https://freebasic.net/](https://freebasic.net/)

FreeBASIC是一款免费开源的BASIC编译器，适用于Windows、DOS和Linux系统。它被设计为与QuickBASIC兼容，允许许多较早的程序在“QB”语言模式下以最小或无需修改即可编译和运行。然而，默认的FreeBASIC模式需要对较大的程序进行更多的代码修改。

FreeBASIC是一个自托管编译器，它使用GNU binutils，并且可以创建控制台、GUI可执行文件以及动态/静态库。它拥有对C库的完全支持和对C++库的部分支持，使程序员能够使用和创建与其他语言兼容的库。功能包括一个具有多行宏、条件编译和文件包含的C风格预处理器。基准测试表明，FreeBASIC的速度与GCC等编译器相当。

该项目包括编译器（fbc）、汇编器、链接器、归档器和运行时库，包括一个图形库。它支持基于i386的架构，包括DOS、Linux、Windows和Xbox。FreeBASIC为流行的第三方库（如Allegro、SDL、OpenGL、GTK+和Windows API）提供绑定，并附带示例程序。

FreeBASIC是一种支持过程式、面向对象和元编程风格的高级语言。最初被设想为QuickBASIC的替代品，它已经发展成为一个强大的开发工具，通过更多的数据类型、语言结构、编程风格以及对现代平台和API的支持，扩展了QuickBASIC的功能。它可以用于创建各种类型的应用程序。

---

## 58. 7000万美元拍卖惨败剖析

**原文标题**: Anatomy of a $70M Auction Flop

**原文链接**: [https://www.nytimes.com/2025/05/14/arts/design/sothebys-flop-giacometti-sculptor.html](https://www.nytimes.com/2025/05/14/arts/design/sothebys-flop-giacometti-sculptor.html)

这篇文章剖析了阿尔贝托·贾科梅蒂1955年的雕塑作品《大头小像（迭戈大头像）》在苏富比现代艺术晚间拍卖会上流拍的原因，尽管其预估价超过7000万美元。这件由索洛维耶夫基金会提供的作品缺乏最低价格保证，这是已故的谢尔顿·H·索洛偏爱的策略，他更喜欢协商买家费的一部分。

拍卖师奥利弗·巴克以5900万美元起拍，但价格停滞在6425万美元。在长时间且徒劳地寻找更高出价后，该拍品被宣布流拍。专家指出，过于激进的预估价是导致流拍的主要原因。

此次流拍对苏富比现代艺术拍卖会产生了重大影响。《贾科梅蒂》的雕塑作品占拍卖会预估低价的近30%。由于该雕塑未能售出，拍卖会在扣除费用后仅产生了1.52亿美元，远低于预期。文章进一步解释说，总共有6个雕塑头像，最近一次出售是在2013年，价格约为5000万美元。索洛维耶夫基金会希望为他们的特定铸件获得7000万美元或更多，因为它也是唯一的彩绘版本。

---

## 59. 将条件判断上移，循环下移

**原文标题**: Push Ifs Up and Fors Down

**原文链接**: [https://matklad.github.io/2023/11/15/push-ifs-up-and-fors-down.html](https://matklad.github.io/2023/11/15/push-ifs-up-and-fors-down.html)

代码优化与清晰度的两条相关经验法则：“上推 If”与“下推 For”。

**上推 If：** 倾向于将条件逻辑（if 语句）移到调用函数中，而不是放在函数内部。这可以减少冗余，集中控制流，并更容易发现无效条件。具体来说，避免编写检查前提条件并在失败时“不执行任何操作”的函数；相反，应通过类型或调用方的断言来强制执行前提条件。“溶解枚举”重构是另一个例子，其中上推条件可以揭示重复的逻辑并允许简化。

**下推 For：** 拥抱批量处理。与其迭代对象集合并分别对每个对象执行操作，不如创建一个 `_batch` 函数来一次性处理整个集合。这通过分摊启动成本、允许灵活的处理顺序（包括矢量化/结构数组技巧）来提高性能，并且在涉及许多实体的热路径中尤其有益。将循环移到条件语句之外以避免重复重新评估条件这一建议也很重要。

本文强调，这些规则甚至可以组合使用，以提高代码性能和可维护性。虽然性能是“下推 For”原则的主要动机，但通过处理集合而不是单个元素，还可以提高表达性和清晰度。

---

## 60. 我如何在2013年修复Basilisk II Windows臭名昭著的“黑屏” bug

**原文标题**: How I fixed the infamous Basilisk II Windows “Black Screen” bug in 2013

**原文链接**: [https://www.downtowndougbrown.com/2025/05/how-i-fixed-the-infamous-basilisk-ii-windows-black-screen-bug-in-2013/](https://www.downtowndougbrown.com/2025/05/how-i-fixed-the-infamous-basilisk-ii-windows-black-screen-bug-in-2013/)

2013年，Doug Brown修复了Basilisk II（Windows上的68k Mac模拟器）中长期存在的“黑屏”错误。此错误会导致模拟的Mac显示黑屏而不是启动，尤其是在Vista和7等较新的Windows版本中更为常见。用户提出了各种解决方法，但只有恢复到旧的、JIT之前的Basilisk II版本才能始终有效。

Brown通过向视频代码添加调试跟踪来调查该问题。他发现由无效的68k CPU操作码（0x7119）触发的`VideoDriverControl()`函数（用于模拟器和主机之间的通信）在黑屏故障期间没有被调用。这意味着模拟的机器没有加载视频驱动程序。

根本原因追溯到Basilisk II在Windows上为RAM和ROM分配内存的方式。单独的`VirtualAlloc()`调用可能导致主机机器的ROM地址*低于*RAM地址。Basilisk II的“直接寻址”模式通过减去偏移量 (RAMBaseHost) 将主机地址转换为虚拟地址。如果ROM的主机地址低于RAM的主机地址，则生成的虚拟ROM地址将不正确，从而阻止视频驱动程序加载。

该修复方法涉及移植Unix版本的内存分配方法，该方法在单个块中分配RAM和ROM，从而保证ROM地址始终*高于*RAM地址。这确保了正确的虚拟ROM地址，解决了黑屏错误，并使Basilisk II能够可靠地工作。

---

## 61. Show HN: 我做了一个刀具钢材对比工具

**原文标题**: Show HN: I built a knife steel comparison tool

**原文链接**: [https://new.knife.day/blog/knife-steel-comparisons/all](https://new.knife.day/blog/knife-steel-comparisons/all)

这个 "Show HN" 帖子介绍了一个 New Knife Day 网站上提供的刀具钢材比较工具。该工具允许用户根据 1-10 评分的性能属性（包括耐腐蚀性、韧性、保持性及易磨性）来比较不同刀具钢材的性能。

目前，该网站拥有 150 个详细的比较，其中 147 个包含比较图表。文章列出了全面的钢材比较范围，从常见的组合（如 1095 与 5160）到更专业的对决（如 CPM 15V 与 Maxamet）。

除了比较工具外，该网站还提供诸如刀具钢材数据库和信息文章等资源。它还根据刀具的预期用途（例如，最佳口袋刀、最佳厨师刀、最佳 EDC 刀）对刀具进行分类，为不同的需求提供建议。该网站的品牌是 New Knife Day，版权声明为 2025 年。

---

## 62. 小鼠植入人类DNA片段后大脑变大

**原文标题**: Mice grow bigger brains when given this stretch of human DNA

**原文链接**: [https://www.nature.com/articles/d41586-025-01515-z](https://www.nature.com/articles/d41586-025-01515-z)

研究人员发现了一段人类DNA片段，一种名为HARE5的“基因拨盘”，它能显著增大小鼠的脑容量。通过将人类版本的HARE5插入小鼠体内，它们的脑容量比正常水平增大了约6.5%。这种效应源于HARE5增强了名为放射状胶质细胞的神经干细胞的活性，使其分裂和增殖得更多，从而导致神经元产量增加。

与之前的研究相比，该研究更深入地探讨了驱动人类大脑发育的遗传机制。它支持了人类加速区域(HARs)的观点，即人类特有的、快速进化的DNA片段在脑容量和发育中起着至关重要的作用。具体来说，HARE5增强了Fzd8基因的表达，这与该过程有关。

虽然该研究表明对脑容量有明显的影响，但脑容量的增加是否转化为小鼠认知功能或记忆的改善仍不清楚。这些发现有助于理解在进化过程中人类大脑的体积是如何比黑猩猩大三倍的，尽管完整的解释仍然难以捉摸。

---

## 63. 新型操作系统目录

**原文标题**: Catalog of Novel Operating Systems

**原文链接**: [https://github.com/prathyvsh/os-catalog](https://github.com/prathyvsh/os-catalog)

本文介绍了一系列近年来开发的新型操作系统目录，这些系统的灵感来自于超越主流操作系统范式的渴望。作者指出，人们对操作系统开发的兴趣再次高涨，让人想起商业系统占据主导地位之前的多样化操作系统格局。

该目录重点介绍了几个项目，包括：

*   **UXN/Varvara:** 100 Rabbits 的个人计算堆栈，专注于激进的愿景和有据可查的理由。

*   **Playbit:** Rasmus Andersson 及其团队为重塑计算机堆栈所做的努力。

*   **Folk.computer:** 一个专注于物理计算接口的研究项目，灵感来自 Bret Victor 的 Dynamicland。

*   **Nette.io:** Pawel Ceranka 为 Web 开发的研究型操作系统。

*   **Interim、Mezzano 和 ChrysalLisp:** 使用 Lisp 构建的最小操作系统，展示了 Lisp 对操作系统开发的吸引力。

*   **RayvnOS 和 RedoxOS** 已列出，但未进行描述。

*   **DesktopNeo:** Lennart Ziburski 对桌面界面的重新思考。

*   **MercuryOS:** Jason Yuan 基于意图的操作系统概念，发展成为 Makespace.fun → New.computer。

*   **Freeze.app:** 一个用于冻结和解冻桌面界面的应用程序。

*   **WormOS:** 一个基于分区心理空间和用于完成任务的“虫洞”的概念。

*   **Bedrock.computer:** 一个状态未知的项目。

最后，本文还提供了其他有趣操作系统列表的链接，包括 @jubalh 的 AwesomeOS 和一个 Anagora 列表。总的主题是在主流商业产品之外，操作系统开发中持续存在的创新精神。

---

## 64. 自行车载传感器或可助力绘制安全骑行路线图

**原文标题**: Bike-mounted sensor could boost the mapping of safe cycling routes

**原文链接**: [https://newatlas.com/bicycles/proxicycle-bicycle-sensor-safe-cycling-routes/](https://newatlas.com/bicycles/proxicycle-bicycle-sensor-safe-cycling-routes/)

本文介绍了华盛顿大学开发的一种新型自行车安装式近距离传感器ProxiCycle，旨在改进安全骑行路线的绘制。与目前依赖事故报告或主观骑行者反馈的地图系统不同，ProxiCycle使用红外传感器来检测和记录车辆危险地靠近骑行者（距离在1米或3.3英尺以内）的情况。该设备取代了车把堵头，通过蓝牙将数据传输到智能手机应用程序，该应用程序使用算法来识别和记录这些近距离通行。

在西雅图进行的初步测试，包括摄像头验证和一个更大的骑行者群体，证明了ProxiCycle在识别危险地点方面的准确性。15名骑行者在两个月内收集的数据，涵盖了2050次近距离通行，与已知自行车-汽车碰撞事故高发区域基本吻合，但也提供了更精确的风险测量。

目标是基于客观的传感器数据创建真实的骑行危险地图，为新手骑行者提供可靠的安全路线信息。据估计，该设备的制造成本不到25美元，使用现成的组件，电池续航时间约为12小时。研究人员计划在不同的城市进行更大规模的研究，以改进和扩展该系统。该研究最近在ACM CHI人机交互大会上发表。

---

## 65. 心脏形成瞬间首次被影像捕捉

**原文标题**: Moment of heart's formation captured in images for first time

**原文链接**: [https://www.theguardian.com/science/2025/may/13/heart-cells-mouse-embryo-science-research](https://www.theguardian.com/science/2025/may/13/heart-cells-mouse-embryo-science-research)

科学家首次利用延时摄影捕捉到心脏开始形成的瞬间。伦敦大学学院的研究人员使用先进的光片显微镜观察到小鼠胚胎在早期发育（特别是原肠胚形成期间）中，心肌细胞如何组织成类似心脏的形状。他们用荧光标记物标记心肌细胞，并每两分钟拍摄一次图像，持续40小时，从而能够追踪细胞的运动和组织。

这段影像揭示了注定要形成心脏的细胞迅速出现，并在原肠胚形成早期遵循有组织的路径，区分了那些构成心室（泵血腔室）和心房（接受血液腔室）的细胞。 这挑战了之前的理解，表明心脏命运的决定和定向细胞运动的调节比之前认为的要早得多，由确保心脏正常形成的隐藏模式所控制。

该研究结果发表在《欧洲分子生物学组织期刊》上，为先天性心脏缺陷提供了新的见解，先天性心脏缺陷影响大约百分之一的婴儿。研究人员认为，这项技术可以促进对这些缺陷的理解和治疗，并加速在实验室中培养心脏组织用于再生医学目的的进展。

---

## 66. OpenAI计划在阿布扎比建设的数据中心将比摩纳哥更大。

**原文标题**: OpenAI's planned data center in Abu Dhabi would be bigger than Monaco

**原文链接**: [https://techcrunch.com/2025/05/16/openais-planned-data-center-in-abu-dhabi-would-be-bigger-than-monaco/](https://techcrunch.com/2025/05/16/openais-planned-data-center-in-abu-dhabi-would-be-bigger-than-monaco/)

OpenAI计划在阿布扎比建设一个5吉瓦的巨型数据中心园区，规模可能超过摩纳哥，作为其与阿联酋科技巨头G42合作的“星门”项目的一部分。该设施将使OpenAI计划在得克萨斯州建设的1.2吉瓦数据中心相形见绌。

该项目反映了美国和阿联酋之间日益增长的人工智能联系，但OpenAI与G42的关系引起了美国官员的担忧，因为G42之前与包括华为和北京基因组研究所在内的中国实体存在联系。这些担忧促使G42剥离了其在华投资。

作为OpenAI的主要股东，微软已向G42投资15亿美元，进一步巩固了合作关系。阿布扎比数据中心凸显了支持日益复杂的人工智能发展所需的巨大基础设施规模，其耗电量相当于五个核反应堆。

---

## 67. 词汇宝库：探索罗杰词典 (2023)

**原文标题**: A library of words: Discovering Roget's Thesaurus (2023)

**原文链接**: [https://austinkleon.substack.com/p/a-library-of-words](https://austinkleon.substack.com/p/a-library-of-words)

无法访问文章链接。

---

## 68. 为C程序员准备的Fortran

**原文标题**: Fortran for C Programmers

**原文链接**: [https://flang.llvm.org/docs/FortranForCProgrammers.html](https://flang.llvm.org/docs/FortranForCProgrammers.html)

本文是为学习Fortran的C/C++程序员提供的快速入门指南，重点介绍基本概念并避免常见陷阱。它以“罗塞塔石碑”的形式呈现，涵盖了这两种语言在语法和术语上的主要差异。

本文重点介绍了Fortran的前向兼容性、两种源代码形式（固定格式和自由格式）、大小写不敏感以及基于隐式类型规则的可选变量声明。它解释了内置的“固有”函数以及模块对于组织代码的重要性。

介绍了关键数据类型（INTEGER、REAL、COMPLEX、LOGICAL、CHARACTER）及其“kind”参数。引入了用户定义的“派生类型”（类似于C++类）的概念，包括继承、析构函数和构造函数等特性。Fortran数组是多维的，以列优先顺序存储，默认下界为1。强调了ALLOCATABLE数据（类似于C++的`std::vector`）用于动态内存管理。

解释了Fortran的内置I/O功能，包括格式化和非格式化传输、内部I/O和文件单元号。讨论了子程序（FUNCTION和SUBROUTINE）、模块和参数传递（主要通过引用）。介绍了通过接口实现的重载和使用CLASS实现的多态。

提到了指针的作用（必须指向TARGET数据）以及缺少标准预处理。指出了Fortran的面向对象功能，特别是类似于C++成员函数的类型绑定过程。最后，本文警告了静态变量初始值设定项的陷阱以及BLOCK结构中的解释。

---

## 69. 用C++模拟1966年的约瑟夫·魏泽鲍姆的Eliza

**原文标题**: A Simulation in C++ of Joseph Weizenbaum's 1966 Eliza

**原文链接**: [https://github.com/anthay/ELIZA](https://github.com/anthay/ELIZA)

本文介绍了一个用C++重新创建的约瑟夫·魏泽鲍姆1966年ELIZA聊天机器人。作者在发现原始ELIZA源代码之前开发了这个C++版本，旨在实现一个使用原始脚本格式（S-表达式）的精确模拟。ELIZA是第一个聊天机器人，它使用模式匹配规则来反射用户输入的部分内容，从而产生一种理解的*错觉*，尽管它的机制很简单。魏泽鲍姆的目标是强调人们多么容易被误导，从而相信计算机能够理解他们。

作者在多个部分中详细介绍了该项目的开发过程，包括在发现原始ELIZA代码后所做的更改，以及对HASH函数的讨论。文章还提到了一个与作者的儿子一起创建的JavaScript版本的ELIZA，以及为在ASR 33电传打字机上运行而进行的串行I/O适配。作者参与证明了1966年的原始ELIZA是图灵完备的，并提供了ELIZA脚本和其他相关资源的链接，包括Jeff Shrager的elizagen.org。作者还在为一本关于ELIZA的书做贡献。文章包括关于如何在符合POSIX标准的系统（如macOS）和Windows上构建和运行C++ ELIZA代码的说明。

---

## 70. Xata：可扩展的Postgres，具备写时复制分支和匿名化功能

**原文标题**: Xata: Postgres at scale, with copy-on-write branching and anonymization

**原文链接**: [https://xata.io/blog/xata-postgres-with-data-branching-and-pii-anonymization](https://xata.io/blog/xata-postgres-with-data-branching-and-pii-anonymization)

Xata 重磅回归，打造“大规模 Postgres”平台，解决团队在大型组织中使用 Postgres 时面临的技术和组织扩展挑战。它提供写时复制分支、数据匿名化以避免开发环境中暴露 PII，以及云无关的部署选项，包括在您自己的云或本地运行。

主要特性包括：

*   **写时复制分支：** 快速高效地创建具有生产环境数据的开发和预发布环境。
*   **数据匿名化：** 确保敏感数据被屏蔽，防止合规性问题和开发者暴露。
*   **零停机模式变更：** 集成 `pgroll` 以实现可逆模式更新。
*   **存储/计算分离：** 使用 Simplyblock 的分布式存储系统（NVMe/TCP）实现独立扩展、高可用性和成本优化。
*   **Postgres 兼容性：** 运行原生 Postgres，确保 100% 兼容扩展和工具。
*   **自带云 (BYOC)：** 可选择在您自己的云帐户中部署 Xata，以增强安全性、合规性和降低延迟。
*   **Xata Agent：** 一款由 LLM 驱动的 Agent，通过分析指标、日志和查询来帮助优化 Postgres 实例。

Xata 提供了一种经济高效的替代方案，可替代 Amazon Aurora 等服务，潜在地降低高达 80% 的成本。该平台与其之前的产品（现在称为 Xata Lite）分离，后者仍然是一个简单的、无服务器的 Postgres 选项，并提供慷慨的免费套餐。目前，对新 Xata 平台的访问受到限制，鼓励感兴趣的用户申请访问。

---

## 71. ARMv9架构助力Arm创下新的财务高度

**原文标题**: ARMv9 Architecture Helps Lift Arm to New Financial Heights

**原文链接**: [https://www.nextplatform.com/2025/05/12/armv9-architecture-helps-lift-arm-to-new-financial-heights/](https://www.nextplatform.com/2025/05/12/armv9-architecture-helps-lift-arm-to-new-financial-heights/)

Arm Holdings营收创历史新高，得益于Armv9架构的应用及超大规模企业和云服务提供商对基于Arm的CPU使用增加。Armv9架构的专利许可费高于以往，对这一财务成功贡献巨大。在2025财年，Arm的销售额首次超过40亿美元，专利许可收入首次超过20亿美元，其中第四季度营收超过10亿美元。

具体而言，尽管芯片出货量仅增长2%，但智能手机芯片专利许可费在本季度增长了30%，凸显了更高Armv9专利许可费的影响。超大规模企业越来越多地选择Arm用于AI云部署，英伟达、谷歌和微软均大量采用。值得注意的是，过去两年中，超过50%的AWS新增CPU容量基于Arm。

在2025财年第四季度，专利许可收入达到6.07亿美元（同比增长18.1%），而许可和其他收入飙升至6.34亿美元（同比增长53.1%）。Arm第四季度总营收为12.4亿美元，增长33.7%。尽管研发支出有所下降，但营业收入却大幅增长。虽然净利润因股权投资损失而下降，但其基本表现反映出强劲的增长。

据估计，Armv9的专利许可费贡献略低于30%，而Armv8则占近50%。虽然云和网络目前仅占专利许可收入的一小部分（估计为15-20%），但预计将显著增长。在2025财年，Arm合作伙伴出货了306亿颗芯片，自公司成立以来总计达到3100亿颗，巩固了Arm作为全球最普及CPU架构的地位。

---

## 72. 韩文编码

**原文标题**: Encoding Hangeul, Koreas writing system

**原文链接**: [https://brookjeynes.dev/posts/unicode-hangeul/](https://brookjeynes.dev/posts/unicode-hangeul/)

本文探讨了韩文（朝鲜语文字系统）在 Unicode 中的编码。韩文于 1443 年创立，使用类似于字母的字母（Jamo）来构成音节。虽然有超过 11,000 种可能的音节组合，但学习韩文只需要掌握 68 个字母及其组合规则。

本文解释了通用字符编码标准 Unicode 如何表示韩文。一个韩语音节包含一个声母（lead consonant）、一个韵母（medial vowel）和一个可选的韵尾（tail consonant）。 Unicode 有两个字母区：用于单个字母的“韩文 Jamo”区和通常呈现更清晰的“韩文兼容 Jamo”区。

至关重要的是，Unicode 还定义了一个“韩文音节”区 (U+AC00 到 U+D7A3)，表示 Jamo 的每种预组合，从而能够直接编码韩语音节。本文详细介绍了一个公式，可以根据韩文字符的 Jamo 成分计算其 Unicode 值，反之亦然。此公式涉及使用声母、韵母和韵尾的规范顺序号，以及特定于韩文音节区的常量。本文还涉及了废弃的 Jamo 以及它们如何在 Unicode 中通过组合处理，因为没有定义预组合形式。

---

## 73. 让AI写出好的SQL

**原文标题**: Getting AI to write good SQL

**原文链接**: [https://cloud.google.com/blog/products/databases/techniques-for-improving-text-to-sql](https://cloud.google.com/blog/products/databases/techniques-for-improving-text-to-sql)

让AI编写高质量SQL：Google Cloud的文本到SQL技术探索

---

## 74. 实现RISC-V虚拟机监控器

**原文标题**: Implementing a RISC-V Hypervisor

**原文链接**: [https://seiya.me/blog/riscv-hypervisor](https://seiya.me/blog/riscv-hypervisor)

本文详细介绍了作者构建名为 Starina 的 RISC-V 虚拟机监控器的过程，该监控器采用类似于 WSL2 的轻量级 VM 方法，以实现无缝的 Linux 集成。 作者利用 RISC-V H 扩展进行硬件辅助虚拟化，类似于 Intel VT-x。 QEMU 模拟 RISC-V H 扩展的能力对于测试和调试至关重要。

该实现过程分步描述如下：

1. **进入访客系统:** 设置 `hstatus.SPV` 位以进入 VS 模式。
2. **首次 ecall:** 设置访客系统的页表 (使用 Sv39x4) 以执行一个简单的 `ecall` 指令。
3. **Hello World:** 在访客系统中运行一个基本的汇编程序，利用 SBI (RISC-V 的 BIOS 接口) 进行输出。
4. **启动 Linux:** 构建一个具有特定配置 (如 `CONFIG_SERIAL_EARLYCON_RISCV_SBI` 等) 的 RISC-V Linux 内核。
5. **设备树:** 使用 `vm-fdt` crate 创建一个设备树，以定义可用的设备，例如内存和 CPU。
6. **rdtime 支持:** 启用 `hcounteren` CSR，以便访客系统可以读取计时器。
7. **定时器支持:** 实现定时器中断注入，利用 `sstc` 扩展，这需要理解 RISC-V 的中断架构。
8. **MMIO 支持:** 通过处理访客系统页面错误并使用 `htinst` CSR 解释指令来模拟内存映射 I/O (MMIO)。 重要的考虑因素包括 `htval` 中的地址偏移和压缩指令。
9. **virtio-fs:** 选择 virtio-fs 作为根文件系统，以实现 Starina 和访客 Linux 之间的无缝集成，并利用 FUSE。

文章最后强调了由于 Starina 的 Unikernel 式模式，能够使用 GDB 同时调试虚拟机监控器和访客内核。

---

## 75. 爆米花：在WASM中运行Elixir

**原文标题**: Popcorn: Run Elixir in WASM

**原文链接**: [https://popcorn.swmansion.com/](https://popcorn.swmansion.com/)

Popcorn是一个允许在Web浏览器中使用WebAssembly (WASM)运行Elixir代码的库。它利用编译成WASM的AtomVM运行时，在客户端执行Elixir字节码，从而实现Elixir和JavaScript之间的交互。

要开始使用，用户需要在他们的Elixir项目中添加Popcorn作为依赖项，并使用 `mix popcorn.build_runtime` 生成一个JavaScript运行时环境。这个环境包括必要的JS库、WASM文件和一个生成的应用程序包。通过初始化Popcorn的JavaScript代码建立通信，设置标准输出/错误的处理器。Elixir应用程序定义一个带有 `start/0` 函数的入口点模块，该函数通过 `Wasm.send_elixir_ready/1` 通知JavaScript端初始化已完成。

核心交互围绕JavaScript中的 `Popcorn` 类和Elixir中的 `Popcorn.Wasm` 模块展开。JavaScript可以使用 `call` 和 `cast` 方法将消息发送到Elixir进程。Elixir进程可以通过 `run_js` 调用JavaScript函数、操作DOM和注册事件监听器来做出响应。

虽然功能强大，但由于Popcorn依赖于AtomVM，而AtomVM缺乏完整的OTP支持，尤其是在标准库NIF中，因此它具有局限性。对大整数和位串的支持也不完整。由于序列化限制，用于处理JavaScript值的API是基于引用的。

在底层，Popcorn使用一个iframe来隔离WASM运行时，并通过 `postMessage()` 进行通信。使用自定义的修补机制来调整Elixir/Erlang标准库以适应AtomVM。JSON序列化用于Elixir和JavaScript之间的数据交换。

---

## 76. 微软裁员：软件工程师成重灾区

**原文标题**: Microsoft winnows: Layoffs hit software engineers hard

**原文链接**: [https://www.theregister.com/2025/05/16/microsofts_axe_software_developers/](https://www.theregister.com/2025/05/16/microsofts_axe_software_developers/)

微软近期大幅裁员，其中软件工程师受到的影响尤为严重。被裁人员包括迈克·德罗埃特博姆（CPython核心开发者）、罗恩·巴克顿（TypeScript开发者）和马特·波德维索克（Azure SDK）等知名人士。裁员影响了Faster CPython项目，导致其被取消。

虽然微软声称裁员是为了“更好地让公司取得成功”，但大量软件开发人员被裁引发了人们对人工智能正在发挥作用的猜测。 微软首席执行官萨蒂亚·纳德拉此前曾表示，微软30%的代码由人工智能编写，而Meta首席执行官马克·扎克伯格也暗示了他的公司也会有类似的未来。

然而，文章还指出了其他潜在因素，例如微软对人工智能数据中心的大规模投资，这可能会影响工资预算。文章还提到工作岗位可能转移到海外，以及一些公司通过使用人工劳动来虚报人工智能自动化的案例。更具讽刺意味的是，微软初创企业人工智能主管加布里埃拉·德·奎罗兹也在被裁之列。 文章总结说，裁员的原因可能是复杂且多方面的，而不仅仅归因于人工智能。

---

## 77. 首例个性化基因编辑疗法治愈婴儿

**原文标题**: Baby is healed with first personalized gene-editing treatment

**原文链接**: [https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html](https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html)

凯尔和妮可·穆尔多恩夫妇的宝宝KJ出生后不久就被诊断出患有罕见的遗传疾病CPS1缺陷，这种疾病的发病率仅为百万分之一点三，通常会导致严重的生长发育迟缓、需要肝移植或在出生后第一周内死亡。面对严峻的预后，穆尔多恩夫妇决定采取积极治疗，尽管他们被建议接受舒缓疗护。

KJ成为了首位接受定制基因编辑疗法以修复其特定突变的患者。费城儿童医院的医生专门为他定制了输液方案。在9个半月大时，KJ的生长发育进展表明该疗法正在起作用，与最初的预后相比，前景大为改善。这次成功的治疗标志着个性化医疗领域的一个重要里程碑，并为其他患有罕见遗传疾病的患者开启了类似的基因编辑疗法的大门。

---

## 78. JavaScript 的新超能力：显式资源管理

**原文标题**: JavaScript's New Superpower: Explicit Resource Management

**原文链接**: [https://v8.dev/features/explicit-resource-management](https://v8.dev/features/explicit-resource-management)

显式资源管理提案引入了一种确定性的 JavaScript 资源生命周期管理方法，从而增强了代码的健壮性、性能和可维护性。主要特性包括：

*   **`using` 和 `await using` 声明：** 这些声明在资源超出作用域时自动调用资源的 `[Symbol.dispose]()` (同步) 或 `[Symbol.asyncDispose]()` (异步) 方法，防止资源泄漏。它们可以用于块、for 循环和函数体内部，但不能用于顶层作用域。

*   **`[Symbol.dispose]()` 和 `[Symbol.asyncDispose]()`：** 这些符号分别定义了同步和异步资源的清理操作。

*   **`DisposableStack` 和 `AsyncDisposableStack`：** 这些基于堆栈的容器允许对多个资源进行分组和协调释放，通过逆序释放确保对依赖关系的正确处理。 `use()`、`adopt()`、`defer()` 和 `move()` 等方法有助于管理堆栈中的资源，而 `dispose()` 或 `asyncDispose()` 则会触发清理。

*   **`SuppressedError`：** 这种新的错误类型解决了资源释放期间发生错误，可能掩盖现有错误的情况。它包含主错误和被抑制的释放错误。

该提案提供了一种结构化的资源管理方法，例如管理 `ReadableStreamDefaultReader` 实例，其中 `using` 确保始终调用 `reader.releaseLock()`，即使在错误情况下也是如此。 显式资源管理已在 Chromium 134、V8 v13.8 和 Firefox 134 中提供，并提供 Babel 支持。

---

## 79. 铸造厂 (YC F24) 招聘 – 创始工程师 (机器学习 × 软件工程师)

**原文标题**: Foundry (YC F24) Is Hiring – Founding Engineer (ML × SWE)

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe](https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe)

Foundry (YC F24) 招募创始工程师（机器学习 × 软件工程师），构建浏览器代理的核心基础设施，超越简单的 GPT 封装，打造专门构建的“世界模型”。该公司由前 Scale AI 和 Meta 员工创立，旨在解决当前浏览器代理在自动化基于浏览器的 workflow 中的不可靠性问题，这是一个巨大的、尚未开发的经济机会。

Foundry 正在创建专注于以下方面基础设施：超逼真的 Web 模拟、全面的标注框架、可靠的基准测试以及强大的强化学习训练环境。该职位适合具备扎实软件工程技能（Python、TypeScript）和实际机器学习经验的工程师，他们热衷于从头开始构建核心机器学习系统和强化学习基础设施。理想的候选人将拥有快速交付项目的良好记录、开源贡献或相关出版物。具有强化学习代理、浏览器自动化工具（Puppeteer、Playwright）或评估工具经验者优先。

Foundry 提供早期股权、具有竞争力的薪酬和高增长轨迹。他们正在构建基础性人工智能基础设施，这将对下一代浏览器代理至关重要。他们的端到端评估和训练平台允许团队大规模地测试、基准测试和优化浏览器自动化模型，利用确定性的 Web 模拟、实时 Web 评估、自动标注和标记以及强化学习驱动的代理优化。

---

## 80. 美国宇航局观测到火星上首次可见光极光

**原文标题**: NASA Observes First Visible-Light Auroras at Mars

**原文链接**: [https://www.jpl.nasa.gov/news/nasa-observes-first-visible-light-auroras-at-mars/](https://www.jpl.nasa.gov/news/nasa-observes-first-visible-light-auroras-at-mars/)

2024年3月，NASA的“毅力号”火星车首次拍摄到火星表面绿色极光的可见光图像，由MAVEN任务确认。 这一现象是由太阳耀斑和日冕物质抛射（CME）引发的，将太阳高能粒子（SEPs）射向火星。

与受全球磁场影响的地球极光不同，火星经历的是太阳高能粒子（SEP）极光。 当来自太阳的高能粒子轰击火星大气层时，就会发生这种现象，使其发光。 虽然MAVEN此前从轨道上观测到紫外光下的SEP极光，但“毅力号”的观测标志着首次从地面上看到这种可见光现象。

成功离不开精确的协调。 研究人员对“毅力号”仪器的最佳观测角度进行了建模，而NASA的“月球到火星空间天气分析办公室”和“社区协同建模中心”的团队预测了CME的影响。 加州大学伯克利分校的克里斯蒂娜·李收到了来自M2M办公室的警报，使“毅力号”和MAVEN团队能够为该事件做好准备。

在极光观测期间，MAVEN的SEP仪器和ESA的“火星快车”任务证实了SEP的存在。 捕获的极光显示出在557.7纳米波长下的均匀绿色发射，与地球的绿色极光相同，这表明未来的宇航员有可能目睹类似的景象。 这些发现为极光研究提供了一个新的途径，对于NASA为未来人类任务做准备，了解火星环境至关重要。

---

## 81. OBNC – Oberon-07 编译器

**原文标题**: OBNC – Oberon-07 Compiler

**原文链接**: [https://miasap.se/obnc/](https://miasap.se/obnc/)

OBNC是Oberon编程语言（特指2016版本）的编译器。它将Oberon源代码转换为C代码，然后使用系统的C编译器进行编译。`obnc`命令可以自动执行此过程，处理重新编译的依赖关系。

该编译器在GNU GPL许可下发布，允许免费使用和修改，而库则采用Mozilla公共许可证，为使用OBNC的Oberon项目提供了更大的灵活性。

该发行包包括编译器、构建工具、文档生成器、一个基本库和一个扩展库（`ext`），其中包含用于命令行参数、错误输出、数字转换和陷阱处理的功能。它可以作为源代码（obnc_0.17.2.tar.gz）或Windows的预编译版本（obnc_0.17.2_win32.zip）下载。源代码版本需要Boehm-Demers-Weiser垃圾回收器（GC）。以前的OBNC版本可能需要使用此版本重新编译（首先删除.obnc目录）。

还提供适用于Gedit/Pluma的文本编辑器扩展，包括语法高亮和自动大小写转换。该网站提供文档、常见问题解答、文章和学习Oberon的书籍推荐。如需支持，用户可以联系作者或使用Stack Overflow、ETHZ Oberon邮件列表或comp.lang.oberon新闻组。该网站不使用Javascript和Cookie。

---

## 82. 大型语言模型比受激励的人类说服者更具说服力

**原文标题**: LLMs are more persuasive than incentivized human persuaders

**原文链接**: [https://arxiv.org/abs/2505.09662](https://arxiv.org/abs/2505.09662)

大型语言模型比受激励的人类说服者更具说服力
        
 这篇 arXiv 论文《大型语言模型比受激励的人类说服者更具说服力》探讨了前沿大型语言模型 (LLM) Claude Sonnet 3.5 相对于人类的说服能力。 该研究采用互动式实时对话测验设置，参与者（测验参与者）受到人类或 LLM 说服者的影响，以选择正确或错误的答案。

关键发现是，**LLM 说服者在他们的说服尝试中表现出比受激励的人类说服者更高的服从性。** 这意味着 LLM 在说服测验参与者方面更成功，无论是真实地（指向正确答案）还是欺骗性地（指向错误答案）。

此外，该研究发现 LLM 直接影响了测验参与者的准确性和收益。 当 LLM 指导向正确答案时，准确性和收益增加； 相反，当他们指导向错误答案时，准确性和收益下降。

作者得出的结论是，**即使在人类受到经济激励以表现良好时，LLM 已经表现出比人类更强的说服能力。** 作者强调，鉴于人工智能快速发展的说服能力，迫切需要建立人工智能的对齐和治理框架。 这项研究由 Philipp Schoenegger 和其他 38 位作者进行，并于 2025 年 5 月 14 日提交。

---

## 83. 计算几何中的未解难题

**原文标题**: Open Problems in Computational geometry

**原文链接**: [https://topp.openproblem.net/](https://topp.openproblem.net/)

开放问题项目 (TOPP) 是一个计算几何及相关领域未解问题集，始于 2001 年。最初发布时包含 30 个问题，现已扩展到 75 个以上。虽然不再鼓励提交新的问题，但非常鼓励通过 Github Pull Requests 更新现有问题，特别是解决方案或部分解决方案。

问题按数字编号组织并分类，以便于浏览。类别包括排列、美术馆问题、着色、组合几何、凸包、数据结构、Delaunay 三角剖分、解剖、折叠与展开、几何图、图绘制、图、线性规划、下界、网格划分、最小生成树、数值计算、优化、 packing、划分、平面图、点集、多边形、多面体、重建、机器人学、调度、最短路径、简化、稀疏化器、刺穿、旅行商、三角剖分、可见性和 Voronoi 图。

该项目旨在为研究人员提供资源，突出具有挑战性的领域并促进计算几何领域的进展。可以通过数字列表、分类列表或单个 PDF 文件访问这些问题及其分类。该项目最初由 NSF 拨款支持。

---

## 84. Climeworks的碳捕获未能抵消其自身排放

**原文标题**: Climeworks' capture fails to cover its own emissions

**原文链接**: [https://heimildin.is/grein/24581/](https://heimildin.is/grein/24581/)

海米尔丁报：Climeworks碳捕获业务远未达标，涉嫌虚假宣传

本文调查了Climeworks公司，该公司因直接从大气中捕获碳而备受赞誉。调查显示，Climeworks在冰岛的业务表现远低于预期，未能实现预计的碳捕获目标，甚至未能抵消自身的排放。

自2021年以来，Climeworks在冰岛仅捕获了2400多个碳单位，远低于其声称的12000个。2023年，其运营排放了1700吨二氧化碳，超过了其捕获率。“逆戟鲸”（Orca）机器的糟糕表现导致了140万美元的折旧。尽管预计产量是“逆戟鲸”自2021年以来产量的九倍，但较新的“猛犸”（Mammoth）工厂在运营的头十个月仅捕获了105吨二氧化碳。

该公司在冰岛的财务状况也岌岌可危，2023年负债权益接近3000万美元，依赖其瑞士母公司的资金支持。尽管Climeworks拥有雄心勃勃的未来目标，并获得了大量投资和拨款，但该公司仍在努力实现其目标，并面临对其技术是“骗局”的批评。

购买了碳信用额的客户，例如Michael de Podesta，表达了失望和怀疑，因为按照目前的捕获率，收到这些信用额的等待时间可能会从几年延长到几十年。文章最后强调了Climeworks转向强化风化这一有争议的方法，表明该公司最初的碳捕获方法并未达到预期效果。

---

## 85. 网络电话簿

**原文标题**: Internet Phone Book

**原文链接**: [https://internetphonebook.net](https://internetphonebook.net)

《互联网电话簿》创刊号已发行。这本年度出版物探索诗意网络，收录了设计师、开发者、作家、策展人和教育者的文章、随笔以及个人网站目录。

创刊号在网上开售后24小时内售罄，但在指定书店、社区空间和图书馆仍有售。该出版物正在通过巡回活动推广这本书，包括计划于2025年5月在鹿特丹和雅典，以及2025年6月在首尔举办的活动。感兴趣者可以联系组织者主办自己的活动或在商店里销售这本书。

《互联网电话簿》可在Are.na的礼品店以及Adad Books（雅典）、Supertime Books（哥本哈根）、Pro qm（柏林）、San Seriffe（阿姆斯特丹）和Birdcall（首尔）等实体店购买。未来刊物也提供赞助机会。该出版物还有一个邮件列表用于接收更新信息。

---

## 86. Show HN: Merliot – 将物理设备接入大型语言模型

**原文标题**: Show HN: Merliot – plugging physical devices into LLMs

**原文链接**: [https://github.com/merliot/hub](https://github.com/merliot/hub)

Merliot Hub：一个 AI 集成的设备中心，允许用户通过 Claude 或 Cursor 等 LLM 主机，使用自然语言控制和交互自制物理设备。与典型的智能家居设备不同，Merliot Hub 专注于树莓派和 Arduino 等爱好者组件构建的设备，需要创客级别的技能。该中心提供设备固件和说明，无需用户编写软件。

主要功能包括通过分布式架构侧重隐私，用户安装和维护自己的中心和设备，防止第三方访问数据。它通过 Web 应用程序访问，无需手机应用程序。该中心充当模型上下文协议 (MCP) 服务器，促进与 LLM 的通信以实现自然语言控制。

Merliot Hub 采用 Docker 封装，便于在本地机器或云端部署，Koyeb 提供免费 VM 用于云托管。支持的设备使用 Raspberry Pi、Arduino Nano、Adafruit PyPortal、Koyeb (云) 或 Linux x86-64 平台构建。提供快速入门指南，用于通过 Docker 安装、云部署或从源代码运行。该项目鼓励贡献和设备共享。

---

## 87. Hacker News 反付费墙

**原文标题**: Hacker News Anti-Paywall

**原文链接**: [https://greasyfork.org/en/scripts/452024-hacker-news-anti-paywall](https://greasyfork.org/en/scripts/452024-hacker-news-anti-paywall)

本文简述“Hacker News 反付费墙”用户脚本，主要指导读者如何安装该脚本，并反复强调必须在浏览器中安装用户脚本管理器扩展，例如：

*   Tampermonkey
*   Greasemonkey
*   Violentmonkey
*   Userscripts

核心信息是用户需要这些扩展之一才能安装和使用反付费墙脚本。

---

## 88. 土卫六泰坦天气预报

**原文标题**: Weather Report from Saturn's Moon Titan

**原文链接**: [https://www.sci.news/astronomy/titan-weather-13907.html](https://www.sci.news/astronomy/titan-weather-13907.html)

詹姆斯·韦伯太空望远镜和凯克II望远镜的最新观测揭示了土卫六泰坦星天气和大气化学的新见解。天文学家已在泰坦星北半球探测到云对流的证据，那里集中了它的大部分甲烷和乙烷湖泊和海洋。这是首次在该区域观测到对流，表明这些湖泊的蒸发可能是甲烷的重要来源。

泰坦星与地球的水循环不同，它经历的是甲烷循环。甲烷从地表蒸发，形成云，然后以降雨形式落下。观测捕捉到云层上升到更高的高度，表明了这种对流过程。这些观测是在泰坦星北半球夏季末进行的，这是卡西尼-惠更斯号任务之前未曾观测到的时期。

此外，詹姆斯·韦伯太空望远镜的数据首次明确探测到泰坦星大气中的甲基自由基（CH3）。该分子是甲烷被阳光或高能粒子分解的关键中间体。它的探测使科学家能够观察到化学反应的进行过程，而不仅仅是看到反应的起始成分和最终产物。

这些发现意义重大，因为甲烷是泰坦星大气及其有机化学的重要组成部分，正在被消耗。甲基自由基的发现阐明了甲烷分解成其他有机分子的过程，从而有助于生命组成部分的构建。如果甲烷没有得到补充，泰坦星最终可能会变成一个没有空气的尘土和沙丘世界。该研究强调需要进一步探索泰坦星，以了解其复杂的大气动力学和有机化学，这可能为生命的起源提供见解。

---

## 89. 内核开发者玩转Home Assistant

**原文标题**: A kernel developer plays with Home Assistant

**原文链接**: [https://lwn.net/SubscriberLink/1017720/7155ecb9602e9ef2/](https://lwn.net/SubscriberLink/1017720/7155ecb9602e9ef2/)

内核开发者Jonathan Corbet在LWN.net的文章中分享了他使用Home Assistant (HA) 一年的感受。他认为HA的本地控制、自由软件方法是云端自动化的一种替代方案，很有价值。

他指出，虽然Nabu Casa公司雇佣了关键开发者，并提供远程访问的订阅服务，但HA表现出健康开源项目的特征。它拥有庞大的贡献者群体，一份源自内核的贡献者许可协议，并且责任已转移到Open Home Foundation。

HA的安装不像典型的Linux应用程序那样简单，通常需要专用计算机或Home Assistant操作系统。集成对于将HA连接到设备至关重要，虽然有些是捆绑的，但许多来自Home Assistant Community Store (HACS)。虽然集成旨在实现本地控制，但通常需要云连接，并且供应商支持各不相同，有些甚至表现出敌意。

Corbet强调安全是一个问题，因为HA在家庭网络中扮演着核心角色。该项目制定了安全策略并发布了安全公告，但第三方集成可能存在漏洞。

设置和配置HA需要大量的调整，特别是传感器和仪表板。自动化和场景提供了更高级的功能，但需要进一步配置。尽管需要付出最初的努力，但配置良好的HA可以提供有价值的信息和控制。

总而言之，Corbet认为HA是一个强大的开放平台，使用户能够控制自己的家和数据，并提供一种替代依赖云系统的方案。后续文章将深入探讨实际应用。

评论者gerdesj建议使用Node-RED集成来实现高级自动化，并强调在Debian上以“Supervised”模式运行HA的灵活性。他还强调了各种工具和集成的可用性，例如ESPHome、Frigate以及ZWave和Zigbee的集成，这证明了该平台广泛的功能。

---

## 90. 关于思考的思考

**原文标题**: Thoughts on thinking

**原文链接**: [https://dcurt.is/thinking](https://dcurt.is/thinking)

2025年5月16日的一篇博文中，作者探讨了人工智能对其创作和智力过程的影响。他们描述了一种日益增长的不安感，认为人工智能生成完全理性且经过研究的思想的能力，使其自身的努力变得徒劳，并削弱了创作的乐趣。作者感叹自身思维系统的萎缩，注意到直觉、才智和智力严谨性的下降。

此前，作者通过写作来发展思想，享受这种缓慢而细致的过程，认为它能促进更深入的理解和智力增长。现在，人工智能提供了即时、润色的输出，绕过了探索、不确定性和内在辩论的关键旅程。虽然人工智能提供信息并回答问题，但它无法提供通过原创思想获得的有意义的、内在化的知识。

作者最初将人工智能视为增强其思维的工具，但现在担心它更像是智力麻醉。他们认识到，与从头开始建立理解所带来的深度学习相比，从人工智能输出中学习是肤浅的。尽管获得信息的途径增加了，但他们感到因依赖人工智能生成的想法而变得智力迟钝。作者总结说，虽然人工智能可能提供更有效率和更雄辩的替代方案，但人类表达行为仍然具有价值。该帖子强调，它完全由人类撰写，没有人工智能的帮助。

---

## 91. 盖尔·惠灵顿，Commodore软件产品经理及“CDTV之母”，去世

**原文标题**: Gail Wellington, Commodore Software Prod Mgr "and Mother of CDTV", Has Died

**原文链接**: [https://www.legacy.com/us/obituaries/name/gail-wellington-obituary?id=58418580](https://www.legacy.com/us/obituaries/name/gail-wellington-obituary?id=58418580)

盖尔·P·惠灵顿，享年85岁，宾夕法尼亚州利默里克居民，于2025年5月14日去世。她于1940年1月14日出生于纽约州扬克斯，在纽约州尤蒂卡长大，并居住于新英格兰各地。她获得了东北大学机械工程理学学士学位，并在科技行业取得了成功的职业生涯，晋升为Commodore Computers的副总裁。她还共同拥有一家名为Three Peas and A Pod Florists的花店。退休后，她通过商会、“艺术走进学校”、“艺术融合”和其他组织，将时间奉献给社区活动。

盖尔热爱艺术、绘画、编织和园艺。她以富有同情心和智慧著称，指导了许多人。她的子女，Chandler Withington Jones III（丽莎）和 Heidi Gail (Jones) Swartz（肖恩）；她的妹妹，朱迪思·惠灵顿；以及她的孙辈，尼古拉斯、萨曼莎、杰西、帕特里克和凯特琳幸存于世。她的父母和哥哥约翰·罗伯特“杰克”·惠灵顿在她之前去世。

生命纪念会将于2025年5月21日在宾夕法尼亚州波茨敦举行。纪念捐款可捐赠给波茨敦艺术融合或艺术走进学校。葬礼由凤凰城的R. Strunk殡仪馆负责安排。

---

## 92. Codex研究预览

**原文标题**: A Research Preview of Codex

**原文链接**: [https://openai.com/index/introducing-codex/](https://openai.com/index/introducing-codex/)

提供的URL链接到一个OpenAI的博客文章，介绍了Codex，一种将自然语言翻译成代码的新型AI系统。Codex驱动GitHub Copilot，代表了AI理解和生成代码能力的一项重大进步。

文章的主要观点是Codex极大地简化了编写软件的过程。用户可以用简单的英语描述他们希望程序做什么，Codex通常可以自动生成相应的代码。这降低了编程的入门门槛，并允许经验丰富的程序员专注于更高级别的任务。

关键信息包括：

*   **Codex理解自然语言指令：** 它可以解释人类语言，并将其翻译成各种编程语言（尤其是Python）中的可用代码。
*   **Codex驱动GitHub Copilot：** 这表明该技术已足够成熟，可以用于实际应用，并已集成到流行的开发者工具中。
*   **Codex可以处理复杂的任务：** 文章中的示例演示了它仅基于自然语言描述创建功能性网站、简单游戏，甚至实现复杂算法的能力。
*   **提高生产力的潜力：** 文章强调Codex可以加速软件开发，使开发人员能够更快、更高效地构建应用程序。
*   **早期研究阶段：** 虽然功能强大，但Codex仍处于研发阶段，表明正在不断努力提高其能力和可靠性。

---

## 93. 风帆冲浪SWE-1：我们的首款前沿型号

**原文标题**: Windsurf SWE-1: Our First Frontier Models

**原文链接**: [https://windsurf.com/blog/windsurf-wave-9-swe-1](https://windsurf.com/blog/windsurf-wave-9-swe-1)

这是一个非常简短的文本片段，因此简短的总结将很简洁：

文本介绍了“Windsurf SWE-1”，作为该公司的首个“前沿型号”。 它暗示了关于这些型号的更多信息和更新可以通过及时了解Windsurf的新闻来找到。 核心信息是推出一个新的产品线或举措。

---

## 94. 第二章：可串行化理论（1987年并发控制书籍）

**原文标题**: Chapter 2: Serializability Theory (1987 Concurrency Control Book)

**原文链接**: [http://muratbuffalo.blogspot.com/2025/05/chapter-2-serializability-theory.html](http://muratbuffalo.blogspot.com/2025/05/chapter-2-serializability-theory.html)

本文总结了“数据库系统中的并发控制和恢复”(1987)一书的第二章，该书是可串行化理论的奠基性著作。该章严谨地构建了该理论，从事务操作（读、写、提交、中止）作为偏序关系的历史定义开始。这些操作的建模方式只捕获依赖关系，忽略值和其他调度器不可见的数据。

核心概念是可串行化：当并发执行等价于串行执行时。该章介绍了序列化图（SG），其中节点是已提交的事务，边代表冲突（例如，写-读依赖）。关键结果，即可串行化定理，指出一个历史是可串行化的，当且仅当其序列化图是无环的。这归功于吉姆·格雷1975年的IBM报告。

然后，本章讨论了存在故障时的可恢复性，定义了可恢复（RC）、避免级联中止（ACA）和严格（ST）历史，并概述了它们的包含层次结构。

通过重新定义冲突的概念，该理论被推广到读取和写入之外的操作（例如，递增、递减），从而为研究更一般的可交换性（CRDT）打开了大门。

最后，介绍了视图可串行化（VSR），这是一种基于观察一致性的更宽松的等价性。尽管VSR是NP完全的并且被认为对调度器来说不切实际，但VSR对观察到的值的关注在定义分布式系统中以客户端为中心的最终一致性方面重新获得了相关性。

---

## 95. 人工智能保险：说来容易做来难

**原文标题**: Insurance for AI: Easier Said Than Done

**原文链接**: [https://loeber.substack.com/p/24-insurance-for-ai-easier-said-than](https://loeber.substack.com/p/24-insurance-for-ai-easier-said-than)

无法访问文章链接。

---

## 96. 互联网时代之前的生活 – 20世纪80年代创业记 (2016)

**原文标题**: Life before the web – Running a Startup in the 1980's (2016)

**原文链接**: [https://blog.zamzar.com/2016/07/13/life-before-the-web-running-a-startup-in-the-1980s/](https://blog.zamzar.com/2016/07/13/life-before-the-web-running-a-startup-in-the-1980s/)

本文讲述了罗伯特·加斯金斯在 1980 年代运营 Forethought 公司的经历，该公司创造了 PowerPoint。加斯金斯将当时创业公司面临的挑战与当今受互联网严重影响的环境进行了对比。

在 80 年代，由于缺乏实时反馈和在线发行，软件开发需要大量的前期投资和仔细的规划。竞争非常激烈，Forethought 战略性地瞄准了新兴的 Windows 和 Macintosh 平台，押注它们未来将超越现有的 MS-DOS 市场。虽然 Windows 版本的 PowerPoint 由于 Windows 平台相对于 Mac 的不成熟而大幅延迟，但这种赌注得到了回报。

该公司多次面临濒临破产的局面，由于缺乏直接的客户沟通渠道，依赖于诸如杂志编辑公关和昂贵的顾问“建议”等非常规销售策略。他们还面临与实体产品制造、分销和升级相关的巨额管理费用。

与通常的建议相反，Forethought 最初在 PowerPoint 开发的同时，也将业务多元化到软件发行领域。这一决定几乎使公司破产，其成本远远超过了 PowerPoint 开发本身。最终，微软收购了 Forethought，而专注于 PowerPoint 最终带来了成功。加斯金斯最后强调了互联网为现代创业公司提供的显著优势，以及它如何从根本上改变了软件开发格局。

---

## 97. 94行Ruby代码实现的编程代理

**原文标题**: Coding agent in 94 lines of Ruby

**原文链接**: [https://radanskoric.com/articles/coding-agent-in-ruby](https://radanskoric.com/articles/coding-agent-in-ruby)

本文详细介绍了作者受 Thorsten Ball 的观点启发，即编码代理并不难创建，使用仅仅 94 行 Ruby 代码构建代码编辑代理的经验。 该代理本质上是一个具有工具访问权限的 AI 聊天代理，利用 RubyLLM gem 与 Anthropic 的 Claude 等 LLM 进行交互。

该代理的核心功能围绕一个聊天循环：读取用户提示，将其输入到 LLM，并显示 LLM 的响应。 为了将其转换为编码代理，作者实现了三个关键工具：`ReadFile`（读取文件内容）、`ListFiles`（列出目录中的文件）和 `EditFile`（替换文件中的字符串）。 `EditFile` 工具尤为重要，因为它允许 LLM 创建新文件。

作者展示了这些工具如何与 LLM 通过结构化描述理解和使用它们的能力相结合，使代理能够执行基本的编码任务。 然后，他们进一步改进了代理，添加了一个 `RunShellCommand` 工具，该工具允许代理执行命令（经过用户确认）以进行测试和迭代。

通过要求代理创建一个 ASCII 扫雷游戏来测试该代理，作者指出了该代理的成功，强调只需要最少的 AI 专业知识，并且由于 Ruby 的可读性和对程序员幸福的重视，Ruby 特别适合该任务。 最终代码可在 GitHub 上以 MIT 许可证获得。

---

## 98. Harmonic：Hacker News的现代安卓客户端

**原文标题**: Harmonic: Modern Android client for Hacker News

**原文链接**: [https://github.com/SimonHalvdansson/Harmonic-HN](https://github.com/SimonHalvdansson/Harmonic-HN)

Harmonic：一款Android Hacker News客户端，设计现代、快速且精良。自2020年起作为个人副项目开发，由于开发者开始攻读博士学位，投入时间减少。尽管未采用Kotlin或最新的Android API（反映了开发者较早的Android开发知识），该应用功能完备并在Google Play上架。

开源Harmonic的主要原因是允许用户通过Pull Request贡献修复和新功能。虽然开发者乐于接受改进，但为了保持代码熟悉度，不鼓励完全使用Kotlin重写。开发者也会在时间允许的情况下继续贡献。

Harmonic的主要功能包括基本的Hacker News账户功能（登录、投票、评论、提交）、基于Material 3的设计和动画、多种主题（包括纯黑选项）、丰富的自定义选项，以及对速度的重视。

---

## 99. Wow@Home –业余无线电望远镜网络

**原文标题**: Wow@Home – Network of Amateur Radio Telescopes

**原文链接**: [https://phl.upr.edu/wow/outreach](https://phl.upr.edu/wow/outreach)

Wow@Home项目旨在创建一个全球性的、经济实惠的业余射电望远镜网络，用于持续监测天空中的瞬时射电事件，包括潜在的技术特征，其灵感来源于最初的Wow!信号。这些小型望远镜，成本约为500美元，将自主运行，扫描天空并将数据上传到中央网络。

该网络通过提供全天候监测、全球覆盖和通过巧合探测抑制射频干扰，克服了专业望远镜的局限性。虽然灵敏度不如专业天文台，但这些望远镜可以探测到因观测时间有限而被大型仪器错过的强烈信号。

该项目强调可访问性和公民科学，提供免费软件（最初使用IDL，然后使用Python）和硬件建议。该软件将分析瞬时事件的数据，借鉴阿雷西博Wow!项目的分析方法。

未来的发展包括集成多波束系统、跟踪能力、干涉测量能力和相控阵配置。第一批硬件建议和软件发布计划于2025年8月15日发布，与Wow!信号周年纪念日同时。该项目欢迎在射频干扰屏蔽、软件GUI和应用程序开发等领域的贡献。

---

## 100. MCP安全简介

**原文标题**: Introduction to MCP Security

**原文链接**: [https://public.support.unisys.com/framework/publicterms.aspx?returnurl=%2faseries%2fdocs%2fClearPath-MCP-20.0%2f26211060-014%2fWebHelp%2fIntroduction_to_Security_Services%2fSecurity_Overview.htm](https://public.support.unisys.com/framework/publicterms.aspx?returnurl=%2faseries%2fdocs%2fClearPath-MCP-20.0%2f26211060-014%2fWebHelp%2fIntroduction_to_Security_Services%2fSecurity_Overview.htm)

题为“MCP安全简介”的文章看似是一篇简短的介绍性文章。虽然提供的内容有限，但它暗示了以下几点：

*   **重点：** 该文章可能讨论与MCP相关的安全方面（MCP可能是特定系统、平台或协议的缩写）。
*   **访问/使用环境：** “公共使用条款”的存在表明该信息是公开可访问的，并受某些使用指南的约束。
*   **支持可用性：** 指向“支持主页”的链接表明存在一个支持系统或资源，供寻求与MCP安全相关的帮助或更多信息的用户使用。
*   **可访问性考虑：** “移动视图”选项意味着该文章和相关资源被设计为可在包括手机和平板电脑在内的不同设备上访问。

本质上，这篇文章是理解MCP安全的起点，强调了其对公众的开放性，指向了支持资源，并考虑了移动可用性。更深入的理解需要访问完整的文章内容。

---

