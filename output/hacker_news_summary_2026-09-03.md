# Hacker News 热门文章摘要 (2026-09-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Qwen 3.8 27B 现已上线 Cerebras，速度达 1500 tokens/s

**原文标题**: Qwen 3.8 27B available on Cerebras at 1500 tokens/s

**原文链接**: [https://inference-docs.cerebras.ai/models/overview](https://inference-docs.cerebras.ai/models/overview)

Cerebras 宣布在其公共 API 端点上推出 **Qwen 3.8 27B** 模型，可实现约每秒 **1,500 个 token** 的高速推理。该模型拥有 270 亿个参数，为免费用户提供 64k 的上下文窗口，为按需付费层级提供 128k 的窗口。

公告的关键细节包括：

*   **模型完整性：** Cerebras 强调其公共端点上的所有模型均为原始、未剪枝的版本。尽管公司在进行剪枝研究（例如其 REAP —— 路由器加权专家激活剪枝技术），但这些修改后的模型仅发布在 Hugging Face 上用于研究，并未应用于生产环境 API。
*   **选择性量化：** 为保持高质量，Cerebras 仅针对存储使用权重量化（4 位、8 位或 16 位）。在推理过程中，权重会进行实时反量化，以确保激活、注意力和 KV 缓存始终保持全精度。
*   **服务层级：** 用户可通过免费试用和按需付费层级访问该模型，并受速率限制。对于需要更高吞吐量、预留容量或生产级服务等级协议（SLA）的用户，Cerebras 提供专用端点。
*   **透明度：** Cerebras 保证在未提前通知的情况下不会更改模型架构。未来任何压缩或剪枝版本都将托管在独立且标识清晰的端点上，以确保开发者能够完全控制其使用的模型版本。

此次更新扩展了 Cerebras 的产品组合，其中还包括运行速度约为每秒 3,000 个 token 的 120B 参数 GPT OSS 等更大型号的模型。

---

## 2. GPT-6 Astra

**原文标题**: GPT-6 Astra

**原文链接**: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)

无法访问文章链接。

---

## 3. 名称 终止

**原文标题**: .name Termination

**原文链接**: [https://neil.fraser.name/news/2026/09/03/](https://neil.fraser.name/news/2026/09/03/)

在这篇文章中，尼尔·弗雷泽（Neil Fraser）讨论了“.name”注册局即将终止三级域名服务的问题。他解释说，在运营了近二十五年后，威瑞信（Verisign）提议移除这些域名以简化其管理流程，这一提议近期已获得 ICANN 的批准。

作者强调了该决定带来的几个严重后果，受影响的用户约有 22,000 名。由于这些域名是长期运营的网站、电子邮件地址和物联网（IoT）设备配置的基础，其突然移除将导致重大的数字混乱。除了个人网络存在的丧失外，弗雷泽还强调了一个重大的安全风险：一旦这些三级域名被注销，底层的二级域名可能会开放给他人注册。这可能允许新所有者重建旧地址，从而劫持敏感账户或拦截私人通信。

弗雷泽对威瑞信表示了深度的不信任，指责该公司向 ICANN 提供误导性信息以确保提案获得通过。尽管他已经预付了直至 2040 年的域名注册费用，但他仍面临数字身份彻底消失的局面。文章最后，作者表示他打算寻求法律咨询，以对这一决定发起挑战。

---

## 4. K2 Horizon：由六个开放模型组成的互联系列

**原文标题**: K2 Horizon: A connected fleet of six open models

**原文链接**: [https://ifm.ai/blog/k2/](https://ifm.ai/blog/k2/)

IFM 发布了 K2 Horizon，这是一个包含六款开源 AI 模型的模型族，参数规模从 0.9B 到 375B 不等。此次发布的独特之处在于其“完全开源”的方式：不仅开源了模型权重，还根据 Apache 2.0 协议公开了整个训练生命周期，包括中间检查点、训练数据配方、代码和细粒度日志。

该系列模型在多个规模上都表现出了顶尖性能：
*   **小规模：** 0.9B、3.7B 和 7B 模型在同尺寸级别中树立了新的性能标杆（SOTA），尤其是在推理和数学领域。
*   **架构创新：** 36B-A4B 模型引入了值注意力混合（MoVA）架构，这种稀疏架构使其能以仅 4B 的激活参数实现接近 32B 模型的性能。
*   **企业级实力：** 375B-A23B 模型是该系列中能力最强的模型，专为高难度的推理和软件工程任务而设计。

K2 Horizon 的核心支柱是其**对智能体化（Agentic）的关注**。它是首个公开了智能体化后训练完整开发过程的开源模型族，让研究人员能够深入研究工具调用和规划能力是如何生成的。这些模型在高达 22 万亿 token 的数据上进行了训练，其中近 17% 的预训练语料由显式推理轨迹组成。

为了提升部署体验，IFM 还推出了 **Uno Diffusion** 技术，通过更高效的 token 生成方式提供无损推理加速，且不会降低质量。凭借统一的架构和词表，K2 Horizon 为开发者提供了一个一致的框架，支持从智能手表等边缘设备到企业级工作站的应用扩展。

---

## 5. 任何曾活过的人——从古往今来所有人中随机抽取的一个生命

**原文标题**: Any Human Ever – One life, drawn at random from all who have ever lived

**原文链接**: [https://anyhumanever.com/](https://anyhumanever.com/)

**《曾活在世上的每一个人》**（Any Human Ever）是一个交互式数据驱动项目，允许用户从估计曾活在世上的 1000 亿人中随机抽取一个生命。通过利用历史数据和统计概率，该工具为跨越时空的人类体验提供了一个具有代表性的缩影。

选择过程分为三个不同的步骤：

1. **时间：** 用户抽取一个出生年份。该项目指出，由于人口的指数级增长，真正的随机抽取落在近现代的可能性远高于古代。
2. **地点：** 用户抽取一个地理位置。其概率根据人口密度进行加权，这意味着抽取结果更有可能落在历史上人口更稠密的“明亮集群”中。
3. **生命：** 最后，该工具会根据所选的时代和地点，生成一个具体的生命轨迹和故事。

该项目是一项旨在理解人口统计数据的统计练习，将关注点从著名的历史人物转向了构成人类历史绝大多数的“普通”个体。它强调了人类的规模，并利用真实数据将每一个随机生成的“故事”植根于历史现实之中。

---

## 6. 将我 1993 年的 Amiga 游戏移植到 Godot，利用大模型解读 68000 汇编代码

**原文标题**: Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

**原文链接**: [https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/)

本文详细记录了作者利用大语言模型（Claude）将其1993年的Amiga游戏《巴比伦孪生子》（Babylonian Twins）移植到 Godot 引擎的经历。这款游戏最初在遭受严厉制裁的巴格达开发，由超过 7.2 万行纯 68000 汇编语言编写，通过绕过操作系统直接驱动 Amiga 硬件运行。

作者为 LLM 设定了三个主要目标：移植 2010 年的 C++ 版本、重构 1993 年的原始汇编代码，并将两者整合。LLM 的表现具有变革意义：它仅用一个晚上就将 3.4 万行的 C++ 引擎移植到了 Godot 中的可运行状态，并成功破解了无注释的汇编代码，重新生成了与 1993 年原始发布版逐字节一致的二进制文件。

技术亮点包括：
*   **解析陈旧格式：** LLM 通过分析汇编程序读取和屏蔽数据位的方式，逆向工程了私有关卡格式和“隐形物理”（碰撞标志）。
*   **保留游戏“手感”：** 为了维持原汁原味的游戏体验，作者保留了不同的刻率（Amiga 版为 50Hz，现代版为 60Hz），并使用了原始的自定义碰撞逻辑，而非 Godot 内置的物理引擎。
*   **验证：** LLM 实现了工具链的自动化，利用现代汇编器和模拟器，结合原始代码和像素级精确的关卡截图来验证移植的准确性。

最后，作者指出，LLM 理清三十年前针对特定硬件的复杂代码的速度和准确度都超过了人类，不仅解决了关于游戏逻辑的历史疑问，还以极高的精度保存了一段伊拉克的游戏历史。

---

## 7. 风投不再是风投了

**原文标题**: VC isn't VC anymore

**原文链接**: [https://www.anildash.com/2026/09/02/cancer-capital/](https://www.anildash.com/2026/09/02/cancer-capital/)

In "VC isn’t VC anymore," tech executive Anil Dash argues that traditional venture capital has been supplanted by "Cancer Capital"—an unaccountable oligarchy driven by billionaire extremists. Dash contends that the industry has shifted from a high-risk funding model for innovation into a predatory system that prioritizes political power and wealth concentration over market success.

Dash highlights several key shifts:

*   **Insulation from Risk:** Large "do-everything" firms manage tens of billions of dollars. By collecting massive management fees (e.g., 2% of a $50 billion fund), these firms profit immensely regardless of whether their portfolio companies succeed or fail.
*   **Regulatory Evasion and Self-Dealing:** These firms have restructured to bypass traditional VC regulations. This allows them to engage in self-dealing—such as selling assets between their own funds—and cashing out long before a company becomes profitable or goes public.
*   **Shifted Power Dynamics:** The relationship between founders and investors has flipped. Dash asserts that many VCs now prioritize extremist political manifestos, selecting founders as mere agents to carry out those agendas rather than supporting independent innovation.
*   **Public Burden:** Modern VC funds increasingly draw from pension funds and retail retirement accounts, meaning the general public bears the financial risk while the "Cancer Capitalists" reap the rewards.
*   **Political Infiltration:** Dash points to firms like Andreessen Horowitz (a16z) as prime examples of this shift, noting their status as some of the largest political donors in the U.S. He argues they use their wealth to aggressively influence AI and crypto policy across both political parties.

Dash concludes that modern venture capital is no longer a financial engine for startups, but a social and political machine focused on dismantling democracy and civil society.

---

## 8. Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%

**原文标题**: Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%

**原文链接**: [https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california)

生成摘要时出错

---

## 9. Gloria Steinem has died

**原文标题**: Gloria Steinem has died

**原文链接**: [https://www.theguardian.com/books/2026/sep/03/gloria-steinem-groundbreaking-feminist-campaigner-dies-aged-92](https://www.theguardian.com/books/2026/sep/03/gloria-steinem-groundbreaking-feminist-campaigner-dies-aged-92)

美国先驱女权主义者、记者兼活动家格洛丽亚·斯泰纳姆（Gloria Steinem）逝世，享年92岁。她在亲友的陪伴下，于纽约市的家中安详离世。

斯泰纳姆在20世纪60和70年代声名鹊起，成为妇女解放运动的领军人物。她的职业生涯致力于通过严谨的新闻报道和公众演讲，将女权主义视角带入主流社会。其职业生涯的亮点包括：对“花花公子兔女郎”待遇著名的卧底揭露、共同创办《女士》（Ms.）杂志，以及创造了“生育自由”一词。

她的社会活动超出了性别平等的范畴：她曾参与反对越战和海湾战争，支持“黑人权力”和“黑人的命也是命”运动，并倡导LGBTQ+权利。她经常强调性别与种族的交织性，认为这两种形式的压迫密不可分。

尽管被许多人奉为英雄，斯泰纳姆也是一个极具争议的人物。批评者有时认为，由于她的种族和外貌，媒体给予了其领导地位优先关注。她还曾因1998年撰文为面临性骚扰指控的比尔·克林顿辩护，以及早期被认为敌视跨性别权利的言论而遭到抵制——她后来对这些立场进行了回应或澄清。

晚年的斯泰纳姆依然是唐纳德·特朗普的著名批评者，并担任了2017年女性大游行的共同主席。她致力于平等事业直至生命尽头，留下了九部著作和近一个世纪的社会活动遗产。她的亲属包括继子、演员克里斯蒂安·贝尔。来自希拉里·克林顿等人士的哀悼高度评价了她的乐观精神，以及她让他人感到被关注与倾听的独特能力。

---

## 10. Gooseworks (YC W23) 招聘：创始创意工程师

**原文标题**: Gooseworks (YC W23) Is Hiring – Founding Creative Engineer

**原文链接**: [https://www.ycombinator.com/companies/gooseworks/jobs/rfgY8La-founding-creative-engineer](https://www.ycombinator.com/companies/gooseworks/jobs/rfgY8La-founding-creative-engineer)

生成摘要时出错

---

## 11. Unusual Suspects

**原文标题**: Unusual Suspects

**原文链接**: [https://neal.fun/unusual-suspects/](https://neal.fun/unusual-suspects/)

生成摘要时出错

---

## 12. Static Allocation, Constant Work

**原文标题**: Static Allocation, Constant Work

**原文链接**: [https://matklad.github.io/2026/09/02/static-allocation-constant-work.html](https://matklad.github.io/2026/09/02/static-allocation-constant-work.html)

生成摘要时出错

---

## 13. How concerned should we be about Astra's recurrent architecture?

**原文标题**: How concerned should we be about Astra's recurrent architecture?

**原文链接**: [https://www.lesswrong.com/posts/PLisnSFir8y5AHkmP/how-concerned-should-we-be-about-astra-s-recurrent](https://www.lesswrong.com/posts/PLisnSFir8y5AHkmP/how-concerned-should-we-be-about-astra-s-recurrent)

生成摘要时出错

---

## 14. The true horror of Edgar Allan Poe’s stories lies in their confessions

**原文标题**: The true horror of Edgar Allan Poe’s stories lies in their confessions

**原文链接**: [https://yalereview.org/article/emily-ogden-edgar-allan-poe](https://yalereview.org/article/emily-ogden-edgar-allan-poe)

生成摘要时出错

---

## 15. Audacity 4.0

**原文标题**: Audacity 4.0

**原文链接**: [https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0)

生成摘要时出错

---

## 16. GPS glitched across the US by as much as 33 feet

**原文标题**: GPS glitched across the US by as much as 33 feet

**原文链接**: [https://www.sciencealert.com/gps-glitched-across-the-us-by-as-much-as-33-feet-scientists-have-never-seen-this-before](https://www.sciencealert.com/gps-glitched-across-the-us-by-as-much-as-33-feet-scientists-have-never-seen-this-before)

生成摘要时出错

---

## 17. “We want it to really confuse people, but also really make people happy”

**原文标题**: “We want it to really confuse people, but also really make people happy”

**原文链接**: [https://unsung.aresluna.org/we-want-it-to-really-confuse-people-but-also-really-make-people-happy/](https://unsung.aresluna.org/we-want-it-to-really-confuse-people-but-also-really-make-people-happy/)

生成摘要时出错

---

## 18. Google Antigravity TOS: 3rd party usage can get Google account suspended

**原文标题**: Google Antigravity TOS: 3rd party usage can get Google account suspended

**原文链接**: [https://twitter.com/GergelyOrosz/status/2095453567955968398](https://twitter.com/GergelyOrosz/status/2095453567955968398)

生成摘要时出错

---

## 19. How to get a free .arpa domain

**原文标题**: How to get a free .arpa domain

**原文链接**: [https://hawksley.dev/blog/get-free-arpa-domain](https://hawksley.dev/blog/get-free-arpa-domain)

生成摘要时出错

---

## 20. Unified Arabic

**原文标题**: Unified Arabic

**原文链接**: [https://worksthatwork.com/6/unified-arabic](https://worksthatwork.com/6/unified-arabic)

生成摘要时出错

---

## 21. A thousand years older than Stonehenge: Archaeologists explore a Czech sanctuary

**原文标题**: A thousand years older than Stonehenge: Archaeologists explore a Czech sanctuary

**原文链接**: [https://info.zcu.cz/clanek.jsp?id=9882&lang=en](https://info.zcu.cz/clanek.jsp?id=9882&lang=en)

生成摘要时出错

---

## 22. Polars 2.0 预发布

**原文标题**: Pre-Release of Polars 2.0

**原文链接**: [https://pola.rs/posts/announcing-polars-2/](https://pola.rs/posts/announcing-polars-2/)

生成摘要时出错

---

## 23. Astronomers Detect a 10-Sided Structure in Saturn's Atmosphere

**原文标题**: Astronomers Detect a 10-Sided Structure in Saturn's Atmosphere

**原文链接**: [https://www.sciencealert.com/astronomers-spot-an-uncannily-geometric-10-sided-structure-in-saturns-atmosphere](https://www.sciencealert.com/astronomers-spot-an-uncannily-geometric-10-sided-structure-in-saturns-atmosphere)

生成摘要时出错

---

## 24. Go grandmaster Shin defeats AI KataGo with a two-stone handicap

**原文标题**: Go grandmaster Shin defeats AI KataGo with a two-stone handicap

**原文链接**: [https://www.kedglobal.com/artificial-intelligence/newsView/ked202607210007](https://www.kedglobal.com/artificial-intelligence/newsView/ked202607210007)

生成摘要时出错

---

## 25. My practical approach to surfing the web safely

**原文标题**: My practical approach to surfing the web safely

**原文链接**: [https://molily.de/safe-websurfing/](https://molily.de/safe-websurfing/)

生成摘要时出错

---

## 26. GPT-6-Astra: infinitely pairs of consecutive primes with distance at most 186

**原文标题**: GPT-6-Astra: infinitely pairs of consecutive primes with distance at most 186

**原文链接**: [https://github.com/openai/PrimeGaps186](https://github.com/openai/PrimeGaps186)

生成摘要时出错

---

## 27. The browser's main thread is expensive

**原文标题**: The browser's main thread is expensive

**原文链接**: [https://kciter.so/posts/the-expensive-main-thread/en/](https://kciter.so/posts/the-expensive-main-thread/en/)

生成摘要时出错

---

## 28. The asteroid currently hitting front end web development

**原文标题**: The asteroid currently hitting front end web development

**原文链接**: [https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/](https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/)

生成摘要时出错

---

## 29. OpenAI begins rolling out GPT-6 Astra

**原文标题**: OpenAI begins rolling out GPT-6 Astra

**原文链接**: [https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)

生成摘要时出错

---

## 30. Nvidia to acquire Hugging Face

**原文标题**: Nvidia to acquire Hugging Face

**原文链接**: [https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html)

生成摘要时出错

---

## 31. Old Directions: Reviving the spirit of revival

**原文标题**: Old Directions: Reviving the spirit of revival

**原文链接**: [https://www.nplusonemag.com/issue-54/the-intellectual-situation/old-directions/](https://www.nplusonemag.com/issue-54/the-intellectual-situation/old-directions/)

生成摘要时出错

---

## 32. Usbsid-Pico: Bridging Real Commodore 64 Sound to Modern USB

**原文标题**: Usbsid-Pico: Bridging Real Commodore 64 Sound to Modern USB

**原文链接**: [https://smallrun.net/blog/loud/usbsid-pico-sids-on-usb](https://smallrun.net/blog/loud/usbsid-pico-sids-on-usb)

生成摘要时出错

---

## 33. Invisible Companies

**原文标题**: Invisible Companies

**原文链接**: [https://colossus.com/article/invisible-companies/](https://colossus.com/article/invisible-companies/)

生成摘要时出错

---

## 34. How to bring up the Linux Kernel on a new platform

**原文标题**: How to bring up the Linux Kernel on a new platform

**原文链接**: [https://werwolv.net/posts/linux_bringup/](https://werwolv.net/posts/linux_bringup/)

生成摘要时出错

---

## 35. What I learned from my mom (1941-2026)

**原文标题**: What I learned from my mom (1941-2026)

**原文链接**: [https://experimentalliving.substack.com/p/what-i-learned-from-my-mom-1941-2026](https://experimentalliving.substack.com/p/what-i-learned-from-my-mom-1941-2026)

生成摘要时出错

---

## 36. Parque Arqueológico do Solstício

**原文标题**: Parque Arqueológico do Solstício

**原文链接**: [https://en.wikipedia.org/wiki/Parque_Arqueol%C3%B3gico_do_Solst%C3%ADcio](https://en.wikipedia.org/wiki/Parque_Arqueol%C3%B3gico_do_Solst%C3%ADcio)

生成摘要时出错

---

## 37. The Double Matthew Walker Knot by Fable 5.1

**原文标题**: The Double Matthew Walker Knot by Fable 5.1

**原文链接**: [https://claude.ai/public/artifacts/06fd26a5-403c-47c8-af49-dcf6c35ec55c](https://claude.ai/public/artifacts/06fd26a5-403c-47c8-af49-dcf6c35ec55c)

生成摘要时出错

---

## 38. Three schoolgirls in Kinsale pulled up a pea plant covered in warts (2014)

**原文标题**: Three schoolgirls in Kinsale pulled up a pea plant covered in warts (2014)

**原文链接**: [https://www.yahoo.com/news/16-old-girls-win-google-science-fair-simple-194434703.html](https://www.yahoo.com/news/16-old-girls-win-google-science-fair-simple-194434703.html)

生成摘要时出错

---

## 39. Intrusive linked lists (2019)

**原文标题**: Intrusive linked lists (2019)

**原文链接**: [https://www.data-structures-in-practice.com/intrusive-linked-lists/](https://www.data-structures-in-practice.com/intrusive-linked-lists/)

生成摘要时出错

---

## 40. GPT-6 Astra System Card

**原文标题**: GPT-6 Astra System Card

**原文链接**: [https://deploymentsafety.openai.com/gpt-6-astra](https://deploymentsafety.openai.com/gpt-6-astra)

生成摘要时出错

---

## 41. 120 days until Google restricts side-loading, declaring war on Android freedom

**原文标题**: 120 days until Google restricts side-loading, declaring war on Android freedom

**原文链接**: [https://tuta.com/blog/android-side-load-apps-google](https://tuta.com/blog/android-side-load-apps-google)

生成摘要时出错

---

## 42. New York Times and The Athletic workers demand company scrap Kalshi deal

**原文标题**: New York Times and The Athletic workers demand company scrap Kalshi deal

**原文链接**: [https://newsguild.org/new-york-times-and-the-athletic-workers-demand-company-scrap-kalshi-deal/](https://newsguild.org/new-york-times-and-the-athletic-workers-demand-company-scrap-kalshi-deal/)

生成摘要时出错

---

## 43. The paradox of diffusion distillation (2024)

**原文标题**: The paradox of diffusion distillation (2024)

**原文链接**: [https://sander.ai/2024/02/28/paradox.html](https://sander.ai/2024/02/28/paradox.html)

生成摘要时出错

---

## 44. My BC-250 Journey (With 40 CUs Unlocked)

**原文标题**: My BC-250 Journey (With 40 CUs Unlocked)

**原文链接**: [https://worldofmatthew.com/blog/bc250/](https://worldofmatthew.com/blog/bc250/)

生成摘要时出错

---

## 45. Fish bad, sugar good, and other medieval ideas about food

**原文标题**: Fish bad, sugar good, and other medieval ideas about food

**原文链接**: [https://lithub.com/fish-bad-sugar-good-and-other-medieval-ideas-about-food/](https://lithub.com/fish-bad-sugar-good-and-other-medieval-ideas-about-food/)

生成摘要时出错

---

## 46. LLMs and self-referentiality

**原文标题**: LLMs and self-referentiality

**原文链接**: [https://scottaaronson.blog/?p=10046](https://scottaaronson.blog/?p=10046)

生成摘要时出错

---

## 47. GoPro acquired, getting into 'defense, government, robotics and aerospace'

**原文标题**: GoPro acquired, getting into 'defense, government, robotics and aerospace'

**原文链接**: [https://www.theverge.com/news/987494/gopro-starman-holding-merger-aquisition](https://www.theverge.com/news/987494/gopro-starman-holding-merger-aquisition)

生成摘要时出错

---

## 48. Cheap Desktop 400GbE Switch MikroTik CRS804-4DDQ-HRM Review

**原文标题**: Cheap Desktop 400GbE Switch MikroTik CRS804-4DDQ-HRM Review

**原文链接**: [https://www.servethehome.com/mikrotik-crs804-4ddq-hrm-review-marvell-annapurna-labs-400gbe/](https://www.servethehome.com/mikrotik-crs804-4ddq-hrm-review-marvell-annapurna-labs-400gbe/)

生成摘要时出错

---

## 49. Instrument clusters are now paid extras in two Hyundai models

**原文标题**: Instrument clusters are now paid extras in two Hyundai models

**原文链接**: [https://www.caranddriver.com/news/a73583741/hyundai-instrument-cluster-paid-option/](https://www.caranddriver.com/news/a73583741/hyundai-instrument-cluster-paid-option/)

生成摘要时出错

---

## 50. The Computer Museum of America reclamation project

**原文标题**: The Computer Museum of America reclamation project

**原文链接**: [https://computer-museum.org/wp/](https://computer-museum.org/wp/)

生成摘要时出错

---

## 51. Claude for Commerce Agents

**原文标题**: Claude for Commerce Agents

**原文链接**: [https://claude.com/blog/claude-for-commerce-agents](https://claude.com/blog/claude-for-commerce-agents)

生成摘要时出错

---

## 52. Renowned NYC Washington Square Park Chess Hustler 'Chichi' Detained by ICE

**原文标题**: Renowned NYC Washington Square Park Chess Hustler 'Chichi' Detained by ICE

**原文链接**: [https://www.chess.com/news/view/washington-square-park-hustler-chichi-detained-by-ice](https://www.chess.com/news/view/washington-square-park-hustler-chichi-detained-by-ice)

生成摘要时出错

---

## 53. Mom gets 6-month suspended sentence for letting 5-year-old walk to the pond

**原文标题**: Mom gets 6-month suspended sentence for letting 5-year-old walk to the pond

**原文链接**: [https://reason.com/2026/09/02/virginia-mom-gets-6-month-suspended-jail-sentence-for-letting-5-year-old-walk-to-the-pond/](https://reason.com/2026/09/02/virginia-mom-gets-6-month-suspended-jail-sentence-for-letting-5-year-old-walk-to-the-pond/)

生成摘要时出错

---

## 54. Microsoft Announces Change to Xbox Cloud Gaming, Switches to Monthly Hour Limits

**原文标题**: Microsoft Announces Change to Xbox Cloud Gaming, Switches to Monthly Hour Limits

**原文链接**: [https://www.ign.com/articles/microsoft-announces-big-changes-to-xbox-cloud-gaming-switches-to-monthly-hour-limits](https://www.ign.com/articles/microsoft-announces-big-changes-to-xbox-cloud-gaming-switches-to-monthly-hour-limits)

生成摘要时出错

---

## 55. MapQuest tops Apple, Google Maps downloads after refusing 'Lake America' change

**原文标题**: MapQuest tops Apple, Google Maps downloads after refusing 'Lake America' change

**原文链接**: [https://thehill.com/homenews/administration/6063924-mapquest-tops-apple-google-maps-in-downloads-after-refusing-trumps-lake-america-change/](https://thehill.com/homenews/administration/6063924-mapquest-tops-apple-google-maps-in-downloads-after-refusing-trumps-lake-america-change/)

生成摘要时出错

---

## 56. Grok outage

**原文标题**: Grok outage

**原文链接**: [https://status.x.ai/](https://status.x.ai/)

生成摘要时出错

---

## 57. Yes, no (built-in) AI is now a feature – LibreOffice blog

**原文标题**: Yes, no (built-in) AI is now a feature – LibreOffice blog

**原文链接**: [https://blog.documentfoundation.org/blog/2026/09/03/yes-no-ai-is-now-a-feature/](https://blog.documentfoundation.org/blog/2026/09/03/yes-no-ai-is-now-a-feature/)

生成摘要时出错

---

## 58. Winter 2026/2027 First Forecast: Super El Niño Drives a Major Weather Divide

**原文标题**: Winter 2026/2027 First Forecast: Super El Niño Drives a Major Weather Divide

**原文链接**: [https://www.severe-weather.eu/long-range-2/winter-2026-2027-first-forecast-super-el-nino-polar-vortex-snow-cold-united-states-canada-europe-fa/](https://www.severe-weather.eu/long-range-2/winter-2026-2027-first-forecast-super-el-nino-polar-vortex-snow-cold-united-states-canada-europe-fa/)

生成摘要时出错

---

## 59. Gemini 3.8 Flash and 3.8 Flash Cyber

**原文标题**: Gemini 3.8 Flash and 3.8 Flash Cyber

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

生成摘要时出错

---

## 60. Muse Spark 1.3

**原文标题**: Muse Spark 1.3

**原文链接**: [https://developer.meta.com/ai/models/muse-spark/](https://developer.meta.com/ai/models/muse-spark/)

生成摘要时出错

---

## 61. Sony makes bold claim about game ownership

**原文标题**: Sony makes bold claim about game ownership

**原文链接**: [https://aginggamer.net/game-industry/sony-makes-bold-claim-about-game-ownership/](https://aginggamer.net/game-industry/sony-makes-bold-claim-about-game-ownership/)

生成摘要时出错

---

## 62. Higher Multipoles of the Cow

**原文标题**: Higher Multipoles of the Cow

**原文链接**: [https://arxiv.org/abs/2504.00506](https://arxiv.org/abs/2504.00506)

生成摘要时出错

---

## 63. Why office workers are turning against AI

**原文标题**: Why office workers are turning against AI

**原文链接**: [https://www.bloodinthemachine.com/p/why-office-workers-are-turning-against](https://www.bloodinthemachine.com/p/why-office-workers-are-turning-against)

生成摘要时出错

---

## 64. Google WeatherNext 3

**原文标题**: Google WeatherNext 3

**原文链接**: [https://deepmind.google/science/weathernext/](https://deepmind.google/science/weathernext/)

生成摘要时出错

---

## 65. Show HN: Real-time AI news aggregator with daily digest

**原文标题**: Show HN: Real-time AI news aggregator with daily digest

**原文链接**: [https://aibriefs.news](https://aibriefs.news)

生成摘要时出错

---

## 66. OpenAI's new reasoning technique alarms AI safety experts

**原文标题**: OpenAI's new reasoning technique alarms AI safety experts

**原文链接**: [https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/](https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/)

生成摘要时出错

---

## 67. Three sites made 215,128 “best software” pages for AI. Perplexity cites them

**原文标题**: Three sites made 215,128 “best software” pages for AI. Perplexity cites them

**原文链接**: [https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/)

生成摘要时出错

---

## 68. Qantas Airbus A380 engine failure in 2010 (2023)

**原文标题**: Qantas Airbus A380 engine failure in 2010 (2023)

**原文链接**: [https://admiralcloudberg.medium.com/a-matter-of-millimeters-the-story-of-qantas-flight-32-bdaa62dc98e7](https://admiralcloudberg.medium.com/a-matter-of-millimeters-the-story-of-qantas-flight-32-bdaa62dc98e7)

生成摘要时出错

---

## 69. Show HN: OwnTime – a chess clock for your day's priorities

**原文标题**: Show HN: OwnTime – a chess clock for your day's priorities

**原文链接**: [https://owntime.app/](https://owntime.app/)

生成摘要时出错

---

## 70. WebLLM: high-performance in-browser LLM inference engine

**原文标题**: WebLLM: high-performance in-browser LLM inference engine

**原文链接**: [https://github.com/mlc-ai/web-llm](https://github.com/mlc-ai/web-llm)

生成摘要时出错

---

## 71. Inside Google’s $200bn Wall Street finance machine for Anthropic

**原文标题**: Inside Google’s $200bn Wall Street finance machine for Anthropic

**原文链接**: [https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c)

生成摘要时出错

---

## 72. We could save petabytes of cache storage with Zstandard and Pingora

**原文标题**: We could save petabytes of cache storage with Zstandard and Pingora

**原文链接**: [https://blog.cloudflare.com/cache-transcoding/](https://blog.cloudflare.com/cache-transcoding/)

生成摘要时出错

---

## 73. Google avoids a breakup of its ad tech business

**原文标题**: Google avoids a breakup of its ad tech business

**原文链接**: [https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html)

生成摘要时出错

---

## 74. Async Rust vs RTOS showdown (2022)

**原文标题**: Async Rust vs RTOS showdown (2022)

**原文链接**: [https://tweedegolf.nl/en/blog/65/async-rust-vs-rtos-showdown/](https://tweedegolf.nl/en/blog/65/async-rust-vs-rtos-showdown/)

生成摘要时出错

---

## 75. Why has Peter Thiel moved to Argentina?

**原文标题**: Why has Peter Thiel moved to Argentina?

**原文链接**: [https://www.theguardian.com/technology/2026/sep/03/peter-thiel-argentina-javier-milei](https://www.theguardian.com/technology/2026/sep/03/peter-thiel-argentina-javier-milei)

生成摘要时出错

---

## 76. Holden's Lightning Flight

**原文标题**: Holden's Lightning Flight

**原文链接**: [https://en.wikipedia.org/wiki/Holden%27s_Lightning_flight](https://en.wikipedia.org/wiki/Holden%27s_Lightning_flight)

生成摘要时出错

---

## 77. Ig Nobel Prize Winners

**原文标题**: Ig Nobel Prize Winners

**原文链接**: [https://arstechnica.com/science/2026/09/meet-the-2026-ig-nobel-prize-winners/](https://arstechnica.com/science/2026/09/meet-the-2026-ig-nobel-prize-winners/)

生成摘要时出错

---

## 78. Quasar 438B: Europe's Leading AI Model

**原文标题**: Quasar 438B: Europe's Leading AI Model

**原文链接**: [https://multiversecomputing.com/resources/introducing-quasar-438b-europe-s-leading-ai-model](https://multiversecomputing.com/resources/introducing-quasar-438b-europe-s-leading-ai-model)

生成摘要时出错

---

## 79. Altair Basic Interpreter Source Code (1975) [pdf]

**原文标题**: Altair Basic Interpreter Source Code (1975) [pdf]

**原文链接**: [https://images.gatesnotes.com/12514eb8-7b51-008e-41a9-512542cf683b/34d561c8-cf5c-4e69-af47-3782ea11482e/Original-Microsoft-Source-Code.pdf](https://images.gatesnotes.com/12514eb8-7b51-008e-41a9-512542cf683b/34d561c8-cf5c-4e69-af47-3782ea11482e/Original-Microsoft-Source-Code.pdf)

生成摘要时出错

---

## 80. Can I opt out of my input or output data being used for training?

**原文标题**: Can I opt out of my input or output data being used for training?

**原文链接**: [https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)

生成摘要时出错

---

## 81. Claude Fable 5.1 and Claude Mythos 5.1

**原文标题**: Claude Fable 5.1 and Claude Mythos 5.1

**原文链接**: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)

生成摘要时出错

---

## 82. A dark horse enters China's AI race: StartLux

**原文标题**: A dark horse enters China's AI race: StartLux

**原文链接**: [https://chinaonchina.com/article/chen-dawei-returns-enters-the-large-model-sector](https://chinaonchina.com/article/chen-dawei-returns-enters-the-large-model-sector)

生成摘要时出错

---

## 83. Fable 5.1 World Modeling

**原文标题**: Fable 5.1 World Modeling

**原文链接**: [https://github.com/PhiloLabs/fable51-worlds](https://github.com/PhiloLabs/fable51-worlds)

生成摘要时出错

---

## 84. My local model setup on an M4 Pro Mac Mini

**原文标题**: My local model setup on an M4 Pro Mac Mini

**原文链接**: [https://lws.io/blog/my-local-model-setup/](https://lws.io/blog/my-local-model-setup/)

生成摘要时出错

---

## 85. Government-funded journalism can work if it's free to report the truth

**原文标题**: Government-funded journalism can work if it's free to report the truth

**原文链接**: [https://theconversation.com/stars-and-stripes-shows-how-government-funded-journalism-can-work-if-its-free-to-report-the-truth-290477](https://theconversation.com/stars-and-stripes-shows-how-government-funded-journalism-can-work-if-its-free-to-report-the-truth-290477)

生成摘要时出错

---

## 86. Reasons robotics is hard

**原文标题**: Reasons robotics is hard

**原文链接**: [https://secondthoughts.ai/p/14-reasons-robotics-is-hard](https://secondthoughts.ai/p/14-reasons-robotics-is-hard)

生成摘要时出错

---

## 87. Show HN: I built my first MCP to manage Google Ads

**原文标题**: Show HN: I built my first MCP to manage Google Ads

**原文链接**: [https://adchestra.com/](https://adchestra.com/)

生成摘要时出错

---

## 88. What if everything we know about recycling is wrong?

**原文标题**: What if everything we know about recycling is wrong?

**原文链接**: [https://worksinprogress.co/issue/just-bury-your-trash/](https://worksinprogress.co/issue/just-bury-your-trash/)

生成摘要时出错

---

## 89. UK's Online Safety Act has made 'absolutely no difference,' kids say

**原文标题**: UK's Online Safety Act has made 'absolutely no difference,' kids say

**原文链接**: [https://www.theregister.com/security/2026/09/03/uks-online-safety-act-has-made-absolutely-no-difference-kids-say/5293893](https://www.theregister.com/security/2026/09/03/uks-online-safety-act-has-made-absolutely-no-difference-kids-say/5293893)

生成摘要时出错

---

## 90. A note on subscription prices from LWN

**原文标题**: A note on subscription prices from LWN

**原文链接**: [https://lwn.net/Articles/1090585/](https://lwn.net/Articles/1090585/)

生成摘要时出错

---

## 91. Aging brains blend memories together instead of just forgetting them

**原文标题**: Aging brains blend memories together instead of just forgetting them

**原文链接**: [https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/](https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/)

生成摘要时出错

---

## 92. Fine, I'll build my own text editor

**原文标题**: Fine, I'll build my own text editor

**原文链接**: [https://dbushell.com/2026/09/01/text-editor/](https://dbushell.com/2026/09/01/text-editor/)

生成摘要时出错

---

## 93. 4.5B Posts Scraped from TikTok

**原文标题**: 4.5B Posts Scraped from TikTok

**原文链接**: [https://tiktok-api.seeksocial.io/](https://tiktok-api.seeksocial.io/)

生成摘要时出错

---

## 94. What archaeology reveals about the rise of autocracy

**原文标题**: What archaeology reveals about the rise of autocracy

**原文链接**: [https://knowablemagazine.org/content/article/society/2026/what-archaeology-reveals-about-rise-of-autocracy](https://knowablemagazine.org/content/article/society/2026/what-archaeology-reveals-about-rise-of-autocracy)

生成摘要时出错

---

## 95. GPT-6 Astra Benchmarks Image

**原文标题**: GPT-6 Astra Benchmarks Image

**原文链接**: [https://cdn.thenewstack.io/media/2026/09/358eb84a-screenshot-2026-09-03-at-10.51.35-am.png](https://cdn.thenewstack.io/media/2026/09/358eb84a-screenshot-2026-09-03-at-10.51.35-am.png)

生成摘要时出错

---

## 96. 'Starwashing': The new space race has an environmental problem

**原文标题**: 'Starwashing': The new space race has an environmental problem

**原文链接**: [https://grist.org/technology/starwashing-space-race-environment-spacex/](https://grist.org/technology/starwashing-space-race-environment-spacex/)

生成摘要时出错

---

## 97. Echo Is Acquiring Minimus

**原文标题**: Echo Is Acquiring Minimus

**原文链接**: [https://www.echo.ai/blog/echo-is-acquiring-minimus](https://www.echo.ai/blog/echo-is-acquiring-minimus)

生成摘要时出错

---

## 98. Reverse Engineering Unknown File Formats with ImHex

**原文标题**: Reverse Engineering Unknown File Formats with ImHex

**原文链接**: [https://werwolv.net/posts/file_format_reverse_engineering/](https://werwolv.net/posts/file_format_reverse_engineering/)

生成摘要时出错

---

## 99. Biggest dark matter detector spots a single weird particle

**原文标题**: Biggest dark matter detector spots a single weird particle

**原文链接**: [https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle)

生成摘要时出错

---

## 100. Commodore 64 released September 1, 1982

**原文标题**: Commodore 64 released September 1, 1982

**原文链接**: [https://dfarq.homeip.net/commodore-64-released-september-1-1982/](https://dfarq.homeip.net/commodore-64-released-september-1-1982/)

生成摘要时出错

---

