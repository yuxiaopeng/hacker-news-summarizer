# Hacker News 热门文章摘要 (2026-09-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国邮政调查员关停销售伪造邮资标签的网站。

**原文标题**: U.S. postal inspectors shut down website selling counterfeit postage labels

**原文链接**: [https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/)

美国邮政检验局（USPIS）及联邦合作伙伴机构已查封域名 LabelsBank.com，并起诉了该网站运营商——33岁的巴基斯坦男子法希姆·阿克拉姆（Faheem Akram），指控其策划了一场大规模的伪造邮资计划。

根据法庭记录，阿克拉姆利用该非法网站向5000多名客户销售了超过510万张伪造的美国邮政署（USPS）运输标签。据称，该网站对每张标签收取约2美元的统一费用，且不限包裹的目的地、尺寸或重量。这一欺诈行为导致美国邮政署估计损失了超过1.26亿美元的收入。

阿克拉姆被控串谋欺诈美国、制造并销售伪造邮资以及电信欺诈。在起诉之后，法院下令授权立即查封并关闭该网站。

美国检察官杰森·A·雷丁·基诺内斯（Jason A. Reding Quiñones）和迈阿密分局首席邮政检验员布拉迪斯米尔·罗霍（Bladismir Rojo）强调了该欺诈行为的规模，并表示联邦政府将追捕针对美国消费者和邮政系统的国际犯罪者。尽管该网站已被关停且相关起诉已经提起，但官员们提醒公众，在法庭证明其有罪之前，被告应被推定为无罪。

---

## 2. Tcl/Tk 9.1 发布

**原文标题**: Tcl/Tk 9.1 Released

**原文链接**: [https://www.tcl-lang.org/software/tcltk/9.1.html](https://www.tcl-lang.org/software/tcltk/9.1.html)

Tcl/Tk 9.1.0 计划于 2026 年 9 月下旬发布，是继 Tcl/Tk 9.0 之后的下一个开发阶段。此次更新为核心语言和图形工具包引入了重大新特性、命令增强以及性能优化。

**Tcl 9.1 亮点：**
核心 Tcl 语言新增了多个命令，包括用于规范化的 `unicode`、用于高分辨率单调时钟功能的 `timer`，以及用于列表项选择的 `lfilter`。它还为 `subst` 和 `switch` 命令引入了新选项，并将许多 C99 数学例程整合为标准 `expr` 函数。开发者将受益于用于 Unicode 处理和列表操作的新 C API 例程，以及针对大型列表的内存效率提升和扩展的 64 位支持。值得注意的是，应用程序现在需要通过 `Tcl_FindExecutable` 或 `TclZipfs_AppHook` 进行特定初始化。特定平台的更新包括 macOS 上不区分大小写的文件系统路径，以及 Windows 上修订后的搜索机制。

**Tk 9.1 亮点：**
Tk 工具包专注于现代化和无障碍化，引入了屏幕阅读器支持和初步的双向/从右至左（RTL）文本处理能力。新特性包括 `ttk::toggleswitch` 组件、`tk attribtable` 命令以及标签（label）上的旋转文本支持。UI 改进包括优化的列表框选择颜色、更好的负向屏幕距离处理，以及针对 Aqua 平台的 `send` 命令修订。为了精简工具包，已移除对 Windows XP 外观的过时支持。

总体而言，Tcl/Tk 9.1 旨在为开发者提供一个更稳健、更易用且更高效的基础，同时扩展该框架在现代硬件和国际化方面的能力。

---

## 3. GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文标题**: GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price

**原文链接**: [https://openai.com/index/introducing-gpt-6-1-sol/](https://openai.com/index/introducing-gpt-6-1-sol/)

生成摘要时出错

---

## 4. 德里如何将电力损耗从50%降至5%

**原文标题**: How Delhi cut electricity loss from 50 to 5 percent

**原文链接**: [https://spectrum.ieee.org/delhi-electricity-loss](https://spectrum.ieee.org/delhi-electricity-loss)

生成摘要时出错

---

## 5. PS5 Relapse 漏洞利用

**原文标题**: PS5 Relapse Exploit

**原文链接**: [https://github.com/ntfargo/Relapse-Exploit](https://github.com/ntfargo/Relapse-Exploit)

**PS5 Relapse Exploit** 是一款专为固件版本在 **7.00 至 13.60** 之间的 PlayStation 5 主机设计的安全研究工具。该漏洞利用程序由包括 ntfargo 和 TheFlow 在内的贡献者团队开发，可实现内核读/写访问并执行自定义载荷。

**技术细节**
该漏洞利用采用两阶段链条：
1.  **浏览器阶段：** 利用 JavaScriptCore (JSC) 信息泄露和结构化克隆对象池不匹配来损坏类型化数组。
2.  **内核阶段：** 结合地址泄露与 `aio_multi_wait` 释放后重用 (UAF) 竞态条件，以建立内核读/写权限。

**使用与稳定性**
用户可以通过将主机的首选 DNS 设置为 `45.56.67.85` 或在本地托管相关文件来执行该漏洞利用程序。成功触发后，一个 ELF 加载器将在 **9021** 端口激活。文档指出该漏洞利用具有不稳定性：Webkit 阶段可能需要多次刷新浏览器，而内核阶段可能导致系统挂起或“内核恐慌 (kernel panic)”，届时需要完整重启主机。

**风险与免责声明**
本项目严格仅用于教育和安全研究目的。使用该漏洞利用程序存在重大风险，包括系统不稳定、潜在的数据丢失以及被索尼封禁账号的风险。本软件按“原样”提供而不作任何担保，维护者不支持盗版或未经授权访问商业设备的行为。

---

## 6. 尼古拉斯·波尔森（Nicholas Polson）在2026年（截至目前）已发表了258篇学术论文。

**原文标题**: Nicholas Polson has authored 258 academic papers in 2026 (so far)

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/08/27/258/](https://statmodeling.stat.columbia.edu/2026/08/27/258/)

无法访问文章链接。

---

## 7. DraftKings正利用人工智能针对嗜赌成瘾者进行行为定向。

**原文标题**: DraftKings Is Using AI to Behaviorally Target Chronic Gamblers

**原文链接**: [https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising)

电子前哨基金会（EFF）报告称，DraftKings 正利用人工智能和机器学习来识别并锁定“处于亏损状态的”赌客。通过分析内部投注记录，DraftKings 训练模型以寻找最有可能输钱的客户，并向其发送个性化的促销信息，诱导其重返平台。这种做法专门剥削“问题赌客”，将公司利润置于弱势个体的福祉之上。

EFF 强调了这种做法存在的几个关键问题：

*   **人工智能驱动的剥削：** 人工智能通过高速处理海量数据集，放大了行为广告的危害。由于人工智能运作如同“黑箱”，它会促使公司收集尽可能多的数据，以优化其模型。
*   **监控风险：** 为行为广告收集的数据经常流入“监控产业”。最初为广告收集的信息通常被出售给保险公司、银行以及美国移民及海关执法局（ICE）和美国海关及边境保护局（CBP）等政府机构，用于调查目的。
*   **第一方数据漏洞：** DraftKings 主要使用直接从用户处收集的“第一方数据”。EFF 认为，仅针对第三方数据共享的政策方案是不够的；要制止这种掠夺性的定向投放，必须禁止所有的行为广告。

最终，EFF 主张，禁止行为广告是消除大规模数据收集动机的唯一途径。他们鼓励用户利用隐私资源（例如其“监控自卫”项目）来保护自己免受这些不断演变的数字威胁。

---

## 8. NAND-16: a computer built from 277,248 NAND gates

**原文标题**: NAND-16: a computer built from 277,248 NAND gates

**原文链接**: [https://somethingbig.ai/computer](https://somethingbig.ai/computer)

**NAND-16** is a project that demonstrates the power of universal logic by constructing a fully functional 16-bit computer using only a single type of component: the **NAND gate**. Comprising exactly **277,248 gates**, the project serves as a massive-scale implementation of the "Nand to Tetris" philosophy, showing how complex computational systems emerge from the simplest possible building blocks.

**Key Features and Technical Details:**

*   **16-bit Architecture:** The computer operates on 16-bit data and addresses, allowing it to handle a level of complexity far beyond simple logic demonstrations.
*   **Universal Logic:** The project proves the principle of functional completeness, where every necessary component—including the Arithmetic Logic Unit (ALU), registers, program counter, and memory management—is synthesized entirely from NAND gates.
*   **Scale and Complexity:** With over a quarter-million gates, the design represents a significant engineering feat, bridging the gap between theoretical computer science and practical hardware architecture.
*   **Educational Value:** The project demystifies the layers of abstraction in modern computing. It provides a transparent view of how binary signals are transformed into executable instructions, showing the direct lineage from electricity to high-level logic.

In summary, NAND-16 is a comprehensive exercise in digital logic design. It illustrates that with enough scale and proper organization, the most basic unit of digital electronics can be used to build a machine capable of general-purpose computing, providing a profound look at the foundational mechanics of the digital age.

---

## 9. Web与移动端对话式AI智能体的隐私分析 [pdf]

**原文标题**: A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]

**原文链接**: [https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)

This article provides a comprehensive evaluation of the privacy landscapes surrounding popular Large Language Model (LLM) platforms, specifically comparing their web-based interfaces with their mobile application counterparts. As conversational AI becomes integrated into daily life, the study investigates the extent to which these agents respect user data and adhere to privacy standards.

**Key Findings:**

*   **Platform Disparities:** The research highlights a significant "privacy gap" between web and mobile versions of the same AI agent. Mobile applications are generally more intrusive, frequently requesting extensive device permissions—such as precise location, microphone access, and contact lists—that are often unnecessary for the agent’s core functionality.
*   **Data Collection Practices:** Most agents collect a vast array of information, including chat histories, account metadata, and device identifiers. A primary concern identified is the use of "training data"; many providers are ambiguous about how they scrub Personally Identifiable Information (PII) before using user conversations to retrain future models.
*   **Third-Party Tracking:** The analysis reveals that mobile AI apps often integrate numerous third-party Software Development Kits (SDKs). These are used for analytics and advertising, leading to the silent transmission of user telemetry data to external domains, a practice less prevalent on "cleaner" web interfaces.
*   **Regulatory & Policy Lacunae:** The study finds that privacy policies are often written in vague, legalistic language that fails to provide users with clear "opt-out" mechanisms regarding data retention or model training.

**Conclusion:**
The authors conclude that the rapid deployment of conversational AI has outpaced current privacy protections. They advocate for "Privacy by Design," urging developers to implement stricter data minimization and providing users with more granular control over how their conversational data is stored and utilized. There is a call for regulators to establish standardized transparency requirements specifically tailored to generative AI.

---

## 10. Show HN: TurboGPT: train 22KiB transformer in 13s

**原文标题**: Show HN: TurboGPT: train 22KiB transformer in 13s

**原文链接**: [https://github.com/lostmsu/TurboGPT](https://github.com/lostmsu/TurboGPT)

生成摘要时出错

---

## 11. Dots: Always-on agents

**原文标题**: Dots: Always-on agents

**原文链接**: [https://openai.com/index/introducing-dots/](https://openai.com/index/introducing-dots/)

生成摘要时出错

---

## 12. Virus Stole a Human Gene and Won't Let Go of It

**原文标题**: Virus Stole a Human Gene and Won't Let Go of It

**原文链接**: [https://www.nytimes.com/2026/09/28/science/virus-molluscum-human-gene.html](https://www.nytimes.com/2026/09/28/science/virus-molluscum-human-gene.html)

生成摘要时出错

---

## 13. Phyllotaxis: An audio-reactive LED display

**原文标题**: Phyllotaxis: An audio-reactive LED display

**原文链接**: [https://jagi.studio/posts/phyllotaxis/](https://jagi.studio/posts/phyllotaxis/)

生成摘要时出错

---

## 14. 美国参考

**原文标题**: America.gov

**原文链接**: [https://america.gov/](https://america.gov/)

生成摘要时出错

---

## 15. Stuck in the Suez Canal – the short version (2021)

**原文标题**: Stuck in the Suez Canal – the short version (2021)

**原文链接**: [https://cathsenker.co.uk/stuck-in-the-suez-canal-the-short-version/](https://cathsenker.co.uk/stuck-in-the-suez-canal-the-short-version/)

生成摘要时出错

---

## 16. Without the Hot Air

**原文标题**: Without the Hot Air

**原文链接**: [https://www.withouthotair.com/](https://www.withouthotair.com/)

生成摘要时出错

---

## 17. C64 MERCENARY (1985): a novel exploit bug at the start of the game

**原文标题**: C64 MERCENARY (1985): a novel exploit bug at the start of the game

**原文链接**: [https://gamesexplained.com/c64/mercenary/](https://gamesexplained.com/c64/mercenary/)

生成摘要时出错

---

## 18. GLM-5.3 and the spread of advanced cyber capabilities

**原文标题**: GLM-5.3 and the spread of advanced cyber capabilities

**原文链接**: [https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)

生成摘要时出错

---

## 19. Jeeves. Reasoning improves Jev-like decision models

**原文标题**: Jeeves. Reasoning improves Jev-like decision models

**原文链接**: [https://github.com/PostHog/jeeves](https://github.com/PostHog/jeeves)

生成摘要时出错

---

## 20. Show HN: Real-time Solar System with 526k asteroids and all tracked satellites

**原文标题**: Show HN: Real-time Solar System with 526k asteroids and all tracked satellites

**原文链接**: [https://space.bl2.net/](https://space.bl2.net/)

生成摘要时出错

---

## 21. A Staff Engineer's Guide to Inventing Work

**原文标题**: A Staff Engineer's Guide to Inventing Work

**原文链接**: [https://sujithjay.com/inventing-work](https://sujithjay.com/inventing-work)

生成摘要时出错

---

## 22. Walking Men

**原文标题**: Walking Men

**原文链接**: [https://bookofjoe2.blogspot.com/2026/09/walking-men.html](https://bookofjoe2.blogspot.com/2026/09/walking-men.html)

生成摘要时出错

---

## 23. Using any C++ library in Godot

**原文标题**: Using any C++ library in Godot

**原文链接**: [https://blog.conan.io/cpp/conan/gamedev/godot/cmake/2026/09/29/Using-Any-Cpp-Library-In-Godot.html](https://blog.conan.io/cpp/conan/gamedev/godot/cmake/2026/09/29/Using-Any-Cpp-Library-In-Godot.html)

生成摘要时出错

---

## 24. Memory Companies Have Destroyed the Consumer Market

**原文标题**: Memory Companies Have Destroyed the Consumer Market

**原文链接**: [https://gamersnexus.net/news-features/memory-companies-have-destroyed-consumer-market](https://gamersnexus.net/news-features/memory-companies-have-destroyed-consumer-market)

生成摘要时出错

---

## 25. You are no longer invited to dinner

**原文标题**: You are no longer invited to dinner

**原文链接**: [https://www.derekthompson.org/p/the-death-of-the-american-host](https://www.derekthompson.org/p/the-death-of-the-american-host)

生成摘要时出错

---

## 26. AI needs $6T in annual revenue to justify data centre boom

**原文标题**: AI needs $6T in annual revenue to justify data centre boom

**原文链接**: [https://www.thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/](https://www.thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/)

生成摘要时出错

---

## 27. DevDay 2026 Recap

**原文标题**: DevDay 2026 Recap

**原文链接**: [https://openai.com/index/devday-2026-recap/](https://openai.com/index/devday-2026-recap/)

生成摘要时出错

---

## 28. What if Jev spoke Arrow?

**原文标题**: What if Jev spoke Arrow?

**原文链接**: [https://columnar.tech/blog/what-if-jev-spoke-arrow/](https://columnar.tech/blog/what-if-jev-spoke-arrow/)

生成摘要时出错

---

## 29. Digital Audio on the ZX Spectrum's 1-Bit Beeper

**原文标题**: Digital Audio on the ZX Spectrum's 1-Bit Beeper

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/09/26/digital-audio-on-the-zx-spectrums-1-bit-beeper/](https://bumbershootsoft.wordpress.com/2026/09/26/digital-audio-on-the-zx-spectrums-1-bit-beeper/)

生成摘要时出错

---

## 30. Galaxy Game – Interim Computer Museum

**原文标题**: Galaxy Game – Interim Computer Museum

**原文链接**: [https://icm.museum/blog/?p=698](https://icm.museum/blog/?p=698)

生成摘要时出错

---

## 31. 1 in 8 cancer cases worldwide are caused by infections, study finds

**原文标题**: 1 in 8 cancer cases worldwide are caused by infections, study finds

**原文链接**: [https://www.cbc.ca/lite/story/9.7361622](https://www.cbc.ca/lite/story/9.7361622)

生成摘要时出错

---

## 32. Google ending ChromeOS support two years early

**原文标题**: Google ending ChromeOS support two years early

**原文链接**: [https://www.theregister.com/os-platforms/2026/09/29/google-ending-chromeos-support-two-years-early/5299674](https://www.theregister.com/os-platforms/2026/09/29/google-ending-chromeos-support-two-years-early/5299674)

生成摘要时出错

---

## 33. TIRx Harness: An Open Compiler Harness for Agentic GPU Programming

**原文标题**: TIRx Harness: An Open Compiler Harness for Agentic GPU Programming

**原文链接**: [https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming](https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming)

生成摘要时出错

---

## 34. Individual locomotor bias drives counterclockwise motion in pedestrian crowds

**原文标题**: Individual locomotor bias drives counterclockwise motion in pedestrian crowds

**原文链接**: [https://www.nature.com/articles/s41467-026-73713-w](https://www.nature.com/articles/s41467-026-73713-w)

生成摘要时出错

---

## 35. Booted up in 1993, this server still runs – but not for much longer (2017)

**原文标题**: Booted up in 1993, this server still runs – but not for much longer (2017)

**原文链接**: [https://www.computerworld.com/article/1673071/booted-up-in-1993-this-server-still-runs-but-not-for-much-longer-2.html](https://www.computerworld.com/article/1673071/booted-up-in-1993-this-server-still-runs-but-not-for-much-longer-2.html)

生成摘要时出错

---

## 36. Show HN: Jevstiller – Distill Jev into a local model, with a disagreement bound

**原文标题**: Show HN: Jevstiller – Distill Jev into a local model, with a disagreement bound

**原文链接**: [https://jevstiller.pages.dev/posts/the-guarantee/](https://jevstiller.pages.dev/posts/the-guarantee/)

生成摘要时出错

---

## 37. McDonald's push to have AI price your Big Mac

**原文标题**: McDonald's push to have AI price your Big Mac

**原文链接**: [https://www.cnbc.com/2026/09/29/inside-mcdonalds-push-ai-price-big-mac.html](https://www.cnbc.com/2026/09/29/inside-mcdonalds-push-ai-price-big-mac.html)

生成摘要时出错

---

## 38. Software occlusion culling in Block Game

**原文标题**: Software occlusion culling in Block Game

**原文链接**: [https://enikofox.com/posts/software-rendered-occlusion-culling-in-block-game/](https://enikofox.com/posts/software-rendered-occlusion-culling-in-block-game/)

生成摘要时出错

---

## 39. macOS Golden Gate Is a Buggy Mess

**原文标题**: macOS Golden Gate Is a Buggy Mess

**原文链接**: [https://www.squareorbits.com/blog/2026/09/macos-golden-gate-is-a-buggy-mess/](https://www.squareorbits.com/blog/2026/09/macos-golden-gate-is-a-buggy-mess/)

生成摘要时出错

---

## 40. OpenAI Targets $30B in New Funding at $1.4T Value

**原文标题**: OpenAI Targets $30B in New Funding at $1.4T Value

**原文链接**: [https://www.bloomberg.com/news/articles/2026-09-29/openai-targets-30-billion-in-new-funding-at-1-4-trillion-value](https://www.bloomberg.com/news/articles/2026-09-29/openai-targets-30-billion-in-new-funding-at-1-4-trillion-value)

生成摘要时出错

---

## 41. 500k facial scans at UK stations yield no arrests, 1 false positive

**原文标题**: 500k facial scans at UK stations yield no arrests, 1 false positive

**原文链接**: [https://www.theguardian.com/technology/2026/sep/29/trial-live-facial-recognition-cameras-london-stations-false-positive](https://www.theguardian.com/technology/2026/sep/29/trial-live-facial-recognition-cameras-london-stations-false-positive)

生成摘要时出错

---

## 42. ESP32S3 cluster running 1.58-bit (BitNet) Language model

**原文标题**: ESP32S3 cluster running 1.58-bit (BitNet) Language model

**原文链接**: [https://github.com/Low-Zi-Hong/ESP32s3-LLM-Cluster](https://github.com/Low-Zi-Hong/ESP32s3-LLM-Cluster)

生成摘要时出错

---

## 43. MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文标题**: MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文链接**: [https://stateofutopia.com/experiments/microllmlab/](https://stateofutopia.com/experiments/microllmlab/)

生成摘要时出错

---

## 44. 12,000-year-old Göbeklitepe burials explain scattered bones

**原文标题**: 12,000-year-old Göbeklitepe burials explain scattered bones

**原文链接**: [https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/](https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/)

生成摘要时出错

---

## 45. Four CHI '26 papers I wish I wrote

**原文标题**: Four CHI '26 papers I wish I wrote

**原文链接**: [https://countingfromzero.blog/2026/04/24/four-chi-26-papers-i-wish-i-wrote/](https://countingfromzero.blog/2026/04/24/four-chi-26-papers-i-wish-i-wrote/)

生成摘要时出错

---

## 46. Tank Body Problem

**原文标题**: Tank Body Problem

**原文链接**: [http://www.jimsitu.com](http://www.jimsitu.com)

生成摘要时出错

---

## 47. ChatGPT Pro 500

**原文标题**: ChatGPT Pro 500

**原文链接**: [https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)

生成摘要时出错

---

## 48. Optimizing x264 settings and per-title ladders

**原文标题**: Optimizing x264 settings and per-title ladders

**原文链接**: [https://streaminglearningcenter.com/articles/optimizing-x264-settings-and-per-title-ladders.html](https://streaminglearningcenter.com/articles/optimizing-x264-settings-and-per-title-ladders.html)

生成摘要时出错

---

## 49. Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

**原文标题**: Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

**原文链接**: [https://github.com/firelex/jeff](https://github.com/firelex/jeff)

生成摘要时出错

---

## 50. Nvidia wants to put a watchdog chip next to every AI agent

**原文标题**: Nvidia wants to put a watchdog chip next to every AI agent

**原文链接**: [https://www.cnbc.com/2026/09/28/nvidia-releases.html](https://www.cnbc.com/2026/09/28/nvidia-releases.html)

生成摘要时出错

---

## 51. Hijacking the PS5's RTMP stream

**原文标题**: Hijacking the PS5's RTMP stream

**原文链接**: [https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/](https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/)

生成摘要时出错

---

## 52. Kids turned low-traffic NPR Spotify comments into a secret group chat

**原文标题**: Kids turned low-traffic NPR Spotify comments into a secret group chat

**原文链接**: [https://www.thisamericanlife.org/897/transcript](https://www.thisamericanlife.org/897/transcript)

生成摘要时出错

---

## 53. Georeferencing Chernarus and visiting in real life (2021)

**原文标题**: Georeferencing Chernarus and visiting in real life (2021)

**原文链接**: [https://longcreek.me/blog/2021/chernarus-irl](https://longcreek.me/blog/2021/chernarus-irl)

生成摘要时出错

---

## 54. Sonnet 5.5

**原文标题**: Sonnet 5.5

**原文链接**: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)

生成摘要时出错

---

## 55. The systems that no one will test

**原文标题**: The systems that no one will test

**原文链接**: [https://blog.christianperone.com/2026/09/the-systems-that-no-one-will-test/](https://blog.christianperone.com/2026/09/the-systems-that-no-one-will-test/)

生成摘要时出错

---

## 56. How El Niño Made the Atlantic Hurricane Season Disappear

**原文标题**: How El Niño Made the Atlantic Hurricane Season Disappear

**原文链接**: [https://www.wsj.com/us-news/climate-environment/how-el-nino-made-the-atlantic-hurricane-season-disappear-142b9ac9](https://www.wsj.com/us-news/climate-environment/how-el-nino-made-the-atlantic-hurricane-season-disappear-142b9ac9)

生成摘要时出错

---

## 57. Does Reddit have an astroturfing problem? What the data suggests

**原文标题**: Does Reddit have an astroturfing problem? What the data suggests

**原文链接**: [https://www.petervijeh.com/projects/reddit-astroturf](https://www.petervijeh.com/projects/reddit-astroturf)

生成摘要时出错

---

## 58. The US state replacing power plants with home batteries

**原文标题**: The US state replacing power plants with home batteries

**原文链接**: [https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms)

生成摘要时出错

---

## 59. When did Google get so weird?

**原文标题**: When did Google get so weird?

**原文链接**: [https://sancho.bearblog.dev/google-weird/](https://sancho.bearblog.dev/google-weird/)

生成摘要时出错

---

## 60. When did Google get so weird?

**原文标题**: When did Google get so weird?

**原文链接**: [https://sancho.bearblog.dev/google-weird/](https://sancho.bearblog.dev/google-weird/)

生成摘要时出错

---

## 61. ShinyHunters member charged with attempted incitement to commit murder

**原文标题**: ShinyHunters member charged with attempted incitement to commit murder

**原文链接**: [https://databreaches.net/2026/09/29/shocker-suspected-shinyhunters-member-charged-with-attempted-incitement-to-commit-two-murders/](https://databreaches.net/2026/09/29/shocker-suspected-shinyhunters-member-charged-with-attempted-incitement-to-commit-two-murders/)

生成摘要时出错

---

## 62. Startup Nights 2026 is comming up on 5-6 Nov. in Switzerland

**原文标题**: Startup Nights 2026 is comming up on 5-6 Nov. in Switzerland

**原文链接**: [https://www.startup-nights.ch/event/](https://www.startup-nights.ch/event/)

生成摘要时出错

---

## 63. California farmers are struggling to sell grapes as demand for wine drops

**原文标题**: California farmers are struggling to sell grapes as demand for wine drops

**原文链接**: [https://www.kqed.org/news/12101534/california-farmers-are-struggling-to-sell-grapes-as-demand-for-wine-drops](https://www.kqed.org/news/12101534/california-farmers-are-struggling-to-sell-grapes-as-demand-for-wine-drops)

生成摘要时出错

---

## 64. Scientists solve 1840s space weather mystery

**原文标题**: Scientists solve 1840s space weather mystery

**原文链接**: [https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/](https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/)

生成摘要时出错

---

## 65. Show HN: HN.watch – Videos of all Hacker News posts

**原文标题**: Show HN: HN.watch – Videos of all Hacker News posts

**原文链接**: [https://hn.watch/](https://hn.watch/)

生成摘要时出错

---

## 66. World Labs is Joining AMD

**原文标题**: World Labs is Joining AMD

**原文链接**: [https://www.worldlabs.ai/blog/amd-announcement](https://www.worldlabs.ai/blog/amd-announcement)

生成摘要时出错

---

## 67. Where's the "Intelligence Explosion"?

**原文标题**: Where's the "Intelligence Explosion"?

**原文链接**: [https://www.noahpinion.blog/p/wheres-the-intelligence-explosion](https://www.noahpinion.blog/p/wheres-the-intelligence-explosion)

生成摘要时出错

---

## 68. Behold the pawpaw

**原文标题**: Behold the pawpaw

**原文链接**: [https://www.cbc.ca/radio/thecurrent/pawpaw-tropical-fruit-canada-9.7356882](https://www.cbc.ca/radio/thecurrent/pawpaw-tropical-fruit-canada-9.7356882)

生成摘要时出错

---

## 69. Pirating the Pirates

**原文标题**: Pirating the Pirates

**原文链接**: [https://mubi.com/en/notebook/posts/pirating-the-pirates](https://mubi.com/en/notebook/posts/pirating-the-pirates)

生成摘要时出错

---

## 70. Evan Doorbell's Phone Tapes – Brought to You by Telephone World

**原文标题**: Evan Doorbell's Phone Tapes – Brought to You by Telephone World

**原文链接**: [https://evan-doorbell.com/](https://evan-doorbell.com/)

生成摘要时出错

---

## 71. It's Time to Investigate the AI Labs

**原文标题**: It's Time to Investigate the AI Labs

**原文链接**: [https://calnewport.com/its-time-to-investigate-the-ai-labs/](https://calnewport.com/its-time-to-investigate-the-ai-labs/)

生成摘要时出错

---

## 72. Building a certificate authority for the whole Internet

**原文标题**: Building a certificate authority for the whole Internet

**原文链接**: [https://blog.cloudflare.com/cloudflare-certificate-authority/](https://blog.cloudflare.com/cloudflare-certificate-authority/)

生成摘要时出错

---

## 73. Backblaze Drive Stats for Q2 2026

**原文标题**: Backblaze Drive Stats for Q2 2026

**原文链接**: [https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/)

生成摘要时出错

---

## 74. Cf: The Agentic CLI for the Cloudflare API

**原文标题**: Cf: The Agentic CLI for the Cloudflare API

**原文链接**: [https://blog.cloudflare.com/cloudflare-cf-cli-launch/](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

生成摘要时出错

---

## 75. Show HN: Destroy Any Website with Stickman

**原文标题**: Show HN: Destroy Any Website with Stickman

**原文链接**: [https://destroy.spritefusion.com/](https://destroy.spritefusion.com/)

生成摘要时出错

---

## 76. Electrification efficiency: The world will need less energy after the transition

**原文标题**: Electrification efficiency: The world will need less energy after the transition

**原文链接**: [https://hannahritchie.substack.com/p/electrification-energy-efficiency](https://hannahritchie.substack.com/p/electrification-energy-efficiency)

生成摘要时出错

---

## 77. Coding is not solved

**原文标题**: Coding is not solved

**原文链接**: [https://blog.alexewerlof.com/p/coding-is-not-solved](https://blog.alexewerlof.com/p/coding-is-not-solved)

生成摘要时出错

---

## 78. 1996 chat room simulator connected to Win95 and System 7 web desktops

**原文标题**: 1996 chat room simulator connected to Win95 and System 7 web desktops

**原文链接**: [https://lolchat.rip/](https://lolchat.rip/)

生成摘要时出错

---

## 79. Language Models for Text Classification: From Bag-of-Words to Jev

**原文标题**: Language Models for Text Classification: From Bag-of-Words to Jev

**原文链接**: [https://magazine.sebastianraschka.com/p/classifier-history-and-jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev)

生成摘要时出错

---

## 80. 37,500 border drawings: a map of the world as people remember it

**原文标题**: 37,500 border drawings: a map of the world as people remember it

**原文链接**: [https://www.habibicode.org/thedrawnworld](https://www.habibicode.org/thedrawnworld)

生成摘要时出错

---

## 81. Updated Google Maps shows destruction of the city of Rafah

**原文标题**: Updated Google Maps shows destruction of the city of Rafah

**原文链接**: [https://twitter.com/AliAbunimah/status/2103890594137309425](https://twitter.com/AliAbunimah/status/2103890594137309425)

生成摘要时出错

---

## 82. AI models keep posting screenshots showing sensitive data from inside companies

**原文标题**: AI models keep posting screenshots showing sensitive data from inside companies

**原文链接**: [https://www.theregister.com/ai-and-ml/2026/09/29/ai-models-keep-posting-screenshots-showing-sensitive-data-from-inside-tech-companies/5299640](https://www.theregister.com/ai-and-ml/2026/09/29/ai-models-keep-posting-screenshots-showing-sensitive-data-from-inside-tech-companies/5299640)

生成摘要时出错

---

## 83. Footguns with Postgres “at time zone 'UTC'”

**原文标题**: Footguns with Postgres “at time zone 'UTC'”

**原文链接**: [https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does](https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does)

生成摘要时出错

---

## 84. What would a serious AI product look like?

**原文标题**: What would a serious AI product look like?

**原文链接**: [https://blog.glyph.im/2026/09/serious-ai-product.html](https://blog.glyph.im/2026/09/serious-ai-product.html)

生成摘要时出错

---

## 85. Mistral CEO says U.S. AI safety debate masks competitors' 'negligence'

**原文标题**: Mistral CEO says U.S. AI safety debate masks competitors' 'negligence'

**原文链接**: [https://www.cnbc.com/2026/09/29/mistral-ai-safety-openai-anthropic.html](https://www.cnbc.com/2026/09/29/mistral-ai-safety-openai-anthropic.html)

生成摘要时出错

---

## 86. Nissan's third generation e-POWER powertrain

**原文标题**: Nissan's third generation e-POWER powertrain

**原文链接**: [https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/E_POWER_GEN3/](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/E_POWER_GEN3/)

生成摘要时出错

---

## 87. What heraldry and Japanese mon can teach about visual-identity generators

**原文标题**: What heraldry and Japanese mon can teach about visual-identity generators

**原文链接**: [https://benovermyer.com/blog/2026/09/japanese-vs-western-heraldry/](https://benovermyer.com/blog/2026/09/japanese-vs-western-heraldry/)

生成摘要时出错

---

## 88. Stupid Over-Reliance on Palantir AI Helped Lead to US Bombing of Iranian School

**原文标题**: Stupid Over-Reliance on Palantir AI Helped Lead to US Bombing of Iranian School

**原文链接**: [https://www.techdirt.com/2026/09/29/reporting-confirms-stupid-over-reliance-on-palantir-ai-helped-lead-to-us-bombing-of-iranian-schoolgirls/](https://www.techdirt.com/2026/09/29/reporting-confirms-stupid-over-reliance-on-palantir-ai-helped-lead-to-us-bombing-of-iranian-schoolgirls/)

生成摘要时出错

---

## 89. Show HN: PaperMono, e-ink fridge magnet shopping list with mobile web page

**原文标题**: Show HN: PaperMono, e-ink fridge magnet shopping list with mobile web page

**原文链接**: [https://github.com/seamusc/papermono-shopping-list](https://github.com/seamusc/papermono-shopping-list)

生成摘要时出错

---

## 90. Dead Money

**原文标题**: Dead Money

**原文链接**: [https://www.wheresyoured.at/dead-money/](https://www.wheresyoured.at/dead-money/)

生成摘要时出错

---

## 91. Show HN: Free alternative to graphics design giants

**原文标题**: Show HN: Free alternative to graphics design giants

**原文链接**: [https://scissor.studio/](https://scissor.studio/)

生成摘要时出错

---

## 92. The art forger who became a national hero

**原文标题**: The art forger who became a national hero

**原文链接**: [https://priceonomics.com/the-art-forger-who-became-a-national-hero/](https://priceonomics.com/the-art-forger-who-became-a-national-hero/)

生成摘要时出错

---

## 93. What is the best shape of a city? Modelling effect of urban form on distance

**原文标题**: What is the best shape of a city? Modelling effect of urban form on distance

**原文链接**: [https://journals.sagepub.com/doi/10.1177/23998083261458842](https://journals.sagepub.com/doi/10.1177/23998083261458842)

生成摘要时出错

---

## 94. The Beatles have permeated research papers across academic disciplines

**原文标题**: The Beatles have permeated research papers across academic disciplines

**原文链接**: [https://phys.org/news/2026-09-beatles-permeated-papers-academic-disciplines.html](https://phys.org/news/2026-09-beatles-permeated-papers-academic-disciplines.html)

生成摘要时出错

---

## 95. MongoDB CEO resigns to join Meta

**原文标题**: MongoDB CEO resigns to join Meta

**原文链接**: [https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/](https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/)

生成摘要时出错

---

## 96. New Cyber-OSINT model released

**原文标题**: New Cyber-OSINT model released

**原文链接**: [https://twitter.com/0x0SojalSec/status/2104736980768866439](https://twitter.com/0x0SojalSec/status/2104736980768866439)

生成摘要时出错

---

## 97. How to win a beer with high-dimensional statistics

**原文标题**: How to win a beer with high-dimensional statistics

**原文链接**: [https://jamiesimon.io/blog/how-to-win-a-beer-with-high-dimensional-statistics/](https://jamiesimon.io/blog/how-to-win-a-beer-with-high-dimensional-statistics/)

生成摘要时出错

---

## 98. Parley: Federated, decentralised chat that speaks plain IRC

**原文标题**: Parley: Federated, decentralised chat that speaks plain IRC

**原文链接**: [https://git.mills.io/prologic/parley](https://git.mills.io/prologic/parley)

生成摘要时出错

---

## 99. Claude partial outage

**原文标题**: Claude partial outage

**原文链接**: [https://status.claude.com/incidents/4xvtc2gnq73l](https://status.claude.com/incidents/4xvtc2gnq73l)

生成摘要时出错

---

## 100. Reducing undefined behavior in the C language

**原文标题**: Reducing undefined behavior in the C language

**原文链接**: [https://lwn.net/SubscriberLink/1095811/b9325731ea9b61e0/](https://lwn.net/SubscriberLink/1095811/b9325731ea9b61e0/)

生成摘要时出错

---

