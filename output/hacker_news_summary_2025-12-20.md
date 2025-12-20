# Hacker News 热门文章摘要 (2025-12-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 尽管自托管 Postgres

**原文标题**: Go ahead, self-host Postgres

**原文链接**: [https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1](https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1)

文章《尽管去自托管 Postgres 吧》(Go ahead, self-host Postgres) 挑战了现代行业的教条，即托管数据库服务（如 AWS RDS）是必不可少的。作者认为，对自托管的恐惧是云服务商推行的一种叙事，目的是为其对本质上是开源软件的产品收取的巨额溢价提供正当理由。

**自托管的理由：**
*   **成本效益：** 云服务的定价已变得极具侵略性。以中端 RDS 实例的价格，用户可以租用一台 CPU 和内存配置显著更高的专用服务器。
*   **性能：** 自托管允许对托管服务通常锁定的参数（如内存界限和 NVMe 存储优化）进行细粒度调优。作者指出，在迁移到专用服务器后，查询延迟降低了 20%。
*   **运维简单：** 作者声称，包括备份、安全更新和监控在内的维护工作每月仅需 30 到 60 分钟。虽然自托管将事故响应的责任转移给了用户，但作者指出，托管服务也会发生故障，且往往让用户缺乏解决问题的工具。

**成功的技术关键：**
作者为那些准备切换的用户强调了几个关键的配置领域：
*   **内存：** 手动调优 `shared_buffers` 和 `effective_cache_size`，而不是依赖默认的 Docker 设置。
*   **连接：** 使用 PgBouncer 等连接池工具来管理开销。
*   **存储：** 调整 `random_page_cost` 以反映现代 NVMe SSD 的速度。

**结论：**
虽然托管服务仍推荐给完全的初学者、具有特殊规模的大型企业或受严格监管的行业（如 PCI/HIPAA），但作者认为，大多数团队都处于一个“甜蜜点”，即自托管既快速、稳定，又便宜得多。他鼓励任何每月为 RDS 支付超过 200 美元的人尝试进行自托管迁移。

---

## 2. 日志级别 ‘error’ 应当意味着有某些问题需要修复。

**原文标题**: Log level 'error' should mean that something needs to be fixed

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing](https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing)

这篇文章由 Chris Siebenmann 撰写于 2025 年 2 月 17 日，解释了其博客 *Wandering Thoughts* 的部分访问者被阻止访问的原因。

主要核心观点包括：

*   **反爬虫措施：** 由于旨在抓取大语言模型（LLM）训练数据的高流量爬虫大幅增加，作者实施了严格的屏蔽措施。
*   **针对旧版浏览器：** 系统专门屏蔽了“版本过旧且可疑”的浏览器，特别是自动化爬虫经常使用的旧版 Chrome 浏览器。
*   **存档服务的问题：** `archive.today` 及其变体（如 `.is`、`.ph` 等）目前已被屏蔽。作者指出，这些服务使用旧版 Chrome 的 User-Agent 字符串，并伪造反向 DNS 记录以冒充 Googlebot，导致系统无法将其与恶意攻击者区分开来。
*   **推荐替代方案：** 建议用户改用 `archive.org` (Internet Archive)，因为它是一个行为规范、能正确识别自身身份的爬虫。
*   **解决误报：** 若合法用户被误屏蔽，可联系作者的大学邮箱并提供具体的 User-Agent 字符串，以协助优化屏蔽标准。

*（注：虽然提示中的标题提到了日志级别，但提供的内容完全侧重于浏览器屏蔽和反爬虫措施。）*

---

## 3. Gemini 3 Pro 对决 2.5 Pro：宝可梦 水晶版

**原文标题**: Gemini 3 Pro vs. 2.5 Pro in Pokemon Crystal

**原文链接**: [https://blog.jcz.dev/gemini-3-pro-vs-25-pro-in-pokemon-crystal](https://blog.jcz.dev/gemini-3-pro-vs-25-pro-in-pokemon-crystal)

无法访问文章链接。

---

## 4. Immersa：基于 Web 的开源 3D 演示工具

**原文标题**: Immersa: Open-source Web-based 3D Presentation Tool

**原文链接**: [https://github.com/ertugrulcetin/immersa](https://github.com/ertugrulcetin/immersa)

**Immersa** 是一款开源的网页版演示工具，旨在创建沉浸式的 3D 演示文稿。与传统的 2D 幻灯片软件不同，Immersa 允许用户在三维空间中排列 3D 模型 (.glb)、图像和 3D 文本。

该工具的核心亮点是其**基于插值的动画系统**。当用户复制幻灯片并修改物体的坐标、旋转或缩放时，Immersa 会在演示过程中自动生成这些状态之间的平滑过渡动画。

**核心特性：**
*   **3D 场景编辑器：** 包含一个带有相机控制和物体操作手柄（gizmos）的完整视口。
*   **内容支持：** 无缝导入 .glb 模型、标准图像格式（JPG/PNG）以及可定制的 3D 文本。
*   **本地存储：** 所有数据通过 IndexedDB 存储在浏览器本地，确保了隐私和持久性，且无需强制注册云端账户。
*   **工作流工具：** 功能包括撤销/重做、键盘快捷键（例如“D”用于复制，“T”用于文本），以及将演示文稿导出为 .edn 文件的能力。

**技术栈：**
该项目由 Ertuğrul Çetin 开发，使用 **ClojureScript**、**Re-frame** 以及用于 3D 渲染的 **Babylon.js** 构建。本地编译需要 Node.js 和 Java (JDK 11+)，并采用 MIT 许可证开源。

Immersa 提供了现代化的深色主题界面，非常适合希望超越静态幻灯片、追求动态空间叙事的创作者。

---

## 5. 纯硅 Demo 编程：无 CPU，无内存，仅 4k 逻辑门

**原文标题**: Pure Silicon Demo Coding: No CPU, No Memory, Just 4k Gates

**原文链接**: [https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html](https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html)

本文详细介绍了为 Tiny Tapeout 8 竞赛开发定制 ASIC Demo 的过程。该设计受限于约 4,000 个逻辑门，且**不包含 CPU、RAM 或 ROM**。设计输出为 2 位 RGB VGA 视频和 1 位音频，所有状态均存储在耗电的触发器中。

由于在没有内存的情况下无法使用数据压缩等传统“尺寸编码”（sizecoding）技巧，作者通过降低**算法复杂度**来优化设计。关键技术实现包括：

*   **正弦滚动条：** 为避免占用大量内存的查找表，设计采用“辛积分器”（向量旋转），通过简单的移位和加法计算每像素和每帧的数值，从而生成正弦波。
*   **3D 棋盘格：** 作者实现了不恢复余数除法算法来进行实时透视变换，将屏幕坐标投影到 3D 平面上。
*   **基于逻辑的数据：** 文本和音乐被直接编码到逻辑门阵列中。由于综合工具会将真值表转换为逻辑门，设计采用了重复的“ABAC”音乐模式和 2 的幂次方字符间距，以便编译器简化硬件需求。
*   **视觉与音频：** Demo 中的星空由线性反馈移位寄存器（LFSR）驱动，1 位音频通过 Σ-Δ 转换生成，作者发现这比 PWM 更易于实现。

该项目在固化至 Skywater 130nm 工艺之前，使用 Verilator 仿真和 OrangeCrab FPGA 进行了原型设计。最终设计使用了 3,374 个单元和 293 个触发器，几乎填满了芯片区域的每一平方纳米。这一成果凸显了 ASIC 设计的独特约束：虽然状态和变化非常“昂贵”，但重复模式和数学捷径基本上是“免费”的。

---

## 6. NIST 博尔德分部的 NTP 服务已断电

**原文标题**: NTP at NIST Boulder Has Lost Power

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/)

由于极端强风以及为预防山火而采取的预防性停电，美国国家标准与技术研究院（NIST）博尔德分部的原子系综时间尺度在经历长时间电力中断后已宣告失效。此次停电始于2025年12月17日，导致位于博尔德的互联网时间服务（NTP）数据变得不准确。

NIST的杰夫·谢尔曼（Jeff Sherman）报告称，虽然部分服务器在备用电源支持下仍可访问，但他正努力将其禁用，以防止错误的时间数据外泄。受影响的服务器包括 time-a-b.nist.gov 至 time-e-b.nist.gov 以及经过身份验证的 ntp-b.nist.gov。

在关键备用发电机发生故障并影响了主信号分配链后，事态进一步恶化。目前的紧急救援重点是在电池备用电源耗尽之前，为氢原子钟确保替代电源。

由于场地关闭和员工进入受限，目前尚无法评估维修完成的具体时间。不过，位于另一栋校区建筑内并由不同发电机支持的其他时钟可能幸存，这将使 NIST 在电力恢复后无需依赖外部参考信号，即可重新校准主时间尺度。

---

## 7. Skills 正式登陆 Codex

**原文标题**: Skills Officially Comes to Codex

**原文链接**: [https://developers.openai.com/codex/skills/](https://developers.openai.com/codex/skills/)

Codex 官方推出了 **Agent Skills**（智能体技能），该功能允许用户通过特定任务的工作流来扩展 AI 的能力。一项“技能”是一个包含 `SKILL.md` 文件（提供指令和元数据）以及可选脚本、文档和资产的软件包。

**功能与调用**
技能利用“渐进式披露”来高效管理上下文；Codex 最初仅加载可用技能的名称和描述。可以通过两种方式激活技能：
*   **显式调用：** 通过使用 `/skills` 斜杠命令，或在 CLI、IDE 中输入 `$` 来引用技能。
*   **隐式调用：** 当 Codex 自动检测到用户的任务与某项技能的描述匹配时。

**存储与范围**
技能存储在不同的位置，Codex 遵循特定的优先级层次结构。如果两个技能同名，优先级较高位置的版本将覆盖其他版本。优先级（从高到低）如下：
1.  **REPO（仓库）：** 本地文件夹、父目录或 git 仓库根目录。
2.  **USER（用户）：** 用户的个人主目录。
3.  **ADMIN（管理员）：** 用于共享自动化的全系统位置。
4.  **SYSTEM（系统）：** 直接随 Codex 捆绑的默认技能。

**创建与安装**
用户可以通过整理文件夹手动创建技能，也可以使用内置的 `$skill-creator` 技能自动创建。为了扩展技能库，用户可以使用 `$skill-installer` 从 GitHub 下载精选技能，例如 Linear 或 Notion 的集成。Codex 还附带了如 `$plan` 等内部技能，用于协助研究和构建复杂的开发任务。

---

## 8. Privacy doesn't mean anything anymore, anonymity does

**原文标题**: Privacy doesn't mean anything anymore, anonymity does

**原文链接**: [https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/](https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/)

生成摘要时出错

---

## 9. CSS Grid Lanes

**原文标题**: CSS Grid Lanes

**原文链接**: [https://webkit.org/blog/17660/introducing-css-grid-lanes/](https://webkit.org/blog/17660/introducing-css-grid-lanes/)

生成摘要时出错

---

## 10. Reflections on AI at the End of 2025

**原文标题**: Reflections on AI at the End of 2025

**原文链接**: [https://antirez.com/news/157](https://antirez.com/news/157)

生成摘要时出错

---

## 11. Mistral OCR 3

**原文标题**: Mistral OCR 3

**原文链接**: [https://mistral.ai/news/mistral-ocr-3](https://mistral.ai/news/mistral-ocr-3)

生成摘要时出错

---

## 12. Arduino UNO Q bridges high-performance computing with real-time control

**原文标题**: Arduino UNO Q bridges high-performance computing with real-time control

**原文链接**: [https://www.arduino.cc/product-uno-q/](https://www.arduino.cc/product-uno-q/)

生成摘要时出错

---

## 13. Charles Proxy

**原文标题**: Charles Proxy

**原文链接**: [https://www.charlesproxy.com/](https://www.charlesproxy.com/)

生成摘要时出错

---

## 14. What Does a Database for SSDs Look Like?

**原文标题**: What Does a Database for SSDs Look Like?

**原文链接**: [https://brooker.co.za/blog/2025/12/15/database-for-ssd.html](https://brooker.co.za/blog/2025/12/15/database-for-ssd.html)

生成摘要时出错

---

## 15. A train-sized tunnel is now carrying electricity under South London

**原文标题**: A train-sized tunnel is now carrying electricity under South London

**原文链接**: [https://www.ianvisits.co.uk/articles/a-train-sized-tunnel-is-now-carrying-electricity-under-south-london-86221/](https://www.ianvisits.co.uk/articles/a-train-sized-tunnel-is-now-carrying-electricity-under-south-london-86221/)

生成摘要时出错

---

## 16. Garage – An S3 object store so reliable you can run it outside datacenters

**原文标题**: Garage – An S3 object store so reliable you can run it outside datacenters

**原文链接**: [https://garagehq.deuxfleurs.fr/](https://garagehq.deuxfleurs.fr/)

生成摘要时出错

---

## 17. Over 40% of Deceased Drivers in Vehicle Crashes Test Positive for THC: Study

**原文标题**: Over 40% of Deceased Drivers in Vehicle Crashes Test Positive for THC: Study

**原文链接**: [https://www.facs.org/media-center/press-releases/2025/over-40-of-deceased-drivers-in-motor-vehicle-crashes-test-positive-for-thc-study-shows/](https://www.facs.org/media-center/press-releases/2025/over-40-of-deceased-drivers-in-motor-vehicle-crashes-test-positive-for-thc-study-shows/)

生成摘要时出错

---

## 18. New Quantum Antenna Reveals a Hidden Terahertz World

**原文标题**: New Quantum Antenna Reveals a Hidden Terahertz World

**原文链接**: [https://www.sciencedaily.com/releases/2025/12/251213032617.htm](https://www.sciencedaily.com/releases/2025/12/251213032617.htm)

生成摘要时出错

---

## 19. Maximizing Compression of Apple II Hi-Res Images

**原文标题**: Maximizing Compression of Apple II Hi-Res Images

**原文链接**: [http://deater.net/weave/vmwprod/hgr_compress/](http://deater.net/weave/vmwprod/hgr_compress/)

生成摘要时出错

---

## 20. Airbus to migrate critical apps to a sovereign Euro cloud

**原文标题**: Airbus to migrate critical apps to a sovereign Euro cloud

**原文链接**: [https://www.theregister.com/2025/12/19/airbus_sovereign_cloud/](https://www.theregister.com/2025/12/19/airbus_sovereign_cloud/)

生成摘要时出错

---

## 21. A terminal emulator that runs in your terminal. Powered by Turbo Vision

**原文标题**: A terminal emulator that runs in your terminal. Powered by Turbo Vision

**原文链接**: [https://github.com/magiblot/tvterm](https://github.com/magiblot/tvterm)

生成摘要时出错

---

## 22. Hash tables in Go and advantage of self-hosted compilers

**原文标题**: Hash tables in Go and advantage of self-hosted compilers

**原文链接**: [https://rushter.com/blog/go-and-hashmaps/](https://rushter.com/blog/go-and-hashmaps/)

生成摘要时出错

---

## 23. Contrails Map

**原文标题**: Contrails Map

**原文链接**: [https://map.contrails.org/](https://map.contrails.org/)

生成摘要时出错

---

## 24. A proof of concept of a semistable C++ vector container

**原文标题**: A proof of concept of a semistable C++ vector container

**原文链接**: [https://github.com/joaquintides/semistable_vector](https://github.com/joaquintides/semistable_vector)

生成摘要时出错

---

## 25. NOAA deploys new generation of AI-driven global weather models

**原文标题**: NOAA deploys new generation of AI-driven global weather models

**原文链接**: [https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models)

生成摘要时出错

---

## 26. Fuzix on a Raspberry Pi Pico

**原文标题**: Fuzix on a Raspberry Pi Pico

**原文链接**: [https://ewpratten.com/blog/fuzix-pi-pico](https://ewpratten.com/blog/fuzix-pi-pico)

生成摘要时出错

---

## 27. TP-Link Tapo C200: Hardcoded Keys, Buffer Overflows and Privacy

**原文标题**: TP-Link Tapo C200: Hardcoded Keys, Buffer Overflows and Privacy

**原文链接**: [https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/](https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/)

生成摘要时出错

---

## 28. LLM Year in Review

**原文标题**: LLM Year in Review

**原文链接**: [https://karpathy.bearblog.dev/year-in-review-2025/](https://karpathy.bearblog.dev/year-in-review-2025/)

生成摘要时出错

---

## 29. 8-bit Boléro

**原文标题**: 8-bit Boléro

**原文链接**: [https://linusakesson.net/music/bolero/index.php](https://linusakesson.net/music/bolero/index.php)

生成摘要时出错

---

## 30. Graphite is joining Cursor

**原文标题**: Graphite is joining Cursor

**原文链接**: [https://cursor.com/blog/graphite](https://cursor.com/blog/graphite)

生成摘要时出错

---

## 31. Sharp: High performance Node.js image processing/optimization

**原文标题**: Sharp: High performance Node.js image processing/optimization

**原文链接**: [https://github.com/lovell/sharp](https://github.com/lovell/sharp)

生成摘要时出错

---

## 32. A better zip bomb (2019)

**原文标题**: A better zip bomb (2019)

**原文链接**: [https://www.bamsoftware.com/hacks/zipbomb/](https://www.bamsoftware.com/hacks/zipbomb/)

生成摘要时出错

---

## 33. Brown/MIT shooting suspect found dead, officials say

**原文标题**: Brown/MIT shooting suspect found dead, officials say

**原文链接**: [https://www.washingtonpost.com/nation/2025/12/18/brown-university-shooting-person-of-interest/](https://www.washingtonpost.com/nation/2025/12/18/brown-university-shooting-person-of-interest/)

生成摘要时出错

---

## 34. The Deviancy Signal: Having "Nothing to Hide" Is a Threat to Us All

**原文标题**: The Deviancy Signal: Having "Nothing to Hide" Is a Threat to Us All

**原文链接**: [https://thompson2026.com/blog/deviancy-signal/](https://thompson2026.com/blog/deviancy-signal/)

生成摘要时出错

---

## 35. Show HN: TinyPDF – 3kb pdf library (70x smaller than jsPDF)

**原文标题**: Show HN: TinyPDF – 3kb pdf library (70x smaller than jsPDF)

**原文链接**: [https://github.com/Lulzx/tinypdf](https://github.com/Lulzx/tinypdf)

生成摘要时出错

---

## 36. History LLMs: Models trained exclusively on pre-1913 texts

**原文标题**: History LLMs: Models trained exclusively on pre-1913 texts

**原文链接**: [https://github.com/DGoettlich/history-llms](https://github.com/DGoettlich/history-llms)

生成摘要时出错

---

## 37. Rust's Block Pattern

**原文标题**: Rust's Block Pattern

**原文链接**: [https://notgull.net/block-pattern/](https://notgull.net/block-pattern/)

生成摘要时出错

---

## 38. Build Your Own React

**原文标题**: Build Your Own React

**原文链接**: [https://pomb.us/build-your-own-react/](https://pomb.us/build-your-own-react/)

生成摘要时出错

---

## 39. Carolina Cloud – One third the cost of AWS for data science workloads

**原文标题**: Carolina Cloud – One third the cost of AWS for data science workloads

**原文链接**: [https://carolinacloud.io/](https://carolinacloud.io/)

生成摘要时出错

---

## 40. Qwen-Image-Layered: transparency and layer aware open diffusion model

**原文标题**: Qwen-Image-Layered: transparency and layer aware open diffusion model

**原文链接**: [https://huggingface.co/papers/2512.15603](https://huggingface.co/papers/2512.15603)

生成摘要时出错

---

## 41. The FreeBSD Foundation's Laptop Support and Usability Project

**原文标题**: The FreeBSD Foundation's Laptop Support and Usability Project

**原文链接**: [https://github.com/FreeBSDFoundation/proj-laptop](https://github.com/FreeBSDFoundation/proj-laptop)

生成摘要时出错

---

## 42. Believe the Checkbook

**原文标题**: Believe the Checkbook

**原文链接**: [https://robertgreiner.com/believe-the-checkbook/](https://robertgreiner.com/believe-the-checkbook/)

生成摘要时出错

---

## 43. Performance Hints (2023)

**原文标题**: Performance Hints (2023)

**原文链接**: [https://abseil.io/fast/hints.html](https://abseil.io/fast/hints.html)

生成摘要时出错

---

## 44. Beginning January 2026, all ACM publications will be made open access

**原文标题**: Beginning January 2026, all ACM publications will be made open access

**原文链接**: [https://dl.acm.org/openaccess](https://dl.acm.org/openaccess)

生成摘要时出错

---

## 45. Airbus moving critical systems away from AWS, Google, and MS

**原文标题**: Airbus moving critical systems away from AWS, Google, and MS

**原文链接**: [https://old.reddit.com/r/europe/comments/1pqucbz/airbus_moving_critical_systems_away_from_aws/](https://old.reddit.com/r/europe/comments/1pqucbz/airbus_moving_critical_systems_away_from_aws/)

生成摘要时出错

---

## 46. Amazon will allow ePub and PDF downloads for DRM-free eBooks

**原文标题**: Amazon will allow ePub and PDF downloads for DRM-free eBooks

**原文链接**: [https://www.kdpcommunity.com/s/article/New-eBook-Download-Options-for-Readers-Coming-in-2026?language=en_US](https://www.kdpcommunity.com/s/article/New-eBook-Download-Options-for-Readers-Coming-in-2026?language=en_US)

生成摘要时出错

---

## 47. GotaTun – Mullvad's WireGuard Implementation in Rust

**原文标题**: GotaTun – Mullvad's WireGuard Implementation in Rust

**原文链接**: [https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn](https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn)

生成摘要时出错

---

## 48. Gh-actions-lockfile: generate and verify lockfiles for GitHub Actions

**原文标题**: Gh-actions-lockfile: generate and verify lockfiles for GitHub Actions

**原文链接**: [https://gh-actions-lockfile.net](https://gh-actions-lockfile.net)

生成摘要时出错

---

## 49. White House website mysteriously streams personal finance YouTube creator

**原文标题**: White House website mysteriously streams personal finance YouTube creator

**原文链接**: [https://www.pbs.org/newshour/politics/white-house-website-mysteriously-streams-personal-finance-youtube-creator](https://www.pbs.org/newshour/politics/white-house-website-mysteriously-streams-personal-finance-youtube-creator)

生成摘要时出错

---

## 50. Texas is suing all of the big TV makers for spying on what you watch

**原文标题**: Texas is suing all of the big TV makers for spying on what you watch

**原文链接**: [https://www.theverge.com/news/845400/texas-tv-makers-lawsuit-samsung-sony-lg-hisense-tcl-spying](https://www.theverge.com/news/845400/texas-tv-makers-lawsuit-samsung-sony-lg-hisense-tcl-spying)

生成摘要时出错

---

## 51. Reverse Engineering US Airline's PNR System and Accessing All Reservations

**原文标题**: Reverse Engineering US Airline's PNR System and Accessing All Reservations

**原文链接**: [https://alexschapiro.com/security/vulnerability/2025/11/20/avelo-airline-reservation-api-vulnerability](https://alexschapiro.com/security/vulnerability/2025/11/20/avelo-airline-reservation-api-vulnerability)

生成摘要时出错

---

## 52. The pitfalls of partitioning Postgres yourself

**原文标题**: The pitfalls of partitioning Postgres yourself

**原文链接**: [https://hatchet.run/blog/postgres-partitioning](https://hatchet.run/blog/postgres-partitioning)

生成摘要时出错

---

## 53. Vm.overcommit_memory=2 is the right setting for servers

**原文标题**: Vm.overcommit_memory=2 is the right setting for servers

**原文链接**: [https://ariadne.space/2025/12/16/vmovercommitmemory-is-always-the-right.html](https://ariadne.space/2025/12/16/vmovercommitmemory-is-always-the-right.html)

生成摘要时出错

---

## 54. Data Bank – Nuforc – Latest UFO Sightings

**原文标题**: Data Bank – Nuforc – Latest UFO Sightings

**原文链接**: [https://nuforc.org/databank/](https://nuforc.org/databank/)

生成摘要时出错

---

## 55. School security AI flagged clarinet as a gun. Exec says it wasn't an error

**原文标题**: School security AI flagged clarinet as a gun. Exec says it wasn't an error

**原文链接**: [https://arstechnica.com/tech-policy/2025/12/florida-schools-plan-to-vastly-expand-use-of-ai-that-mistook-clarinet-for-gun/](https://arstechnica.com/tech-policy/2025/12/florida-schools-plan-to-vastly-expand-use-of-ai-that-mistook-clarinet-for-gun/)

生成摘要时出错

---

## 56. The scariest boot loader code

**原文标题**: The scariest boot loader code

**原文链接**: [http://miod.online.fr/software/openbsd/stories/boot_hppa.html](http://miod.online.fr/software/openbsd/stories/boot_hppa.html)

生成摘要时出错

---

## 57. Feast Your Eyes on Japan's Fake Food

**原文标题**: Feast Your Eyes on Japan's Fake Food

**原文链接**: [https://www.newyorker.com/culture/annals-of-gastronomy/feast-your-eyes-on-japans-fake-food](https://www.newyorker.com/culture/annals-of-gastronomy/feast-your-eyes-on-japans-fake-food)

生成摘要时出错

---

## 58. We pwned X, Vercel, Cursor, and Discord through a supply-chain attack

**原文标题**: We pwned X, Vercel, Cursor, and Discord through a supply-chain attack

**原文链接**: [https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28](https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28)

生成摘要时出错

---

## 59. 1.5 TB of VRAM on Mac Studio – RDMA over Thunderbolt 5

**原文标题**: 1.5 TB of VRAM on Mac Studio – RDMA over Thunderbolt 5

**原文链接**: [https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5](https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5)

生成摘要时出错

---

## 60. Reconstructed Commander Keen 1-3 Source Code

**原文标题**: Reconstructed Commander Keen 1-3 Source Code

**原文链接**: [https://pckf.com/viewtopic.php?t=18248](https://pckf.com/viewtopic.php?t=18248)

生成摘要时出错

---

## 61. What Makes You Senior

**原文标题**: What Makes You Senior

**原文链接**: [https://terriblesoftware.org/2025/11/25/what-actually-makes-you-senior/](https://terriblesoftware.org/2025/11/25/what-actually-makes-you-senior/)

生成摘要时出错

---

## 62. Great ideas in theoretical computer science

**原文标题**: Great ideas in theoretical computer science

**原文链接**: [https://www.cs251.com/](https://www.cs251.com/)

生成摘要时出错

---

## 63. Response Healing: Reduce JSON defects by 80%+

**原文标题**: Response Healing: Reduce JSON defects by 80%+

**原文链接**: [https://openrouter.ai/announcements/response-healing-reduce-json-defects-by-80percent](https://openrouter.ai/announcements/response-healing-reduce-json-defects-by-80percent)

生成摘要时出错

---

## 64. Firefox will have an option to disable all AI features

**原文标题**: Firefox will have an option to disable all AI features

**原文链接**: [https://mastodon.social/@firefoxwebdevs/115740500373677782](https://mastodon.social/@firefoxwebdevs/115740500373677782)

生成摘要时出错

---

## 65. Show HN: Stickerbox, a kid-safe, AI-powered voice to sticker printer

**原文标题**: Show HN: Stickerbox, a kid-safe, AI-powered voice to sticker printer

**原文链接**: [https://stickerbox.com/](https://stickerbox.com/)

生成摘要时出错

---

## 66. A tagging system for documentation review comments

**原文标题**: A tagging system for documentation review comments

**原文链接**: [https://blog.techdocs.studio/p/a-tagging-system-for-documentation-review-comments](https://blog.techdocs.studio/p/a-tagging-system-for-documentation-review-comments)

生成摘要时出错

---

## 67. Prompt caching for cheaper LLM tokens

**原文标题**: Prompt caching for cheaper LLM tokens

**原文链接**: [https://ngrok.com/blog/prompt-caching/](https://ngrok.com/blog/prompt-caching/)

生成摘要时出错

---

## 68. Using TypeScript to obtain one of the rarest license plates

**原文标题**: Using TypeScript to obtain one of the rarest license plates

**原文链接**: [https://www.jack.bio/blog/licenseplate](https://www.jack.bio/blog/licenseplate)

生成摘要时出错

---

## 69. Why U.S. sports tickets have gotten so expensive

**原文标题**: Why U.S. sports tickets have gotten so expensive

**原文链接**: [https://www.nytimes.com/athletic/6901912/2025/12/19/usa-ticket-prices-sporting-events-world-cup-2026/](https://www.nytimes.com/athletic/6901912/2025/12/19/usa-ticket-prices-sporting-events-world-cup-2026/)

生成摘要时出错

---

## 70. Penny Farthing Race at 1928 Olympics

**原文标题**: Penny Farthing Race at 1928 Olympics

**原文链接**: [https://twitter.com/JamesMelville/status/2002324487576977716](https://twitter.com/JamesMelville/status/2002324487576977716)

生成摘要时出错

---

## 71. Debian adds LoongArch as officially supported architecture

**原文标题**: Debian adds LoongArch as officially supported architecture

**原文链接**: [https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html](https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html)

生成摘要时出错

---

## 72. Designing a Passive Lidar Detector Device

**原文标题**: Designing a Passive Lidar Detector Device

**原文链接**: [https://www.atredis.com/blog/2025/11/20/designing-a-passive-lidar-detection-sensor](https://www.atredis.com/blog/2025/11/20/designing-a-passive-lidar-detection-sensor)

生成摘要时出错

---

## 73. We ran Anthropic’s interviews through structured LLM analysis

**原文标题**: We ran Anthropic’s interviews through structured LLM analysis

**原文链接**: [https://www.playbookatlas.com/research/ai-adoption-explorer](https://www.playbookatlas.com/research/ai-adoption-explorer)

生成摘要时出错

---

## 74. Show HN: Misata – synthetic data engine using LLM and Vectorized NumPy

**原文标题**: Show HN: Misata – synthetic data engine using LLM and Vectorized NumPy

**原文链接**: [https://github.com/rasinmuhammed/misata](https://github.com/rasinmuhammed/misata)

生成摘要时出错

---

## 75. James Webb Space Telescope confirms first 'runaway' supermassive black hole

**原文标题**: James Webb Space Telescope confirms first 'runaway' supermassive black hole

**原文链接**: [https://www.space.com/astronomy/black-holes/james-webb-space-telescope-confirms-1st-runaway-supermassive-black-hole-rocketing-through-cosmic-owl-galaxies-at-2-2-million-mph-it-boggles-the-mind](https://www.space.com/astronomy/black-holes/james-webb-space-telescope-confirms-1st-runaway-supermassive-black-hole-rocketing-through-cosmic-owl-galaxies-at-2-2-million-mph-it-boggles-the-mind)

生成摘要时出错

---

## 76. GPT-5.2-Codex

**原文标题**: GPT-5.2-Codex

**原文链接**: [https://openai.com/index/introducing-gpt-5-2-codex/](https://openai.com/index/introducing-gpt-5-2-codex/)

生成摘要时出错

---

## 77. Noclip.website – A digital museum of video game levels

**原文标题**: Noclip.website – A digital museum of video game levels

**原文链接**: [https://noclip.website/](https://noclip.website/)

生成摘要时出错

---

## 78. Meta Segment Anything Model Audio

**原文标题**: Meta Segment Anything Model Audio

**原文链接**: [https://ai.meta.com/samaudio/](https://ai.meta.com/samaudio/)

生成摘要时出错

---

## 79. Open Source Historical LLM trained exclusively on 19th century text

**原文标题**: Open Source Historical LLM trained exclusively on 19th century text

**原文链接**: [https://github.com/haykgrigo3/TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM)

生成摘要时出错

---

## 80. How getting richer made teenagers less free

**原文标题**: How getting richer made teenagers less free

**原文链接**: [https://www.theargumentmag.com/p/how-getting-richer-made-teenagers](https://www.theargumentmag.com/p/how-getting-richer-made-teenagers)

生成摘要时出错

---

## 81. Building a Transparent Keyserver

**原文标题**: Building a Transparent Keyserver

**原文链接**: [https://words.filippo.io/keyserver-tlog/](https://words.filippo.io/keyserver-tlog/)

生成摘要时出错

---

## 82. Getting bitten by Intel's poor naming schemes

**原文标题**: Getting bitten by Intel's poor naming schemes

**原文链接**: [https://lorendb.dev/posts/getting-bitten-by-poor-naming-schemes/](https://lorendb.dev/posts/getting-bitten-by-poor-naming-schemes/)

生成摘要时出错

---

## 83. Parallelizing ClickHouse aggregation merge for fixed hash map

**原文标题**: Parallelizing ClickHouse aggregation merge for fixed hash map

**原文链接**: [https://blog.incfly.org/parallelize-clickhouse-aggregation-merge-for-fixed-hash-map/](https://blog.incfly.org/parallelize-clickhouse-aggregation-merge-for-fixed-hash-map/)

生成摘要时出错

---

## 84. Two kinds of vibe coding

**原文标题**: Two kinds of vibe coding

**原文链接**: [https://davidbau.com/archives/2025/12/16/vibe_coding.html](https://davidbau.com/archives/2025/12/16/vibe_coding.html)

生成摘要时出错

---

## 85. Please just try HTMX

**原文标题**: Please just try HTMX

**原文链接**: [http://pleasejusttryhtmx.com/](http://pleasejusttryhtmx.com/)

生成摘要时出错

---

## 86. I've been writing ring buffers wrong all these years (2016)

**原文标题**: I've been writing ring buffers wrong all these years (2016)

**原文链接**: [https://www.snellman.net/blog/archive/2016-12-13-ring-buffers/](https://www.snellman.net/blog/archive/2016-12-13-ring-buffers/)

生成摘要时出错

---

## 87. Pompeii site reveals recipe for Roman concrete

**原文标题**: Pompeii site reveals recipe for Roman concrete

**原文链接**: [https://www.cnn.com/2025/12/19/science/roman-concrete-recipe-process-pompeii](https://www.cnn.com/2025/12/19/science/roman-concrete-recipe-process-pompeii)

生成摘要时出错

---

## 88. The Scottish Highlands, the Appalachians, Atlas are the same mountain range

**原文标题**: The Scottish Highlands, the Appalachians, Atlas are the same mountain range

**原文链接**: [https://vividmaps.com/central-pangean-mountains/](https://vividmaps.com/central-pangean-mountains/)

生成摘要时出错

---

## 89. T5Gemma 2: The next generation of encoder-decoder models

**原文标题**: T5Gemma 2: The next generation of encoder-decoder models

**原文链接**: [https://blog.google/technology/developers/t5gemma-2/](https://blog.google/technology/developers/t5gemma-2/)

生成摘要时出错

---

## 90. Android introduces $2-4 install fee and 10–20% cut for US external content links

**原文标题**: Android introduces $2-4 install fee and 10–20% cut for US external content links

**原文链接**: [https://support.google.com/googleplay/android-developer/answer/16470497?hl=en](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en)

生成摘要时出错

---

## 91. How China built its ‘Manhattan Project’ to rival the West in AI chips

**原文标题**: How China built its ‘Manhattan Project’ to rival the West in AI chips

**原文链接**: [https://www.japantimes.co.jp/business/2025/12/18/tech/china-west-ai-chips/](https://www.japantimes.co.jp/business/2025/12/18/tech/china-west-ai-chips/)

生成摘要时出错

---

## 92. FunctionGemma 270M Model

**原文标题**: FunctionGemma 270M Model

**原文链接**: [https://blog.google/technology/developers/functiongemma/](https://blog.google/technology/developers/functiongemma/)

生成摘要时出错

---

## 93. Classical statues were not painted horribly

**原文标题**: Classical statues were not painted horribly

**原文链接**: [https://worksinprogress.co/issue/were-classical-statues-painted-horribly/](https://worksinprogress.co/issue/were-classical-statues-painted-horribly/)

生成摘要时出错

---

## 94. Wood wide web – the underground network of microbes that connects trees

**原文标题**: Wood wide web – the underground network of microbes that connects trees

**原文链接**: [https://www.science.org/content/article/wood-wide-web-underground-network-microbes-connects-trees-mapped-first-time](https://www.science.org/content/article/wood-wide-web-underground-network-microbes-connects-trees-mapped-first-time)

生成摘要时出错

---

## 95. It boots (Linux compatible kernel)

**原文标题**: It boots (Linux compatible kernel)

**原文链接**: [https://github.com/jgarzik/hk](https://github.com/jgarzik/hk)

生成摘要时出错

---

## 96. You can now play Grand Theft Auto Vice City in the browser

**原文标题**: You can now play Grand Theft Auto Vice City in the browser

**原文链接**: [https://dos.zone/grand-theft-auto-vice-city/](https://dos.zone/grand-theft-auto-vice-city/)

生成摘要时出错

---

## 97. Valve is running Apple's playbook in reverse

**原文标题**: Valve is running Apple's playbook in reverse

**原文链接**: [https://www.garbagecollected.dev/p/valve-the-reverse-apple](https://www.garbagecollected.dev/p/valve-the-reverse-apple)

生成摘要时出错

---

## 98. TailwindSQL – Like TailwindCSS, but for SQL Queries in React Server Components

**原文标题**: TailwindSQL – Like TailwindCSS, but for SQL Queries in React Server Components

**原文链接**: [https://github.com/mmarinovic/tailwindsql](https://github.com/mmarinovic/tailwindsql)

生成摘要时出错

---

## 99. Detailed balance in large language model-driven agents

**原文标题**: Detailed balance in large language model-driven agents

**原文链接**: [https://arxiv.org/abs/2512.10047](https://arxiv.org/abs/2512.10047)

生成摘要时出错

---

## 100. SMB Direct – SMB3 over RDMA

**原文标题**: SMB Direct – SMB3 over RDMA

**原文链接**: [https://docs.kernel.org/filesystems/smb/smbdirect.html](https://docs.kernel.org/filesystems/smb/smbdirect.html)

生成摘要时出错

---

