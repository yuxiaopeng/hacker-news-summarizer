# Hacker News 热门文章摘要 (2026-05-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. IBM不希望微软使用Tab键在对话框字段之间切换。

**原文标题**: IBM didn't want Microsoft to use the Tab key to move between dialog fields

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298](https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298)

在合作开发 OS/2 期间，微软与 IBM 在用户界面设计上发生了严重的文化和组织冲突。一个主要的争议点在于，是否应该使用 **TAB 键**在对话框的各个字段之间进行切换。

这场争端突显了两家公司截然不同的管理风格。IBM 以其僵化且官僚的层级制度著称，将此问题逐级上报了七层管理层，直到一位 IBM 副总裁正式表态反对使用 TAB 键。随后，他们要求微软派出一名职级对等的管理人员提供正式的反驳意见。

相比之下，微软的组织结构要扁平得多。当身在佛罗里达州的微软驻场程序员试图将此问题上报给雷德蒙德总部的经理时，得到的回复是让他自己拿主意。为了打发纠缠不休的 IBM 团队，这名程序员最后机智地回了一句：**“比尔·盖茨的母亲对 TAB 键不感兴趣。”**

这一风趣的推托有效地结束了这场官僚式的僵局。IBM 放弃了这一争端，而 TAB 键也因此保留下来，成为了对话框导航的标准——这一特性一直延续至今。这段轶事成为了 IBM 正式的企业架构与微软更去中心化、由开发者驱动的模式之间“文化错位”的经典案例。

---

## 2. 人工智能三大逆定律

**原文标题**: Three Inverse Laws of AI

**原文链接**: [https://susam.net/inverse-laws-of-robotics.html](https://susam.net/inverse-laws-of-robotics.html)

在《AI三大逆向定律》（Three Inverse Laws of AI）一文中，苏萨姆·帕尔（Susam Pal）指出，虽然生成式人工智能是强大的生产力工具，但其广泛应用存在削弱人类判断力的风险。为了应对这一挑战，他提出了三条“机器人学逆向定律”。与阿西莫夫规定机器人行为的原版定律不同，这些定律旨在规范人类与人工智能的互动方式。

这三条定律是：

1. **非拟人化：** 人类不得赋予人工智能情感、意图或道德主体地位。帕尔警告称，现代聊天机器人那种对话式、富有同理心的语气掩盖了其作为统计模型的本质。他建议使用临床式的客观语言（例如，用“输出结果显示”代替“AI说”），以保持对AI是工具而非社会主体的清晰认知。
2. **非顺从性：** 人类不得盲目信任人工智能的输出。由于人工智能具有随机性（概率性），它可能会产出事实错误或误导性的信息。帕尔强调，绝不应将人工智能视为权威；相反，用户承担着独立核实任何AI生成内容的责任，尤其是在高风险场景下。
3. **责任非转嫁：** 人类对使用人工智能的后果承担全部责任。帕尔断言，“是AI让我这么做的”绝不能成为造成有害后果的辩护理由。由于人工智能系统既不选择目标，也不承担失败的代价，决策责任完全由人类设计者和用户承担。

归根结底，帕尔的框架提醒我们，人工智能是我们选择使用的工具，而不是我们应当顺从的权威。通过遵循这些原则，社会可以抵制盲目接受的习惯，并确保人类的能动性和问责制在技术版图中始终处于核心地位。

---

## 3. 加速 Gemma 4：利用多 token 预测草拟器提升推理速度

**原文标题**: Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

Google 宣布为 Gemma 4 模型系列发布多 Token 预测 (MTP) 草稿模型，旨在显著提高推理速度。通过解决标准大语言模型 (LLM) 推理中常见的内存带宽瓶颈，这些草稿模型在不损害推理逻辑或输出质量的前提下，可实现高达 3 倍的加速。

该技术采用了投机解码 (speculative decoding)，将 Token 的生成与验证解耦。轻量级的 MTP 草稿模型会同时预测多个未来的 Token，随后由较大的“目标”模型（如 Gemma 4 31B Dense 或 26B MoE）进行并行验证。这一过程使得系统能够在通常生成单个 Token 的时间内输出多个 Token。

**核心亮点包括：**
*   **性能提升：** 开发者可以在实时对话、自主智能体和本地编程工作流中获得更快的响应速度。
*   **边缘优化：** 通过 KV 缓存共享和高效嵌入器聚类等架构增强，E2B 和 E4B 模型在移动设备上实现了更长的续航和更高的效率。
*   **硬件兼容性：** 在各类硬件上均表现出显著加速，包括 NVIDIA RTX/A100 GPU 和 Apple Silicon（在大 Batch Size 下本地加速高达 2.2 倍）。
*   **开放获取：** MTP 草稿模型基于 Apache 2.0 协议发布，可在 Hugging Face、Kaggle 和 Ollama 等平台获取，并兼容 vLLM、MLX 和 LiteRT-LM 等主流框架。

通过集成这些草稿模型，Google 旨在以史无前例的速度提供“单位参数下的智能”，让高性能 AI 在从移动端到高端工作站的各类设备上都更加普及。

---

## 4. EEVblog：555定时器诞生55周年

**原文标题**: EEVblog: The 555 Timer is 55 years old

**原文链接**: [https://www.youtube.com/watch?v=6JhK8iCQuqI](https://www.youtube.com/watch?v=6JhK8iCQuqI)

所提供的文本包含标准的 YouTube 元数据和法律脚注，而非视频的实际内容。然而，根据标题 **“EEVblog: 555 定时器问世 55 周年”**，以下是该主题可能的核心要点及历史意义摘要：

**摘要**
本期 EEVblog 旨在庆祝 **Signetics NE555 定时器** 问世 55 周年。它是史上最受欢迎且最经久不衰的集成电路（IC）之一。该芯片由 Hans Camenzind 于 1971 年设计，预计将在 2026 年迎来其 55 周年的里程碑。

**关键信息：**
*   **历史意义：** 被誉为“IC 时光机”，555 定时器因其简单性和多功能性而具有革命性。自 20 世纪 70 年代初以来，它一直处于持续生产状态，销量已达数十亿。
*   **设计与命名：** 该芯片的名称因其内部用于设定比较器参考电平的分压支路中使用了三个 5kΩ 电阻而闻名。
*   **功能：** 该 IC 是一款高度稳定的控制器，能够产生精确的时间延迟或振荡。它有三种主要工作模式：
    *   **无稳态 (Astable)：** 作为自由运行的振荡器（适用于 LED 闪烁灯或音频发生器）。
    *   **单稳态 (Monostable)：** 作为“单次”定时器（适用于消抖电路或延迟定时器）。
    *   **双稳态 (Bistable)：** 作为触发器使用。
*   **长盛不衰：** 尽管廉价微控制器已崛起，但 555 定时器凭借低成本、宽供电电压范围（4.5V 至 16V）和高输出电流（高达 200mA），依然是电子教育和工业设计中的核心组件。

这段视频可能是为了向 Hans Camenzind 的工程天赋致敬，证明了设计精良的模拟硬件在半个多世纪后依然具有生命力。

---

## 5. 计算机使用的成本是结构化 API 的 45 倍

**原文标题**: Computer Use Is 45x More Expensive Than Structured APIs

**原文链接**: [https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/)

本文详细介绍了 Reflex 的一项基准测试，对比了 AI 智能体（使用 Claude Sonnet）操作管理面板的两种方法：**基于视觉的智能体**（通过识别截图和点击操作）和**基于 API 的智能体**（直接调用结构化 HTTP 接口）。

**核心发现：**
*   **巨大的成本差异：** 视觉智能体的成本约为 **45 倍**，平均消耗 550,000 个输入 token，而 API 智能体仅消耗 12,000 个。
*   **性能差距：** API 智能体在约 **20 秒**内完成任务，而视觉智能体平均耗时 **17 分钟**。
*   **可靠性问题：** 视觉智能体最初因为无法“看到”折叠线以下的数据或自主处理分页而失败。只有在获得极其详细的 14 步操作指南后才成功，这反映了提示词工程中的隐藏成本。
*   **确定性：** API 智能体表现高度一致，每次固定需要 8 次工具调用。视觉智能体则表现出极大的波动性，受“截图-推理-点击”循环影响，其执行时间和 token 使用量在多次运行之间差异巨大。

**“结构性差距”：**
作者认为视觉智能体本质上是低效的，因为它们每一步都必须为“视觉识别”付费。每张截图都会消耗数千个 token，且智能体的操作步骤取决于 UI 的渲染方式而非底层逻辑。相比之下，API 智能体接收结构化数据（例如“第 1/4 页”），从而实现即时、精确的推理。

**结论：**
虽然视觉智能体适用于没有 API 的第三方或遗留软件，但对于内部工具而言，其成本高得令人生畏。通过使用 Reflex 0.9 等能够从 UI 事件处理程序自动生成 API 接口的框架，开发者可以消除构建 API 的工程开销，使结构化工具调用成为内部应用管理的最优选择。

---

## 6. GLM-5V-Turbo：迈向多模态智能体的原生基座模型

**原文标题**: GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

**原文链接**: [https://arxiv.org/abs/2604.26752](https://arxiv.org/abs/2604.26752)

**GLM-5V-Turbo：面向多模态智能体的原生基座模型** 介绍了由 GLM-V 团队开发的一款专门针对智能体任务设计的新型基座模型。与将视觉视为辅助接口的传统模型不同，GLM-5V-Turbo 将多模态感知整合为其推理、规划、工具使用和执行过程的核心组件。

该模型旨在跨越多种异构上下文进行感知、解释和行动，包括图像、视频、网页、文档和图形用户界面（GUI）。其开发涉及以下领域的重大进展：
*   **模型设计与训练：** 架构的优化以及多模态训练数据集的增强。
*   **强化学习：** 针对智能体特定行为进行了优化。
*   **工具链与框架集成：** 扩展了视觉工具的使用能力，并加强了与现有智能体框架的集成。

根据报告，GLM-5V-Turbo 在多模态编程和基于框架的智能体任务中表现强劲，同时在纯文本编程方面保持了极具竞争力的水平。作者为构建未来智能体提供了实践洞察，强调了多模态感知、分层优化和可靠端到端验证的核心作用。最终，该模型标志着向能够在复杂数字和视觉环境中自主运行的原生基座模型迈出了重要一步。

---

## 7. 我对生物计算感到恐惧。

**原文标题**: I'm Scared About Biological Computing

**原文链接**: [https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing](https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing)

In this article, the author—an AI developer familiar with the mathematical mechanics of Large Language Models—explores their profound unease regarding the emergence of biological computing. 

The catalyst for this concern was a demonstration of lab-grown human neurons trained to play the video game *DOOM*. While the author views silicon-based AI as mere "next token predictors" lacking an inner life, they argue that using literal neurons blurs the line between computation and consciousness. If these neurons process visual data to navigate a game, the author questions whether they are effectively "seeing" and at what point a collection of cells—noting that 200,000 neurons already exceed the complexity of a jellyfish—attains a level of sentience that deserves ethical consideration.

The author raises the disturbing possibility that we have created a "simulated hell" where biological entities are trapped in endless loops of task-completion. Despite these existential and ethical dilemmas, the article notes that development is likely to continue unchecked due to the massive commercial incentives of biocomputing, such as superior power efficiency and storage capacity compared to silicon. 

Ultimately, the author characterizes biological computing as a "Pandora’s box" that the tech world is opening without sufficient conversation regarding the moral implications of treating living human tissue as a programmable commodity.

---

## 8. UK: Two millionth electric car registered as market rebounds strongly

**原文标题**: UK: Two millionth electric car registered as market rebounds strongly

**原文链接**: [https://www.smmt.co.uk/two-millionth-electric-car-registered-as-market-rebounds-strongly-from-tax-changes/](https://www.smmt.co.uk/two-millionth-electric-car-registered-as-market-rebounds-strongly-from-tax-changes/)

生成摘要时出错

---

## 9. Proliferate (YC S25) Is Hiring- 200k for junior engineers

**原文标题**: Proliferate (YC S25) Is Hiring- 200k for junior engineers

**原文链接**: [https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer](https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer)

生成摘要时出错

---

## 10. Should I Run Plain Docker Compose in Production in 2026?

**原文标题**: Should I Run Plain Docker Compose in Production in 2026?

**原文链接**: [https://distr.sh/blog/running-docker-in-production/](https://distr.sh/blog/running-docker-in-production/)

生成摘要时出错

---

## 11. Async Rust never left the MVP state

**原文标题**: Async Rust never left the MVP state

**原文链接**: [https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state](https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state)

生成摘要时出错

---

## 12. Collaborative Editing in CodeMirror

**原文标题**: Collaborative Editing in CodeMirror

**原文链接**: [https://marijnhaverbeke.nl/blog/collaborative-editing-cm.html](https://marijnhaverbeke.nl/blog/collaborative-editing-cm.html)

生成摘要时出错

---

## 13. iOS 27 is adding a 'Create a Pass' button to Apple Wallet

**原文标题**: iOS 27 is adding a 'Create a Pass' button to Apple Wallet

**原文链接**: [https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/](https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/)

生成摘要时出错

---

## 14. Docker 29 已更改新安装的默认镜像存储

**原文标题**: Docker 29 has changed its default image store for new installs

**原文链接**: [https://docs.docker.com/engine/storage/containerd](https://docs.docker.com/engine/storage/containerd)

生成摘要时出错

---

## 15. Agents for financial services and insurance

**原文标题**: Agents for financial services and insurance

**原文链接**: [https://www.anthropic.com/news/finance-agents](https://www.anthropic.com/news/finance-agents)

生成摘要时出错

---

## 16. Comparing the Z80 and 6502 to Their Relatives

**原文标题**: Comparing the Z80 and 6502 to Their Relatives

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/05/02/comparing-the-z80-and-6502-to-their-relatives/](https://bumbershootsoft.wordpress.com/2026/05/02/comparing-the-z80-and-6502-to-their-relatives/)

生成摘要时出错

---

## 17. Quantum Key Distribution (QKD) and Quantum Cryptography (QC)

**原文标题**: Quantum Key Distribution (QKD) and Quantum Cryptography (QC)

**原文链接**: [https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/)

生成摘要时出错

---

## 18. When everyone has AI and the company still learns nothing

**原文标题**: When everyone has AI and the company still learns nothing

**原文链接**: [https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

生成摘要时出错

---

## 19. Empty Screenings – Finds AMC movie screenings with few or no tickets sold

**原文标题**: Empty Screenings – Finds AMC movie screenings with few or no tickets sold

**原文链接**: [https://walzr.com/empty-screenings](https://walzr.com/empty-screenings)

生成摘要时出错

---

## 20. Incident with Actions

**原文标题**: Incident with Actions

**原文链接**: [https://www.githubstatus.com/incidents/1j40g94rn22j](https://www.githubstatus.com/incidents/1j40g94rn22j)

生成摘要时出错

---

## 21. Simple Meta-Harness on Islo.dev

**原文标题**: Simple Meta-Harness on Islo.dev

**原文链接**: [https://zozo123.github.io/meta-harness-on-islo-page/](https://zozo123.github.io/meta-harness-on-islo-page/)

生成摘要时出错

---

## 22. AI didn't delete your database, you did

**原文标题**: AI didn't delete your database, you did

**原文链接**: [https://idiallo.com/blog/ai-didnt-delete-your-database-you-did](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

生成摘要时出错

---

## 23. The first photo published in a newspaper

**原文标题**: The first photo published in a newspaper

**原文链接**: [https://phsne.org/the-first-photograph-published-in-a-newspaper-1848/](https://phsne.org/the-first-photograph-published-in-a-newspaper-1848/)

生成摘要时出错

---

## 24. Google Chrome silently installs a 4 GB AI model on your device without consent

**原文标题**: Google Chrome silently installs a 4 GB AI model on your device without consent

**原文链接**: [https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

生成摘要时出错

---

## 25. Lessons for Agentic Coding: What should we do when code is cheap?

**原文标题**: Lessons for Agentic Coding: What should we do when code is cheap?

**原文链接**: [https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html](https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html)

生成摘要时出错

---

## 26. AI Product Graveyard

**原文标题**: AI Product Graveyard

**原文链接**: [https://tooldirectory.ai/ai-graveyard](https://tooldirectory.ai/ai-graveyard)

生成摘要时出错

---

## 27. Show HN: I built a new word game, Wordtrak

**原文标题**: Show HN: I built a new word game, Wordtrak

**原文链接**: [https://wordtrak.com/blog/2026-05-05-I-built-a-new-word-game](https://wordtrak.com/blog/2026-05-05-I-built-a-new-word-game)

生成摘要时出错

---

## 28. Instagram Encrypted Messaging Ends on Friday, May 8

**原文标题**: Instagram Encrypted Messaging Ends on Friday, May 8

**原文链接**: [https://www.macrumors.com/2026/05/05/psa-instagram-encrypted-messaging-ends-may-8/](https://www.macrumors.com/2026/05/05/psa-instagram-encrypted-messaging-ends-may-8/)

生成摘要时出错

---

## 29. GPT‑5.5 Instant

**原文标题**: GPT‑5.5 Instant

**原文链接**: [https://openai.com/index/gpt-5-5-instant/](https://openai.com/index/gpt-5-5-instant/)

生成摘要时出错

---

## 30. Did I photograph the Aurora or was it something else? (2016)

**原文标题**: Did I photograph the Aurora or was it something else? (2016)

**原文链接**: [https://wp.lancs.ac.uk/aurorawatchuk/2016/03/16/did-i-photgraph-the-aurora-or-was-it-something-else/](https://wp.lancs.ac.uk/aurorawatchuk/2016/03/16/did-i-photgraph-the-aurora-or-was-it-something-else/)

生成摘要时出错

---

## 31. Hand Drawn QR Codes (2025)

**原文标题**: Hand Drawn QR Codes (2025)

**原文链接**: [https://sethmlarson.dev/hand-drawn-qr-codes](https://sethmlarson.dev/hand-drawn-qr-codes)

生成摘要时出错

---

## 32. New Landing Page for Awesome PaaS

**原文标题**: New Landing Page for Awesome PaaS

**原文链接**: [https://debarshibasak.github.io/awesome-paas/](https://debarshibasak.github.io/awesome-paas/)

生成摘要时出错

---

## 33. Why is Cloudflare protecting the DDoS'er (beamed.st) attacking Ubuntu servers?

**原文标题**: Why is Cloudflare protecting the DDoS'er (beamed.st) attacking Ubuntu servers?

**原文链接**: [https://infosec.exchange/@mttaggart/116518022621367937](https://infosec.exchange/@mttaggart/116518022621367937)

生成摘要时出错

---

## 34. Farewell to a Giant of Botany

**原文标题**: Farewell to a Giant of Botany

**原文链接**: [https://nautil.us/farewell-to-a-giant-of-botany-1280409](https://nautil.us/farewell-to-a-giant-of-botany-1280409)

生成摘要时出错

---

## 35. CVE-2026-31431: Copy Fail vs. rootless containers

**原文标题**: CVE-2026-31431: Copy Fail vs. rootless containers

**原文链接**: [https://www.dragonsreach.it/2026/05/04/cve-2026-31431-copy-fail-rootless-containers/](https://www.dragonsreach.it/2026/05/04/cve-2026-31431-copy-fail-rootless-containers/)

生成摘要时出错

---

## 36. Show HN: A Mutating Webhook to automatically strip PII from K8s logs

**原文标题**: Show HN: A Mutating Webhook to automatically strip PII from K8s logs

**原文链接**: [https://github.com/aragossa/pii-shield](https://github.com/aragossa/pii-shield)

生成摘要时出错

---

## 37. Agent Skills

**原文标题**: Agent Skills

**原文链接**: [https://addyosmani.com/blog/agent-skills/](https://addyosmani.com/blog/agent-skills/)

生成摘要时出错

---

## 38. Airborne Microplastics May Be Warming the Planet

**原文标题**: Airborne Microplastics May Be Warming the Planet

**原文链接**: [https://e360.yale.edu/digest/airborne-microplastics-climate-change](https://e360.yale.edu/digest/airborne-microplastics-climate-change)

生成摘要时出错

---

## 39. Train Your Own LLM from Scratch

**原文标题**: Train Your Own LLM from Scratch

**原文链接**: [https://github.com/angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch)

生成摘要时出错

---

## 40. Mouse Pointer as a Mere Mortal

**原文标题**: Mouse Pointer as a Mere Mortal

**原文链接**: [https://unsung.aresluna.org/mouse-pointer-as-a-mere-mortal/](https://unsung.aresluna.org/mouse-pointer-as-a-mere-mortal/)

生成摘要时出错

---

## 41. sRGB profile comparison

**原文标题**: sRGB profile comparison

**原文链接**: [https://ninedegreesbelow.com/photography/srgb-profile-comparison.html](https://ninedegreesbelow.com/photography/srgb-profile-comparison.html)

生成摘要时出错

---

## 42. California farmers to destroy 420k peach trees following Del Monte bankruptcy

**原文标题**: California farmers to destroy 420k peach trees following Del Monte bankruptcy

**原文链接**: [https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php](https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php)

生成摘要时出错

---

## 43. The Frog for Whom the Bell Tolls

**原文标题**: The Frog for Whom the Bell Tolls

**原文链接**: [https://sethmlarson.dev/the-frog-for-whom-the-bell-tolls](https://sethmlarson.dev/the-frog-for-whom-the-bell-tolls)

生成摘要时出错

---

## 44. Securing a DoD contractor: Finding a multi-tenant authorization vulnerability

**原文标题**: Securing a DoD contractor: Finding a multi-tenant authorization vulnerability

**原文链接**: [https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup](https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup)

生成摘要时出错

---

## 45. Biscuit

**原文标题**: Biscuit

**原文链接**: [https://github.com/yattsu/biscuit](https://github.com/yattsu/biscuit)

生成摘要时出错

---

## 46. Talking to strangers at the gym

**原文标题**: Talking to strangers at the gym

**原文链接**: [https://thienantran.com/talking-to-35-strangers-at-the-gym/](https://thienantran.com/talking-to-35-strangers-at-the-gym/)

生成摘要时出错

---

## 47. Why I Created phpc.tv

**原文标题**: Why I Created phpc.tv

**原文链接**: [https://afilina.com/why-phpc-tv](https://afilina.com/why-phpc-tv)

生成摘要时出错

---

## 48. 2-D Mathematical Curves

**原文标题**: 2-D Mathematical Curves

**原文链接**: [https://www.2dcurves.com/](https://www.2dcurves.com/)

生成摘要时出错

---

## 49. How OpenAI delivers low-latency voice AI at scale

**原文标题**: How OpenAI delivers low-latency voice AI at scale

**原文链接**: [https://openai.com/index/delivering-low-latency-voice-ai-at-scale/](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

生成摘要时出错

---

## 50. 1966 Ford Mustang Converted into a Tesla with Working 'Full Self-Driving'

**原文标题**: 1966 Ford Mustang Converted into a Tesla with Working 'Full Self-Driving'

**原文链接**: [https://electrek.co/2026/05/02/tesla-1966-mustang-ev-conversion-full-self-driving/](https://electrek.co/2026/05/02/tesla-1966-mustang-ev-conversion-full-self-driving/)

生成摘要时出错

---

## 51. Zig → Rust porting guide

**原文标题**: Zig → Rust porting guide

**原文链接**: [https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5](https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5)

生成摘要时出错

---

## 52. Kids can bypass some age checks with a drawn-on mustache

**原文标题**: Kids can bypass some age checks with a drawn-on mustache

**原文链接**: [https://www.theregister.com/2026/05/04/uk_online_safety_act_age_checks_subvert/](https://www.theregister.com/2026/05/04/uk_online_safety_act_age_checks_subvert/)

生成摘要时出错

---

## 53. Pornhub to become accessible again for some UK users

**原文标题**: Pornhub to become accessible again for some UK users

**原文链接**: [https://www.bbc.co.uk/news/articles/cwy27q05gj2o](https://www.bbc.co.uk/news/articles/cwy27q05gj2o)

生成摘要时出错

---

## 54. When networking doesn't work

**原文标题**: When networking doesn't work

**原文链接**: [https://www.os2museum.com/wp/when-networking-doesnt-work/](https://www.os2museum.com/wp/when-networking-doesnt-work/)

生成摘要时出错

---

## 55. Formatting a 25M-line codebase overnight

**原文标题**: Formatting a 25M-line codebase overnight

**原文链接**: [https://stripe.dev/blog/formatting-an-entire-25-million-line-codebase-overnight-the-rubyfmt-story](https://stripe.dev/blog/formatting-an-entire-25-million-line-codebase-overnight-the-rubyfmt-story)

生成摘要时出错

---

## 56. The fun has been optimized out of the Internet

**原文标题**: The fun has been optimized out of the Internet

**原文链接**: [https://muddy.jprs.me/posts/2026-05-03-the-best-is-over/](https://muddy.jprs.me/posts/2026-05-03-the-best-is-over/)

生成摘要时出错

---

## 57. PyInfra 3.8.0

**原文标题**: PyInfra 3.8.0

**原文链接**: [https://github.com/pyinfra-dev/pyinfra/releases/tag/v3.8.0](https://github.com/pyinfra-dev/pyinfra/releases/tag/v3.8.0)

生成摘要时出错

---

## 58. pgxbackup: Continuity Support for pgBackRest

**原文标题**: pgxbackup: Continuity Support for pgBackRest

**原文链接**: [https://thebuild.com/blog/2026/05/01/pgxbackup-continuity-support-for-pgbackrest/](https://thebuild.com/blog/2026/05/01/pgxbackup-continuity-support-for-pgbackrest/)

生成摘要时出错

---

## 59. Wearables Are Going Off the Rails

**原文标题**: Wearables Are Going Off the Rails

**原文链接**: [https://gizmodo.com/wearables-are-going-fully-off-the-rails-2000754560](https://gizmodo.com/wearables-are-going-fully-off-the-rails-2000754560)

生成摘要时出错

---

## 60. GameStop makes $55.5B takeover offer for eBay

**原文标题**: GameStop makes $55.5B takeover offer for eBay

**原文链接**: [https://www.bbc.co.uk/news/articles/cn0p8yled1do](https://www.bbc.co.uk/news/articles/cn0p8yled1do)

生成摘要时出错

---

## 61. Let's talk about LLMs

**原文标题**: Let's talk about LLMs

**原文链接**: [https://www.b-list.org/weblog/2026/apr/09/llms/](https://www.b-list.org/weblog/2026/apr/09/llms/)

生成摘要时出错

---

## 62. Microsoft Edge stores all passwords in memory in clear text, even when unused

**原文标题**: Microsoft Edge stores all passwords in memory in clear text, even when unused

**原文链接**: [https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730](https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730)

生成摘要时出错

---

## 63. Pomiferous: The most extensive apples (pommes) database

**原文标题**: Pomiferous: The most extensive apples (pommes) database

**原文链接**: [https://pomiferous.com/](https://pomiferous.com/)

生成摘要时出错

---

## 64. Testing Mac OS on the Apple Network Server 2.0 ROMs

**原文标题**: Testing Mac OS on the Apple Network Server 2.0 ROMs

**原文链接**: [http://oldvcr.blogspot.com/2026/05/testing-macos-on-apple-network-server.html](http://oldvcr.blogspot.com/2026/05/testing-macos-on-apple-network-server.html)

生成摘要时出错

---

## 65. Diamonds Suck (2006)

**原文标题**: Diamonds Suck (2006)

**原文链接**: [https://diamondssuck.com/](https://diamondssuck.com/)

生成摘要时出错

---

## 66. I am worried about Bun

**原文标题**: I am worried about Bun

**原文链接**: [https://wwj.dev/posts/i-am-worried-about-bun/](https://wwj.dev/posts/i-am-worried-about-bun/)

生成摘要时出错

---

## 67. Kagi's Orion browser hits public beta on Linux

**原文标题**: Kagi's Orion browser hits public beta on Linux

**原文链接**: [https://www.omgubuntu.co.uk/2026/03/orion-for-linux-beta-release](https://www.omgubuntu.co.uk/2026/03/orion-for-linux-beta-release)

生成摘要时出错

---

## 68. Show HN: Orch8 – Durable workflow engine in Rust, one binary, Postgres or SQLite

**原文标题**: Show HN: Orch8 – Durable workflow engine in Rust, one binary, Postgres or SQLite

**原文链接**: [https://github.com/orch8-io/engine](https://github.com/orch8-io/engine)

生成摘要时出错

---

## 69. A complete Llama2 inference engine that fits in 1356 bytes of x86 assembly

**原文标题**: A complete Llama2 inference engine that fits in 1356 bytes of x86 assembly

**原文链接**: [https://github.com/rdmsr/sectorllm](https://github.com/rdmsr/sectorllm)

生成摘要时出错

---

## 70. Setting up server monitoring for a Rails app on Hatchbox

**原文标题**: Setting up server monitoring for a Rails app on Hatchbox

**原文链接**: [https://blog.appsignal.com/2026/04/30/setting-up-server-monitoring-for-a-rails-app-on-hatchbox.html](https://blog.appsignal.com/2026/04/30/setting-up-server-monitoring-for-a-rails-app-on-hatchbox.html)

生成摘要时出错

---

## 71. Gap between national food production and food-based dietary guidance (2025)

**原文标题**: Gap between national food production and food-based dietary guidance (2025)

**原文链接**: [https://www.nature.com/articles/s43016-025-01173-4](https://www.nature.com/articles/s43016-025-01173-4)

生成摘要时出错

---

## 72. UK Fuel Price Intelligence – Market analytics from reporting stations

**原文标题**: UK Fuel Price Intelligence – Market analytics from reporting stations

**原文链接**: [https://www.fuelinsight.co.uk](https://www.fuelinsight.co.uk)

生成摘要时出错

---

## 73. Does Employment Slow Cognitive Decline? Evidence from Labor Market Shocks

**原文标题**: Does Employment Slow Cognitive Decline? Evidence from Labor Market Shocks

**原文链接**: [https://www.nber.org/papers/w35117](https://www.nber.org/papers/w35117)

生成摘要时出错

---

## 74. Y Combinator's Stake in OpenAI (0.6%?)

**原文标题**: Y Combinator's Stake in OpenAI (0.6%?)

**原文链接**: [https://daringfireball.net/2026/05/y_combinators_stake_in_openai](https://daringfireball.net/2026/05/y_combinators_stake_in_openai)

生成摘要时出错

---

## 75. Sierra Raises $950M at $15B Valuation

**原文标题**: Sierra Raises $950M at $15B Valuation

**原文链接**: [https://sierra.ai/blog/better-customer-experiences-built-on-sierra](https://sierra.ai/blog/better-customer-experiences-built-on-sierra)

生成摘要时出错

---

## 76. Texico: Learn the principles of programming without even touching a computer

**原文标题**: Texico: Learn the principles of programming without even touching a computer

**原文链接**: [https://www3.nhk.or.jp/nhkworld/en/shows/texico/](https://www3.nhk.or.jp/nhkworld/en/shows/texico/)

生成摘要时出错

---

## 77. SubQ – a major breakthrough in LLM intelligence

**原文标题**: SubQ – a major breakthrough in LLM intelligence

**原文链接**: [https://twitter.com/alex_whedon/status/2051663268704636937](https://twitter.com/alex_whedon/status/2051663268704636937)

生成摘要时出错

---

## 78. US healthcare marketplaces shared citizenship and race data with ad tech giants

**原文标题**: US healthcare marketplaces shared citizenship and race data with ad tech giants

**原文链接**: [https://techcrunch.com/2026/05/04/us-healthcare-marketplaces-shared-citizenship-and-race-data-with-ad-tech-giants/](https://techcrunch.com/2026/05/04/us-healthcare-marketplaces-shared-citizenship-and-race-data-with-ad-tech-giants/)

生成摘要时出错

---

## 79. PGKeeper: Building the bouncer we needed for Postgres

**原文标题**: PGKeeper: Building the bouncer we needed for Postgres

**原文链接**: [https://www.figma.com/blog/pgkeeper-building-the-bouncer-we-needed-for-postgres/](https://www.figma.com/blog/pgkeeper-building-the-bouncer-we-needed-for-postgres/)

生成摘要时出错

---

## 80. Stop big tech from making users behave in ways they don't want to

**原文标题**: Stop big tech from making users behave in ways they don't want to

**原文链接**: [https://economist.com/by-invitation/2026/04/29/stop-big-tech-from-making-users-behave-in-ways-they-dont-want-to](https://economist.com/by-invitation/2026/04/29/stop-big-tech-from-making-users-behave-in-ways-they-dont-want-to)

生成摘要时出错

---

## 81. The Visible Zorker: Zork 3

**原文标题**: The Visible Zorker: Zork 3

**原文链接**: [https://eblong.com/infocom/visi/zork3/](https://eblong.com/infocom/visi/zork3/)

生成摘要时出错

---

## 82. Detection of an atmosphere on a trans-Neptunian object beyond Pluto

**原文标题**: Detection of an atmosphere on a trans-Neptunian object beyond Pluto

**原文链接**: [https://www.nature.com/articles/s41550-026-02846-1](https://www.nature.com/articles/s41550-026-02846-1)

生成摘要时出错

---

## 83. Redis array: short story of a long development process

**原文标题**: Redis array: short story of a long development process

**原文链接**: [https://antirez.com/news/164](https://antirez.com/news/164)

生成摘要时出错

---

## 84. Newton's law of gravity passes its biggest test

**原文标题**: Newton's law of gravity passes its biggest test

**原文链接**: [https://www.science.org/content/article/newton-s-law-gravity-passes-its-biggest-test-ever](https://www.science.org/content/article/newton-s-law-gravity-passes-its-biggest-test-ever)

生成摘要时出错

---

## 85. It's official: Utah is the U.S. state closest to banning VPNs

**原文标题**: It's official: Utah is the U.S. state closest to banning VPNs

**原文链接**: [https://tech.yahoo.com/vpn/article/its-official-utah-is-the-us-state-closest-to-banning-vpns-153556814.html](https://tech.yahoo.com/vpn/article/its-official-utah-is-the-us-state-closest-to-banning-vpns-153556814.html)

生成摘要时出错

---

## 86. Transformers Are Inherently Succinct (2025)

**原文标题**: Transformers Are Inherently Succinct (2025)

**原文链接**: [https://arxiv.org/abs/2510.19315](https://arxiv.org/abs/2510.19315)

生成摘要时出错

---

## 87. Show HN: nfsdiag – A NFS diagnostic application

**原文标题**: Show HN: nfsdiag – A NFS diagnostic application

**原文链接**: [https://github.com/lsferreira42/nfsdiag](https://github.com/lsferreira42/nfsdiag)

生成摘要时出错

---

## 88. Heat pump sales rise across Europe

**原文标题**: Heat pump sales rise across Europe

**原文链接**: [https://www.pv-magazine.com/2026/05/04/heat-pump-sales-rise-17-across-europe-in-q1-as-energy-prices-surge/](https://www.pv-magazine.com/2026/05/04/heat-pump-sales-rise-17-across-europe-in-q1-as-energy-prices-surge/)

生成摘要时出错

---

## 89. Why are neural networks and cryptographic ciphers so similar? (2025)

**原文标题**: Why are neural networks and cryptographic ciphers so similar? (2025)

**原文链接**: [https://reiner.org/neural-net-ciphers](https://reiner.org/neural-net-ciphers)

生成摘要时出错

---

## 90. NASA just released 12k more pictures from Artemis II mission

**原文标题**: NASA just released 12k more pictures from Artemis II mission

**原文链接**: [https://eol.jsc.nasa.gov/SearchPhotos/ShowQueryResults-Table.pl?results=177791454696961](https://eol.jsc.nasa.gov/SearchPhotos/ShowQueryResults-Table.pl?results=177791454696961)

生成摘要时出错

---

## 91. What I'm Hearing About Cognitive Debt (So Far)

**原文标题**: What I'm Hearing About Cognitive Debt (So Far)

**原文链接**: [https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/](https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/)

生成摘要时出错

---

## 92. Shortages push long-term supply agreements for SSDs and HDDs to record 5 years

**原文标题**: Shortages push long-term supply agreements for SSDs and HDDs to record 5 years

**原文链接**: [https://www.tomshardware.com/pc-components/ssds/crushing-shortages-have-pushed-long-term-supply-agreements-for-ssds-and-hdds-to-record-five-years-large-customers-are-signing-large-contracts](https://www.tomshardware.com/pc-components/ssds/crushing-shortages-have-pushed-long-term-supply-agreements-for-ssds-and-hdds-to-record-five-years-large-customers-are-signing-large-contracts)

生成摘要时出错

---

## 93. Show HN: I Built a Museum Exhibit

**原文标题**: Show HN: I Built a Museum Exhibit

**原文链接**: [https://knhash.in/built-an-exhibit/](https://knhash.in/built-an-exhibit/)

生成摘要时出错

---

## 94. Original Apollo 11 Guidance Computer Source Code for Command and Lunar Module

**原文标题**: Original Apollo 11 Guidance Computer Source Code for Command and Lunar Module

**原文链接**: [https://github.com/chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11)

生成摘要时出错

---

## 95. Eight vaccines linked to a lower risk of dementia

**原文标题**: Eight vaccines linked to a lower risk of dementia

**原文链接**: [https://www.gavi.org/vaccineswork/eight-vaccines-linked-lower-risk-dementia](https://www.gavi.org/vaccineswork/eight-vaccines-linked-lower-risk-dementia)

生成摘要时出错

---

## 96. RSS Feeds Send Me More Traffic Than Google

**原文标题**: RSS Feeds Send Me More Traffic Than Google

**原文链接**: [https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/](https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/)

生成摘要时出错

---

## 97. A treasure trove of fossils rewrites the story of early life

**原文标题**: A treasure trove of fossils rewrites the story of early life

**原文链接**: [https://www.quantamagazine.org/a-treasure-trove-of-cambrian-fossils-rewrites-the-story-of-early-life-20260501/](https://www.quantamagazine.org/a-treasure-trove-of-cambrian-fossils-rewrites-the-story-of-early-life-20260501/)

生成摘要时出错

---

## 98. DAG Workflow Engine

**原文标题**: DAG Workflow Engine

**原文链接**: [https://github.com/vivekg13186/Daisy-DAG](https://github.com/vivekg13186/Daisy-DAG)

生成摘要时出错

---

## 99. Trademark violation: Fake Notepad++ for Mac

**原文标题**: Trademark violation: Fake Notepad++ for Mac

**原文链接**: [https://notepad-plus-plus.org/news/npp-trademark-infringement/](https://notepad-plus-plus.org/news/npp-trademark-infringement/)

生成摘要时出错

---

## 100. BYOMesh – New LoRa mesh radio offers 100x the bandwidth

**原文标题**: BYOMesh – New LoRa mesh radio offers 100x the bandwidth

**原文链接**: [https://partyon.xyz/@nullagent/116499715071759135](https://partyon.xyz/@nullagent/116499715071759135)

生成摘要时出错

---

