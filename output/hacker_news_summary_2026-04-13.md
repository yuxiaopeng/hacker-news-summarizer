# Hacker News 热门文章摘要 (2026-04-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 无事发生：在非体育类市场中始终买入“否”的 Polymarket 机器人

**原文标题**: Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets

**原文链接**: [https://github.com/sterlingcrispin/nothing-ever-happens](https://github.com/sterlingcrispin/nothing-ever-happens)

“Nothing Ever Happens” 是一个基于 Python 的异步机器人，专为 Polymarket 设计，执行一种特定的逆向策略：在独立的非体育赛事市场中购买“No”结果。该机器人基于“预测的事件通常不会发生”这一怀疑前提，扫描市场中价格低于可配置上限的“No”头寸。

该项目通过分层执行模型强调安全性和风险管理。实盘交易被严格锁定在涉及特定环境变量（`BOT_MODE`、`LIVE_TRADING_ENABLED` 和 `DRY_RUN`）的三重确认机制之后。如果未针对实盘操作进行明确配置，机器人将默认使用 `PaperExchangeClient` 进行模拟交易。对于实盘运行，该机器人需要私钥、出资人地址、数据库和 Polygon RPC URL。

技术上，该仓库分为三个主要部分：
*   **bot/:** 包含核心运行时、交易所客户端以及“nothing_happens”策略逻辑。
*   **scripts/:** 提供用于数据库检查、钱包历史记录和日志解析的操作工具。
*   **tests/:** 包含单元测试和回归测试覆盖。

该机器人配备了用于实时监控的仪表板，以及一个在实盘交易期间实现状态持久化的恢复系统。它针对 Heroku 部署进行了优化，特别是使用 web dyno 作为其运行环境。作者按“原样”提供该软件，仅供娱乐之用，明确声明不对使用过程中产生的任何财务损失或损害承担任何责任。

---

## 2. The Future of Everything Is Lies, I Guess: Safety

**原文标题**: The Future of Everything Is Lies, I Guess: Safety

**原文链接**: [https://aphyr.com/posts/417-the-future-of-everything-is-lies-i-guess-safety](https://aphyr.com/posts/417-the-future-of-everything-is-lies-i-guess-safety)

In "The Future of Everything Is Lies, I Guess: Safety," the author argues that machine learning (ML) systems pose an existential threat to security and societal trust. The central thesis is that "alignment"—the effort to ensure AI remains pro-social—is a failing endeavor. Because alignment is expensive, optional, and easily bypassed, the democratization of hardware and data ensures that "evil" models will inevitably be built alongside "friendly" ones.

The article details three primary safety crises:

1.  **The "Unifecta" of Security:** LLMs are chaotic systems that cannot distinguish between legitimate user instructions and malicious "prompt injections" from untrusted data. Consequently, the author argues that LLMs should never be given the power to perform irreversible actions (like deleting files or communicating externally), as they are fundamentally unpredictable.
2.  **Accelerated Exploits:** ML models are becoming highly efficient at identifying software vulnerabilities. This lowers the cost of cyberattacks, particularly for the "long tail" of less-secure software. The author characterizes the current AI boom as a "venture-capital Manhattan project" creating digital weapons that will be difficult to defend against.
3.  **The Death of Evidence:** The ability to synthesize realistic audio and imagery undermines the foundational trust required for insurance, legal systems, and personal communication. This enables sophisticated, high-touch fraud (such as voice cloning or fake evidence) at an industrial scale.

Ultimately, the author predicts a "culture of suspicion" where the economic and social costs of fraud increase significantly. While cryptographic solutions for verifying "real" content exist, they are currently insufficient to stem the tide of ML-generated deception. The author concludes that by building these models, the tech industry has lowered the bar for malicious actors, making a future of widespread "lies" inevitable.

---

## 3. 为整个 Cloudflare 构建 CLI

**原文标题**: Building a CLI for All of Cloudflare

**原文链接**: [https://blog.cloudflare.com/cf-cli-local-explorer/](https://blog.cloudflare.com/cf-cli-local-explorer/)

生成摘要时出错

---

## 4. Servo 现已在 crates.io 上线

**原文标题**: Servo is now available on crates.io

**原文链接**: [https://servo.org/blog/2026/04/13/servo-0.1.0-release/](https://servo.org/blog/2026/04/13/servo-0.1.0-release/)

2026年4月13日，Servo 团队宣布在 crates.io 上发布了 **servo** crate 的 0.1.0 版本，正式允许 Servo 作为嵌入式库使用。虽然该引擎现在已可供开发者使用，但团队指出，目前暂无计划将演示浏览器 **servoshell** 发布至 crates.io。

此次发布是在该项目自 2025 年 10 月在 GitHub 首次发布以来，开发流程日趋成熟的基础上进行的。尽管团队仍在确定 1.0 里程碑的具体要求，但 0.1.0 版本反映了其对当前嵌入式 API 的高度信心。

为了满足不同的用户需求，团队推出了 Servo 的**长期支持 (LTS)** 版本。该版本专为倾向于更稳定开发周期的嵌入方设计，提供定期的半年更新、安全补丁及迁移指南，以避免应对常规每月发布中可能出现的破坏性变更。关于 LTS 版本的更多详情，可参阅 Servo book。

---

## 5. Make Tmux Pretty and Usable (2024)

**原文标题**: Make Tmux Pretty and Usable (2024)

**原文链接**: [https://hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/](https://hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/)

生成摘要时出错

---

## 6. Tracking down a 25% Regression on LLVM RISC-V

**原文标题**: Tracking down a 25% Regression on LLVM RISC-V

**原文链接**: [https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/](https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/)

生成摘要时出错

---

## 7. MEMS阵列芯片可投影沙粒大小的视频

**原文标题**: MEMS Array Chip Can Project Video the Size of a Grain of Sand

**原文链接**: [https://spectrum.ieee.org/mems-photonics](https://spectrum.ieee.org/mems-photonics)

研究人员开发出一种突破性的MEMS（微机电系统）阵列芯片，能够在仅约沙粒大小的微观尺度上投影高分辨率视频和图像。

该装置最初旨在操控量子计算机内部的激光，利用“长分立电极”结构实现极高精度的光线操纵。尽管其核心功能是满足量子处理器的复杂需求，但该技术在极小尺度下投影出可辨识图像（如《蒙娜丽莎》）的能力，证明了其广泛的适用性。

这一创新标志着小型化和激光偏转技术的重大飞跃。除了最初的量子计算用途外，该技术在消费电子、生物医学成像和超紧凑显示系统等领域也展现出巨大的应用潜力。通过成功将高端计算组件转用于图像投影，研究人员为将光学系统集成到更微型设备中开辟了新路径。

---

## 8. 仅由单一二元算子构成的所有初等函数

**原文标题**: All elementary functions from a single binary operator

**原文链接**: [https://arxiv.org/abs/2603.21852](https://arxiv.org/abs/2603.21852)

生成摘要时出错

---

## 9. Initial mainline video capture and camera support for Rockchip RK3588

**原文标题**: Initial mainline video capture and camera support for Rockchip RK3588

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/mainline-video-capture-and-camera-support-for-rockchip-rk3588.html](https://www.collabora.com/news-and-blog/news-and-events/mainline-video-capture-and-camera-support-for-rockchip-rk3588.html)

This article details Collabora’s multi-year effort to bring mainline Linux support for video capture and camera functionality to the Rockchip RK3588 SoC. While most RK3588 features are already well-supported upstream, Image Signal Processors (ISPs) and video capture blocks (VICAP) often lag behind due to hardware complexity and documentation gaps.

Key milestones in this journey include:

*   **VICAP Support:** After five years and 25 iterations, the `rkcif` driver was accepted into the mainline kernel in October 2025. It initially supported the PX30 and RK3568, with extension patches for the RK3588 recently submitted for review.
*   **MIPI CSI-2:** A driver for the MIPI CSI-2 receiver unit, essential for camera connectivity, was merged in January 2026.
*   **Current Progress:** While raw image capture is now possible, current software-based debayering results in low performance (e.g., 1 fps). 

To achieve a fully functional, hardware-accelerated pipeline, the project is focusing on three next steps:

1.  **VICAP MUX-TOISP:** Implementing the hardware connection that passes data directly from the capture unit to the ISP to reduce latency and memory bandwidth.
2.  **RKISP2 Driver:** Developing a new, from-scratch `rkisp2` kernel driver in collaboration with Rockchip and Ideas on Board to support the RK35 generation ISPs.
3.  **libcamera Integration:** Building support for Image Processing Algorithms (IPA) within libcamera to handle tasks like auto white balance and hardware debayering.

Collabora aims to replace current vendor-kernel reliance with this mainline solution to improve regulatory compliance and system longevity. A live demo of the RK3588 ISP support is scheduled for the Embedded Recipes conference in late May 2026.

---

## 10. Microsoft isn't removing Copilot from Windows 11, it's just renaming it

**原文标题**: Microsoft isn't removing Copilot from Windows 11, it's just renaming it

**原文链接**: [https://www.neowin.net/opinions/microsoft-isnt-removing-copilot-from-windows-11-its-just-renaming-it/](https://www.neowin.net/opinions/microsoft-isnt-removing-copilot-from-windows-11-its-just-renaming-it/)

生成摘要时出错

---

## 11. US appeals court declares 158-year-old home distilling ban unconstitutional

**原文标题**: US appeals court declares 158-year-old home distilling ban unconstitutional

**原文链接**: [https://nypost.com/2026/04/11/us-news/us-appeals-court-declares-158-year-old-home-distilling-ban-unconstitutional/](https://nypost.com/2026/04/11/us-news/us-appeals-court-declares-158-year-old-home-distilling-ban-unconstitutional/)

生成摘要时出错

---

## 12. Michigan 'digital age' bills pulled after privacy concerns raised

**原文标题**: Michigan 'digital age' bills pulled after privacy concerns raised

**原文链接**: [https://www.thecentersquare.com/michigan/article_7ca4e268-4a68-42fb-9042-f9d8604ebd7f.html](https://www.thecentersquare.com/michigan/article_7ca4e268-4a68-42fb-9042-f9d8604ebd7f.html)

生成摘要时出错

---

## 13. The economics of software teams: Why most engineering orgs are flying blind

**原文标题**: The economics of software teams: Why most engineering orgs are flying blind

**原文链接**: [https://www.viktorcessan.com/the-economics-of-software-teams/](https://www.viktorcessan.com/the-economics-of-software-teams/)

生成摘要时出错

---

## 14. We May Be Living Through the Most Consequential Hundred Days in Cyber History

**原文标题**: We May Be Living Through the Most Consequential Hundred Days in Cyber History

**原文链接**: [https://ringmast4r.substack.com/p/we-may-be-living-through-the-most](https://ringmast4r.substack.com/p/we-may-be-living-through-the-most)

生成摘要时出错

---

## 15. Taking on CUDA with ROCm: 'One Step After Another'

**原文标题**: Taking on CUDA with ROCm: 'One Step After Another'

**原文链接**: [https://www.eetimes.com/taking-on-cuda-with-rocm-one-step-after-another/](https://www.eetimes.com/taking-on-cuda-with-rocm-one-step-after-another/)

生成摘要时出错

---

## 16. DIY Soft Drinks

**原文标题**: DIY Soft Drinks

**原文链接**: [https://blinry.org/diy-soft-drinks/](https://blinry.org/diy-soft-drinks/)

生成摘要时出错

---

## 17. The Rational Conclusion of Doomerism Is Violence

**原文标题**: The Rational Conclusion of Doomerism Is Violence

**原文链接**: [https://www.campbellramble.ai/p/the-rational-conclusion](https://www.campbellramble.ai/p/the-rational-conclusion)

生成摘要时出错

---

## 18. Bring Back Idiomatic Design (2023)

**原文标题**: Bring Back Idiomatic Design (2023)

**原文链接**: [https://essays.johnloeber.com/p/4-bring-back-idiomatic-design](https://essays.johnloeber.com/p/4-bring-back-idiomatic-design)

生成摘要时出错

---

## 19. Show HN: boringBar – a taskbar-style dock replacement for macOS

**原文标题**: Show HN: boringBar – a taskbar-style dock replacement for macOS

**原文链接**: [https://boringbar.app/](https://boringbar.app/)

生成摘要时出错

---

## 20. Android now stops you sharing your location in photos

**原文标题**: Android now stops you sharing your location in photos

**原文链接**: [https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/](https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/)

生成摘要时出错

---

## 21. Who's Been Impersonating This ProPublica Reporter?

**原文标题**: Who's Been Impersonating This ProPublica Reporter?

**原文链接**: [https://www.propublica.org/article/impersonating-propublica-reporter](https://www.propublica.org/article/impersonating-propublica-reporter)

生成摘要时出错

---

## 22. Most people can't juggle one ball

**原文标题**: Most people can't juggle one ball

**原文链接**: [https://www.lesswrong.com/posts/jTGbKKGqs5EdyYoRc/most-people-can-t-juggle-one-ball](https://www.lesswrong.com/posts/jTGbKKGqs5EdyYoRc/most-people-can-t-juggle-one-ball)

生成摘要时出错

---

## 23. I ran Gemma 4 as a local model in Codex CLI

**原文标题**: I ran Gemma 4 as a local model in Codex CLI

**原文链接**: [https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4](https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4)

生成摘要时出错

---

## 24. I gave every train in New York an instrument

**原文标题**: I gave every train in New York an instrument

**原文链接**: [https://www.trainjazz.com/](https://www.trainjazz.com/)

生成摘要时出错

---

## 25. Missouri town fires half its city council over data center deal

**原文标题**: Missouri town fires half its city council over data center deal

**原文链接**: [https://www.politico.com/news/2026/04/13/missouri-city-council-data-center-00867259](https://www.politico.com/news/2026/04/13/missouri-city-council-data-center-00867259)

生成摘要时出错

---

## 26. A perfectable programming language

**原文标题**: A perfectable programming language

**原文链接**: [https://alok.github.io/lean-pages/perfectable-lean/](https://alok.github.io/lean-pages/perfectable-lean/)

生成摘要时出错

---

## 27. We have a 99% email reputation, but Gmail disagrees

**原文标题**: We have a 99% email reputation, but Gmail disagrees

**原文链接**: [https://blogfontawesome.wpcomstaging.com/we-have-a-99-email-reputation-gmail-disagrees/](https://blogfontawesome.wpcomstaging.com/we-have-a-99-email-reputation-gmail-disagrees/)

生成摘要时出错

---

## 28. Exploiting the most prominent AI agent benchmarks

**原文标题**: Exploiting the most prominent AI agent benchmarks

**原文链接**: [https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

生成摘要时出错

---

## 29. Show HN: Oberon System 3 runs natively on Raspberry Pi 3 (with ready SD card)

**原文标题**: Show HN: Oberon System 3 runs natively on Raspberry Pi 3 (with ready SD card)

**原文链接**: [https://github.com/rochus-keller/OberonSystem3Native/releases](https://github.com/rochus-keller/OberonSystem3Native/releases)

生成摘要时出错

---

## 30. Show HN: I built a social media management tool in 3 weeks with Claude and Codex

**原文标题**: Show HN: I built a social media management tool in 3 weeks with Claude and Codex

**原文链接**: [https://github.com/brightbeanxyz/brightbean-studio](https://github.com/brightbeanxyz/brightbean-studio)

生成摘要时出错

---

## 31. Point Cloud Allemansrätten

**原文标题**: Point Cloud Allemansrätten

**原文链接**: [https://digitalflapjack.com/weeknotes/point-cloud-allemansr%C3%A4tten/](https://digitalflapjack.com/weeknotes/point-cloud-allemansr%C3%A4tten/)

生成摘要时出错

---

## 32. Apple's accidental moat: How the "AI Loser" may end up winning

**原文标题**: Apple's accidental moat: How the "AI Loser" may end up winning

**原文链接**: [https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

生成摘要时出错

---

## 33. EasyPost (YC S13) Is Hiring

**原文标题**: EasyPost (YC S13) Is Hiring

**原文链接**: [https://www.easypost.com/careers](https://www.easypost.com/careers)

生成摘要时出错

---

## 34. Is math big or small?

**原文标题**: Is math big or small?

**原文链接**: [https://chessapig.github.io/talks/Big-Small](https://chessapig.github.io/talks/Big-Small)

生成摘要时出错

---

## 35. Claude.ai down

**原文标题**: Claude.ai down

**原文链接**: [https://status.claude.com/incidents/6jd2m42f8mld](https://status.claude.com/incidents/6jd2m42f8mld)

生成摘要时出错

---

## 36. Seven countries now generate nearly all their electricity from renewables (2024)

**原文标题**: Seven countries now generate nearly all their electricity from renewables (2024)

**原文链接**: [https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html](https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html)

生成摘要时出错

---

## 37. JVM Options Explorer

**原文标题**: JVM Options Explorer

**原文链接**: [https://chriswhocodes.com/vm-options-explorer.html](https://chriswhocodes.com/vm-options-explorer.html)

生成摘要时出错

---

## 38. Claude Mythos: The System Card

**原文标题**: Claude Mythos: The System Card

**原文链接**: [https://thezvi.substack.com/p/claude-mythos-the-system-card](https://thezvi.substack.com/p/claude-mythos-the-system-card)

生成摘要时出错

---

## 39. Phyphox – Physical Experiments Using a Smartphone

**原文标题**: Phyphox – Physical Experiments Using a Smartphone

**原文链接**: [https://phyphox.org/](https://phyphox.org/)

生成摘要时出错

---

## 40. Von der Leyen uses Orbán defeat to push for end of veto in EU foreign policy

**原文标题**: Von der Leyen uses Orbán defeat to push for end of veto in EU foreign policy

**原文链接**: [https://www.politico.eu/article/ursula-von-der-leyen-uses-hungary-viktor-orban-defeat-to-push-for-end-of-veto-in-eu-foreign-policy/](https://www.politico.eu/article/ursula-von-der-leyen-uses-hungary-viktor-orban-defeat-to-push-for-end-of-veto-in-eu-foreign-policy/)

Following the electoral defeat of Hungary’s longtime Prime Minister Viktor Orbán, European Commission President Ursula von der Leyen is urging the EU to abolish national vetoes in foreign policy. She advocates for a shift to "qualified majority voting" to prevent individual member states from blocking critical decisions, such as sanctions against Russia or financial aid for Ukraine.

Von der Leyen argues that the EU must capitalize on the "momentum" created by the election results. Under Orbán, who was often at odds with Brussels due to his ties with Russia and the U.S. far-right, Hungary frequently used its veto power to stall collective EU initiatives. The incoming Prime Minister, Péter Magyar, has signaled a clear pro-European stance, which von der Leyen welcomed as a "victory for fundamental freedoms" and a return to the "European path."

Despite her optimism, the proposal faces significant hurdles. Changing the voting structure requires unanimous consent from all member states. Even typically pro-EU nations may resist the move, as it would mean relinquishing sovereign control over their own foreign policies and potentially being forced to accept decisions they oppose. 

Nevertheless, von der Leyen emphasized that the Hungarian election—marked by record-high turnout—has strengthened EU unity. She expressed a commitment to working quickly with the new Hungarian government to prioritize reforms and the release of EU funds.

---

## 41. A Tour of Oodi

**原文标题**: A Tour of Oodi

**原文链接**: [https://blinry.org/oodi/](https://blinry.org/oodi/)

生成摘要时出错

---

## 42. How long-distance couples use digital games to facilitate intimacy (2025)

**原文标题**: How long-distance couples use digital games to facilitate intimacy (2025)

**原文链接**: [https://arxiv.org/abs/2505.09509](https://arxiv.org/abs/2505.09509)

生成摘要时出错

---

## 43. Pro Max 5x quota exhausted in 1.5 hours despite moderate usage

**原文标题**: Pro Max 5x quota exhausted in 1.5 hours despite moderate usage

**原文链接**: [https://github.com/anthropics/claude-code/issues/45756](https://github.com/anthropics/claude-code/issues/45756)

生成摘要时出错

---

## 44. Optimization of 32-bit Unsigned Division by Constants on 64-bit Targets

**原文标题**: Optimization of 32-bit Unsigned Division by Constants on 64-bit Targets

**原文链接**: [https://arxiv.org/abs/2604.07902](https://arxiv.org/abs/2604.07902)

生成摘要时出错

---

## 45. Show HN: Equirect – a Rust VR video player

**原文标题**: Show HN: Equirect – a Rust VR video player

**原文链接**: [https://github.com/greggman/equirect](https://github.com/greggman/equirect)

生成摘要时出错

---

## 46. Uncharted island soon to appear on nautical charts

**原文标题**: Uncharted island soon to appear on nautical charts

**原文链接**: [https://www.awi.de/en/about-us/service/press/single-view/unkartierte-insel-demnaechst-auf-seekarten-verzeichnet.html](https://www.awi.de/en/about-us/service/press/single-view/unkartierte-insel-demnaechst-auf-seekarten-verzeichnet.html)

生成摘要时出错

---

## 47. The peril of laziness lost

**原文标题**: The peril of laziness lost

**原文链接**: [https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/](https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/)

生成摘要时出错

---

## 48. Caffeine, cocaine, and painkillers detected in sharks from The Bahamas

**原文标题**: Caffeine, cocaine, and painkillers detected in sharks from The Bahamas

**原文链接**: [https://www.sciencedirect.com/science/article/abs/pii/S0269749126001880](https://www.sciencedirect.com/science/article/abs/pii/S0269749126001880)

生成摘要时出错

---

## 49. Galactic Algorithm

**原文标题**: Galactic Algorithm

**原文链接**: [https://en.wikipedia.org/wiki/Galactic_algorithm](https://en.wikipedia.org/wiki/Galactic_algorithm)

生成摘要时出错

---

## 50. Doom, Played over Curl

**原文标题**: Doom, Played over Curl

**原文链接**: [https://github.com/xsawyerx/curl-doom](https://github.com/xsawyerx/curl-doom)

生成摘要时出错

---

## 51. A Canonical Generalization of OBDD

**原文标题**: A Canonical Generalization of OBDD

**原文链接**: [https://arxiv.org/abs/2604.05537](https://arxiv.org/abs/2604.05537)

生成摘要时出错

---

## 52. Zed, A sans for the needs of 21st century (2024)

**原文标题**: Zed, A sans for the needs of 21st century (2024)

**原文链接**: [https://www.typotheque.com/blog/zed-a-sans-for-the-needs-of-21century](https://www.typotheque.com/blog/zed-a-sans-for-the-needs-of-21century)

生成摘要时出错

---

## 53. Why AI Sucks at Front End

**原文标题**: Why AI Sucks at Front End

**原文链接**: [https://nerdy.dev/why-ai-sucks-at-front-end](https://nerdy.dev/why-ai-sucks-at-front-end)

生成摘要时出错

---

## 54. Categorization Is 'Baked' into the Brain

**原文标题**: Categorization Is 'Baked' into the Brain

**原文链接**: [https://www.nature.com/articles/s41583-026-01036-2](https://www.nature.com/articles/s41583-026-01036-2)

生成摘要时出错

---

## 55. Google removes "Doki Doki Literature Club" from Google Play

**原文标题**: Google removes "Doki Doki Literature Club" from Google Play

**原文链接**: [https://bsky.app/profile/serenityforge.com/post/3mj3r4nbiws2t](https://bsky.app/profile/serenityforge.com/post/3mj3r4nbiws2t)

生成摘要时出错

---

## 56. Textbooks and Methods of Note-Taking in Early Modern Europe (2008)

**原文标题**: Textbooks and Methods of Note-Taking in Early Modern Europe (2008)

**原文链接**: [https://dash.harvard.edu/server/api/core/bitstreams/7312037d-e342-6bd4-e053-0100007fdf3b/content](https://dash.harvard.edu/server/api/core/bitstreams/7312037d-e342-6bd4-e053-0100007fdf3b/content)

生成摘要时出错

---

## 57. Programming Used to Be Free

**原文标题**: Programming Used to Be Free

**原文链接**: [https://purplesyringa.moe/blog/programming-used-to-be-free/](https://purplesyringa.moe/blog/programming-used-to-be-free/)

生成摘要时出错

---

## 58. Anthropic downgraded cache TTL on March 6th

**原文标题**: Anthropic downgraded cache TTL on March 6th

**原文链接**: [https://github.com/anthropics/claude-code/issues/46829](https://github.com/anthropics/claude-code/issues/46829)

生成摘要时出错

---

## 59. Basics of Radar Technology

**原文标题**: Basics of Radar Technology

**原文链接**: [https://www.radartutorial.eu/index.en.html](https://www.radartutorial.eu/index.en.html)

生成摘要时出错

---

## 60. Rockstar hackers set to release GTA 6 data breach as 'demands not met'

**原文标题**: Rockstar hackers set to release GTA 6 data breach as 'demands not met'

**原文链接**: [https://www.dexerto.com/gaming/hackers-threaten-to-leak-gta-6-plans-as-deadline-set-for-rockstar-3350476/](https://www.dexerto.com/gaming/hackers-threaten-to-leak-gta-6-plans-as-deadline-set-for-rockstar-3350476/)

生成摘要时出错

---

## 61. Mark's Magic Multiply

**原文标题**: Mark's Magic Multiply

**原文链接**: [https://wren.wtf/shower-thoughts/marks-magic-multiply/](https://wren.wtf/shower-thoughts/marks-magic-multiply/)

生成摘要时出错

---

## 62. The Physics of GPS

**原文标题**: The Physics of GPS

**原文链接**: [https://perthirtysix.com/how-does-gps-work](https://perthirtysix.com/how-does-gps-work)

生成摘要时出错

---

## 63. Cooperative Vectors Introduction

**原文标题**: Cooperative Vectors Introduction

**原文链接**: [https://www.evolvebenchmark.com/blog-posts/cooperative-vectors-introduction](https://www.evolvebenchmark.com/blog-posts/cooperative-vectors-introduction)

生成摘要时出错

---

## 64. Filing the corners off my MacBooks

**原文标题**: Filing the corners off my MacBooks

**原文链接**: [https://kentwalters.com/posts/corners/](https://kentwalters.com/posts/corners/)

生成摘要时出错

---

## 65. Bouncer: Block "crypto", "rage politics", and more from your X feed using AI

**原文标题**: Bouncer: Block "crypto", "rage politics", and more from your X feed using AI

**原文链接**: [https://github.com/imbue-ai/bouncer](https://github.com/imbue-ai/bouncer)

生成摘要时出错

---

## 66. AI could be the end of the digital wave, not the next big thing

**原文标题**: AI could be the end of the digital wave, not the next big thing

**原文链接**: [https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

生成摘要时出错

---

## 67. Show HN: Claudraband – Claude Code for the Power User

**原文标题**: Show HN: Claudraband – Claude Code for the Power User

**原文链接**: [https://github.com/halfwhey/claudraband](https://github.com/halfwhey/claudraband)

生成摘要时出错

---

## 68. Haunt, the 70s text adventure game, is now playable on a website

**原文标题**: Haunt, the 70s text adventure game, is now playable on a website

**原文链接**: [https://haunt.madebywindmill.com](https://haunt.madebywindmill.com)

生成摘要时出错

---

## 69. Struggling to heat your home? How about 500 Raspberry Pi units? (2025)

**原文标题**: Struggling to heat your home? How about 500 Raspberry Pi units? (2025)

**原文链接**: [https://www.theregister.com/2025/10/03/thermify_heathub_raspberry_pi/](https://www.theregister.com/2025/10/03/thermify_heathub_raspberry_pi/)

生成摘要时出错

---

## 70. The End of Eleventy

**原文标题**: The End of Eleventy

**原文链接**: [https://brennan.day/the-end-of-eleventy/](https://brennan.day/the-end-of-eleventy/)

生成摘要时出错

---

## 71. I run multiple $10K MRR companies on a $20/month tech stack

**原文标题**: I run multiple $10K MRR companies on a $20/month tech stack

**原文链接**: [https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack](https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack)

生成摘要时出错

---

## 72. An Interview with Pat Gelsinger

**原文标题**: An Interview with Pat Gelsinger

**原文链接**: [https://morethanmoore.substack.com/p/an-interview-with-pat-gelsinger-2026](https://morethanmoore.substack.com/p/an-interview-with-pat-gelsinger-2026)

生成摘要时出错

---

## 73. Nordics and Estonia rolling out offline card payment backup in case internet cut

**原文标题**: Nordics and Estonia rolling out offline card payment backup in case internet cut

**原文链接**: [https://www.reuters.com/business/finance/nordics-estonia-plan-offline-card-payment-back-up-if-internet-cut-2025-05-07/](https://www.reuters.com/business/finance/nordics-estonia-plan-offline-card-payment-back-up-if-internet-cut-2025-05-07/)

生成摘要时出错

---

## 74. 2025 Tesla Cybertruck: Regular Car Reviews [video]

**原文标题**: 2025 Tesla Cybertruck: Regular Car Reviews [video]

**原文链接**: [https://www.youtube.com/watch?v=L3oO510dyVI](https://www.youtube.com/watch?v=L3oO510dyVI)

生成摘要时出错

---

## 75. IrDA

**原文标题**: IrDA

**原文链接**: [https://computer.rip/2026-04-11-IrDA.html](https://computer.rip/2026-04-11-IrDA.html)

生成摘要时出错

---

## 76. Small models also found the vulnerabilities that Mythos found

**原文标题**: Small models also found the vulnerabilities that Mythos found

**原文链接**: [https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

生成摘要时出错

---

## 77. The Problem That Built an Industry

**原文标题**: The Problem That Built an Industry

**原文链接**: [https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/](https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/)

生成摘要时出错

---

## 78. The Triumph of Stupidity (1933)

**原文标题**: The Triumph of Stupidity (1933)

**原文链接**: [https://russell-j.com/0583TS.HTM](https://russell-j.com/0583TS.HTM)

生成摘要时出错

---

## 79. 1D Chess

**原文标题**: 1D Chess

**原文链接**: [https://rowan441.github.io/1dchess/chess.html](https://rowan441.github.io/1dchess/chess.html)

**1D Chess** is a simplified variant of the classic game that reduces play to a single dimension. Originally described by Martin Gardner in the July 1980 issue of *Scientific American*, this version strips away the complexity of a 2D grid while maintaining core strategic elements.

**Pieces and Movement:**
The game utilizes three piece types with specific movement rules:
*   **King:** Moves one square in either direction.
*   **Knight:** Moves exactly two squares forward or backward, jumping over any intervening pieces.
*   **Rook:** Moves any number of squares in either direction along the line.

**Objective and Rules:**
The goal is to achieve **checkmate**, which occurs when the opponent's king is under attack and has no legal moves to escape. The game follows standard chess logic regarding draws, including:
*   **Stalemate:** A player has no legal moves but is not in check.
*   **Three-Fold Repetition:** The same board position occurs three times.
*   **Insufficient Material:** Only kings remain on the board, making checkmate impossible.

While playing against an AI can be deceptively difficult, the game is mathematically solved; there is a forced win for White using a specific five-move sequence involving the Knight and Rook. 1D Chess serves as both a playable game and a mathematical exercise in reducing complex systems to their most fundamental components.

---

## 80. Tech valuations are back to pre-AI boom levels

**原文标题**: Tech valuations are back to pre-AI boom levels

**原文链接**: [https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

生成摘要时出错

---

## 81. Every plane you see in the sky – you can now follow it from the cockpit in 3D

**原文标题**: Every plane you see in the sky – you can now follow it from the cockpit in 3D

**原文链接**: [https://flight-viz.com/cockpit.html?lat=40.64&lon=-73.78&alt=3000&hdg=220&spd=130&cs=DAL123](https://flight-viz.com/cockpit.html?lat=40.64&lon=-73.78&alt=3000&hdg=220&spd=130&cs=DAL123)

生成摘要时出错

---

## 82. Keeping a Postgres Queue Healthy

**原文标题**: Keeping a Postgres Queue Healthy

**原文链接**: [https://planetscale.com/blog/keeping-a-postgres-queue-healthy](https://planetscale.com/blog/keeping-a-postgres-queue-healthy)

生成摘要时出错

---

## 83. High-Level Rust: Getting 80% of the Benefits with 20% of the Pain

**原文标题**: High-Level Rust: Getting 80% of the Benefits with 20% of the Pain

**原文链接**: [https://hamy.xyz/blog/2026-01_high-level-rust](https://hamy.xyz/blog/2026-01_high-level-rust)

生成摘要时出错

---

## 84. The Closing of the Frontier

**原文标题**: The Closing of the Frontier

**原文链接**: [https://tanyaverma.sh/2026/04/10/closing-of-the-frontier.html](https://tanyaverma.sh/2026/04/10/closing-of-the-frontier.html)

生成摘要时出错

---

## 85. What have been the greatest intellectual achievements? (2017)

**原文标题**: What have been the greatest intellectual achievements? (2017)

**原文链接**: [https://www.thinkingcomplete.com/2017/09/what-have-been-greatest-intellectual.html](https://www.thinkingcomplete.com/2017/09/what-have-been-greatest-intellectual.html)

生成摘要时出错

---

## 86. Now is the best time to write code by hand

**原文标题**: Now is the best time to write code by hand

**原文链接**: [https://sitebloom.ch/writing/now-is-the-best-time-to-write-code-by-hand/](https://sitebloom.ch/writing/now-is-the-best-time-to-write-code-by-hand/)

生成摘要时出错

---

## 87. The APL programming language source code (2012)

**原文标题**: The APL programming language source code (2012)

**原文链接**: [https://computerhistory.org/blog/the-apl-programming-language-source-code/](https://computerhistory.org/blog/the-apl-programming-language-source-code/)

生成摘要时出错

---

## 88. European AI. A playbook to own it

**原文标题**: European AI. A playbook to own it

**原文链接**: [https://europe.mistral.ai/](https://europe.mistral.ai/)

生成摘要时出错

---

## 89. Starfling: A one-tap endless orbital slingshot game in a single HTML file

**原文标题**: Starfling: A one-tap endless orbital slingshot game in a single HTML file

**原文链接**: [https://playstarfling.com](https://playstarfling.com)

生成摘要时出错

---

## 90. Compute iOS XNU offset from kernel cache

**原文标题**: Compute iOS XNU offset from kernel cache

**原文链接**: [https://blog.reversesociety.co/blog/2026/kernel-rw-not-enough-extract-offsets-from-xnu-kernelcaches](https://blog.reversesociety.co/blog/2026/kernel-rw-not-enough-extract-offsets-from-xnu-kernelcaches)

生成摘要时出错

---

## 91. I went to America's worst national parks so you don't have to

**原文标题**: I went to America's worst national parks so you don't have to

**原文链接**: [https://substack.com/home/post/p-193626949](https://substack.com/home/post/p-193626949)

生成摘要时出错

---

## 92. They See Your Photos

**原文标题**: They See Your Photos

**原文链接**: [https://theyseeyourphotos.com/](https://theyseeyourphotos.com/)

生成摘要时出错

---

## 93. 447 TB/cm² at zero retention energy – atomic-scale memory on fluorographane

**原文标题**: 447 TB/cm² at zero retention energy – atomic-scale memory on fluorographane

**原文链接**: [https://zenodo.org/records/19513269](https://zenodo.org/records/19513269)

生成摘要时出错

---

## 94. How Passive Radar Works

**原文标题**: How Passive Radar Works

**原文链接**: [https://www.passiveradar.com/how-passive-radar-works/](https://www.passiveradar.com/how-passive-radar-works/)

生成摘要时出错

---

## 95. Productive Procrastination

**原文标题**: Productive Procrastination

**原文链接**: [https://www.maxvanijsselmuiden.nl/blog/productive-procrastination/](https://www.maxvanijsselmuiden.nl/blog/productive-procrastination/)

生成摘要时出错

---

## 96. South Korea introduces universal basic mobile data access

**原文标题**: South Korea introduces universal basic mobile data access

**原文链接**: [https://www.theregister.com/2026/04/10/south_korea_data_access_universal/](https://www.theregister.com/2026/04/10/south_korea_data_access_universal/)

生成摘要时出错

---

## 97. Palantir Stock Continues to Fall. Not Even the President Can Erase the Losses

**原文标题**: Palantir Stock Continues to Fall. Not Even the President Can Erase the Losses

**原文链接**: [https://www.barrons.com/articles/palantir-stock-price-president-trump-anthropic-7313031c](https://www.barrons.com/articles/palantir-stock-price-president-trump-anthropic-7313031c)

生成摘要时出错

---

## 98. Cirrus Labs to join OpenAI

**原文标题**: Cirrus Labs to join OpenAI

**原文链接**: [https://cirruslabs.org/](https://cirruslabs.org/)

生成摘要时出错

---

## 99. Dark Castle

**原文标题**: Dark Castle

**原文链接**: [https://darkcastle.co.uk/](https://darkcastle.co.uk/)

生成摘要时出错

---

## 100. France's government is ditching Windows for Linux, says US tech a strategic risk

**原文标题**: France's government is ditching Windows for Linux, says US tech a strategic risk

**原文链接**: [https://www.xda-developers.com/frances-government-ditching-windows-for-linux/](https://www.xda-developers.com/frances-government-ditching-windows-for-linux/)

生成摘要时出错

---

