# Hacker News 热门文章摘要 (2025-06-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 编写玩具软件是一种乐趣

**原文标题**: Writing toy software is a joy

**原文链接**: [https://blog.jsbarretto.com/post/software-is-joy](https://blog.jsbarretto.com/post/software-is-joy)

约书亚·巴雷托的文章倡导创建“玩具程序”，认为这对软件开发者来说是一项有价值且能带来乐趣的学习活动。他认为，尽管人工智能兴起和软件开发日益商品化，但构建简化的个人项目，以重新发现编码的乐趣并加深理解，仍具有巨大的益处。

其核心原则是“创造以理解”，强调构建自己简陋的复杂系统版本（例如正则表达式引擎或操作系统内核）比单纯地研究它们能提供更深刻的见解。这些玩具程序旨在遵循80/20法则，专注于核心功能，同时积极避免过度设计。

除了固有的学习之外，作者还强调了意想不到的实际好处，即从这些项目中获得的知识经常在专业环境中证明是有价值的。他提供了一份建议的玩具程序清单，按难度和时间投入进行分级，范围从简单的正则表达式引擎到更具雄心的编译器或操作系统内核。这些建议涵盖了各种领域，包括模拟器、游戏开发、解释器和图形渲染。

巴雷托告诫不要依赖大型语言模型来完成这些项目，而是提倡亲身探索和发现。他强调，学习的乐趣在于克服挑战和开发独特的解决方案，而不是仅仅接收预先打包的答案。文章最后呼吁拥抱焦油坑，承认潜在的挫折，但强调了从头开始构建和理解某些东西所带来的令人欣慰的“跑步者高峰”体验。

---

## 2. 在Power Mac G3 ROM中发现一个27年前的彩蛋

**原文标题**: Finding a 27-year-old easter egg in the Power Mac G3 ROM

**原文链接**: [https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)

道格·布朗详细描述了他对 Power Mac G3 ROM 中一个先前未被记录的彩蛋的发现。在使用 Hex Fiend 和 Eric Harmon 的 ROM Fiend 模板检查 ROM 时，他发现了 Apple 员工的 JPEG 图像（资源类型为 HPOE）以及 SCSI Manager 4.3 代码中的 Pascal 字符串（nitt 资源 ID 为 43），特别是“.Edisk”和“secret ROM image”。

由于对“secret ROM image”文本和隐藏图片之间的联系感兴趣，道格使用 Ghidra 反汇编了代码。他发现代码会检查名为“secret ROM image”的 RAM 磁盘。如果找到，它会从 HPOE 资源加载 JPEG 图像数据，并在 RAM 磁盘中创建一个名为“The Team”的文件，类型为 JPEG。

与 Libera 上 #mac68k 的 ^alex 合作，他们发现，在格式化过程中格式化 RAM 磁盘并将卷命名为“secret ROM image”会触发这个彩蛋。用这个名称格式化 RAM 磁盘后，一个名为“The Team”的文件会出现在 RAM 磁盘中，打开时会包含 JPEG 图像。

该彩蛋适用于高达 Mac OS 9.0.4 的版本，可能在 9.1 中被禁用。布朗认为这是史蒂夫·乔布斯据报道禁止彩蛋之前的最后一个彩蛋之一。他希望与“The Team”中的任何一位成员联系，他们可能还记得这个彩蛋。

---

## 3. 食品塑料含量列表

**原文标题**: PlasticList – Plastic Levels in Foods

**原文链接**: [https://www.plasticlist.org/](https://www.plasticlist.org/)

鉴于内容极其有限，“塑料清单 – 食品中的塑料含量”难以进行简明扼要的总结。但我们可以推断其可能用途并进行概括。

**总结:**

“塑料清单 – 食品中的塑料含量”可能是一种资源（文章、数据库或指南），提供关于各种食品中存在的塑料污染及其含量的信息。它可能旨在告知消费者通过食物摄入塑料的潜在来源，并可能根据食品中的塑料含量对食品进行排名或分类。 这些信息可能来源于关于食品中微塑料和纳米塑料的科学研究、研究结果或报告。该资源还可能提供关于检测到的塑料类型、其潜在健康影响以及通过饮食选择减少塑料暴露的可能缓解策略的见解。最终，“塑料清单”可能作为一种工具，提高人们的意识并使个人能够就与塑料污染相关的食品消费做出更明智的决定。

---

## 4. 星舰：适用于任何 Shell 的极简、快速且可定制的提示符

**原文标题**: Starship: The minimal, fast, and customizable prompt for any shell

**原文链接**: [https://starship.rs/](https://starship.rs/)

Starship：极简、快速、可定制的终端提示符。其主要优势在于广泛的兼容性，可跨多种Shell和操作系统运行，几乎可在任何环境中使用。关键在于其“随处可用”的原则，意味着通用且可移植的提示解决方案。

---

## 5. 北欧半导体收购Memfault

**原文标题**: Nordic Semiconductor Acquires Memfault

**原文链接**: [https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault](https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault)

Nordic Semiconductor于2025年6月24日收购Memfault，标志着Nordic从硬件供应商向提供硬件、软件和云服务的完整解决方案合作伙伴的重要转变。Memfault是市场领先的云平台供应商，专门从事大规模互联产品部署。

此次收购旨在简化产品开发，加速上市时间，并通过持续的软件升级和设备管理，增强互联产品的安全性、性能和功能。Nordic计划将Memfault的功能集成到其产品组合和nRF Cloud服务平台中，从而创建更强大、更有效的解决方案。

Nordic Semiconductor首席执行官Vegard Wollan强调，此举将使客户能够与现场数百万台设备进行交互。Memfault首席执行官François Baldassari强调了为互联产品创建全栈解决方案。

预计此次收购将加强Nordic在边缘人工智能和安全解决方案方面的地位，使开发人员能够满足不断发展的行业和监管标准，例如欧盟网络弹性法案。Nordic致力于支持现有的Memfault客户，无论他们选择何种硬件，确保该平台通过对硬件集成、设备管理和人工智能功能的投资而持续发展。最终目标是缩短上市时间，降低运营成本，并改善互联产品的生命周期管理。

---

## 6. GPU基本知识

**原文标题**: Basic Facts about GPUs

**原文链接**: [https://damek.github.io/random/basic-facts-about-gpus/](https://damek.github.io/random/basic-facts-about-gpus/)

本文概述了GPU架构和优化技术的基础知识，重点介绍了NVIDIA A100 GPU。它解释了计算和内存层次结构，突出了快速计算和较慢内存访问之间的性能不平衡。

核心概念是Roofline模型，它定义了两种性能状态：内存受限和计算受限。内存受限的操作受限于内存带宽，而计算受限的操作受限于SM的算术速度。算术强度 (AI)，即FLOPs与访问字节的比率，决定了性能状态。目标是最大化AI以实现计算受限的性能。

本文介绍了两种关键的优化策略：**算子融合**和**分块**。算子融合将多个内存受限的操作组合成一个内核，消除中间内存流量并减少开销。分块用于计算受限的内核，如矩阵乘法，其中线程协同工作，将数据块加载到共享内存（SRAM）中，以最大化数据重用并增加AI。分块算法包括将数据加载到共享内存、同步线程和执行计算。

最后，本文讨论了来自主机CPU的开销影响，强调内核大小的重要性。如果内核太小或数量过多，则GPU会将时间花费在等待主机上，而不是执行计算。

---

## 7. 痛苦的教训即将降临到Token化领域。

**原文标题**: The Bitter Lesson is coming for Tokenization

**原文链接**: [https://lucalp.dev/bitter-lesson-tokenization-and-blt/](https://lucalp.dev/bitter-lesson-tokenization-and-blt/)

“Tokenization的苦涩教训即将到来”：本文认为，分词（LLM 中的常见做法）是一个瓶颈，应该用更通用、计算和数据驱动的方法来取代。

作者批评了字节对编码 (BPE) 这种流行的分词方法，强调了它的局限性，例如创建建模不佳的“故障标记”和不连贯的数字分词。 虽然承认存在变通方法，但文章质疑由于不完美的分词，有多少模型能力被浪费了。它质疑是否可以完全绕过分词。

文章指出 ByT5 是一个初步答案，表明纯字节建模可以用更少的数据实现相当的性能，但代价是增加了预训练和推理时间。 它还提到了替代架构，如 MambaByte，以绕过注意力的复杂性并减少增加的推理步骤。

文章强调，要成功取代分词，模型应表现出具有竞争力的损失分数，改进下游任务，并在增加计算和数据的情况下表现出更好的缩放曲线。它讨论了无分词模型的设计空间，围绕具有下/上采样的压缩表示和灵活的字节宽度。 探索包括 CANINE、Charformer 和 Hourglass Transformers 等架构，它们使用各种方法来压缩字节表示并减轻计算成本。 作者还提到了通过学习边界预测器来进行动态令牌池化。

---

## 8. Gemini机器人设备端：将AI引入本地机器人设备

**原文标题**: Gemini Robotics On-Device brings AI to local robotic devices

**原文链接**: [https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

Gemini Robotics On-Device是谷歌推出的一款新型高效AI模型，旨在本地运行于机器人设备上，无需持续的数据网络连接即可实现更强的灵活性和更快的任务适应性。这使其适用于对延迟敏感的应用以及在连接受限区域的稳定性能。

该模型建立在Gemini Robotics模型的功能之上，但针对最小化计算资源进行了优化。主要特点包括快速实验、通过少量（仅50-100个）演示进行微调以适应新任务以及低延迟推理。它擅长视觉、语义和行为泛化，能够遵循自然语言指令并完成复杂的任务，例如拉开拉链和折叠衣服，所有这些都直接在机器人上运行。

谷歌正在通过一个可信测试者计划向开发者提供Gemini Robotics SDK，以促进评估、在物理模拟器中进行测试以及快速适应新领域。该模型已展示了对各种机器人形态的适应性，包括双臂 Franka FR3 机器人和 Apptronik 公司的 Apollo 人形机器人。

谷歌强调负责任的开发和安全，秉承其 AI 原则，整合语义和物理安全措施，并进行红队演练以识别漏洞。该模型最初发布给精选的可信测试者群体，以收集反馈并确保负责任的使用。Gemini Robotics SDK 旨在通过使强大的模型更易于访问来加速机器人技术的创新。

---

## 9. Show HN: Oasis – 一款开源的3D打印智能生态箱

**原文标题**: Show HN: Oasis – an open-source, 3D-printed smart terrarium

**原文链接**: [https://github.com/justbuchanan/oasis](https://github.com/justbuchanan/oasis)

Oasis是一个开源的、主要采用3D打印技术的智能生态缸，旨在为喜湿植物创造理想的环境。它配备高功率LED照明、喷雾器、用于气流循环的风扇以及温湿度传感器。通过WiFi连接，可以使用网页界面进行控制和配置。

该项目完全开源，包括CAD模型（CadQuery）、电子原理图（KiCad）和软件（使用esp-rs的Rust）。虽然拥有3D打印机的DIY爱好者可以使用，但电子组装较为复杂。可以从像JLCPCB这样的公司订购组装好的电子元件，但少量订购可能比较昂贵。经验丰富的用户可以订购裸PCB板和元件进行DIY组装。

创建者计划将来提供组装好的电子元件套件，并邀请有兴趣的人通过Google表单表达兴趣并订阅更新。该网站提供了图片和构建细节。

---

## 10. Timdle – 将历史事件按时间顺序排列

**原文标题**: Timdle – Place historical events in chronological order

**原文链接**: [https://www.timdle.com/](https://www.timdle.com/)

Timdle：一款每日在线游戏，挑战玩家通过按时间顺序排列历史事件来测试他们的历史知识。核心玩法涉及在时间线上安排事件，网站鼓励玩家“玩今天的timeline”。页面还包含“如何玩”的说明，表明其设计旨在易于上手且引人入胜。最后，电子邮件地址(daily.timdle@gmail.com)表明了一个联系点，用于解答疑问或潜在的用户生成内容。总而言之，Timdle被呈现为一款有趣且具有教育意义的游戏，通过时间线排列来测试和加强历史知识。

---

## 11. 展示 HN：Autumn – 基于 Stripe 的开源基础设施

**原文标题**: Show HN: Autumn – Open-source infra over Stripe

**原文链接**: [https://github.com/useautumn/autumn](https://github.com/useautumn/autumn)

Autumn是一个构建于Stripe之上的开源层，旨在简化应用程序各种定价模型的创建和实施。它致力于抽象化账单基础设施的复杂性，例如管理网络钩子、升级/降级、取消和支付失败。

主要功能包括支持订阅、信用系统、基于使用量的模型和自定义计划。该平台的架构将账单逻辑与应用程序逻辑分离，从而更容易迭代定价策略，而无需进行大量的代码更改或数据库迁移。

Autumn提供了一个仪表板，用于创建产品和计划，支持使用量和超额使用、信用、基于席位的计费以及预付购买等定价模型。核心功能通过三个主要函数公开：`/attach` 用于购买流程和升级/降级，`/check` 用于验证客户对功能或使用量的访问权限，以及 `/track` 用于记录计量功能的使用事件。

用户可以通过云服务或使用Node.js、pnpm和Docker Compose进行自托管来开始使用。文档还提供了常见问题的故障排除步骤，并鼓励通过他们的指南进行贡献。通过Discord和电子邮件提供支持。

---

## 12. 法官支持Anthropic未经作者许可使用书籍训练人工智能

**原文标题**: Judge sides with Anthropic over training AI on books without authors' permission

**原文链接**: [https://techcrunch.com/2025/06/24/a-federal-judge-sides-with-anthropic-in-lawsuit-over-training-ai-on-books-without-authors-permission/](https://techcrunch.com/2025/06/24/a-federal-judge-sides-with-anthropic-in-lawsuit-over-training-ai-on-books-without-authors-permission/)

联邦法官裁定Anthropic胜诉，称未经作者许可使用受版权保护的图书训练人工智能模型可被视为合理使用。对于已对OpenAI和Meta等人工智能公司提起多起诉讼的作者和出版商来说，这项裁决是一次挫折。这些诉讼声称，这些公司使用他们的作品来训练大型语言模型（LLMs）构成侵犯版权。

法官的裁决取决于“合理使用”原则，这是版权法的一部分，它考虑了使用受版权保护材料的目的和转化性。虽然这项裁决不能保证在其他案件中取得类似的结果，但它为法院在此类纠纷中偏袒科技公司树立了先例。

诉讼案件*Bartz v. Anthropic*还引发了人们对Anthropic创建包含数百万份从盗版网站非法下载的有版权图书的“中央图书馆”的担忧。虽然法官认为使用这些材料训练人工智能模型属于合理使用，但将专门举行审判，以解决盗版副本和与Anthropic的“中央图书馆”相关的损害问题。法官承认，在最初从网上盗窃图书后获得合法副本并不能免除Anthropic的盗窃责任。

---

## 13. 循环微电脑，采用再利用的智能手机组件供电和驱动。

**原文标题**: Circular Microcomputers embedded and powered by repurposed smartphone components

**原文链接**: [https://citronics.eu/](https://citronics.eu/)

Citronics提供“循环微电脑”——由回收智能手机组件驱动的嵌入式计算解决方案。这些运行在基于Linux的操作系统上的微电脑，专为可扩展性、连接性（4G LTE、WiFi、以太网）而设计，并拥有强大的多核CPU和GPU。

Citronics将退役的智能手机转变为工业级的微型嵌入式计算机，为开发、原型设计和大规模生产的定制微电脑提供解决方案。他们提供的服务包括安全云管理、运营监管和工程培训，以加速产品上市时间并优化产品开发。

应用领域涵盖多个行业：能源（供暖优化）、教育（边缘计算集群）、工业（区域供热网关）和活动（可持续显示器）。

Citronics通过独特的性价比、利用标准化硬件和开源软件缩短上市时间以及可靠的本地供应来突出其竞争优势。他们使公司能够将自己定位为可持续发展的领导者，每个部署的设备可改善17.71千克二氧化碳当量的可持续发展报告。Citronics鼓励有兴趣的人士联系他们、预约通话或预订他们的产品。Destore、UCLouvain和Karno等公司正在使用Citronics进行各种应用。

---

## 14. 破解 WebAuthn、FIDO2 及伪造通行密钥

**原文标题**: Breaking WebAuthn, FIDO2, and Forging Passkeys

**原文链接**: [https://www.nullpt.rs/forging-passkeys](https://www.nullpt.rs/forging-passkeys)

本文详细探讨了通行密钥（FIDO2凭据的营销名称）的攻击面。它演示了如何伪造通行密钥和重放签名，以自动化在使用WebAuthn的网站上的登录过程，即使是那些看似需要硬件密钥的网站。

作者概述了FIDO2/WebAuthn生态系统的复杂性，突出了源于CTAP2二进制协议、CBOR数据结构和WebAuthn API怪癖的漏洞。该过程涉及剖析硬件密钥和平台验证器，以了解签名过程。

作者构建了一个软件验证器，通过USB-HID模拟FIDO2设备，使用用户模式代码和Wireshark捕获和分析CTAP2流量。通过解码CBOR/COSE结构并验证Yubico的打包证明，他们开发了一个基于Rust的CTAP2引擎，可以注入确定性密钥，确保通行密钥重放的可复现签名。

本文进一步深入探讨了如何通过DevTools协议（CDP）利用Chrome内置的“虚拟验证器”。这种方法可以通过编写无头FIDO2堆栈的脚本来完全控制WebAuthn调用，从而有效地绕过安全保护措施，而无需驱动程序、内核修改或扩展程序。该漏洞通过展示如何使用任意密钥预先填充验证器并禁用UX保护来得到证实。

文章最后强调了潜在的威胁模型，并为浏览器和依赖方（RPs）提出了加固通行密钥生态系统的缓解策略。

---

## 15. 在 Dockerized Flask / Django 应用中使用 Uv 替代 Pip

**原文标题**: Switching Pip to Uv in a Dockerized Flask / Django App

**原文链接**: [https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app](https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app)

本文详细介绍了如何在 Docker 化的 Flask 和 Django 应用中使用 `uv` 替代 `pip` 进行依赖管理，从而显著提高速度。文章提倡使用 `pyproject.toml` 替代 `requirements.txt` 定义依赖，并让 `uv` 自动生成包含正确依赖树的锁文件。

指南概述了 Dockerfile 的修改，包括从 GitHub 发布版安装 `uv`，复制 `pyproject.toml` 和 `uv.lock*`（初始时可选择不使用锁文件），设置诸如 `UV_COMPILE_BYTECODE=1` 在内的环境变量以便在构建时编译字节码，以及设置 `UV_PROJECT_ENVIRONMENT` 以避免创建虚拟环境。安装命令被替换为 `uv sync --frozen --no-install-project`，以利用锁文件并防止项目作为包安装。

文章还提供了用于常见任务的 Shell 脚本快捷方式，例如安装依赖、构建镜像以及在容器中运行 `uv` 命令。它涵盖了如何使用 `uv add` 和 `uv remove` 添加、更新或删除依赖，以及使用 `uv tree --outdated` 检查过时的包。作者强调使用“uv 方式” 通过 `uv sync` 管理依赖，并提供了一个视频演示来展示这些更改和命令。

---

## 16. Cloudflare如何拦截了一次高达7.3 Tbps的DDoS攻击

**原文标题**: How Cloudflare blocked a monumental 7.3 Tbps DDoS attack

**原文链接**: [https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/)

2025年5月中旬，Cloudflare成功缓解了一次针对一家托管服务提供商的、打破纪录的7.3 Tbps DDoS攻击，该攻击使用了Magic Transit。这次攻击在短短45秒内传送了37.4 TB的数据，是一次多向量攻击，主要由UDP泛洪组成，但也包括QOTD、Echo、NTP、Mirai、Portmap和RIPv1反射/放大攻击。

这次攻击源自161个国家/地区的5433个自治系统（AS）的超过122,000个源IP地址，其中很大一部分来自巴西和越南。巴西电信贡献了最大部分的流量。

Cloudflare的自主DDoS检测和缓解系统部署在其全球任播网络（477个数据中心）上，无需人工干预或警报即可识别并阻止这次攻击。该系统使用通过eBPF程序进行实时指纹识别来分析数据包样本并识别可疑模式。检测到的模式随后用于创建缓解规则，以丢弃恶意数据包。该系统还使用gossiping在全球范围内共享威胁情报，从而提高缓解效果。

Cloudflare为服务提供商提供免费的DDoS僵尸网络威胁信息源，以帮助他们识别并关闭其网络中的滥用帐户。该公司强调其致力于提供免费的、不限量的DDoS保护，作为其构建更好互联网使命的一部分。

---

## 17. 使用 Haskell 解决 LinkedIn 女王问题

**原文标题**: Solving LinkedIn Queens Using Haskell

**原文链接**: [https://imiron.io/post/linkedin-queens/](https://imiron.io/post/linkedin-queens/)

本文详细介绍了使用 Haskell 和回溯法解决 LinkedIn Queens 难题的过程。该难题要求在 N 色棋盘上放置 N 个皇后，使得每行、每列和每种颜色区域都恰好有一个皇后，且任意两个皇后不能在对角线上相邻。

文章从一个基本的回溯方法（尝试 0）开始，将部分解表示为一组皇后的位置，并使用 `LogicT` 库进行非确定性计算。这种方法是函数式的，但速度很慢。

尝试 1 通过基于行、列、颜色和对角线约束标记已排除的单元格（使用 `Map`）来提高性能，确保每一步的部分解都是合理的，并显著加快了解的速度。

尝试 2 侧重于及早发现死胡同。它跟踪每行、每列和每种颜色区域中剩余的未排除单元格的数量。`Partial` 类型被扩展以存储此信息，并且该算法会丢弃行、列或颜色区域没有可用单元格的分支，从而提高效率。

尝试 3 通过使用集合直接跟踪每行、每列和每种颜色的潜在候选者，进一步改进了候选者生成。它使用 `Remaining` 类型来表示可用的候选者或满足条件，避免了对无效分支的不必要探索。

尝试 4 引入了“策略”的概念，其中一组候选单元格在任何完整解决方案中必须恰好包含一个皇后。 引入了这种优化思想，表明了未来探索和改进的可能方向，但并未在提供的代码示例中完全实现。

本文展示了 Haskell 代码的逐步改进，通过结合约束和智能候选者选择，逐步提高算法的性能。每次尝试之后都有基准测试结果，展示了效率的提升。

---

## 18. 硬件疫情简史

**原文标题**: A brief history of hardware epidemics

**原文链接**: [https://eclecticlight.co/2025/06/21/a-brief-history-of-hardware-epidemics/](https://eclecticlight.co/2025/06/21/a-brief-history-of-hardware-epidemics/)

本文探讨了困扰计算机的“硬件瘟疫”，重点关注三个主要问题：电容瘟疫、无铅焊料问题和蝶式键盘。

**电容瘟疫（1999-2007）：** 廉价、伪劣的电容器使用有缺陷的电解液，导致主板和其他组件（包括某些iMac G5和eMac型号）出现大范围故障。 这些电容器过热、泄漏，甚至有时会着火，给制造商造成了数百万美元的损失。 苹果受到的影响不如其他一些公司，并且该问题在2007年后基本消退。

**无铅焊料（2006-2017）：** 欧盟禁止在电子产品中使用铅导致了无铅焊料的采用。 虽然对环境有益，但这种焊料的可靠性较差，尤其是在MacBook、iMac和PC中的高性能显卡中。 笔记本电脑中的热循环导致焊点失效，从而导致显卡问题。 苹果为某些受影响的型号延长了保修期。

**蝶式键盘（2015-2019）：** 苹果的蝶式键盘设计旨在实现更薄的笔记本电脑，但存在可靠性问题。 碎屑堆积导致按键卡住、重复或无法使用。 尽管进行了设计调整，但苹果最终恢复了传统的剪刀式结构，并实施了一项大型维修计划。

文章最后强调了苹果在通过服务计划和客户支持解决产品问题方面的相对强势记录，通常超出保修义务来解决问题。

---

## 19. FICO将把先买后付贷款纳入信用评分

**原文标题**: FICO to incorporate buy-now-pay-later loans into credit scores

**原文链接**: [https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later](https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later)

无法访问文章链接。

---

## 20. 基于 SQLite 的检索增强生成

**原文标题**: Retrieval Augmented Generation Based on SQLite

**原文链接**: [https://github.com/ggozad/haiku.rag](https://github.com/ggozad/haiku.rag)

Haiku SQLite RAG 是一个基于 SQLite 构建的检索增强生成库，无需外部服务器。它为管理和搜索文档提供了一个本地解决方案。主要特性包括：

*   **本地 SQLite 数据库：** 直接在 SQLite 数据库中存储文档和嵌入。
*   **嵌入提供者灵活性：** 支持 Ollama（默认）、VoyageAI 和 OpenAI 嵌入提供者，并允许自定义实现。
*   **混合搜索：** 结合向量搜索（使用 sqlite-vec）和全文搜索 (FTS5)，使用倒数排序融合 (Reciprocal Rank Fusion) 以获得更好的结果。
*   **文件监控：** 自动索引指定目录中的文件，检测添加、修改和删除。
*   **广泛的文件格式支持：** 解析超过 40 种文件格式，包括 PDF、DOCX、HTML、Markdown 和音频。也支持 URL 摄取。
*   **MCP 服务器：** 将 RAG 功能公开为 MCP 工具，以便与 AI 助手集成。
*   **CLI 和 Python 客户端：** 提供命令行和 Python 接口，用于管理和搜索文档。

该工具可以通过 `uv pip install haiku.rag` 安装。它支持通过环境变量配置，以指定嵌入提供者、API 密钥和监控目录。CLI 提供了用于列出、添加、获取、删除和搜索文档的命令。MCP 服务器允许与诸如 Claude Desktop 等 AI 助手集成。Python 客户端提供用于文档管理和搜索的异步方法。

---

## 21. 你的终端能显示表情符号吗？多大？

**原文标题**: Can your terminal do emojis? How big?

**原文链接**: [https://dgl.cx/2025/06/can-your-terminal-do-emojis](https://dgl.cx/2025/06/can-your-terminal-do-emojis)

本文探讨了终端显示表情符号的能力，尤其关注如何放大它们。重点介绍了1978年推出的VT100终端令人惊讶的功能，即使用DECDHL（DEC双倍高度行）转义序列来显示双倍高度文本。文章通过在两行中显示相同的文本来演示这些序列的工作原理，从而有效地将高度翻倍。

然后，文章挑战读者使用提供的`printf`命令测试自己的终端是否支持DECDHL。当与Unicode支持结合使用时，DECDHL可用于“切碎”表情符号，通过显示一个表情符号的上半部分和另一个表情符号的下半部分来创建新的、独特的组合。作者提供了诸如组合“面无表情的脸”和“没有嘴的脸”之类的例子。

文章承认并非所有终端都支持表情符号和DECDHL，但认为这在脚本中是一个易于实现的功能，并且在不支持的环境中会优雅地降级为重复文本。文章提供了一个gist链接，该链接尝试检测DECDHL支持。最后，作者提到了Kitty，一个更现代的终端模拟器，它提供了用于以不同大小显示文本的替代方法。

---

## 22. Svalboard：Datahand 重生

**原文标题**: Svalboard: Datahand Lives

**原文链接**: [https://svalboard.com/](https://svalboard.com/)

Svalboard：Datahand 再生 旨在推广 Svalboard Lightly，这是一款符合人体工程学的键盘，通过模仿 Datahand 来缓解疼痛并提高生产力。它采用磁性、轻触按键，并提供高度可定制的贴合度，以适应任何手的大小或形状。与传统键盘相比，Svalboard 允许用户采用自然的手部姿势，从而显著减少压力和疲劳。

主要特点包括：

*   **磁性按键：** 轻巧、触感灵敏的磁光按键，具有短行程。
*   **定制贴合：** 可调节手指长度、指尖大小和手掌大小。
*   **多种安装选项：** 兼容各种桌面、椅子或膝上安装方式。
*   **指点选项：** 集成轨迹球、指点杆和触摸板选项。
*   **可定制布局：** 支持 QWERTY、Dvorak、Colemak，并允许通过 Vial-QMK 重新映射。
*   **自制套件：** 可选择 3D 打印和组装您自己的键盘。
*   **耐用且可维护：** 模块化设计，便于维修和修改，并配有可更换部件。

该键盘基于 QMK 引擎构建，可实现广泛的自定义和宏编程。作为 Datahand 的长期用户，其创建者设计 Svalboard 是为了替代已停产的设备，旨在提供无痛的打字体验。该设计强调可修复性、可修改性和社区支持。Svalboard Lightly 自豪地在美国制造，并在全球范围内使用。可选的附加组件包括彩色键帽、底座颜色选项和自制套件。

---

## 23. 新的火狐浏览器附加组件政策

**原文标题**: New Firefox Add-On Policies

**原文链接**: [https://blog.mozilla.org/addons/2025/06/23/updated-add-on-policies-simplified-clarified/](https://blog.mozilla.org/addons/2025/06/23/updated-add-on-policies-simplified-clarified/)

火狐附加组件团队更新了addons.mozilla.org (AMO) 的附加组件策略，自2025年8月4日起生效，主要目标是简化和明确开发者的策略。

主要变更包括：

*   **取消“封闭组”禁令：** AMO现在将允许扩展程序用于有限数量用户的私人或内部用途，从而为开发者提供更大的灵活性。

*   **数据同意和控制术语更新：** 该策略仅关注用户数据在扩展程序或浏览器之外的*传输*，消除了对扩展程序内部数据收集的担忧（只要未经同意不进行传输）。更新后的术语旨在减少开发者的困惑。

*   **隐私政策托管灵活性：** 开发者不再需要在AMO上直接托管隐私政策。相反，他们可以链接到自行托管的政策，从而简化更新并减少提交新扩展程序的需要。文章强调，数据收集的透明度仍然至关重要。

*   **用户脚本API策略：** userScripts API只能由用户脚本管理器扩展程序使用，不得用于扩展或修改脚本管理器本身的功能。

*   **源代码提交指南：** 所有依赖项必须直接包含在源代码包中，或者仅在构建过程中通过官方包管理器下载。

这些更改旨在使火狐扩展程序的开发更加简化。

---

## 24. 霍尼韦尔H316厨房电脑 (2023)

**原文标题**: Honeywell H316 Kitchen Computer (2023)

**原文链接**: [https://kbd.news/Honeywell-H316-kitchen-computer-1940.html](https://kbd.news/Honeywell-H316-kitchen-computer-1940.html)

KBD.news 的这篇文章回顾了霍尼韦尔 H316“厨房电脑”，这款机器常因其不切实际和缺乏商业成功而备受嘲笑。作者旨在为它辩护，澄清误解并突出其重要性。

虽然 H316 最初是一款机架式计算机，但霍尼韦尔提供了桌面式和基座式版本，后者就是臭名昭著的“厨房电脑”。它在 1969 年的内曼·马库斯目录中出现，目标客户是家庭主妇，用于存储食谱，尽管它采用二进制界面，缺乏键盘（最初），并且价格高昂（相当于 2023 年的 86,900 美元）。

这篇文章驳斥了内置砧板的说法，澄清它更像是一个扶手。作者认为，考虑到 N-M 目录中稀奇古怪的商品以及 H316 在广告之前就已存在且没有厨房专用品牌的事实，厨房电脑很可能是一种公关噱头。

尽管其被认为是失败的，但霍尼韦尔还是生产了 20 台，主要作为落地模型，并且营销活动确实引起了关注。文章总结说，虽然没有人把它当作厨房电器购买，但它仍然是一件收藏品，并且可能通过让公众接触个人技术，影响了未来消费计算机的发展。一台霍尼韦尔计算机甚至记录了那个臭名昭著的 N-M 目录的内容。

---

## 25. MCP正在吞噬世界

**原文标题**: MCP is eating the world

**原文链接**: [https://www.stainless.com/blog/mcp-is-eating-the-world--and-its-here-to-stay](https://www.stainless.com/blog/mcp-is-eating-the-world--and-its-here-to-stay)

无法访问文章链接。

---

## 26. 爱彼迎和民宿短租正在走下坡路，就像河马在滑水梯上一样。

**原文标题**: Airbnb and Vrbo are going downhill like a hippo on a water slide

**原文链接**: [https://www.washingtonpost.com/opinions/2025/06/19/vacation-rentals-airbnb-vrbo/](https://www.washingtonpost.com/opinions/2025/06/19/vacation-rentals-airbnb-vrbo/)

无法访问文章链接。

---

## 27. 变形虫：九十年代的分布式操作系统 (1990) [pdf]

**原文标题**: Amoeba: A distributed operating system for the 1990s (1990) [pdf]

**原文链接**: [https://www.cs.cornell.edu/home/rvr/papers/Amoeba1990s.pdf](https://www.cs.cornell.edu/home/rvr/papers/Amoeba1990s.pdf)

该文档似乎是1990年发表的题为“Amoeba：面向20世纪90年代的分布式操作系统”论文的线性化PDF数据。PDF代码包含关于文档结构的元数据，包括目录、页面树、资源和对象引用。它使用诸如Linearized、对象编号、交叉引用表（xref）和定义PDF内容的流对象等PDF运算符。/ID字段表明该文档曾经被处理过。

仅根据线性化PDF数据，无法提供Amoeba论文实际*内容*的摘要，例如其架构、特性或实验结果。PDF代码仅仅描述了论文内容如何在PDF文件格式中组织。流对象包含需要解码和渲染的压缩和编码的图像和文本数据，才能理解论文的内容。

---

## 28. 4Real-Video-V2：用于四维场景生成的前馈重建

**原文标题**: 4Real-Video-V2: Feedforward Reconstruction for 4D Scene Generation

**原文链接**: [https://snap-research.github.io/4Real-Video-V2/](https://snap-research.github.io/4Real-Video-V2/)

4Real-Video-V2是一种新的4D场景生成方法，它建立在原有的4Real-Video之上。它采用前馈架构，包括一个4D视频扩散模型和一个前馈重建模型，以生成视频帧的时空网格以及每个时间步的3D高斯粒子。

V2的一个关键改进是更新后的4D视频扩散模型架构。重要的是，它引入了一种新的稀疏注意力模式，而没有增加基础视频模型中的参数总数。这种稀疏注意力允许令牌专注于同一帧内、同一时间戳或来自同一视点的其他令牌。这种设计实现了与大型预训练视频模型的可扩展性，提供了高效的训练，并增强了泛化能力。

该论文展示了该方法从文本提示生成4D视频、动画化真实3D场景和动画化3D资产的能力。视觉比较表明，与先前的多视角视频生成方法（包括原始的4Real-Video）相比，其性能更优越，尤其是在3D资产动画方面。在Objaverse数据上的架构比较进一步突出了相对于并行、顺序和SV4D方法的进步。

---

## 29. 展示一下：天气观测

**原文标题**: Show HN: Weather Watching

**原文链接**: [https://walzr.com/weather-watching](https://walzr.com/weather-watching)

无法访问文章链接。

---

## 30. 英伟达RTX 5050 GPU起价249美元，采用上一代GDDR6显存

**原文标题**: Nvidia's RTX 5050 GPU starts at $249 with last-gen GDDR6 VRAM

**原文链接**: [https://www.theverge.com/news/692045/nvidia-geforce-rtx-5050-desktop-laptop-gpu-gddr6-gddr7](https://www.theverge.com/news/692045/nvidia-geforce-rtx-5050-desktop-laptop-gpu-gddr6-gddr7)

英伟达发布GeForce RTX 5050桌面及笔记本GPU。桌面版起价249美元，配备8GB GDDR6显存，2560个Blackwell CUDA核心，功耗最高130W。这些显卡将于7月下半月由华硕和微星等第三方合作伙伴提供，预计7月初发布驱动更新。

RTX 5050笔记本版本将采用8GB GDDR7显存，2560个Blackwell CUDA核心，功耗在35W到100W之间。搭载该GPU的笔记本电脑预计起价999美元，部分型号将立即上市。GDDR7的效率有助于实现更纤薄的笔记本设计。

虽然桌面版RTX 5050配备GDDR6显存，这似乎有些奇怪，但预计其性能仍将优于配备GDDR7的笔记本版本。尽管与RTX 5060具有相同的显存容量，但其CUDA核心数量的减少可能会导致性能差距。

英伟达声称RTX 5050可以在高设置下提供“沉浸式光线追踪体验”，并引用了在启用DLSS 4的情况下，《赛博朋克2077》等游戏中超过150 fps的帧率。然而，此性能是在高端AMD Ryzen CPU和1080p分辨率下实现的。在传统光栅化中，据称RTX 5050比RTX 3050快60%。这款新卡是广受欢迎的RTX 3050的直接继任者。

---

## 31. 数学主要是混沌还是秩序？

**原文标题**: Is mathematics mostly chaos or mostly order?

**原文链接**: [https://www.quantamagazine.org/is-mathematics-mostly-chaos-or-mostly-order-20250620/](https://www.quantamagazine.org/is-mathematics-mostly-chaos-or-mostly-order-20250620/)

本文探讨了集合论中关于数学本质的争论：数学本质是主要有序的还是混乱的？这场争论的核心在于无穷的概念及其各种大小，即基数。几十年来，集合论学家一直在定义越来越大的基数，发现了一个出人意料的整洁层次结构，这表明了一个结构良好的数学宇宙（V）。休·伍丁旨在通过构建“终极L”来映射V，这是一个包含所有大基数的内部模型，依赖于V是“世袭序数可定义的”（HOD）的假设。

然而，胡安·阿吉莱拉、霍安·巴加里亚和菲利普·卢克引入了两种新的无穷类型，“精确”和“超精确”基数，它们挑战了这种有序的观点。这些基数表现出不寻常的性质，当与较小的基数结合时会“爆炸”，这意味着存在出乎意料的更大的无穷，并可能使V远非HOD。这一发现表明，数学宇宙的很大一部分可能是不可定义的和混乱的。

虽然伍丁仍然致力于他的终极L计划，但其他数学家，如托比·梅多斯，发现混乱的可能性令人兴奋，这为探索开辟了新的途径。该团队目前正在收集证据，以证明这些基数与ZFC是一致的。本文强调，在集合论中证明这样的说法类似于实验科学，需要证据和分析，而不是明确的证明。这场辩论最终取决于这些新的无穷是否与已建立的集合论公理一致，以及它们是否真正破坏了大基数的现有层次结构。

---

## 32. FPGA迎来40周年

**原文标题**: The FPGA turns 40

**原文链接**: [https://www.adiuvoengineering.com/post/the-fpga-turns-40](https://www.adiuvoengineering.com/post/the-fpga-turns-40)

本文庆祝FPGA诞生40周年，重点介绍了其从1985年首款具有商业价值的Xilinx XC2064到现代高度复杂器件的演变历程。XC2064提供64个具有三输入查找表(LUT)的可配置逻辑块(CLB)，而如今最大的AMD FPGA则拥有890万个系统逻辑单元、820万个触发器和400万个LUT。

文章强调，进步不仅体现在逻辑容量的增加上，现代FPGA还集成了Arm处理内核、高速收发器、存储控制器、DSP元件和AI加速。文章回顾了XC2064最初55美元（约合2025年165美元）的价格以及最终降至5美元的情况，突出了其对数字逻辑设计的影响，使得电路板可以在单个芯片内实现。

文章还重点介绍了FPGA技术的快速发展，从XC2000系列到XC3000和XC4000系列，最终发展到Virtex和Spartan系列。文章描述了从XDE等物理设计编辑器到使用HDL和自动布局布线工具的转变，以及IP内核的出现。作者回顾了为各种应用开发FPGA的个人经验，并指出了可用的学习资源，如网络研讨会、研讨会、培训课程和Adiuvo开发板。

---

## 33. ASUS可疑漏洞 - 用户信息自2022年起暴露

**原文标题**: ASUSpicious Flaw – Users' Information Exposed Since 2022

**原文链接**: [https://mrbruh.com/asus_p2/](https://mrbruh.com/asus_p2/)

安全研究人员发现华硕MyAsus软件存在漏洞，自2022年8月以来暴露了数百万用户的个人信息。该漏洞源于AsusSSO.dll和AsusAPI.dll文件中硬编码的加密管理凭据，导致对多个API端点拥有不受限制的访问权限。

利用这些凭据，恶意行为者可能：

*   根据电子邮件地址列出支持工单信息（工单ID、姓名、日期）。
*   将文件上传到任何支持工单。
*   创建欺诈性支持工单。
*   检索支持工单的完整详细信息。
*   可能访问RMA工单信息。
*   通过电子邮件地址获取用户ID。
*   检索完整的用户数据，包括姓名、出生日期、电话号码和地址。

该研究人员成功演示了这些漏洞利用，并向华硕报告了这些问题。该漏洞已于2025年5月20日通过发布MyAsus 4.2.35.0版本进行修补。该研究人员批评华硕缺乏漏洞赏金计划，认为这会激励研究人员将漏洞出售给恶意行为者，而不是报告它们。该研究人员于2025年4月23日报告了该漏洞，在华硕邮件系统阻止PoC代码出现一些问题后，华硕在一个月后修补了该漏洞。华硕还要求研究人员免费测试修补后的版本，由于缺乏补偿，该请求被拒绝。

---

## 34. 《禁止假冒商品法案》已修改，情况更糟了

**原文标题**: The NO FAKES act has changed, and it's worse

**原文链接**: [https://www.eff.org/deeplinks/2025/06/no-fakes-act-has-changed-and-its-so-much-worse](https://www.eff.org/deeplinks/2025/06/no-fakes-act-has-changed-and-its-so-much-worse)

根据这篇文章，最初旨在打击生成式人工智能产生的不实信息的《禁止伪造法案》（NO FAKES Act）已经成为对互联网自由和创新的一大威胁。该法案试图围绕数字“复制品”建立广泛的知识产权，更新后的版本变本加厉地采取了这种有缺陷的做法，强制要求建立全面的审查基础设施。

这种新的基础设施要求互联网守门人实施过于宽泛的过滤器，类似于现有的版权过滤器，以防止违规内容的重新上传，甚至删除用于创建“复制品”的工具。这很可能导致过度审查和“反对者的否决”效应，扼杀合法的言论，如模仿和讽刺。

此外，该法案允许仅凭指控就轻易地揭露用户身份，从而扼杀匿名言论，并可能使个人面临伤害。通过增加对新服务的监管负担，《禁止伪造法案》也巩固了大型科技公司的统治地位，并阻碍了人工智能工具的创新，因为开发者担心会因未经证实的指控而成为目标。

这篇文章认为，《禁止伪造法案》是一个为了解决问题而创造的问题，特别是因为国会最近通过了另一项旨在监管在线内容的法案《下架它》（Take It Down）。作者得出结论，《禁止伪造法案》的主要目的是巩固对数字图像商业利用的控制权，但会对言论自由、创新和个人隐私造成重大附带损害。文章敦促读者联系国会并反对该法案。

---

## 35. “龙太子”恐龙发现“改写”霸王龙家族树

**原文标题**: 'Dragon prince' dinosaur discovery 'rewrites' T.rex family tree

**原文链接**: [https://www.bbc.com/news/articles/cy8dzv3vp5jo](https://www.bbc.com/news/articles/cy8dzv3vp5jo)

根据《自然》杂志发表的一项研究，一种新发现的恐龙物种，蒙古克胡鲁（*Khankhuuluu mongoliensis*），正在改写暴龙的家谱。这些8600万年前的化石在蒙古的一家博物馆收藏中被发现，代表了所有暴龙（包括标志性的雷克斯霸王龙）已知的最接近的祖先。

“蒙古龙太子”克胡鲁为理解从小型、敏捷的暴龙类向最终演变成的巨大顶级掠食者的进化过渡提供了关键的联系。克胡鲁重约750公斤，被认为是过渡化石，比成年雷克斯霸王龙小得多，后者重量可能是它的八倍。

这项发现揭示了暴龙统治地位的关键特征的早期进化阶段，包括由特定头骨结构（在鼻骨中很明显）促进的强有力的下颚。这些特征使后来的暴龙（如雷克斯霸王龙）能够猎捕更大的猎物，甚至咬碎骨头。

这些化石最初于20世纪70年代被发现，并被错误地归类为阿莱克托龙，后来研究人员重新对其进行了检查，并识别出独特的暴龙类特征。这些恐龙通过陆桥在北美和亚洲之间移动，在其进化过程中发挥了关键作用，推动了数百万年来不同暴龙群体的演变。这项发现突显了在暴龙成为“国王”之前，它们曾是“王子”，展示了它们从小祖先进化而来的过程。

---

## 36. 维拉·C·鲁宾天文台首批图像

**原文标题**: Vera C. Rubin Observatory first images

**原文链接**: [https://rubinobservatory.org/news/rubin-first-look/cosmic-treasure-chest](https://rubinobservatory.org/news/rubin-first-look/cosmic-treasure-chest)

维拉·C·鲁宾天文台发布首批图像，展示了其32亿像素LSST相机（世界上最大的数码相机）所捕捉的丰富数据。首张图像聚焦于室女座星系团南部区域，距离约5500万光年，揭示了数百万个星系，仅占其为期10年的“时空遗产巡天”（LSST）计划中将捕捉的200亿个星系的一小部分。这项巡天将以前所未有的细节呈现整个南半球天空。

鲁宾天文台以其快速生成大型、细节丰富的图像的能力而著称，它将短时间内采用不同颜色滤镜拍摄的多次曝光结合在一起。这使得探测极其微弱的物体以及以前所未有的细节绘制银河系地图成为可能。这些图像还捕捉到了小行星，展示了该天文台追踪太阳系中潜在危险物体的能力。

LSST将使全球科学家能够解决关于宇宙的基本问题，包括银河系的形成、暗物质和暗能量的本质，以及太阳系内天体的详细清单。它还将追踪夜空的变化，识别数百万个瞬态事件，如超新星和黑洞耀斑。这些数据将被用于调查我们宇宙邻域的动态历史，并了解宇宙的演化。鲁宾天文台的独特功能为不断变化的天空提供了新的视角，并有望带来无数新的发现。

---

## 37. 弹珠爆破

**原文标题**: Marble Blast

**原文链接**: [https://marbleblast.vaniverse.io/](https://marbleblast.vaniverse.io/)

《弹珠冲击网页版》是一款基于网页的游戏，玩家需要操控弹珠穿越充满挑战的环境，收集宝石，并竞速到达终点。游戏利用加速、超级跳跃和陀螺仪等道具来克服障碍，提升速度。玩家通过键盘控制弹珠的移动，通过鼠标控制视角。

描述中详细介绍了游戏元素，例如起点和终点平台、宝石，以及各种影响弹珠能力的道具。还概述了关卡中的危险，例如风扇、龙卷风、活板门、保险杠、地雷和油污。

文本还指出 GarageGames 是最初的发行商，并强调了他们支持独立游戏开发者的使命。 游戏中使用的 Torque 游戏引擎也被提及，以及其低成本的可访问性。列出了弹珠冲击开发团队的主要贡献者。网页移植版由 Vanilagy 创建，他将代码开源。

还提到了其他设置和选项，例如自定义弹珠纹理、视频渲染和音频设置。

---

## 38. 首例以甲烷为食的海蜘蛛在海底被发现

**原文标题**: First methane-powered sea spiders found crawling on the ocean floor

**原文链接**: [https://www.cnn.com/2025/06/17/science/spiders-deep-sea-methane-new-species](https://www.cnn.com/2025/06/17/science/spiders-deep-sea-methane-new-species)

美国有线电视新闻网报道称，在美国西海岸附近的甲烷渗漏区，发现了三种新的毛颚蛛属海蜘蛛。与其他海蜘蛛不同，这些物种似乎与以甲烷为食的细菌存在共生关系。这些细菌生活在海蜘蛛的外骨骼上，将甲烷转化为糖类和脂肪，然后海蜘蛛将这些糖类和脂肪作为主要食物来源。这种摄食策略在海蜘蛛中独一无二。

这些海蜘蛛可能在阻止强效温室气体甲烷逸入大气层方面发挥着至关重要的作用。文章强调了理解深海生态系统对于其保护以及对更广泛环境问题（如减少水污染）的潜在益处的重要性。这些细菌会作为早期食物来源传递给幼体。

这一发现强调了深海生物的多样性和相互联系性，以及这些小生物对更大环境的潜在影响。需要进一步研究，以了解这种共生关系的全部程度及其对深海生态和气候变化的影响。科学家们警告说，在不了解可能对当地栖息地造成的损害的情况下，不要开采海底。

---

## 39. Show HN: Comparator - 我构建了一个免费开源的应用程序来比较工作 Offer

**原文标题**: Show HN: Comparator - I built a free, open-source app to compare job offers

**原文链接**: [https://comparator-one.vercel.app/](https://comparator-one.vercel.app/)

Comparator：一款免费开源的职位比较应用

---

## 40. 将翻盖手机打字方式复活为Linux驱动程序

**原文标题**: Resurrecting flip phone typing as a Linux driver

**原文链接**: [https://github.com/FoxMoss/libt9](https://github.com/FoxMoss/libt9)

本文介绍 LibT9，一个旨在在现代系统上复活 T9 预测文本输入（在老式翻盖手机上常见）的 C 语言库。该项目旨在提供一种在各种平台上实现 T9 输入的方法。

LibT9 提供了三种主要的实现选项：

*   **作为 Linux 驱动程序：** 允许在 Linux 内核中直接进行 T9 输入，模拟原始翻盖手机体验。
*   **作为 CLI 实用程序：** 一个用于测试和使用 LibT9 的命令行界面，编译需要 `ncurses` 和 `cmake`。
*   **作为网站：** 一个基于 Web 的演示，可在 foxmoss.github.io/libt9/ 上访问，展示了该库的功能。

除了基本的 C 标准库实现之外，该库没有外部依赖项。 CLI 实用程序需要 `ncurses` 来实现其基于文本的界面。该项目欢迎贡献，特别是实现标点符号支持、IBus 驱动程序和处理非单词输入。

该文档感谢 Matt Hardy（为 Web 演示背景）、Takala（为单词数据集）和 Chengtao Wang（为原始驱动程序代码）的贡献。

---

## 41. 使用C语言开发跨平台复古Roguelike游戏

**原文标题**: Developing a Retro-Roguelike Game for Multiple Platforms in C

**原文链接**: [https://retrogamecoders.com/roguelike-multiplatform/](https://retrogamecoders.com/roguelike-multiplatform/)

本文详细介绍了为多个平台开发复古Roguelike游戏的历程，从Commodore 64和PET等老式系统到现代Linux、Mac和Windows。最初使用TRSE（基于Pascal）的方法因作者不熟悉且对旧系统的支持不一致而充满挑战。

随后，作者转向C语言，希望通过交叉编译器获得更好的可移植性。然而，他们面临着条件编译的现实，需要处理不同的系统架构和编译器标准，这可能导致代码膨胀和维护问题。

主要挑战围绕硬件限制：内存限制、图形/字符集差异、输入方法和加载机制。为了缓解这些问题，重点转移到具有类似功能的系统（64K+ RAM）。

一个关键的胜利是实施程序化生成的地图，以节省空间并提供独特的游戏体验。该游戏包括基本的玩家移动、收藏品、敌人、战斗和物品交互。最初是基于文本的，作者探索了用户定义的图形，但面临着字符集变化的挑战。

最终，由于Commodore 64的普及、良好的图形/声音支持以及更简单的交叉开发，该策略演变为优先考虑该平台。作者强调从小处着手，明智地使用条件编译，优先考虑核心机制，设计灵活的资源，并研究硬件特性，以实现成功的多平台开发。结论强调了在雄心和实用主义之间取得平衡的重要性，从一个良好支持的平台开始，并逐步适应其他平台。

---

## 42. 深入剖析 Ruby on Rails 的 Solid Queue

**原文标题**: A Deep Dive into Solid Queue for Ruby on Rails

**原文链接**: [https://blog.appsignal.com/2025/06/18/a-deep-dive-into-solid-queue-for-ruby-on-rails.html](https://blog.appsignal.com/2025/06/18/a-deep-dive-into-solid-queue-for-ruby-on-rails.html)

深入剖析Solid Queue：基于数据库的Rails后台任务系统

本文深入探讨Solid Queue，一个使用数据库存储任务的Ruby on Rails后台任务系统。它在初步介绍的基础上，扩展讲解了诸如任务调度、周期性任务和并发控制等关键特性。

**任务调度：** Solid Queue 使用 `solid_queue_scheduled_executions` 表存储计划在未来运行的任务。Dispatcher进程持续轮询此表，并在任务到达预定时间时，通过创建 `ReadyExecution` 记录来分派任务。

**周期性任务：** 通过 `config/recurring.yml` 配置，周期性任务由 `RecurringTask` 模型和 `solid_queue_recurring_tasks` 表表示。Scheduler 进程与 Dispatcher 类似，查询此表来调度周期性任务。它使用 `Concurrent::ScheduledTask` 来调度一个线程，该线程将在正确的时间将任务加入队列，并为下一次执行重新调度自身。`RecurringExecution` 记录用于防止重复执行周期性任务。

**并发控制：** 通过 `limits_concurrency` 实现，此功能限制特定类型的任务并发运行的数量。它使用 `Semaphore` 记录来管理任务容量，并使用 `BlockedExecution` 记录来保存超过并发限制的任务。当具有并发限制的任务入队时，Solid Queue 尝试获取信号量锁。如果可用，任务将被入队；否则，将创建一个 `BlockedExecution` 记录。信号量被持有指定的时间。

---

## 43. Fairphone 6 将采用更可持续的新设计

**原文标题**: Fairphone 6 is switching to a new design that's even more sustainable

**原文链接**: [https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design](https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design)

Fairphone 6：下一代可持续手机，预计6月25日发布，起价549欧元，采用全新模块化设计，着重于轻松更换组件。泄露的渲染图展示了黑色、白色和绿色的手机，具有扁平边缘和独特的霓虹灯主题电源按钮。与之前的型号不同，Fairphone 6取消了突出的相机遮阳板，改为独立放置的镜头，并用螺丝固定。

一个关键特性是易于拆卸的后盖、电池、摄像头、显示屏和扬声器模块，所有这些都旨在实现简单的可修复性和更换。这一设计突显了Fairphone对可持续发展的承诺。

传闻的规格包括6.31英寸pOLED 120Hz显示屏，骁龙7s Gen 3处理器，搭配8GB RAM和256GB可扩展存储。预计配备4415mAh电池，支持33W快速充电。相机设置据称包括一个50MP主传感器、一个13MP辅助传感器和一个32MP前置摄像头。据报道，Fairphone 6还获得了欧盟标准的A级可修复性和耐用性认证。

---

## 44. 美国化学安全委员会或将被裁撤

**原文标题**: U.S. Chemical Safety Board could be eliminated

**原文链接**: [https://www.ishn.com/articles/114776-us-chemical-safety-board-could-be-eliminated](https://www.ishn.com/articles/114776-us-chemical-safety-board-could-be-eliminated)

特朗普政府提议于2026年10月前取消美国化学安全与危害调查委员会（CSB），理由是财政责任以及与环保署（EPA）和职业安全与健康管理局（OSHA）的职能重叠。这项提案是2026财年预算的一部分，面临国会的两党反对和行业团体的担忧。

CSB成立于1990年，自1998年开始运作，负责调查工业化学事故，确定根本原因，并发布安全建议，但没有监管权力。其调查结果影响了环保署和职业安全与健康管理局的政策。CSB以精干的团队和预算运作，但已调查了170多起化学事故，并发布了1000多项建议。

白宫管理和预算办公室（OMB）认为，关闭该机构符合财政责任，而CSB自身提交的2026年预算申请也设定为零美元。批评人士认为，CSB在根本原因分析方面发挥着独特作用，在提高安全性方面有着良好的记录，并为面临化学灾害风险的社区和工人提供支持。取消CSB将增加风险，并可能阻碍环境正义方面的进展。

美国化学理事会和氯气研究所等行业团体已表示支持CSB继续运作。该提案需要国会批准，预计将面临阻力。CSB继续其运作，强调其在确保化学安全以及保护社区、工人和环境方面的作用。

---

## 45. 游览 Zig-EM 代码景观 (2024)

**原文标题**: Touring the Zig-EM code-scape (2024)

**原文链接**: [https://zigem.openem.org/post-003/](https://zigem.openem.org/post-003/)

本文介绍 Zig•EM，一个构建于 Zig 之上的嵌入式系统编程框架。它指导读者通过安装 Zig，克隆 `zigem-dev` 仓库，并使用 `zig build` 来设置和更新 Zig•EM 安装。文章强调了 Zig 缓存对于构建效率的重要性。

随后，文章探讨了一个典型的 Zig•EM 项目的组织结构，重点介绍了 `build.zig` 文件以及 `workspace/` 文件夹内的结构。该文件夹包含诸如 `em.core` 这样的包，其中有唯一命名的桶（buckets），例如 `em.utils`。单独的编译单元位于 `.em.zig` 文件中，并使用 "em" 库。该框架强制执行三级结构：包 > 桶 > 单元，并提倡使用具有全局唯一前缀的命名空间层级结构来管理桶和包。`em.import` 操作符用于引用其他单元。

文章还介绍了诸如 `EM__TARG` 和 `EM__META` 结构等关键概念，它们包含定义和声明。`EM__CONFIG` 被呈现出来，当实例化为 `EM__C` 时，允许访问之前创建的纤程（fibers）。文章给出了一个示例程序，`em.examples.basic/FiberP`，演示了使用 `em.utils/FiberMgr` 管理的轻量级线程。最后，文章展示了如何使用 `zigem compile`，并描述了双重编译过程，该过程首先针对 `META` 域进行编译，然后再针对 `TARG` 域进行编译。

---

## 46. 京都后院咖啡与爵士乐

**原文标题**: Backyard Coffee and Jazz in Kyoto

**原文链接**: [https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto](https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto)

无法访问文章链接。

---

## 47. Discord 威胁要关闭 BotGhost

**原文标题**: Discord Is Threatening to Shutdown BotGhost

**原文链接**: [https://update.botghost.com/](https://update.botghost.com/)

文章称Discord正威胁关闭BotGhost，一项允许用户轻松创建和管理Discord机器人而无需大量编码知识的流行服务。此举被认为是Discord“垃圾化”的一个例证，该术语指的是平台因优先考虑利润而非用户体验而导致的价值下降。

核心论点是，Discord越来越倾向于其自身的原生机器人工具和更严格的政策，使得BotGhost等第三方机器人平台难以运营。这限制了用户的选择，并可能导致Discord体验变得不那么多样化和可定制。

文章可能认为BotGhost提供了一项有价值的服务，使缺乏高级编码技能的用户能够为Discord社区做出贡献。它的潜在关闭将损害这些用户，并代表Discord生态系统中创新能力的丧失。作者可能将Discord的行为描述为反竞争，并且对平台的整体健康有害。最终，文章暗示Discord正在牺牲用户友好的选项，以换取更严格的控制和潜在的更赚钱的途径。

---

## 48. QuEra量子系统利用中性原子进行计算

**原文标题**: QuEra Quantum System Leverages Neutral Atoms to Compute

**原文链接**: [https://www.nextplatform.com/2025/06/20/quera-quantum-system-leverages-neutral-atoms-to-compute/](https://www.nextplatform.com/2025/06/20/quera-quantum-system-leverages-neutral-atoms-to-compute/)

量子计算势头正劲：从理论到实践

本文重点介绍了量子计算日益增长的势头，正从理论上的“是否实现”转变为实际的“何时实现”。QuEra、IBM、谷歌和微软等公司正在构建可靠的量子系统方面取得进展，尤其侧重于纠错。IBM计划在2029年前发布容错量子系统。

对量子技术的投资激增，今年第一季度投资额超过12.5亿美元。Nvidia等公司正在进入市场，而D-Wave等现有企业也在扩大其产品。

QuEra利用中性原子技术，最近获得了2.3亿美元的融资，并在日本和英国安装了其基于门的中性原子Gemini量子系统。QuEra的方法具有室温运行和紧凑设计等优势。Yuval Boger强调了混合经典-量子环境的重要性，其中QPU补充CPU和GPU。

量子计算正从创建量子比特发展到构建具有足够量子比特来解决实际问题的系统。预计未来几年内，初步应用将出现在化学、制药和材料科学领域。QuEra的Aquila系统可通过AWS访问，是一个模拟系统，而Gemini系统是一个数字系统，标志着可编程性和性能的进步。该行业预计量子比特质量、连接性和软件基础设施将进一步改进。

---

## 49. Fedora Linux开发者讨论放弃32位软件包——对Steam游戏玩家是坏消息

**原文标题**: Fedora Linux devs discuss dropping 32-bit packages – bad news for Steam gamers

**原文链接**: [https://www.gamingonlinux.com/2025/06/fedora-linux-devs-discuss-dropping-32-bit-packages-potentially-bad-news-for-steam-gamers/](https://www.gamingonlinux.com/2025/06/fedora-linux-devs-discuss-dropping-32-bit-packages-potentially-bad-news-for-steam-gamers/)

GamingOnLinux.com文章讨论了Fedora Linux开发者提出的在Fedora 44中放弃对32位软件包(i686)支持的提议。虽然从长远来看，这一改变可能是有益的，但它引起了人们的担忧，尤其是Steam游戏玩家，因为Steam客户端和许多游戏都依赖于32位库，通过Proton/Wine实现正常功能。

文章强调了潜在的强烈反对，并提到了Ubuntu的类似情况，当时Valve曾威胁要撤回支持，之后Ubuntu撤销了该决定。作者强调，该提议正在Fedora论坛上讨论，尚未获得批准，但指出开发者们已经意识到这可能对Steam和Wine产生的影响。

虽然仅支持64位可能会促使Valve加速Steam向完全64位架构的过渡，但作者怀疑能否快速解决。文章还提到了Steam以外的其他应用程序和游戏的复杂性。提出该提议的开发者的一项更新强调了放弃32位支持的必然性，因为它越来越不相关，并且维护起来越来越困难，并建议积极规划至关重要。

评论部分揭示了对游戏的影响、一些用户可能从Fedora迁移以及使用Flatpak Steam作为直接替代方案的局限性的担忧。此外，还有关于Wine是否可以完全弥补缺少32位库的不足以及对Bazzite和OBS游戏捕获等其他项目的影响的讨论。一些评论者主张更快地过渡到64位，而另一些人则担心对现有32位游戏的直接影响。

---

## 50. Excalidraw+ 现已获得 SoC 2 认证

**原文标题**: Excalidraw+ Is Now SoC 2 Certified

**原文链接**: [https://plus.excalidraw.com/blog/excalidraw-soc2](https://plus.excalidraw.com/blog/excalidraw-soc2)

Excalidraw+ 通过 SOC 2 Type I 认证，精简客户安全保障流程，不再只是简单的安全承诺。该公司利用 Vanta 识别并解决合规性差距，实施策略，建立零信任生产访问，升级技术栈并进行渗透测试。尽管已采取强有力的安全措施，但 SOC 2 强制要求正式的文档记录和标准化。

SOC 2 是 AICPA 的一项安全框架，侧重于安全性、可用性、处理完整性、保密性和隐私性。Type I 验证系统和策略是否到位，而 Type II 评估其随时间的有效性。Excalidraw+ 已完成 Type I，并正在努力实现 Type II。

该过程包括将服务与 Vanta 集成、自动化安全工作流程、建立安全工作站策略以及创建全面的安全策略。技术改进包括过渡到 Nx 进行构建管理，使用 Infisical 进行加密密钥管理，设置强大的监控以及增强 CI/CD 管道。

供应商风险管理也至关重要，需要评估供应商的安全实践和认证。该公司使用以隐私为中心的分析工具，如 Umami 和 Simple Analytics。审计由 Insight Assurance 执行。Excalidraw+ 旨在实现 SOC 2 Type II，并正在考虑根据客户需求进行 GDPR 和 ISO 27001 合规性认证。所有相关的安全文档均可在 Excalidraw+ 的信任中心获取。

---

## 51. 研究发现：食品包装脱落的微塑料正在污染我们的食物

**原文标题**: Microplastics shed by food packaging are contaminating our food, study finds

**原文链接**: [https://www.cnn.com/2025/06/24/health/microplastics-food-packaging-study-wellness](https://www.cnn.com/2025/06/24/health/microplastics-food-packaging-study-wellness)

一项新研究表明，食品包装是食物中微塑料和纳米塑料污染的重要来源，正常使用，如打开容器，就会将这些颗粒释放到食物中。研究强调，重复动作，如打开瓶盖、清洗密胺碗，甚至使用塑料涂层金属封口，都会增加食物中微塑料的含量。由于加工步骤增多，超加工食品比最低限度加工食品含有更多的微塑料。

该研究发表在《NPJ食品科学》上，分析了现有研究，并确定了七项高质量的研究证实了这种污染。研究强调了潜在的健康风险，因为纳米塑料可以进入血液，并在全身传播有害化学物质。过去的研究已将微塑料与心脏病、中风和过早死亡联系起来。

除了食品包装外，另一项独立研究发现，在食品的生产和储存过程中，有超过3600种化学物质会渗入食物，其中79种已知会导致严重的健康问题。专家建议，通过选择不锈钢和玻璃容器、避免用塑料容器微波炉加热食物、并注意回收代码来减少塑料的使用。然而，他们强调需要采取系统性行动，敦促个人要求政府干预，以减少塑料的生产和污染。即将在日内瓦举行的全球塑料条约谈判为重大变革提供了一个机会。

---

## 52. 最后生还者2 – 西雅图地点巡礼

**原文标题**: The Last of Us Part II – Seattle Locations Tour

**原文链接**: [https://docs.google.com/document/d/1gfFoe2xVoS9GzmmcbGUjTVVtss1Jwh4Yi-73C6Trn-I/edit?usp=sharing](https://docs.google.com/document/d/1gfFoe2xVoS9GzmmcbGUjTVVtss1Jwh4Yi-73C6Trn-I/edit?usp=sharing)

本文题为《最后生还者2 - 西雅图地点巡礼》，似乎是一篇Google Docs文档，详细介绍了一次与电子游戏《最后生还者2》相关的西雅图地点巡礼。

然而，提供的文本并不完整。它只显示了标题、文档格式信息以及一条需要启用Javascript才能打开文档的提示。

因此，在无法访问文档全部内容的情况下，无法提供关于巡礼中出现的西雅图地点的全面总结或关键信息。 唯一确切的信息是该文档可能提供了有关西雅图中与游戏有关联或受其启发的真实地点的信息。 我们可以推断它可能列出了具体地点，并可能提供了关于它们与游戏的故事、角色或环境的相关性的信息。

---

## 53. 容器现已公测，提供简单且可编程的计算能力。

**原文标题**: Containers are available in public beta for simple, and programmable compute

**原文链接**: [https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/)

Cloudflare 公开了容器的公开测试版，使付费计划用户能够将其容器化应用程序与 Workers 一起运行。此集成提供了一个简单、全球化且可编程的计算环境。开发者只需几行代码即可定义容器，并使用 `wrangler deploy` 将其全局部署，与 Workers 类似。 Workers 和 Containers 可以轻松地在它们之间路由请求，让开发者可以选择合适的工具来完成工作：Workers 用于轻量级和可扩展的任务，而 Containers 用于更强大的功能和灵活性。

容器按需启动并由 Workers 代码控制，无需复杂的 API 调用或 Kubernetes 运营商。本文详细介绍了如何配置容器，包括指定镜像源（Dockerfile 或镜像 URL）、内存、CPU 和磁盘。 `wrangler dev` 支持本地开发，具有自动镜像构建和路由功能。 Cloudflare 还提供内置的可观测性，包括可通过 Cloudflare 仪表板访问的指标和日志。

定价模式是基于使用量的，仅对活动的容器运行时收费（每 10 毫秒），Workers 标准计划中包含每月免费额度。未来的增强功能包括更高的并发实例限制、全局自动缩放、延迟感知路由、增强的 Containers 和 Workers 之间的通信（exec 命令），以及与 Cloudflare 开发者平台其他服务的更深入集成。本文鼓励用户通过部署示例应用程序来试用 Containers。

---

## 54. 时之笛随机化

**原文标题**: Ocarina of Time Randomizer

**原文链接**: [https://ootrandomizer.com/](https://ootrandomizer.com/)

本文介绍了时之笛随机Mod (OoTR)，这是一款修改游戏物品位置的Mod，旨在创造动态且富有挑战性的体验。该随机Mod确保所有种子都能在无故障情况下完成，并避免游戏卡死。

本文重点介绍了其主要功能，包括随机化地牢、宝箱和其他位置的物品，并允许随机化游戏的各个其他方面，例如三角力量碎片、黄金骷髅、Boss和地牢入口，以及商店价格。玩家可以通过各种选项自定义体验，例如大师任务地牢、起始物品、伤害设置，甚至是外观更改。

本文提供了帮助玩家开始使用OoTR的资源，包括设置指南、物品追踪器和无故障逻辑指南。它鼓励用户通过Discord服务器加入活跃的社区，以获得支持、参与竞速和进行讨论。本文提及了各种竞速社区和内容创作者，例如The Silver Gauntlets、ZeldaSpeedRuns和Scrubs Central。该随机Mod正在积极开发中，最新消息、播客和挑战种子会定期更新。对于那些对最新进展感兴趣的人，本文提供了GitHub存储库和开发者分支的链接。

---

## 55. 我是如何使用终端的

**原文标题**: How I use my terminal

**原文链接**: [https://jyn.dev/how-i-use-my-terminal/](https://jyn.dev/how-i-use-my-terminal/)

此博文详细介绍了作者围绕 tmux 构建的高度定制化的终端工作流，以提高效率并减少编辑器延迟。由于对 VSCode 的性能和快捷键冲突感到沮丧，他们转而使用终端中的 nvim，并开发了脚本来简化文件导航和打开。

该设置的核心是使用 tmux 搜索终端回滚以查找文件名，然后在 nvim 中打开所选文件。关键方面包括用于文件名识别的复杂正则表达式、用于在默认应用程序或 nvim 中打开文件的脚本，以及另一个使用 tmux 发送命令以在现有 nvim 实例中打开文件的脚本。

作者认为，这种设置使他们能够避免本地克隆、编写终端脚本并高效地进行调试。虽然承认其自定义脚本的脆弱性，但他们发现诸如减少编辑器延迟和保持一致的快捷键等好处是值得的。

尽管提倡这种方法，但他们承认其复杂性使其不适合大多数用户。他们推荐 fish + zoxide + fzf 等替代方案以及 `qf` 和 `e` 等工具，以便在没有大量脚本的情况下实现类似的功能。他们还指出他们计划迁移到 kitty 以减少开销，并且该帖子最后强调了终端未被挖掘的力量以及使用编辑器特定工具复制这些功能的可能性，尽管这会导致编辑器锁定。作者邀请读者分享他们自己的设置。

---

## 56. GitHub CEO：尽管人工智能蓬勃发展，手动编码仍然是关键。

**原文标题**: GitHub CEO: manual coding remains key despite AI boom

**原文链接**: [https://www.techinasia.com/news/github-ceo-manual-coding-remains-key-despite-ai-boom](https://www.techinasia.com/news/github-ceo-manual-coding-remains-key-despite-ai-boom)

GitHub CEO: 尽管人工智能蓬勃发展，手动编码仍然是关键

---

## 57. uv: 一个用 Rust 编写的极速 Python 包和项目管理器

**原文标题**: uv: An extremely fast Python package and project manager, written in Rust

**原文链接**: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

uv: 用 Rust 构建的极速 Python 包和项目管理器

---

## 58. 我将 pigz 从 Unix 移植到了 Windows。

**原文标题**: I ported pigz from Unix to Windows

**原文链接**: [https://blog.kowalczyk.info/article/4/how-i-ported-pigz-from-unix-to-windows.html](https://blog.kowalczyk.info/article/4/how-i-ported-pigz-from-unix-to-windows.html)

本文详细介绍了作者将 Unix 命令行工具 pigz 移植到 Windows 的经验。作者强调，pigz 最初是为 Unix 系统设计的，缺乏跨平台考虑。然而，由于存在针对常见 Unix 依赖项的预先存在的兼容层，这项任务得以简化。

主要挑战通过使用 Windows 的 pthreads 实现和 Windows 端口的 dirent API（用于目录读取）来解决。函数名称上的细微差异（例如，`stat` 与 `_stat`）和缺失的类型定义（`ssize_t`、`PATH_MAX`）通过 `#define` 语句和 typedef 来解决，所有这些都整合到一个 `wincompat.h` 头文件中。Unix 特定的头文件使用 `#ifndef _WIN32` 从 Windows 构建中排除。

本文还重点介绍了使用 Premake 生成 Visual Studio 项目文件。Premake 允许作者避免手动创建和维护项目文件这一耗时的过程，特别是对于多个 Visual Studio 版本。作者赞扬 Premake 在定义项目配置方面的易用性，以及它生成适用于最新 Visual Studio 版本的项目文件的能力。

作者总结说，由于现有的兼容层，移植过程相对简单，并强调了 Premake 在管理 Visual Studio 项目方面的实用性。他们还提到了他们的其他软件项目，Edna 和 SumatraPDF。

---

## 59. 坦迪公司，第一部分 – 布拉德福德·摩根·怀特 著

**原文标题**: The Tandy Corporation, Part 1 – By Bradford Morgan White

**原文链接**: [https://www.abortretry.fail/p/the-tandy-corporation-part-1](https://www.abortretry.fail/p/the-tandy-corporation-part-1)

本文《坦迪公司，第一部分》追溯了该公司从1919年作为欣克利-坦迪皮革公司成立到1977年发布TRS-80电脑的历史。

最初专注于皮革鞋材，该公司在查尔斯·大卫·坦迪的领导下扩展到邮购爱好部门和零售商店。大卫·刘易斯·坦迪去世后，坦迪面临财务困境，于1955年与美国皮革公司（AHLC）合并，最终重新获得控制权，并于1959年将公司更名为坦迪公司。

坦迪随后多元化经营，涉足包括电子产品在内的其他零售业务，并于1963年以30万美元收购了Radio Shack。坦迪精简了Radio Shack的库存，专注于自有品牌产品，并通过利润分享和股权激励店长。该公司拓展了国际业务，于1973年在比利时和英国开设了门店。

本文详细介绍了TRS-80微型计算机的开发过程。唐·弗兰奇和史蒂夫·莱宁格认识到微型计算机的潜力，开发了一个最初受到质疑的原型。尽管最初存在疑虑，坦迪还是批准了生产，最终于1977年发布了TRS-80 Model I。发布当天，纽约市发生了恐怖袭击，发布活动因此黯然失色，但该产品的发布仍然取得了成功。文章最后强调了对TRS-80的意外需求。

---

## 60. 贝佐斯无容身之地运动：“一人租下一座城市三天？”

**原文标题**: The No Space for Bezos movement: 'One man rents a city for three days? '

**原文链接**: [https://www.theguardian.com/technology/2025/jun/24/inside-the-no-space-for-bezos-movement-one-man-rents-a-city-for-three-days-thats-obscene](https://www.theguardian.com/technology/2025/jun/24/inside-the-no-space-for-bezos-movement-one-man-rents-a-city-for-three-days-thats-obscene)

这篇文章聚焦于意大利威尼斯“贝佐斯没地儿”运动，该运动抗议杰夫·贝佐斯婚礼庆典，原因是人们认为他的财富过于炫耀，并对威尼斯及其更广泛的社会造成了影响。这场运动由反法西斯主义、反资本主义和环保人士组成，旨在打破围绕该活动的奢华和名人叙事，凸显过度旅游、住房短缺、气候变化以及亚马逊对当地企业造成的有害影响等问题。

活动人士组织了公开示威活动，包括展开横幅谴责贝佐斯，并计划阻止进入计划中的派对场地。他们认为，贝佐斯的出现代表着更广泛的、不受约束的亿万富翁权力及其对当地社区漠视的问题。

文章详细介绍了该运动的担忧，即威尼斯正被当作一个主题公园来对待，以牺牲其居民和文化完整性为代价，迎合游客和富人的需求。活动人士还将贝佐斯的商业行为、对特朗普的支持以及数字资本主义与专制倾向相结合的更广泛趋势联系起来。该运动的目的是将焦点从贝佐斯的财富转移到它所代表的结构性问题上，并引发对亿万富翁作为一种影响生活的力量的更广泛批判。尽管有报道称贝佐斯已更换派对场地，但该运动强调，即使是亿万富翁也无法在威尼斯这样的城市购买善意或避免异议。

---

## 61. 美国的预期寿命低于大多数相似的富裕国家。

**原文标题**: The United States has lower life expectancy than most similarly wealthy nations

**原文链接**: [https://www.nature.com/articles/d41586-025-01969-1](https://www.nature.com/articles/d41586-025-01969-1)

这篇《自然》杂志的文章探讨了美国医疗支出最高，但预期寿命却低于其他富裕国家的令人担忧的趋势。文章强调，尽管新任卫生与公众服务部部长小罗伯特·肯尼迪承认慢性病问题，但他对疫苗和超加工食品的关注忽略了导致美国人过早死亡的其他重要因素，例如交通事故、药物过量和枪支暴力，而美国在这些方面明显是异常值。

文章指出，数据显示美国出生时预期寿命为78.4岁，远低于可比国家的平均水平。新冠疫情加剧了这一差距，尤其是在15-49岁年龄段。虽然心脏病、癌症、中风和呼吸道疾病等慢性病是重要原因，但研究人员强调了药物滥用（特别是阿片类药物过量）、交通事故和与枪支相关的死亡的影响。

文章还指出，美国在健康预期寿命方面存在差距，且缺乏全民医保，这阻碍了早期诊断和治疗。虽然癌症筛查和积极治疗改善了癌症治疗效果，但对于肥胖症、糖尿病和心血管疾病等其他疾病，也需要同样程度的重视。总而言之，这篇文章描绘了导致美国健康挑战的各种复杂因素，并表明除了小罗伯特·肯尼迪目前关注的重点之外，还需要采取更广泛、更全面的方法。

---

## 62. 新生儿体内阿尔茨海默症生物标志物水平偏高

**原文标题**: Newborns have elevated levels of a biomarker for Alzheimer's

**原文链接**: [https://medicalxpress.com/news/2025-06-newborns-elevated-biomarker-alzheimer.html](https://medicalxpress.com/news/2025-06-newborns-elevated-biomarker-alzheimer.html)

该文章报道了哥德堡大学研究人员发表在《大脑通讯》上的一项研究，该研究发现新生儿体内p-tau217水平升高，而p-tau217通常与阿尔茨海默病相关。该研究分析了包括新生儿、成人和阿尔茨海默病患者在内的400多名个体的血液样本，结果显示，新生儿，尤其是早产儿，其p-tau217水平甚至高于阿尔茨海默病患者。

虽然阿尔茨海默病患者体内p-tau217水平升高表明tau蛋白聚集和脑细胞损伤，但在新生儿体内，它似乎在健康的大脑发育中起着至关重要的作用。tau蛋白的激增有助于神经元生长并形成连接，从而塑造发育中的大脑。其水平也与胎龄有关，早产儿的水平较高，表明它在快速大脑生长中起着支持作用。

研究人员认为，了解新生儿如何在没有阿尔茨海默病患者所见的有害影响的情况下耐受高水平的磷酸化tau蛋白，可以为新的治疗方法提供路线图。模仿新生儿的天然保护机制，有可能减缓或阻止阿尔茨海默病的进展。该研究强调了理解p-tau217升高的潜在机制的重要性，尤其是考虑到它在阿尔茨海默病诊断中日益广泛的应用。研究结果表明，淀粉样蛋白斑块可能不是p-tau217升高的主要驱动因素，为研究和治疗开辟了新的途径。

---

## 63. 铁甲骑兵：中世纪奇幻角色扮演兵棋推演，背景设定于公元1300年左右的黑海地区

**原文标题**: Cataphract: Medieval-fantasy roleplaying wargame, in the Black-Sea C. 1300

**原文链接**: [https://samsorensen.blot.im/cataphracts-design-diary-1](https://samsorensen.blot.im/cataphracts-design-diary-1)

这篇设计日志详述了“重装骑兵”(Cataphract)，一款以1300年黑海周边为背景的中世纪幻想角色扮演战争游戏，侧重于作战层面的战争——后勤、通讯和调动——而非仅仅是战略或战术。该游戏是异步的、帖子形式的、实时的，这意味着命令通过Discord下达并在实时追踪，同时会考虑行军和通讯延误。

主要特性包括：

*   **指挥结构：** 一个分层指挥系统，指挥官可以任命半独立运作的下属，主要通过缓慢的信使进行沟通。
*   **战争迷雾：** 有限且经常不准确的信息，造成“信息滞后”并使协调变得困难。指挥官只能知道他们的侦察兵看到的东西，或通过信件收到的信息。
*   **五个阵营：** 每个阵营都具有独特的特征和特殊部队：诺万帝国（拜占庭人），萨卡尔齐亚神权主教区（东正教教皇国），兹兰尼克公国（基辅罗斯），第三瓦尔加王国（波各米尔派保加利亚人）和卡尔汗国（伊儿汗国）。
*   **强调后勤：** 补给、天气和行军时间严重影响作战。
*   **意外结果：** 简单的计划往往会成功，因为复杂的协调非常困难。玩家由于依赖上级提供信息和指示，因此对上级非常忠诚。联盟经常因为后勤和沟通不畅而失败。
* 随机生成的角色导致复杂的人际关系。

作者强调，游戏难度源于永远无法清晰了解局势，这使得作战情报成为至关重要的资源。

---

## 64. 2025伊比利亚半岛停电报告 [pdf]

**原文标题**: 2025 Iberia Blackout Report [pdf]

**原文链接**: [https://media.licdn.com/dms/document/media/v2/D4D1FAQGcyyYYrelkNg/feedshare-document-pdf-analyzed/B4DZeBtlohGsAk-/0/1750227910090?e=1750896000&v=beta&t=uEftse3BPsTjdLQ3DmjoVkadhUGqf7-MfYj_6UnSS28](https://media.licdn.com/dms/document/media/v2/D4D1FAQGcyyYYrelkNg/feedshare-document-pdf-analyzed/B4DZeBtlohGsAk-/0/1750227910090?e=1750896000&v=beta&t=uEftse3BPsTjdLQ3DmjoVkadhUGqf7-MfYj_6UnSS28)

很抱歉，我无法总结这个PDF文件。文件内的文字似乎经过编码，我无法访问要点和关键信息以进行概括。

---

## 65. 当工作不在乎你时，如何关怀你的工作

**原文标题**: How to Care About Your Job When It Doesn't Care About You

**原文链接**: [https://matthogg.fyi/how-to-care-about-your-job-when-it-doesnt-care-about-you/](https://matthogg.fyi/how-to-care-about-your-job-when-it-doesnt-care-about-you/)

当雇佣关系本质上不平等，且组织机构（“公司”）似乎对个人福祉漠不关心时，本文探讨如何保持工作投入度和从中获得满足感。

作者认为，组织机构优先考虑自身目标（利润、服务等），而非个人需求，导致次优决策和“只是一个项目”的感觉。他们揭穿了组织机构是一个理性、有凝聚力的实体的神话，而是将其描述为一个容易出现功能失调的“集体”，有时甚至会采取诸如强制排名、随意裁员和“重返办公室”等公然的剥削性做法。

解决办法不是辞职，而是转变重心。本文倡导关注你的“影响力圈子”——经理、下属和同事——并优化这些局部关系。成为你经理的盟友，对下属实行服务型领导，并与团队成员培养友谊。

至关重要的是，它强调在你的“控制圈子”内设定个人界限，避免过度志愿工作，并认识到额外工作往往不会受到组织的赏识。任何额外工作都应该为了个人利益（技能提升、工作流程改进）或直接造福你的直属团队。

最后，本文提倡持续、随意的求职，作为自我保护、内省和保持自主意识的一种手段。这种积极主动的方法提供了选择并增强了信心，最终在往往非个性化的工作环境中赋予个人权力。

---

## 66. 谷歌发布用于翻译和语言服务供应商的设备端手语模型

**原文标题**: Google Unveils On-Device Sign Language Model for Translators and LSPs

**原文链接**: [https://multilingual.com/google-signgemma-on-device-asl-translation/](https://multilingual.com/google-signgemma-on-device-asl-translation/)

好的，以下是我预期multilingual.com上的文章“谷歌发布用于翻译和LSP的设备端手语模型”将涵盖的摘要：

谷歌宣布推出SignGemma，一种新的设备端美国手语(ASL)模型，旨在增强听障人士的无障碍访问并提高翻译能力。与以往基于云的解决方案不同，SignGemma直接在设备（例如智能手机）上处理手语，无需互联网连接并减少延迟，这对实时通信至关重要。

这项技术与语言服务提供商(LSP)和翻译人员尤其相关，为他们提供了一个强大的工具来集成到他们的工作流程中。通过启用设备端翻译，SignGemma增强了隐私和安全性，因为视频数据保留在用户的设备上。预计的优势是更高效、更具成本效益的手语翻译服务。

SignGemma建立在Gemma开放模型系列之上。这使开发人员能够针对特定应用程序和区域方言微调和定制模型，从而有助于实现更个性化和准确的翻译体验。

部署像SignGemma这样的设备端模型旨在弥合沟通鸿沟，并促进聋人在教育、医疗保健和日常生活等各种场景中的无缝互动。这篇文章可能强调SignGemma在普及手语翻译和提高聋人整体生活质量方面的潜力。该公告强调了谷歌致力于利用人工智能造福社会，并通过技术创新促进包容性。

---

## 67. US safety regulators contact Tesla over erratic robotaxis

**原文标题**: US safety regulators contact Tesla over erratic robotaxis

**原文链接**: [https://www.bbc.com/news/articles/cg75zv4gny2o](https://www.bbc.com/news/articles/cg75zv4gny2o)

The U.S. National Highway Traffic Safety Administration (NHTSA) has contacted Tesla after social media footage showed its newly-launched robotaxis in Austin, Texas appearing to break traffic laws and drive erratically. Tesla's long-awaited robotaxis, deemed crucial by Elon Musk, were tested on public roads with a safety driver present.

Videos online suggest instances of abrupt stops and other driving errors. The NHTSA confirmed it's aware of the incidents and is gathering information from Tesla. The launch was low-key, with a limited number of analysts, influencers, and shareholders participating in paid rides.

TechCrunch reported observations of speeding and swerving into the wrong lane. The initial rollout is limited to 12 taxis with operational restrictions including weather conditions, difficult intersections and customer age.

Analysts believe the small scale launch proves Tesla still has a long way to go to compete with rivals like Waymo and Zoox, who already operate self-driving taxi services in multiple cities.

Tesla is using a camera-based approach, differing from the radar and sensor-based systems used by competitors, banking on cost-effectiveness. Questions about the safety of Tesla's technology have been raised. The NHTSA doesn't pre-approve technologies but investigates potential safety defects.


---

## 68. BYOK – Bring Your Own Keyboard

**原文标题**: BYOK – Bring Your Own Keyboard

**原文链接**: [https://byok.io](https://byok.io)

生成摘要时出错

---

## 69. Transparent Ambition

**原文标题**: Transparent Ambition

**原文链接**: [https://take.surf/2025/06/19/transparent-ambition](https://take.surf/2025/06/19/transparent-ambition)

生成摘要时出错

---

## 70. SourceHut moves business operations from US to Europe

**原文标题**: SourceHut moves business operations from US to Europe

**原文链接**: [https://lists.sr.ht/~sircmpwn/sr.ht-dev/patches/60282](https://lists.sr.ht/~sircmpwn/sr.ht-dev/patches/60282)

生成摘要时出错

---

## 71. Removal of unwanted drivers from Windows Update

**原文标题**: Removal of unwanted drivers from Windows Update

**原文链接**: [https://techcommunity.microsoft.com/blog/hardwaredevcenter/removal-of-unwanted-drivers-from-windows-update/4425647](https://techcommunity.microsoft.com/blog/hardwaredevcenter/removal-of-unwanted-drivers-from-windows-update/4425647)

生成摘要时出错

---

## 72. Nano-Vllm: Lightweight vLLM implementation built from scratch

**原文标题**: Nano-Vllm: Lightweight vLLM implementation built from scratch

**原文链接**: [https://github.com/GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm)

生成摘要时出错

---

## 73. PBKDF2 JS Lib: Improper Input Validation Vulnerability

**原文标题**: PBKDF2 JS Lib: Improper Input Validation Vulnerability

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-6545](https://nvd.nist.gov/vuln/detail/CVE-2025-6545)

生成摘要时出错

---

## 74. Comparison of Android-Based Operating Systems

**原文标题**: Comparison of Android-Based Operating Systems

**原文链接**: [https://eylenburg.github.io/android_comparison.htm](https://eylenburg.github.io/android_comparison.htm)

生成摘要时出错

---

## 75. Making TRAMP faster

**原文标题**: Making TRAMP faster

**原文链接**: [https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./](https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./)

生成摘要时出错

---

## 76. Homotopy Equivalences

**原文标题**: Homotopy Equivalences

**原文链接**: [https://bartoszmilewski.com/2025/06/20/weak-homotopy-equivalences/](https://bartoszmilewski.com/2025/06/20/weak-homotopy-equivalences/)

生成摘要时出错

---

## 77. Fedora 44 Looks to Drop I686 Support: No More Multi-Lib / x86 32-Bit Packages

**原文标题**: Fedora 44 Looks to Drop I686 Support: No More Multi-Lib / x86 32-Bit Packages

**原文链接**: [https://www.phoronix.com/news/Fedora-43-Change-No-i686](https://www.phoronix.com/news/Fedora-43-Change-No-i686)

生成摘要时出错

---

## 78. Breakthrough cancer test predicts whether chemotherapy will work

**原文标题**: Breakthrough cancer test predicts whether chemotherapy will work

**原文链接**: [https://www.telegraph.co.uk/news/2025/06/23/cancer-test-predicts-whether-chemotherapy-will-work/](https://www.telegraph.co.uk/news/2025/06/23/cancer-test-predicts-whether-chemotherapy-will-work/)

生成摘要时出错

---

## 79. WhatsApp banned on House staffers' devices

**原文标题**: WhatsApp banned on House staffers' devices

**原文链接**: [https://www.axios.com/2025/06/23/whatsapp-house-congress-staffers-messaging-app](https://www.axios.com/2025/06/23/whatsapp-house-congress-staffers-messaging-app)

生成摘要时出错

---

## 80. Show HN: Pickaxe – A TypeScript library for building AI agents

**原文标题**: Show HN: Pickaxe – A TypeScript library for building AI agents

**原文链接**: [https://github.com/hatchet-dev/pickaxe](https://github.com/hatchet-dev/pickaxe)

生成摘要时出错

---

## 81. New Linux udisks flaw lets attackers get root on major Linux distros

**原文标题**: New Linux udisks flaw lets attackers get root on major Linux distros

**原文链接**: [https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/](https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/)

生成摘要时出错

---

## 82. Interesting Bits of Postgres Grammar

**原文标题**: Interesting Bits of Postgres Grammar

**原文链接**: [https://steve.dignam.xyz/2025/06/20/interesting-bits-of-postgres-grammar/](https://steve.dignam.xyz/2025/06/20/interesting-bits-of-postgres-grammar/)

生成摘要时出错

---

## 83. NASA's Voyager Found a 30k-50k Kelvin "Wall" at the Edge of Solar System

**原文标题**: NASA's Voyager Found a 30k-50k Kelvin "Wall" at the Edge of Solar System

**原文链接**: [https://www.iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-79454](https://www.iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-79454)

生成摘要时出错

---

## 84. Rocknix is an immutable Linux distribution for handheld gaming devices

**原文标题**: Rocknix is an immutable Linux distribution for handheld gaming devices

**原文链接**: [https://rocknix.org/](https://rocknix.org/)

生成摘要时出错

---

## 85. Open source Ethernet switch – part 2

**原文标题**: Open source Ethernet switch – part 2

**原文链接**: [https://serd.es/2025/06/23/Switch-project-pt2.html](https://serd.es/2025/06/23/Switch-project-pt2.html)

生成摘要时出错

---

## 86. Polystate: Composable Finite State Machines

**原文标题**: Polystate: Composable Finite State Machines

**原文链接**: [https://github.com/sdzx-1/polystate](https://github.com/sdzx-1/polystate)

生成摘要时出错

---

## 87. Show HN: Luna Rail – Treating night trains as a spatial optimization problem

**原文标题**: Show HN: Luna Rail – Treating night trains as a spatial optimization problem

**原文链接**: [https://luna-rail.com/en/home-2](https://luna-rail.com/en/home-2)

生成摘要时出错

---

## 88. Mmc-Utils 1.0 Released for Managing MMC Storage on Linux

**原文标题**: Mmc-Utils 1.0 Released for Managing MMC Storage on Linux

**原文链接**: [https://www.phoronix.com/news/mmc-utils-1.0](https://www.phoronix.com/news/mmc-utils-1.0)

生成摘要时出错

---

## 89. Remote MCP Support in Claude Code

**原文标题**: Remote MCP Support in Claude Code

**原文链接**: [https://www.anthropic.com/news/claude-code-remote-mcp?campaignId=13926158&source=i_email&medium=email&content=Oct2024AnalysisTool&messageTypeId=140367](https://www.anthropic.com/news/claude-code-remote-mcp?campaignId=13926158&source=i_email&medium=email&content=Oct2024AnalysisTool&messageTypeId=140367)

生成摘要时出错

---

## 90. Phoenix.new – Remote AI Runtime for Phoenix

**原文标题**: Phoenix.new – Remote AI Runtime for Phoenix

**原文链接**: [https://fly.io/blog/phoenix-new-the-remote-ai-runtime/](https://fly.io/blog/phoenix-new-the-remote-ai-runtime/)

生成摘要时出错

---

## 91. Judge denies creating “mass surveillance program” harming all ChatGPT users

**原文标题**: Judge denies creating “mass surveillance program” harming all ChatGPT users

**原文链接**: [https://arstechnica.com/tech-policy/2025/06/judge-rejects-claim-that-forcing-openai-to-keep-chatgpt-logs-is-mass-surveillance/](https://arstechnica.com/tech-policy/2025/06/judge-rejects-claim-that-forcing-openai-to-keep-chatgpt-logs-is-mass-surveillance/)

生成摘要时出错

---

## 92. How fast are Linux pipes anyway?

**原文标题**: How fast are Linux pipes anyway?

**原文链接**: [https://mazzo.li/posts/fast-pipes.html](https://mazzo.li/posts/fast-pipes.html)

生成摘要时出错

---

## 93. Using Wave Function Collapse to solve puzzle map generation at scale

**原文标题**: Using Wave Function Collapse to solve puzzle map generation at scale

**原文链接**: [https://sublevelgames.github.io/blogs/2025-06-22-nurikabe-map-gen-with-wfc/](https://sublevelgames.github.io/blogs/2025-06-22-nurikabe-map-gen-with-wfc/)

生成摘要时出错

---

## 94. Using Home Assistant, adguard home and an $8 smart outlet to avoid brain rot

**原文标题**: Using Home Assistant, adguard home and an $8 smart outlet to avoid brain rot

**原文链接**: [https://www.romanklasen.com/blog/beating-brainrot-by-button/](https://www.romanklasen.com/blog/beating-brainrot-by-button/)

生成摘要时出错

---

## 95. Minimal Boolean Formulas (2011)

**原文标题**: Minimal Boolean Formulas (2011)

**原文链接**: [https://research.swtch.com/boolean](https://research.swtch.com/boolean)

生成摘要时出错

---

## 96. Python can run Mojo now

**原文标题**: Python can run Mojo now

**原文链接**: [https://koaning.io/posts/giving-mojo-a-spin/](https://koaning.io/posts/giving-mojo-a-spin/)

生成摘要时出错

---

## 97. The X Window System didn't immediately have X terminals

**原文标题**: The X Window System didn't immediately have X terminals

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate](https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate)

生成摘要时出错

---

## 98. RaptorCast: Designing a Messaging Layer

**原文标题**: RaptorCast: Designing a Messaging Layer

**原文链接**: [https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer](https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer)

生成摘要时出错

---

## 99. ESA Biomass satellite returns striking first images of forest

**原文标题**: ESA Biomass satellite returns striking first images of forest

**原文链接**: [https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/Biomass_satellite_returns_striking_first_images_of_forests_and_more](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/Biomass_satellite_returns_striking_first_images_of_forests_and_more)

生成摘要时出错

---

## 100. We’ve had a Denisovan skull since the 1930s, only nobody knew

**原文标题**: We’ve had a Denisovan skull since the 1930s, only nobody knew

**原文链接**: [https://arstechnica.com/science/2025/06/the-controversial-dragon-man-skull-was-a-denisovan/](https://arstechnica.com/science/2025/06/the-controversial-dragon-man-skull-was-a-denisovan/)

生成摘要时出错

---

