# Hacker News 热门文章摘要 (2025-08-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: 我花了六年时间造了个奇葩的木制像素显示器

**原文标题**: Show HN: I spent 6 years building a ridiculous wooden pixel display

**原文链接**: [https://benholmen.com/blog/kilopixel/](https://benholmen.com/blog/kilopixel/)

作者历经六年开发，推出了Kilopixel (kilopx.com)，这是一个大型且不实用的木制显示器，尺寸为40x25（1000像素），通过网络界面控制，允许互联网上的任何人进行绘制。该项目受非传统镜子和慢速电子墨水屏的启发，旨在成为效率最低的显示器。

开发过程涉及众多原型，最初采用木制龙门系统，后转向挤压铝材。一个重大挑战是寻找合适的像素，作者尝试了各种球体（乒乓球、Nerf球等），最终因成本、重量和一致性问题而选择了定制的立方木制像素。作者在像素旋转机制上也遇到了困难，最初考虑使用小型电机和乐高轮子。

最终版本使用CNC机床，配备定制的龙门架，移动到每个像素，并使用独特的“戳动”机制来旋转木块。该系统使用树莓派来查询API获取下一个像素，编写g代码，戳动像素，并读取光传感器以确定其状态。

Web应用程序允许用户提交40x25像素的图像、投票选出提交内容，甚至可以实时协作。作者计划在YouTube上直播显示器，并创建绘制过程的延时视频，期待看到互联网如何与该项目互动，并计划可能将该项目传递下去。

---

## 2. 第一部分：Rust与C内存互操作性深度解析

**原文标题**: Part 1: A Deep Dive into Rust and C Memory Interoperability

**原文链接**: [https://notashes.me/blog/part-1-memory-management/](https://notashes.me/blog/part-1-memory-management/)

第一部分：Rust与C内存互操作深度剖析

本文探讨了混合Rust和C内存分配器的复杂性。首先强调了这种做法的潜在危险，即不正确的内存释放可能导致静默损坏，这是最坏的情况。作者强调理解内存分配器如何运作对于避免意外崩溃和bug的重要性。

文章随后深入探讨了内存基础知识，解释了诸如虚拟内存、虚拟地址如何转化为物理RAM以及与内存访问相关的成本等概念。它描述了堆在动态内存分配中的作用以及碎片化的挑战。CPU缓存架构，包括L1、L2和L3缓存，也被讨论，重点关注“伪共享”及其对性能的负面影响。

文章的重要部分详细介绍了内存测试实验室的创建。这个使用Rust和C构建的框架，旨在通过测试多种分配器实现、处理崩溃、测量性能以及提供详细的调试信息来安全地探索分配器交互。该框架使用子进程隔离、通过FFI加载C库、退出代码分析和性能测量工具。

最后，文章介绍了测试框架中使用的四种不同的C分配器实现：标准的`malloc`封装器、用于检测内存损坏的调试分配器、用于绕过堆的直接`mmap`分配器以及用于快速、临时分配的arena分配器。

---

## 3. 开放式IP摄像头固件

**原文标题**: Open IP Camera Firmware

**原文链接**: [https://openipc.org/à](https://openipc.org/à)

OpenIPC 是一款开源的第三方固件，旨在取代许多使用 ARM 和 MIPS 处理器的 IP 摄像头上封闭源代码、通常过时且不安全的固件。它为用户提供了对其摄像头更大的控制权和安全性。

该固件以预编译二进制文件的形式分发，以便于安装，但完整的源代码也以 MIT 许可证提供，鼓励社区贡献和修改。OpenIPC 项目使用 Buildroot 构建其 Linux 发行版，并利用 Majestic、Mini 或 Venc 流处理器。虽然 Majestic 目前是闭源的，但作者计划在未来获得足够的资金支持后将其开源。

OpenIPC 的主要优势在于它提供的自由。用户可以完全控制他们的摄像头和视频流，从而消除对后门、恶意软件或数据泄露的担忧。该固件优先考虑诸如固件升级和视频/音频流配置等核心功能。

除了基本功能之外，OpenIPC 还支持与 IPEYE 云存储、向 YouTube 和 Telegram 进行视频流、SOCKS5 代理和虚拟隧道的集成。该项目还满足无人机摄像头、建筑头盔、医学研究和水下捕鱼等专业应用的需求。本文还提到了一个支持者部分。

---

## 4. Perplexity 正使用隐蔽的、未声明的爬虫来规避禁止抓取的指令。

**原文标题**: Perplexity is using stealth, undeclared crawlers to evade no-crawl directives

**原文链接**: [https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)

Cloudflare 指责 Perplexity 使用隐形爬虫绕过网站“禁止抓取”指令。Cloudflare 观察到，在使用 robots.txt 和 WAF 规则阻止 Perplexity 声明的爬虫 (PerplexityBot 和 Perplexity-User) 后，Perplexity 仍然使用伪装成通用 Chrome 浏览器的未声明爬虫访问内容。这种“隐形爬虫”使用不同的 IP 和 ASN 来逃避检测和规避屏蔽。

Cloudflare 认为这种行为违反了互联网的信任原则，该原则要求爬虫具有透明度并遵守网站的偏好。相比之下，该文章赞扬 OpenAI 尊重 robots.txt 并且不试图规避屏蔽。

Cloudflare 已采取行动，将 Perplexity 从已验证的机器人列表中移除，并添加规则到其管理系统中以阻止这种隐形爬虫。 现有的拥有机器人管理规则的 Cloudflare 客户已经受到保护。该公司还提供了挑战来自可疑机器人的请求的选项，提供进一步的保护。

文章最后强调了 Cloudflare 对内容独立日（Content Independence Day）的承诺，该活动旨在让内容创作者控制 AI 如何访问他们的内容。Cloudflare 正在与技术和政策专家合作，为行为良好的机器人运营商建立明确的原则，并调整其方法来对抗不断演变的规避技术。

---

## 5. 事实无法拯救你 - 人工智能、历史与苏联科幻

**原文标题**: Facts will not Save You - AI, History and Soviet Sci-Fi

**原文链接**: [https://hegemon.substack.com/p/facts-will-not-save-you](https://hegemon.substack.com/p/facts-will-not-save-you)

无法访问文章链接。

---

## 6. 我理想的数组语言

**原文标题**: My Ideal Array Language

**原文链接**: [https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html](https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html)

本文概述了作者对理想数组语言的愿景，强调语言和编译器需要适应现代硬件日益增长的异构性。关键特性包括用户可扩展的秩多态、具有自动缓冲区化的值语义以及编译器透明性。

作者认为，秩多态对于数组语言至关重要，它允许用户编写自己的多态内核。他们强调了值语义和自动缓冲区化的优势，并将其与Fortran因其数组语义而生成高性能代码的能力相提并论。本文深入探讨了MLIR在数组编译中的作用，特别是张量和memref类型，展示了函数式数组语言如何与编译器内部表示很好地对齐。

本文强调了基于语言语义进行优化的编译步骤（离线或在线）的重要性。编译器透明性和可检查性被认为是至关重要的，它允许用户了解优化失败并调试性能问题。作者引用了LLVM的remarks框架作为很好的例子，尽管它面向编译器工程师。最终，本文倡导一种数组语言，该语言赋予用户控制和洞察编译过程的能力，使他们能够编写针对各种硬件架构优化的高效代码。

---

## 7. 日本沿海的百年石头“海啸石”（2015年）

**原文标题**: Century-Old Stone “Tsunami Stones” Dot Japan's Coastline (2015)

**原文链接**: [https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/](https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/)

本文探讨了日本历史上竖立“海啸石”的做法，旨在警示后代在沿海地区建设的危险。这些石头，有些可以追溯到1896年毁灭性海啸之后，提醒人们在地震后寻找更高地势以避免后续海浪。本文重点介绍了姉吉的海啸石，它明确指示人们不要在其下方建造房屋。

历史学家北原糸子强调，这些石头是跨世代的警告，旨在防止未来的苦难。然而，随着时间的推移，随着沿海城镇的扩张和对海堤的信任，它们的意义往往被忽视。尽管如此，一些社区，如姉吉，继续听取石头的警告，这在2011年的海啸中证明至关重要。

本文还提到，海啸在地名上留下了印记，指示着安全或危险的地点。今村文彦指出，灾难的记忆往往在三代之后消退，导致警告被遗忘。文章最后提到了2011年海啸和福岛第一核电站事故的持续恢复，强调了理解和尊重沿海地区潜在危险的持续重要性。

---

## 8. 科学家用激光照射人头

**原文标题**: Scientists shine a laser through a human head

**原文链接**: [https://spectrum.ieee.org/optical-brain-imaging](https://spectrum.ieee.org/optical-brain-imaging)

科学家首次成功地将激光穿透人头。这项由BiomedicalNews报道的突破是开发潜在的廉价新型医学成像技术的重要一步。格拉斯哥大学极端光研究小组的研究人员通过将激光中的光子穿过颅骨和大脑发送到另一侧的探测器来实现的。提供的图像显示了50个光子从激光器（红色）到探测器（绿色）的潜在路径。虽然文章没有详细说明成像技术的具体细节，但它清楚地表明，光线穿透颅骨的能力是其发展的根本。这一成就意义重大，因为它表明与现有的MRI或CT扫描等技术相比，有可能获得更经济实惠的医学成像解决方案。

---

## 9. 求职者躲避AI面试官

**原文标题**: Job-seekers are dodging AI interviewers

**原文链接**: [https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/](https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/)

财富杂志文章探讨了公司使用人工智能进行面试的日益增长的趋势，以及由此产生的求职者反弹。 虽然人力资源部门将人工智能面试官视为高效处理大量求职者和腾出时间进行更有意义的后期对话的方式，但许多候选人认为这种体验不人性化且无效。

求职者将人工智能面试描述为尴尬、冷漠，甚至是一个表明公司文化不佳的危险信号。他们对重复提问、人工智能无法回答有关公司的问题以及感觉自己被低估表示沮丧。有些人完全拒绝参加人工智能面试，宁愿冒着继续失业的风险，也不愿让自己接受这个过程。

该文章突出了对比鲜明的观点：人力资源专业人士强调节省时间的好处以及专注于优秀候选人的能力，而求职者则感叹缺乏人际交往，并对工作过度自动化的未来表示担忧。

尽管求职者的负面反馈，提供人工智能面试解决方案的公司声称他们的客户对结果感到满意，这表明该技术将继续存在，特别是在初始筛选阶段。 然而，即使是人工智能的支持者也承认其局限性，尤其是在评估文化契合度方面，突显了在招聘过程中仍然需要人的参与。

---

## 10. Show HN：为孩子们制作的迷你逻辑和数字游戏

**原文标题**: Show HN: Tiny logic and number games I built for my kids

**原文链接**: [https://quizmathgenius.com/](https://quizmathgenius.com/)

这个“Show HN”帖子介绍了一系列为作者孩子制作的微型逻辑和数字游戏。内容比较简单，主要由标题和导航元素“Prev”和“Next”组成，暗示可以通过这些导航链接访问一系列游戏。大脑表情符号“🧠”强化了这些游戏是基于谜题或逻辑的想法。该帖子强调了作者的个人动机（为他们的孩子制作游戏），并隐式地邀请其他人探索这个合集。

---

## 11. 具有原位训练功能的GHz脉冲神经形态光子芯片

**原文标题**: GHz spiking neuromorphic photonic chip with in-situ training

**原文链接**: [https://arxiv.org/abs/2506.14272](https://arxiv.org/abs/2506.14272)

本文（arXiv:2506.14272）报道了神经形态光子计算领域的重大进展。由项金龙和郭旭涵领导的作者团队展示了一种具有原位训练能力的GHz脉冲神经形态光子芯片。

核心创新是一种基于硅平台的互补金属氧化物半导体（CMOS）兼容光子脉冲神经网络（PSNN）芯片。该芯片通过千兆赫兹级的非线性脉冲动力学、基于监督突触可塑性的原位学习以及受视网膜启发的脉冲编码，模拟大脑类功能。这些特性解决了时空数据集成和节能动态处理中的关键挑战。

该PSNN芯片实现了无帧、事件驱动的操作。作者在KTH视频识别数据集上展示了其性能，实现了80%的准确率，同时处理速度比传统的基于帧的方法快约100倍。

这项研究代表了神经形态计算领域的一大进步，由于其低延迟和高吞吐量，有望在自动驾驶汽车和机器人导航等应用中实现实时动态视觉处理和自适应决策。该论文详细介绍了芯片的架构和性能，包括18页内容和4张图。

---

## 12. 微软市值突破4万亿美元：对MSFT是好消息，对员工则未必

**原文标题**: Microsoft tops $4T in valuation: Great news for MSFT, not so great for workers

**原文链接**: [https://www.computerworld.com/article/4032921/microsoft-tops-4t-in-valuation-great-news-for-the-company-not-so-great-for-its-workers.html](https://www.computerworld.com/article/4032921/microsoft-tops-4t-in-valuation-great-news-for-the-company-not-so-great-for-its-workers.html)

微软市值突破四万亿背后的裁员困境：AI替代人工是否得不偿失？

---

## 13. 软件需要“独立审计员”

**原文标题**: Software needs an "independent auditor"

**原文链接**: [https://www.greptile.com/blog/auditor](https://www.greptile.com/blog/auditor)

AI代码审查工具Greptile联合创始人Daksh认为，软件开发越来越依赖AI生成的代码，因此需要独立的审计工具，类似于安然丑闻后金融行业对独立审计师的依赖。他将安达信同时为安然提供审计和咨询服务所存在的利益冲突，与Greptile如果也生成代码可能产生的冲突进行了类比。

Daksh解释说，Greptile故意避免生成代码，以保持其代码审查过程的公正性。他认为，如果Greptile也提供代码生成工具（“GrepIDE”），那么它公正地审查代码，尤其是审查自身代码的能力和意愿将会受到影响。就像财务审计师必须保持独立以确保公正评估一样，代码审查者应该与代码生成者区分开来。

文章强调，AI编码代理会产生人类可能忽略的独特错误，例如虚构的函数或对无关文件的意外更改。随着AI生成代码数量的增加，在拉取请求阶段进行自动化的对抗性审查变得至关重要。核心观点：像Greptile这样的独立AI代码审查工具对于确保使用AI构建的软件的质量和可靠性至关重要。

---

## 14. 技嘉最新BIOS更新移除B650主板的PCIe 5.0支持

**原文标题**: Gigabyte removes PCIe 5.0 support from B650 motherboards in latest BIOS update

**原文链接**: [https://videocardz.com/newz/gigabyte-removes-unofficial-pcie-5-0-support-from-b650-motherboards-in-latest-bios-update](https://videocardz.com/newz/gigabyte-removes-unofficial-pcie-5-0-support-from-b650-motherboards-in-latest-bios-update)

技嘉在新版BIOS中移除了B650系列主板的非官方PCIe 5.0支持。部分B650主板，特别是那些带有外部时钟发生器的型号，之前一直在第一条用于显卡的PCIe插槽上非官方地启用PCIe 5.0支持，尽管B650芯片组官方仅支持PCIe 4.0。

这种非官方支持受到希望具有未来兼容性或计划使用下一代PCIe 5.0 GPU的用户欢迎。然而，BIOS更新禁用了此功能，将第一条PCIe插槽限制在官方支持的PCIe 4.0速度。

技嘉在文章中没有明确说明更改的原因。有人推测可能是由于稳定性问题、与特定PCIe 5.0设备的兼容性问题，或者潜在的遵守AMD规范。也有可能在B650上维持PCIe 5.0支持可能在电源供应或信号完整性方面带来挑战。

虽然文章没有详细说明哪些特定的B650型号受到影响，但暗示是那些先前已知非官方提供PCIe 5.0的型号。更新了BIOS的用户将不再在第一条PCIe插槽上拥有PCIe 5.0功能。其影响主要在于那些期望在这些主板上使用PCIe 5.0设备的用户。

---

## 15. 基于激光雷达的新罕布什尔州石墙GIS地图

**原文标题**: Lidar-based GIS map of New Hampshire stone walls

**原文链接**: [https://nhgranit.maps.arcgis.com/apps/webappviewer/index.html?id=25930044fe2b4d8fb5cab3ec07565e83](https://nhgranit.maps.arcgis.com/apps/webappviewer/index.html?id=25930044fe2b4d8fb5cab3ec07565e83)

本文介绍了一个 ArcGIS Web 应用程序，该应用程序展示了基于激光雷达的 New Hampshire 州石墙 GIS 地图。该应用程序利用激光雷达数据（一种使用激光创建地球表面高精度 3D 表示的遥感技术）来识别和绘制石墙地图。

该应用程序允许用户探索全州石墙的分布、密度和潜在特征。这为 New Hampshire 州的历史土地利用实践和文化景观提供了宝贵的见解。通过使用可通过 ArcGIS 访问的 Web 应用程序，研究人员、历史学家、自然资源保护主义者和公众可以轻松获取数据。

主要收获是将激光雷达技术创新地应用于绘制和分析重要的文化特征。ArcGIS Web 应用程序作为一个可视化和交互此空间数据的平台，促进了对 New Hampshire 州历史悠久的石墙网络的更大理解和欣赏。该项目可能会促进对该州遗产的重要方面的进一步研究、保护工作和公众参与。

---

## 16. 完善有向距离函数的抗锯齿

**原文标题**: Perfecting anti-aliasing on signed distance functions

**原文链接**: [https://blog.pkh.me/p/44-perfecting-anti-aliasing-on-signed-distance-functions.html](https://blog.pkh.me/p/44-perfecting-anti-aliasing-on-signed-distance-functions.html)

本文探讨了有向距离场 (SDF) 的抗锯齿技术，强调实现良好效果并非简单地应用 `smoothstep` 函数就能达成，其中蕴含着更多技巧。

核心思想依赖于 SDF 梯度长度为 1 的属性，这使得形状内部和外部之间能够平滑过渡。文章首先使用 `linearstep` 函数进行抗锯齿，并由宽度参数 `w` 控制。`w` 的值至关重要：对于抗锯齿而言，它应对应于像素的大小。

文章讨论了确定像素大小的方法。在 2D 中，可以直接从分辨率计算得出。然而，在 3D 中或应用透视变换等变换时，这种方法会变得复杂。解决方案是使用数值导数与 `fwidth(d)`，后者估计了从像素角度看到的有向距离 (`d`) 的变化率，从而适当地调整抗锯齿宽度。另一种方法是 L2 范数 `length(vec2(dFdx(d), dFdy(d)))`，但计算成本更高。

文章随后比较了 `linearstep` 和 `smoothstep`，令人惊讶地得出结论：尽管存在不连续性，但 `smoothstep` 通常会产生视觉上更好的效果，尤其是在较大的模糊宽度下。

最后，文章提到了色彩空间的重要性，建议使用 OkLab 进行颜色混合，尤其是在模糊处理时，尽管线性混合足以满足基本的抗锯齿需求。文章最后提供了一些实用代码示例，将这些技术结合起来用于各种场景。

---

## 17. Token级别奖励的变革

**原文标题**: The Revolution of Token-Level Rewards

**原文链接**: [https://www.levroai.com/blog/revolution-of-token-rewards-08-01-2025](https://www.levroai.com/blog/revolution-of-token-rewards-08-01-2025)

Levro，一家致力于利用AI智能体简化国际贸易的初创公司，在训练LLM以应对复杂任务（如技术客户支持和结构化推理）时遇到了挑战。传统的强化学习（RL）方法被证明是不够的，因为难以向模型提供具体和细致的反馈。

文章强调了现有RL技术的局限性，例如GRPO，它为整个输出分配单一奖励，甚至惩罚部分正确的响应。这与过程监督形成对比，尽管过程监督旨在实现精细的反馈，但由于难以定义“步骤”、奖励模型评分不一致以及奖励破解，在实践中经常失败。

Levro开发了“Token级奖励”来解决这些问题。这种方法根据各种质量指标（例如语法、工具使用、相关性）为单个token分配详细的分数，并使用“裁判LLM”来识别输出中具有影响力的部分。然后，这些分数被分配给特定的token及其之前的token，从而创建“token热图”。针对每个指标独立计算优势（每个token对总分有多少帮助或损害），然后将它们相加，从而在训练期间为LLM提供精确的反馈。

这种有针对性的训练方法显著提高了训练速度（25%），增加了基准测试的评估奖励，减少了奖励破解，并提高了模型在修复错误的同时保持良好结构的能力。其核心优势是更高效的训练和更高质量的输出，尤其是在代码生成和智能体工作流等复杂任务中，而无需大量的计算资源。Token级奖励将过程监督转化为一种实用的解决方案，可以在更小、更专业的模型上使用。

---

## 18. 编程界的丰田卡罗拉

**原文标题**: The Toyota Corolla of programming

**原文链接**: [https://deprogrammaticaipsum.com/the-toyota-corolla-of-programming/](https://deprogrammaticaipsum.com/the-toyota-corolla-of-programming/)

本文探讨了 PHP 和 JavaScript 令人惊讶的相似之处和持久的影响。这两种脚本语言都诞生于 1995 年，尽管最初存在设计缺陷和持续的批评，但它们都成为了 Web 开发的基石。作者将 PHP 比作丰田卡罗拉：可靠、经济、普及，为互联网的很大一部分提供动力。

文章讨论了针对 PHP 的常见批评，承认其怪癖和安全漏洞，但认为它已经发展成为一种现代语言，具有 OOP 特性、函数式编程结构、类型检查、强大的包管理器和强大的单元测试支持。文章还强调了解决安全问题和使该语言现代化的努力。

作者承认过去参与过反 PHP 的情绪，但承认它的进步以及由 PHP 基金会推动的蓬勃发展的社区。讨论的一个关键发展是 FrankenPHP，这是一种基于 Go 的新运行时，有望简化容器化并改进执行模型。

尽管取得了这些进展，但文章预计 PHP 将继续面临批评，因为它的起源和“集市”开发风格。然而，作者最终捍卫了 PHP 的持久价值及其在实现经济实惠的 Web 托管和赋能庞大的开发者社区方面发挥的关键作用。文章最后强调了重新评估 PHP 当前状态并承认其对 Web 的重大贡献的重要性。

---

## 19. ScreenCoder：智能UI到代码生成系统

**原文标题**: ScreenCoder: An intelligent UI-to-code generation system

**原文链接**: [https://github.com/leigest519/ScreenCoder](https://github.com/leigest519/ScreenCoder)

ScreenCoder是一个智能的UI到代码生成系统，旨在将UI截图或设计模型转化为干净、可用于生产环境的HTML/CSS代码。它采用模块化的多代理架构，结合视觉理解、布局规划和自适应代码合成，以生成准确且可编辑的前端代码。该系统还支持开发者和设计师进行定制化修改。

文章提供了一个Hugging Face演示和演示视频，展示了其功能。定性比较突出了ScreenCoder在准确性、视觉对齐和语义保真度方面优于现有方法。

该项目的结构包括UI元素检测 (UIED)、HTML生成、图像替换和映射等模块。安装说明详细介绍了克隆存储库、创建虚拟环境、安装依赖项以及配置模型和API密钥（Doubao、Qwen、GPT或Gemini）的步骤。

使用工作流程包括几个步骤：使用占位符进行初始HTML生成、块检测、占位符检测、UI元素检测、映射对齐和占位符替换。还提供了一个简单的运行命令（`python main.py`）来生成最终的HTML代码。最后，文章感谢了WebPAI和Awesome-Multimodal-LLM-for-Code等相关项目，并感谢对UIED、DCGen和Design2Code做出贡献的人。

---

## 20. Drawafish.com事后剖析：哎呀

**原文标题**: Drawafish.com Postmortem: Whoops

**原文链接**: [https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html](https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html)

奥尔登·哈拉克对DrawAFish.com的事故分析报告详细描述了2025年8月3日发生的安全事件，该网站由于多个漏洞遭到破坏。事件持续约6小时，导致用户名被污蔑，恶俗的鱼被批准，而合法的鱼被删除。

根本原因包括：用于测试后被遗忘的旧版6位管理员密码（从过去的Neopets数据泄露事件中泄露），缺少身份验证的用户名更新API，以及未绑定到特定用户的JWT。 泄露的密码使恶意用户能够访问管理员权限并进行更改。

恢复过程包括使用审核日志手动撤销修改操作并修补漏洞。 哈拉克不得不修复他有缺陷的Firebase备份以开始恢复。 Hackernews用户@iceweaselfan44利用JWT漏洞授权为管理员并删除了冒犯性内容，这是一线希望。

哈拉克承认他“随心所欲地编码”，并将速度置于安全之上，忽略代码审查，并过度依赖Copilot而没有适当的监督。 他承认了自己的缺点，并认识到代码审查和透彻文档的重要性。 虽然@iceweaselfan44最初被禁止，但两人后来取得了联系，他帮助重构了代码以提高安全性。 哈拉克现在声称以每张100美元的价格出售贴纸。

---

## 21. 大型语言模型能识别字体吗？

**原文标题**: Do LLMs identify fonts?

**原文链接**: [https://maxhalford.github.io/blog/llm-font-identification/](https://maxhalford.github.io/blog/llm-font-identification/)

大型语言模型能否准确识别图像中的字体？一项针对全新字体的基准测试

---

## 22. 万事达卡否认应为成人游戏下架负责

**原文标题**: Mastercard deflects blame for NSFW games being taken down

**原文链接**: [https://www.pcgamer.com/games/mastercard-deflects-blame-for-nsfw-games-being-taken-down-but-valve-says-payment-processors-specifically-cited-a-mastercard-rule-about-damaging-the-brand/](https://www.pcgamer.com/games/mastercard-deflects-blame-for-nsfw-games-being-taken-down-but-valve-says-payment-processors-specifically-cited-a-mastercard-rule-about-damaging-the-brand/)

本文讨论了万事达卡对Steam和Itch.io移除NSFW游戏的回应。Valve和Itch.io将此举归因于信用卡公司的压力。万事达卡否认直接要求下架，声明其“允许所有合法购买”，仅要求商家对非法活动，特别是非法成人内容，进行管控。

文章突出了万事达卡的声明与Valve的经历之间的脱节。Valve表示，支付处理商援引万事达卡规则5.12.7（关于“非法或损害品牌交易”），以此作为拒绝发行合法NSFW游戏的理由。该规则允许万事达卡认为任何“明显具有冒犯性且缺乏严肃艺术价值”的材料是不可接受的。

文章还阐明了万事达卡的运营角色：他们不直接处理付款，而是为交易提供技术和网络。这意味着压力很可能施加给了支付处理商和收单银行，然后由他们将限制传达给Valve和Itch.io。Itch.io暂停了Stripe对18+内容的支付，Valve也被其支付处理商告知了这些限制，后者援引了万事达卡。尽管万事达卡否认直接参与，但Valve坚持认为万事达卡的规定是NSFW游戏被取消索引或移除的催化剂。

文章最后指出，公众压力可以影响这些决策，并指出游戏移除最初源于反色情活动家的公众活动。

---

## 23. 特斯拉隐瞒数据、撒谎并误导警方以逃避自动驾驶事故责任

**原文标题**: Tesla withheld data, lied, misdirected police to avoid blame in Autopilot crash

**原文链接**: [https://electrek.co/2025/08/04/tesla-withheld-data-lied-misdirected-police-plaintiffs-avoid-blame-autopilot-crash/](https://electrek.co/2025/08/04/tesla-withheld-data-lied-misdirected-police-plaintiffs-avoid-blame-autopilot-crash/)

这篇Electrek文章详细描述了特斯拉如何在2019年一起涉及致命Autopilot撞车的非正常死亡案件中，涉嫌隐瞒关键数据、撒谎、并误导当局和原告，而该公司在2025年被判负部分责任。在撞车发生后几分钟内，特斯拉Model S就将一份全面的“碰撞快照”上传到特斯拉的服务器，而该公司据称随后隐瞒了这份快照。

文章声称，特斯拉的律师为警方编写了一份有限的证据请求，省略了关键数据，如视频和Autopilot信息。后来，当警方试图直接从汽车的计算机中提取数据时，特斯拉据称上演了一场“合作”活动，其中一名技术人员声称数据已损坏。多年来，特斯拉一直否认碰撞快照的存在，直到面临无可辩驳的法医证据。

在法院命令进行的法医分析之后，工程师们得以恢复完整的数据集，该数据集显示Autopilot处于激活状态，尽管即将发生撞车，但没有发出警告，并且特斯拉知道该区域是Autosteer的限制区域。

原告辩称，特斯拉因允许在不适宜的条件下使用Autopilot以及未实施充分的驾驶员监控而存在疏忽。陪审团将33%的责任归咎于特斯拉。作者认为，特斯拉的粉丝应该对受害者家属表现出同情和谦逊，承认特斯拉应该对这起撞车事故承担一些责任。文章最后断言，监管机构应调查与销毁证据相关的刑事指控，并对特斯拉处以罚款。

---

## 24. 英国社会分层的遗传相关性 (2019) [pdf]

**原文标题**: Genetic correlates of social stratification in Great Britain (2019) [pdf]

**原文链接**: [https://research.vu.nl/ws/portalfiles/portal/127420931/Genetic_correlates_of_social_stratification_in_Great_Britain.pdf](https://research.vu.nl/ws/portalfiles/portal/127420931/Genetic_correlates_of_social_stratification_in_Great_Britain.pdf)

以下是我根据文章标题及该领域常见研究对其内容理解而作的“英国社会分层的遗传相关性”一文的摘要：

本研究调查了英国的遗传倾向与社会分层之间的关系。它旨在确定遗传变异是否与教育程度、职业地位和收入水平相关，即使在考虑了环境和社会因素之后。

研究人员可能使用了全基因组关联研究（GWAS）和来自大规模数据集的多基因评分（PGS），以预测个体对某些社会结果的倾向。然后，他们将这些PGS与社会经济地位的指标（例如，受教育年限、职业（例如，使用标准职业分类量表）和收入）相关联。

该研究可能发现，教育程度的PGS与更高的职业地位和收入呈正相关。这表明了对社会流动的遗传贡献，即具有较高教育遗传倾向的个人更有可能获得更高的社会经济成果。

文章可能讨论了这些发现对于理解基因和环境在塑造社会不平等中的复杂相互作用的意义。它可能通过强调PGS仅解释社会结果中一小部分差异，并且环境和社会因素仍然至关重要，来解决对遗传决定论的担忧。研究人员可能还探讨了遗传培育的可能性，即父母的基因影响孩子的环境，从而进一步塑造他们的社会轨迹。最后，该研究可能以呼吁进一步研究以了解使用遗传信息预测社会结果的伦理和社会影响而告终。

---

## 25. 你想解析PDF？

**原文标题**: So you want to parse a PDF?

**原文链接**: [https://eliot-jones.com/2025/8/pdf-parsing-xref](https://eliot-jones.com/2025/8/pdf-parsing-xref)

本文深入探讨了PDF文件解析的复杂性，对比了理想规范与真实文档中遇到的混乱现实。虽然PDF规范概述了一个清晰的过程，包括定位版本头、交叉引用表、对象偏移和尾部字典，但实际应用中往往存在显著偏差。

作者强调了解析PDF文件时遇到的常见问题：由于前导“垃圾”数据导致的错误的startxref指针、指向交叉引用表中间的指针、偏移“接近”但不完全正确，或者交叉引用表本身格式错误（例如，缺少换行符、额外的对象条目、垃圾数据）。文章指出，即使startxref指针正确，交叉引用表内的对象偏移也可能仍然不准确。修改后的文件可能在尾部具有不正确的/Prev指针，从而阻碍了交叉引用表链的解析。

一项对近4000个文件的调查显示，由于这些不符合规范的文件，失败率为0.5%。尽管与规范存在这些偏差，但大多数PDF查看器通过采用更宽松的解析方法来打开这些文件。作者强调，解析PDF远非易事，并列举了这些挑战只是广泛的PDF规范所带来的整体困难中的一小部分。本质上，本文告诫不要假设严格遵守PDF规范，并强调在PDF解析实现中需要强大的错误处理和灵活性。

---

## 26. 每个可视化工作流工具都只是放弃了的开发者用的Excel

**原文标题**: Every Visual Workflow Tool Is Just Excel for Developers Who Gave Up

**原文链接**: [https://medium.com/@mohamedalibenothmen1/every-visual-workflow-tool-is-just-excel-for-developers-who-gave-up-f7261090fbc8](https://medium.com/@mohamedalibenothmen1/every-visual-workflow-tool-is-just-excel-for-developers-who-gave-up-f7261090fbc8)

该文章认为，Zapier和Power Automate等可视化工作流工具本质上是“放弃治疗的开发者使用的Excel”，它们提供了一个简化的界面，掩盖了底层的复杂性和局限性。作者认为，这些工具看似更简单，实则会造成类似庞大Excel表格的依赖噩梦，最终导致开发者的能力下降。

作者批评开发者选择拖放界面而不是代码的力量和控制力，理由包括冒名顶替综合症、决策疲劳和速度的错觉。他们认为，代码允许版本控制、测试和精确的错误消息，而可视化工具则提供模糊的错误消息，并且缺乏自定义集成的能力。

一个关键点是经济效率低下：当开发者拥有使用Python或JavaScript等语言免费构建更优秀解决方案的技能时，他们却为这些工具支付高昂的费用。作者强调了这些平台固有的供应商锁定、速率限制、缺少集成、糟糕的错误处理和性能限制的危险。

文章总结说，依赖可视化工作流意味着认知上的懒惰和愿意用开发者身份换取便利。它敦促开发者认识到他们固有的能力，并选择代码的力量而不是可视化工作流工具的约束。

---

## 27. 我们如何构建《布鲁伊》的世界

**原文标题**: How we built Bluey’s world

**原文链接**: [https://www.itsnicethat.com/features/how-we-built-bluey-s-world-cartoon-background-scenery-art-director-catriona-drummond-animation-090725](https://www.itsnicethat.com/features/how-we-built-bluey-s-world-cartoon-background-scenery-art-director-catriona-drummond-animation-090725)

本文详细介绍了《蓝色小考拉》第一季的首席美术指导卡特里奥娜·德拉蒙德如何设计该剧迷人且具有视觉吸引力的场景，重点在于该剧背景的创作。德拉蒙德的任务是展现该剧背景地澳大利亚布里斯班的美丽。

该过程包括收集大量的参考资料，特别是昆士兰风格的房屋，并融入关键的想法。这些想法包括：受凯蒂·爱德华兹和黛布拉·胡德等当地艺术家启发的空间图形表达；类似于娃娃屋的比例，以增强该剧的可爱性和吸引力；以及捕捉布里斯班独特的色彩和光线，受到简·约根森等画家的影响。

一个关键要素是建立一种“形状语言”，使用圆形、三角形和正方形来潜意识地传达角色和个性，最终确定使用圆角矩形来代表世界，以呼应角色。

最后，德拉蒙德为剧组创建了一本“蓝色小考拉圣经”，概述了关键规则和指导方针，包括：避免过于字面的狗的参考；保持可爱、简化和粗犷的物体；使用直接的相机调度；简化和扁平化空间；采用“反向”两点透视以获得更宽的地面；以及使用色彩鲜艳、生动的布里斯班光线表现。目标是创造出在视觉上美味且具有吸引力的东西。

---

## 28. 在奇异材料界面发现新型量子物态

**原文标题**: New quantum state of matter found at interface of exotic materials

**原文链接**: [https://phys.org/news/2025-07-quantum-state-interface-exotic-materials.html](https://phys.org/news/2025-07-quantum-state-interface-exotic-materials.html)

罗格斯大学主导的研究人员在一项突破性发现中，于外尔半金属（一种导电材料）和自旋冰（一种绝缘磁性材料）的界面处，发现了一种新的量子物态——量子液晶。这项发表在《科学进展》上的研究表明，在极高磁场下，这两种奇异材料之间的相互作用会产生一种独特的“电子各向异性”现象。

这种各向异性表现为电导率的方向依赖性。该材料在360度圆周内的六个特定方向上表现出最低的电导率。有趣的是，增加磁场会导致电子突然朝两个相反的方向流动。这种行为与旋转对称性破缺相一致，表明出现了一种新型量子相。

该研究团队由Jak Chakhalian领导，成员包括Tsung-Chi Wu和Jedediah Pixley，他们在国家高磁场实验室使用了实验技术，得以在超低温和高磁场下研究这些材料。这一发现为控制和操纵材料特性提供了见解，有可能实现为极端环境（如太空）设计高度灵敏的量子传感器。

外尔半金属/自旋冰异质结构的创建是使用一种名为Q-DiP的特殊机器实现的。该研究强调了结合不同材料探索新的量子相和扩展我们对物质超出传统状态的理解的潜力。它还强调了实验物理学家和理论物理学家之间合作在推进科学知识方面的关键作用。

---

## 29. 1981年BASIC冒险游戏登陆新平台TRS-80 MC-10

**原文标题**: 1981 BASIC adventure game comes to a new platform, the TRS-80 MC-10

**原文链接**: [https://www.arctic81.com/arctic-adventure-mc10.html](https://www.arctic81.com/arctic-adventure-mc10.html)

2025年8月，哈利·麦克拉肯宣布吉姆·格里将他1981年的BASIC文本冒险游戏《北极冒险》移植到TRS-80 MC-10平台。该游戏最初于1981年在一本书中出版，但包含一个灾难性的错误，导致游戏无法进行，麦克拉肯也因此放弃了游戏开发。

四十年后，麦克拉肯重新发现了该游戏并进行了修复，增加了改进并使其可以在Web浏览器中运行。这次更新受到了意想不到的关注，促使人们有兴趣将其移植到其他平台。吉姆·格里的MC-10移植版是第一个这样的改编。

TRS-80 MC-10，一款于1983年发布的廉价电脑，被选为新的移植平台。它功能有限，但也具有彩色图形。尽管MC-10的寿命很短，但它在老式计算机爱好者中仍然拥有一定的追随者。

格里的移植版是一个实质性的重写，成功地使游戏在MC-10上运行，消除了最初的破坏性错误。做了一些小的改动，例如用更现代的术语替换了对“爱斯基摩人”的引用，并将英里换成了公里。该移植版本比麦克拉肯自己的更新网络版本更接近他对游戏的最初设想。浏览器版本包括当前浏览器会话的保存和加载功能。吉姆·格里创建的攻略也可用。麦克拉肯表示，希望会有更多针对其他模拟平台的版本推出。

---

## 30. 编写优秀的設計文檔

**原文标题**: Writing a good design document

**原文链接**: [https://grantslatton.com/how-to-design-document](https://grantslatton.com/how-to-design-document)

本文旨在指导如何编写高效的设计文档，将其构建为旨在说服读者（包括作者本人）设计方案最优的论证。作者强调清晰组织的重要性，将结构不良的文档比作“意大利面条式代码”。目标是在不引起意外的情况下引导读者，先发制人地解决潜在的异议，并确保直接的理解。

主要原则包括：

*   **清晰度和结构：** 组织文档，使每个要点都从前一个要点逻辑地流出，预测读者的疑问和顾虑。
*   **读者考量：** 模拟读者的初始知识，并引导他们理解设计的价值。
*   **简洁性：** 大力编辑，删除不必要的词语，尊重读者有限的注意力。
*   **实践：** 编写大量文档是提高的最佳途径。

本文还提供具体的技巧：

*   **短段落：** 每个段落应代表一个可以用一句话概括的单一想法。
*   **附录：** 将复杂的计算或模拟移至附录，确保它们不会中断主流程。

作者使用“编辑示例”来说明如何在不牺牲信息的情况下减少字数。本文强调，掌握设计文档的写作需要实践以及接受（并从中学习）反馈的意愿。

---

## 31. AI承诺提高效率，结果却让我们工作更辛苦。

**原文标题**: AI promised efficiency. Instead, it's making us work harder

**原文链接**: [https://afterburnout.co/p/ai-promised-to-make-us-more-efficient](https://afterburnout.co/p/ai-promised-to-make-us-more-efficient)

人工智能：效率提升的承诺与倦怠的悖论

本文指出，尽管人工智能承诺提高效率并释放时间，但实际上往往导致工作量、认知负荷增加，最终导致倦怠。它挑战了人工智能自动转化为更高生产力的观点，并引用研究表明，开发者在使用人工智能辅助时完成任务的时间*更长*，同时*认为*自己更快。作者强调了个人感觉更有效率，而团队和组织整体绩效却下降的悖论。

文章认为，核心问题在于人工智能将精神能量从执行转移到持续的质量控制、事实核查和提示工程，从而导致一种新的认知疲惫。文章将此与更广泛的生产力文化问题联系起来，在这种文化中，不断优化和采用新工具的压力反映了不健康的“更加努力”心态。

作者为减轻这些负面影响提出的建议包括：重新定义生产力，将认知能量的保存置于节省时间之上；根据个人经验而非炒作有选择性地采用人工智能工具；并承认人工智能的采用通常涉及暂时的生产力下降，需要进行重大的组织调整。核心是，我们应该专注于使用人工智能来创建可持续的工作流程，而不是仅仅在相同的时间内塞入更多的工作，这可能会导致倦怠。

---

## 32. 通义千问·图像

**原文标题**: Qwen Image

**原文链接**: [https://huggingface.co/Qwen/Qwen-Image](https://huggingface.co/Qwen/Qwen-Image)

Qwen-Image是千问系列中一种新型图像生成基础模型，擅长复杂的文本渲染和精确的图像编辑，尤其是在中文文本方面。 Qwen-Image于2025年8月4日发布，并在Hugging Face和ModelScope上发布了其技术报告和权重，在图像生成和编辑方面均具有强大的通用能力。

该模型可用于使用`diffusers`库从文本提示生成图像。 提供代码示例以便快速入门。

Qwen-Image的主要特点包括：

*   **高保真文本渲染：** 准确地保留不同语言的排版细节、布局连贯性和上下文和谐性。
*   **通用图像生成：** 支持从照片级逼真到抽象的各种艺术风格。
*   **高级图像编辑：** 支持风格迁移、对象操作、文本编辑和人体姿势操作。
*   **图像理解能力：** 支持对象检测、语义分割、深度估计、新视角合成和超分辨率。

Qwen-Image采用Apache 2.0许可，并鼓励用户引用他们的工作。 尽管已发布，但在撰写本文时，该模型尚未被任何推理提供商部署。

---

## 33. KDE Plasma 准备严厉打击 Wayland 下抢夺焦点的窗口行为

**原文标题**: KDE Plasma prepares crackdown on focus-stealing window behavior under Wayland

**原文链接**: [https://www.neowin.net/news/kde-plasma-prepares-crackdown-on-focus-stealing-window-behavior-under-wayland/](https://www.neowin.net/news/kde-plasma-prepares-crackdown-on-focus-stealing-window-behavior-under-wayland/)

KDE Plasma 正在准备在 Wayland 下使用 “XDG Activation” 协议来强制执行更严格的焦点窃取预防措施。该系统旨在防止不必要的窗口焦点更改。与存在缺陷的 X11 系统不同，Wayland 要求应用程序向合成器（此处为 KWin）提供有效的、一次性令牌才能获得焦点，从而确保焦点更改是由用户交互发起的。

目前，KWin 对不正确使用或忽略 XDG Activation 协议的应用程序一直比较宽容，经常会授予新窗口焦点。即将到来的更改将在窗口管理设置中引入一个“极端”设置，该设置将强制 KWin 仅在提供有效令牌时才授予焦点。

这种更严格的执行已经促使修复了多个 KDE 组件和相关库，包括 Dolphin、KRunner、Kickoff、LayerShell-Qt 和 Baloo。这些修复确保了应用程序在启动新实例或打开文件时，能正确地请求和使用激活令牌。这些更新还解决了与修饰键按下相关的问题，并允许特权客户端正确地请求令牌。目标是创建一个在 Wayland 下更可预测和安全的窗口管理体验，消除令人沮丧的焦点窃取行为。

---

## 34. 因PL-15射程情报失误，印度阵风被击落

**原文标题**: Indian Rafale Downed Due to Intel Failure on PL-15 Range

**原文链接**: [https://theaviationist.com/2025/08/03/indian-rafale-downed-reuters/](https://theaviationist.com/2025/08/03/indian-rafale-downed-reuters/)

本文详细描述了2025年5月7日发生的一起报告事件，据称巴基斯坦空军（PAF）的一架J-10C使用一枚从约200公里外发射的PL-15空对空导弹击落了一架印度空军（IAF）的阵风战斗机。 该文章基于路透社的报道，强调了信息优势、超视距（BVR）能力以及网络中心战在现代空战中的重要性。

主要结论是，印度空军在PL-15导弹有效射程方面的情报失误是阵风战机失利的关键因素。 印度飞行员误判了交战距离，认为他们处于导弹射程之外。 巴基斯坦空军利用“数据链17”网络融合来自空中、陆地和太空资产的数据，从而获得了全面的态势感知优势。

文章强调，这次事件不一定反映了阵风战机的能力，而是反映了巴基斯坦空军网络的有效性以及对情报漏洞的利用。 据报道，印度在交战后调整了战术并更新了装备。

文章还提到了未经证实的关于印度空军更多损失的报告，包括阵风、苏-30MKI和米格-29，以及中国可能以实时雷达和卫星数据的形式向巴基斯坦提供的支持。 尽管中国和巴基斯坦否认这些说法，但该事件突显了准确的情报、强大的网络以及在现代空战中不断适应的重要性。

---

## 35. 生活、工作、死亡与农民：家庭构成

**原文标题**: Life, Work, Death and the Peasant: Family Formation

**原文链接**: [https://acoup.blog/2025/08/01/collections-life-work-death-and-the-peasant-part-iiia-family-formation/](https://acoup.blog/2025/08/01/collections-life-work-death-and-the-peasant-part-iiia-family-formation/)

布雷特·德弗罗的文章《生活、工作、死亡与农民：家庭的形成》引发了一场关于前现代农民社会婚姻模式的讨论，强调了其作为日常生活基石的重要性。文章强调，虽然高死亡率在各种文化中普遍存在，但婚姻模式却差异显著。

德弗罗强调了关注农民阶级（底层90%）婚姻实践的重要性，并指出将精英阶层的婚姻行为概括到普通民众身上的弊端。为了简化起见，他以一夫一妻制作为中心。

文章根据首次结婚年龄（AAFM）确定了三种婚姻模式：“早婚”（女性在十几岁早期到后期结婚，平均年龄在16岁左右）、“中婚”（女性在十几岁中期到后期结婚，平均年龄在20岁左右）和“晚婚”。文章特别指出，这并不意味着每个人都在特定年龄单身或结婚，而是代表该社会所有人的平均年龄。作者用古希腊（早婚）和罗马（中婚）的例子来说明这些模式。在古希腊，男性结婚年龄往往在30岁左右。

德弗罗解释说，为了维持高出生率以抵消死亡率，需要控制婚内生育或推迟婚姻的开始。作者指出，早婚模式通常与女性在安排婚姻方面缺乏自主权有关，而晚婚社会可能会更加重视女性的同意。

---

## 36. 医生为何讨厌他们的电脑（2018）

**原文标题**: Why doctors hate their computers (2018)

**原文链接**: [https://www.newyorker.com/magazine/2018/11/12/why-doctors-hate-their-computers](https://www.newyorker.com/magazine/2018/11/12/why-doctors-hate-their-computers)

医生为何讨厌他们的电脑

在《医生为何讨厌他们的电脑》一文中，一位外科医生探讨了医院广泛采用像Epic这样的电子健康记录（EHR）系统所带来的挫败感和低效率。 尽管投入了高达16亿美元巨资升级到Epic系统，旨在简化医疗流程，但作者和许多同事发现该系统繁琐且不利于患者护理。

文章强调，医生现在花在电脑任务上的时间比陪伴患者的时间还多，导致工作时间更长，倦怠率更高。 作者描述了该软件的复杂性、冗余的数据录入要求以及“辅助人员的复仇”（行政需求掩盖了临床效率）如何加剧这一问题。 初级保健医生Sadoughi博士就体现了这种挣扎，他指出，EHR使得诸如开具乳房X光片或更新患者问题列表等任务耗时更多，帮助更少。

作者通过类比流体动力学研究人员及其软件的案例研究解释说，随着软件系统的发展，它们变得更加官僚化，用户友好性降低。 这导致沮丧和一种被技术控制而不是被技术赋能的感觉。 文章最后指出，虽然计算机化简化了许多行业的任务，但矛盾的是，它使医疗行业更加繁琐和压力重重，从而导致人们对EHR系统普遍不满。

---

## 37. Converge (YC S23) 资金充足的纽约初创公司 寻产品开发人员

**原文标题**: Converge (YC S23) well-capitalized New York startup seeks product developers

**原文链接**: [https://www.runconverge.com/careers](https://www.runconverge.com/careers)

Converge，一家资金充足的纽约初创公司，YC S23毕业生，正在寻找产品开发人员加入他们的团队，成为第7名员工。该公司强调其令人印象深刻的产品与市场契合度，并以仅有六人的精简团队实现了超过100万美元的ARR和200多家客户。

Converge强调了获得重大所有权和影响力的机会，这与典型的以功能为中心的角色形成对比。他们与Segment和Fivetran等主要参与者竞争，为开发人员提供了拥有公司内部整个产品的机会。客户参与度很高，每日使用率达33%，从而能够立即感受到已发布功能的影响。尽管处于早期阶段，该公司还拥有真正的规模，处理大量的客户互动和GMV，从而提供了真正的工程挑战。

Converge的价值观围绕着紧迫感、深刻理解、谦逊和简单。他们正在寻找优先考虑交付和实际客户价值，而非管理、无休止的审查或炒作的构建者。理想的候选人能够适应现场工作，并且不需要大量的指导。

创始团队由Jan-Henrik（CEO）、Jerome（COO）和Thomas（CTO）组成，他们都拥有强大的工程背景。他们强调其创业精神和紧密的关系，培养一种注重实践贡献和快速增长的文化。

---

## 38. 如何种植几乎任何东西

**原文标题**: How to grow almost anything

**原文链接**: [https://howtogrowalmostanything.notion.site/htgaa25](https://howtogrowalmostanything.notion.site/htgaa25)

好的，我无法访问外部网站或特定的Notion页面来直接总结您提到的题为“如何种植几乎任何东西”的文章。

但是，根据标题、Notion的用途以及常见的园艺建议，我可以提供该文章可能包含的摘要。它可能侧重于在利用Notion进行组织和跟踪的框架内，对植物护理和栽培采取一般方法。

以下是一个可能的摘要：

文章“如何种植几乎任何东西”很可能指导读者开发一种系统的园艺方法，利用Notion的组织能力。它强调理解基本的植物需求的重要性，包括阳光、水、土壤和养分，并针对不同的植物种类进行调整。

该文章可能提倡使用Notion来跟踪有关单个植物或植物组的基本信息。这可能涉及创建数据库来记录种子开始日期、移植时间表、浇水程序、施肥计划、病虫害防治方法和收获时间表。它可能还包括用于记录观察结果、解决问题和记录成功（和不成功）实验的部分。

这篇文章很可能会强调研究特定植物的需求，重点是使植物与您的气候和可用空间相匹配。它还可能推广改善土壤健康的方法，例如堆肥或使用覆盖作物。它还可以强调持续监测植物健康状况，以尽早发现和解决问题。总体的目标可能是通过使用Notion来计划、跟踪和分析他们的园艺努力，从而使读者能够培养一个成功的花园，从而提高他们种植“几乎任何东西”的机会。

---

## 39. Python如何从一种语言成长为一个社区

**原文标题**: How Python grew from a language to a community

**原文链接**: [https://thenewstack.io/how-python-grew-from-a-language-to-a-community/](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/)

这是The New Stack关于“大规模软件开发”的newsletter注册表单。它重点介绍了Python从一种语言到社群的成长。

表单首先提示用户通过提供电子邮件地址来订阅，并附带一条关于之前取消订阅用户的重新订阅的说明。它向用户保证，他们的信息不会被出售或与无关的第三方共享，并链接到使用条款和隐私政策。

成功订阅后，用户会被要求提供个人和职业详细信息，包括：

* 名字、姓氏、公司名称、国家/地区和邮政编码。
* 职位级别（C级、副总裁/总监等）和职位角色（开发人员、系统管理员、架构师等）。
* 公司规模（个体经营、2-10人、11-50人等）。
* 组织类型（最终用户、供应商、云提供商等）。
* 主要行业（广告、航空航天、金融、医疗保健等）。
* 可选的LinkedIn个人资料URL。

最后，该表单欢迎新订阅者，告知他们newsletter的发送时间，并鼓励他们调整偏好、加入其他小组以及在社交媒体（尤其是LinkedIn）上关注The New Stack。它还建议浏览网站上的精选故事。

---

## 40. 现代Node.js模式

**原文标题**: Modern Node.js Patterns

**原文链接**: [https://kashw1n.com/blog/nodejs-2025/](https://kashw1n.com/blog/nodejs-2025/)

本文重点介绍了Node.js向现代、基于标准的开发环境的重大演变。它对比了旧的实践和现代模式，强调了改进的开发者体验、减少的依赖性以及增强的性能和安全性。

主要改进包括采用带有`node:`前缀的ES模块（ESM）用于内置模块，从而促进了更好的工具和清晰度。顶层`await`简化了初始化，消除了对包装函数的需要。

Node.js现在包含了内置的Web API，如Fetch和AbortController，减少了对外部库的依赖。原生测试运行器消除了对第三方测试框架的需求。

本文还讨论了高级异步模式，包括使用`async/await`进行高效的错误处理，以及使用AsyncIterators进行事件驱动编程。流处理已通过Web标准集成和用于可靠错误处理的`pipeline`函数得到增强。

Worker线程为CPU密集型任务实现了真正的并行性，而内置的watch模式和环境文件支持简化了开发流程。最后，本文还介绍了增强的安全功能，如权限模型和内置的性能监控，以及通过单个可执行应用程序更轻松地进行应用程序分发。总而言之，现代Node.js拥抱Web标准，提供更好的工具，并培养更高效、更安全的开发工作流程。

---

## 41. 美国应该对人工智能抱持最坏的打算

**原文标题**: America Should Assume the Worst About AI

**原文链接**: [https://www.foreignaffairs.com/united-states/artificial-intelligence-geopolitics-worst-about-ai](https://www.foreignaffairs.com/united-states/artificial-intelligence-geopolitics-worst-about-ai)

在《美国应以最坏打算看待人工智能》一文中，马坦·乔雷夫和乔尔·普雷德认为，人工智能的快速发展，尤其是通用人工智能（AGI）的潜力，构成了重大且不可预测的国家安全挑战，华盛顿必须积极应对。他们认为，决策者需要为人工智能驱动的颠覆性事件做好准备，例如美国或中国公司声称在AGI方面取得突破，或出现人工智能支持的网络攻击，而不是像过去的地缘政治转变那样措手不及。

作者强调，美国需要加强对全球人工智能生态系统的理解，促进公私合作以应对人工智能的挑战，并制定与盟友分享敏感信息的政策。他们强调了人工智能支持的网络攻击的潜力，这些攻击难以归因，并可能由自主人工智能代理执行，因此需要加强网络防御和国际协调。

乔雷夫和普雷德提出了多管齐下的方法：制定“不后悔”行动，创建适应性强的“破窗”应急预案，投资于各种情况下的关键能力，并优先考虑战略失败的早期指标。他们警告不要将AGI视为“普通技术”或“正常情况”，主张政府部门的广泛参与，超出传统的国家安全机构。他们还强调了考虑AGI可能如何重塑国际格局和全球力量动态的重要性，主张与多极世界中的盟友和伙伴尽早进行规划。文章总结说，未能为AGI的变革性影响做好规划将使任何国家安全战略都变得无关紧要。

---

## 42. 逃离《华盛顿邮报》

**原文标题**: The Exodus from the Washington Post

**原文链接**: [https://www.cjr.org/the_media_today/exodus-washington-post-wapo-storied-paper-dying-jeff-bezos-donald-trump.php](https://www.cjr.org/the_media_today/exodus-washington-post-wapo-storied-paper-dying-jeff-bezos-donald-trump.php)

在CEO威尔·刘易斯和所有者杰夫·贝索斯领导下，由于组织变革和战略不确定性，《华盛顿邮报》正经历着重大的人才流失。多位知名记者、专栏作家和编辑已经离职，其原因包括收购、新的工作机会以及对组织发展方向的不同意见。

贝索斯的影响力体现在评论版块向“个人自由和自由市场”的重新定位上，一些人认为此举是为了迎合中间偏右的精英阶层，并可能受到特朗普的影响。 这种转变导致了包括大卫·希普利、露丝·马库斯和尤金·罗宾逊在内的重要评论人物的离职。

刘易斯的“重塑之旅”涉及吸引更广泛的受众，这可能会削弱《华盛顿邮报》对精英读者的关注。该报宏伟的目标，例如达到2亿订阅者，受到了怀疑，商业风险投资的“第三新闻编辑室”和人工智能辅助的观点平台等举措也同样如此。

虽然《华盛顿邮报》面临着媒体行业常见的挑战，例如吸引订阅者和驾驭内容创作者的格局，但离职也受到个人职业抱负和对独立性的渴望的驱动。 文章承认《华盛顿邮报》仍然拥有人才，同时也质疑其长期战略和方向。它不是在“消亡”，而是在“重塑”，而这种重塑是否会成功还有待观察。

---

## 43. 类型化语言更适合氛围编码。

**原文标题**: Typed languages are better suited for vibecoding

**原文链接**: [https://solmaz.io/typed-languages-are-better-suited-for-vibecoding](https://solmaz.io/typed-languages-are-better-suited-for-vibecoding)

作者认为，由于 Claude Code 等人工智能工具的进步，TypeScript、Rust 和 Go 等类型化语言正变得更适合快速原型开发（他们称之为“氛围编码”）。他们过去通常使用 Python 来实现这一目的，但现在发现，当类型化语言与人工智能结合使用时，可以在规模上提供更快、更安全的开发。

Claude Code 在类型化语言中自动检查和强制执行编译时安全性的能力，使得作者能够更有信心地对代码库进行重大更改（例如，3-5k 行差异），并保持代码的稳定性，这在 Python 中由于其动态类型特性而更难实现。作者特别强调了重构前端 TypeScript 代码的例子，其中 AI 辅助的类型化语言开发超越了他们在使用 Python 时所体验到的速度和安全性。

虽然承认 LLM 存在抽象泄露问题，但作者认为，人工智能工具现在有效地解决了 Python 在快速原型开发方面的优势，同时缓解了其缺点，例如较低的安全保证、速度慢和模糊性。因此，作者预测公司在生产部署中采用 Python 的比例将会下降。虽然有些人可能认为这种趋势在人工智能出现之前就存在，但作者认为这些工具放大了这种影响。

---

## 44. 我如何配置 BorgBackup 和 borgmatic (2023)

**原文标题**: How I configure BorgBackup and borgmatic (2023)

**原文链接**: [https://www.justus.pw/garden/borgbackup.html](https://www.justus.pw/garden/borgbackup.html)

本文详细介绍了作者在 macOS 上 BorgBackup 和 borgmatic 的配置，重点介绍了挑战和解决方案。由于 macOS 日志记录不可靠，作者建议使用辅助脚本（`borgmatic_timestamp.sh`）将标准输出和错误重定向到带有时间戳的日志文件。该脚本使用 `moreutils` 中的 `ts` 命令包装 borgmatic 命令，并处理标准输出和错误流。

文章随后解释了如何创建和激活 LaunchAgent（`.plist` 文件）来按小时调度 borgmatic 备份。它指出 `launchctl` 在进程隔离方面相比 `systemd` 的局限性。

作者提供了一个 fish shell 快捷方式，用于使用 `fzf` 恢复单个文件，以模拟 Time Machine 的日期选择 UI。文章还介绍了使用 `borgmatic key export --paper` 进行恢复的关键导出。

文章接着深入探讨了验证和测试备份。它解释了如何使用 `borgmatic export-tar` 和 `gtar` 将备份的数据与文件系统进行比较，以及用于测试备份完整性的抽样方法，包括 `find`/`mdfind`、`sort`、`awk` 和 `mapfile` 命令。文章提供了示例脚本和命令，用于选择随机文件并创建用于比较的 tar 存档。

最后，作者提倡同时使用 Time Machine（用于快速、本地备份）和 BorgBackup（用于通过 BorgBase 进行一致的、本地/异地备份），以遵守 3-2-1 备份规则。

---

## 45. 美国青年工人日益增长的绝望感

**原文标题**: Rising young worker despair in the United States

**原文链接**: [https://www.nber.org/papers/w34071](https://www.nber.org/papers/w34071)

David G. Blanchflower和Alex Bryson的这篇工作论文调查了1990年代初到2023年间美国精神绝望与年龄之间变化的关系。历史上，精神绝望呈现驼峰状模式，在中年时期达到顶峰。然而，该研究表明，这种模式已转变为随年龄单调递减，表明年轻人中的绝望感显著增加。

该研究强调，这种转变主要由年轻*工人*中日益增长的绝望感驱动。虽然传统的驼峰状模式仍然存在于无法工作和失业者中，并且对于家庭主妇、学生和退休人员观察到的是一种平坦的关系，但年轻工人中增加的绝望感是年龄-绝望曲线整体变化的关键驱动因素。

作者使用了来自各种来源的数据，包括行为风险因素监测系统(BRFSS)、国家药物使用与健康调查(NSDUH)以及皮尤研究中心、经济咨商局和约翰·霍普金斯大学的调查，以支持他们的发现。这些数据集提供了广泛的证据，表明随着时间的推移，年轻工人中的精神绝望感有所增加，从而导致工作人群中年龄与精神绝望感之间呈现更为明显的向下倾斜关系。

---

## 46. HTMX 很难，所以让我们做对。

**原文标题**: HTMX is hard, so let's get it right

**原文链接**: [https://github.com/BookOfCooks/blog/blob/master/htmx-is-hard-so-lets-get-it-right.md](https://github.com/BookOfCooks/blog/blob/master/htmx-is-hard-so-lets-get-it-right.md)

本文题为《HTMX很难，让我们做对》，很可能是一篇博客文章，重点讨论开发者在学习和实施HTMX时面临的挑战。元数据表明这是一篇公开的文章，发布在与“BookOfCooks”相关的平台上。

鉴于标题，这篇文章可能讨论了有效使用HTMX时常见的陷阱、误解和复杂性。它可能提供实用的建议、最佳实践，甚至可能提供开发者遇到的常见问题的解决方案。“Fork 0”和“Star 34”表明该文章托管在一个类似于GitHub的平台上，用户可以在该平台上Fork和Star仓库/内容。这暗示社区认为该文章有帮助或有价值。“通知”部分表明用户可以接收与该文章相关的更新或通知的功能，可能需要登录。本质上，这篇文章旨在通过解决HTMX被认为的困难来改善开发人员的HTMX学习体验。

---

## 47. 人类语言可能存在一个普遍的传输速率 (2019)

**原文标题**: Human speech may have a universal transmission rate (2019)

**原文链接**: [https://www.science.org/content/article/human-speech-may-have-universal-transmission-rate-39-bits-second](https://www.science.org/content/article/human-speech-may-have-universal-transmission-rate-39-bits-second)

无法访问文章链接。

---

## 48. 用 TypeScript 类型编写的 TypeScript 类型解析器

**原文标题**: A parser for TypeScript types, written in TypeScript types

**原文链接**: [https://github.com/easrng/tsints](https://github.com/easrng/tsints)

`tsints` 是一个 TypeScript 库，它使用 TypeScript 类型本身来解析 TypeScript 类型，这意味着它避免了任何 JavaScript 代码。该库旨在生成已解析类型的抽象语法树 (AST) 表示，类似于 `@babel/parser` 的输出。

使用方法包括从库中导入 `Parse` 类型，并将其应用于表示 TypeScript 类型的字符串。结果是一个表示 AST 的复杂类型。例如，解析类型 `"{some:[ts, 'type']}"` 会输出一个描述 `TSTypeLiteral` 的类型，该类型具有一个名为 "some" 的属性签名，其类型注释是一个包含对 `ts` 的类型引用和字符串字面量 `'type'` 的元组。

作者开玩笑地质疑使用该库的实用性，指出由于类型评估的复杂性，它可能会增加编译时间。该项目可能旨在演示 TypeScript 类型系统的功能，尽管潜在用例可能会受到性能考虑的限制。语气轻松幽默，幽默的推荐证明了这一点。

---

## 49. ThinkBook Plus Gen 6 – 联想的可卷轴笔记本电脑

**原文标题**: ThinkBook Plus Gen 6 – Lenovo’s rollable laptop

**原文链接**: [https://www.theverge.com/reviews/717491/lenovo-thinkbook-plus-gen-6-rollable-laptop-review](https://www.theverge.com/reviews/717491/lenovo-thinkbook-plus-gen-6-rollable-laptop-review)

安东尼奥·G·迪·贝内德托评测联想ThinkBook Plus Gen 6，这是一款售价3300美元的笔记本电脑，其可卷轴屏幕可从14英寸扩展到16.7英寸。他称赞这款设备，称其为他用过的最酷、最具未来感的笔记本电脑之一，并强调了扩展屏幕在多任务处理和改善人体工程学方面的实用性，尤其是在进行视线水平视频通话时。OLED显示屏提供鲜艳的色彩和清晰的细节。

然而，评测人员指出了一些缺点。这款笔记本电脑对于其尺寸来说过于笨重（3.72磅），铰链倾斜角度和端口选择有限。非触摸屏表现出晃动、吱吱声和可见的波纹。扬声器对于这个价格来说表现平庸，联想的Workspace应用程序也存在漏洞。

尽管价格高昂且存在一些怪癖，迪·贝内德托仍然欣赏ThinkBook Plus的出色键盘和触控板、强大的性能和良好的电池续航能力。他还发现“你做错了”的警报令人怀旧。他承认可以用同样的价格购买其他优秀的笔记本电脑，但没有一款提供独特的扩展显示屏。他对可卷轴屏幕的寿命和维修成本表示担忧，但最终希望这种创新能够继续下去，并在未来变得更容易获得。他总结说，联想值得赞扬，因为它将如此独特的概念推向市场。

---

## 50. 阅读你的代码

**原文标题**: Read your code

**原文链接**: [https://etsd.tech/posts/rtfc/](https://etsd.tech/posts/rtfc/)

即使拥有 Claude Code 和 Windsurf 等高级工具，本文仍然强调阅读和理解 AI 生成代码的关键重要性。 虽然“感觉式编程”（与 AI 进行基于对话的编程）提供了速度和效率，但忽略代码审查会带来重大风险：

*   **架构弱化：** 未经审查的代码可能会引入不一致性并偏离既定模式，导致整体架构崩溃。
*   **实现知识丧失：** 过度依赖 AI 而不理解底层代码会削弱开发人员的领域专业知识，并阻碍编码之外的创造性问题解决。
*   **安全漏洞：** AI 可能会忽略诸如访问控制之类的关键安全考虑因素，从而可能引入可能导致漏洞的安全漏洞。

本文提出了两种负责任的感觉式编程方法：

1.  **采用自动接受模式的快速原型设计：** 适用于外围功能或探索新技术，允许 AI 更独立地运行，然后再进行全面审查。
2.  **用于核心功能的同步编码：** 涉及对 AI 建议的密切监督和迭代接受，从而实现持续的修正并确保架构一致性。

提供了一个“感觉式编程检查清单”来指导代码审查，涵盖架构、安全性、测试、文档、错误处理和性能。 核心信息是，AI 编码助手是增强专业知识的工具，而不是取代专业知识的工具。 保持对代码库的掌握对于长期创新和防止架构衰退至关重要。 团队不应基于 AI 提供足够的质量保证的假设而取消代码审查。

---

## 51. 小鼠皮肤到大脑的专用冷感通路

**原文标题**: A dedicated skin-to-brain circuit for cool sensation in mice

**原文链接**: [https://www.sciencedaily.com/releases/2025/07/250730030354.htm](https://www.sciencedaily.com/releases/2025/07/250730030354.htm)

密歇根大学研究发现小鼠皮肤至大脑的专用冷感神经回路。这是首个完整绘制的温度感应通路，表明冷感温度拥有独立于热感的独特回路。

该通路始于皮肤中探测冷温（15-25°C）的分子传感器。这些传感器激活初级感觉神经元，将信号传递到脊髓。令人惊讶的是，信号在脊髓中被专门的中间神经元放大，然后发送到连接大脑的投射神经元。研究人员发现，禁用这种“放大器”会使冷感信号无法被检测到。

虽然该研究是在小鼠身上进行的，但基因测序表明人类也拥有相同的回路。这一发现具有潜在的医学意义，尤其是在理解和治疗与寒冷相关的疼痛方面，例如化疗患者所经历的疼痛。虽然新绘制的回路并不能调节这种类型的疼痛，但了解其正常功能可以帮助研究人员确定疾病或损伤中出现的问题，并开发有针对性的疗法。未来的研究将侧重于识别与急性寒冷疼痛相关的通路，以及大脑如何处理各种皮肤信号并将它们与情绪联系起来。

---

## 52. C++：“硬件模型”与“编译器模型”(2018)

**原文标题**: C++: "model of the hardware" vs. "model of the compiler" (2018)

**原文链接**: [http://ithare.com/c-model-of-the-hardware-vs-model-of-the-compiler/](http://ithare.com/c-model-of-the-hardware-vs-model-of-the-compiler/)

“无Bug”的黑兔批评了对Bjarne Stroustrup的C++定义的提议修正案([P1063R0])。Stroustrup指出C++提供了一个“硬件的直接且高效的模型，并结合了定义轻量级和高效抽象的工具。” [P1063R0]建议将“硬件的模型”改为“平台的模型”，认为模板映射的是*编译器*的代码生成工具，而不是硬件。

黑兔强烈反对，认为这会将重点从“硬件的模型”转移到“编译器的模型”，他认为这是一个根本性的错误。他认为编程语言的目的是将人类表达的程序翻译成硬件可以理解的指令。唯一的接口应该存在于人类和语言之间，以及语言和硬件之间。编译器内部结构是实现细节，不应在定义语言时暴露或考虑。

他认为，关注编译器的模型可能会使与现实世界需求无关的任意设计选择合理化。黑兔认为，模板的价值不在于它们映射编译器工具，而在于它们通过允许泛型算法简化了人类的编程。

黑兔担心，使用“编译器的模型”作为理由会打开过度指定语言并将内部实现细节暴露给程序员的大门，他认为这对C++来说是一条危险的道路。他最后强调了基于编译器实现细节来合理化功能的风险，这可能会损害该语言的整体设计。

---

## 53. 欢迎来到url.town，人口465。

**原文标题**: Welcome to url.town, population 465

**原文链接**: [https://url.town/](https://url.town/)

url.town 自称是一个有趣的在线资源目录，并自豪地宣称拥有 465 个资源。该网站将资源分类为广泛的主题，从实用到异想天开。

最新的添加内容突出显示了一项名为“pieterpostsend”的服务，该服务无需物理接触即可传递真实的纸质信件，建议在“家庭 › 活动”下查找。

该目录涵盖的主题包括：

*   **艺术与设计：** 从抽象艺术到网络漫画。
*   **电脑：** 从博客引擎到网络浏览器。
*   **家庭：** 活动和育儿。
*   **食物：** 从农场到餐桌到纯素食谱。
*   **游戏：** 从纸牌游戏到文字游戏。
*   **健康：** ADHD、自闭症、精神健康。
*   **爱好：** 从民俗到纱线工艺。
*   **包容性：** 可访问性和代词。
*   **互联网：** 从博客到网站联盟。
*   **语言：** 从美国手语到日语。
*   **LGBTQ+：** 从骄傲支持到跨性别资源。
*   **数学与科学：** 数学。
*   **音乐：** 音乐博客和在线音乐项目。
*   **自然：** 从鸟类到兔子和野兔。
*   **新闻：** 从游戏新闻到世界新闻。
*   **组织：** 慈善机构
*   **组织：** 促进、存储、工具
*   **人物：** 个人网站
*   **摄影：** 应用和照片博客。
*   **播客：** 从艺术到真实犯罪。
*   **阅读与文学：** 从博客到杂志。
*   **购物：** 从包袋和行李到贴纸。
*   **社交：** Mastodon
*   **运动：** 公路自行车
*   **视频：** 从工匠视频到 YouTube 前端。

总而言之，url.town 似乎是一个精选的网页目录，旨在将用户与各种不同的利基在线资源联系起来。

---

## 54. 食用超加工食品可能使减肥变得更困难。

**原文标题**: Eating ultra-processed foods could make it harder to lose weight

**原文链接**: [https://www.nature.com/articles/d41586-025-02451-8](https://www.nature.com/articles/d41586-025-02451-8)

自然杂志文章探讨了一项发表在《自然医学》上的研究，该研究表明，食用超加工食品（UPF）可能会阻碍减肥效果，即使遵循推荐的膳食指南。该研究比较了基于最少加工食品（MPF）的8周饮食和基于UPF的8周饮食的效果，两者都符合英国国家膳食指南。

研究人员发现，与UPF饮食相比，参加MPF饮食的参与者体重明显减轻更多（1.84公斤 vs. 0.88公斤），并且身体成分发生了积极变化，例如脂肪减少。在MPF阶段，对食物的渴望也减少了。

这篇文章强调，尽管超加工食品在英国、欧洲和美国等国家消费量很高，但国家膳食建议可能缺乏对超加工食品的关注。文章还强调了社会经济影响，表明超加工食品的负担能力和可及性不成比例地影响着低收入人群，即使他们有意健康饮食，也可能导致饮食失败。该研究呼吁人们更加了解超加工食品对饮食和健康的影响，并在膳食指南中加以考虑。

---

## 55. 阿纳托利·布戈尔斯基，头部遭质子束贯穿的幸存苏联科学家

**原文标题**: Anatoli Bugorski, Soviet scientist proton beam passing through his head survivor

**原文链接**: [https://en.wikipedia.org/wiki/Anatoli_Bugorski](https://en.wikipedia.org/wiki/Anatoli_Bugorski)

阿纳托利·布戈尔斯基，一位1942年出生的俄罗斯粒子物理学家，因在1978年的一次辐射事故中幸存而闻名。他在普罗特维诺高能物理研究所工作时，不慎将头部伸入U-70同步加速器发出的76GeV质子束路径中。质子束穿过他的头部，估计剂量为2000至3000希沃特。

尽管受到极高的辐射暴露，布戈尔斯基仍然幸存，这违背了医生的预期。最初，他左侧脸部肿胀，皮肤脱落，显露出质子束的路径。虽然他的智力没有受到重大损害，但他感到精神疲劳加剧。他左耳失聪，左侧脸部瘫痪，但这种瘫痪阻止了该侧的衰老。他还偶尔会癫痫发作。

布戈尔斯基继续担任物理学家，甚至成为同一加速器的实验协调员。由于苏联的保密政策，他在十多年里对事故保持沉默。他定期去莫斯科辐射诊所就诊。他表示有兴趣接受西方研究人员的研究，但缺乏旅行的经济手段。他与维拉·尼古拉耶芙娜结婚，育有一子彼得。

---

## 56. 角色向量：监控和控制语言模型中的性格特征

**原文标题**: Persona vectors: Monitoring and controlling character traits in language models

**原文链接**: [https://www.anthropic.com/research/persona-vectors](https://www.anthropic.com/research/persona-vectors)

本文介绍了一种名为“人格向量”的新技术，用于理解和控制语言模型（LLM）中的性格特征。Anthropic的研究人员发现了与特定人格特征（如“邪恶”、“奉承”和“幻觉”）相对应的神经网络活动模式。这些“人格向量”允许：

*   **监控：** 跟踪LLM在对话或训练期间的人格转变，有助于检测向不良特征的漂移。
*   **缓解：** 在训练期间进行干预，以防止模型获得不需要的性格。这种反直觉的方法包括通过引导模型走向不良人格来“免疫”模型，使其更能抵抗有害的训练数据。
*   **识别：** 通过分析训练数据如何激活人格向量，标记可能诱发不良特征的问题训练数据。这允许管理数据集以避免负面人格发展。

该方法是自动化的，只需要定义目标特征。验证涉及通过人为注入人格向量来“引导”模型，证明了向量与表达的特征之间的因果关系。对开源模型（Qwen和Llama）的实验表明了这些应用的有效性。文章总结说，人格向量提供了一种有前景的方法，通过深入了解模型如何获得和表达不同的行为特征，从而确保LLM与人类价值观保持一致。

---

## 57. 高效生成一个范围内的数字 (2018)

**原文标题**: Efficiently Generating a Number in a Range (2018)

**原文链接**: [https://www.pcg-random.org/posts/bounded-rands.html](https://www.pcg-random.org/posts/bounded-rands.html)

生成特定范围内随机数的性能开销

本文探讨了生成特定范围内随机数的性能开销，这是随机算法中常见的任务，它常常掩盖了底层伪随机数生成器 (PRNG) 本身的性能。文章强调了一个虚构的场景，其中由于范围生成效率低下，一个优化程度较低但高效实现的 PRNG 胜过了一个更快的 PRNG。

本文回顾了在 [0..k) 范围内生成随机数的各种方法，重点关注 C++ 实现。这些方法包括：

*   **C++ 内置:** 使用 `std::uniform_int_distribution`，通常过度设计，并非最有效率。
*   **经典取模:** 简单但速度慢且有偏差，原因在于除法运算和余数的不均匀分布。
*   **FP 乘法:** 将 PRNG 输出转换为 [0..1) 范围内的浮点数并缩放，有偏差且在 64 位系统上的移植性较差。
*   **整数乘法:** 使用定点算术，速度更快但有偏差。
*   **除法与拒绝:** 无偏差，但由于除法运算和拒绝循环而速度较慢。
*   **消除偏差的取模（两次）：** OpenBSD 的方法，通过两次取模运算消除偏差，比经典方法慢。
*   **消除偏差的取模（一次）：** Java 的方法，使用一次取模运算，偶尔执行拒绝。
*   **消除偏差的整数乘法:** Lemire 的方法，消除整数乘法中的偏差。
*   **位掩码与拒绝:** Apple 的方法，使用掩码来获得范围内的数字，如果结果太大则拒绝。

然后，本文介绍了一个“大型洗牌基准测试”，并测试了不同的方法，包括 32 位和 64 位实现。关键结论是，用于在范围内生成数字的方法会显著影响性能，即使较慢的 PRNG，如果范围生成得到优化，也可以带来更快的整体性能。文章强调了基准测试对于确定特定用例的最佳方法的重要性。

---

## 58. 如果你是远程办公，那就随意漫谈吧。

**原文标题**: If you're remote, ramble

**原文链接**: [https://stephango.com/ramblings](https://stephango.com/ramblings)

本文倡导在远程团队的聊天应用中创建个人“随想”频道，以促进社交凝聚力和想法产生。这些频道专为2-10人的团队设计，充当个人微型博客或日志，团队成员可以在其中分享想法、观念和更新，而不会干扰群组频道。

建议的格式是，每个团队成员都拥有一个以自己名字命名的频道，只有他们才能发起新帖子。其他人可以在主题讨论中回复。频道应分组放在专门的“随想”部分，默认静音，且不期望被阅读。

作者分享了他们在Obsidian的经验，在那里，“随想”已经成为在没有定期会议的情况下，水吧闲聊的一种成功替代方案。它们促进深度专注时间，同时保持连接。

好处包括浮现创造性的想法、原型和解决方案，以及在面对面聚会之间保持人际联系。这些频道宽松、非结构化的性质允许自由流动的思想和意想不到的见解。最终，“随想”提供了一种轻量且有效的方式来改善远程团队中的沟通和协作。

---

## 59. 昔日SGI：关于Silicon Graphics 4D系列的回忆与笔记 (1996)

**原文标题**: This Old SGI: notes and memoirs on the Silicon Graphics 4D series (1996)

**原文链接**: [https://archive.irixnet.org/thisoldsgi/](https://archive.irixnet.org/thisoldsgi/)

《老SGI》是关于Silicon Graphics 4D系列计算机（特别是Professional、Personal和Power IRIS型号）的指南和笔记合集。由A. J. Corda撰写并于1997年最后更新，该文档作为SGI官方常见问题解答的非官方补充，旨在帮助希望恢复或摆弄这些旧系统的硬件黑客和实验者。

该文档涵盖了广泛的主题，包括：

*   不同4D系列型号的**配置和性能**。
*   **图形配置**、立体声连接和显示器兼容性。
*   **硬件调试**技巧，包括LED测试代码和PROM监视器命令。
*   **解决常见问题**，例如电源问题、时钟和内存错误。
*   **安装程序**，包括CD-ROM启动、操作系统安装和硬盘格式化。
*   **串口引脚定义**和使用Sun-3鼠标的修改。
*   **在密码未知的情况下访问root**的信息。
*   **在小磁盘上构建可启动的IRIX文件系统**。

作者强调在使用潜在危险的硬件时，常识和谨慎的重要性。他还提供了一份供应商列表，用于采购SGI系统和零件，并按个人经验和网络声誉进行分类。

---

## 60. 超过一万家酒店集体起诉Booking.com

**原文标题**: Over 10k hotels join mass claim against Booking.com

**原文链接**: [https://nltimes.nl/2025/08/04/10000-hotels-join-mass-claim-bookingcom](https://nltimes.nl/2025/08/04/10000-hotels-join-mass-claim-bookingcom)

超过1万家欧洲酒店加入了一项针对Booking.com的集体诉讼，寻求赔偿据称因该平台过去阻止酒店在其他地方提供更低价格的行为而造成的损失。该诉讼由欧洲酒店餐饮协会Hotrec发起，声称这些“价格一致性条款”违反了欧洲法规，并导致了对酒店不公平的条款和过高的成本。

与此同时，在荷兰，消费者协会Consumentenbond正在代表受Booking.com政策影响，可能遭受价格虚高的消费者准备一项集体索赔。

Booking.com否认了这些指控，称其基于对先前裁决的错误解读，并且他们的行为并未人为抬高价格。他们辩称，根据欧盟法律，这些限制本质上不具有反竞争性。尽管如此，该公司已经在欧洲放弃了有争议的政策，因为价格一致性条款现在已被《欧洲数字市场法案》禁止，该法案旨在限制主要数字平台的力量。如果诉讼进入法院审理，Booking.com打算反对这些诉讼。

---

## 61. 地球上的闪电是由来自外太空的强大连锁反应引发的。

**原文标题**: Lightning on Earth is sparked by a powerful chain reaction from outer space

**原文链接**: [https://www.livescience.com/physics-mathematics/lightning-on-earth-is-sparked-by-a-powerful-chain-reaction-from-outer-space-simulations-show](https://www.livescience.com/physics-mathematics/lightning-on-earth-is-sparked-by-a-powerful-chain-reaction-from-outer-space-simulations-show)

本文探讨了长期以来闪电如何产生的谜团，提出一项新研究，表明来自外太空的宇宙射线起着至关重要的作用。 尽管闪电的电性已为人所知数个世纪，但暴风云产生必要电场的精确机制仍然难以捉摸。

该研究利用计算机模型和来自各种来源的数据，支持了宇宙射线触发导致闪电的链式反应的理论。 来自太阳和超新星等来源的高能质子撞击高层大气，产生电子，这些电子沿暴风云内的电场线加速。 这种加速导致电子在与氮气和氧气等大气分子碰撞时成倍增加，从而导致电子雪崩。

这种雪崩产生高能光子，包括 X 射线和伽马射线，模型解释说，它们通常先于闪电发生。 X 射线反过来又通过光电效应产生更多的“种子”电子，从而放大雪崩。 这种链式反应可能发生在强度不同的小区域内，解释了为什么一些伽马射线闪光会从看似昏暗且无线电静默的区域出现。

由 Victor Pasko 领导的这项研究为闪电的产生提供了一个“精确的定量解释”，将 X 射线、电场和电子雪崩联系起来。 该研究为宇宙射线如何促成被观察为闪电的强大放电提供了一个令人信服的解释。

---

## 62. 关注者少于1000的Instagram公共账号将无法直播。

**原文标题**: Instagram public accounts with less than 1k followers can no longer go live

**原文链接**: [https://www.engadget.com/apps/instagram-public-accounts-with-less-than-1000-followers-can-no-longer-go-live-133049758.html](https://www.engadget.com/apps/instagram-public-accounts-with-less-than-1000-followers-can-no-longer-go-live-133049758.html)

Instagram 现要求公开和私人账户至少拥有 1,000 名关注者才能使用直播功能。用户报告称收到通知，声明只有拥有 1000+ 关注者的账户才能创建直播视频。Meta 确认了这项新的资格要求，表示此举是为了确保创作者获得最佳体验并改善直播功能的整体使用情况。该公司并未解释为什么关注者较少的账户会阻碍这种“最佳体验”。虽然该通知目前仅提及公开账户，但 Meta 澄清说，该要求也将适用于私人账户。这一变化可能会取消向最多三位密友进行直播的功能，该功能于 2024 年初推出。简而言之，Instagram 正在限制其直播功能的访问权限，仅限拥有最低关注者数量的账户使用。

---

## 63. 数织：推断的复杂性与相变行为

**原文标题**: Nonogram: Complexity of Inference and Phase Transition Behavior

**原文链接**: [https://arxiv.org/abs/2507.07283](https://arxiv.org/abs/2507.07283)

Aaron Foote和Danny Krizanc撰写的arXiv文章“Nonogram：推理的复杂性和相变行为”探讨了Nonogram谜题的计算复杂性。尽管确定Nonogram *是否存在解*的问题已知在计算上是困难的，但作者研究了*推理问题*的复杂性——确定无需猜测即可逻辑推导出的谜题参数。

这项研究旨在调和Nonogram内在的难度与其在人类玩家中的受欢迎程度之间的明显矛盾。主要发现是：

1.  **推理的复杂性分析：** 该研究分析了Nonogram中推理问题的计算复杂性。
2.  **相变行为：** 该研究通过实验证明了推理问题难度中存在相变。具体而言，难度受到谜题中*填充单元的密度（正参数）*的极大影响。

为了方便他们的实验，作者开发了一种有效的方法，使用正则表达式将Nonogram板编码为合取范式 (CNF) 中的布尔公式。这种编码使得能够使用SAT求解器来分析推理问题。总而言之，该研究将解决Nonogram的难度与填充单元的密度联系起来，从而深入了解为什么人类通常可以解决它们，尽管它们在理论上很复杂。

---

## 64. 如何制作几乎任何东西 (2019)

**原文标题**: How to make almost anything (2019)

**原文链接**: [https://fab.cba.mit.edu/classes/863.19/CBA/people/dsculley/index.html](https://fab.cba.mit.edu/classes/863.19/CBA/people/dsculley/index.html)

本文档介绍了2019年“如何创造几乎所有东西”课程。 它介绍了剑桥谷歌的机器学习研究员D. Sculley，作为该课程的参与者。Sculley的兴趣源于机器学习在设计和制造领域的应用，包括生物学和化学等领域。他希望探索其他制造方法，并找到跨领域的联系。

Sculley的背景包括机器学习（自2003年以来）经验、教师教育经历以及本科视觉和环境研究（V.E.S.）背景。他计划积极参与课堂项目，并预计会犯错，欢迎有关机器学习的讨论。

该文档随后提供了课程内容的每周概述，涵盖了广泛的数字制造技术。 这些包括：

*   CAD和草图绘制
*   激光和乙烯基切割
*   电子产品制作
*   3D扫描和打印
*   电子设计
*   数控加工
*   嵌入式编程
*   模具和铸造
*   输入设备
*   输出设备
*   网络
*   机器周
*   应用程序编程
*   自由发挥周

该课程最终以一个最终项目结束。

---

## 65. Objects should shut the fuck up

**原文标题**: Objects should shut the fuck up

**原文链接**: [https://dustri.org/b/objects-should-shut-the-fuck-up.html](https://dustri.org/b/objects-should-shut-the-fuck-up.html)

作者抱怨日常用品发出不必要且常常适得其反的噪音。他的不满源于汽车液化石油气罐响亮的警报，他发现这在驾驶时会令人惊慌和分心，讽刺的是反而危及安全。他批评缺乏可配置性以及警报的重复性。

他将抱怨扩展到其他电器，特别是他的洗衣机和烘干机。他厌烦洗衣机上响亮、短暂的警报，以及无法禁用按钮操作时的提示音。烘干机也有一个无法避免的警报。他认为这些噪音，特别是对于非关键事件，是侵入性的和毫无意义的。

作者还强调了他的电磁炉，触摸式控制上有物体时会触发过度警报。他提出了替代解决方案，例如闪烁的灯光或自动关闭。

在他看来，最过分的例子是一个婴儿监视器，它在打开时会发出响亮的嘟嘟声，破坏了其主要目的——安静地监视一个正在睡觉的孩子。

他将这些有问题的设备与那些安静或有实用、微妙通知的电器进行对比，例如他的洗碗机、冰箱和电子书阅读器。

作者最后恳请设计师优先考虑安静的功能，并考虑通知对睡眠不足的人和正在睡觉的孩子的影响。他感叹需要在他的购物标准中添加“静音操作”。

---

## 66. Show HN: Gmap: 从命令行以可视化方式探索 Git 仓库

**原文标题**: Show HN: Gmap: Explore Git Repos Visually from the CLI

**原文链接**: [https://github.com/seeyebe/gmap](https://github.com/seeyebe/gmap)

生成摘要时出错

---

## 67. Palantir Is Extending Its Reach Even Further into Government

**原文标题**: Palantir Is Extending Its Reach Even Further into Government

**原文链接**: [https://www.wired.com/story/palantir-government-contracting-push/](https://www.wired.com/story/palantir-government-contracting-push/)

生成摘要时出错

---

## 68. Helsinki records zero traffic deaths for full year

**原文标题**: Helsinki records zero traffic deaths for full year

**原文链接**: [https://www.helsinkitimes.fi/finland/finland-news/domestic/27539-helsinki-records-zero-traffic-deaths-for-full-year.html](https://www.helsinkitimes.fi/finland/finland-news/domestic/27539-helsinki-records-zero-traffic-deaths-for-full-year.html)

生成摘要时出错

---

## 69. 可学习的编程 (2012)

**原文标题**: Learnable Programming (2012)

**原文链接**: [https://worrydream.com/LearnableProgramming/](https://worrydream.com/LearnableProgramming/)

生成摘要时出错

---

## 70. The Ski Rental Problem

**原文标题**: The Ski Rental Problem

**原文链接**: [https://lesves.github.io/articles/ski-rental/](https://lesves.github.io/articles/ski-rental/)

生成摘要时出错

---

## 71. Survival at High Altitudes: Wheel-Well Passengers (1996)

**原文标题**: Survival at High Altitudes: Wheel-Well Passengers (1996)

**原文链接**: [https://rosap.ntl.bts.gov/view/dot/57536](https://rosap.ntl.bts.gov/view/dot/57536)

生成摘要时出错

---

## 72. Names are not type safety (2020)

**原文标题**: Names are not type safety (2020)

**原文链接**: [https://lexi-lambda.github.io/blog/2020/11/01/names-are-not-type-safety/](https://lexi-lambda.github.io/blog/2020/11/01/names-are-not-type-safety/)

生成摘要时出错

---

## 73. Micron rolls out 276-layer SSD trio for speed, scale, and stability

**原文标题**: Micron rolls out 276-layer SSD trio for speed, scale, and stability

**原文链接**: [https://blocksandfiles.com/2025/07/30/micron-three-276-layer-ssds/](https://blocksandfiles.com/2025/07/30/micron-three-276-layer-ssds/)

Micron has announced three new SSDs leveraging their 276-layer 3D NAND technology, each targeting a distinct market segment. The 9650 is a high-performance PCIe Gen 6 SSD using TLC flash, aimed at accelerating AI training and inference. It comes in Pro (read-optimized) and Max (mixed-use) variants with capacities ranging from 6.4 TB to 30.72 TB. Key specs include up to 5.5 million random read IOPS and 28 GBps sequential read bandwidth.

The 6600 ION is a high-capacity PCIe Gen 5 drive, reaching up to 122.88 TB, that uses QLC flash for maximum storage density. It offers higher random read IOPS than its predecessor but lower random write IOPS. A larger 245 TB version is planned for 2026.

Finally, the 7600 is a PCIe Gen 5 TLC SSD designed for consistent low latency, positioned for AI, databases, and cloud computing. It comes in Pro and Max versions with capacities between 1.6 TB and 15.36 TB. All three SSDs incorporate Micron's DRAM, NAND, controller, and firmware, and feature robust security options. The 9650 and 7600 samples are currently shipping, while the 122 TB 6600 ION samples will ship in Q3 2025.


---

## 74. A Real PowerBook: The Macintosh Application Environment on a Pa-RISC Laptop

**原文标题**: A Real PowerBook: The Macintosh Application Environment on a Pa-RISC Laptop

**原文链接**: [http://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html](http://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html)

生成摘要时出错

---

## 75. Poorest US workers hit hardest by slowing wage growth

**原文标题**: Poorest US workers hit hardest by slowing wage growth

**原文链接**: [https://www.ft.com/content/cfb77a53-fef8-4382-b102-c217e0aa4b25](https://www.ft.com/content/cfb77a53-fef8-4382-b102-c217e0aa4b25)

生成摘要时出错

---

## 76. UN report finds UN reports are not widely read

**原文标题**: UN report finds UN reports are not widely read

**原文链接**: [https://www.reuters.com/world/un-report-finds-united-nations-reports-are-not-widely-read-2025-08-01/](https://www.reuters.com/world/un-report-finds-united-nations-reports-are-not-widely-read-2025-08-01/)

生成摘要时出错

---

## 77. Show HN: Schematra – Sinatra-inspired minimal web framework for Chicken Scheme

**原文标题**: Show HN: Schematra – Sinatra-inspired minimal web framework for Chicken Scheme

**原文链接**: [https://github.com/rolandoam/schematra](https://github.com/rolandoam/schematra)

生成摘要时出错

---

## 78. 苹果缺乏战略眼光

**原文标题**: Apple lacks strategic vision

**原文链接**: [https://unherd.com/2025/08/time-is-running-out-for-tim-cook/?lang=us](https://unherd.com/2025/08/time-is-running-out-for-tim-cook/?lang=us)

Patrick McGee's article argues that Tim Cook's tenure as Apple CEO is increasingly under scrutiny due to a perceived lack of strategic vision, particularly in the face of the AI revolution. While Cook successfully scaled Apple and generated significant profits, the company now lags behind competitors like Microsoft, Alphabet, and Nvidia in innovation and growth.

The article highlights several key issues: Apple's slow adoption of AI, evidenced by Siri's stagnation and delays in releasing "Apple Intelligence"; the company's over-reliance on China for manufacturing, which has empowered local competitors; and Cook's diminished diplomatic influence compared to Nvidia's CEO. While Apple was once seen as staying ahead of the competition, it now appears to be a complacent observer while other companies, particularly Nvidia, are rapidly advancing in AI.

The iPhone design has stagnated, the electric car project was scrapped, and the Vision Pro headset faces a lack of compelling content. The article questions whether Cook, whose mandate was scaling rather than innovation, is still the right leader for Apple, especially as the company faces increasing competition and the need to adapt to the AI-driven future. While Apple remains profitable, its slow growth and lack of a clear AI strategy raise concerns about its long-term competitiveness.


---

## 79. Shrinking freshwater availability increasing land contribution to sea level rise

**原文标题**: Shrinking freshwater availability increasing land contribution to sea level rise

**原文链接**: [https://news.asu.edu/20250725-environment-and-sustainability-new-global-study-shows-freshwater-disappearing-alarming](https://news.asu.edu/20250725-environment-and-sustainability-new-global-study-shows-freshwater-disappearing-alarming)

生成摘要时出错

---

## 80. Automerge 3.0

**原文标题**: Automerge 3.0

**原文链接**: [https://automerge.org/blog/automerge-3/](https://automerge.org/blog/automerge-3/)

生成摘要时出错

---

## 81. Flourishing chemosynthetic life at the greatest depths of hadal trenches

**原文标题**: Flourishing chemosynthetic life at the greatest depths of hadal trenches

**原文链接**: [https://www.nature.com/articles/s41586-025-09317-z](https://www.nature.com/articles/s41586-025-09317-z)

生成摘要时出错

---

## 82. The US military’s on-base slot machines

**原文标题**: The US military’s on-base slot machines

**原文链接**: [https://www.wired.com/story/us-military-on-base-slot-machines-gambling-addiction/](https://www.wired.com/story/us-military-on-base-slot-machines-gambling-addiction/)

生成摘要时出错

---

## 83. LangExtract: Python library for extracting structured data from language models

**原文标题**: LangExtract: Python library for extracting structured data from language models

**原文链接**: [https://github.com/google/langextract](https://github.com/google/langextract)

生成摘要时出错

---

## 84. HTML-in-Canvas

**原文标题**: HTML-in-Canvas

**原文链接**: [https://github.com/WICG/html-in-canvas](https://github.com/WICG/html-in-canvas)

生成摘要时出错

---

## 85. Ultra Ethernet: Reinventing X.25

**原文标题**: Ultra Ethernet: Reinventing X.25

**原文链接**: [https://blog.ipspace.net/2025/07/ultra-ethernet-reinventing-x25/](https://blog.ipspace.net/2025/07/ultra-ethernet-reinventing-x25/)

生成摘要时出错

---

## 86. A study of lights at night suggests dictators lie about economic growth (2022)

**原文标题**: A study of lights at night suggests dictators lie about economic growth (2022)

**原文链接**: [https://www.economist.com/graphic-detail/2022/09/29/a-study-of-lights-at-night-suggests-dictators-lie-about-economic-growth](https://www.economist.com/graphic-detail/2022/09/29/a-study-of-lights-at-night-suggests-dictators-lie-about-economic-growth)

生成摘要时出错

---

## 87. Extreme black hole system OJ 287 just got more interesting

**原文标题**: Extreme black hole system OJ 287 just got more interesting

**原文链接**: [https://bigthink.com/starts-with-a-bang/black-hole-oj-287/](https://bigthink.com/starts-with-a-bang/black-hole-oj-287/)

生成摘要时出错

---

## 88. 2,500-year-old Siberian 'ice mummy' had intricate tattoos, imaging reveals

**原文标题**: 2,500-year-old Siberian 'ice mummy' had intricate tattoos, imaging reveals

**原文链接**: [https://www.bbc.com/news/articles/c4gzx0zm68vo](https://www.bbc.com/news/articles/c4gzx0zm68vo)

生成摘要时出错

---

## 89. Ghost 6.0

**原文标题**: Ghost 6.0

**原文链接**: [https://ghost.org/changelog/6/](https://ghost.org/changelog/6/)

生成摘要时出错

---

## 90. The Algebra Gatekeepers

**原文标题**: The Algebra Gatekeepers

**原文链接**: [https://www.educationprogress.org/p/the-algebra-gatekeepers](https://www.educationprogress.org/p/the-algebra-gatekeepers)

生成摘要时出错

---

## 91. Splatshop: Efficiently Editing Large Gaussian Splat Models

**原文标题**: Splatshop: Efficiently Editing Large Gaussian Splat Models

**原文链接**: [https://momentsingraphics.de/HPG2025.html](https://momentsingraphics.de/HPG2025.html)

生成摘要时出错

---

## 92. Microsoft is open sourcing Windows 11's UI framework

**原文标题**: Microsoft is open sourcing Windows 11's UI framework

**原文链接**: [https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/](https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/)

生成摘要时出错

---

## 93. CloudGazing

**原文标题**: CloudGazing

**原文链接**: [https://cloudgazing.online/](https://cloudgazing.online/)

生成摘要时出错

---

## 94. Even Happier Eyeballs

**原文标题**: Even Happier Eyeballs

**原文链接**: [https://daniel.haxx.se/blog/2025/08/04/even-happier-eyeballs/](https://daniel.haxx.se/blog/2025/08/04/even-happier-eyeballs/)

生成摘要时出错

---

## 95. Ghost 6.0

**原文标题**: Ghost 6.0

**原文链接**: [https://ghost.org/6](https://ghost.org/6)

生成摘要时出错

---

## 96. Tokens are getting more expensive

**原文标题**: Tokens are getting more expensive

**原文链接**: [https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed](https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed)

生成摘要时出错

---

## 97. The Fulbright Program: Chock Full of Bright Ideas

**原文标题**: The Fulbright Program: Chock Full of Bright Ideas

**原文链接**: [https://bastian.rieck.me/blog/2025/fulbright/](https://bastian.rieck.me/blog/2025/fulbright/)

生成摘要时出错

---

## 98. Happy Birthday 6502

**原文标题**: Happy Birthday 6502

**原文链接**: [https://hackaday.com/2025/08/04/happy-birthday-6502/](https://hackaday.com/2025/08/04/happy-birthday-6502/)

生成摘要时出错

---

## 99. Ongoing Lean formalization of the proof for Fermat's Last Theorem

**原文标题**: Ongoing Lean formalization of the proof for Fermat's Last Theorem

**原文链接**: [https://github.com/ImperialCollegeLondon/FLT](https://github.com/ImperialCollegeLondon/FLT)

生成摘要时出错

---

## 100. The Dollar Is Dead

**原文标题**: The Dollar Is Dead

**原文链接**: [https://mathmeetsmoney.substack.com/p/the-dollar-is-dead](https://mathmeetsmoney.substack.com/p/the-dollar-is-dead)

生成摘要时出错

---

