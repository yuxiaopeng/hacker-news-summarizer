# Hacker News 热门文章摘要 (2025-05-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国诉谷歌案：Y Combinator支持原告的法院之友意见陈述书 [pdf]

**原文标题**: US vs. Google Amicus Curiae Brief of Y Combinator in Support of Plaintiffs [pdf]

**原文链接**: [https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1300.1.pdf](https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1300.1.pdf)

该PDF文档似乎是Y Combinator在“美国诉谷歌”案中提交的法庭之友意见陈述。法庭之友意见陈述是由“法庭之友”（amicus curiae）提交的法律文件，旨在提供信息或论点，以协助法院做出决策。

根据标题和元数据，该文档很可能是使用Microsoft Word创建，并使用iText Core进行PDF制作处理的。

文档的核心由PDF指令和内容流组成。PDF结构定义了页面、字体以及简报中文字和其他元素的布局。内容流包含压缩的文本和命令，当PDF查看器解释这些内容时，会呈现简报的实际内容。在未完全解压缩和解释这些流的情况下，无法提供论点的详细摘要。然而，根据标题，Y Combinator正在支持该案件中的原告，并就与该案件相关的事项提供他们的观点。

---

## 2. 萨姆·奥特曼想要你的眼球

**原文标题**: Sam Altman Wants Your Eyeball

**原文链接**: [https://www.privacyguides.org/articles/2025/05/10/sam-altman-wants-your-eyeball/](https://www.privacyguides.org/articles/2025/05/10/sam-altman-wants-your-eyeball/)

萨姆·奥特曼的Worldcoin项目，现扩展为“World App”，正因其扫描人们虹膜以换取数字身份和访问其生态系统的做法而面临审查。批评人士担心收集生物识别数据所带来的隐私影响，尤其考虑到该公司在发展中国家针对弱势群体时，据称存在不道德行为的历史。

World App旨在成为一个集加密货币管理、通讯、游戏等功能于一体的平台，所有功能都与通过虹膜扫描（使用名为Orb的设备）验证的“人格证明”相关联。该项目与Tinder、Stripe和Visa等大型公司建立了合作关系，引发了人们对广泛采用和潜在胁迫的担忧。

批评人士认为，该项目是在为OpenAI（奥特曼的另一家公司）所制造的问题（即AI生成的机器人和虚假账户的泛滥）提供解决方案。他们还强调了与生物识别数据相关的风险，包括身份盗窃和失去在线匿名性的可能性。人们还对该公司声称的隐私保护表示担忧，批评人士认为，从扫描中提取的虹膜代码构成个人数据，并且敏感数据最终会传输到用户的手机上。虽然该公司声称使用端到端加密，但这并不意味着数据从未离开过Orb。

---

## 3. 对MCP的批判性审视

**原文标题**: A Critical Look at MCP

**原文链接**: [https://raz.sh/blog/2025-05-02_a_critical_look_at_mcp](https://raz.sh/blog/2025-05-02_a_critical_look_at_mcp)

本文批判性地审视了Anthropic的模型上下文协议 (MCP)，该协议旨在使大型语言模型与外部数据和工具进行交互的标准。作者对其实现缺乏成熟的工程实践表示失望，并强调了文档不足、SDK质量不高以及协议规范存在疑问。

作者重点关注MCP的HTTP传输协议，包括HTTP+SSE和“可流式HTTP”，认为它们不必要地复杂化了实现，试图在不实际使用WebSockets的情况下模拟类似套接字的行为。他们声称这些方法引入了复杂性、潜在的不一致性、可扩展性问题以及诸如会话劫持和攻击面增加等安全漏洞。作者认为WebSockets将是更合适和更直接的选择，反映了首选的stdio传输的简单性。

此外，本文还批评了带有主观色彩的授权要求，主张标准化，而不是为stdio和HTTP制定不同的规则。文章认为，该行业正在优先考虑短期利益，而忽略了长期可维护性。最后，作者简要地提到了新兴协议，如IBM的ACP和Google的A2A，建议可以将它们作为工具集成到MCP中，从而减少冗余。

---

## 4. 逆向工程分析386处理器预取队列电路

**原文标题**: Reverse engineering the 386 processor's prefetch queue circuitry

**原文链接**: [http://www.righto.com/2025/05/386-prefetch-circuitry-reverse-engineered.html](http://www.righto.com/2025/05/386-prefetch-circuitry-reverse-engineered.html)

本文深入研究了386处理器预取队列电路的逆向工程，重点关注其通过在需要之前从内存中获取指令来提高性能的作用。预取单元包含一个16字节的队列，通过利用空闲的内存总线周期来最大限度地减少处理器等待时间。

文章重点介绍了预取电路的几个关键组件。 “提前指令获取指针”而不是指令指针，用于跟踪要获取的下一条指令的地址。限制检查机制，将获取指针与代码段限制进行比较，以防止超出有效内存区域的预取。这种比较使用异或门网络和动态逻辑来实现效率。

增量器负责更新获取指针，它采用曼彻斯特进位链和进位跳跃技术来实现高速运行。曼彻斯特进位链使用晶体管开关来快速确定进位位，而进位跳跃允许进位跳过位块以实现更快的处理。动态逻辑用于管理和放大进位信号。

文章还涉及用于对齐预取队列中的数据的数据移位网络，以及将有符号的 8 位和 16 位值转换为 32 位值的符号扩展电路。作者注意到将电路安装在固定芯片宽度内的限制，这导致了巧妙的布局技巧。总体目标是提高对 386 处理器中低级电路和动态逻辑的理解。

---

## 5. 展示HN：代码克劳德代码

**原文标题**: Show HN: Code Claude Code

**原文链接**: [https://github.com/RVCA212/codesys](https://github.com/RVCA212/codesys)

"Code Claude Code" 介绍了 `codesys`，这是一个 Python SDK，旨在简化与 Claude CLI 工具的交互，以进行代码生成和任务自动化。 该 SDK 允许用户在 Python 项目中利用 Claude 的功能，从而促进以计划和执行为中心的工作流程。

主要功能包括：

*   **简化的 Claude CLI 交互：** 提供了一个 Python 式的接口，用于使用 Claude CLI 执行提示。
*   **灵活性：** 支持流式输出、可定制的工具访问（编辑、Bash、写入）以及传递额外的 CLI 参数。
*   **工作流程模仿：** 鼓励用户采用先计划后实施的方法，模仿 Claude Code 的有效工作流程。
*   **`Agent` 类：** 核心组件，允许使用工作目录和允许的工具进行初始化。 提供 `run` 和 `run_with_tools` 方法，用于使用不同的配置执行提示。
*   **实用示例：** 该 SDK 通过实用示例进行演示，展示了流式输出处理、工具定制、手动流式处理以及输出格式/参数的使用。

该 SDK 需要 Python 3.8+ 以及正确安装和配置的 Claude CLI。 通过 `pip install codesys` 进行安装。 它提供自动和手动流式输出管理，支持 JSON 解析和其他格式。 MIT 许可证促进开放使用和贡献。 本质上，`codesys` 旨在简化在 Python 环境中使用 Claude 进行代码相关任务。

---

## 6. Prolog永恒的九月 (2017)

**原文标题**: Prolog's Eternal September (2017)

**原文链接**: [https://storytotell.org/prologs-eternal-september](https://storytotell.org/prologs-eternal-september)

这篇2017年的博客文章《Prolog的永恒九月》探讨了Stack Overflow上不断涌现的非常基础的Prolog问题。作者观察到，这些问题主要与家庭作业有关，并揭示了一个更深层次的问题：Prolog通常由不理解它的教授教授。这导致学生们第一次接触Prolog时感到消极和困惑。

作者认为，在Stack Overflow上回答这些基本问题是适得其反的，因为学生们不是在寻求理解或参与，而仅仅是在寻找答案。作者提出了一个双管齐下的方法来解决这个问题：

1. **解决方案数据库：**一个小型、带有注释的Prolog解决方案数据库，其中包含对基本语法和高级概念的解释。这将作为一个资源，全面地回答即使是最基本的问题。
2. **教授用教学幻灯片：**预先制作的幻灯片，供教授们在教授Prolog时使用，即使他们对该语言缺乏深入的理解。这些幻灯片将根据不同的教学时长（一节课，三节课）进行定制。

作者建议暂停在Stack Overflow上提供直接解决方案，而是引导用户访问解决方案数据库。

作者寻求想法和合作，以解决Prolog教学不佳的系统性问题，并鼓励读者与他们联系。

---

## 7. Weave (YC W25) 招聘创始工程师

**原文标题**: Weave (YC W25) is hiring a founding engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs](https://www.ycombinator.com/companies/weave-3/jobs)

Weave (YC W25) 是一家软件公司，致力于提高工程团队的工作效率，现招聘两位创始工程师：一位人工智能工程师和一位产品工程师。两个职位均位于旧金山/奥克兰地区，薪资范围为 14 万美元至 20 万美元，股权在 0.50% 至 2.00% 之间。人工智能工程师职位至少需要 1 年经验，而产品工程师职位欢迎应届毕业生。

Weave 是一家资金充足且盈利的初创公司，拥有顶级投资者的支持，并且正在快速增长。Weave 由 Andrew Churchill 和 Adam Cohen 于 2024 年创立，是 Y Combinator W25 批次的一部分。该公司正在积极开发软件，专注于使用人工智能来衡量和改进工程工作。他们的网站是 workweave.dev。

---

## 8. 临终谬误

**原文标题**: The deathbed fallacy

**原文链接**: [https://www.hjorthjort.xyz/2018/02/21/the-deathbed-fallacy.html](https://www.hjorthjort.xyz/2018/02/21/the-deathbed-fallacy.html)

本文批判了一种普遍的观点，即人们临终前的遗憾能够提供有价值的人生建议，作者将这一概念称为“临终谬论”。作者认为，临终视角提供的建议不一定适用于或有益于当下活着的人。

该论点基于三个主要方面：首先，临终视角并不能代表充实的人生，因为它被迫在眉睫的终结所定义，从而影响优先事项并扭曲对过去的认知。其次，我们对过去自我的理解往往存在缺陷，导致对过去行为的真正益处做出不准确的判断。作者举了一个例子，青少年时期优先考虑融入群体，后来被认为是遗憾，但实际上当时是一种有益的生存策略。最后，世界随着时间推移而变化，使得过去世代的遗憾可能与当今的个体无关。例如，有人后悔没有做到真实，可能没有意识到老一辈在表达自我方面所面临的挑战。

作者认为，那些信奉这些临终遗憾的人往往处境舒适，忘记了让他们获得当前生活方式的辛勤工作和牺牲。相反，在没有稳定基础的情况下追求真实、无忧无虑的生活可能会导致痛苦。

作者建议，与其依赖临终遗憾，不如关注幸福研究，反思个人过去的幸福感，并思考当下真正带来满足感的事物。这样做可以避免未来的潜在遗憾。努力工作和做出艰难的选择可能是当下正确的道路，即使未来的老年自我可能不这样认为。

---

## 9. React Three 生态系统

**原文标题**: React Three Ecosystem

**原文链接**: [https://www.react-three.org/](https://www.react-three.org/)

文章“React Three Ecosystem”极其简短，只包含标题两次。因此，几乎没有什么可总结的。

本质上，该文章*提到了 React Three Ecosystem*。它没有定义它，解释它的组成部分，也没有深入探讨它的功能。我们只知道它是一个叫做“React Three Ecosystem”的东西。

由于提供的文本缺乏实质内容，任何总结都将固有地受到限制。“关键信息”仅仅是对名为“React Three Ecosystem”主题的确认。

---

## 10. Linux 下 C/POSIX 标准库实现比较

**原文标题**: Comparison of C/POSIX standard library implementations for Linux

**原文链接**: [https://www.etalabs.net/compare_libcs.html](https://www.etalabs.net/compare_libcs.html)

本文对Linux下C/POSIX标准库的实现进行了比较分析，包括musl、uClibc、dietlibc和glibc。比较范围涵盖几个关键领域：臃肿程度、资源耗尽时的行为、性能、ABI和版本控制、使用的算法、特性、目标架构、构建环境以及安全/强化。

本文强调，musl旨在实现功能丰富性和最小臃肿程度之间的平衡，而glibc功能更丰富但体积更大。Dietlibc专注于极端的尺寸缩减，而uClibc介于两者之间。

性能基准测试揭示了内存分配、字符串操作、线程创建和I/O等方面的差异。ABI和版本控制比较强调了musl的稳定ABI和向前兼容性，与glibc的复杂性和偶尔的不兼容性形成对比。用于子字符串搜索和排序等任务的算法在不同的实现中也有所不同，从而影响性能。

特性比较详细说明了对C标准、POSIX标准、宽字符接口和各种扩展的支持程度。目标架构比较显示了每种库的平台支持范围。

最后，本文讨论了构建环境的注意事项，如头文件的可用性和命名空间遵守，以及安全强化措施，包括UTF-8解码和堆栈粉碎保护。总而言之，此比较旨在提供对不同C标准库实现之间权衡的见解，以帮助开发人员选择最适合其特定需求的实现。

---

## 11. Llama.cpp 现已支持视觉功能

**原文标题**: Vision Now Available in Llama.cpp

**原文链接**: [https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md)

文章宣布`llama.cpp`项目现已支持视觉功能。这意味着该项目，专注于Llama模型的高效C/C++实现，现在除了文本之外，还支持处理和理解视觉信息。

此公告可能意义重大，因为`llama.cpp`以其性能和易用性而闻名，允许用户在包括消费级计算机在内的各种硬件上运行Llama模型。为`llama.cpp`添加视觉支持使得视觉模型更容易访问，并允许对视觉数据进行本地处理。

文章还通过指标突出了该项目的受欢迎程度：1.17万个fork和7.95万个star。这突显了社区对`llama.cpp`在Llama相关开发和部署方面的强烈兴趣和依赖。因此，视觉功能的集成很可能被广泛采用，并进一步提升该项目在开源AI生态系统中的价值。

---

## 12. LTXVideo 13B AI视频生成

**原文标题**: LTXVideo 13B AI video generation

**原文链接**: [https://ltxv.video/](https://ltxv.video/)

LTXV 13B是由Lightricks开发的突破性AI视频生成模型，拥有130亿参数，可用于高质量视频创作。于2025年5月发布，是其20亿参数前身的重大升级，由于其先进的多尺度渲染技术和内核优化，其速度比同类模型提高了30倍。

主要功能包括文本到视频和图像到视频转换、在消费级硬件（如NVIDIA 4090/5090，配备8GB+ VRAM）上的实时性能，以及增强的提示词遵循能力，可实现精确的视频生成。该模型基于DiT架构，支持1216x704分辨率，帧率为30 FPS。它还包括高级运动质量控制。

LTXV的多尺度渲染首先以低细节草拟视频以进行运动捕捉，然后细化细节，从而确保速度和质量。它支持关键帧动画，并利用LTX-Video-Trainer进行微调，同时支持ComfyUI集成和LoRA，用于自定义效果。

LTXV 13B在LTXV开放权重许可下提供，可在Hugging Face和GitHub上访问，并附带文档、示例工作流程以及用于社区开发和自定义的工具。量化版本适用于VRAM较少的系统。0.9.7版本包括改进的提示词遵循能力、增强的运动质量、更好的精细细节以及对随机推理的支持。

---

## 13. 告别李·戈尔德的惊扰与骚动

**原文标题**: Farewell to Lee Gold's Alarums and Excursions

**原文链接**: [https://www.chaosium.com/blogout-of-the-suitcase-54-farewell-to-lee-golds-alarums-excursions/](https://www.chaosium.com/blogout-of-the-suitcase-54-farewell-to-lee-golds-alarums-excursions/)

本文宣布李·戈尔德持续发行近50年、超过590期的业余新闻协会（APA）刊物《警报与出击》（Alarums & Excursions，简称A&E）正式完结。APA是线上论坛的前身，是由投稿文章和订阅支持的实体印刷出版物。

《警报与出击》是一份备受推崇的APA刊物，曾荣获多项大奖，并于2022年入选Origins名人堂。它刊登了许多格洛兰萨角色扮演游戏社区著名人物的稿件，包括格雷格·斯塔福德、史蒂夫·佩林和珍妮尔·杰奎斯。投稿者不仅提供原创内容，还对彼此的作品进行了广泛的评论。

除了《警报与出击》，李·戈尔德还是一位开创性的女性RPG作家，著有《旭日之国》、《通用角色扮演系统：日本》和《维京人》等作品。她也是一位备受尊敬的科幻幻想人物、小说家和菲尔克音乐家。遗憾的是，由于视力衰退，她已经停止了《警报与出击》和《异域菲尔克歌曲》的出版。

本文指出，《警报与出击》早期刊物的印刷数量非常有限，使得实体副本非常稀有。然而，所有过刊的PDF版本都可从李·戈尔德处购买。作者里克·梅因茨一直在为他的《梅因茨格洛兰萨索引》索引《警报与出击》中的符文探索和格洛兰萨相关内容。

---

## 14. 英特尔：得与失

**原文标题**: Intel: Winning and Losing

**原文链接**: [https://www.abortretry.fail/p/intel-winning-and-losing](https://www.abortretry.fail/p/intel-winning-and-losing)

本文延续了英特尔发展历程的系列报道，重点关注2008年至2011年期间，这是一个既有胜利也有战略转变的时期。

2008年，英特尔在台式机和笔记本电脑CPU市场占据主导地位。他们推出了采用Bonnell微架构的Atom CPU系列，目标是低功耗设备，但Poulsbo芯片组的局限性阻碍了其在手持设备中的应用。与此同时，英特尔推出了Nehalem微架构（Core i7/Xeon），该架构具有片上内存控制器、TurboBoost和QuickPath互连（QPI）等创新，与前几代产品相比，以更少的功耗提供了卓越的性能。

2009年，基于Nehalem的Xeon发布，英特尔宣布了其32纳米工艺。简·肖成为董事长，打破了内部任命CEO的传统。

2010年，英特尔发布了采用32纳米工艺的Nehalem/Westmere微架构，扩展了其产品线。他们还推出了英特尔SSD 310，一款紧凑型mSATA SSD。个人电脑市场蓬勃发展，使英特尔受益匪浅，包括Atom产品线。

到2011年，英特尔认识到日益激烈的竞争，并致力于多元化，尤其是在Atom和相关生态系统中进行了大量投资。他们还在其32纳米工艺上推出了Sandy Bridge，提供了显著的性能改进。最初名为Light Peak的Thunderbolt也已推出。本文重点介绍了英特尔收购McAfee的举动，旨在构建一个软件生态系统并解决安全问题。最后，英特尔宣布了其具有突破性的22纳米工艺，引入了FinFET晶体管，为晶体管技术设定了新的标准。

---

## 15. 日本私营月球着陆器进入绕月轨道，计划六月着陆。

**原文标题**: Private Japanese lunar lander enters orbit around moon ahead of a June touchdown

**原文链接**: [https://phys.org/news/2025-05-private-japanese-lunar-lander-orbit.html](https://phys.org/news/2025-05-private-japanese-lunar-lander-orbit.html)

2025年5月，日本东京 ispace 公司开发的私营月球着陆器“坚韧号”成功进入月球轨道。这标志着该公司计划于六月第一周进行的着陆尝试迈出了重要一步。

“坚韧号”着陆器于2025年1月与美国萤火虫宇航公司的一个着陆器一同发射。萤火虫公司在3月成功实现月球着陆，成为第一家无事故完成此壮举的私营实体。另一家美国公司，直觉机器公司，紧随其后，但他们的着陆器最终侧翻在一个陨石坑里。

这是 ispace 公司第二次尝试月球着陆，此前曾在2023年发生撞击事故。“坚韧号”着陆器携带了一个配备铲子的迷你漫游车，旨在收集月球土壤进行分析，以及其他实验。该公司表示，成功绕月飞行意味着“月球着陆的倒计时现在正式开始”。

---

## 16. 商业书籍是娱乐，而非战略工具。

**原文标题**: Business books are entertainment, not strategic tools

**原文链接**: [https://theorthagonist.substack.com/p/why-reading-business-books-is-a-waste](https://theorthagonist.substack.com/p/why-reading-business-books-is-a-waste)

无法访问文章链接。

---

## 17. Embracer游戏档案馆正在保存75000款电子游戏，需要您的贡献

**原文标题**: Embracer Games Archive is preserving 75000 video games and needs contributions

**原文链接**: [https://embracergamesarchive.com/](https://embracergamesarchive.com/)

拥抱者游戏档案馆是由拥抱者集团发起的一个项目，致力于通过收集和存档实体游戏、游戏机、电脑和配件来保护电子游戏历史。该档案馆目前在瑞典卡尔斯塔德拥有超过75000件藏品，旨在成为行业和研究人员的综合资源。

该档案馆的目标是与机构、记者和游戏社区的其他人士合作，记录和推广游戏遗产。虽然尚未完全向公众开放，但他们优先考虑游戏行业专业人士、研究人员、学校和类似机构的访问。网站和社交媒体渠道提供了对档案馆工作的见解。

他们正在积极寻求贡献，特别是大量的游戏和硬件收藏品，适用于3DO、Amstrad CPC 464、Apple II、Bandai Playdia、BBC Micro、Dragon 32、Macintosh大盒装、MSX PC大盒装和飞利浦CD-i等系统，以及来自巴西、韩国和台湾的游戏。有兴趣出售或捐赠藏品的人士可以通过[email protected]联系收购经理Thomas Sunhede。

---

## 18. 用简单数学规则制作的16x16像素动画

**原文标题**: A simple 16x16 dot animation from simple math rules

**原文链接**: [https://tixy.land](https://tixy.land)

本文介绍了一种使用简单数学规则生成16x16点阵动画的方法，作为“创意代码高尔夫”的示例。其核心思想是将动画逻辑编码进数学公式中，通过计算公式并在16x16网格上渲染成可视图案。

动画系统的输入包含四个变量：`t`（可能代表时间）、`i`（可能用于迭代或索引）、`x`和`y`（代表网格上像素的x和y坐标）。每个像素的动画视觉输出由一个作用于这些输入的数学函数决定。

“创意代码高尔夫”意味着作者专注于寻找最短、最优雅、通常也最隐晦的方式来表达产生有趣动画的数学规则。挑战在于使用数学运算将动画行为的复杂性压缩到最少的代码中。

本质上，该提交描述了一个系统，其中数学表达式驱动着16x16网格的视觉表示，并通过这些表达式的输出随时间(`t`)的演变来创建动画。目标是展示数学函数在用最少的代码创建出令人惊讶的丰富且复杂的视觉图案方面的强大能力。作者并未明确详述所使用的具体数学方法，而是在宣传这一概念。

---

## 19. 西雅图港口称“目前没有集装箱船”

**原文标题**: 'We Currently Have No Container Ships,' Seattle Port Says

**原文链接**: [https://www.newsweek.com/seattle-port-says-no-container-ships-tariffs-2069464](https://www.newsweek.com/seattle-port-says-no-container-ships-tariffs-2069464)

西雅图港称“目前没有集装箱船”的《新闻周刊》文章报道称，西雅图港的集装箱船吞吐量正经历显著下滑。据该港口称，他们目前没有集装箱船停靠，这种情况归因于贸易政策（尤其是关税）和更广泛的经济转变等多种因素。

文章强调，贸易战期间征收的关税影响了航运路线和贸易量，可能将船只转移到被认为在经济上更有利的其它港口。该港口的代表表示，这些贸易争端对其运营产生了持久的影响。

此外，文章暗示，集装箱船的缺乏反映了更广泛的经济放缓或对供应链的重新评估，可能会影响依赖该港口进行进出口的当地企业。远离西雅图可能会导致该地区的失业和经济挑战。虽然这篇文章关注的是西雅图，但它可能暗示了一种影响美国各地港口的更普遍的趋势。

---

## 20. Gmail 转 SQLite

**原文标题**: Gmail to SQLite

**原文链接**: [https://github.com/marcboeker/gmail-to-sqlite](https://github.com/marcboeker/gmail-to-sqlite)

本文档介绍了一个名为“Gmail to SQLite”的工具，它可以从 Gmail 账户下载电子邮件并将它们存储到 SQLite 数据库中。这允许用户对其电子邮件数据执行复杂的查询和分析。

要使用该工具，您必须首先克隆存储库，安装必要的 Python 包，并设置启用了 Gmail API 的 Google Cloud 项目。这包括为桌面应用程序创建 OAuth 客户端 ID，并将下载的凭据文件以 `credentials.json` 的名称保存在存储库的根目录中。

`main.py` 脚本提供两个主要命令：`sync` 用于下载和同步电子邮件，`sync-message` 用于同步单个邮件。`sync` 命令需要指定 `--data-dir`，数据库（`messages.db`）和用户凭据将存储在该目录中。`--full-sync` 选项允许更新现有邮件的已读状态、标签和上次索引时间戳。`sync-message` 命令需要 `--data-dir` 和 `--message-id`。

数据库模式包括诸如发送者、收件人（To、CC、BCC）、标签、主题、正文、大小、时间戳、已读状态、发件状态和上次索引时间戳等字段。

该文档提供了 SQL 查询示例，以演示该工具的功能，例如计算每个发送者的电子邮件数量、识别每个发送者的未读电子邮件、分析电子邮件随时间变化的频率、查找新闻通讯以及确定最大电子邮件的发送者。

未来的开发计划包括检测和标记数据库中已删除的电子邮件。

---

## 21. Radxa Orion O6 将 Arm 带入中端 PC 市场 (但存在不足)

**原文标题**: Radxa Orion O6 brings Arm to the midrange PC (with caveats)

**原文链接**: [https://www.jeffgeerling.com/blog/2025/radxa-orion-o6-brings-arm-midrange-pc](https://www.jeffgeerling.com/blog/2025/radxa-orion-o6-brings-arm-midrange-pc)

Radxa Orion O6：具备潜力但有缺陷的 Arm ITX 主板

Radxa Orion O6 是一款 Arm ITX 主板，提供高达 12 核、64 GB 内存和 Armv9.2 支持，起价略高于 200 美元。它拥有 SystemReady SR 认证的 BIOS，无需修改即可使用 Windows on Arm 和各种 Linux arm64 ISO。

尽管潜力巨大，O6 仍存在许多固件问题，不适合喜欢即插即用体验的用户。早期承诺的 2.8 GHz 时钟频率已修改为 2.6 GHz，并且某些固件将主板限制为 8 核。虽然 SystemReady 固件允许原生安装 Windows 和 Linux，但驱动支持有限，影响了不同 Linux 发行版上 iGPU 和 5 Gbps 以太网等功能。

基准测试显示，其性能与五年前的 Apple M1 相当，但不如 M2 或骁龙 X 等较新的芯片，尤其是在效率方面。CPU 的行为不一致，主板的空闲功耗高于预期。

O6 的优势在于其自定义 PC 集成能力。Windows 11 运行出乎意料地好，尽管设备驱动程序支持匮乏。Linux 提供更好的 GPU 支持，但 AMD 显卡存在问题。Nvidia 显卡可用于 AI 任务和 GPU 计算。

总而言之，Radxa Orion O6 是一款有前景但有缺陷的 Arm ITX 主板。其硬件的价格颇具吸引力，但在吸引主流用户之前，其软件和固件需要进行重大改进。目前，它最适合擅长故障排除和驱动程序调整的经验丰富的用户。

---

## 22. Show HN: Sprigman – 用有限的基于瓦片的JavaScript引擎重制的吃豆人

**原文标题**: Show HN: Sprigman – Pac-Man Recreated in a Limited Tile Based JavaScript Engine

**原文链接**: [https://sprig.hackclub.com/share/X4EGvOFk1q8FroEPCj1G](https://sprig.hackclub.com/share/X4EGvOFk1q8FroEPCj1G)

这个“Show HN”帖子介绍了Sprig，一个用于构建基于图块游戏的微型JavaScript构建工具包。它由Hack Club开发，强调通过实践创建和在青少年程序员社区内分享进行学习。

Sprig采用一个简单的基于图块的系统，游戏通过正方形图块网格构建。核心功能通过JavaScript函数暴露，例如 `setLegend` (使用单字符键和位图定义精灵类型)、`setMap` (创建和加载关卡)、`setSolids` (定义非重叠精灵，如墙壁) 和 `setPushables` (允许精灵推动其他精灵)。

用户输入通过 `onInput` 处理，响应按键 (w, a, s, d, i, j, k, l)。精灵可以通过修改其 `x`、`y` 和 `type` 属性在 JavaScript 中进行操作。实用函数如 `getTile`、`tilesWith`、`addSprite`、`clearTile`、`getAll` 和 `getFirst` 有助于精灵管理。

该系统还包括使用 `addText` 添加带有自定义位置和颜色的文本到屏幕的功能，以及使用内置的声音引擎和音序器通过 `tune` 和 `playTune` 函数创建音乐和音效的功能。

该编辑器包括一个无限循环检测机制。最后，用户可以自定义键绑定以适应他们的偏好。

---

## 23. 北部阿切人舞蹈和育儿歌曲的失落

**原文标题**: Loss of dance and infant-directed song among the Northern Aché

**原文链接**: [https://www.cell.com/current-biology/fulltext/S0960-9822(25)00447-6](https://www.cell.com/current-biology/fulltext/S0960-9822(25)00447-6)

无法访问文章链接。

---

## 24. 检测并崩溃 Chromium 机器人

**原文标题**: Detect and crash Chromium bots

**原文链接**: [https://blog.castle.io/detect-and-crash-chromium-bots-with-one-weird-trick-bots-hate-it/](https://blog.castle.io/detect-and-crash-chromium-bots-with-one-weird-trick-bots-hate-it/)

本文探讨了一个JavaScript代码片段，该片段利用与`iframe.contentWindow.open`相关的漏洞，导致无头Chromium浏览器（如Puppeteer和Playwright使用的浏览器）崩溃。作者将其展示为一种看似理想的机器人检测方法，允许在客户端识别并立即“中和”机器人。

该代码片段涉及创建一个iframe，然后使用特定参数调用`contentWindow.open`，从而触发无头Chromium环境中的崩溃。作者甚至提供了一个名为`botCheckMate`的代码片段来展示这一点。

然而，文章很快警告不要在生产环境中使用此方法。缺点超过了其新颖性：它会为真实用户创建未经请求的弹出窗口，从而对用户体验产生负面影响。它还将检测与响应（使浏览器崩溃）联系得过于紧密，从而限制了处理机器人的灵活性。此外，这是一个响亮且明显的信号，很容易被机器人作者检测到和规避。客户端性质限制了对服务器端元数据的访问，阻碍了明智的决策和白名单的使用。

作者强调了安静、不易察觉的检测信号的重要性，这些信号不会降低性能或用户信任。他们建议将检测与响应分离，并确保对适应的抵御能力。虽然崩溃代码片段在受控环境中既有趣又有效，但最终它是一种脆弱、侵入性和响亮的方法，不适合实际部署，尤其是在您重视搜索引擎排名的情况下。

---

## 25. 赞美 grobi 自动配置 X11 显示器

**原文标题**: In praise of grobi for auto-configuring X11 monitors

**原文链接**: [https://michael.stapelberg.ch/posts/2025-05-10-grobi-x11-monitor-autoconfig/](https://michael.stapelberg.ch/posts/2025-05-10-grobi-x11-monitor-autoconfig/)

本文赞扬了Alexander Neumann开发的程序`grobi`，它能自动配置X11显示器，特别是解决了作者使用戴尔32英寸8K显示器(UP3218K)遇到的挑战。此前，作者使用包含`xrandr`和sleep命令的自定义脚本来配置显示器，以便在从挂起到内存唤醒后进行配置，但这种方法不可靠，经常需要通过SSH手动干预。

作者通过安装和配置`grobi`解决了这个问题。一个自定义配置文件（`~/.config/grobi.conf`）定义了规则来检测显示器（基于连接的输出`DP-2`和`DP-4`），并自动运行`xrandr`来设置正确的分辨率和定位。`grobi`监听X11 RandR输出更改事件，并在显示器连接时触发配置过程。提供了使用`systemctl`和`journalctl`进行调试的技巧。

作者解释了他选择`grobi`而不是`autorandr`的原因，理由是熟悉以及Go的长期稳定性。文章承认`grobi`可能无法在Wayland上工作。

最后，文章详细介绍了作者的挂起到内存设置，其中包括一个使用`rtcwake`和`systemctl suspend`来管理挂起过程的`zleep`脚本，并与一个myStrom智能插头集成，以便在睡眠期间关闭显示器的电源以节省能源。一个systemd脚本（`/lib/systemd/system-sleep/zleep.sh`）用于在唤醒后调用带有`-resume`标志的`zleep`，以重新打开显示器。一旦电源恢复，`grobi`会自动配置显示。

---

## 26. 燃眉之急的慢速软件

**原文标题**: Slow software for a burning world

**原文链接**: [https://bonfirenetworks.org/posts/slow_software_for_a_burning_world/](https://bonfirenetworks.org/posts/slow_software_for_a_burning_world/)

Bonfire 发布 1.0 版本，不同于典型的技术公告，它反思了其独特的软件开发方法：“慢速软件”，建立在关怀、集体管理和长期弹性之上。与硅谷快速增长和利润最大化的模式形成对比，Bonfire 从萨帕塔的“蜗牛”中汲取灵感，优先考虑来自边缘的社区治理，先倾听后行动，以及自治而非等级制度。

Bonfire 的设计强调模块化、社区管理的“风格”（配置）、可配置的默认设置、自定义角色和灵活的“圈子”和“边界”，以赋能用户和社区塑造其数字空间。它优先考虑真实的人和复杂的关系，而不是速度和简单性，满足通常被边缘化的需求。

为了抵御掠夺并确保长期的社区自治，Bonfire 采用 AGPL 许可、易于分叉的多层模块化、社区管理的风格，并承诺零风险投资或广告。他们正在试验社会计量圈进行治理和参与式资金模式。Bonfire 与 Mastodon 和联邦宇宙联合，强调通过连接而非集中式平台来实现自治。

Bonfire 被定位为一个“公共利益社交网络”，一个用于共同创造和持久网络的共享空间，建立在关怀、同意和集体管理之上。文章邀请社区组织者、活动家和建设者通过对话、治理、功能提案、反馈和文化贡献来参与塑造 Bonfire。他们提供了一个测试实例“营地”，用于共同设计和实验。核心信息是邀请大家共同构建一种不同的数字未来，一个建立在有意性、集体性和关怀之上的未来。

---

## 27. 商业崇拜

**原文标题**: The cult of doing business

**原文链接**: [https://www.commonwealmagazine.org/calvert-work-entrepreneur-ethic-baker-review-job](https://www.commonwealmagazine.org/calvert-work-entrepreneur-ethic-baker-review-job)

德鲁·卡尔弗特的文章评论了埃里克·贝克的《创造你自己的工作》，该书探讨了美国普遍存在的“创业工作伦理”。贝克认为，这种伦理受到积极心理学和自助思想的驱动，促使人们过度工作，并将自我价值与工作联系起来，导致精疲力竭，失业时感到毫无目标。

文章追溯了这种伦理的根源，可追溯到19世纪的新思想运动，该运动承诺个人可以通过积极思考克服经济困难。这演变成一种“教义模糊的成功哲学”，由拿破仑·希尔和戴尔·卡耐基等人物推广，他们从摆脱经济衰退的人们的焦虑中获利。

贝克将这一历史趋势与现代积极心理学运动联系起来，认为它主要用于使创业伦理合法化，鼓励工人拥抱“毅力”和“心流”以促进企业成功。他批判了史蒂夫·乔布斯等人物和硅谷公司如何利用这种伦理来创造类似邪教的工作环境，最终剥削工人。

评论总结说，创业工作伦理虽然承诺自由和自主，但最终使工人接受不稳定，并在科技亿万富翁和零工之间制造了一种一致的错觉。它强调了仅凭职业定义自己的危险性，而是提倡优先考虑爱和人际关系。文章强调了商业自助和管理理论的掠夺性本质，这些理论提倡将个人视为“自己公司的首席执行官”。

---

## 28. “无法提供细微差别”：英国专家警告人工智能治疗聊天机器人不安全

**原文标题**: 'It cannot provide nuance': UK experts warn AI therapy chatbots are not safe

**原文链接**: [https://www.theguardian.com/technology/2025/may/07/experts-warn-therapy-ai-chatbots-are-not-safe-to-use](https://www.theguardian.com/technology/2025/may/07/experts-warn-therapy-ai-chatbots-are-not-safe-to-use)

本文探讨了英国专家对使用人工智能治疗聊天机器人进行心理健康支持日益增长的担忧。尽管马克·扎克伯格设想人工智能可以作为治疗师的现成替代品，但心理健康临床医生持谨慎态度，认为其可能提供危险的建议，并且缺乏细致的理解。蒂尔·怀克斯教授爵士指出，过去曾发生过一个饮食失调聊天机器人提供有害建议的事件。她还认为，人工智能可能会取代与朋友分享和讨论个人问题的需求，从而扰乱现有的社交联系。

本文强调了Noah和Wysa等心理健康聊天机器人以及Replika等人工智能伴侣的受欢迎程度，但强调需要监督和监管以确保用户安全。OpenAI最近撤回了一个版本的ChatGPT，因为它对分享个人挣扎的用户给出了过于奉承和可能鼓励性回应。

杰米·克雷格博士强调了心理健康专业人士参与人工智能开发的重要性，以确保遵循最佳实践。他承认，一些人工智能工具受到用户的重视，但警告说，英国尚未充分解决围绕这些技术的安全和伦理问题，包括在Instagram等平台上出现的虚假治疗师聊天机器人。

---

## 29. Fixrleak：使用GenAI修复Java资源泄漏

**原文标题**: Fixrleak: Fixing Java Resource Leaks with GenAI

**原文链接**: [https://www.uber.com/en-IL/blog/fixrleak-fixing-java-resource-leaks-with-genai/](https://www.uber.com/en-IL/blog/fixrleak-fixing-java-resource-leaks-with-genai/)

本文介绍了FixrLeak，一个由Uber开发的基于生成式人工智能（GenAI）的框架，旨在自动检测和修复Java应用程序中的资源泄漏。资源泄漏，例如未关闭的文件或数据库连接，可能导致性能下降和系统故障。虽然像SonarQube这样的工具可以识别这些泄漏，但手动修复它们既耗时又容易出错。

FixrLeak使用抽象语法树（AST）分析，结合生成式人工智能（特别是像OpenAI的ChatGPT-4O这样的模型）来生成准确且符合习惯的修复，通常利用Java的“try-with-resources”最佳实践。该系统识别泄漏，执行AST级别的分析以确保修复是安全的（避免像use-after-close错误之类的问题），使用GenAI生成代码修复，并通过构建代码、运行测试以及使用SonarQube重新检查来验证修复，然后创建pull request供开发人员审查。

Uber在其广泛的Java代码库上部署了FixrLeak，并成功地自动化了最初由SonarQube识别出的102个符合条件的资源泄漏中的93个的修复。这显著减少了手动工作量，提高了开发人员的生产力，并提高了代码质量。未来的发展目标是扩展FixrLeak以处理过程间修复，将GenAI纳入到其他语言（如Golang）的泄漏检测中，并改进对用户定义的资源类的分析。文章强调了结构化代码分析、有针对性的自动化以及负责任的AI集成对于希望大规模提高代码质量的组织的重要性。

---

## 30. 互联网公路旅行：投票决定方向

**原文标题**: Internet Roadtrip: Vote to steer

**原文链接**: [https://neal.fun/internet-roadtrip/](https://neal.fun/internet-roadtrip/)

无法访问文章链接。

---

## 31. QueryLeaf: MongoDB 的 SQL 查询

**原文标题**: QueryLeaf: SQL for Mongo

**原文链接**: [https://github.com/beekeeper-studio/queryleaf](https://github.com/beekeeper-studio/queryleaf)

QueryLeaf 是一个 NodeJS 库，可以将 SQL 查询转换为 MongoDB 命令，使用户能够使用熟悉的 SQL 语法与 MongoDB 交互。它利用 `node-sql-parser` 解析 SQL，将 AST 转换为 MongoDB 命令，并通过官方 MongoDB Node.js 驱动程序执行它们。

主要功能包括支持基本的和高级的 SQL 操作，如 SELECT、INSERT、UPDATE、DELETE、嵌套字段访问、数组元素访问、带有聚合的 GROUP BY 和 JOIN。QueryLeaf 提供了一个用于直接集成的库接口、一个 CLI、一个用于 REST API 访问的 Web 服务器和一个 PostgreSQL wire protocol 服务器。

该文档提供了 SQL 到 MongoDB 转换的示例，演示了常见的 SQL 查询如何转换为 MongoDB 的查询语言。它概述了使用 npm 的安装过程，并提供了使用真实 MongoDB 客户端和用于测试的 `DummyQueryLeaf` 的使用示例。

该架构是模块化的，包含用于解析 SQL、编译为 MongoDB 命令和执行这些命令的组件。该项目包括单元测试和集成测试，后者使用 Docker 启动一个 MongoDB 实例。全面的文档可在网上查阅。

QueryLeaf 采用双重许可，AGPL-3.0 用于开源使用，并提供商业许可用于嵌入商业产品。

---

## 32. DNA中包含多少信息？

**原文标题**: How much information is in DNA?

**原文链接**: [https://dynomight.substack.com/p/dna](https://dynomight.substack.com/p/dna)

无法访问文章链接。

---

## 33. Ash (Almquist Shell) 变体

**原文标题**: Ash (Almquist Shell) Variants

**原文链接**: [https://www.in-ulm.de/~mascheck/various/ash/](https://www.in-ulm.de/~mascheck/various/ash/)

本文细致地详述了Ash (Almquist Shell) 变体的历史和演变，追溯了其从1989年的原始版本到现代实现（如dash、BusyBox和Android的shell）的谱系。文章着重强调了Ash最初作为System V Release 4 Bourne shell的替代品出现，旨在规避许可问题。

文章随后深入探讨了各种BSD衍生的Ash版本（4.3BSD-Net/2到4.4BSD-Lite2）、386BSD、BSD/OS、NetBSD和FreeBSD的具体演变，细致地记录了每个变体和版本中的代码更改、错误修复和功能添加。文章指出了Ash和SVR4 shell之间的关键差异，例如命令替换语法和`echo`选项。文章还讨论了早期Ash变体特有的功能以及Ash和SVR4 shell之间共享的功能。

作者概述了不同分支之间的同步点（例如，FreeBSD合并NetBSD代码）、关键的错误修复、以及诸如命令行编辑、算术扩展和内置命令等功能的添加。文章着重介绍了最初的Ash缺乏后期版本中存在的功能，例如`type`、`trap`处理符号名称和正确的IFS处理。本质上，这是一篇关于各种shell实现源代码的考古学研究。

---

## 34. Sofie：用于自动化直播电视新闻制作的开源网页系统

**原文标题**: Sofie: open-source web based system for automating live TV news production

**原文链接**: [https://nrkno.github.io/sofie-core/](https://nrkno.github.io/sofie-core/)

Sofie：开源的Web直播电视新闻制作自动化系统。文档为各类用户群体提供资源：

*   **用户指南：** 提供关于Sofie系统功能、安装和操作方面的通用文档。
*   **面向开发者：** 针对有兴趣开发和贡献Sofie代码库的人员提供特定文档。
*   **发行版：** 提供关于Sofie系统当前、过去和未来发行版的信息。
*   **社区：** 鼓励用户加入Sofie Slack社区，与开发者和其他用户联系。

本质上，内容是对Sofie系统及其全面的文档资源的介绍，同时服务于最终用户和开发者，并促进社区参与。

---

## 35. 宇宙482号下降舱追踪器

**原文标题**: Cosmos 482 Descent Craft tracker

**原文链接**: [http://astria.tacc.utexas.edu/AstriaGraph/](http://astria.tacc.utexas.edu/AstriaGraph/)

“宇宙482号下降器追踪器”可能提供有关追踪宇宙482号任务下降器的数据。数据可按星座、原产国、轨道类型（近地轨道、中地球轨道、地球静止/同步轨道、高椭圆轨道）和物体类型（活跃/非活跃卫星、火箭体、碎片、未分类）进行筛选。

数据来源于包括JSC Vimpel、Planet、SeeSat-L、SpaceX、忧思科学家联盟和美国太空司令部在内的多个组织。轨道确定依赖于美国太空司令部的特殊摄动星历，并使用基于Orekit的开源`orbdetpy`库。

轨道可视化利用EME2000状态向量和开普勒运动方程。但需要注意的是，为了最大限度地降低计算成本，可视化*不*考虑由地球扁率、第三体、大气阻力或太阳辐射压力引起的摄动。

最后，AstriaGraph数据可用于非商业用途，但需注明出处。商业用途需要获得数据来源的许可。

---

## 36. 布兰登半导体模拟器

**原文标题**: Brandon's Semiconductor Simulator

**原文链接**: [https://brandonli.net/semisim/](https://brandonli.net/semisim/)

布兰登半导体模拟器是一款允许用户绘制和模拟电路，可视化电磁场并利用各种材料的程序。它既可以作为基于浏览器的模拟（需要强大的计算机）访问，也可以作为需要Java的更快下载版本访问。

该模拟器具有交互式电路绘图功能，并提供包含金属、半导体和电介质的各种材料库。该模拟器包括常见电路、半导体器件和数字逻辑的示例。示例电路包括电阻、RC、LC、BJT和MOSFET电路。

该网站包含一个联系电子邮件地址，用于提供建议或示例请求。该模拟器最初由Brandon Li于2025年开发，后来在Paul Falstad的协助下移植到JavaScript。最近的更新（2022年5月10日）包括对电介质/铁磁体参数的调整、改进的N-MOSFET示例的准确性以及增强的肖特基二极管演示。

---

## 37. WebGL 水面 (2010)

**原文标题**: WebGL Water (2010)

**原文链接**: [https://madebyevan.com/webgl-water/](https://madebyevan.com/webgl-water/)

WebGL水体 (2010)：这是一个由Evan Wallace创建的WebGL演示，展示了在网页浏览器中逼真的水体渲染效果。该演示需要一块性能不错的显卡和最新的驱动程序，但无法运行的用户可以观看YouTube视频。

用户可以通过多种方式与水体互动：绘制涟漪、拖动背景旋转视角、用空格键暂停/取消暂停模拟、移动一个球体、用“L”键设置光照方向、以及用“G”键切换重力。

该演示的主要特性包括：

*   **光线追踪反射和折射：**模拟光线从水面反射和穿过的效果。
*   **解析环境光遮蔽：**通过近似计算到达每个点的环境光量来增强阴影的真实感。
*   **高度场水体模拟：**使用高度场模拟水体的运动和行为。
*   **柔和阴影：**产生更真实和漫射的阴影。
*   **焦散：**模拟水折射光线形成的图案，需要OES\_standard\_derivatives扩展。

水体模拟依赖于OES\_texture\_float扩展。该演示还包含一个来自Flickr用户zooboing的瓷砖纹理。

---

## 38. 恶之花

**原文标题**: Fleurs du Mal

**原文链接**: [https://fleursdumal.org](https://fleursdumal.org)

Fleursdumal.org是一个致力于法国诗人夏尔·波德莱尔作品的网站，特别是他的杰作《恶之花》。该网站提供了一个全面的在线版本，包含每个出版版本中的所有诗歌，以及多个英文翻译。

该网站由Supervert自2004年创建和维护，提供了该诗集的四个主要版本：1857年第一版（100首诗），1861年第二版（不包括被审查的诗歌但包括新的诗歌），《残篇》（1866年，包含被审查的诗歌作为“残片”），以及1868年 posthumous“最终”版。用户可以按字母顺序或通过1861年的目录（被认为是最权威的）浏览诗歌。还提供波德莱尔诗歌的录音，主要为法语。

该网站承认其翻译 ранее在书本中出现过，并欢迎翻译投稿，但保留拒绝的权利。它提供了联系信息，供权利持有人就 включения их переводов事宜进行联系。该网站是Supervert的作品，拥有所有权利，并且是Supervert更广泛的艺术作品组合的一部分，其中包括“Extraterrestrial Sex Fetish”和“Necrophilia Variations”等书籍，详细信息可在supervert.com上找到。

---

## 39. 在AMD 9950X上使用SIMD实现21 GB/s的CSV解析

**原文标题**: 21 GB/s CSV Parsing Using SIMD on AMD 9950X

**原文链接**: [https://nietras.com/2025/05/09/sep-0-10-0/](https://nietras.com/2025/05/09/sep-0-10-0/)

本文详细介绍了 CSV 解析库 Sep 在性能方面的改进，特别关注了针对支持 AVX-512 的 CPU（如 AMD 9950X (Zen 5)）的优化。Sep 0.10.0 在 9950X 上实现了 21 GB/s 的速度，相比之前版本有了显著提升。本文追踪了 Sep 从 .NET 7.0 到 .NET 9.0 以及从 AMD Ryzen 9 5950X (Zen 3) 到 9950X (Zen 5) 的性能提升，展示了在不到 2 年的时间内大约 3 倍的改进。

解决的核心问题是 .NET 9.0 中次优的 AVX-512 代码生成，特别是关于掩码寄存器的使用。最初的基准测试显示，Sep 的 AVX2 解析器在 9950X 上的性能竟然优于 AVX-512 解析器。作者随后分析了生成的汇编代码，强调了 AVX-512 实现中掩码寄存器和普通寄存器之间低效的来回移动。

为了规避这个问题，Sep 0.10.0 包含了一个经过调整的 AVX-512 解析器，它将 MoveMask 调用提前。一个更重要的解决方案是引入了一个新的 AVX-512 到 256 的解析器，该解析器利用 AVX-512 指令加载数据，但将数据转换为 256 位寄存器，从而避免了 512 位掩码寄存器，并实现了最高的解析速度。本文包含了详细的代码片段和汇编比较，以说明这些优化的影响。

---

## 40. 查尔斯·布考斯基、威廉·巴勒斯与电脑 (2009)

**原文标题**: Charles Bukowski, William Burroughs, and the Computer (2009)

**原文链接**: [https://realitystudio.org/bibliographic-bunker/charles-bukowski-william-burroughs-and-the-computer/](https://realitystudio.org/bibliographic-bunker/charles-bukowski-william-burroughs-and-the-computer/)

本文探讨了查尔斯·布考斯基和威廉·巴勒斯与计算机的关系，考察了这些技术如何影响他们的写作过程和文学遗产。

作者详细描述了布考斯基晚年出人意料地热情拥抱 Macintosh IIsi。尽管最初有所保留，布考斯基还是接受了电脑，发现它加快了他的写作速度，更容易编辑，甚至影响了他的诗歌风格，使其更加简单、直接。他的作品产量增加，并开始对传真和电子书等新技术着迷。电脑也成为他作品中的一种隐喻，既代表着创作潜力，也代表着衰老的作家的衰落。

相比之下，文章表明威廉·巴勒斯并没有直接将计算机融入他的创作过程。虽然他意识到了电脑生成诗歌的潜力，但巴勒斯档案馆中没有发现任何原生数字作品的证据。作者提出，展示庞大的巴勒斯档案可能需要创新的数字方法，例如《裸体午餐》的电子版，突出了档案管理员在管理和展示原生数字文学资料时面临的挑战。

文章最后讨论了数字技术对文学学术和档案管理的更广泛影响，提出了关于保存、分析和以合乎道德的方式管理当代作家数字档案的问题。

---

## 41. 量子视界：量子物理与当代艺术的融合展

**原文标题**: Quantum Visions, an exhibition combining quantum physics and contemporary art

**原文链接**: [https://www.tabakalera.eus/en/visiones-cuanticas/](https://www.tabakalera.eus/en/visiones-cuanticas/)

公告介绍了一个名为“量子视界”的展览，该展览融合了量子物理学和当代艺术。该活动属于艺术、科学、技术和社会范畴。由Jaime de los Ríos带领的导览参观活动“量子视界。展览中的量子比特”定于2025年5月10日12:00举行。公告中包含一个“阅读更多”信息的链接和一个购买“Entradas”（门票）的链接。

---

## 42. 西门子 PC 100 汇编手册中的 6502 非法操作码

**原文标题**: 6502 Illegal Opcodes in the Siemens PC 100 Assembly Manual

**原文链接**: [https://www.pagetable.com/?p=1798](https://www.pagetable.com/?p=1798)

本文探讨了西门子PC 100汇编手册（1980/1981年出版，德语，主要基于Rockwell AIM-65文档）中意外包含了6502非法操作码的文档。"6502参考"章节增加了三页，详细介绍了原始MOS/Rockwell参考资料中没有的“Sonderbefehle”（“特殊指令”）。

该手册识别了这些未记录指令的助记符（AAX、DCM、LAX、ISB）和操作码值，以及它们的操作和影响的标志。值得注意的是，西门子警告说某些指令（LAX Immediate、AAX X reg $02和AAX X reg accu $02）不稳定，并指出它们“并非总是被正确处理”。

本文分析了西门子的发现，并将其与6502非法操作码的已知行为进行了比较。结果发现，西门子正确识别了稳定的指令（SAX、DCP、LAX、ISC），但遗漏了寻址方式，并错误地识别了SHX/SHA。他们对LAX Immediate不稳定的评估是准确的，尽管他们没有准确指出原因。

作者的结论是，包含这些信息表明要么是西门子进行了原创研究，要么是从未经证实的来源复制而来，因为官方的MOS/Rockwell文档很可能包含了完整的寻址方式，并且避免记录不稳定的指令。

---

## 43. 西班牙沉船揭示最早抵达美国的宠物猫证据

**原文标题**: Spanish Shipwreck Reveals Evidence of Earliest Known Pet Cats to Arrive in US

**原文链接**: [https://www.smithsonianmag.com/smart-news/spanish-shipwreck-reveals-evidence-of-earliest-known-pet-cats-to-arrive-in-the-united-states-180986560/](https://www.smithsonianmag.com/smart-news/spanish-shipwreck-reveals-evidence-of-earliest-known-pet-cats-to-arrive-in-the-united-states-180986560/)

本文探讨了在佛罗里达州彭萨科拉附近一艘有466年历史的西班牙沉船“埃马努埃尔角二号”中发现的猫遗骸。这些遗骸被认为是美国最早的家猫证据。该船是1559年飓风中沉没的大型西班牙探险队的一部分。

研究人员分析了一只成年猫和一只幼年猫的遗骸，确定它们很可能被带到船上是为了控制啮齿动物，但也得到了水手的良好喂养。饮食分析表明，这些猫吃鱼和肉，表明它们不是为了食物或毛皮而饲养的。通过基因检测证实了这些猫的欧洲血统。

这一发现揭示了家猫传入美洲的情况，可能早于克里斯托弗·哥伦布带来的猫。主要作者马丁·韦尔克指出，西班牙在佛罗里达州的探险为家猫到达现在的美国提供了首次机会。本文还探讨了水手和猫之间的关系，强调了这些动物可能被视为同伴并被认为是幸运的。

---

## 44. Show HN: Hyvector – 一款快速现代的SVG编辑器

**原文标题**: Show HN: Hyvector – A fast and modern SVG editor

**原文链接**: [https://www.hyvector.com](https://www.hyvector.com)

此“Show HN”帖子宣传 Hyvector，一个“快速且现代的 SVG 编辑器”。然而，显示的内容表明存在一个关键问题：Hyvector 需要 JavaScript 才能运行，禁用 JavaScript 后，编辑器将无法使用。核心信息是 Hyvector 作为一个 SVG 编辑器而存在，但如果没有 JavaScript，用户体验会立刻崩溃。

---

## 45. Linux内核将放弃486 CPU，距离最后一款486 CPU生产已过去18年

**原文标题**: Linux kernel is leaving 486 CPUs behind, only 18 years after the last one made

**原文链接**: [https://arstechnica.com/gadgets/2025/05/linux-to-end-support-for-1989s-hottest-chip-the-486-with-next-release/](https://arstechnica.com/gadgets/2025/05/linux-to-end-support-for-1989s-hottest-chip-the-486-with-next-release/)

这篇Ars Technica的文章讨论了即将到来的Linux内核6.15版本中移除对i486处理器支持的决定，预计在本月晚些时候发布。这项由Linus Torvalds等内核开发者推动的决定，源于通过消除为这些过时处理器实施古老变通方法和仿真的需求，来简化开发工作的愿望。

i486处理器发布于36多年前，并于18年前被英特尔停产，它缺乏关键功能，如TSC（时间戳计数器）和CX8，而这些功能现在是内核更新后的最低支持特性所必需的。作者回忆起他们与i486的个人联系，并将其标记为他们第一次了解计算机硬件。

文章承认，仍在运行486系统的用户可以继续使用旧版本的Linux内核和发行版。它建议了FreeDOS和可能OS/2的后代ArcaOS等替代方案，同时指出需要至少奔腾处理器才能运行的轻量级操作系统（如MenuetOS、KolibriOS和Visopsys）的局限性。作者还提到了用户修改过的适用于486处理器的Windows XP版本，并警告不要将它们连接到互联网。文章最后表示，致力于运行486系统的用户可能会足够有资源找到合适的软件。

---

## 46. Itter.sh – 终端上的微型博客

**原文标题**: Itter.sh – Micro-Blogging via Terminal

**原文链接**: [https://www.itter.sh/](https://www.itter.sh/)

Itter.sh：基于终端的极简微型博客平台，完全通过 SSH 访问。旨在提供一种无干扰的社交媒体体验，摆脱了网页浏览器、JavaScript 和算法内容推送。用户通过终端与服务互动，发布限制为 180 个字符的短消息（“eets”）。

要使用 Itter.sh，用户需要一个 SSH 密钥。他们使用 `ssh register:YOUR_USERNAME@app.itter.sh` 注册，并使用 `ssh YOUR_USERNAME@app.itter.sh` 登录。该平台提供诸如 `ittereet`（发布消息）、`ittertimeline`（查看时间线，包括我的、全部、频道或特定用户）、`itterwatch`（实时时间线推送）、`itterfollow` 和 `itterunfollow`（管理关注）以及 `itterprofile`（查看和编辑个人资料）等命令。

Itter.sh 支持话题标签和提及。它使用 Python、AsyncSSH 和 Supabase 构建，专注于终端美学。该项目是开源的，可在 GitHub 上找到，欢迎贡献和错误报告（又称“未记录的功能”）。它的定位是逃离现代社交媒体的喧嚣和复杂性。

---

## 47. Stratolaunch成功完成可重复使用高超音速飞行及回收

**原文标题**: Stratolaunch Successfully Completes Reusable Hypersonic Flight and Recovery

**原文链接**: [https://www.stratolaunch.com/news/stratolaunch-successfully-completes-reusable-hypersonic-flight-and-recovery-with-talon-a2-vehicle/](https://www.stratolaunch.com/news/stratolaunch-successfully-completes-reusable-hypersonic-flight-and-recovery-with-talon-a2-vehicle/)

Stratolaunch公司宣布，继2024年12月成功首飞后，其Talon-A2 (TA-2)飞行器于2025年3月再次成功完成可重复使用的高超音速飞行。TA-2在两次飞行中均超过5马赫，展示了其可重复使用性和性能。Stratolaunch强调，这些飞行标志着自1968年以来，美国重返可重复使用的高超音速飞行测试领域。

这些飞行是在测试资源管理中心 (TRMC) 多服务高级能力高超音速测试平台 (MACH-TB) 项目下进行的，该项目与Leidos合作，旨在加速高超音速系统测试。首次飞行的数据已经过分析，为高速率的技术测试带来了积极成果。MACH-TB项目认为这些成功以及快速周转的可能性是高超音速测试的重要一步。

Stratolaunch公司首席执行官Zachary Krevor博士强调了团队的成就，包括多次Talon-A飞行、Roc飞行以及新型超音速和高超音速飞机的开发，为高超音速飞行测试服务铺平了道路。重点是支持美国国防倡议，并确保可重复使用的高超音速测试平台的持续性。

---

## 48. Swift 6.2 的新特性

**原文标题**: What’s new in Swift 6.2

**原文链接**: [https://www.hackingwithswift.com/articles/277/whats-new-in-swift-6-2](https://www.hackingwithswift.com/articles/277/whats-new-in-swift-6-2)

本文概述了 Swift 6.2 中即将推出的新特性和改进。一个主要重点是改进并发支持，并添加了旨在降低学习曲线的功能。

一项关键更改是引入了编译器标志 `-default-isolation MainActor`，允许开发者选择加入单线程程序，其中代码默认在主 Actor 上运行。

其他重大更新包括：

*   **原始标识符:** 允许在变量和函数名称中使用反引号括起来的更广泛字符，有利于测试名称和表示错误代码的枚举用例。

*   **字符串插值中的默认值:** 启用 `\(optional, default: "value")` 的用法，为字符串插值中的可选值提供默认值，解决类型不兼容问题。

*   **`enumerated()` 的集合一致性:** 使 `enumerated()` 返回的类型符合 `Collection`，提高与 SwiftUI `List` 和 `ForEach` 的可用性。

*   **方法和初始化器键路径:** 扩展键路径以支持方法以及属性和下标。

*   **选择性严格内存安全检查:** 引入 `@safe` 和 `@unsafe` 属性来标记不安全的 Swift 代码，调用 `@unsafe` 代码时需要 `unsafe` 关键字。

*   **Swift 回溯 API:** 引入 `Backtrace` 结构体，用于捕获调用堆栈数据以进行调试。

*   **`weak let`:** 允许对属性使用 `weak let`，补充 `weak var` 并使类能够符合 `Sendable`。

*   **值的事务性观察:** 创建一个新的 Observations 结构体，其中包含闭包，提供一个 AsyncSequence，每当 `@Observable` 数据更改时发出新值。

---

## 49. 古代人类用防晒霜在致命的磁极转换中幸存

**原文标题**: Ancient humans used sunscreen to survive a deadly magnetic pole shift

**原文链接**: [https://newatlas.com/history/ancient-humans-ochre-sunscreen-magnetic-pole-shift/](https://newatlas.com/history/ancient-humans-ochre-sunscreen-magnetic-pole-shift/)

大约41000年前，地球经历了拉斯尚事件，期间磁极发生偏移，显著削弱了地球的磁场。这一事件使得更多的紫外线（UV）和宇宙辐射到达地表，对地球上的生命构成了严重的健康风险。密歇根大学最近的一项研究表明，智人通过运用创新策略度过了这段时期。

研究人员分析了地球地空间系统的3D重建模型，发现拉斯尚事件与人类行为变化之间存在关联。考古证据表明，洞穴作为庇护所的使用量激增，定制服装的制作（骨针和锥子的普遍存在表明了这一点），以及红色和黄色赭石颜料的使用增加。

定制服装本可以为觅食提供有害辐射的防护。更值得注意的是，富含矿物质的化合物赭石，很可能发挥了天然防晒霜的作用。实验测试表明，赭石具有类似防晒霜的特性，并且智人在这一时期对其使用量的增加表明，它是出于辐射防护的目的而被有意识地使用的。

虽然这项研究是相关性的，但它提出了一个新的假设：智人通过使用庇护所、服装和防晒霜来适应增加的辐射暴露，可能有助于他们的生存，并可能在尼安德特人的衰落中发挥了作用，尼安德特人似乎没有以同样的方式适应。

---

## 50. ALICE在大型强子对撞机上探测到铅转化为金

**原文标题**: ALICE detects the conversion of lead into gold at the LHC

**原文链接**: [https://www.home.cern/news/news/physics/alice-detects-conversion-lead-gold-lhc](https://www.home.cern/news/news/physics/alice-detects-conversion-lead-gold-lhc)

大型强子对撞机ALICE实验组报告称，通过一种涉及铅核近失碰撞的新机制，实现了铅到金的嬗变。这些碰撞产生强烈的电磁场，导致光子与铅核相互作用，从而喷射出质子和中子。当三个质子被喷射出来时，铅（82个质子）就转变成了金（79个质子）。

虽然以前已经通过中子或质子实现了人工生产金，但这种方法利用了大型强子对撞机的高能铅核束及其相关的电磁场。ALICE探测器识别出导致特定数量质子和中子发射的相互作用，从而能够量化金的产量。

在ALICE碰撞点进行的铅-铅碰撞期间，大型强子对撞机以大约每秒89,000个核的速度生产金。尽管有这个速度，但大型强子对撞机第二轮运行（2015-2018）期间产生的金仅约29皮克。第三轮运行几乎使这个数量翻了一番，但仍然太少，不具备商业可行性。

ALICE的分析为大型强子对撞机中金的生产提供了实验证据，并有助于改进电磁离解的理论模型。这些模型对于理解和预测束流损失至关重要，而束流损失是限制大型强子对撞机和未来对撞机性能的关键因素。虽然炼金术士将铅变成金的梦想已经实现，但其数量太小，无法获得任何显著的经济效益。

---

## 51. EM-LLM：受人类启发、用于无限上下文LLM的情节记忆

**原文标题**: EM-LLM: Human-Inspired Episodic Memory for Infinite Context LLMs

**原文链接**: [https://github.com/em-llm/EM-LLM-model](https://github.com/em-llm/EM-LLM-model)

EM-LLM：一种结合人类情景记忆和事件认知的新型架构，通过整合人类情景记忆和事件认知，增强了大型语言模型(LLMs)的能力，使其能够以更高的效率处理几乎无限的上下文长度。它解决了标准LLM在处理大量上下文方面的局限性。EM-LLM通过使用贝叶斯惊讶度和图论边界细化将tokens序列组织成情景事件。此过程在线进行，无需对LLM进行微调。

信息检索通过结合基于相似度和时间连续性的两阶段记忆过程执行。在LongBench和$\infty$-Bench基准测试上的实验表明，与InfLLM等SOTA检索模型相比，EM-LLM表现出优越的性能，甚至在某些任务中超越了全上下文模型，尤其是在1000万个tokens的规模下，这对于全上下文模型来说在计算上是具有挑战性的。

该架构基于惊讶度分割输入序列，然后使用图论细化段边界。检索涉及k-NN搜索和从情景记忆中选择连续事件。EM-LLM利用`chunk_size`、`max_block_size`和`n_mem`等参数来控制内存管理和检索。一个关键特性是其能够动态地将内存块卸载到磁盘以处理非常长的序列。文章还强调了EM-LLM的事件分割与人类感知的事件之间的相关性，表明它与人类记忆机制存在联系。提供了代码和配置详细信息，以便进行复制和实验。

---

## 52. 展示HN: Aberdeen – 一种优雅的响应式UI方案

**原文标题**: Show HN: Aberdeen – An elegant approach to reactive UIs

**原文链接**: [https://aberdeenjs.org/](https://aberdeenjs.org/)

Aberdeen：一个用于构建响应式 UI 的 JavaScript/TypeScript 库（压缩后约 5KB，零依赖），无需虚拟 DOM。它使用小的匿名函数来生成 DOM 元素，并在其底层代理数据更改时自动重新运行。这种方法承诺速度和简单性，只更新必要的 UI 部分。

主要优势包括易用性（极简概念，无需构建步骤）、速度（无虚拟 DOM）、列表性能、体积小巧，以及诸如客户端路由、乐观 UI 更新、组件局部 CSS 和数据转换助手等内置功能。

提到的缺点是社区小，缺乏大型生态系统，需要开发者自己构建更多功能，而不是依赖现有的库。

文章提供了响应式计数器和待办事项列表示例来演示其用法。待办事项列表展示了编辑状态、动态排序和过渡效果等功能。其他示例包括输入处理、井字游戏、列表、路由和基准测试演示。

1.0 版本最近发布，包含交互式文档和教程。

---

## 53. Sorbet类型语法的过去、现在与未来

**原文标题**: Past, present, and future of Sorbet type syntax

**原文链接**: [https://blog.jez.io/history-of-sorbet-syntax/](https://blog.jez.io/history-of-sorbet-syntax/)

本文探讨了Sorbet类型语法在Stripe工程需求背景下的历史、设计选择和潜在未来。长期参与Sorbet开发的Jake解释说，最初丑陋而冗长的语法是经过深思熟虑的选择，优先考虑了语义而非美观。

Stripe工程师对静态类型检查、代码组织和改进模块化的需求（正如内部调查所显示）催生了Sorbet的诞生。之前使用Ruby DSL（如Odin::Model和`declare_method`）进行运行时类型检查的尝试表明了对类型的需求。

本文详细说明了为什么拒绝了当前语法的替代方案：由于Stripe庞大的Ruby代码库，重写为类型化语言是不切实际的，并且现有的Ruby类型检查器不足。TypeScript方法（引入构建步骤）被认为对Ruby开发工作流程的破坏性太大。头部文件（如RBS）被认为是不完整的，缺乏内联类型转换支持。基于注释的方法（如JSDoc）无法提供所需的运行时检查益处。

运行时检查的关键优势在于保证方法遵守其声明的类型契约，从而防止在修改代码时出现意外错误。作者旨在解决对语法的担忧，并提供对潜在语法改进的见解。

---

## 54. NSF面临改革：官员废除其37个部门

**原文标题**: NSF faces shake-up as officials abolish its 37 divisions

**原文链接**: [https://www.science.org/content/article/exclusive-nsf-faces-radical-shake-officials-abolish-its-37-divisions](https://www.science.org/content/article/exclusive-nsf-faces-radical-shake-officials-abolish-its-37-divisions)

无法访问文章链接。

---

## 55. CryptPad：谷歌套装的替代方案

**原文标题**: CryptPad: An Alternative to the Google Suite

**原文链接**: [https://cryptpad.org/](https://cryptpad.org/)

CryptPad被誉为注重隐私、开源且端到端加密的Google Suite替代方案。它强调协作和实时编辑，同时确保用户数据安全。本文重点介绍了CryptPad的完整应用程序套件，并着重介绍了用户评价。

用户称赞CryptPad易于使用、功能强大且注重隐私。提到的主要优点包括：安全的数据存储、无需收件人拥有帐户即可共享文件的能力、设计良好的界面以及免费开源。许多用户珍视 CryptPad 作为 Google Docs 的首要隐私替代品，提供类似的功能，而无需担心隐私问题。他们赞赏该平台在多种操作系统上的可用性及其广泛的协作工具，包括文档编辑、电子表格、看板和代码编辑。用户评价还强调了CryptPad适用于敏感文档、安全团队协作以及独立于大型科技公司监控的特点。欧洲托管地点以及符合数据保护法规的情况也受到了重视。总而言之，用户评价将CryptPad展示为值得信赖、多功能且尊重隐私的主流办公软件替代方案。

---

## 56. 简预算 - 极简纯文本预算

**原文标题**: PlainBudget – Minimalist Plain Text Budgeting

**原文链接**: [https://plainbudget.com/](https://plainbudget.com/)

PlainBudget：一款使用纯文本文件的极简预算应用。文章宣传 macOS 的 beta 版本（v1.0.0-beta.2），售价 9.99 美元。购买 beta 版支持该项目，并可获得最终发布版的访问权限。同时提供免费开源的命令行界面 (CLI) 版本。 macOS beta 版本未经签名，用户需手动授权，可通过 macOS 安全设置或运行特定命令行指令进行授权。鼓励用户通过电子邮件联系开发者寻求支持。 总而言之，本文旨在推广 PlainBudget，重点介绍付费的 macOS beta 版，并提供替代方案和必要的使用说明。

---

## 57. 失落的世界：侏罗纪公园游戏中“DNA序列”的逆向工程

**原文标题**: Reverse Engineering "DNA Sequences" in the Lost World: Jurassic Park Video Game

**原文链接**: [https://32bits.substack.com/p/under-the-microscope-the-lost-world](https://32bits.substack.com/p/under-the-microscope-the-lost-world)

好的，我已阅读了来自所提供URL的题为“逆向工程《失落的世界：侏罗纪公园》电子游戏中的“DNA序列””的文章。以下是摘要：

这篇文章深入探讨了用于理解PlayStation 1游戏《失落的世界：侏罗纪公园》中“DNA测序”小游戏运作方式的逆向工程过程。与实际的DNA测序不同，该游戏向玩家展示了一个简化的匹配拼图，其中涉及代表遗传密码的彩色瓷砖。

作者详细介绍了使用诸如Ghidra（一种软件逆向工程工具）等工具执行的技术分析，以检查游戏的ROM并揭示控制该小游戏的底层代码。分析揭示了游戏如何程序化地生成这些序列，以及如何评估玩家的行为。

主要发现包括：

*   “DNA”序列基于四种颜色，作者将其称为A、C、G和T（与实际的DNA碱基对名称相匹配）。
*   随着所需匹配瓷砖数量的增加，小游戏难度会逐渐增加。
*   分析揭示了游戏用于生成序列、比较玩家输入以及确定成功或失败的特定内存位置和算法。
*   作者揭示了游戏如何确定玩家何时未通过DNA测序谜题。

最终，这篇文章展示了逆向工程的力量，可以剖析看似简单的游戏机制，并理解隐藏在代码中的复杂细节。它还强调了游戏中对DNA测序的简化、游戏化表示与现实世界遗传学复杂性之间的差异。这是一次对游戏开发者如何使用有限的资源来创造引人入胜的游戏体验的精彩观察。

---

## 58. 数学机器 – 笔记本记录孩子的学习进度

**原文标题**: Math Machine – A notebook will show your kid how far they have travelled

**原文链接**: [https://kidswholovemath.substack.com/p/math-machine](https://kidswholovemath.substack.com/p/math-machine)

无法访问文章链接。

---

## 59. 尖叫者 - 一声吼开一声吼关的灯

**原文标题**: The Screamer – A yell-on yell-off light

**原文链接**: [https://rulethepla.net/the-screamer/](https://rulethepla.net/the-screamer/)

本文介绍了一个名为“尖叫者”的项目，这是一个声控灯开关，当有人对着它尖叫时，它可以打开或关闭。受到“拍手器”的启发，作者旨在利用现代技术改进这个概念。

该项目使用了Sonoff S31智能开关，因其ESP8266芯片的可破解性而被选中，从而可以通过ESPHome使用自定义固件。使用INMP441麦克风来检测尖叫声。由于Sonoff S31上的GPIO引脚有限，因此额外的ESP32板处理尖叫声检测处理。ESP32通过TX引脚连接到Sonoff。

ESP32运行Arduino代码，分析音频样本。它通过检查振幅是否超过阈值以及1000-4000 Hz频率范围内是否有足够的能量来确定是否存在尖叫声。如果检测到尖叫声且系统尚未处于“尖叫”状态（防抖动），则ESP32会将连接到Sonoff的GPIO引脚拉低，从而触发Sonoff的继电器切换灯。

作者有意避免使用更高级的语言（如Python）或在Raspberry Pi上运行该项目，以方便使用，旨在实现无需网络连接的即插即用体验。他们对其他尖叫声检测方法持开放态度。该项目使用ESPHome，可以与Home Assistant集成。

作者开发“尖叫者”主要是为了娱乐，并且因为人们觉得它很有趣。他们正在考虑完善该项目并将其分享到GitHub上，并有可能出售它。他们邀请感兴趣的读者注册以获取更新。

---

## 60. 展示 HN: Hydra (YC W22) – 基于 Postgres 的无服务器分析

**原文标题**: Show HN: Hydra (YC W22) – Serverless Analytics on Postgres

**原文链接**: [https://www.hydra.so/](https://www.hydra.so/)

Hydra：基于Postgres的无服务器分析平台，利用DuckDB进行分析查询处理。它旨在通过自动伸缩和自动缓存，在任何规模下提供可预测的亚秒级响应时间。Hydra提供开源、Postgres原生和无服务器执行，以及用于快速、实时分析的列式存储。

主要优势包括：

*   **性能：** 亚秒级分析性能。
*   **可扩展性：** 自动伸缩计算资源。
*   **集成：** 可与Node.js、Python、Ruby等各种技术栈配合使用。

多家行业领导者和创始人认可Hydra，强调其提升Postgres内部分析查询性能、消除对独立分析数据库的需求以及实现快速数据就地分析的能力。客户评价强调了易用性、高效数据压缩、响应迅速的支持以及平台的可靠性。pg\_duckdb项目被特别提及，它结合了Postgres和DuckDB的优势，可同时处理事务和分析工作负载。Hydra提供托管版本和开源选项，并邀请用户加入其社区，在Github上探索其资源。

---

## 61. 欧洲启动计划，吸引科学家离开美国

**原文标题**: Europe launches program to lure scientists away from the US

**原文链接**: [https://es.wired.com/articulos/europa-lanza-iniciativa-para-atraer-talento-cientifico-tras-recortes-en-ee-uu](https://es.wired.com/articulos/europa-lanza-iniciativa-para-atraer-talento-cientifico-tras-recortes-en-ee-uu)

欧盟启动“选择欧洲搞科研”计划，吸引研究人员和科学家，特别是来自美国的科研人员，他们因经费削减和前任美国政府下科学自由遭受威胁而寻求机会。该计划包括2025年至2027年间投资5亿欧元，目标是到2030年将研发投资提高到欧盟GDP的3%。

该计划旨在对抗欧洲领导人认为全球日益增长的对科学的漠视，并寻求为科学家提供稳定、长期的资金、改善的基础设施以及对开放和协作科学的承诺。欧盟计划简化其研究流程，并确保科学自由。

包括艾滋病毒研究、新冠病毒研究等领域的科研经费削减，以及因校园抗议活动而面临影响的大学等多种因素，正在促成美国潜在的“人才流失”。这导致申请国外职位的美国科学家激增，而寻求在美国获得机会的国际研究人员相应减少。

法国和德国等欧洲各国也在启动自己的计划以吸引美国科学家。西班牙正在积极招募生物技术、人工智能和半导体等领域的人才，提供可观的经济激励，并简化现有计划，以吸引年轻的和已成名的研究人员。其目标是通过利用不断变化的科学格局，将欧洲定位为全球研究和创新的领导者。

---

## 62. Rust的依赖开始让我担忧。

**原文标题**: Rust’s dependencies are starting to worry me

**原文链接**: [https://vincents.dev/blog/rust-dependencies-scare-me/?](https://vincents.dev/blog/rust-dependencies-scare-me/?)

Rust爱好者对依赖膨胀的担忧：一个实例及思考

---

## 63. 巴塞罗那附近有毒氯气云致超16万人居家避险

**原文标题**: Toxic chlorine cloud near Barcelona confines more than 160k indoors

**原文链接**: [https://www.theguardian.com/world/2025/may/10/toxic-chlorine-cloud-near-barcelona-confines-tens-of-thousands-indoors](https://www.theguardian.com/world/2025/may/10/toxic-chlorine-cloud-near-barcelona-confines-tens-of-thousands-indoors)

西班牙巴塞罗那南部维拉诺瓦-伊-拉赫尔特鲁一家存储泳池清洁产品的仓库发生火灾，释放出有毒氯气云，促使西班牙当局命令周边地区超过16万人留在室内。 民防部门建议五个沿海地区的居民关闭门窗。 截至报告发布时，尚未有人员伤亡报告，消防部门已部署多个单位控制火势并监测毒气云的毒性。 道路封闭，火车站关闭，以防止进入受影响区域。 仓库所有者认为可能是锂电池引起了火灾，一旦氯气着火，就很难扑灭。 当局预计毒气云会在火灾扑灭后消散，届时他们将解除实施的限制。

---

## 64. 所有旧金山湾区捷运列车因“计算机网络问题”而停运。

**原文标题**: All BART trains were stopped due to ‘computer networking problem’

**原文链接**: [https://www.kqed.org/news/12039472/bart-shuts-down-entire-train-service-due-to-computer-networking-problem](https://www.kqed.org/news/12039472/bart-shuts-down-entire-train-service-due-to-computer-networking-problem)

旧金山湾区捷运（BART）因大范围“计算机网络问题”于周四上午关闭了整个列车系统。此次故障始于早上5:30左右，给整个湾区的通勤者造成了严重的延误和中断。

该问题影响了BART监控列车位置和与之通信的能力，使其无法安全运行。BART官员表示，问题源于支持列车控制系统的计算机网络故障。技术人员努力恢复系统，并将问题根源确定为主要和备用计算机系统故障。

乘客在车站经历了严重拥堵，许多人被迫寻找替代交通方式。BART最初宣布预计延误两小时，但该系统最终恢复，并于早上8:30左右恢复正常运营，大约在最初关闭三个小时后。

BART官员为造成的不便表示歉意，并承认对通勤者造成了重大影响。他们强调了计算机网络对于安全可靠的列车运营的重要性，并承诺调查故障的根本原因，以防止未来发生类似事件。该事件引发了人们对BART基础设施可靠性及其应对意外系统故障能力的担忧。

---

## 65. 我想爱Linux，但它不爱我。

**原文标题**: I Want to Love Linux. It Doesn't Love Me Back

**原文链接**: [https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-1-built-for-control-but-not-for-people/](https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-1-built-for-control-but-not-for-people/)

一篇题为《我想爱Linux，但它不爱我》的博文中，一位失明Linux用户详细描述了困扰该操作系统的持续可访问性问题，尽管他们拥有多年的经验并努力修复这些问题。作者表达了对基本可访问性功能从一开始就损坏的沮丧，这些功能通常在登录之前就已损坏，并且需要大量的手动配置和脚本才能运行。

强调的具体问题包括初始启动和登录期间缺乏语音或盲文输出，带有未标记元素的损坏的安装程序，不可靠的屏幕阅读器持久性，以及经常无法正确加载的问题音频堆栈。作者还感叹依赖用户维护的脚本来实现基本的辅助功能，例如持久的Orca、Speakup和正确的音频路由。

像GTK4和Wayland这样的新系统组件因破坏辅助功能或在没有辅助功能支持的情况下启动而受到批评，将测试和修复的负担放在残疾用户身上。虽然MATE桌面环境因其相对的稳定性和可访问性而受到赞扬，但由于Orca中的一个错误，平铺窗口管理器i3现在无法使用。

作者称赞Debian的安装程序可访问性，但指出其过时的软件包抵消了这一优势。他们描述了使用Bedrock Linux来组合来自多个发行版的软件包以获得可用的设置，但承认了这种解决方案的复杂性和潜在的不稳定性。NixOS被认为是一个可能很有希望的未来解决方案，但目前对于一般用途来说过于复杂。

最终，作者感到沮丧的是，由于可访问性障碍以及克服这些障碍所需的技术专业知识，他们无法向他们的伴侣推荐Linux。这篇文章是该系列文章的第一篇，将深入探讨Linux生态系统中的具体可访问性问题。

---

## 66. 《活死人之夜》意外进入公有领域 (2019)

**原文标题**: "Night of the Living Dead" accidentally became public domain (2019)

**原文链接**: [https://screenrant.com/night-living-dead-movie-public-domain-copyright-accident/](https://screenrant.com/night-living-dead-movie-public-domain-copyright-accident/)

由于发行商的失误，乔治·罗梅罗的开创性僵尸电影《活死人之夜》意外进入公有领域。发行商在将电影名称从《食人肉之夜》更改时，忘记添加必要的版权声明。这意味着任何人都可以免费复制、发行和发布该电影，而无需支付版权费。

这个失误让罗梅罗损失了本可以从家庭录像带发行和重映中获得的数百万美元收入。尽管这部电影在票房上取得了可观的收入，但罗梅罗本人却没有从中获得多少收益。文章强调，尽管这部电影对恐怖类型片产生了巨大影响，并且罗梅罗创造了现代僵尸形象，但他从未获得他应得的经济回报。

具有讽刺意味的是，这部电影的公有领域地位反而促成了其持久的流行和经典地位。 通过各种发行渠道和频繁的电视播出，这部电影很容易获得，从而使其能够接触到更广泛的受众，并巩固其在电影史上的地位。 该电影的影响力体现在其11.4万美元的预算获得了3000万美元的票房收入，以及烂番茄上的高影评人和观众评分。

---

## 67. Show HN: Oliphaunt – macOS 原生 Mastodon 客户端

**原文标题**: Show HN: Oliphaunt – A native Mastodon client for macOS

**原文链接**: [https://testflight.apple.com/join/Epq1P3Cw](https://testflight.apple.com/join/Epq1P3Cw)

本文档是使用 TestFlight 的综合指南，TestFlight 是 Apple 公司的平台，用于在 iOS、iPadOS、macOS、Apple tvOS、visionOS 和 watchOS 等平台上进行应用程序的 Beta 测试。内容涵盖从通过电子邮件或公共链接接受邀请到安装和测试 Beta 版本的所有环节。关键要求包括拥有开发者指定的兼容设备和操作系统版本。

本指南解释了如何在各种设备上安装 TestFlight、接受邀请以及安装 Beta 应用程序。重点介绍了每个版本 90 天的测试期限、自动更新管理以及访问以前版本的权限。此外，还明确了应用内购买在 Beta 测试期间是免费的，但不会转移到 App Store 版本中。

至关重要的是，它详细说明了向开发者提供反馈的过程，可以通过 TestFlight 应用本身、共享屏幕截图或报告崩溃来完成。用户可以选择在使用公共链接提供反馈时保持匿名。该文档还解释了如何管理自动更新和测试 Beta 的早期版本。

最后，它介绍了如何直接联系开发者以及如何退出 Beta 测试计划。关于隐私和数据的部分强调，Apple 会收集崩溃日志、个人信息（如果提供）和使用数据，这些数据会与开发者共享，以改进他们的应用程序。

---

## 68. 异世界

**原文标题**: Another World

**原文链接**: [https://www.anotherworld.fr/anotherworld_uk/another_world.htm](https://www.anotherworld.fr/anotherworld_uk/another_world.htm)

异次元 - 官方网站

---

## 69. 为什么美国的ADHD发病率如此之高？

**原文标题**: Why Are ADHD Rates So Much Higher in the U.S.?

**原文链接**: [https://gizmodo.com/why-are-adhd-rates-so-much-higher-in-the-u-s-2000595804](https://gizmodo.com/why-are-adhd-rates-so-much-higher-in-the-u-s-2000595804)

Gizmodo文章《为何美国ADHD发病率如此之高？》探讨了美国ADHD诊断率显著高于其他国家的原因。尽管全球ADHD患病率都在上升，但美国遥遥领先。

文章指出，这种差异不仅仅是遗传或环境因素造成的，尽管这些因素确实起作用。相反，美国的文化、医疗和教育因素对更高的发病率有显著贡献。

专家强调了几个关键点：

*   **医疗：** 美国更频繁地进行ADHD筛查，使用诊断标准更广泛的DSM，并允许ADHD药物的直接面向消费者广告，从而提高了人们的认知度和诊断率。
*   **社会/文化：** 美国对ADHD的认知度提高可能导致一些行为被迅速贴上紊乱的标签。文章还认为，较低的耻辱感可能会鼓励更多人寻求治疗。学校对自我控制的强调也可能导致ADHD症状的发现。
*   **教育：** ADHD诊断可以带来学校资源和便利，从而产生诊断的动机。学校在标准化考试中取得好成绩的压力也可能抬高诊断率。

文章还强调，空气污染、铅暴露和贫困等环境因素可能会影响患病率。此外，历史因素、利他林在美国的早期引入和营销，以及女性ADHD的诊断不足也导致了这种差异。

本质上，美国较高的ADHD发病率似乎是诊断实践、社会压力和历史背景复杂相互作用的结果，而不是纯粹的生物现象。

---

## 70. Show HN: 一个与后端无关的 Ruby 框架，用于构建响应式桌面应用

**原文标题**: Show HN: A backend agnostic Ruby framework for building reactive desktop apps

**原文链接**: [https://codeberg.org/skinnyjames/hokusai](https://codeberg.org/skinnyjames/hokusai)

无法访问文章链接。

---

## 71. 如何与朋友一起创办学校

**原文标题**: How to start a school with your friends

**原文链接**: [https://prigoose.substack.com/p/how-to-start-a-university](https://prigoose.substack.com/p/how-to-start-a-university)

无法访问文章链接。

---

## 72. 人工智能幻觉正在恶化——而且会持续存在

**原文标题**: AI hallucinations are getting worse – and they're here to stay

**原文链接**: [https://www.newscientist.com/article/2479545-ai-hallucinations-are-getting-worse-and-theyre-here-to-stay/](https://www.newscientist.com/article/2479545-ai-hallucinations-are-getting-worse-and-theyre-here-to-stay/)

人工智能大语言模型中的“幻觉”问题日益严重

本文探讨了人工智能大语言模型（LLM）如ChatGPT和Gemini中持续存在且可能恶化的“幻觉”问题。“幻觉”指的是人工智能生成的错误，包括将虚假信息作为真实信息呈现、给出不相关的答案以及未能遵循指令。

最近的测试表明，一些较新的模型，即使是那些具有“推理升级”的模型，也表现出比旧版本更高的幻觉率。例如，OpenAI的o3和o4-mini模型在总结事实时显示出比o1模型显著更高的幻觉率。同样，DeepSeek-R1模型的幻觉率也比其开发者之前的模型增加了两位数。

尽管各公司最初希望幻觉会随着时间的推移而减少，但最近的数据对这一假设提出了挑战。Vectara排行榜等评估摘要事实一致性的排名表明，推理模型和非推理模型的幻觉率相似。然而，这些排名也是不完善的；它们可能混淆了不同类型的幻觉，并且可能无法准确反映LLM在文本摘要之外的任务中的表现。

像Emily Bender这样的专家认为“幻觉”一词存在问题，暗示错误很少见，并且将技术拟人化。Arvind Narayanan强调，人工智能模型也会犯其他错误，例如使用不可靠或过时的信息。

文章的结论是，容易出错的人工智能可能将长期存在。文章建议仅在人工核实人工智能答案的速度快于独立研究的情况下使用人工智能，或者完全避免依赖人工智能聊天机器人获取事实信息。

---

## 73. GNU Taler 1.0 发布

**原文标题**: GNU Taler 1.0 Released

**原文链接**: [https://www.taler.net/en/news/2025-01.html](https://www.taler.net/en/news/2025-01.html)

GNU Taler v1.0 发布，标志着一个重要里程碑，即 Taler Operations AG 在瑞士成立，并以瑞士法郎运营支付系统。此版本被视为公开测试版，面向瑞士的个人和企业，即使目前尚无商店接受 Taler。未来版本保证向后兼容。

GNU Taler 是一种免费软件支付系统，在确保当局能够看到收入的同时，优先考虑付款人的隐私。它使用由受监管的支付服务提供商发行的数字现金，这些数字现金存储在用户控制的钱包中，并由托管银行账户支持。交易几乎是即时的，需要在线连接以防止双重支付，但也支持离线销售点。Taler 被设计为可扩展的，适用于各种应用，包括区域货币、商业部署，以及潜在的中央银行数字货币 (CBDC)。

1.0 版本包含超过 200 个已解决的问题，包括单签名提款等性能改进、通过确定性签名进行刷新的后量子准备、简化的端点设计、用于反洗钱的每收款人统计、幂等的两步操作、iOS 钱包中的安全增强，以及法律文件的完整翻译。

钱包和其他组件（如交易所、商户后端、同步和银行）的下载链接已通过 GNU FTP 镜像提供。编译需要 GNUnet v0.24.1 或当前的 Git master。该项目由欧盟委员会和瑞士联邦教育、研究和创新国务秘书处 (SERI) 共同资助。

---

## 74. 宇宙-482号下降舱再入预测

**原文标题**: Cosmos-482 descent craft re-entry prediction

**原文链接**: [https://blogs.esa.int/rocketscience/2025/05/07/reentry-prediction-soviet-era-venera-venus-lander-cosmos-482-descent-craft/](https://blogs.esa.int/rocketscience/2025/05/07/reentry-prediction-soviet-era-venera-venus-lander-cosmos-482-descent-craft/)

本文提供欧洲空间局空间碎片办公室关于苏联“宇宙-482”号着陆舱失控再入的实时更新。该着陆舱是53年前发射的苏联金星探测器金星着陆舱，原计划用于探测金星。由于发射器故障，它一直停留在地球轨道上。

本文追踪了预测的再入时间，最初的预测范围很广，但随着事件临近而缩小。早期预测范围为2025年5月10日06:18 UTC至08:16 UTC，不确定性窗口很大（+/- 18.07小时至+/- 8.61小时）。后来的更新修正了预测，最终估计为2025年5月10日06:16 UTC，不确定性为+/- 0.36小时。德国上空的雷达观测大约发生在04:30 UTC和06:04 UTC，表明再入可能已经发生。未收到视觉确认或地面撞击报告。

预计该舱将再入北纬52°至南纬52°之间。关键信息包括显示再入时间和高度预测变化的图表。本文强调了此次再入的独特之处：着陆器为金星恶劣大气层设计的坚固结构可能使其完好无损地到达地球表面，并且着陆器的形状使再入成为测量大气密度的意外科学实验。虽然卫星再入很常见，但受伤的风险极低。本文还包括社区评论，其中包含问题和观察结果。

---

## 75. 新工具：lsds – 一处列出所有Linux块设备及设置

**原文标题**: New Tool: lsds – List All Linux Block Devices and Settings in One Place

**原文链接**: [https://tanelpoder.com/posts/lsds-list-linux-block-devices-and-their-config/](https://tanelpoder.com/posts/lsds-list-linux-block-devices-and-their-config/)

本文介绍了一款由Tanel Poder创建的名为`lsds`的全新Python版Linux工具，用于整合关于块设备的信息。`lsds` 不再需要运行多个命令（如 `lsblk`、`lsscsi` 和 `nvme list`），而是直接从 `/sys/class/block/...` 目录读取相关数据，从而在一个地方提供每个磁盘的全面概述。

该工具显示关键属性，如设备名称、主/次设备号、大小、类型、调度器、旋转状态、型号、队列深度、请求数量和写入缓存设置。它包括自定义输出的功能，例如选择特定列、向默认集添加列、显示数据源的详细模式以及易于阅读的透视输出格式。

本文演示了如何使用 `lsds` 来识别不同类型的存储设备（NVMe SSD、机械硬盘、USB 驱动器）及其配置。它还强调了其在确定关键方面（如硬件扇区大小 (`HWSEC`)、NVMe 队列深度 (`NVME_QDEPTH`) 和对强制单元访问 (`FUA`) 的支持）方面的实用性，`FUA` 表明写入是否立即刷新到持久存储。作者指出 `NVME_QDEPTH` 反映的是 Linux 级别的最大值，不一定是单个设备的容量。

这些示例展示了 `lsds` 如何帮助用户了解其存储设备的性能特征和缓存行为，从而能够就数据放置和系统优化做出更明智的决策，尤其是在处理持久写入要求时。

---

## 76. 乐高GPT：生成物理稳定且可建造的乐高模型

**原文标题**: LegoGPT: Generating Physically Stable and Buildable Lego

**原文链接**: [https://avalovelace1.github.io/LegoGPT/](https://avalovelace1.github.io/LegoGPT/)

LegoGPT 是一种从文本提示生成物理稳定且可搭建乐高模型的新方法。该系统采用一个在新建数据集 StableText2Lego 上微调的大型语言模型，该数据集包含超过 47,000 个带有详细描述和验证物理稳定性的乐高结构。

该过程包括训练语言模型 (LLaMA-3.2-Instruct-1B) 以预测乐高设计序列中的下一个砖块，使用从下到上的栅格扫描顺序。 在推理过程中，LegoGPT 以增量方式生成设计，并在每次放置砖块后检查有效性和物理稳定性。 一种高效的物理感知回滚机制会移除不稳定的砖块及其后续添加，并从上一个稳定状态恢复生成。

StableText2Lego 数据集通过将 ShapeNetCore 网格转换为乐高设计，增加结构变化，过滤物理稳定的结构，并使用 GPT-4o 生成描述性说明来构建。

LegoGPT 能够生成与文本提示高度吻合的、多样且美观的乐高模型。 该系统还包含一种基于文本的乐高纹理化方法，用于创建彩色和纹理设计。 生成的模型可以手动和通过机械臂自动组装。 研究人员正在发布 StableText2Lego 数据集、代码和模型。

---

## 77. 华为麒麟X90或是该公司的“苹果硅”时刻

**原文标题**: Huawei's Kirin X90 may be the company's 'Apple Silicon' moment

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/huaweis-kirin-x90-may-be-the-companys-apple-silicon-moment-matebook-pro-2025-features-in-house-hardware-and-software](https://www.tomshardware.com/pc-components/cpus/huaweis-kirin-x90-may-be-the-companys-apple-silicon-moment-matebook-pro-2025-features-in-house-hardware-and-software)

华为麒麟X90 SoC的潜在突破：或将成为其“苹果芯片”时刻。搭载麒麟X90的全新Matebook Pro 2025笔记本电脑运行鸿蒙操作系统，该芯片是海思定制的Arm架构设计。此举使华为能够整合其软硬件生态系统，减少因美国制裁对西方技术的依赖。

麒麟X90代号为Charlotte Pro，采用10核(4+4+2)/20线程布局，类似于Pura 70手机中的麒麟9010，主核采用泰山V121架构，性能核采用泰山V120架构，效率核可能采用Cortex-A510。虽然性能数据有限，但据说面向服务器的泰山V120架构在单核性能方面与AMD的Zen 3相当。然而，该芯片可能采用中芯国际较旧的7nm工艺制造，这可能会限制其潜力。

鸿蒙操作系统的成功取决于应用程序兼容性和开发者支持。虽然兼容层是可能的，但华为需要强大的生态系统和必要的应用程序才能与苹果竞争。构建本土软件替代方案也是一种选择，这符合中国技术自给自足的目标。预计Matebook Pro于5月19日发布后，将进行麒麟X90的性能测试。

---

## 78. 实现结构体数组

**原文标题**: Implementing a Struct of Arrays

**原文链接**: [https://brevzin.github.io/c++/2025/05/02/soa/](https://brevzin.github.io/c++/2025/05/02/soa/)

本文演示了如何在 C++26 中使用反射来实现“结构体数组”（SoA）数据结构，特别是 `SoaVector<T>`。与存储结构体数组 (AoS) 不同，SoA 为结构体的每个非静态数据成员存储单独的数组，旨在获得更好的内存利用率。

该实现重点关注一个 `Point` 结构体 (char x, int y)，并构建一个管理 `char* x`、`int* y`、`size_t size` 和 `size_t capacity` 的 `SoaVector`。它利用 `std::meta::define_aggregate` 来基于 `T` 的成员动态创建 `Pointers` 结构体（包含 `x` 和 `y` 指针）。

文章随后逐步讲解 `push_back`、`grow`（用于动态调整大小）、用于内存管理的析构函数和索引运算符的实现。 主要挑战包括 C++26 反射中缺乏完整的代码生成能力，需要诸如 `std::define_static_array` 之类的变通方法，以便对数据成员信息进行 constexpr 操作。 索引运算符以两种方式实现：一个 `const` 版本，按值返回一个 `Point`，以及一个可变版本，返回一个 `PointRef`（一个包含对各个数据成员的引用的结构体），从而支持就地修改。 注释用于自动派生调试输出。

总体目标是说明如何使用 C++26 反射基于其他结构的成员生成数据结构，从而创建一个 `SoaVector`，该结构体提供给定类型 `T` 的结构体数组表示。

---

## 79. 并非三岁扫烟囱工 (2022)

**原文标题**: Not a three-year-old chimney sweep (2022)

**原文链接**: [https://fakehistoryhunter.net/2022/07/26/not-a-3-year-old-chimney-sweep/](https://fakehistoryhunter.net/2022/07/26/not-a-3-year-old-chimney-sweep/)

该文章驳斥了1933年英国百代电影展示一名3岁儿童从事烟囱清扫工作的说法。作者认为，这段拍摄于1929-1930年左右柏林的影像，描绘的是一个孩子为了好玩而打扮成烟囱清扫工，而不是真正从事童工劳动。

主要论点包括：影片中存在德国标牌和独特的柏林人行道，与1929年波兰杂志上刊登的同一对父子的照片相符，并标注为在柏林拍摄。虽然过去存在儿童烟囱清扫工，但作者强调，即使在当时，使用如此年幼的儿童也很罕见，并且自1903年以来在德国属于非法行为。文章强调了幼儿的迷你工具，这些工具对于实际工作无效，并且烟囱清扫技术已经发展到不再需要攀爬烟囱的地步。

作者还提到了在德国将儿童打扮成烟囱清扫工以求好运的流行做法。通过众包在线研究，该男子和他的儿子被确认为奥托·伯恩克和霍斯特·伯恩克，并出现在全球出版物中。作者的结论是，这段影像很可能展示了霍斯特扮演烟囱清扫工的角色，可能是为摄影师或新闻短片，并强调他不是真正的童工。调查仍在继续，以揭示更多关于伯恩克家族的故事。

---

## 80. Void: 开源光标替代方案

**原文标题**: Void: Open-source Cursor alternative

**原文链接**: [https://github.com/voideditor/void](https://github.com/voideditor/void)

Void：Cursor 代码编辑器的开源替代方案。其主要功能包括直接作用于代码库的 AI 代理、用于检查点和可视化变更的版本控制功能，以及使用任何 AI 模型并在本地托管的能力。 隐私是重点：Void 直接向提供商发送消息，避免在其端保留数据。

文章引导新用户访问项目网站、Discord 服务器和项目看板以获取更多信息。 它鼓励贡献并参与 Discord 上举行的每周会议。 贡献指南可以在 HOW_TO_CONTRIBUTE 文档中找到。

由于 Void 从 VS Code 仓库 fork 而来，因此提供了一个专门的 `VOID_CODEBASE_GUIDE` 来帮助浏览代码库。

可以通过 Discord 服务器或通过电子邮件 hello@voideditor.com 获得支持。

---

## 81. Show HN: BlenderQ – 用于管理多个Blender渲染的TUI

**原文标题**: Show HN: BlenderQ – A TUI for managing multiple Blender renders

**原文链接**: [https://github.com/KyleTryon/BlenderQ](https://github.com/KyleTryon/BlenderQ)

BlenderQ：本地Blender渲染队列管理和监控终端UI工具。它使用Node.js编写，Ink构建TUI，允许用户将多个`.blend`文件添加到渲染队列，并在命令行跟踪进度。功能包括交互式终端界面、主题支持和简单导航。

该工具目前处于beta阶段，需要Node.js (v20+)和Blender (v3.5+)。推荐使用Nerd Fonts以显示图标。可以使用npm或pnpm轻松安装。用户可以单独添加文件，或者指定目录让BlenderQ搜索`.blend`文件。

作者选择Node.js是因为熟悉它，以及Ink中提供了受React启发的组件，这有助于快速开发出功能齐全且易于维护的TUI。虽然承认Python在直接Blender集成方面的潜力，但Node.js能够更快地发布一个可用的工具。

---

## 82. 发明冒险游戏 (1984)

**原文标题**: Inventing the Adventure Game (1984)

**原文链接**: [http://www.warrenrobinett.com/inventing_adventure/](http://www.warrenrobinett.com/inventing_adventure/)

沃伦·罗宾内特于1983-84年撰写的《冒险游戏的创造》一书，探讨了冒险游戏的早期历史和设计原则。该手稿考察了从依赖文本描述和键入命令的文本冒险游戏（如巨洞冒险）到第一款动作冒险电子游戏《Atari 2600 冒险》的演变。它深入研究了这些游戏的关键要素，包括玩家输入、物品、生物和迷宫设计。

罗宾内特还进一步探讨了《冒险》作为一种教育模拟游戏，并以洛基的靴子（一款Apple II互动游戏，允许玩家构建机器并学习电路知识）为例。该书还包含对有抱负的游戏设计师的建议，探讨了创意生成、游戏内的空间设计（包括缩放和 3D 视角）以及创建可信的生物行为。

该手稿最后附有附录，详细介绍了《冒险》和《洛基的靴子》的程序结构。本书为了解电子游戏开发的先驱时代以及塑造冒险游戏类型的创新思维提供了宝贵的见解。

---

## 83. 初创公司 Google 文档模板

**原文标题**: Google Doc Templates for Startups

**原文链接**: [https://www.templatesbypaul.com/](https://www.templatesbypaul.com/)

本文由Paul（前Keeper的CEO/创始人）撰写，提供了一系列对初创公司有用的Google Doc模板。他分享这些模板是因为他相信记录可重复的流程。这些模板分为两个主要部分：通用模板和产品管理模板。

**通用模板**包括：

*   **决策文档：** 用于就Type 2决策达成团队共识。
*   **回顾文档：** 用于改善团队凝聚力和流程。
*   **战略文档：** 用于制定和传达战略。
*   **项目跟踪器：** 用于跟踪任务和项目状态。
*   **调查文档：** 用于调查不明确的问题。
*   **直属汇报1:1：** 用于经理一对一会议的基本模板。
*   **全体会议幻灯片：** 用于大型团体会议的幻灯片。
*   **角色与职责澄清器：** 用于消除歧义。

**产品管理模板**包括：

*   **PRD（产品需求文档）：** 产品改进提案的真理来源。
*   **评估报告：** 产品变更效果分析。
*   **产品愿景文档：** 愿景陈述指南。
*   **职级指南：** 通用产品管理职级指南。
*   **面试练习：** PM面试练习示例。

作者根据其作为产品负责人和创始人的经验提供这些模板，希望它们能成为初创公司的宝贵工具。他还提供了他的联系方式。

---

## 84. 星链用户终端拆解

**原文标题**: Starlink User Terminal Teardown

**原文链接**: [https://www.darknavy.org/blog/a_first_glimpse_of_the_starlink_user_ternimal/](https://www.darknavy.org/blog/a_first_glimpse_of_the_starlink_user_ternimal/)

本文详细介绍了DARKNAVY对星链标准执行器（Rev3）用户终端天线 (UTA) 的拆解和分析。UTA的PCB板主要由意法半导体 (STMicroelectronics) 的射频前端芯片构成，核心控制组件，包括定制的ST制造的四核Cortex-A53 SoC，集中在一侧。

DARKNAVY通过拆焊eMMC芯片提取了UTA的固件。提取的固件大部分未加密，揭示了引导链、内核和部分文件系统。分析表明，其网络堆栈架构类似于DPDK，即用户空间C++程序处理网络数据包，绕过内核以提高效率。有趣的是，该固件包含看似为卫星或地面网关设计的功能。

为了促进持续的研究，DARKNAVY为Rev3固件构建了一个基于QEMU的模拟环境，成功运行和调试了各项服务。UTA还集成了STSAFE-A110安全芯片（CC EAL5+ 认证），提供唯一的设备标识符，管理用于卫星通信身份验证的公钥证书，并派生对称加密密钥。该芯片充当独立的信任根。

分析发现了一个“以太网数据记录器”程序，该程序基于类似pcap_filter的规则捕获加密的卫星遥测数据。本文提出了对用户终端的 /root/.ssh/authorized_keys 文件中自动添加41个SSH公钥的担忧，这可能会造成安全风险。文章最后强调了卫星互联网领域中新兴的安全挑战，强调了数字和物理安全考虑的重要性。

---

## 85. 微软量子芯片奠基研究被指存在数据操控

**原文标题**: Data manipulations alleged in study that paved way for Microsoft's quantum chip

**原文链接**: [https://www.science.org/content/article/data-manipulations-alleged-study-paved-way-microsoft-s-quantum-chip](https://www.science.org/content/article/data-manipulations-alleged-study-paved-way-microsoft-s-quantum-chip)

无法访问文章链接。

---

## 86. 人工智能扑克的诞生？来自1984年WSOP的信件

**原文标题**: The birth of AI poker? Letters from the 1984 WSOP

**原文链接**: [https://www.poker.org/latest-news/the-birth-of-ai-poker-letters-from-the-1984-wsop-a4v2W4N4X3EP/](https://www.poker.org/latest-news/the-birth-of-ai-poker-letters-from-the-1984-wsop-a4v2W4N4X3EP/)

短文《AI扑克的诞生？来自1984年WSOP的信件》聚焦于迈克·卡罗写给亨利·博林格的一封信，信中涉及计算机扑克策略的潜力。这封信写于1984年世界扑克大赛期间，暗示了卡罗早期对使用计算机分析甚至可能玩扑克的探索。

这篇文章表明，卡罗的信件代表了AI驱动的扑克策略发展的萌芽阶段。虽然没有明确详细说明卡罗正在追求的具体想法，但暗示了他正在考虑如何使用计算机来理解和优化扑克游戏。早在1984年就出现这种讨论的事实突显了卡罗的远见卓识，并使他成为最终复杂的AI扑克机器人兴起的潜在早期先驱。这封信是计算机科学与扑克策略交叉领域的一个历史标志。

---

## 87. 依据劳森判据衡量聚变能量增益进展

**原文标题**: Progress toward fusion energy gain as measured against the Lawson criteria

**原文链接**: [https://www.fusionenergybase.com/articles/continuing-progress-toward-fusion-energy-breakeven-and-gain-as-measured-against-the-lawson-criteria](https://www.fusionenergybase.com/articles/continuing-progress-toward-fusion-energy-breakeven-and-gain-as-measured-against-the-lawson-criteria)

本文探讨了在实现聚变能量增益方面的进展，特别关注以劳森判据衡量的进步。劳森判据是一组持续聚变反应产生净能量所需的条件，定义了所需的等离子体密度、温度和约束时间。

文章可能重点介绍了近期的聚变实验，特别是使用托卡马克和惯性约束聚变（ICF）方法的实验，在接近甚至超过劳森判据的关键组成部分方面取得了显著进展。这可能包括在联合欧洲环形加速器（JET）或国家点火装置（NIF）等实验中，实现破纪录的等离子体温度或约束时间等具体成就。

然而，文章可能承认，超过个别判据要素并不能保证净能量增益。同时实现所有必需条件并保持其稳定是一个巨大的挑战。文章可能会讨论正在进行的研究和开发工作，重点是提高等离子体稳定性、增强约束技术以及开发更高效的加热和燃料输送系统。

最后，文章可能强调，虽然在劳森判据方面的进展令人鼓舞，但在商业上可行的聚变能源成为现实之前，仍然存在重大的工程和科学障碍。这可能包括与材料科学、反应堆设计以及聚变发电厂的总体成本效益相关的问题。

---

## 88. 代数效应：又一个臻于完美的错误？

**原文标题**: Algebraic Effects: Another mistake carried through to perfection?

**原文链接**: [https://kjosib.github.io/Counterpoint/effects.html](https://kjosib.github.io/Counterpoint/effects.html)

Beth Kjos 批评了效应系统，认为它们与异常一样，都存在动态作用域的“原罪”，导致大型、长期运行的代码库出现可维护性问题。她承认一些有副作用的语言使用词法/静态作用域，但认为这在很大程度上复制了面向对象依赖注入，而这是一种被充分理解的实践。

根据 Kjos 的说法，核心问题在于效应系统模糊了因果关系，使得维护人员难以在本地推理代码。她认为，设计良好的面向对象架构通过参数传递（依赖注入）明确地表示这些关系。

Kjos 回忆了她在一家过度使用动态作用域的公司的工作经历。她的团队成功地过渡到显式依赖注入，从而使开发人员更加快乐和高效。她认为效应系统违反了 "Python 之禅 "中显式性和简单性的原则，而参数传递是一种被充分理解且有效的替代方案。

最后，Kjos 提出，围绕受检异常的工业问题源于它们与依赖注入的不良交互。她建议了一些替代方案，例如将异常处理程序作为对象传递，以改善错误处理。她的关键点是，对什么可能出错的检查应该适用于谁创建了对象，而不是谁调用了方法。她总结说，动态作用域是有问题的，而显式控制是更可取的。

---

## 89. 使用Grasshopper的参数化建模

**原文标题**: Parametric Modeling with Grasshopper

**原文链接**: [https://baharmon.github.io/basics](https://baharmon.github.io/basics)

本文介绍了使用Grasshopper进行参数化建模的基础知识。Grasshopper是Rhino的可视化编程界面。本文讲解了如何在Grasshopper环境中创建基本的几何元素，例如点、线、折线、曲线和曲面。

本文首先概述了Grasshopper的基础原理，强调其可视化编程方法允许用户通过链接数据和函数来算法式地生成几何图形。它重点介绍了使用参数存储数据和使用组件执行操作。

接下来，教程深入讲解了创建特定几何元素的方法。可以使用“构建点”组件，通过滑块或面板提供的x、y和z坐标来定义点，也可以通过引用Rhino中绘制的点来定义点。可以通过指定起点和终点、指定具有方向和长度的起点，或者通过引用Rhino中绘制的线来创建线。折线是通过连接有序的点序列形成的，并且可以闭合形成多边形。曲线，特别是NURBS曲线，是通过控制点插值形成的，控制点可以通过多种方法创建，包括正弦波。最后，可以使用原始曲面组件或自由曲面组件来创建曲面，例如“边界曲面”、“直纹曲面”和“放样”。

本文最后指出，可以通过拉伸曲面或使用原始组件（如盒子或球体）来创建实体对象。本文还提供了若干学习资源的链接，并暗示了关于创建参数化长椅的后续教程。

---

## 90. Audiobookshelf: 自托管有声读物和播客服务器

**原文标题**: Audiobookshelf: Self-hosted audiobook and podcast server

**原文链接**: [https://www.audiobookshelf.org/](https://www.audiobookshelf.org/)

本文介绍Audiobookshelf，一款用于管理和收听有声读物和播客的自托管服务器应用程序。内容表明 Audiobookshelf 允许用户在自己的服务器上维护个人音频内容库。“文档”、“用户指南”和“常见问题解答”等部分的存在表明该文章为使用该应用程序提供了全面的支持。“如何支持”的包含表明作者乐于接受对该项目的贡献或捐赠。最后，“展示”可能重点介绍了用户如何使用 Audiobookshelf 的真实示例。本质上，该文章是 Audiobookshelf 的着陆页，该平台使用户能够通过自托管来控制他们的有声读物和播客收听体验。

---

## 91. 苹果iMessage PQ3协议的形式化分析 [pdf]

**原文标题**: A Formal Analysis of Apple's iMessage PQ3 Protocol [pdf]

**原文链接**: [https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf)

本文档似乎是对苹果 iMessage PQ3 协议的技术分析，很可能是逆向工程的结果。PQ3 是一种后量子密码协议，旨在保护 iMessage 对话免受窃听，包括来自拥有量子计算机的攻击者的攻击。

根据 PDF 内容，这很可能是对完整文章的高度压缩且不完整的表示。内容显示了压缩的数据流和代码片段，表明了该协议的设计。一个合适的摘要应包括以下内容（尽管此信息无法从提供的片段中完全提取）：

*   **PQ3 的目标：** 为 iMessage 提供前向保密和后量子安全性，这意味着即使当前密钥泄露，过去的对话仍然安全，并且该加密能够抵抗量子计算攻击。

*   **密钥交换机制：** 文章可能分析了密钥交换方法。

*   **加密方案：** 该文档可能深入研究了 PQ3 协议中使用的加密算法的细节。

*   **棘轮机制：** 文章可能分析了该协议如何使用棘轮机制来持续为每条消息生成新密钥，从而进一步增强安全性。

*   **安全属性：** 文章很可能对 PQ3 的安全属性进行了评估，可能指出了优点和潜在的弱点。

*   **技术细节：** 内容表明该分析可能涵盖 iMessage PQ3 协议中涉及的特定数据结构、密码学原语和消息流程图。

---

## 92. 伊丽莎白·霍姆斯的合伙人为新的生物科技检测初创公司筹集数百万美元

**原文标题**: Elizabeth Holmes' partner raises millions for new biotech testing startup

**原文链接**: [https://www.npr.org/2025/05/10/nx-s1-5393950/elizabeth-holmes-theranos-billy-evans-blood-testing](https://www.npr.org/2025/05/10/nx-s1-5393950/elizabeth-holmes-theranos-billy-evans-blood-testing)

因欺诈罪被定罪的Theranos诈骗犯伊丽莎白·霍尔姆斯的伴侣比利·埃文斯为一家名为Haemanthus的新生物科技初创公司筹集了数百万美元，该公司旨在创建人工智能引导的医疗检测产品。据报道，尽管霍尔姆斯因Theranos欺诈投资者而入狱，但她仍在为埃文斯的新事业提供建议。

Haemanthus在希腊语中意为“血花”，目前处于早期阶段，雇佣了大约十几名员工，其中一些人之前曾在Luminar Technologies与埃文斯共事。资金主要来自朋友、家人和支持者。该公司专注于利用光探测技术和拉曼光谱技术来开发负担得起的、可商业化的诊断测试。最初的专利表明，该技术可以分析生物材料，如汗液、尿液、唾液或小血样。

虽然霍尔姆斯由于被禁止担任上市公司的高管或董事而在Haemanthus中不会担任正式职务，但她正在积极为埃文斯提供指导。霍尔姆斯还计划在出狱后重返医疗保健行业，并据报道一直在撰写专利。

---

## 93. 太阳可能正在进入更强烈的11年周期时代

**原文标题**: The Sun May Be Entering an Era of Stronger 11-Year Cycles

**原文链接**: [https://www.scientificamerican.com/article/stronger-solar-activity-cycles-may-be-in-the-suns-forecast/](https://www.scientificamerican.com/article/stronger-solar-activity-cycles-may-be-in-the-suns-forecast/)

本文探讨了当前的太阳活动周期以及未来出现更强太阳活动周期的可能性。太阳目前正处于高活动期，接近其11年周期的最大值，导致壮观的极光，并对卫星和地球电网构成潜在风险。

科学家通过监测太阳黑子来跟踪太阳活动周期的进程，并指出当前的周期已经产生了大量的太阳黑子。虽然最近活动有所减缓，但仍有可能出现另一次高峰。展望未来，研究人员正在探索更长周期的可能性，例如格莱斯贝格周期，这可能预示着未来几十年太阳活动会增加。

虽然由于数据有限，关于这些更长周期的存在尚有争议，但普遍认为未来的太阳活动周期可能比相对较弱的第24太阳活动周期更活跃。这种活动增加引起了人们对空间天气对技术（特别是卫星和电网）的影响，以及宇航员冒险进入地球保护性磁场之外的安全性的担忧。因此，改进空间天气预报对于保护基础设施和未来的太空任务至关重要。

---

## 94. CL1：首个可部署的代码化生物计算机

**原文标题**: The CL1: the first code deployable biological computer

**原文链接**: [https://corticallabs.com/cl1.html](https://corticallabs.com/cl1.html)

Cortical Labs公司推出CL1，号称世界首款可代码部署的生物计算机。它将培养在富营养液中的真实神经元与硅芯片相结合。芯片刺激神经元并接收其电脉冲，神经元在硅片上生长，从而形成生物神经网络。

神经元存在于由生物智能操作系统(biOS)管理的模拟世界中，允许用户通过代码直接与它们交互。该系统促进了生活在数字环境中的可编程有机神经网络。

CL1的关键特性包括：神经元和软件实时交互的闭环系统；包含所有生命支持、记录和应用的自成一体的设计；以及通过Cortical Cloud连接外部设备的即插即用功能。该设备具有用于神经通讯的双向刺激和读取接口、用于数据可视化的触摸屏，以及通过USB和其他端口的可扩展性。

CL1旨在通过提供相关的人类数据和见解，为医学和研究实验室中的动物试验提供一种伦理上更优越的替代方案。它还有望通过实时捕获神经适应性和学习能力，来促进更深入的学习，从而有可能揭示疾病机制以及化合物对认知的影响。由于其低功耗，它是可持续的，旨在以最少的输入使神经元存活长达六个月。

---

## 95. Fui：用于在TTY环境中与帧缓冲交互的C语言库

**原文标题**: Fui: C library for interacting with the framebuffer in a TTY context

**原文链接**: [https://github.com/martinfama/fui](https://github.com/martinfama/fui)

Fui是一个C语言库，旨在TTY环境中创建帧缓冲用户界面。它允许开发者直接与帧缓冲设备交互，从而实现底层图形编程。

Fui的主要特性包括：

*   **基于图层的绘图:** 支持将像素值绘制到多个图层，然后将这些图层合成并渲染到帧缓冲。
*   **图元绘图函数:** 提供绘制基本形状（如线条、矩形和圆形）的函数。
*   **文本渲染:** 提供基于位图字体的文本渲染功能。
*   **事件处理:** 使用libevdev管理键盘和鼠标输入，并提供可扩展的通用事件系统，以支持其他事件类型。
*   **声音系统:** 包含一个基于ALSA的基础声音系统，用于播放正弦波和和弦。

该库通过`make`和`sudo make install`进行安装。它是静态链接的，简化了依赖管理。为了避免使用Fui的程序需要root权限，建议用户将自己添加到`video`和`input`组。

该代码库包含演示Fui特性的示例，例如`main.c`和`bodies.c`，一个展示声音系统的简单小行星游戏，以及使用cmocka实现的测试。

---

## 96. Show HN: Hyper – 首重标准的 React 替代方案

**原文标题**: Show HN: Hyper – Standards-first React alternative

**原文链接**: [https://nuejs.org/blog/standards-first-react-alternative/](https://nuejs.org/blog/standards-first-react-alternative/)

Hyper：以标准为先的React替代方案，旨在构建简洁、可扩展的用户界面，并强调结构(HTML)、样式(CSS)和行为(JavaScript)之间的关注点分离。 它与React的整体架构形成鲜明对比，认为React混合了这些关注点。

Hyper强调使用语义化的HTML和CSS进行样式设计，提倡一种解耦的设计系统，允许轻松更换主题而无需修改组件代码。 文章批评了诸如CSS-in-JS和Tailwind等方法，因为它们将设计与组件紧密耦合，导致维护问题和样板代码。

它通过简单和复杂的表格组件示例展示了Hyper的优势，与ShadCN/UI等React解决方案相比， JavaScript包大小有所减小。 一个仪表盘示例说明了如何使用Hyper的解耦方法轻松更换设计系统。

文章声称Hyper简化了UI开发，提倡一种范例，即应用程序一开始很简单，并且随着规模的扩大仍然如此。 它还讨论了Hyper的未来路线图，包括全栈应用程序示例、面向开发者和AI模型的生成式UI功能、直观的路由/导航、跨组件通信和云部署。

常见问题解答中涉及了与Svelte和Vue的比较、Nue的性质（Hyper最终将取代Nue）、Hyper是否为“另一个框架”的问题以及Web标准的重要性。 文章最后提出了贡献和反馈的机会。

---

## 97. GIMP讨论更名

**原文标题**: Gimp to Discuss Changing Name

**原文链接**: [https://floss.social/@GIMP/114481178111577485](https://floss.social/@GIMP/114481178111577485)

文章讨论了 GIMP (GNU 图像处理程序) 可能更名的问题，原因是有人担心该缩写是一个“歧视残疾人的侮辱性词语”。 这篇帖子，很可能是在 Mastodon 社交媒体平台上发布的，强调了围绕该术语的争议及其负面含义，表明 GIMP 项目正在考虑重新命名，以避免引起冒犯。 该消息特别提到，要查看 FLOSS.social (一个专注于自由/开放源码软件的 Mastodon 实例) 上的完整讨论，用户需要启用 JavaScript。 这意味着可能更改名称的实际论点和理由在 FLOSS.social 对话中详细说明。 这个提示是对这场辩论的简短公告，促使人们进一步调查社区的感受和该项目的官方立场。

---

## 98. 线性规划：乐在其中，受益匪浅

**原文标题**: Linear Programming for Fun and Profit

**原文链接**: [https://modal.com/blog/resource-solver](https://modal.com/blog/resource-solver)

本文探讨了Modal如何利用线性规划 (LP) 来管理 GPU 资源分配并优化其无服务器平台的云实例成本。面对波动的 GPU 价格和不断变化的客户需求，Modal 开发了一种基于单纯形算法的“资源求解器”，以高效地分配资源并识别套利机会。

该求解器接收当前需求、实例价格、可用性和性能等方面的数据，并输出一个用于启动或关闭实例的计划，从而以最低的成本满足需求。该系统使 Modal 能够为其客户提供可预测的定价和即时可扩展性，使其免受云资源管理的复杂性困扰。

本文重点介绍了使用 LP 进行资源优化的优势，包括处理多个约束（CPU、RAM、GPU 类型、区域）和快速适应变化条件的能力。作者强调了求解器性能和可靠性的重要性，使用谷歌的 GLOP 求解器和启发式方法来防止长时间求解和无法解决的问题。他们还描述了求解器如何从失败的实例请求中学习，并将观察到的云提供商容量限制纳入后续的优化运行中。通过利用 LP，Modal 可以专注于面向用户的核心功能，同时信任求解器提供最佳的资源分配和成本节约。

---

## 99. Linux内核的PGP信任网络

**原文标题**: The Linux Kernel's PGP Web of Trust

**原文链接**: [https://blog.kleine-koenig.org/ukl/the-linux-kernels-pgp-web-of-trust.html](https://blog.kleine-koenig.org/ukl/the-linux-kernels-pgp-web-of-trust.html)

本文探讨了移除 SHA-1 签名对 Linux 内核 PGP 信任网络（用于验证代码贡献的真实性）的潜在影响。当前系统依赖于 Konstantin Ryabitsev 维护的受信任密钥的 Git 仓库，其中一个密钥必须具有从 Linus Torvalds 的密钥到该密钥的 5 个或更少的信任路径才能被包含。

尽管 GnuPG 拒绝 SHA-1 签名的举措通常对安全有利，但它也带来了重大挑战。虽然内核的专用工具目前接受 SHA-1 签名，但本文强调了 GnuPG 的“清理”过程（最近 Theodore Ts'o 的密钥更新就证明了这一点）如何可能无意中移除这些签名。

分析表明，korg-pgpkeys 仓库中绝大部分（7976 个中的 6045 个）签名都使用 SHA-1。移除这些签名将严重扰乱信任网络，导致 485 个密钥无法建立来自 Linus Torvalds 的有效信任路径，其中包括 Andrew Morton 和 Greg Kroah-Hartman 等知名内核开发人员的密钥。内核的“强集”将大幅缩减。

文章最后宣布将在 Embedded Recipes 2025 举办一次密钥签名会来解决这个问题，并鼓励大家参与，通过创建新的、基于 SHA-256 的签名来加强信任网络。与会者被敦促在截止日期前提交他们的公钥。

---

## 100. Fastgron: 快速让 JSON 可搜索

**原文标题**: Fastgron: Make JSON greppable, super fast

**原文链接**: [https://github.com/adamritter/fastgron](https://github.com/adamritter/fastgron)

Fastgron 是一个高性能的 C++20 实用工具，可将 JSON 转换为可 grep 的格式，性能显著优于原始的 `gron`（速度提升高达 50 倍）。 它将 JSON 转换为离散的赋值语句（例如，`json.name = "Tom"`），从而可以轻松地在大型 JSON 文件中查找特定的数据点及其路径。 Fastgron 还提供了一个 `--ungron` 选项，可以将过滤后的输出转换回有效的 JSON。

主要特性包括：

*   **速度：** 专为大型 JSON 文件设计，与 `gron` 相比，性能大幅提升。
*   **可 Grep 性：** 可以使用诸如 `fgrep` 之类的标准工具轻松搜索 JSON 数据。
*   **Ungron 转换：** 将 "gron" 输出转换回 JSON 格式。
*   **路径过滤：** 支持使用 `-p` 或 `.path` 进行路径过滤。 允许使用更复杂的路径表达式，包括重命名。
*   **可安装性：** 可通过各种软件包管理器（Arch、Homebrew、Nix）获得，并提供适用于 Ubuntu 和 Windows 的可下载二进制文件。
*   **流模式：** 可以使用 `-s` 或 `--stream` 选项处理 JSON 行。
*   **其他特性：** 包括排序、用户代理设置、自定义标头、着色、缩进控制以及添加分号的选项。

该文档还提供了基准测试，说明了 fastgron 在 JSON 处理任务中（尤其是在 JSON 文档中查找路径方面）相对于 gron、jq 和 jj 的速度优势。 其中包括 Ubuntu 的安装说明和通用构建信息，以及用于增强 fastgron 功能的未来开发思路，例如更复杂的路径查询和 CSV/TOML/YAML 支持。

---

