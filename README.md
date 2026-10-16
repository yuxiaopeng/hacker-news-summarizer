# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-16.md)

*最后自动更新时间: 2026-10-16 20:16:25*
## 1. 特斯拉 Roadster

**原文标题**: Tesla Roadster

**原文链接**: [https://www.tesla.com/roadster](https://www.tesla.com/roadster)

特斯拉 Roadster 被定位为一款纯电动超级跑车，旨在树立汽车性能的新标杆。作为全球加速最快的汽车，Roadster 拥有打破纪录的加速性能，0-60 英里/小时加速仅需惊人的 1.9 秒，0-100 英里/小时加速仅需 4.2 秒，完成四分之一英里加速仅需 8.8 秒。

除了极致的速度，该车还拥有卓越的动力表现，轮上扭矩高达 10,000 牛·米，最高时速超过 250 英里。特斯拉还强调了该车的效率和长途续航能力，声称其单次充电续航里程达到行业领先的 620 英里。全轮驱动系统优化了牵引力和操控性，为这些性能表现提供了有力支撑。

在设计方面，Roadster 配备了可收纳于行李箱的轻量化可拆卸玻璃车顶，使其能够转换为敞篷跑车。尽管具备超跑身份，它仍采用了 2+2 座椅布局，可容纳四名乘客。

新款 Roadster 的主要目标是展示电动汽车相对于传统内燃机超跑的技术优势，通过集破纪录的速度、续航和工程技术于一体，旨在挑战燃油性能车的统治地位。

---

## 2. Claude 揭秘 ECDSA 曲线起源

**原文标题**: Claude reveals ECDSA curve origins

**原文链接**: [https://www.anthropic.com/research/ecdsa-curve-origins](https://www.anthropic.com/research/ecdsa-curve-origins)

2026年10月，据报道，Anthropic的AI模型Claude解开了一个困扰界内25年之久的谜团，该谜团涉及生成NIST ECDSA椭圆曲线所用种子的来源。自2000年发布以来，这些由美国国家安全局（NSA）提供的种子一直是激烈猜测的对象，许多研究人员担心其中隐藏着后门。

Claude发现，这些种子并非如传闻中所说是由幽默的短语或复杂的哈希生成的，而是利用一个名为`lrand48`的20世纪90年代标准C库伪随机数生成器（PRNG）生成的。通过分析种子的位模式，Claude确定它们只是以1997年和1998年的Unix时间戳初始化的PRNG输出。该AI利用扫描器识别输出中的特征模式，并采用LLL（Lenstra–Lenstra–Lovász）算法恢复了生成器的内部状态。

这一发现对密码学界具有重大意义：
*   **安全信心：** 研究结果表明，这些参数是通过简单、可重现的过程而非恶意手段选择的，这使得存在故意预置后门的可能性变得极低。
*   **基点来源：** Claude还将几条曲线（如P-192）的基点追溯到了Arjen Lenstra的FreeLIP算术包，解释了该标准中另一个此前未知的方面。
*   **尚存谜团：** 虽然大多数素数曲线和二进制曲线都得到了解释，但B-163曲线的种子以及P-224至P-521的基点仍然是一个谜。

总的来说，这一发现为长达数年的猜测画上了“终句”，证实了世界上使用最广泛的加密标准之一很可能是安全的，且并未受到破坏。

---

## 3. NIST 椭圆曲线种子赏金已被领取

**原文标题**: The NIST Elliptic Curves Seeds Bounty Has Been Claimed

**原文链接**: [https://words.filippo.io/seeds-solved/](https://words.filippo.io/seeds-solved/)

2026年10月16日，来自Anthropic的一个团队成功领取了发现NIST椭圆曲线（P-192, P-224, P-256, P-384 和 P-521）生成种子来源的悬赏奖金。

**核心发现**
该团队揭示，这些种子并非如传闻已久的那样由被遗忘的英文句子生成，而是通过POSIX标准的 **`drand48`** 随机数生成器生成的。这些种子是将1997年至1998年间的UNIX时间戳输入 `srand48()` 并遵循ANSI X9.62流程创建的。研究人员确定了每条曲线对应的具体时间戳和种子序列，证实了其生成过程是确定性的，且与创建时间紧密相关。

**安全意义**
这一发现是密码学透明度的一个重要里程碑。它有力地驳斥了长期存在的阴谋论——尤其是Daniel Bernstein和Tanja Lange曾暗示的，即美国国家安全局（NSA）可能操纵了种子以嵌入“后门”或针对特定的弱曲线。研究结果显示，创作者拥有的“选择自由”仅约30位熵。这不足以蓄意针对特定类别的弱曲线，因为后者通常需要显著更高的自由度（约70位）。

**最终结果**
作者总结认为，这一发现“完成了NIST曲线的声誉修复历程”，使其相比Curve25519等替代方案在某些方面更具优势。这笔奖金通过各方贡献和三倍增长，最终达到36,864美元，已捐赠给Let’s Encrypt背后的非营利组织互联网安全研究小组（ISRG）。Anthropic团队还成功解码了较少见的NIST B曲线（二元域）的种子。

---

## 4. 越狱 PS5 上的 Llama.cpp：在主机上原生运行任何 GGUF 模型

**原文标题**: Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console

**原文链接**: [https://github.com/cobanov/PS5LM](https://github.com/cobanov/PS5LM)

**PS5LM** 是一款开源应用程序，可将越狱后的 PlayStation 5 转换为私密、高性能的人工智能模型服务器。通过利用 **llama.cpp 的 Vulkan 后端**，该工具能够在主机的 RDNA 2 GPU 上原生运行 GGUF 语言模型，并利用 11.4 GB 的共享内存来处理模型和上下文。

**核心功能：**
*   **网络集成：** 它作为一个本地枢纽，提供兼容 **OpenAI 和 Anthropic** 的 API 端点。这使得笔记本电脑、手机和编程工具等外部设备能够将 PS5 作为大语言模型（LLM）请求的后端。
*   **决策模型：** 在 Ollaya 的支持下，该应用支持“决策模型”（如 d1 和 Clef），能够在极短时间内为分类任务提供类型化的、校准后的概率。
*   **电视优化 UI：** 界面实时显示遥测数据（温度、功率、GPU/CPU 负载），并直接在电视屏幕上流式传输当前的聊天请求。
*   **模型管理：** 用户可以直接从 Hugging Face 下载模型到内置存储或 USB 存储设备中。该应用还包含一个针对主机硬件优化的“推荐”模型列表。
*   **性能表现：** PS5 的表现令人印象深刻，Qwen 9B 模型的生成速度约为 **55 tokens/秒 (t/s)**，而较大的 27B 模型约为 **20 t/s**。

**系统

PS5LM 是 PS5 自制软件社区的一个重要里程碑，它将游戏硬件重新利用于私密的本地“边缘人工智能”应用。

---

## 5. JPEG XL 与 AVIF：Web 应用场景对比

**原文标题**: JPEG XL vs. AVIF for web use-cases

**原文链接**: [https://jakearchibald.com/2026/jpeg-xl-vs-avif/](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

本文评估了截至 2026 年底 JPEG XL 与 AVIF 在 Web 场景中的表现，结论是：在大多数场景下，**AVIF 目前是更优的默认选择**。

**主要发现：**
*   **效率：** 对于有损照片，在默认设置下，AVIF 的文件体积通常比 JPEG XL 小 15–25%。在处理屏幕截图和插图时，这一优势更加显著，AVIF 的体积可缩小 30–90%。
*   **性能：** 综合考虑文件体积，AVIF 的编码速度通常更快且占用内存更少。至关重要的是，在中等质量下，AVIF 的解码速度比 JPEG XL 快 2–3 倍，但在极高质量下差距会缩小。
*   **透明度与 HDR：** AVIF 处理透明度的表现远优于 JPEG XL。在 HDR 应用场景中，AVIF 目前处于领先地位，因为 JPEG XL 缺乏浏览器对增益图（gain maps）的功能性支持，这严重限制了跨设备的兼容性。
*   **编码器：** 对于 JPEG XL，较新的 *jixel* 编码器在文件体积和速度方面通常优于标准的 *libjxl*，但在处理复杂的透明度时除外。
*   **渐进式渲染：** 虽然 JPEG XL 提供了“近乎零成本”的渐进式预览，但 AVIF 最近也增加了渐进式支持（目前仅限 Chrome），且提供了更强的控制力及更小的文件体积。

**JPEG XL 的优势领域：**
*   **无损压缩：** JPEG XL 在无损图像方面是明显的赢家，性能显著优于 AVIF 和 WebP。
*   **JPEG 再压缩：** 它可以在不产生额外代间损失的情况下，将现有的 JPEG 文件缩小 9–20%。

**建议：**
作者建议默认使用最高压缩强度设置下的 **AVIF 4:4:4**。JPEG XL 应保留用于无损需求、再压缩旧有 JPEG 存档，或 AVIF 表现欠佳的特定特殊情况。作者指出，由于两种格式都在快速演进，随着编码器的改进，这些建议可能会发生变化。

---

## 6. 美国90%的工作时间花在AI基准测试未能充分覆盖的任务上。

**原文标题**: 90% of US working hours are spent on tasks not covered well by AI benchmarks

**原文链接**: [https://www.mercor.com/research/labor-index/benchmark-map/](https://www.mercor.com/research/labor-index/benchmark-map/)

Mercor Research 的这篇文章揭示了 AI 基准测试与美国实际经济之间的显著差距，指出 90% 的美国工作时间花在现有 AI 基准测试几乎或完全未涵盖的任务上。

Mercor 利用美国劳工部的 O*NET 分类系统（涵盖 923 种职业和近 18,800 项任务），对 29 个高质量基准测试进行了映射，以评估其经济相关性。研究结果包括：

*   **覆盖范围有限：** 在 923 种职业中，仅有 208 种职业的任务在基准测试中拥有至少五个提示词（prompts）代表。在 22 个主要职业类别中，有 6 个完全没有被涵盖的职业。
*   **结构性偏见：** 基准测试的开发并非随机，而是不成比例地针对高薪职业以及已被确定为“AI 暴露度”较高的角色（如软件工程和法律）。虽然基准测试大量涵盖了律师的任务，但几乎完全忽略了法律秘书或法院书记员的任务。
*   **优先考虑“重要性”：** 在特定职业内部，基准测试侧重于被行业专家评为“最重要”的任务，导致中等收入知识性工作的“长尾”部分评估不足。

作者认为，这种覆盖范围的缺失使得准确衡量 AI 在美国人实际从事的工作中的效能变得几乎不可能。这为试图预测 AI 经济影响的政策制定者、企业和劳动者造成了盲点。

尽管 Mercor 尝试了“O*NET 加权法”（一种通过平均模型在特定任务上的表现来得出更准确职业级评分的方法），但目前缺乏多样化且符合经济实际的基准测试数据，限制了该方法的有效性。文章最后指出，必须显著提高基准测试的多样性和忠实度，才能理解 AI 在更广泛经济领域中的真实能力。

---

## 7. Waymo in Toronto

**原文标题**: Waymo in Toronto

**原文链接**: [https://waymo.com/blog/2026/10/waymo-in-toronto/](https://waymo.com/blog/2026/10/waymo-in-toronto/)

Waymo has officially announced its expansion into Canada, selecting Toronto as the first international site for its fully autonomous ride-hailing service. The company aims to welcome its first commercial riders in 2028.

The rollout will follow a phased, safety-first approach. In the coming days, residents will see Waymo vehicles on the streets operating manually to perform high-definition mapping and local validation. This ensures the "Waymo Driver" technology can navigate Toronto’s specific driving conditions and all-weather environment.

To facilitate this expansion, Waymo is partnering with Toronto-headquartered **Element Fleet Management**, which will provide end-to-end fleet solutions. This initiative is expected to create hundreds of local jobs in areas such as vehicle maintenance, validation driving, and customer service. The move strengthens Waymo’s existing Canadian ties, which include manufacturing partner Magna International and investor Canada Pension Plan Investment Board (CPPIB).

Safety and accessibility are central to the mission. Waymo cites data showing its technology is involved in 95% fewer serious crashes than human drivers. Additionally, the company is collaborating with advocacy groups like **BALANCE for Blind Adults** and **CNIB** to ensure the service provides inclusive mobility for the sight-loss community and others with accessibility needs.

Waymo intends for its service to complement Toronto's existing transportation ecosystem, including public transit and bike lanes. Interested residents can now sign up for updates via the company’s website to stay informed as the service nears its 2028 launch.

---

## 8. eBay限制无线电设备刊登，但豁免仅限业余频段的设备。

**原文标题**: eBay Restricts Listings of Radio Equipment, but Exempts Ham-Band-Only Gear

**原文链接**: [https://www.arrl.org/arrlletterissue?issue=2026-10-15#eBay-Restricts-Listings-of-Radio-Equipment_-But-Exempts-Ham-Band-Only-Gear](https://www.arrl.org/arrlletterissue?issue=2026-10-15#eBay-Restricts-Listings-of-Radio-Equipment_-But-Exempts-Ham-Band-Only-Gear)

The October 15, 2026, edition of *The ARRL Letter* highlights significant regulatory changes, emergency response efforts, and organizational updates within the amateur radio community.

**eBay and FCC Regulations**
In response to new FCC rules effective October 13, 2026, aimed at protecting the communications supply chain, eBay has restricted listings of radio transmitting equipment. While the FCC now requires FCC ID numbers for most RF devices sold online, eBay clarified that equipment operating **exclusively** on amateur radio frequencies is exempt. However, VHF/UHF gear capable of operating outside ham bands still requires FCC certification to be listed.

**Emergency Communications**
Amateur radio operators across several Florida counties provided critical communication support during Hurricane Isaias. Volunteers staffed Emergency Operations Centers and evacuation shelters, maintaining a resilient auxiliary link to the State Emergency Operations Center in Tallahassee to ensure data flow if traditional networks failed.

**Leadership and Recognition**
*   **ARRL Leadership:** Ed James, KA8JMW, was appointed Vice Director of the Rocky Mountain Division following the resignation of Mel Parkes, NM7P, due to health reasons.
*   **RCA Awards:** The Radio Club of America announced its 2026 award recipients and Fellows, including Dr. Charles C. Counselman, III, W1HIS, and Jay Adrick, K8CJY. They will be honored at a banquet in New York City on November 21.

**Technical and Educational News**
*   **44Net Expansion:** ARDC is doubling its "points of presence" (PoPs) for 44Net Connect, adding locations in Chicago, Los Angeles, and Sydney to reduce latency for digital experimenters.
*   **Events:** ARRL will host a "On the Air LIVE" webinar on October 27 focused on introducing new hams to contesting. Additionally, America250 W1AW portable activations continue across several states, and the KØDOG club will hold a special event in November to support animal shelters.

---

## 9. 苹果机器学习研究：在 Mac Studio 上通过 MLX 运行 Muse Spark Open

**原文标题**: Apple ML Research: Muse Spark Open with MLX on Mac Studio

**原文链接**: [https://machinelearning.apple.com/research/mlx-distributed-inference](https://machinelearning.apple.com/research/mlx-distributed-inference)

Apple Research has demonstrated the ability to run frontier-class Large Language Models (LLMs) locally on Mac Studio clusters using the **MLX framework**. The highlight is the successful inference of **Muse Spark Open**, a Mixture-of-Experts (MoE) model with nearly one trillion parameters (816B), achieving over 36 tokens per second on a four-node Mac Studio cluster.

The article emphasizes the architectural advantages of the new **M5 Ultra chip**, which features a **GPU Neural Accelerator** for matrix multiplication and 1.2 TB/s of unified memory bandwidth. Compared to the M3 Ultra, the M5 Ultra delivers up to a 4.6x speedup in Time to First Token (TTFT) and a 1.6x increase in generation speed.

To handle models too large for a single machine's 512GB RAM, MLX utilizes two distributed computing strategies powered by **RDMA over Thunderbolt 5** (introduced in macOS 26.2) and the **jaccl** communication backend:

1.  **Pipeline Parallelization:** Distributes the model by depth (layers). This method is easy to implement and speeds up "prefilling" large contexts (up to 65,536 tokens) by overlapping computation across machines.
2.  **Tensor Parallelization:** Distributes the model by width. Although more complex, it significantly increases decode throughput by parallelizing per-layer computations, provided there is low-latency connectivity like Thunderbolt RDMA.

The research benchmarks three models—**Muse Spark Open (816B)**, **Mistral Medium 3.5 (128B)**, and **Qwen 3.8 (27B)**—showing that even the largest models can run efficiently at 4-bit precision (NVFP4). Despite this high performance, the M5 Ultra remains energy-efficient, peaking at 300W. This ecosystem allows researchers to run private, large-scale agentic AI applications locally on desktop hardware.

---

## 10. The Fatal Flaw of 911

**原文标题**: The Fatal Flaw of 911

**原文链接**: [https://www.themarshallproject.org/2026/10/16/911-book-policing-mental-health](https://www.themarshallproject.org/2026/10/16/911-book-policing-mental-health)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 2 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 3 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 4 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 5 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 6 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 7 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 8 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 9 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 10 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 11 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 12 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 13 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 14 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 15 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 16 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 17 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 18 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 19 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 20 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 21 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 22 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 23 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 24 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 25 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 26 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 27 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 28 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 29 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 30 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 31 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 32 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 33 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 34 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 35 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 36 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 37 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 38 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 39 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 40 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 41 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 42 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 43 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 44 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 45 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 46 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 47 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 48 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 49 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 50 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 51 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 52 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 53 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 54 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 55 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 56 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 57 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 58 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 59 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 60 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 61 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 62 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 63 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 64 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 65 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 66 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 67 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 68 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 69 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 70 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 71 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 72 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 73 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 74 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 75 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 76 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 77 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 78 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 79 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 80 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 81 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 82 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 83 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 84 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 85 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 86 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 87 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 88 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 89 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 90 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 91 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 92 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 93 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 94 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 95 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 96 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 97 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 98 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 99 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 100 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 101 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 102 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 103 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 104 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 105 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 106 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 107 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 108 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 109 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 110 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 111 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 112 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 113 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 114 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 115 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 116 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 117 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 118 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 119 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 120 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 121 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 122 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 123 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 124 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 125 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 126 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 127 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 128 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 129 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 130 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 131 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 132 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 133 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 134 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 135 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 136 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 137 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 138 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 139 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 140 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 141 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 142 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 143 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 144 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 145 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 146 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 147 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 148 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 149 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 150 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 151 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 152 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 153 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 154 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 155 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 156 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 157 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 158 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 159 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 160 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 161 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 162 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 163 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 164 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 165 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 166 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 167 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 168 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 169 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 170 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 171 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 172 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 173 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 174 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 175 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 176 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 177 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 178 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 179 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 180 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 181 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 182 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 183 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 184 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 185 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 186 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 187 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 188 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 189 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 190 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 191 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 192 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 193 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 194 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 195 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 196 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 197 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 198 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 199 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 200 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 201 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 202 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 203 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 204 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 205 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 206 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 207 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 208 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 209 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 210 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 211 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 212 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 213 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 214 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 215 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 216 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 217 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 218 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 219 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 220 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 221 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 222 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 223 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 224 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 225 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 226 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 227 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 228 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 229 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 230 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 231 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 232 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 233 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 234 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 235 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 236 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 237 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 238 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 239 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 240 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 241 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 242 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 243 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 244 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 245 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 246 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 247 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 248 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 249 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 250 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 251 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 252 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 253 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 254 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 255 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 256 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 257 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 258 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 259 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 260 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 261 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 262 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 263 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 264 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 265 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 266 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 267 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 268 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 269 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 270 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 271 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 272 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 273 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 274 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 275 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 276 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 277 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 278 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 279 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 280 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 281 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 282 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 283 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 284 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 285 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 286 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 287 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 288 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 289 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 290 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 291 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 292 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 293 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 294 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 295 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 296 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 297 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 298 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 299 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 300 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 301 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 302 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 303 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 304 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 305 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 306 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 307 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 308 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 309 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 310 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 311 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 312 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 313 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 314 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 315 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 316 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 317 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 318 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 319 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 320 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 321 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 322 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 323 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 324 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 325 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 326 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 327 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 328 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 329 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 330 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 331 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 332 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 333 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 334 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 335 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 336 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 337 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 338 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 339 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 340 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 341 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 342 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 343 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 344 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 345 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 346 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 347 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 348 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 349 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 350 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 351 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 352 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 353 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 354 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 355 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 356 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 357 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 358 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 359 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 360 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 361 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 362 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 363 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 364 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 365 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 366 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 367 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 368 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 369 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 370 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 371 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 372 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 373 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 374 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 375 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 376 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 377 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 378 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 379 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 380 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 381 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 382 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 383 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 384 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 385 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 386 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 387 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 388 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 389 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 390 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 391 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 392 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 393 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 394 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 395 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 396 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 397 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 398 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 399 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 400 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 401 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 402 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 403 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 404 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 405 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 406 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 407 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 408 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 409 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 410 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 411 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 412 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 413 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 414 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 415 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 416 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 417 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 418 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 419 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 420 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 421 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 422 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 423 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 424 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 425 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 426 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 427 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 428 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 429 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 430 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 431 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 432 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 433 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 434 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 435 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 436 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 437 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 438 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 439 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 440 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 441 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 442 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 443 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 444 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 445 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 446 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 447 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 448 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 449 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 450 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 451 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 452 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 453 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 454 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 455 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 456 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 457 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 458 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 459 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 460 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 461 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 462 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 463 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 464 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 465 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 466 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 467 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 468 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 469 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 470 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 471 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 472 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 473 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 474 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 475 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 476 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 477 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 478 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 479 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 480 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 481 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 482 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 483 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 484 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 485 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 486 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 487 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 488 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 489 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 490 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 491 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 492 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 493 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 494 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 495 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 496 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 497 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 498 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 499 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 500 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 501 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 502 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 503 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 504 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 505 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 506 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 507 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 508 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 509 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 510 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 511 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 512 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 513 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 514 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 515 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 516 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 517 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 518 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 519 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 520 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 521 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 522 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 523 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 524 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 525 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 526 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 527 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 528 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 529 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 530 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 531 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 532 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 533 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 534 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 535 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 536 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 537 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 538 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 539 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 540 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 541 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 542 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 543 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 544 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 545 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 546 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 547 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 548 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 549 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 550 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 551 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 552 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 553 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 554 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 555 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 556 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 557 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 558 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 559 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 560 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 561 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 562 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 563 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 564 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 565 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 566 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 567 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 568 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 569 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 570 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 571 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 572 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 573 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
