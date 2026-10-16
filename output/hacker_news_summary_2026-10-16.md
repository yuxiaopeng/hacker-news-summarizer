# Hacker News 热门文章摘要 (2026-10-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Piramidal (YC W24) Is Hiring

**原文标题**: Piramidal (YC W24) Is Hiring

**原文链接**: [https://job-boards.greenhouse.io/piramidalinc/jobs/4443102009](https://job-boards.greenhouse.io/piramidalinc/jobs/4443102009)

生成摘要时出错

---

## 12. 利用 Claude 设计更高效的量子电路

**原文标题**: Designing more efficient quantum circuits with Claude

**原文链接**: [https://www.anthropic.com/research/designing-efficient-quantum-circuits](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

生成摘要时出错

---

## 13. How the Claude Code team does code review

**原文标题**: How the Claude Code team does code review

**原文链接**: [https://claude.dev/blog/solving-code-review-at-anthropic/](https://claude.dev/blog/solving-code-review-at-anthropic/)

生成摘要时出错

---

## 14. /dev/null: social network for developers

**原文标题**: /dev/null: social network for developers

**原文链接**: [https://dev-null.sh](https://dev-null.sh)

生成摘要时出错

---

## 15. Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD

**原文标题**: Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD

**原文链接**: [https://calif.io/research/big-fish](https://calif.io/research/big-fish)

生成摘要时出错

---

## 16. C++26: The New Debugging Header

**原文标题**: C++26: The New Debugging Header

**原文链接**: [https://www.sandordargo.com/blog/2026/09/30/cpp26-debugging](https://www.sandordargo.com/blog/2026/09/30/cpp26-debugging)

生成摘要时出错

---

## 17. Show HN: Gemini 4 Argon plays StarCraft

**原文标题**: Show HN: Gemini 4 Argon plays StarCraft

**原文链接**: [https://starskirmish.com/bench/v0-2/](https://starskirmish.com/bench/v0-2/)

生成摘要时出错

---

## 18. What on Earth Is Dekton?

**原文标题**: What on Earth Is Dekton?

**原文链接**: [https://www.worksinprogress.news/p/porcelain](https://www.worksinprogress.news/p/porcelain)

生成摘要时出错

---

## 19. 被盗雷诺阿画作于空心砖墙后被发现，且已受损。

**原文标题**: Stolen Renoir paintings found hidden, and damaged, behind cinder block wall

**原文链接**: [https://www.cbsnews.com/news/stolen-renoir-paintings-found-behind-wall-france/](https://www.cbsnews.com/news/stolen-renoir-paintings-found-behind-wall-france/)

生成摘要时出错

---

## 20. Anthropic assigned highest junk credit rating in June

**原文标题**: Anthropic assigned highest junk credit rating in June

**原文链接**: [https://www.ft.com/content/5a310aee-f555-4266-874c-b1b4db20186d](https://www.ft.com/content/5a310aee-f555-4266-874c-b1b4db20186d)

生成摘要时出错

---

## 21. GifCities

**原文标题**: GifCities

**原文链接**: [https://gifcities.org/](https://gifcities.org/)

生成摘要时出错

---

## 22. I Love Software Rendering

**原文标题**: I Love Software Rendering

**原文链接**: [https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/](https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/)

生成摘要时出错

---

## 23. Woman who rescued injured crow keeps getting 'thank-you gifts' from birds [video]

**原文标题**: Woman who rescued injured crow keeps getting 'thank-you gifts' from birds [video]

**原文链接**: [https://www.youtube.com/watch?v=sjNpfz4UzqU](https://www.youtube.com/watch?v=sjNpfz4UzqU)

生成摘要时出错

---

## 24. Monte-Carlo Simulations

**原文标题**: Monte-Carlo Simulations

**原文链接**: [https://eli.thegreenplace.net/2026/monte-carlo-simulations/](https://eli.thegreenplace.net/2026/monte-carlo-simulations/)

生成摘要时出错

---

## 25. RFC8950: Announce IPv4 with an IPv6 next-hop

**原文标题**: RFC8950: Announce IPv4 with an IPv6 next-hop

**原文链接**: [https://anuragbhatia.com/post/2026/06/rfc8950-announce-ipv4-with-ipv6-next-hop/](https://anuragbhatia.com/post/2026/06/rfc8950-announce-ipv4-with-ipv6-next-hop/)

生成摘要时出错

---

## 26. Show HN: Stoke Money – Personal finance app built around a cash flow forecast

**原文标题**: Show HN: Stoke Money – Personal finance app built around a cash flow forecast

**原文链接**: [https://stoke.money](https://stoke.money)

生成摘要时出错

---

## 27. Making 1,750 programmable PCB badges for Canada's biggest hackathon

**原文标题**: Making 1,750 programmable PCB badges for Canada's biggest hackathon

**原文链接**: [https://va3ndf.com/blog/hacker-badges/](https://va3ndf.com/blog/hacker-badges/)

生成摘要时出错

---

## 28. Is Liquid Metal Killing Our PCs? Scientific Analysis and a 2-Year Test [video]

**原文标题**: Is Liquid Metal Killing Our PCs? Scientific Analysis and a 2-Year Test [video]

**原文链接**: [https://www.youtube.com/watch?v=eF6bMSjPepM](https://www.youtube.com/watch?v=eF6bMSjPepM)

生成摘要时出错

---

## 29. Yet another way to invoke functions without parentheses

**原文标题**: Yet another way to invoke functions without parentheses

**原文链接**: [https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/)

生成摘要时出错

---

## 30. US Rep Announces Congressional Legislation to Protect Video Game Ownership

**原文标题**: US Rep Announces Congressional Legislation to Protect Video Game Ownership

**原文链接**: [https://ritchietorres.house.gov/posts/rep-torres-announces-power-to-the-players-act-legislation-to-ensure-gamers-own-their-games](https://ritchietorres.house.gov/posts/rep-torres-announces-power-to-the-players-act-legislation-to-ensure-gamers-own-their-games)

生成摘要时出错

---

## 31. How to make System 1 LLMs show System 2 competencies?

**原文标题**: How to make System 1 LLMs show System 2 competencies?

**原文链接**: [https://onlinelibrary.wiley.com/doi/epdf/10.1002/aaai.70113](https://onlinelibrary.wiley.com/doi/epdf/10.1002/aaai.70113)

生成摘要时出错

---

## 32. Postgres 19 delayed after AI reviewers find more bugs than humans can fix

**原文标题**: Postgres 19 delayed after AI reviewers find more bugs than humans can fix

**原文链接**: [https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471)

生成摘要时出错

---

## 33. Inside Polymarket's paid quote-retweet esports program

**原文标题**: Inside Polymarket's paid quote-retweet esports program

**原文链接**: [https://www.readergrev.com/p/polymarket-paid-quote-retweet-esports-investigation](https://www.readergrev.com/p/polymarket-paid-quote-retweet-esports-investigation)

生成摘要时出错

---

## 34. You could have invented transformers from memory

**原文标题**: You could have invented transformers from memory

**原文链接**: [https://alexwang.ai/posts/associative-memory/](https://alexwang.ai/posts/associative-memory/)

生成摘要时出错

---

## 35. Show HN: rStation – A shared research lab for your AI agents

**原文标题**: Show HN: rStation – A shared research lab for your AI agents

**原文链接**: [https://rstation.ai/](https://rstation.ai/)

生成摘要时出错

---

## 36. Show HN: Weatherdeck – a read-only status board for AI coding agent lanes

**原文标题**: Show HN: Weatherdeck – a read-only status board for AI coding agent lanes

**原文链接**: [https://github.com/Moshik21/weatherdeck](https://github.com/Moshik21/weatherdeck)

生成摘要时出错

---

## 37. Will MOOCs Destroy Academia? (2012)

**原文标题**: Will MOOCs Destroy Academia? (2012)

**原文链接**: [https://cacm.acm.org/opinion/will-moocs-destroy-academia/](https://cacm.acm.org/opinion/will-moocs-destroy-academia/)

生成摘要时出错

---

## 38. The Economic Complexity of the Western Roman Empire

**原文标题**: The Economic Complexity of the Western Roman Empire

**原文链接**: [https://www.michelecoscia.com/?p=2613](https://www.michelecoscia.com/?p=2613)

生成摘要时出错

---

## 39. How gyroscopes got so small [video]

**原文标题**: How gyroscopes got so small [video]

**原文链接**: [https://www.youtube.com/watch?v=0Zc_6xB5W3Y](https://www.youtube.com/watch?v=0Zc_6xB5W3Y)

生成摘要时出错

---

## 40. AI-assisted PCB design for KiCad 10

**原文标题**: AI-assisted PCB design for KiCad 10

**原文链接**: [https://github.com/mixelpixx/Konnect](https://github.com/mixelpixx/Konnect)

生成摘要时出错

---

## 41. Show HN: Wonderhop – A daily game: guess what most people say, or what none do

**原文标题**: Show HN: Wonderhop – A daily game: guess what most people say, or what none do

**原文链接**: [https://wonderhop.io/en/](https://wonderhop.io/en/)

生成摘要时出错

---

## 42. Chicago-Area Cops Helped HSI Spy on Minnesota Anti-ICE Activists

**原文标题**: Chicago-Area Cops Helped HSI Spy on Minnesota Anti-ICE Activists

**原文链接**: [https://www.wired.com/story/chicago-area-cops-helped-hsi-spy-on-minnesota-anti-ice-activists/](https://www.wired.com/story/chicago-area-cops-helped-hsi-spy-on-minnesota-anti-ice-activists/)

生成摘要时出错

---

## 43. AB Fab – On Anthony Burgess

**原文标题**: AB Fab – On Anthony Burgess

**原文链接**: [https://www.lrb.co.uk/the-paper/v48/n18/ian-penman/ab-fab](https://www.lrb.co.uk/the-paper/v48/n18/ian-penman/ab-fab)

生成摘要时出错

---

## 44. Show HN: 2026 Midterms Tracker blends polls and Kalshi/Poymarket odds

**原文标题**: Show HN: 2026 Midterms Tracker blends polls and Kalshi/Poymarket odds

**原文链接**: [https://pressaudit.org/midterms-2026](https://pressaudit.org/midterms-2026)

生成摘要时出错

---

## 45. A story of WiFi secrets, UART lockdowns and a damaged flash memory chip

**原文标题**: A story of WiFi secrets, UART lockdowns and a damaged flash memory chip

**原文链接**: [https://adepts.of0x.cc/eufy-homestation2-firmware/](https://adepts.of0x.cc/eufy-homestation2-firmware/)

生成摘要时出错

---

## 46. Bark: The Toll-Free BBS for 90s Teens

**原文标题**: Bark: The Toll-Free BBS for 90s Teens

**原文链接**: [https://blog.bityard.net/articles/2026/October/bark-the-toll-free-bbs-for-90s-teens](https://blog.bityard.net/articles/2026/October/bark-the-toll-free-bbs-for-90s-teens)

生成摘要时出错

---

## 47. The Folders Programming Language

**原文标题**: The Folders Programming Language

**原文链接**: [https://danieltemkin.com/esolangs/folders](https://danieltemkin.com/esolangs/folders)

生成摘要时出错

---

## 48. MS Paint Adds Freeform Rotation (2026)

**原文标题**: MS Paint Adds Freeform Rotation (2026)

**原文链接**: [https://blogs.windows.com/windows-insider/2026/02/20/announcing-windows-11-insider-preview-build-28020-1619-canary-channel/](https://blogs.windows.com/windows-insider/2026/02/20/announcing-windows-11-insider-preview-build-28020-1619-canary-channel/)

生成摘要时出错

---

## 49. Two-Stack Sliding-Window Aggregation

**原文标题**: Two-Stack Sliding-Window Aggregation

**原文链接**: [https://orlp.net/blog/two-stack-sliding-window-aggregation/](https://orlp.net/blog/two-stack-sliding-window-aggregation/)

生成摘要时出错

---

## 50. Show HN: OneDeploy – Managed open-source apps with nightly backups and TLS

**原文标题**: Show HN: OneDeploy – Managed open-source apps with nightly backups and TLS

**原文链接**: [https://onedeploy.co](https://onedeploy.co)

生成摘要时出错

---

## 51. We don't want decentralized systems, we want small ones

**原文标题**: We don't want decentralized systems, we want small ones

**原文链接**: [https://en.andros.dev/blog/7447ecbb/we-dont-want-decentralized-systems-we-want-small-ones/](https://en.andros.dev/blog/7447ecbb/we-dont-want-decentralized-systems-we-want-small-ones/)

生成摘要时出错

---

## 52. Any window from your Mac, on your iPhone and iPad

**原文标题**: Any window from your Mac, on your iPhone and iPad

**原文链接**: [https://github.com/Saffsanity/sill](https://github.com/Saffsanity/sill)

生成摘要时出错

---

## 53. Meta’s new commercial terms will allow the scraping of news sites: experts

**原文标题**: Meta’s new commercial terms will allow the scraping of news sites: experts

**原文链接**: [https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/)

生成摘要时出错

---

## 54. Untitled Goose Game Studio's Newest Isn't on Xbox Because of BDS Movement

**原文标题**: Untitled Goose Game Studio's Newest Isn't on Xbox Because of BDS Movement

**原文链接**: [https://bigwalk.game/xbox/](https://bigwalk.game/xbox/)

生成摘要时出错

---

## 55. Meta employees said Lula's accounts were hindered during Brazil election

**原文标题**: Meta employees said Lula's accounts were hindered during Brazil election

**原文链接**: [https://www.reuters.com/world/americas/meta-employees-said-lulas-accounts-were-hindered-during-brazil-election-folha-2026-10-16/](https://www.reuters.com/world/americas/meta-employees-said-lulas-accounts-were-hindered-during-brazil-election-folha-2026-10-16/)

生成摘要时出错

---

## 56. I sold all my SP500 yesterday morning

**原文标题**: I sold all my SP500 yesterday morning

**原文链接**: [https://twitter.com/dwlz/status/2111116751735791742](https://twitter.com/dwlz/status/2111116751735791742)

生成摘要时出错

---

## 57. Taco Bell drive-thru AI bot increased employee retention by making jobs easier

**原文标题**: Taco Bell drive-thru AI bot increased employee retention by making jobs easier

**原文链接**: [https://fortune.com/2026/10/14/yum-brands-executive-data-center-hate-ai-tools-improvement/](https://fortune.com/2026/10/14/yum-brands-executive-data-center-hate-ai-tools-improvement/)

生成摘要时出错

---

## 58. Expedia Amazoned Hotel Rooms

**原文标题**: Expedia Amazoned Hotel Rooms

**原文链接**: [https://pluralistic.net/2026/10/15/enshittipedia/](https://pluralistic.net/2026/10/15/enshittipedia/)

生成摘要时出错

---

## 59. Muse Spark Open

**原文标题**: Muse Spark Open

**原文链接**: [https://research.meta.ai/blog/muse-spark-open](https://research.meta.ai/blog/muse-spark-open)

生成摘要时出错

---

## 60. Firefox 158 released with JPEG XL support by default

**原文标题**: Firefox 158 released with JPEG XL support by default

**原文链接**: [https://www.firefox.com/en-US/firefox/158.0/releasenotes/](https://www.firefox.com/en-US/firefox/158.0/releasenotes/)

生成摘要时出错

---

## 61. How to Formalize All of Mathematics

**原文标题**: How to Formalize All of Mathematics

**原文链接**: [https://xenaproject.wordpress.com/2026/10/16/how-to-formalize-all-of-mathematics/](https://xenaproject.wordpress.com/2026/10/16/how-to-formalize-all-of-mathematics/)

生成摘要时出错

---

## 62. Infinite Jeffs

**原文标题**: Infinite Jeffs

**原文链接**: [https://www.amazon.com/dp/B0GTJ4P1PT](https://www.amazon.com/dp/B0GTJ4P1PT)

生成摘要时出错

---

## 63. Freedoom on AWS Lambda Web Functions

**原文标题**: Freedoom on AWS Lambda Web Functions

**原文链接**: [https://www.wooditwork.com/freedoom-on-lambda-web-functions/](https://www.wooditwork.com/freedoom-on-lambda-web-functions/)

生成摘要时出错

---

## 64. New 'Super Ice' 10 Times Stronger, Bringing It Close to the Strength of Concrete

**原文标题**: New 'Super Ice' 10 Times Stronger, Bringing It Close to the Strength of Concrete

**原文链接**: [https://www.sciencealert.com/a-new-super-ice-is-10-times-stronger-bringing-it-close-to-the-strength-of-concrete](https://www.sciencealert.com/a-new-super-ice-is-10-times-stronger-bringing-it-close-to-the-strength-of-concrete)

生成摘要时出错

---

## 65. Espresso Machine Can Run Doom

**原文标题**: Espresso Machine Can Run Doom

**原文链接**: [https://www.gamespot.com/articles/this-espresso-machine-can-run-doom/](https://www.gamespot.com/articles/this-espresso-machine-can-run-doom/)

生成摘要时出错

---

## 66. How to Avoid AI Brain Rot

**原文标题**: How to Avoid AI Brain Rot

**原文链接**: [https://twitter.com/MilesCranmer/status/2111105654211608847](https://twitter.com/MilesCranmer/status/2111105654211608847)

生成摘要时出错

---

## 67. Thank You, Deno

**原文标题**: Thank You, Deno

**原文链接**: [https://www.vlt.io/blog/competition-keeps-javascript-moving](https://www.vlt.io/blog/competition-keeps-javascript-moving)

生成摘要时出错

---

## 68. Comparing Chromium Development at Google and Igalia

**原文标题**: Comparing Chromium Development at Google and Igalia

**原文链接**: [https://lwn.net/Articles/1094721/](https://lwn.net/Articles/1094721/)

生成摘要时出错

---

## 69. Neural networks are clean

**原文标题**: Neural networks are clean

**原文链接**: [https://already-clean.goodfire.com/](https://already-clean.goodfire.com/)

生成摘要时出错

---

## 70. Mark Zuckerberg versus the Pint of Guinness

**原文标题**: Mark Zuckerberg versus the Pint of Guinness

**原文链接**: [https://www.wsj.com/arts-culture/food-cooking/mark-zuckerberg-versus-the-pint-of-guinness-94460282](https://www.wsj.com/arts-culture/food-cooking/mark-zuckerberg-versus-the-pint-of-guinness-94460282)

生成摘要时出错

---

## 71. Here's What Telegram Giving Data to the U.S. Government Looks Like

**原文标题**: Here's What Telegram Giving Data to the U.S. Government Looks Like

**原文链接**: [https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/](https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/)

生成摘要时出错

---

## 72. Binary Serialization in Df_game_data

**原文标题**: Binary Serialization in Df_game_data

**原文链接**: [https://blog.demofox.org/2026/10/15/binary-serialization-in-df_game_data/](https://blog.demofox.org/2026/10/15/binary-serialization-in-df_game_data/)

生成摘要时出错

---

## 73. BeBox is a Haiku application that emulates Be Inc.'s BeBox

**原文标题**: BeBox is a Haiku application that emulates Be Inc.'s BeBox

**原文链接**: [https://github.com/johnrash/bebox](https://github.com/johnrash/bebox)

生成摘要时出错

---

## 74. Fruits and Vegetables 50% Less Nutritious Than in the 1960s

**原文标题**: Fruits and Vegetables 50% Less Nutritious Than in the 1960s

**原文链接**: [https://www.independent.co.uk/news/uk/home-news/vegetables-nutrition-soil-quality-decline-b3063325.html](https://www.independent.co.uk/news/uk/home-news/vegetables-nutrition-soil-quality-decline-b3063325.html)

生成摘要时出错

---

## 75. Jev meets the Trolley Problem

**原文标题**: Jev meets the Trolley Problem

**原文链接**: [https://zachlandes.com/trolley-problem/](https://zachlandes.com/trolley-problem/)

生成摘要时出错

---

## 76. It Ain't AGI Until H100s Go for $30 an Hour

**原文标题**: It Ain't AGI Until H100s Go for $30 an Hour

**原文链接**: [https://corbt.com/posts/it-aint-agi-until-h100s-go-for-30-an-hour](https://corbt.com/posts/it-aint-agi-until-h100s-go-for-30-an-hour)

生成摘要时出错

---

## 77. MeshXFS: A clustered filesystem built on XFS, written by AI

**原文标题**: MeshXFS: A clustered filesystem built on XFS, written by AI

**原文链接**: [https://github.com/sshoecraft/meshxfs](https://github.com/sshoecraft/meshxfs)

生成摘要时出错

---

## 78. The engineering that allows articulated buses to bend

**原文标题**: The engineering that allows articulated buses to bend

**原文链接**: [https://www.theautopian.com/you-wont-believe-the-incredible-engineering-that-allows-articulated-buses-to-bend/](https://www.theautopian.com/you-wont-believe-the-incredible-engineering-that-allows-articulated-buses-to-bend/)

生成摘要时出错

---

## 79. Things to know when you get cancer

**原文标题**: Things to know when you get cancer

**原文链接**: [https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/)

生成摘要时出错

---

## 80. Post About Recreating Adobe Tools Using AI Banned per Adobe Request

**原文标题**: Post About Recreating Adobe Tools Using AI Banned per Adobe Request

**原文链接**: [https://www.reddit.com/r/Bard/comments/1wxmqpt/ive_created_open_source_100_rust_cleanroom/](https://www.reddit.com/r/Bard/comments/1wxmqpt/ive_created_open_source_100_rust_cleanroom/)

生成摘要时出错

---

## 81. Why I Still Shun Passkeys

**原文标题**: Why I Still Shun Passkeys

**原文链接**: [https://lapcatsoftware.com/articles/2026/10/6.html](https://lapcatsoftware.com/articles/2026/10/6.html)

生成摘要时出错

---

## 82. RPKI now protects 70% of internet routes

**原文标题**: RPKI now protects 70% of internet routes

**原文链接**: [https://ipinfo.io/blog/rpki-protects-70-internet-routes](https://ipinfo.io/blog/rpki-protects-70-internet-routes)

生成摘要时出错

---

## 83. Wayland desktop for Linux with skeuomorphic design

**原文标题**: Wayland desktop for Linux with skeuomorphic design

**原文链接**: [https://github.com/fyzugx/DEsk](https://github.com/fyzugx/DEsk)

生成摘要时出错

---

## 84. Signal says minister's changes to bill will not persuade it to stay in Canada

**原文标题**: Signal says minister's changes to bill will not persuade it to stay in Canada

**原文链接**: [https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/](https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/)

生成摘要时出错

---

## 85. Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint

**原文标题**: Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint

**原文链接**: [https://huggingface.co/blog/ibm-granite/granite-switch-4-1](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)

生成摘要时出错

---

## 86. Major ICQ security hole (1998)

**原文标题**: Major ICQ security hole (1998)

**原文链接**: [https://opennet.ru/base/maillist/169.txt.html](https://opennet.ru/base/maillist/169.txt.html)

生成摘要时出错

---

## 87. AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware

**原文标题**: AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware

**原文链接**: [https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)

生成摘要时出错

---

## 88. Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1

**原文标题**: Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1

**原文链接**: [https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html](https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html)

生成摘要时出错

---

## 89. iPhone Duo sells out now backordered until next year

**原文标题**: iPhone Duo sells out now backordered until next year

**原文链接**: [https://9to5mac.com/2026/10/16/iphone-duo-pre-orders-now-backordered-to-next-year/](https://9to5mac.com/2026/10/16/iphone-duo-pre-orders-now-backordered-to-next-year/)

生成摘要时出错

---

## 90. Tesla Roadster: It Flies, Flips, and Hits 0-60 in 0.81s

**原文标题**: Tesla Roadster: It Flies, Flips, and Hits 0-60 in 0.81s

**原文链接**: [https://www.notateslaapp.com/news/4837/tesla-roadster-event-recap-it-flies-flips-and-hits-0-60-in-081s](https://www.notateslaapp.com/news/4837/tesla-roadster-event-recap-it-flies-flips-and-hits-0-60-in-081s)

生成摘要时出错

---

## 91. The 8-mile hole in a Hawaii national park that no one can explain

**原文标题**: The 8-mile hole in a Hawaii national park that no one can explain

**原文链接**: [https://www.sfgate.com/national-parks/article/hawaii-volcanoes-park-great-crack-22358849.php](https://www.sfgate.com/national-parks/article/hawaii-volcanoes-park-great-crack-22358849.php)

生成摘要时出错

---

## 92. Show HN: Capy-flash – a 125B MoE model on two 16 GB consumer GPUs

**原文标题**: Show HN: Capy-flash – a 125B MoE model on two 16 GB consumer GPUs

**原文链接**: [https://github.com/ValerioDolci/capy-flash](https://github.com/ValerioDolci/capy-flash)

**Capy-flash** is a specialized inference engine designed to run the massive **Qwen3.8-Flash-Next (125B MoE)** model on consumer-grade hardware—specifically **two 16 GB GPUs** (such as the RTX 5070 Ti). It achieves this through high-efficiency NVFP4 quantization and a hybrid execution strategy.

**Key Technical Features:**
*   **Hybrid GPU/CPU Execution:** To handle the 125B parameters, the engine uses a VRAM cache for routed experts. Experts that do not fit in VRAM are computed on the CPU using AVX-512 kernels, while the rest of the model runs tensor-parallel across the two GPUs via PCIe.
*   **Performance:** The system achieves impressive speeds, including prefill rates of approximately **4,000 tok/s** for large prompts and generation speeds of around **100 tok/s**. It features a median Time to First Token (TTFT) of 1.82s for agentic tasks.
*   **Optimization Techniques:** It utilizes MTP speculative decoding, INT8 KV caching with an elastic budget (up to 262k tokens), and prefix caching to improve efficiency for multi-turn agentic workflows.
*   **High Fidelity:** Benchmarks (GSM8K and MMLU-Pro) indicate that Capy-flash maintains quality nearly identical to NVIDIA’s official datacenter references (GB300), successfully passing complex multi-step coding tasks with zero malformed tool calls.

**Requirements & Compatibility:**
The project requires Linux, an AVX-512 compatible CPU, and at least 70 GB of free system RAM to host the model's experts. It provides an OpenAI- and Anthropic-compatible API and can also serve smaller dense models like **Qwen3.8-27B**. 

Formerly known as `ninfer-tp2`, Capy-flash is an open-source evolution of the `ninfer` framework, optimized specifically for the latest generation of NVIDIA consumer hardware.

---

## 93. Apple routed a graphite pipe through the iPhone Duo's hinge to dissipate heat

**原文标题**: Apple routed a graphite pipe through the iPhone Duo's hinge to dissipate heat

**原文链接**: [https://www.pcmag.com/news/apple-routed-a-graphite-pipe-through-the-iphone-duos-hinge](https://www.pcmag.com/news/apple-routed-a-graphite-pipe-through-the-iphone-duos-hinge)

生成摘要时出错

---

## 94. Show HN: Flipflop – Iroh-powered persistent tunnels for filesharing

**原文标题**: Show HN: Flipflop – Iroh-powered persistent tunnels for filesharing

**原文链接**: [https://github.com/andunieee/flipflop](https://github.com/andunieee/flipflop)

生成摘要时出错

---

## 95. E Ink Kaleido 4

**原文标题**: E Ink Kaleido 4

**原文链接**: [https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4](https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4)

生成摘要时出错

---

## 96. BIPM decides to stop adding leap seconds to UTC

**原文标题**: BIPM decides to stop adding leap seconds to UTC

**原文链接**: [https://www.bipm.org/en/cgpm-2026/resolution-5](https://www.bipm.org/en/cgpm-2026/resolution-5)

生成摘要时出错

---

## 97. Zombie shooter game based in San Francisco sparks online controversy

**原文标题**: Zombie shooter game based in San Francisco sparks online controversy

**原文链接**: [https://www.kron4.com/news/technology-ai/zombie-shooter-game-based-in-san-francisco-sparks-online-controversy/](https://www.kron4.com/news/technology-ai/zombie-shooter-game-based-in-san-francisco-sparks-online-controversy/)

生成摘要时出错

---

## 98. An Apology

**原文标题**: An Apology

**原文链接**: [https://www.elevationlab.com/blogs/news/an-apology](https://www.elevationlab.com/blogs/news/an-apology)

生成摘要时出错

---

## 99. Someone on Torrent Sites Kept Fucking with My Sonarr

**原文标题**: Someone on Torrent Sites Kept Fucking with My Sonarr

**原文链接**: [https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup](https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup)

生成摘要时出错

---

## 100. 100GiB DB Served from a Durable Object

**原文标题**: 100GiB DB Served from a Durable Object

**原文链接**: [https://twitter.com/tantaman/status/2110946680661287406](https://twitter.com/tantaman/status/2110946680661287406)

生成摘要时出错

---

