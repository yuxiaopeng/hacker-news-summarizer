# Hacker News 热门文章摘要 (2025-10-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Willow quantum chip demonstrates verifiable quantum advantage on hardware

**原文标题**: Willow quantum chip demonstrates verifiable quantum advantage on hardware

**原文链接**: [https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/](https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/)

Google Quantum AI's "Willow" quantum chip has achieved a significant breakthrough: demonstrating verifiable quantum advantage on hardware for the first time. Their "Quantum Echoes" algorithm, published in Nature, runs 13,000 times faster than the best classical algorithm on a supercomputer and can be repeatedly verified on similar quantum computers.

The Quantum Echoes algorithm measures out-of-order time correlators (OTOC) and can be used to learn the structure of complex systems, from molecules to black holes. It works by sending a signal into the quantum system, perturbing a qubit, reversing the signal, and listening for the "echo," which is amplified by constructive interference.

The team also demonstrated a "molecular ruler" technique, using Quantum Echoes and Nuclear Magnetic Resonance (NMR) data to measure molecular geometry, gaining more information about chemical structure than traditional methods. This was verified in a proof-of-principle experiment with molecules containing 15 and 28 atoms in partnership with The University of California, Berkeley.

This verifiable quantum advantage is enabled by Willow's low error rates and high-speed operations. The algorithm tests both complexity and precision, crucial for real-world applications. The advances have the potential to enhance NMR technology, leading to a "quantum-scope" for observing previously unobservable natural phenomena, impacting fields like drug discovery and materials science.

The team is now focusing on achieving a long-lived logical qubit, a key milestone in their quantum hardware roadmap.


---

## 2. 推出 Galaxy XR，首款安卓 XR 头显

**原文标题**: Introducing Galaxy XR, the first Android XR headset

**原文链接**: [https://blog.google/products/android/samsung-galaxy-xr/](https://blog.google/products/android/samsung-galaxy-xr/)

三星Galaxy XR是首款基于Android XR的设备，这是一款融合数字与物理体验并集成Gemini AI的新操作系统。它提供了一个无限屏幕，可用于Google Play的应用程序和全新的XR体验，通过语音、手势和眼睛进行控制。主要功能包括通过YouTube和Google TV进行沉浸式电影观看，使用Google Photos将2D照片转换为3D，以及使用Google Maps在3D中探索世界，所有这些都通过Gemini的上下文帮助得到增强。Galaxy XR还提供了一个带有多个应用程序、键盘/鼠标支持以及Gemini组织帮助的广阔工作空间。

该头显利用Gemini提供关于屏幕内容的实时信息，例如篮球比赛期间的球员统计数据，或Google Maps中地标的历史背景。它支持为XR重新设计的Google应用程序，全新的XR体验以及数百万个移动和平板电脑应用程序。

Galaxy XR在美国和韩国的Samsung.com和三星体验店有售，价格为1799美元或每月149美元。限时“探索者套装”提供订阅捆绑包，包括Google AI Pro，YouTube Premium，Google Play Pass，访问流媒体服务试用版，体育通行证以及提前访问Adobe的Project Pulsar和Status Pro的NFL PRO ERA等应用程序。Android XR系统还支持OpenXR，WebXR和Unity等开放标准。预计未来将会有更多基于Android XR的设备和体验。

---

## 3. Cloudflare Circl FourQ 实现中的密码学问题 (CVE-2025-8556)

**原文标题**: Cryptographic Issues in Cloudflare's Circl FourQ Implementation (CVE-2025-8556)

**原文链接**: [https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation](https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation)

This article details CVE-2025-8556, a vulnerability discovered in Cloudflare's CIRCL library, specifically in its implementation of the FourQ elliptic curve. The vulnerability stems from insufficient validation of points used in cryptographic calculations, making the implementation susceptible to invalid point attacks.

The FourQ curve, designed for efficiency in resource-constrained environments, relies on specific characteristics including endomorphisms. The core issue lies in the `Shared` function of `Curve4Q` (a Diffie-Hellman implementation), where a public point isn't validated for curve membership before scalar multiplication with a secret key. This allows attackers to supply invalid points, potentially belonging to curves with small subgroup orders, which drastically reduces the difficulty of recovering the server's secret key via brute-force methods and the Chinese Remainder Theorem.

While traditional invalid curve attacks on Weierstrass curves don't directly translate to Edwards curves like FourQ, a specific attack vector exploiting points of the form (0, y) was identified. This allows manipulation of the scalar multiplication to reveal the secret key.

The reported issues include: incorrect point validation during unmarshalling (missing conjugate validation), a faulty point comparison in `pointR1.isEqual` that returns true when Z = 0, lack of point validation after cofactor clearing in `pointR1.ClearCofactor`, and the absence of pre-validation in `pointR1.ScalarMult`, which is vulnerable to degenerate curve attacks. Cloudflare addressed the major points raised.


---

## 4. Linux Capabilities Revisited

**原文标题**: Linux Capabilities Revisited

**原文链接**: [https://dfir.ch/posts/linux_capabilities/](https://dfir.ch/posts/linux_capabilities/)

生成摘要时出错

---

## 5. MinIO停止分发免费Docker镜像

**原文标题**: MinIO stops distributing free Docker images

**原文链接**: [https://github.com/minio/minio/issues/21647#issuecomment-3418675115](https://github.com/minio/minio/issues/21647#issuecomment-3418675115)

本次问题报告指出，Quay.io和DockerHub上均缺少最近MinIO安全版本(Security/CVE RELEASE.2025-10-15T17-29-55Z)的新的Docker镜像。报告人neil-lcv-cs询问这是否是有意的，如果不是，则请求发布新的Docker镜像。该问题被标记为“社区”和“按预期工作”，表明MinIO可能有意停止为该安全版本提供免费Docker镜像，或者由于其他原因该版本未通过Docker分发。报告人和至少22人对最初的报告表示赞同。

---

## 6. 为易腐物品设计软件

**原文标题**: Designing software for things that rot

**原文链接**: [https://drobinin.com/posts/designing-software-for-things-that-rot/](https://drobinin.com/posts/designing-software-for-things-that-rot/)

软件设计与发酵的交汇：一个软件工具“Fermento”的开发历程

---

## 7. Bild AI (YC W25) 正在招聘创始 AI 工程师

**原文标题**: Bild AI (YC W25) Is Hiring a Founding AI Engineer

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai](https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai)

Bild AI（YC W25）是一家专注于将人工智能应用于建筑蓝图的初创公司，正在旧金山招聘创始AI工程师。该职位提供10万至18万美元的薪资，以及0.50%至2.00%的股权。Bild AI旨在简化蓝图阅读、成本估算和许可证申请流程，从而更高效地建造房屋、医院和学校。

理想的候选人将专注于智能层，应用最新的计算机视觉、大型语言模型和人工智能系统，根据用户反馈快速进行原型设计和迭代。期望的资质包括应用计算机视觉/机器学习经验、从零开始构建和部署人工智能解决方案的经验、成长型思维、强大的沟通能力，以及愿意处理创业生活中不太光鲜的一面。有成功产品的早期创业/创始人经验、建筑背景以及以影响力为导向的动机者将获得加分。

申请人应说明他们为何适合该职位，并分享他们最喜欢的水果。该职位要求全职在旧金山办公室工作，或愿意搬迁。Bild AI成立于2024年，是YC W25的一部分，采用模型花园方法来解决蓝图理解中的复杂技术挑战，并已获得顶级风险投资的支持。创始人是Roop Pal和Puneet Sukhija。

---

## 8. AI助手45%的时间内错误呈现新闻内容

**原文标题**: AI assistants misrepresent news content 45% of the time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content](https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content)

EBU与BBC联合研究揭示AI助手常曲解新闻内容

---

## 9. Meta 裁减其人工智能部门 600 个职位

**原文标题**: Meta is axing 600 roles across its AI division

**原文链接**: [https://www.theverge.com/news/804253/meta-ai-research-layoffs-fair-superintelligence](https://www.theverge.com/news/804253/meta-ai-research-layoffs-fair-superintelligence)

Meta裁减人工智能部门600个职位，涉及基础人工智能研究(FAIR)部门、人工智能产品和基础设施部门。尽管公司仍在为其新成立的超智能团队TBD Lab招聘，但仍采取了这一举措。Meta发言人证实了裁员，此前公司曾对人工智能进行大量投资和招聘，包括聘请Scale AI首席执行官Alexandr Wang。此次重组标志着公司将重点转向与人工智能相关的产品和基础设施，而FAIR则退居次要地位。Meta人工智能负责人Wang表示，公司旨在将FAIR的研究成果整合到TBD Lab中。裁员旨在通过创建一个更小、更具影响力的团队来简化决策流程。受影响的员工将有机会申请Meta内部的其他职位。

---

## 10. 本地LLM的安全悖论

**原文标题**: The security paradox of local LLMs

**原文链接**: [https://quesma.com/blog/local-llms-security-paradox/](https://quesma.com/blog/local-llms-security-paradox/)

Jacek Migdal 的文章强调了使用本地 LLM 保护隐私的一个安全悖论。 虽然本意是更安全，但对 gpt-oss-20b 的研究表明，它们比大型前沿模型更容易受到恶意提示的攻击。 这是因为它们识别恶意意图的能力较弱。

该文章详细介绍了两种攻击：第一种是“彩蛋”后门，通过将其伪装成无害的功能来植入成功率高达 95% 的隐藏 RCE 后门。 第二种是通过认知过载实现的即时 RCE，诱骗模型在代码生成期间执行恶意代码。 这种攻击虽然成功率较低 (43.5%)，但由于其即时性而十分危险。

这些攻击通过将恶意提示注入 AI 助手的上下文中来实现，途径包括文档污染、受损的 MCP 服务器或社会工程。 该文章强调，由于本地模型推理能力较弱、对齐效果较差且安全训练有限，因此会加剧这种情况。 前沿模型虽然可能更安全，但由于提供商的限制，难以进行测试。

文章最后提倡一种新的防御方式，包括对生成的代码进行静态分析、沙盒化初始执行、监控输入、输出和网络流量，以及使用较小、更简单的模型进行“二次审查”以检查政策违规情况。 关键在于，所有 AI 生成的代码都应持怀疑态度，认识到本地 LLM 虽然具有隐私优势，但也需要强大的安全措施。

---

## 11. 尽可能多的CPU和其他有趣芯片的芯片照片

**原文标题**: Die shots of as many CPUs and other interesting chips as possible

**原文链接**: [https://commons.wikimedia.org/wiki/User:Birdman86](https://commons.wikimedia.org/wiki/User:Birdman86)

这个维基共享资源页面是由 Pauli Rautakorpi 发起的一个项目，旨在收集和整理各种 CPU 和其他集成电路的芯片照片（内部电路照片）。该页面作为一个索引，将这些芯片照片分类到不同的芯片类别和系列中，以便于浏览。

该合集内容广泛，涵盖了从 x86 CPU 和 FPU（包括 Intel、AMD、Cyrix 等）到 AMD、Intel、DEC、HP、Motorola、MIPS、SPARC、ARM 等制造商的其他 CPU 和 FPU 的各种处理器。该列表包括每个系列中的特定型号，通常会注明不同的修订版本或变体。

除了 CPU 和 FPU 之外，该合集还包括各种支持芯片的芯片照片，例如缓存控制器、内存控制器、内存管理单元、DMA 控制器、总线/接口控制器、中断控制器和网络控制器。它还包括来自德州仪器、模拟器件、摩托罗拉和英特尔等制造商的数字信号处理器 (DSP) 和微控制器部分。此外，该合集还包含图形芯片、视频编/解码器、RAMDAC、存储芯片和加密芯片的芯片照片。该项目正在进行中，随着新的芯片照片的出现，会不断添加。该页面还提供一个链接，指向贡献者的完整文件列表，以供进一步探索。

---

## 12. 互联网最大的烦恼：Cookie法应针对浏览器，而非网站

**原文标题**: Internet's biggest annoyance: Cookie laws should target browsers, not websites

**原文链接**: [https://nednex.com/en/the-internets-biggest-annoyance-why-cookie-laws-should-target-browsers-not-websites/](https://nednex.com/en/the-internets-biggest-annoyance-why-cookie-laws-should-target-browsers-not-websites/)

本文认为，目前Cookie同意法律（如GDPR和CCPA）的实施是失败的，因为它将同意的负担置于各个网站，导致用户厌烦、同意疲劳，以及小型企业面临不成比例的困难。作者提出转变重点，主张由浏览器来处理Cookie同意事宜。

当前系统的主要问题是：1）同意疲劳使Cookie横幅变得毫无意义；2）它给小型企业带来了不成比例的负担；3）它提供了一种虚假的控制感，促使用户为了方便而接受所有Cookie。

提议的解决方案是浏览器中心模型，用户在浏览器设置中一次性设置其隐私偏好。然后，浏览器充当个人隐私执行者，根据用户预定义的选项自动允许或拒绝Cookie。这种方法将提供以下几个好处：

*   **对于用户：** 真正的控制和更简洁的网络体验，无需持续不断的Cookie横幅。
*   **对于网站所有者：** 减轻合规负担，无需复杂且降低性能的同意管理平台。
*   **对于监管机构：** 通过关注少数浏览器开发商而非数百万个网站，更容易执行。

作者强调，这种改变将简化当前复杂的系统，用基于浏览器的单一真实来源取代脆弱的合规工具拼凑。它旨在简化用户、创建者和监管机构的流程，创造一个更私密、更少烦扰的互联网。

---

## 13. SourceFS：借助虚拟文件系统，原本2小时以上的Android构建任务缩短至15分钟

**原文标题**: SourceFS: A 2h+ Android build becomes a 15m task with a virtual filesystem

**原文链接**: [https://www.source.dev/journal/sourcefs](https://www.source.dev/journal/sourcefs)

SourceFS：利用虚拟文件系统将Android构建从2小时缩短至15分钟

---

## 14. 对数时间感知假说

**原文标题**: The Logarithmic Time Perception Hypothesis

**原文链接**: [http://www.kafalas.com/Logtime.html](http://www.kafalas.com/Logtime.html)

詹姆斯·梅因·肯尼的“对数时间感知假说”(Logtime) 提出我们对时间流逝的感知并非线性的，而是对数的，随着年龄增长而收缩。该理论认为，我们根据当前的年龄来判断时间间隔的长短。一年对于一个幼儿来说代表着更大的人生比例，因此我们主观感觉时间随着年龄增长而加速。

肯尼创造了术语“心理计时学”来描述对主观时间估计的研究，并将 Logtime 作为理解人类时间体验的数学模型。他认为这种对数感知与支配我们对物理刺激感知的韦伯-费希纳定律相符。

该文章介绍了“生命八度”的概念——起始年龄和结束年龄之比为 2:1 的时期（例如，10-20 岁、20-40 岁、40-80 岁）。这些八度音阶被认为是同样感知到的时间单位，取代了线性的十年概念。他认为，由于幼儿时期与我们现在的年龄在对数上的距离增加，所以回忆起童年早期更加困难。

作者提供了各种对数刻度和内插八度音阶，以说明在人生的不同阶段如何以不同的方式体验主观时间。他承认准确测量这些感知的局限性，并指出外部因素和适应不断变化的环境会影响我们的主观时间感知。文章最后提出了使用不同八度音阶及其内插的建议，作者指出音乐家可能喜欢缩放八度音阶，这是音乐界常用的术语。

---

## 15. Patina：UEFI固件的Rust实现

**原文标题**: Patina: a Rust implementation of UEFI firmware

**原文链接**: [https://github.com/OpenDevicePartnership/patina](https://github.com/OpenDevicePartnership/patina)

Patina：一种 Rust 实现的 UEFI 固件，旨在用内存安全的 Rust 替代方案取代基于 C 的核心组件，从而在不牺牲启动性能的前提下，增强系统固件的安全性和稳定性。目前处于 Beta 阶段，欢迎进行平台测试和集成反馈。

发布版本通过 GitHub Releases 进行管理，该版本会触发工作流程以更新 Cargo.toml 版本。文档位于 OpenDevicePartnership.github.io/patina/，可以使用 `mdbook` 自行托管。该文档概述了工具设置，包括 `rustup`、`cargo-make` 和 `cargo-llvm-cov`。

构建说明涵盖 aarch64、x64 和原生目标，包括开发和发布配置文件。测试包括运行单元测试和构建平台上测试。建议每季度更新 Rust 版本，并应由 `OpenDevicePartnership/patina-contributors` 团队进行审查。

路线图侧重于稳定化（错误修复、性能）、扩展（新组件、MM Core 支持）和生态系统集成（固件和 Rust）。欢迎贡献。

---

## 16. 法国前总统萨科齐开始服刑

**原文标题**: French ex-president Sarkozy begins jail sentence

**原文链接**: [https://www.bbc.com/news/articles/cvgkm2j0xelo](https://www.bbc.com/news/articles/cvgkm2j0xelo)

前法国总统萨科齐因共谋利用卡扎菲利比亚资金非法资助其2007年竞选活动，已开始服刑五年。他是二战后第一位被判入狱的前法国总统。

萨科齐坚称自己无罪，已被送往巴黎的桑特监狱，为安全起见，他将被关押在隔离区。他将拥有一个配备基本设施的小牢房，并限制与其他囚犯的接触。

尽管萨科齐对判决提出上诉，但他因指控的严重性而被勒令入狱。他表达了对法国的悲伤之情，并重申他相信真相终将获胜。他的律师已经提交了释放申请。

这次监禁在法国引起了巨大反响。马克龙总统在萨科齐入狱前在爱丽舍宫接见了他，并对情况发表了评论，但没有批评司法裁决。司法部长达尔马宁也计划探望狱中的萨科齐。

萨科齐还面临进一步的法律挑战，包括即将对Bygmalion事件中，另一起非法竞选资金案，提出的六个月监禁上诉的判决。自2012年卸任以来，他一直受到刑事调查的困扰。

---

## 17. 围棋妙手

**原文标题**: Go subtleties

**原文链接**: [https://harrisoncramer.me/15-go-sublteties-you-may-not-already-know/](https://harrisoncramer.me/15-go-sublteties-you-may-not-already-know/)

对开发者有益的 18 个 Go 语言技巧

1. **遍历整数:** 在 Go 1.22+ 中，可以直接使用 `range` 迭代整数。
2. **重命名包:** Go 的 LSP 允许重命名包，更新所有引用和目录名。
3. **约束泛型函数签名:** 使用 `~` 将泛型类型约束为底层类型，对类型化的常量很有用。
4. **基于索引的字符串插值:** 在 `fmt.Printf` 中使用 `%[index]s` 来重用插值。
5. **`time.After` 函数:** 创建一个通道，该通道在指定的持续时间后接收消息，可用于带有 `select` 的超时。
6. **`embed` 包:** 将非 Go 文件嵌入到二进制文件中，简化部署。
7. **带有字符串和 UTF-8 的 `len()`:** `len()` 返回字节数，而不是字符数。使用 `range` 迭代 runes（代码点）。
8. **Nil 接口:** 封装在接口中的 nil 值不是 nil。这可能会导致 nil 检查中出现意外行为。
9. **在 Nil 值上调用方法:** 你可以在 nil 结构体指针上调用方法，但访问属性会 panic。
10. **使用 Ranging 遍历 Map 的变量引用:** 由于内部哈希和存储桶，在 map 循环内的更新可能不会立即显示。
11. **返回自定义错误:** 定义错误类型以提供结构化数据和自定义逻辑。
12. **上下文感知函数:** 始终选择上下文来处理取消并避免不必要的等待。传播上下文时要小心。
13. **空结构体:** 占用零字节，通常用于在通道上发出信号。
14. **Go 编译器和 range 关键字:** range 关键字被降低为基本循环。
15. **隐藏的接口实现:** 嵌入的结构体可以隐式地提升方法，可能会覆盖所需的行为，例如 JSON 序列化。使用结构体嵌入时要小心！
16. **JSON 的 “-” 标签:** 在序列化期间从 JSON 输出中省略字段。
17. **比较时间:** 不要对 `time.Time` 值使用字符串比较；使用 `.Equal()` 方法。
18. **wg.Go 函数:** Go 1.25 引入了一种方便的方法来向等待组添加 Go 例程。

---

## 18. 硬盘挖矿 (2012)

**原文标题**: Farming Hard Drives (2012)

**原文链接**: [https://www.backblaze.com/blog/backblaze_drive_farming/](https://www.backblaze.com/blog/backblaze_drive_farming/)

2011年末，泰国毁灭性洪水重创硬盘制造业，导致价格飙升，并威胁到Backblaze的无限数据备份服务模式。该公司面临关键硬盘成本上涨200%的困境，亟需找到解决方案，以继续提供每月5美元的服务。

Backblaze启动了一项名为“硬盘农场”的策略，安排员工、朋友和家人从Costco和百思买等零售店购买外置硬盘。然后将这些硬盘“拆解”（从外壳中取出），用于Backblaze的存储舱。尽管需要额外的人工和回收成本，但这样做比购买内置硬盘更便宜。

最初，员工们搜遍了当地商店，但购买数量的限制迫使Backblaze将行动扩大到全国范围，依靠朋友和家人购买并运送硬盘。该公司继续面临挑战，包括购买限制和供应商短缺。尽管面临这些困难，Backblaze还是避免了提价，这一决定与其他科技公司形成对比。

“硬盘农场”行动一直持续到2012年初，最终获得了5.5拍字节的存储空间。随着泰国的复苏和硬盘生产的正常化，Backblaze得以回归传统的采购渠道。他们对在危机期间帮助过他们的人表示感谢。文章的尾声讲述了Backblaze在2012年晚些时候获得了风险投资，并利用Costco的交易购买了更多硬盘。

---

## 19. 一种无需稳定化即可并行计算的非对角SSM RNN

**原文标题**: A non-diagonal SSM RNN computed in parallel without requiring stabilization

**原文链接**: [https://github.com/glassroom/goom_ssm_rnn](https://github.com/glassroom/goom_ssm_rnn)

本文介绍`goom_ssm_rnn`，一种深度循环神经网络（RNN）实现，它利用广义数量级（GOOMs）来实现非对角线性状态空间模型（SSM）递归的并行计算，而无需稳定化。 其关键创新在于在循环层中使用复数类型GOOMs（torch.complex64张量），从而使模型能够有效地捕获具有非对角SSM的序列依赖性。

该RNN被设计为PyTorch `nn.Module`，并提供便捷的方法来进行参数分组（带/不带权重衰减）、损失和准确率计算以及文本生成。 虽然复数张量的使用限制了完整的PyTorch编译，但部分编译仍然是可能的，从而显著提高了性能。 作者强调，对于浮点张量，支持自动转换为`torch.float16`。

本文展示了使用The Pile数据集进行自然语言生成的性能基准测试，使用1.24亿参数模型实现了具有竞争力的结果（10B token后交叉熵约为2.7）。 该模型还在诸如Sequential MNIST（生成和分类）、Wikitext-103和Copy-Memory任务等任务上表现出强大的性能，使用了较小的配置（1280万-3800万参数）。 详细介绍了实现这些结果的超参数设置。 代码完全记录在`goom_ssm_rnn.py`中，可以很容易地修改以用于各种任务。 作者强调了他们的方法对于在RNN中实现可扩展和并行的高动态范围计算的重要性。

---

## 20. 评估AMD Strix Halo中的Infinity Cache

**原文标题**: Evaluating the Infinity Cache in AMD Strix Halo

**原文链接**: [https://chipsandcheese.com/p/evaluating-the-infinity-cache-in](https://chipsandcheese.com/p/evaluating-the-infinity-cache-in)

Chester Lam 的这篇文章评估了 AMD 的 Infinity Cache 在 Strix Halo APU 中的有效性，特别是其在图形工作负载中缓解 DRAM 带宽瓶颈的能力。 Strix Halo 结合了强大的 CPU 和 GPU，配备 256 位 LPDDR5X-8000 设置和 32 MB Infinity Cache。

Lam 利用相干站 (CS) 和统一内存控制器 (UMC) 的性能监控工具，通过比较流量水平来估算 Infinity Cache 命中率。 CS 上的流量而 UMC 上没有的流量表明缓存命中。

结果表明，在测试的图形工作负载中，32 MB Infinity Cache 有效地使 Strix Halo 远低于其理论上的 256 GB/s DRAM 带宽限制。 虽然某些工作负载接近该限制，但缓存始终能提高带宽效率。 作者指出，各种分辨率和工作负载类型如何影响缓存性能，观察到增加分辨率通常会降低命中率，但缓存仍然可以显著降低 DRAM 带宽需求。

文章还将 Strix Halo 的内存设置与 PS5 的内存设置进行了比较，表明 Strix Halo 的缓存和 DRAM 带宽组合是仅使用高带宽 GDDR6 解决方案的一种节能替代方案，尤其适用于移动设备。

最终，文章得出结论，AMD 选择 32 MB 缓存和 256 GB/s DRAM 带宽对于各种工作负载来说都是经过精心调整的。 Lam 表示希望 AMD 的开发者工具能够提供有关 Infinity Cache 命中率的直接数据，以便更好地了解其性能。

---

## 21. Show HN: Cadence – 吉他乐理应用

**原文标题**: Show HN: Cadence – A Guitar Theory App

**原文链接**: [https://cadenceguitar.com/](https://cadenceguitar.com/)

Cadence：一款通过互动课程和游戏化挑战，让学习吉他理论和练耳变得有趣且引人入胜的应用。该应用将吉他理论分解为小节课程，辅以视觉和听觉辅助，并进行直观的总结以巩固内容。用户可以通过难度递增的理论、视觉和听觉挑战来测试他们的知识，并在进步过程中赢得奖杯。

一个关键功能是专门的练耳训练，使用户能够通过听觉识别音程、和弦、音阶和进行。包括每日活动报告和连胜记录的进度跟踪有助于保持动力。

Cadence提供了一个全面的吉他库，其中包含2000多个不同位置的和弦、音阶（CAGED、3NPS、八度）、琶音以及带有发声建议的进行。

该应用提供一个免费层级，其中包括初学者课程和挑战，每天5次挑战尝试，进度跟踪以及对吉他库的完全访问权限。Pro订阅（按月或按年提供）可解锁所有课程和挑战、无限次挑战尝试、练习模式和自定义库预设。两种层级都提供无广告体验，并且可以选择多设备同步。还可以通过一次性购买获得永久访问权限。

---

## 22. 以太网供电（PoE）基础及进阶

**原文标题**: Power over Ethernet (PoE) basics and beyond

**原文链接**: [https://www.edn.com/poe-basics-and-beyond-what-every-engineer-should-know/](https://www.edn.com/poe-basics-and-beyond-what-every-engineer-should-know/)

无法访问文章链接。

---

## 23. 敲门者：一个基于敲击的家庭实验室访问控制系统

**原文标题**: Knocker, a knock based access control system for your homelab

**原文链接**: [https://github.com/FarisZR/knocker](https://github.com/FarisZR/knocker)

Knocker：自托管的单包授权（SPA）网关，旨在通过提供基于 HTTP 的“敲敲门”系统来增强家庭实验室环境中的安全性。它通过保持服务的私密性，并且仅为授权 IP 地址按需开放来保护服务。Knocker 可以与 Caddy 等反向代理集成，甚至可以在防火墙级别使用 FirewallD。

主要功能包括：API 密钥身份验证、可配置的 IP 白名单有效期 (TTL)、远程白名单、静态 IP 白名单、基于路径的排除以及 IPv6 支持。它提供 Web、CLI 和 Android 客户端，方便敲门。

Knocker 的工作原理是验证 API 密钥，并将客户端 IP 加入白名单，有效期可指定。与 Caddy 集成时，它充当身份验证网关，向非白名单 IP 返回 401 未授权响应。FirewallD 集成允许 Knocker 创建动态的、基于时间的防火墙规则，并根据 TTL 自动过期这些规则，即使对于非 HTTP 服务也有效。

可以通过 Docker Compose 轻松部署。配置包括设置 API 密钥、审查受信任的代理，以及选择性地启用 FirewallD 集成（需要容器的 root 访问权限）。本文包含有关使用 Caddy 和 FirewallD 设置 Knocker 的详细说明，以及故障排除提示。

该项目包括单元测试和集成测试。可以在配置文件中启用 API 文档端点。该项目是在 AI 的帮助下构建的，不赞成使用 AI 的用户请勿使用它。

---

## 24. 古腾堡计划文学档案馆基金会CEO格雷格·纽比去世

**原文标题**: Greg Newby, CEO of Project Gutenberg Literary Archive Foundation, has died

**原文链接**: [https://www.pgdp.net/wiki/In_Memoriam/gbnewby](https://www.pgdp.net/wiki/In_Memoriam/gbnewby)

本文沉痛宣布古腾堡计划文学档案馆基金会首席执行官格雷戈里·B·纽比博士因罹患癌症，经短暂抗争后不幸逝世。纽比博士担任首席执行官超过20年，同时也是分布式校对者基金会董事会的投票成员，保持着两家机构之间的紧密合作关系。

文章重点介绍了纽比博士对普及文学的热情。1987年收到电子版《爱丽丝梦游仙境》的启发，他认识到电子书的潜力，并全身心投入到古腾堡计划的使命中。他坚信，通过向所有人提供文学作品，产生积极影响至关重要。

在他的领导下，古腾堡计划的电子书藏书增长到超过75,000部，其中许多是由分布式校对者制作的。2023年的一项重大成就是古腾堡计划开放式人工智能旁白有声读物收藏，这是与微软和麻省理工学院合作的项目，被《时代》杂志评为年度最佳发明之一。

文章强调了纽比博士与分布式校对者之间的牢固伙伴关系，并表示他的领导才能和对古腾堡计划的奉献精神将被人们深深怀念。

---

## 25. 龙雏：连接Transformer和脑模型之间的缺失环节

**原文标题**: The Dragon Hatchling: The missing link between the transformer and brain models

**原文链接**: [https://arxiv.org/abs/2509.26507](https://arxiv.org/abs/2509.26507)

本文介绍了“龙雏”（BDH），一种受生物大脑启发的新型大型语言模型架构，旨在弥合Transformer模型与大脑模型之间的差距。BDH利用局部交互的“神经元粒子”的无尺度网络，在保持类Transformer性能的同时，提供理论基础和内在可解释性。

该模型被认为是一种实用且高性能的，基于注意力机制的最先进的状态空间序列学习架构。它可以通过公式在GPU上进行处理，并表现出与Transformer相似的缩放规律，在相同参数大小（1000万到10亿）和训练数据下，其在语言和翻译任务上的性能可与GPT2相媲美。

BDH的一个关键方面是其生物合理性。该模型的工作记忆依赖于具有赫布学习的突触可塑性，表明当模型处理相关概念时，特定突触会得到加强。神经元交互网络具有高度模块化和重尾度分布，表明其可能是人类语音处理的一种机制。

BDH在设计时也考虑到了可解释性。激活向量是稀疏且为正的，并且该模型在语言任务上表现出单义性。可解释性不仅限于神经元和模型参数，还扩展到模型本身的状态。代码和配套博客可供进一步探索。

---

## 26. 特斯拉因电池电力损失风险召回近13000辆电动汽车

**原文标题**: Tesla Recalls Almost 13,000 EVs over Risk of Battery Power Loss

**原文链接**: [https://www.bloomberg.com/news/articles/2025-10-22/tesla-recalls-almost-13-000-evs-over-risk-of-battery-power-loss](https://www.bloomberg.com/news/articles/2025-10-22/tesla-recalls-almost-13-000-evs-over-risk-of-battery-power-loss)

无法访问文章链接。

---

## 27. 走私香烟气球迫使立陶宛机场关闭

**原文标题**: Cigarette-smuggling balloons force closure of Lithuanian airport

**原文链接**: [https://www.theguardian.com/world/2025/oct/22/cigarette-smuggling-balloons-force-closure-vilnius-airport-lithuania](https://www.theguardian.com/world/2025/oct/22/cigarette-smuggling-balloons-force-closure-vilnius-airport-lithuania)

来自白俄罗斯的走私香烟气球迫使立陶宛维尔纽斯机场因安全原因暂时关闭一夜。数十个气球被用来将白俄罗斯香烟运往欧盟，那里的烟草价格更高。立陶宛国家危机管理中心称该事件为“今年最严重的一次”，导致周二晚上11点至周三早上6:30之间的航班停飞。陆地边境口岸也暂时关闭。

立陶宛总理英格丽达·西蒙尼特呼吁白俄罗斯合作，防止未来发生类似事件，强调无论政治关系如何，都需要采取负责任的态度。担忧源于大量气球越境，去年有966个进入，今年已超过500个。

10月5日也发生过类似事件，当时有25个气球进入立陶宛领空。边防部队自去年以来已被授权击落这些气球。邻国波兰今年也经历了100多起类似事件。由于之前发生过疑似俄罗斯无人机从白俄罗斯进入立陶宛领土的事件，这些领空入侵行为尤其敏感。

---

## 28. 鬼火沼泽或可用科学解释

**原文标题**: Ghostly swamp will-O'-the-wisps may be explained by science

**原文链接**: [https://www.snexplores.org/article/swamp-gas-methane-will-o-wisp-chemistry](https://www.snexplores.org/article/swamp-gas-methane-will-o-wisp-chemistry)

对鬼火现象的科学解释探索

---

## 29. rlsw – 少于5千行代码的Raylib软件OpenGL渲染器

**原文标题**: rlsw – Raylib software OpenGL renderer in less than 5k LOC

**原文链接**: [https://github.com/raysan5/raylib/blob/master/src/external/rlsw.h](https://github.com/raysan5/raylib/blob/master/src/external/rlsw.h)

raysan5/raylib的GitHub仓库"rlsw"展示了一个使用Raylib库实现的软件OpenGL渲染器，其代码量少于5000行。标题突出了该项目的核心特性：它是一个软件渲染器（与硬件加速相对），使用OpenGL作为其API，并且实现非常紧凑。在捕获时，该仓库本身似乎遇到了加载错误。尽管如此，提供的信息表明该项目很受欢迎，拥有2.7k个fork和28.8k个star。该项目很可能为理解软件渲染、OpenGL原理和高效代码实现提供了一个宝贵的资源，尤其是在备受推崇的Raylib游戏开发库的背景下。由于现代图形编程中软件渲染器越来越罕见，因此它具有重要意义。

---

## 30. 星云

**原文标题**: Starcloud

**原文链接**: [https://blogs.nvidia.com/blog/starcloud/](https://blogs.nvidia.com/blog/starcloud/)

题为“星云”的文章宣布NVIDIA和谷歌云扩大合作，以加速企业人工智能和工业数字化。该合作的重点是为企业提供更大的加速计算能力，以转变各种企业工作负载，范围从视觉计算到先进人工智能，包括智能体和物理人工智能应用。

具体而言，谷歌云推出了利用NVIDIA硬件和软件的新产品和集成。这可能包括：

*   **访问NVIDIA最新的GPU：**谷歌云可能会向其客户提供访问NVIDIA最先进的GPU的权限，从而为AI模型实现更快的训练和推理。
*   **优化的软件集成：** 预计NVIDIA的软件堆栈（如CUDA、TensorRT等）与谷歌云的AI平台和服务之间将进行集成。 这使得开发人员可以更轻松地在谷歌云上构建和部署AI应用程序。
*   **针对特定行业的解决方案：** 该合作关系可能旨在满足制造业、医疗保健和汽车等行业的需求，在这些行业中，加速计算对于模拟、机器人和实时数据分析等任务至关重要。

本质上，NVIDIA和谷歌云正在共同努力，普及对强大计算资源的访问，从而使企业能够利用人工智能和数字化来推动其运营中的创新和效率。

---

## 31. 美国宇航局局长暗示SpaceX或将被踢出登月任务

**原文标题**: NASA chief suggests SpaceX may be booted from moon mission

**原文链接**: [https://www.cnn.com/2025/10/20/science/nasa-spacex-moon-landing-contract-sean-duffy](https://www.cnn.com/2025/10/20/science/nasa-spacex-moon-landing-contract-sean-duffy)

美国国家航空航天局考虑开放“阿耳忒弥斯III”登月舱合同，可能因SpaceX的星舰开发时间表及其在新太空竞赛中落后于中国的风险担忧而将其搁置。美国国家航空航天局代理局长肖恩·达菲在最近的采访中表达了这些担忧，并表示他打算允许其他公司与SpaceX竞争。

“阿耳忒弥斯III”任务计划于2027年中期进行，旨在自阿波罗计划以来首次将宇航员送回月球。虽然SpaceX目前持有价值29亿美元的登月舱合同，但达菲暗示，已经拥有美国国家航空航天局后续阿耳忒弥斯任务合同的蓝色起源公司有可能接手。他还提到，有可能向其他没有现有合同的公司开放竞争。

美国国家航空航天局已要求SpaceX和蓝色起源在10月29日之前提交“加速方案”，并将向整个商业航天工业发布信息征询书（RFI），以探索增加登月任务频率的方法。该机构强调了在登月方面击败中国的紧迫性，这也是立法者们共同的目标。

专家们对星舰和蓝色月亮的复杂性和时间表表示担忧，特别是对轨道加油的需求。文章指出，信息征询书通常是一个非正式的事实调查过程，而征求建议书（RFP）将是一个更正式的招标。

---

## 32. 分布式光线追踪

**原文标题**: Distributed Ray-Tracing

**原文链接**: [https://www.4rknova.com//blog/2019/02/24/distributed-raytracing](https://www.4rknova.com//blog/2019/02/24/distributed-raytracing)

本文解释了分布式光线追踪，以及它与传统Whitted光线追踪相比如何增强真实感。Whitted光线追踪对每个像素使用单条光线，并对阴影、反射和折射使用有限数量的额外光线，因此难以准确模拟真实世界的光学现象。

分布式光线追踪，也称为随机光线追踪，通过使用蒙特卡洛采样来解决这些限制。它不是依赖于无限小光源的单个、二元阴影查询（导致硬阴影），而是通过向光源上的随机点投射多条阴影光线来模拟任意大小的光源，从而近似计算遮挡概率并创建带有半影的柔和阴影。

这种采样方法也适用于其他效果。通过向镜面反射叶瓣上的随机样本生成多条反射光线来实现光泽反射。通过在薄透镜上分布积分样本来模拟景深。通过在时域中积分样本来产生运动模糊。本质上，分布式光线追踪通过在整个域中的多个点对被积函数进行采样，从而更好地逼近渲染方程。

本文展示了分布式光线追踪的实际应用示例，展示了更柔和的阴影、光泽表面和景深。它还提供了实现景深的薄透镜模型的示例代码，并链接到开源渲染器xtracer，以便进一步探索。

---

## 33. 神经音频编解码器：如何将音频输入大型语言模型

**原文标题**: Neural audio codecs: how to get audio into LLMs

**原文链接**: [https://kyutai.org/next/codec-explainer](https://kyutai.org/next/codec-explainer)

本文探讨了构建有效的语音LLM所面临的挑战，并介绍了神经音频编解码器作为一种解决方案。当前的语音界面依赖于转录，缺乏细微差别和对音频的真正理解。作者认为，由于音频数据的高采样率和时间连贯性要求，直接将文本LLM的成功应用于音频是困难的。

文章详细介绍了一项尝试在原始音频样本上训练语言模型的尝试，结果表现不佳。随后介绍了神经音频编解码器的概念，该编解码器将音频压缩成离散的token，从而使LLM能够更有效地预测延续。

文章使用Fashion MNIST示例来解释向量量化变分自编码器（VQ-VAE），这是一种神经音频编解码器。它演示了如何训练带有量化的自编码器，使用直通估计器解决不可微问题，并添加承诺损失以改善量化。它展示了这如何压缩数据，尽管会损失质量。

最后，文章介绍了残差向量量化（RVQ），它是VQ-VAE的扩展，通过在多个级别量化残差来提高重建保真度。该技术使用多个量化器来表示数据，从而允许更多的可能值，而无需大幅增加计算成本。RVQ迭代地量化来自先前量化级别的误差（残差），从而产生对原始数据的更精细的表示。文章为这些编解码器（包括Kyutai的Mimi编解码器）如何使LLM能够处理音频奠定了基础。

---

## 34. Erowid - 记录人类与精神活性物质之间的复杂关系

**原文标题**: Erowid - Documenting the Complex Relationship Between Humans and Psychoactives

**原文链接**: [https://www.erowid.org](https://www.erowid.org)

无法访问文章链接。

---

## 35. 尼亚加拉瀑布的隐秘工程

**原文标题**: The Hidden Engineering of Niagara Falls

**原文链接**: [https://practical.engineering/blog/2025/10/21/the-hidden-engineering-of-niagara-falls](https://practical.engineering/blog/2025/10/21/the-hidden-engineering-of-niagara-falls)

尼亚加拉瀑布不仅是旅游胜地，也是与航运、发电和水利控制相关的重大工程壮举的中心。瀑布阻碍了伊利湖和安大略湖之间的航运，而韦兰运河克服了这一障碍，这是一条关键的水道，拥有八个船闸来管理高程差。

瀑布高流量和显著高程下降的独特结合使其成为北美大规模水力发电的诞生地。尼亚加拉河的水通过巨大的隧道被引流到发电厂，从而减少了瀑布的流量。这种引流由国际控制坝管理，以平衡旅游业和发电需求。抽水蓄能电站通过储存水并在高峰需求期间释放水来进一步优化发电。

虽然水流的转移减少了瀑布流量的50%，但它也减缓了侵蚀，有助于保护瀑布。美国瀑布甚至在1969年被暂时关闭，以评估和稳定其底部的岩屑（岩石碎片）。

本质上，尼亚加拉瀑布展示了自然奇观和人类工程的交汇，其基础设施旨在利用其力量、促进交通运输和保护其美丽。

---

## 36. 用每月55美元的服务器替代每月3000美元的Heroku账单

**原文标题**: Replacing a $3000/mo Heroku bill with a $55/mo server

**原文链接**: [https://disco.cloud/blog/how-idealistorg-replaced-a-3000mo-heroku-bill-with-a-55-server/](https://disco.cloud/blog/how-idealistorg-replaced-a-3000mo-heroku-bill-with-a-55-server/)

用每月55美元的服务器替换每月3000美元的Heroku账单
        
文章“用每月55美元的服务器替换每月3000美元的Heroku账单”详细介绍了Idealist.org如何通过从Heroku迁移到自管理服务器来显著降低其托管成本。面对每月高达3000美元的Heroku账单，他们寻求更具成本效益的解决方案。

此举可能涉及设置他们自己的基础设施，可能使用AWS、DigitalOcean或Linode等云提供商，甚至专用服务器。 该文章可能概述了采取的步骤，其中包括：

*   **分析Heroku使用情况：** 了解资源消耗以确定所需的服务器规格。
*   **服务器设置和配置：** 安装必要的软件、配置数据库以及设置部署管道。
*   **应用程序迁移：** 将应用程序代码和数据从Heroku迁移到新服务器。
*   **优化：** 调整服务器设置和应用程序代码以获得最佳性能。
*   **持续维护：** 实施监控、安全措施和更新。

主要的结论是，对于具有可预测资源需求和技术专长的项目，与Heroku等PaaS解决方案相比，管理自己的服务器可以带来可观的成本节省，即使这需要更多的初始努力和持续维护。每月55美元的数字突显了大幅降低成本的潜力。

---

## 37. Show HN: Modshim – Python 中一种新的替代猴子补丁的方法

**原文标题**: Show HN: Modshim – A new alternative to monkey-patching in Python

**原文链接**: [https://github.com/joouha/modshim](https://github.com/joouha/modshim)

Modshim：Python中替代猴子补丁、Fork和Vendoring的方案

Modshim是一种干净的替代方案，用于替代Python中的猴子补丁、Fork和Vendoring，它提供了一种增强现有模块的方法，而无需直接修改其源代码。它通过将自定义功能覆盖到原始模块上来创建一个新的“shimmed”模块，在保留其行为的同时引入修改，如错误修复、功能添加或替代实现。

该库通过拦截Python的导入系统来运行，创建一个可在指定“挂载点”下访问的虚拟合并模块。这涉及到定位原始（“下层”）模块和增强（“上层”）模块，按顺序执行它们的代码，并重写抽象语法树（AST），以将这些模块内的内部引用重定向到新的组合模块。

强调的关键优势包括：避免与猴子补丁相关的全局命名空间污染，通过依赖原始库来减少Fork的维护负担，以及与Vendoring相比，保持更清晰的代码分离。文章提供了实际示例，例如向`textwrap.TextWrapper`添加前缀参数，以及向`requests`库添加可配置的重试机制，展示了modshim如何实现模块化增强和内部引用重写。它强调了对原始模块完整性的保护，确保应用程序的其他部分不受修改的影响。Modshim的方法使增强功能保持隔离、可维护，并为潜在的向上游贡献做好准备。

---

## 38. 数学家发现撤销旋转的隐藏“重置按钮”

**原文标题**: Mathematicians have found a hidden 'reset button' for undoing rotation

**原文链接**: [https://www.newscientist.com/article/2499647-mathematicians-have-found-a-hidden-reset-button-for-undoing-rotation/](https://www.newscientist.com/article/2499647-mathematicians-have-found-a-hidden-reset-button-for-undoing-rotation/)

数学家发现还原物体旋转的通用“重置按钮”

数学家让-皮埃尔·埃克曼和茨维·特拉斯蒂发现了一种通用的“重置按钮”，可以撤销几乎任何物体的旋转。他们的办法不是费力地逆转每一次单独的旋转，而是将初始旋转按一个通用系数缩放并重复两次。

该原理适用于旋转陀螺、量子比特、陀螺仪和机械臂等物体，使其在经过一系列复杂的旋转后能够返回到原始位置。该发现根植于数学空间SO(3)，它记录了三维空间中所有可能的旋转。撤销旋转就像找到一条回到这个空间中心的路径，这很困难。埃克曼和特拉斯蒂意识到，找到一条通往空间*表面*的路径（撤销旋转的中途点）要容易得多。

他们的证明依赖于19世纪的罗德里格斯公式和1889年的一条数论定理。重置所需的缩放因子几乎总是存在的。

这项研究展示了数学在旋转研究中的丰富性，并可能在核磁共振（NMR）和机器人等领域具有实际应用。在NMR/MRI中，它可以帮助撤销不需要的自旋旋转。在机器人领域，它可以使滚动机器人能够使用可靠的“滚动-重置-滚动”运动来遵循重复路径，甚至允许机器人通过改变形状来进行导航。

---

## 39. 评估Argon2在实际软件中的应用与有效性

**原文标题**: Evaluating Argon2 adoption and effectiveness in real-world software

**原文链接**: [https://arxiv.org/abs/2504.17121](https://arxiv.org/abs/2504.17121)

Tippe和Berner的论文《评估Argon2在实际软件中的采纳和有效性》研究了Argon2密码哈希算法在真实世界中的安全性。它将攻击模拟与Argon2在公共GitHub存储库中的部署的实证研究相结合。

该研究量化了不同Argon2参数配置在现实攻击预算下对密码猜测成本的影响。该经济模型通过加密货币挖掘基准验证，表明OWASP推荐的46 MiB配置比SHA-256显著提高了安全性。然而，该研究表明，随着内存分配增加到RFC 9106的2048 MiB，收益递减。一个关键发现是，无论配置如何，Argon2都难以防御弱密码和常用密码，例如RockYou数据集中发现的密码。

对GitHub存储库的分析表明，Argon2的采用率不断增长，但其实现存在令人担忧的弱点。高达46.6%的部署使用了弱于OWASP推荐的参数。令人惊讶的是，像密码管理器和加密工具这样的敏感应用程序并没有表现出比通用软件更强的Argon2配置。

作者得出结论，仅仅采用安全的算法不足以实现强大的密码安全性。有效的参数指导和开发者教育对于发挥Argon2的潜力并减轻与弱密码和不正确配置相关的风险至关重要。该论文强调了Argon2的理论安全性与其在实际软件中的实际实现之间存在脱节。

---

## 40. 民主与开放的互联网在光天化日之下消亡

**原文标题**: Democracy and the open internet die in daylight

**原文链接**: [https://heatherburns.tech/2025/10/22/democracy-and-the-open-internet-die-in-daylight/](https://heatherburns.tech/2025/10/22/democracy-and-the-open-internet-die-in-daylight/)

英国科技政策专家Heather Burns对《华盛顿邮报》最近的一项举措表示担忧。她指出，该报正提供免费访问其文章的权限，以换取下载PerplexityAI的Comet浏览器，该浏览器是围绕代理AI构建的。Burns认为这尤其令人不安，将其比作20世纪90年代过时的、限制性的做法，即内容访问取决于使用特定的浏览器。

她认为此举可能是新闻业融资模式的转变，从广告技术转向代理AI。虽然她承认广告技术模式的缺点，认为它导致了新闻业的现状，但Burns强烈反对用另一种侵犯隐私的技术取代它。她认为这是对机会的虚假承诺，本质上是用一种形式的隐私侵犯换取另一种。

Burns的担忧源于她对基于人权、隐私、可访问性和言论自由的开放网络的承诺。她担心《华盛顿邮报》和PerplexityAI之间的这种合作可能会进一步损害这些价值观。作者的总体基调是警惕和失望，表明这一发展标志着朝着侵蚀民主和开放互联网迈出了重要一步。

---

## 41. 通过Claude代码暴力破解，使DeepSeek-OCR在Nvidia Spark上运行

**原文标题**: Getting DeepSeek-OCR working on an Nvidia Spark via brute force with Claude Code

**原文链接**: [https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/](https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/)

Simon Willison 成功利用 Anthropic 的 Claude Code 在 NVIDIA Spark 设备上运行了 DeepSeek-OCR，这是一款新的 PyTorch CUDA OCR 模型。他本质上是将这项复杂的任务外包给了 Docker 沙箱内的 Claude，并赋予其访问相关代码仓库和一个用于 OCR 的示例图片的权限。

整个过程大约花费了 40 分钟，Willison 本人几乎没有直接参与。Claude Code 克服了在 NVIDIA ARM 架构上运行带有 CUDA 的 PyTorch 所面临的挑战，包括不兼容的 PyTorch 版本。它识别并安装了兼容的 ARM CUDA wheels，解决了 CUDA 错误，并最终成功运行了该模型。

Claude 还尝试了不同的 OCR 提示词，并记录了它的发现，包括速度、文本质量、结构以及每种提示词的最佳使用案例的比较。在整个过程中，它在 `notes.md` 文件中生成了全面的笔记，以及详细的 README 文件和脚本，供将来使用。

主要经验包括使用类似 Docker 的沙箱环境和完整权限的代理循环进行自动化问题解决的有效性，以及向 AI 代理提供清晰的目标和资源的重要性。Willison 还强调了当 Claude 遇到阻碍时，他自身专业知识在引导 Claude 方面的价值。他还利用 VS Code 的 Remote SSH 和 Dev Containers 扩展来实时监控 Docker 容器的文件系统。该项目展示了 DeepSeek-OCR 的潜力，并提供了一种在类似硬件上运行该模型的可复现方法。

---

## 42. 捷豹路虎遭黑客攻击，致英国经济损失约25亿美元

**原文标题**: Jaguar Land Rover hack cost UK economy an estimated $2.5B

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/jaguar-land-rover-hack-cost-uk-economy-25-billion-report-says-2025-10-22/](https://www.reuters.com/sustainability/boards-policy-regulation/jaguar-land-rover-hack-cost-uk-economy-25-billion-report-says-2025-10-22/)

**摘要：**

据路透社援引的一份报告，2024年初对捷豹路虎（JLR）的网络攻击给英国经济造成了约25亿美元的损失。该报告可能由网络安全公司或相关组织委托编写，强调了此次事件对经济造成的重大影响，远超捷豹路虎的直接损失。

虽然本摘要版本并未详尽概述此次攻击的具体细节，但报告表明，损失源于生产中断、声誉受损导致销量下降、供应链中断，以及事件响应、补救和法律后果相关的成本。据报道，此次攻击针对捷豹路虎的运营，可能泄露了知识产权和客户数据。

该报告强调了大型制造商在网络攻击面前的脆弱性，并强调此类事件可能对国家经济产生的连锁反应。它提醒人们，强大的网络安全措施和积极主动的风险管理策略对企业（尤其是那些涉及汽车制造等关键领域的企业）来说日益重要。25亿美元的数字非常可观，突显了对一家英国大型公司成功的网络攻击可能造成的潜在经济损失规模。

---

## 43. 停滞的秩序：以及崛起大国的终结

**原文标题**: The Stagnant Order. and the End of Rising Powers

**原文链接**: [https://www.foreignaffairs.com/united-states/stagnant-order-michael-beckley](https://www.foreignaffairs.com/united-states/stagnant-order-michael-beckley)

迈克尔·贝克利的《停滞的秩序和崛起大国的终结》认为，快速崛起的全球大国时代——工业时代的标志——正在走向终结。 这一转变的关键驱动因素是生产力下降、人口萎缩以及征服的难度增加和回报减少。

历史上，英国、德国和美国等崛起大国得益于工业革命带来的前所未有的生产力提高、人口增长和军事力量增强。 然而，当前的技术进步尚未重现过去的变革性影响，生产力增长已经停滞。 人口下降普遍存在，大多数工业化国家的出生率都低于更替水平。 此外，技术和核武器的扩散使征服的风险更高，利润更低。

中国是最后一个主要的崛起大国，但已经达到了顶峰，而日本、俄罗斯、欧洲和印度等其他潜在竞争者也面临着各自的局限性。 美国虽然面临挑战，但其表现优于正在经历更深层次衰退的竞争对手。

这一转变的后果是深远的。 虽然权力过渡的减少最终可能会降低崛起大国寻求资源和地位而引发大规模冲突的可能性，但眼前的后果却带来了危险。 脆弱国家在债务和青年人口膨胀中挣扎，而衰落的大国可能会诉诸军事化和收复失地主义。 经济不安全感助长了极端主义，侵蚀了民主制度，并可能导致主要大国采取单边主义行动。 文章的结论是，崛起大国时代的终结并不能保证一个更加和平的世界。

---

## 44. ChatGPT 地图集

**原文标题**: ChatGPT Atlas

**原文链接**: [https://chatgpt.com/atlas](https://chatgpt.com/atlas)

无法访问文章链接。

---

## 45. 研究人员完成首个人体肠内通气可行性试验

**原文标题**: Researchers complete first human trial on viability of enteral ventilation

**原文链接**: [https://newatlas.com/disease/butt-breathing-ignobel-prize/](https://newatlas.com/disease/butt-breathing-ignobel-prize/)

研究人员已完成首次人体肠道通气试验，该技术旨在通过肠道向身体输送氧气，为严重呼吸衰竭患者提供潜在替代方案。这项由辛辛那提儿童医院领导的研究，紧随科学家们此前因证明某些哺乳动物可以通过肛门呼吸而获得的搞笑诺贝尔奖之后。

该试验的重点是评估该程序的安全性和耐受性。在日本，27名健康的男性志愿者接受了单次直肠内剂量的无氧全氟癸烷液体，这是一种以其携氧能力而闻名的物质，并被指示保持液体60分钟。结果表明，该程序安全且耐受性良好，仅在最大剂量1500毫升时出现轻微的腹胀和不适副作用。所有临床实验室指标均保持在正常范围内。

这项首次人体研究为未来的研究奠定了关键的安全基础。科学家们现在计划进行进一步的试验，以确定有效提高血氧水平的最佳剂量和持续时间。这项技术受到通过肠道吸收氧气的底栖鱼类的启发，有望成为因气道阻塞或肺功能受损的人的救生急救治疗方法。

---

## 46. 每核线程的终结

**原文标题**: The death of thread per core

**原文链接**: [https://buttondown.com/jaffray/archive/the-death-of-thread-per-core/](https://buttondown.com/jaffray/archive/the-death-of-thread-per-core/)

贾斯汀·贾弗雷的文章《每核线程之死》探讨了并发模型的转变，尤其是在数据处理领域。其核心论点是，传统的“每核线程”方法——优先考虑数据局部性和减少跨核心通信——正面临挑战，“工作窃取”模型可能再次兴起。

文章强调了数据分布相对均匀时每核线程的优势。然而，它指出该模型在处理倾斜数据时会遇到困难，并且随着核心数量的增加，问题会变得越来越严重。工作窃取（空闲线程可以从繁忙线程“窃取”任务）为解决不均衡的工作负载和提高整体CPU利用率提供了一种方案。

反对每核线程的关键论点包括：

*   **核心数量增加：**在具有更多核心的机器上，倾斜的数据分布会受到更严重的影响。
*   **IO延迟的改善：**由于磁盘速度等其他领域的改进，最大限度地提高CPU利用率的理由变得更加重要。
*   **对数据处理的洞察：** 与通用编程相比，数据处理允许对数据需求和任务操作进行更具预测性的内省。
*   **文化转变：** 随着数据系统的扩展，处理倾斜变得必然，使得“在上层解决倾斜问题”成为一种不充分的策略。

最终，文章认为，每核线程和工作窃取之间的选择取决于具体的应用程序和数据特性。然而，它认为，倾斜数据的日益普遍和大规模数据系统中对弹性的日益增长的需求，正在推动人们对工作窃取和共享状态并发模型重新产生兴趣，从而摆脱严格的每核线程范例。

---

## 47. 我们应该担心人工智能的循环交易吗？

**原文标题**: Should we worry about AI's circular deals?

**原文链接**: [https://www.noahpinion.blog/p/should-we-worry-about-ais-circular](https://www.noahpinion.blog/p/should-we-worry-about-ais-circular)

诺亚·史密斯的文章探讨了人工智能行业中围绕“循环交易”的担忧，即人工智能公司互相投资，引发了对即将崩溃的恐惧。这些交易通常涉及像英伟达这样的芯片制造商投资像OpenAI这样的人工智能模型开发商，然后后者利用这些资金购买芯片制造商的硬件，从而形成一个闭环。

主要的担忧有两方面：首先，这些交易人为地抬高了收入，误导投资者并造成不可持续的估值；其次，它们通过使所有相关公司的命运相互依存来增加系统性风险。史密斯认为，这些交易更像是“供应商融资”（如通用汽车向汽车购买者贷款），而不是互联网泡沫时代常见的非法“循环交易”。他认为，收入是单向流动的，相关公司正受到严密审查，而且英伟达的股价在OpenAI交易后并没有显著上涨。

然而，他承认相互依存的风险增加。虽然普遍的人工智能崩溃会摧毁所有这些公司，但这些交易使它们的命运更加紧密地联系在一起。史密斯认为，这些交易可能是人工智能公司分散其依赖性并降低风险的一种方式，从而避免依赖少数主要客户。本质上，他总结说，这些循环交易是押注人工智能潜力的更大赌注的一部分，导致一个更容易受到人工智能崩溃影响，但不太容易受到特定人工智能公司失败影响的系统。

---

## 48. GitHub 正在开发堆叠式差异。

**原文标题**: GitHub is working on stacked diffs

**原文链接**: [https://twitter.com/jaredpalmer/status/1980619222918262842](https://twitter.com/jaredpalmer/status/1980619222918262842)

这并非关于GitHub开发堆叠式差异的文章。这是一个占位符页面，表明用户尝试访问X（前身为Twitter）时，其浏览器已禁用JavaScript。该页面指示用户启用JavaScript或切换到受支持的浏览器，并提供X帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接。版权声明表明该页面属于X Corp.，版权所有年份为2025年。标题具有误导性，内容不相关。其中没有关于GitHub或堆叠式差异的信息。

---

## 49. 阿根廷比索再创新低，尽管有美国支持——情况可能更糟

**原文标题**: Argentine peso hits fresh lows despite U.S. support – and it could get worse

**原文链接**: [https://www.cnbc.com/2025/10/22/argentine-peso-at-fresh-lows-despite-us-purchases.html](https://www.cnbc.com/2025/10/22/argentine-peso-at-fresh-lows-despite-us-purchases.html)

尽管美国提供了包括购买美元和200亿美元货币互换在内的支持方案，但由于中期选举前政治局势不明朗，阿根廷比索持续跌至新低。自美国干预以来，比索已贬值超过5%。

专家认为，比索疲软的主要原因是人们预期庇隆主义（左翼）政党将表现强劲，这些政党历来倾向于导致通货膨胀和对比索不信任的政策。 虽然美国的支持缓解了局势，但在选举不确定性的情况下，可能无法完全抵消市场压力。

财政部长斯科特·贝森特强调了阿根廷改革的“系统重要性”，并强调了该国“严重的流动性不足”，导致了美国的干预。 古斯塔沃·梅代罗斯指出了阿根廷的流动性问题以及支持方案的重要性，尤其是在阿根廷试图通过以折扣价回购债券来减少债务之际。 然而，比索持续贬值表明，政治担忧超过了美国财政援助的影响。

---

## 50. OpenBSD 7.8

**原文标题**: OpenBSD 7.8

**原文链接**: [https://cdn.openbsd.org/pub/OpenBSD/7.8/ANNOUNCEMENT](https://cdn.openbsd.org/pub/OpenBSD/7.8/ANNOUNCEMENT)

OpenBSD 7.8 发布，带来诸多改进和新特性

OpenBSD 7.8 于 2025 年 10 月 22 日发布，标志着该操作系统第 59 次发布，该操作系统以其强大的安全记录而闻名。此版本带来了整个系统的众多改进和新特性。

关键的平台特定更新包括 Raspberry Pi 5 支持和 arm64 的 acpicpu(4) 实现，以及 amd64 上 AMD CPU 电源管理的修复。内核改进包括更好的错误报告、POSIX-2024 close-on-fork 标志实现（为安全而修改）、改进的锁处理、新的高级软件中断分发器，以及移动到纳秒睡眠时间参数以获得更好的精度。现在支持 AMD SEV-ES 来宾模式，并启用了 CPU xcall。

Suspend/hibernate 支持得到了增强，修复了各种设备的问题，SMP 改进包括并行 TCP 栈和 IPv6 处理。图形驱动程序更新到 Linux 6.12.50，并为高通 Snapdragon 增加了一个新的 qcdrm(4) 驱动程序。VMM/VMD 支持 AMD SEV-ES 机密虚拟机，以及各种安全和内存管理增强功能。

Userland 更新包括 pkgconf 替换用于 pkg-config(1) 的 Perl 脚本，添加 watch(1) 实用程序，以及通过 security(8) 进行 GPT/MBR 备份和通过 fdisk(8) 进行恢复。fdisk(8) 获得了改进的交互式编辑器。分析使用新的 gprof 系统进行了更新。整个 userland 实用程序进行了大量的错误修复和文档改进。

硬件支持通过 Raspberry Pi 外围设备、华硕 I2C HID 键盘和 Realtek RTL8125D/8127 以太网芯片等各种设备的驱动程序得到扩展。无线驱动程序在 qwx(4)、bwfm(4) 和 iwx(4) 中得到了改进。安装程序的改进包括磁盘首选项和防止损坏 /bsd 安装。安全增强功能包括扩展的 pledge 权限以及 PCB 和内核堆栈之间的未映射保护页。网络栈获得了对 TCP 的软 LRO 支持和一个新的 erspan(4) 驱动程序。pf(4) 防火墙和路由守护程序也收到了错误修复和改进。

---

## 51. 20,858部公共版权领域有声书

**原文标题**: 20,858 Public Domain Audio Books

**原文链接**: [https://librivox.org/search](https://librivox.org/search)

This LibriVox webpage advertises a catalog of 20,858 public domain audiobooks available for browsing. Users can utilize an advanced search function, filling in specific fields and options to refine their search. The catalog includes audiobooks recorded by individuals (solo) and groups. The page also encourages users to donate to LibriVox and thank the volunteer readers.

A crucial disclaimer emphasizes that LibriVox recordings are in the public domain in the USA. However, users outside the US are responsible for verifying the copyright status of the audiobooks in their own country to ensure they are not violating copyright laws before downloading.

The catalog can be ordered alphabetically or by release date, offering users flexibility in how they browse the available titles.


---

## 52. Minds, brains, and programs (1980) [pdf]

**原文标题**: Minds, brains, and programs (1980) [pdf]

**原文链接**: [https://home.csulb.edu/~cwallis/382/readings/482/searle.minds.brains.programs.bbs.1980.pdf](https://home.csulb.edu/~cwallis/382/readings/482/searle.minds.brains.programs.bbs.1980.pdf)

生成摘要时出错

---

## 53. Our modular, high-performance Merkle Tree library for Rust

**原文标题**: Our modular, high-performance Merkle Tree library for Rust

**原文链接**: [https://github.com/bilinearlabs/rs-merkle-tree](https://github.com/bilinearlabs/rs-merkle-tree)

生成摘要时出错

---

## 54. Principles and Methodologies for Serial Performance Optimization

**原文标题**: Principles and Methodologies for Serial Performance Optimization

**原文链接**: [https://danglingpointers.substack.com/p/principles-and-methodologies-for](https://danglingpointers.substack.com/p/principles-and-methodologies-for)

生成摘要时出错

---

## 55. Bare Metal (The Emacs Essay)

**原文标题**: Bare Metal (The Emacs Essay)

**原文链接**: [https://waxbanks.wordpress.com/2025/08/01/bare-metal-the-emacs-essay/](https://waxbanks.wordpress.com/2025/08/01/bare-metal-the-emacs-essay/)

生成摘要时出错

---

## 56. Wikipedia says traffic is falling due to AI search summaries and social video

**原文标题**: Wikipedia says traffic is falling due to AI search summaries and social video

**原文链接**: [https://techcrunch.com/2025/10/18/wikipedia-says-traffic-is-falling-due-to-ai-search-summaries-and-social-video/](https://techcrunch.com/2025/10/18/wikipedia-says-traffic-is-falling-due-to-ai-search-summaries-and-social-video/)

生成摘要时出错

---

## 57. Foreign hackers breached a US nuclear weapons plant via SharePoint flaws

**原文标题**: Foreign hackers breached a US nuclear weapons plant via SharePoint flaws

**原文链接**: [https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html](https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html)

生成摘要时出错

---

## 58. iPhone 17 Pro Camera Review: Dolomites – Travel Photographer – Austin Mann

**原文标题**: iPhone 17 Pro Camera Review: Dolomites – Travel Photographer – Austin Mann

**原文链接**: [https://www.austinmann.com/trek/iphone-17-pro-camera-review-dolomites](https://www.austinmann.com/trek/iphone-17-pro-camera-review-dolomites)

生成摘要时出错

---

## 59. Diamond Thermal Conductivity: A New Era in Chip Cooling

**原文标题**: Diamond Thermal Conductivity: A New Era in Chip Cooling

**原文链接**: [https://spectrum.ieee.org/diamond-thermal-conductivity](https://spectrum.ieee.org/diamond-thermal-conductivity)

生成摘要时出错

---

## 60. Ilo – a Forth system running on UEFI

**原文标题**: Ilo – a Forth system running on UEFI

**原文链接**: [https://asciinema.org/a/Lbxa2w9R5IbaJqW3INqVrbX8E](https://asciinema.org/a/Lbxa2w9R5IbaJqW3INqVrbX8E)

生成摘要时出错

---

## 61. Language Support for Marginalia Search

**原文标题**: Language Support for Marginalia Search

**原文链接**: [https://www.marginalia.nu/log/a_126_multilingual/](https://www.marginalia.nu/log/a_126_multilingual/)

生成摘要时出错

---

## 62. LLMs can get "brain rot"

**原文标题**: LLMs can get "brain rot"

**原文链接**: [https://llm-brain-rot.github.io/](https://llm-brain-rot.github.io/)

生成摘要时出错

---

## 63. The Gypsy Life of Robert Louis Stevenson

**原文标题**: The Gypsy Life of Robert Louis Stevenson

**原文链接**: [https://hudsonreview.com/2025/10/the-gypsy-life-of-robert-louis-stevenson/](https://hudsonreview.com/2025/10/the-gypsy-life-of-robert-louis-stevenson/)

生成摘要时出错

---

## 64. iPhone 17 Pro Camera Review: Dolomites – Travel Photographer – Austin Mann

**原文标题**: iPhone 17 Pro Camera Review: Dolomites – Travel Photographer – Austin Mann

**原文链接**: [https://www.austinmann.com/trek/iphone-17-pro-camera-review-dolomites](https://www.austinmann.com/trek/iphone-17-pro-camera-review-dolomites)

生成摘要时出错

---

## 65. Understanding conflict resolution and avoidance in PostgreSQL: a complete guide

**原文标题**: Understanding conflict resolution and avoidance in PostgreSQL: a complete guide

**原文链接**: [https://www.pgedge.com/blog/living-on-the-edge](https://www.pgedge.com/blog/living-on-the-edge)

生成摘要时出错

---

## 66. Weekend projects: Chicken Squisher 3000

**原文标题**: Weekend projects: Chicken Squisher 3000

**原文链接**: [https://lcamtuf.substack.com/p/weekend-projects-chicken-squisher](https://lcamtuf.substack.com/p/weekend-projects-chicken-squisher)

生成摘要时出错

---

## 67. Meta Plans to Cut 600 Jobs at A.I. Superintelligence Labs

**原文标题**: Meta Plans to Cut 600 Jobs at A.I. Superintelligence Labs

**原文链接**: [https://www.nytimes.com/2025/10/22/technology/meta-plans-to-cut-600-jobs-at-ai-superintelligence-labs.html](https://www.nytimes.com/2025/10/22/technology/meta-plans-to-cut-600-jobs-at-ai-superintelligence-labs.html)

生成摘要时出错

---

## 68. Is Vibe Coding Dying?

**原文标题**: Is Vibe Coding Dying?

**原文链接**: [https://garymarcus.substack.com/p/is-vibe-coding-dying](https://garymarcus.substack.com/p/is-vibe-coding-dying)

生成摘要时出错

---

## 69. Subprime Lender PrimaLend Enters Bankruptcy After Bond Default

**原文标题**: Subprime Lender PrimaLend Enters Bankruptcy After Bond Default

**原文链接**: [https://www.bloomberg.com/news/articles/2025-10-22/subprime-lender-primalend-enters-bankruptcy-after-bond-default](https://www.bloomberg.com/news/articles/2025-10-22/subprime-lender-primalend-enters-bankruptcy-after-bond-default)

生成摘要时出错

---

## 70. Do not accept terms and conditions

**原文标题**: Do not accept terms and conditions

**原文链接**: [https://www.termsandconditions.game/](https://www.termsandconditions.game/)

生成摘要时出错

---

## 71. Show HN: Run any GitHub Action locally from your Cron job -- finally!

**原文标题**: Show HN: Run any GitHub Action locally from your Cron job -- finally!

**原文链接**: [https://docs.dagu.io/features/executors/github-actions#basic-usage](https://docs.dagu.io/features/executors/github-actions#basic-usage)

生成摘要时出错

---

## 72. South Africa's one million invisible children without birth certificates

**原文标题**: South Africa's one million invisible children without birth certificates

**原文链接**: [https://www.france24.com/en/africa/20250705-south-africa-s-one-million-invisible-children-without-birth-certificates](https://www.france24.com/en/africa/20250705-south-africa-s-one-million-invisible-children-without-birth-certificates)

生成摘要时出错

---

## 73. Show HN: bbcli – A TUI and CLI to browse BBC News like a hacker

**原文标题**: Show HN: bbcli – A TUI and CLI to browse BBC News like a hacker

**原文链接**: [https://github.com/hako/bbcli](https://github.com/hako/bbcli)

生成摘要时出错

---

## 74. Doomsday scoreboard

**原文标题**: Doomsday scoreboard

**原文链接**: [https://doomsday.march1studios.com/](https://doomsday.march1studios.com/)

生成摘要时出错

---

## 75. Space Elevator

**原文标题**: Space Elevator

**原文链接**: [https://neal.fun/space-elevator/](https://neal.fun/space-elevator/)

生成摘要时出错

---

## 76. Pasta/80 is a simple Pascal cross compiler targeting the Z80 microprocessor

**原文标题**: Pasta/80 is a simple Pascal cross compiler targeting the Z80 microprocessor

**原文链接**: [https://github.com/pleumann/pasta80](https://github.com/pleumann/pasta80)

生成摘要时出错

---

## 77. 60k kids have avoided peanut allergies due to 2015 advice, study finds

**原文标题**: 60k kids have avoided peanut allergies due to 2015 advice, study finds

**原文链接**: [https://www.cbsnews.com/news/peanut-allergies-60000-kids-avoided-2015-advice/](https://www.cbsnews.com/news/peanut-allergies-60000-kids-avoided-2015-advice/)

生成摘要时出错

---

## 78. Show HN: ASCII Automata

**原文标题**: Show HN: ASCII Automata

**原文链接**: [https://hlnet.neocities.org/ascii-automata/](https://hlnet.neocities.org/ascii-automata/)

生成摘要时出错

---

## 79. StarGrid: A new Palm OS strategy game

**原文标题**: StarGrid: A new Palm OS strategy game

**原文链接**: [https://quarters.captaintouch.com/blog/posts/2025-10-21-stargrid-has-arrived,-a-brand-new-palm-os-strategy-game-in-2025.html](https://quarters.captaintouch.com/blog/posts/2025-10-21-stargrid-has-arrived,-a-brand-new-palm-os-strategy-game-in-2025.html)

生成摘要时出错

---

## 80. The Programmer Identity Crisis

**原文标题**: The Programmer Identity Crisis

**原文链接**: [https://hojberg.xyz/the-programmer-identity-crisis/](https://hojberg.xyz/the-programmer-identity-crisis/)

生成摘要时出错

---

## 81. Practical Scheme

**原文标题**: Practical Scheme

**原文链接**: [https://practical-scheme.net/index.html#docs](https://practical-scheme.net/index.html#docs)

生成摘要时出错

---

## 82. Show HN: AutoLearn Skills for self-improving agents

**原文标题**: Show HN: AutoLearn Skills for self-improving agents

**原文链接**: [https://www.autolearn.dev](https://www.autolearn.dev)

生成摘要时出错

---

## 83. You Cannot Outsource Understanding

**原文标题**: You Cannot Outsource Understanding

**原文链接**: [https://russmiles.substack.com/p/you-cannot-outsource-understanding](https://russmiles.substack.com/p/you-cannot-outsource-understanding)

生成摘要时出错

---

## 84. Meta Cutting 600 AI Jobs to move faster

**原文标题**: Meta Cutting 600 AI Jobs to move faster

**原文链接**: [https://www.bloomberg.com/news/articles/2025-10-22/meta-cutting-roughly-600-ai-jobs-as-company-aims-to-move-faster](https://www.bloomberg.com/news/articles/2025-10-22/meta-cutting-roughly-600-ai-jobs-as-company-aims-to-move-faster)

生成摘要时出错

---

## 85. Binary Retrieval-Augmented Reward Mitigates Hallucinations

**原文标题**: Binary Retrieval-Augmented Reward Mitigates Hallucinations

**原文链接**: [https://arxiv.org/abs/2510.17733](https://arxiv.org/abs/2510.17733)

生成摘要时出错

---

## 86. What do we do if SETI is successful?

**原文标题**: What do we do if SETI is successful?

**原文链接**: [https://www.universetoday.com/articles/what-do-we-do-if-seti-is-successful](https://www.universetoday.com/articles/what-do-we-do-if-seti-is-successful)

生成摘要时出错

---

## 87. Public trust demands open-source voting systems

**原文标题**: Public trust demands open-source voting systems

**原文链接**: [https://www.voting.works/news/public-trust-demands-open-source-voting-systems](https://www.voting.works/news/public-trust-demands-open-source-voting-systems)

生成摘要时出错

---

## 88. KDE Connect: Enabling communication between all your devices

**原文标题**: KDE Connect: Enabling communication between all your devices

**原文链接**: [https://community.kde.org/KDEConnect](https://community.kde.org/KDEConnect)

生成摘要时出错

---

## 89. Peanut allergies have plummeted in children

**原文标题**: Peanut allergies have plummeted in children

**原文链接**: [https://www.nytimes.com/2025/10/20/well/peanut-allergy-drop.html](https://www.nytimes.com/2025/10/20/well/peanut-allergy-drop.html)

生成摘要时出错

---

## 90. Why companies are lying about mass layoffs

**原文标题**: Why companies are lying about mass layoffs

**原文链接**: [https://www.youtube.com/watch?v=VEA7vQKJ8aQ](https://www.youtube.com/watch?v=VEA7vQKJ8aQ)

生成摘要时出错

---

## 91. Quantum dynamics on your laptop? New technique moves us closer

**原文标题**: Quantum dynamics on your laptop? New technique moves us closer

**原文链接**: [https://www.buffalo.edu/news/releases/2025/10/quantum-dynamics-on-your-laptop.html](https://www.buffalo.edu/news/releases/2025/10/quantum-dynamics-on-your-laptop.html)

生成摘要时出错

---

## 92. Apple alerts exploit developer that his iPhone was targeted with gov spyware

**原文标题**: Apple alerts exploit developer that his iPhone was targeted with gov spyware

**原文链接**: [https://techcrunch.com/2025/10/21/apple-alerts-exploit-developer-that-his-iphone-was-targeted-with-government-spyware/](https://techcrunch.com/2025/10/21/apple-alerts-exploit-developer-that-his-iphone-was-targeted-with-government-spyware/)

生成摘要时出错

---

## 93. If you'd built a "tool" that stupid, why would you advertise the fact?

**原文标题**: If you'd built a "tool" that stupid, why would you advertise the fact?

**原文链接**: [https://svpow.com/2025/10/13/if-youd-built-a-tool-that-stupid-why-would-you-advertise-the-fact/](https://svpow.com/2025/10/13/if-youd-built-a-tool-that-stupid-why-would-you-advertise-the-fact/)

生成摘要时出错

---

## 94. Workers and Employers Face Higher Health Insurance Costs

**原文标题**: Workers and Employers Face Higher Health Insurance Costs

**原文链接**: [https://www.nytimes.com/2025/10/22/health/health-insurance-costs-2025.html](https://www.nytimes.com/2025/10/22/health/health-insurance-costs-2025.html)

生成摘要时出错

---

## 95. DeepSeek OCR

**原文标题**: DeepSeek OCR

**原文链接**: [https://github.com/deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)

生成摘要时出错

---

## 96. The Salt and Pepper Shaker Museum

**原文标题**: The Salt and Pepper Shaker Museum

**原文链接**: [https://www.thesaltandpeppershakermuseum.com](https://www.thesaltandpeppershakermuseum.com)

生成摘要时出错

---

## 97. Sentence Transformers is joining Hugging Face

**原文标题**: Sentence Transformers is joining Hugging Face

**原文链接**: [https://huggingface.co/blog/sentence-transformers-joins-hf](https://huggingface.co/blog/sentence-transformers-joins-hf)

生成摘要时出错

---

## 98. A laser pointer at 2B FPS [video]

**原文标题**: A laser pointer at 2B FPS [video]

**原文链接**: [https://www.youtube.com/watch?v=o4TdHrMi6do](https://www.youtube.com/watch?v=o4TdHrMi6do)

生成摘要时出错

---

## 99. The Greatness of Text Adventures

**原文标题**: The Greatness of Text Adventures

**原文链接**: [https://entropicthoughts.com/the-greatness-of-text-adventures](https://entropicthoughts.com/the-greatness-of-text-adventures)

生成摘要时出错

---

## 100. Meta overhauls legacy AI operations

**原文标题**: Meta overhauls legacy AI operations

**原文链接**: [https://www.axios.com/2025/10/22/meta-superintelligence-tbd-ai-reorg](https://www.axios.com/2025/10/22/meta-superintelligence-tbd-ai-reorg)

生成摘要时出错

---

