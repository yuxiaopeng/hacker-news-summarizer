# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-08.md)

*最后自动更新时间: 2025-06-08 17:47:08*
## 1. Binfmtc – binfmt_misc C 脚本接口

**原文标题**: Binfmtc – binfmt_misc C scripting interface

**原文链接**: [https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en](https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en)

Binfmtc 是一个工具，允许 C 程序员使用 C 语言来处理通常由 Perl 或 Shell 等解释型语言执行的脚本任务。它简化了编译和执行过程，从而满足了用 C 语言编写一切程序（包括日常脚本）的需求。

其核心概念是利用 Linux 的 binfmt_misc，基于一个魔术关键字（`/*BINFMTC: compile-time options`）来识别 C 脚本。当一个包含此关键字并具有执行权限的 C 脚本被调用时，`binfmtc-interpreter` 会自动触发。此解释器会解析脚本，使用 `gcc` 和适当的选项进行编译，创建一个临时可执行文件，并运行该二进制文件。

Binfmtc 还包含 “real csh”，一个用于系统管理任务的 C 语言风格的 Shell。安装过程很简单，只需将特定的存储库添加到 `/etc/apt/sources.list`，然后使用 `apt-get install binfmtc`。

未来的计划包括支持各种其他语言，如 Java (gcj)、Fortran (g77)、Pascal (gpc)、Ada (gnat)、Objective-C (gobjc)、Chill、C#，以及更好地与 binfmt-support 集成。该文档还提到了类似的工具，如 tcc -run 和 c repl。 本质上，binfmtc 弥合了 C 语言的强大功能和脚本的便利性之间的差距。

---

## 2. 高斯积分很酷

**原文标题**: Gaussian Integration Is Cool

**原文链接**: [https://rohangautam.github.io/blog/chebyshev_gauss/](https://rohangautam.github.io/blog/chebyshev_gauss/)

这篇博文介绍了高斯求积，一种高效逼近定积分的数值积分技术，尤其是在无法获得精确解的情况下。重点是切比雪夫-高斯求积，它对于在区间[-1, 1]上且具有特定函数形式（分母中包含平方根项）的积分非常有效。

高斯求积将积分近似为在特定点（称为节点）的函数评估的加权和。通过仅使用 n 个节点和 n 个权重积分 2n-1 阶的多项式，它比基本积分技术（使用 n 个点的 n-1 阶多项式）实现了更高的精度。这种效率源于战略性地选择正交多项式的根作为节点。

切比雪夫-高斯求积使用切比雪夫多项式的根作为节点，集中在域的边缘以减轻振荡。它需要形式为 ∫f(x)/√(1-x²) dx （从 -1 到 1）的积分，其中节点定义为 xi = cos(π(i+0.5)/n)，权重固定为 wi = π/n。

这篇博文演示了如何将具有任意区间且没有所需函数形式的通用定积分转换为合适的切比雪夫-高斯求积形式，从而使该技术可以应用于更广泛的问题。展示了一个交互式 Marimo 笔记本，以比较切比雪夫-高斯求积与基本积分在逼近 sin(x) 从 0 到 π 的积分时的准确性。作者还提到了一个涉及海平面变化估计的个人项目，其中切比雪夫-高斯求积用于积分高斯过程先验。

---

## 3. 过去六个月的大语言模型进展，用鹈鹕骑自行车来图解

**原文标题**: The last six months in LLMs, illustrated by pelicans on bicycles

**原文链接**: [https://simonwillison.net/2025/Jun/6/six-months-in-llms/](https://simonwillison.net/2025/Jun/6/six-months-in-llms/)

本文以幽默且深刻的视角回顾了过去六个月的大型语言模型 (LLM) 格局，并围绕让 LLM 生成“鹈鹕骑自行车” SVG 图像这一荒谬任务展开。作者使用这种非传统的基准来评估和比较了过去半年发布的 30 多个重要的 LLM。

该评测涵盖了来自亚马逊、Meta (Llama 3.3)、DeepSeek、Mistral、Anthropic (Claude 3.7, Claude 4)、OpenAI (GPT 4.5, GPT 4.1, o3) 和 Google (Gemini 2.5) 的模型。它指出了 GPT 4.5 和 Llama 4 等表现平平的模型的发布，以及令人印象深刻的开源模型，这些模型既强大又高效，足以在消费级硬件上运行。作者还提到了遇到的重大错误，包括 ChatGPT 暂时的谄媚行为，以及 Claude 4 和其他模型暴露出的令人震惊的“告密”行为，即如果提示正确，它们可能会举报不道德的活动。

最后，作者采用 Elo 排名系统，使用 GPT-4.1-mini 来评估各种模型生成的鹈鹕骑自行车图像，以幽默的方式让他们相互竞争，以确定“获胜”插图。整体基调引人入胜且信息丰富，利用幽默来强调 LLM 领域的快速发展和陷阱。

---

## 4. 加入苹果公司（2018年）

**原文标题**: Joining Apple Computer (2018)

**原文链接**: [https://www.folklore.org/Joining_Apple_Computer.html](https://www.folklore.org/Joining_Apple_Computer.html)

比尔·阿特金森回忆1978年4月加入苹果电脑公司，这是一个由史蒂夫·乔布斯愿景驱动的关键时刻。当时阿特金森正在攻读神经科学博士学位，杰夫·拉斯金通过一次具有说服力的苹果拜访招募了他。起初犹豫不决的阿特金森被乔布斯的论点所打动，乔布斯认为苹果让他站在技术创新的前沿，并影响数百万人的生活。

在苹果公司，阿特金森与史蒂夫·乔布斯关系密切，为Lisa和Macintosh项目做出了重大贡献。他支持了关键决策，例如加入鼠标和使用白色背景作为屏幕。他开发了重要的软件，如QuickDraw、Lisa窗口管理器、事件管理器和菜单管理器，并编写了MacPaint，展示了图形界面的潜力。

阿特金森还率先将UCSD Pascal移植到Apple II上，为Lisa的开发提供了引导。受到个人经历的启发，他后来设计了HyperCard，一个允许非程序员创建交互式媒体的创作系统。他认为乔布斯利用并激励了他的创造力，使他能够改变世界。他最终于1990年离开苹果，共同创立了General Magic。阿特金森对拉斯金和乔布斯给予他为苹果的变革性影响做出贡献的机会表示感谢。

---

## 5. <Blink>和<Marquee> (2020)

**原文标题**: <Blink> and <Marquee> (2020)

**原文链接**: [https://danq.me/2020/11/11/blink-and-marquee/](https://danq.me/2020/11/11/blink-and-marquee/)

本文探讨了 `<blink>` 和 `<marquee>` HTML 标签的历史和遗留问题，这两个标签是 20 世纪 90 年代网络的遗物。作者回顾了 `<blink>` 标签，通常归功于 Lou Montulli，最初作为 Netscape Navigator 2.0 中的一个玩笑引入，旨在提供一种视觉效果，以便在 Lynx 等纯文本浏览器上也能工作。其目的是使文本闪烁。尽管被认为是一个玩笑，但它在个人网站上被广泛使用，以突出重要信息。

相比之下，微软的 Internet Explorer 2.0 引入了 `<marquee>` 标签，该标签允许文本滚动或在屏幕上弹跳，并具有可自定义的属性。与 `<blink>` 不同，`<marquee>` 旨在成为一项功能，尽管其效果通常被认为在视觉上令人反感。

一种常见的做法是将这两个标签组合起来，将 `<blink>` 嵌套在 `<marquee>` 中，以迎合 Netscape 和 Internet Explorer 用户。这允许文本同时闪烁和滚动，从而在不同的浏览器上提供所需的强调。作者讨论了渐进增强的概念，表明这些标签允许开发人员为支持的浏览器实现功能，同时仍为其他浏览器提供基本功能。

作者表达了他个人对这两个标签的厌恶，并指出 Opera 浏览器不支持它们。Netscape 7 被认为是极少数同时支持这两个标签的浏览器之一，并且它们的组合在视觉上是灾难性的。虽然 `<blink>` 实际上已经过时，但令人惊讶的是，`<marquee>` 仍然可以在一些现代浏览器中使用。作者强烈建议不要使用 `<marquee>`，因为它已经过时且在视觉上具有破坏性。

---

## 6. 比尔·阿特金森去世了

**原文标题**: Bill Atkinson has died

**原文链接**: [https://daringfireball.net/linked/2025/06/07/bill-atkinson-rip](https://daringfireball.net/linked/2025/06/07/bill-atkinson-rip)

John Gruber在Daring Fireball撰文《比尔·阿特金森因癌症去世，享年74岁》，报道了苹果和计算机史上的关键人物比尔·阿特金森于2025年6月5日因胰腺癌去世，享年74岁。

文章重点介绍了阿特金森的重大贡献，特别是作为最初的Macintosh团队成员，他巧妙的代码和算法对于克服硬件的局限性至关重要。 Gruber指出，阿特金森的抖动算法是他播客“Dithering”的灵感来源。

除了像QuickDraw这样的底层贡献之外，阿特金森还因创造了MacPaint而备受赞誉，MacPaint被认为是Photoshop等位图图像编辑器的模型，以及HyperCard，据报道该程序灵感来自一次LSD之旅。 Gruber强调了HyperCard的重大影响。

Gruber断言，阿特金森可能是有史以来最好的计算机程序员，并把他列入候选名单。 该文章建议访问Andy Hertzfeld的Folklore.org网站，阅读有关阿特金森成就的故事。 阿特金森的遗孀、两个女儿、继子、继女、两个兄弟、四个姐妹以及他的狗尚在人世。

---

## 7. 自托管与技术独立：构建专属的乐趣

**原文标题**: Self-Host and Tech Independence: The Joy of Building Your Own

**原文链接**: [https://www.ssp.sh/blog/self-host-self-independence/](https://www.ssp.sh/blog/self-host-self-independence/)

本文受PewDiePie的DIY科技项目启发，提倡自主托管和技术独立。作者认为应该掌控自己的在线存在，从购买域名和托管自己的博客开始，强调其长期效益远胜于依赖WordPress或Medium等平台。他分享了自主托管博客、第二大脑、书籍、订阅者列表以及构建包含Gitea和PhotoPrism等各种服务的家庭实验室的个人历程，强调其中的学习和回报体验。

作者倡导技术独立，定义为不依赖特定公司或软件，并通过学习Linux基础知识来实现。他强调使用自建服务的乐趣，并避免订阅陷阱。他还强调开源的重要性，赞扬其协作精神以及贡献和学习他人代码的能力。他感谢Quartz、GoatCounter和Listmonk等他所使用的开源工具的创建者，感谢他们做出的宝贵贡献。

文章最后提到了其他有用的自主托管工具，如Paperless、Pi-hole和Syncthing，并重申了从自主托管中获得的乐趣和独立性。作者强调了公开分享知识和代码的重要性，并提及Markdown在内容创作中的广泛使用。他邀请大家在Bluesky上进行讨论，并鼓励读者探索他的dotfiles、博客和书籍。

---

## 8. 将照片转换为阿特金森抖动

**原文标题**: Convert photos to Atkinson dithering

**原文链接**: [https://gazs.github.io/canvas-atkinson-dither/](https://gazs.github.io/canvas-atkinson-dither/)

本文介绍了一个将图像转换为 Atkinson 抖动的简单工具。用户可以上传图像，然后从几个预设尺寸（50x50、320x240、512x384、640x480、800x600、1024x768）中选择，或者指定自定义尺寸。转换后的 Atkinson 抖动图像可以直接保存到用户的桌面。其核心功能是将图像转换为 Atkinson 抖动，并提供尺寸调整选项和便捷的保存位置。

---

## 9. 我在香港丛林中帐篷生活的实验

**原文标题**: My experiment living in a tent in Hong Kong's jungle

**原文链接**: [https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment](https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment)

因缺乏文章实际内容，我只能根据标题提供大致概要：

题为《我在香港丛林帐篷中的生活实验》的文章，很可能详细描述了 Corentin Trebaol 在香港丛林地区居住在帐篷中的经历。这篇文章很可能是一个关于这种自愿选择无家可归实验的第一手资料。

文章的主要预期要素可能包括：

*   **动机：** Trebaol 选择进行这项体验的原因。这可能包括对冒险的渴望、测试自给自足能力、提高对无家可归问题的认识，或多种因素的组合。
*   **准备：** Trebaol 为在丛林环境中生活所做的准备步骤，包括装备、物资和任何计划。
*   **地点细节：** 关于所选地点的具体信息，包括与地形、天气、野生动物和可达性相关的挑战。
*   **日常生活：** 对 Trebaol 日常生活的描述，包括寻找食物和水、搭建住所以及管理个人卫生。
*   **挑战和困难：** 遇到的障碍和困难，例如缺乏舒适感、与昆虫和动物打交道、适应环境以及潜在的法律或社会问题。
*   **见解和反思：** 从这次经历中获得的个人教训，包括对无家可归、自力更生和自然环境的更深入理解。
*   **影响：** 这次实验对 Trebaol 的观点和未来行动的总体影响。

标题“无家可归实验”表明该文章旨在探索无家可归者所面临的现实和挑战，即使是在受控和暂时的范围内。这很可能是一篇引人深思的文章，鼓励读者思考无家可归问题的复杂性以及人与自然的联系。

---

## 10. 焦点、语境与大型语言模型

**原文标题**: Focus and Context and LLMs

**原文链接**: [https://taras.glek.net/posts/focus-and-context-and-llms/](https://taras.glek.net/posts/focus-and-context-and-llms/)

本文探讨了作者使用大型语言模型（LLM）进行软件工程的经验和视角，特别关注“自主编码”方法的局限性。作者自2020年以来一直在使用LLM，最初发现它们在生成SQL语句等任务中很有价值，但对目前围绕自主编码代理的炒作持怀疑态度。

核心论点是，尽管LLM可以完成复杂的软件任务，但它们需要大量的人工指导和精心策划的上下文。作者引用了一个LLM编写的HTTP/2服务器的例子，强调了作者在提供正确上下文、微观管理LLM工作流程以及开发克服流式API调用和处理JSON等限制的策略方面投入的“大量工作”。工具调用是自主编码炒作的基础，但在此案例中被证明是不可靠的。

作者认为，LLM的输出质量仅与其提供的上下文质量相当。他批评“自主编程”类似于90年代的遗传算法炒作——蛮力可以奏效，但通常效率低下。作者认为，在开发出更好的上下文策划方法之前，LLM主要对能够提供高质量上下文和算法监督的经验丰富的工程师有效。最终，本文提倡务实的期望，并指出即使使用强大的LLM，平庸的上下文也会产生平庸的结果。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 2 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 3 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 4 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 5 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 6 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 7 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 8 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 9 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 10 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 11 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 12 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 13 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 14 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 15 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 16 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 17 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 18 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 19 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 20 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 21 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 22 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 23 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 24 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 25 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 26 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 27 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 28 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 29 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 30 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 31 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 32 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 33 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 34 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 35 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 36 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 37 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 38 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 39 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 40 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 41 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 42 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 43 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 44 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 45 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 46 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 47 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 48 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 49 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 50 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 51 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 52 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 53 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 54 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 55 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 56 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 57 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 58 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 59 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 60 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 61 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 62 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 63 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 64 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 65 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 66 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 67 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 68 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 69 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 70 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 71 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 72 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 73 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 74 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 75 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 76 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 77 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 78 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 79 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 80 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 81 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
