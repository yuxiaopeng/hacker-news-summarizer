# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-04.md)

*最后自动更新时间: 2026-11-04 22:52:09*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 2 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 3 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 4 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 5 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 6 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 7 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 8 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 9 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 10 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 11 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 12 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 13 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 14 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 15 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 16 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 17 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 18 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 19 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 20 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 21 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 22 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 23 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 24 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 25 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 26 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 27 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 28 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 29 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 30 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 31 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 32 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 33 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 34 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 35 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 36 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 37 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 38 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 39 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 40 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 41 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 42 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 43 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 44 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 45 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 46 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 47 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 48 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 49 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 50 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 51 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 52 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 53 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 54 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 55 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 56 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 57 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 58 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 59 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 60 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 61 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 62 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 65 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 66 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 67 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 68 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 69 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 70 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 71 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 72 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 73 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 74 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 75 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 76 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 77 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 78 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 79 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 80 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 81 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 82 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 83 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 84 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 85 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 86 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 87 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 88 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 89 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 90 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 91 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 92 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 93 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 94 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 95 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 96 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 97 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 98 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 99 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 100 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 101 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 102 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 103 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 104 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 105 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 106 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 107 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 108 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 109 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 110 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 111 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 112 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 113 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 114 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 115 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 116 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 117 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 118 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 119 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 120 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 121 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 122 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 123 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 124 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 125 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 126 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 127 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 128 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 129 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 130 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 131 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 132 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 133 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 134 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 135 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 136 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 137 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 138 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 139 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 140 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 141 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 142 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 143 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 144 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 145 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 146 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 147 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 148 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 149 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 150 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 151 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 152 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 153 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 154 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 155 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 156 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 157 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 158 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 159 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 160 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 161 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 162 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 163 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 164 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 165 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 166 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 167 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 168 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 169 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 170 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 171 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 172 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 173 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 174 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 175 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 176 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 177 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 178 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 179 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 180 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 181 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 182 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 183 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 184 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 185 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 186 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 187 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 188 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 189 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 190 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 191 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 192 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 193 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 194 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 195 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 196 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 197 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 198 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 199 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 200 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 201 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 202 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 203 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 204 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 205 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 206 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 207 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 208 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 209 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 210 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 211 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 212 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 213 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 214 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 215 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 216 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 217 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 218 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 219 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 220 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 221 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 222 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 223 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 224 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 225 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 226 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 227 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 228 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 229 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 230 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 231 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 232 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 233 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 234 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 235 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 236 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 237 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 238 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 239 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 240 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 241 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 242 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 243 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 244 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 245 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 246 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 247 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 248 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 249 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 250 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 251 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 252 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 253 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 254 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 255 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 256 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 257 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 258 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 259 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 260 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 261 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 262 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 263 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 264 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 265 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 266 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 267 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 268 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 269 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 270 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 271 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 272 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 273 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 274 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 275 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 276 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 277 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 278 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 279 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 280 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 281 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 282 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 283 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 284 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 285 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 286 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 287 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 288 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 289 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 290 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 291 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 292 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 293 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 294 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 295 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 296 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 297 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 298 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 299 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 300 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 301 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 302 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 303 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 304 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 305 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 306 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 307 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 308 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 309 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 310 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 311 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 312 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 313 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 314 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 315 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 316 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 317 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 318 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 319 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 320 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 321 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 322 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 323 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 324 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 325 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 326 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 327 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 328 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 329 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 330 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 331 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 332 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 333 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 334 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 335 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 336 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 337 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 338 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 339 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 340 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 341 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 342 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 343 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 344 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 345 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 346 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 347 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 348 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 349 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 350 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 351 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 352 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 353 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 354 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 355 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 356 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 357 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 358 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 359 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 360 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 361 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 362 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 363 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 364 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 365 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 366 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 367 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 368 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 369 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 370 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 371 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 372 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 373 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 374 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 375 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 376 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 377 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 378 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 379 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 380 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 381 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 382 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 383 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 384 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 385 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 386 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 387 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 388 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 389 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 390 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 391 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 392 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 393 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 394 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 395 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 396 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 397 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 398 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 399 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 400 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 401 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 402 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 403 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 404 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 405 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 406 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 407 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 408 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 409 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 410 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 411 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 412 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 413 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 414 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 415 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 416 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 417 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 418 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 419 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 420 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 421 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 422 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 423 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 424 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 425 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 426 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 427 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 428 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 429 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 430 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 431 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 432 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 433 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 434 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 435 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 436 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 437 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 438 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 439 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 440 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 441 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 442 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 443 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 444 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 445 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 446 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 447 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 448 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 449 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 450 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 451 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 452 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 453 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 454 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 455 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 456 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 457 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 458 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 459 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 460 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 461 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 462 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 463 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 464 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 465 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 466 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 467 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 468 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 469 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 470 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 471 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 472 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 473 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 474 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 475 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 476 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 477 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 478 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 479 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 480 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 481 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 482 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 483 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 484 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 485 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 486 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 487 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 488 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 489 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 490 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 491 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 492 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 493 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 494 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 495 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 496 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 497 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 498 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 499 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 500 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 501 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 502 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 503 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 504 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 505 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 506 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 507 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 508 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 509 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 510 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 511 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 512 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 513 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 514 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 515 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 516 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 517 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 518 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 519 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 520 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 521 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 522 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 523 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 524 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 525 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 526 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 527 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 528 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 529 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 530 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 531 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 532 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 533 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 534 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 535 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 536 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 537 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 538 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 539 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 540 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 541 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 542 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 543 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 544 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 545 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 546 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 547 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 548 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 549 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 550 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 551 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 552 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 553 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 554 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 555 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 556 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 557 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 558 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 559 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 560 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 561 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 562 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 563 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 564 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 565 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 566 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 567 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 568 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 569 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 570 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 571 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 572 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 573 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 574 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 575 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 576 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 577 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 578 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 579 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 580 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 581 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 582 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 583 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 584 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 585 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 586 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 587 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 588 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 589 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 590 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 591 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
