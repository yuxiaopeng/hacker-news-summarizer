# Hacker News 热门文章摘要 (2025-06-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Magistral — Mistral AI 首个推理模型

**原文标题**: Magistral — the first reasoning model by Mistral AI

**原文链接**: [https://mistral.ai/news/magistral](https://mistral.ai/news/magistral)

Mistral AI发布Magistral，其首个推理模型，专为领域特定、透明和多语言推理而设计。它有两个版本：Magistral Small（240亿参数，开源）和Magistral Medium（更强大，企业版）。Magistral Medium在AIME2024上取得了73.6%的成绩（多数投票@64时为90%），而Magistral Small的得分为70.7%（多数投票@64时为83.3%）。

主要特性包括跨多种语言的自然推理、适用于各种企业应用，以及Le Chat中用于10倍速响应的“思考模式”。Magistral针对多步骤逻辑进行了微调，增强了解释性，并在用户的语言中提供可追溯的推理。它擅长英语、法语、西班牙语和中文等语言。

Magistral用途广泛，非常适合需要大量思考处理和精度的任务，例如法律研究、财务预测、软件开发和创意故事讲述。它专为战略规划、风险评估以及法律、金融和医疗保健等受监管行业中以数据驱动的决策而设计。它还可以改善编码和内容创作。

Magistral Small可在Hugging Face上以Apache 2.0许可证下载，而Magistral Medium的预览版可在Le Chat上以及通过La Plateforme上的API获得。它很快将在Amazon SageMaker、IBM WatsonX、Azure AI和Google Cloud Marketplace上提供。Mistral AI也在招聘，寻求为未来AI创新做出贡献的人才。

---

## 2. 被美国列入黑名单的魔术师成为了巴西的英雄

**原文标题**: A Blacklisted American Magician Became a Hero in Brazil

**原文链接**: [https://www.wsj.com/lifestyle/careers/magician-brazil-national-celebrity-d31f547a](https://www.wsj.com/lifestyle/careers/magician-brazil-national-celebrity-d31f547a)

无法访问文章链接。

---

## 3. 伪造OpenPGP.js签名验证

**原文标题**: Spoofing OpenPGP.js signature verification

**原文链接**: [https://codeanlabs.com/blog/research/cve-2025-47934-spoofing-openpgp-js-signatures/](https://codeanlabs.com/blog/research/cve-2025-47934-spoofing-openpgp-js-signatures/)

Codean Labs 的这篇文章详细介绍了 CVE-2025-47934，OpenPGP.js 中的一个严重漏洞，该漏洞允许攻击者伪造签名。通过将一个格式错误的包（特别是包含恶意数据的压缩数据包）附加到有效的签名消息，攻击者可以诱使 OpenPGP.js 针对原始的有效数据验证签名，同时返回攻击者控制的恶意数据作为签名内容。

该漏洞存在于 OpenPGP.js 解析消息的方式中。它最初只读取部分数据包列表，然后使用 `unwrapCompressed()` 来潜在地从压缩包中提取数据。关键在于，在最初调用 `unwrapCompressed()` 之后，数据包流可能已被完全读取，从而导致验证了真实的签名，但最终输出的 `data` 却是从稍后添加的恶意数据包中检索的。

此缺陷会影响标准签名消息和加密消息，允许攻击者注入任意内容，同时保持有效的签名，可能导致严重的安全漏洞。文章提供了一个概念验证，演示了如何使用 Python 脚本生成伪造的消息。

该漏洞已在 OpenPGP.js v5.11.3 和 v6.1.1 版本中修复。建议用户更新其库和任何依赖软件（如 Mailvelope）以降低风险。修复方案包括实施严格的语法验证，以拒绝格式错误的数据包列表。

---

## 4. 标枪卫士：低成本LLM安全Transformer架构

**原文标题**: JavelinGuard: Low-Cost Transformer Architectures for LLM Security

**原文链接**: [https://arxiv.org/abs/2506.07330](https://arxiv.org/abs/2506.07330)

本文介绍了JavelinGuard，一套低成本、高性能的Transformer架构，旨在检测LLM交互中的恶意意图，重点关注生产部署效率。作者Yash Datta和Sharath Rajasekar探索了五种架构：Sharanga（基线）、Mahendra（增强的注意力加权池化）、Vaishnava和Ashwina（混合神经集成）、以及Raudra（多任务框架）。这些架构利用紧凑型BERT变体的最新进展，以约4亿参数和标准CPU上的快速推理速度实现高精度。

这些模型针对九个不同的对抗性数据集进行了严格的基准测试，包括流行的集合和一个新的数据集JavelinBench，旨在测试泛化能力。JavelinGuard架构的性能与领先的开源护栏模型以及大型仅解码器LLM（如gpt-4o）进行了比较。

研究结果表明，虽然Raudra凭借其多任务设计提供了最强大的整体性能，但每种架构在速度、可解释性和资源需求方面都提供了不同的权衡。这使得从业者能够根据其特定的LLM安全需求选择最佳平衡。本文认为，在准确性和延迟方面，与现有的护栏解决方案和大型LLM相比，JavelinGuard提供了卓越的性价比。该研究为在实际应用中构建高效、有效的LLM安全措施提供了有价值的见解。

---

## 5. 更快速、更简易的2D矢量渲染[视频]

**原文标题**: Faster, easier 2D vector rendering [video]

**原文链接**: [https://www.youtube.com/watch?v=_sv8K190Zps](https://www.youtube.com/watch?v=_sv8K190Zps)

名为“更快、更简单的 2D 矢量渲染 [视频]”的文章似乎是 YouTube 上托管的视频。然而，提供的“内容”部分并未描述视频本身，而是列出了标准的 YouTube 页脚信息，包括指向法律和信息页面的链接，例如：

*   版权信息
*   联系信息
*   创作者资源
*   广告信息
*   开发者资源
*   服务条款
*   隐私政策
*   安全信息
*   YouTube 运作方式
*   测试新功能
*   NFL Sunday Ticket 信息

因此，仅根据所提供的信息，无法总结关于更快、更简单的 2D 矢量渲染的视频的实际内容。我们只能推断该视频存在于 YouTube 上，并且可能与图形编程、设计或动画相关。所列内容仅仅是与视频主题无关的样板式 YouTube 信息。

---

## 6. Denuvo分析

**原文标题**: Denuvo Analysis

**原文链接**: [https://connorjaydunn.github.io/blog/posts/denuvo-analysis/](https://connorjaydunn.github.io/blog/posts/denuvo-analysis/)

本文深入分析了Denuvo，这是一种用于保护视频游戏的重要反篡改和数字版权管理(DRM)系统。文章解释了Denuvo背后的总体思路，即采用半在线DRM方法。该过程包括收集硬件信息，将其发送到Denuvo服务器，接收许可证文件，然后执行运行时检查以确保游戏的完整性。

文章深入探讨了技术层面，描述了Denuvo如何通过在虚拟机中执行函数并删除部分指令来保护函数，并将这些删除的“被盗常量”存储在与硬件标识混合的许可证文件中。在运行时解密这些常量对于游戏的正常运行至关重要。

Denuvo功能的核心在于其用户完整性检查，包括验证硬件和软件组件。这些检查在OEP（原始入口点）之前和运行时执行，包括检查KUSER_SHARED_DATA、CPUID、SYSCALL、NTDLL、PEB、XGETBV以及GetWindowsDirectoryW、GetVolumeInformationW、GetComputerNameW和GetUsernameW等函数。还会执行CRC等代码完整性检查以防止篡改。

文章还强调了Denuvo对虚拟机的使用、用于非连续存储值的位向量实现、基于本机寄存器的随机性以及混合布尔算术(MBA)混淆，以使逆向工程复杂化。该分析旨在提供对Denuvo保护机制的教育性见解，同时隐去敏感信息。

---

## 7. 《无尽的玩笑》中的可疑数学 (2009)

**原文标题**: Dubious Math in Infinite Jest (2009)

**原文链接**: [https://www.thehowlingfantods.com/dfw/dubious-math-in-infinite-jest.html](https://www.thehowlingfantods.com/dfw/dubious-math-in-infinite-jest.html)

迈克·斯特朗的文章《〈无尽的玩笑〉中的可疑数学》探讨了戴维·福斯特·华莱士的小说中发现的数学错误。斯特朗自称是华莱士的粉丝，他对华莱士表现出的数学能力与这些错误的存在感到好奇。他记录了在第二次阅读这本书时发现的四个具体错误，其中两个可能是印刷错误。

最显著的错误涉及叙述者计算一场108局网球比赛以54-54平局结束的几率。叙述者声称几率是1/2^27，但斯特朗认为，使用组合数学计算得出的正确概率约为0.0766，明显更高。

第二个错误出现在一个脚注中，迈克·佩姆利斯在脚注中描述了如何在末世论计算中使用积分中值定理。斯特朗指出，虽然佩姆利斯对该定理的描述是正确的，但该定理本身是证明存在性的理论工具，并没有提供找到佩姆利斯应用所需特定值的方法。与此相关的一个小错误发生在积分中值定理的公式中，缺少了积分符号。

最后一个错误也归因于佩姆利斯，涉及x^n的导数。佩姆利斯错误地将导数表示为nx + x^(n-1)，而正确的表达式是nx^(n-1)。

斯特朗没有对这些错误的出现提供具体的解释，而是将它们作为记录在案的观察结果呈现出来，并邀请进一步的讨论。

---

## 8. Show HN: PyDoll – 具有原生验证码绕过的异步Python爬虫引擎

**原文标题**: Show HN: PyDoll – Async Python scraping engine with native CAPTCHA bypass

**原文链接**: [https://github.com/autoscrape-labs/pydoll](https://github.com/autoscrape-labs/pydoll)

PyDoll：一款新型异步Python爬虫引擎，旨在简化浏览器自动化操作，尤其适用于处理受反爬虫系统保护的网站。其关键特性是原生验证码绕过，无需外部服务或API密钥即可处理Cloudflare Turnstile和reCAPTCHA v3，通过模拟类人交互来避免检测。

传统的浏览器自动化通常依赖webdriver，导致兼容性问题，并且容易被网站识别和屏蔽。PyDoll直接连接到Chrome DevTools Protocol (CDP)，无需驱动程序，从而解决了这个问题。

该引擎强调简单性，易于安装 (`pip install pydoll-python`)，直观的元素查找以及事件驱动架构。它支持异步操作，实现快速性能和多个站点的并发处理。网络监控允许修改和分析流量，从而进一步绕过保护机制。

文档重点介绍了智能验证码绕过、类人交互和强大的网络监控等功能。提供了基本用法、自定义配置、高级验证码处理、元素查找、并发自动化、事件驱动任务和iframe交互的示例。

该项目是开源的（MIT许可证），鼓励贡献，并提供了指南。也鼓励通过GitHub赞助、为仓库加星、在社交媒体上分享以及提供反馈来支持该项目。

---

## 9. Show HN: 高端色彩量化器

**原文标题**: Show HN: High End Color Quantizer

**原文链接**: [https://github.com/big-nacho/patolette](https://github.com/big-nacho/patolette)

Patolette 是一个新的 C/Python 库，用于高端颜色量化和抖动，它实现了一种受吴晓林工作启发的基于加权 PCA 的量化器。它具有避免轴对齐细分等优势，并支持 CIEL*u*v* 和 ICtCp 等颜色空间。值得注意的是，它可以利用显著性图来强调量化过程中视觉上突出的区域，并具有可选的 KMeans 细化功能，以改进调色板的生成。

虽然仍在开发中且尚未准备好用于生产环境，但 patolette 是可用的，需要手动安装（提供了针对 Linux、macOS 和 Windows 的说明，包括依赖项管理）。一个关键特性是能够利用 AVX CPU 扩展来显著提升 KMeans 的性能。

该文档解释了基本用法，包括使用 Pillow 读取图像，使用 quantize 函数进行量化（带有抖动、颜色空间选择和瓦片大小等选项），以及保存结果图像。"tile\_size" 参数可以通过引入显著性图来根据视觉突出程度对样本进行加权，从而减轻大簇主导小簇的问题。

该库目前存在高内存占用、速度慢以及缺少完整的 C API 和 RGBA 支持等问题。作者承认了 patolette 所依赖的工作，包括吴晓林的颜色量化算法、显著物体检测方法以及 faiss、flann 和 OpenBLAS 等库。

---

## 10. 可塑软件：在应用锁定的世界中恢复用户自主性

**原文标题**: Malleable software: Restoring user agency in a world of locked-down apps

**原文链接**: [https://www.inkandswitch.com/essay/malleable-software/](https://www.inkandswitch.com/essay/malleable-software/)

本文倡导“可塑软件”的概念，即一种计算生态系统，用户能够以最小的阻力根据自身需求调整工具，这与当今流行的僵化、大规模生产的软件形成对比。作者认为，当前的软件常常阻碍生产力并导致用户沮丧，因为它缺乏可定制性，并且受到中心化的开发团队控制，无法满足个体需求。他们举例说明，医疗专业人员难以应对不灵活的电子病历，以及软件团队在切换到僵化的基于Web的问题跟踪器后失去了流程流畅性。

本文探讨了现有定制方法的局限性，如设置（过于有限）、插件（API受限且难以创建）、modding（繁琐且不稳定）和开源（需要大量的专业知识）。虽然承认人工智能辅助编码的潜力，但作者强调，它并不能解决所有可塑性障碍，特别是如何调整现有工具、确保互操作性以及在不进行全面编码的情况下提供精确控制。

他们设想了一个赋予用户共同创造者地位的生态系统，用户可以调整现有软件、进行修改，甚至构建新工具。目标是使定制变得快速而简单，使用户能够在需求出现时立即调整其工具。本文展望了一个未来，即从用户到创造者的转变是一个平滑、自然的过程。

---

## 11. 容器化：在 macOS 上运行 Linux 容器的 Swift 包

**原文标题**: Containerization is a Swift package for running Linux containers on macOS

**原文链接**: [https://github.com/apple/containerization](https://github.com/apple/containerization)

容器化是一个Swift软件包，使应用程序能够利用Apple的Virtualization.framework在macOS上运行Linux容器。它提供了管理OCI镜像、与注册中心交互、创建ext4文件系统、使用Netlink套接字、制作优化的Linux内核以实现快速启动、管理轻量级虚拟机、启动容器化进程以及利用Rosetta 2在Apple芯片上执行x86_64代码的API。

该设计为每个容器采用轻量级虚拟机，分配专用IP地址以消除端口转发。通过优化的内核和使用vminitd的最小根文件系统（一种通过GRPC API促进运行时配置和进程启动的小型init系统）实现亚秒级的启动时间。

要求包括Apple芯片Mac和macOS 15或更高版本（或macOS 26 Beta 1+用于构建），macOS 15上某些网络功能不可用。示例位于`cctl`可执行文件中，展示了镜像操作、注册中心登录和运行容器等核心功能。

用户可以使用提供的配置编译自定义的优化内核，或者使用Kata Containers项目中的预构建内核。提供了准备构建环境、构建和测试软件包的说明，以及生成和查看API文档的指导。

欢迎贡献，该项目目前版本为0.1.0，源稳定性仅在次要版本内保证。

---

## 12. 使用人工智能教授国家安全政策

**原文标题**: Teaching National Security Policy with AI

**原文链接**: [https://steveblank.com/2025/06/10/teaching-national-security-policy-with-ai/](https://steveblank.com/2025/06/10/teaching-national-security-policy-with-ai/)

史蒂夫·布兰克的文章讨论了将人工智能工具整合到斯坦福大学“技术、创新与大国竞争”国家安全政策课程中的情况。目标是为学生迎接人工智能驱动的国际政策未来做好准备。

学生们以团队形式使用人工智能执行各种任务，包括总结政策文件、识别关键主题、创建利益相关者访谈名单、转录播客以及批判自己的假设。他们利用了诸如ChatGPT、Claude、Perplexity、NotebookLM、Otter.ai、Mermaid和Beautiful.ai等工具，这些工具可通过斯坦福大学的AI Playground获得。

文章重点介绍了几个团队的经验，展示了创新的人工智能应用。例如，一个团队使用人工智能模拟与利益相关者的访谈，而另一个团队则使用人工智能生成图形和PowerPoint演示文稿。团队还使用人工智能来识别要采访的专家并批判学生的假设。

主要收获包括人工智能加速学习，充当有用的合作者（尤其是在与利益相关者访谈相结合时），并促进创造性的问题解决。学生们迅速掌握了人工智能工具，并且常常发现意想不到的应用。指导教师强调了交叉检查人工智能输出的准确性和相关性的重要性，并指出人工智能与人类的努力和洞察力相结合时效果最佳。作者教授的所有斯坦福课程现在都将人工智能作为课程的一部分。

---

## 13. 强化预训练

**原文标题**: Reinforcement Pre-Training

**原文链接**: [https://arxiv.org/abs/2506.08007](https://arxiv.org/abs/2506.08007)

这篇arXiv文章 (arXiv:2506.08007) 介绍了一种名为强化预训练 (RPT) 的新方法，用于扩展大型语言模型 (LLM) 和强化学习 (RL)。这篇由董清秀及其同事撰写的论文，将传统的下一个token预测任务重新定义为一种用RL训练的推理任务。在RPT中，模型因准确预测给定上下文中的后续token而获得奖励。

RPT的关键优势在于其能够利用大量现成的文本数据进行通用RL，而无需专门的标注数据集。通过激励下一个token推理，RPT显著提高了语言建模的准确性。该方法还为后续的强化微调提供了强大的预训练基础，可能带来更有效的RL代理。

作者强调，使用RPT增加训练计算量可以持续提高下一个token预测的准确性，表明其具有可扩展性。结果表明，RPT是一种有前景的范例，可以推进语言模型预训练并弥合LLM和RL之间的差距。该论文还提供了PDF、HTML和TeX源代码的链接，以及用于探索引用、相关论文和相关代码的各种工具。

---

## 14. 分子动力学入门

**原文标题**: A Primer on Molecular Dynamics

**原文链接**: [https://www.owlposting.com/p/a-primer-on-molecular-dynamics](https://www.owlposting.com/p/a-primer-on-molecular-dynamics)

分子动力学入门：模拟原子分子运动的计算方法

本文介绍分子动力学（MD）的基本原理，这是一种通过计算机模拟原子和分子随时间运动的技术。MD使科学家能够观察动态分子行为、预测分子相互作用，并理解蛋白质折叠和药物结合等复杂过程。

本文解释了MD模拟的工作原理，即首先定义一个系统，通常是在充满水、离子和盐的立方体中的蛋白质。然后，应用一个力场，该力场近似于支配原子间相互作用的物理定律。力场是势能的数学表示，根据键长、角度和静电相互作用等因素计算得出。随后，模拟利用该势能的负梯度来确定原子应如何移动以最小化系统的总能量。

作者分解了MD中常用的势能方程，解释了与键能、角能、二面角能量以及范德华力和静电相互作用相关的项。尽管力场不能完全解释量子效应，但它们对于模拟蛋白质折叠等过程仍然有用。本文旨在帮助读者理解MD相关的论文，并为运行基本模拟奠定基础。

---

## 15. 沃顿·埃舍里克与阿姆斯特朗油毡公司

**原文标题**: Wharton Esherick and the Armstrong Linoleum Company

**原文链接**: [https://whartonesherickmuseum.org/wharton-esherick-and-armstrong-linoleum/](https://whartonesherickmuseum.org/wharton-esherick-and-armstrong-linoleum/)

本文探讨了沃顿·埃舍里克标志性的三脚凳，以及它们与阿姆斯特朗油毡公司之间出人意料的联系。埃舍里克从20世纪50年代开始用剩余的木头边角料制作凳子，并以实惠的价格（最初25美元，后来50美元）出售，以贴补收入。这些凳子的设计考虑了舒适性和美观性，具有细长的腿和独特的手工塑形座椅。

1968年，阿姆斯特朗油毡公司在《妇女节》和《女士家庭杂志》等杂志的广告中使用了埃舍里克的凳子，宣传他们的新型油毡地板。这些广告以现代和乡村风格的厨房为背景，展示了这些凳子，引起了公众的极大兴趣。

埃舍里克收到了大量关于购买凳子的咨询，他和后来的米里亚姆·菲利普斯亲自回复了这些咨询。埃舍里克虽然感激大家的关注，但他强调自己不是大规模生产的制造商。

在二十多年的时间里，埃舍里克大约售出了300个凳子。如今，它们在二手市场上备受珍视，正如《古董巡回秀》中的一次亮相所强调的那样，其中一个凳子被估价为2500美元。除了三脚设计外，埃舍里克还创作了其他凳子设计，其中一些目前在他的工作室展出。

---

## 16. 在随机生成的数据中寻找雅达利游戏

**原文标题**: Finding Atari Games in Randomly Generated Data

**原文链接**: [https://bbenchoff.github.io/pages/FiniteAtari.html](https://bbenchoff.github.io/pages/FiniteAtari.html)

本文详细介绍了一个项目，该项目旨在从随机生成的数据中寻找可玩的雅达利2600游戏。作者生成了数十亿个4KB的随机数据文件，然后使用启发式方法和一个分类器系统（雅达利模拟器）来过滤和扫描它们，以寻找类似游戏的特征。

这个前提基于雅达利ROM庞大的数量($2^{32768}$)，这使得暴力破解方法不切实际。为了克服这个问题，作者开发了基于真实雅达利ROM结构的启发式方法，重点关注诸如有效6502操作码的存在、有效的重置向量，以及对TIA（用于图形和声音）和RIOT（用于输入/输出）芯片的访问等因素。特定的指令和寄存器访问模式被识别为功能性游戏的指标。

这些启发式方法已针对现有雅达利游戏的完整ROM集合进行了验证，以建立实际的阈值。创建了一个综合评分系统，对操作码比率、TIA访问、RIOT访问、分支指令和跳转指令进行加权。

为了加速这一过程，该项目使用CUDA在GPU上实现，从而可以大规模并行地生成和分析ROM。CUDA实现使用查找表来有效地识别操作码、TIA和RIOT模式。通过并行分析一百万个ROM，GPU实现与最初基于CPU的方法相比，极大地提高了性能。

---

## 17. Shell命令的奇特案例，或“这个bug是POSIX要求的”（2021）

**原文标题**: The curious case of shell commands, or how "this bug is required by POSIX" (2021)

**原文链接**: [https://notes.volution.ro/v1/2021/01/notes/502e747f/](https://notes.volution.ro/v1/2021/01/notes/502e747f/)

本文重点阐述了依赖`system(3)`和`sh -c`执行命令的工具所关联的安全风险，尤其是在处理用户输入时。作者认为这种方法存在根本性缺陷，可能导致 shell 注入漏洞。

核心问题在于，包括 `watch`、`ssh`、`i3`、`make` 以及构建系统等许多程序，将命令执行委托给 `sh -c`，后者会将输入解释为 shell 脚本。如果用户输入未得到适当的清理，攻击者便可注入恶意命令。作者批评 POSIX 标准未能充分警告这些危险。

本文提供了看似无害的命令由于不正确处理空格、引号和特殊字符而遭到利用的例子。作者提倡完全避免使用 `system(3)` 的工具，而倾向于直接使用 `execve(2)` 的工具。

在被迫使用存在漏洞的工具时，作者概述了涉及引号、使用 `exec` 以及使用 `--` 参数以防止将命令误解为标志的复杂的应对措施。最终，本文强调开发人员需要意识到这些安全风险，并优先选择安全地执行命令的工具。`printf`、`ssh` 和 `i3-msg` 的示例展示了安全使用这些工具所需的复杂引用和转义。

---

## 18. 在球体表面动画网格

**原文标题**: Animate a mesh across a sphere's surface

**原文链接**: [https://garden.bradwoods.io/notes/javascript/three-js/animate-a-mesh-on-a-spheres-surface](https://garden.bradwoods.io/notes/javascript/three-js/animate-a-mesh-on-a-spheres-surface)

本文介绍如何使用 three.js 和 GSAP 让网格模型沿着球体表面运动。 该过程包括定义球体表面上的路径，然后使网格模型沿着该路径运动。

首先，使用经度和纬度定义两个点，然后使用 `latLongToVector3` 函数将其转换为 3D 坐标。 接下来，使用 `calcPathPoints` 创建这些点之间的路径，该函数会生成沿着最短路径（大圆弧）的一系列点。 此路径使用 `createPath` 可视化。

对于动画，`animateMeshAlongPath` 使用 `THREE.CatmullRomCurve3` 从路径点创建平滑样条曲线。 GSAP 用于插值一个从 0 到 1 的值 `t`，表示动画进度。 网格模型的位置根据 `t` 使用 `spline.getPoint(t)` 进行更新。

为了确保网格模型正确地位于球体表面上，需要进行两个调整。 `setOriginYBottom` 调整网格模型的几何体原点，使底部与 y=0 对齐，防止其穿过球体。 `calcMeshQuaterionAlongPath` 计算网格模型旋转的正确四元数，确保其沿路径朝前，并相对于球体表面保持直立。 此函数使用切向量和法向量来正确定位网格模型。

---

## 19. “证明”影评：在数字中寻找真理

**原文标题**: 'Proof' Review: Finding Truth in Numbers

**原文链接**: [https://www.wsj.com/arts-culture/books/proof-review-finding-truth-in-numbers-b9779228](https://www.wsj.com/arts-culture/books/proof-review-finding-truth-in-numbers-b9779228)

无法访问文章链接。

---

## 20. 斯莱·斯通去世了。

**原文标题**: Sly Stone has died

**原文链接**: [https://abcnews.go.com/US/sly-stone-pioneering-leader-funk-band-sly-family/story?id=122666345](https://abcnews.go.com/US/sly-stone-pioneering-leader-funk-band-sly-family/story?id=122666345)

放克乐队Sly and the Family Stone的极具影响力的主唱Sly Stone去世，享年82岁，他生前一直与慢性阻塞性肺病和其他健康问题作斗争。该乐队以融合福音、放克和迷幻音乐而闻名，于20世纪60年代末凭借《Dance to the Music》、《Everyday People》和《Hot Fun in the Summertime》等热门歌曲以及1969年在伍德斯托克的激动人心的表演而声名鹊起。

Stone，本名Sylvester Stewart，与他的兄弟姐妹组建了种族融合的Family Stone乐队，以其独特的音乐风格和社会意识歌词彻底改变了音乐界。在组建乐队之前，他学会了演奏多种乐器，并最初担任唱片骑师。

尽管他们取得了巨大的成功，但该乐队也面临着药物滥用和演出缺席的挑战，最终导致了在20世纪70年代的衰落。Sly Stone在他的回忆录中承认与毒瘾作斗争。

Sly and the Family Stone乐队于1993年入选摇滚名人堂。近年来，一部名为《Sly Lives!》的纪录片和一部传记片的计划旨在揭示Stone的生活和遗产。Stone在2006年格莱美颁奖典礼上罕见地进行了表演，并在去世前完成了他的人生故事的剧本。他身后留下了三个孩子。

---

## 21. 为什么智能体不适合做结对编程

**原文标题**: Why agents are bad pair programmers

**原文链接**: [https://justin.searls.co/posts/why-agents-are-bad-pair-programmers/](https://justin.searls.co/posts/why-agents-are-bad-pair-programmers/)

作者在2025年5月30日的一篇博文中指出，像GitHub Copilot的代理模式这样的LLM智能体，作为结对程序员表现不佳，主要是因为它们编码速度太快，人类跟不上。作者将其与和技术高超的人类程序员结对的不良经历相提并论，这些程序员会快速地默默编码，让作者感到脱节和迷茫。

AI智能体快速的编码节奏阻碍了有意义的协作和理解，导致人类伙伴无法做出贡献或在智能体犯错或走错方向时纠正方向。

作者建议采用类似于GitHub新推出的Coding Agent的异步工作流程，即通过拉取请求审查，而不是基于编辑器的智能体结对。作者还建议在“编辑”或“提问”模式下使用基于编辑器的工具，这样可以实现更可控、回合制的互动，并促进更慢、更审慎的节奏。

为了改进AI驱动的结对编程，作者提出了使体验更像人类协作的功能，包括：控制智能体的编码速度，允许用户轻松暂停和提问，集成反映当前任务的UI元素，设计具有较少自信和更多自我怀疑的智能体以鼓励频繁对话，以及使用语音聊天进行更自然的交互。核心思想是，放慢节奏并促进对话将使AI智能体成为更有效和协作的结对编程伙伴。

---

## 22. Show HN: Munal OS: 一个带WASM沙盒的图形化实验性操作系统

**原文标题**: Show HN: Munal OS: a graphical experimental OS with WASM sandboxing

**原文链接**: [https://github.com/Askannz/munal-os](https://github.com/Askannz/munal-os)

Munal OS 是一个实验性的、基于 Rust 的操作系统，采用 unikernel 设计，专注于简洁性和基于 WASM 的沙箱安全机制。它直接作为 EFI 二进制文件启动，绕过传统引导加载程序，避免了页面映射，并在单个、身份映射的内存空间内运行。

主要特性包括：带有鼠标/键盘支持的完整图形 HD 界面、沙箱化的 WASM 应用程序、带有 TCP 协议栈的网络驱动程序以及可定制的 UI 工具包。该操作系统包含一个 Web 浏览器、文本编辑器和 Python 终端。它使用基于轮询的 VirtIO 驱动程序，用于键盘、鼠标、网络和 GPU 与 QEMU 的通信，而无需 CPU 中断。

该操作系统在单个全局事件循环中运行，轮询驱动程序、绘制 UI、运行 WASM 应用程序和刷新帧缓冲区。应用程序使用 wasmi WASM 引擎进行沙箱化，从而在没有虚拟地址空间的情况下实现内存隔离。应用程序通过自定义系统调用 API 与内核通信。

Munal OS 使用自定义 UI 工具包 (Uitk)，并通过样式表支持样式设置。缓存系统优化重绘。构建需要 Rust Nightly 和 QEMU。该项目承认受到 Philipp Oppermann 的 OS 教程的启发，并使用 Wasmi、smoltcp、Rustls 和 RustPython 等库。

---

## 23. CompactLog – 使用LSM树解决CT可扩展性问题

**原文标题**: CompactLog – Solving CT Scalability with LSM-Trees

**原文链接**: [https://github.com/Barre/compact_log](https://github.com/Barre/compact_log)

CompactLog：一个基于SlateDB的证书透明度(CT)日志实现，旨在通过利用LSM树存储解决可扩展性问题。它遵循RFC 6962 CT API，接受X.509证书，颁发SCT，维护Merkle树，并提供密码学证明，将数据存储在云对象存储或本地文件系统中。

关键区别包括通过SlateDB实现的LSM树存储、STH边界版本控制，以及消除合并延迟(MMD)的同步树更新。CompactLog通过在颁发SCT *之前*将证书合并到Merkle树中，在树更新前批量提交最多500毫秒来实现零MMD。

STH边界版本控制通过仅持久化已发布检查点的树状态来降低存储开销。它仅在STH发布边界处对节点进行版本控制，在批处理操作期间在内存中更新节点。

存储模式包括叶节点、版本化节点、最新节点版本、操作状态、证书哈希和SCT数据的数据。它具有使用内容寻址存储的证书链去重功能，通过哈希分别存储证书，并在检索期间重建链。

CompactLog保持严格的一致性，读取可以看到最新的已提交STH状态，序列化写入，并且仅在STH边界处提供证明可用性。配置通过`Config.toml`文件管理，允许自定义服务器绑定、存储提供商（本地、AWS或Azure）和密钥路径。系统在缺失时自动生成密钥和默认配置。

---

## 24. 苹果发布基础模型和容器化框架等

**原文标题**: Apple announces Foundation Models and Containerization frameworks, etc

**原文链接**: [https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/)

苹果于2025年6月9日的新闻稿详细介绍了旨在增强Apple平台应用创建的一系列全新开发者工具和技术，重点在于智能、设计和用户体验。一项关键公告是**Foundation Models框架**，它允许开发者将设备端Apple Intelligence集成到他们的应用中，使用Swift提供以隐私为中心的AI功能，并内置引导生成和工具调用支持。

**Xcode 26** 具有大型语言模型集成，包括对ChatGPT的支持，使开发者能够更高效地编写代码、测试和文档。Coding Tools为各种任务提供建议操作和内联提示。

一种采用 **Liquid Glass** 构建的全新软件设计，提供流畅且极具视觉吸引力的界面。 **Icon Composer app** 帮助开发者创建引人入胜的应用图标。

**App Intents** 现在支持视觉智能，允许像Etsy这样的应用将视觉搜索结果直接集成到他们的应用中。

**Swift 6.2** 增强了性能、并发性和互操作性，包括对WebAssembly的支持。

**Containerization框架** 使开发者能够在Mac上直接创建、下载和运行Linux容器镜像。

对于游戏开发，**Game Porting Toolkit 3** 提供了更新的评估和分析工具，而专为Apple芯片设计的 **Metal 4** 支持高级图形和机器学习。**Apple Games app** 引入了让玩家连接和竞争的新方式。Game Overlay增强了游戏内互动，Managed Background Assets简化了资产托管。

Apple推出了保护儿童在线的工具，包括 **Declared Age Range API**，使开发者能够在确保隐私的同时提供适合年龄的内容。

App Store上新的 **Accessibility Nutrition Labels** 向用户告知支持的辅助功能。App Store Connect app已更新，具有TestFlight和崩溃反馈的新功能。Apple Intelligence功能需要特定设备（iPhone 16型号、iPhone 15 Pro、iPad mini (A17 Pro) 以及配备M1及更高版本的iPad/Mac）和语言设置。

---

## 25. 成功人士设定约束，而非追逐目标。

**原文标题**: Successful people set constraints rather than chasing goals

**原文链接**: [https://www.joanwestenberg.com/smart-people-dont-chase-goals-they-create-limits/](https://www.joanwestenberg.com/smart-people-dont-chase-goals-they-create-limits/)

本文认为，成功人士更注重设定约束而非追逐目标。它挑战了目标对于成功至关重要的传统观念，并以捏造的耶鲁大学研究为例，强调了“目标设定崇拜”。作者认为，虽然目标可以提供一种进步的错觉，但它们往往导致人们在缺乏内在一致性的环境中工作，专注于结果而非方法。

本文强调，约束或界限，在应对复杂和不确定的情况下更为有效。约束有助于定义一个人不愿违反的东西，从而带来更清晰、更有意义的工作。与目标不同，目标是对未来的赌注，而约束是适应性的，并且对反馈做出响应。它们将注意力集中在真正重要的事情上，揭示了目标经常忽略的“隐形漏洞”。

约翰·博伊德的OODA循环、理查德·费曼的问题解决方法，以及NASA的登月计划等例子，都说明了约束如何促进创造力和创新。作者还介绍了“反目标”的概念——拒绝像雄心壮志一样有力地塑造生活。

最终，本文提倡从以结果为导向的目标转向以约束为导向的思维，尤其是在模糊和定义不清的领域。文章以博伊德的问题结尾：“你想成为什么人，还是你想做些什么？” 将目标定义为源于前者，约束源于后者，表明身份驱动的约束会带来更大的成长潜力。

---

## 26. 在 Forth 中实现 DOES>， 这就是我开始这一切烂摊子的原因。

**原文标题**: Implementing DOES> in Forth, the entire reason I started this mess

**原文链接**: [https://boston.conman.org/2025/06/09.1](https://boston.conman.org/2025/06/09.1)

本文详细介绍了作者理解和实现Forth中`DOES>`的历程，`DOES>`是一个允许创建具有自定义运行时行为的“智能数据结构”的词。作者解释了由于其时间复杂性和缺乏清晰文档，尤其是在JonesForth实现中，理解其实现的挑战。

`DOES>`的关键在于其三个时间方面：定义词的编译、新词的创建和新词的执行。在编译时，`DOES>`将其自身的运行时编译到定义词中，并准备稍后编译其后的代码。在新词的创建过程中，`DOES>`修改新词的执行令牌（XT），使其指向定义词中`DOES>`之后的代码。在运行时，新词执行一个特殊的钩子`forth_core_create.does_hook`，该钩子将新词主体的地址压入堆栈，然后跳转到定义词内`DOES>`之后的代码。

作者提供了一个使用`CREATE`、`SHAPE`和`MAN`的详细示例，展示了XT是如何更新的，以及`does_hook`是如何管理执行流程的。6809汇编代码说明了该过程。作者最后推测，JonesForth没有实现`DOES>`的原因可能是由于现代系统中常见的安全限制，即需要内存既可写又可执行。

---

## 27. Go 适合智能体

**原文标题**: Go is a good fit for agents

**原文链接**: [https://docs.hatchet.run/blog/go-agents](https://docs.hatchet.run/blog/go-agents)

本文认为，由于其并发模型、基于通道的通信、集中式取消机制、广泛的标准库以及性能分析工具，Go 是构建代理（尤其是大规模代理）的强大选择。

作者将代理定义为在循环中执行，并对其执行路径具有自主权的进程，并强调了它们的特点：长期运行、昂贵的执行、用户交互以及大量的 I/O 等待时间。 这就需要一个能够处理许多并发、长期运行的进程的运行时环境，这使得 Go 的 goroutine 成为理想之选。

Go 的轻量级 goroutine（2kb 预分配内存）和多核利用率允许高并发，与 Node.js 或 Python 等单线程运行时相比，开销更低。 使用通道的“通过通信共享内存”范例，通过避免对互斥锁等复杂同步机制的需求，简化了代理循环。

作者进一步强调了集中式取消机制的重要性，Go 的 `context.Context` 有效地提供了这一点，节省了用户停止执行时的资源。 Go 专为 Web I/O 设计的广泛标准库，以及该语言的单一并发模型，通过避免需要处理多个并发范例和研究库的兼容性，简化了开发。 最后，Go 提供了强大的性能分析工具，用于识别和解决内存和 goroutine 泄漏问题。 作者提到的一个额外好处是，LLM 擅长编写 Go 代码，因此您可以在编程时获得 LLM 的帮助。

虽然承认 Go 的局限性，如第三方支持滞后、缺乏机器学习库以及使用 Rust 或 C++ 等语言可能获得更好的性能，但作者的结论是，Go 的优势使其成为构建可扩展且高效的代理的引人注目的选择。

---

## 28. 苹果在各平台推出通用设计

**原文标题**: Apple introduces a universal design across platforms

**原文链接**: [https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/](https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/)

苹果宣布了一项重大的软件设计改革，旨在统一其平台（iOS 26、iPadOS 26、macOS Tahoe 26、watchOS 26 和 tvOS 26），使其拥有单一、一致的美学风格。本次更新将于 2025 年 6 月 9 日发布，重点是改善内容专注度、增强活力，并在 Apple 设备上提供直观的熟悉感。

新设计的基石是“液态玻璃”，一种半透明材料，能够动态适应内容和周围环境，反射和折射光线。这种材料正被集成到各种 UI 元素中，从按钮和控件到侧边栏和 Dock，从而创造更具沉浸感和吸引力的用户体验。

应用程序设计已经更新，以更好地与现代硬件的圆角相协调，从而促进硬件、软件和内容之间的和谐。控件和导航元素现在都由液态玻璃制成，能够流畅地适应用户交互。标签栏会在滚动时缩小以突出显示内容，而 iPadOS 和 macOS 中的侧边栏会折射内容以提供上下文感。

锁屏、主屏幕、桌面和 Dock 等系统体验也正在接收液态玻璃增强功能。例如，锁屏时间会适应照片壁纸的主题，而 macOS Tahoe 26 的 Dock 和桌面提供可定制的小部件和应用程序图标，具有浅色、深色、着色和透明外观。

苹果正在为开发者提供更新后的 SwiftUI、UIKit 和 AppKit 的 API，以促进在其应用程序中采用新的设计元素。这包括用于跨平台创建液态玻璃图标的工具。

本质上，本次更新代表了苹果迄今为止最广泛的软件重新设计，旨在在其整个生态系统中创造更统一、更具表现力和更令人愉悦的用户体验。

---

## 29. 永远在线，永远互联，永远搜索，永远分心

**原文标题**: Always On, Always Connected, Always Searching, Always Distracted

**原文链接**: [https://leejo.github.io/2025/06/10/always_on/](https://leejo.github.io/2025/06/10/always_on/)

这篇酝酿了十余年的博文，探讨了作者在充斥着图像和信息的世界中，与摄影和文化不断演变的关系。文章以加拿大的一次公路旅行和对比尔·沃特森采访的反思为开端，作者感叹在分裂、原子化的社会中，共享文化体验的丧失。

文章继而穿梭于各种旅行和摄影活动，质疑过度生产时代中个体图像的价值，强调语境和长期项目的必要性。作者批判对摄影“规则”的墨守成规和艺术界的虚伪，突出了对认可的渴望与在线验证的短暂性之间的矛盾。

作者进一步反思了技术和文化变革不可持续的步伐，探讨了在线社区分裂成越来越窄的利基市场。前往日本和中国的旅程揭示了技术进步与传统价值观之间的对比，突出了对长期项目的承诺和对消失世界的记录。作者的旅程最终在意大利达到高潮，在那里他继续努力理解摄影在一个被文化淹没的世界中的意义。最终，这篇文章探讨了在不断分心和信息过载的时代，创造有意义的作品所面临的挑战。

---

## 30. 封装的Co–Ni合金提升高温CO2电还原

**原文标题**: Encapsulated Co–Ni alloy boosts high-temperature CO2 electroreduction

**原文链接**: [https://www.nature.com/articles/s41586-025-08978-0](https://www.nature.com/articles/s41586-025-08978-0)

本文介绍了一种用于固体氧化物电解池（SOECs）高温CO2电还原的高效稳定催化剂。该催化剂为封装在Sm2O3掺杂的CeO2（SDC）内的Co-Ni合金，在1 A cm-2和800°C下，CO2转化为CO的能量效率达到90%，寿命超过2000小时，优于现有催化剂。

Co0.5Ni0.5@SDC催化剂表现出接近100%的CO选择性和90%的单程转化率。其卓越性能源于独特的封装结构和优化的合金成分。封装结构可防止合金团聚，同时为CO2吸附和CO解吸创造丰富的界面，从而克服了典型的活性/稳定性权衡。

表征数据证实了封装结构、Co-Ni合金化以及合金与SDC之间的电荷转移，从而增强了氧离子传输。稳定性测试凸显了封装催化剂的稳健性，而非封装催化剂随时间推移会显著降解。该研究强调了这种催化剂设计在高温CO2转化工业应用中的潜力。

---

## 31. 海军陆战队正在动员以应对洛杉矶的抗议活动

**原文标题**: Marines being mobilized in response to LA protests

**原文链接**: [https://www.cnn.com/2025/06/09/politics/marines-mobilized-los-angeles-protests](https://www.cnn.com/2025/06/09/politics/marines-mobilized-los-angeles-protests)

为应对洛杉矶的抗议活动，来自加利福尼亚州海军陆战队空地作战中心超过700名海军陆战队员正在动员，加入此前由特朗普总统启动的数千名国民警卫队成员的行列。此次部署标志着特朗普对抗议者使用军队的显著升级，尽管他们的具体任务仍不清楚。与国民警卫队一样，除非援引《叛乱法》，否则他们不得从事执法活动。

这些来自第一海军陆战师第七海军陆战团第二营的海军陆战队员，预计将加强国民警卫队的存在，可能协助人群控制和周边安全。此次部署是自1992年洛杉矶暴动以来，美国境内首次为应对内乱而动员海军陆战队。

加州州长加文·纽森批评此次动员是“不必要的”和“前所未有的”，而洛杉矶警察局长吉姆·麦克唐纳则强调所有响应机构之间需要公开沟通，以确保协调和合法的应对。国防部正在最终确定部队的武力使用准则，预计将与标准的军事规则相符。

---

## 32. 海洋酸化突破“行星边界”

**原文标题**: Ocean acidification crosses "planetary boundaries"

**原文链接**: [https://insideclimatenews.org/news/09062025/ocean-acidification-crosses-planetary-boundaries/](https://insideclimatenews.org/news/09062025/ocean-acidification-crosses-planetary-boundaries/)

一项发表在《全球变化生物学》上的新研究显示，海洋酸化已跨越了一个关键的“地球边界”，对海洋生态系统构成的威胁比之前认为的更大。这项由多个机构研究人员参与的研究发现，到2020年，世界海洋已接近或已进入酸度的“危险区”。衡量标准是海洋生物用来建造外壳的碳酸钙含量，目前已比工业化前水平降低了17%，超过了被认为是边界的20%阈值。

海洋酸化是由于从大气中吸收过量二氧化碳所致，正在全球范围内影响海洋，从表层水域到更深层次。该研究强调，拥有多样海洋生物的深层水域正在经历更严重的酸化。这导致栖息地丧失，热带珊瑚礁、极地地区的海蝶种群和沿海贝类物种已经遭受重大损失。

科学家们将海洋酸化确定为对人类生存至关重要的九个地球边界之一，其中六个已经突破。研究结果强调了解决该问题的紧迫性，尤其是在极地地区和西海岸等高产地区，这些地区正在经历重大影响。虽然专家们正在联合国海洋大会上讨论解决方案，但该研究的作者强调，需要利用这项研究来影响政策，并促使采取行动来保护世界海洋。

---

## 33. 显微镜图志 (1665) [pdf]

**原文标题**: Micrographia (1665) [pdf]

**原文链接**: [https://arhipa.org/libros/Hooke_Robert_Micrographia-1665.pdf](https://arhipa.org/libros/Hooke_Robert_Micrographia-1665.pdf)

这个PDF似乎是罗伯特·虎克所著《显微图谱》(1665年)的数字扫描版。它是显微学和科学观察的奠基之作。 从无法辨认的内容中散落的词语和短语（例如，“显微图谱”、“1665”、“罗伯特·虎克”）可以辨认出该文本，其中呈现了虎克对微观观察的详细描述和插图。

鉴于PDF内容的性质（文本的扫描图像），其主要价值在于其作为虎克开创性工作的数字档案的历史意义。虽然由于格式原因无法直接访问文本，但PDF保留了该书的原始视觉布局和形式。

《显微图谱》的关键方面（来自对该作品的一般了解，而不是来自所提供摘录的可访问文本）包括：

*   **开创性的显微学：** 虎克使用显微镜揭示了以前未见的微小结构世界。
*   **详细的观察：** 他对昆虫、植物和其他材料的细致记录。
*   **插图：** 包含精心制作的雕刻，以视觉方式呈现他的发现，普及了显微镜和科学探究。
*   **“细胞”的发现：** 也许是最著名的贡献，虎克在软木中识别出细胞结构，他称之为“cells”（细胞）。

该PDF代表了这份具有里程碑意义的科学文献的数字化形式，为研究人员和公众提供了访问科学史上这一关键作品的途径。

---

## 34. 学术论文：创新还是模仿？

**原文标题**: Scientific Papers: Innovation or Imitation?

**原文链接**: [https://www.johndcook.com/blog/2025/06/05/scientific-papers-innovation-or-imitation/](https://www.johndcook.com/blog/2025/06/05/scientific-papers-innovation-or-imitation/)

本文探讨了科学研究中创新与模仿之间的平衡，认为虽然衍生性工作是自然且有时有益的，但如果开创性思想没有被充分掌握和探索，该领域可能会受到影响。作者以麦卡洛克-皮茨关于神经网络的论文和乔治·米勒关于短期记忆的“7±2”论文为例，指出这些开创性著作的更广泛意义常常被忽视，导致衍生研究而非突破性进展。

作者认为，出版的激励机制（奖励快速评估和微小调整）助长了这一趋势。“烟囱效应”，即只关注狭窄领域，限制了研究人员看到跨学科联系并识别潜在新研究途径的能力。

本文承认，当前的人工智能研究表现出创新与模仿的混合，部分原因是加速主义心态的驱动。作者还指出，有时在没有方法论严谨性的情况下就对人脑做出声明。同样，由于不同领域的“烟囱效应”也可能出现错误。总而言之，本文倡导一种更全面的科学研究方法，鼓励研究人员超越眼前的结果，探索开创性工作的更大意义。

---

## 35. 医生可以用超声波入侵神经系统

**原文标题**: Doctors could hack the nervous system with ultrasound

**原文链接**: [https://spectrum.ieee.org/focused-ultrasound-stimulation-inflammation-diabetes](https://spectrum.ieee.org/focused-ultrasound-stimulation-inflammation-diabetes)

本文探讨了聚焦超声刺激（FUS）作为一种新型、非侵入性技术，通过靶向神经系统来治疗各种疾病。研究人员正在探索FUS来调节神经细胞活动，从而可能提供一种针对性替代方案，以取代具有广泛副作用的药物。

本文强调了FUS在治疗炎症方面的潜力。研究表明，超声刺激脾脏可以减少细胞因子生成和炎症反应，模拟迷走神经刺激（VNS）的效果，而无需手术。初步人体试验表明，FUS治疗降低了肿瘤坏死因子（TNF）水平，这是一种炎症生物标志物。

此外，本文还探讨了FUS在肥胖症和糖尿病中的应用。对喂食高脂肪食物的小鼠进行的实验表明，FUS可降低细胞因子水平，减少食物摄入量和减轻体重。在糖尿病大鼠中，FUS靶向肝脏中的葡萄糖感应神经元，使葡萄糖水平正常化。研究表明，FUS会影响从肝脏到大脑的葡萄糖感应信号，从而改变下丘脑向身体代谢系统发出的指令。

本文还涉及FUS在治疗心肺疾病，特别是肺动脉高压方面的潜力。对大鼠的研究表明，FUS治疗可降低肺动脉压力，改善心脏功能并减少肺部炎症。

作者设想未来可以通过人工智能系统引导，在家中使用可穿戴设备进行FUS治疗。然而，他们强调需要进一步的研究，包括临床试验，以充分了解FUS的机制并验证其在治疗慢性疾病方面的有效性。

---

## 36. 柏拉图几乎全错了（2018）

**原文标题**: Plato got virtually everything wrong (2018)

**原文链接**: [https://www.prospectmagazine.co.uk/opinions/41672/plato-got-virtually-everything-wrong](https://www.prospectmagazine.co.uk/opinions/41672/plato-got-virtually-everything-wrong)

朱利安·巴吉尼在他的文章《柏拉图几乎全错了》中认为，虽然柏拉图是个天才，但他的思想却大错特错，并且持续对西方思想产生负面影响。巴吉尼批评柏拉图犯了几个关键错误。

首先，柏拉图关于灵魂在死亡后继续存在的概念导致了身心二元论，阻碍了现代思维。其次，柏拉图为真知设定了过高的标准，导致人们对它的可获得性产生怀疑。第三，他通过必要和充分条件来定义术语的方法是有缺陷的，因为语言更加细致，并且基于用法，而不是严格的定义。第四，柏拉图错误地认为，在试图实现理想之前必须定义理想，这阻碍了诸如正义之类的目标的进展，因为它会延迟行动，直到达成完美的定义。最后，巴吉尼认为，柏拉图的苏格拉底所实践的“苏格拉底式方法”是一种具有破坏性的对抗性辩论模式，缺乏真正的对话并阻碍了智力进步。

巴吉尼总结说，柏拉图的才华正是问题所在，因为他对有缺陷的思想提出的令人信服的论点对西方知识文化产生了持久且不利的影响。

---

## 37. 容器：苹果公司的Linux容器运行时

**原文标题**: Container: Apple's Linux-Container Runtime

**原文链接**: [https://github.com/apple/container](https://github.com/apple/container)

`container` 是苹果公司开发的工具，允许你在 Apple 芯片 Mac 上创建和运行 Linux 容器，将其作为轻量级虚拟机。它用 Swift 编写，针对 Apple 的架构进行了优化，并使用 Containerization Swift 包进行底层容器管理。

主要功能包括：

*   **OCI 兼容性：** 它与标准 OCI 兼容的容器镜像协同工作，允许你从任何注册表拉取和运行镜像，并推送你构建的镜像。
*   **

本质上，`container` 提供了一种在 macOS 上运行基于 Linux 的容器化应用程序的方法，利用容器化的优势，如可移植性和效率，同时通过其 OCI 兼容性融入更广泛的容器生态系统。

---

## 38. 西班牙科学家拉斐尔·卢克因欺诈被撤回11项研究。

**原文标题**: Eleven studies by Spanish scientist Rafael Luque retracted due to fraud

**原文链接**: [https://english.elpais.com/science-tech/2025-06-10/eleven-studies-by-spanish-scientist-rafael-luque-are-retracted-due-to-fraudulent-practices.html](https://english.elpais.com/science-tech/2025-06-10/eleven-studies-by-spanish-scientist-rafael-luque-are-retracted-due-to-fraudulent-practices.html)

本文详细介绍了西班牙化学家拉斐尔·卢克的欺诈行为，他因数据操纵和可疑的署名变更而被撤回了11篇研究。卢克通过发表大量无足轻重的研究、与全球研究人员合作，并利用这些合作来增加引用和提升学术排名而声名狼藉。他最终在克里姆林宫获得荣誉。

一种名为Argos的分析工具揭示了他异常的发表模式，表明存在一个通过作弊来膨胀声誉的国际网络。ChatGPT帮助了卢克高产的发表速度，他承认这加速了他的写作过程。本文重点介绍了他与其他撤稿数量众多的科学家的合作。

作弊的驱动力是金钱，因为学术机构竞相招募高引用率的科学家以提高其排名。卢克为获取经济利益而虚假声称隶属于沙特大学，导致他于2022年被科尔多瓦大学开除。他的签名出现在多个国家的研究中，表明他可能一直在出售他的署名权。尽管他的欺诈活动已被曝光，但卢克仍坚称自己是无辜的，并将批评归咎于嫉妒。

---

## 39. 为什么C++认为我的类是可复制构造的，即使它不能？

**原文标题**: Why does C++ think my class is copy-constructible when it can't be?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250606-00/?p=111254](https://devblogs.microsoft.com/oldnewthing/20250606-00/?p=111254)

`std::is_copy_constructible`为何有时会误报类可拷贝构造：存在声明但编译期报错

---

## 40. 北斋模様画谱：染色图样集

**原文标题**: Hokusai Moyo Gafu: an album of dyeing patterns

**原文链接**: [https://ndlsearch.ndl.go.jp/en/imagebank/theme/hokusaimoyo](https://ndlsearch.ndl.go.jp/en/imagebank/theme/hokusaimoyo)

本文介绍葛飾北斎创作的图案集《北斎模様画譜》。该画谱作为染色图案的样本集出版，收录了北斎创作的众多原创设计。本文展示了来自NDL图像库的画谱图像。

NDL图像库是日本国立国会图书馆（NDL）提供的公共领域数字画廊，收录了图书馆馆藏的大量无版权日本艺术品和图像。

除了北斎的画谱外，本文还重点介绍了通过NDL图像库和NDL Gallery提供的其他相关资源，包括纺织品设计书籍（例如《友紋百花》、《明治図案文明振》、《著選集》）、植物设计（例如《樱花模様》、《梅尽》、《翡翠百花譜》）和其他图案集（例如《百蝶図案》）等各种收藏。

NDL Gallery是一个在线空间，展示了国立国会图书馆举办的展览的数字化资料和信息。NDL数字展览以诸如*锦絵*、风景照片和历史资料等主题组织，提供NDL独特馆藏的精选展示。本质上，本文旨在推广NDL的数字资源，并强调该馆藏中提供的北斎画谱。

---

## 41. 施乐奥托、Smalltalk 以及重写运行中的 GUI (2017)

**原文标题**: The Xerox Alto, Smalltalk, and rewriting a running GUI (2017)

**原文链接**: [https://www.righto.com/2017/10/the-xerox-alto-smalltalk-and-rewriting.html](https://www.righto.com/2017/10/the-xerox-alto-smalltalk-and-rewriting.html)

本文探讨了施乐奥托（Xerox Alto）计算机及其Smalltalk-76环境，重点介绍了Smalltalk的革命性功能，尤其是其在运行时修改系统代码的能力。作者描述了修复Alto的过程，并探讨了Smalltalk的桌面隐喻，包括重叠窗口、弹出菜单和类浏览器。

本文强调了Smalltalk的动态特性，展示了作者如何通过类浏览器修改和重新编译代码，从而在运行的系统中更改滚动条的外观。它还提供了一个查看平方根函数代码的例子，并描述了Smalltalk独特的语法。

参与Smalltalk开发的Alan Kay为本文添加了宝贵的评论，分享了关于史蒂夫·乔布斯访问施乐PARC的轶事、代码更改的速度以及图标的演变。他还感叹，运行时修改系统的能力（Smalltalk和Lisp的标志）至今仍未被广泛采用。文章最后讨论了Smalltalk对现代面向对象编程语言的影响，并提到了当代的Smalltalk系统，如Pharo、GNU Smalltalk和Squeak。

---

## 42. 离散数学：开放式导论 [pdf]

**原文标题**: Discrete Mathematics: An Open Introduction [pdf]

**原文链接**: [https://discrete.openmathbooks.org/pdfs/dmoi4.pdf](https://discrete.openmathbooks.org/pdfs/dmoi4.pdf)

文档“离散数学：开放式导论[pdf]”看似为PDF文件，但所提供的内容主要为PDF对象数据和压缩流。它不包含书中可读的文本。数据包括XObject定义（可能用于图像或矢量图形）、包含压缩数据的对象流以及各种PDF特定的指令和资源。大量压缩数据流表明该文档包含复杂的格式，并且可能包含图像和/或图表。

由于缺少“离散数学：开放式导论”的实际文本，因此无法提供其内容的摘要。所包含的数据仅描述了PDF的结构，而非涵盖的数学概念。要理解本书的内容，需要渲染PDF并提取文本信息。

---

## 43. 亚甲蓝对大脑的作用 (与局限)

**原文标题**: What methylene blue can (and can’t) do for the brain

**原文链接**: [https://neurofrontiers.blog/what-methylene-blue-can-and-cant-do-for-the-brain/](https://neurofrontiers.blog/what-methylene-blue-can-and-cant-do-for-the-brain/)

本文探讨了亚甲蓝(MB)据称具有的促进大脑功能的益处。亚甲蓝是一种用途广泛且历史悠久的药物，可用于治疗高铁血红蛋白血症甚至鱼缸维护。虽然亚甲蓝作为一种改善记忆和情绪的“神奇补充剂”备受关注，但本文深入研究了其科学原理，旨在区分炒作与现实。

亚甲蓝的潜力在于其多方面的细胞效应：它作为一种单胺氧化酶(MAO)抑制剂，影响多巴胺和血清素等神经递质；通过防止自由基形成来辅助线粒体功能；并阻断一氧化氮，导致血管收缩。然而，在分离细胞中观察到的这些有希望的机制并不能保证在人体中的成功，因为生物相互作用非常复杂。本文还强调了亚甲蓝的剂量效应，即低剂量有益，高剂量有害。

虽然动物研究显示其在治疗各种神经系统疾病方面具有潜力，但人体试验有限。一些小型研究显示，它对双相情感障碍、重度抑郁症和精神分裂症的症状有所改善，但需要更大规模的试验。一项针对阿尔茨海默病的大型III期研究没有显示出积极效果。目前还没有数据显示健康人服用亚甲蓝会产生什么影响。

本文告诫不要广泛使用亚甲蓝，因为它可能产生副作用，如膀胱刺激、恶心，以及更严重的，G6PD缺陷患者的溶血性贫血，以及与SSRIs合用时的5-羟色胺综合征。高剂量也会抑制线粒体功能。非处方补充剂缺乏监管以及未知的安全剂量进一步增加了风险。作者总结说，在亚甲蓝被认为是安全有效的健脑补充剂之前，还需要进一步的研究。

---

## 44. 新型量子算法用一个量子比特分解数字

**原文标题**: New Quantum Algorithm Factors Numbers with One Qubit

**原文链接**: [https://www.quantamagazine.org/new-quantum-algorithm-factors-numbers-with-one-qubit-20250609/](https://www.quantamagazine.org/new-quantum-algorithm-factors-numbers-with-one-qubit-20250609/)

本文探讨了一种新型量子算法，该算法仅用一个量子比特即可分解数字，这与肖尔算法中需要多个量子比特的传统方法有显著不同。该算法由慕尼黑工业大学的研究人员开发，利用振荡器执行分解的数学运算，并使用连续变量而不是离散量子比特值来编码信息。

虽然该算法在理论上具有开创性，但它存在一个主要缺点：分解大型数字需要指数级的能量，可能相当于多颗恒星的能量输出。这使得它目前在实际应用中不切实际。

尽管存在能量成本，这一发现为计算思维和在量子计算中利用连续变量系统开辟了新思路。该研究表明，除了量子比特之外的组件（如振荡器）可以用于计算，从而为替代量子算法和实现方式打开了可能性。慕尼黑研究小组正在探索降低能量需求的方法，并将该方法应用于分解之外的其他计算问题。本文强调了使用连续变量系统运行算法的新颖性，以及利用量子设备中已有的其他组件进行计算的潜力。

---

## 45. 展示 HN: 一款 16 x 9 像素的开源节奏地牢探索游戏

**原文标题**: Show HN: An open-source rhythm dungeon crawler in 16 x 9 pixels

**原文链接**: [https://github.com/jgalecki/qrawl-tiny-mass-disco](https://github.com/jgalecki/qrawl-tiny-mass-disco)

这个“Show HN”帖子介绍QRawl：微型质量迪斯科，一个16x9节奏地牢探险游戏，作为微型质量游戏项目的一部分创建，现已开源。作者重点介绍了设计此类游戏的两个关键方面：节奏组件和地牢探险元素。

关于节奏方面，作者推荐fizzd的《冰与火之舞》教程，强调其对于节奏游戏开发的永恒价值。对于地牢探险部分，灵感来自该类型的先驱《节奏地牢》。玩家输入被分为几种状态：无、早、好、良好、优秀、晚、失败和错过，每种状态都与相对于节拍的特定时序相关联。当到达下一个节拍的25%时，会发送一个“节拍结束信号”，关闭节拍逻辑。

核心创新在于“时间旅行”的实现，以协调节奏和移动。游戏会在一个节拍到来但没有玩家输入时保存一个游戏状态的副本（previous_game_state）。如果玩家在有效窗口内稍后输入，则该动作将应用于previous_game_state。这使得迟到但有效的玩家输入能够在怪物做出反应之前影响游戏世界，从而保持一切同步。

最后，作者提到了一些关于16x9像素限制的轻微规则调整，用于显示制作人员名单以及最终揭示地牢是一个二维码。他们表达了对未来基于二维码的地牢探险概念的兴趣。该项目采用MIT许可证。

---

## 46. AI让我的公司从两年的诉讼噩梦中解脱

**原文标题**: AI Saved My Company from a 2-Year Litigation Nightmare

**原文链接**: [https://tylertringas.com/ai-legal/](https://tylertringas.com/ai-legal/)

在一篇2025年6月8日发表于《创业家》杂志的文章中，作者详细描述了人工智能如何从一场耗时且代价高昂的两年法律诉讼中拯救了他们的公司，Calm Company Fund。作者认为，特拉华州的法律体系对被告不利，即使胜诉，被告也常常承担巨额费用，这鼓励了和解。他们强调了驳回动议和简易判决的局限性，强调被告常常面临“囚徒困境”，促使他们无论案件是否有价值都倾向于和解。

作者最初将案件委托给律师处理，结果证明既昂贵又无效。他们强调企业家积极管理法律诉讼的重要性，将律师视为“总承包商”，而不是被动地接受他们的建议。他们主张最大限度地降低成本，并创造对对方的杠杆作用，以鼓励和解。

转折点出现在作者开始使用人工智能，特别是像Claude或ChatGPT这样的LLM，来分析合同、文件和判例法时。这使他们能够形成知情的观点，挑战法律顾问，并最终做出战略决策，以最大限度地降低成本和最大限度地提高杠杆作用。他们的人工智能法律研究工作流程包括将所有相关文件上传到人工智能平台，使用人工智能作为“教练”来理解法律原则和机制，并利用人工智能分析复杂合同的能力。这种人工智能驱动的方法使他们能够成功地以有利的条件解决诉讼，从而拯救了他们的公司。

---

## 47. Show HN: 实现最新规范的 MCP 服务器和客户端

**原文标题**: Show HN: A MCP server and client implementing the latest spec

**原文链接**: [https://github.com/hemanth/paws-on-mcp](https://github.com/hemanth/paws-on-mcp)

Paws-on-MCP是一个全面的模型上下文协议（MCP）服务器实现，符合最新的MCP 2025-03-26规范。它展示了MCP的各项功能，包括工具、资源、提示、根以及通过模型偏好增强的采样，并利用了HackerNews和GitHub API集成。

核心功能已达到生产就绪状态，5个测试套件中有3个通过。所有MCP工具、资源和提示都功能齐全，并符合MCP规范。增强采样，包括模型偏好和上下文感知采样，也已正常工作。在负载下，MCP根和增强采样测试的并发性方面存在限制。

该项目包括一个用于测试的CLI客户端、全面的测试套件和详细的文档。提供了用于安装和运行服务器和测试的快速入门说明。

主要功能包括完整的MCP 2025-03-26规范支持、通过模型偏好和提示增强的采样，以及丰富的CLI客户端。服务器使用async/await框架和SSE传输。

该实现提供了9个可用的工具（包括用于HackerNews和GitHub的工具）、15个可用的资源（包括HackerNews、GitHub和采样策略）以及14个可用的提示模板。它以MIT许可证发布，并声称具有60%的测试覆盖率。

---

## 48. 帕斯卡三角中的圆周率 (2014)

**原文标题**: Pi in Pascal's Triangle (2014)

**原文链接**: [https://www.cut-the-knot.org/arithmetic/algebra/PiInPascal.shtml](https://www.cut-the-knot.org/arithmetic/algebra/PiInPascal.shtml)

本文探讨了$\pi$在帕斯卡三角形中令人惊讶的存在，通过涉及二项式系数和三角数的各种级数。文章首先介绍了Daniel Hardisky对尼拉坎塔·索玛雅吉$\pi$级数的修改，将其表示为组合数倒数之和。文章重点介绍了Tony Foster的观察，他将尼拉坎塔级数的 denominador 与毕达哥拉斯三角形的面积联系起来。

文章随后介绍了其他使用二项式系数的$\pi$级数表示，包括Leibniz级数的重新表述和另一个尼拉坎塔级数的改编。文章还介绍了Jonas Castillo Toloza发现的$\pi - 2$级数，该级数涉及三角数的倒数，三角数也可以表示为组合数。这个级数被认为是显著的，作者计划专门用一页来介绍包含其推导过程。总而言之，本文展示了$\pi$（看似与帕斯卡三角形和组合数学无关）可以通过涉及二项式系数及其与毕达哥拉斯三角形和三角数等几何概念的联系的级数来表达的几种方式。

---

## 49. Algovivo：一种基于能量的软体虚拟生物建模方法

**原文标题**: Algovivo an energy-based formulation for soft-bodied virtual creatures

**原文链接**: [https://juniorrojas.com/algovivo/](https://juniorrojas.com/algovivo/)

本文介绍Algovivo，一种基于能量的软体虚拟生物模拟方法。其重点在于提供一种能够真实模拟这些生物内在的复杂形变和行为的方法。

Algovivo的核心概念是将虚拟生物表示为一个具有相关能量势的互连节点网络。这些能量势捕捉了诸如静止形状、刚度和驱动力等属性。通过最小化系统的总能量，模拟确定生物的形变状态。

这种基于能量的方法的一个关键优势在于，它比传统的基于力的方法更稳健地处理复杂的形变和自碰撞。能量公式允许直接计算平衡状态，减少了对显式时间积分的需求，从而提高了稳定性。

本文可能详细阐述了用于模拟生物材料属性和驱动机制的特定能量函数。它可能讨论了如何参数化这些能量函数，以及如何调整参数来控制生物的行为和运动。

此外，Algovivo基于能量的基础使其能够轻松应用优化技术。这使其适用于生物设计、控制器学习和形态计算等任务，从而能够开发自主和自适应的虚拟生物。

本质上，Algovivo通过利用基于能量的公式，为模拟软体虚拟生物提供了一个引人注目的框架，该公式在稳定性、处理复杂形变以及促进基于优化的设计和控制方面具有优势。

---

## 50. 重建印加绳桥的男人

**原文标题**: A man rebuilding the last Inca rope bridge

**原文链接**: [https://www.atlasobscura.com/articles/last-inca-rope-bridge-qeswachaka-tradition](https://www.atlasobscura.com/articles/last-inca-rope-bridge-qeswachaka-tradition)

本文讲述了每年重建Q'eswachaka桥的传统，这是现存的最后一座印加绳桥。记者艾略特·斯坦因描述了他前往秘鲁记录这一古老习俗的旅程，这记录将收录在他的著作《奇迹守护者》中。这座桥完全由草编织而成，横跨安第斯山脉一条湍急的河流，长达100英尺。

这项传统由维克多里亚诺·阿里扎帕纳领导，他是最后一位桥梁建造者(chakaruwaq)，也是拥有500年历史传统的继承人。每年，四个当地社区通过提供编织的稻草(coya)来参与minka（一种源自印加米塔概念的公共劳动形式）。维克多里亚诺负责监督整个过程，确保材料符合标准，并指导社区编织巨大的缆绳并将其吊到河上。

文章描述了为期三天的庆祝活动，最终由维克多里亚诺赤脚悬挂在河面上编织桥梁的最后一部分而达到高潮。尽管附近存在一座现代钢桥，但这些社区仍在延续这一传统，将其视为生命的更新和与遗产的连接。重建这座桥并非没有风险，但它加强了社区联系并保存了印加历史。迪伦·图拉斯和艾略特·斯坦因都强调了这座桥独特的建筑奇迹以及它与印加帝国保持的精神联系。

---

## 51. 新的哥德尔奖得主味道好极了，而且不那么油腻。

**原文标题**: The new Gödel Prize winner tastes great and is less filling

**原文链接**: [https://blog.computationalcomplexity.org/2025/06/the-new-godel-prize-winner-tastes-great.html](https://blog.computationalcomplexity.org/2025/06/the-new-godel-prize-winner-tastes-great.html)

本博客宣布Eshan Chattopadhyay和David Zuckerman因其关于显式双源提取器和弹性函数的论文荣获2025年哥德尔奖。博客作者Bill和Lance分别强调了这项工作的不同方面。

Bill强调该论文在构造性Ramsey理论中的应用。他解释了经典的Ramsey数问题及其已知的界限，并指出Chattopadhyay和Zuckerman所取得的构造性下界改进。

Lance则侧重于该论文在伪随机性方面的意义。他认为从两个具有低最小熵的独立来源提取近乎完美的随机比特是其核心成就，并认为Ramsey应用只是一个次要的推论。他还吹嘘了他之前的一篇博文，该博文强调了这篇论文，并给它起了个巧妙的标题“提取Ramsey图”。

这篇文章以Bill和Lance之间有趣的争论为框架，Bill将该结果比作米勒淡啤“既不饱腹又味道好”，代表了Ramsey理论的应用和去随机化的成就。Lance则对Ramsey方面不屑一顾。

最后，Eshan Chattopadhyay（获奖者之一）评论了这篇文章，感谢博主并提供了相关论文的链接。

---

## 52. 小罗伯特·肯尼迪：卫生与公众服务部采取行动以重建公众对疫苗的信任

**原文标题**: RFK Jr.: HHS moves to restore public trust in vaccines

**原文链接**: [https://www.wsj.com/opinion/rfk-jr-hhs-moves-to-restore-public-trust-in-vaccines-45495112](https://www.wsj.com/opinion/rfk-jr-hhs-moves-to-restore-public-trust-in-vaccines-45495112)

无法访问文章链接。

---

## 53. Alex Chinneck 打造的波纹联排别墅外墙在伦敦广场就座

**原文标题**: A Rippling Townhouse Facade by Alex Chinneck Takes a Seat in a London Square

**原文链接**: [https://www.thisiscolossal.com/2025/05/alex-chinneck-a-week-at-the-knees/](https://www.thisiscolossal.com/2025/05/alex-chinneck-a-week-at-the-knees/)

英国艺术家亚历克斯·钦内克在伦敦查特豪斯广场揭幕了名为“屈膝一周”的全新公共雕塑，作为克勒肯维尔设计周的一部分。该作品的灵感源于他2013年的早期装置作品“从我的鼻尖到我的脚趾”，该作品以马盖特一栋滑动的联排别墅外墙为特色。“屈膝一周”将经典的乔治亚风格外墙重新想象成一个俏皮的拟人化结构。 нижние два этажа, по-видимому, перетекают через дорожку, создавая иллюзию здания, сидящего на коленях. 该雕塑由320米再生钢材和7000块砖砌而成，重达12吨，但厚度仅为15厘米，虽然体型庞大，但给人以优雅轻盈的感觉。钦内克与众多英国公司合作，采购并创作定制元素，包括钢梁、弧形窗户和砖块。该作品高五米，包括排水管和拱形前门两侧的灯等细节。该作品旨在与伦敦标志性的绿色广场和花园互动，邀请游客与一个独特的入口互动，该入口参考了周围环境的历史。该雕塑将展出至六月。

---

## 54. 与环保署合作保障暴露的水源人机界面安全

**原文标题**: Working with the EPA to Secure Exposed Water HMIs

**原文链接**: [https://censys.com/blog/turning-off-the-information-flow-working-with-the-epa-to-secure-hundreds-of-exposed-water-hmis](https://censys.com/blog/turning-off-the-information-flow-working-with-the-epa-to-secure-hundreds-of-exposed-water-hmis)

2024年10月，Censys研究人员发现近400个美国水务设施的人机界面(HMI)暴露于网络，通过TLS证书分析和截图提取识别。这些HMI使用相同的SCADA软件，存在于三个状态：已认证、只读和未认证。令人震惊的是，40个系统完全未认证，无需凭据即可完全控制。

Censys与EPA和软件供应商分享了这些发现，促成了一项协调的补救工作。九天内，24%的系统得到了保护，几周内增加到58%。截至2025年5月，只有不到6%的系统仍处于只读或未认证状态。

文章强调了HMI作为有价值目标的重要性，因为它们提供了关于关键基础设施的背景信息，这与通用的ICS协议暴露不同。最初供应商的反应平淡，但EPA的迅速行动，包括联系EPA区域机构和制造商，推动了补救。制造商还协助客户通过MFA和其他最佳实践来增强安全性。

Censys使用每月扫描验证缓解进展，通过跟踪TLS证书而不是仅仅依赖IP地址来解决DHCP IP地址更改问题。Censys、EPA和供应商之间迅速而有效的合作，为关键基础设施安全补救提供了一个积极的例子，强调了HMI保护的重要性，因为它易于访问并有可能被未授权控制。

---

## 55. 大语言模型很便宜

**原文标题**: LLMs are cheap

**原文链接**: [https://www.snellman.net/blog/archive/2025-06-02-llms-are-cheap/](https://www.snellman.net/blog/archive/2025-06-02-llms-are-cheap/)

本文认为，与普遍认知相反，运行大型语言模型（LLMs）现在相对便宜。作者认为这种误解源于人工智能热潮初期的高昂推理成本以及对“每百万token美元”定价模式的误解。

作者将LLMs的成本与网络搜索进行比较，网络搜索是一种用户无需直接付费的普遍服务。他们展示了Gemini、Bing和Brave等搜索引擎的API定价，然后根据Gemma、Qwen、Gemini和GPT等模型的token输出和每token价格估算LLM查询的成本。他们的计算表明，即使不考虑批量请求折扣或非高峰定价，LLMs通常也比搜索便宜。

作者解决了潜在的反对意见，例如LLM响应的长度、补贴的API定价以及构建搜索索引的成本。他们认为，API很可能是有利可图的，这得到了Deepseek发布的推理效率数据以及与观察到的定价相符的第一性原理分析的支持。他们还指出，OpenAI的亏损是由于未变现的用户，而不一定是高昂的推理成本。

作者强调，LLMs的低成本对人工智能的未来具有重要意义。这表明人工智能公司可以收回训练成本，并且可以通过广告来支持消费者使用。他们预测，真正的成本挑战将在于人工智能代理使用的后端服务，例如预订机票。作者探讨了涉及人工智能代理、服务提供商和数据提供商的潜在场景，并得出结论，LLMs本身的运行成本不会太高。

---

## 56. 研究人员重现古埃及蓝

**原文标题**: Researchers recreate ancient Egyptian blues

**原文链接**: [https://news.wsu.edu/press-release/2025/06/02/researchers-recreate-ancient-egyptian-blues/](https://news.wsu.edu/press-release/2025/06/02/researchers-recreate-ancient-egyptian-blues/)

华盛顿州立大学的研究人员重现了古埃及颜料——埃及蓝，这是世界上最古老的人工合成颜料，大约在5000年前被使用。通过试验不同的原材料、加热时间和冷却速率，该团队开发了12种不同的配方，为考古学家和文物保护科学家提供了关于这种颜料创造的见解。

这项发表在《NPJ文物科学》上的研究，强调了现代科学如何阐明古代物品的历史。埃及蓝是昂贵矿物的替代品，被用于绘制木材、石头和纸莎草画。对其制作工艺的了解在文艺复兴时期之后基本失传。

最近，由于其独特的光学、磁性和生物学特性，人们对它重新产生了兴趣。它能发出近红外光，可用于指纹识别或防伪墨水。研究人员用二氧化硅、铜、钙和碳酸钠创造了这种颜料，并将其加热到1000摄氏度。然后使用现代显微镜技术分析了得到的颜料，并将其与古埃及文物进行了比较。

该研究表明，埃及蓝的颜色和成分因其产地和质量而异。令人惊讶的是，最蓝的颜色只需要大约50%的蓝色成分，而且这种颜料并不均匀。重现的样品目前在卡内基自然历史博物馆展出。

---

## 57. Show HN: Glowstick – 在稳定版 Rust 中进行类型级别的张量形状推导

**原文标题**: Show HN: Glowstick – type level tensor shapes in stable rust

**原文链接**: [https://github.com/nicksenger/glowstick](https://github.com/nicksenger/glowstick)

Glowstick 是一个 Rust crate，它将类型级别的张量形状追踪引入到稳定的 Rust 中，旨在使张量操作更安全、更容易。它与像 candle 这样的框架一起工作，并提供张量形状的编译时检查，从而减少运行时错误。

主要功能包括将张量形状表达为类型，支持动态维度以实现渐进式类型，提供人类可读的（但仍在发展中）错误消息，以及使用 `debug_tensor!` 宏启用手动形状检查。该 crate 提供了各种张量操作，并通过涉及 `reshape`、`unsqueeze`、`squeeze`、`narrow`、`broadcast_add`、`transpose`、`conv2d` 和 `flatten` 的示例，展示了 `glowstick_candle` 集成。

虽然仍处于 pre-1.0 阶段，意味着会发生重大更改，但 Glowstick 计划支持所有 ONNX 操作。 该 crate 的 examples 目录展示了更复杂的使用方式以及与 candle 和 Burn 等 ML 框架的集成。其核心目标是通过利用类型系统来实现形状安全性和清晰性，从而改善在 Rust 中使用张量时的开发者体验。

---

## 58. Meta正在创建一个新的AI实验室以追求“超级智能”

**原文标题**: Meta Is Creating a New A.I. Lab to Pursue 'Superintelligence'

**原文链接**: [https://www.nytimes.com/2025/06/10/technology/meta-new-ai-lab-superintelligence.html](https://www.nytimes.com/2025/06/10/technology/meta-new-ai-lab-superintelligence.html)

Meta将成立新AI研究实验室，专注于实现超越人类智能的“超人工智能”，以保持在快速发展的科技领域中的竞争力。 在经历了内部斗争、员工离职和不成功的产品发布后，该公司正在重组其人工智能工作。

Meta已招募Scale AI的CEO Alexandr Wang加入新实验室，并考虑对Scale AI进行数十亿美元的投资，可能从该初创公司带来更多员工。 据报道，Meta还向OpenAI和Google等领先公司的人工智能研究人员提供了优厚的薪酬待遇，并成功吸引了一些人才。

在ChatGPT取得成功后，Meta的CEO 马克·扎克伯格已承诺投入巨额资金将Meta转型为人工智能强国，并将该技术整合到其所有产品中。 这一举动使Meta与微软（投资了OpenAI）和亚马逊（投资了Anthropic）等其他科技巨头一样，加入了争夺人工智能领域主导地位的竞赛，该领域被视为行业的未来。 其他例子包括谷歌授权Character.AI的技术。

---

## 59. 如何制作出一个优秀的语言原型？

**原文标题**: How do you prototype a nice language?

**原文链接**: [https://kevinlynagh.com/newsletter/2025_06_03_prototyping_a_language/](https://kevinlynagh.com/newsletter/2025_06_03_prototyping_a_language/)

这份简报探讨了原型化一种“好用”的codeCAD语言所面临的挑战，强调关注用户体验（“软件舒适感”），而非炫酷的演示。作者的目标是创造一种感觉即时响应、稳定且使用舒适的语言，但在构建多少功能才能正确评估该语言是否达到这种感觉方面遇到了困难，尤其是在双向编辑方面。

双向编辑涉及将代码更改与图形用户界面同步，对源代码重写、编辑器集成（例如，Emacs）以及维护注释和空格提出了重大挑战。正确实现这一点需要大量的努力，提出了验证核心理念需要多少复杂性的问题。

作者讨论了除了基本教程之外，缺乏关于复杂语言语义的更精细细节的资源。Nystrom的《Crafting Interpreters》被认为是很有用的资源，以及用于解析和数据处理的Clojure工具。作者曾考虑过Tree-sitter的性能和生态系统优势，但目前选择坚持使用熟悉的工具。他们正在研究语言和编辑器工具集成统一方法，并引用Gleam、Lady Deirdre和Roslyn作为例子。

这份简报还包括各种链接，指向其他文章和资源，涵盖了诸如语言设计、用户界面设计、调试工具，甚至无壳面包烘焙等主题。总体主题围绕着构建一种以用户体验为中心的语言的迭代过程，在功能与有凝聚力且令人愉悦的开发环境之间取得平衡。

---

## 60. 拉斯维加斯拥抱简单的气候解决方案：多种树

**原文标题**: Las Vegas is embracing a simple climate solution: More trees

**原文链接**: [https://www.npr.org/2025/06/09/nx-s1-5340363/las-vegas-climate-change-solution-trees](https://www.npr.org/2025/06/09/nx-s1-5340363/las-vegas-climate-change-solution-trees)

拉斯维加斯正通过种植更多树木来应对不断上升的气温（去年夏天，高温导致超过500人死亡），尤其是在“城市热岛”地区——这些地区通常是树木覆盖率较低的低收入社区，气温明显高于其他地区。一项2022年的研究发现，这些区域的温度可能比城市其他区域高出11度。

该市计划到2050年种植6万棵树，这意味着每年需要种植大约2000棵树。城市林务员布拉德·达塞勒正专注于耐旱、能提供阴凉的树种。

由Ariel Choinard领导的南内华达州热适应力实验室强调了影响低收入社区的“阴凉差异”，迫使居民在给房屋降温和负担其他必需品之间做出选择。树木可以显著降低周围温度，提供急需的缓解。

在合适的位置种植合适的树木至关重要。除了市政府的努力外，学校也在通过创建园艺俱乐部来教育孩子们关于环境保护的知识。该项目的希望是，教育孩子们关于环境保护的知识将产生涓滴效应，并帮助地球。

---

## 61. 丹麦：数字化大臣希望逐步淘汰微软

**原文标题**: Denmark: Minister for Digitalization wants to phase out Microsoft

**原文链接**: [https://nordjyske.dk/nyheder/politik/digitaliseringsminister-vil-udfase-microsoft-i-sit-eget-ministerium/5616096](https://nordjyske.dk/nyheder/politik/digitaliseringsminister-vil-udfase-microsoft-i-sit-eget-ministerium/5616096)

丹麦数字化大臣计划减少对微软程序的依赖，追求数字主权。下月起，该部门一半员工将从微软Office切换至Libre Office，目标是2025年秋季完成全面过渡。大臣Caroline Stage希望以身作则，测试此切换的可行性。

这项举措符合Stage旨在降低丹麦对大型科技公司（尤其是总部位于美国的科技公司）依赖的更广泛战略。此举的动因是对与美国相关的数据保护和数字基础设施的担忧，当前全球局势加剧了这一辩论。

此次过渡与即将启动的国家数字化战略相吻合，该战略优先考虑与国家、地区和市政当局合作的“数字主权”。

文章指出，团结名单党（Enhedslisten）和替代党（Alternativet）等政党也表达了类似的愿望，希望丹麦摆脱美国科技巨头，倡导更大的数字独立性。团结名单党的Rosa Lund呼吁切断联系，而替代党的Helene Brydensholt敦促政府制定实现数字主权的计划。Stage表示，如果Libre Office的切换出现问题，他们愿意在短期内恢复使用微软Office。

---

## 62. Salesforce/Heroku宕机8小时

**原文标题**: Salesforce/Heroku down for 8 hours

**原文链接**: [https://status.salesforce.com/generalmessages/10001540](https://status.salesforce.com/generalmessages/10001540)

根据提供的标题和内容，现有信息似乎不完整，主要指向服务中断。以下是根据我们能推断出的摘要：

**摘要：**

Salesforce和Heroku经历了重大中断，持续约8小时。信息来源于“信任状态”页面，表明问题影响了Salesforce的信任度和服务的可用性。提供的内容表明需要JavaScript才能访问完整的状态报告，阻碍了对中断原因和范围的全面理解。

---

## 63. 词汇宝典：一本教你大型语言模型术语的奇幻故事

**原文标题**: The Lexiconia Codex: A fantasy story that teaches you LLM buzzwords

**原文链接**: [https://medium.com/@isranimohit/the-lexiconia-codex-a-fantasy-story-that-teaches-you-every-llm-buzzword-3b7f6eb23da9](https://medium.com/@isranimohit/the-lexiconia-codex-a-fantasy-story-that-teaches-you-every-llm-buzzword-3b7f6eb23da9)

《词典法典》是一部奇幻故事，通过隐喻来解释与大型语言模型（LLMs）相关的关键流行语和概念。故事发生在词典世界，那里的抄写员利用神秘知识（LLMs）来生成文本和见解。

**解释的关键概念：**

*   **LLMs & Transformer架构：** 变形金刚塔的抄写员使用注意力之镜（自注意力）通过自回归生成令牌轨迹（单词序列）。
*   **训练LLMs：** 微调神庙详细介绍了预训练（从大量文本中学习）、微调（在特定数据集上训练）和RLHF（带人类反馈的强化学习），以提高抄写员的能力。LoRA（低秩适应）被引入作为一种有效的模型修改方法。
*   **检索增强生成（RAG）：** 检索行会会将卷轴索引到记忆金库中的向量水晶（嵌入）。当被提示时，他们会检索相关卷轴以增强抄写员的回复。
*   **提示工程：** 提示工匠塔专注于使用零样本、少样本、思维链和ReAct等技术来制作有效的提示，同时解决诸如提示注入之类的安全问题。
*   **LLM代理：** 代理机构训练抄写员（代理）使用LangChain等框架来计划任务、使用工具（API）并执行行动。
*   **LLM内部机制：** 内部学院展示了混合专家（MoE）、旋转位置嵌入（RoPE）、闪存注意力和稀疏注意力等技术，这些技术用于优化LLM的速度和效率。

该故事提供了一种隐喻且引人入胜的方式来理解现代LLMs背后的基本原理和技术。

---

## 64. 暴力破解任何谷歌用户的电话号码

**原文标题**: Bruteforcing the phone number of any Google user

**原文链接**: [https://brutecat.com/articles/leaking-google-phones](https://brutecat.com/articles/leaking-google-phones)

本文详细介绍了一个漏洞，该漏洞允许通过利用一个无 JavaScript 的用户名恢复表单，对 Google 用户的电话号码进行暴力破解。作者发现该表单没有正确地限制请求速率，从而允许枚举与特定显示名称关联的电话号码。

最初，基于 IP 的速率限制和验证码是障碍。然而，作者通过使用 IPv6 地址轮换，以及更有效地，通过将 `js_disabled` 参数替换为从启用 JavaScript 的表单获得的有效 BotGuard 令牌，绕过了这些限制。这允许无限请求，而不会触发安全措施。

暴力破解方法是通过迭代与已知显示名称（名字和姓氏）以及国家代码相关的可能电话号码来实现的，国家代码通过分析密码恢复流程中提供的掩码电话号码格式来确定。最初，找到受害者的显示名称具有挑战性，但作者发现了一种使用 Looker Studio 泄露此信息的方法。

作者创建了一个程序 (`gpb`) 来自动化该过程，利用 libphonenumbers 进行号码验证，并利用 Go 脚本生成 BotGuard 令牌。借助一个基本的服务器，该过程可以在几分钟内显示一个电话号码，具体取决于要暴力破解的位数。

该漏洞已报告给 Google，最初由于认为可利用性较低而导致奖励较低。经过申诉后，奖励有所增加，并且 Google 实施了缓解措施，最终弃用了存在漏洞的无 JS 用户名恢复表单。

---

## 65. Show HN: Somo – 一款更友好的 netstat 替代方案

**原文标题**: Show HN: Somo – a human friendly alternative to netstat

**原文链接**: [https://github.com/theopfr/somo](https://github.com/theopfr/somo)

Somo：Linux下监控套接字和端口的友好型netstat替代方案。它提供了一个具有视觉吸引力的表格界面，具备过滤功能和交互式进程终止能力。

主要功能包括：

*   **可读性输出：** 以清晰的表格格式呈现网络信息。
*   **过滤：** 允许用户按协议（TCP/UDP）、本地端口、远程端口、IP地址、程序名称、PID、开放/监听连接和IPv6排除来过滤结果。
*   **进程终止：** 允许直接从Somo界面交互式终止进程。
*   **便捷语法：** 提供更短的命令选项，例如`somo -l`，而不是`netstat -tulpn`。

可以通过Debian系统的`.deb`包或通过`cargo`（Rust包管理器）进行安装。建议在使用`cargo`安装时创建符号链接，以便使用`sudo`执行，从而获得完整的系统访问权限。

本文还包括使用示例，演示了过滤和进程终止功能。

---

## 66. 窥视秀：全球4万个物联网摄像头向任何有浏览器的人直播秘密

**原文标题**: Peep show: 40K IoT cameras worldwide stream secrets to anyone with a browser

**原文链接**: [https://www.theregister.com/2025/06/10/40000_iot_cameras_exposed/](https://www.theregister.com/2025/06/10/40000_iot_cameras_exposed/)

Bitsight的安全研究人员发现全球约有4万个未受保护的联网摄像头，暴露了来自敏感地点（如数据中心、医疗机构、工厂、酒店、健身房、零售商店和住宅区）的实时视频流。美国是受影响最严重的地区，约有14000个摄像头暴露。

访问这些视频流的便利性引发了人们对间谍活动、商业机密盗窃、国家安全漏洞以及潜在犯罪活动（如抢劫和跟踪）的严重担忧。Bitsight强调，许多摄像头缺乏基本的安全措施，可以通过简单的Web浏览器访问，利用HTTP和RTSP技术。基于HTTP的摄像头在暴露的视频流中更为普遍。

该研究支持美国国土安全部（DHS）的一份公告，该公告警告称，中国可能会利用暴露的摄像头进行间谍活动，尤其是那些在中国制造且缺乏默认安全控制的摄像头。美国国土安全部担心，位于关键基础设施中的这些摄像头可能会被利用来窃取数据、抑制警报或禁用安全机制。

Bitsight还发现，网络犯罪分子在网上论坛分享暴露摄像头的IP地址，表明他们有兴趣利用这些视频流进行跟踪、勒索和其他恶意目的。该报告强调，需要提高对联网摄像头的安全意识，并改进安全措施，以防止未经授权的访问和潜在的滥用。

---

## 67. 调试弹性云无服务器的Azure网络

**原文标题**: Debugging Azure Networking for Elastic Cloud Serverless

**原文链接**: [https://www.elastic.co/observability-labs/blog/debugging-aks-packet-loss](https://www.elastic.co/observability-labs/blog/debugging-aks-packet-loss)

本文详细介绍了Elastic SRE团队如何调试在Azure Kubernetes Service (AKS) 上运行的Elastic Cloud Serverless的性能问题。他们观察到吞吐量不稳定和数据包丢失，影响了Elasticsearch的索引速率。调查显示，SR-IOV接口上的RX环形缓冲区溢出和内核输入队列饱和是主要原因。

该团队使用USE方法和自定义的Elastic Observability仪表板来识别AKS节点上的数据包丢失。他们发现加速网络 (SR-IOV) 绕过了虚拟机监控程序，使VM直接负责处理NIC中断。快速的100 Gb/s接口可能会传递微突发，从而压垮小缓冲区。

为了解决这个问题，他们使用通过特权DaemonSet部署的`udev`规则，将NIC的RX环形缓冲区大小从1024增加到8192。这一改变显著减少了数据包丢失并提高了索引吞吐量。

尽管有所改善，但Elasticsearch Pod使用的物理接口的TX侧和逻辑接口上仍然存在一些数据包丢失。丢弃计数器表明数据包是被内核或网络接口故意丢弃的，需要进一步调查与内核网络堆栈相关的问题。

---

## 68. Salesforce Services 身份验证失败

**原文标题**: Authentication fails for Salesforce Services

**原文链接**: [https://status.salesforce.com/generalmessages/10001540](https://status.salesforce.com/generalmessages/10001540)

Salesforce服务身份验证失败，提示“您需要启用JavaScript才能运行此应用”，表明身份验证依赖JavaScript。由于用户浏览器禁用了JavaScript或JavaScript未正确运行，导致身份验证失败。**本质是，Salesforce身份验证失败是因为JavaScript在用户浏览器中被禁用或无法正常运行。** 用户可能需要在浏览器设置中启用JavaScript，或排除阻止JavaScript运行的故障。

---

## 69. Spectre.Console – 创建漂亮的控制台应用程序

**原文标题**: Spectre.Console – create beautiful console applications

**原文链接**: [https://spectreconsole.net/](https://spectreconsole.net/)

Spectre.Console 是一个 .NET 库，旨在简化创建具有视觉吸引力且功能强大的控制台应用程序的过程。它提供了一种受 Rich 启发的标记语言，用于带有颜色和格式选项的样式文本输出，并支持各种终端颜色深度。

其主要功能包括渲染复杂小部件（如表格、树和 ASCII 图像）、显示长时间任务的进度条和状态更新，以及通过强类型文本或选择控件提示用户输入。它还为 .NET 异常提供带有颜色编码主题的自定义格式。

Spectre.Console 包括 Spectre.Console.Cli（用于构建复杂的命令行界面）和 Spectre.Console.Testing（提供广泛的测试支持，反映了该库自身严格的测试过程）。单元测试指南和示例代码也很容易获得。

---

## 70. 寻找肖恩·蒙德兹 (2019)

**原文标题**: Finding Shawn Mendes (2019)

**原文链接**: [https://ericneyman.wordpress.com/2019/11/26/finding-shawn-mendes/](https://ericneyman.wordpress.com/2019/11/26/finding-shawn-mendes/)

埃里克·内曼的文章《寻找肖恩·蒙德兹（2019）》是一篇幽默而详尽的尝试，通过分析肖恩·蒙德兹的歌曲《迷失在日本》的歌词，来确定他对日本和俄罗斯之间关于千岛群岛领土争端的立场。

内曼首先强调了名人在政治领域的影响力。然后他提出了问题：肖恩·蒙德兹对千岛群岛争端的看法是什么？

核心论点围绕着蒙德兹声称自己“距离日本几百英里”的歌词展开。内曼仔细排除了各种地理可能性，例如韩国、中国，甚至包括一个偏远的日本岛屿（台湾附近的石垣岛），理由是时区差异、飞行距离以及蒙德兹所谓的蚊虫过敏。

他最终确定了俄罗斯远东地区，特别是萨哈林岛以及蒙德兹飞往择捉岛（争议中的千岛群岛的一部分）的可能性。通过分析航班时刻表，他发现了一班从南萨哈林斯克飞往择捉岛的航班，与歌曲的歌词相符（一趟夜间航班，蒙德兹鼓励他的朋友保持清醒）。他甚至还包括了一张伪造的蒙德兹在择捉岛机场的照片。

内曼得出结论，通过歌唱飞往“日本”，同时暗示自己靠近择捉岛，蒙德兹实际上是在支持日本对争议岛屿的主张。最后，作者宣布了他自己对该问题观点的转变，现在站在日本一边，受到了蒙德兹假定立场的影响。整篇文章都是一个对过度分析和荒谬推论的戏谑练习。

---

## 71. 辫子般的群舞（2009）

**原文标题**: Maypole Dance of Braid Like Groups (2009)

**原文链接**: [https://divisbyzero.com/2009/05/04/the-maypole-braid-group/](https://divisbyzero.com/2009/05/04/the-maypole-braid-group/)

本文探讨了五月柱舞背后的数学结构，并将其与辫群理论联系起来。作者刚教授完纽结理论，便观察到五月柱舞中产生的丝带图案与（Artin）辫群之间的联系。

作者首先解释了辫群的基本知识，包括生成元（sigma_i和sigma_i^-1代表相邻股线的交叉）、群运算（连接）以及定义关系：远距离交换律（生成元如果足够远则交换）和辫子关系（与Reidemeister移动相关）。

文章随后将五月柱舞视为辫群的一种变体，其中股线连接到两个圆（五月柱的顶部和底部），形成一个圆柱辫。作者提出定义一个“五月柱辫群”，最初尝试通过考虑与第一股线相邻的第*n*股线来推广标准辫群。

然而，作者证明这种概括不足以生成所有可能的五月柱辫。为了弥补这一点，他们引入了一个新的生成元，表示为`rho`，它代表一种旋转，其中每股线逆时针方向移动一个位置。也可以进行相应的顺时针运动。他们演示了`rho`及其逆如何生成以前无法实现的辫子。

最后，文章提出了一个使用生成元（sigma_i和rho）和关系的五月柱辫群的定义，包括为考虑圆形邻接而修改的原始辫群关系，以及描述`rho`与其他生成元之间相互作用的新“旋转关系”。作者最后以五月节快乐的问候语结束，并为读者留下了一些练习。

---

## 72. 高频内核与缓存的潜力与局限 (2024)

**原文标题**: Potential and Limitation of High-Frequency Cores and Caches (2024)

**原文链接**: [https://arch.cs.ucdavis.edu/simulation/2024/08/06/potentiallimitationhighfreqcorescaches.html](https://arch.cs.ucdavis.edu/simulation/2024/08/06/potentiallimitationhighfreqcorescaches.html)

这篇2024年的论文《高频核心与缓存的潜力和局限性》探讨了低温半导体计算和超导电子学作为传统半导体替代方案，实现高性能、低功耗计算的可行性。该研究探讨了传统半导体所面临的局限性，例如在高温度下增加的漏电流和降低的性能。

该论文研究了低温半导体（在-150°C以下运行）和超导电子学（在10K以下运行），它们分别具有降低漏电流和电阻的优势。作者使用gem5模拟器对在高频率下运行的顺序和乱序核心进行建模，利用这些新兴技术的潜力。他们使用真实世界的应用程序工作负载（包括NPB、SPEC CPU2006和GAPBS）评估这些模拟核心的性能。

结果突出了通过这些技术可以实现的潜在加速，但也揭示了缓存带宽带来的局限性。该研究为低温和超导技术相关的性能影响和设计权衡提供了宝贵的见解，旨在为未来使用gem5在该领域的研究提供信息。这篇论文有助于理解这些先进计算范式的潜力和约束。

---

## 73. MDMA治疗自恋？专访精神分析师和精神科医生艾莉克莎·阿尔伯特，5个问题

**原文标题**: MDMA for narcissism? 5 Questions for psychoanalyst and psychiatrist Alexa Albert

**原文链接**: [https://themicrodose.substack.com/p/mdma-for-narcissism-5-questions-for](https://themicrodose.substack.com/p/mdma-for-narcissism-5-questions-for)

好的，这是一篇基于标题《MDMA治疗自恋？精神分析师和精神科医生Alexa Albert的5个问题》和可能内容（假设其是关于MDMA潜在治疗应用）的文章摘要：

该文章可能探讨了MDMA辅助心理疗法在治疗自恋型人格障碍 (NPD) 中的潜在应用。文章采访了精神分析师和精神科医生 Alexa Albert，她可能讨论了这种新型治疗方法的各个方面。

基于对MDMA和NPD的普遍理解，文章可能涉及以下关键点：

*   **治疗NPD的挑战：** 由于个体缺乏洞察力、防御性和自大，NPD的治疗非常困难，这些常常阻碍治疗联盟的形成。
*   **MDMA可能如何提供帮助：** MDMA可以促进同情、开放和连接感，这可能打破这些防御，使NPD患者更有效地参与治疗。
*   **Albert讨论的具体问题：** 访谈可能集中在以下主题：哪些类型的NPD表现最适合MDMA辅助治疗，如何管理潜在的风险和挑战（例如，对治疗师的理想化、脆弱性），以及所涉及的伦理考量。
*   **作用机制：** 文章可能提到MDMA如何通过允许个体在安全、支持性的治疗环境中体验困难的情绪和关系，从而改变与NPD相关的神经通路和思维模式。
*   **未来研究：** 文章可能触及需要进行严格的临床试验，以研究MDMA辅助治疗NPD的疗效和安全性，并制定具体的治疗方案。

本质上，该文章探索了一种潜在的突破性方法（尽管仍然是高度实验性的）来治疗一种出了名的难治的人格障碍，通过利用MDMA增强同理心和促进在结构化心理治疗背景下的情感处理的能力。

---

## 74. 二次方资助为何并非最优

**原文标题**: Why quadratic funding is not optimal

**原文链接**: [https://jonathanwarden.com/quadratic-funding-is-not-optimal/](https://jonathanwarden.com/quadratic-funding-is-not-optimal/)

本文认为，二次方资助（QF）虽然在理论上对于在特定假设下资助公共物品是最佳的，但在实践中往往达不到理想效果，因为这些假设在现实世界中很少成立。

该论点的核心在于一系列 QF 要发挥最佳作用所必需的假设：财富平等、免费补贴、自私的贡献者、均衡发现、充足的预算、收益递减、完美知识和独立主体。文章随后详细阐述了每个假设，解释了为什么它们不太可能得到满足，并详细描述了未能满足时的负面后果。

例如，财富不平等会将资金导向富人青睐的项目，即使这些项目惠及的人较少。“免费”补贴的假设忽略了贡献者通过税收承担的实际成本，这可能会将财富从较贫穷的公民转移到较富裕的公民。此外，利他主义的贡献者可能导致对项目的过度资助，超出社会最佳水平。

文章强调了实现均衡发现的困难，因为贡献者缺乏关于他人贡献的完整信息。预算不足和固定价格的项目可能会产生多个不可预测的均衡。对项目的不完全了解也会导致资金偏向高知名度（但不一定是高价值）的倡议。最后，缺乏真正独立的代理人会导致勾结和欺诈。

作者总结说，除非至少满足其中一些假设，否则可能存在比纯 QF 更好的公共物品资助机制，尤其是在没有采取措施防止勾结的情况下。虽然存在抗勾结的变体，但它们牺牲了 QF 的理论最佳性。还需要更多的研究来解决其他被违反的假设。

---

## 75. Show HN: 我正在开发一个可以媲美 "Everything" 的应用

**原文标题**: Show HN: I am making an app to rival "Everything"

**原文链接**: [https://drimiteros.github.io/Da-Deep-Search-Website/](https://drimiteros.github.io/Da-Deep-Search-Website/)

Da Deep Search：一款极简高性能的Windows文件浏览工具，旨在成为比Windows搜索更快、集成度更高的替代方案。它拥有便携性（无需安装）、无需管理员权限、自动更新、广泛的文件系统兼容性（NTFS、FAT32）、智能搜索功能，以及用C++20构建的线程化超快速搜索引擎等特性。

该应用程序提供文件名、大小和路径等文件信息，并提供文件执行和快速操作。使用方法简单：Ctrl + 空格键切换窗口，用户选择要扫描的驱动器，然后输入即可立即查找文件。2.1_2及以下版本的源代码是开源的，鼓励修改和贡献。开发者鼓励用户下载、探索并捐赠以支持该项目。

---

## 76. 软件即承诺

**原文标题**: Software is about promises

**原文链接**: [https://www.bramadams.dev/software-is-about-promises/](https://www.bramadams.dev/software-is-about-promises/)

本文认为软件开发从根本上来说就是向用户做出并遵守承诺。软件既抽象又真实，这导致一个悖论：虽然软件易于扩展，但开发却受到时间和创造力的瓶颈制约。这种紧张关系需要向用户做出清晰且可测试的承诺，在雄心壮志与现实资源限制之间取得平衡。

作者用个人图书馆科学软件“Your Commonbase”(YCB)的案例研究来说明这一概念。YCB专注于四个功能：存储、搜索、综合和分享。对于YCB Beta版，针对每个功能都做出了具体承诺，概述了具体特性和平台支持（Chrome、iOS和配套应用程序）。

*   **存储：** 从Chrome和iOS捕获文本、图像和URL，并支持图像标题。
*   **搜索：** 语义搜索和滚动，具有“边输入边搜索”功能。
*   **综合：** 跨平台评论功能，用于连接条目。
*   **分享：** 截图和URL的基本分享（承认尚不完善）。

作者强调了资源分配的重要性，优先考虑Beta版的基础工作——存储和综合。这些承诺旨在让用户进行测试，从而指导未来的开发。结论再次强调了承诺在保护开发者、用户和软件完整性方面的重要性。最后，作者邀请读者体验YCB的演示并加入等候名单。

---

## 77. 临时电脑博物馆

**原文标题**: The Interim Computer Museum

**原文链接**: [https://icm.museum/](https://icm.museum/)

临时电脑博物馆（ICM）是一家致力于保存和分享36位计算历史的非营利组织。它提供互动式、动手操作的展品，利用经过现代技术增强的古董硬件，连接过去与现在，让参观者探索计算的演变。

该博物馆与SDF Public Access UNIX System, Inc.合作运营，并严重依赖会员支持其使命，包括社区活动和历史文物的保存。博物馆鼓励参观者通过捐赠或成为会员来做出贡献。网站提示感兴趣的人士“访问”以获取联系方式和预订信息。

---

## 78. CoverDrop：新闻阅读器应用的安全消息系统

**原文标题**: CoverDrop: A secure messaging system for newsreader apps

**原文链接**: [https://github.com/guardian/coverdrop](https://github.com/guardian/coverdrop)

CoverDrop：为新闻机构移动应用设计的安全消息系统，可在保护消息来源匿名性的同时，实现记者与消息来源之间的保密通讯。它通过在新闻应用的正常运作中嵌入安全消息功能来实现这一点。所有应用实例，无论是否用于安全通讯，都会定期与机构服务器交换加密的“掩护消息”。

当消息来源发送消息时，该消息将使用记者的公钥加密，并伪装成例行的掩护消息，使网络观察者无法区分。消息会被附加到 Kinesis 流中，并由新闻机构的安全服务器检索。记者通过“死信箱”访问消息，其中可能包含真实消息和虚假消息的混合。记者的回复也以类似方式处理。

至关重要的是，用户应用上的消息存储库设计成看起来完全相同，无论它们是否包含真实消息，从而确保没有安全通讯的法证证据。

该系统包括移动应用内的模块、基于云的 API、CoverNode（安全位置中的服务）和记者桌面应用程序。其设计和架构详见一份白皮书。项目的实现分为客户端和服务端，并设有管理工具、Android/iOS 库、API、云基础设施资源等的存储库。

项目欢迎安全反馈，特别是关于消息保密性、网络匿名性和可信推诿方面的反馈，并提供安全报告的联系电子邮件。CoverDrop 包含加密软件，用户应遵守当地有关其使用的法规。该项目根据 Apache License 2.0 获得许可。

---

## 79. 我第一次尝试iOS应用开发

**原文标题**: My first attempt at iOS app development

**原文链接**: [https://mgx.me/my-first-attempt-at-ios-app-development](https://mgx.me/my-first-attempt-at-ios-app-development)

本文记录了作者首次尝试iOS应用开发的经历，其动力源于对现有照片管理应用的不满以及好奇心。作者在没有任何Swift经验的情况下，利用Xcode和Cursor等人工智能工具（用于代码生成和问题解决），在三天内构建了一个功能完备的应用程序。

该应用专注于照片管理、重复查找和滑动删除，计划采用一次性购买的定价模式，价格为2.99美元，拒绝了市场上常见的订阅模式。作者批评了一些照片工具应用开发者过度定价和营销手段。

作者强调了使用人工智能进行编码的好处，尤其是在快速迭代、错误诊断和理解iOS设计模式方面，同时也承认了其局限性，尤其是在涉及安全敏感的代码时。他们还强调，与多年前相比，如今的iOS开发更加容易上手，并引用了使用原生库和API的便利性。他们对iOS“开箱即用”的功能之多感到惊讶。

该项目面临一些挑战，包括在检测中国境内位置时，Apple的CLGeocoder出现问题，需要进行变通处理。总而言之，作者即将完成项目，专注于完善用户体验，并正在考虑加入Apple开发者计划。他们对应用程序的性能印象深刻，整体体验出乎意料地积极。

---

## 80. 潘坚德朗：为突破希特勒大西洋壁垒而建造的“巨型烟花”

**原文标题**: Panjandrum: The ‘giant firework’ built to break Hitler's Atlantic Wall

**原文链接**: [https://www.bbc.com/future/article/20250603-the-giant-firework-built-to-break-hitlers-atlantic-wall](https://www.bbc.com/future/article/20250603-the-giant-firework-built-to-break-hitlers-atlantic-wall)

本文详细介绍了“潘贾德鲁姆”，一种由英国在二战期间开发的、奇特且最终失败的武器，旨在突破希特勒的大西洋壁垒。“潘贾德鲁姆”由工程师内维尔·舒特·挪威（后来成为著名小说家）构思，本质上是一个巨大的火箭驱动的烟花轮，旨在向混凝土防御工事运送一吨重的炸药。

本文概述了盟军在突破戒备森严的港口和海滩时面临的问题，促使杂项武器发展局的“能工巧匠”们探索非常规解决方案。“潘贾德鲁姆”凭借其由火箭驱动的两个巨大轮子，旨在克服障碍并运送大量的爆炸性载荷。

尽管该项目背后充满热情和独创性，“潘贾德鲁姆”在测试过程中一直受到不稳定性和不可靠性的困扰。火箭经常脱落，导致机器疯狂地偏离航向。公开演示暴露了该项目的秘密，并且该武器不可预测的行为导致了险些发生的灾难。

最终，“潘贾德鲁姆”在D日登陆前因不切实际而被放弃。尽管是一次失败，但本文指出，“潘贾德鲁姆”的无人武器运送炸药的概念预示了现代无人机战争。本文还提到，经过改装的坦克“趣味坦克”在D日突破德国防线方面证明更为有效。战后，内维尔·舒特专注于他的写作事业。 近年来，人们已经尝试重建“潘贾德鲁姆”，主要用于娱乐和演示目的。

---

## 81. 新闻网站正被谷歌新人工智能工具碾压

**原文标题**: News Sites Are Getting Crushed by Google's New AI Tools

**原文链接**: [https://www.wsj.com/tech/ai/google-ai-news-publishers-7e687141](https://www.wsj.com/tech/ai/google-ai-news-publishers-7e687141)

无法访问文章链接。

---

## 82. 2025年的编译器探索器如何运作

**原文标题**: How Compiler Explorer Works in 2025

**原文链接**: [https://xania.org/202506/how-compiler-explorer-works](https://xania.org/202506/how-compiler-explorer-works)

Compiler Explorer：每年处理9200万次编译，使用户在Monaco编辑器中输入代码，经CloudFront和负载均衡器发送到特定服务器集群。服务器对请求进行排队，nsjail（一个轻量级进程隔离工具）创建一个沙箱来运行编译器。过滤后的结果以JSON格式返回给浏览器。

安全是首要考虑因素，通过使用nsjail解决，它利用Linux命名空间和资源限制来防止攻击。该系统使用Python和shell脚本管理超过4TB的编译器集合，确保旧版本编译器可用于历史目的。Squashfs镜像用于缓解与网络文件系统相关的延迟问题。

Compiler Explorer每天晚上使用GitHub Actions构建新的编译器，包括主干和实验性分支。它支持包括Windows、ARM和GPU实例在内的各种平台，主要在AWS的us-east-1区域运行。该系统使用Grafana、Prometheus、Loki和CloudWatch进行监控。

通过竞价实例和缓存来实现成本管理。该项目由Patreon、GitHub赞助者和商业赞助商支持。未来计划包括AI解释工具、用户帐户、RISC-V架构支持和CPU性能分析可视化。配置管理、多集群支持、服务发现和部署流程仍然面临挑战。该项目严重依赖于核心团队、社区英雄和编译器维护者的贡献。

---

## 83. FSE会见FBI

**原文标题**: FSE meets the FBI

**原文链接**: [https://blog.freespeechextremist.com/blog/fse-vs-fbi.html](https://blog.freespeechextremist.com/blog/fse-vs-fbi.html)

皮特的博客文章“FSE遭遇FBI”讲述了一个离奇事件，涉及FSE（一个联邦宇宙实例）、爬虫、FBI和数据投毒。 根本原因是FSE上长期存在恋童癖者，由于潜在的执法审查和儿童色情制品突袭，这对平台构成了生存威胁。 皮特试图禁止他们并发布他们的IP地址和其他信息，但这没有效果。

FBI正在从社交媒体（包括联邦宇宙实例）抓取数据，以查找关键词。 这些数据，连同情感分析和其他初步分析，按主题组织，并由FBI探员通过内部界面使用。

这篇文章随后深入探讨了实例管理员处理不良活动的技术建议。 它强调了理解日志文件、诊断工具和数据分析对于识别和解决诸如机器人、扫描器和有针对性的攻击等威胁的重要性。 文章提倡学习awk、grep、dig、whois、traceroute、tcpdump和iftop等工具，用于实时日志分析和网络探索。 它还强调了数值分析对于识别服务器流量异常的价值。 这篇文章提供了一个使用这些工具进行服务器管理的“速成课程”，强调了诊断和理解服务器问题的能力对于成功运行实例至关重要。

---

## 84. 希克苏鲁伯小行星撞击与大规模灭绝

**原文标题**: The Chicxulub Asteroid Impact and Mass Extinction

**原文链接**: [https://www.science.org/doi/10.1126/science.1177265](https://www.science.org/doi/10.1126/science.1177265)

我无法访问该文章链接。

---

## 85. 关于Twitter/X新加密消息功能的一点补充

**原文标题**: A bit more on Twitter/X's new encrypted messaging

**原文链接**: [https://blog.cryptographyengineering.com/2025/06/09/a-bit-more-on-twitter-xs-new-encrypted-messaging/](https://blog.cryptographyengineering.com/2025/06/09/a-bit-more-on-twitter-xs-new-encrypted-messaging/)

本文分析了Twitter/X新加密消息协议XChat的安全性，重点关注其密钥存储机制Juicebox。文章指出，XChat缺乏前向保密性，并使用Juicebox（一种旨在加强密码并防止暴力破解攻击的协议）将用户私钥存储在X的服务器上。

Juicebox将密钥分片到多个服务器（“领域”）上，并限制密码猜测尝试次数。作者认为，XChat的安全性取决于X是否使用硬件安全模块（HSM）来保护这些领域，以及这些领域是否由独立实体运营。如果X在没有HSM的情况下，在软件中控制所有领域，正如作者所怀疑的那样，X有可能访问用户密钥并解密消息。X工程主管最近声称正在使用HSM，但由于缺乏可验证的证据或已发布的安全仪式，这种说法受到了质疑。

作者深入研究了Juicebox协议，解释了它如何使用阈值不经意伪随机函数（t-OPRF）将弱密码转换为强大的加密密钥。理想情况下，Juicebox会将信任分配给多个组织和/或使用HSM。然而，作者得出结论，除非X提供HSM使用情况和Juicebox领域独立运营的可验证证据，否则用户应该假设他们的解密密钥容易被X访问。

---

## 86. 我用了人工智能卡路里计数App，结果比预期的还要糟糕

**原文标题**: I used AI-powered calorie counting apps, and they were even worse than expected

**原文链接**: [https://lifehacker.com/health/ai-powered-calorie-counting-apps-worse-than-expected](https://lifehacker.com/health/ai-powered-calorie-counting-apps-worse-than-expected)

本文批评了 Cal AI、SnapCalorie 和 Calorie Mama 等人工智能卡路里计数应用程序，认为它们未能兑现准确高效卡路里追踪的承诺。作者具有卡路里计数背景，发现这些应用程序持续错误识别食材并错误估计份量，导致卡路里计数经常出现严重偏差。

作者使用简单和复杂的膳食测试了这些应用程序，突出了将苹果识别为印度咖喱鸡块和沙拉的卡路里被低估数百卡路里的情况。虽然像 SnapCalorie 这样的应用程序提供手动纠正错误的功能，但这抵消了人工智能本应带来的节省时间的好处。Calorie Mama 被认为特别没用，需要手动输入所有食物项目和份量，使得人工智能方面毫无意义。

作者认为，核心问题在于这些应用程序依赖二维图像来估计三维体积。此外，作者还对用户盲目信任不准确的估计表示担忧，这可能对体重管理和整体健康有害。

文章最后质疑了精确卡路里计数本身的价值，并建议直觉饮食和注重均衡营养对于许多人来说是更健康、更可持续的方法。最终，作者发现人工智能卡路里计数应用程序是浪费时间，并且不如使用食物秤和数据库的传统方法准确。他们建议倾听身体的信号比依赖有缺陷的算法更好。

---

## 87. BeBox页面 - 关于BeBox的一切 (2013)

**原文标题**: BeBox Page – Everything about the BeBox (2013)

**原文链接**: [https://www.beunited.org/bebook/](https://www.beunited.org/bebook/)

BeBox：一款为数字媒体专业人士设计的独特而罕见的计算机，由Be公司出品，因其双处理器（多核技术的前身）带来的卓越处理能力而闻名。

主要特点包括带有焊接处理器（最初是AT&T Hobbit，后来是PowerPC）的定制主板和用户可安装的显卡。它拥有广泛的RAM容量（8个SIMM插槽，高达256MB），并支持IDE和SCSI驱动器。由于缺少板载网络，用户可以安装他们首选的以太网或调制解调器。

BeBox的体积庞大，其“Blinkenlights”（LED灯条，直观地显示CPU负载）引人注目。

一个决定性的特点是其全面的I/O板，提供了大量的端口，包括串口、PS/2、操纵杆、MIDI、红外线、音频输入和输出以及16位立体声系统。

最独特的方面是“Geekport”，这是一个37针端口，专门用于用户创建的硬件项目，允许数字和模拟I/O以及直流电源。

尽管它具有强大的性能、创新的设计和可靠的操作系统，但一系列不幸的境遇阻碍了BeBox成为领先的数字媒体计算机并取得广泛成功。

---

## 88. Show HN: Let’s Bend – 开源口琴压音训练器

**原文标题**: Show HN: Let’s Bend – Open-Source Harmonica Bending Trainer

**原文链接**: [https://letsbend.de](https://letsbend.de)

Let's Bend 是一款开源口琴压音训练器，旨在帮助初学者掌握口琴压音技巧。压音技术允许演奏者获得乐器上通常无法获得的音符，从而有效地实现半音阶演奏。该应用程序解决了常见的挑战：确定压音是否正确，而不是意外地发出半音。

Let's Bend 提供正在演奏音符的视觉反馈，从而加快学习速度。开发者创建此应用程序是为了使其可在各种操作系统（macOS、Debian、Windows 和 Android）和设备上访问，优先考虑可扩展性并支持所有琴键和常见的特殊口琴调音。

该应用程序有两个版本：桌面版和 Android 版。Android 版在 Google Play、Amazon 和 F-Droid 上免费且无广告。虽然网络版可供预览，但由于成本考虑，桌面版未在 Microsoft 或 Apple 商店上架。用户可以找到桌面版的替代下载选项。

源代码是开源的，用户可以通过桌面版本中的“请我喝杯咖啡”选项来支持开发者，尽管该应用程序从根本上来说是免费的。该项目强调了有抱负的口琴演奏者的可访问性和易用性。同时还提供用户指南。

---

## 89. 廉价超纯钛或将推动工业广泛应用 (2024)

**原文标题**: Cheap yet ultrapure titanium might enable widespread use in industry (2024)

**原文链接**: [https://phys.org/news/2024-06-cheap-ultrapure-titanium-metal-enable.amp](https://phys.org/news/2024-06-cheap-ultrapure-titanium-metal-enable.amp)

东京大学的研究人员开发了一种新型的、具有成本效益的方法来生产超纯钛，该方法通过高效去除高氧浓度钛矿中的氧来实现。钛以其强度高、重量轻和耐化学腐蚀的特性而闻名，但由于其生产成本高于钢铁和铝等材料，因此未得到充分利用。

新工艺包括将熔融钛与金属钇和三氟化钇反应，从而产生氧浓度低至0.02%（按质量计）的固体脱氧钛合金。一个关键优势在于，即使是含氧量高的钛废料也可以进行处理。反应后的钇也可以回收利用。

研究人员强调了其方案的简单性和缺乏中间化合物，这使其更易于工业应用。这项突破旨在降低钛的生产成本，从而可能使其在各个行业和消费品中得到更广泛的应用。

然而，所得钛中含有高达1%（按质量计）的钇，这可能会影响其机械和化学性能。解决钇污染问题是该工艺实现实际工业应用的下一步。该研究发表在《自然·通讯》上。

---

## 90. 为什么安卓无法使用CDC以太网 (2023)

**原文标题**: Why Android can't use CDC Ethernet (2023)

**原文链接**: [https://jordemort.dev/blog/why-android-cant-use-cdc-ethernet/](https://jordemort.dev/blog/why-android-cant-use-cdc-ethernet/)

本文探讨了为什么CDC以太网（USB以太网适配器的标准）在Android设备上无法工作，尽管Android的Linux内核基础似乎有明显的支持。

作者首先解释了由于官方支持列表有限以及内核配置的作用，寻找与Android兼容的USB以太网适配器的困难。他们指导读者通过ADB启用USB调试，确定手机的内核版本和架构，并获取内核配置文件（通过`/proc/config.gz`或制造商的源代码发布）。

然后分析内核配置中的`USB_NET`条目，指示支持哪些以太网芯片组。解释了CDC以太网标准（EEM、ECM、NCM），突出了它们简化USB以太网适配器支持的潜力。

通过调试揭示了核心问题：虽然Android内核*确实*支持CDC以太网驱动程序（通过内核配置中存在`CONFIG_USB_NET_CDCETHER`、`CONFIG_USB_NET_CDC_EEM`等可以看出），但Linux CDC以太网驱动程序创建的接口被命名为`usbX`，而Android的`EthernetTracker`服务*仅*识别名为`ethX`的接口。这种命名不匹配阻止了Android利用CDC以太网连接。唯一的解决方法是root手机并修改`config_ethernet_iface_regex`设置。

---

## 91. NASA火星轨道器捕捉到火山在晨云之上显现

**原文标题**: NASA Mars Orbiter Captures Volcano Peeking Above Morning Cloud Tops

**原文链接**: [https://www.jpl.nasa.gov/news/nasa-mars-orbiter-captures-volcano-peeking-above-morning-cloud-tops/](https://www.jpl.nasa.gov/news/nasa-mars-orbiter-captures-volcano-peeking-above-morning-cloud-tops/)

美国宇航局2001火星奥德赛轨道器捕捉到阿尔西亚山独特的全景图，这座巨大的火星火山正从晨间水冰云中探出头来。这是首次从地平线上拍摄到火星火山，提供了类似于宇航员从国际空间站观看地球的视角。阿尔西亚山是塔尔西斯山脉的一部分，比地球上的火山大得多。

奥德赛轨道器是绕另一颗行星运行时间最长的任务，它通过旋转90度实现了这张图像的拍摄，使其表面扫描相机能够捕捉到火星地平线的高空景象。这些图像帮助科学家研究尘埃和水冰云层，并观察火星大气层的季节性变化，为火星的演变和天气模式提供有价值的线索。

了解火星云对于预测沙尘暴等天气现象至关重要，这对于未来的火星任务，尤其是在着陆作业期间，非常有帮助。阿尔西亚山的图像高达12英里（20公里），也突出了火山的云形成过程，因为空气沿着其斜坡上升和冷却，特别是在火星远日点，即行星距离太阳最远的时候，远日点云带形成。

奥德赛号上的热辐射成像系统（THEMIS）相机能够以可见光和红外光观察火星，还有助于识别地下水冰并分析火星卫星的成分。该任务由喷气推进实验室（JPL）管理，洛克希德·马丁空间公司和亚利桑那州立大学参与，继续为我们对这颗红色星球的理解做出重大贡献。

---

## 92. 当人们不了解人工智能如何运作时会发生什么

**原文标题**: What happens when people don't understand how AI works

**原文链接**: [https://www.theatlantic.com/culture/archive/2025/06/artificial-intelligence-illiteracy/683021/](https://www.theatlantic.com/culture/archive/2025/06/artificial-intelligence-illiteracy/683021/)

本文着重强调了误解人工智能（尤其是大型语言模型，LLM）实际运作方式的危险性。尽管支持者将人工智能描绘成具有智慧和情感意识，但现实是LLM只是复杂的统计工具，它们模仿人类语言，却缺乏真正的理解或情感。

这种“人工智能盲”会导致几个问题。人们可能会对人工智能产生不健康的依恋，将聊天机器人误认为是精神导师或真正的伴侣，例如“ChatGPT诱发的精神病”。这是因为我们的大脑天生就会假设文本背后存在思维。

此外，硅谷推崇人工智能取代人际关系，大力推广人工智能治疗师、人工智能朋友，甚至人工智能约会管家。这削弱了真正人际关系的价值，而真正的人际关系是建立在相互理解和相互协商的基础上的，而不是个性化的互动。

尽管业界承诺会取得进步，但这些技术往往将利润置于福祉之上，依靠剥削性的劳动实践来训练人工智能模型。然而，仍有希望。许多美国人对人工智能持怀疑态度，通过教育人们了解LLM的局限性，我们可以减轻其潜在危害，并确保它们被负责任地使用。如果人们了解人工智能是什么以及不是什么，他们就可以避免其负面影响。

---

## 93. WWDC25：macOS Tahoe打破Finder数十年历史

**原文标题**: WWDC25: macOS Tahoe Breaks Decades of Finder History

**原文链接**: [https://512pixels.net/2025/06/wwdc25-macos-tahoe-breaks-decades-of-finder-history/](https://512pixels.net/2025/06/wwdc25-macos-tahoe-breaks-decades-of-finder-history/)

作者关注即将发布的macOS Tahoe中一个看似微小但意义重大的变化：Finder图标被反转了。传统上，Finder的“暗面”一直位于左侧，这种设计在数十年的macOS版本中保持一致，从1996年的System 7.5.3到当前的macOS Sequoia都是如此。

文章追溯了Finder图标的演变，展示了其在各种操作系统中的外观，包括Mac OS 8、Mac OS X Public Beta、Panther、Lion、Yosemite和Big Sur。虽然图标在风格上随着时间的推移进行了更新，但其核心设计——暗面位于左侧——一直保持不变。

作者理解这种改变的潜在理由，认为这是为了使Finder图标与macOS Tahoe中新的“Liquid Glass”用户界面保持一致。然而，他们认为有些东西最好不要碰，因为它们是传统。

为了说明当前的Finder图标仍然可以与新的美学相适应，作者甚至将现有图标通过Apple的新Icon Composer应用程序运行，展示了其与Liquid Glass设计的兼容性。

最终，作者希望苹果公司能够重新考虑这一改变，并恢复到传统的Finder图标方向，他们已经向苹果公司提交了反馈（FB17840162）以表达他们的担忧。文章还指出，在WWDC主题演讲中，反转的Finder图标以后视镜装饰的形式出现。

---

## 94. 扎克伯格亲自招人组建全新“超智能”AI团队

**原文标题**: Mark Zuckerberg Personally Hiring to Create New 'Superintelligence' AI Team

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-10/zuckerberg-recruits-new-superintelligence-ai-group-at-meta](https://www.bloomberg.com/news/articles/2025-06-10/zuckerberg-recruits-new-superintelligence-ai-group-at-meta)

总结：

据彭博社报道，马克·扎克伯格正亲自领导Meta公司创建一个新的人工智能团队，专注于实现“超人工智能”。这项举措标志着Meta在当前人工智能应用之外的一次重大推进，旨在开发在各个领域超越人类认知能力的人工智能系统。扎克伯格直接参与该团队的人才招聘，表明该项目在Meta内部具有高度优先地位。

预计该超人工智能团队将在多个领域开展前沿研究和开发。这包括推进通用人工智能模型、提高推理和规划能力，并可能探索机器中的意识和自我意识。重点似乎在于创造不仅能执行特定任务，还能像人类一样理解、学习和适应新情况的人工智能，但速度和效率要高得多。

虽然具体目标和时间表尚未公开，但该团队的创建凸显了Meta致力于保持在人工智能创新前沿的决心。这一举措也加强了科技巨头们加大对通用人工智能（AGI）及更高层次人工智能的投资的趋势，在技术进步的同时也引发了伦理和社会问题。该报告表明，扎克伯格认为这对Meta的长期未来以及以日益复杂的方式连接和服务用户的雄心至关重要。

---

## 95. 轻量级形式化方法的轻量级图表绘制

**原文标题**: Lightweight Diagramming for Lightweight Formal Methods

**原文链接**: [https://blog.brownplt.org/2025/06/09/copeanddrag.html](https://blog.brownplt.org/2025/06/09/copeanddrag.html)

本文介绍了一种名为CnD（应对和拖拽）的新型轻量级图表语言，旨在提高Alloy和Forge等形式化方法工具中可视化的可用性。当前的可视化方法经常存在布局杂乱、排列随意以及视觉表示与用户预期结构脱节等问题。现有的自定义可视化工具要求用户学习复杂的语言（如CSS），并且可能很脆弱，掩盖潜在的规范错误。

CnD通过侧重于结构清晰性和正确性而非美观性来解决这些问题。它允许用户通过一小组操作来逐步改进默认可视化，这些操作约束空间布局、对元素进行分组并指导绘图风格。该语言的设计易于学习和使用，类似于编写规范而不是完整的程序。

CnD的关键特性包括：优先考虑结构清晰性、支持增量可视化以及在可视化约束无法满足时发出明确的错误提示，从而防止产生误导性图表。CnD嵌入到Forge的开源可视化工具中，鼓励用户有效探索和改进他们的模型。该语言优先考虑易用性和模型-图表不匹配的探索，用准确性和清晰性换取视觉上的润色。

---

## 96. 苹果为何因液态玻璃UI更新遭遇强烈反对

**原文标题**: Why Apple Is Facing Backlash with the Liquid Glass UI Refresh

**原文链接**: [https://www.realmikechong.com/why-apple-is-facing-backlash-with-the-liquid-glass-ui-refresh/](https://www.realmikechong.com/why-apple-is-facing-backlash-with-the-liquid-glass-ui-refresh/)

本文探讨了对苹果公司传闻中的“液态玻璃”UI更新的强烈反对，认为其优先考虑美观而非可用性和可访问性，这与iOS 7扁平化设计的积极简化背道而驰。作者是一位资深的苹果开发者，对控制中心因对比度差而降低可用性表示担忧，并声称它将无法达到可访问性标准。

作者认为这种UI更新是错位的，并建议未来在于人工智能驱动的界面，而不是视觉华丽但功能较差的设计。他们强调了向语音和基于聊天的交互方式演变，从而降低了传统UI元素的重要性。他们引用了锤子科技早期不成功的语音控制工作站TNT Station的例子，作为前车之鉴。

作者还承认，像GPT转录这样的人工智能进步使语音输入成为一种可行且通常优于打字的替代方案，即使对于非英语母语者也是如此。他们认为，在增长放缓的市场中，与开发增强用户体验和可访问性的人工智能原生界面相比，投资于资源密集型的UI更新的优先级较低。这篇博客文章本身甚至是语音撰写的。简而言之，作者认为苹果应该专注于人工智能界面的未来，而不是固守过时的UI范式。

---

## 97. 逐个生成像素

**原文标题**: Generating Pixels One by One

**原文链接**: [https://tunahansalih.github.io/blog/autoregressive-vision-generation-part-1/](https://tunahansalih.github.io/blog/autoregressive-vision-generation-part-1/)

本文介绍了自回归图像生成模型，解释了基于其前驱像素预测下一个像素的核心概念。 旨在通过构建一个简单的 MLP 模型来使用 MNIST 数据集生成手写数字图像，从而教授自回归模型的基础知识。

作者 Tuna 将自回归模型定义为一种基于先前结果预测下一个结果的模型，类似于手机上的单词建议。 在数学上，它由概率的链式法则表示，其中每个新元素都依赖于所有先前的元素。 对于图像，每个像素都被认为是序列中的一个元素。

文章然后深入研究了数据准备，特别是使用 MNIST 数字。 它介绍了将像素强度量化为离散 bins 的概念，有效地将像素转换为“tokens”。 模型任务变成了预测下一个像素的整数标签 (token)，将其构架为一个分类问题。 这允许使用类似于 NLP 的技术，如嵌入层。

模型的核心涉及使用上下文窗口，即最后一个 'k' 像素的滑动窗口，来近似预测下一个像素。 起始 tokens 用于处理没有足够历史信息的初始像素。

最后，文章介绍了一个基本的 MLP 模型 `OneHotPixelPredictor`，它接受先前 tokens 的 one-hot 编码并预测下一个 token。 文章还描述了一个函数 `create_token_training_data` 来生成训练数据集，包含上下文 tokens 和目标 tokens，为模型做好准备。

---

## 98. 引爆科技业大规模裁员的税法定时炸弹

**原文标题**: The time bomb in the tax code that's fueling mass tech layoffs

**原文链接**: [https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502](https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502)

本文认为，2017年《减税与就业法案》(TCJA)中一项鲜为人知的美国税法第174条的修改，极大地促成了自2023年以来的大规模科技裁员。近70年来，第174条允许公司立即扣除100%的合格研发支出。为了抵消企业减税，TCJA推迟了一项变更的实施，该变更要求公司从2022年开始将研发支出摊销五年或十五年。

这一变更使研发成本更高，特别是对于资金短缺且无利可图的公司而言。本文认为，它充当了一种隐藏的加速剂，加剧了疫情期间过度招聘和人工智能兴起带来的现有压力。Meta、微软、谷歌、亚马逊、Salesforce、Twilio、Shopify和Coinbase等公司都在该变更生效后宣布了大规模裁员。

本文认为，这一变更正在扼杀创新，刺激在美国境外建立科技公司，并且正在对更广泛的数字经济产生负面影响，而不仅仅是科技行业。它还认为，这是因为许多初创公司、直接面向消费者的品牌和互联网优先的公司长期以来都围绕着立即注销研发支出的能力来建立其增长模式。一项两党努力正在进行中，以废除这一变更，但对数十万被裁员工、城市经济和美国竞争力的影响可能已经无法挽回。本文最后警告说，即将出台的税收立法中可能存在类似的隐藏影响。

---

## 99. 王子特别定制字体符号软盘 (2016)

**原文标题**: Prince's special custom-font symbol floppy disks (2016)

**原文链接**: [https://nymag.com/intelligencer/2016/04/princes-legendary-floppy-disk-symbol-font.html](https://nymag.com/intelligencer/2016/04/princes-legendary-floppy-disk-symbol-font.html)

1993年，王子将其名字改为一个无法发音的符号“爱之符号”，主要是为了激怒他的唱片公司华纳兄弟。 这给需要报道他的媒体带来了一个实际问题，因为该符号无法输入。 王子通过创建一个自定义字体解决了这个问题，该字体用该符号代替了大写字母“P”，并通过软盘将其分发给新闻媒体。 该字体还通过CompuServe在线提供，并附有使用说明。

这个想法源于王子在佩斯利公园平面设计团队内部的挫败感，他们很难使用该符号进行沟通。 史蒂夫·帕克帮助邮寄了这些磁盘，最初持怀疑态度，但后来看到该符号被整合到《滚石》等出版物中而感到印象深刻。

虽然王子现在以对流媒体和在线内容持谨慎态度而闻名，但在 90 年代初，他非常有前瞻性。 他对公告牌系统、美国在线、Photoshop 等新兴技术以及数字艺术创作的可能性感到兴奋。 一旦他理解了聊天群在结识人方面的潜力，他甚至对聊天群产生了兴趣。 软盘的发行突显了王子当时对新媒体的拥抱。

---

## 100. Makefile.md – Makefile 和 Markdown 的多语言合成，可能有用（或无用）

**原文标题**: Makefile.md – Possibly Use(Ful|Less) Polyglot Synthesis of Makefile and Markdown

**原文链接**: [https://zoo.dev/blog/polyglot-makefile-markdown](https://zoo.dev/blog/polyglot-makefile-markdown)

本文详细介绍了创建同时作为 Makefile 和 Markdown 文档（Makefile.md）的多语言混合文件的方法。作者受到同事观察的启发，探索了这两种格式之间的协同潜力。核心概念围绕寻找“风格空操作”——在 Makefile 中没有计算效果但在 Markdown 中提供样式的语法元素。

作者利用 Makefile 注释（以 `#` 开头），这些注释被解释为 Markdown 标题。然后，他们处理更复杂的 Markdown 元素，如代码块，使用 Makefile 的行折叠 (`\`) 和分隔符 `:` 来规避语法冲突。组合 `[](:)` 被发现是一种引入纯文本段落的方法，同时避免 Makefile 中的语法错误，并结合一个空操作配方 `):` 来解决依赖问题。

本文强调了合并这两种格式的挑战，强调需要平衡 Makefile 的执行要求与 Markdown 的渲染需求。最终结果是一个功能性的 Makefile，当作为 Markdown 渲染时，呈现出一个可读且具有样式的文档。虽然作者质疑这种特定多语言混合文件的实际效用，但他们认为它是类似项目的灵感来源，特别是探索具有更好协同作用的语言组合。他们邀请读者贡献改进 Makefile-Markdown 多语言混合文件词汇表的想法。

---

