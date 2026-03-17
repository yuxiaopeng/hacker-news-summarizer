# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-17.md)

*最后自动更新时间: 2026-03-17 18:25:20*
## 1. 微软“不可破解”的 Xbox One 已被“Bliss”破解

**原文标题**: Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

**原文链接**: [https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)

在被认为“不可破解”十多年后，微软的 Xbox One 终于被攻破了。一名代号为“Bliss”的安全研究员成功绕过了该主机的复杂安全层，实现了在系统各个层面运行未签名代码。

该漏洞利用了一种名为**电压故障注入（voltage glitching）**的硬件技术。通过精确控制主机电源供应的波动时间，研究人员成功干扰了 AMD 平台安全处理器（PSP）在启动过程中的安全检查。这一漏洞提供了对系统硬件的深度访问权限，使得运行自制软件、定制操作系统以及进行以往无法实现的深度技术修改成为可能。

这一突破具有重要意义，因为 2013 年发布的 Xbox One 采用了复杂的“虚拟机管理程序（hypervisor）”和安全启动链，其保持不被破解的时间远超其前代产品 Xbox 360 以及同世代对手 PlayStation 4。

“Bliss”漏洞利用适用于初代 Xbox One 以及 Xbox One S 和 Xbox One X 机型。由于这是一个硬件层面的漏洞，微软很难通过标准的软件更新对现有设备进行修补。虽然该过程目前需要专业的硬件知识和物理改装——这意味着面向普通大众的简易“越狱”方案尚未问世——但它标志着主机黑客社区的一个历史性里程碑，并终结了 Xbox One 长期以来坚不可摧的神话。

---

## 2. Kagi 小众网络

**原文标题**: Kagi Small Web

**原文链接**: [https://kagi.com/smallweb/](https://kagi.com/smallweb/)

**Kagi Small Web** 是由 Kagi 搜索引擎发起的一项倡议，旨在复兴并挖掘“独立网络”。它旨在为日益被 SEO 驱动的内容、侵入性广告和 AI 生成的噪音所主导的现代互联网提供一种替代选择。通过专注于非商业性、以人为本的网站，该项目将用户与个人博客、匠心网站和分众社区连接起来，而这些内容在传统的搜索结果中往往被深埋。

该项目包含三个主要组件：

1.  **Small Web Feed：** 一个精选的实时信息流，汇集了来自高质量个人博客和独立创作者的最新动态。
2.  **Small Web Index：** 一个专门的搜索引擎，仅抓取小型独立域名，让用户在不受商业干扰的情况下发现独特的观点。
3.  **Teacup：** 一个轻量级的集成 RSS 阅读器，帮助用户在纯净、无干扰的环境下关注他们喜爱的独立声音。

其核心理念是通过优先考虑人类的创造力而非算法优化，来对抗互联网的“糟糕化”（enshittification）。Kagi Small Web 鼓励回归“旧互联网”精神——即一个由个人表达、爱好者热情和真实知识共享所定义的数字空间。通过提供这些工具，Kagi 旨在支持独立创作者，并为用户提供一种更有意义、更少商业气息的浏览体验。

---

## 3. Node.js 需要一个虚拟文件系统

**原文标题**: Node.js needs a virtual file system

**原文链接**: [https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system](https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system)

生成摘要时出错

---

## 4. 迈向未经审核 AI 生成代码的自动化验证

**原文标题**: Toward automated verification of unreviewed AI-generated code

**原文链接**: [https://peterlavigne.com/writing/verifying-ai-generated-code](https://peterlavigne.com/writing/verifying-ai-generated-code)

本文提出了关于 AI 生成代码视角的转变：从人工**审查**（逐行阅读代码）转向自动化**验证**（使用机器强制约束来确认正确性）。作者认为，如果 AI 生成的代码满足一系列严格的自动化检查，就可以在无需人工审查的情况下投入生产环境。

作者概述了验证的四个关键约束：
1. **基于属性的测试 (Property-based testing)：** 使用 Hypothesis 等工具测试广泛的半随机输入，确保满足需求且不产生异常。
2. **变异测试 (Mutation testing)：** 使用 *mutmut* 等工具修改代码并确保测试失败。这能将代码限制在必要的逻辑内，防止模型包含冗余代码或通过硬编码测试数据来“作弊”。
3. **副作用预防：** 确保代码不会产生意外后果。
4. **静态分析：** 强制执行类型检查和代码扫描。

一个核心主题是，我们应该将未经审查的 AI 输出视为**编译后的代码**。在这种范式下，人类可读性和可维护性变得次要，代码是否能持续通过其验证套件才是关键。

虽然作者承认，目前设置这些约束的开销与人工审查所花费的时间不相上下，但他们认为这为未来的自动化奠定了基础。通过这些测试缩小“解空间”，无效代码通过的可能性被降至极低，从而可能实现一种“软件工厂”模式，即智能体在无需人工干预的情况下生产出可交付使用的代码。

---

## 5. FFmpeg 8.1

**原文标题**: FFmpeg 8.1

**原文链接**: [https://ffmpeg.org/index.html#pr8.1](https://ffmpeg.org/index.html#pr8.1)

本文记录了 FFmpeg 从 2023 年初到 2026 年初，通过一系列重大和次要版本（版本 6.0 至 8.1）的演进历程。这些更新突显了其在现代化、性能优化和扩展编解码支持方面的重要阶段。

**技术进步**
这些版本的一个主要焦点是集成基于 Vulkan 计算的编解码器和硬件加速。这一转变实现了跨平台、厂商通用的解码/编码流水线，支持包括 H.264、HEVC、AV1、FFv1 和 ProRes 在内的格式。此外，FFmpeg 成功引入并稳定了原生 VVC（多功能视频编码）解码器，并增加了对 xHE-AAC、IAMF（沉浸式音频）和 MV-HEVC（立体编码）的支持。

**性能与基础设施**
该软件进行了多次内部重构以提高效率：
*   **CLI 改进：** `ffmpeg` 命令行工具针对多线程进行了重构，允许解复用器、解码器和过滤器并行运行。
*   **架构：** 7.0 版本迁移至符合 C11 标准的编译器并移除了过时的 API，而 6.0 版本确立了新的年度重大版本发布计划。
*   **优化：** 项目使用更快的 `libavutil/tx` 替换了原有的 FFT/MDCT 实现，并引入了大量的 RISC-V 汇编优化。
*   **数据完整性：** 完成了修复颜色范围协商的大量工作，确保全范围图像在过滤器和编码器中得到正确处理。

**社区与安全**
根据 Coverity 静态分析，FFmpeg 达到了历史最低的缺陷密度，这得益于德国主权科技基金（Sovereign Tech Fund）的资助，该基金于 2024 年成为该项目的首个政府赞助商。项目还通过在 `code.ffmpeg.org` 启动新的托管平台，实现了贡献工作流的现代化。

这些更新共同巩固了 FFmpeg 作为多媒体处理行业标准、跨平台解决方案的地位，在采用尖端硬件 API 与严格内部维护之间取得了平衡。

---

## 6. 发现 Xbox 360 中的 CPU 设计缺陷 (2018)

**原文标题**: Finding a CPU Design Bug in the Xbox 360 (2018)

**原文链接**: [https://randomascii.wordpress.com/2018/01/07/finding-a-cpu-design-bug-in-the-xbox-360/](https://randomascii.wordpress.com/2018/01/07/finding-a-cpu-design-bug-in-the-xbox-360/)

在这篇文章中，前 Xbox 360 CPU 专家 Bruce Dawson 讲述了一个涉及名为 `xdcbt` 的自定义 PowerPC 指令的严重硬件设计缺陷的发现过程。

`xdcbt` 旨在缓解高内存延迟和仅有 1MB 的二级缓存（L2 cache）带来的限制，它是一种“扩展预取”指令，能将数据直接从主内存加载到核心的一级缓存（L1 cache）中，完全绕过二级缓存。虽然这提升了速度，但却破坏了硬件的 MESI 内存一致性协议。由于二级缓存负责跟踪哪些核心持有特定数据，绕过它意味着多个核心最终可能对同一块内存产生冲突且不一致的视图。

最初，Dawson 发现他的内存复制例程导致了堆损坏，因为该例程预取的数据略微超出了缓冲区边界，导致 `xdcbt` 抓取了相邻的元数据，而其他核心当时正在同步修改这些数据。然而，“真正”的漏洞更为隐蔽，且与现代的 **Meltdown（熔断）和 Spectre（幽灵）** 漏洞具有相同的根源：**推测执行**。

即使在开发人员停止显式调用该指令后，Xbox 360 的分支预测器仍会根据预测的代码路径推测性地执行 `xdcbt`。由于 CPU 为了降低延迟会立即启动内存总线事务，并且一旦开始就无法取消，因此错误的分支预测仍会触发破坏缓存的预取操作。

Dawson 通过将所有 `xdcbt` 实例替换为断点验证了这一点。尽管断点从未被触发（证明指令从未被“正式”执行），但崩溃消失了。这证实了即使程序流在技术上从未到达这些指令，它们仍会导致硬件层面的故障。最终，由于分支预测器的不可预测性导致该指令无法受控，它被认为过于危险而无法使用。

---

## 7. 《秘密特工》：探索充满活力却又暴力的巴西 (2025)

**原文标题**: 'The Secret Agent': Exploring a Vibrant, yet Violent Brazil (2025)

**原文链接**: [https://theasc.com/articles/the-secret-agent-cinematography](https://theasc.com/articles/the-secret-agent-cinematography)

《秘密特工》是巴西选送角逐2025年奥斯卡最佳国际影片奖的作品。这是一部以1977年巴西军事独裁末期为背景的政治惊悚片。该片由克莱伯·门多萨·菲略执导，艾夫根尼亚·亚历山德罗娃（AFC）担任摄影指导，讲述了持不同政见者兼技术专家马塞洛（瓦格纳·莫拉饰）在狂欢节周期间，于累西腓四处潜逃的故事。

亚历山德罗娃的摄影手法刻意将影片阴郁、节奏缓慢的主题与充满活力且高饱和度的视觉色调形成对比。她力求捕捉巴西内在的矛盾——即快乐与音乐同苦难与暴力的交织。为了营造出一种富有质感且“不完美”的视觉效果，她选用了阿莱（Arri）Alexa 35摄影机搭配潘那维申（Panavision）B系列经典变形镜头，从而呈现出独特的光晕和像差。在后期制作中，亚历山德罗娃强调色彩分离，摒弃了怀旧的棕褐色调，转而选择在阴影中加入偏红的底色，以还原那个时代巴西摄影的美学风格。

文中重点介绍了两个主要片段：
1. **开场加油站场景：** 一个高景深的长时间审讯镜头，在恶劣天气下拍摄了两周之久。亚历山德罗娃利用12K Dino灯和精密的调色确保了视觉效果的连贯性。
2. **狂欢节序列：** 在观看完电影《凶兆》后，马塞洛加入了一场街头庆典。这一复杂场景动用了庞大的灯光装置（包括SkyPanel和气球灯）来模拟20世纪70年代的街灯。舞者抛撒的面粉营造了独特的质感，象征着一场“死亡之舞”。

最终，影片的技术选择将一段恐怖的政治时代植根于华丽、喜庆的氛围之中，体现了巴西文化在动荡历史中依然保有的“对生命的庆颂”。

---

## 8. Spice Data (YC S19) Is Hiring a Product Specialist

**原文标题**: Spice Data (YC S19) Is Hiring a Product Specialist

**原文链接**: [https://www.ycombinator.com/companies/spice-data/jobs/P0e9MKz-product-specialist-new-grad](https://www.ycombinator.com/companies/spice-data/jobs/P0e9MKz-product-specialist-new-grad)

**Spice Data**, a Y Combinator-backed (S19) startup based in San Francisco, is seeking a **Product Specialist** for a full-time, entry-level role. The company licenses high-quality, cleaned data to Fortune 500 enterprises, with a current focus on the restaurant industry.

**Role and Responsibilities**
The Product Specialist will act as the final quality checkpoint between the data pipeline and customers. Key tasks include:
*   Cleaning raw data and maintaining data mappings.
*   Performing basic data analysis using tools like Excel.
*   Managing third-party contractors involved in data collection.
*   Investigating data inconsistencies and taking initiative in ambiguous situations.

**Candidate Requirements**
The role is open to new graduates and requires a highly organized, detail-oriented individual with strong investigative instincts and clear communication skills. While a technical background is a plus, it is not required. The position is strictly **on-site** in downtown San Francisco five days a week and is open only to US citizens or visa holders.

**Compensation and Benefits**
*   **Salary:** $80,000 – $100,000.
*   **Equity:** 0.1% – 0.5%.
*   **Benefits:** Platinum PPO health insurance, 401k, unlimited PTO, and daily office lunch.

**About the Company**
Founded in 2019, Spice Data is a small, profitable, and lean team with minimal equity dilution. The interview process consists of a 15-minute intro call, two 30-minute skill-based interviews focusing on data cleaning and problem-solving, and a final onsite visit.

---

## 9. Show HN: Antfly: Distributed, Multimodal Search and Memory and Graphs in Go

**原文标题**: Show HN: Antfly: Distributed, Multimodal Search and Memory and Graphs in Go

**原文链接**: [https://github.com/antflydb/antfly](https://github.com/antflydb/antfly)

生成摘要时出错

---

## 10. OpenSUSE Kalpa

**原文标题**: OpenSUSE Kalpa

**原文链接**: [https://kalpadesktop.org/](https://kalpadesktop.org/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 2 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 3 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 4 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 5 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 6 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 7 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 8 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 9 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 10 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 11 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 12 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 13 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 14 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 15 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 16 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 17 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 18 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 19 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 20 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 21 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 22 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 23 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 24 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 25 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 26 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 27 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 28 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 29 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 30 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 31 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 32 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 33 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 34 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 35 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 36 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 37 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 38 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 39 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 40 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 41 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 42 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 43 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 44 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 45 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 46 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 47 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 48 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 49 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 50 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 51 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 52 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 53 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 54 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 55 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 56 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 57 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 58 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 59 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 60 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 61 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 62 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 63 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 64 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 65 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 66 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 67 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 68 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 69 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 70 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 71 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 72 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 73 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 74 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 75 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 76 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 77 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 78 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 79 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 80 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 81 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 82 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 83 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 84 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 85 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 86 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 87 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 88 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 89 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 90 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 91 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 92 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 93 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 94 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 95 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 96 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 97 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 98 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 99 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 100 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 101 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 102 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 103 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 104 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 105 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 106 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 107 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 108 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 109 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 110 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 111 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 112 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 113 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 114 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 115 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 116 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 117 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 118 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 119 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 120 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 121 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 122 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 123 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 124 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 125 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 126 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 127 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 128 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 129 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 130 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 131 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 132 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 133 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 134 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 135 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 136 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 137 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 138 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 139 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 140 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 141 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 142 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 143 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 144 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 145 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 146 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 147 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 148 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 149 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 150 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 151 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 152 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 153 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 154 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 155 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 156 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 157 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 158 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 159 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 160 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 161 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 162 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 163 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 164 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 165 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 166 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 167 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 168 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 169 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 170 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 171 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 172 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 173 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 174 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 175 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 176 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 177 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 178 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 179 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 180 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 181 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 182 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 183 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 184 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 185 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 186 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 187 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 188 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 189 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 190 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 191 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 192 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 193 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 194 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 195 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 196 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 197 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 198 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 199 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 200 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 201 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 202 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 203 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 204 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 205 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 206 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 207 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 208 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 209 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 210 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 211 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 212 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 213 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 214 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 215 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 216 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 217 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 218 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 219 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 220 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 221 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 222 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 223 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 224 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 225 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 226 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 227 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 228 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 229 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 230 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 231 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 232 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 233 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 234 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 235 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 236 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 237 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 238 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 239 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 240 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 241 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 242 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 243 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 244 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 245 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 246 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 247 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 248 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 249 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 250 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 251 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 252 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 253 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 254 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 255 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 256 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 257 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 258 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 259 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 260 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 261 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 262 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 263 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 264 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 265 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 266 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 267 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 268 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 269 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 270 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 271 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 272 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 273 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 274 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 275 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 276 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 277 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 278 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 279 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 280 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 281 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 282 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 283 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 284 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 285 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 286 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 287 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 288 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 289 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 290 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 291 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 292 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 293 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 294 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 295 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 296 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 297 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 298 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 299 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 300 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 301 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 302 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 303 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 304 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 305 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 306 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 307 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 308 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 309 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 310 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 311 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 312 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 313 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 314 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 315 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 316 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 317 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 318 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 319 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 320 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 321 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 322 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 323 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 324 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 325 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 326 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 327 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 328 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 329 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 330 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 331 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 332 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 333 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 334 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 335 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 336 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 337 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 338 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 339 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 340 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 341 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 342 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 343 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 344 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 345 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 346 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 347 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 348 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 349 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 350 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 351 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 352 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 353 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 354 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 355 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 356 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 357 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 358 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 359 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 360 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 361 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 362 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
