# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-29.md)

*最后自动更新时间: 2026-01-29 18:06:39*
## 1. Claude Code 性能退化追踪每日基准测试

**原文标题**: Claude Code Daily Benchmarks for Degradation Tracking

**原文链接**: [https://marginlab.ai/trackers/claude-code/](https://marginlab.ai/trackers/claude-code/)

本报告详细介绍了一项针对 **Claude Code (Opus 4.5)** 的性能跟踪计划，旨在检测其处理软件工程 (SWE) 任务能力中是否存在统计学意义上的显著退化。该追踪器由独立第三方管理，是在 Anthropic 就 2025 年模型退化问题进行复盘后建立的。

**核心发现（截至 2026 年 1 月 29 日）：**
过去 30 天内检测到了**统计学意义上的显著退化**。虽然每日和每周的波动（通过率分别为 50% 和 53%）处于预期的误差范围内，但 30 天累计通过率降至 **54%**。这较设定的 **58% 基准**下降了 4.1%，突破了统计显著性（p < 0.05）所需的 ±3.4% 阈值。

**方法论：**
*   **真实场景测试：** 基准测试直接调用 Claude Code CLI 及最新的 SOTA 模型 (Opus 4.5)，避免使用自定义测试框架，以确保结果反映真实的用户体验。
*   **数据来源：** 每日评估基于经过策划且具有防污染特性的 **SWE-Bench-Pro** 子集。
*   **样本量：** 每日评估包含 50 次试验。为了减少“噪点”并提高可靠性，追踪器将数据汇总为 7 天（250 次试验）和 30 天（655 次试验）的滚动平均值。
*   **统计严谨性：** 使用 95% 置信区间的伯努利随机变量对性能进行建模。

该追踪器为开发者提供了透明度，通过每日趋势可视化和邮件预警，在工具的编码能力出现经证实的质量下降时及时提醒用户。

---

## 2. Project Genie：探索无限交互式世界

**原文标题**: Project Genie: Experimenting with infinite, interactive worlds

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/)

Google 推出了 **Project Genie**，这是一个实验性研究原型，允许用户创建、探索和重混互动式沉浸世界。这款网页端应用目前面向美国的 Google AI Ultra 订阅用户开放，由通用世界模型 **Genie 3** 驱动，旨在实时模拟复杂的环境和物理属性。

该体验围绕三个核心能力展开：
*   **世界草绘 (World Sketching)：** 用户可以使用文本提示或图像生成环境。他们可以定义自己的角色、移动模式（如飞行或驾驶）以及视角（第一人称或第三人称）。
*   **世界探索 (World Exploration)：** 不同于静态环境，Project Genie 会随着用户的移动动态生成前方的路径，创造出一个可导航且不断演进的空间。
*   **世界重混 (World Remixing)：** 用户可以在现有作品的基础上进行二次创作，浏览精选画廊寻找灵感，并下载其探索过程的视频。

在技术层面，Project Genie 代表了向通用人工智能 (AGI) 迈进的一步，它超越了静态模拟，实现了能够预测并生成现实世界动态的系统。它将 Genie 3 与 Gemini 和 Nano Banana Pro 等其他模型集成，为世界创建提供精细化的控制。

作为早期研究原型，该工具尚存一些局限：生成的世界可能缺乏完全的真实感，角色控制可能存在延迟，且目前的生成时长限制在 60 秒以内。Google 计划利用此次初步推出的反馈来完善技术，并最终向全球更广泛的用户开放。

---

## 3. 如何为 CLI 应用程序选择颜色 (2023)

**原文标题**: How to Choose Colors for Your CLI Applications (2023)

**原文链接**: [https://blog.xoria.org/terminal-colors/](https://blog.xoria.org/terminal-colors/)

在《如何为 CLI 应用程序选择颜色（2023）》一文中，Luna Razzaghipour 探讨了确保命令行界面（CLI）在各种终端主题下保持可读性的难点。虽然开发者个人的主题可能效果极佳，但默认主题往往会导致常用颜色难以辨认。

作者测试了几种流行环境以找出这些隐患：
*   **基础主题 (macOS)：** 这些主题通常对比度较差；例如，明黄色在浅色模式下无法看清，而蓝色和亮蓝色在深色模式下则不可见。
*   **Tango 主题 (Ubuntu)：** 这些主题未能针对对比度调整灰度。白色和亮白色在浅色背景下不可读，而黑色在深色背景下不可读。
*   **Solarized：** 作为最流行的自定义主题，Solarized 带来了独特的挑战。由于它设计于 24 位色尚未普及的年代，它占用了“亮色”槽位来定义其界面的单色调。因此，任何使用亮色的 CLI 在 Solarized 用户眼中都会变成低对比度的灰色，甚至完全隐形。

文章还强调了“加粗”问题：许多终端模拟器会自动将加粗文本映射到其对应的“亮色”变体，这可能会意外触发上述可见性问题。

最终，作者得出结论：在 32 种可能的颜色与加粗组合中，**只有 11 种在通用场景下“大致可行”**。为了确保 CLI 工具对最广泛的用户群体保持易用和可读，Razzaghipour 建议开发者避免使用亮色变体和特定灰度，转而坚持使用一组严格受限、可靠且高对比度的颜色。

---

## 4. 欧洲新一代气象卫星传回首批图像

**原文标题**: Europe’s next-generation weather satellite sends back first images

**原文链接**: [https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/meteosat_third_generation/Europe_s_next-generation_weather_satellite_sends_back_first_images](https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/meteosat_third_generation/Europe_s_next-generation_weather_satellite_sends_back_first_images)

欧洲航天局（ESA）发布了第三代气象卫星探测卫星（MTG-S）的首批图像，标志着气象技术的重大进步。MTG-S于2025年7月发射，是欧洲首个将高光谱探测仪器部署在地球上方36,000公里的地球静止轨道的任务。

该卫星的红外探测器利用1,700个通道，以前所未有的细节测量大气温度和湿度。这些功能使科学家能够生成三维大气图，并追踪微量气体、风力，甚至包括埃塞俄比亚海利古比（Hayli Gubbi）事件在内的火山喷发。通过保持在赤道上空的固定位置，该卫星每15至30分钟提供一次欧洲和北非的更新数据。

该任务的主要益处是彻底改变了“临近预报”——即以显著提高的准确性和预警时间预测严重且快速演变的风暴的能力。这些实时数据对于保护公民安全和优化受天气影响的行业至关重要。

MTG项目是ESA、欧洲气象卫星开发组织（Eumetsat）、欧盟委员会以及包括泰雷兹阿莱尼亚航天公司（Thales Alenia Space）和OHB系统公司在内的工业伙伴共同合作的结晶。MTG-S与现有的MTG成像卫星（MTG-I）互补，并搭载了负责监测空气质量的哥白尼哨兵-4号（Copernicus Sentinel-4）任务。第二颗成像卫星计划于2026年发射，以进一步增强该卫星星座的能力。

---

## 5. 报道称美国网络安全主管向 ChatGPT 泄露政府敏感文件

**原文标题**: US cybersecurity chief leaked sensitive government files to ChatGPT: Report

**原文链接**: [https://www.dexerto.com/entertainment/us-cybersecurity-chief-leaked-sensitive-government-files-to-chatgpt-report-3311462/](https://www.dexerto.com/entertainment/us-cybersecurity-chief-leaked-sensitive-government-files-to-chatgpt-report-3311462/)

据《政治新闻网》（Politico）报道，美国网络安全与基础设施安全局（CISA）代理局长马杜·戈图穆卡拉（Madhu Gottumukkala）因将政府敏感文件上传至公开版 ChatGPT 而正在接受调查。

据称，该事件发生在去年夏天，当时戈图穆卡拉上传了标记为“仅供官方使用”的合同文件。尽管美国国土安全部（DHS）通常禁止员工使用 ChatGPT，但据报道，戈图穆卡拉此前获得了使用该工具的特殊豁免。内部监控系统在 8 月发现了这一活动，随后由国土安全部主导开展了损失评估，以确定这些敏感数据（在公开版软件中会与 OpenAI 共享）是否泄露。

对此，CISA 发言人玛茜·麦卡锡（Marci McCarthy）为该行为辩护，称其使用是“短期且有限的”，且是在“国土安全部管控之下”进行的。

此次泄密事件进一步加剧了外界对戈图穆卡拉代理期间领导能力的审查。他此前还曾面临未通过强制性反情报测谎的指控，但他在此前的国会听证会上否认了这一说法。这些安全疑虑出现之际正值关键时刻，因为特朗普政府正在积极推动“人工智能优先”战略，并致力于扩大人工智能在联邦机构和军事部门的应用。

---

## 6. Reflex (YC W23) 高级基础架构软件工程师

**原文标题**: Reflex (YC W23) Senior Software Engineer Infra

**原文链接**: [https://www.ycombinator.com/companies/reflex/jobs/Jcwrz7A-lead-software-engineer-infra](https://www.ycombinator.com/companies/reflex/jobs/Jcwrz7A-lead-software-engineer-infra)

Reflex 是一家由 Y Combinator 孵化（W23）的初创公司，目前正在旧金山招聘一名**基础架构首席软件工程师**。公司致力于为企业级应用提供统一的“操作系统”，通过单一平台替代碎片化的开发技术栈，实现生产级应用端到端的构建、部署与管理。

**职位与薪酬**
*   **薪资：** 13 万美元 – 20 万美元
*   **期权：** 0.15% – 0.50%
*   **核心职责：** 领导基础架构团队，负责全栈基础设施，并优化可观测性与监控系统。
*   **任职

**公司概况**
Reflex 正在飞速增长，其开源框架已驱动超过 100 万个应用，并获得逾 2.8 万个 GitHub 星标。目前，全球 30% 的财富 500 强企业已采用 Reflex。公司团队规模约 10 人，汇聚了 IOI（国际信息学奥赛）奖牌得主及开发者工具领域独角兽企业的资深人士。Reflex 近期刚完成新一轮融资，旨在通过在框架和基础架构层提供可重用的抽象，消除组织内部的效率瓶颈。

**面试流程**
全程远程进行，包括：
1.  初步介绍性通话。
2.  技术家庭测试 (Take-home test)。
3.  “现场”面试（远程），包含 2–3 轮技术面试（每轮 45 分钟）。
4.  最终跟进或直接发放 Offer。

该职位是加入早期高增长、使命驱动型初创公司的理想机会，候选人将参与塑造 Web 开发与企业基础架构的未来。

---

## 7. OTelBench：AI 难以应对简单的 SRE 任务（Opus 4.5 得分仅为 29%）

**原文标题**: OTelBench: AI struggles with simple SRE tasks (Opus 4.5 scores only 29%)

**原文链接**: [https://quesma.com/blog/introducing-otel-bench/](https://quesma.com/blog/introducing-otel-bench/)

OTelBench, a new open-source benchmark, reveals that frontier AI models significantly struggle with "simple" Site Reliability Engineering (SRE) tasks. Specifically, the benchmark evaluates an AI’s ability to implement OpenTelemetry (OTel) instrumentation—adding distributed tracing to microservices—across 11 programming languages.

Despite the high expectations for frontier models, the results were underwhelming. **Claude 4.5 Opus** led the field with a success rate of only **29%**, followed by **GPT 5.2** at **26%**. Notably, the much cheaper **Gemini 3 Flash** (19%) outperformed Gemini 3 Pro, making it the most cost-effective model tested.

The study identified several core reasons for these failures:
*   **Lack of Business Context:** Models often applied instrumentation mechanically to all HTTP calls. This resulted in "silent failures" where code compiled, but separate user actions were incorrectly merged into a single trace.
*   **Polyglot Complexity:** Instrumentation requires more than coding; it demands mastery of language-specific build systems (like CMake for C++ or Maven for Java). Models failed entirely in Java, Ruby, and Swift.
*   **Long-Horizon Tasks:** Effective instrumentation is a "job, not a puzzle," requiring diligent testing and context propagation that current models cannot yet sustain over 300+ lines of code.

The authors conclude that while "AI SRE" is currently overhyped, OTelBench provides a necessary "North Star" for improvement. They suggest that future progress may come from multi-agent systems or Reinforcement Learning with Verified Rewards. For now, however, complex distributed tracing remains a task that requires a skilled human engineer.

---

## 8. Heating homes with the largest particle accelerator

**原文标题**: Heating homes with the largest particle accelerator

**原文链接**: [https://home.cern/news/news/cern/heating-homes-worlds-largest-particle-accelerator](https://home.cern/news/news/cern/heating-homes-worlds-largest-particle-accelerator)

生成摘要时出错

---

## 9. Drug trio found to block tumour resistance in pancreatic cancer

**原文标题**: Drug trio found to block tumour resistance in pancreatic cancer

**原文链接**: [https://www.drugtargetreview.com/news/192714/drug-trio-found-to-block-tumour-resistance-in-pancreatic-cancer/](https://www.drugtargetreview.com/news/192714/drug-trio-found-to-block-tumour-resistance-in-pancreatic-cancer/)

生成摘要时出错

---

## 10. Project Genie: Interactive worlds generated in real-time

**原文标题**: Project Genie: Interactive worlds generated in real-time

**原文链接**: [https://labs.google/projectgenie](https://labs.google/projectgenie)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 2 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 3 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 4 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 5 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 6 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 7 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 8 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 9 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 10 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 11 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 12 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 13 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 14 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 15 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 16 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 17 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 18 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 19 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 20 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 21 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 22 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 23 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 24 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 25 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 26 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 27 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 28 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 29 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 30 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 31 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 32 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 33 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 34 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 35 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 36 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 37 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 38 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 39 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 40 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 41 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 42 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 43 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 44 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 45 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 46 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 47 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 48 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 49 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 50 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 51 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 52 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 53 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 54 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 55 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 56 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 57 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 58 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 59 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 60 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 61 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 62 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 63 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 64 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 65 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 66 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 67 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 68 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 69 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 70 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 71 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 72 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 73 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 74 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 75 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 76 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 77 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 78 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 79 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 80 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 81 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 82 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 83 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 84 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 85 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 86 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 87 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 88 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 89 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 90 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 91 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 92 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 93 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 94 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 95 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 96 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 97 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 98 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 99 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 100 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 101 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 102 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 103 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 104 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 105 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 106 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 107 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 108 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 109 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 110 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 111 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 112 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 113 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 114 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 115 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 116 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 117 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 118 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 119 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 120 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 121 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 122 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 123 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 124 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 125 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 126 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 127 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 128 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 129 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 130 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 131 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 132 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 133 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 134 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 135 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 136 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 137 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 138 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 139 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 140 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 141 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 142 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 143 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 144 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 145 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 146 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 147 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 148 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 149 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 150 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 151 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 152 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 153 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 154 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 155 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 156 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 157 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 158 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 159 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 160 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 161 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 162 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 163 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 164 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 165 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 166 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 167 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 168 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 169 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 170 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 171 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 172 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 173 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 174 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 175 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 176 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 177 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 178 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 179 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 180 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 181 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 182 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 183 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 184 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 185 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 186 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 187 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 188 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 189 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 190 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 191 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 192 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 193 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 194 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 195 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 196 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 197 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 198 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 199 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 200 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 201 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 202 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 203 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 204 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 205 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 206 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 207 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 208 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 209 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 210 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 211 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 212 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 213 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 214 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 215 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 216 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 217 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 218 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 219 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 220 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 221 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 222 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 223 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 224 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 225 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 226 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 227 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 228 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 229 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 230 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 231 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 232 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 233 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 234 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 235 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 236 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 237 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 238 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 239 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 240 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 241 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 242 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 243 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 244 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 245 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 246 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 247 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 248 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 249 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 250 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 251 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 252 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 253 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 254 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 255 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 256 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 257 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 258 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 259 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 260 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 261 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 262 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 263 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 264 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 265 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 266 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 267 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 268 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 269 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 270 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 271 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 272 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 273 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 274 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 275 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 276 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 277 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 278 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 279 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 280 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 281 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 282 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 283 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 284 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 285 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 286 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 287 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 288 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 289 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 290 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 291 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 292 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 293 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 294 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 295 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 296 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 297 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 298 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 299 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 300 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 301 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 302 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 303 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 304 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 305 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 306 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 307 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 308 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 309 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 310 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 311 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 312 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 313 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 314 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 315 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
