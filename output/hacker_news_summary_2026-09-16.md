# Hacker News 热门文章摘要 (2026-09-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 向量化且性能可移植的快速排序

**原文标题**: Vectorized and performance-portable Quicksort

**原文链接**: [https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html](https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html)

研究人员开发了一种矢量化、性能可移植的快速排序（Quicksort）实现，其性能比 C++ 标准库（`std::sort`）快 10 到 19 倍。尽管排序在传统上一直是计算瓶颈，但这种新方法利用 SIMD（单指令多数据）指令，大幅加速了算法的划分阶段。

**关键技术创新：**
该实现利用现代指令集（如 AVX-512 和 Arm SVE）中的“压缩存储”（compress-store）指令，根据基准值快速将元素过滤到子数组中。为了确保可移植性，研究人员使用了 **Highway** SIMD 库，使代码能够在六种不同的指令集（包括 AVX2、AVX-512 和 Arm NEON）上高效运行，而无需针对每种架构进行手动重新优化。在缺乏“压缩存储”指令的旧硬件上，该库通过排列（permute）指令模拟该功能。

**性能与通用性：**
*   **高吞吐量：** 该算法在 Intel Skylake (AVX-512) 上的处理速度达到约 1.1 GB/s，在 Apple M1 (NEON) 上接近 500 MB/s。
*   **广泛支持：** 与以往仅限于 32 位整数的专用排序算法不同，该版本支持 16 位到 128 位的全范围输入。
*   **高效性：** 它甚至优于现有的针对特定架构的最先进算法，例如仅针对 AVX2 优化的算法。

**重要意义：**
这一突破对于列式数据库尤为重要，因为快速排序和过滤是高性能 SQL 查询的核心需求。通过在单个 CPU 核心上实现 1 GB/s 的处理能力，该实现为数据处理开辟了新的可能性。该项目基于 Apache2 协议开源，并已在 GitHub 上发布。

---

## 2. Training a 4B model to produce 81% faster query plans than Postgres

**原文标题**: Training a 4B model to produce 81% faster query plans than Postgres

**原文链接**: [https://rohanbansal.com/qorl](https://rohanbansal.com/qorl)

This article documents a successful experiment in which a 4B-parameter language model was trained to outperform the Postgres query optimizer, achieving a **44.7% reduction in latency** across 113 join-heavy queries.

The author identifies that while query optimization—specifically **join ordering**—is an NP-hard problem, it is an ideal candidate for Reinforcement Learning (RL) because the output is easily verifiable: a "good" plan is simply one that runs faster. Traditional optimizers like Postgres struggle with the **combinatorial explosion** of possible plans. For a query with nine tables, factors such as join trees, inner/outer orientations, algorithms (hash vs. merge), and scan types (sequential vs. index) result in quadrillions of potential execution paths.

**Key methodology and technical highlights include:**
*   **Post-Training:** The model underwent Supervised Fine-Tuning (SFT) followed by agentic RL.
*   **GRPO Variant:** The author designed a custom variant of Group Relative Policy Optimization to score RL rollouts in a noisy environment.
*   **Noise Reduction:** To ensure accurate benchmarking, a custom Postgres rig was built to minimize Linux page cache contention across concurrent containers.
*   **Distributed Training:** The setup utilized vLLM and a trainer on a remote 2x H100 node, while the Postgres execution environment ran on local hardware.
*   **Distillation:** The process incorporated off-policy distillation from high-quality agent trajectories.

The experiment demonstrates that a small, open-weights model can learn to navigate massive search spaces more effectively than traditional heuristic-based or dynamic programming optimizers. By focusing on the single axis of execution time, the model evolved from being unable to produce valid plans to consistently beating Postgres’s default selections.

---

## 3. Small programming tricks

**原文标题**: Small programming tricks

**原文链接**: [https://will-keleher.com/posts/small-programming-tricks-matter/](https://will-keleher.com/posts/small-programming-tricks-matter/)

生成摘要时出错

---

## 4. AMD 矩阵核心的精确模型

**原文标题**: Accurate Models of AMD Matrix Cores

**原文链接**: [https://arxiv.org/abs/2609.14845](https://arxiv.org/abs/2609.14845)

《AMD 矩阵核心的精确模型》针对 GPU 矩阵乘法器缺乏标准化和文档记录的问题进行了研究，这些硬件通常偏离 IEEE 754 浮点标准。由于累加器宽度、舍入行为和次正规数处理等特性在不同厂商及代际之间存在差异，仅通过软件往往无法在不同设备间实现位级可复现性。

研究人员表征了三种 AMD 架构的数值行为：CDNA 1 (MI100)、CDNA 2 (MI210/250) 和 CDNA 3 (MI300A/X)。为了逆向推导这些未公开的实现细节，作者设计了特定的测试向量，以探测所有支持的输入格式下的数值特性。随后，他们为每种架构开发了基于 MATLAB 的软件模型。

为确保位级准确性，作者采用了迭代精化技术。他们利用包含 1000 万个输入向量的随机化测试集，针对硬件对模型进行了验证，不断完善逻辑，直到软件模型在所有情况下都与硬件输出完全匹配。

最后，作者通过对比分析 AMD 矩阵核心与 NVIDIA Tensor Core 的应用级精度，展示了这些模型的实用价值。这项工作为理解特定硬件的数值差异提供了一个框架，并为高性能计算和数学软件领域更精确的实验研究奠定了基础。

---

## 5. 通胀担忧推高债券收益率，美联储加息。

**原文标题**: Fed hikes rates as inflation worries push up bond yields

**原文链接**: [https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/](https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/)

无法访问文章链接。

---

## 6. Dream-RSI：通过演化世界实现递归自我提升

**原文标题**: Dream-RSI: Recursive Self-Improvement through Evolving Worlds

**原文链接**: [https://arxiv.org/abs/2609.14858](https://arxiv.org/abs/2609.14858)

摘要生成失败

---

## 7. Mistral X Mozilla：私密、多语言 AI 浏览

**原文标题**: Mistral X Mozilla: Private, Multilingual AI Browsing

**原文链接**: [https://mistral.ai/news/mistral-x-mozilla/](https://mistral.ai/news/mistral-x-mozilla/)

Mistral 和 Mozilla 宣布建立战略合作伙伴关系，将 Mistral 的 AI 模型集成到一款全新的 AI 驱动浏览助手——**Firefox Smart Window** 中。Smart Window 目前处于测试阶段，旨在帮助用户进行复杂搜索、调取已访问页面的信息，并根据当前活动的浏览器标签页获取数据。

此次合作聚焦于四大核心支柱：

*   **开放分发：** 推动开源 AI 成为封闭、专有系统的可行且透明的替代方案。
*   **文化本土化：** 针对地区语言、方言和文化背景对模型进行微调，确保 AI 能够理解当地的细微差别，而非提供“千篇一律”的体验。
*   **隐私与控制：** 秉持 Mozilla 隐私至上的标准。默认情况下，对话不会保存在 Mozilla 的服务器上，且 Mistral 已承诺执行零数据保留政策。
*   **主权 AI：** 将企业级、高掌控的技术延伸至普通消费者，确保用户对自己的浏览体验拥有自主权。

该集成功能将率先面向**法国和北美**用户推出，并预计于 2026 年晚些时候在**英国和德国**上线。

Mozilla 首席执行官 Anthony Enzor-DeMeo 和 Mistral 首席执行官 Arthur Mensch 强调，此次合作旨在防止互联网变成由少数几家主导科技公司控制的“单向漏斗”。通过优先考虑选择权和开放技术，他们力求在提供原生于浏览器的私密、多语言 AI 体验的同时，维护互联网探索与发现的核心价值。

---

## 8. Tell the speakers that you liked their talks

**原文标题**: Tell the speakers that you liked their talks

**原文链接**: [https://ohhelloana.blog/tell-the-speakers/](https://ohhelloana.blog/tell-the-speakers/)

在这篇文章中，Ana Rodrigues 反思了她在 SmashingConf 和 CSS Day 等会议上的近期经历，强调了参会者向演讲者提供反馈的需求正日益增长。

Rodrigues 观察到“演讲圈”已经发生了变化，并指出 Twitter 等平台的衰落造成了反馈真空。由于失去了演讲者曾经依赖的即时在线评论浪潮，许多人陷入了自我怀疑，纳闷自己的演讲是引起了共鸣，还是反应平平。她坦诚地分享道，尽管她有担任主持人和演讲者的丰富经验，但她仍会受到冒名顶替综合征、害羞以及演讲后对表现产生的焦虑所困扰。

为了弥补这一鸿沟，Rodrigues 描述了她如何积极促成“吃豆人式”的小组对话，帮助害羞的参会者克服在接触演讲者时的畏缩心理。她强调，演讲者也“只是普通人”，他们感受到的紧张情绪往往不亚于那些想与他们交谈的观众。

文章最后向参会者发出了直接呼吁：**如果你喜欢他们的演讲，请告诉演讲者。** 无论是当面的一句简单赞美，还是网络上的一条发布，这种反馈都至关重要。它肯定了准备演讲所付出的巨大努力，并为那些往往对自己最为苛刻的演讲者提供了急需的宽慰。

---

## 9. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 10. The Siberian Ice Maiden and the Scythian World

**原文标题**: The Siberian Ice Maiden and the Scythian World

**原文链接**: [https://patrickwyman.substack.com/p/the-siberian-ice-maiden-and-the-scythian](https://patrickwyman.substack.com/p/the-siberian-ice-maiden-and-the-scythian)

生成摘要时出错

---

## 11. Learning Programming in an Age of LLMs

**原文标题**: Learning Programming in an Age of LLMs

**原文链接**: [https://blog.ploeh.dk/2026/09/16/on-learning-programming-in-an-age-of-llms/](https://blog.ploeh.dk/2026/09/16/on-learning-programming-in-an-age-of-llms/)

生成摘要时出错

---

## 12. How big are factorials?

**原文标题**: How big are factorials?

**原文链接**: [https://eli.thegreenplace.net/2026/how-big-are-factorials/](https://eli.thegreenplace.net/2026/how-big-are-factorials/)

生成摘要时出错

---

## 13. GitHub is having trouble counting things

**原文标题**: GitHub is having trouble counting things

**原文链接**: [https://chuckgreenman.com/2026/09/16/counting-at-github](https://chuckgreenman.com/2026/09/16/counting-at-github)

生成摘要时出错

---

## 14. Claude Cowork and chat are now one Claude

**原文标题**: Claude Cowork and chat are now one Claude

**原文链接**: [https://claude.com/blog/cowork-is-now-claude](https://claude.com/blog/cowork-is-now-claude)

生成摘要时出错

---

## 15. The DeepMind Institute

**原文标题**: The DeepMind Institute

**原文链接**: [https://institute.deepmind.com/](https://institute.deepmind.com/)

生成摘要时出错

---

## 16. A coffee shop owner used AI to make a menu poster. Then came the angry DMs

**原文标题**: A coffee shop owner used AI to make a menu poster. Then came the angry DMs

**原文链接**: [https://www.businessinsider.com/coffee-shop-owner-ai-menu-backlash-2026-9](https://www.businessinsider.com/coffee-shop-owner-ai-menu-backlash-2026-9)

生成摘要时出错

---

## 17. Hackers Got Inside a Flock Camera

**原文标题**: Hackers Got Inside a Flock Camera

**原文链接**: [https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)

生成摘要时出错

---

## 18. The Google Play app review process now regularly takes longer than a week

**原文标题**: The Google Play app review process now regularly takes longer than a week

**原文链接**: [https://gultsch.social/@daniel/117280438824908947](https://gultsch.social/@daniel/117280438824908947)

生成摘要时出错

---

## 19. ER visits for gambling disorders doubled after expanded online gambling market

**原文标题**: ER visits for gambling disorders doubled after expanded online gambling market

**原文链接**: [https://temertymedicine.utoronto.ca/news/emergency-room-visits-gambling-disorders-nearly-doubled-after-expanded-online-gambling-market](https://temertymedicine.utoronto.ca/news/emergency-room-visits-gambling-disorders-nearly-doubled-after-expanded-online-gambling-market)

生成摘要时出错

---

## 20. How good are frontier models at physics?

**原文标题**: How good are frontier models at physics?

**原文链接**: [https://arxiv.org/abs/2609.13009](https://arxiv.org/abs/2609.13009)

生成摘要时出错

---

## 21. Kyber (YC W23) Is Hiring a Forward Deployed Engineer

**原文标题**: Kyber (YC W23) Is Hiring a Forward Deployed Engineer

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/eturrAR-forward-deployed-engineer](https://www.ycombinator.com/companies/kyber/jobs/eturrAR-forward-deployed-engineer)

生成摘要时出错

---

## 22. Can we stop with the uptime percentages?

**原文标题**: Can we stop with the uptime percentages?

**原文链接**: [https://blog.jim-nielsen.com/2026/stop-with-the-uptime-percentage/](https://blog.jim-nielsen.com/2026/stop-with-the-uptime-percentage/)

生成摘要时出错

---

## 23. Show HN: How Stale Is Your AI? Release age and training cutoff for 20 models

**原文标题**: Show HN: How Stale Is Your AI? Release age and training cutoff for 20 models

**原文链接**: [https://stale.jock.pl/](https://stale.jock.pl/)

生成摘要时出错

---

## 24. Why a fast-growing German AI startup is moving its parent company from the US

**原文标题**: Why a fast-growing German AI startup is moving its parent company from the US

**原文链接**: [https://www.euronews.com/business/2026/09/16/why-this-fast-growing-german-ai-start-up-is-moving-its-parent-company-from-the-us](https://www.euronews.com/business/2026/09/16/why-this-fast-growing-german-ai-start-up-is-moving-its-parent-company-from-the-us)

生成摘要时出错

---

## 25. Salesforce Global Outage

**原文标题**: Salesforce Global Outage

**原文链接**: [https://status.salesforce.com/products/all](https://status.salesforce.com/products/all)

生成摘要时出错

---

## 26. This Code Is CRAP (2011)

**原文标题**: This Code Is CRAP (2011)

**原文链接**: [https://testing.googleblog.com/2011/02/this-code-is-crap.html](https://testing.googleblog.com/2011/02/this-code-is-crap.html)

生成摘要时出错

---

## 27. Anatomy of a Texture

**原文标题**: Anatomy of a Texture

**原文链接**: [https://agentlien.github.io/texture/](https://agentlien.github.io/texture/)

生成摘要时出错

---

## 28. Show HN: I made a flight simulator, except you're just a passenger

**原文标题**: Show HN: I made a flight simulator, except you're just a passenger

**原文链接**: [https://inflightsimulator.com](https://inflightsimulator.com)

生成摘要时出错

---

## 29. Scaling Golang CI by Replacing actions/setup-go

**原文标题**: Scaling Golang CI by Replacing actions/setup-go

**原文链接**: [https://www.cloudx.ai/posts/setup-go](https://www.cloudx.ai/posts/setup-go)

生成摘要时出错

---

## 30. A warning about 'model welfare'

**原文标题**: A warning about 'model welfare'

**原文链接**: [https://mustafa-suleyman.ai/a-warning-about-model-welfare](https://mustafa-suleyman.ai/a-warning-about-model-welfare)

生成摘要时出错

---

## 31. Original Sony PlayStation 2 security chip 'broken wide open' after 26 years

**原文标题**: Original Sony PlayStation 2 security chip 'broken wide open' after 26 years

**原文链接**: [https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip](https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip)

生成摘要时出错

---

## 32. Introducing System One Models and Jev

**原文标题**: Introducing System One Models and Jev

**原文链接**: [https://typesafe.ai/blog/introducing-system-one-models-and-jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

生成摘要时出错

---

## 33. Why I'm still bearish on LLMs after Navier-Stokes

**原文标题**: Why I'm still bearish on LLMs after Navier-Stokes

**原文链接**: [https://dank.systems/posts/2026-09-15-ai-bear.html](https://dank.systems/posts/2026-09-15-ai-bear.html)

生成摘要时出错

---

## 34. Doing Everyone Else's Job

**原文标题**: Doing Everyone Else's Job

**原文链接**: [https://yosefk.com/blog/doing-everyone-elses-job.html](https://yosefk.com/blog/doing-everyone-elses-job.html)

生成摘要时出错

---

## 35. Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

**原文标题**: Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

**原文链接**: [https://arxiv.org/abs/2511.07885](https://arxiv.org/abs/2511.07885)

生成摘要时出错

---

## 36. Fed Raises Rates for First Time in Three Years

**原文标题**: Fed Raises Rates for First Time in Three Years

**原文链接**: [https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe](https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe)

生成摘要时出错

---

## 37. German Rheinmetall open-sources its Battlesuite connected weapon system protcol

**原文标题**: German Rheinmetall open-sources its Battlesuite connected weapon system protcol

**原文链接**: [https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html)

生成摘要时出错

---

## 38. Apple Reference Image: A New Approach for Verified Photography

**原文标题**: Apple Reference Image: A New Approach for Verified Photography

**原文链接**: [https://security.apple.com/blog/apple-reference-image/](https://security.apple.com/blog/apple-reference-image/)

生成摘要时出错

---

## 39. I sent Google proof of a bot farm. They called it "normal user behavior."

**原文标题**: I sent Google proof of a bot farm. They called it "normal user behavior."

**原文链接**: [https://dayzlegame.com/blog/google-ads-normal-user-behavior/](https://dayzlegame.com/blog/google-ads-normal-user-behavior/)

生成摘要时出错

---

## 40. Recreating Voodoo Graphics and a Late-1990s Gaming PC on an FPGA

**原文标题**: Recreating Voodoo Graphics and a Late-1990s Gaming PC on an FPGA

**原文链接**: [https://nand2mario.github.io/posts/2026/zsst-voodoo/](https://nand2mario.github.io/posts/2026/zsst-voodoo/)

生成摘要时出错

---

## 41. DeepSeek v4.1 Flash Is Now Our Best Hacking Model

**原文标题**: DeepSeek v4.1 Flash Is Now Our Best Hacking Model

**原文链接**: [https://enclave.ai/blog/deepseek-v41-flash-is-now-our-best-hacking-model](https://enclave.ai/blog/deepseek-v41-flash-is-now-our-best-hacking-model)

生成摘要时出错

---

## 42. Measuring Gauss-Seidel loop-carried dependency and fixing it via loop unrolling

**原文标题**: Measuring Gauss-Seidel loop-carried dependency and fixing it via loop unrolling

**原文链接**: [https://loiseaujc.github.io/posts/blog-title/make_gauss_seidel_great_again.html](https://loiseaujc.github.io/posts/blog-title/make_gauss_seidel_great_again.html)

生成摘要时出错

---

## 43. We got admin access to Baseten's production GitHub

**原文标题**: We got admin access to Baseten's production GitHub

**原文链接**: [https://www.strix.ai/blog/baseten-harbor-github-pat-takeover](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover)

生成摘要时出错

---

## 44. A software thing I built: GPS on a 25MHz 486-SX

**原文标题**: A software thing I built: GPS on a 25MHz 486-SX

**原文链接**: [https://forum.vcfed.org/index.php?threads/a-software-thing-i-built-gps-on-a-25mhz-486-sx.1258966/](https://forum.vcfed.org/index.php?threads/a-software-thing-i-built-gps-on-a-25mhz-486-sx.1258966/)

生成摘要时出错

---

## 45. Building a Linux GPU Driver for the M4 Mac Mini in One Month

**原文标题**: Building a Linux GPU Driver for the M4 Mac Mini in One Month

**原文链接**: [https://codyho.dev/blog/gpu-driver/](https://codyho.dev/blog/gpu-driver/)

生成摘要时出错

---

## 46. We do modern frequentist statistics: Using fake-data simulation

**原文标题**: We do modern frequentist statistics: Using fake-data simulation

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/09/14/this-is-modern-frequentist-statistics-using-fake-data-simulation-to-understand/](https://statmodeling.stat.columbia.edu/2026/09/14/this-is-modern-frequentist-statistics-using-fake-data-simulation-to-understand/)

生成摘要时出错

---

## 47. Negativland, Culture Jamming, and the Art of Making Something New

**原文标题**: Negativland, Culture Jamming, and the Art of Making Something New

**原文链接**: [https://blog.archive.org/2026/09/11/negativland-culture-jamming-and-the-art-of-making-something-new/](https://blog.archive.org/2026/09/11/negativland-culture-jamming-and-the-art-of-making-something-new/)

生成摘要时出错

---

## 48. Flock (YC S17) dumped by Boston for sharing data in violation of contract

**原文标题**: Flock (YC S17) dumped by Boston for sharing data in violation of contract

**原文链接**: [https://arstechnica.com/tech-policy/2026/09/boston-dumps-flock-says-it-shared-data-nationwide-in-violation-of-contract/](https://arstechnica.com/tech-policy/2026/09/boston-dumps-flock-says-it-shared-data-nationwide-in-violation-of-contract/)

生成摘要时出错

---

## 49. Column built an issuer processor from scratch

**原文标题**: Column built an issuer processor from scratch

**原文链接**: [https://column.com/card-issuing/](https://column.com/card-issuing/)

生成摘要时出错

---

## 50. Saving Jet Fuel

**原文标题**: Saving Jet Fuel

**原文链接**: [https://tech.marksblogg.com/scikit-decide-openap-optimal-flight-planning.html](https://tech.marksblogg.com/scikit-decide-openap-optimal-flight-planning.html)

生成摘要时出错

---

## 51. An update on Wayback Machine access

**原文标题**: An update on Wayback Machine access

**原文链接**: [https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/)

生成摘要时出错

---

## 52. Chopping up books when they're physically too big

**原文标题**: Chopping up books when they're physically too big

**原文链接**: [https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html](https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html)

生成摘要时出错

---

## 53. OpenAI expands ChatGPT ads with Sponsored Agents

**原文标题**: OpenAI expands ChatGPT ads with Sponsored Agents

**原文链接**: [https://openai.com/index/reimagining-advertising-with-ai/](https://openai.com/index/reimagining-advertising-with-ai/)

生成摘要时出错

---

## 54. 4chan/Kiwifarms lawsuit against OFCOM dismissed for lack of jurisdiction

**原文标题**: 4chan/Kiwifarms lawsuit against OFCOM dismissed for lack of jurisdiction

**原文链接**: [https://prestonbyrne.com/2026/09/15/4chan_ofcom_mtd/](https://prestonbyrne.com/2026/09/15/4chan_ofcom_mtd/)

On September 15, 2026, the U.S. District Court for the District of Columbia dismissed a lawsuit filed by 4chan and Lolcow, LLC (Kiwifarms) against the United Kingdom’s Office of Communications (Ofcom). The court ruled that Ofcom, as an arm of a foreign state, is immune from U.S. jurisdiction under the Foreign Sovereign Immunities Act (FSIA).

The lawsuit challenged Ofcom’s attempts to impose fines and regulatory orders on American websites for speech protected by the First Amendment. While the court did not rule on the merits of the constitutional claims, it observed that U.S. courts generally decline to enforce foreign judgments that violate the Constitution or are "penal" in nature. 

Legal counsel for the plaintiffs, Byrne & Storm, P.C., argued that Ofcom used sovereign immunity to avoid defending the legality of its actions. The firm highlighted a troubling "chilling effect," noting that of 197 orders Ofcom sent to U.S. targets between 2025 and 2026, 98% resulted in compliance. They contend the ruling creates a loophole where foreign regulators can threaten Americans on American soil without any judicial oversight.

To address this, the firm is calling on Congress to pass the **GRANITE Act** and the **HOMEFRONT Act**. These bills seek to strip foreign sovereign immunity in cases of extraterritorial censorship and prevent U.S. courts from recognizing foreign speech-related judgments. Similar "shield laws" are also being pursued at the state level in Wyoming and New Hampshire. 

The plaintiffs maintain that Ofcom will never be able to collect its fines in the U.S. and are currently considering an appeal to ensure American citizens have a proactive legal remedy against foreign regulatory overreach.

---

## 55. Backflip: Apple now wants to train AI models with user data after all

**原文标题**: Backflip: Apple now wants to train AI models with user data after all

**原文链接**: [https://www.heise.de/en/news/Backflip-Apple-now-wants-to-train-AI-models-with-user-data-after-all-11451252.html](https://www.heise.de/en/news/Backflip-Apple-now-wants-to-train-AI-models-with-user-data-after-all-11451252.html)

生成摘要时出错

---

## 56. The Beauty of Roundabouts

**原文标题**: The Beauty of Roundabouts

**原文链接**: [https://gruhn.me/blog/2026-09-14/](https://gruhn.me/blog/2026-09-14/)

生成摘要时出错

---

## 57. Gemini 3.8 Live and 3.8 Live Extended Thinking

**原文标题**: Gemini 3.8 Live and 3.8 Live Extended Thinking

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)

生成摘要时出错

---

## 58. Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue

**原文标题**: Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue

**原文链接**: [https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/](https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/)

生成摘要时出错

---

## 59. Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part

**原文标题**: Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part

**原文链接**: [https://manybot.org](https://manybot.org)

生成摘要时出错

---

## 60. WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages

**原文标题**: WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages

**原文链接**: [https://github.com/GraafHenk/numberwang](https://github.com/GraafHenk/numberwang)

生成摘要时出错

---

## 61. 52 Factorial

**原文标题**: 52 Factorial

**原文链接**: [https://czep.net/weblog/52cards.html](https://czep.net/weblog/52cards.html)

生成摘要时出错

---

## 62. Jean-Pierre Serre turns 100

**原文标题**: Jean-Pierre Serre turns 100

**原文链接**: [https://mathshistory.st-andrews.ac.uk/Biographies/Serre/](https://mathshistory.st-andrews.ac.uk/Biographies/Serre/)

生成摘要时出错

---

## 63. UK mathematician debunks myth around Parthenon's optical illusions

**原文标题**: UK mathematician debunks myth around Parthenon's optical illusions

**原文链接**: [https://www.theguardian.com/science/2026/sep/16/uk-mathematician-debunks-myth-parthenon-optical-illusions](https://www.theguardian.com/science/2026/sep/16/uk-mathematician-debunks-myth-parthenon-optical-illusions)

生成摘要时出错

---

## 64. Learning to solve hard problems in RL for LLMs by never giving up

**原文标题**: Learning to solve hard problems in RL for LLMs by never giving up

**原文链接**: [https://mnoukhov.github.io/posts/ngu/](https://mnoukhov.github.io/posts/ngu/)

生成摘要时出错

---

## 65. NSF memo implementing Trump's 'golden age' of science unsettles researchers

**原文标题**: NSF memo implementing Trump's 'golden age' of science unsettles researchers

**原文链接**: [https://www.science.org/content/article/nsf-memo-implementing-trump-s-golden-age-science-unsettles-researchers](https://www.science.org/content/article/nsf-memo-implementing-trump-s-golden-age-science-unsettles-researchers)

生成摘要时出错

---

## 66. I can't stop thinking about Papua New Guinea

**原文标题**: I can't stop thinking about Papua New Guinea

**原文链接**: [https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua](https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua)

生成摘要时出错

---

## 67. China's Ubtech Opens Plant Making a Humanoid Robot Every 10 Minutes

**原文标题**: China's Ubtech Opens Plant Making a Humanoid Robot Every 10 Minutes

**原文链接**: [https://en.sedaily.com/international/2026/09/16/chinas-ubtech-opens-plant-making-a-humanoid-robot-every-10](https://en.sedaily.com/international/2026/09/16/chinas-ubtech-opens-plant-making-a-humanoid-robot-every-10)

生成摘要时出错

---

## 68. Is GitHub a social network that endangers children? Australia wants to know

**原文标题**: Is GitHub a social network that endangers children? Australia wants to know

**原文链接**: [https://www.theregister.com/offbeat/2025/09/25/australia-asks-github-if-its-a-dangerous-social-network/509016](https://www.theregister.com/offbeat/2025/09/25/australia-asks-github-if-its-a-dangerous-social-network/509016)

生成摘要时出错

---

## 69. Better routing, probe fixes, plugin updates in Freenet/Hyphanet 0.7.5 build 1507

**原文标题**: Better routing, probe fixes, plugin updates in Freenet/Hyphanet 0.7.5 build 1507

**原文链接**: [https://www.hyphanet.org/freenet-hyphanet-075-build-1507-fix-probe-routing-plugins-and-upkeep.html](https://www.hyphanet.org/freenet-hyphanet-075-build-1507-fix-probe-routing-plugins-and-upkeep.html)

生成摘要时出错

---

## 70. The Inference Hardware Revolution of 2026

**原文标题**: The Inference Hardware Revolution of 2026

**原文链接**: [https://spectrum.ieee.org/inference-hardware-revolution](https://spectrum.ieee.org/inference-hardware-revolution)

生成摘要时出错

---

## 71. 25 years of mass surveillance is enough

**原文标题**: 25 years of mass surveillance is enough

**原文链接**: [https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html)

生成摘要时出错

---

## 72. Douglas Adams and the exterminated Doctor Who adventure

**原文标题**: Douglas Adams and the exterminated Doctor Who adventure

**原文链接**: [https://www.bbc.co.uk/news/articles/c8jdp38z4jgo](https://www.bbc.co.uk/news/articles/c8jdp38z4jgo)

生成摘要时出错

---

## 73. A single firm is behind OpenAI, Anthropic, and Meta hacking scandals

**原文标题**: A single firm is behind OpenAI, Anthropic, and Meta hacking scandals

**原文链接**: [https://www.effort.news/irregular](https://www.effort.news/irregular)

生成摘要时出错

---

## 74. Show HN: Hacking a $20 4G wireless hotspot into a texting device

**原文标题**: Show HN: Hacking a $20 4G wireless hotspot into a texting device

**原文链接**: [https://bkovac.github.io/modem-thing/](https://bkovac.github.io/modem-thing/)

生成摘要时出错

---

## 75. An interactive world map of the stories cultures have told

**原文标题**: An interactive world map of the stories cultures have told

**原文链接**: [https://originmap.sunnyguha.com/](https://originmap.sunnyguha.com/)

生成摘要时出错

---

## 76. CSS-Tricks in Limbo

**原文标题**: CSS-Tricks in Limbo

**原文链接**: [https://vale.rocks/micros/20260915-0135](https://vale.rocks/micros/20260915-0135)

生成摘要时出错

---

## 77. Datamimic – don't let your coding agent invent its own test world

**原文标题**: Datamimic – don't let your coding agent invent its own test world

**原文链接**: [https://github.com/rapiddweller/datamimic](https://github.com/rapiddweller/datamimic)

生成摘要时出错

---

## 78. Alternatives to MinIO for single-node local S3

**原文标题**: Alternatives to MinIO for single-node local S3

**原文链接**: [https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/](https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/)

生成摘要时出错

---

## 79. Let's make quality the norm again

**原文标题**: Let's make quality the norm again

**原文链接**: [https://www.forbrukerradet.no/short-life/](https://www.forbrukerradet.no/short-life/)

生成摘要时出错

---

## 80. How the Meta Settlement Silences Youth Activism

**原文标题**: How the Meta Settlement Silences Youth Activism

**原文链接**: [https://www.eff.org/deeplinks/2026/09/meta-settlement-yet-another-example-online-youth-organizing-under-threat](https://www.eff.org/deeplinks/2026/09/meta-settlement-yet-another-example-online-youth-organizing-under-threat)

生成摘要时出错

---

## 81. Sierra digital cameras on the Apple II

**原文标题**: Sierra digital cameras on the Apple II

**原文链接**: [https://www.colino.net/wordpress/archives/2026/09/11/sierra-digital-cameras-on-the-apple-ii/](https://www.colino.net/wordpress/archives/2026/09/11/sierra-digital-cameras-on-the-apple-ii/)

生成摘要时出错

---

## 82. We know what a world without work looks like

**原文标题**: We know what a world without work looks like

**原文链接**: [https://asteriskmag.substack.com/p/we-already-know-what-a-world-without](https://asteriskmag.substack.com/p/we-already-know-what-a-world-without)

生成摘要时出错

---

## 83. Cartesian – AI 3D Modeling for Design

**原文标题**: Cartesian – AI 3D Modeling for Design

**原文链接**: [https://www.formas.ai/cartesian](https://www.formas.ai/cartesian)

生成摘要时出错

---

## 84. MartyPC – A Cycle-Accurate IBM PC/XT Emulator

**原文标题**: MartyPC – A Cycle-Accurate IBM PC/XT Emulator

**原文链接**: [https://github.com/dbalsom/martypc](https://github.com/dbalsom/martypc)

生成摘要时出错

---

## 85. Stay discoverable in search while disallowing AI training

**原文标题**: Stay discoverable in search while disallowing AI training

**原文链接**: [https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)

生成摘要时出错

---

## 86. PS5 Linux lead quits: "a bunch of noobs using LLMs" that "they don't understand"

**原文标题**: PS5 Linux lead quits: "a bunch of noobs using LLMs" that "they don't understand"

**原文链接**: [https://frvr.com/blog/news/ps5-linux-lead-quits-as-open-source-projects-have-become-a-bunch-of-noobs-using-llms-that-they-dont-even-understand/](https://frvr.com/blog/news/ps5-linux-lead-quits-as-open-source-projects-have-become-a-bunch-of-noobs-using-llms-that-they-dont-even-understand/)

生成摘要时出错

---

## 87. Show HN: Capsule – Single-file web apps that save their data into SQLite

**原文标题**: Show HN: Capsule – Single-file web apps that save their data into SQLite

**原文链接**: [https://withcapsule.app/](https://withcapsule.app/)

生成摘要时出错

---

## 88. OpenArm: An open-source 7DOF humanoid arm

**原文标题**: OpenArm: An open-source 7DOF humanoid arm

**原文链接**: [https://github.com/enactic/OpenArm](https://github.com/enactic/OpenArm)

生成摘要时出错

---

## 89. Potemkin Village

**原文标题**: Potemkin Village

**原文链接**: [https://en.wikipedia.org/wiki/Potemkin_village](https://en.wikipedia.org/wiki/Potemkin_village)

生成摘要时出错

---

## 90. We know what a world without work looks like

**原文标题**: We know what a world without work looks like

**原文链接**: [https://asteriskmag.substack.com/p/we-already-know-what-a-world-without](https://asteriskmag.substack.com/p/we-already-know-what-a-world-without)

生成摘要时出错

---

## 91. Ubuntu 26.10 completes transition to Rust-based coreutils

**原文标题**: Ubuntu 26.10 completes transition to Rust-based coreutils

**原文链接**: [https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete](https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete)

生成摘要时出错

---

## 92. Giving up on smart rings

**原文标题**: Giving up on smart rings

**原文链接**: [https://notesbylex.com/giving-up-on-smart-rings](https://notesbylex.com/giving-up-on-smart-rings)

生成摘要时出错

---

## 93. The CSS Zen Garden dream, finally shipped

**原文标题**: The CSS Zen Garden dream, finally shipped

**原文链接**: [https://josprague.com/blog/the-css-zen-garden-dream-finally-shipped/](https://josprague.com/blog/the-css-zen-garden-dream-finally-shipped/)

生成摘要时出错

---

## 94. Java 27

**原文标题**: Java 27

**原文链接**: [https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/](https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/)

生成摘要时出错

---

## 95. Most people prefer traditional architecture

**原文标题**: Most people prefer traditional architecture

**原文链接**: [https://www.worksinprogress.news/p/do-people-prefer-traditional-architecture](https://www.worksinprogress.news/p/do-people-prefer-traditional-architecture)

生成摘要时出错

---

## 96. Show HN: Pizza Bot – An inbox for AI agents that work in the background

**原文标题**: Show HN: Pizza Bot – An inbox for AI agents that work in the background

**原文链接**: [https://github.com/pizza-bot-app/pizza-bot](https://github.com/pizza-bot-app/pizza-bot)

生成摘要时出错

---

## 97. GEFS on OpenBSD: A Early Preview

**原文标题**: GEFS on OpenBSD: A Early Preview

**原文链接**: [https://marc.info/?l=openbsd-tech&m=178948744271633&w=2](https://marc.info/?l=openbsd-tech&m=178948744271633&w=2)

生成摘要时出错

---

## 98. Suspected sabotage causes major Netherlands rail disruption

**原文标题**: Suspected sabotage causes major Netherlands rail disruption

**原文链接**: [https://www.bbc.com/news/articles/c8ly49w9g1edo](https://www.bbc.com/news/articles/c8ly49w9g1edo)

生成摘要时出错

---

## 99. Over 12% of links posted to Hacker News are Show HN projects now

**原文标题**: Over 12% of links posted to Hacker News are Show HN projects now

**原文链接**: [https://www.orangecrumbs.com/stories/show-hn](https://www.orangecrumbs.com/stories/show-hn)

生成摘要时出错

---

## 100. Fed approves interest rate hike, signals one more to come this year

**原文标题**: Fed approves interest rate hike, signals one more to come this year

**原文链接**: [https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html)

生成摘要时出错

---

