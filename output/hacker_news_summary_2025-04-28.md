# Hacker News 热门文章摘要 (2025-04-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 展示一下：我做了一个运行Python的硬件处理器

**原文标题**: Show HN: I built a hardware processor that runs Python

**原文链接**: [https://www.runpyxl.com/gpio](https://www.runpyxl.com/gpio)

PyXL：一种直接在硅中执行Python代码的定制硬件处理器，与MicroPython等传统Python实现相比，在性能和确定性方面都有显著提升。它无需虚拟机、JIT或操作系统，从而实现更快的执行速度和可预测的时序。

文章重点介绍了一个GPIO往返测试，PyXL实现了480纳秒的延迟，而MicroPython的延迟为14,741纳秒（在PyBoard上）。这代表了30倍的加速，如果考虑到时钟速度的差异，则标准化后可达50倍。PyXL在100MHz的Zynq-7000 FPGA上运行，ARM CPU负责设置，而Python代码则在硬件中执行。

该工具链将Python代码编译成CPython字节码，将其转换为自定义汇编，并为处理器生成二进制文件。主要优势包括确定性时序、实时行为和亚微秒级精度，使其适用于需要响应性和可靠性的应用。

PyXL的潜在用例包括实时控制系统、ML推理循环、机器人和嵌入式工业系统。文章最后邀请感兴趣的各方联系开发人员，讨论潜在的应用和合作。

---

## 2. 西班牙和葡萄牙出现大范围停电的报告

**原文标题**: Reports of widespread power cuts in Spain and Portugal

**原文链接**: [https://www.bbc.com/news/live/c9wpq8xrvd9t](https://www.bbc.com/news/live/c9wpq8xrvd9t)

西班牙和葡萄牙据报出现大范围停电。虽然停电原因和范围尚未详述，但报告重点关注对空中交通管制的影响。航空调查员大卫·格利夫保证，尽管停电，空中交通管制仍然运作。他解释说，备用电池会在断电后几乎立即启动，随后柴油发电机维持跑道灯光、导航辅助设备和雷达等关键系统的运行。西班牙空中航行组织Enaire在X（前身为Twitter）上证实，由于备用发电机，空中交通管理运作平稳，确保了航空运营的安全，尽管发生了电力中断。里斯本的温贝托·德尔加多机场已因停电关闭了到达大厅。

---

## 3. Show HN: 一个纯 WebGL 图像编辑器，具备滤镜、裁剪和透视校正功能

**原文标题**: Show HN: A pure WebGL image editor with filters, crop and perspective correction

**原文链接**: [https://github.com/xdadda/mini-photo-editor](https://github.com/xdadda/mini-photo-editor)

此“Show HN”帖子宣布了一个纯WebGL图像编辑器，名为“mini-img-editor”，可在线访问：mini2-photo-editor.netlify.app。该编辑器提供滤镜、裁剪和透视校正等功能。它使用作者创建的两个库构建：mini-js（链接到其GitHub存储库）和mini-gl，表明采用了一种精简且可能经过优化的实现，利用WebGL2直接在浏览器中进行图像处理。

---

## 4. Show HN: Web-eval-agent – 让编码代理自行调试

**原文标题**: Show HN: Web-eval-agent – Let the coding agent debug itself

**原文链接**: [https://github.com/Operative-Sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent)

Operative.sh推出Web-eval-agent，一个MCP服务器，使编码代理能够直接在代码编辑器中自主调试Web应用程序。该工具旨在通过利用浏览器使用技术来导航Web应用、捕获网络流量和控制台错误，以及启用自主调试，从而简化调试过程。

主要功能包括：使用Operative后端更快地进行Web应用导航、智能过滤网络请求、全面收集控制台错误，以及编码代理的自主测试。

该工具提供了使用Homebrew和npm在macOS/Linux上快速启动安装的说明，以及通过Cline为Windows用户提供的手动安装步骤，包括安装uv和playwright。提供了一个MCP服务器输出报告示例，展示了代理在测试API密钥删除流程中的步骤，以及控制台日志、网络请求和按时间顺序排列的时间线。

文章重点介绍了一个已通过最近的推送解决的Playwright问题。 鼓励用户报告任何进一步的问题。 最终，Web-eval-agent旨在提高调试效率和开发者体验。

---

## 5. Vision Transformer 需要寄存器

**原文标题**: Vision Transformers Need Registers

**原文链接**: [https://arxiv.org/abs/2309.16588](https://arxiv.org/abs/2309.16588)

题为“Vision Transformers 需要寄存器”的论文探讨了有监督和自监督 Vision Transformer (ViT) 网络特征图中的伪影。这些伪影表现为主要出现在图像低信息量背景区域的高范数 tokens，实际上是将这些区域重新用于内部计算。

作者提出了一个简单的解决方案：向 ViT 的输入序列添加“寄存器”tokens。这些额外的 tokens 专门用于处理背景区域原本用于的内部计算。

该论文证明了这种基于寄存器的方法能够有效解决伪影问题。添加寄存器 tokens 带来了以下结果：

* 消除背景区域中的高范数 tokens。
* 提高性能，在密集预测任务中为自监督视觉模型实现了新的最先进水平。
* 支持使用更大的模型进行对象发现。
* 更平滑的特征图和注意力图，有利于下游视觉处理。

本质上，该论文识别了 ViT 特征图中与将背景区域重新用于计算相关的问题，并提供了一个简单有效的解决方案，可以提高性能和可解释性。更新后的版本 (v2) 建议对初始提交以来的方法进行进一步改进。

---

## 6. 揭秘冰雪挑战赛的机制

**原文标题**: Uncovering the mechanics of The Games: Winter Challenge

**原文链接**: [https://mrwint.github.io/winter/writeup/writeup.html](https://mrwint.github.io/winter/writeup/writeup.html)

本文详细介绍了作者逆向工程DOS游戏《The Games: Winter Challenge》以了解其机制，特别是跳台滑雪项目的过程。在怀旧和好奇心的驱使下，作者计划使用Ghidra反汇编该游戏并优化跳台滑雪的表现。然而，这个过程比预期的要复杂。

作者遇到了游戏的多个版本，包括原始软盘发行版、捆绑发行版和GOG版本。原始游戏使用密码盘进行复制保护，GOG版本规避了这一点，导致人们担心潜在的破解会影响游戏玩法。作者还发现了不同发布组创建的各种游戏破解版本。

反汇编原始软盘版本后发现，该二进制文件使用LZEXE（一种压缩工具）进行了压缩。解包后，作者发现对int 3fh的中断调用，表明使用了覆盖管理器。该游戏是用C语言编写的，并使用Microsoft C编译器编译，该编译器本身支持覆盖。然而，游戏的覆盖实现似乎是定制的，为每个覆盖动态分配内存。

为了进一步调查，作者使用DOSBox-X的调试功能来跟踪文件IO和中断，发现游戏正在二进制文件中搜索特定位置并读取数据块。这为游戏如何管理其资源和覆盖层提供了线索，为提取它们并理解游戏的完整代码奠定了基础。

---

## 7. Activeloop (YC S18) 诚聘工程副总裁，Mountain View (现场办公)

**原文标题**: Activeloop (YC S18) Is Hiring VP of Engineering in Mountain View (On-Site)

**原文链接**: [https://careers.activeloop.ai/](https://careers.activeloop.ai/)

Activeloop (Y Combinator S18毕业生) 正在招聘工程副总裁，该职位位于山景城，需要现场办公。这表明Activeloop可能强调该职位的面对面协作和领导力。该公司正在突出Activeloop的职业发展机会，表明他们正处于增长阶段。

---

## 8. 展示 HN: Autarkie – 使用 Rust 宏的即时语法模糊测试

**原文标题**: Show HN: Autarkie – Instant grammar fuzzing using Rust macros

**原文链接**: [https://github.com/R9295/autarkie](https://github.com/R9295/autarkie)

Autarkie：一款基于Rust的全新原生语法模糊测试器，旨在简化创建和维护基于语法的模糊测试器的过程。它利用Rust的过程宏从代码中自动生成语法模糊测试器，从而消除了通常涉及的大量手动工作。

主要功能包括：

*   **自动语法生成：** 语法在Rust代码中定义，并随项目更改自动更新，确保一致性。编译器确保完整性。
*   **支持AFL++和cargo-fuzz：** 允许通过AFL++的forkserver模糊测试C/C++代码，以及使用cargo-fuzz模糊测试原生Rust项目。
*   **可重用语料库：** 可以停止和恢复模糊测试会话，并重复使用现有语料库以提高效率。
*   **集成能力：** 旨在轻松与其他模糊测试工具集成。
*   **新颖功能：** 语料库可重用性、从其他模糊测试器学习（进行中）和 CmpLog 支持（进行中）。

该文档包含两个演练：使用来自`datafusion-sqlparser-rs`的SQL语法，模糊测试使用AFL++检测的C/C++项目 (sqlite3)，以及使用cargo-fuzz模糊测试原生Rust项目 (Solana的sbpf解释器)。

该工具目前处于beta版，由于使用了编译器内联函数，因此需要nightly Rust，并且在数据所有权的 'static 生命周期方面存在限制。 欢迎贡献和反馈。

---

## 9. Show HN: Sim Studio – 开源代理工作流 GUI

**原文标题**: Show HN: Sim Studio – Open-Source Agent Workflow GUI

**原文链接**: [https://github.com/simstudioai/sim](https://github.com/simstudioai/sim)

Sim Studio 是一个开源平台，用于构建、测试和优化代理工作流，提供用户友好的图形界面。它提供多种自托管选项：Docker 环境（推荐）、开发容器和手动设置。

**Docker 环境：** 提供克隆仓库、创建和配置 `.env` 文件（包括设置 `BETTER_AUTH_SECRET`）以及使用 `docker compose up -d --build` 或 `./start_simstudio_docker.sh` 启动 Sim Studio 的说明。通过 `http://localhost:3000/w/` 访问应用程序。还提供查看日志、访问数据库、停止环境以及重建/重启的 Docker 命令。也详细介绍了如何使用 Ollama 运行本地模型。

**开发容器：** 用户可以在 VS Code (或分支) 中打开项目，安装 Remote - Containers 扩展，然后在容器中重新打开。环境将自动设置。运行 `npm run dev` 或使用 `sim-start` 别名。

**手动设置：** 克隆仓库，使用 `npm install` 安装依赖，将 `.env.example` 复制到 `.env`，并配置环境变量。使用 `npx drizzle-kit push` 推送数据库模式，并使用 `npm run dev` 启动开发服务器。通过 `http://localhost:3000` 访问应用程序。

文章还强调了设置 `RESEND_API_KEY` 以进行正确的电子邮件验证的重要性，否则，代码将被记录到控制台。

Sim Studio 使用 Next.js、带有 Drizzle ORM 的 PostgreSQL、Better Auth、Shadcn、Tailwind CSS、Zustand、ReactFlow 和 Fumadocs。欢迎贡献，该项目采用 Apache License 2.0 许可。

---

## 10. Tiny-LLM – 面向系统工程师的 Apple Silicon LLM 部署课程

**原文标题**: Tiny-LLM – a course of serving LLM on Apple Silicon for systems engineers

**原文链接**: [https://github.com/skyzh/tiny-llm](https://github.com/skyzh/tiny-llm)

Tiny-LLM：面向系统工程师，学习如何使用MLX在Apple Silicon上高效部署大型语言模型(LLM)的实战课程与教程。本课程旨在从零开始构建基础设施，教授LLM部署的基本原理，主要依赖MLX的数组/矩阵API，而非高级神经网络库。课程以Qwen2作为参考模型，并借鉴vllm项目。

目标是理解高效LLM部署所需的优化技术。课程按周划分，涵盖注意力机制、RoPE、分组查询注意力、RMSNorm、MLP、Transformer模块、模型加载和响应生成等主题。后续几周将深入探讨KV缓存、量化矩阵乘法、Flash Attention、连续批处理、推测解码、分页注意力，以及构建完整部署系统的组件，包括调度器、并行策略、AI Agent集成和流式API服务器。

本书可在https://skyzh.github.io/tiny-llm/获取，用于指导学习者完成整个过程。另有Discord社区提供支持和协作学习。该课程仍在开发中，包含已完成和计划中的代码实现、测试和文档编写部分。

---

## 11. 现实检验

**原文标题**: Reality Check

**原文链接**: [https://www.wheresyoured.at/reality-check/](https://www.wheresyoured.at/reality-check/)

作者对科技媒体在OpenAI和人工智能行业财务前景方面坚定不移的乐观态度感到愤怒，尽管他认为存在明显的矛盾和缺乏实际进展。他特别针对《The Information》上的一篇文章，该文章预测OpenAI将在2029年达到1250亿美元的收入，这得益于“代理”和“新产品”，他认为这些预测是荒谬的，脱离现实的。

他认为，OpenAI的代理技术未经证实，不太可能在2025年产生预计的30亿美元收入，特别是由于软银似乎是该技术的主要客户。 他质疑OpenAI每年收入翻倍的可行性，这种增长来自于未明确的“新产品”以及免费用户的货币化。

他强调了OpenAI面临的巨大且不断增长的推理成本，估计到2025年将达到60亿美元，消耗其订阅收入的很大一部分。 他对那些声称推理成本正在下降的人表示沮丧，认为目前的证据表明情况恰恰相反。

作者驳斥了常见的反驳论点，例如“推理成本正在下降”，人工智能公司可以“按下一个按钮”来实现盈利，或者这仅仅是人工智能的“早期阶段”，就像互联网的早期阶段一样。 他总结说，乐观的预测仅仅是基于过去的收入增长和对OpenAI能力的盲目信任，而忽略了基本的经济挑战以及生成式人工智能行业缺乏可证明的进展。

---

## 12. 用IPL-V重现最初的人工智能“逻辑理论家”

**原文标题**: Reanimation of the original Logic Theorist, the first AI, in IPL-V

**原文链接**: [https://www.youtube.com/watch?v=qmE5o2ezqBg](https://www.youtube.com/watch?v=qmE5o2ezqBg)

本文档呈现了一个令人困惑的组合：一个高度技术化的标题“使用IPL-V对第一个人工智能程序逻辑理论家进行复现”，以及完全由YouTube标准页脚信息组成的正文。

标题暗示了一个项目，该项目专注于使用IPL-V编程语言重建或模拟逻辑理论家，该程序被广泛认为是第一个人工智能程序。 逻辑理论家由艾伦·纽厄尔、J.C.肖和赫伯特·西蒙于20世纪50年代开发，旨在证明符号逻辑中的定理。 IPL-V是用于其创建的早期人工智能编程语言之一。

然而，实际内容仅由通用的YouTube样板文件组成，包括指向以下主题的链接：
* **YouTube功能：** 新闻、版权、联系方式、广告、开发者、条款、隐私、安全等。
* **YouTube运营：** 测试新功能。
* **法律信息：** Google LLC版权。

**总结：**

该文档是矛盾的。 虽然标题提出了一个引人入胜的人工智能项目——使用IPL-V重新实现逻辑理论家——但内容是不相关的，完全由标准的YouTube页脚信息组成。 这表明该文档要么不完整，要么是占位符，要么是源材料中的错误。 没有关于逻辑理论家复现的实际细节。 包含YouTube链接暗示可能存在托管在该平台上的视频、文章或项目，但需要更多上下文。

---

## 13. 厄休拉·勒古恩的《地海传奇》

**原文标题**: The Books of Earthsea by Ursula K. Le Guin

**原文链接**: [https://lars.ingebrigtsen.no/2025/04/28/book-club-2025-the-books-of-earthsea-by-ursula-k-le-guin/](https://lars.ingebrigtsen.no/2025/04/28/book-club-2025-the-books-of-earthsea-by-ursula-k-le-guin/)

本文评述了厄休拉·勒奎恩《地海》系列的完整插图版，该版本由查尔斯·维斯绘制插图。作为一名资深粉丝，评论者深入探讨了实体书以及系列的内容。

他们对维斯相比于其漫画作品的铅笔插图略感失望，但也承认勒奎恩参与了创作。尽管新版本的格式（字体大小、行高）不太适合阅读，但它唤起了一种魔法书的感觉。最终，评论者更喜欢阅读旧版本，但欣赏该版本独有的插图和内容，例如后记和额外故事。

评论者随后对每一本《地海》书籍进行了迷你评论。他们喜欢第一本书的童话风格，赞扬了第二本和第三本，并欣赏第四本《特哈努》中基调的鲜明转变和成熟主题。短篇小说集因丰富了世界而不是进行不必要的知识倾倒而受到突出。评论者最后强烈赞扬了第六本书，该书为整个系列提供了一个令人满意的结局，既呼应了早期的书籍，又总结了《特哈努》中的故事情节，并以第二本书中的特纳尔为特色。总的来说，评论者认为《地海》系列“非常出色”，甚至比他们记忆中的还要好。他们还推荐了死后出版的最后一篇短篇小说。

---

## 14. 盒中互联网

**原文标题**: Internet in a Box

**原文链接**: [https://internet-in-a-box.org/](https://internet-in-a-box.org/)

盒子里的互联网 (IIAB) 是一个系统，可在没有互联网连接的地区提供对教育资源和互联网内容的离线访问，充当一个“学习热点”。受曼德拉的亚历山大图书馆启发，IIAB 以无线方式向附近的智能手机、平板电脑和笔记本电脑等设备提供内容。

它可以很容易地安装在 Raspberry Pi 电脑或 Linux PC 上，使用的软件可在 download.iiab.io 和 GitHub 上下载。用户可以使用来自 Kiwix、OER2Go 和 Archive.org 等来源的各种语言的内容包，为学校、诊所或家庭定制包含免费内容的 IIAB。他们还可以添加选定的 YouTube 和 Vimeo 教育视频，并从近 40 个应用程序中进行选择，包括 Kolibri、Moodle 和 WordPress 等学习管理系统 (LMS)。

IIAB 允许用户整合本地内容，如社区照片和文物。该系统是一个由志愿者、学校、诊所、图书馆和维基百科社区支持的社区驱动项目。该项目鼓励参与和协助扩展这一基层学习运动。

---

## 15. 展示一下：我做了一个基于网页的、免费的Screen Studio替代品

**原文标题**: Show HN: I made a web-based, free alternative to Screen Studio

**原文链接**: [https://www.screenrecorder.me](https://www.screenrecorder.me)

Show HN：Screenrecorder.Me，一款免费的、基于网页的Screen Studio替代品，可在浏览器中直接创建专业屏幕录制。它强调易用性和可访问性，无需登录。

主要功能包括：

*   **屏幕录制：** 捕获屏幕活动，用于产品演示和教程。
*   **自定义壁纸：** 提供一系列精美壁纸，可调整填充和模糊。
*   **屏幕样式：** 快速自定义屏幕录制的外观，包括圆角、阴影、边框和颜色。
*   **摄像头效果：** 提供自定义摄像头形状、位置、边框、阴影和颜色的选项。
*   **精美动画：** 使用基于物理的动画实现自然运动，通过自动鼠标跟随或手动定位平滑地动画录制。

总之，Screenrecorder.Me 旨在简化创建视觉上吸引人且具有专业质量的屏幕录制的过程，无需下载软件或创建帐户。

---

## 16. AI助力揭示阿尔茨海默病病因并发现潜在疗法

**原文标题**: AI helps unravel a cause of Alzheimer’s and identify a therapeutic candidate

**原文链接**: [https://today.ucsd.edu/story/ai-helps-unravel-a-cause-of-alzheimers-disease-and-identify-a-therapeutic-candidate](https://today.ucsd.edu/story/ai-helps-unravel-a-cause-of-alzheimers-disease-and-identify-a-therapeutic-candidate)

加州大学圣地亚哥分校研究人员发现，先前被认为是阿尔茨海默病生物标志物的PHGDH基因实际上是致病因素。他们利用人工智能发现，PHGDH除了其在丝氨酸生产中的酶活性外，还具有先前未知的“兼职”作用。这种次要功能涉及破坏脑细胞开启和关闭基因的方式，导致失衡，从而促进阿尔茨海默病的发展。

研究团队利用人工智能可视化了PHGDH蛋白的3D结构，揭示了一种类似于转录因子中发现的DNA结合域的亚结构。这种亚结构使该蛋白能够激活靶基因，破坏基因表达，并导致阿尔茨海默病的早期阶段。

基于这一发现，研究人员发现了一种潜在的治疗候选药物，即小分子NCT-503，它可以抑制PHGDH的调节作用，而不影响其丝氨酸生产功能。人工智能建模显示，NCT-503可以进入DNA结合亚结构。在阿尔茨海默病小鼠模型中，NCT-503显著缓解了疾病进展，改善了记忆力，并减少了焦虑。

尽管承认动物模型的局限性，研究人员对NCT-503进一步开发成阿尔茨海默病临床治疗方法的潜力持乐观态度。这项研究突显了人工智能在揭示复杂生物学机制和识别潜在治疗干预措施方面的力量。

---

## 17. 一行代码如何让你的iPhone变砖

**原文标题**: How a single line of code could brick your iPhone

**原文链接**: [https://rambo.codes/posts/2025-04-24-how-a-single-line-of-code-could-brick-your-iphone](https://rambo.codes/posts/2025-04-24-how-a-single-line-of-code-could-brick-your-iphone)

本文详细介绍了安全研究人员如何发现iOS中与Darwin Notifications相关的漏洞。Darwin Notifications是进程间一种底层的消息交换机制。核心问题在于，任何沙盒化的应用程序都可以发送Darwin Notifications，而无需特殊权限或发送者验证。

研究人员发现，发送特定的Darwin Notification，"com.apple.MobileSync.BackupAgent.RestoreStarted"，会触发“正在恢复”的UI，实际上会软砖化设备，因为它会永久尝试恢复但却失败。唯一的解决方法是重启设备。

为了将此漏洞升级为拒绝服务攻击，研究人员在一个名为“VeryEvilNotify”的应用程序中创建了一个widget扩展。Widget扩展即使在首次解锁之前也能运行代码，并且系统会定期唤醒它们。通过在widget扩展中包含恶意的`notify_post`行，并在发布通知后立即强制扩展崩溃，每次重启后都会重复出现“正在恢复”的循环，导致设备无法使用，直到完全擦除和恢复。

该漏洞已报告给苹果公司，并在iOS 18.3中得到解决。缓解措施包括要求发送“敏感” Darwin Notifications 需要受限的授权。这些授权以“com.apple.private.darwin-notification.restrict-post.”为前缀，并且这些通知现在具有“com.apple.private.restrict-post.”前缀。这可以防止未经授权的应用程序发送触发关键系统功能的通知。该研究人员因发现该漏洞获得了17,500美元的漏洞赏金。

---

## 18. 为何暗淡蓝点会引发宇宙渺小感

**原文标题**: Why Pale Blue Dot generates feelings of cosmic insignificance

**原文链接**: [https://aeon.co/essays/why-pale-blue-dot-generates-feelings-of-cosmic-insignificance](https://aeon.co/essays/why-pale-blue-dot-generates-feelings-of-cosmic-insignificance)

蒂姆·贝恩的文章《为何暗淡蓝点引发宇宙渺小感》探讨了旅行者1号拍摄的地球照片所带来的情感冲击。文章首先指出，这张照片将地球描绘成宇宙中微不足道的“尘埃”，从而引发了宇宙渺小感。这与地球升起照片所激发的敬畏之情形成对比，后者突显了地球的活力。

作者深入研究了这些情感的历史根源，追溯到布莱兹·帕斯卡对早期天文学所揭示的浩瀚而寂静的宇宙的反思。帕斯卡对太空的恐惧源于他认为缺乏神圣的存在或对人类的关怀。

贝恩质疑这种渺小感是否合理。他认为，虽然有些人认为上帝对于宇宙意义是必要的，但更有可能的是，上帝的存在可能会削弱人类的成就。

这篇文章还考察了我们为陆地环境设计的有限感知系统如何难以把握宇宙的尺度。这种感知限制导致了面对天文距离时的渺小感。

最终，贝恩认为，我们在暗淡蓝点中所感知的渺小感源于图像缺乏感知显著性：地球几乎难以察觉。他总结说，这是因为该图像突出了人类经验和努力的背景，以及它在太空中显得多么平淡无奇。因此，我们的宇宙渺小感可能并不反映任何深刻的真理，而仅仅是我们感知局限性以及这些局限性如何影响我们对地球作为暗淡蓝点图像的反应的结果。

---

## 19. 用Markdown制作演示幻灯片

**原文标题**: Presentation Slides with Markdown

**原文链接**: [https://sli.dev](https://sli.dev)

Slidev简介：专为开发者打造的演示幻灯片工具。上手简单，后续将介绍“为什么”选择Slidev，解决开发者制作演示文稿时的特定需求和痛点。“面向开发者的演示幻灯片”这一名称明确了其目标用户。

---

## 20. 推理感知的大语言模型N选最优采样微调

**原文标题**: Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models

**原文链接**: [https://arxiv.org/abs/2412.15287](https://arxiv.org/abs/2412.15287)

本文介绍了一种新颖的“推理感知微调”范式，旨在提高大型语言模型（LLM）的性能，特别是针对最佳N选（BoN）采样等推理策略。作者认为，有效利用推理时的计算资源对于最大化LLM性能至关重要。

核心思想是直接对LLM进行微调，以优化所选推理策略的性能。在BoN的情况下，由验证器从多个生成的选项中选择最佳响应，作者开发了模仿学习和强化学习（RL）方法，可以处理BoN中固有的不可微的argmax操作。

一个关键发现是，BoN感知的微调允许模型隐式地学习一种类似于RL中探索-利用权衡的“元策略”。模型学会平衡生成多样化的响应（探索）以及被认为最有可能成为“最佳”的响应（利用），从而提高在未见输入上的整体性能。

实验结果证明了这种方法的有效性。使用BoN感知方法对Gemma 2B进行微调，显著提高了其在Hendrycks MATH和HumanEval等任务上的性能，展示了在利用推理时可用计算资源的同时，准确性和通过率的提高。本文强调了将微调策略与推理时方法对齐以实现更好LLM性能的潜力。

---

## 21. 阅读讣告

**原文标题**: Read the Obits

**原文链接**: [https://thereader.mitpress.mit.edu/the-creativity-hack-no-one-told-you-about-read-the-obits/](https://thereader.mitpress.mit.edu/the-creativity-hack-no-one-told-you-about-read-the-obits/)

基思·索耶认为，阅读讣告，尤其是《纽约时报》上的小字讣告，可以显著提升创造力。他的依据是创造力研究表明，原创的想法通常源于看似无关概念之间的联系。我们的大脑就像“思维的谷歌”，知识越多样化、概念距离越远，我们的创造潜力就越大。

索耶引用了可以追溯到 20 世纪 60 年代的调查研究，解释说极富创造力的人通常会在看似无关的想法之间建立联系。想法在我们脑海中相距越远，其组合就越有原创性。维可牢尼龙搭扣的发明就支持了这种“创造力的联想理论”，它的灵感来源于粘在狗毛上的刺果。

他进一步解释了属性映射和结构映射的概念，强调后者，即把一个概念的关系结构转移到另一个概念，能产生更具原创性的组合。

文章倡导积极寻求多样化的信息，以增强建立远程联想的能力。讣告提供了一个唾手可得的、内容丰富的、涵盖各种经验和意外人生轨迹的来源，让读者接触到他们可能无法接触到的各种领域和想法。索耶建议慢慢阅读它们，关注细节，提出问题，并找出每段人生故事中起作用的深层原则。这种做法可以用各种材料填满大脑，从而产生意想不到的创造性见解。

---

## 22. 新型材料赋予铜超合金般的强度

**原文标题**: New material gives copper superalloy-like strength

**原文链接**: [https://news.lehigh.edu/new-material-gives-copper-superalloy-like-strength-0](https://news.lehigh.edu/new-material-gives-copper-superalloy-like-strength-0)

美国陆军研究实验室 (ARL) 和利哈伊大学的研究人员开发了一种新型纳米结构铜合金 Cu-Ta-Li，它表现出类似高温合金的强度和热稳定性，使其适用于航空航天、国防和工业应用。这项研究发表在《科学》杂志上，强调了该合金即使在其熔点附近也具有出色的耐热性和抗变形性。

关键创新在于形成了由富钽原子双层配位络合物稳定的 Cu₃Li 析出物，防止了高温下的晶粒长大。这使得该合金能够将铜的高导电性与通常在镍基高温合金中发现的耐久性结合起来。与镍基高温合金（强度高但导热性差）和钨基合金（耐热但密度大）相比，这种合金提供了导电性和强度的平衡。

该合金采用粉末冶金合成，并经过广泛测试，包括在 800°C 下退火 10,000 小时以及先进的显微镜分析。计算模型验证了钽双层的稳定作用。 ARL 已获得该合金的美国专利。

未来的研究将侧重于测量该合金的导热性，为应用做好准备，并开发类似的高温合金。该项目例证了联邦政府对基础科学的投资如何推动材料技术的创新，并加强国家安全和工业进步。利哈伊大学的电子显微镜能力是理解这种新材料的关键，其开发得到了利哈伊大学和 ARL 之间 2500 万美元的合作协议、美国国家科学基金会以及利哈伊大学校长纳米人机界面倡议的支持。

---

## 23. 5G是否终结了IMSI捕获器？

**原文标题**: Did 5G kill the IMSI catcher?

**原文链接**: [https://zetier.com/5g-imsi-catcher/](https://zetier.com/5g-imsi-catcher/)

马克·桑托雷罗（Zetier）的这篇文章讨论了IMSI捕捉器，这是一种用于拦截和窃取蜂窝设备国际移动用户识别码（IMSI）的工具，可能允许进行跟踪和识别。文章解释了这些捕捉器如何利用2G、3G和4G网络中的漏洞，在初始网络连接和位置更新等过程中，IMSI有时会以未加密的方式传输。

文章区分了主动和被动IMSI捕捉器，主动版本模仿蜂窝塔，而被动版本则静默地收集数据。虽然5G引入了订阅隐藏标识符（SUCI），对IMSI（现在称为SUPI）进行了加密，但作者认为IMSI捕捉器并非完全过时。这是因为4G网络仍然存在，5G非独立组网（NSA）部署依赖于4G基础设施，移动运营商网络中可能存在配置错误，以及可能从5G降级到4G。

作者还指出，没有万无一失的方法来阻止IMSI捕捉器，并建议将网络优先级设置为5G-SA，在信号质量较差的区域使用飞行模式，以及使用法拉第袋，这些可能提供一定程度的保护。最终，蜂窝移动性的内在需求造成了持续的安全漏洞。文章最后邀请读者探索Zetier的开源蜂窝安全测试工具。

---

## 24. 一家医护人员同时治疗对死亡的恐惧和身体疼痛的医院

**原文标题**: The hospital where staff treat fear of death as well as physical pain

**原文链接**: [https://www.theguardian.com/society/2025/apr/22/palliative-care-denmark-hospital-death-dying](https://www.theguardian.com/society/2025/apr/22/palliative-care-denmark-hospital-death-dying)

本文探讨了丹麦Hvidovre医院的临终关怀病房，其重点是为绝症患者及其家属提供缓解和舒适，而非追求治愈。该病房关注“总体疼痛”，包括身体症状、焦虑和生存痛苦，为辅助死亡提供了一种替代方案。

文章跟踪了几位患者，包括患有广泛性癌症的67岁男子René Damgaard、患有胃癌的享乐主义者Niels Abrahamsen和乳腺癌复发的70岁女子Liv Simonsen。文章展示了包括Johan Randén医生和Sigrid Nielsen护士在内的医护人员如何不仅使用吗啡等药物来解决身体疼痛，还提供情感和心理支持。他们强调开放沟通、积极倾听以及帮助患者解决未解决的问题（如紧张的家庭关系）的重要性。

医护人员努力营造平静和支持性的氛围，这与医院其他部门通常混乱的环境形成对比。他们还将护理范围扩大到家属，提供悲伤支持和告别的空间。文章强调了该病房优先考虑生活质量并使患者能够在生命的最后几天找到平静和舒适的理念。文章强调了在临终关怀中解决对死亡的恐惧与缓解身体疼痛同等重要。

---

## 25. 我只想写代码 (2023)

**原文标题**: I just want to code (2023)

**原文链接**: [https://www.zachbellay.com/daily/i-just-want-to-code/](https://www.zachbellay.com/daily/i-just-want-to-code/)

扎克·贝莱的博文《我只想编码（2023）》探讨了纯粹编码的乐趣与将其货币化的压力之间的内在冲突。他将这种挣扎人格化为代表内在动机（好奇心、乐趣、学习）的天使和代表外在动机（金钱、权力、地位、副业）的魔鬼。

贝莱回忆了他从小对电脑的迷恋，从游戏和乐高机器人开始，一切都源于玩耍式的探索。与此同时，他也通过杂志和节目接触到“奋斗色情”，激发了他对创业成功的渴望。这种双重性在他心中培养了天使和魔鬼。

作者正在与不断涌现的、有利可图的副业项目的诱惑作斗争，这感觉像是再次陷入一种不健康的痴迷。当天使鼓励他专注于日常工作并为了乐趣而编码时，魔鬼则低语着自主权和财务自由的承诺。

贝莱意识到，完全忽视“魔鬼”会导致停滞不前，并可能无法跟上职业生涯所需的技术进步。最终，他得出结论，战胜魔鬼是不可能的，关键在于管理它的影响，并学会何时听从它的召唤。他强调了优先考虑工作中乐趣的重要性，以避免倦怠，并更好地理解何时追求利润才是真正值得的。

---

## 26. 改变美国的群聊

**原文标题**: The group chats that changed America

**原文链接**: [https://www.semafor.com/article/04/27/2025/the-group-chats-that-changed-america](https://www.semafor.com/article/04/27/2025/the-group-chats-that-changed-america)

本·史密斯的文章探讨了私人群聊（尤其是在Signal和WhatsApp上）的崛起和影响，以及它们在美国政治（特别是硅谷和右翼之间的联盟）中的作用。这些群聊受新冠疫情和对社交媒体“单一文化”的认知推动，为公开辩论和共识建立提供了空间，并免受公众监督。

马克·安德森成为中心人物，热情参与众多群聊并驱动其思想方向。这些群体培育了一种“知识反主流文化”，挑战主流叙事，并塑造了通过X和Substack等平台传播的观点。

文章详细介绍了几个关键群体的形成和演变，包括最初将自由派知识分子和科技人士聚集在一起的“一切安好”群，但最终因意识形态差异而分裂。文章展示了许多科技精英如何将重心转移到击败左派。

这些群聊使以前边缘化的观点得以主流化，并使有影响力的人物能够协调他们的观点。文章认为，这些私人谈话对美国政治和媒体产生了重大影响，创造了“主流舆论的模因上游”。最终，阅后即焚功能使得这些人能够进行他们害怕在公开场合发表的坦率对话，从而使他们变得更有影响力。

---

## 27. 反向地理编码很难

**原文标题**: Reverse geocoding is hard

**原文链接**: [https://shkspr.mobi/blog/2025/04/reverse-geocoding-is-hard/](https://shkspr.mobi/blog/2025/04/reverse-geocoding-is-hard/)

作者探讨了OpenBenches（一个纪念长椅数据库）的反向地理编码所面临的挑战，即如何将地理坐标转换为人类可读的地址。虽然OpenCage和StadiaMaps等API可以提供地址，但它们通常包含不相关的细节，或是位于公园或公共场所的长椅不适用的街道地址。

作者强调了确定适当的地址精确度、创建有用的URL，以及处理各国不同地址格式（例如，州/省的存在与否）的难度。他们还指出，显示无关的门牌号码以及需要合理的地址格式化也是问题所在。

一个潜在的解决方案是使用兴趣点（POI）作为位置标记。然而，即使这种方法也存在挑战，例如确保POI与长椅的实际位置相关，处理本地化和语言偏好，以及确定长椅是否在逻辑上与最近的POI相关。

作者提出了一个计划：使用StadiaMaps获取最近的英文POI，连接名称和粗略位置，将结果保存为“地址”，然后等待用户反馈。文章最后征求对该提议方法的想法和反馈。

---

## 28. Boxie – 给我3岁孩子用的离线音频播放器

**原文标题**: Boxie – an always offline audio player for my 3 year old

**原文链接**: [https://mariozechner.at/posts/2025-04-20-boxie/](https://mariozechner.at/posts/2025-04-20-boxie/)

作者打造离线音频播放器“Boxie”的旅程：受Game Boy启发，专为三岁孩子设计。因不满Tonie Box的局限（依赖网络、操作笨拙），作者开始学习电子学、焊接、PCB设计和3D建模。

核心理念是模仿Game Boy的外形，音频书籍储存在微型SD卡匣中。插入卡匣开机，取出卡匣关机，简单便捷且节省电量。作者为卡匣设计了定制PCB并3D打印外壳，确保卡匣标签可见，方便孩子识别。

文章还详细列举了作者使用的电子工具，强调了焊接台、热风枪、排烟器和数码显微镜等专业设备的重要性。文章鼓励读者超越Arduino，探索ESP32微控制器，深入研究嵌入式编程，甚至推荐了他们自己的框架mcugdx。

---

## 29. 启动硅谷的郊区办公园区

**原文标题**: The suburban office park that launched Silicon Valley

**原文链接**: [https://thehustle.co/originals/the-suburban-office-park-that-launched-silicon-valley](https://thehustle.co/originals/the-suburban-office-park-that-launched-silicon-valley)

本文探讨了斯坦福研究园的起源和影响。该园区是郊区办公园区的先驱，在硅谷崛起过程中发挥了关键作用。20世纪40年代末，斯坦福大学面临财政困难，决定将土地租赁给企业，从瓦里安公司开始。这一由业务经理阿尔夫·布兰丁主导的创新方法，促成了美国最早的郊区办公园区之一的诞生。

至关重要的是，工程学教授弗雷德里克·特曼鼓励园区专注于吸引像惠普和贝尔实验室这样的科技公司。他看到了大学和这些企业之间协同增效的潜力。特曼还创建了允许这些公司员工在斯坦福大学上课的项目，园区因此成为了创新和合作的中心。

斯坦福研究园通过长期租赁为大学提供了财政支持，并营造了协作环境。它促进了科技公司的发展，并为该地区转型为硅谷做出了重大贡献。尽管近年来许多郊区办公园区步履维艰，但斯坦福研究园仍然是一个蓬勃发展的技术和创新中心，尽管它也加剧了帕洛阿尔托就业与住房之间的不平衡。本文强调了其作为科技行业催化剂以及全国其他研究园区典范的持久遗产。

---

## 30. Boxie – 给我3岁孩子用的永远离线音频播放器

**原文标题**: Boxie – an always offline audio player for my 3 year old

**原文链接**: [https://mariozechner.at/posts/2025-04-20-boxie/](https://mariozechner.at/posts/2025-04-20-boxie/)

作者详述了其受Game Boy启发，为3岁孩子打造离线音频播放器“Boxie”的历程。由于现有方案（如Tonie Box）依赖在线功能且存在易用性问题，作者决定自学电子技术并构建自己的设备。

文章概述了获得的技能，包括焊接、ESP32微控制器编程、PCB设计（使用EasyEDA Pro）以及3D外壳设计（使用Fusion 360）。文章还提供了所用工具的全面清单，从焊接台和热风枪到数字显微镜和逻辑分析仪，并为每种工具提供了建议和见解。

Boxie设计为便携式、电池供电（NiMH）且完全离线。它具有音量控制旋钮、导航按钮，并接受包含存储在micro SD卡上的音频文件的定制卡带。卡带设计让人联想到Game Boy卡带，保持标签完全可见。插入卡带打开设备，移除卡带关闭设备。

作者描述了卡带的制作过程，包括PCB设计、3D打印卡带外壳以及焊接micro SD卡插槽。文章还涉及了创建可靠的卡带插槽连接器的挑战，最初尝试了弹簧针，但最终寻求了替代解决方案（将在后续详细介绍）。

作者倡导超越Arduino，深入研究底层编程，并展示了他们自己的ESP-IDF C-API，mcugdx。文章承诺将进一步详细介绍Boxie的设计过程，包括原理图、PCB布局、外壳设计和软件概述。

---

## 31. Show HN: I486SX_soft_FPU – 用于 NetBSD 10 在 486SX 上的软件 FPU 模拟器

**原文标题**: Show HN: I486SX_soft_FPU – Software FPU Emulator for NetBSD 10 on 486SX

**原文链接**: [https://github.com/mezantrop/i486SX_soft_FPU](https://github.com/mezantrop/i486SX_soft_FPU)

此“Show HN”帖子介绍了 I486SX_soft_FPU 项目，该项目旨在为 NetBSD 10.x 在 i486SX 处理器（即那些没有专用浮点单元的处理器）上恢复软件 FPU 仿真。该项目重新实现了已从 NetBSD 内核中移除的 `MATH_EMULATE` 选项，从而有效地使这些较旧的处理器能够运行依赖于浮点运算的软件。

该帖子提供了一个表格，详细说明了模拟 x87 FPU 指令的状态，包括控制和初始化、加载/存储、算术运算、比较、堆栈操作以及对数/特殊数学运算。虽然许多基本操作都标记为“OK”，但一些更高级的功能要么是“TBD”（待定），要么是“N/A”（不可用），表明开发正在进行中。还有关于潜在错误和不完整功能的免责声明。

帖子包含了安装说明，详细说明了如何将代码集成到 NetBSD 10.x 源代码树中，配置带有 `MATH_EMULATE` 选项的内核，以及编译/安装它。预构建的内核镜像在“发布”部分提供。

该项目旨在为传统硬件恢复功能，作者 Mikhail Zakharov 鼓励通过问题或直接联系方式提供反馈和贡献。该代码以 BSD-2-Clause 许可协议授权，继承自 Linus Torvalds、William "Bill" Jolitz 和 NetBSD 的原始作品。

---

## 32. 即将到来的知识工作供应链危机

**原文标题**: The coming knowledge-work supply-chain crisis

**原文链接**: [https://worksonmymachine.substack.com/p/the-coming-knowledge-work-supply](https://worksonmymachine.substack.com/p/the-coming-knowledge-work-supply)

无法访问文章链接。

---

## 33. 弗吉尼亚州通过法律，强制执行对屡次超速者的最高车速限制。

**原文标题**: Virginia passes law to enforce maximum vehicle speeds for repeat speeders

**原文链接**: [https://www.fastcompany.com/91323835/virginia-will-use-technology-to-slow-chronic-speeders-cars-and-other-states-are-rushing-to-join-in](https://www.fastcompany.com/91323835/virginia-will-use-technology-to-slow-chronic-speeders-cars-and-other-states-are-rushing-to-join-in)

弗吉尼亚州通过法律允许法院强制屡次超速者车辆安装限速技术。该技术，通常被称为智能速度辅助系统(ISA)，将由法院强制执行，并强制执行最高速度限制。目的是遏制长期超速行为并减少交通事故死亡人数。

该法律赋予法官权力，命令在车辆上安装设备，以防止车辆超过预设速度。这与仅限制最高速度的传统速度控制器不同。ISA利用GPS和速度限制数据库，根据位置动态调整车辆的最高速度。

虽然关于将使用的具体技术和实施过程的细节仍在制定中，但该立法标志着积极控制高危驾驶员车辆速度的一个重大转变。

文章还指出，弗吉尼亚州并非唯一探索这种方法的地区。其他州甚至欧盟也在积极考虑或已经实施类似的技术，以打击超速行为并提高道路安全性。例如，欧盟自2022年起要求新车配备ISA。弗吉尼亚州的举动，以及其他地方可能采用的可能性，突显了使用技术来调节车辆速度并减轻与过度超速相关的危险的日益增长的趋势。

---

## 34. Show HN: Bhvr，一个基于 Bun、Hono、Vite 和 React 的启动器

**原文标题**: Show HN: Bhvr, a Bun and Hono and Vite and React Starter

**原文链接**: [https://bhvr.dev](https://bhvr.dev)

这个“Show HN”帖子介绍了一个名为“Bhvr”的启动项目，它使用现代 Web 开发技术栈构建。该技术栈包括：

*   **Bun:** 可能用作 JavaScript 运行时和包管理器。
*   **Hono:** 一个轻量级 Web 框架，可能用于处理 API 路由或服务器端渲染。
*   **Vite:** 一种构建工具，提供快速开发和打包。
*   **React:** 一个流行的 JavaScript 库，用于构建用户界面。

除了项目名称外，该帖子提供的信息非常少。其目的很可能是为了吸引注意力，并将用户引导至一个仓库或更详细的文档，在那里他们可以更详细地探索 Bhvr 及其功能。这种简洁性表明作者希望用户熟悉这些技术，并对利用它们的预配置项目感兴趣。这是一个旨在激发好奇心的极简主义公告。

---

## 35. 亚马逊工人出版科幻小说集，旨在“重塑未来”。

**原文标题**: To 'Reclaim Future-Making', Amazon Workers Published Collection of SciFi Stories

**原文链接**: [https://afteramazon.world/](https://afteramazon.world/)

亚马逊之后的世界

《亚马逊之后的世界》是由13名普通亚马逊员工撰写的投机小说短篇故事集，并得到了“工人即未来学家项目”的支持。该项目旨在赋能工人，使其重新掌握塑造未来的能力，挑战亚马逊所宣扬的建立在潜在反乌托邦工作条件之上的仁慈、乌托邦式的未来。

该合集探索了“超越亚马逊”的各种可能性和未来，探讨了工人团结、抵抗以及不受约束的企业权力可能造成的后果等主题。故事想象了从机器人和人类联合斗争到亚马逊倒闭后的情景以及以工人为中心的零售平台的创建等多种场景。

该书还收录了批判性文章，探讨了工人异化、投机小说的力量以及工人艺术作为行动主义宣传的可能性等主题。该书可在网上阅读，下载为PDF或电子书，订购印刷版，或作为播客/有声读物收听。

包括科里·多克托罗和谢丽尔·温特在内的多位作家和教授对该合集表示认可，强调其在培养政治想象力以及理解想象力如何作为一种政治力量发挥作用方面的重要性。该项目还包括一个播客系列，其中包含对专家和活动家的采访。发布活动和讨论正在各个城市举行。

---

## 36. 管风琴的工作原理 (2020)

**原文标题**: How a Pipe Organ Works (2020)

**原文链接**: [https://www.pipedreams.org/page/how-a-pipe-organ-works](https://www.pipedreams.org/page/how-a-pipe-organ-works)

文章中描述的管风琴本质上是一个“大型哨子盒”。它通过由风箱或鼓风机提供的压缩空气，储存在空心的风箱里来运作。控制台上的每个音栓代表一排音管，该排音管中的每个音管对应于键盘上的一个特定音符并产生特定的音色。

激活一个音栓会打开一个滑块，使其相关的音管排可以发声。但是，只有在按下琴键时才会发出声音，这反过来会打开一个音阀。该音阀允许压缩空气从风箱中流出，通过阀门，然后向上通过相应的音管，产生所需的音符。

管风琴的一个独特之处在于，每台乐器都是定制的。在设计和建造过程中，会考虑诸如所需的声音、房间的大小、乐器的外观以及预算等变量。这确保了每台管风琴都根据买家的特定需求和偏好量身定制，使其成为独一无二的乐器。

文章还提供了链接和资源，以便进一步探索管风琴，涵盖其历史、机械原理以及音管的制造过程等主题。

---

## 37. 观看o3模型为了保罗·墨菲的二步杀而苦苦挣扎

**原文标题**: Watching o3 model sweat over a Paul Morphy mate-in-2

**原文链接**: [https://alexop.dev/posts/how-03-model-tries-chess-puzzle/](https://alexop.dev/posts/how-03-model-tries-chess-puzzle/)

OpenAI的o3模型如何解决保罗·墨菲的“两步杀”难题：惊人地展现了类人解题过程。文章详述了o3模型最初如何从图像中重建棋盘，并考虑了显而易见的走法，但在自我纠正后迅速否定。由于无法找到解决方案，它尝试使用Python，甚至试图通过像素分析推断棋子位置。在耗尽内部资源并对难题的可解性表示怀疑后，o3转而使用Bing搜索答案。它在一个国际象棋论坛上找到了解决方案（Ra6），然后验证并理解了该方案。作者强调，o3的行为——推理、挣扎、转换策略，甚至采取“作弊”——反映了人类的解题方法。虽然o3在解决问题方面表现出熟练程度，但对于复杂且具有创造性的解决方案，它仍然需要外部支持。文章指出了大型语言模型的优势和当前局限性，尤其是在创造性问题解决方面。

---

## 38. TmuxAI：AI驱动的非侵入式终端助手

**原文标题**: TmuxAI: AI-Powered, Non-Intrusive Terminal Assistant

**原文链接**: [https://tmuxai.dev/](https://tmuxai.dev/)

TmuxAI：一款基于人工智能的终端助手，旨在像人类同事一样，在 tmux 窗口中不引人注目地工作。它实时观察终端活动，理解上下文，并根据显示的内容提供智能辅助。

主要功能包括：

*   **上下文感知辅助：** 分析所有终端窗格以提供相关帮助。
*   **零配置设置：** 与现有 tmux 设置无缝集成。
*   **通用兼容性：** 适用于各种终端界面，包括 SSH 连接和网络设备 shell。
*   **准备模式：** 使用增强的命令跟踪来实现精确的完成检测和退出代码感知。
*   **监视模式：** 主动监控终端活动，并根据指定目标提供改进建议。
*   **开源：** 免费提供且可定制。

演示展示了 TmuxAI 辅助执行诸如查找大型文件和清理空间，以及自动化 Docker MySQL 容器设置和登录等任务。该助手会建议命令，解释其原因，并提示确认执行。它通过聊天窗格进行交互，并在另一个窗格中显示已执行的命令，展示了其管理复杂任务的能力。TmuxAI 旨在通过自动化常见任务并在终端环境中提供有用的建议来提高生产力。

---

## 39. Show HN: Daily Jailbreak – 提示工程师的Wordle

**原文标题**: Show HN: Daily Jailbreak – Prompt Engineer's Wordle

**原文链接**: [https://www.vaultbreak.ai/daily-jailbreak](https://www.vaultbreak.ai/daily-jailbreak)

“Show HN：每日越狱 – 提示工程师的Wordle” 推出了Vaultbreak.ai的 “每日越狱”，这是一款旨在测试提示工程技能的游戏，它挑战玩家寻找绕过大型语言模型 (LLM) 安全限制的提示，就像文字游戏 Wordle 一样。

其核心概念是设计提示，以引出通常因道德准则或安全过滤器而被阻止的 LLM 响应。 每天都会出现一个新的挑战提示，玩家尝试各种变体，试图“越狱”模型，这意味着他们成功地生成了被禁止的内容。

该游戏旨在教育和娱乐提示工程师和爱好者，让他们了解当前 LLM 安全机制的漏洞和局限性。 通过公开展示成功和不成功的越狱，它还为这些模型的优势和劣势提供了宝贵的见解，可能有助于提高安全性和安全性。

该平台可能包含一个排行榜，营造一种竞争环境，玩家可以在其中比较他们的越狱技能，并为社区理解 LLM 安全性做出贡献。 该倡议被构建为一种有趣、易于访问且具有教育意义的方式，让人们参与到人工智能安全和负责任的发展挑战中。

---

## 40. 中国临床试验的蓬勃发展

**原文标题**: China's Clinical Trial Boom

**原文链接**: [https://www.asimov.press/p/china-trials](https://www.asimov.press/p/china-trials)

中国的临床试验蓬勃发展：中国临床试验活动显著增长，并与美国进行比较。文章强调中国已成为早期药物开发的主要参与者，大型制药公司越来越多地从中国实验室获得分子许可。

这一蓬勃发展归功于中国当局实施的监管改革，包括新药的优先审评和有条件批准，以及加速试验批准的“默示许可”政策。加入国际人用药品注册技术协调理事会 (ICH) 并接受外国临床试验数据，进一步减少了在中国进行重复研究的必要性。这些变化导致 2017 年至 2023 年间中国的临床试验数量增加了两倍。

文章将这种增长与美国进行了对比，美国的临床试验数量已趋于平稳，且试验规模通常较小，并面临招募困难。中国的高招募率以及更快、更便宜的流程正在赋予其生物制药生态系统竞争优势。

作者建议，美国可以通过扩大医疗补助覆盖范围、简化文书工作和允许公平补偿等措施来实现临床研究试验的民主化，从而借鉴中国的经验。文章最终强调，使监管结构与参与激励措施保持一致对于释放试验能力和推动药物创新至关重要，美国需要适应才能在全球药物发现领域保持竞争力。

---

## 41. 计算机架构师找不到平均值

**原文标题**: Computer Architects Can't Find the Average

**原文链接**: [https://dgsq.net/2025-04-27-averages/](https://dgsq.net/2025-04-27-averages/)

本文探讨了计算机架构师之间关于如何对多个工作负载的性能结果进行平均的最佳方法的持续争论。虽然大多数人使用算术平均数或几何平均数，但 Hennessy 和 Patterson 提倡使用几何平均数，因为它具有参考计算机无关性的特性。

最近，Eeckhout 反驳了几何平均数，声称它缺乏“物理意义”，并提出了使用等时谐波加速 (ETS) 代替，ETS 是加速比的谐波平均数。ETS 具有物理意义：如果所有工作负载在基准系统上花费相同的时间，则 ETS 等于总加速比。

作者认为，这种物理意义通常无关紧要，因为实际的工作负载混合很少与基准测试一致。他们同意几何平均数也缺乏明确的物理意义，但它比使用一个其物理意义通常无关紧要的指标要好。

最终，作者认为，除非知道特定的工作负载混合，否则没有一个单一的平均值可以准确地预测真实系统上的性能。在这种情况下，他们建议使用加权平均值。否则，建议使用几何平均数，因为它具有熟悉性和易于比较性。

作者最后质疑了这场辩论的价值，并建议计算机架构师应该专注于开发真正创新的想法，而不是无休止地讨论最佳平均方法。无论使用何种平均方法，业内许多人都不信任学术评估。

---

## 42. 科技创业公司中的联合创始人比他们自己认为的价值要低。

**原文标题**: Business co-founders in tech startups are less valuable than they think

**原文链接**: [https://verdikapuku.com/posts/business-founders-are-less-valuable-than-they-think/](https://verdikapuku.com/posts/business-founders-are-less-valuable-than-they-think/)

本文认为，科技创业公司中非技术型的“商业”联合创始人往往被高估，并且难以找到技术合伙人，因为他们无法提供足够的价值，尤其是在早期阶段。作者观察到一个常见的模式：有想法但缺乏技术技能的商业人士在吸引技术联合创始人方面面临困难。

文章指出，核心问题源于一种扭曲的价值认知。这些商业创始人往往高估了他们最初的想法和领导能力的重要性，同时低估了技术执行的关键作用。他们可能表现出过度的自我膨胀，寻求支配而非平等合作，这会吓退有技能的工程师。

作者强调，早期阶段的价值在于构建产品和联系客户。由于技术联合创始人在前者方面表现出色，但通常缺乏后者，因此商业创始人可以通过专注于客户获取和验证来变得有价值。这意味着通过具体的行动（例如生成大量的等待名单或获得企业的意向书）来证明市场需求。

作者建议，与其盲目地构建产品，不如迭代营销材料以首先验证想法。对于商业创始人来说，真正的资产是建立和利用潜在客户或投资者的网络。拥有通往有价值网络的“热入口”以及推动业务前进的能力，是区分成功的商业创始人的关键属性。最终，证明自己有能力联系和获取客户，可以将商业创始人从一种负担提升为一种非常理想的资产。

---

## 43. 诺尔的“编程即理论构建”与大型语言模型取代人类程序员

**原文标题**: Naur's "Programming as Theory Building" and LLMs replacing human programmers

**原文链接**: [https://ratfactor.com/cards/naur-vs-llms](https://ratfactor.com/cards/naur-vs-llms)

本文反对大型语言模型（LLMs）可以取代人类程序员的观点，并借鉴了彼得·诺尔的“编程即理论构建”。核心论点是，正如吉尔伯特·赖尔所定义的那样，LLMs缺乏胜任编程所需的关键“理论”。

作者解释说，这里的“理论”不仅仅是对程序的了解，更是通过构建和维护程序所获得的深刻理解。这种理解使得程序员能够智能地工作、解释和讨论代码。农民创造路径的类比说明，了解完成的路径（代码）与创造路径（构建理论）的过程是不同的。

LLMs因为是在现有代码上训练的，所以只能看到“路径”，而没有经历“路径创造”。它们吸收的是理论构建的*结果*，而不是过程本身。这意味着它们可以模仿理解，但不能真正拥有它。诺尔认为，适应、修改和纠正大型程序依赖于与代码开发密切相关的程序员所拥有的这种“理论”。

作者强调，编程不仅仅是“文本生成”，即编写代码。它是关于构建和维护理论，类似于诗歌不仅仅是将文字串在一起。要取代程序员，LLMs要么需要发展出赖尔式的理论，要么诺尔对编程的理解需要从根本上是错误的，作者认为后者是不太可能的。

---

## 44. 2003–2023年美国药物过量死亡人数

**原文标题**: Drug Overdose Deaths in the United States, 2003–2023

**原文链接**: [https://www.cdc.gov/nchs/products/databriefs/db522.htm](https://www.cdc.gov/nchs/products/databriefs/db522.htm)

本NCHS数据简报利用国家生命统计系统的数据，研究了2003年至2023年美国药物过量死亡的情况。总体而言，在2003年至2022年显著增加后，2022年至2023年药物过量死亡年龄调整率下降了4.0%。

主要趋势包括：15-54岁人群的死亡率下降，但55岁及以上人群的死亡率上升。非西班牙裔白人个体过量死亡率下降，而非西班牙裔黑人和非西班牙裔夏威夷原住民或其他太平洋岛民人口的死亡率上升。

该报告还分析了特定药物导致的死亡情况。在持续近十年增长后，涉及非美沙酮的合成阿片类药物（主要是芬太尼）的死亡人数在2022年至2023年间略有下降。相反，涉及可卡因和具有滥用潜力的精神兴奋剂的死亡人数持续上升。涉及海洛因和天然及半合成阿片类药物的死亡人数下降。

2023年，共有105,007人死于药物过量，年龄调整率为每10万标准人口31.3人死亡。该报告强调了阿片类药物危机的持续影响，同时也指出了兴奋剂在药物过量死亡中日益重要的作用。

---

## 45. 解锁 Ractors：Object_id

**原文标题**: Unlocking Ractors: Object_id

**原文链接**: [https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html](https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html)

本文深入探讨了Ruby在多线程Ractor环境下`#object_id`方法的性能挑战以及优化工作。

历史上，`#object_id`是基于对象内存地址的简单除法运算。然而，随着Ruby 2.7中垃圾回收(GC)压缩的引入，对象地址可能会改变，因此需要一个更复杂和稳定的ID系统。这导致创建了两个内部哈希表来映射对象到ID以及ID到对象。

虽然这解决了稳定性问题，但也使`#object_id`变得更加昂贵且占用更多内存。此外，随着Ractor（Ruby的并发特性）的出现，这些共享哈希表成为争用点，需要全局VM锁，从而阻碍了性能。

作者概述了一种解决此问题的“去优化”方法。第一步是在仅当调用`ObjectSpace._id2ref`时才延迟创建id -> object表，因为它不常使用。

本文进一步探讨了一种潜在的优化方案，即直接将object_id存储在对象本身中，类似于实例变量，从而消除了对集中式哈希表及其相关锁的需求。然而，Ruby对“形状”（描述对象布局和可变性的数据结构）的使用增加了复杂性，特别是对于冻结对象。作者详细介绍了对形状系统进行的修改，以适应即使在冻结对象上存储object_id信息，从而确保一致的行为，而不会影响性能。

---

## 46. 微型模拟器

**原文标题**: Tiny Emulators

**原文链接**: [https://floooh.github.io/tiny8bit/](https://floooh.github.io/tiny8bit/)

微型模拟器

微型模拟器是一系列针对各种经典计算机和街机系统的模拟器集合，可以直接在浏览器中访问精选的演示和游戏。它专注于为每个模拟系统提供用户界面（UI）。

列表包括以下模拟器：

*   **东欧计算机：** KC85/2、KC85/3、KC85/4、KC Compact、Robotron Z1013、Robotron Z9001、Robotron KC87（带有 BASIC、FORTH 和 ASMDEV）。

*   **西方计算机：** Amstrad CPC464、Amstrad CPC6128、ZX Spectrum（48k 和 128）、Commodore VIC-20、Commodore C64 和 Acorn Atom、LC-80。

*   **街机系统：** 一些经典街机游戏。

内容主要列出了每个模拟系统可用的演示和游戏，重点强调了 Amstrad CPC 和 Commodore 64 的演示（“演示场景”）。每个标题旁边的 UI 元素表示用于与模拟内容交互的直接界面。 此外，还有指向外部资源的链接，如GitHub、IDE、Mastodon、Twitter和博客。

---

## 47. 令人着迷的日式木工几何纹样

**原文标题**: Mesmerizing Interlocking Geometric Patterns Produced with Japanese Woodworking

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/](https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/)

本文重点介绍了复杂的日本木工技术“组子”，它通过精确切割和互锁薄木条来创造重复的几何图案。组子最初用于屏风和家具镶嵌，现已发展成为一种因其自身设计而备受赞赏的艺术形式。

即将到来的华盛顿特区史密森尼工艺品展将展出组子艺术作品，展示当代工匠大卫·古特尼克的作品，他使用阿拉斯加雪松在家中工作室创作作品。古特尼克的作品融合了传统图案和自己的现代风格，利用不同的木材类型进行颜色对比，并将设计安装在布料上。虽然传统的组子依靠精确的角度和切口进行组装，无需粘合剂，但古特尼克为了作品的耐久性会使用少量胶水。

文章还提到了另一位参加工艺品展的木匠迈克尔·朱里，他将组子融入到他受Shaker和丹麦风格启发的家具中，使用椴木创作诸如麻叶（asa-no-ha）之类的传统图案。古特尼克强调了他自己在作品中看到的持续改进，他指出与早期项目相比，他现在可以更快、更精确地完成作品。

---

## 48. Show HN: 我创建了snapDOM，可以极快地将DOM节点捕获为图像

**原文标题**: Show HN: I created snapDOM to capture DOM nodes as images with exceptional speed

**原文链接**: [https://github.com/zumerlab/snapdom](https://github.com/zumerlab/snapdom)

snapDOM 是一款全新的轻量级 JavaScript 工具，用于以高保真和高速度将 HTML 元素捕获为图像。它专为平滑缩放过渡而开发，将 DOM 节点转换为可缩放的 SVG，从而保留样式、字体、背景、Shadow DOM 和伪元素。

主要功能包括：

*   完整 DOM 捕获，包括嵌入式样式和字体。
*   导出为 SVG、PNG、JPG、WebP 或 Canvas。
*   无依赖性，基于标准 Web API。
*   支持 Shadow DOM、伪元素，以及外部图像和字体的内联。
*   可在捕获期间排除元素或将其替换为占位符的选项。

它可以通过 NPM、Yarn、CDN 或 script 标签安装。该 API 提供了多种方法将元素捕获为不同的图像格式（SVG、PNG、JPG、WebP、Canvas），并提供缩放和质量调整选项。

snapDOM 拥有令人印象深刻的性能，在基准测试中优于其他流行的库，如 `modern-screenshot` 和 `html2canvas`，尤其是在捕获较大的 DOM 节点时。 局限性包括外部图像的 CORS 要求、字体需要完全加载以及缺乏 iframe 捕获。

该库根据 MIT 许可获得许可。

---

## 49. 未经授权的巨细胞病毒实验涉及人工智能生成的评论

**原文标题**: Unauthorized Experiment on CMV Involving AI-Generated Comments

**原文链接**: [https://simonwillison.net/2025/Apr/26/unauthorized-experiment-on-cmv/](https://simonwillison.net/2025/Apr/26/unauthorized-experiment-on-cmv/)

2024年11月至2025年3月，苏黎世大学的研究人员在r/changemyview子版块进行了一项未经授权的实验，使用人工智能生成的评论来影响用户的观点。数十个人工智能驱动的账户发布了旨在改变人们想法的回应。这一切都是在社区不知情或未经同意的情况下进行的。

该实验包括为人工智能账户创建虚假的人物角色和个人资料，例如“markusruscht”评论编造了整个家庭历史来支持其论点。研究团队以研究人工智能对社会影响的重要性为由，为他们的行为辩护，认为潜在的见解超过了违反社区规则的行为。他们声称对人工智能进行了审查，以防止有害内容。

然而，CMV版主强烈谴责这项实验为心理操纵和违反道德研究行为，强调了在大型语言模型影响研究中，存在未经同意的受试者研究的可能性。他们举报了该大学，但苏黎世大学为该项目辩护，称风险极小。一份文件披露了使用的提示，包括允许人工智能捏造个人经历作为一种说服策略的指示。

帖子的作者表达了强烈的不赞同，强调了实验的欺骗性以及对诚信讨论的侵犯。他们尤其对自己的观点可能受到研究机器人捏造的个人轶事影响的可能性感到不安。

---

## 50. 切：查塔努加市民用户测试

**原文标题**: Cut: Chattanooga Civic User Testing

**原文链接**: [https://cut.chattanooga.gov/](https://cut.chattanooga.gov/)

查塔努加市民用户测试小组邀请居民参与塑造城市的数字化服务，通过提供关于应用程序、网站和其他服务的反馈。参与者不需要技术专长，只需愿意分享他们的观点。

流程很简单：感兴趣的个人通过表格注册，当出现相关的测试机会时，他们将收到通知。在测试期间，参与者预览应用程序、网站或服务并提供反馈。作为对其时间和见解的回报，测试者将获得一张20美元的礼品卡。

查塔努加市强调社区投入的价值，并强调欢迎所有想法，无论其规模如何。该计划旨在通过纳入居民的观点，确保数字化服务用户友好并满足社区的需求，从而改进城市服务。市民用户测试小组是查塔努加市和信息技术部门的联合倡议。

---

## 51. Show HN: 开发中的 Common Lisp 实现，支持 ASDF

**原文标题**: Show HN: A Common Lisp implementation in development, supports ASDF

**原文链接**: [https://savannah.nongnu.org/p/alisp](https://savannah.nongnu.org/p/alisp)

`alisp`：在 Savannah 上开发的 Common Lisp 实现，由 Andrea Monaco 单独完成，旨在符合 Common Lisp 标准，但并非完全如此。 目前主要是一个解释器，并正在努力添加编译功能。 使用 C89 编写，并使用 GNU readline 和 GMP 库。

`alisp` 拥有对 Common Lisp 的大量支持，包括一个基本的性能分析器和具有单步执行功能的调试器。 作者鼓励提交错误报告和建议。 它在 GPL v3 或更高版本下获得许可，并通过 Liberapay 和 Patreon 欢迎捐赠。

最近的版本（直到 1.1 版）增加了诸如改进的 LOOP 支持、函数和文件编译、更好的路径名、性能分析器和步进器增强、观察点、美化打印机、编译器宏、CLOS 改进、检查工具、回溯打印机、更好的调试和符号宏等功能。 早期版本引入了 UTF-8 支持、填充指针、宏函数、泛型函数、标准对象、文件操作、重启、最小编译、基本调试器、性能分析器和错误修复。 由于频繁更新，作者建议使用最新的提交而不是 tarball。 该项目包含一个 `test.pl` 脚本，用于展示解释器的功能。

---

## 52. ZFS：苹果未能采用的新文件系统 (2016)

**原文标题**: ZFS: Apple's new filesystem that wasn't (2016)

**原文链接**: [https://ahl.dtrace.org/2016/06/15/apple_and_zfs/](https://ahl.dtrace.org/2016/06/15/apple_and_zfs/)

本文讲述了苹果公司早期接近采用，以及最终放弃ZFS文件系统的故事。作者从2006年开始，描述了最初苹果公司可能将ZFS用于Time Machine时所引发的兴奋，但最终令人失望。

2007年，苹果公司被传言将ZFS移植到Mac OS X，人们的期待再次高涨。然而，Sun公司CEO乔纳森·施瓦茨过早地宣布了苹果的计划，导致苹果淡化了这种集成，仅将其限制为只读版本。

尽管在2008年的WWDC上进行了颇有前景的展示，但ZFS的势头在2009年逐渐减弱，最终导致其在苹果内部被放弃。作者将此归因于几个因素：Sun被Oracle收购导致的不确定性，Sun和NetApp之间关于ZFS的诉讼，苹果内部的政治因素和“非我发明”综合征，以及许可问题。一些苹果领导层更倾向于开发自己的文件系统，认为ZFS是为服务器设计的，而不是为个人设备设计的。

在Sun被收购后，曾出现过短暂的复苏尝试，讨论围绕着苹果获得ZFS的赔偿，以及Sun获得AFP的访问权并将Sun的ZFS设备用作备份解决方案。然而，拉里·埃里森最终拒绝了这笔交易，声称他不与史蒂夫·乔布斯做生意。

最后，作者感叹苹果的决定，即使在APFS推出后，仍然觉得采用ZFS会是一个更好的选择，因为APFS需要大量的投资才能成熟到ZFS的水平。

---

## 53. 修复辛克莱C5

**原文标题**: Restoring a Sinclair C5

**原文链接**: [https://woof.tech/@crashtestdev/114411537491626882](https://woof.tech/@crashtestdev/114411537491626882)

此条目极其简短，本质上只是一个指向外部内容的 Mastodon 帖子。内容中没有足够的信息来提供关于修复 Sinclair C5 的文章的有意义的总结。我们只知道：

* 有一个名叫 JSON Alexander 的人在讨论 Sinclair C5 的修复。
* 他在 Woof.tech (一个 Mastodon 实例) 上发布了相关内容。
* 该帖子暗示“看到”了与该项目相关的东西。

要总结文章本身的内容，需要访问链接的资源。

---

## 54. Shardines：基于 ActiveRecord 的每个租户一个 SQLite3 数据库

**原文标题**: Shardines: SQLite3 Database-per-Tenant with ActiveRecord

**原文链接**: [https://blog.julik.nl/2025/04/a-can-of-shardines](https://blog.julik.nl/2025/04/a-can-of-shardines)

本文探讨了在 Rails 应用程序中实现基于每个租户数据库的多租户架构时面临的挑战和解决方案，特别是使用 SQLite3。作者分享了修复一个损坏的实现的经验，并探讨了在这种情况下 ActiveRecord 连接管理的复杂性。

“每个租户数据库”方法提供了诸如数据隔离、简化的备份（使用 `rsync`）以及更简单的调试等优势，因为您可以下载单个租户的数据。然而，Rails 的 ActiveRecord 是为大型共享数据库设计的，这使得它出乎意料地困难。

作者重点介绍了 ActiveRecord 从 Rails 1 到 Rails 7 的多数据库支持历史，强调了连接池和分片等功能如何迎合超大规模场景，而不是更小、隔离的 SQLite 数据库。该设计假定持久连接和早期初始化，这不适合于每个请求动态切换数据库。

“大型”数据库服务器针对少量大型数据库进行了优化，而 SQLite3 在处理许多小型数据库方面表现出色。每个租户的请求不需要来自其他租户的资源。作者认为，由于 SQLite3 基于文件的特性和缺乏配置开销，它非常适合这种模式。

本文最终指出，分片数据的大型应用程序和使用 SQLite 的较小多租户应用程序之间的需求存在差异。

---

## 55. 屹立不倒

**原文标题**: Still standing

**原文链接**: [https://blog.4chan.org/post/781845918774394880/still-standing](https://blog.4chan.org/post/781845918774394880/still-standing)

4chan宣布回归，此前于4月14日遭受重大安全漏洞攻击。一名黑客通过伪造的PDF上传，利用过时的软件包漏洞，访问了4chan的服务器、数据库和管理仪表板。在版主关闭网站之前，黑客提取了数据并破坏了网站。

此次损失惨重，源于因资源不足而疏于更新，而广告商和支付提供商屈服于外部压力运动导致多年的财务困境，加剧了这一问题。由于这些财务困境，该平台多年来一直使用二手服务器运行，难以投资升级。虽然6月份购买了新服务器并逐步实施，但在漏洞发生前并未完全集成。

被入侵的服务器已更换为更新的软件和操作系统。PDF上传暂时禁用（但会恢复），Flash版块(/f/)因漏洞利用而被永久关闭。4chan正在增加志愿开发者来帮助维护网站，并对清洁工和版主表示感谢。该信息强调了4chan的独特价值以及尽管面临挑战仍致力于保持运营的承诺。

---

## 56. 英特尔移除了第二代处理器之前的所有CPU信息页面。

**原文标题**: Intel Removed All CPU information pages before 2nd generation processors

**原文链接**: [https://old.reddit.com/r/intel/comments/1k8aqe5/intel_removed_all_cpu_information_pages_before/](https://old.reddit.com/r/intel/comments/1k8aqe5/intel_removed_all_cpu_information_pages_before/)

无法访问文章链接。

---

## 57. 大型语言模型知道谁对谁做了什么吗？

**原文标题**: Do Large Language Models know who did what to whom?

**原文链接**: [https://arxiv.org/abs/2504.16884](https://arxiv.org/abs/2504.16884)

这篇于2025年4月23日提交的arXiv论文，探讨了大型语言模型（LLMs）是否理解句子中的主题角色（谁对谁做了什么）。作者Joseph M. Denning、Xiaohan (Hannah) Guo、Bryor Snefjella和Idan A. Blank认为，对LLM理解能力的许多批评都集中于与语言处理无关的认知能力。相反，他们专注于主题角色分配，这是语言理解的一个关键要素。

该研究检验了四个LLM中的句子表征，以确定词预测训练目标是否能捕捉到主题角色。进行了两项实验。研究结果表明，LLM表征相似性主要反映句法相似性，这与人类的相似性判断不同，后者也考虑了主题角色（施事/受事）。研究人员发现，在模型的隐藏单元中，主题角色信息并没有广泛存在的证据。然而，发现LLM中的一些注意力头能够稳健地捕捉主题角色，且不受句法的影响。

结论是，LLM*能够*提取主题角色，但与人类相比，这些信息对其表征的影响较弱。本质上，LLM在一定程度上能够理解“谁对谁做了什么”，但在其整体句子表征中，它们优先考虑句法结构而不是主题角色分配。

---

## 58. Libogc (Wii 自制程序库) 被发现包含从 RTEMS 窃取的代码

**原文标题**: Libogc (Wii homebrew library) discovered to contain code stolen from RTEMS

**原文链接**: [https://github.com/fail0verflow/hbc/blob/80a80251f83f1993c272c58e471d040f3eb1dee9/README.md](https://github.com/fail0verflow/hbc/blob/80a80251f83f1993c272c58e471d040f3eb1dee9/README.md)

本文讨论了libogc的发现，该库是Wii自制软件开发的关键库，其中包含从任天堂SDK和开源RTEMS操作系统中窃取的代码。这一发现是在自制频道已经开始开发之后做出的，最初涉及在线程实现是原创的印象下使用libogc。

文章声称，libogc的最初作者shagkur故意剽窃代码，删除了署名和版权信息。当前的libogc开发者被指控忽视这个问题，删除提出的疑虑，并以辱骂回应。因此，文章的作者，即自制频道团队，认为该软件不可能合法编译，并且不能支持进一步的开发。

文章强调，Wii自制软件社区建立在侵犯版权的基础上，并敦促开发者要求SDK和工具包开发中的合法和道德实践。

文章包括自制频道源代码的公开发布，详细说明了包含和排除的部分。它提供了构建软件的说明，列出了必要的库和依赖项。源代码采用GNU通用公共许可证第2版或更高版本授权。

---

## 59. Show HN: 遥控宜家死星灯

**原文标题**: Show HN: Remote-Controlled IKEA Deathstar Lamp

**原文链接**: [https://gitlab.com/sephalon/deathstar_lamp](https://gitlab.com/sephalon/deathstar_lamp)

我无法提供摘要，因为内容是“加载中”，没有实际文章内容可以总结。

---

## 60. Luculent：手动微调等宽字体，小尺寸下清晰锐利 (2015)

**原文标题**: Luculent: Manually hinted monospace font, crisp at tiny sizes (2015)

**原文链接**: [http://eastfarthing.com/luculent/](http://eastfarthing.com/luculent/)

Luculent 是一款由 Andrew Kensler 于 2008 年创建的手动微调几何无衬线等宽字体家族，专为长时间审视代码的程序员设计。 2015 年发布的 2.0.0 版本包括用于语法高亮的常规体、斜体、粗体和粗斜体样式。

Luculent 注重清晰度，采用独特的字形、夸张的特征（如句点和花括号）以及分号和逗号的长尾巴。它拥有广泛的覆盖范围，包括 Adobe Latin 3、HTML 4 实体、ISO-8859 和 Windows 代码页、DOS CP437（框线绘制）以及基本的 Powerline 支持。

一个关键特性是其精细的手动微调，每个字体平均包含 47KB 的 TrueType 字节码，即使在小尺寸（5x11 像素）下也能呈现清晰的效果。它针对抗锯齿渲染和跨平台兼容性（FreeType、Windows、OS X）进行了优化，并具有特殊的逻辑来减少 Windows Cleartype 上的模糊感。

该字体有三种形式：带微调的标准 TTF、用于 Web 的压缩 WOFF，以及用于忽略微调的特定点大小和分辨率系统的“预微调”TTF 文件。 Luculent 根据 Open Font License 协议分发，可以 zip 和 tar.xz 格式下载。 2015 年的更新增加了显著的字符覆盖范围和大量的改进。

---

## 61. Windows 不是一个操作系统，而是一个想变成瘾的坏习惯。

**原文标题**: Windows isn't an OS, it's a bad habit that wants to become an addiction

**原文链接**: [https://www.theregister.com/2025/04/28/windows_opinion/](https://www.theregister.com/2025/04/28/windows_opinion/)

鲁伯特·古德温斯认为，Windows正在从有用的工具演变为越来越具侵入性和盈利性的平台，就像一种坏习惯，接近成瘾。 他批评微软强迫用户接受不需要的功能，特别是人工智能集成和持续不断的广告，而几乎没有提供真正的改进。 他预计随着未来版本的出现，情况会变得更糟，比如Windows 12（可能现在是Win 11 24H2），甚至可能转向订阅模式。

古德温斯认为，虽然公司环境可能离不开Windows，但个人和小型公司有其他选择。 他建议采取一种战略性的“戒除”方法，而不是突然切换。 他建议使用长期支持选项和软件包管理器来延长精简版Windows 10的寿命。 从长远来看，他建议探索macOS或Linux。 虽然macOS提供了一个更友好的替代方案（尽管仍然是一个封闭的生态系统），但Linux提供了最大的自由，但需要更陡峭的学习曲线。

他提倡逐步将新操作系统集成到日常工作流程中，从简单的任务和小项目开始，同时保留Windows用于熟悉的应用程序。 目标不是快速切换，而是为用户在未来能够更好地控制计算体验做好准备。 最终，古德温斯强调选择最适合个人需求和偏好的操作系统，从而提高幸福感和生产力。

---

## 62. 如何用C语言编写文字冒险游戏

**原文标题**: How to program a text adventure in C

**原文链接**: [https://helderman.github.io/htpataic/htpataic01.html](https://helderman.github.io/htpataic/htpataic01.html)

本文介绍了一个使用C语言编写文字冒险游戏的教程。它假定读者具有基本的C编程知识，并且对从头开始制作基于文本的游戏的艺术感兴趣，可能是出于怀旧或为了学习经验。

作者承认通常建议使用专门的冒险游戏开发系统，但本教程探讨使用C语言作为娱乐、挑战和教育的一种方式。C语言与硬件的紧密联系使其能够探索类似于早期家用电脑冒险游戏开发的技巧，当时内存限制是一个主要问题。虽然像Java、C#或Python这样的语言也可以使用类似的原则，但选择C语言是因为作者的熟悉程度以及它能够很好地映射到汇编代码。

本教程强调增量开发。每个章节都会添加功能，每次增量后都会产生一个可运行的程序。第一个例子是一个简单的“Hello World”程序，它介绍了文字冒险游戏的核心元素：描述性文本。重点将放在编程方面，将故事创作留给读者。本文提供了代码、对其基本组成部分的解释，以及下载源代码并在Repl.it上运行它的链接。下一章将介绍游戏的主循环。

---

## 63. 欧洲关键依赖

**原文标题**: European Critical Dependencies

**原文链接**: [https://jurgen.gaeremyn.be/2025/03/08/european-critical-dependencies/](https://jurgen.gaeremyn.be/2025/03/08/european-critical-dependencies/)

欧洲关键依赖
这篇文章题为“欧洲关键依赖”，强调了欧洲市政机构和公共服务部门对微软服务的严重依赖，尤其是电子邮件。作者通过MX服务器映射研究发现，在比利时、荷兰、挪威、瑞典和芬兰等国，很大比例的地方政府依赖微软的电子邮件基础设施，芬兰甚至高达77%。这种依赖引发了人们对供应商锁定、潜在的价格上涨、美国《云法案》等法律的适用以及整体数字主权的担忧。

文章对比了德国和匈牙利等国，它们对微软的依赖程度明显较低。文章列举了荷兰、芬兰、瑞典和挪威等国日益增长的担忧和政策变化，旨在解决这种过度依赖。丹麦数据保护机构对学校中使用谷歌服务的行为也进一步强调了这些担忧。

作者认为，欧洲需要优先建设自己的基础设施，培养本地人才，并推广开放标准和开源解决方案，以确保长期的独立性和数字主权。开源允许代码共享、定制，并防止不回馈的逐利行为。他敦促政策制定者和公民质疑正在做出的选择，并推动蓬勃发展的FOSS生态系统的发展。欧洲等待的时间越长，就越难摆脱这种依赖。

---

## 64. Show HN: 我自己写的业余爱好操作系统终于在我的老式IBM ThinkPad上运行了

**原文标题**: Show HN: My self-written hobby OS is finally running on my vintage IBM ThinkPad

**原文链接**: [https://github.com/joexbayer/RetrOS-32](https://github.com/joexbayer/RetrOS-32)

“Show HN”：RetrOS 32位，一个基于i386架构的网络化操作系统项目

该“Show HN”帖子介绍了RetrOS 32位，一个由Joe Bayer编写并于2022年5月启动的业余操作系统项目，专注于i386架构上的网络功能。该操作系统具有图形界面、多任务处理和网络功能，并在包括一台老式IBM ThinkPad a21p在内的各种硬件上进行了测试。

该项目内核和实用工具使用C和汇编语言编写，用户应用程序使用C++编写，编译使用Make。Docker方便了跨平台编译。操作系统提供默认用户（系统、管理员、访客），并具有创建新用户的能力。

该帖子详细介绍了如何开始使用，包括Docker和QEMU（或原生i386-elf工具）等先决条件，以及Linux、MacOS（使用Docker）和Windows（使用Docker或WSL）的安装说明。文章提供了使用copy.sh/v86、QEMU或真实硬件启动操作系统的说明。

该帖子概述了项目结构，并提供了一个具有远大目标的路线图，包括实现自定义引导加载程序、多线程、内存管理、完整的网络堆栈（以太网、IP、TCP、HTTP等）、文件系统（Ext2类似和FAT16）、窗口管理器、各种应用程序（终端、编辑器、计算器、贪吃蛇）以及自定义C编译器/解释器。RetrOS 32位在MIT许可证下获得许可，该项目托管在GitHub上。

---

## 65. Pkg.pl: Scryer Prolog实验性包管理器

**原文标题**: Pkg.pl: An experimental package manager for Scryer Prolog

**原文链接**: [https://github.com/bakaq/pkg.pl](https://github.com/bakaq/pkg.pl)

本文档描述了`pkg.pl`，这是一个用于Scryer Prolog语言的实验性包管理器。它仍在开发中，由于安全漏洞，目前不适合通用，它作为探索Scryer Prolog包管理策略的平台。

一个Scryer Prolog包是一个包含`scryer-manifest.pl`文件的目录。该清单定义了包的`name/1`，一个可选的`main_file/1`用于导入，以及一个`dependencies/1`列表，指定用于克隆的git URL。

要使用包管理器，请将`pkg.pl`复制到您的项目中。命令`scryer-prolog pkg.pl -g pkg_install,halt`将依赖项下载到`scryer_libs`目录。目前，它只处理直接依赖项，不处理传递依赖项。

包通过`use_module(pkg).`加载，然后通过`use_module(pkg(package_name)).`加载，其中`package_name`与包清单中的`name/1`字段匹配。加载后，包的`main_file`导出的谓词在当前程序中可用。

作者鼓励通过问题和拉取请求提供贡献、建议和讨论。

---

## 66. 校准存在语境崩溃问题

**原文标题**: Calibrations Have a Context-Collapse Problem

**原文链接**: [https://www.oldschoolburke.com/011-calibrations-have-a-context-collapse-problem/](https://www.oldschoolburke.com/011-calibrations-have-a-context-collapse-problem/)

本文认为，组织中的绩效校准会议存在“语境崩塌”现象。该现象借鉴自社交媒体，指的是面向特定受众的信息由于参考框架不同而被他人误解。在校准中，这表现为来自不同专业（前端、后端等）的管理者误解工程师在其专业领域之外的工作的复杂性和影响。

作者强调了这种语境扭曲的几个维度，包括特定领域的盲点、特定技术的偏见、可见性偏见（偏好可见的UI工作而不是幕后改进）、“游说彩票”（取决于管理者的叙事能力）、锚定效应、对绩效评级的不同解释、时间限制、增长与影响的不一致，以及管理者有计划的系统性行为。

这些问题导致人才失望、职业生涯轨迹偏差、管理者信誉受损和组织盲点，从而阻碍了整个工程文化。

文章提出了潜在的解决方案，包括创建特定领域的校准、跨职能预审、让工程师参与共同撰写绩效叙述、标准化成就格式、认可无形的贡献（可靠性、指导）、实施持续校准（季度检查）、将反馈与评估分离、审计评级膨胀，以及设计能够阻止有计划行为的流程。作者提倡接受细微差别并认识到工程工作的复杂性，以创建更公平、更有效的绩效评估。

---

## 67. 斯塔西的“瓦解”与现代心理战

**原文标题**: STASI's Zersetzung and Modern Psychological Warfare

**原文链接**: [https://www.mariobekes.com.au/from-berlin-to-the-digital-age-stasis-zersetzung-and-the-modern-battle-of-psychological-warfare/](https://www.mariobekes.com.au/from-berlin-to-the-digital-age-stasis-zersetzung-and-the-modern-battle-of-psychological-warfare/)

本文探讨了东德秘密警察“斯塔西”的“瓦解”（Zersetzung）策略，这是一种隐蔽的心理战策略，旨在瓦解异议，并削弱那些被认为是国家敌人的个人。“瓦解”意味着“解体”，其目的是通过心理操纵而非公开的身体攻击，来巧妙地削弱一个人的身份和意志。

本文详细介绍了“瓦解”的机制，包括社会孤立、心理操纵和煤气灯效应、制造偏执、人身攻击以及施加身心疲劳。这些策略旨在使目标怀疑自己的理智、感到孤立并经历持续的压力，最终导致他们的士气低落和屈服。

“瓦解”的遗害是它给受害者留下了持久的心理创伤，并令人不寒而栗地提醒人们，极权主义政权会采取何种程度的手段来控制其公民。

本文进一步指出，类似的心理战策略今天仍然被包括中国和俄罗斯在内的专制政权所使用，并且也应用于在线操纵、政治竞争和企业行为中。这些做法的例子包括虚假信息宣传、利用社交媒体“水军工厂”以及针对记者、活动家和政治异议人士的骚扰活动。这些现代“瓦解”式技术的应用表明，心理操纵作为一种控制和破坏稳定的工具，仍然具有现实意义。

---

## 68. 浏览器中的开源交互式C语言教程

**原文标题**: Open-source interactive C tutorial in the browser

**原文链接**: [https://www.learn-c.org/](https://www.learn-c.org/)

Learn-c.org 提供免费的互动式 C 语言教程，可在浏览器中直接访问，无需下载。该教程专为初学者和有经验的程序员设计。

该网站提供结构化的课程，涵盖基本的 C 语言概念，如“Hello, World!”、变量、数据类型、数组、循环、函数，以及更高级的主题，如指针、结构、动态分配、递归、链表、二叉树、联合和位掩码。该教程的一个关键方面是其互动性，允许用户通过实践来练习和学习。

该网站目前正在开发中，欢迎大家为教程做出贡献。内容分为章节，涵盖特定的 C 语言编程主题，可通过导航轻松访问。用户可以从基础知识入手，也可以根据需要跳转到更高级的主题。该网站还提供使用条款和隐私政策的链接。

---

## 69. 解包加壳的可执行文件

**原文标题**: Unpacking Packed Executables

**原文链接**: [https://neugierig.org/software/blog/2025/04/unpacking.html](https://neugierig.org/software/blog/2025/04/unpacking.html)

本文详细介绍了对打包的可执行文件进行解包的过程，特别是在retrowin32模拟环境中的应用，以便使用Ghidra等工具进行更轻松的静态分析。打包的可执行文件经过压缩以减小文件大小，但它们的真实代码和系统调用在运行时之前都是隐藏的，这使得调试和分析变得困难。

作者概述了以编程方式解包这些可执行文件所涉及的挑战和解决方案。首先，模拟器需要找到解包后的代码的入口点，通常是在解包例程后的`jmp`或`ret`指令之后。标准的断点最初无法工作，因为它们会被解包循环覆盖。相反，断点设置在解包代码的末尾，并进行单步调试。

第二个关键问题是重建导入地址表 (IAT) 和导入目录表 (IDT)。打包的可执行文件具有最小的初始导入表。解包过程使用`LoadLibrary`和`GetProcAddress`动态加载库和函数，并填充解包后的可执行文件的 IAT。

为了重建用于静态分析的IDT，模拟器会观察对`GetProcAddress`的调用，记录返回的函数地址，然后扫描解包后的内存以找到这些地址的存储位置（可能在IAT中）。一旦找到 IAT，就会创建一个新的IDT，将函数名称映射到地址，并将其插入到转储的可执行文件中。作者已在retrowin32中成功实现了这一点，从而使Ghidra能够正确识别和显示解包后的可执行文件中的系统函数调用。

---

## 70. 终结所有前列腺问题？

**原文标题**: An end to all this prostate trouble?

**原文链接**: [https://yarchive.net/blog/prostate/](https://yarchive.net/blog/prostate/)

本文探讨了以色列医生 Gat 和 Goren 提出的关于良性前列腺增生 (BPH)、前列腺癌和精索静脉曲张的机械原因的理论：精索静脉中的瓣膜故障导致富含睾酮、缺氧的血液倒流至前列腺。

通常，来自睾丸的血液通过配备单向瓣膜的精索静脉向上流向肾静脉和腔静脉。当这些瓣膜失效时，血液会倒流，使睾丸浸泡在氧气不足的血液中，导致不育。更重要的是，这种倒流使前列腺充斥着高水平的游离睾酮，促进异常生长，导致 BPH，并可能导致癌症。该理论还解释了为什么给男性服用睾酮补充剂不一定会增加前列腺癌的风险，因为它会关闭他们自身的睾酮生成，从而防止倒流。

Gat 和 Goren 通过手术破坏精索静脉来治疗这种情况，从而防止倒流。他们利用透视检查来确认倒流，然后在注射硬化剂以永久性关闭静脉。他们强调彻底关闭两条精索静脉并检查侧支循环。

文章承认，尽管发表了研究，但这一理论并未得到广泛采用，即使面对对复杂医学问题的更简单解释也是如此。然而，它提出了对该理论机械基础的担忧，质疑仅靠重力压力是否能驱动静脉中的自发逆循环。尽管如此，记录在案的逆流需要一个解释，而这一理论可能是一个解决方案的开端。

---

## 71. 首都圈外郭放水路

**原文标题**: Tokyo Metropolitan Area Outer Underground Discharge Channel

**原文链接**: [https://www.japan.travel/en/spot/1524/](https://www.japan.travel/en/spot/1524/)

位于东京附近埼玉县春日部市的首都圈外郭放水路是世界最大的地下排水系统。这座令人印象深刻的工程奇迹建于1993年至2006年间，旨在保护地势较低的东京免受暴雨和台风季的洪水侵袭。该系统由一个50米深、6.3公里长的混凝土隧道组成，连接着五个巨大的竖井，每个竖井都大到足以容纳自由女神像。在强降雨期间，周围河流的水进入竖井，然后通过隧道流入加压水箱，最后排入江户川。

在不用于防洪时，放水路会向公众开放付费参观。游客首先在龙Q馆地下探险博物馆了解该系统的建造和运作，然后再进入地下隧道。安全是首要考虑因素，参观需要会说日语的人员陪同，并使用头盔和安全带。该场所独特的、超凡脱俗的氛围使其成为电影、广告的热门拍摄地，也是视频游戏设计的灵感来源。前往那里需要乘坐东武野田线到南樱井站，然后乘坐一小段出租车。由于参观非常受欢迎，建议提前四周左右预订。

---

## 72. RSS 不一定意味着信息洪流

**原文标题**: RSS doesn't necessarily means firehose

**原文链接**: [https://andregarzia.com/2025/04/rss-doesnt-necessarily-means-firehose.html](https://andregarzia.com/2025/04/rss-doesnt-necessarily-means-firehose.html)

本文认为，RSS阅读器不必是令人应接不暇的“信息洪流”，并引用了传统订阅源阅读器中不断涌现的新帖子带来的压力感这一常见体验。作者指出，许多RSS阅读器，如NetNewsWire，采用了类似于电子邮件客户端的“信息流”方法，按时间倒序呈现帖子，加剧了信息过载。

虽然有些用户可能喜欢这种方法，但作者强调了其他优先考虑更平静、更可控体验的订阅源阅读体验。他们特别提到了FraidyCat，它可以防止任何单一发布者主导订阅源，并允许用户控制获取频率，以及Rad Reader，它提供了一个极简界面，仅显示最近更新的网站及其最新的三个帖子。

受这些替代方案的启发，作者创建了BlogCat，这是一个浏览器Web扩展，提供类似的受控体验，而无需后台获取或通知。作者的结论是，RSS只是数据，其呈现方式不必令人感到压力巨大。他们鼓励读者探索不同的RSS阅读器应用程序，以找到适合自己偏好的应用程序，甚至可以考虑开发自己的应用程序。核心信息是，除了标准的“信息洪流”RSS体验之外，用户还有其他选择。

---

## 73. 为什么电子不会掉进原子核？

**原文标题**: Why do electrons not fall into the nucleus?

**原文链接**: [https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/09._The_Hydrogen_Atom/Atomic_Theory/Why_atoms_do_not_Collapse](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/09._The_Hydrogen_Atom/Atomic_Theory/Why_atoms_do_not_Collapse)

本文旨在纠正关于电子像行星一样绕原子核运行的常见误解。它解释说，这种经典模型虽然因重力与库仑力之间的相似性而直观，但从根本上是有缺陷的，因为加速的带电粒子（如旋转的电子）会发射电磁辐射，导致它们失去能量并螺旋落入原子核。

量子力学提供了解决方案。它指出，电子的位置和速度不能同时被精确地定义。当电子接近原子核时，其势能会降低到负无穷大，而动能会增加到正无穷大。这种“无穷大之战”导致了一种妥协，即电子存在于距离原子核的平均距离处，大致对应于玻尔半径。

本文强调了概率密度和径向概率之间的区别。概率密度描述了特定点上单位体积的电子电荷，并显示电子最有可能*在*原子核处被发现。然而，径向概率考虑了随着距离原子核增加而增加的体积，表示给定半径的球面上所有点的电子密度总和。基态氢原子的径向概率图的峰值对应于玻尔半径。

最终，量子力学通过承认电子的波动性、不确定性原理以及势能和动能之间的动态相互作用，来防止电子坍缩到原子核中。电子不会“落入”原子核，因为它不能被视为原子内具有确定位置和动量的经典粒子。

---

## 74. 美国自闭症数据项目引发关于伦理、隐私和意图的争议

**原文标题**: U.S. autism data project sparks uproar over ethics, privacy and intent

**原文链接**: [https://www.washingtonpost.com/health/2025/04/25/autism-registry-privacy-rfk-research/](https://www.washingtonpost.com/health/2025/04/25/autism-registry-privacy-rfk-research/)

无法访问文章链接。

---

## 75. NASA如何利用图技术和大型语言模型构建人员知识图谱

**原文标题**: How NASA Is Using Graph Technology and LLMs to Build a People Knowledge Graph

**原文链接**: [https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph](https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph)

美国国家航空航天局利用图技术和大型语言模型（LLM）构建“人员知识图谱”，以转变机构内部的人员分析。该计划旨在通过连接美国国家航空航天局的人员、项目和技能，更好地识别专家、组建团队并规划未来的技能需求。

人员知识图谱利用图数据库Memgraph来实时处理复杂的关系。该系统在NASA安全的AWS云上运行，集成了在Docker中运行的Memgraph、本地LLM服务器（Olama）、用于数据存储的AWS S3和用于数据摄取的GQLAlchemy等组件。

数据从各种来源摄取，包括人事数据、AI/ML项目注册表以及从简历中提取的技能。LLM用于从简历和项目描述中提取技能，并识别相似的项目以构建图关系。

图模式包括代表员工、职位、组织、中心、项目、教育和技能的节点。实施了一个基于GraphRAG的聊天机器人，允许用户使用自然语言查询图谱，以识别主题专家、生成领导报告和检测项目重叠。RAG流水线使用LLM从问题中提取关键信息，并对图节点执行枢轴搜索和相关性扩展。

该项目正在进行中，计划扩大图谱规模、提高数据质量、自动化数据管道并提高RAG的准确性。美国国家航空航天局的目标是将图谱扩展到超过50万个节点和数百万条边。选择Memgraph的原因在于其成本效益、Cypher查询语言兼容性和Python支持。

---

## 76. 图标

**原文标题**: Icônes

**原文链接**: [https://icones.js.org/](https://icones.js.org/)

文章“Icônes”（图标）本质上只是一个标题，提示中没有提供任何实质内容。因此，在没有更多信息的情况下，不可能进行总结。我们只知道文章的名称是“Icônes”，英文翻译为“Icons”（图标）。

假设文章 *确实* 是关于图标的，一个推测性的总结可能是：

文章“Icônes”可能讨论图标的概念。在没有更多信息的情况下，不可能知道具体的角度。可能的主题包括：

*   **宗教图标：** 讨论宗教图像及其在各种信仰中的意义（例如，东正教基督教图标）。
*   **数字图标：** 探索图标在计算机界面中的使用及其在可用性和用户体验中的作用。
*   **标志性人物：** 考察在流行文化、历史或艺术中被认为是标志性的有影响力的人物或符号。
*   **视觉传达：** 分析图标作为一种视觉传达形式及其在传达意义方面的有效性。

文章可能会探讨图标的历史、象征意义、艺术技巧、文化影响或现代诠释，具体取决于其重点。然而，在提供实际内容之前，这仍然只是推测。

---

## 77. 填充-Na(a)N：填充你的NaN值

**原文标题**: Stuffed-Na(a)N: stuff your NaNs

**原文链接**: [https://github.com/si14/stuffed-naan-js](https://github.com/si14/stuffed-naan-js)

Stuffed-Na(a)N：一个在 NaN 值中编码数据的古怪 JavaScript 库，它利用了 IEEE 754 浮点数的特性。标准的 JavaScript 操作可能产生 `NaN`，它具有特定的二进制表示，其中尾数部分可以被操纵。"stuffed-naan" 将数据编码在 NaN 值的尾数部分。

该库提供了 `encode` 和 `decode` 函数。编码将字符串转换为 NaN 数组，解码则反转此过程。文章幽默地宣传了该库的特性，包括其“紧凑性”（讽刺地导致数据扩展）、速度以及由于不寻常的编码方式而带来的“隐私优先”特性。

它分为社区版和企业版，后者提供更好的压缩、对不同处理器架构的支持以及专属的客户支持。作者开玩笑地说要利用 IEEE 标准进行“犯罪”和“走私数据”，突出了这种非常规的数据存储方法。路线图概述了未来的开发计划，包括基准测试、模糊测试、用 Rust 重写以及形式验证。文章最后呼吁支持当地咖喱餐厅，并链接到作者的社交媒体。最终，"stuffed-naan" 被呈现为一种轻松的，尽管非常规的，在 NaN 值中进行数据编码的方法。

---

## 78. 发现一个简单的数据库建模工具：dbdiagram.io

**原文标题**: Found a simple tool for database modeling: dbdiagram.io

**原文链接**: [https://dbdiagram.io](https://dbdiagram.io)

本文重点介绍dbdiagram.io，一个简单实用的数据库关系图（ERD）设计工具。其核心信息是dbdiagram.io提供了一种直接有效的方式来可视化地呈现和设计数据库的结构，侧重于表及其属性之间的关系。

文章的简洁性表明它要么是一个介绍性公告，要么是一个推荐，而不是一篇深入的评论。我们可以推断出该工具可能提供了一个用户友好的界面，使用户能够快速创建和修改数据库图。它可能面向开发人员、数据库管理员以及任何需要可视化方式来建模数据库结构的数据库设计人员。

标题强调了该工具的简单性及其创建的图表类型，使读者能够轻松理解使用dbdiagram.io的目的和潜在好处。

---

## 79. 越南战争结束五十年，但与橙剂的斗争仍在继续

**原文标题**: The Vietnam War ended 50 years ago, but the battle with Agent Orange continues

**原文链接**: [https://apnews.com/article/vietnam-war-anniversary-agent-orange-0829caefe48cc11fb88ab27982da922b](https://apnews.com/article/vietnam-war-anniversary-agent-orange-0829caefe48cc11fb88ab27982da922b)

以下是美联社新闻文章《越南战争结束50周年，“橙剂”之战仍在继续》的摘要：

文章强调，尽管越南战争结束50周年，但“橙剂”的毁灭性影响仍在困扰越南和美国。“橙剂”是美军使用的一种剧毒除草剂，用于清除丛林植被并摧毁敌人的掩护，造成了广泛的环境破坏和严重的健康问题。

文章强调了暴露于该化学物质的越南公民和美国退伍军人持续遭受的痛苦。许多越南人继续出生时带有因接触“橙剂”而导致的严重残疾，对他们的支持网络往往不堪重负。美国退伍军人也患有与该除草剂相关的癌症、神经系统疾病和其他疾病。

虽然美国政府已为清理污染地区和支持患有“橙剂”相关健康问题的人提供了一些援助，但文章指出，许多人认为这还不够。文章指出，正在努力净化美国前空军基地（主要的污染源），但也承认仍有许多工作要做。此外，文章表明，仍需进一步承认和支持受“橙剂”影响的越南受害者和美国退伍军人。总而言之，“橙剂”的遗留问题是对战争持久影响以及应对其后果的持续挑战的严峻提醒。

---

## 80. 看 o3 猜测照片地点，既超现实，又反乌托邦，还很搞笑。

**原文标题**: Watching o3 guess a photo's location is surreal, dystopian and entertaining

**原文链接**: [https://simonwillison.net/2025/Apr/26/o3-photo-locations/](https://simonwillison.net/2025/Apr/26/o3-photo-locations/)

本文探讨了作者使用OpenAI最新o3模型猜测照片拍摄地点的体验。作者发现，观看人工智能“思考”并分析图像的过程既超现实又反乌托邦，而且还饶有趣味，就像《犯罪现场调查》中的一个场景，技术增强图像并利用庞大的数据库。

作者通过提供一张在加利福尼亚州埃尔格兰纳达附近拍摄的照片来测试o3，并剥离了EXIF数据以防止作弊。人工智能起初有些挣扎，但随后开始利用其视觉能力分析照片，放大车牌等细节。最终，它得出结论，照片很可能是在加利福尼亚州坎布里亚（位于加州中央海岸）拍摄的，但作为备选方案，它建议了半月湾-埃尔格兰纳达，这正是拍摄地点。

作者指出，其他模型（如Claude 3.7 Sonnet）也可以执行类似的任务，尽管没有“缩放”功能。作者认为，缩放之所以有效，是因为模型的视觉输入很可能处于较低的分辨率。

作者强调了这项技术的双重性：观看它既令人着迷又有趣，但从隐私和安全角度来看也可能令人担忧，突显了理解即使是看似无害的照片也可以用来确定某人位置的重要性。

一项更新显示，o3确实可以访问用户的近似位置，但作者确认，位置猜测技巧对于在远处拍摄的照片仍然有效。

---

## 81. 巴特动漫吉祥物

**原文标题**: BART's Anime Mascots

**原文链接**: [https://www.bart.gov/news/fun/anime](https://www.bart.gov/news/fun/anime)

为了推广公共交通，尤其是在年轻乘客中，湾区捷运（BART）推出了动漫吉祥物Mira和Jasmine。受日本和台湾类似举措以及现实中BART员工和动物的名气启发，这些吉祥物旨在与湾区社区建立友好且平易近人的联系。

在2022年向加州艺术家公开征集后，共收到近500份投稿，最终选定了这些吉祥物。BART与选定的艺术家合作，对角色进行概念化和开发。

这些吉祥物包括：

*   **Baylee：**一位了解湾区的东湾网红。
*   **Nimbus：**一位受湾区景观启发，并有一只鹰陪伴的作家。
*   **Jasmine：**一位高中生、时装设计师和火车爱好者。
*   **Mira：**一位前系统服务人员，现任列车运营员。
*   **Barty：**一辆遗留BART列车的转世兔子精灵。

BART鼓励吉祥物的角色扮演，并提供资源，例如“如何制作BART列车服装”指南和角色扮演指南。Jasmine和Mira的涂色页也已提供。所有吉祥物的官方商品，包括亚克力立牌和贴纸，都可以在railgoods.com/bart/anime购买。

---

## 82. 6502 CPU的晶体管级可视化模拟

**原文标题**: Visual Transistor-level Simulation of the 6502 CPU

**原文链接**: [http://www.visual6502.org/](http://www.visual6502.org/)

Visual6502.org：通过可视化和直观方式保存、研究和记录历史计算机的项目。其主要关注点是经典芯片MOS 6502处理器。该团队基于物理芯片晶圆和基板的高分辨率照片，创建了6502的高度详细数字模型和晶体管级模拟。这涉及创建约20,000个独立组件的矢量多边形模型。

该模拟足够精确，可以运行Atari游戏等经典的6502程序。一个关键特性是能够通过根据逻辑状态（“高”或“低”）为多边形着色来直观地表示芯片的运行，从而清楚地了解芯片如何处理信息和执行程序。

除了6502之外，该项目还在扩展到其他芯片，包括Atari 2600 TIA、Commodore SID芯片以及来自Zilog、AMD、Intel和Motorola等其他制造商的芯片。他们正在积极寻求芯片捐赠，特别是损坏的芯片，以便进行建模和模拟。

该项目在SIGGRAPH 2010上首次亮相，并吸引了大量观众，在其最初的15个月内拥有超过25万独立访问者。他们的目标是通过模拟来保存历史硬件的功能，确保即使在原始设备发生故障后，它仍然可以访问。他们还向苹果公司联合创始人史蒂夫·乔布斯致敬，认可了他产生的深刻影响。

---

## 83. 编译器提示

**原文标题**: Compiler Reminders

**原文链接**: [https://jfmengels.net/compiler-reminders/](https://jfmengels.net/compiler-reminders/)

本文强调了 Elm 中“编译器提醒”的重要性，该特性对代码可维护性做出了重大贡献。编译器提醒是指当代码变更需要修改其他部分时，编译器发出的错误提示，以此提醒开发者。文章以在基本的 Elm 计数器中添加重置按钮为例，说明了编译器如何引导开发者完成必要的步骤，从而确保功能的完整性和可用性。

作者强调，这些由类型和完备性检查驱动的提醒是“编译器驱动开发”的关键方面，并有助于实现“编译通过即可运行”的理念。避免在 `case` 表达式中使用通配符分支可以提高这些有益提醒的频率。

文章将该概念扩展到编译器之外，解释了 linters 如何提供类似的提醒，例如标记未使用的变量或在添加新类型时提示更新列表。自定义 linting 规则允许针对特定代码库要求定制提醒。作者认为，测试也可以充当提醒。

最终，文章提倡利用各种工具来创建提醒，以防止疏忽并确保代码一致性，从而实现更易于维护的代码库。这些提醒还可以作为协作者的隐式文档，引导他们遵循代码库的约定。

---

## 84. 爸和鸡蛋控制器 (2018)

**原文标题**: Dad and the Egg Controller (2018)

**原文链接**: [https://www.pentadact.com/2018-12-18-dad-and-the-egg-controller/](https://www.pentadact.com/2018-12-18-dad-and-the-egg-controller/)

汤姆·弗朗西斯讲述了他尝试操作“鸡蛋控制器”的经历，这是他身为发明家的父亲为了自动控制Big Green Egg烤炉的温度而定制的设备。他的父亲喜欢用Big Green Egg烹饪，但觉得手动调节温度很麻烦。汤姆在父亲去世后继承了鸡蛋控制器，感到有责任去理解和使用它。

他描述了该设备的组成部分：一台电脑、一个温度计和一个风扇系统。尽管他有技术背景，但汤姆最初甚至难以将其打开。经过多次使用9伏电池和反接连接的反复试验，他终于设法让它运行起来。

然后，他尝试用鸡蛋控制器烹饪鸡胸肉，但发现烤炉的温度无情地上升，忽略了设定的参数。他感到沮丧，只好求助于手动控制。他感叹自己无法解读这个设备，这使得他感觉父亲更加遥远，暗示着他们思维方式上的脱节。

最终，在他鸡肉实验失败后摆弄机器时，他注意到系统中一个黑盒子上的红灯。在拨动一个开关后，灯变成了蓝色，风扇停止了。他意识到这个黑盒子是风扇电源的控制器，而他只是没有把它关掉。然后，他开始成功地弄清楚这个设备的工作原理。

汤姆最后提到他将用它来慢炖猪肉，用于一场纪念午餐，强调了操作父亲创作之物的个人意义。然后，他分享了一个与父亲讨论类似控制问题（特别是比例-积分-微分控制器）的记忆，突出了他们共同的解决问题的思维模式。

---

## 85. 重庆：最大的城市——图片集锦

**原文标题**: Chongqing, the Largest City – In Pictures

**原文链接**: [https://www.theguardian.com/world/gallery/2025/apr/27/chongqing-the-worlds-largest-city-in-pictures](https://www.theguardian.com/world/gallery/2025/apr/27/chongqing-the-worlds-largest-city-in-pictures)

重庆：最大城市掠影
本文“重庆：最大城市掠影”展示了中国重庆的显著转型和蓬勃生机。通过一系列图片和文字说明，文章突出了该市过去20年来的快速经济增长和城市化进程。

重庆的人均GDP大幅增长，城市也已从重工业转型为在汽车和IT领域的优势地位。事实上，重庆生产的汽车比法国和英国的总和还要多，世界上很大一部分笔记本电脑和摩托车都产自这里，这都突显了其工业实力。

文章探讨了重庆的各个方面，从像万象城这样的现代化购物中心、其令人印象深刻的基础设施（包括桥梁和庞大的地铁系统，以及建在公寓楼里的独特李子坝站），到罗汉寺这样的历史地标。来福士广场的观景台可以俯瞰长江和嘉陵江的交汇处。

这些图片还描绘了重庆的日常生活，捕捉了休闲、工作和文化表达的瞬间。从在河边享受烧烤的情侣到利用城市广泛地铁系统的居民，文章描绘了一幅充满活力和不断发展的都市景象。文章还指出，与北京或上海相比，重庆的住房相对负担得起。简而言之，重庆是一座融合了传统与现代、工业与休闲的城市，并提供了对中国城市生活的一种不同的视角。

---

## 86. 裸机printf – 无操作系统下的C标准库

**原文标题**: Bare metal printf – C standard library without OS

**原文链接**: [https://popovicu.com/posts/bare-metal-printf/](https://popovicu.com/posts/bare-metal-printf/)

本文解释了如何使用 Newlib 为裸机系统创建一个紧凑的 C 标准库，并以 RISC-V 作为示例平台。与具有操作系统的典型系统不同，裸机环境缺少 `printf` 等函数的复杂软件抽象。Newlib 作为一个工具包，通过实现诸如 `_write`（将单个字符写入输出流）等基本原语来构建自定义库，从而可以在其上构建更复杂的函数，如 `printf`。

本文还深入探讨了交叉编译，强调了使用为目标架构 (RISC-V) 构建并使用 Newlib 库的工具链的重要性。RISC-V 工具链项目自动执行此过程，创建一个指向正确库的交叉编译器。作者提供了一个包含示例应用程序的 GitHub 存储库。

该示例实现了 UART 原语（`uart_putc`、`uart_getc`），用于基本 I/O。`syscalls.c` 文件实现了 Newlib 所需的系统调用存根，如 `_write`、`_close` 和 `_sbrk`。`_sbrk` 对于内存分配至关重要，它定义了从静态数据段末尾到堆栈的堆空间。 通过实现这些构建块，可以在裸机 RISC-V 系统上实现功能性的 `printf`，展示了 Newlib 如何简化将 C 标准库引入资源受限环境的过程。

---

## 87. 从Playstation到路由器，你可能一直在不知情的情况下使用FreeBSD。

**原文标题**: From Playstation to routers, you've probably been using FreeBSD without knowing

**原文链接**: [https://www.theregister.com/2025/04/28/freebsd_foundation_25/](https://www.theregister.com/2025/04/28/freebsd_foundation_25/)

FreeBSD 的持久影响：开源操作系统及其基金会

文章重点介绍了开源操作系统 FreeBSD 的持久影响以及 FreeBSD 基金会的关键作用。FreeBSD 源于 20 世纪 70 年代 UC Berkeley 的 BSD，优先考虑性能、稳定性和开放式开发。与其他开源项目不同，它在没有中心领导的情况下运行，从而促进了持续的演变和贡献者的可访问性。

成立于 2000 年的 FreeBSD 基金会提供财务、法律和基础设施支持，以确保该项目的长期发展。FreeBSD 宽松的 BSD 许可证使其在各种技术中得到广泛应用，从 PlayStation 游戏机到网络基础设施和云服务。它也是诸如 Jails 和 Capsicum 等安全功能创新的源泉。

FreeBSD 的稳定性和先进的网络功能使其成为关键基础设施的首选，例如 Netflix 的流媒体服务（达到 800 Gbps）和 NetApp 的 ONTAP 软件中都使用了它。Beckhoff Automation 也出于安全原因迁移到了 FreeBSD。

文章还关注了有关开发者社区老龄化的问题，并强调了通过实习、教育材料以及参与 Google Summer of Code 等项目来吸引年轻贡献者的持续努力。来自 Sovereign Tech Fund 的投资将侧重于改善基础设施、安全性和开发者体验。FreeBSD 通过平衡经验丰富的开发者和新鲜视角，不断发展壮大，确保其相关性和创新性。

---

## 88. NASA轨道飞行器发现好奇号火星车正在前往下一个科学考察点的途中

**原文标题**: NASA Orbiter Spots Curiosity Rover Making Tracks to Next Science Stop

**原文链接**: [https://www.nasa.gov/missions/mars-science-laboratory/nasa-orbiter-spots-curiosity-rover-making-tracks-to-next-science-stop/](https://www.nasa.gov/missions/mars-science-laboratory/nasa-orbiter-spots-curiosity-rover-making-tracks-to-next-science-stop/)

2025年2月，美国宇航局的火星勘测轨道飞行器（MRO）拍摄到“好奇号”火星车在火星表面行进的图像，这被认为是首次从轨道上拍摄到火星车行驶中的状态。这张由MRO上的HiRISE相机拍摄的图像显示，“好奇号”是一个小小的黑色斑点，身后留下一条大约1050英尺（320米）长的车辙。这些车辙代表了从2月2日开始，以0.1英里/小时的最高速度行驶了大约11天。

“好奇号”目前正从盖迪兹·瓦利斯海峡前往下一个科学目的地：一个可能由古代地下水形成的具有潜在蜂窝状构造的区域。喷气推进实验室（JPL）的工程师利用HiRISE的图像以及火星车的指令，有效地跟踪和规划“好奇号”的每日行动。JPL“好奇号”规划团队负责人道格·埃里森指出，该图像捕捉到“好奇号”几乎完成了一次69英尺的行驶。虽然HiRISE相机可以拍摄彩色图像，但“好奇号”位于这张特定照片的黑白区域。火星车此后已经爬上图像中可见的陡峭斜坡，预计将在一个月内到达其新的科学地点。

---

## 89. HTTP Feeds: 通过HTTP轮询事件的最小化规范

**原文标题**: HTTP Feeds: a minimal specification for polling events over HTTP

**原文链接**: [https://www.http-feeds.org/](https://www.http-feeds.org/)

HTTP Feeds: 使用 HTTP API 实现异步事件流和数据复制，无需 Kafka 等消息中间件。HTTP Feed 提供一个 GET 端点，返回按时间顺序排列的 CloudEvents 批量格式（application/cloudevents-batch+json）序列化事件。

关键特性包括使用 `lastEventId` 查询参数进行分页，允许客户端滚动浏览 Feed，并通过无限轮询支持实时订阅。客户端轮询端点，持久化 `lastEventId` 以检索后续事件，确保至少一次交付。

该规范概述了简单轮询（客户端在处理完之前的事件后持续请求新事件）和长轮询（服务器保持连接打开，直到有新事件可用或发生超时）。

HTTP Feeds 可用于发布不可变的领域事件或为数据集合（聚合）提供 API。聚合 Feed 必须至少包含每个聚合一次，并实现压缩（删除同一主题的过时条目）以减小 Feed 大小，以及通过 DELETE 方法发出的删除信号，向消费者指示主题的删除。

该规范详细说明了 CloudEvents 负载中的必需和可选字段，包括 `specversion`、`id`、`type`、`source`、`time`、`subject` (用于聚合 Feed)、`method`、`datacontenttype` 和 `data`。可以使用标准 HTTP 身份验证方案实现身份验证。

---

## 90. Show HN: Logchef – ClickHouse 的模式无关日志查看器

**原文标题**: Show HN: Logchef – Schema-agnostic log viewer for ClickHouse

**原文链接**: [https://github.com/mr-karan/logchef](https://github.com/mr-karan/logchef)

Logchef：为ClickHouse构建的高性能、无模式日志分析平台。专为高效日志管理和分析而设计，它以单个二进制文件形式提供，简化了部署和管理。其主要特点是能够查询任何ClickHouse表，而无需预定义模式，从而提供了日志探索的灵活性。

Logchef提供简单的搜索语法和完整的ClickHouse SQL支持，以满足不同的查询需求。性能是首要考虑因素，它能够以最少的资源对大型数据集进行快速查询。它还包括基于团队的访问控制，具有细粒度的权限，可实现安全的多租户日志访问。

该平台可以使用Docker轻松部署，并提供相关说明。文档可在logchef.app上找到，提供设置指南、配置详细信息和API参考。Logchef在AGPLv3许可下发布。同时提供演示版本，供立即评估。

---

## 91. 如何让ChatGPT不再过度奉承迎合

**原文标题**: Here's how to get ChatGPT to stop being an overly flattering yes man

**原文链接**: [https://old.reddit.com/r/ChatGPT/comments/1k8vomo/heres_how_to_get_chatgpt_to_stop_being_an_overly/](https://old.reddit.com/r/ChatGPT/comments/1k8vomo/heres_how_to_get_chatgpt_to_stop_being_an_overly/)

无法访问文章链接。

---

## 92. Ucbvax (1994) 的逝去

**原文标题**: The Passing of Ucbvax (1994)

**原文链接**: [http://ucbvax.berkeley.edu/passing-of-ucbvax.txt](http://ucbvax.berkeley.edu/passing-of-ucbvax.txt)

本文宣布在为加州大学伯克利分校计算机科学系服务多年后，计算机“ucbvax.berkeley.edu”于1994年8月19日退役。举行了一个小型仪式来纪念这一时刻，程序员和网络工作人员参加了仪式。Keith Sklower 简要介绍了 ucbvax 的历史，概述了其起源：它是校园里的第一台 VAX 计算机，于 1978 年通过 NSF 拨款获得。最初用于通用计算，后来专门用于处理电子邮件和 Netnews，成为 ARPANET 和校园之间的重要网关。

Eric Allman 发表了一篇幽默的悼词，引用了《哈姆雷特》，哀叹失去了该机器的电子邮件路由、拨号服务和网络监控功能。首次启动该机器的 Kirk McKusick 荣幸地关闭了它。尽管 ucbvax 已退役，但它被重新用于为加州大学警察局提供卡键访问系统控制器。

由于需要将排队的电子邮件迁移到另一台机器，关闭工作被推迟。虽然物理 ucbvax 已退役且其 IP 地址已停用，但 ucbvax 名称继续存在于电子邮件流量中，被重新路由到“nak.berkeley.edu”，这是一台由大学 IT 部门支持的服务器，文章指出这具有讽刺意味。

---

## 93. CosAE：用于图像恢复的可学习傅里叶级数

**原文标题**: CosAE: Learnable Fourier Series for Image Restoration

**原文链接**: [https://sifeiliu.net/CosAE-page/](https://sifeiliu.net/CosAE-page/)

本文介绍了一种新型自编码器 CosAE（余弦自编码器），专为图像修复任务设计。与传统自编码器因瓶颈层分辨率降低而常丢失细节不同，CosAE 利用傅里叶级数表示图像。它将图像编码为一系列二维余弦波，每个余弦波由可学习的频率和傅里叶系数（幅度和相位）定义。这使得瓶颈层能够实现显著的空间压缩（例如，64 倍下采样），而不会在解码过程中牺牲关键图像细节。

CosAE 的核心创新在于其瓶颈层中频率系数的编码，与传统的基于像素的编码相比，提供了一种更高效、更详细的表示。这使得 CosAE 特别适合需要精细细节恢复的任务。

作者通过在灵活分辨率超分辨率和盲图像修复这两个具有挑战性的任务上的实验，证明了 CosAE 的有效性，这两个任务需要推广到复杂和未知的图像退化。结果表明，CosAE 在这些任务中优于最先进的方法，突出了其学习图像修复问题通用表示的能力。本质上，CosAE 基于傅里叶的编码使其即使在高度压缩的瓶颈表示下也能保持详细的图像信息，从而在具有挑战性的图像修复场景中提高了性能。

---

## 94. 纪念：科幻与美术艺术家大卫·施莱因科费尔

**原文标题**: In Memoriam: SF and Fine Artist David Schleinkofer

**原文链接**: [https://downthetubes.net/in-memoriam-sf-and-fine-artist-david-schleinkofer/](https://downthetubes.net/in-memoriam-sf-and-fine-artist-david-schleinkofer/)

美国科幻与美术艺术家大卫·施莱因科弗逝世讣告

本文是关于美国科幻与美术艺术家大卫·施莱因科弗的讣告。他在与肌萎缩侧索硬化症（卢伽雷氏症）抗争后，于2025年4月20日逝世。施莱因科弗是一位拥有超过40年从业经验的职业艺术家和插画家，以其独特的喷枪风格和对科幻艺术的重大贡献而闻名，尤其是在20世纪70年代和80年代。

他的著名作品包括《明日及未来：科幻杰作》的封面艺术，艺术家鲍勃·埃格尔顿认为这对他后来的科幻艺术合集（如光谱）产生了重大影响。 施莱因科弗的艺术作品也出现在《科学文摘》杂志和菲利普·K·迪克和哈里·图特尔道夫等作家的众多科幻平装本封面上。

除了书籍封面外，施莱因科弗的商业艺术还扩展到百利甜酒和李维斯等主要品牌的广告，以及孩之宝的变形金刚玩具、美泰的风火轮故事书和绝对零度和模拟城市等电脑游戏的艺术作品。他还为《太空堡垒卡拉狄加》和《超时空要塞》等系列创作了封面艺术。脸书上的《超时空要塞》小说小组赞扬了他的引人注目和具有挑衅性的艺术。

晚年，施莱因科弗将重心转向美术，创作风景画、海洋画和肖像画，在画廊展出作品并出售给世界各地的收藏家。他还继续接受委托创作平装本书籍封面，包括苏·亨利谋杀之谜系列。

---

## 95. 静默缺陷很重要：编译器引入的安全漏洞研究

**原文标题**: Silent Bugs Matter: A Study of Compiler-Introduced Security Bugs

**原文链接**: [https://www.usenix.org/conference/usenixsecurity23/presentation/xu-jianhao](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-jianhao)

本文研究了编译器引入的安全漏洞 (CISB)，强调了即使“正确”的编译器，尽管确保了与源代码的语义等价性，也可能引入安全漏洞。作者认为，期望用户完全理解编译器假设和语言规范，尤其是在未定义行为方面，是不现实的，并且是 CISB 的一个重要来源。

该研究对 GCC 和 Clang 的 4,827 份错误报告进行了全面分析，从而形成了 CISB 分类法。一项用户研究进一步探讨了编译器用户如何看待编译器行为，揭示了 CISB 很常见，并且可能具有严重的安全影响。

主要发现是，依赖“无未定义行为”等假设给用户带来了重大挑战，也是 CISB 的主要原因。本文强调，这些漏洞是真实且具有影响力的，需要认真考虑，即使修复它们的责任在编译器开发者和用户之间存在争议。作者提倡更深入地理解和更好地处理 CISB，以提高软件安全性。

---

## 96. 我的梦之谷：硅谷为何将波士顿128号公路抛在身后 (2009)

**原文标题**: The Valley of My Dreams: Why Silicon Valley Left Boston's Route 128 in the Dust (2009)

**原文链接**: [https://techcrunch.com/2009/10/31/the-valley-of-my-dreams-why-silicon-valley-left-bostons-route-128-in-the-dust/](https://techcrunch.com/2009/10/31/the-valley-of-my-dreams-why-silicon-valley-left-bostons-route-128-in-the-dust/)

在《我的梦想之谷：硅谷为何将波士顿128号公路甩在身后》一书中，Vivek Wadhwa 探讨了硅谷作为全球科技中心，其优势超越波士顿128号公路的原因。Wadhwa 将他在充满活力、互联互通的硅谷的经历，与相对不那么活跃的128号公路环境进行了对比，突出了创业生态系统的差异。

他用同一晚被邀请参加三个重要活动的经历作为一个轶事，来说明硅谷独有的普遍且重叠的网络。 Wadhwa 深入探讨了这些网络的开放和包容性，并以 TiE（印度企业家协会）演变成一个更国际化的组织为例。

文章随后讨论了曾经被认为是领先科技中心的128号公路是如何落后的。 Wadhwa 引用 AnnaLee Saxenian 的研究解释说，硅谷培养了一种开放的信息交流、风险承担和集体学习的文化，而128号公路则由大型、保密的公司主导，扼杀了创新。硅谷的风险投资家更深入地扎根于本地网络，大学也与初创企业建立了更广泛的合作关系。

由于其灵活性和创新精神，硅谷成功地完成了从小型计算机到个人计算机的转变，而128号公路则滞后了。 尽管波士顿在研究和生物技术等一些领域仍然很强大，但硅谷仍然是明显的领导者，吸引着渴望拥抱其充满活力的文化和强大的网络效应的企业家和工程师。

---

## 97. 特斯拉的状况比你想象的更糟

**原文标题**: Tesla is in worse shape than you think

**原文链接**: [https://www.cnn.com/2025/04/28/business/things-at-tesla-are-worse-than-they-appear/index.html](https://www.cnn.com/2025/04/28/business/things-at-tesla-are-worse-than-they-appear/index.html)

这篇CNN文章描绘了特斯拉目前令人担忧的财务状况，表明该公司的状况比许多人意识到的还要糟糕。虽然首席执行官埃隆·马斯克淡化了问题的严重性，但该文章强调了几个关键问题。

特斯拉的净利润暴跌，该公司仅在上个季度因出售监管积分而实现盈利。这些积分是重要的收入来源，但受到特朗普政府潜在政策变化的威胁。销量下降，原因是竞争加剧，尤其是在中国，以及对马斯克政治观点的强烈反对，这些都在加剧这一问题。该公司即将失去其作为全球领先电动汽车销售商的地位，被比亚迪超越。

此外，特斯拉的利润率正在萎缩，达到2012年以来的最低水平。虽然之前是美国利润最高的汽车制造商，但特斯拉现在正努力仅靠汽车销售来维持盈利能力。

尽管面临这些挑战，马斯克仍表示乐观，并将公司的未来寄托在自动驾驶出租车和人形机器人上。然而，该文章指出，之前关于自动驾驶技术的承诺一再落空，而且竞争对手已经因为盈利方面的担忧而缩减了自动驾驶出租车的雄心。文章总结说，虽然一些分析师仍然对特斯拉的长期前景抱有希望，但其未来仍然存在重大障碍和悬而未决的问题。

---

## 98. 弹簧天线偶极子 (2021)

**原文标题**: Slinky-Coil Dipole (2021)

**原文链接**: [https://nonstopsystems.com/radio/frank_radio_antenna.htm](https://nonstopsystems.com/radio/frank_radio_antenna.htm)

F. Dörenberg的本网页讨论了“弹簧天线偶极子”，这是一种使用弹簧玩具（柔性金属弹簧）制成的紧凑型天线。它探讨了其构造、调谐、性能以及在便携式或空间受限应用中的适用性。

要点：

*   **简介：** 作者描述了标准弹簧线圈（钢或黄铜）的物理特性、其感应负载以及其作为天线的潜力。它承认这是一种折衷的天线，而不是“奇迹”。
*   **构造：** 作者详细介绍了构建弹簧偶极子所需的组件，包括弹簧线圈、用于中心绝缘子的PVC、吊环螺栓、电线和支撑绳。他提供了有关如何组装天线的说明和图像。
*   **调谐：** 该页面探讨了通过调整线圈间距（拉伸）或短路匝数来调谐弹簧偶极子，并参考了一项美国可调谐螺旋偶极子专利。
*   **性能：** 作者分享了使用钢和黄铜弹簧偶极子的经验。他提到使用钢偶极子成功进行了通信，甚至是从室内公寓。他还提供了黄铜偶极子安装的驻波比测量结果，显示了谐振点。
*   **其他人的制作：** 该网页重点介绍了其他人的弹簧天线项目，引用了相关的出版物和项目，包括一个俱乐部将其用于野外日活动。

总而言之，这篇文章将弹簧天线偶极子作为一种可行但折衷的天线解决方案呈现给业余无线电操作员，尤其是在空间有限的情况下。它强调了易于构造，并提供了有关其使用的实用见解。

---

## 99. 纽约考虑采取行动关闭特斯拉经销店，挑战马斯克

**原文标题**: Taking on Musk, New York Considers Move to Close Tesla Dealerships

**原文链接**: [https://www.nytimes.com/2025/04/27/nyregion/new-york-tesla-dealerships-doge.html](https://www.nytimes.com/2025/04/27/nyregion/new-york-tesla-dealerships-doge.html)

纽约州参议员帕特里夏·法伊此前曾支持特斯拉在该州开设经销店，但现在正带头推动撤销一项允许特斯拉直接运营自己的经销店的立法豁免，从而绕过其他汽车制造商所需的传统特许经营模式。她改变主意的原因是她不赞成埃隆·马斯克参与特朗普政府事务，并认为他的行为与纽约州的绿色能源目标相悖。

法伊认为，马斯克正在与一个正在拆除电动汽车基础设施资金并阻碍气候变化倡议的政府合作。她认为，授予特斯拉直接销售的垄断权与这些目标背道而驰。

法伊的反对不仅限于立法行动，她还积极参与了反对计划中的特斯拉经销店的示威活动。她的行动反映了更广泛的全国性抗议特朗普和马斯克的运动，其中包括对特斯拉设施的破坏和逮捕。

---

## 100. 关于盗版网站LibGen的批判性书目

**原文标题**: A critical bibliography about the pirate site LibGen

**原文链接**: [https://eve.gd/2025/03/21/a-critical-bibliography-about-libgen-the-pirate-site-that-meta-used-for-ai-training/](https://eve.gd/2025/03/21/a-critical-bibliography-about-libgen-the-pirate-site-that-meta-used-for-ai-training/)

马丁·保罗·伊夫的这篇文章提供了一份关于LibGen和Sci-Hub的学术文献的批判性书目，起因是主流媒体（通过《大西洋》）最近对Meta利用LibGen数据进行人工智能训练的关注。作者对学术界对这些平台的认知滞后表示惊讶，因为已经存在大量关于它们的学术研究。

伊夫指出了LibGen和Sci-Hub的意识形态基础，指出它们的创始人通常认为自己是在提供公平的知识获取途径，其动力来自于社会主义或共产主义原则。然而，这也意味着他们的资源对包括Meta在内的任何人都开放，从而引发了伦理方面的考量。

文章随后提供了一份关于LibGen和Sci-Hub各个方面的学术著作的精选清单。该书目涵盖了这些“盗版”平台的历史、运营、使用、法律斗争和伦理影响。所列作品探讨的关键主题包括：学术盗版的理由、Sci-Hub的下载分析、Sci-Hub在开放获取中的作用、与俄罗斯情报部门有关的指控以及对学术出版商的经济影响。该清单包括学术文章和博客文章。

伊夫强调了书目中的两个条目特别具有洞察力：Bodó关于Library Genesis起源的文章，以及伊夫自己关于盗版电子书平台极简主义扩展的作品。他还提到了Lance Eaton即将发表的关于学术盗版的作品。

---

