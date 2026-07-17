# Hacker News 热门文章摘要 (2026-07-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. More Bounce to the Ounce

**原文标题**: More Bounce to the Ounce

**原文链接**: [https://mceglowski.substack.com/p/more-bounce-to-the-ounce](https://mceglowski.substack.com/p/more-bounce-to-the-ounce)

生成摘要时出错

---

## 12. EEG shows brain can simultaneous encode two speech streams

**原文标题**: EEG shows brain can simultaneous encode two speech streams

**原文链接**: [https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003876](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003876)

生成摘要时出错

---

## 13. Apple targets dozens of OpenAI employees with legal letters

**原文标题**: Apple targets dozens of OpenAI employees with legal letters

**原文链接**: [https://www.ft.com/content/1b8c9d52-88a9-426b-ba47-f1811f859166](https://www.ft.com/content/1b8c9d52-88a9-426b-ba47-f1811f859166)

生成摘要时出错

---

## 14. Designing emoji for the way we communicate today

**原文标题**: Designing emoji for the way we communicate today

**原文链接**: [https://blog.google/products-and-platforms/platforms/android/world-emoji-day-noto-3d/](https://blog.google/products-and-platforms/platforms/android/world-emoji-day-noto-3d/)

生成摘要时出错

---

## 15. Manufact (YC S25) Is Hiring a Senior infra engineer to build the MCP cloud

**原文标题**: Manufact (YC S25) Is Hiring a Senior infra engineer to build the MCP cloud

**原文链接**: [https://www.ycombinator.com/companies/manufact/jobs/Dh6PYP5-senior-infrastructure-engineer](https://www.ycombinator.com/companies/manufact/jobs/Dh6PYP5-senior-infrastructure-engineer)

生成摘要时出错

---

## 16. Claude Code: Anatomy of a Misfeature

**原文标题**: Claude Code: Anatomy of a Misfeature

**原文链接**: [https://www.olafalders.com/2026/07/17/claude-code-anatomy-of-a-misfeature/](https://www.olafalders.com/2026/07/17/claude-code-anatomy-of-a-misfeature/)

生成摘要时出错

---

## 17. Pebble Mega Update – July 2026

**原文标题**: Pebble Mega Update – July 2026

**原文链接**: [https://repebble.com/blog/pebble-mega-update-july-2026](https://repebble.com/blog/pebble-mega-update-july-2026)

生成摘要时出错

---

## 18. Short sellers notch $8.7B profit as SpaceX shares dip to IPO price

**原文标题**: Short sellers notch $8.7B profit as SpaceX shares dip to IPO price

**原文链接**: [https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/](https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/)

生成摘要时出错

---

## 19. Faster binary search: from compiled code to mechanical sympathy

**原文标题**: Faster binary search: from compiled code to mechanical sympathy

**原文链接**: [https://pythonspeed.com/articles/branchless-binary-search/](https://pythonspeed.com/articles/branchless-binary-search/)

生成摘要时出错

---

## 20. VulnHunter: Capital One's agentic AI code security tool

**原文标题**: VulnHunter: Capital One's agentic AI code security tool

**原文链接**: [https://www.capitalone.com/tech/open-source/announcing-vulnhunter/](https://www.capitalone.com/tech/open-source/announcing-vulnhunter/)

生成摘要时出错

---

## 21. PennyLane is an open-source quantum software platform for quantum

**原文标题**: PennyLane is an open-source quantum software platform for quantum

**原文链接**: [https://github.com/PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)

生成摘要时出错

---

## 22. Microsoft Comic Chat is now open source

**原文标题**: Microsoft Comic Chat is now open source

**原文链接**: [https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/)

生成摘要时出错

---

## 23. Camera Chase Vehicle

**原文标题**: Camera Chase Vehicle

**原文链接**: [https://transistor-man.com/gimbal_camera_rover.html](https://transistor-man.com/gimbal_camera_rover.html)

生成摘要时出错

---

## 24. Show HN: Simulator for a custom 8-bit discreet logic computer

**原文标题**: Show HN: Simulator for a custom 8-bit discreet logic computer

**原文链接**: [https://msap2.mehran.dk](https://msap2.mehran.dk)

生成摘要时出错

---

## 25. Decoy Font

**原文标题**: Decoy Font

**原文链接**: [https://www.mixfont.com/experiments/decoy-font](https://www.mixfont.com/experiments/decoy-font)

生成摘要时出错

---

## 26. Kimi K3: Open Frontier Intelligence

**原文标题**: Kimi K3: Open Frontier Intelligence

**原文链接**: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)

生成摘要时出错

---

## 27. How Has Roman Concrete Lasted for Millennia? 1,900-Year-Old Latrine Offers Clues

**原文标题**: How Has Roman Concrete Lasted for Millennia? 1,900-Year-Old Latrine Offers Clues

**原文链接**: [https://www.smithsonianmag.com/smart-news/how-has-roman-concrete-lasted-for-millennia-a-1900-year-old-latrine-offers-new-clues-about-the-materials-impressive-durability-180989115/](https://www.smithsonianmag.com/smart-news/how-has-roman-concrete-lasted-for-millennia-a-1900-year-old-latrine-offers-new-clues-about-the-materials-impressive-durability-180989115/)

生成摘要时出错

---

## 28. Tannakian Reconstruction

**原文标题**: Tannakian Reconstruction

**原文链接**: [https://bartoszmilewski.com/2026/07/14/tannakian-reconstruction/](https://bartoszmilewski.com/2026/07/14/tannakian-reconstruction/)

生成摘要时出错

---

## 29. An Engineer's Guide to USB Typе-С (2024)

**原文标题**: An Engineer's Guide to USB Typе-С (2024)

**原文链接**: [https://www.ti.com/lit/eb/slyy228/slyy228.pdf?ts=1759892558029](https://www.ti.com/lit/eb/slyy228/slyy228.pdf?ts=1759892558029)

生成摘要时出错

---

## 30. An Engineer's Guide to USB Typе-С (2024)

**原文标题**: An Engineer's Guide to USB Typе-С (2024)

**原文链接**: [https://www.ti.com/lit/eb/slyy228/slyy228.pdf?ts=1759892558029](https://www.ti.com/lit/eb/slyy228/slyy228.pdf?ts=1759892558029)

生成摘要时出错

---

## 31. $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol

**原文标题**: $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol

**原文链接**: [https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

生成摘要时出错

---

## 32. LM Studio Bionic: the AI agent for open models

**原文标题**: LM Studio Bionic: the AI agent for open models

**原文链接**: [https://lmstudio.ai/blog/introducing-lm-studio-bionic](https://lmstudio.ai/blog/introducing-lm-studio-bionic)

生成摘要时出错

---

## 33. NotebookLM is now Gemini Notebook

**原文标题**: NotebookLM is now Gemini Notebook

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)

生成摘要时出错

---

## 34. Evidence of inconsistencies in evaluation process and selection of winners

**原文标题**: Evidence of inconsistencies in evaluation process and selection of winners

**原文链接**: [https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423)

生成摘要时出错

---

## 35. Turn your singing voice into printable notes (in the browser)

**原文标题**: Turn your singing voice into printable notes (in the browser)

**原文链接**: [https://om-intelligence.ch/projects/vocal-notation/vocal-notation.html](https://om-intelligence.ch/projects/vocal-notation/vocal-notation.html)

生成摘要时出错

---

## 36. The Little Book of Reinforcement Learning

**原文标题**: The Little Book of Reinforcement Learning

**原文链接**: [https://github.com/alxndrTL/little-book-rl/](https://github.com/alxndrTL/little-book-rl/)

生成摘要时出错

---

## 37. Solod: Go can be a better C

**原文标题**: Solod: Go can be a better C

**原文链接**: [https://solod.dev](https://solod.dev)

生成摘要时出错

---

## 38. Meta in Talks to Lease Computing Power to Anthropic in Potential $10B Deal

**原文标题**: Meta in Talks to Lease Computing Power to Anthropic in Potential $10B Deal

**原文链接**: [https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html)

生成摘要时出错

---

## 39. Immersive Linear Algebra Book with Interactive Figures (2015)

**原文标题**: Immersive Linear Algebra Book with Interactive Figures (2015)

**原文链接**: [https://immersivemath.com/ila/](https://immersivemath.com/ila/)

生成摘要时出错

---

## 40. Starlink from 1984

**原文标题**: Starlink from 1984

**原文链接**: [https://nemanjatrifunovic.substack.com/p/starlink-from-1984](https://nemanjatrifunovic.substack.com/p/starlink-from-1984)

生成摘要时出错

---

## 41. CD sales growth outpaced vinyl in the first half of 2026

**原文标题**: CD sales growth outpaced vinyl in the first half of 2026

**原文链接**: [https://consequence.net/2026/07/the-cd-revival-is-getting-hard-to-ignore/](https://consequence.net/2026/07/the-cd-revival-is-getting-hard-to-ignore/)

生成摘要时出错

---

## 42. Detecting LLM-Generated Texts with “Classical” Machine Learning

**原文标题**: Detecting LLM-Generated Texts with “Classical” Machine Learning

**原文链接**: [https://blog.lyc8503.net/en/post/llm-classifier/](https://blog.lyc8503.net/en/post/llm-classifier/)

生成摘要时出错

---

## 43. Mathematics of Data Science

**原文标题**: Mathematics of Data Science

**原文链接**: [https://arxiv.org/abs/2607.11938](https://arxiv.org/abs/2607.11938)

生成摘要时出错

---

## 44. Helium escaping from atmosphere of nearby rocky exoplanet in a habitable zone

**原文标题**: Helium escaping from atmosphere of nearby rocky exoplanet in a habitable zone

**原文链接**: [https://www.science.org/doi/10.1126/science.aea9708](https://www.science.org/doi/10.1126/science.aea9708)

生成摘要时出错

---

## 45. The LLM Critics Are Right. I Use LLMs Anyway

**原文标题**: The LLM Critics Are Right. I Use LLMs Anyway

**原文链接**: [https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

生成摘要时出错

---

## 46. Alzheimer's trial results lend momentum to strategies targeting tau

**原文标题**: Alzheimer's trial results lend momentum to strategies targeting tau

**原文链接**: [https://www.science.org/content/article/alzheimer-s-trial-results-lend-momentum-strategies-targeting-tau](https://www.science.org/content/article/alzheimer-s-trial-results-lend-momentum-strategies-targeting-tau)

生成摘要时出错

---

## 47. 'Likweli': A new monkey species discovered in the Congo Basin

**原文标题**: 'Likweli': A new monkey species discovered in the Congo Basin

**原文链接**: [https://news.yale.edu/2026/07/15/meet-likweli-new-monkey-species-discovered-congo-basin](https://news.yale.edu/2026/07/15/meet-likweli-new-monkey-species-discovered-congo-basin)

生成摘要时出错

---

## 48. How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文标题**: How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文链接**: [https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

生成摘要时出错

---

## 49. US Corporate Insiders Are Selling Stocks at a Near Record Pace

**原文标题**: US Corporate Insiders Are Selling Stocks at a Near Record Pace

**原文链接**: [https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace](https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace)

生成摘要时出错

---

## 50. Old Icons

**原文标题**: Old Icons

**原文链接**: [https://leancrew.com/all-this/2026/07/old-icons/](https://leancrew.com/all-this/2026/07/old-icons/)

生成摘要时出错

---

## 51. Pushinka

**原文标题**: Pushinka

**原文链接**: [https://en.wikipedia.org/wiki/Pushinka](https://en.wikipedia.org/wiki/Pushinka)

生成摘要时出错

---

## 52. In Praise of Exhaustive Destructuring

**原文标题**: In Praise of Exhaustive Destructuring

**原文链接**: [https://antoine.vandecreme.net/blog/exhaustive-destructuring-praise/](https://antoine.vandecreme.net/blog/exhaustive-destructuring-praise/)

生成摘要时出错

---

## 53. US manufacturing employment is down, but each state has its own story

**原文标题**: US manufacturing employment is down, but each state has its own story

**原文链接**: [https://fredblog.stlouisfed.org/2026/07/us-manufacturing-employment-is-down-but-each-state-has-its-own-story/](https://fredblog.stlouisfed.org/2026/07/us-manufacturing-employment-is-down-but-each-state-has-its-own-story/)

生成摘要时出错

---

## 54. Ente – Opening Our Books

**原文标题**: Ente – Opening Our Books

**原文链接**: [https://ente.com/open/](https://ente.com/open/)

生成摘要时出错

---

## 55. Goes-19 weather satellite enters Safe Hold mode

**原文标题**: Goes-19 weather satellite enters Safe Hold mode

**原文链接**: [https://www.spaceweather.gov/news/goes-19-safe-hold](https://www.spaceweather.gov/news/goes-19-safe-hold)

生成摘要时出错

---

## 56. Cops Use Flock to Track People, Not Cars

**原文标题**: Cops Use Flock to Track People, Not Cars

**原文链接**: [https://www.404media.co/how-cops-use-flock-to-track-people-not-cars/](https://www.404media.co/how-cops-use-flock-to-track-people-not-cars/)

生成摘要时出错

---

## 57. Show HN: Clx – Compile Lua to Native Executables Through C++20

**原文标题**: Show HN: Clx – Compile Lua to Native Executables Through C++20

**原文链接**: [https://github.com/samyeyo/clx](https://github.com/samyeyo/clx)

生成摘要时出错

---

## 58. Pseudpocalypse

**原文标题**: Pseudpocalypse

**原文链接**: [https://dynomight.net/pseudpocalypse/](https://dynomight.net/pseudpocalypse/)

生成摘要时出错

---

## 59. Australian Data Centres forced to generate more power than they use

**原文标题**: Australian Data Centres forced to generate more power than they use

**原文链接**: [https://www.afr.com/technology/albanese-hits-data-centres-with-grid-mandate-in-major-ai-pivot-20260715-p60fg6](https://www.afr.com/technology/albanese-hits-data-centres-with-grid-mandate-in-major-ai-pivot-20260715-p60fg6)

生成摘要时出错

---

## 60. Multi-Primary Color Display Emerges as Next-Gen Color Reproduction Technology

**原文标题**: Multi-Primary Color Display Emerges as Next-Gen Color Reproduction Technology

**原文链接**: [https://en.ubiresearchnet.com/multi-primary-color-display-technology-2026/](https://en.ubiresearchnet.com/multi-primary-color-display-technology-2026/)

生成摘要时出错

---

## 61. The lost joy of music piracy

**原文标题**: The lost joy of music piracy

**原文链接**: [https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming](https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming)

生成摘要时出错

---

## 62. British Steel taken into public ownership to protect 'vital' UK supply

**原文标题**: British Steel taken into public ownership to protect 'vital' UK supply

**原文链接**: [https://www.bbc.com/news/articles/c5y680w62wno](https://www.bbc.com/news/articles/c5y680w62wno)

生成摘要时出错

---

## 63. Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

**原文标题**: Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

**原文链接**: [https://arxiv.org/abs/2607.12395](https://arxiv.org/abs/2607.12395)

生成摘要时出错

---

## 64. Sony deletes more movies from the accounts of people who ‘bought’ them

**原文标题**: Sony deletes more movies from the accounts of people who ‘bought’ them

**原文链接**: [https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/)

生成摘要时出错

---

## 65. Schema Harness Achieves ~99% on Arc‑AGI‑3 Public

**原文标题**: Schema Harness Achieves ~99% on Arc‑AGI‑3 Public

**原文链接**: [https://schema-harness.github.io/](https://schema-harness.github.io/)

生成摘要时出错

---

## 66. Abstracting Effects with Continuations

**原文标题**: Abstracting Effects with Continuations

**原文链接**: [https://crowdhailer.me/2026-07-15/abstracting-effects-with-continuations/](https://crowdhailer.me/2026-07-15/abstracting-effects-with-continuations/)

生成摘要时出错

---

## 67. UIUC AI Teaching Assistant

**原文标题**: UIUC AI Teaching Assistant

**原文链接**: [https://github.com/Center-for-AI-Innovation/ai-teaching-assistant-uiuc](https://github.com/Center-for-AI-Innovation/ai-teaching-assistant-uiuc)

生成摘要时出错

---

## 68. OnePlus halts operations in USA and Europe

**原文标题**: OnePlus halts operations in USA and Europe

**原文链接**: [https://community.oneplus.com/thread/2170715118587871237](https://community.oneplus.com/thread/2170715118587871237)

生成摘要时出错

---

## 69. Kimi K3 may be an important inflection point for AI

**原文标题**: Kimi K3 may be an important inflection point for AI

**原文链接**: [https://twitter.com/GavinSBaker/status/2078110934740980193](https://twitter.com/GavinSBaker/status/2078110934740980193)

生成摘要时出错

---

## 70. Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文标题**: Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文链接**: [https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/](https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/)

生成摘要时出错

---

## 71. Let's Build PlanetScale from Scratch: Infrastructure

**原文标题**: Let's Build PlanetScale from Scratch: Infrastructure

**原文链接**: [https://onatm.dev/2026/07/16/homescale-part-1/](https://onatm.dev/2026/07/16/homescale-part-1/)

生成摘要时出错

---

## 72. The privacy problems hidden in your period tracker

**原文标题**: The privacy problems hidden in your period tracker

**原文链接**: [https://www.bbc.com/future/article/20260715-how-period-trackers-share-womens-private-details](https://www.bbc.com/future/article/20260715-how-period-trackers-share-womens-private-details)

生成摘要时出错

---

## 73. Show HN: Mojibake – A low-level Unicode library written in C

**原文标题**: Show HN: Mojibake – A low-level Unicode library written in C

**原文链接**: [https://mojibake.zaerl.com/](https://mojibake.zaerl.com/)

生成摘要时出错

---

## 74. How Our Rust-to-Zig Rewrite Is Going

**原文标题**: How Our Rust-to-Zig Rewrite Is Going

**原文链接**: [https://rtfeldman.com/rust-to-zig](https://rtfeldman.com/rust-to-zig)

生成摘要时出错

---

## 75. Show HN: On-chain bond market where the issuers are AI agents

**原文标题**: Show HN: On-chain bond market where the issuers are AI agents

**原文链接**: [https://selbonds.now](https://selbonds.now)

生成摘要时出错

---

## 76. Inkling: Our Open-Weights Model

**原文标题**: Inkling: Our Open-Weights Model

**原文链接**: [https://thinkingmachines.ai/news/introducing-inkling/](https://thinkingmachines.ai/news/introducing-inkling/)

生成摘要时出错

---

## 77. If you want to create a button from scratch, you must first create the universe

**原文标题**: If you want to create a button from scratch, you must first create the universe

**原文链接**: [https://madcampos.dev/blog/2026/07/accessibility-from-scratch/](https://madcampos.dev/blog/2026/07/accessibility-from-scratch/)

生成摘要时出错

---

## 78. No liability exemption for Google in Italian YouTube spat, EU court says

**原文标题**: No liability exemption for Google in Italian YouTube spat, EU court says

**原文链接**: [https://www.reuters.com/world/eu-court-upholds-googles-854250-italian-fine-over-gambling-advertising-2026-07-16/](https://www.reuters.com/world/eu-court-upholds-googles-854250-italian-fine-over-gambling-advertising-2026-07-16/)

生成摘要时出错

---

## 79. Show HN: Leaves – A text-UI disk usage treemap visualizer

**原文标题**: Show HN: Leaves – A text-UI disk usage treemap visualizer

**原文链接**: [https://github.com/patonw/leaves](https://github.com/patonw/leaves)

生成摘要时出错

---

## 80. I Owe My Life to the Commodore 64

**原文标题**: I Owe My Life to the Commodore 64

**原文链接**: [https://www.goto10retro.com/p/i-owe-my-life-to-the-commodore-64](https://www.goto10retro.com/p/i-owe-my-life-to-the-commodore-64)

生成摘要时出错

---

## 81. CVE-2026-25089: FortiSandbox unauthenticated command injection added to CISA KEV

**原文标题**: CVE-2026-25089: FortiSandbox unauthenticated command injection added to CISA KEV

**原文链接**: [https://hellorecon.com/blog/cve-2026-25089](https://hellorecon.com/blog/cve-2026-25089)

生成摘要时出错

---

## 82. M 3.9 Experimental Explosion – 147 Km ENE of Ponce Inlet, Florida

**原文标题**: M 3.9 Experimental Explosion – 147 Km ENE of Ponce Inlet, Florida

**原文链接**: [https://earthquake.usgs.gov/earthquakes/eventpage/us7000t13l/executive](https://earthquake.usgs.gov/earthquakes/eventpage/us7000t13l/executive)

生成摘要时出错

---

## 83. How RCA Victor sold Sound Service to classrooms in 1939

**原文标题**: How RCA Victor sold Sound Service to classrooms in 1939

**原文链接**: [https://pncnmnp.github.io/blogs/rca-victor-education.html](https://pncnmnp.github.io/blogs/rca-victor-education.html)

生成摘要时出错

---

## 84. Bluesky Trademarks ATProto

**原文标题**: Bluesky Trademarks ATProto

**原文链接**: [https://atproto.com/blog/at-protocol-trademark](https://atproto.com/blog/at-protocol-trademark)

生成摘要时出错

---

## 85. Scaling to 1M concurrent sandboxes in seconds

**原文标题**: Scaling to 1M concurrent sandboxes in seconds

**原文链接**: [https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds)

生成摘要时出错

---

## 86. Guide to data tools landscape for developers

**原文标题**: Guide to data tools landscape for developers

**原文链接**: [https://sinja.io/blog/data-landscape-guide-for-developers](https://sinja.io/blog/data-landscape-guide-for-developers)

生成摘要时出错

---

## 87. Lingbot-map: A 3D foundation model for reconstructing scenes from streaming data

**原文标题**: Lingbot-map: A 3D foundation model for reconstructing scenes from streaming data

**原文链接**: [https://github.com/Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map)

生成摘要时出错

---

## 88. Reynard: A real Firefox web browser for iOS 13 or later

**原文标题**: Reynard: A real Firefox web browser for iOS 13 or later

**原文链接**: [https://github.com/minh-ton/reynard-browser](https://github.com/minh-ton/reynard-browser)

生成摘要时出错

---

## 89. The human-in-the-loop is tired

**原文标题**: The human-in-the-loop is tired

**原文链接**: [https://pydantic.dev/articles/the-human-in-the-loop-is-tired](https://pydantic.dev/articles/the-human-in-the-loop-is-tired)

生成摘要时出错

---

## 90. Timeline Scan – AI fixes the dates on your scanned photos

**原文标题**: Timeline Scan – AI fixes the dates on your scanned photos

**原文链接**: [https://timelinescan.com/](https://timelinescan.com/)

生成摘要时出错

---

## 91. Anthropic Thinks Its Own Success Is Key to Making AI Safe

**原文标题**: Anthropic Thinks Its Own Success Is Key to Making AI Safe

**原文链接**: [https://www.wired.com/story/anthropic-thinks-ai-can-only-be-safe-under-its-control/](https://www.wired.com/story/anthropic-thinks-ai-can-only-be-safe-under-its-control/)

生成摘要时出错

---

## 92. Win1998

**原文标题**: Win1998

**原文链接**: [https://win1998.com/](https://win1998.com/)

生成摘要时出错

---

## 93. I also filed the corners off my MacBook

**原文标题**: I also filed the corners off my MacBook

**原文链接**: [https://www.brt.fyi/posts/mac-book-filing/](https://www.brt.fyi/posts/mac-book-filing/)

生成摘要时出错

---

## 94. Agent-talk: Enabling coding agents to work together

**原文标题**: Agent-talk: Enabling coding agents to work together

**原文链接**: [https://github.com/xhluca/agent-talk](https://github.com/xhluca/agent-talk)

生成摘要时出错

---

## 95. How Should We Prepare Our Children for AI?

**原文标题**: How Should We Prepare Our Children for AI?

**原文链接**: [https://blog.comini.in/p/how-should-we-prepare-our-children](https://blog.comini.in/p/how-should-we-prepare-our-children)

生成摘要时出错

---

## 96. Making 768 servers look like 1

**原文标题**: Making 768 servers look like 1

**原文链接**: [https://planetscale.com/blog/making-768-servers-look-like-1](https://planetscale.com/blog/making-768-servers-look-like-1)

生成摘要时出错

---

## 97. After wearing the Pebble Time 2 for two weeks, I'll never buy another smartwatch

**原文标题**: After wearing the Pebble Time 2 for two weeks, I'll never buy another smartwatch

**原文链接**: [https://www.androidauthority.com/pebble-time-2-smartwatch-hands-on-3680077/](https://www.androidauthority.com/pebble-time-2-smartwatch-hands-on-3680077/)

生成摘要时出错

---

## 98. A Beautiful Theory Falls to Ugly Data

**原文标题**: A Beautiful Theory Falls to Ugly Data

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/05/a-beautiful-theory-falls-to-ugly-data.html](https://marginalrevolution.com/marginalrevolution/2026/05/a-beautiful-theory-falls-to-ugly-data.html)

生成摘要时出错

---

## 99. A Silly Adaptation of "The Odyssey"

**原文标题**: A Silly Adaptation of "The Odyssey"

**原文链接**: [https://economist.com/culture/2026/07/15/a-very-silly-adaptation-of-the-odyssey](https://economist.com/culture/2026/07/15/a-very-silly-adaptation-of-the-odyssey)

生成摘要时出错

---

## 100. CO2 overload, detected in human blood, suggests toxic atmosphere within 50 years

**原文标题**: CO2 overload, detected in human blood, suggests toxic atmosphere within 50 years

**原文链接**: [https://link.springer.com/article/10.1007/s11869-026-01918-5](https://link.springer.com/article/10.1007/s11869-026-01918-5)

生成摘要时出错

---

