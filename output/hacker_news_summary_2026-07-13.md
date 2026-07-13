# Hacker News 热门文章摘要 (2026-07-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 苹果全新的 SpeechAnalyzer API：与 Whisper 及其前代产品的基准测试对比

**原文标题**: Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

**原文链接**: [https://get-inscribe.com/blog/apple-speech-api-benchmark.html](https://get-inscribe.com/blog/apple-speech-api-benchmark.html)

根据 Inscribe 的最新基准测试，随 iOS/macOS 26 推出的苹果全新 **SpeechAnalyzer API** 已成为英语领域最准确的端侧语音转文本引擎。

在 M2 Pro Mac 上使用 LibriSpeech 数据集进行的测试显示，SpeechAnalyzer 的表现明显优于其前代产品（**SFSpeechRecognizer**）以及 OpenAI 的 **Whisper** 模型。主要结论包括：

*   **卓越的准确率：** 在清晰语音测试中，SpeechAnalyzer 的词错误率（WER）仅为 **2.12%**，而 Whisper Small 为 **3.74%**，苹果旧版 API 则表现滞后，为 **9.02%**。在嘈杂语音环境下，新 API 依然以 4.56% 的词错误率保持领先。
*   **更快的速度：** 除了准确率，SpeechAnalyzer 的运行速度比 Whisper Small 快约 **3 倍**，在设备端转写一小时的音频仅需 1.5 到 5 分钟。
*   **较旧版大幅提升：** 强烈建议开发者从 SFSpeechRecognizer 迁移，因为新 API 将错误率降低了 3.5 到 4 倍，并提供了更好的格式化功能，包括标点符号和大小写。

**方法论与局限性**
基准测试使用 Inscribe 的生产环境代码运行，以确保符合实际应用场景。为了证明数据的完整性，研究人员将他们的 Whisper 测试结果与 OpenAI 公布的数据进行了对比，发现两者几乎完全一致。

虽然 SpeechAnalyzer 目前是苹果硬件上英语转换“最强的端侧方案”，但 Whisper 仍保留两大优势：它支持 **100 多种语言**（而 SpeechAnalyzer 仅支持约 30 种），且支持非苹果平台。因此，Inscribe 已更新其产品，针对受支持的语言优先使用 SpeechAnalyzer，而对其他语言则回退使用 Whisper。结果表明，对于现代 iPhone 和 Mac 上的英语用户而言，苹果内置工具在效率和精度上均已超越了专业的第三方模型。

---

## 2. xAI 的 Grok Build CLI 将 Git 仓库上传至 Google Cloud 存储桶

**原文标题**: xAI's Grok Build CLI Uploads Git Repositories to a Google Cloud Bucket

**原文链接**: [https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/](https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/)

安全研究员“cereblab”最近披露，xAI 的 Grok Build CLI 正在悄无声息地将开发者的整个 Git 仓库——包括完整的历史记录、密钥以及未经脱敏的凭据——上传到 Google Cloud Storage 存储桶。

尽管该工具在宣传中被标榜为“本地优先”工具，但研究发现，无论文件是否与 AI 的特定编码任务相关，该 CLI 都会打包并传输海量数据。在一次测试中，该工具上传了 5.1 GB 的数据，而模型请求实际仅需 192 KB。值得注意的是，许多用户认为“改进模型”开关是数据收集的控制项，但该开关并没能阻止上传；据报道，它仅用于管理训练授权，而非限制代码库的物理传输。

在这些行为被公开曝光后，xAI 实施了隐秘的服务端缓解措施。随后的测试表明，该公司通过远程切换标志位禁用了代码库上传，但这一改动是在没有发布软件更新或公开承认的情况下进行的。

截至目前，xAI 尚未发布安全公告，也未就此次数据收集的范围和目的提供任何解释。目前尚不清楚这些收集到的数据将保留多久、谁曾拥有访问权限，以及 xAI 是否打算删除已存储在其“grok-code-session-traces”存储桶中的仓库。最新的官方变更日志对此事保持沉默，导致用户无法获得关于其专有源代码为何在未披露的情况下被收集的正式说明。

---

## 3. 作品展示：Super Dario

**原文标题**: Show HN: Super Dario

**原文链接**: [https://superdario.pawb.de](https://superdario.pawb.de)

根据提供的 "Show HN" (Hacker News) 项目标题，以下是 **Super Dario** 项目及其 "One More Week" 更新背景的摘要：

**Super Dario** 是一款基于 Web 的平台跳跃游戏及引擎，旨在向经典 8 位游戏（特别是《超级马里奥乐园》）致敬。该项目是一个技术展示，旨在探索现代 Web 技术在游戏领域的边界。

### 核心信息：
*   **技术栈：** 与使用 Unity 或 Godot 等专用引擎构建的传统游戏不同，Super Dario 是利用 **React、TypeScript 和 HTML5 Canvas API** 构建的。它作为一种概念验证，展示了如何使用 React 来管理复杂的游戏状态和渲染周期。
*   **开发里程碑：** "One More Week" 副标题指的是一个特定的开发冲刺或最后的“打磨”阶段。开发者利用这段时间优化了物理引擎，改进了碰撞检测，并确保游戏在不同浏览器中都能流畅运行。
*   **玩法与美学：** 该项目忠实地重现了复古掌机游戏的观感。它包含了标准的平台跳跃机制，如跳跃、踩踏敌人和收集金币，并针对 Web 环境下的低延迟输入进行了优化。
*   **目的：** 作为一篇 "Show HN" 帖子，该项目旨在供开发者社区评价和学习。它展示了 Web 开发者如何利用熟悉的框架（React）来处理高频 UI 更新和动画，从而将现有技能应用到游戏开发中。

**结论：**
Super Dario 不仅仅是一个游戏克隆版，它更是 **Web 性能**的一次精彩演示。"One More Week" 更新标志着项目从功能原型向打磨完善、可供社区反馈和开源贡献的可玩体验的转变。

---

## 4. Sega CD《希尔菲德》的艺术与工程

**原文标题**: The art and engineering of Sega CD Silpheed

**原文链接**: [https://fabiensanglard.net/silpheed/index.html](https://fabiensanglard.net/silpheed/index.html)

Fabien Sanglard 的文章探讨了《银河枪骑兵》（Silpheed）在世嘉 CD（Sega CD）上实现突破性 3D 视觉效果的技术奥秘。尽管该平台以低画质全动态影像（FMV）著称，且面临 CD-ROM 带宽缓慢和 12.5MHz CPU 的性能瓶颈，但《银河枪骑兵》依然脱颖而出。

与其他试图在系统中塞入高保真影片的开发商不同，Game Arts 采用了“自下而上”的工程方法。他们针对硬件限制专门设计了一套引擎，利用平直着色多边形（flat-shaded polygons）、严格的 16 色调色板和极少的抖动处理，在每帧仅 8 KiB 的预算下实现了 15fps 的视频播放。

Sanglard 指出了实现这一性能的三项核心优化：

1.  **图块循环利用（Tile Recycling）：** 由于 Genesis 主机使用 8x8 的图块显示图像，该引擎通过仅存储每个纯色图块的一个实例并在图块地图中多次引用，节省了大量带宽。仅此一项就将带宽占用降低了 50%。
2.  **利用 ASIC 字体位（ASIC Font Bit Exploitation）：** 开发人员巧妙地改造了 Mega-CD ASIC 中原本用于快速文本渲染的功能。通过使用“字体位”寄存器，他们仅需 3 字节数据即可生成双色图块，显著减轻了 CPU 负载并缩小了数据体积。
3.  **图块地图压缩（Tilemap Compression）：** 包含 768 个图块的布局通过一个使用“自动递增”索引的 768 位位图进行压缩，使图块地图的大小缩减了 30%。

该游戏还利用了双 CPU 架构：Mega-CD 的从 CPU（Sub-CPU）负责渲染电影化的背景，而 Genesis 的主 CPU（Main-CPU）则处理 HUD 和游戏精灵。通过巧妙的折衷方案——例如在处理复杂纹理时降低帧率，以及利用调色板变换实现实时特效——Game Arts 打造了一款将世嘉 CD 性能推向极限的传奇之作。

---

## 5. Logseq 2.0 Beta (数据库版本) 现已发布

**原文标题**: Logseq 2.0 Beta (DB version) is here

**原文链接**: [https://github.com/logseq/logseq/releases](https://github.com/logseq/logseq/releases)

Logseq 官方宣布发布 **Logseq 2.0 Beta（版本 2.0.1）**，这标志着该应用开发进程中的一个重大里程碑。本次发布的亮点在于引入了期待已久的 **数据库（DB）版本**，这代表了该平台重大的架构转型。

**Logseq 2.0 Beta 核心要点：**
*   **架构变革：** 应用将分为两个版本，2.0 分支专注于全新的数据库底层架构。
*   **测试阶段：** 作为一个早期测试版，开发者提醒其仍存在“不完善之处”，并强烈建议用户在迁移或测试前备份重要数据。
*   **社区反馈：** 团队正积极通过 GitHub 征集错误报告和反馈，以完善稳定版本。

**近期维护（0.10.x 系列）：**
发布说明还详细列举了通往 2.0 版本过程中的持续改进，包括：
*   **安全与稳定：** 修复了远程代码执行（RCE）漏洞、CPU/GPU 占用过高，以及 macOS 和 Linux 上的应用卡死等关键问题。
*   **功能优化：** 改进了 YouTube 嵌入、PDF 区域高亮、搜索索引可靠性以及 Zotero 集成。
*   **扩展支持：** 新增了对 Linux ARM64 的支持，并增强了 Android 端功能（如更优的资源共享）。
*   **国际化：** 在社区贡献者的推动下，持续更新包括中文、意大利语、土耳其语和波斯语在内的多种语言翻译。

向 2.0 版本的转型标志着 Logseq 开启了新篇章，在迈向更强大的数据管理系统的同时，依然坚守其社区驱动、注重隐私的知识管理理念。

---

## 6. 洛杉矶警局任由与监控巨头 Flock 的合同到期

**原文标题**: LAPD lets contract with surveillance giant Flock expire

**原文链接**: [https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/)

洛杉矶警察局（LAPD）已允许其与监控巨头 Flock Safety 的三年合同到期不再续约，理由是该部门对公民自由、隐私和数据安全存在“严重关切”。作为 Flock 最大的客户之一，LAPD 的退出对该公司造成了重大打击。Flock 在全美运营着一个由超过 8 万个车牌识别摄像头组成的网络。

LAPD 首席信息官 Dean Gialamas 表示，该部门将停止这项服务，直到通过新合同“解决”数据共享和隐私保护问题。在此之前，加利福尼亚州山景城和缅因州南波特兰等城市也采取了类似行动，当地官员对隐私问题以及联邦移民局可能违反地方庇护政策利用相关数据表示担忧。

文章强调了与 Flock 技术相关的几个关键问题：
*   **安全风险：** 技术错误和“误报”导致无辜驾驶员被拦下、被持枪拘留或入狱。
*   **安全漏洞：** 有报告称摄像头画面公开暴露，且警察登录缺乏多因素身份验证，导致数据极易受到黑客攻击。
*   **未经授权的访问：** 据报道，在一起案例中，美国缉毒局（DEA）在当地警官不知情的情况下，使用其凭据搜索嫌疑人。

Flock Safety 对合同到期表示“惊讶”，并将其归因于他们希望澄清的“误解”。虽然如果能制定更严格的隐私和数据存储条款，LAPD 仍对未来达成交易持开放态度，但此举反映了公众和政府对不受监管的自动化监控扩张日益增长的抵制。

---

## 7. 实时同步的体素风东京——乘坐山手线，学习日语

**原文标题**: A voxel Tokyo in real Japan time – ride the Yamanote line and study Japanese

**原文链接**: [https://jivx.com/densha](https://jivx.com/densha)

**Summary: A Voxel Tokyo in Real Japan Time**

"Densha," a web-based project created by developer Jivx, offers an immersive, voxel-style recreation of Tokyo’s iconic Yamanote Line. The project serves as both a technical marvel and a unique educational tool designed to help users study Japanese through environmental immersion.

The most striking feature of the simulation is its synchronization with real-world Japan Standard Time (JST). The trains in the voxel world follow actual, live transit schedules; if a train is pulling into Shibuya Station in real life, its digital counterpart does the same in the browser. The environment also reflects the current time of day in Tokyo, transitioning through morning light, sunset, and neon-lit nightscapes.

Beyond its aesthetic appeal, the platform is built for language learners. As users "ride" the train, the interface displays relevant Japanese vocabulary, kanji, and station names. This contextual learning allows users to associate language with specific landmarks and transit scenarios, mimicking the experience of a daily commute in Japan.

Technical highlights and user features include:
*   **Interactive Camera:** Users can toggle between different cinematic views or a "driver’s eye" perspective.
*   **Voxel Art Style:** A detailed, 3D pixel-art aesthetic that covers major landmarks along the 34.5km loop.
*   **Accessibility:** The project runs directly in the browser, making it an easily accessible "window into Tokyo" for students and enthusiasts worldwide.

By blending real-time data with a relaxing, lo-fi atmosphere, "Densha" provides a functional study aid that captures the specific rhythm of life in Japan’s capital.

---

## 8. Ancient Roman Board Game

**原文标题**: Ancient Roman Board Game

**原文链接**: [https://ludus-coriovalli.web.app/](https://ludus-coriovalli.web.app/)

生成摘要时出错

---

## 9. PgDog (YC P25) Is Hiring a Founding Software Engineer

**原文标题**: PgDog (YC P25) Is Hiring a Founding Software Engineer

**原文链接**: [https://www.ycombinator.com/companies/pgdog/jobs/uWymUYy-founding-software-engineer](https://www.ycombinator.com/companies/pgdog/jobs/uWymUYy-founding-software-engineer)

生成摘要时出错

---

## 10. Benchmarking 15 "E-Waste" GPUs with Modern Workloads

**原文标题**: Benchmarking 15 "E-Waste" GPUs with Modern Workloads

**原文链接**: [https://esologic.com/benchmarking-tesla-gpus/](https://esologic.com/benchmarking-tesla-gpus/)

生成摘要时出错

---

## 11. Tune Code Before Your Garbage Collector

**原文标题**: Tune Code Before Your Garbage Collector

**原文链接**: [http://blog.vanillajava.blog/2026/06/why-you-should-tun-code-before-your.html](http://blog.vanillajava.blog/2026/06/why-you-should-tun-code-before-your.html)

生成摘要时出错

---

## 12. Show HN: DOM-docx – HTML to native, editable Word docs (MIT)

**原文标题**: Show HN: DOM-docx – HTML to native, editable Word docs (MIT)

**原文链接**: [https://github.com/floodtide/dom-docx](https://github.com/floodtide/dom-docx)

生成摘要时出错

---

## 13. Show HN: OpenClawMachines – Extending OpenClaw to the Enterprise

**原文标题**: Show HN: OpenClawMachines – Extending OpenClaw to the Enterprise

**原文链接**: [https://github.com/mathaix/OpenClawMachines](https://github.com/mathaix/OpenClawMachines)

生成摘要时出错

---

## 14. The 'absolute magic' of Morse code that still connects people globally

**原文标题**: The 'absolute magic' of Morse code that still connects people globally

**原文链接**: [https://www.bbc.com/news/articles/cwye0dlzgejo](https://www.bbc.com/news/articles/cwye0dlzgejo)

生成摘要时出错

---

## 15. Backtrack-Free Cursive

**原文标题**: Backtrack-Free Cursive

**原文链接**: [https://mmapped.blog/posts/52-backtrack-free-cursive](https://mmapped.blog/posts/52-backtrack-free-cursive)

生成摘要时出错

---

## 16. GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

**原文标题**: GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

**原文链接**: [https://nebusec.ai/research/ionstack-part-2/](https://nebusec.ai/research/ionstack-part-2/)

生成摘要时出错

---

## 17. Cursed circuits #6: reverse avalanche oscillator

**原文标题**: Cursed circuits #6: reverse avalanche oscillator

**原文链接**: [https://lcamtuf.substack.com/p/cursed-circuits-6-reverse-avalanche](https://lcamtuf.substack.com/p/cursed-circuits-6-reverse-avalanche)

生成摘要时出错

---

## 18. Counting ArXiv Delays

**原文标题**: Counting ArXiv Delays

**原文链接**: [https://fi-le.net/arxiv/](https://fi-le.net/arxiv/)

生成摘要时出错

---

## 19. Show HN: Clawk – Give coding agents a disposable Linux VM, not your laptop

**原文标题**: Show HN: Clawk – Give coding agents a disposable Linux VM, not your laptop

**原文链接**: [https://github.com/clawkwork/clawk](https://github.com/clawkwork/clawk)

生成摘要时出错

---

## 20. The Graph That Should Be Front-Page News

**原文标题**: The Graph That Should Be Front-Page News

**原文链接**: [https://www.lyrebirddreaming.com/post/the-graph-that-should-be-front-page-news](https://www.lyrebirddreaming.com/post/the-graph-that-should-be-front-page-news)

生成摘要时出错

---

## 21. The social physics of conversation: Communication patterns matter

**原文标题**: The social physics of conversation: Communication patterns matter

**原文链接**: [https://andiroberts.com/citizenship/the-social-physics-of-conversation-citizenship-leadership](https://andiroberts.com/citizenship/the-social-physics-of-conversation-citizenship-leadership)

生成摘要时出错

---

## 22. Wikipedia escapes Category 1 designation under the UK Online Safety Act for now

**原文标题**: Wikipedia escapes Category 1 designation under the UK Online Safety Act for now

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-07-13/Special_report](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-07-13/Special_report)

生成摘要时出错

---

## 23. Precursor

**原文标题**: Precursor

**原文链接**: [https://blog.cloudflare.com/introducing-precursor/](https://blog.cloudflare.com/introducing-precursor/)

生成摘要时出错

---

## 24. DMS 1.5 "The Wolverine" Released

**原文标题**: DMS 1.5 "The Wolverine" Released

**原文链接**: [https://danklinux.com/blog/v1-5-release](https://danklinux.com/blog/v1-5-release)

生成摘要时出错

---

## 25. Cyberpunk Comics, Manga and Graphic Novels

**原文标题**: Cyberpunk Comics, Manga and Graphic Novels

**原文链接**: [https://shellzine.net/cyberpunk-comics/](https://shellzine.net/cyberpunk-comics/)

生成摘要时出错

---

## 26. A Farewell to ARPs: IPv4 Service on IPv6-Only Networks

**原文标题**: A Farewell to ARPs: IPv4 Service on IPv6-Only Networks

**原文链接**: [https://labs.ripe.net/author/remco-van-mook/a-farewell-to-arps-ipv4-service-on-ipv6-only-networks/](https://labs.ripe.net/author/remco-van-mook/a-farewell-to-arps-ipv4-service-on-ipv6-only-networks/)

生成摘要时出错

---

## 27. Zig Creator Calls Spade a Spade, Anthropic Blows Smoke

**原文标题**: Zig Creator Calls Spade a Spade, Anthropic Blows Smoke

**原文链接**: [https://raymyers.org/post/zed-creator-calls-spade-a-spade/](https://raymyers.org/post/zed-creator-calls-spade-a-spade/)

生成摘要时出错

---

## 28. Go-Flavored Concurrency in C

**原文标题**: Go-Flavored Concurrency in C

**原文链接**: [https://antonz.org/concurrency-in-c/](https://antonz.org/concurrency-in-c/)

生成摘要时出错

---

## 29. Tiny Emulators

**原文标题**: Tiny Emulators

**原文链接**: [https://floooh.github.io/tiny8bit-preview/index.html](https://floooh.github.io/tiny8bit-preview/index.html)

生成摘要时出错

---

## 30. So you want to learn physics (second edition, 2021)

**原文标题**: So you want to learn physics (second edition, 2021)

**原文链接**: [https://www.susanrigetti.com/physics](https://www.susanrigetti.com/physics)

生成摘要时出错

---

## 31. Interrail: 6,379Km and 13 Countries over 7 weeks

**原文标题**: Interrail: 6,379Km and 13 Countries over 7 weeks

**原文链接**: [https://shkspr.mobi/blog/2026/07/another-ridiculous-interrail-holiday-6379km-and-13-countries-over-7-weeks/](https://shkspr.mobi/blog/2026/07/another-ridiculous-interrail-holiday-6379km-and-13-countries-over-7-weeks/)

生成摘要时出错

---

## 32. Frieve Vinyl Explained – Microscopic stylus/groove physics simulation

**原文标题**: Frieve Vinyl Explained – Microscopic stylus/groove physics simulation

**原文链接**: [https://frieve-a.github.io/sound_toolbox/vinyl_explained/vinyl_explained.html](https://frieve-a.github.io/sound_toolbox/vinyl_explained/vinyl_explained.html)

生成摘要时出错

---

## 33. How to read more books

**原文标题**: How to read more books

**原文链接**: [https://scotto.me/blog/2026-07-12-how-to-read-more-books/](https://scotto.me/blog/2026-07-12-how-to-read-more-books/)

生成摘要时出错

---

## 34. Grok CLI uploaded the whole home directory to GCS

**原文标题**: Grok CLI uploaded the whole home directory to GCS

**原文链接**: [https://twitter.com/a_green_being/status/2076598897779020159](https://twitter.com/a_green_being/status/2076598897779020159)

生成摘要时出错

---

## 35. Beavis Ultrasound PnP ISA Sound Card Replica

**原文标题**: Beavis Ultrasound PnP ISA Sound Card Replica

**原文链接**: [https://github.com/schlae/BeavisUltrasound](https://github.com/schlae/BeavisUltrasound)

生成摘要时出错

---

## 36. Samsung overtakes Apple as smartphone market sinks to a 13-year low

**原文标题**: Samsung overtakes Apple as smartphone market sinks to a 13-year low

**原文链接**: [https://www.androidauthority.com/counterpoint-research-q2-2026-smartphone-shipment-report-3686931/](https://www.androidauthority.com/counterpoint-research-q2-2026-smartphone-shipment-report-3686931/)

生成摘要时出错

---

## 37. Software Has Changed

**原文标题**: Software Has Changed

**原文链接**: [https://www.abeautifulsite.net/posts/software-has-changed/](https://www.abeautifulsite.net/posts/software-has-changed/)

生成摘要时出错

---

## 38. Show HN: HTML, CSS and JavaScript in the Terminal

**原文标题**: Show HN: HTML, CSS and JavaScript in the Terminal

**原文链接**: [https://duetbrowser.com/krnl-ss-redirect?k2vh](https://duetbrowser.com/krnl-ss-redirect?k2vh)

生成摘要时出错

---

## 39. GLP-1s are shrinking bodies. Enter cadaver fat injections

**原文标题**: GLP-1s are shrinking bodies. Enter cadaver fat injections

**原文链接**: [https://www.cnn.com/2026/07/13/style/alloclae-glp-1-cadaver-fat-interview](https://www.cnn.com/2026/07/13/style/alloclae-glp-1-cadaver-fat-interview)

生成摘要时出错

---

## 40. LARP – Revenue infrastructure for serious founders

**原文标题**: LARP – Revenue infrastructure for serious founders

**原文链接**: [https://www.larp.website/](https://www.larp.website/)

生成摘要时出错

---

## 41. Vint Cerf, “father of the Internet”, is retiring

**原文标题**: Vint Cerf, “father of the Internet”, is retiring

**原文链接**: [https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/](https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/)

生成摘要时出错

---

## 42. DOGE is done. What happened to its records?

**原文标题**: DOGE is done. What happened to its records?

**原文链接**: [https://www.ms.now/opinion/doge-government-efficiency-records-job-cuts-elon-musk-foia](https://www.ms.now/opinion/doge-government-efficiency-records-job-cuts-elon-musk-foia)

生成摘要时出错

---

## 43. Designing and assembling my first PCB

**原文标题**: Designing and assembling my first PCB

**原文链接**: [https://vilkeliskis.com/b/2026/0711.html](https://vilkeliskis.com/b/2026/0711.html)

生成摘要时出错

---

## 44. Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper

**原文标题**: Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper

**原文链接**: [https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

生成摘要时出错

---

## 45. Latent Space as a New Medium

**原文标题**: Latent Space as a New Medium

**原文链接**: [https://kevinkelly.substack.com/p/latent-space-as-a-new-medium](https://kevinkelly.substack.com/p/latent-space-as-a-new-medium)

生成摘要时出错

---

## 46. Sam Neill has died

**原文标题**: Sam Neill has died

**原文链接**: [https://www.theguardian.com/film/2026/jul/13/sam-neill-death-actor-dies-aged-78](https://www.theguardian.com/film/2026/jul/13/sam-neill-death-actor-dies-aged-78)

生成摘要时出错

---

## 47. Kode Dot Programmable pocket device for makers, pentesters and geeks

**原文标题**: Kode Dot Programmable pocket device for makers, pentesters and geeks

**原文链接**: [https://kode.diy](https://kode.diy)

生成摘要时出错

---

## 48. Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

**原文标题**: Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

**原文链接**: [https://systima.ai/blog/claude-code-vs-opencode-token-overhead](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)

生成摘要时出错

---

## 49. How we can reduce traffic congestion

**原文标题**: How we can reduce traffic congestion

**原文链接**: [https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

生成摘要时出错

---

## 50. Are you telling me a readonly property is wrecking my performance?

**原文标题**: Are you telling me a readonly property is wrecking my performance?

**原文链接**: [https://shub.club/writings/2026/july/check-your-scrollheight/](https://shub.club/writings/2026/july/check-your-scrollheight/)

生成摘要时出错

---

## 51. Why Copyright Analysis Alone Is Not Enough for Open Source Licensing

**原文标题**: Why Copyright Analysis Alone Is Not Enough for Open Source Licensing

**原文链接**: [https://shujisado.org/2026/07/13/why-copyright-analysis-alone-is-not-enough-for-open-source-licensing/](https://shujisado.org/2026/07/13/why-copyright-analysis-alone-is-not-enough-for-open-source-licensing/)

生成摘要时出错

---

## 52. Why write code in 2026

**原文标题**: Why write code in 2026

**原文链接**: [https://softwaredoug.com/blog/2026/07/09/write-code](https://softwaredoug.com/blog/2026/07/09/write-code)

生成摘要时出错

---

## 53. Control the Ideas, Not the Code

**原文标题**: Control the Ideas, Not the Code

**原文链接**: [https://antirez.com/news/169](https://antirez.com/news/169)

生成摘要时出错

---

## 54. (bun GitHub repository) AI slop #33864

**原文标题**: (bun GitHub repository) AI slop #33864

**原文链接**: [https://github.com/oven-sh/bun/pull/33864](https://github.com/oven-sh/bun/pull/33864)

生成摘要时出错

---

## 55. Automation Without Understanding

**原文标题**: Automation Without Understanding

**原文链接**: [https://arxiv.org/abs/2607.06377](https://arxiv.org/abs/2607.06377)

生成摘要时出错

---

## 56. I Learned to Read Again

**原文标题**: I Learned to Read Again

**原文链接**: [https://substack.magazinenongrata.com/p/how-i-learned-to-read-again](https://substack.magazinenongrata.com/p/how-i-learned-to-read-again)

生成摘要时出错

---

## 57. Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance

**原文标题**: Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance

**原文链接**: [https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai](https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai)

生成摘要时出错

---

## 58. Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance

**原文标题**: Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance

**原文链接**: [https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai](https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai)

生成摘要时出错

---

## 59. Death of the Status Update: Why 55% of Americans Stopped Posting on Social Media

**原文标题**: Death of the Status Update: Why 55% of Americans Stopped Posting on Social Media

**原文链接**: [https://ca.pcmag.com/social-media/16790/the-death-of-the-status-update-why-55-of-americans-stopped-posting-on-social-media](https://ca.pcmag.com/social-media/16790/the-death-of-the-status-update-why-55-of-americans-stopped-posting-on-social-media)

生成摘要时出错

---

## 60. First look at Quest, the final ship of Antarctic explorer Shackleton

**原文标题**: First look at Quest, the final ship of Antarctic explorer Shackleton

**原文链接**: [https://www.cbc.ca/news/canada/quest-shipwreck-expedition-images-9.7262229](https://www.cbc.ca/news/canada/quest-shipwreck-expedition-images-9.7262229)

生成摘要时出错

---

## 61. Guy took Jupiter photo with Game Boy Camera, giant telescope, publishes tutorial

**原文标题**: Guy took Jupiter photo with Game Boy Camera, giant telescope, publishes tutorial

**原文链接**: [https://www.engadget.com/2211886/guy-who-took-photo-of-jupiter-with-a-game-boy-camera-and-giant-telescope-publishes-diy-tutorial/](https://www.engadget.com/2211886/guy-who-took-photo-of-jupiter-with-a-game-boy-camera-and-giant-telescope-publishes-diy-tutorial/)

生成摘要时出错

---

## 62. A Metallurgist's Doubts About Self-Replicating Probes

**原文标题**: A Metallurgist's Doubts About Self-Replicating Probes

**原文链接**: [https://www.centauri-dreams.org/2026/07/10/a-metallurgists-doubts-about-self-replicating-probes/](https://www.centauri-dreams.org/2026/07/10/a-metallurgists-doubts-about-self-replicating-probes/)

生成摘要时出错

---

## 63. Against Usefulness

**原文标题**: Against Usefulness

**原文链接**: [https://www.motivenotes.ai/p/against-usefulness](https://www.motivenotes.ai/p/against-usefulness)

生成摘要时出错

---

## 64. A Heuristic for When to Reason vs When to Act

**原文标题**: A Heuristic for When to Reason vs When to Act

**原文链接**: [https://techandsundry.medium.com/when-to-reason-and-when-to-act-8144f3c31053](https://techandsundry.medium.com/when-to-reason-and-when-to-act-8144f3c31053)

生成摘要时出错

---

## 65. Nokia's 14 Years of Mobile-Phone Supremacy Ended in an Afternoon

**原文标题**: Nokia's 14 Years of Mobile-Phone Supremacy Ended in an Afternoon

**原文链接**: [https://spectrum.ieee.org/nokia-phones-history](https://spectrum.ieee.org/nokia-phones-history)

生成摘要时出错

---

## 66. Mechanistic interpretability researchers applying causality theory to LLMs

**原文标题**: Mechanistic interpretability researchers applying causality theory to LLMs

**原文链接**: [https://cacm.acm.org/news/can-we-understand-how-large-language-models-reason/](https://cacm.acm.org/news/can-we-understand-how-large-language-models-reason/)

生成摘要时出错

---

## 67. Old and new apps, via modern coding agents

**原文标题**: Old and new apps, via modern coding agents

**原文链接**: [https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/)

生成摘要时出错

---

## 68. I love LLMs, I hate hype

**原文标题**: I love LLMs, I hate hype

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html)

生成摘要时出错

---

## 69. Quadrupling code performance with a "useless" if

**原文标题**: Quadrupling code performance with a "useless" if

**原文链接**: [https://purplesyringa.moe/blog/quadrupling-code-performance-with-a-useless-if/](https://purplesyringa.moe/blog/quadrupling-code-performance-with-a-useless-if/)

生成摘要时出错

---

## 70. The shingles vaccine may reduce the risk of dementia

**原文标题**: The shingles vaccine may reduce the risk of dementia

**原文链接**: [https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain](https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain)

生成摘要时出错

---

## 71. Stop Telling Me to Ask an LLM

**原文标题**: Stop Telling Me to Ask an LLM

**原文链接**: [https://blog.yaelwrites.com/stop-telling-me-to-ask-an-llm/](https://blog.yaelwrites.com/stop-telling-me-to-ask-an-llm/)

生成摘要时出错

---

## 72. Flash-MSA: Accelerating Million-Token Training with Sparse Attention Kernels

**原文标题**: Flash-MSA: Accelerating Million-Token Training with Sparse Attention Kernels

**原文链接**: [https://nanduruganesh.github.io/flash-msa/](https://nanduruganesh.github.io/flash-msa/)

生成摘要时出错

---

## 73. There's no way this bond market can fund the markets needs without higher yields

**原文标题**: There's no way this bond market can fund the markets needs without higher yields

**原文链接**: [https://www.youtube.com/watch?v=W-Dxpp9YG3s](https://www.youtube.com/watch?v=W-Dxpp9YG3s)

生成摘要时出错

---

## 74. Show HN: Loot Raiders – an ARC Raiders-inspired inventory game in Svelte

**原文标题**: Show HN: Loot Raiders – an ARC Raiders-inspired inventory game in Svelte

**原文链接**: [https://loot-raiders.vercel.app](https://loot-raiders.vercel.app)

生成摘要时出错

---

## 75. An Infuriating Goodbye to Photoshop

**原文标题**: An Infuriating Goodbye to Photoshop

**原文链接**: [https://anderegg.ca/2026/07/12/an-infuriating-goodbye-to-photoshop](https://anderegg.ca/2026/07/12/an-infuriating-goodbye-to-photoshop)

生成摘要时出错

---

## 76. Protobuf-py: Protobuf for Python, without compromises

**原文标题**: Protobuf-py: Protobuf for Python, without compromises

**原文链接**: [https://buf.build/blog/protobuf-py](https://buf.build/blog/protobuf-py)

生成摘要时出错

---

## 77. What xAI's Grok build CLI sends to xAI: A wire-level analysis

**原文标题**: What xAI's Grok build CLI sends to xAI: A wire-level analysis

**原文链接**: [https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)

生成摘要时出错

---

## 78. Why Am I Left-Handed?

**原文标题**: Why Am I Left-Handed?

**原文链接**: [https://www.quantamagazine.org/why-am-i-left-handed-20260713/](https://www.quantamagazine.org/why-am-i-left-handed-20260713/)

生成摘要时出错

---

## 79. Don't you mean extinct?

**原文标题**: Don't you mean extinct?

**原文链接**: [https://fabiensanglard.net/extinct/index.html](https://fabiensanglard.net/extinct/index.html)

生成摘要时出错

---

## 80. Calculix: A Free Software Three-Dimensional Structural Finite Element Program

**原文标题**: Calculix: A Free Software Three-Dimensional Structural Finite Element Program

**原文链接**: [https://www.calculix.de/](https://www.calculix.de/)

生成摘要时出错

---

## 81. Gleam for Python Programmers

**原文标题**: Gleam for Python Programmers

**原文链接**: [https://third-bit.com/gl4py/](https://third-bit.com/gl4py/)

生成摘要时出错

---

## 82. Show HN: Mindwalk – Replay coding-agent sessions on a 3D map of your codebase

**原文标题**: Show HN: Mindwalk – Replay coding-agent sessions on a 3D map of your codebase

**原文链接**: [https://github.com/cosmtrek/mindwalk](https://github.com/cosmtrek/mindwalk)

生成摘要时出错

---

## 83. Croc: Securely transfer files and folders between two computers

**原文标题**: Croc: Securely transfer files and folders between two computers

**原文链接**: [https://github.com/schollz/croc/](https://github.com/schollz/croc/)

生成摘要时出错

---

## 84. Unauthenticated RCE in Motorola's MR2600 Router

**原文标题**: Unauthenticated RCE in Motorola's MR2600 Router

**原文链接**: [https://mrbruh.com/motorola/](https://mrbruh.com/motorola/)

生成摘要时出错

---

## 85. The One-Step Trap (In AI Research)

**原文标题**: The One-Step Trap (In AI Research)

**原文链接**: [http://incompleteideas.net/IncIdeas/OneStepTrap.html](http://incompleteideas.net/IncIdeas/OneStepTrap.html)

生成摘要时出错

---

## 86. Why study Diophantine equations?

**原文标题**: Why study Diophantine equations?

**原文链接**: [https://hidden-phenomena.com/articles/modular](https://hidden-phenomena.com/articles/modular)

生成摘要时出错

---

## 87. Modern decor may be straining people's brains

**原文标题**: Modern decor may be straining people's brains

**原文链接**: [https://studyfinds.com/modern-decor-may-be-straining-peoples-brains/](https://studyfinds.com/modern-decor-may-be-straining-peoples-brains/)

生成摘要时出错

---

## 88. AI boosts research careers but narrow the span of ideas explored: study

**原文标题**: AI boosts research careers but narrow the span of ideas explored: study

**原文链接**: [https://spectrum.ieee.org/ai-science-research-flattens-discovery](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

生成摘要时出错

---

## 89. The State of MCP Security [pdf]

**原文标题**: The State of MCP Security [pdf]

**原文链接**: [https://www.canopii.dev/State%20of%20MCP%20Security%202026.pdf](https://www.canopii.dev/State%20of%20MCP%20Security%202026.pdf)

生成摘要时出错

---

## 90. Photovoltaics are still running after a year under Swiss trains

**原文标题**: Photovoltaics are still running after a year under Swiss trains

**原文链接**: [https://www.theregister.com/offbeat/2026/07/13/photovoltaics-are-still-running-after-a-year-under-swiss-trains/5269664](https://www.theregister.com/offbeat/2026/07/13/photovoltaics-are-still-running-after-a-year-under-swiss-trains/5269664)

生成摘要时出错

---

## 91. Z.ai founder backs open-source AI as global security debate intensifies

**原文标题**: Z.ai founder backs open-source AI as global security debate intensifies

**原文链接**: [https://www.business-standard.com/technology/tech-news/zhipu-founder-backs-open-source-ai-as-global-security-debate-intensifies-126071200342_1.html](https://www.business-standard.com/technology/tech-news/zhipu-founder-backs-open-source-ai-as-global-security-debate-intensifies-126071200342_1.html)

生成摘要时出错

---

## 92. Profiling the "Abundance" housing bottleneck with real data

**原文标题**: Profiling the "Abundance" housing bottleneck with real data

**原文链接**: [https://laxmena.com/same-capacity-less-throughput](https://laxmena.com/same-capacity-less-throughput)

生成摘要时出错

---

## 93. Show HN: Getting GLM 5.2 running on my slow computer

**原文标题**: Show HN: Getting GLM 5.2 running on my slow computer

**原文链接**: [https://github.com/JustVugg/colibri](https://github.com/JustVugg/colibri)

生成摘要时出错

---

## 94. Why Vanilla JavaScript

**原文标题**: Why Vanilla JavaScript

**原文链接**: [https://guseyn.com/html/posts/why-vanilla-js.html](https://guseyn.com/html/posts/why-vanilla-js.html)

生成摘要时出错

---

## 95. Ukraine Lands Armed Robot Ashore in Russian-Held Territory via Drone Boat

**原文标题**: Ukraine Lands Armed Robot Ashore in Russian-Held Territory via Drone Boat

**原文链接**: [https://www.twz.com/sea/ukraine-lands-armed-robot-ashore-in-russian-held-territory-via-drone-boat](https://www.twz.com/sea/ukraine-lands-armed-robot-ashore-in-russian-held-territory-via-drone-boat)

生成摘要时出错

---

## 96. Show HN: Codebase Posters – turn any Git repo into generative poster art

**原文标题**: Show HN: Codebase Posters – turn any Git repo into generative poster art

**原文链接**: [https://github.com/unable12/codebase-posters](https://github.com/unable12/codebase-posters)

生成摘要时出错

---

## 97. Autoresearch, Claude and Constrained Optimization

**原文标题**: Autoresearch, Claude and Constrained Optimization

**原文链接**: [https://www.elliotcsmith.com/autoresearch-claude-and-constrained-optimization/](https://www.elliotcsmith.com/autoresearch-claude-and-constrained-optimization/)

生成摘要时出错

---

## 98. Mesh LLM: distributed AI computing on iroh

**原文标题**: Mesh LLM: distributed AI computing on iroh

**原文链接**: [https://www.iroh.computer/blog/mesh-llm](https://www.iroh.computer/blog/mesh-llm)

生成摘要时出错

---

## 99. Show HN: 18 Words

**原文标题**: Show HN: 18 Words

**原文链接**: [https://18words.com/](https://18words.com/)

生成摘要时出错

---

## 100. Wildest claims in Apple's lawsuit against OpenAI

**原文标题**: Wildest claims in Apple's lawsuit against OpenAI

**原文链接**: [https://www.theverge.com/tech/964843/apple-openai-lawsuit-wildest-claims](https://www.theverge.com/tech/964843/apple-openai-lawsuit-wildest-claims)

生成摘要时出错

---

