# Hacker News 热门文章摘要 (2026-06-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 因漏气修复避险后，宇航员受命返回国际空间站。

**原文标题**: Astronauts told to return to ISS after sheltering over air leak repairs

**原文链接**: [https://www.bbc.com/news/live/c4g44ew3g1kt](https://www.bbc.com/news/live/c4g44ew3g1kt)

国际空间站（ISS）上的五名宇航员在俄罗斯舱段维修期间，于对接的飞船内采取避险措施后，现已返回空间站主舱。在两名俄罗斯航天员修复“星辰”号服务舱转移通道的漏气点时，机组人员接到指令，采取了“提升安全防范级别”的姿态。

据美国国家航空航天局（NASA）称，该特定舱段一段时间以来一直饱受裂缝和漏气问题的困扰。俄罗斯国际文传电讯社报道，俄罗斯国家航天集团（Roscosmos）在最近的任务中发现了两处漏气点，其中一处已成功修复。

NASA发言人贝瑟尼·史蒂文斯表示，由于工程师正在评估测量结果和数据，结构修复工作已暂时暂停。尽管漏气问题反复出现，但NASA和俄罗斯国家航天集团均确认，机组人员及空间站机载系统在整个过程中始终保持安全。

---

## 2. pg_durable：微软开源数据库内持久执行

**原文标题**: pg_durable: Microsoft open sources in-database durable execution

**原文链接**: [https://github.com/microsoft/pg_durable](https://github.com/microsoft/pg_durable)

微软开源了 **pg_durable**，这是一个专为**持久化执行（durable execution）**设计的 PostgreSQL 扩展。它允许工程师直接在数据库内使用 SQL 构建长耗时、容错的工作流。通过为工作流图的每个步骤设置检查点，pg_durable 确保进程在崩溃、重启或失败后能从上一个成功状态自动恢复，从而消除了手动重建状态的必要。

**核心特性与优势：**
*   **降低复杂性：** 它取代了外部编排器（如 Temporal 或 Airflow）以及碎片化的“cron + 队列 + 工作节点”配置，使计算更贴近数据。
*   **原生 SQL DSL：** 工作流使用可组合的 SQL 语法定义（例如，使用 `~>` 表示顺序执行，使用 `|=>` 表示管道传输），并通过标准 SQL 命令进行管理。
*   **运维可见性：** 进度和状态存储在标准 Postgres 表中，可以使用熟悉的工具对工作流进行审计。
*   **应用场景：** 非常适合向量嵌入流水线、批量数据摄取、定期维护以及并行的“扇出”聚合。

**技术架构：**
pg_durable 基于 Rust 和 `pgrx` 框架构建，作为 PostgreSQL 进程内的后台工作线程运行。它利用 `duroxide` 编排库进行确定性回放和状态管理。该扩展支持 PostgreSQL 17 和 18，并包含行级安全性（RLS），以确保用户只能管理自己的工作流实例。

**局限性：**
该工具专门围绕 SQL 设计。它不适用于亚毫秒级的同步请求，或需要复杂非 HTTP SDK 的逻辑，除非该逻辑被封装在 SQL 函数或外部 HTTP 端点中。

pg_durable 目前处于**预览阶段**，旨在为已将 PostgreSQL 作为主要状态存储的团队简化后端架构。

---

## 3. Gemma 4 QAT 模型：针对移动端与笔记本电脑优化压缩效率

**原文标题**: Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)

Google DeepMind 宣布发布 **Gemma 4 QAT 模型**，这是利用量化感知训练 (QAT) 优化的全新系列检查点。这些模型旨在通过在不牺牲质量的前提下显著降低显存需求，从而最大限度地提高手机、笔记本电脑和消费级 GPU 等边缘设备的性能和效率。

与通常会导致性能下降的标准训练后量化 (PTQ) 不同，QAT 将压缩过程集成到训练阶段，使模型在缩小体积的同时能够保持更高的准确度。此次发布的主要亮点包括：

*   **移动端优化：** 一种新型的专业移动量化方案将 **Gemma 4 E2B** 模型的内存占用降低至仅 **1GB**。这是通过静态激活、通道级量化以及针对 Token 生成层的定向 2-bit 量化实现的。
*   **性能格式：** 此次发布包含了主流的 **Q4_0** 格式检查点，确保在各种硬件上实现高速推理。
*   **模块化：** 为了进一步节省显存 (VRAM)，开发者可以部署特定模态的版本（例如纯文本版），从而移除不必要的音频或视觉编码器。
*   **生态集成：** 模型权重已在 Hugging Face 上以 **GGUF** 和压缩张量格式提供。它们兼容多种开发者工具，包括 llama.cpp、Ollama、LM Studio、vLLM 以及 Google 的 LiteRT-LM。

通过弥合高端 AI 能力与本地消费级硬件之间的差距，这些 QAT 模型让开发者能够以极低的内存开销，在日常设备上本地运行复杂的 Gemma 4 架构。

---

## 4. Cloudflare CEO 正就机器人流量激增一事对你撒谎

**原文标题**: Cloudflare CEO Is Lying to You About the Bot Traffic Jump

**原文链接**: [https://www.flyingpenguin.com/cloudflare-ceo-is-lying-to-you-about-the-bot-traffic-jump/](https://www.flyingpenguin.com/cloudflare-ceo-is-lying-to-you-about-the-bot-traffic-jump/)

这篇文章指出，Cloudflare 首席执行官 Matthew Prince 歪曲了数据，虚假声称机器人流量已首次超过人类流量。作者断言，Prince 的说法基于一种“伎俩”，即他采用了“仅限 HTML”的统计指标，却忽略了 Cloudflare 自身的“全流量”数据面板，而后者显示人类仍占据互联网活动约三分之二的份额。

作者强调了 Prince 叙述中的几处具体矛盾：

*   **AI 增长的错误分类：** 尽管 Prince 将流量激增归咎于“代理型”AI（代表用户操作的 AI），但作者指出，在 Cloudflare 的数据集中，这一类别实际上是占比最小的。
*   **爬虫的作用：** AI 流量的真实增长源于大规模训练爬虫（如 GPTBot 和 ClaudeBot），它们被用于构建模型，而非响应个人用户请求。
*   **数据虚增：** 作者声称，通过重复计算 Googlebot 以及错误呈现搜索引擎爬虫（这仍是最大的机器人类别），AI 流量数据被人为夸大了。

最终，文章将这些言论定性为一场欺骗性的营销辞令。作者认为，Prince 有意将“代理型”AI 与大规模抓取混为一谈，以此构建一套叙事来为其 Cloudflare 的“付费爬取”产品辩护，实际上是歪曲了自家公司的数据以驱动收入增长。

---

## 5. 约定式提交引导人们关注错误的事情

**原文标题**: Conventional Commits encourages focus on the wrong things

**原文链接**: [https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/](https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/)

在《常规提交（Conventional Commits）助长了错误的关注点》一文中，作者指出“常规提交”标准是一种有缺陷的实践，它将元数据置于有意义的上下文之上。

作者的核心批评在于，该标准优先考虑“类型”（如 `feat`、`fix`）而非“作用域”（代码更改的具体区域）。对于贡献者、调试者和事故响应者来说，作用域是查阅历史或定位 Bug 来源时最关键的信息。通过将作用域设为可选并将类型置于首位，“常规提交”完全搞错了优先级。

此外，作者认为提交类型通常是多余的——因为清晰的描述往往已隐含了类型——且具有局限性，因为许多提交无法简单地归入单一类别。文章还拆解了该标准所谓的几大优势：

*   **自动化变更日志：** 作者认为面向用户的变更日志与面向开发者的提交日志受众不同，不应从同一来源生成。
*   **自动化语义化版本（SemVer）：** 这被认为是不可靠的，因为它无法兼顾回滚、意外破坏或追溯修复等复杂情况。
*   **工具化/安全性：** 相比于对更改文件使用 `git diff`，依赖提交类型来触发 CI/CD 流程被视为一种安全风险。

作为替代方案，作者提倡“作用域提交”（Scoped Commits），这是 Linux、Git 和 Go 等成功项目采用的格式。该方法使用简单的 `作用域: 描述` 格式（如 `kernel: fix memory leak`）来提供即时且相关的上下文。为了推动这种“回归理性”，作者推出了 `scopedcommits.com`，敦促开发者优先考虑与项目相关的作用域，而非僵化的、便于自动化的类型。

---

## 6. Mouseless – 键盘驱动的 macOS/Linux/Windows 操控

**原文标题**: Mouseless – keyboard-driven control of macOS/Linux/Windows

**原文链接**: [https://mouseless.click](https://mouseless.click)

**Mouseless** 是一款跨平台软件工具，旨在仅通过键盘实现对计算机鼠标功能的高速控制。该应用兼容 **macOS、Linux 和 Windows**，旨在让用户在无需将手移开键盘的情况下导航操作系统，从而提升生产力和效率。

其核心宗旨是提供“闪电般快速”的光标控制，这主要通过键盘快捷键和特定的导航模式来实现。根据文中所述，该工具面向偏好在多种桌面环境中使用键盘驱动型工作流的高级用户。

---

## 7. I tested every IP KVM in my Homelab

**原文标题**: I tested every IP KVM in my Homelab

**原文链接**: [https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/](https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/)

The article explores the evolution of IP KVM (Keyboard, Video, Mouse) devices since the PiKVM’s 2017 debut, highlighting their utility for remote hardware management without requiring local software. Unlike VNC or SSH, IP KVMs provide BIOS-level access and function even when the target computer is frozen or powered off.

The author categorizes the current market into three main groups:

1.  **Premium/Open-Source Pioneers:** **PiKVM** and **TinyPilot** remain the gold standards. PiKVM offers a fully open-source stack and high-end features like 5G backup but carries a high price tag ($275–$400). TinyPilot targets business users with simplified setup, centralized management, and professional support.
2.  **Budget-Friendly Innovations:** Newer entries like **GL-iNet’s Comet** ($99) and **JetKVM** ($103) offer features like 4K support and polished UIs at a much lower price point. **Sipeed’s NanoKVM** ($70) represents the extreme budget end using RISC-V hardware, though its low cost and inconspicuous nature have reportedly made it a tool for corporate espionage, leading to an FBI visit for the author.
3.  **Specialized Form Factors:** Many brands now offer PCIe card versions for internal installation. Additionally, "direct-connect" options like **Openterface KVM-GO** and **Pi-Cast** allow users to control machines via a direct USB/VGA connection rather than over a standard LAN.

The author concludes with a strong security warning: because these devices provide deep access to hardware, they must be treated as potential security holes. Users should prioritize firewalls, frequent updates, and vendor trust when integrating an IP KVM into their network. For hobbyists, the market now offers a wide range of choices between premium open-source hardware and affordable, specialized clones.

---

## 8. New method turns ocean water into drinking water, without waste

**原文标题**: New method turns ocean water into drinking water, without waste

**原文链接**: [https://www.rochester.edu/newscenter/what-is-desalination-definition-ocean-water-704732/](https://www.rochester.edu/newscenter/what-is-desalination-definition-ocean-water-704732/)

生成摘要时出错

---

## 9. My Agent Skill for Test-Driven Development

**原文标题**: My Agent Skill for Test-Driven Development

**原文链接**: [https://www.saturnci.com/my-agent-skill-for-test-driven-development.html](https://www.saturnci.com/my-agent-skill-for-test-driven-development.html)

生成摘要时出错

---

## 10. Gov.uk has replaced Stripe with Dutch provider Adyen

**原文标题**: Gov.uk has replaced Stripe with Dutch provider Adyen

**原文链接**: [https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763](https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763)

生成摘要时出错

---

## 11. Mantine-datatable (and others) compromised – owner account suspended

**原文标题**: Mantine-datatable (and others) compromised – owner account suspended

**原文链接**: [https://github.com/icflorescu/mantine-datatable/discussions/813](https://github.com/icflorescu/mantine-datatable/discussions/813)

生成摘要时出错

---

## 12. Cooldown Support for Ruby Bundler

**原文标题**: Cooldown Support for Ruby Bundler

**原文链接**: [https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html](https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html)

生成摘要时出错

---

## 13. 深入 FAISS：十亿级相似性搜索

**原文标题**: Inside FAISS: Billion-Scale Similarity Search

**原文链接**: [https://fremaconsulting.ch/blog/faiss](https://fremaconsulting.ch/blog/faiss)

生成摘要时出错

---

## 14. Tracing a powerful GNSS interference source over Europe

**原文标题**: Tracing a powerful GNSS interference source over Europe

**原文链接**: [https://arxiv.org/abs/2606.03673](https://arxiv.org/abs/2606.03673)

生成摘要时出错

---

## 15. Did Claude increase bugs in rsync?

**原文标题**: Did Claude increase bugs in rsync?

**原文链接**: [https://alexispurslane.github.io/rsync-analysis/](https://alexispurslane.github.io/rsync-analysis/)

生成摘要时出错

---

## 16. 做最难的事

**原文标题**: Do the Hardest Thing

**原文链接**: [https://justinjackson.ca/hard-thing](https://justinjackson.ca/hard-thing)

生成摘要时出错

---

## 17. Sakana AI's Recursive Self-Improvement (RSI) Lab

**原文标题**: Sakana AI's Recursive Self-Improvement (RSI) Lab

**原文链接**: [https://sakana.ai/rsi-lab/](https://sakana.ai/rsi-lab/)

生成摘要时出错

---

## 18. Redis 8.8：新增数组数据结构、限流器及性能提升

**原文标题**: Redis 8.8: New array data structure, rate limiter, performance improvements

**原文链接**: [https://redis.io/blog/announcing-redis-8-8/](https://redis.io/blog/announcing-redis-8-8/)

生成摘要时出错

---

## 19. Nango (YC W23, dev infra) is hiring staff back end engineers

**原文标题**: Nango (YC W23, dev infra) is hiring staff back end engineers

**原文链接**: [https://nango.dev/careers](https://nango.dev/careers)

生成摘要时出错

---

## 20. Dutch gov't will only allow European company to operate DigiD platform

**原文标题**: Dutch gov't will only allow European company to operate DigiD platform

**原文链接**: [https://nltimes.nl/2026/06/05/dutch-govt-will-allow-european-company-operate-digid-platform](https://nltimes.nl/2026/06/05/dutch-govt-will-allow-european-company-operate-digid-platform)

生成摘要时出错

---

## 21. India's surprise baby bust

**原文标题**: India's surprise baby bust

**原文链接**: [https://www.economist.com/leaders/2026/06/04/indias-surprise-baby-bust-is-a-warning-to-the-world](https://www.economist.com/leaders/2026/06/04/indias-surprise-baby-bust-is-a-warning-to-the-world)

生成摘要时出错

---

## 22. "Maybe later" was a feature

**原文标题**: "Maybe later" was a feature

**原文链接**: [https://arnorhs.dev/posts/2026-06-04/maybe-later-was-a-feature/](https://arnorhs.dev/posts/2026-06-04/maybe-later-was-a-feature/)

生成摘要时出错

---

## 23. Show HN: Lowfat – pluggable CLI filter that saved 91.8% of my LLM tokens

**原文标题**: Show HN: Lowfat – pluggable CLI filter that saved 91.8% of my LLM tokens

**原文链接**: [https://github.com/zdk/lowfat](https://github.com/zdk/lowfat)

生成摘要时出错

---

## 24. C++: The Documentary

**原文标题**: C++: The Documentary

**原文链接**: [https://herbsutter.com/2026/06/04/c-the-documentary-released-today/](https://herbsutter.com/2026/06/04/c-the-documentary-released-today/)

生成摘要时出错

---

## 25. Entanglement Builds Space-Time. Now "Magic" Gives It Gravity

**原文标题**: Entanglement Builds Space-Time. Now "Magic" Gives It Gravity

**原文链接**: [https://www.quantamagazine.org/entanglement-builds-space-time-now-magic-gives-it-gravity-20260603/](https://www.quantamagazine.org/entanglement-builds-space-time-now-magic-gives-it-gravity-20260603/)

生成摘要时出错

---

## 26. Changing how we develop Ladybird

**原文标题**: Changing how we develop Ladybird

**原文链接**: [https://ladybird.org/posts/changing-how-we-develop-ladybird/](https://ladybird.org/posts/changing-how-we-develop-ladybird/)

生成摘要时出错

---

## 27. South Korean forums will need to scan every images with AI censorship tools

**原文标题**: South Korean forums will need to scan every images with AI censorship tools

**原文链接**: [https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

生成摘要时出错

---

## 28. ESP32 Bit Pirate, a Hardware Hacking Tool with WebCLI That Speaks Every Protocol

**原文标题**: ESP32 Bit Pirate, a Hardware Hacking Tool with WebCLI That Speaks Every Protocol

**原文链接**: [https://github.com/geo-tp/ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate)

生成摘要时出错

---

## 29. Fine-tuning an LLM to write docs like it's 1995

**原文标题**: Fine-tuning an LLM to write docs like it's 1995

**原文链接**: [https://passo.uno/fine-tuning-docs-llm/](https://passo.uno/fine-tuning-docs-llm/)

生成摘要时出错

---

## 30. Fine-tuning an LLM to write docs like it's 1995

**原文标题**: Fine-tuning an LLM to write docs like it's 1995

**原文链接**: [https://passo.uno/fine-tuning-docs-llm/](https://passo.uno/fine-tuning-docs-llm/)

生成摘要时出错

---

## 31. Lee Kuan Yew's Singapore Story (2023)

**原文标题**: Lee Kuan Yew's Singapore Story (2023)

**原文链接**: [https://www.historytoday.com/archive/feature/lee-kuan-yews-singapore-story](https://www.historytoday.com/archive/feature/lee-kuan-yews-singapore-story)

生成摘要时出错

---

## 32. Azure Linux 4.0 is Microsoft's first general-purpose Linux

**原文标题**: Azure Linux 4.0 is Microsoft's first general-purpose Linux

**原文链接**: [https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/](https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/)

生成摘要时出错

---

## 33. Meta enables ADB on deprecated Portal devices [video]

**原文标题**: Meta enables ADB on deprecated Portal devices [video]

**原文链接**: [https://fb.watch/HxPu0fSyeH/](https://fb.watch/HxPu0fSyeH/)

生成摘要时出错

---

## 34. Anthropic's open-source framework for AI-powered vulnerability discovery

**原文标题**: Anthropic's open-source framework for AI-powered vulnerability discovery

**原文链接**: [https://github.com/anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)

生成摘要时出错

---

## 35. Leap in DNA synthesis slashes time to build new genetic sequences

**原文标题**: Leap in DNA synthesis slashes time to build new genetic sequences

**原文链接**: [https://spectrum.ieee.org/faster-dna-synthesis-sidewinder](https://spectrum.ieee.org/faster-dna-synthesis-sidewinder)

生成摘要时出错

---

## 36. I'm skeptical about efforts to revolutionize schooling

**原文标题**: I'm skeptical about efforts to revolutionize schooling

**原文链接**: [https://www.scotthyoung.com/blog/2026/05/27/revolutionize-schooling/](https://www.scotthyoung.com/blog/2026/05/27/revolutionize-schooling/)

生成摘要时出错

---

## 37. databow: a Rust CLI to query any database with an ADBC driver

**原文标题**: databow: a Rust CLI to query any database with an ADBC driver

**原文链接**: [https://columnar.tech/blog/introducing-databow//](https://columnar.tech/blog/introducing-databow//)

生成摘要时出错

---

## 38. Open Code Review – An AI-powered code review CLI tool

**原文标题**: Open Code Review – An AI-powered code review CLI tool

**原文链接**: [https://github.com/alibaba/open-code-review](https://github.com/alibaba/open-code-review)

生成摘要时出错

---

## 39. At the Autograph Show

**原文标题**: At the Autograph Show

**原文链接**: [https://oldster.substack.com/p/at-the-autograph-show](https://oldster.substack.com/p/at-the-autograph-show)

生成摘要时出错

---

## 40. The IsUpMap lets you check the status of over 100 major sites at once

**原文标题**: The IsUpMap lets you check the status of over 100 major sites at once

**原文链接**: [https://isupmap.com/](https://isupmap.com/)

生成摘要时出错

---

## 41. Do transformers need three projections? Systematic study of QKV variants

**原文标题**: Do transformers need three projections? Systematic study of QKV variants

**原文链接**: [https://arxiv.org/abs/2606.04032](https://arxiv.org/abs/2606.04032)

生成摘要时出错

---

## 42. Neocities domain suspended by Namecheap for unrelated court case

**原文标题**: Neocities domain suspended by Namecheap for unrelated court case

**原文链接**: [https://bsky.app/profile/neocities.org/post/3mnkqgxostk2k](https://bsky.app/profile/neocities.org/post/3mnkqgxostk2k)

生成摘要时出错

---

## 43. The company I work for is losing all of its humanity, I don't know where to go

**原文标题**: The company I work for is losing all of its humanity, I don't know where to go

**原文链接**: [https://superlemon.bearblog.dev/the-company-i-work-for-is-losing-all-of-its-humanity-but-i-dont-know-where-else-to-go/](https://superlemon.bearblog.dev/the-company-i-work-for-is-losing-all-of-its-humanity-but-i-dont-know-where-else-to-go/)

生成摘要时出错

---

## 44. Meta's ships facial recognition on smart glasses

**原文标题**: Meta's ships facial recognition on smart glasses

**原文链接**: [https://www.buchodi.com/meta-glasses-facial-recognition/](https://www.buchodi.com/meta-glasses-facial-recognition/)

生成摘要时出错

---

## 45. Let's celebrate work that is 100% human-made

**原文标题**: Let's celebrate work that is 100% human-made

**原文链接**: [https://www.human-made.work/](https://www.human-made.work/)

生成摘要时出错

---

## 46. Programmers will document for Claude, but not for each other

**原文标题**: Programmers will document for Claude, but not for each other

**原文链接**: [https://blog.plover.com/2026/03/09/#documentation-wins-2](https://blog.plover.com/2026/03/09/#documentation-wins-2)

生成摘要时出错

---

## 47. Watching a Z80 from an RP2350

**原文标题**: Watching a Z80 from an RP2350

**原文链接**: [https://emalliab.wordpress.com/2026/05/26/watching-a-z80-from-an-rp2350/](https://emalliab.wordpress.com/2026/05/26/watching-a-z80-from-an-rp2350/)

生成摘要时出错

---

## 48. SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P

**原文标题**: SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation](https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation)

生成摘要时出错

---

## 49. Branchless Quicksort faster than std:sort and pdqsort with C and C++ API

**原文标题**: Branchless Quicksort faster than std:sort and pdqsort with C and C++ API

**原文链接**: [https://tiki.li/blog/blqsort](https://tiki.li/blog/blqsort)

生成摘要时出错

---

## 50. How much value is AI creating?

**原文标题**: How much value is AI creating?

**原文链接**: [https://www.ft.com/content/8e9ae7a4-7209-4e2c-aa36-f3af77d6ce1f](https://www.ft.com/content/8e9ae7a4-7209-4e2c-aa36-f3af77d6ce1f)

生成摘要时出错

---

## 51. Communication on European Tech Sovereignty, and an EU Open-Source Strategy

**原文标题**: Communication on European Tech Sovereignty, and an EU Open-Source Strategy

**原文链接**: [https://digital-strategy.ec.europa.eu/en/library/communication-european-tech-sovereignty-accompanied-eu-open-source-strategy](https://digital-strategy.ec.europa.eu/en/library/communication-european-tech-sovereignty-accompanied-eu-open-source-strategy)

生成摘要时出错

---

## 52. Valve says it's ready to launch the Steam Machine this summer

**原文标题**: Valve says it's ready to launch the Steam Machine this summer

**原文链接**: [https://www.theverge.com/games/943657/valve-steam-machine-frame-summer-launch-verified](https://www.theverge.com/games/943657/valve-steam-machine-frame-summer-launch-verified)

生成摘要时出错

---

## 53. Go Experiments Explained

**原文标题**: Go Experiments Explained

**原文链接**: [https://www.alexedwards.net/blog/go-experiments-explained](https://www.alexedwards.net/blog/go-experiments-explained)

生成摘要时出错

---

## 54. Delacroix's Entry of the Crusaders into Constantinople Restored

**原文标题**: Delacroix's Entry of the Crusaders into Constantinople Restored

**原文链接**: [https://www.louvre.fr/en/explore/life-at-the-museum/delacroix-s-entry-of-the-crusaders-into-constantinople-restored-to-its-original-glory](https://www.louvre.fr/en/explore/life-at-the-museum/delacroix-s-entry-of-the-crusaders-into-constantinople-restored-to-its-original-glory)

生成摘要时出错

---

## 55. Fake Money Built America

**原文标题**: Fake Money Built America

**原文链接**: [https://mail.blockworks.com/p/how-fake-money-built-america](https://mail.blockworks.com/p/how-fake-money-built-america)

生成摘要时出错

---

## 56. New IronWorm malware hits 36 packages in NPM supply-chain attack

**原文标题**: New IronWorm malware hits 36 packages in NPM supply-chain attack

**原文链接**: [https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/)

生成摘要时出错

---

## 57. Ohbin – uv wrapper for installing tools from GitHub

**原文标题**: Ohbin – uv wrapper for installing tools from GitHub

**原文链接**: [https://github.com/prostomarkeloff/ohbin](https://github.com/prostomarkeloff/ohbin)

生成摘要时出错

---

## 58. SVG of a Hamster Playing Table-Tennis

**原文标题**: SVG of a Hamster Playing Table-Tennis

**原文链接**: [https://aibenchy.com/ro/showcase/hamster-playing-table-tennis-svg/](https://aibenchy.com/ro/showcase/hamster-playing-table-tennis-svg/)

生成摘要时出错

---

## 59. Linear Cosine Palettes(2025)

**原文标题**: Linear Cosine Palettes(2025)

**原文链接**: [https://blog.djnavarro.net/posts/2025-09-14_cosine-palettes/](https://blog.djnavarro.net/posts/2025-09-14_cosine-palettes/)

生成摘要时出错

---

## 60. Buffy the Vampire Slayer, Ted Lasso, and Little Britain Actor Anthony Head Dies

**原文标题**: Buffy the Vampire Slayer, Ted Lasso, and Little Britain Actor Anthony Head Dies

**原文链接**: [https://news.sky.com/story/buffy-the-vampire-slayer-and-ted-lasso-actor-dies-13545934](https://news.sky.com/story/buffy-the-vampire-slayer-and-ted-lasso-actor-dies-13545934)

生成摘要时出错

---

## 61. The Causes of Long Covid

**原文标题**: The Causes of Long Covid

**原文链接**: [https://www.science.org/content/blog-post/causes-long-covid](https://www.science.org/content/blog-post/causes-long-covid)

生成摘要时出错

---

## 62. Agentic Search Models with OpenSearch and Elasticsearch

**原文标题**: Agentic Search Models with OpenSearch and Elasticsearch

**原文链接**: [https://bonsai.io/blog/agent-search-with-sid/](https://bonsai.io/blog/agent-search-with-sid/)

生成摘要时出错

---

## 63. IPv6 zones in URLs are a mistake

**原文标题**: IPv6 zones in URLs are a mistake

**原文链接**: [https://xeiaso.net/notes/2026/ipv6-zones-go-url/](https://xeiaso.net/notes/2026/ipv6-zones-go-url/)

生成摘要时出错

---

## 64. The Empty Field That Wasn't: GPS Broadcasts a Numbers Station

**原文标题**: The Empty Field That Wasn't: GPS Broadcasts a Numbers Station

**原文链接**: [https://lsc-pagepro.mydigitalpublication.com/publication/?i=865273&p=62&view=issueViewer](https://lsc-pagepro.mydigitalpublication.com/publication/?i=865273&p=62&view=issueViewer)

生成摘要时出错

---

## 65. Samurai City

**原文标题**: Samurai City

**原文链接**: [https://worksinprogress.co/issue/samurai-city/](https://worksinprogress.co/issue/samurai-city/)

生成摘要时出错

---

## 66. VoidZero Is Joining Cloudflare

**原文标题**: VoidZero Is Joining Cloudflare

**原文链接**: [https://blog.cloudflare.com/voidzero-joins-cloudflare/](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

生成摘要时出错

---

## 67. When AI Builds Itself: Our progress toward recursive self-improvement

**原文标题**: When AI Builds Itself: Our progress toward recursive self-improvement

**原文链接**: [https://www.anthropic.com/institute/recursive-self-improvement](https://www.anthropic.com/institute/recursive-self-improvement)

生成摘要时出错

---

## 68. WiFi Time

**原文标题**: WiFi Time

**原文链接**: [https://mitxela.com/projects/wifi_time](https://mitxela.com/projects/wifi_time)

生成摘要时出错

---

## 69. KVarN: Native vLLM backend for KV-cache quantization by Huawei

**原文标题**: KVarN: Native vLLM backend for KV-cache quantization by Huawei

**原文链接**: [https://github.com/huawei-csl/KVarN](https://github.com/huawei-csl/KVarN)

生成摘要时出错

---

## 70. Magenta RealTime 2: Open and Local Live Music Models

**原文标题**: Magenta RealTime 2: Open and Local Live Music Models

**原文链接**: [https://magenta.withgoogle.com/magenta-realtime-2](https://magenta.withgoogle.com/magenta-realtime-2)

生成摘要时出错

---

## 71. They’re made out of weights

**原文标题**: They’re made out of weights

**原文链接**: [https://maxleiter.com/blog/weights](https://maxleiter.com/blog/weights)

生成摘要时出错

---

## 72. Queen bees emerge from special wax chambers

**原文标题**: Queen bees emerge from special wax chambers

**原文链接**: [https://cen.acs.org/materials/biobased-materials/queen-bees-special-wax/104/web/2026/06](https://cen.acs.org/materials/biobased-materials/queen-bees-special-wax/104/web/2026/06)

生成摘要时出错

---

## 73. The destruction of 3D printing: Bloomberg is behind it [video]

**原文标题**: The destruction of 3D printing: Bloomberg is behind it [video]

**原文链接**: [https://www.youtube.com/watch?v=E1B2cWEaWDw](https://www.youtube.com/watch?v=E1B2cWEaWDw)

生成摘要时出错

---

## 74. Advanced micro reactor achieves criticality in only two years

**原文标题**: Advanced micro reactor achieves criticality in only two years

**原文链接**: [https://www.powermag.com/antares-mark-0-becomes-first-advanced-nuclear-reactor-to-achieve-criticality-under-doe-pilot-program/](https://www.powermag.com/antares-mark-0-becomes-first-advanced-nuclear-reactor-to-achieve-criticality-under-doe-pilot-program/)

生成摘要时出错

---

## 75. Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes

**原文标题**: Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes

**原文链接**: [https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

生成摘要时出错

---

## 76. The British university is dying, and it seems that almost nobody cares

**原文标题**: The British university is dying, and it seems that almost nobody cares

**原文链接**: [https://newleftreview.org/sidecar/posts/irreversible](https://newleftreview.org/sidecar/posts/irreversible)

生成摘要时出错

---

## 77. Ian's Secure Shoelace Knot

**原文标题**: Ian's Secure Shoelace Knot

**原文链接**: [https://www.fieggen.com/shoelace/secureknot.htm](https://www.fieggen.com/shoelace/secureknot.htm)

生成摘要时出错

---

## 78. Learn SQL Once, Use It for 30 Years

**原文标题**: Learn SQL Once, Use It for 30 Years

**原文链接**: [https://fagnerbrack.com/learn-sql-once-use-it-for-30-years-9aceb0bdee03](https://fagnerbrack.com/learn-sql-once-use-it-for-30-years-9aceb0bdee03)

生成摘要时出错

---

## 79. Retro-Tech Parenting

**原文标题**: Retro-Tech Parenting

**原文链接**: [https://havenweb.org/2026/05/28/retro-tech.html](https://havenweb.org/2026/05/28/retro-tech.html)

生成摘要时出错

---

## 80. Something is jamming GPS over Europe

**原文标题**: Something is jamming GPS over Europe

**原文链接**: [https://www.youtube.com/watch?v=tz23G_UXCGA](https://www.youtube.com/watch?v=tz23G_UXCGA)

生成摘要时出错

---

## 81. JLink JTAG Access on the Pinecil

**原文标题**: JLink JTAG Access on the Pinecil

**原文链接**: [https://danielmangum.com/posts/jlink-jtag-pinecil/](https://danielmangum.com/posts/jlink-jtag-pinecil/)

生成摘要时出错

---

## 82. Making Debian or Fedora persistent live images

**原文标题**: Making Debian or Fedora persistent live images

**原文链接**: [https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html](https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html)

生成摘要时出错

---

## 83. Under Notre Dame, a 'dig of the century' unearths 1,700 years of history

**原文标题**: Under Notre Dame, a 'dig of the century' unearths 1,700 years of history

**原文链接**: [https://apnews.com/article/notre-dame-dig-treasures-paris-archaeology-roman-dae41f792c1402faf32a87c154cc9a77](https://apnews.com/article/notre-dame-dig-treasures-paris-archaeology-roman-dae41f792c1402faf32a87c154cc9a77)

生成摘要时出错

---

## 84. Show HN: Local-first fast CPU image to text for screenshots, PDFs, webpages

**原文标题**: Show HN: Local-first fast CPU image to text for screenshots, PDFs, webpages

**原文链接**: [https://github.com/kouhxp/textsnap](https://github.com/kouhxp/textsnap)

生成摘要时出错

---

## 85. Republicans Claim Anti-Data Center Movement Is a Chinese Psy-Op

**原文标题**: Republicans Claim Anti-Data Center Movement Is a Chinese Psy-Op

**原文链接**: [https://gizmodo.com/republicans-claim-anti-data-center-movement-is-a-chinese-psy-op-2000767611](https://gizmodo.com/republicans-claim-anti-data-center-movement-is-a-chinese-psy-op-2000767611)

生成摘要时出错

---

## 86. Gemma 4 12B: A unified, encoder-free multimodal model

**原文标题**: Gemma 4 12B: A unified, encoder-free multimodal model

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

生成摘要时出错

---

## 87. 3D-printed book turns its own G-code into raised lettering

**原文标题**: 3D-printed book turns its own G-code into raised lettering

**原文链接**: [https://www.designboom.com/design/3d-printed-book-manual-darius-ou-benson-chong/](https://www.designboom.com/design/3d-printed-book-manual-darius-ou-benson-chong/)

生成摘要时出错

---

## 88. Elixir v1.20: Now a gradually typed language

**原文标题**: Elixir v1.20: Now a gradually typed language

**原文链接**: [https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/)

生成摘要时出错

---

## 89. Show HN: Mercek – A Desktop IDE for AWS ECS

**原文标题**: Show HN: Mercek – A Desktop IDE for AWS ECS

**原文链接**: [https://www.mercek.dev/](https://www.mercek.dev/)

生成摘要时出错

---

## 90. Castor: CERN Advanced STORage Manager

**原文标题**: Castor: CERN Advanced STORage Manager

**原文链接**: [https://castor.web.cern.ch/content/home.html](https://castor.web.cern.ch/content/home.html)

生成摘要时出错

---

## 91. Kiki – a tiny homepage construction kit with a small footprint

**原文标题**: Kiki – a tiny homepage construction kit with a small footprint

**原文链接**: [https://tomotama.com/kiki](https://tomotama.com/kiki)

生成摘要时出错

---

## 92. Sum-product, unit distances, and number fields

**原文标题**: Sum-product, unit distances, and number fields

**原文链接**: [https://www.erdosproblems.com/forum/thread/blog:6](https://www.erdosproblems.com/forum/thread/blog:6)

生成摘要时出错

---

## 93. The Pentagon is running an AI propaganda mill targeting Latin America

**原文标题**: The Pentagon is running an AI propaganda mill targeting Latin America

**原文链接**: [https://theintercept.com/2026/06/02/la-tilde-propaganda-latin-america-pentagon/](https://theintercept.com/2026/06/02/la-tilde-propaganda-latin-america-pentagon/)

生成摘要时出错

---

## 94. WSL 2 is getting faster Windows file system access

**原文标题**: WSL 2 is getting faster Windows file system access

**原文链接**: [https://www.boxofcables.dev/wsl2-per-device-swiotlb-pools-for-virtiofs-and-virtioproxy/](https://www.boxofcables.dev/wsl2-per-device-swiotlb-pools-for-virtiofs-and-virtioproxy/)

生成摘要时出错

---

## 95. Artificial intelligence is not conscious – Ted Chiang

**原文标题**: Artificial intelligence is not conscious – Ted Chiang

**原文链接**: [https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/)

生成摘要时出错

---

## 96. DNS is for people, not for IT infrastructure

**原文标题**: DNS is for people, not for IT infrastructure

**原文链接**: [https://louwrentius.com/dns-is-for-people-not-for-it-infrastructure.html](https://louwrentius.com/dns-is-for-people-not-for-it-infrastructure.html)

生成摘要时出错

---

## 97. Understanding why autism symptoms sometimes improve amid fever

**原文标题**: Understanding why autism symptoms sometimes improve amid fever

**原文链接**: [https://news.mit.edu/2024/understanding-why-autism-symptoms-sometimes-improve-amid-fever-0523](https://news.mit.edu/2024/understanding-why-autism-symptoms-sometimes-improve-amid-fever-0523)

生成摘要时出错

---

## 98. French-Iranian author Marjane Satrapi, author of 'Persepolis', dies at 56

**原文标题**: French-Iranian author Marjane Satrapi, author of 'Persepolis', dies at 56

**原文链接**: [https://www.france24.com/en/culture/20260604-french-iranian-author-marjane-satrapi-author-of-persepolis-dies-at-56](https://www.france24.com/en/culture/20260604-french-iranian-author-marjane-satrapi-author-of-persepolis-dies-at-56)

生成摘要时出错

---

## 99. Reverse-Engineered Userspace Driver for Asus ZenVision Lid OLED on Linux"

**原文标题**: Reverse-Engineered Userspace Driver for Asus ZenVision Lid OLED on Linux"

**原文链接**: [https://github.com/tarpediem/zenvision-linux](https://github.com/tarpediem/zenvision-linux)

生成摘要时出错

---

## 100. PlayStation Architecture

**原文标题**: PlayStation Architecture

**原文链接**: [https://www.copetti.org/writings/consoles/playstation/](https://www.copetti.org/writings/consoles/playstation/)

生成摘要时出错

---

