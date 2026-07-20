# Hacker News 热门文章摘要 (2026-07-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 中国的 AI 开源权重战略正在胜出

**原文标题**: China's open-weights AI strategy is winning

**原文链接**: [https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

本文认为，中国正通过采用“权重开放”（open-weights）战略，成功挑战美国在人工智能领域的主导地位。相比 OpenAI 和 Anthropic 等美国领军企业依靠封闭的专有模型获取利润，中国企业则通过发布便携、无需许可的模型来培育全球生态系统。

核心观点包括：

*   **护城河问题：** AI 模型本身几乎没有竞争“护城河”，因为它们极易被替代。真正的价值在于企业服务和基础设施。通过开放权重，中国将美国公司试图获利的层级变成了通用商品。
*   **化劣势为优势：** 美国对 GPU 的出口管制和数据法规阻碍了中国提供中心化的全球云服务。作为应对，中国转向了开放分发模式，使其技术能够无门槛地集成到全球制造业和研究领域。
*   **缩小差距：** 阿里巴巴和月之暗面（Moonshot）等中国公司的模型，目前正以更低的成本与美国前沿模型的性能平起平坐。报告显示，绝大多数 AI 初创公司已经在使用中国模型。
*   **战略讽刺：** 尽管中国常被视为“封闭”社会，但其对开源理念的利用比美国更有效。目前，美国公司受激励机制影响，倾向于通过封闭系统追求短期利润，作者认为这在长期战略上注定会失败。

作者总结指出，美国的领先优势正在迅速缩小。为了保持竞争力和保护国家利益，美国必须转变战略，从单纯的限制性措施转向支持开放、具有公益性质的 AI 基础设施。

---

## 2. 黑客抹除罗马尼亚土地登记数据库

**原文标题**: Hacker wipes Romania's land registry database

**原文链接**: [https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/)

生成摘要时出错

---

## 3. 超过30%的ArXiv新提交论文读起来像是AI写的

**原文标题**: Over 30% of new ArXiv submissions now read as AI-written

**原文链接**: [https://unslop.run/blog/measuring-ai-writing-on-arxiv](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

一项针对 12,750 篇 arXiv 论文的研究显示，目前超过 30% 的新提交论文似乎是由机器撰写的。研究人员使用了一个误报率校准为 0.4% 的检测器（以 ChatGPT 问世前即 2021–2022 年的论文作为对照组），发现类 AI 文风在 2023 年后急剧上升，到 2026 年中期已达到约 32%。

AI 生成内容的普及程度在不同学科间存在显著差异：
*   **计算机科学：** 采用率最高，达 65%。
*   **定量生物学：** 56.3%。
*   **电气工程：** 51.3%。
*   **数学：** 最低，仅为 0.7%。

研究人员分析了正文全文而非仅看摘要，并指出摘要往往会掩盖 AI 的存在。他们强调了几个关键局限性：
1.  **下限值：** 报告的百分比可能是实际采用率的下限，因为检测器可能无法识别所有的生成模型或提示词。
2.  **学科盲点：** 数学领域接近于零的比例可能是由于“检测器盲点”造成的，因为该学科包含大量符号文本和定理证明结构，这与检测工具训练时所用的科学英语显著不同。
3.  **风格 vs. 署名：** “标记”仅表示文本读起来像是机器撰写的；它无法区分是整篇文档全由 AI 生成，还是仅经过了深度的 AI 辅助润色。

该研究得出结论，类机器写作风格的兴起是学术生产方式的真实转变，而非检测工具的误差，被标记论文的比例在 2026 年初达到了近 39% 的峰值。

---

## 4. Hyprland 0.55 宣布配置文件切换至 Lua

**原文标题**: Hyprland 0.55 announced the switch to Lua for its config files

**原文链接**: [https://hypr.land/news/update55/](https://hypr.land/news/update55/)

Hyprland 0.55 版本现已发布。作为该 Wayland 合成器的一个重要里程碑，本版本在配置架构和功能特性方面带来了重大变革。

**核心亮点：**
*   **Lua 配置：** 最显著的变化是配置文件转向 **Lua**。虽然旧的 Hyprlang 格式在未来几个版本中仍将获得支持，但建议用户尽快迁移。此次更新还引入了全新的 **Layout API**，允许用户直接在配置中定义自定义窗口布局。
*   **色彩管理与渲染：** 引入了**分屏 ICC 配置文件支持**，并将渲染器默认精度设为 **FP16**。这些改进提升了色彩准确度、HDR 处理能力以及屏幕共享性能。
*   **滚动与手势：** 默认支持对全屏窗口进行滚动。新增了原生触控板手势 (`scroll_move`)，以及针对光标的实时捏合缩放手势。
*   **视觉与功能增项：** 新增了“发光 (glow)”窗口装饰、设备标签、`confine_pointer` 窗口规则，以及多个用于窗口分组和布局操作的新调度器。
*   **破坏性变更：** 移除或重定位了部分配置选项。特别地，`dwindle:pseudotile` 和 `decoration:shadow:ignore_window` 已被移除，`misc:vfr` 则被移至 debug 分组。

这是该项目迄今为止规模最大的更新之一，涵盖了海量的代码改动与贡献者投入，并对官方 Wiki 进行了全面翻新，以适配全新的 Lua 生态系统。

---

## 5. Kimi 办公

**原文标题**: Kimi Work

**原文链接**: [https://www.kimi.com/products/kimi-work](https://www.kimi.com/products/kimi-work)

**Kimi Work** 是一款基于内置 Cron 引擎的自动化解决方案，旨在实现全天候的高效生产力。它通过在后台自动执行重复性任务，实现了“一经设置，无需干预”的工作流程，确保任务在没有人工介入的情况下精准按时运行。

核心功能包括：定时调用大语言模型（LLM）智能体以完成每日简报撰写，以及运行 Python 脚本进行大规模数据处理。通过自主处理这些操作，Kimi Work 能够全天候保持工作流的持续高效。

---

## 6. Jelly UI: Soft-body physics for native HTML form controls

**原文标题**: Jelly UI: Soft-body physics for native HTML form controls

**原文链接**: [https://jelly-ui.com/](https://jelly-ui.com/)

**Jelly UI** is a dependency-free Web Components library designed to create soft, tactile, and interactive user interfaces using soft-body physics. It bridges the gap between functional native HTML form controls and playful, physics-based animations.

The library is lightweight and developer-friendly, requiring only a single script tag to implement. It offers over 40 custom elements that integrate seamlessly into standard HTML. Key technical and design features include:

*   **Accessibility:** Built-in WCAG AA color tokens to ensure high contrast and readability.
*   **Internationalization:** Native support for right-to-left (RTL) layouts.
*   **Visual Modes:** Automatic and manual support for dark mode.
*   **Performance:** Zero external dependencies, ensuring a small footprint and fast load times.

By combining tactile physics with essential modern UI features, Jelly UI provides a unique framework for building expressive yet accessible web applications.

---

## 7. 角落并非如此：关于屏幕空间环境光遮蔽 (2012)

**原文标题**: Corners Don't Look Like That: Regarding Screenspace Ambient Occlusion (2012)

**原文链接**: [https://nothings.org/gamedev/ssao/](https://nothings.org/gamedev/ssao/)

生成摘要时出错

---

## 8. 机场模拟器

**原文标题**: Airport Simulator

**原文链接**: [https://airport.apunen.com/](https://airport.apunen.com/)

由于提供的内容仅包含标题，以下是通常与“机场模拟器”（Airport Simulator）类软件及游戏相关的通用概念和核心功能概述：

**概览**
机场模拟器属于经营模拟类游戏，玩家需要负责商业航空枢纽的设计、建设和日常运营。其主要目标是在保持财务盈利和乘客满意度的同时，建立一个高效的交通网络。

**核心功能与机制**
*   **基础设施建设：** 玩家负责建造核心设施，包括跑道、滑行道、航站楼和控制塔。合理的战略布局对于缩短飞机滑行时间和防止地面拥堵至关重要。
*   **物流与运营：** 核心玩法涉及管理复杂的起降时刻表。这包括监管各项地面服务，如飞机加油、行李搬运、餐饮供应和机舱清洁，以确保快速的过站周转。
*   **乘客体验：** 游戏高度重视“客流”管理。玩家必须优化值机柜台、安检点和登机口，同时提供座椅、餐厅和商店等配套设施，以获取额外收入。
*   **员工与资源管理：** 成功运营需要招聘和培训多元化的员工团队，包括空中交通管制员、安检人员和保洁人员。在工资成本与运营需求之间取得平衡是一项持续的挑战。
*   **危机管理：** 模拟器通常会引入随机变量，如极端天气、技术故障或安全威胁，迫使玩家实时调整策略以避免延误或事故。

**结语**
机场模拟器让玩家能够全面了解航空管理的微观与宏观层面，挑战玩家在高压环境下平衡航空公司、乘客和员工等多方需求。

---

## 9. Firefox Merges Support for Vulkan Video Decoding

**原文标题**: Firefox Merges Support for Vulkan Video Decoding

**原文链接**: [https://github.com/search](https://github.com/search)

生成摘要时出错

---

## 10. Perfection Is Not Over-Engineering

**原文标题**: Perfection Is Not Over-Engineering

**原文链接**: [https://var0.xyz/posts/perfection-is-not-over-engineering.html](https://var0.xyz/posts/perfection-is-not-over-engineering.html)

生成摘要时出错

---

## 11. We're Squandering LEDs' Potential to Save Our Night Skies

**原文标题**: We're Squandering LEDs' Potential to Save Our Night Skies

**原文链接**: [https://spectrum.ieee.org/led-light-pollution](https://spectrum.ieee.org/led-light-pollution)

生成摘要时出错

---

## 12. Nativ: Run frontier open models locally on your Mac

**原文标题**: Nativ: Run frontier open models locally on your Mac

**原文链接**: [https://blaizzy.github.io/nativ/](https://blaizzy.github.io/nativ/)

生成摘要时出错

---

## 13. The Voice of Google

**原文标题**: The Voice of Google

**原文链接**: [https://www.newyorker.com/culture/the-weekend-essay/the-voice-of-google](https://www.newyorker.com/culture/the-weekend-essay/the-voice-of-google)

生成摘要时出错

---

## 14. The drivers behind software delivery inefficiency

**原文标题**: The drivers behind software delivery inefficiency

**原文链接**: [https://dl.acm.org/doi/10.1145/3800646.3800650](https://dl.acm.org/doi/10.1145/3800646.3800650)

生成摘要时出错

---

## 15. Ziggity – A terminal UI for Git, written in Zig

**原文标题**: Ziggity – A terminal UI for Git, written in Zig

**原文链接**: [https://github.com/simoarpe/ziggity](https://github.com/simoarpe/ziggity)

生成摘要时出错

---

## 16. Cross sectioning insects in an electron microscope with a femtosecond laser [video]

**原文标题**: Cross sectioning insects in an electron microscope with a femtosecond laser [video]

**原文链接**: [https://www.youtube.com/watch?v=NwhVJ7cv9B4](https://www.youtube.com/watch?v=NwhVJ7cv9B4)

生成摘要时出错

---

## 17. Exploit brokers pay $500k for WordPress RCEs. I found one with GPT5.6 and $25

**原文标题**: Exploit brokers pay $500k for WordPress RCEs. I found one with GPT5.6 and $25

**原文链接**: [https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/)

生成摘要时出错

---

## 18. Shinjuku Station in 3D

**原文标题**: Shinjuku Station in 3D

**原文链接**: [https://satoshi7190.github.io/Shinjuku-indoor-threejs-demo/](https://satoshi7190.github.io/Shinjuku-indoor-threejs-demo/)

生成摘要时出错

---

## 19. An Empirical Study: AI Agent Rules Need Context and Layered Enforcement

**原文标题**: An Empirical Study: AI Agent Rules Need Context and Layered Enforcement

**原文链接**: [https://eunomia.dev/blog/2026/07/15/ebpf-ai-agent-policy-enforcement/](https://eunomia.dev/blog/2026/07/15/ebpf-ai-agent-policy-enforcement/)

生成摘要时出错

---

## 20. That post never existed. Stop listening to that thing

**原文标题**: That post never existed. Stop listening to that thing

**原文链接**: [https://rachelbythebay.com/w/2026/05/05/404/](https://rachelbythebay.com/w/2026/05/05/404/)

生成摘要时出错

---

## 21. Kimi K3, Qwen 3.8, and Anthropic's (Potential) Unravelling

**原文标题**: Kimi K3, Qwen 3.8, and Anthropic's (Potential) Unravelling

**原文链接**: [https://www.emergingtrajectories.com/lh/frontier-lab-economics/](https://www.emergingtrajectories.com/lh/frontier-lab-economics/)

生成摘要时出错

---

## 22. Controlling Reasoning Effort in LLMs

**原文标题**: Controlling Reasoning Effort in LLMs

**原文链接**: [https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)

生成摘要时出错

---

## 23. The EU is about to sell our most sensitive data to the US for visa-free travel

**原文标题**: The EU is about to sell our most sensitive data to the US for visa-free travel

**原文链接**: [https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/)

生成摘要时出错

---

## 24. I Stopped "Creating Content"

**原文标题**: I Stopped "Creating Content"

**原文链接**: [https://refactoringenglish.com/blog/why-i-stopped-creating-content/](https://refactoringenglish.com/blog/why-i-stopped-creating-content/)

生成摘要时出错

---

## 25. I turned my bearblog into a text based adventure

**原文标题**: I turned my bearblog into a text based adventure

**原文链接**: [https://peaceful.bearblog.dev](https://peaceful.bearblog.dev)

生成摘要时出错

---

## 26. Inertia-1: An Open Exploration to a Unified Motion Foundation Model

**原文标题**: Inertia-1: An Open Exploration to a Unified Motion Foundation Model

**原文链接**: [https://yang-ai-lab.github.io/Inertia-1/](https://yang-ai-lab.github.io/Inertia-1/)

生成摘要时出错

---

## 27. NYC Subway Signals: A Complete Guide

**原文标题**: NYC Subway Signals: A Complete Guide

**原文链接**: [https://www.nycsubway.org/wiki/Subway_Signals%3A_A_Complete_Guide](https://www.nycsubway.org/wiki/Subway_Signals%3A_A_Complete_Guide)

生成摘要时出错

---

## 28. Agent swarms and the new model economics

**原文标题**: Agent swarms and the new model economics

**原文链接**: [https://cursor.com/blog/agent-swarm-model-economics](https://cursor.com/blog/agent-swarm-model-economics)

生成摘要时出错

---

## 29. Soofi – Sovereign Open Source Foundation Models

**原文标题**: Soofi – Sovereign Open Source Foundation Models

**原文链接**: [https://www.soofi.info/](https://www.soofi.info/)

生成摘要时出错

---

## 30. Satan's 19th-Century Bank Note (2017)

**原文标题**: Satan's 19th-Century Bank Note (2017)

**原文链接**: [https://www.historytoday.com/miscellanies/satans-19th-century-bank-note](https://www.historytoday.com/miscellanies/satans-19th-century-bank-note)

生成摘要时出错

---

## 31. Show HN: Wheesper – Start an anonymous discussion with a link

**原文标题**: Show HN: Wheesper – Start an anonymous discussion with a link

**原文链接**: [https://wheesper.com/](https://wheesper.com/)

生成摘要时出错

---

## 32. What does the Riemann zeta function have to do with the distribution of primes?

**原文标题**: What does the Riemann zeta function have to do with the distribution of primes?

**原文链接**: [https://hidden-phenomena.com/articles/rh](https://hidden-phenomena.com/articles/rh)

生成摘要时出错

---

## 33. Moonshine: Lets you stream games from your PC to any device running Moonlight

**原文标题**: Moonshine: Lets you stream games from your PC to any device running Moonlight

**原文链接**: [https://github.com/hgaiser/moonshine](https://github.com/hgaiser/moonshine)

生成摘要时出错

---

## 34. Annoying and alarming things about OpenCode

**原文标题**: Annoying and alarming things about OpenCode

**原文链接**: [https://wren.wtf/shower-thoughts/stop-using-opencode/](https://wren.wtf/shower-thoughts/stop-using-opencode/)

生成摘要时出错

---

## 35. Sealed tomb filled with paintings and inscriptions discovered in Egypt

**原文标题**: Sealed tomb filled with paintings and inscriptions discovered in Egypt

**原文链接**: [https://www.labrujulaverde.com/en/2026/07/sealed-tomb-of-a-high-official-or-priest-filled-with-paintings-and-inscriptions-discovered-on-luxors-west-bank/](https://www.labrujulaverde.com/en/2026/07/sealed-tomb-of-a-high-official-or-priest-filled-with-paintings-and-inscriptions-discovered-on-luxors-west-bank/)

生成摘要时出错

---

## 36. Czechia moves to ban mobile phones in schools from September 2027

**原文标题**: Czechia moves to ban mobile phones in schools from September 2027

**原文链接**: [https://www.expats.cz/czech-news/article/czech-news-in-brief-for-july-20-2026-monday-top-afternoon-headlines](https://www.expats.cz/czech-news/article/czech-news-in-brief-for-july-20-2026-monday-top-afternoon-headlines)

生成摘要时出错

---

## 37. Sensing warm and cool: how the body detects temperature changes

**原文标题**: Sensing warm and cool: how the body detects temperature changes

**原文链接**: [https://news.uq.edu.au/2026-07-sensing-warm-and-cool-how-body-detects-temperature-changes](https://news.uq.edu.au/2026-07-sensing-warm-and-cool-how-body-detects-temperature-changes)

生成摘要时出错

---

## 38. We rewrote our custom visualisation renderers from SVG to be in Canvas

**原文标题**: We rewrote our custom visualisation renderers from SVG to be in Canvas

**原文链接**: [https://www.polarsignals.com/blog/posts/2026/07/14/new-and-faster-profiler](https://www.polarsignals.com/blog/posts/2026/07/14/new-and-faster-profiler)

生成摘要时出错

---

## 39. There are no lossless transformations of natural-language text

**原文标题**: There are no lossless transformations of natural-language text

**原文链接**: [https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text](https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text)

生成摘要时出错

---

## 40. ECC and DDR5

**原文标题**: ECC and DDR5

**原文链接**: [https://etbe.coker.com.au/2026/07/19/ecc-ddr5/](https://etbe.coker.com.au/2026/07/19/ecc-ddr5/)

生成摘要时出错

---

## 41. Inhaling high-dose CO2 clears Alzheimer's proteins from the brain

**原文标题**: Inhaling high-dose CO2 clears Alzheimer's proteins from the brain

**原文链接**: [https://www.newscientist.com/article/2580471-inhaling-high-dose-co2-clears-alzheimers-proteins-from-the-brain/](https://www.newscientist.com/article/2580471-inhaling-high-dose-co2-clears-alzheimers-proteins-from-the-brain/)

生成摘要时出错

---

## 42. The footprints of every building in NYC – updated weekly

**原文标题**: The footprints of every building in NYC – updated weekly

**原文链接**: [https://www.beautifulpublicdata.com/the-footprints-of-every-building-in-nyc/](https://www.beautifulpublicdata.com/the-footprints-of-every-building-in-nyc/)

生成摘要时出错

---

## 43. The ACLU Is Arming Lawyers to Expose State Surveillance Secrets

**原文标题**: The ACLU Is Arming Lawyers to Expose State Surveillance Secrets

**原文链接**: [https://www.wired.com/story/the-aclu-is-arming-lawyers-to-expose-state-surveillance-secrets/](https://www.wired.com/story/the-aclu-is-arming-lawyers-to-expose-state-surveillance-secrets/)

生成摘要时出错

---

## 44. 1-Bit LLM in the Browser

**原文标题**: 1-Bit LLM in the Browser

**原文链接**: [https://huggingface.co/spaces/webml-community/bonsai-webgpu](https://huggingface.co/spaces/webml-community/bonsai-webgpu)

生成摘要时出错

---

## 45. LoRA Speedrun – a public wall-clock leaderboard for fine-tuning techniques

**原文标题**: LoRA Speedrun – a public wall-clock leaderboard for fine-tuning techniques

**原文链接**: [https://github.com/Saivineeth147/lora-speedrun](https://github.com/Saivineeth147/lora-speedrun)

生成摘要时出错

---

## 46. Moist Towelette Museum

**原文标题**: Moist Towelette Museum

**原文链接**: [https://moisttowelettemuseum.com/](https://moisttowelettemuseum.com/)

生成摘要时出错

---

## 47. Fable is now included on Max plans (up to 50% of weekly limit)

**原文标题**: Fable is now included on Max plans (up to 50% of weekly limit)

**原文链接**: [https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)

生成摘要时出错

---

## 48. Ben Thompson is wrong: US frontier labs are right to be panicking

**原文标题**: Ben Thompson is wrong: US frontier labs are right to be panicking

**原文链接**: [https://larrysalibra.com/ben-thompson-is-wrong-us-frontier-labs-are-right-to-be-panicking/](https://larrysalibra.com/ben-thompson-is-wrong-us-frontier-labs-are-right-to-be-panicking/)

生成摘要时出错

---

## 49. Kimi K3: The open-weights escalation

**原文标题**: Kimi K3: The open-weights escalation

**原文链接**: [https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation)

生成摘要时出错

---

## 50. Model 4: Our best model yet for local dictation and cleanup on Mac

**原文标题**: Model 4: Our best model yet for local dictation and cleanup on Mac

**原文链接**: [https://www.epilude.com/news/introducing-model-4](https://www.epilude.com/news/introducing-model-4)

生成摘要时出错

---

## 51. Eliminating Go bounds checks with unsafe

**原文标题**: Eliminating Go bounds checks with unsafe

**原文链接**: [https://blog.andr2i.com/posts/2026-07-06-eliminating-go-bound-checks-with-unsafe](https://blog.andr2i.com/posts/2026-07-06-eliminating-go-bound-checks-with-unsafe)

生成摘要时出错

---

## 52. The Reverse Information Paradox (Satya Nadella)

**原文标题**: The Reverse Information Paradox (Satya Nadella)

**原文链接**: [https://snscratchpad.com/posts/reverse-information-paradox/](https://snscratchpad.com/posts/reverse-information-paradox/)

生成摘要时出错

---

## 53. Judge orders pause to Paramount-Warner Bros merger as states argue antitrust law

**原文标题**: Judge orders pause to Paramount-Warner Bros merger as states argue antitrust law

**原文链接**: [https://variety.com/2026/film/news/judge-paramount-warner-bros-merger-tro-1236815048/](https://variety.com/2026/film/news/judge-paramount-warner-bros-merger-tro-1236815048/)

生成摘要时出错

---

## 54. Caffeine and Cardiovascular Disease: AHA Scientific Statement

**原文标题**: Caffeine and Cardiovascular Disease: AHA Scientific Statement

**原文链接**: [https://www.ahajournals.org/doi/epub/10.1161/CIR.0000000000001454](https://www.ahajournals.org/doi/epub/10.1161/CIR.0000000000001454)

生成摘要时出错

---

## 55. Primate 0.40: Route pages, store enums, async schemas and events

**原文标题**: Primate 0.40: Route pages, store enums, async schemas and events

**原文链接**: [https://primate.run/blog/primate-040](https://primate.run/blog/primate-040)

生成摘要时出错

---

## 56. Xiaomi-Robotics-1

**原文标题**: Xiaomi-Robotics-1

**原文链接**: [https://robotics.xiaomi.com/xiaomi-robotics-1.html](https://robotics.xiaomi.com/xiaomi-robotics-1.html)

生成摘要时出错

---

## 57. 5 Cups of coffee per day (up to 400 mg of caffeine/day) is safe for most adults

**原文标题**: 5 Cups of coffee per day (up to 400 mg of caffeine/day) is safe for most adults

**原文链接**: [https://newsroom.heart.org/news/coffee-and-heart-health-how-many-cups-of-caffeinated-coffee-are-safe-to-drink-each-day](https://newsroom.heart.org/news/coffee-and-heart-health-how-many-cups-of-caffeinated-coffee-are-safe-to-drink-each-day)

生成摘要时出错

---

## 58. AliExpress hit with record $629M fine for counterfeit and illegal goods

**原文标题**: AliExpress hit with record $629M fine for counterfeit and illegal goods

**原文链接**: [https://www.engadget.com/2218530/aliexpress-hit-with-record-629-million-fine-for-selling-counterfeit-and-illegal-products/](https://www.engadget.com/2218530/aliexpress-hit-with-record-629-million-fine-for-selling-counterfeit-and-illegal-products/)

生成摘要时出错

---

## 59. Programming the Amiga and Atari ST in C: Reading Keyboard Input

**原文标题**: Programming the Amiga and Atari ST in C: Reading Keyboard Input

**原文链接**: [https://retrogamecoders.com/st-amiga-vbcc-c-input-echo/](https://retrogamecoders.com/st-amiga-vbcc-c-input-echo/)

生成摘要时出错

---

## 60. Introduce a memory safe compilation mode inspired by Fil-C

**原文标题**: Introduce a memory safe compilation mode inspired by Fil-C

**原文链接**: [https://codeberg.org/ziglang/zig/issues/36237](https://codeberg.org/ziglang/zig/issues/36237)

生成摘要时出错

---

## 61. Watching Tucson's Backyard Birds with Solar-Powered M1 Mac Mini

**原文标题**: Watching Tucson's Backyard Birds with Solar-Powered M1 Mac Mini

**原文链接**: [https://alec.is/birds/](https://alec.is/birds/)

生成摘要时出错

---

## 62. How much energy do data centers and artificial intelligence use?

**原文标题**: How much energy do data centers and artificial intelligence use?

**原文链接**: [https://ourworldindata.org/how-much-energy-do-data-centers-and-artificial-intelligence-use](https://ourworldindata.org/how-much-energy-do-data-centers-and-artificial-intelligence-use)

生成摘要时出错

---

## 63. FCC pays $340k/year to keep 100's of empty Alaska buildings wired for internet

**原文标题**: FCC pays $340k/year to keep 100's of empty Alaska buildings wired for internet

**原文链接**: [https://www.propublica.org/article/adak-island-alaska-internet-subsidy-fcc](https://www.propublica.org/article/adak-island-alaska-internet-subsidy-fcc)

An investigation by the *Anchorage Daily News* and *ProPublica* reveals that the FCC pays approximately $340,000 annually to maintain internet connections for hundreds of abandoned, deteriorating buildings in Adak, Alaska. These subsidies, drawn from the Universal Service Fund (USF) via fees on American phone bills, are intended to bring broadband to remote areas. However, in Adak—a former Navy base where the population has dwindled to roughly two dozen residents—the money is largely funding "ghost" connections.

The local provider, Adak Eagle Enterprises, is subsidized to serve 306 locations, yet reporters who visited every site found that not a single resident actually subscribes to the service. Instead, the community has switched to Starlink, which is 40 times faster and significantly cheaper than Adak Eagle’s subsidized offerings. Remarkably, even the Adak Eagle office uses Starlink dishes for its own internet.

The report highlights a systemic lack of federal oversight. Despite a 2013 federal order finding that Adak Eagle’s owner, Larry Mayes, used subsidy money for a fishing boat and "unreasonable" salaries, the FCC continues to provide millions in support. Many "connected" buildings are literally falling apart, with missing walls and grass growing on living room floors.

While Mayes claims he is following FCC rules, the agency has refused to comment on the waste. This situation serves as a stark example of the FCC’s failure to safeguard the USF, which continues to pay telecom companies regardless of their performance or the actual existence of customers. Ultimately, Alaskans continue to pay the highest rates for the slowest service while federal funds are funneled into infrastructure for a ghost town.

---

## 64. Show HN: A Pipeline for Making 10-minute AI Movies with Claude Code and Seedance

**原文标题**: Show HN: A Pipeline for Making 10-minute AI Movies with Claude Code and Seedance

**原文链接**: [https://github.com/dawndrain/movie-gen](https://github.com/dawndrain/movie-gen)

生成摘要时出错

---

## 65. Public Transport – Don't Make Me Think

**原文标题**: Public Transport – Don't Make Me Think

**原文链接**: [https://shkspr.mobi/blog/2026/07/public-transport-dont-make-me-think/](https://shkspr.mobi/blog/2026/07/public-transport-dont-make-me-think/)

生成摘要时出错

---

## 66. California to impose sales and use tax on digital products including SaaS

**原文标题**: California to impose sales and use tax on digital products including SaaS

**原文链接**: [https://www.pwc.com/us/en/services/tax/library/california-imposes-sales-and-use-tax-on-digital-products-and-saas.html](https://www.pwc.com/us/en/services/tax/library/california-imposes-sales-and-use-tax-on-digital-products-and-saas.html)

生成摘要时出错

---

## 67. Qwen 3.8

**原文标题**: Qwen 3.8

**原文链接**: [https://twitter.com/Alibaba_Qwen/status/2078759124914098291](https://twitter.com/Alibaba_Qwen/status/2078759124914098291)

生成摘要时出错

---

## 68. EU fines AliExpress €550M over illegal products

**原文标题**: EU fines AliExpress €550M over illegal products

**原文链接**: [https://www.euractiv.com/news/eu-fines-aliexpress-e550-million-over-illegal-products/](https://www.euractiv.com/news/eu-fines-aliexpress-e550-million-over-illegal-products/)

生成摘要时出错

---

## 69. DrDroid (YC W23) Is Hiring

**原文标题**: DrDroid (YC W23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory](https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory)

生成摘要时出错

---

## 70. SPIR-V on ROCm: A Portable IR for AMD GPUs

**原文标题**: SPIR-V on ROCm: A Portable IR for AMD GPUs

**原文链接**: [https://rocm.blogs.amd.com/software-tools-optimization/spir-v-rocm/README.html](https://rocm.blogs.amd.com/software-tools-optimization/spir-v-rocm/README.html)

生成摘要时出错

---

## 71. Chrome installed a global Ctrl+G keyboard shortcut to launch Gemini

**原文标题**: Chrome installed a global Ctrl+G keyboard shortcut to launch Gemini

**原文链接**: [https://mastodon.online/users/mwichary/statuses/116952836351215165](https://mastodon.online/users/mwichary/statuses/116952836351215165)

生成摘要时出错

---

## 72. 11,700 Free Photos from John Margolies' Archive of Americana Architecture

**原文标题**: 11,700 Free Photos from John Margolies' Archive of Americana Architecture

**原文链接**: [https://www.openculture.com/2026/07/free-photos-from-john-margolies-archive-of-americana-architecture.html](https://www.openculture.com/2026/07/free-photos-from-john-margolies-archive-of-americana-architecture.html)

生成摘要时出错

---

## 73. A 600-acre AI data center could cost some Wisconsin residents their land

**原文标题**: A 600-acre AI data center could cost some Wisconsin residents their land

**原文链接**: [https://abcnews.com/US/600-acre-ai-data-center-cost-wisconsin-residents/story?id=130153006](https://abcnews.com/US/600-acre-ai-data-center-cost-wisconsin-residents/story?id=130153006)

生成摘要时出错

---

## 74. Claude Code uses Bun written in Rust now

**原文标题**: Claude Code uses Bun written in Rust now

**原文链接**: [https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)

生成摘要时出错

---

## 75. Datasette-plot – Datasette Plugin for building data visualizations

**原文标题**: Datasette-plot – Datasette Plugin for building data visualizations

**原文链接**: [https://www.datasette.cloud/blog/2023/datasette-plot/](https://www.datasette.cloud/blog/2023/datasette-plot/)

生成摘要时出错

---

## 76. I burned all my tokens researching how to save tokens

**原文标题**: I burned all my tokens researching how to save tokens

**原文链接**: [https://quesma.com/blog/custom-deep-research-pipeline/](https://quesma.com/blog/custom-deep-research-pipeline/)

生成摘要时出错

---

## 77. AliExpress fined €550M by EU for failing to stop sale of illegal and fake goods

**原文标题**: AliExpress fined €550M by EU for failing to stop sale of illegal and fake goods

**原文链接**: [https://www.theguardian.com/business/2026/jul/20/aliexpress-fined-by-eu-sale-of-illegal-fake-goods](https://www.theguardian.com/business/2026/jul/20/aliexpress-fined-by-eu-sale-of-illegal-fake-goods)

生成摘要时出错

---

## 78. Jacobian conjecture is false (with help of Fable)

**原文标题**: Jacobian conjecture is false (with help of Fable)

**原文链接**: [https://twitter.com/__alpoge__/status/2079028340955197566](https://twitter.com/__alpoge__/status/2079028340955197566)

生成摘要时出错

---

## 79. Visualizing the Artemis II Mission

**原文标题**: Visualizing the Artemis II Mission

**原文链接**: [https://foxglove.dev/blog/visualizing-the-artemis-ii-mission](https://foxglove.dev/blog/visualizing-the-artemis-ii-mission)

生成摘要时出错

---

## 80. Who Is America's Homer?

**原文标题**: Who Is America's Homer?

**原文链接**: [https://www.plough.com/articles/who-is-americas-homer](https://www.plough.com/articles/who-is-americas-homer)

生成摘要时出错

---

## 81. Codex is wearing out our devices

**原文标题**: Codex is wearing out our devices

**原文链接**: [https://old.reddit.com/r/codex/comments/1v0m3lt/codex_is_wearing_out_our_devices/](https://old.reddit.com/r/codex/comments/1v0m3lt/codex_is_wearing_out_our_devices/)

生成摘要时出错

---

## 82. Dupes took over the world

**原文标题**: Dupes took over the world

**原文链接**: [https://www.vox.com/podcasts/493930/dupe-culture-fender-ugg-quince-tiktok-amazon-online-shopping](https://www.vox.com/podcasts/493930/dupe-culture-fender-ugg-quince-tiktok-amazon-online-shopping)

生成摘要时出错

---

## 83. Trial Lawyers Lobby Against Autonomous Vehicles

**原文标题**: Trial Lawyers Lobby Against Autonomous Vehicles

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/07/trial-lawyers-lobby-against-autonomous-vehicles.html](https://marginalrevolution.com/marginalrevolution/2026/07/trial-lawyers-lobby-against-autonomous-vehicles.html)

生成摘要时出错

---

## 84. Police searched Twin Cities Flock cameras during ICE surge

**原文标题**: Police searched Twin Cities Flock cameras during ICE surge

**原文链接**: [https://www.startribune.com/police-search-immigration-twin-cities-flock-license-plate-cameras-ice-dhs-metro-surge/601807825](https://www.startribune.com/police-search-immigration-twin-cities-flock-license-plate-cameras-ice-dhs-metro-surge/601807825)

生成摘要时出错

---

## 85. HMD Touch 4G

**原文标题**: HMD Touch 4G

**原文链接**: [https://www.hmd.com/en_int/hmd-touch-4g](https://www.hmd.com/en_int/hmd-touch-4g)

生成摘要时出错

---

## 86. What I learned selling 2,500 MIDI recorders: Hardware is not so hard

**原文标题**: What I learned selling 2,500 MIDI recorders: Hardware is not so hard

**原文链接**: [https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard)

生成摘要时出错

---

## 87. Cagire: Live Coding in Forth

**原文标题**: Cagire: Live Coding in Forth

**原文链接**: [https://cagire.raphaelforment.fr](https://cagire.raphaelforment.fr)

生成摘要时出错

---

## 88. Orion Browser by Kagi

**原文标题**: Orion Browser by Kagi

**原文链接**: [https://orionbrowser.com/](https://orionbrowser.com/)

生成摘要时出错

---

## 89. C64 Basic Dungeon Crawler: Goblin Attack (C64 Basic Part 8)

**原文标题**: C64 Basic Dungeon Crawler: Goblin Attack (C64 Basic Part 8)

**原文链接**: [https://retrogamecoders.com/c64-basic-dungeon-part8/](https://retrogamecoders.com/c64-basic-dungeon-part8/)

生成摘要时出错

---

## 90. Ontario prison AI assigns black prisoners harsher living conditions

**原文标题**: Ontario prison AI assigns black prisoners harsher living conditions

**原文链接**: [https://breachmedia.ca/black-prisoners-are-assigned-harsher-living-conditions-in-ontario-jails-thanks-to-ai/](https://breachmedia.ca/black-prisoners-are-assigned-harsher-living-conditions-in-ontario-jails-thanks-to-ai/)

生成摘要时出错

---

## 91. The AI hype is a mass psychosis echo chamber of incompetent individuals

**原文标题**: The AI hype is a mass psychosis echo chamber of incompetent individuals

**原文链接**: [https://aob2f.substack.com/p/the-ai-hype-is-a-mass-psychosis-echo](https://aob2f.substack.com/p/the-ai-hype-is-a-mass-psychosis-echo)

生成摘要时出错

---

## 92. Talk: The Art of Braiding Algorithms

**原文标题**: Talk: The Art of Braiding Algorithms

**原文链接**: [https://pgadey.ca/notes/talk-relatorium-2026/](https://pgadey.ca/notes/talk-relatorium-2026/)

生成摘要时出错

---

## 93. NYC Roam: 3D world with real transit and building data

**原文标题**: NYC Roam: 3D world with real transit and building data

**原文链接**: [https://www.nycroam.com/](https://www.nycroam.com/)

生成摘要时出错

---

## 94. Modder Makes GTA: Vice City Playable Inside GTA 3 Inside GTA: San Andreas

**原文标题**: Modder Makes GTA: Vice City Playable Inside GTA 3 Inside GTA: San Andreas

**原文链接**: [https://kotaku.com/gta-vice-city-made-playable-in-gta-3-made-playable-in-gta-san-andreas-2000717510](https://kotaku.com/gta-vice-city-made-playable-in-gta-3-made-playable-in-gta-san-andreas-2000717510)

生成摘要时出错

---

## 95. The World Cup Could Not Be Americanized

**原文标题**: The World Cup Could Not Be Americanized

**原文链接**: [https://www.theatlantic.com/culture/2026/07/world-cup-spain-argentina/688000/](https://www.theatlantic.com/culture/2026/07/world-cup-spain-argentina/688000/)

生成摘要时出错

---

## 96. Terence McKenna's Mega Bad Trip (2025)

**原文标题**: Terence McKenna's Mega Bad Trip (2025)

**原文链接**: [https://psychedelics.community/cultural-icons/terence-mckennas-mega-bad-trip](https://psychedelics.community/cultural-icons/terence-mckennas-mega-bad-trip)

生成摘要时出错

---

## 97. My husbands suicide shows theres something very wrong with US insurance industry

**原文标题**: My husbands suicide shows theres something very wrong with US insurance industry

**原文链接**: [https://www.statnews.com/2026/07/20/psychiatric-insurance-coverage-suicide-denial-personal-essay/](https://www.statnews.com/2026/07/20/psychiatric-insurance-coverage-suicide-denial-personal-essay/)

生成摘要时出错

---

## 98. Natural experiments prove phytoplankton carbon removal works

**原文标题**: Natural experiments prove phytoplankton carbon removal works

**原文链接**: [https://www.onepercentbrighter.com/p/natural-experiments-prove-feeding](https://www.onepercentbrighter.com/p/natural-experiments-prove-feeding)

生成摘要时出错

---

## 99. Homeowner may lose 1/3 of her property to data center high-voltage power line

**原文标题**: Homeowner may lose 1/3 of her property to data center high-voltage power line

**原文链接**: [https://www.nbcwashington.com/news/local/weve-been-sacrificed-homeowner-may-lose-1-3-of-her-property-to-high-voltage-power-line-for-data-cente/4128713/](https://www.nbcwashington.com/news/local/weve-been-sacrificed-homeowner-may-lose-1-3-of-her-property-to-high-voltage-power-line-for-data-cente/4128713/)

生成摘要时出错

---

## 100. Blender 5.2 LTS

**原文标题**: Blender 5.2 LTS

**原文链接**: [https://www.blender.org/download/releases/5-2/](https://www.blender.org/download/releases/5-2/)

生成摘要时出错

---

