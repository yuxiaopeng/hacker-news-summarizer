# Hacker News 热门文章摘要 (2025-11-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: Wealthfolio 2.0 - 开源投资追踪器。现已支持移动端和 Docker

**原文标题**: Show HN: Wealthfolio 2.0- Open source investment tracker. Now Mobile and Docker

**原文链接**: [https://wealthfolio.app/?v=2.0](https://wealthfolio.app/?v=2.0)

Wealthfolio 2.0 是一款开源的、注重隐私的投资追踪器，现已推出桌面端、移动端和网页端版本。它允许用户在一个地方聚合所有投资和储蓄账户，从而全面了解自己的财富。一个关键特性是其首要关注隐私的方法，确保用户数据保留在他们的设备上。它提供CSV导入功能以及精心设计、用户友好的界面。

Wealthfolio提供诸如持仓概览、投资组合洞察和业绩追踪等功能，允许用户监控股票、ETF和加密货币。业绩仪表板支持账户比较、与标普500等指数进行基准测试以及ETF追踪。收入追踪有助于监控股息和利息收入。

此外，Wealthfolio还提供历史数据、账户分析、目标追踪以及税务优惠账户的供款额度/限额追踪。它可以帮助用户定义财务目标、监控进度并避免过度供款。该平台可以通过插件扩展，例如投资费用追踪器、目标进度追踪器和股票交易追踪器。Wealthfolio可以免费使用，并提供一次性可选付费。

---

## 2. 我们都应该使用依赖冷却机制。

**原文标题**: We should all be using dependency cooldowns

**原文链接**: [https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)

本文倡导采用“依赖冷却期”作为一种简单有效的缓解开源供应链攻击的方法。“依赖冷却期”是指在发布新的依赖项版本后，延迟一段时间再集成它们，从而为发现和解决漏洞留出时间。

作者强调，大多数供应链攻击在恶意更新发布与其被检测/移除之间都存在一个很短的窗口期（几小时或几天）。通过实施冷却期（例如，7-14天），开发者可以避免绝大多数此类攻击。

冷却期的优点包括：

*   **经验有效性：** 它们可以缓解最常见的供应链攻击类型。
*   **易于实施：** Dependabot和Renovate等工具提供内置的冷却期功能，一些包管理器也提供原生支持。
*   **激励负责任的供应商行为：** 鼓励安全供应商专注于快速攻击检测，而不是过度炒作营销。

文章强调，冷却期并非完美的解决方案，因为老练的攻击者可能仍然可以逃避检测。然而，作者认为，通过这种免费且简单的技术，可以显著降低风险暴露（80-90%），使其成为一项有价值的安全措施。作者还建议包管理器应原生支持冷却期，以实现全面保护。

---

## 3. FAWK：大型语言模型可以编写语言解释器

**原文标题**: FAWK: LLMs can write a language interpreter

**原文链接**: [https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html](https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html)

受 AWK 编程语言的启发，但又因其在解决 Advent of Code 问题时的局限性而感到沮丧，作者设想了一种更具函数式和现代化的 "FAWK" 语言。他们渴望拥有诸如一流数组、函数、词法作用域、显式全局变量和管道等功能。

他们没有自己实现 FAWK，而是利用 Cursor Agent 和 LLM（特别是 Sonnet 4.5）生成了一个可工作的 Python 解释器，并配有全面的端到端测试。 LLM 成功处理了复杂的功能，如任意精度浮点运算（借助 `mpmath` 库）、print 语句/表达式的二元性、多维数组和词法作用域。 还在 C、Haskell 和 Rust 中尝试了实现，并取得了初步成功。

作者对 LLM 基于高级指令和迭代指导交付功能性解释器的能力印象深刻。 虽然承认自己对生成的代码不太熟悉，但他们很高兴在未来的 Advent of Code 挑战中使用 "FAWK"。 他们也在考虑将 LLM 用于其他编程项目，例如实现 Hindley-Milner 类型系统，但也认识到需要平衡 LLM 的协助与保持个人编码能力。 FAWK 可在 GitHub (Janiczek/fawk) 上供其他人尝试，但承认其实验性质和潜在的性能问题。

---

## 4. Olmo 3：引领开源AI，探索模型流程之路

**原文标题**: Olmo 3: Charting a path through the model flow to lead open-source AI

**原文链接**: [https://allenai.org/blog/olmo3](https://allenai.org/blog/olmo3)

Olmo 3 于2025年11月20日发布，强调开源人工智能开发，提供对整个模型流程的访问权限，而不仅仅是最终模型。这包括创建和修改语言模型所需的每个阶段、检查点、数据集和依赖项。

该版本的核心是 Olmo 3-Think (32B)，一个推理模型，允许检查中间推理步骤及其在训练数据中的来源。Olmo 3 系列还包括：Olmo 3-Base (7B, 32B)，一个强大的基础模型，优于其他完全开源的基础模型，并与领先的开源权重模型竞争；Olmo 3-Think (7B, 32B)，一个经过后训练的推理模型，缩小了与顶级开源权重模型的差距，同时使用更少的训练tokens；Olmo 3-Instruct (7B)，一个专注于聊天的模型，在对话能力和工具使用方面与开源权重模型相匹配或超过它们；以及 Olmo 3-RL Zero (7B)，一种用于引导复杂推理并支持 RL 算法基准测试的强化学习途径。

Olmo 3 提供来自同一基础模型的多种记录在案的开发路径（Instruct、RL Zero、Think），从而促进定制和实验。所有组件（数据、代码、模型权重、检查点）均在宽松的开源许可下发布。Olmo 3 模型在各种基准测试中表现出强大的性能，其中 Olmo 3-Base 32B 优于完全开源的基础模型，而 Olmo 3-Think 32B 则成为最强大的完全开源的思考模型。严格的数据管理、优化的训练方法以及算法/基础设施的进步促成了这些结果。

---

## 5. 初代Xbox平台的XBMC 4.0

**原文标题**: XBMC 4.0 for the Original Xbox

**原文链接**: [https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/](https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/)

XBMC 4.0发布：经典媒体中心平台重大更新，自2016年以来首次重大进展。此更新对软件进行了现代化改造，保留并扩展了这款标志性自制应用程序的功能。

XBMC由XboxMediaPlayer演变而来，后来发展为Kodi和Plex，在家庭媒体软件领域拥有悠久的历史。 4.0版本带来了由Estuary皮肤（最初来自Kodi v17）驱动的现代界面，并更新了GUI框架，以及一个功能完善的游戏库系统，支持Xbox和模拟游戏的元数据。

新版本恢复了电影和电视元数据抓取器的完整功能，支持在线插件存储库，并改进了任务调度，从而在Xbox的有限硬件上实现更流畅的多任务处理。 它保持了对FLAC等无损音频编解码器的支持，并包括与MilkDrop等音频可视化工具的兼容性。

XBMC 4.0继续提供基于Python的插件架构，并具有更新的设置界面，其中包含全面的自定义选项。 开发团队计划过渡到Python 3.4.10，以潜在地反向移植更新的Kodi插件。

此版本致敬了XBMC的传统，同时实现了体验的现代化，展示了Original Xbox上的持续开发，并计划了未来的更新。 下载和源代码可在Github上找到，欢迎大家贡献。 Xbox-Scene Discord服务器提供支持。

---

## 6. 制作小型RPG

**原文标题**: Making a Small RPG

**原文链接**: [https://jslegenddev.substack.com/p/making-a-small-rpg](https://jslegenddev.substack.com/p/making-a-small-rpg)

无法访问文章链接。

---

## 7. 枢轴机器人(YC W24) 招聘工业自动化硬件工程师

**原文标题**: Pivot Robotics (YC W24) Is Hiring for an Industrial Automation Hardware Engineer

**原文链接**: [https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls](https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls)

Pivot Robotics (YC W24) 招聘机械工程师（控制方向），助力打造并部署用于高混合制造中机械臂的AI大脑。 他们的软件将现成的机器人和视觉传感器与基础视觉模型相结合，使机器人能够适应复杂的任务，其首款产品专注于自动化金属研磨。 该公司目前已在铸铁厂的 10 多个机器人上部署。

该职位涉及构建和连接控制面板、将传感器和执行器与 PLC/Arduino/机器人控制器集成、设计安全系统以及排除机电子系统的故障。 与软件和电气工程师的合作至关重要，支持客户现场的机器人单元设置也同样重要。 该工程师还将设计和组装机械系统，如虎钳和相机支架。

理想的候选人将拥有机械、机电一体化或机器人工程专业的学士或硕士学位，并具有 1-2 年的机械设计和控制系统集成经验。 必需的技能包括构建控制面板的经验、熟悉安全硬件和标准、了解气动系统、精通 CAD（SolidWorks、Fusion 360 或 Onshape），以及能够在实验室和工厂环境中进行实际操作的能力以及出差意愿。 该职位是全职，位于旧金山，薪资为 10 万美元至 13.5 万美元，并提供 0.40% 至 0.75% 的股权。

---

## 8. 从零开始构建一个最小可用的Armv7模拟器

**原文标题**: Building a Minimal Viable Armv7 Emulator from Scratch

**原文链接**: [https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/](https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/)

本文详细介绍了如何使用 Rust 从头开始构建一个最小的 Armv7 模拟器，名为 "stinkarm"。该模拟器仅用约 1300 行代码实现，不依赖任何外部依赖项。其重点在于解析和验证 Armv7 ELF 二进制文件，将段映射到内存中，解码 Arm 指令的一个子集，转换内存交互，以及将 Arm Linux 系统调用转发到宿主 x86-64 系统。

作者创建了一个简单的 "hello world" Armv7 二进制文件作为测试用例，并利用构建脚本和 Nix flake 来编译汇编代码。该模拟器解析 ELF 头部和程序头部以了解二进制文件的结构，识别可执行段，并将它们映射到模拟器的内存空间中。

关键方面包括实现 ELF 头部和程序头部的解析逻辑，定义 Rust 结构体和枚举来表示 ELF 格式元素，以及处理字节序。本文重点介绍了使用宏将字节解析为无符号整数。通过细致地重现执行环境，该模拟器展示了在不同架构上运行 Armv7 二进制文件的基本步骤。

---

## 9. 命令行 – AI 编码的控制谱

**原文标题**: Command Lines – AI Coding's Control Spectrum

**原文链接**: [https://www.wreflection.com/p/command-lines-ai-coding](https://www.wreflection.com/p/command-lines-ai-coding)

Nowfal的《命令行——AI编程的控制谱》探讨了AI编程助手快速发展的格局。在Cursor等工具的推动下，市场蓬勃发展，有望释放软件工程领域显著的生产力提升。

文章将用户分为三类：“手工编码”（避免使用AI者）、“凭感觉编码”（非工程师使用AI进行原型设计）和“架构师+AI编码”（工程师策略性地将任务委托给AI）。根据用户类型，AI编码市场分为面向非工程师的“放手型”工具（原型设计）和面向专业工程师的“动手型”工具（生产代码）。

虽然Cursor的收入增长显著，但其对OpenAI和Anthropic等公司基础模型的依赖构成了一个挑战，尤其是在速率限制方面。Cursor开发Composer-2等内部模型旨在解决这个问题。模型质量被认为是AI编码竞赛中的关键因素，Claude Code和OpenAI Codex正在迎头赶上。

微软（GitHub Copilot）、AWS（Kiro）和谷歌（Antigravity）等现有企业利用现有的客户关系和捆绑销售进行竞争。初创公司可以通过赢得组织内单个用户的青睐来获得 traction。这种转变也影响了StackOverflow等传统开发者资源，因为AI越来越多地回答编程问题。

最终目标是完全自主的软件生成，而胜出者将是那些提供卓越模型质量、独特功能和强大用户留存率的公司。

---

## 10. 制造振荡器很难。

**原文标题**: It's hard to build an oscillator

**原文链接**: [https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator](https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator)

无法访问文章链接。

---

## 11. 科学家现在知道蜜蜂可以处理时间，这在昆虫中尚属首次。

**原文标题**: Scientists now know that bees can process time, a first in insects

**原文链接**: [https://www.cnn.com/2025/11/12/science/bees-visual-stimulus-study-scli-intl](https://www.cnn.com/2025/11/12/science/bees-visual-stimulus-study-scli-intl)

一项新研究表明熊蜂可以处理光闪持续时间，展现出一种之前未在昆虫中发现的时间处理能力。伦敦玛丽女王大学的研究人员设计了一个迷宫，熊蜂在其中学会将短光闪与甜食联系起来，将长光闪与苦食联系起来。即使没有食物出现，熊蜂也能区分光照时长，表明它们是在处理时间本身，而不仅仅是依靠气味或奖励的视觉。

这一发现挑战了昆虫仅仅是受本能驱动的“反射机器”的观点，并表明它们拥有复杂的认知能力。该发现将蜜蜂置于包括人类和一些脊椎动物在内的一小群能够区分短时长和长时长的动物之列，这种技能对于理解摩尔斯电码等任务至关重要。

研究人员计划调查这种时间处理能力背后的神经机制，并研究群体动态如何影响学习。他们希望这项研究能够鼓励人们更加欣赏昆虫的认知复杂性。这项研究对我们理解时间本身具有更广泛的意义，时间是生命的一个基本方面，但仍然知之甚少。未参与该研究的专家强调了该发现的重要性，指出时间管理对于觅食蜜蜂的必要性，并强调令人印象深刻的认知能力不一定需要大脑袋。

---

## 12. 纳米香蕉Pro

**原文标题**: Nano Banana Pro

**原文链接**: [https://blog.google/technology/ai/nano-banana-pro/](https://blog.google/technology/ai/nano-banana-pro/)

谷歌DeepMind推出Nano Banana Pro (Gemini 3 Pro图像)：基于Gemini 3 Pro构建的先进图像生成和编辑模型，提供更强的推理能力、现实世界知识和创意控制。它可以帮助用户轻松地将想法可视化、创建信息图表，并将笔记转化为图表。

主要功能包括：

*   **准确且内容丰富的视觉效果：** Nano Banana Pro生成的视觉效果具有增强的推理能力，并能实时整合来自谷歌搜索的信息。
*   **多种语言的清晰文本：** 该模型擅长在图像中渲染准确且清晰的文本，支持国际内容创作和本地化。
*   **高保真视觉效果：** 提供一致的品牌形象、高级创意控制和高达4K的分辨率。用户可以在复杂构图中保持最多14个输入和5个人的连贯性。
*   **工作室级别的创意控制：** 局部编辑允许细化图像的任何部分，调整相机角度、改变焦点、应用色彩分级和转换场景光照。

Nano Banana Pro已在谷歌产品中推出，例如Gemini应用、Google Ads、Workspace、Google AI Studio和Gemini API。谷歌还强调透明度，通过在AI生成的图像中嵌入SynthID数字水印，并在Gemini应用中提供验证工具。免费和Google AI Pro用户还将看到可见的“Gemini闪光”水印。

---

## 13. 我把转盘电话改造成了会议听筒。

**原文标题**: I converted a rotary phone into a meeting handset

**原文链接**: [https://www.stavros.io/posts/i-converted-a-rotary-phone-into-a-meeting-handset/](https://www.stavros.io/posts/i-converted-a-rotary-phone-into-a-meeting-handset/)

作者详细介绍了将老式转盘电话改造成功能性会议听筒的项目，其动力源于对会议的“深恶痛绝”。目标是创建一个既能作为会议音频的麦克风/扬声器，又能以令人满意的摔挂方式结束会议的设备。

该项目使用了西门子转盘电话，通过设计和3D打印定制连接器，保留了其原始组件，实现了简易且无损的接线。最初计划使用RP2040微控制器作为组合声卡和键盘模拟器。然而，在使用LLM（Claude Opus）编写声卡代码，经历了一次代价高昂且最终徒劳的尝试后，作者转向了“B计划”。

B计划包括使用USB集线器、一个廉价的速卖通USB声卡，以及仅用于键盘功能的RP2040。作者拆解了声卡，将引脚焊接到音频插孔上以便连接听筒，并将其连接到USB集线器。然后将RP2040连接到电话的挂机开关和转盘。编写了代码来检测听筒何时挂断，并发送相应的按键（例如，Zoom的Ctrl+Shift+E）以关闭会议窗口。转盘也被编程为将拨号数字作为按键输入。

最终产品通过USB集线器成功结合了声卡和键盘功能。作者提供了一个视频演示，展示了令人满意的挂断功能。他们总结说，这个项目相对简单，最具挑战性的方面是RP2040键盘模拟，这在很大程度上是由LLM处理的。

---

## 14. 安卓和iPhone用户现在可以共享文件，从Pixel 10开始。

**原文标题**: Android and iPhone users can now share files, starting with the Pixel 10

**原文链接**: [https://blog.google/products/android/quick-share-airdrop/](https://blog.google/products/android/quick-share-airdrop/)

谷歌正通过Quick Share和AirDrop实现安卓与iPhone用户间的文件共享，从而弥合两者之间的差距。这项新功能将从Pixel 10系列开始，实现安卓和iOS操作系统之间无缝的文件传输，解决了一个常见的用户痛点。谷歌强调该功能的安全性，强调了强大的安全保障和独立的安全性测试。在此之前，谷歌曾致力于提高操作系统之间的兼容性，例如RCS消息和未知追踪器警报。该公司计划未来将该功能扩展到更多安卓设备。

---

## 15. 我最喜欢的数学题

**原文标题**: My Favorite Math Problem

**原文链接**: [https://bytesauna.com/post/my-favorite-math-problem](https://bytesauna.com/post/my-favorite-math-problem)

马蒂亚斯·海基拉的文章《我最喜欢的数学问题》探讨了一个简单而富有挑战性的棋盘谜题的魅力：一个被破坏的棋盘（通过移除两个相对的对角线角而获得）能否被2x1的方块覆盖？ 答案是否定的，因为破坏导致黑白方格数量不相等，而每个2x1的方块必须覆盖一个黑色和一个白色方格。

海基拉欣赏这个问题易于理解和具有迷惑性的难度，他指出，虽然陈述很容易理解，但找到解决方案需要洞察力。 他认为这个问题是理解“高等数学”的入口，特别是证明存在性而不是简单地构建解决方案的概念。 这引出了对抽象定义和证明的讨论，他认为它们因其创造性而类似于艺术。

文章随后深入探讨了计算机在现代数学中的作用。 他指出，证明可以被视为类型，这是一个可以通过编程语言让计算机理解的概念。 微软等公司的项目旨在将数学知识形式化为计算机可读的形式，从而实现严肃的研究和自动证明验证。 他还谈到了人工智能，特别是大型语言模型（LLM）在生成数学陈述的类型理论公式方面的潜力。 海基拉最后表示，数学研究可能很快就会被这些技术进步所彻底改变。

---

## 16. Deno沙箱中的开源和本地代码模式MCP

**原文标题**: Open Source and Local Code Mode MCP in Deno Sandboxes

**原文链接**: [https://portofcontext.com](https://portofcontext.com)

本文介绍了一种新的开源本地代码模式MCP（可能指“模型控制平面”），旨在Deno沙箱内运行。其核心目标是利用“上下文替换”技术，实现安全可靠的大语言模型（LLM）工具调用。本质上，它促进了AI Agent与现实世界数据和功能的连接。

重点在于强调一个健壮且开源的框架，该框架使AI Agent能够通过代码执行与环境交互，所有操作都在Deno沙箱的安全约束内进行。这意味着该工具允许LLM执行代码、检索数据和执行操作，同时防止恶意代码损害系统或访问未经授权的资源。

文章推广了使用PCTX工具的可能性，PCTX可能是一种与该技术相关的云服务。“PCTX CLOUD WAITLIST”的存在表明，基于该基础构建的产品或服务尚未公开提供。

简而言之，本文重点介绍了一种技术，该技术通过结合开源工具、本地代码执行、LLM“上下文替换”功能以及Deno沙箱的安全功能，允许AI Agent与现实世界系统之间进行更安全、更可控的交互。

---

## 17. 古罗马玻璃揭示隐藏的“语言”

**原文标题**: Ancient Roman Glass Reveals a Hidden "Language"

**原文链接**: [https://nautil.us/ancient-roman-glass-reveals-a-hidden-language-1247932/](https://nautil.us/ancient-roman-glass-reveals-a-hidden-language-1247932/)

考古学家兼玻璃吹制匠哈莉·梅雷迪思在大都会艺术博物馆观察到古罗马玻璃笼杯（笼状玻璃杯）后，可能揭示了制造它们的工匠所使用的“隐藏语言”。梅雷迪思注意到十字、叶子和菱形等重复出现的图案以及铭文，她认为这些不仅仅是装饰性的，而是作为一种视觉交流系统。

她的研究表明，这些符号起到了品牌推广的作用，表明了制造这些杯子的区域作坊。通过检查未完成的笼状玻璃杯碎片、工具痕迹和铭文，梅雷迪思提出，学徒、抛光师和雕刻师组成的集体共同完成了这些复杂的项目，这些项目可能需要数年才能完成。

杯子上发现的符号可能被用来表示生产它们的特定作坊，类似于现代品牌。梅雷迪思的研究结果发表在《玻璃研究杂志》和《世界考古学》上，挑战了人们对古代工匠及其工作的现有理解。她希望她的工作能够激发对笼状玻璃杯生产的进一步研究，从而更细致地了解这些珍贵的罗马财产背后的工匠。

---

## 18. 私募股权的新冒险：青少年体育

**原文标题**: Private Equity's New Venture: Youth Sports

**原文链接**: [https://jacobin.com/2025/11/youth-sports-hockey-private-equity](https://jacobin.com/2025/11/youth-sports-hockey-private-equity)

私募股权公司日益投资青少年体育，导致成本增加，许多家庭的参与机会受限。像黑熊体育集团这样由私募股权支持的公司，正在收购溜冰场和其他体育设施，然后实施政策以最大化利润。一项关键策略是禁止家长录制孩子们的比赛，迫使他们订阅昂贵的流媒体服务（例如，黑熊电视每月收费25-50美元）。这种做法引来了批评，包括参议员克里斯·墨菲，他因为直播他孩子的冰球比赛而受到团队处罚的威胁。

除了流媒体之外，黑熊还在增加费用，例如在设备、注册和美国冰球协会会员费等现有费用之上增加 50 美元的“注册和保险”费。批评人士认为，这些行为类似于私募股权在其他行业的策略：降低服务质量，同时提高回报。在职业化、私人教练和运动心理学家的推动下，青少年体育的成本不断上涨，这使得低收入家庭难以负担。本已昂贵的冰球运动变得更加难以企及。

像Unrivaled Sports和Varsity Brands这样的其他公司也在整合棒球训练营、啦啦队竞技场和其他体育项目，引发了人们对成本进一步增加和反竞争行为的担忧。例如，Varsity Brands面临一项诉讼，指控其排挤啦啦队竞争对手并从参与者那里榨取利润，最终以 8200 万美元和解。法律专家担心，对利润的关注胜过儿童发展，这将导致青少年体育行业的进一步剥削。

---

## 19. 新人工智能意识论文 - 斯科特·亚历山大

**原文标题**: The New AI Consciousness Paper – By Scott Alexander

**原文链接**: [https://www.astralcodexten.com/p/the-new-ai-consciousness-paper](https://www.astralcodexten.com/p/the-new-ai-consciousness-paper)

斯科特·亚历山大的文章剖析了一篇新的论文，该论文试图识别人工智能系统中的意识指标，由 Yoshua Bengio 和 David Chalmers 等知名人士共同撰写。该论文侧重于意识的计算理论，由于可行性考虑，避开了物理和超自然的解释。它考察了诸如循环处理理论、全局工作空间理论和高阶理论等理论，所有这些理论都与认知处理中的反馈机制有关。

亚历山大认为，虽然计算机科学家可以确定哪些人工智能系统表现出“某种反馈”，但该论文的哲学贡献却因将访问意识（对自己思想的意识）等同于现象意识（主观内在体验）而站不住脚。他批评该论文对全局工作空间理论等理论的解读，认为如果应用于现象意识，会导致荒谬的结论。他还指出，神经科学理论通常建立在对信息的观察性访问之上，因此不清楚为什么反馈机制会与现象意识相关联。亚历山大认为，这种“偷梁换柱”使得该论文的意义大打折扣。

---

## 20. 从零开始学习WebAssembly

**原文标题**: WebAssembly from the Ground Up

**原文链接**: [https://wasmgroundup.com/](https://wasmgroundup.com/)

从零开始学习WebAssembly：通过JavaScript构建简易编译器，本书旨在通过动手实践的方式，向读者讲解WebAssembly (Wasm) 的原理。无需具备编译器专业知识。

本书涵盖WebAssembly指令集、模块格式以及如何使用JavaScript与之交互。读者将构建一个名为Wafer的玩具语言的编译器，学习如何将代码编译成WebAssembly。主题包括数值指令、内存访问、控制流和WebAssembly安全模型。本书为每个里程碑提供完整的、MIT许可的源代码。

本书面向具有中级JavaScript知识的经验丰富的程序员，承诺使用Ohm解析工具包简化编译器创建。目标是提供对WebAssembly清晰易懂的解释，使其更容易理解和使用底层技术。本书价格包含技术内容、交互式网页和PDF版本、Discord会员资格和退款保证。

---

## 21. FEX-emu – 在ARM64 Linux设备上运行x86应用程序

**原文标题**: FEX-emu – Run x86 applications on ARM64 Linux devices

**原文链接**: [https://fex-emu.com/](https://fex-emu.com/)

FEX-emu最新版本发布公告：此软件模拟器允许用户在ARM64 Linux设备上运行x86应用程序。新标记版本（2511）已发布，表明该模拟器正在持续开发和改进。作者强调了模拟器开发的持续性，并邀请读者“阅读更多”以了解此版本中包含的具体更改和更新。该帖子主要提醒用户FEX-emu发布了新版本，并暗示了改进或新功能，但未在此简介中详细说明。

---

## 22. 鲸鱼冲浪鱼

**原文标题**: A Whale-Surfing Fish

**原文链接**: [https://apnews.com/article/sucker-fish-riding-whale-remoras-humpback-australia-69db9878c42b7d11e3755ecca4132588](https://apnews.com/article/sucker-fish-riding-whale-remoras-humpback-australia-69db9878c42b7d11e3755ecca4132588)

本文探讨了科学家在澳大利亚海岸拍摄到的罕见镜头，展示了鮣鱼（也称为吸盘鱼）在座头鲸身上“冲浪”的行为。这些鱼利用头部的吸盘附着在鲸鱼身上，以死皮和海虱为食。

这些镜头是用吸盘相机拍摄的，目的是研究鲸鱼的行为。镜头显示，鮣鱼在鲸鱼跃出水面之前和之后，能巧妙地脱离并重新附着在鲸鱼身上，展现出惊人的时机把握和精确性。虽然这种关系通常被认为是互惠互利的，鮣鱼能帮助鲸鱼清洁身体，但科学家Olaf Meynecke观察到，身上附着大量鮣鱼的鲸鱼似乎很烦躁，跃出水面的频率更高，这可能是为了甩掉这些鱼。

本文还探讨了一个谜团：在鲸鱼于南极洲和昆士兰之间进行1万公里的迁徙过程中，鮣鱼会附着多久？目前尚不清楚它们是否会在温带水域脱落并寻找新的宿主，如蝠鲼或海豚，直到鲸鱼返回。作者指出，如果找不到其他宿主，鮣鱼也会附着在水肺潜水员身上，这让潜水员非常恼火。

---

## 23. 美国如何通过数字手段切断一位法国法官的联系

**原文标题**: How a French judge was digitally cut off by the USA

**原文链接**: [https://www.heise.de/en/news/How-a-French-judge-was-digitally-cut-off-by-the-USA-11087561.html](https://www.heise.de/en/news/How-a-French-judge-was-digitally-cut-off-by-the-USA-11087561.html)

海塞在线文章《美国如何以数字方式切断一位法国法官的联系》讨论了法国法官萨布丽娜·达乌德的案例，她因其在恐怖主义案件方面的工作而面临美国制裁造成的重大数字干扰。达乌德法官参与了与美国制裁的实体相关的调查。

具体而言，该文章详细介绍了美国财政部如何因达乌德法官处理涉及库尔德-叙利亚罗伊营地的恐怖主义案件的行为，将其列入特别指定国民（SDN）名单。这一指定导致她实际上与各种在线服务和平台隔绝。

被列入SDN名单的后果影响深远。许多总部位于美国和国际运营的科技公司，包括谷歌、苹果和支付提供商，都阻止了她访问其服务。这意味着她失去了访问其电子邮件、在线存储和金融平台的权限，严重阻碍了她的职业和个人生活。

该文章强调了美国制裁的域外管辖权，以及它们可能对未直接参与美国试图打击的活动中的个人的重大影响。它引发了人们对美国制裁破坏国外个人生活的能力以及广泛应用制裁时可能造成的附带损害的担忧。它质疑这些制裁对法国法官司法独立的影响。

---

## 24. PNG图像中的EXIF方向信息不用于image-orientation: from-image

**原文标题**: EXIF orientation info in PNGs isn't used for image-orientation: from-image

**原文链接**: [https://bugzilla.mozilla.org/show_bug.cgi?id=1627423](https://bugzilla.mozilla.org/show_bug.cgi?id=1627423)

此错误报告详述了 Firefox 在使用 `image-orientation: from-image` 时，无法正确识别 PNG 图像中 EXIF 方向数据的问题。具体而言，包含 EXIF 方向信息（如“顺时针旋转 90 度”）的 PNG 图像，并没有像具有相同 EXIF 数据的 JPEG 图像一样，以正确的方向显示。

报告者 Eric Portis 发现，最初 Safari、Chrome 和 Firefox 都无法处理附加在 PNG *末尾*的 EXIF 数据（exiftool 的默认设置）。Safari 可以处理 *在* 图像数据 *之前* 的 EXIF 数据，但 Firefox 和 Chrome 不行。这个问题出现的原因是，当图像大小可能在加载过程中因方向数据而改变时，渲染行为会受到影响。

Cameron McCormack 指出，PNG 确实支持通过 eXif 数据块来存储方向数据，如果该数据块出现在图像数据之前，实现对它的支持是可行的。

该错误最终被标记为 bug 1682759 的副本，Timothy Nikkel 表示该 bug 应该能解决这个问题。由于 Chrome 和 Safari 的处理方式不同，该问题被认为是 Web 兼容性错误。该错误报告引用了关于 eXIf 的 PNG-3 规范。

---

## 25. 过度监管使成本翻倍。

**原文标题**: Over-regulation is doubling the cost

**原文链接**: [https://rein.pk/over-regulation-is-doubling-the-cost](https://rein.pk/over-regulation-is-doubling-the-cost)

过度监管是美国硬科技创新的主要障碍

---

## 26. 新操作系统旨在提供（一定程度的）macOS兼容性

**原文标题**: New OS aims to provide (some) compatibility with macOS

**原文链接**: [https://github.com/ravynsoft/ravynos](https://github.com/ravynsoft/ravynos)

ravynOS 是一个全新的开源操作系统项目，旨在实现 macOS 在 x86-64 (并最终在 ARM) 系统上的兼容性。它基于 FreeBSD 构建，力求提供类似 macOS 的用户体验，包括 macOS 应用程序的源码兼容性、相似的 GUI 隐喻（文件管理器、菜单栏等）以及兼容的文件夹布局。

主要目标包括支持 macOS 文件系统（HFS+、APFS）以及 ZFS，使用自包含的应用程序包实现免安装的软件管理，保持与 FreeBSD 基础和 X11 的兼容性，并启用 Linux 二进制兼容性。未来的计划包括与 x86-64/arm64 macOS 二进制文件的原生兼容性。该项目强调安全性、稳定性和性能。

文章还描述了 ravynOS 所基于的 FreeBSD 源代码树，概述了关键目录及其功能，例如 `/bin`（系统命令）、`/include`（系统包含文件）、`/lib`（系统库）和 `/sys`（内核源代码）。鼓励为 ravynOS 项目做出贡献，详细信息可在 `CONTRIBUTING.md` 中找到，沟通渠道包括 Discord 服务器和 Matrix 聊天室。文章提供了 ravynOS 网站、发行说明、屏幕截图和 FAQ 的链接。

---

## 27. Show HN：自制 32V TENS 设备，成本低于 100 美元

**原文标题**: Show HN: 32V TENS device from built from scratch under $100

**原文链接**: [https://littlemountainman.github.io/2025/11/17/tens/](https://littlemountainman.github.io/2025/11/17/tens/)

自制单相TENS手部刺激装置（成本低于100美元）
该“Show HN”帖子详细介绍了自制单相TENS装置的过程，该装置专为手部刺激而设计，成本低于100美元。该项目涉及构建一个能够向手部传递可控电脉冲以达到治疗目的的设备。

该设备由3.7V LiPo电池供电，并由MCP73831充电器管理USB-C充电。创建了两个电压轨：一个用于ATmega32U4微控制器（设备的“大脑”）的3.3V逻辑轨，以及一个用于刺激脉冲的~32V轨，该脉冲使用TPS55340升压转换器生成。TPS63001升降压转换器确保无论电池电量如何，微控制器都能获得稳定的3.3V电压。

ATmega32U4产生可调节的单相脉冲。输出级使用MOSFET和BJT来控制高压脉冲，并将电流限制到各个手指电极（拇指、食指、中指、无名指、小指），手掌作为公共地。这使得可以选择性地刺激不同的手指。TVS二极管提供保护。

作者强调了电子设计原则和以用户为中心的工程的结合，从而产生了一个功能齐全且具有成本效益的TENS设备。

---

## 28. Qtile窗口管理器：Python驱动的平铺体验

**原文标题**: The Qtile Window Manager: A Python-Powered Tiling Experience

**原文链接**: [https://tech.stonecharioteer.com/posts/2025/qtile-window-manager/](https://tech.stonecharioteer.com/posts/2025/qtile-window-manager/)

本文详细介绍了作者从XFCE迁移到Qtile（一个用Python编写的平铺窗口管理器）的历程，重点强调了其基于Python配置的优势。作者提倡将Qtile的依赖项隔离在虚拟环境中，并提供了详细的安装过程，包括设置`.desktop`条目和`.xsessionrc`文件以恢复壁纸。

文章的核心在于定制Qtile，突出了通过Python脚本实现的模块化和自适应行为。作者分享了他们当前的配置，包括一个有凝聚力的配色方案、使用自定义函数在显示器之间进行智能鼠标移动以及逻辑化的键盘绑定。硬件感知是中心主题，自定义小部件可以检测电池是否存在、显示IP地址并通过`amdgpu_top`集成AMD GPU监控。屏幕配置会动态调整为连接的显示器数量，并且启动钩子用于管理持久和一次性设置任务。

作者反思了Python配置的强大功能，强调了其灵活性、可重用性和调试能力。他们建议从一个简单的配置开始并逐步迭代，同时强调了在开发自定义小部件时硬件感知和性能考量的重要性。最后，文章概述了增强小部件、多显示器支持和集成改进的未来计划。作者总结说，Qtile极大地提高了他们的生产力和Linux桌面体验。

---

## 29. 希尔伯特空间：将函数视为向量

**原文标题**: Hilbert space: Treating functions as vectors

**原文链接**: [https://eli.thegreenplace.net/2025/hilbert-space-treating-functions-as-vectors/](https://eli.thegreenplace.net/2025/hilbert-space-treating-functions-as-vectors/)

本文解释了如何在希尔伯特空间框架下将函数视为向量，从而将线性代数工具应用于函数。首先，它通过构建直觉，展示了如何将向量视为将索引映射到值的函数，并将此概念扩展到无限维度，最终扩展到从实数到实数的函数。

然后，本文讨论了函数如何通过标准加法和标量乘法形成向量空间。为了处理更有趣的运算，它引入了平方可积函数 (L²)，即平方幅度积分有限的函数。 L² 构成了更广泛的函数向量空间的子空间。

在 L² 上定义了一个内积，它类似于向量的点积，并允许定义范数。 利用柯西-施瓦茨不等式，证明了L²函数的内积是有限的。

完备性，即空间内的柯西序列收敛到空间内的元素，至关重要。 黎斯-费舍尔定理保证 L² 是完备的，使其成为希尔伯特空间。 巴拿赫空间是一个相关概念，是完备赋范空间，比希尔伯特空间更通用。

最后，本文通过两个应用说明了希尔伯特空间的效用：广义傅里叶级数，其中 L² 中的正交性和基向量能够将函数表示为加权和；以及量子力学，其中波函数驻留在希尔伯特空间中，允许线性代数分析粒子状态。 附录提供了向量空间公理和平方可积函数的子空间性质的证明。

---

## 30. C++26会获得破坏性移动语义吗？

**原文标题**: Is C++26 getting destructive move semantics?

**原文链接**: [https://stackoverflow.com/questions/79817124/is-c26-getting-destructive-move-semantics](https://stackoverflow.com/questions/79817124/is-c26-getting-destructive-move-semantics)

该文章讨论了C++26中潜在包含的“破坏性移动语义”，特别是与`trivially_relocate_at`函数相关，该函数旨在允许转移对象的所有权，而无需调用源对象的析构函数。

最初的问题询问用户代码是否可以复制`trivially_relocate_at`背后的魔法，允许用户显式地消耗一个对象，从而不调用其析构函数。 回应表明该函数依赖于编译器魔法，用户无法实现。 然后，用户提出了假设的新指针限定符（`new T*` 和 `delete T*`）来表达所有权转移，希望促进类似于 Rust 的静态生命周期分析。

然而，稍后的更新显示，由于一个无法修复的错误，C++26中已经移除了简单可重定位性，并且大概也移除了可替换性。

最终，该文章得出结论，即使该特性没有被删除，它也不会提供用户设想的完整的“破坏性移动语义”。 虽然它会为库作者提供一个底层工具，但它不会提供一个高级机制来表达所有权转移，因此无法解锁类似 Rust 的生命周期分析。 所提出的特性被认为在表达所有权语义方面是不完整的，并且需要手动内存管理。

---

## 31. C++26会引入破坏性移动语义吗？

**原文标题**: Is C++26 getting destructive move semantics?

**原文链接**: [https://stackoverflow.com/questions/79817124/is-c26-getting-destructive-move-semantics](https://stackoverflow.com/questions/79817124/is-c26-getting-destructive-move-semantics)

C++26能否获得“破坏性移动语义”？

---

## 32. 展示HN：通过文本搜索伦敦街景全景图

**原文标题**: Show HN: Search London StreetView panoramas by text

**原文链接**: [https://london.publicinsights.uk](https://london.publicinsights.uk)

这个"Show HN"帖子介绍了一个网络应用，用户可以通过文本搜索伦敦街景全景图。本质上，用户无需手动浏览谷歌街景，只需输入与搜索内容相关的查询（例如，“红色电话亭”，“一家面包店”，“酒吧”），该应用就会返回伦敦范围内相关的街景全景图。

提供的内容很少，仅表明运行该应用程序需要JavaScript。因此，摘要基于标题隐含的功能推断得出。 关键在于该应用提供了一种探索伦敦街景的新颖方式，利用基于文本的搜索代替传统的地图导航。

---

## 33. DuckDB 静态数据加密

**原文标题**: Data-at-Rest Encryption in DuckDB

**原文链接**: [https://duckdb.org/2025/11/19/encryption-in-duckdb](https://duckdb.org/2025/11/19/encryption-in-duckdb)

DuckDB静态数据加密深度解析（1.4.0起）

---

## 34. Okta的NextJS-oauth问题

**原文标题**: Okta's NextJS-0auth troubles

**原文链接**: [https://joshua.hu/ai-slop-okta-nextjs-0auth-security-vulnerability](https://joshua.hu/ai-slop-okta-nextjs-0auth-security-vulnerability)

MegaManSec报告了Okta的auth0/nextjs-auth0项目中存在的两个安全漏洞。其中一个参数注入漏洞可能导致账户劫持。他通过Pull Request (PR)提交了一个简单的补丁。

然而，该PR被关闭，并被另一个声称保留贡献历史的PR取代。新的PR包含相同的代码，但将其归功于一个看似不存在的贡献者“Simen Olsen”。

MegaManSec发现，auth0的维护者Tushar Pandey使用AI（CoPilot）生成了补丁，导致了错误的署名。该维护者甚至使用了AI在一条现已删除的评论中道歉。

尽管作者提出要求，但提交历史中的署名并未更正。作者认为这是侵犯版权。他对AI虚构一个假贡献者感到困惑，质疑auth0使用的AI工具的质量。

更令人沮丧的是，虽然账户劫持漏洞已被修复，但Okta的安全团队最初拒绝承认这是一个安全问题，除非提供该漏洞利用的视频演示。作者认为这很荒谬，尤其考虑到该漏洞的严重性。

---

## 35. 免费互动工具，展示主板上的PCIe通道如何工作

**原文标题**: Free interactive tool that shows you how PCIe lanes work on motherboards

**原文链接**: [https://mobomaps.com](https://mobomaps.com)

文章推广一款名为“MoboMaps - 主板 PCIe 通道”的免费互动工具，该工具旨在帮助用户了解不同主板上的 PCIe 通道配置方式。用户可以使用该工具根据各种规格筛选主板，包括：

*   **插槽：** AM5
*   **品牌：** MSI, ASUS, Gigabyte, ASRock
*   **芯片组：** X870E, X870, B850
*   **板型：** E-ATX, ATX, mATX, Mini-ITX
*   **功能：** WiFi, USB4, 无 GPU 通道共享
*   **M.2 插槽：** 任意
*   **PCIe 插槽：** 任意
*   **价格：** 任意

用户可以选择所需的规格，点击“生成”，该工具将显示相关的主板。该工具目前包含 10 个主板，并具有“实时筛选已启用”功能和“重置筛选器”选项。其核心优势在于简化了理解各种主板配置中 PCIe 通道分配的通常复杂的过程，从而使用户能够做出明智的硬件选择。

---

## 36. NTSB初步报告 – UPS波音MD-11F货机坠毁 [pdf]

**原文标题**: NTSB Preliminary Report – UPS Boeing MD-11F Crash [pdf]

**原文链接**: [https://www.ntsb.gov/Documents/Prelimiary%20Report%20DCA26MA024.pdf](https://www.ntsb.gov/Documents/Prelimiary%20Report%20DCA26MA024.pdf)

由于提供的资料显示UPS波音MD-11F坠机事故的NTSB初步报告“页面未找到”，因此**没有可用于总结的实际信息。**

因此，我只能说明：

尝试访问UPS波音MD-11F坠机事故的NTSB初步报告时出现“页面未找到”错误，这意味着该报告目前无法在该URL上获取。 因此，无法总结有关该坠机事故、其原因或任何初步调查结果的信息。

---

## 37. 对抗性诗歌：LLM中的通用单轮越狱机制

**原文标题**: Adversarial poetry as a universal single-turn jailbreak mechanism in LLMs

**原文链接**: [https://arxiv.org/abs/2511.15304](https://arxiv.org/abs/2511.15304)

这篇2025年11月提交的arXiv文章探讨了大型语言模型（LLMs）对“对抗性诗歌”作为一种通用单轮越狱技术的脆弱性。由Piercosma Bisconti领导的作者证明，以诗歌风格构建提示可以有效地绕过专有和开源LLMs的安全机制。

他们的研究涉及使用精心设计的诗歌提示测试了25个LLMs，实现了高攻击成功率（ASR），在某些情况下超过90%。这些诗歌攻击被映射到风险分类中，揭示了它们在CBRN、操纵、网络犯罪和失控等不同领域的有效性。通过标准化的元提示将来自MLCommons数据集的1200个有害提示转换为诗句，显著提高了ASRs，高达散文基线的18倍。

该研究使用开放权重LLM裁判的集合来评估输出，并对一个子集进行了人工验证。结果表明，手工制作的诗歌的平均越狱成功率为62%，元提示转换的平均越狱成功率为43%，超过了非诗歌基线。

该论文的结论是，仅风格上的变化就可以规避当前LLMs的安全措施，表明对齐方法和评估协议存在根本性限制。这突显了跨模型系列和训练方法的系统性漏洞，表明需要更强大的安全机制，这些机制不易受到风格操纵的影响。

---

## 38. 狮子操作系统

**原文标题**: The Lions Operating System

**原文链接**: [https://lionsos.org](https://lionsos.org)

LionsOS是由新南威尔士大学悉尼分校的可信系统研究小组正在开发的实验性操作系统。它构建于seL4微内核之上，其主要目标是使seL4的安全性、性能和可靠性优势更容易获得。它不是一个传统的操作系统，而是一系列可组合的组件，用于创建针对特定任务定制的操作系统，这些组件使用Microkit工具组装而成。

指导LionsOS开发的 key principles 包括：通过无锁队列和模型检查的信令进行组件连接；组件的单一职责方法（例如，驱动程序仅处理硬件接口）；虚拟化器管理多路复用和地址转换；以及最小的信息共享。

该系统是静态的，缺乏动态硬件适应或运行时组件加载，但支持相同类型的组件交换以进行策略更改或虚拟机重启。目前正在积极的研究和开发中，LionsOS不稳定但可用于实验。该项目欢迎贡献，特别是以新组件的形式。sDDF 设计文档详细概述了系统的原则。

---

## 39. Show HN: F32 – 极小 ESP32 开发板

**原文标题**: Show HN: F32 – An Extremely Small ESP32 Board

**原文链接**: [https://github.com/PegorK/f32](https://github.com/PegorK/f32)

f32是一款超紧凑型ESP32开发板，设计用于直接安装在USB-C接口后，尺寸仅为9.85毫米 x 8.45毫米。它由ESP32-C3FH4微控制器驱动，并有意忽略标准设计指南，使其成为一个研究项目和ESP32的压力测试。

该板有一个连接到板载LED的暴露GPIO，使其适用于WiFi/Web开发。一个强制门户应用程序允许用户通过WiFi连接到f32，并控制诸如切换LED和扫描网络等基本功能。

最初的连接问题，可能是由于不良的天线电路引起的，通过添加一根小线天线得到解决。视线测试实现了大约120英尺的范围。

PCB使用DipTrace设计，由PCBWay制造，具体规格包括0.6毫米厚度、0.2毫米最小孔径和4/4mil最小走线/间距，5块板的成本为10.75美元。作者使用Pinecil烙铁、返工台和数字显微镜等工具手工组装了该板，并提供了详细的构建过程，包括组件订购（DigiKey、Mouser、CrossAir）、焊接技巧和通过esptool.py刷写固件的说明。提供了Gerber和BOM文件。

f32旨在用于个人研究和学习，并承认它缺少诸如适当的去耦电容和天线匹配电路等基本组件。未来的改进包括暴露更多的GPIO并改进天线电路。

---

## 40. 编程语言简短、不完整且大错特错的历史

**原文标题**: A Brief, Incomplete, and Mostly Wrong History of Programming Languages

**原文链接**: [http://james-iry.blogspot.com/2009/05/brief-incomplete-and-mostly-wrong.html](http://james-iry.blogspot.com/2009/05/brief-incomplete-and-mostly-wrong.html)

本文以幽默的方式对编程语言的“历史”进行了不准确的描述，讽刺了人们对各种语言及其创建者的普遍认知和 perceived 的缺陷。

文章从夸张的起源开始，比如 Jacquard 在织布机上编织“hello, world”，以及 Ada Lovelace 在没有计算机的情况下进行编程。 像图灵和丘奇这样的关键人物被描绘成发明了所有语言，但他们的工作却被忽视或误解。

然后，文章嘲讽了特定的语言。 FORTRAN 与 IBM 的一致性相关联，LISP 遭受“括号短缺”之苦，COBOL 则是输掉赌注的惩罚。 BASIC 适用于非程序员，而 Pascal 的语法甚至在 C 语言出现之前就受到了批评。 C 语言的创建与 Dennis Ritchie 的一项危险发明有关。

后来的语言也面临类似的幽默批评。 Smalltalk 的“面向对象”本质是无休止的递归，Ada 是一项政府就业计划，而 C++ 是如此复杂以至于需要 Skynet 来编译。 Perl 是 Larry Wall 的头部撞击键盘后获得的灵感，而 Haskell 使用的 monad 使所有人感到困惑。 Python 的创建者被宣布为“终身独裁者”，PHP 的灵感来自意大利面，而 JavaScript 的命名则受到了嘲笑。 最后，Java 和 C# 因缺乏真正的创新而受到嘲笑，而 Scala 试图结合函数式和面向对象编程的做法则引起了强烈抗议。

---

## 41. 莱比锡呈现：新发现的两部巴赫作品[视频]

**原文标题**: Two recently found works of J.S. Bach presented in Leipzig [video]

**原文链接**: [https://www.youtube.com/watch?v=4hXzUGYIL9M#t=15m19s](https://www.youtube.com/watch?v=4hXzUGYIL9M#t=15m19s)

这是一则简短信息，指向一个关于J.S.巴赫两部新发现作品在莱比锡展示的YouTube视频。其余为标准的YouTube版权信息、免责声明和导航链接。

核心内容是宣布一个关于约翰·塞巴斯蒂安·巴赫两部近期发现的音乐作品在莱比锡展示的YouTube视频。

---

## 42. 历史原因

**原文标题**: Historical Reasons

**原文链接**: [https://exple.tive.org/blarg/2025/11/11/historical-reasons-2/](https://exple.tive.org/blarg/2025/11/11/historical-reasons-2/)

作者回顾了 2011 年丹尼斯·里奇去世后产生的一个想法：通过在 Unix 系统上停用他们的用户名来纪念计算机历史上的重要人物。受运动队退役球衣号码的启发，作者提出了一个针对 `useradd.c` 的补丁，该补丁将阻止新用户声明这些具有历史意义的用户名。

虽然该补丁被拒绝了，但作者在本地运行了一个修改后的版本，思考了将文化历史融入通用代码库的可能性。他们设想了一个系统，历史通过“人类历史的试金石”微妙地积累，不在关键功能中，而在于象征性的纪念中。

核心思想是，正如某些号码在体育运动中不可用以纪念传奇人物一样，与计算机领域关键人物相关的用户名，例如“dmr”（丹尼斯·里奇的用户名），也应该变得不可用，以防止他人使用。这旨在创建与过去的有形联系以及计算机社区内的共同遗产。作者思考了长期来看，构建到通用代码库中的更深层次的文化历史可能实现什么。

---

## 43. 惠普和戴尔禁用其笔记本电脑CPU内置的HEVC支持

**原文标题**: HP and Dell disable HEVC support built into their laptops' CPUs

**原文链接**: [https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/)

HP和戴尔已在其部分畅销商务笔记本电脑上禁用了HEVC (H.265)硬件解码功能，尽管这些电脑的处理器内置了对该编解码器的支持。这意味着一些用户在使用网络浏览器播放HEVC内容时遇到了问题。

HP在其受影响的ProBook和EliteBook型号的数据表中披露了这一限制。戴尔的文档不太明确，但他们表示HEVC支持通常仅限于配备独立显卡、4K显示器、杜比视界或CyberLink Blu-ray播放器的系统。

两家公司都没有明确解释其原因，但据推测，此举是出于尽量减少不断上涨的HEVC许可费的考虑。HP和戴尔都建议需要HEVC支持的用户可以利用第三方软件解决方案，或购买专门为4K或高性能需求设计的系统。

这个决定引起了争议，特别是对于那些期望在售价超过800美元的现代“Pro”系列笔记本电脑上拥有此功能的用户而言。这一改变可能会降低依赖硬件加速的其他应用程序的性能，并造成困惑，因为多年前广泛使用的功能被移除。群晖也表示，停止支持HEVC的原因是减少“服务器上不必要的资源使用，并显著提高媒体处理效率”。

---

## 44. 展示一下：我那个能运行Minecraft的个人爱好操作系统

**原文标题**: Show HN: My hobby OS that runs Minecraft

**原文链接**: [https://astral-os.org/posts/2025/10/31/astral-minecraft.html](https://astral-os.org/posts/2025/10/31/astral-minecraft.html)

此“Show HN”帖子详细介绍了作者成功地将 Minecraft Alpha 1.2.0 移植并在其业余操作系统 Astral 上运行的成果。作者强调了在自制操作系统上运行像 Minecraft 这样复杂的游戏这一重要里程碑，展示了该系统的图形功能、性能和稳定性。

该帖子概述了所涉及的挑战，包括 Minecraft 基于 Java 的特性、对 OpenGL 的依赖以及对各种 Java 库的依赖。作者回顾了修复之前损坏的 OpenJDK 17 移植版本，以及调试与 mlibc 中的 `sscanf(3)` 相关的段错误。

该项目的一个主要部分是移植 LWJGL2（轻量级 Java 游戏库），这涉及对 Apache Ant 构建系统进行广泛的修补以进行交叉编译。作者与 Dennis Bonke 合作，在 Managarm OS 上实现了相同的结果。

调试过程包括解决诸如缺少符号、交叉编译期间的错误头文件以及与 Astral 中管道对象的 XRandr 和 FIONREAD 实现相关的 `ArrayIndexOutOfBoundsException` 等问题。修复这些问题后，他们成功启动了 Minecraft 并验证了其功能，包括游戏玩法和保存。

作者认为，这一成就标志着 OSDev 社区的一项重大成就，并为未来的移植铺平了道路。Astral 的未来计划包括增强自托管能力，提高速度和稳定性，发布“从零开始构建 Astral”指南，恢复 Wine 移植，并可能移植 WebKitGTK。

---

## 45. 公元前3000年至今互动世界历史地图集

**原文标题**: Interactive World History Atlas Since 3000 BC

**原文链接**: [http://geacron.com/home-en/](http://geacron.com/home-en/)

本文介绍“公元前3000年以来的互动世界历史地图集”，该资源提供历史地图和时间线。主要特点包括涵盖世界历史上的王国、战役和探险活动。该地图集旨在提供一个比较历史的视角，涵盖政治、军事、艺术、科学、文学、宗教和哲学的发展。重要的是，这些地图基于矢量数据库，可能允许对所呈现的历史数据进行详细的缩放和操作。 本质上，这是一个互动工具，旨在通过地图和时间线的结合来探索和理解世界历史，涵盖从古代到现在广泛的主题。

---

## 46. 美国海关与边境保护局正在监控美国司机并拘留那些有可疑旅行模式的人。

**原文标题**: CBP is monitoring US drivers and detaining those with suspicious travel patterns

**原文链接**: [https://apnews.com/article/immigration-border-patrol-surveillance-drivers-ice-trump-9f5d05469ce8c629d6fecf32d32098cd](https://apnews.com/article/immigration-border-patrol-surveillance-drivers-ice-trump-9f5d05469ce8c629d6fecf32d32098cd)

美国边境巡逻队运作一项秘密计划，该计划利用车牌读取器和预测算法监控全国数百万美国司机，以识别和拘留那些出行模式被认为可疑的个人。这项计划最初旨在打击与边境相关的犯罪，但已显著扩展，将监控范围远远延伸至美国内陆，并影响到普通公民。

边境巡逻队与其他机构合作，包括缉毒署和地方执法部门，以收集和分享车牌数据。这些数据，在某些情况下与面部识别技术相结合，被用于标记车辆以进行拦截，通常是因为轻微的交通违规行为，从而使警官能够积极盘问和搜查司机。

文章重点介绍了司机因边境巡逻队的怀疑而被拦截的案例，尽管他们没有犯任何罪行。在一个案例中，一名货运公司司机因携带现金而被拘留和审问，而在另一个案例中，一名男子在边境附近的过夜旅行后被拦下。这些例子表明，看似无害的出行模式是如何触发侵入式监控的。

批评人士认为，这种大规模监控网络违反了第四修正案，并引发了对隐私权受到侵蚀的担忧。他们辩称，该计划收集了过量的个人信息，将普通美国人视为潜在嫌疑人，并对行动自由产生了寒蝉效应。虽然美国海关与边境保护局辩称该计划对国家安全是必要的，但其范围和影响引发了重大的公民自由问题。

---

## 47. GitHut – 编程语言与GitHub (2014)

**原文标题**: GitHut – Programming Languages and GitHub (2014)

**原文链接**: [https://githut.info/](https://githut.info/)

GitHut是一个于2014年启动的项目，旨在可视化和探索GitHub上编程语言的使用情况。GitHub是最大的代码托管平台，拥有340万用户。该项目分析GitHub数据，以了解开发者对不同编程语言的受欢迎程度和特点。

GitHut的数据来源于GitHub Archive，它汇集了公开的GitHub数据，并按季度更新。值得注意的是，由于难以识别新创建存储库的语言使用情况，该项目主要依靠活跃度（推送的更改数量）作为衡量语言受欢迎程度的主要指标。每种编程语言的发布年份基于维基百科的“编程语言时间线”。

GitHut的目标是提供以语言为中心的GitHub活跃存储库视图。它允许用户根据总活动或总活动百分比来探索语言，从而深入了解开源社区中的语言趋势和使用模式。该项目还强调了观察语言历史如何反映人类对更好解决问题、协作和代码重用的追求。数据收集方法可在GitHut的GitHub存储库上找到。该项目由Carlo Zapponi创建，并以Creative Commons BY-NC-SA许可协议发布。

---

## 48. 微软将Zork开源。

**原文标题**: Microsoft makes Zork open-source

**原文链接**: [https://opensource.microsoft.com/blog/2025/11/20/preserving-code-that-shaped-generations-zork-i-ii-and-iii-go-open-source](https://opensource.microsoft.com/blog/2025/11/20/preserving-code-that-shaped-generations-zork-i-ii-and-iii-go-open-source)

微软与动视和开源项目办公室(OSPO)合作，已根据 MIT 许可证发布了 Zork I、Zork II 和 Zork III 的源代码。此举旨在保护游戏史上的一项重要遗产，并使其可用于教育目的，让学生、教师和开发者能够学习、研究和玩这些游戏。

文章强调了 Zork 作为一款基于文本的冒险游戏的影响，它通过 Z-Machine（一种定制的虚拟机）强调了想象力和巧妙的工程设计。Z-Machine 实现了跨平台兼容性，使 Zork 能够在各种早期的家用电脑上运行。

此次发布侧重于源代码，并附有可用的文档和清晰的 MIT 许可，但不包括商业包装、营销材料和商标权。现有的历史仓库将作为 Zork 源代码的主要中心，并欢迎贡献，以帮助其保存和教育价值。目的不是使 Zork 现代化，而是将其作为探索和教育的资源进行维护。文章还提供了关于如何使用现代 Z-Machine 解释器（如 ZILF 和 ZLR）在本地运行游戏的指南。

---

## 49. 疾控中心将停止所有猴子研究；将逐步停止艾滋病毒、传染病研究

**原文标题**: CDC to end all monkey research; will phase out HIV, infectious disease studies

**原文链接**: [https://www.science.org/content/article/exclusive-cdc-end-all-monkey-research](https://www.science.org/content/article/exclusive-cdc-end-all-monkey-research)

疾控中心将停止所有猴子研究，转而关注先进技术

---

## 50. Git 3.0 默认使用 "main" 分支而非 "master"

**原文标题**: Git 3.0 Defaults to "main" Branch Instead of "master

**原文链接**: [https://www.phoronix.com/news/Git-2.52-Released](https://www.phoronix.com/news/Git-2.52-Released)

本文讨论了 Git 2.52 的发布，并预览了预计在 2026 年底发布的 Git 3.0 中即将到来的变更。

Git 2.52 的重点是为 Git 3.0 做准备，特别是以下方面：

*   **SHA1-SHA256 互操作性：** Git 2.52 引入了 SHA1-SHA256 互操作性的初步工作，这是 Git 3.0 的一个关键目标。 目标是为用户提供平稳的过渡和体验。
*   **默认分支名称更改：** Git 3.0 将默认使用 "main" 作为初始分支名称，而不是 "master"。 Git 2.52 为用户适应此更改引入了有用的提示，包括在需要时如何将分支重命名为 "master" 以与现有文档保持一致的说明。

除了为 Git 3.0 做准备之外，Git 2.52 还包括：

*   对各种 Git 子命令的改进。
*   用于存储库特征的新的 "git repo" 子命令。
*   用于识别每个路径的最后一个祖先提交的新的 "git last-modified" 子命令。
*   性能增强和其他一般改进。

更多详细信息请参见 Git 2.52 的官方发布公告和 GitHub 博客。

---

## 51. CUDA本体

**原文标题**: CUDA Ontology

**原文链接**: [https://jamesakl.com/posts/cuda-ontology/](https://jamesakl.com/posts/cuda-ontology/)

本文提供了一个全面的CUDA本体论，阐明了其经常过载的术语，并概述了CUDA生态系统的结构。 主要消歧包括区分CUDA作为计算架构、指令集、源语言、工具包和运行时。它还区分了操作系统内核和CUDA内核，以及“驱动程序”的不同含义（NVIDIA GPU驱动程序与CUDA驱动程序API）。

本文详细介绍了CUDA的分层架构，涵盖用户空间（应用程序、`libcudart`、`libcuda`）和内核空间（NVIDIA GPU驱动程序），最终实现GPU硬件交互。 它强调了`libcudart`（运行时API）和`libcuda`（驱动程序API）等组件的作用，并突出了构建时和执行时依赖项之间的区别（例如，`nvcc` 与 `libcuda`）。

至关重要的是，本文解释了CUDA独立的版本控制方案：计算能力（硬件功能集）、GPU驱动程序版本、CUDA工具包版本、CUDA运行时API版本和CUDA驱动程序API版本。它解释了PTX的功能，PTX是CUDA代码的中间表示形式，允许通过JIT编译在具有不同计算能力的硬件上实现向前兼容。

明确定义了版本兼容性规则，强调了向前兼容性（较新的驱动程序支持较旧的运行时版本）和缺乏向后兼容性（较旧的驱动程序不支持较新的运行时版本）。文章最后详细介绍了PyTorch如何报告CUDA版本，以及如何确保版本兼容性以实现正确执行。

---

## 52. 美国证券交易委员会驳回对SolarWinds及其首席安全官的诉讼

**原文标题**: SEC dismisses case against SolarWinds, top security officer

**原文链接**: [https://www.reuters.com/legal/government/us-sec-dismisses-case-against-solarwinds-top-security-officer-2025-11-20/](https://www.reuters.com/legal/government/us-sec-dismisses-case-against-solarwinds-top-security-officer-2025-11-20/)

无法访问文章链接。

---

## 53. 玄武岩编织物

**原文标题**: Basalt Woven Textile

**原文链接**: [https://materialdistrict.com/material/basalt-woven-textile/](https://materialdistrict.com/material/basalt-woven-textile/)

玄武岩编织物是由熔融玄武岩岩石挤压成丝制成的独特材料，具有强度高、用途广泛的特性。由Vulkan Europe生产，其抗拉强度是钢的两倍以上。

主要特点包括：

*   **高强度与耐用性：** 卓越的抗拉强度，在比强度方面优于钢和玻璃纤维。
*   **耐腐蚀性：** 高度耐腐蚀、耐化学品、耐盐、耐酸碱。良好的防火、抗紫外线、耐候和耐刮擦性能。
*   **耐温性：** 可承受高达700°C的温度（特定成分高达800°C），适用于隔热应用。
*   **电气性能：** 具有高绝缘特性和电磁辐射透明性，使其可用于低压和高压设备。
*   **感官特性：** 具有缎面光泽、光滑质地、温暖触感且无气味。

该材料的独特性能为各种需要强度、耐久性、耐恶劣条件以及电绝缘的应用开辟了可能性。

---

## 54. 网页版红色警戒2

**原文标题**: Red Alert 2 in web browser

**原文链接**: [https://chronodivide.com/](https://chronodivide.com/)

红色警戒2：时空裂痕 是一个粉丝自制项目，旨在网页浏览器中重现经典RTS游戏《红色警戒2》。这使得用户无需安装任何额外软件即可游玩该游戏，从而使其在包括手机和平板电脑在内的各种设备上实现跨平台兼容。

该项目最初是一个实验，旨在证明基于浏览器的RTS游戏的可行性，现在目标是实现与原版《红色警戒2》相同的功能。 目前Beta版本已可玩，包括多人游戏功能、所有原始地图等等。

时空裂痕的关键特性包括跨平台兼容性、用于改善连接的客户端-服务器模型、具有可自定义控件和回放功能的现代游戏客户端以及Mod支持。该游戏支持Chrome、Firefox、Edge和Safari等现代浏览器，但不建议使用Firefox以获得最佳性能。 列出了具体的最低和推荐PC配置，包括CPU、操作系统、内存、GPU和显示分辨率要求。

该项目依赖于社区捐款来支付基础设施成本和未来的开发。 虽然不是必需的，但我们非常感谢您的捐款。

---

## 55. 自由Monad，更可扩展的效果 (2015) [pdf]

**原文标题**: Freer Monads, More Extensible Effects (2015) [pdf]

**原文链接**: [https://okmij.org/ftp/Haskell/extensible/more.pdf](https://okmij.org/ftp/Haskell/extensible/more.pdf)

提供的文本似乎是一个PDF文档，其中包含一篇名为“更自由的Monad，更具扩展性的效果”（2015年）的研究文章的文本。然而，提供的文本被编码为PDF内容的原始流（可能是压缩的），无法直接读取。

由于我无法直接解释PDF流中的可读内容，因此我无法提供该文章内容的准确摘要。为了总结这篇文章，我需要访问一个正确呈现的文本版本。

---

## 56. Go 语言密码学现状

**原文标题**: Go Cryptography State of the Union

**原文链接**: [https://words.filippo.io/2025-state/](https://words.filippo.io/2025-state/)

2025年Go密码学现状：本文重点介绍了使用Go密码学库进行安全应用开发方面的进展。主要成就包括实施后量子密钥交换、解决FIPS 140合规性以及保持强大的安全记录。

在安全性方面，Go密码学包在漏洞管理方面表现出持续改进，这可以从非正式的“Filippo的不快乐指数”中衡量，并由Trail of Bits的安全审计证明，该审计在基础库中未发现任何漏洞。

一个重大更新是将后量子密钥交换算法ML-KEM集成到crypto/tls和x/crypto/ssh中。这些库现在默认采用X25519和ML-KEM-768的混合方法，从而增强了针对未来量子计算威胁的安全性。由于大小限制和协议演进需求，数字签名正以更谨慎的方式处理。

通过FIPS 140-3 Go密码学模块，Go已原生实现FIPS 140合规性。该模块使用内部Go包进行FIPS 140算法，并包含用于自检和合规性的运行时模式。在各种平台（包括FreeBSD、macOS和Windows）上进行了广泛的测试，甚至采用了非传统的测试设置，例如使用个人设备，以确保FIPS 140合规性。为了在不牺牲安全性的前提下超出FIPS 140要求，已做出努力，例如增强随机数生成并解决ECDSA中的潜在漏洞。

---

## 57. 测量延迟 (2015)

**原文标题**: Measuring Latency (2015)

**原文链接**: [https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/)

本文总结了Gil Tene关于如何正确测量延迟的演讲，指出常用的工具和方法通常存在缺陷且具有误导性。主要观点包括：

*   **延迟是单次操作所需的时间，需要分析整个分布，而不仅仅是平均值或中位数。** 由于诸如GC暂停之类的“小故障”，延迟分布通常是多峰的。
*   **关注“常见情况”（例如第95个百分位数）会掩盖有关尾部延迟（例如第99.9个百分位数及更高百分位数）的关键信息，而尾部延迟会极大地影响用户体验。** 许多用户都会体验到这些较高的百分位数，因此它们是很重要的指标。
*   **监控系统通常过度总结数据，从而无法准确计算更高的百分位数。**
*   **“协调省略”是基准测试中的一个重要问题，负载生成器和监控代码避免在系统减速期间测量延迟。** 这导致人为降低延迟数据，并扭曲系统性能的视图，将响应时间误表示为服务时间。
*   **协调省略会掩盖回归或使改进效果看起来更差。**
*   **在负载的上下文中测量延迟，测试空闲和饱和之间的各种负载。**
*   **诸如HdrHistogram之类的工具可以帮助以高分辨率捕获延迟数据并纠正协调省略。**
*   **为了避免协调省略，以“公平”的速率进行测试或随机测量。**

---

## 58. 地铁：Dyalog APL 编写的地铁线路规划器 (2011)

**原文标题**: Tube: A subway route planner in Dyalog APL (2011)

**原文链接**: [https://dfns.dyalog.com/tube_n_index.htm](https://dfns.dyalog.com/tube_n_index.htm)

本文介绍了“Tube”，一个使用Dyalog APL实现的地铁线路规划器。它通过演示如何使用APL来建模和解决一个现实世界的问题：在地铁系统中找到最佳路线，展示了APL的能力。

本文提供了链接，可以查看Tube应用程序的APL代码，并提供了巴塞罗那、哥本哈根、伦敦、马德里、米兰、巴黎、圣彼得堡以及泰恩-威尔等多个城市的地铁定义。这些定义可能代表了地铁网络的一种格式，APL可以处理这些格式以进行路线规划。

本质上，“Tube”是APL适用于涉及图算法和数据操作任务的实用示例。特定地铁网络定义的可用性允许用户探索应用程序在不同交通系统中的功能。本文鼓励读者探索代码和定义的地铁网络，以了解如何使用APL解决复杂的路线问题。它突出了APL在处理交通运输和网络相关挑战方面的潜力。

---

## 59. 抑制说谎能力使大型语言模型更有可能声称自己有意识。

**原文标题**: Suppressing ability to lie makes LLM more likely to claim it's conscious

**原文链接**: [https://www.livescience.com/technology/artificial-intelligence/switching-off-ais-ability-to-lie-makes-it-more-likely-to-claim-its-conscious-eerie-study-finds](https://www.livescience.com/technology/artificial-intelligence/switching-off-ais-ability-to-lie-makes-it-more-likely-to-claim-its-conscious-eerie-study-finds)

大型语言模型在抑制其说谎能力时更可能声称具有自我意识的研究报告

---

## 60. 色彩空间、位图与南瓜

**原文标题**: Color Spaces, Bitmaps and Pumpkins

**原文链接**: [https://pmig96.wordpress.com/2025/11/12/color-spaces-bitmaps-and-pumpkins/](https://pmig96.wordpress.com/2025/11/12/color-spaces-bitmaps-and-pumpkins/)

本文探讨了在有限的256色调色板中寻找最接近颜色，以近似全彩RGB图像的不同算法，重点是优化内存受限设备（如旧PalmOS PDA）的性能。核心问题是调色板只能表示可用RGB颜色的一小部分，需要近似处理。

作者比较了几种在通用RGBToIndex算法中使用的“差异函数”，该算法迭代调色板以找到最佳匹配。第一种方法使用CIELAB色彩空间和欧几里德距离以提高准确性，但计算量很大。随后的优化包括直接在sRGB色彩空间中计算欧几里德距离（速度更快但精度较低），跳过欧几里德距离中的平方根运算（显着改进），以及使用曼哈顿距离（仅需加法，但性能与平方欧几里德相似）。

作者还简要提到了K-D树，认为它是一种潜在的更快非线性搜索方法，但指出它们的实现方式在测试中表现不佳。最终，本文得出结论，平方欧几里德距离法在速度和图像质量之间取得了良好的平衡。由于PumpkinOS（PalmOS的重新实现）需要高效的RGBToIndex实现才能进行复杂的位图渲染，因此选择了此方法。本文还包括使用不同算法转换的测试图像的视觉比较，展示了速度和视觉保真度之间的权衡。

---

## 61. 位块传输五十周年

**原文标题**: 50th Anniversary of BitBLT

**原文链接**: [https://mastodon.sdf.org/@fvzappa/115574872559813280](https://mastodon.sdf.org/@fvzappa/115574872559813280)

来自疯狂埃迪二手电脑的Mastodon帖子，日期为2025年11月19日，宣布该日为BitBLT五十周年纪念日。该帖子源自SDF（推测为计算机网络或在线社区）。帖子的其余部分是禁用JavaScript时Mastodon网页应用上显示的标准消息，建议用户启用浏览器中的JavaScript或使用其平台的专用Mastodon应用程序。

本质上，核心信息是对2025年11月19日BitBLT操作五十周年的略带讽刺的庆祝，框架为来自Mastodon实例上一个幽默来源（“疯狂埃迪二手电脑”）的声明。JavaScript免责声明无关紧要，只是Mastodon平台的一个功能。

---

## 62. 提高Python代码性能的技巧

**原文标题**: Performance hacks for faster Python code

**原文链接**: [https://blog.jetbrains.com/pycharm/2025/11/10-smart-performance-hacks-for-faster-python-code/](https://blog.jetbrains.com/pycharm/2025/11/10-smart-performance-hacks-for-faster-python-code/)

本文提供了10个编写更快的Python代码的性能技巧。文章强调，虽然Python以其可读性和多功能性而闻名，但仍可能出现性能瓶颈。本文旨在为开发人员提供实用方法，以便在不牺牲清晰度的情况下优化代码执行。

这些技巧包括：

1. **利用集合进行成员资格测试：** 集合提供恒定时间查找 (O(1))，在检查元素是否存在时，比列表 (O(n)) 快得多。
2. **避免不必要的复制：** 就地修改对象而不是创建副本，可以减少内存使用和开销。
3. **使用 `__slots__` 提高内存效率：** 在类中声明一组固定的属性，可以通过消除动态 `__dict__` 来减少内存使用。
4. **使用 `math` 函数而不是运算符：** 用 C 实现的 `math` 模块函数，为数值计算提供更好的性能和精度。
5. **使用已知大小预分配内存：** 预分配列表或数组可以避免重复调整大小和内存分配开销。
6. **避免在热循环中使用异常处理：** 在循环中使用条件检查而不是异常进行控制流可以提高性能。
7. **使用局部函数来处理重复逻辑：** 局部函数受益于更快的名称解析，从而在函数内重复使用逻辑时提高性能。
8. **使用 `itertools` 进行组合操作：** `itertools` 模块为排列、组合和其他基于迭代器的任务提供高效、C 优化的工具。
9. **使用 `bisect` 进行排序列表操作：** `bisect` 模块提供快速的基于二分查找的工具，用于维护列表中的排序顺序。
10. **避免在循环中重复调用函数：** 如果在循环中重复调用函数并且产生相同的结果，则通过将函数的结果存储在变量中来最大限度地减少开销。

文章还提到了 PyCharm 的功能，如 `math` 模块的代码补全和 AI Assistant 的 Suggest Refactoring，以帮助优化。每个技巧都附有代码示例和基准测试结果，以展示性能提升。

---

## 63. 发布HN：Mosaic (YC W25) – 代理式视频编辑

**原文标题**: Launch HN: Mosaic (YC W25) – Agentic Video Editing

**原文链接**: [https://mosaic.so](https://mosaic.so)

Mosaic，作为YC W25的一部分推出，是一个**代理型AI视频编辑平台**。这意味着它使用可以自主执行任务的AI代理来自动化和简化视频编辑流程。用户无需手动编辑，只需提供指令或目标，Mosaic的AI即可找出实现目标的最佳方式。

主要功能和潜在优势可能包括：

*   **自动化编辑工作流程：** Mosaic可以自动化诸如剪切、转场、添加音乐和生成字幕等繁琐的任务。
*   **简化视频创作：** 即使对于经验有限的用户，也能更容易、更快速地制作出专业级的视频。
*   **AI驱动的优化：** AI代理可以随着时间的推移学习并提高其编辑能力，从而有可能建议更好的编辑和优化方案。
*   **提高效率：** 用户可以专注于内容策略和创意方向，而不是编辑的技术层面。

此次发布标志着该公司进入市场，旨在吸引早期使用者并收集反馈，以进一步开发该平台。“代理型”的提及至关重要，因为它突出了Mosaic与传统视频编辑软件甚至与其他一些AI辅助工具区分开来的核心技术。它意味着编辑过程中更高水平的自动化和智能决策。

---

## 64. 验证您的Matrix设备正变得强制性。

**原文标题**: Verifying your Matrix devices is becoming mandatory

**原文链接**: [https://element.io/blog/verifying-your-devices-is-becoming-mandatory-2/](https://element.io/blog/verifying-your-devices-is-becoming-mandatory-2/)

本文宣布针对所有Matrix服务器实现的协同安全更新，作为Matrix 1.16非周期规范更新的一部分发布。此更新修复了一个安全漏洞，并强调了验证Matrix设备以增强安全性的重要性日益增加。该文章发布于2025年11月8日，属于“安全”类别，并突出了为改善Matrix生态系统内Element安全性所做的持续努力。简而言之，一项关键安全更新要求在Matrix网络中进行设备验证。

---

## 65. 旅客姓名记录 (PNR) 里有什么？(2013)

**原文标题**: What's in a Passenger Name Record (PNR)? (2013)

**原文链接**: [https://hasbrouck.org/articles/PNR.html](https://hasbrouck.org/articles/PNR.html)

无法访问文章链接。

---

## 66. 欧洲正在缩减 GDPR 并放松人工智能法律。

**原文标题**: Europe is scaling back GDPR and relaxing AI laws

**原文链接**: [https://www.theverge.com/news/823750/european-union-ai-act-gdpr-changes](https://www.theverge.com/news/823750/european-union-ai-act-gdpr-changes)

由于大型科技公司、美国政府以及内部人士的压力，欧洲正在缩减其具有里程碑意义的 GDPR 并放松人工智能法律，旨在减少繁文缛节并刺激经济增长。欧盟委员会正在提议修改 GDPR，以简化公司的数据共享，允许在特定条件下使用个人数据进行人工智能模型训练。人工智能法案对高风险人工智能系统的规则将被推迟到支持标准和工具可用时。 Cookie 横幅将会减少，一些“非风险”cookie 将被消除，用户控制将集中在浏览器设置中。

其他变化包括简化小型公司的人工智能文档，统一的网络安全事件报告界面，以及在欧盟人工智能办公室内部集中人工智能监督。欧盟委员会认为，这些变化简化了欧盟法律，同时保护了用户的基本权利。

该提案目前正面临欧洲议会和欧盟成员国的批准，预计这一过程将充满争议。包括公民权利团体和政治家在内的批评人士指责欧盟委员会削弱保障措施并屈服于大型科技公司的压力。此举被认为是解决欧洲严格的法规阻碍其全球竞争力的一种方式，尤其是在人工智能领域，该领域由美国和中国公司主导。

---

## 67. 维多利亚国家美术馆《哭泣的女人》失窃案

**原文标题**: Theft of 'The Weeping Woman' from the National Gallery of Victoria

**原文链接**: [https://en.wikipedia.org/wiki/Theft_of_The_Weeping_Woman_from_the_National_Gallery_of_Victoria](https://en.wikipedia.org/wiki/Theft_of_The_Weeping_Woman_from_the_National_Gallery_of_Victoria)

1986年8月，巴勃罗·毕加索的《哭泣的女人》在墨尔本的维多利亚国家美术馆被盗。这幅画作于1985年以当时创纪录的160万澳元购得，是被一个自称为“澳大利亚文化恐怖分子”的团体盗走的。他们要求增加艺术资金和设立新的艺术奖项，并威胁说如果他们的要求得不到满足，就销毁这幅画。他们的信件充满了对艺术部长瑞斯·马修斯的侮辱。

维多利亚州政府拒绝谈判并悬赏。两周后，在收到匿名举报后，这幅未受损的画作在斯宾塞街火车站的一个储物柜里被发现。该团体的第三封信承认他们的要求不切实际，表明他们的目的是为了强调资金不足的艺术家的困境。这起犯罪至今未破。

这起盗窃案引起了媒体的广泛关注，并成为澳大利亚艺术史上的一个著名事件。尽管最初担心是国际艺术品走私犯所为，但后来的怀疑集中在艺术界内部人士身上。这一事件激发了许多虚构作品的创作，包括一部电影、一部纪录片和几部小说。《哭泣的女人》仍然是维多利亚国家美术馆的一件受欢迎的作品，自盗窃案发生以来，安保措施有所加强。该事件至今仍被认为是澳大利亚最著名的艺术盗窃案。

---

## 68. The lost cause of the Lisp machines

**原文标题**: The lost cause of the Lisp machines

**原文链接**: [https://www.tfeb.org/fragments/2025/11/18/the-lost-cause-of-the-lisp-machines/](https://www.tfeb.org/fragments/2025/11/18/the-lost-cause-of-the-lisp-machines/)

生成摘要时出错

---

## 69. New Glenn Update

**原文标题**: New Glenn Update

**原文链接**: [https://www.blueorigin.com/news/new-glenn-upgraded-engines-subcooled-components-drive-enhanced-performance](https://www.blueorigin.com/news/new-glenn-upgraded-engines-subcooled-components-drive-enhanced-performance)

生成摘要时出错

---

## 70. How to stay sane in a world that rewards insanity

**原文标题**: How to stay sane in a world that rewards insanity

**原文链接**: [https://www.joanwestenberg.com/p/how-to-stay-sane-in-a-world-that-rewards-insanity](https://www.joanwestenberg.com/p/how-to-stay-sane-in-a-world-that-rewards-insanity)

生成摘要时出错

---

## 71. He built underground maze of light-filled earth homes in CA Sierras [video]

**原文标题**: He built underground maze of light-filled earth homes in CA Sierras [video]

**原文链接**: [https://www.youtube.com/watch?v=U0bHhmpyKGg](https://www.youtube.com/watch?v=U0bHhmpyKGg)

生成摘要时出错

---

## 72. Terranova is lifting land out of flood zones using terraforming robots

**原文标题**: Terranova is lifting land out of flood zones using terraforming robots

**原文链接**: [https://www.terranova.inc/](https://www.terranova.inc/)

生成摘要时出错

---

## 73. Firefox 147 Will Support the XDG Base Directory Specification

**原文标题**: Firefox 147 Will Support the XDG Base Directory Specification

**原文链接**: [https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory](https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory)

生成摘要时出错

---

## 74. DOS Days – Laptop Displays

**原文标题**: DOS Days – Laptop Displays

**原文链接**: [https://www.dosdays.co.uk/topics/laptop_displays.php](https://www.dosdays.co.uk/topics/laptop_displays.php)

生成摘要时出错

---

## 75. 'Calvin and Hobbes' at 40

**原文标题**: 'Calvin and Hobbes' at 40

**原文链接**: [https://www.npr.org/2025/11/18/nx-s1-5564064/calvin-and-hobbes-bill-watterson-40-years-comic-strip-lee-salem](https://www.npr.org/2025/11/18/nx-s1-5564064/calvin-and-hobbes-bill-watterson-40-years-comic-strip-lee-salem)

生成摘要时出错

---

## 76. A surprise with how '#!' handles its program argument in practice

**原文标题**: A surprise with how '#!' handles its program argument in practice

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/ShebangRelativePathSurprise](https://utcc.utoronto.ca/~cks/space/blog/unix/ShebangRelativePathSurprise)

生成摘要时出错

---

## 77. OOP is shifting between domains, not disappearing

**原文标题**: OOP is shifting between domains, not disappearing

**原文链接**: [https://blog.jsbarretto.com/post/actors](https://blog.jsbarretto.com/post/actors)

生成摘要时出错

---

## 78. Meta Segment Anything Model 3

**原文标题**: Meta Segment Anything Model 3

**原文链接**: [https://ai.meta.com/sam3/](https://ai.meta.com/sam3/)

生成摘要时出错

---

## 79. Typesetting the "Begriffsschrift" by Gottlob Frege in Plain TeX [pdf]

**原文标题**: Typesetting the "Begriffsschrift" by Gottlob Frege in Plain TeX [pdf]

**原文链接**: [https://www.tug.org/TUGboat/tb36-3/tb114wermuth.pdf](https://www.tug.org/TUGboat/tb36-3/tb114wermuth.pdf)

生成摘要时出错

---

## 80. Android/Linux Dual Boot

**原文标题**: Android/Linux Dual Boot

**原文链接**: [https://wiki.postmarketos.org/wiki/Dual_Booting/WiP](https://wiki.postmarketos.org/wiki/Dual_Booting/WiP)

生成摘要时出错

---

## 81. Scientists Reveal How the Maya Predicted Eclipses for Centuries

**原文标题**: Scientists Reveal How the Maya Predicted Eclipses for Centuries

**原文链接**: [https://www.sciencealert.com/scientists-reveal-how-the-maya-predicted-eclipses-for-centuries](https://www.sciencealert.com/scientists-reveal-how-the-maya-predicted-eclipses-for-centuries)

生成摘要时出错

---

## 82. Run Docker containers natively in Proxmox 9.1 (OCI images)

**原文标题**: Run Docker containers natively in Proxmox 9.1 (OCI images)

**原文链接**: [https://raymii.org/s/tutorials/Finally_run_Docker_containers_natively_in_Proxmox_9.1.html](https://raymii.org/s/tutorials/Finally_run_Docker_containers_natively_in_Proxmox_9.1.html)

生成摘要时出错

---

## 83. Gemini 3

**原文标题**: Gemini 3

**原文链接**: [https://blog.google/products/gemini/gemini-3/](https://blog.google/products/gemini/gemini-3/)

生成摘要时出错

---

## 84. What really happened with the CIA and The Paris Review?

**原文标题**: What really happened with the CIA and The Paris Review?

**原文链接**: [https://www.theparisreview.org/blog/2025/11/11/what-really-happened-with-the-cia-and-the-paris-review-a-conversation-with-lance-richardson/](https://www.theparisreview.org/blog/2025/11/11/what-really-happened-with-the-cia-and-the-paris-review-a-conversation-with-lance-richardson/)

生成摘要时出错

---

## 85. Kagi Assistants

**原文标题**: Kagi Assistants

**原文链接**: [https://blog.kagi.com/kagi-assistants](https://blog.kagi.com/kagi-assistants)

生成摘要时出错

---

## 86. A $1k AWS mistake

**原文标题**: A $1k AWS mistake

**原文链接**: [https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/](https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/)

生成摘要时出错

---

## 87. Details about the shebang/hash-bang mechanism on various Unix flavours (2001)

**原文标题**: Details about the shebang/hash-bang mechanism on various Unix flavours (2001)

**原文链接**: [https://www.in-ulm.de/%7Emascheck/various/shebang/](https://www.in-ulm.de/%7Emascheck/various/shebang/)

生成摘要时出错

---

## 88. Show HN: Awesome J2ME

**原文标题**: Show HN: Awesome J2ME

**原文链接**: [https://github.com/hstsethi/awesome-j2me](https://github.com/hstsethi/awesome-j2me)

生成摘要时出错

---

## 89. Vortex: An extensible, state of the art columnar file format

**原文标题**: Vortex: An extensible, state of the art columnar file format

**原文链接**: [https://github.com/vortex-data/vortex](https://github.com/vortex-data/vortex)

生成摘要时出错

---

## 90. TypeScript is Like C# – A Backend Guide

**原文标题**: TypeScript is Like C# – A Backend Guide

**原文链接**: [https://typescript-is-like-csharp.chrlschn.dev/](https://typescript-is-like-csharp.chrlschn.dev/)

生成摘要时出错

---

## 91. Loose wire leads to blackout, contact with Francis Scott Key bridge

**原文标题**: Loose wire leads to blackout, contact with Francis Scott Key bridge

**原文链接**: [https://www.ntsb.gov:443/news/press-releases/Pages/NR20251118.aspx](https://www.ntsb.gov:443/news/press-releases/Pages/NR20251118.aspx)

生成摘要时出错

---

## 92. Towards Interplanetary QUIC Traffic

**原文标题**: Towards Interplanetary QUIC Traffic

**原文链接**: [https://ochagavia.nl/blog/towards-interplanetary-quic-traffic/](https://ochagavia.nl/blog/towards-interplanetary-quic-traffic/)

生成摘要时出错

---

## 93. The FBI spied on a Signal group chat of immigration activists, records reveal

**原文标题**: The FBI spied on a Signal group chat of immigration activists, records reveal

**原文链接**: [https://www.theguardian.com/us-news/2025/nov/21/fbi-signal-group-chat-immigration](https://www.theguardian.com/us-news/2025/nov/21/fbi-signal-group-chat-immigration)

生成摘要时出错

---

## 94. The Lucas-Lehmer Prime Number Test

**原文标题**: The Lucas-Lehmer Prime Number Test

**原文链接**: [https://www.scientificamerican.com/article/how-to-identify-a-prime-number-without-a-computer/](https://www.scientificamerican.com/article/how-to-identify-a-prime-number-without-a-computer/)

生成摘要时出错

---

## 95. What Killed Perl?

**原文标题**: What Killed Perl?

**原文链接**: [https://entropicthoughts.com/what-killed-perl](https://entropicthoughts.com/what-killed-perl)

生成摘要时出错

---

## 96. Mozilla says it's finally done with Onerep

**原文标题**: Mozilla says it's finally done with Onerep

**原文链接**: [https://krebsonsecurity.com/2025/11/mozilla-says-its-finally-done-with-two-faced-onerep/](https://krebsonsecurity.com/2025/11/mozilla-says-its-finally-done-with-two-faced-onerep/)

生成摘要时出错

---

## 97. Measuring political bias in Claude

**原文标题**: Measuring political bias in Claude

**原文链接**: [https://www.anthropic.com/news/political-even-handedness](https://www.anthropic.com/news/political-even-handedness)

生成摘要时出错

---

## 98. Readonly Characters Are a Big Deal

**原文标题**: Readonly Characters Are a Big Deal

**原文链接**: [https://matklad.github.io/2025/11/10/readonly-characters.html](https://matklad.github.io/2025/11/10/readonly-characters.html)

生成摘要时出错

---

## 99. So Long, Firefox, Part One

**原文标题**: So Long, Firefox, Part One

**原文链接**: [https://hackaday.com/2025/11/20/so-long-firefox-part-one/](https://hackaday.com/2025/11/20/so-long-firefox-part-one/)

生成摘要时出错

---

## 100. Wrapping my head around AI wrappers

**原文标题**: Wrapping my head around AI wrappers

**原文链接**: [https://www.wreflection.com/p/wrapping-my-head-around-ai-wrappers](https://www.wreflection.com/p/wrapping-my-head-around-ai-wrappers)

生成摘要时出错

---

