# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-25.md)

*最后自动更新时间: 2025-04-25 17:48:23*
## 1. 写入“/etc/hosts”文件会破坏 Substack 编辑器。

**原文标题**: Writing "/etc/hosts" breaks the Substack editor

**原文链接**: [https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack](https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack)

文章《修改'/etc/hosts'导致Substack编辑器崩溃》详细描述了直接修改`/etc/hosts`文件可能如何意外地破坏Substack编辑器的功能。作者回忆了一段个人经历，为了测试目的，他们修改了`/etc/hosts`文件以重定向一个特定域名，却无意中导致了Substack编辑器崩溃。

关键在于，Substack依赖于某些域名和服务，通过`/etc/hosts`文件干扰它们的解析可能会导致编辑器中出现意外问题，例如无法保存草稿、图片上传问题以及编辑器总体无响应。文章强调，这是因为Substack的编辑器会对其自身的基础设施进行API调用。当域名解析被篡改时，这些调用会失败。

作者的解决方案是恢复对`/etc/hosts`文件所做的更改，从而有效地恢复Substack服务的正确域名解析。这篇文章是对经常修改`/etc/hosts`文件的开发者和高级用户的一个警示，强调了考虑对依赖特定域名解析的Web应用程序的潜在影响的重要性。它强调了现代Web应用程序的隐藏依赖性，以及看似无害的系统级修改可能造成的重大后果。

---

## 2. Eurorack旋钮创意

**原文标题**: Eurorack Knob Idea

**原文链接**: [https://mitxela.com/projects/euroknob](https://mitxela.com/projects/euroknob)

Mitxela详述了他的“Eurorack旋钮创意”，这是一种旨在减少面板杂乱的新型Eurorack模块设计方法。该概念用混合旋钮和跳线系统取代了传统的电位器。该系统使用3.5mm TRS插孔代替电位器，并配有位于插孔下方的磁编码器芯片(AS5600)。一个小的钕磁铁嵌入在TRS插头中，充当旋钮。插入时，磁铁与AS5600相互作用，将旋钮的旋转转化为角度读数，可用于控制模块参数。

作者描述了磁性旋钮的构造、结合了AS5600和用于读取和显示编码器数据的微控制器（CH32V003）的电路板设计以及组装过程。该原型成功地通过场强读数检测到磁性旋钮的存在，将其与标准跳线区分开来。

尽管原型成功，但作者承认在整个Eurorack系统中实施该想法可能不切实际且成本高昂。他设想了一个专门致力于此概念的小众社区，“Euroknobists”。虽然没有申请专利，但他提出了一个更具商业可行性的替代方案：带有同轴TRS插孔的电位器。他最后邀请企业家资助和开发这个想法，并承认他在该领域的局限性。

---

## 3. Show HN: Magnitude – 面向 Web 应用的开源、AI 原生测试框架

**原文标题**: Show HN: Magnitude – open-source, AI-native test framework for web apps

**原文链接**: [https://github.com/magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)

Magnitude：一个AI原生、开源的Web应用测试框架。它允许用户使用自然语言构建和运行端到端测试，利用视觉AI代理理解并适应UI变化。

其工作原理是：用户用简单的步骤、数据输入和自然语言检查编写测试用例。Magnitude使用强大的通用多模态LLM（如Gemini）作为“规划者”来规划测试策略，并使用快速视觉LLM（Moondream）作为“执行者”以像素级精度与UI交互。如果在执行过程中出现问题，推理代理会介入。

要开始使用，用户需要安装`magnitude-test`包，在其项目中初始化Magnitude，并配置规划者和执行者LLM的API密钥。然后通过`npx magnitude`命令运行测试。Magnitude支持并行测试执行。

该框架专注于简化测试用例的创建，使用户能够像向同事描述一样描述测试。测试可以集成到CI/CD管道中。

Magnitude通过使用专门的模型进行规划和执行，区别于 OpenAI Operator/Claude Computer Use 等解决方案。 这种方法旨在提高专门针对测试场景的速度、可靠性和成本效益。

---

## 4. 肿瘤来源的促红细胞生成素作为癌症免疫中的免疫抑制开关

**原文标题**: Tumor-derived erythropoietin acts as immunosuppressive switch in cancer immunity

**原文链接**: [https://www.science.org/doi/10.1126/science.adr3026](https://www.science.org/doi/10.1126/science.adr3026)

无法访问文章链接。

---

## 5. 大型可重复性项目未能验证生物医学研究。

**原文标题**: Huge reproducibility project fails to validate biomedical studies

**原文链接**: [https://www.nature.com/articles/d41586-025-01266-x](https://www.nature.com/articles/d41586-025-01266-x)

巴西可重复性倡议是一项大型可重复性项目，旨在评估巴西生物医学研究的可重复性，重点关注采用三种常用方法的研究：细胞代谢测定、遗传物质扩增技术和啮齿动物迷宫测试。来自 56 个实验室的 200 多名科学家试图重复 1998 年至 2017 年间发表的 47 篇论文中的实验。

结果令人沮丧，只有不到一半的测试实验可重复。使用五个标准，只有 21% 的实验在至少一半的标准上是可重复的。原始论文中的效应量平均也比重复尝试中的大 60%，表明原始研究倾向于高估干预措施的效果。

该研究强调了加强巴西科学实践的必要性，并为在公共政策和大学内部实施变革提供了基础。这项雄心勃勃的项目在 COVID-19 大流行期间面临物流挑战，并且参与团队在遵守协议方面存在差异。

---

## 6. 致相信人的爱之书

**原文标题**: A Love Letter to People Who Believe in People

**原文链接**: [https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html](https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html)

蒂娜的《致相信他人之人的情书》颂扬了热情带来的变革力量以及成为他人“粉丝”的重要性。她强调，相信某人并为他们的生活带来热情具有感染力且能改变人生。蒂娜用个人轶事来说明这一点，着重介绍了对她的旅程产生重大影响的个人。

她将自己大胆生活的灵感归功于古怪的Hugi阿姨，将职场中展现的善良归功于她的第一任老板Matthew Waldman，将激励她创办自己的设计工作室归功于她的女儿Ella，并将向她展示如何将她的想法变为现实归功于Jim Coudal。她还强调了Ben Chestnut (Mailchimp) 和Ruth Ann Harnisch (Harnisch Foundation) 对 CreativeMornings 的影响，强调了支持性伙伴关系和彻底慷慨的力量。

蒂娜强调了创建以心为本、培养慷慨、善良和好奇心的社区的重要性。她认为，相互支持和彼此信任可以赋予个人力量，让他们发挥潜力并为更美好的未来而努力。最终，她鼓励读者拥抱“粉丝心态”，通过大胆、勇敢和热情来激励他人。这篇文章也是一封献给CreativeMornings社区的情书，分享了他们在创建有意义的人际关系空间方面的经验。

---

## 7. 作为思维工具的符号 (1979)

**原文标题**: Notation as a Tool of Thought (1979)

**原文链接**: [https://www.jsoftware.com/papers/tot.htm](https://www.jsoftware.com/papers/tot.htm)

作为思维工具的记号 (1979) 认为，记号不仅仅是被动的记录系统，而是一种积极且强大的工具，能够塑造和影响我们的思维。该文章强调了记号的选择如何显著影响我们理解、操作和发现新想法的能力。

它强调，好的记号可以通过揭示潜在的结构和关系使复杂问题看起来更简单，而差的记号甚至会模糊最基本的概念。作者很可能讨论了数学、逻辑或计算机科学的例子来阐明这一点，展示了特定记号如何促进特定类型的推理和问题解决。

此外，该文章可能探讨了记号的演变以及它们的发展对于科学和数学进步的重要性。它表明，新记号的发明通常先于理解上的突破，使我们能够以新的方式“看到”问题并开发更有效的解决方案。 本质上，这篇文章提倡认真考虑记号的影响，敦促我们选择甚至发明最能支持我们认知过程并促进智力探索的记号。 中心思想是，记号不仅仅是一种记录思想的方式，更是一种塑造和推进思想的强大工具。

---

## 8. 利用C/C++程序中的未定义行为：性能影响 [pdf]

**原文标题**: Exploiting Undefined Behavior in C/C++ Programs: The Performance Impact [pdf]

**原文链接**: [https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf](https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf)

利用 C/C++ 程序中未定义行为：性能影响

---

## 9. 策略傀儡提示：绕过主流大型语言模型的新方法

**原文标题**: The Policy Puppetry Prompt: Novel bypass for major LLMs

**原文链接**: [https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/)

HiddenLayer是一家Gartner认可的AI安全提供商，提供独特的平台来保护企业机器学习模型免受各种威胁。他们专注于保护AI模型，无需增加复杂性或访问敏感数据和算法。他们的平台提供开箱即用的安全性，解决推理、绕过、提取攻击和模型窃取问题。

该公司以其安全至上的方法和避免数据访问要求而著称。HiddenLayer获得了包括微软、Moore Strategic Ventures、Booz Allen Ventures、IBM Ventures和Capital One Ventures在内的重要投资者的支持。

本文提供了HiddenLayer网站各个部分的链接，包括预约演示、平台详情、解决方案、服务、学习资源、合作信息、公司信息、职业、以及联系方式。文章还提到了他们的安全隐私政策、漏洞披露政策、网站地图以及Twitter和LinkedIn的个人资料链接。

本质上，HiddenLayer旨在为AI模型提供强大的安全解决方案，专注于易于实施，并避免不必要的数据或算法访问，这使其成为利用机器学习的企业的宝贵资产。

---

## 10. UIT – 云端大规模、高性能、模块化、低内存文件处理

**原文标题**: UIT – performant, modular, low-memory file processing at scale, in the Cloud

**原文链接**: [https://github.com/janwilmake/uit](https://github.com/janwilmake/uit)

UIT (通用信息终端) 是一个为云端大规模文件处理而设计的库，它具有高性能、模块化和低内存占用等特点。它提供了一个四步流程：摄取、过滤/转换、合并和输出，使用户能够从各种来源收集文件层级结构，应用转换，并以所需的格式输出它们。

UIT通过流式处理和并行化来强调性能，使其能够在Cloudflare Workers等低内存环境中高效运行。它的模块化设计确保了可组合性和对构建块的清晰概览，每个模块都可以潜在地在不同的位置运行。

该库利用FormData处理多个文件和二进制数据，并使用Streams API处理中间结果。它提供了几个模块：`uithub.ingestzip`（ZIP摄取）、`uithub.merge`（FormData合并）、`uithub.outputmd`（Markdown输出）、`uithub.outputzip`（ZIP打包）、`uithub.search`（搜索功能）、`uithub.ziptree`（ZIP层级结构提取）、`uithub.otp`（密钥管理）和`uithub`（UI模块）。

UIT协议定义了UIT模块的约定，将其分为摄取、合并、过滤/转换和输出模块。它指定了用于处理文件的必需的和自定义的FormData标头，包括`Content-Disposition`、`Content-Type`、`x-url`和`x-file-hash`。

UIT鼓励贡献，并旨在创建一个插件系统，以简化文件过滤和转换。该项目是开源的，欢迎开发人员添加模块。它目前处于预发布阶段，并正在寻找赞助商。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 2 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 3 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 4 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 5 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 6 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 7 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 8 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 9 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 10 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 11 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 12 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 13 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 14 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 15 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 16 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 17 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 18 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 19 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 20 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 21 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 22 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 23 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 24 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 25 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 26 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 27 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 28 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 29 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 30 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 31 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 32 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 33 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 34 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 35 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 36 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 37 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
