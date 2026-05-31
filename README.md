# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-31.md)

*最后自动更新时间: 2026-05-31 18:30:41*
## 1. 肌酸可提高大脑能量水平，使阿尔茨海默病认知功能下降减缓30%

**原文标题**: Creatine raise brain energy levels and slow Alzheimer's cognitive decline by 30%

**原文链接**: [https://thesciverse.org/scientists-found-that-the-creatine-supplement-millions-take-for-muscle-gains-is-quietly-raising-brain-energy-levels-and-slowing-early-alzheimers-cognitive-decline-by-30/](https://thesciverse.org/scientists-found-that-the-creatine-supplement-millions-take-for-muscle-gains-is-quietly-raising-brain-energy-levels-and-slowing-early-alzheimers-cognitive-decline-by-30/)

最近的研究（包括2026年的一项临床试验）表明，长期用于促进肌肉生长的补充剂——一水肌酸，具有显著的神经保护作用。作为人体耗能最高的器官，大脑依赖磷酸肌酸系统来快速再生ATP。肌酸充当了至关重要的能量缓冲剂，在记忆编码和解决问题等高代谢需求期间为神经元提供支持。

引用研究的关键发现包括：

*   **阿尔茨海默病：** 在一项具有里程碑意义的试验中，服用肌酸的早期阿尔茨海默病患者与安慰剂组相比，其**认知能力下降速度减缓了30%**。影像学证实，口服补充剂能成功穿过血脑屏障，提高大脑磷酸肌酸水平，并解决由线粒体功能障碍引起的“生物能量危机”。
*   **健康认知表现：** 荟萃分析显示，肌酸能提高健康成人的处理速度、准确性和短时记忆。这些益处在**睡眠不足**等代谢压力状态下尤为显著，肌酸在此时可补偿能量缺口。
*   **心理健康：** 肌酸正成为一种极具前景的**抑郁症**辅助治疗手段。通过改善前额叶皮层和海马体的线粒体功能，它有助于稳定情绪调节所需的能量代谢。

尽管肌酸是目前研究最充分、最安全且最实惠的补充剂之一，但其作为强效“大脑药物”的作用在很大程度上仍未得到充分宣传。虽然与优化肌肉水平相比，优化大脑水平可能需要更高的剂量（最高达20克），但证据表明，长期坚持补充可提供关键的能量储备，既能抵御与年龄相关的认知衰退，又能增强日常心理韧性。

---

## 2. Cloudflare Turnstile 需要可用于指纹识别的 WebGL

**原文标题**: Cloudflare Turnstile requiring fingerprintable WebGL

**原文链接**: [https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting)

本文报道称，Cloudflare Turnstile（一种“验证你是人类”的机器人检测服务）已开始要求通过 WebGL 指纹识别进行设备验证。这一变化实际上封锁了基于 WebKitGTK 的浏览器用户，因为这些浏览器长期以来设有强制性隐私保护措施，会屏蔽或随机化 Cloudflare 目前要求的指纹数据。

作者认为，Cloudflare 的要求是一种伪装成安全的侵入式追踪手段。尽管 Cloudflare 辩称隐私工具会导致合法用户被误认为机器人，但作者指出，这些追踪方法具有极强的侵入性，甚至连苹果的 WebKit 引擎都会对其进行拦截。文章暗示，Safari 浏览器目前之所以能维持运行，很可能只是因为获得了特定豁免。

文章还批评了 Mozilla Firefox 不一致的隐私保护策略。作者指出，Firefox 目前能通过 Turnstile 检测，是因为其 WebGL 指纹保护存在缺陷，泄露的是经过清理的 GPU 特性而非硬编码字符串。此外，Firefox 的“严格”隐私模式默认并不启用 `privacy.resistfingerprinting`。作者警告称，如果 Firefox 用户为了保护隐私而手动开启这些更严格的保护措施，他们很可能会面临与 WebKitGTK 用户同样的无限循环和网站封锁问题。

最后，本文凸显了一个日益严重的冲突：安全服务要求获取唯一的硬件标识符，这实际上排斥了那些优先考虑隐私并使用拒绝被指纹识别的浏览器的用户。

---

## 3. 1-Bit Bonsai Image 4B Image Generation for Local Devices

**原文标题**: 1-Bit Bonsai Image 4B Image Generation for Local Devices

**原文链接**: [https://prismml.com/news/bonsai-image-4b](https://prismml.com/news/bonsai-image-4b)

生成摘要时出错

---

## 4. 戴夫2D

**原文标题**: Dav2d

**原文链接**: [https://jbkempf.com/blog/2026/dav2d/](https://jbkempf.com/blog/2026/dav2d/)

本文介绍了 **dav2d**，这是即将推出的 **AV2 视频编解码器**开源解码器，由开发了极具声望的 **dav1d** 的原班人马（VideoLAN、VLC 和 Two Orioles）打造。

dav2d 的首要目标是为下一代免版税视频提供高性能、跨平台且轻量级的解码器。通过在开放媒体联盟（AOM）尚未敲定 AV2 标准时就开始开发，该团队旨在影响规范本身。这确保了该编解码器保持“软件友好”，并能在广泛的消费级硬件上高效解码，而不是过度倾向于纯硬件实现。

dav2d 的核心技术亮点与目标包括：

*   **性能至上的设计：** 沿袭 dav1d 的理念，该解码器使用 C 语言编写，并将关键路径以底层汇编实现，以最大化硬件效率。
*   **SIMD 优化：** 该项目重点利用 SIMD 指令集，例如针对现代 x86 处理器的 AVX-512 和针对 ARM 架构的 NEON。
*   **可扩展性：** 旨在处理 8K 分辨率和高位深内容（10 位和 12 位）的需求，同时保持极小的内存占用和卓越的多线程能力。
*   **宽松的许可协议：** 该项目采用 BSD-2-Clause 许可，以鼓励其集成到开源和专有软件中。

总而言之，dav2d 代表了一项积极的努力，旨在确保 AV2 生态系统从发布之日起就具备生产就绪能力。通过尽早提供参考级的软件解码器，该团队希望加速 AV2 的普及，并消除经常阻碍新视频标准推广的性能瓶颈。

---

## 5. 可重启序列

**原文标题**: Restartable Sequences

**原文链接**: [https://justine.lol/rseq/](https://justine.lol/rseq/)

Justine 的文章探讨了 **可重启动序列 (rseq)**，这是 Linux 4.18+ 引入的一项特性，能够在不使用传统锁或原子指令的情况下实现线程安全的数据结构。通过允许线程执行在 CPU 迁移层面具备“原子性”的操作，rseq 在现代多核处理器上实现了巨大的性能提升。

**核心性能影响：**
在高核系统上，互斥锁 (mutex) 等传统同步方法会面临严重的争用和“缓存行抖动”。Justine 的演示表明，在 128 核 ARM 系统上，使用 rseq 使其 `malloc` 实现比传统分片 (sharding) 快 34 倍；在 96 核 AMD Threadripper 上则快 43 倍。在点击计数器基准测试中，就 CPU 时间而言，rseq 的效率比 glibc 互斥锁高出数百万倍。

**工作原理：**
Rseq 的功能类似于“微型数据库事务”。线程向内核提供一个包含特定汇编序列的内存地址。如果内核在该序列执行期间抢占或迁移了该线程，它会强制线程跳转到中止处理器 (abort handler) 以重试操作。这确保了线程仅在未被中断且未迁移到其他 CPU 的情况下才完成数据修改，从而有效地消除了对昂贵的互斥锁或原子指令的需求。

**硬件与未来展望：**
文章强调，尽管 ARM Altra CPU 拥有高效的原子指令，但 rseq 仍能提供更卓越的可扩展性。Justine 预测，随着 128 核和 192 核 CPU 成为主流，rseq 将变得至关重要。她认为，所有主要的操作系统、编程语言和数据结构库最终都将进行重新设计以原生支持 rseq，类似于 C11 原子指令的普及。然而目前，它仍是一项需要手写汇编的“秘密”强力工具。

---

## 6. 因蓝牙名称引发警报，美联航一架767客机返航纽瓦克。

**原文标题**: United Airlines 767 returns to Newark after Bluetooth name sparks alert

**原文链接**: [https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

2026年5月30日，美国联合航空（United Airlines）从纽瓦克自由国际机场（EWR）飞往马略卡岛帕尔马（PMI）的UA236航班，因一个蓝牙设备名称触发安全警报，被迫返航。

在横跨大西洋的航程进行约一小时后，机组人员发现了一个名为“BOMB”（炸弹）的可识别蓝牙名称，据报道该设备属于一名青少年乘客。机组人员通过广播系统多次发出警告，要求所有乘客立即关闭蓝牙。在发出最后通牒后，仍有至少两台设备处于激活状态，机长随即宣布进入紧急状态（应答机代码7700），并在大西洋上空掉头返航。

这架波音767-400ER客机于晚上8:50降落在纽瓦克，距离起飞已过去近三个小时。地方和联邦执法人员在现场待命。乘客被要求在不携带个人物品的情况下下机，以便安全团队对客舱和行李进行全面搜查。

在通过第二次TSA安检后，乘客获准于次日凌晨2:30左右乘坐原班机再次出发。此次事件是近期涉及威胁性数字名称的安全恐慌趋势的一部分；本月早些时候，另一架美联航航班也曾因一个具有政治色彩的Wi-Fi热点名称而受到干扰。航空专家指出，尽管此类名称通常只是恶作剧，但为了确保乘客安全，它们均会被视为真实威胁。

---

## 7. AI时代的原型开发速度

**原文标题**: The Speed of Prototyping in the Age of AI

**原文链接**: [https://darylcecile.net/notes/speed-of-prototyping-age-of-ai](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)

在《AI时代的原型设计速度》一文中，作者反思了AI智能体如何从根本上改变了其工程工作流，将主要的瓶颈从手动搭建脚手架转向了高层级的概念化设计。

**核心观点：**

*   **提升效率：** 作者称日常工程任务的速度提高了约4倍。这种速度使得许多原本可能仅停留在构想阶段的多元化项目得以完成，包括系统语言（Sakoa）、符号语言（Kato）以及各种工具。
*   **认知转变：** AI促使开发方式从“逐行编写”向“工程编排”转型。作者现在的关注点在于边界、契约和整体系统设计。这种向AI“描述成功标准”的实践，意外地提升了作者在人际委派和领导力方面的技能。
*   **职业影响：** 生产力的提升让作者能够完成工作中以前被搁置的高影响力贡献，例如自动化内部支持系统，以及将代码空间（codespace）的启动时间缩短50%。
*   **保持技艺：** 为了避免技术退化，作者特意留出时间进行“手动操作”——阅读源代码、不借助辅助进行调试以及手动实现功能。这确保了当AI工具达到极限时，作者依然具备解决问题的能力。
*   **行业背景：** 作者指出这是一种全行业的转变，并引用了Mike McQuaid和Cassidy Williams等同行的例子，他们也在利用智能体来并行化工作，并降低个人实验的门槛。

作者最后总结道，尽管AI并非“魔法”，且存在环境和社交方面的合理担忧，但其目前的价值在于扩大了工程师所能成就的“表面积”，使构建和学习的过程变得更加流畅且充满乐趣。

---

## 8. Odysseus – 自托管 AI 工作空间

**原文标题**: Odysseus – self-hosted AI workspace

**原文链接**: [https://github.com/pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)

**Odysseus** 是一个自托管、隐私优先的 AI 工作空间，旨在为 ChatGPT 和 Claude 等平台提供本地优先的替代方案。它运行在个人硬件上，在提供功能丰富的“本地优先”体验的同时，强调数据主权和用户控制。

**核心功能：**
*   **AI 模型与智能体：** 支持本地（Ollama、vLLM、llama.cpp）和远程（OpenAI、OpenRouter）模型。它拥有一个智能体系统，能够使用工具、访问 Shell、管理文件并利用 MCP（模型上下文协议）。
*   **The Cookbook：** 一个独特的硬件感知实用程序，可扫描用户系统，根据可用显存（VRAM）推荐模型，并管理 GGUF/FP8 格式的下载与服务。
*   **研究与生产力：** 包括用于将资料整合为报告的“深度研究（Deep Research）”、模型并排对比工具以及 AI 辅助文档编辑器。
*   **工作空间集成：** 除聊天外，它还集成了由 AI 自动分拣的电子邮件客户端（IMAP/SMTP）、本地优先的日历（CalDAV）以及任务/笔记管理系统。
*   **记忆：** 使用 ChromaDB 实现持久化的向量化记忆，让智能体能够随着时间推移不断“进化”并记住用户偏好。

**技术概览：**
Odysseus 采用 FastAPI 后端和模块化前端构建，支持移动端响应式布局，并可作为 PWA（渐进式 Web 应用）安装。通过 Docker（推荐方式）可实现流式部署，该方式将应用与 ChromaDB、SearXNG（用于网络搜索）以及 ntfy 捆绑在一起。

**安全与隐私：**
该平台设计秉承“无木马”和本地数据存储原则。它包含强制身份验证、管理员权限管控工具（如 Shell 访问），并建议在涉及网络访问的部署中使用 HTTPS 反向代理（如 Caddy）。所有用户数据都存储在本地的一个 git-ignored（git 忽略）目录中。

Odysseus 为希望根据自身需求构建强大、私密且具备智能体能力的 AI 环境的用户，提供了一个全面的核心枢纽。

---

## 9. London's Free Roof Terraces

**原文标题**: London's Free Roof Terraces

**原文链接**: [https://diamondgeezer.blogspot.com/2026/05/londons-free-roof-terraces.html](https://diamondgeezer.blogspot.com/2026/05/londons-free-roof-terraces.html)

生成摘要时出错

---

## 10. The Website Specification

**原文标题**: The Website Specification

**原文链接**: [https://specification.website/](https://specification.website/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 2 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 3 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 4 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 5 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 6 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 7 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 8 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 9 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 10 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 11 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 12 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 13 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 14 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 15 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 16 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 17 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 18 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 19 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 20 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 21 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 22 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 23 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 24 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 25 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 26 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 27 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 28 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 29 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 30 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 31 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 32 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 33 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 34 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 35 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 36 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 37 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 38 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 39 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 40 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 41 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 42 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 43 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 44 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 45 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 46 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 47 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 48 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 49 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 50 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 51 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 52 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 53 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 54 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 55 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 56 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 57 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 58 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 59 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 60 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 61 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 62 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 63 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 64 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 65 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 66 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 67 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 68 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 69 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 70 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 71 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 72 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 73 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 74 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 75 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 76 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 77 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 78 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 79 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 80 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 81 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 82 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 83 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 84 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 85 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 86 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 87 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 88 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 89 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 90 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 91 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 92 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 93 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 94 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 95 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 96 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 97 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 98 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 99 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 100 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 101 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 102 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 103 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 104 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 105 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 106 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 107 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 108 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 109 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 110 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 111 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 112 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 113 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 114 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 115 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 116 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 117 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 118 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 119 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 120 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 121 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 122 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 123 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 124 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 125 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 126 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 127 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 128 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 129 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 130 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 131 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 132 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 133 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 134 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 135 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 136 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 137 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 138 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 139 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 140 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 141 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 142 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 143 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 144 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 145 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 146 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 147 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 148 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 149 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 150 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 151 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 152 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 153 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 154 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 155 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 156 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 157 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 158 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 159 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 160 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 161 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 162 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 163 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 164 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 165 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 166 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 167 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 168 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 169 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 170 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 171 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 172 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 173 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 174 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 175 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 176 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 177 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 178 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 179 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 180 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 181 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 182 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 183 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 184 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 185 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 186 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 187 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 188 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 189 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 190 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 191 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 192 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 193 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 194 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 195 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 196 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 197 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 198 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 199 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 200 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 201 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 202 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 203 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 204 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 205 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 206 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 207 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 208 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 209 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 210 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 211 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 212 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 213 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 214 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 215 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 216 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 217 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 218 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 219 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 220 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 221 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 222 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 223 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 224 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 225 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 226 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 227 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 228 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 229 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 230 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 231 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 232 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 233 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 234 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 235 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 236 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 237 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 238 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 239 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 240 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 241 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 242 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 243 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 244 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 245 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 246 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 247 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 248 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 249 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 250 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 251 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 252 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 253 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 254 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 255 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 256 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 257 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 258 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 259 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 260 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 261 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 262 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 263 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 264 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 265 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 266 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 267 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 268 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 269 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 270 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 271 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 272 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 273 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 274 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 275 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 276 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 277 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 278 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 279 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 280 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 281 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 282 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 283 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 284 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 285 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 286 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 287 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 288 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 289 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 290 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 291 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 292 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 293 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 294 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 295 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 296 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 297 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 298 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 299 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 300 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 301 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 302 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 303 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 304 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 305 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 306 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 307 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 308 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 309 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 310 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 311 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 312 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 313 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 314 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 315 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 316 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 317 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 318 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 319 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 320 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 321 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 322 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 323 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 324 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 325 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 326 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 327 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 328 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 329 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 330 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 331 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 332 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 333 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 334 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 335 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 336 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 337 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 338 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 339 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 340 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 341 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 342 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 343 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 344 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 345 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 346 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 347 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 348 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 349 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 350 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 351 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 352 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 353 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 354 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 355 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 356 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 357 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 358 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 359 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 360 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 361 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 362 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 363 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 364 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 365 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 366 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 367 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 368 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 369 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 370 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 371 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 372 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 373 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 374 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 375 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 376 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 377 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 378 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 379 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 380 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 381 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 382 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 383 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 384 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 385 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 386 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 387 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 388 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 389 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 390 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 391 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 392 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 393 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 394 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 395 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 396 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 397 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 398 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 399 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 400 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 401 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 402 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 403 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 404 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 405 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 406 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 407 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 408 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 409 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 410 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 411 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 412 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 413 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 414 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 415 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 416 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 417 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 418 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 419 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 420 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 421 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 422 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 423 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 424 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 425 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 426 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 427 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 428 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 429 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 430 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 431 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 432 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 433 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 434 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 435 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 436 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 437 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
