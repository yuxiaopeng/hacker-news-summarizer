# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-13.md)

*最后自动更新时间: 2026-04-13 18:30:33*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 2 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 3 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 4 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 5 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 6 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 7 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 8 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 9 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 10 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 11 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 12 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 13 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 14 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 15 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 16 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 17 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 18 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 19 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 20 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 21 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 22 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 23 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 24 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 25 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 26 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 27 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 28 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 29 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 30 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 31 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 32 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 33 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 34 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 35 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 36 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 37 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 38 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 39 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 40 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 41 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 42 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 43 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 44 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 45 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 46 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 47 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 48 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 49 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 50 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 51 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 52 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 53 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 54 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 55 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 56 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 57 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 58 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 59 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 60 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 61 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 62 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 63 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 64 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 65 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 66 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 67 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 68 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 69 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 70 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 71 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 72 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 73 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 74 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 75 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 76 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 77 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 78 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 79 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 80 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 81 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 82 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 83 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 84 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 85 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 86 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 87 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 88 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 89 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 90 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 91 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 92 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 93 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 94 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 95 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 96 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 97 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 98 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 99 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 100 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 101 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 102 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 103 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 104 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 105 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 106 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 107 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 108 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 109 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 110 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 111 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 112 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 113 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 114 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 115 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 116 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 117 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 118 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 119 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 120 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 121 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 122 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 123 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 124 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 125 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 126 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 127 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 128 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 129 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 130 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 131 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 132 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 133 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 134 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 135 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 136 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 137 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 138 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 139 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 140 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 141 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 142 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 143 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 144 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 145 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 146 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 147 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 148 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 149 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 150 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 151 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 152 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 153 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 154 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 155 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 156 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 157 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 158 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 159 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 160 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 161 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 162 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 163 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 164 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 165 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 166 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 167 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 168 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 169 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 170 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 171 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 172 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 173 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 174 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 175 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 176 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 177 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 178 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 179 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 180 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 181 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 182 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 183 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 184 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 185 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 186 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 187 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 188 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 189 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 190 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 191 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 192 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 193 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 194 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 195 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 196 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 197 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 198 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 199 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 200 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 201 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 202 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 203 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 204 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 205 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 206 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 207 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 208 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 209 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 210 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 211 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 212 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 213 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 214 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 215 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 216 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 217 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 218 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 219 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 220 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 221 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 222 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 223 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 224 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 225 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 226 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 227 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 228 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 229 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 230 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 231 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 232 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 233 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 234 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 235 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 236 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 237 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 238 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 239 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 240 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 241 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 242 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 243 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 244 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 245 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 246 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 247 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 248 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 249 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 250 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 251 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 252 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 253 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 254 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 255 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 256 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 257 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 258 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 259 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 260 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 261 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 262 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 263 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 264 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 265 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 266 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 267 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 268 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 269 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 270 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 271 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 272 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 273 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 274 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 275 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 276 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 277 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 278 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 279 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 280 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 281 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 282 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 283 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 284 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 285 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 286 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 287 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 288 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 289 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 290 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 291 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 292 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 293 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 294 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 295 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 296 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 297 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 298 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 299 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 300 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 301 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 302 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 303 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 304 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 305 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 306 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 307 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 308 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 309 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 310 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 311 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 312 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 313 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 314 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 315 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 316 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 317 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 318 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 319 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 320 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 321 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 322 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 323 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 324 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 325 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 326 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 327 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 328 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 329 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 330 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 331 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 332 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 333 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 334 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 335 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 336 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 337 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 338 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 339 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 340 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 341 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 342 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 343 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 344 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 345 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 346 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 347 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 348 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 349 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 350 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 351 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 352 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 353 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 354 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 355 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 356 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 357 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 358 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 359 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 360 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 361 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 362 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 363 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 364 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 365 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 366 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 367 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 368 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 369 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 370 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 371 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 372 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 373 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 374 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 375 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 376 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 377 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 378 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 379 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 380 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 381 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 382 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 383 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 384 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 385 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 386 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 387 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 388 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 389 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
