# Hacker News 热门文章摘要 (2026-06-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Elixir v1.20 发布：现已成为渐进类型语言

**原文标题**: Elixir v1.20 released: now a gradually typed language

**原文链接**: [https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/)

Elixir v1.20 通过引入**渐进式、基于集合论的类型系统**，标志着该语言演进过程中的一个重要里程碑。此版本完成了第一个开发目标：在无需对现有代码进行任何更改或添加类型注解的情况下，对所有 Elixir 程序进行类型推导和类型检查。

该系统的设计目标是可靠、开发者友好且渐进的。它以 `dynamic()` 类型的独特实现为核心。与其他动态类型通常会忽略错误的语言不同，Elixir 的 `dynamic()` 类型利用了“兼容性”和“收窄”。这使得编译器能够随着变量的使用不断细化类型信息——例如识别特定的 Map 字段，或在守卫（guards）和 `case` 子句中收窄类型。因此，编译器能够识别出“经证实的 Bug”——即那些必定会导致运行时失败的类型违规，同时保持极低的误报率。

技术亮点包括：
*   **类型收窄：** 系统能从普通代码中恢复精确的类型信息，例如根据变量的访问方式推断其为 Map 或特定的基本类型。
*   **智能守卫与子句：** Elixir 现在可以通过复杂的守卫（包括取反和大小检查）推断类型，并在多个函数子句中细化类型。
*   **性能：** 针对多核机器进一步优化了编译时间。新的 `:module_definition` 选项允许开发者在构建过程中选择编译执行或解释执行，以潜在地提高速度。

展望未来，团队将继续研究递归类型和参数化类型。一旦这些复杂结构的性能和实现障碍得到解决，正式的类型签名和带类型的结构体（typed structs）将在未来的版本中引入。

---

## 2. Gemma 4 12B：统一的无编码器多模态模型

**原文标题**: Gemma 4 12B: A unified, encoder-free multimodal model

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

Google DeepMind 推出了 **Gemma 4 12B**，这是一款中型多模态模型，旨在将先进的“智能体”智能引入消费级硬件。该 12B 版本定位介于侧重边缘端的 E4B 和较大的 26B 混合专家（MoE）模型之间，经过优化，可在内存低至 16GB 的笔记本电脑上本地运行。

**核心技术创新**
Gemma 4 12B 的核心特色是其**无编码器架构（encoder-free architecture）**。与使用独立编码器处理不同输入的传统多模态模型不同，该模型直接在 LLM 主干网络中处理视觉和音频。
*   **视觉：** 用轻量级嵌入模块取代了沉重的编码器。
*   **音频：** 将原始音频信号直接投影到文本 Token 空间，使其成为首个具有原生音频支持的中型 Gemma 模型。
这种精简设计在不牺牲推理能力的情况下，显著降低了延迟和内存占用。

**性能与速度**
尽管体积更小，Gemma 4 12B 提供的推理能力已接近 26B MoE 模型。为了确保高速性能，它包含了**多 Token 预测（MTP）草拟器**，可降低推理延迟，使其成为实时智能体工作流的理想选择。

**易用性与生态系统**
该模型基于 **Apache 2.0 许可证**发布，对开发者社区高度开放。它兼容 Hugging Face、llama.cpp、Ollama 和 vLLM 等流行工具。为了进一步支持开发者，Google 推出了 **Gemma Skills Repository**，这是一个专门的技能库，旨在帮助构建复杂的 AI 智能体。

Gemma 4 12B 现已可在 Hugging Face 和 Kaggle 上下载，并可通过 Google Cloud 部署，或使用各种移动和桌面 AI 框架在本地运行。

---

## 3. I was recently diagnosed with anti-NMDA receptor encephalitis

**原文标题**: I was recently diagnosed with anti-NMDA receptor encephalitis

**原文链接**: [https://burntsushi.net/encephalitis/](https://burntsushi.net/encephalitis/)

生成摘要时出错

---

## 4. ESP32-S31

**原文标题**: ESP32-S31

**原文链接**: [https://www.espressif.com/en/products/socs/esp32-s31](https://www.espressif.com/en/products/socs/esp32-s31)

该文本是无线通信解决方案领导者**乐鑫科技 (Espressif Systems)** 的全面站点地图及产品导航指南。它概述了公司广泛的生态系统，并将其划分为硬件、软件、云服务和行业专用解决方案四大类。

**核心信息：**

*   **硬件产品组合：** 文中列出了广泛的 SoC（系统级芯片）、模组及开发套件。这包括核心的 **ESP32** 和 **ESP8266** 系列，以及较新的迭代版本，如 **ESP32-S3**、**S 系列**（S2、S3）、**C 系列**（C2、C3、C5、C6、C61）、**H 系列**（H2、H4）和 **P 系列**（P4）。
*   **软件与 SDK：** 该生态系统由 **ESP-IDF**（物联网开发框架）以及针对人工智能（ESP-SR、ESP-WHO）、多媒体（ESP-ADF、ESP-GMF）和连接协议（如 **Matter**、**ESP-BLE-MESH** 和 **ESP-NOW**）的专业 SDK 提供支持。此外，它还强调了对 **Arduino** 和 **Zephyr** 等第三方生态系统的兼容性。
*   **云与服务：** 核心产品包括端到端物联网云解决方案 **ESP RainMaker**，以及远程诊断与可观测性平台 **ESP Insights**。
*   **针对性解决方案：** 乐鑫为 **AI 解决方案**（大语言模型和聊天代理）、**HMI**（智能显示屏）、**智能感知**（Wi-Fi CSI 和 FTM）及安全领域提供了专门的框架。
*   **支持与社区：** 该平台提供详尽的技术文档、证书、开发者门户、教育资源，以及产品的长期供货承诺。

总之，该文本旨在作为开发者和企业了解乐鑫软硬件集成环境的指南，旨在促进 AIoT（人工智能物联网）应用的开发。

---

## 5. 达芬奇 21

**原文标题**: DaVinci Resolve 21

**原文链接**: [https://www.blackmagicdesign.com/products/davinciresolve/whatsnew](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew)

DaVinci Resolve 21 在其后期制作套件中引入了重大突破，核心亮点包括全新的 **Photo（照片）页面**以及一系列扩展的 AI 驱动工具。

**静态摄影集成**
DaVinci Resolve 首次将其专业的调色工具引入静态摄影领域。Photo 页面支持节点式编辑、RAW 调整，以及索尼和佳能相机的直接联机拍摄。摄影师现在可以在静态图像上使用好莱坞标准的初级调色控制、AI 魔术遮罩和 Resolve FX。

**先进 AI 神经引擎**
此次更新利用 DaVinci AI 神经引擎实现了多项新功能：
*   **IntelliSearch（智能搜索）：** 允许用户根据人脸、物体或特定的语音关键词搜索素材片段。
*   **音频与文本：** 包含用于高质量旁白的 AI 语音生成器，以及可从场记板自动提取元数据的 AI Slate ID。
*   **视觉增强：** Face Age Transformer（人脸年龄转换器）、Face Reshaper（人脸重塑器）、CineFocus（电影焦外，用于景深控制）和 UltraSharpen（超强锐化）等工具提供了高端的修图与图像修复能力。

**工作流增强**
*   **剪辑与快编：** 现支持 Lottie 动画、HTML 图形及改进的关键帧功能。Fusion 特效也可直接在剪辑时间线上进行调整。
*   **调色：** MultiMaster 裁切管理器支持同时交付 HDR/SDR 格式，同时节点编辑器新增了简化的图层列表视图。
*   **Fusion：** 集成了 Krokodove VFX 库和音频驱动的动画工具。
*   **Fairlight：** 通过轨道文件夹、6 波段剪辑均衡器以及自动均衡器/电平匹配功能提升了音频管理效率。

**下一代工程技术**
第 21 版针对苹果 M 系列和骁龙 X Elite 芯片进行了优化。它引入了用于 VR 的 Apple Immersive（苹果沉浸式）注视点渲染，并扩展了对 3D 视频编码 (MV-HEVC) 及 VR180/360 工作流的支持，使该软件始终处于沉浸式媒体技术的前沿。

---

## 6. Gooey：Zig 语言的 GPU 加速 UI 框架

**原文标题**: Gooey: A GPU-accelerated UI framework for Zig

**原文链接**: [https://github.com/duanebester/gooey](https://github.com/duanebester/gooey)

**Gooey** 是一个为 Zig 编程语言（v0.16.0+）设计的 GPU 加速 UI 框架，支持 macOS (Metal)、Linux (Vulkan/Wayland) 和 Web (WASM/WebGPU)。它秉持**零依赖**的设计理念，仅链接至平台系统库，并内置了如 Objective-C 等必要的绑定。

### 核心技术特性
*   **GPU 渲染：** 利用 Metal 和 Vulkan，支持 MSAA 抗锯齿及自定义着色器。
*   **声明式 UI：** 采用基于组件的系统，提供类 Flexbox 的布局原语（`ui.box`、`ui.stack`）。
*   **纯状态模式：** 应用逻辑与 UI 完全分离，使状态变更在无需图形环境的情况下即可进行完整的单元测试。
*   **保留模式与丰富组件：** 包含 `TextInput`、`Checkbox` 和 `Scroll` 容器等标准组件，以及虚拟列表（可处理 1 万个以上列表项）、拖放操作和“液态玻璃”透明效果等高级特性。
*   **操作系统集成：** 提供原生文件对话框、剪贴板支持、国际化文本 IME 输入以及辅助功能（VoiceOver、Orca、ARIA）。

### 架构与并发
Gooey 将关注点分离为管理状态与焦点的 **Cx** (Context) 以及处理布局的 **ui**。它利用多种处理器类型（`update`、`command`、`defer`）来管理状态变更和框架交互。为保持高性能，这些处理器的参数被限制在 8 字节以内，以确保零分配存储。

对于重计算或 I/O 任务，Gooey 与 Zig 的 `std.Io` 栈集成。后台任务通过类型化的有界队列与 UI 线程通信。这种“推送”模型确保后台工作永远不会直接触及 UI 状态，从而消除了对复杂锁定机制的需求，并确保了界面的流畅响应。

---

## 7. 人工智能没有意识——特德·姜

**原文标题**: Artificial intelligence is not conscious – Ted Chiang

**原文链接**: [https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/)

In this article, Ted Chiang argues that large language models (LLMs) like Anthropic’s Claude are not conscious, despite the anthropomorphic language used by their creators. Chiang contends that LLMs are essentially sophisticated "sentence-continuation" machines that engage in a form of role-play. Whether an LLM generates a dialogue between historical figures or a "helpful chatbot," it is merely predicting the next word based on statistical patterns, not expressing subjective experience. 

Chiang asserts that we mistake linguistic fluency for consciousness because humans are conditioned to read intention into grammatical sentences. He compares LLM output to a "deepfake," noting that it is far easier to simulate the appearance of conversation than to build a sentient mind. To be truly conscious, Chiang argues, a program would require a body, sense organs, and the ability to navigate the world—solving foundational problems of survival, social interaction, and tool use seen in animals long before achieving language. 

The author concludes that jumping straight to "grammatical sentences" without these preceding steps is like claiming to have reached another star system without first landing on the moon. Without physical grounding and genuine desires, LLMs remain ungrounded tools. Consequently, documents like Claude’s “constitution” should be viewed as "character sheets" for a fictional persona rather than moral frameworks for a sentient being. Chiang warns that confusing fluency with agency risks assigning responsibility to software instead of the humans who deploy it.

---

## 8. 无需物理接触，利用扬声器即可入侵你的电脑

**原文标题**: Hacking your PC using your speaker without ever touching it

**原文链接**: [https://blog.nns.ee/2026/06/03/katana-badusb/](https://blog.nns.ee/2026/06/03/katana-badusb/)

本文详细介绍了对 Creative Sound Blaster Katana V2X 回音壁的安全研究，揭示了允许远程攻击者在无需物理接触的情况下入侵连接 PC 的漏洞。

**主要发现：**
*   **协议实现不安全：** 该扬声器使用 Creative 传输协议 (CTP) 进行配置和固件更新。虽然 USB 接口需要挑战-响应认证，但蓝牙低功耗 (BLE) 接口则不需要。这使得蓝牙范围内（约 15 米）的任何攻击者都可以在无需配对的情况下连接并发布管理命令。
*   **缺乏固件完整性检查：** 该设备对固件更新缺乏数字签名验证。它仅检查基本的 SHA-256 校验和，而这很容易被修改。因此，设备会接受并执行未经授权的修改版固件。

**漏洞利用：**
通过串联这些漏洞，研究人员演示了一种远程攻击：
1.  **远程刷机：** 攻击者通过 BLE 连接并上传自定义固件镜像。
2.  **HID 模拟 (Rubber Ducky)：** 研究人员修改了固件以重新定义扬声器的 USB 描述符。虽然它通常作为“消费者控制”设备（用于调节音量），但补丁增加了“键盘”功能。
3.  **命令执行：** 启动恶意固件后，扬声器充当虚拟键盘，并向连接的 PC “键入”任意命令，从而有效地将回音壁转变为远程“Rubber Ducky”工具。

**修复与响应：**
研究人员通过 SingCERT 向 Creative 报告了这些发现。根据文章，Creative 认为这不属于网络安全风险，并拒绝发布补丁。为了保护用户，研究人员开发了一个非官方的 “v2x-patcher” 工具，该工具禁用了蓝牙上的 CTP，以牺牲移动应用功能为代价，阻止了远程更新攻击向量。

---

## 9. Stop Killing Games

**原文标题**: Stop Killing Games

**原文链接**: [https://jxself.org/stop-killing-games.shtml](https://jxself.org/stop-killing-games.shtml)

生成摘要时出错

---

## 10. A Post-Quantum Future for Let's Encrypt

**原文标题**: A Post-Quantum Future for Let's Encrypt

**原文链接**: [https://letsencrypt.org/2026/06/03/pq-certs](https://letsencrypt.org/2026/06/03/pq-certs)

生成摘要时出错

---

## 11. Uber's $1,500/month AI limit is a useful signal for AI tool pricing

**原文标题**: Uber's $1,500/month AI limit is a useful signal for AI tool pricing

**原文链接**: [https://simonwillison.net/2026/Jun/3/uber-caps-usage/](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

生成摘要时出错

---

## 12. Skyvern (YC S23) Is Hiring Open-Source Loving DevRel Engineers

**原文标题**: Skyvern (YC S23) Is Hiring Open-Source Loving DevRel Engineers

**原文链接**: [https://www.ycombinator.com/companies/skyvern/jobs/1qRTlVx-founding-developer-marketing-open-source-ai](https://www.ycombinator.com/companies/skyvern/jobs/1qRTlVx-founding-developer-marketing-open-source-ai)

生成摘要时出错

---

## 13. Rootshell: A new E2EE email service hosted in Iceland

**原文标题**: Rootshell: A new E2EE email service hosted in Iceland

**原文链接**: [https://rootshell.is](https://rootshell.is)

生成摘要时出错

---

## 14. Angular v22

**原文标题**: Angular v22

**原文链接**: [https://blog.angular.dev/announcing-angular-v22-c52bb83a4664](https://blog.angular.dev/announcing-angular-v22-c52bb83a4664)

生成摘要时出错

---

## 15. Embryos shape their limbs: a key discovery of "genetic brakes"

**原文标题**: Embryos shape their limbs: a key discovery of "genetic brakes"

**原文链接**: [https://nouvelles.umontreal.ca/en/article/2026/06/02/how-embryos-shape-their-limbs-a-key-discovery-of-genetic-brakes](https://nouvelles.umontreal.ca/en/article/2026/06/02/how-embryos-shape-their-limbs-a-key-discovery-of-genetic-brakes)

生成摘要时出错

---

## 16. Fluid Simulation for Dummies

**原文标题**: Fluid Simulation for Dummies

**原文链接**: [https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html](https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html)

生成摘要时出错

---

## 17. Every Byte Matters

**原文标题**: Every Byte Matters

**原文链接**: [https://fzakaria.com/2026/06/01/every-byte-matters](https://fzakaria.com/2026/06/01/every-byte-matters)

生成摘要时出错

---

## 18. PlayStation Architecture

**原文标题**: PlayStation Architecture

**原文链接**: [https://www.copetti.org/writings/consoles/playstation/](https://www.copetti.org/writings/consoles/playstation/)

生成摘要时出错

---

## 19. Meta workers can opt out of being tracked at work up to 30 min

**原文标题**: Meta workers can opt out of being tracked at work up to 30 min

**原文链接**: [https://www.bbc.com/news/articles/c93x0k194yno](https://www.bbc.com/news/articles/c93x0k194yno)

生成摘要时出错

---

## 20. Mathematicians issue warning as AI rapidly gains ground

**原文标题**: Mathematicians issue warning as AI rapidly gains ground

**原文链接**: [https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)

生成摘要时出错

---

## 21. Brume is a 24-voice multi-timbral desktop synth for the CM5

**原文标题**: Brume is a 24-voice multi-timbral desktop synth for the CM5

**原文链接**: [https://brume.aftertone.co/](https://brume.aftertone.co/)

生成摘要时出错

---

## 22. What I've learned about the trombone

**原文标题**: What I've learned about the trombone

**原文链接**: [http://bryanhu.com/blog/posts/what-ive-learned-about-the-trombone/](http://bryanhu.com/blog/posts/what-ive-learned-about-the-trombone/)

生成摘要时出错

---

## 23. Bot vs human traffic

**原文标题**: Bot vs human traffic

**原文链接**: [https://radar.cloudflare.com/traffic#bot-vs-human](https://radar.cloudflare.com/traffic#bot-vs-human)

生成摘要时出错

---

## 24. New Texas Instruments 5532 chips are not the 5532's we've used for decades

**原文标题**: New Texas Instruments 5532 chips are not the 5532's we've used for decades

**原文链接**: [https://groupdiy.com/threads/the-new-ti-5532-chips-are-not-5532s-weve-used-for-decades.93707/](https://groupdiy.com/threads/the-new-ti-5532-chips-are-not-5532s-weve-used-for-decades.93707/)

生成摘要时出错

---

## 25. Show HN: Edsger – A handwritten Clojure REPL for the reMarkable 2

**原文标题**: Show HN: Edsger – A handwritten Clojure REPL for the reMarkable 2

**原文链接**: [https://handwritten.danieljanus.pl/2026-06-01-edsger.html](https://handwritten.danieljanus.pl/2026-06-01-edsger.html)

生成摘要时出错

---

## 26. 32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building

**原文标题**: 32GB of DDR5 now costs $375 – AI shortage continues to squeeze PC building

**原文链接**: [https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

生成摘要时出错

---

## 27. GoPro warned it may not survive

**原文标题**: GoPro warned it may not survive

**原文链接**: [https://thenextweb.com/news/gopro-going-concern-ai-memory-crisis-default](https://thenextweb.com/news/gopro-going-concern-ai-memory-crisis-default)

生成摘要时出错

---

## 28. MacBook Neo Is So Popular That Apple Doubled Production

**原文标题**: MacBook Neo Is So Popular That Apple Doubled Production

**原文链接**: [https://www.macrumors.com/2026/06/03/macbook-neo-production-doubled-says-kuo/](https://www.macrumors.com/2026/06/03/macbook-neo-production-doubled-says-kuo/)

生成摘要时出错

---

## 29. Nabokov's pale fire: the lost 'father of all hypertext demos'? (2011)

**原文标题**: Nabokov's pale fire: the lost 'father of all hypertext demos'? (2011)

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/1995966.1996008](https://dl.acm.org/doi/pdf/10.1145/1995966.1996008)

生成摘要时出错

---

## 30. MacBook Neo Is So Popular That Apple Doubled Production

**原文标题**: MacBook Neo Is So Popular That Apple Doubled Production

**原文链接**: [https://www.macrumors.com/2026/06/03/macbook-neo-production-doubled-says-kuo/](https://www.macrumors.com/2026/06/03/macbook-neo-production-doubled-says-kuo/)

生成摘要时出错

---

## 31. How turkey hacked the hair-transplant industry

**原文标题**: How turkey hacked the hair-transplant industry

**原文链接**: [https://www.wired.com/story/how-turkey-hacked-the-hair-transplant-industry/](https://www.wired.com/story/how-turkey-hacked-the-hair-transplant-industry/)

生成摘要时出错

---

## 32. Use your Nvidia GPU's VRAM as swap space on Linux

**原文标题**: Use your Nvidia GPU's VRAM as swap space on Linux

**原文链接**: [https://github.com/c0dejedi/nbd-vram](https://github.com/c0dejedi/nbd-vram)

生成摘要时出错

---

## 33. A blueprint for democratic governance of frontier AI

**原文标题**: A blueprint for democratic governance of frontier AI

**原文链接**: [https://openai.com/index/frontier-safety-blueprint/](https://openai.com/index/frontier-safety-blueprint/)

生成摘要时出错

---

## 34. Sixteen Kids and a Hit Man (2024)

**原文标题**: Sixteen Kids and a Hit Man (2024)

**原文链接**: [https://nymag.com/intelligencer/article/christopher-pence-corderos-fbi-dark-web-hit-man.html](https://nymag.com/intelligencer/article/christopher-pence-corderos-fbi-dark-web-hit-man.html)

生成摘要时出错

---

## 35. Show HN: I reverse-engineered the world maps of Test Drive III (1990 DOS game)

**原文标题**: Show HN: I reverse-engineered the world maps of Test Drive III (1990 DOS game)

**原文链接**: [https://github.com/s-macke/Test-Drive-3-Maps](https://github.com/s-macke/Test-Drive-3-Maps)

生成摘要时出错

---

## 36. I built a ceiling projection mapping of the planes flying over my house

**原文标题**: I built a ceiling projection mapping of the planes flying over my house

**原文链接**: [https://old.reddit.com/r/nextfuckinglevel/comments/1tvmcin/i_live_in_the_take_off_path_of_sfo_and_built_a/](https://old.reddit.com/r/nextfuckinglevel/comments/1tvmcin/i_live_in_the_take_off_path_of_sfo_and_built_a/)

生成摘要时出错

---

## 37. Show HN: Rscrypto, pure-Rust crypto with industry leading public benches

**原文标题**: Show HN: Rscrypto, pure-Rust crypto with industry leading public benches

**原文链接**: [https://github.com/loadingalias/rscrypto](https://github.com/loadingalias/rscrypto)

生成摘要时出错

---

## 38. The Public Should Own Half of the Big A.I. Companies

**原文标题**: The Public Should Own Half of the Big A.I. Companies

**原文链接**: [https://www.sanders.senate.gov/op-eds/the-public-should-own-half-of-the-big-a-i-companies/](https://www.sanders.senate.gov/op-eds/the-public-should-own-half-of-the-big-a-i-companies/)

生成摘要时出错

---

## 39. Shopify outage [resolved]

**原文标题**: Shopify outage [resolved]

**原文链接**: [https://www.shopifystatus.com](https://www.shopifystatus.com)

生成摘要时出错

---

## 40. Show HN: Ideogram 4.0 – open-weight 9.3B text-to-image model

**原文标题**: Show HN: Ideogram 4.0 – open-weight 9.3B text-to-image model

**原文链接**: [https://github.com/ideogram-oss/ideogram4](https://github.com/ideogram-oss/ideogram4)

生成摘要时出错

---

## 41. U of T researchers demonstrate AI worm could target any online device

**原文标题**: U of T researchers demonstrate AI worm could target any online device

**原文链接**: [https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device](https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device)

生成摘要时出错

---

## 42. 1-Click GitHub Token Stealing via a VSCode Bug

**原文标题**: 1-Click GitHub Token Stealing via a VSCode Bug

**原文链接**: [https://blog.ammaraskar.com/github-token-stealing/](https://blog.ammaraskar.com/github-token-stealing/)

生成摘要时出错

---

## 43. REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image

**原文标题**: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image

**原文链接**: [https://shirleymaxx.github.io/REST3D/](https://shirleymaxx.github.io/REST3D/)

生成摘要时出错

---

## 44. The Unreasonable Redundancy of Nature's Protein Folds

**原文标题**: The Unreasonable Redundancy of Nature's Protein Folds

**原文链接**: [https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/](https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/)

生成摘要时出错

---

## 45. AI outperforms law professors in Stanford Law study

**原文标题**: AI outperforms law professors in Stanford Law study

**原文链接**: [https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)

生成摘要时出错

---

## 46. SpaceX's IPO is a disaster waiting to happen for your pension fund

**原文标题**: SpaceX's IPO is a disaster waiting to happen for your pension fund

**原文链接**: [https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/](https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/)

生成摘要时出错

---

## 47. Pluto.jl 1.0 release – reactive notebook for Julia

**原文标题**: Pluto.jl 1.0 release – reactive notebook for Julia

**原文链接**: [https://discourse.julialang.org/t/pluto-1-0-release/137296](https://discourse.julialang.org/t/pluto-1-0-release/137296)

生成摘要时出错

---

## 48. DIY Bipedal Robot Used Pneumatic "Air-Muscles" Instead of Motors

**原文标题**: DIY Bipedal Robot Used Pneumatic "Air-Muscles" Instead of Motors

**原文链接**: [https://spectrum.ieee.org/shadow-walker-biped-humanoid-robot](https://spectrum.ieee.org/shadow-walker-biped-humanoid-robot)

生成摘要时出错

---

## 49. I believe a whole generation of developers miss how open source used to work

**原文标题**: I believe a whole generation of developers miss how open source used to work

**原文链接**: [https://twitter.com/mitsuhiko/status/2062181646804152626](https://twitter.com/mitsuhiko/status/2062181646804152626)

生成摘要时出错

---

## 50. Roku LT Operating System open source distribution

**原文标题**: Roku LT Operating System open source distribution

**原文链接**: [https://blog.roku.com/developer/roku-lt-os](https://blog.roku.com/developer/roku-lt-os)

生成摘要时出错

---

## 51. A Visual Guide to Gemma 4 12B

**原文标题**: A Visual Guide to Gemma 4 12B

**原文链接**: [https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b)

生成摘要时出错

---

## 52. Tuta has joined Euro-Office and will now contribute to its codebase

**原文标题**: Tuta has joined Euro-Office and will now contribute to its codebase

**原文链接**: [https://www.neowin.net/news/tuta-has-joined-euro-office-and-will-now-contribute-to-its-codebase/](https://www.neowin.net/news/tuta-has-joined-euro-office-and-will-now-contribute-to-its-codebase/)

生成摘要时出错

---

## 53. Leiden Declaration on Artificial Intelligence and Mathematics

**原文标题**: Leiden Declaration on Artificial Intelligence and Mathematics

**原文链接**: [https://leidendeclaration.ai/](https://leidendeclaration.ai/)

生成摘要时出错

---

## 54. Capstone – multi-platform, multi-architecture disassembly framework

**原文标题**: Capstone – multi-platform, multi-architecture disassembly framework

**原文链接**: [https://www.capstone-engine.org/](https://www.capstone-engine.org/)

生成摘要时出错

---

## 55. Why Kernel-Level eBPF Is Replacing User-Space Agents for Security Observability

**原文标题**: Why Kernel-Level eBPF Is Replacing User-Space Agents for Security Observability

**原文链接**: [https://www.infoq.com/articles/ebpf-for-security-observability/](https://www.infoq.com/articles/ebpf-for-security-observability/)

生成摘要时出错

---

## 56. Thomas Mann: Goethe Heartened by Panama (As Suez for English, or Danube-Rhine)

**原文标题**: Thomas Mann: Goethe Heartened by Panama (As Suez for English, or Danube-Rhine)

**原文链接**: [https://yalereview.org/article/thomas-mann-goethe](https://yalereview.org/article/thomas-mann-goethe)

生成摘要时出错

---

## 57. How we index images for RAG

**原文标题**: How we index images for RAG

**原文链接**: [https://www.kapa.ai/blog/how-we-index-images-for-rag](https://www.kapa.ai/blog/how-we-index-images-for-rag)

生成摘要时出错

---

## 58. HP re-releases classic computer science calculator: The HP-16C

**原文标题**: HP re-releases classic computer science calculator: The HP-16C

**原文链接**: [https://hpcalcs.com/product/hp-16c-collectors-edition/](https://hpcalcs.com/product/hp-16c-collectors-edition/)

生成摘要时出错

---

## 59. Uber cuts 23% of people division as new president takes over

**原文标题**: Uber cuts 23% of people division as new president takes over

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-03/uber-cuts-23-of-people-division-as-new-president-takes-charge](https://www.bloomberg.com/news/articles/2026-06-03/uber-cuts-23-of-people-division-as-new-president-takes-charge)

生成摘要时出错

---

## 60. German startup advancing compressor-free electrocaloric heat pump technology

**原文标题**: German startup advancing compressor-free electrocaloric heat pump technology

**原文链接**: [https://www.pv-magazine.com/2026/06/02/german-startup-advancing-compressor-free-electrocaloric-heat-pump-technology/](https://www.pv-magazine.com/2026/06/02/german-startup-advancing-compressor-free-electrocaloric-heat-pump-technology/)

生成摘要时出错

---

## 61. QBE – Compiler Backend – 1.3

**原文标题**: QBE – Compiler Backend – 1.3

**原文链接**: [https://c9x.me/compile/release/qbe-1.3.html](https://c9x.me/compile/release/qbe-1.3.html)

生成摘要时出错

---

## 62. The Florida woman catfishing America's political class

**原文标题**: The Florida woman catfishing America's political class

**原文链接**: [https://www.politico.com/news/2026/06/02/bumble-new-jersey-gamble-catfishing-crowder-00941061](https://www.politico.com/news/2026/06/02/bumble-new-jersey-gamble-catfishing-crowder-00941061)

生成摘要时出错

---

## 63. UN calculates nation-sized environmental footprints for AI and data centers

**原文标题**: UN calculates nation-sized environmental footprints for AI and data centers

**原文链接**: [https://apnews.com/article/ai-data-centers-environment-climate-footprint-a792f184a9f2833b5388dbae8b41ca95](https://apnews.com/article/ai-data-centers-environment-climate-footprint-a792f184a9f2833b5388dbae8b41ca95)

生成摘要时出错

---

## 64. Show HN: Live breath detection and biofeedback from a phone microphone

**原文标题**: Show HN: Live breath detection and biofeedback from a phone microphone

**原文链接**: [https://github.com/shiihaa-app/shiihaa-breath-detection](https://github.com/shiihaa-app/shiihaa-breath-detection)

生成摘要时出错

---

## 65. The advertising cartel coming to your web browser

**原文标题**: The advertising cartel coming to your web browser

**原文链接**: [https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/](https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/)

生成摘要时出错

---

## 66. Age verification for social media, the beginning of the end for a free internet?

**原文标题**: Age verification for social media, the beginning of the end for a free internet?

**原文链接**: [https://mullvad.net/en/blog/age-verification-for-social-media-the-beginning-of-the-end-for-a-free-internet](https://mullvad.net/en/blog/age-verification-for-social-media-the-beginning-of-the-end-for-a-free-internet)

生成摘要时出错

---

## 67. Bringing Up DeepSeek-V4-Flash on AMD MI300X

**原文标题**: Bringing Up DeepSeek-V4-Flash on AMD MI300X

**原文链接**: [https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/)

生成摘要时出错

---

## 68. CSS-Native Parallax Effect

**原文标题**: CSS-Native Parallax Effect

**原文链接**: [https://dan-webnotes.com/posts/2026-06-02-css-native-parallax-effect/](https://dan-webnotes.com/posts/2026-06-02-css-native-parallax-effect/)

生成摘要时出错

---

## 69. Amazon's search bar will invent AI-generated products you can't buy

**原文标题**: Amazon's search bar will invent AI-generated products you can't buy

**原文链接**: [https://www.theverge.com/tech/942547/amazon-search-bar-ai-images](https://www.theverge.com/tech/942547/amazon-search-bar-ai-images)

生成摘要时出错

---

## 70. Show HN: Instant DBML Schema to Database Diagram PNG Tool

**原文标题**: Show HN: Instant DBML Schema to Database Diagram PNG Tool

**原文链接**: [https://vibe-schema.com/dbml-to-png](https://vibe-schema.com/dbml-to-png)

生成摘要时出错

---

## 71. Man out of Time: The travels and ecstasies of a Russian aesthete

**原文标题**: Man out of Time: The travels and ecstasies of a Russian aesthete

**原文链接**: [https://lareviewofbooks.org/article/evocations-italy-pavel-muratov-russian-travel-modernism-art/](https://lareviewofbooks.org/article/evocations-italy-pavel-muratov-russian-travel-modernism-art/)

生成摘要时出错

---

## 72. GitHub Copilot App

**原文标题**: GitHub Copilot App

**原文链接**: [https://github.com/features/preview/github-app](https://github.com/features/preview/github-app)

生成摘要时出错

---

## 73. Why Janet? (2023)

**原文标题**: Why Janet? (2023)

**原文链接**: [https://ianthehenry.com/posts/why-janet/](https://ianthehenry.com/posts/why-janet/)

生成摘要时出错

---

## 74. Economists Are Obsessed with "Job Creation." How about Less Work? (2017)

**原文标题**: Economists Are Obsessed with "Job Creation." How about Less Work? (2017)

**原文链接**: [https://evonomics.com/less-work-job-creation-peter-gray/](https://evonomics.com/less-work-job-creation-peter-gray/)

生成摘要时出错

---

## 75. Can the stockmarket swallow Anthropic, SpaceX and OpenAI?

**原文标题**: Can the stockmarket swallow Anthropic, SpaceX and OpenAI?

**原文链接**: [https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai](https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai)

生成摘要时出错

---

## 76. Show HN: Phive, a Gomoku-like game to play with friends or solo

**原文标题**: Show HN: Phive, a Gomoku-like game to play with friends or solo

**原文链接**: [https://phive.app](https://phive.app)

生成摘要时出错

---

## 77. Love systemd timers

**原文标题**: Love systemd timers

**原文链接**: [https://blog.tjll.net/you-dont-love-systemd-timers-enough/](https://blog.tjll.net/you-dont-love-systemd-timers-enough/)

生成摘要时出错

---

## 78. Loading Sega Games Off a Vinyl Record [video]

**原文标题**: Loading Sega Games Off a Vinyl Record [video]

**原文链接**: [https://www.youtube.com/watch?v=c744iD0_fWU](https://www.youtube.com/watch?v=c744iD0_fWU)

生成摘要时出错

---

## 79. What appear to be biochemical processes may be a natural feature of geology

**原文标题**: What appear to be biochemical processes may be a natural feature of geology

**原文链接**: [https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/](https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/)

生成摘要时出错

---

## 80. If AI data centers are so great, why are they being built in secret?

**原文标题**: If AI data centers are so great, why are they being built in secret?

**原文链接**: [https://www.thebrockovichreport.com/p/if-data-centers-are-so-great-why](https://www.thebrockovichreport.com/p/if-data-centers-are-so-great-why)

生成摘要时出错

---

## 81. CQL: Categorical Databases

**原文标题**: CQL: Categorical Databases

**原文链接**: [https://categoricaldata.net/](https://categoricaldata.net/)

生成摘要时出错

---

## 82. Show HN: RePlaya – self-hosted browser session replay with live tailing

**原文标题**: Show HN: RePlaya – self-hosted browser session replay with live tailing

**原文链接**: [https://github.com/s2-streamstore/replaya](https://github.com/s2-streamstore/replaya)

生成摘要时出错

---

## 83. Codex Discovered a Hidden HTTP/2 Bomb

**原文标题**: Codex Discovered a Hidden HTTP/2 Bomb

**原文链接**: [https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb](https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb)

生成摘要时出错

---

## 84. Lean Inference: Lean Manufacturing Principles Applied to AI

**原文标题**: Lean Inference: Lean Manufacturing Principles Applied to AI

**原文链接**: [https://neurometric.substack.com/p/lean-inference-workflows-applying](https://neurometric.substack.com/p/lean-inference-workflows-applying)

生成摘要时出错

---

## 85. Reviving Teletext for Ham Radio

**原文标题**: Reviving Teletext for Ham Radio

**原文链接**: [https://spectrum.ieee.org/reviving-teletext-for-ham-radio](https://spectrum.ieee.org/reviving-teletext-for-ham-radio)

生成摘要时出错

---

## 86. A walking tour of surveillance infrastructure in Seattle (2020)

**原文标题**: A walking tour of surveillance infrastructure in Seattle (2020)

**原文链接**: [https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/](https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/)

生成摘要时出错

---

