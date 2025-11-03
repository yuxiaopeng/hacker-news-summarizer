# Hacker News 热门文章摘要 (2025-11-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们为什么从Python迁移到Node.js

**原文标题**: Why We Migrated from Python to Node.js

**原文链接**: [https://blog.yakkomajuri.com/blog/python-to-node](https://blog.yakkomajuri.com/blog/python-to-node)

Skald上线一周后，将其后端从Python (Django) 重写为 Node.js (Express + MikroORM)，尽管通常建议优先关注产品与市场的契合度，但他们优先考虑了可扩展性。 主要原因是Django中Python的异步能力难以满足需求，对于处理其RAG API平台所需的众多对LLM和嵌入服务的异步API调用来说，它显得笨重且不直观。

作者对Node.js中的异步操作经验丰富，认为Python的异步支持是“打补丁”式的添加，而非核心功能，这导致了复杂性和性能瓶颈。 他们探索了FastAPI等替代方案，但最终选择了Node.js来统一代码库，因为他们的后台工作服务已经用Node.js编写。

迁移后，吞吐量提高了约3倍，并实现了并发处理的能力。 虽然他们怀念Django的易用性和ORM，但他们获得了统一代码库、更好的测试以及对MikroORM的熟悉等好处。 他们承认失去了Python生态系统的丰富性，尤其是在机器学习方面，但接受了这种权衡，以换取效率和可维护性的即时提升。 他们愿意接受对其决定的任何批评，只要能让他们更多地了解Python的异步能力。 他们得出结论，重写是有益且是一次学习经验，并分享了pull request的链接以供审查。

---

## 2. Learning to read Arthur Whitney's C to become Smart (2024)

**原文标题**: Learning to read Arthur Whitney's C to become Smart (2024)

**原文链接**: [https://needleful.net/blog/2024/01/arthur_whitney.html](https://needleful.net/blog/2024/01/arthur_whitney.html)

生成摘要时出错

---

## 3. 社交媒体戒断月

**原文标题**: No Socials November

**原文链接**: [https://bjhess.com/posts/no-socials-november](https://bjhess.com/posts/no-socials-november)

生成摘要时出错

---

## 4. Vim图

**原文标题**: VimGraph

**原文链接**: [https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/](https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/)

生成摘要时出错

---

## 5. 反对PGVector 的理由

**原文标题**: The Case Against PGVector

**原文链接**: [https://alex-jacobs.com/posts/the-case-against-pgvector/](https://alex-jacobs.com/posts/the-case-against-pgvector/)

生成摘要时出错

---

## 6. Linux内核的WebAssembly (WASM) 架构支持

**原文标题**: WebAssembly (WASM) arch support for the Linux kernel

**原文链接**: [https://github.com/joelseverin/linux-wasm](https://github.com/joelseverin/linux-wasm)

本文档描述了一个项目，该项目提供脚本以在 WebAssembly (Wasm) 上构建和运行 Linux 系统。该项目利用了几个软件组件：LLVM（已针对 GNU ld 样式链接器脚本进行了修补）、Linux 内核（已针对 Wasm 架构支持、binfmt 和 Web 控制台驱动程序进行了修补）、musl libc（已针对 Wasm 目标支持进行了修补）、BusyBox（已针对 clang/wasm-ld 兼容性和 Wasm 默认配置进行了修补）、一个最小的 initramfs 和一个运行时（基于 JavaScript 的 Wasm 主机示例）。

构建过程包括下载和修补这些组件，然后使用 clang 和 wasm-ld 编译它们。主要挑战包括 musl 不完整的 Wasm 支持，以及 Linux 内核构建系统中的限制，这些限制需要用于交叉编译器安装的无空格路径。生成的系统是一个 Linux 内核，可以在 Wasm 环境中将 .wasm 文件作为可执行文件执行。

该文档提供了在主机上或 Docker 容器中直接运行构建脚本的说明。提供了两种 Docker 容器配置：`linux-wasm-base`（一个具有必要工具的开发环境）和 `linux-wasm-contained`（用于隔离构建）。提供的 `linux-wasm.sh` 脚本管理下载和构建，并提供用于选择性重建组件的选项。运行时提供示例 JavaScript 代码来启动 Wasm 环境并与内核交互。

该文档还强调了由于 Wasm 缺乏 MMU，因此需要在 NOMMU 配置中构建 Linux，并建议对 Wasm 程序使用 `-fPIC/-shared` 或 syscalls 代理，同时指出共享内存和内存保护之间的权衡。

---

## 7. 罗伯特·胡克致戈特弗里德·莱布尼茨的“赛博朋克”信件

**原文标题**: Robert Hooke's "Cyberpunk” Letter to Gottfried Leibniz

**原文链接**: [https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/](https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/)

This article explores Robert Hooke's 1681 letter to Gottfried Leibniz, arguing it embodies a "cyberpunk" sensibility centuries before the genre existed. The author, who discovered the letter in the Royal Society archives, finds it significant because it demonstrates Hooke's engagement with Leibniz's "Characteristica Universalis," a project to create a universal language for science capable of mechanizing reasoning. This idea, which Norbert Wiener saw as a precursor to cybernetics, is framed as a proto-computer programming language.

The article posits that Hooke's letter goes beyond mere cybernetics. While Leibniz envisioned a system for rational thought, Hooke foresaw the potential for this language to empower individuals and bypass restrictive authorities. He hoped a universally accessible system of thought would allow for the free exploration and testing of ideas without censorship, a key element of cyberpunk's do-it-yourself ethos.

The author connects Hooke's life experiences – a politically charged upbringing, a penchant for hands-on tinkering, and clashes with authority – to this vision. They argue that Hooke's belief in the liberating potential of mechanized reasoning, particularly in challenging established power structures, aligns him with the core tenets of cyberpunk. Therefore, the article proposes that, just as Wiener is considered the patron saint of cybernetics, Hooke should be considered the patron saint of cyberpunk.


---

## 8. 具名颜色所覆盖的RGB空间可视化

**原文标题**: A visualization of the RGB space covered by named colors

**原文链接**: [https://codepen.io/meodai/full/zdgXJj/](https://codepen.io/meodai/full/zdgXJj/)

无法访问文章链接。

---

## 9. Skyfall-GS：从卫星图像合成沉浸式3D城市场景

**原文标题**: Skyfall-GS – Synthesizing Immersive 3D Urban Scenes from Satellite Imagery

**原文链接**: [https://skyfall-gs.jayinnn.dev/](https://skyfall-gs.jayinnn.dev/)

Skyfall-GS：一种生成大规模、可探索、几何精确的三维城市场景的新框架，无需依赖昂贵的3D扫描进行训练。它认识到现有方法因高质量3D数据稀缺而存在的局限性，利用易于获取的卫星图像进行粗略几何建模，并利用开放域扩散模型生成高质量纹理。

其核心创新在于协同这两种数据源，以创建城市街区尺度上的逼真三维环境，从而实现实时的沉浸式探索。Skyfall-GS采用课程驱动的迭代优化策略。这种渐进式方法增强了生成场景的几何完整性和照片级真实纹理，从而产生更高质量的输出。

本质上，Skyfall-GS通过绕过对大量3D标注的需求，解决了创建大规模3D城市环境的挑战。相反，它巧妙地将易于获取的卫星图像与扩散模型相结合，以实现逼真且可探索的3D世界。结果表明，与其他方法相比，不同视角的几何一致性更好，纹理也更逼真。

---

## 10. 为什么Nextcloud用起来感觉很慢

**原文标题**: Why Nextcloud feels slow to use

**原文链接**: [https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/](https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/)

本文探讨了作者对Nextcloud性能的不满，特别是其加载速度缓慢的问题，即使在配置不错的硬件上也是如此。作者认为这种缓慢的根源在于需要下载和执行过多的JavaScript，通常每个页面加载都需要15-20MB，即使压缩后仍有4-5MB，对于一个Web应用程序来说，这还是太多了。

作者指出了导致这种臃肿的具体JavaScript包，例如`core-common.js`、`NotificationsApp.chunk.mjs`，以及Calendar、Files和Notes等应用程序的大型特定JavaScript。他提供了这些应用程序在较慢的连接上加载所需时间的示例，突出了糟糕的用户体验。他举例说明了Tasks应用程序在iPhone上需要5-10秒才能加载。

作者怀疑Nextcloud的架构，及其通过通用库强调统一体验的方式，是根本原因。他认为功能与包大小的比例失调。

为了解决这个问题，作者已经开始用更轻量级的替代品替换一些Nextcloud应用程序，例如用Vikunja处理任务，用Immich处理照片，欣赏它们显著更小的JavaScript体积和更高的速度。虽然作者承认Nextcloud的功能集对其他功能很方便，但他仍然对其性能不满意。

作者承认造成这种情况的潜在原因，例如开发团队工作量过大，但他强调了这对用户体验和可访问性的负面影响。他最后推荐了Alex Russell关于Web性能的研究，以及在开发过程中考虑这些因素的重要性。

---

## 11. 持续学习问题

**原文标题**: The Continual Learning Problem

**原文链接**: [https://jessylin.com/2025/10/20/continual-learning/](https://jessylin.com/2025/10/20/continual-learning/)

本文探讨了持续学习的挑战，即模型在不断从新经验中学习而不忘记先前知识的能力。作者指出了两个关键的子问题：**泛化**（从数据中学习重要的部分，这些部分可以应用于各种未来的环境中）和**整合**（整合新的信息而不灾难性地遗忘旧的知识）。

作者提出“记忆层”作为一种潜在的解决方案，认为它们在有针对性的更新、高容量和自适应整合之间取得了良好的平衡。记忆层用一种稀疏的注意力机制取代了前馈网络，该机制在学习到的记忆池中查找信息。这允许有针对性的更新，因为每个输入只激活一小部分记忆槽。

本文将记忆层与其他方法进行了对比，如上下文学习 (ICL)、检索增强生成 (RAG)、全量微调以及参数高效微调 (PEFT) 方法（如 LoRA 和适配器）。ICL 存在上下文腐烂的问题，RAG 不能压缩知识，全量微调会导致遗忘，而 PEFT 方法通常缺乏容量。记忆层旨在解决这些替代方案的局限性。

作者的研究“通过稀疏记忆微调实现持续学习”表明，在持续学习场景中，微调记忆层比全量微调和 LoRA 更有效，从而在学习新事实时显著减少遗忘。该方法使用基于 TF-IDF 的方法选择性地微调与新数据最相关的记忆槽，确保有针对性的更新并防止灾难性遗忘。这项研究的动机是希望推动模型朝着“始终在训练”和持续改进的方向发展。

---

## 12. 线性代数图解入门，第二章：点积

**原文标题**: An Illustrated Introduction to Linear Algebra, Chapter 2: The Dot Product

**原文链接**: [https://www.ducktyped.org/p/linear-algebra-chapter-2-the-dot](https://www.ducktyped.org/p/linear-algebra-chapter-2-the-dot)

生成摘要时出错

---

## 13. 2025年终端模拟器现状：失落的霸主

**原文标题**: State of Terminal Emulators in 2025: The Errant Champions

**原文链接**: [https://www.jeffquast.com/post/state-of-terminal-emulation-2025/](https://www.jeffquast.com/post/state-of-terminal-emulation-2025/)

This article, a follow-up to a 2023 piece on Unicode support in terminal emulators, reports on the state of terminal emulators in 2025, using the updated `ucs-detect` tool to assess support for DEC Private Modes, sixel graphics, and pixel size. The primary challenge remains accurately mapping diverse Unicode scripts onto fixed-width grids.

Ghostty, developed by Mitchell Hashimoto, emerges as a frontrunner due to its strong Unicode support, built from scratch in Zig, and its accompanying `libghostty` library. Kitty, by Kovid Goyal, also performs exceptionally well, further validated by Goyal's text-splitting algorithm closely mirroring the Python `wcwidth` specification. Both Ghostty and Kitty correctly support Variation Selector 15.

The article highlights performance issues in iTerm2, Extraterm, and GNOME Terminal (and its VTE-based derivatives), which exhibited significant slowdowns during testing. Conversely, Python `wcwidth`, optimized with an LRU cache, performed surprisingly well.

The article also discusses quirks observed in Terminology, iTerm2, and Konsole, relating to handling of DEC Private Modes, noting that they often report inconsistent or incorrect support.  Improvements in `libvte` are noted as a positive sign for future language support.

Finally, the article examines the potential of the new text sizing protocol to address limitations in fixed-width terminal displays, potentially leading to improved legibility and accessibility for diverse languages, giving Khün as an example of where variable text sizing shows promise.


---

## 14. 离线数学：使用MathJax将LaTeX转换为SVG

**原文标题**: Offline Math: Converting LaTeX to SVG with MathJax

**原文链接**: [https://sigwait.org/~alex/blog/2025/10/07/3t8acq.html](https://sigwait.org/~alex/blog/2025/10/07/3t8acq.html)

离线渲染 LaTeX 数学公式的解决方案：HTML 文档中的 SVG 嵌入

---

## 15. 2003年关于安圭拉的链接集合

**原文标题**: A collection of links that existed about Anguilla as of 2003

**原文链接**: [https://web.ai/](https://web.ai/)

生成摘要时出错

---

## 16. 展示HN：我厌倦了浪费工程师的时间在筛选电话上，所以我做了Niju

**原文标题**: Show HN: I was tired of wasting engineer time on screening calls so I built Niju

**原文链接**: [https://niju.dev](https://niju.dev)

Niju是一个旨在简化技术筛选的平台，它用一个20分钟的异步编程挑战取代了冗长而低效的筛选电话。其目标是节省工程师的时间，降低筛选成本，并加速招聘流程。

Niju的主要功能包括低压力的录制编程会话、浏览器内代码编辑器、屏幕/摄像头/音频录制、完整的面试记录以及AI驱动的代码质量和全面评估。这使得对候选人的实际编程能力、解决问题的能力和沟通风格进行更客观和公正的评估。

该平台解决了耗时的筛选电话、面试官之间评估不一致以及糟糕的候选人体验等问题。通过使用人工智能分析候选人的代码、音频和思考过程，Niju提供了一份全面的报告，使招聘人员和工程师能够在短短5分钟内做出更明智的决策，而传统方式需要45-75分钟。

Niju旨在测试真实的编码流畅性，而不是抽象的难题，从而更好地预测在职成功率并提高offer接受率。该过程包括定义职位空缺，通过唯一的链接邀请候选人参加20分钟的挑战，然后分析AI驱动的报告。Niju提供简单透明的定价，并提供首次面试免费的特别 introductory offer。

---

## 17. Show HN: FinBodhi – 本地优先的双式记账应用/PWA，伴你财务旅程

**原文标题**: Show HN: FinBodhi – Local-first, double-entry app/PWA for your financial journey

**原文链接**: [https://finbodhi.com/](https://finbodhi.com/)

FinBodhi是一款本地优先的双式记账应用和渐进式Web应用(PWA)，旨在帮助用户管理其财务旅程。“本地优先”意味着该应用优先考虑离线功能和用户设备上的数据存储，从而增强隐私和性能。“双式记账”表明该应用采用严谨的会计系统，与简单的预算工具相比，可能提供更准确、更全面的财务跟踪。这表明该应用侧重于提供更专业或更深入的财务管理体验。PWA则意味着跨平台兼容性和可安装性，如同原生应用，为用户提供在不同设备上无缝体验的可能性。该应用的总体目的是使个人能够使用强大的会计方法有效地、私密地管理和跟踪他们的财务。

---

## 18. 展示HN：一个可以在任何GPU上运行的Rust光线追踪器 – 甚至在浏览器中

**原文标题**: Show HN: a Rust ray tracer that runs on any GPU – even in the browser

**原文链接**: [https://github.com/tchauffi/rust-rasterizer](https://github.com/tchauffi/rust-rasterizer)

生成摘要时出错

---

## 19. 养殖海鲜的问题

**原文标题**: The Problem with Farmed Seafood

**原文链接**: [https://nautil.us/the-problem-with-farmed-seafood-1243674/](https://nautil.us/the-problem-with-farmed-seafood-1243674/)

John Steele's "The Problem with Farmed Seafood" highlights the unsustainable practice of feeding farmed fish with wild-caught forage fish like anchoveta, sardines, and menhaden. This "forage fish bottleneck" threatens both marine ecosystems and global food security. The overfishing of these small fish depletes the ocean's foundation, impacting seabirds, marine mammals, and the overall health of the ocean.

The article introduces the F3 Challenge, a competition designed to incentivize the aquaculture industry to develop marine-animal-free food for farmed fish. This initiative seeks to future-proof farm operations and reduce reliance on dwindling wild fish stocks. The premise is revolutionary: fish need nutrients, not necessarily other fish, to thrive.

The article celebrates successful breakthroughs achieved through the F3 Challenge. Companies have created plant-based feeds, algae-derived omega-3 fatty acids, and insect-based protein meals to replace fishmeal, thereby sparing billions of forage fish. These solutions offer alternative sources of nutrition that are both sustainable and scalable.

The article also emphasizes the potential for a cultural shift, envisioning seafood labels proclaiming "fish-free feed" to promote sustainable aquaculture practices. The author concludes that by embracing innovative feed solutions, aquaculture can contribute to a healthier ocean, enhanced food security, and even help mitigate climate change.


---

## 20. Python Steering Council unanimously accepts "PEP 810, Explicit lazy imports"

**原文标题**: Python Steering Council unanimously accepts "PEP 810, Explicit lazy imports"

**原文链接**: [https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131?page=23](https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131?page=23)

本文片段展示了如何使用Python中的`sys.modules`来验证“PEP 810，显式惰性导入”中提出的惰性加载行为。 关键在于，`惰性导入`不会立即使用导入的模块填充`sys.modules`。 这与常规`import`形成对比，后者在导入时会将模块添加到`sys.modules`。

该示例表明，在使用`lazy import email`之后，访问`sys.modules['email']`最初会引发`KeyError`。 这证实了该模块尚未加载并在`sys.modules`中注册。 只有在实际使用该模块（通过直接引用`email`）之后，它才会被加载到内存中并添加到`sys.modules`。 随后，访问`sys.modules['email']`会检索已加载的模块对象。

该片段建议在单元测试中使用此行为（可能在子进程中）来确认惰性导入是否按预期工作，以及模块是否仅在需要时才加载。 这是PEP 810的一个关键方面，旨在通过延迟模块加载直到绝对必要时来缩短启动时间。

---

## 21. 在互联网规模上测量TCP连接的特性

**原文标题**: Measuring characteristics of TCP connections at Internet scale

**原文链接**: [https://blog.cloudflare.com/measuring-network-connections-at-scale/](https://blog.cloudflare.com/measuring-network-connections-at-scale/)

生成摘要时出错

---

## 22. Open WebUI的OSS替代方案 - 类似ChatGPT的UI、API和CLI

**原文标题**: OSS Alternative to Open WebUI – ChatGPT-Like UI, API and CLI

**原文链接**: [https://github.com/ServiceStack/llms](https://github.com/ServiceStack/llms)

llms.py 是一款轻量级、离线优先、开源的 Open WebUI 替代方案，提供类似 ChatGPT 的用户界面、API 和 CLI，用于与多个大型语言模型 (LLM) 交互。 它通过将所有内容存储在浏览器存储中来优先考虑数据隐私。 它支持多种提供商（OpenRouter、Ollama、Anthropic、Google、OpenAI、Grok、Qwen、Z.ai、Mistral），并允许用户混合使用本地和远程模型，根据定义的顺序自动将请求路由到可用的提供商，并在失败时重试。

主要功能包括：单文件 Python 实现、OpenAI 兼容的 API、内置分析、可选的 GitHub OAuth 以及简单的配置管理。 它提供了一个 CLI 用于快速交互，以及一个服务器模式用于运行 OpenAI 兼容的 HTTP 服务器。 该系统通过支持视觉/音频的模型处理图像和音频，提供可自定义的聊天模板，并具有自动 Ollama 模型发现功能。

本文详细介绍了通过 pip 或 Docker 安装、设置 API 密钥、启用/禁用提供商，并提供了运行 UI 和 API 服务器的说明。 它涵盖了命令行用法，并提供了文本、图像、音频和文件请求的示例，展示了特定于模型的指令和自定义聊天模板。 它解释了服务器模式的用法，并提供了 `curl` 示例，还提供了高级选项，例如自定义配置文件和详细日志记录。 它还提到了自动配置更新和 OAuth 设置以提高安全性。

---

## 23. 使用 Rust 编写 Asciidoc 解析器：Asciidocr

**原文标题**: Writing an Asciidoc Parser in Rust: Asciidocr

**原文链接**: [https://www.bikesbooksandbullshit.com/bullshit/2025/01/08/writing-an-asciidoc-parser-in-rust.html](https://www.bikesbooksandbullshit.com/bullshit/2025/01/08/writing-an-asciidoc-parser-in-rust.html)

作者详细描述了其创建 `asciidocr` 的历程，这是一个用 Rust 编写的 Asciidoc 解析器。 由于对现有的 Asciidoc 转换器不满意，尤其是基于 Ruby 的 Asciidoctor，因为它属于解释型语言且 Ruby 存在固有局限性，作者便着手构建一个基于 Rust 的解决方案。

受 "Crafting Interpreters" 一书的启发，作者选择了手写解析器，而不是使用像 `pest` 这样的词法分析包，目的是为了更好地理解和潜在的性能优势。 过程包括将 Asciidoc 文档扫描成 tokens，将这些 tokens 解析成抽象语法图，然后使用该图进行输出。

扫描阶段涉及创建 `TokenType` 枚举和 `Token` 结构体，处理诸如 Unicode 字符和 emojis 的字符边界等复杂问题。 作为迭代器实现的 `Scanner` 结构体使用模式匹配来识别 tokens。 单元测试非常广泛，并由 `rstest` crate 提供支持。

解析阶段的重点是生成符合规范的抽象语法图，利用 Rust 的 `serde` 和 `serde-json` crates 将其序列化为 JSON。 作者选择为每个 Asciidoc 元素类型定义一个结构体，而不是使用更抽象的方法。 文章最后简单介绍了内联元素的结构。

---

## 24. KaTeX – 网页上最快的数学公式排版库

**原文标题**: KaTeX – The fastest math typesetting library for the web

**原文链接**: [https://katex.org/](https://katex.org/)

KaTeX：快速、独立的Web数学排版库，旨在高效准确地渲染数学表达式。它拥有简洁的API，无依赖，并在主流浏览器中表现出色。其主要特点是同步渲染，避免页面重排，从而提高了速度。

KaTeX以Donald Knuth的TeX为基础进行布局，保证了打印质量，TeX是公认的数学排版黄金标准。它是独立的，易于与网站资源捆绑，并且可以通过Node.js用于服务器端渲染，无论在何种环境中都能产生一致的输出。这使其非常适合将数学表达式预渲染为纯HTML。即使在包含数百个表达式的页面上，它也能保持闪电般的快速性能，使其优于MathJax等替代方案。

该页面还提供了安装说明、文档和GitHub存储库的链接。交互式示例允许用户输入KaTeX表达式并实时查看其渲染效果。该网站还详细介绍了可用于自定义KaTeX行为的各种配置选项，包括显示模式、错误处理、输出格式、信任和自定义宏的选项。编辑器选项包括最大化编辑器、复制KaTeX代码和复制永久链接。

---

## 25. 我分析了1.8亿份工作，看看人工智能正在取代哪些工作。

**原文标题**: I analyzed 180M jobs to see what jobs AI is replacing today

**原文链接**: [https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/](https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/)

The article, titled "I analyzed 180M jobs to see what jobs AI is replacing today," discusses how to AI-proof your career as a knowledge worker in light of the advancements in AI like ChatGPT. Written by Henley Wing Chiu and updated on March 20, 2024, the article is based on an analysis of a large dataset of 180 million jobs. While the summary lacks specific details about the analysis findings or the jobs most at risk, the core theme centers on understanding the impact of AI on the job market and providing guidance on how knowledge workers can adapt to remain valuable in an increasingly AI-driven world. The article falls under the categories of "AI" and "Learning & Development," suggesting it likely offers strategies for upskilling and reskilling to complement or work alongside AI technologies. The author shares their personal experiences with ChatGPT to illustrate the transformative potential of AI and likely uses this anecdote as a springboard to discuss broader career implications and proactive measures.


---

## 26. 杜鹃花镇的转弯车道

**原文标题**: A turn lane in Rhododendron

**原文链接**: [https://www.greentape.pub/p/a-turn-lane-in-rhododendron](https://www.greentape.pub/p/a-turn-lane-in-rhododendron)

This article details the arduous 25-year journey to install a left-turn lane on a dangerous 1.26-mile stretch of US-26 near Rhododendron, Oregon. In 1998, residents pleaded with ODOT for the turn lane due to a high accident rate, including fatal crashes, caused by the lack of a safe place to turn off the busy highway.

The project triggered NEPA and NHPA reviews due to FHWA jurisdiction. This process was complicated by past resistance to highway development, spearheaded by Michael P. Jones of CFASH, who had previously stalled a highway widening project with claims of a pioneer gravesite, which was later debunked by archaeologists.

Despite ODOT's extensive efforts, including archaeological surveys, public hearings, and newsletters, Jones resurfaced with new allies, including individuals claiming tribal affiliations, to demand further NHPA reviews. They argued that the area contained sacred burial sites, delaying the project for years.

Construction finally began in 2008 after ODOT determined it had fulfilled its NHPA obligations. However, Jones continued to fight the project, filing a lawsuit that dragged on for 13 years. The courts ultimately ruled in favor of the agencies, and a final settlement was reached in 2023.

The article highlights the immense cost, in terms of time, money, and human life, caused by the prolonged delays and litigation. What should have been a simple safety improvement was stalled by community opposition and legal challenges, turning a pile of rocks into a major obstacle.


---

## 27. Oxy 是 Cloudflare 基于 Rust 的下一代代理框架 (2023)

**原文标题**: Oxy is Cloudflare's Rust-based next generation proxy framework (2023)

**原文链接**: [https://blog.cloudflare.com/introducing-oxy/](https://blog.cloudflare.com/introducing-oxy/)

Oxy：Cloudflare 的下一代代理框架，采用 Rust 构建，专为高负载流量处理而设计，是 Zero Trust Gateway 和 iCloud Private Relay 第二跳等项目的基础。它提供对代理各个方面的编程控制，包括协议处理、流量分析、路由和 DNS 解析。

Oxy 的架构允许开发者从基本解决方案开始，并利用其扩展点逐步添加功能。它支持各种入口（HTTP、TCP、UDP、IP）和出口，在流量进入和退出方面提供灵活性。一个关键特性是应用程序可以强制流量解封装，从而实现多层（L3-L7）分析和处理。

该框架处理 TCP、UDP、QUIC 和 IP 的有状态隧道，并提供全面的 HTTP 处理，包含流分析工具。它还支持高级 HTTP 隧道方法和 HTTP CONNECT 负载的递归处理。

安全至关重要，TLS 基于 BoringSSL（符合 FIPS 标准且使用最新版本）、浏览器级 TLS 客户端功能和 mTLS 支持。Oxy 提供动态证书生成和原始公钥使用的功能。

Oxy 提供了一个有凝聚力的环境，处理引导、配置、异步运行时、安全加固和优雅重启。它内置支持 Sentry、Prometheus 和 Kibana 等监控工具，以及集成测试框架。

Oxy 应用程序使用 YAML 文件配置，可通过 Rust 宏扩展。其扩展模型允许通过一套全面的钩子修改流量的几乎所有方面。选择 Rust 技术确保了安全性和性能，并利用了 hyper 和 tokio 等开源依赖项。

---

## 28. 1900年巴黎曾有自动人行道，托马斯·爱迪生的一部影片记录了这一场景 (2020)

**原文标题**: Paris had a moving sidewalk in 1900, and a Thomas Edison film captured it (2020)

**原文链接**: [https://www.openculture.com/2020/03/paris-had-a-moving-sidewalk-in-1900.html](https://www.openculture.com/2020/03/paris-had-a-moving-sidewalk-in-1900.html)

本文探讨了1900年巴黎世博会上展出的移动人行道，该人行道由托马斯·爱迪生的制片人詹姆斯·亨利·怀特拍摄成电影。虽然移动人行道在今天已司空见惯，但在世纪之交，它们还是一种新奇事物，是人们娱乐的来源。

文章详细介绍了怀特如何通过一种新型摇摄云台三脚架拍摄到公众对这项创新技术的反应。文章引用了《纽约观察家报》记者的话，描述了该人行道有三个以不同速度移动的升高平台，使得穿越世博会更快、更有趣。

文章还深入探讨了移动人行道的历史，提到了阿尔弗雷德·斯佩尔在1871年获得的专利以及芝加哥1893年哥伦比亚世博会的版本，后者不如巴黎的版本可靠。尽管是一项古老的技术，但文章认为移动人行道仍然具有公共交通的潜力，使步行距离更易于管理，旅途更加愉快。作者感叹巴黎在世博会结束后没有保留移动人行道，认为这是在交通和娱乐方面错失的机会。

---

## 29. 微型电机可产生超过1000马力

**原文标题**: Tiny electric motor can produce more than 1,000 horsepower

**原文链接**: [https://supercarblondie.com/electric-motor-yasa-more-powerful-tesla-mercedes/](https://supercarblondie.com/electric-motor-yasa-more-powerful-tesla-mercedes/)

梅赛德斯-奔驰英国子公司YASA开发出一款微型高性能电机，其功率和性能密度超越了现有电动汽车电机。这款轴向磁通电机仅重28磅，可产生750千瓦（1005马力）的功率，超过四个特斯拉电机的总功率，并比YASA之前的记录保持者提升了40%。它还能持续输出469-536马力。

该电机的小型轻量化设计有助于提高电动汽车的效率、加速和续航里程。YASA声称该设计可以使用现成材料进行扩展。该公司已经为梅赛德斯-AMG GT XX和法拉利296 GTB等高端车型提供电机。虽然目前应用于昂贵的汽车，但随着生产规模扩大和成本降低，这项技术最终有可能应用于更经济实惠的电动汽车，如日产聆风。

---

## 30. Arduino Uno Q：奇特的混合型单板计算机

**原文标题**: The Arduino Uno Q is a weird hybrid SBC

**原文链接**: [https://www.jeffgeerling.com/blog/2025/arduino-uno-q-weird-hybrid-sbc](https://www.jeffgeerling.com/blog/2025/arduino-uno-q-weird-hybrid-sbc)

Arduino Uno Q 是一款混合型单板计算机 (SBC)，是高通收购 Arduino 后的产物。它将较早的高通 Dragonwing SoC（Arm A53 CPU 内核、Adreno iGPU、2GB RAM、16GB eMMC）与运行 Debian Linux 的 Arduino 微控制器相结合。主要接口是一个 USB-C 端口，处理电源、HDMI 和 USB，虽然底部存在高速连接器用于未来扩展。

该设备运行 Arduino 的 App Lab，一个统一的 IDE，支持 Linux 端的 Python 和 MCU 端的 C++。虽然 Linux 性能与 Raspberry Pi 3 B+ 或 Pi 4 相当，但它并不适合像网页浏览这样要求较高的任务。功耗在 0.5-3W 之间，还算不错，但 Linux 堆栈无法禁用，不能单独运行 MCU。

2GB 版本的售价为 44 美元，与 Raspberry Pi 5 或 Radxa X4 等更快的替代品相比，它并不是性价比最高的 SBC。虽然它以“边缘的现代 AI”为卖点，但它仅限于较小的模型，并且性能比竞争对手慢。App Lab 在管理 Python/C++ 代码方面有所改进，但仍然不如在 Raspberry Pi 上访问 GPIO 那样无缝。

尽管存在潜在的缺点，但 Uno Q 仍然秉承 Arduino 的开源承诺，提供可用的原理图。它的优势在于以 Arduino 为中心的课程或受益于 Linux 进行远程访问和轻量级 ML 模型的机器人管道，但作者认为在现有 Arduino 生态系统之外的个人使用价值不大。长期可行性取决于高通的持续投资和支持。

---

## 31. 使用 FreeBSD 让自托管再次充满乐趣

**原文标题**: Using FreeBSD to make self-hosting fun again

**原文链接**: [https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/](https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/)

生成摘要出错

---

## 32. ECL在浏览器中运行Maxima

**原文标题**: ECL Runs Maxima in a Browser

**原文链接**: [https://mailman3.common-lisp.net/hyperkitty/list/ecl-devel@common-lisp.net/thread/T64S5EMVV6WHDPKWZ3AQHEPO3EQE2K5M/](https://mailman3.common-lisp.net/hyperkitty/list/ecl-devel@common-lisp.net/thread/T64S5EMVV6WHDPKWZ3AQHEPO3EQE2K5M/)

ecl-devel邮件列表上的这封邮件宣布 Marius Gerbershagen 已经成功地使用 ECL (可嵌入 Common Lisp) 将 Maxima 计算机代数系统编译为 WebAssembly (wasm)。 这使得 Maxima 能够直接在网页浏览器中运行。

该实现的关键特性是它是一个“相当完整的实现”，支持用于数学符号的公式的 TeX 显示，并通过 wasm 编译的 gnuplot 版本合并了图形功能。 该邮件提供了一个链接 (http://maxima-on-wasm.pages.dev/) 指向在浏览器中运行的 Maxima 的实时演示。 该邮件由 Raymond Toy 于 2025 年 1 月 27 日撰写，旨在告知 ECL 开发社区这一成就，并暗示他们会对它感兴趣。

---

## 33. 谷歌撤回AI模型，此前参议员称其捏造袭击指控。

**原文标题**: Google pulls AI model after senator says it fabricated assault allegation

**原文链接**: [https://www.theverge.com/news/812376/google-removes-gemma-senator-blackburn-hallucination](https://www.theverge.com/news/812376/google-removes-gemma-senator-blackburn-hallucination)

生成摘要时出错

---

## 34. 谷歌第三次暂停了我公司的谷歌云账户。

**原文标题**: Google suspended my company's Google cloud account for the third time

**原文链接**: [https://www.agwa.name/blog/post/google_suspended_sslmates_cloud_account_again](https://www.agwa.name/blog/post/google_suspended_sslmates_cloud_account_again)

本文详述了作者在使用谷歌云时令人沮丧的经历：其公司SSLMate的账户在没有事先通知的情况下被暂停了三次。SSLMate使用谷歌云来促进与客户谷歌云账户的集成，用于证书验证和域名监控，采用了谷歌文档推荐的服务账户模拟系统。

作者强调这种方法既安全（没有长期有效的凭据），又便于客户配置。然而，谷歌的重复暂停中断了这项服务，需要与支持部门进行广泛而令人沮丧的沟通才能解决。每次暂停都涉及不同的错误消息和恢复流程，导致作者对暂停的原因或如何防止暂停一无所知。

作者探讨了其他集成方法，特别强调了OpenID Connect (OIDC) 作为长期有效的服务账户密钥的更安全替代方案。然而，谷歌对OIDC的实现被认为是不必要的复杂，涉及一个七步流程，阻碍了可用性。

最终，作者认为，谷歌反复无常的账户暂停和繁琐的OIDC设置迫使人们在设置跨提供商访问时，需要在安全性、可用性和可靠性之间做出权衡。他们提出了一个问题，即这三者中哪两个最重要。他们对谷歌没有简化OIDC的使用感到沮丧，如果能简化，这将鼓励使用更安全的替代方案来存储密钥。

---

## 35. 错位的鱼

**原文标题**: Fish in the Wrong Place

**原文链接**: [https://www.lrb.co.uk/the-paper/v47/n19/oliver-cussen/fish-in-the-wrong-place](https://www.lrb.co.uk/the-paper/v47/n19/oliver-cussen/fish-in-the-wrong-place)

奥利弗·库森的文章《错位的鱼》探讨了殖民时期移植鱼类和实施大型水利工程所带来的意想不到的生态后果。文章强调，诸如引入亚洲鲤鱼控制杂草或在河流中放养鳟鱼以供娱乐等看似有益的干预措施，往往会导致生态破坏和本土物种的衰退。

该文还借鉴科里·罗斯的《液态帝国》和詹姆斯·C·斯科特的著作，考察了水利工程在殖民项目中的作用。殖民势力试图控制和改造水道，以用于农业、贸易和资源开采。例如，将孟加拉邦的红树林转化为农田，在旁遮普邦修建灌溉系统，以及诸如撒哈拉海计划等失败的项目。这些努力常常导致生态破坏、社会动荡以及意想不到的后果，例如对自然灾害的脆弱性增加和土著居民的流离失所。

库森讨论了斯科特对“高度现代主义”国家权力的批判，以及其对复杂自然系统强加简化秩序的倾向，并引用了苏联和坦桑尼亚农业改革以及巴西和印度的城市规划的例子。文章强调，控制河流和管理环境的尝试往往适得其反，导致不稳定和“计划中的混乱”。尽管技术进步，人类仍然难以完全控制自然系统，而这样做的努力常常导致无法预见且有害的后果。

---

## 36. 据称 Jabber Zeus 编写者 'MrICQ' 在美国被拘留

**原文标题**: Alleged Jabber Zeus Coder 'MrICQ' in U.S. Custody

**原文链接**: [https://krebsonsecurity.com/2025/11/alleged-jabber-zeus-coder-mricq-in-u-s-custody/](https://krebsonsecurity.com/2025/11/alleged-jabber-zeus-coder-mricq-in-u-s-custody/)

Yuriy Igorevich Rybtsov, a Ukrainian man known online as "MrICQ," has been arrested in Italy and is now in U.S. custody for his alleged involvement in the "Jabber Zeus" cybercrime group. Indicted in 2012, Rybtsov is accused of being a key developer who managed notifications of compromised victims and helped launder stolen funds.

The Jabber Zeus group used a custom version of the ZeuS banking trojan to steal login credentials and intercept one-time passcodes, targeting primarily small to mid-sized businesses. They pioneered "man-in-the-browser" attacks to steal financial data and used money mules to launder the stolen funds.

Key figures in the Jabber Zeus operation include Vyacheslav “Tank” Penchukov, already sentenced to 18 years in prison, and Maksim Yakubets ("Aqua"), who later led the "Evil Corp" cybercrime ring. The group even interacted with Evgeniy Mikhailovich Bogachev, the original author of the Zeus Trojan.

Threat intelligence company myNetWatchman infiltrated Jabber Zeus's chat server, providing crucial evidence and enabling the disruption of their activities. Their key innovation, "Leprechaun," allowed them to identify and target high-value commercial bank accounts with two-factor authentication. The group also utilized "backconnect" components to mask their activity by using the victim's own IP address.


---

## 37. 瑞坎莎的微型工具箱

**原文标题**: Recantha's Tiny Toolkit

**原文链接**: [https://tinytoolk.it/toolkits/recantha-kit/](https://tinytoolk.it/toolkits/recantha-kit/)

Recantha的迷你工具包是一个通用工具包，设计用于各种任务，包括设计工作，收纳于一个Lihit Lab勃艮第迷彩笔盒中。笔盒外侧口袋装有便利贴。

该工具包分层收纳。第一层包含Temu多功能工具、剪刀和瑞士军刀。第二层1包含切割工具，如凿头Sharpie笔、斜口钳、手术刀、小型活动扳手和开箱/美工刀。第二层2包含一个小型螺丝刀手柄及批头和套筒适配器、剥线钳/剪线钳、各种镊子、另一个活动扳手、更多开箱刀、eSpares免费赠送的铅笔、一个小清洁刷和大型镊子。

第三层侧重于线缆和文具：USB线缆和一个双向分线器、回形针、长尾夹、microSD适配器、另一个多功能工具、电路板尺、更多镊子和开箱刀、一套套筒、iFixit撬棒、荧光笔、迷你卷尺和一个橡皮擦。

Recantha承认存在一些冗余，特别是开箱刀，并计划扩展工具包以包含电动螺丝刀和电工胶带，同时移除重复物品以腾出空间。尽管由于多功能工具的存在导致重量较重，但该工具包被认为非常有用。

---

## 38. Meta暗示Windows 11版WhatsApp将切换为Chromium Web应用。

**原文标题**: Meta hints WhatsApp for Windows 11 will switch to a Chromium web app

**原文链接**: [https://www.windowslatest.com/2025/10/31/whatsapp-native-app-on-windows-11-is-getting-killed-on-nov-5-replaced-by-chromium/](https://www.windowslatest.com/2025/10/31/whatsapp-native-app-on-windows-11-is-getting-killed-on-nov-5-replaced-by-chromium/)

Windows 11 原生 WhatsApp 应用将过渡到基于 Chromium 的 Web 应用，本质上是在容器内运行 web.whatsapp.com。此更改计划于 2025 年 11 月 5 日开始分阶段推出，届时用户需要重新登录。

切换到 Chromium 意味着该应用可能会消耗更多的系统资源，特别是 RAM，这是因为 Chromium 本身就是资源密集型的。Beta 测试人员已经体验了这一变化，并观察到 RAM 使用量增加。虽然之前的原生 WhatsApp 应用存在性能问题，但它与 Windows 的集成度更高，且占用内存更少。然而，基于 Chromium 的版本可能会受到性能问题、离线工作不佳以及通知问题的困扰。

Meta 承认原生应用通常提供更好的性能和可靠性，但切换到 Chromium 的决定可能源于节约成本的措施。使用 Web 代码可以降低开发和维护成本，因为相同的代码可以在多个平台上运行。作者认为这可能是 Meta 最近裁员的结果。

过渡将分阶段进行，提示用户重新登录。在此过程中，最多可以从用户的手机同步一年的聊天记录。

---

## 39. 为什么不用依赖类型？

**原文标题**: Why don't you use dependent types?

**原文链接**: [https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html](https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html)

生成摘要出错

---

## 40. 新型提示注入论文：二二法则与攻击者后动

**原文标题**: New prompt injection papers: Agents rule of two and the attacker moves second

**原文链接**: [https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/)

生成摘要时出错

---

## 41. 模型操纵流形：计数任务的几何学

**原文标题**: When models manipulate manifolds: The geometry of a counting task

**原文链接**: [https://transformer-circuits.pub/2025/linebreaks/index.html](https://transformer-circuits.pub/2025/linebreaks/index.html)

当模型操纵流形：计数任务的几何学

本文题为“当模型操纵流形：计数任务的几何学”，研究了像 Claude 3.5 Haiku 这样的语言模型如何从文本中学习感知任务，特别是固定宽度文本中的换行。作者发现，该模型发展出类似于哺乳动物“位置细胞”的位置表征，使用离散特征和一维“特征流形”来跟踪字符数。

该模型结合了代表行中当前位置和总行宽的特征，以估计与行尾的距离并预测换行符。这种计算被描述为一个“归因图”，显示了不同的特征如何相互激发或抑制。

主要发现包括：
* 整数计数在一维特征流形上表示，这些流形嵌入在低维子空间中。
* 注意力头旋转一个计数流形，使其与另一个流形对齐以检测行边界。
* 计数位于近正交子空间上，从而允许换行预测中的线性可分离性。
* 字符计数表示流形中的曲率由多个注意力头产生。

作者通过干预和消融验证了他们的解释。他们认为，使用特征流形是表示标量量的有效方法，并且研究语言模型固有的任务可以揭示一般的机制。该研究强调了特征和几何学在理解模型行为中的二元性，以及降低解释的“复杂性税”的重要性。他们引入了一个合成数据集来系统地分析换行行为。

---

## 42. 教学大纲 – 具有工具、RAG和多渠道部署的开源代理AI

**原文标题**: Syllabi – Open-source agentic AI with tools, RAG, and multi-channel deploy

**原文链接**: [https://www.syllabi-ai.com/](https://www.syllabi-ai.com/)

Syllabi：构建可定制化智能AI聊天机器人的开源平台，具备知识库、多应用集成和全渠道部署能力。它允许用户将文档、网站和其他数据源转化为智能知识库，利用检索增强生成（RAG）技术，实现准确的信息检索并提供来源引用。

主要功能包括多格式支持（PDF、网站、Google Drive等）、高级RAG，以及在Web插件、Slack和Discord等多个渠道部署聊天机器人的能力。它通过自定义技能和通过Webhooks和API实现的工具集成，实现智能体行为，使聊天机器人能够执行发送Slack消息或触发工作流程等操作。

Syllabi支持超越简单问答的丰富、交互式对话，允许文档高亮、图表生成（Mermaid、流程图）、原生代码执行（Python、R）和多媒体嵌入。它专为各种用例而设计，包括课程助手、网站支持、团队知识共享和API/代码文档。

该平台提供对聊天机器人行为和外观的完全控制，包括品牌定制选项、模型配置（GPT-4、GPT-3.5）和对话设计。还提供分析和见解。Syllabi与各种工具集成，包括Google Drive、Notion、Slack、Google Workspace，并通过Gmail、Google Calendar和自定义API提供操作/工作流程。

作为一个采用MIT许可的开源、自托管解决方案，Syllabi优先考虑数据隐私和安全，确保用户保留对其AI基础设施的完全控制。该平台正在积极开发中，并由社区驱动，鼓励贡献和可扩展性。

---

## 43. X.Org安全公告：X.Org X服务器和Xwayland存在多个安全问题

**原文标题**: X.org Security Advisory: multiple security issues X.Org X server and Xwayland

**原文链接**: [https://lists.x.org/archives/xorg-announce/2025-October/003635.html](https://lists.x.org/archives/xorg-announce/2025-October/003635.html)

X.Org安全公告：2025年10月28日，宣布修复X.Org X服务器21.1.18之前版本和Xwayland 24.1.8之前版本中发现的多个安全漏洞。修复程序已在xorg-server-21.1.19和xwayland-24.1.9中发布。

修复了三个具体漏洞：

1.  **CVE-2025-62229：** 与XPresentNotify结构创建相关的释放后使用漏洞。此问题发生在X11 Present扩展中，在显示pixmap后处理通知时，错误可能导致悬空指针，从而在销毁通知结构期间导致释放后使用。
2.  **CVE-2025-62230：** 与Xkb客户端资源移除相关的释放后使用漏洞。`XkbRemoveResourceClient()`函数未能释放与设备关联的资源，导致客户端终止且资源删除函数被触发时出现释放后使用。
3.  **CVE-2025-62231：** Xkb扩展的`XkbSetCompatMap()`函数中的值溢出漏洞。`XkbCompatMap`结构使用unsigned short存储值，但缺乏适当的检查以防止在对输入数据求和时溢出，可能超出unsigned short的最大值。

所有三个漏洞均由Jan-Niklas Sohn与Trend Micro Zero Day Initiative合作发现。每个漏洞的修复程序均以GitLab提交链接的形式提供。该公告鼓励用户更新到已修补的版本，以降低这些安全风险。

---

## 44. Lisp：关于其过去与未来的札记 (1980)

**原文标题**: Lisp: Notes on its Past and Future (1980)

**原文链接**: [https://www-formal.stanford.edu/jmc/lisp20th/lisp20th.html](https://www-formal.stanford.edu/jmc/lisp20th/lisp20th.html)

约翰·麦卡锡在1980年的文章《Lisp：对其过去和未来的思考》中认为，LISP的长寿（当时为21年）源于其在编程语言领域中的有利地位。然而，他认为该语言已经背负了不必要的功能（“藤壶”），并错失了增强的机会。

麦卡锡提倡合作维护，尤其是在LISP程序库的开发和维护方面。他强调了LISP支持计算机检查程序正确性证明的潜力，尤其是在其纯粹形式和某些扩展的情况下。然而，他承认，要充分实现这一潜力，利用LISP的数学基础，既需要理论上的进步，也需要对语言本身的改进。

在1999年的一份说明中，麦卡锡断言他的观点与1980年文章中表达的观点保持一致。他认为这篇文章与当代Lisp讨论相关，强调了继续解决该语言积累的缺点和未实现潜力的必要性。文章随后概述了所讨论的主题：LISP的生存、潜在的改进、证明程序正确性以及其他相关谜题。

---

## 45. 趁还能用CarPlay，好好享受吧

**原文标题**: Enjoy CarPlay While You Still Can

**原文链接**: [https://www.theatlantic.com/technology/2025/11/apple-carplay-general-motors/684799/](https://www.theatlantic.com/technology/2025/11/apple-carplay-general-motors/684799/)

帕特里克·乔治的文章《趁现在还能用，好好享受CarPlay吧》讨论了汽车制造商（特别是通用汽车）放弃支持苹果 CarPlay 和 Android Auto，转而支持其自有车载软件的日益增长的趋势。虽然 CarPlay 是一款备受欢迎且免费的功能，可以将 iPhone 的功能映射到汽车屏幕上，但通用汽车认为其自有软件可以提供更卓越的用户体验。

然而，这种转变对消费者有着重大影响。通用汽车的软件需要单独的数据套餐，为基于订阅的功能和数据货币化打开了大门，而这在汽车行业正日益成为一种趋势。汽车公司将车载技术视为一种新的收入来源，可能会对诸如免提驾驶、远程启动甚至出售用户数据等功能收费。

虽然一些汽车制造商仍然致力于 CarPlay，甚至还在增强它，但作者认为它的好日子屈指可数了。苹果公司凭借 CarPlay Ultra 展现出的雄心壮志（旨在控制更多的车辆功能）被汽车公司视为一种威胁，它们不想仅仅成为科技巨头的硬件供应商。最终，放弃 CarPlay 预示着未来驾驶员可能需要为各种车载技术支付定期订阅费，从而增加每月的账单支出。

---

## 46. Show HN: Centia.io – 面向开发者的开放PostgreSQL/PostGIS后端

**原文标题**: Show HN: Centia.io – Open PostgreSQL/PostGIS back end for developers

**原文链接**: [https://centia.io/](https://centia.io/)

生成摘要时出错

---

## 47. 使用模型检测器重现AWS中断竞争条件

**原文标题**: Reproducing the AWS Outage Race Condition with a Model Checker

**原文链接**: [https://wyounas.github.io/aws/concurrency/2025/10/30/reproducing-the-aws-outage-race-condition-with-model-checker/](https://wyounas.github.io/aws/concurrency/2025/10/30/reproducing-the-aws-outage-race-condition-with-model-checker/)

本文详细介绍了如何使用模型检查器 (Spin) 重现一个导致 AWS 宕机的竞态条件，该竞态条件在事后分析报告中有所描述。作者简化了涉及 DynamoDB DNS 管理系统（DNS Planner、DNS Enactor 和 Route 53）的事件，并使用 Promela 对关键组件进行建模。

该模型表示 DNS Planner 创建计划，Enactor 将其应用于 Route 53，包括删除旧计划的清理过程。当一个 Enactor 应用较新的计划，随后另一个 Enactor 应用较旧的计划，而该计划随后被第一个 Enactor 的清理过程删除时，就会出现潜在的竞态条件，从而导致 DNS 故障。

为了发现这一点，作者定义了不变式，特别是 DNS 在应用较新的计划后绝不应被删除。Spin 识别到一个违反，生成一个轨迹文件，展示了竞态条件。第二个不变式，即活动计划绝不应被删除，产生类似的结果。

本文强调了不变式在验证系统正确性方面的价值，以及模型检查如何暴露细微的并发错误。解决方案涉及原子性地执行有问题的语句，以防止竞争。作者提供了 Promela 代码（包括修复前和修复后的代码）以及在链接的存储库中运行模型检查器的说明，并强调由于缺乏 AWS 内部设计细节，该模型已得到简化。

---

## 48. 考拉茨-外尔生成器：伪随机数生成器 (2023)

**原文标题**: Collatz-Weyl Generators: Pseudorandom Number Generators (2023)

**原文链接**: [https://arxiv.org/abs/2312.17043](https://arxiv.org/abs/2312.17043)

托马斯·R·贾瓦的这篇arXiv文章，题为“Collatz-Weyl生成器：高质量和高吞吐量参数化伪随机数生成器”，介绍了一种新的伪随机数生成器(PRNGs)，称为Collatz-Weyl生成器。这些生成器基于广义Collatz映射（与Collatz猜想相关）和Weyl序列的组合。

关键主张是这些生成器提供了高质量的统计特性，并通过了研究和标准化中使用的严格随机性测试来证明。除了质量之外，该论文还强调了几个重要的优点：

*   **坚实的数学基础：** 这些生成器建立在已建立的数学概念之上。
*   **高吞吐量和低延迟：** 它们被设计用于高效实现。
*   **小占用空间：** 这些生成器需要最少的代码或ASIC尺寸。
*   **多个独立流：** 该设计支持独立随机序列的生成。
*   **密码学潜力：** 这些生成器具有用于密码学应用的潜力。

该文章被归类为计算机科学>计算工程、金融和科学（cs.CE）。它经历了多次修订，最新版本于2024年12月2日提交。该文章还提供了相关论文、代码和演示工具的链接。

---

## 49. 太赫兹技术为“无线有线”芯片奠定基础

**原文标题**: Terahertz Tech Sets Stage for "Wireless Wired" Chips

**原文链接**: [https://spectrum.ieee.org/terahertz-chip-room-temperature](https://spectrum.ieee.org/terahertz-chip-room-temperature)

生成摘要时出错

---

## 50. 抽象语法树：C语言示例

**原文标题**: Abstract Syntax Tree: An Example in C

**原文链接**: [https://keleshev.com/abstract-syntax-tree-an-example-in-c/](https://keleshev.com/abstract-syntax-tree-an-example-in-c/)

本文演示了如何在 C 语言中实现和使用抽象语法树 (AST)。C 语言本身没有内置对通常用于 AST 的面向对象或函数式数据结构的支持。本文展示了一种使用结构体、枚举和联合的标记联合方法，以表示 AST 内的不同节点类型（数字、加法、乘法和主程序）。

文章概述了 C 语言在创建 AST 节点时面临的挑战，特别是需要显式类型转换和指定初始化器。引入了一个变参宏 `AST_NEW`，以减少样板代码并提高 AST 构建过程中的可读性。

然后，文章通过漂亮打印、释放内存（内存管理）和代码生成（x86-64 汇编）的示例，说明了如何操作 AST。代码生成示例展示了如何遍历 AST 并为算术运算发出相应的汇编指令。文章强调了编译器警告（-Wswitch，-Wimplicit-fallthrough）对于可靠使用标记联合的重要性。

最后，本文包含一个奖励部分，展示了在 OCaml 中相同的 AST 实现和代码生成示例，突出了函数式语言在编译器开发方面的简洁性和类型安全优势。

---

## 51. 机器的不确定编织（2021）[视频]

**原文标题**: Underdetermined Weaving with Machines (2021) [video]

**原文链接**: [https://www.youtube.com/watch?v=on_sK8KoObo](https://www.youtube.com/watch?v=on_sK8KoObo)

这并非文章，而是YouTube页脚信息的片段。内容详细说明了与YouTube平台相关的标准法律免责声明、运营信息和联系方式。内容包括：

*   **法律政策链接：**版权信息、条款、隐私政策和安全指南。
*   **创作者资源：** 创作者关于广告、开发和平台通用用法的资源。
*   **通用信息：** "关于"、"媒体"和"联系我们"链接。
*   **运营说明：** "YouTube运作方式"和"测试新功能"信息。
*   **未来合作关系指示：** 提及 "NFL Sunday Ticket © 2025 Google LLC"，表明未来合作关系。

本质上，所提供的内容是YouTube页面底部的标准样板信息。

---

## 52. 瑞士奶酪为什么有孔？

**原文标题**: Why does Swiss cheese have holes?

**原文链接**: [https://www.usdairy.com/news-articles/why-does-swiss-cheese-have-holes](https://www.usdairy.com/news-articles/why-does-swiss-cheese-have-holes)

This article explains why Swiss cheese has its signature holes, also known as "eyes." The holes are created by carbon dioxide bubbles produced by Propionibacteria (Props) during fermentation. These bacteria, naturally found in raw milk and often added back after pasteurization, consume lactic acid in the cheese, releasing carbon dioxide as a byproduct.

The cheese is aged in warm rooms, facilitating the fermentation process and allowing the carbon dioxide to form the characteristic holes while maintaining the cheese's texture. The size, number, and distribution of these holes are carefully monitored and regulated as an indicator of quality.

In Switzerland, Swiss cheese is called Emmental. Varieties like Baby Swiss and Jarlsburg are also forms of Emmental, with differences in moisture, fat content, and bacterial composition affecting the size and appearance of the holes.

While Swiss cheese is most known for this characteristic, other cheeses can develop holes through different bacteria or fermentation conditions. Swiss cheese without holes is referred to as "blind" but retains the same taste. Cheesemakers diligently control hole size to meet quality standards.


---

## 53. Is Your Bluetooth Chip Leaking Secrets via RF Signals?

**原文标题**: Is Your Bluetooth Chip Leaking Secrets via RF Signals?

**原文链接**: [https://www.semanticscholar.org/paper/Is-Your-Bluetooth-Chip-Leaking-Secrets-via-RF-Ji-Dubrova/c1d3ceb47ea6f9cc4f29929e2f97d36862a260a2](https://www.semanticscholar.org/paper/Is-Your-Bluetooth-Chip-Leaking-Secrets-via-RF-Ji-Dubrova/c1d3ceb47ea6f9cc4f29929e2f97d36862a260a2)

This Semantic Scholar entry highlights a research paper titled "Is Your Bluetooth Chip Leaking Secrets via RF Signals?" by Ji, Dubrova, and Wang, published in IACR Cryptology ePrint Archive in 2025. The paper describes a machine learning-assisted side-channel attack targeting the hardware AES accelerator within a Bluetooth chip commonly found in devices like wearables, smart home products, and industrial IoT.

The core finding is that the researchers successfully recovered the full encryption key by analyzing RF signals emitted by the chip during AES encryption. This was achieved by capturing 90,000 traces at a distance of one meter from the target device. This demonstrates a vulnerability where sensitive information, specifically the encryption key, can be extracted remotely through the analysis of RF emissions.

The paper is related to other research in the field of side-channel attacks, particularly "screaming channels," which involve exploiting electromagnetic side channels in radio transceivers. These related works explore similar vulnerabilities and countermeasures in other wireless communication protocols like WiFi. The research emphasizes the need for enhanced security measures, such as masking or hiding techniques, to protect devices from such attacks. Further investigations explore deep learning techniques for far-field electromagnetic side-channel attacks on AES implementations. Ultimately, this study adds to the growing body of evidence suggesting that RF signals can be a viable attack vector for extracting sensitive data from embedded systems.


---

## 54. 举办出色派对的诀窍

**原文标题**: Facts about throwing good parties

**原文链接**: [https://www.atvbt.com/21-facts-about-throwing-good-parties/](https://www.atvbt.com/21-facts-about-throwing-good-parties/)

生成摘要时出错

---

## 55. OpenAI与亚马逊签署380亿美元云计算协议

**原文标题**: OpenAI Signs $38B Cloud Computing Deal with Amazon

**原文链接**: [https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html](https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html)

无法访问文章链接。

---

## 56. AMD勘误：AMD Zen 5处理器RDSEED故障

**原文标题**: AMD Errata: RDSEED failure on AMD Zen 5 Processors

**原文链接**: [https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7055.html](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7055.html)

AMD勘误表 (AMD-SB-7055) 详细说明了影响“Zen 5”处理器的严重缺陷，其中 RDSEED 指令（特别是 16 位和 32 位形式）可能会错误地返回 0 值，同时仍指示成功，从而导致潜在的故障误判和使用随机性不足的值。这可能会损害机密性和完整性。RDSEED 的 64 位形式不受影响。

AMD 计划通过 AGESA 和微代码更新发布针对受影响产品的缓解措施，目标发布日期从 2025 年 10 月下旬到 2026 年 1 月不等，具体取决于特定产品线（EPYC、Ryzen、Embedded）。建议用户联系其 OEM 获取 BIOS 更新。

在官方修复程序发布之前，该文档概述了几种软件解决方法：

1. 使用 64 位 RDSEED 指令。
2. 屏蔽 RDSEED CPUID 标志，以防止软件使用有缺陷的指令。
3. 将 RDSEED 返回的 0 值视为失败 (CF=0) 并重试该指令。

该问题被跟踪为 CVE-2025-62626，CVSS 评分为 7.2（高）。该勘误表强调，信息可能会发生变化，并附带有关准确性和责任的免责声明。

---

## 57. 青少年屏幕使用可能引发家庭冲突，加剧心理健康问题。

**原文标题**: Youth screen use can cause family conflict, exacerbate mental health problems

**原文链接**: [https://medicalxpress.com/news/2025-10-youth-screen-family-conflict-exacerbate.html](https://medicalxpress.com/news/2025-10-youth-screen-family-conflict-exacerbate.html)

A new study from the University of Georgia highlights the potential negative impacts of early smartphone use on family dynamics and youth mental health. Researchers analyzed data from over 11,000 families over a decade, finding that increased screen use, particularly social media, in children as young as 11 correlates with more frequent and intense family conflicts. These conflicts stemmed from disagreements and difficulty resolving issues related to social media use. This trend was particularly pronounced in young girls, who may be more prone to social comparison online. Interestingly, video games and video viewing alone did not cause the same level of strife.

The study also revealed a correlation between early smartphone ownership and a decreased likelihood of adolescents disclosing emotional struggles like anxiety or depression to their parents. This creates communication gaps, potentially leading to children internalizing problems, which can have long-term mental health implications. Researchers suggest delaying smartphone ownership and setting boundaries on screen time, prioritizing face-to-face interactions. They emphasize early detection of internalizing symptoms to allow parents to intervene and mitigate potential negative effects.


---

## 58. Arrests in Louvre Heist Show Power of DNA Databases in Solving Crimes

**原文标题**: Arrests in Louvre Heist Show Power of DNA Databases in Solving Crimes

**原文链接**: [https://www.nytimes.com/2025/11/03/world/europe/louvre-heist-dna-databases.html](https://www.nytimes.com/2025/11/03/world/europe/louvre-heist-dna-databases.html)

无法访问文章链接。

---

## 59. OpenAI Signs $38B Cloud Computing Deal with Amazon

**原文标题**: OpenAI Signs $38B Cloud Computing Deal with Amazon

**原文链接**: [https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html](https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html)

无法访问文章链接。

---

## 60. 更新并关机不再重启电脑，25H2补丁修复数十年老Bug

**原文标题**: Update and shut down no longer restarts PC, 25H2 patch addresses decades-old bug

**原文链接**: [https://www.windowslatest.com/2025/11/02/update-and-shut-down-no-longer-restarts-pc-as-windows-11-25h2-patch-addresses-a-decades-old-bug/](https://www.windowslatest.com/2025/11/02/update-and-shut-down-no-longer-restarts-pc-as-windows-11-25h2-patch-addresses-a-decades-old-bug/)

本文探讨了Windows 10和11中一个长期存在的Bug，即选择“更新并关机”后，电脑经常重启而不是关机。这个困扰用户多年的问题终于在Windows 11 25H2 Build 26200.7019（或24H2上的26100.7019）中得到解决。

微软在2025年10月的可选更新(KB5067036)中确认了此修复，承认存在一个潜在问题阻止了预期的关机。虽然具体原因未正式披露，但作者推测这很可能是一个竞争条件或Windows Servicing Stack中的问题，影响了必要的离线服务阶段（“正在处理更新”屏幕）完成后“关闭电源”的任务。

文章强调了这个Bug造成的不便，尤其是在用户需要整夜关闭电脑时。该修复确保在选择“更新并关机”选项后，电脑在安装更新后正确关机。微软表示该修复将包含在11月11日的Patch Tuesday更新中。

---

## 61. 提高覆盖率的简单技巧：谎报信号强度

**原文标题**: Simple trick to increase coverage: Lying to users about signal strength

**原文链接**: [https://nickvsnetworking.com/simple-trick-to-increase-coverage-lying-to-users-about-signal-strength/](https://nickvsnetworking.com/simple-trick-to-increase-coverage-lying-to-users-about-signal-strength/)

文章揭示了安卓运营商配置管理器中一个隐藏设置，名为`KEY_INFLATE_SIGNAL_STRENGTH_BOOL`。启用此标志后，安卓操作系统会将显示给用户的信号强度人为地增加一格。作者指出，这实际上是在信号强度上欺骗用户。

作者提到，AT&T 和 Verizon 都在其网络上启用了此标志。虽然此设置的确切起源和理由尚不清楚，但作者批评了它的使用，认为这破坏了运营商和消费者之间的信任。作者进一步认为，这种欺骗行为，以及“假5G”指示器的实施，与运营商声称的网络优势相矛盾，并质疑在天线技术据称取得进步的情况下，这种操纵的必要性。作者认为，这些做法优先考虑的是感知覆盖范围，而非对网络基础设施的真正改进。

---

## 62. x86中断列表，又名“Ralf Brown中断列表”（2018）

**原文标题**: The x86 Interrupt List, aka “Ralf Brown's Interrupt List” (2018)

**原文链接**: [http://www.cs.cmu.edu/~ralf/files.html](http://www.cs.cmu.edu/~ralf/files.html)

Ralf Brown的网站托管了“x86中断列表”(RBIL)，这是一个关于IBM PC及其兼容机的中断调用、I/O端口、内存位置和远调用接口的综合信息集合。该列表涵盖了已记录和未记录的特性，并以一系列总计约8MB的ASCII文本文件形式提供。该网站提供列表各部分的下载链接、常见问题解答和一个DESQview专用摘录。

除了RBIL之外，该网站还提供几个开源项目，包括CMU-EBMT（一个基于实例的机器翻译系统）、ZipRec（一个ZIP压缩文件恢复程序）、LA-Strings（一个语言感知的“strings”实用程序）、CanvasLMS.py（一个用于Canvas LMS的Python库）和WordClus（一个用于在文本中查找相似单词集群的程序）。

该网站还提供编程库，如SPAWNO（C的spawn函数的交换替代品）、AMISLIB（一个用于编写自高加载TSR的库）和DV-GLUE（一个用于DESQview API的库）。可供下载的应用程序包括RBcomm（一个终端程序）、RBPCI（一个PCI设备信息程序）、DVdevload（一个用于DESQview的设备驱动程序加载器）、DVPtame（一个用于修改DESQview程序信息文件的程序）、RBdualVGA（用于使用两块VGA卡的程序）、RBkeyswap（一个用于交换CapsLock和左Ctrl键的TSR）和RBspeed（一个用于设置Intel Neptune芯片组速度的工具）。该网站还托管其他人编写的程序，如Epsilon的EEL代码和VT100相关的文本文件。

---

## 63. 荒谬的工作流：仅使用 Postgres 实现持久执行

**原文标题**: Absurd Workflows: Durable Execution with Just Postgres

**原文链接**: [https://lucumr.pocoo.org/2025/11/3/absurd-workflows/](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/)

生成摘要时出错

---

## 64. 欧特克的约翰·沃克在1991年解释惠普和IBM（2015年）

**原文标题**: Autodesk's John Walker Explained HP and IBM in 1991 (2015)

**原文链接**: [https://www.cringely.com/2015/06/03/autodesks-john-walker-explained-hp-and-ibm-in-1991/](https://www.cringely.com/2015/06/03/autodesks-john-walker-explained-hp-and-ibm-in-1991/)

本文分析了惠普和IBM在1991年面临的困境，并将其与Autodesk创始人约翰·沃克在“Autodesk的末日”备忘录中描述的Autodesk内部挑战相提并论。作者认为，惠普和IBM都面临衰退，原因是他们为了满足华尔街，过于关注短期利润率，往往牺牲了长期投资和创新。这种目光短浅的做法包括裁员等削减成本的措施，以及忽视对新产品开发的投资，最终导致销售额下降和容易受到竞争对手的攻击。

文章强调了沃克的核心论点：即优先考虑会计规则和利润维持，而不是战略愿景和员工反馈，会导致糟糕的决策。具体来说，文章解释了会计实务如何激励有害行为，例如为了短期利润而收购并扼杀小公司，或者因为销售记录方式而削减成功的营销计划。

作者以Autodesk为例，说明了一个成功的重大客户计划如何因会计账簿上“销售成本”的增加而自相矛盾地导致营销预算削减。文章批评惠普和IBM未能倾听员工的意见，扼杀创新，并将短期财务收益置于长期战略投资之上，最终导致恶性循环。中心论点是，虽然管理利润很重要，但不应以牺牲未来增长和创新为代价来决定战略决策。

---

## 65. Show HN: Serie – 终端内功能丰富的 Git 提交图

**原文标题**: Show HN: Serie – A rich Git commit graph in your terminal

**原文链接**: [https://github.com/lusingander/serie](https://github.com/lusingander/serie)

Serie 是一个终端 UI 应用程序，旨在提供比 `git log --graph` 更丰富的 Git 提交图浏览体验。它使用 iTerm2 和 kitty 等终端图像显示协议渲染提交图，从而提供更具视觉吸引力和信息量的提交历史表示。

该工具旨在简化 Git 日志浏览，而不会成为一个功能齐全的 Git 客户端或拥有复杂的 UI。它支持不同的提交排序算法（按时间顺序和拓扑顺序），可配置的图形宽度（单字符单元格或双字符单元格），并允许预加载图形图像以实现更平滑的滚动。

Serie 可以通过 Cargo、pacman（Arch Linux）、Homebrew、pkgin（NetBSD）等软件包管理器安装，也可以从发布版本部分下载预编译的二进制文件。

该应用程序提供可自定义的快捷键，用于导航、搜索和显示提交详细信息。用户还可以配置自定义命令，以在专用视图中显示输出，从而实现与 `git diff` 等外部工具的集成。配置选项涵盖诸如图形颜色、日期格式、UI 元素外观和快捷键等方面。

本文档详细介绍了配置、用户命令定义和受支持的终端，强调目前不支持终端复用器和 Sixel 图形。它还包括贡献指南，并提到该项目在 MIT 许可证下获得许可。

---

## 66. 反网络犯罪法正被武器化以压制新闻业。

**原文标题**: Anti-cybercrime laws are being weaponized to repress journalism

**原文链接**: [https://www.cjr.org/analysis/nigeria-pakistan-jordan-cybercrime-laws-journalism.php](https://www.cjr.org/analysis/nigeria-pakistan-jordan-cybercrime-laws-journalism.php)

生成摘要时出错

---

## 67. Tongyi DeepResearch – open-source 30B MoE Model that rivals OpenAI DeepResearch

**原文标题**: Tongyi DeepResearch – open-source 30B MoE Model that rivals OpenAI DeepResearch

**原文链接**: [https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/](https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/)

生成摘要时出错

---

## 68. At the end you use `git bisect`

**原文标题**: At the end you use `git bisect`

**原文链接**: [https://kevin3010.github.io/git/2025/11/02/At-the-end-you-use-git-bisect.html](https://kevin3010.github.io/git/2025/11/02/At-the-end-you-use-git-bisect.html)

生成摘要时出错

---

## 69. Cops on ketamine? Largely unregulated mental health treatment faces hurdles

**原文标题**: Cops on ketamine? Largely unregulated mental health treatment faces hurdles

**原文链接**: [https://kffhealthnews.org/news/article/ketamine-first-responders-depression-ptsd-trauma-unregulated-north-carolina/](https://kffhealthnews.org/news/article/ketamine-first-responders-depression-ptsd-trauma-unregulated-north-carolina/)

生成摘要时出错

---

## 70. Solar-powered QR reading postboxes being rolled out across UK

**原文标题**: Solar-powered QR reading postboxes being rolled out across UK

**原文链接**: [https://www.bbc.co.uk/news/articles/cgln72rgrero](https://www.bbc.co.uk/news/articles/cgln72rgrero)

生成摘要时出错

---

## 71. URLs are state containers

**原文标题**: URLs are state containers

**原文链接**: [https://alfy.blog/2025/10/31/your-url-is-your-state.html](https://alfy.blog/2025/10/31/your-url-is-your-state.html)

生成摘要时出错

---

## 72. In Defence of Digital ID

**原文标题**: In Defence of Digital ID

**原文链接**: [https://timharford.com/2025/10/in-defence-of-digital-id/](https://timharford.com/2025/10/in-defence-of-digital-id/)

生成摘要时出错

---

## 73. World’s largest heat pump under development in Germany

**原文标题**: World’s largest heat pump under development in Germany

**原文链接**: [https://www.pv-magazine.com/2025/10/31/worlds-largest-heat-pump-under-development-in-germany/](https://www.pv-magazine.com/2025/10/31/worlds-largest-heat-pump-under-development-in-germany/)

生成摘要时出错

---

## 74. How to build a solar powered electric oven

**原文标题**: How to build a solar powered electric oven

**原文链接**: [https://solar.lowtechmagazine.com/2025/10/how-to-build-a-solar-powered-electric-oven/](https://solar.lowtechmagazine.com/2025/10/how-to-build-a-solar-powered-electric-oven/)

生成摘要时出错

---

## 75. Notes by djb on using Fil-C

**原文标题**: Notes by djb on using Fil-C

**原文链接**: [https://cr.yp.to/2025/fil-c.html](https://cr.yp.to/2025/fil-c.html)

生成摘要时出错

---

## 76. Welcome to hell; please drive carefully

**原文标题**: Welcome to hell; please drive carefully

**原文链接**: [https://2earth.github.io/website/20251026.html](https://2earth.github.io/website/20251026.html)

生成摘要时出错

---

## 77. Mock – An API creation and testing utility: Examples

**原文标题**: Mock – An API creation and testing utility: Examples

**原文链接**: [https://dhuan.github.io/mock/latest/examples.html](https://dhuan.github.io/mock/latest/examples.html)

生成摘要时出错

---

## 78. Meta readies $25B bond sale as soaring AI costs trigger stock sell-off

**原文标题**: Meta readies $25B bond sale as soaring AI costs trigger stock sell-off

**原文链接**: [https://www.ft.com/content/120d2321-8382-4d74-ab48-f9ecb483c2a9](https://www.ft.com/content/120d2321-8382-4d74-ab48-f9ecb483c2a9)

生成摘要时出错

---

## 79. Linux gamers on Steam cross over the 3% mark

**原文标题**: Linux gamers on Steam cross over the 3% mark

**原文链接**: [https://www.gamingonlinux.com/2025/11/linux-gamers-on-steam-finally-cross-over-the-3-mark/](https://www.gamingonlinux.com/2025/11/linux-gamers-on-steam-finally-cross-over-the-3-mark/)

生成摘要时出错

---

## 80. Printed circuit board substrates derived from lignocellulose nanofibrils

**原文标题**: Printed circuit board substrates derived from lignocellulose nanofibrils

**原文链接**: [https://www.nature.com/articles/s41598-025-91653-1](https://www.nature.com/articles/s41598-025-91653-1)

生成摘要时出错

---

## 81. Scents of Arabia: Interdisciplinary approaches to ancient olfactory worlds

**原文标题**: Scents of Arabia: Interdisciplinary approaches to ancient olfactory worlds

**原文链接**: [https://www.scientificamerican.com/article/how-archaeology-is-reviving-the-smell-of-history/](https://www.scientificamerican.com/article/how-archaeology-is-reviving-the-smell-of-history/)

生成摘要时出错

---

## 82. Linux Tidbits and Collecting Pebbles

**原文标题**: Linux Tidbits and Collecting Pebbles

**原文链接**: [https://unixbhaskar.wordpress.com/2025/03/02/linux-tidbits-and-collecting-pebbles/](https://unixbhaskar.wordpress.com/2025/03/02/linux-tidbits-and-collecting-pebbles/)

生成摘要时出错

---

## 83. Rats filmed snatching bats from air

**原文标题**: Rats filmed snatching bats from air

**原文链接**: [https://www.science.org/content/article/rats-filmed-snatching-bats-air-first-time](https://www.science.org/content/article/rats-filmed-snatching-bats-air-first-time)

生成摘要时出错

---

## 84. LM8560, the eternal chip from the 1980 years

**原文标题**: LM8560, the eternal chip from the 1980 years

**原文链接**: [https://www.tycospages.com/other-themes/lm8560-the-eternal-chip-from-the-1980-years/](https://www.tycospages.com/other-themes/lm8560-the-eternal-chip-from-the-1980-years/)

生成摘要时出错

---

## 85. React-Native-Godot

**原文标题**: React-Native-Godot

**原文链接**: [https://github.com/borndotcom/react-native-godot](https://github.com/borndotcom/react-native-godot)

生成摘要时出错

---

## 86. Automatically Translating C to Rust

**原文标题**: Automatically Translating C to Rust

**原文链接**: [https://cacm.acm.org/research/automatically-translating-c-to-rust/](https://cacm.acm.org/research/automatically-translating-c-to-rust/)

生成摘要时出错

---

## 87. Working Past 100? In Japan, Some People Never Quit

**原文标题**: Working Past 100? In Japan, Some People Never Quit

**原文链接**: [https://www.nytimes.com/2025/11/01/world/asia/japan-work-job-retirement-centenarian.html](https://www.nytimes.com/2025/11/01/world/asia/japan-work-job-retirement-centenarian.html)

生成摘要时出错

---

## 88. When O3 is 2x slower than O2

**原文标题**: When O3 is 2x slower than O2

**原文链接**: [https://cat-solstice.github.io/test-pqueue/](https://cat-solstice.github.io/test-pqueue/)

生成摘要时出错

---

## 89. Backpropagation is a leaky abstraction (2016)

**原文标题**: Backpropagation is a leaky abstraction (2016)

**原文链接**: [https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b)

生成摘要时出错

---

## 90. UBCO study disproves the simulation hypothesis

**原文标题**: UBCO study disproves the simulation hypothesis

**原文链接**: [https://news.ok.ubc.ca/2025/10/30/ubco-study-debunks-the-idea-that-the-universe-is-a-computer-simulation/](https://news.ok.ubc.ca/2025/10/30/ubco-study-debunks-the-idea-that-the-universe-is-a-computer-simulation/)

生成摘要时出错

---

## 91. How the Mayans were able to accurately predict solar eclipses for centuries

**原文标题**: How the Mayans were able to accurately predict solar eclipses for centuries

**原文链接**: [https://phys.org/news/2025-10-mayans-accurately-solar-eclipses-centuries.html](https://phys.org/news/2025-10-mayans-accurately-solar-eclipses-centuries.html)

生成摘要时出错

---

## 92. The Authoritarian Stack: How Tech Billionaires Are Building a Post-Democratic US

**原文标题**: The Authoritarian Stack: How Tech Billionaires Are Building a Post-Democratic US

**原文链接**: [https://www.authoritarian-stack.info/](https://www.authoritarian-stack.info/)

生成摘要时出错

---

## 93. Why do AI models use so many em-dashes?

**原文标题**: Why do AI models use so many em-dashes?

**原文链接**: [https://www.seangoedecke.com/em-dashes/](https://www.seangoedecke.com/em-dashes/)

生成摘要时出错

---

## 94. Context engineering

**原文标题**: Context engineering

**原文链接**: [https://chrisloy.dev/post/2025/08/03/context-engineering](https://chrisloy.dev/post/2025/08/03/context-engineering)

生成摘要时出错

---

## 95. Java 中的原始类型，还是在盒子里用 Go

**原文标题**: Go Primitive in Java, or Go in a Box

**原文链接**: [https://donraab.medium.com/go-primitive-in-java-or-go-in-a-box-c26f5c6d7574](https://donraab.medium.com/go-primitive-in-java-or-go-in-a-box-c26f5c6d7574)

唐纳德·拉布的文章《在Java中使用基本类型，或装箱受限》倡导在Java中使用基本类型集合，以避免标准Java集合中装箱基本类型的性能开销。他批评了Java中缺乏原生基本类型集合支持，强调了为集合使用而装箱基本类型的低效性。

拉布推广Eclipse Collections作为一种解决方案，强调其对包括List、Set、Stack、Bag、LazyIterable、Map、Interval和String在内的所有八种Java基本类型的基本类型集合的全面支持。这些集合提供可变和不可变版本（Interval、String和LazyIterable除外）。

他指出了Eclipse Collections的设计考虑和权衡，例如由于其设计味道而故意省略`Boolean<V>Map`，并建议使用`Pair`代替。他还解决了将lambda表达式与基本类型集合集成的问题，展示了Eclipse Collections如何使用自定义函数式接口（Procedure、Function、Predicate）来克服基本类型缺乏泛型类型支持的问题。

文章最后鼓励Java开发者采用Eclipse Collections的基本类型集合，以实现更好的性能和内存效率。拉布强调，尽管等待未来Java增强功能（如Valhalla项目）可能很吸引人，但开发者可以利用现有的解决方案（如Eclipse Collections）立即“使用基本类型”。文章提供了博客、代码kata和书籍的链接，以供进一步学习。

---

## 96. Plumbing vs. Internet, Revisited

**原文标题**: Plumbing vs. Internet, Revisited

**原文链接**: [https://gwern.net/blog/2025/plumbing-vs-internet](https://gwern.net/blog/2025/plumbing-vs-internet)

生成摘要时出错

---

## 97. Visopsys: OS maintained by a single developer since 1997

**原文标题**: Visopsys: OS maintained by a single developer since 1997

**原文链接**: [https://visopsys.org/](https://visopsys.org/)

生成摘要时出错

---

## 98. AWS and OpenAI announce multi-year strategic partnership

**原文标题**: AWS and OpenAI announce multi-year strategic partnership

**原文链接**: [https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure](https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure)

生成摘要时出错

---

## 99. Amazon has launched a major global crackdown on Fire Stick piracy

**原文标题**: Amazon has launched a major global crackdown on Fire Stick piracy

**原文链接**: [https://www.the-sun.com/tech/15422622/amazon-fire-tv-stick-dodgy-apps-block-piracy-streaming/](https://www.the-sun.com/tech/15422622/amazon-fire-tv-stick-dodgy-apps-block-piracy-streaming/)

生成摘要时出错

---

## 100. Claude Code can debug low-level cryptography

**原文标题**: Claude Code can debug low-level cryptography

**原文链接**: [https://words.filippo.io/claude-debugging/](https://words.filippo.io/claude-debugging/)

生成摘要时出错

---

