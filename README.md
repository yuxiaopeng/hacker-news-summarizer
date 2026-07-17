# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-17.md)

*最后自动更新时间: 2026-07-17 18:41:11*
## 1. 首次在遥远恒星宜居带内的类地行星上发现大气层

**原文标题**: First atmosphere found on Earth-like planet in habitable zone of distant star

**原文链接**: [https://www.bbc.com/news/articles/cy4kdd1e0ejo](https://www.bbc.com/news/articles/cy4kdd1e0ejo)

研究人员在寻找外星生命的过程中取得了一项重大里程碑：首次在位于恒星宜居带内的岩石类地行星周围发现了大气层。

这颗名为 LHS 1140 b 的行星距离地球 48 光年，绕着一颗小型、冷却的红矮星运行。尽管目前已发现超过 6,000 颗系外行星，但此项发现意义重大，因为它标志着人类首次确认一颗位于“宜居带”（即温度允许液态水存在的区域）内的小型岩石世界拥有大气层。

该发现的关键细节包括：
*   **大气成分：** 到目前为止，研究人员已探测到**氦气**。虽然氦气本身无法支持生命，但科学家认为，低层大气中可能存在更多维持生命的成分。
*   **科学意义：** 哈佛大学的 Collin Cherubim 博士和 David Charbonneau 博士强调，这为太阳系外存在具备类地条件的星球提供了迄今为止最强有力的证据。
*   **背景：** 该研究成果发表在《科学》杂志上。由于此前其他极具潜力的候选行星均未得出确定结论，此项发现因此脱颖而出。例如，NASA 的詹姆斯·韦伯空间望远镜最近排除了 TRAPPIST-1d 存在类地大气的可能性，而此前在 K2-18b 行星上发现的生物特征最近也被认定为未经证实。

虽然研究人员尚未发现生命，但在宜居带内的岩石行星上发现大气层，使科学界在回答“我们在宇宙中是否孤独”这一问题上又迈进了一步。

---

## 2. Mozilla：开源 AI 现状

**原文标题**: Mozilla: The state of open source AI

**原文链接**: [https://stateofopensource.ai/](https://stateofopensource.ai/)

Mozilla 2026年7月的报告《开源AI现状》指出，开放权重模型在功能上已达到与封闭专有系统同等的水平。虽然封闭模型在复杂推理方面仍保持微弱优势，但开放模型目前在生产环境的 Token 使用量上占据主导地位，尤其是在编程和特定专业任务中。这一转变主要得益于推理成本在三年内下降了50倍。

尽管开发者采用率高达79%，但“运营差距”依然存在：仅有51%的开源模型项目成功投入生产，而封闭模型这一比例为63%。主要障碍在于基础设施、安全和维护，而非模型本身的能力。这为“开源技术栈”创造了巨大的市场空间，DeepSeek、Mistral和Databricks等公司通过托管、微调和企业级平台，证明了数十亿美元营收模式的成功。

报告强调，开源现已成为一种“主权选择”。在政局动荡和供应商锁定的时代，开放权重提供了“退出权”，允许各国和企业在本地运行AI，而无需担心服务突然中断或价格随意上涨。值得注意的是，中国已成为开放权重的领先提供商；到2026年中期，以通义千问（Qwen）和DeepSeek为代表的中国模型已占据全球开放模型Token流量的近一半，成为应对出口管制的战略对冲手段。

Mozilla总结道，AI的前沿阵地正在向“堆栈上层”转移。随着模型趋于商品化，下一阶段的竞争将集中在“智能体架构（agentic harness）”——即管理模型与现实世界交互的互操作软件层。通过倡导竞争和互操作性，开源社区旨在确保AI保持为一种去中心化的资源，而非由企业控制的垄断门槛。

---

## 3. Lisp 之路：该选哪种 Lisp

**原文标题**: A Road to Lisp: Which Lisp

**原文链接**: [https://scotto.me/blog/2026-07-17-which-lisp/](https://scotto.me/blog/2026-07-17-which-lisp/)

《Lisp 之路：选择哪种 Lisp》探讨了 Lisp 方言家族的多样性，强调虽然 Common Lisp 和 Clojure 等选择在语义和平台方面有所不同，但它们共享一种能够转变程序员思维方式的核心哲学。

**Common Lisp (CL)** 是一种成熟且标准化的“老派”方言。它以稳定性著称——自 1994 年 ANSI 标准化以来基本保持不变——并通过 SBCL 等可编译为原生代码的实现提供高性能。CL 的功能极其完备，拥有用于实时调试的强大条件/重启（condition/restart）系统以及灵活的 Common Lisp 对象系统（CLOS）。它在科学研究、原型设计以及需要快速迭代和长时运行进程的环境中表现卓越。

**Clojure** 由 Rich Hickey 创建，是一种主要运行在 JVM 上（并可通过 ClojureScript 运行在 JavaScript 上）的现代函数式方言。它优先考虑不可变性，利用持久化数据结构和显式状态管理工具来简化并发。通过利用现有的 Java 生态系统，Clojure 在金融和大规模 Web 服务等数据密集型领域获得了显著的企业认可，被 Nubank 和沃尔玛（Walmart）等公司所采用。

作者总结道，对于初学者来说，具体的方言选型并不如学习 Lisp 范式本身重要。一旦掌握了核心概念，在不同方言之间切换就会相对容易。Common Lisp 提供了具有原生性能的深度集成开发体验，而 Clojure 则提供了一种针对现代企业环境量身定制的实用主义函数式方法。这两种语言都得到了活跃社区和丰富学习资源的支持，从《Practical Common Lisp》一书到 Rich Hickey 关于软件设计的极具影响力的演讲，均是不错的选择。

---

## 4. Kimi K3，以及我们仍能从 Pelican 基准测试中学到什么

**原文标题**: Kimi K3, and what we can still learn from the pelican benchmark

**原文链接**: [https://simonwillison.net/2026/Jul/16/kimi-k3/](https://simonwillison.net/2026/Jul/16/kimi-k3/)

2026年7月16日，中国AI实验室月之暗面（Moonshot AI）发布了拥有2.8万亿参数的巨型模型Kimi K3。Kimi K3定位为首个“开源3T级模型”，计划于7月27日开放模型权重。基准测试显示，其性能与GPT-5.6 Sol和Claude Fable 5等顶级模型旗鼓相当，尤其在前端编码和长程知识任务方面表现优异。然而，作为一款国产模型，其定价显著偏高：输入每百万Token 3美元，输出每百万Token 15美元。

作者使用其标志性的“鹈鹕基准测试”（生成一个骑自行车的鹈鹕SVG图像）对K3进行了评估。该测试的关键观察结果包括：

*   **高推理强度**：K3消耗了超过13,000个推理Token来生成该SVG，导致单次提示词的成本达25美分。
*   **Token开销**：发送“hello”提示词消耗了86个Token，表明其包含约85个Token的庞大隐藏系统提示词。
*   **强大的视觉能力**：该模型准确描述了生成的SVG，证实了其高质量的图像识别能力。

尽管作者承认鹈鹕测试并非完美的基准——因为它缺乏对智能体工具调用的评估，且部分中端模型（如GLM-5.2）在SVG生成上已超越旗舰模型——但他认为这仍是一项有价值的“Hello World”式练习。它能作为测试API连接性的硬性手段，揭示推理与成本结构，并确认模型的空间感知及输出有效代码的能力。总之，虽然K3较K2.5有显著进步，但该测试凸显了最新一代大语言模型向高成本、重推理输出转型的趋势。

---

## 5. AI 遇上密码学 2：AI 在 OpenVM 的 ZkVM 中发现了什么

**原文标题**: AI Meets Cryptography 2: What AI Found in OpenVM's ZkVM

**原文链接**: [https://blog.zksecurity.xyz/posts/openvm-bugs/](https://blog.zksecurity.xyz/posts/openvm-bugs/)

zkSecurity 的 AI 审计工具 **zkao** 在 OpenVM 的 `openvm-pairing` 客户端库中发现了一个严重的可靠性（soundness）漏洞（**CVE-2026-46669**）。虽然 zkVM 的核心证明系统保持完好，但该漏洞允许恶意证明者伪造配对等式，从而破坏了 Groth16、PLONK 和 BLS 签名等协议的密码学基础。

该漏洞源于一种优化的配对检查实现。为了避免高昂的最终幂运算（final exponentiation）开销，该库使用了一种涉及缩放因子的“残差见证”（residue-witness）技巧。然而，该实现未能验证该缩放因子是否属于正确的子域（$\mathbb{F}_{p^6}$）。因此，证明者可以通过提供伪造的见证（$c=1, u=f^{-1}$）来绕过对任何 Miller 循环输出的检查，从而有效地使虚假证明通过验证。这一影响对于依赖这些密码学原语进行验证的 L2 rollup、跨链桥和隐私协议而言具有重大意义。

在技术层面，本文强调了“原生”大语言模型（LLM）配置的局限性。虽然标准模型由于 zkVM 密集的依赖关系和复杂的架构而失败，但 zkao 通过专门的“上下文工程”和一种名为“cryptopsy”的工作流取得了成功。该方法通过将代码分析与学术文献中关于已知密码学陷阱的见解相结合，模拟了专家的手动审计。

该漏洞已在 **OpenVM 1.6.0 版本**中得到修复。zkSecurity 总结道，虽然 AI 正在成为持续安全覆盖的有力工具，但人工验证仍然必不可少，因为自动生成的概念验证（PoC）仍然存在较高的误报率，需要专家进行分诊和评估。

---

## 6. 人们应对问题的三种方式（除解决之外）

**原文标题**: Three ways people respond to a problem (other than solving it)

**原文链接**: [https://improvesomething.today/responses-to-problems/](https://improvesomething.today/responses-to-problems/)

在本文中，一位专业顾问指出了在解决问题过程中（或与之并存）常见的三种错误应对方式。这些方式被归纳为三个“P”：

1. **推转问题（Pushing problems around）：** 这源于“局部优化”，即解决一个部门的问题却无意中在别处制造了新问题。作者建议，领导者不应因这种行为责备个人，而应审视并修正那些奖励局部利益而非全局方案的系统性激励机制。
2. **维持问题（Preserving problems）：** 引用“舍基原则（Shirky Principle）”，作者指出机构往往会无意中延续其原本旨在解决的问题，因为机构的生存依赖于这些问题的存在。要应对这一点，必须识别谁从问题的持续中获益，并将这些利益相关者纳入规划过程。
3. **催生新问题（Promoting new problems）：** 解决一个问题往往会使次要问题上升为首要任务，或产生全新的复杂情况。作者认为解决问题是一个无止境的循环，因此顾问和领导者必须放弃问题会彻底“完结”的幻想。

作者总结道，虽然解决问题能带来更好的生活，但最高效的人也懂得如何排列优先级。通过使用图表等工具来可视化问题并达成共识，人们可以将精力集中在真正值得解决的问题上，同时学会忽略其余无关痛痒的问题。

---

## 7. Frame – the first Linux Assembly X server

**原文标题**: Frame – the first Linux Assembly X server

**原文链接**: [https://isene.org/2026/07/Frame.html](https://isene.org/2026/07/Frame.html)

在文章**《Frame——首个 Linux 汇编 X 服务器》**中，作者详述了其如何用一个完全由汇编语言编写的精简定制方案，来取代庞大且复杂的软件栈的历程。

**关键要点：**

*   **核心软件：** 核心部分是 **Frame**，一个由 2 万行汇编代码编写的 Linux X 服务器。它取代了传统包含 400 万行代码的 X11 服务器，且在运行时无需任何依赖项、库或垃圾回收机制。
*   **“CHasm” 软件栈：** Frame 是一个完整定制软件栈的一部分，该栈还包括窗口管理器 (**tile**)、终端 (**glass**) 和 shell (**bare**)。该软件栈的总代码量约为 10 万行，比其所取代的环境（gdm、X11、i3 等）缩减了约 50 倍。
*   **效率与性能：** 作者的主要动力源于对电池续航和软件自主权的追求。Frame 在空闲时的 CPU 占用率远低于 Xorg，消除了不必要的唤醒和“热路径”。在没有用户输入时，系统保持完全静止。
*   **开发过程：** 尽管硬件层和 GPU 移交过程非常复杂，但作者将 AI 工具 **Claude** 作为编程伙伴和导师，以此攻克 X 协议和硬件层面的各种需求。
*   **哲学理念：** 作者倡导“为单一受众而作的软件”，将个人控制权和简洁性置于通用软件的臃肿之上。为了回馈社区，所有代码均已发布至**公有领域**（Public Domain）。

目前，该系统已稳定到足以胜任日常使用，在支持 Firefox 和 GIMP 等大型应用的同时，提供了量身定制且极致高效的计算体验。

---

## 8. Show HN: Watch bots interact with an SSH honeypot in real time

**原文标题**: Show HN: Watch bots interact with an SSH honeypot in real time

**原文链接**: [https://honeypotlive.cc/](https://honeypotlive.cc/)

生成摘要时出错

---

## 9. Frank Lloyd Wright's First Home

**原文标题**: Frank Lloyd Wright's First Home

**原文链接**: [https://www.architecturaldigest.com/story/frank-lloyd-wright-home-and-studio-everything-you-need-to-know](https://www.architecturaldigest.com/story/frank-lloyd-wright-home-and-studio-everything-you-need-to-know)

生成摘要时出错

---

## 10. Show HN: Explore the Workspaces of Modern Creators

**原文标题**: Show HN: Explore the Workspaces of Modern Creators

**原文链接**: [https://workspaces.xyz/](https://workspaces.xyz/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 2 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 3 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 4 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 5 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 6 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 7 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 8 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 9 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 10 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 11 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 12 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 13 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 14 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 15 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 16 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 17 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 18 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 19 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 20 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 21 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 22 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 23 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 24 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 25 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 26 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 27 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 28 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 29 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 30 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 31 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 32 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 33 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 34 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 35 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 36 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 37 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 38 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 39 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 40 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 41 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 42 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 43 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 44 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 45 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 46 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 47 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 48 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 49 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 50 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 51 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 52 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 53 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 54 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 55 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 56 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 57 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 58 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 59 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 60 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 61 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 62 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 63 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 64 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 65 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 66 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 67 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 68 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 69 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 70 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 71 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 72 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 73 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 74 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 75 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 76 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 77 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 78 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 79 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 80 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 81 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 82 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 83 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 84 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 85 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 86 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 87 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 88 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 89 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 90 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 91 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 92 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 93 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 94 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 95 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 96 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 97 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 98 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 99 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 100 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 101 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 102 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 103 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 104 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 105 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 106 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 107 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 108 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 109 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 110 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 111 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 112 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 113 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 114 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 115 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 116 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 117 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 118 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 119 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 120 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 121 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 122 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 123 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 124 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 125 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 126 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 127 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 128 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 129 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 130 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 131 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 132 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 133 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 134 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 135 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 136 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 137 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 138 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 139 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 140 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 141 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 142 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 143 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 144 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 145 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 146 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 147 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 148 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 149 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 150 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 151 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 152 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 153 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 154 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 155 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 156 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 157 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 158 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 159 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 160 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 161 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 162 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 163 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 164 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 165 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 166 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 167 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 168 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 169 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 170 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 171 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 172 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 173 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 174 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 175 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 176 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 177 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 178 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 179 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 180 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 181 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 182 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 183 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 184 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 185 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 186 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 187 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 188 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 189 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 190 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 191 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 192 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 193 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 194 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 195 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 196 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 197 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 198 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 199 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 200 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 201 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 202 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 203 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 204 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 205 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 206 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 207 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 208 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 209 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 210 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 211 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 212 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 213 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 214 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 215 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 216 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 217 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 218 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 219 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 220 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 221 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 222 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 223 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 224 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 225 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 226 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 227 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 228 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 229 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 230 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 231 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 232 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 233 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 234 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 235 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 236 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 237 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 238 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 239 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 240 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 241 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 242 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 243 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 244 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 245 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 246 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 247 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 248 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 249 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 250 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 251 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 252 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 253 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 254 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 255 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 256 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 257 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 258 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 259 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 260 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 261 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 262 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 263 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 264 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 265 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 266 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 267 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 268 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 269 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 270 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 271 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 272 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 273 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 274 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 275 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 276 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 277 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 278 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 279 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 280 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 281 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 282 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 283 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 284 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 285 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 286 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 287 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 288 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 289 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 290 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 291 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 292 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 293 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 294 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 295 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 296 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 297 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 298 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 299 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 300 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 301 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 302 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 303 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 304 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 305 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 306 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 307 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 308 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 309 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 310 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 311 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 312 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 313 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 314 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 315 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 316 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 317 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 318 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 319 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 320 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 321 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 322 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 323 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 324 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 325 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 326 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 327 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 328 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 329 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 330 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 331 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 332 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 333 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 334 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 335 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 336 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 337 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 338 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 339 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 340 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 341 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 342 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 343 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 344 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 345 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 346 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 347 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 348 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 349 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 350 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 351 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 352 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 353 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 354 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 355 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 356 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 357 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 358 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 359 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 360 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 361 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 362 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 363 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 364 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 365 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 366 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 367 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 368 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 369 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 370 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 371 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 372 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 373 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 374 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 375 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 376 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 377 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 378 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 379 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 380 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 381 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 382 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 383 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 384 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 385 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 386 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 387 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 388 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 389 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 390 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 391 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 392 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 393 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 394 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 395 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 396 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 397 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 398 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 399 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 400 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 401 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 402 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 403 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 404 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 405 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 406 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 407 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 408 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 409 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 410 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 411 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 412 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 413 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 414 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 415 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 416 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 417 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 418 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 419 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 420 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 421 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 422 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 423 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 424 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 425 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 426 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 427 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 428 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 429 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 430 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 431 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 432 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 433 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 434 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 435 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 436 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 437 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 438 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 439 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 440 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 441 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 442 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 443 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 444 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 445 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 446 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 447 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 448 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 449 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 450 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 451 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 452 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 453 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 454 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 455 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 456 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 457 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 458 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 459 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 460 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 461 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 462 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 463 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 464 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 465 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 466 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 467 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 468 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 469 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 470 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 471 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 472 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 473 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 474 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 475 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 476 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 477 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 478 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 479 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 480 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 481 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 482 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 483 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 484 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
