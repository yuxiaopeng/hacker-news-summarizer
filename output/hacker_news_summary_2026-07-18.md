# Hacker News 热门文章摘要 (2026-07-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Waldi：一个静谧的写作与被阅读空间。

**原文标题**: Waldi: A quiet place to write, and to be read

**原文链接**: [https://github.com/waaldev/waldi](https://github.com/waaldev/waldi)

Waldi 是一款专业的博客平台，旨在通过确保作者的声音被听到以及读者能够发现新视角，来培养“机缘巧合”（serendipity）。与受不透明算法支配的传统平台不同，Waldi 保证每篇博文至少能触达 100 位读者。其核心功能是“通配符”（wildcard）系统，每天向每位注册读者的收件箱随机推送一篇来自陌生人的博文。目前，阅读功能对所有人开放，但写作则采用邀请制，以维持精选的内容质量。

在技术层面，Waldi 为性能和简洁而生。后端使用 **Go** 语言编写，利用 **PostgreSQL** 进行数据存储，并采用 **Tiptap** 构建自定义的服务端验证文档模型。前端完全不使用框架，依赖手写的 CSS 和服务端渲染的 HTML。其架构通过 **Caddy** 和 **Cloudflare** 管理子域名及经验证的自定义域名，从而支持多租户模式。

核心架构亮点包括：
*   **Telegram 管理机器人：** 没有传统的 Web 管理面板；所有审核、用户邀请和内容筛选均通过 Telegram 机器人完成。
*   **极简基础设施：** 使用由 cron 触发的基于命令行（CLI）的后台任务，而非沉重的队列进程。
*   **优化的媒体资源：** 图片会自动转换为 WebP 格式并存储在兼容 S3 的存储（Cloudflare R2）中。
*   **国际化（i18n）：** 精简的翻译系统使用扁平的 JSON 目录来支持多语言，无需重复模板。

虽然该项目在 **MIT 许可证**下开源并支持自托管，但开发者指出，“受众保证循环”在官方的 waldi.blog 实例上效果最佳。开发工作通过 GitHub Actions 进行管理，路线图侧重于维持“宁静”的写作环境，并力求避开“极简引擎”的陈词滥调，转而追求有意义的内容分发。

---

## 2. In-toto：保障软件供应链完整性的框架

**原文标题**: In-toto: A framework to secure the integrity of software supply chains

**原文链接**: [https://in-toto.io/](https://in-toto.io/)

**总结：In-toto 框架**

In-toto 是一个开源框架，旨在保护软件供应链从启动到最终用户安装的全过程完整性。其主要目的是通过记录软件生命周期的每一个步骤来提供完全的透明度，确保用户能够验证执行了哪些操作、执行者是谁以及操作发生的具体顺序。

该框架构建于开放且可扩展的元数据标准之上，使其能够适应各种软件交付流水线。为了支持实施，in-toto 提供了一套基于 Apache 许可证发布的完备工具和库。

值得注意的是，in-toto 是云原生计算基金会 (CNCF) 的“毕业”项目，这一地位反映了其成熟度、安全性，以及作为保障现代软件分发安全的标准所获得的广泛采用。

---

## 3. Show HN：宜家复杂度指数

**原文标题**: Show HN: IKEA Complexity Index

**原文链接**: [https://ikea.greg.technology/](https://ikea.greg.technology/)

根据提供的文本，**宜家复杂度指数**（IKEA Complexity Index）是一个在 Hacker News 上分享的项目，旨在量化并对宜家产品的组装难度进行排名。

该工具的主要特点包括：

*   **目标：** 为宜家家具提供一个数据驱动的“复杂度指数”，帮助用户了解组装某款产品可能面临的难度或耗时。
*   **数据来源：** 该指数专注于拥有“单份 PDF”说明书的产品，可能通过分析官方手册中列出的步骤数、页数或零件数量等要素来进行评估。
*   **范围：** 该项目目前涵盖了宜家所有产品类别的项目。

在目前的状态下，该网站似乎是一个数据密集型应用，它将这些指标汇总成一个可搜索或可筛选的列表，方便消费者在购买前对比组装不同家具所需的精力。

---

## 4. DrDroid (YC W23) 正在招聘

**原文标题**: DrDroid (YC W23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory](https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory)

**DrDroid** 是一家由 Y Combinator (W23) 和 Accel 支持的初创公司，目前正为其位于**印度班加罗尔**的团队招聘一名**产品工程师 (Product Engineer)**。

**公司使命**
DrDroid 为平台和基础设施团队构建 AI 智能体 (AI Agents)。其目标是实现生产环境问题的分拣、调试和修复自动化，从而减轻 On-call 轮值负担。此外，他们还维护着 *Playbooks*（运维手册自动化）和 *Kenobi*（事件分析）等开源项目。

**岗位职责**
公司正在寻找一名拥有一年以上经验、能够将用户需求转化为技术解决方案的全栈工程师。
*   **核心技能：** JavaScript、Python、TypeScript，以及对分布式系统的理解。
*   **薪酬待遇：** 170 万 – 210 万卢比 (INR)，外加 0.01% – 0.10% 的股权。
*   **工作地点：** 班加罗尔实地办公（或愿意搬迁至此）。

**招聘流程**
招聘流程旨在高效快捷，目标是在提交申请后的七天内得出最终结果。流程包括：
1.  **强制性技术作业：** 候选人在进入后续环节前，必须完成职位描述中链接的特定任务。
2.  **CTO 面试：** 技术与战略层面的深入讨论。
3.  **工程师面试：** 同行级别的技术评估。

该岗位非常适合那些热衷于构建工具以改善工程师工作体验，并能在充满活力的初创环境中迅速成长的开发者。

---

## 5. 我开始写“泥土笔记本”了。

**原文标题**: I started a “dirt notebook”

**原文链接**: [https://pinewind.bearblog.dev/i-started-a-dirt-notebook/](https://pinewind.bearblog.dev/i-started-a-dirt-notebook/)

在这篇文章中，作者探讨了笔记记录中常见的一个困扰：过度整理和“美化”笔记本，以至于它们变得过于珍贵，不舍得日常使用。这种完美主义形成了一个“恶性循环”：随手涂鸦的心理门槛变得如此之高，导致作者不断放弃旧笔记本去开启新的。

为了打破这一习惯，作者创建了一个绰号为“排水渠”的**“脏笔记”**。这个专属空间被刻意设计得毫无美感，以抵制完美主义。通过使用一个纸质低劣、透墨且无法平摊的旧笔记本，作者被迫使用廉价圆珠笔并接受潦草的字迹。

一周后，作者总结了以下几点好处：
*   **创作自由：** 笔记本成了记录随机引文、故事构思、生活感悟和零散备忘的原始意识流空间。
*   **减少阻力：** 缺乏固定结构让即时捕捉灵感变得更加容易。
*   **提高留存：** 在周末回顾潦草的笔记，让作者能够重新发现被遗忘的想法。

作者的最终目标是写满这本“脏笔记”并学会接纳混乱。一旦克服了对完美整理的执念，作者计划回归使用高品质纸张和钢笔，而不再担心会“毁掉”笔记本。

---

## 6. 再探 Yliluoma 有序抖动算法

**原文标题**: Revisiting Yliluoma's ordered dither algorithm

**原文链接**: [https://30fps.net/pages/revisiting-yliluoma-2/](https://30fps.net/pages/revisiting-yliluoma-2/)

本文探讨了 Joel Yliluoma 在 2011 年提出的有序抖动算法（特别是 "Yliluoma-2"），并将其作为传统方法（如 Adobe Photoshop 中使用的 Thomas Knoll 算法）的高质量替代方案。

作者首先解释了旨在实现“局部均值再现”的“N 候选”方法。该原则确保抖动后的图像在从远处观察时，视觉上与原色一致。Knoll 的算法通过误差补偿循环实现这一目标——即通过不断移动目标点以寻找互补的调色板颜色——而 Yliluoma 的方法则利用了指数移动平均（EMA）。

Yliluoma-2 的核心在于通过几何上的“线段最近点”测试来选择候选调色板颜色。对于每个像素，该算法会识别出一个调色板颜色，当该颜色与当前的运行平均值混合时，产生的点最接近原始输入颜色。

作者提出的关键见解与改进包括：
*   **简化色彩公式**：作者认为通常不需要复杂的感知色差公式。相反，通过对图像进行亮度加权（强调绿色和明亮通道）预处理，即可获得类似的高质量结果。
*   **解析优化**：作者没有采用 Yliluoma 原始的“参数扫描”法来寻找最佳混合因子 ($t$)，而是提供了一种利用点积的解析解，显著提高了效率。
*   **几何精化**：作者建议对混合因子进行限制（例如 $t \geq 0.2$），以防止算法停滞在单一颜色上，从而确保更好的候选分布。

最终，本文通过几何原理解构了 Yliluoma 复杂的 C++ 实现，提供了一个现代化且简化的算法版本。

---

## 7. 静态搜索树：比二分查找快40倍 (2024)

**原文标题**: Static search trees: 40x faster than binary search (2024)

**原文链接**: [https://curiouscoding.nl/posts/static-search-tree/](https://curiouscoding.nl/posts/static-search-tree/)

本文详细介绍了如何优化静态搜索树（S-trees），以实现远高于标准二分查找的吞吐量，特别针对 32 位无符号整数。

**核心问题**
标准二分查找在现代硬件上效率低下，因为它每次会获取 64 字节的完整缓存行，却仅利用其中 4 字节的数据。虽然 Eytzinger 布局通过优化数据组织形式以实现有效预取，从而提升了性能，但其内存带宽利用率依然不高。

**S-Tree 解决方案**
为了最大限度地利用缓存行，作者采用了 S-trees（B+ 树的一种静态变体）。通过将 15-16 个值打包进单个缓存行，搜索过程从二叉转变为 16 叉或 17 叉。这显著增加了分支因子，意味着从内存中获取结果所需的缓存行读取次数更少。

**关键优化**
*   **SIMD 与 AVX2：** 作者使用手写 SIMD 指令同时在包含 16 个值的单个节点内进行搜索，大幅缩短了每个节点的处理时间。
*   **批处理与预取：** 查询不再是逐个处理，而是成批处理。这使得 CPU 能够重叠多个查询的高延迟内存获取操作，从而有效隐藏等待内存响应的时间。
*   **内存管理：** 该实现利用 2MB 巨页（Hugepages）来减轻转换后备缓冲区（TLB）的压力，加快了大型数据集的虚拟地址到物理地址的转换。
*   **布局精简：** 作者探索了包括“前缀分区”在内的多种内存布局，以进一步减少树上层结构的占用空间。

**结论**
通过将硬件感知的内存布局、SIMD 加速的节点搜索以及查询批处理相结合，作者证明了在基因组数据索引等高吞吐量场景下，静态搜索树的性能最高可达标准库二分查找的 40 倍。

---

## 8. Funny item co-occurrences in 3.2M Instacart orders

**原文标题**: Funny item co-occurrences in 3.2M Instacart orders

**原文链接**: [https://rogerdickey.com/funny-item-co-occurrences-in-3-million-instacart-orders/](https://rogerdickey.com/funny-item-co-occurrences-in-3-million-instacart-orders/)

生成摘要时出错

---

## 9. Roko's Dancing Basilisk

**原文标题**: Roko's Dancing Basilisk

**原文链接**: [https://boston.conman.org/2025/12/02.1](https://boston.conman.org/2025/12/02.1)

生成摘要时出错

---

## 10. Stenchill: 3D Printable Solder Paste Stencil Generator

**原文标题**: Stenchill: 3D Printable Solder Paste Stencil Generator

**原文链接**: [https://www.stenchill.com/en/](https://www.stenchill.com/en/)

生成摘要时出错

---

## 11. Overtraining as the path to human-like AI

**原文标题**: Overtraining as the path to human-like AI

**原文链接**: [https://www.seangoedecke.com/overtraining-as-the-path-to-human-like-ai/](https://www.seangoedecke.com/overtraining-as-the-path-to-human-like-ai/)

生成摘要时出错

---

## 12. Traders are increasingly betting against SpaceX just weeks after IPO

**原文标题**: Traders are increasingly betting against SpaceX just weeks after IPO

**原文链接**: [https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5](https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5)

生成摘要时出错

---

## 13. Open Book Touch: open-source e-reader

**原文标题**: Open Book Touch: open-source e-reader

**原文链接**: [https://www.crowdsupply.com/oddly-specific-objects/open-book-touch](https://www.crowdsupply.com/oddly-specific-objects/open-book-touch)

生成摘要时出错

---

## 14. Painting the sides of railroad rails white to reduce derailment

**原文标题**: Painting the sides of railroad rails white to reduce derailment

**原文链接**: [https://www.up.com/news/safety/Tracking-Rail-Heat-260608](https://www.up.com/news/safety/Tracking-Rail-Heat-260608)

生成摘要时出错

---

## 15. An Update on Igalia's Layer Based SVG Engine in WebKit (Reducing Layer Overhead)

**原文标题**: An Update on Igalia's Layer Based SVG Engine in WebKit (Reducing Layer Overhead)

**原文链接**: [https://blogs.igalia.com/nzimmermann/posts/2026-07-14-lbse-conditional-layers/](https://blogs.igalia.com/nzimmermann/posts/2026-07-14-lbse-conditional-layers/)

生成摘要时出错

---

## 16. Topcoat: The full full-stack framework for Rust

**原文标题**: Topcoat: The full full-stack framework for Rust

**原文链接**: [https://github.com/tokio-rs/topcoat](https://github.com/tokio-rs/topcoat)

生成摘要时出错

---

## 17. Lego building instructions through time

**原文标题**: Lego building instructions through time

**原文链接**: [https://www.lego.com/en-us/history/articles/d-lego-building-instructions-through-time](https://www.lego.com/en-us/history/articles/d-lego-building-instructions-through-time)

生成摘要时出错

---

## 18. Kimi K3: Open Frontier Intelligence

**原文标题**: Kimi K3: Open Frontier Intelligence

**原文链接**: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)

生成摘要时出错

---

## 19. Battery packs: Let's talk about crates, baby

**原文标题**: Battery packs: Let's talk about crates, baby

**原文链接**: [https://smallcultfollowing.com/babysteps/blog/2026/07/15/battery-packs/](https://smallcultfollowing.com/babysteps/blog/2026/07/15/battery-packs/)

生成摘要时出错

---

## 20. Vāgdhenu: A Sanskrit Chanting TTS System

**原文标题**: Vāgdhenu: A Sanskrit Chanting TTS System

**原文链接**: [https://prathosh.in/vagdhenu/](https://prathosh.in/vagdhenu/)

生成摘要时出错

---

## 21. Surrender as a non-stupid life strategy

**原文标题**: Surrender as a non-stupid life strategy

**原文链接**: [https://sashachapin.substack.com/p/should-you-be-in-charge-of-your-life](https://sashachapin.substack.com/p/should-you-be-in-charge-of-your-life)

生成摘要时出错

---

## 22. Show HN: A zoomable timeline of 4M Wikipedia events

**原文标题**: Show HN: A zoomable timeline of 4M Wikipedia events

**原文链接**: [https://app.everything.diena.co/](https://app.everything.diena.co/)

生成摘要时出错

---

## 23. The state of open source AI

**原文标题**: The state of open source AI

**原文链接**: [https://stateofopensource.ai/](https://stateofopensource.ai/)

生成摘要时出错

---

## 24. How early SunOS did diskless workstations before NFS

**原文标题**: How early SunOS did diskless workstations before NFS

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/solaris/SunOSDisklessWithoutNFS](https://utcc.utoronto.ca/~cks/space/blog/solaris/SunOSDisklessWithoutNFS)

生成摘要时出错

---

## 25. Three ways people respond to a problem (other than solving it)

**原文标题**: Three ways people respond to a problem (other than solving it)

**原文链接**: [https://improvesomething.today/responses-to-problems/](https://improvesomething.today/responses-to-problems/)

生成摘要时出错

---

## 26. Steam Machine: Between 12k and 15k Units Sold per week

**原文标题**: Steam Machine: Between 12k and 15k Units Sold per week

**原文链接**: [https://boilingsteam.com/steam-machine-between-10k-and-15k-sold-per-week/](https://boilingsteam.com/steam-machine-between-10k-and-15k-sold-per-week/)

生成摘要时出错

---

## 27. Show HN: Watch bots interact with an SSH honeypot in real time

**原文标题**: Show HN: Watch bots interact with an SSH honeypot in real time

**原文链接**: [https://honeypotlive.cc/](https://honeypotlive.cc/)

生成摘要时出错

---

## 28. Frank Lloyd Wright’s first home

**原文标题**: Frank Lloyd Wright’s first home

**原文链接**: [https://www.architecturaldigest.com/story/frank-lloyd-wright-home-and-studio-everything-you-need-to-know](https://www.architecturaldigest.com/story/frank-lloyd-wright-home-and-studio-everything-you-need-to-know)

生成摘要时出错

---

## 29. Engineering Peace

**原文标题**: Engineering Peace

**原文链接**: [https://asteriskmag.com/issues/14/engineering-peace](https://asteriskmag.com/issues/14/engineering-peace)

生成摘要时出错

---

## 30. Why do AI company logos look like buttholes? (2025)

**原文标题**: Why do AI company logos look like buttholes? (2025)

**原文链接**: [https://velvetshark.com/ai-company-logos-that-look-like-buttholes](https://velvetshark.com/ai-company-logos-that-look-like-buttholes)

生成摘要时出错

---

## 31. Camera Chase Vehicle

**原文标题**: Camera Chase Vehicle

**原文链接**: [https://transistor-man.com/gimbal_camera_rover.html](https://transistor-man.com/gimbal_camera_rover.html)

生成摘要时出错

---

## 32. More Bounce to the Ounce

**原文标题**: More Bounce to the Ounce

**原文链接**: [https://mceglowski.substack.com/p/more-bounce-to-the-ounce](https://mceglowski.substack.com/p/more-bounce-to-the-ounce)

生成摘要时出错

---

## 33. Porting nanochat to a TPU: what carries over from PyTorch, and what breaks

**原文标题**: Porting nanochat to a TPU: what carries over from PyTorch, and what breaks

**原文链接**: [https://github.com/tucan9389/nanochat-jax/discussions/1](https://github.com/tucan9389/nanochat-jax/discussions/1)

生成摘要时出错

---

## 34. Kaiser nurses say AI, surveillance are making their jobs and patient care worse

**原文标题**: Kaiser nurses say AI, surveillance are making their jobs and patient care worse

**原文链接**: [https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/)

生成摘要时出错

---

## 35. Evidence of inconsistencies in evaluation process and selection of winners

**原文标题**: Evidence of inconsistencies in evaluation process and selection of winners

**原文链接**: [https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423)

生成摘要时出错

---

## 36. Workspaces – Explore the workspaces of modern creators

**原文标题**: Workspaces – Explore the workspaces of modern creators

**原文链接**: [https://workspaces.xyz/](https://workspaces.xyz/)

生成摘要时出错

---

## 37. Designing emoji for the way we communicate today

**原文标题**: Designing emoji for the way we communicate today

**原文链接**: [https://blog.google/products-and-platforms/platforms/android/world-emoji-day-noto-3d/](https://blog.google/products-and-platforms/platforms/android/world-emoji-day-noto-3d/)

生成摘要时出错

---

## 38. AI Meets Cryptography 2: What AI Found in OpenVM's ZkVM

**原文标题**: AI Meets Cryptography 2: What AI Found in OpenVM's ZkVM

**原文链接**: [https://blog.zksecurity.xyz/posts/openvm-bugs/](https://blog.zksecurity.xyz/posts/openvm-bugs/)

生成摘要时出错

---

## 39. Latent Space as a New Medium

**原文标题**: Latent Space as a New Medium

**原文链接**: [https://kevinkelly.substack.com/p/latent-space-as-a-new-medium](https://kevinkelly.substack.com/p/latent-space-as-a-new-medium)

生成摘要时出错

---

## 40. Lobste.rs is now running on SQLite

**原文标题**: Lobste.rs is now running on SQLite

**原文链接**: [https://lobste.rs/s/ko1ji1](https://lobste.rs/s/ko1ji1)

生成摘要时出错

---

## 41. FAA lets Boeing sign off on 737 MAX, 787 airworthiness certificates again

**原文标题**: FAA lets Boeing sign off on 737 MAX, 787 airworthiness certificates again

**原文链接**: [https://www.cnbc.com/2026/07/17/faa-boeing-737-max-787.html](https://www.cnbc.com/2026/07/17/faa-boeing-737-max-787.html)

生成摘要时出错

---

## 42. GitRoot

**原文标题**: GitRoot

**原文链接**: [https://gitroot.dev/](https://gitroot.dev/)

生成摘要时出错

---

## 43. MoonBASIC: A modern BASIC for building 2D and 3D games

**原文标题**: MoonBASIC: A modern BASIC for building 2D and 3D games

**原文链接**: [https://github.com/CharmingBlaze/moonbasic](https://github.com/CharmingBlaze/moonbasic)

生成摘要时出错

---

## 44. CD sales growth outpaced vinyl in the first half of 2026

**原文标题**: CD sales growth outpaced vinyl in the first half of 2026

**原文链接**: [https://consequence.net/2026/07/the-cd-revival-is-getting-hard-to-ignore/](https://consequence.net/2026/07/the-cd-revival-is-getting-hard-to-ignore/)

生成摘要时出错

---

## 45. Moonstone: Modern, cross-platform Lua runtime and package manager written in Zig

**原文标题**: Moonstone: Modern, cross-platform Lua runtime and package manager written in Zig

**原文链接**: [https://moonstone.sh/](https://moonstone.sh/)

生成摘要时出错

---

## 46. The LLM Critics Are Right. I Use LLMs Anyway

**原文标题**: The LLM Critics Are Right. I Use LLMs Anyway

**原文链接**: [https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

生成摘要时出错

---

## 47. Apple targets dozens of OpenAI employees with legal letters

**原文标题**: Apple targets dozens of OpenAI employees with legal letters

**原文链接**: [https://www.ft.com/content/1b8c9d52-88a9-426b-ba47-f1811f859166](https://www.ft.com/content/1b8c9d52-88a9-426b-ba47-f1811f859166)

生成摘要时出错

---

## 48. Faster binary search: from compiled code to mechanical sympathy

**原文标题**: Faster binary search: from compiled code to mechanical sympathy

**原文链接**: [https://pythonspeed.com/articles/branchless-binary-search/](https://pythonspeed.com/articles/branchless-binary-search/)

生成摘要时出错

---

## 49. Three workers digging in a field outside the data center

**原文标题**: Three workers digging in a field outside the data center

**原文链接**: [https://sign2.nl/websign/three-workers-digging-in-a-field-outside-the-data-center-by-dinnis-van-dijken/](https://sign2.nl/websign/three-workers-digging-in-a-field-outside-the-data-center-by-dinnis-van-dijken/)

生成摘要时出错

---

## 50. How Has Roman Concrete Lasted for Millennia? 1,900-Year-Old Latrine Offers Clues

**原文标题**: How Has Roman Concrete Lasted for Millennia? 1,900-Year-Old Latrine Offers Clues

**原文链接**: [https://www.smithsonianmag.com/smart-news/how-has-roman-concrete-lasted-for-millennia-a-1900-year-old-latrine-offers-new-clues-about-the-materials-impressive-durability-180989115/](https://www.smithsonianmag.com/smart-news/how-has-roman-concrete-lasted-for-millennia-a-1900-year-old-latrine-offers-new-clues-about-the-materials-impressive-durability-180989115/)

生成摘要时出错

---

## 51. Microsoft Comic Chat is now open source

**原文标题**: Microsoft Comic Chat is now open source

**原文链接**: [https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/)

生成摘要时出错

---

## 52. The Isomorphic Labs Drug Design Engine unlocks a new frontier beyond AlphaFold

**原文标题**: The Isomorphic Labs Drug Design Engine unlocks a new frontier beyond AlphaFold

**原文链接**: [https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier)

生成摘要时出错

---

## 53. VulnHunter: Capital One's agentic AI code security tool

**原文标题**: VulnHunter: Capital One's agentic AI code security tool

**原文链接**: [https://www.capitalone.com/tech/open-source/announcing-vulnhunter/](https://www.capitalone.com/tech/open-source/announcing-vulnhunter/)

生成摘要时出错

---

## 54. Mac gaming is finally getting the overpowered upgrade it deserves

**原文标题**: Mac gaming is finally getting the overpowered upgrade it deserves

**原文链接**: [https://www.macworld.com/article/3189951/apples-latest-game-porting-toolkit-beta-changed-how-i-think-about-mac-gaming.html](https://www.macworld.com/article/3189951/apples-latest-game-porting-toolkit-beta-changed-how-i-think-about-mac-gaming.html)

生成摘要时出错

---

## 55. Homomorphically encrypted CIFAR-10 inference in 200ms

**原文标题**: Homomorphically encrypted CIFAR-10 inference in 200ms

**原文链接**: [https://sofar.belfortlabs.cloud/](https://sofar.belfortlabs.cloud/)

生成摘要时出错

---

## 56. How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文标题**: How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文链接**: [https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

生成摘要时出错

---

## 57. Helium escaping from atmosphere of nearby rocky exoplanet in a habitable zone

**原文标题**: Helium escaping from atmosphere of nearby rocky exoplanet in a habitable zone

**原文链接**: [https://www.science.org/doi/10.1126/science.aea9708](https://www.science.org/doi/10.1126/science.aea9708)

生成摘要时出错

---

## 58. Decoy Font

**原文标题**: Decoy Font

**原文链接**: [https://www.mixfont.com/experiments/decoy-font](https://www.mixfont.com/experiments/decoy-font)

生成摘要时出错

---

## 59. Mathematics of Data Science

**原文标题**: Mathematics of Data Science

**原文链接**: [https://arxiv.org/abs/2607.11938](https://arxiv.org/abs/2607.11938)

生成摘要时出错

---

## 60. Ente – Opening Our Books

**原文标题**: Ente – Opening Our Books

**原文链接**: [https://ente.com/open/](https://ente.com/open/)

生成摘要时出错

---

## 61. Claude Code(Fable) refused my slow down instruction

**原文标题**: Claude Code(Fable) refused my slow down instruction

**原文链接**: [https://qusaisuwan.github.io/cc-incident/index.html](https://qusaisuwan.github.io/cc-incident/index.html)

生成摘要时出错

---

## 62. The lost joy of music piracy

**原文标题**: The lost joy of music piracy

**原文链接**: [https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming](https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming)

生成摘要时出错

---

## 63. Goes-19 weather satellite enters Safe Hold mode

**原文标题**: Goes-19 weather satellite enters Safe Hold mode

**原文链接**: [https://www.spaceweather.gov/news/goes-19-safe-hold](https://www.spaceweather.gov/news/goes-19-safe-hold)

生成摘要时出错

---

## 64. ASCII Art

**原文标题**: ASCII Art

**原文链接**: [https://github.com/doctorfree/Asciiville](https://github.com/doctorfree/Asciiville)

生成摘要时出错

---

## 65. Estimating the heights of New Yorkers from their scuff marks

**原文标题**: Estimating the heights of New Yorkers from their scuff marks

**原文链接**: [https://blog.jse.li/posts/smith9street/](https://blog.jse.li/posts/smith9street/)

生成摘要时出错

---

## 66. Pebble Mega Update – July 2026

**原文标题**: Pebble Mega Update – July 2026

**原文链接**: [https://repebble.com/blog/pebble-mega-update-july-2026](https://repebble.com/blog/pebble-mega-update-july-2026)

生成摘要时出错

---

## 67. The case for eating more organ meat

**原文标题**: The case for eating more organ meat

**原文链接**: [https://www.nationalgeographic.com/health/article/offal-organ-meat-nutrition-health](https://www.nationalgeographic.com/health/article/offal-organ-meat-nutrition-health)

生成摘要时出错

---

## 68. Quintile – keyboard N×M grid tiling for macOS

**原文标题**: Quintile – keyboard N×M grid tiling for macOS

**原文链接**: [https://github.com/stefanopineda/quintile](https://github.com/stefanopineda/quintile)

生成摘要时出错

---

## 69. British Steel taken into public ownership to protect 'vital' UK supply

**原文标题**: British Steel taken into public ownership to protect 'vital' UK supply

**原文链接**: [https://www.bbc.com/news/articles/c5y680w62wno](https://www.bbc.com/news/articles/c5y680w62wno)

生成摘要时出错

---

## 70. Frame – Linux X server in Assembly

**原文标题**: Frame – Linux X server in Assembly

**原文链接**: [https://isene.org/2026/07/Frame.html](https://isene.org/2026/07/Frame.html)

生成摘要时出错

---

## 71. Starlink from 1984

**原文标题**: Starlink from 1984

**原文链接**: [https://nemanjatrifunovic.substack.com/p/starlink-from-1984](https://nemanjatrifunovic.substack.com/p/starlink-from-1984)

生成摘要时出错

---

## 72. Inkling: Our Open-Weights Model

**原文标题**: Inkling: Our Open-Weights Model

**原文链接**: [https://thinkingmachines.ai/news/introducing-inkling/](https://thinkingmachines.ai/news/introducing-inkling/)

生成摘要时出错

---

## 73. 'Likweli': A new monkey species discovered in the Congo Basin

**原文标题**: 'Likweli': A new monkey species discovered in the Congo Basin

**原文链接**: [https://news.yale.edu/2026/07/15/meet-likweli-new-monkey-species-discovered-congo-basin](https://news.yale.edu/2026/07/15/meet-likweli-new-monkey-species-discovered-congo-basin)

生成摘要时出错

---

## 74. Turn your singing voice into printable notes (in the browser)

**原文标题**: Turn your singing voice into printable notes (in the browser)

**原文链接**: [https://om-intelligence.ch/projects/vocal-notation/vocal-notation.html](https://om-intelligence.ch/projects/vocal-notation/vocal-notation.html)

生成摘要时出错

---

## 75. A Road to Lisp: Which Lisp

**原文标题**: A Road to Lisp: Which Lisp

**原文链接**: [https://scotto.me/blog/2026-07-17-which-lisp/](https://scotto.me/blog/2026-07-17-which-lisp/)

生成摘要时出错

---

## 76. Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文标题**: Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文链接**: [https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/](https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/)

生成摘要时出错

---

## 77. Sony deletes more movies from the accounts of people who ‘bought’ them

**原文标题**: Sony deletes more movies from the accounts of people who ‘bought’ them

**原文链接**: [https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/)

生成摘要时出错

---

## 78. Why is tiny Norway so good at sports? It's more than Erling Haaland

**原文标题**: Why is tiny Norway so good at sports? It's more than Erling Haaland

**原文链接**: [https://www.csmonitor.com/World/Europe/2026/0710/norway-erling-haaland-soccer-youth-sports-competition-training](https://www.csmonitor.com/World/Europe/2026/0710/norway-erling-haaland-soccer-youth-sports-competition-training)

生成摘要时出错

---

## 79. EEG shows brain can simultaneous encode two speech streams

**原文标题**: EEG shows brain can simultaneous encode two speech streams

**原文链接**: [https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003876](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003876)

生成摘要时出错

---

## 80. AI Mania Is Eviscerating Global Decision-Making

**原文标题**: AI Mania Is Eviscerating Global Decision-Making

**原文链接**: [https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/)

生成摘要时出错

---

## 81. Show HN: Clx – Compile Lua to Native Executables Through C++20

**原文标题**: Show HN: Clx – Compile Lua to Native Executables Through C++20

**原文链接**: [https://github.com/samyeyo/clx](https://github.com/samyeyo/clx)

生成摘要时出错

---

## 82. Aurora DSQL: Scalable, Multi-Region OLTP

**原文标题**: Aurora DSQL: Scalable, Multi-Region OLTP

**原文链接**: [https://arxiv.org/abs/2607.13276](https://arxiv.org/abs/2607.13276)

生成摘要时出错

---

## 83. If you want to create a button from scratch, you must first create the universe

**原文标题**: If you want to create a button from scratch, you must first create the universe

**原文链接**: [https://madcampos.dev/blog/2026/07/accessibility-from-scratch/](https://madcampos.dev/blog/2026/07/accessibility-from-scratch/)

生成摘要时出错

---

## 84. $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol

**原文标题**: $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol

**原文链接**: [https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

生成摘要时出错

---

## 85. Pseudpocalypse

**原文标题**: Pseudpocalypse

**原文链接**: [https://dynomight.net/pseudpocalypse/](https://dynomight.net/pseudpocalypse/)

生成摘要时出错

---

## 86. OnePlus halts operations in USA and Europe

**原文标题**: OnePlus halts operations in USA and Europe

**原文链接**: [https://community.oneplus.com/thread/2170715118587871237](https://community.oneplus.com/thread/2170715118587871237)

生成摘要时出错

---

## 87. NotebookLM is now Gemini Notebook

**原文标题**: NotebookLM is now Gemini Notebook

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)

生成摘要时出错

---

## 88. Tannakian Reconstruction

**原文标题**: Tannakian Reconstruction

**原文链接**: [https://bartoszmilewski.com/2026/07/14/tannakian-reconstruction/](https://bartoszmilewski.com/2026/07/14/tannakian-reconstruction/)

生成摘要时出错

---

