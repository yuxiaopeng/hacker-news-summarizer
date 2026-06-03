# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-03.md)

*最后自动更新时间: 2026-06-03 20:38:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 2 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 3 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 4 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 5 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 6 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 7 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 8 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 9 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 10 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 11 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 12 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 13 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 14 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 15 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 16 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 17 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 18 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 19 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 20 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 21 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 22 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 23 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 24 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 25 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 26 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 27 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 28 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 29 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 30 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 31 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 32 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 33 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 34 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 35 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 36 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 37 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 38 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 39 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 40 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 41 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 42 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 43 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 44 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 45 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 46 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 47 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 48 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 49 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 50 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 51 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 52 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 53 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 54 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 55 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 56 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 57 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 58 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 59 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 60 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 61 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 62 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 63 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 64 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 65 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 66 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 67 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 68 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 69 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 70 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 71 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 72 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 73 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 74 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 75 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 76 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 77 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 78 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 79 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 80 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 81 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 82 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 83 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 84 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 85 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 86 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 87 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 88 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 89 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 90 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 91 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 92 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 93 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 94 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 95 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 96 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 97 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 98 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 99 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 100 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 101 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 102 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 103 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 104 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 105 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 106 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 107 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 108 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 109 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 110 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 111 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 112 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 113 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 114 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 115 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 116 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 117 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 118 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 119 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 120 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 121 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 122 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 123 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 124 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 125 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 126 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 127 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 128 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 129 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 130 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 131 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 132 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 133 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 134 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 135 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 136 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 137 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 138 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 139 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 140 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 141 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 142 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 143 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 144 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 145 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 146 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 147 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 148 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 149 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 150 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 151 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 152 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 153 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 154 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 155 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 156 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 157 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 158 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 159 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 160 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 161 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 162 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 163 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 164 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 165 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 166 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 167 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 168 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 169 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 170 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 171 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 172 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 173 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 174 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 175 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 176 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 177 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 178 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 179 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 180 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 181 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 182 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 183 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 184 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 185 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 186 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 187 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 188 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 189 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 190 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 191 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 192 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 193 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 194 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 195 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 196 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 197 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 198 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 199 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 200 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 201 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 202 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 203 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 204 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 205 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 206 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 207 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 208 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 209 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 210 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 211 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 212 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 213 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 214 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 215 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 216 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 217 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 218 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 219 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 220 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 221 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 222 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 223 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 224 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 225 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 226 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 227 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 228 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 229 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 230 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 231 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 232 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 233 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 234 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 235 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 236 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 237 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 238 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 239 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 240 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 241 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 242 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 243 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 244 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 245 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 246 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 247 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 248 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 249 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 250 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 251 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 252 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 253 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 254 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 255 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 256 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 257 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 258 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 259 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 260 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 261 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 262 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 263 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 264 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 265 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 266 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 267 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 268 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 269 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 270 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 271 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 272 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 273 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 274 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 275 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 276 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 277 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 278 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 279 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 280 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 281 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 282 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 283 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 284 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 285 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 286 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 287 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 288 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 289 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 290 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 291 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 292 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 293 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 294 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 295 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 296 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 297 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 298 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 299 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 300 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 301 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 302 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 303 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 304 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 305 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 306 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 307 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 308 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 309 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 310 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 311 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 312 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 313 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 314 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 315 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 316 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 317 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 318 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 319 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 320 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 321 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 322 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 323 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 324 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 325 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 326 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 327 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 328 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 329 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 330 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 331 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 332 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 333 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 334 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 335 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 336 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 337 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 338 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 339 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 340 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 341 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 342 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 343 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 344 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 345 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 346 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 347 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 348 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 349 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 350 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 351 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 352 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 353 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 354 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 355 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 356 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 357 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 358 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 359 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 360 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 361 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 362 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 363 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 364 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 365 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 366 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 367 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 368 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 369 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 370 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 371 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 372 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 373 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 374 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 375 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 376 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 377 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 378 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 379 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 380 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 381 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 382 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 383 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 384 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 385 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 386 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 387 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 388 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 389 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 390 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 391 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 392 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 393 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 394 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 395 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 396 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 397 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 398 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 399 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 400 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 401 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 402 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 403 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 404 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 405 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 406 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 407 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 408 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 409 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 410 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 411 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 412 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 413 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 414 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 415 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 416 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 417 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 418 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 419 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 420 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 421 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 422 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 423 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 424 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 425 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 426 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 427 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 428 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 429 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 430 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 431 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 432 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 433 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 434 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 435 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 436 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 437 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 438 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 439 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 440 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
