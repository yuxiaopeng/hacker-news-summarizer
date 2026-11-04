# Hacker News 热门文章摘要 (2026-11-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 白宫网络检测到住宅代理

**原文标题**: Residential proxies detected on White House network

**原文链接**: [https://layer3intel.com/blog/residential-proxies-white-house-network](https://layer3intel.com/blog/residential-proxies-white-house-network)

Layer3 Intel 的新型住宅代理观测站（Residential Proxy Observatory）检测到了源自白宫网络（AS2650）的住宅代理活动。在 2026 年 10 月 5 日至 11 月 3 日期间，该公司在 6 个 IP 地址上记录了 236 次出口事件，涉及 28 种不同的住宅代理服务。

这种活动模式主要发生在下午 5 点至午夜之间，表明其源于被感染的个人设备，而非公共访客 Wi-Fi 网络。这一发现构成了重大的安全风险，因为存在漏洞的代理 SDK（软件开发工具包）可被威胁行为者利用，进行未经授权的内网访问和横向移动。此类手段在历史上曾被用于传播大规模僵尸网络，例如波及数百万台设备的 Kimwolf。

除了白宫，该报告还强调了住宅代理在全球范围内的无处不在，并记录了在世界一些最偏远地区的活动。显著的检测结果包括：
* **南极洲：** 麦克默多站（McMurdo Station）的 3 次观察记录。
* **圣赫勒拿岛：** 在 413 个地址中记录了超过 32,000 次观察。
* **其他偏远地区：** 皮特凯恩群岛、斯瓦尔巴群岛和福克兰群岛也记录到了相关活动。

这些代理的广泛存在表明，无论地理位置如何或感知安全性高低，没有任何网络能对感染免疫。Layer3 Intel 已提议与相关联邦机构共享原始日志，以协助缓解这些漏洞。研究结果突显了日益严峻的网络安全挑战：住宅代理允许任何人利用日常设备上安全性较差的 SDK，通过合法网络掩盖其流量，从而绕过传统防御手段。

---

## 2. 昆虫不会聚集在LED灯旁。

**原文标题**: Insects don't swarm at LED lights

**原文链接**: [https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/](https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/)

本文探讨了为什么与传统的白炽灯和荧光灯相比，昆虫被 LED 灯吸引的程度显著降低。

**导航机制**
夜行昆虫利用“横向定向”进行导航，并以月亮作为参照点。由于月球距离无穷远，它们通过让光线保持在背部来维持身体直立并沿直线飞行。由于月光包含紫外线 (UV) 和红外线波长，昆虫会识别紫外线信号来确定其导航源。

**LED 与传统照明的对比**
传统的白炽灯泡会发出大量的紫外线辐射，这会误导昆虫将灯泡错认为月亮，导致它们绕着灯光打转，甚至由于平衡失调而翻转。相比之下，LED 的设计侧重于能效；它们几乎将电能完全转化为可见光谱（400–700 纳米），通常不产生紫外线或红外线辐射。因此，昆虫不会将 LED 视为导航线索，聚集在灯光周围的可能性也大大降低。

**科学证据与生态影响**
布里斯托大学 2016 年的一项研究证实了这一点。研究发现，与白炽灯或紧凑型荧光灯 (CFL) 相比，LED 吸引的昆虫数量显著减少，尤其是双翅目（蝇类）和摇蚊。

这种转变具有显著的生态后果：
*   **捕食者行为**：壁虎等物种以往常聚集在户外灯光周围捕食成群的昆虫，现在由于缺乏猎物，正从这些区域消失。
*   **生态保护**：夜间人造光是全球昆虫数量下降的主要因素。改用 LED 可能有助于减轻对野生动物的干扰，并减少虫媒疾病的传播。

---

## 3. Ripple-65B 预览：美国智能体编程开源权重 SOTA

**原文标题**: Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding

**原文链接**: [https://www.ricursive.com/ripple](https://www.ricursive.com/ripple)

Ricursive Intelligence 发布了 **Ripple-65B Preview**。这是一款前沿的开源权重模型，在智能体编程（agentic coding）领域创下了美国新的 SOTA（最高水平）。尽管参数量较小，Ripple-65B 在 **TerminalBench 2.1 上获得了 80.52 分**，显著超越了 Reflection Beam 501B 和 Meta Muse Spark 816B 等规模大得多的模型。

本次发布的核心亮点包括：

*   **成本效益：** Ricursive 仅耗资 **3200 万美元**便开发出该模型，成本约为此前开源 SOTA 模型的十分之一。这笔预算涵盖了整个研发过程，包括在 12 万亿 token 上的预训练及后训练。
*   **架构设计：** 团队摒弃了混合专家（MoE）架构，采用了针对英伟达硬件优化的“窄而深”的**稠密 Transformer 架构**（80 层）。其特性包括门控注意力（gated attention）、全局 NoPE 和数值残差（value residuals）。与 Olmo 3 基准相比，该设计在编程任务上的计算效率提高了 16 倍。
*   **训练方法：** 该模型通过“陡升强化学习”（Steep Ascent Reinforcement Learning）进行精炼。利用自定义合成数据管道和高质量环境，Ricursive 仅通过 140 万次 rollout 就达到了 SOTA 性能，比此前的记录保持者减少了 **70 倍**。
*   **能力：** 该模型支持 **100 万（1M）上下文长度**，并专为在英伟达 DGX Spark 等本地设备上实现低延迟推理而设计。

Ripple-65B Preview 是 Ricursive 用于其 AI 芯片设计平台的专有模型的通用变体。该模型目前已在 **Hugging Face、Together AI、GMI Cloud 和 OpenRouter** 上线，并预计很快将在 Fireworks AI 发布。该项目证明，通过精细的模型阶梯化（laddering）和软硬件协同优化，能以远低于传统行业水平的成本实现前沿级的性能。

---

## 4. AI正迫使我们偿还积压了40年的技术债。

**原文标题**: AI is forcing us to pay off 40 years of technical debt

**原文链接**: [https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)

在《IEEE Spectrum》计算与硬件编辑迪娜·根金娜（Dina Genkina）撰写的《人工智能正迫使我们偿还 40 年的技术债》一文中，她指出，人工智能的整合正在暴露数字基础设施中累积数十年的缺陷。

核心观点是，在过去 40 年里，软件开发往往优先考虑开发速度和即时功能，而非安全性与长期稳定性。这导致了巨额的“技术债”——即大量积压的遗留代码、架构捷径以及过时的协议。

根金娜以 “PHP2Shell” 漏洞为例，说明了当这些陈旧缺陷与新技术相遇时，我们即将面临的“网络安全地狱”。虽然这些遗留代码在孤立系统中曾被埋没或尚可管控，但人工智能的出现改变了局势。由于人工智能系统通常需要深度集成并访问庞大的数据层，它们充当了催化剂，揭示并加剧了这些潜在的漏洞。

文章指出，我们已达到一个临界点，无法再在摇摇欲坠的基础之上构建先进的人工智能。为了确保未来系统的安全与功能完备，科技行业现在被迫投入大量资源开展“还债”工作，通过基础设施现代化改造并修复被忽视了近半个世纪的漏洞。如果不这样做，现代系统将日益脆弱，面临前所未有的安全威胁。

---

## 5. JSON 的新 Go API

**原文标题**: A new Go API for JSON

**原文链接**: [https://go.dev/blog/jsonv2](https://go.dev/blog/jsonv2)

Go 1.27 引入了两个新包——`encoding/json/v2` 和 `encoding/json/jsontext`——旨在解决原 `encoding/json` (v1) 库长期存在的局限性和行为缺陷。

**关键改进与架构**
新架构将语法关注点（处理 JSON 语法）与语义关注点（将 Go 类型映射到 JSON）分离。`jsontext` 包提供了一个无反射的底层 API，用于流式传输 token 和值。在此基础上，`v2` 包负责处理 Go 类型的高级序列化（marshaling）和反序列化（unmarshaling）。

**修复行为缺陷**
`v2` 包采用了更安全、更现代的默认设置：
*   **严格性：** 强制要求有效的 UTF-8 编码，并拒绝重复的对象成员名称。
*   **区分大小写：** 反序列化现在默认对结构体字段进行区分大小写的匹配。
*   **Nil 处理：** Nil 切片和 map 会被序列化为空数组 (`[]`) 或对象 (`{}`)，而非 `null`。
*   **改进的标签：** 重新定义了 `omitempty` 选项，用于省略编码为“空”值（如 `[]` 或 `{}`）的字段。

**API 与自定义**
`v2` API 允许直接向 `Marshal` 和 `Unmarshal` 函数传递选项，这是 v1 中缺失的功能。它还引入了 `MarshalerTo` 和 `UnmarshalerFrom` 接口，支持真正的流式处理并允许选项在调用栈中向下传递。强大的全新“调用者指定自定义”功能让开发者无需修改原始类型，即可为任何类型（包括第三方类型）定义 JSON 表示形式。

**性能**
虽然 `Marshal` 的性能与 v1 持平，但 `v2` 的 `Unmarshal` 速度显著提升——在某些基准测试中最高提升了 10 倍。这些性能增益主要得益于内存分配的减少，以及消除了旧版 v1 接口所需的冗余解析。

---

## 6. 高通 Cloud AI 100 Ultra – 150W AI加速卡，配备128GB显存，带宽548GB/s

**原文标题**: Qualcomm Cloud AI 100 Ultra – 150W AI Accelerator Card with 128GB at 548GB/s

**原文链接**: [https://www.qualcomm.com/data-center/products/cloud-ai-100-ultra](https://www.qualcomm.com/data-center/products/cloud-ai-100-ultra)

高通 Cloud AI 100 Ultra 是一款高性能 AI 加速卡，专门针对生成式 AI 和大语言模型 (LLM) 等高负载推理任务而设计。

关键技术规格包括：
*   **显存：** 128GB LPDDR5x 显存，为单卡运行超大型模型提供了必要的容量支持。
*   **带宽：** 548GB/s 的显存带宽，确保了数据的快速处理并降低了实时应用的延迟。
*   **能效：** 热设计功耗 (TDP) 为 150W，彰显了高通对高能效比的关注，这对于降低数据中心的运营成本至关重要。

Cloud AI 100 Ultra 专为可扩展性而设计，能够轻松集成到现有的数据中心基础设施和边缘环境中。通过针对推理而非训练进行优化，该卡为大规模部署 AI 提供了专门的解决方案。其架构经过量身定制，旨在实现吞吐量和效率的最大化，为寻求在高速 AI 处理与可持续能源消耗之间取得平衡的企业提供了一个极具竞争力的替代方案。

---

## 7. 大语言模型可证明推理的进展

**原文标题**: Progress on provable inference for large language models

**原文链接**: [https://www.anthropic.com/research/provable-inference](https://www.anthropic.com/research/provable-inference)

Anthropic 与合作者推出了 **FlashProve**，这是一个用于大语言模型“可证明推理”（PI）的高性能系统。该系统解决了关键的信任鸿沟：即用户此前无法验证 AI 响应究竟是由特定模型生成的，还是由更廉价的替代品或被篡改的内容流生成的。

FlashProve 利用 **zkSNARKs**（零知识简洁非交互式知识论证）为模型输出提供加密证明。这种方法提供了两个核心保障：
1. **简洁性：** 证明文件体积小（1,024 个 token 约 19 MB），且可在消费级硬件上快速验证。
2. **零知识性：** 在验证计算过程的同时，确保模型的专有权重信息不被泄露。

**性能与技术里程碑**
该系统展示了远超以往开源方法的效率。在单张 H100 GPU 上，FlashProve 处理 4000 亿参数的混合专家（MoE）模型（采用 4 位量化）的速度可达 **每秒 110 个 token**。虽然其证明器的速度比 vLLM 等标准推理库慢约 70–95 倍，但对于高可靠性应用而言仍具实用价值。为确保安全性，团队使用 **Lean** 编程语言对其技术主张进行了形式化验证。

**关键应用场景**
* **合规监管：** 允许监管机构验证硬件是否被用于推理，而非未经授权的模型训练（“算力节制”）。
* **安全保障：** 检测服务器是否遭到入侵，或模型是否被攻击者替换。
* **出处溯源：** 使开发者能够证明特定的前沿模型已被用于代码审计或安全性评估等任务。

Anthropic 已将 FlashProve 作为开源项目在 Apache 2.0 协议下发布，涵盖了协议规范、可执行代码（C++ 和 Lean）以及技术文档，以鼓励 AI 完整性领域的进一步发展。

---

## 8. Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux

**原文标题**: Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux

**原文链接**: [https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop)

生成摘要时出错

---

## 9. Show HN: After a decade of reversing, I got co-op working in DOS Wing Commander

**原文标题**: Show HN: After a decade of reversing, I got co-op working in DOS Wing Commander

**原文链接**: [https://fireflyk64.github.io/wcmulti/](https://fireflyk64.github.io/wcmulti/)

生成摘要时出错

---

## 10. Conductor Is Joining Meta

**原文标题**: Conductor Is Joining Meta

**原文链接**: [https://www.conductor.build/announcement](https://www.conductor.build/announcement)

生成摘要时出错

---

## 11. Hacking the Xbox 360 Hypervisor Part 3: Bad Update Improvements

**原文标题**: Hacking the Xbox 360 Hypervisor Part 3: Bad Update Improvements

**原文链接**: [https://icode4.coffee/?p=1746](https://icode4.coffee/?p=1746)

生成摘要时出错

---

## 12. OpenAI to acquire Pierre Computer Company

**原文标题**: OpenAI to acquire Pierre Computer Company

**原文链接**: [https://openai.com/index/openai-to-acquire-pierre/](https://openai.com/index/openai-to-acquire-pierre/)

生成摘要时出错

---

## 13. Tencent Hy4

**原文标题**: Tencent Hy4

**原文链接**: [https://hy.tencent.ai/research/hy4](https://hy.tencent.ai/research/hy4)

生成摘要时出错

---

## 14. AMD expects to outsell Intel in Q4 for the first time in history

**原文标题**: AMD expects to outsell Intel in Q4 for the first time in history

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections](https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections)

生成摘要时出错

---

## 15. Verification Is Not Knowledge: Science needs more than answers

**原文标题**: Verification Is Not Knowledge: Science needs more than answers

**原文链接**: [https://blog.cosmos-institute.org/p/verification-is-not-knowledge](https://blog.cosmos-institute.org/p/verification-is-not-knowledge)

生成摘要时出错

---

## 16. North Korean fake job interview led to $6.3B Binance heist

**原文标题**: North Korean fake job interview led to $6.3B Binance heist

**原文链接**: [https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398](https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398)

生成摘要时出错

---

## 17. Show HN: I built a tool that prices a prebuilt PC part by part

**原文标题**: Show HN: I built a tool that prices a prebuilt PC part by part

**原文链接**: [https://pcdealcheck.com/](https://pcdealcheck.com/)

生成摘要时出错

---

## 18. Incident with Pull Requests, Git Operations and Issues

**原文标题**: Incident with Pull Requests, Git Operations and Issues

**原文链接**: [https://www.githubstatus.com/incidents/smtdswd1h2w4](https://www.githubstatus.com/incidents/smtdswd1h2w4)

生成摘要时出错

---

## 19. Show HN: The DNA of DOOM – How code structure survives across 44 ports

**原文标题**: Show HN: The DNA of DOOM – How code structure survives across 44 ports

**原文链接**: [https://squid-protocol.github.io/gitgalaxy/museum-of-code/doom-dna/](https://squid-protocol.github.io/gitgalaxy/museum-of-code/doom-dna/)

生成摘要时出错

---

## 20. Kimi K3.1 Pro model weights are out

**原文标题**: Kimi K3.1 Pro model weights are out

**原文链接**: [https://huggingface.co/moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

生成摘要时出错

---

## 21. If you're on Replit Pro, you have until November 8 to opt out of arbitration

**原文标题**: If you're on Replit Pro, you have until November 8 to opt out of arbitration

**原文链接**: [https://readthediff.substack.com/p/replit-pro-arbitration-opt-out-november-8](https://readthediff.substack.com/p/replit-pro-arbitration-opt-out-november-8)

生成摘要时出错

---

## 22. Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)

**原文标题**: Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)

**原文链接**: [https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/](https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/)

生成摘要时出错

---

## 23. From wild to mild: Friendly foxes show changes in brain region

**原文标题**: From wild to mild: Friendly foxes show changes in brain region

**原文链接**: [https://news.cornell.edu/stories/2026/11/wild-mild-friendly-foxes-show-changes-brain-region](https://news.cornell.edu/stories/2026/11/wild-mild-friendly-foxes-show-changes-brain-region)

生成摘要时出错

---

## 24. Evergreen: A Provably Safe Systems Language

**原文标题**: Evergreen: A Provably Safe Systems Language

**原文链接**: [https://evergreenlang.net](https://evergreenlang.net)

生成摘要时出错

---

## 25. Benchfmt.rs: Bringing Go's benchmarking and benchstat workflow to Rust

**原文标题**: Benchfmt.rs: Bringing Go's benchmarking and benchstat workflow to Rust

**原文链接**: [https://www.bwplotka.dev/2026/rust-microbenchmarks-benchstat/](https://www.bwplotka.dev/2026/rust-microbenchmarks-benchstat/)

生成摘要时出错

---

## 26. Everything is an AI scam now

**原文标题**: Everything is an AI scam now

**原文链接**: [https://www.davidralphlewis.co.uk/posts/everything-is-an-ai-scam-now/](https://www.davidralphlewis.co.uk/posts/everything-is-an-ai-scam-now/)

生成摘要时出错

---

## 27. Kitty 0.50

**原文标题**: Kitty 0.50

**原文链接**: [https://sw.kovidgoyal.net/kitty/changelog/#](https://sw.kovidgoyal.net/kitty/changelog/#)

生成摘要时出错

---

## 28. Letting users trust their own MCP clients, without opening a phishing hole

**原文标题**: Letting users trust their own MCP clients, without opening a phishing hole

**原文链接**: [https://streamvessel.com/blog/mcp-trusted-redirect-uris](https://streamvessel.com/blog/mcp-trusted-redirect-uris)

生成摘要时出错

---

## 29. In Praise of Japan's Failure to Keep Up

**原文标题**: In Praise of Japan's Failure to Keep Up

**原文链接**: [https://www.noemamag.com/in-praise-of-japans-failure-to-keep-up/](https://www.noemamag.com/in-praise-of-japans-failure-to-keep-up/)

生成摘要时出错

---

## 30. Have I befriended a murderer?

**原文标题**: Have I befriended a murderer?

**原文链接**: [https://longreads.com/2026/11/03/murder-friendship-doubt/](https://longreads.com/2026/11/03/murder-friendship-doubt/)

生成摘要时出错

---

## 31. This Month in Ladybird – October 2026

**原文标题**: This Month in Ladybird – October 2026

**原文链接**: [https://ladybird.org/newsletter/2026-10-31/](https://ladybird.org/newsletter/2026-10-31/)

生成摘要时出错

---

## 32. The lost malloc()

**原文标题**: The lost malloc()

**原文链接**: [https://napcakes.nekoweb.org/posts/malloc/](https://napcakes.nekoweb.org/posts/malloc/)

生成摘要时出错

---

## 33. Giant canyon on Mars is still tectonically active

**原文标题**: Giant canyon on Mars is still tectonically active

**原文链接**: [https://lamont.columbia.edu/news/giant-canyon-mars-still-tectonically-active-today](https://lamont.columbia.edu/news/giant-canyon-mars-still-tectonically-active-today)

生成摘要时出错

---

## 34. Debian apt security update (man-in-the-middle)

**原文标题**: Debian apt security update (man-in-the-middle)

**原文链接**: [https://lists.debian.org/debian-security-announce/2026/msg00526.html?pow_referer=](https://lists.debian.org/debian-security-announce/2026/msg00526.html?pow_referer=)

生成摘要时出错

---

## 35. 512GB Mac Studio

**原文标题**: 512GB Mac Studio

**原文链接**: [https://www.apple.com/shop/buy-mac/mac-studio/m5-ultra-chip-36-core-cpu-80-core-gpu-512gb-memory-1tb-storage](https://www.apple.com/shop/buy-mac/mac-studio/m5-ultra-chip-36-core-cpu-80-core-gpu-512gb-memory-1tb-storage)

生成摘要时出错

---

## 36. Adding Window Functions to a Spreadsheet

**原文标题**: Adding Window Functions to a Spreadsheet

**原文链接**: [https://www.getgrist.com/blog/running-totals-you-dont-have-to-chase/](https://www.getgrist.com/blog/running-totals-you-dont-have-to-chase/)

生成摘要时出错

---

## 37. Nintendo's cartridge maker shifts focus to data centers, hurting physical media

**原文标题**: Nintendo's cartridge maker shifts focus to data centers, hurting physical media

**原文链接**: [https://kotaku.com/nintendo-switch-cart-rom-physical-media-data-centers-manufacture-2000753293](https://kotaku.com/nintendo-switch-cart-rom-physical-media-data-centers-manufacture-2000753293)

生成摘要时出错

---

## 38. Synaptics Appears to Use Legal Threats to Block Open-Source DisplayLink Driver

**原文标题**: Synaptics Appears to Use Legal Threats to Block Open-Source DisplayLink Driver

**原文链接**: [https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver](https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver)

生成摘要时出错

---

## 39. Ashby (YC W19) Is Hiring EMs

**原文标题**: Ashby (YC W19) Is Hiring EMs

**原文链接**: [https://www.ashbyhq.com/careers?ashby_jid=695b1ce6-c375-4fad-94ef-61b50a3fbd28&utm_source=hn](https://www.ashbyhq.com/careers?ashby_jid=695b1ce6-c375-4fad-94ef-61b50a3fbd28&utm_source=hn)

生成摘要时出错

---

## 40. Jelly Sheet

**原文标题**: Jelly Sheet

**原文链接**: [https://mrdoob.github.io/codevember-2026/01/](https://mrdoob.github.io/codevember-2026/01/)

生成摘要时出错

---

## 41. Distinct cellular and genetic differences in colorectal cancer in young patients

**原文标题**: Distinct cellular and genetic differences in colorectal cancer in young patients

**原文链接**: [https://www.dana-farber.org/newsroom/news-releases/2026/study-reveals-distinct-cellular-and-genetic-differences-in-colorectal-cancer-in-younger-patients](https://www.dana-farber.org/newsroom/news-releases/2026/study-reveals-distinct-cellular-and-genetic-differences-in-colorectal-cancer-in-younger-patients)

生成摘要时出错

---

## 42. Mocktastic: A Meshtastic Node on Arduino

**原文标题**: Mocktastic: A Meshtastic Node on Arduino

**原文链接**: [https://github.com/Vapmuz/Mocktastic](https://github.com/Vapmuz/Mocktastic)

生成摘要时出错

---

## 43. Show HN: Unclickbait – Replace clickbait YouTube thumbnails

**原文标题**: Show HN: Unclickbait – Replace clickbait YouTube thumbnails

**原文链接**: [https://unclickbait.app/](https://unclickbait.app/)

生成摘要时出错

---

## 44. Show HN: Uncracked City, detective game where you question LLM suspects that lie

**原文标题**: Show HN: Uncracked City, detective game where you question LLM suspects that lie

**原文链接**: [https://uncracked.city](https://uncracked.city)

生成摘要时出错

---

## 45. Apple Will Scan Public iCloud Links for Harmful Content Starting in iOS 27.3

**原文标题**: Apple Will Scan Public iCloud Links for Harmful Content Starting in iOS 27.3

**原文链接**: [https://support.apple.com/en-us/149168](https://support.apple.com/en-us/149168)

生成摘要时出错

---

## 46. Funimation Shutdown Fuels Push for DMCA Exemption to Legally Rip Anime Content

**原文标题**: Funimation Shutdown Fuels Push for DMCA Exemption to Legally Rip Anime Content

**原文链接**: [https://torrentfreak.com/funimation-shutdown-fuels-push-for-dmca-exemption-to-legally-rip-anime-content/](https://torrentfreak.com/funimation-shutdown-fuels-push-for-dmca-exemption-to-legally-rip-anime-content/)

生成摘要时出错

---

## 47. National Radio Quiet Zone

**原文标题**: National Radio Quiet Zone

**原文链接**: [https://greenbankobservatory.org/about/national-radio-quiet-zone/](https://greenbankobservatory.org/about/national-radio-quiet-zone/)

生成摘要时出错

---

## 48. Stringman, an $800 open-source room scale gripper robot

**原文标题**: Stringman, an $800 open-source room scale gripper robot

**原文链接**: [https://neufangled.com/](https://neufangled.com/)

生成摘要时出错

---

## 49. Jailbreaking my car's navigation system just so I can change the time

**原文标题**: Jailbreaking my car's navigation system just so I can change the time

**原文链接**: [https://blog.nns.ee/2026/11/02/renault-hack/](https://blog.nns.ee/2026/11/02/renault-hack/)

生成摘要时出错

---

## 50. There is no posttraining data commons

**原文标题**: There is no posttraining data commons

**原文链接**: [https://openathena.ai/blog/there-is-no-posttraining-data-commons/](https://openathena.ai/blog/there-is-no-posttraining-data-commons/)

生成摘要时出错

---

## 51. Flock (YC 2018) Re-Connects Camera Disabled by Police Chief

**原文标题**: Flock (YC 2018) Re-Connects Camera Disabled by Police Chief

**原文链接**: [https://www.thedrive.com/news/flock-just-replaced-a-camera-my-city-banned-and-unplugged-calling-it-broken](https://www.thedrive.com/news/flock-just-replaced-a-camera-my-city-banned-and-unplugged-calling-it-broken)

生成摘要时出错

---

## 52. Basically no one is using AI agents for their DoorDash orders

**原文标题**: Basically no one is using AI agents for their DoorDash orders

**原文链接**: [https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/](https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/)

生成摘要时出错

---

## 53. Arrows to arrows, categories to queries (2025)

**原文标题**: Arrows to arrows, categories to queries (2025)

**原文链接**: [https://reasonablypolymorphic.com/blog/arrows-to-arrows/](https://reasonablypolymorphic.com/blog/arrows-to-arrows/)

生成摘要时出错

---

## 54. We're training a Figma-fluent editing model

**原文标题**: We're training a Figma-fluent editing model

**原文链接**: [https://www.figma.com/blog/training-a-figma-fluent-editing-model/](https://www.figma.com/blog/training-a-figma-fluent-editing-model/)

生成摘要时出错

---

## 55. AI data centers comprehensively defeated at US midterm elections

**原文标题**: AI data centers comprehensively defeated at US midterm elections

**原文链接**: [https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments](https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments)

生成摘要时出错

---

## 56. People say they want small smartphones–Enough Phone will put that to the test

**原文标题**: People say they want small smartphones–Enough Phone will put that to the test

**原文链接**: [https://arstechnica.com/gadgets/2026/11/people-say-they-want-small-smartphones-the-enough-phone-will-put-that-to-the-test/](https://arstechnica.com/gadgets/2026/11/people-say-they-want-small-smartphones-the-enough-phone-will-put-that-to-the-test/)

生成摘要时出错

---

## 57. Safari introduces Adaptive Dark Mode in 27.3

**原文标题**: Safari introduces Adaptive Dark Mode in 27.3

**原文链接**: [https://webkit.org/blog/18541/introducing-adaptive-dark-mode/](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

生成摘要时出错

---

## 58. Show HN: Codemap – one-page interactive map of any Go repository

**原文标题**: Show HN: Codemap – one-page interactive map of any Go repository

**原文链接**: [https://github.com/peterretief/codemap](https://github.com/peterretief/codemap)

生成摘要时出错

---

## 59. The Internals of PostgreSQL

**原文标题**: The Internals of PostgreSQL

**原文链接**: [https://www.interdb.jp/pg/index.html](https://www.interdb.jp/pg/index.html)

生成摘要时出错

---

## 60. Kellogg's Rice Krispies changed U.K. recipe, muffling its snap, crackle and pop

**原文标题**: Kellogg's Rice Krispies changed U.K. recipe, muffling its snap, crackle and pop

**原文链接**: [https://www.cbc.ca/news/business/rice-krispies-changes-recipe-rice-9.7408568](https://www.cbc.ca/news/business/rice-krispies-changes-recipe-rice-9.7408568)

生成摘要时出错

---

## 61. The 'Astra can read and write weights to improve Qwen' post is misleading

**原文标题**: The 'Astra can read and write weights to improve Qwen' post is misleading

**原文链接**: [https://honnibal.dev/blog/astra-read-write-misleading](https://honnibal.dev/blog/astra-read-write-misleading)

生成摘要时出错

---

## 62. Education shouldn't be held for ransom

**原文标题**: Education shouldn't be held for ransom

**原文链接**: [https://blog.kagi.com/education-should-not-be-held-for-ransom](https://blog.kagi.com/education-should-not-be-held-for-ransom)

生成摘要时出错

---

## 63. NetBSD 11.1

**原文标题**: NetBSD 11.1

**原文链接**: [https://netbsd.org/releases/formal-11/NetBSD-11.1.html](https://netbsd.org/releases/formal-11/NetBSD-11.1.html)

生成摘要时出错

---

## 64. C++26 Disapproved

**原文标题**: C++26 Disapproved

**原文链接**: [https://andreasfertig.com/blog/2026/11/cpp26-dis-failed-how-does-cpp-survive/](https://andreasfertig.com/blog/2026/11/cpp26-dis-failed-how-does-cpp-survive/)

生成摘要时出错

---

## 65. Fujifilm to boost tape production 5x as AI fuels archiving demand

**原文标题**: Fujifilm to boost tape production 5x as AI fuels archiving demand

**原文链接**: [https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)

生成摘要时出错

---

## 66. Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels

**原文标题**: Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels

**原文链接**: [https://hackertv.org](https://hackertv.org)

生成摘要时出错

---

## 67. Curiosity Traps

**原文标题**: Curiosity Traps

**原文链接**: [https://www.autodidacts.io/curiosity-traps/](https://www.autodidacts.io/curiosity-traps/)

生成摘要时出错

---

## 68. Mac at any scale

**原文标题**: Mac at any scale

**原文链接**: [https://namespace.so/blog/mac-at-any-scale](https://namespace.so/blog/mac-at-any-scale)

生成摘要时出错

---

## 69. Writing seen in PHerc. 306B, for the first time in 2000 years

**原文标题**: Writing seen in PHerc. 306B, for the first time in 2000 years

**原文链接**: [https://scrollprize.substack.com/p/writing-seen-in-pherc-306b-for-the](https://scrollprize.substack.com/p/writing-seen-in-pherc-306b-for-the)

生成摘要时出错

---

## 70. The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer

**原文标题**: The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer

**原文链接**: [https://arxiv.org/abs/2605.29713](https://arxiv.org/abs/2605.29713)

生成摘要时出错

---

## 71. New York reports first measles death in more than 30 years

**原文标题**: New York reports first measles death in more than 30 years

**原文链接**: [https://www.nbcnews.com/health/health-news/new-york-measles-death-rcna607137](https://www.nbcnews.com/health/health-news/new-york-measles-death-rcna607137)

生成摘要时出错

---

## 72. Introduction to Programming in ATS

**原文标题**: Introduction to Programming in ATS

**原文链接**: [https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/book1.html](https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/book1.html)

生成摘要时出错

---

## 73. Durable Coroutines for TypeScript

**原文标题**: Durable Coroutines for TypeScript

**原文链接**: [https://restate.dev/blog/durable_coroutines](https://restate.dev/blog/durable_coroutines)

生成摘要时出错

---

## 74. Antimony: CAD Software Evolved from Lisp Machines and Not Drafting Tables (2015)

**原文标题**: Antimony: CAD Software Evolved from Lisp Machines and Not Drafting Tables (2015)

**原文链接**: [https://www.mattkeeter.com/projects/antimony/3/](https://www.mattkeeter.com/projects/antimony/3/)

生成摘要时出错

---

## 75. Toit v2.0.0

**原文标题**: Toit v2.0.0

**原文链接**: [https://toit.io/blog/toit-v2-0-0/](https://toit.io/blog/toit-v2-0-0/)

生成摘要时出错

---

## 76. Japan's Jimi 'Mundane' Halloween Costumes of 2026

**原文标题**: Japan's Jimi 'Mundane' Halloween Costumes of 2026

**原文链接**: [https://spoon-tamago.com/japan-jimi-mundane-halloween-costumes-2026/](https://spoon-tamago.com/japan-jimi-mundane-halloween-costumes-2026/)

生成摘要时出错

---

## 77. Kyiv Independent reports system breach

**原文标题**: Kyiv Independent reports system breach

**原文链接**: [https://hromadske.ua/en/war/273759-kyiv-independent-reports-system-breach-after-readers-receive-fake-nuclear-attack-warning](https://hromadske.ua/en/war/273759-kyiv-independent-reports-system-breach-after-readers-receive-fake-nuclear-attack-warning)

生成摘要时出错

---

## 78. Resisting Cognitive Surrender

**原文标题**: Resisting Cognitive Surrender

**原文链接**: [https://knlb.dev/essays/surrender](https://knlb.dev/essays/surrender)

生成摘要时出错

---

## 79. Why Clip Art Was Everywhere Until It Wasn't [video]

**原文标题**: Why Clip Art Was Everywhere Until It Wasn't [video]

**原文链接**: [https://www.youtube.com/watch?v=XfLlpxE6AYM](https://www.youtube.com/watch?v=XfLlpxE6AYM)

生成摘要时出错

---

## 80. Practice speaking Japanese with real YouTube videos, graded line by line

**原文标题**: Practice speaking Japanese with real YouTube videos, graded line by line

**原文链接**: [https://jivx.com/yt](https://jivx.com/yt)

生成摘要时出错

---

## 81. Why Don't We Live in an Art Nouveau World?

**原文标题**: Why Don't We Live in an Art Nouveau World?

**原文链接**: [https://asteriskmag.com/issues/16/why-don-t-we-life-in-an-art-nouveau-world](https://asteriskmag.com/issues/16/why-don-t-we-life-in-an-art-nouveau-world)

生成摘要时出错

---

## 82. Shlemiel the Painter Is Back: How Zig's Libc Rewrite Made SQLite 12,000× Slower

**原文标题**: Shlemiel the Painter Is Back: How Zig's Libc Rewrite Made SQLite 12,000× Slower

**原文链接**: [https://dennisforbes.ca/blog/microblog/2026/10/the_accidental_12000x_sqlite_slowdown/](https://dennisforbes.ca/blog/microblog/2026/10/the_accidental_12000x_sqlite_slowdown/)

生成摘要时出错

---

## 83. Brainstem Theory of Consciousness

**原文标题**: Brainstem Theory of Consciousness

**原文链接**: [https://journals.sagepub.com/doi/10.1177/10738584261470362](https://journals.sagepub.com/doi/10.1177/10738584261470362)

生成摘要时出错

---

## 84. Nvidia – open-source auto-ontology

**原文标题**: Nvidia – open-source auto-ontology

**原文链接**: [https://github.com/NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

生成摘要时出错

---

## 85. Qwen 3.8 27B on my laptop can interpret model weights, too

**原文标题**: Qwen 3.8 27B on my laptop can interpret model weights, too

**原文链接**: [https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)

生成摘要时出错

---

## 86. European RISC-V Industrial Computing Initiative

**原文标题**: European RISC-V Industrial Computing Initiative

**原文链接**: [https://erici.eu](https://erici.eu)

生成摘要时出错

---

## 87. Microsoft fixes a Windows 11 annoyance as PC revenue declines

**原文标题**: Microsoft fixes a Windows 11 annoyance as PC revenue declines

**原文链接**: [https://arstechnica.com/gadgets/2026/10/windows-11-gets-right-click-menu-improvements-as-pc-revenue-slides/](https://arstechnica.com/gadgets/2026/10/windows-11-gets-right-click-menu-improvements-as-pc-revenue-slides/)

生成摘要时出错

---

## 88. HackerTube: YouTube built from videos recommended by HN

**原文标题**: HackerTube: YouTube built from videos recommended by HN

**原文链接**: [https://karpathy.bearblog.dev/hacker-tube/](https://karpathy.bearblog.dev/hacker-tube/)

生成摘要时出错

---

## 89. Show HN: Kairos – Open-source risk and fraud decisioning platform

**原文标题**: Show HN: Kairos – Open-source risk and fraud decisioning platform

**原文链接**: [https://github.com/finic-ai/kairos](https://github.com/finic-ai/kairos)

生成摘要时出错

---

## 90. Katamari Damacy but it's The Met collection

**原文标题**: Katamari Damacy but it's The Met collection

**原文链接**: [https://katamari.vaguespac.es/](https://katamari.vaguespac.es/)

生成摘要时出错

---

## 91. Union Types and Option Types (2025)

**原文标题**: Union Types and Option Types (2025)

**原文链接**: [https://tibleiz.net/blog/2025-03-16-union-types-and-option-types.html](https://tibleiz.net/blog/2025-03-16-union-types-and-option-types.html)

生成摘要时出错

---

## 92. TScert: A Sound Core for TypeScript

**原文标题**: TScert: A Sound Core for TypeScript

**原文链接**: [https://github.com/cristianoc/TScert](https://github.com/cristianoc/TScert)

生成摘要时出错

---

## 93. How I use AI (Oct 2026)

**原文标题**: How I use AI (Oct 2026)

**原文链接**: [https://ben.stolovitz.com/posts/how-use-ai-oct-2026/](https://ben.stolovitz.com/posts/how-use-ai-oct-2026/)

生成摘要时出错

---

## 94. Upcoming change for eMudhra CA certificates included in the Chrome Root Store

**原文标题**: Upcoming change for eMudhra CA certificates included in the Chrome Root Store

**原文链接**: [https://groups.google.com/a/ccadb.org/g/public/c/DU8p98nyQWc/m/R33zS9UIBgAJ](https://groups.google.com/a/ccadb.org/g/public/c/DU8p98nyQWc/m/R33zS9UIBgAJ)

生成摘要时出错

---

## 95. Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app

**原文标题**: Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app

**原文链接**: [https://momentic.ai/](https://momentic.ai/)

生成摘要时出错

---

## 96. Geoffrey Hinton: it might turn out we were better off without AI

**原文标题**: Geoffrey Hinton: it might turn out we were better off without AI

**原文链接**: [https://www.theguardian.com/uk-news/2026/nov/03/ai-godfather-geoffrey-hinton-better-off-without-ai](https://www.theguardian.com/uk-news/2026/nov/03/ai-godfather-geoffrey-hinton-better-off-without-ai)

生成摘要时出错

---

## 97. So my ISP was hijacking my DNS

**原文标题**: So my ISP was hijacking my DNS

**原文链接**: [https://www.karthihegde.dev/posts/dns_tampering](https://www.karthihegde.dev/posts/dns_tampering)

生成摘要时出错

---

## 98. Could a modern chess engine on a Pentium have defeated Kasparov in 1996?

**原文标题**: Could a modern chess engine on a Pentium have defeated Kasparov in 1996?

**原文链接**: [https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html](https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html)

生成摘要时出错

---

## 99. Postman silently auto-installs AI plugins and attempts to share all API data

**原文标题**: Postman silently auto-installs AI plugins and attempts to share all API data

**原文链接**: [https://github.com/postmanlabs/postman-app-support/issues/14370](https://github.com/postmanlabs/postman-app-support/issues/14370)

生成摘要时出错

---

## 100. Jaron Lanier on parallels between AI and social media

**原文标题**: Jaron Lanier on parallels between AI and social media

**原文链接**: [https://www.youtube.com/watch?v=WxaRn8kX2eI](https://www.youtube.com/watch?v=WxaRn8kX2eI)

生成摘要时出错

---

