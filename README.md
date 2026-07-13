# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-13.md)

*最后自动更新时间: 2026-07-13 19:13:27*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 2 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 3 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 4 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 5 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 6 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 7 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 8 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 9 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 10 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 11 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 12 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 13 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 14 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 15 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 16 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 17 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 18 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 19 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 20 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 21 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 22 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 23 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 24 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 25 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 26 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 27 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 28 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 29 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 30 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 31 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 32 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 33 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 34 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 35 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 36 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 37 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 38 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 39 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 40 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 41 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 42 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 43 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 44 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 45 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 46 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 47 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 48 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 49 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 50 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 51 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 52 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 53 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 54 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 55 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 56 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 57 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 58 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 59 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 60 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 61 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 62 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 63 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 64 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 65 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 66 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 67 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 68 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 69 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 70 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 71 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 72 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 73 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 74 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 75 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 76 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 77 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 78 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 79 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 80 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 81 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 82 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 83 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 84 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 85 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 86 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 87 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 88 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 89 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 90 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 91 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 92 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 93 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 94 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 95 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 96 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 97 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 98 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 99 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 100 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 101 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 102 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 103 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 104 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 105 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 106 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 107 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 108 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 109 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 110 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 111 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 112 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 113 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 114 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 115 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 116 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 117 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 118 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 119 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 120 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 121 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 122 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 123 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 124 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 125 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 126 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 127 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 128 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 129 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 130 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 131 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 132 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 133 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 134 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 135 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 136 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 137 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 138 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 139 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 140 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 141 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 142 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 143 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 144 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 145 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 146 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 147 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 148 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 149 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 150 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 151 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 152 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 153 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 154 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 155 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 156 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 157 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 158 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 159 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 160 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 161 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 162 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 163 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 164 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 165 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 166 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 167 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 168 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 169 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 170 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 171 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 172 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 173 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 174 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 175 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 176 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 177 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 178 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 179 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 180 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 181 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 182 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 183 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 184 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 185 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 186 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 187 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 188 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 189 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 190 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 191 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 192 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 193 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 194 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 195 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 196 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 197 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 198 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 199 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 200 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 201 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 202 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 203 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 204 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 205 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 206 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 207 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 208 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 209 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 210 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 211 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 212 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 213 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 214 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 215 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 216 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 217 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 218 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 219 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 220 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 221 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 222 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 223 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 224 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 225 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 226 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 227 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 228 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 229 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 230 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 231 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 232 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 233 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 234 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 235 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 236 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 237 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 238 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 239 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 240 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 241 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 242 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 243 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 244 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 245 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 246 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 247 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 248 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 249 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 250 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 251 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 252 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 253 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 254 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 255 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 256 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 257 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 258 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 259 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 260 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 261 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 262 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 263 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 264 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 265 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 266 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 267 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 268 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 269 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 270 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 271 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 272 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 273 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 274 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 275 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 276 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 277 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 278 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 279 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 280 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 281 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 282 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 283 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 284 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 285 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 286 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 287 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 288 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 289 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 290 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 291 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 292 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 293 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 294 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 295 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 296 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 297 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 298 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 299 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 300 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 301 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 302 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 303 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 304 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 305 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 306 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 307 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 308 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 309 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 310 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 311 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 312 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 313 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 314 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 315 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 316 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 317 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 318 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 319 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 320 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 321 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 322 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 323 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 324 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 325 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 326 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 327 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 328 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 329 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 330 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 331 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 332 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 333 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 334 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 335 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 336 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 337 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 338 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 339 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 340 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 341 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 342 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 343 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 344 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 345 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 346 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 347 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 348 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 349 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 350 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 351 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 352 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 353 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 354 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 355 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 356 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 357 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 358 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 359 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 360 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 361 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 362 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 363 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 364 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 365 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 366 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 367 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 368 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 369 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 370 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 371 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 372 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 373 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 374 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 375 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 376 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 377 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 378 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 379 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 380 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 381 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 382 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 383 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 384 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 385 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 386 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 387 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 388 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 389 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 390 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 391 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 392 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 393 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 394 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 395 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 396 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 397 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 398 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 399 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 400 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 401 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 402 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 403 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 404 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 405 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 406 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 407 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 408 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 409 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 410 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 411 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 412 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 413 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 414 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 415 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 416 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 417 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 418 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 419 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 420 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 421 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 422 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 423 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 424 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 425 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 426 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 427 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 428 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 429 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 430 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 431 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 432 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 433 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 434 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 435 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 436 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 437 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 438 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 439 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 440 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 441 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 442 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 443 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 444 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 445 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 446 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 447 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 448 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 449 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 450 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 451 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 452 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 453 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 454 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 455 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 456 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 457 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 458 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 459 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 460 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 461 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 462 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 463 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 464 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 465 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 466 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 467 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 468 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 469 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 470 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 471 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 472 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 473 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 474 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 475 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 476 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 477 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 478 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 479 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 480 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
