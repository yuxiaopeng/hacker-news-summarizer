# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-06.md)

*最后自动更新时间: 2026-06-06 18:37:49*
## 1. Zeroserve：一款支持 eBPF 脚本编写的零配置 Web 服务器

**原文标题**: Zeroserve: A zero-config web server you can script with eBPF

**原文链接**: [https://su3.io/posts/introducing-zeroserve](https://su3.io/posts/introducing-zeroserve)

**Zeroserve** 是一款高性能、零配置的 HTTPS 服务器，旨在通过脚本化的 **eBPF 程序**取代传统的声明式配置。它的开发初衷是简化 Web 服务和中间件管理，将路由、身份验证和限流整合进单个、易读的 C 语言脚本中，并运行在用户态沙盒内。

### 核心特性与架构：
*   **eBPF 脚本化：** Zeroserve 弃用复杂的配置文件，转而使用通过用户态 JIT (async-ebpf) 编译为原生代码的 eBPF 程序。这些脚本通过“指针笼 (pointer cage)”和抢占定时器进行沙盒化隔离，确保其安全性的同时，避免阻塞服务器的事件循环。
*   **部署：** 整个网站被打包成单个 **tar 压缩包**。服务器会对该压缩包建立索引，并直接利用字节范围读取提供文件服务，无需解压至磁盘。更新过程是原子性的，仅需更换文件并发送 `SIGHUP` 信号即可实现热重载。
*   **I/O 与性能：** 基于 `io_uring` 构建，Zeroserve 采用单线程设计，效率极高。基准测试显示，在处理小型静态文件时，其性能优于 Nginx 约 17%；在小响应代理方面优于 Nginx 约 22%。尽管在处理大型代理包体时略逊于 Nginx，但在大多数工作负载下仍显著快于 Caddy。
*   **高级传输安全：** 原生支持 TLS 1.3、HTTP/2 和加密客户端问候 (ECH)，并集成 JA4 客户端指纹识别。
*   **内置功能：** 脚本可调用广泛的辅助接口，包括 OIDC 登录流、AWS SigV4 签名、JSON 转换以及令牌桶限流。

### 结论：
Zeroserve 的设计赌注在于“程序即配置”。通过将逻辑移至统一的沙盒脚本层，并利用现代 Linux I/O 原语，它为那些追求可编程请求路径、又不愿承担 Lua 等外部运行时开销的开发者，提供了一个比 Nginx 和 Caddy 更快、更可预测的替代方案。

---

## 2. 英伟达正提议为 Windows PC 打造一款性能怪兽级的 CPU 系统。

**原文标题**: Nvidia is proposing a beast of a CPU system for Windows PCs

**原文链接**: [https://twitter.com/lemire/status/2062880075117113739](https://twitter.com/lemire/status/2062880075117113739)

提供的文本不包含实际文章；这是一条来自 X（原 Twitter）的错误消息，提示 JavaScript 已禁用。由于文章内容未能加载，无法对该特定文本进行摘要。

然而，根据标题及当前的行业动态，该文章可能指向英伟达（Nvidia）传闻中计划为 Windows PC 推出高性能 ARM 架构 CPU 的消息。以下是围绕该主题的相关背景摘要：

**主题摘要：**
据报道，英伟达正在开发一款专为运行 Windows 设计的强大消费级 CPU，这标志着 PC 硬件格局的重大转变。虽然英伟达在 GPU 和 AI 服务器市场占据主导地位，但此举将使其在处理器领域与英特尔（Intel）、AMD 和高通（Qualcomm）展开直接竞争。

有关该提案的关键点包括：
*   **ARM 架构：** 继苹果 M 系列芯片和高通骁龙 X Elite 取得成功后，该系统预计将基于 ARM 技术。
*   **高性能：** 该系统被冠以“性能怪兽”之名，预计将优先考虑高端性能，可能会将英伟达先进的 Blackwell 或未来的 GPU 架构直接与处理器集成，以提供卓越的游戏和 AI 能力。
*   **AI PC 集成：** 这一时机契合了微软对“AI PC”的推动，英伟达在本地 AI 处理方面的专业优势可能会使其相比传统 x86 处理器更具显著竞争力。
*   **目标市场：** 该系统可能面向高端笔记本电脑和高性能台式机，最早可能在 2025 年或 2026 年发布。

如需获取完整详情，您需要在启用 JavaScript 的浏览器中查看原始帖子。

---

## 3. 超越 fork() + exec()

**原文标题**: Moving beyond fork() + exec()

**原文链接**: [https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/](https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/)

本文探讨了 Linux 社区为实现进程创建现代化而做出的持续努力，旨在超越传统的 `fork()` 和 `exec()` 模型。

虽然 `fork()` 和 `exec()` 模式是类 Unix 系统的基石，但它正日益被视为低效。`fork()` 非常耗费资源，因为它需要复制父进程的全部状态，而这些状态往往会在随后的 `exec()` 调用中被立即丢弃。

开发者 Li Chen 最近提出了“生成模板”（spawn templates）来解决这些效率问题，特别是针对需要重复启动相同可执行文件（如 Git）的应用。该 API 允许内核通过 `spawn_template_create()` 缓存可执行文件信息，然后使用 `spawn_template_spawn()` 启动进程。虽然基准测试显示性能提升了 2%，但内核维护者认为该提议在解决 `fork()` 根本性开销方面做得还不够。

包括 Christian Brauner 和 Mateusz Guzik 在内的评审人员建议，内核不应仅停留在优化父进程的复制过程，而应转向从头开始创建“纯净”（pristine）进程。Brauner 提议利用现有的 `pidfd` 抽象构建一个“生成器 API”（builder API）。在该模型中，开发者将先使用 `pidfd_open()` 创建一个空进程，然后通过新的 `pidfd_config()` 系统调用来配置其环境、文件描述符和可执行映像。

最终，Chen 的“生成模板”不会以当前形式被合并。然而，讨论已转向开发一种不依赖于传统 `fork()`/`exec()` 开销的、原生且高效的 `posix_spawn()` 实现。这一路径有望为未来 Linux 内核提供更简洁、更快速的进程创建原语。

---

## 4. 莱比锡基准

**原文标题**: Benchmarks in Leipzig

**原文链接**: [https://arxiv.org/abs/2606.05818](https://arxiv.org/abs/2606.05818)

文章《莱比锡基准》（Benchmarks in Leipzig，arXiv:2606.05818）详细阐述了一个旨在测试人工智能在高阶数学领域极限的新数据集的创建过程。该数据集由49位数学家在2026年马克斯·普朗克数学科学研究所举行的一次研讨会上合作编制，包含100道带有经验证答案的研究级数学问题。

研究人员通过三个日益严苛的阶段，评估了最先进的大型语言模型（LLM）在这些基准上的表现：

1.  **第一阶段：** 五种模型对每道题仅进行一次尝试，有41道题未能解决。
2.  **第二阶段：** 其中三种模型对每道题各进行20次尝试，未解决的问题数量降至16道。
3.  **第三阶段：** 两种“深度思考”模型各进行三次尝试，最终仅剩**两道**问题未能解决。

作者总结认为，LLM的数学推理能力已达到“令人印象深刻”的水平，因为它们现在能够解决几乎所有专门用于挑战研究级数学直觉的问题。该论文对数学史与综述、人工智能以及多个专业数学学科领域做出了贡献。

---

## 5. 你可以跑

**原文标题**: You Can Run

**原文链接**: [https://magazine.atavist.com/2026/mccann-cocaine-fugitives](https://magazine.atavist.com/2026/mccann-cocaine-fugitives)

在《你可以跑》（You Can Run）中，调查记者巴里·迈耶（Barry Meier）探讨了一个看似完美的美国精英家庭的崩坏。1984年，艾琳（Erin）和梅雷迪思·麦肯（Meredith McCann）被迫离开了她们在宾夕法尼亚州福克斯查珀尔（Fox Chapel）的优渥生活，沦为国际逃犯。她们的父亲约翰·H·麦肯三世（John H. McCann III）是一个富有魅力但极具控制欲的人，他声称全家潜逃是因为与美国国税局（IRS）的一场误会。而事实却是，约翰是一个惯性骗子，他伪造学历，在担任市长和法官期间因丑闻引咎辞职，并卷入了欺诈性的煤矿投资和避税陷阱。

在随后的18个月里，这家人隐姓埋名，辗转于全球各地，住在马略卡岛的豪华别墅和伦敦的高档酒店里。尽管女孩们就读于名校，过着逃亡者的“黄金时代”，但她们不得不隐瞒真实身份，并永远切断了与朋友的联系。父母对犯罪真相始终保持沉默，这种沉默一直持续到女儿们成年。

故事的框架是一场现代的“时间竞赛”：现为律师的艾琳得知母亲莉娅终于决定处理掉两箱详述家族犯罪往事的政府记录，于是火速赶往位于宾夕法尼亚州约克的母亲家中。艾琳希望通过从垃圾堆中抢救出这些文件，最终揭开那些摧毁她童年并让全家遁入阴影的往事真相。这个故事深刻地审视了父母的欺瞒、身份的脆弱，以及建立在秘密之上的生活所带来的长久创伤。

---

## 6. 谷歌将每月向SpaceX支付9.2亿美元购买算力

**原文标题**: Google will pay SpaceX $920M per month for compute

**原文链接**: [https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/)

谷歌已与 SpaceX 达成一项巨额协议，将在 2026 年 10 月至 2029 年 6 月期间，每月向后者支付 9.2 亿美元以获取 AI 算力。根据协议条款，谷歌将获得约 11 万块英伟达 GPU 及相关组件的使用权。

该交易的规模与 SpaceX 最近同 Anthropic 达成的每月 12.5 亿美元的协议相仿。尽管谷歌已是全球 AI 基础设施领域的领导者，但其代表将此次交易描述为一项“短期、及时的协议”，旨在为其 Gemini 企业版和智能体平台激增的需求提供“过渡容量”。此举正值谷歌母公司 Alphabet 大力扩张资本支出之际，预计其今年资本支出将超过 1800 亿美元。

合同包含一项于 2026 年 12 月 31 日后生效的 90 天取消条款。SpaceX 必须在 2026 年 9 月 30 日之前交付硬件，否则将面临合同终止或费用削减的风险。

该消息在 SpaceX 预计于纳斯达克上市的一周前发布。该公司正寻求约 1.75 万亿美元的历史性估值。作为 SpaceX 的长期投资者，谷歌持有的股份价值在 IPO 后预计将超过 1000 亿美元。除硬件租赁外，据报道，两家公司还在讨论开发轨道数据中心，作为 SpaceX 长期增长战略的一部分。

---

## 7. 《宝可梦 绿宝石》移植至 WebAssembly（帧率达 10 万 FPS）

**原文标题**: Pokemon Emerald Ported to WebAssembly (100k FPS)

**原文链接**: [https://pokeemerald.com/](https://pokeemerald.com/)

本技术演示展示了经典 Game Boy Advance 游戏《**宝可梦 绿宝石**》的移植版本，该版本通过 **WebAssembly (Wasm)** 直接在 Web 浏览器中运行。

该项目突显了现代 Web 技术的高性能潜力，声称其运行速度最高可达每秒 **100,000 帧 (FPS)**。此移植版拥有功能完备的界面，并将标准游戏控制映射至键盘（方向键控制移动，Z/X 键对应 A/B 按钮，Enter/Shift 键对应 Start/Select 按钮）。

通过利用 WebAssembly，该移植版展示了如何在标准 Web 环境中，以极高的效率和近乎原生的性能来实现对复杂经典主机游戏的模拟。

---

## 8. How LLMs work

**原文标题**: How LLMs work

**原文链接**: [https://www.0xkato.xyz/how-llms-actually-work/](https://www.0xkato.xyz/how-llms-actually-work/)

生成摘要时出错

---

## 9. Running Python code in a sandbox with MicroPython and WASM

**原文标题**: Running Python code in a sandbox with MicroPython and WASM

**原文链接**: [https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)

生成摘要时出错

---

## 10. Police in England and Wales told to halt AI use in court statements

**原文标题**: Police in England and Wales told to halt AI use in court statements

**原文链接**: [https://www.ft.com/content/229e5949-3ebc-4151-8a86-a01b5e259241](https://www.ft.com/content/229e5949-3ebc-4151-8a86-a01b5e259241)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 2 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 3 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 4 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 5 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 6 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 7 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 8 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 9 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 10 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 11 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 12 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 13 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 14 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 15 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 16 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 17 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 18 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 19 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 20 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 21 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 22 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 23 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 24 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 25 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 26 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 27 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 28 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 29 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 30 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 31 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 32 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 33 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 34 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 35 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 36 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 37 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 38 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 39 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 40 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 41 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 42 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 43 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 44 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 45 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 46 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 47 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 48 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 49 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 50 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 51 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 52 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 53 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 54 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 55 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 56 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 57 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 58 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 59 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 60 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 61 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 62 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 63 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 64 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 65 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 66 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 67 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 68 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 69 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 70 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 71 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 72 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 73 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 74 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 75 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 76 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 77 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 78 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 79 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 80 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 81 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 82 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 83 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 84 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 85 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 86 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 87 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 88 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 89 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 90 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 91 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 92 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 93 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 94 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 95 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 96 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 97 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 98 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 99 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 100 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 101 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 102 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 103 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 104 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 105 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 106 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 107 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 108 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 109 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 110 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 111 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 112 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 113 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 114 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 115 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 116 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 117 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 118 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 119 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 120 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 121 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 122 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 123 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 124 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 125 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 126 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 127 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 128 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 129 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 130 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 131 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 132 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 133 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 134 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 135 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 136 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 137 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 138 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 139 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 140 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 141 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 142 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 143 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 144 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 145 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 146 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 147 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 148 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 149 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 150 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 151 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 152 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 153 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 154 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 155 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 156 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 157 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 158 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 159 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 160 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 161 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 162 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 163 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 164 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 165 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 166 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 167 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 168 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 169 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 170 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 171 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 172 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 173 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 174 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 175 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 176 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 177 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 178 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 179 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 180 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 181 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 182 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 183 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 184 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 185 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 186 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 187 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 188 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 189 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 190 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 191 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 192 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 193 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 194 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 195 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 196 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 197 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 198 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 199 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 200 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 201 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 202 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 203 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 204 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 205 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 206 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 207 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 208 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 209 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 210 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 211 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 212 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 213 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 214 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 215 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 216 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 217 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 218 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 219 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 220 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 221 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 222 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 223 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 224 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 225 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 226 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 227 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 228 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 229 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 230 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 231 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 232 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 233 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 234 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 235 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 236 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 237 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 238 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 239 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 240 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 241 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 242 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 243 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 244 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 245 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 246 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 247 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 248 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 249 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 250 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 251 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 252 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 253 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 254 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 255 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 256 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 257 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 258 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 259 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 260 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 261 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 262 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 263 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 264 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 265 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 266 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 267 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 268 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 269 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 270 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 271 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 272 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 273 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 274 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 275 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 276 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 277 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 278 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 279 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 280 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 281 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 282 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 283 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 284 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 285 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 286 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 287 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 288 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 289 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 290 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 291 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 292 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 293 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 294 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 295 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 296 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 297 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 298 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 299 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 300 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 301 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 302 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 303 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 304 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 305 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 306 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 307 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 308 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 309 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 310 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 311 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 312 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 313 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 314 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 315 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 316 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 317 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 318 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 319 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 320 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 321 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 322 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 323 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 324 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 325 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 326 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 327 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 328 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 329 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 330 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 331 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 332 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 333 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 334 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 335 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 336 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 337 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 338 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 339 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 340 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 341 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 342 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 343 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 344 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 345 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 346 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 347 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 348 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 349 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 350 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 351 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 352 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 353 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 354 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 355 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 356 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 357 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 358 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 359 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 360 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 361 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 362 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 363 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 364 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 365 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 366 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 367 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 368 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 369 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 370 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 371 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 372 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 373 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 374 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 375 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 376 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 377 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 378 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 379 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 380 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 381 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 382 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 383 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 384 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 385 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 386 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 387 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 388 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 389 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 390 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 391 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 392 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 393 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 394 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 395 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 396 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 397 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 398 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 399 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 400 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 401 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 402 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 403 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 404 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 405 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 406 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 407 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 408 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 409 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 410 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 411 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 412 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 413 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 414 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 415 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 416 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 417 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 418 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 419 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 420 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 421 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 422 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 423 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 424 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 425 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 426 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 427 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 428 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 429 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 430 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 431 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 432 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 433 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 434 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 435 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 436 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 437 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 438 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 439 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 440 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 441 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 442 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 443 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
